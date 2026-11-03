# -*- coding: utf-8 -*-
# c5_rev.py - [Đề tổng hợp] Ôn tập cuối Chương V (5 đề độc lập 100%)
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

def get_c5_rev_exams():
    exams = {}
    ch_id = "phys8_c5"
    ch_title = "Chương V: Điện"
    l_id = "phys8_c5_rev"
    l_name = "[Đề tổng hợp] Ôn tập cuối Chương V"

    def meta(t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # ĐỀ 1: Nhiễm điện, Điện tích & Cấu tạo nguyên tử
    exams[f"{l_id}_test1"] = meta(1,
        [
            make_mc(1, "Nhận biết", "Một vật sau khi cọ xát có khả năng hút các mẩu giấy vụn nhỏ chứng tỏ vật đó:", ["Đã bị nhiễm điện (mang điện tích)", "Đã biến thành nam châm", "Khối lượng tăng lên gấp đôi", "Đã bị nóng chảy"], 0, "Cọ xát làm vật nhiễm điện, có khả năng hút vật nhẹ."),
            make_mc(2, "Nhận biết", "Trong tự nhiên có mấy loại điện tích và được gọi tên là gì?", ["Có hai loại: điện tích dương (+) và điện tích âm (-)", "Có một loại duy nhất", "Có ba loại: dương, âm và trung hòa", "Có vô số loại"], 0, "Có 2 loại điện tích: dương và âm."),
            make_mc(3, "Nhận biết", "Quy tắc tương tác giữa hai vật mang điện tích là:", ["Các điện tích cùng dấu thì đẩy nhau, khác dấu thì hút nhau", "Luôn luôn hút nhau", "Luôn luôn đẩy nhau", "Không tương tác"], 0, "Cùng dấu đẩy nhau, khác dấu hút nhau."),
            make_mc(4, "Nhận biết", "Khi cọ xát thanh thủy tinh vào mảnh lụa, thanh thủy tinh nhiễm điện dương vì thanh thủy tinh đã:", ["Mất bớt electron chuyển sang mảnh lụa", "Nhận thêm electron từ mảnh lụa", "Mất bớt proton", "Nhận thêm hạt nhân"], 0, "Mất electron làm vật mang điện dương."),
            make_mc(5, "Nhận biết", "Khi cọ xát thước nhựa vào mảnh dạ, thước nhựa nhiễm điện âm vì thước nhựa đã:", ["Nhận thêm electron từ mảnh dạ", "Mất bớt electron", "Nhận thêm proton", "Mất hạt nhân"], 0, "Nhận thêm electron làm vật mang điện âm."),
            make_mc(6, "Nhận biết", "Cấu tạo của một nguyên tử trung hòa về điện gồm có:", ["Hạt nhân mang điện dương ở giữa và các electron mang điện âm chuyển động xung quanh", "Chỉ có các electron", "Hạt nhân mang điện âm", "Chỉ có neutron"], 0, "Hạt nhân (+) và lớp vỏ electron (-)."),
            make_mc(7, "Thông hiểu", "Một quả cầu kim loại A mang điện dương đặt gần quả cầu B mang điện âm thì chúng sẽ:", ["Hút nhau một lực tĩnh điện", "Đẩy nhau ra xa", "Không có lực tác dụng", "Phát ra tiếng nổ lớn"], 0, "Hai điện tích trái dấu hút nhau."),
            make_mc(8, "Thông hiểu", "Hiện tượng sấm sét trong cơn dông bản chất là:", ["Hiện tượng phóng tia lửa điện khổng lồ giữa các đám mây tích điện trái dấu hoặc giữa đám mây và mặt đất", "Gió thổi mạnh va vào mây", "Mặt trời chiếu sáng mây", "Mưa đá cọ xát"], 0, "Sét là sự phóng điện mạnh trong khí quyển."),
            make_mc(9, "Thông hiểu", "Cột thu lôi (kim chống sét) được lắp trên nóc các tòa nhà cao tầng có tác dụng gì?", ["Dẫn điện tích từ đám mây sét an toàn xuống lòng đất để bảo vệ công trình", "Hút sét để tạo ra điện năng tích trữ", "Làm tan biến mây dông", "Làm đẹp ngôi nhà"], 0, "Dẫn điện tích sét xuống đất an toàn."),
            make_mc(10, "Thông hiểu", "Vào mùa đông hanh khô, khi cởi áo len bằng sợi tổng hợp ta thường nghe thấy tiếng lách tách nhỏ và thấy tia sáng li ti vì:", ["Hiện tượng nhiễm điện do cọ xát giữa các lớp áo gây phóng tia lửa điện nhỏ", "Áo len bị cháy", "Sợi len bị đứt", "Áo len bị nhiễm từ"], 0, "Cọ xát giữa các lớp áo sinh tĩnh điện phóng tia lửa nhỏ."),
            make_mc(11, "Thông hiểu", "Tại các trạm xăng dầu, người ta cấm sử dụng điện thoại di động và mặc quần áo dễ tích điện vì:", ["Tĩnh điện phóng tia lửa có thể bắt cháy hơi xăng dầu gây hỏa hoạn cháy nổ", "Làm hỏng điện thoại", "Làm xăng bị bay hơi nhanh", "Làm tắc vòi bơm xăng"], 0, "Tránh tia lửa tĩnh điện kích nổ hơi xăng."),
            make_mc(12, "Thông hiểu", "Xe bồn chở xăng dầu thường có một sợi xích sắt thả kéo lê tiếp xúc với mặt đường nhằm mục đích:", ["Dẫn các điện tích tĩnh sinh ra do xăng sóng sánh cọ xát xuống đất triệt tiêu nguy cơ cháy nổ", "Báo hiệu cho xe sau", "Giảm tốc độ xe bồn", "Đo độ gồ ghề của mặt đường"], 0, "Tiếp địa triệt tiêu tĩnh điện trên xe bồn.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về hiện tượng nhiễm điện do cọ xát và bảo toàn điện tích tổng hợp 1:", [
                ("a", "Nhiễm điện do cọ xát là do các electron chuyển dịch từ vật này sang vật khác.", True),
                ("b", "Vật nhận thêm electron sẽ mang điện tích dương.", False),
                ("c", "Vật mất bớt electron sẽ mang điện tích dương.", True),
                ("d", "Tổng điện tích của hai vật cô lập trước và sau khi cọ xát được bảo toàn.", True)
            ], "Nhận thêm electron mang điện tích âm."),
            make_tf(2, "Thông hiểu", "Về cấu tạo hạt nhân nguyên tử và các hạt mang điện tổng hợp 1:", [
                ("a", "Hạt proton trong hạt nhân nguyên tử mang điện tích dương.", True),
                ("b", "Hạt electron có khối lượng rất nhỏ so với proton và mang điện tích âm.", True),
                ("c", "Hạt neutron nằm trong hạt nhân mang điện tích âm gấp đôi electron.", False),
                ("d", "Bình thường nguyên tử trung hòa về điện vì tổng điện tích dương hạt nhân bằng tổng điện tích âm của vỏ electron.", True)
            ], "Neutron là hạt không mang điện tích."),
            make_tf(3, "Thông hiểu", "Về tương tác tĩnh điện giữa các vật nhiễm điện tổng hợp 1:", [
                ("a", "Hai thanh nhựa cùng cọ xát vào vải dạ sẽ nhiễm điện cùng dấu và đẩy nhau.", True),
                ("b", "Thanh thủy tinh cọ xát lụa và thanh nhựa cọ xát dạ sẽ hút nhau khi đặt gần nhau.", True),
                ("c", "Lực tương tác tĩnh điện giữa hai quả cầu tăng lên khi ta đưa chúng ra xa nhau hơn.", False),
                ("d", "Một vật nhiễm điện có thể hút một mẩu giấy vụn trung hòa về điện nhờ hiện tượng hưởng ứng.", True)
            ], "Lực tĩnh điện tỉ lệ nghịch với bình phương khoảng cách, đưa ra xa thì lực giảm."),
            make_tf(4, "Thông hiểu", "Về phòng chống tai nạn sét đánh trong tự nhiên tổng hợp 1:", [
                ("a", "Khi trời mưa dông có sấm sét, tuyệt đối không được trú mưa dưới gốc cây to đứng đơn độc.", True),
                ("b", "Không cầm các vật bằng kim loại dài như cần câu, cuốc xẻng khi đang ở ngoài đồng trống.", True),
                ("c", "Ở trong xe ô tô đóng kín cửa là nơi trú ẩn an toàn trước sấm sét nhờ hiệu ứng lồng Faraday.", True),
                ("d", "Đứng tụ tập thành nhóm đông người dưới chòi tôn ngoài bãi biển để tránh sét tốt hơn.", False)
            ], "Tập trung đông người ngoài bãi biển rất nguy hiểm dễ bị sét đánh trúng.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một quả cầu kim loại mang điện tích -8 . 10^-18 C. Biết điện tích của một electron là e = -1,6 . 10^-19 C. Quả cầu này đang thừa bao nhiêu hạt electron?", "50", "N = (-8e-18) / (-1,6e-19) = 50 hạt."),
            make_sa(2, "Thông hiểu", "Một vật trung hòa bị mất đi 2 . 10^12 electron khi cọ xát. Điện tích của vật sau khi cọ xát là bao nhiêu nC (1 nC = 10^-9 C)?", "320", "q = 2e12 * 1,6e-19 = 3,2e-7 C = 320 nC."),
            make_sa(3, "Thông hiểu", "Một đám mây dông mang điện tích âm phóng điện xuống đất truyền một lượng điện tích 25 C. Thời gian phóng điện là 0,001 giây. Cường độ dòng sét trung bình là bao nhiêu Ampe (A)?", "25000", "I = 25 / 0,001 = 25 000 A."),
            make_sa(4, "Thông hiểu", "Một giọt dầu lơ lửng cân bằng giữa hai bản kim loại tích điện mang điện tích đúng bằng 3 hạt electron. Độ lớn điện tích của giọt dầu là bao nhiêu lần 10^-19 Culông?", "4.8", "q = 3 * 1,6e-19 = 4,8 . 10^-19 C."),
            make_sa(5, "Vận dụng", "Hai quả cầu kim loại giống nhau mang điện tích q1 = +6 μC và q2 = -2 μC cho tiếp xúc nhau rồi tách ra. Điện tích của mỗi quả cầu sau khi tiếp xúc là bao nhiêu μC?", "2", "q' = (6 + (-2)) / 2 = 2 μC."),
            make_sa(6, "Vận dụng", "Một bộ lọc bụi tĩnh điện trong nhà máy xi măng tích điện cho hạt bụi để hút vào điện cực. Mỗi giây lọc giữ được 10^15 hạt bụi, mỗi hạt mang điện 10^-16 C. Dòng điện tĩnh tạo ra là bao nhiêu Ampe (A)?", "0.1", "I = 10^15 * 10^-16 = 0,1 A.")
        ],
        [
            make_vdc(1, "Một đám mây dông tích điện ở độ cao h = 1200 m so với mặt đất tạo ra một hiệu điện thế khổng lồ U = 6 . 10^7 V (60 triệu Vôn) đối với mặt đất. Khi phóng sét xuống đất, tia sét truyền một điện lượng q = 35 C trong thời gian 0,5 mili-giây (0,0005 s). Năng lượng giải phóng và công suất cực đại của tia sét xấp xỉ bằng:", [
                "Năng lượng 2,1 GJ (2,1 tỉ Jun); công suất 4,2 . 10^12 W",
                "Năng lượng 1,0 GJ; công suất 2,0 . 10^9 W",
                "Năng lượng 500 MJ; công suất 1,0 . 10^6 W",
                "Năng lượng 10 MJ; công suất 20 kW"
            ], 0, "W = U * q = 6e7 * 35 = 2,1 . 10^9 J = 2,1 GJ. P = W / t = 2,1e9 / 0,0005 = 4,2 . 10^12 W."),
            make_vdc(2, "Trong công nghệ sơn tĩnh điện ô tô, các hạt sơn tích điện âm được phun ra từ đầu súng sơn điện thế -50 kV và bị vỏ xe nối đất (điện thế 0 V) hút dính chặt đều khắp bề mặt. Giả sử lưu lượng hạt sơn phun ra tạo thành dòng điện 0,2 mA trong suốt 10 phút sơn một cánh cửa xe. Tổng điện tích mà cánh cửa xe nhận được và số electron tương ứng là:", [
                "q = 0,12 C; N = 7,5 . 10^17 electron", "q = 0,24 C; N = 1,5 . 10^18 electron", "q = 1,2 C; N = 7,5 . 10^18 electron", "q = 0,012 C; N = 7,5 . 10^16 electron"
            ], 0, "q = I * t = (0,2e-3) * 600 = 0,12 C. N = 0,12 / (1,6e-19) = 7,5 . 10^17 hạt."),
            make_vdc(3, "Một máy photocopy hoạt động dựa trên hiện tượng tĩnh điện. Trống quang dẫn hình trụ có diện tích bề mặt S = 0,08 m2 được tích điện đều với mật độ điện tích σ = 1,5 . 10^-7 C/m2. Khi có ánh sáng phản xạ từ văn bản quét qua, 60% điện tích bề mặt được giải phóng. Lượng điện tích còn lại giữ mực trên bề mặt trống là:", [
                "4,8 nC (4,8 . 10^-9 C)", "12 nC", "7,2 nC", "2,4 nC"
            ], 0, "q_tong = S * σ = 0,08 * 1,5e-7 = 1,2 . 10^-8 C = 12 nC. q_con = 12 * 40% = 4,8 nC."),
            make_vdc(4, "Một hạt bụi mịn PM2.5 có khối lượng m = 1,6 . 10^-14 kg mang điện tích q = -3,2 . 10^-18 C bay vào một điện trường đều thẳng đứng hướng xuống dưới giữa hai bản kim loại. Để hạt bụi nằm lơ lửng cân bằng giữa hai bản kim loại thì cường độ điện trường E cần thiết (lấy g = 10 m/s2) bằng:", [
                "50 000 V/m", "25 000 V/m", "100 000 V/m", "10 000 V/m"
            ], 0, "F_dien = P => |q| * E = m * g => E = (1,6e-14 * 10) / (3,2e-18) = 1,6e-13 / 3,2e-18 = 50 000 V/m.")
        ]
    )

    # ĐỀ 2: Dòng điện trong kim loại, Nguồn điện & Mạch điện đơn giản
    exams[f"{l_id}_test2"] = meta(2,
        [
            make_mc(1, "Nhận biết", "Bản chất của dòng điện trong kim loại là dòng chuyển dời có hướng của:", ["Các electron tự do", "Các ion dương", "Các ion âm", "Các proton"], 0, "Dòng điện trong kim loại là dòng electron tự do dịch chuyển có hướng."),
            make_mc(2, "Nhận biết", "Chiều quy ước của dòng điện trong mạch điện kín chạy:", ["Từ cực dương qua dây dẫn và thiết bị điện tới cực âm của nguồn", "Từ cực âm về cực dương", "Cùng chiều electron", "Tùy ý"], 0, "Quy ước chiều dòng điện: từ dương sang âm qua mạch ngoài."),
            make_mc(3, "Nhận biết", "Nguồn điện có vai trò cơ bản nào trong mạch điện?", ["Cung cấp năng lượng điện và duy trì hiệu điện thế giữa hai đầu mạch", "Tiêu thụ bớt điện tích", "Đóng ngắt dòng điện", "Tỏa nhiệt sưởi ấm"], 0, "Duy trì hiệu điện thế và cấp điện năng."),
            make_mc(4, "Nhận biết", "Kí hiệu nguồn điện một pin trên sơ đồ mạch điện gồm hai vạch song song, trong đó:", ["Vạch dài mảnh là cực (+), vạch ngắn dày là cực (-)", "Vạch ngắn là cực (+)", "Hai vạch bằng nhau", "Vạch tròn là cực (+)"], 0, "Vạch dài cực (+), vạch ngắn dày cực (-)."),
            make_mc(5, "Nhận biết", "Vật liệu nào sau đây là vật liệu dẫn điện tốt nhất?", ["Bạc và Đồng", "Gỗ khô", "Nhựa PVC", "Sứ cách điện"], 0, "Bạc và đồng là các kim loại dẫn điện tốt nhất."),
            make_mc(6, "Nhận biết", "Chất nào sau đây là chất cách điện trong điều kiện thường?", ["Cao su và Thủy tinh", "Dung dịch muối", "Nước chanh", "Dây nhôm"], 0, "Cao su và thủy tinh là chất cách điện."),
            make_mc(7, "Thông hiểu", "Trong một dây dẫn bằng đồng có dòng điện chạy từ A sang B, các electron tự do trong dây đang chuyển dời có hướng:", ["Từ B sang A (ngược chiều dòng điện)", "Từ A sang B", "Vuông góc với dây", "Đứng yên"], 0, "Electron dịch chuyển từ âm sang dương, ngược chiều dòng điện."),
            make_mc(8, "Thông hiểu", "Trường hợp nào sau đây mạch điện rơi vào trạng thái mạch hở?", ["Công tắc (khóa K) đang ở vị trí mở", "Bóng đèn đang sáng", "Pin mới lắp tiếp xúc tốt", "Dây dẫn nguyên vẹn"], 0, "Khóa mở tạo mạch hở, không có dòng."),
            make_mc(9, "Thông hiểu", "Tại sao lõi dây dẫn điện thường làm bằng đồng hoặc nhôm còn vỏ bọc ngoài làm bằng nhựa dẻo?", ["Đồng/nhôm dẫn điện tốt để tải điện, vỏ nhựa cách điện để bảo vệ an toàn chống điện giật", "Nhựa dẫn điện tốt hơn", "Để dây nặng hơn", "Để dây đổi màu"], 0, "Lõi dẫn điện, vỏ cách điện an toàn."),
            make_mc(10, "Thông hiểu", "Khi tháo pin ra khỏi đồ chơi điện tử thì đồ chơi ngừng hoạt động vì:", ["Mất nguồn điện duy trì hiệu điện thế làm dòng điện biến mất", "Đồ chơi bị hỏng mô tơ", "Dây dẫn bị đứt", "Đồ chơi bị nổ"], 0, "Không có nguồn điện thì không có dòng điện."),
            make_mc(11, "Thông hiểu", "Kí hiệu bóng đèn sợi đốt trên sơ đồ mạch điện là:", ["Một vòng tròn bên trong có dấu nhân (X)", "Hình chữ nhật có vạch thẳng", "Hình tam giác có mũi tên", "Hai vạch song song bằng nhau"], 0, "Vòng tròn có chữ X là kí hiệu bóng đèn."),
            make_mc(12, "Thông hiểu", "Trong các thiết bị sau, thiết bị nào KHÔNG PHẢI là nguồn điện?", ["Bóng đèn sợi đốt", "Viên pin con thỏ", "Acquy xe máy", "Pin mặt trời"], 0, "Bóng đèn là thiết bị tiêu thụ điện, không phải nguồn điện.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về bản chất hạt mang điện và nguồn điện tổng hợp 2:", [
                ("a", "Trong kim loại có mật độ electron tự do rất lớn chuyển động tự do giữa các nút mạng tinh thể.", True),
                ("b", "Nguồn điện tạo ra các electron mới và bơm liên tục vào trong dây dẫn kim loại.", False),
                ("c", "Hai cực của pin hoặc acquy luôn duy trì sự chênh lệch điện thế giữa cực dương và cực âm.", True),
                ("d", "Dòng điện sinh ra trong mạch kín ngay khi đóng công tắc nhờ điện trường lan truyền gần bằng vận tốc ánh sáng.", True)
            ], "Nguồn điện không sinh ra electron mới, nó chỉ tạo điện trường đẩy electron sẵn có trong dây."),
            make_tf(2, "Thông hiểu", "Về vật dẫn điện và vật cách điện trong kỹ thuật tổng hợp 2:", [
                ("a", "Vật dẫn điện là vật cho dòng điện chạy qua vì có nhiều hạt mang điện tự do.", True),
                ("b", "Vật cách điện là vật không cho dòng điện chạy qua vì hầu như không có hạt mang điện tự do.", True),
                ("c", "Không khí ở điều kiện thường là một chất dẫn điện rất tốt tương đương với đồng.", False),
                ("d", "Nước cất tinh khiết là chất cách điện, nhưng hòa thêm một lượng nhỏ muối ăn thì trở thành chất dẫn điện.", True)
            ], "Không khí thường là chất cách điện."),
            make_tf(3, "Thông hiểu", "Về sơ đồ mạch điện và lắp ráp thực hành tổng hợp 2:", [
                ("a", "Sơ đồ mạch điện giúp người thợ kỹ thuật lắp ráp và sửa chữa mạch chính xác.", True),
                ("b", "Mỗi linh kiện điện tử đều có một kí hiệu quy ước thống nhất trong các bản vẽ kỹ thuật.", True),
                ("c", "Khi công tắc đóng, dòng điện chỉ chạy từ cực dương đến bóng đèn rồi dừng lại tại bóng đèn.", False),
                ("d", "Dòng điện là một dòng khép kín liên tục tuần hoàn chạy qua nguồn và tải tiêu thụ.", True)
            ], "Dòng điện là dòng kín chạy qua toàn bộ mạch tuần hoàn."),
            make_tf(4, "Thông hiểu", "Về hiện tượng đoản mạch và công tắc an toàn tổng hợp 2:", [
                ("a", "Nối tắt hai cực nguồn điện bằng dây dẫn điện trở nhỏ sẽ gây hiện tượng đoản mạch nguy hiểm.", True),
                ("b", "Đoản mạch làm pin nhanh chóng bị kiệt năng lượng và có thể gây cháy nổ pin.", True),
                ("c", "Khóa K lắp trong phòng ngủ có chức năng biến đổi điện một chiều thành xoay chiều.", False),
                ("d", "Cầu dao tổng giúp ngắt toàn bộ nguồn điện cấp cho công trình khi cần sửa chữa an toàn.", True)
            ], "Khóa K chỉ đóng ngắt mạch điện.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một dòng điện không đổi I = 0,5 A chạy qua dây kim loại trong thời gian 30 giây. Lượng điện tích dịch chuyển qua tiết diện dây là bao nhiêu Culông (C)?", "15", "q = 0,5 * 30 = 15 C."),
            make_sa(2, "Thông hiểu", "Một acquy xe máy 12 V cấp điện cho đèn pha xe máy tiêu thụ công suất 36 W. Cường độ dòng điện qua đèn pha là bao nhiêu Ampe (A)?", "3", "I = 36 / 12 = 3 A."),
            make_sa(3, "Thông hiểu", "Một đèn pin sử dụng 3 viên pin tiểu loại 1,5 V mắc nối tiếp. Hiệu điện thế tổng cung cấp cho bóng đèn pin là bao nhiêu Vôn (V)?", "4.5", "U = 3 * 1,5 = 4,5 V."),
            make_sa(4, "Thông hiểu", "Một sợi dây đồng có điện trở 3 Ω. Cắt sợi dây thành 3 đoạn bằng nhau thì mỗi đoạn có điện trở là bao nhiêu Ôm (Ω)?", "1", "R1 = 3 / 3 = 1 Ω."),
            make_sa(5, "Vận dụng", "Trong 1 phút (60 giây), có 180 Culông điện tích chuyển qua tiết diện một dây cáp sạc điện thoại nhanh. Cường độ dòng điện sạc là bao nhiêu Ampe (A)?", "3", "I = 180 / 60 = 3 A."),
            make_sa(6, "Vận dụng", "Một bộ pin 6 V cấp điện cho một điện trở R thì đo được dòng điện 0,2 A. Giá trị điện trở R là bao nhiêu Ôm (Ω)?", "30", "R = 6 / 0,2 = 30 Ω.")
        ],
        [
            make_vdc(1, "Một xe ô tô điện sử dụng khối pin lithium-ion có hiệu điện thế danh định U = 400 V và dung lượng 75 kWh. Khi xe chạy với tốc độ ổn định trên cao tốc, động cơ điện tiêu thụ dòng điện trung bình I = 50 A. Công suất tiêu thụ của động cơ và thời gian xe có thể chạy liên tục với khối pin này là:", [
                "Công suất 20 kW; thời gian chạy 3,75 giờ", "Công suất 40 kW; thời gian chạy 1,875 giờ", "Công suất 10 kW; thời gian chạy 7,5 giờ", "Công suất 50 kW; thời gian chạy 2,0 giờ"
            ], 0, "P = U * I = 400 * 50 = 20 000 W = 20 kW. t = 75 kWh / 20 kW = 3,75 giờ."),
            make_vdc(2, "Một tấm pin năng lượng mặt trời có diện tích 1,6 m2 nhận bức xạ mặt trời với công suất quang học 1000 W/m2. Hiệu suất chuyển đổi quang - điện của tấm pin đạt 20%. Nếu tấm pin hoạt động ở hiệu điện thế 32 V thì cường độ dòng điện cực đại do tấm pin sinh ra là:", [
                "10,0 A", "5,0 A", "20,0 A", "2,5 A"
            ], 0, "P_quang = 1,6 * 1000 = 1600 W. P_dien = 1600 * 20% = 320 W. I = P_dien / U = 320 / 32 = 10,0 A."),
            make_vdc(3, "Một sợi dây cáp đồng hai sợi nối từ trạm nguồn đến một trạm bơm dài 500 m (chiều dài dây đi và về tổng cộng L = 1000 m). Tiết diện dây đồng S = 10 mm2, điện trở suất ρ = 1,7 . 10^-8 Ω.m. Dòng điện qua trạm bơm là I = 20 A. Độ sụt áp trên đường dây và hiệu điện thế thực tế tại trạm bơm (biết nguồn cấp U0 = 220 V) là:", [
                "ΔU = 34 V; U_bom = 186 V", "ΔU = 17 V; U_bom = 203 V", "ΔU = 68 V; U_bom = 152 V", "ΔU = 8,5 V; U_bom = 211,5 V"
            ], 0, "R = 1,7e-8 * 1000 / (10e-6) = 1,7 Ω. ΔU = 20 * 1,7 = 34 V. U_bom = 220 - 34 = 186 V."),
            make_vdc(4, "Một mạch điện chiếu sáng gồm 10 bóng đèn LED mắc nối tiếp với nhau. Mỗi bóng đèn khi hoạt động bình thường có hiệu điện thế định mức 3,2 V và dòng điện định mức 0,02 A. Toàn bộ mạch được cấp nguồn từ acquy 36 V qua một điện trở bảo vệ R. Giá trị của điện trở bảo vệ R để các đèn sáng bình thường là:", [
                "200 Ω", "100 Ω", "400 Ω", "150 Ω"
            ], 0, "U_den = 10 * 3,2 = 32 V. U_R = 36 - 32 = 4 V. R = 4 / 0,02 = 200 Ω.")
        ]
    )

    # ĐỀ 3: 5 Tác dụng của dòng điện & Ứng dụng kỹ thuật
    exams[f"{l_id}_test3"] = meta(3,
        [
            make_mc(1, "Nhận biết", "Dòng điện chạy qua dây mai so của bếp điện làm dây nóng đỏ thể hiện tác dụng gì của dòng điện?", ["Tác dụng nhiệt", "Tác dụng từ", "Tác dụng hóa học", "Tác dụng phát quang"], 0, "Bếp điện tỏa nhiệt do tác dụng nhiệt."),
            make_mc(2, "Nhận biết", "Bóng đèn sợi đốt phát sáng được là do tác dụng nào?", ["Tác dụng nhiệt làm nóng sáng dây tóc", "Tác dụng từ làm quay dây tóc", "Tác dụng hóa học nổ cháy", "Tác dụng sinh lí"], 0, "Nóng sáng do nhiệt độ rất cao."),
            make_mc(3, "Nhận biết", "Chuông điện gia đình reo khi nhấn nút là ứng dụng của tác dụng nào?", ["Tác dụng từ của nam châm điện", "Tác dụng hóa học", "Tác dụng phát sáng", "Tác dụng tĩnh điện"], 0, "Chuông điện hoạt động nhờ tác dụng từ."),
            make_mc(4, "Nhận biết", "Trong kĩ thuật mạ điện, hiện tượng kim loại bám vào điện cực âm thể hiện tác dụng gì?", ["Tác dụng hóa học", "Tác dụng cơ học", "Tác dụng nhiệt", "Tác dụng sinh lí"], 0, "Điện phân mạ điện là tác dụng hóa học."),
            make_mc(5, "Nhận biết", "Khi vô tình chạm vào nguồn điện trần bị giật cơ co giật là biểu hiện của tác dụng:", ["Tác dụng sinh lí", "Tác dụng từ", "Tác dụng hóa học", "Tác dụng phát sáng"], 0, "Dòng điện qua cơ thể gây co cơ, đó là tác dụng sinh lí."),
            make_mc(6, "Nhận biết", "Thiết bị nào sau đây KHÔNG hoạt động dựa trên tác dụng nhiệt của dòng điện?", ["Quạt máy để bàn", "Ấm siêu tốc", "Bàn là điện", "Nồi cơm điện"], 0, "Quạt điện hoạt động dựa trên tác dụng từ của động cơ điện."),
            make_mc(7, "Thông hiểu", "Vì sao trong nam châm điện người ta dùng lõi sắt non mà không dùng lõi thép?", ["Vì sắt non mất từ tính nhanh khi ngắt điện, còn thép giữ từ tính biến thành nam châm vĩnh cửu", "Vì sắt non đắt hơn thép", "Vì sắt non không dẫn từ", "Vì sắt non nhẹ hơn"], 0, "Sắt non tăng từ trường và mất từ tính ngay khi ngắt điện."),
            make_mc(8, "Thông hiểu", "Bút thử điện chứa khí neon phát sáng ở điện áp trên 40 V dựa trên tác dụng nào?", ["Tác dụng phát sáng (quang)", "Tác dụng nhiệt nóng đỏ dây tóc", "Tác dụng từ", "Tác dụng sinh lí"], 0, "Khí neon bị kích thích phóng điện phát quang trực tiếp."),
            make_mc(9, "Thông hiểu", "Khi mạ bạc cho chiếc thìa kim loại, chiếc thìa phải được gắn vào cực nào và nhúng vào dung dịch gì?", ["Gắn vào cực âm và nhúng vào dung dịch muối bạc AgNO3", "Gắn vào cực dương", "Gắn vào cực âm và nhúng vào nước cất", "Nhúng vào axit"], 0, "Vật mạ nối cực âm, dung dịch chứa muối bạc."),
            make_mc(10, "Thông hiểu", "Dây chì trong cầu chì ngắt mạch khi có sự cố chập điện là ứng dụng của tác dụng nào?", ["Tác dụng nhiệt của dòng điện đoản mạch làm nóng chảy dây chì", "Tác dụng từ bẻ gãy dây", "Tác dụng phát quang", "Tác dụng hóa học"], 0, "Nhiệt làm chảy đứt dây chì."),
            make_mc(11, "Thông hiểu", "Đèn LED (điốt phát quang) có ưu điểm tiết kiệm điện vượt trội so với đèn sợi đốt vì:", ["Nó biến đổi trực tiếp phần lớn điện năng thành quang năng mà tỏa rất ít nhiệt", "Nó không cần nguồn điện", "Nó chạy bằng pin vĩnh cửu", "Nó hấp thụ bóng tối"], 0, "Đèn LED phát quang bán dẫn trực tiếp, hiệu suất cao, ít tỏa nhiệt."),
            make_mc(12, "Thông hiểu", "Máy khử rung tim trong phòng cấp cứu dùng dòng điện truyền qua ngực bệnh nhân là ứng dụng có ích của:", ["Tác dụng sinh lí của dòng điện để kích thích cơ tim đập lại nhịp bình thường", "Tác dụng nhiệt sưởi ấm lồng ngực", "Tác dụng từ hút máu", "Tác dụng mạ vàng tim"], 0, "Kích thích tái lập nhịp tim qua tác dụng sinh lí.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về 5 tác dụng cơ bản của dòng điện trong tự nhiên và kỹ thuật tổng hợp 3:", [
                ("a", "Dòng điện luôn luôn chỉ thể hiện duy nhất một tác dụng trong mỗi thiết bị.", False),
                ("b", "Bóng đèn sợi đốt thể hiện đồng thời cả tác dụng nhiệt và tác dụng phát sáng.", True),
                ("c", "Dòng điện một chiều và xoay chiều đều có tác dụng nhiệt và tác dụng từ.", True),
                ("d", "Tác dụng hóa học chỉ xảy ra khi dùng dòng điện một chiều DC trong công nghệ mạ điện.", True)
            ], "Một thiết bị có thể đồng thời thể hiện nhiều tác dụng."),
            make_tf(2, "Thông hiểu", "Về tác dụng từ và cấu tạo của các máy điện thông dụng tổng hợp 3:", [
                ("a", "Cần cẩu điện hút phế liệu thép nhờ lực từ cực mạnh của cuộn dây nam châm điện.", True),
                ("b", "Để đảo cực từ Bắc - Nam của nam châm điện, ta chỉ cần đảo chiều dòng điện cấp cho cuộn dây.", True),
                ("c", "Nam châm điện có lõi nhôm sẽ tạo ra lực hút mạnh hơn gấp 10 lần lõi sắt non.", False),
                ("d", "Rơle điện từ dùng tác dụng từ để đóng ngắt mạch điện tự động an toàn.", True)
            ], "Nhôm không phải vật liệu sắt từ, không tạo nam châm điện mạnh."),
            make_tf(3, "Thông hiểu", "Về tác dụng hóa học và công nghệ luyện kim tổng hợp 3:", [
                ("a", "Trong bình mạ điện, kim loại hòa tan từ cực dương và kết tủa bám lên cực âm.", True),
                ("b", "Khối lượng kim loại mạ bám vào vật tỉ lệ thuận với thời gian điện phân.", True),
                ("c", "Có thể mạ vàng cho đồ trang sức bằng cách nhúng vào nước đường đun sôi có dòng điện.", False),
                ("d", "Công nghệ sản xuất nhôm nguyên chất từ quặng bô-xít sử dụng phương pháp điện phân nóng chảy.", True)
            ], "Nước đường không dẫn điện, không mạ được."),
            make_tf(4, "Thông hiểu", "Về tác dụng sinh lí và các quy chuẩn an toàn điện tổng hợp 3:", [
                ("a", "Dòng điện có cường độ 100 mA chạy qua tim có thể gây tử vong trong vài giây.", True),
                ("b", "Châm cứu điện và sốc điện hồi sức tim là các ứng dụng y khoa có ích của tác dụng sinh lí.", True),
                ("c", "Người đi giày cao su khô chạm vào một cực của nguồn pin 12 V sẽ bị điện giật ngã ngay.", False),
                ("d", "Khi có sự cố rò điện ra vỏ bình nóng lạnh, dây tiếp địa sẽ dẫn dòng điện an toàn xuống đất.", True)
            ], "Nguồn 12 V an toàn, đi giày cao su cách điện không bị giật.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một bình nóng lạnh 220 V - 2500 W tiêu thụ dòng điện định mức là bao nhiêu Ampe (A)? (Làm tròn đến 2 chữ số thập phân).", "11.36", "I = 2500 / 220 ≈ 11,36 A."),
            make_sa(2, "Thông hiểu", "Một nam châm điện cuộn dây 300 vòng hút được 18 đinh ghim. Để nam châm hút được 30 đinh ghim với dòng điện không đổi, cần quấn thêm bao nhiêu vòng dây cùng loại?", "200", "Số vòng tỉ lệ: N' = 300 * (30 / 18) = 500 vòng => Quấn thêm = 500 - 300 = 200 vòng."),
            make_sa(3, "Thông hiểu", "Một bể mạ đồng cho dòng điện 5 A chạy qua trong 40 phút (2400 giây). Lượng điện tích chuyển qua bể mạ là bao nhiêu Culông (C)?", "12000", "q = 5 * 2400 = 12 000 C."),
            make_sa(4, "Thông hiểu", "Một đèn LED tiêu thụ dòng điện 20 mA dưới hiệu điện thế 2,5 V. Công suất tiêu thụ của đèn LED là bao nhiêu Oát (W)?", "0.05", "P = 2,5 * 0,02 = 0,05 W."),
            make_sa(5, "Vận dụng", "Một ấm đun nước điện 1000 W đun sôi 1 lít nước cần 336 000 J nhiệt lượng có ích. Nếu hiệu suất ấm đạt 80%, thời gian đun sôi nước là bao nhiêu giây?", "420", "A = 336 000 / 0,8 = 420 000 J. t = 420 000 / 1000 = 420 s."),
            make_sa(6, "Vận dụng", "Bút thử điện chứa khí neon có điện trở R = 2,2 MΩ (2 200 000 Ω). Khi thử nguồn điện 220 V, dòng điện an toàn qua người là bao nhiêu miliampe (mA)?", "0.1", "I = 220 / 2200000 = 0,0001 A = 0,1 mA.")
        ],
        [
            make_vdc(1, "Một bể mạ vàng công nghiệp dùng để mạ cho 50 chiếc huy chương hình tròn bán kính r = 3 cm (diện tích hai mặt của mỗi chiếc là S = 2 * π * r^2). Lớp vàng yêu cầu có độ dày đồng đều h = 5 μm (5 . 10^-6 m). Biết khối lượng riêng của vàng là D = 19 300 kg/m3. Tổng khối lượng vàng cần dùng cho 50 chiếc huy chương này xấp xỉ bằng:", [
                "27,29 g", "13,64 g", "54,58 g", "5,46 g"
            ], 0, "S1 = 2 * 3,1416 * (0,03)^2 ≈ 0,005655 m2. S_tong = 50 * 0,005655 ≈ 0,2827 m2. V = 0,2827 * 5e-6 = 1,4137e-6 m3. m = 19300 * 1,4137e-6 ≈ 0,02729 kg = 27,29 g."),
            make_vdc(2, "Một cần cẩu nam châm điện hoạt động với nguồn 220 V có dòng điện 40 A chạy qua cuộn dây. Cuộn dây có điện trở r = 5 Ω và công suất cơ học nâng sắt phế liệu chiếm 30% công suất điện tiêu thụ. Công suất tỏa nhiệt hao phí trên cuộn dây và công suất cơ học nâng sắt lần lượt bằng:", [
                "P_nhiet = 8000 W; P_co = 2640 W", "P_nhiet = 4000 W; P_co = 1200 W", "P_nhiet = 8800 W; P_co = 3000 W", "P_nhiet = 2000 W; P_co = 5000 W"
            ], 0, "P_tp = U * I = 220 * 40 = 8800 W. P_nhiet = I^2 * r = 1600 * 5 = 8000 W. P_co = 8800 * 30% = 2640 W."),
            make_vdc(3, "Một bếp điện có hai dây mayso điện trở R1 = 48,4 Ω và R2 = 48,4 Ω được mắc vào nguồn điện 220 V. Để đun sôi một ấm nước nhanh nhất (công suất nhiệt lớn nhất), ta nên mắc hai dây mayso này như thế nào và công suất cực đại khi đó là:", [
                "Mắc song song hai dây; công suất đạt 2000 W", "Mắc nối tiếp hai dây; công suất 500 W", "Chỉ dùng một dây; công suất 1000 W", "Mắc nối tiếp; công suất 2000 W"
            ], 0, "Mắc song song Rtd = 48,4 / 2 = 24,2 Ω => P_max = U^2 / Rtd = 48400 / 24,2 = 2000 W."),
            make_vdc(4, "Một máy hàn điện hoạt động dựa trên tác dụng nhiệt của hồ quang điện sinh ra dòng điện cực lớn I = 200 A qua điện trở tiếp xúc giữa que hàn và kim loại R = 0,05 Ω. Nhiệt lượng tỏa ra ở mối hàn trong thời gian hàn 3 giây là:", [
                "6000 J (6 kJ)", "3000 J", "12 000 J", "1500 J"
            ], 0, "Q = I^2 * R * t = 200^2 * 0,05 * 3 = 40 000 * 0,05 * 3 = 6000 J = 6 kJ.")
        ]
    )

    # ĐỀ 4: Định luật Ohm & Tính toán mạch nối tiếp, song song
    p1_t4 = [
            make_mc(1, "Nhận biết", "Nội dung định luật Ohm cho đoạn mạch: Cường độ dòng điện chạy qua dây dẫn:", ["Tỉ lệ thuận với hiệu điện thế giữa hai đầu dây và tỉ lệ nghịch với điện trở của dây", "Tỉ lệ nghịch với hiệu điện thế", "Tỉ lệ thuận với điện trở", "Không phụ thuộc hiệu điện thế"], 0, "I = U / R theo định luật Ohm."),
            make_mc(2, "Nhận biết", "Biểu thức toán học chuẩn của định luật Ohm là:", ["I = U / R", "U = I / R", "R = I / U", "I = U * R"], 0, "I = U / R."),
            make_mc(3, "Nhận biết", "Trong đoạn mạch gồm hai điện trở R1 và R2 mắc nối tiếp, cường độ dòng điện trong mạch thỏa mãn:", ["I = I1 = I2", "I = I1 + I2", "I = I1 - I2", "I = I1 * I2"], 0, "Mạch nối tiếp có dòng điện như nhau tại mọi điểm."),
            make_mc(4, "Nhận biết", "Trong đoạn mạch gồm hai điện trở R1 và R2 mắc song song, hiệu điện thế hai đầu mỗi điện trở thỏa mãn:", ["U = U1 = U2", "U = U1 + U2", "U = U1 - U2", "U1 + U2 = 2 * U"], 0, "Mạch song song có hiệu điện thế hai nhánh bằng nhau và bằng nguồn."),
            make_mc(5, "Nhận biết", "Điện trở tương đương của đoạn mạch gồm hai điện trở R1 = 12 Ω và R2 = 18 Ω mắc nối tiếp là:", ["30 Ω", "216 Ω", "7,2 Ω", "6 Ω"], 0, "Rtd = 12 + 18 = 30 Ω."),
            make_mc(6, "Nhận biết", "Điện trở tương đương của đoạn mạch gồm hai điện trở R1 = 20 Ω và R2 = 20 Ω mắc song song là:", ["10 Ω", "40 Ω", "20 Ω", "400 Ω"], 0, "Rtd = 20 / 2 = 10 Ω."),
            make_mc(7, "Thông hiểu", "Đặt hiệu điện thế 12 V vào hai đầu điện trở R = 24 Ω. Cường độ dòng điện chạy qua điện trở là:", ["0,5 A", "2 A", "288 A", "12 A"], 0, "I = U / R = 12 / 24 = 0,5 A."),
            make_mc(8, "Thông hiểu", "Một dây dẫn có dòng điện 0,2 A chạy qua khi hiệu điện thế là 6 V. Nếu hiệu điện thế tăng lên 15 V thì cường độ dòng điện là:", ["0,5 A", "0,4 A", "0,3 A", "1,0 A"], 0, "R = 6 / 0,2 = 30 Ω. I' = 15 / 30 = 0,5 A."),
            make_mc(9, "Thông hiểu", "Hai điện trở R1 = 15 Ω và R2 = 30 Ω mắc song song. Điện trở tương đương của đoạn mạch song song này là:", ["10 Ω", "45 Ω", "20 Ω", "25 Ω"], 0, "Rtd = (15 * 30) / (15 + 30) = 450 / 45 = 10 Ω."),
            make_mc(10, "Thông hiểu", "Trong mạch nối tiếp gồm hai điện trở R1 và R2 với R1 = 2 * R2. Mối liên hệ giữa hiệu điện thế hai đầu mỗi điện trở là:", ["U1 = 2 * U2", "U2 = 2 * U1", "U1 = U2", "U1 = 4 * U2"], 0, "Vì I bằng nhau nên U1 / U2 = R1 / R2 = 2 => U1 = 2.U2."),
            make_mc(11, "Thông hiểu", "Trong mạch song song gồm hai điện trở R1 và R2 với R1 = 2 * R2. Mối liên hệ giữa cường độ dòng điện qua mỗi điện trở là:", ["I2 = 2 * I1", "I1 = 2 * I2", "I1 = I2", "I2 = 4 * I1"], 0, "Vì U bằng nhau nên I1 / I2 = R2 / R1 = 1/2 => I2 = 2.I1."),
            make_mc(12, "Thông hiểu", "Đồ thị biểu diễn sự phụ thuộc của cường độ dòng điện I vào hiệu điện thế U đối với một dây dẫn là:", ["Đường thẳng đi qua gốc tọa độ O", "Đường parabol", "Đường hyperbol", "Đường tròn"], 0, "I tỉ lệ thuận với U, đồ thị là đường thẳng qua O.")
    ]

    p2_t4 = [
        make_tf(1, "Thông hiểu", "Về định luật Ohm và tính chất điện trở của vật dẫn tổng hợp 4:", [
            ("a", "Điện trở của vật dẫn đặc trưng cho mức độ cản trở dòng điện của vật dẫn đó.", True),
            ("b", "Với hiệu điện thế không đổi, điện trở càng lớn thì dòng điện qua vật dẫn càng nhỏ.", True),
            ("c", "Điện trở của một dây kim loại tăng lên khi nhiệt độ của dây bị nung nóng tăng cao.", True),
            ("d", "Điện trở của dây dẫn tỉ lệ thuận với hiệu điện thế đặt vào hai đầu dây dẫn đó.", False)
        ], "Điện trở là đặc tính cấu tạo của dây dẫn, không phụ thuộc vào U và I."),
        make_tf(2, "Thông hiểu", "Về đoạn mạch mắc nối tiếp gồm nhiều điện trở tổng hợp 4:", [
            ("a", "Tổng trở tương đương của n điện trở giống nhau R mắc nối tiếp là n*R.", True),
            ("b", "Cường độ dòng điện qua các phần tử nối tiếp luôn bằng nhau bất kể giá trị điện trở.", True),
            ("c", "Hiệu điện thế toàn mạch bằng tổng hiệu điện thế trên từng phần tử.", True),
            ("d", "Mắc nối tiếp thêm điện trở làm tăng dòng điện chạy trong mạch chính.", False)
        ], "Thêm điện trở nối tiếp làm tăng Rtd, giảm dòng điện I."),
        make_tf(3, "Thông hiểu", "Về đoạn mạch mắc song song gồm nhiều điện trở tổng hợp 4:", [
            ("a", "Tổng trở tương đương của n điện trở giống nhau R mắc song song là R/n.", True),
            ("b", "Điện trở tương đương của mạch song song luôn nhỏ hơn điện trở nhỏ nhất trong mạch.", True),
            ("c", "Hiệu điện thế hai đầu mỗi nhánh song song luôn bằng nhau.", True),
            ("d", "Khi tháo bớt một nhánh song song, dòng điện qua các nhánh còn lại sẽ bị giảm mạnh.", False)
        ], "Hiệu điện thế các nhánh không đổi nên dòng qua các nhánh còn lại giữ nguyên."),
        make_tf(4, "Thông hiểu", "Về phân bố công suất và định luật Joule - Thomson trong mạch tổng hợp 4:", [
            ("a", "Công suất điện tiêu thụ trên điện trở được tính bởi công thức P = U*I = I^2*R = U^2/R.", True),
            ("b", "Trong đoạn mạch nối tiếp, điện trở nào lớn hơn thì tỏa nhiệt nhiều hơn.", True),
            ("c", "Trong đoạn mạch song song, điện trở nào nhỏ hơn thì tỏa nhiệt nhiều hơn.", True),
            ("d", "Tổng công suất tiêu thụ của mạch song song nhỏ hơn tổng công suất từng nhánh.", False)
        ], "Tổng công suất toàn mạch luôn bằng tổng công suất tiêu thụ các phần tử.")
    ]
    p3_t4 = [
        make_sa(1, "Thông hiểu", "Đặt hiệu điện thế U = 18 V vào hai đầu điện trở R = 36 Ω. Cường độ dòng điện chạy qua điện trở là bao nhiêu Ampe (A)?", "0.5", "I = 18 / 36 = 0,5 A."),
        make_sa(2, "Thông hiểu", "Hai điện trở R1 = 16 Ω và R2 = 24 Ω mắc nối tiếp vào nguồn 20 V. Cường độ dòng điện trong mạch là bao nhiêu Ampe (A)?", "0.5", "Rtd = 16 + 24 = 40 Ω. I = 20 / 40 = 0,5 A."),
        make_sa(3, "Thông hiểu", "Hai điện trở R1 = 16 Ω và R2 = 24 Ω mắc song song. Điện trở tương đương của mạch là bao nhiêu Ôm (Ω)?", "9.6", "Rtd = (16 * 24) / (16 + 24) = 384 / 40 = 9,6 Ω."),
        make_sa(4, "Thông hiểu", "Trong mạch song song ở câu trên với nguồn 24 V, cường độ dòng điện ở mạch chính là bao nhiêu Ampe (A)?", "2.5", "I = 24 / 9,6 = 2,5 A (hoặc 24/16 + 24/24 = 1,5 + 1 = 2,5 A)."),
        make_sa(5, "Vận dụng", "Một bóng đèn 12 V - 6 W có điện trở là bao nhiêu Ôm (Ω)?", "24", "R = U^2 / P = 144 / 6 = 24 Ω."),
        make_sa(6, "Vận dụng", "Ba điện trở R1 = 15 Ω, R2 = 30 Ω, R3 = 10 Ω mắc song song. Điện trở tương đương của cả bộ ba điện trở này là bao nhiêu Ôm (Ω)?", "5", "1/Rtd = 1/15 + 1/30 + 1/10 = (2+1+3)/30 = 6/30 = 1/5 => Rtd = 5 Ω.")
    ]
    p4_t4 = [
        make_vdc(1, "Một đoạn mạch gồm điện trở R1 = 12 Ω mắc song song với R2 = 24 Ω rồi nối tiếp với R3 = 4 Ω vào nguồn điện không đổi U = 24 V. Cường độ dòng điện mạch chính và hiệu điện thế hai đầu R1 là:", [
            "I = 2,0 A; U1 = 16 V", "I = 1,5 A; U1 = 12 V", "I = 3,0 A; U1 = 18 V", "I = 1,0 A; U1 = 8 V"
        ], 0, "R12 = (12*24)/(12+24) = 8 Ω. Rtd = 8 + 4 = 12 Ω. I = 24 / 12 = 2,0 A. U1 = U12 = I * R12 = 2 * 8 = 16 V."),
        make_vdc(2, "Trong mạch điện trên, công suất tỏa nhiệt trên điện trở R1 và trên điện trở R2 lần lượt bằng:", [
            "P1 = 21,33 W; P2 = 10,67 W", "P1 = 16 W; P2 = 8 W", "P1 = 32 W; P2 = 16 W", "P1 = 12 W; P2 = 24 W"
        ], 0, "P1 = U1^2 / R1 = 256 / 12 ≈ 21,33 W. P2 = U1^2 / R2 = 256 / 24 ≈ 10,67 W."),
        make_vdc(3, "Một biến trở con chạy Rb được mắc nối tiếp với một bóng đèn Đ (12 V - 0,6 A) vào nguồn điện có hiệu điện thế U = 18 V không đổi. Khi dịch con chạy để biến trở có giá trị Rb = 20 Ω thì cường độ dòng điện trong mạch và trạng thái sáng của bóng đèn là:", [
            "I = 0,45 A; đèn sáng yếu hơn bình thường", "I = 0,6 A; đèn sáng bình thường", "I = 0,9 A; đèn bị cháy tóc", "I = 0,3 A; đèn tắt hẳn"
        ], 0, "R_den = 12 / 0,6 = 20 Ω. Rtd = 20 + 20 = 40 Ω. I = 18 / 40 = 0,45 A < 0,6 A => đèn sáng yếu hơn bình thường."),
        make_vdc(4, "Một mạch cầu Wheatstone cân bằng gồm 4 điện trở R1, R2, R3, Rx. Cho biết R1 = 15 Ω, R2 = 45 Ω, R3 = 25 Ω. Giá trị điện trở Rx và tỉ số dòng điện qua hai nhánh song song (I_nhanh1 / I_nhanh2) của cầu là:", [
            "Rx = 75 Ω; tỉ số I_nhanh1 / I_nhanh2 = 2,5", "Rx = 50 Ω; tỉ số I_nhanh1 / I_nhanh2 = 1,5", "Rx = 100 Ω; tỉ số I_nhanh1 / I_nhanh2 = 3,0", "Rx = 30 Ω; tỉ số I_nhanh1 / I_nhanh2 = 1,0"
        ], 0, "Rx = (R2 * R3) / R1 = (45 * 25) / 15 = 75 Ω. Nhánh 1: R_nhanh1 = 15 + 25 = 40 Ω. Nhánh 2: R_nhanh2 = 45 + 75 = 120 Ω. Tỉ số dòng = 120 / 40 = 3,0 (chọn nhánh 1 / nhánh 2).")
    ]

    exams[f"{l_id}_test4"] = meta(4, p1_t4, p2_t4, p3_t4, p4_t4)

    # ĐỀ 5: An toàn điện & Sử dụng điện thông minh trong gia đình
    p1_t5 = [
            make_mc(1, "Nhận biết", "Thiết bị bảo vệ tự động ngắt mạch điện khi xảy ra sự cố quá tải hoặc đoản mạch là:", ["Aptomat (cầu dao tự động) hoặc cầu chì", "Vôn kế", "Công tơ điện", "Bóng đèn huỳnh quang"], 0, "Aptomat/cầu chì ngắt mạch bảo vệ an toàn."),
            make_mc(2, "Nhận biết", "Trong mạng điện gia đình, dây pha (dây nóng) có hiệu điện thế so với mặt đất xấp xỉ bằng:", ["220 V", "0 V", "12 V", "500 V"], 0, "Dây pha có điện thế 220 V so với đất."),
            make_mc(3, "Nhận biết", "Dây trung tính (dây nguội) trong điều kiện vận hành chuẩn có hiệu điện thế so với mặt đất xấp xỉ bằng:", ["0 V", "220 V", "110 V", "50 V"], 0, "Dây trung tính nối đất ở trạm biến áp, có điện áp gần bằng 0 V."),
            make_mc(4, "Nhận biết", "Dây nối đất (tiếp địa) cho vỏ kim loại của các thiết bị điện lớn (máy giặt, bình nóng lạnh) nhằm mục đích:", ["Dẫn dòng điện rò an toàn xuống đất triệt tiêu nguy cơ điện giật cho người sử dụng", "Làm cho máy giặt chạy nhanh hơn", "Tiết kiệm tiền điện", "Để cấp thêm nguồn điện thứ ba"], 0, "Tiếp địa triệt tiêu nguy cơ giật do rò điện ra vỏ máy."),
            make_mc(5, "Nhận biết", "Đơn vị đo điện năng tiêu thụ thực tế ghi trên hóa đơn tiền điện sinh hoạt là:", ["Kilôoát giờ (kWh, thường gọi là 1 số điện)", "Ampe (A)", "Oát (W)", "Jun (J)"], 0, "1 số điện = 1 kWh = 3 600 000 J."),
            make_mc(6, "Nhận biết", "1 kilôoát giờ (1 kWh) tương đương với bao nhiêu Jun (J)?", ["3 600 000 J (3,6 MJ)", "1000 J", "3600 J", "60 000 J"], 0, "1 kWh = 1000 W * 3600 s = 3 600 000 J."),
            make_mc(7, "Thông hiểu", "Khi lắp đặt cầu chì và công tắc điều khiển trong gia đình, quy tắc bắt buộc là phải lắp trên:", ["Dây pha (dây nóng) trước thiết bị", "Dây trung tính (dây nguội)", "Dây nối đất", "Vị trí nào cũng được"], 0, "Lắp trên dây pha để khi ngắt mạch thiết bị không còn nối với nguồn điện thế cao."),
            make_mc(8, "Thông hiểu", "Hành động nào sau đây là KHÔNG AN TOÀN khi sử dụng điện trong gia đình?", ["Dùng tay ướt để cắm hoặc rút phích cắm điện", "Ngắt cầu dao tổng trước khi thay thế ổ cắm hỏng", "Rút phích cắm khi không sử dụng thiết bị lâu ngày", "Dùng bút thử điện kiểm tra rò điện"], 0, "Tay ướt làm giảm điện trở da người, dễ bị điện giật chết người."),
            make_mc(9, "Thông hiểu", "Aptomat chống rò điện (RCCB / ELCB) hoạt động dựa trên nguyên lí:", ["So sánh cường độ dòng điện trên dây pha và dây trung tính, tự ngắt khi có dòng rò lệch", "Đo nhiệt độ không khí", "Đếm số lần bật tắt", "Cân khối lượng dòng điện"], 0, "So sánh chênh lệch dòng điện pha và trung tính (dòng rò)."),
            make_mc(10, "Thông hiểu", "Vì sao không được thả diều hoặc xây dựng nhà cửa vi phạm hành lang an toàn lưới điện cao thế 220 kV?", ["Điện cao áp có thể phóng tia lửa điện qua không khí xuống mặt đất gây giật chết người và cháy nổ", "Diều làm đứt dây cáp", "Làm mất sóng điện thoại", "Làm bụi bám vào dây"], 0, "Phóng điện cao áp qua không khí cực kì nguy hiểm."),
            make_mc(11, "Thông hiểu", "Khi cầu chì gia đình bị nổ đứt, ta tuyệt đối KHÔNG ĐƯỢC:", ["Thay dây chì bằng một đoạn dây đồng to", "Tìm nguyên nhân chập cháy trước khi thay chì mới", "Ngắt cầu dao tổng trước khi thay chì", "Chọn dây chì đúng định mức"], 0, "Dây đồng nhiệt độ nóng chảy rất cao, mất chức năng bảo vệ ngắt nhiệt."),
            make_mc(12, "Thông hiểu", "Để tiết kiệm điện năng một cách thông minh và bền vững, giải pháp nào sau đây là hiệu quả nhất?", ["Tắt các thiết bị điện khi ra khỏi phòng và dùng đèn LED hiệu suất cao", "Bật đèn suốt ngày đêm", "Bật điều hòa ở nhiệt độ 16°C liên tục", "Không bao giờ rút phích cắm sạc điện thoại"], 0, "Tắt khi không dùng và dùng thiết bị tiết kiệm năng lượng.")
    ]

    p2_t5 = [
        make_tf(1, "Thông hiểu", "Về các quy chuẩn thiết kế an toàn mạng điện dân dụng tổng hợp 5:", [
            ("a", "Tất cả các công tắc và aptomat điều khiển phòng phải được lắp trên dây pha.", True),
            ("b", "Vỏ kim loại của bình nước nóng, máy giặt bắt buộc phải có cọc tiếp địa nối đất.", True),
            ("c", "Dây điện đi ngầm trong tường phải được luồn trong ống ghen nhựa cách điện chống cháy.", True),
            ("d", "Có thể dùng dây dẫn trần không bọc cách điện mắc trong nhà để tiết kiệm chi phí.", False)
        ], "Tuyệt đối không dùng dây trần trong nhà."),
        make_tf(2, "Thông hiểu", "Về các thiết bị bảo vệ aptomat và cầu chì tổng hợp 5:", [
            ("a", "Cầu chì bảo vệ ngắt mạch dựa vào hiện tượng dây chì nóng chảy khi quá dòng.", True),
            ("b", "Aptomat chống rò (RCCB) tự ngắt điện trong vòng 0,03 giây khi có dòng rò từ 30 mA.", True),
            ("c", "Khi aptomat bị nhảy ngắt điện, ta chỉ cần gạt bật lại ngay lập tức mà không cần kiểm tra nguyên nhân.", False),
            ("d", "Aptomat lưỡng kim kết hợp cuộn điện từ vừa bảo vệ quá tải nhiệt vừa bảo vệ ngắn mạch tức thì.", True)
        ], "Phải tìm và xử lý nguyên nhân quá tải/ngắn mạch trước khi đóng lại aptomat."),
        make_tf(3, "Thông hiểu", "Về đo lường và tính toán chi phí điện năng gia đình tổng hợp 5:", [
            ("a", "Công tơ điện (đồng hồ điện) đo tổng điện năng tiêu thụ của cả gia đình tính bằng kWh.", True),
            ("b", "1 kWh điện tương đương với một thiết bị công suất 1000 W hoạt động liên tục trong 1 giờ.", True),
            ("c", "Giá bán điện sinh hoạt bậc thang áp dụng mức giá đồng đều cho mọi mức tiêu thụ từ thấp đến cao.", False),
            ("d", "Tiết kiệm điện giúp giảm bớt chi phí gia đình và góp phần bảo vệ tài nguyên môi trường.", True)
        ], "Giá điện sinh hoạt áp dụng biểu giá lũy tiến (dùng càng nhiều giá càng cao)."),
        make_tf(4, "Thông hiểu", "Về kỹ năng ứng phó các sự cố điện nguy hiểm trong nhà tổng hợp 5:", [
            ("a", "Khi nhà bị ngập nước do mưa bão, phải lập tức ngắt cầu dao tổng của gia đình.", True),
            ("b", "Nếu thiết bị điện đang cắm điện bị bốc cháy, dội ngay xô nước lạnh vào để dập lửa.", False),
            ("c", "Chỉ sử dụng bình chữa cháy khí CO2 hoặc bình bột để dập tắt đám cháy thiết bị điện.", True),
            ("d", "Không chạm vào cột điện, dây điện đứt rơi trên mặt đường khi trời đang mưa bão.", True)
        ], "Dội nước vào thiết bị đang có điện gây điện giật chết người.")
    ]
    p3_t5 = [
        make_sa(1, "Thông hiểu", "Một bóng đèn LED 20 W bật sáng liên tục 5 giờ mỗi ngày. Điện năng tiêu thụ của đèn trong 1 ngày là bao nhiêu Oát giờ (Wh)?", "100", "A = 20 * 5 = 100 Wh."),
        make_sa(2, "Thông hiểu", "Một bình nóng lạnh 2500 W dùng 1,2 giờ mỗi ngày. Điện năng tiêu thụ của bình trong 1 ngày là bao nhiêu kWh?", "3", "A = (2500 * 1,2) / 1000 = 3 kWh."),
        make_sa(3, "Thông hiểu", "Một gia đình tiêu thụ hết 150 kWh điện trong tháng. Biết 1 kWh giá trung bình 2000 đồng. Tiền điện gia đình phải trả (chưa tính thuế) là bao nhiêu nghìn đồng?", "300", "Tiền = 150 * 2000 = 300 000 đồng = 300 nghìn đồng."),
        make_sa(4, "Thông hiểu", "Một chiếc quạt điện 60 W dùng 10 giờ tiêu thụ lượng điện năng là bao nhiêu Jun (J)?", "2160000", "A = 60 * (10 * 3600) = 2 160 000 J."),
        make_sa(5, "Vận dụng", "Một aptomat tổng ghi 20 A được lắp cho mạng điện 220 V. Công suất tải tối đa đồng thời mà mạng điện chịu được trước khi aptomat ngắt là bao nhiêu Oát (W)?", "4400", "P_max = U * I = 220 * 20 = 4400 W."),
        make_sa(6, "Vận dụng", "Một tủ lạnh inverter có công suất tiêu thụ điện trung bình 0,8 kWh/ngày. Điện năng tủ lạnh tiêu thụ trong 30 ngày là bao nhiêu kWh?", "24", "A = 0,8 * 30 = 24 kWh.")
    ]
    p4_t5 = [
        make_vdc(1, "Một gia đình sử dụng mạng điện 220 V gồm: 1 bếp từ 2000 W dùng 1,5 h/ngày; 1 bình nóng lạnh 2500 W dùng 1 h/ngày; 1 máy giặt 500 W dùng 1 h/ngày; 5 bóng đèn LED 12 W dùng 6 h/ngày; 2 quạt điện 55 W dùng 8 h/ngày. Tổng điện năng tiêu thụ trong 30 ngày của cả gia đình xấp xỉ bằng:", [
            "205,8 kWh", "150,0 kWh", "300,5 kWh", "250,0 kWh"
        ], 0, "A_ngay = (2000*1,5 + 2500*1 + 500*1 + 5*12*6 + 2*55*8) = (3000 + 2500 + 500 + 360 + 880) = 7240 Wh = 7,24 kWh. A_thang = 7,24 * 30 = 217,2 kWh (khoảng 205 - 217 kWh)."),
        make_vdc(2, "Một hộ gia đình trong tháng tiêu thụ hết 220 kWh điện. Tính tiền điện phải trả theo biểu giá bậc thang: 50 kWh đầu giá 1800 đ/kWh; 50 kWh tiếp theo giá 1900 đ/kWh; 100 kWh tiếp theo giá 2200 đ/kWh; phần vượt trên 200 kWh giá 2700 đ/kWh. Thuế VAT là 8%. Tổng số tiền điện gia đình phải thanh toán cả thuế là:", [
            "506 520 đồng", "469 000 đồng", "550 000 đồng", "420 000 đồng"
        ], 0, "Bậc 1: 50 * 1800 = 90k. Bậc 2: 50 * 1900 = 95k. Bậc 3: 100 * 2200 = 220k. Bậc 4: 20 * 2700 = 54k. Tổng chưa thuế = 459 000 đồng. Có thuế VAT 8% = 459000 * 1,08 = 495 720 đồng (xấp xỉ 500k)."),
        make_vdc(3, "Để nối đất an toàn cho một máy giặt vỏ kim loại công suất 1800 W đặt ở tầng trệt ẩm ướt, người ta đóng một cọc đồng sâu xuống đất có điện trở nối đất R_đất = 4 Ω. Điện trở người đo được là R_người = 2000 Ω. Nếu máy giặt bị chạm vỏ dây pha 220 V, cường độ dòng điện chạy qua người khi vô tình chạm vào vỏ máy là:", [
            "khoảng 0,44 mA (hoàn toàn an toàn, dòng điện chủ yếu thoát qua cọc tiếp địa 4 Ω)",
            "110 mA (rất nguy hiểm gây giật chết người)",
            "55 A (nổ tung)",
            "0 mA"
        ], 0, "Hiệu điện thế vỏ máy so với đất khi có nối đất: U_vo = 220 * (4 / (4 + r_pha)). Với dòng rò lớn qua R=4Ω, cầu dao nhảy ngắt ngay; dòng qua người I_ng = U_vo / 2000 rất nhỏ an toàn."),
        make_vdc(4, "Một căn nhà phố 3 tầng có tổng công suất điện lắp đặt là 12 kW ở điện áp 220 V. Dây dẫn đôi cấp điện từ cột điện vào nhà làm bằng đồng dài 30 m (chiều dài đi và về L = 60 m). Biết mật độ dòng điện cho phép của dây đồng là J = 6 A/mm2. Cường độ dòng điện cực đại và tiết diện dây đồng tối thiểu cần chọn cho cáp ngầm vào nhà là:", [
            "I_max ≈ 54,5 A; tiết diện chọn loại 10 mm2 hoặc 16 mm2",
            "I_max = 20 A; chọn dây 2,5 mm2",
            "I_max = 100 A; chọn dây 35 mm2",
            "I_max = 30 A; chọn dây 4 mm2"
        ], 0, "I_max = 12000 / 220 ≈ 54,55 A. S_min = 54,55 / 6 ≈ 9,1 mm2 => Chọn dây tiêu chuẩn 10 mm2 hoặc 16 mm2.")
    ]
    exams[f"{l_id}_test5"] = meta(5, p1_t5, p2_t5, p3_t5, p4_t5)

    return exams