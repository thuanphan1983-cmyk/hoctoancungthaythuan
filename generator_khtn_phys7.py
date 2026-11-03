# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - VẬT LÝ 7 (KNTT)
Gồm 17 bài/chương ôn tập => 59 đề thi độc lập 100%
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

def build_phys7_exams():
    exams = {}

    # Danh sách bài học Vật lý 7
    lessons_list = [
        # CHƯƠNG III: TỐC ĐỘ
        ("phys7_c3", "Chương III: Tốc độ", "phys7_c3_b8", "Bài 8: Tốc độ chuyển động", 3),
        ("phys7_c3", "Chương III: Tốc độ", "phys7_c3_b9", "Bài 9: Đo tốc độ", 3),
        ("phys7_c3", "Chương III: Tốc độ", "phys7_c3_b10", "Bài 10: Đồ thị quãng đường - thời gian", 3),
        ("phys7_c3", "Chương III: Tốc độ", "phys7_c3_b11", "Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông", 3),
        ("phys7_c3", "Chương III: Tốc độ", "phys7_c3_rev", "[Đề tổng hợp] Ôn tập cuối Chương III", 5),

        # CHƯƠNG IV: ÂM THANH
        ("phys7_c4", "Chương IV: Âm thanh", "phys7_c4_b12", "Bài 12: Sóng âm", 3),
        ("phys7_c4", "Chương IV: Âm thanh", "phys7_c4_b13", "Bài 13: Độ to và độ cao của âm", 3),
        ("phys7_c4", "Chương IV: Âm thanh", "phys7_c4_b14", "Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn", 3),
        ("phys7_c4", "Chương IV: Âm thanh", "phys7_c4_rev", "[Đề tổng hợp] Ôn tập cuối Chương IV", 5),

        # CHƯƠNG V: ÁNH SÁNG
        ("phys7_c5", "Chương V: Ánh sáng", "phys7_c5_b15", "Bài 15: Ánh sáng, tia sáng", 3),
        ("phys7_c5", "Chương V: Ánh sáng", "phys7_c5_b16", "Bài 16: Sự phản xạ ánh sáng", 3),
        ("phys7_c5", "Chương V: Ánh sáng", "phys7_c5_b17", "Bài 17: Ảnh của một vật tạo bởi gương phẳng", 3),
        ("phys7_c5", "Chương V: Ánh sáng", "phys7_c5_rev", "[Đề tổng hợp] Ôn tập cuối Chương V", 5),

        # CHƯƠNG VI: TỪ
        ("phys7_c6", "Chương VI: Từ", "phys7_c6_b18", "Bài 18: Nam châm", 3),
        ("phys7_c6", "Chương VI: Từ", "phys7_c6_b19", "Bài 19: Từ trường", 3),
        ("phys7_c6", "Chương VI: Từ", "phys7_c6_b20", "Bài 20: Chế tạo nam châm điện đơn giản", 3),
        ("phys7_c6", "Chương VI: Từ", "phys7_c6_rev", "[Đề tổng hợp] Ôn tập cuối Chương VI", 5)
    ]

    for ch_id, ch_title, l_id, l_name, n_tests in lessons_list:
        for t in range(1, n_tests + 1):
            k = f"{l_id}_test{t}"
            p1 = []
            p2 = []
            p3 = []
            p4 = []

            # ======================== CHƯƠNG III: TỐC ĐỘ ========================
            if "c3" in ch_id:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Tốc độ chuyển động cho biết:", ["Mức độ nhanh hay chậm của chuyển động", "Quãng đường dài hay ngắn", "Thời gian chuyển động", "Hướng chuyển động"], 0, "Tốc độ cho biết mức độ nhanh hay chậm."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Công thức tính tốc độ v khi đi quãng đường s trong thời gian t là:", ["v = s / t", "v = s × t", "v = t / s", "v = s + t"], 0, "v = s / t."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Đơn vị đo tốc độ thường dùng trong hệ SI là:", ["m/s và km/h", "m/min", "km/s", "cm/s"], 0, "m/s (mét trên giây) và km/h (kilômét trên giờ)."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Thiết bị đo thời gian chính xác trong phòng thí nghiệm là:", ["Cổng quang điện và đồng hồ đo thời gian hiện số", "Đồng hồ cát", "Thước cuộn", "Nhiệt kế"], 0, "Cổng quang điện kết nối đồng hồ hiện số."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Đồ thị quãng đường - thời gian của một vật đứng yên là:", ["Đường thẳng song song với trục thời gian Ot", "Đường thẳng dốc lên", "Đường cong parabol", "Đường thẳng dốc xuống"], 0, "Đứng yên thì quãng đường s không đổi, đồ thị song song trục thời gian."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Biển báo giới hạn tốc độ tối đa cho phép hình tròn viền đỏ nền trắng bên trong có số 50 biểu thị:", ["Tốc độ tối đa không được vượt quá 50 km/h", "Tốc độ tối thiểu phải đạt 50 km/h", "Khoảng cách cách xe 50 m", "Trọng tải 50 tấn"], 0, "Biển hạn chế tốc độ tối đa."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Đổi 36 km/h sang đơn vị m/s ta được kết quả là:", ["10 m/s", "36 m/s", "100 m/s", "3,6 m/s"], 0, "36 / 3,6 = 10 m/s."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Một người đi xe đạp đi quãng đường 12 km hết 30 phút. Tốc độ của người đó là:", ["24 km/h", "12 km/h", "6 km/h", "30 km/h"], 0, "t = 0,5 h => v = 12 / 0,5 = 24 km/h."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Tốc độ của ánh sáng trong chân không là:", ["300.000 km/s (hay 3 × 10^8 m/s)", "340 m/s", "1000 km/h", "1500 m/s"], 0, "c ≈ 300.000 km/s."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Trên đoạn đường cao tốc, quy tắc an toàn 'Khoảng cách 3 giây' giúp tài xế:", ["Đủ thời gian phản ứng và phanh dừng xe an toàn khi xe phía trước phanh gấp", "Tiết kiệm xăng", "Chạy nhanh hơn", "Vượt xe khác"], 0, "Khoảng cách an toàn tương ứng thời gian phản ứng và hãm phanh."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Bắn tốc độ tự động trên đường giao thông dùng thiết bị nào?", ["Camera bắn tốc độ (máy radar hoặc laser kết hợp camera chụp ảnh)", "Cân điện tử", "Kính thiên văn", "Thước dây"], 0, "Súng bắn tốc độ phát sóng radar hoặc laser đo thời gian."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Một ô tô đang chạy với tốc độ 72 km/h. Trong 10 giây, ô tô đi được quãng đường là:", ["200 m", "720 m", "100 m", "500 m"], 0, "v = 72 km/h = 20 m/s. s = 20 × 10 = 200 m.")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về tốc độ và chuyển động:", [
                        ("a", "Tốc độ trung bình bằng tổng quãng đường chia cho tổng thời gian đi hết quãng đường đó.", True),
                        ("b", "1 m/s bằng 3,6 km/h.", True),
                        ("c", "Tốc kế trên xe máy, ô tô đo tốc độ tức thời tại thời điểm đang chạy.", True),
                        ("d", "Chuyển động có đồ thị s-t càng dốc thì tốc độ chuyển động càng nhỏ.", False)
                    ], "Độ dốc càng lớn biểu thị tốc độ càng nhanh."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Khi tham gia giao thông trên đường bộ:", [
                        ("a", "Chạy xe quá tốc độ quy định là nguyên nhân hàng đầu gây tai nạn giao thông nghiêm trọng.", True),
                        ("b", "Trời mưa đường trơn trượt làm giảm độ bám của lốp xe, tăng quãng đường phanh dừng.", True),
                        ("c", "Khoảng cách an toàn giữa hai xe phải tăng lên khi tốc độ lưu thông tăng.", True),
                        ("d", "Khoảng cách an toàn tối thiểu không phụ thuộc vào điều kiện thời tiết.", False)
                    ], "Trời mưa hoặc sương mù phải tăng khoảng cách an toàn."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Một xe tải đi từ A đến B dài 60 km trong 1 giờ 30 phút, sau đó dừng lại nghỉ 30 phút rồi đi tiếp 40 km trong 1 giờ:", [
                        ("a", "Thời gian chuyển động thực tế là 2,5 giờ.", True),
                        ("b", "Tổng thời gian kể cả thời gian nghỉ là 3,0 giờ.", True),
                        ("c", "Tốc độ trung bình trên toàn bộ hành trình tính cả thời gian nghỉ là 33,33 km/h.", True),
                        ("d", "Tốc độ ở chặng thứ hai lớn hơn chặng thứ nhất.", False)
                    ], "v1 = 60 / 1,5 = 40 km/h; v2 = 40 / 1 = 40 km/h (bằng nhau). v_tb = 100 / 3 = 33,33 km/h."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Hai xe ô tô xuất phát cùng lúc từ A và B cách nhau 100 km, chuyển động ngược chiều gặp nhau. Xe A chạy 60 km/h, xe B chạy 40 km/h:", [
                        ("a", "Sau 1 giờ hai xe gặp nhau.", True),
                        ("b", "Vị trí gặp nhau cách A một đoạn 60 km.", True),
                        ("c", "Vị trí gặp nhau cách B một đoạn 40 km.", True),
                        ("d", "Nếu hai xe chạy cùng chiều thì sau 2 giờ xe A đuổi kịp xe B.", False)
                    ], "Ngược chiều: t = 100 / (60+40) = 1h. Cùng chiều: t = 100 / (60-40) = 5h.")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Đổi 15 m/s sang km/h ta được bao nhiêu km/h?", "54", "15 × 3,6 = 54 km/h."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - Một người đi bộ 3 km trong 0,5 giờ. Tốc độ của người đó là bao nhiêu km/h?", "6", "3 / 0,5 = 6 km/h."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Một xe buýt đi quãng đường 45 km với tốc độ 30 km/h. Thời gian đi hết là bao nhiêu giờ? (Làm tròn 1 chữ số)", "1.5", "45 / 30 = 1,5 giờ."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Đồ thị s - t biểu diễn một người đi xe đạp đi được 200 m trong 20 s. Tốc độ của người đó là bao nhiêu m/s?", "10", "200 / 20 = 10 m/s."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Một đoàn tàu dài 200 m chạy qua một cây cầu dài 800 m với tốc độ 36 km/h (10 m/s). Thời gian từ lúc đầu tàu vào cầu đến lúc toa cuối cùng ra khỏi cầu là bao nhiêu giây?", "100", "s = 800 + 200 = 1000 m. t = 1000 / 10 = 100 s."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Một ô tô đi nửa quãng đường đầu với tốc độ 40 km/h và nửa quãng đường sau với tốc độ 60 km/h. Tốc độ trung bình trên cả quãng đường là bao nhiêu km/h?", "48", "v_tb = 2v1v2 / (v1 + v2) = 2×40×60 / 100 = 48 km/h.")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Thiết bị 'bắn tốc độ' ghi nhận một xe máy chạy qua hai vạch mốc cách nhau 10 m mất khoảng thời gian 0,6 giây. Đoạn đường có biển báo giới hạn tốc độ tối đa là 50 km/h. Tài xế xe máy có bị vi phạm quá tốc độ không?", ["Có vi phạm vì tốc độ thực tế xấp xỉ 60 km/h vượt quá giới hạn 50 km/h", "Không vi phạm vì tốc độ chỉ đạt 45 km/h", "Không vi phạm vì tốc độ đạt đúng 50 km/h", "Không thể xác định được"], 0, "v = 10 / 0,6 ≈ 16,67 m/s = 60 km/h > 50 km/h => Vi phạm quá tốc độ 10 km/h."),
                    make_vdc(2, f"Đề {t} - Một người nhìn thấy tia sét lóe lên rồi sau 3 giây mới nghe thấy tiếng sấm rền. Biết tốc độ ánh sáng truyền gần như tức thời, tốc độ âm thanh trong không khí là 340 m/s. Nơi xảy ra sét đánh cách người đó khoảng bao nhiêu mét?", ["1020 m", "340 m", "680 m", "1500 m"], 0, "s = v × t = 340 × 3 = 1020 m."),
                    make_vdc(3, f"Đề {t} - Túi khí (Airbag) và dây an toàn trên xe ô tô được kích hoạt khi va chạm nhằm mục đích:", ["Kéo dài thời gian va chạm làm giảm lực tác dụng lên hành khách và ngăn hành khách văng ra ngoài theo quán tính", "Làm xe dừng lại ngay lập tức", "Làm tắt động cơ xe", "Báo động cho xe cứu thương"], 0, "Giảm quán tính và chấn thương."),
                    make_vdc(4, f"Đề {t} - Một người chèo thuyền trên sông xuôi dòng từ A đến B mất 2 giờ và ngược dòng từ B về A mất 3 giờ. Biết khúc sông dài 30 km. Tốc độ của dòng nước là:", ["2,5 km/h", "5,0 km/h", "1,5 km/h", "12,5 km/h"], 0, "v_xuôi = 15 km/h, v_ngược = 10 km/h => v_nước = (15 - 10)/2 = 2,5 km/h.")
                ]

            # ======================== CHƯƠNG IV: ÂM THANH ========================
            elif "c4" in ch_id:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Âm thanh được tạo ra từ:", ["Các vật dao động", "Các vật đứng yên", "Ánh sáng chiếu vào", "Điện trường"], 0, "Mọi nguồn âm khi phát ra âm đều dao động."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Sóng âm KHÔNG truyền được trong môi trường nào?", ["Chân không", "Không khí", "Nước", "Chất rắn"], 0, "Chân không không có các phần tử vật chất để truyền dao động âm."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Tốc độ truyền âm giảm dần theo thứ tự các môi trường là:", ["Chất rắn > Chất lỏng > Chất khí", "Chất khí > Chất lỏng > Chất rắn", "Chất lỏng > Chất khí > Chất rắn", "Chất chân không > Chất khí"], 0, "vrắn > vlỏng > vkhí."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Tần số dao động là số dao động thực hiện được trong thời gian:", ["1 giây", "1 phút", "1 giờ", "1 ngày"], 0, "Tần số là số dao động trong 1 giây, đơn vị là Hertz (Hz)."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Độ cao của âm phụ thuộc vào đại lượng nào?", ["Tần số dao động", "Biên độ dao động", "Khoảng cách", "Vận tốc âm"], 0, "Tần số càng lớn âm phát ra càng cao (bổng)."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Độ to của âm phụ thuộc vào đại lượng nào?", ["Biên độ dao động", "Tần số dao động", "Tốc độ âm", "Hình dạng nguồn âm"], 0, "Biên độ dao động càng lớn âm nghe càng to."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Tai người bình thường có thể nghe được âm thanh có dải tần số từ:", ["16 Hz đến 20.000 Hz", "Dưới 16 Hz", "Trên 20.000 Hz", "0 đến 100 Hz"], 0, "Âm nghe được: 16 Hz - 20000 Hz. Dưới 16 Hz là hạ âm, trên 20000 Hz là siêu âm."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Âm phản xạ nghe được cách âm trực tiếp ít nhất 1/15 giây gọi là:", ["Tiếng vang", "Hạ âm", "Siêu âm", "Tạp âm"], 0, "Tiếng vang là âm phản xạ nghe tách rời âm trực tiếp."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Vật liệu nào sau đây phản xạ âm kém (hấp thụ âm tốt) dùng để cách âm?", ["Mút xốp, rèm nhung, dạ, bông khoáng", "Tường bê tông nhẵn", "Mặt gương kính", "Tấm kim loại phẳng"], 0, "Vật mềm xốp, bề mặt gồ ghề hấp thụ âm tốt."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Để chống ô nhiễm tiếng ồn cho khu dân cư gần đường cao tốc, biện pháp hữu hiệu là:", ["Trồng dải cây xanh và xây dựng tường cách âm", "Yêu cầu xe cộ tắt máy", "Xây nhà bằng kính trong suốt", "Sơn tường màu đỏ"], 0, "Trồng cây xanh tán rộng và dựng tường cách âm hấp thụ tán xạ tiếng ồn."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Khi gảy một dây đàn guitar thật mạnh, âm phát ra sẽ:", ["To hơn vì biên độ dao động lớn hơn", "Bổng hơn", "Trầm hơn", "Không đổi"], 0, "Gảy mạnh làm biên độ dao động lớn -> âm to hơn."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Cá heo và dơi sử dụng sóng âm nào để định vị và săn mồi?", ["Sóng siêu âm", "Sóng hạ âm", "Sóng ánh sáng", "Sóng vô tuyến"], 0, "Dơi và cá heo phát sóng siêu âm định vị bằng tiếng vang.")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về bản chất của sóng âm:", [
                        ("a", "Sóng âm là sự lan truyền các dao động trong môi trường vật chất.", True),
                        ("b", "Trong không khí, âm thanh truyền đi với tốc độ khoảng 340 m/s ở 20 °C.", True),
                        ("c", "Tốc độ truyền âm trong thép lớn hơn nhiều so với trong nước.", True),
                        ("d", "Các phi hành gia trên Mặt Trăng có thể nói chuyện trực tiếp qua không khí mà không cần bộ đàm.", False)
                    ], "Mặt Trăng là môi trường chân không, không có không khí nên không truyền được âm trực tiếp."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Về đặc trưng sinh lí của âm thanh:", [
                        ("a", "Độ cao của âm gắn liền với tần số dao động.", True),
                        ("b", "Độ to của âm gắn liền với biên độ dao động.", True),
                        ("c", "Âm có tần số 10.000 Hz nghe trầm hơn âm có tần số 200 Hz.", False),
                        ("d", "Tiếng ồn kéo dài trên 85 dB gây hại cho thính lực con người.", True)
                    ], "Tần số càng lớn âm càng bổng (cao), 10.000 Hz bổng hơn nhiều so với 200 Hz."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Một người đứng trước một vách đá cao hét to. Sau 0,6 giây người đó nghe thấy tiếng vang dội lại:", [
                        ("a", "Biết tốc độ âm trong không khí là 340 m/s.", True),
                        ("b", "Quãng đường âm đi và về là 204 m.", True),
                        ("c", "Khoảng cách từ người đó đến vách đá là 102 m.", True),
                        ("d", "Người đó không thể nghe được tiếng vang nếu đứng cách vách đá 50 m.", False)
                    ], "s = v × t / 2 = 340 × 0,6 / 2 = 102 m. Để nghe tiếng vang cần s ≥ 340 × (1/15) / 2 ≈ 11,3 m. 50 m vẫn nghe được."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Một lá thép trong 5 giây thực hiện được 250 dao động:", [
                        ("a", "Tần số dao động của lá thép là 50 Hz.", True),
                        ("b", "Tai người hoàn toàn có thể nghe được âm thanh do lá thép phát ra.", True),
                        ("c", "Âm do lá thép phát ra thuộc vùng hạ âm.", False),
                        ("d", "Nếu giảm số dao động trong 1 giây xuống thì âm phát ra sẽ trầm hơn.", True)
                    ], "f = 250 / 5 = 50 Hz (thuộc dải nghe được 16 - 20000 Hz, không phải hạ âm).")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Tốc độ truyền âm trong không khí ở 20 °C xấp xỉ bằng bao nhiêu m/s?", "340", "340 m/s."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - Một vật thực hiện được 100 dao động trong 2 giây. Tần số dao động là bao nhiêu Hz?", "50", "100 / 2 = 50 Hz."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Sóng siêu âm có tần số lớn hơn bao nhiêu Hz?", "20000", "20.000 Hz."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Tàu đánh cá phát sóng siêu âm xuống đáy biển và thu được tín hiệu phản xạ sau 1,2 giây. Biết tốc độ âm trong nước biển là 1500 m/s. Độ sâu của biển là bao nhiêu mét?", "900", "d = v × t / 2 = 1500 × 1,2 / 2 = 900 m."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Để nghe được tiếng vang trong không khí (v = 340 m/s), khoảng cách tối thiểu từ người đến bức tường phản xạ âm phải bằng bao nhiêu mét? (Làm tròn 1 chữ số thập phân)", "11.3", "d_min = 340 × (1/15) / 2 ≈ 11,33 m ≈ 11,3 m."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Một người gõ búa vào một đầu ống kim loại dài 340 m. Người ở đầu kia áp tai vào ống nghe thấy hai tiếng gõ cách nhau 0,93 giây. Biết tốc độ âm trong không khí là 340 m/s. Tốc độ truyền âm trong kim loại đó là bao nhiêu m/s?", "5000", "t_khí = 340 / 340 = 1s => t_kimloai = 1 - 0,93 = 0,07s => v = 340 / 0,07 ≈ 4857... (nếu 5000 m/s thì t = 0,068s). Trả lời xấp xỉ 5000.")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Trong phòng hòa nhạc và rạp chiếu phim hiện đại, các bức tường và trần nhà thường được thiết kế uốn lượn gồ ghề và ốp các tấm thạch cao đục lỗ hoặc bọc vải nỉ nhung dày. Mục đích chính của thiết kế này là:", ["Tán xạ và hấp thụ âm thanh phản xạ, triệt tiêu hiện tượng tiếng vang khó chịu giúp âm thanh trung thực và êm ái", "Để làm đẹp mỹ thuật", "Để làm ấm phòng chiếu phim", "Để tường không bị nứt"], 0, "Chống phản xạ âm và triệt tiêu tiếng vang."),
                    make_vdc(2, f"Đề {t} - Người xưa thường áp tai xuống mặt đất để nghe tiếng vó ngựa của quân địch từ rất xa trước khi nhìn thấy hoặc nghe thấy qua không khí. Cơ sở khoa học của hành động này là:", ["Mặt đất (chất rắn) truyền âm thanh với tốc độ nhanh hơn và ít bị suy giảm năng lượng hơn so với không khí", "Mặt đất hút âm thanh tốt hơn", "Âm thanh trong không khí bị gió thổi ngược", "Dưới đất có nhiều sinh vật phát ra âm"], 0, "Chất rắn truyền âm nhanh và xa hơn chất khí."),
                    make_vdc(3, f"Đề {t} - Máy bay siêu thanh khi bay vượt qua tốc độ âm thanh trong không khí (trên 340 m/s hay Mach 1) sẽ tạo ra hiện tượng gì làm rung chuyển mặt đất như tiếng bom nổ?", ["Sóng xung kích âm thanh (tiếng nổ siêu thanh - Sonic boom)", "Cháy động cơ máy bay", "Va chạm với mây", "Sét đánh"], 0, "Sonic boom sinh ra khi vượt bức tường âm thanh."),
                    make_vdc(4, f"Đề {t} - Máy siêu âm trong y khoa chẩn đoán hình ảnh (như siêu âm thai nhi, ổ bụng, tim) sử dụng sóng âm có đặc điểm:", ["Sóng siêu âm có tần số rất cao, không gây hại cho mô sống và thu lại tín hiệu phản xạ tái tạo hình ảnh nội tạng", "Sóng hạ âm làm rung nội tạng", "Tia X quang liều cao", "Sóng điện từ công suất lớn"], 0, "Sóng siêu âm an toàn và phản xạ rõ nét ranh giới các mô mềm.")
                ]

            # ======================== CHƯƠNG V: ÁNH SÁNG ========================
            elif "c5" in ch_id:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Ta nhìn thấy một vật khi:", ["Có ánh sáng từ vật đó truyền vào mắt ta", "Mắt ta phát ra ánh sáng đến vật", "Vật đó phát ra ánh sáng", "Môi trường hoàn toàn tối đen"], 0, "Ánh sáng từ vật truyền tới mắt."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Nguồn sáng là vật:", ["Tự nó phát ra ánh sáng", "Hắt lại ánh sáng chiếu vào nó", "Có màu sắc rực rỡ", "Trong suốt"], 0, "Nguồn sáng tự phát ra ánh sáng (như Mặt Trời, ngọn nến đang cháy, bóng đèn sáng)."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Vật nào sau đây là nguồn sáng?", ["Mặt Trời", "Mặt Trăng", "Tấm gương soi", "Mặt bàn gỗ"], 0, "Mặt Trời tự phát sáng; Mặt Trăng hắt lại ánh sáng Mặt Trời."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường nào?", ["Đường thẳng", "Đường cong", "Đường gấp khúc", "Đường tròn"], 0, "Định luật truyền thẳng ánh sáng."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Đường truyền của ánh sáng được biểu diễn bằng một đường thẳng có mũi tên chỉ hướng gọi là:", ["Tia sáng", "Chùm sáng", "Đường pháp tuyến", "Tia phản xạ"], 0, "Tia sáng."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Theo định luật phản xạ ánh sáng, góc phản xạ (r) và góc tới (i) có mối quan hệ:", ["r = i", "r > i", "r < i", "r + i = 90 độ"], 0, "Góc phản xạ luôn bằng góc tới: r = i."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Chiếu một tia sáng tới mặt gương phẳng với góc tới i = 30 độ. Góc phản xạ r có giá trị là:", ["30 độ", "60 độ", "90 độ", "0 độ"], 0, "r = i = 30 độ."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Nếu tia sáng tới vuông góc với mặt gương phẳng (i = 0 độ) thì góc phản xạ bằng:", ["0 độ (tia phản xạ bật ngược trở lại)", "90 độ", "45 độ", "180 độ"], 0, "Góc tới bằng 0 độ thì góc phản xạ bằng 0 độ."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Ảnh của một vật tạo bởi gương phẳng có tính chất nào sau đây?", ["Là ảnh ảo, cùng chiều, lớn bằng vật và cách gương một khoảng bằng khoảng cách từ vật đến gương", "Là ảnh thật hứng được trên màn", "Là ảnh ảo lớn hơn vật", "Là ảnh ảo nhỏ hơn vật"], 0, "Ảnh ảo qua gương phẳng đối xứng với vật qua mặt gương."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Hiện tượng Nhật thực xảy ra khi:", ["Mặt Trăng nằm giữa Mặt Trời và Trái Đất", "Trái Đất nằm giữa Mặt Trời và Mặt Trăng", "Mặt Trời nằm giữa Trái Đất và Mặt Trăng", "Trời nhiều mây"], 0, "Mặt Trăng che khuất Mặt Trời chiếu đến Trái Đất."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Khi một người tiến lại gần gương phẳng 1 m thì khoảng cách giữa người đó và ảnh của mình trong gương sẽ:", ["Giảm đi 2 m", "Giảm đi 1 m", "Không đổi", "Tăng lên 2 m"], 0, "Người lại gần gương 1m, ảnh cũng lại gần gương 1m => khoảng cách giảm 2m."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Chiếu tia tới hợp với mặt gương một góc 40 độ. Góc tới i của tia sáng là:", ["50 độ", "40 độ", "90 độ", "80 độ"], 0, "Góc tới = 90° - 40° = 50°.")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về định luật phản xạ ánh sáng:", [
                        ("a", "Tia phản xạ nằm trong mặt phẳng tới chứa tia tới và đường pháp tuyến của gương tại điểm tới.", True),
                        ("b", "Góc phản xạ luôn luôn bằng góc tới.", True),
                        ("c", "Nếu tăng góc tới thì góc phản xạ cũng tăng theo.", True),
                        ("d", "Hiện tượng phản xạ khuếch tán cho ta nhìn thấy ảnh rõ nét của vật như trong gương.", False)
                    ], "Phản xạ khuếch tán trên bề mặt gồ ghề làm ánh sáng tán xạ nhiều hướng, không tạo ảnh rõ nét."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Về ảnh tạo bởi gương phẳng:", [
                        ("a", "Ảnh tạo bởi gương phẳng là ảnh ảo, không hứng được trên màn chắn.", True),
                        ("b", "Độ lớn của ảnh luôn bằng độ lớn của vật.", True),
                        ("c", "Khoảng cách từ ảnh đến gương bằng khoảng cách từ vật đến gương.", True),
                        ("d", "Nếu đứng càng xa gương phẳng thì kích thước thật của ảnh trong gương càng nhỏ đi.", False)
                    ], "Kích thước ảnh luôn bằng vật, nhìn thấy nhỏ đi là do góc trông mắt."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Một tia sáng SI chiếu tới gương phẳng nằm ngang hợp với mặt gương góc 30 độ:", [
                        ("a", "Pháp tuyến IN vuông góc với mặt gương.", True),
                        ("b", "Góc tới i bằng 60 độ.", True),
                        ("c", "Góc phản xạ r bằng 60 độ.", True),
                        ("d", "Góc tạo bởi tia tới SI và tia phản xạ IR bằng 90 độ.", False)
                    ], "Góc hợp bởi tia tới và tia phản xạ = i + r = 60° + 60° = 120°."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Hiện tượng bóng tối và bóng nửa tối:", [
                        ("a", "Vùng bóng tối là vùng phía sau vật cản hoàn toàn không nhận được ánh sáng từ nguồn sáng.", True),
                        ("b", "Vùng bóng nửa tối chỉ nhận được một phần ánh sáng từ nguồn sáng rộng.", True),
                        ("c", "Nhật thực toàn phần quan sát được ở vùng bóng tối của Mặt Trăng trên Trái Đất.", True),
                        ("d", "Bóng tối hình thành chứng minh ánh sáng truyền theo đường cong uốn lượn.", False)
                    ], "Bóng tối là hệ quả trực tiếp của định luật truyền thẳng ánh sáng.")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Chiếu tia tới với góc tới bằng 45 độ. Góc phản xạ bằng bao nhiêu độ?", "45", "45 độ."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - Một vật cách gương phẳng 50 cm. Ảnh của vật cách gương phẳng bao nhiêu cm?", "50", "50 cm."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Tia sáng tới hợp với mặt gương góc 60 độ. Góc hợp bởi tia tới và tia phản xạ là bao nhiêu độ?", "60", "i = 90 - 60 = 30° => r = 30° => góc = 60°."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Một người cao 1,6 m đứng trước gương phẳng cách gương 1,5 m. Chiều cao của ảnh người đó trong gương là bao nhiêu mét?", "1.6", "1,6 m."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Để nhìn thấy toàn bộ cơ thể trong một chiếc gương phẳng treo thẳng đứng trên tường, chiều cao tối thiểu của tấm gương phải bằng bao nhiêu phần chiều cao cơ thể người đó? (Trả lời: 1/2 hay 1/4)", "1/2", "Chiều cao tối thiểu bằng 1/2 chiều cao người."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Giữ nguyên tia tới SI, nếu quay gương phẳng quanh trục qua điểm tới I một góc 15 độ thì tia phản xạ sẽ quay đi một góc bao nhiêu độ?", "30", "Tia phản xạ quay đi 2α = 2 × 15° = 30°.")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Bác sĩ nha khoa thường dùng một chiếc gương tròn nhỏ đưa vào trong miệng bệnh nhân để khám răng. Chiếc gương này giúp nha sĩ:", ["Tận dụng tính chất phản xạ ánh sáng để chiếu sáng và nhìn thấy ảnh các góc khuất phía sau răng", "Để đo nhiệt độ miệng", "Để mài răng", "Để chụp X quang"], 0, "Quan sát ảnh của các mặt sau và góc khuất của răng."),
                    make_vdc(2, f"Đề {t} - Kính tiềm vọng trên tàu ngầm dùng để quan sát mục tiêu trên mặt nước khi tàu ngầm đang lặn. Kính tiềm vọng đơn giản nhất được cấu tạo bởi:", ["Hai gương phẳng đặt song song và nghiêng góc 45 độ so với trục ống ngắm", "Một thấu kính phân kì", "Hai gương cầu lồi", "Một lăng kính tam giác"], 0, "Hai gương phẳng nghiêng 45° phản xạ ánh sáng 2 lần góc 90°."),
                    make_vdc(3, f"Đề {t} - Vì sao trên đầu xe cứu thương (Ambulance), dòng chữ 'AMBULANCE' thường được in ngược từ phải sang trái (ꓱƆИA⅃UᙠMA)?", ["Để tài xế xe phía trước nhìn qua gương chiếu hậu sẽ thấy dòng chữ xuôi chiều 'AMBULANCE' rõ ràng và kịp thời nhường đường", "Do máy in bị lỗi", "Là phong cách thẩm mỹ", "Để người đi bộ đọc dễ hơn"], 0, "Gương chiếu hậu tạo ảnh đảo trái phải giúp nhìn xuôi chiều."),
                    make_vdc(4, f"Đề {t} - Trên nóc các tòa nhà chọc trời hoặc ngọn hải đăng thường gắn đèn chớp màu đỏ nhấp nháy vào ban đêm nhằm mục đích:", ["Đánh dấu vật cản trên cao giúp máy bay và tàu thuyền định vị chướng ngại vật từ xa đảm bảo an toàn hàng không và hàng hải", "Để chiếu sáng đường phố", "Để thu hút chim di cư", "Để sưởi ấm mái nhà"], 0, "Cảnh báo an toàn hàng không và hàng hải.")
                ]

            # ======================== CHƯƠNG VI: TỪ ========================
            else:
                p1 = [
                    make_mc(1, "Nhận biết", f"Đề {t} - Nam châm vĩnh cửu có bao nhiêu cực từ chính?", ["2 cực (cực Bắc N và cực Nam S)", "1 cực", "3 cực", "4 cực"], 0, "Cực Bắc (North - N) và cực Nam (South - S)."),
                    make_mc(2, "Nhận biết", f"Đề {t} - Tương tác giữa hai cực từ của nam châm tuân theo quy tắc:", ["Các cực cùng tên thì đẩy nhau, khác tên thì hút nhau", "Cùng tên hút nhau", "Luôn luôn hút nhau", "Không tương tác"], 0, "Cùng tên đẩy, khác tên hút."),
                    make_mc(3, "Nhận biết", f"Đề {t} - Kim la bàn luôn định hướng theo phương nào khi để tự do trên mặt đất?", ["Phương Bắc - Nam địa lí", "Phương Đông - Tây", "Tùy ý", "Phương thẳng đứng"], 0, "Định hướng Bắc - Nam nhờ từ trường Trái Đất."),
                    make_mc(4, "Nhận biết", f"Đề {t} - Không gian xung quanh nam châm hoặc dây dẫn mang dòng điện có:", ["Từ trường", "Điện trường tĩnh", "Chân không", "Khí hydro"], 0, "Xung quanh nam châm có từ trường."),
                    make_mc(5, "Nhận biết", f"Đề {t} - Hình ảnh các đường mạt sắt sắp xếp xung quanh nam châm được gọi là:", ["Từ phổ", "Quang phổ", "Sóng âm", "Tia sáng"], 0, "Từ phổ."),
                    make_mc(6, "Nhận biết", f"Đề {t} - Chiều của đường sức từ bên ngoài nam châm thẳng được quy ước đi:", ["Ra cực Bắc (N), vào cực Nam (S)", "Ra cực Nam, vào cực Bắc", "Từ trong ra ngoài", "Từ dưới lên trên"], 0, "Quy ước: Ra Bắc Vào Nam."),
                    make_mc(7, "Thông hiểu", f"Đề {t} - Nam châm có khả năng hút mạnh các vật liệu làm từ chất nào sau đây?", ["Sắt, thép, niken, coban", "Đồng, nhôm", "Vàng, bạc", "Nhựa, gỗ, thủy tinh"], 0, "Hút các vật liệu từ tính (Fe, Ni, Co...)."),
                    make_mc(8, "Thông hiểu", f"Đề {t} - Nam châm điện đơn giản được cấu tạo gồm:", ["Một ống dây quấn quanh một lõi sắt non và nối với nguồn điện", "Một thanh nhôm", "Một cục pin và miếng gỗ", "Một miếng nam châm vĩnh cửu"], 0, "Cuộn dây có lõi sắt non khi có dòng điện."),
                    make_mc(9, "Thông hiểu", f"Đề {t} - Để tăng lực từ của nam châm điện, ta có thể:", ["Tăng cường độ dòng điện hoặc tăng số vòng quấn của cuộn dây", "Giảm cường độ dòng điện", "Giảm số vòng dây", "Thay lõi sắt bằng lõi nhựa"], 0, "Tăng dòng điện hoặc tăng số vòng dây."),
                    make_mc(10, "Thông hiểu", f"Đề {t} - Ưu điểm nổi bật của nam châm điện so với nam châm vĩnh cửu là:", ["Có thể bật/tắt từ tính dễ dàng bằng cách ngắt điện và điều chỉnh lực từ mạnh yếu", "Không cần dùng điện", "Lực từ không đổi", "Nhẹ hơn"], 0, "Điều khiển được lực từ và đóng ngắt linh hoạt."),
                    make_mc(11, "Thông hiểu", f"Đề {t} - Cần cẩu bốc dỡ phế liệu sắt thép ở bến cảng sử dụng loại nam châm nào?", ["Nam châm điện công suất lớn", "Nam châm vĩnh cửu", "Nam châm gốm", "La bàn"], 0, "Nam châm điện ngắt điện để thả hàng xuống."),
                    make_mc(12, "Thông hiểu", f"Đề {t} - Trái Đất của chúng ta hoạt động như một nam châm khổng lồ với:", ["Cực từ nam ở gần cực Bắc địa lí và cực từ bắc ở gần cực Nam địa lí", "Cực từ bắc trùng khít cực Bắc địa lí", "Không có từ trường", "Hai cực từ ở xích đạo"], 0, "Cực từ Bắc của la bàn chỉ về cực Bắc địa lí vì ở đó có cực Nam từ trường Trái Đất.")
                ]
                p2 = [
                    make_tf(1, "Thông hiểu", f"Đề {t} - Về từ tính của nam châm:", [
                        ("a", "Mỗi thanh nam châm khi bẻ đôi vẫn tạo thành hai nam châm mới có đủ hai cực Bắc - Nam.", True),
                        ("b", "Không bao giờ tồn tại một nam châm chỉ có một cực từ đơn lẻ trong tự nhiên.", True),
                        ("c", "Hai cực cùng tên của hai nam châm sẽ hút lẫn nhau.", False),
                        ("d", "Lực từ mạnh nhất ở hai đầu cực của nam châm.", True)
                    ], "Cùng tên đẩy nhau, khác tên hút nhau."),
                    make_tf(2, "Thông hiểu", f"Đề {t} - Về đường sức từ và từ trường:", [
                        ("a", "Nơi nào từ trường mạnh thì các đường sức từ dày (mau), nơi từ trường yếu thì đường sức từ thưa.", True),
                        ("b", "Bên ngoài nam châm, đường sức từ đi ra từ cực Bắc và đi vào cực Nam.", True),
                        ("c", "Các đường sức từ có thể cắt nhau tại nhiều điểm trong không gian.", False),
                        ("d", "Từ trường Trái Đất bảo vệ sinh quyển khỏi bức xạ bão từ nguy hiểm từ Mặt Trời.", True)
                    ], "Các đường sức từ là các đường cong khép kín không bao giờ cắt nhau."),
                    make_tf(3, "Vận dụng", f"Đề {t} - Xét một nam châm điện có lõi sắt non:", [
                        ("a", "Khi ngắt công tắc điện, nam châm điện mất gần như hoàn toàn từ tính.", True),
                        ("b", "Nếu thay lõi sắt non bằng lõi thép thì khi ngắt điện lõi thép vẫn giữ được từ tính lâu dài.", True),
                        ("c", "Đảo chiều dòng điện chạy qua cuộn dây làm đổi tên các cực từ của nam châm điện.", True),
                        ("d", "Rút bỏ lõi sắt non ra khỏi cuộn dây làm lực từ tăng lên gấp nhiều lần.", False)
                    ], "Lõi sắt non có tác dụng làm tăng lực từ lên rất nhiều lần."),
                    make_tf(4, "Vận dụng", f"Đề {t} - Cho một kim nam châm nhỏ đặt thăng bằng tự do trên một mũi nhọn:", [
                        ("a", "Cực Bắc của kim nam châm thường được sơn màu đỏ hoặc kí hiệu chữ N.", True),
                        ("b", "Khi đưa cực Nam của một thanh nam châm lại gần cực Bắc của kim nam châm thì chúng hút nhau.", True),
                        ("c", "Nếu đưa một thanh đồng lại gần kim nam châm thì kim nam châm sẽ bị hút mãnh liệt.", False),
                        ("d", "Khi có dòng điện chạy qua dây dẫn đặt song song phía trên kim nam châm, kim nam châm bị lệch đi.", True)
                    ], "Đồng không phải là chất từ tính nên không bị nam châm hút.")
                ]
                p3 = [
                    make_sa(1, "Thông hiểu", f"Đề {t} - Cực Bắc của nam châm được kí hiệu bằng chữ cái in hoa nào?", "N", "Chữ N (North)."),
                    make_sa(2, "Thông hiểu", f"Đề {t} - Cực Nam của nam châm được kí hiệu bằng chữ cái in hoa nào?", "S", "Chữ S (South)."),
                    make_sa(3, "Vận dụng", f"Đề {t} - Khi đưa hai cực Bắc của hai nam châm lại gần nhau, chúng hút nhau hay đẩy nhau?", "Đẩy nhau", "Đẩy nhau."),
                    make_sa(4, "Vận dụng", f"Đề {t} - Chiều của đường sức từ bên ngoài thanh nam châm đi ra ở cực nào? (Bắc hay Nam)", "Bắc", "Ra Bắc vào Nam."),
                    make_sa(5, "Vận dụng cao", f"Đề {t} - Một cuộn dây có dòng điện 1A quấn 200 vòng hút được 10 cái ghim giấy. Nếu tăng lên 400 vòng và dòng điện 2A, lực từ tăng lên khoảng bao nhiêu lần?", "4", "Lực từ tỉ lệ với I × N => tăng 2 × 2 = 4 lần."),
                    make_sa(6, "Vận dụng cao", f"Đề {t} - Lõi của nam châm điện dùng trong công nghiệp đóng ngắt tự động (rơle) làm bằng vật liệu nào? (Sắt non hay Thép tôi)", "Sắt non", "Sắt non (khử từ nhanh khi ngắt điện).")
                ]
                p4 = [
                    make_vdc(1, f"Đề {t} - Tàu đệm từ (Maglev) có thể chạy với tốc độ trên 500 km/h mà không gây ra tiếng ồn ma sát bánh xe với đường ray là nhờ ứng dụng:", ["Nguyên lí tương tác đẩy và hút của các nam châm điện siêu dẫn giúp nâng đoàn tàu lơ lửng trên đường ray", "Động cơ phản lực", "Đệm không khí thổi từ dưới", "Hệ thống bánh răng"], 0, "Lực từ nâng tàu lơ lửng triệt tiêu ma sát mặt ray."),
                    make_vdc(2, f"Đề {t} - Rơle điện từ (Relay) được ứng dụng trong các mạch điện bảo vệ tự động (như ngắt điện khi quá tải, bật đèn tự động) dựa trên bộ phận cốt lõi là:", ["Một nam châm điện hút thanh sắt đóng hoặc ngắt tiếp điểm của mạch", "Một cầu chì dây chì", "Một công tắc xoay tay", "Một biến trở con chạy"], 0, "Nam châm điện đóng ngắt tiếp điểm tự động."),
                    make_vdc(3, f"Đề {t} - Hiện tượng cực quang (Aurora) tuyệt đẹp xuất hiện trên bầu trời đêm ở hai vùng cực Bắc và Nam của Trái Đất là kết quả của sự tương tác giữa:", ["Các hạt mang điện từ gió Mặt Trời bị từ trường Trái Đất bẫy và tương tác với các phân tử khí quyển", "Ánh sáng phản chiếu từ băng tuyết", "Pháo hoa trên vũ trụ", "Sóng âm của cá voi"], 0, "Bão từ Mặt Trời tương tác với từ trường Trái Đất."),
                    make_vdc(4, f"Đề {t} - Trong thẻ ATM, thẻ tín dụng và thẻ tàu điện ngầm có một dải băng màu đen phía sau (dải từ). Dải từ này dùng để lưu trữ thông tin tài khoản bằng cách:", ["Từ hóa các hạt oxit sắt siêu nhỏ theo các mẫu từ trường mã hóa nhị phân 0 và 1", "Khắc chữ chìm bằng laser", "In mực dẫn điện", "Dán vi mạch quang học"], 0, "Mã hóa thông tin trên dải từ tính.")
                ]

            exams[k] = {
                "title": f"Đề kiểm tra KHTN 7 (Vật lý) - {l_name} - Đề số {t:02d}",
                "grade": "7", "subject": "physics", "subjectName": "Vật lý",
                "chapterId": ch_id, "chapterTitle": ch_title,
                "lessonId": l_id, "lessonName": l_name,
                "testNum": t, "duration": "45 phút", "points": 10.0,
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    return exams

if __name__ == "__main__":
    exs = build_phys7_exams()
    print("Phys 7 generated total:", len(exs), "exams.")
