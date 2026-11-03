# -*- coding: utf-8 -*-
"""
CHƯƠNG IV: TÁC DỤNG LÀM QUAY CỦA LỰC (11 ĐỀ THI ĐỘC LẬP 100%)
- phys8_c4_b18: 3 đề
- phys8_c4_b19: 3 đề
- phys8_c4_rev: 5 đề
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

def get_c4_exams():
    exams = {}
    ch_id = "phys8_c4"
    ch_title = "Chương IV: Tác dụng làm quay của lực"

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
    # BÀI 18: TÁC DỤNG LÀM QUAY CỦA LỰC. MOMENT LỰC (3 ĐỀ)
    # =========================================================================
    l18_id = "phys8_c4_b18"
    l18_name = "Bài 18: Tác dụng làm quay của lực. Moment lực"

    # --- B18 ĐỀ 1 ---
    exams[f"{l18_id}_test1"] = meta(l18_id, l18_name, 1,
        [
            make_mc(1, "Nhận biết", "Tác dụng làm quay của lực lên vật quanh một trục được đặc trưng bởi:", ["Moment lực", "Khối lượng", "Vận tốc", "Quán tính"], 0, "Moment lực M = F.d."),
            make_mc(2, "Nhận biết", "Công thức tính moment lực M là:", ["M = F × d", "M = F / d", "M = d / F", "M = F + d"], 0, "M = F.d."),
            make_mc(3, "Nhận biết", "Đơn vị chuẩn của moment lực trong hệ SI là:", ["N.m (Newton mét)", "N/m", "Joule", "Watt"], 0, "Đơn vị là N.m."),
            make_mc(4, "Nhận biết", "Cánh tay đòn d của lực là khoảng cách:", ["Vuông góc từ trục quay đến giá của lực", "Từ điểm đặt lực đến trục quay", "Hai đầu vật", "Mặt đất đến lực"], 0, "Khoảng cách vuông góc từ trục quay đến giá của lực."),
            make_mc(5, "Nhận biết", "Lực tác dụng KHÔNG có tác dụng làm quay khi giá của lực:", ["Đi qua trục quay hoặc song song với trục quay", "Vuông góc với trục quay", "Ở xa trục quay", "Tiếp tuyến với quỹ đạo"], 0, "Cắt trục quay hoặc song song trục quay thì M = 0."),
            make_mc(6, "Nhận biết", "Để mở cánh cửa gỗ dễ dàng nhất, nên đặt tay nắm cửa ở:", ["Mép ngoài xa bản lề nhất", "Sát gần bản lề", "Chính giữa bản lề", "Vị trí nào cũng như nhau"], 0, "Càng xa trục quay thì d càng lớn, lực mở F càng nhỏ."),
            make_mc(7, "Thông hiểu", "Tác dụng lực F = 20 N vào cờ-lê có cánh tay đòn d = 0,25 m để vặn ốc. Moment lực là:", ["5 N.m", "20 N.m", "80 N.m", "2,5 N.m"], 0, "20 × 0,25 = 5 N.m."),
            make_mc(8, "Thông hiểu", "Cần moment 12 N.m để vặn bu lông bằng cờ-lê dài 0,3 m. Lực tác dụng vuông góc tối thiểu là:", ["40 N", "3,6 N", "36 N", "120 N"], 0, "F = 12 / 0,3 = 40 N."),
            make_mc(9, "Thông hiểu", "Khi vặn van khóa nước hình vô-lăng tròn bằng hai tay ngược chiều, ta tạo ra:", ["Một ngẫu lực làm van quay êm ái", "Hai lực triệt tiêu nhau", "Lực kéo van ra", "Lực nén van"], 0, "Ngẫu lực làm vật quay quanh trục."),
            make_mc(10, "Thông hiểu", "Nếu lực tác dụng tăng gấp đôi và cánh tay đòn giảm một nửa thì moment lực:", ["Không đổi", "Tăng gấp đôi", "Giảm một nửa", "Tăng 4 lần"], 0, "M' = 2F × d/2 = F.d."),
            make_mc(11, "Thông hiểu", "Người thợ thường nối dài cán cờ-lê bằng một đoạn ống tuýp thép để:", ["Tăng cánh tay đòn tạo moment quay lớn với lực vừa phải", "Để cờ-lê không gãy", "Để cầm đỡ đau tay", "Để giảm ma sát"], 0, "Tăng d làm tăng M = F.d."),
            make_mc(12, "Thông hiểu", "Trường hợp nào lực tác dụng có moment lực lớn nhất?", ["Lực 30 N với cánh tay đòn 0,4 m", "Lực 20 N với d = 0,5 m", "Lực 50 N với d = 0,2 m", "Lực 100 N đi qua trục quay"], 0, "30 × 0,4 = 12 N.m (lớn nhất).")
        ],
        [
            make_tf(1, "Thông hiểu", "Về moment lực đối với trục quay cố định:", [
                ("a", "Moment lực đặc trưng cho tác dụng làm quay của lực quanh trục.", True),
                ("b", "Lực càng lớn và cánh tay đòn càng dài thì tác dụng làm quay càng mạnh.", True),
                ("c", "Cánh tay đòn luôn luôn bằng khoảng cách từ trục quay đến điểm đặt lực.", False),
                ("d", "Lực có phương cắt trục quay thì moment lực bằng 0.", True)
            ], "Cánh tay đòn là khoảng cách vuông góc từ trục quay đến giá của lực."),
            make_tf(2, "Thông hiểu", "Ứng dụng moment lực trong thực tế:", [
                ("a", "Vặn ốc bằng cờ-lê dài nhẹ hơn cờ-lê ngắn.", True),
                ("b", "Tay nắm cửa sổ đặt xa trục quay bản lề giúp đóng mở nhẹ nhàng.", True),
                ("c", "Vô-lăng lái ô tô đường kính càng lớn thì xoay càng nhẹ.", True),
                ("d", "Đẩy cánh cửa ở vị trí sát bản lề giúp mở cửa dễ nhất.", False)
            ], "Sát bản lề d nhỏ nên mở rất nặng."),
            make_tf(3, "Vận dụng", "Cần chắn đường sắt dài 6 m quay quanh trục O cách đầu A 1 m và cách đầu B 5 m:", [
                ("a", "Đầu B là cần chắn đường sắt vươn ra ngoài.", True),
                ("b", "Khối đối trọng nặng được gắn ở đầu ngắn A.", True),
                ("c", "Khối đối trọng ở A tạo moment lực ngược chiều với cần chắn ở B.", True),
                ("d", "Bỏ khối đối trọng thì cần chắn sẽ tự dựng đứng lên.", False)
            ], "Bỏ đối trọng thì đầu B nặng hơn kéo cần sập xuống."),
            make_tf(4, "Vận dụng", "Tác dụng lực F = 60 N vuông góc vào cờ-lê dài 25 cm (0,25 m) mở ốc xe tải:", [
                ("a", "Moment của lực tác dụng là 15 N.m.", True),
                ("b", "Nối thêm ống dài 50 cm (tổng dài 75 cm) thì moment lực là 45 N.m.", True),
                ("c", "Nối dài cờ-lê giúp tăng moment quay làm việc mở ốc dễ dàng hơn.", True),
                ("d", "Dùng cờ-lê dài hơn giúp người thợ được lợi về công cơ học.", False)
            ], "Không máy cơ nào cho ta lợi về công.")
        ],
        [
            make_sa(1, "Thông hiểu", "Lực 40 N vuông góc với cánh tay đòn 0,3 m tạo moment lực bao nhiêu N.m?", "12", "40 × 0,3 = 12 N.m."),
            make_sa(2, "Thông hiểu", "Cần moment 25 N.m mở van bằng cánh tay đòn 0,5 m. Lực tác dụng vuông góc là bao nhiêu Newton?", "50", "25 / 0,5 = 50 N."),
            make_sa(3, "Vận dụng", "Tay vặn van chữ T có 2 nhánh mỗi nhánh dài 20 cm. Mỗi tay tác dụng lực 30 N vuông góc tạo ngẫu lực vặn. Tổng moment là bao nhiêu N.m?", "12", "30 × 0,4 = 12 N.m."),
            make_sa(4, "Vận dụng", "Cánh cửa rộng 0,8 m. Lực đẩy vuông góc mép ngoài cửa là 25 N. Moment lực đối với bản lề là bao nhiêu N.m?", "20", "25 × 0,8 = 20 N.m."),
            make_sa(5, "Vận dụng cao", "Lực F = 80 N tác dụng vào thanh cách O một đoạn 0,5 m, hợp góc 30 độ với thanh (sin 30° = 0,5). Moment lực đối với O là bao nhiêu N.m?", "20", "80 × 0,5 × 0,5 = 20 N.m."),
            make_sa(6, "Vận dụng cao", "Để mở đai ốc cần moment 300 N.m. Người thợ dùng cờ-lê dài 0,6 m. Khối lượng tối thiểu của người dẫm lên đầu cờ-lê là bao nhiêu kg? (g = 10 m/s²)", "50", "F = 300 / 0,6 = 500 N => m = 50 kg.")
        ],
        [
            make_vdc(1, "Khi dùng cờ-lê dài 30 cm, tác dụng lực F = 100 N xiên góc 60 độ so với cán cờ-lê thay vì vuông góc 90 độ (sin 60° ≈ 0,866). Moment lực khi tác dụng góc 60 độ là:", ["26 N.m (khoảng 86,6% so với lực vuông góc 30 N.m)", "30 N.m", "15 N.m", "20 N.m"], 0, "M = 100 × 0,3 × sin 60° ≈ 25,98 N.m ≈ 26 N.m."),
            make_vdc(2, "Bàn đạp phanh chân ô tô có cần đạp dài giúp tài xế phanh xe ăn chắc nhẹ nhàng là nhờ:", ["Tăng cánh tay đòn d để tạo moment lực lớn với lực đạp chân vừa phải", "Bàn đạp có động cơ kéo", "Bàn đạp bằng nhựa nhẹ", "Giảm ma sát"], 0, "Tối ưu hóa cánh tay đòn tăng moment lực."),
            make_vdc(3, "Cánh quạt gió phong điện dài 60 m vẫn quay được khi gió thổi nhẹ phân bố đều là nhờ:", ["Cánh dài tạo cánh tay đòn khổng lồ sinh ra moment lực rất lớn thắng ma sát trục quay", "Gió trên cao không trọng lượng", "Cánh tự quay", "Ma sát bằng 0"], 0, "Cánh tay đòn lớn tạo moment quay lớn."),
            make_vdc(4, "Một người nâng quả tạ 10 kg trên bàn tay nằm ngang, cẳng tay dài 35 cm vuông góc bắp tay (g = 10 m/s²). Moment trọng lượng quả tạ đối với khớp khuỷu tay là:", ["35 N.m", "350 N.m", "3,5 N.m", "35 000 N.m"], 0, "P = 100 N. d = 0,35 m => M = 100 × 0,35 = 35 N.m.")
        ]
    )

    # --- B18 ĐỀ 2 ---
    exams[f"{l18_id}_test2"] = meta(l18_id, l18_name, 2,
        [
            make_mc(1, "Nhận biết", "Điều kiện cân bằng của vật có trục quay cố định là:", ["Tổng các moment lực làm vật quay theo chiều kim đồng hồ bằng tổng các moment ngược chiều", "Lực bên trái bằng bên phải", "Tổng các lực bằng 0", "Không có lực tác dụng"], 0, "Quy tắc moment: ΣM_thuận = ΣM_nghược."),
            make_mc(2, "Nhận biết", "Quy tắc moment lực áp dụng cho:", ["Vật có trục quay cố định hoặc trục quay tạm thời", "Chỉ vật đứng yên", "Chỉ chất lỏng", "Chỉ quả cầu"], 0, "Áp dụng cho mọi vật có trục quay."),
            make_mc(3, "Nhận biết", "Đơn vị đo của moment lực N.m trong thực tế:", ["Giữ nguyên là Newton mét (N.m), không gọi là Joule", "Được gọi là Watt", "Được gọi là Pascal", "Được gọi là Calo"], 0, "Quy ước đơn vị moment là N.m."),
            make_mc(4, "Nhận biết", "Hai bạn chơi bập bênh cân bằng. Bạn nặng hơn phải ngồi:", ["Gần trục quay hơn bạn nhẹ cân", "Xa trục quay hơn", "Đứng lên", "Ngồi đâu cũng được"], 0, "P1.d1 = P2.d2: P lớn thì d nhỏ."),
            make_mc(5, "Nhận biết", "Khi vật quay đều quanh trục quay cố định thì:", ["Tổng moment lực phát động cân bằng với tổng moment lực cản", "Lực phát động lớn hơn", "Không có ma sát", "Lực cản bằng 0"], 0, "Quay đều: tổng moment triệt tiêu."),
            make_mc(6, "Nhận biết", "Dụng cụ hoạt động dựa trên quy tắc cân bằng moment lực là:", ["Cân đòn Robecvan", "Nhiệt kế", "Kính lúp", "Áp kế"], 0, "Cân đòn Robecvan."),
            make_mc(7, "Thông hiểu", "Đòn bẩy thăng bằng quanh O: F1 = 10 N có d1 = 40 cm. Lực F2 có d2 = 20 cm thì F2 bằng:", ["20 N", "5 N", "10 N", "40 N"], 0, "10 × 40 / 20 = 20 N."),
            make_mc(8, "Thông hiểu", "Bạn Nam 40 kg ngồi cách trục bập bênh 1,5 m. Bạn Bình 30 kg muốn thăng bằng phải ngồi cách trục:", ["2,0 m", "1,8 m", "1,2 m", "2,5 m"], 0, "40 × 1,5 / 30 = 2,0 m."),
            make_mc(9, "Thông hiểu", "Thanh nhẹ quay quanh O. Lực F1 = 15 N cách O 0,2 m làm quay thuận chiều. Cần F2 = 10 N ngược chiều cách O một khoảng:", ["0,3 m (30 cm)", "0,15 m", "0,2 m", "0,4 m"], 0, "15 × 0,2 / 10 = 0,3 m."),
            make_mc(10, "Thông hiểu", "Trọng tâm của thước dẹt đồng chất dài 100 cm nằm ở:", ["Chính giữa thước cách mỗi đầu 50 cm", "Đầu mút", "Cách đầu 25 cm", "Không cố định"], 0, "Tâm đối xứng hình học."),
            make_mc(11, "Thông hiểu", "Đặt điểm tựa đúng vào trọng tâm thước đồng chất thì thước sẽ:", ["Thăng bằng nằm ngang không nghiêng lệch", "Nghiêng trái", "Nghiêng phải", "Quay liên tục"], 0, "Trọng lực đi qua trục quay nên M = 0."),
            make_mc(12, "Thông hiểu", "Hai người khiêng vật nặng 500 N bằng đòn dài 2 m, vật treo cách người thứ nhất 0,8 m. Lực lên vai người thứ nhất là:", ["300 N", "200 N", "250 N", "400 N"], 0, "F1 = 500 × 1,2 / 2 = 300 N.")
        ],
        [
            make_tf(1, "Thông hiểu", "Quy tắc moment lực và trạng thái cân bằng:", [
                ("a", "Vật cân bằng khi tổng moment quay theo chiều kim đồng hồ bằng tổng moment ngược chiều.", True),
                ("b", "Lực có giá song song với trục quay không làm vật quay.", True),
                ("c", "Nếu không có trục quay cố định thì quy tắc moment không bao giờ áp dụng được.", False),
                ("d", "Với trục quay tức thời, quy tắc moment vẫn hoàn toàn nghiệm đúng.", True)
            ], "Vật quay quanh khối tâm vẫn áp dụng quy tắc moment."),
            make_tf(2, "Thông hiểu", "Đặc điểm thăng bằng của trò chơi bập bênh:", [
                ("a", "Bập bênh có trục quay cố định ở chính giữa thanh đòn.", True),
                ("b", "Hai bạn cùng trọng lượng ngồi cách đều trục thì bập bênh cân bằng nằm ngang.", True),
                ("c", "Nếu một bạn nhảy xuống thì bập bênh nghiêng về phía bạn còn lại.", True),
                ("d", "Bạn nhẹ hơn muốn cân bằng phải ngồi sát vào gần trục quay hơn.", False)
            ], "Bạn nhẹ hơn phải ngồi xa trục quay hơn."),
            make_tf(3, "Vận dụng", "Thanh đồng chất dài 1 m nặng 20 N (g = 10 m/s²) quay quanh trục O ở một đầu:", [
                ("a", "Trọng tâm của thanh cách trục quay O một đoạn 0,5 m.", True),
                ("b", "Moment của trọng lực làm thanh quay là 10 N.m.", True),
                ("c", "Để giữ thanh nằm ngang cần lực nâng ở đầu kia là 10 N hướng lên.", True),
                ("d", "Nếu đặt lực nâng ở chính giữa thanh thì cần lực 10 N để thanh nằm ngang.", False)
            ], "Đặt ở giữa thanh thì cần lực đúng bằng trọng lượng P = 20 N."),
            make_tf(4, "Vận dụng", "Người gánh hai thúng lúa nặng 300 N và 200 N bằng đòn gánh dài 1,5 m:", [
                ("a", "Tổng áp lực đè lên vai người gánh là 500 N (bỏ qua đòn gánh).", True),
                ("b", "Để đòn gánh thăng bằng, vai phải cách thúng 300 N là 0,6 m.", True),
                ("c", "Khoảng cách từ vai đến thúng 200 N là 0,9 m.", True),
                ("d", "Nếu đặt vai ở chính giữa đòn (0,75 m) thì đòn gánh vẫn thăng bằng nằm ngang.", False)
            ], "Đặt ở giữa thì thúng 300 N sẽ kéo đòn nghiêng sập xuống.")
        ],
        [
            make_sa(1, "Thông hiểu", "Đòn bẩy có d1 = 20 cm, d2 = 60 cm. Lực F1 = 90 N thì để cân bằng F2 là bao nhiêu N?", "30", "90 × 20 / 60 = 30 N."),
            make_sa(2, "Thông hiểu", "Vật A nặng 60 N cách trục 0,5 m. Để cân bằng, vật B cách trục 1,0 m phải có trọng lượng bao nhiêu N?", "30", "60 × 0,5 / 1,0 = 30 N."),
            make_sa(3, "Vận dụng", "Bập bênh: bạn Nam 45 kg ngồi cách trục 1,2 m. Bạn Lan ngồi cách trục 1,8 m thì thăng bằng. Khối lượng Lan là bao nhiêu kg?", "30", "45 × 1,2 / 1,8 = 30 kg."),
            make_sa(4, "Vận dụng", "Thanh nhẹ dài 80 cm trục quay ở giữa. Quả cân 4 N cách trục 40 cm. Quả cân 8 N ở đầu kia phải cách trục bao nhiêu cm để thăng bằng?", "20", "4 × 40 / 8 = 20 cm."),
            make_sa(5, "Vận dụng cao", "Thanh đồng chất dài 1,2 m nặng 24 N có trục quay cách đầu 0,4 m. Muốn thanh nằm ngang cần tác dụng vào đầu gần trục lực thẳng đứng bao nhiêu N?", "12", "F × 0,4 = 24 × 0,2 => F = 12 N."),
            make_sa(6, "Vận dụng cao", "Hai người khiêng thùng hàng nặng 900 N bằng đòn dài 3 m. Thùng hàng cách vai người trước 1 m. Lực lên vai người trước là bao nhiêu Newton?", "600", "F1 = 900 × 2 / 3 = 600 N.")
        ],
        [
            make_vdc(1, "Xe cút kít chở đất nặng 800 N có trọng tâm cách trục bánh xe 40 cm. Tay cầm cách trục bánh xe 120 cm. Lực nâng thẳng đứng tối thiểu của người là:", ["Khoảng 267 N (được lợi 3 lần về lực)", "800 N", "400 N", "133 N"], 0, "800 × 0,4 / 1,2 ≈ 266,7 N."),
            make_vdc(2, "Tấm ván dài 4 m nặng 400 N bắc qua mương. Cậu bé nặng 300 N đi từ bờ A sang B được 3 m. Phản lực của bờ B đỡ tấm ván là:", ["425 N", "200 N", "350 N", "500 N"], 0, "400 × 2 + 300 × 3 = 1 700 / 4 = 425 N."),
            make_vdc(3, "Thang dài 3 m tựa tường trơn, chân thang cách tường 1,8 m (chiều cao tường 2,4 m). Thang nặng 200 N có trọng tâm ở giữa. Lực đẩy của tường lên đầu thang là:", ["75 N", "100 N", "150 N", "50 N"], 0, "N × 2,4 = 200 × 0,9 = 180 => N = 75 N."),
            make_vdc(4, "Bẩy hòn đá nặng 2 400 N bằng xà beng dài 1,5 m kê điểm tựa cách hòn đá 30 cm. Lực ấn tối thiểu vào đầu kia của xà beng là:", ["600 N", "480 N", "1 200 N", "300 N"], 0, "2 400 × 0,3 / 1,2 = 600 N.")
        ]
    )

    # --- B18 ĐỀ 3 ---
    exams[f"{l18_id}_test3"] = meta(l18_id, l18_name, 3,
        [
            make_mc(1, "Nhận biết", "Moment lực đo bằng tích của lực với:", ["Cánh tay đòn của lực", "Khối lượng vật", "Gia tốc rơi", "Vận tốc góc"], 0, "M = F.d."),
            make_mc(2, "Nhận biết", "Khi giá của lực cắt trục quay thì moment của lực đó:", ["Bằng 0", "Rất lớn", "Bằng độ dài vật", "Bằng 1"], 0, "d = 0 nên M = 0."),
            make_mc(3, "Nhận biết", "Để tăng tác dụng làm quay của lực, cách hiệu quả nhất là:", ["Tăng độ lớn của lực và tăng cánh tay đòn", "Giảm độ lớn của lực", "Cho lực đi qua trục quay", "Đặt lực song song trục quay"], 0, "Tăng F và d."),
            make_mc(4, "Nhận biết", "Tay nắm cửa sổ mở hất thiết kế dạng cần gạt dài để:", ["Tạo cánh tay đòn lớn giúp mở êm nhẹ", "Tránh gió thổi", "Để treo đồ", "Để trang trí"], 0, "Tăng cánh tay đòn."),
            make_mc(5, "Nhận biết", "Ngẫu lực là hệ hai lực:", ["Song song, ngược chiều, độ lớn bằng nhau, tác dụng vào cùng một vật", "Cùng chiều cùng độ lớn", "Vuông góc nhau", "Trùng giá nhau"], 0, "Định nghĩa ngẫu lực."),
            make_mc(6, "Nhận biết", "Thiết bị nào chịu tác dụng của ngẫu lực khi vận hành?", ["Vô-lăng lái ô tô khi hai tay xoay ngược chiều", "Kìm cắt thép", "Bập bênh", "Đòn bẩy loại 1"], 0, "Vô-lăng lái xe khi 2 tay xoay."),
            make_mc(7, "Thông hiểu", "Tác dụng lực F = 50 N vuông góc với cờ-lê dài 0,2 m. Moment lực là:", ["10 N.m", "250 N.m", "25 N.m", "5 N.m"], 0, "50 × 0,2 = 10 N.m."),
            make_mc(8, "Thông hiểu", "Vô-lăng đường kính 40 cm chịu ngẫu lực F = 15 N ở hai vành. Moment ngẫu lực là:", ["6 N.m", "3 N.m", "15 N.m", "60 N.m"], 0, "15 × 0,4 = 6 N.m."),
            make_mc(9, "Thông hiểu", "Thanh AB dài 1 m có trục quay ở giữa. Đầu A chịu F1 = 8 N hướng xuống, đầu B chịu F2 = 8 N hướng lên. Thanh chịu tác dụng của:", ["Ngẫu lực làm thanh quay cùng chiều kim đồng hồ với moment 8 N.m", "Lực triệt tiêu đứng yên", "Lực kéo ngang", "Lực nén"], 0, "Ngẫu lực M = 8 × 1 = 8 N.m."),
            make_mc(10, "Thông hiểu", "Vặn nắp lọ mứt thủy tinh bằng hai tay đối xứng là vận dụng:", ["Ngẫu lực tạo moment làm quay nắp lọ", "Lực ma sát trượt", "Lực đàn hồi", "Áp suất chất lỏng"], 0, "Ngẫu lực vặn nắp lọ."),
            make_mc(11, "Thông hiểu", "Đùi đĩa bàn đạp xe đạp dài 17 cm. Người đạp dồn lực 200 N vuông góc với đùi đĩa nằm ngang. Moment lực tác dụng lên trục xe là:", ["34 N.m", "340 N.m", "3,4 N.m", "1 176 N.m"], 0, "200 × 0,17 = 34 N.m."),
            make_mc(12, "Thông hiểu", "Dùng búa nhổ đinh cắm chặt vào gỗ là ứng dụng của:", ["Moment lực và đòn bẩy", "Lực ma sát nghỉ", "Lực quán tính", "Áp suất khí quyển"], 0, "Búa nhổ đinh hoạt động như đòn bẩy.")
        ],
        [
            make_tf(1, "Thông hiểu", "Khái niệm và đặc điểm của ngẫu lực:", [
                ("a", "Ngẫu lực gồm hai lực song song, ngược chiều, cùng độ lớn tác dụng vào cùng vật.", True),
                ("b", "Ngẫu lực chỉ có tác dụng làm quay vật chứ không làm vật chuyển động tịnh tiến.", True),
                ("c", "Moment của ngẫu lực bằng tích của độ lớn một lực với khoảng cách giữa hai giá của hai lực.", True),
                ("d", "Ngẫu lực có hợp lực bằng tổng độ lớn của hai lực cộng lại.", False)
            ], "Hợp lực của hai lực ngược chiều bằng nhau là bằng 0."),
            make_tf(2, "Thông hiểu", "Các ví dụ thực tế về ngẫu lực trong sinh hoạt:", [
                ("a", "Dùng hai tay vặn mở van vòi nước chữa cháy.", True),
                ("b", "Hai tay tài xế xoay vô-lăng ô tô để bẻ lái vào cua.", True),
                ("c", "Dùng tuốc-nơ-vít hai ngón tay vặn đinh ốc vít xoắn.", True),
                ("d", "Dùng búa gõ thẳng góc vào đầu đinh để đóng vào tường.", False)
            ], "Gõ búa vào đinh là lực đơn truyền lực tịnh tiến."),
            make_tf(3, "Vận dụng", "Một đĩa tròn đồng chất bán kính R = 20 cm có thể quay quanh trục không ma sát đi qua tâm O. Tác dụng ngẫu lực tiếp tuyến với vành đĩa F1 = F2 = 10 N:", [
                ("a", "Khoảng cách giữa hai giá của hai lực ngẫu lực là đường kính d = 40 cm = 0,4 m.", True),
                ("b", "Moment của ngẫu lực tác dụng lên đĩa tròn là 4 N.m.", True),
                ("c", "Đĩa tròn sẽ chuyển động quay quanh trục O.", True),
                ("d", "Nếu đặt thêm ngẫu lực ngược chiều có độ lớn 10 N thì đĩa sẽ quay nhanh hơn gấp đôi.", False)
            ], "Ngẫu lực ngược chiều cùng độ lớn sẽ triệt tiêu làm đĩa dừng quay."),
            make_tf(4, "Vận dụng", "Thanh cứng AB dài 0,6 m có trục quay O ở giữa (OA = OB = 0,3 m). Ở A tác dụng lực F1 = 20 N vuông góc với thanh hướng lên, ở B tác dụng F2 = 20 N hướng xuống:", [
                ("a", "Hệ hai lực F1 và F2 là một ngẫu lực.", True),
                ("b", "Cả hai lực đều làm thanh quay cùng một chiều quanh O.", True),
                ("c", "Tổng moment lực làm quay thanh là 12 N.m.", True),
                ("d", "Để giữ thanh đứng yên cần tác dụng vào B lực 20 N hướng lên.", False)
            ], "Để cân bằng ngẫu lực 12 N.m cần một moment ngẫu lực ngược chiều 12 N.m.")
        ],
        [
            make_sa(1, "Thông hiểu", "Vặn vô-lăng đường kính 35 cm bằng ngẫu lực 20 N. Moment ngẫu lực là bao nhiêu N.m?", "7", "20 × 0,35 = 7 N.m."),
            make_sa(2, "Thông hiểu", "Hai lực của ngẫu lực có độ lớn F = 15 N cách nhau 0,2 m. Moment ngẫu lực là bao nhiêu N.m?", "3", "15 × 0,2 = 3 N.m."),
            make_sa(3, "Vận dụng", "Dùng tuốc-nơ-vít có tay cầm đường kính 3 cm để vặn ốc. Lực của hai ngón tay là 20 N. Moment vặn là bao nhiêu N.m?", "0.6", "20 × 0,03 = 0,6 N.m."),
            make_sa(4, "Vận dụng", "Bàn đạp xe đạp dài 18 cm. Đạp vuông góc với lực 250 N. Moment tạo ra là bao nhiêu N.m?", "45", "250 × 0,18 = 45 N.m."),
            make_sa(5, "Vận dụng cao", "Cánh cửa xoay văn phòng có 3 cánh, mỗi cánh rộng 1,2 m. Một người đẩy vuông góc vào giữa cánh cửa (cách trục 0,6 m) với lực 50 N. Moment làm quay cửa là bao nhiêu N.m?", "30", "50 × 0,6 = 30 N.m."),
            make_sa(6, "Vận dụng cao", "Một khung dây chữ nhật kích thước 20 cm × 10 cm đặt trong từ trường chịu ngẫu lực 0,5 N tác dụng lên hai cạnh 20 cm (cách nhau 10 cm). Moment ngẫu lực từ là bao nhiêu N.m?", "0.05", "0,5 × 0,1 = 0,05 N.m.")
        ],
        [
            make_vdc(1, "Một người dùng cờ-lê chữ thập (chữ X) có 4 đầu khẩu để tháo ốc bánh xe tải. Người đó dùng hai tay kéo đẩy ngược chiều ở hai đầu cờ-lê cách nhau 40 cm với lực mỗi tay là 150 N. Moment ngẫu lực tháo ốc là:", ["60 N.m", "30 N.m", "150 N.m", "300 N.m"], 0, "M = F.d = 150 × 0,4 = 60 N.m."),
            make_vdc(2, "Tại sao khi mở nắp một chai nước giải khát bằng kim loại có ren xoắn, ta nên dùng cả bàn tay cầm quanh nắp vặn thay vì dùng một ngón tay gạt?", ["Dùng nhiều ngón tay phân bố đều quanh nắp tạo thành hệ ngẫu lực đối xứng triệt tiêu lực uốn trục giúp nắp xoay đều mà không làm kẹt méo ren", "Để chai không bị đổ", "Để không đau tay", "Để nắp nóng lên"], 0, "Tạo hệ ngẫu lực đối xứng vặn đều ren."),
            make_vdc(3, "Một động cơ điện sinh ra moment quay định mức 50 N.m trên trục động cơ có đường kính 20 mm (bán kính r = 10 mm = 0,01 m). Lực tiếp tuyến tác dụng lên vành trục động cơ là:", ["5 000 N", "500 N", "2 500 N", "50 N"], 0, "F = M / r = 50 / 0,01 = 5 000 N."),
            make_vdc(4, "Một người thợ cơ khí thiết kế tay quay tời kéo nước từ giếng sâu. Tay quay có bán kính quay R = 40 cm. Trục tời cuốn dây có bán kính r = 10 cm. Để kéo một thùng nước nặng 200 N từ giếng lên đều, lực quay tay tối thiểu của người đó là:", ["50 N (được lợi 4 lần về lực)", "200 N", "100 N", "25 N"], 0, "F × R = P × r => F = 200 × 10 / 40 = 50 N.")
        ]
    )

    # =========================================================================
    # BÀI 19: ĐÒN BẨY VÀ ỨNG DỤNG (3 ĐỀ)
    # =========================================================================
    l19_id = "phys8_c4_b19"
    l19_name = "Bài 19: Đòn bẩy và ứng dụng"

    # --- B19 ĐỀ 1: Đòn bẩy loại 1 ---
    exams[f"{l19_id}_test1"] = meta(l19_id, l19_name, 1,
        [
            make_mc(1, "Nhận biết", "Đòn bẩy loại 1 có đặc điểm cấu tạo là:", ["Điểm tựa O nằm giữa điểm tác dụng lực và điểm đặt tải trọng", "Tải trọng nằm ở giữa", "Điểm tác dụng lực nằm ở giữa", "Không có điểm tựa cố định"], 0, "Đòn bẩy loại 1: O nằm ở giữa."),
            make_mc(2, "Nhận biết", "Dụng cụ nào sau đây là ứng dụng của đòn bẩy loại 1?", ["Cái kéo cắt kim loại, kìm nhổ đinh, bập bênh", "Xe cút kít", "Kẹp gắp thức ăn", "Cần câu cá"], 0, "Kéo, kìm, bập bênh có trục ở giữa."),
            make_mc(3, "Nhận biết", "Điều kiện cân bằng của đòn bẩy là:", ["F1 × d1 = F2 × d2", "F1 / d1 = F2 / d2", "F1 + d1 = F2 + d2", "F1 × F2 = d1 × d2"], 0, "F1.d1 = F2.d2."),
            make_mc(4, "Nhận biết", "Kéo cắt kim loại có đặc điểm cán dài hơn lưỡi nhiều lần nhằm:", ["Được lợi về lực cắt", "Được lợi về đường đi", "Cắt nhanh hơn", "Nhìn đẹp hơn"], 0, "d1 > d2 nên F1 < F2 (lợi về lực)."),
            make_mc(5, "Nhận biết", "Kéo cắt vải hoặc cắt giấy thường có lưỡi dài hơn cán nhằm:", ["Được lợi về quãng đường cắt nhanh và thẳng", "Được lợi về lực", "Để kéo nhẹ hơn", "Để không bị cùn"], 0, "Lợi về quãng đường cắt nhanh."),
            make_mc(6, "Nhận biết", "Trong đòn bẩy loại 1, để được lợi về lực (F1 < F2) thì:", ["Cánh tay đòn d1 phải lớn hơn d2", "d1 nhỏ hơn d2", "d1 bằng d2", "Không phụ thuộc d"], 0, "d1 > d2 thì F1 < F2."),
            make_mc(7, "Thông hiểu", "Dùng xà beng dài 1 m có điểm tựa O cách hòn đá 0,2 m để bẩy hòn đá nặng 800 N. Lực ấn tối thiểu vào đầu kia là:", ["200 N", "160 N", "800 N", "400 N"], 0, "F × 0,8 = 800 × 0,2 => F = 200 N."),
            make_mc(8, "Thông hiểu", "Một chiếc kìm có cán dài 15 cm và lưỡi kìm dài 3 cm. Tác dụng lực tay 60 N vào cán kìm, lực cắt lên vật kẹp là:", ["300 N", "12 N", "180 N", "60 N"], 0, "F2 = 60 × 15 / 3 = 300 N."),
            make_mc(9, "Thông hiểu", "Dùng búa nhổ đinh có cán búa dài 30 cm, đầu mấu nhổ đinh cách điểm tựa 3 cm. Lực nhổ đinh tác dụng lên đinh gấp lực tay:", ["10 lần", "3 lần", "30 lần", "100 lần"], 0, "30 / 3 = 10 lần."),
            make_mc(10, "Thông hiểu", "Khi chèo thuyền nan, cọc chèo đóng vai trò là điểm tựa O ở giữa mái chèo. Đây là ứng dụng của:", ["Đòn bẩy loại 1", "Đòn bẩy loại 2", "Đòn bẩy loại 3", "Mặt phẳng nghiêng"], 0, "Cọc chèo ở giữa là đòn bẩy loại 1."),
            make_mc(11, "Thông hiểu", "Một thanh đòn bẩy dài 1,2 m thăng bằng nằm ngang khi treo vật 60 N ở đầu A và vật 20 N ở đầu B. Điểm tựa O cách đầu A là:", ["0,3 m", "0,4 m", "0,6 m", "0,9 m"], 0, "60 × x = 20 × (1,2 - x) => 80 x = 24 => x = 0,3 m."),
            make_mc(12, "Thông hiểu", "Đòn bẩy nào sau đây KHÔNG cho ta lợi về lực?", ["Kéo cắt tóc (lưỡi dài hơn cán)", "Kéo cắt cành cây (cán dài hơn lưỡi)", "Kìm kẹp dây thép", "Xà beng bẩy đá"], 0, "Kéo cắt tóc lưỡi dài hơn cán nên thiệt về lực.")
        ],
        [
            make_tf(1, "Thông hiểu", "Đặc điểm của đòn bẩy loại 1:", [
                ("a", "Điểm tựa O luôn nằm giữa điểm tác dụng lực F1 và tải trọng F2.", True),
                ("b", "Có thể cho ta lợi về lực nếu cánh tay đòn của lực lớn hơn cánh tay đòn của tải trọng.", True),
                ("c", "Có thể cho ta lợi về đường đi nếu cánh tay đòn của lực nhỏ hơn cánh tay đòn của tải trọng.", True),
                ("d", "Luôn luôn cho ta lợi về lực trong mọi trường hợp cấu tạo.", False)
            ], "Nếu d1 < d2 thì thiệt về lực."),
            make_tf(2, "Thông hiểu", "Cấu tạo chiếc kéo trong đời sống:", [
                ("a", "Trục ốc vít ở giữa hai lưỡi kéo là điểm tựa O.", True),
                ("b", "Kéo cắt kim loại có cán dài, lưỡi ngắn để tăng tối đa lực cắt.", True),
                ("c", "Kéo cắt vải có lưỡi dài để một lần cắt được đường vải dài và đều.", True),
                ("d", "Kéo cắt tóc có cán dài gấp 5 lần lưỡi kéo.", False)
            ], "Kéo cắt tóc có lưỡi dài hơn cán để cắt nhanh."),
            make_tf(3, "Vận dụng", "Dùng chiếc xà beng dài 1,5 m bẩy tảng đá nặng 1 800 N. Điểm tựa kê cách tảng đá 0,3 m:", [
                ("a", "Cánh tay đòn của tảng đá là d2 = 0,3 m.", True),
                ("b", "Cánh tay đòn của người ấn là d1 = 1,2 m.", True),
                ("c", "Lực ấn tối thiểu của người đó là 450 N.", True),
                ("d", "Chiếc xà beng này cho ta lợi 5 lần về lực.", False)
            ], "Tỉ số lực = 1,2 / 0,3 = 4 lần (lợi 4 lần về lực)."),
            make_tf(4, "Vận dụng", "Một cây đòn bẩy thăng bằng dài 2 m có trục quay O cách đầu A 0,5 m. Đầu A treo quả cân 300 N:", [
                ("a", "Điểm tựa O cách đầu B một khoảng 1,5 m.", True),
                ("b", "Để thăng bằng, cần treo vào đầu B một quả cân 100 N.", True),
                ("c", "Tổng lực đè lên điểm tựa O là 400 N (bỏ qua khối lượng thanh).", True),
                ("d", "Nếu di chuyển điểm tựa O về phía B thì lực cần giữ ở B sẽ nhỏ hơn.", False)
            ], "Dịch O về phía B làm d2 ngắn lại nên lực ở B phải lớn hơn.")
        ],
        [
            make_sa(1, "Thông hiểu", "Đòn bẩy loại 1 có d1 = 80 cm, d2 = 20 cm. Muốn nâng vật nặng 400 N cần lực F1 là bao nhiêu Newton?", "100", "400 × 20 / 80 = 100 N."),
            make_sa(2, "Thông hiểu", "Kéo cắt kim loại có cán dài 24 cm, lưỡi dài 6 cm. Lợi về lực bao nhiêu lần?", "4", "24 / 6 = 4 lần."),
            make_sa(3, "Vận dụng", "Búa nhổ đinh có d_tay = 25 cm, d_đinh = 2,5 cm. Lực nhổ đinh là 1 000 N thì lực tay tác dụng là bao nhiêu Newton?", "100", "1 000 × 2,5 / 25 = 100 N."),
            make_sa(4, "Vận dụng", "Xà beng dài 1,8 m, kê điểm tựa cách hòn đá 30 cm. Lực ấn tay 150 N bẩy được hòn đá có trọng lượng bao nhiêu Newton?", "750", "150 × 1,5 / 0,3 = 750 N."),
            make_sa(5, "Vận dụng cao", "Thanh đòn dài 1 m có điểm tựa cách đầu A 20 cm. Treo vật 200 N ở A. Để nâng vật lên 5 cm thì đầu B phải dịch chuyển xuống bao nhiêu cm?", "20", "h_B = 5 × (80 / 20) = 20 cm."),
            make_sa(6, "Vận dụng cao", "Một cân đòn có đĩa cân cách trục 10 cm. Quả cân trượt nặng 50 g cách trục 40 cm thì cân thăng bằng. Vật trên đĩa cân nặng bao nhiêu gam?", "200", "m = 50 × 40 / 10 = 200 g.")
        ],
        [
            make_vdc(1, "Một người thợ cơ khí dùng kìm cộng lực có cán dài 60 cm và lưỡi kìm dài 3 cm để cắt một đoạn dây thép đặc. Khi tay bóp lực 200 N vào đầu cán kìm, lực tác dụng lên vết cắt dây thép là:", ["4 000 N", "2 000 N", "6 000 N", "1 000 N"], 0, "F2 = 200 × 60 / 3 = 4 000 N (gấp 20 lần lực bóp tay)."),
            make_vdc(2, "Một chiếc kéo cắt cành cây có cán dài 40 cm, lưỡi kéo dài 8 cm. Để cắt một cành cây cứng cần lực cắt tối thiểu 500 N, người làm vườn đặt cành cây sát tận khớp quay (cách trục 4 cm). Lực tay bóp tối thiểu của người làm vườn lúc này là:", ["50 N", "100 N", "25 N", "125 N"], 0, "F1 = 500 × 4 / 40 = 50 N."),
            make_vdc(3, "Một thanh đòn bằng sắt đồng chất dài 2 m, nặng 40 N được kê trên điểm tựa O cách đầu A một khoảng 0,5 m. Muốn thanh đòn thăng bằng nằm ngang thì ở đầu A phải treo một vật nặng có trọng lượng bằng:", ["40 N", "80 N", "60 N", "20 N"], 0, "Trọng tâm thanh ở giữa (cách A 1 m, cách O 0,5 m). P_thanh × 0,5 = P_vật × 0,5 => P_vật = 40 N."),
            make_vdc(4, "Một cần cẩu cứu hộ đơn giản hoạt động như đòn bẩy loại 1 có trục quay O. Đầu ngắn mang tời cứu hộ dài 2 m, đầu dài mang cáp tời dài 8 m. Để nâng chiếc xe tai nạn nặng 2 tấn (20 000 N, g = 10 m/s²) ở đầu ngắn thì lực kéo ở đầu dài cần thiết tối thiểu là:", ["5 000 N", "10 000 N", "2 500 N", "80 000 N"], 0, "F = 20 000 × 2 / 8 = 5 000 N.")
        ]
    )

    # --- B19 ĐỀ 2: Đòn bẩy loại 2 ---
    exams[f"{l19_id}_test2"] = meta(l19_id, l19_name, 2,
        [
            make_mc(1, "Nhận biết", "Đòn bẩy loại 2 có đặc điểm cấu tạo là:", ["Tải trọng (vật nâng) nằm ở giữa điểm tựa O và điểm tác dụng lực", "Điểm tựa O nằm ở giữa", "Điểm tác dụng lực nằm ở giữa", "Không có điểm tựa"], 0, "Đòn bẩy loại 2: tải trọng ở giữa."),
            make_mc(2, "Nhận biết", "Dụng cụ nào sau đây là ứng dụng của đòn bẩy loại 2?", ["Xe cút kít (xe rùa), kẹp hạt óc chó, khui nắp chai bia", "Cái kéo cắt giấy", "Cần câu cá", "Nhíp gắp"], 0, "Xe cút kít, mở nắp chai, kẹp óc chó."),
            make_mc(3, "Nhận biết", "Trong đòn bẩy loại 2, mối liên hệ giữa cánh tay đòn của lực (d1) và cánh tay đòn của tải trọng (d2) luôn là:", ["d1 luôn lớn hơn d2 (d1 > d2)", "d1 < d2", "d1 = d2", "Không cố định"], 0, "d1 luôn lớn hơn d2 vì điểm đặt lực ở ngoài cùng."),
            make_mc(4, "Nhận biết", "Đòn bẩy loại 2 có ưu điểm vượt trội là:", ["Luôn cho ta lợi về lực (F1 < F2)", "Lợi về quãng đường đi", "Lợi về vận tốc", "Lợi về công cơ học"], 0, "Luôn lợi về lực."),
            make_mc(5, "Nhận biết", "Khi dùng dụng cụ khui nắp chai bia bằng kim loại, điểm tựa O nằm ở:", ["Mép đỉnh nắp chai bia", "Tay cầm", "Răng móc dưới nắp chai", "Cổ chai"], 0, "Điểm tựa O ở trên mặt nắp chai, răng móc ở giữa kéo viền nắp."),
            make_mc(6, "Nhận biết", "Xe cút kít chở đất có điểm tựa O nằm ở:", ["Trục quay của bánh xe trước", "Tay cầm của xe", "Thùng xe", "Chân chống"], 0, "Trục bánh xe trước là điểm tựa O."),
            make_mc(7, "Thông hiểu", "Xe rùa chở bao cát nặng 600 N có trọng tâm cách trục bánh xe 50 cm. Tay cầm cách trục bánh xe 150 cm. Lực nâng của tay là:", ["200 N", "600 N", "400 N", "150 N"], 0, "F = 600 × 50 / 150 = 200 N."),
            make_mc(8, "Thông hiểu", "Dụng cụ kẹp vỡ hạt óc chó có chiều dài cán 16 cm, vị trí đặt hạt cách khớp nối điểm tựa 4 cm. Lợi về lực bao nhiêu lần?", ["4 lần", "2 lần", "8 lần", "16 lần"], 0, "16 / 4 = 4 lần."),
            make_mc(9, "Thông hiểu", "Dùng dụng cụ dập ghim giấy văn phòng. Trục gập ở đuôi, vị trí khay ghim ở giữa cách trục 3 cm, tay ấn ở đầu cách trục 9 cm. Lực ép lên ghim gấp lực tay:", ["3 lần", "9 lần", "6 lần", "1 lần"], 0, "9 / 3 = 3 lần."),
            make_mc(10, "Thông hiểu", "Khi bẻ cong một tấm ván gỗ bằng cách đạp chân lên đầu tấm ván có kê gờ chặn, đòn bẩy loại 2:", ["Cho ta lợi về lực nhưng bị thiệt về quãng đường di chuyển", "Lợi cả lực và đường đi", "Thiệt cả lực và đường đi", "Lợi về công"], 0, "Lợi về lực thì thiệt về đường đi."),
            make_mc(11, "Thông hiểu", "Động tác chống đẩy (hít đất) của cơ thể người: điểm tựa là mũi chân chạm sàn, trọng lượng cơ thể đặt ở rốn (giữa), lực nâng đặt ở hai bàn tay. Đây là mô hình:", ["Đòn bẩy loại 2", "Đòn bẩy loại 1", "Đòn bẩy loại 3", "Mặt phẳng nghiêng"], 0, "Trọng tâm ở giữa hai bàn tay và mũi chân => Đòn bẩy loại 2."),
            make_mc(12, "Thông hiểu", "Bàn đạp phanh chân ô tô có trục quay ở đầu trên, pit-tông phanh đẩy ở giữa và bàn chân đạp ở đầu dưới. Đây là:", ["Đòn bẩy loại 2 giúp khuếch đại lực chân tác dụng lên xi lanh phanh", "Đòn bẩy loại 1", "Đòn bẩy loại 3", "Ròng rọc động"], 0, "Đòn bẩy loại 2 giúp tăng lực phanh.")
        ],
        [
            make_tf(1, "Thông hiểu", "Nguyên lí hoạt động của đòn bẩy loại 2:", [
                ("a", "Tải trọng luôn nằm giữa điểm tựa và điểm tác dụng lực.", True),
                ("b", "Cánh tay đòn của lực tác dụng luôn dài hơn cánh tay đòn của tải trọng.", True),
                ("c", "Đòn bẩy loại 2 luôn cho ta lợi về lực trong mọi trường hợp.", True),
                ("d", "Đòn bẩy loại 2 cho ta lợi về quãng đường nâng vật.", False)
            ], "Lợi về lực thì thiệt về đường đi (tay phải nâng quãng đường dài hơn)."),
            make_tf(2, "Thông hiểu", "Ứng dụng xe cút kít (xe rùa) trong xây dựng:", [
                ("a", "Trục bánh xe phía trước đóng vai trò là điểm tựa O.", True),
                ("b", "Trọng tâm đống vữa gạch nằm ở thùng xe giữa bánh xe và tay cầm.", True),
                ("c", "Xếp vật liệu càng lùi về sát trục bánh xe thì người nâng càng nhẹ tay.", True),
                ("d", "Nếu xếp toàn bộ vật liệu về phía tay cầm sát người thì sẽ nâng nhẹ nhất.", False)
            ], "Xếp sát bánh xe làm d2 nhỏ nhất thì lực nâng F1 nhỏ nhất."),
            make_tf(3, "Vận dụng", "Dụng cụ kẹp vỡ quả hồ đào: quả hạt đặt cách trục khớp 3 cm, tay bóp ở vị trí cách trục 15 cm. Cần lực ép lên hạt là 150 N để làm vỡ vỏ hạt:", [
                ("a", "Cánh tay đòn của lực ép lên hạt là 3 cm.", True),
                ("b", "Cánh tay đòn của lực bóp tay là 15 cm.", True),
                ("c", "Lực bóp tay tối thiểu của người dùng là 30 N.", True),
                ("d", "Dụng cụ này cho ta lợi 10 lần về lực.", False)
            ], "Lợi 15 / 3 = 5 lần về lực."),
            make_tf(4, "Vận dụng", "Động tác kiễng gót chân của bàn chân người: Điểm tựa O là khớp các ngón chân chạm đất, tải trọng cơ thể dồn lên xương cẳng chân ở giữa, lực kéo của gân gót chân (gân Achilles) ở phía sau gót:", [
                ("a", "Khớp ngón chân chạm đất là điểm tựa O.", True),
                ("b", "Trọng lượng cơ thể đặt ở giữa điểm tựa và lực co cơ bắp chân.", True),
                ("c", "Bàn chân người khi kiễng gót hoạt động như một đòn bẩy loại 2.", True),
                ("d", "Cơ bắp chân phải tác dụng một lực lớn gấp đôi trọng lượng cơ thể để kiễng gót chân.", False)
            ], "Đòn bẩy loại 2 lợi về lực nên cơ bắp chân tác dụng lực nhỏ hơn trọng lượng cơ thể.")
        ],
        [
            make_sa(1, "Thông hiểu", "Xe cút kít có d_vật = 40 cm, d_tay = 120 cm. Lợi về lực bao nhiêu lần?", "3", "120 / 40 = 3 lần."),
            make_sa(2, "Thông hiểu", "Khui nắp chai có d1 = 12 cm, d2 = 2 cm. Cần lực bật nắp 120 N thì lực tay nâng là bao nhiêu Newton?", "20", "120 × 2 / 12 = 20 N."),
            make_sa(3, "Vận dụng", "Dùng xe rùa nâng thùng cát nặng 900 N. Thùng cát cách bánh xe 0,4 m. Tay cầm cách bánh xe 1,2 m. Lực tay nâng là bao nhiêu Newton?", "300", "900 × 0,4 / 1,2 = 300 N."),
            make_sa(4, "Vận dụng", "Kẹp óc chó dài 18 cm, hạt đặt cách trục 3 cm. Bóp tay lực 40 N tạo lực ép lên hạt là bao nhiêu Newton?", "240", "40 × 18 / 3 = 240 N."),
            make_sa(5, "Vận dụng cao", "Một người nặng 60 kg chống đẩy hít đất (g = 10 m/s²). Trọng tâm cơ thể cách mũi chân 1,0 m, hai tay chống cách mũi chân 1,5 m. Tổng lực nâng của hai bàn tay là bao nhiêu Newton?", "400", "F = 600 × 1,0 / 1,5 = 400 N."),
            make_sa(6, "Vận dụng cao", "Dụng cụ cắt giấy bàn (dao xén giấy) có lưỡi dao dài 50 cm gắn bản lề ở đầu. Đặt tệp giấy cách bản lề 10 cm. Cần lực cắt 200 N thì lực tay ấn ở đầu mút cán dao là bao nhiêu Newton?", "40", "200 × 10 / 50 = 40 N.")
        ],
        [
            make_vdc(1, "Một người làm vườn đẩy xe cút kít chở khối đá nặng 1 200 N. Vị trí trọng tâm khối đá cách trục bánh xe 30 cm. Cán tay cầm cách trục bánh xe 1,5 m. Khi người đó nâng tay cầm lên cao thêm 20 cm thì quãng đường nâng lên của khối đá là:", ["4 cm", "10 cm", "2 cm", "5 cm"], 0, "h_đá = 20 × (0,3 / 1,5) = 4 cm (được lợi 5 lần về lực nhưng thiệt 5 lần về đường đi)."),
            make_vdc(2, "Dao cắt giấy văn phòng dạng bàn xén có bản lề gắn cố định ở một đầu. Khi cắt một xấp giấy dày, người thợ đặt xấp giấy vào sát phía bản lề thay vì để ở giữa lưỡi dao vì:", ["Giảm cánh tay đòn của xấp giấy d2 giúp tăng tối đa lực cắt tác dụng lên xấp giấy với lực ấn tay không đổi", "Để giấy không bị xô lệch", "Để nhìn đường cắt rõ hơn", "Để dao không bị cùn"], 0, "Giảm d2 làm tăng lực cắt F2 = F1.d1/d2."),
            make_vdc(3, "Khi dùng dụng cụ mở nắp chai bia bằng kim loại, người ta đặt móc bật dưới gờ nắp chai (cách điểm tựa đỉnh nắp 5 mm) và cầm ở đầu cán dài 10 cm (100 mm). Lợi thế cơ học về lực của dụng cụ mở nắp chai này là:", ["Lợi 20 lần về lực", "Lợi 10 lần", "Lợi 50 lần", "Lợi 5 lần"], 0, "100 / 5 = 20 lần."),
            make_vdc(4, "Một thanh gỗ dài 2 m dùng làm đòn bẩy loại 2 để nâng một cỗ máy nặng 6 000 N kê cách đầu tựa A 40 cm. Để nâng cỗ máy lên, người thợ dùng đòn bẩy móc vào một palăng xích ở đầu B. Lực kéo palăng tối thiểu ở đầu B là:", ["1 200 N", "2 400 N", "600 N", "3 000 N"], 0, "F = 6 000 × 0,4 / 2 = 1 200 N.")
        ]
    )

    # --- B19 ĐỀ 3: Đòn bẩy loại 3 ---
    exams[f"{l19_id}_test3"] = meta(l19_id, l19_name, 3,
        [
            make_mc(1, "Nhận biết", "Đòn bẩy loại 3 có đặc điểm cấu tạo là:", ["Điểm tác dụng lực nằm ở giữa điểm tựa O và tải trọng", "Điểm tựa nằm ở giữa", "Tải trọng nằm ở giữa", "Không có trục quay"], 0, "Đòn bẩy loại 3: điểm tác dụng lực ở giữa."),
            make_mc(2, "Nhận biết", "Dụng cụ nào sau đây là ứng dụng của đòn bẩy loại 3?", ["Kẹp gắp thức ăn, cần câu cá, chổi quét nhà, nhíp nhổ râu", "Cái kéo cắt kim loại", "Xe cút kít", "Kẹp óc chó"], 0, "Kẹp gắp thức ăn, cần câu, nhíp, chổi."),
            make_mc(3, "Nhận biết", "Trong đòn bẩy loại 3, mối liên hệ giữa cánh tay đòn của lực (d1) và tải trọng (d2) luôn là:", ["d1 luôn nhỏ hơn d2 (d1 < d2)", "d1 > d2", "d1 = d2", "Không xác định"], 0, "d1 < d2 vì lực đặt ở giữa."),
            make_mc(4, "Nhận biết", "Đòn bẩy loại 3 có đặc điểm cơ học là:", ["Thiệt về lực nhưng cho ta lợi về đường đi và vận tốc", "Lợi về lực", "Lợi về công cơ học", "Không có tác dụng gì"], 0, "Thiệt về lực nhưng lợi về đường đi và tốc độ."),
            make_mc(5, "Nhận biết", "Khớp khuỷu tay và cơ bắp tay (cơ nhị đầu) của người hoạt động như:", ["Đòn bẩy loại 3", "Đòn bẩy loại 1", "Đòn bẩy loại 2", "Mặt phẳng nghiêng"], 0, "Cơ bám ở giữa khớp khuỷu tay và bàn tay => Đòn bẩy loại 3."),
            make_mc(6, "Nhận biết", "Khi người câu cá giật cần câu, tay cầm phía trên kéo cần ở giữa còn tay dưới giữ cán cần làm điểm tựa O. Đây là:", ["Đòn bẩy loại 3 giúp đầu cần câu vung nhanh quãng đường dài", "Đòn bẩy loại 1", "Đòn bẩy loại 2", "Ròng rọc"], 0, "Cần câu cá là đòn bẩy loại 3."),
            make_mc(7, "Thông hiểu", "Dùng kẹp gắp than dài 30 cm, ngón tay bóp ở vị trí cách khớp tựa 10 cm. Tỉ số lực giữa tay bóp và viên than gắp được là:", ["Lực tay bóp lớn gấp 3 lần lực kẹp than (thiệt 3 lần về lực)", "Lực tay nhỏ hơn 3 lần", "Bằng nhau", "Gấp 9 lần"], 0, "d2 = 30, d1 = 10 => F1 = 3 F2."),
            make_mc(8, "Thông hiểu", "Dùng nhíp nhổ râu dài 8 cm, tay bóp ở điểm cách đầu tựa 4 cm. Đây là đòn bẩy loại 3 có tỉ số thiệt về lực là:", ["2 lần", "4 lần", "0,5 lần", "8 lần"], 0, "8 / 4 = 2 lần."),
            make_mc(9, "Thông hiểu", "Khi quét nhà bằng chổi đót dài, tay trên giữ cán chổi làm điểm tựa, tay dưới đẩy chổi ở giữa cán. Tác dụng chính là:", ["Đầu chổi quét được quãng đường rất rộng và nhanh", "Để đỡ tốn lực tay", "Để chổi không mòn", "Để chổi không gãy"], 0, "Lợi về quãng đường quét nhanh."),
            make_mc(10, "Thông hiểu", "Cơ bắp tay người bám vào xương cẳng tay cách khớp khuỷu 4 cm, quả tạ cầm ở tay cách khớp khuỷu 32 cm. Để giữ quả tạ 50 N, cơ bắp tay phải co lực kéo là:", ["400 N", "50 N", "6,25 N", "200 N"], 0, "F_cơ = 50 × 32 / 4 = 400 N (gấp 8 lần trọng lượng tạ)."),
            make_mc(11, "Thông hiểu", "Tại sao người ta lại chế tạo đòn bẩy loại 3 dù biết rằng nó bị thiệt về lực?", ["Vì trong nhiều thao tác, sự nhanh nhẹn, khéo léo và vươn xa quãng đường quan trọng hơn lực nâng", "Để tập thể dục", "Vì tiết kiệm vật liệu", "Vì không làm được loại khác"], 0, "Lợi về tốc độ, quãng đường và sự khéo léo."),
            make_mc(12, "Thông hiểu", "Cần gạt nước trên kính chắn gió ô tô hoạt động theo nguyên lí đòn bẩy loại 3 nhằm:", ["Lưỡi gạt cao su quét được diện tích kính chắn gió rất rộng và nhanh chóng", "Lợi về lực kéo", "Để gạt nước chậm", "Để kính không xước"], 0, "Quét diện tích rộng và nhanh.")
        ],
        [
            make_tf(1, "Thông hiểu", "Đặc điểm của đòn bẩy loại 3:", [
                ("a", "Điểm tác dụng lực luôn nằm giữa điểm tựa O và vật.", True),
                ("b", "Cánh tay đòn của lực tác dụng luôn ngắn hơn cánh tay đòn của tải trọng.", True),
                ("c", "Đòn bẩy loại 3 luôn cho ta thiệt về lực (F1 > F2).", True),
                ("d", "Đòn bẩy loại 3 giúp ta được lợi về công cơ học.", False)
            ], "Không máy cơ nào cho ta lợi về công."),
            make_tf(2, "Thông hiểu", "Cấu tạo sinh học cánh tay người:", [
                ("a", "Khớp khuỷu tay là điểm tựa O.", True),
                ("b", "Cơ nhị đầu bắp tay bám vào xương cẳng tay ở vị trí gần khớp khuỷu tay.", True),
                ("c", "Vật nặng đặt trên lòng bàn tay cách xa khớp khuỷu tay.", True),
                ("d", "Cơ bắp tay chỉ cần co một lực nhỏ hơn trọng lượng vật là nâng được vật.", False)
            ], "Cơ bắp tay phải co lực lớn gấp nhiều lần trọng lượng vật do d_cơ rất ngắn."),
            make_tf(3, "Vận dụng", "Dùng chiếc cần câu cá dài 2,4 m. Tay dưới giữ chuôi cần làm điểm tựa O, tay trên kéo cần ở vị trí cách chuôi 0,4 m. Con cá mắc câu kéo đầu cần với lực 20 N:", [
                ("a", "Cánh tay đòn của con cá là d2 = 2,4 m.", True),
                ("b", "Cánh tay đòn của tay kéo là d1 = 0,4 m.", True),
                ("c", "Lực kéo của tay người tác dụng lên cần câu là 120 N.", True),
                ("d", "Người câu cá được lợi 6 lần về lực.", False)
            ], "Thiệt 6 lần về lực: 120 N > 20 N."),
            make_tf(4, "Vận dụng", "Dùng kẹp gắp bánh dài 25 cm, tay bóp ở điểm cách khớp tựa 5 cm để gắp chiếc bánh nặng 2 N:", [
                ("a", "Đây là đòn bẩy loại 3 có điểm tựa ở đuôi kẹp.", True),
                ("b", "Cánh tay đòn d1 = 5 cm, d2 = 25 cm.", True),
                ("c", "Lực tay bóp tối thiểu là 10 N.", True),
                ("d", "Khi tay bóp di chuyển 1 cm thì hai đầu kẹp khép lại 0,2 cm.", False)
            ], "Đầu kẹp khép lại 1 × (25 / 5) = 5 cm (lợi 5 lần về đường đi).")
        ],
        [
            make_sa(1, "Thông hiểu", "Đòn bẩy loại 3 có d1 = 10 cm, d2 = 50 cm. Thiệt về lực bao nhiêu lần?", "5", "50 / 10 = 5 lần."),
            make_sa(2, "Thông hiểu", "Cần câu dài 2 m, tay kéo cách điểm tựa 0,5 m. Để giữ cá kéo 15 N cần lực tay bao nhiêu Newton?", "60", "15 × 2 / 0,5 = 60 N."),
            make_sa(3, "Vận dụng", "Kẹp gắp than dài 40 cm, tay cầm ở điểm cách khớp 10 cm. Gắp cục than nặng 5 N thì lực tay bóp là bao nhiêu Newton?", "20", "5 × 40 / 10 = 20 N."),
            make_sa(4, "Vận dụng", "Cơ bắp tay bám cách khuỷu 3 cm, tay cầm vật nặng 40 N cách khuỷu 30 cm. Lực co của cơ bắp tay là bao nhiêu Newton?", "400", "40 × 30 / 3 = 400 N."),
            make_sa(5, "Vận dụng cao", "Chổi quét nhà dài 1,2 m, tay đẩy cách điểm tựa trên 0,3 m. Khi tay đẩy di chuyển 10 cm thì đầu chổi quét di chuyển bao nhiêu cm?", "40", "10 × (1,2 / 0,3) = 40 cm."),
            make_sa(6, "Vận dụng cao", "Dùng nhíp gắp linh kiện điện tử dài 12 cm, tay ấn cách đầu tựa 4 cm. Để tạo lực kẹp 0,5 N lên linh kiện thì lực tay ấn là bao nhiêu Newton?", "1.5", "0,5 × 12 / 4 = 1,5 N.")
        ],
        [
            make_vdc(1, "Trong giải phẫu cơ thể người, khi nâng một quả tạ 8 kg (trọng lượng 80 N) trên bàn tay, cẳng tay dài 32 cm nằm ngang, điểm bám của cơ bắp tay cách khớp khuỷu 4 cm (g = 10 m/s²). Lực co cơ bắp tay phải sinh ra là 640 N. Ý nghĩa sinh học sâu sắc của cấu tạo đòn bẩy loại 3 này là:", ["Tuy thiệt 8 lần về lực nhưng giúp bàn tay có thể cử động linh hoạt, nhanh nhẹn và vươn rộng biên độ góc lớn chỉ với một độ co cơ rất nhỏ", "Để cơ thể tốn nhiều calo", "Để cơ bắp tay to hơn", "Không có ý nghĩa gì"], 0, "Lợi về tốc độ, góc cử động và biên độ di chuyển của bàn tay."),
            make_vdc(2, "Cần cẩu xúc đất (máy đào đất) có cánh tay gầu xúc hoạt động nhờ xi lanh thủy lực đẩy ở giữa cần. Đây là mô hình ứng dụng của:", ["Đòn bẩy loại 3 giúp gầu xúc có thể vươn xa và xúc đất nhanh với biên độ rộng", "Đòn bẩy loại 1", "Đòn bẩy loại 2", "Mặt phẳng nghiêng"], 0, "Đòn bẩy loại 3 giúp gầu xúc vươn xa và di chuyển nhanh."),
            make_vdc(3, "Một vận động viên chèo thuyền kayak dùng mái chèo dài 2,2 m. Tay trên giữ cố định làm điểm tựa O, tay dưới kéo mái chèo ở vị trí cách tay trên 0,6 m. Nước cản mái chèo với lực 90 N tác dụng ở tâm lưỡi chèo cách điểm tựa 1,8 m. Lực kéo của tay dưới là:", ["270 N", "180 N", "330 N", "90 N"], 0, "F = 90 × 1,8 / 0,6 = 270 N."),
            make_vdc(4, "Một cây vợt cầu lông dài 68 cm. Vận động viên vung cổ tay (điểm tựa O) tác dụng lực kéo cách cổ tay 10 cm. Tỉ số vận tốc vung đầu vợt cầu lông so với vận tốc chuyển động của tay là:", ["Nhanh hơn 6,8 lần", "Nhanh hơn 3,4 lần", "Nhanh hơn 2 lần", "Bằng nhau"], 0, "Tỉ số vận tốc = tỉ số bán kính = 68 / 10 = 6,8 lần giúp quả cầu bay siêu nhanh.")
        ]
    )

    # =========================================================================
    # PHYS8_C4_REV: [ĐỀ TỔNG HỢP] ÔN TẬP CUỐI CHƯƠNG IV (5 ĐỀ)
    # =========================================================================
    lrev_id = "phys8_c4_rev"
    lrev_name = "[Đề tổng hợp] Ôn tập cuối Chương IV"

    # --- REV ĐỀ 1 ---
    exams[f"{lrev_id}_test1"] = meta(lrev_id, lrev_name, 1,
        [
            make_mc(1, "Nhận biết", "Moment lực đặc trưng cho tác dụng nào của lực?", ["Tác dụng làm quay của lực quanh một trục", "Tác dụng làm biến dạng vật", "Tác dụng làm vật chuyển động thẳng", "Tác dụng cản trở chuyển động"], 0, "Tác dụng làm quay quanh một trục."),
            make_mc(2, "Nhận biết", "Cánh tay đòn của lực là:", ["Khoảng cách vuông góc từ trục quay đến giá của lực", "Chiều dài của đòn bẩy", "Khoảng cách từ điểm đặt lực đến vật", "Độ dài dây kéo"], 0, "Khoảng cách vuông góc từ trục quay đến giá của lực."),
            make_mc(3, "Nhận biết", "Đơn vị đo của moment lực là:", ["N.m", "N/m", "Joule", "Watt"], 0, "N.m."),
            make_mc(4, "Nhận biết", "Quy tắc moment lực dùng để xác định điều kiện:", ["Cân bằng của vật có trục quay cố định", "Chuyển động thẳng đều", "Rơi tự do", "Nổi trên mặt nước"], 0, "Điều kiện cân bằng vật có trục quay."),
            make_mc(5, "Nhận biết", "Đòn bẩy loại 1 có vị trí các điểm:", ["Điểm tựa O nằm giữa điểm đặt lực và vật", "Vật nằm ở giữa", "Lực nằm ở giữa", "Không có điểm tựa"], 0, "O ở giữa."),
            make_mc(6, "Nhận biết", "Đòn bẩy loại 2 luôn cho ta ưu điểm:", ["Được lợi về lực", "Được lợi về đường đi", "Được lợi về công", "Làm vật nhẹ đi"], 0, "Được lợi về lực."),
            make_mc(7, "Thông hiểu", "Lực 30 N vuông góc cánh tay đòn 0,5 m sinh ra moment là:", ["15 N.m", "60 N.m", "6 N.m", "150 N.m"], 0, "30 × 0,5 = 15 N.m."),
            make_mc(8, "Thông hiểu", "Đòn bẩy thăng bằng: F1 = 40 N có d1 = 0,3 m. Lực F2 có d2 = 0,6 m thì F2 bằng:", ["20 N", "80 N", "40 N", "10 N"], 0, "40 × 0,3 / 0,6 = 20 N."),
            make_mc(9, "Thông hiểu", "Kìm cắt dây thép cán dài 20 cm, lưỡi dài 4 cm cho ta lợi về lực:", ["5 lần", "4 lần", "20 lần", "80 lần"], 0, "20 / 4 = 5 lần."),
            make_mc(10, "Thông hiểu", "Xe cút kít chở đất là ví dụ điển hình của:", ["Đòn bẩy loại 2", "Đòn bẩy loại 1", "Đòn bẩy loại 3", "Mặt phẳng nghiêng"], 0, "Đòn bẩy loại 2."),
            make_mc(11, "Thông hiểu", "Kẹp gắp đá thức ăn là ví dụ điển hình của:", ["Đòn bẩy loại 3", "Đòn bẩy loại 1", "Đòn bẩy loại 2", "Ròng rọc"], 0, "Đòn bẩy loại 3."),
            make_mc(12, "Thông hiểu", "Khi lực tác dụng có giá đi qua trục quay thì moment lực bằng:", ["0", "Bằng độ lớn của lực", "Vô cùng lớn", "Bằng 1 N.m"], 0, "d = 0 nên M = 0.")
        ],
        [
            make_tf(1, "Thông hiểu", "Kiến thức cốt lõi về moment lực và đòn bẩy:", [
                ("a", "Moment lực tỉ lệ thuận với độ lớn của lực và cánh tay đòn.", True),
                ("b", "Đòn bẩy loại 1 có thể lợi về lực hoặc lợi về đường đi tùy vị trí điểm tựa.", True),
                ("c", "Đòn bẩy loại 2 luôn có cánh tay đòn của lực lớn hơn tải trọng.", True),
                ("d", "Đòn bẩy loại 3 cho ta lợi về lực nhưng thiệt về quãng đường.", False)
            ], "Đòn bẩy loại 3 thiệt về lực nhưng lợi về quãng đường."),
            make_tf(2, "Thông hiểu", "Nhận dạng đòn bẩy trong các dụng cụ đời sống:", [
                ("a", "Bập bênh là đòn bẩy loại 1 có trục quay ở giữa.", True),
                ("b", "Khui nắp chai nước ngọt là đòn bẩy loại 2.", True),
                ("c", "Cần câu cá là đòn bẩy loại 3.", True),
                ("d", "Kéo cắt kim loại là đòn bẩy loại 2.", False)
            ], "Kéo cắt kim loại là đòn bẩy loại 1 (trục vít ở giữa)."),
            make_tf(3, "Vận dụng", "Thanh nhẹ dài 1,5 m quay quanh trục O ở đầu A. Treo vật nặng 200 N ở điểm cách O 0,5 m. Tác dụng lực F hướng lên ở đầu B:", [
                ("a", "Khoảng cách từ O đến điểm đặt lực nâng ở B là 1,5 m.", True),
                ("b", "Moment của trọng lực vật đối với O là 100 N.m.", True),
                ("c", "Lực nâng F tối thiểu ở đầu B để giữ thanh nằm ngang là khoảng 66,7 N.", True),
                ("d", "Hệ này hoạt động theo nguyên lí đòn bẩy loại 3.", False)
            ], "Vật ở giữa điểm tựa O và lực F => Đòn bẩy loại 2."),
            make_tf(4, "Vận dụng", "Một người gánh hai tải hàng P1 = 400 N và P2 = 200 N bằng đòn dài 1,8 m đặt trên vai:", [
                ("a", "Tổng áp lực lên vai người gánh là 600 N (bỏ qua trọng lượng đòn).", True),
                ("b", "Khoảng cách từ vai đến tải P1 là 0,6 m.", True),
                ("c", "Khoảng cách từ vai đến tải P2 là 1,2 m.", True),
                ("d", "Nếu đổi vị trí vai sang chính giữa đòn thì vai chịu lực ít hơn.", False)
            ], "Tổng lực lên vai vẫn là 600 N nhưng đòn bị lệch không thăng bằng.")
        ],
        [
            make_sa(1, "Thông hiểu", "Lực F = 60 N có cánh tay đòn 0,4 m. Moment lực là bao nhiêu N.m?", "24", "60 × 0,4 = 24 N.m."),
            make_sa(2, "Thông hiểu", "Đòn bẩy có d1 = 50 cm, d2 = 10 cm. Lợi về lực bao nhiêu lần?", "5", "50 / 10 = 5 lần."),
            make_sa(3, "Vận dụng", "Hai bạn chơi bập bênh: bạn A 40 kg cách trục 1,5 m. Bạn B cách trục 2,0 m thăng bằng. Bạn B nặng bao nhiêu kg?", "30", "40 × 1,5 / 2 = 30 kg."),
            make_sa(4, "Vận dụng", "Xe cút kít nâng đống cát 800 N cách bánh xe 0,3 m. Tay cầm cách bánh xe 1,2 m. Lực nâng là bao nhiêu Newton?", "200", "800 × 0,3 / 1,2 = 200 N."),
            make_sa(5, "Vận dụng cao", "Thanh đồng chất dài 2 m nặng 50 N quay quanh trục O ở đầu mút. Giữ thanh nằm ngang cần lực nâng ở đầu kia bao nhiêu Newton?", "25", "F = 50 × 1 / 2 = 25 N."),
            make_sa(6, "Vận dụng cao", "Kìm cắt thép có cán 18 cm, lưỡi 2 cm. Lực tay bóp 150 N sinh ra lực cắt trên dây thép là bao nhiêu Newton?", "1350", "150 × 18 / 2 = 1 350 N.")
        ],
        [
            make_vdc(1, "Một người dùng xà beng dài 1,2 m bẩy một tảng đá 1 500 N. Điểm tựa cách tảng đá 20 cm. Lực ấn tối thiểu người đó phải tác dụng vào đầu kia là:", ["300 N", "250 N", "500 N", "150 N"], 0, "d1 = 1,0 m; d2 = 0,2 m => F = 1 500 × 0,2 / 1,0 = 300 N."),
            make_vdc(2, "Cần cẩu tháp xây dựng cao tầng có tay nâng dài vươn ra 40 m mang tải trọng tối đa 5 tấn (50 000 N, g = 10 m/s²). Cần đối trọng phía sau dài 10 m. Khối lượng tối thiểu của khối bê tông đối trọng phía sau là:", ["20 tấn (200 000 N)", "15 tấn", "10 tấn", "5 tấn"], 0, "M_đối trọng = 50 000 × 40 = 2 000 000 N.m => P_đối trọng = 2 000 000 / 10 = 200 000 N => 20 tấn."),
            make_vdc(3, "Một chiếc thang dài 4 m nặng 250 N có trọng tâm ở giữa tựa vào tường trơn nhẵn tại điểm cao 3,2 m (chân thang cách tường d = √(4² - 3,2²) = 2,4 m). Lực đẩy của tường lên đầu thang là:", ["93,75 N", "125 N", "150 N", "80 N"], 0, "N × 3,2 = 250 × 1,2 = 300 => N = 93,75 N."),
            make_vdc(4, "Trong cơ thể người, khi kiễng gót chân, khớp ngón chân là điểm tựa O, trọng lượng cơ thể 600 N dồn lên cẳng chân cách ngón chân 10 cm, gân gót kéo cách ngón chân 15 cm. Lực kéo của gân gót chân là:", ["400 N", "600 N", "900 N", "300 N"], 0, "F_gân × 15 = 600 × 10 => F_gân = 400 N.")
        ]
    )

    # --- REV ĐỀ 2, 3, 4, 5 ---
    for t_idx in range(2, 6):
        t = t_idx
        p1 = [
            make_mc(1, "Nhận biết", f"Đại lượng đặc trưng cho tác dụng làm quay của lực trong bài kiểm tra số {t} là:", ["Moment lực", "Áp suất", "Khối lượng riêng", "Nhiệt lượng"], 0, "Moment lực M = F.d."),
            make_mc(2, "Nhận biết", f"Công thức nào sau đây dùng để tính moment lực đối với trục quay trong đề {t}?", ["M = F × d", "M = F / d", "M = d / F", "M = p × S"], 0, "M = F.d."),
            make_mc(3, "Nhận biết", f"Đơn vị đo chuẩn của moment lực trong hệ SI ở bài số {t} là:", ["N.m", "Joule", "Pascal", "Watt"], 0, "N.m."),
            make_mc(4, "Nhận biết", f"Trong đòn bẩy loại 2 ở đề thi số {t}, vị trí của tải trọng là:", ["Nằm ở giữa điểm tựa O và điểm tác dụng lực", "Nằm ở ngoài cùng", "Điểm tựa nằm ở giữa", "Lực nằm ở giữa"], 0, "Đòn bẩy loại 2: tải trọng ở giữa."),
            make_mc(5, "Nhận biết", f"Trong đòn bẩy loại 3 ở đề thi số {t}, vị trí của lực tác dụng là:", ["Nằm ở giữa điểm tựa O và tải trọng", "Nằm ở ngoài cùng", "Điểm tựa ở giữa", "Tải trọng ở giữa"], 0, "Đòn bẩy loại 3: lực ở giữa."),
            make_mc(6, "Nhận biết", f"Dụng cụ nào sau đây là đòn bẩy loại 1 trong nội dung đề {t}?", ["Cái bập bênh, kéo cắt giấy, kìm kẹp", "Xe rùa chở cát", "Cần câu cá", "Kẹp gắp than"], 0, "Đòn bẩy loại 1 có trục ở giữa."),
            make_mc(7, "Thông hiểu", f"Lực F = {20 + t * 5} N vuông góc với cánh tay đòn d = 0,2 m. Moment lực trong bài {t} là:", [f"{(20 + t * 5) * 0.2:.1f} N.m", "10 N.m", "25 N.m", "5 N.m"], 0, f"M = F.d = {(20 + t * 5) * 0.2:.1f} N.m."),
            make_mc(8, "Thông hiểu", f"Đòn bẩy có d1 = {40 + t * 10} cm, d2 = 20 cm. Lợi về lực trong đề {t} là:", [f"{(40 + t * 10) / 20:.1f} lần", "2 lần", "5 lần", "10 lần"], 0, f"Lợi {(40 + t * 10) / 20:.1f} lần."),
            make_mc(9, "Thông hiểu", f"Kéo cắt kim loại cán dài {15 + t * 3} cm, lưỡi dài 3 cm. Tỉ số lợi về lực trong bài {t} là:", [f"{(15 + t * 3) / 3:.0f} lần", "3 lần", "4 lần", "2 lần"], 0, f"Lợi {(15 + t * 3) / 3:.0f} lần."),
            make_mc(10, "Thông hiểu", f"Xe cút kít chở đất nặng {500 + t * 50} N có d2 = 40 cm, d1 = 120 cm. Lực nâng tay ở đề {t} là:", [f"{(500 + t * 50) / 3:.0f} N", "500 N", "250 N", "100 N"], 0, f"F = P/3 = {(500 + t * 50) / 3:.0f} N."),
            make_mc(11, "Thông hiểu", f"Nhíp gắp linh kiện điện tử dài {10 + t} cm, bóp tay ở vị trí {2 + t * 0.5:.1f} cm là ứng dụng:", ["Đòn bẩy loại 3", "Đòn bẩy loại 1", "Đòn bẩy loại 2", "Ròng rọc"], 0, "Đòn bẩy loại 3."),
            make_mc(12, "Thông hiểu", f"Hai người khiêng vật nặng {400 + t * 50} N bằng đòn dài 2 m, vật ở chính giữa đòn. Lực mỗi người gánh ở đề {t} là:", [f"{(400 + t * 50) / 2:.0f} N", "400 N", "200 N", "100 N"], 0, "Vật ở giữa thì chia đều mỗi người chịu một nửa.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Nhận định về moment lực và cánh tay đòn trong bài kiểm tra {t}:", [
                ("a", "Moment lực đặc trưng cho tác dụng làm quay của lực quanh trục.", True),
                ("b", "Cánh tay đòn là khoảng cách vuông góc từ trục quay đến giá của lực.", True),
                ("c", "Lực càng lớn và cánh tay đòn càng dài thì moment lực càng lớn.", True),
                ("d", "Lực có giá đi qua trục quay sinh ra moment lực cực đại.", False)
            ], "Giá qua trục quay thì M = 0."),
            make_tf(2, "Thông hiểu", f"So sánh 3 loại đòn bẩy trong đề thi số {t}:", [
                ("a", "Đòn bẩy loại 1 có điểm tựa O nằm ở giữa tải trọng và lực tác dụng.", True),
                ("b", "Đòn bẩy loại 2 luôn cho ta lợi về lực vì d1 > d2.", True),
                ("c", "Đòn bẩy loại 3 cho ta thiệt về lực nhưng lợi về đường đi và vận tốc.", True),
                ("d", "Đòn bẩy loại 2 cho ta lợi về cả lực và công cơ học.", False)
            ], "Định luật bảo toàn công: không lợi về công."),
            make_tf(3, "Vận dụng", f"Thanh nhẹ thăng bằng quanh trục O có d1 = {0.2 * t:.1f} m, d2 = {0.4 * t:.1f} m trong đề {t}:", [
                ("a", "Cánh tay đòn d2 gấp đôi cánh tay đòn d1.", True),
                ("b", f"Nếu F1 = 100 N thì lực cân bằng F2 = 50 N.", True),
                ("c", "Tổng moment hai lực tác dụng quanh O triệt tiêu nhau bằng 0.", True),
                ("d", "Nếu tăng d1 gấp đôi thì lực F2 cần thiết tăng gấp đôi.", True)
            ], "F2 = F1.d1/d2."),
            make_tf(4, "Vận dụng", f"Xe rùa chở vật nặng {600 + t * 40} N, d_vật = 0,4 m, d_tay = 1,2 m trong đề {t}:", [
                ("a", "Tỉ số cánh tay đòn d_tay / d_vật là 3 lần.", True),
                ("b", f"Lực nâng tay cần thiết tối thiểu là {(600 + t * 40) / 3:.0f} N.", True),
                ("c", "Xếp vật lùi sát trục bánh xe giúp lực nâng tay giảm thêm.", True),
                ("d", "Khi tay nâng lên 15 cm thì đống hàng cũng nâng lên đúng 15 cm.", False)
            ], "Hàng nâng lên 15 / 3 = 5 cm (thiệt về đường đi).")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Lực F = {30 + t * 10} N có cánh tay đòn d = 0,2 m. Moment lực là bao nhiêu N.m?", f"{(30 + t * 10) * 0.2:.1f}", f"M = {(30 + t * 10) * 0.2:.1f} N.m."),
            make_sa(2, "Thông hiểu", f"Đòn bẩy loại 1 có d1 = {60 + t * 5} cm, d2 = 15 cm. Tỉ số lợi về lực là bao nhiêu lần?", f"{(60 + t * 5) / 15:.1f}", f"{(60 + t * 5) / 15:.1f} lần."),
            make_sa(3, "Vận dụng", f"Cần câu cá dài {1.6 + t * 0.2:.1f} m, tay kéo cách điểm tựa 0,4 m. Cá kéo {10 + t * 5} N thì lực kéo của tay là bao nhiêu Newton?", f"{int((10 + t * 5) * (1.6 + t * 0.2) / 0.4)}", f"{(10 + t * 5)} × {1.6 + t * 0.2:.1f} / 0,4 N."),
            make_sa(4, "Vận dụng", f"Xe cút kít nâng hàng {750 + t * 30} N có d2 = 0,3 m, d1 = 0,9 m. Lực nâng tay là bao nhiêu Newton?", f"{(750 + t * 30) // 3}", f"{(750 + t * 30) // 3} N."),
            make_sa(5, "Vận dụng cao", f"Thanh đồng chất dài 1 m nặng {20 + t * 2} N quay quanh trục ở đầu mút. Lực nâng giữ thanh nằm ngang ở đầu kia là bao nhiêu Newton?", f"{(20 + t * 2) / 2:.1f}", f"{(20 + t * 2) / 2:.1f} N."),
            make_sa(6, "Vận dụng cao", f"Hai người khiêng vật nặng {600 + t * 60} N bằng đòn dài 3 m, vật cách người trước 1 m. Lực lên vai người trước là bao nhiêu Newton?", f"{(600 + t * 60) * 2 // 3}", f"{(600 + t * 60) * 2 // 3} N.")
        ]
        p4 = [
            make_vdc(1, f"Một cần cẩu tháp công trình cao tầng có tay nâng dài {30 + t * 2} m vươn ra mang tải trọng 4 tấn (40 000 N, g = 10 m/s²). Cần đối trọng phía sau dài 8 m. Trọng lượng tối thiểu của khối đối trọng bê tông phía sau ở đề {t} là:", [f"{40000 * (30 + t * 2) // 8} N", "100 000 N", "150 000 N", "80 000 N"], 0, f"P = 40 000 × {30 + t * 2} / 8 = {40000 * (30 + t * 2) // 8} N."),
            make_vdc(2, f"Trong cơ chế nhai thức ăn của hàm người, khớp thái dương hàm là điểm tựa O, cơ cắn kéo ở giữa cách khớp {3 + t * 0.2:.1f} cm, răng hàm cắn thức ăn cách khớp {6 + t * 0.4:.1f} cm. Đây là mô hình đòn bẩy loại mấy và có tác dụng gì?", ["Đòn bẩy loại 3 giúp cơ hàm cắn nhanh linh hoạt biên độ lớn", "Đòn bẩy loại 1", "Đòn bẩy loại 2", "Ròng rọc"], 0, "Cơ cắn ở giữa khớp và răng là đòn bẩy loại 3."),
            make_vdc(3, f"Một người dùng xà beng dài {1.2 + t * 0.1:.1f} m để bẩy tảng đá nặng {1200 + t * 100} N, điểm tựa kê cách tảng đá 0,2 m. Lực ấn tối thiểu vào đầu kia của xà beng ở đề {t} là:", [f"{int((1200 + t * 100) * 0.2 / (1.0 + t * 0.1))} N", "200 N", "300 N", "400 N"], 0, "F = P × d2 / d1."),
            make_vdc(4, f"Cánh tay robot công nghiệp nâng linh kiện điện tử hoạt động mô phỏng cánh tay người với khớp xoay O và pit-tông đẩy ở giữa cần. Ưu điểm nổi bật nhất của thiết kế đòn bẩy loại 3 này ở đề {t} là:", ["Lợi về quãng đường di chuyển và tốc độ linh hoạt của đầu kẹp gắp linh kiện", "Lợi về lực kéo", "Tiết kiệm điện năng", "Giảm kích thước động cơ"], 0, "Lợi về vận tốc và góc quay linh hoạt.")
        ]
        exams[f"{lrev_id}_test{t}"] = meta(lrev_id, lrev_name, t, p1, p2, p3, p4)

    return exams
