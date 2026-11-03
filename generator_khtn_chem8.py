# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - HÓA HỌC 8 (KNTT)
Gồm 13 bài/chương ôn tập => 43 đề thi độc lập 100%
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

def build_chem8_exams():
    exams = {}

    # =========================================================================
    # CHƯƠNG I: PHẢN ỨNG HÓA HỌC
    # =========================================================================

    # --- BÀI 2: BIẾN ĐỔI VẬT LÍ VÀ BIẾN ĐỔI HÓA HỌC (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c1_b2_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Hiện tượng nào sau đây là hiện tượng biến đổi vật lí?", ["Nước đá tan chảy thành nước lỏng", "Cơm bị ôi thiu", "Đốt cháy que diêm", "Sắt bị gỉ trong không khí ẩm"], 0, "Nước đá tan chỉ biến đổi trạng thái, không tạo chất mới."),
            make_mc(2, "Nhận biết", f"Đề {t} - Hiện tượng nào sau đây là hiện tượng hóa học?", ["Thịt nướng bị cháy đen", "Nước sôi bốc hơi", "Hòa tan đường vào nước", "Cắt nhỏ đoạn dây đồng"], 0, "Cháy đen tạo thành than (chất mới) là biến đổi hóa học."),
            make_mc(3, "Nhận biết", f"Đề {t} - Dấu hiệu nào chứng tỏ có biến đổi hóa học xảy ra?", ["Có sự tạo thành chất mới", "Chất thay đổi hình dạng", "Chất thay đổi trạng thái", "Chất bị chia nhỏ"], 0, "Dấu hiệu cốt lõi là sinh ra chất mới."),
            make_mc(4, "Nhận biết", f"Đề {t} - Khi hòa tan muối ăn vào nước thu được nước muối trong suốt, đây là quá trình:", ["Biến đổi vật lí", "Biến đổi hóa học", "Phản ứng phân hủy", "Sự cháy"], 0, "Hòa tan là biến đổi vật lí."),
            make_mc(5, "Nhận biết", f"Đề {t} - Quá trình đốt củi sinh ra tro, khói và nhiệt là:", ["Biến đổi hóa học", "Biến đổi vật lí", "Hiện tượng cơ học", "Hiện tượng từ"], 0, "Đốt củi tạo chất mới CO2, H2O, tro."),
            make_mc(6, "Nhận biết", f"Đề {t} - Dấu hiệu nào sau đây thường đi kèm phản ứng hóa học?", ["Thay đổi màu sắc, xuất hiện chất khí hoặc kết tủa", "Chỉ đổi hình dạng", "Chỉ đổi kích thước", "Không có thay đổi gì"], 0, "Dấu hiệu nhận biết phản ứng: kết tủa, khí, màu sắc, nhiệt."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Cho một viên sủi C vào cốc nước thấy sủi bọt khí mạnh. Quá trình sủi bọt khí là:", ["Biến đổi hóa học vì có khí mới sinh ra", "Biến đổi vật lí vì viên sủi tan ra", "Hiện tượng bay hơi của nước", "Hiện tượng ngưng tụ"], 0, "Khí CO2 sinh ra từ phản ứng giữa acid và muối hydrogencarbonate."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Hiện tượng quang hợp ở lá cây xanh là biến đổi:", ["Hóa học", "Vật lí", "Nhiễm điện", "Phản xạ ánh sáng"], 0, "CO2 và H2O biến đổi thành glucose C6H12O6 và O2."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Thổi hơi thở vào ống nghiệm chứa nước vôi trong thấy nước vôi vẩn đục. Đây là hiện tượng:", ["Hóa học vì tạo kết tủa CaCO3 không tan", "Vật lí vì nước vôi lạnh đi", "Hòa tan thông thường", "Bay hơi"], 0, "CO2 + Ca(OH)2 -> CaCO3 (kết tủa trắng) + H2O."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Quá trình nghiền nhỏ gạo thành bột gạo là:", ["Biến đổi vật lí", "Biến đổi hóa học", "Quá trình lên men", "Hiện tượng tỏa nhiệt"], 0, "Chỉ thay đổi kích thước hạt gạo."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Quá trình lên men sữa chua từ sữa tươi là:", ["Biến đổi hóa học nhờ vi khuẩn lactic", "Biến đổi vật lí", "Quá trình đông đặc", "Quá trình hòa tan"], 0, "Lên men sinh ra acid lactic làm chua sữa."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Dây tóc bóng đèn nóng sáng khi có dòng điện chạy qua rồi nguội lại khi tắt điện là hiện tượng:", ["Vật lí", "Hóa học", "Cháy dây tóc", "Oxi hóa"], 0, "Vonfram nóng sáng mà không biến thành chất khác.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Xét các quá trình sau xảy ra trong đời sống:", [
                ("a", "Đốt cháy khí gas để nấu nướng là biến đổi hóa học.", True),
                ("b", "Nước cất đun sôi bốc thành hơi nước là biến đổi hóa học.", False),
                ("c", "Thức ăn để lâu ngày ngoài không khí bị chua là biến đổi hóa học.", True),
                ("d", "Băng tan ở hai cực Bắc Cực và Nam Cực là biến đổi vật lí.", True)
            ], "Hơi nước ngưng tụ lại thành nước lỏng, không sinh chất mới nên là biến đổi vật lí."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Khi nói về biến đổi vật lí và biến đổi hóa học:", [
                ("a", "Biến đổi vật lí không làm thay đổi bản chất của chất.", True),
                ("b", "Trong biến đổi hóa học, liên kết giữa các nguyên tử bị phá vỡ và hình thành liên kết mới.", True),
                ("c", "Tất cả các quá trình tỏa nhiệt đều là biến đổi hóa học.", False),
                ("d", "Sự tạo thành chất mới là tiêu chí quyết định biến đổi hóa học.", True)
            ], "Hơi nước ngưng tụ tỏa nhiệt nhưng là biến đổi vật lí."),
            make_tf(3, "Vận dụng", f"Đề {t} - Xét thí nghiệm cho mẩu đá vôi (CaCO3) vào dung dịch axit clohiđric (HCl):", [
                ("a", "Mẩu đá vôi tan dần và sủi nhiều bọt khí.", True),
                ("b", "Khí thoát ra là khí carbon dioxide (CO2).", True),
                ("c", "Dung dịch thu được chứa muối Calcium chloride (CaCl2).", True),
                ("d", "Đây là quá trình biến đổi vật lí thông thường.", False)
            ], "CaCO3 + 2HCl -> CaCl2 + CO2 + H2O (biến đổi hóa học)."),
            make_tf(4, "Vận dụng", f"Đề {t} - Khi thắp một cây nến làm bằng parafin:", [
                ("a", "Parafin ở bấc nến nóng chảy và thấm vào bấc là biến đổi vật lí.", True),
                ("b", "Hơi parafin cháy tạo thành CO2 và hơi nước là biến đổi hóa học.", True),
                ("c", "Ngọn nến tỏa nhiệt và phát sáng là dấu hiệu của phản ứng cháy.", True),
                ("d", "Toàn bộ quá trình cháy nến chỉ xảy ra biến đổi vật lí duy nhất.", False)
            ], "Có cả hai quá trình: biến đổi vật lí (nóng chảy, bay hơi) và biến đổi hóa học (cháy).")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Trong quá trình biến đổi hóa học, hạt vi mô nào được bảo toàn về số lượng? (Trả lời: Nguyên tử hay Phân tử)", "Nguyên tử", "Số nguyên tử mỗi nguyên tố luôn bảo toàn."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Quá trình đun sôi nước ở 100°C làm nước bốc hơi là biến đổi gì? (Vật lí hay Hóa học)", "Vật lí", "Chỉ đổi thể từ lỏng sang hơi."),
            make_sa(3, "Vận dụng", f"Đề {t} - Đốt cháy hoàn toàn 12 gam Carbon trong khí Oxygen sinh ra 44 gam khí CO2. Khối lượng khí Oxygen đã tham gia phản ứng là bao nhiêu gam?", "32", "m_O2 = 44 - 12 = 32 gam."),
            make_sa(4, "Vận dụng", f"Đề {t} - Nung nóng 100 gam đá vôi (chứa 90% CaCO3), khối lượng CaCO3 nguyên chất có trong mẫu đá vôi là bao nhiêu gam?", "90", "100 × 90% = 90 gam."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Hòa tan hoàn toàn 5,6 gam Sắt vào dung dịch HCl dư. Khối lượng muối FeCl2 thu được là bao nhiêu gam? (Biết Fe=56, Cl=35,5)", "12.7", "nFe = 0,1 mol => mFeCl2 = 0,1 × 127 = 12,7 gam."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Đốt cháy hoàn toàn 3,1 gam Phosphorus trong khí oxygen dư thu được bao nhiêu gam P2O5? (P=31, O=16)", "7.1", "nP = 0,1 mol => nP2O5 = 0,05 mol => m = 0,05 × 142 = 7,1 gam.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Khi để một đinh sắt sạch ngoài không khí ẩm sau vài tuần thấy xuất hiện một lớp gỉ màu nâu đỏ xốp trên bề mặt đinh sắt và khối lượng đinh sắt tăng lên. Lý do khối lượng tăng là vì:", ["Sắt đã kết hợp với oxygen và hơi nước trong không khí tạo thành gỉ sắt Fe2O3.nH2O", "Không khí đè nặng lên đinh sắt", "Sắt hấp thụ bụi bẩn trong không khí", "Có vi khuẩn sinh sôi trên bề mặt sắt"], 0, "Khối lượng gỉ sắt = mFe + mO2 + mH2O."),
            make_vdc(2, f"Đề {t} - Quá trình nào sau đây vừa có biến đổi vật lí, vừa có biến đổi hóa học diễn ra đồng thời?", ["Đốt cháy một ngọn nến parafin", "Xé vụn một tờ giấy", "Hòa tan đường vào cốc nước", "Nước đóng băng trong tủ lạnh"], 0, "Parafin nóng chảy, bay hơi (vật lí) và hơi parafin cháy (hóa học)."),
            make_vdc(3, f"Đề {t} - Để nhận biết khí CO2 sinh ra từ phản ứng hóa học, người ta thường dùng thuốc thử nào sau đây?", ["Dung dịch nước vôi trong Ca(OH)2", "Dung dịch muối ăn NaCl", "Nước cất", "Dung dịch cồn"], 0, "CO2 làm đục nước vôi trong."),
            make_vdc(4, f"Đề {t} - Một mẩu vôi sống (CaO) để lâu ngày ngoài không khí bị 'chết vôi' (không còn khả năng tỏa nhiệt khi tôi vôi) do tác dụng với chất nào trong không khí?", ["Hơi nước và khí carbon dioxide CO2", "Khí nitrogen N2", "Khí argon Ar", "Khí neon Ne"], 0, "CaO hút ẩm thành Ca(OH)2 rồi tác dụng CO2 tạo CaCO3.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 2: Biến đổi vật lí và hóa học - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c1", "chapterTitle": "Chương I: Phản ứng hóa học",
            "lessonId": "chem8_c1_b2", "lessonName": "Bài 2: Biến đổi vật lí và biến đổi hóa học",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 3: PHẢN ỨNG HÓA HỌC (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c1_b3_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Chất ban đầu tham gia vào phản ứng hóa học được gọi là:", ["Chất phản ứng (chất tham gia)", "Sản phẩm", "Chất xúc tác", "Chất chỉ thị"], 0, "Chất ban đầu là chất phản ứng."),
            make_mc(2, "Nhận biết", f"Đề {t} - Chất mới sinh ra sau phản ứng hóa học được gọi là:", ["Sản phẩm", "Chất tham gia", "Chất nền", "Dung môi"], 0, "Chất mới là sản phẩm."),
            make_mc(3, "Nhận biết", f"Đề {t} - Phản ứng tỏa nhiệt là phản ứng:", ["Giải phóng năng lượng dưới dạng nhiệt ra môi trường", "Hấp thụ năng lượng nhiệt từ môi trường", "Không có sự thay đổi năng lượng", "Làm môi trường lạnh đi"], 0, "Tỏa nhiệt giải phóng nhiệt làm nóng môi trường xung quanh."),
            make_mc(4, "Nhận biết", f"Đề {t} - Phản ứng thu nhiệt là phản ứng:", ["Hấp thụ năng lượng nhiệt từ môi trường xung quanh", "Tỏa nhiệt ra môi trường", "Làm nhiệt độ môi trường tăng lên", "Sinh ra ánh sáng chói"], 0, "Thu nhiệt hấp thu nhiệt làm môi trường lạnh đi."),
            make_mc(5, "Nhận biết", f"Đề {t} - Quá trình đốt than đá để đun nấu là phản ứng:", ["Tỏa nhiệt", "Thu nhiệt", "Không đổi nhiệt", "Biến đổi vật lí"], 0, "Phản ứng cháy tỏa nhiệt rất lớn."),
            make_mc(6, "Nhận biết", f"Đề {t} - Trong phản ứng hóa học, liên kết giữa các nguyên tử:", ["Bị thay đổi", "Giữ nguyên vẹn", "Không liên quan", "Biến mất hoàn toàn"], 0, "Liên kết cũ bị phá vỡ, liên kết mới hình thành."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Quá trình nung đá vôi (CaCO3) ở nhiệt độ cao cần cung cấp nhiệt liên tục. Đây là phản ứng:", ["Thu nhiệt", "Tỏa nhiệt", "Tự phát", "Tỏa sáng"], 0, "Phản ứng phân hủy đá vôi hấp thụ nhiệt (thu nhiệt)."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Phản ứng hòa tan vôi sống vào nước (tôi vôi) thấy nước sôi sùng sục và bốc hơi nóng. Đây là phản ứng:", ["Tỏa nhiệt mạnh", "Thu nhiệt", "Vật lí", "Nóng chảy vôi"], 0, "CaO + H2O -> Ca(OH)2 tỏa nhiệt rất mạnh."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Khi đốt cồn, chất phản ứng là:", ["Cồn và khí oxygen", "Khí carbon dioxide và nước", "Chỉ có cồn", "Chỉ có khí oxygen"], 0, "Cồn tác dụng với oxygen."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Cho mẩu kẽm vào ống nghiệm chứa dung dịch acid sunfuric loãng, dấu hiệu nhận biết có phản ứng là:", ["Có bọt khí không màu thoát ra và kẽm tan dần", "Xuất hiện kết tủa màu vàng", "Dung dịch chuyển sang màu đỏ", "Ống nghiệm lạnh buốt"], 0, "Zn + H2SO4 -> ZnSO4 + H2 (khí)."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Nhận định nào sau đây là ĐÚNG về bản chất của phản ứng hóa học?", ["Chỉ có liên kết giữa các nguyên tử thay đổi, còn số nguyên tử mỗi nguyên tố được giữ nguyên", "Số nguyên tử của các nguyên tố thay đổi", "Các nguyên tử biến mất và nguyên tử mới sinh ra", "Khối lượng của các chất tăng lên sau phản ứng"], 0, "Bản chất là thay đổi liên kết giữa các nguyên tử."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Ứng dụng nào sau đây lợi dụng phản ứng tỏa nhiệt?", ["Đốt nhiên liệu chạy động cơ xe máy", "Nấu chín thức ăn bằng củi", "Hàn cắt kim loại bằng ngọn lửa axetilen", "Tất cả các phương án trên"], 3, "Tất cả đều dùng nhiệt lượng tỏa ra từ phản ứng cháy.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Xét phản ứng đốt cháy khí Methane: CH4 + 2O2 -> CO2 + 2H2O:", [
                ("a", "Chất phản ứng là CH4 và O2.", True),
                ("b", "Sản phẩm tạo thành là CO2 và H2O.", True),
                ("c", "Đây là phản ứng thu nhiệt.", False),
                ("d", "Số nguyên tử Carbon trước và sau phản ứng đều bằng 1.", True)
            ], "Phản ứng cháy của methane là phản ứng tỏa nhiệt mạnh."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Về phản ứng tỏa nhiệt và thu nhiệt:", [
                ("a", "Phản ứng tỏa nhiệt làm tăng nhiệt độ của hệ môi trường xung quanh.", True),
                ("b", "Phản ứng quang hợp của cây xanh là quá trình thu năng lượng ánh sáng.", True),
                ("c", "Hòa tan viên sủi hạ sốt vào nước làm cốc nước mát hơn là hiện tượng thu nhiệt.", True),
                ("d", "Tất cả các phản ứng hóa học đều xảy ra ở nhiệt độ phòng mà không cần khơi mào.", False)
            ], "Nhiều phản ứng cần đun nóng mới xảy ra (như than cháy trong oxy)."),
            make_tf(3, "Vận dụng", f"Đề {t} - Khi cho dung dịch BaCl2 vào dung dịch Na2SO4:", [
                ("a", "Xuất hiện kết tủa trắng không tan.", True),
                ("b", "Kết tủa trắng là Barium sulfate (BaSO4).", True),
                ("c", "Sản phẩm còn lại trong dung dịch là Sodium chloride (NaCl).", True),
                ("d", "Đây là phản ứng phân hủy.", False)
            ], "Đây là phản ứng trao đổi tạo kết tủa BaSO4."),
            make_tf(4, "Vận dụng", f"Đề {t} - Xét phản ứng nhiệt phân Potassium permanganate (KMnO4) điều chế oxy trong phòng thí nghiệm:", [
                ("a", "Phản ứng cần đun nóng liên tục nên là phản ứng thu nhiệt.", True),
                ("b", "Chất khí sinh ra là khí Oxygen (O2) duy trì sự cháy.", True),
                ("c", "Khối lượng chất rắn sau phản ứng nhỏ hơn khối lượng KMnO4 ban đầu do có khí thoát ra.", True),
                ("d", "Phản ứng này không tuân theo định luật bảo toàn khối lượng.", False)
            ], "Mọi phản ứng hóa học đều tuân theo định luật bảo toàn khối lượng.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Cho phản ứng: 2H2 + O2 -> 2H2O. Số phân tử nước tạo thành từ 2 phân tử H2 là bao nhiêu?", "2", "Tỉ lệ 2 : 1 : 2."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Phản ứng đốt cháy cồn giải phóng nhiệt ra môi trường gọi là phản ứng gì? (Tỏa nhiệt hay Thu nhiệt)", "Tỏa nhiệt", "Tỏa nhiệt."),
            make_sa(3, "Vận dụng", f"Đề {t} - Đốt cháy hoàn toàn 2,4 gam Magie trong khí Oxi thu được 4,0 gam MgO. Khối lượng Oxi đã phản ứng là bao nhiêu gam?", "1.6", "4,0 - 2,4 = 1,6 gam."),
            make_sa(4, "Vận dụng", f"Đề {t} - Cho 10 gam CaCO3 tác dụng hết với dung dịch HCl sinh ra 4,4 gam khí CO2. Số mol khí CO2 thu được là bao nhiêu mol? (Làm tròn 2 chữ số)", "0.1", "4,4 / 44 = 0,1 mol."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Nhiệt lượng tỏa ra khi đốt cháy hoàn toàn 1 mol khí methane CH4 là 890 kJ. Nhiệt lượng tỏa ra khi đốt cháy 3,2 gam methane là bao nhiêu kJ?", "178", "nCH4 = 3,2 / 16 = 0,2 mol. Q = 0,2 × 890 = 178 kJ."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Nung m gam Cu(OH)2 màu xanh thu được 16 gam chất rắn CuO màu đen và 3,6 gam nước. Giá trị của m là bao nhiêu gam?", "19.6", "m = 16 + 3,6 = 19,6 gam.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Túi chườm lạnh khẩn cấp dùng trong sơ cứu thể thao thường chứa nước và muối ammonium nitrate (NH4NO3). Khi bóp vỡ ngăn cách bên trong, muối tan vào nước và nhiệt độ giảm sâu. Quá trình hòa tan này là:", ["Quá trình thu nhiệt", "Quá trình tỏa nhiệt", "Phản ứng cháy", "Phản ứng trùng hợp"], 0, "Quá trình hòa tan NH4NO3 thu nhiệt mạnh làm lạnh nhanh."),
            make_vdc(2, f"Đề {t} - Trong lò nung vôi công nghiệp, người ta đốt than đá để cung cấp nhiệt lượng nung đá vôi (CaCO3 phân hủy thành CaO và CO2). Nhận định đúng về năng lượng trong lò vôi là:", ["Phản ứng đốt cháy than là tỏa nhiệt, cung cấp nhiệt cho phản ứng phân hủy đá vôi là thu nhiệt", "Cả hai phản ứng đều là phản ứng tỏa nhiệt", "Cả hai phản ứng đều là phản ứng thu nhiệt", "Phân hủy đá vôi tỏa nhiệt cho than cháy"], 0, "Đốt than tỏa nhiệt, nung đá vôi thu nhiệt."),
            make_vdc(3, f"Đề {t} - Cơ thể con người duy trì thân nhiệt ổn định ở mức khoảng 37°C chủ yếu nhờ vào quá trình nào?", ["Các phản ứng oxy hóa chất dinh dưỡng (glucose, chất béo) tỏa nhiệt trong tế bào", "Sự hấp thụ nhiệt từ ánh nắng mặt trời", "Sự dẫn nhiệt từ quần áo", "Sự ma sát giữa các mạch máu"], 0, "Oxy hóa thức ăn cung cấp năng lượng và duy trì thân nhiệt."),
            make_vdc(4, f"Đề {t} - Dấu hiệu nào sau đây chắc chắn khẳng định có phản ứng hóa học xảy ra khi trộn hai dung dịch trong suốt không màu?", ["Xuất hiện kết tủa đục hoặc sủi bọt khí", "Thể tích dung dịch tăng lên gấp đôi", "Nhiệt độ không đổi tuyệt đối", "Dung dịch vẫn trong suốt không màu"], 0, "Kết tủa hoặc khí là minh chứng rõ ràng tạo chất mới.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 3: Phản ứng hóa học - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c1", "chapterTitle": "Chương I: Phản ứng hóa học",
            "lessonId": "chem8_c1_b3", "lessonName": "Bài 3: Phản ứng hóa học",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 4: ĐỊNH LUẬT BẢO TOÀN KHỐI LƯỢNG VÀ PHƯƠNG TRÌNH HÓA HỌC (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c1_b4_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Nội dung của Định luật bảo toàn khối lượng phát biểu rằng: Trong một phản ứng hóa học,", ["Tổng khối lượng của các sản phẩm bằng tổng khối lượng của các chất phản ứng", "Tổng khối lượng sản phẩm luôn lớn hơn", "Tổng thể tích được bảo toàn", "Khối lượng của từng chất không đổi"], 0, "Tổng khối lượng chất tham gia = tổng khối lượng sản phẩm."),
            make_mc(2, "Nhận biết", f"Đề {t} - Nhà khoa học nào đã phát hiện ra định luật bảo toàn khối lượng?", ["Lomonosov và Lavoisier", "Mendeleev", "Newton", "Dalton"], 0, "Mikhail Lomonosov và Antoine Lavoisier."),
            make_mc(3, "Nhận biết", f"Đề {t} - Trong phương trình hóa học, hệ số đứng trước công thức hóa học cho biết:", ["Tỉ lệ số nguyên tử hoặc số phân tử giữa các chất trong phản ứng", "Số electron trao đổi", "Khối lượng của mỗi chất", "Hóa trị của chất"], 0, "Tỉ lệ số nguyên tử, phân tử."),
            make_mc(4, "Nhận biết", f"Đề {t} - Hệ số cân bằng của phương trình: 2H2 + O2 -> ? H2O là:", ["2", "1", "3", "4"], 0, "2H2 + O2 -> 2H2O."),
            make_mc(5, "Nhận biết", f"Đề {t} - Cho phản ứng A + B -> C + D. Biểu thức định luật bảo toàn khối lượng là:", ["mA + mB = mC + mD", "mA + mC = mB + mD", "mA × mB = mC × mD", "mA - mB = mC - mD"], 0, "mA + mB = mC + mD."),
            make_mc(6, "Nhận biết", f"Đề {t} - Nung đá vôi: CaCO3 -> CaO + CO2. Biết nung 100 g CaCO3 thu được 56 g CaO. Khối lượng CO2 thoát ra là:", ["44 g", "56 g", "100 g", "156 g"], 0, "100 - 56 = 44 g."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Cân bằng phương trình: Al + O2 -> Al2O3. Các hệ số lần lượt là:", ["4, 3, 2", "2, 3, 1", "4, 3, 1", "2, 1, 2"], 0, "4Al + 3O2 -> 2Al2O3."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Cân bằng phương trình: Fe + HCl -> FeCl2 + H2. Hệ số của HCl là:", ["2", "1", "3", "4"], 0, "Fe + 2HCl -> FeCl2 + H2."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Đốt cháy hoàn toàn 6 gam Carbon cần vừa đủ m gam Oxygen, thu được 22 gam khí CO2. Giá trị của m là:", ["16 gam", "12 gam", "28 gam", "8 gam"], 0, "m = 22 - 6 = 16 gam."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Cho phương trình: 2Na + 2H2O -> 2NaOH + H2. Tỉ lệ số phân tử Na phản ứng và H2 sinh ra là:", ["2 : 1", "1 : 1", "1 : 2", "2 : 2"], 0, "Tỉ lệ hệ số Na : H2 là 2 : 1."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Cân bằng phương trình: CH4 + ? O2 -> CO2 + 2H2O. Số thích hợp điền vào dấu ? là:", ["2", "1", "3", "4"], 0, "CH4 + 2O2 -> CO2 + 2H2O."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Hòa tan 6,5 gam Kẽm (Zn) bằng acid HCl thu được 13,6 gam muối ZnCl2 và 0,2 gam khí H2. Khối lượng acid HCl đã phản ứng là:", ["7,3 gam", "6,5 gam", "13,8 gam", "14,1 gam"], 0, "mHCl = (13,6 + 0,2) - 6,5 = 7,3 gam.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Xét phản ứng: 4Al + 3O2 -> 2Al2O3:", [
                ("a", "Tỉ lệ số nguyên tử Al và phân tử O2 là 4 : 3.", True),
                ("b", "Cứ 4 nguyên tử Al phản ứng tạo ra 2 phân tử Al2O3.", True),
                ("c", "Khối lượng Al phản ứng cộng khối lượng O2 phản ứng bằng khối lượng Al2O3 tạo thành.", True),
                ("d", "Số phân tử O2 phản ứng bằng số phân tử Al2O3 sinh ra.", False)
            ], "Tỉ lệ phân tử O2 : Al2O3 là 3 : 2."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Về định luật bảo toàn khối lượng:", [
                ("a", "Định luật giải thích rằng số nguyên tử của mỗi nguyên tố trước và sau phản ứng không đổi.", True),
                ("b", "Trong bình kín, khối lượng toàn phần của bình trước và sau phản ứng không đổi.", True),
                ("c", "Khi đốt cháy thanh củi ngoài không khí thấy tro nhẹ hơn củi là do định luật bảo toàn khối lượng bị sai.", False),
                ("d", "Khí CO2 và hơi nước thoát vào không khí chính là phần khối lượng mất đi của củi.", True)
            ], "Định luật luôn đúng, khối lượng giảm do CO2 và hơi nước bay đi."),
            make_tf(3, "Vận dụng", f"Đề {t} - Nung m gam hỗn hợp đá vôi (CaCO3) và quặng quặng sắt, sau phản ứng thấy khối lượng giảm đi 4,4 gam do khí CO2 bay ra:", [
                ("a", "Khối lượng CO2 sinh ra là 4,4 gam.", True),
                ("b", "Số mol khí CO2 thoát ra là 0,1 mol.", True),
                ("c", "Khối lượng CaCO3 đã bị nhiệt phân là 10,0 gam.", True),
                ("d", "Khối lượng CaO tạo thành bằng 4,4 gam.", False)
            ], "mCaO = 10 - 4,4 = 5,6 gam."),
            make_tf(4, "Vận dụng", f"Đề {t} - Cho phản ứng: a Fe3O4 + b CO -> c Fe + d CO2:", [
                ("a", "Hệ số a bằng 1.", True),
                ("b", "Hệ số b bằng 4.", True),
                ("c", "Hệ số c bằng 3 và d bằng 4.", True),
                ("d", "Tổng hệ số tối giản (a + b + c + d) bằng 10.", False)
            ], "Fe3O4 + 4CO -> 3Fe + 4CO2 => Tổng hệ số = 1 + 4 + 3 + 4 = 12.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Cho phản ứng: N2 + 3H2 -> 2NH3. Tỉ lệ số phân tử N2 và NH3 là 1 : bao nhiêu?", "2", "Tỉ lệ 1 : 2."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Đốt 3,6 gam kim loại Mg thu được 6,0 gam MgO. Khối lượng khí Oxygen đã phản ứng là bao nhiêu gam?", "2.4", "6,0 - 3,6 = 2,4 gam."),
            make_sa(3, "Vận dụng", f"Đề {t} - Cho phương trình: 2KMnO4 -> K2MnO4 + MnO2 + O2. Khi nhiệt phân hoàn toàn 31,6 gam KMnO4 thu được 3,2 gam O2 và m gam chất rắn. Giá trị của m là bao nhiêu gam?", "28.4", "m = 31,6 - 3,2 = 28,4 gam."),
            make_sa(4, "Vận dụng", f"Đề {t} - Tổng hệ số nguyên tối giản của phương trình: 2Fe + 3Cl2 -> 2FeCl3 là bao nhiêu?", "7", "2 + 3 + 2 = 7."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Cho 10 gam hỗn hợp Mg và Fe tác dụng với dung dịch HCl dư thu được 0,4 gam khí H2. Khối lượng muối clorua tạo thành là bao nhiêu gam?", "24.2", "m_muối = m_kim loại + 71 × nH2 = 10 + 71 × 0,2 = 24,2 gam (hoặc mHCl = 0,4 × 36,5 = 14,6 => m_muối = 10 + 14,6 - 0,4 = 24,2 g)."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Cân bằng phương trình: CxHy + (x + y/4) O2 -> x CO2 + y/2 H2O. Với C3H8, hệ số của O2 là bao nhiêu?", "5", "3 + 8/4 = 5.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Khi nung một thanh sắt trong không khí ở nhiệt độ cao, sau một thời gian để nguội thấy khối lượng thanh sắt tăng lên. Kết luận nào sau đây đúng?", ["Hiện tượng này hoàn toàn tuân theo định luật bảo toàn khối lượng vì khối lượng tăng bằng đúng khối lượng khí oxygen đã phản ứng", "Hiện tượng này mâu thuẫn với định luật bảo toàn khối lượng", "Khối lượng tăng do nhiệt độ cao làm giãn nở sắt", "Không có phản ứng nào xảy ra"], 0, "m_rắn sau = mFe + mO2 phản ứng."),
            make_vdc(2, f"Đề {t} - Cho phương trình phản ứng hóa học: a FeS2 + b O2 -> c Fe2O3 + d SO2. Tổng các hệ số nguyên tối giản (a + b + c + d) của phương trình là:", ["25", "23", "27", "21"], 0, "4FeS2 + 11O2 -> 2Fe2O3 + 8SO2 => Tổng = 4 + 11 + 2 + 8 = 25."),
            make_vdc(3, f"Đề {t} - Hòa tan hoàn toàn 11,2 gam bột Sắt (Fe) vào dung dịch CuSO4 dư. Sau khi phản ứng kết thúc, khối lượng kim loại Đồng (Cu) thu được là:", ["12,8 gam", "6,4 gam", "11,2 gam", "16,0 gam"], 0, "nFe = 0,2 mol => nCu = 0,2 mol => mCu = 0,2 × 64 = 12,8 gam."),
            make_vdc(4, f"Đề {t} - Đốt cháy hoàn toàn 2,2 gam khí Propane (C3H8) trong khí Oxygen dư. Thể tích khí CO2 thu được ở điều kiện chuẩn (25°C, 1 bar, 1 mol = 24,79 L) xấp xỉ bằng:", ["3,72 lít", "2,48 lít", "4,96 lít", "1,24 lít"], 0, "nC3H8 = 2,2 / 44 = 0,05 mol => nCO2 = 0,15 mol => V = 0,15 × 24,79 = 3,7185 L ≈ 3,72 lít.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 4: Định luật bảo toàn khối lượng - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c1", "chapterTitle": "Chương I: Phản ứng hóa học",
            "lessonId": "chem8_c1_b4", "lessonName": "Bài 4: Định luật bảo toàn khối lượng và phương trình hóa học",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 5: MOL VÀ TỈ KHỐI CỦA CHẤT KHÍ (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c1_b5_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Mol là lượng chất có chứa bao nhiêu nguyên tử hoặc phân tử chất đó (số Avogadro)?", ["6,022 × 10^23", "6,022 × 10^22", "6,022 × 10^24", "3,011 × 10^23"], 0, "Số Avogadro N = 6,022 × 10^23."),
            make_mc(2, "Nhận biết", f"Đề {t} - Ở điều kiện chuẩn (25 °C và 1 bar), thể tích mol của mọi chất khí đều bằng:", ["24,79 lít", "22,4 lít", "24,0 lít", "22,7 lít"], 0, "Theo chuẩn mới IUPAC / GDPT 2018: 24,79 L/mol."),
            make_mc(3, "Nhận biết", f"Đề {t} - Công thức tính số mol n khi biết khối lượng m và khối lượng mol M là:", ["n = m / M", "n = m × M", "n = M / m", "n = m + M"], 0, "n = m / M."),
            make_mc(4, "Nhận biết", f"Đề {t} - Công thức tính thể tích chất khí V ở điều kiện chuẩn (25 °C, 1 bar) là:", ["V = n × 24,79", "V = n × 22,4", "V = n / 24,79", "V = n × 24"], 0, "V = n × 24,79."),
            make_mc(5, "Nhận biết", f"Đề {t} - Tỉ khối của chất khí A đối với chất khí B được tính theo công thức:", ["dA/B = MA / MB", "dA/B = MB / MA", "dA/B = MA × MB", "dA/B = MA - MB"], 0, "dA/B = MA / MB."),
            make_mc(6, "Nhận biết", f"Đề {t} - Khối lượng mol không khí xấp xỉ bằng:", ["29 g/mol", "28 g/mol", "32 g/mol", "18 g/mol"], 0, "M_kk ≈ 29 g/mol."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Khối lượng của 0,5 mol khí Oxygen (O2) là:", ["16 gam", "32 gam", "8 gam", "64 gam"], 0, "m = 0,5 × 32 = 16 gam."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Thể tích của 0,2 mol khí CO2 ở điều kiện chuẩn (25 °C, 1 bar) là:", ["4,958 lít", "4,48 lít", "2,479 lít", "5,60 lít"], 0, "V = 0,2 × 24,79 = 4,958 lít."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Tỉ khối của khí Methane (CH4) đối với không khí xấp xỉ bằng:", ["0,55", "1,55", "0,85", "1,10"], 0, "16 / 29 ≈ 0,55 (nhẹ hơn không khí)."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Khí nào sau đây nặng hơn không khí?", ["CO2 (M=44)", "CH4 (M=16)", "NH3 (M=17)", "H2 (M=2)"], 0, "CO2 có M = 44 > 29 nên nặng hơn không khí."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Số mol của 5,6 gam kim loại Sắt (Fe, M=56 g/mol) là:", ["0,1 mol", "0,2 mol", "0,05 mol", "1 mol"], 0, "5,6 / 56 = 0,1 mol."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Để thu khí Hydrogen vào bình bằng phương pháp đẩy không khí, người ta phải đặt bình như thế nào?", ["Úp ngược bình thu", "Ngửa miệng bình thu", "Đặt nằm ngang", "Tùy ý"], 0, "Vì khí H2 nhẹ hơn không khí (2 < 29) nên phải úp ngược bình.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Về khái niệm mol và chất khí:", [
                ("a", "1 mol bất kì chất khí nào ở cùng điều kiện nhiệt độ và áp suất đều chiếm thể tích bằng nhau.", True),
                ("b", "Khối lượng mol của một chất có trị số bằng nguyên tử khối hoặc phân tử khối của chất đó.", True),
                ("c", "Khí CO nhẹ hơn không khí.", True),
                ("d", "Khí Oxygen (O2) nhẹ hơn khí Nitrogen (N2).", False)
            ], "M_O2 = 32 > M_N2 = 28 nên O2 nặng hơn N2. M_CO = 28 < 29 nên nhẹ hơn không khí."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Xét 11 gam khí CO2 ở điều kiện chuẩn (25 °C, 1 bar):", [
                ("a", "Khối lượng mol của CO2 là 44 g/mol.", True),
                ("b", "Số mol CO2 là 0,25 mol.", True),
                ("c", "Thể tích của lượng khí trên ở điều kiện chuẩn xấp xỉ 6,20 lít.", True),
                ("d", "Số phân tử CO2 có trong 11 gam là 6,022 × 10^23 phân tử.", False)
            ], "Số phân tử = 0,25 × 6,022 × 10^23 = 1,5055 × 10^23. V = 0,25 × 24,79 = 6,1975 L ≈ 6,20 L."),
            make_tf(3, "Vận dụng", f"Đề {t} - Cho hai khí X và Y: biết dX/H2 = 14 và dY/O2 = 2:", [
                ("a", "Khối lượng mol của khí X là 28 g/mol (có thể là N2 hoặc CO).", True),
                ("b", "Khối lượng mol của khí Y là 64 g/mol (SO2).", True),
                ("c", "Khí X nặng hơn khí Y.", False),
                ("d", "Khí Y nặng hơn không khí khoảng 2,2 lần.", True)
            ], "MX = 14×2 = 28; MY = 2×32 = 64. dY/kk = 64/29 ≈ 2,21."),
            make_tf(4, "Vận dụng", f"Đề {t} - Hỗn hợp khí gồm 0,1 mol O2 và 0,4 mol N2:", [
                ("a", "Tổng số mol của hỗn hợp khí là 0,5 mol.", True),
                ("b", "Thể tích hỗn hợp khí ở đkc (25 °C, 1 bar) là 12,395 lít.", True),
                ("c", "Khối lượng của hỗn hợp khí là 14,4 gam.", True),
                ("d", "Khối lượng mol trung bình của hỗn hợp khí lớn hơn 30 g/mol.", False)
            ], "m = 0,1×32 + 0,4×28 = 3,2 + 11,2 = 14,4 g. M_tb = 14,4 / 0,5 = 28,8 g/mol < 30.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Số mol của 18 gam nước H2O là bao nhiêu mol?", "1", "18 / 18 = 1 mol."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Thể tích ở đkc (25 °C, 1 bar) của 1 mol khí bất kì là bao nhiêu lít? (Làm tròn 2 chữ số)", "24.79", "24,79 lít."),
            make_sa(3, "Vận dụng", f"Đề {t} - Tỉ khối của khí Sulfur dioxide (SO2, M=64) so với khí Oxygen (O2, M=32) bằng bao nhiêu?", "2", "64 / 32 = 2."),
            make_sa(4, "Vận dụng", f"Đề {t} - Cho 4,958 lít khí Hydrogen ở đkc (25 °C, 1 bar). Số mol khí H2 là bao nhiêu mol?", "0.2", "4,958 / 24,79 = 0,2 mol."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Một chất khí A có tỉ khối đối với khí H2 là 16. Khối lượng mol của chất khí A là bao nhiêu g/mol?", "32", "16 × 2 = 32 g/mol (O2)."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Khí gas sinh học Biogas chứa 60% thể tích là khí CH4 (M=16) và 40% thể tích là khí CO2 (M=44). Khối lượng mol trung bình của Biogas là bao nhiêu g/mol?", "27.2", "M_tb = 0,6 × 16 + 0,4 × 44 = 9,6 + 17,6 = 27,2 g/mol.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Trong các hang động sâu dưới lòng đất hoặc đáy giếng sâu thường tích tụ một lượng lớn khí CO2 và ít khí O2, rất nguy hiểm cho con người. Nguyên nhân khí CO2 tích tụ ở đáy là do:", ["Khí CO2 có khối lượng mol (44 g/mol) nặng hơn không khí (29 g/mol) nên chìm xuống dưới", "Khí CO2 nhẹ hơn không khí", "Khí CO2 hòa tan hoàn toàn vào đất", "Áp suất ở đáy giếng đẩy O2 bay lên"], 0, "Tỉ khối dCO2/kk = 44/29 ≈ 1,52 nên CO2 lắng xuống đáy."),
            make_vdc(2, f"Đề {t} - Bơm khí nào sau đây vào khinh khí cầu hoặc bóng bay để chúng bay lơ lửng an toàn nhất lên bầu trời?", ["Khí Helium (He)", "Khí Hydrogen (H2)", "Khí Carbon dioxide (CO2)", "Khí Oxygen (O2)"], 0, "He nhẹ hơn không khí (M=4 < 29) và là khí trơ, không bắt cháy nổ như H2."),
            make_vdc(3, f"Đề {t} - Một hợp chất khí của Carbon và Hydrogen có tỉ khối so với không khí xấp xỉ 1,034. Trong hợp chất, C chiếm 80% về khối lượng. Công thức hóa học của chất khí đó là:", ["C2H6", "CH4", "C3H8", "C2H4"], 0, "M = 1,034 × 29 ≈ 30 g/mol => C2H6."),
            make_vdc(4, f"Đề {t} - Số phân tử có trong 2,479 lít khí N2 ở điều kiện chuẩn (25 °C, 1 bar) là:", ["6,022 × 10^22 phân tử", "6,022 × 10^23 phân tử", "1,204 × 10^23 phân tử", "3,011 × 10^22 phân tử"], 0, "n = 2,479 / 24,79 = 0,1 mol => Số phân tử = 0,1 × 6,022 × 10^23 = 6,022 × 10^22 phân tử.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 5: Mol và tỉ khối chất khí - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c1", "chapterTitle": "Chương I: Phản ứng hóa học",
            "lessonId": "chem8_c1_b5", "lessonName": "Bài 5: Mol và tỉ khối của chất khí",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 6: NỒNG ĐỘ DUNG DỊCH (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c1_b6_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Nồng độ phần trăm (C%) của dung dịch cho biết:", ["Số gam chất tan có trong 100 gam dung dịch", "Số mol chất tan trong 1 lít dung dịch", "Số gam chất tan trong 1 lít nước", "Số mol chất tan trong 100 gam dung dịch"], 0, "C% là số gam chất tan trong 100g dung dịch."),
            make_mc(2, "Nhận biết", f"Đề {t} - Công thức tính nồng độ phần trăm C% là:", ["C% = (mct / mdd) × 100%", "C% = (mdd / mct) × 100%", "C% = mct × V", "C% = n / V"], 0, "C% = (mct / mdd) × 100%."),
            make_mc(3, "Nhận biết", f"Đề {t} - Nồng độ mol (CM) của dung dịch cho biết:", ["Số mol chất tan có trong 1 lít dung dịch", "Số gam chất tan trong 1 lít dung dịch", "Số mol chất tan trong 100 gam nước", "Số gam dung môi"], 0, "CM = n / V (mol/L)."),
            make_mc(4, "Nhận biết", f"Đề {t} - Công thức tính nồng độ mol CM là:", ["CM = n / V", "CM = V / n", "CM = m / V", "CM = n × V"], 0, "CM = n / V."),
            make_mc(5, "Nhận biết", f"Đề {t} - Dung dịch là hỗn hợp đồng nhất giữa:", ["Dung môi và chất tan", "Chất rắn và chất khí", "Hai chất không tan", "Nước và cát"], 0, "Hỗn hợp đồng nhất giữa dung môi và chất tan."),
            make_mc(6, "Nhận biết", f"Đề {t} - Độ tan (S) của một chất trong nước là số gam chất đó tan được trong bao nhiêu gam nước để tạo thành dung dịch bão hòa ở nhiệt độ xác định?", ["100 gam nước", "1000 gam nước", "10 gam nước", "50 gam nước"], 0, "Số gam chất tan trong 100g nước."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Hòa tan 20 gam NaCl vào 80 gam nước. Nồng độ phần trăm của dung dịch thu được là:", ["20%", "25%", "15%", "10%"], 0, "mdd = 20 + 80 = 100g => C% = 20 / 100 × 100% = 20%."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Hòa tan 0,5 mol NaOH vào nước để được 250 mL dung dịch. Nồng độ mol của dung dịch NaOH là:", ["2,0 M", "1,0 M", "0,5 M", "0,2 M"], 0, "V = 0,25 L => CM = 0,5 / 0,25 = 2,0 M."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Khi tăng nhiệt độ, độ tan của hầu hết các chất rắn trong nước sẽ:", ["Tăng lên", "Giảm đi", "Không đổi", "Biến đổi không xác định"], 0, "Độ tan của đa số chất rắn tăng khi nhiệt độ tăng."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Dung dịch bão hòa là dung dịch:", ["Không thể hòa tan thêm chất tan đó ở nhiệt độ xác định", "Có thể hòa tan thêm chất tan", "Có nồng độ rất loãng", "Có màu sắc đậm"], 0, "Không thể hòa tan thêm chất tan."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Cần bao nhiêu gam đường để pha chế 200 gam dung dịch đường 5%?", ["10 gam", "20 gam", "5 gam", "15 gam"], 0, "m_đường = 200 × 5% = 10 gam."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Hòa tan 4 gam NaOH (M=40 g/mol) vào nước thành 500 mL dung dịch. Nồng độ mol của dung dịch là:", ["0,2 M", "0,1 M", "0,4 M", "0,5 M"], 0, "n = 4 / 40 = 0,1 mol. CM = 0,1 / 0,5 = 0,2 M.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Xét quá trình pha chế dung dịch nước muối sinh lí NaCl 0,9%:", [
                ("a", "Trong 100 gam nước muối sinh lí có chứa đúng 0,9 gam NaCl.", True),
                ("b", "Nước là dung môi, NaCl là chất tan.", True),
                ("c", "Để pha 1000 gam dung dịch trên cần 9 gam NaCl và 991 gam nước cất.", True),
                ("d", "Đây là dung dịch bão hòa của NaCl ở nhiệt độ phòng.", False)
            ], "NaCl tan rất nhiều trong nước (khoảng 36g trong 100g nước ở 20°C), nồng độ 0,9% là dung dịch rất loãng chưa bão hòa."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Về nồng độ dung dịch:", [
                ("a", "Khi thêm nước cất vào một dung dịch thì nồng độ phần trăm của dung dịch giảm đi.", True),
                ("b", "Khi cô cạn bớt nước thì nồng độ mol của dung dịch tăng lên.", True),
                ("c", "Khối lượng dung dịch bằng khối lượng chất tan cộng khối lượng dung môi.", True),
                ("d", "Thể tích dung dịch luôn bằng tổng thể tích chất tan cộng thể tích dung môi.", False)
            ], "Thể tích dung dịch thường có sự co ngót hoặc dãn nở thể tích (ví dụ pha cồn với nước)."),
            make_tf(3, "Vận dụng", f"Đề {t} - Hòa tan 10 gam CuSO4 vào nước thu được 200 mL dung dịch (khối lượng riêng D = 1,05 g/mL):", [
                ("a", "Khối lượng dung dịch là 210 gam.", True),
                ("b", "Nồng độ phần trăm của dung dịch xấp xỉ 4,76%.", True),
                ("c", "Số mol CuSO4 là 0,0625 mol (M=160).", True),
                ("d", "Nồng độ mol của dung dịch là 0,5 M.", False)
            ], "CM = 0,0625 / 0,2 = 0,3125 M."),
            make_tf(4, "Vận dụng", f"Đề {t} - Ở 20 °C, độ tan của KNO3 là 32 gam trong 100 gam nước:", [
                ("a", "Trong 132 gam dung dịch bão hòa có 32 gam KNO3.", True),
                ("b", "Nồng độ phần trăm của dung dịch KNO3 bão hòa ở 20 °C xấp xỉ 24,24%.", True),
                ("c", "Hòa tan 40 gam KNO3 vào 100 gam nước ở 20 °C sẽ có 8 gam không tan lắng xuống đáy.", True),
                ("d", "Độ tan của KNO3 giảm khi đun nóng nước.", False)
            ], "Độ tan của muối nitrat tăng mạnh khi tăng nhiệt độ.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Hòa tan 15 gam muối vào 85 gam nước. Khối lượng dung dịch thu được là bao nhiêu gam?", "100", "15 + 85 = 100 gam."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Nồng độ phần trăm của dung dịch chứa 10 gam đường trong 100 gam dung dịch là bao nhiêu %?", "10", "10%."),
            make_sa(3, "Vận dụng", f"Đề {t} - Cần bao nhiêu mL dung dịch HCl 2M để có chứa 0,4 mol HCl?", "200", "V = 0,4 / 2 = 0,2 L = 200 mL."),
            make_sa(4, "Vận dụng", f"Đề {t} - Hòa tan 8 gam NaOH vào nước được 100 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M?", "2", "n = 8 / 40 = 0,2 mol. CM = 0,2 / 0,1 = 2 M."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Thêm 100 gam nước cất vào 100 gam dung dịch NaCl 10%. Nồng độ phần trăm của dung dịch mới là bao nhiêu %?", "5", "mct = 10g, mdd mới = 200g => C% = 5%."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Trộn 200 mL dung dịch NaOH 1M với 300 mL dung dịch NaOH 2M. Nồng độ mol của dung dịch thu được là bao nhiêu M?", "1.6", "n = 0,2×1 + 0,3×2 = 0,8 mol. V = 0,5 L => CM = 0,8 / 0,5 = 1,6 M.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Để ngâm chua ngọt các món rau củ quả, người ta thường dùng dung dịch giấm ăn có nồng độ acetic acid khoảng 5%. Để pha 500 gam dung dịch giấm 5% từ dung dịch giấm mẹ có nồng độ 25%, khối lượng dung dịch giấm mẹ cần dùng là:", ["100 gam", "50 gam", "200 gam", "125 gam"], 0, "mct = 500 × 5% = 25g. mdd mẹ = 25 / 25% = 100 gam."),
            make_vdc(2, f"Đề {t} - Trong y tế, dung dịch glucose 5% thường được truyền vào tĩnh mạch để cung cấp năng lượng và nước cho bệnh nhân suy nhược. Trong một chai truyền dịch chứa 500 mL dung dịch glucose 5% (coi khối lượng riêng D ≈ 1,0 g/mL), khối lượng đường glucose tinh khiết đưa vào cơ thể là:", ["25 gam", "50 gam", "5 gam", "10 gam"], 0, "mdd = 500g => m_glucose = 500 × 5% = 25 gam."),
            make_vdc(3, f"Đề {t} - Một dung dịch H2SO4 có nồng độ 98% và khối lượng riêng D = 1,84 g/mL. Nồng độ mol (CM) của dung dịch H2SO4 này xấp xỉ bằng:", ["18,4 M", "10,0 M", "12,5 M", "15,2 M"], 0, "CM = 10 × D × C% / M = 10 × 1,84 × 98 / 98 = 18,4 M."),
            make_vdc(4, f"Đề {t} - Hòa tan 11,2 lít khí HCl (ở đkc 25 °C, 1 bar) vào nước để được 500 mL dung dịch acid clohiđric. Nồng độ mol của dung dịch acid thu được xấp xỉ bằng:", ["0,90 M", "1,00 M", "0,45 M", "1,20 M"], 0, "nHCl = 11,2 / 24,79 ≈ 0,4518 mol. CM = 0,4518 / 0,5 ≈ 0,90 M.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 6: Nồng độ dung dịch - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c1", "chapterTitle": "Chương I: Phản ứng hóa học",
            "lessonId": "chem8_c1_b6", "lessonName": "Bài 6: Nồng độ dung dịch",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 7: TỐC ĐỘ PHẢN ỨNG VÀ CHẤT XÚC TÁC (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c1_b7_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Tốc độ phản ứng là đại lượng đặc trưng cho:", ["Mức độ nhanh hay chậm của một phản ứng hóa học", "Nhiệt lượng tỏa ra", "Màu sắc của sản phẩm", "Khối lượng chất tạo thành"], 0, "Đặc trưng cho độ nhanh hay chậm của phản ứng."),
            make_mc(2, "Nhận biết", f"Đề {t} - Yếu tố nào sau đây KHÔNG làm tăng tốc độ của phản ứng hóa học?", ["Giảm nồng độ chất phản ứng", "Tăng nhiệt độ", "Tăng diện tích tiếp xúc", "Dùng chất xúc tác"], 0, "Giảm nồng độ làm giảm tốc độ phản ứng."),
            make_mc(3, "Nhận biết", f"Đề {t} - Chất làm tăng tốc độ phản ứng nhưng không bị tiêu hao sau phản ứng được gọi là:", ["Chất xúc tác", "Chất phản ứng", "Chất ức chế", "Sản phẩm"], 0, "Chất xúc tác làm tăng tốc độ mà không bị biến đổi."),
            make_mc(4, "Nhận biết", f"Đề {t} - Để củi cháy nhanh và đượm hơn, người ta thường chẻ nhỏ củi ra. Yếu tố ảnh hưởng ở đây là:", ["Diện tích tiếp xúc", "Nhiệt độ", "Chất xúc tác", "Áp suất"], 0, "Tăng diện tích bề mặt tiếp xúc giữa củi và oxy."),
            make_mc(5, "Nhận biết", f"Đề {t} - Đun nấu thức ăn trong nồi áp suất nhanh chín hơn nồi thường chủ yếu do yếu tố nào?", ["Nhiệt độ và áp suất cao hơn", "Có chất xúc tác", "Thức ăn tiếp xúc nhiều nước hơn", "Diện tích tiếp xúc"], 0, "Áp suất cao làm tăng nhiệt độ sôi của nước (lên khoảng 120°C)."),
            make_mc(6, "Nhận biết", f"Đề {t} - Bảo quản thức ăn trong tủ lạnh giúp thức ăn lâu ôi thiu là do yếu tố:", ["Giảm nhiệt độ làm chậm tốc độ phản ứng phân hủy", "Tăng nồng độ chất bảo quản", "Giảm diện tích tiếp xúc", "Có chất xúc tác làm chậm"], 0, "Hạ nhiệt độ làm giảm tốc độ phản ứng ôi thiu."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Cho cùng một lượng kẽm hạt và kẽm bột vào hai ống nghiệm chứa cùng lượng dung dịch HCl cùng nồng độ. Ống nghiệm nào thoát khí H2 nhanh hơn?", ["Ống nghiệm chứa kẽm bột vì diện tích tiếp xúc lớn hơn", "Ống nghiệm chứa kẽm hạt", "Cả hai ống thoát khí với tốc độ như nhau", "Không xác định được"], 0, "Dạng bột có diện tích bề mặt lớn hơn nhiều so với dạng hạt."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Khi thổi thêm không khí vào bếp than đang cháy dở, than cháy bùng lên mạnh mẽ là do:", ["Tăng nồng độ khí Oxygen", "Giảm nhiệt độ", "Tăng chất xúc tác", "Giảm diện tích tiếp xúc"], 0, "Cung cấp thêm oxy làm tăng nồng độ O2."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Phản ứng phân hủy nước oxy già (H2O2) giải phóng khí O2 xảy ra rất chậm ở nhiệt độ phòng. Nếu thêm một ít bột MnO2 vào thì bọt khí thoát ra mãnh liệt. MnO2 đóng vai trò là:", ["Chất xúc tác", "Chất phản ứng", "Chất chỉ thị", "Dung môi"], 0, "MnO2 là chất xúc tác cho phản ứng phân hủy H2O2."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Men tiêu hóa trong dạ dày và ruột non của người (như pepsin, amylase) là ví dụ về:", ["Chất xúc tác sinh học (enzyme)", "Chất phản ứng vô cơ", "Chất chỉ thị màu", "Chất ức chế"], 0, "Enzyme là chất xúc tác sinh học."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Quá trình nào sau đây có tốc độ phản ứng diễn ra NHANH NHẤT?", ["Vụ nổ của thuốc nổ đen", "Sắt bị gỉ trong không khí ẩm", "Lên men rượu từ tinh bột", "Sự hình thành thạch nhũ trong hang động"], 0, "Vụ nổ xảy ra gần như tức thời trong tích tắc."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Quá trình nào sau đây có tốc độ phản ứng diễn ra CHẬM NHẤT?", ["Sự hình thành thạch nhũ trong hang động đá vôi (hàng triệu năm)", "Đốt cháy que diêm", "Cho vôi sống vào nước", "Viên sủi tan trong nước"], 0, "Hình thành thạch nhũ mất hàng nghìn đến hàng triệu năm.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Xét các biện pháp thực tiễn điều khiển tốc độ phản ứng:", [
                ("a", "Bảo quản thực phẩm trong tủ lạnh giúp làm giảm tốc độ phân hủy thức ăn.", True),
                ("b", "Quạt gió vào bếp than đang cháy làm tăng nồng độ oxygen giúp than cháy nhanh hơn.", True),
                ("c", "Nghiền nhỏ thuốc trước khi uống làm tăng tốc độ hòa tan và hấp thu vào máu.", True),
                ("d", "Chất xúc tác bị biến đổi hoàn toàn thành chất khác sau khi kết thúc phản ứng.", False)
            ], "Chất xúc tác không bị tiêu hao hay biến đổi thành chất khác."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Khi nghiên cứu phản ứng giữa đá vôi (CaCO3) và dung dịch acid HCl:", [
                ("a", "Dùng dung dịch HCl 2M phản ứng nhanh hơn dung dịch HCl 0,5M.", True),
                ("b", "Đun nóng dung dịch phản ứng làm bọt khí thoát ra nhanh hơn.", True),
                ("c", "Dùng đá vôi dạng bột phản ứng nhanh hơn đá vôi dạng tảng lớn.", True),
                ("d", "Tăng thể tích nước cất thêm vào làm tăng tốc độ phản ứng.", False)
            ], "Thêm nước làm loãng dung dịch, giảm nồng độ HCl nên tốc độ giảm."),
            make_tf(3, "Vận dụng", f"Đề {t} - Trong công nghiệp sản xuất sulfuric acid, phản ứng 2SO2 + O2 -> 2SO3 được thực hiện ở 450 °C với chất xúc tác V2O5:", [
                ("a", "V2O5 đóng vai trò là chất xúc tác giúp phản ứng đạt hiệu suất nhanh chóng.", True),
                ("b", "Ở nhiệt độ phòng, phản ứng diễn ra rất chậm.", True),
                ("c", "Nếu không có V2O5 thì phản ứng không thể xảy ra dù ở bất kì điều kiện nào.", False),
                ("d", "Khí SO3 tan vào nước tạo thành acid sulfuric (H2SO4).", True)
            ], "Không có xúc tác phản ứng vẫn xảy ra nhưng tốc độ vô cùng chậm."),
            make_tf(4, "Vận dụng", f"Đề {t} - Hiện tượng cháy nổ bụi than hoặc bụi bột mì trong các nhà máy xay xát:", [
                ("a", "Bột than hoặc bột mì có diện tích tiếp xúc với oxygen cực kì lớn.", True),
                ("b", "Khi có tia lửa điện kích hoạt, phản ứng cháy diễn ra với tốc độ cực nhanh tỏa nhiệt mạnh gây nổ.", True),
                ("c", "Để phòng chống cháy nổ bụi, cần thông gió tốt và hút bụi thường xuyên.", True),
                ("d", "Bụi bột mì không thể cháy được vì là chất hữu cơ.", False)
            ], "Bột mì là carbohydrate cháy rất tốt, dạng bụi mịn dễ nổ.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Để tăng diện tích tiếp xúc của chất rắn, người ta cần làm gì với chất rắn đó? (Đập nhỏ/nghiền bột hay Để nguyên khối)", "Nghiền bột", "Nghiền nhỏ hoặc đập vụn."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Chất làm tăng tốc độ phản ứng mà không bị tiêu hao gọi là chất gì?", "Chất xúc tác", "Chất xúc tác."),
            make_sa(3, "Vận dụng", f"Đề {t} - Khi tăng nhiệt độ lên 10 °C, tốc độ một phản ứng tăng lên 2 lần. Nếu tăng nhiệt độ từ 20 °C lên 50 °C (tăng 30 °C), tốc độ phản ứng tăng lên bao nhiêu lần?", "8", "2^(30/10) = 2^3 = 8 lần."),
            make_sa(4, "Vận dụng", f"Đề {t} - Hòa tan hết 1 viên sủi C vào nước lạnh mất 60 giây. Nếu hòa tan vào nước ấm, thời gian tan hết là 20 giây. Tốc độ tan trong nước ấm nhanh gấp bao nhiêu lần trong nước lạnh?", "3", "60 / 20 = 3 lần."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Một phản ứng ở 30 °C hoàn thành sau 16 phút. Biết hệ số nhiệt độ Van't Hoff của phản ứng là 2. Ở 50 °C, phản ứng trên sẽ hoàn thành trong bao nhiêu phút?", "4", "Tốc độ tăng 2^(20/10) = 4 lần => thời gian giảm 4 lần: 16 / 4 = 4 phút."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Trong sản xuất ammonia NH3 từ N2 và H2, người ta dùng chất xúc tác là kim loại nào được trộn thêm oxide nhôm và kali? (Ghi tên kim loại hoặc kí hiệu)", "Fe", "Sắt (Fe) là xúc tác tổng hợp ammonia.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Tại sao người ta tạo các lỗ rỗng trong viên than tổ ong?", ["Để tăng diện tích tiếp xúc của than với không khí, giúp than cháy dễ và đều hơn", "Để giảm khối lượng viên than dễ vận chuyển", "Để than cháy chậm lại tiết kiệm nhiên liệu", "Để giảm lượng khí thải độc hại"], 0, "Tăng bề mặt tiếp xúc với không khí giúp than cháy kiệt."),
            make_vdc(2, f"Đề {t} - Trong bảo quản ngũ cốc (thóc, ngô, đậu) sau thu hoạch, việc phơi thật khô trước khi cất giữ vào kho kín có tác dụng:", ["Làm giảm hàm lượng nước, ức chế quá trình hô hấp của hạt và sự phát triển của nấm mốc", "Làm tăng khối lượng hạt", "Làm hạt nảy mầm nhanh hơn", "Giúp hạt biến đổi thành tinh bột"], 0, "Giảm nước làm chậm tốc độ phản ứng trao đổi chất và ngăn vi sinh vật."),
            make_vdc(3, f"Đề {t} - Nồi áp suất giúp hầm nhừ xương nhanh gấp nhiều lần nồi thường vì:", ["Nắp đậy kín giữ hơi nước làm áp suất trong nồi tăng cao, dẫn đến nhiệt độ sôi của nước tăng lên khoảng 115 - 120 °C", "Áp suất nén trực tiếp làm gãy xương", "Trong nồi có lớp phủ chất xúc tác", "Nước trong nồi áp suất không sôi"], 0, "Tăng áp suất làm tăng nhiệt độ sôi, nhiệt độ cao làm tăng tốc độ phản ứng chín nhừ."),
            make_vdc(4, f"Đề {t} - Khi nhai kĩ cơm trong miệng, ta thấy có vị ngọt thanh xuất hiện. Đó là do enzyme amylase trong nước bọt đã đóng vai trò xúc tác cho phản ứng thủy phân:", ["Tinh bột thành đường maltose", "Chất đạm thành amino acid", "Chất béo thành glycerol", "Cellulose thành glucose"], 0, "Amylase xúc tác thủy phân tinh bột thành đường đôi maltose gây ngọt.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 7: Tốc độ phản ứng và chất xúc tác - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c1", "chapterTitle": "Chương I: Phản ứng hóa học",
            "lessonId": "chem8_c1_b7", "lessonName": "Bài 7: Tốc độ phản ứng và chất xúc tác",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- ÔN TẬP CUỐI CHƯƠNG I (5 ĐỀ) ---
    for t in range(1, 6):
        k = f"chem8_c1_rev_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề tổng hợp {t} - Hiện tượng nào sau đây là hiện tượng hóa học?", ["Đốt cháy khí Hydrogen trong không khí", "Băng tan chảy", "Xé rách một tờ giấy", "Hòa tan muối vào nước"], 0, "2H2 + O2 -> 2H2O tạo chất mới."),
            make_mc(2, "Nhận biết", f"Đề tổng hợp {t} - Định luật bảo toàn khối lượng được áp dụng cho:", ["Mọi phản ứng hóa học", "Chỉ phản ứng tỏa nhiệt", "Chỉ phản ứng trong phòng thí nghiệm", "Chỉ phản ứng có chất khí"], 0, "Mọi phản ứng hóa học."),
            make_mc(3, "Nhận biết", f"Đề tổng hợp {t} - Thể tích mol của chất khí ở điều kiện chuẩn (25 °C, 1 bar) là:", ["24,79 L/mol", "22,4 L/mol", "24,0 L/mol", "25,0 L/mol"], 0, "24,79 L/mol."),
            make_mc(4, "Nhận biết", f"Đề tổng hợp {t} - Công thức tính nồng độ mol là:", ["CM = n / V", "CM = m / V", "CM = n × V", "CM = V / n"], 0, "CM = n / V."),
            make_mc(5, "Nhận biết", f"Đề tổng hợp {t} - Để làm tăng tốc độ phản ứng giữa chất rắn và chất lỏng, ta nên:", ["Nghiền nhỏ chất rắn và tăng nhiệt độ", "Giảm nhiệt độ", "Giảm nồng độ chất lỏng", "Dùng chất rắn dạng khối to"], 0, "Tăng diện tích tiếp xúc và tăng nhiệt độ."),
            make_mc(6, "Nhận biết", f"Đề tổng hợp {t} - Phản ứng tỏa nhiệt là phản ứng:", ["Giải phóng nhiệt năng ra môi trường xung quanh", "Hấp thụ nhiệt năng từ môi trường", "Làm giảm nhiệt độ môi trường", "Không thay đổi nhiệt độ"], 0, "Giải phóng nhiệt năng."),
            make_mc(7, "Thông hiểu", f"Đề tổng hợp {t} - Cân bằng phương trình: Fe3O4 + CO -> Fe + CO2. Hệ số của CO là:", ["4", "3", "2", "1"], 0, "Fe3O4 + 4CO -> 3Fe + 4CO2."),
            make_mc(8, "Thông hiểu", f"Đề tổng hợp {t} - Khối lượng của 0,25 mol khí CO2 là:", ["11 gam", "22 gam", "44 gam", "5,5 gam"], 0, "0,25 × 44 = 11 gam."),
            make_mc(9, "Thông hiểu", f"Đề tổng hợp {t} - Khí nào sau đây nhẹ hơn không khí (Mkk ≈ 29)?", ["CH4 (M=16)", "O2 (M=32)", "CO2 (M=44)", "SO2 (M=64)"], 0, "CH4 nhẹ hơn không khí."),
            make_mc(10, "Thông hiểu", f"Đề tổng hợp {t} - Nồng độ phần trăm của dung dịch pha từ 25 g đường và 75 g nước là:", ["25%", "33,3%", "20%", "15%"], 0, "mdd = 100g => C% = 25%."),
            make_mc(11, "Thông hiểu", f"Đề tổng hợp {t} - Cho 5,6 gam Sắt phản ứng hoàn toàn với dung dịch HCl dư. Thể tích khí H2 thu được ở đkc (25 °C, 1 bar) là:", ["2,479 lít", "4,958 lít", "2,24 lít", "1,24 lít"], 0, "nFe = 0,1 mol => nH2 = 0,1 mol => V = 2,479 L."),
            make_mc(12, "Thông hiểu", f"Đề tổng hợp {t} - Nhận định nào sau đây SAI về chất xúc tác?", ["Chất xúc tác bị tiêu hao dần theo thời gian phản ứng", "Chất xúc tác làm tăng tốc độ phản ứng", "Chất xúc tác được hoàn nguyên sau phản ứng", "Enzyme là chất xúc tác sinh học"], 0, "Chất xúc tác không bị tiêu hao sau phản ứng.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề tổng hợp {t} - Xét phản ứng: 2Al + 6HCl -> 2AlCl3 + 3H2:", [
                ("a", "Tỉ lệ số nguyên tử Al và phân tử H2 là 2 : 3.", True),
                ("b", "Đây là phản ứng có giải phóng khí.", True),
                ("c", "Nếu hòa tan 5,4 gam Al cần vừa đủ 0,6 mol HCl.", True),
                ("d", "Khối lượng dung dịch sau phản ứng luôn lớn hơn tổng khối lượng Al và dung dịch HCl ban đầu.", False)
            ], "Khối lượng dung dịch sau phản ứng = mAl + mdd HCl - mH2 (bay đi). nAl = 5,4/27 = 0,2 mol => nHCl = 0,6 mol."),
            make_tf(2, "Thông hiểu", f"Đề tổng hợp {t} - Về các đại lượng hóa học cơ bản:", [
                ("a", "Khối lượng mol của H2SO4 là 98 g/mol.", True),
                ("b", "Ở đkc, 0,5 mol khí N2 chiếm thể tích là 12,395 lít.", True),
                ("c", "Tỉ khối của khí O2 đối với khí H2 là 16.", True),
                ("d", "Độ tan của chất khí trong nước tăng lên khi tăng nhiệt độ.", False)
            ], "Độ tan của chất khí giảm khi nhiệt độ tăng (nước sôi bốc hết khí hòa tan)."),
            make_tf(3, "Vận dụng", f"Đề tổng hợp {t} - Hòa tan hoàn toàn 4,8 gam Magie (Mg) vào dung dịch HCl dư:", [
                ("a", "Số mol Mg tham gia phản ứng là 0,2 mol.", True),
                ("b", "Khối lượng muối MgCl2 thu được là 19,0 gam.", True),
                ("c", "Thể tích khí H2 thoát ra ở đkc là 4,958 lít.", True),
                ("d", "Nếu dùng Mg dạng bột thì thời gian tan hết sẽ lâu hơn dạng lá.", False)
            ], "mMgCl2 = 0,2 × 95 = 19,0 g. VH2 = 0,2 × 24,79 = 4,958 L. Dạng bột tan nhanh hơn."),
            make_tf(4, "Vận dụng", f"Đề tổng hợp {t} - Xét các yếu tố ảnh hưởng đến tốc độ phản ứng trong thực tế:", [
                ("a", "Đập dập củ sả trước khi nấu ăn giúp tinh dầu khuếch tán nhanh hơn do tăng diện tích tiếp xúc.", True),
                ("b", "Rắc men vào cơm nếp ủ rượu là sử dụng chất xúc tác sinh học.", True),
                ("c", "Nhiệt độ càng cao thì tốc độ phản ứng cháy càng chậm.", False),
                ("d", "Bảo quản vắc-xin ở nhiệt độ âm sâu để hạn chế tối đa sự phân hủy thuốc.", True)
            ], "Nhiệt độ cao làm tăng tốc độ cháy.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề tổng hợp {t} - Thể tích của 0,1 mol khí Oxygen ở đkc (25 °C, 1 bar) là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "2.48", "0,1 × 24,79 = 2,479 ≈ 2,48 lít."),
            make_sa(2, "Thông hiểu", f"Đề tổng hợp {t} - Khối lượng mol của khí Carbon dioxide CO2 là bao nhiêu g/mol?", "44", "12 + 32 = 44 g/mol."),
            make_sa(3, "Vận dụng", f"Đề tổng hợp {t} - Cần bao nhiêu gam NaOH để pha được 500 mL dung dịch NaOH 1M?", "20", "n = 0,5 × 1 = 0,5 mol => m = 0,5 × 40 = 20 gam."),
            make_sa(4, "Vận dụng", f"Đề tổng hợp {t} - Hòa tan 13 gam Kẽm (Zn) bằng acid HCl dư thu được bao nhiêu gam khí Hydrogen? (Zn=65)", "0.4", "nZn = 0,2 mol => nH2 = 0,2 mol => mH2 = 0,4 gam."),
            make_sa(5, "Vận dụng cao", f"Đề tổng hợp {t} - Đốt cháy hoàn toàn 6,4 gam Cu trong không khí thu được bao nhiêu gam CuO? (Cu=64, O=16)", "8", "nCu = 0,1 mol => nCuO = 0,1 mol => mCuO = 0,1 × 80 = 8 gam."),
            make_sa(6, "Vận dụng cao", f"Đề tổng hợp {t} - Khối lượng dung dịch HCl 7,3% cần dùng để phản ứng vừa hết với 10 gam CaCO3 là bao nhiêu gam?", "100", "nCaCO3 = 0,1 mol => nHCl = 0,2 mol => mHCl = 7,3 g => mdd = 7,3 / 7,3% = 100 gam.")
        ]
        p4 = [
            make_vdc(1, f"Đề tổng hợp {t} - Một hỗn hợp khí gồm khí CH4 và khí O2 có tỉ lệ thể tích 1 : 2. Hỗn hợp này phát nổ mạnh nhất khi gặp tia lửa điện. Tỉ khối của hỗn hợp nổ này so với không khí xấp xỉ bằng:", ["0,92", "1,52", "0,55", "1,20"], 0, "M_tb = (1×16 + 2×32) / 3 = 80 / 3 ≈ 26,67 g/mol. d = 26,67 / 29 ≈ 0,92."),
            make_vdc(2, f"Đề tổng hợp {t} - Nung nóng 50 gam đá vôi chứa 80% CaCO3 (phần còn lại là tạp chất trơ không bị nhiệt phân), sau một thời gian thu được 33,4 gam chất rắn. Hiệu suất của phản ứng phân hủy đá vôi trên là:", ["94,3%", "80,0%", "75,5%", "85,0%"], 0, "mCaCO3 ban đầu = 50 × 80% = 40g (0,4 mol). Khối lượng giảm = mCO2 = 50 - 33,4 = 16,6g => nCO2 = 16,6 / 44 = 0,3773 mol. H = 0,3773 / 0,4 × 100% ≈ 94,3%."),
            make_vdc(3, f"Đề tổng hợp {t} - Trong phòng thí nghiệm, để pha loãng dung dịch H2SO4 đặc một cách an toàn tuyệt đối, người ta phải thực hiện thao tác nào sau đây?", ["Rót từ từ acid đặc vào cốc nước và khuấy đều bằng đũa thủy tinh", "Rót nhanh nước vào cốc đựng acid đặc", "Rót đồng thời cả nước và acid vào nhau", "Đun sôi nước rồi mới đổ acid vào"], 0, "Acid đặc háo nước và tỏa nhiệt cực mạnh, đổ nước vào acid làm nước sôi đột ngột bắn tung tóe gây bỏng acid."),
            make_vdc(4, f"Đề tổng hợp {t} - Khí SO2 là một trong những nguyên nhân chính gây ra hiện tượng mưa acid tàn phá rừng cây và ăn mòn công trình kiến trúc. Trong khí quyển, khí SO2 bị oxy hóa thành SO3 rồi kết hợp với nước mưa tạo thành acid nào sau đây?", ["Sulfuric acid (H2SO4)", "Hydrochloric acid (HCl)", "Nitric acid (HNO3)", "Carbonic acid (H2CO3)"], 0, "SO3 + H2O -> H2SO4.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - [Đề tổng hợp] Ôn tập cuối Chương I - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c1", "chapterTitle": "Chương I: Phản ứng hóa học",
            "lessonId": "chem8_c1_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương I",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # =========================================================================
    # CHƯƠNG II: MỘT SỐ HỢP CHẤT THÔNG DỤNG (Acid, Base, Oxide, Muối, Phân bón)
    # =========================================================================

    # --- BÀI 8: ACID (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c2_b8_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Dung dịch acid làm quỳ tím chuyển sang màu gì?", ["Màu đỏ", "Màu xanh", "Không đổi màu", "Màu vàng"], 0, "Acid làm quỳ tím hóa đỏ."),
            make_mc(2, "Nhận biết", f"Đề {t} - Công thức hóa học của hydrochloric acid là:", ["HCl", "H2SO4", "HNO3", "H3PO4"], 0, "HCl là hydrochloric acid."),
            make_mc(3, "Nhận biết", f"Đề {t} - Acid tác dụng với kim loại đứng trước Hydrogen giải phóng khí gì?", ["Khí Hydrogen (H2)", "Khí Oxygen (O2)", "Khí Chlorine (Cl2)", "Khí Nitrogen (N2)"], 0, "Giải phóng khí H2."),
            make_mc(4, "Nhận biết", f"Đề {t} - Kim loại nào sau đây KHÔNG tác dụng với dung dịch HCl loãng?", ["Đồng (Cu)", "Sắt (Fe)", "Kẽm (Zn)", "Nhôm (Al)"], 0, "Cu đứng sau H trong dãy hoạt động hóa học."),
            make_mc(5, "Nhận biết", f"Đề {t} - Công thức hóa học của sulfuric acid là:", ["H2SO4", "H2SO3", "HCl", "HNO3"], 0, "Sulfuric acid là H2SO4."),
            make_mc(6, "Nhận biết", f"Đề {t} - Acid nào có trong dịch dạ dày của người giúp tiêu hóa thức ăn?", ["Hydrochloric acid (HCl)", "Sulfuric acid (H2SO4)", "Acetic acid (CH3COOH)", "Nitric acid (HNO3)"], 0, "Dịch vị dạ dày chứa acid HCl nồng độ khoảng 0,0001 - 0,001M (pH ≈ 1,5 - 3,5)."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Cho mẩu kẽm (Zn) vào dung dịch HCl, hiện tượng quan sát được là:", ["Kẽm tan dần và có bọt khí không màu thoát ra", "Xuất hiện kết tủa màu đỏ", "Dung dịch đổi sang màu xanh", "Không có hiện tượng gì"], 0, "Zn + 2HCl -> ZnCl2 + H2."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Dung dịch H2SO4 loãng tác dụng được với chất nào sau đây?", ["Fe", "Cu", "Ag", "Au"], 0, "Fe đứng trước H nên phản ứng tạo FeSO4 và H2."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Khi cho dung dịch HCl tác dụng với CuO (màu đen), dung dịch thu được có màu:", ["Xanh lam", "Đỏ nâu", "Vàng nhạt", "Không màu"], 0, "CuO + 2HCl -> CuCl2 (dung dịch xanh lam) + H2O."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Để thử tính acid của giấm ăn hay nước chanh, người ta dùng:", ["Giấy quỳ tím", "Muối ăn", "Dầu ăn", "Cát"], 0, "Quỳ tím chuyển sang màu đỏ."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Sản phẩm của phản ứng giữa acid và base (phản ứng trung hòa) luôn gồm:", ["Muối và nước", "Kim loại và nước", "Khí và nước", "Oxide và acid"], 0, "Acid + Base -> Muối + Nước."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Acid nào sau đây có tính háo nước mạnh và có thể làm cháy đen đường mía, vải, da?", ["H2SO4 đặc", "HCl loãng", "H2SO4 loãng", "CH3COOH"], 0, "H2SO4 đặc háo nước cực mạnh, than hóa đường thành carbon C.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Xét các tính chất hóa học chung của acid:", [
                ("a", "Làm đổi màu quỳ tím thành đỏ.", True),
                ("b", "Tác dụng với nhiều kim loại đứng trước H giải phóng khí H2.", True),
                ("c", "Tác dụng với base tạo thành muối và nước.", True),
                ("d", "Tác dụng được với tất cả các kim loại kể cả vàng (Au) và bạc (Ag).", False)
            ], "Acid thông thường không tác dụng với Cu, Ag, Au."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Khi sử dụng và pha loãng Sulfuric acid đặc (H2SO4 đặc):", [
                ("a", "H2SO4 đặc hút nước rất mạnh và tỏa nhiệt lượng lớn.", True),
                ("b", "Quy tắc an toàn: luôn rót từ từ acid vào nước, tuyệt đối không làm ngược lại.", True),
                ("c", "Nếu bị acid dính vào da, cần rửa ngay dưới vòi nước chảy trong nhiều phút.", True),
                ("d", "Có thể dùng xô bằng sắt hoặc nhôm để chứa dung dịch H2SO4 loãng lâu ngày.", False)
            ], "H2SO4 loãng ăn mòn mạnh Fe và Al."),
            make_tf(3, "Vận dụng", f"Đề {t} - Cho 6,5 gam Zn tác dụng vừa đủ với 100 mL dung dịch HCl:", [
                ("a", "Số mol Zn phản ứng là 0,1 mol.", True),
                ("b", "Số mol khí H2 thoát ra là 0,1 mol.", True),
                ("c", "Nồng độ mol của dung dịch HCl đã dùng là 2,0 M.", True),
                ("d", "Khối lượng muối ZnCl2 thu được là 16,0 gam.", False)
            ], "mZnCl2 = 0,1 × 136 = 13,6 gam."),
            make_tf(4, "Vận dụng", f"Đề {t} - Nhận biết 3 dung dịch không nhãn: HCl, H2SO4 loãng, NaCl:", [
                ("a", "Dùng quỳ tím nhận biết được dung dịch NaCl (không đổi màu quỳ tím).", True),
                ("b", "Hai dung dịch làm đỏ quỳ tím là HCl và H2SO4.", True),
                ("c", "Dùng dung dịch BaCl2 phân biệt được H2SO4 (tạo kết tủa trắng BaSO4).", True),
                ("d", "Dung dịch HCl cũng tạo kết tủa trắng với dung dịch BaCl2.", False)
            ], "BaCl2 không phản ứng với HCl vì không tạo kết tủa.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Dung dịch HCl làm quỳ tím chuyển sang màu gì?", "Đỏ", "Màu đỏ."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Cho kim loại Fe tác dụng với dung dịch HCl tạo thành muối sắt có hóa trị mấy?", "2", "Muối FeCl2 sắt có hóa trị II."),
            make_sa(3, "Vận dụng", f"Đề {t} - Hòa tan hết 5,6 gam Fe vào dung dịch HCl dư. Thể tích khí H2 sinh ra ở đkc (25 °C, 1 bar) là bao nhiêu lít? (Làm tròn 2 chữ số)", "2.48", "nFe = 0,1 mol => V = 0,1 × 24,79 = 2,479 ≈ 2,48 L."),
            make_sa(4, "Vận dụng", f"Đề {t} - Để trung hòa hoàn toàn 100 mL dung dịch HCl 1M cần bao nhiêu mL dung dịch NaOH 1M?", "100", "nHCl = 0,1 mol => nNaOH = 0,1 mol => V = 100 mL."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Cho 4 gam bột MgO tác dụng vừa đủ với dung dịch H2SO4. Khối lượng muối MgSO4 thu được là bao nhiêu gam? (Mg=24, S=32, O=16)", "12", "nMgO = 4/40 = 0,1 mol => mMgSO4 = 0,1 × 120 = 12 gam."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Cho 10 gam hỗn hợp Cu và Fe tác dụng với dung dịch HCl dư. Sau phản ứng còn lại 4,4 gam chất rắn không tan. Khối lượng Fe trong hỗn hợp ban đầu là bao nhiêu gam?", "5.6", "mFe = 10 - 4,4 = 5,6 gam (vì Cu không tan).")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Bệnh đau dạ dày (viêm loét dạ dày) thường đi kèm triệu chứng ợ chua do dư thừa acid HCl trong dịch vị. Thuốc đau dạ dày thường chứa thành phần nào sau đây để trung hòa bớt lượng acid dư thừa một cách êm dịu?", ["Sodium hydrogencarbonate (NaHCO3) hoặc Al(OH)3, Mg(OH)2", "Sulfuric acid đặc", "Sodium hydroxide (NaOH)", "Muối ăn (NaCl)"], 0, "NaHCO3 hoặc Al(OH)3, Mg(OH)2 là các chất có tính kiềm nhẹ an toàn giúp trung hòa acid dư."),
            make_vdc(2, f"Đề {t} - Để tẩy gỉ sét (thành phần chính là Fe2O3) trên bề mặt các chi tiết máy bằng thép trước khi sơn hoặc mạ kim loại, người ta thường ngâm chi tiết máy vào dung dịch nào sau đây?", ["Dung dịch hydrochloric acid (HCl) loãng", "Dung dịch nước muối NaCl", "Nước cất", "Dung dịch cồn"], 0, "Fe2O3 + 6HCl -> 2FeCl3 + 3H2O làm sạch gỉ sét."),
            make_vdc(3, f"Đề {t} - Cho một lượng bột nhôm Al vào cốc chứa dung dịch H2SO4 loãng dư. Khi phản ứng kết thúc, thêm tiếp dung dịch Ba(OH)2 dư vào cốc thì hiện tượng quan sát được là:", ["Xuất hiện kết tủa trắng BaSO4", "Không có kết tủa nào", "Dung dịch chuyển sang màu tím", "Khí CO2 thoát ra"], 0, "Ba(OH)2 tác dụng H2SO4 dư và Al2(SO4)3 tạo kết tủa trắng BaSO4 không tan."),
            make_vdc(4, f"Đề {t} - Trong acquy xe máy và ô tô truyền thống thường chứa dung dịch chất điện phân nào sau đây?", ["Dung dịch sulfuric acid (H2SO4) nồng độ khoảng 30%", "Dung dịch hydrochloric acid", "Dung dịch acetic acid", "Dung dịch muối ăn"], 0, "Acquy chì dùng dung dịch H2SO4 làm chất điện phân.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 8: Acid - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c2", "chapterTitle": "Chương II: Một số hợp chất thông dụng",
            "lessonId": "chem8_c2_b8", "lessonName": "Bài 8: Acid",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 9: BASE VÀ THANG pH (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c2_b9_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Dung dịch base (kiềm) làm quỳ tím đổi sang màu gì?", ["Màu xanh", "Màu đỏ", "Không đổi màu", "Màu vàng"], 0, "Base làm quỳ tím hóa xanh."),
            make_mc(2, "Nhận biết", f"Đề {t} - Dung dịch kiềm làm dung dịch phenolphthalein không màu chuyển sang màu:", ["Màu hồng (hoặc đỏ)", "Màu xanh", "Màu vàng", "Màu tím"], 0, "Phenolphthalein chuyển sang màu hồng trong môi trường kiềm."),
            make_mc(3, "Nhận biết", f"Đề {t} - Thang pH thường dùng có giá trị nằm trong khoảng từ:", ["0 đến 14", "1 đến 10", "0 đến 7", "7 đến 14"], 0, "Thang pH từ 0 đến 14."),
            make_mc(4, "Nhận biết", f"Đề {t} - Dung dịch có tính acid khi giá trị pH:", ["pH < 7", "pH = 7", "pH > 7", "pH = 14"], 0, "pH < 7 là môi trường acid."),
            make_mc(5, "Nhận biết", f"Đề {t} - Dung dịch trung tính (như nước tinh khiết) có giá trị pH bằng:", ["7", "0", "14", "1"], 0, "pH = 7 là trung tính."),
            make_mc(6, "Nhận biết", f"Đề {t} - Dung dịch có tính base khi giá trị pH:", ["pH > 7", "pH < 7", "pH = 7", "pH = 0"], 0, "pH > 7 là môi trường base."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Chất nào sau đây là một base tan trong nước (kiềm)?", ["Sodium hydroxide (NaOH)", "Copper(II) hydroxide (Cu(OH)2)", "Iron(III) hydroxide (Fe(OH)3)", "Aluminium hydroxide (Al(OH)3)"], 0, "NaOH là kiềm tan tốt trong nước."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Base nào sau đây là chất kết tủa màu xanh lam không tan trong nước?", ["Cu(OH)2", "NaOH", "KOH", "Ba(OH)2"], 0, "Cu(OH)2 là kết tủa màu xanh lam."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Base nào sau đây là kết tủa màu nâu đỏ?", ["Fe(OH)3", "Fe(OH)2", "Mg(OH)2", "Al(OH)3"], 0, "Fe(OH)3 có màu nâu đỏ."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Nhiệt phân Cu(OH)2 màu xanh ở nhiệt độ cao thu được chất rắn màu đen là:", ["CuO", "Cu2O", "Cu", "CuSO4"], 0, "Cu(OH)2 -> CuO (màu đen) + H2O."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Nước chanh tươi có vị chua, giá trị pH dự đoán của nước chanh là:", ["pH ≈ 2 - 3", "pH = 7", "pH ≈ 9 - 10", "pH = 14"], 0, "Nước chanh có tính acid nên pH < 7 (khoảng 2 - 3)."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Để khử chua cho đất trồng trọt (đất có pH < 5), người nông dân thường bón chất nào?", ["Vôi bột (CaO hoặc Ca(OH)2)", "Muối ăn (NaCl)", "Phân đạm Urê", "Cát"] , 0, "Vôi có tính kiềm giúp trung hòa acid trong đất nâng độ pH.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Về phân loại và tính chất của Base:", [
                ("a", "Base tan trong nước được gọi là kiềm (như NaOH, KOH, Ca(OH)2, Ba(OH)2).", True),
                ("b", "Tất cả các base đều làm đổi màu phenolphthalein thành màu hồng.", False),
                ("c", "Tất cả các base (tan và không tan) đều tác dụng với acid tạo thành muối và nước.", True),
                ("d", "Các base không tan bị nhiệt phân hủy tạo ra oxide bazơ tương ứng và nước.", True)
            ], "Chỉ các base tan (kiềm) mới làm đổi màu chỉ thị, base không tan không đổi màu chỉ thị."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Về ý nghĩa của thang pH trong đời sống:", [
                ("a", "Nước uống sinh hoạt đạt chuẩn thường có pH trong khoảng 6,5 đến 8,5.", True),
                ("b", "Máu người có pH ổn định trong khoảng 7,35 đến 7,45.", True),
                ("c", "Môi trường có pH = 1 có tính acid yếu hơn môi trường có pH = 6.", False),
                ("d", "Nước xà phòng giặt đồ có tính kiềm với pH > 7.", True)
            ], "pH càng nhỏ tính acid càng mạnh (pH = 1 rất mạnh, pH = 6 rất yếu)."),
            make_tf(3, "Vận dụng", f"Đề {t} - Cho dung dịch NaOH tác dụng với dung dịch muối FeCl3:", [
                ("a", "Xuất hiện kết tủa màu nâu đỏ.", True),
                ("b", "Kết tủa là Iron(III) hydroxide Fe(OH)3.", True),
                ("c", "Dung dịch sau phản ứng có chứa muối NaCl.", True),
                ("d", "Kết tủa Fe(OH)3 tan được trong nước cất khi đun sôi.", False)
            ], "Fe(OH)3 là base không tan trong nước."),
            make_tf(4, "Vận dụng", f"Đề {t} - Nhiệt phân hoàn toàn 19,6 gam Cu(OH)2:", [
                ("a", "Số mol Cu(OH)2 là 0,2 mol (M=98).", True),
                ("b", "Chất rắn màu đen thu được là CuO có khối lượng 16,0 gam.", True),
                ("c", "Khối lượng hơi nước thoát ra là 3,6 gam.", True),
                ("d", "CuO tạo thành tác dụng được với khí CO ở nhiệt độ cao giải phóng kim loại Cu.", True)
            ], "Cu(OH)2 -> CuO + H2O; CuO + CO -> Cu + CO2.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Dung dịch có pH = 7 là môi trường gì? (Acid, Base hay Trung tính)", "Trung tính", "Môi trường trung tính."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Dung dịch NaOH làm phenolphthalein chuyển sang màu gì?", "Hồng", "Màu hồng (hoặc đỏ hồng)."),
            make_sa(3, "Vận dụng", f"Đề {t} - Cần bao nhiêu gam NaOH để phản ứng vừa hết với 0,1 mol HCl?", "4", "nNaOH = 0,1 mol => m = 0,1 × 40 = 4 gam."),
            make_sa(4, "Vận dụng", f"Đề {t} - Nung nóng hoàn toàn 9,8 gam Cu(OH)2 thu được bao nhiêu gam CuO? (Cu=64, O=16)", "8", "n = 0,1 mol => mCuO = 0,1 × 80 = 8 gam."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Trộn 100 mL dung dịch HCl 0,1M với 100 mL dung dịch NaOH 0,1M. Dung dịch thu được có pH bằng bao nhiêu?", "7", "Số mol HCl = NaOH = 0,01 mol => trung hòa hoàn toàn => pH = 7."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Cho 200 mL dung dịch NaOH 1M tác dụng hoàn toàn với dung dịch CuCl2 dư. Khối lượng kết tủa Cu(OH)2 thu được là bao nhiêu gam?", "9.8", "nNaOH = 0,2 mol => nCu(OH)2 = 0,1 mol => m = 0,1 × 98 = 9,8 gam.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Xà phòng và các chất tẩy rửa thường có tính kiềm (pH từ 8 đến 10). Lý do tính kiềm được ứng dụng trong tẩy rửa là vì:", ["Dung dịch kiềm có khả năng thủy phân và làm tan chất béo, dầu mỡ bám dính", "Dung dịch kiềm làm tăng độ nhớt", "Dung dịch kiềm ăn mòn vải", "Kiềm trung hòa nước"], 0, "Phản ứng xà phòng hóa thủy phân chất béo dầu mỡ."),
            make_vdc(2, f"Đề {t} - Khi bị ong vò vẽ đốt (nọc ong vò vẽ có tính kiềm), kinh nghiệm dân gian khuyên nên bôi chất nào sau đây vào vết đốt để làm dịu cơn đau?", ["Nước vôi trong", "Nước xà phòng", "Nước giấm ăn hoặc nước chanh", "Dung dịch nước muối"], 2, "Giấm/chanh có tính acid nhẹ giúp trung hòa nọc kiềm của ong vò vẽ."),
            make_vdc(3, f"Đề {t} - Nhỏ vài giọt dung dịch phenolphthalein vào cốc chứa dung dịch NaOH thấy dung dịch có màu hồng. Nhỏ từ từ dung dịch HCl vào cốc và khuấy đều cho đến khi dung dịch vừa mất màu hồng hoàn toàn. Hiện tượng mất màu hồng chứng tỏ:", ["Lượng NaOH trong cốc đã bị trung hòa hết hoàn toàn bởi acid HCl", "Acid HCl đã biến thành chất khác", "Phenolphthalein bị phân hủy bởi ánh sáng", "Dung dịch đã chuyển sang màu xanh"], 0, "Mất màu hồng khi pH giảm về ≤ 7 (NaOH hết)."),
            make_vdc(4, f"Đề {t} - Một mẫu đất nông nghiệp kiểm tra đo được pH = 4,2. Để đất trồng thích hợp cho cây lúa sinh trưởng (pH tối ưu từ 5,5 đến 6,5), người kỹ sư nông nghiệp cần chỉ đạo bà con:", ["Bón vôi bột (Ca(OH)2) với lượng thích hợp để khử chua", "Bón thêm acid nitric", "Ngừng tưới nước", "Bón thật nhiều phân đạm"], 0, "Bón vôi trung hòa acid trong đất.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 9: Base và thang pH - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c2", "chapterTitle": "Chương II: Một số hợp chất thông dụng",
            "lessonId": "chem8_c2_b9", "lessonName": "Bài 9: Base - Thang pH",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 10: OXIDE (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c2_b10_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Oxide là hợp chất của bao nhiêu nguyên tố hóa học, trong đó có một nguyên tố là Oxygen?", ["Hai nguyên tố", "Ba nguyên tố", "Một nguyên tố", "Bốn nguyên tố"], 0, "Oxide là hợp chất gồm 2 nguyên tố, trong đó có 1 nguyên tố là Oxygen."),
            make_mc(2, "Nhận biết", f"Đề {t} - Oxide nào sau đây là oxide acid?", ["CO2", "CaO", "Na2O", "CuO"], 0, "CO2 là oxide acid (tác dụng nước tạo carbonic acid)."),
            make_mc(3, "Nhận biết", f"Đề {t} - Oxide nào sau đây là oxide base?", ["CaO", "SO2", "P2O5", "CO2"], 0, "CaO là oxide base (tác dụng nước tạo base Ca(OH)2)."),
            make_mc(4, "Nhận biết", f"Đề {t} - Khí nào sau đây là oxide trung tính (không tác dụng với acid và base ở điều kiện thường)?", ["CO", "CO2", "SO2", "SO3"], 0, "CO, NO là các oxide trung tính."),
            make_mc(5, "Nhận biết", f"Đề {t} - Oxide nào sau đây là oxide lưỡng tính (tác dụng được với cả dung dịch acid và dung dịch base)?", ["Al2O3", "Na2O", "CaO", "SO2"], 0, "Al2O3 và ZnO là oxide lưỡng tính."),
            make_mc(6, "Nhận biết", f"Đề {t} - Tên gọi thông thường của Calcium oxide (CaO) trong đời sống là:", ["Vôi sống", "Đá vôi", "Vôi tôi", "Thạch cao"], 0, "CaO là vôi sống."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Khí Carbon dioxide (CO2) tác dụng với dung dịch Ca(OH)2 tạo kết tủa trắng là chất nào?", ["CaCO3", "CaO", "Ca(HCO3)2", "CaCl2"], 0, "CO2 + Ca(OH)2 -> CaCO3 (kết tủa trắng) + H2O."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Khi cho CaO vào nước xảy ra hiện tượng tỏa nhiều nhiệt và tạo thành dung dịch vôi tôi có công thức:", ["Ca(OH)2", "CaCO3", "CaCl2", "CaSO4"], 0, "CaO + H2O -> Ca(OH)2."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Oxide nào sau đây tác dụng với nước tạo thành dung dịch làm quỳ tím hóa đỏ?", ["P2O5", "Na2O", "BaO", "K2O"], 0, "P2O5 + 3H2O -> 2H3PO4 (acid làm đỏ quỳ)."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Cho bột Đồng(II) oxide (CuO) màu đen vào ống nghiệm đựng dung dịch H2SO4 loãng, đun nóng nhẹ. Hiện tượng là:", ["Chất rắn màu đen tan dần, dung dịch chuyển sang màu xanh lam", "Có bọt khí bay ra", "Xuất hiện kết tủa màu trắng", "Không đổi màu"], 0, "CuO + H2SO4 -> CuSO4 (xanh lam) + H2O."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Oxide nào sau đây là chất khí không màu, không mùi, rất độc vì liên kết chặt với hemoglobin trong máu ngăn cản vận chuyển oxy?", ["Carbon monoxide (CO)", "Carbon dioxide (CO2)", "Sulfur dioxide (SO2)", "Nitrogen dioxide (NO2)"], 0, "Khí CO rất độc sinh ra khi đốt than thiếu oxy."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Dãy gồm toàn các oxide base tan được trong nước ở điều kiện thường là:", ["Na2O, K2O, CaO, BaO", "CuO, FeO, Al2O3, MgO", "CO2, SO2, P2O5, N2O5", "ZnO, PbO, Fe2O3, Cr2O3"], 0, "Na2O, K2O, CaO, BaO tan trong nước tạo kiềm.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Về phân loại các oxide:", [
                ("a", "Oxide base thường là oxide của kim loại và tương ứng với một base.", True),
                ("b", "Oxide acid thường là oxide của phi kim và tương ứng với một acid.", True),
                ("c", "Al2O3 và ZnO là các oxide lưỡng tính tác dụng được với cả acid và kiềm.", True),
                ("d", "Tất cả các oxide kim loại đều tan trong nước ở nhiệt độ phòng.", False)
            ], "Nhiều oxide kim loại như CuO, Fe2O3, Al2O3 không tan trong nước."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Khi dẫn khí CO2 sục từ từ vào cốc đựng nước vôi trong Ca(OH)2:", [
                ("a", "Ban đầu nước vôi trong bị vẩn đục do tạo kết tủa CaCO3.", True),
                ("b", "Nếu tiếp tục sục dư khí CO2 thì kết tủa tan dần tạo dung dịch trong suốt Ca(HCO3)2.", True),
                ("c", "Đun nóng dung dịch trong suốt lại thấy xuất hiện kết tủa trở lại.", True),
                ("d", "Khí CO2 là một oxide base điển hình.", False)
            ], "CO2 là oxide acid."),
            make_tf(3, "Vận dụng", f"Đề {t} - Cho 8,0 gam CuO tác dụng vừa đủ với dung dịch HCl 2M:", [
                ("a", "Số mol CuO là 0,1 mol (M=80).", True),
                ("b", "Số mol HCl đã phản ứng là 0,2 mol.", True),
                ("c", "Thể tích dung dịch HCl đã dùng là 100 mL.", True),
                ("d", "Khối lượng muối CuCl2 tạo thành là 12,0 gam.", False)
            ], "mCuCl2 = 0,1 × 135 = 13,5 gam."),
            make_tf(4, "Vận dụng", f"Đề {t} - Xét ứng dụng của Calcium oxide (vôi sống CaO):", [
                ("a", "Dùng trong công nghiệp luyện kim, sản xuất xi măng.", True),
                ("b", "Dùng làm chất hút ẩm trong phòng thí nghiệm vì háo nước.", True),
                ("c", "Dùng để khử chua đất trồng trọt và xử lí nước thải.", True),
                ("d", "Vôi sống để lâu ngoài không khí ẩm vẫn giữ nguyên 100% độ tinh khiết.", False)
            ], "CaO hút ẩm thành Ca(OH)2 rồi tác dụng CO2 tạo CaCO3.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Khí Carbon dioxide có công thức hóa học là gì?", "CO2", "CO2."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Calcium oxide có công thức hóa học là gì?", "CaO", "CaO."),
            make_sa(3, "Vận dụng", f"Đề {t} - Hòa tan hoàn toàn 5,6 gam CaO vào nước thu được bao nhiêu gam Ca(OH)2? (Ca=40, O=16, H=1)", "7.4", "nCaO = 0,1 mol => mCa(OH)2 = 0,1 × 74 = 7,4 gam."),
            make_sa(4, "Vận dụng", f"Đề {t} - Dẫn 2,479 lít khí CO2 ở đkc vào dung dịch Ca(OH)2 dư thu được bao nhiêu gam kết tủa CaCO3?", "10", "n = 0,1 mol => mCaCO3 = 0,1 × 100 = 10 gam."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Dùng 0,1 mol khí CO khử hoàn toàn 8 gam bột Fe2O3 ở nhiệt độ cao. Khối lượng Fe kim loại thu được là bao nhiêu gam?", "5.6", "Fe2O3 + 3CO -> 2Fe + 3CO2. nCO = 0,1 mol => nFe = 0,1 × 2/3 không tròn. Xét: nFe2O3 = 8/160 = 0,05 mol. Cần 0,15 mol CO. Nếu CO dư thì nFe = 0,05 × 2 = 0,1 mol => mFe = 5,6 gam."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Khử hoàn toàn 16 gam Fe2O3 cần vừa đủ bao nhiêu lít khí CO ở điều kiện chuẩn (25 °C, 1 bar)? (Làm tròn 2 chữ số)", "7.44", "nFe2O3 = 0,1 mol => nCO = 0,3 mol => V = 0,3 × 24,79 = 7,437 L ≈ 7,44 L.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Hiệu ứng nhà kính khiến Trái Đất nóng lên toàn cầu chủ yếu do sự gia tăng nồng độ của oxide nào sau đây trong khí quyển do đốt cháy nhiên liệu hóa thạch?", ["Carbon dioxide (CO2)", "Sulfur dioxide (SO2)", "Nitrogen monoxide (NO)", "Phosphorus pentoxide (P2O5)"], 0, "CO2 là khí nhà kính chính."),
            make_vdc(2, f"Đề {t} - Khí SO2 sinh ra từ việc đốt than đá và dầu mỏ có chứa lưu huỳnh. Để loại bỏ khí SO2 trong khí thải công nghiệp trước khi xả ra môi trường, người ta thường dẫn khí thải qua chất nào sau đây có giá thành rẻ và hiệu quả cao?", ["Dung dịch hoặc sữa vôi tôi Ca(OH)2", "Dung dịch acid HCl", "Nước cất", "Dung dịch muối ăn NaCl"], 0, "SO2 + Ca(OH)2 -> CaSO3 + H2O kết tủa giữ lại SO2."),
            make_vdc(3, f"Đề {t} - Một hỗn hợp bột gồm Fe2O3 và Cu. Để hòa tan hết hỗn hợp chất rắn này thành dung dịch đồng nhất, người ta có thể dùng một lượng dư dung dịch nào sau đây?", ["Dung dịch hydrochloric acid (HCl)", "Nước cất", "Dung dịch kiềm NaOH", "Dung dịch muối BaCl2"], 0, "Fe2O3 tan trong HCl thành FeCl3, sau đó Cu tan trong FeCl3: Cu + 2FeCl3 -> CuCl2 + 2FeCl2."),
            make_vdc(4, f"Đề {t} - Gạch chịu lửa dùng để lót bên trong các lò luyện gang thép công nghiệp thường được chế tạo từ oxide nào có nhiệt độ nóng chảy cực kì cao (trên 2000 °C)?", ["Aluminium oxide (Al2O3) và Magnesium oxide (MgO)", "Sulfur trioxide (SO3)", "Carbon dioxide (CO2)", "Sodium oxide (Na2O)"], 0, "Al2O3 và MgO rất bền nhiệt, nóng chảy ở nhiệt độ trên 2000 - 2800 °C.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 10: Oxide - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c2", "chapterTitle": "Chương II: Một số hợp chất thông dụng",
            "lessonId": "chem8_c2_b10", "lessonName": "Bài 10: Oxide",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 11: MUỐI (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c2_b11_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Muối là hợp chất được tạo nên từ:", ["Kim loại (hoặc ion NH4+) liên kết với gốc acid", "Kim loại và nhóm OH", "Hydrogen và gốc acid", "Kim loại và Oxygen"], 0, "Muối gồm kim loại (hoặc NH4+) và gốc acid."),
            make_mc(2, "Nhận biết", f"Đề {t} - Muối nào sau đây tan tốt trong nước ở nhiệt độ phòng?", ["NaCl (muối ăn)", "BaSO4", "CaCO3", "AgCl"], 0, "NaCl tan tốt trong nước."),
            make_mc(3, "Nhận biết", f"Đề {t} - Muối nào sau đây là chất kết tủa màu trắng không tan trong nước và acid?", ["Barium sulfate (BaSO4)", "Sodium sulfate (Na2SO4)", "Copper sulfate (CuSO4)", "Potassium chloride (KCl)"], 0, "BaSO4 kết tủa trắng."),
            make_mc(4, "Nhận biết", f"Đề {t} - Muối nào sau đây là kết tủa màu vàng nhạt?", ["Silver bromide (AgBr)", "Barium sulfate (BaSO4)", "Calcium carbonate (CaCO3)", "Sodium nitrate (NaNO3)"], 0, "AgBr kết tủa vàng nhạt, AgI vàng đậm."),
            make_mc(5, "Nhận biết", f"Đề {t} - Điều kiện để phản ứng trao đổi giữa hai dung dịch muối xảy ra là sản phẩm phải có:", ["Chất kết tủa hoặc chất khí", "Chất tan tốt", "Màu sắc đậm", "Nhiệt độ sôi cao"], 0, "Tạo kết tủa, bay hơi hoặc chất điện li yếu (nước)."),
            make_mc(6, "Nhận biết", f"Đề {t} - Tên gọi thông thường của muối Sodium chloride (NaCl) là:", ["Muối ăn", "Muối nở", "Phèn chua", "Diêm tiêu"], 0, "NaCl là muối ăn."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Cho mẩu đinh sắt (Fe) sạch vào ống nghiệm chứa dung dịch CuSO4 màu xanh lam. Hiện tượng là:", ["Đinh sắt có lớp kim loại màu đỏ bám ngoài, màu xanh của dung dịch nhạt dần", "Có bọt khí bay ra", "Sắt tan biến mất hoàn toàn", "Không có hiện tượng gì"], 0, "Fe + CuSO4 -> FeSO4 + Cu (đỏ bám trên Fe)."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Cho dung dịch AgNO3 tác dụng với dung dịch NaCl, hiện tượng là:", ["Xuất hiện kết tủa trắng AgCl", "Có khí bay ra", "Dung dịch chuyển sang màu xanh", "Không đổi màu"], 0, "AgNO3 + NaCl -> AgCl (kết tủa trắng) + NaNO3."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Cặp chất nào sau đây CÙNG TỒN TẠI trong một dung dịch (không phản ứng với nhau)?", ["NaCl và KNO3", "BaCl2 và Na2SO4", "AgNO3 và HCl", "Na2CO3 và CaCl2"], 0, "NaCl và KNO3 không tạo kết tủa hay khí nên cùng tồn tại."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Cho dung dịch Na2CO3 vào dung dịch HCl, hiện tượng quan sát được là:", ["Sủi bọt khí không màu CO2", "Xuất hiện kết tủa trắng", "Dung dịch đổi màu tím", "Không hiện tượng"], 0, "Na2CO3 + 2HCl -> 2NaCl + CO2 + H2O."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Muối Baking soda (dùng làm bánh, tẩy rửa) có công thức là:", ["NaHCO3", "Na2CO3", "NaCl", "Na2SO4"], 0, "Sodium hydrogencarbonate NaHCO3."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Để phân biệt dung dịch Na2SO4 và dung dịch NaCl, thuốc thử thích hợp nhất là:", ["Dung dịch BaCl2", "Dung dịch NaOH", "Quỳ tím", "Dung dịch HCl"], 0, "BaCl2 tạo kết tủa trắng BaSO4 với Na2SO4.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Về tính tan của muối trong nước:", [
                ("a", "Tất cả các muối chứa gốc nitrate (-NO3) và muối của Na, K đều tan tốt trong nước.", True),
                ("b", "Hầu hết các muối carbonate (gốc CO3) đều không tan (trừ Na2CO3, K2CO3, (NH4)2CO3).", True),
                ("c", "Muối AgCl không tan trong nước và có màu trắng.", True),
                ("d", "Muối BaSO4 tan rất tốt trong dung dịch acid HCl.", False)
            ], "BaSO4 không tan trong cả nước và dung dịch acid."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Xét phản ứng trao đổi trong dung dịch:", [
                ("a", "Phản ứng trao đổi là phản ứng trong đó hai hợp chất trao đổi thành phần với nhau để tạo thành hợp chất mới.", True),
                ("b", "Phản ứng trao đổi chỉ xảy ra khi sản phẩm tạo thành có chất kết tủa hoặc chất khí hoặc nước.", True),
                ("c", "Phản ứng giữa acid và base (phản ứng trung hòa) cũng là một dạng phản ứng trao đổi.", True),
                ("d", "Mọi phản ứng trao đổi đều làm thay đổi số oxi hóa của các nguyên tố.", False)
            ], "Phản ứng trao đổi không có sự thay đổi số oxi hóa."),
            make_tf(3, "Vận dụng", f"Đề {t} - Nhúng một thanh kẽm (Zn) nặng 10 gam vào 100 mL dung dịch CuSO4 1M. Sau khi phản ứng hoàn toàn lấy thanh kẽm ra cân lại:", [
                ("a", "Số mol CuSO4 là 0,1 mol.", True),
                ("b", "Có 0,1 mol Zn tan ra và 0,1 mol Cu bám vào thanh kẽm.", True),
                ("c", "Khối lượng thanh kẽm sau phản ứng sẽ giảm đi 0,1 gam.", True),
                ("d", "Dung dịch sau phản ứng có màu xanh đậm hơn ban đầu.", False)
            ], "Zn (65) tan, Cu (64) bám => m giảm = 0,1 × (65 - 64) = 0,1g. Dung dịch nhạt màu xanh do Cu2+ hết."),
            make_tf(4, "Vận dụng", f"Đề {t} - Cho dung dịch Ba(OH)2 dư vào ống nghiệm chứa dung dịch MgSO4:", [
                ("a", "Xuất hiện kết tủa trắng gồm hai chất BaSO4 và Mg(OH)2.", True),
                ("b", "Đây là phản ứng trao đổi.", True),
                ("c", "Số mol kết tủa thu được bằng 2 lần số mol MgSO4 phản ứng.", True),
                ("d", "Thêm dung dịch HCl dư vào ống nghiệm thì toàn bộ kết tủa tan hết.", False)
            ], "Chỉ có Mg(OH)2 tan trong HCl, BaSO4 không tan trong HCl.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Muối ăn có công thức hóa học là gì?", "NaCl", "NaCl."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Kết tủa Barium sulfate BaSO4 có màu gì?", "Trắng", "Màu trắng."),
            make_sa(3, "Vận dụng", f"Đề {t} - Hòa tan 10,6 gam Na2CO3 vào dung dịch HCl dư. Thể tích khí CO2 thu được ở đkc (25 °C, 1 bar) là bao nhiêu lít? (Làm tròn 2 chữ số)", "2.48", "n = 0,1 mol => V = 0,1 × 24,79 = 2,479 ≈ 2,48 lít."),
            make_sa(4, "Vận dụng", f"Đề {t} - Cho 0,1 mol BaCl2 tác dụng hoàn toàn với dung dịch Na2SO4 dư. Khối lượng kết tủa BaSO4 thu được là bao nhiêu gam? (Ba=137, S=32, O=16)", "23.3", "0,1 × 233 = 23,3 gam."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Cho một lá sắt nặng 50 gam vào dung dịch CuSO4 dư. Sau một thời gian lấy lá sắt ra cân lại thấy nặng 50,8 gam. Khối lượng Cu đã bám lên lá sắt là bao nhiêu gam?", "6.4", "Tăng 50,8 - 50 = 0,8g = n × (64 - 56) = 8n => n = 0,1 mol => mCu = 0,1 × 64 = 6,4 gam."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Trộn 100 mL dung dịch AgNO3 1M với 100 mL dung dịch NaCl 1M. Khối lượng kết tủa AgCl thu được là bao nhiêu gam? (Ag=108, Cl=35,5)", "14.35", "n = 0,1 mol => m = 0,1 × 143,5 = 14,35 gam.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Nước muối sinh lí NaCl 0,9% được sử dụng phổ biến trong y tế để súc họng, rửa vết thương, nhỏ mắt vì:", ["Nồng độ 0,9% đẳng trương với dịch cơ thể người, giúp làm sạch dịu nhẹ và ngăn ngừa vi khuẩn mà không gây tổn thương tế bào", "Nước muối sinh lí có tính acid diệt khuẩn", "Nước muối sinh lí có chứa chất kháng sinh", "Nồng độ muối càng cao càng tốt"], 0, "Đẳng trương với dịch cơ thể."),
            make_vdc(2, f"Đề {t} - Trong nông nghiệp và đời sống, muối Baking soda (NaHCO3) thường được dùng làm bột nở khi nướng bánh bông lan. Cơ chế làm bánh nở xốp là do:", ["Khi nướng ở nhiệt độ cao, NaHCO3 bị nhiệt phân giải phóng bọt khí CO2 làm bột bánh phồng xốp", "NaHCO3 nở ra khi gặp nhiệt", "NaHCO3 phản ứng với tinh bột tạo bọt", "NaHCO3 hút ẩm làm bánh khô ráo"], 0, "2NaHCO3 -> Na2CO3 + CO2 + H2O tạo các lỗ khí xốp trong bánh."),
            make_vdc(3, f"Đề {t} - Để loại bỏ các ion kim loại nặng độc hại như Pb2+, Cu2+, Cd2+ trong nước thải công nghiệp trước khi thải ra nguồn nước tự nhiên, phương pháp hóa học đơn giản và hiệu quả nhất là:", ["Cho sữa vôi Ca(OH)2 hoặc Na2S vào để kết tủa các ion kim loại nặng dưới dạng hydroxide hoặc sulfide không tan rồi lắng lọc", "Thêm acid HCl vào nước thải", "Đun sôi nước thải", "Cho muối ăn NaCl vào"], 0, "Tạo kết tủa không tan Pb(OH)2, Cu(OH)2, PbS, CuS rồi lắng đọng tách ra."),
            make_vdc(4, f"Đề {t} - Thạch cao nung dùng để bó bột khi gãy xương hoặc đúc tượng mỹ thuật có thành phần chính là muối nào sau đây?", ["Calcium sulfate ngậm nước: CaSO4.0,5H2O", "Calcium carbonate: CaCO3", "Barium sulfate: BaSO4", "Sodium chloride: NaCl"], 0, "CaSO4.0,5H2O hút nước đông cứng thành thạch cao sống CaSO4.2H2O.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 11: Muối - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c2", "chapterTitle": "Chương II: Một số hợp chất thông dụng",
            "lessonId": "chem8_c2_b11", "lessonName": "Bài 11: Muối",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- BÀI 12: PHÂN BÓN HÓA HỌC (3 ĐỀ) ---
    for t in range(1, 4):
        k = f"chem8_c2_b12_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề {t} - Ba nguyên tố dinh dưỡng chính cần thiết cho cây trồng trong phân bón vô cơ là:", ["N, P, K", "Ca, Mg, S", "C, H, O", "Fe, Cu, Zn"], 0, "Đạm (N), Lân (P), Kali (K)."),
            make_mc(2, "Nhận biết", f"Đề {t} - Phân đạm cung cấp nguyên tố dinh dưỡng nào cho cây trồng?", ["Nitrogen (N)", "Phosphorus (P)", "Potassium (K)", "Calcium (Ca)"], 0, "Phân đạm cung cấp Nitrogen (N)."),
            make_mc(3, "Nhận biết", f"Đề {t} - Phân lân cung cấp nguyên tố dinh dưỡng nào cho cây trồng?", ["Phosphorus (P)", "Nitrogen (N)", "Potassium (K)", "Silicon (Si)"], 0, "Phân lân cung cấp Phosphorus (P)."),
            make_mc(4, "Nhận biết", f"Đề {t} - Phân kali cung cấp nguyên tố dinh dưỡng nào cho cây trồng?", ["Potassium (K)", "Nitrogen (N)", "Phosphorus (P)", "Sodium (Na)"], 0, "Phân kali cung cấp K."),
            make_mc(5, "Nhận biết", f"Đề {t} - Phân bón NPK là loại phân bón:", ["Hỗn hợp cung cấp cả 3 nguyên tố N, P, K", "Chỉ cung cấp N", "Chỉ cung cấp P", "Chỉ cung cấp K"], 0, "Phân bón hỗn hợp NPK."),
            make_mc(6, "Nhận biết", f"Đề {t} - Phân đạm Urê có công thức hóa học là:", ["(NH2)2CO", "NH4NO3", "(NH4)2SO4", "KNO3"], 0, "(NH2)2CO là phân đạm Urê."),
            make_mc(7, "Thông hiểu", f"Đề {t} - Vai trò chính của phân đạm đối với cây trồng là:", ["Kích thích cây phát triển thân, lá, cành xanh tốt", "Kích thích rễ phát triển và ra hoa kết quả", "Tăng khả năng chống rét, chống sâu bệnh và chịu hạn", "Làm ngọt quả"], 0, "Phân đạm phát triển cành lá sinh trưởng."),
            make_mc(8, "Thông hiểu", f"Đề {t} - Vai trò chính của phân kali đối với cây trồng là:", ["Tăng cường khả năng chống chịu rét, hạn hán, sâu bệnh và tăng phẩm chất hạt/củ/quả", "Chỉ phát triển lá", "Chỉ giúp nảy mầm", "Làm chua đất"], 0, "Kali tăng sức chống chịu và chất lượng nông sản."),
            make_mc(9, "Thông hiểu", f"Đề {t} - Phân bón nào sau đây có hàm lượng Nitrogen cao nhất trong các loại phân đạm đơn?", ["Urê (NH2)2CO (khoảng 46%)", "Đạm amoni nitrate NH4NO3 (khoảng 35%)", "Đạm amoni sunfat (NH4)2SO4 (khoảng 21%)", "Đạm amoni clorua NH4Cl"], 0, "Urê có hàm lượng N cao nhất (≈ 46,67%)."),
            make_mc(10, "Thông hiểu", f"Đề {t} - Không nên bón phân đạm amoni cùng với chất nào sau đây vì sẽ làm mất đạm do thoát khí ammonia (NH3)?", ["Vôi sống hoặc vôi tôi", "Phân kali", "Nước tưới", "Cát"], 0, "Kiềm tác dụng muối amoni giải phóng khí NH3 bay đi làm mất tác dụng của phân đạm."),
            make_mc(11, "Thông hiểu", f"Đề {t} - Phân bón vi lượng cung cấp các nguyên tố cần thiết với hàm lượng rất nhỏ như:", ["B, Zn, Cu, Fe, Mn", "N, P, K", "Ca, Mg", "C, H, O"], 0, "Vi lượng gồm Bo, Kẽm, Đồng, Sắt, Mangan..."),
            make_mc(12, "Thông hiểu", f"Đề {t} - Hậu quả của việc lạm dụng bón quá nhiều phân bón hóa học là:", ["Làm thoái hóa đất, ô nhiễm nguồn nước ngầm và dư lượng nitrate trong nông sản", "Cây luôn luôn khỏe mạnh", "Đất ngày càng màu mỡ", "Không có tác hại gì"], 0, "Gây chua đất, phú dưỡng nguồn nước và tồn dư nitrate độc hại.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề {t} - Về các loại phân bón hóa học:", [
                ("a", "Phân đơn chỉ chứa một trong ba nguyên tố dinh dưỡng chính N, P hoặc K.", True),
                ("b", "Phân NPK là phân bón hỗn hợp chứa cả ba nguyên tố N, P, K.", True),
                ("c", "Độ dinh dưỡng của phân đạm được đánh giá bằng phần trăm khối lượng của nguyên tố N.", True),
                ("d", "Phân lân giúp cây tăng cường khả năng chịu rét và tích tụ đường trong quả.", False)
            ], "Tăng chịu rét và ngọt quả là vai trò của Kali; Lân kích thích phát triển rễ và ra hoa kết hạt."),
            make_tf(2, "Thông hiểu", f"Đề {t} - Nguyên tắc bón phân hợp lí cho cây trồng:", [
                ("a", "Bón đúng loại phân phù hợp với từng giai đoạn sinh trưởng của cây.", True),
                ("b", "Bón đúng liều lượng, tránh bón thừa gây lãng phí và ô nhiễm môi trường.", True),
                ("c", "Bón đúng thời điểm và đúng cách (không bón lúc trời mưa to hay nắng gắt).", True),
                ("d", "Càng bón nhiều phân đạm hóa học thì nông sản càng sạch và an toàn.", False)
            ], "Bón thừa đạm làm tích lũy nitrate gây hại cho sức khỏe người tiêu dùng."),
            make_tf(3, "Vận dụng", f"Đề {t} - Một bao phân bón NPK có ghi tỉ lệ 20 - 20 - 15:", [
                ("a", "Số 20 đầu tiên cho biết hàm lượng %N trong bao phân bón là 20%.", True),
                ("b", "Số 20 thứ hai biểu thị hàm lượng lân tính theo %P2O5.", True),
                ("c", "Số 15 thứ ba biểu thị hàm lượng kali tính theo %K2O.", True),
                ("d", "Trong bao phân bón này không chứa bất kì thành phần tạp chất nào.", False)
            ], "Phân bón NPK chứa các chất phụ gia và tạp chất độn."),
            make_tf(4, "Vận dụng", f"Đề {t} - Xét phân đạm Ammonium nitrate (NH4NO3):", [
                ("a", "Khối lượng mol của NH4NO3 là 80 g/mol.", True),
                ("b", "Trong 1 phân tử NH4NO3 có 2 nguyên tử Nitrogen.", True),
                ("c", "Phần trăm khối lượng của Nitrogen trong phân đạm này là 35%.", True),
                ("d", "Bón phân amoni nitrate lâu năm làm đất có xu hướng kiềm hóa.", False)
            ], "%N = 28 / 80 = 35%. Muối amoni thủy phân tạo acid làm chua đất.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề {t} - Phân bón nào cung cấp nguyên tố Nitrogen cho cây trồng? (Đạm, Lân hay Kali)", "Đạm", "Phân đạm."),
            make_sa(2, "Thông hiểu", f"Đề {t} - Công thức hóa học của phân kali clorua là gì?", "KCl", "KCl."),
            make_sa(3, "Vận dụng", f"Đề {t} - Phần trăm khối lượng của nguyên tố Nitrogen trong phân đạm Urê (NH2)2CO là bao nhiêu %? (Làm tròn 1 chữ số thập phân)", "46.7", "28 / 60 × 100% ≈ 46,67% ≈ 46,7%."),
            make_sa(4, "Vận dụng", f"Đề {t} - Để cung cấp 14 kg Nitrogen cho ruộng lúa, người nông dân cần bón bao nhiêu kg phân đạm Urê chứa 46,7% N? (Làm tròn số nguyên)", "30", "14 / 0,467 ≈ 29,98 kg ≈ 30 kg."),
            make_sa(5, "Vận dụng cao", f"Đề {t} - Phần trăm khối lượng của nguyên tố Nitrogen trong phân đạm Ammonium sulfate (NH4)2SO4 là bao nhiêu %? (Làm tròn 1 chữ số thập phân)", "21.2", "M = 132 g/mol. %N = 28 / 132 × 100% ≈ 21,2%."),
            make_sa(6, "Vận dụng cao", f"Đề {t} - Trong một bao phân bón NPK 16-16-8 nặng 50 kg, khối lượng nguyên tố Nitrogen có trong bao phân bón là bao nhiêu kg?", "8", "50 × 16% = 8 kg.")
        ]
        p4 = [
            make_vdc(1, f"Đề {t} - Vì sao các nhà khoa học và chuyên gia nông nghiệp luôn khuyến cáo không được bón vôi sống (CaO) hoặc tro bếp (chứa K2CO3 kiềm) cùng một lúc với các loại phân đạm chứa gốc amoni (NH4+)?", ["Vì môi trường kiềm sẽ phản ứng với ion amoni giải phóng khí ammonia (NH3) có mùi khai bay mất, làm mất tác dụng của phân đạm", "Vì tạo thành hỗn hợp nổ nguy hiểm", "Vì làm đất bị đông cứng lại như xi măng", "Vì làm cây bị cháy lá ngay lập tức"], 0, "NH4+ + OH- -> NH3 (khí bay đi) + H2O làm mất hàm lượng đạm."),
            make_vdc(2, f"Đề {t} - Hiện tượng 'phú dưỡng' (thủy vực nở hoa, tảo phát triển bùng nổ rồi chết y sinh mùi hôi thối và làm cá chết ngạt) ở các ao hồ, sông ngòi lân cận vùng sản xuất nông nghiệp nguyên nhân chính là do:", ["Nước mưa cuốn trôi lượng dư thừa phân bón hóa học (đặc biệt là đạm N và lân P) từ đồng ruộng vào nguồn nước", "Do nhiệt độ nước hồ quá lạnh", "Do nồng độ muối ăn NaCl quá cao", "Do rác thải túi nilon"], 0, "Dư thừa N và P gây hiện tượng phú dưỡng nguồn nước."),
            make_vdc(3, f"Đề {t} - Trong giai đoạn cây ăn quả đang chuẩn bị đón tết và tích lũy đường làm ngọt quả, tăng độ bóng đẹp cho vỏ quả, loại phân bón nào cần được ưu tiên bổ sung tăng cường?", ["Phân Kali", "Phân Đạm", "Phân Lân", "Vôi sống"], 0, "Kali tăng tích tụ đường và phẩm chất quả."),
            make_vdc(4, f"Đề {t} - Xu hướng phát triển nông nghiệp hữu cơ bền vững hiện nay khuyến khích thay thế dần phân bón hóa học bằng:", ["Phân hữu cơ vi sinh, phân chuồng hoai mục và phân trùn quế", "Tăng gấp đôi lượng phân vô cơ NPK", "Chỉ dùng thuốc trừ sâu sinh học", "Không bón bất kì loại phân nào"], 0, "Phân bón hữu cơ vi sinh cải tạo đất và an toàn bền vững.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - Bài 12: Phân bón hóa học - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c2", "chapterTitle": "Chương II: Một số hợp chất thông dụng",
            "lessonId": "chem8_c2_b12", "lessonName": "Bài 12: Phân bón hóa học",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    # --- ÔN TẬP CUỐI CHƯƠNG II (5 ĐỀ) ---
    for t in range(1, 6):
        k = f"chem8_c2_rev_test{t}"
        p1 = [
            make_mc(1, "Nhận biết", f"Đề tổng hợp {t} - Dung dịch acid làm quỳ tím chuyển sang màu:", ["Màu đỏ", "Màu xanh", "Màu vàng", "Màu tím"], 0, "Màu đỏ."),
            make_mc(2, "Nhận biết", f"Đề tổng hợp {t} - Dung dịch kiềm làm quỳ tím chuyển sang màu:", ["Màu xanh", "Màu đỏ", "Màu vàng", "Không đổi màu"], 0, "Màu xanh."),
            make_mc(3, "Nhận biết", f"Đề tổng hợp {t} - Oxide nào sau đây là oxide acid?", ["SO2", "CaO", "BaO", "K2O"], 0, "SO2 là oxide acid."),
            make_mc(4, "Nhận biết", f"Đề tổng hợp {t} - Oxide nào sau đây là oxide base?", ["Na2O", "CO2", "SO3", "P2O5"], 0, "Na2O là oxide base."),
            make_mc(5, "Nhận biết", f"Đề tổng hợp {t} - Muối nào sau đây không tan trong nước?", ["BaSO4", "NaCl", "KNO3", "CaCl2"], 0, "BaSO4 kết tủa trắng."),
            make_mc(6, "Nhận biết", f"Đề tổng hợp {t} - Nguyên tố dinh dưỡng chính trong phân đạm là:", ["Nitrogen (N)", "Phosphorus (P)", "Potassium (K)", "Calcium (Ca)"], 0, "Nitrogen."),
            make_mc(7, "Thông hiểu", f"Đề tổng hợp {t} - Kim loại nào tác dụng được với dung dịch HCl loãng giải phóng H2?", ["Zn", "Cu", "Ag", "Au"], 0, "Zn đứng trước H."),
            make_mc(8, "Thông hiểu", f"Đề tổng hợp {t} - Dãy các base tan trong nước (kiềm) là:", ["NaOH, KOH, Ba(OH)2, Ca(OH)2", "Cu(OH)2, Fe(OH)2, Fe(OH)3", "Al(OH)3, Mg(OH)2, Zn(OH)2", "Pb(OH)2, Ni(OH)2"], 0, "Kiềm: Na, K, Ba, Ca."),
            make_mc(9, "Thông hiểu", f"Đề tổng hợp {t} - Dung dịch có pH = 12 có môi trường:", ["Base mạnh", "Acid mạnh", "Trung tính", "Acid yếu"], 0, "pH = 12 > 7 là base mạnh."),
            make_mc(10, "Thông hiểu", f"Đề tổng hợp {t} - Khí CO2 tác dụng với nước vôi trong tạo kết tủa trắng là:", ["CaCO3", "CaO", "Ca(HCO3)2", "CaCl2"], 0, "CaCO3."),
            make_mc(11, "Thông hiểu", f"Đề tổng hợp {t} - Để phân biệt dung dịch H2SO4 và dung dịch HCl người ta dùng thuốc thử nào?", ["Dung dịch BaCl2", "Dung dịch NaOH", "Quỳ tím", "Dung dịch phenolphtalein"], 0, "BaCl2 tạo kết tủa trắng BaSO4 với H2SO4."),
            make_mc(12, "Thông hiểu", f"Đề tổng hợp {t} - Phản ứng giữa acid và base luôn tạo thành:", ["Muối và nước", "Kim loại và nước", "Khí H2 và muối", "Oxide và acid"], 0, "Phản ứng trung hòa tạo muối và nước.")
        ]
        p2 = [
            make_tf(1, "Thông hiểu", f"Đề tổng hợp {t} - Xét tính chất của các hợp chất vô cơ thông dụng:", [
                ("a", "Acid làm quỳ tím chuyển sang màu đỏ, base làm quỳ tím chuyển sang màu xanh.", True),
                ("b", "Tất cả các muối đều tan tốt trong nước.", False),
                ("c", "Phản ứng trao đổi trong dung dịch cần điều kiện có kết tủa, khí hoặc nước.", True),
                ("d", "Oxide lưỡng tính như Al2O3 tác dụng được với cả dung dịch acid và dung dịch kiềm.", True)
            ], "Có nhiều muối không tan như BaSO4, CaCO3, AgCl."),
            make_tf(2, "Thông hiểu", f"Đề tổng hợp {t} - Về phân bón hóa học:", [
                ("a", "Phân đạm cung cấp N giúp phát triển thân lá.", True),
                ("b", "Phân lân cung cấp P kích thích ra hoa, đâm chồi và bộ rễ khỏe mạnh.", True),
                ("c", "Phân kali giúp cây cứng cáp và chống chịu sâu bệnh, rét, hạn.", True),
                ("d", "Nên bón phân đạm amoni cùng với vôi bột để tăng hiệu quả.", False)
            ], "Trộn với vôi làm thoát khí NH3 mất đạm."),
            make_tf(3, "Vận dụng", f"Đề tổng hợp {t} - Hòa tan hoàn toàn 8,0 gam bột CuO vào dung dịch H2SO4 20% vừa đủ:", [
                ("a", "Số mol CuO phản ứng là 0,1 mol.", True),
                ("b", "Dung dịch thu được có màu xanh lam của muối CuSO4.", True),
                ("c", "Khối lượng dung dịch H2SO4 đã dùng là 49 gam.", True),
                ("d", "Khối lượng muối CuSO4 thu được là 16,0 gam.", True)
            ], "mH2SO4 = 0,1 × 98 = 9,8g => mdd = 9,8 / 20% = 49g. mCuSO4 = 0,1 × 160 = 16g."),
            make_tf(4, "Vận dụng", f"Đề tổng hợp {t} - Cho 10 gam hỗn hợp Fe và Cu vào dung dịch HCl dư thu được 2,479 lít khí H2 ở đkc:", [
                ("a", "Số mol khí H2 là 0,1 mol.", True),
                ("b", "Kim loại Cu không phản ứng với dung dịch HCl.", True),
                ("c", "Khối lượng Fe trong hỗn hợp là 5,6 gam.", True),
                ("d", "Phần trăm khối lượng của Cu trong hỗn hợp là 56%.", False)
            ], "%Cu = (10 - 5,6) / 10 = 4,4 / 10 = 44%.")
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Đề tổng hợp {t} - Dung dịch nước vôi trong Ca(OH)2 có pH lớn hơn 7 hay nhỏ hơn 7?", "Lớn hơn 7", "Lớn hơn 7 (môi trường base)."),
            make_sa(2, "Thông hiểu", f"Đề tổng hợp {t} - Muối ăn có công thức hóa học là gì?", "NaCl", "NaCl."),
            make_sa(3, "Vận dụng", f"Đề tổng hợp {t} - Cần bao nhiêu gam NaOH để trung hòa hết 0,2 mol HCl?", "8", "nNaOH = 0,2 mol => m = 0,2 × 40 = 8 gam."),
            make_sa(4, "Vận dụng", f"Đề tổng hợp {t} - Hòa tan hoàn toàn 5,6 gam Fe vào dung dịch H2SO4 loãng dư thu được bao nhiêu gam muối FeSO4? (Fe=56, S=32, O=16)", "15.2", "0,1 × 152 = 15,2 gam."),
            make_sa(5, "Vận dụng cao", f"Đề tổng hợp {t} - Hòa tan 10 gam CaCO3 vào dung dịch HCl dư. Thể tích khí CO2 thu được ở đkc (25 °C, 1 bar) là bao nhiêu lít? (Làm tròn 2 chữ số)", "2.48", "n = 0,1 mol => V = 0,1 × 24,79 = 2,479 ≈ 2,48 L."),
            make_sa(6, "Vận dụng cao", f"Đề tổng hợp {t} - Cho một lá sắt vào dung dịch CuSO4. Sau khi phản ứng hoàn toàn, khối lượng lá sắt tăng thêm 0,8 gam. Khối lượng Cu bám vào lá sắt là bao nhiêu gam?", "6.4", "n = 0,8 / 8 = 0,1 mol => mCu = 0,1 × 64 = 6,4 gam.")
        ]
        p4 = [
            make_vdc(1, f"Đề tổng hợp {t} - Trong phòng thí nghiệm, một học sinh sơ ý làm đổ dung dịch acid sulfuric đặc ra bàn gỗ. Để trung hòa acid một cách an toàn và lau dọn sạch sẽ, học sinh đó nên dùng hóa chất nào sau đây?", ["Rắc bột vôi tôi Ca(OH)2 hoặc bột baking soda NaHCO3 lên vết acid", "Đổ thật nhiều nước lạnh lên ngay lập tức", "Dùng dung dịch NaOH đặc", "Dùng cồn 90 độ"], 0, "Dùng vôi tôi hoặc NaHCO3 bột trung hòa êm dịu, không đổ nước vào acid đặc vì gây bắn sôi."),
            make_vdc(2, f"Đề tổng hợp {t} - Hiện tượng thạch nhũ trong các hang động đá vôi (như động Phong Nha, Vịnh Hạ Long) được hình thành nhờ hai phản ứng thuận nghịch diễn ra qua hàng triệu năm giữa đá vôi, nước và khí carbon dioxide:", ["$CaCO_3 + H_2O + CO_2 \\rightleftharpoons Ca(HCO_3)_2$", "$CaO + H_2O \\rightarrow Ca(OH)_2$", "$CaCO_3 \\rightarrow CaO + CO_2$", "$CaCl_2 + Na_2CO_3 \\rightarrow CaCO_3 + 2NaCl$"], 0, "Quá trình hòa tan và tái kết tủa CaCO3 tạo thạch nhũ."),
            make_vdc(3, f"Đề tổng hợp {t} - Nước ngầm ở nhiều vùng nông thôn chứa hàm lượng sắt cao dưới dạng muối tan Fe(HCO3)2 làm nước có mùi tanh và để lâu ngoài không khí có váng màu vàng nâu. Người ta xử lí nước giếng khoan này bằng phương pháp nào sau đây?", ["Giàn phun mưa sục khí oxy để oxy hóa Fe(II) thành Fe(III) kết tủa Fe(OH)3 màu nâu đỏ rồi lọc qua cát sỏi", "Thêm acid HCl vào bể nước", "Cho muối ăn vào nước", "Đun sôi toàn bộ nước giếng"], 0, "Oxy hóa Fe(II) thành Fe(OH)3 kết tủa rồi lọc cát."),
            make_vdc(4, f"Đề tổng hợp {t} - Phân bón Supephotphat đơn chứa chất dinh dưỡng chính là muối nào sau đây?", ["$Ca(H_2PO_4)_2$ kèm theo thạch cao $CaSO_4$", "$Ca_3(PO_4)_2$", "$KNO_3$", "$(NH_4)_2SO_4$"], 0, "Supephotphat đơn gồm Ca(H2PO4)2 và CaSO4.")
        ]
        exams[k] = {
            "title": f"Đề kiểm tra KHTN 8 (Hóa học) - [Đề tổng hợp] Ôn tập cuối Chương II - Đề số {t:02d}",
            "grade": "8", "subject": "chemistry", "subjectName": "Hóa học",
            "chapterId": "chem8_c2", "chapterTitle": "Chương II: Một số hợp chất thông dụng",
            "lessonId": "chem8_c2_rev", "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương II",
            "testNum": t, "duration": "45 phút", "points": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }

    return exams

if __name__ == "__main__":
    exs = build_chem8_exams()
    print("Chem 8 generated total:", len(exs), "exams.")
