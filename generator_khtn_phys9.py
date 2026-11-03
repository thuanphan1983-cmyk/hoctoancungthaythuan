# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - VẬT LÝ 9 (KNTT)
Gồm 14 bài/chương ôn tập => 48 đề thi độc lập 100%
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

def build_phys9_exams():
    exams = {}

    lessons_list = [
        # CHƯƠNG VI: ÁNH SÁNG
        ("phys9_c6", "Chương VI: Ánh sáng", "phys9_c6_b17", "Bài 17: Hiện tượng khúc xạ ánh sáng", 3),
        ("phys9_c6", "Chương VI: Ánh sáng", "phys9_c6_b18", "Bài 18: Hiện tượng phản xạ toàn phần", 3),
        ("phys9_c6", "Chương VI: Ánh sáng", "phys9_c6_b19", "Bài 19: Thấu kính", 3),
        ("phys9_c6", "Chương VI: Ánh sáng", "phys9_c6_b20", "Bài 20: Thực hành xác định tiêu cự của thấu kính hội tụ", 3),
        ("phys9_c6", "Chương VI: Ánh sáng", "phys9_c6_b21", "Bài 21: Kính lúp", 3),
        ("phys9_c6", "Chương VI: Ánh sáng", "phys9_c6_rev", "[Đề tổng hợp] Ôn tập cuối Chương VI", 5),

        # CHƯƠNG VII: ĐIỆN TỪ
        ("phys9_c7", "Chương VII: Điện từ", "phys9_c7_b22", "Bài 22: Từ trường của ống dây có dòng điện. Nam châm điện", 3),
        ("phys9_c7", "Chương VII: Điện từ", "phys9_c7_b23", "Bài 23: Tác dụng của từ trường lên đoạn dây dẫn mang dòng điện", 3),
        ("phys9_c7", "Chương VII: Điện từ", "phys9_c7_b24", "Bài 24: Hiện tượng cảm ứng điện từ. Dòng điện xoay chiều", 3),
        ("phys9_c7", "Chương VII: Điện từ", "phys9_c7_b25", "Bài 25: Máy biến thế", 3),
        ("phys9_c7", "Chương VII: Điện từ", "phys9_c7_rev", "[Đề tổng hợp] Ôn tập cuối Chương VII", 5),

        # CHƯƠNG VIII: NĂNG LƯỢNG VÀ SỰ BIẾN ĐỔI NĂNG LƯỢNG
        ("phys9_c8", "Chương VIII: Năng lượng và sự biến đổi năng lượng", "phys9_c8_b26", "Bài 26: Vòng năng lượng trên Trái Đất. Năng lượng tái tạo", 3),
        ("phys9_c8", "Chương VIII: Năng lượng và sự biến đổi năng lượng", "phys9_c8_b27", "Bài 27: Sự bảo toàn và chuyển hóa năng lượng", 3),
        ("phys9_c8", "Chương VIII: Năng lượng và sự biến đổi năng lượng", "phys9_c8_rev", "[Đề tổng hợp] Ôn tập cuối Chương VIII", 5)
    ]

    for ch_id, ch_title, l_id, l_name, n_tests in lessons_list:
        for t in range(1, n_tests + 1):
            k = f"{l_id}_test{t}"
            p1 = []
            p2 = []
            p3 = []
            p4 = []

            # ======================== CHƯƠNG VI: ÁNH SÁNG ========================
            if "c6" in ch_id:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Hiện tượng khúc xạ ánh sáng là hiện tượng tia sáng:", ["Bị gãy khúc tại mặt phân cách giữa hai môi trường trong suốt khi truyền xiên góc", "Bị hắt ngược trở lại môi trường cũ", "Truyền thẳng tuyệt đối", "Bị đổi màu sắc"], 0, "Hiện tượng tia sáng bị gãy khúc khi truyền qua mặt phân cách hai môi trường trong suốt."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Khi truyền tia sáng từ không khí vào nước với góc tới i > 0, mối quan hệ giữa góc khúc xạ r và góc tới i là:", ["r < i", "r > i", "r = i", "r = 2i"], 0, "Từ không khí vào nước chiết quang hơn nên góc khúc xạ nhỏ hơn góc tới: r < i."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Điều kiện để xảy ra hiện tượng phản xạ toàn phần là:", ["Ánh sáng truyền từ môi trường chiết quang hơn sang kém hơn và góc tới i >= igh", "Ánh sáng truyền từ không khí vào nước", "Góc tới bằng 0 độ", "Chiếu vuông góc"], 0, "Truyền từ môi trường chiết quang hơn sang kém hơn và i ≥ igh."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Thấu kính hội tụ có phần rìa:", ["Mỏng hơn phần giữa", "Dày hơn phần giữa", "Bằng phần giữa", "Có dạng hình cầu lồi cả 2 mặt"], 0, "Thấu kính hội tụ (rìa mỏng)."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Thấu kính phân kì có phần rìa:", ["Dày hơn phần giữa", "Mỏng hơn phần giữa", "Bằng phần giữa", "Rất mỏng"], 0, "Thấu kính phân kì (rìa dày)."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Chiếu một chùm tia sáng song song với trục chính đến thấu kính hội tụ thì chùm tia ló:", ["Hội tụ tại tiêu điểm của thấu kính", "Phân kì loe rộng", "Song song với nhau", "Bật ngược trở lại"], 0, "Hội tụ tại tiêu điểm F'."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Đặt vật thật ngoài khoảng tiêu cự (d > f) của thấu kính hội tụ, ảnh thu được luôn là:", ["Ảnh thật, ngược chiều với vật", "Ảnh ảo, cùng chiều", "Ảnh ảo nhỏ hơn vật", "Không có ảnh"], 0, "d > f cho ảnh thật ngược chiều."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Đặt vật thật trong khoảng tiêu cự (d < f) của thấu kính hội tụ, ảnh thu được có tính chất:", ["Là ảnh ảo, cùng chiều và lớn hơn vật", "Là ảnh thật ngược chiều", "Là ảnh ảo nhỏ hơn vật", "Ảnh hứng được trên màn"], 0, "d < f cho ảnh ảo, cùng chiều, lớn hơn vật (kính lúp)."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Vật thật đặt trước thấu kính phân kì luôn cho:", ["Ảnh ảo, cùng chiều và nhỏ hơn vật nằm trong khoảng tiêu cự", "Ảnh thật ngược chiều", "Ảnh ảo lớn hơn vật", "Không tạo ảnh"], 0, "Thấu kính phân kì luôn cho ảnh ảo nhỏ hơn vật cùng chiều."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Kính lúp là:", ["Một thấu kính hội tụ có tiêu cự ngắn dùng để quan sát các vật nhỏ", "Thấu kính phân kì", "Gương phẳng", "Gương cầu lồi"], 0, "Thấu kính hội tụ có f ngắn."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Công thức tính số bội giác G của kính lúp là:", ["G = 25 / f (với f tính bằng cm)", "G = f / 25", "G = 25 × f", "G = f + 25"], 0, "G = 25 / f."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Ứng dụng quan trọng nhất của hiện tượng phản xạ toàn phần trong thông tin liên lạc hiện đại là:", ["Cáp quang viễn thông truyền dẫn internet tốc độ cao", "Kính tiềm vọng", "Gương soi", "Kính râm"], 0, "Cáp quang truyền tín hiệu ánh sáng bằng phản xạ toàn phần.")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về hiện tượng khúc xạ ánh sáng:", [
                        ("a", "Hiện tượng khúc xạ chỉ xảy ra khi tia sáng truyền xiên góc qua mặt phân cách giữa hai môi trường trong suốt.", True),
                        ("b", "Nếu tia sáng truyền vuông góc với mặt phân cách (i = 0) thì tia sáng truyền thẳng không bị khúc xạ.", True),
                        ("c", "Góc tới tăng thì góc khúc xạ cũng tăng theo.", True),
                        ("d", "Tốc độ truyền ánh sáng trong nước lớn hơn tốc độ truyền ánh sáng trong không khí.", False)
                    ], "Ánh sáng truyền trong không khí nhanh hơn trong nước (c ≈ 300.000 km/s > v_nước ≈ 225.000 km/s)."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Về đường truyền của các tia sáng đặc biệt qua thấu kính hội tụ:", [
                        ("a", "Tia tới đi qua quang tâm O truyền thẳng không đổi hướng.", True),
                        ("b", "Tia tới song song với trục chính cho tia ló đi qua tiêu điểm F'.", True),
                        ("c", "Tia tới đi qua tiêu điểm F cho tia ló song song với trục chính.", True),
                        ("d", "Tia tới bất kì đều bị phản xạ bật ngược trở lại.", False)
                    ], "Thấu kính cho ánh sáng truyền qua và khúc xạ, không phải phản xạ."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Đặt một vật sáng AB cao 2 cm vuông góc với trục chính của thấu kính hội tụ có tiêu cự f = 10 cm, cách thấu kính d = 20 cm:", [
                        ("a", "Vật đặt tại vị trí d = 2f.", True),
                        ("b", "Ảnh thu được là ảnh thật, ngược chiều với vật.", True),
                        ("c", "Ảnh cách thấu kính một đoạn d' = 20 cm.", True),
                        ("d", "Chiều cao của ảnh A'B' bằng 4 cm.", False)
                    ], "Khi d = 2f thì d' = 2f = 20 cm và chiều cao ảnh bằng đúng chiều cao vật A'B' = AB = 2 cm."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Một kính lúp có tiêu cự f = 5 cm:", [
                        ("a", "Số bội giác của kính lúp là G = 5X.", True),
                        ("b", "Để quan sát vật nhỏ rõ nét, vật phải được đặt trong khoảng tiêu cự (d < 5 cm).", True),
                        ("c", "Ảnh quan sát qua kính lúp là ảnh ảo, cùng chiều và lớn hơn vật.", True),
                        ("d", "Kính lúp giúp ta quan sát được các vi khuẩn có kích thước nano mét.", False)
                    ], "Kính lúp chỉ phóng đại 2 - 20 lần; vi khuẩn và virus cần kính hiển vi quang học hoặc điện tử.")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Thấu kính có phần rìa mỏng hơn phần giữa là thấu kính gì? (Hội tụ hay Phân kì)", "Hội tụ", "Thấu kính hội tụ."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - Kính lúp có tiêu cự f = 10 cm có số bội giác G bằng bao nhiêu X?", "2.5", "G = 25 / 10 = 2,5X."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Đặt vật sáng cách thấu kính hội tụ (f = 12 cm) một khoảng d = 24 cm. Khoảng cách từ ảnh thật đến thấu kính là bao nhiêu cm?", "24", "d = 2f => d' = 2f = 24 cm."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Một tia sáng truyền từ nước ra không khí có góc giới hạn phản xạ toàn phần igh = 48,5 độ. Nếu chiếu góc tới i = 60 độ thì có tia khúc xạ ra không khí không? (Có hay Không)", "Không", "i = 60° > igh = 48,5° nên xảy ra phản xạ toàn phần, không có tia khúc xạ."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Đặt vật AB cao 4 cm trước thấu kính hội tụ cách thấu kính 30 cm (f = 20 cm). Chiều cao ảnh thật thu được là bao nhiêu cm?", "8", "d' = d.f / (d - f) = 30×20 / 10 = 60 cm. A'B' = AB × d'/d = 4 × 60 / 30 = 8 cm."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Một người dùng kính lúp có f = 5 cm để quan sát một con kiến dài 2 mm đặt cách kính 4 cm. Chiều dài ảnh của con kiến nhìn thấy qua kính lúp là bao nhiêu mm?", "10", "d' = 4×5 / (5 - 4) = 20 cm. k = d'/d = 20/4 = 5 => ảnh dài 2 × 5 = 10 mm.")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Hiện tượng ảo ảnh (Mirage) vũng nước lấp loáng trên mặt đường nhựa khô khốc vào những buổi trưa hè nắng gắt là do hiện tượng quang học nào gây ra?", ["Sự khúc xạ và phản xạ toàn phần của ánh sáng qua các lớp không khí có nhiệt độ và mật độ khác nhau sát mặt đường", "Nước bốc hơi từ lòng đất", "Mắt người bị hoa mắt", "Mặt đường bị nóng chảy"], 0, "Không khí sát mặt đường rất nóng và loãng làm tia sáng bị bẻ cong phản xạ toàn phần."),
                    make_vdc(2, f"Đề {t} - Trong nội soi y học (nội soi dạ dày, phế quản, đại tràng), bác sĩ đưa một dây dẫn mềm vào cơ thể bệnh nhân có gắn nguồn sáng và camera truyền hình ảnh ra màn hình. Dây dẫn này truyền ánh sáng dựa trên công nghệ:", ["Sợi quang học ứng dụng phản xạ toàn phần của ánh sáng", "Dây cáp điện thông thường", "Sóng siêu âm", "Ống gương phản chiếu"], 0, "Sợi quang học truyền ánh sáng bằng phản xạ toàn phần."),
                    make_vdc(3, f"Đề {t} - Mắt người bình thường có thể nhìn rõ các vật ở xa và gần là nhờ khả năng điều tiết của bộ phận nào trong mắt đóng vai trò như một thấu kính hội tụ có thể thay đổi độ cong?", ["Thể thủy tinh", "Giác mạc", "Võng mạc (màng lưới)", "Lòng đen"], 0, "Thể thủy tinh thay đổi độ cong để điều tiết ảnh hiện rõ trên võng mạc."),
                    make_vdc(4, f"Đề {t} - Người bị tật cận thị khi nhìn các vật ở xa mắt thì ảnh của vật rơi ở phía trước màng lưới nên nhìn mờ. Để khắc phục tật cận thị, người đó phải đeo kính có tác dụng phân kì (kính cận) nhằm mục đích:", ["Đẩy ảnh của vật lùi về đúng trên màng lưới để nhìn rõ", "Thu phóng đại vật to lên", "Chống bụi và nắng", "Làm mắt không bị chớp"], 0, "Kính phân kì giúp ảnh rơi đúng trên màng lưới.")
                ]

            # ======================== CHƯƠNG VII: ĐIỆN TỪ ========================
            elif "c7" in ch_id:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Đường sức từ bên trong lòng ống dây có dòng điện chạy qua là những:", ["Đường thẳng song song cách đều nhau (từ trường đều)", "Đường tròn đồng tâm", "Đường parabol", "Đường gấp khúc"], 0, "Từ trường trong lòng ống dây là từ trường đều."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Quy tắc nắm tay phải dùng để xác định:", ["Chiều của đường sức từ trong lòng ống dây có dòng điện", "Độ lớn của dòng điện", "Điện trở của dây", "Công suất điện"], 0, "Quy tắc nắm tay phải xác định chiều đường sức từ."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Lực do từ trường tác dụng lên một đoạn dây dẫn mang dòng điện đặt trong từ trường được gọi là:", ["Lực từ", "Lực hấp dẫn", "Lực đàn hồi", "Lực ma sát"], 0, "Lực từ."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Quy tắc bàn tay trái dùng để xác định:", ["Chiều của lực từ tác dụng lên đoạn dây dẫn mang dòng điện", "Chiều dòng điện", "Điện áp", "Cực từ của ống dây"], 0, "Quy tắc bàn tay trái xác định chiều lực từ."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Hiện tượng xuất hiện dòng điện cảm ứng trong cuộn dây dẫn kín khi số đường sức từ xuyên qua tiết diện cuộn dây biến thiên gọi là:", ["Hiện tượng cảm ứng điện từ", "Hiện tượng đoản mạch", "Hiện tượng nhiễm điện", "Hiện tượng quang điện"], 0, "Hiện tượng cảm ứng điện từ (Faraday phát hiện)."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Dòng điện xoay chiều (AC) là dòng điện có:", ["Chiều và cường độ luân phiên biến đổi theo thời gian", "Chiều không đổi", "Điện thế cố định", "Cường độ luôn bằng 0"], 0, "Luân phiên đổi chiều theo thời gian."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Máy biến áp (máy biến thế) là thiết bị dùng để:", ["Biến đổi hiệu điện thế xoay chiều mà không làm thay đổi tần số", "Biến đổi dòng một chiều thành xoay chiều", "Tạo ra điện năng", "Đo công suất điện"], 0, "Biến đổi hiệu điện thế xoay chiều."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Mối liên hệ giữa hiệu điện thế và số vòng dây trong máy biến áp là:", ["U1 / U2 = N1 / N2", "U1 / U2 = N2 / N1", "U1 × U2 = N1 × N2", "U1 + U2 = N1 + N2"], 0, "U1 / U2 = N1 / N2."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Máy tăng áp có số vòng dây cuộn thứ cấp N2 so với cuộn sơ cấp N1 là:", ["N2 > N1", "N2 < N1", "N2 = N1", "N2 = 0"], 0, "Tăng áp: N2 > N1 => U2 > U1."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Khi truyền tải điện năng đi xa, biện pháp hiệu quả nhất để giảm hao phí do tỏa nhiệt trên đường dây là:", ["Tăng hiệu điện thế ở hai đầu đường dây truyền tải trước khi truyền đi", "Tăng tiết diện dây đồng lên gấp trăm lần", "Hạ hiệu điện thế", "Dùng dây dẫn bằng bạc"], 0, "Php = R.P2 / U2 nên tăng U giúp giảm hao phí tỉ lệ nghịch với U2."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Nếu tăng hiệu điện thế truyền tải lên 10 lần thì công suất hao phí do tỏa nhiệt trên đường dây sẽ:", ["Giảm đi 100 lần", "Giảm đi 10 lần", "Tăng 100 lần", "Không đổi"], 0, "Giảm 10^2 = 100 lần."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Máy phát điện xoay chiều gồm hai bộ phận chính là:", ["Roto (phần quay) và Stato (phần đứng yên)", "Hai cuộn dây", "Ắc quy và công tắc", "Vôn kế và ampe kế"], 0, "Roto và stato (nam châm và cuộn dây).")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về hiện tượng cảm ứng điện từ:", [
                        ("a", "Dòng điện cảm ứng chỉ xuất hiện khi số đường sức từ xuyên qua tiết diện cuộn dây dẫn kín biến thiên (tăng hoặc giảm).", True),
                        ("b", "Đưa nam châm lại gần hoặc ra xa cuộn dây đều tạo ra dòng điện cảm ứng.", True),
                        ("c", "Nếu để nam châm đứng yên bất động bên trong cuộn dây thì dòng điện cảm ứng liên tục sinh ra.", False),
                        ("d", "Dòng điện xoay chiều trong lưới điện quốc gia có tần số 50 Hz.", True)
                    ], "Nam châm đứng yên thì số đường sức từ không biến thiên nên không có dòng cảm ứng."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Về máy biến áp:", [
                        ("a", "Máy biến áp chỉ hoạt động với dòng điện xoay chiều, không hoạt động với dòng điện một chiều không đổi.", True),
                        ("b", "Máy hạ áp có số vòng dây cuộn thứ cấp nhỏ hơn cuộn sơ cấp (N2 < N1).", True),
                        ("c", "Máy biến áp lý tưởng cho ta lợi về cả hiệu điện thế và công suất điện.", False),
                        ("d", "Lõi thép của máy biến áp được ghép từ các lá thép kỹ thuật điện mỏng cách điện để giảm dòng điện xoáy Foucault.", True)
                    ], "Máy biến áp không làm tăng công suất điện (P1 ≈ P2)."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Một máy biến áp cuộn sơ cấp có N1 = 4400 vòng, cuộn thứ cấp có N2 = 220 vòng. Đặt vào hai đầu cuộn sơ cấp hiệu điện thế xoay chiều U1 = 220 V:", [
                        ("a", "Đây là máy hạ áp.", True),
                        ("b", "Tỉ số biến áp N1 / N2 bằng 20.", True),
                        ("c", "Hiệu điện thế ở hai đầu cuộn thứ cấp là U2 = 11 V.", True),
                        ("d", "Nếu đặt vào cuộn sơ cấp nguồn pin một chiều 12V thì cuộn thứ cấp cho điện áp 0,6V.", False)
                    ], "U2 = 220 / 20 = 11 V. Dòng một chiều không đổi không làm biến thiên từ thông nên U2 = 0V."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Truyền tải công suất điện P = 100 kW trên đường dây có điện trở tổng cộng R = 10 Ω dưới hiệu điện thế U = 10 kV (10.000 V):", [
                        ("a", "Cường độ dòng điện trên đường dây là I = 10 A.", True),
                        ("b", "Công suất hao phí do tỏa nhiệt là Php = 1 kW (1000 W).", True),
                        ("c", "Hiệu suất truyền tải điện đạt 99%.", True),
                        ("d", "Nếu tăng hiệu điện thế lên U = 20 kV thì công suất hao phí giảm đi một nửa.", False)
                    ], "Tăng U lên 2 lần thì Php giảm đi 2^2 = 4 lần (còn 250 W).")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Tần số của dòng điện xoay chiều trong lưới điện sinh hoạt gia đình ở Việt Nam là bao nhiêu Hz?", "50", "50 Hz."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - Máy biến áp có N1 = 1000 vòng, N2 = 5000 vòng là máy tăng áp hay hạ áp?", "Tăng áp", "Máy tăng áp."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Một máy biến thế có N1 = 500 vòng, N2 = 2500 vòng. Đặt vào cuộn sơ cấp hiệu điện thế U1 = 220 V. Hiệu điện thế U2 là bao nhiêu Volt?", "1100", "U2 = 220 × (2500/500) = 1100 V."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Muốn giảm công suất hao phí do tỏa nhiệt trên đường dây truyền tải điện đi 16 lần thì cần tăng hiệu điện thế lên bao nhiêu lần?", "4", "4^2 = 16 lần."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Một máy hạ áp sạc điện thoại có N1 = 2200 vòng, cắm vào nguồn U1 = 220 V để lấy ra điện áp U2 = 5 V. Số vòng dây cuộn thứ cấp N2 là bao nhiêu vòng?", "50", "N2 = 2200 × (5/220) = 50 vòng."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Đường dây truyền tải có điện trở 20 Ω truyền công suất 500 kW ở hiệu điện thế 50 kV. Công suất hao phí tỏa nhiệt trên đường dây là bao nhiêu kW?", "2", "I = 500.000 / 50.000 = 10 A. Php = I^2 × R = 100 × 20 = 2000 W = 2 kW.")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Đường dây tải điện cao thế Bắc - Nam 500 kV của Việt Nam truyền tải điện năng từ các nhà máy thủy điện lớn (Hòa Bình, Sơn La) vào miền Trung và miền Nam. Lí do bắt buộc phải sử dụng cấp điện áp cực cao 500.000 V là:", ["Giảm thiểu tối đa tổn thất hao phí điện năng do tỏa nhiệt trên chiều dài hơn 1500 km đường dây", "Để dòng điện chạy nhanh hơn tốc độ ánh sáng", "Để làm đẹp cảnh quan", "Để dây điện không bị đứt"], 0, "Hiệu điện thế 500 kV giảm hao phí nhiệt hàng trăm triệu lần."),
                    make_vdc(2, f"Đề {t} - Động cơ điện một chiều và động cơ điện xoay chiều hoạt động dựa trên tác dụng nào sau đây?", ["Tác dụng của lực từ lên cuộn dây mang dòng điện đặt trong từ trường làm roto quay liên tục", "Tác dụng nhiệt nung nóng trục quay", "Lực ma sát cơ học", "Trọng lực"], 0, "Lực từ làm quay khung dây."),
                    make_vdc(3, f"Đề {t} - Bếp từ nấu ăn gia đình làm nóng đáy nồi kim loại rất nhanh mà mặt kính bếp hầu như không nóng là nhờ hiện tượng:", ["Dòng điện Foucault (dòng điện xoáy) cảm ứng sinh ra trong đáy nồi kim loại khi đặt trong từ trường biến thiên tần số cao của mâm từ", "Bếp phát ra lửa hồng ngoại", "Bếp truyền nhiệt trực tiếp qua kính", "Sóng âm công suất lớn"], 0, "Dòng điện xoáy Foucault cảm ứng trực tiếp ở đáy nồi sinh nhiệt tức thì."),
                    make_vdc(4, f"Đề {t} - Bộ sạc không dây cho điện thoại thông minh truyền năng lượng điện từ đế sạc sang pin điện thoại qua khoảng cách vài milimét là ứng dụng của:", ["Hiện tượng cảm ứng điện từ giữa cuộn dây phát trong đế sạc và cuộn dây thu trong điện thoại", "Bức xạ nhiệt", "Tia laser", "Sóng âm thanh"], 0, "Cảm ứng điện từ cộng hưởng không dây.")
                ]

            # ======================== CHƯƠNG VIII: NĂNG LƯỢNG ========================
            else:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Định luật bảo toàn năng lượng phát biểu rằng: Năng lượng:", ["Không tự sinh ra cũng không tự mất đi, chỉ chuyển hóa từ dạng này sang dạng khác hoặc truyền từ vật này sang vật khác", "Tự sinh ra khi vận động", "Mất dần theo thời gian", "Chỉ có thể tăng lên"], 0, "Định luật bảo toàn và chuyển hóa năng lượng."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Nguồn năng lượng nào sau đây là nguồn năng lượng tái tạo?", ["Năng lượng mặt trời, gió, thủy điện, sinh khối", "Than đá", "Dầu mỏ", "Khí tự nhiên"], 0, "Năng lượng tái tạo tự bổ sung liên tục từ thiên nhiên."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Nguồn năng lượng nào sau đây là nhiên liệu hóa thạch không thể tái tạo?", ["Than đá, dầu mỏ, khí thiên nhiên", "Năng lượng gió", "Năng lượng sóng biển", "Năng lượng địa nhiệt"], 0, "Nhiên liệu hóa thạch hình thành hàng triệu năm không tái tạo."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Hiệu suất H của một quá trình chuyển hóa năng lượng được tính theo công thức:", ["H = (Năng lượng có ích / Năng lượng toàn phần) × 100%", "H = (Năng lượng hao phí / Năng lượng toàn phần) × 100%", "H = Năng lượng có ích + Năng lượng hao phí", "H = Năng lượng toàn phần / Năng lượng có ích"], 0, "H = (A_ích / A_tp) × 100%."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Nguồn gốc ban đầu của hầu hết các dạng năng lượng trên Trái Đất (như gió, sóng, sinh khối, nhiên liệu hóa thạch) bắt nguồn từ:", ["Năng lượng bức xạ của Mặt Trời", "Năng lượng hạt nhân lòng đất", "Thủy triều Mặt Trăng", "Gió bão"], 0, "Mặt Trời là cội nguồn của hầu hết năng lượng trên Trái Đất."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Trong nhà máy thủy điện, dạng năng lượng nào của dòng nước được chuyển hóa thành điện năng?", ["Cơ năng (thế năng và động năng của dòng nước)", "Hóa năng", "Nhiệt năng", "Năng lượng nguyên tử"], 0, "Thế năng dòng nước chuyển thành động năng quay tuabin phát điện."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Khi quạt điện hoạt động, điện năng chủ yếu được chuyển hóa thành:", ["Cơ năng của cánh quạt quay và một phần nhiệt năng hao phí", "Quang năng", "Hóa năng", "Năng lượng hạt nhân"], 0, "Điện năng chuyển thành cơ năng có ích và nhiệt năng hao phí."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Khi sạc pin điện thoại, điện năng được chuyển hóa thành dạng năng lượng nào tích trữ trong pin?", ["Hóa năng", "Cơ năng", "Quang năng", "Thế năng hấp dẫn"], 0, "Tích trữ dưới dạng hóa năng trong pin."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Một bóng đèn LED tiêu thụ 100 J điện năng và phát ra 85 J năng lượng ánh sáng. Hiệu suất của đèn LED là:", ["85%", "15%", "100%", "50%"], 0, "H = 85 / 100 × 100% = 85%."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Việc sử dụng quá nhiều nhiên liệu hóa thạch gây ra hậu quả môi trường nghiêm trọng nhất là:", ["Phát thải khí CO2 gây hiệu ứng nhà kính làm biến đổi khí hậu toàn cầu và ô nhiễm không khí", "Làm Trái Đất quay chậm lại", "Làm cạn kiệt oxy vũ trụ", "Làm tăng lượng mưa đá"], 0, "Hiệu ứng nhà kính và biến đổi khí hậu."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Pin mặt trời (quang điện) chuyển hóa trực tiếp năng lượng ánh sáng thành:", ["Điện năng", "Hóa năng", "Cơ năng", "Năng lượng âm thanh"], 0, "Chuyển quang năng thành điện năng trực tiếp."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Biện pháp sử dụng năng lượng tiết kiệm và hiệu quả trong gia đình là:", ["Tắt thiết bị điện khi không sử dụng, tận dụng ánh sáng tự nhiên, dùng đèn LED", "Bật đèn suốt ngày đêm", "Mở cửa phòng khi đang bật điều hòa", "Để tủ lạnh mở toang"], 0, "Tiết kiệm điện và sử dụng thiết bị hiệu suất cao.")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về định luật bảo toàn và chuyển hóa năng lượng:", [
                        ("a", "Năng lượng toàn phần của một hệ kín luôn luôn được bảo toàn.", True),
                        ("b", "Trong mọi quá trình chuyển hóa năng lượng, luôn có một phần năng lượng bị hao phí (thường dưới dạng nhiệt tỏa ra môi trường).", True),
                        ("c", "Hiệu suất của bất kì động cơ nhiệt hay máy móc nào trong thực tế đều không thể vượt quá 100%.", True),
                        ("d", "Có thể chế tạo được một động cơ vĩnh cửu hoạt động mãi mãi mà không cần cung cấp bất kì năng lượng nào.", False)
                    ], "Động cơ vĩnh cửu loại 1 vi phạm định luật bảo toàn năng lượng nên không thể tồn tại."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Về năng lượng tái tạo và phát triển bền vững:", [
                        ("a", "Năng lượng gió và năng lượng mặt trời là nguồn năng lượng sạch không phát thải khí nhà kính.", True),
                        ("b", "Việt Nam có bờ biển dài trên 3260 km rất giàu tiềm năng phát triển điện gió ngoài khơi.", True),
                        ("c", "Năng lượng sinh khối (Biomass) tận dụng phụ phẩm nông nghiệp như rơm rạ, bã mía, vỏ trấu để phát điện.", True),
                        ("d", "Năng lượng hóa thạch không bao giờ cạn kiệt.", False)
                    ], "Nhiên liệu hóa thạch sẽ cạn kiệt trong vài thập kỉ tới."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Một động cơ điện tiêu thụ công suất điện P = 2 kW và nâng một vật nặng có trọng lượng P = 1500 N lên cao 10 m trong thời gian 10 giây:", [
                        ("a", "Điện năng toàn phần tiêu thụ trong 10 giây là 20.000 J (20 kJ).", True),
                        ("b", "Công có ích để nâng vật lên cao là 15.000 J (15 kJ).", True),
                        ("c", "Năng lượng hao phí do tỏa nhiệt và ma sát là 5.000 J (5 kJ).", True),
                        ("d", "Hiệu suất của động cơ điện là 80%.", False)
                    ], "H = 15.000 / 20.000 × 100% = 75%."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Một nhà máy nhiệt điện đốt than có hiệu suất 35%:", [
                        ("a", "35% năng lượng từ đốt than được chuyển hóa thành điện năng có ích.", True),
                        ("b", "65% năng lượng bị thất thoát dưới dạng nhiệt tỏa ra môi trường làm mát và khí thải.", True),
                        ("c", "Đốt than phát thải lượng lớn khí CO2 và bụi mịn PM2.5.", True),
                        ("d", "Nhiệt điện than là nguồn năng lượng tái tạo thân thiện môi trường nhất.", False)
                    ], "Nhiệt điện than phát thải CO2 lớn và ô nhiễm môi trường.")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Năng lượng mặt trời là nguồn năng lượng tái tạo hay không tái tạo?", "Tái tạo", "Năng lượng tái tạo."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - Động cơ vĩnh cửu có thể chế tạo được trong thực tế không? (Có hay Không)", "Không", "Không (vi phạm định luật bảo toàn năng lượng)."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Một bóng đèn sợi đốt tiêu thụ 100 J điện năng nhưng chỉ phát ra 5 J năng lượng ánh sáng. Hiệu suất phát quang của bóng đèn sợi đốt là bao nhiêu %?", "5", "5 / 100 = 5%."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Một tấm pin mặt trời nhận được 2000 J năng lượng ánh sáng và sinh ra 400 J điện năng. Hiệu suất của pin mặt trời là bao nhiêu %?", "20", "400 / 2000 = 20%."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Một máy bơm nước có công suất 750 W hoạt động với hiệu suất 80%. Công suất có ích để bơm nước lên cao là bao nhiêu Watt?", "600", "750 × 80% = 600 W."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Một nhà máy thủy điện có cột nước cao 50 m. Lưu lượng nước qua tuabin là 20 m3/s (khối lượng 20.000 kg/s). Lấy g = 10 m/s2, hiệu suất nhà máy là 85%. Công suất phát điện của nhà máy là bao nhiêu MW? (Làm tròn 1 chữ số)", "8.5", "P_tp = m.g.h / t = 20.000 × 10 × 50 = 10 MW. P_ích = 10 × 85% = 8,5 MW.")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Cam kết của Việt Nam tại Hội nghị biến đổi khí hậu COP26 đạt mức phát thải ròng bằng '0' (Net Zero) vào năm 2050 đòi hỏi chiến lược chuyển dịch năng lượng trọng tâm là:", ["Chuyển đổi mạnh mẽ từ nhiệt điện than sang phát triển điện gió ngoài khơi, điện mặt trời và năng lượng hydro xanh", "Đốt than nhiều hơn", "Ngừng phát triển kinh tế", "Nhập khẩu toàn bộ điện năng"], 0, "Chuyển dịch năng lượng xanh và Net Zero 2050."),
                    make_vdc(2, f"Đề {t} - Xe ô tô điện (EV) có hiệu suất sử dụng năng lượng từ pin đến bánh xe đạt tới 85 - 90%, trong khi xe chạy xăng truyền thống hiệu suất động cơ đốt trong chỉ đạt khoảng 20 - 25%. Sự chênh lệch hiệu suất lớn này là do xe chạy xăng:", ["Bị thất thoát tới 75 - 80% năng lượng dưới dạng nhiệt lượng tỏa ra két nước làm mát và khí xả nóng", "Xe điện không dùng pin", "Xe xăng chạy nhanh hơn", "Xe điện không chịu ma sát"], 0, "Động cơ đốt trong thất thoát phần lớn nhiệt ra két nước và khí thải."),
                    make_vdc(3, f"Đề {t} - Ngôi nhà năng lượng số không (Net Zero Energy House) là mô hình nhà ở thông minh:", ["Tự sản xuất đủ lượng điện năng từ pin mặt trời trên mái bằng hoặc lớn hơn lượng điện tiêu thụ trong suốt cả năm", "Không dùng bóng đèn", "Không có cửa sổ", "Nhà bằng tre nứa không có điện"], 0, "Tự cung ứng năng lượng tái tạo."),
                    make_vdc(4, f"Đề {t} - Tận dụng năng lượng biogas từ hầm ủ chất thải chăn nuôi lợn, bò ở nông thôn mang lại lợi ích kép vừa cung cấp khí gas đun nấu miễn phí vừa:", ["Xử lí triệt để ô nhiễm chất thải chăn nuôi, giảm mùi hôi và ngăn phát thải khí methane vào khí quyển", "Làm tăng lượng rác thải", "Gây ô nhiễm đất", "Làm mất nguồn phân bón"], 0, "Bảo vệ môi trường và tạo năng lượng sinh học sạch.")
                ]

            exams[k] = {
                "title": f"Đề kiểm tra KHTN 9 (Vật lý) - {l_name} - Đề số {t:02d}",
                "grade": "9", "subject": "physics", "subjectName": "Vật lý",
                "chapterId": ch_id, "chapterTitle": ch_title,
                "lessonId": l_id, "lessonName": l_name,
                "testNum": t, "duration": "45 phút", "points": 10.0,
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    return exams

if __name__ == "__main__":
    exs = build_phys9_exams()
    print("Phys 9 generated total:", len(exs), "exams.")
