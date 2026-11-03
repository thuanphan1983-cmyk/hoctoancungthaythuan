# -*- coding: utf-8 -*-
"""
CHƯƠNG III: KHỐI LƯỢNG RIÊNG VÀ ÁP SUẤT (20 ĐỀ THI ĐỘC LẬP 100%)
- phys8_c3_b13: 3 đề
- phys8_c3_b14: 3 đề
- phys8_c3_b15: 3 đề
- phys8_c3_b16: 3 đề
- phys8_c3_b17: 3 đề
- phys8_c3_rev: 5 đề
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

def get_c3_exams():
    exams = {}
    ch_id = "phys8_c3"
    ch_title = "Chương III: Khối lượng riêng và áp suất"

    def meta(l_id, l_name, t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # Import hoặc ghép b13 đã viết từ make_phys8_c3.py
    from make_phys8_c3 import get_c3_exams as get_b13
    b13_dict = get_b13()
    exams.update(b13_dict)

    # =========================================================================
    # BÀI 14: THỰC HÀNH XÁC ĐỊNH KHỐI LƯỢNG RIÊNG (3 ĐỀ)
    # =========================================================================
    l14_id = "phys8_c3_b14"
    l14_name = "Bài 14: Thực hành xác định khối lượng riêng"

    # --- B14 ĐỀ 1: Đo vật rắn có dạng hình học đều ---
    exams[f"{l14_id}_test1"] = meta(l14_id, l14_name, 1,
        [
            make_mc(1, "Nhận biết", "Dụng cụ dùng để đo khối lượng của vật trong bài thực hành là:", ["Cân điện tử hoặc cân Robecvan", "Bình chia độ", "Thước dây", "Lực kế"], 0, "Cân là dụng cụ đo khối lượng m."),
            make_mc(2, "Nhận biết", "Để xác định thể tích của một khối lập phương bằng kim loại, ta dùng dụng cụ nào?", ["Thước kẻ có độ chia nhỏ nhất phù hợp để đo cạnh", "Cân điện tử", "Bút thử điện", "Nhiệt kế"], 0, "Đo độ dài cạnh rồi tính V = a³."),
            make_mc(3, "Nhận biết", "Công thức tính thể tích khối hộp chữ nhật có ba kích thước a, b, c là:", ["V = a × b × c", "V = a + b + c", "V = 2 × (a + b) × c", "V = (a × b) / c"], 0, "V = a.b.c."),
            make_mc(4, "Nhận biết", "Trước khi cân khối lượng bằng cân điện tử, thao tác quan trọng cần làm là:", ["Bấm nút Tare để đưa chỉ số hiển thị về 0", "Rửa đĩa cân bằng nước", "Lắc mạnh cân", "Tắt nguồn cân"], 0, "Hiệu chỉnh số 0 trước khi đo."),
            make_mc(5, "Nhận biết", "Đơn vị đo thể tích thường in trên các ống đong thí nghiệm là:", ["Mililit (mL)", "Kilôgam (kg)", "Milimét (mm)", "Newton (N)"], 0, "1 mL = 1 cm³."),
            make_mc(6, "Nhận biết", "Trình tự xác định khối lượng riêng của khối gỗ hình hộp chữ nhật là:", ["Đo kích thước tính V, cân khối lượng m, tính D = m/V", "Tính D trước rồi cân m", "Ngâm nước đo V rồi mới cân", "Cân m rồi chia cho chu vi đáy"], 0, "Quy trình đo kích thước, cân khối lượng, tính D."),
            make_mc(7, "Thông hiểu", "Một khối sắt hình lập phương có cạnh đo được 2 cm. Thể tích khối sắt là:", ["8 cm³", "4 cm³", "6 cm³", "2 cm³"], 0, "V = 2³ = 8 cm³."),
            make_mc(8, "Thông hiểu", "Khối nhôm hình hộp chữ nhật có m = 54 g, V = 20 cm³. Khối lượng riêng của nhôm là:", ["2,7 g/cm³", "0,37 g/cm³", "7,4 g/cm³", "27 g/cm³"], 0, "D = 54 / 20 = 2,7 g/cm³."),
            make_mc(9, "Thông hiểu", "Khi đọc số đo trên thước thẳng, đặt mắt nhìn thế nào để tránh sai số thị sai?", ["Vuông góc với cạnh thước tại vạch đọc", "Nghiêng góc 45 độ", "Nhìn từ phía trên xuống", "Nhìn song song mặt thước"], 0, "Đặt mắt vuông góc với vạch đọc."),
            make_mc(10, "Thông hiểu", "Đo ba lần khối lượng một vật được: 24,1 g; 24,0 g; 24,2 g. Giá trị trung bình là:", ["24,1 g", "24,0 g", "24,2 g", "24,3 g"], 0, "(24,1 + 24,0 + 24,2) / 3 = 24,1 g."),
            make_mc(11, "Thông hiểu", "Khối trụ bằng đồng có bán kính r = 1 cm, cao h = 10 cm (cho π ≈ 3,14). Thể tích khối trụ là:", ["31,4 cm³", "62,8 cm³", "15,7 cm³", "3,14 cm³"], 0, "V = 3,14 × 1² × 10 = 31,4 cm³."),
            make_mc(12, "Thông hiểu", "Tại sao không đo thể tích khối gỗ xốp bằng cách thả vào bình chia độ chứa nước?", ["Vì gỗ xốp hút nước và nổi trên mặt nước làm sai lệch kết quả", "Vì gỗ làm nước đóng băng", "Vì bình chia độ sẽ vỡ", "Vì gỗ làm đổi màu nước"], 0, "Vật hút nước và nổi gây sai số lớn.")
        ],
        [
            make_tf(1, "Thông hiểu", "Thí nghiệm đo khối lượng riêng khối hộp kim loại:", [
                ("a", "Dùng thước có ĐCNN mm để đo chiều dài, rộng, cao.", True),
                ("b", "Đo mỗi kích thước nhiều lần lấy trung bình để giảm sai số.", True),
                ("c", "Nếu đo sai một kích thước thì thể tích V vẫn chính xác.", False),
                ("d", "Khối lượng riêng tính theo D = m / (a × b × c).", True)
            ], "Sai lệch kích thước làm sai thể tích."),
            make_tf(2, "Thông hiểu", "Quy tắc an toàn trong phòng thí nghiệm khi dùng cân điện tử:", [
                ("a", "Đặt cân trên mặt bàn phẳng thăng bằng trước khi chỉnh số 0.", True),
                ("b", "Đặt nhẹ nhàng vật mẫu lên đĩa cân.", True),
                ("c", "Có thể đặt vật mẫu ướt sũng nước lên cân không chống nước.", False),
                ("d", "Ghi kết quả đo kèm theo đơn vị đo tương ứng.", True)
            ], "Không để nước ngấm vào cân điện tử."),
            make_tf(3, "Vận dụng", "Khối kim loại hình hộp 5 cm × 4 cm × 2 cm, cân nặng m = 312 g:", [
                ("a", "Thể tích khối kim loại là 40 cm³.", True),
                ("b", "Khối lượng riêng kim loại là 7,8 g/cm³.", True),
                ("c", "Kim loại này có khối lượng riêng bằng nhôm.", False),
                ("d", "Khối lượng riêng theo đơn vị SI là 7 800 kg/m³.", True)
            ], "D = 312 / 40 = 7,8 g/cm³ = 7 800 kg/m³ (sắt)."),
            make_tf(4, "Vận dụng", "Đo khối chì hình lập phương cạnh a = 2,0 cm, khối lượng m = 90,4 g:", [
                ("a", "Thể tích khối chì là 8,0 cm³.", True),
                ("b", "Khối lượng riêng tính được là 11,3 g/cm³.", True),
                ("c", "Khối chì đặc nguyên chất đúng theo số liệu chuẩn.", True),
                ("d", "Cắt khối chì làm đôi thì khối lượng riêng mỗi nửa là 5,65 g/cm³.", False)
            ], "Khối lượng riêng không đổi khi cắt vật.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một khối gỗ lập phương có cạnh dài 5 cm. Thể tích của khối gỗ là bao nhiêu cm³?", "125", "5³ = 125 cm³."),
            make_sa(2, "Thông hiểu", "Cân điện tử chỉ 270 g khi đặt thanh nhôm thể tích 100 cm³. Khối lượng riêng của nhôm là bao nhiêu g/cm³?", "2.7", "270 / 100 = 2,7 g/cm³."),
            make_sa(3, "Vận dụng", "Khối đá hình hộp 40 cm × 25 cm × 10 cm nặng 26 kg. Khối lượng riêng của đá là bao nhiêu kg/m³?", "2600", "V = 0,01 m³ => D = 2 600 kg/m³."),
            make_sa(4, "Vận dụng", "Trụ đồng có bán kính đáy 2 cm, cao 10 cm (cho π ≈ 3,14), D = 8,9 g/cm³. Khối lượng trụ đồng xấp xỉ bao nhiêu gam? (Làm tròn đến hàng đơn vị)", "1118", "m = 8,9 × 3,14 × 4 × 10 ≈ 1 118 g."),
            make_sa(5, "Vận dụng cao", "Đo viên bi thép đường kính d = 2 cm (r = 1 cm). Cho V = 4/3 π r³ (π ≈ 3,14). Bi nặng 32,6 g. Khối lượng riêng của bi là bao nhiêu g/cm³? (Làm tròn 1 chữ số thập phân)", "7.8", "V ≈ 4,187 cm³ => D ≈ 7,8 g/cm³."),
            make_sa(6, "Vận dụng cao", "Hộp kim loại rỗng kích thước ngoài 10 cm × 10 cm × 10 cm, ruột rỗng 8 cm × 8 cm × 8 cm. Hộp nặng 1 903,2 g. Khối lượng riêng kim loại là bao nhiêu g/cm³?", "3.9", "V_vỏ = 1000 - 512 = 488 cm³ => D = 3,9 g/cm³.")
        ],
        [
            make_vdc(1, "Thanh hợp kim nhôm (2,7 g/cm³) và đồng (8,9 g/cm³) có kích thước 10 cm × 5 cm × 2 cm, nặng 840 g. Phần trăm thể tích của nhôm xấp xỉ bằng:", ["8,1%", "12,5%", "25,0%", "45,0%"], 0, "2,7V1 + 8,9(100 - V1) = 840 => V1 ≈ 8,1 cm³ = 8,1%."),
            make_vdc(2, "Xác định bề dày lá nhôm mỏng kích thước 20 cm × 15 cm bằng cách cân m = 4,05 g (D_nhôm = 2,7 g/cm³). Bề dày lá nhôm là:", ["0,05 mm", "0,10 mm", "0,02 mm", "0,50 mm"], 0, "V = 1,5 cm³. S = 300 cm² => h = 1,5 / 300 = 0,005 cm = 0,05 mm."),
            make_vdc(3, "Đúc chi tiết máy bằng thép có thể tích thiết kế 500 cm³. Cân thực tế nặng 3,9 kg (D_thép = 7 800 kg/m³). Kết luận đúng nhất là:", ["Chi tiết máy đặc nguyên khối chuẩn thiết kế", "Bị rỗng 100 cm³", "Bị lẫn nhôm", "Bị nứt vỡ"], 0, "m = 7 800 × 0,0005 = 3,9 kg chuẩn."),
            make_vdc(4, "Đo viên gạch nung thấy D = 1 400 kg/m³ trong khi đất sét nung đặc có D = 2 100 kg/m³. Nguyên nhân là:", ["Gạch có cấu trúc nhiều lỗ xốp chứa không khí", "Thước dãn dài", "Cân bị non", "Nhiệt độ phòng cao"], 0, "Độ xốp bên trong viên gạch.")
        ]
    )

    # --- B14 ĐỀ 2: Đo vật rắn bất kì bằng bình chia độ / bình tràn ---
    exams[f"{l14_id}_test2"] = meta(l14_id, l14_name, 2,
        [
            make_mc(1, "Nhận biết", "Để đo thể tích vật rắn không thấm nước hình dạng bất kì bỏ lọt ống đong, ta dùng:", ["Bình chia độ chứa nước", "Thước dây", "Cân điện tử", "Bình tràn không nước"], 0, "Dùng bình chia độ đo nước dâng."),
            make_mc(2, "Nhận biết", "Thể tích vật rắn V tính theo mức nước ban đầu V1 và sau khi chìm V2 là:", ["V = V2 - V1", "V = V1 + V2", "V = V2 / V1", "V = V1 - V2"], 0, "V = V2 - V1."),
            make_mc(3, "Nhận biết", "Khi thả vật vào bình tràn đầy nước, thể tích của vật bằng:", ["Thể tích nước tràn vào bình chứa", "Thể tích nước còn lại trong bình tràn", "Tổng thể tích hai bình", "Một nửa thể tích nước tràn"], 0, "Thể tích nước tràn đúng bằng V_vật."),
            make_mc(4, "Nhận biết", "Đọc mực nước trong ống đong chuẩn xác tại vị trí:", ["Đáy màng khum lõm ngang tầm mắt", "Mép trên màng khum", "Chính giữa màng khum", "Bất kì điểm nào"], 0, "Đáy màng khum meniscus ngang tầm mắt."),
            make_mc(5, "Nhận biết", "Dụng cụ KHÔNG cần thiết khi đo khối lượng riêng hòn sỏi bằng bình chia độ là:", ["Thước cuộn", "Cân điện tử", "Bình chia độ", "Dây chỉ buộc"], 0, "Không dùng thước cuộn để đo sỏi xù xì."),
            make_mc(6, "Nhận biết", "Nếu vật rắn nổi trên nước (nút bấc), muốn đo thể tích bằng bình chia độ cần:", ["Buộc thêm vật nặng đã biết thể tích để kéo chìm", "Đổ thêm nhiều nước", "Đun sôi nước", "Nghiền nát vật"], 0, "Dùng vật chìm kéo cùng."),
            make_mc(7, "Thông hiểu", "Bình chia độ có 60 cm³ nước. Thả chìm hòn sỏi vào thì nước dâng lên 85 cm³. Thể tích hòn sỏi là:", ["25 cm³", "145 cm³", "85 cm³", "60 cm³"], 0, "85 - 60 = 25 cm³."),
            make_mc(8, "Thông hiểu", "Quả cân đồng nặng 178 g, thả vào bình chia độ nước dâng lên 20 mL. Khối lượng riêng của quả cân là:", ["8,9 g/cm³", "8,0 g/cm³", "7,8 g/cm³", "9,8 g/cm³"], 0, "178 / 20 = 8,9 g/cm³."),
            make_mc(9, "Thông hiểu", "Nếu có bọt khí lớn bám quanh vật khi ngâm vào bình chia độ thì kết quả đo thể tích sẽ:", ["Lớn hơn thể tích thực của vật", "Nhỏ hơn thể tích thực", "Bằng thể tích thực", "Không đổi"], 0, "Bọt khí chiếm thêm thể tích."),
            make_mc(10, "Thông hiểu", "Thả khối kim loại vào bình tràn đầy nước hứng được 40 mL nước tràn. Kim loại nặng 108 g. Đó là kim loại:", ["Nhôm (2,7 g/cm³)", "Sắt (7,8 g/cm³)", "Đồng (8,9 g/cm³)", "Chì (11,3 g/cm³)"], 0, "D = 108 / 40 = 2,7 g/cm³ (Nhôm)."),
            make_mc(11, "Thông hiểu", "Cần lau khô vật rắn trước khi đặt lên cân điện tử để:", ["Tránh làm tăng khối lượng ảo do nước bám", "Làm vật nhỏ hơn", "Làm đổi khối lượng riêng", "Chống nhiễm điện"], 0, "Nước dính làm tăng khối lượng ảo."),
            make_mc(12, "Thông hiểu", "Nếu nhúng ướt vật đo thể tích trước rồi đem cân khối lượng thì D tính ra sẽ:", ["Lớn hơn thực tế", "Nhỏ hơn thực tế", "Hoàn toàn chuẩn", "Bằng 0"], 0, "m bị tăng ảo do nước bám => D tăng.")
        ],
        [
            make_tf(1, "Thông hiểu", "Thao tác đo thể tích bằng bình chia độ:", [
                ("a", "Chọn bình có GHĐ lớn hơn thể tích nước và vật.", True),
                ("b", "Đặt bình thẳng đứng trên bàn nằm ngang.", True),
                ("c", "Đặt mắt nhìn chéo từ trên xuống mặt khum.", False),
                ("d", "Dùng chỉ mảnh buộc vật thả từ từ tránh vỡ bình.", True)
            ], "Tầm mắt phải ngang bằng đáy màng khum."),
            make_tf(2, "Thông hiểu", "Quy trình đo khối lượng riêng hòn đá cuội:", [
                ("a", "Cân khối lượng khi đá hoàn toàn khô ráo.", True),
                ("b", "Lượng nước ban đầu phải đủ ngập hòn đá.", True),
                ("c", "Nếu nước dâng vượt quá GHĐ thì vẫn đọc được chính xác.", False),
                ("d", "Khối lượng riêng bằng khối lượng chia thể tích dâng.", True)
            ], "Vượt GHĐ không đọc được thể tích."),
            make_tf(3, "Vận dụng", "Đo cụm ốc vít sắt: Cân m = 156 g. Nước trong ống đong dâng từ 100 mL lên 120 mL:", [
                ("a", "Thể tích cụm ốc vít là 20 cm³.", True),
                ("b", "Khối lượng riêng tính được là 7,8 g/cm³.", True),
                ("c", "Khối lượng riêng đổi ra SI là 7 800 kg/m³.", True),
                ("d", "Lấy bớt một nửa số ốc vít thì D tính được giảm một nửa.", False)
            ], "D là đặc trưng của chất sắt, không đổi."),
            make_tf(4, "Vận dụng", "Đo thể tích nút gỗ nổi bằng vật chìm: Miếng chì có V = 15 cm³. Nước dâng khi thả chì là từ 60 lên 75 mL. Buộc nút gỗ vào chì thả chìm cả hai thì nước lên 105 mL:", [
                ("a", "Thể tích cả chì và nút gỗ là 45 cm³.", True),
                ("b", "Thể tích nút gỗ là 30 cm³.", True),
                ("c", "Nút gỗ nặng 6 g thì D_gỗ = 0,2 g/cm³.", True),
                ("d", "Nút gỗ có khối lượng riêng lớn hơn nước.", False)
            ], "D_gỗ = 0,2 g/cm³ < 1 g/cm³ nên nút gỗ nổi.")
        ],
        [
            make_sa(1, "Thông hiểu", "Bình có 50 mL nước, thả thỏi kim loại vào nước lên 72 mL. Thể tích thỏi kim loại là bao nhiêu mL?", "22", "72 - 50 = 22 mL."),
            make_sa(2, "Thông hiểu", "Cân hòn đá cuội được 78 g, đo thể tích được 30 cm³. Khối lượng riêng của đá là bao nhiêu g/cm³?", "2.6", "78 / 30 = 2,6 g/cm³."),
            make_sa(3, "Vận dụng", "Khối chì thả vào bình tràn đầy nước làm tràn 50 mL nước. Khối lượng khối chì là bao nhiêu gam (D = 11,3 g/cm³)?", "565", "11,3 × 50 = 565 g."),
            make_sa(4, "Vận dụng", "Mười viên bi thủy tinh nặng 75 g làm nước trong bình chia độ dâng 30 cm³. Khối lượng riêng của thủy tinh là bao nhiêu g/cm³?", "2.5", "75 / 30 = 2,5 g/cm³."),
            make_sa(5, "Vận dụng cao", "Chiếc nhẫn vàng tây nặng 3,75 g làm nước dâng 0,25 cm³. Khối lượng riêng của nhẫn là bao nhiêu g/cm³?", "15", "3,75 / 0,25 = 15 g/cm³."),
            make_sa(6, "Vận dụng cao", "Buộc miếng sáp nến nặng 22,5 g vào quả cân thể tích 10 cm³ thả vào bình chia độ thấy nước tăng từ 60 lên 95 mL. Khối lượng riêng của sáp nến là bao nhiêu g/cm³?", "0.9", "V_sáp = 35 - 10 = 25 cm³ => D = 22,5 / 25 = 0,9 g/cm³.")
        ],
        [
            make_vdc(1, "Mẫu quặng pyrit nặng 200 g thả vào bình tràn hứng được 40 mL nước. Biết pyrit chuẩn có D = 5,0 g/cm³. Mẫu quặng có độ tinh khiết về D đạt:", ["100% chuẩn pyrit nguyên chất", "Chỉ 80%", "120%", "Bị pha tạp nhôm"], 0, "D = 200 / 40 = 5,0 g/cm³ chuẩn."),
            make_vdc(2, "Để đo khối lượng riêng của hạt đỗ xanh nhỏ và nhẹ, phương án thực hành tối ưu là:", ["Đếm 500 hạt cân tổng m rồi thả vào ống đong đo tổng V", "Dùng kính hiển vi", "Luộc chín hạt đỗ", "Nghiền nát hạt đỗ"], 0, "Đo tập hợp số lượng lớn giảm sai số."),
            make_vdc(3, "Thỏi kim loại rỗng nặng 390 g làm nước dâng 80 cm³. Biết làm bằng sắt D = 7,8 g/cm³. Thể tích phần rỗng bên trong thỏi là:", ["30 cm³", "50 cm³", "20 cm³", "40 cm³"], 0, "V_thực = 390 / 7,8 = 50 cm³ => V_rỗng = 80 - 50 = 30 cm³."),
            make_vdc(4, "Muốn đo khối lượng riêng chất lỏng không tan trong nước và nhẹ hơn nước, thao tác nào KHÔNG đo được?", ["Rót trực tiếp vào bình chia độ có sẵn nước để đo mức dâng", "Cân cốc chất lỏng trừ cốc rỗng rồi chia V", "Dùng pipet lấy thể tích rồi cân", "Dùng bình tỉ trọng"], 0, "Chất lỏng hòa lẫn hoặc loang lổ không đo được mức dâng.")
        ]
    )

    # --- B14 ĐỀ 3: Đo khối lượng riêng của chất lỏng ---
    exams[f"{l14_id}_test3"] = meta(l14_id, l14_name, 3,
        [
            make_mc(1, "Nhận biết", "Dụng cụ dùng để đo thể tích chất lỏng trong phòng thí nghiệm là:", ["Ống đong (bình chia độ)", "Thước kẹp", "Cân phân tích", "Lực kế"], 0, "Ống đong đo thể tích chất lỏng."),
            make_mc(2, "Nhận biết", "Muốn đo khối lượng chất lỏng, cách làm đúng nhất là:", ["Cân cốc rỗng m1, rót chất lỏng vào cân m2, tính m = m2 - m1", "Rót chất lỏng trực tiếp lên đĩa cân", "Móc lực kế vào chất lỏng", "Đo thể tích rồi đoán"], 0, "Cân trừ bì: m = m2 - m1."),
            make_mc(3, "Nhận biết", "Nếu thành ống đong bị dính ướt phía trên vạch đọc thể tích thì kết quả:", ["Bị sai số do một phần chất lỏng bám dính thành ống", "Hoàn toàn chuẩn", "Giảm một nửa", "Tăng gấp đôi"], 0, "Chất lỏng dính phía trên không thuộc thể tích đo."),
            make_mc(4, "Nhận biết", "Khối lượng riêng chất lỏng phụ thuộc vào yếu tố nào?", ["Nhiệt độ chất lỏng", "Hình dạng bình chứa", "Chiều cao cột chất lỏng", "Màu sắc bình"], 0, "Nhiệt độ làm chất lỏng dãn nở đổi thể tích."),
            make_mc(5, "Nhận biết", "Dụng cụ chuyên dụng đo nhanh khối lượng riêng chất lỏng trong thực tế là:", ["Tỉ trọng kế (phù kế)", "Áp kế", "Tốc kế", "Nhiệt kế"], 0, "Tỉ trọng kế đo khối lượng riêng chất lỏng."),
            make_mc(6, "Nhận biết", "Đơn vị thể tích 1 lít (L) tương đương với:", ["1 dm³", "1 m³", "100 cm³", "10 cm³"], 0, "1 L = 1 dm³ = 1 000 cm³."),
            make_mc(7, "Thông hiểu", "Cốc thủy tinh rỗng nặng 120 g, rót 100 mL chất lỏng vào thì nặng 200 g. Khối lượng riêng chất lỏng là:", ["0,8 g/cm³", "1,2 g/cm³", "2,0 g/cm³", "1,0 g/cm³"], 0, "m = 80 g => D = 80 / 100 = 0,8 g/cm³."),
            make_mc(8, "Thông hiểu", "Rót 50 mL cồn nặng 40 g. Khối lượng riêng của cồn theo đơn vị SI là:", ["800 kg/m³", "80 kg/m³", "0,8 kg/m³", "8 000 kg/m³"], 0, "D = 40 / 50 = 0,8 g/cm³ = 800 kg/m³."),
            make_mc(9, "Thông hiểu", "Đo 200 mL nước ngọt thấy nặng 216 g. Khối lượng riêng nước ngọt là:", ["1,08 g/cm³", "0,92 g/cm³", "1,00 g/cm³", "1,16 g/cm³"], 0, "D = 216 / 200 = 1,08 g/cm³."),
            make_mc(10, "Thông hiểu", "Dầu ăn có D = 0,8 g/cm³, nước có D = 1,0 g/cm³. Rót dầu ăn vào cốc nước thì:", ["Dầu ăn nổi lên trên mặt nước", "Dầu ăn chìm xuống đáy", "Dầu ăn lơ lửng", "Dầu tan hết vào nước"], 0, "Dầu nhẹ hơn nước và không tan nên nổi."),
            make_mc(11, "Thông hiểu", "Khi rót sữa đặc có đường vào cốc nước, sữa đặc chìm xuống đáy vì:", ["Khối lượng riêng sữa đặc lớn hơn nước", "Sữa đặc lạnh hơn", "Thể tích sữa nhỏ", "Cốc hút sữa"], 0, "D_sữa đặc ≈ 1,3 g/cm³ > 1 g/cm³."),
            make_mc(12, "Thông hiểu", "Lấy 50 cm³ mật ong cân được 71 g. Khối lượng riêng mật ong là:", ["1,42 g/cm³", "1,20 g/cm³", "1,50 g/cm³", "0,70 g/cm³"], 0, "71 / 50 = 1,42 g/cm³.")
        ],
        [
            make_tf(1, "Thông hiểu", "Các bước xác định khối lượng riêng của dầu hỏa:", [
                ("a", "Cân khối lượng m1 của ống đong rỗng sạch, khô.", True),
                ("b", "Rót dầu hỏa vào ống đong, đọc thể tích V.", True),
                ("c", "Cân khối lượng m2 của ống đong chứa dầu.", True),
                ("d", "Khối lượng riêng tính theo công thức D = m2 / V.", False)
            ], "D = (m2 - m1) / V."),
            make_tf(2, "Thông hiểu", "Ảnh hưởng của nhiệt độ tới phép đo khối lượng riêng chất lỏng:", [
                ("a", "Nhiệt độ tăng làm chất lỏng dãn nở tăng thể tích.", True),
                ("b", "Khối lượng chất lỏng không đổi khi tăng nhiệt độ.", True),
                ("c", "Khối lượng riêng của đa số chất lỏng giảm khi nhiệt độ tăng.", True),
                ("d", "Nước đá luôn có khối lượng riêng lớn hơn nước lỏng.", False)
            ], "Nước đá nhẹ hơn nước lỏng nên nổi."),
            make_tf(3, "Vận dụng", "Đo nước biển nhân tạo: Cốc rỗng m1 = 45 g, có 150 mL nước biển cân m2 = 199,5 g:", [
                ("a", "Khối lượng nước biển là 154,5 g.", True),
                ("b", "Khối lượng riêng nước biển là 1,03 g/cm³.", True),
                ("c", "Đổi ra đơn vị SI là 1 030 kg/m³.", True),
                ("d", "Nước cất có khối lượng riêng lớn hơn nước biển này.", False)
            ], "Nước cất D = 1 000 kg/m³ nhỏ hơn nước biển."),
            make_tf(4, "Vận dụng", "Can xăng 20 lít nặng tổng cộng 15,2 kg, vỏ can rỗng nặng 1,2 kg:", [
                ("a", "Lượng xăng trong can nặng 14,0 kg.", True),
                ("b", "Thể tích xăng là 0,02 m³.", True),
                ("c", "Khối lượng riêng của xăng là 700 kg/m³.", True),
                ("d", "Pha thêm nước vào can xăng sẽ làm giảm khối lượng riêng trung bình.", False)
            ], "Nước nặng hơn xăng nên làm tăng D trung bình.")
        ],
        [
            make_sa(1, "Thông hiểu", "Ống đong có 80 mL cồn nặng 64 g. Khối lượng riêng của cồn là bao nhiêu g/cm³?", "0.8", "64 / 80 = 0,8 g/cm³."),
            make_sa(2, "Thông hiểu", "Chai nước chứa 500 mL nước (D = 1 g/cm³). Khối lượng nước trong chai là bao nhiêu gam?", "500", "1 × 500 = 500 g."),
            make_sa(3, "Vận dụng", "Cốc rỗng nặng 50 g, có 100 cm³ dầu thực vật cân nặng 142 g. Khối lượng riêng của dầu là bao nhiêu kg/m³?", "920", "m = 92 g => D = 920 kg/m³."),
            make_sa(4, "Vận dụng", "Bình định mức 250 mL đựng đầy dung dịch axit loãng nặng 300 g. Khối lượng riêng dung dịch là bao nhiêu g/cm³?", "1.2", "300 / 250 = 1,2 g/cm³."),
            make_sa(5, "Vận dụng cao", "Bình đựng đầy thủy ngân (D = 13,6 g/cm³) nặng 730 g, vỏ rỗng nặng 50 g. Dung tích bình là bao nhiêu cm³?", "50", "m = 680 g => V = 680 / 13,6 = 50 cm³."),
            make_sa(6, "Vận dụng cao", "Pha 100 g đường vào 400 g nước cất thu được 460 mL dung dịch nước đường. Khối lượng riêng dung dịch là bao nhiêu g/cm³? (Làm tròn 2 chữ số thập phân)", "1.09", "500 / 460 ≈ 1,09 g/cm³.")
        ],
        [
            make_vdc(1, "Mật ong rừng chuẩn có D từ 1,40 đến 1,44 g/cm³. Cân 2 lít mật ong thấy nặng 2 720 g. Kết luận chuẩn nhất là:", ["D = 1,36 g/cm³ (mật ong đã bị pha nước loãng)", "D = 1,46 g/cm³", "Chuẩn mật ong rừng", "Bị đông đặc"], 0, "D = 2 720 / 2 000 = 1,36 g/cm³ < 1,40 g/cm³ => pha loãng."),
            make_vdc(2, "Mẫu rượu vang có khối lượng riêng 979 kg/m³. Biết D_cồn = 790 kg/m³, D_nước = 1 000 kg/m³. Phần trăm thể tích cồn trong rượu vang là:", ["10%", "12%", "15%", "8%"], 0, "790x + 1000(1-x) = 979 => x = 0,10 = 10%."),
            make_vdc(3, "Bình rỗng nặng 100 g, đầy nước nặng 600 g, đầy chất lỏng X nặng 500 g. Khối lượng riêng của chất lỏng X là:", ["0,8 g/cm³ (800 kg/m³)", "0,9 g/cm³", "1,2 g/cm³", "0,7 g/cm³"], 0, "V = 500 cm³. m_X = 400 g => D = 0,8 g/cm³."),
            make_vdc(4, "Đo khối lượng riêng dung dịch axit H2SO4 trong ắc quy bằng tỉ trọng kế có tác dụng:", ["Đánh giá mức độ tích điện của ắc quy", "Đo nhiệt độ bình", "Đo lượng nước bay hơi", "Làm sạch cực chì"], 0, "Xác định dung lượng điện tích trữ.")
        ]
    )

    # =========================================================================
    # BÀI 15: ÁP SUẤT TRÊN MỘT BỀ MẶT (3 ĐỀ)
    # =========================================================================
    l15_id = "phys8_c3_b15"
    l15_name = "Bài 15: Áp suất trên một bề mặt"

    # --- B15 ĐỀ 1: Khái niệm áp lực & áp suất ---
    exams[f"{l15_id}_test1"] = meta(l15_id, l15_name, 1,
        [
            make_mc(1, "Nhận biết", "Áp lực là:", ["Lực ép có phương vuông góc với mặt bị ép", "Lực kéo song song mặt tiếp xúc", "Trọng lực vật rơi", "Lực ma sát"], 0, "Định nghĩa áp lực."),
            make_mc(2, "Nhận biết", "Áp suất là đại lượng tính bằng:", ["Áp lực trên một đơn vị diện tích bị ép", "Tích áp lực và diện tích", "Thương số diện tích chia áp lực", "Trọng lượng 1 m³ chất"], 0, "p = F / S."),
            make_mc(3, "Nhận biết", "Công thức tính áp suất bề mặt là:", ["p = F / S", "p = F × S", "p = S / F", "p = F - S"], 0, "p = F / S."),
            make_mc(4, "Nhận biết", "Đơn vị đo áp suất trong hệ SI là:", ["Pascal (Pa) hay N/m²", "Newton (N)", "Joule (J)", "Watt (W)"], 0, "1 Pa = 1 N/m²."),
            make_mc(5, "Nhận biết", "1 Pascal (Pa) tương đương với:", ["1 N/m²", "10 N/m²", "100 N/m²", "1 000 N/m²"], 0, "1 Pa = 1 N/m²."),
            make_mc(6, "Nhận biết", "Trường hợp nào lực tác dụng KHÔNG phải áp lực?", ["Lực kéo xe của con ngựa", "Trọng lượng tủ trên sàn", "Ngón tay ấn đinh mũ", "Lưỡi dao đè miếng thịt"], 0, "Lực kéo song song mặt đất không phải áp lực."),
            make_mc(7, "Thông hiểu", "Áp lực 600 N tác dụng lên diện tích 0,03 m² gây ra áp suất:", ["20 000 Pa", "18 Pa", "2 000 Pa", "18 000 Pa"], 0, "600 / 0,03 = 20 000 Pa."),
            make_mc(8, "Thông hiểu", "Người nặng 500 N đứng 2 chân trên sàn, diện tích mỗi bàn chân là 0,0125 m². Áp suất tác dụng lên sàn là:", ["20 000 Pa", "40 000 Pa", "10 000 Pa", "25 000 Pa"], 0, "500 / 0,025 = 20 000 Pa."),
            make_mc(9, "Thông hiểu", "Người chuyển từ đứng 2 chân sang đứng 1 chân thì:", ["Áp lực không đổi nhưng áp suất tăng gấp đôi", "Cả hai đều tăng gấp đôi", "Áp lực tăng gấp đôi", "Cả hai giảm một nửa"], 0, "F không đổi, S giảm một nửa => p tăng gấp đôi."),
            make_mc(10, "Thông hiểu", "Cách nào sau đây làm tăng áp suất lên mặt bị ép?", ["Tăng áp lực đồng thời giảm diện tích tiếp xúc", "Giảm áp lực tăng diện tích", "Chỉ tăng diện tích", "Giảm cả hai cùng tỉ lệ"], 0, "Tăng F và giảm S làm tăng p."),
            make_mc(11, "Thông hiểu", "Xe lu nặng 10 tấn nén lên mặt đường tiếp xúc 0,5 m² (lấy g = 10 m/s²). Áp suất là:", ["200 000 Pa", "20 000 Pa", "50 000 Pa", "100 000 Pa"], 0, "100 000 / 0,5 = 200 000 Pa."),
            make_mc(12, "Thông hiểu", "Đơn vị áp suất 1 Bar bằng bao nhiêu Pascal?", ["100 000 Pa (10⁵ Pa)", "1 000 Pa", "10 000 Pa", "1 000 000 Pa"], 0, "1 bar = 10⁵ Pa.")
        ],
        [
            make_tf(1, "Thông hiểu", "Phân biệt áp lực và áp suất:", [
                ("a", "Áp lực là lực ép vuông góc với mặt tiếp xúc.", True),
                ("b", "Áp suất đặc trưng cho tác dụng làm lún của áp lực.", True),
                ("c", "Hai vật cùng trọng lượng thì luôn tác dụng áp suất bằng nhau.", False),
                ("d", "Áp suất phụ thuộc áp lực và diện tích tiếp xúc.", True)
            ], "Áp suất còn phụ thuộc S."),
            make_tf(2, "Thông hiểu", "Biện pháp thay đổi áp suất trong thực tế:", [
                ("a", "Mài sắc lưỡi kéo để giảm S nhằm tăng áp suất cắt.", True),
                ("b", "Đầu đinh nhọn để tăng áp suất giúp đinh dễ xuyên gỗ.", True),
                ("c", "Móng nhà xây rộng để tăng S làm giảm áp suất chống lún.", True),
                ("d", "Xe tăng lắp bánh xích để tăng áp suất lên bùn lầy.", False)
            ], "Bánh xích giảm áp suất tránh lún bùn."),
            make_tf(3, "Vận dụng", "Khối bê tông lập phương cạnh 0,5 m nặng 300 kg đặt trên sàn (g = 10 m/s²):", [
                ("a", "Áp lực lên sàn là 3 000 N.", True),
                ("b", "Diện tích tiếp xúc là 0,25 m².", True),
                ("c", "Áp suất tác dụng lên sàn là 12 000 Pa.", True),
                ("d", "Chồng thêm một khối y hệt thì áp suất không đổi.", False)
            ], "Chồng thêm thì p tăng gấp đôi (24 000 Pa)."),
            make_tf(4, "Vận dụng", "Người nặng 60 kg đứng trên tuyết chỉ chịu được 15 000 Pa (g = 10 m/s²):", [
                ("a", "Trọng lượng người là 600 N.", True),
                ("b", "Đi giày thường tiếp xúc 0,03 m² thì áp suất là 20 000 Pa.", True),
                ("c", "Người đi giày thường sẽ bị lún xuống tuyết.", True),
                ("d", "Để không lún cần ván trượt diện tích tối thiểu 0,02 m².", False)
            ], "S_min = 600 / 15 000 = 0,04 m².")
        ],
        [
            make_sa(1, "Thông hiểu", "Áp lực 800 N ép lên diện tích 0,04 m². Áp suất tạo ra là bao nhiêu Pascal?", "20000", "800 / 0,04 = 20 000 Pa."),
            make_sa(2, "Thông hiểu", "Khối kim loại gây áp suất 5 000 Pa trên diện tích 0,2 m². Áp lực là bao nhiêu Newton?", "1000", "5 000 × 0,2 = 1 000 N."),
            make_sa(3, "Vận dụng", "Người nặng 54 kg đứng 1 chân tiếp xúc 180 cm² (g = 10 m/s²). Áp suất là bao nhiêu Pa?", "30000", "540 / 0,018 = 30 000 Pa."),
            make_sa(4, "Vận dụng", "Ô tô 4 bánh nặng 1,6 tấn, mỗi bánh tiếp xúc 200 cm² (g = 10 m/s²). Áp suất mỗi bánh là bao nhiêu kPa?", "200", "4 000 / 0,02 = 200 000 Pa = 200 kPa."),
            make_sa(5, "Vận dụng cao", "Đầu nhọn chiếc đinh diện tích 0,1 mm², lực đóng 50 N. Áp suất mũi đinh tác dụng lên gỗ là bao nhiêu MPa?", "500", "50 / 10^-7 = 500 MPa."),
            make_sa(6, "Vận dụng cao", "Máy xúc nặng 80 000 N có 2 bản xích, mỗi bản 2 m × 0,4 m. Áp suất máy xúc lên mặt đất là bao nhiêu kPa?", "50", "80 000 / 1,6 = 50 kPa.")
        ],
        [
            make_vdc(1, "Diễn viên xiếc nặng 60 kg nằm trên 1 200 mũi đinh nhọn, mỗi đinh diện tích 0,5 mm² (g = 10 m/s²). Áp suất tại mỗi đầu đinh là:", ["1 MPa (1 000 000 Pa)", "0,5 MPa", "2 MPa", "10 MPa"], 0, "F_mỗi đinh = 0,5 N => p = 0,5 / (0,5 × 10^-6) = 1 MPa."),
            make_vdc(2, "Viên gạch kích thước 20 cm × 10 cm × 5 cm nặng 2 kg đặt theo các mặt khác nhau. Tỉ số giữa áp suất lớn nhất và nhỏ nhất là:", ["4 lần", "2 lần", "8 lần", "10 lần"], 0, "S_max/S_min = 200 / 50 = 4 lần."),
            make_vdc(3, "Bồn nước trụ đáy bán kính 1 m, nước cao 2 m (D = 1 000 kg/m³, g = 10 m/s²). Bỏ qua vỏ bồn, áp suất đáy bồn lên sàn bê tông là:", ["20 000 Pa", "31 400 Pa", "62 800 Pa", "10 000 Pa"], 0, "p = 10 × 1 000 × 2 = 20 000 Pa."),
            make_vdc(4, "Người phụ nữ 50 kg đi giày cao gót dồn 80% trọng lượng lên 1 gót diện tích 1 cm². Con voi 3 tấn đứng 4 chân mỗi chân 300 cm² (g = 10 m/s²). So sánh áp suất gót giày và chân voi:", ["Gót giày (4 000 000 Pa) gấp 16 lần chân voi (250 000 Pa)", "Chân voi lớn hơn", "Bằng nhau", "Chân voi gấp 10 lần"], 0, "p_gót = 4 000 000 Pa; p_voi = 250 000 Pa => gấp 16 lần.")
        ]
    )

    # --- B15 ĐỀ 2: Ứng dụng tăng/giảm áp suất ---
    exams[f"{l15_id}_test2"] = meta(l15_id, l15_name, 2,
        [
            make_mc(1, "Nhận biết", "Để giảm áp suất lên mặt bị ép, người ta thực hiện:", ["Tăng diện tích tiếp xúc hoặc giảm áp lực", "Giảm diện tích tăng áp lực", "Chỉ giảm diện tích", "Tăng cả hai cùng tỉ lệ"], 0, "Giảm F hoặc tăng S."),
            make_mc(2, "Nhận biết", "Ứng dụng nào sau đây nhằm mục đích LÀM GIẢM áp suất?", ["Kê thanh tà vẹt dưới đường ray xe lửa", "Mài sắc lưỡi dao gọt", "Mũi khoan kim loại nhọn", "Mũi kim khâu mài nhọn"], 0, "Tà vẹt tăng diện tích tiếp xúc giảm áp suất."),
            make_mc(3, "Nhận biết", "Ứng dụng nào sau đây nhằm mục đích LÀM TĂNG áp suất?", ["Đầu mũi dùi, mũi kim khâu mài nhọn", "Xe tải lắp nhiều bánh", "Máy kéo có bản xích rộng", "Lạc đà có đệm chân to bè"], 0, "Mũi nhọn giảm diện tích tăng áp suất."),
            make_mc(4, "Nhận biết", "Kê tấm ván rộng qua mương bùn lầy để đi qua nhằm mục đích:", ["Tăng diện tích tiếp xúc giảm áp suất tránh lún", "Tăng ma sát", "Làm ván nổi", "Để đi nhanh hơn"], 0, "Tăng S giảm áp suất tránh lún."),
            make_mc(5, "Nhận biết", "Đơn vị áp suất N/m² còn gọi là:", ["Pascal (Pa)", "Newton (N)", "Atmotphe (atm)", "Torr"], 0, "1 Pa = 1 N/m²."),
            make_mc(6, "Nhận biết", "Đinh có mũi nhọn còn mũ đinh to nhằm mục đích:", ["Mũi nhọn tăng áp suất vào tường, mũ to giảm áp suất tránh hỏng búa", "Cả hai đều tăng áp suất", "Cả hai đều giảm áp suất", "Để trang trí"], 0, "Mũi nhọn tăng p, mũ to giảm p."),
            make_mc(7, "Thông hiểu", "Khối gỗ nặng 120 N đặt lên bàn diện tích tiếp xúc 0,06 m². Áp suất lên bàn là:", ["2 000 Pa", "7,2 Pa", "720 Pa", "200 Pa"], 0, "120 / 0,06 = 2 000 Pa."),
            make_mc(8, "Thông hiểu", "Máy cày nặng 40 000 N đi trên đất mềm chịu được tối đa 20 000 Pa. Diện tích tiếp xúc tối thiểu là:", ["2 m²", "0,5 m²", "1 m²", "4 m²"], 0, "40 000 / 20 000 = 2 m²."),
            make_mc(9, "Thông hiểu", "Lạc đà đi dễ dàng trên cát sa mạc không bị lún là do:", ["Bàn chân to bè tiếp xúc lớn làm áp suất nhỏ", "Lạc đà rất nhẹ", "Lạc đà chạy nhanh", "Cát sa mạc rất cứng"], 0, "Bàn chân rộng giảm áp suất tránh lún."),
            make_mc(10, "Thông hiểu", "Xe tải nặng 120 000 N có 6 bánh tiếp xúc mỗi bánh 0,04 m². Áp suất mỗi bánh xe là:", ["500 000 Pa", "3 000 000 Pa", "20 000 Pa", "120 000 Pa"], 0, "20 000 / 0,04 = 500 000 Pa."),
            make_mc(11, "Thông hiểu", "Dây quai ba lô học sinh thường bản rộng và có đệm mút vì:", ["Tăng diện tích tiếp xúc với vai làm giảm áp suất đỡ đau vai", "Làm ba lô đẹp", "Để đựng nhiều sách", "Để bền hơn"], 0, "Tăng S giảm áp suất lên vai."),
            make_mc(12, "Thông hiểu", "Cắt bánh chưng bằng sợi lạt dễ hơn dùng bản dao dày vì:", ["Sợi lạt có diện tích tiếp xúc rất nhỏ tạo áp suất cắt lớn", "Lạt có tính chất hóa học", "Lạt ép mạnh hơn dao", "Bánh chưng hút lạt"], 0, "Sợi lạt diện tích nhỏ tạo áp suất cắt lớn.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về tăng giảm áp suất trong đời sống:", [
                ("a", "Răng động vật ăn thịt nhọn sắc để tăng áp suất cắn xé con mồi.", True),
                ("b", "Xe bánh xích chạy được trên cát lún vì áp suất nhỏ hơn xe bánh lốp.", True),
                ("c", "Dao cùn khó cắt gọt vì diện tích tiếp xúc lớn làm giảm áp suất.", True),
                ("d", "Lắp thêm bánh phụ cho xe tải nặng làm tăng áp suất lên mặt đường.", False)
            ], "Lắp thêm bánh làm giảm áp suất lên mặt đường."),
            make_tf(2, "Thông hiểu", "Các yếu tố quyết định độ lún của vật trên bề mặt mềm:", [
                ("a", "Cùng áp lực, vật nào có diện tích tiếp xúc nhỏ hơn sẽ lún sâu hơn.", True),
                ("b", "Cùng diện tích tiếp xúc, áp lực càng lớn lún càng sâu.", True),
                ("c", "Độ lún chỉ phụ thuộc vào trọng lượng vật, không phụ thuộc diện tích.", False),
                ("d", "Áp suất là đại lượng đặc trưng cho tác dụng làm lún bề mặt.", True)
            ], "Độ lún phụ thuộc vào áp suất p = F/S."),
            make_tf(3, "Vận dụng", "Máy kéo bánh xích nặng 50 000 N có diện tích tiếp xúc hai dải xích là 1,25 m²:", [
                ("a", "Áp suất máy kéo tác dụng lên mặt đất là 40 000 Pa.", True),
                ("b", "Một ô tô nặng 20 000 N có 4 bánh tiếp xúc 0,05 m² gây áp suất 400 000 Pa.", True),
                ("c", "Máy kéo nặng hơn ô tô nên gây áp suất lên mặt đất lớn hơn ô tô.", False),
                ("d", "Máy kéo di chuyển trên nền đất yếu tốt hơn ô tô con.", True)
            ], "Áp suất máy kéo (40 000 Pa) nhỏ hơn nhiều ô tô (400 000 Pa)."),
            make_tf(4, "Vận dụng", "Khối sắt hình hộp chữ nhật kích thước 20 cm × 10 cm × 5 cm (D = 7 800 kg/m³, g = 10 m/s²):", [
                ("a", "Thể tích khối sắt là 0,001 m³.", True),
                ("b", "Trọng lượng khối sắt là 78 N.", True),
                ("c", "Đặt mặt 20 cm × 10 cm xuống sàn thì áp suất là 3 900 Pa.", True),
                ("d", "Đặt mặt 10 cm × 5 cm xuống sàn thì áp suất là 7 800 Pa.", False)
            ], "Đặt mặt 10×5 (0,005 m²) thì p = 78 / 0,005 = 15 600 Pa.")
        ],
        [
            make_sa(1, "Thông hiểu", "Đổi áp suất 25 kPa sang đơn vị Pascal (Pa) được bao nhiêu Pa?", "25000", "25 × 1 000 = 25 000 Pa."),
            make_sa(2, "Thông hiểu", "Một mũi khoan có diện tích đầu nhọn 0,2 mm² chịu lực ép 40 N. Áp suất mũi khoan là bao nhiêu MPa?", "200", "40 / (0,2 × 10^-6) = 200 MPa."),
            make_sa(3, "Vận dụng", "Xe tải có trọng lượng 80 000 N, bánh xe truyền lên đường áp suất 400 000 Pa. Tổng diện tích tiếp xúc các bánh xe là bao nhiêu m²?", "0.2", "S = 80 000 / 400 000 = 0,2 m²."),
            make_sa(4, "Vận dụng", "Chiếc ghế 4 chân nặng 40 N, người ngồi nặng 560 N. Mỗi chân ghế tiếp xúc sàn 10 cm² (g = 10 m/s²). Áp suất mỗi chân ghế lên sàn là bao nhiêu kPa?", "150", "F_mỗi chân = 600 / 4 = 150 N. p = 150 / 0,001 = 150 kPa."),
            make_sa(5, "Vận dụng cao", "Tác dụng lực F vuông góc lên mũ đinh có diện tích 0,5 cm² tạo áp suất 60 000 Pa. Mũi đinh nhọn 0,05 mm² cắm vào gỗ sẽ gây ra áp suất bao nhiêu MPa?", "600", "F = 60 000 × 0,00005 = 3 N. p_mũi = 3 / (0,05 × 10^-6) = 600 MPa."),
            make_sa(6, "Vận dụng cao", "Tàu hỏa chạy trên đường ray nặng 2 400 tấn, có 80 bánh xe. Biết ray kê trên tà vẹt truyền áp suất xuống nền đá là 150 kPa trên tổng diện tích tà vẹt 160 m² (g = 10 m/s²). Lực ép toàn bộ tàu hỏa lên nền đá là bao nhiêu triệu Newton (MN)?", "24", "F = 24 000 000 N = 24 MN.")
        ],
        [
            make_vdc(1, "Bảng phi tiêu có mũi kim cắm sâu vào bia gỗ. Dù lực phóng tay chỉ khoảng 10 N nhưng mũi phi tiêu vẫn cắm ngập vào thớ gỗ cứng là vì:", ["Đầu mũi phi tiêu siêu nhọn diện tích cỡ 0,01 mm² tạo áp suất lên tới hàng nghìn MPa xé rách thớ gỗ", "Phi tiêu mang điện tích", "Gỗ hút phi tiêu", "Không khí đẩy mũi phi tiêu"], 0, "p = F/S cực lớn ở đầu nhọn."),
            make_vdc(2, "Để cứu một người bị rơi xuống hố băng tuyết nứt mỏng, người cứu hộ không nên chạy thẳng tới mà phải nằm trườn bò trên mặt băng tuyết vì:", ["Nằm trườn làm tăng tối đa diện tích tiếp xúc S giúp giảm áp suất phân tán trọng lượng tránh làm vỡ thêm băng", "Để tránh gió lạnh", "Để băng không nhận ra người", "Để nhìn rõ người bị nạn"], 0, "Tăng S giảm áp suất chống sập vỡ băng."),
            make_vdc(3, "Một cột trụ bê tông hình lăng trụ đứng đáy diện tích S, cao h làm bằng bê tông có khối lượng riêng D (gia tốc g). Áp suất do cột trụ gây ra lên mặt móng được xác định bằng công thức độc lập với diện tích đáy là:", ["p = 10 × D × h", "p = 10 × D / h", "p = D × h / 10", "p = 10 × D × S"], 0, "F = P = 10D.V = 10D.S.h => p = F/S = 10Dh."),
            make_vdc(4, "Một người muốn mua máy nén khí cho gara rửa xe ô tô nâng cầu nâng tải trọng 4 tấn (40 000 N). Pit-tông nâng có đường kính 20 cm (diện tích S xấp xỉ 0,0314 m²). Áp suất khí nén tối thiểu mà máy nén khí cần tạo ra là:", ["Khoảng 1 274 kPa (12,74 bar)", "Khoảng 127 kPa", "Khoảng 400 kPa", "Khoảng 2 500 kPa"], 0, "p = 40 000 / 0,0314 ≈ 1 273 885 Pa ≈ 1 274 kPa.")
        ]
    )

    # --- B15 ĐỀ 3: Bài toán định lượng và áp suất đa chiều ---
    exams[f"{l15_id}_test3"] = meta(l15_id, l15_name, 3,
        [
            make_mc(1, "Nhận biết", "Yếu tố nào sau đây quyết định áp suất của vật lên mặt đỡ?", ["Áp lực và diện tích mặt bị ép", "Chỉ có khối lượng của vật", "Chỉ có thể tích của vật", "Màu sắc và hình dạng vật"], 0, "p = F/S."),
            make_mc(2, "Nhận biết", "Khi diện tích bị ép giảm đi một nửa còn áp lực giữ nguyên thì áp suất:", ["Tăng gấp đôi", "Giảm đi một nửa", "Không đổi", "Tăng 4 lần"], 0, "p' = F / (S/2) = 2p."),
            make_mc(3, "Nhận biết", "Đơn vị đo áp suất trong ngành khí tượng thường dùng là:", ["hPa (Hectopascal) hoặc mmHg", "kg/m³", "Joule", "m/s"], 0, "1 hPa = 100 Pa."),
            make_mc(4, "Nhận biết", "Một khối lập phương đặt trên sàn, nếu tăng chiều dài mỗi cạnh lên gấp đôi thì áp suất lên sàn sẽ:", ["Tăng gấp đôi", "Tăng 4 lần", "Tăng 8 lần", "Không đổi"], 0, "m tăng 8 lần, S tăng 4 lần => p = F/S tăng 2 lần."),
            make_mc(5, "Nhận biết", "Tại sao mũi kim khâu nhọn hoắt nhưng đuôi kim lại có lỗ xỏ chỉ to bè?", ["Mũi kim giảm S để tăng p xuyên vải, đuôi to để xỏ chỉ và ấn tay không bị đau", "Cả hai đều tăng áp suất", "Để kim không bị gãy", "Để trang trí"], 0, "Đuôi to giảm áp suất ngón tay ấn."),
            make_mc(6, "Nhận biết", "Hiện tượng ván trượt tuyết giúp vận động viên lướt trên tuyết xốp là nhờ:", ["Tấm ván dài rộng làm tăng diện tích tiếp xúc giảm áp suất tránh lún tuyết", "Ván trượt tự phát nhiệt", "Tuyết đẩy ván", "Ván không có trọng lượng"], 0, "Tăng S giảm áp suất."),
            make_mc(7, "Thông hiểu", "Một bao xi măng nặng 50 kg đặt trên sàn có diện tích đáy 0,25 m² (g = 10 m/s²). Áp suất là:", ["2 000 Pa", "500 Pa", "125 Pa", "200 Pa"], 0, "500 / 0,25 = 2 000 Pa."),
            make_mc(8, "Thông hiểu", "Đặt một cuốn sách nặng 6 N lên mặt bàn, diện tích bìa tiếp xúc là 0,03 m². Áp suất cuốn sách là:", ["200 Pa", "18 Pa", "20 Pa", "180 Pa"], 0, "6 / 0,03 = 200 Pa."),
            make_mc(9, "Thông hiểu", "Nếu đặt chồng 3 cuốn sách giống hệt nhau lên nhau thì áp suất cuốn dưới cùng tác dụng lên bàn:", ["Tăng gấp 3 lần", "Không đổi", "Giảm 3 lần", "Tăng 9 lần"], 0, "F tăng 3 lần, S không đổi => p tăng 3 lần."),
            make_mc(10, "Thông hiểu", "Một tượng đá nặng 5 200 N đặt trên bệ đỡ diện tích 0,4 m². Áp suất tượng lên bệ đỡ là:", ["13 000 Pa", "2 080 Pa", "1 300 Pa", "20 800 Pa"], 0, "5 200 / 0,4 = 13 000 Pa."),
            make_mc(11, "Thông hiểu", "Để tránh xe chở hàng nặng làm nứt gãy mặt đường nhựa mùa hè, người ta quy định:", ["Giới hạn tải trọng trục xe (áp lực trên mỗi bánh xe)", "Xe phải chạy thật nhanh", "Bơm lốp thật căng", "Xe chỉ chạy ban đêm"], 0, "Hạn chế tải trọng trục xe để giới hạn áp suất."),
            make_mc(12, "Thông hiểu", "Dụng cụ đóng cọc bê tông móng nhà có đầu búa rất nặng và rơi từ trên cao nhằm:", ["Tạo áp lực cực lớn tác dụng lên đầu cọc sinh áp suất nén cọc sâu vào đất", "Làm nóng cọc", "Giảm ma sát", "Làm đẹp cọc"], 0, "Tăng áp lực F sinh áp suất lớn đóng cọc.")
        ],
        [
            make_tf(1, "Thông hiểu", "So sánh áp suất của các vật thể trong đời sống:", [
                ("a", "Áp suất chân bàn 4 chân tác dụng lên sàn phụ thuộc tổng diện tích 4 chân.", True),
                ("b", "Bàn chân người đứng thẳng gây áp suất nhỏ hơn khi đi nhón chân trên đầu ngón.", True),
                ("c", "Dao cắt gọt sắc bén vì áp lực tay tác dụng lên dao luôn lớn hơn búa tạ.", False),
                ("d", "Xe lu san mặt đường có áp suất lớn để nén chặt đất đá.", True)
            ], "Dao sắc bén do diện tích lưỡi dao cực nhỏ, không phải do F lớn hơn búa."),
            make_tf(2, "Thông hiểu", "Ảnh hưởng của diện tích tiếp xúc trong công trình xây dựng:", [
                ("a", "Móng đơn, móng băng có bản đế rộng để giảm áp suất truyền xuống nền đất.", True),
                ("b", "Nền đất sét yếu chịu áp suất nhỏ hơn nền đá granit cứng.", True),
                ("c", "Nhà càng nhiều tầng thì móng nhà càng phải thiết kế diện tích đáy lớn hơn.", True),
                ("d", "Áp suất móng nhà truyền xuống đất không phụ thuộc trọng lượng tòa nhà.", False)
            ], "Áp suất tỉ lệ thuận với tổng trọng lượng tòa nhà."),
            make_tf(3, "Vận dụng", "Khối đồng chất hình hộp chữ nhật kích thước 40 cm × 20 cm × 10 cm, khối lượng riêng D = 2 500 kg/m³ (g = 10 m/s²):", [
                ("a", "Thể tích khối hộp là 0,008 m³.", True),
                ("b", "Trọng lượng khối hộp là 200 N.", True),
                ("c", "Áp suất nhỏ nhất khi đặt mặt 40 cm × 20 cm là 2 500 Pa.", True),
                ("d", "Áp suất lớn nhất khi đặt mặt 20 cm × 10 cm là 5 000 Pa.", False)
            ], "S_min = 0,2 × 0,1 = 0,02 m² => p_max = 200 / 0,02 = 10 000 Pa."),
            make_tf(4, "Vận dụng", "Một xe container 18 bánh có tổng khối lượng 36 tấn. Mỗi bánh xe có diện tích tiếp xúc mặt đường là 250 cm² (g = 10 m/s²):", [
                ("a", "Tổng trọng lượng xe và hàng là 360 000 N.", True),
                ("b", "Mỗi bánh xe chịu áp lực trung bình là 20 000 N.", True),
                ("c", "Áp suất mỗi bánh xe tác dụng lên mặt đường là 800 000 Pa.", True),
                ("d", "Nếu giảm bớt 9 bánh xe thì áp suất mỗi bánh xe còn lại sẽ giảm đi.", False)
            ], "Giảm số bánh xe thì mỗi bánh còn lại phải gánh áp lực lớn hơn nên áp suất tăng.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một chiếc bàn nặng 160 N có 4 chân, mỗi chân tiếp xúc sàn 0,002 m². Áp suất mỗi chân bàn là bao nhiêu kPa?", "20", "F = 40 N => p = 40 / 0,002 = 20 000 Pa = 20 kPa."),
            make_sa(2, "Thông hiểu", "Áp suất 150 kPa tương đương với bao nhiêu N/m²?", "150000", "150 × 1 000 = 150 000 N/m²."),
            make_sa(3, "Vận dụng", "Một thỏi chì hình hộp 10 cm × 5 cm × 2 cm (D = 11,3 g/cm³, g = 10 m/s²). Trọng lượng thỏi chì là bao nhiêu Newton? (Làm tròn 2 chữ số thập phân)", "11.3", "V = 100 cm³ => m = 1,13 kg => P = 11,3 N."),
            make_sa(4, "Vận dụng", "Một khối trụ sắt cao 1 m, D = 7 800 kg/m³ đặt thẳng đứng trên sàn (g = 10 m/s²). Áp suất khối sắt tác dụng lên sàn là bao nhiêu kPa?", "78", "p = 10Dh = 10 × 7 800 × 1 = 78 000 Pa = 78 kPa."),
            make_sa(5, "Vận dụng cao", "Người nặng 68 kg đứng trên sàn 2 chân tiếp xúc 0,034 m² (g = 10 m/s²). Cầm thêm bao gạo 50 kg thì áp suất người đó lên sàn là bao nhiêu kPa?", "34.7", "F = (68 + 50) × 10 = 1 180 N. p = 1 180 / 0,034 ≈ 34,7 kPa."),
            make_sa(6, "Vận dụng cao", "Móng nhà hình vuông chịu tải 800 kN. Nền đất chỉ chịu được 200 kPa. Chiều dài tối thiểu mỗi cạnh móng vuông là bao nhiêu mét?", "2", "S = 800 / 200 = 4 m² => cạnh a = 2 m.")
        ],
        [
            make_vdc(1, "Một khối lập phương đặc bằng đồng chất đặt trên bàn phẳng gây áp suất p0. Nếu gọt bớt khối lập phương này chỉ còn một nửa kích thước cạnh ban đầu thì áp suất của khối mới tác dụng lên bàn sẽ:", ["Bằng một nửa p0 (p = p0 / 2)", "Bằng p0", "Bằng p0 / 4", "Bằng 2 p0"], 0, "p = 10.D.a => a giảm một nửa thì p giảm một nửa."),
            make_vdc(2, "Khi thiết kế đường hầm dưới lòng đất hoặc hầm mỏ than, các thanh vì kèo chống vòm hầm thường có đệm chân đế bản thép rất rộng kê trên nền đá. Mục đích kỹ thuật cốt lõi là:", ["Phân tán áp lực khổng lồ của tầng đất đá bên trên lên diện tích tiếp xúc rộng giúp giảm áp suất chống sụt lún chân vì kèo vào nền hầm", "Để chống nước ngầm", "Để tránh ma sát", "Để trang trí đường hầm"], 0, "Tăng diện tích tiếp xúc giảm áp suất chống lún vì kèo."),
            make_vdc(3, "Một ô tô 4 bánh chạy trên đường cao tốc với áp suất lốp xe tiêu chuẩn là 2,2 bar (220 000 Pa). Biết tổng khối lượng ô tô là 1,54 tấn (g = 10 m/s²). Tổng diện tích tiếp xúc của cả 4 bánh xe với mặt đường là:", ["0,07 m² (700 cm²)", "0,035 m²", "0,14 m²", "0,28 m²"], 0, "F = 15 400 N. S = 15 400 / 220 000 = 0,07 m²."),
            make_vdc(4, "Một tảng đá hoa cương hình nón có chiều cao h, khối lượng riêng D đặt đứng trên đáy tròn bán kính R (g = 10 m/s²). Biết thể tích hình nón V = 1/3 π R² h. Áp suất tảng đá hình nón tác dụng lên mặt sàn bê tông bằng:", ["p = 10/3 × D × h", "p = 10 × D × h", "p = 10 × D × R", "p = 5 × D × h"], 0, "F = 10 × D × 1/3 π R² h. S = π R² => p = F/S = 10/3 D h.")
        ]
    )

    return exams
