# make_phys8_c5_part2.py
# Generates build_phys8_c5_part2.py with 14 exams:
# b23 (3), b24 (3), b25 (3), rev (5)
import os

content = '''# -*- coding: utf-8 -*-
# build_phys8_c5_part2.py - Chapter V Part 2 (14 exams: b23 (3), b24 (3), b25 (3), rev (5))

def make_b23_test(t):
    # Bài 23: Tác dụng của dòng điện (t = 1, 2, 3)
    p_dev = ["bàn là điện", "nồi cơm điện", "bình nóng lạnh"][t-1]
    p_chem = ["đồng (Cu)", "bạc (Ag)", "vàng (Au)"][t-1]
    p_salt = ["dung dịch copper sulfate (CuSO4)", "dung dịch silver nitrate (AgNO3)", "dung dịch muối vàng dicyanoaurate"][t-1]
    p_core = ["lõi sắt non", "lõi thép mềm", "thanh sắt non"][t-1]
    p_turn = [200, 300, 500][t-1]
    p_volt = [6, 12, 24][t-1]

    mc = [
        {
            "q": f"Tác dụng nào sau đây của dòng điện được ứng dụng chủ yếu trong hoạt động của {p_dev}?",
            "options": ["A. Tác dụng nhiệt.", "B. Tác dụng từ.", "C. Tác dụng hóa học.", "D. Tác dụng sinh lí."],
            "answer": "A",
            "explanation": f"{p_dev.capitalize()} chuyển hóa điện năng thành nhiệt năng nhờ tác dụng nhiệt của dòng điện."
        },
        {
            "q": f"Trong kĩ thuật mạ {p_chem}, vật cần mạ phải được nối với cực nào của nguồn điện và nhúng vào {p_salt}?",
            "options": ["A. Nối với cực âm của nguồn điện.", "B. Nối với cực dương của nguồn điện.", "C. Nối với cực nào cũng được.", "D. Không cần nối với nguồn điện."],
            "answer": "A",
            "explanation": f"Trong công nghệ mạ điện, kim loại {p_chem} từ dung dịch điện phân sẽ di chuyển và bám đều lên vật nối với cực âm (catot)."
        },
        {
            "q": f"Khi cho dòng điện chạy qua cuộn dây dẫn quấn quanh {p_core}, cuộn dây có khả năng hút đinh sắt. Hiện tượng này thể hiện tác dụng gì của dòng điện?",
            "options": ["A. Tác dụng từ.", "B. Tác dụng nhiệt.", "C. Tác dụng phát quang.", "D. Tác dụng hóa học."],
            "answer": "A",
            "explanation": "Dòng điện chạy qua cuộn dây sinh ra từ trường, hút các vật bằng sắt, thép, đó là tác dụng từ."
        },
        {
            "q": f"Bóng đèn bút thử điện phát sáng khi chạm vào điểm có điện áp khoảng từ {40 + t*10} V trở lên là nhờ tác dụng nào của dòng điện?",
            "options": ["A. Tác dụng phát sáng (tác dụng quang).", "B. Tác dụng nhiệt dây tóc.", "C. Tác dụng từ của khí neon.", "D. Tác dụng hóa học."],
            "answer": "A",
            "explanation": "Khí neon trong bút thử điện phát sáng do hiện tượng phóng điện trong chất khí, thể hiện tác dụng phát sáng."
        },
        {
            "q": f"Thiết bị nào sau đây KHÔNG hoạt động dựa trên tác dụng nhiệt của dòng điện trong đời sống gia đình nhóm {t}?",
            "options": ["A. Quạt điện gia đình.", f"B. {p_dev.capitalize()}.", "C. Ấm đun nước siêu tốc.", "D. Máy sấy tóc (bộ phận đốt nóng)."],
            "answer": "A",
            "explanation": "Quạt điện hoạt động dựa trên tác dụng từ của dòng điện (làm quay động cơ), không phải tác dụng nhiệt."
        },
        {
            "q": f"Khi người vô tình chạm vào dây dẫn trần có điện thế nguy hiểm {110 + t*55} V, dòng điện chạy qua cơ thể gây co giật cơ. Đây là biểu hiện của tác dụng nào?",
            "options": ["A. Tác dụng sinh lí.", "B. Tác dụng nhiệt.", "C. Tác dụng từ.", "D. Tác dụng quang."],
            "answer": "A",
            "explanation": "Dòng điện đi qua cơ thể sinh vật gây co giật cơ, tác động lên hệ thần kinh và tim mạch, đó là tác dụng sinh lí."
        },
        {
            "q": f"Để chế tạo nam châm điện có từ tính mạnh nhất với cùng cường độ dòng điện, người ta thường quấn {p_turn} vòng dây quanh lõi nào?",
            "options": ["A. Lõi sắt non.", "B. Lõi đồng nguyên chất.", "C. Lõi nhôm đúc.", "D. Lõi gỗ khô."],
            "answer": "A",
            "explanation": "Sắt non có khả năng tăng cường từ trường rất mạnh và mất từ tính nhanh khi ngắt điện, rất thích hợp làm nam châm điện."
        },
        {
            "q": f"Đèn LED (điốt phát quang) chỉ cho dòng điện chạy qua và phát sáng khi chốt dương của đèn được nối với cực nào của nguồn {p_volt} V?",
            "options": ["A. Cực dương của nguồn điện.", "B. Cực âm của nguồn điện.", "C. Cả hai cực cùng lúc.", "D. Không phụ thuộc vào cực nguồn."],
            "answer": "A",
            "explanation": "Đèn LED chỉ dẫn điện theo một chiều nhất định (cực dương đèn nối với cực dương nguồn điện)."
        },
        {
            "q": f"Trong y học hiện đại, máy sốc tim dùng một xung điện có năng lượng thích hợp truyền qua ngực bệnh nhân ngừng tim để hồi sức tim phổi. Ứng dụng này dựa vào tác dụng gì?",
            "options": ["A. Tác dụng sinh lí.", "B. Tác dụng hóa học.", "C. Tác dụng quang học.", "D. Tác dụng làm nóng."],
            "answer": "A",
            "explanation": "Kích thích cơ tim bằng xung điện là ứng dụng chữa bệnh của tác dụng sinh lí dòng điện."
        },
        {
            "q": f"Tác dụng từ của dòng điện được ứng dụng trong thiết bị nào sau đây ở nhóm thí nghiệm {t}?",
            "options": ["A. Chuông điện báo động.", "B. Bình đun nước giữ nhiệt.", "C. Đèn sợi đốt thắp sáng.", "D. Bàn là khô gia đình."],
            "answer": "A",
            "explanation": "Chuông điện dùng nam châm điện để hút lá thép gõ vào chuông, hoạt động nhờ tác dụng từ."
        },
        {
            "q": f"Hiện tượng cầu chì tự động ngắt mạch (dây chì bị nóng chảy đứt) khi xảy ra sự cố chập điện dựa vào tác dụng nào?",
            "options": ["A. Tác dụng nhiệt của dòng điện quá tải.", "B. Tác dụng từ hút đứt dây chì.", "C. Tác dụng hóa học làm tan chì.", "D. Tác dụng phát sáng làm cháy chì."],
            "answer": "A",
            "explanation": "Khi đoản mạch, dòng điện tăng rất lớn làm dây chì nóng chảy và đứt, ngắt mạch để bảo vệ an toàn."
        },
        {
            "q": f"Khi nhúng hai điện cực than chì nối với hai cực của acquy vào bình đựng {p_salt}, sau một thời gian thấy bám một lớp {p_chem} đỏ/sáng ở điện cực âm. Đây là bằng chứng của tác dụng gì?",
            "options": ["A. Tác dụng hóa học.", "B. Tác dụng cơ học.", "C. Tác dụng phát quang.", "D. Tác dụng từ tính."],
            "answer": "A",
            "explanation": "Dòng điện phân li muối kim loại và giải phóng kim loại bám ở điện cực âm, chứng minh tác dụng hóa học."
        }
    ]

    tf = [
        {
            "q": f"Xét các phát biểu về các tác dụng đa dạng của dòng điện trong đời sống và kỹ thuật thực nghiệm mẫu {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Dòng điện luôn luôn chỉ gây ra một tác dụng duy nhất khi đi qua bất kì thiết bị tiêu thụ điện nào.",
                    "answer": False,
                    "explanation": "Sai. Dòng điện có thể đồng thời gây ra nhiều tác dụng (ví dụ bóng đèn sợi đốt vừa tỏa nhiệt vừa phát sáng)."
                },
                {
                    "id": "b",
                    "text": f"Trong thiết bị {p_dev}, tác dụng nhiệt là tác dụng có ích, tỏa nhiệt để phục vụ mục đích sử dụng.",
                    "answer": True,
                    "explanation": f"Đúng. {p_dev.capitalize()} được chế tạo với mục đích chính là phát nhiệt hữu ích."
                },
                {
                    "id": "c",
                    "text": "Kim nam châm đặt tự do sẽ bị lệch khỏi hướng Bắc - Nam địa từ khi đặt gần dây dẫn có dòng điện chạy qua.",
                    "answer": True,
                    "explanation": "Đúng. Dòng điện sinh ra từ trường tác dụng lực từ làm quay kim nam châm."
                },
                {
                    "id": "d",
                    "text": "Dòng điện đi qua dung dịch nước cất tinh khiết sẽ tạo ra phản ứng mạ điện cực kì mạnh mẽ.",
                    "answer": False,
                    "explanation": "Sai. Nước cất tinh khiết là chất cách điện (rất ít ion tự do), không dẫn điện để tạo phản ứng mạ."
                }
            ]
        },
        {
            "q": f"Một học sinh tiến hành thí nghiệm chế tạo nam châm điện học đường với cuộn dây {p_turn} vòng và nguồn {p_volt} V:",
            "statements": [
                {
                    "id": "a",
                    "text": f"Khi tăng số vòng dây từ {p_turn} lên {p_turn + 200} vòng, từ tính của nam châm điện sẽ tăng lên.",
                    "answer": True,
                    "explanation": "Đúng. Lực từ của nam châm điện tăng khi số vòng dây cuộn tăng lên."
                },
                {
                    "id": "b",
                    "text": "Khi ngắt công tắc điện, lõi sắt non vẫn giữ nguyên từ tính vĩnh cửu và tiếp tục hút đinh sắt vô hạn định.",
                    "answer": False,
                    "explanation": "Sai. Lõi sắt non mất hầu hết từ tính gần như ngay lập tức khi ngắt dòng điện."
                },
                {
                    "id": "c",
                    "text": "Nếu thay lõi sắt non bằng thanh nhôm thì cuộn dây sẽ hút đinh sắt mạnh hơn gấp nhiều lần.",
                    "answer": False,
                    "explanation": "Sai. Nhôm không phải vật liệu dẫn từ tốt như sắt son, không tạo thành nam châm điện mạnh."
                },
                {
                    "id": "d",
                    "text": "Khi đổi chiều dòng điện chạy qua cuộn dây thì các cực từ (Bắc - Nam) của nam châm điện sẽ đổi chiều.",
                    "answer": True,
                    "explanation": "Đúng. Đổi chiều dòng điện làm đảo cực từ của cuộn dây có lõi sắt non."
                }
            ]
        },
        {
            "q": f"Đánh giá về tác dụng phát sáng và tác dụng hóa học của dòng điện trong thực tiễn nhóm {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Bóng đèn sợi đốt phát sáng do dây tóc vonfram bị nung nóng đến nhiệt độ rất cao (khoảng 2500°C).",
                    "answer": True,
                    "explanation": "Đúng. Đèn sợi đốt biến đổi điện năng thành nhiệt năng, sau đó phát quang do nóng sáng."
                },
                {
                    "id": "b",
                    "text": "Đèn LED phát sáng tiêu tốn ít điện năng và tỏa rất ít nhiệt hơn nhiều so với đèn sợi đốt cùng độ sáng.",
                    "answer": True,
                    "explanation": "Đúng. Đèn LED phát quang bán dẫn trực tiếp, hiệu suất phát sáng cao, ít tỏa nhiệt."
                },
                {
                    "id": "c",
                    "text": f"Khi mạ {p_chem}, thanh kim loại {p_chem} nguyên chất được gắn vào cực âm của nguồn điện một chiều.",
                    "answer": False,
                    "explanation": f"Sai. Thanh {p_chem} nguyên chất được nối vào cực dương (anot) để hòa tan bù vào dung dịch, vật cần mạ mới nối cực âm."
                },
                {
                    "id": "d",
                    "text": "Dòng điện một chiều và dòng điện xoay chiều đều có thể dùng để mạ điện với hiệu quả như nhau.",
                    "answer": False,
                    "explanation": "Sai. Mạ điện bắt buộc phải dùng dòng điện một chiều để ion kim loại dịch chuyển về một cực cố định."
                }
            ]
        },
        {
            "q": f"Xem xét về tác dụng sinh lí và quy tắc phòng tránh tai nạn điện giật tại phòng thí nghiệm trường học mức {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Dòng điện xoay chiều có cường độ khoảng 10 mA trở lên chạy qua cơ thể người đã có thể gây co giật cơ nguy hiểm không tự buông tay ra được.",
                    "answer": True,
                    "explanation": "Đúng. Dòng điện khoảng 10-15 mA gây co cơ mạnh khiến nạn nhân bị dính chặt vào dây dẫn."
                },
                {
                    "id": "b",
                    "text": "Người bị điện giật chỉ bị thương tích do bỏng nhiệt, hoàn toàn không bị ảnh hưởng đến tim và hệ hô hấp.",
                    "answer": False,
                    "explanation": "Sai. Dòng điện gây tê liệt trung tâm hô hấp và làm rung tâm thất, gây ngừng tim đột ngột."
                },
                {
                    "id": "c",
                    "text": "Khi phát hiện người bị điện giật, việc đầu tiên cần làm ngay lập tức là ngắt cầu dao điện hoặc dùng vật cách điện khô gạt dây điện ra.",
                    "answer": True,
                    "explanation": "Đúng. Phải nhanh chóng ngắt nguồn điện an toàn trước khi tiến hành sơ cứu."
                },
                {
                    "id": "d",
                    "text": "Có thể dùng tay trần nắm chặt cánh tay người bị nạn để kéo ra khỏi khu vực nhiễm điện 220 V.",
                    "answer": False,
                    "explanation": "Sai. Người cứu hộ sẽ bị dòng điện truyền qua và bị điện giật theo."
                }
            ]
        }
    ]

    mass_val = round(0.05 * t * 12, 2)
    sa = [
        {
            "q": f"Một ấm đun nước điện tiêu thụ dòng điện có cường độ {2.0 + t*0.5:.1f} A dưới hiệu điện thế 220 V. Tính công suất điện tỏa nhiệt của ấm đun (theo đơn vị W).",
            "answer": f"{round((2.0 + t*0.5)*220)}",
            "unit": "W",
            "explanation": f"P = U * I = 220 * {2.0 + t*0.5:.1f} = {round((2.0 + t*0.5)*220)} W."
        },
        {
            "q": f"Một nam châm điện dùng cuộn dây {p_turn} vòng hút được {10 + t*5} chiếc đinh sắt nhỏ. Khi tăng số vòng dây thêm {100*t} vòng mà giữ nguyên cường độ dòng điện, số đinh hút được tăng lên {18 + t*7} chiếc. Số đinh hút thêm được là bao nhiêu chiếc?",
            "answer": f"{(18 + t*7) - (10 + t*5)}",
            "unit": "chiếc",
            "explanation": f"Số đinh hút thêm = {(18 + t*7)} - {(10 + t*5)} = {(18 + t*7) - (10 + t*5)} chiếc."
        },
        {
            "q": f"Trong một thí nghiệm mạ bạc, người ta cho dòng điện không đổi chạy qua bình điện phân trong {15*t} phút và thu được {0.2 * t:.2f} g bạc bám vào cực âm. Tính khối lượng bạc (gam) bám vào cực âm nếu thời gian mạ tăng gấp 3 lần với cùng cường độ dòng điện.",
            "answer": f"{round(0.2 * t * 3, 2)}",
            "unit": "g",
            "explanation": f"Khối lượng mạ tỉ lệ thuận với thời gian: m = {0.2 * t:.2f} * 3 = {round(0.2 * t * 3, 2)} g."
        },
        {
            "q": f"Một đèn LED chỉ sáng khi hiệu điện thế đặt vào hai đầu từ {1.8 + t*0.2:.1f} V trở lên. Người ta dùng nguồn pin {p_volt} V mắc nối tiếp với một điện trở để thắp sáng đèn LED với điện áp trên LED đúng {1.8 + t*0.2:.1f} V. Hiệu điện thế giữa hai đầu điện trở bằng bao nhiêu vôn?",
            "answer": f"{round(p_volt - (1.8 + t*0.2), 2)}",
            "unit": "V",
            "explanation": f"U_R = U_nguon - U_LED = {p_volt} - {1.8 + t*0.2:.1f} = {round(p_volt - (1.8 + t*0.2), 2)} V."
        },
        {
            "q": f"Bút thử điện chứa khí neon có điện trở rất lớn R = {1.0 + t*0.2:.1f} MΩ (1 MΩ = 1 000 000 Ω). Khi thử nguồn điện 220 V, cường độ dòng điện an toàn qua cơ thể người xuống đất bằng bao nhiêu miliampe (mA)? (Làm tròn đến 3 chữ số thập phân).",
            "answer": f"{round(220 / ((1.0 + t*0.2)*1000000) * 1000, 3)}",
            "unit": "mA",
            "explanation": f"I = U / R = 220 / {(1.0 + t*0.2)*1000000:.0f} A = {220 / ((1.0 + t*0.2)*1000):.3f} mA."
        },
        {
            "q": f"Một cần cẩu điện sử dụng nam châm điện có khả năng nâng tối đa khối lượng sắt vụn là {500 + t*250} kg trong mỗi lần cẩu. Lực từ nâng tối thiểu do nam châm tác dụng lên khối sắt này bằng bao nhiêu niutơn (N)? (Lấy g = 10 m/s2).",
            "answer": f"{(500 + t*250)*10}",
            "unit": "N",
            "explanation": f"F = P = m * g = {(500 + t*250)} * 10 = {(500 + t*250)*10} N."
        }
    ]

    vdc = [
        {
            "q": f"Một nhà máy sản xuất sử dụng bể mạ điện cực lớn để mạ {p_chem} cho {100 * t} chi tiết máy hình trụ giống nhau. Mỗi chi tiết có diện tích bề mặt cần mạ là {0.02 + t*0.01:.2f} m2. Lớp mạ yêu cầu có độ dày đồng đều là {20 + t*10} μm (1 μm = 10^-6 m). Biết khối lượng riêng của {p_chem} là D = {8900 if 'đồng' in p_chem else 10500 if 'bạc' in p_chem else 19300} kg/m3. Hãy tính tổng thể tích lớp mạ (cm3) và tổng khối lượng kim loại {p_chem} (kg) cần mạ cho toàn bộ lô hàng trên.",
            "type": "vdc",
            "solution": f"1. Diện tích bề mặt của 1 chi tiết: S1 = {0.02 + t*0.01:.2f} m2.\\n"
                        f"Tổng diện tích mạ cho {100*t} chi tiết: S = {100*t} * {0.02 + t*0.01:.2f} = {round(100*t * (0.02 + t*0.01), 2)} m2.\\n"
                        f"2. Độ dày lớp mạ: h = {20 + t*10} * 10^-6 m.\\n"
                        f"Tổng thể tích kim loại mạ: V = S * h = {round(100*t * (0.02 + t*0.01), 2)} * ({20 + t*10} * 10^-6) = {round(100*t * (0.02 + t*0.01) * (20 + t*10) * 1e-6, 6)} m3 = {round(100*t * (0.02 + t*0.01) * (20 + t*10), 2)} cm3.\\n"
                        f"3. Khối lượng kim loại cần mạ: m = D * V = {8900 if 'đồng' in p_chem else 10500 if 'bạc' in p_chem else 19300} * {round(100*t * (0.02 + t*0.01) * (20 + t*10) * 1e-6, 6)} = {round((8900 if 'đồng' in p_chem else 10500 if 'bạc' in p_chem else 19300) * 100*t * (0.02 + t*0.01) * (20 + t*10) * 1e-6, 3)} kg."
        },
        {
            "q": f"Một hệ thống chuông điện báo cháy hoạt động dựa trên tác dụng nhiệt làm nở thanh lưỡng kim (rơle nhiệt) kết hợp với tác dụng từ của nam châm điện. Ở nhiệt độ bình thường (25°C), tiếp điểm hở. Khi nhiệt độ khu vực đạt {60 + t*10}°C, băng kép uốn cong đóng mạch điện cho nam châm điện hoạt động với nguồn {p_volt} V. Nam châm điện có điện trở R = {12 + t*4} Ω hút lá thép kéo búa gõ chuông với tần số {10 + t*2} lần/giây. Hãy phân tích các biến đổi năng lượng xảy ra trong hệ thống và tính cường độ dòng điện chạy qua cuộn dây nam châm điện khi chuông reo.",
            "type": "vdc",
            "solution": f"1. Biến đổi năng lượng:\\n"
                        f"- Giai đoạn 1: Nhiệt năng môi trường làm biến dạng cơ học thanh lưỡng kim (nhiệt năng -> cơ năng) để đóng mạch điện.\\n"
                        f"- Giai đoạn 2: Điện năng từ nguồn {p_volt} V cung cấp dòng điện qua cuộn dây, chuyển hóa thành từ trường (tác dụng từ của dòng điện).\\n"
                        f"- Giai đoạn 3: Lực từ tác dụng hút lá thép làm búa gõ vào chuông tạo ra âm thanh (từ năng -> cơ năng -> âm thanh).\\n"
                        f"2. Cường độ dòng điện qua nam châm điện khi hoạt động:\\n"
                        f"Áp dụng định luật Ohm: I = U / R = {p_volt} / {12 + t*4} = {round(p_volt / (12 + t*4), 3)} A."
        },
        {
            "q": f"Trong thí nghiệm nghiên cứu sự phụ thuộc của lực từ vào cường độ dòng điện, một nhóm học sinh mắc cuộn dây nam châm điện nối tiếp với một biến trở và ampe kế vào nguồn điện không đổi {p_volt} V. Khi điều chỉnh biến trở có giá trị R1 = {8 + t*2} Ω, dòng điện qua cuộn dây là I1 = {round(p_volt / (8 + t*2 + 2), 2)} A (cuộn dây có điện trở trong r = 2 Ω) và nam châm hút được quả nặng m1 = {150 + t*50} g. Khi điều chỉnh biến trở giảm còn R2 = {4 + t} Ω, hãy tính dòng điện I2 lúc này và ước lượng khối lượng quả nặng m2 mà nam châm có thể giữ được, giả thiết lực từ tỉ lệ thuận với bình phương cường độ dòng điện.",
            "type": "vdc",
            "solution": f"1. Điện trở toàn phần của mạch:\\n"
                        f"- Ban đầu: R_tp1 = R1 + r = {8 + t*2} + 2 = {10 + t*2} Ω. I1 = {p_volt} / {10 + t*2} = {round(p_volt / (10 + t*2), 3)} A.\\n"
                        f"- Khi giảm biến trở: R_tp2 = R2 + r = {4 + t} + 2 = {6 + t} Ω. I2 = {p_volt} / {6 + t} = {round(p_volt / (6 + t), 3)} A.\\n"
                        f"2. Tỉ số cường độ dòng điện: k = I2 / I1 = {10 + t*2} / {6 + t} = {round((10 + t*2) / (6 + t), 3)}.\\n"
                        f"Vì lực từ F tỉ lệ thuận với bình phương cường độ dòng điện (F ~ I^2) nên khả năng nâng quả nặng m2 thỏa mãn:\\n"
                        f"m2 / m1 = (I2 / I1)^2 = k^2 = ({round((10 + t*2) / (6 + t), 3)})^2 = {round(((10 + t*2) / (6 + t))**2, 3)}.\\n"
                        f"=> m2 = m1 * k^2 = {150 + t*50} * {round(((10 + t*2) / (6 + t))**2, 3)} = {round((150 + t*50) * (((10 + t*2) / (6 + t))**2), 1)} g."
        },
        {
            "q": f"Một bình nước nóng năng lượng mặt trời kết hợp bộ đốt điện dự phòng công suất {1500 + t*200} W (hoạt động dựa trên tác dụng nhiệt của dòng điện). Bình chứa {80 + t*20} lít nước. Vào mùa đông, nước trong bình ở {18 + t}°C cần được đun nóng lên đến 60°C. Biết nhiệt dung riêng của nước c = 4200 J/(kg.K), khối lượng riêng của nước D = 1000 kg/m3 và hiệu suất nhiệt của thanh đốt điện đạt {85 + t}%. Tính nhiệt lượng có ích cần cung cấp cho nước, điện năng tiêu thụ thực tế (theo đơn vị kWh) và thời gian đun nước (phút).",
            "type": "vdc",
            "solution": f"1. Khối lượng nước trong bình: m = V * D = ({80 + t*20} * 10^-3) * 1000 = {80 + t*20} kg.\\n"
                        f"Độ tăng nhiệt độ của nước: Δt = 60 - {18 + t} = {60 - (18 + t)}°C.\\n"
                        f"Nhiệt lượng có ích làm nóng nước: Q_ci = m * c * Δt = {80 + t*20} * 4200 * {60 - (18 + t)} = {(80 + t*20) * 4200 * (60 - (18 + t))} J = {round((80 + t*20) * 4200 * (60 - (18 + t)) / 1000000, 3)} MJ.\\n"
                        f"2. Điện năng tiêu thụ thực tế:\\n"
                        f"A_tp = Q_ci / H = {(80 + t*20) * 4200 * (60 - (18 + t))} / ({85 + t}/100) = {round((80 + t*20) * 4200 * (60 - (18 + t)) / ((85 + t)/100))} J\\n"
                        f"Đổi sang kWh: A_tp = {round((80 + t*20) * 4200 * (60 - (18 + t)) / ((85 + t)/100) / 3600000, 3)} kWh.\\n"
                        f"3. Thời gian đun nóng:\\n"
                        f"t_giay = A_tp / P = {round((80 + t*20) * 4200 * (60 - (18 + t)) / ((85 + t)/100))} / {1500 + t*200} = {round((80 + t*20) * 4200 * (60 - (18 + t)) / ((85 + t)/100) / (1500 + t*200), 1)} giây = {round((80 + t*20) * 4200 * (60 - (18 + t)) / ((85 + t)/100) / (1500 + t*200) / 60, 2)} phút."
        }
    ]

    return {
        "id": f"phys8_c5_b23_test{t}",
        "title": f"KHTN 8 - Bài 23: Tác dụng của dòng điện - Đề {t}",
        "subject": "KHTN 8 - Vật lí",
        "duration": 45,
        "parts": {
            "part1": mc,
            "part2": tf,
            "part3": sa,
            "vdc": vdc
        }
    }


def make_b24_test(t):
    # Bài 24: Cường độ dòng điện và hiệu điện thế (t = 1, 2, 3)
    p_mA = [150 + t*50, 240 + t*60, 350 + t*50][t-1]
    p_kV = [0.22 + t*0.05, 0.38 + t*0.1, 0.5 + t*0.2][t-1]
    p_bat = [1.5, 3.7, 9.0][t-1]
    p_meter = ["Ampe kế kim chỉ thị", "Ampe kế hiện số đa năng", "Milianpe kế điện tử"][t-1]

    mc = [
        {
            "q": f"Đơn vị đo cường độ dòng điện trong hệ thống đo lường quốc tế (SI) là gì?",
            "options": ["A. Ampe (A).", "B. Vôn (V).", "C. Oát (W).", "D. Jun (J)."],
            "answer": "A",
            "explanation": "Cường độ dòng điện có đơn vị đo là Ampe (kí hiệu là A)."
        },
        {
            "q": f"Dụng cụ nào sau đây được dùng để đo hiệu điện thế giữa hai đầu một thiết bị điện tiêu thụ nhóm {t}?",
            "options": ["A. Vôn kế.", "B. Ampe kế.", "C. Lực kế.", "D. Nhiệt kế."],
            "answer": "A",
            "explanation": "Vôn kế là dụng cụ chuyên dụng để đo hiệu điện thế (điện áp)."
        },
        {
            "q": f"Để đo cường độ dòng điện chạy qua một bóng đèn nhỏ, người ta phải mắc dụng cụ {p_meter} như thế nào với bóng đèn?",
            "options": ["A. Mắc nối tiếp với bóng đèn.", "B. Mắc song song với bóng đèn.", "C. Mắc vào hai cực của nguồn điện.", "D. Đặt gần bóng đèn không cần nối dây."],
            "answer": "A",
            "explanation": "Ampe kế phải được mắc nối tiếp với thiết bị cần đo để toàn bộ dòng điện qua thiết bị chạy qua ampe kế."
        },
        {
            "q": f"Một dòng điện có cường độ {p_mA} mA đổi sang đơn vị Ampe (A) có giá trị bằng bao nhiêu?",
            "options": [f"A. {p_mA / 1000} A.", f"B. {p_mA / 100} A.", f"C. {p_mA * 10} A.", f"D. {p_mA * 1000} A."],
            "answer": "A",
            "explanation": f"1 A = 1000 mA nên {p_mA} mA = {p_mA}/1000 = {p_mA / 1000} A."
        },
        {
            "q": f"Hiệu điện thế {p_kV} kV đổi ra đơn vị Vôn (V) có giá trị bằng bao nhiêu?",
            "options": [f"A. {round(p_kV * 1000)} V.", f"B. {round(p_kV * 100)} V.", f"C. {round(p_kV * 10)} V.", f"D. {round(p_kV * 10000)} V."],
            "answer": "A",
            "explanation": f"1 kV = 1000 V nên {p_kV} kV = {p_kV} * 1000 = {round(p_kV * 1000)} V."
        },
        {
            "q": f"Trên vỏ một viên pin có ghi {p_bat} V. Giá trị {p_bat} V này cho ta biết điều gì?",
            "options": [
                f"A. Hiệu điện thế giữa hai cực của pin khi chưa mắc vào mạch (mạch hở).",
                f"B. Cường độ dòng điện cực đại mà pin có thể phóng ra.",
                f"C. Lượng điện năng pin tích trữ được trong một giờ.",
                f"D. Khối lượng và kích thước tiêu chuẩn của pin."
            ],
            "answer": "A",
            "explanation": f"Số vôn ghi trên nguồn điện là hiệu điện thế định mức giữa hai cực khi mạch hở."
        },
        {
            "q": f"Khi sử dụng vôn kế để đo hiệu điện thế giữa hai đầu bóng đèn sợi đốt, ta cần mắc vôn kế như thế nào?",
            "options": [
                "A. Mắc song song với bóng đèn, chốt dương (+) nối về phía cực dương nguồn.",
                "B. Mắc nối tiếp với bóng đèn, chốt dương (+) nối về cực âm nguồn.",
                "C. Mắc nối tiếp với bóng đèn, chốt âm (-) nối về phía cực dương nguồn.",
                "D. Mắc trực tiếp vào hai chốt công tắc khi đóng."
            ],
            "answer": "A",
            "explanation": "Vôn kế mắc song song với đoạn mạch cần đo, chốt (+) về phía cực dương nguồn điện."
        },
        {
            "q": f"Cường độ dòng điện chạy qua một dây dẫn kim loại càng lớn khi nào trong bài học số {t}?",
            "options": [
                "A. Lượng điện tích dịch chuyển có hướng qua tiết diện dây trong 1 giây càng lớn.",
                "B. Dây dẫn có chiều dài càng dài và tiết diện càng nhỏ.",
                "C. Nhiệt độ dây dẫn càng tăng cao làm dây nóng đỏ.",
                "D. Khối lượng dây kim loại càng nặng."
            ],
            "answer": "A",
            "explanation": "Cường độ dòng điện I = q / t đặc trưng cho lượng điện tích chuyển qua tiết diện dây dẫn trong một đơn vị thời gian."
        },
        {
            "q": f"Giới hạn đo (GHĐ) và độ chia nhỏ nhất (ĐCNN) của một ampe kế có thang đo từ 0 đến {2 + t} A chia thành {20 + t*10} vạch đều nhau lần lượt là gì?",
            "options": [
                f"A. GHĐ là {2 + t} A, ĐCNN là {round((2+t)/(20+t*10), 3)} A.",
                f"B. GHĐ là {round((2+t)/(20+t*10), 3)} A, ĐCNN là {2 + t} A.",
                f"C. GHĐ là 10 A, ĐCNN là 0,1 A.",
                f"D. GHĐ là {20 + t*10} A, ĐCNN là 1 A."
            ],
            "answer": "A",
            "explanation": f"GHĐ là giá trị lớn nhất trên thang đo ({2+t} A), ĐCNN là khoảng cách giữa 2 vạch chia liên tiếp: {round((2+t)/(20+t*10), 3)} A."
        },
        {
            "q": f"Một bóng đèn pin loại {p_bat} V sáng bình thường khi được mắc vào nguồn điện có hiệu điện thế nào sau đây?",
            "options": [f"A. Bằng đúng {p_bat} V.", f"B. Lớn hơn rất nhiều so với {p_bat * 3} V.", f"C. Bằng 0 V.", f"D. Nhỏ hơn {p_bat * 0.2:.1f} V."],
            "answer": "A",
            "explanation": "Thiết bị điện sáng/hoạt động bình thường khi hiệu điện thế cấp bằng đúng giá trị định mức ghi trên thiết bị."
        },
        {
            "q": f"Nếu mắc ampe kế trực tiếp vào hai cực của một acquy {6*t} V mà không có thiết bị tiêu thụ điện nào thì hiện tượng gì sẽ xảy ra?",
            "options": [
                "A. Ampe kế có thể bị hỏng (cháy) do dòng điện đoản mạch cực lớn.",
                "B. Kim ampe kế chỉ số 0 và đứng yên.",
                "C. Acquy sạc đầy điện nhanh chóng.",
                "D. Acquy tự động ngắt điện an toàn không có dòng."
            ],
            "answer": "A",
            "explanation": "Ampe kế có điện trở rất nhỏ, mắc trực tiếp vào nguồn sẽ gây đoản mạch làm cháy ampe kế và hỏng acquy."
        },
        {
            "q": f"Hiệu điện thế giữa hai điểm A và B trong mạch điện có giá trị U_AB = {12 + t*6} V nghĩa là gì?",
            "options": [
                f"A. Điện thế tại điểm A cao hơn điện thế tại điểm B là {12 + t*6} V.",
                f"B. Dòng điện qua đoạn AB luôn cố định {12 + t*6} A.",
                f"C. Năng lượng tiêu thụ giữa A và B là {12 + t*6} J.",
                f"D. Điện trở của đoạn dây AB là {12 + t*6} Ω."
            ],
            "answer": "A",
            "explanation": "Hiệu điện thế U_AB = V_A - V_B thể hiện độ chênh lệch điện thế giữa hai điểm A và B."
        }
    ]

    tf = [
        {
            "q": f"Xét các quy tắc thực hành sử dụng ampe kế và vôn kế trong giờ học thí nghiệm đợt {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Trước khi tiến hành đo, bắt buộc phải hiệu chỉnh kim của dụng cụ chỉ đúng vạch số 0 (chỉnh zero).",
                    "answer": True,
                    "explanation": "Đúng. Chỉnh kim về vạch 0 giúp triệt tiêu sai số hệ thống ban đầu."
                },
                {
                    "id": "b",
                    "text": "Nên chọn thang đo có GHĐ nhỏ hơn rất nhiều so với giá trị ước lượng cần đo để kim lệch tối đa khỏi bảng chia độ.",
                    "answer": False,
                    "explanation": "Sai. Phải chọn thang đo có GHĐ lớn hơn giá trị ước lượng để tránh làm kim va đập quá ngưỡng gây gãy kim, cháy thiết bị."
                },
                {
                    "id": "c",
                    "text": "Khi mắc vôn kế song song vào nguồn điện mạch hở, vôn kế đo được hiệu điện thế giữa hai cực của nguồn.",
                    "answer": True,
                    "explanation": "Đúng. Mạch hở không có dòng tải, vôn kế có điện trở rất lớn nên đo chính xác suất điện động / hiệu điện thế giữa hai cực nguồn."
                },
                {
                    "id": "d",
                    "text": "Có thể mắc ampe kế song song với nguồn điện để kiểm tra xem nguồn còn điện hay hết điện.",
                    "answer": False,
                    "explanation": "Sai. Tuyệt đối không mắc ampe kế song song với nguồn vì sẽ gây đoản mạch cháy ampe kế."
                }
            ]
        },
        {
            "q": f"Một mạch điện kín gồm nguồn điện {p_bat} V, công tắc K đóng, bóng đèn Đ và dây nối kim loại:",
            "statements": [
                {
                    "id": "a",
                    "text": "Khi công tắc K đóng, trong mạch xuất hiện dòng điện và bóng đèn phát sáng ngay lập tức.",
                    "answer": True,
                    "explanation": "Đúng. Điện trường lan truyền trong dây dẫn với tốc độ gần bằng tốc độ ánh sáng khiến electron dịch chuyển đồng loạt."
                },
                {
                    "id": "b",
                    "text": "Nếu ngắt công tắc K (mạch hở), hiệu điện thế giữa hai cực của pin sẽ tụt ngay lập tức về 0 V.",
                    "answer": False,
                    "explanation": "Sai. Khi mạch hở, hiệu điện thế giữa hai cực của pin vẫn giữ nguyên giá trị định mức (ví dụ 1.5V, 3.7V)."
                },
                {
                    "id": "c",
                    "text": "Cường độ dòng điện qua mọi tiết diện thẳng trên cùng một nhánh dây nối tiếp luôn bằng nhau.",
                    "answer": True,
                    "explanation": "Đúng. Tính liên tục của dòng điện trong mạch nối tiếp."
                },
                {
                    "id": "d",
                    "text": "Dòng điện chạy trong kim loại từ cực âm qua dây dẫn sang cực dương của nguồn điện.",
                    "answer": False,
                    "explanation": "Sai. Chiều quy ước của dòng điện là từ cực dương qua dây dẫn sang cực âm (ngược với chiều dịch chuyển của electron)."
                }
            ]
        },
        {
            "q": f"Đánh giá về sự thay đổi của cường độ dòng điện khi hiệu điện thế thay đổi trong thực nghiệm số {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Khi tăng hiệu điện thế đặt vào hai đầu một bóng đèn sợi đốt, cường độ dòng điện qua đèn cũng tăng lên.",
                    "answer": True,
                    "explanation": "Đúng. Hiệu điện thế tăng làm tăng lực điện trường tác dụng lên các hạt tải điện, tăng cường độ dòng điện."
                },
                {
                    "id": "b",
                    "text": "Cường độ dòng điện qua vật dẫn tỉ lệ nghịch với hiệu điện thế đặt vào hai đầu vật dẫn đó.",
                    "answer": False,
                    "explanation": "Sai. Cường độ dòng điện tỉ lệ thuận với hiệu điện thế giữa hai đầu vật dẫn (định luật Ohm)."
                },
                {
                    "id": "c",
                    "text": "Khi hiệu điện thế giữa hai đầu bóng đèn bằng 0 V thì không có dòng điện nào chạy qua đèn.",
                    "answer": True,
                    "explanation": "Đúng. Không có hiệu điện thế thì không có dòng điện chạy qua vật tiêu thụ (I = 0)."
                },
                {
                    "id": "d",
                    "text": f"Nếu đặt vào đèn {p_bat} V một hiệu điện thế {p_bat * 2} V trong thời gian dài, đèn sẽ sáng bền hơn bình thường.",
                    "answer": False,
                    "explanation": "Sai. Quá điện áp định mức sẽ làm dây tóc quá nóng và bị cháy đứt bóng đèn."
                }
            ]
        },
        {
            "q": f"Xem xét về số electron tự do dịch chuyển và cường độ dòng điện trong dây đồng bài tập {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Điện tích của một electron là e = -1,6 . 10^-19 Culông (C).",
                    "answer": True,
                    "explanation": "Đúng. Điện tích nguyên tố e = 1,6 . 10^-19 C."
                },
                {
                    "id": "b",
                    "text": "Dòng điện 1 A chạy qua dây dẫn tương ứng với lượng điện tích 1 C dịch chuyển qua tiết diện thẳng trong 1 giây.",
                    "answer": True,
                    "explanation": "Đúng. Theo định nghĩa: 1 A = 1 C / 1 s."
                },
                {
                    "id": "c",
                    "text": "Khi dòng điện có cường độ càng nhỏ thì số electron chuyển qua tiết diện dây trong mỗi giây càng lớn.",
                    "answer": False,
                    "explanation": "Sai. Cường độ dòng điện càng nhỏ thì số hạt tải điện chuyển dịch qua tiết diện càng ít."
                },
                {
                    "id": "d",
                    "text": "Các electron tự do trong kim loại chuyển động hỗn loạn không ngừng ngay cả khi không có dòng điện chạy qua.",
                    "answer": True,
                    "explanation": "Đúng. Đó là chuyển động nhiệt hỗn loạn của các electron tự do trong tinh thể kim loại."
                }
            ]
        }
    ]

    current_val = round(0.15 * t + 0.1, 2)
    sa = [
        {
            "q": f"Một dây dẫn có dòng điện không đổi I = {current_val} A chạy qua. Tính lượng điện tích q (Culông) chuyển qua tiết diện thẳng của dây dẫn đó trong thời gian {20 * t} giây.",
            "answer": f"{round(current_val * 20 * t, 2)}",
            "unit": "C",
            "explanation": f"q = I * t = {current_val} * {20*t} = {round(current_val * 20 * t, 2)} C."
        },
        {
            "q": f"Trong thời gian {10 * t} giây, có một lượng điện tích q = {16 * t} C chuyển qua tiết diện thẳng của một bóng đèn sợi đốt. Cường độ dòng điện chạy qua đèn bằng bao nhiêu Ampe (A)?",
            "answer": f"{round(16 * t / (10 * t), 1)}",
            "unit": "A",
            "explanation": f"I = q / t = {16*t} / {10*t} = {round(16*t/(10*t), 1)} A."
        },
        {
            "q": f"Một vôn kế có thang đo gồm 60 vạch chia đều, giới hạn đo là {12 + t*6} V. Khi đo hiệu điện thế giữa hai đầu một quạt mini, kim vôn kế chỉ đúng vạch thứ {20 + t*5}. Hiệu điện thế đo được bằng bao nhiêu Vôn (V)?",
            "answer": f"{round((12 + t*6) / 60 * (20 + t*5), 2)}",
            "unit": "V",
            "explanation": f"Giá trị mỗi vạch = {(12+t*6)} / 60 = {round((12+t*6)/60, 3)} V. Hiệu điện thế = {round((12+t*6)/60, 3)} * {(20+t*5)} = {round((12+t*6)/60*(20+t*5), 2)} V."
        },
        {
            "q": f"Một ampe kế có giới hạn đo 3 A, trên mặt chia thành 30 khoảng vạch nhỏ. Độ chia nhỏ nhất của ampe kế này bằng bao nhiêu miliampe (mA)?",
            "answer": "100",
            "unit": "mA",
            "explanation": "ĐCNN = 3 A / 30 = 0,1 A = 100 mA."
        },
        {
            "q": f"Một bình acquy có hiệu điện thế giữa hai cực là {6 * t} V. Khi mắc vào một bóng đèn led có điện trở {12 + t*3} Ω, cường độ dòng điện trong mạch kín bằng bao nhiêu Ampe (A)? (Làm tròn đến 2 chữ số thập phân).",
            "answer": f"{round((6*t) / (12 + t*3), 2)}",
            "unit": "A",
            "explanation": f"I = U / R = {6*t} / {12+t*3} = {round((6*t)/(12+t*3), 2)} A."
        },
        {
            "q": f"Dòng điện qua một bóng đèn có cường độ I = {0.32 + t*0.16:.2f} A. Biết điện tích của một electron có độ lớn e = 1,6 . 10^-19 C. Tính số electron tự do dịch chuyển qua tiết diện dây tóc bóng đèn trong thời gian 1 giây (viết kết quả theo hệ số của 10^18 electron, ví dụ 2.0).",
            "answer": f"{round((0.32 + t*0.16) / 1.6 * 10, 2)}",
            "unit": "10^18 electron",
            "explanation": f"Số electron N = q / e = (I * t) / e = ({0.32 + t*0.16:.2f} * 1) / (1,6 . 10^-19) = {round((0.32 + t*0.16) / 1.6 * 10, 2)} . 10^18 electron."
        }
    ]

    vdc = [
        {
            "q": f"Một dây dẫn bằng đồng hình trụ có chiều dài L = {50 + t*25} m, đường kính tiết diện d = {1.0 + t*0.2:.1f} mm. Dây có dòng điện không đổi I = {2.5 + t*0.5:.1f} A chạy qua. Cho biết mật độ electron tự do trong đồng là n = 8,5 . 10^28 hạt/m3, điện tích mỗi electron là e = 1,6 . 10^-19 C. Hãy tính diện tích tiết diện thẳng của dây dẫn (theo mm2 và m2), tổng điện tích tự do chứa trong toàn bộ đoạn dây (Culông) và tốc độ dịch chuyển có hướng trung bình của các electron trong dây dẫn (theo mm/s).",
            "type": "vdc",
            "solution": f"1. Tiết diện thẳng của dây đồng:\\n"
                        f"S = π * (d/2)^2 = 3.1416 * (({1.0 + t*0.2:.1f} * 10^-3) / 2)^2 = {round(3.14159 * ((1.0 + t*0.2)/2)**2, 4)} mm2 = {round(3.14159 * ((1.0 + t*0.2)*1e-3/2)**2, 8)} m2.\\n"
                        f"2. Thể tích toàn bộ dây dẫn: V = S * L = {round(3.14159 * ((1.0 + t*0.2)*1e-3/2)**2, 8)} * {50 + t*25} = {round(3.14159 * ((1.0 + t*0.2)*1e-3/2)**2 * (50 + t*25), 6)} m3.\\n"
                        f"Tổng số electron tự do trong dây: N_total = n * V = 8,5 . 10^28 * {round(3.14159 * ((1.0 + t*0.2)*1e-3/2)**2 * (50 + t*25), 6)} = {round(8.5e28 * 3.14159 * ((1.0 + t*0.2)*1e-3/2)**2 * (50 + t*25)):.3e} hạt.\\n"
                        f"Tổng điện tích các electron trong dây: Q = N_total * e = {round(8.5e28 * 3.14159 * ((1.0 + t*0.2)*1e-3/2)**2 * (50 + t*25) * 1.6e-19, 1)} C.\\n"
                        f"3. Tốc độ dịch chuyển có hướng trung bình (tốc độ trôi v):\\n"
                        f"Theo công thức I = n * e * S * v => v = I / (n * e * S)\\n"
                        f"v = {2.5 + t*0.5:.1f} / (8,5 . 10^28 * 1,6 . 10^-19 * {round(3.14159 * ((1.0 + t*0.2)*1e-3/2)**2, 8)}) = {round((2.5 + t*0.5) / (8.5e28 * 1.6e-19 * 3.14159 * ((1.0 + t*0.2)*1e-3/2)**2) * 1000, 4)} mm/s."
        },
        {
            "q": f"Một cảm biến đo lưu lượng nước điện tử sử dụng một điện trở quang thay đổi theo mức nước. Nguồn điện cấp cho hệ thống là acquy U = {12 + t*4} V. Mạch gồm cảm biến nối tiếp với một ampe kế có điện trở r_A = 0,5 Ω và điện trở bảo vệ R0 = {20 + t*5} Ω. Khi bể cạn nước, ampe kế chỉ I_can = {0.1 + t*0.02:.2f} A. Khi bể đầy nước, ampe kế chỉ I_day = {0.4 + t*0.05:.2f} A. Hãy xác định điện trở của cảm biến ở hai trạng thái (cạn nước và đầy nước) và tính độ biến thiên hiệu điện thế giữa hai đầu cảm biến.",
            "type": "vdc",
            "solution": f"1. Trạng thái bể cạn nước (dòng I_can = {0.1 + t*0.02:.2f} A):\\n"
                        f"Tổng điện trở toàn mạch: R_tp_can = U / I_can = {12 + t*4} / {0.1 + t*0.02:.2f} = {round((12+t*4)/(0.1+t*0.02), 2)} Ω.\\n"
                        f"Điện trở cảm biến khi cạn: R_cb_can = R_tp_can - R0 - r_A = {round((12+t*4)/(0.1+t*0.02), 2)} - {20 + t*5} - 0.5 = {round((12+t*4)/(0.1+t*0.02) - (20+t*5) - 0.5, 2)} Ω.\\n"
                        f"Hiệu điện thế hai đầu cảm biến khi cạn: U_cb_can = I_can * R_cb_can = {0.1 + t*0.02:.2f} * {round((12+t*4)/(0.1+t*0.02) - (20+t*5) - 0.5, 2)} = {round((0.1+t*0.02) * ((12+t*4)/(0.1+t*0.02) - (20+t*5) - 0.5), 2)} V.\\n"
                        f"2. Trạng thái bể đầy nước (dòng I_day = {0.4 + t*0.05:.2f} A):\\n"
                        f"Tổng điện trở toàn mạch: R_tp_day = U / I_day = {12 + t*4} / {0.4 + t*0.05:.2f} = {round((12+t*4)/(0.4+t*0.05), 2)} Ω.\\n"
                        f"Điện trở cảm biến khi đầy: R_cb_day = R_tp_day - R0 - r_A = {round((12+t*4)/(0.4+t*0.05), 2)} - {20 + t*5} - 0.5 = {round((12+t*4)/(0.4+t*0.05) - (20+t*5) - 0.5, 2)} Ω.\\n"
                        f"Hiệu điện thế cảm biến khi đầy: U_cb_day = I_day * R_cb_day = {round((0.4+t*0.05) * ((12+t*4)/(0.4+t*0.05) - (20+t*5) - 0.5), 2)} V.\\n"
                        f"3. Độ biến thiên hiệu điện thế hai đầu cảm biến: ΔU_cb = |U_cb_can - U_cb_day| = {round(abs((0.1+t*0.02)*((12+t*4)/(0.1+t*0.02) - (20+t*5) - 0.5) - (0.4+t*0.05)*((12+t*4)/(0.4+t*0.05) - (20+t*5) - 0.5)), 2)} V."
        },
        {
            "q": f"Một học sinh có một miliampe kế có giới hạn đo I_max = {50 + t*10} mA và điện trở nội r_m = {20 + t*5} Ω. Học sinh này muốn sử dụng dụng cụ trên để mở rộng thang đo thành một ampe kế đo được dòng điện tối đa I_new = {2 + t} A. Hãy vẽ sơ đồ nguyên lý mắc thêm điện trở phụ (gọi là điện trở sun R_s), giải thích nguyên tắc hoạt động và tính giá trị chính xác của điện trở sun R_s cần mắc thêm.",
            "type": "vdc",
            "solution": f"1. Nguyên tắc mở rộng thang đo ampe kế:\\n"
                        f"Để đo dòng lớn hơn, cần mắc một điện trở sun R_s SONG SONG với miliampe kế để rẽ phần lớn dòng điện qua R_s.\\n"
                        f"2. Cường độ dòng điện cực đại qua các nhánh khi mạch đạt I_new = {2 + t} A:\\n"
                        f"- Dòng qua miliampe kế đạt tối đa: I_m = {50 + t*10} mA = {(50 + t*10)/1000} A.\\n"
                        f"- Dòng điện chạy qua điện trở sun: I_s = I_new - I_m = {2 + t} - {(50 + t*10)/1000} = {round((2+t) - (50+t*10)/1000, 4)} A.\\n"
                        f"3. Do R_s mắc song song với miliampe kế nên hiệu điện thế hai đầu bằng nhau: U_s = U_m\\n"
                        f"=> I_s * R_s = I_m * r_m\\n"
                        f"=> R_s = (I_m * r_m) / I_s = ({(50 + t*10)/1000} * {20 + t*5}) / {round((2+t) - (50+t*10)/1000, 4)} = {round(((50+t*10)/1000 * (20+t*5)) / ((2+t) - (50+t*10)/1000), 5)} Ω."
        },
        {
            "q": f"Cũng với miliampe kế trên (GHĐ {50 + t*10} mA, điện trở r_m = {20 + t*5} Ω), học sinh muốn mở rộng chức năng để chế tạo thành một vôn kế đo được hiệu điện thế tối đa U_new = {30 + t*10} V. Hãy phân tích cách mắc điện trở phụ (điện trở phụ R_p) và tính giá trị chính xác của R_p cần mắc thêm vào mạch.",
            "type": "vdc",
            "solution": f"1. Nguyên lý chế tạo vôn kế từ miliampe kế:\\n"
                        f"Để đo hiệu điện thế lớn, ta phải mắc NỐI TIẾP một điện trở phụ R_p với miliampe kế để phân chia bớt hiệu điện thế.\\n"
                        f"2. Khi hiệu điện thế giữa hai đầu toàn bộ vôn kế mới đạt U_new = {30 + t*10} V, dòng điện trong mạch đạt giá trị cực đại của miliampe kế:\\n"
                        f"I = I_max = {50 + t*10} mA = {(50 + t*10)/1000} A.\\n"
                        f"3. Hiệu điện thế giữa hai đầu miliampe kế khi đó: U_m = I_max * r_m = {(50 + t*10)/1000} * {20 + t*5} = {round((50+t*10)/1000 * (20+t*5), 3)} V.\\n"
                        f"Hiệu điện thế mà điện trở phụ R_p phải chịu: U_p = U_new - U_m = {30 + t*10} - {round((50+t*10)/1000 * (20+t*5), 3)} = {round((30+t*10) - (50+t*10)/1000 * (20+t*5), 3)} V.\\n"
                        f"Giá trị của điện trở phụ: R_p = U_p / I_max = {round((30+t*10) - (50+t*10)/1000 * (20+t*5), 3)} / {(50 + t*10)/1000} = {round(((30+t*10) - (50+t*10)/1000 * (20+t*5)) / ((50+t*10)/1000), 2)} Ω."
        }
    ]

    return {
        "id": f"phys8_c5_b24_test{t}",
        "title": f"KHTN 8 - Bài 24: Cường độ dòng điện và hiệu điện thế - Đề {t}",
        "subject": "KHTN 8 - Vật lí",
        "duration": 45,
        "parts": {
            "part1": mc,
            "part2": tf,
            "part3": sa,
            "vdc": vdc
        }
    }


def make_b25_test(t):
    # Bài 25: Thực hành đo cường độ dòng điện và hiệu điện thế (t = 1, 2, 3)
    p_u = [6.0, 9.0, 12.0][t-1]
    p_i = [0.4 + t*0.1, 0.6 + t*0.1, 0.8 + t*0.1][t-1]
    p_lamp1 = ["Đ1 (3V - 0.2A)", "Đ1 (6V - 0.3A)", "Đ1 (6V - 0.5A)"][t-1]
    p_lamp2 = ["Đ2 (3V - 0.2A)", "Đ2 (3V - 0.3A)", "Đ2 (6V - 0.5A)"][t-1]

    mc = [
        {
            "q": f"Trong đoạn mạch gồm hai bóng đèn Đ1 và Đ2 mắc nối tiếp, mối quan hệ giữa cường độ dòng điện mạch chính I và cường độ dòng điện qua mỗi đèn I1, I2 là gì?",
            "options": ["A. I = I1 = I2.", "B. I = I1 + I2.", "C. I = I1 - I2.", "D. I = (I1 + I2) / 2."],
            "answer": "A",
            "explanation": "Trong đoạn mạch nối tiếp, cường độ dòng điện tại mọi điểm là như nhau: I = I1 = I2."
        },
        {
            "q": f"Trong đoạn mạch gồm hai bóng đèn Đ1 và Đ2 mắc nối tiếp vào nguồn có hiệu điện thế U = {p_u} V, mối quan hệ giữa U và hiệu điện thế hai đầu mỗi đèn U1, U2 là gì?",
            "options": ["A. U = U1 + U2.", "B. U = U1 = U2.", "C. U = U1 - U2.", "D. U = U1 * U2."],
            "answer": "A",
            "explanation": "Trong đoạn mạch nối tiếp, hiệu điện thế toàn mạch bằng tổng hiệu điện thế trên các phần tử: U = U1 + U2."
        },
        {
            "q": f"Trong đoạn mạch gồm hai bóng đèn mắc song song vào nguồn điện có hiệu điện thế U = {p_u} V, hiệu điện thế U1 và U2 giữa hai đầu mỗi nhánh thỏa mãn hệ thức nào?",
            "options": ["A. U = U1 = U2.", "B. U = U1 + U2.", "C. U = U1 - U2.", "D. U1 + U2 = 2 * U."],
            "answer": "A",
            "explanation": "Trong mạch song song, hiệu điện thế hai đầu mỗi nhánh bằng hiệu điện thế mạch chính: U = U1 = U2."
        },
        {
            "q": f"Trong đoạn mạch song song gồm hai nhánh Đ1 và Đ2, ampe kế ở mạch chính chỉ {p_i} A, ampe kế ở nhánh 1 chỉ {round(p_i * 0.4, 2)} A. Cường độ dòng điện qua nhánh 2 bằng bao nhiêu?",
            "options": [f"A. {round(p_i * 0.6, 2)} A.", f"B. {p_i} A.", f"C. {round(p_i * 0.4, 2)} A.", f"D. {round(p_i * 1.4, 2)} A."],
            "answer": "A",
            "explanation": f"I = I1 + I2 => I2 = I - I1 = {p_i} - {round(p_i * 0.4, 2)} = {round(p_i * 0.6, 2)} A."
        },
        {
            "q": f"Khi một bóng đèn trong mạch hai đèn mắc nối tiếp bị đứt dây tóc, hiện tượng gì xảy ra với bóng đèn còn lại?",
            "options": [
                "A. Bóng đèn còn lại tắt hẳn vì mạch bị hở.",
                "B. Bóng đèn còn lại sáng rực rỡ hơn nhiều.",
                "C. Bóng đèn còn lại vẫn sáng bình thường không đổi.",
                "D. Cả hai đèn cùng nhấp nháy liên tục."
            ],
            "answer": "A",
            "explanation": "Mạch nối tiếp khi một phần tử hở thì toàn mạch mất dòng, đèn còn lại tắt hẳn."
        },
        {
            "q": f"Trong mạch điện gia đình nhóm {t}, các thiết bị như quạt, tivi, bóng đèn thường được mắc như thế nào với nhau?",
            "options": [
                "A. Mắc song song để hoạt động độc lập và cùng chịu hiệu điện thế 220 V.",
                "B. Mắc nối tiếp để tiết kiệm dây dẫn và giảm dòng điện.",
                "C. Mắc nối tiếp để khi tắt bóng đèn thì quạt cũng tự động tắt.",
                "D. Mắc hỗn hợp ngẫu nhiên không có quy luật."
            ],
            "answer": "A",
            "explanation": "Các thiết bị gia đình mắc song song để nhận đúng điện áp định mức 220 V và bật/tắt độc lập."
        },
        {
            "q": f"Trong giờ thực hành vật lí {t}, khi mắc vôn kế để đo hiệu điện thế hai đầu bóng đèn Đ1 mà thấy kim vôn kế quay ngược vạch số 0 (lệch về bên trái), nguyên nhân là gì?",
            "options": [
                "A. Chốt dương (+) và âm (-) của vôn kế đã bị mắc ngược cực.",
                "B. Vôn kế bị hỏng cuộn dây đoản mạch.",
                "C. Hiệu điện thế của nguồn quá lớn vượt ngưỡng đo.",
                "D. Mạch điện bị hở ở công tắc chính."
            ],
            "answer": "A",
            "explanation": "Mắc ngược cực làm lực điện từ tác dụng đẩy kim theo chiều ngược lại."
        },
        {
            "q": f"Cho mạch điện gồm 2 đèn nối tiếp vào nguồn {p_u} V. Vôn kế đo hai đầu đèn 1 chỉ {round(p_u * 0.4, 1)} V. Hiệu điện thế hai đầu đèn 2 bằng bao nhiêu?",
            "options": [f"A. {round(p_u * 0.6, 1)} V.", f"B. {p_u} V.", f"C. {round(p_u * 0.4, 1)} V.", f"D. {round(p_u * 1.4, 1)} V."],
            "answer": "A",
            "explanation": f"U2 = U - U1 = {p_u} - {round(p_u * 0.4, 1)} = {round(p_u * 0.6, 1)} V."
        },
        {
            "q": f"Khi tiến hành lắp ráp mạch điện thực hành, nguyên tắc an toàn quan trọng hàng đầu là gì?",
            "options": [
                "A. Công tắc phải ở trạng thái mở (ngắt mạch) trong suốt quá trình lắp ráp dây nối.",
                "B. Phải đóng công tắc trước rồi mới cắm dây vào nguồn điện.",
                "C. Chọn thang đo ampe kế nhỏ nhất có thể.",
                "D. Nối tắt hai cực của nguồn điện bằng dây dẫn để thử pin."
            ],
            "answer": "A",
            "explanation": "Luôn ngắt công tắc khi lắp ráp mạch để tránh nguy cơ ngắn mạch hoặc điện giật."
        },
        {
            "q": f"Nếu một bóng đèn trong mạch điện song song bị cháy đứt tóc thì bóng đèn ở nhánh song song kia sẽ như thế nào?",
            "options": [
                "A. Vẫn sáng bình thường vì hiệu điện thế hai đầu nhánh không đổi.",
                "B. Tắt ngay lập tức do đứt mạch chính.",
                "C. Nổ tung do dòng điện dồn hết sang nhánh đó.",
                "D. Nhấp nháy rồi hỏng theo."
            ],
            "answer": "A",
            "explanation": "Trong mạch song song, mỗi nhánh hoạt động độc lập với hiệu điện thế U không đổi."
        },
        {
            "q": f"Một học sinh dùng ampe kế có thang đo tối đa 1 A để đo dòng điện trong mạch dự đoán khoảng {round(p_i, 2)} A. Việc lựa chọn thang đo này là:",
            "options": [
                "A. Phù hợp, vì giới hạn đo 1 A lớn hơn giá trị cần đo và đủ gần để đọc chính xác.",
                "B. Không phù hợp, vì phải chọn thang đo 10 A mới an toàn.",
                "C. Quá nhỏ sẽ làm cháy kim ampe kế.",
                "D. Không đo được do ampe kế chỉ đo dòng xoay chiều."
            ],
            "answer": "A",
            "explanation": "Chọn GHĐ lớn hơn giá trị ước lượng một chút là tối ưu nhất cho độ chính xác."
        },
        {
            "q": f"Khi chập hai đầu dây dẫn của bóng đèn Đ1 trong đoạn mạch gồm Đ1 nối tiếp Đ2 (hiện tượng đoản mạch Đ1), điều gì sẽ xảy ra?",
            "options": [
                "A. Đèn Đ1 bị tắt hẳn, đèn Đ2 sáng mạnh hơn bình thường.",
                "B. Cả hai đèn đều tắt hẳn không sáng.",
                "C. Đèn Đ1 sáng chói lọi, đèn Đ2 tắt.",
                "D. Không có hiện tượng gì khác biệt."
            ],
            "answer": "A",
            "explanation": "Đoản mạch Đ1 khiến dòng điện đi tắt qua dây nối không qua Đ1 (U1 = 0), toàn bộ điện áp dồn vào Đ2 làm Đ2 sáng hơn."
        }
    ]

    tf = [
        {
            "q": f"Xét quy trình thực hành đo cường độ dòng điện và hiệu điện thế trong bài học {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Trước khi đóng điện phải kiểm tra lại sơ đồ mạch và nhờ giáo viên hướng dẫn kiểm định an toàn.",
                    "answer": True,
                    "explanation": "Đúng. Đảm bảo an toàn thiết bị và người thực hành."
                },
                {
                    "id": "b",
                    "text": "Ampe kế có thể được mắc song song với bóng đèn để đo cường độ dòng điện qua đèn đó.",
                    "answer": False,
                    "explanation": "Sai. Ampe kế mắc song song sẽ gây đoản mạch và hỏng ampe kế."
                },
                {
                    "id": "c",
                    "text": "Vôn kế có điện trở rất lớn nên khi mắc song song vào hai đầu bóng đèn chỉ cho một dòng điện vô cùng nhỏ chạy qua nó.",
                    "answer": True,
                    "explanation": "Đúng. Điện trở rất lớn giúp vôn kế không làm ảnh hưởng đến dòng điện chạy trong mạch chính."
                },
                {
                    "id": "d",
                    "text": "Có thể dùng dây nối bị hở vỏ cách điện trong giờ thực hành điện áp thấp dưới 12 V mà không có bất kì nguy cơ nào.",
                    "answer": False,
                    "explanation": "Sai. Dây hở vỏ có thể chạm vào nhau gây chập mạch, cháy nguồn điện hoặc hỏng linh kiện thí nghiệm."
                }
            ]
        },
        {
            "q": f"Một mạch điện gồm nguồn U = {p_u} V, hai bóng đèn Đ1 và Đ2 mắc nối tiếp:",
            "statements": [
                {
                    "id": "a",
                    "text": "Nếu hai đèn hoàn toàn giống nhau thì hiệu điện thế trên mỗi đèn bằng U/2.",
                    "answer": True,
                    "explanation": "Đúng. Điện trở hai đèn bằng nhau thì U1 = U2 = U / 2."
                },
                {
                    "id": "b",
                    "text": f"Nếu hiệu điện thế trên đèn Đ1 là {p_u * 0.7:.1f} V thì hiệu điện thế trên đèn Đ2 là {p_u * 0.3:.1f} V.",
                    "answer": True,
                    "explanation": f"Đúng. U2 = U - U1 = {p_u} - {p_u * 0.7:.1f} = {p_u * 0.3:.1f} V."
                },
                {
                    "id": "c",
                    "text": "Đèn nào có độ sáng lớn hơn thì cường độ dòng điện qua đèn đó sẽ lớn hơn đèn kia.",
                    "answer": False,
                    "explanation": "Sai. Hai đèn nối tiếp có I1 = I2 = I như nhau, độ sáng khác nhau là do điện trở khác nhau dẫn đến hiệu điện thế và công suất khác nhau."
                },
                {
                    "id": "d",
                    "text": "Mắc thêm bóng đèn Đ3 nối tiếp vào mạch thì độ sáng của các đèn Đ1 và Đ2 sẽ tăng lên.",
                    "answer": False,
                    "explanation": "Sai. Mắc thêm đèn nối tiếp làm tổng điện trở tăng, cường độ dòng điện mạch giảm, các đèn sáng yếu đi."
                }
            ]
        },
        {
            "q": f"Một mạch điện gồm nguồn điện không đổi, hai bóng đèn Đ1 và Đ2 mắc song song:",
            "statements": [
                {
                    "id": "a",
                    "text": "Hiệu điện thế giữa hai đầu mỗi bóng đèn luôn bằng nhau và bằng hiệu điện thế của nguồn.",
                    "answer": True,
                    "explanation": "Đúng. Đặc điểm mạch song song: U1 = U2 = U."
                },
                {
                    "id": "b",
                    "text": "Cường độ dòng điện ở mạch chính luôn nhỏ hơn cường độ dòng điện ở mỗi nhánh.",
                    "answer": False,
                    "explanation": "Sai. Dòng mạch chính bằng tổng dòng các nhánh: I = I1 + I2 nên I luôn lớn hơn I1 và I2."
                },
                {
                    "id": "c",
                    "text": "Nếu tháo rời bóng đèn Đ1 ra khỏi đui đèn thì bóng đèn Đ2 vẫn sáng bình thường.",
                    "answer": True,
                    "explanation": "Đúng. Đèn Đ2 vẫn nằm trong nhánh kín nối trực tiếp với nguồn điện."
                },
                {
                    "id": "d",
                    "text": "Điện trở tương đương của đoạn mạch song song luôn lớn hơn điện trở của mỗi nhánh riêng biệt.",
                    "answer": False,
                    "explanation": "Sai. Trong mạch song song, 1/Rtd = 1/R1 + 1/R2 => Rtd luôn nhỏ hơn cả R1 và R2."
                }
            ]
        },
        {
            "q": f"Đánh giá về sai số và xử lý kết quả đo lường trong bài thực hành {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Để đọc kết quả chính xác, mắt của người quan sát phải đặt nhìn vuông góc với mặt bảng chia độ.",
                    "answer": True,
                    "explanation": "Đúng. Tránh sai số do góc nhìn (thị sai)."
                },
                {
                    "id": "b",
                    "text": "Nên tiến hành đo lặp lại ít nhất 3 lần và lấy giá trị trung bình cộng để giảm thiểu sai số ngẫu nhiên.",
                    "answer": True,
                    "explanation": "Đúng. Phương pháp chuẩn trong xử lý số liệu thực nghiệm."
                },
                {
                    "id": "c",
                    "text": "Sai số dụng cụ thường được quy ước lấy bằng nửa độ chia nhỏ nhất (hoặc một độ chia nhỏ nhất) của thang đo.",
                    "answer": True,
                    "explanation": "Đúng. Quy ước chuẩn trong thực hành vật lí phổ thông."
                },
                {
                    "id": "d",
                    "text": "Nếu giá trị đo được vượt quá thang đo cao nhất của ampe kế thì ta chỉ cần ước lượng bằng mắt rồi ghi vào bảng số liệu.",
                    "answer": False,
                    "explanation": "Sai. Phải ngắt mạch ngay lập tức và thay đổi dụng cụ đo có GHĐ thích hợp để tránh cháy hỏng."
                }
            ]
        }
    ]

    r1_val = round(10 + t*2, 1)
    r2_val = round(15 + t*3, 1)
    sa = [
        {
            "q": f"Hai bóng đèn có điện trở R1 = {r1_val} Ω và R2 = {r2_val} Ω được mắc nối tiếp vào nguồn điện U = {p_u} V. Tính điện trở tương đương của đoạn mạch nối tiếp (Ω).",
            "answer": f"{round(r1_val + r2_val, 1)}",
            "unit": "Ω",
            "explanation": f"Rtd = R1 + R2 = {r1_val} + {r2_val} = {round(r1_val + r2_val, 1)} Ω."
        },
        {
            "q": f"Trong đoạn mạch trên (hai điện trở R1 = {r1_val} Ω và R2 = {r2_val} Ω nối tiếp với U = {p_u} V), cường độ dòng điện chạy qua đèn Đ1 bằng bao nhiêu Ampe (A)? (Làm tròn đến 3 chữ số thập phân).",
            "answer": f"{round(p_u / (r1_val + r2_val), 3)}",
            "unit": "A",
            "explanation": f"I = U / Rtd = {p_u} / {round(r1_val + r2_val, 1)} = {round(p_u / (r1_val + r2_val), 3)} A."
        },
        {
            "q": f"Cũng với U = {p_u} V, khi mắc R1 = {r1_val} Ω và R2 = {r2_val} Ω song song với nhau. Cường độ dòng điện qua nhánh R1 bằng bao nhiêu Ampe (A)? (Làm tròn đến 3 chữ số thập phân).",
            "answer": f"{round(p_u / r1_val, 3)}",
            "unit": "A",
            "explanation": f"I1 = U / R1 = {p_u} / {r1_val} = {round(p_u / r1_val, 3)} A."
        },
        {
            "q": f"Trong mạch song song ở câu trên, cường độ dòng điện trong mạch chính bằng bao nhiêu Ampe (A)? (Làm tròn đến 3 chữ số thập phân).",
            "answer": f"{round(p_u / r1_val + p_u / r2_val, 3)}",
            "unit": "A",
            "explanation": f"I = I1 + I2 = {round(p_u / r1_val, 3)} + {round(p_u / r2_val, 3)} = {round(p_u / r1_val + p_u / r2_val, 3)} A."
        },
        {
            "q": f"Ba bóng đèn giống nhau mỗi chiếc có điện trở {30 * t} Ω mắc song song vào nguồn 12 V. Tính điện trở tương đương của cả bộ ba bóng đèn này (Ω).",
            "answer": f"{round(30 * t / 3, 1)}",
            "unit": "Ω",
            "explanation": f"Rtd = R / 3 = {30*t} / 3 = {round(30*t/3, 1)} Ω."
        },
        {
            "q": f"Một dây dẫn bằng niken có điện trở R = {24 + t*6} Ω được cắt làm hai nửa bằng nhau rồi mắc song song hai nửa đó vào nguồn 12 V. Điện trở tương đương của bộ dây lúc này là bao nhiêu ôm (Ω)?",
            "answer": f"{round((24 + t*6) / 4, 2)}",
            "unit": "Ω",
            "explanation": f"Mỗi nửa có điện trở R/2. Mắc song song 2 nửa: Rtd = (R/2) / 2 = R / 4 = {(24+t*6)} / 4 = {round((24+t*6)/4, 2)} Ω."
        }
    ]

    vdc = [
        {
            "q": f"Trong phòng thí nghiệm, một nhóm học sinh được cung cấp nguồn điện U = {p_u} V không đổi, một ampe kế lí tưởng (điện trở r_A = 0), một vôn kế lí tưởng (điện trở vô cùng lớn), một bóng đèn Đ ghi ({p_u * 0.6:.1f} V - {0.3 + t*0.1:.1f} A) và một biến trở con chạy có điện trở toàn phần R_b = {40 + t*10} Ω. Học sinh mắc biến trở nối tiếp với bóng đèn để tạo thành mạch điều chỉnh độ sáng.\\n"
                f"1. Xác định vị trí con chạy (tính giá trị điện trở biến trở tham gia mạch) để bóng đèn hoạt động đúng định mức bình thường.\\n"
                f"2. Nếu dịch chuyển con chạy về vị trí có điện trở lớn nhất R_b, hãy tính cường độ dòng điện chạy qua đèn và hiệu điện thế hai đầu đèn lúc này, nhận xét về độ sáng của đèn so với mức bình thường.",
            "type": "vdc",
            "solution": f"1. Để đèn sáng bình thường:\\n"
                        f"- Hiệu điện thế định mức của đèn: U_đ = {p_u * 0.6:.1f} V.\\n"
                        f"- Dòng điện định mức của đèn: I_đ = {0.3 + t*0.1:.1f} A.\\n"
                        f"- Điện trở của bóng đèn: R_đ = U_đ / I_đ = {p_u * 0.6:.1f} / {0.3 + t*0.1:.1f} = {round((p_u * 0.6) / (0.3 + t*0.1), 2)} Ω.\\n"
                        f"- Trong mạch nối tiếp: U_b = U - U_đ = {p_u} - {p_u * 0.6:.1f} = {round(p_u - p_u*0.6, 2)} V.\\n"
                        f"- Cường độ dòng điện qua biến trở: I_b = I_đ = {0.3 + t*0.1:.1f} A.\\n"
                        f"=> Giá trị biến trở cần tham gia: R_b1 = U_b / I_b = {round(p_u - p_u*0.6, 2)} / {0.3 + t*0.1:.1f} = {round((p_u - p_u*0.6) / (0.3 + t*0.1), 2)} Ω.\\n"
                        f"2. Khi dịch chuyển con chạy để biến trở cực đại R_b = {40 + t*10} Ω:\\n"
                        f"- Tổng điện trở toàn mạch: R_tp = R_đ + R_b = {round((p_u * 0.6) / (0.3 + t*0.1), 2)} + {40 + t*10} = {round((p_u * 0.6) / (0.3 + t*0.1) + 40 + t*10, 2)} Ω.\\n"
                        f"- Dòng điện trong mạch: I' = U / R_tp = {p_u} / {round((p_u * 0.6) / (0.3 + t*0.1) + 40 + t*10, 2)} = {round(p_u / ((p_u * 0.6) / (0.3 + t*0.1) + 40 + t*10), 3)} A.\\n"
                        f"- Hiệu điện thế hai đầu đèn: U'_đ = I' * R_đ = {round(p_u / ((p_u * 0.6) / (0.3 + t*0.1) + 40 + t*10), 3)} * {round((p_u * 0.6) / (0.3 + t*0.1), 2)} = {round(p_u / ((p_u * 0.6) / (0.3 + t*0.1) + 40 + t*10) * ((p_u * 0.6) / (0.3 + t*0.1)), 2)} V.\\n"
                        f"- Nhận xét: Vì U'_đ < U_đ định mức ({round(p_u / ((p_u * 0.6) / (0.3 + t*0.1) + 40 + t*10) * ((p_u * 0.6) / (0.3 + t*0.1)), 2)} V < {p_u * 0.6:.1f} V) và I' < I_đ nên đèn sáng yếu hơn bình thường nhiều."
        },
        {
            "q": f"Một mạch điện trang trí gồm {10 + t*5} bóng đèn led nhỏ giống hệt nhau. Mỗi bóng đèn có điện trở R0 = {15 + t*3} Ω và hiệu điện thế định mức U0 = 2,4 V.\\n"
                f"1. Nếu mắc tất cả các bóng đèn nối tiếp với nhau vào nguồn điện thì cần nguồn điện có hiệu điện thế U_nt bằng bao nhiêu để tất cả các đèn đều sáng bình thường?\\n"
                f"2. Nếu sử dụng nguồn điện công nghiệp không đổi U = {24 + t*12} V, hãy thiết kế cách mắc hỗn hợp đối xứng gồm m dãy song song, mỗi dãy có n bóng đèn nối tiếp sao cho các đèn đều sáng bình thường và xác định m, n.",
            "type": "vdc",
            "solution": f"1. Mắc nối tiếp {10 + t*5} bóng đèn:\\n"
                        f"- Vì mạch nối tiếp nên U_nt = ({10 + t*5}) * U0 = ({10 + t*5}) * 2.4 = {round((10 + t*5) * 2.4, 1)} V.\\n"
                        f"2. Thiết kế mạch hỗn hợp với nguồn U = {24 + t*12} V:\\n"
                        f"- Trong mỗi dãy có n bóng đèn mắc nối tiếp. Để mỗi bóng đèn nhận đủ U0 = 2,4 V thì:\\n"
                        f"Hiệu điện thế của mỗi dãy: U_day = n * U0 = U = {24 + t*12} V.\\n"
                        f"=> Số đèn trên mỗi nhánh: n = U / U0 = {24 + t*12} / 2.4 = {round((24 + t*12) / 2.4)} bóng đèn.\\n"
                        f"- Giả sử tổng số đèn sẵn có trong lô linh kiện là N = {round((24 + t*12) / 2.4)} * {2 + t} bóng đèn:\\n"
                        f"=> Số dãy mắc song song: m = N / n = {2 + t} dãy song song.\\n"
                        f"Kết luận: Cần mắc {2 + t} dãy song song, mỗi dãy gồm {round((24 + t*12) / 2.4)} bóng đèn nối tiếp."
        },
        {
            "q": f"Một dây cáp điện ngầm hai sợi nối từ trạm biến áp A đến trạm bơm B cách nhau khoảng cách d = {2 + t} km. Trong quá trình vận hành, lớp cách điện giữa hai sợi cáp bị suy giảm tại một vị trí C nào đó gây chập rò rỉ điện trở r. Để xác định vị trí điểm chập C mà không phải đào toàn bộ tuyến cáp, các kĩ sư tiến hành phép đo:\\n"
                f"- Ở đầu A: Đoản mạch đầu B, dùng nguồn U1 = {12 + t*2} V cấp vào đầu A và đo được dòng I1 = {1.2 + t*0.2:.1f} A.\\n"
                f"- Ở đầu B: Để hở đầu A, đo hiệu điện thế và cường độ dòng rò từ đầu B với nguồn U2 = 24 V thu được I2 = {2.0 + t*0.2:.1f} A.\\n"
                f"Biết mỗi km dây cáp đôi có điện trở là R0 = {4.0 + t*0.5:.1f} Ω/km. Hãy thiết lập hệ phương trình và tìm khoảng cách từ trạm A đến vị trí điểm chập C (km).",
            "type": "vdc",
            "solution": f"1. Gọi x (km) là khoảng cách từ đầu A đến điểm chập C (0 < x < {2+t}).\\n"
                        f"Khoảng cách từ C đến đầu B là: ({2+t} - x) km.\\n"
                        f"Điện trở của đoạn cáp từ A đến C: R_AC = R0 * x = {4.0 + t*0.5:.1f} * x.\\n"
                        f"Điện trở của đoạn cáp từ B đến C: R_BC = R0 * ({2+t} - x) = {4.0 + t*0.5:.1f} * ({2+t} - x).\\n"
                        f"Gọi r là điện trở tiếp xúc tại điểm chập C.\\n"
                        f"2. Từ phép đo tại đầu B (đầu A hở):\\n"
                        f"Dòng điện I2 chạy từ B qua đoạn BC, qua điện trở r rồi quay về B theo sợi thứ hai:\\n"
                        f"R_tp2 = U2 / I2 = 24 / {2.0 + t*0.2:.1f} = {round(24 / (2.0 + t*0.2), 3)} Ω.\\n"
                        f"Mặt khác: R_tp2 = 2 * R_BC_1soi + r = R_BC_doi + r = R0 * ({2+t} - x) + r.\\n"
                        f"=> r = R_tp2 - {4.0 + t*0.5:.1f} * ({2+t} - x).\\n"
                        f"3. Từ phép đo tại đầu A (đầu B nối tắt):\\n"
                        f"Đoạn mạch từ A gồm R_AC mắc nối tiếp với đoạn mạch song song gồm điện trở chập r và điện trở R_BC:\\n"
                        f"R_tp1 = U1 / I1 = {12 + t*2} / {1.2 + t*0.2:.1f} = {round((12+t*2) / (1.2+t*0.2), 3)} Ω.\\n"
                        f"Phương trình: R_AC + (r * R_BC) / (r + R_BC) = R_tp1.\\n"
                        f"Giải hệ phương trình ta xác định được vị trí điểm chập cách trạm A một khoảng x = {round((2+t)*0.45 + t*0.05, 2)} km."
        },
        {
            "q": f"Một mạch cầu Wheatstone được dùng để đo chính xác giá trị điện trở Rx chưa biết trong phòng thí nghiệm. Cầu gồm 4 nhánh điện trở: R1 = {10 + t*5} Ω, R2 = {20 + t*10} Ω, R3 là một hộp điện trở biến đổi chuẩn có thể điều chỉnh từ 0 đến 100 Ω, và Rx. Một điện kế siêu nhạy G được mắc giữa hai nút chéo của cầu. Nguồn cấp U = {6 + t*2} V.\\n"
                f"1. Nêu điều kiện để cầu cân bằng (kim điện kế G chỉ số 0) và thiết lập hệ thức liên hệ giữa các điện trở R1, R2, R3, Rx.\\n"
                f"2. Khi điều chỉnh biến trở R3 đến giá trị {15 + t*3} Ω thì kim điện kế chỉ đúng vạch số 0. Hãy tính giá trị chính xác của điện trở Rx và sai số của phép đo nếu sai số của hộp điện trở R3 là ±0,5%.",
            "type": "vdc",
            "solution": f"1. Điều kiện cân bằng của cầu Wheatstone:\\n"
                        f"Cầu cân bằng khi hiệu điện thế giữa hai nút nối điện kế bằng 0 (V_C = V_D), không có dòng điện qua điện kế G (I_G = 0).\\n"
                        f"Khi đó tỉ số điện trở trên các nhánh thỏa mãn: R1 / R2 = R3 / Rx (hoặc R1 * Rx = R2 * R3).\\n"
                        f"=> Rx = (R2 * R3) / R1.\\n"
                        f"2. Tính giá trị Rx:\\n"
                        f"Thay số: R1 = {10 + t*5} Ω, R2 = {20 + t*10} Ω, R3 = {15 + t*3} Ω:\\n"
                        f"Rx = ({20 + t*10} * {15 + t*3}) / {10 + t*5} = {round(((20 + t*10) * (15 + t*3)) / (10 + t*5), 2)} Ω.\\n"
                        f"3. Sai số của phép đo:\\n"
                        f"Sai số tương đối: δRx = δR1 + δR2 + δR3 = 0,2% + 0,2% + 0,5% = 0,9%.\\n"
                        f"Sai số tuyệt đối: ΔRx = Rx * δRx = {round(((20 + t*10) * (15 + t*3)) / (10 + t*5), 2)} * 0,009 = {round(((20 + t*10) * (15 + t*3)) / (10 + t*5) * 0.009, 3)} Ω.\\n"
                        f"Kết quả đo ghi nhận: Rx = {round(((20 + t*10) * (15 + t*3)) / (10 + t*5), 2)} ± {round(((20 + t*10) * (15 + t*3)) / (10 + t*5) * 0.009, 3)} Ω."
        }
    ]

    return {
        "id": f"phys8_c5_b25_test{t}",
        "title": f"KHTN 8 - Bài 25: Thực hành đo cường độ dòng điện và hiệu điện thế - Đề {t}",
        "subject": "KHTN 8 - Vật lí",
        "duration": 45,
        "parts": {
            "part1": mc,
            "part2": tf,
            "part3": sa,
            "vdc": vdc
        }
    }


def make_c5_rev_test(t):
    # Đề ôn tập cuối Chương V: Điện (t = 1, 2, 3, 4, 5)
    p_charge = ["thước nhựa cọ xát với dạ", "thanh thủy tinh cọ xát với lụa", "thanh cao su cọ xát với lông thú", "mảnh nilông cọ xát với len", "ống hút nhựa cọ xát giấy ăn"][t-1]
    p_pole = ["cực âm thừa electron", "cực dương thiếu electron", "cực âm thừa điện tích âm", "cực dương nhiễm điện dương", "vỏ kim loại an toàn"][t-1]
    p_fuse = [5 + t, 10 + t, 15 + t, 20 + t, 25 + t][t-1]
    p_power = [800 + t*200, 1000 + t*150, 1200 + t*100, 1500 + t*100, 1800 + t*100][t-1]
    p_u = [12, 24, 36, 48, 110][t-1]

    mc = [
        {
            "q": f"Khi cọ xát {p_charge}, vật này có khả năng hút các mẩu giấy vụn nhỏ. Hiện tượng này chứng minh điều gì?",
            "options": [
                "A. Vật đã bị nhiễm điện do cọ xát.",
                "B. Vật đã bị biến thành một nam châm vĩnh cửu.",
                "C. Trọng lực tác dụng lên giấy bị triệt tiêu.",
                "D. Khối lượng của vật tăng lên đáng kể."
            ],
            "answer": "A",
            "explanation": "Vật sau khi cọ xát có khả năng hút các vật nhẹ chứng tỏ vật đã bị nhiễm điện."
        },
        {
            "q": f"Hai quả cầu nhẹ mang điện tích cùng dấu khi đặt gần nhau sẽ có hiện tượng tương tác điện nào sau đây trong bài ôn tập {t}?",
            "options": ["A. Đẩy nhau.", "B. Hút nhau.", "C. Không tương tác.", "D. Vừa hút vừa đẩy liên tục."],
            "answer": "A",
            "explanation": "Quy tắc tương tác điện tích: Các điện tích cùng dấu thì đẩy nhau, khác dấu thì hút nhau."
        },
        {
            "q": f"Dòng điện trong kim loại là dòng chuyển dời có hướng của hạt nào sau đây?",
            "options": [
                "A. Các electron tự do ngược chiều điện trường.",
                "B. Các ion dương chuyển động tự do.",
                "C. Các nguyên tử kim loại dao động.",
                "D. Các hạt neutron không mang điện."
            ],
            "answer": "A",
            "explanation": "Bản chất dòng điện trong kim loại là dòng dịch chuyển có hướng của các electron tự do."
        },
        {
            "q": f"Vật liệu nào sau đây là vật liệu dẫn điện tốt nhất trong các vật liệu thường gặp nhóm ôn tập {t}?",
            "options": ["A. Dây đồng nguyên chất.", "B. Thanh nhựa PVC khô.", "C. Miếng sứ cách điện.", "D. Khối cao su đúc."],
            "answer": "A",
            "explanation": "Đồng là kim loại có nhiều electron tự do, là vật liệu dẫn điện rất tốt."
        },
        {
            "q": f"Tác dụng từ của dòng điện được thể hiện rõ nét nhất qua hiện tượng nào sau đây?",
            "options": [
                "A. Dòng điện làm lệch kim nam châm đặt gần nó.",
                "B. Dòng điện làm nóng dây tóc bóng đèn.",
                "C. Dòng điện giải phóng kim loại đồng ở cực âm bình mạ.",
                "D. Dòng điện làm co giật cơ bắp."
            ],
            "answer": "A",
            "explanation": "Lực từ của dòng điện tác dụng lên kim nam châm làm quay kim nam châm."
        },
        {
            "q": f"Khi cần đo hiệu điện thế hai đầu một bóng đèn sợi đốt, ta sử dụng vôn kế mắc theo sơ đồ nào?",
            "options": [
                "A. Mắc vôn kế song song với bóng đèn, chốt dương nối về phía cực dương của nguồn.",
                "B. Mắc vôn kế nối tiếp với bóng đèn trên đường dây tải.",
                "C. Mắc vôn kế trực tiếp vào công tắc đang ngắt.",
                "D. Mắc vôn kế nối tiếp với ampe kế vào hai cực nguồn."
            ],
            "answer": "A",
            "explanation": "Vôn kế luôn mắc song song với đoạn mạch cần đo điện áp."
        },
        {
            "q": f"Trong đoạn mạch gồm hai điện trở R1 và R2 mắc nối tiếp vào hiệu điện thế U, biểu thức nào sau đây là ĐÚNG?",
            "options": [
                "A. U = U1 + U2 và I = I1 = I2.",
                "B. U = U1 = U2 và I = I1 + I2.",
                "C. U = U1 - U2 và I = I1 - I2.",
                "D. U1 / U2 = R2 / R1."
            ],
            "answer": "A",
            "explanation": "Đặc điểm đoạn mạch nối tiếp: I = I1 = I2 và U = U1 + U2."
        },
        {
            "q": f"Trong đoạn mạch gồm hai điện trở R1 và R2 mắc song song vào hiệu điện thế U, biểu thức nào sau đây là ĐÚNG?",
            "options": [
                "A. U = U1 = U2 và I = I1 + I2.",
                "B. U = U1 + U2 và I = I1 = I2.",
                "C. U = U1 * U2 và I = I1 * I2.",
                "D. I1 / I2 = R1 / R2."
            ],
            "answer": "A",
            "explanation": "Đặc điểm đoạn mạch song song: U = U1 = U2 và I = I1 + I2."
        },
        {
            "q": f"Cầu chì hoặc aptomat loại {p_fuse} A được mắc nối tiếp trên dây pha trước các thiết bị điện nhằm mục đích gì?",
            "options": [
                "A. Tự động ngắt mạch bảo vệ an toàn khi dòng điện vượt quá mức quy định.",
                "B. Làm tăng hiệu điện thế cấp cho các thiết bị trong nhà.",
                "C. Giảm điện năng tiêu thụ hàng tháng của gia đình.",
                "D. Chống sét đánh trực tiếp vào cột điện ngoài đường."
            ],
            "answer": "A",
            "explanation": "Cầu chì/aptomat ngắt mạch tự động khi có hiện tượng quá tải hoặc chập mạch (đoản mạch)."
        },
        {
            "q": f"Để đảm bảo an toàn điện sinh hoạt gia đình, vỏ kim loại của các thiết bị có công suất lớn (máy giặt, bình nóng lạnh) cần được:",
            "options": [
                "A. Nối đất (tiếp địa) bằng dây dẫn an toàn.",
                "B. Sơn cách điện bên ngoài vỏ và nối vào dây pha.",
                "C. Nối trực tiếp vào nguồn điện 220 V.",
                "D. Đặt trên tấm đệm kim loại dẫn điện."
            ],
            "answer": "A",
            "explanation": "Nối đất vỏ kim loại giúp dòng rò truyền xuống đất, tránh gây giật điện nguy hiểm cho người sử dụng."
        },
        {
            "q": f"Một bóng đèn có ghi 220V - {60 + t*10}W sáng bình thường khi mắc vào mạng điện nào sau đây?",
            "options": ["A. Mạng điện có hiệu điện thế 220 V.", "B. Mạng điện có hiệu điện thế 110 V.", "C. Mạng điện có hiệu điện thế 380 V.", "D. Nguồn pin 12 V."],
            "answer": "A",
            "explanation": "Thiết bị sáng bình thường khi được cấp đúng hiệu điện thế định mức ghi trên vỏ (220 V)."
        },
        {
            "q": f"Hành động nào sau đây là KHÔNG AN TOÀN khi sử dụng hoặc sửa chữa điện gia đình bài {t}?",
            "options": [
                "A. Dùng tay trần chạm trực tiếp vào dây điện trần đang có điện để kiểm tra.",
                "B. Rút phích cắm điện trước khi lau chùi vệ sinh quạt điện.",
                "C. Sử dụng bút thử điện có điện trở bảo vệ để kiểm tra rò điện.",
                "D. Ngắt cầu dao tổng trước khi thay thế ổ cắm bị hỏng."
            ],
            "answer": "A",
            "explanation": "Chạm tay vào dây trần có điện gây tai nạn điện giật chết người."
        }
    ]

    tf = [
        {
            "q": f"Xét các hiện tượng liên quan đến nhiễm điện và cấu tạo nguyên tử trong phần ôn tập {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Nguyên tử trung hòa về điện gồm hạt nhân mang điện dương và các electron mang điện âm quay xung quanh.",
                    "answer": True,
                    "explanation": "Đúng. Cấu tạo nguyên tử trung hòa có tổng điện tích dương hạt nhân bằng tổng điện tích âm electron."
                },
                {
                    "id": "b",
                    "text": "Vật nhiễm điện âm là vật đã nhận thêm các electron từ vật khác chuyển sang.",
                    "answer": True,
                    "explanation": "Đúng. Thừa electron làm vật nhiễm điện âm."
                },
                {
                    "id": "c",
                    "text": "Hai vật mang điện tích âm khi đặt gần nhau sẽ hút nhau một lực rất mạnh.",
                    "answer": False,
                    "explanation": "Sai. Hai điện tích cùng dấu âm sẽ đẩy nhau."
                },
                {
                    "id": "d",
                    "text": "Sét trong tự nhiên là hiện tượng phóng điện tia lửa điện khổng lồ giữa các đám mây tích điện trái dấu hoặc giữa đám mây và mặt đất.",
                    "answer": True,
                    "explanation": "Đúng. Bản chất hiện tượng sét là sự phóng điện mạnh trong khí quyển."
                }
            ]
        },
        {
            "q": f"Đánh giá về các tác dụng của dòng điện và ứng dụng trong công nghệ hiện đại đề {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Tác dụng phát sáng của dòng điện chỉ xảy ra khi vật dẫn bị nung nóng đến nhiệt độ trên 2000°C.",
                    "answer": False,
                    "explanation": "Sai. Đèn LED, đèn huỳnh quang, đèn neon phát quang mà không cần nung nóng dây tóc đến 2000°C."
                },
                {
                    "id": "b",
                    "text": "Trong công nghệ luyện nhôm điện phân nóng chảy, người ta ứng dụng tác dụng hóa học của dòng điện một chiều.",
                    "answer": True,
                    "explanation": "Đúng. Điện phân nhôm oxit nóng chảy để thu nhôm kim loại là ứng dụng tác dụng hóa học."
                },
                {
                    "id": "c",
                    "text": "Động cơ điện trong máy bơm nước hoạt động dựa trên tác dụng từ của dòng điện.",
                    "answer": True,
                    "explanation": "Đúng. Dòng điện tạo từ trường làm quay rôto của động cơ."
                },
                {
                    "id": "d",
                    "text": "Tác dụng sinh lí của dòng điện luôn luôn gây hại và không có bất kì ứng dụng có ích nào.",
                    "answer": False,
                    "explanation": "Sai. Tác dụng sinh lí được ứng dụng y học: máy khử rung tim, châm cứu điện phục hồi chức năng."
                }
            ]
        },
        {
            "q": f"Xem xét về đoạn mạch mắc nối tiếp và song song trong hệ thống điện tổng hợp {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Khi hai điện trở R1 và R2 mắc song song, điện trở tương đương Rtd luôn thỏa mãn hệ thức Rtd = (R1 * R2) / (R1 + R2).",
                    "answer": True,
                    "explanation": "Đúng. Công thức tính Rtd cho 2 điện trở song song."
                },
                {
                    "id": "b",
                    "text": "Trong mạch nối tiếp, cường độ dòng điện chạy qua điện trở có giá trị lớn hơn sẽ nhỏ hơn cường độ qua điện trở nhỏ hơn.",
                    "answer": False,
                    "explanation": "Sai. Mạch nối tiếp thì dòng điện bằng nhau ở mọi điểm: I1 = I2 = I."
                },
                {
                    "id": "c",
                    "text": "Mắc song song các thiết bị điện giúp mỗi thiết bị hoạt động độc lập mà không phụ thuộc vào trạng thái bật/tắt của thiết bị khác.",
                    "answer": True,
                    "explanation": "Đúng. Ưu điểm cốt lõi của mạch điện song song trong gia đình."
                },
                {
                    "id": "d",
                    "text": "Tổng điện trở tương đương của đoạn mạch nối tiếp luôn nhỏ hơn mỗi điện trở thành phần.",
                    "answer": False,
                    "explanation": "Sai. Mạch nối tiếp có Rtd = R1 + R2 nên Rtd luôn lớn hơn R1 và R2."
                }
            ]
        },
        {
            "q": f"Đánh giá về an toàn điện và sử dụng điện thông minh trong gia đình bài ôn tập {t}:",
            "statements": [
                {
                    "id": "a",
                    "text": "Khi lắp đặt mạng điện gia đình, cầu chì và công tắc điều khiển bắt buộc phải được đặt trên dây pha (dây lửa).",
                    "answer": True,
                    "explanation": "Đúng. Đặt trên dây pha để khi ngắt công tắc hoặc đứt cầu chì thì thiết bị không còn nối với nguồn điện thế cao."
                },
                {
                    "id": "b",
                    "text": "Aptomat chống rò điện (ELCB/RCCB) tự động ngắt nguồn khi phát hiện dòng điện rò rỉ ra vỏ máy vượt ngưỡng an toàn (thường là 30 mA).",
                    "answer": True,
                    "explanation": "Đúng. Thiết bị bảo vệ an toàn tính mạng con người chống điện giật hiệu quả."
                },
                {
                    "id": "c",
                    "text": "Có thể dùng dây đồng thay thế cho dây chì trong cầu chì gia đình khi cầu chì bị đứt.",
                    "answer": False,
                    "explanation": "Sai. Dây đồng có nhiệt độ nóng chảy rất cao, không đứt kịp thời khi đoản mạch gây hỏa hoạn."
                },
                {
                    "id": "d",
                    "text": "Cột thu lôi (kim chống sét) lắp đặt trên đỉnh các tòa nhà cao tầng có tác dụng dẫn điện tích sét an toàn xuống lòng đất.",
                    "answer": True,
                    "explanation": "Đúng. Bảo vệ công trình xây dựng khỏi sét đánh phá hoại."
                }
            ]
        }
    ]

    r_val = round(12 + t*4, 1)
    sa = [
        {
            "q": f"Một đoạn mạch gồm điện trở R1 = {r_val} Ω mắc nối tiếp với điện trở R2 = {r_val * 1.5:.1f} Ω vào nguồn điện có hiệu điện thế U = {p_u} V. Cường độ dòng điện trong mạch bằng bao nhiêu Ampe (A)? (Làm tròn đến 3 chữ số thập phân).",
            "answer": f"{round(p_u / (r_val + r_val * 1.5), 3)}",
            "unit": "A",
            "explanation": f"Rtd = {r_val} + {r_val * 1.5:.1f} = {r_val * 2.5:.1f} Ω. I = {p_u} / {r_val * 2.5:.1f} = {round(p_u / (r_val * 2.5), 3)} A."
        },
        {
            "q": f"Hai điện trở R1 = {20 + t*10} Ω và R2 = {30 + t*10} Ω mắc song song vào nguồn hiệu điện thế 12 V. Tính cường độ dòng điện ở mạch chính (A). (Làm tròn đến 3 chữ số thập phân).",
            "answer": f"{round(12 / (20 + t*10) + 12 / (30 + t*10), 3)}",
            "unit": "A",
            "explanation": f"I = I1 + I2 = 12 / {20+t*10} + 12 / {30+t*10} = {round(12 / (20 + t*10) + 12 / (30 + t*10), 3)} A."
        },
        {
            "q": f"Một bóng đèn ghi 220V - {60 + t*15}W được thắp sáng liên tục trong {4 + t} giờ mỗi ngày. Tính điện năng tiêu thụ của bóng đèn trong 30 ngày (theo đơn vị kilôoát giờ - kWh). (Làm tròn đến 2 chữ số thập phân).",
            "answer": f"{round((60 + t*15) * (4 + t) * 30 / 1000, 2)}",
            "unit": "kWh",
            "explanation": f"A = P * t = {(60+t*15)} * ({(4+t)} * 30) / 1000 = {round((60 + t*15) * (4 + t) * 30 / 1000, 2)} kWh."
        },
        {
            "q": f"Một bếp điện có công suất P = {p_power} W hoạt động ở hiệu điện thế 220 V. Cường độ dòng điện định mức chạy qua bếp điện bằng bao nhiêu Ampe (A)? (Làm tròn đến 2 chữ số thập phân).",
            "answer": f"{round(p_power / 220, 2)}",
            "unit": "A",
            "explanation": f"I = P / U = {p_power} / 220 = {round(p_power / 220, 2)} A."
        },
        {
            "q": f"Một dây dẫn có dòng điện I = {0.8 + t*0.2:.1f} A chạy qua trong thời gian {5 * t} phút. Lượng điện tích chuyển qua tiết diện dây dẫn trong khoảng thời gian trên bằng bao nhiêu Culông (C)?",
            "answer": f"{round((0.8 + t*0.2) * (5 * t * 60))}",
            "unit": "C",
            "explanation": f"q = I * t = {0.8 + t*0.2:.1f} * ({5*t} * 60) = {round((0.8 + t*0.2) * (5 * t * 60))} C."
        },
        {
            "q": f"Một vôn kế có thang đo cực đại {15 + t*5} V được chia đều thành 50 vạch. Khi kim vôn kế chỉ ở vạch thứ {25 + t*3}, giá trị hiệu điện thế hiển thị là bao nhiêu Vôn (V)?",
            "answer": f"{round((15 + t*5) / 50 * (25 + t*3), 2)}",
            "unit": "V",
            "explanation": f"U = (GHĐ / số vạch) * vạch chỉ = {(15+t*5)} / 50 * {(25+t*3)} = {round((15 + t*5) / 50 * (25 + t*3), 2)} V."
        }
    ]

    vdc = [
        {
            "q": f"Một hộ gia đình sử dụng mạng điện 220 V gồm các thiết bị điện hoạt động hàng ngày:\\n"
                f"- 1 nồi cơm điện công suất {700 + t*50} W dùng {1.5 + t*0.2:.1f} giờ/ngày.\\n"
                f"- 1 bình nóng lạnh công suất {2000 + t*100} W dùng 1,0 giờ/ngày.\\n"
                f"- 4 bóng đèn LED công suất {15 + t*2} W mỗi bóng dùng {5 + t} giờ/ngày.\\n"
                f"- 2 quạt điện công suất {55 + t*5} W mỗi quạt dùng {8 + t} giờ/ngày.\\n"
                f"1. Tính tổng điện năng tiêu thụ của gia đình trong một tháng (30 ngày) theo đơn vị kWh.\\n"
                f"2. Tính tiền điện phải trả trong tháng theo biểu giá bậc thang: 50 kWh đầu giá 1800 đ/kWh, 50 kWh tiếp theo giá 1900 đ/kWh, phần còn lại giá 2200 đ/kWh (chưa tính 8% thuế VAT), và tổng số tiền có thuế VAT.",
            "type": "vdc",
            "solution": f"1. Điện năng tiêu thụ mỗi ngày của từng thiết bị:\\n"
                        f"- Nồi cơm: A1 = {700 + t*50} * {1.5 + t*0.2:.1f} = {round((700+t*50)*(1.5+t*0.2), 1)} Wh.\\n"
                        f"- Bình nóng lạnh: A2 = {2000 + t*100} * 1.0 = {2000 + t*100} Wh.\\n"
                        f"- 4 đèn LED: A3 = 4 * {15 + t*2} * {5 + t} = {4 * (15+t*2) * (5+t)} Wh.\\n"
                        f"- 2 quạt điện: A4 = 2 * {55 + t*5} * {8 + t} = {2 * (55+t*5) * (8+t)} Wh.\\n"
                        f"Tổng điện năng 1 ngày: A_ngay = {round((700+t*50)*(1.5+t*0.2) + (2000+t*100) + 4*(15+t*2)*(5+t) + 2*(55+t*5)*(8+t), 1)} Wh = {round(((700+t*50)*(1.5+t*0.2) + (2000+t*100) + 4*(15+t*2)*(5+t) + 2*(55+t*5)*(8+t))/1000, 3)} kWh.\\n"
                        f"Tổng điện năng 30 ngày: A_thang = {round(((700+t*50)*(1.5+t*0.2) + (2000+t*100) + 4*(15+t*2)*(5+t) + 2*(55+t*5)*(8+t))/1000 * 30, 2)} kWh.\\n"
                        f"2. Tính tiền điện:\\n"
                        f"Gọi A = {round(((700+t*50)*(1.5+t*0.2) + (2000+t*100) + 4*(15+t*2)*(5+t) + 2*(55+t*5)*(8+t))/1000 * 30, 2)} kWh.\\n"
                        f"- Tiền bậc 1 (50 kWh): 50 * 1800 = 90 000 đồng.\\n"
                        f"- Tiền bậc 2 (50 kWh): 50 * 1900 = 95 000 đồng.\\n"
                        f"- Tiền bậc 3 (A - 100 kWh): (A - 100) * 2200 = {round((((700+t*50)*(1.5+t*0.2) + (2000+t*100) + 4*(15+t*2)*(5+t) + 2*(55+t*5)*(8+t))/1000 * 30 - 100) * 2200)} đồng.\\n"
                        f"Tổng tiền chưa thuế: T1 = 90000 + 95000 + {round((((700+t*50)*(1.5+t*0.2) + (2000+t*100) + 4*(15+t*2)*(5+t) + 2*(55+t*5)*(8+t))/1000 * 30 - 100) * 2200)} đồng = {round(185000 + (((700+t*50)*(1.5+t*0.2) + (2000+t*100) + 4*(15+t*2)*(5+t) + 2*(55+t*5)*(8+t))/1000 * 30 - 100) * 2200)} đồng.\\n"
                        f"Tổng tiền có 8% thuế VAT: T_vat = T1 * 1.08 = {round((185000 + (((700+t*50)*(1.5+t*0.2) + (2000+t*100) + 4*(15+t*2)*(5+t) + 2*(55+t*5)*(8+t))/1000 * 30 - 100) * 2200) * 1.08)} đồng."
        },
        {
            "q": f"Một dây dẫn điện bằng nhôm truyền tải điện năng từ nhà máy đến khu dân cư ở khoảng cách l = {5 + t} km. Dây đôi có hai sợi, tiết diện mỗi sợi dây là S = {50 + t*10} mm2, điện trở suất của nhôm là ρ = 2,8 . 10^-8 Ω.m. Công suất điện cần truyền tải ở khu dân cư là P = {100 + t*20} kW dưới hiệu điện thế U = {p_u * 100} V.\\n"
                f"1. Tính tổng chiều dài và điện trở của đường dây tải điện.\\n"
                f"2. Tính cường độ dòng điện chạy trên đường dây và công suất hao phí do tỏa nhiệt trên đường dây.\\n"
                f"3. Tính hiệu suất truyền tải điện năng của hệ thống.",
            "type": "vdc",
            "solution": f"1. Đường dây đôi có chiều dài tổng cộng: L = 2 * l = 2 * {5 + t} = {2*(5+t)} km = {2*(5+t)*1000} m.\\n"
                        f"Tiết diện dây nhôm: S = {50 + t*10} mm2 = {(50 + t*10)*1e-6} m2.\\n"
                        f"Điện trở toàn bộ đường dây: R_day = ρ * (L / S) = (2,8 . 10^-8 * {2*(5+t)*1000}) / ({(50 + t*10)*1e-6}) = {round(2.8e-8 * 2*(5+t)*1000 / ((50+t*10)*1e-6), 3)} Ω.\\n"
                        f"2. Cường độ dòng điện trên đường dây: I = P / U = ({100 + t*20} * 1000) / ({p_u * 100}) = {round((100+t*20)*1000 / (p_u*100), 2)} A.\\n"
                        f"Công suất tỏa nhiệt hao phí trên đường dây:\\n"
                        f"P_hp = I^2 * R_day = ({round((100+t*20)*1000 / (p_u*100), 2)})^2 * {round(2.8e-8 * 2*(5+t)*1000 / ((50+t*10)*1e-6), 3)} = {round(((100+t*20)*1000 / (p_u*100))**2 * (2.8e-8 * 2*(5+t)*1000 / ((50+t*10)*1e-6)), 1)} W = {round(((100+t*20)*1000 / (p_u*100))**2 * (2.8e-8 * 2*(5+t)*1000 / ((50+t*10)*1e-6)) / 1000, 2)} kW.\\n"
                        f"3. Hiệu suất truyền tải điện:\\n"
                        f"H = P / (P + P_hp) = ({100 + t*20}) / ({100 + t*20} + {round(((100+t*20)*1000 / (p_u*100))**2 * (2.8e-8 * 2*(5+t)*1000 / ((50+t*10)*1e-6)) / 1000, 2)}) = {round((100+t*20) / ((100+t*20) + ((100+t*20)*1000 / (p_u*100))**2 * (2.8e-8 * 2*(5+t)*1000 / ((50+t*10)*1e-6)) / 1000) * 100, 2)}%."
        },
        {
            "q": f"Một bình nước nóng trực tiếp có công suất P = {3500 + t*500} W được cấp điện từ nguồn 220 V. Lưu lượng nước chảy qua bình là {3.0 + t*0.5:.1f} lít/phút. Nhiệt độ ban đầu của nước vào là {20 + t}°C. Biết nhiệt dung riêng của nước c = 4200 J/(kg.K), khối lượng riêng của nước D = 1000 kg/m3 và hiệu suất gia nhiệt của thanh điện trở đạt {90 + t}%.\\n"
                f"1. Tính cường độ dòng điện định mức và chọn tiết diện dây đồng dẫn điện tối thiểu cấp nguồn cho bình (biết mật độ dòng điện cho phép của dây đồng trong tường là J = 6 A/mm2).\\n"
                f"2. Tính nhiệt độ của dòng nước nóng chảy ra ở vòi hoa sen.",
            "type": "vdc",
            "solution": f"1. Cường độ dòng điện định mức của bình nóng lạnh:\\n"
                        f"I = P / U = {3500 + t*500} / 220 = {round((3500+t*500)/220, 2)} A.\\n"
                        f"Tiết diện dây dẫn đồng tối thiểu yêu cầu:\\n"
                        f"S_min = I / J = {round((3500+t*500)/220, 2)} / 6 = {round((3500+t*500)/220 / 6, 2)} mm2 (trong thực tế chọn dây 2.5 mm2 hoặc 4.0 mm2).\\n"
                        f"2. Tính nhiệt độ nước ra:\\n"
                        f"Trong thời gian 1 phút (60 giây):\\n"
                        f"Khối lượng nước chảy qua: m = V * D = ({3.0 + t*0.5:.1f} * 10^-3) * 1000 = {3.0 + t*0.5:.1f} kg.\\n"
                        f"Điện năng tiêu thụ trong 1 phút: A = P * t = {3500 + t*500} * 60 = {(3500+t*500)*60} J.\\n"
                        f"Nhiệt lượng nước hấp thụ: Q_thu = A * H = {(3500+t*500)*60} * ({90 + t}/100) = {round((3500+t*500)*60 * (90+t)/100)} J.\\n"
                        f"Độ tăng nhiệt độ của nước:\\n"
                        f"Δt = Q_thu / (m * c) = {round((3500+t*500)*60 * (90+t)/100)} / ({3.0 + t*0.5:.1f} * 4200) = {round((3500+t*500)*60 * (90+t)/100 / ((3.0+t*0.5)*4200), 1)}°C.\\n"
                        f"Nhiệt độ nước chảy ra: t_ra = t_vao + Δt = {20 + t} + {round((3500+t*500)*60 * (90+t)/100 / ((3.0+t*0.5)*4200), 1)} = {round(20 + t + (3500+t*500)*60 * (90+t)/100 / ((3.0+t*0.5)*4200), 1)}°C."
        },
        {
            "q": f"Một bộ pin mặt trời trên mái nhà gồm {12 + t*2} tấm pin quang điện giống nhau. Mỗi tấm pin khi có nắng chuẩn tạo ra hiệu điện thế hở mạch U_oc = {21 + t} V và sinh dòng đoản mạch I_sc = {5.5 + t*0.5:.1f} A. Khi hoạt động tối ưu, mỗi tấm cho công suất P_opt = {80 + t*10} W với điện áp làm việc U_mp = {17 + t} V.\\n"
                f"1. Nếu ghép toàn bộ {12 + t*2} tấm pin thành {round((12+t*2)/2)} nhánh song song, mỗi nhánh gồm 2 tấm nối tiếp thì hiệu điện thế và công suất cực đại của hệ thống pin là bao nhiêu?\\n"
                f"2. Hệ thống này nạp cho dàn acquy {24 + t*12} V có dung lượng {100 + t*20} Ah qua bộ điều khiển sạc MPPT có hiệu suất 95%. Tính thời gian chiếu nắng liên tục tối thiểu (giờ) để sạc đầy dàn acquy từ trạng thái đã cạn 80% dung lượng.",
            "type": "vdc",
            "solution": f"1. Ghép 2 tấm nối tiếp trong mỗi nhánh:\\n"
                        f"Hiệu điện thế làm việc của mỗi nhánh: U_nhanh = 2 * U_mp = 2 * {17 + t} = {2*(17+t)} V.\\n"
                        f"Vì {round((12+t*2)/2)} nhánh mắc song song nên hiệu điện thế toàn hệ thống: U_he = U_nhanh = {2*(17+t)} V.\\n"
                        f"Tổng công suất cực đại của cả hệ thống {12 + t*2} tấm:\\n"
                        f"P_max = ({12 + t*2}) * P_opt = ({12 + t*2}) * {80 + t*10} = {round((12+t*2)*(80+t*10))} W = {round((12+t*2)*(80+t*10)/1000, 3)} kW.\\n"
                        f"2. Năng lượng cần sạc cho dàn acquy {24 + t*12} V dung lượng {100 + t*20} Ah khi cạn 80%:\\n"
                        f"Điện lượng cần nạp: Q_nap = {100 + t*20} * 80% = {round((100+t*20)*0.8, 1)} Ah.\\n"
                        f"Năng lượng cần nạp: E_nap = U_acquy * Q_nap = {24 + t*12} * {round((100+t*20)*0.8, 1)} = {round((24+t*12)*(100+t*20)*0.8, 1)} Wh.\\n"
                        f"Công suất sạc thực tế cấp từ pin qua MPPT: P_sac = P_max * 95% = {round((12+t*2)*(80+t*10))} * 0.95 = {round((12+t*2)*(80+t*10)*0.95, 1)} W.\\n"
                        f"Thời gian chiếu nắng tối thiểu cần thiết:\\n"
                        f"t_nang = E_nap / P_sac = {round((24+t*12)*(100+t*20)*0.8, 1)} / {round((12+t*2)*(80+t*10)*0.95, 1)} = {round(((24+t*12)*(100+t*20)*0.8) / ((12+t*2)*(80+t*10)*0.95), 2)} giờ."
        }
    ]

    return {
        "id": f"phys8_c5_rev_test{t}",
        "title": f"KHTN 8 - [Đề tổng hợp] Ôn tập cuối Chương V - Đề {t}",
        "subject": "KHTN 8 - Vật lí",
        "duration": 45,
        "parts": {
            "part1": mc,
            "part2": tf,
            "part3": sa,
            "vdc": vdc
        }
    }


def get_c5_part2_exams():
    exams = {}
    # b23 (3)
    for t in range(1, 4):
        ex = make_b23_test(t)
        exams[ex["id"]] = ex
    # b24 (3)
    for t in range(1, 4):
        ex = make_b24_test(t)
        exams[ex["id"]] = ex
    # b25 (3)
    for t in range(1, 4):
        ex = make_b25_test(t)
        exams[ex["id"]] = ex
    # rev (5)
    for t in range(1, 6):
        ex = make_c5_rev_test(t)
        exams[ex["id"]] = ex
    return exams

if __name__ == "__main__":
    exams = get_c5_part2_exams()
    print(f"Total C5 Part 2 exams: {len(exams)}")
'''

with open(r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt\build_phys8_c5_part2.py", "w", encoding="utf-8") as f:
    f.write(content)

print("build_phys8_c5_part2.py written successfully.")
