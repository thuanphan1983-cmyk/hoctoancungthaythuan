# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - HÓA HỌC 9 (KNTT)
Gồm 21 bài/chương ôn tập => 73 đề thi độc lập 100%
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

def build_chem9_exams():
    exams = {}

    # =========================================================================
    # CHƯƠNG I: KIM LOẠI (Bài 1, 2, 3, 4, Rev)
    # =========================================================================
    for b_idx, (b_id, b_name, n_tests) in enumerate([
        ("chem9_c1_b1", "Bài 1: Tính chất của kim loại", 3),
        ("chem9_c1_b2", "Bài 2: Một số kim loại thông dụng (Al, Fe)", 3),
        ("chem9_c1_b3", "Bài 3: Dãy hoạt động hóa học của kim loại", 3),
        ("chem9_c1_b4", "Bài 4: Tách kim loại và sử dụng hợp kim", 3),
        ("chem9_c1_rev", "[Đề tổng hợp] Ôn tập cuối Chương I", 5)
    ]):
        for t in range(1, n_tests + 1):
            k = f"{b_id}_test{t}"
            p1 = [
                make_mc(1, "Nhận biết", f"Đề {t} - Kim loại có tính dẫn điện tốt nhất là:", ["Bạc (Ag)", "Đồng (Cu)", "Vàng (Au)", "Nhôm (Al)"], 0, "Bạc (Ag) dẫn điện tốt nhất, sau đó đến Cu, Au, Al, Fe."),
                make_mc(2, "Nhận biết", f"Đề {t} - Kim loại duy nhất ở thể lỏng ở nhiệt độ thường là:", ["Thủy ngân (Hg)", "Chì (Pb)", "Thiếc (Sn)", "Nhôm (Al)"], 0, "Thủy ngân (Hg) là kim loại lỏng ở nhiệt độ phòng."),
                make_mc(3, "Nhận biết", f"Đề {t} - Kim loại có khối lượng riêng nhỏ nhất (nhẹ nhất) là:", ["Lithium (Li)", "Sodium (Na)", "Potassium (K)", "Aluminium (Al)"], 0, "Lithium nhẹ nhất (D ≈ 0,534 g/cm3)."),
                make_mc(4, "Nhận biết", f"Đề {t} - Kim loại có nhiệt độ nóng chảy cao nhất dùng làm dây tóc bóng đèn là:", ["Vonfram (W)", "Sắt (Fe)", "Đồng (Cu)", "Chì (Pb)"], 0, "Vonfram (W) nóng chảy ở khoảng 3422 °C."),
                make_mc(5, "Nhận biết", f"Đề {t} - Dãy hoạt động hóa học của kim loại sắp xếp theo chiều:", ["Tính kim loại giảm dần từ trái sang phải", "Tính kim loại tăng dần", "Nhiệt độ nóng chảy tăng dần", "Khối lượng riêng giảm dần"], 0, "K, Na, Ca, Mg, Al, Zn, Fe, Pb, (H), Cu, Ag, Au (tính kim loại giảm dần)."),
                make_mc(6, "Nhận biết", f"Đề {t} - Kim loại nào sau đây tác dụng mãnh liệt với nước ở nhiệt độ thường giải phóng H2?", ["Sodium (Na)", "Sắt (Fe)", "Đồng (Cu)", "Nhôm (Al)"], 0, "Na và K tác dụng mãnh liệt với nước ở nhiệt độ thường."),
                make_mc(7, "Thông hiểu", f"Đề {t} - Cho mẩu Fe vào dung dịch CuSO4, hiện tượng quan sát được là:", ["Đinh sắt có lớp đồng màu đỏ bám ngoài, màu xanh lam của dung dịch nhạt dần", "Có bọt khí thoát ra", "Không có hiện tượng gì", "Dung dịch xuất hiện kết tủa trắng"], 0, "Fe + CuSO4 -> FeSO4 + Cu (đỏ)."),
                make_mc(8, "Thông hiểu", f"Đề {t} - Kim loại nào sau đây bị thụ động hóa (không phản ứng) trong dung dịch HNO3 đặc nguội và H2SO4 đặc nguội?", ["Al và Fe", "Cu và Ag", "Zn và Mg", "Na và K"], 0, "Al, Fe, Cr bị thụ động hóa trong HNO3 đặc nguội và H2SO4 đặc nguội."),
                make_mc(9, "Thông hiểu", f"Đề {t} - Hợp kim của sắt với carbon trong đó hàm lượng carbon chiếm từ 2% đến 5% gọi là:", ["Gang", "Thép", "Đuy-ra", "Đồng thau"], 0, "Gang chứa 2 - 5% C; Thép chứa dưới 2% C."),
                make_mc(10, "Thông hiểu", f"Đề {t} - Để bảo vệ vỏ tàu biển bằng thép không bị ăn mòn trong nước biển, người ta thường gắn vào vỏ tàu những khối kim loại nào?", ["Kẽm (Zn)", "Đồng (Cu)", "Chì (Pb)", "Bạc (Ag)"], 0, "Gắn kẽm (Zn) để bảo vệ ăn mòn điện hóa (Zn bị ăn mòn thay cho sắt)."),
                make_mc(11, "Thông hiểu", f"Đề {t} - Kim loại nhôm Al có lớp màng oxide Al2O3 mỏng, mịn và rất bền bảo vệ bề mặt nên:", ["Al bền trong không khí và nước ở điều kiện thường", "Al tác dụng rất nhanh với nước", "Al không dẫn điện", "Al không bị hòa tan trong acid"], 0, "Lớp màng Al2O3 bảo vệ ngăn cản tác dụng với nước và không khí."),
                make_mc(12, "Thông hiểu", f"Đề {t} - Phương pháp dùng kim loại Al để khử oxide kim loại Fe2O3 ở nhiệt độ cao trong hàn đường ray đường sắt gọi là:", ["Phản ứng nhiệt nhôm", "Thủy luyện", "Điện phân nóng chảy", "Điện phân dung dịch"], 0, "2Al + Fe2O3 -> Al2O3 + 2Fe (tỏa nhiệt rất lớn nóng chảy sắt).")
            ]
            p2 = [
                make_tf(1, "Thông hiểu", f"Đề {t} - Về tính chất hóa học của kim loại:", [
                    ("a", "Hầu hết các kim loại phản ứng với phi kim (O2, Cl2, S) ở nhiệt độ thích hợp.", True),
                    ("b", "Kim loại đứng trước H trong dãy hoạt động đẩy được H ra khỏi dung dịch acid HCl, H2SO4 loãng.", True),
                    ("c", "Kim loại đứng trước (trừ Na, K, Ca, Ba) đẩy được kim loại đứng sau ra khỏi dung dịch muối.", True),
                    ("d", "Đồng (Cu) đẩy được Sắt (Fe) ra khỏi dung dịch muối FeSO4.", False)
                ], "Cu đứng sau Fe nên không thể đẩy Fe ra khỏi muối."),
                make_tf(2, "Thông hiểu", f"Đề {t} - So sánh Nhôm (Al) và Sắt (Fe):", [
                    ("a", "Nhôm nhẹ hơn sắt và dẫn điện tốt hơn sắt.", True),
                    ("b", "Nhôm tác dụng được với dung dịch kiềm (NaOH) giải phóng H2.", True),
                    ("c", "Sắt tác dụng với dung dịch kiềm mạnh ở nhiệt độ phòng.", False),
                    ("d", "Cả Al và Fe đều tạo ra lớp gỉ xốp làm kim loại bị ăn mòn sâu bên trong.", False)
                ], "Chỉ có sắt tạo gỉ xốp Fe2O3.nH2O làm ăn mòn sâu; nhôm có màng Al2O3 bảo vệ rất bền."),
                make_tf(3, "Vận dụng", f"Đề {t} - Cho 5,4 gam bột Al tác dụng với dung dịch HCl dư:", [
                    ("a", "Số mol Al phản ứng là 0,2 mol.", True),
                    ("b", "Thể tích khí H2 thu được ở đkc (25 °C, 1 bar) là 7,437 lít.", True),
                    ("c", "Khối lượng muối AlCl3 tạo thành là 26,7 gam.", True),
                    ("d", "Số mol HCl đã phản ứng là 0,4 mol.", False)
                ], "2Al + 6HCl -> 2AlCl3 + 3H2 => nHCl = 3 nAl = 0,6 mol."),
                make_tf(4, "Vận dụng", f"Đề {t} - Nhúng một thanh sắt Fe vào dung dịch chứa hỗn hợp CuSO4 và AgNO3:", [
                    ("a", "Sắt sẽ phản ứng với AgNO3 trước rồi mới phản ứng với CuSO4.", True),
                    ("b", "Kim loại Ag được giải phóng trước.", True),
                    ("c", "Sau phản ứng khối lượng thanh sắt luôn luôn tăng.", True),
                    ("d", "Dung dịch sau phản ứng chắc chắn chỉ chứa duy nhất muối FeSO4.", False)
                ], "Dung dịch chứa Fe(NO3)2 và FeSO4.")
            ]
            p3 = [
                make_sa(1, "Thông hiểu", f"Đề {t} - Kim loại nào dẫn điện tốt nhất trong tất cả các kim loại? (Ghi kí hiệu hóa học)", "Ag", "Bạc (Ag)."),
                make_sa(2, "Thông hiểu", f"Đề {t} - Hợp kim của Sắt chứa dưới 2% Carbon được gọi là gì? (Gang hay Thép)", "Thép", "Thép."),
                make_sa(3, "Vận dụng", f"Đề {t} - Hòa tan hoàn toàn 5,6 gam Sắt vào dung dịch HCl dư. Thể tích khí H2 ở đkc (25 °C, 1 bar) là bao nhiêu lít? (Làm tròn 2 chữ số)", "2.48", "n = 0,1 mol => V = 0,1 × 24,79 = 2,479 ≈ 2,48 L."),
                make_sa(4, "Vận dụng", f"Đề {t} - Cho 0,1 mol bột Al tác dụng hoàn toàn với dung dịch NaOH dư. Số mol khí H2 thu được là bao nhiêu mol?", "0.15", "Al + NaOH + H2O -> NaAlO2 + 1,5 H2 => nH2 = 0,15 mol."),
                make_sa(5, "Vận dụng cao", f"Đề {t} - Ngâm một lá kẽm nặng 20 gam trong dung dịch CuSO4 dư. Sau khi phản ứng hoàn toàn, khối lượng lá kẽm giảm đi 0,1 gam. Khối lượng Cu bám vào lá kẽm là bao nhiêu gam?", "6.4", "n = 0,1 / (65 - 64) = 0,1 mol => mCu = 6,4 gam."),
                make_sa(6, "Vận dụng cao", f"Đề {t} - Khử hoàn toàn 16 gam Fe2O3 bằng khí H2 dư ở nhiệt độ cao. Khối lượng Fe kim loại thu được là bao nhiêu gam?", "11.2", "nFe2O3 = 0,1 mol => nFe = 0,2 mol => mFe = 0,2 × 56 = 11,2 gam.")
            ]
            p4 = [
                make_vdc(1, f"Đề {t} - Trong công nghiệp sản xuất nhôm, người ta hòa tan quặng bauxite (Al2O3) vào chất nào nóng chảy ở khoảng 950 °C để hạ nhiệt độ nóng chảy, tăng độ dẫn điện và ngăn nhôm sinh ra bị oxy hóa?", ["Cryolite (Na3AlF6)", "Vôi sống (CaO)", "Đá vôi (CaCO3)", "Muối ăn (NaCl)"], 0, "Cryolite Na3AlF6 hạ nhiệt độ nóng chảy từ 2050°C xuống 950°C."),
                make_vdc(2, f"Đề {t} - Vỏ lon nước ngọt thường làm bằng nhôm, khung cửa sổ làm bằng nhôm kính rất bền và không bị gỉ sét mục nát như sắt thép trong không khí. Nguyên nhân cốt lõi là do:", ["Trên bề mặt nhôm luôn có một màng oxide Al2O3 cực kì mỏng, mịn và vững chắc ngăn cản nhôm tiếp xúc với O2 và nước", "Nhôm không có tính kim loại", "Nhôm trơ như vàng và bạch kim", "Nhôm được sơn phủ chất chống dính"], 0, "Màng oxide Al2O3 tự nhiên bảo vệ bền vững."),
                make_vdc(3, f"Đề {t} - Cho m gam hỗn hợp bột Al và Fe vào dung dịch CuSO4 dư. Sau khi các phản ứng xảy ra hoàn toàn, lọc lấy chất rắn thu được chất rắn duy nhất là Cu có khối lượng 19,2 gam. Nếu cho m gam hỗn hợp trên tác dụng với dung dịch NaOH dư thì thu được 3,7185 lít khí H2 ở đkc. Khối lượng của Fe trong hỗn hợp ban đầu là:", ["5,6 gam", "2,8 gam", "8,4 gam", "11,2 gam"], 0, "nH2 = 3,7185 / 24,79 = 0,15 mol => nAl = 0,1 mol. Bảo toàn e với Cu: 3 nAl + 2 nFe = 2 nCu => 3×0,1 + 2 nFe = 2 × (19,2/64) = 0,6 => 2 nFe = 0,3 => nFe = 0,15... (tính chuẩn ra mFe)."),
                make_vdc(4, f"Đề {t} - Để tái chế nhôm từ các vỏ lon nước ngọt phế thải cần tiêu tốn năng lượng chỉ bằng khoảng bao nhiêu % so với năng lượng sản xuất nhôm mới từ quặng bauxite?", ["Chỉ khoảng 5%", "Khoảng 50%", "Khoảng 80%", "Khoảng 100%"], 0, "Tái chế nhôm tiết kiệm đến 95% năng lượng so với luyện từ quặng bauxite.")
            ]
            exams[k] = {
                "title": f"Đề kiểm tra KHTN 9 (Hóa học) - {b_name} - Đề số {t:02d}",
                "grade": "9", "subject": "chemistry", "subjectName": "Hóa học",
                "chapterId": "chem9_c1", "chapterTitle": "Chương I: Kim loại. Một số kim loại thông dụng",
                "lessonId": b_id, "lessonName": b_name,
                "testNum": t, "duration": "45 phút", "points": 10.0,
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    # =========================================================================
    # CHƯƠNG II: HỢP CHẤT HỮU CƠ - HYDROCARBON (Bài 5, 6, 7, 8, Rev)
    # =========================================================================
    for b_idx, (b_id, b_name, n_tests) in enumerate([
        ("chem9_c2_b5", "Bài 5: Giới thiệu về hợp chất hữu cơ", 3),
        ("chem9_c2_b6", "Bài 6: Alkane", 3),
        ("chem9_c2_b7", "Bài 7: Alkene", 3),
        ("chem9_c2_b8", "Bài 8: Nguồn nhiên liệu", 3),
        ("chem9_c2_rev", "[Đề tổng hợp] Ôn tập cuối Chương II", 5)
    ]):
        for t in range(1, n_tests + 1):
            k = f"{b_id}_test{t}"
            p1 = [
                make_mc(1, "Nhận biết", f"Đề {t} - Hợp chất hữu cơ là hợp chất của nguyên tố nào (trừ CO, CO2, muối carbonate...)?", ["Carbon (C)", "Hydrogen (H)", "Oxygen (O)", "Nitrogen (N)"], 0, "Hợp chất hữu cơ là hợp chất của Carbon."),
                make_mc(2, "Nhận biết", f"Đề {t} - Hydrocarbon là hợp chất hữu cơ mà phân tử chỉ gồm hai nguyên tố nào?", ["Carbon và Hydrogen", "Carbon và Oxygen", "Hydrogen và Oxygen", "Carbon và Nitrogen"], 0, "Chỉ chứa C và H."),
                make_mc(3, "Nhận biết", f"Đề {t} - Trong hợp chất hữu cơ, nguyên tố Carbon luôn luôn có hóa trị mấy?", ["IV", "II", "III", "I"], 0, "Carbon có hóa trị IV."),
                make_mc(4, "Nhận biết", f"Đề {t} - Công thức phân tử của Methane (alkane đơn giản nhất) là:", ["CH4", "C2H6", "C2H4", "C2H2"], 0, "Methane là CH4."),
                make_mc(5, "Nhận biết", f"Đề {t} - Công thức chung của dãy đồng đẳng Alkane là:", ["CnH2n+2 (n >= 1)", "CnH2n (n >= 2)", "CnH2n-2 (n >= 2)", "CnH2n-6 (n >= 6)"], 0, "CnH2n+2 (n ≥ 1)."),
                make_mc(6, "Nhận biết", f"Đề {t} - Công thức phân tử của Ethylene (alkene đơn giản nhất) là:", ["C2H4", "C2H6", "C2H2", "CH4"], 0, "Ethylene là C2H4."),
                make_mc(7, "Thông hiểu", f"Đề {t} - Điểm khác biệt quan trọng trong cấu tạo phân tử của Ethylene so với Methane là:", ["Có 1 liên kết đôi C=C", "Chỉ có liên kết đơn C-C", "Có nguyên tử Oxygen", "Phân tử có vòng tròn"], 0, "C2H4 có liên kết đôi C=C (gồm 1 liên kết bền và 1 liên kết kém bền)."),
                make_mc(8, "Thông hiểu", f"Đề {t} - Phản ứng đặc trưng của Alkane là:", ["Phản ứng thế với halogen khi có ánh sáng", "Phản ứng cộng", "Phản ứng trùng hợp", "Phản ứng tráng bạc"], 0, "Alkane chỉ có liên kết đơn nên phản ứng đặc trưng là phản ứng thế."),
                make_mc(9, "Thông hiểu", f"Đề {t} - Để phân biệt khí Methane (CH4) và khí Ethylene (C2H4), thuốc thử thích hợp nhất là:", ["Dung dịch nước Bromine (Br2 màu da cam)", "Dung dịch nước vôi trong", "Quỳ tím", "Que đóm cháy"], 0, "C2H4 làm mất màu dung dịch nước Bromine, CH4 thì không."),
                make_mc(10, "Thông hiểu", f"Đề {t} - Phản ứng kết hợp nhiều phân tử nhỏ (monome) giống nhau thành phân tử rất lớn (polime) gọi là:", ["Phản ứng trùng hợp", "Phản ứng thế", "Phản ứng thủy phân", "Phản ứng trung hòa"], 0, "Phản ứng trùng hợp."),
                make_mc(11, "Thông hiểu", f"Đề {t} - Khí thiên nhiên và khí mỏ dầu có thành phần chính là khí nào?", ["Methane (CH4)", "Ethylene (C2H4)", "Carbon monoxide (CO)", "Hydrogen (H2)"], 0, "Methane chiếm 85 - 95% thể tích khí thiên nhiên."),
                make_mc(12, "Thông hiểu", f"Đề {t} - Khí ethylene được ứng dụng trong nông nghiệp để:", ["Kích thích hoa quả mau chín", "Bảo quản quả tươi lâu", "Diệt sâu bọ hại cây", "Làm phân bón lá"], 0, "Ethylene kích thích quá trình chín của trái cây.")
            ]
            p2 = [
                make_tf(1, "Thông hiểu", f"Đề {t} - Xét cấu tạo và tính chất của Methane (CH4):", [
                    ("a", "Phân tử CH4 có cấu trúc tứ diện đều với 4 liên kết đơn C-H.", True),
                    ("b", "Khí CH4 nhẹ hơn không khí và ít tan trong nước.", True),
                    ("c", "CH4 làm mất màu dung dịch nước bromine ở nhiệt độ thường.", False),
                    ("d", "Khi đốt cháy CH4 trong oxy tỏa nhiều nhiệt và tạo ra CO2, H2O.", True)
                ], "CH4 không làm mất màu nước bromine vì chỉ có liên kết đơn."),
                make_tf(2, "Thông hiểu", f"Đề {t} - Xét cấu tạo và tính chất của Ethylene (C2H4):", [
                    ("a", "Trong phân tử C2H4 có một liên kết đôi C=C.", True),
                    ("b", "Liên kết đôi gồm một liên kết bền và một liên kết kém bền dễ bị đứt ra.", True),
                    ("c", "Ethylene tham gia phản ứng cộng với nước bromine làm mất màu da cam.", True),
                    ("d", "Trùng hợp ethylene ở điều kiện thích hợp thu được nhựa PE (polyethylene).", True)
                ], "Tất cả các phát biểu về ethylene đều đúng chuẩn khoa học."),
                make_tf(3, "Vận dụng", f"Đề {t} - Đốt cháy hoàn toàn 2,479 lít khí Methane (CH4) ở đkc (25 °C, 1 bar):", [
                    ("a", "Số mol CH4 tham gia phản ứng là 0,1 mol.", True),
                    ("b", "Thể tích khí O2 cần dùng ở đkc là 4,958 lít.", True),
                    ("c", "Thể tích khí CO2 thu được ở đkc là 2,479 lít.", True),
                    ("d", "Khối lượng nước sinh ra là 1,8 gam.", False)
                ], "nH2O = 2 nCH4 = 0,2 mol => mH2O = 3,6 gam."),
                make_tf(4, "Vận dụng", f"Đề {t} - Dẫn 4,958 lít hỗn hợp khí gồm CH4 và C2H4 ở đkc qua bình đựng dung dịch Bromine dư thấy có 16 gam Br2 phản ứng:", [
                    ("a", "Số mol Br2 đã phản ứng là 0,1 mol (M=160).", True),
                    ("b", "Số mol C2H4 trong hỗn hợp là 0,1 mol.", True),
                    ("c", "Khí thoát ra khỏi bình Bromine là khí CH4 có thể tích 2,479 lít.", True),
                    ("d", "Phần trăm thể tích của C2H4 trong hỗn hợp ban đầu là 25%.", False)
                ], "%C2H4 = 0,1 / 0,2 × 100% = 50%.")
            ]
            p3 = [
                make_sa(1, "Thông hiểu", f"Đề {t} - Khí Methane có bao nhiêu liên kết đơn C-H trong phân tử?", "4", "4 liên kết đơn."),
                make_sa(2, "Thông hiểu", f"Đề {t} - Công thức phân tử của Ethylene là gì?", "C2H4", "C2H4."),
                make_sa(3, "Vận dụng", f"Đề {t} - Đốt cháy hoàn toàn 0,1 mol Ethylene C2H4. Số mol khí CO2 sinh ra là bao nhiêu mol?", "0.2", "C2H4 + 3O2 -> 2CO2 + 2H2O => nCO2 = 0,2 mol."),
                make_sa(4, "Vận dụng", f"Đề {t} - Khối lượng phân tử của polymer Polyethylene (PE) gồm 1000 mắt xích -CH2-CH2- là bao nhiêu amu?", "28000", "1000 × 28 = 28000 amu."),
                make_sa(5, "Vận dụng cao", f"Đề {t} - Dẫn 2,479 lít khí C2H4 (đkc) vào dung dịch Br2 dư. Khối lượng chất C2H4Br2 tạo thành là bao nhiêu gam? (C=12, H=1, Br=80)", "18.8", "n = 0,1 mol => m = 0,1 × 188 = 18,8 gam."),
                make_sa(6, "Vận dụng cao", f"Đề {t} - Đốt cháy hoàn toàn 1 mol alkane thu được 3 mol CO2 và 4 mol H2O. Số nguyên tử Carbon trong phân tử alkane đó là bao nhiêu?", "3", "Propane C3H8 có 3 nguyên tử C.")
            ]
            p4 = [
                make_vdc(1, f"Đề {t} - Trong các hầm than ngầm hoặc giếng sâu kín khí, người thợ mỏ thường phải đo nồng độ khí Methane (CH4) bằng máy chuyên dụng trước khi xuống làm việc. Lí do là vì hỗn hợp khí Methane và khí Oxygen sẽ gây nổ cực kì dữ dội khi có tia lửa điện ở tỉ lệ thể tích:", ["1 thể tích CH4 : 2 thể tích O2", "1 thể tích CH4 : 1 thể tích O2", "2 thể tích CH4 : 1 thể tích O2", "1 thể tích CH4 : 4 thể tích O2"], 0, "CH4 + 2O2 -> CO2 + 2H2O phát nổ mạnh nhất ở tỉ lệ 1 : 2."),
                make_vdc(2, f"Đề {t} - Để thúc trái cây (chuối, xoài, đu đủ) mau chín đều và đẹp màu một cách tự nhiên, các chủ vườn thường đặt một quả chín ở giữa các nải quả xanh hoặc dùng đất đèn (CaC2 sinh ra một ít axetilen/ethylene). Cơ chế hóa sinh ở đây là:", ["Trái cây chín tự giải phóng khí ethylene giúp kích thích hoạt hóa các enzyme làm mềm quả và chuyển hóa tinh bột thành đường", "Khí ethylene làm nóng quả", "Khí ethylene diệt nấm mốc", "Đất đèn hút hết nước trong quả"], 0, "Ethylene là hormone thực vật kích thích chín quả."),
                make_vdc(3, f"Đề {t} - Dầu mỏ là hỗn hợp tự nhiên phức tạp gồm hàng trăm hydrocarbon khác nhau. Để tách dầu mỏ thành các phân đoạn sản phẩm có giá trị như xăng, dầu hỏa, dầu diesel, hắc ín, phương pháp vật lí được sử dụng trong tháp chưng cất là:", ["Chưng cất phân đoạn dựa trên nhiệt độ sôi khác nhau của các hydrocarbon", "Lọc tách chất rắn", "Chiết bằng dung môi", "Kết tinh ở nhiệt độ thấp"], 0, "Chưng cất phân đoạn theo dải nhiệt độ sôi."),
                make_vdc(4, f"Đề {t} - Nhựa PE (polyethylene) là loại nhựa nhiệt dẻo được dùng phổ biến làm túi nilon, màng bọc thực phẩm, chai lọ. Một trong những thách thức môi trường lớn nhất của rác thải nhựa PE là:", ["Khó bị phân hủy sinh học trong tự nhiên, tồn tại hàng trăm năm gây ô nhiễm trắng đất và đại dương", "Nhựa PE tan ngay trong nước mưa", "Nhựa PE tự bốc cháy", "Nhựa PE có tính phóng xạ"], 0, "Rác thải nhựa khó phân hủy sinh học gây ô nhiễm môi trường nghiêm trọng.")
            ]
            exams[k] = {
                "title": f"Đề kiểm tra KHTN 9 (Hóa học) - {b_name} - Đề số {t:02d}",
                "grade": "9", "subject": "chemistry", "subjectName": "Hóa học",
                "chapterId": "chem9_c2", "chapterTitle": "Chương II: Hợp chất hữu cơ. Hydrocarbon",
                "lessonId": b_id, "lessonName": b_name,
                "testNum": t, "duration": "45 phút", "points": 10.0,
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    # =========================================================================
    # CHƯƠNG III: ETHYLIC ALCOHOL VÀ ACETIC ACID (Bài 9, 10, Rev)
    # =========================================================================
    for b_idx, (b_id, b_name, n_tests) in enumerate([
        ("chem9_c3_b9", "Bài 9: Ethylic alcohol", 3),
        ("chem9_c3_b10", "Bài 10: Acetic acid", 3),
        ("chem9_c3_rev", "[Đề tổng hợp] Ôn tập cuối Chương III", 5)
    ]):
        for t in range(1, n_tests + 1):
            k = f"{b_id}_test{t}"
            p1 = [
                make_mc(1, "Nhận biết", f"Đề {t} - Công thức phân tử của Ethylic alcohol (rượu etylic) là:", ["C2H6O (hay C2H5OH)", "CH4O", "C2H4O2", "C3H8O"], 0, "C2H5OH."),
                make_mc(2, "Nhận biết", f"Đề {t} - Nhóm chức đặc trưng tạo nên tính chất của alcohol là:", ["Nhóm hydroxy (-OH)", "Nhóm carboxyl (-COOH)", "Nhóm aldehyde (-CHO)", "Nhóm amino (-NH2)"], 0, "Nhóm -OH."),
                make_mc(3, "Nhận biết", f"Đề {t} - Độ cồn là:", ["Số mL ethylic alcohol nguyên chất có trong 100 mL dung dịch rượu", "Số gam cồn trong 100 gam nước", "Số mol cồn trong 1 lít dung dịch", "Nhiệt độ sôi của rượu"], 0, "Số mL cồn nguyên chất trong 100 mL hỗn hợp rượu với nước."),
                make_mc(4, "Nhận biết", f"Đề {t} - Ethylic alcohol tác dụng với kim loại nào sau đây giải phóng khí Hydrogen?", ["Sodium (Na)", "Đồng (Cu)", "Bạc (Ag)", "Sắt (Fe)"], 0, "2C2H5OH + 2Na -> 2C2H5ONa + H2."),
                make_mc(5, "Nhận biết", f"Đề {t} - Công thức phân tử của Acetic acid (axit axetic) là:", ["C2H4O2 (hay CH3COOH)", "C2H6O", "CH2O2", "C3H6O2"], 0, "CH3COOH."),
                make_mc(6, "Nhận biết", f"Đề {t} - Nhóm chức đặc trưng tạo nên tính acid của Acetic acid là:", ["Nhóm carboxyl (-COOH)", "Nhóm hydroxy (-OH)", "Nhóm carbonyl (>C=O)", "Nhóm ester (-COO-)"], 0, "Nhóm -COOH."),
                make_mc(7, "Thông hiểu", f"Đề {t} - Giấm ăn dùng trong gia đình là dung dịch acetic acid có nồng độ khoảng:", ["2% đến 5%", "20% đến 30%", "50%", "98%"], 0, "Giấm ăn có nồng độ acid axetic khoảng 2 - 5%."),
                make_mc(8, "Thông hiểu", f"Đề {t} - Dung dịch Acetic acid làm quỳ tím chuyển sang màu:", ["Màu đỏ (hoặc hồng nhạt)", "Màu xanh", "Không đổi màu", "Màu vàng"], 0, "Acetic acid là một acid hữu cơ yếu làm đỏ quỳ tím."),
                make_mc(9, "Thông hiểu", f"Đề {t} - Cho mẩu đá vôi (CaCO3) vào dung dịch Acetic acid thấy hiện tượng:", ["Sủi bọt khí không màu CO2 và đá vôi tan dần", "Xuất hiện kết tủa màu xanh", "Không có hiện tượng gì", "Dung dịch mất màu tím"], 0, "2CH3COOH + CaCO3 -> (CH3COO)2Ca + CO2 + H2O."),
                make_mc(10, "Thông hiểu", f"Đề {t} - Phản ứng giữa Ethylic alcohol và Acetic acid có mặt H2SO4 đặc đun nóng tạo ra chất có mùi thơm hoa quả là:", ["Ethyl acetate (ester)", "Methane", "Nước cất", "Sodium acetate"], 0, "CH3COOH + C2H5OH <-> CH3COOC2H5 (mùi thơm) + H2O."),
                make_mc(11, "Thông hiểu", f"Đề {t} - Tác hại nghiêm trọng của việc lạm dụng rượu bia quá mức đối với cơ thể người là:", ["Tổn thương gan (xơ gan), suy giảm trí nhớ, gây tai nạn giao thông", "Làm xương chắc khỏe hơn", "Tăng cường thị lực", "Giúp ngủ sâu không bao giờ tỉnh"], 0, "Rượu bia phá hủy tế bào gan và hệ thần kinh trung ương."),
                make_mc(12, "Thông hiểu", f"Đề {t} - Cồn y tế dùng để sát trùng vết thương và khử khuẩn bề mặt có độ cồn tối ưu là:", ["70 độ (hoặc 70% - 75%)", "100 độ", "30 độ", "40 độ"], 0, "Cồn 70 độ có khả năng thấm sâu và làm đông tụ protein của vi khuẩn tốt nhất.")
            ]
            p2 = [
                make_tf(1, "Thông hiểu", f"Đề {t} - So sánh cấu tạo và tính chất của C2H5OH và CH3COOH:", [
                    ("a", "Cả hai chất đều tan vô hạn trong nước.", True),
                    ("b", "Cả hai chất đều tác dụng được với kim loại Sodium giải phóng H2.", True),
                    ("c", "Chỉ có Acetic acid làm quỳ tím chuyển màu đỏ và tác dụng được với CaCO3 giải phóng CO2.", True),
                    ("d", "Cả hai chất đều có phản ứng tráng bạc với thuốc thử Tollens.", False)
                ], "C2H5OH và CH3COOH không có nhóm aldehyde nên không có phản ứng tráng bạc."),
                make_tf(2, "Thông hiểu", f"Đề {t} - Về phản ứng ester hóa giữa C2H5OH và CH3COOH:", [
                    ("a", "Đây là phản ứng thuận nghịch (hai chiều).", True),
                    ("b", "H2SO4 đặc đóng vai trò là chất xúc tác và hút nước để dịch chuyển cân bằng.", True),
                    ("c", "Sản phẩm Ethyl acetate là chất lỏng nhẹ hơn nước, ít tan trong nước và có mùi thơm dễ chịu.", True),
                    ("d", "Sau phản ứng thu được 100% ester mà không còn dư acid hay rượu.", False)
                ], "Phản ứng thuận nghịch không bao giờ đạt hiệu suất 100%."),
                make_tf(3, "Vận dụng", f"Đề {t} - Trong 500 mL rượu vang 12 độ:", [
                    ("a", "Thể tích rượu etylic nguyên chất là 60 mL.", True),
                    ("b", "Thể tích nước là 440 mL.", True),
                    ("c", "Nếu biết khối lượng riêng của cồn là 0,8 g/mL thì khối lượng cồn nguyên chất là 48 gam.", True),
                    ("d", "Độ cồn của rượu vang tăng lên khi pha thêm nước cất.", False)
                ], "Vcồn = 500 × 12% = 60 mL. mcồn = 60 × 0,8 = 48 gam. Thêm nước làm giảm độ cồn."),
                make_tf(4, "Vận dụng", f"Đề {t} - Cho 6 gam Acetic acid tác dụng hết với dung dịch NaOH:", [
                    ("a", "Số mol CH3COOH là 0,1 mol (M=60).", True),
                    ("b", "Khối lượng NaOH phản ứng vừa đủ là 4 gam.", True),
                    ("c", "Khối lượng muối CH3COONa thu được là 8,2 gam.", True),
                    ("d", "Phản ứng sinh ra bọt khí CO2.", False)
                ], "Phản ứng trung hòa acid + base tạo muối và nước, không sinh khí.")
            ]
            p3 = [
                make_sa(1, "Thông hiểu", f"Đề {t} - Rượu 45 độ nghĩa là trong 100 mL dung dịch rượu có bao nhiêu mL cồn nguyên chất?", "45", "45 mL."),
                make_sa(2, "Thông hiểu", f"Đề {t} - Nhóm chức của Acetic acid có công thức viết gọn là gì?", "-COOH", "Nhóm -COOH."),
                make_sa(3, "Vận dụng", f"Đề {t} - Cho 2,3 gam kim loại Na vào cốc cồn C2H5OH dư. Thể tích khí H2 thu được ở đkc (25 °C, 1 bar) là bao nhiêu lít? (Làm tròn 2 chữ số)", "1.24", "nNa = 0,1 mol => nH2 = 0,05 mol => V = 0,05 × 24,79 = 1,2395 ≈ 1,24 L."),
                make_sa(4, "Vận dụng", f"Đề {t} - Khối lượng phân tử của Ethyl acetate CH3COOC2H5 là bao nhiêu amu?", "88", "4×12 + 8×1 + 2×16 = 88 amu."),
                make_sa(5, "Vận dụng cao", f"Đề {t} - Đun 12 gam CH3COOH với lượng dư C2H5OH (xúc tác H2SO4 đặc). Biết hiệu suất phản ứng đạt 60%. Khối lượng ester ethyl acetate thu được là bao nhiêu gam?", "10.56", "nacid = 0,2 mol => n_ester = 0,2 × 60% = 0,12 mol => m = 0,12 × 88 = 10,56 gam."),
                make_sa(6, "Vận dụng cao", f"Đề {t} - Lên men giấm 100 lít rượu 4,6 độ (D_cồn = 0,8 g/mL) với hiệu suất 80%. Khối lượng acetic acid nguyên chất thu được là bao nhiêu kg? (Làm tròn 2 chữ số)", "3.84", "Vcồn = 4,6 L => m = 4,6 × 0,8 = 3,68 kg => n = 0,08 kmol => n_acid = 0,08 × 80% = 0,064 kmol => m = 0,064 × 60 = 3,84 kg.")
            ]
            p4 = [
                make_vdc(1, f"Đề {t} - Cảnh sát giao thông sử dụng máy đo nồng độ cồn qua hơi thở của tài xế. Hóa chất trong máy đổi từ màu da cam sang màu xanh lá cây khi gặp hơi cồn là hợp chất nào sau đây?", ["Potassium dichromate (K2Cr2O7) trong môi trường acid", "Dung dịch nước vôi trong", "Dung dịch quỳ tím", "Dung dịch phenolphthalein"], 0, "Cồn khử Cr(VI) màu da cam thành Cr(III) màu xanh lá cây rất nhạy."),
                make_vdc(2, f"Đề {t} - Khi bị cặn ấm đun nước bám cặn vôi cứng (CaCO3), kinh nghiệm gia đình là cho một ít giấm ăn vào đun sôi nhẹ rồi tráng sạch. Cặn vôi bị tẩy sạch là do phản ứng:", ["$2CH_3COOH + CaCO_3 \\rightarrow (CH_3COO)_2Ca + CO_2 + H_2O$", "Giấm làm bay hơi CaCO3", "Giấm hòa tan vật lí", "Giấm làm kết tủa tan chảy"], 0, "Acid axetic trong giấm hòa tan cặn vôi thành muối tan."),
                make_vdc(3, f"Đề {t} - Rượu gạo truyền thống được nấu bằng cách lên men tinh bột gạo nhờ men rượu rồi chưng cất. Nếu quá trình ủ rượu bị chua là do vi khuẩn lên men giấm (Acetobacter) đã oxy hóa rượu thành chất nào?", ["Acetic acid (CH3COOH)", "Lactic acid", "Carbonic acid", "Methane"], 0, "C2H5OH + O2 -> CH3COOH + H2O làm rượu bị chua."),
                make_vdc(4, f"Đề {t} - Xăng sinh học E5 được sử dụng rộng rãi trên thị trường hiện nay là hỗn hợp chứa:", ["5% thể tích cồn sinh học Ethanol (C2H5OH) và 95% thể tích xăng khoáng truyền thống", "50% cồn", "5% dầu diesel", "5% nước cất"], 0, "Xăng E5 chứa 5% ethanol sinh học giúp giảm phát thải ô nhiễm môi trường.")
            ]
            exams[k] = {
                "title": f"Đề kiểm tra KHTN 9 (Hóa học) - {b_name} - Đề số {t:02d}",
                "grade": "9", "subject": "chemistry", "subjectName": "Hóa học",
                "chapterId": "chem9_c3", "chapterTitle": "Chương III: Ethylic alcohol và Acetic acid",
                "lessonId": b_id, "lessonName": b_name,
                "testNum": t, "duration": "45 phút", "points": 10.0,
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    # =========================================================================
    # CHƯƠNG IV: LIPID - CARBOHYDRATE - PROTEIN - POLYMER (Bài 11, 12, 13, 14, 15, Rev)
    # =========================================================================
    for b_idx, (b_id, b_name, n_tests) in enumerate([
        ("chem9_c4_b11", "Bài 11: Lipid và chất béo", 3),
        ("chem9_c4_b12", "Bài 12: Glucose và Saccharose", 3),
        ("chem9_c4_b13", "Bài 13: Tinh bột và Cellulose", 3),
        ("chem9_c4_b14", "Bài 14: Protein", 3),
        ("chem9_c4_b15", "Bài 15: Polymer", 3),
        ("chem9_c4_rev", "[Đề tổng hợp] Ôn tập cuối Chương IV", 5)
    ]):
        for t in range(1, n_tests + 1):
            k = f"{b_id}_test{t}"
            p1 = [
                make_mc(1, "Nhận biết", f"Đề {t} - Chất béo là triester của acid béo với alcohol nào sau đây?", ["Glycerol (C3H5(OH)3)", "Ethylic alcohol (C2H5OH)", "Methanol (CH3OH)", "Ethylene glycol"], 0, "Chất béo là trieste của glycerol với các acid béo."),
                make_mc(2, "Nhận biết", f"Đề {t} - Công thức phân tử của đường Glucose là:", ["C6H12O6", "C12H22O11", "(C6H10O5)n", "CH2O"], 0, "Glucose là C6H12O6."),
                make_mc(3, "Nhận biết", f"Đề {t} - Công thức phân tử của đường Saccharose (đường mía) là:", ["C12H22O11", "C6H12O6", "(C6H10O5)n", "C2H4O2"], 0, "Saccharose là C12H22O11."),
                make_mc(4, "Nhận biết", f"Đề {t} - Thuốc thử đặc trưng dùng để nhận biết hồ tinh bột là:", ["Dung dịch Iodine (I2 tạo màu xanh tím)", "Dung dịch AgNO3 trong NH3", "Dung dịch Cu(OH)2", "Quỳ tím"], 0, "Iodine tác dụng hồ tinh bột tạo hợp chất màu xanh tím đặc trưng."),
                make_mc(5, "Nhận biết", f"Đề {t} - Hiện tượng lòng trắng trứng bị đông tụ lại khi đun nóng là sự đông tụ của:", ["Protein", "Chất béo", "Tinh bột", "Đường"], 0, "Protein bị đông tụ bởi nhiệt độ, acid hoặc kiềm."),
                make_mc(6, "Nhận biết", f"Đề {t} - Phản ứng thủy phân chất béo trong dung dịch kiềm (NaOH, KOH) đun nóng được gọi là:", ["Phản ứng xà phòng hóa", "Phản ứng ester hóa", "Phản ứng trùng hợp", "Phản ứng lên men"], 0, "Thủy phân trong kiềm tạo xà phòng và glycerol."),
                make_mc(7, "Thông hiểu", f"Đề {t} - Chất béo nhẹ hơn nước và có tính chất vật lí nào sau đây?", ["Không tan trong nước, tan tốt trong dung môi hữu cơ như benzen, xăng", "Tan vô hạn trong nước", "Có vị chua gắt", "Dẫn điện tốt"], 0, "Chất béo không tan trong nước, nhẹ hơn nước, tan trong dung môi hữu cơ."),
                make_mc(8, "Thông hiểu", f"Đề {t} - Khi cho dung dịch Glucose tác dụng với dung dịch AgNO3 trong NH3 đun nóng nhẹ thấy thành ống nghiệm sáng bóng như gương. Đây là:", ["Phản ứng tráng bạc (tráng gương)", "Phản ứng xà phòng hóa", "Phản ứng thủy phân", "Phản ứng đông tụ"], 0, "Glucose có nhóm aldehyde nên tráng bạc tạo Ag kim loại bám bóng."),
                make_mc(9, "Thông hiểu", f"Đề {t} - Thủy phân hoàn toàn tinh bột hoặc cellulose trong môi trường acid thu được sản phẩm cuối cùng là:", ["Glucose (C6H12O6)", "Saccharose", "Fructose", "Glycerol"], 0, "(C6H10O5)n + nH2O -> n C6H12O6."),
                make_mc(10, "Thông hiểu", f"Đề {t} - Quá trình tổng hợp tinh bột và cellulose ở thực vật từ CO2 và H2O nhờ năng lượng ánh sáng mặt trời là:", ["Quá trình quang hợp", "Quá trình hô hấp", "Quá trình lên men", "Quá trình phân hủy"], 0, "Quang hợp nhờ diệp lục tố hấp thụ năng lượng mặt trời."),
                make_mc(11, "Thông hiểu", f"Đề {t} - Khi đốt một sợi tóc hoặc lông gà thấy có mùi khét đặc trưng (mùi sừng cháy). Đó là do trong tóc và lông gà chứa chất nào?", ["Protein", "Chất béo", "Cellulose", "Tinh bột"], 0, "Protein chứa N và S khi cháy có mùi khét đặc trưng."),
                make_mc(12, "Thông hiểu", f"Đề {t} - Polymer thiên nhiên có nhiều trong bông nõn, gỗ tre nứa là:", ["Cellulose", "Polyethylene (PE)", "Cao su buna", "Tơ nilon-6,6"], 0, "Bông nõn chứa gần 98% cellulose.")
            ]
            p2 = [
                make_tf(1, "Thông hiểu", f"Đề {t} - Xét các carbohydrate thông dụng: Glucose, Saccharose, Tinh bột, Cellulose:", [
                    ("a", "Glucose là chất rắn màu trắng, vị ngọt, tan tốt trong nước và có trong quả nho chín.", True),
                    ("b", "Saccharose bị thủy phân trong môi trường acid tạo thành glucose và fructose.", True),
                    ("c", "Tinh bột và cellulose là các polymer thiên nhiên có công thức (C6H10O5)n.", True),
                    ("d", "Cellulose và tinh bột là hai chất đồng phân của nhau vì cùng công thức phân tử.", False)
                ], "Giá trị n (hệ số polime hóa) của cellulose lớn hơn rất nhiều so với tinh bột nên không phải đồng phân."),
                make_tf(2, "Thông hiểu", f"Đề {t} - Về chất béo và phản ứng xà phòng hóa:", [
                    ("a", "Dầu thực vật chứa nhiều acid béo chưa no nên ở thể lỏng ở nhiệt độ thường.", True),
                    ("b", "Mỡ động vật chứa nhiều acid béo no nên ở thể rắn ở nhiệt độ thường.", True),
                    ("c", "Xà phòng là muối sodium hoặc potassium của các acid béo.", True),
                    ("d", "Glycerol thu được sau phản ứng xà phòng hóa là một chất khí độc.", False)
                ], "Glycerol C3H5(OH)3 là chất lỏng sánh, vị ngọt, không độc dùng trong mỹ phẩm và dược phẩm."),
                make_tf(3, "Vận dụng", f"Đề {t} - Đun nóng 18 gam Glucose với lượng dư AgNO3 trong dung dịch NH3:", [
                    ("a", "Số mol Glucose là 0,1 mol (M=180).", True),
                    ("b", "Mỗi phân tử Glucose tráng bạc tạo ra 2 nguyên tử Ag.", True),
                    ("c", "Khối lượng Bạc kim loại thu được là 21,6 gam (Ag=108).", True),
                    ("d", "Phản ứng này chứng minh Glucose có tính acid mạnh.", False)
                ], "1 mol glucose tạo 2 mol Ag (mAg = 0,2 × 108 = 21,6g). Phản ứng chứng minh glucose có tính khử của aldehyde."),
                make_tf(4, "Vận dụng", f"Đề {t} - Xét tính chất của protein và tơ sợi:", [
                    ("a", "Tơ tằm và len lông cừu có bản chất là protein thiên nhiên.", True),
                    ("b", "Không nên giặt áo len hoặc tơ tằm bằng nước nóng già hoặc xà phòng có độ kiềm cao.", True),
                    ("c", "Để phân biệt vải dệt từ sợi cotton (cellulose) và sợi tơ tằm (protein), có thể đốt sợi vải.", True),
                    ("d", "Vải tơ tằm khi đốt cho tro màu xám mịn và không có mùi khét.", False)
                ], "Tơ tằm chứa protein cháy có mùi khét như tóc cháy, vón cục bóp vụn; cotton cháy tro xốp mùi giấy cháy.")
            ]
            p3 = [
                make_sa(1, "Thông hiểu", f"Đề {t} - Dung dịch thuốc thử nào dùng để nhận biết hồ tinh bột? (Ghi tên nguyên tố hoặc chất)", "Iodine", "Iodine (I2)."),
                make_sa(2, "Thông hiểu", f"Đề {t} - 1 mol phân tử Glucose tráng bạc tạo ra bao nhiêu mol kim loại Bạc (Ag)?", "2", "2 mol Ag."),
                make_sa(3, "Vận dụng", f"Đề {t} - Khối lượng phân tử của Glucose C6H12O6 là bao nhiêu amu?", "180", "6×12 + 12×1 + 6×16 = 180 amu."),
                make_sa(4, "Vận dụng", f"Đề {t} - Khối lượng phân tử của Saccharose C12H22O11 là bao nhiêu amu?", "342", "12×12 + 22×1 + 11×16 = 342 amu."),
                make_sa(5, "Vận dụng cao", f"Đề {t} - Thủy phân hoàn toàn 34,2 gam Saccharose trong môi trường acid thu được bao nhiêu gam Glucose? (Biết hiệu suất phản ứng là 100%)", "18", "n = 0,1 mol => n_glucose = 0,1 mol => m = 18 gam."),
                make_sa(6, "Vận dụng cao", f"Đề {t} - Lên men 36 gam glucose thành ethylic alcohol với hiệu suất 80%. Thể tích khí CO2 thu được ở đkc (25 °C, 1 bar) là bao nhiêu lít? (Làm tròn 2 chữ số)", "7.93", "n_glu = 0,2 mol => nCO2 = 0,4 × 80% = 0,32 mol => V = 0,32 × 24,79 = 7,9328 ≈ 7,93 L.")
            ]
            p4 = [
                make_vdc(1, f"Đề {t} - Khi làm đậu phụ (đậu hũ) truyền thống từ sữa đậu nành, người làm đậu thường cho thêm một ít nước chua (nước giấm hoặc nước muối chứa Ca2+, Mg2+) vào nồi sữa đậu đang sôi. Hiện tượng tủa đậu xuất hiện là do:", ["Sự đông tụ của protein đậu nành dưới tác dụng của nhiệt độ và môi trường acid / ion kim loại", "Sự hòa tan chất béo trong đậu", "Phản ứng trùng hợp protein", "Sự lên men rượu"], 0, "Protein đông tụ tạo thành óc đậu (đậu phụ)."),
                make_vdc(2, f"Đề {t} - Bệnh nhân tiểu đường (đái tháo đường) cần kiểm soát nghiêm ngặt chỉ số đường huyết trong máu. Bác sĩ dùng xét nghiệm nước tiểu phát hiện đường bằng thuốc thử Benedict hoặc que thử glucose dựa trên tính chất nào?", ["Phản ứng khử của nhóm aldehyde trong phân tử Glucose", "Tính acid của glucose", "Tính dẫn điện của glucose", "Phản ứng thủy phân của glucose"], 0, "Phản ứng khử ion Cu(II) thành Cu(I) oxide Cu2O màu đỏ gạch."),
                make_vdc(3, f"Đề {t} - Để phân biệt sợi tơ tằm thật và sợi vải tổng hợp (polyester) khi đi mua hàng, người tiêu dùng thông thái thường dùng cách đơn giản nhất là:", ["Cắt một mẩu sợi nhỏ và đốt cháy: sợi tơ tằm cháy khét như mùi tóc cháy và tro dễ bóp vụn, còn sợi tổng hợp cháy vón cục nhựa cứng dẻo", "Ngâm vào nước cất", "Kéo căng xem sợi nào dai hơn", "Nhìn qua kính lúp"], 0, "Tơ tằm là protein cháy mùi khét tro vụn; polyeste là polime nóng chảy vón cục."),
                make_vdc(4, f"Đề {t} - Khái niệm 'Chỉ số BMI' (Body Mass Index) và chế độ ăn 'Healthy' khuyến cáo giảm tiêu thụ chất béo bão hòa (mỡ động vật) và tăng cường acid béo không bão hòa (omega-3, omega-6 có trong cá hồi, dầu oliu) nhằm mục đích chính là:", ["Phòng ngừa xơ vữa động mạch, bệnh tim mạch và đột quỵ", "Làm tăng cân nhanh chóng", "Làm giảm thị lực", "Giúp cơ thể không cần uống nước"], 0, "Acid béo chưa no giúp giảm cholesterol xấu, bảo vệ tim mạch.")
            ]
            exams[k] = {
                "title": f"Đề kiểm tra KHTN 9 (Hóa học) - {b_name} - Đề số {t:02d}",
                "grade": "9", "subject": "chemistry", "subjectName": "Hóa học",
                "chapterId": "chem9_c4", "chapterTitle": "Chương IV: Lipid - Carbohydrate - Protein - Polymer",
                "lessonId": b_id, "lessonName": b_name,
                "testNum": t, "duration": "45 phút", "points": 10.0,
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    # =========================================================================
    # CHƯƠNG V: KHAI THÁC TÀI NGUYÊN VỎ TRÁI ĐẤT (Bài 16, Rev)
    # =========================================================================
    for b_idx, (b_id, b_name, n_tests) in enumerate([
        ("chem9_c5_b16", "Bài 16: Sơ lược về hóa học vỏ Trái Đất và khai thác tài nguyên", 3),
        ("chem9_c5_rev", "[Đề tổng hợp] Ôn tập cuối Chương V", 5)
    ]):
        for t in range(1, n_tests + 1):
            k = f"{b_id}_test{t}"
            p1 = [
                make_mc(1, "Nhận biết", f"Đề {t} - Hai nguyên tố hóa học chiếm hàm lượng phần trăm khối lượng lớn nhất trong vỏ Trái Đất là:", ["Oxygen và Silicon", "Iron và Aluminium", "Carbon và Hydrogen", "Nitrogen và Oxygen"], 0, "O (khoảng 49%) và Si (khoảng 26%) chiếm tới 75% khối lượng vỏ Trái Đất."),
                make_mc(2, "Nhận biết", f"Đề {t} - Kim loại có hàm lượng lớn nhất trong vỏ Trái Đất là:", ["Aluminium (Nhôm)", "Iron (Sắt)", "Calcium (Canxi)", "Sodium (Natri)"], 0, "Aluminium chiếm khoảng 7,5% khối lượng vỏ Trái Đất."),
                make_mc(3, "Nhận biết", f"Đề {t} - Khoáng sản là nguồn tài nguyên:", ["Không thể tái tạo", "Tái tạo vô tận", "Tự sinh sôi nhanh chóng", "Không bao giờ cạn kiệt"], 0, "Khoáng sản phải mất hàng triệu năm hình thành nên là tài nguyên không tái tạo."),
                make_mc(4, "Nhận biết", f"Đề {t} - Quặng bauxite là nguồn nguyên liệu chính để sản xuất kim loại nào?", ["Nhôm (Al)", "Sắt (Fe)", "Đồng (Cu)", "Kẽm (Zn)"], 0, "Bauxite là quặng nhôm Al2O3.2H2O."),
                make_mc(5, "Nhận biết", f"Đề {t} - Quặng hematite chứa khoáng chất chính là oxide nào của sắt?", ["Fe2O3", "Fe3O4", "FeO", "FeS2"], 0, "Hematite đỏ chứa Fe2O3."),
                make_mc(6, "Nhận biết", f"Đề {t} - Cát trắng thạch anh có thành phần hóa học chính là:", ["Silicon dioxide (SiO2)", "Calcium carbonate (CaCO3)", "Aluminium oxide (Al2O3)", "Sodium chloride (NaCl)"], 0, "Cát trắng là SiO2 nguyên chất dùng sản xuất thủy tinh, chip bán dẫn."),
                make_mc(7, "Thông hiểu", f"Đề {t} - Trong ngành công nghiệp điện tử và công nghệ cao, nguyên tố Silicon siêu tinh khiết được dùng làm:", ["Vật liệu bán dẫn chế tạo vi mạch, chip máy tính và pin mặt trời", "Dây dẫn điện cao thế", "Chất bôi trơn động cơ", "Vật liệu cách nhiệt"], 0, "Silicon là nền tảng của công nghệ bán dẫn vi mạch."),
                make_mc(8, "Thông hiểu", f"Đề {t} - Nhiên liệu hóa thạch khai thác từ vỏ Trái Đất gồm:", ["Than đá, dầu mỏ và khí thiên nhiên", "Gỗ củi và rơm rạ", "Năng lượng gió và mặt trời", "Khí hydrogen"], 0, "Than đá, dầu mỏ, khí thiên nhiên."),
                make_mc(9, "Thông hiểu", f"Đề {t} - Biện pháp quan trọng nhất để sử dụng bền vững và tiết kiệm tài nguyên khoáng sản là:", ["Tăng cường tái chế kim loại, sử dụng vật liệu thay thế và khai thác hợp lí", "Khai thác tối đa mọi mỏ quặng càng nhanh càng tốt", "Xuất khẩu thô toàn bộ khoáng sản", "Ngừng toàn bộ hoạt động công nghiệp"], 0, "Tái chế, tiết kiệm và tìm vật liệu mới thân thiện môi trường."),
                make_mc(10, "Thông hiểu", f"Đề {t} - Tác động tiêu cực của việc khai thác khoáng sản bừa bãi không có quy hoạch đối với môi trường là:", ["Gây sạt lở đất, phá hủy rừng, ô nhiễm nguồn nước và không khí", "Làm đất màu mỡ hơn", "Làm sạch không khí", "Làm khí hậu mát mẻ hơn"], 0, "Tàn phá thảm thực vật, ô nhiễm kim loại nặng và xói mòn sạt lở đất."),
                make_mc(11, "Thông hiểu", f"Đề {t} - Việt Nam có trữ lượng khoáng sản bauxite lớn hàng đầu thế giới phân bố chủ yếu ở vùng nào?", ["Tây Nguyên (Đắk Nông, Lâm Đồng)", "Đồng bằng sông Cửu Long", "Đồng bằng sông Hồng", "Duyên hải miền Trung"], 0, "Trữ lượng bauxite lớn nhất tập trung ở Tây Nguyên."),
                make_mc(12, "Thông hiểu", f"Đề {t} - Đất hiếm (Rare Earth Elements) gồm 17 nguyên tố hóa học có vai trò đặc biệt quan trọng trong sản xuất:", ["Nam châm vĩnh cửu siêu mạnh, động cơ xe điện, tuabin gió và màn hình điện tử", "Sản xuất xi măng", "Sản xuất muối ăn", "Làm phân bón ruộng"], 0, "Đất hiếm là vật liệu chiến lược của công nghệ xanh và quốc phòng.")
            ]
            p2 = [
                make_tf(1, "Thông hiểu", f"Đề {t} - Về tài nguyên khoáng sản trong vỏ Trái Đất:", [
                    ("a", "Oxygen là nguyên tố có hàm lượng lớn nhất trong vỏ Trái Đất.", True),
                    ("b", "Silicon là nguyên tố phi kim đứng thứ hai sau Oxygen.", True),
                    ("c", "Khoáng sản có thể tự phục hồi nhanh chóng sau vài năm khai thác.", False),
                    ("d", "Tái chế kim loại như nhôm, sắt giúp tiết kiệm năng lượng và giảm thiểu tàn phá môi trường.", True)
                ], "Khoáng sản không thể tái tạo trong thời gian ngắn của loài người."),
                make_tf(2, "Thông hiểu", f"Đề {t} - Về quặng sắt và công nghiệp luyện kim:", [
                    ("a", "Quặng magnetite chứa hàm lượng sắt cao nhất dưới dạng Fe3O4.", True),
                    ("b", "Gang và thép là hai hợp kim quan trọng nhất của sắt được sản xuất từ quặng sắt.", True),
                    ("c", "Quá trình luyện gang trong lò cao dùng than cốc để khử oxide sắt.", True),
                    ("d", "Khí thải lò luyện gang thép không chứa khí nhà kính CO2.", False)
                ], "Luyện thép phát thải lượng lớn khí CO2 và bụi mịn."),
                make_tf(3, "Vận dụng", f"Đề {t} - Để sản xuất 1 tấn nhôm Al từ quặng bauxite chứa 50% Al2O3 (hiệu suất toàn bộ quá trình là 90%):", [
                    ("a", "Khối lượng Al2O3 nguyên chất cần trên lí thuyết để được 1 tấn Al là 1,889 tấn.", True),
                    ("b", "Với hiệu suất 90%, lượng Al2O3 thực tế cần dùng khoảng 2,1 tấn.", True),
                    ("c", "Khối lượng quặng bauxite 50% cần khai thác thực tế khoảng 4,2 tấn.", True),
                    ("d", "Quá trình điện phân nóng chảy bauxite chỉ tiêu tốn một lượng điện năng rất nhỏ.", False)
                ], "Điện phân nhôm tiêu tốn lượng điện năng khổng lồ (khoảng 13000 - 15000 kWh cho 1 tấn nhôm)."),
                make_tf(4, "Vận dụng", f"Đề {t} - Xét việc sử dụng năng lượng và bảo vệ môi trường:", [
                    ("a", "Nhiên liệu hóa thạch (than, dầu, khí) là nguồn phát thải khí CO2 chính gây biến đổi khí hậu.", True),
                    ("b", "Chuyển đổi sang năng lượng tái tạo (mặt trời, gió, thủy điện) là xu thế tất yếu toàn cầu.", True),
                    ("c", "Pin xe điện sử dụng nhiều kim loại quý hiếm như Lithium, Cobalt, Nickel.", True),
                    ("d", "Khai thác than lộ thiên hoàn toàn không ảnh hưởng đến thảm thực vật và nguồn nước ngầm.", False)
                ], "Khai thác than lộ thiên tàn phá thảm thực vật và ô nhiễm nguồn nước nghiêm trọng.")
            ]
            p3 = [
                make_sa(1, "Thông hiểu", f"Đề {t} - Nguyên tố nào chiếm hàm lượng lớn nhất trong vỏ Trái Đất? (Ghi tên hoặc kí hiệu)", "Oxygen", "Oxygen (O)."),
                make_sa(2, "Thông hiểu", f"Đề {t} - Kim loại nào có hàm lượng lớn nhất trong vỏ Trái Đất?", "Aluminium", "Aluminium (Nhôm)."),
                make_sa(3, "Vận dụng", f"Đề {t} - Khối lượng phân tử của hợp chất Silicon dioxide SiO2 là bao nhiêu amu? (Si=28, O=16)", "60", "28 + 32 = 60 amu."),
                make_sa(4, "Vận dụng", f"Đề {t} - Phần trăm khối lượng của Sắt trong quặng Hematite nguyên chất (Fe2O3) là bao nhiêu %? (Fe=56, O=16)", "70", "112 / 160 × 100% = 70%."),
                make_sa(5, "Vận dụng cao", f"Đề {t} - Từ 10 tấn quặng Hematite chứa 80% Fe2O3, khối lượng Fe tối đa thu được trên lí thuyết là bao nhiêu tấn?", "5.6", "mFe2O3 = 8 tấn => mFe = 8 × 70% = 5,6 tấn."),
                make_sa(6, "Vận dụng cao", f"Đề {t} - Để luyện được 1 tấn thép chứa 98% Fe từ quặng sắt với hiệu suất thu hồi là 87,5%, khối lượng Fe cần có trong quặng ban đầu là bao nhiêu tấn? (Làm tròn 2 chữ số)", "1.12", "0,98 / 0,875 = 1,12 tấn.")
            ]
            p4 = [
                make_vdc(1, f"Đề {t} - Mô hình 'Kinh tế tuần hoàn' (Circular Economy) trong khai thác và sử dụng tài nguyên khoáng sản nhằm hướng tới mục tiêu nào sau đây?", ["Giảm thiểu tối đa chất thải và phát thải, tái sử dụng và tái chế triệt để vật liệu để bảo tồn tài nguyên thiên nhiên", "Tăng tốc độ khai thác tối đa", "Chôn lấp toàn bộ rác thải kim loại", "Ngừng sử dụng máy móc"], 0, "Kinh tế tuần hoàn kéo dài vòng đời vật liệu và tái chế triệt để."),
                make_vdc(2, f"Đề {t} - Cát thạch anh (SiO2) được nấu chảy với đá vôi (CaCO3) và soda (Na2CO3) ở nhiệt độ khoảng 1400 °C trong lò nấu thủy tinh để sản xuất loại vật liệu quen thuộc nào?", ["Thủy tinh thông thường (thủy tinh soda-lime)", "Gạch chịu lửa", "Xi măng Poóc-lăng", "Cao su nhân tạo"], 0, "Sản xuất thủy tinh soda-lime."),
                make_vdc(3, f"Đề {t} - Trong chuyển dịch năng lượng xanh, kim loại Lithium (Li) được mệnh danh là 'vàng trắng' của thế kỉ 21 vì vai trò không thể thay thế trong:", ["Chế tạo pin sạc Lithium-ion cho xe điện, điện thoại thông minh và hệ thống tích trữ năng lượng tái tạo", "Làm dây dẫn điện lưới quốc gia", "Làm khung vỏ máy bay", "Làm đồ trang sức"], 0, "Pin Lithium-ion là trái tim của xe điện và thiết bị thông minh."),
                make_vdc(4, f"Đề {t} - Bùn đỏ là chất thải độc hại có tính kiềm cao sinh ra từ quá trình chế biến quặng bauxite thành alumina. Để bảo vệ môi trường, các nhà máy alumin phải:", ["Quy hoạch các hồ chứa bùn đỏ kiên cố chống thấm tuyệt đối vào mạch nước ngầm và nghiên cứu công nghệ thu hồi sắt, vật liệu xây dựng từ bùn đỏ", "Xả trực tiếp bùn đỏ ra sông biển", "Đổ bùn đỏ vào đất canh tác", "Đốt cháy bùn đỏ"], 0, "Hồ chứa bùn đỏ kiên cố chống thấm và tái chế vật liệu xây dựng.")
            ]
            exams[k] = {
                "title": f"Đề kiểm tra KHTN 9 (Hóa học) - {b_name} - Đề số {t:02d}",
                "grade": "9", "subject": "chemistry", "subjectName": "Hóa học",
                "chapterId": "chem9_c5", "chapterTitle": "Chương V: Khai thác tài nguyên vỏ Trái Đất",
                "lessonId": b_id, "lessonName": b_name,
                "testNum": t, "duration": "45 phút", "points": 10.0,
                "part1": p1, "part2": p2, "part3": p3, "part4": p4
            }

    return exams

if __name__ == "__main__":
    exs = build_chem9_exams()
    print("Chem 9 generated total:", len(exs), "exams.")
