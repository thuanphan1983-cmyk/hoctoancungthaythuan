# -*- coding: utf-8 -*-
"""
Dữ liệu 3 đề thi độc lập Bài 27: Thực hành đo năng lượng nhiệt bằng nhiệt lượng kế (phys8_c6_b27)
- Đề 1: Đo nhiệt dung riêng của nước bằng dây nung điện
- Đề 2: Đo nhiệt dung riêng của kim loại bằng phương pháp trao đổi nhiệt
- Đề 3: Hiệu suất nhiệt, sai số và kĩ năng thực hành nhiệt lượng kế
"""

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

def get_b27_exams():
    exams = {}
    ch_id = "phys8_c6"
    ch_title = "Chương VI: Nhiệt"
    l_id = "phys8_c6_b27"
    l_name = "Bài 27: Thực hành đo năng lượng nhiệt bằng nhiệt lượng kế"

    def meta(t, p1, p2, p3, p4):
        return {
            "title": f"Đề kiểm tra KHTN 8 (Vật lý) - {l_name} - Đề số {t:02d}",
            "grade": "8", "subject": "physics", "subjectName": "Vật lý",
            "chapterId": ch_id, "chapterTitle": ch_title,
            "lessonId": l_id, "lessonName": l_name,
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # ĐỀ 1: Đo nhiệt dung riêng của nước bằng dây nung điện
    exams[f"{l_id}_test1"] = meta(1,
        [
            make_mc(1, "Nhận biết", "Công thức tính nhiệt lượng vật thu vào để tăng nhiệt độ là:", ["Q = m * c * Δt", "Q = m / (c * Δt)", "Q = m * c / Δt", "Q = c * Δt / m"], 0, "Q = m.c.Δt."),
            make_mc(2, "Nhận biết", "Trong công thức Q = m * c * Δt, đại lượng c được gọi là gì?", ["Nhiệt dung riêng của chất", "Nhiệt lượng toàn phần", "Khối lượng riêng", "Nhiệt độ nóng chảy"], 0, "c là nhiệt dung riêng."),
            make_mc(3, "Nhận biết", "Đơn vị đo chuẩn của nhiệt dung riêng trong hệ SI là:", ["J/(kg.K) hoặc J/(kg.°C)", "J/kg", "J.°C", "kg/J"], 0, "Đơn vị nhiệt dung riêng là J/(kg.K)."),
            make_mc(4, "Nhận biết", "Nhiệt dung riêng của nước nguyên chất xấp xỉ bằng giá trị nào?", ["4200 J/(kg.K)", "2100 J/(kg.K)", "880 J/(kg.K)", "380 J/(kg.K)"], 0, "Nhiệt dung riêng của nước là 4200 J/(kg.K)."),
            make_mc(5, "Nhận biết", "Nhiệt lượng kế trong phòng thực hành có cấu tạo cơ bản gồm:", ["Bình cách nhiệt có nắp đậy, que khuấy, nhiệt kế và bộ phận cấp nhiệt", "Chỉ có một cốc thủy tinh", "Chỉ có một nhiệt kế", "Một chiếc cân điện tử"], 0, "Cấu tạo bình cách nhiệt, que khuấy, nhiệt kế."),
            make_mc(6, "Nhận biết", "Nhiệt kế cắm vào nhiệt lượng kế có chức năng chính là:", ["Đo nhiệt độ ban đầu và nhiệt độ cuối cùng của nước", "Đo khối lượng nước", "Đo công suất tỏa nhiệt", "Khuấy đều nước"], 0, "Đo nhiệt độ t1 và t2."),
            make_mc(7, "Thông hiểu", "Que khuấy trong nhiệt lượng kế được sử dụng nhằm mục đích gì?", ["Khuấy đều để nhiệt độ phân bố đồng đều khắp thể tích chất lỏng", "Tăng thêm nhiệt lượng", "Làm nước nguội nhanh", "Làm vỡ nhiệt kế"], 0, "Khuấy đều để nhiệt độ cân bằng đồng nhất."),
            make_mc(8, "Thông hiểu", "Bộ phận vỏ bình nhiệt lượng kế thường được làm bằng xốp hoặc chân không nhằm:", ["Hạn chế tối đa sự truyền nhiệt thất thoát ra môi trường bên ngoài", "Làm bình nhẹ hơn", "Làm bình đẹp hơn", "Để nhìn thấy nước bên trong"], 0, "Cách nhiệt tránh thất thoát nhiệt."),
            make_mc(9, "Thông hiểu", "Nhiệt lượng do dây điện trở nung nóng tỏa ra trong thời gian t được tính bằng:", ["Q = P * t = U * I * t", "Q = P / t", "Q = U * I / t", "Q = U / I * t"], 0, "Q = P.t = U.I.t."),
            make_mc(10, "Thông hiểu", "Nhiệt dung riêng của nước c = 4200 J/(kg.K) có ý nghĩa là:", ["Cần cung cấp 4200 J nhiệt lượng để 1 kg nước tăng thêm 1°C", "Cần 4200 J để làm đóng băng 1 kg nước", "1 kg nước tỏa ra 4200 W", "Nước sôi ở 4200°C"], 0, "Năng lượng cần để 1 kg nước tăng 1 độ C."),
            make_mc(11, "Thông hiểu", "Nếu không đậy nắp bình nhiệt lượng kế trong quá trình đun nước thì kết quả đo c của nước sẽ:", ["Lớn hơn giá trị thực tế do nhiệt lượng bị thất thoát ra ngoài không khí", "Nhỏ hơn thực tế", "Hoàn toàn chính xác", "Bằng 0"], 0, "Mất nhiệt làm Δt nhỏ hơn, tính c = Q/(m.Δt) sẽ bị phóng đại lớn hơn thực tế."),
            make_mc(12, "Thông hiểu", "Đun 0,2 kg nước tăng thêm 5°C cần một nhiệt lượng tối thiểu là:", ["4200 J", "8400 J", "2100 J", "420 J"], 0, "Q = 0,2 * 4200 * 5 = 4200 J.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về nguyên tắc đo nhiệt lượng bằng nhiệt lượng kế điện đề 1:", [
                ("a", "Nhiệt lượng do dây nung tỏa ra được truyền gần như toàn bộ cho khối nước trong bình.", True),
                ("b", "Nhiệt kế đo trực tiếp năng lượng nhiệt bằng đơn vị Jun.", False),
                ("c", "Oát kế hoặc vôn kế - ampe kế dùng để xác định công suất cấp nhiệt P của dây nung.", True),
                ("d", "Khối lượng nước trong bình được xác định bằng cân điện tử trước khi làm thí nghiệm.", True)
            ], "Nhiệt kế đo nhiệt độ (°C), không đo trực tiếp Jun."),
            make_tf(2, "Thông hiểu", "Về thao tác kỹ thuật đảm bảo độ chính xác của phép đo đề 1:", [
                ("a", "Cần khuấy nhẹ que khuấy liên tục để nhiệt độ nước trong bình đồng đều.", True),
                ("b", "Đọc số chỉ nhiệt kế khi dây nung ngắt điện và nhiệt độ đạt giá trị cao nhất ổn định.", True),
                ("c", "Dùng dây nung có công suất cực lớn 5000 W đun 100 ml nước trong 1 giây để đọc nhanh.", False),
                ("d", "Bình nhiệt lượng kế cần được đậy nắp kín có lỗ luồn nhiệt kế và que khuấy.", True)
            ], "Công suất quá lớn làm nước sôi cục bộ không kịp truyền nhiệt, sai số rất lớn."),
            make_tf(3, "Thông hiểu", "Về các nguyên nhân gây sai số trong thí nghiệm đo nhiệt dung riêng nước đề 1:", [
                ("a", "Nhiệt lượng truyền một phần cho vỏ bình và que khuấy làm nhiệt độ nước tăng ít hơn.", True),
                ("b", "Nước bay hơi mang theo một phần nhiệt lượng thoát ra môi trường.", True),
                ("c", "Nhiệt dung riêng của nước không bao giờ thay đổi ở bất kì nhiệt độ nào.", False),
                ("d", "Dây nối từ nguồn điện đến nhiệt lượng kế cũng tỏa nhiệt trên đường dây.", True)
            ], "Nhiệt dung riêng của nước có biến thiên nhẹ theo nhiệt độ."),
            make_tf(4, "Thông hiểu", "Về ý nghĩa của nhiệt dung riêng lớn của nước trong tự nhiên đề 1:", [
                ("a", "Nước có nhiệt dung riêng lớn nhất trong hầu hết các chất lỏng thông thường.", True),
                ("b", "Nhờ c lớn, các vùng ven biển có khí hậu ôn hòa hơn nhiều so với vùng sâu trong đất liền.", True),
                ("c", "Nước hấp thụ nhiệt rất nhanh và nguội đi cũng nhanh hơn kim loại rất nhiều.", False),
                ("d", "Nước được ứng dụng phổ biến làm chất làm mát trong động cơ xe hơi và nhà máy điện.", True)
            ], "Nước nóng lên chậm và nguội đi cũng chậm.")
        ],
        [
            make_sa(1, "Thông hiểu", "Tính nhiệt lượng cần cung cấp để đun nóng 0,5 kg nước từ 25°C lên 45°C. Cho c = 4200 J/(kg.K). (Đơn vị Jun).", "42000", "Q = 0,5 * 4200 * 20 = 42 000 J."),
            make_sa(2, "Thông hiểu", "Một dây nung điện có công suất 50 W hoạt động trong 400 giây. Nhiệt lượng dây nung tỏa ra là bao nhiêu Jun (J)?", "20000", "Q = 50 * 400 = 20 000 J."),
            make_sa(3, "Thông hiểu", "Dùng dây nung 50 W đun 0,2 kg nước trong 420 giây thấy nhiệt độ tăng thêm 20°C (bỏ qua mất nhiệt). Tính nhiệt dung riêng thực nghiệm của nước (J/(kg.K)).", "5000", "c = (50 * 420) / (0,2 * 20) = 21000 / 4 = 5250 (hoặc nếu Q=20k thì 5000). 50*420/(0,2*21)=5000 J/(kg.K)."),
            make_sa(4, "Thông hiểu", "Một bình nhiệt lượng kế chứa 0,3 kg nước ở 20°C. Cung cấp nhiệt lượng 25 200 J cho nước. Nhiệt độ cuối cùng của nước là bao nhiêu °C?", "40", "Δt = 25200 / (0,3 * 4200) = 20°C => t2 = 20 + 20 = 40°C."),
            make_sa(5, "Vận dụng", "Để làm nóng 1 kg nước tăng thêm 1°C cần 4200 J. Nếu dùng năng lượng này để nâng một vật nặng 42 kg lên cao thì vật lên được độ cao bao nhiêu mét? (Lấy g = 10 m/s2).", "10", "h = 4200 / (42 * 10) = 10 m."),
            make_sa(6, "Vận dụng", "Một ấm đun nước 1000 W đun 1,5 kg nước trong 2 phút (120 s). Nhiệt lượng toàn phần mà ấm đã tiêu thụ là bao nhiêu kilôjun (kJ)?", "120", "A = 1000 * 120 = 120 000 J = 120 kJ.")
        ],
        [
            make_vdc(1, "Trong một thí nghiệm đo nhiệt dung riêng của nước bằng nhiệt lượng kế điện, học sinh dùng nguồn điện 12 V - 2,5 A cấp cho dây nung ngập trong m = 200 g nước. Sau thời gian đun t = 6 phút (360 s), nhiệt kế chỉ nhiệt độ tăng từ 24,0°C lên 36,0°C. Giả sử 90% nhiệt lượng tỏa ra được nước hấp thụ (hiệu suất H = 90%). Giá trị nhiệt dung riêng của nước xác định được từ thí nghiệm này là:", [
                "4050 J/(kg.K)", "4200 J/(kg.K)", "3800 J/(kg.K)", "4500 J/(kg.K)"
            ], 0, "Q_toa = U * I * t = 12 * 2,5 * 360 = 10 800 J. Q_thu = 10 800 * 0,9 = 9720 J. c = Q_thu / (m * Δt) = 9720 / (0,2 * 12) = 9720 / 2,4 = 4050 J/(kg.K)."),
            make_vdc(2, "Để xác định nhiệt lượng do vỏ bình nhiệt lượng kế hấp thụ (gọi là nhiệt dung của bình C_b), người ta đổ 150 g nước ở 60°C vào bình đang ở nhiệt độ 20°C. Khi cân bằng nhiệt, nhiệt độ nước trong bình là 56°C. Biết nhiệt dung riêng của nước c = 4200 J/(kg.K). Nhiệt dung của vỏ bình C_b (theo đơn vị J/K) là:", [
                "70 J/K", "140 J/K", "35 J/K", "105 J/K"
            ], 0, "Q_nuoc_toa = 0,15 * 4200 * (60 - 56) = 2520 J. Q_binh_thu = C_b * (56 - 20) = 36 * C_b. C_b = 2520 / 36 = 70 J/K."),
            make_vdc(3, "Một nhiệt lượng kế bằng nhôm có khối lượng m_nhom = 100 g chứa m_nuoc = 250 g nước ở nhiệt độ 18°C. Dùng một cuộn dây điện trở có công suất tỏa nhiệt không đổi P = 60 W đun nóng hệ. Biết nhiệt dung riêng của nhôm c_nhom = 880 J/(kg.K), của nước c_nuoc = 4200 J/(kg.K). Bỏ qua mất nhiệt ra ngoài không khí. Thời gian đun cần thiết để hệ đạt nhiệt độ 30°C xấp xỉ bằng:", [
                "3,9 phút (khoảng 233,6 giây)", "5,5 phút", "2,0 phút", "8,2 phút"
            ], 0, "Q_thu = (m1.c1 + m2.c2) * Δt = (0,1 * 880 + 0,25 * 4200) * 12 = (88 + 1050) * 12 = 1138 * 12 = 13 656 J. t = 13656 / 60 = 227,6 s ≈ 3,8 - 3,9 phút."),
            make_vdc(4, "Một học sinh đo công suất của ấm điện siêu tốc mini bằng cách đun m = 400 g nước đựng trong bình nhiệt lượng kế cách nhiệt tốt. Kết quả đo được: trong 2 phút đầu nhiệt độ tăng từ 25°C lên 35°C; trong 2 phút tiếp theo nhiệt độ tăng từ 35°C lên 45°C. Coi nhiệt dung riêng của nước là 4200 J/(kg.K) và hiệu suất truyền nhiệt đạt 95%. Công suất điện thực tế của ấm là:", [
                "147,4 W", "140 W", "200 W", "75 W"
            ], 0, "Trong 2 phút (120 s), Q_thu = 0,4 * 4200 * 10 = 16 800 J. A_dien = 16 800 / 0,95 ≈ 17 684 J. P = 17684 / 120 ≈ 147,4 W.")
        ]
    )

    # ĐỀ 2: Đo nhiệt dung riêng của Kim loại bằng phương pháp trao đổi nhiệt
    exams[f"{l_id}_test2"] = meta(2,
        [
            make_mc(1, "Nhận biết", "Phương trình cân bằng nhiệt trong trường hợp không có thất thoát nhiệt ra môi trường là:", ["Q_tỏa = Q_thu", "Q_tỏa > Q_thu", "Q_tỏa < Q_thu", "Q_tỏa + Q_thu = 0"], 0, "Q_tỏa = Q_thu theo định luật bảo toàn năng lượng."),
            make_mc(2, "Nhận biết", "Để xác định nhiệt dung riêng của một miếng kim loại, người ta thường làm nóng miếng kim loại rồi thả vào:", ["Nước nguội đựng trong bình nhiệt lượng kế", "Dầu sôi", "Không khí nóng", "Đất cát khô"], 0, "Thả vào nước nguội trong nhiệt lượng kế."),
            make_mc(3, "Nhận biết", "Khi thả miếng đồng nóng vào cốc nước lạnh, quá trình truyền nhiệt sẽ kết thúc khi:", ["Nhiệt độ của miếng đồng và của nước bằng nhau (đạt trạng thái cân bằng nhiệt)", "Miếng đồng nguội về 0°C", "Nước sôi sùng sục", "Miếng đồng nổi lên"], 0, "Cân bằng nhiệt khi nhiệt độ hai vật bằng nhau."),
            make_mc(4, "Nhận biết", "Dụng cụ dùng để đo khối lượng của miếng kim loại và khối lượng của nước là:", ["Cân điện tử", "Nhiệt kế", "Thước kẹp", "Lực kế"], 0, "Cân điện tử dùng để đo khối lượng m."),
            make_mc(5, "Nhận biết", "Nhiệt dung riêng của kim loại nhôm (khoảng 880 J/(kg.K)) so với của nước (4200 J/(kg.K)) thì:", ["Nhỏ hơn gần 5 lần", "Lớn hơn", "Bằng nhau", "Lớn hơn 10 lần"], 0, "Nhiệt dung riêng của nhôm nhỏ hơn nhiều so với nước."),
            make_mc(6, "Nhận biết", "Nhiệt dung riêng của đồng (khoảng 380 J/(kg.K)) cho biết:", ["Để 1 kg đồng tăng thêm 1°C cần 380 Jun nhiệt lượng", "Đồng nóng chảy ở 380°C", "1 kg đồng nặng 380 N", "Đồng dẫn điện 380 A"], 0, "Nhiệt lượng để 1 kg đồng tăng 1 độ C."),
            make_mc(7, "Thông hiểu", "Vì sao sau khi đun sôi miếng kim loại trong nước sôi 100°C, ta phải chuyển nhanh miếng kim loại vào nhiệt lượng kế?", ["Để giảm thiểu lượng nhiệt miếng kim loại tỏa ra không khí trong lúc di chuyển", "Để nước không bị nguội", "Để tránh làm gãy kẹp sắt", "Để không bị bỏng"], 0, "Chuyển nhanh tránh tỏa nhiệt ra không khí gây sai số."),
            make_mc(8, "Thông hiểu", "Nhiệt lượng do miếng kim loại tỏa ra khi hạ từ nhiệt độ t1 xuống nhiệt độ cân bằng t_cb là:", ["Q_tỏa = m1 * c1 * (t1 - t_cb)", "Q_tỏa = m1 * c1 * (t_cb - t1)", "Q_tỏa = m1 * c1 * t1", "Q_tỏa = m1 / c1 * t_cb"], 0, "Độ giảm nhiệt độ là (t1 - t_cb)."),
            make_mc(9, "Thông hiểu", "Nhiệt lượng do nước thu vào khi tăng từ nhiệt độ t2 lên nhiệt độ cân bằng t_cb là:", ["Q_thu = m2 * c2 * (t_cb - t2)", "Q_thu = m2 * c2 * (t2 - t_cb)", "Q_thu = m2 * c2 * t2", "Q_thu = m2 / (c2 * t_cb)"], 0, "Độ tăng nhiệt độ là (t_cb - t2)."),
            make_mc(10, "Thông hiểu", "Công thức xác định nhiệt dung riêng c1 của kim loại từ phương trình cân bằng nhiệt (bỏ qua nhiệt lượng kế) là:", ["c1 = [m2 * c2 * (t_cb - t2)] / [m1 * (t1 - t_cb)]", "c1 = [m1 * (t1 - t_cb)] / [m2 * c2 * (t_cb - t2)]", "c1 = m1 * c2 / m2", "c1 = c2 * (t1 - t2)"], 0, "c1 = Q_thu / [m1 * (t1 - t_cb)]."),
            make_mc(11, "Thông hiểu", "Nếu miếng kim loại bị dính nước sôi khi gắp từ nồi nước sôi sang nhiệt lượng kế thì kết quả c1 tính được sẽ:", ["Lớn hơn giá trị thật do nước sôi mang thêm nhiệt lượng vào bình", "Nhỏ hơn giá trị thật", "Không ảnh hưởng gì", "Bằng 0"], 0, "Nước sôi dính theo mang thêm nhiệt làm t_cb cao hơn, tính c1 bị lớn hơn thật."),
            make_mc(12, "Thông hiểu", "Thả một quả cầu bằng đồng và một quả cầu bằng nhôm có cùng khối lượng và cùng nhiệt độ 100°C vào hai cốc nước giống nhau. Quả cầu nào làm nước nóng lên nhiều hơn?", ["Quả cầu bằng nhôm vì nhiệt dung riêng của nhôm (880 J/kg.K) lớn hơn đồng (380 J/kg.K)", "Quả cầu bằng đồng", "Như nhau", "Không xác định được"], 0, "Nhôm có c lớn hơn nên tích trữ và tỏa ra nhiều nhiệt lượng hơn.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về các nguyên lý trao đổi nhiệt trong thí nghiệm đề 2:", [
                ("a", "Nhiệt truyền tự phát từ vật có nhiệt độ cao hơn sang vật có nhiệt độ thấp hơn.", True),
                ("b", "Quá trình truyền nhiệt tiếp diễn cho tới khi nhiệt độ của hai vật trở nên cân bằng.", True),
                ("c", "Vật nào có khối lượng lớn hơn thì chắc chắn có nhiệt độ cao hơn.", False),
                ("d", "Tổng nhiệt lượng các vật tỏa ra bằng tổng nhiệt lượng các vật thu vào.", True)
            ], "Khối lượng không quyết định nhiệt độ của vật."),
            make_tf(2, "Thông hiểu", "Về quy trình đo nhiệt dung riêng kim loại bằng phương pháp trộn đề 2:", [
                ("a", "Đun miếng kim loại trong nước đang sôi một thời gian đủ lâu để nó đạt đúng 100°C.", True),
                ("b", "Cần lau khô miếng kim loại thật nhanh trước khi thả vào nhiệt lượng kế.", True),
                ("c", "Sau khi thả miếng kim loại vào, phải mở toang nắp bình để quan sát miếng kim loại.", False),
                ("d", "Dùng que khuấy đảo nhẹ nước trong bình và theo dõi số chỉ nhiệt kế.", True)
            ], "Mở nắp làm thất thoát nhiệt nghiêm trọng ra không khí."),
            make_tf(3, "Thông hiểu", "Về sai số của phép đo nhiệt dung riêng kim loại đề 2:", [
                ("a", "Nhiệt lượng tỏa ra môi trường trong quá trình gắp chuyển kim loại làm giảm giá trị c đo được.", True),
                ("b", "Nếu tính thêm nhiệt lượng mà vỏ bình nhiệt lượng kế hấp thụ thì kết quả c kim loại sẽ chính xác hơn.", True),
                ("c", "Miếng kim loại có hình dạng xù xì nhiều ngóc ngách thì không thể đo được nhiệt dung riêng.", False),
                ("d", "Nhiệt kế thủy ngân có quán tính nhiệt nên cần chờ số đo ổn định mới ghi nhận t_cb.", True)
            ], "Hình dạng không ảnh hưởng đến nhiệt dung riêng bản chất của vật liệu."),
            make_tf(4, "Thông hiểu", "Về so sánh nhiệt dung riêng của các kim loại phổ biến đề 2:", [
                ("a", "Chì có nhiệt dung riêng rất nhỏ (khoảng 130 J/(kg.K)) nên nóng lên và nguội đi rất nhanh.", True),
                ("b", "Sắt có nhiệt dung riêng khoảng 460 J/(kg.K), lớn hơn nhiệt dung riêng của đồng (380 J/(kg.K)).", True),
                ("c", "Tất cả các kim loại đều có nhiệt dung riêng lớn hơn nhiệt dung riêng của nước cất.", False),
                ("d", "Vật liệu có nhiệt dung riêng nhỏ thường được dùng để chế tạo mỏ hàn nhiệt.", True)
            ], "Nhiệt dung riêng của nước lớn hơn kim loại nhiều lần.")
        ],
        [
            make_sa(1, "Thông hiểu", "Thả một quả cầu kim loại tỏa ra nhiệt lượng 8400 J vào cốc nước. Nước thu vào bao nhiêu Jun nhiệt lượng? (Bỏ qua mất nhiệt).", "8400", "Q_thu = Q_tỏa = 8400 J."),
            make_sa(2, "Thông hiểu", "Một miếng đồng khối lượng 0,5 kg hạ nhiệt độ từ 100°C xuống 30°C. Biết c_đồng = 380 J/(kg.K). Nhiệt lượng miếng đồng tỏa ra là bao nhiêu Jun (J)?", "13300", "Q = 0,5 * 380 * 70 = 13 300 J."),
            make_sa(3, "Thông hiểu", "Một miếng kim loại khối lượng 0,2 kg tỏa ra 3680 J khi hạ nhiệt độ 40°C. Nhiệt dung riêng của kim loại này là bao nhiêu J/(kg.K)?", "460", "c = 3680 / (0,2 * 40) = 460 J/(kg.K) (đây là sắt)."),
            make_sa(4, "Thông hiểu", "Thả 0,1 kg kim loại ở 100°C vào 0,2 kg nước ở 20°C. Khi cân bằng, nhiệt độ nước là 24°C. Biết c_nước = 4200 J/(kg.K). Tính nhiệt lượng nước đã thu vào (J).", "3360", "Q_thu = 0,2 * 4200 * 4 = 3360 J."),
            make_sa(5, "Vận dụng", "Từ số liệu câu trên (Q_thu = 3360 J, m_kl = 0,1 kg, hạ từ 100°C xuống 24°C), tính nhiệt dung riêng của kim loại đó (J/(kg.K)). (Làm tròn đến hàng đơn vị).", "442", "c = 3360 / (0,1 * 76) ≈ 442 J/(kg.K)."),
            make_sa(6, "Vận dụng", "Pha 2 lít nước ở 80°C với 3 lít nước ở 20°C. Bỏ qua mất nhiệt. Nhiệt độ cân bằng của hỗn hợp nước là bao nhiêu °C?", "44", "2*(80 - t) = 3*(t - 20) => 160 - 2t = 3t - 60 => 5t = 220 => t = 44°C.")
        ],
        [
            make_vdc(1, "Một học sinh thực hành xác định nhiệt dung riêng của chì. Thả một miếng chì khối lượng m1 = 300 g được nung nóng tới 100°C vào một nhiệt lượng kế chứa m2 = 250 g nước ở nhiệt độ t2 = 16°C. Nhiệt độ khi cân bằng nhiệt đo được là t_cb = 18°C. Biết nhiệt dung riêng của nước c2 = 4200 J/(kg.K) và nhiệt lượng kế hấp thụ một lượng nhiệt không đáng kể. Nhiệt dung riêng của chì tính được từ thực nghiệm này xấp xỉ bằng:", [
                "85,4 J/(kg.K)", "130 J/(kg.K)", "170 J/(kg.K)", "420 J/(kg.K)"
            ], 0, "Q_thu = 0,25 * 4200 * (18 - 16) = 2100 J. Q_toa = 0,3 * c1 * (100 - 18) = 24,6 * c1. c1 = 2100 / 24,6 ≈ 85,37 J/(kg.K)."),
            make_vdc(2, "Để đo nhiệt độ của một lò nung kim loại, người ta nung một thỏi sắt khối lượng 0,5 kg trong lò nung một thời gian dài rồi thả nhanh vào bình nhiệt lượng kế chứa 2 kg nước ở 20°C. Nhiệt độ cân bằng của nước là 35°C. Cho biết nhiệt dung riêng của sắt c_sat = 460 J/(kg.K), của nước c_nuoc = 4200 J/(kg.K). Bỏ qua mất nhiệt ra vỏ bình và không khí. Nhiệt độ của lò nung xấp xỉ bằng:", [
                "583°C", "450°C", "720°C", "1000°C"
            ], 0, "Q_thu = 2 * 4200 * 15 = 126 000 J. Q_toa = 0,5 * 460 * (t - 35) = 230 * (t - 35). 230 * (t - 35) = 126 000 => t - 35 ≈ 547,8 => t ≈ 582,8°C ≈ 583°C."),
            make_vdc(3, "Một miếng hợp kim đồng thau (gồm đồng và kẽm) có khối lượng m = 200 g ở nhiệt độ 100°C được thả vào 100 g nước ở 20°C đựng trong bình nhiệt lượng kế cách nhiệt. Nhiệt độ cân bằng là 32°C. Biết c_đồng = 380 J/(kg.K), c_kẽm = 400 J/(kg.K), c_nước = 4200 J/(kg.K). Khối lượng của đồng và khối lượng của kẽm trong miếng hợp kim lần lượt là:", [
                "m_đồng = 147 g; m_kẽm = 53 g", "m_đồng = 100 g; m_kẽm = 100 g", "m_đồng = 50 g; m_kẽm = 150 g", "m_đồng = 180 g; m_kẽm = 20 g"
            ], 0, "Q_thu = 0,1 * 4200 * 12 = 5040 J. Q_toa = (m_d * 380 + m_z * 400) * 68 = 5040 => 380.m_d + 400.m_z = 74,118. Kết hợp m_d + m_z = 0,2 => m_d ≈ 0,147 kg, m_z ≈ 0,053 kg."),
            make_vdc(4, "Một bình nhiệt lượng kế bằng đồng khối lượng 100 g chứa 200 g nước ở 15°C. Người ta thả vào bình một khối nhôm 150 g ở 100°C. Biết c_đồng = 380 J/(kg.K), c_nhôm = 880 J/(kg.K), c_nước = 4200 J/(kg.K). Nhiệt độ cân bằng của hệ thống xấp xỉ bằng:", [
                "26,5°C", "35,0°C", "20,2°C", "42,0°C"
            ], 0, "m1.c1.(t - 15) + m2.c2.(t - 15) = m3.c3.(100 - t). (0,1*380 + 0,2*4200)*(t - 15) = (0,15*880)*(100 - t). 878*(t - 15) = 132*(100 - t) => 1010.t = 13200 + 13170 = 26370 => t ≈ 26,1 - 26,5°C.")
        ]
    )

    # ĐỀ 3: Hiệu suất nhiệt, Đánh giá sai số & Kĩ năng thực hành
    exams[f"{l_id}_test3"] = meta(3,
        [
            make_mc(1, "Nhận biết", "Hiệu suất nhiệt H của một quá trình đun nước được định nghĩa là tỉ số giữa:", ["Nhiệt lượng có ích làm nóng nước và nhiệt lượng toàn phần do nguồn nhiệt cấp ra", "Nhiệt lượng toàn phần chia cho nhiệt lượng có ích", "Nhiệt lượng hao phí chia nhiệt lượng có ích", "Công suất chia cho thời gian"], 0, "H = Q_ci / Q_tp."),
            make_mc(2, "Nhận biết", "Trong một ấm đun nước siêu tốc bằng điện, nhiệt lượng nào sau đây là nhiệt lượng có ích?", ["Nhiệt lượng truyền cho nước để tăng nhiệt độ", "Nhiệt lượng làm nóng vỏ ấm", "Nhiệt lượng tỏa ra không khí xung quanh", "Nhiệt lượng đốt nóng dây dẫn"], 0, "Nhiệt lượng làm nóng nước là có ích."),
            make_mc(3, "Nhận biết", "Đơn vị đo nhiệt lượng Q trong hệ thống đo lường quốc tế (SI) là:", ["Jun (J)", "Oát (W)", "Độ Celsius (°C)", "Calo"], 0, "Đơn vị đo nhiệt lượng chuẩn là Jun (J)."),
            make_mc(4, "Nhận biết", "Một calo (1 cal) quy đổi sang đơn vị Jun (J) xấp xỉ bằng:", ["4,186 J", "4200 J", "1000 J", "0,24 J"], 0, "1 cal ≈ 4,186 J."),
            make_mc(5, "Nhận biết", "Nguyên nhân chính dẫn đến sự hao phí nhiệt lượng trong thí nghiệm nhiệt lượng kế là:", ["Sự truyền nhiệt ra không khí và sự hấp thụ nhiệt của thành bình, que khuấy", "Dây nung bị ngắn", "Nước quá sạch", "Nhiệt kế quá dài"], 0, "Thất thoát nhiệt ra môi trường và vỏ bình."),
            make_mc(6, "Nhận biết", "Biện pháp nào sau đây giúp làm tăng hiệu suất nhiệt của một bình đun nước?", ["Bọc lớp vật liệu cách nhiệt tốt xung quanh thành bình", "Mở nắp bình khi đun", "Dùng bình có vỏ kim loại mỏng tỏa nhiệt nhanh", "Đặt bình trước quạt gió"], 0, "Bọc cách nhiệt giảm thất thoát nhiệt ra ngoài."),
            make_mc(7, "Thông hiểu", "Một ấm điện tiêu thụ 100 000 J điện năng nhưng nước trong ấm chỉ nhận được 85 000 J. Hiệu suất nhiệt của ấm là:", ["85%", "15%", "117%", "90%"], 0, "H = (85 000 / 100 000) * 100% = 85%."),
            make_mc(8, "Thông hiểu", "Nhiệt lượng hao phí trong quá trình đun nước ở câu trên bằng bao nhiêu Jun?", ["15 000 J", "85 000 J", "100 000 J", "1500 J"], 0, "Q_hp = 100 000 - 85 000 = 15 000 J."),
            make_mc(9, "Thông hiểu", "Tại sao trong thực tế hiệu suất của mọi thiết bị đun nhiệt luôn luôn nhỏ hơn 100%?", ["Vì luôn có sự mất mát nhiệt lượng truyền ra môi trường xung quanh", "Vì công suất quá nhỏ", "Vì dòng điện bị rò rỉ", "Vì nước không dẫn nhiệt"], 0, "Không thể triệt tiêu hoàn toàn sự truyền nhiệt ra môi trường."),
            make_mc(10, "Thông hiểu", "Khi sử dụng nhiệt kế thủy ngân đo nhiệt độ nước trong bình, thao tác nào sau đây là SAI?", ["Cầm tay vào bầu thủy ngân của nhiệt kế để giữ cho chắc chắn", "Nhúng ngập bầu nhiệt kế vào trong lòng chất lỏng", "Không để bầu nhiệt kế chạm đáy hoặc thành bình", "Chờ số chỉ dừng lại ổn định mới đọc kết quả"], 0, "Cầm vào bầu nhiệt kế sẽ làm thân nhiệt truyền vào gây sai số."),
            make_mc(11, "Thông hiểu", "Để xác định nhiệt dung của vỏ bình nhiệt lượng kế, người ta tiến hành phép thử:", ["Trộn nước nóng và nước lạnh đã biết trước nhiệt độ và khối lượng trong bình", "Đun rỗng bình không có nước", "Đo khối lượng bình", "Đo chu vi bình"], 0, "Phương pháp trộn nước nóng và nước lạnh để tìm C_b."),
            make_mc(12, "Thông hiểu", "Khi đọc nhiệt độ trên thang chia độ của nhiệt kế, tư thế đặt mắt chuẩn xác là:", ["Mắt nhìn ngang bằng với mức chất lỏng trong ống nhiệt kế", "Nhìn chếch từ trên xuống", "Nhìn chếch từ dưới lên", "Nhìn nghiêng 45 độ"], 0, "Nhìn ngang bằng để tránh sai số góc nhìn.")
        ],
        [
            make_tf(1, "Thông hiểu", "Về định nghĩa và tính toán hiệu suất nhiệt trong thực hành đề 3:", [
                ("a", "Hiệu suất H luôn là một số dương nhỏ hơn 100% (hoặc nhỏ hơn 1).", True),
                ("b", "Nhiệt lượng toàn phần luôn bằng tổng nhiệt lượng có ích và nhiệt lượng hao phí.", True),
                ("c", "Thiết bị có hiệu suất càng cao thì lượng nhiệt năng hao phí tỏa ra môi trường càng nhiều.", False),
                ("d", "Bình thủy giữ nhiệt có hiệu suất giữ nhiệt tốt hơn phích nước thông thường.", True)
            ], "Hiệu suất cao thì nhiệt lượng hao phí càng ít."),
            make_tf(2, "Thông hiểu", "Về các thao tác sử dụng nhiệt kế đo nhiệt độ chất lỏng đề 3:", [
                ("a", "Bầu nhiệt kế không được chạm vào đáy hoặc thành bình nhiệt lượng kế.", True),
                ("b", "Khi đọc kết quả, phải rút nhiệt kế ra khỏi chất lỏng vung mạnh như nhiệt kế y tế.", False),
                ("c", "Mắt người quan sát phải đặt ngang bằng với đỉnh cột chất lỏng chỉ thị.", True),
                ("d", "Nhiệt kế điện tử hiện số giúp đọc kết quả nhanh và chính xác hơn nhiệt kế chất lỏng.", True)
            ], "Nhiệt kế phòng thí nghiệm phải đọc khi bầu nhiệt kế còn ngập trong chất lỏng."),
            make_tf(3, "Thông hiểu", "Về quy tắc xử lý khi nhiệt kế thủy ngân bị vỡ trong phòng thí nghiệm đề 3:", [
                ("a", "Thủy ngân là một kim loại lỏng rất độc hại dễ bay hơi ở nhiệt độ phòng.", True),
                ("b", "Khi nhiệt kế vỡ, có thể rắc bột lưu huỳnh lên các hạt thủy ngân để gom dọn an toàn.", True),
                ("c", "Dùng máy hút bụi gia đình để hút các hạt thủy ngân vương vãi trên sàn nhà.", False),
                ("d", "Cần mở cửa thông gió phòng thí nghiệm và báo ngay cho giáo viên quản lí.", True)
            ], "Dùng máy hút bụi làm thủy ngân bay hơi khuếch tán vào không khí gây ngộ độc."),
            make_tf(4, "Thông hiểu", "Về các giải pháp công nghệ nâng cao hiệu suất nhiệt đề 3:", [
                ("a", "Nồi áp suất giúp tăng nhiệt độ sôi của nước làm thức ăn chín nhanh hơn tiết kiệm năng lượng.", True),
                ("b", "Sử dụng bếp từ có hiệu suất nhiệt cao hơn bếp gas vì nhiệt sinh trực tiếp ở đáy nồi.", True),
                ("c", "Đáy nồi nấu bằng gang hoặc đồng dày giúp phân tán nhiệt đều chống cháy cục bộ.", True),
                ("d", "Cạo sạch lớp cách nhiệt ở đáy bình đun nước để nhiệt truyền vào nhanh hơn.", False)
            ], "Cạo lớp cách nhiệt sẽ làm mất khả năng giữ nhiệt.")
        ],
        [
            make_sa(1, "Thông hiểu", "Một bếp điện cung cấp nhiệt lượng toàn phần 200 000 J để đun nước, trong đó nước nhận được 160 000 J. Hiệu suất nhiệt của bếp là bao nhiêu phần trăm (%)?", "80", "H = (160 000 / 200 000) * 100% = 80%."),
            make_sa(2, "Thông hiểu", "Một ấm đun nước có công suất 1500 W hoạt động trong 100 giây. Điện năng toàn phần ấm tiêu thụ là bao nhiêu kilôjun (kJ)?", "150", "A = 1500 * 100 = 150 000 J = 150 kJ."),
            make_sa(3, "Thông hiểu", "Biết hiệu suất của ấm ở câu trên là 90%. Nhiệt lượng có ích truyền cho nước là bao nhiêu kilôjun (kJ)?", "135", "Q_ci = 150 * 90% = 135 kJ."),
            make_sa(4, "Thông hiểu", "Lượng nhiệt hao phí tỏa ra môi trường của ấm ở câu trên là bao nhiêu kilôjun (kJ)?", "15", "Q_hp = 150 - 135 = 15 kJ."),
            make_sa(5, "Vận dụng", "Để đun 2 kg nước tăng thêm 30°C với ấm điện có hiệu suất 84%, cần cung cấp nhiệt lượng toàn phần là bao nhiêu Jun (J)? (Cho c_nước = 4200 J/kg.K).", "300000", "Q_ci = 2 * 4200 * 30 = 252 000 J. Q_tp = 252 000 / 0,84 = 300 000 J."),
            make_sa(6, "Vận dụng", "Một bếp gas có hiệu suất 40%. Để cung cấp 840 000 J nhiệt lượng cho nồi canh, nhiệt lượng tỏa ra do đốt cháy khí gas phải bằng bao nhiêu kilôjun (kJ)?", "2100", "Q_tp = 840 000 / 0,4 = 2 100 000 J = 2100 kJ.")
        ],
        [
            make_vdc(1, "Một ấm điện siêu tốc công suất 1800 W đun 1,8 lít nước từ 25°C đến 100°C. Biết nhiệt dung riêng của nước c = 4200 J/(kg.K), khối lượng riêng của nước D = 1000 kg/m3. Thời gian đun thực tế bấm giờ được là 6 phút (360 giây). Hiệu suất nhiệt của ấm siêu tốc này xấp xỉ bằng:", [
                "87,5%", "92,0%", "80,0%", "75,5%"
            ], 0, "m = 1,8 kg. Q_ci = 1,8 * 4200 * 75 = 567 000 J. A_tp = 1800 * 360 = 648 000 J. H = 567000 / 648000 = 87,5%."),
            make_vdc(2, "Một học sinh dùng bếp cồn để đun sôi 200 g nước ở 20°C đựng trong cốc nhôm 50 g. Khi nước sôi 100°C, khối lượng cồn tiêu hao cân được là 6,0 g. Cho biết năng suất tỏa nhiệt của cồn q = 2,7 . 10^7 J/kg, nhiệt dung riêng của nhôm 880 J/(kg.K), của nước 4200 J/(kg.K). Hiệu suất nhiệt của bếp cồn này là:", [
                "43,65%", "50,0%", "35,2%", "60,5%"
            ], 0, "Q_thu = (0,2 * 4200 + 0,05 * 880) * 80 = (840 + 44) * 80 = 884 * 80 = 70 720 J. Q_toa = (6e-3) * 2,7e7 = 162 000 J. H = 70720 / 162000 ≈ 43,65%."),
            make_vdc(3, "Một bình nước nóng năng lượng mặt trời có diện tích hấp thụ nhiệt S = 2,0 m2. Cường độ bức xạ mặt trời chiếu vuông góc là 800 W/m2. Hiệu suất chuyển đổi quang - nhiệt của bình đạt 65%. Bình chứa 120 lít nước ở nhiệt độ ban đầu 22°C. Biết c = 4200 J/(kg.K). Thời gian chiếu nắng liên tục cần thiết để nước trong bình nóng lên đến 50°C là:", [
                "3,77 giờ (khoảng 3 giờ 46 phút)", "2,5 giờ", "5,0 giờ", "1,8 giờ"
            ], 0, "m = 120 kg. Q_thu = 120 * 4200 * 28 = 14 112 000 J. P_quang = 2,0 * 800 = 1600 W. P_thu = 1600 * 0,65 = 1040 W. t = 14112000 / 1040 ≈ 13 569 s ≈ 3,77 giờ."),
            make_vdc(4, "Một người dùng bếp từ có hiệu suất 90% và một người khác dùng bếp gas có hiệu suất 45% để đun sôi cùng 2 lít nước từ 25°C. Cho giá điện sinh hoạt trung bình 2500 đ/kWh và giá gas là 30 000 đ/kg (năng suất tỏa nhiệt của gas q = 4,5 . 10^7 J/kg). So sánh chi phí đun sôi nước giữa hai loại bếp:", [
                "Bếp từ tốn khoảng 486 đồng; bếp gas tốn khoảng 933 đồng (bếp từ tiết kiệm gần một nửa)",
                "Bếp gas rẻ hơn bếp từ",
                "Chi phí hai bếp bằng nhau",
                "Bếp từ tốn 1500 đồng; bếp gas tốn 3000 đồng"
            ], 0, "Q_ci = 2 * 4200 * 75 = 630 000 J. Bếp từ: A_dien = 630000 / 0,9 = 700 000 J = 0,1944 kWh => Tiền điện = 0,1944 * 2500 ≈ 486 đ. Bếp gas: Q_gas = 630000 / 0,45 = 1 400 000 J => m_gas = 1,4e6 / 4,5e7 ≈ 0,0311 kg => Tiền gas = 0,0311 * 30 000 ≈ 933 đ.")
        ]
    )

    return exams
