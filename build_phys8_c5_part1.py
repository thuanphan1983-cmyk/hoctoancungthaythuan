# -*- coding: utf-8 -*-
"""
CHƯƠNG V - PHẦN 1 (9 ĐỀ THI ĐỘC LẬP 100%):
- phys8_c5_b20: Bài 20: Hiện tượng nhiễm điện do cọ xát (3 đề)
- phys8_c5_b21: Bài 21: Dòng điện, nguồn điện (3 đề)
- phys8_c5_b22: Bài 22: Mạch điện đơn giản (3 đề)
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

def get_c5_part1_exams():
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
    # BÀI 20: HIỆN TƯỢNG NHIỄM ĐIỆN DO CỌ XÁT (3 ĐỀ)
    # =========================================================================
    l20_id = "phys8_c5_b20"
    l20_name = "Bài 20: Hiện tượng nhiễm điện do cọ xát"

    # --- B20 ĐỀ 1: Hiện tượng nhiễm điện do cọ xát ---
    exams[f"{l20_id}_test1"] = meta(l20_id, l20_name, 1,
        [
            make_mc(1, "Nhận biết", "Vật bị nhiễm điện (mang điện tích) có khả năng:", ["Hút các vật nhẹ khác hoặc làm sáng bóng đèn bút thử điện", "Đẩy tất cả các vật khác", "Làm thay đổi khối lượng vật khác", "Làm nóng chảy kim loại"], 0, "Vật nhiễm điện có khả năng hút các vật nhẹ."),
            make_mc(2, "Nhận biết", "Có thể làm nhiễm điện cho một thước nhựa bằng cách:", ["Cọ xát thước nhựa vào mảnh vải khô hoặc len dạ", "Nhúng thước nhựa vào nước ấm", "Hơ thước nhựa trên ngọn lửa", "Phơi thước nhựa ngoài nắng"], 0, "Cọ xát làm thước nhựa nhiễm điện."),
            make_mc(3, "Nhận biết", "Khi cọ xát thanh thủy tinh vào lụa, thanh thủy tinh sẽ:", ["Nhiễm điện dương", "Nhiễm điện âm", "Không nhiễm điện", "Bị nóng chảy"], 0, "Quy ước: thanh thủy tinh cọ vào lụa nhiễm điện dương (+)."),
            make_mc(4, "Nhận biết", "Khi cọ xát thanh nhựa sẫm màu vào mảnh dạ len, thanh nhựa sẽ:", ["Nhiễm điện âm", "Nhiễm điện dương", "Không nhiễm điện", "Mang cả hai điện tích"], 0, "Quy ước: thanh nhựa sẫm màu cọ vào dạ nhiễm điện âm (-)."),
            make_mc(5, "Nhận biết", "Các vật mang điện tích cùng loại (cùng dấu) khi đặt gần nhau sẽ:", ["Đẩy nhau", "Hút nhau", "Không tương tác", "Vừa hút vừa đẩy"], 0, "Cùng dấu đẩy nhau, khác dấu hút nhau."),
            make_mc(6, "Nhận biết", "Các vật mang điện tích khác loại (trái dấu) khi đặt gần nhau sẽ:", ["Hút nhau", "Đẩy nhau", "Không tương tác", "Phát sáng"], 0, "Khác dấu hút nhau."),
            make_mc(7, "Thông hiểu", "Vào mùa đông khô hanh, khi chải tóc bằng lược nhựa, ta thấy nhiều sợi tóc bị lược nhựa hút dựng đứng lên vì:", ["Lược nhựa cọ xát với tóc bị nhiễm điện nên hút các sợi tóc", "Lược có keo dính", "Tóc bị ẩm ướt", "Từ trường của đầu"], 0, "Lược nhựa nhiễm điện do cọ xát với tóc nên hút tóc."),
            make_mc(8, "Thông hiểu", "Treo hai quả cầu nhẹ A và B bằng hai sợi chỉ mảnh. Khi đưa chúng lại gần nhau thấy chúng hút nhau. Kết luận đúng là:", ["A và B nhiễm điện trái dấu hoặc một quả nhiễm điện còn quả kia không nhiễm điện", "A và B chắc chắn cùng dấu", "Cả hai không nhiễm điện", "A mang điện tích dương"], 0, "Vật nhiễm điện hút vật trái dấu và hút cả vật nhẹ trung hòa điện."),
            make_mc(9, "Thông hiểu", "Nguyên nhân sâu xa làm một vật bị nhiễm điện khi cọ xát là do:", ["Các hạt electron dịch chuyển từ vật này sang vật khác", "Các hạt proton dịch chuyển", "Hạt nhân bị vỡ", "Phân tử bị phân hủy"], 0, "Thuyết electron: do sự chuyển dịch của các electron."),
            make_mc(10, "Thông hiểu", "Một nguyên tử trung hòa về điện nếu bị mất bớt electron sẽ trở thành:", ["Hạt mang điện tích dương (ion dương)", "Hạt mang điện tích âm", "Hạt trung hòa", "Neutron"], 0, "Mất bớt electron âm thì số proton dương nhiều hơn => mang điện tích dương."),
            make_mc(11, "Thông hiểu", "Một vật trung hòa về điện nhận thêm một số electron thì vật đó sẽ:", ["Nhiễm điện âm", "Nhiễm điện dương", "Không nhiễm điện", "Trở thành chất dẫn điện"], 0, "Nhận thêm electron âm => nhiễm điện âm."),
            make_mc(12, "Thông hiểu", "Cánh quạt điện trong gia đình sau một thời gian quay thường bị bám đầy bụi ở mép cánh quạt vì:", ["Khi quay, cánh quạt cọ xát với không khí bị nhiễm điện nên hút các hạt bụi trong không khí", "Gió thổi bụi vào bám", "Cánh quạt bị ẩm", "Cánh quạt có dầu mỡ"], 0, "Cọ xát với không khí làm cánh quạt nhiễm điện hút bụi.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về hiện tượng nhiễm điện do cọ xát:", [
                ("a", "Nhiều vật sau khi cọ xát có khả năng hút các vật nhỏ, nhẹ.", True),
                ("b", "Trong tự nhiên có hai loại điện tích là điện tích dương (+) và điện tích âm (-).", True),
                ("c", "Hai vật cùng nhiễm điện âm khi đặt gần nhau sẽ hút nhau.", False),
                ("d", "Hai vật nhiễm điện trái dấu khi đặt gần nhau sẽ hút nhau.", True)
            ], "Cùng dấu thì đẩy nhau, trái dấu hút nhau."),
            make_tf(2, "Thông hiểu", "Bản chất vi mô của sự nhiễm điện theo thuyết electron:", [
                ("a", "Electron là hạt mang điện tích âm có thể dịch chuyển từ nguyên tử này sang nguyên tử khác.", True),
                ("b", "Vật nhiễm điện dương là vật đã nhận thêm các hạt proton từ vật khác.", False),
                ("c", "Vật nhiễm điện âm là vật đã nhận thêm các electron.", True),
                ("d", "Tổng đại số điện tích trong một hệ cô lập luôn được bảo toàn.", True)
            ], "Proton nằm chặt trong hạt nhân không dịch chuyển; vật nhiễm điện dương do mất bớt electron."),
            make_tf(3, "Vận dụng", "Cọ xát một thanh thủy tinh vào một mảnh lụa khô rồi đưa lại gần một quả cầu bấc nhẹ treo bằng sợi chỉ:", [
                ("a", "Thanh thủy tinh bị mất electron sang mảnh lụa nên nhiễm điện dương.", True),
                ("b", "Mảnh lụa nhận thêm electron nên bị nhiễm điện âm.", True),
                ("c", "Thanh thủy tinh nhiễm điện dương sẽ hút quả cầu bấc trung hòa về điện.", True),
                ("d", "Nếu quả cầu bấc chạm vào thanh thủy tinh rồi bị bật ra thì quả cầu bấc nhiễm điện trái dấu với thanh thủy tinh.", False)
            ], "Sau khi chạm, quả cầu nhận cùng dấu điện tích nên bị đẩy bật ra."),
            make_tf(4, "Vận dụng", "Xét hiện tượng tĩnh điện trong thực tế đời sống hàng ngày:", [
                ("a", "Vào mùa khô hanh, khi cởi áo len chui đầu thường nghe tiếng lách tách nhỏ và thấy tia sáng li ti.", True),
                ("b", "Màn hình tivi sau khi tắt thường hút nhiều bụi bẩn do bị nhiễm điện tĩnh.", True),
                ("c", "Khi đổ xăng cho xe bồn, xích sắt thả kéo lê trên mặt đường để truyền điện tích ma sát an toàn xuống đất.", True),
                ("d", "Hiện tượng nhiễm điện do cọ xát chỉ xảy ra giữa hai kim loại với nhau.", False)
            ], "Kim loại dẫn điện tốt nên điện tích dễ truyền đi, cọ xát thường quan sát rõ ở vật cách điện.")
        ],
        [
            make_sa(1, "Thông hiểu", "Có mấy loại điện tích tồn tại trong tự nhiên?", "2", "Có 2 loại điện tích: dương và âm."),
            make_sa(2, "Thông hiểu", "Hạt electron trong nguyên tử mang điện tích dấu gì? (Ghi chữ 'âm' hoặc 'dương')", "âm", "Electron mang điện tích âm (-)."),
            make_sa(3, "Vận dụng", "Hai quả cầu tích điện cùng mang điện tích +2 μC và +3 μC đặt gần nhau sẽ tương tác với nhau bằng lực hút hay lực đẩy? (Ghi 'đẩy' hoặc 'hút')", "đẩy", "Cùng dấu dương nên đẩy nhau."),
            make_sa(4, "Vận dụng", "Một vật trung hòa về điện bị mất đi 10^12 electron. Vật đó sẽ mang điện tích âm hay dương? (Ghi 'dương' hoặc 'âm')", "dương", "Mất electron mang điện tích dương."),
            make_sa(5, "Vận dụng cao", "Biết điện tích của một electron là -1,6 × 10^-19 C. Một quả cầu nhiễm điện âm có độ lớn điện tích là -3,2 × 10^-16 C. Số electron mà quả cầu đã nhận thêm là bao nhiêu hạt?", "2000", "N = 3,2 × 10^-16 / (1,6 × 10^-19) = 2 000 hạt."),
            make_sa(6, "Vận dụng cao", "Cọ xát thước nhựa vào mảnh dạ thấy thước nhựa nhận thêm 5 × 10^10 electron. Mảnh dạ bị mất đi bao nhiêu electron?", "50000000000", "Theo định luật bảo toàn điện tích, số e mất bằng số e nhận: 5 × 10^10 hạt.")
        ],
        [
            make_vdc(1, "Một xe bồn chở xăng dầu khi chạy trên đường dài thường có một sợi xích sắt một đầu gắn vào khung xe, đầu kia thả kéo lê tiếp xúc liên tục với mặt đường bê tông. Tác dụng an toàn cốt lõi của sợi xích sắt này là:", ["Dẫn toàn bộ các điện tích tĩnh sinh ra do xăng dầu sóng sánh cọ xát với thành bồn truyền an toàn xuống đất, triệt tiêu nguy cơ phóng tia lửa điện gây nổ", "Để báo hiệu cho xe sau", "Để giảm tốc độ xe bồn", "Để đo độ mòn mặt đường"], 0, "Dẫn điện tích tĩnh xuống đất chống cháy nổ xe bồn."),
            make_vdc(2, "Trong các nhà máy dệt sợi bông hoặc sản xuất giấy, người ta luôn phải duy trì độ ẩm không khí trong phân xưởng ở mức cao (trên 70%) hoặc lắp các thanh khử tĩnh điện nhằm mục đích:", ["Độ ẩm cao giúp bề mặt vật liệu dẫn điện tốt, nhanh chóng truyền triệt tiêu các điện tích ma sát sinh ra, tránh sợi vải hút dính vào máy móc hoặc phát tia lửa điện cháy bụi sợi", "Để công nhân mát mẻ", "Để sợi vải nặng hơn bán được nhiều tiền", "Để máy chạy êm hơn"], 0, "Hạn chế tích điện tĩnh gây rối sợi và chống cháy nổ bụi dệt."),
            make_vdc(3, "Công nghệ sơn tĩnh điện ô tô và thiết bị gia dụng hoạt động dựa trên nguyên lí: các hạt sơn phun ra được tích điện âm (-), còn vỏ thân xe ô tô được nối cực dương (+). Ưu điểm vượt trội của phương pháp này là:", ["Các hạt sơn bị vỏ xe hút mạnh bám đều khắp mọi khe kẽ ngóc ngách, các hạt sơn cùng dấu tự đẩy nhau tản đều mịn và không bị bay lãng phí ra môi trường", "Sơn nhanh khô bằng nhiệt", "Sơn tự đổi màu", "Sơn không bị trầy xước bao giờ"], 0, "Hút tĩnh điện giúp sơn bám đều, tiết kiệm và mịn đẹp."),
            make_vdc(4, "Một người đưa một thanh thủy tinh nhiễm điện dương lại gần một dòng nước nhỏ chảy êm từ vòi nước xuống chậu. Hiện tượng quan sát được là dòng nước bị uốn cong lệch về phía thanh thủy tinh. Giải thích hiện tượng này là do:", ["Phân tử nước bị phân cực tĩnh điện, đầu âm của phân tử nước hướng về thanh thủy tinh nhiễm điện dương nên bị hút về phía thanh thủy tinh", "Nước dẫn nhiệt làm nóng thanh thủy tinh", "Thanh thủy tinh hút trọng lực dòng nước", "Áp suất không khí đẩy dòng nước"], 0, "Phân cực tĩnh điện của phân tử nước lưỡng cực bị hút về vật nhiễm điện.")
        ]
    )

    # --- B20 ĐỀ 2: Hai loại điện tích & Thuyết electron ---
    exams[f"{l20_id}_test2"] = meta(l20_id, l20_name, 2,
        [
            make_mc(1, "Nhận biết", "Trong tự nhiên chỉ tồn tại hai loại điện tích là:", ["Điện tích dương (+) và điện tích âm (-)", "Điện tích Bắc và điện tích Nam", "Điện tích nóng và điện tích lạnh", "Điện tích đẩy và hút"], 0, "Điện tích dương và âm."),
            make_mc(2, "Nhận biết", "Quy ước thanh thủy tinh cọ xát vào mảnh lụa mang điện tích gì?", ["Điện tích dương", "Điện tích âm", "Điện tích trung hòa", "Điện tích từ"], 0, "Thanh thủy tinh mang điện tích dương (+)."),
            make_mc(3, "Nhận biết", "Hạt mang điện tích dương trong nguyên tử là:", ["Proton", "Electron", "Neutron", "Positron"], 0, "Proton mang điện dương +1,6 × 10^-19 C."),
            make_mc(4, "Nhận biết", "Hạt mang điện tích âm quay xung quanh hạt nhân nguyên tử là:", ["Electron", "Proton", "Neutron", "Hạt nhân"], 0, "Electron mang điện âm."),
            make_mc(5, "Nhận biết", "Một nguyên tử ở trạng thái bình thường trung hòa về điện vì:", ["Tổng điện tích dương của các proton bằng tổng độ lớn điện tích âm của các electron", "Hạt nhân không mang điện", "Electron không mang điện", "Số neutron gấp đôi proton"], 0, "Số proton bằng số electron."),
            make_mc(6, "Nhận biết", "Vật nhiễm điện dương khi vật đó:", ["Bị mất bớt electron", "Nhận thêm proton", "Nhận thêm neutron", "Mất bớt hạt nhân"], 0, "Mất bớt electron."),
            make_mc(7, "Thông hiểu", "Vật nhiễm điện âm khi vật đó:", ["Nhận thêm electron từ vật khác", "Mất bớt electron", "Mất bớt proton", "Nhận thêm proton"], 0, "Nhận thêm electron mang điện âm."),
            make_mc(8, "Thông hiểu", "Đưa quả cầu kim loại A nhiễm điện âm lại gần quả cầu kim loại B nhiễm điện âm thì chúng sẽ:", ["Đẩy nhau", "Hút nhau", "Không tương tác", "Phát ra tia lửa"], 0, "Cùng dấu âm nên đẩy nhau."),
            make_mc(9, "Thông hiểu", "Đưa thanh nhựa nhiễm điện âm lại gần thanh thủy tinh nhiễm điện dương thì chúng sẽ:", ["Hút nhau", "Đẩy nhau", "Không có lực tác dụng", "Đổi dấu điện tích"], 0, "Trái dấu nên hút nhau."),
            make_mc(10, "Thông hiểu", "Vì sao khi lau chùi mặt kính gương soi bằng khăn vải khô, ta thấy các sợi bông vải bám dính nhiều hơn trên mặt kính?", ["Khăn vải cọ xát làm mặt kính bị nhiễm điện nên hút các sợi bông vải nhẹ", "Kính có keo dính", "Khăn vải ẩm", "Không khí thổi bụi vào"], 0, "Kính nhiễm điện do cọ xát hút sợi bông."),
            make_mc(11, "Thông hiểu", "Khi hai vật trung hòa cọ xát vào nhau thì:", ["Một vật nhiễm điện dương còn vật kia nhiễm điện âm với độ lớn điện tích bằng nhau", "Cả hai cùng nhiễm điện dương", "Cả hai cùng nhiễm điện âm", "Cả hai không đổi"], 0, "Electron chuyển từ vật này sang vật kia."),
            make_mc(12, "Thông hiểu", "Đưa một vật nhiễm điện lại gần một con lắc bấc nhẹ không nhiễm điện thì hiện tượng xảy ra là:", ["Vật nhiễm điện sẽ hút con lắc bấc", "Vật nhiễm điện sẽ đẩy con lắc bấc", "Không có hiện tượng gì", "Con lắc bấc phát sáng"], 0, "Vật nhiễm điện hút các vật nhẹ trung hòa.")
        ],
        [
            make_tf(1, "Thông hiểu", "Tương tác giữa các vật mang điện tích:", [
                ("a", "Hai vật mang điện cùng dấu thì đẩy nhau.", True),
                ("b", "Hai vật mang điện trái dấu thì hút nhau.", True),
                ("c", "Vật nhiễm điện có thể hút vật nhẹ không mang điện.", True),
                ("d", "Hai vật không mang điện khi đặt gần nhau sẽ đẩy nhau.", False)
            ], "Hai vật không mang điện không có lực tương tác tĩnh điện."),
            make_tf(2, "Thông hiểu", "Cấu tạo nguyên tử và giải thích hiện tượng nhiễm điện:", [
                ("a", "Nguyên tử gồm hạt nhân mang điện dương ở tâm và lớp vỏ electron mang điện âm xung quanh.", True),
                ("b", "Khối lượng của electron rất nhỏ so với proton và electron có thể bứt ra khỏi nguyên tử.", True),
                ("c", "Khi vật nhận thêm electron thì vật nhiễm điện dương.", False),
                ("d", "Cọ xát là quá trình tạo ra thêm các hạt mang điện tích mới hoàn toàn từ hư không.", False)
            ], "Điện tích không tự sinh ra, cọ xát chỉ chuyển dời electron từ vật này sang vật khác."),
            make_tf(3, "Vận dụng", "Có ba quả cầu kim loại nhỏ tích điện M, N, P treo bằng chỉ cách điện. Thấy M đẩy N, N hút P. Biết P mang điện tích âm (-):", [
                ("a", "Quả cầu P mang điện tích âm.", True),
                ("b", "Quả cầu N mang điện tích dương do bị P hút.", True),
                ("c", "Quả cầu M mang điện tích dương do đẩy N.", True),
                ("d", "Quả cầu M và P sẽ đẩy nhau khi đưa lại gần.", False)
            ], "M dương, P âm nên M và P sẽ hút nhau."),
            make_tf(4, "Vận dụng", "Thí nghiệm với thước nhựa và mảnh len dạ khô:", [
                ("a", "Trước khi cọ xát, cả thước nhựa và mảnh len đều trung hòa về điện.", True),
                ("b", "Sau khi cọ xát, electron truyền từ mảnh len sang thước nhựa.", True),
                ("c", "Thước nhựa mang điện tích âm, mảnh len mang điện tích dương.", True),
                ("d", "Độ lớn điện tích âm của thước nhựa lớn hơn độ lớn điện tích dương của mảnh len.", False)
            ], "Độ lớn điện tích bằng nhau theo bảo toàn điện tích.")
        ],
        [
            make_sa(1, "Thông hiểu", "Hai quả cầu tích điện cùng mang điện tích âm đặt gần nhau sẽ hút hay đẩy nhau? (Ghi 'đẩy' hoặc 'hút')", "đẩy", "Cùng dấu đẩy nhau."),
            make_sa(2, "Thông hiểu", "Quả cầu A mang điện dương, quả cầu B mang điện âm. Chúng tương tác với nhau bằng lực gì? (Ghi 'hút' hoặc 'đẩy')", "hút", "Trái dấu hút nhau."),
            make_sa(3, "Vận dụng", "Thanh thủy tinh cọ vào lụa mất đi 2 × 10^11 electron. Mảnh lụa nhận thêm bao nhiêu electron?", "200000000000", "2 × 10^11 hạt electron."),
            make_sa(4, "Vận dụng", "Một vật có 1 000 hạt proton và 900 hạt electron. Vật này nhiễm điện dương hay âm? (Ghi 'dương' hoặc 'âm')", "dương", "Số proton nhiều hơn electron nên nhiễm điện dương."),
            make_sa(5, "Vận dụng cao", "Một quả cầu kim loại trung hòa được truyền thêm 6,25 × 10^18 electron (mỗi e mang -1,6 × 10^-19 C). Điện tích quả cầu nhận được là bao nhiêu Coulomb?", "-1", "q = 6,25 × 10^18 × (-1,6 × 10^-19) = -1 C."),
            make_sa(6, "Vận dụng cao", "Hai quả cầu kim loại giống nhau mang điện tích +4 μC và -2 μC cho tiếp xúc nhau rồi tách ra. Điện tích mỗi quả cầu sau tiếp xúc là bao nhiêu μC?", "1", "q' = (+4 - 2) / 2 = +1 μC.")
        ],
        [
            make_vdc(1, "Một người làm thí nghiệm dùng thanh nhựa nhiễm điện âm (-) đưa lại gần (không chạm) vào đầu A của một thanh nhôm trung hòa về điện đặt trên đế cách điện. Hiện tượng xảy ra tại hai đầu của thanh nhôm là:", ["Đầu A nhiễm điện dương (+) do hút electron đi xa, đầu B nhiễm điện âm (-) do electron dồn về (hiện tượng hưởng ứng tĩnh điện)", "Cả thanh nhôm bị nhiễm điện âm", "Cả thanh nhôm bị nhiễm điện dương", "Không có hiện tượng gì"], 0, "Hiện tượng nhiễm điện do hưởng ứng (cảm ứng tĩnh điện)."),
            make_vdc(2, "Tại sao các máy bay chở khách khi hạ cánh xuống đường băng sân bay thường có các chốt phóng điện tĩnh (sợi dây kim loại nhỏ nhọn) gắn ở mép sau cánh máy bay?", ["Để phóng các điện tích ma sát với không khí tích tụ trên vỏ máy bay vào không khí, tránh nguy cơ sốc điện và cháy nổ khi tra nạp nhiên liệu", "Để giảm sức cản không khí", "Để đo tốc độ gió", "Để trang trí máy bay"], 0, "Giải phóng tĩnh điện ma sát không khí an toàn."),
            make_vdc(3, "Thiết bị lọc bụi tĩnh điện trong các nhà máy nhiệt điện và xi măng hoạt động bằng cách tích điện âm cho các hạt bụi khói bay qua, sau đó các hạt bụi này bị hút bám dính chặt vào:", ["Các tấm điện cực thu gom mang điện tích dương (+)", "Các tấm màng lọc vải", "Ống khói bằng bê tông", "Quạt hút gió"], 0, "Điện cực dương hút giữ hạt bụi tích điện âm sạch khói thải."),
            make_vdc(4, "Một người mặc áo khoác len bước đi trên thảm trải sàn sợi tổng hợp trong phòng khách vào ngày đông hanh khô. Khi người đó đưa tay chạm vào nắm cửa bằng kim loại thì bị giật nhẹ một cái và nghe tiếng 'tách'. Cơ chế vật lí là:", ["Cơ thể người bị tích điện do ma sát với thảm và quần áo, khi chạm vào kim loại xảy ra sự phóng tia lửa điện phóng điện tích sang nắm cửa dẫn xuống đất", "Nắm cửa có điện lưới rò rỉ", "Kim loại bị nhiễm từ", "Cơ thể bị cảm lạnh"], 0, "Phóng điện tích tĩnh ma sát từ cơ thể sang kim loại dẫn điện.")
        ]
    )

    # --- B20 ĐỀ 3: Tĩnh điện trong đời sống & Chống sét ---
    exams[f"{l20_id}_test3"] = meta(l20_id, l20_name, 3,
        [
            make_mc(1, "Nhận biết", "Tia sét trong các cơn dông mưa bão thực chất là:", ["Hiện tượng phóng điện tia lửa điện khổng lồ giữa các đám mây tích điện trái dấu hoặc giữa đám mây và mặt đất", "Ngọn lửa đốt cháy không khí", "Ánh sáng phản chiếu từ Mặt Trời", "Dòng nước sôi rơi xuống"], 0, "Sự phóng điện tĩnh khổng lồ trong khí quyển."),
            make_mc(2, "Nhận biết", "Cột thu lôi (cột chống sét) do nhà bác học nào phát minh?", ["Benjamin Franklin", "Thomas Edison", "Isaac Newton", "Albert Einstein"], 0, "Benjamin Franklin phát minh năm 1752."),
            make_mc(3, "Nhận biết", "Cột thu lôi thường được gắn ở vị trí nào của công trình xây dựng?", ["Nơi cao nhất trên đỉnh mái nhà, tòa tháp", "Dưới tầng hầm", "Ở chính giữa phòng khách", "Quanh tường rào"], 0, "Gắn ở nơi cao nhất để đón sét."),
            make_mc(4, "Nhận biết", "Cột thu lôi được nối với mặt đất bằng:", ["Dây kim loại dẫn điện tốt (dây đồng dày) chôn sâu vào lòng đất ẩm", "Dây nhựa cách điện", "Dây cao su", "Sợi dây dù"], 0, "Dây kim loại dẫn điện tốt nối cọc đất."),
            make_mc(5, "Nhận biết", "Khi trời mưa dông có sấm sét, vị trí nào sau đây là NGUY HIỂM NHẤT tuyệt đối không được trú ẩn?", ["Đứng dưới gốc cây to trơ trọi giữa đồng trống", "Ở trong nhà kiên cố đóng kín cửa", "Ở trong xe ô tô đóng kín cửa", "Ở trong nhà có lắp cột thu lôi"], 0, "Cây to trơ trọi dễ bị sét đánh nhất."),
            make_mc(6, "Nhận biết", "Tại sao ô tô vỏ kim loại đóng kín cửa là nơi trú ẩn an toàn khi có sấm sét?", ["Vỏ kim loại của ô tô tạo thành lồng Faraday che chắn và dẫn dòng điện sét truyền thẳng xuống đất an toàn quanh cabin", "Bánh xe cao su cách điện hoàn toàn với sét", "Ô tô chạy nhanh hơn sét", "Ô tô không hút sét"], 0, "Hiệu ứng lồng Faraday vỏ kim loại dẫn dòng sét an toàn."),
            make_mc(7, "Thông hiểu", "Sự tích điện khổng lồ trong các đám mây dông hình thành chủ yếu do:", ["Sự cọ xát mạnh mẽ giữa các giọt nước, tinh thể băng trong luồng không khí đối lưu thăng hoa", "Nhiệt độ mây quá nóng", "Mây hút điện từ Mặt Trời", "Gió biển thổi vào"], 0, "Ma sát giữa các hạt nước đá trong dòng đối lưu."),
            make_mc(8, "Thông hiểu", "Tiếng sấm rền vang sau tia chớp là do:", ["Tia sét làm không khí quanh nó nóng lên đột ngột tới hàng vạn độ giãn nở nổ tung tạo ra sóng âm thanh truyền đi", "Mây va chạm vào nhau vỡ ra", "Gió thổi mạnh vào núi", "Nước mưa sôi ùng ục"], 0, "Không khí bị ion hóa giãn nở nhiệt nổ tung sinh sóng âm."),
            make_mc(9, "Thông hiểu", "Khi thấy tia chớp lóe lên, sau đó 3 giây mới nghe thấy tiếng sấm. Biết vận tốc âm thanh trong không khí là 340 m/s. Nơi sét đánh cách ta khoảng:", ["1 020 m (khoảng 1 km)", "340 m", "680 m", "3 000 m"], 0, "s = v × t = 340 × 3 = 1 020 m."),
            make_mc(10, "Thông hiểu", "Đầu mũi nhọn của cột thu lôi có tác dụng:", ["Tập trung mật độ điện tích cực lớn làm ion hóa không khí phóng điện êm dịu dần triệt tiêu điện tích đám mây hoặc dẫn dòng sét", "Để hứng nước mưa", "Để trang trí tòa nhà", "Để cản gió bão"], 0, "Hiệu ứng mũi nhọn phóng điện ion hóa."),
            make_mc(11, "Thông hiểu", "Khi đang ở ngoài đồng trống mà gặp cơn dông sấm sét, tư thế an toàn nhất là:", ["Ngồi xổm co ro, chụm hai chân sát nhau, cúi đầu gục xuống đầu gối", "Nằm sấp áp sát người xuống đất", "Đứng thẳng giương ô kim loại", "Chạy thật nhanh dưới mưa"], 0, "Ngồi xổm chụm chân giảm diện tích và giảm điện áp bước."),
            make_mc(12, "Thông hiểu", "Tại sao các trạm xăng dầu luôn cấm sử dụng điện thoại di động khi đang bơm xăng?", ["Sóng vô tuyến và vi mạch điện thoại có thể phát sinh tia lửa điện tĩnh nhỏ gây bắt lửa hơi xăng nổ buồng chứa", "Để khách tập trung trả tiền", "Điện thoại làm sai số đồng hồ bơm", "Sợ làm rơi điện thoại"], 0, "Phòng chống tĩnh điện và tia lửa kích nổ hơi xăng.")
        ],
        [
            make_tf(1, "Thông hiểu", "Nguyên lí bảo vệ của cột thu lôi chống sét:", [
                ("a", "Cột thu lôi có đầu kim loại nhọn đặt nhô cao trên mái công trình.", True),
                ("b", "Được nối với hệ thống cọc tiếp địa chôn sâu trong lòng đất bằng dây dẫn kim loại dày.", True),
                ("c", "Khi sét đánh, dòng điện cực lớn phóng qua cột thu lôi truyền thẳng xuống đất an toàn.", True),
                ("d", "Cột thu lôi làm bằng chất cách điện cao su để ngăn sét không đánh vào nhà.", False)
            ], "Cột thu lôi phải bằng kim loại dẫn điện cực tốt (đồng/thép mạ kẽm)."),
            make_tf(2, "Thông hiểu", "Các quy tắc an toàn khi gặp dông bão sấm sét:", [
                ("a", "Rút phích cắm các thiết bị điện tử đắt tiền khỏi ổ cắm điện gia đình.", True),
                ("b", "Không tắm vòi sen hoặc rửa bát khi có dông lớn vì đường ống nước kim loại có thể dẫn dòng sét lan truyền.", True),
                ("c", "Tuyệt đối không cầm que sắt, gậy golf hay giương ô có cán kim loại giữa bãi đất trống.", True),
                ("d", "Trú ẩn dưới bóng cây cao to giữa bãi đất trống là giải pháp an toàn tuyệt đối.", False)
            ], "Cây to giữa bãi trống là điểm sét đánh hàng đầu."),
            make_tf(3, "Vận dụng", "Tính khoảng cách từ người quan sát đến nơi sét đánh:", [
                ("a", "Ánh sáng chớp truyền đi với vận tốc gần 300 000 km/s nên ta thấy chớp gần như tức thì.", True),
                ("b", "Âm thanh tiếng sấm truyền trong không khí với vận tốc khoảng 340 m/s.", True),
                ("c", "Nếu thời gian từ lúc thấy chớp đến khi nghe sấm là 5 giây thì khoảng cách sét đánh là 1 700 m.", True),
                ("d", "Nếu thấy chớp và nghe sấm cùng một lúc thì khoảng cách sét đánh là rất xa trên 10 km.", False)
            ], "Cùng lúc chứng tỏ sét đánh ngay sát cạnh cực kỳ nguy hiểm."),
            make_tf(4, "Vận dụng", "Hiện tượng tĩnh điện trong máy photocopy và máy in laser văn phòng:", [
                ("a", "Trống in (drum) được tích điện tĩnh bề mặt bằng dây corona hoặc trục cao su tích điện.", True),
                ("b", "Tia laser chiếu vào trống làm triệt tiêu điện tích ở những chỗ không có chữ.", True),
                ("c", "Mực in dạng bột mịn mang điện tích trái dấu bị các vùng tích điện trên trống in hút dính vào.", True),
                ("d", "Máy in laser hoàn toàn không sử dụng bất kì nguyên lí tĩnh điện nào.", False)
            ], "Máy in laser và photocopy hoạt động hoàn toàn dựa trên công nghệ chụp ảnh tĩnh điện (xerography).")
        ],
        [
            make_sa(1, "Thông hiểu", "Vận tốc truyền âm thanh trong không khí xấp xỉ bằng bao nhiêu m/s?", "340", "Khoảng 340 m/s."),
            make_sa(2, "Thông hiểu", "Thấy tia sét lóe lên, 2 giây sau nghe thấy tiếng sấm. Khoảng cách đến nơi sét đánh là bao nhiêu mét?", "680", "340 × 2 = 680 m."),
            make_sa(3, "Vận dụng", "Tia sét có cường độ dòng điện lên tới 30 000 A phóng trong thời gian 0,001 giây. Điện lượng truyền xuống đất là bao nhiêu Coulomb?", "30", "q = I × t = 30 000 × 0,001 = 30 C."),
            make_sa(4, "Vận dụng", "Khoảng cách từ đám mây dông xuống đất là 2 000 m. Nếu vận tốc âm thanh là 340 m/s thì sau khi sét đánh bao nhiêu giây (làm tròn 1 chữ số thập phân) người ở dưới đất nghe thấy tiếng sấm?", "5.9", "2 000 / 340 ≈ 5,88 ≈ 5,9 s."),
            make_sa(5, "Vận dụng cao", "Hiệu điện thế giữa đám mây và mặt đất trước khi phóng sét là 100 000 000 V (10^8 V). Tia sét phóng điện lượng 20 C. Năng lượng tỏa ra của tia sét là bao nhiêu triệu Joule (MJ)?", "2000", "W = U × q = 10^8 × 20 = 2 × 10^9 J = 2 000 MJ."),
            make_sa(6, "Vận dụng cao", "Dây cáp thoát sét bằng đồng có tiết diện 50 mm². Mật độ dòng điện cực đại khi sét 25 000 A đánh qua dây cáp là bao nhiêu A/mm²?", "500", "25 000 / 50 = 500 A/mm².")
        ],
        [
            make_vdc(1, "Một người nông dân đang làm việc giữa cánh đồng trống thì bất ngờ có cơn dông kèm sấm sét dữ dội. Trong các hành động sau, hành động nào đảm bảo an toàn tính mạng cao nhất?", ["Lập tức bỏ các nông cụ bằng sắt kim loại ra xa, chạy khỏi các vũng nước đọng, chọn chỗ đất trũng thấp ngồi xổm co người chụm hai chân sát nhau", "Chạy lại nấp dưới gốc cây cổ thụ to nhất đồng", "Nằm duỗi thẳng tay chân áp sát ngực xuống mặt ruộng ướt", "Đứng thẳng giương cuốc sắt lên trời"], 0, "Ngồi xổm chụm hai chân ở chỗ trũng thấp giảm thiểu rủi ro sét đánh trực tiếp và điện áp bước."),
            make_vdc(2, "Khái niệm 'Điện áp bước' (Step Voltage) nguy hiểm tính mạng khi có sét đánh xuống mặt đất gần đó được hiểu là:", ["Sự chênh lệch điện thế giữa hai bàn chân khi bước đi trên mặt đất nhiễm điện sét, bước chân càng rộng thì điện áp chênh lệch càng lớn làm dòng điện chạy qua hai chân gây tử vong", "Điện áp của viên pin bước đi", "Điện áp trong giày cao su", "Điện áp của bước nhảy"], 0, "Điện áp bước chênh lệch giữa hai bàn chân; chụm chân lại triệt tiêu điện áp bước."),
            make_vdc(3, "Tại sao các bồn chứa dầu và khí đốt hóa lỏng lớn tại các kho cảng bắt buộc phải được bao quanh bằng một hệ thống lưới kim loại nối đất chằng chịt và nhiều kim thu lôi?", ["Tạo lồng đẳng thế bảo vệ ngăn chặn điện trường sét cảm ứng tĩnh điện gây đánh lửa trên van thở bồn chứa", "Để che nắng mưa", "Để giữ bồn không bị gió bão thổi bay", "Để phát sóng viễn thông"], 0, "Lưới chống sét ngăn cảm ứng tĩnh điện gây nổ hơi dầu khí."),
            make_vdc(4, "Một tia sét phóng thẳng vào cây cổ thụ làm thân cây bị toác vỏ nứt đôi bốc khói dữ dội. Nguyên nhân vật lí của hiện tượng nứt toác thân cây là:", ["Dòng điện sét cực lớn chạy qua dòng nhựa cây làm nước trong nhựa bốc hơi tức thời sinh áp suất hơi cực lớn nổ tung thân gỗ từ bên trong", "Do cây bị sét đốt cháy hoàn toàn", "Do gió thổi gãy", "Do cây hút điện tích"], 0, "Nước trong thân cây bốc hơi nổ sinh áp suất cực lớn xé toác thớ gỗ.")
        ]
    )

    # =========================================================================
    # BÀI 21: DÒNG ĐIỆN, NGUỒN ĐIỆN (3 ĐỀ)
    # =========================================================================
    l21_id = "phys8_c5_b21"
    l21_name = "Bài 21: Dòng điện, nguồn điện"

    # --- B21 ĐỀ 1: Khái niệm Dòng điện & Dòng điện kim loại ---
    exams[f"{l21_id}_test1"] = meta(l21_id, l21_name, 1,
        [
            make_mc(1, "Nhận biết", "Dòng điện là dòng:", ["Chuyển dời có hướng của các hạt mang điện tích", "Chuyển động hỗn loạn của các phân tử", "Chảy của chất lỏng", "Chuyển động của proton trong hạt nhân"], 0, "Dòng điện là dòng chuyển dời có hướng của các hạt mang điện."),
            make_mc(2, "Nhận biết", "Trong kim loại, dòng điện là dòng chuyển dời có hướng của:", ["Các electron tự do", "Các ion dương", "Các ion âm", "Các nguyên tử kim loại"], 0, "Dòng electron tự do trong kim loại."),
            make_mc(3, "Nhận biết", "Hạt nào sau đây tự do dịch chuyển trong mạng tinh thể kim loại?", ["Electron tự do", "Proton", "Neutron", "Hạt nhân"], 0, "Electron tự do."),
            make_mc(4, "Nhận biết", "Vật liệu nào sau đây là chất dẫn điện tốt nhất?", ["Kim loại (đồng, nhôm, bạc, sắt)", "Nhựa cao su", "Thủy tinh", "Gỗ khô"], 0, "Kim loại dẫn điện tốt."),
            make_mc(5, "Nhận biết", "Vật liệu nào sau đây là chất cách điện?", ["Nhựa, cao su, sứ, thủy tinh, gỗ khô", "Dây đồng", "Dây nhôm", "Dung dịch nước muối"], 0, "Chất cách điện: nhựa, cao su, sứ, thủy tinh."),
            make_mc(6, "Nhận biết", "Khi chưa nối vào nguồn điện, các electron tự do trong dây dẫn kim loại:", ["Chuyển động hỗn loạn không ngừng về mọi hướng", "Đứng yên bất động", "Chuyển động theo đường thẳng về một đầu", "Quay quanh hạt nhân cố định"], 0, "Chuyển động nhiệt hỗn loạn về mọi hướng."),
            make_mc(7, "Thông hiểu", "Khi nối hai đầu dây kim loại với hai cực của pin thì:", ["Dưới tác dụng của nguồn điện, các electron tự do chuyển dời có hướng tạo thành dòng điện", "Các proton chạy ra ngoài", "Dây kim loại nở ra", "Dây biến thành chất khác"], 0, "Nguồn điện tạo điện trường định hướng các electron."),
            make_mc(8, "Thông hiểu", "Trong mạch điện kín, các electron tự do trong dây dẫn kim loại bị:", ["Cực âm của pin đẩy và cực dương của pin hút", "Cực dương đẩy cực âm hút", "Cả hai cực hút", "Cả hai cực đẩy"], 0, "Electron âm bị cực âm đẩy, cực dương hút."),
            make_mc(9, "Thông hiểu", "Vì sao ruột dây điện làm bằng đồng còn vỏ bọc ngoài bằng nhựa dẻo PVC?", ["Đồng dẫn điện tốt để tải dòng điện, nhựa cách điện an toàn cho người sử dụng", "Để dây điện đẹp", "Đồng dẻo hơn nhựa", "Nhựa đắt tiền hơn đồng"], 0, "Đồng dẫn điện, nhựa cách điện bảo vệ."),
            make_mc(10, "Thông hiểu", "Nước cất tinh khiết hầu như không dẫn điện, nhưng khi hòa thêm một ít muối ăn vào thì dung dịch dẫn điện tốt vì:", ["Khi hòa tan, muối phân li thành các ion dương Na+ và ion âm Cl- tự do chuyển động dẫn điện", "Muối làm nước nóng lên", "Muối tạo ra kim loại natri", "Muối hút electron"], 0, "Các ion Na+ và Cl- tự do dẫn điện."),
            make_mc(11, "Thông hiểu", "Không khí ở điều kiện bình thường là một chất:", ["Cách điện rất tốt", "Dẫn điện tốt như đồng", "Bán dẫn", "Chất siêu dẫn"], 0, "Không khí bình thường cách điện rất tốt."),
            make_mc(12, "Thông hiểu", "Dòng điện trong dung dịch axit, bazơ, muối (chất điện phân) là dòng chuyển dời có hướng của:", ["Các ion dương và ion âm", "Chỉ có electron tự do", "Các phân tử nước", "Các nguyên tử"], 0, "Dòng ion dương và ion âm ngược chiều nhau.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về bản chất dòng điện và hạt tải điện:", [
                ("a", "Dòng điện là dòng chuyển dời có hướng của các điện tích.", True),
                ("b", "Trong kim loại, các hạt tải điện mang điện tích tự do là các electron.", True),
                ("c", "Chiều chuyển dịch của electron tự do trong kim loại là từ cực âm về cực dương.", True),
                ("d", "Các hạt proton trong hạt nhân kim loại tự do chạy dọc dây dẫn tạo thành dòng điện.", False)
            ], "Proton gắn chặt tại các nút mạng tinh thể không dịch chuyển tự do."),
            make_tf(2, "Thông hiểu", "Chất dẫn điện và chất cách điện:", [
                ("a", "Chất dẫn điện là chất cho dòng điện chạy qua.", True),
                ("b", "Chất cách điện là chất không cho dòng điện chạy qua.", True),
                ("c", "Dây cáp nhôm truyền tải điện cao thế dùng không khí xung quanh làm môi trường cách điện tự nhiên.", True),
                ("d", "Gỗ ướt và nước máy sinh hoạt là chất cách điện hoàn hảo tuyệt đối.", False)
            ], "Nước máy và gỗ ướt có ion dẫn điện nên dẫn điện gây điện giật nguy hiểm."),
            make_tf(3, "Vận dụng", "Thí nghiệm kiểm tra tính dẫn điện của các vật liệu:", [
                ("a", "Ruột bút chì làm bằng than chì (graphite) dẫn điện được.", True),
                ("b", "Vỏ bút bi bằng nhựa không dẫn điện (chất cách điện).", True),
                ("c", "Đoạn dây chỉ khâu bằng sợi cotton khô dẫn điện tốt làm đèn sáng.", False),
                ("d", "Chiếc chìa khóa cửa bằng đồng dẫn điện làm bóng đèn phát sáng.", True)
            ], "Chỉ khô là chất cách điện."),
            make_tf(4, "Vận dụng", "Sự di chuyển của các hạt mang điện trong pin và dây dẫn:", [
                ("a", "Trong dây dẫn kim loại ngoài mạch, electron chạy từ cực âm sang cực dương.", True),
                ("b", "Bên trong nguồn điện, các phản ứng hóa học đưa electron từ cực dương về cực âm.", True),
                ("c", "Cường độ dòng điện là đại lượng đặc trưng cho độ mạnh yếu của dòng điện.", True),
                ("d", "Khi mạch điện bị hở ở công tắc, các electron tự do vẫn tiếp tục chạy vòng quanh mạch.", False)
            ], "Mạch hở thì dòng điện ngừng chạy ngay lập tức.")
        ],
        [
            make_sa(1, "Thông hiểu", "Hạt mang điện tự do trong kim loại là gì? (Viết tên hạt)", "electron", "Hạt electron (electron tự do)."),
            make_sa(2, "Thông hiểu", "Đồng, nhôm, cao su, sắt: chất nào là chất cách điện?", "cao su", "Cao su là chất cách điện."),
            make_sa(3, "Vận dụng", "Trong 10 giây có một điện lượng 5 Coulomb chuyển qua tiết diện dây dẫn. Cường độ dòng điện là bao nhiêu Ampe? (I = q / t)", "0.5", "I = 5 / 10 = 0,5 A."),
            make_sa(4, "Vận dụng", "Một dây dẫn kim loại có dòng điện 2 A chạy qua trong 5 giây. Điện lượng đã dịch chuyển qua dây là bao nhiêu Coulomb?", "10", "q = I × t = 2 × 5 = 10 C."),
            make_sa(5, "Vận dụng cao", "Biết một electron mang điện tích -1,6 × 10^-19 C. Dòng điện 1,6 A chạy qua dây tóc bóng đèn trong 1 giây thì có bao nhiêu electron chạy qua tiết diện dây tóc?", "10000000000000000000", "q = 1,6 C => N = 1,6 / (1,6 × 10^-19) = 10^19 hạt."),
            make_sa(6, "Vận dụng cao", "Vận tốc trôi có hướng trung bình của electron trong kim loại chỉ khoảng 0,1 mm/s (rất chậm), nhưng tại sao khi vừa bật công tắc thì bóng đèn ở cách xa hàng trăm mét lập tức sáng ngay?", "300000", "Điện trường lan truyền với vận tốc ánh sáng xấp xỉ 300 000 km/s tác dụng lên tất cả electron cùng lúc.")
        ],
        [
            make_vdc(1, "Một người làm thí nghiệm cắm hai bản cực kim loại (một bản đồng Cu và một bản kẽm Zn) vào một quả chanh tươi rồi nối hai đầu cực với một đồng hồ đo điện vôn kế. Hiện tượng xảy ra là đồng hồ chỉ khoảng 0,9 V. Quả chanh đóng vai trò là:", ["Một nguồn điện hóa học (pin quả chanh) sinh ra dòng điện nhờ phản ứng hóa học giữa axit citric và hai kim loại khác nhau", "Một điện trở tiêu thụ điện", "Một tụ điện tích điện", "Một cuộn dây cảm ứng"], 0, "Pin hóa học quả chanh tạo hiệu điện thế nhờ axit citric phân li ion tác dụng với hai điện cực."),
            make_vdc(2, "Đèn phát quang đi-ốt (đèn LED) chỉ cho dòng điện chạy qua theo đúng một chiều xác định. Nếu mắc cực dương của pin vào bản cực dài (anot) và cực âm vào bản cực ngắn (catot) của đèn LED thì đèn sáng, đảo ngược cực thì đèn không sáng. Tính chất này được gọi là:", ["Tính dẫn điện một chiều của đi-ốt bán dẫn", "Tính dẫn điện hai chiều", "Tính cách điện", "Tính siêu dẫn"], 0, "Tính dẫn điện một chiều của lớp tiếp giáp p-n trong LED."),
            make_vdc(3, "Tại sao khi nối hai cực của một cục pin tiểu bằng một đoạn dây đồng ngắn trần (không qua bóng đèn hay thiết bị điện nào) thì dây đồng và pin nhanh chóng nóng ran lên nguy hiểm?", ["Xảy ra hiện tượng ngắn mạch (đoản mạch), dòng điện trong mạch tăng vọt cực lớn sinh nhiệt lượng khổng lồ làm hỏng pin và có thể phát hỏa", "Do pin tự hút nhiệt môi trường", "Do đồng sinh ra ma sát", "Do pin bị nhiễm từ"], 0, "Đoản mạch dòng điện cực lớn sinh nhiệt phá hủy nguồn."),
            make_vdc(4, "Trong y học hiện đại, máy đo điện tim (ECG) và máy đo điện não (EEG) ghi lại được các tín hiệu hoạt động của tim và não là nhờ phát hiện:", ["Các dòng điện sinh học cực nhỏ xuất hiện do sự dịch chuyển có hướng của các ion qua màng tế bào thần kinh và cơ tim", "Nhiệt độ phát ra từ tim", "Sóng âm thanh từ tim", "Lực co bóp cơ học"], 0, "Dòng điện sinh học tạo bởi gradient nồng độ ion Na+, K+, Ca2+ qua màng tế bào.")
        ]
    )

    # --- B21 ĐỀ 2: Nguồn điện & Phân loại nguồn điện ---
    exams[f"{l21_id}_test2"] = meta(l21_id, l21_name, 2,
        [
            make_mc(1, "Nhận biết", "Chức năng cốt lõi của nguồn điện trong mạch là:", ["Cung cấp và duy trì dòng điện lâu dài cho các thiết bị điện hoạt động", "Tiêu thụ năng lượng điện", "Đo dòng điện", "Ngắt mạch điện"], 0, "Cung cấp dòng điện."),
            make_mc(2, "Nhận biết", "Mỗi nguồn điện thông thường (như pin, ắc quy) đều có:", ["Hai cực: cực dương (+) và cực âm (-)", "Chỉ một cực duy nhất", "Ba cực", "Bốn cực"], 0, "Hai cực (+) và (-)."),
            make_mc(3, "Nhận biết", "Thiết bị nào sau đây là nguồn điện?", ["Pin con thỏ, ắc quy xe máy, pin mặt trời", "Bóng đèn sợi đốt", "Quạt điện", "Công tắc điện"], 0, "Pin, ắc quy, pin mặt trời là nguồn điện."),
            make_mc(4, "Nhận biết", "Đinamô xe đạp là thiết bị biến đổi năng lượng nào thành điện năng?", ["Cơ năng thành điện năng", "Nhiệt năng thành điện năng", "Hóa năng thành điện năng", "Quang năng thành điện năng"], 0, "Cơ năng bánh xe thành điện năng."),
            make_mc(5, "Nhận biết", "Pin mặt trời biến đổi trực tiếp dạng năng lượng nào thành điện năng?", ["Quang năng (năng lượng ánh sáng)", "Hóa năng", "Nhiệt năng", "Cơ năng"], 0, "Quang năng thành điện năng."),
            make_mc(6, "Nhận biết", "Ắc quy là nguồn điện hóa học có đặc điểm vượt trội so với pin thông thường là:", ["Có thể nạp điện lại nhiều lần để tái sử dụng lâu dài", "Không cần hai cực", "Không bao giờ hết điện", "Làm bằng nhựa"], 0, "Ắc quy là pin thứ cấp sạc lại được."),
            make_mc(7, "Thông hiểu", "Trên vỏ một viên pin tiểu AA có ghi số 1,5 V. Số liệu này cho biết:", ["Hiệu điện thế giữa hai cực của viên pin khi chưa mắc vào mạch kín", "Cường độ dòng điện của pin", "Khối lượng viên pin", "Thời gian dùng pin"], 0, "Hiệu điện thế định mức của pin 1,5 V."),
            make_mc(8, "Thông hiểu", "Cực dương của pin tròn (pin con thỏ) thông thường là:", ["Núm kim loại nhỏ nhô lên ở đầu trên", "Đáy phẳng bằng kẽm ở đầu dưới", "Vỏ giấy bọc ngoài", "Không có cực dương"], 0, "Núm kim loại nhô lên là cực dương (+)."),
            make_mc(9, "Thông hiểu", "Khi một viên pin dùng lâu ngày bị 'hết điện', nguyên nhân là do:", ["Hóa chất bên trong pin đã tham gia phản ứng hết nên không duy trì được hiệu điện thế giữa hai cực", "Electron bị chảy ra ngoài", "Pin bị lạnh đi", "Pin bị nhiễm từ"], 0, "Hóa chất trong pin phản ứng hết."),
            make_mc(10, "Thông hiểu", "Nguồn điện trong lưới điện sinh hoạt gia đình ở Việt Nam cung cấp dòng điện xoay chiều có hiệu điện thế hiệu dụng là:", ["220 V", "110 V", "12 V", "1,5 V"], 0, "Điện lưới gia đình 220 V."),
            make_mc(11, "Thông hiểu", "Ắc quy trên xe máy, ô tô thường cung cấp hiệu điện thế một chiều định mức là:", ["12 V", "220 V", "1,5 V", "100 V"], 0, "Ắc quy xe máy, ô tô thường là 12 V."),
            make_mc(12, "Thông hiểu", "Để có một bộ nguồn 6 V thắp sáng đèn từ các viên pin 1,5 V, người ta cần:", ["Mắc nối tiếp 4 viên pin 1,5 V cực dương pin này nối cực âm pin kia", "Mắc song song 4 viên", "Mắc 2 viên pin", "Chỉ cần 1 viên pin"], 0, "4 × 1,5 V = 6 V mắc nối tiếp.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về cấu tạo và phân loại nguồn điện:", [
                ("a", "Nguồn điện có khả năng duy trì hiệu điện thế giữa hai cực của nó.", True),
                ("b", "Cực dương kí hiệu bằng dấu (+), cực âm kí hiệu bằng dấu (-).", True),
                ("c", "Pin cúc áo dùng trong đồng hồ đeo tay là nguồn điện.", True),
                ("d", "Bóng đèn và ấm đun nước là các nguồn điện gia đình.", False)
            ], "Bóng đèn, ấm đun nước là thiết bị tiêu thụ điện năng, không phải nguồn."),
            make_tf(2, "Thông hiểu", "Sử dụng pin an toàn và bảo vệ môi trường:", [
                ("a", "Pin cũ đã qua sử dụng chứa nhiều kim loại nặng độc hại như chì, thủy ngân, cadimi.", True),
                ("b", "Không vứt pin cũ vào thùng rác sinh hoạt thông thường hay đốt pin.", True),
                ("c", "Nên thu gom pin cũ riêng để chuyển đến các điểm xử lý rác thải nguy hại.", True),
                ("d", "Có thể ném pin cũ vào đống lửa đốt rác thoải mái.", False)
            ], "Đốt pin có thể gây nổ và phát tán kim loại nặng cực độc vào không khí."),
            make_tf(3, "Vận dụng", "Ghép nối các nguồn điện một chiều:", [
                ("a", "Mắc nối tiếp hai pin 1,5 V ta được bộ nguồn có hiệu điện thế 3,0 V.", True),
                ("b", "Khi mắc nối tiếp, cực dương pin 1 nối cực âm pin 2.", True),
                ("c", "Nếu lắp ngược một viên pin trong khay 2 pin nối tiếp thì bóng đèn không sáng.", True),
                ("d", "Mắc nối tiếp 3 viên pin 1,5 V ta được bộ nguồn 12 V.", False)
            ], "3 viên pin 1,5 V nối tiếp tạo hiệu điện thế 4,5 V."),
            make_tf(4, "Vận dụng", "Nguồn điện trong thực tế đời sống:", [
                ("a", "Pin mặt trời chuyển đổi quang năng của ánh nắng thành điện năng sạch.", True),
                ("b", "Đinamô xe đạp tạo ra dòng điện thắp sáng đèn khi bánh xe quay.", True),
                ("c", "Pin dự phòng (sạc dự phòng) điện thoại là một khối pin Lithium-ion sạc lại được.", True),
                ("d", "Ổ cắm điện 220 V trong nhà là nguồn điện một chiều giống hệt pin tiểu.", False)
            ], "Điện lưới gia đình là dòng điện xoay chiều (AC), pin là dòng điện một chiều (DC).")
        ],
        [
            make_sa(1, "Thông hiểu", "Mỗi nguồn điện luôn có mấy cực?", "2", "2 cực: (+) và (-)."),
            make_sa(2, "Thông hiểu", "Một viên pin tiểu thông dụng có hiệu điện thế định mức là bao nhiêu Volt?", "1.5", "1,5 V."),
            make_sa(3, "Vận dụng", "Mắc nối tiếp 3 viên pin 1,5 V. Hiệu điện thế tổng cộng của bộ nguồn là bao nhiêu Volt?", "4.5", "1,5 × 3 = 4,5 V."),
            make_sa(4, "Vận dụng", "Để có bộ nguồn 9 V cần mắc nối tiếp bao nhiêu viên pin loại 1,5 V?", "6", "9 / 1,5 = 6 viên."),
            make_sa(5, "Vận dụng cao", "Một ắc quy 12 V có dung lượng 5 Ah. Nếu cung cấp dòng điện 0,5 A liên tục thì ắc quy dùng được trong bao nhiêu giờ?", "10", "t = 5 / 0,5 = 10 giờ."),
            make_sa(6, "Vận dụng cao", "Một tấm pin mặt trời cung cấp dòng điện 2 A ở hiệu điện thế 18 V. Công suất phát điện của tấm pin là bao nhiêu Watt? (P = U × I)", "36", "P = 18 × 2 = 36 W.")
        ],
        [
            make_vdc(1, "Một người lắp 2 viên pin 1,5 V vào khay pin của một chiếc đèn pin cầm tay. Đèn pin không sáng dù pin mới mua. Khi mở khay pin ra kiểm tra, người đó phát hiện hai viên pin được đặt cùng chiều: hai cực dương đều hướng về phía bóng đèn. Nguyên nhân đèn không sáng là:", ["Do lắp ngược cực một viên pin làm hiệu điện thế hai pin triệt tiêu nhau: U = 1,5 V - 1,5 V = 0 V nên không có dòng điện", "Do bóng đèn bị cháy ngay tức khắc", "Do khay pin quá chật", "Do pin tự hút nhiệt"], 0, "Hai pin mắc ngược cực triệt tiêu hiệu điện thế U = 0."),
            make_vdc(2, "Hệ thống trạm phát điện mặt trời mái nhà kết hợp bộ lưu trữ pin lithium (BESS) hoạt động theo chu trình:", ["Ban ngày pin mặt trời biến quang năng thành điện năng cung cấp tải và sạc vào khối pin tích điện, ban đêm khối pin phóng điện cung cấp cho ngôi nhà", "Ban đêm pin mặt trời hút ánh trăng phát điện", "Ban ngày pin mặt trời chạy động cơ nổ", "Khối pin tự sinh ra điện không cần sạc"], 0, "Tích trữ năng lượng quang điện ban ngày dùng cho ban đêm."),
            make_vdc(3, "Tại sao các thiết bị điện tử thông minh như điện thoại, máy tính bảng dùng pin Lithium-ion khi pin báo còn dưới 5% hoặc bị phồng pin thì người dùng không nên tiếp tục cắm sạc vừa dùng?", ["Pin bị phồng chứng tỏ màng ngăn bên trong bị tổn hại thoát khí dễ xảy ra ngắn mạch bên trong gây cháy nổ pin ở nhiệt độ cao", "Để tiết kiệm điện", "Để màn hình không bị mờ", "Để loa không bị rè"], 0, "Nguy cơ thoát nhiệt gây nổ pin lithium bị tổn hại."),
            make_vdc(4, "Một máy phát điện gió mini ở vùng biển đảo quay cánh quạt truyền động tới máy phát điện xoay chiều, qua bộ chỉnh lưu cầu đi-ốt nạp vào hệ ắc quy 24 V. Bộ chỉnh lưu đi-ốt có nhiệm vụ cốt lõi là:", ["Biến đổi dòng điện xoay chiều do máy phát gió tạo ra thành dòng điện một chiều để nạp điện an toàn vào ắc quy", "Tăng tốc độ gió", "Làm mát cánh quạt", "Đo áp suất gió"], 0, "Chỉnh lưu AC thành DC nạp cho ắc quy.")
        ]
    )

    # --- B21 ĐỀ 3: An toàn nguồn điện & Pin hóa học ---
    exams[f"{l21_id}_test3"] = meta(l21_id, l21_name, 3,
        [
            make_mc(1, "Nhận biết", "Nguồn điện nào sau đây an toàn cho học sinh thực hành cầm tay trực tiếp vào hai cực mà không bị giật?", ["Pin tiểu 1,5 V, pin vuông 9 V, ắc quy 12 V", "Ổ cắm điện lưới gia đình 220 V", "Đường dây điện cao thế 110 kV", "Biến áp công nghiệp 380 V"], 0, "Nguồn pin dưới 40 V an toàn cho người chạm vào."),
            make_mc(2, "Nhận biết", "Hiệu điện thế nào sau đây bắt đầu có thể gây nguy hiểm giật chết người đối với cơ thể người?", ["Trên 40 V (như điện 110 V, 220 V)", "Dưới 1,5 V", "Dưới 6 V", "Dưới 12 V"], 0, "Hiệu điện thế trên 40 V là ngưỡng nguy hiểm."),
            make_mc(3, "Nhận biết", "Dụng cụ dùng để kiểm tra nhanh xem dây dẫn có điện nguy hiểm hay không là:", ["Bút thử điện", "Nhiệt kế", "Thước kẹp", "Kính lúp"], 0, "Bút thử điện."),
            make_mc(4, "Nhận biết", "Trong pin hóa học Volta cổ điển gồm hai bản cực kim loại nhúng vào dung dịch axit loãng, hai kim loại đó là:", ["Đồng (Cu) và Kẽm (Zn)", "Sắt và Nhôm", "Vàng và Bạc", "Chì và Thủy ngân"], 0, "Cực dương Cu và cực âm Zn."),
            make_mc(5, "Nhận biết", "Cực âm của pin Volta làm bằng:", ["Kẽm (Zn)", "Đồng (Cu)", "Than chì (C)", "Chì (Pb)"], 0, "Kẽm Zn là cực âm."),
            make_mc(6, "Nhận biết", "Khi nạp điện cho ắc quy, nguồn điện nạp biến đổi:", ["Điện năng thành hóa năng tích trữ trong ắc quy", "Hóa năng thành cơ năng", "Nhiệt năng thành quang năng", "Quang năng thành cơ năng"], 0, "Nạp điện: điện năng thành hóa năng."),
            make_mc(7, "Thông hiểu", "Tại sao tuyệt đối không được tự ý chọc que kim loại hoặc ngón tay vào ổ điện 220 V trong nhà?", ["Vì dòng điện 220 V qua cơ thể người gây co giật cơ, ngừng tim, ngừng thở dẫn đến tử vong ngay tức khắc", "Vì làm hỏng ổ điện", "Vì làm tốn tiền điện", "Vì ổ điện sẽ bị bẩn"], 0, "Nguy cơ điện giật chết người ở 220 V."),
            make_mc(8, "Thông hiểu", "Một chiếc xe đạp điện sử dụng bộ nguồn gồm 4 bình ắc quy 12 V mắc nối tiếp. Hiệu điện thế tổng cung cấp cho động cơ xe là:", ["48 V", "12 V", "24 V", "36 V"], 0, "4 × 12 V = 48 V."),
            make_mc(9, "Thông hiểu", "Vì sao không bao giờ được chạm tay vào dây điện trần bị đứt rơi xuống đường sau mưa bão?", ["Vì dây có thể vẫn mang điện áp cao truyền qua mặt đất ướt gây điện giật chết người từ xa", "Vì dây bẩn", "Vì dây sắc nhọn", "Vì dây quá nặng"], 0, "Nguy cơ điện giật do dòng rò cao áp trên đất ướt."),
            make_mc(10, "Thông hiểu", "Để tránh bị điện giật khi sửa chữa điện gia đình, thao tác bắt buộc đầu tiên là:", ["Ngắt cầu dao tổng (aptomat tổng) của mạng điện", "Đeo kính râm", "Bật đèn sáng hết cỡ", "Đi chân trần"], 0, "Ngắt nguồn aptomat tổng."),
            make_mc(11, "Thông hiểu", "Khi một người bị điện giật dính vào dây điện, người cứu hộ tuyệt đối KHÔNG ĐƯỢC:", ["Dùng tay trần chạm trực tiếp vào nạn nhân để kéo ra", "Ngắt cầu dao điện ngay", "Dùng gậy gỗ khô gạt dây điện ra", "Đứng trên vật cách điện khô ráo"], 0, "Tay trần chạm vào nạn nhân sẽ bị điện giật truyền sang."),
            make_mc(12, "Thông hiểu", "Pin sạc NiMH hoặc Li-ion được dùng rộng rãi thay thế pin dùng một lần vì:", ["Tái sạc được hàng trăm lần giúp tiết kiệm chi phí và giảm thiểu rác thải pin độc hại ra môi trường", "Có điện áp 220 V", "Không bao giờ phải sạc", "Làm bằng vàng"], 0, "Tái sử dụng nhiều lần, bảo vệ môi trường.")
        ],
        [
            make_tf(1, "Thông hiểu", "Nguyên tắc an toàn điện với các loại nguồn điện:", [
                ("a", "Nguồn điện pin tiểu 1,5 V hoàn toàn an toàn khi tiếp xúc trực tiếp bằng tay.", True),
                ("b", "Nguồn điện lưới gia đình 220 V rất nguy hiểm chết người.", True),
                ("c", "Dòng điện chạy qua cơ thể người phụ thuộc hiệu điện thế và điện trở cơ thể người.", True),
                ("d", "Người đứng chân trần trên sàn nhà ướt thì điện trở cơ thể người tăng lên rất cao.", False)
            ], "Sàn ướt làm giảm mạnh điện trở cơ thể, dòng điện giật tăng vọt nguy hiểm hơn."),
            make_tf(2, "Thông hiểu", "Quy trình sơ cứu người bị điện giật an toàn:", [
                ("a", "Bình tĩnh tìm cách ngắt cầu dao hoặc aptomat điện gần nhất ngay lập tức.", True),
                ("b", "Nếu không ngắt được điện, dùng gậy gỗ khô, que tre khô gạt dây điện ra khỏi nạn nhân.", True),
                ("c", "Người cứu hộ đứng trên tấm gỗ khô, đi ủng cao su hoặc dép nhựa khô ráo.", True),
                ("d", "Lao vào ôm lấy người bị nạn kéo ra thật nhanh bằng tay trần.", False)
            ], "Chạm tay trần vào người bị giật sẽ bị dòng điện truyền sang gây tử vong cho cả hai."),
            make_tf(3, "Vận dụng", "Bộ nguồn ắc quy xe máy điện gồm 5 ắc quy loại 12 V mắc nối tiếp:", [
                ("a", "Tổng hiệu điện thế của bộ nguồn là 60 V.", True),
                ("b", "Hiệu điện thế 60 V đã vượt qua ngưỡng an toàn thông thường (40 V).", True),
                ("c", "Khi sửa chữa khối ắc quy này cần dùng dụng cụ có cán cách điện.", True),
                ("d", "Mắc nối tiếp 5 ắc quy sẽ làm dung lượng Ah của bộ nguồn tăng gấp 5 lần.", False)
            ], "Mắc nối tiếp chỉ tăng hiệu điện thế U, dung lượng Ah giữ nguyên."),
            make_tf(4, "Vận dụng", "Pin củ khoai tây và pin quả chanh làm thí nghiệm KHTN 8:", [
                ("a", "Chanh hoặc khoai tây đóng vai trò là dung dịch chất điện phân.", True),
                ("b", "Cần hai kim loại khác nhau (như thanh đồng và đinh kẽm) cắm vào củ khoai tây.", True),
                ("c", "Hai kim loại giống hệt nhau (hai thanh đồng) cắm vào chanh vẫn tạo ra nguồn điện mạnh.", False),
                ("d", "Có thể ghép nối tiếp nhiều quả chanh để làm sáng một bóng đèn LED nhỏ.", True)
            ], "Phải là hai kim loại khác nhau mới tạo chênh lệch điện thế hóa học.")
        ],
        [
            make_sa(1, "Thông hiểu", "Ngưỡng hiệu điện thế bắt đầu gây nguy hiểm chết người đối với người là bao nhiêu Volt?", "40", "Khoảng 40 V."),
            make_sa(2, "Thông hiểu", "Hiệu điện thế của mạng điện sinh hoạt gia đình ở nước ta là bao nhiêu Volt?", "220", "220 V."),
            make_sa(3, "Vận dụng", "Xe máy điện dùng bộ 4 bình ắc quy 12 V mắc nối tiếp. Hiệu điện thế của bộ nguồn là bao nhiêu Volt?", "48", "12 × 4 = 48 V."),
            make_sa(4, "Vận dụng", "Mỗi quả chanh tạo hiệu điện thế 0,8 V. Cần mắc nối tiếp tối thiểu bao nhiêu quả chanh để thắp sáng đèn LED đỏ yêu cầu 2,4 V?", "3", "2,4 / 0,8 = 3 quả."),
            make_sa(5, "Vận dụng cao", "Dòng điện qua cơ thể người khoảng bao nhiêu miliampe (mA) thì gây co giật cơ bắp không thể tự buông tay ra được? (Ghi giá trị số nguyên từ 10 đến 20)", "15", "Khoảng 10-15 mA."),
            make_sa(6, "Vận dụng cao", "Một người chạm vào nguồn điện 220 V, điện trở cơ thể là 2 200 Ω. Cường độ dòng điện qua người là bao nhiêu Ampe? (I = U / R)", "0.1", "220 / 2 200 = 0,1 A (100 mA, mức gây tử vong).")
        ],
        [
            make_vdc(1, "Một người thợ điện kiểm tra dây nóng (dây pha) của ổ cắm 220 V bằng bút thử điện. Khi cắm đầu kim loại bút vào lỗ ổ điện và ngón tay chạm vào nút kim loại ở chuôi bút, đèn neon trong bút sáng lên nhưng người thợ hoàn toàn không bị giật. Nguyên nhân khoa học là:", ["Bên trong bút thử điện có mắc nối tiếp một điện trở bảo vệ có trị số cực lớn (khoảng 1 đến 2 triệu Ohm), làm cho dòng điện chạy qua đèn neon và cơ thể người xuống đất giảm xuống dưới mức an toàn (dưới 0,1 mA) nên cơ thể không cảm nhận thấy", "Do người thợ có khả năng miễn nhiễm với điện", "Do bóng đèn neon hút hết điện áp", "Do bút thử điện làm bằng nhựa cách điện 100% không cho dòng điện chạy qua"], 0, "Điện trở hàng triệu Ohm hạn chế dòng điện cực nhỏ qua người an toàn."),
            make_vdc(2, "Aptomat chống giật (ELCB hay RCCB) lắp trong mạng điện gia đình hoạt động dựa trên nguyên lí:", ["So sánh cường độ dòng điện đi vào dây nóng (dây pha) và dòng điện đi về ở dây trung tính, nếu có sự chênh lệch (dòng rò qua người xuống đất vượt quá 30 mA) thì rơle tự động ngắt điện trong tích tắc (dưới 0,03 giây)", "Đo nhiệt độ của dây dẫn điện", "Đo áp suất không khí trong phòng", "Đếm số thiết bị điện đang bật"], 0, "Bảo vệ so lệch dòng rò chống điện giật an toàn."),
            make_vdc(3, "Trong các bể bơi hiện đại hoặc hồ nước tiểu cảnh có lắp hệ thống đèn chiếu sáng chìm dưới nước, tiêu chuẩn kỹ thuật an toàn điện quốc tế bắt buộc phải dùng nguồn điện có hiệu điện thế tối đa là:", ["12 V hoặc 24 V (nguồn điện cực thấp an toàn SELV) cách ly qua máy biến áp an toàn", "220 V trực tiếp", "110 V", "380 V"], 0, "Dưới nước phải dùng nguồn điện an toàn dưới 24 V SELV."),
            make_vdc(4, "Một cục pin dự phòng dung lượng 20 000 mAh (tức 20 Ah) ở hiệu điện thế danh định 3,7 V tích trữ được tổng năng lượng điện là bao nhiêu Watt-giờ (Wh)? (Biết E = U × Q)", ["74 Wh (được phép mang lên khoang máy bay vì dưới ngưỡng 100 Wh)", "200 Wh", "37 Wh", "100 Wh"], 0, "E = 3,7 V × 20 Ah = 74 Wh (< 100 Wh theo quy chuẩn an toàn hàng không IATA).")
        ]
    )

    # =========================================================================
    # BÀI 22: MẠCH ĐIỆN ĐƠN GIẢN (3 ĐỀ ĐỘC LẬP 100%)
    # =========================================================================
    l22_id = "phys8_c5_b22"
    l22_name = "Bài 22: Mạch điện đơn giản"

    # --- B22 ĐỀ 1: Cấu tạo & Sơ đồ mạch điện cơ bản ---
    exams[f"{l22_id}_test1"] = meta(l22_id, l22_name, 1,
        [
            make_mc(1, "Nhận biết", "Một mạch điện đơn giản gồm có các bộ phận cơ bản là:", ["Nguồn điện, thiết bị tiêu thụ điện, dây dẫn và công tắc (khóa K)", "Chỉ cần bóng đèn và pin", "Chỉ cần dây dẫn và công tắc", "Chỉ cần ampe kế và vôn kế"], 0, "Nguồn, tải, dây dẫn, công tắc."),
            make_mc(2, "Nhận biết", "Công tắc (khóa K) trong mạch điện có chức năng chính là:", ["Đóng hoặc ngắt dòng điện trong mạch", "Tạo ra dòng điện", "Làm bóng đèn sáng hơn", "Tăng hiệu điện thế"], 0, "Đóng ngắt mạch điện."),
            make_mc(3, "Nhận biết", "Kí hiệu nguồn điện một pin trên sơ đồ mạch điện gồm:", ["Hai vạch song song: vạch dài mảnh là cực dương (+), vạch ngắn dày là cực âm (-)", "Hai vạch bằng nhau", "Một hình tròn chữ thập", "Một đường lượn sóng"], 0, "Vạch dài cực dương, vạch ngắn dày cực âm."),
            make_mc(4, "Nhận biết", "Kí hiệu bóng đèn trên sơ đồ mạch điện là:", ["Hình tròn có dấu nhân (X) bên trong", "Hình vuông có dấu cộng", "Hai vạch song song", "Hình tam giác"], 0, "Hình tròn có chữ X."),
            make_mc(5, "Nhận biết", "Mạch điện kín là mạch điện thỏa mãn điều kiện nào?", ["Các bộ phận nối liền thành vòng khép kín và có dòng điện chạy qua", "Bị đứt dây dẫn", "Công tắc mở", "Bóng đèn bị tháo ra"], 0, "Mạch kín có dòng điện chạy qua."),
            make_mc(6, "Nhận biết", "Kí hiệu công tắc (khóa K) đang đóng trên sơ đồ mạch điện là:", ["Đoạn thẳng nối liền hai chốt tròn tiếp xúc nhau", "Đoạn thẳng bật chếch lên trên hở một chốt", "Hình chữ nhật có vạch gạch", "Hình tam giác"], 0, "Khóa đóng tiếp điểm khép kín."),
            make_mc(7, "Thông hiểu", "Khi tháo bóng đèn ra khỏi đui đèn trong mạch điện kín, điều gì xảy ra?", ["Mạch trở thành mạch hở và không còn dòng điện chạy qua", "Dòng điện tăng vọt", "Pin bị nổ", "Mạch vẫn kín"], 0, "Mạch bị hở tại vị trí đui đèn."),
            make_mc(8, "Thông hiểu", "Thiết bị nào sau đây biến đổi trực tiếp điện năng thành cơ năng trong mạch điện gia đình?", ["Quạt điện", "Bóng đèn sợi đốt", "Bàn là khô", "Ấm siêu tốc"], 0, "Quạt điện biến điện năng thành cơ năng quay cánh quạt."),
            make_mc(9, "Thông hiểu", "Sơ đồ mạch điện có vai trò gì quan trọng trong kỹ thuật điện?", ["Giúp biểu diễn mạch điện một cách trực quan và hỗ trợ lắp ráp, sửa chữa chính xác", "Làm đẹp trang vẽ", "Giảm tiền điện", "Tăng tuổi thọ bóng đèn"], 0, "Sơ đồ mạch điện biểu diễn trực quan cấu trúc mạch."),
            make_mc(10, "Thông hiểu", "Trong mạch thắp sáng đèn pin bỏ túi, nguồn điện thường gồm:", ["Hai viên pin mắc nối tiếp (cực âm pin 1 tiếp xúc cực dương pin 2)", "Hai pin mắc đối đầu cực dương vào nhau", "Một ắc quy 220 V", "Một tụ điện đơn"], 0, "Ghép nối tiếp 2 pin để tăng hiệu điện thế."),
            make_mc(11, "Thông hiểu", "Khi đóng khóa K mà đèn pin không sáng, nguyên nhân nào sau đây KHÔNG hợp lí?", ["Công tắc đóng tiếp xúc rất tốt", "Pin đã cạn hết năng lượng điện", "Dây tóc bóng đèn đã bị đứt", "Các điểm tiếp xúc bị rỉ sét cách điện"], 0, "Tiếp xúc tốt thì đèn phải sáng bình thường."),
            make_mc(12, "Thông hiểu", "Dây dẫn điện trong sơ đồ mạch điện được quy ước vẽ bằng:", ["Các đoạn thẳng vuông góc và thẳng hàng", "Các đường cong uốn lượn tùy ý", "Các đường đứt nét ziczac", "Đường tròn khép kín"], 0, "Vẽ bằng các đoạn thẳng rõ ràng, vuông góc.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về các bộ phận cấu tạo của mạch điện đơn giản cơ bản:", [
                ("a", "Nguồn điện có nhiệm vụ duy trì hiệu điện thế và cung cấp năng lượng điện cho mạch.", True),
                ("b", "Chỉ cần có bóng đèn và dây dẫn nối với nhau là bóng đèn có thể tự phát sáng rực rỡ.", False),
                ("c", "Dây dẫn bằng đồng dùng để kết nối các bộ phận điện thành một mạch kín tuần hoàn.", True),
                ("d", "Khóa K ở vị trí mở thì mạch vẫn kín nếu dây dẫn không bị đứt.", False)
            ], "Cần nguồn điện cấp năng lượng; khóa mở thì mạch hở."),
            make_tf(2, "Thông hiểu", "Về các kí hiệu quy ước trên sơ đồ mạch điện học đường:", [
                ("a", "Kí hiệu chữ nhật rỗng biểu diễn một điện trở trong sơ đồ kỹ thuật.", True),
                ("b", "Nguồn điện gồm hai pin mắc nối tiếp được kí hiệu gồm hai cặp vạch dài mảnh và ngắn dày xen kẽ.", True),
                ("c", "Kí hiệu vòng tròn có chữ A bên trong là vôn kế đo điện áp.", False),
                ("d", "Dây dẫn nối giao nhau có tiếp xúc điện được đánh dấu bằng một chấm tròn đậm tại điểm giao.", True)
            ], "Vòng tròn có chữ A là ampe kế, chữ V mới là vôn kế."),
            make_tf(3, "Thông hiểu", "Về mạch điện của chiếc đèn pin cầm tay thông dụng:", [
                ("a", "Vỏ kim loại của đèn pin có thể được dùng làm dây dẫn nối cực âm của pin về công tắc.", True),
                ("b", "Gương cầu lõm ở đầu đèn pin có tác dụng phân tán chùm sáng ra xung quanh thật rộng.", False),
                ("c", "Lò xo ở đuôi đèn pin vừa giữ pin chặt vừa làm vật dẫn điện tiếp xúc cực âm.", True),
                ("d", "Khi bấm công tắc trượt sang vị trí ON, mạch điện bên trong đèn pin trở thành mạch kín.", True)
            ], "Gương cầu lõm hội tụ ánh sáng thành chùm song song chiếu xa."),
            make_tf(4, "Thông hiểu", "Về an toàn khi lắp ráp mạch điện thực hành tại lớp học:", [
                ("a", "Bắt buộc phải mở công tắc trong suốt quá trình cắm dây nối các linh kiện.", True),
                ("b", "Có thể nối trực tiếp một sợi dây đồng ngắn vào hai cực của viên pin để thử độ nóng.", False),
                ("c", "Cần kiểm tra kỹ các mối nối xem có bị lỏng lẻo hoặc chạm chập vào nhau hay không.", True),
                ("d", "Được phép sử dụng các nguồn điện 220 V không có biến áp cách li cho học sinh thực hành cầm tay.", False)
            ], "Không ngắn mạch pin; học sinh chỉ thực hành với nguồn an toàn dưới 12 V.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một mạch điện gồm 1 viên pin 1,5 V nối với một bóng đèn nhỏ. Hiệu điện thế nguồn cấp cho bóng đèn khi công tắc đóng là bao nhiêu Vôn (V)?", "1.5", "U = 1,5 V."),
            make_sa(2, "Thông hiểu", "Người ta mắc nối tiếp 3 viên pin giống nhau, mỗi viên pin có hiệu điện thế 1,5 V. Hiệu điện thế tổng cộng của bộ nguồn pin này là bao nhiêu Vôn (V)?", "4.5", "U = 1,5 * 3 = 4,5 V."),
            make_sa(3, "Thông hiểu", "Trong một sơ đồ mạch điện có 4 điện trở giống hệt nhau mắc nối tiếp. Nếu điện trở tương đương toàn mạch là 48 Ω thì giá trị của mỗi điện trở là bao nhiêu Ôm (Ω)?", "12", "R = 48 / 4 = 12 Ω."),
            make_sa(4, "Thông hiểu", "Một bóng đèn pin tiêu thụ dòng điện 0,25 A dưới hiệu điện thế 3 V. Điện trở của bóng đèn khi sáng bình thường bằng bao nhiêu Ôm (Ω)?", "12", "R = U / I = 3 / 0,25 = 12 Ω."),
            make_sa(5, "Vận dụng", "Một bộ pin gồm các viên pin 1,5 V mắc nối tiếp để thắp sáng bóng đèn 9 V. Cần dùng ít nhất bao nhiêu viên pin như vậy?", "6", "Số pin = 9 / 1,5 = 6 viên."),
            make_sa(6, "Vận dụng", "Một dây dẫn đồng dài 20 m có điện trở 4 Ω. Một đoạn dây cùng loại dài 35 m sẽ có điện trở là bao nhiêu Ôm (Ω)?", "7", "R2 = (4 / 20) * 35 = 7 Ω.")
        ],
        [
            make_vdc(1, "Để thắp sáng một bóng đèn LED loại (3 V - 0,02 A) bằng nguồn pin 9 V, người ta phải mắc nối tiếp bóng đèn với một điện trở hạn dòng R. Giá trị điện trở R cần chọn là:", [
                "300 Ω", "150 Ω", "450 Ω", "600 Ω"
            ], 0, "U_R = 9 - 3 = 6 V. R = 6 / 0,02 = 300 Ω."),
            make_vdc(2, "Một chiếc đèn bàn học sử dụng bộ đổi nguồn hạ áp từ 220 V xuống 12 V để cấp cho bóng đèn sợi đốt 12 V - 24 W. Cường độ dòng điện chạy qua bóng đèn khi sáng bình thường là:", [
                "2,0 A", "0,5 A", "1,0 A", "4,0 A"
            ], 0, "I = P / U = 24 / 12 = 2,0 A."),
            make_vdc(3, "Một mạch điện có sơ đồ gồm nguồn pin 6 V nối tiếp với khóa K, ampe kế có điện trở không đáng kể và bóng đèn (6 V - 3 W). Khi đóng khóa K, số chỉ của ampe kế là:", [
                "0,5 A", "2,0 A", "1,5 A", "0,25 A"
            ], 0, "I = P / U = 3 / 6 = 0,5 A."),
            make_vdc(4, "Một mạch điện gồm nguồn điện E = 12 V, nối tiếp với biến trở con chạy Rb và bóng đèn Đ ghi 6 V - 0,5 A. Để đèn sáng bình thường, giá trị điện trở biến trở tham gia mạch phải bằng:", [
                "12 Ω", "6 Ω", "24 Ω", "18 Ω"
            ], 0, "U_b = 12 - 6 = 6 V. Rb = 6 / 0,5 = 12 Ω.")
        ]
    )

    # --- B22 ĐỀ 2: Mạch điện kín, Mạch hở & Chiều dòng điện quy ước ---
    exams[f"{l22_id}_test2"] = meta(l22_id, l22_name, 2,
        [
            make_mc(1, "Nhận biết", "Chiều dòng điện trong mạch điện kín theo quy ước quốc tế là chiều:", ["Từ cực dương qua dây dẫn và thiết bị điện về cực âm của nguồn", "Từ cực âm qua dây dẫn về cực dương", "Cùng chiều chuyển động của electron tự do", "Từ điểm có điện thế thấp đến cao"], 0, "Quy ước chiều dòng điện: từ cực dương qua dây dẫn tới cực âm."),
            make_mc(2, "Nhận biết", "Trong chất dẫn điện kim loại, các hạt mang điện tích tự do chuyển dịch tạo ra dòng điện là:", ["Các electron tự do", "Các ion dương kim loại", "Các proton hạt nhân", "Các lỗ trống tĩnh điện"], 0, "Electron tự do chuyển động tạo thành dòng điện trong kim loại."),
            make_mc(3, "Nhận biết", "Mối quan hệ giữa chiều quy ước của dòng điện và chiều dịch chuyển có hướng của electron tự do là:", ["Ngược chiều nhau hoàn toàn", "Cùng chiều với nhau", "Vuông góc với nhau", "Không có liên hệ"], 0, "Electron dịch chuyển từ âm sang dương, ngược chiều quy ước."),
            make_mc(4, "Nhận biết", "Khi công tắc trong mạch điện ở trạng thái mở, mạch điện được gọi là:", ["Mạch hở", "Mạch kín", "Mạch đoản", "Mạch chập"], 0, "Công tắc mở tạo ra mạch hở, không có dòng điện."),
            make_mc(5, "Nhận biết", "Kí hiệu một công tắc (khóa K) đang mở trên sơ đồ mạch điện là:", ["Đoạn thẳng có một đầu nâng chếch lên không chạm vào chốt bên cạnh", "Đoạn thẳng khép kín hai chốt", "Vòng tròn có chữ K", "Dấu nhân gạch chéo"], 0, "Tiếp điểm hở nâng lên khỏi chốt."),
            make_mc(6, "Nhận biết", "Thiết bị nào sau đây có chức năng tự động ngắt mạch khi dòng điện vượt quá mức an toàn?", ["Cầu chì hoặc aptomat", "Bóng đèn sợi đốt", "Khóa K đảo chiều", "Vôn kế điện tử"], 0, "Cầu chì/aptomat ngắt mạch bảo vệ quá tải."),
            make_mc(7, "Thông hiểu", "Tại sao khi bật công tắc đèn trên tường, bóng đèn trên trần nhà sáng lên gần như tức thời?", ["Điện trường lan truyền dọc theo dây dẫn với tốc độ xấp xỉ tốc độ ánh sáng", "Các electron chạy từ công tắc đến bóng đèn với vận tốc ánh sáng", "Bóng đèn tự tích sẵn năng lượng", "Công tắc phóng hạt photon đến đèn"], 0, "Điện trường lan truyền cực nhanh (gần 300.000 km/s) đẩy mọi electron chuyển động cùng lúc."),
            make_mc(8, "Thông hiểu", "Trường hợp nào sau đây mạch điện trở thành mạch hở?", ["Dây dẫn bị chuột cắn đứt lìa một đoạn", "Công tắc đóng chặt tiếp xúc tốt", "Nguồn điện còn mới nguyên", "Bóng đèn được lắp chặt vào đui"], 0, "Dây đứt làm gián đoạn mạch kín thành mạch hở."),
            make_mc(9, "Thông hiểu", "Khi nối hai cực của một viên pin bằng dây đồng ngắn mà không qua tải tiêu thụ thì xảy ra:", ["Hiện tượng ngắn mạch (đoản mạch), làm pin nóng ran và nhanh hỏng", "Pin được nạp thêm điện", "Dòng điện trong dây bằng 0", "Bóng đèn phụ sáng lên"], 0, "Đoản mạch sinh dòng rất lớn làm nóng hỏng pin."),
            make_mc(10, "Thông hiểu", "Một chiếc quạt bàn đang chạy, nếu ta rút phích cắm ra khỏi ổ điện thì:", ["Quạt ngừng quay vì mạch điện bị hở tại vị trí phích cắm", "Quạt vẫn tiếp tục quay vĩnh viễn", "Quạt bị cháy mô tơ", "Dòng điện đảo chiều liên tục"], 0, "Rút phích cắm ngắt nguồn tạo mạch hở."),
            make_mc(11, "Thông hiểu", "Để xác định chiều dòng điện trong một đoạn dây dẫn thẳng trên sơ đồ, người ta dùng:", ["Mũi tên đặt dọc theo dây dẫn chỉ từ cực dương hướng về cực âm", "Dấu cộng và trừ xen kẽ", "Đường nét đứt cong", "Hình tam giác tô đen"], 0, "Dùng mũi tên chỉ chiều từ (+) sang (-)."),
            make_mc(12, "Thông hiểu", "Trong một mạch kín gồm pin và bóng đèn, năng lượng điện ban đầu do bộ phận nào cung cấp?", ["Nguồn điện (pin)", "Bóng đèn tiêu thụ", "Dây đồng dẫn điện", "Không khí xung quanh"], 0, "Nguồn điện chuyển hóa hóa năng thành điện năng cung cấp cho mạch.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về chiều dòng điện và sự dịch chuyển hạt điện tích trong dây kim loại đề 2:", [
                ("a", "Quy ước chiều dòng điện được các nhà khoa học thống nhất trước khi tìm ra hạt electron.", True),
                ("b", "Trong dây dẫn đồng, electron mang điện âm bị cực âm của nguồn đẩy và cực dương hút.", True),
                ("c", "Chiều chuyển động của electron tự do luôn trùng khớp với chiều mũi tên dòng điện trên sơ đồ.", False),
                ("d", "Dòng điện chỉ có thể chạy trong mạch khi có nguồn điện duy trì hiệu điện thế giữa hai đầu mạch.", True)
            ], "Electron tự do chuyển động ngược chiều quy ước của dòng điện."),
            make_tf(2, "Thông hiểu", "Về trạng thái mạch kín và mạch hở trong hệ thống điện dân dụng:", [
                ("a", "Khi bấm tắt công tắc đèn phòng, ta đã biến mạch thắp sáng đèn thành mạch hở.", True),
                ("b", "Nếu dây tóc của bóng đèn sợi đốt bị cháy đứt, mạch điện thắp sáng đèn đó trở thành mạch hở.", True),
                ("c", "Khi mạch hở, dòng điện chạy qua công tắc vẫn có giá trị rất lớn.", False),
                ("d", "Ổ cắm điện trên tường khi chưa cắm thiết bị tải nào là một đoạn mạch hở an toàn.", True)
            ], "Mạch hở không có dòng điện chạy qua."),
            make_tf(3, "Thông hiểu", "Về các hiện tượng đoản mạch và an toàn điện thực hành:", [
                ("a", "Hiện tượng đoản mạch xảy ra khi điện trở của phần mạch ngoài giảm xuống gần bằng 0.", True),
                ("b", "Khi đoản mạch, cường độ dòng điện trong dây dẫn giảm mạnh làm dây dẫn bị đóng băng.", False),
                ("c", "Để bảo vệ thiết bị tránh nguy cơ đoản mạch, người ta luôn mắc nối tiếp cầu chì hoặc aptomat.", True),
                ("d", "Dùng dây đồng nguyên chất dày thay cho dây chì bị đứt là giải pháp kỹ thuật an toàn tuyệt đối.", False)
            ], "Đoản mạch làm dòng tăng vọt sinh nhiệt lớn gây cháy nổ."),
            make_tf(4, "Thông hiểu", "Về sự biến đổi năng lượng trong các nhánh của mạch điện kín:", [
                ("a", "Bóng đèn dây tóc biến đổi một phần điện năng thành quang năng và phần lớn thành nhiệt năng.", True),
                ("b", "Động cơ điện mini biến đổi phần lớn điện năng tiêu thụ thành cơ năng hữu ích.", True),
                ("c", "Nguồn điện biến đổi hoàn toàn nhiệt năng của môi trường thành điện năng không hao phí.", False),
                ("d", "Khi dòng điện chạy qua bất kì vật dẫn có điện trở nào thì luôn có sự hao phí dưới dạng nhiệt.", True)
            ], "Nguồn pin biến đổi hóa năng thành điện năng; vật dẫn có điện trở luôn tỏa nhiệt J-L.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một acquy xe máy 12 V cấp điện cho còi xe có điện trở 6 Ω. Cường độ dòng điện qua còi khi bấm còi là bao nhiêu Ampe (A)?", "2", "I = U / R = 12 / 6 = 2 A."),
            make_sa(2, "Thông hiểu", "Một mạch điện có dòng điện I = 0,4 A chạy qua trong thời gian 50 giây. Lượng điện tích chuyển qua tiết diện dây là bao nhiêu Culông (C)?", "20", "q = I * t = 0,4 * 50 = 20 C."),
            make_sa(3, "Thông hiểu", "Người ta mắc nối tiếp 4 viên pin tiểu 1,5 V để thắp sáng đèn pin LED. Hiệu điện thế của bộ 4 viên pin này là bao nhiêu Vôn (V)?", "6", "U = 4 * 1,5 = 6 V."),
            make_sa(4, "Thông hiểu", "Một bóng đèn xe đạp 6 V tiêu thụ công suất 3 W. Cường độ dòng điện qua đèn khi sáng bình thường là bao nhiêu Ampe (A)?", "0.5", "I = P / U = 3 / 6 = 0,5 A."),
            make_sa(5, "Vận dụng", "Trong thời gian 2 phút (120 s), có 72 Culông điện tích chuyển qua tiết diện một dây tóc bóng đèn. Cường độ dòng điện qua đèn là bao nhiêu Ampe (A)?", "0.6", "I = 72 / 120 = 0,6 A."),
            make_sa(6, "Vận dụng", "Một điện trở R được mắc vào nguồn 9 V thì dòng điện qua R là 0,18 A. Nếu mắc R vào nguồn 15 V thì dòng điện qua R là bao nhiêu Ampe (A)?", "0.3", "R = 9 / 0,18 = 50 Ω. I' = 15 / 50 = 0,3 A.")
        ],
        [
            make_vdc(1, "Một chuỗi đèn led trang trí gồm 24 bóng đèn nhỏ giống nhau mắc nối tiếp vào hiệu điện thế U = 72 V. Hiệu điện thế trên mỗi bóng đèn led là:", [
                "3,0 V", "2,5 V", "1,5 V", "6,0 V"
            ], 0, "U1 = 72 / 24 = 3,0 V."),
            make_vdc(2, "Một mạch điện gồm nguồn pin 12 V, nối tiếp với khóa K và hai bóng đèn Đ1 (6 V - 0,5 A), Đ2 (6 V - 0,5 A). Khi đóng khóa K, trạng thái hoạt động của hai đèn là:", [
                "Cả hai đèn đều sáng bình thường", "Cả hai đèn đều bị cháy tóc", "Đèn 1 sáng mạnh, đèn 2 tối", "Cả hai đèn không sáng"
            ], 0, "Hai đèn giống nhau chia đôi điện áp 12V thành mỗi đèn 6V đúng định mức."),
            make_vdc(3, "Một mô tơ đồ chơi chạy bằng pin có điện trở trong r = 2 Ω, hoạt động ở hiệu điện thế 4,5 V. Dòng điện tiêu thụ đo được là 0,5 A. Công suất điện toàn phần của động cơ là:", [
                "2,25 W", "1,5 W", "0,5 W", "4,5 W"
            ], 0, "P = U * I = 4,5 * 0,5 = 2,25 W."),
            make_vdc(4, "Để có nguồn điện 12 V thắp sáng đèn từ các viên pin loại 1,5 V, một học sinh cần ghép nối tiếp bao nhiêu viên pin?", [
                "8 viên", "6 viên", "10 viên", "12 viên"
            ], 0, "Số pin = 12 / 1,5 = 8 viên pin nối tiếp.")
        ]
    )

    # --- B22 ĐỀ 3: Sơ đồ mạch điện kỹ thuật, Đoản mạch & Thiết bị bảo vệ ---
    exams[f"{l22_id}_test3"] = meta(l22_id, l22_name, 3,
        [
            make_mc(1, "Nhận biết", "Kí hiệu chiếc chuông điện trên bản vẽ sơ đồ mạch điện là:", ["Hình bán nguyệt có hai chân chốt hướng xuống dưới", "Hình chữ nhật có vạch chéo", "Hình tròn có dấu cộng", "Hai vạch song song dài ngắn"], 0, "Hình bán nguyệt úp tượng trưng cho chuông điện."),
            make_mc(2, "Nhận biết", "Kí hiệu cầu chì trên sơ đồ mạch điện theo tiêu chuẩn quốc tế là:", ["Hình chữ nhật hẹp có một đường dây thẳng xuyên suốt qua trục giữa", "Hình tam giác đen", "Vòng tròn có chữ F", "Hai vạch lượn sóng"], 0, "Hình chữ nhật có vạch trục dây chì xuyên qua."),
            make_mc(3, "Nhận biết", "Trong một sơ đồ mạch điện, kí hiệu đường dây dẫn nối tiếp xúc dẫn điện với nhau được thể hiện bằng:", ["Một chấm tròn đặc màu đen tại giao điểm hai dây", "Hai đường thẳng cắt chéo không có dấu chấm", "Dấu gạch chéo đỏ", "Vòng cung cầu nhảy qua dây"], 0, "Chấm tròn tại giao điểm thể hiện mối nối điện."),
            make_mc(4, "Nhận biết", "Kí hiệu vôn kế trên sơ đồ mạch điện gồm một vòng tròn bên trong có chứa chữ cái nào?", ["Chữ V in hoa", "Chữ A in hoa", "Chữ K in hoa", "Chữ W in hoa"], 0, "Chữ V đại diện cho Vôn kế (Volt meter)."),
            make_mc(5, "Nhận biết", "Kí hiệu ampe kế trên sơ đồ mạch điện gồm một vòng tròn bên trong chứa chữ cái:", ["Chữ A in hoa", "Chữ V in hoa", "Chữ R in hoa", "Chữ P in hoa"], 0, "Chữ A đại diện cho Ampe kế (Ampere meter)."),
            make_mc(6, "Nhận biết", "Khi xảy ra hiện tượng chập điện (hai dây dẫn trần chạm trực tiếp vào nhau trước tải), hiện tượng này được gọi là:", ["Đoản mạch (ngắn mạch)", "Hở mạch kỹ thuật", "Tăng tải có ích", "Cân bằng điện áp"], 0, "Chạm chập trước tải là hiện tượng đoản mạch nguy hiểm."),
            make_mc(7, "Thông hiểu", "Tác hại nguy hiểm nhất của hiện tượng đoản mạch trong gia đình nếu không có cầu chì bảo vệ là:", ["Cường độ dòng điện tăng vọt làm nóng đỏ dây dẫn gây bốc cháy hỏa hoạn", "Làm bóng đèn sáng quá chói", "Làm pin tích thêm nhiều điện", "Làm công tắc bị hút chặt"], 0, "Dòng đoản mạch sinh nhiệt cực lớn gây cháy nhà."),
            make_mc(8, "Thông hiểu", "Dây chì trong cầu chì được chế tạo từ kim loại chì hoặc hợp kim có đặc tính cơ bản là:", ["Nhiệt độ nóng chảy tương đối thấp (khoảng 327°C)", "Độ dẫn điện tốt nhất trong tự nhiên", "Không bao giờ bị nóng chảy", "Rất cứng và không bị uốn cong"], 0, "Chì nóng chảy ở nhiệt độ thấp để đứt kịp thời khi quá nhiệt."),
            make_mc(9, "Thông hiểu", "Khi tháo một bóng đèn trong dãy 3 bóng đèn đang mắc nối tiếp, các bóng đèn còn lại sẽ:", ["Đồng loạt tắt hết vì toàn bộ mạch nối tiếp bị ngắt hở", "Vẫn sáng bình thường", "Sáng rực hơn gấp 3 lần", "Nhấp nháy phát tiếng kêu"], 0, "Mạch nối tiếp chỉ cần hở một điểm là toàn mạch mất dòng."),
            make_mc(10, "Thông hiểu", "Trong đèn pin đội đầu, người ta sử dụng công tắc 3 nấc (Tắt - Sáng vừa - Sáng mạnh). Công tắc này hoạt động bằng cách:", ["Thay đổi cách nối điện qua các mức điện trở hạn dòng khác nhau", "Thay đổi cực tính của pin", "Tạo hiện tượng đoản mạch", "Thay đổi màu sắc bóng đèn"], 0, "Chuyển nấc nối tiếp thêm điện trở để giảm dòng hoặc nối trực tiếp để sáng mạnh."),
            make_mc(11, "Thông hiểu", "Để kiểm tra xem pin đồng hồ còn điện hay đã hết mà không có vôn kế, phương pháp thực nghiệm nhanh là:", ["Lắp pin vào một mạch thử có đèn LED nhỏ và công tắc", "Ngâm pin vào nước lạnh", "Nối tắt hai cực bằng một sợi xích sắt", "Cọ xát pin vào tóc"], 0, "Dùng mạch kiểm tra đèn LED đơn giản an toàn."),
            make_mc(12, "Thông hiểu", "Khi một thiết bị tiêu thụ điện được cấp đúng hiệu điện thế định mức ghi trên vỏ thì:", ["Thiết bị hoạt động bình thường và đạt đúng công suất thiết kế", "Thiết bị sẽ nhanh chóng bị nổ cháy", "Cường độ dòng điện qua thiết bị bằng 0", "Thiết bị phát ra tia lửa điện"], 0, "Hoạt động ổn định đúng định mức nhà sản xuất quy định.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về các thiết bị bảo vệ mạch điện tự động trong đời sống đề 3:", [
                ("a", "Cầu chì là linh kiện bảo vệ mạch điện bằng nguyên lí tác dụng nhiệt của dòng điện.", True),
                ("b", "Aptomat (cầu dao tự động) có thể tự ngắt khi quá tải và dễ dàng đóng lại bằng tay sau khi xử lý sự cố.", True),
                ("c", "Khi cầu chì bị cháy đứt, người dùng nên thay bằng một đoạn dây đồng lớn để tránh đứt tiếp.", False),
                ("d", "Cầu dao tổng của gia đình luôn được lắp ở đầu mạng điện ngay sau công tơ điện.", True)
            ], "Không dùng dây đồng thay cầu chì vì mất tính năng bảo vệ."),
            make_tf(2, "Thông hiểu", "Về sơ đồ nguyên lí mạch điện phòng khách gia đình:", [
                ("a", "Bóng đèn chiếu sáng và ổ cắm quạt điện được mắc song song với nhau vào nguồn 220 V.", True),
                ("b", "Công tắc bật tắt bóng đèn phải được mắc nối tiếp trên dây pha trước bóng đèn.", True),
                ("c", "Nếu tắt công tắc bóng đèn thì ổ cắm quạt cũng bị mất điện theo.", False),
                ("d", "Dây nguội (dây trung tính) có hiệu điện thế đối với mặt đất xấp xỉ bằng 0 V.", True)
            ], "Các tải mắc song song hoạt động độc lập."),
            make_tf(3, "Thông hiểu", "Về hiện tượng chập cháy và đoản mạch trong thực tế:", [
                ("a", "Chuột cắn mất lớp vỏ bọc cách điện làm hai dây dẫn chạm vào nhau là nguyên nhân phổ biến gây đoản mạch.", True),
                ("b", "Hiện tượng đoản mạch làm cho hiệu điện thế hai cực nguồn điện tăng lên gấp hàng nghìn lần.", False),
                ("c", "Các ổ cắm bị ẩm ướt hoặc dính nước mưa dễ dẫn đến hiện tượng rò rỉ điện và chập mạch.", True),
                ("d", "Sử dụng cùng lúc quá nhiều thiết bị công suất lớn vào một ổ cắm điện có thể gây quá tải đứt cầu chì.", True)
            ], "Đoản mạch làm điện trở giảm về 0, dòng điện tăng vọt, hiệu điện thế nguồn không tăng nghìn lần."),
            make_tf(4, "Thông hiểu", "Về các kỹ năng xử lý sự cố điện khẩn cấp an toàn:", [
                ("a", "Khi phát hiện có khói bốc ra từ ổ cắm điện, việc đầu tiên là chạy ngay đến ngắt cầu dao tổng.", True),
                ("b", "Dùng nước lạnh dội trực tiếp vào đám cháy thiết bị điện đang cắm điện để dập lửa nhanh.", False),
                ("c", "Chỉ sử dụng bình cứu hỏa khí CO2 hoặc bình bột chữa cháy chuyên dụng cho đám cháy điện.", True),
                ("d", "Sau khi đã ngắt hoàn toàn nguồn điện mới tiến hành kiểm tra và dập tắt các tàn lửa còn lại.", True)
            ], "Nước dẫn điện, tuyệt đối không dội nước vào thiết bị đang có điện.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một cầu chì gia đình có dòng điện giới hạn định mức là 10 A. Mạch điện sau cầu chì đang tiêu thụ dòng điện 7,2 A. Cầu chì có bị đứt hay không? (Ghi 'Không' hoặc 'Có').", "Không", "I = 7,2 A < 10 A nên cầu chì không đứt."),
            make_sa(2, "Thông hiểu", "Một gia đình bật đồng thời ấm điện (dòng 5 A), bàn là (dòng 4,5 A) và nồi cơm (dòng 3 A). Tổng cường độ dòng điện mạch chính qua cầu chì là bao nhiêu Ampe (A)?", "12.5", "I = 5 + 4,5 + 3 = 12,5 A."),
            make_sa(3, "Thông hiểu", "Trong mạch điện trên (I = 12,5 A), nếu cầu chì tổng chỉ chịu được dòng tối đa 10 A thì cầu chì sẽ phản ứng thế nào? (Ghi 'Đứt' hoặc 'Không').", "Đứt", "Dòng 12,5 A > 10 A nên cầu chì sẽ nóng chảy đứt."),
            make_sa(4, "Thông hiểu", "Một pin vuông 9 V nối với điện trở R = 45 Ω. Cường độ dòng điện qua mạch kín là bao nhiêu Ampe (A)?", "0.2", "I = U / R = 9 / 45 = 0,2 A."),
            make_sa(5, "Vận dụng", "Một bộ nguồn gồm 6 viên pin 1,5 V mắc nối tiếp cung cấp điện cho một bóng đèn 9 V - 4,5 W. Điện trở của dây tóc bóng đèn khi sáng bình thường là bao nhiêu Ôm (Ω)?", "18", "R = U^2 / P = 9^2 / 4,5 = 18 Ω."),
            make_sa(6, "Vận dụng", "Để làm giảm dòng điện qua bóng đèn từ 0,6 A xuống còn 0,4 A khi hiệu điện thế nguồn không đổi 12 V, điện trở toàn mạch cần tăng từ 20 Ω lên bao nhiêu Ôm (Ω)?", "30", "R' = U / I' = 12 / 0,4 = 30 Ω.")
        ],
        [
            make_vdc(1, "Một đường dây điện nối từ bảng điện chính vào phòng học dài 20 m (dây đôi gồm 2 sợi dài tổng cộng 40 m). Dây làm bằng đồng tiết diện 2 mm2, điện trở suất ρ = 1,7 . 10^-8 Ω.m. Điện trở của toàn bộ đường dây dẫn này là:", [
                "0,34 Ω", "0,17 Ω", "0,68 Ω", "1,7 Ω"
            ], 0, "R = ρ * (L / S) = 1,7e-8 * 40 / (2e-6) = 0,34 Ω."),
            make_vdc(2, "Khi dòng điện qua đường dây trên là 10 A, độ sụt giảm hiệu điện thế trên đường dây cấp điện này là:", [
                "3,4 V", "1,7 V", "6,8 V", "0,34 V"
            ], 0, "ΔU = I * R = 10 * 0,34 = 3,4 V."),
            make_vdc(3, "Một căn phòng có 5 bóng đèn huỳnh quang giống nhau loại 220 V - 40 W mắc song song vào mạng điện 220 V. Cường độ dòng điện tổng chạy trong mạch chính khi bật cả 5 đèn xấp xỉ bằng:", [
                "0,91 A", "0,18 A", "2,0 A", "4,5 A"
            ], 0, "P_tong = 5 * 40 = 200 W. I = P / U = 200 / 220 ≈ 0,91 A."),
            make_vdc(4, "Một mạch điện bảo vệ sử dụng một rơle nhiệt lưỡng kim. Khi nhiệt độ tăng thêm 50°C, thanh lưỡng kim uốn cong 2 mm làm hở tiếp điểm ngắt dòng điện. Biết cứ tăng 10°C thanh uốn cong thêm 0,4 mm. Để rơle tác động ngắt ở độ cong 3,2 mm thì nhiệt độ cần tăng thêm là:", [
                "80°C", "60°C", "100°C", "70°C"
            ], 0, "Δt = (3,2 / 0,4) * 10 = 80°C.")
        ]
    )

    return exams
