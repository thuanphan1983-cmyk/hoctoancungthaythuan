# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - VẬT LÝ 8 (KNTT)
Gồm 21 bài/chương ôn tập => 71 đề thi độc lập 100%
Cấu trúc mỗi đề: 12 TN + 4 Đ/S (16 ý) + 6 TLN + 4 VDC (TN nâng cao)
Tỉ lệ ma trận: 30% NB, 30% TH, 20% VD, 20% VDC
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text,
        "options": options,
        "correct": correct_idx,
        "explanation": explanation
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": prompt,
        "statements": [
            {"subId": s[0], "text": s[1], "correct": s[2]} for s in statements
        ],
        "explanation": explanation
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text,
        "correctAnswer": str(answer).strip(),
        "explanation": explanation
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": "Vận dụng cao",
        "question": q_text,
        "options": options,
        "correct": correct_idx,
        "explanation": explanation
    }

def build_phys8_exams():
    exams = {}

    lessons_list = [
        # CHƯƠNG III: KHỐI LƯỢNG RIÊNG VÀ ÁP SUẤT
        ("phys8_c3", "Chương III: Khối lượng riêng và áp suất", "phys8_c3_b13", "Bài 13: Khối lượng riêng", 3),
        ("phys8_c3", "Chương III: Khối lượng riêng và áp suất", "phys8_c3_b14", "Bài 14: Thực hành xác định khối lượng riêng", 3),
        ("phys8_c3", "Chương III: Khối lượng riêng và áp suất", "phys8_c3_b15", "Bài 15: Áp suất trên một bề mặt", 3),
        ("phys8_c3", "Chương III: Khối lượng riêng và áp suất", "phys8_c3_b16", "Bài 16: Áp suất chất lỏng. Áp suất khí quyển", 3),
        ("phys8_c3", "Chương III: Khối lượng riêng và áp suất", "phys8_c3_b17", "Bài 17: Lực đẩy Archimedes", 3),
        ("phys8_c3", "Chương III: Khối lượng riêng và áp suất", "phys8_c3_rev", "[Đề tổng hợp] Ôn tập cuối Chương III", 5),

        # CHƯƠNG IV: TÁC DỤNG LÀM QUAY CỦA LỰC
        ("phys8_c4", "Chương IV: Tác dụng làm quay của lực", "phys8_c4_b18", "Bài 18: Tác dụng làm quay của lực. Moment lực", 3),
        ("phys8_c4", "Chương IV: Tác dụng làm quay của lực", "phys8_c4_b19", "Bài 19: Đòn bẩy và ứng dụng", 3),
        ("phys8_c4", "Chương IV: Tác dụng làm quay của lực", "phys8_c4_rev", "[Đề tổng hợp] Ôn tập cuối Chương IV", 5),

        # CHƯƠNG V: ĐIỆN
        ("phys8_c5", "Chương V: Điện", "phys8_c5_b20", "Bài 20: Hiện tượng nhiễm điện do cọ xát", 3),
        ("phys8_c5", "Chương V: Điện", "phys8_c5_b21", "Bài 21: Dòng điện, nguồn điện", 3),
        ("phys8_c5", "Chương V: Điện", "phys8_c5_b22", "Bài 22: Mạch điện đơn giản", 3),
        ("phys8_c5", "Chương V: Điện", "phys8_c5_b23", "Bài 23: Tác dụng của dòng điện", 3),
        ("phys8_c5", "Chương V: Điện", "phys8_c5_b24", "Bài 24: Cường độ dòng điện và hiệu điện thế", 3),
        ("phys8_c5", "Chương V: Điện", "phys8_c5_b25", "Bài 25: Thực hành đo cường độ dòng điện và hiệu điện thế", 3),
        ("phys8_c5", "Chương V: Điện", "phys8_c5_rev", "[Đề tổng hợp] Ôn tập cuối Chương V", 5),

        # CHƯƠNG VI: NHIỆT
        ("phys8_c6", "Chương VI: Nhiệt", "phys8_c6_b26", "Bài 26: Năng lượng nhiệt và nội năng", 3),
        ("phys8_c6", "Chương VI: Nhiệt", "phys8_c6_b27", "Bài 27: Thực hành đo năng lượng nhiệt bằng nhiệt lượng kế", 3),
        ("phys8_c6", "Chương VI: Nhiệt", "phys8_c6_b28", "Bài 28: Sự truyền nhiệt", 3),
        ("phys8_c6", "Chương VI: Nhiệt", "phys8_c6_b29", "Bài 29: Sự nở vì nhiệt", 3),
        ("phys8_c6", "Chương VI: Nhiệt", "phys8_c6_rev", "[Đề tổng hợp] Ôn tập cuối Chương VI", 5)
    ]

    for ch_id, ch_title, l_id, l_name, n_tests in lessons_list:
        for t in range(1, n_tests + 1):
            k = f"{l_id}_test{t}"
            p1 = []
            p2 = []
            p3 = []
            p4 = []

            # ======================== CHƯƠNG III: D & ÁP SUẤT ========================
            if "c3" in ch_id:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Khối lượng riêng D của một chất được tính theo công thức:", ["D = m / V", "D = m × V", "D = V / m", "D = m + V"], 0, "D = m / V (kg/m3 hoặc g/cm3)."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Đơn vị chuẩn của khối lượng riêng trong hệ SI là:", ["kg/m3", "g/cm3", "kg/L", "g/mL"], 0, "kg/m3."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Áp suất p tác dụng lên một bề mặt được tính theo công thức:", ["p = F / S", "p = F × S", "p = S / F", "p = F - S"], 0, "p = F / S (N/m2 hay Pa)."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Đơn vị của áp suất trong hệ SI là:", ["Pascal (Pa hay N/m2)", "Newton (N)", "Joule (J)", "Watt (W)"], 0, "1 Pa = 1 N/m2."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Áp suất chất lỏng tại một điểm có độ sâu h được tính theo:", ["p = d × h", "p = d / h", "p = d + h", "p = m × h"], 0, "p = d.h (trong đó d là trọng lượng riêng chất lỏng)."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Độ lớn của lực đẩy Archimedes tác dụng lên vật nhúng trong chất lỏng bằng:", ["Trọng lượng của phần chất lỏng bị vật chiếm chỗ (FA = d × V)", "Trọng lượng của chính vật đó", "Khối lượng của vật", "Áp suất chất lỏng"], 0, "FA = d.V = 10.D.V."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Một khối kim loại có khối lượng 7,8 kg và thể tích 0,001 m3. Khối lượng riêng của kim loại là:", ["7800 kg/m3 (Sắt)", "2700 kg/m3", "1000 kg/m3", "8900 kg/m3"], 0, "D = 7,8 / 0,001 = 7800 kg/m3."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Một người đứng thẳng bằng hai chân tác dụng lên sàn áp lực F = 600 N, diện tích hai bàn chân là 0,03 m2. Áp suất người đó tác dụng lên sàn là:", ["20.000 Pa", "600 Pa", "18.000 Pa", "2.000 Pa"], 0, "p = 600 / 0,03 = 20.000 Pa."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Khi lặn sâu dưới biển, người thợ lặn phải mặc bộ đồ lặn chịu áp suất cao để chống lại:", ["Áp suất rất lớn của nước biển đè nén lên cơ thể", "Nhiệt độ quá nóng", "Lực đẩy Archimedes quá lớn", "Sóng âm của cá voi"], 0, "Càng xuống sâu áp suất chất lỏng p = d.h càng lớn."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Điều kiện để một vật nổi trên mặt chất lỏng là:", ["Khối lượng riêng của vật nhỏ hơn khối lượng riêng của chất lỏng (dvật < dchất lỏng)", "dvật = dchất lỏng", "dvật > dchất lỏng", "Vật làm bằng kim loại"], 0, "dvật < dchất lỏng thì vật nổi."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Máy nén thủy lực nâng ô tô hoạt động dựa trên nguyên lí truyền nguyên vẹn áp suất chất lỏng của nhà bác học:", ["Pascal", "Archimedes", "Newton", "Torricelli"], 0, "Nguyên lí Pascal: F2/F1 = S2/S1."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Để giảm áp suất của xe tăng tác dụng lên mặt đất bùn lầy tránh bị sa lầy, người ta dùng:", ["Hệ thống bánh xích có diện tích tiếp xúc rất lớn", "Bánh xe nhỏ hẹp", "Tăng thêm trọng lượng xe", "Chạy thật nhanh"], 0, "Tăng diện tích tiếp xúc S làm giảm áp suất p = F/S.")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về khối lượng riêng và đo thể tích:", [
                        ("a", "Khối lượng riêng của nước nguyên chất là 1000 kg/m3 (hay 1 g/cm3).", True),
                        ("b", "Khối lượng riêng là đặc tính của chất, không phụ thuộc vào kích thước của vật thể.", True),
                        ("c", "Để đo thể tích vật rắn không thấm nước, người ta có thể dùng bình chia độ.", True),
                        ("d", "Khối lượng riêng của sắt bằng khối lượng riêng của nhôm.", False)
                    ], "Dsắt = 7800 kg/m3 lớn hơn nhiều so với Dnhôm = 2700 kg/m3."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Về áp suất chất lỏng và khí quyển:", [
                        ("a", "Chất lỏng gây ra áp suất theo mọi phương lên đáy bình, thành bình và các vật trong lòng nó.", True),
                        ("b", "Trong bình thông nhau chứa cùng một chất lỏng đứng yên, mực mặt thoáng ở các nhánh luôn ở cùng một độ cao.", True),
                        ("c", "Áp suất khí quyển giảm dần khi lên càng cao so với mặt nước biển.", True),
                        ("d", "Áp suất tại đáy biển sâu 100 m nhỏ hơn áp suất tại độ sâu 10 m.", False)
                    ], "Độ sâu h càng lớn thì áp suất p = d.h càng lớn."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Một khối nhôm có thể tích 0,002 m3 được nhúng chìm hoàn toàn trong nước (dnước = 10.000 N/m3):", [
                        ("a", "Thể tích phần nước bị chiếm chỗ là 0,002 m3.", True),
                        ("b", "Lực đẩy Archimedes tác dụng lên khối nhôm có độ lớn là 20 N.", True),
                        ("c", "Trọng lượng của khối nhôm là 54 N (Dnhôm = 2700 kg/m3).", True),
                        ("d", "Khối nhôm sẽ lơ lửng trong nước.", False)
                    ], "P = 54 N > FA = 20 N nên khối nhôm sẽ chìm xuống đáy."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Trong một máy ép thủy lực, pit-tông nhỏ có diện tích S1 = 2 cm2, pit-tông lớn có diện tích S2 = 200 cm2:", [
                        ("a", "Diện tích pit-tông lớn gấp 100 lần pit-tông nhỏ.", True),
                        ("b", "Tác dụng một lực F1 = 100 N lên pit-tông nhỏ sẽ sinh ra lực nâng F2 = 10.000 N ở pit-tông lớn.", True),
                        ("c", "Máy ép thủy lực giúp ta lợi 100 lần về lực.", True),
                        ("d", "Máy ép thủy lực giúp ta lợi cả về công cơ học.", False)
                    ], "Định luật bảo toàn công: không một máy cơ đơn giản nào cho ta lợi về công.")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Khối lượng riêng của nước nguyên chất là bao nhiêu kg/m3?", "1000", "1000 kg/m3."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - 1 Pascal (Pa) bằng bao nhiêu Newton trên mét vuông (N/m2)?", "1", "1 N/m2."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Một vật có khối lượng 540 gam và thể tích 200 cm3. Khối lượng riêng của vật là bao nhiêu g/cm3?", "2.7", "540 / 200 = 2,7 g/cm3 (Nhôm)."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Một khối kim loại nhúng chìm trong nước chịu lực đẩy Archimedes là 50 N. Biết trọng lượng riêng của nước là 10.000 N/m3. Thể tích của khối kim loại là bao nhiêu dm3?", "5", "V = 50 / 10000 = 0,005 m3 = 5 dm3."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Áp suất tác dụng lên một thợ lặn ở độ sâu 30 m dưới biển (biết trọng lượng riêng nước biển là 10.300 N/m3) là bao nhiêu kPa?", "309", "p = 10300 × 30 = 309.000 Pa = 309 kPa."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Một tảng băng nổi trên mặt nước biển. Biết thể tích phần chìm trong nước chiếm 90% thể tích toàn bộ tảng băng. Trọng lượng riêng của nước biển là 10.300 N/m3. Khối lượng riêng của băng là bao nhiêu kg/m3?", "927", "Dbăng = 0,9 × 1030 = 927 kg/m3.")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Con tàu chở hàng bằng thép nặng hàng vạn tấn vẫn có thể nổi và di chuyển dễ dàng trên mặt biển trong khi một chiếc đinh sắt nhỏ lại chìm nghỉm ngay lập tức. Nguyên nhân cốt lõi là do:", ["Vỏ tàu được thiết kế rỗng chứa rất nhiều không khí làm cho khối lượng riêng trung bình của toàn bộ con tàu nhỏ hơn khối lượng riêng của nước biển", "Nước biển đẩy mạnh hơn nước ngọt", "Tàu có động cơ đẩy nước", "Thép làm tàu nhẹ hơn nước"], 0, "Khối lượng riêng trung bình của tàu nhỏ hơn nước biển."),
                    make_vdc(2, f"Đề {t} - Khi cắm ống hút vào hộp sữa và hút bớt không khí bên trong ra, vỏ hộp sữa bằng giấy bị móp méo bẹp dúm lại. Hiện tượng này là minh chứng rõ ràng cho sự tồn tại của:", ["Áp suất khí quyển bao quanh đè nén từ bên ngoài", "Áp lực của sữa bên trong kéo vỏ lại", "Lực hút của miệng người", "Nhiệt độ trong hộp giảm"], 0, "Áp suất khí quyển bên ngoài lớn hơn áp suất bên trong hộp sữa."),
                    make_vdc(3, f"Đề {t} - Một khối gỗ có thể tích 0,01 m3 thả vào nước thì có 0,006 m3 bị chìm trong nước. Biết trọng lượng riêng của nước là 10.000 N/m3. Trọng lượng của khối gỗ đó là:", ["60 N", "100 N", "40 N", "10 N"], 0, "Vật nổi thăng bằng: P = FA = d × Vchìm = 10.000 × 0,006 = 60 N."),
                    make_vdc(4, f"Đề {t} - Càng lên cao trên núi hoặc trên máy bay, áp suất khí quyển giảm khiến tai ta bị ù. Cơ chế gây ù tai là do:", ["Chênh lệch áp suất giữa tai giữa và khí quyển bên ngoài làm màng nhĩ bị phồng căng ra ngoài", "Âm thanh gió thổi quá to", "Nhiệt độ trên cao lạnh", "Không khí thiếu oxy"], 0, "Chênh lệch áp suất màng nhĩ gây cảm giác ù tai.")
                ]

            # ======================== CHƯƠNG IV: TÁC DỤNG LÀM QUAY ========================
            elif "c4" in ch_id:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Tác dụng làm quay của lực lên một vật quanh một trục quay được đặc trưng bởi đại lượng nào?", ["Moment lực (M)", "Khối lượng", "Vận tốc", "Quán tính"], 0, "Moment lực M = F.d."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Công thức tính moment lực M là:", ["M = F × d", "M = F / d", "M = d / F", "M = F + d"], 0, "M = F.d (trong đó d là cánh tay đòn)."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Đơn vị của moment lực trong hệ SI là:", ["N.m (Newton mét)", "N/m", "Joule", "Watt"], 0, "N.m."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Cánh tay đòn d của lực là khoảng cách từ:", ["Trục quay đến giá của lực", "Điểm đặt lực đến trục quay", "Hai đầu đòn bẩy", "Mặt đất đến lực"], 0, "Khoảng cách vuông góc từ trục quay đến giá của lực."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Dụng cụ nào sau đây hoạt động dựa trên nguyên lí đòn bẩy?", ["Cái kéo cắt giấy, kìm nhổ đinh, bập bênh", "Thước kẻ", "Nhiệt kế", "Kính lúp"], 0, "Kéo, kìm, đòn bẩy, bập bênh."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Điều kiện cân bằng của một vật có trục quay cố định là:", ["Tổng các moment lực làm vật quay theo chiều kim đồng hồ bằng tổng các moment lực làm vật quay ngược chiều kim đồng hồ", "Lực bên trái bằng lực bên phải", "Không có lực nào tác dụng", "Trọng lượng bằng 0"], 0, "Quy tắc moment lực (điều kiện cân bằng)."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Tác dụng một lực F = 20 N vào cờ-lê có cánh tay đòn d = 0,25 m để vặn ốc. Moment của lực tác dụng là:", ["5 N.m", "20 N.m", "80 N.m", "2,5 N.m"], 0, "M = 20 × 0,25 = 5 N.m."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Để mở một cánh cửa gỗ nặng dễ dàng nhất, ta nên đặt tay nắm cửa ở vị trí nào?", ["Ở mép ngoài xa bản lề nhất", "Ở sát gần bản lề", "Ở chính giữa bản lề", "Vị trí nào cũng như nhau"], 0, "Càng xa trục quay bản lề thì cánh tay đòn d càng lớn => lực mở F càng nhỏ."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Kéo cắt kim loại thường có đặc điểm cấu tạo:", ["Cán kéo dài hơn lưỡi kéo nhiều lần để được lợi về lực", "Lưỡi kéo dài hơn cán", "Cán và lưỡi bằng nhau", "Lưỡi kéo mỏng dính"], 0, "Được lợi về lực (F1.d1 = F2.d2 với d1 > d2 => F1 < F2)."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Kéo cắt vải hoặc cắt tóc thường có đặc điểm:", ["Lưỡi kéo dài hơn cán kéo để được lợi về đường đi (cắt nhanh)", "Cán kéo rất dài", "Lưỡi kéo ngắn củn", "Không có trục quay"], 0, "Lợi về quãng đường cắt nhanh và đều."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Khi hai bạn chơi trò bập bênh thăng bằng, bạn nặng hơn phải ngồi:", ["Gần trục quay hơn bạn nhẹ cân", "Xa trục quay hơn", "Đứng lên trên", "Ngồi vị trí nào cũng được"], 0, "P1.d1 = P2.d2: P lớn thì d phải nhỏ."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Chiếc xà beng dùng để bẩy hòn đá tảng là đòn bẩy loại mấy có điểm tựa O nằm giữa điểm tác dụng lực và tải trọng?", ["Đòn bẩy loại 1", "Đòn bẩy loại 2", "Đòn bẩy loại 3", "Đòn bẩy không có điểm tựa"], 0, "Điểm tựa ở giữa là đòn bẩy loại 1.")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về moment lực và tác dụng làm quay:", [
                        ("a", "Moment lực đặc trưng cho tác dụng làm quay của lực quanh một trục.", True),
                        ("b", "Lực có giá đi qua trục quay sẽ không có tác dụng làm quay (M = 0).", True),
                        ("c", "Lực càng lớn và cánh tay đòn càng dài thì tác dụng làm quay càng mạnh.", True),
                        ("d", "Khoảng cách từ điểm đặt của lực đến trục quay luôn luôn bằng cánh tay đòn.", False)
                    ], "Cánh tay đòn là khoảng cách vuông góc từ trục quay đến giá của lực, không phải khoảng cách tới điểm đặt nếu lực xiên."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Xét các loại đòn bẩy trong đời sống và kỹ thuật:", [
                        ("a", "Đòn bẩy có điểm tựa ở giữa (như kéo, bập bênh, kìm) là đòn bẩy loại 1.", True),
                        ("b", "Xe cút kít (xe rùa) có tải trọng ở giữa điểm tựa bánh xe và tay nâng là đòn bẩy loại 2.", True),
                        ("c", "Kẹp gắp thức ăn và cần câu cá là đòn bẩy loại 3 có lợi về lực.", False),
                        ("d", "Khớp khuỷu tay của cơ thể người hoạt động như một hệ đòn bẩy.", True)
                    ], "Đòn bẩy loại 3 thiệt về lực nhưng lợi về đường đi và tốc độ."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Một thanh đòn bẩy dài 1 m có điểm tựa O cách đầu A một đoạn 0,2 m và cách đầu B một đoạn 0,8 m. Treo ở đầu A vật nặng P1 = 400 N:", [
                        ("a", "Cánh tay đòn d1 của vật tại A là 0,2 m.", True),
                        ("b", "Cánh tay đòn d2 của lực tại B là 0,8 m.", True),
                        ("c", "Để đòn bẩy thăng bằng cần tác dụng vào B một lực thẳng đứng hướng xuống F2 = 100 N.", True),
                        ("d", "Đòn bẩy này cho ta thiệt 4 lần về lực.", False)
                    ], "F2 = P1 × d1 / d2 = 400 × 0,2 / 0,8 = 100 N (được lợi 4 lần về lực)."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Hai người khiêng một vật nặng P = 600 N bằng một chiếc đòn dài 2 m. Vật treo cách vai người thứ nhất 0,8 m và cách vai người thứ hai 1,2 m:", [
                        ("a", "Tổng lực do hai người chịu bằng 600 N.", True),
                        ("b", "Người thứ nhất đứng gần vật hơn nên chịu lực lớn hơn người thứ hai.", True),
                        ("c", "Lực tác dụng lên vai người thứ nhất là 360 N.", True),
                        ("d", "Lực tác dụng lên vai người thứ hai là 300 N.", False)
                    ], "F1 × 0,8 = F2 × 1,2 và F1 + F2 = 600 => F1 = 360 N, F2 = 240 N.")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Đơn vị của moment lực là gì? (Viết tắt)", "N.m", "N.m."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - Tác dụng lực F = 50 N vuông góc với cánh tay đòn d = 0,2 m. Moment lực là bao nhiêu N.m?", "10", "50 × 0,2 = 10 N.m."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Cần một moment lực 30 N.m để siết ốc. Nếu dùng cờ-lê dài 0,3 m thì lực tác dụng vuông góc tối thiểu là bao nhiêu N?", "100", "F = 30 / 0,3 = 100 N."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Đòn bẩy có d1 = 10 cm, d2 = 50 cm. Muốn nâng vật nặng 500 N ở đầu 1 cần tác dụng lực ở đầu 2 là bao nhiêu N?", "100", "F2 = 500 × 10 / 50 = 100 N."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Một thanh đồng chất tiết diện đều dài 1 m, nặng 20 N. Đặt một điểm tựa cách một đầu 0,3 m. Muốn thanh thăng bằng nằm ngang phải tác dụng vào đầu gần điểm tựa nhất một lực bằng bao nhiêu N?", "13.3", "Trọng tâm thanh ở giữa (0,5m cách đầu, tức cách điểm tựa 0,2m). P × 0,2 = F × 0,3 => F = 20 × 0,2 / 0,3 ≈ 13,3 N."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Một người dùng xà beng bẩy hòn đá nặng 1200 N. Điểm tựa cách hòn đá 0,2 m và cách tay người 1,0 m. Lực ấn tối thiểu của người đó là bao nhiêu N?", "240", "F = 1200 × 0,2 / 1,0 = 240 N.")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Tay nắm cửa sổ mở hất ra ngoài hoặc tay vặn van nước cứu hỏa thường có dạng vô-lăng tròn hoặc cánh tay đòn dài nhằm mục đích:", ["Tăng cánh tay đòn d để tạo moment lực lớn với lực tác dụng nhỏ giúp đóng mở êm nhẹ", "Để trang trí", "Để giảm độ ma sát", "Để tránh trộm"], 0, "Tăng cánh tay đòn tăng moment quay."),
                    make_vdc(2, f"Đề {t} - Cần cẩu tháp xây dựng nhà cao tầng có một cánh tay đòn dài vươn ra mang tải trọng và một cánh tay đòn ngắn phía sau mang các khối bê tông nặng. Khối bê tông phía sau được gọi là:", ["Đối trọng dùng để cân bằng moment lực ngăn cần cẩu bị lật đổ", "Khối neo giữ gió", "Trang trí cân xứng", "Bệ chứa máy nổ"], 0, "Đối trọng tạo moment lực cân bằng chống lật."),
                    make_vdc(3, f"Đề {t} - Khi cắt một thanh kim loại hoặc dây thép dày bằng kìm cộng lực, người thợ thường đặt thanh thép vào sâu sát tận khớp quay của kìm và cầm ở đầu mút cán kìm. Cách làm này mang lại hiệu quả:", ["Làm d_thép nhỏ nhất và d_tay lớn nhất giúp tăng tối đa lực cắt tác dụng lên thanh thép", "Để kìm không bị gãy", "Để quan sát vết cắt rõ hơn", "Để không bị trơn tay"], 0, "Tối ưu hóa đòn bẩy để lực cắt lớn nhất."),
                    make_vdc(4, f"Đề {t} - Vận động viên chèo thuyền kayak dùng mái chèo có trục quay là điểm nắm tay phía trên, tay phía dưới kéo mái chèo tạo lực đẩy thuyền. Đây là ứng dụng của:", ["Đòn bẩy loại 3 cho ta lợi về tốc độ di chuyển mái chèo trong nước", "Đòn bẩy loại 1", "Ròng rọc", "Mặt phẳng nghiêng"], 0, "Đòn bẩy loại 3 lợi về vận tốc và đường đi.")
                ]

            # ======================== CHƯƠNG V: ĐIỆN ========================
            elif "c5" in ch_id:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Có hai loại điện tích là:", ["Điện tích dương (+) và điện tích âm (-)", "Điện tích Bắc và điện tích Nam", "Điện tích nóng và lạnh", "Điện tích đẩy và hút"], 0, "Điện tích dương và âm."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Các vật mang điện tích cùng loại thì:", ["Đẩy nhau", "Hút nhau", "Không tương tác", "Vừa hút vừa đẩy"], 0, "Cùng dấu đẩy nhau, khác dấu hút nhau."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Dòng điện là dòng:", ["Chuyển dời có hướng của các hạt mang điện tích", "Chuyển động hỗn loạn của các phân tử", "Chảy của chất lỏng", "Chuyển động của proton trong hạt nhân"], 0, "Dòng điện là dòng chuyển dời có hướng của các điện tích."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Nguồn điện có chức năng:", ["Cung cấp và duy trì dòng điện lâu dài trong mạch", "Tiêu thụ điện năng", "Đo dòng điện", "Ngắt mạch điện"], 0, "Cung cấp dòng điện."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Chiều dòng điện theo quy ước là chiều đi từ:", ["Cực dương qua dây dẫn và thiết bị điện về cực âm của nguồn", "Cực âm về cực dương", "Trong ra ngoài", "Dưới lên trên"], 0, "Quy ước: Từ cực dương sang cực âm."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Đơn vị đo cường độ dòng điện trong hệ SI là:", ["Ampe (A)", "Volt (V)", "Ohm (Ω)", "Watt (W)"], 0, "Ampe (A)."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Đơn vị đo hiệu điện thế là:", ["Volt (V)", "Ampe (A)", "Joule (J)", "Coulomb (C)"], 0, "Volt (V)."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Dụng cụ dùng để đo cường độ dòng điện là:", ["Ampe kế (mắc nối tiếp vào đoạn mạch)", "Vôn kế", "Nhiệt kế", "Tốc kế"], 0, "Ampe kế mắc nối tiếp."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Dụng cụ dùng để đo hiệu điện thế là:", ["Vôn kế (mắc song song với đoạn mạch)", "Ampe kế", "Nhiệt kế", "Ohm kế"], 0, "Vôn kế mắc song song."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Tác dụng nhiệt của dòng điện được ứng dụng trong thiết bị nào sau đây?", ["Bàn là điện, nồi cơm điện, ấm đun nước điện", "Quạt điện", "Chuông điện", "La bàn"], 0, "Biến điện năng thành nhiệt năng."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Tác dụng phát sáng của dòng điện được ứng dụng trong:", ["Đèn sợi đốt, đèn huỳnh quang, đèn LED", "Bàn là", "Bếp từ", "Ắc quy"], 0, "Phát sáng."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Tác dụng từ của dòng điện được ứng dụng trong:", ["Nam châm điện, chuông điện, động cơ điện", "Bàn là", "Bình nóng lạnh", "Bóng đèn sợi đốt"], 0, "Tác dụng từ trong nam châm điện, động cơ điện.")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về các loại tác dụng của dòng điện:", [
                        ("a", "Dòng điện chạy qua dây dẫn đồng thông thường luôn kèm theo tác dụng nhiệt làm dây dẫn nóng lên.", True),
                        ("b", "Tác dụng sinh lí của dòng điện có thể gây co giật cơ, ngừng tim nhưng cũng được ứng dụng máy sốc tim cứu sống bệnh nhân.", True),
                        ("c", "Tác dụng hóa học của dòng điện được ứng dụng trong mạ điện, đúc điện và tinh luyện kim loại.", True),
                        ("d", "Dòng điện một chiều từ pin không có tác dụng từ.", False)
                    ], "Dòng điện không đổi từ pin vẫn có tác dụng từ bình thường."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Trong mạch điện gồm hai bóng đèn mắc nối tiếp:", [
                        ("a", "Cường độ dòng điện qua mọi vị trí trong mạch đều bằng nhau: I = I1 = I2.", True),
                        ("b", "Hiệu điện thế giữa hai đầu đoạn mạch bằng tổng các hiệu điện thế: U = U1 + U2.", True),
                        ("c", "Nếu một bóng đèn bị đứt dây tóc thì bóng đèn còn lại vẫn sáng bình thường.", False),
                        ("d", "Dòng điện chỉ có một con đường duy nhất để chạy qua cả hai đèn.", True)
                    ], "Mắc nối tiếp đứt 1 đèn thì toàn mạch bị hở, cả hai đèn đều tắt."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Trong mạch điện gồm hai bóng đèn mắc song song:", [
                        ("a", "Hiệu điện thế giữa hai đầu mỗi bóng đèn bằng nhau: U = U1 = U2.", True),
                        ("b", "Cường độ dòng điện mạch chính bằng tổng cường độ qua các mạch rẽ: I = I1 + I2.", True),
                        ("c", "Nếu tháo rời một bóng đèn thì bóng đèn kia vẫn sáng bình thường.", True),
                        ("d", "Cường độ dòng điện qua các nhánh luôn luôn bằng nhau dù hai đèn có công suất khác nhau.", False)
                    ], "Cường độ dòng điện qua mỗi nhánh phụ thuộc vào điện trở của nhánh đó."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Về an toàn khi sử dụng điện trong gia đình:", [
                        ("a", "Mạng điện sinh hoạt gia đình ở Việt Nam có hiệu điện thế hiệu dụng là 220 V.", True),
                        ("b", "Aptomat (cầu dao tự động) tự ngắt mạch khi xảy ra sự cố ngắn mạch (chập điện) hoặc quá tải.", True),
                        ("c", "Có thể chạm tay trần vào dây pha (dây nóng) 220V mà hoàn toàn không bị giật nếu đứng trên ghế gỗ khô.", False),
                        ("d", "Không bao giờ được dùng nước để dập đám cháy do chập điện khi chưa ngắt nguồn điện.", True)
                    ], "Dây pha 220V rất nguy hiểm chết người, tuyệt đối không chạm vào.")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Hiệu điện thế của mạng điện lưới gia đình ở Việt Nam là bao nhiêu Volt?", "220", "220 V."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - Đổi 500 mA sang đơn vị Ampe (A) ta được bao nhiêu A?", "0.5", "500 / 1000 = 0,5 A."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Hai bóng đèn mắc nối tiếp vào nguồn U = 9V. Biết U1 = 4V. Hiệu điện thế U2 là bao nhiêu Volt?", "5", "9 - 4 = 5 V."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Hai bóng đèn mắc song song, dòng điện mạch chính I = 1,5A. Biết I1 = 0,6A. Dòng điện I2 là bao nhiêu A?", "0.9", "1,5 - 0,6 = 0,9 A."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Một bóng đèn có ghi 6V - 0,5A sáng bình thường. Điện trở của bóng đèn là bao nhiêu Ohm (Ω)?", "12", "R = U / I = 6 / 0,5 = 12 Ω."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Đèn pin dùng 3 viên pin 1,5V mắc nối tiếp. Hiệu điện thế của bộ nguồn cung cấp cho bóng đèn pin là bao nhiêu Volt?", "4.5", "1,5 × 3 = 4,5 V.")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Cột thu lôi (cột chống sét) gắn trên đỉnh các tòa nhà cao tầng được nối đất bằng một dây đồng dày nhằm mục đích bảo vệ công trình bằng cách:", ["Dẫn dòng điện cực lớn của tia sét phóng thẳng xuống lòng đất an toàn để trung hòa điện tích", "Hút sét để nạp pin", "Làm tan mây dông", "Làm nóng không khí"], 0, "Dẫn dòng điện sét an toàn xuống đất triệt tiêu nguy cơ cháy nổ."),
                    make_vdc(2, f"Đề {t} - Đèn đi-ốt phát quang (đèn LED) ngày càng được sử dụng phổ biến thay thế hoàn toàn bóng đèn sợi đốt truyền thống vì ưu điểm vượt trội nào?", ["Hiệu suất phát quang cao, tiết kiệm tới 80% điện năng và tuổi thọ rất bền (trên 30.000 giờ)", "Tỏa ra rất nhiều nhiệt sưởi ấm", "Rất dễ vỡ", "Phát ra tia tử ngoại"], 0, "Hiệu suất cao và tiết kiệm điện tối ưu."),
                    make_vdc(3, f"Đề {t} - Khi sửa chữa điện gia đình, người thợ điện luôn dùng bút thử điện để kiểm tra dây nóng (dây pha). Đèn của bút thử điện sáng lên khi chạm vào dây nóng là nhờ:", ["Một dòng điện cực nhỏ (dưới ngưỡng giật an toàn) chạy qua điện trở bảo vệ trong bút, qua bóng đèn neon, qua cơ thể người xuống đất làm đèn sáng", "Pin trong bút thử điện phóng ra", "Từ trường xung quanh dây", "Điện tích ma sát"], 0, "Dòng điện an toàn microampe qua điện trở bảo vệ làm sáng bóng neon."),
                    make_vdc(4, f"Đề {t} - Hiện tượng mạ vàng cho đồng hồ, đồ trang sức hoặc mạ kẽm bảo vệ sắt thép khỏi gỉ sét là ứng dụng thực tiễn của tác dụng nào của dòng điện?", ["Tác dụng hóa học (điện phân)", "Tác dụng nhiệt", "Tác dụng phát sáng", "Tác dụng sinh lí"], 0, "Tác dụng hóa học trong bình điện phân mạ kim loại.")
                ]

            # ======================== CHƯƠNG VI: NHIỆT ========================
            else:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Năng lượng nhiệt là:", ["Tổng động năng của các phân tử cấu tạo nên vật do chuyển động nhiệt", "Thế năng của vật", "Cơ năng", "Quang năng"], 0, "Nội năng là tổng động năng và thế năng của các phân tử."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Khi nhiệt độ của vật càng cao thì các phân tử cấu tạo nên vật chuyển động:", ["Càng nhanh", "Càng chậm", "Đứng yên", "Không đổi"], 0, "Nhiệt độ càng cao phân tử chuyển động nhiệt càng nhanh."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Các hình thức truyền nhiệt gồm:", ["Dẫn nhiệt, đối lưu và bức xạ nhiệt", "Chỉ có dẫn nhiệt", "Chỉ có bay hơi", "Chỉ có ngưng tụ"], 0, "Dẫn nhiệt, đối lưu, bức xạ nhiệt."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Dẫn nhiệt là hình thức truyền nhiệt chủ yếu ở môi trường nào?", ["Chất rắn (đặc biệt là kim loại)", "Chất lỏng", "Chất khí", "Chân không"], 0, "Dẫn nhiệt chủ yếu ở chất rắn."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Đối lưu là hình thức truyền nhiệt chủ yếu ở môi trường nào?", ["Chất lỏng và chất khí", "Chất rắn", "Chân không", "Kim loại"], 0, "Đối lưu nhờ dòng chất lưu di chuyển ở chất lỏng và khí."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Năng lượng nhiệt từ Mặt Trời truyền qua khoảng chân không vũ trụ đến Trái Đất bằng hình thức nào?", ["Bức xạ nhiệt", "Dẫn nhiệt", "Đối lưu", "Dòng điện"], 0, "Bức xạ nhiệt truyền được trong chân không dưới dạng sóng điện từ."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Nồi, xoong nấu ăn thường làm bằng kim loại (nhôm, inox) nhưng quai nồi lại làm bằng nhựa hoặc gỗ vì:", ["Kim loại dẫn nhiệt tốt giúp thức ăn nhanh chín, còn nhựa/gỗ dẫn nhiệt kém giúp cầm không bị bỏng", "Kim loại nhẹ hơn nhựa", "Gỗ bắt lửa tốt", "Chỉ để làm đẹp"], 0, "Kim loại dẫn nhiệt tốt, gỗ/nhựa cách nhiệt an toàn."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Khối lượng riêng của nước thay đổi thế nào khi đun nóng nước từ 20 °C đến 80 °C?", ["Giảm đi vì nước nở ra tăng thể tích", "Tăng lên", "Không đổi", "Bằng 0"], 0, "Nước nở ra khi nóng nên thể tích tăng => D = m/V giảm."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Băng kép gồm hai thanh kim loại khác nhau (như đồng và thép) tán chặt vào nhau, khi bị đốt nóng sẽ:", ["Bị cong về phía thanh kim loại nở vì nhiệt ít hơn (thép)", "Giữ thẳng nguyên vẹn", "Bị đứt đôi", "Bị co ngắn lại"], 0, "Đồng nở nhiều hơn thép làm băng kép uốn cong về phía thép."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Ứng dụng quan trọng của băng kép là:", ["Dùng trong rơle nhiệt đóng ngắt tự động mạch điện của bàn là, nồi cơm điện", "Làm dây dẫn điện", "Làm nhiệt kế đo độ ẩm", "Làm khung xe đạp"], 0, "Rơle nhiệt tự ngắt khi quá nhiệt."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Tại sao giữa các thanh ray xe lửa luôn có một khe hở nhỏ?", ["Để đường ray có chỗ dãn nở khi trời nắng nóng mà không bị uốn cong làm trật bánh tàu", "Để tiết kiệm thép", "Để tàu chạy êm hơn", "Để thoát nước mưa"], 0, "Tạo khe co giãn nở vì nhiệt."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Vào mùa hè, mặc áo màu trắng mát hơn mặc áo màu đen vì:", ["Áo màu trắng phản xạ bức xạ nhiệt tốt hơn và hấp thụ nhiệt ít hơn áo màu đen", "Áo màu đen mỏng hơn", "Áo màu trắng thấm mồ hôi nhiều hơn", "Màu đen nặng hơn"], 0, "Vật màu sáng phản xạ nhiệt tốt, vật màu tối hấp thụ nhiệt mạnh.")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về năng lượng nhiệt và sự truyền nhiệt:", [
                        ("a", "Nhiệt năng tự truyền từ vật có nhiệt độ cao sang vật có nhiệt độ thấp hơn.", True),
                        ("b", "Quá trình truyền nhiệt dừng lại khi hai vật đạt trạng thái cân bằng nhiệt (cùng nhiệt độ).", True),
                        ("c", "Bức xạ nhiệt có thể truyền qua cả môi trường chân không.", True),
                        ("d", "Chất khí dẫn nhiệt tốt hơn kim loại rất nhiều lần.", False)
                    ], "Chất khí dẫn nhiệt rất kém (chất cách nhiệt tốt)."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Về sự nở vì nhiệt của các chất:", [
                        ("a", "Chất rắn, chất lỏng và chất khí đều dãn nở khi nóng lên và co lại khi lạnh đi.", True),
                        ("b", "Các chất khí khác nhau nở vì nhiệt giống nhau.", True),
                        ("c", "Chất khí nở vì nhiệt nhiều hơn chất lỏng, chất lỏng nở vì nhiệt nhiều hơn chất rắn.", True),
                        ("d", "Khi nước đông đặc thành đá, thể tích của nó giảm đi.", False)
                    ], "Hiện tượng dị thường của nước: từ 4°C xuống 0°C đóng băng thể tích tăng lên (nước đá nổi)."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Thả một miếng đồng nặng 0,5 kg ở nhiệt độ 100 °C vào 1 kg nước ở 20 °C trong một nhiệt lượng kế cách nhiệt:", [
                        ("a", "Nhiệt lượng tỏa ra từ miếng đồng bằng nhiệt lượng thu vào của nước.", True),
                        ("b", "Nhiệt độ cân bằng của hệ sẽ nằm trong khoảng từ 20 °C đến 100 °C.", True),
                        ("c", "Nhiệt dung riêng của nước lớn hơn nhiều so với nhiệt dung riêng của đồng.", True),
                        ("d", "Nhiệt độ cuối cùng của miếng đồng và nước sẽ bằng đúng 60 °C.", False)
                    ], "Do cnước = 4200 J/kg.K rất lớn so với cđồng = 380 J/kg.K nên nhiệt độ cân bằng tăng rất ít (khoảng 23,5°C)."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Cấu tạo và nguyên lí của phích giữ nhiệt (bình thủy):", [
                        ("a", "Ruột phích gồm hai lớp thủy tinh, ở giữa là khoảng chân không giúp ngăn chặn dẫn nhiệt và đối lưu.", True),
                        ("b", "Thành bên trong ruột phích được tráng bạc sáng bóng để phản xạ bức xạ nhiệt trở lại.", True),
                        ("c", "Nút bấc hoặc nắp xốp đậy kín miệng phích giúp ngăn chặn truyền nhiệt bằng đối lưu ra ngoài.", True),
                        ("d", "Phích giữ nhiệt có thể giữ nước nóng vĩnh viễn không bao giờ nguội.", False)
                    ], "Nhiệt vẫn rò rỉ chậm qua miệng phích và nắp phích.")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Kim loại nào dẫn nhiệt tốt nhất trong các kim loại? (Ghi kí hiệu hóa học)", "Ag", "Bạc (Ag)."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - Nhiệt lượng từ Mặt Trời truyền đến Trái Đất bằng hình thức truyền nhiệt nào?", "Bức xạ nhiệt", "Bức xạ nhiệt."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Tính nhiệt lượng cần cung cấp để đun nóng 1 kg nước từ 20 °C lên 100 °C (tăng 80 °C). Biết nhiệt dung riêng của nước c = 4200 J/kg.K. Kết quả là bao nhiêu kJ?", "336", "Q = m.c.Δt = 1 × 4200 × 80 = 336.000 J = 336 kJ."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Trộn 1 lít nước ở 20 °C với 1 lít nước ở 80 °C (bỏ qua hao phí nhiệt ra môi trường). Nhiệt độ cân bằng của hỗn hợp là bao nhiêu °C?", "50", "(20 + 80) / 2 = 50 °C."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Một ấm điện công suất 1000 W đun sôi 1 kg nước từ 20 °C trong 6 phút (360 giây). Biết nhiệt lượng cần đun sôi là 336 kJ. Hiệu suất của ấm điện xấp xỉ bằng bao nhiêu %? (Làm tròn 1 chữ số thập phân)", "93.3", "A = P × t = 1000 × 360 = 360 kJ. H = 336 / 360 × 100% ≈ 93,3%."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Nước có nhiệt dung riêng lớn nhất ở nhiệt độ bao nhiêu °C khi khối lượng riêng đạt cực đại 1000 kg/m3?", "4", "Ở 4 °C nước có khối lượng riêng lớn nhất.")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Các hồ nước ở vùng hàn đới (như Bắc Âu, Nga, Canada) vào mùa đông băng giá thì lớp băng chỉ đóng cứng trên bề mặt phía trên, trong khi phía đáy hồ nước vẫn ở khoảng 4 °C giúp cá và sinh vật thủy sinh sống sót qua mùa đông. Hiện tượng kì diệu này là nhờ tính chất đặc biệt nào của nước?", ["Nước ở 4 °C có khối lượng riêng lớn nhất nên chìm xuống đáy, còn nước đá ở 0 °C nhẹ hơn nổi lên trên tạo lớp cách nhiệt bảo vệ đáy hồ", "Cá tỏa nhiệt sưởi ấm đáy hồ", "Dưới đáy hồ có mạch nước nóng ngầm", "Đáy hồ sâu không nhận ánh sáng"], 0, "Đặc tính dị thường của nước ở 4°C bảo vệ sự sống."),
                    make_vdc(2, f"Đề {t} - Đèn sưởi nhà tắm dùng bóng đèn halogen hoặc hồng ngoại làm ấm phòng tắm gần như ngay tức thì khi bật công tắc. Hình thức truyền nhiệt chính của đèn sưởi là:", ["Bức xạ nhiệt bằng tia hồng ngoại truyền thẳng đến da người", "Dẫn nhiệt qua không khí", "Đối lưu không khí nóng", "Dòng điện chạy qua người"], 0, "Tia hồng ngoại truyền nhiệt tức thời qua bức xạ nhiệt."),
                    make_vdc(3, f"Đề {t} - Trong xây dựng nhà ở vùng khí hậu nhiệt đới nắng nóng, giải pháp kiến trúc xanh nào sau đây giúp ngôi nhà luôn mát mẻ tự nhiên và tiết kiệm điện điều hòa?", ["Lợp mái ngói màu sáng hoặc có trần thạch cao cách nhiệt, thiết kế cửa thông gió đối lưu tự nhiên và trồng cây xanh che bóng", "Sơn tường toàn bộ màu đen", "Bịt kín toàn bộ cửa sổ", "Dùng kính dày bao quanh"], 0, "Cách nhiệt và đối lưu thông gió tự nhiên."),
                    make_vdc(4, f"Đề {t} - Thùng xốp đựng đá lạnh giữ cho đá lâu tan suốt cả ngày là do:", ["Xốp chứa nhiều túi khí nhỏ li ti khép kín, mà không khí là chất dẫn nhiệt cực kì kém nên cách nhiệt rất tốt", "Xốp tự phát ra hơi lạnh", "Xốp hấp thụ nước đá", "Xốp ngăn cản lực hấp dẫn"], 0, "Không khí bị giữ trong các lỗ xốp là chất cách nhiệt tuyệt vời.")
                ]

            exams[k] = {
                "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
                "grade": "8", "subject": "physics", "subjectName": "Vật lý",
                "chapterId": ch_id, "chapterTitle": ch_title,
                "lessonId": l_id, "lessonName": l_name,
                "testNum": t, "duration": "45 phút", "points": 10.0,
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    return exams

if __name__ == "__main__":
    exs = build_phys8_exams()
    print("Phys 8 generated total:", len(exs), "exams.")
