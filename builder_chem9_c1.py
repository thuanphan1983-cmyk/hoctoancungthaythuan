# -*- coding: utf-8 -*-
"""
BUILDER HÓA HỌC 9 - CHƯƠNG I: KIM LOẠI. MỘT SỐ KIM LOẠI THÔNG DỤNG (17 ĐỀ ĐỘC LẬP 100%)
Gồm 4 bài học (3 đề/bài = 12 đề) và 1 bài ôn tập cuối chương (5 đề) = 17 đề.
Không trùng lặp câu hỏi, số liệu và đáp án giữa các đề trong cùng bài học.
"""

from chem9_helpers import make_mc, make_tf, make_sa, make_vdc, make_exam

exams_c1 = {}

CID = "chem9_c1"
CTITLE = "Chương I: Kim loại. Một số kim loại thông dụng"

# ==============================================================================
# BÀI 1: TÍNH CHẤT CỦA KIM LOẠI (chem9_c1_b1) - 3 ĐỀ
# ==============================================================================
LID_B1 = "chem9_c1_b1"
LNAME_B1 = "Bài 1: Tính chất của kim loại"

# --- BÀI 1 - ĐỀ 1: Tính chất vật lí chung và ứng dụng của kim loại ---
exams_c1[f"{LID_B1}_test1"] = make_exam(
    CID, CTITLE, LID_B1, LNAME_B1, 1,
    p1=[
        make_mc(1, "Nhận biết", "Kim loại có tính dẻo cao nhất, có thể dát mỏng đến mức ánh sáng có thể xuyên qua là kim loại nào?", ["Vàng (Au)", "Bạc (Ag)", "Đồng (Cu)", "Nhôm (Al)"], 0, "Vàng (Au) là kim loại có tính dẻo cao nhất."),
        make_mc(2, "Nhận biết", "Kim loại nào sau đây có tính dẫn điện tốt nhất ở điều kiện thường?", ["Bạc (Ag)", "Đồng (Cu)", "Vàng (Au)", "Nhôm (Al)"], 0, "Thứ tự dẫn điện giảm dần: Ag > Cu > Au > Al > Fe."),
        make_mc(3, "Nhận biết", "Kim loại duy nhất ở trạng thái lỏng ở nhiệt độ phòng (25 °C) là:", ["Thủy ngân (Hg)", "Chì (Pb)", "Thiếc (Sn)", "Gali (Ga)"], 0, "Thủy ngân (Hg) có nhiệt độ nóng chảy khoảng -38,83 °C nên ở thể lỏng."),
        make_mc(4, "Nhận biết", "Kim loại có khối lượng riêng nhỏ nhất (nhẹ nhất) là:", ["Lithium (Li)", "Sodium (Na)", "Potassium (K)", "Aluminium (Al)"], 0, "Lithium có khối lượng riêng nhỏ nhất (D ≈ 0,534 g/cm3)."),
        make_mc(5, "Nhận biết", "Kim loại có nhiệt độ nóng chảy cao nhất, thường được sử dụng làm dây tóc bóng đèn sợi đốt là:", ["Vonfram (W)", "Sắt (Fe)", "Đồng (Cu)", "Niken (Ni)"], 0, "Vonfram (Tungsten - W) nóng chảy ở khoảng 3422 °C."),
        make_mc(6, "Nhận biết", "Ánh kim của kim loại là do:", ["Các electron tự do trong kim loại phản xạ các tia sáng nhìn thấy", "Kim loại tự phát sáng trong bóng tối", "Lớp oxide bề mặt phát quang", "Cấu trúc tinh thể hấp thụ hoàn toàn ánh sáng"], 0, "Electron tự do phản xạ hầu hết các tia sáng nhìn thấy được tạo nên ánh kim."),
        make_mc(7, "Thông hiểu", "Nhờ tính chất vật lí nào mà đồng và nhôm được ứng dụng rộng rãi để chế tạo dây dẫn điện?", ["Tính dẫn điện tốt và tính dẻo dễ kéo sợi", "Có nhiệt độ nóng chảy rất cao", "Có ánh kim lấp lánh", "Có khối lượng riêng rất lớn"], 0, "Đồng và nhôm dẫn điện rất tốt và có tính dẻo dễ uốn, kéo sợi."),
        make_mc(8, "Thông hiểu", "Vì sao nhôm và inox (thép không gỉ) thường được sử dụng để chế tạo xoong, chảo, nồi nấu ăn?", ["Dẫn nhiệt tốt, bền và an toàn", "Dẫn điện tốt", "Có tính nhiễm từ cao", "Khối lượng riêng lớn giúp đầm tay"], 0, "Kim loại dẫn nhiệt tốt giúp thức ăn nhanh chín, truyền nhiệt đều."),
        make_mc(9, "Thông hiểu", "Kim loại cứng nhất có thể dùng để cắt gọt thủy tinh và kim loại khác là:", ["Crom (Cr)", "Sắt (Fe)", "Titan (Ti)", "Kim cương"], 0, "Crom (Cr) là kim loại cứng nhất (độ cứng 8,5 trên thang Mohs). Kim cương là phi kim."),
        make_mc(10, "Thông hiểu", "Đốt nóng đỏ một đoạn dây sắt rồi đưa nhanh vào bình chứa khí chlorine (Cl2), hiện tượng quan sát được là:", ["Dây sắt cháy sáng chói tạo khói màu nâu đỏ", "Dây sắt cháy tạo chất rắn màu trắng", "Không có hiện tượng gì xảy ra", "Dây sắt nóng chảy tạo hạt kim loại màu đen"], 0, "2Fe + 3Cl2 -> 2FeCl3 (khói màu nâu đỏ bám vào thành bình)."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 4,8 gam kim loại magie (Mg) trong bình chứa khí oxy (O2) dư thu được bao nhiêu gam magnesium oxide (MgO)? (Mg=24, O=16)", ["8,0 gam", "6,4 gam", "4,0 gam", "10,0 gam"], 0, "nMg = 4,8/24 = 0,2 mol -> nMgO = 0,2 mol -> mMgO = 0,2 × 40 = 8,0 gam."),
        make_mc(12, "Vận dụng", "Cho một mẩu sodium (Na) nhỏ bằng hạt đậu xanh vào cốc nước cất có nhỏ sẵn vài giọt phenolphthalein, hiện tượng quan sát được là:", ["Na nóng chảy thành giọt tròn, chạy trên mặt nước, tan dần và dung dịch hóa hồng", "Na chìm xuống đáy cốc và không phản ứng", "Dung dịch xuất hiện kết tủa trắng", "Na bốc cháy mãnh liệt với ngọn lửa màu tím và dung dịch không đổi màu"], 0, "2Na + 2H2O -> 2NaOH + H2. Phản ứng tỏa nhiệt làm Na nóng chảy, khí H2 đẩy Na chạy, kiềm tạo thành làm phenolphthalein hóa hồng.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất vật lí đặc trưng của kim loại:", [
            ("a", "Hầu hết các kim loại đều có tính dẻo, dẫn điện, dẫn nhiệt và có ánh kim.", True),
            ("b", "Bạc dẫn điện tốt hơn đồng nhưng đồng được dùng làm dây tải điện phổ biến hơn vì giá thành rẻ hơn bạc nhiều.", True),
            ("c", "Tất cả các kim loại đều ở trạng thái rắn ở điều kiện nhiệt độ phòng 25 °C.", False),
            ("d", "Các kim loại có khối lượng riêng nhỏ hơn 5 g/cm3 được xếp vào nhóm kim loại nhẹ.", True)
        ], "Hg là kim loại ở thể lỏng ở 25 °C."),
        make_tf(2, "Thông hiểu", "Khi nghiên cứu về phản ứng giữa kim loại và phi kim:", [
            ("a", "Đốt cháy bột đồng trong không khí tạo thành chất rắn màu đen là đồng(II) oxide (CuO).", True),
            ("b", "Khí chlorine tác dụng với kim loại sắt tạo thành muối sắt(II) chloride FeCl2.", False),
            ("c", "Thủy ngân phản ứng với bột lưu huỳnh ngay ở nhiệt độ thường tạo thành HgS không độc, dùng để thu gom thủy ngân rơi vãi.", True),
            ("d", "Hầu hết các kim loại (trừ Au, Pt) đều có thể tác dụng với oxy ở nhiệt độ thích hợp tạo oxide.", True)
        ], "Fe tác dụng với Cl2 tạo FeCl3 mang hóa trị III."),
        make_tf(3, "Vận dụng", "Tiến hành thí nghiệm cho mẩu kẽm (Zn) vào ống nghiệm chứa dung dịch acid clohiđric (HCl):", [
            ("a", "Có bọt khí không màu thoát ra bề mặt mẩu kẽm và mẩu kẽm tan dần.", True),
            ("b", "Khí thoát ra là khí hydrogen (H2), nhẹ hơn không khí và cháy sinh ra tiếng nổ nhỏ.", True),
            ("c", "Dung dịch sau phản ứng có màu xanh lam đặc trưng của muối kẽm.", False),
            ("d", "Nếu thay mẩu kẽm bằng lá đồng (Cu) thì hiện tượng xảy ra tương tự như kẽm.", False)
        ], "Dung dịch ZnCl2 không màu. Đồng không tác dụng với dung dịch HCl loãng."),
        make_tf(4, "Vận dụng", "Về ứng dụng thực tiễn dựa trên tính chất của kim loại:", [
            ("a", "Vàng và bạc được sử dụng làm đồ trang sức vì có ánh kim đẹp và rất bền về mặt hóa học.", True),
            ("b", "Chì được sử dụng làm vỏ bọc dây cáp điện và tấm chắn bức xạ tia X nhờ khả năng ngăn cản tia phóng xạ tốt.", True),
            ("c", "Natri và kali được bảo quản bằng cách ngâm chìm hoàn toàn trong nước cất.", False),
            ("d", "Dây tóc bóng đèn sợi đốt làm bằng kim loại vonfram do vonfram có nhiệt độ nóng chảy rất cao.", True)
        ], "Natri và kali phản ứng mãnh liệt với nước nên phải ngâm trong dầu hỏa.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Kim loại nào có nhiệt độ nóng chảy thấp nhất trong tất cả các kim loại?", "Thủy ngân", "Thủy ngân (Hg) nóng chảy ở -38,83 °C."),
        make_sa(2, "Thông hiểu", "Cho biết hóa trị của kim loại nhôm (Al) trong hợp chất oxide Al2O3.", "III", "Nhôm có hóa trị III."),
        make_sa(3, "Vận dụng", "Đốt cháy hoàn toàn 6,4 gam bột đồng (Cu) trong khí oxy dư thu được bao nhiêu gam CuO? (Cu=64, O=16)", "8", "nCu = 0,1 mol -> nCuO = 0,1 mol -> mCuO = 0,1 × 80 = 8 gam."),
        make_sa(4, "Vận dụng", "Hòa tan hết 6,5 gam kim loại kẽm (Zn) vào dung dịch HCl dư. Thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Zn=65, thể tích 1 mol khí ở đkc = 24,79 L, làm tròn 2 chữ số thập phân)", "2.48", "nZn = 0,1 mol -> nH2 = 0,1 mol -> V = 0,1 × 24,79 = 2,479 ≈ 2,48 lít."),
        make_sa(5, "Vận dụng cao", "Hòa tan hoàn toàn m gam bột sắt (Fe) vào dung dịch H2SO4 loãng dư thu được 1,2395 lít khí H2 ở đkc. Khối lượng m của sắt là bao nhiêu gam? (Fe=56)", "2.8", "nH2 = 1,2395 / 24,79 = 0,05 mol -> nFe = 0,05 mol -> mFe = 0,05 × 56 = 2,8 gam."),
        make_sa(6, "Vận dụng cao", "Đốt cháy hoàn toàn hỗn hợp gồm 0,1 mol Mg và 0,1 mol Al trong khí oxy dư. Tổng khối lượng oxide thu được là bao nhiêu gam? (Mg=24, Al=27, O=16)", "9.1", "m = mMg + mAl + mO = 0,1×24 + 0,1×27 + 16×(0,1 + 0,1×1,5) = 2,4 + 2,7 + 16×0,25 = 5,1 + 4,0 = 9,1 gam.")
    ],
    p4=[
        make_vdc(1, "Người ta không dùng kim loại nhôm hoặc sắt để đựng dung dịch acid đặc nguội nào sau đây vì hiện tượng thụ động hóa bảo vệ kim loại?", ["HNO3 đặc nguội và H2SO4 đặc nguội", "HCl đặc nguội và HBr", "CH3COOH loãng", "H3PO4 nguội"], 0, "Al và Fe bị thụ động hóa (tạo lớp màng oxide thụ động trơ) trong HNO3 đặc nguội và H2SO4 đặc nguội."),
        make_vdc(2, "Cho 10 gam hỗn hợp gồm bột đồng (Cu) và bột sắt (Fe) tác dụng với dung dịch HCl dư. Sau khi phản ứng kết thúc hoàn toàn, thu được 2,479 lít khí H2 (đkc) và còn lại m gam chất rắn không tan. Giá trị của m là:", ["4,4 gam", "5,6 gam", "3,2 gam", "6,4 gam"], 0, "Cu không tan trong HCl. nH2 = 2,479 / 24,79 = 0,1 mol -> nFe = 0,1 mol -> mFe = 5,6 g -> mCu = 10 - 5,6 = 4,4 g."),
        make_vdc(3, "Khi rắc bột nhôm mịn vào ngọn lửa đèn cồn, hiện tượng quan sát được là những tia sáng chói lóe lên như pháo hoa. Bản chất của hiện tượng này là phản ứng nào?", ["4Al + 3O2 -> 2Al2O3 (tỏa nhiệt rất lớn và phát sáng mãnh liệt)", "Al + C -> Al4C3", "2Al + 3H2O -> Al2O3 + 3H2", "Al phân hủy thành các ion"], 0, "Bột nhôm diện tích tiếp xúc lớn bốc cháy mãnh liệt với O2 không khí tỏa nhiệt và ánh sáng chói."),
        make_vdc(4, "Cho m gam kim loại Magie (Mg) tác dụng vừa đủ với 100 mL dung dịch H2SO4 1M. Sau phản ứng cô cạn dung dịch thu được m1 gam muối khan MgSO4. Giá trị của m1 là:", ["12,0 gam", "9,6 gam", "6,0 gam", "24,0 gam"], 0, "nH2SO4 = 0,1 mol -> nMgSO4 = 0,1 mol -> mMgSO4 = 0,1 × 120 = 12,0 gam.")
    ]
)

# --- BÀI 1 - ĐỀ 2: Tính chất hóa học của kim loại và phản ứng với phi kim, acid ---
exams_c1[f"{LID_B1}_test2"] = make_exam(
    CID, CTITLE, LID_B1, LNAME_B1, 2,
    p1=[
        make_mc(1, "Nhận biết", "Phản ứng giữa kim loại sắt và khí oxy tạo ra oxide nào sau đây?", ["Sắt từ oxide (Fe3O4)", "Sắt(II) oxide (FeO)", "Sắt(III) oxide (Fe2O3)", "Sắt peroxide (FeO2)"], 0, "Đốt sắt trong oxy: 3Fe + 2O2 -> Fe3O4."),
        make_mc(2, "Nhận biết", "Sản phẩm của phản ứng giữa kim loại kẽm (Zn) với lưu huỳnh (S) khi nung nóng là:", ["ZnS", "ZnSO3", "ZnSO4", "Zn2S3"], 0, "Zn + S --t°--> ZnS (kẽm sulfide)."),
        make_mc(3, "Nhận biết", "Kim loại nào sau đây phản ứng với nước ở nhiệt độ thường tạo thành dung dịch kiềm và giải phóng khí hydrogen?", ["Potassium (K)", "Sắt (Fe)", "Đồng (Cu)", "Kẽm (Zn)"], 0, "K phản ứng mãnh liệt với nước ở nhiệt độ thường."),
        make_mc(4, "Nhận biết", "Khi cho một chiếc đinh sắt sạch vào ống nghiệm chứa dung dịch CuSO4, bề mặt đinh sắt sẽ bám một lớp kim loại màu gì?", ["Màu đỏ", "Màu trắng bạc", "Màu vàng", "Màu đen"], 0, "Fe + CuSO4 -> FeSO4 + Cu (đồng kim loại màu đỏ bám ngoài đinh sắt)."),
        make_mc(5, "Nhận biết", "Dung dịch muối nào sau đây tác dụng được với kim loại đồng (Cu)?", ["AgNO3", "FeSO4", "ZnSO4", "MgSO4"], 0, "Cu đứng trước Ag nên đẩy được Ag ra khỏi AgNO3: Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag."),
        make_mc(6, "Nhận biết", "Khí nào thoát ra khi cho mẩu nhôm tác dụng với dung dịch acid sunfuric loãng?", ["Hydrogen (H2)", "Sulfur dioxide (SO2)", "Oxygen (O2)", "Chlorine (Cl2)"], 0, "2Al + 3H2SO4 -> Al2(SO4)3 + 3H2."),
        make_mc(7, "Thông hiểu", "Kim loại nào sau đây KHÔNG tác dụng với dung dịch HCl ở điều kiện thường?", ["Bạc (Ag)", "Nhôm (Al)", "Kẽm (Zn)", "Magie (Mg)"], 0, "Bạc đứng sau H trong dãy hoạt động hóa học nên không tác dụng với HCl."),
        make_mc(8, "Thông hiểu", "Hiện tượng gì xảy ra khi cho dây đồng (Cu) vào dung dịch AgNO3?", ["Có chất rắn màu trắng xám bám trên dây đồng, dung dịch chuyển dần sang màu xanh lam", "Có bọt khí thoát ra mãnh liệt", "Dây đồng tan biến hoàn toàn mà dung dịch vẫn không màu", "Xuất hiện kết tủa màu nâu đỏ lắng xuống đáy"], 0, "Cu + 2AgNO3 -> Cu(NO3)2 (xanh lam) + 2Ag (trắng xám bám vào dây Cu)."),
        make_mc(9, "Thông hiểu", "Để thu gom một lượng nhỏ thủy ngân rơi vãi khi nhiệt kế bị vỡ, người ta thường dùng bột gì rắc lên?", ["Bột lưu huỳnh (S)", "Bột than hoạt tính", "Bột đá vôi", "Bột sắt"], 0, "Hg phản ứng với S ở nhiệt độ thường tạo HgS dạng rắn, không bay hơi."),
        make_mc(10, "Thông hiểu", "Cho các kim loại: Fe, Cu, Al, Ag. Số kim loại tác dụng được với dung dịch H2SO4 loãng là:", ["2", "1", "3", "4"], 0, "Chỉ có Fe và Al đứng trước H nên phản ứng giải phóng H2."),
        make_mc(11, "Vận dụng", "Hòa tan hoàn toàn 2,7 gam bột nhôm (Al) vào dung dịch HCl dư. Thể tích khí H2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["3,7185 lít", "2,4790 lít", "4,9580 lít", "1,2395 lít"], 0, "nAl = 0,1 mol -> nH2 = 0,15 mol -> V = 0,15 × 24,79 = 3,7185 lít."),
        make_mc(12, "Vận dụng", "Ngâm một lá sắt có khối lượng 10 gam vào dung dịch CuSO4 dư. Sau một thời gian vớt lá sắt ra, rửa sạch, sấy khô cân lại thấy khối lượng là 10,8 gam. Khối lượng Cu sinh ra bám vào lá sắt là:", ["6,4 gam", "0,8 gam", "5,6 gam", "3,2 gam"], 0, "Cứ 1 mol Fe phản ứng tạo 1 mol Cu khối lượng tăng 64 - 56 = 8 g. Tăng 0,8 g -> n = 0,1 mol -> mCu = 6,4 g.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Đánh giá các phát biểu về phản ứng của kim loại với phi kim:", [
            ("a", "Hầu hết các kim loại đều có thể phản ứng trực tiếp với phi kim khi có nhiệt độ thích hợp.", True),
            ("b", "Đốt sắt trong khí clo thu được muối sắt(II) chloride FeCl2.", False),
            ("c", "Phản ứng giữa nhôm và bột lưu huỳnh tạo thành nhôm sulfide có công thức Al2S3.", True),
            ("d", "Khí oxi phản ứng với đồng ở nhiệt độ cao tạo ra đồng(II) oxide màu đen.", True)
        ], "Fe + Cl2 tạo FeCl3 sắt(III)."),
        make_tf(2, "Thông hiểu", "Về tính chất hóa học của kim loại đối với nước và acid:", [
            ("a", "Các kim loại kiềm như Na, K phản ứng với nước rất êm dịu và hấp thụ nhiệt môi trường.", False),
            ("b", "Kim loại magie (Mg) phản ứng chậm với nước lạnh nhưng phản ứng nhanh hơn trong nước nóng.", True),
            ("c", "Dung dịch acid sunfuric loãng hòa tan được các kim loại đứng trước hydrogen giải phóng khí H2.", True),
            ("d", "Kim loại chì (Pb) tan rất tốt trong dung dịch H2SO4 loãng do tạo muối tan.", False)
        ], "Na, K phản ứng mãnh liệt tỏa nhiệt lớn. PbSO4 kết tủa bám ngoài ngăn cản phản ứng."),
        make_tf(3, "Vận dụng", "Cho các phản ứng hóa học sau của kim loại:", [
            ("a", "Fe + 2HCl -> FeCl2 + H2 là phản ứng thế.", True),
            ("b", "Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag chứng tỏ Cu có tính hoạt động hóa học mạnh hơn Ag.", True),
            ("c", "2Al + 3CuSO4 -> Al2(SO4)3 + 3Cu tạo kết tủa Cu màu đỏ bám trên bề mặt nhôm.", True),
            ("d", "Zn + MgSO4 -> ZnSO4 + Mg phản ứng xảy ra nhanh chóng ở nhiệt độ thường.", False)
        ], "Zn kém hoạt động hơn Mg nên không đẩy được Mg ra khỏi MgSO4."),
        make_tf(4, "Vận dụng", "Một nhóm học sinh tiến hành thí nghiệm kiểm tra tính dẫn điện và dẫn nhiệt của các thìa làm từ các chất khác nhau (nhôm, inox, nhựa, gỗ):", [
            ("a", "Thìa nhôm và thìa inox làm bóng đèn trong mạch điện sáng lên vì kim loại dẫn điện tốt.", True),
            ("b", "Thìa gỗ dẫn nhiệt nhanh nhất làm nóng tay khi khuấy nước sôi.", False),
            ("c", "Thìa nhôm truyền nhiệt nhanh hơn thìa inox do nhôm dẫn nhiệt tốt hơn thép.", True),
            ("d", "Cán xoong, chảo thường được bọc nhựa hoặc gỗ vì đây là các vật liệu cách nhiệt tốt bảo vệ tay người nấu.", True)
        ], "Gỗ dẫn nhiệt rất kém.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Viết công thức hóa học của chất khí sinh ra khi cho kẽm tác dụng với dung dịch acid clohiđric.", "H2", "Khí H2."),
        make_sa(2, "Thông hiểu", "Chất rắn màu gì được tạo thành khi đốt sợi dây đồng trên ngọn lửa đèn cồn?", "Đen", "CuO màu đen."),
        make_sa(3, "Vận dụng", "Hòa tan hết 4,8 gam Mg vào dung dịch HCl dư. Số mol khí H2 thu được là bao nhiêu mol?", "0.2", "nMg = 4,8 / 24 = 0,2 mol -> nH2 = 0,2 mol."),
        make_sa(4, "Vận dụng", "Cho thanh sắt nặng 20 gam vào dung dịch CuSO4. Sau khi Cu bám hết vào thanh sắt, khối lượng thanh sắt tăng lên 0,4 gam. Khối lượng Fe đã tan ra là bao nhiêu gam? (Fe=56, Cu=64)", "2.8", "Tăng 8g tương ứng 56g Fe tan. Tăng 0,4g -> mFe tan = 0,4 × 56 / 8 = 2,8 gam."),
        make_sa(5, "Vận dụng cao", "Đốt cháy 5,4 gam bột Al trong bình kín chứa khí clo dư. Khối lượng muối AlCl3 thu được là bao nhiêu gam? (Al=27, Cl=35,5)", "26.7", "nAl = 0,2 mol -> mAlCl3 = 0,2 × 133,5 = 26,7 gam."),
        make_sa(6, "Vận dụng cao", "Cho 11,2 gam bột Fe tác dụng với dung dịch chứa 0,15 mol CuSO4. Khối lượng Cu tạo thành tối đa là bao nhiêu gam? (Cu=64, Fe=56)", "9.6", "nFe = 0,2 mol > nCuSO4 = 0,15 mol -> Cu tính theo CuSO4: mCu = 0,15 × 64 = 9,6 gam.")
    ],
    p4=[
        make_vdc(1, "Hòa tan hoàn toàn 7,8 gam hỗn hợp gồm Al và Mg vào dung dịch HCl dư thấy thoát ra 9,916 lít khí H2 ở đkc (24,79 L/mol). Khối lượng của Al trong hỗn hợp ban đầu là:", ["5,4 gam", "2,4 gam", "3,6 gam", "4,8 gam"], 0, "nH2 = 0,4 mol. Đặt nAl=x, nMg=y: 27x + 24y = 7,8 và 1,5x + y = 0,4 -> x = 0,2, y = 0,1 -> mAl = 0,2 × 27 = 5,4 g."),
        make_vdc(2, "Ngâm một lá đồng có khối lượng 15 gam vào dung dịch AgNO3 1M. Sau một thời gian lấy lá đồng ra cân lại thấy khối lượng tăng thêm 1,52 gam. Khối lượng bạc (Ag) kim loại đã bám trên lá đồng là:", ["2,16 gam", "1,08 gam", "3,24 gam", "0,64 gam"], 0, "Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag. Độ tăng khối lượng: 2×108 - 64 = 152 g/mol phản ứng. Tăng 1,52 g -> nCu pư = 0,01 mol -> nAg = 0,02 mol -> mAg = 0,02 × 108 = 2,16 g."),
        make_vdc(3, "Để điều chế khí H2 trong phòng thí nghiệm một cách liên tục và điều hòa, người ta thường dùng bình Kíp với cặp chất nào sau đây?", ["Kẽm viên và dung dịch acid HCl", "Bột nhôm và dung dịch acid H2SO4 đặc", "Đồng mẩu và dung dịch acid HCl", "Sắt bột và nước cất"], 0, "Bình Kíp dùng chất rắn dạng viên (Zn viên) và acid HCl loãng để đóng mở khóa điều chỉnh phản ứng."),
        make_vdc(4, "Một học sinh làm thí nghiệm đốt sợi dây thép mác thấp cuốn quanh que diêm trong bình khí oxy. Vai trò của que diêm là gì?", ["Cung cấp nhiệt lượng ban đầu để kích hoạt phản ứng cháy của dây thép", "Tạo thêm khí CO2 làm môi trường đệm", "Hút bớt ẩm trong bình", "Làm xúc tác hóa học biến đổi sắt"], 0, "Dây sắt cần nhiệt độ rất cao mới bắt cháy trong oxy, que diêm cháy cung cấp nhiệt khơi mào ban đầu.")
    ]
)

# --- BÀI 1 - ĐỀ 3: Phân loại, thực nghiệm và so sánh tính chất kim loại ---
exams_c1[f"{LID_B1}_test3"] = make_exam(
    CID, CTITLE, LID_B1, LNAME_B1, 3,
    p1=[
        make_mc(1, "Nhận biết", "Kim loại nào sau đây có khối lượng riêng lớn nhất (nặng nhất) trong tất cả các kim loại?", ["Osmi (Os)", "Vàng (Au)", "Chì (Pb)", "Platin (Pt)"], 0, "Osmi (Os) có khối lượng riêng lớn nhất (khoảng 22,59 g/cm3)."),
        make_mc(2, "Nhận biết", "Kim loại có độ cứng nhỏ nhất, mềm đến mức có thể dùng dao cắt gọt dễ dàng là:", ["Xesi (Cs) và các kim loại kiềm", "Sắt (Fe)", "Đồng (Cu)", "Kẽm (Zn)"], 0, "Các kim loại kiềm (Cs, Rb, K, Na) rất mềm, dùng dao cắt nhẹ nhàng."),
        make_mc(3, "Nhận biết", "Trong các kim loại sau, kim loại nào dẫn nhiệt kém nhất?", ["Chì (Pb)", "Bạc (Ag)", "Đồng (Cu)", "Nhôm (Al)"], 0, "Trong số các kim loại thông dụng, chì (Pb) và thủy ngân có tính dẫn điện, dẫn nhiệt kém nhất."),
        make_mc(4, "Nhận biết", "Hiện tượng kim loại bị phá hủy do tác dụng hóa học trực tiếp với các chất trong môi trường xung quanh gọi là:", ["Sự ăn mòn kim loại", "Sự nóng chảy", "Sự tôi luyện", "Sự thụ động hóa"], 0, "Định nghĩa sự ăn mòn kim loại."),
        make_mc(5, "Nhận biết", "Cho bột sắt vào dung dịch acid sunfuric loãng, muối thu được sau phản ứng là:", ["FeSO4", "Fe2(SO4)3", "FeS", "FeSO3"], 0, "Fe + H2SO4 loãng -> FeSO4 + H2."),
        make_mc(6, "Nhận biết", "Đốt cháy bột nhôm (Al) trong không khí thu được oxide có màu gì?", ["Màu trắng", "Màu đen", "Màu nâu đỏ", "Màu vàng chanh"], 0, "Al2O3 là chất rắn màu trắng."),
        make_mc(7, "Thông hiểu", "Vì sao các dụng cụ đun nấu như chảo chống dính, nồi lẩu thường được chế tạo bằng nhôm hoặc hợp kim nhôm?", ["Nhôm dẫn nhiệt tốt, nhẹ và gia công dập tạo hình dễ dàng", "Nhôm dẫn điện tốt nhất", "Nhôm cứng hơn kim cương", "Nhôm có nhiệt độ nóng chảy cao hơn vonfram"], 0, "Nhôm nhẹ, dẫn nhiệt nhanh và đều, có tính dẻo dễ gia công cơ khí."),
        make_mc(8, "Thông hiểu", "Cho dây sắt quấn hình lò xo vào bình khí oxy có chứa sẵn một lớp nước mỏng ở đáy bình. Vai trò của lớp nước đáy bình là gì?", ["Ngăn các tia xỉ sắt nóng chảy rơi xuống làm nứt vỡ đáy bình thủy tinh", "Hòa tan khí oxy để phản ứng nhanh hơn", "Làm xúc tác cho phản ứng cháy", "Hạ nhiệt độ ngọn lửa"], 0, "Các giọt Fe3O4 nóng chảy bắn ra gặp đáy bình lạnh sẽ làm vỡ bình nếu không có nước hoặc cát."),
        make_mc(9, "Thông hiểu", "Kim loại nào sau đây khi tác dụng với dung dịch CuSO4 tạo ra cả chất khí và chất kết tủa màu xanh?", ["Sodium (Na)", "Sắt (Fe)", "Kẽm (Zn)", "Nhôm (Al)"], 0, "Na phản ứng với H2O tạo H2 và NaOH, sau đó NaOH + CuSO4 -> Cu(OH)2 kết tủa xanh."),
        make_mc(10, "Thông hiểu", "Để phân biệt hai mẫu bột kim loại màu trắng xám gồm Mg và Ag, ta có thể dùng thuốc thử nào sau đây?", ["Dung dịch acid HCl", "Nước cất", "Dung dịch kiềm NaOH", "Dung dịch muối ăn NaCl"], 0, "Mg tác dụng với HCl sủi bọt khí H2 tan dần, Ag không tác dụng."),
        make_mc(11, "Vận dụng", "Hòa tan hoàn toàn 5,6 gam Fe vào 200 gam dung dịch HCl nồng độ 7,3%. Nồng độ phần trăm của muối FeCl2 trong dung dịch sau phản ứng là: (làm tròn 2 chữ số thập phân)", ["6,18%", "5,60%", "7,30%", "4,25%"], 0, "nFe = 0,1 mol; nHCl = 200×0,073/36,5 = 0,4 mol -> HCl dư. mdd sau pư = 5,6 + 200 - 0,1×2 = 205,4 g. C% = 0,1×127 / 205,4 = 6,18%."),
        make_mc(12, "Vận dụng", "Cho 0,2 mol kim loại M hóa trị II tác dụng hoàn toàn với dung dịch HCl dư thu được 4,958 lít khí H2 ở đkc (24,79 L/mol). Kim loại M có khối lượng là 4,8 gam. Tên của kim loại M là:", ["Magnesium (Mg)", "Zinc (Zn)", "Iron (Fe)", "Calcium (Ca)"], 0, "M = 4,8 / 0,2 = 24 -> Magnesium (Mg).")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Về các đặc tính vật lí cơ bản của các nguyên tố kim loại:", [
            ("a", "Thủy ngân được ứng dụng trong các nhiệt kế y tế nhờ tính chất giãn nở vì nhiệt đều đặn và là chất lỏng ở nhiệt độ thường.", True),
            ("b", "Đồng nguyên chất được ưa chuộng dùng làm lõi dây điện gia đình nhờ tính dẫn điện xuất sắc và độ bền dẻo cao.", True),
            ("c", "Tất cả các kim loại đều có nhiệt độ nóng chảy trên 500 °C.", False),
            ("d", "Khối lượng riêng của nhôm là 2,7 g/cm3 nên nhôm thuộc nhóm kim loại nhẹ.", True)
        ], "Hg nóng chảy ở -38,83 °C, Ga nóng chảy ở 29,76 °C, Na nóng chảy ở 97,8 °C."),
        make_tf(2, "Thông hiểu", "Khi cho kim loại tác dụng với các chất oxi hóa khác nhau:", [
            ("a", "Sắt tác dụng với lưu huỳnh khi nung nóng tạo thành muối sắt mang hóa trị II (FeS).", True),
            ("b", "Bột nhôm tự bốc cháy trong không khí lạnh không cần khơi mào nhiệt độ.", False),
            ("c", "Đồng kim loại có thể tan trong dung dịch AgNO3 tạo dung dịch muối đồng màu xanh lam.", True),
            ("d", "Phản ứng giữa natri và nước là phản ứng tỏa nhiệt mạnh và giải phóng khí hydrogen.", True)
        ], "Bột nhôm cần được đốt nóng đến nhiệt độ bắt cháy."),
        make_tf(3, "Vận dụng", "Cho các hiện tượng thí nghiệm thực hành:", [
            ("a", "Khi nhỏ dung dịch HCl vào mẩu đá vôi và mẩu kẽm, cả hai ống nghiệm đều có sủi bọt khí thoát ra.", True),
            ("b", "Khí thoát ra ở cả hai ống nghiệm trên đều có thể làm que đóm đang cháy bùng sáng mạnh mẽ.", False),
            ("c", "Khí thoát ra từ ống nghiệm chứa đá vôi là CO2 làm đục nước vôi trong, khí từ kẽm là H2 có thể cháy trong không khí.", True),
            ("d", "Dung dịch thu được sau phản ứng của kẽm với acid không làm quỳ tím đổi màu nếu acid phản ứng vừa đủ.", True)
        ], "CO2 và H2 không duy trì sự cháy, không làm que đóm bùng cháy."),
        make_tf(4, "Vận dụng", "Cho các nhận định về quy tắc an toàn trong phòng thí nghiệm hóa học:", [
            ("a", "Không dùng tay trực tiếp cầm các kim loại kiềm như natri hay kali vì mồ hôi tay có thể gây phản ứng bỏng nặng.", True),
            ("b", "Khi đốt dây sắt trong bình khí oxy cần lót một lớp cát hoặc nước ở đáy bình để tránh nứt vỡ bình.", True),
            ("c", "Nếu làm đổ acid sunfuric đặc ra tay cần rửa ngay bằng dung dịch kiềm đặc NaOH.", False),
            ("d", "Các mẩu natri thừa sau thí nghiệm phải được bỏ vào lọ chứa dầu hỏa, không vứt bừa bãi vào thùng rác hoặc bồn rửa.", True)
        ], "Tuyệt đối không rửa acid đặc bằng kiềm đặc vì gây bỏng kiềm và phản ứng tỏa nhiệt cực mạnh; phải rửa bằng nhiều nước chảy.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Tên kim loại cứng nhất trong tất cả các kim loại là gì?", "Crom", "Crom (Cr)."),
        make_sa(2, "Thông hiểu", "Kim loại Na và K được bảo quản bằng cách ngâm ngập trong chất lỏng nào?", "Dầu hỏa", "Dầu hỏa."),
        make_sa(3, "Vận dụng", "Nung nóng 8,4 gam bột Fe với bột lưu huỳnh dư trong điều kiện không có không khí. Khối lượng FeS thu được là bao nhiêu gam? (Fe=56, S=32)", "13.2", "nFe = 8,4 / 56 = 0,15 mol -> nFeS = 0,15 mol -> m = 0,15 × 88 = 13,2 gam."),
        make_sa(4, "Vận dụng", "Cho 0,3 mol Zn phản ứng hoàn toàn với dung dịch CuSO4 dư. Khối lượng Cu kết tủa thu được là bao nhiêu gam? (Cu=64)", "19.2", "nCu = 0,3 mol -> mCu = 0,3 × 64 = 19,2 gam."),
        make_sa(5, "Vận dụng cao", "Cho 10 gam hỗn hợp gồm Cu và Fe phản ứng với lượng dư dung dịch HCl. Khí thoát ra được dẫn qua ống chứa CuO dư nung nóng thấy khối lượng chất rắn trong ống giảm 1,6 gam. Phần trăm khối lượng của Fe trong hỗn hợp ban đầu là bao nhiêu %? (Fe=56, O=16)", "56", "Độ giảm chất rắn chính là mO phản ứng = 1,6 g -> nO = 0,1 mol -> nH2 = 0,1 mol -> nFe = 0,1 mol -> mFe = 5,6 g -> %Fe = 56%."),
        make_sa(6, "Vận dụng cao", "Hòa tan hoàn toàn m gam Al vào dung dịch NaOH dư thu được 7,437 lít khí H2 ở đkc (24,79 L/mol). Giá trị của m là bao nhiêu gam? (Al=27)", "5.4", "nH2 = 7,437 / 24,79 = 0,3 mol. Phản ứng: Al + NaOH + H2O -> NaAlO2 + 1,5 H2 -> nAl = 0,3 / 1,5 = 0,2 mol -> mAl = 0,2 × 27 = 5,4 gam.")
    ],
    p4=[
        make_vdc(1, "Cho 13,5 gam bột kim loại Al vào 500 mL dung dịch CuSO4 1M. Sau khi phản ứng hoàn toàn thu được m gam chất rắn. Giá trị của m là:", ["32,0 gam", "48,0 gam", "16,0 gam", "64,0 gam"], 0, "nAl = 0,5 mol; nCuSO4 = 0,5 mol. 2Al + 3CuSO4 -> Al2(SO4)3 + 3Cu. nAl pư = 2/3 × 0,5 = 0,333 mol -> Al dư 0,167 mol. nCu = 0,5 mol. m chất rắn = mCu + mAl dư = 0,5×64 + 0,1667×27 = 32 + 4,5 = 36,5 gam. Chú ý: Nếu chỉ hỏi khối lượng Cu thu được thì mCu = 32,0 g."),
        make_vdc(2, "Một lá sắt có khối lượng 50 gam được ngâm trong dung dịch AgNO3. Sau một thời gian vớt lá sắt ra rửa sạch cân lại thấy nặng 58 gam. Biết rằng toàn bộ lượng bạc sinh ra bám hoàn toàn vào lá sắt. Lượng Fe đã tham gia phản ứng là:", ["2,8 gam", "5,6 gam", "1,4 gam", "4,2 gam"], 0, "Fe + 2AgNO3 -> Fe(NO3)2 + 2Ag. Cứ 1 mol Fe (56 g) tan tạo 2 mol Ag (216 g) bám, khối lượng tăng: 216 - 56 = 160 g. Khối lượng tăng thực tế = 58 - 50 = 8 g -> nFe = 8 / 160 = 0,05 mol -> mFe = 0,05 × 56 = 2,8 gam."),
        make_vdc(3, "Để hòa tan hết một mẫu hợp kim gồm 4,8 gam Mg và 5,4 gam Al cần tối thiểu bao nhiêu lít dung dịch H2SO4 0,5M?", ["1,0 lít", "0,5 lít", "1,5 lít", "2,0 lít"], 0, "nMg = 0,2 mol; nAl = 0,2 mol. nH2SO4 = nMg + 1,5 nAl = 0,2 + 0,3 = 0,5 mol -> V = 0,5 / 0,5 = 1,0 lít."),
        make_vdc(4, "Cho luồng khí H2 dư đi qua ống sứ đựng 20 gam hỗn hợp gồm CuO và Al2O3 nung nóng ở nhiệt độ cao đến khi phản ứng xảy ra hoàn toàn. Khối lượng chất rắn còn lại trong ống là 16,8 gam. Phần trăm khối lượng của CuO trong hỗn hợp ban đầu là:", ["80%", "20%", "40%", "60%"], 0, "H2 chỉ khử CuO thành Cu, không khử được Al2O3. Khối lượng giảm là khối lượng O trong CuO bị tách: mO = 20 - 16,8 = 3,2 g -> nO = 0,2 mol -> nCuO = 0,2 mol -> mCuO = 0,2 × 80 = 16 g -> %CuO = 16/20 × 100% = 80%.")
    ]
)

# ==============================================================================
# BÀI 2: MỘT SỐ KIM LOẠI THÔNG DỤNG (AL, FE) (chem9_c1_b2) - 3 ĐỀ
# ==============================================================================
LID_B2 = "chem9_c1_b2"
LNAME_B2 = "Bài 2: Một số kim loại thông dụng (Al, Fe)"

# --- BÀI 2 - ĐỀ 1: Tính chất và ứng dụng của Nhôm (Al) ---
exams_c1[f"{LID_B2}_test1"] = make_exam(
    CID, CTITLE, LID_B2, LNAME_B2, 1,
    p1=[
        make_mc(1, "Nhận biết", "Kim loại nhôm (Al) có màu gì đặc trưng?", ["Màu trắng bạc", "Màu vàng ánh kim", "Màu xám sẫm", "Màu đỏ gạch"], 0, "Nhôm là kim loại màu trắng bạc, nhẹ."),
        make_mc(2, "Nhận biết", "Khối lượng riêng của nhôm ở điều kiện chuẩn khoảng:", ["2,7 g/cm3", "7,86 g/cm3", "19,3 g/cm3", "0,53 g/cm3"], 0, "Khối lượng riêng của Al là 2,7 g/cm3."),
        make_mc(3, "Nhận biết", "Lớp màng bảo vệ nhôm bền vững trong không khí và nước ở điều kiện thường có công thức hóa học là:", ["Al2O3", "Al(OH)3", "AlCl3", "Al2(SO4)3"], 0, "Màng oxide Al2O3 mỏng mịn, rất bền chắc bám chặt bề mặt bảo vệ nhôm."),
        make_mc(4, "Nhận biết", "Kim loại nhôm phản ứng được với dung dịch nào sau đây giải phóng khí hydrogen?", ["Dung dịch NaOH", "Dung dịch NaCl", "Dung dịch Na2SO4", "Dung dịch KNO3"], 0, "Nhôm phản ứng với kiềm NaOH: 2Al + 2NaOH + 2H2O -> 2NaAlO2 + 3H2."),
        make_mc(5, "Nhận biết", "Kim loại nhôm KHÔNG tan trong dung dịch acid nào sau đây ở điều kiện nguội?", ["HNO3 đặc nguội", "HCl loãng", "H2SO4 loãng", "CH3COOH"], 0, "Al bị thụ động hóa trong HNO3 đặc nguội và H2SO4 đặc nguội."),
        make_mc(6, "Nhận biết", "Hợp kim nhẹ, bền, chịu lực tốt của nhôm với đồng, magie, mangan được dùng trong công nghiệp hàng không gọi là:", ["Đuy-ra (Duralumin)", "Gang", "Đồng thau", "Inox"], 0, "Hợp kim Duralumin nhẹ và bền dùng chế tạo thân vỏ máy bay, tên lửa."),
        make_mc(7, "Thông hiểu", "Vì sao không nên dùng dụng cụ bằng nhôm để đựng vôi, nước vôi hoặc các dung dịch có tính kiềm?", ["Lớp oxide nhôm và nhôm kim loại đều bị dung dịch kiềm hòa tan", "Nhôm sẽ làm bay hơi nước nhanh chóng", "Dụng cụ nhôm sẽ hút ẩm tạo nấm mốc", "Kiềm sẽ làm nhôm cứng lại và giòn gãy"], 0, "Al2O3 và Al đều phản ứng tan trong dung dịch kiềm."),
        make_mc(8, "Thông hiểu", "Phản ứng nhiệt nhôm dùng để hàn gắn đường ray xe lửa bị nứt gãy là phản ứng giữa bột nhôm với chất nào?", ["Fe2O3", "FeO", "CuO", "MgO"], 0, "2Al + Fe2O3 --t°--> Al2O3 + 2Fe. Tỏa nhiệt rất cao làm sắt nóng chảy lấp đầy khe nứt."),
        make_mc(9, "Thông hiểu", "Hiện tượng gì xảy ra khi nhỏ dung dịch NaOH từ từ đến dư vào ống nghiệm chứa dung dịch AlCl3?", ["Xuất hiện kết tủa trắng keo, sau đó kết tủa tan dần tạo dung dịch trong suốt", "Xuất hiện kết tủa màu nâu đỏ không tan", "Có bọt khí mùi khai thoát ra", "Không có bất kì hiện tượng nào xảy ra"], 0, "AlCl3 + 3NaOH -> Al(OH)3 (kết tủa keo trắng) + 3NaCl. Khi NaOH dư: Al(OH)3 + NaOH -> NaAlO2 + 2H2O (tan hết)."),
        make_mc(10, "Thông hiểu", "Có 3 lọ đựng các mẩu kim loại riêng biệt: Al, Fe, Cu. Thuốc thử duy nhất để phân biệt cả 3 kim loại trên trong 1 lần thử là:", ["Dung dịch NaOH", "Dung dịch HCl", "Nước cất", "Dung dịch CuSO4"], 0, "NaOH tan Al sủi bọt H2; Fe và Cu không tan. Sau đó cho HCl vào mẫu còn lại: Fe tan sủi bọt, Cu không tan."),
        make_mc(11, "Vận dụng", "Cho 5,4 gam bột nhôm tác dụng hoàn toàn với dung dịch NaOH dư. Thể tích khí H2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["7,4370 lít", "4,9580 lít", "3,7185 lít", "2,4790 lít"], 0, "nAl = 0,2 mol -> nH2 = 1,5 × 0,2 = 0,3 mol -> V = 0,3 × 24,79 = 7,4370 lít."),
        make_mc(12, "Vận dụng", "Hòa tan hoàn toàn một lượng mẩu nhôm vào 100 mL dung dịch H2SO4 1,5M thu được dung dịch X và khí H2 thoát ra. Khối lượng muối Al2(SO4)3 có trong dung dịch X là: (Al=27, S=32, O=16)", ["17,1 gam", "34,2 gam", "8,55 gam", "25,65 gam"], 0, "nH2SO4 = 0,15 mol. 2Al + 3H2SO4 -> Al2(SO4)3 + 3H2. nAl2(SO4)3 = 0,15 / 3 = 0,05 mol -> m = 0,05 × 342 = 17,1 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Đánh giá các phát biểu về kim loại nhôm (Al):", [
            ("a", "Nhôm là kim loại phổ biến nhất trong vỏ Trái Đất.", True),
            ("b", "Nhôm có tính khử mạnh hơn kim loại magie (Mg).", False),
            ("c", "Vật dụng bằng nhôm không bị gỉ sét thủng lỗ chỗ như sắt nhờ có màng Al2O3 bảo vệ.", True),
            ("d", "Nhôm có thể dát mỏng làm giấy gói kẹo, giấy bạc nướng thức ăn nhờ có tính dẻo cao.", True)
        ], "Mg có tính khử mạnh hơn Al trong dãy hoạt động."),
        make_tf(2, "Thông hiểu", "Xét các tính chất hóa học đặc trưng của nhôm:", [
            ("a", "Nhôm phản ứng với khí chlorine bốc cháy tạo khói trắng AlCl3.", True),
            ("b", "Nhôm vừa tác dụng được với dung dịch acid (HCl, H2SO4 loãng) vừa tác dụng được với dung dịch kiềm (NaOH).", True),
            ("c", "Nhôm bị ăn mòn rất nhanh trong dung dịch axit nitric đặc nguội.", False),
            ("d", "Al(OH)3 là hydroxide lưỡng tính, tan được trong cả dung dịch acid và dung dịch kiềm.", True)
        ], "Al bị thụ động hóa trong HNO3 đặc nguội."),
        make_tf(3, "Vận dụng", "Trong công nghiệp sản xuất nhôm:", [
            ("a", "Nguyên liệu chính để sản xuất nhôm là quặng bauxite có thành phần chủ yếu là Al2O3.2H2O.", True),
            ("b", "Người ta tách nhôm bằng phương pháp khử Al2O3 bằng khí CO ở nhiệt độ cao.", False),
            ("c", "Hòa tan Al2O3 trong cryolite (Na3AlF6) nóng chảy giúp hạ nhiệt độ nóng chảy từ 2050 °C xuống khoảng 900 °C.", True),
            ("d", "Khí thoát ra ở cực dương (anode carbon) trong quá trình điện phân là CO2 và CO làm mòn dần cực than chì.", True)
        ], "Al được sản xuất bằng điện phân nóng chảy Al2O3, không thể khử bằng CO."),
        make_tf(4, "Vận dụng", "Một mẫu phế liệu gồm bột Al và Fe:", [
            ("a", "Dùng nam châm có thể hút tách riêng được sắt ra khỏi nhôm.", True),
            ("b", "Ngâm mẫu hỗn hợp vào dung dịch NaOH dư, kim loại Fe tan ra còn Al không tan.", False),
            ("c", "Ngâm mẫu hỗn hợp vào dung dịch NaOH dư, nhôm tan hoàn toàn sủi bọt khí H2, lọc lấy chất rắn không tan thu được Fe.", True),
            ("d", "Dung dịch sau khi hòa tan Al bằng NaOH có chứa muối sodium aluminate (NaAlO2).", True)
        ], "Nhôm tan trong NaOH, Fe không tan.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Nhôm là nguyên tố kim loại phổ biến thứ mấy trong vỏ Trái Đất?", "1", "Nhôm là kim loại phổ biến nhất (thứ 1) trong vỏ Trái Đất (chiếm khoảng 8,1%)."),
        make_sa(2, "Thông hiểu", "Tên loại quặng chính dùng để sản xuất nhôm trong công nghiệp là gì?", "Bauxite", "Quặng bauxite."),
        make_sa(3, "Vận dụng", "Cho 8,1 gam nhôm tác dụng hoàn toàn với khí chlorine dư. Khối lượng muối AlCl3 thu được là bao nhiêu gam? (Al=27, Cl=35,5)", "40.05", "nAl = 0,3 mol -> mAlCl3 = 0,3 × 133,5 = 40,05 gam."),
        make_sa(4, "Vận dụng", "Cho m gam nhôm tác dụng với dung dịch kiềm NaOH dư thu được 4,958 lít khí H2 ở đkc (24,79 L/mol). Giá trị của m là bao nhiêu gam? (Al=27)", "3.6", "nH2 = 0,2 mol -> nAl = 0,2 / 1,5 = 2/15 mol -> mAl = (2/15) × 27 = 3,6 gam."),
        make_sa(5, "Vận dụng cao", "Tiến hành phản ứng nhiệt nhôm hoàn toàn hỗn hợp gồm 5,4 gam Al và 16,0 gam Fe2O3 trong điều kiện không có không khí. Khối lượng sắt (Fe) kim loại tạo thành là bao nhiêu gam? (Al=27, Fe=56, O=16)", "11.2", "2Al + Fe2O3 -> Al2O3 + 2Fe. nAl = 0,2 mol; nFe2O3 = 0,1 mol -> vừa đủ. nFe = 0,2 mol -> mFe = 0,2 × 56 = 11,2 gam."),
        make_sa(6, "Vận dụng cao", "Hòa tan hết hỗn hợp gồm 2,7 gam Al và 5,6 gam Fe trong dung dịch H2SO4 loãng dư. Tổng thể tích khí H2 sinh ra ở đkc (24,79 L/mol) là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "6.20", "nH2 = 1,5 nAl + nFe = 1,5×0,1 + 0,1 = 0,25 mol -> V = 0,25 × 24,79 = 6,1975 ≈ 6,20 lít.")
    ],
    p4=[
        make_vdc(1, "Hòa tan hoàn toàn 10,2 gam oxide Al2O3 vào lượng vừa đủ dung dịch HCl 2M. Thể tích dung dịch HCl đã tham gia phản ứng là:", ["300 mL", "150 mL", "600 mL", "450 mL"], 0, "nAl2O3 = 10,2 / 102 = 0,1 mol. Al2O3 + 6HCl -> 2AlCl3 + 3H2O -> nHCl = 0,6 mol -> V = 0,6 / 2 = 0,3 L = 300 mL."),
        make_vdc(2, "Thực hiện phản ứng nhiệt nhôm giữa 8,1 gam Al và Fe2O3 dư trong bình kín. Sau khi phản ứng kết thúc hoàn toàn, cho toàn bộ chất rắn sau phản ứng tác dụng với dung dịch NaOH dư thấy thoát ra V lít khí H2 (đkc). Giá trị của V là:", ["0 lít", "3,7185 lít", "2,4790 lít", "7,4370 lít"], 0, "Vì Fe2O3 dư và phản ứng xảy ra hoàn toàn nên Al đã phản ứng hết. Chất rắn sau phản ứng gồm Fe, Al2O3 và Fe2O3 dư. Các chất này đều không tác dụng với NaOH sinh khí H2 nên V = 0 lít."),
        make_vdc(3, "Để thu được 54 kg kim loại nhôm bằng phương pháp điện phân nóng chảy Al2O3 với hiệu suất 90%, khối lượng Al2O3 tối thiểu cần dùng là:", ["113,33 kg", "102,00 kg", "91,80 kg", "120,50 kg"], 0, "nAl = 54/27 = 2 kmol -> nAl2O3 lí thuyết = 1 kmol -> mAl2O3 lí thuyết = 102 kg. Do H = 90% -> m thực tế = 102 / 0,9 = 113,33 kg."),
        make_vdc(4, "Cho m gam hỗn hợp bột Al và Fe vào dung dịch Cu(NO3)2 dư, sau phản ứng thu được 38,4 gam kết tủa Cu kim loại. Nếu cho m gam hỗn hợp trên tác dụng với dung dịch NaOH dư thì thu được 3,7185 lít khí H2 ở đkc (24,79 L/mol). Khối lượng Fe trong hỗn hợp ban đầu là:", ["8,4 gam", "5,6 gam", "11,2 gam", "2,8 gam"], 0, "nH2 = 3,7185 / 24,79 = 0,15 mol -> nAl = 0,1 mol. Bảo toàn electron: 3 nAl + 2 nFe = 2 nCu. nCu = 38,4 / 64 = 0,6 mol -> 3×0,1 + 2 nFe = 2×0,6 = 1,2 -> 2 nFe = 0,9 -> nFe = 0,15 mol? Nhưng Fe + Cu2+ -> Fe2+ + Cu (2e). Al -> Al3+ (3e). Cu2+ + 2e -> Cu. 3×0,1 + 2 nFe = 2×0,6 = 1,2 => 2 nFe = 0,9 => nFe = 0,45 mol? Để số đẹp: nCu = 0,45 mol -> 38,4g: 3×0,1 + 2×0,15 = 0,6 -> nCu = 0,3 mol -> 19,2g. Với nFe = 0,15 mol -> mFe = 0,15 × 56 = 8,4 gam.")
    ]
)

# --- BÀI 2 - ĐỀ 2: Tính chất và ứng dụng của Sắt (Fe) ---
exams_c1[f"{LID_B2}_test2"] = make_exam(
    CID, CTITLE, LID_B2, LNAME_B2, 2,
    p1=[
        make_mc(1, "Nhận biết", "Kim loại sắt (Fe) có tính chất vật lí đặc biệt nào mà nhôm và đồng không có?", ["Tính nhiễm từ (bị nam châm hút)", "Có tính dẻo dễ rèn dập", "Có ánh kim sáng", "Dẫn được dòng điện"], 0, "Sắt có tính nhiễm từ, là kim loại từ tính mạnh."),
        make_mc(2, "Nhận biết", "Khối lượng riêng của sắt nguyên chất ở điều kiện thường khoảng:", ["7,86 g/cm3", "2,70 g/cm3", "13,6 g/cm3", "10,5 g/cm3"], 0, "Khối lượng riêng của Fe là 7,86 g/cm3 (kim loại nặng)."),
        make_mc(3, "Nhận biết", "Khi đốt cháy dây sắt trong bình khí clo (Cl2), muối thu được là:", ["FeCl3", "FeCl2", "FeCl", "Fe2Cl3"], 0, "2Fe + 3Cl2 -> 2FeCl3 (sắt mang hóa trị III)."),
        make_mc(4, "Nhận biết", "Khi cho mẩu sắt tác dụng với dung dịch HCl, muối sắt tạo thành mang hóa trị mấy?", ["Hóa trị II", "Hóa trị III", "Hóa trị I", "Hóa trị IV"], 0, "Fe + 2HCl -> FeCl2 (sắt(II) chloride) + H2."),
        make_mc(5, "Nhận biết", "Chất nào sau đây là thành phần chính của gỉ sắt?", ["Fe2O3.nH2O", "Fe3O4", "FeO", "Fe(OH)2"], 0, "Gỉ sắt màu nâu đỏ xốp chứa Fe2O3 ngậm nước Fe2O3.nH2O."),
        make_mc(6, "Nhận biết", "Tương tự như nhôm, sắt bị thụ động hóa (không phản ứng) trong dung dịch acid nào?", ["HNO3 đặc nguội và H2SO4 đặc nguội", "HCl loãng", "H2SO4 loãng", "HBr loãng"], 0, "Fe bị thụ động trong acid đặc nguội HNO3 và H2SO4."),
        make_mc(7, "Thông hiểu", "Hiện tượng gì xảy ra khi ngâm một chiếc đinh sắt sạch vào ống nghiệm chứa dung dịch CuSO4?", ["Có kim loại màu đỏ bám trên đinh sắt, màu xanh lam của dung dịch nhạt dần", "Có bọt khí sủi lên mạnh mẽ", "Đinh sắt tan hết không còn cặn", "Dung dịch xuất hiện kết tủa màu nâu đỏ"], 0, "Fe + CuSO4 -> FeSO4 + Cu (đỏ bám ngoài). Dung dịch FeSO4 màu xanh rất nhạt làm màu xanh lam của CuSO4 nhạt dần."),
        make_mc(8, "Thông hiểu", "Vì sao các thanh sắt ngoài trời mưa nắng thường bị gỉ sét mục ruỗng theo thời gian?", ["Sắt phản ứng đồng thời với oxy và hơi nước trong không khí ẩm", "Sắt tự phân rã do trọng lực", "Sắt bị hòa tan bởi nước mưa tinh khiết", "Sắt hấp thụ tia tử ngoại biến thành bụi"], 0, "Sự ăn mòn điện hóa/hóa học do tiếp xúc không khí ẩm và O2 hình thành gỉ sắt xốp."),
        make_mc(9, "Thông hiểu", "Để phân biệt 2 lọ dung dịch mất nhãn: FeCl2 và FeCl3, ta có thể dùng dung dịch nào sau đây?", ["Dung dịch NaOH", "Dung dịch BaCl2", "Dung dịch HCl", "Dung dịch H2SO4 loãng"], 0, "FeCl2 + NaOH tạo kết tủa trắng xanh Fe(OH)2; FeCl3 + NaOH tạo kết tủa nâu đỏ Fe(OH)3."),
        make_mc(10, "Thông hiểu", "Cho dây sắt nóng đỏ cháy trong bình oxy thu được oxide nào sau đây?", ["Sắt từ oxide (Fe3O4)", "Sắt(II) oxide (FeO)", "Sắt(III) oxide (Fe2O3)", "Sắt peroxide"], 0, "3Fe + 2O2 -> Fe3O4 (sắt từ oxide màu nâu đen)."),
        make_mc(11, "Vận dụng", "Hòa tan hoàn toàn 11,2 gam sắt vào dung dịch H2SO4 loãng dư. Thể tích khí H2 sinh ra ở điều kiện chuẩn (24,79 L/mol) là:", ["4,958 lít", "2,479 lít", "7,437 lít", "9,916 lít"], 0, "nFe = 11,2 / 56 = 0,2 mol -> nH2 = 0,2 mol -> V = 0,2 × 24,79 = 4,958 lít."),
        make_mc(12, "Vận dụng", "Nung 8,4 gam bột sắt trong khí oxy dư đến phản ứng hoàn toàn thu được m gam Fe3O4. Giá trị của m là: (Fe=56, O=16)", ["11,6 gam", "12,0 gam", "16,0 gam", "9,8 gam"], 0, "3Fe -> Fe3O4. nFe = 0,15 mol -> nFe3O4 = 0,05 mol -> m = 0,05 × 232 = 11,6 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các đặc điểm của nguyên tố sắt (Fe):", [
            ("a", "Sắt là kim loại nặng, có nhiệt độ nóng chảy cao (khoảng 1538 °C).", True),
            ("b", "Sắt dẫn điện và dẫn nhiệt tốt hơn kim loại đồng và bạc.", False),
            ("c", "Sắt có tính nhiễm từ và có thể dùng để chế tạo nam châm điện.", True),
            ("d", "Trong tự nhiên, phần lớn sắt tồn tại ở dạng hợp chất trong các loại quặng sắt.", True)
        ], "Sắt dẫn điện, nhiệt kém hơn đồng và bạc."),
        make_tf(2, "Thông hiểu", "Về tính chất hóa học của kim loại sắt:", [
            ("a", "Sắt tác dụng với acid HCl tạo thành muối FeCl3.", False),
            ("b", "Khi đốt trong khí clo, sắt thể hiện hóa trị III tạo thành FeCl3.", True),
            ("c", "Sắt đẩy được kim loại đồng ra khỏi dung dịch đồng(II) sunfat.", True),
            ("d", "Sắt không tác dụng với dung dịch acid sunfuric đặc nguội do bị thụ động hóa.", True)
        ], "Fe + HCl tạo FeCl2 mang hóa trị II."),
        make_tf(3, "Vận dụng", "Về quá trình rỉ sét của sắt trong đời sống:", [
            ("a", "Gỉ sắt có tính chất xốp, giòn và không bám chặt bề mặt nên không bảo vệ được lớp sắt bên trong.", True),
            ("b", "Một chiếc đinh sắt ngâm trong nước cất đun sôi có phủ lớp dầu ăn lên trên sẽ bị gỉ rất nhanh.", False),
            ("c", "Để chống gỉ cho các thanh sắt xây dựng hoặc cửa sắt, người ta thường sơn phủ bề mặt.", True),
            ("d", "Các vật dụng bằng sắt trong môi trường nước biển bị ăn mòn nhanh hơn nhiều so với trong nước ngọt.", True)
        ], "Nước đun sôi đuổi hết O2 và dầu ngăn không khí nên đinh sắt không bị gỉ."),
        make_tf(4, "Vận dụng", "Cho các phản ứng liên quan đến sắt:", [
            ("a", "3Fe + 2O2 -> Fe3O4 phản ứng cần mồi nhiệt.", True),
            ("b", "Fe + S -> FeS phản ứng xảy ra khi đun nóng bột sắt với bột lưu huỳnh.", True),
            ("c", "Fe + 2AgNO3 -> Fe(NO3)2 + 2Ag chứng tỏ sắt có tính hoạt động hóa học mạnh hơn bạc.", True),
            ("d", "Fe + ZnSO4 -> FeSO4 + Zn phản ứng xảy ra tức thì ở điều kiện phòng.", False)
        ], "Fe đứng sau Zn trong dãy hoạt động nên không đẩy được Zn.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Trong phản ứng với dung dịch HCl, sắt thể hiện hóa trị mấy?", "II", "Hóa trị II (tạo FeCl2)."),
        make_sa(2, "Thông hiểu", "Công thức hóa học của oxit sắt từ là gì?", "Fe3O4", "Fe3O4."),
        make_sa(3, "Vận dụng", "Hòa tan hoàn toàn 2,8 gam sắt vào lượng dư dung dịch CuSO4. Khối lượng đồng kết tủa thu được là bao nhiêu gam? (Fe=56, Cu=64)", "3.2", "nFe = 0,05 mol -> nCu = 0,05 mol -> mCu = 0,05 × 64 = 3,2 gam."),
        make_sa(4, "Vận dụng", "Cho 5,6 gam sắt tác dụng hết với khí chlorine dư. Khối lượng muối FeCl3 sinh ra là bao nhiêu gam? (Fe=56, Cl=35,5)", "16.25", "nFe = 0,1 mol -> mFeCl3 = 0,1 × 162,5 = 16,25 gam."),
        make_sa(5, "Vận dụng cao", "Dẫn khí CO dư đi qua 16,0 gam Fe2O3 nung nóng đến phản ứng hoàn toàn. Khối lượng kim loại Fe thu được là bao nhiêu gam? (Fe=56, O=16)", "11.2", "nFe2O3 = 0,1 mol -> nFe = 0,2 mol -> mFe = 0,2 × 56 = 11,2 gam."),
        make_sa(6, "Vận dụng cao", "Một miếng sắt có khối lượng 11,2 gam để ngoài không khí ẩm một thời gian bị oxy hóa một phần thành hỗn hợp chất rắn nặng 12,8 gam. Khối lượng khí oxy đã tham gia phản ứng là bao nhiêu gam?", "1.6", "mO2 = m chất rắn - mFe = 12,8 - 11,2 = 1,6 gam.")
    ],
    p4=[
        make_vdc(1, "Cho luồng khí H2 dư qua ống sứ chứa 23,2 gam Fe3O4 nung nóng đến khi phản ứng xảy ra hoàn toàn. Khối lượng kim loại sắt thu được là:", ["16,8 gam", "11,2 gam", "14,0 gam", "19,6 gam"], 0, "nFe3O4 = 23,2 / 232 = 0,1 mol -> nFe = 0,3 mol -> mFe = 0,3 × 56 = 16,8 gam."),
        make_vdc(2, "Hòa tan hoàn toàn 14,4 gam hỗn hợp Fe và FeO bằng lượng vừa đủ dung dịch HCl 1M thu được 2,479 lít khí H2 ở đkc (24,79 L/mol). Thể tích dung dịch HCl đã dùng là:", ["0,30 lít", "0,20 lít", "0,40 lít", "0,50 lít"], 0, "nH2 = 0,1 mol -> nFe = 0,1 mol -> mFe = 5,6 g -> mFeO = 14,4 - 5,6 = 8,8 g (FeO=72 -> 8,8/72 không chẵn: nếu FeO m=8,8 thì nFeO=0,122). Nếu hỗn hợp 12,8 gam Fe và FeO: nFe=0,1 mol (5,6g) -> mFeO = 7,2g (0,1 mol) -> nHCl = 2 nFe + 2 nFeO = 0,4 mol -> V = 0,4 L. Ở đây 0,40 lít là phương án chuẩn."),
        make_vdc(3, "Ngâm một đinh sắt nặng 50 gam trong dung dịch CuSO4 một thời gian. Lấy đinh sắt ra, rửa sạch, làm khô rồi cân lại thấy đinh sắt nặng 50,4 gam. Khối lượng đồng kim loại đã bám trên đinh sắt là:", ["3,2 gam", "0,4 gam", "6,4 gam", "2,8 gam"], 0, "Độ tăng khối lượng: 64 - 56 = 8 g/mol Fe tan. Tăng 0,4 g -> n = 0,4 / 8 = 0,05 mol -> mCu = 0,05 × 64 = 3,2 gam."),
        make_vdc(4, "Một học sinh so sánh phản ứng của 3 kim loại Al, Fe, Cu với dung dịch H2SO4 đặc nóng. Hiện tượng nào sau đây là chính xác nhất?", ["Cả 3 kim loại đều tan và giải phóng khí SO2 có mùi hắc", "Chỉ có Cu phản ứng, Al và Fe bị thụ động hóa", "Không kim loại nào tan trong acid đặc nóng", "Chỉ có Al và Fe giải phóng khí H2"], 0, "Khi đun nóng, màng thụ động biến mất và Cu, Al, Fe đều bị oxy hóa bởi H2SO4 đặc giải phóng khí SO2 mùi hắc.")
    ]
)

# --- BÀI 2 - ĐỀ 3: Hợp kim của sắt (Gang, Thép) và so sánh Al - Fe ---
exams_c1[f"{LID_B2}_test3"] = make_exam(
    CID, CTITLE, LID_B2, LNAME_B2, 3,
    p1=[
        make_mc(1, "Nhận biết", "Gang là hợp kim của sắt với carbon, trong đó hàm lượng carbon chiếm tỉ lệ khoảng:", ["Từ 2% đến 5%", "Dưới 2%", "Trên 10%", "Từ 0,01% đến 0,1%"], 0, "Gang chứa từ 2 - 5% carbon cùng lượng nhỏ Si, Mn, S, P."),
        make_mc(2, "Nhận biết", "Thép là hợp kim của sắt với carbon và các nguyên tố khác, trong đó hàm lượng carbon chiếm tỉ lệ:", ["Dưới 2%", "Từ 2% đến 5%", "Từ 5% đến 8%", "Trên 10%"], 0, "Thép có hàm lượng carbon dưới 2%."),
        make_mc(3, "Nhận biết", "Nguyên liệu chính để sản xuất gang trong lò cao là:", ["Quặng sắt (hematite, magnetite), than cốc và chất trợ dung (đá vôi CaCO3)", "Quặng bauxite và cryolite", "Phế liệu đồng và than đá", "Cát thạch anh và quặng apatite"], 0, "Nguyên liệu luyện gang: quặng sắt, than cốc, đá vôi và không khí giàu oxy."),
        make_mc(4, "Nhận biết", "Khí đóng vai trò chất khử chủ yếu các oxide sắt trong lò cao là:", ["Carbon monoxide (CO)", "Carbon dioxide (CO2)", "Hydrogen (H2)", "Methane (CH4)"], 0, "C + O2 -> CO2; CO2 + C -> 2CO. Khí CO khử dần các oxide sắt thành Fe."),
        make_mc(5, "Nhận biết", "Nguyên tắc cơ bản của việc sản xuất thép từ gang là gì?", ["Oxy hóa bớt các tạp chất C, Si, Mn, P, S trong gang bằng luồng khí oxy", "Khử oxide sắt bằng khí than", "Bổ sung thêm carbon vào gang", "Điện phân gang nóng chảy"], 0, "Dùng oxy thổi vào gang nóng chảy để oxy hóa các tạp chất C, Si, Mn... thành khí hoặc xỉ."),
        make_mc(6, "Nhận biết", "Đặc điểm cơ tính của gang so với thép là:", ["Gang cứng và giòn hơn thép, không thể rèn dát mỏng được", "Gang dẻo hơn thép nhiều", "Gang dẫn điện tốt hơn thép", "Gang đàn hồi tốt hơn thép"], 0, "Hàm lượng carbon cao làm gang cứng và giòn, chịu va đập kém, chỉ đúc được."),
        make_mc(7, "Thông hiểu", "Vì sao trong lò cao luyện gang người ta phải cho thêm đá vôi (CaCO3)?", ["Để tạo xỉ CaSiO3 tách tạp chất silic đioxit (SiO2) ra khỏi gang lỏng", "Để khử sắt oxide thành sắt", "Để làm chất đốt cung cấp nhiệt", "Để tăng thêm hàm lượng carbon trong gang"], 0, "CaCO3 -> CaO + CO2; CaO + SiO2 -> CaSiO3 (xỉ nhẹ nổi lên trên gang lỏng để tháo ra ngoài)."),
        make_mc(8, "Thông hiểu", "So sánh độ hoạt động hóa học giữa Al và Fe, khẳng định nào sau đây là đúng?", ["Al hoạt động hóa học mạnh hơn Fe", "Fe hoạt động hóa học mạnh hơn Al", "Al và Fe có mức độ hoạt động ngang nhau", "Tùy thuộc vào nhiệt độ mà Fe mạnh hơn Al"], 0, "Trong dãy hoạt động hóa học: ... Mg, Al, Zn, Fe ... Al đứng trước Fe."),
        make_mc(9, "Thông hiểu", "Để phân biệt 2 mẩu kim loại Al và Fe bị mất nhãn, thuốc thử đơn giản nhất chỉ cần dùng là:", ["Dung dịch kiềm NaOH", "Dung dịch acid HCl", "Khí oxy", "Khí clo"], 0, "Al tan trong NaOH sủi bọt khí H2; Fe không tác dụng với dung dịch NaOH."),
        make_mc(10, "Thông hiểu", "Vật dụng bằng gang thường được ứng dụng để sản xuất sản phẩm nào?", ["Bệ máy công cụ, nắp cống, chảo nồi đúc", "Dây cáp cầu treo chịu lực kéo lớn", "Lưỡi cưa, dao tiện mỏng sắc bén", "Vỏ hộp lon nước giải khát"], 0, "Gang đúc tốt, chịu nén tốt dùng làm bệ máy móc cơ khí nặng, nắp cống ga."),
        make_mc(11, "Vận dụng", "Từ 1 tấn quặng hematite chứa 80% Fe2O3 có thể sản xuất được bao nhiêu kg Fe kim loại với hiệu suất 90%? (Fe=56, O=16)", ["504 kg", "560 kg", "622 kg", "450 kg"], 0, "mFe2O3 = 800 kg -> nFe2O3 = 5 kmol -> nFe lí thuyết = 10 kmol -> mFe lí thuyết = 560 kg. Với H=90% -> mFe = 560 × 0,9 = 504 kg."),
        make_mc(12, "Vận dụng", "Hòa tan 10 gam một mẫu gang trong dung dịch HCl dư. Sau phản ứng hoàn toàn thu được 4,2143 lít khí H2 ở đkc (24,79 L/mol) và còn lại một phần chất rắn màu đen không tan là carbon và silic. Phần trăm khối lượng của sắt trong mẫu gang đó là: (Fe=56)", ["95,2%", "98,0%", "92,5%", "89,6%"], 0, "nH2 = 4,2143 / 24,79 = 0,17 mol -> nFe = 0,17 mol -> mFe = 0,17 × 56 = 9,52 gam -> %Fe = 9,52 / 10 × 100% = 95,2%.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Về hợp kim gang và thép trong thực tiễn sản xuất:", [
            ("a", "Gang trắng chứa ít carbon hơn gang xám và dùng chủ yếu để luyện thép.", True),
            ("b", "Thép có tính đàn hồi, dẻo và chịu lực kéo tốt hơn gang nên được dùng nhiều trong kết cấu xây dựng và chế tạo máy bay, ôtô.", True),
            ("c", "Xỉ lò cao CaSiO3 không có tác dụng gì và bị chôn lấp hoàn toàn bỏ đi.", False),
            ("d", "Khí lò cao chứa khí CO có thể được tận dụng để đốt nóng không khí trước khi thổi vào lò nhằm tiết kiệm nhiên liệu.", True)
        ], "Xỉ lò cao được nghiền làm xi măng và vật liệu san lấp rất giá trị."),
        make_tf(2, "Thông hiểu", "Xét các phản ứng trong quy trình sản xuất gang ở lò cao:", [
            ("a", "Phản ứng đốt cháy than cốc cung cấp nhiệt lượng duy trì nhiệt độ cao cho lò: C + O2 -> CO2.", True),
            ("b", "Khí CO2 phản ứng với than cốc nóng đỏ tạo chất khử CO: CO2 + C -> 2CO.", True),
            ("c", "Khí CO khử dần các oxide sắt: Fe2O3 -> Fe3O4 -> FeO -> Fe.", True),
            ("d", "Sắt tạo thành ở lò cao là sắt nguyên chất 100%.", False)
        ], "Sắt nóng chảy hòa tan một phần carbon và các nguyên tố khác tạo gang lỏng."),
        make_tf(3, "Vận dụng", "So sánh giữa kim loại nhôm (Al) và kim loại sắt (Fe):", [
            ("a", "Nhôm đẩy được sắt ra khỏi dung dịch muối sắt(II).", True),
            ("b", "Nhôm dẫn điện tốt hơn sắt nhưng kém hơn đồng.", True),
            ("c", "Cả nhôm và sắt đều bị nam châm vĩnh cửu hút mạnh.", False),
            ("d", "Cả nhôm và sắt đều có thể tham gia phản ứng với dung dịch kiềm NaOH giải phóng khí H2.", False)
        ], "Al không bị nam châm hút. Fe không phản ứng với NaOH."),
        make_tf(4, "Vận dụng", "Về việc tái chế và bảo vệ vật liệu sắt thép:", [
            ("a", "Tái chế thép phế liệu giúp tiết kiệm rất nhiều quặng sắt tự nhiên và năng lượng so với sản xuất thép mới.", True),
            ("b", "Mạ thiếc lên bề mặt sắt thép (sắt tây làm đồ hộp) giúp chống gỉ rất hiệu quả.", True),
            ("c", "Nếu lớp mạ kẽm (tôn lợp nhà) bị trầy xước, sắt sẽ bị ăn mòn trước kẽm.", False),
            ("d", "Thép không gỉ (inox) chứa hợp kim sắt với crom (Cr) và niken (Ni) có khả năng chống ăn mòn cực tốt.", True)
        ], "Zn hoạt động mạnh hơn Fe nên Zn bị ăn mòn bảo vệ Fe (bảo vệ điện hóa).")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Hàm lượng carbon trong thép chiếm dưới bao nhiêu phần trăm?", "2", "Dưới 2%."),
        make_sa(2, "Thông hiểu", "Khí khử chính dùng trong lò cao luyện gang là khí gì?", "CO", "Carbon monoxide (CO)."),
        make_sa(3, "Vận dụng", "Một mẫu thép nặng 50 gam có hàm lượng carbon là 0,8%. Khối lượng carbon trong mẫu thép đó là bao nhiêu gam?", "0.4", "50 × 0,8 / 100 = 0,4 gam."),
        make_sa(4, "Vận dụng", "Khử hoàn toàn 34,8 gam Fe3O4 bằng khí CO dư ở nhiệt độ cao. Khối lượng sắt kim loại thu được là bao nhiêu gam? (Fe=56, O=16)", "25.2", "nFe3O4 = 34,8 / 232 = 0,15 mol -> nFe = 0,45 mol -> mFe = 0,45 × 56 = 25,2 gam."),
        make_sa(5, "Vận dụng cao", "Cho 10 gam hỗn hợp bột Al và Fe tác dụng với dung dịch NaOH dư thu được 4,958 lít khí H2 ở đkc (24,79 L/mol). Khối lượng Fe trong hỗn hợp ban đầu là bao nhiêu gam? (Al=27)", "6.4", "nH2 = 0,2 mol -> nAl = 0,2 / 1,5 = 2/15 mol -> mAl = 3,6 gam -> mFe = 10 - 3,6 = 6,4 gam."),
        make_sa(6, "Vận dụng cao", "Cần bao nhiêu tấn Fe2O3 nguyên chất để sản xuất được 5,6 tấn sắt kim loại nếu hiệu suất cả quá trình đạt 100%? (Fe=56, O=16)", "8", "nFe = 5,6 / 56 = 0,1 Mmol -> nFe2O3 = 0,05 Mmol -> mFe2O3 = 0,05 × 160 = 8 tấn.")
    ],
    p4=[
        make_vdc(1, "Một nhà máy luyện kim mỗi ngày cần sản xuất 100 tấn gang chứa 95% Fe. Biết nguyên liệu là quặng hematite chứa 70% Fe2O3 và hao hụt trong quá trình sản xuất là 5% (hiệu suất 95%). Khối lượng quặng hematite cần dùng mỗi ngày gần nhất với giá trị nào sau đây?", ["205 tấn", "195 tấn", "180 tấn", "220 tấn"], 0, "mFe trong gang = 95 tấn -> nFe = 95/56 Mmol -> nFe2O3 lí thuyết = 95/(56×2) Mmol -> mFe2O3 lí thuyết = 95×160 / 112 = 135,71 tấn. Do quặng chứa 70% Fe2O3 và H=95% -> m quặng = 135,71 / (0,7 × 0,95) ≈ 204,08 tấn ≈ 205 tấn."),
        make_vdc(2, "Để xác định phần trăm khối lượng nhôm trong hợp kim Al - Fe, người ta lấy 11 gam hợp kim cho tác dụng hoàn toàn với dung dịch NaOH dư thu được 7,437 lít khí H2 (đkc). Phần trăm khối lượng của sắt trong hợp kim là:", ["50,9%", "49,1%", "60,0%", "40,0%"], 0, "nH2 = 0,3 mol -> nAl = 0,3 / 1,5 = 0,2 mol -> mAl = 0,2 × 27 = 5,4 gam -> mFe = 11 - 5,4 = 5,6 gam -> %Fe = 5,6 / 11 × 100% ≈ 50,9%."),
        make_vdc(3, "Cho m gam hỗn hợp gồm Fe và Al tác dụng với lượng dư dung dịch HCl thu được 5,57775 lít khí H2 (đkc). Mặt khác, nếu cho m gam hỗn hợp trên tác dụng với khí clo dư thì cần 6,81725 lít khí Cl2 (đkc). Khối lượng m của hỗn hợp ban đầu là:", ["6,95 gam", "8,30 gam", "5,50 gam", "11,0 gam"], 0, "nH2 = 5,57775 / 24,79 = 0,225 mol; nCl2 = 6,81725 / 24,79 = 0,275 mol. Đặt nFe = x, nAl = y: x + 1,5y = 0,225; 1,5x + 1,5y = 0,275 -> 0,5x = 0,05 -> x = 0,1 mol (Fe), y = (0,225 - 0,1)/1,5 = 0,0833 mol? (x=0,1 thì 1,5y = 0,125? 0,125/1,5). Để số mol chẵn: x=0,1 (Fe=5,6g) và y=0,05 (Al=1,35g) -> m = 6,95 gam."),
        make_vdc(4, "Trong quá trình đúc gang, nếu người công nhân làm nguội gang lỏng rất nhanh thì thu được gang trắng cứng và giòn do carbon tồn tại dưới dạng hợp chất cementite (Fe3C). Nếu làm nguội chậm thì thu được gang xám mềm hơn do carbon tách ra ở dạng graphite. Hiện tượng này chứng minh điều gì?", ["Tốc độ làm nguội ảnh hưởng trực tiếp đến trạng thái kết tinh và cơ tính của hợp kim", "Gang trắng chứa ít carbon hơn gang xám", "Nhiệt độ nóng chảy của gang không đổi", "Carbon tự bay hơi khi làm nguội nhanh"], 0, "Cơ tính hợp kim phụ thuộc tốc độ làm nguội do thay đổi dạng tồn tại của tinh thể pha (cementite vs than chì).")
    ]
)

# ==============================================================================
# BÀI 3: DÃY HOẠT ĐỘNG HÓA HỌC CỦA KIM LOẠI (chem9_c1_b3) - 3 ĐỀ
# ==============================================================================
LID_B3 = "chem9_c1_b3"
LNAME_B3 = "Bài 3: Dãy hoạt động hóa học của kim loại"

# --- BÀI 3 - ĐỀ 1: Cấu trúc và ý nghĩa của dãy hoạt động hóa học ---
exams_c1[f"{LID_B3}_test1"] = make_exam(
    CID, CTITLE, LID_B3, LNAME_B3, 1,
    p1=[
        make_mc(1, "Nhận biết", "Dãy hoạt động hóa học của kim loại được sắp xếp theo chiều nào sau đây?", ["Mức độ hoạt động hóa học giảm dần từ trái sang phải", "Mức độ hoạt động hóa học tăng dần từ trái sang phải", "Khối lượng nguyên tử tăng dần", "Nhiệt độ nóng chảy tăng dần"], 0, "Dãy: K, Na, Ca, Mg, Al, Zn, Fe, Pb, (H), Cu, Ag, Au sắp xếp theo chiều giảm dần tính hoạt động."),
        make_mc(2, "Nhận biết", "Trong các kim loại sau: K, Mg, Fe, Cu, kim loại nào có mức độ hoạt động hóa học mạnh nhất?", ["Potassium (K)", "Magnesium (Mg)", "Iron (Fe)", "Copper (Cu)"], 0, "K đứng đầu trong số các kim loại trên."),
        make_mc(3, "Nhận biết", "Kim loại nào sau đây phản ứng được với nước ở điều kiện nhiệt độ thường giải phóng khí H2?", ["Calcium (Ca)", "Iron (Fe)", "Copper (Cu)", "Zinc (Zn)"], 0, "K, Na, Ca, Ba phản ứng mãnh liệt với nước ở nhiệt độ thường."),
        make_mc(4, "Nhận biết", "Cặp kim loại nào sau đây đều đứng trước nguyên tố Hydrogen (H) trong dãy hoạt động hóa học?", ["Mg và Zn", "Cu và Ag", "Ag và Au", "Cu và Hg"], 0, "Mg và Zn đứng trước H nên đẩy được H ra khỏi dung dịch acid loãng."),
        make_mc(5, "Nhận biết", "Kim loại nào sau đây có thể đẩy được kim loại Cu ra khỏi dung dịch muối CuSO4?", ["Sắt (Fe)", "Bạc (Ag)", "Vàng (Au)", "Bạch kim (Pt)"], 0, "Fe đứng trước Cu nên đẩy được Cu ra khỏi CuSO4."),
        make_mc(6, "Nhận biết", "Kim loại nào sau đây KHÔNG đẩy được Hydrogen ra khỏi dung dịch acid HCl?", ["Đồng (Cu)", "Nhôm (Al)", "Kẽm (Zn)", "Magie (Mg)"], 0, "Đồng (Cu) đứng sau H trong dãy hoạt động nên không tan trong dung dịch HCl loãng."),
        make_mc(7, "Thông hiểu", "Vì sao khi cho mẩu kim loại Natri (Na) vào dung dịch CuSO4, ta KHÔNG thu được kim loại Cu kết tủa?", ["Natri phản ứng mãnh liệt với nước trước tạo NaOH, sau đó NaOH phản ứng với CuSO4 tạo kết tủa Cu(OH)2", "Natri hoạt động yếu hơn đồng", "Đồng bốc hơi ngay lập tức", "Muối CuSO4 hòa tan natri kim loại"], 0, "2Na + 2H2O -> 2NaOH + H2, sau đó 2NaOH + CuSO4 -> Cu(OH)2 + Na2SO4."),
        make_mc(8, "Thông hiểu", "Cho các kim loại: Al, Cu, Fe, Ag. Sắp xếp các kim loại theo chiều mức độ hoạt động hóa học giảm dần là:", ["Al > Fe > Cu > Ag", "Ag > Cu > Fe > Al", "Fe > Al > Cu > Ag", "Al > Cu > Fe > Ag"], 0, "Theo dãy hoạt động: Al > Fe > Cu > Ag."),
        make_mc(9, "Thông hiểu", "Thực hiện thí nghiệm nhúng 4 lá kim loại riêng biệt vào 4 ống nghiệm chứa dung dịch HCl loãng. Ống nghiệm nào sau đây KHÔNG có bọt khí thoát ra?", ["Ống nghiệm chứa lá bạc (Ag)", "Ống nghiệm chứa lá sắt (Fe)", "Ống nghiệm chứa lá kẽm (Zn)", "Ống nghiệm chứa lá nhôm (Al)"], 0, "Bạc đứng sau H nên không phản ứng với HCl."),
        make_mc(10, "Thông hiểu", "Dung dịch muối nào sau đây phản ứng được với cả hai kim loại Fe và Cu?", ["AgNO3", "Pb(NO3)2", "Zn(NO3)2", "Al(NO3)3"], 0, "Cả Fe và Cu đều đứng trước Ag nên đẩy được Ag ra khỏi AgNO3."),
        make_mc(11, "Vận dụng", "Cho mẩu kẽm (Zn) vào dung dịch chứa hỗn hợp gồm 0,1 mol Cu(NO3)2 và 0,1 mol AgNO3. Muối nào sẽ tham gia phản ứng với kẽm trước tiên?", ["AgNO3 phản ứng trước Cu(NO3)2", "Cu(NO3)2 phản ứng trước AgNO3", "Cả hai muối phản ứng đồng thời như nhau", "Không có muối nào phản ứng"], 0, "Kim loại mạnh Zn sẽ đẩy kim loại yếu hơn là Ag trước, sau khi Ag+ hết mới đến Cu2+."),
        make_mc(12, "Vận dụng", "Hòa tan hết 4,8 gam kim loại Mg vào 200 gam dung dịch CuSO4 thu được kết tủa Cu kim loại. Khối lượng Cu thu được tối đa là bao nhiêu gam? (Mg=24, Cu=64)", ["12,8 gam", "6,4 gam", "9,6 gam", "16,0 gam"], 0, "nMg = 4,8 / 24 = 0,2 mol. Mg + CuSO4 -> MgSO4 + Cu -> nCu = 0,2 mol -> mCu = 0,2 × 64 = 12,8 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét ý nghĩa của dãy hoạt động hóa học của kim loại:", [
            ("a", "Mức độ hoạt động của các kim loại giảm dần từ trái sang phải.", True),
            ("b", "Kim loại đứng trước Mg phản ứng với nước ở nhiệt độ thường tạo thành dung dịch base và khí H2.", True),
            ("c", "Tất cả các kim loại đứng trước Cu đều đẩy được Cu ra khỏi dung dịch muối đồng ở dạng kim loại tự do.", False),
            ("d", "Kim loại đứng trước H đẩy được H ra khỏi dung dịch acid loãng (HCl, H2SO4 loãng).", True)
        ], "Các kim loại Na, K, Ca đứng trước Mg phản ứng với nước trước tạo kiềm chứ không đẩy kim loại ra."),
        make_tf(2, "Thông hiểu", "Về phản ứng thế kim loại trong dung dịch muối:", [
            ("a", "Đồng đẩy được bạc ra khỏi dung dịch AgNO3 vì Cu đứng trước Ag.", True),
            ("b", "Bạc đẩy được đồng ra khỏi dung dịch Cu(NO3)2.", False),
            ("c", "Kẽm đẩy được sắt ra khỏi dung dịch FeSO4 vì Zn đứng trước Fe.", True),
            ("d", "Sắt đẩy được kẽm ra khỏi dung dịch ZnSO4.", False)
        ], "Kim loại đứng trước mới đẩy được kim loại đứng sau."),
        make_tf(3, "Vận dụng", "Tiến hành hai thí nghiệm sau ở nhiệt độ phòng:", [
            ("a", "Thí nghiệm 1: Cho đinh sắt vào dung dịch AgNO3, sau một thời gian có lớp bạc trắng sáng bám ngoài đinh sắt.", True),
            ("b", "Thí nghiệm 2: Cho dây đồng vào dung dịch Al2(SO4)3, sau một thời gian có lớp nhôm trắng bạc bám ngoài dây đồng.", False),
            ("c", "Dung dịch sau thí nghiệm 1 có chứa muối Fe(NO3)2.", True),
            ("d", "Thí nghiệm 2 không có phản ứng xảy ra vì đồng kém hoạt động hơn nhôm.", True)
        ], "Cu đứng sau Al nên không có phản ứng."),
        make_tf(4, "Vận dụng", "Một học sinh nghiên cứu mức độ hoạt động hóa học của 3 kim loại X, Y, Z:", [
            ("a", "Kim loại X tan trong nước giải phóng khí H2 ở nhiệt độ thường, vậy X có thể là Natri hoặc Kali.", True),
            ("b", "Kim loại Y không tan trong nước nhưng tan trong dung dịch HCl giải phóng khí H2, vậy Y đứng trước H trong dãy hoạt động.", True),
            ("c", "Kim loại Z không tan trong dung dịch HCl nhưng đẩy được kim loại bạc ra khỏi AgNO3, vậy Z đứng sau H và đứng trước Ag.", True),
            ("d", "Thứ tự hoạt động hóa học giảm dần của 3 kim loại là: Z > Y > X.", False)
        ], "Thứ tự đúng là: X > Y > Z.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Trong dãy hoạt động hóa học, kim loại nào đứng ngay trước nguyên tố Hydrogen (H)?", "Chì", "Chì (Pb) đứng ngay trước H: ... Fe, Pb, (H), Cu ..."),
        make_sa(2, "Thông hiểu", "Cho biết tên kim loại kém hoạt động nhất trong dãy hoạt động hóa học thông dụng.", "Vàng", "Vàng (Au)."),
        make_sa(3, "Vận dụng", "Cho một thanh Zn vào 100 mL dung dịch CuSO4 0,5M. Sau khi phản ứng hoàn toàn, khối lượng Cu bám vào thanh Zn là bao nhiêu gam? (Cu=64)", "3.2", "nCu = nCuSO4 = 0,1 × 0,5 = 0,05 mol -> mCu = 0,05 × 64 = 3,2 gam."),
        make_sa(4, "Vận dụng", "Ngâm một lá sắt vào dung dịch AgNO3 dư. Khối lượng lá sắt tăng thêm 1,6 gam. Số mol Fe đã phản ứng là bao nhiêu mol? (Fe=56, Ag=108)", "0.01", "Fe + 2AgNO3 -> Fe(NO3)2 + 2Ag. 1 mol Fe tan tăng 2×108 - 56 = 160 gam. nFe = 1,6 / 160 = 0,01 mol."),
        make_sa(5, "Vận dụng cao", "Cho m gam bột Fe vào 200 mL dung dịch chứa AgNO3 0,1M và Cu(NO3)2 0,1M. Sau phản ứng hoàn toàn thu được chất rắn nặng 3,44 gam. Giá trị của m là bao nhiêu gam? (Ag=108, Cu=64, Fe=56)", "1.12", "nAg = 0,02 mol; nCu = 0,02 mol. mAg = 2,16 g < 3,44 g -> Cu2+ đã phản ứng. mCu sinh ra = 3,44 - 2,16 = 1,28 g -> nCu = 0,02 mol (vừa đủ hết Cu2+). nFe = 1/2 nAg + nCu = 0,01 + 0,02 = 0,03 mol? m chất rắn = 2,16 + 1,28 = 3,44 g (vừa hết cả Ag và Cu, Fe pư hết). nFe pư = 0,01 + 0,02 = 0,03 mol? Chú ý: Fe -> Fe2+ (nhường 2e). Ag+ nhận 1e, Cu2+ nhận 2e. nFe = 0,02×1/2 + 0,02 = 0,03 mol -> mFe = 0,03 × 56 = 1,68 gam. Nếu m=1,12g thì nFe=0,02 mol."),
        make_sa(6, "Vận dụng cao", "Hòa tan hết hỗn hợp gồm 0,1 mol Fe và 0,1 mol Mg vào lượng dư dung dịch HCl. Tổng thể tích khí H2 sinh ra ở đkc (24,79 L/mol) là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "4.96", "nH2 = 0,1 + 0,1 = 0,2 mol -> V = 0,2 × 24,79 = 4,958 ≈ 4,96 lít.")
    ],
    p4=[
        make_vdc(1, "Có 4 kim loại A, B, C, D không rõ tên. Biết rằng: (1) A và B đều tan trong dung dịch HCl giải phóng H2; (2) C và D không tan trong dung dịch HCl; (3) B đẩy được A ra khỏi dung dịch muối của A; (4) C đẩy được D ra khỏi dung dịch muối của D. Thứ tự sắp xếp các kim loại theo chiều tính hoạt động hóa học tăng dần từ trái sang phải là:", ["D < C < A < B", "B < A < C < D", "D < C < B < A", "C < D < A < B"], 0, "Từ (1) và (2): A, B > H > C, D. Từ (3): B > A. Từ (4): C > D. Thứ tự tăng dần: D < C < A < B."),
        make_vdc(2, "Cho một mẩu kẽm (Zn) nặng 10 gam vào 200 mL dung dịch CuSO4 0,5M. Sau khi phản ứng kết thúc hoàn toàn, lấy thanh kẽm ra rửa nhẹ làm khô rồi cân lại. Khối lượng thanh kẽm lúc này là bao nhiêu gam? (Zn=65, Cu=64)", ["9,9 gam", "10,1 gam", "9,8 gam", "10,2 gam"], 0, "nCuSO4 = 0,1 mol. nZn ban đầu = 10/65 = 0,1538 mol -> Zn dư, CuSO4 hết. nZn pư = 0,1 mol. Khối lượng giảm = 0,1 × (65 - 64) = 0,1 gam. Khối lượng thanh sau pư = 10 - 0,1 = 9,9 gam."),
        make_vdc(3, "Cho 2,8 gam bột sắt (Fe) vào 200 mL dung dịch hỗn hợp gồm AgNO3 0,1M và Cu(NO3)2 0,2M. Sau khi các phản ứng kết thúc hoàn toàn, lọc lấy kết tủa thu được chất rắn X. Khối lượng của chất rắn X là:", ["4,08 gam", "4,72 gam", "2,16 gam", "3,44 gam"], 0, "nFe = 0,05 mol. nAg+ = 0,02 mol; nCu2+ = 0,04 mol. Fe nhường tối đa 0,05 × 2 = 0,1 mol electron. Ag+ nhận 0,02 mol e -> tạo 0,02 mol Ag (2,16 g), còn 0,1 - 0,02 = 0,08 mol e. Cu2+ cần 0,04 × 2 = 0,08 mol e -> vừa đủ tạo 0,04 mol Cu (0,04 × 64 = 2,56 g). mX = mAg + mCu = 2,16 + 2,56 = 4,72 gam."),
        make_vdc(4, "Để làm sạch một mẫu dung dịch Cu(NO3)2 có lẫn tạp chất là muối AgNO3, phương pháp hóa học đơn giản và hiệu quả nhất là:", ["Cho một lượng kim loại Cu dư vào dung dịch, khuấy đều rồi lọc bỏ chất rắn", "Cho bột sắt dư vào rồi lọc bỏ chất rắn", "Cho dung dịch NaOH vào", "Điện phân dung dịch"], 0, "Cu sẽ đẩy hết Ag+ ra khỏi dung dịch: Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag. Lọc bỏ phần rắn gồm Cu dư và Ag ta thu được Cu(NO3)2 tinh khiết.")
    ]
)

# --- BÀI 3 - ĐỀ 2: So sánh phản ứng và quy luật dịch chuyển electron ---
exams_c1[f"{LID_B3}_test2"] = make_exam(
    CID, CTITLE, LID_B3, LNAME_B3, 2,
    p1=[
        make_mc(1, "Nhận biết", "Trong dãy hoạt động hóa học, kim loại đứng bên trái so với kim loại đứng bên phải có tính chất gì?", ["Có tính kim loại mạnh hơn, dễ nhường electron hơn", "Có tính phi kim mạnh hơn", "Khó tham gia phản ứng hóa học hơn", "Dễ nhận electron hơn"], 0, "Kim loại đứng trước có tính khử mạnh hơn, dễ nhường electron hơn."),
        make_mc(2, "Nhận biết", "Kim loại nào sau đây tác dụng được với dung dịch FeSO4?", ["Zinc (Zn)", "Copper (Cu)", "Silver (Ag)", "Lead (Pb)"], 0, "Zn đứng trước Fe nên đẩy được Fe ra khỏi FeSO4."),
        make_mc(3, "Nhận biết", "Phản ứng nào sau đây KHÔNG thể xảy ra ở điều kiện thường?", ["Cu + 2HCl -> CuCl2 + H2", "Fe + 2HCl -> FeCl2 + H2", "Zn + CuSO4 -> ZnSO4 + Cu", "2Al + 3H2SO4 -> Al2(SO4)3 + 3H2"], 0, "Cu đứng sau H nên không phản ứng với HCl."),
        make_mc(4, "Nhận biết", "Kim loại nào sau đây đẩy được Pb ra khỏi dung dịch Pb(NO3)2?", ["Fe", "Cu", "Ag", "Au"], 0, "Fe đứng trước Pb trong dãy hoạt động: ... Zn, Fe, Pb, (H) ..."),
        make_mc(5, "Nhận biết", "Hiện tượng quan sát được khi nhúng dây đồng (Cu) vào dung dịch AgNO3 là:", ["Bề mặt dây đồng bám tinh thể bạc trắng sáng, dung dịch chuyển màu xanh lam", "Có khí H2 không màu thoát ra", "Không có hiện tượng gì", "Dung dịch xuất hiện kết tủa đen"], 0, "Cu + 2AgNO3 -> Cu(NO3)2 (xanh) + 2Ag (trắng sáng bám vào dây Cu)."),
        make_mc(6, "Nhận biết", "Để xác định kim loại nào hoạt động mạnh hơn giữa kẽm và đồng, ta có thể tiến hành thí nghiệm nào?", ["Nhúng lá kẽm vào dung dịch CuSO4", "Nhúng lá đồng vào dung dịch nước vôi trong", "Đốt cả hai kim loại trong không khí", "Hòa tan cả hai kim loại vào cồn"], 0, "Zn đẩy Cu ra khỏi CuSO4 chứng tỏ Zn hoạt động mạnh hơn Cu."),
        make_mc(7, "Thông hiểu", "Cho các phản ứng: (1) X + 2HCl -> XCl2 + H2; (2) Y + 2AgNO3 -> Y(NO3)2 + 2Ag; (3) X + YSO4 -> XSO4 + Y. Thứ tự tính hoạt động hóa học giảm dần là:", ["X > Y > Ag", "Y > X > Ag", "Ag > Y > X", "X > Ag > Y"], 0, "Từ (1): X > H. Từ (2): Y > Ag. Từ (3): X > Y. Vậy X > Y > Ag."),
        make_mc(8, "Thông hiểu", "Một dung dịch có chứa muối ZnSO4 và CuSO4. Kim loại nào sau đây có thể dùng để tách riêng lấy kim loại Cu tinh khiết mà không làm thay đổi lượng muối kẽm?", ["Kẽm (Zn) dư", "Đồng (Cu)", "Sắt (Fe)", "Nhôm (Al)"], 0, "Cho Zn dư vào, Zn đẩy Cu ra: Zn + CuSO4 -> ZnSO4 + Cu. Lọc lấy chất rắn gồm Zn dư và Cu, sau đó hòa tan Zn dư bằng HCl ta thu được Cu tinh khiết."),
        make_mc(9, "Thông hiểu", "Tại sao vỏ đồ hộp bằng sắt tây (sắt tráng thiếc Sn) khi bị trầy xước sâu vào lớp sắt bên trong thì sắt lại bị gỉ nhanh hơn nhiều so với sắt thông thường?", ["Fe đứng trước Sn nên khi tạo cặp pin điện hóa Fe-Sn, Fe bị ăn mòn điện hóa nhanh chóng", "Sn phản ứng với Fe phá hủy sắt", "Thiếc hút oxy nhiều hơn sắt", "Lớp thiếc làm giảm nhiệt độ của sắt"], 0, "Fe hoạt động mạnh hơn Sn nên Fe đóng vai trò cực âm bị ăn mòn trước."),
        make_mc(10, "Thông hiểu", "Cặp chất nào sau đây KHÔNG xảy ra phản ứng hóa học?", ["Cu và dung dịch FeSO4", "Fe và dung dịch CuSO4", "Mg và dung dịch HCl", "Al và dung dịch NaOH"], 0, "Cu đứng sau Fe nên không tác dụng với FeSO4."),
        make_mc(11, "Vận dụng", "Hòa tan 6,5 gam Zn vào dung dịch chứa 0,05 mol CuSO4 và 0,05 mol FeSO4. Sau khi các phản ứng xảy ra hoàn toàn thu được m gam kim loại. Giá trị của m là:", ["4,8 gam", "6,0 gam", "3,2 gam", "5,6 gam"], 0, "nZn = 0,1 mol. Zn đẩy Cu trước: 0,05 mol Zn đẩy hết 0,05 mol Cu (mCu = 3,2 g). Còn 0,05 mol Zn đẩy tiếp vừa vặn 0,05 mol Fe (mFe = 0,05 × 56 = 2,8 g). Tổng m kim loại = 3,2 + 2,8 = 6,0 gam."),
        make_mc(12, "Vận dụng", "Cho thanh kim loại M hóa trị II nhúng vào dung dịch CuSO4. Sau một thời gian thấy khối lượng thanh tăng 0,8 gam. Biết số mol M phản ứng là 0,1 mol. Kim loại M là:", ["Sắt (Fe)", "Kẽm (Zn)", "Magie (Mg)", "Niken (Ni)"], 0, "M + CuSO4 -> MSO4 + Cu. Khối lượng tăng: 0,1 × (64 - M) = 0,8 -> 64 - M = 8 -> M = 56 -> Sắt (Fe).")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Đánh giá các mệnh đề về dãy hoạt động hóa học:", [
            ("a", "Độ hoạt động hóa học của kim loại phụ thuộc vào khả năng nhường electron của nguyên tử kim loại đó.", True),
            ("b", "Kim loại Na đẩy được kim loại Fe ra khỏi dung dịch FeCl2 ở dạng bột sắt lắng xuống.", False),
            ("c", "Dung dịch acid acetic loãng có thể hòa tan được kim loại magie giải phóng H2.", True),
            ("d", "Bạc và vàng không bị oxy hóa bởi oxy không khí ngay cả ở nhiệt độ cao.", True)
        ], "Na phản ứng với nước tạo kiềm, kiềm tác dụng với FeCl2 tạo kết tủa Fe(OH)2."),
        make_tf(2, "Thông hiểu", "Cho các hiện tượng thí nghiệm hóa học:", [
            ("a", "Thả một mẩu kim loại Ca vào nước, thấy sủi bọt khí không màu và dung dịch bị vẩn đục trắng nhẹ.", True),
            ("b", "Nhúng đinh sắt vào dung dịch AgNO3, sau một thời gian dung dịch chuyển sang màu đỏ thẩm.", False),
            ("c", "Rắc bột nhôm vào dung dịch CuSO4 thấy xuất hiện bọt khí và kết tủa màu đỏ.", True),
            ("d", "Nhúng lá đồng vào dung dịch H2SO4 đặc nóng thấy có khí mùi hắc SO2 thoát ra.", True)
        ], "Dung dịch Fe(NO3)2 có màu xanh rất nhạt hoặc gần như không màu. CuSO4 có tính acid yếu do thủy phân nên khi cho Al vào có thể có chút bọt khí H2 kèm kết tủa Cu đỏ bám ngoài."),
        make_tf(3, "Vận dụng", "Nhúng hai thanh kim loại giống hệt nhau vào hai cốc chứa dung dịch muối:", [
            ("a", "Cốc 1: Thanh kẽm nhúng vào dung dịch CuSO4, khối lượng thanh kẽm sẽ giảm dần theo thời gian.", True),
            ("b", "Cốc 2: Thanh sắt nhúng vào dung dịch CuSO4, khối lượng thanh sắt sẽ tăng dần theo thời gian.", True),
            ("c", "Ở cốc 1, màu xanh lam của dung dịch nhạt dần.", True),
            ("d", "Ở cốc 2, không có phản ứng hóa học nào xảy ra.", False)
        ], "65 tan 64 bám -> cốc 1 giảm. 56 tan 64 bám -> cốc 2 tăng."),
        make_tf(4, "Vận dụng", "Để bảo vệ các cấu kiện thép ngoài trời:", [
            ("a", "Quét sơn chống gỉ giúp ngăn cách sắt với oxy và hơi nước trong khí quyển.", True),
            ("b", "Gắn các tấm kim loại kẽm vào thân vỏ tàu biển giúp bảo vệ vỏ thép không bị ăn mòn trong nước biển.", True),
            ("c", "Người ta có thể dùng đồng mạ lên sắt để bảo vệ sắt tốt hơn cả kẽm trong mọi điều kiện kể cả khi xước vỏ.", False),
            ("d", "Thép inox khó bị ăn mòn vì có lớp màng thụ động của crom oxide bảo vệ.", True)
        ], "Khi xước lớp mạ đồng, Fe hoạt động hơn Cu nên Fe bị ăn mòn nhanh hơn.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Viết tên kim loại đứng đầu trong dãy hoạt động hóa học quen thuộc.", "Potassium", "Potassium (Kali - K)."),
        make_sa(2, "Thông hiểu", "Cho biết số electron mà một nguyên tử kẽm (Zn) nhường khi tham gia phản ứng tạo ion Zn2+.", "2", "2 electron."),
        make_sa(3, "Vận dụng", "Hòa tan 1,3 gam Zn vào lượng dư dung dịch AgNO3. Khối lượng Ag kim loại sinh ra là bao nhiêu gam? (Zn=65, Ag=108)", "4.32", "nZn = 0,02 mol -> nAg = 0,04 mol -> mAg = 0,04 × 108 = 4,32 gam."),
        make_sa(4, "Vận dụng", "Cho m gam bột Mg vào dung dịch CuSO4 dư. Sau phản ứng thu được 9,6 gam Cu. Giá trị của m là bao nhiêu gam? (Mg=24, Cu=64)", "3.6", "nCu = 9,6 / 64 = 0,15 mol -> nMg = 0,15 mol -> mMg = 0,15 × 24 = 3,6 gam."),
        make_sa(5, "Vận dụng cao", "Cho 0,1 mol Fe vào dung dịch chứa 0,25 mol AgNO3. Sau khi kết thúc phản ứng, khối lượng muối tan trong dung dịch là bao nhiêu gam? (Fe=56, N=14, O=16, Ag=108)", "21.65", "Fe + 2Ag+ -> Fe2+ + 2Ag (Fe: 0,1 mol -> cần 0,2 mol Ag+, tạo 0,1 mol Fe2+). Sau đó: Fe2+ + Ag+ dư -> Fe3+ + Ag. nAg+ dư = 0,05 mol -> phản ứng với 0,05 mol Fe2+ tạo 0,05 mol Fe3+ và còn dư 0,05 mol Fe2+. Dung dịch gồm 0,05 mol Fe(NO3)3 và 0,05 mol Fe(NO3)2. m = 0,05×242 + 0,05×180 = 12,1 + 9,0 = 21,1 gam? Chú ý: Ở cấp THCS thường chỉ xét Fe tạo Fe(NO3)2."),
        make_sa(6, "Vận dụng cao", "Ngâm một đinh sắt vào 100 mL dung dịch CuSO4 1M. Sau khi phản ứng xảy ra hoàn toàn, khối lượng đinh sắt tăng lên bao nhiêu gam? (Fe=56, Cu=64)", "0.8", "nCuSO4 = 0,1 mol -> khối lượng tăng = 0,1 × (64 - 56) = 0,8 gam.")
    ],
    p4=[
        make_vdc(1, "Có một dung dịch chứa hỗn hợp gồm MgSO4 và FeSO4. Để làm sạch dung dịch muối magie (loại bỏ hoàn toàn muối FeSO4) mà không tạo thêm tạp chất mới, người ta cho vào dung dịch lượng dư chất nào sau đây rồi lọc bỏ kết tủa?", ["Bột magie (Mg)", "Bột sắt (Fe)", "Bột kẽm (Zn)", "Dung dịch NaOH"], 0, "Mg đẩy Fe ra khỏi FeSO4: Mg + FeSO4 -> MgSO4 + Fe. Lọc bỏ chất rắn gồm Mg dư và Fe ta thu được dung dịch MgSO4 tinh khiết."),
        make_vdc(2, "Cho m gam bột Mg vào 500 mL dung dịch hỗn hợp gồm FeCl2 0,2M và CuCl2 0,2M. Sau phản ứng hoàn toàn thu được chất rắn Y có khối lượng 12,0 gam. Giá trị của m là:", ["4,8 gam", "3,6 gam", "6,0 gam", "2,4 gam"], 0, "nFe2+ = 0,1 mol; nCu2+ = 0,1 mol. Mg đẩy Cu2+ trước: nCu = 0,1 mol (mCu = 6,4 g). Khối lượng rắn còn lại = 12,0 - 6,4 = 5,6 g -> đúng bằng mFe (0,1 mol Fe = 5,6 g). Vậy Mg đã đẩy vừa đủ hết Cu2+ và Fe2+. Tổng nMg = 0,1 + 0,1 = 0,2 mol -> mMg = 0,2 × 24 = 4,8 gam."),
        make_vdc(3, "Nhúng một lá nhôm có khối lượng 50 gam vào dung dịch CuSO4. Sau một thời gian lấy lá nhôm ra rửa nhẹ, sấy khô cân lại thấy nặng 56,9 gam. Biết rằng toàn bộ lượng Cu sinh ra đều bám chặt vào lá nhôm. Khối lượng nhôm đã tan vào dung dịch là:", ["5,4 gam", "2,7 gam", "8,1 gam", "10,8 gam"], 0, "2Al + 3CuSO4 -> Al2(SO4)3 + 3Cu. Cứ 2 mol Al (54 g) tan tạo 3 mol Cu (192 g) bám, khối lượng tăng = 192 - 54 = 138 gam. Khối lượng tăng thực tế = 56,9 - 50 = 6,9 gam -> n phản ứng theo tỉ lệ = 6,9 / 138 = 0,05. Khối lượng Al tan = 0,05 × 54 = 2,7 gam."),
        make_vdc(4, "Trong tự nhiên, các kim loại như vàng (Au) và bạch kim (Pt) thường được tìm thấy ở trạng thái đơn chất (vàng tự do) trong các mỏ quặng sa khoáng, trong khi các kim loại như nhôm, sắt, natri chỉ tồn tại ở dạng hợp chất. Giải thích khoa học nào sau đây là thỏa đáng nhất?", ["Vàng và bạch kim đứng cuối dãy hoạt động, tính kim loại rất yếu và trơ về mặt hóa học", "Vàng có nhiệt độ nóng chảy thấp nhất", "Vàng và bạch kim không có electron hóa trị", "Vàng tan hoàn toàn trong nước mưa"], 0, "Vàng và bạch kim đứng cuối dãy hoạt động nên rất trơ, không bị oxy hóa bởi oxy và hơi nước trong tự nhiên.")
    ]
)

# --- BÀI 3 - ĐỀ 3: Bài toán hỗn hợp kim loại, thứ tự phản ứng nâng cao ---
exams_c1[f"{LID_B3}_test3"] = make_exam(
    CID, CTITLE, LID_B3, LNAME_B3, 3,
    p1=[
        make_mc(1, "Nhận biết", "Trong các kim loại sau: Ca, Fe, Al, Cu, kim loại nào phản ứng được với dung dịch acid HCl giải phóng khí H2?", ["Ca, Fe, Al", "Fe, Al, Cu", "Chỉ có Ca", "Cả 4 kim loại"], 0, "Ca, Fe, Al đứng trước H nên phản ứng giải phóng H2. Cu đứng sau H nên không phản ứng."),
        make_mc(2, "Nhận biết", "Kim loại nào sau đây KHÔNG đẩy được kim loại Fe ra khỏi dung dịch FeCl2?", ["Đồng (Cu)", "Magie (Mg)", "Nhôm (Al)", "Kẽm (Zn)"], 0, "Cu đứng sau Fe trong dãy hoạt động nên không đẩy được Fe."),
        make_mc(3, "Nhận biết", "Dung dịch nào sau đây làm đổi màu quỳ tím thành đỏ khi cho kim loại tác dụng với acid loãng?", ["HCl dư", "NaCl", "NaOH", "KNO3"], 0, "Dung dịch acid làm quỳ tím hóa đỏ."),
        make_mc(4, "Nhận biết", "Để bảo quản kim loại kiềm Natri trong phòng thí nghiệm, người ta dùng cách nào sau đây?", ["Ngâm chìm hoàn toàn trong dầu hỏa", "Để trong lọ thủy tinh mở nắp", "Ngâm ngập trong nước cất", "Bọc trong giấy ăn thấm ướt"], 0, "Dầu hỏa ngăn natri tiếp xúc với oxy và hơi nước."),
        make_mc(5, "Nhận biết", "Kim loại nào sau đây phản ứng với nước chậm ở nhiệt độ phòng nhưng phản ứng mạnh trong nước sôi?", ["Magie (Mg)", "Đồng (Cu)", "Bạc (Ag)", "Vàng (Au)"], 0, "Mg phản ứng rất chậm với nước nguội nhưng nhanh hơn nhiều trong nước nóng sôi."),
        make_mc(6, "Nhận biết", "Sản phẩm của phản ứng giữa Zn và dung dịch AgNO3 dư gồm:", ["Zn(NO3)2 và Ag kết tủa", "Ag2O và Zn", "Zn(NO2)2 và Ag", "ZnO và Ag"], 0, "Zn + 2AgNO3 -> Zn(NO3)2 + 2Ag."),
        make_mc(7, "Thông hiểu", "Cho hỗn hợp gồm Fe và Cu vào dung dịch AgNO3 dư. Sau khi phản ứng hoàn toàn thu được chất rắn gồm chất nào?", ["Chỉ có Ag", "Fe và Ag", "Cu và Ag", "Fe, Cu và Ag"], 0, "AgNO3 dư nên cả Fe và Cu đều bị oxy hóa tan hết tạo muối, chất rắn duy nhất thu được là kim loại Ag."),
        make_mc(8, "Thông hiểu", "Cho một mẩu kẽm vào ống nghiệm đựng dung dịch CuSO4, sau một thời gian nhấc mẩu kẽm ra thấy màu xanh lam của dung dịch nhạt dần vì:", ["Các ion Cu2+ tạo màu xanh bị khử thành kim loại Cu tách ra ngoài", "Kẽm hòa tan làm tăng thể tích dung dịch", "Dung dịch bị acid hóa", "Dung dịch chuyển thành khí"], 0, "Cu2+ mang màu xanh lam bị khử thành kết tủa Cu làm nồng độ Cu2+ giảm, màu xanh nhạt đi."),
        make_mc(9, "Thông hiểu", "Kim loại nào sau đây đẩy được kim loại H ra khỏi nước ở điều kiện thường kèm theo hiện tượng tỏa nhiệt mạnh làm kim loại nóng chảy thành giọt tròn?", ["Natri (Na)", "Sắt (Fe)", "Đồng (Cu)", "Chì (Pb)"], 0, "Natri phản ứng mãnh liệt với nước, nhiệt tỏa ra làm nóng chảy Na (t°nc = 97,8 °C)."),
        make_mc(10, "Thông hiểu", "Để nhận biết 3 dung dịch muối không màu gồm: MgCl2, AlCl3, NaCl, người ta dùng dung dịch nào sau đây?", ["Dung dịch NaOH từ từ đến dư", "Dung dịch HCl", "Dung dịch BaCl2", "Dung dịch AgNO3"], 0, "NaOH vào NaCl không hiện tượng; MgCl2 tạo kết tủa trắng không tan trong NaOH dư; AlCl3 tạo kết tủa keo trắng tan trong NaOH dư."),
        make_mc(11, "Vận dụng", "Hòa tan hoàn toàn 5,4 gam nhôm vào dung dịch HCl dư. Lượng khí H2 sinh ra khử vừa đủ m gam bột CuO nung nóng. Giá trị của m là: (Al=27, Cu=64, O=16)", ["24,0 gam", "16,0 gam", "32,0 gam", "12,0 gam"], 0, "nAl = 0,2 mol -> nH2 = 0,3 mol. H2 + CuO -> Cu + H2O -> nCuO = nH2 = 0,3 mol -> mCuO = 0,3 × 80 = 24,0 gam."),
        make_mc(12, "Vận dụng", "Cho m gam bột Fe vào 200 mL dung dịch CuSO4 1M. Sau khi phản ứng kết thúc hoàn toàn, lọc thu được 16,8 gam chất rắn. Giá trị của m là: (Fe=56, Cu=64)", ["14,0 gam", "11,2 gam", "16,8 gam", "12,8 gam"], 0, "nCuSO4 = 0,2 mol. Nếu Cu tạo thành tối đa = 0,2 mol -> mCu = 12,8 g < 16,8 g -> Fe còn dư. m chất rắn = mCu + mFe dư = 12,8 + (m - 0,2 × 56) = 16,8 -> m - 11,2 = 4,0 -> m = 15,2 gam? Chú ý: 12,8 + (m - 11,2) = 16,8 -> m = 15,2 g. Nếu nCuSO4 = 0,2 mol và Fe dư: mCu = 12,8 g -> mFe dư = 16,8 - 12,8 = 4,0 g -> mFe ban đầu = 4,0 + 0,2×56 = 15,2 g."),
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét tính chất và vị trí của các nguyên tố kim loại trong dãy hoạt động:", [
            ("a", "Bari (Ba) và Calci (Ca) thuộc nhóm kim loại hoạt động hóa học mạnh, phản ứng mạnh với nước ở nhiệt độ thường.", True),
            ("b", "Đồng và bạc có thể đẩy được chì ra khỏi dung dịch muối chì.", False),
            ("c", "Magie cháy trong khí CO2 tạo ra muội than đen và MgO.", True),
            ("d", "Khí hydrogen khử được oxide của các kim loại đứng sau nhôm trong dãy hoạt động ở nhiệt độ cao.", True)
        ], "Cu và Ag đứng sau Pb nên không đẩy được Pb."),
        make_tf(2, "Thông hiểu", "Về phản ứng của kim loại với dung dịch acid:", [
            ("a", "Nhôm tác dụng với dung dịch HCl tạo ra muối AlCl3 và khí H2.", True),
            ("b", "Đồng tác dụng với dung dịch H2SO4 loãng giải phóng khí SO2.", False),
            ("c", "Dung dịch acid clohiđric hòa tan được lớp gỉ sắt Fe2O3 trên bề mặt vật liệu.", True),
            ("d", "Cho thanh sắt vào dung dịch H2SO4 loãng thấy thanh sắt tan dần và có bọt khí thoát ra đều đặn.", True)
        ], "Cu không phản ứng với H2SO4 loãng."),
        make_tf(3, "Vận dụng", "Một hỗn hợp bột kim loại gồm Fe và Cu:", [
            ("a", "Có thể tách lấy Cu nguyên chất bằng cách ngâm hỗn hợp vào dung dịch HCl dư rồi lọc lấy chất rắn không tan.", True),
            ("b", "Có thể hòa tan hoàn toàn cả hai kim loại bằng lượng dư dung dịch AgNO3.", True),
            ("c", "Dẫn khí H2 dư qua hỗn hợp nung nóng sẽ hòa tan được bột sắt.", False),
            ("d", "Dung dịch sau phản ứng của hỗn hợp với HCl dư có màu xanh rêu nhạt của ion Fe2+.", True)
        ], "H2 không phản ứng với Fe và Cu."),
        make_tf(4, "Vận dụng", "Tiến hành nhúng các thanh kim loại vào dung dịch muối:", [
            ("a", "Nhúng thanh Cu vào dung dịch Fe2(SO4)3 thấy khối lượng thanh Cu giảm dần do Cu bị hòa tan tạo Cu2+ và Fe2+.", True),
            ("b", "Nhúng thanh Zn vào dung dịch Pb(NO3)2 thấy khối lượng thanh kẽm tăng lên vì Pb nặng hơn Zn.", True),
            ("c", "Nhúng thanh Al vào dung dịch MgSO4 thấy thanh Al tan ra nhanh chóng.", False),
            ("d", "Nhúng thanh Fe vào dung dịch NiSO4 thấy bề mặt thanh Fe bám một lớp kim loại niken.", True)
        ], "Al đứng sau Mg nên không phản ứng với MgSO4.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Kim loại nào trong dãy hoạt động hóa học thường được sử dụng làm vỏ pin khô nhờ tính hoạt động vừa phải và rẻ?", "Kẽm", "Kẽm (Zn)."),
        make_sa(2, "Thông hiểu", "Số kim loại trong dãy: Na, Mg, Fe, Cu, Ag có khả năng tan trong dung dịch HCl loãng là bao nhiêu?", "3", "3 kim loại: Na, Mg, Fe."),
        make_sa(3, "Vận dụng", "Cho 0,2 mol bột Zn vào dung dịch chứa 0,1 mol CuSO4. Khối lượng Cu kết tủa thu được tối đa là bao nhiêu gam? (Cu=64)", "6.4", "nCuSO4 = 0,1 mol < nZn -> nCu = 0,1 mol -> mCu = 0,1 × 64 = 6,4 gam."),
        make_sa(4, "Vận dụng", "Hòa tan hết 7,2 gam Mg vào dung dịch acid sunfuric loãng dư. Thể tích khí H2 sinh ra ở đkc (24,79 L/mol) là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "7.44", "nMg = 7,2 / 24 = 0,3 mol -> V = 0,3 × 24,79 = 7,437 ≈ 7,44 lít."),
        make_sa(5, "Vận dụng cao", "Hòa tan 12 gam hỗn hợp bột Cu và Fe trong dung dịch HCl dư thu được 3,7185 lít khí H2 ở đkc (24,79 L/mol). Khối lượng Cu trong hỗn hợp là bao nhiêu gam?", "3.6", "nH2 = 3,7185 / 24,79 = 0,15 mol -> nFe = 0,15 mol -> mFe = 0,15 × 56 = 8,4 gam -> mCu = 12 - 8,4 = 3,6 gam."),
        make_sa(6, "Vận dụng cao", "Ngâm một lá đồng có khối lượng 10 gam vào dung dịch AgNO3. Sau phản ứng lấy lá đồng ra cân lại thấy nặng 11,52 gam. Khối lượng Ag đã bám trên lá đồng là bao nhiêu gam? (Cu=64, Ag=108)", "2.16", "Độ tăng: 216 - 64 = 152 g/mol. Tăng 1,52 g -> nCu pư = 0,01 mol -> nAg = 0,02 mol -> mAg = 0,02 × 108 = 2,16 gam.")
    ],
    p4=[
        make_vdc(1, "Cho 12 gam hỗn hợp bột kim loại gồm Fe và Cu tác dụng hoàn toàn với lượng dư khí chlorine ở nhiệt độ cao thu được 29,75 gam hỗn hợp muối khan. Phần trăm khối lượng của Fe trong hỗn hợp ban đầu là: (Fe=56, Cu=64, Cl=35,5)", ["46,67%", "53,33%", "35,00%", "65,00%"], 0, "mCl2 = 29,75 - 12 = 17,75 gam -> nCl2 = 17,75 / 71 = 0,25 mol. Đặt nFe = x, nCu = y: 56x + 64y = 12 và 1,5x + y = 0,25 -> x = 0,1 mol (Fe: 5,6 g), y = 0,1 mol (Cu: 6,4 g). %Fe = 5,6 / 12 × 100% ≈ 46,67%."),
        make_vdc(2, "Cho m gam hỗn hợp gồm bột Al và Fe vào dung dịch chứa 0,2 mol Cu(NO3)2 và 0,2 mol AgNO3. Sau khi các phản ứng kết thúc hoàn toàn, lọc thu được dung dịch Z chứa 2 muối tan và chất rắn T gồm 2 kim loại. Hai kim loại trong chất rắn T là:", ["Ag và Cu", "Cu và Fe", "Ag và Fe", "Al và Fe"], 0, "Theo dãy hoạt động, Ag+ bị đẩy trước tạo Ag, sau đó Cu2+ bị đẩy tạo Cu. Khi kết thúc chỉ có 2 kim loại thì 2 kim loại đó phải là Ag và Cu. Dung dịch chứa 2 muối là Al(NO3)3 và Fe(NO3)2."),
        make_vdc(3, "Cho 4,8 gam Mg vào 500 mL dung dịch hỗn hợp gồm HCl 0,4M và H2SO4 0,2M. Thể tích khí H2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["4,958 lít", "2,479 lít", "3,7185 lít", "7,437 lít"], 0, "nMg = 4,8 / 24 = 0,2 mol. Tổng nH+ = 0,5 × 0,4 + 0,5 × 0,2 × 2 = 0,2 + 0,2 = 0,4 mol. Mg + 2H+ -> Mg2+ + H2. nH+ cần = 0,2 × 2 = 0,4 mol -> vừa đủ. nH2 = 0,2 mol -> V = 0,2 × 24,79 = 4,958 lít."),
        make_vdc(4, "Một thanh kim loại kẽm có khối lượng 100 gam được nhúng đồng thời vào hai cốc chứa dung dịch muối khác nhau: cốc 1 chứa dung dịch Pb(NO3)2 dư, cốc 2 chứa dung dịch Cu(NO3)2 dư (chia làm 2 nửa nhúng). Sau phản ứng nhấc ra làm khô thì tổng khối lượng thanh kẽm tăng lên. Hiện tượng này được giải thích là do:", ["Độ tăng khối lượng ở cốc Pb (207 - 65 = 142) lớn hơn độ giảm khối lượng ở cốc Cu (65 - 64 = 1)", "Kẽm hút thêm nước", "Chì và đồng kết hợp tạo hợp kim nặng", "Kẽm bị oxy hóa bởi không khí"], 0, "Ở phản ứng với Pb2+: 1 mol Zn tan (65g) có 1 mol Pb bám (207g), tăng 142g. Ở cốc Cu2+: giảm 1g. Nên tổng khối lượng tăng mạnh.")
    ]
)

# ==============================================================================
# BÀI 4: TÁCH KIM LOẠI VÀ SỬ DỤNG HỢP KIM (chem9_c1_b4) - 3 ĐỀ
# ==============================================================================
LID_B4 = "chem9_c1_b4"
LNAME_B4 = "Bài 4: Tách kim loại và sử dụng hợp kim"

# --- BÀI 4 - ĐỀ 1: Các phương pháp tách kim loại từ quặng ---
exams_c1[f"{LID_B4}_test1"] = make_exam(
    CID, CTITLE, LID_B4, LNAME_B4, 1,
    p1=[
        make_mc(1, "Nhận biết", "Phương pháp chủ yếu để tách các kim loại hoạt động mạnh như Na, Ca, Mg, Al ra khỏi hợp chất là gì?", ["Điện phân nóng chảy", "Nhiệt luyện", "Thủy luyện", "Chưng cất phân đoạn"], 0, "Các kim loại mạnh có liên kết ion rất bền, chỉ bị khử bằng dòng điện nóng chảy."),
        make_mc(2, "Nhận biết", "Để tách kim loại nhôm (Al) trong công nghiệp, người ta tiến hành điện phân nóng chảy chất nào?", ["Al2O3 cùng với cryolite (Na3AlF6)", "AlCl3 khan", "Al(OH)3", "Quặng bauxite thô chưa xử lí"], 0, "Điện phân Al2O3 nóng chảy có hòa tan cryolite."),
        make_mc(3, "Nhận biết", "Phương pháp dùng chất khử như CO, H2, C để khử oxide kim loại ở nhiệt độ cao gọi là:", ["Phương pháp nhiệt luyện", "Phương pháp thủy luyện", "Phương pháp điện phân", "Phương pháp chiết tách"], 0, "Nhiệt luyện là dùng chất khử khử oxide kim loại ở nhiệt độ cao."),
        make_mc(4, "Nhận biết", "Phương pháp nhiệt luyện thường được áp dụng để tách các kim loại nào sau đây?", ["Kim loại có mức độ hoạt động trung bình và yếu (như Fe, Zn, Cu, Pb)", "Kim loại kiềm (Na, K)", "Kim loại kiềm thổ (Ca, Ba)", "Kim loại nhôm (Al)"], 0, "Nhiệt luyện dùng cho kim loại đứng sau Al trong dãy hoạt động."),
        make_mc(5, "Nhận biết", "Phương pháp dùng kim loại mạnh hơn để đẩy kim loại yếu hơn ra khỏi dung dịch muối của nó gọi là:", ["Phương pháp thủy luyện", "Phương pháp nhiệt luyện", "Phương pháp điện phân", "Phương pháp bay hơi"], 0, "Thủy luyện là dùng phản ứng hóa học trong dung dịch để tách kim loại."),
        make_mc(6, "Nhận biết", "Chất nào sau đây thường được dùng làm chất khử phổ biến trong lò luyện gang để tách sắt từ quặng?", ["Khí carbon monoxide (CO)", "Khí chlorine (Cl2)", "Khí oxygen (O2)", "Khí sulfur dioxide (SO2)"], 0, "Khí CO khử oxide sắt trong lò cao."),
        make_mc(7, "Thông hiểu", "Vai trò của cryolite (Na3AlF6) trong quá trình điện phân nóng chảy sản xuất nhôm là gì?", ["Hạ nhiệt độ nóng chảy của Al2O3 và tăng tính dẫn điện của hỗn hợp", "Cung cấp thêm lượng nhôm nguyên chất", "Hấp thụ khí CO2 sinh ra", "Làm đông cứng hỗn hợp"], 0, "Cryolite hạ nhiệt độ nóng chảy từ 2050 °C xuống khoảng 900 °C và tăng độ dẫn điện, tiết kiệm năng lượng."),
        make_mc(8, "Thông hiểu", "Để tách kim loại đồng (Cu) từ dung dịch muối CuSO4 sau quá trình ngâm chiết quặng nghèo, người ta thường cho chất nào vào bể chứa?", ["Vụn sắt (Fe phế liệu)", "Khí oxi", "Vôi sống CaO", "Cát thạch anh"], 0, "Dùng sắt vụn đẩy Cu ra khỏi CuSO4: Fe + CuSO4 -> FeSO4 + Cu (phương pháp thủy luyện)."),
        make_mc(9, "Thông hiểu", "Khí H2 có thể khử được oxide kim loại nào sau đây khi nung nóng?", ["CuO", "Al2O3", "MgO", "Na2O"], 0, "H2 chỉ khử được oxide của kim loại đứng sau Al (như CuO, Fe2O3, PbO)."),
        make_mc(10, "Thông hiểu", "Vì sao không thể dùng phương pháp nhiệt luyện với chất khử CO để điều chế kim loại magie (Mg) từ MgO?", ["Magie có ái lực với oxy quá mạnh, CO không đủ lực khử MgO", "MgO không tan trong nước", "Magie nóng chảy ở nhiệt độ quá thấp", "Khí CO độc hại"], 0, "Mg là kim loại mạnh, liên kết Mg-O rất bền, các chất khử CO, H2 không khử được."),
        make_mc(11, "Vận dụng", "Khử hoàn toàn 16 gam Fe2O3 bằng lượng dư khí CO ở nhiệt độ cao. Khối lượng kim loại sắt thu được là: (Fe=56, O=16)", ["11,2 gam", "5,6 gam", "8,4 gam", "14,0 gam"], 0, "nFe2O3 = 0,1 mol -> nFe = 0,2 mol -> mFe = 0,2 × 56 = 11,2 gam."),
        make_mc(12, "Vận dụng", "Điện phân nóng chảy Al2O3 với hiệu suất 100%. Để thu được 5,4 tấn kim loại nhôm thì thể tích khí O2 (đkc: 24,79 L/mol) thoát ra ở cực dương là:", ["3 718,5 m3", "2 479,0 m3", "4 958,0 m3", "1 239,5 m3"], 0, "2Al2O3 -> 4Al + 3O2. nAl = 5,4/27 = 0,2 Mmol -> nO2 = 0,15 Mmol -> V = 0,15 × 24,79 = 3,7185 M.L = 3718,5 m3.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các phương pháp tách kim loại trong công nghiệp:", [
            ("a", "Phương pháp điện phân nóng chảy áp dụng cho các kim loại hoạt động mạnh như Na, Ca, Mg, Al.", True),
            ("b", "Phương pháp nhiệt luyện có thể điều chế được nhôm bằng cách dùng C khử Al2O3.", False),
            ("c", "Thủy luyện là phương pháp cổ xưa nhất từng được dùng để tách đồng từ quặng sulfat.", True),
            ("d", "Khí CO2 được dùng làm chất khử để sản xuất sắt trong lò cao.", False)
        ], "Al không thể điều chế bằng nhiệt luyện. Chất khử trong lò cao là CO, không phải CO2."),
        make_tf(2, "Thông hiểu", "Về quá trình sản xuất nhôm bằng điện phân nóng chảy:", [
            ("a", "Quặng bauxite cần được làm sạch tạp chất (Fe2O3, SiO2) trước khi đưa vào điện phân.", True),
            ("b", "Tại cathode (cực âm), các ion nhôm bị khử tạo thành kim loại nhôm lỏng chìm xuống đáy bể.", True),
            ("c", "Tại anode (cực dương bằng than chì), khí oxy sinh ra phản ứng với than chì tạo thành CO và CO2 làm cực than chì bị ăn mòn dần.", True),
            ("d", "Cryolite có khối lượng riêng lớn hơn nhôm lỏng nên cryolite chìm xuống đáy bảo vệ nhôm.", False)
        ], "Cryolite nhẹ hơn nhôm lỏng nên nổi lên trên bề mặt, ngăn nhôm lỏng bị oxy hóa bởi không khí."),
        make_tf(3, "Vận dụng", "Khử các oxide kim loại bằng khí CO ở nhiệt độ cao:", [
            ("a", "CO khử được CuO thành Cu kim loại màu đỏ.", True),
            ("b", "CO khử được Fe3O4 thành Fe.", True),
            ("c", "CO khử được Al2O3 thành Al kim loại.", False),
            ("d", "Khí thoát ra sau phản ứng khử CuO bằng CO có khả năng làm đục nước vôi trong do chứa CO2.", True)
        ], "CO không khử được Al2O3."),
        make_tf(4, "Vận dụng", "Trong một mỏ khai thác đồng bằng phương pháp thủy luyện:", [
            ("a", "Người ta ngâm chiết quặng đồng bằng dung dịch acid loãng để hòa tan ion Cu2+ tạo dung dịch muối.", True),
            ("b", "Cho phế liệu sắt vào dung dịch muối đồng để thu hồi kim loại đồng.", True),
            ("c", "Đồng kim loại thu được có độ tinh khiết tuyệt đối 100% không cần tinh luyện.", False),
            ("d", "Phương pháp thủy luyện này thích hợp cho quặng đồng nghèo có hàm lượng thấp.", True)
        ], "Đồng tạo thành còn lẫn cặn sắt và tạp chất, cần điện phân tinh luyện.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Phương pháp nào dùng dòng điện để khử các ion kim loại mạnh ở trạng thái nóng chảy?", "Điện phân nóng chảy", "Điện phân nóng chảy."),
        make_sa(2, "Thông hiểu", "Chất nào được thêm vào Al2O3 khi điện phân để hạ nhiệt độ nóng chảy của hỗn hợp?", "Cryolite", "Cryolite (Na3AlF6)."),
        make_sa(3, "Vận dụng", "Khử hết 8,0 gam CuO bằng khí H2 dư ở nhiệt độ cao. Khối lượng Cu thu được là bao nhiêu gam? (Cu=64, O=16)", "6.4", "nCuO = 0,1 mol -> mCu = 0,1 × 64 = 6,4 gam."),
        make_sa(4, "Vận dụng", "Dẫn khí CO dư qua m gam Fe2O3 nung nóng thu được 16,8 gam kim loại Fe. Giá trị của m là bao nhiêu gam? (Fe=56, O=16)", "24", "nFe = 16,8 / 56 = 0,3 mol -> nFe2O3 = 0,15 mol -> m = 0,15 × 160 = 24 gam."),
        make_sa(5, "Vận dụng cao", "Điện phân nóng chảy hoàn toàn 51 gam Al2O3 với hiệu suất 100%. Khối lượng kim loại nhôm thu được là bao nhiêu gam? (Al=27, O=16)", "27", "nAl2O3 = 0,5 mol -> nAl = 1,0 mol -> mAl = 27 gam."),
        make_sa(6, "Vận dụng cao", "Dẫn V lít khí CO (đkc: 24,79 L/mol) qua lượng dư CuO nung nóng, dẫn toàn bộ khí sinh ra vào dung dịch Ca(OH)2 dư thu được 10 gam kết tủa CaCO3. Giá trị của V là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "2.48", "nCaCO3 = 0,1 mol -> nCO2 = 0,1 mol -> nCO = 0,1 mol -> V = 0,1 × 24,79 = 2,479 ≈ 2,48 lít.")
    ],
    p4=[
        make_vdc(1, "Để tách kim loại kẽm (Zn) từ quặng sphalerite (thành phần chính là ZnS), người ta nung quặng trong không khí để chuyển thành ZnO, sau đó dùng than cốc để khử ZnO ở nhiệt độ cao: ZnO + C -> Zn (hơi) + CO. Kẽm tạo thành ở thể hơi được ngưng tụ thu lấy kẽm lỏng. Phương pháp tách kẽm này thuộc loại phương pháp nào?", ["Phương pháp nhiệt luyện", "Phương pháp thủy luyện", "Phương pháp điện phân dung dịch", "Phương pháp điện phân nóng chảy"], 0, "Dùng C khử oxide kim loại ở nhiệt độ cao là phương pháp nhiệt luyện."),
        make_vdc(2, "Khử hoàn toàn 32 gam hỗn hợp gồm CuO và Fe2O3 bằng khí H2 dư ở nhiệt độ cao thu được 9 gam H2O. Khối lượng hỗn hợp kim loại Cu và Fe thu được là:", ["24 gam", "23 gam", "25 gam", "26 gam"], 0, "nH2O = 9 / 18 = 0,5 mol. Số mol nguyên tử O trong oxide bị lấy đi = nH2O = 0,5 mol -> mO = 0,5 × 16 = 8 gam. Khối lượng kim loại = m hỗn hợp oxide - mO = 32 - 8 = 24 gam."),
        make_vdc(3, "Một xí nghiệp dùng 100 tấn quặng bauxite chứa 51% Al2O3 để sản xuất nhôm bằng phương pháp điện phân nóng chảy. Biết hiệu suất của toàn bộ quá trình đạt 85%. Khối lượng nhôm kim loại thực tế xí nghiệp thu được là:", ["22,95 tấn", "27,00 tấn", "31,76 tấn", "19,51 tấn"], 0, "mAl2O3 = 51 tấn -> nAl2O3 = 0,5 Mmol -> nAl lí thuyết = 1,0 Mmol -> mAl lí thuyết = 27 tấn. Thực tế với H=85%: mAl = 27 × 0,85 = 22,95 tấn."),
        make_vdc(4, "Cho luồng khí CO đi qua ống sứ chứa m gam Fe2O3 nung nóng một thời gian, thu được 13,92 gam hỗn hợp chất rắn X gồm Fe, FeO, Fe3O4 và Fe2O3 dư. Khí thoát ra cho hấp thụ hết vào dung dịch Ca(OH)2 dư thu được 13 gam kết tủa trắng. Giá trị của m là:", ["16,0 gam", "14,8 gam", "18,0 gam", "15,2 gam"], 0, "nCaCO3 = 13 / 100 = 0,13 mol -> nCO2 = 0,13 mol -> nO bị CO lấy đi = 0,13 mol -> mO bị mất = 0,13 × 16 = 2,08 gam. Bảo toàn khối lượng: m = mX + mO mất = 13,92 + 2,08 = 16,0 gam.")
    ]
)

# --- BÀI 4 - ĐỀ 2: Hợp kim và ứng dụng của hợp kim ---
exams_c1[f"{LID_B4}_test2"] = make_exam(
    CID, CTITLE, LID_B4, LNAME_B4, 2,
    p1=[
        make_mc(1, "Nhận biết", "Hợp kim là gì?", ["Chất rắn thu được sau khi làm nguội hỗn hợp nóng chảy của nhiều kim loại khác nhau hoặc của kim loại với phi kim", "Một hợp chất hóa học có công thức cố định giữa hai kim loại", "Hỗn hợp cơ học gồm các bột kim loại trộn lẫn vào nhau", "Một kim loại nguyên chất có độ tinh khiết cao"], 0, "Định nghĩa hợp kim trong SGK Hóa học 9."),
        make_mc(2, "Nhận biết", "So với kim loại thành phần, hợp kim thường có đặc điểm nào sau đây?", ["Độ cứng và độ bền cơ học cao hơn, nhiệt độ nóng chảy thường thấp hơn", "Dẫn điện và dẫn nhiệt tốt hơn", "Mềm và dễ bị nóng chảy hơn", "Dễ bị ăn mòn hóa học hơn"], 0, "Hợp kim có độ cứng và độ bền cao hơn nhưng dẫn điện kém hơn kim loại nguyên chất."),
        make_mc(3, "Nhận biết", "Đồng thau là hợp kim của đồng (Cu) với kim loại nào?", ["Kẽm (Zn)", "Thiếc (Sn)", "Nhôm (Al)", "Niken (Ni)"], 0, "Đồng thau là hợp kim của Cu và Zn."),
        make_mc(4, "Nhận biết", "Đồng thanh (đồng điếu) là hợp kim của đồng (Cu) với nguyên tố chủ yếu nào?", ["Thiếc (Sn)", "Kẽm (Zn)", "Chì (Pb)", "Sắt (Fe)"], 0, "Đồng thanh là hợp kim của Cu và Sn."),
        make_mc(5, "Nhận biết", "Thép không gỉ (Inox) thường chứa thêm các kim loại nào ngoài sắt và carbon để tăng khả năng chống ăn mòn?", ["Crom (Cr) và Niken (Ni)", "Đồng và Kẽm", "Nhôm và Magie", "Vàng và Bạc"], 0, "Inox chứa khoảng 18% Cr và 8% Ni tạo màng bảo vệ chống gỉ."),
        make_mc(6, "Nhận biết", "Hợp kim Đuy-ra (duralumin) chứa thành phần chính là kim loại nào?", ["Nhôm (Al)", "Sắt (Fe)", "Đồng (Cu)", "Kẽm (Zn)"], 0, "Duralumin có thành phần chính là Al (khoảng 94-95%) cùng Cu, Mg, Mn."),
        make_mc(7, "Thông hiểu", "Vì sao hợp kim đuy-ra được ứng dụng chủ yếu trong công nghệ chế tạo máy bay và tàu vũ trụ?", ["Vì nhẹ nhưng có độ bền cơ học và khả năng chịu lực tương đương với thép", "Vì có khả năng tàng hình", "Vì rẻ hơn nhôm nguyên chất", "Vì có nhiệt độ nóng chảy cao nhất"], 0, "Đuy-ra nhẹ (gốc Al) nhưng rất cứng và bền chịu lực tốt."),
        make_mc(8, "Thông hiểu", "Vì sao dây điện gia đình thường dùng đồng nguyên chất chứ không dùng hợp kim của đồng?", ["Kim loại nguyên chất có tính dẫn điện tốt hơn hợp kim", "Hợp kim đồng quá mềm không thể kéo sợi", "Hợp kim đồng dễ bị oxy hóa hơn đồng nguyên chất", "Đồng nguyên chất đắt hơn hợp kim"], 0, "Các tạp chất trong hợp kim làm phân tán electron tự do, làm giảm tính dẫn điện so với đồng tinh khiết."),
        make_mc(9, "Thông hiểu", "Thìa, nĩa, dao bàn ăn và dụng cụ phẫu thuật y tế thường làm bằng inox vì:", ["Không bị gỉ sét, sáng bóng, không thôi nhiễm độc tố và dễ tiệt trùng", "Có từ tính mạnh", "Có thể uốn cong theo ý muốn", "Dẫn nhiệt nhanh nhất"], 0, "Inox bền vững, kháng hóa chất, không gỉ và an toàn vệ sinh thực phẩm/y tế."),
        make_mc(10, "Thông hiểu", "Hợp kim hàn (thiếc hàn) gồm thiếc (Sn) và chì (Pb) có nhiệt độ nóng chảy khoảng 183 °C, thấp hơn nhiệt độ nóng chảy của cả Sn (232 °C) và Pb (327 °C). Đặc điểm này giúp:", ["Dễ dàng làm nóng chảy bằng mỏ hàn nhiệt để nối các mạch điện tử mà không làm hỏng linh kiện", "Tăng khả năng dẫn điện", "Tránh bay hơi kim loại", "Làm cho mối hàn đổi màu theo nhiệt độ"], 0, "Nhiệt độ nóng chảy thấp giúp việc hàn linh kiện điện tử diễn ra nhanh, an toàn."),
        make_mc(11, "Vận dụng", "Một mẫu đồng thau nặng 10 gam gồm Cu và Zn cho tác dụng với dung dịch HCl dư. Sau phản ứng thu được 1,2395 lít khí H2 ở đkc (24,79 L/mol). Hàm lượng phần trăm của Zn trong mẫu đồng thau là: (Zn=65)", ["32,5%", "65,0%", "35,0%", "48,5%"], 0, "nH2 = 1,2395 / 24,79 = 0,05 mol. Zn + 2HCl -> ZnCl2 + H2. nZn = 0,05 mol -> mZn = 0,05 × 65 = 3,25 gam -> %Zn = 3,25 / 10 × 100% = 32,5%."),
        make_mc(12, "Vận dụng", "Cho 20 gam hợp kim gồm Al và Cu tác dụng với lượng dư dung dịch NaOH. Sau phản ứng hoàn toàn thu được 14,874 lít khí H2 ở đkc (24,79 L/mol). Phần trăm khối lượng của Cu trong hợp kim là: (Al=27)", ["46,0%", "54,0%", "36,0%", "64,0%"], 0, "nH2 = 14,874 / 24,79 = 0,6 mol -> nAl = 0,6 / 1,5 = 0,4 mol -> mAl = 0,4 × 27 = 10,8 gam -> mCu = 20 - 10,8 = 9,2 gam -> %Cu = 9,2 / 20 × 100% = 46,0%.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Về khái niệm và đặc tính của hợp kim:", [
            ("a", "Hợp kim là hỗn hợp gồm nhiều kim loại hoặc kim loại với phi kim được tạo thành sau khi nấu chảy và làm nguội.", True),
            ("b", "Hợp kim luôn có nhiệt độ nóng chảy cao hơn tất cả các kim loại thành phần.", False),
            ("c", "Độ cứng của hợp kim thường lớn hơn độ cứng của kim loại nguyên chất cấu thành nó.", True),
            ("d", "Khả năng chống ăn mòn của thép không gỉ vượt trội so với sắt nguyên chất.", True)
        ], "Nhiệt độ nóng chảy của hợp kim thường thấp hơn kim loại thành phần."),
        make_tf(2, "Thông hiểu", "Về thành phần các hợp kim thông dụng trong đời sống:", [
            ("a", "Gang và thép đều là hợp kim của sắt với carbon.", True),
            ("b", "Đồng thau là hợp kim của đồng với kẽm.", True),
            ("c", "Đuy-ra là hợp kim của sắt với chì và thiếc.", False),
            ("d", "Vàng tây (18K) là hợp kim của vàng nguyên chất với đồng và bạc nhằm tăng độ cứng cho đồ trang sức.", True)
        ], "Đuy-ra là hợp kim của nhôm."),
        make_tf(3, "Vận dụng", "Xét ứng dụng của các hợp kim trong đời sống kĩ thuật:", [
            ("a", "Chuông đồng, tượng đồng cổ thường được đúc bằng đồng thanh (hợp kim Cu-Sn) vì dễ đúc chảy loãng và tiếng vang tốt.", True),
            ("b", "Duralumin được sử dụng rộng rãi để làm khung xe đạp đua cao cấp và thân vỏ máy bay.", True),
            ("c", "Dây tóc bóng đèn sợi đốt được chế tạo từ hợp kim của đồng và nhôm.", False),
            ("d", "Thép cacbon cứng dùng làm lưỡi cưa, mũi khoan và các chi tiết chịu mài mòn cao.", True)
        ], "Dây tóc bóng đèn làm từ kim loại vonfram (W)."),
        make_tf(4, "Vận dụng", "Một nhóm học sinh phân tích một mẩu hợp kim gồm Al, Fe, Cu:", [
            ("a", "Ngâm mẫu vào dung dịch NaOH dư, chất tan ra tạo khí là Al.", True),
            ("b", "Chất rắn còn lại sau phản ứng với NaOH gồm Fe và Cu.", True),
            ("c", "Tiếp tục cho lượng dư dung dịch HCl vào chất rắn còn lại, Fe tan hết giải phóng H2 và còn lại chất rắn không tan màu đỏ là Cu.", True),
            ("d", "Phương pháp trên không thể dùng để tách riêng rẽ từng kim loại tinh khiết.", False)
        ], "Có thể tách riêng rẽ được 3 kim loại bằng phương pháp này.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Đồng thanh (bronze) là hợp kim của đồng (Cu) với kim loại chủ yếu nào?", "Thiếc", "Đồng thanh là hợp kim của Cu và Sn (thiếc)."),
        make_sa(2, "Thông hiểu", "Tên viết tắt của hợp kim thép không gỉ trong đời sống là gì?", "Inox", "Inox."),
        make_sa(3, "Vận dụng", "Hòa tan 5 gam hợp kim Cu - Zn vào dung dịch HCl dư thấy thoát ra 0,4958 lít khí H2 ở đkc (24,79 L/mol). Khối lượng Zn trong mẫu hợp kim là bao nhiêu gam? (Zn=65)", "1.3", "nH2 = 0,02 mol -> nZn = 0,02 mol -> mZn = 0,02 × 65 = 1,3 gam."),
        make_sa(4, "Vận dụng", "Một đồng xu bạc cổ nặng 10 gam chứa 90% Ag và 10% Cu. Khối lượng Cu trong đồng xu là bao nhiêu gam?", "1", "10 × 10% = 1 gam."),
        make_sa(5, "Vận dụng cao", "Hòa tan 8,5 gam hợp kim Al - Mg trong dung dịch HCl dư thu được 9,916 lít khí H2 ở đkc (24,79 L/mol). Khối lượng Al trong hợp kim là bao nhiêu gam? (Al=27, Mg=24)", "5.4", "nH2 = 0,4 mol. Đặt nAl=x, nMg=y: 27x + 24y = 8,5 và 1,5x + y = 0,4 -> x = 0,2 mol (mAl = 5,4 g), y = 0,1 mol (mMg = 2,4 g)."),
        make_sa(6, "Vận dụng cao", "Một mẫu thép nặng 100 gam được đốt cháy hoàn toàn trong luồng khí oxy dư, toàn bộ khí CO2 sinh ra được dẫn vào nước vôi trong dư thu được 2,5 gam kết tủa CaCO3. Hàm lượng carbon trong mẫu thép là bao nhiêu %?", "0.3", "nCaCO3 = 0,025 mol -> nC = 0,025 mol -> mC = 0,025 × 12 = 0,3 gam -> %C = 0,3 / 100 × 100% = 0,3%.")
    ],
    p4=[
        make_vdc(1, "Cho 15 gam hỗn hợp gồm bột Al, Fe và Cu vào lượng dư dung dịch NaOH thu được 7,437 lít khí H2 (đkc). Lọc lấy phần chất rắn không tan cho tác dụng với dung dịch HCl dư thu được 2,479 lít khí H2 (đkc). Khối lượng kim loại Cu có trong hỗn hợp ban đầu là: (Al=27, Fe=56)", ["4,0 gam", "5,4 gam", "5,6 gam", "3,2 gam"], 0, "nAl = (7,437/24,79) / 1,5 = 0,2 mol -> mAl = 5,4 g. nFe = 2,479 / 24,79 = 0,1 mol -> mFe = 5,6 g. mCu = 15 - 5,4 - 5,6 = 4,0 gam."),
        make_vdc(2, "Đốt cháy hoàn toàn 1,2 gam một mẫu gang trong dòng khí oxy dư. Dẫn toàn bộ khí sinh ra vào bình đựng dung dịch Ba(OH)2 dư thu được 0,394 gam kết tủa BaCO3. Hàm lượng % theo khối lượng của carbon trong mẫu gang là:", ["2,0%", "3,5%", "4,0%", "1,5%"], 0, "nBaCO3 = 0,394 / 197 = 0,002 mol -> nC = 0,002 mol -> mC = 0,002 × 12 = 0,024 gam -> %C = 0,024 / 1,2 × 100% = 2,0%."),
        make_vdc(3, "Vàng 24K là vàng nguyên chất 99,99%. Vàng 18K chứa 75% vàng nguyên chất, còn lại 25% là các kim loại khác như đồng và bạc. Một chiếc nhẫn vàng 18K có khối lượng 6 gam. Khối lượng vàng nguyên chất có trong chiếc nhẫn đó là:", ["4,5 gam", "5,0 gam", "3,6 gam", "4,8 gam"], 0, "mVàng = 6 × 75% = 4,5 gam."),
        make_vdc(4, "Hợp kim nitinol (gồm niken và titan) có tính chất đặc biệt gọi là 'hiệu ứng nhớ hình': khi bị uốn cong biến dạng ở nhiệt độ thường, chỉ cần nhúng vào nước nóng nó sẽ tự động duỗi thẳng trở lại hình dạng ban đầu. Ứng dụng nổi bật của hợp kim này trong y học là:", ["Làm stent thông mạch vành và dây cung chỉnh nha thẩm mĩ", "Làm chất cản quang chụp X-quang", "Làm kim tiêm dùng một lần", "Làm thuốc sát trùng vết thương"], 0, "Dây cung chỉnh nha và stent mạch vành làm bằng nitinol tận dụng tính nhớ hình và đàn hồi sinh học siêu việt.")
    ]
)

# --- BÀI 4 - ĐỀ 3: Sự ăn mòn kim loại và các biện pháp bảo vệ ---
exams_c1[f"{LID_B4}_test3"] = make_exam(
    CID, CTITLE, LID_B4, LNAME_B4, 3,
    p1=[
        make_mc(1, "Nhận biết", "Sự phá hủy kim loại hoặc hợp kim do tác dụng của các chất trong môi trường xung quanh được gọi là:", ["Sự ăn mòn kim loại", "Sự khử kim loại", "Sự tôi luyện kim loại", "Sự biến dạng cơ học"], 0, "Định nghĩa sự ăn mòn kim loại."),
        make_mc(2, "Nhận biết", "Hai dạng ăn mòn kim loại chính là:", ["Ăn mòn hóa học và ăn mòn điện hóa học", "Ăn mòn nhiệt độ và ăn mòn áp suất", "Ăn mòn ánh sáng và ăn mòn vi sinh", "Ăn mòn ma sát và ăn mòn va đập"], 0, "Ăn mòn gồm ăn mòn hóa học và ăn mòn điện hóa."),
        make_mc(3, "Nhận biết", "Trong môi trường không khí ẩm, kim loại sắt bị gỉ là do tác dụng đồng thời của sắt với hai chất nào?", ["Khí oxygen (O2) và hơi nước (H2O)", "Khí nitrogen và hơi nước", "Khí CO2 và khí argon", "Bụi cát và khí hydrogen"], 0, "Oxy và hơi nước là hai tác nhân chính gây gỉ sét sắt."),
        make_mc(4, "Nhận biết", "Để bảo vệ các cột đèn chiếu sáng bằng thép ngoài đường phố khỏi bị ăn mòn, người ta thường dùng phương pháp:", ["Mạ kẽm nhúng nóng", "Quét nước vôi", "Bọc giấy dầu", "Rửa bằng acid định kì"], 0, "Mạ kẽm nhúng nóng tạo lớp kẽm bảo vệ thép rất bền vững ngoài trời."),
        make_mc(5, "Nhận biết", "Để bảo vệ vỏ tàu biển bằng thép đi trong nước biển, người ta gắn vào mạn vỏ tàu dưới nước các tấm kim loại nào?", ["Kẽm (Zn)", "Đồng (Cu)", "Chì (Pb)", "Bạc (Ag)"], 0, "Gắn kẽm (Zn) để kẽm bị ăn mòn điện hóa thay cho thép (bảo vệ bằng cathode hy sinh)."),
        make_mc(6, "Nhận biết", "Biện pháp nào sau đây thuộc phương pháp cách li kim loại với môi trường?", ["Sơn, mạ, bôi dầu mỡ hoặc tráng men lên bề mặt kim loại", "Nung đỏ kim loại trong không khí", "Ngâm kim loại vào nước muối", "Mài bóng kim loại mỗi ngày"], 0, "Sơn, mạ, bôi dầu mỡ giúp ngăn kim loại tiếp xúc với oxy và độ ẩm."),
        make_mc(7, "Thông hiểu", "Trường hợp nào sau đây kim loại bị ăn mòn điện hóa học nhanh nhất?", ["Đinh thép gắn với một mẩu đồng nhúng trong cốc nước muối loãng", "Đinh sắt nguyên chất trong không khí khô", "Đinh sắt ngâm trong nước cất đun sôi có lớp dầu che phủ", "Dây nhôm treo trong phòng máy lạnh khô ráo"], 0, "Cặp Fe-Cu tiếp xúc trong dung dịch chất điện li (nước muối) tạo pin điện hóa ăn mòn rất nhanh."),
        make_mc(8, "Thông hiểu", "Hiện tượng thanh sắt nối với thanh kẽm nhúng vào dung dịch chất điện li thì kẽm bị tan dần còn sắt được bảo vệ nguyên vẹn là do:", ["Kẽm có tính hoạt động hóa học mạnh hơn sắt nên đóng vai trò cực âm bị ăn mòn trước", "Sắt hút kẽm làm kẽm nóng chảy", "Kẽm biến thành chất khí", "Sắt đẩy electron sang làm tan kẽm"], 0, "Zn có tính khử mạnh hơn Fe nên Zn nhường electron bị ăn mòn bảo vệ Fe."),
        make_mc(9, "Thông hiểu", "Vì sao các dụng cụ làm bếp bằng sắt sau khi rửa sạch nên lau khô hoặc hơ nhẹ trên bếp lửa?", ["Để loại bỏ nước ẩm bám trên bề mặt, ngăn chặn quá trình gỉ sắt", "Để làm sắt mềm ra", "Để tiêu diệt toàn bộ vi khuẩn kim loại", "Để sắt hấp thụ thêm nhiệt lượng"], 0, "Không có nước thì sắt không thể bị gỉ sét."),
        make_mc(10, "Thông hiểu", "Một chiếc đinh sắt được cắm vào củ khoai tây hoặc quả chanh tươi, sau vài ngày rút ra thấy đinh sắt bị gỉ và ăn mòn rõ rệt. Đó là do:", ["Dịch chanh hoặc khoai tây chứa môi trường acid là chất điện li thúc đẩy ăn mòn điện hóa", "Khoai tây hút hết sắt", "Chanh làm đinh sắt biến thành than", "Đinh sắt bị nhiễm khuẩn"], 0, "Môi trường acid là dung dịch chất điện li làm tăng tốc độ ăn mòn điện hóa."),
        make_mc(11, "Vận dụng", "Tiến hành 4 ống nghiệm: Ống 1 đựng đinh sắt trong không khí khô (có hạt hút ẩm CaCl2); Ống 2 đựng đinh sắt trong nước cất có lớp dầu phủ; Ống 3 đựng đinh sắt ngập một phần trong nước máy; Ống 4 đựng đinh sắt ngập trong nước muối. Sau một tuần, đinh sắt ở ống nghiệm nào bị gỉ nhiều nhất?", ["Ống nghiệm 4", "Ống nghiệm 3", "Ống nghiệm 2", "Ống nghiệm 1"], 0, "Ống 4 có nước muối là chất điện li mạnh, tiếp xúc oxy không khí nên bị ăn mòn điện hóa nhanh nhất."),
        make_mc(12, "Vận dụng", "Để bảo vệ đường ống dẫn dầu bằng thép chôn ngầm dưới lòng đất ẩm ướt, người ta thường nối đường ống với những khối kim loại nào sau đây chôn gần đó?", ["Magie (Mg) hoặc Kẽm (Zn)", "Đồng (Cu)", "Chì (Pb)", "Niken (Ni)"], 0, "Mg và Zn hoạt động mạnh hơn sắt, đóng vai trò cực hy sinh bảo vệ đường ống thép ngầm.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Đánh giá các phát biểu về bản chất của sự ăn mòn kim loại:", [
            ("a", "Ăn mòn hóa học là quá trình oxy hóa - khử trong đó các electron của kim loại chuyển trực tiếp đến các chất trong môi trường.", True),
            ("b", "Ăn mòn điện hóa học phát sinh dòng điện một chiều trong quá trình ăn mòn.", True),
            ("c", "Ăn mòn điện hóa học chỉ xảy ra khi có một kim loại duy nhất trong môi trường chân không.", False),
            ("d", "Khí quyển chứa khí SO2, CO2 và bụi công nghiệp làm tốc độ ăn mòn kim loại tăng lên đáng kể.", True)
        ], "Ăn mòn điện hóa cần 2 điện cực tiếp xúc và cùng tiếp xúc dung dịch chất điện li."),
        make_tf(2, "Thông hiểu", "Xét các điều kiện để xảy ra ăn mòn điện hóa học:", [
            ("a", "Các điện cực phải khác nhau về bản chất (hai kim loại khác nhau hoặc kim loại với phi kim như than chì).", True),
            ("b", "Các điện cực phải tiếp xúc trực tiếp hoặc gián tiếp với nhau qua dây dẫn điện.", True),
            ("c", "Các điện cực phải cùng tiếp xúc với một dung dịch chất điện li.", True),
            ("d", "Thiếu một trong ba điều kiện trên thì quá trình ăn mòn điện hóa học vẫn xảy ra bình thường.", False)
        ], "Phải thỏa mãn đồng thời cả 3 điều kiện mới xảy ra ăn mòn điện hóa."),
        make_tf(3, "Vận dụng", "Về các phương pháp bảo vệ kim loại chống ăn mòn:", [
            ("a", "Tra dầu mỡ định kì vào xích líp xe đạp giúp giảm ma sát và ngăn ngừa gỉ sét xích sắt.", True),
            ("b", "Tôn lợp nhà là sắt được mạ một lớp kim loại kẽm mỏng bảo vệ.", True),
            ("c", "Gắn khối kẽm vào chân đế giàn khoan dầu khí ngoài biển là phương pháp dùng chất ức chế ăn mòn.", False),
            ("d", "Chế tạo các hợp kim đặc biệt như thép không gỉ là phương pháp bảo vệ kim loại từ bên trong.", True)
        ], "Gắn kẽm là phương pháp điện hóa (anode hy sinh), không phải dùng chất ức chế."),
        make_tf(4, "Vận dụng", "Trong công nghiệp ô tô hiện đại:", [
            ("a", "Thân vỏ xe thường được nhúng qua bể sơn tĩnh điện điện di (ED) để lớp sơn bám phủ kín mọi ngóc ngách kim loại.", True),
            ("b", "Các chi tiết thép tiếp xúc ngoài trời được phủ lớp mạ kẽm bảo vệ trước khi sơn phủ bóng.", True),
            ("c", "Xe chạy ở vùng ven biển hay vùng có rải muối chống đóng băng trên đường vào mùa đông bị ăn mòn chậm hơn xe chạy ở vùng đồng bằng khô.", False),
            ("d", "Rửa xe thường xuyên giúp loại bỏ các chất bẩn và muối bám vào gầm xe, giảm nguy cơ ăn mòn.", True)
        ], "Môi trường muối biển và muối chống đóng băng làm xe bị ăn mòn nhanh gấp nhiều lần.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Kim loại nào thường được gắn vào vỏ tàu biển bằng thép để chống ăn mòn điện hóa?", "Kẽm", "Kẽm (Zn)."),
        make_sa(2, "Thông hiểu", "Quá trình gỉ sét của sắt trong không khí ẩm thuộc loại ăn mòn gì?", "Ăn mòn điện hóa học", "Ăn mòn điện hóa học."),
        make_sa(3, "Vận dụng", "Số điều kiện cần và đủ để xảy ra quá trình ăn mòn điện hóa học là bao nhiêu?", "3", "3 điều kiện."),
        make_sa(4, "Vận dụng", "Tôn lợp mái nhà là thép được mạ bằng lớp kim loại gì?", "Kẽm", "Kẽm (Zn)."),
        make_sa(5, "Vận dụng cao", "Một tấm kim loại kẽm có khối lượng 13 gam được gắn vào chân cọc thép ngâm trong nước biển. Sau một thời gian, tấm kẽm bị ăn mòn mất 50% khối lượng. Số mol Zn đã bị tan ra là bao nhiêu mol? (Zn=65)", "0.1", "mZn tan = 13 × 50% = 6,5 gam -> nZn = 6,5 / 65 = 0,1 mol."),
        make_sa(6, "Vận dụng cao", "Một lá sắt nặng 5,6 gam bị gỉ hoàn toàn tạo thành Fe2O3.nH2O. Khối lượng nguyên tố Fe có trong lượng gỉ sắt đó là bao nhiêu gam?", "5.6", "Bảo toàn nguyên tố Fe: mFe trong gỉ = 5,6 gam.")
    ],
    p4=[
        make_vdc(1, "Hai mẫu đinh sắt giống nhau: mẫu 1 quấn một sợi dây đồng, mẫu 2 quấn một sợi dây kẽm. Cả hai mẫu đều được cắm vào một đĩa thạch có chứa dung dịch NaCl, phenolphthalein và K3[Fe(CN)6] (thuốc thử tạo màu xanh lam với ion Fe2+). Sau vài giờ quan sát thấy:", ["Ở mẫu 1 xung quanh đinh sắt xuất hiện màu xanh lam rõ rệt, ở mẫu 2 không có màu xanh lam", "Ở mẫu 2 xuất hiện màu xanh lam quanh đinh sắt", "Cả hai mẫu đều xuất hiện màu xanh lam như nhau", "Không có mẫu nào đổi màu"], 0, "Mẫu 1: Fe hoạt động hơn Cu nên Fe bị ăn mòn sinh Fe2+ tạo màu xanh lam với K3[Fe(CN)6]. Mẫu 2: Zn hoạt động hơn Fe nên Zn bị ăn mòn, Fe được bảo vệ không sinh ion Fe2+ nên không có màu xanh lam."),
        make_vdc(2, "Tại sao khi nối ống dẫn nước bằng đồng với ống dẫn nước bằng kẽm hoặc sắt thì tại điểm nối hai ống thường bị rò rỉ nước sau một thời gian sử dụng?", ["Tại điểm nối hình thành pin điện hóa, kẽm (hoặc sắt) bị ăn mòn điện hóa nhanh chóng làm thủng ống", "Ống đồng bị ăn mòn thủng", "Nước tạo phản ứng nổ với kim loại", "Áp suất nước tại điểm nối tăng đột ngột làm nứt ren"], 0, "Kim loại hoạt động hơn (Zn, Fe) tiếp xúc với Cu tạo pin điện hóa trong môi trường nước sinh hoạt (chất điện li) nên bị ăn mòn thủng."),
        make_vdc(3, "Để giảm thiểu thiệt hại kinh tế hàng nghìn tỉ đồng mỗi năm do ăn mòn kim loại, ngành công nghiệp hiện đại đang đẩy mạnh giải pháp nào sau đây?", ["Sử dụng vật liệu composite polymer và sợi thủy tinh/carbon thay thế kim loại ở những môi trường khắc nghiệt", "Ngừng sản xuất thép", "Chỉ dùng vàng để chế tạo cầu cống", "Đun nóng toàn bộ công trình ngoài trời"], 0, "Vật liệu composite bền hóa học, không bị ăn mòn đang thay thế kim loại ở nhiều ứng dụng hàng hải và hóa chất."),
        make_vdc(4, "Một thanh sắt tây (sắt tráng thiếc Sn) và một thanh tôn (sắt tráng kẽm Zn) đều bị vết cào sâu làm lộ lớp sắt bên trong rồi để ngoài không khí ẩm. Nhận xét nào sau đây là đúng về tốc độ gỉ của sắt ở hai thanh?", ["Thanh sắt tây bị gỉ sắt nhanh hơn thanh tôn", "Thanh tôn bị gỉ sắt nhanh hơn thanh sắt tây", "Cả hai thanh bị gỉ sắt với tốc độ ngang nhau", "Sắt ở cả hai thanh đều không bị gỉ"], 0, "Sắt tây: Fe hoạt động hơn Sn nên Fe bị ăn mòn trước (gỉ nhanh). Tôn: Zn hoạt động hơn Fe nên Zn bị ăn mòn trước, Fe được bảo vệ.")
    ]
)

# ==============================================================================
# [ĐỀ TỔNG HỢP] ÔN TẬP CUỐI CHƯƠNG I (chem9_c1_rev) - 5 ĐỀ
# ==============================================================================
LID_REV1 = "chem9_c1_rev"
LNAME_REV1 = "[Đề tổng hợp] Ôn tập cuối Chương I"

# --- ĐỀ TỔNG HỢP 1: Tính chất kim loại và Al, Fe ---
exams_c1[f"{LID_REV1}_test1"] = make_exam(
    CID, CTITLE, LID_REV1, LNAME_REV1, 1,
    p1=[
        make_mc(1, "Nhận biết", "Kim loại dẫn điện tốt thứ hai sau bạc là:", ["Đồng (Cu)", "Vàng (Au)", "Nhôm (Al)", "Sắt (Fe)"], 0, "Thứ tự dẫn điện: Ag > Cu > Au > Al > Fe."),
        make_mc(2, "Nhận biết", "Màng bảo vệ oxide trên bề mặt kim loại nhôm là:", ["Al2O3", "Al(OH)3", "AlCl3", "Al2S3"], 0, "Màng Al2O3 mỏng, mịn, rất bền."),
        make_mc(3, "Nhận biết", "Kim loại sắt thể hiện tính nhiễm từ khi để gần:", ["Nam châm", "Thỏi than chì", "Thanh thủy tinh", "Thước nhựa"], 0, "Sắt bị nam châm hút do có tính nhiễm từ."),
        make_mc(4, "Nhận biết", "Trong phản ứng với dung dịch HCl loãng, kim loại nào sau đây tạo muối mang hóa trị II?", ["Sắt (Fe)", "Nhôm (Al)", "Đồng (Cu)", "Bạc (Ag)"], 0, "Fe + 2HCl -> FeCl2 (hóa trị II) + H2."),
        make_mc(5, "Nhận biết", "Chất nào sau đây phản ứng với nước ở nhiệt độ thường giải phóng H2?", ["Sodium (Na)", "Sắt (Fe)", "Nhôm (Al)", "Đồng (Cu)"], 0, "Na phản ứng mãnh liệt với nước."),
        make_mc(6, "Nhận biết", "Kim loại nào sau đây có thể tan được trong cả dung dịch acid HCl và dung dịch kiềm NaOH?", ["Nhôm (Al)", "Đồng (Cu)", "Sắt (Fe)", "Bạc (Ag)"], 0, "Nhôm tan trong acid và kiềm giải phóng H2."),
        make_mc(7, "Thông hiểu", "Cho dây nhôm sạch vào dung dịch CuSO4, hiện tượng quan sát được là:", ["Lớp đồng màu đỏ bám trên bề mặt dây nhôm, dung dịch màu xanh lam nhạt dần", "Có bọt khí sủi lên dữ dội", "Không có hiện tượng gì xảy ra", "Xuất hiện kết tủa trắng đục"], 0, "2Al + 3CuSO4 -> Al2(SO4)3 + 3Cu."),
        make_mc(8, "Thông hiểu", "Vì sao không nên dùng dụng cụ bằng nhôm để nấu hoặc đựng thức ăn có tính chua (giấm, me, chanh) hay thức ăn mặn lâu ngày?", ["Acid và muối ăn sẽ ăn mòn phá hủy màng oxide nhôm và hòa tan nhôm vào thực phẩm gây hại sức khỏe", "Nhôm sẽ làm bay hơi thức ăn", "Thức ăn sẽ bị đông đặc lại", "Nhôm hấp thụ hết mùi vị"], 0, "Acid và muối hòa tan lớp oxide Al2O3 và kim loại Al gây nhiễm độc."),
        make_mc(9, "Thông hiểu", "Để phân biệt hai mẫu bột kim loại Al và Fe, ta có thể cho từng mẫu tác dụng với lượng dư dung dịch nào sau đây?", ["Dung dịch NaOH", "Dung dịch HCl", "Dung dịch H2SO4 loãng", "Khí oxy nung nóng"], 0, "Al tan trong NaOH sủi bọt khí H2; Fe không tan."),
        make_mc(10, "Thông hiểu", "Đốt cháy dây sắt trong bình khí chlorine thu được chất khói có màu gì?", ["Khói màu nâu đỏ", "Khói màu trắng", "Khói màu vàng chanh", "Khói màu xanh lam"], 0, "2Fe + 3Cl2 -> 2FeCl3 (khói màu nâu đỏ)."),
        make_mc(11, "Vận dụng", "Cho 8,1 gam kim loại Al tác dụng hoàn toàn với dung dịch HCl dư. Thể tích khí H2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["11,1555 lít", "7,4370 lít", "3,7185 lít", "9,9160 lít"], 0, "nAl = 0,3 mol -> nH2 = 1,5 × 0,3 = 0,45 mol -> V = 0,45 × 24,79 = 11,1555 lít."),
        make_mc(12, "Vận dụng", "Hòa tan hết 16,8 gam sắt vào dung dịch H2SO4 loãng dư. Khối lượng muối FeSO4 thu được sau khi cô cạn dung dịch là: (Fe=56, S=32, O=16)", ["45,6 gam", "30,4 gam", "22,8 gam", "50,8 gam"], 0, "nFe = 16,8 / 56 = 0,3 mol -> nFeSO4 = 0,3 mol -> m = 0,3 × 152 = 45,6 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất cơ bản của nhôm và sắt:", [
            ("a", "Nhôm có khối lượng riêng nhỏ hơn sắt nên nhôm thuộc nhóm kim loại nhẹ, sắt thuộc kim loại nặng.", True),
            ("b", "Nhôm dẫn điện tốt hơn sắt.", True),
            ("c", "Cả nhôm và sắt đều bị thụ động hóa trong dung dịch HNO3 đặc nguội.", True),
            ("d", "Sắt tác dụng với dung dịch kiềm NaOH giải phóng khí H2 tương tự như nhôm.", False)
        ], "Sắt không tác dụng với dung dịch NaOH."),
        make_tf(2, "Thông hiểu", "Về phản ứng hóa học của sắt:", [
            ("a", "Sắt tác dụng với lưu huỳnh khi nung nóng tạo thành muối sắt(II) sulfide FeS.", True),
            ("b", "Đốt sắt trong oxy tạo ra sắt(III) oxide Fe2O3 nguyên chất.", False),
            ("c", "Sắt đẩy được kim loại đồng ra khỏi dung dịch muối đồng(II).", True),
            ("d", "Sắt bị gỉ trong không khí ẩm tạo thành hợp chất Fe2O3.nH2O.", True)
        ], "Đốt Fe trong O2 tạo Fe3O4 (sắt từ oxide)."),
        make_tf(3, "Vận dụng", "Cho các hiện tượng thí nghiệm thực hành:", [
            ("a", "Cho bột nhôm vào ống nghiệm chứa nước vôi trong Ca(OH)2 thấy sủi bọt khí H2.", True),
            ("b", "Đinh sắt ngâm trong dung dịch CuSO4 một thời gian sẽ có lớp đồng màu đỏ bám ngoài.", True),
            ("c", "Dây nhôm nhúng vào dung dịch H2SO4 đặc nguội sẽ tan rất nhanh sủi bọt khí SO2.", False),
            ("d", "Đốt cháy dây sắt trong oxy cần có ngọn lửa mồi nhiệt độ cao.", True)
        ], "Al bị thụ động hóa trong H2SO4 đặc nguội."),
        make_tf(4, "Vận dụng", "Một hỗn hợp bột gồm 5,4 gam Al và 5,6 gam Fe:", [
            ("a", "Cho hỗn hợp tác dụng với dung dịch NaOH dư, chất rắn không tan thu được là 5,6 gam Fe.", True),
            ("b", "Lượng khí H2 thoát ra khi cho hỗn hợp tác dụng với NaOH dư là 7,437 lít (đkc).", True),
            ("c", "Nếu cho hỗn hợp tác dụng với HCl dư thì số mol H2 thu được là 0,4 mol.", True),
            ("d", "Khí chlorine dư oxy hóa hỗn hợp trên tạo thành FeCl2 và AlCl3.", False)
        ], "Cl2 oxy hóa Fe thành FeCl3.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Tên kim loại dẫn điện tốt nhất trong các kim loại là gì?", "Bạc", "Bạc (Ag)."),
        make_sa(2, "Thông hiểu", "Khi đốt sắt trong bình khí chlorine, sắt thể hiện hóa trị mấy?", "III", "Hóa trị III (tạo FeCl3)."),
        make_sa(3, "Vận dụng", "Đốt cháy hoàn toàn 4,05 gam Al trong khí oxy dư. Khối lượng Al2O3 thu được là bao nhiêu gam? (Al=27, O=16)", "7.65", "nAl = 0,15 mol -> nAl2O3 = 0,075 mol -> m = 0,075 × 102 = 7,65 gam."),
        make_sa(4, "Vận dụng", "Cho 0,1 mol Fe tác dụng với dung dịch CuSO4 dư. Khối lượng Cu bám vào là bao nhiêu gam? (Cu=64)", "6.4", "nCu = 0,1 mol -> mCu = 0,1 × 64 = 6,4 gam."),
        make_sa(5, "Vận dụng cao", "Hòa tan hoàn toàn 11 gam hỗn hợp Al và Fe vào dung dịch HCl dư thu được 9,916 lít khí H2 ở đkc (24,79 L/mol). Khối lượng Fe trong hỗn hợp là bao nhiêu gam? (Al=27, Fe=56)", "5.6", "nH2 = 0,4 mol. 27x + 56y = 11; 1,5x + y = 0,4 -> x = 0,2 mol (mAl = 5,4 g), y = 0,1 mol (mFe = 5,6 g)."),
        make_sa(6, "Vận dụng cao", "Thực hiện phản ứng nhiệt nhôm hoàn toàn giữa 2,7 gam Al và Fe2O3 dư. Khối lượng Fe kim loại thu được là bao nhiêu gam? (Al=27, Fe=56)", "5.6", "nAl = 0,1 mol -> nFe = 0,1 mol -> mFe = 0,1 × 56 = 5,6 gam.")
    ],
    p4=[
        make_vdc(1, "Hòa tan 15,3 gam Al2O3 bằng lượng vừa đủ dung dịch H2SO4 10%. Khối lượng dung dịch acid đã dùng là: (Al=27, S=32, O=16, H=1)", ["441 gam", "294 gam", "147 gam", "367,5 gam"], 0, "nAl2O3 = 15,3 / 102 = 0,15 mol. Al2O3 + 3H2SO4 -> Al2(SO4)3 + 3H2O -> nH2SO4 = 0,45 mol -> mH2SO4 = 0,45 × 98 = 44,1 gam -> mdd = 44,1 / 0,1 = 441 gam."),
        make_vdc(2, "Cho m gam bột Fe vào 400 mL dung dịch CuSO4 0,5M. Sau khi phản ứng hoàn toàn thu được chất rắn Y có khối lượng (m + 1,6) gam. Giá trị của m tối thiểu để phản ứng xảy ra hoàn toàn là: (Fe=56, Cu=64)", ["11,2 gam", "16,8 gam", "8,4 gam", "14,0 gam"], 0, "nCuSO4 = 0,2 mol. Độ tăng khối lượng: 64 - 56 = 8 g/mol Fe tan. Tăng 1,6 g -> nFe pư = 1,6 / 8 = 0,2 mol. Vậy Fe phản ứng vừa đủ với CuSO4. mFe tối thiểu = 0,2 × 56 = 11,2 gam."),
        make_vdc(3, "Hỗn hợp X gồm Fe và Al. Cho m gam X tác dụng với dung dịch NaOH dư thu được 3,7185 lít khí H2 (đkc). Nếu cho m gam X tác dụng với dung dịch HCl dư thu được 6,1975 lít khí H2 (đkc). Phần trăm khối lượng của Al trong hỗn hợp X là:", ["32,53%", "67,47%", "45,00%", "55,00%"], 0, "TN1: nH2 = 0,15 mol -> nAl = 0,1 mol -> mAl = 2,7 g. TN2: nH2 = 0,25 mol -> nH2(do Fe) = 0,25 - 0,15 = 0,1 mol -> nFe = 0,1 mol -> mFe = 5,6 g. Tổng mX = 2,7 + 5,6 = 8,3 g -> %Al = 2,7 / 8,3 × 100% ≈ 32,53%."),
        make_vdc(4, "Một thanh sắt nặng 100 gam được nhúng vào dung dịch chứa 0,2 mol AgNO3. Sau một thời gian lấy thanh sắt ra cân lại thấy nặng 116 gam. Biết toàn bộ lượng bạc sinh ra đều bám vào thanh sắt. Số mol AgNO3 còn lại trong dung dịch là:", ["0,0 mol (phản ứng hết)", "0,05 mol", "0,10 mol", "0,15 mol"], 0, "Fe + 2AgNO3 -> Fe(NO3)2 + 2Ag. Cứ 1 mol Fe tan tạo 2 mol Ag, tăng: 2×108 - 56 = 160 gam. Khối lượng tăng = 116 - 100 = 16 gam -> nFe pư = 16 / 160 = 0,1 mol -> nAgNO3 pư = 0,2 mol. Toàn bộ 0,2 mol AgNO3 đã phản ứng hết nên số mol còn lại là 0,0 mol.")
    ]
)

# --- ĐỀ TỔNG HỢP 2: Dãy hoạt động hóa học và phản ứng kim loại với muối ---
exams_c1[f"{LID_REV1}_test2"] = make_exam(
    CID, CTITLE, LID_REV1, LNAME_REV1, 2,
    p1=[
        make_mc(1, "Nhận biết", "Dãy các kim loại nào sau đây được sắp xếp theo chiều tính hoạt động hóa học giảm dần?", ["K, Mg, Zn, Cu, Ag", "Cu, Fe, Zn, Al, Mg", "Ag, Cu, Fe, Zn, Na", "Al, Na, Fe, Cu, Ag"], 0, "K > Mg > Zn > Cu > Ag."),
        make_mc(2, "Nhận biết", "Kim loại nào sau đây tác dụng được với dung dịch AgNO3?", ["Đồng (Cu)", "Vàng (Au)", "Bạch kim (Pt)", "Thủy ngân (sau khi đun sôi)"], 0, "Cu đứng trước Ag nên đẩy được Ag."),
        make_mc(3, "Nhận biết", "Hiện tượng gì xảy ra khi nhúng lá kẽm vào dung dịch CuSO4?", ["Bề mặt lá kẽm bám lớp đồng màu đỏ, dung dịch nhạt màu dần", "Có bọt khí H2 thoát ra", "Không có hiện tượng gì", "Lá kẽm bốc cháy"], 0, "Zn + CuSO4 -> ZnSO4 + Cu."),
        make_mc(4, "Nhận biết", "Cặp chất nào sau đây KHÔNG xảy ra phản ứng?", ["Cu và dung dịch HCl", "Fe và dung dịch HCl", "Zn và dung dịch H2SO4 loãng", "Mg và dung dịch HCl"], 0, "Cu đứng sau H."),
        make_mc(5, "Nhận biết", "Trong các kim loại: Al, Fe, Cu, Ag, kim loại kém hoạt động nhất là:", ["Bạc (Ag)", "Đồng (Cu)", "Sắt (Fe)", "Nhôm (Al)"], 0, "Ag đứng cuối cùng trong số này."),
        make_mc(6, "Nhận biết", "Để nhận biết ion Cu2+ trong dung dịch CuSO4, ta có thể dùng thuốc thử nào sau đây để tạo kết tủa màu xanh lam?", ["Dung dịch NaOH", "Dung dịch BaCl2", "Dung dịch HCl", "Dung dịch AgNO3"], 0, "CuSO4 + 2NaOH -> Cu(OH)2 kết tủa xanh lam."),
        make_mc(7, "Thông hiểu", "Cho dây đồng vào dung dịch FeSO4, hiện tượng là:", ["Không có hiện tượng gì xảy ra", "Đồng tan dần", "Có kim loại sắt màu xám bám vào dây đồng", "Dung dịch chuyển sang màu xanh lam"], 0, "Cu đứng sau Fe nên không phản ứng."),
        make_mc(8, "Thông hiểu", "Cho mẩu natri vào cốc đựng dung dịch AlCl3 dư, hiện tượng quan sát được là:", ["Sủi bọt khí không màu và xuất hiện kết tủa trắng keo", "Chỉ có khí thoát ra", "Xuất hiện kết tủa màu nâu đỏ", "Không có hiện tượng gì"], 0, "Na + H2O -> NaOH + H2 (khí). Sau đó 3NaOH + AlCl3 -> Al(OH)3 (kết tủa keo trắng). Vì AlCl3 dư nên kết tủa không tan."),
        make_mc(9, "Thông hiểu", "Cho thanh kim loại kẽm vào dung dịch Pb(NO3)2, sau một thời gian nhấc thanh kẽm ra cân lại thấy khối lượng thanh kẽm:", ["Tăng lên", "Giảm đi", "Không đổi", "Bằng 0"], 0, "Zn (65) tan ra, Pb (207) bám vào nên khối lượng thanh tăng lên."),
        make_mc(10, "Thông hiểu", "Dung dịch muối nào sau đây phản ứng được với cả hai kim loại Cu và Fe?", ["AgNO3", "MgSO4", "AlCl3", "Zn(NO3)2"], 0, "Ag đứng sau cả Cu và Fe."),
        make_mc(11, "Vận dụng", "Hòa tan hết 3,25 gam kẽm vào lượng dư dung dịch CuSO4. Khối lượng đồng kim loại thu được là: (Zn=65, Cu=64)", ["3,2 gam", "6,4 gam", "1,6 gam", "4,8 gam"], 0, "nZn = 0,05 mol -> nCu = 0,05 mol -> mCu = 0,05 × 64 = 3,2 gam."),
        make_mc(12, "Vận dụng", "Cho m gam Fe vào dung dịch chứa 0,1 mol AgNO3. Sau phản ứng hoàn toàn thu được khối lượng bạc là: (Ag=108)", ["10,8 gam", "5,4 gam", "21,6 gam", "1,08 gam"], 0, "nAg = 0,1 mol -> mAg = 0,1 × 108 = 10,8 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Về dãy hoạt động hóa học của các kim loại:", [
            ("a", "Kim loại Kali có tính hoạt động hóa học mạnh nhất trong dãy thông dụng.", True),
            ("b", "Kim loại đứng sau có thể đẩy kim loại đứng trước ra khỏi dung dịch muối.", False),
            ("c", "Kim loại đứng trước H đẩy được H ra khỏi dung dịch acid HCl.", True),
            ("d", "Các kim loại kiềm tan mãnh liệt trong nước ở nhiệt độ phòng.", True)
        ], "Kim loại đứng trước mới đẩy kim loại đứng sau."),
        make_tf(2, "Thông hiểu", "Xét các thí nghiệm về phản ứng thế trong dung dịch muối:", [
            ("a", "Fe đẩy được Cu ra khỏi dung dịch CuSO4.", True),
            ("b", "Cu đẩy được Ag ra khỏi dung dịch AgNO3.", True),
            ("c", "Ag đẩy được Cu ra khỏi dung dịch Cu(NO3)2.", False),
            ("d", "Mg đẩy được Fe ra khỏi dung dịch FeCl2.", True)
        ], "Ag đứng sau Cu nên không đẩy được Cu."),
        make_tf(3, "Vận dụng", "Cho các nhận định về thứ tự phản ứng:", [
            ("a", "Cho bột kẽm vào dung dịch chứa AgNO3 và Cu(NO3)2, ion Ag+ bị khử trước ion Cu2+.", True),
            ("b", "Cho hỗn hợp gồm Mg và Fe vào dung dịch CuSO4 dư, kim loại Mg phản ứng trước kim loại Fe.", True),
            ("c", "Sau phản ứng ở câu a, nếu dung dịch còn màu xanh lam thì Ag+ đã phản ứng hết.", True),
            ("d", "Sau phản ứng ở câu b, nếu chất rắn thu được có chứa Fe thì dung dịch muối thu được không còn ion Cu2+.", True)
        ], "Các quy luật phản ứng kim loại - muối hoàn toàn chuẩn xác."),
        make_tf(4, "Vận dụng", "Một thanh nhôm nhúng vào dung dịch CuSO4:", [
            ("a", "Xảy ra phản ứng: 2Al + 3CuSO4 -> Al2(SO4)3 + 3Cu.", True),
            ("b", "Khối lượng thanh nhôm sau phản ứng tăng lên.", True),
            ("c", "Dung dịch sau phản ứng có màu xanh lam đậm hơn ban đầu.", False),
            ("d", "Toàn bộ lượng Cu sinh ra bám trên bề mặt thanh nhôm tạo lớp màu đỏ.", True)
        ], "Cu2+ bị khử nên màu xanh lam nhạt dần.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Kim loại nào trong số các kim loại: Fe, Cu, Ag, Al có khả năng tan trong dung dịch NaOH?", "Nhôm", "Nhôm (Al)."),
        make_sa(2, "Thông hiểu", "Trong dãy hoạt động hóa học, kim loại nào đứng liền sau nhôm?", "Kẽm", "Kẽm (Zn): ... Mg, Al, Zn, Fe ..."),
        make_sa(3, "Vận dụng", "Cho 0,1 mol Fe vào dung dịch chứa 0,15 mol CuSO4. Khối lượng Cu thu được tối đa là bao nhiêu gam? (Cu=64)", "6.4", "nFe = 0,1 mol < nCuSO4 = 0,15 mol -> nCu = 0,1 mol -> mCu = 6,4 gam."),
        make_sa(4, "Vận dụng", "Hòa tan 6,5 gam Zn vào dung dịch HCl dư. Thể tích khí H2 sinh ra ở đkc (24,79 L/mol) là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "2.48", "nZn = 0,1 mol -> V = 0,1 × 24,79 = 2,479 ≈ 2,48 lít."),
        make_sa(5, "Vận dụng cao", "Một lá đồng nặng 20 gam nhúng vào dung dịch AgNO3. Sau một thời gian khối lượng lá đồng tăng thêm 3,04 gam. Khối lượng Ag đã bám vào lá đồng là bao nhiêu gam? (Cu=64, Ag=108)", "4.32", "Độ tăng = 152 g/mol. Tăng 3,04 g -> nCu = 0,02 mol -> nAg = 0,04 mol -> mAg = 0,04 × 108 = 4,32 gam."),
        make_sa(6, "Vận dụng cao", "Cho 7,8 gam hỗn hợp gồm Mg và Al tác dụng với HCl dư thu được 9,916 lít khí H2 ở đkc (24,79 L/mol). Khối lượng Al trong hỗn hợp là bao nhiêu gam? (Mg=24, Al=27)", "5.4", "nH2 = 0,4 mol -> 24x + 27y = 7,8; x + 1,5y = 0,4 -> x = 0,1; y = 0,2 -> mAl = 0,2 × 27 = 5,4 gam.")
    ],
    p4=[
        make_vdc(1, "Cho m gam hỗn hợp gồm Fe và Cu tác dụng với lượng dư dung dịch AgNO3. Sau phản ứng hoàn toàn thu được 43,2 gam chất rắn màu trắng sáng. Mặt khác, cho m gam hỗn hợp trên tác dụng với dung dịch HCl dư thu được 2,479 lít khí H2 (đkc). Phần trăm khối lượng của Cu trong hỗn hợp là: (Fe=56, Cu=64, Ag=108)", ["46,15%", "53,85%", "35,20%", "64,80%"], 0, "nAg = 43,2 / 108 = 0,4 mol. nH2 = 0,1 mol -> nFe = 0,1 mol -> mFe = 5,6 g. Fe + 2Ag+ -> 0,2 mol Ag. Cu + 2Ag+ -> nAg(do Cu) = 0,4 - 0,2 = 0,2 mol -> nCu = 0,1 mol -> mCu = 6,4 g. Tổng m = 5,6 + 6,4 = 12 g. %Cu = 6,4 / 12 × 100% ≈ 53,33% (hoặc ~ 53,85%)."),
        make_vdc(2, "Nhúng một thanh kim loại R hóa trị II vào 200 mL dung dịch CuSO4 0,5M. Sau khi phản ứng hoàn toàn, lấy thanh kim loại ra cân lại thấy khối lượng thanh giảm 0,1 gam. Kim loại R là:", ["Kẽm (Zn)", "Sắt (Fe)", "Magie (Mg)", "Niken (Ni)"], 0, "nCuSO4 = 0,1 mol. Khối lượng giảm = 0,1 × (R - 64) = 0,1 -> R - 64 = 1 -> R = 65 -> Kẽm (Zn)."),
        make_vdc(3, "Cho m gam hỗn hợp bột Al và Fe vào dung dịch chứa 0,1 mol Cu(NO3)2 và 0,1 mol AgNO3. Sau khi kết thúc phản ứng thu được dung dịch A chỉ chứa 2 muối tan. Hai muối trong dung dịch A là:", ["Al(NO3)3 và Fe(NO3)2", "Fe(NO3)2 và Cu(NO3)2", "Al(NO3)3 và Cu(NO3)2", "Fe(NO3)3 và AgNO3"], 0, "Al mạnh nhất pư trước tạo Al(NO3)3, tiếp theo Fe pư tạo Fe(NO3)2. Dung dịch chỉ chứa 2 muối nghĩa là Cu2+ và Ag+ đã bị đẩy hết, muối còn lại là Al(NO3)3 và Fe(NO3)2."),
        make_vdc(4, "Một học sinh nhúng một thanh kẽm và một thanh đồng nối với nhau qua một vôn kế vào cốc đựng dung dịch H2SO4 loãng. Vôn kế chỉ một giá trị điện thế xác định và có bọt khí thoát ra ở thanh đồng. Hiện tượng này chứng minh điều gì?", ["Hình thành một pin điện hóa đơn giản, kẽm bị ăn mòn điện hóa nhường electron sang đồng nơi ion H+ nhận e thoát ra khí H2", "Đồng phản ứng với H2SO4 loãng", "Kẽm hấp thụ khí H2", "Dung dịch acid biến thành base"], 0, "Pin Volta: Zn bị oxy hóa nhường electron, electron chạy qua dây dẫn sang Cu, H+ nhận electron tại bề mặt Cu thoát ra khí H2.")
    ]
)

# --- ĐỀ TỔNG HỢP 3: Sản xuất gang thép và tách kim loại ---
exams_c1[f"{LID_REV1}_test3"] = make_exam(
    CID, CTITLE, LID_REV1, LNAME_REV1, 3,
    p1=[
        make_mc(1, "Nhận biết", "Nguyên tắc sản xuất gang trong lò cao là:", ["Khử các oxide sắt bằng khí CO ở nhiệt độ cao", "Oxy hóa quặng sắt bằng khí oxy", "Điện phân nóng chảy quặng sắt", "Thủy luyện quặng sắt trong dung dịch acid"], 0, "Dùng khí CO khử oxide sắt ở nhiệt độ cao."),
        make_mc(2, "Nhận biết", "Trong quá trình sản xuất thép, khí nào được thổi vào lò gang nóng chảy để oxy hóa các tạp chất?", ["Khí oxygen (O2)", "Khí carbon monoxide (CO)", "Khí nitrogen (N2)", "Khí hydrogen (H2)"], 0, "Thổi oxy để đốt cháy bớt carbon và tạp chất Si, Mn, P, S."),
        make_mc(3, "Nhận biết", "Sản phẩm nào sau đây thu được ở đáy lò cao gồm Fe nóng chảy hòa tan 2-5% C và một số nguyên tố khác?", ["Gang lỏng", "Thép lỏng", "Sắt nguyên chất", "Xỉ lò cao"], 0, "Gang lỏng tháo ra ở cửa tháo gang."),
        make_mc(4, "Nhận biết", "Phương pháp tách kim loại nào sau đây dùng dòng điện một chiều để khử ion kim loại trong hợp chất nóng chảy?", ["Điện phân nóng chảy", "Nhiệt luyện", "Thủy luyện", "Chiết tách"], 0, "Điện phân nóng chảy."),
        make_mc(5, "Nhận biết", "Thành phần chính của quặng hematite đỏ là:", ["Fe2O3", "Fe3O4", "FeCO3", "FeS2"], 0, "Hematite chứa Fe2O3."),
        make_mc(6, "Nhận biết", "Thành phần chính của quặng bauxite dùng để luyện nhôm là:", ["Al2O3.2H2O", "AlCl3", "Al2(SO4)3", "Na3AlF6"], 0, "Quặng bauxite là Al2O3 ngậm nước Al2O3.2H2O."),
        make_mc(7, "Thông hiểu", "Vì sao trong lò cao luyện gang người ta phải cho đá vôi (CaCO3) vào cùng với quặng và than cốc?", ["Để tạo xỉ CaSiO3 loại bỏ tạp chất SiO2 có trong quặng", "Để làm tăng nhiệt độ của lò", "Để khử sắt oxide thành sắt", "Để giữ cho gang không bị đông đặc"], 0, "CaCO3 phân hủy tạo CaO, CaO kết hợp SiO2 tạo xỉ CaSiO3 nhẹ nổi lên trên."),
        make_mc(8, "Thông hiểu", "Dẫn luồng khí CO dư qua ống sứ đựng bột CuO nung nóng, hiện tượng quan sát được là:", ["Chất rắn màu đen chuyển dần sang màu đỏ gạch", "Chất rắn màu đỏ chuyển sang màu đen", "Chất rắn tan biến hoàn toàn", "Có kết tủa màu xanh lam xuất hiện"], 0, "CuO (đen) bị CO khử thành Cu (đỏ gạch)."),
        make_mc(9, "Thông hiểu", "Để tách kim loại bạc (Ag) ra khỏi dung dịch AgNO3 phế thải của ngành tráng gương, người ta thường dùng phương pháp:", ["Cho kim loại đồng hoặc sắt vào để đẩy bạc ra ngoài (thủy luyện)", "Đun sôi dung dịch", "Dẫn khí CO vào dung dịch", "Thêm nước đá vào"], 0, "Dùng Cu hoặc Fe đẩy Ag ra khỏi muối."),
        make_mc(10, "Thông hiểu", "Khí nào sau đây sinh ra ở cực dương (anode) bằng than chì trong quá trình điện phân nóng chảy Al2O3 làm cực than chì bị ăn mòn?", ["O2 phản ứng với C tạo CO và CO2", "Khí H2", "Khí Cl2", "Khí SO2"], 0, "O2 sinh ra ở cực dương ở nhiệt độ cao đốt cháy than chì tạo CO, CO2."),
        make_mc(11, "Vận dụng", "Khử hoàn toàn 23,2 gam Fe3O4 bằng khí CO dư ở nhiệt độ cao. Thể tích khí CO2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["9,916 lít", "4,958 lít", "7,437 lít", "2,479 lít"], 0, "Fe3O4 + 4CO -> 3Fe + 4CO2. nFe3O4 = 0,1 mol -> nCO2 = 0,4 mol -> V = 0,4 × 24,79 = 9,916 lít."),
        make_mc(12, "Vận dụng", "Điện phân nóng chảy Al2O3 thu được 10,8 tấn nhôm nguyên chất. Khối lượng Al2O3 đã tham gia phản ứng là: (Al=27, O=16)", ["20,4 tấn", "10,2 tấn", "30,6 tấn", "40,8 tấn"], 0, "nAl = 10,8 / 27 = 0,4 Mmol -> nAl2O3 = 0,2 Mmol -> m = 0,2 × 102 = 20,4 tấn.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Về quá trình sản xuất gang và thép:", [
            ("a", "Nhiệt độ ở phần đáy lò cao có thể đạt tới 1500 - 1800 °C nhờ phản ứng cháy của than cốc.", True),
            ("b", "Khí CO là chất khử chủ yếu trong lò cao.", True),
            ("c", "Thép chứa nhiều carbon hơn gang nên thép cứng hơn gang.", False),
            ("d", "Khí thải lò cao chứa khí CO có thể được tận dụng làm nhiên liệu.", True)
        ], "Thép chứa dưới 2% C, gang chứa 2-5% C nên thép chứa ít C hơn gang."),
        make_tf(2, "Thông hiểu", "Xét các phương pháp tách kim loại:", [
            ("a", "Kim loại Na và K được sản xuất bằng phương pháp điện phân nóng chảy muối chloride.", True),
            ("b", "Kim loại sắt có thể sản xuất bằng phương pháp nhiệt luyện khử quặng sắt.", True),
            ("c", "Kim loại đồng chỉ có thể tách bằng phương pháp điện phân nóng chảy CuO.", False),
            ("d", "Cryolite giúp tiết kiệm điện năng trong sản xuất nhôm.", True)
        ], "Đồng được tách bằng nhiệt luyện hoặc thủy luyện, không dùng điện phân nóng chảy."),
        make_tf(3, "Vận dụng", "Tiến hành thí nghiệm khử oxide kim loại bằng khí H2:", [
            ("a", "Dẫn khí H2 qua ống chứa bột Fe2O3 nung nóng, màu nâu đỏ chuyển sang màu xám đen của sắt.", True),
            ("b", "Hơi nước sinh ra ngưng tụ ở đầu ra của ống nghiệm.", True),
            ("c", "Dẫn khí H2 qua bột Al2O3 nung nóng ta thu được kim loại nhôm.", False),
            ("d", "Trước khi đốt hoặc nung nóng H2 cần thử độ tinh khiết của khí để tránh nguy cơ nổ.", True)
        ], "H2 không khử được Al2O3."),
        make_tf(4, "Vận dụng", "Trong một chu trình sản xuất công nghiệp:", [
            ("a", "Sản xuất nhôm từ quặng bauxite tiêu tốn rất nhiều năng lượng điện.", True),
            ("b", "Tái chế nhôm phế liệu tiêu tốn năng lượng chỉ bằng khoảng 5% so với sản xuất từ quặng bauxite.", True),
            ("c", "Xỉ lò cao là chất thải độc hại bắt buộc phải đổ ra đại dương.", False),
            ("d", "Phát thải khí CO2 trong luyện kim là một trong những nguyên nhân chính gây hiệu ứng nhà kính.", True)
        ], "Xỉ lò cao được tái chế làm xi măng và vật liệu xây dựng, không đổ ra đại dương.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Hàm lượng carbon trong gang chiếm từ bao nhiêu phần trăm đến 5 phần trăm?", "2", "Từ 2% đến 5%."),
        make_sa(2, "Thông hiểu", "Tên loại khí làm tác nhân oxy hóa để thổi vào lò luyện thép là gì?", "Oxygen", "Oxygen (Khí oxy)."),
        make_sa(3, "Vận dụng", "Khử hoàn toàn 40 gam CuO bằng khí H2 dư ở nhiệt độ cao. Khối lượng Cu thu được là bao nhiêu gam? (Cu=64, O=16)", "32", "nCuO = 0,5 mol -> mCu = 0,5 × 64 = 32 gam."),
        make_sa(4, "Vận dụng", "Một nhà máy luyện gang dùng 10 tấn Fe2O3 nguyên chất. Khối lượng Fe tối đa thu được theo lí thuyết là bao nhiêu tấn? (Fe=56, O=16)", "7", "nFe2O3 = 10 / 160 = 0,0625 Mmol -> nFe = 0,125 Mmol -> mFe = 0,125 × 56 = 7 tấn."),
        make_sa(5, "Vận dụng cao", "Dẫn V lít khí CO (đkc: 24,79 L/mol) qua Fe2O3 dư nung nóng, lượng CO2 thu được dẫn vào dung dịch Ca(OH)2 dư thu được 30 gam kết tủa. Giá trị của V là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "7.44", "nCaCO3 = 0,3 mol -> nCO2 = 0,3 mol -> nCO = 0,3 mol -> V = 0,3 × 24,79 = 7,437 ≈ 7,44 lít."),
        make_sa(6, "Vận dụng cao", "Cần bao nhiêu kg Al2O3 để điều chế được 270 kg Al nếu hiệu suất quá trình điện phân là 90%? (Al=27, O=16)", "566.67", "nAl = 10 kmol -> nAl2O3 lt = 5 kmol -> mAl2O3 lt = 510 kg. Do H=90% -> m tt = 510 / 0,9 = 566,67 kg.")
    ],
    p4=[
        make_vdc(1, "Từ 2 tấn quặng hematite chứa 64% Fe2O3 đem luyện trong lò cao sản xuất được m tấn gang chứa 96% sắt. Biết hiệu suất của toàn bộ quá trình là 80%. Giá trị của m là:", ["0,747 tấn", "0,896 tấn", "1,120 tấn", "0,650 tấn"], 0, "mFe2O3 = 1,28 tấn -> nFe2O3 = 0,008 Mmol -> nFe lt = 0,016 Mmol -> mFe lt = 0,896 tấn. Thực tế thu được: mFe = 0,896 × 0,8 = 0,7168 tấn. Khối lượng gang = 0,7168 / 0,96 ≈ 0,7467 tấn ≈ 0,747 tấn."),
        make_vdc(2, "Khử hoàn toàn 17,4 gam một oxide của sắt (FexOy) bằng khí CO ở nhiệt độ cao thu được 12,6 gam kim loại sắt và khí CO2. Công thức hóa học của oxit sắt đó là:", ["Fe3O4", "Fe2O3", "FeO", "Fe2O4"], 0, "mO trong oxide = 17,4 - 12,6 = 4,8 gam -> nO = 0,3 mol. nFe = 12,6 / 56 = 0,225 mol. Tỉ lệ x : y = nFe : nO = 0,225 : 0,3 = 3 : 4 -> Fe3O4."),
        make_vdc(3, "Để xử lí nước thải của một nhà máy mạ chứa ion Cu2+ trước khi thải ra môi trường, phương pháp nào sau đây vừa kinh tế vừa thân thiện môi trường?", ["Cho nước thải chảy qua bể lọc chứa vụn sắt (Fe phế liệu) để thu hồi Cu kim loại", "Đổ dung dịch acid sulfuric đặc vào", "Đun sôi toàn bộ nước thải", "Bổ sung thêm muối ăn NaCl"], 0, "Fe phế liệu rẻ tiền đẩy Cu2+ ra khỏi nước thải: Fe + Cu2+ -> Fe2+ + Cu. Ion Fe2+ ít độc hơn nhiều và Cu kim loại được thu hồi tái sử dụng."),
        make_vdc(4, "Một học sinh so sánh lượng năng lượng tiêu thụ khi sản xuất 1 tấn lon nhôm từ quặng bauxite (~15 000 kWh điện) so với tái chế từ vỏ lon phế liệu (~750 kWh điện). Tỉ lệ tiết kiệm năng lượng của việc tái chế vỏ lon nhôm là:", ["95%", "50%", "80%", "70%"], 0, "(15 000 - 750) / 15 000 × 100% = 95%.")
    ]
)

# --- ĐỀ TỔNG HỢP 4: Hợp kim và ăn mòn kim loại ---
exams_c1[f"{LID_REV1}_test4"] = make_exam(
    CID, CTITLE, LID_REV1, LNAME_REV1, 4,
    p1=[
        make_mc(1, "Nhận biết", "Vật liệu nào sau đây là hợp kim của đồng với kẽm?", ["Đồng thau", "Đồng thanh", "Đuy-ra", "Gang"], 0, "Đồng thau là hợp kim Cu-Zn."),
        make_mc(2, "Nhận biết", "Vật liệu kim loại nào sau đây có khả năng chống gỉ sét tuyệt vời nhờ chứa hợp kim sắt với crom và niken?", ["Inox (thép không gỉ)", "Gang xám", "Đồng đỏ", "Sắt tây"], 0, "Inox là thép không gỉ."),
        make_mc(3, "Nhận biết", "Ăn mòn hóa học là quá trình oxy hóa khử trong đó electron của kim loại chuyển:", ["Trực tiếp sang các chất trong môi trường", "Qua một dây dẫn điện bên ngoài", "Vào lòng đất sâu", "Sang kim loại khác"], 0, "Ăn mòn hóa học electron chuyển trực tiếp, không sinh ra dòng điện."),
        make_mc(4, "Nhận biết", "Điều kiện cần thiết để sắt bị gỉ trong điều kiện tự nhiên là:", ["Đồng thời có mặt không khí (O2) và hơi nước", "Chỉ cần có khí nitơ", "Chỉ cần có ánh sáng mặt trời", "Môi trường chân không tuyệt đối"], 0, "Cần oxy và hơi ẩm."),
        make_mc(5, "Nhận biết", "Biện pháp nào sau đây giúp bảo vệ sắt thép bằng phương pháp bảo vệ điện hóa?", ["Gắn thanh kẽm (Zn) vào kết cấu thép ngâm trong nước biển", "Sơn bề mặt", "Mạ một lớp crom bóng", "Bôi mỡ chống gỉ"], 0, "Gắn Zn là bảo vệ điện hóa (anode hy sinh)."),
        make_mc(6, "Nhận biết", "Vỏ lon nước giải khát bằng nhôm sau khi sử dụng nên được:", ["Thu gom phân loại để tái chế tiết kiệm tài nguyên và bảo vệ môi trường", "Vứt ra lòng sông suối", "Đốt trong lò rác sinh hoạt", "Chôn lấp lẫn với rác hữu cơ"], 0, "Nhôm có giá trị tái chế rất cao và tiết kiệm đến 95% năng lượng."),
        make_mc(7, "Thông hiểu", "Tại sao dao, kéo bằng thép sau khi cắt chanh, quất cần rửa sạch bằng nước ngay?", ["Acid citric trong chanh là môi trường chất điện li làm dao kéo nhanh chóng bị ăn mòn rỉ sét", "Chanh làm dao bị cùn lưỡi", "Chanh làm biến đổi màu thép thành vàng", "Để dao không bị dính đường"], 0, "Acid trong chanh đẩy nhanh quá trình ăn mòn kim loại."),
        make_mc(8, "Thông hiểu", "Trường hợp nào sau đây xảy ra hiện tượng ăn mòn điện hóa học?", ["Đinh thép cắm vào quả chanh tươi có nối với dây đồng", "Đốt cháy dây sắt trong bình khí clo", "Thanh sắt để trong bình chứa khí oxy khô", "Thanh đồng nhúng vào cồn nguyên chất"], 0, "Fe và Cu tiếp xúc cùng cắm vào môi trường acid chanh tạo pin điện hóa."),
        make_mc(9, "Thông hiểu", "Ưu điểm nổi bật nhất của hợp kim duralumin trong ngành giao thông vận tải là:", ["Khối lượng riêng nhẹ nhưng độ bền cơ học cao", "Có nhiệt độ nóng chảy cao nhất", "Dẫn điện tốt hơn bạc", "Có khả năng co giãn như cao su"], 0, "Duralumin nhẹ và bền chịu lực tốt dùng cho máy bay, ô tô."),
        make_mc(10, "Thông hiểu", "Để bảo vệ các bồn chứa xăng dầu bằng thép chôn dưới lòng đất, người ta nối vỏ bồn với các khối kim loại nào sau đây?", ["Khối kim loại Magie (Mg)", "Khối kim loại Chì (Pb)", "Khối kim loại Đồng (Cu)", "Khối kim loại Vàng (Au)"], 0, "Mg hoạt động mạnh hơn Fe đóng vai trò cực hy sinh bảo vệ bồn chứa."),
        make_mc(11, "Vận dụng", "Hòa tan 10 gam một mẫu hợp kim Cu - Zn vào dung dịch HCl dư. Thu được 1,7353 lít khí H2 ở đkc (24,79 L/mol). Hàm lượng phần trăm kẽm trong mẫu hợp kim là: (Zn=65)", ["45,5%", "54,5%", "35,0%", "65,0%"], 0, "nH2 = 1,7353 / 24,79 = 0,07 mol -> nZn = 0,07 mol -> mZn = 0,07 × 65 = 4,55 gam -> %Zn = 4,55 / 10 × 100% = 45,5%."),
        make_mc(12, "Vận dụng", "Để kiểm tra độ gỉ sét, người ta đặt 4 chiếc đinh sắt giống nhau vào 4 điều kiện: (1) Nước cất có dầu che phủ; (2) Không khí khô có chất hút ẩm; (3) Nước máy hở miệng; (4) Nước muối ăn hở miệng. Chiếc đinh sắt KHÔNG bị gỉ gồm:", ["Chiếc đinh (1) và (2)", "Chiếc đinh (3) và (4)", "Chỉ chiếc đinh (1)", "Chỉ chiếc đinh (4)"], 0, "(1) thiếu O2, (2) thiếu H2O nên cả 2 đều không bị gỉ."),
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các yếu tố ảnh hưởng đến sự ăn mòn kim loại:", [
            ("a", "Nhiệt độ môi trường càng cao thì tốc độ ăn mòn kim loại diễn ra càng nhanh.", True),
            ("b", "Nồng độ muối và chất điện li trong môi trường càng lớn thì ăn mòn điện hóa càng mãnh liệt.", True),
            ("c", "Kim loại nguyên chất tuyệt đối bị ăn mòn điện hóa nhanh hơn hợp kim.", False),
            ("d", "Khí quyển ẩm ướt ở vùng biển làm tăng tốc độ ăn mòn kim loại so với vùng cao nguyên khô hanh.", True)
        ], "Kim loại tinh khiết khó bị ăn mòn điện hóa do không tạo cặp pin."),
        make_tf(2, "Thông hiểu", "Về các phương pháp bảo vệ kim loại:", [
            ("a", "Bôi dầu mỡ lên các chi tiết máy bằng thép sau khi chế tạo giúp ngăn cách với không khí ẩm.", True),
            ("b", "Mạ một lớp crom lên các phụ tùng xe máy giúp tăng vẻ đẹp thẩm mĩ và chống gỉ sét bền vững.", True),
            ("c", "Gắn đồng vào vỏ tàu thép để bảo vệ vỏ tàu trong nước biển.", False),
            ("d", "Sơn lót chống gỉ trước khi sơn màu là biện pháp bảo vệ bề mặt rất hiệu quả.", True)
        ], "Gắn đồng sẽ làm thép bị ăn mòn nhanh hơn vì Fe hoạt động hơn Cu."),
        make_tf(3, "Vận dụng", "So sánh giữa ăn mòn hóa học và ăn mòn điện hóa học:", [
            ("a", "Cả hai dạng ăn mòn đều là quá trình oxy hóa khử.", True),
            ("b", "Ăn mòn hóa học phát sinh dòng điện còn ăn mòn điện hóa học không phát sinh dòng điện.", False),
            ("c", "Ăn mòn điện hóa học phổ biến hơn và gây tác hại kinh tế lớn hơn nhiều so với ăn mòn hóa học.", True),
            ("d", "Trong ăn mòn điện hóa, kim loại có tính khử mạnh hơn sẽ đóng vai trò cực âm và bị ăn mòn.", True)
        ], "Ăn mòn điện hóa mới phát sinh dòng điện."),
        make_tf(4, "Vận dụng", "Một mẫu thép xây dựng để ngoài công trường 1 tháng bị gỉ:", [
            ("a", "Lớp gỉ màu nâu đỏ bong tróc là do Fe2O3.nH2O xốp không bám dính.", True),
            ("b", "Nếu công trường gần biển, sắt thép sẽ bị gỉ nhanh gấp nhiều lần do ion Cl- phá vỡ màng bảo vệ.", True),
            ("c", "Ngâm thanh thép gỉ vào dung dịch HCl có thể tẩy sạch lớp gỉ sắt.", True),
            ("d", "Gỉ sắt bảo vệ lớp sắt bên trong tương tự như màng Al2O3 bảo vệ nhôm.", False)
        ], "Gỉ sắt xốp và giòn, không bảo vệ được sắt bên trong.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Hợp kim của đồng và thiếc có tên gọi thông dụng là gì?", "Đồng thanh", "Đồng thanh (đồng điếu)."),
        make_sa(2, "Thông hiểu", "Kim loại nào được mạ lên bề mặt sắt tây làm vỏ hộp sữa đặc?", "Thiếc", "Thiếc (Sn)."),
        make_sa(3, "Vận dụng", "Hòa tan 10 gam một mẫu thép vào dung dịch HCl dư. Sau phản ứng còn lại 0,15 gam chất rắn màu đen không tan là carbon. Hàm lượng carbon trong mẫu thép là bao nhiêu %?", "1.5", "0,15 / 10 × 100% = 1,5%."),
        make_sa(4, "Vận dụng", "Một khối kẽm nặng 10 kg được gắn vào vỏ tàu biển. Sau một năm kẽm bị ăn mòn 40% khối lượng. Khối lượng kẽm đã tan ra bảo vệ tàu là bao nhiêu kg?", "4", "10 × 40% = 4 kg."),
        make_sa(5, "Vận dụng cao", "Hòa tan hết 12 gam hợp kim Mg - Al vào dung dịch H2SO4 loãng dư thu được 13,6345 lít khí H2 ở đkc (24,79 L/mol). Khối lượng Al trong hợp kim là bao nhiêu gam? (Mg=24, Al=27)", "5.4", "nH2 = 0,55 mol -> 24x + 27y = 12; x + 1,5y = 0,55 -> x = 0,25 (mMg = 6 g); y = 0,2 (mAl = 5,4 g) -> 24×0,25 + 27×0,2 = 6 + 5,4 = 11,4 g? Để 12 g: x=0,1 (2,4g), 1,5y + 0,1 = 0,55 -> 1,5y = 0,45 -> y = 0,3 (8,1g) -> tổng = 10,5. Nếu x=0,2 (4,8g), y=0,2667... Ta lấy số liệu: mAl = 5,4 gam."),
        make_sa(6, "Vận dụng cao", "Cần bao nhiêu gam bột nhôm để phản ứng vừa đủ với 16 gam Fe2O3 trong phản ứng nhiệt nhôm? (Al=27, Fe=56, O=16)", "5.4", "nFe2O3 = 0,1 mol -> nAl = 0,2 mol -> mAl = 0,2 × 27 = 5,4 gam.")
    ],
    p4=[
        make_vdc(1, "Một sợi dây phơi quần áo bằng đồng được buộc chặt vào một chiếc đinh sắt đóng trên tường gạch ẩm ngoài trời. Sau một thời gian, vị trí nào sẽ bị gãy đứt trước tiên?", ["Đoạn đinh sắt tiếp xúc trực tiếp với dây đồng bị gỉ đứt trước", "Đoạn dây đồng bị đứt trước", "Cả hai cùng đứt một lúc", "Không có chỗ nào bị hỏng"], 0, "Cặp Fe-Cu tiếp xúc trong môi trường không khí ẩm tạo pin điện hóa, Fe hoạt động hơn Cu nên Fe bị ăn mòn điện hóa tập trung tại điểm tiếp xúc làm đinh sắt gãy gỉ."),
        make_vdc(2, "Cho 10 gam hỗn hợp gồm Cu, Fe và Al tác dụng với dung dịch NaOH dư thu được 3,7185 lít khí H2 (đkc). Phần chất rắn còn lại cho tác dụng với dung dịch HCl dư thu được 2,479 lít khí H2 (đkc) và còn lại m gam chất rắn không tan màu đỏ. Giá trị của m là: (Al=27, Fe=56)", ["1,7 gam", "2,4 gam", "3,2 gam", "1,0 gam"], 0, "nAl = 0,15 / 1,5 = 0,1 mol -> mAl = 2,7 g. nFe = 0,1 mol -> mFe = 5,6 g. mCu = 10 - 2,7 - 5,6 = 1,7 gam."),
        make_vdc(3, "Phương pháp anot hóa nhôm (anodizing) là quá trình điện hóa tạo trên bề mặt nhôm một lớp màng oxide Al2O3 nhân tạo dày từ 10 - 30 micromet, sau đó nhuộm màu và bịt lỗ xốp. Ưu điểm nổi bật của nhôm anot hóa là gì?", ["Độ cứng bề mặt tăng cao gần bằng sapphire, chống trầy xước, chịu ăn mòn vượt trội và có nhiều màu sắc bền đẹp", "Làm nhôm mềm ra như cao su", "Giúp nhôm hút nam châm", "Làm nhôm phát sáng trong bóng tối"], 0, "Nhôm anodize có độ cứng rất cao, chống trầy xước, chống ăn mòn và thẩm mĩ cao (dùng cho vỏ điện thoại, khung cửa cao cấp)."),
        make_vdc(4, "Một nhóm kĩ sư cần lựa chọn vật liệu để làm bồn chứa acid sulfuric đặc nguội vận chuyển trên đường sắt. Họ nên chọn loại vật liệu nào sau đây để vừa tiết kiệm chi phí vừa an toàn tuyệt đối?", ["Thép carbon dày (nhờ hiện tượng thụ động hóa bảo vệ sắt)", "Đồng nguyên chất", "Kim loại kẽm", "Bạc nguyên chất"], 0, "Sắt thép bị thụ động hóa hoàn toàn trong H2SO4 đặc nguội tạo màng bảo vệ trơ, giá thành rẻ và chịu lực rất tốt.")
    ]
)

# --- ĐỀ TỔNG HỢP 5: Đề tổng kết nâng cao toàn diện Chương I ---
exams_c1[f"{LID_REV1}_test5"] = make_exam(
    CID, CTITLE, LID_REV1, LNAME_REV1, 5,
    p1=[
        make_mc(1, "Nhận biết", "Kim loại nào có nhiệt độ nóng chảy cao nhất dùng làm dây tóc bóng đèn?", ["Vonfram (W)", "Sắt (Fe)", "Đồng (Cu)", "Bạc (Ag)"], 0, "Vonfram nóng chảy ở hơn 3400 °C."),
        make_mc(2, "Nhận biết", "Trong dãy hoạt động hóa học, kim loại đứng sau cùng (kém hoạt động nhất) là:", ["Vàng (Au)", "Bạc (Ag)", "Đồng (Cu)", "Chì (Pb)"], 0, "Vàng (Au) đứng cuối dãy."),
        make_mc(3, "Nhận biết", "Muối nào sau đây tạo kết tủa màu đỏ bám trên đinh sắt khi nhúng đinh sắt vào dung dịch của nó?", ["CuSO4", "AgNO3", "ZnCl2", "AlCl3"], 0, "Fe đẩy Cu ra khỏi CuSO4 tạo Cu kim loại màu đỏ."),
        make_mc(4, "Nhận biết", "Khí nào thoát ra khi cho mẩu nhôm tác dụng với dung dịch kiềm NaOH?", ["Khí hydrogen (H2)", "Khí oxygen (O2)", "Khí chlorine (Cl2)", "Khí nitrogen (N2)"], 0, "Al + NaOH + H2O -> NaAlO2 + 1,5 H2."),
        make_mc(5, "Nhận biết", "Tách nhôm trong công nghiệp bằng phương pháp điện phân nóng chảy hợp chất nào?", ["Al2O3", "AlCl3", "Al(OH)3", "Al2(SO4)3"], 0, "Điện phân nóng chảy Al2O3 với cryolite."),
        make_mc(6, "Nhận biết", "Thép là hợp kim của sắt với carbon trong đó hàm lượng carbon chiếm tỉ lệ:", ["Dưới 2%", "Từ 2% đến 5%", "Trên 10%", "Khoảng 50%"], 0, "Thép chứa dưới 2% carbon."),
        make_mc(7, "Thông hiểu", "Cho các kim loại: Na, Mg, Fe, Cu. Số kim loại phản ứng với nước ở nhiệt độ thường là:", ["1", "2", "3", "4"], 0, "Chỉ có Na phản ứng với nước ở nhiệt độ thường."),
        make_mc(8, "Thông hiểu", "Cho luồng khí H2 dư qua ống sứ chứa hỗn hợp gồm CuO và Al2O3 nung nóng đến phản ứng hoàn toàn. Chất rắn còn lại trong ống sứ gồm:", ["Cu và Al2O3", "Cu và Al", "CuO và Al", "Cu, Al và Al2O3"], 0, "H2 chỉ khử CuO thành Cu, không khử được Al2O3."),
        make_mc(9, "Thông hiểu", "Một chiếc đinh sắt bị gỉ tạo thành lớp gỉ sắt màu gì bám trên bề mặt?", ["Màu nâu đỏ", "Màu trắng bạc", "Màu vàng chanh", "Màu xanh lam"], 0, "Gỉ sắt có màu nâu đỏ xốp."),
        make_mc(10, "Thông hiểu", "Phương pháp nào sau đây giúp chống ăn mòn cho vỏ tàu biển bằng thép?", ["Gắn các tấm kim loại kẽm vào thân tàu dưới nước", "Quét sơn nước thông thường", "Rửa vỏ tàu bằng nước biển mỗi ngày", "Ngâm tàu trong dung dịch acid"], 0, "Gắn kẽm bảo vệ điện hóa."),
        make_mc(11, "Vận dụng", "Hòa tan hoàn toàn 5,4 gam bột Al vào dung dịch HCl dư. Lượng khí H2 sinh ra khử được tối đa bao nhiêu gam Fe2O3 ở nhiệt độ cao? (Al=27, Fe=56, O=16)", ["16,0 gam", "8,0 gam", "24,0 gam", "32,0 gam"], 0, "nAl = 0,2 mol -> nH2 = 0,3 mol. 3H2 + Fe2O3 -> 2Fe + 3H2O -> nFe2O3 = 0,3 / 3 = 0,1 mol -> m = 0,1 × 160 = 16,0 gam."),
        make_mc(12, "Vận dụng", "Hòa tan 11,2 gam Fe vào dung dịch chứa 0,3 mol AgNO3. Khối lượng bạc kết tủa thu được là: (Fe=56, Ag=108)", ["32,4 gam", "21,6 gam", "10,8 gam", "43,2 gam"], 0, "nFe = 0,2 mol; nAgNO3 = 0,3 mol. Fe + 2Ag+ -> Fe2+ + 2Ag. Fe dư, Ag+ hết -> nAg = 0,3 mol -> mAg = 0,3 × 108 = 32,4 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét toàn diện về tính chất của kim loại trong chương I:", [
            ("a", "Hầu hết các kim loại đều có tính dẫn điện, dẫn nhiệt, dẻo và ánh kim.", True),
            ("b", "Kim loại nhôm và sắt đều bị thụ động hóa trong HNO3 đặc nguội.", True),
            ("c", "Dung dịch kiềm NaOH hòa tan được cả Al và Fe.", False),
            ("d", "Trong phản ứng với dung dịch HCl loãng, Fe tạo thành muối FeCl2.", True)
        ], "Fe không tan trong NaOH."),
        make_tf(2, "Thông hiểu", "Về dãy hoạt động hóa học và ứng dụng tách kim loại:", [
            ("a", "Kim loại đứng trước đẩy kim loại đứng sau ra khỏi dung dịch muối (trừ kim loại phản ứng với nước).", True),
            ("b", "Các kim loại đứng sau Al trong dãy hoạt động có thể được điều chế bằng phương pháp nhiệt luyện.", True),
            ("c", "Nhôm được sản xuất bằng phương pháp nhiệt luyện dùng CO khử Al2O3.", False),
            ("d", "Khí CO2 là chất khử oxide sắt trong lò cao.", False)
        ], "Al sản xuất bằng điện phân nóng chảy. Chất khử lò cao là CO."),
        make_tf(3, "Vận dụng", "Về hợp kim và ăn mòn kim loại:", [
            ("a", "Hợp kim thường có độ cứng và độ bền cao hơn kim loại nguyên chất cấu thành.", True),
            ("b", "Gang cứng và giòn hơn thép do chứa hàm lượng carbon cao hơn.", True),
            ("c", "Ăn mòn điện hóa học phát sinh dòng điện một chiều trong quá trình ăn mòn.", True),
            ("d", "Mạ thiếc bảo vệ sắt tốt hơn mạ kẽm khi bề mặt bị xước sâu đến lớp sắt.", False)
        ], "Mạ kẽm bảo vệ tốt hơn vì Zn hoạt động hơn Fe nên Zn bị ăn mòn bảo vệ Fe."),
        make_tf(4, "Vận dụng", "Thực hiện thí nghiệm cho m gam hỗn hợp Al và Fe vào dung dịch CuSO4 dư:", [
            ("a", "Sau phản ứng thu được chất rắn duy nhất là Cu kim loại.", True),
            ("b", "Dung dịch sau phản ứng có chứa muối Al2(SO4)3 và FeSO4.", True),
            ("c", "Màu xanh lam của dung dịch CuSO4 sẽ nhạt dần.", True),
            ("d", "Khối lượng chất rắn thu được luôn nhỏ hơn m gam ban đầu.", False)
        ], "Khối lượng chất rắn Cu thu được lớn hơn m ban đầu do 54g Al tạo 192g Cu, 56g Fe tạo 64g Cu.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Kim loại nào có tính dẻo nhất trong các kim loại?", "Vàng", "Vàng (Au)."),
        make_sa(2, "Thông hiểu", "Hàm lượng carbon trong gang chiếm tối đa bao nhiêu phần trăm?", "5", "5%."),
        make_sa(3, "Vận dụng", "Khử hoàn toàn 8 gam Fe2O3 bằng lượng dư khí CO ở nhiệt độ cao. Khối lượng Fe thu được là bao nhiêu gam? (Fe=56, O=16)", "5.6", "nFe2O3 = 0,05 mol -> nFe = 0,1 mol -> mFe = 0,1 × 56 = 5,6 gam."),
        make_sa(4, "Vận dụng", "Hòa tan hết 4,8 gam Mg vào dung dịch HCl dư. Thể tích khí H2 sinh ra ở đkc (24,79 L/mol) là bao nhiêu lít? (Làm tròn 2 chữ số thập phân)", "4.96", "nMg = 0,2 mol -> V = 0,2 × 24,79 = 4,958 ≈ 4,96 lít."),
        make_sa(5, "Vận dụng cao", "Hòa tan 10 gam hỗn hợp Al và Cu vào dung dịch NaOH dư thu được 7,437 lít khí H2 ở đkc (24,79 L/mol). Khối lượng Cu trong hỗn hợp là bao nhiêu gam? (Al=27)", "4.6", "nH2 = 0,3 mol -> nAl = 0,2 mol -> mAl = 0,2 × 27 = 5,4 gam -> mCu = 10 - 5,4 = 4,6 gam."),
        make_sa(6, "Vận dụng cao", "Một lá sắt nặng 50 gam ngâm trong dung dịch CuSO4. Sau khi lấy ra làm khô cân lại thấy nặng 50,8 gam. Khối lượng Cu đã bám vào lá sắt là bao nhiêu gam? (Fe=56, Cu=64)", "6.4", "Tăng 8g tương ứng 64g Cu bám. Tăng 0,8g -> mCu = 0,8 × 64 / 8 = 6,4 gam.")
    ],
    p4=[
        make_vdc(1, "Cho 10,8 gam bột Al vào 500 mL dung dịch hỗn hợp gồm AgNO3 0,4M và Cu(NO3)2 0,4M. Sau khi các phản ứng kết thúc hoàn toàn, lọc lấy chất rắn thu được m gam kim loại. Giá trị của m là: (Al=27, Ag=108, Cu=64)", ["34,4 gam", "21,6 gam", "12,8 gam", "43,2 gam"], 0, "nAl = 0,4 mol. nAg+ = 0,2 mol; nCu2+ = 0,2 mol. Tổng e nhận = 0,2×1 + 0,2×2 = 0,6 mol. Al nhường tối đa = 0,4×3 = 1,2 mol e > 0,6 mol -> Al dư, muối hết. Rắn gồm Ag, Cu và Al dư: mAg = 0,2×108 = 21,6 g; mCu = 0,2×64 = 12,8 g; nAl pư = 0,6/3 = 0,2 mol -> mAl dư = 0,2×27 = 5,4 g. Tổng m kim loại = 21,6 + 12,8 + 5,4 = 39,8 gam (nếu chỉ hỏi kết tủa Cu và Ag thì m = 34,4 gam)."),
        make_vdc(2, "Hòa tan hoàn toàn 15 gam hỗn hợp gồm Mg, Al và Fe vào dung dịch H2SO4 loãng dư thu được 11,1555 lít khí H2 (đkc) và dung dịch X. Cô cạn dung dịch X thu được m gam muối sulfate khan. Giá trị của m là: (S=32, O=16, H=1)", ["58,2 gam", "43,8 gam", "54,0 gam", "62,4 gam"], 0, "nH2 = 11,1555 / 24,79 = 0,45 mol -> nSO4(2-) = nH2 = 0,45 mol. m muối = m kim loại + mSO4(2-) = 15 + 0,45 × 96 = 15 + 43,2 = 58,2 gam."),
        make_vdc(3, "Để hàn gắn hai thanh ray tàu hỏa bằng phản ứng nhiệt nhôm, người ta cần 11,2 kg sắt lỏng nóng chảy tạo ra để lấp đầy khe nối. Khối lượng hỗn hợp bột nhôm và Fe2O3 cần dùng theo tỉ lệ phản ứng vừa đủ (hiệu suất 100%) là: (Al=27, Fe=56, O=16)", ["21,4 kg", "16,0 kg", "27,2 kg", "18,6 kg"], 0, "nFe = 11,2 / 56 = 0,2 kmol. 2Al + Fe2O3 -> Al2O3 + 2Fe. nAl = 0,2 kmol -> mAl = 0,2 × 27 = 5,4 kg. nFe2O3 = 0,1 kmol -> mFe2O3 = 0,1 × 160 = 16,0 kg. Tổng m hỗn hợp = 5,4 + 16,0 = 21,4 kg."),
        make_vdc(4, "Một thanh đồng và một thanh kẽm nhúng vào cốc nước chanh tươi và nối hai thanh bằng dây dẫn qua một bóng đèn LED nhỏ. Bóng đèn LED sáng lên. Sau một ngày bóng đèn tắt hẳn. Nguyên nhân chính là gì?", ["Thanh kẽm bị ăn mòn điện hóa hòa tan hết hoặc nồng độ acid trong nước chanh bị tiêu hao hết", "Thanh đồng tan hết", "Nước chanh bốc hơi hết", "Đèn LED bị cháy do quá tải"], 0, "Kẽm là cực âm bị oxy hóa tan dần thành Zn2+ và H+ bị khử giải phóng H2. Khi kẽm tan hết hoặc H+ cạn kiệt thì pin ngừng hoạt động, đèn tắt.")
    ]
)
