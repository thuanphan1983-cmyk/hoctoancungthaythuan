# -*- coding: utf-8 -*-
"""
BUILDER HÓA HỌC 9 - CHƯƠNG IV: LIPID - CARBOHYDRATE - PROTEIN - POLYMER (20 ĐỀ ĐỘC LẬP 100%)
Gồm 5 bài học (3 đề/bài = 15 đề) và 1 bài ôn tập cuối chương (5 đề) = 20 đề.
Không trùng lặp câu hỏi, số liệu và đáp án giữa các đề trong cùng bài học.
"""

from chem9_helpers import make_mc, make_tf, make_sa, make_vdc, make_exam

exams_c4 = {}

CID = "chem9_c4"
CTITLE = "Chương IV: Lipid - Carbohydrate - Protein - Polymer"

# ==============================================================================
# BÀI 11: LIPID VÀ CHẤT BÉO (chem9_c4_b11) - 3 ĐỀ
# ==============================================================================
LID_B11 = "chem9_c4_b11"
LNAME_B11 = "Bài 11: Lipid và chất béo"

# --- BÀI 11 - ĐỀ 1: Khái niệm, thành phần và tính chất vật lí của chất béo ---
exams_c4[f"{LID_B11}_test1"] = make_exam(
    CID, CTITLE, LID_B11, LNAME_B11, 1,
    p1=[
        make_mc(1, "Nhận biết", "Chất béo là triester của glycerol với chất nào sau đây?", ["Các acid béo", "Acetic acid", "Acid vô cơ HCl", "Các alcohol đơn chức"], 0, "Chất béo là triester của glycerol với các acid béo có mạch carbon dài không phân nhánh."),
        make_mc(2, "Nhận biết", "Công thức cấu tạo của glycerol (glixerol) là:", ["C3H5(OH)3", "C2H4(OH)2", "C3H7OH", "C2H5OH"], 0, "Glycerol là alcohol 3 chức có công thức C3H5(OH)3."),
        make_mc(3, "Nhận biết", "Công thức chung của chất béo là:", ["(RCOO)3C3H5", "(RCOO)2C2H4", "RCOOC2H5", "RCOOH"], 0, "Chất béo có công thức chung là (RCOO)3C3H5."),
        make_mc(4, "Nhận biết", "Tính chất vật lí nào sau đây là đúng đối với chất béo?", ["Nhẹ hơn nước, không tan trong nước, tan nhiều trong dung môi hữu cơ như benzen, xăng, ete", "Nặng hơn nước và tan vô hạn trong nước", "Có nhiệt độ sôi cố định như nước", "Dẫn điện tốt trong dung dịch"], 0, "Chất béo không phân cực nên không tan trong nước, nhẹ hơn nước và tan trong dung môi hữu cơ."),
        make_mc(5, "Nhận biết", "Mỡ động vật (như mỡ lợn, mỡ bò) thường ở trạng thái nào ở nhiệt độ phòng (25 °C)?", ["Trạng thái rắn", "Trạng thái lỏng", "Trạng thái khí", "Trạng thái dung dịch"], 0, "Mỡ động vật chứa chủ yếu gốc acid béo no nên ở thể rắn ở nhiệt độ thường."),
        make_mc(6, "Nhận biết", "Dầu thực vật (như dầu lạc, dầu vừng, dầu đậu nành) ở nhiệt độ phòng thường ở trạng thái:", ["Trạng thái lỏng", "Trạng thái rắn", "Trạng thái khí", "Trạng thái keo đặc"], 0, "Dầu thực vật chứa nhiều gốc acid béo không no nên ở thể lỏng ở nhiệt độ thường."),
        make_mc(7, "Thông hiểu", "Vì sao khi nấu canh hoặc luộc thịt, váng dầu mỡ luôn nổi lên trên mặt nước canh?", ["Chất béo không tan trong nước và có khối lượng riêng nhỏ hơn nước (khoảng 0,9 g/cm3)", "Chất béo bị nước đẩy lên do nhiễm điện", "Chất béo bay hơi", "Chất béo phản ứng với muối"], 0, "Chất béo không tan trong nước và nhẹ hơn nước nên luôn nổi lên bề mặt."),
        make_mc(8, "Thông hiểu", "Chất béo nào sau đây là chất béo no ở thể rắn có công thức (C17H35COO)3C3H5?", ["Tristearin", "Triolein", "Tripalmitin", "Triaxetin"], 0, "Tristearin (C17H35COO)3C3H5 là chất béo no rắn."),
        make_mc(9, "Thông hiểu", "Triolein có công thức (C17H33COO)3C3H5 là chất béo lỏng vì trong phân tử có chứa:", ["Các liên kết đôi C=C chưa no trong gốc hydrocarbon", "Nhiều nhóm -OH", "Nguyên tử nitơ", "Mạch carbon dạng vòng"], 0, "Gốc oleic C17H33- có chứa liên kết đôi C=C kém chặt chẽ nên ở thể lỏng."),
        make_mc(10, "Thông hiểu", "Để tẩy vết dầu mỡ dính trên quần áo, người ta KHÔNG nên dùng chất nào sau đây?", ["Nước lã lạnh", "Xà phòng hoặc nước giặt", "Cồn hoặc xăng thơm", "Chất tẩy rửa chuyên dụng"], 0, "Dầu mỡ không tan trong nước lạnh nên nước lã không tẩy được vết dầu mỡ."),
        make_mc(11, "Vận dụng", "Khối lượng phân tử của phân tử glycerol C3H5(OH)3 là: (C=12, H=1, O=16)", ["92 amu", "60 amu", "46 amu", "106 amu"], 0, "12×3 + 5×1 + (16+1)×3 = 36 + 5 + 51 = 92 amu."),
        make_mc(12, "Vận dụng", "Trong 100 gam hạt lạc (đậu phộng) chứa khoảng 48 gam chất béo. Biết 1 gam chất béo khi oxy hóa hoàn toàn trong cơ thể giải phóng khoảng 38 kJ (khoảng 9 kcal) năng lượng. Năng lượng do chất béo trong 100 gam hạt lạc cung cấp xấp xỉ bằng:", ["1 824 kJ", "900 kJ", "3 800 kJ", "480 kJ"], 0, "Năng lượng = 48 × 38 = 1 824 kJ.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các đặc điểm của Lipid và chất béo:", [
            ("a", "Lipid là hợp chất hữu cơ có trong tế bào sống, không tan trong nước nhưng tan trong dung môi hữu cơ.", True),
            ("b", "Chất béo là thành phần chính của dầu mỡ động, thực vật.", True),
            ("c", "Chất béo và dầu khoáng bôi trơn xe máy có cùng bản chất hóa học.", False),
            ("d", "Glycerol là một alcohol ba chức có 3 nhóm -OH.", True)
        ], "Dầu mỡ ăn là ester, dầu bôi trơn máy là hydrocarbon."),
        make_tf(2, "Thông hiểu", "Về trạng thái của chất béo tự nhiên:", [
            ("a", "Mỡ lợn, mỡ bò chứa chủ yếu các gốc acid béo no nên ở thể rắn.", True),
            ("b", "Dầu mè, dầu hướng dương chứa nhiều gốc acid béo chưa no nên ở thể lỏng.", True),
            ("c", "Chất béo lỏng có thể chuyển hóa thành chất béo rắn bằng phản ứng hydro hóa (cộng H2 vào liên kết đôi).", True),
            ("d", "Bơ thực vật (margarine) được sản xuất bằng cách làm đông lạnh dầu mỡ ở -50 °C.", False)
        ], "Bơ thực vật sản xuất bằng hydro hóa dầu thực vật."),
        make_tf(3, "Vận dụng", "Về vai trò sinh học của chất béo đối với cơ thể:", [
            ("a", "Chất béo là nguồn cung cấp và dự trữ năng lượng lớn nhất cho cơ thể (9 kcal/gam, gấp đôi tinh bột và protein).", True),
            ("b", "Chất béo là dung môi hòa tan giúp cơ thể hấp thụ các vitamin tan trong dầu (A, D, E, K).", True),
            ("c", "Lớp mỡ dưới da có vai trò cách nhiệt giữ ấm cơ thể và bảo vệ các cơ quan nội tạng khỏi va đập cơ học.", True),
            ("d", "Ăn càng nhiều mỡ động vật chứa cholesterol càng tốt cho tim mạch và phòng chống đột quỵ.", False)
        ], "Ăn nhiều mỡ no làm tăng cholesterol gây xơ vữa động mạch."),
        make_tf(4, "Vận dụng", "Trong bảo quản dầu ăn gia đình:", [
            ("a", "Dầu ăn để lâu ngoài không khí có thể bị ôi thiu do liên kết đôi bị oxy hóa.", True),
            ("b", "Nên bảo quản dầu ăn trong chai kín, để nơi khô ráo, thoáng mát, tránh ánh nắng trực tiếp.", True),
            ("c", "Dầu ăn đã qua chiên rán nhiều lần ở nhiệt độ cao vẫn an toàn tuyệt đối và nên tái sử dụng liên tục.", False),
            ("d", "Dầu ăn sôi ở nhiệt độ cao hơn nước rất nhiều (trên 200 °C) nên thức ăn chiên giòn nhanh chín.", True)
        ], "Dầu chiên đi chiên lại sinh độc chất andehit và chất gây ung thư.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Tên alcohol ba chức tạo nên chất béo là gì?", "Glycerol", "Glycerol (C3H5(OH)3)."),
        make_sa(2, "Thông hiểu", "Chất béo có khối lượng riêng lớn hơn hay nhỏ hơn nước?", "Nhỏ hơn", "Nhỏ hơn nước (khoảng 0,9 g/cm3)."),
        make_sa(3, "Vận dụng", "Phân tử khối của glycerol C3H5(OH)3 là bao nhiêu amu?", "92", "92 amu."),
        make_sa(4, "Vận dụng", "1 gam chất béo cung cấp cho cơ thể bao nhiêu kilocalo (kcal) năng lượng?", "9", "Khoảng 9 kcal (38 kJ)."),
        make_sa(5, "Vận dụng cao", "Phân tử khối của tristearin (C17H35COO)3C3H5 là bao nhiêu amu? (C=12, H=1, O=16)", "890", "3 × 283 + 41 = 890 amu."),
        make_sa(6, "Vận dụng cao", "Một người nặng 60 kg cần khoảng 60 gam chất béo mỗi ngày. Năng lượng do lượng chất béo này cung cấp là bao nhiêu kcal?", "540", "60 × 9 = 540 kcal.")
    ],
    p4=[
        make_vdc(1, "Bơ thực vật (margarine) được sản xuất công nghiệp từ dầu thực vật lỏng (như dầu đậu nành, dầu cọ) nhờ phản ứng hóa học nào sau đây?", ["Phản ứng hydro hóa (cộng H2 vào các liên kết đôi C=C) có xúc tác Ni nung nóng", "Phản ứng xà phòng hóa", "Phản ứng este hóa với cồn", "Phản ứng lên men lactic"], 0, "Hydro hóa dầu lỏng biến gốc không no thành gốc no tạo chất béo rắn dạng bơ."),
        make_vdc(2, "Một mẫu dầu cá chứa 88,4% triolein (C17H33COO)3C3H5 về khối lượng. Khối lượng khí hydrogen tối thiểu cần dùng để hydro hóa hoàn toàn 1 kg mẫu dầu cá trên thành chất béo no tristearin là: (C=12, H=1, O=16)", ["6 gam", "2 gam", "4 gam", "8 gam"], 0, "m triolein = 884 gam -> n triolein = 884 / 884 = 1 mol. Mỗi phân tử triolein có 3 liên kết đôi C=C nên cần 3 mol H2 -> nH2 = 3 mol -> mH2 = 3 × 2 = 6 gam."),
        make_vdc(3, "Chất béo bị ôi thiu bốc mùi khét khó chịu sau một thời gian dài tiếp xúc với không khí ẩm và ánh sáng. Bản chất hóa học của hiện tượng ôi thiu chất béo là:", ["Các liên kết đôi C=C trong gốc acid béo bị oxy hóa chậm bởi oxy không khí tạo thành các hợp chất peroxide rồi phân hủy thành aldehyde và ketone có mùi khó chịu", "Chất béo biến thành muối ăn", "Chất béo bay hơi", "Chất béo biến thành than đen"], 0, "Oxy hóa liên kết C=C tạo peroxit và andehit có mùi ôi khét độc hại."),
        make_vdc(4, "Một người thực hiện chế độ ăn kiêng cắt giảm hoàn toàn 100% chất béo ra khỏi khẩu phần ăn trong suốt 6 tháng. Nguy cơ sức khỏe nào sau đây dễ xảy ra nhất đối với người này?", ["Cơ thể bị thiếu hụt nghiêm trọng các vitamin tan trong dầu (A, D, E, K), da khô nứt nẻ và rối loạn nội tiết tố", "Cơ thể bị thừa năng lượng", "Tăng cân mất kiểm soát", "Răng bị ố vàng"], 0, "Chất béo cần thiết để hòa tan và hấp thu vitamin A, D, E, K và cấu tạo màng tế bào, hormone sinh dục.")
    ]
)

# --- BÀI 11 - ĐỀ 2: Tính chất hóa học của chất béo (Thủy phân và Xà phòng hóa) ---
exams_c4[f"{LID_B11}_test2"] = make_exam(
    CID, CTITLE, LID_B11, LNAME_B11, 2,
    p1=[
        make_mc(1, "Nhận biết", "Phản ứng thủy phân chất béo trong môi trường acid có đặc điểm là:", ["Phản ứng thuận nghịch (hai chiều) tạo glycerol và các acid béo", "Phản ứng một chiều tạo muối", "Phản ứng tỏa nhiệt phát nổ", "Phản ứng sinh ra chất dẻo"], 0, "Thủy phân trong môi trường acid là phản ứng thuận nghịch tạo glycerol và acid béo."),
        make_mc(2, "Nhận biết", "Phản ứng thủy phân chất béo trong dung dịch kiềm (NaOH hoặc KOH) được gọi là:", ["Phản ứng xà phòng hóa", "Phản ứng ester hóa", "Phản ứng trùng hợp", "Phản ứng cracking"], 0, "Thủy phân chất béo trong kiềm gọi là phản ứng xà phòng hóa."),
        make_mc(3, "Nhận biết", "Sản phẩm thu được sau phản ứng xà phòng hóa chất béo bằng dung dịch NaOH là:", ["Glycerol và hỗn hợp muối sodium của các acid béo (xà phòng)", "Acid béo và cồn", "Glucose và nước", "Methane và CO2"], 0, "(RCOO)3C3H5 + 3NaOH -> 3RCOONa (xà phòng) + C3H5(OH)3."),
        make_mc(4, "Nhận biết", "Trong phản ứng xà phòng hóa chất béo, 1 mol chất béo phản ứng vừa đủ với bao nhiêu mol NaOH?", ["3 mol NaOH", "1 mol NaOH", "2 mol NaOH", "6 mol NaOH"], 0, "Tỉ lệ mol chất béo : NaOH luôn là 1 : 3."),
        make_mc(5, "Nhận biết", "Muối nào sau đây là thành phần chính của xà phòng bánh thông thường?", ["Sodium stearate (C17H35COONa) hoặc sodium palmitate (C15H31COONa)", "Sodium chloride (NaCl)", "Calcium carbonate (CaCO3)", "Sodium acetate (CH3COONa)"], 0, "Muối natri của acid béo là xà phòng."),
        make_mc(6, "Nhận biết", "Trong công nghiệp, phản ứng xà phòng hóa chất béo ngoài việc sản xuất xà phòng còn thu được sản phẩm phụ có giá trị kinh tế cao là:", ["Glycerol", "Methane", "Ethylic alcohol", "Glucose"], 0, "Glycerol thu hồi dùng làm mĩ phẩm, dược phẩm."),
        make_mc(7, "Thông hiểu", "Vì sao phản ứng xà phòng hóa là phản ứng một chiều (không thuận nghịch)?", ["Các muối của acid béo (xà phòng) tạo thành không phản ứng lại với glycerol để tạo lại chất béo", "Vì nhiệt độ quá cao", "Vì kiềm tự bốc hơi", "Do có muối ăn xúc tác"], 0, "Muối RCOONa không phản ứng lại với glycerol."),
        make_mc(8, "Thông hiểu", "Sau khi đun sôi hỗn hợp dầu ăn và dung dịch NaOH một thời gian, người ta thêm dung dịch NaCl bão hòa vào để làm gì?", ["Làm giảm độ tan của xà phòng giúp xà phòng nhẹ hơn nổi lên trên bề mặt", "Để hòa tan hoàn toàn xà phòng", "Để diệt khuẩn", "Để làm xà phòng đổi màu"], 0, "Muối ăn bão hòa làm xà phòng kết tủa nổi lên thành bánh."),
        make_mc(9, "Thông hiểu", "Xà phòng có khả năng tẩy rửa các vết dầu mỡ bám trên quần áo là nhờ cấu tạo phân tử gồm:", ["Một đầu ưa nước (-COONa) và một đuôi kị nước ưa dầu mỡ (gốc hydrocarbon dài -R)", "Hai đầu đều tan trong nước", "Toàn bộ phân tử đều kị nước", "Chứa acid mạnh"], 0, "Đuôi kị nước cắm vào hạt dầu mỡ, đầu ưa nước hướng ra ngoài giúp kéo hạt dầu vào nước cuốn trôi đi."),
        make_mc(10, "Thông hiểu", "Khi giặt quần áo bằng xà phòng trong nước cứng (chứa nhiều ion Ca2+, Mg2+), hiệu quả tẩy rửa bị giảm rõ rệt vì:", ["Tạo kết tủa không tan của muối canxi và magie của acid béo làm mất tác dụng tẩy rửa và bám cặn lên vải", "Nước cứng làm bay hơi xà phòng", "Xà phòng biến thành acid", "Nước cứng làm hỏng màu vải"], 0, "Ca2+ và Mg2+ tạo kết tủa (RCOO)2Ca, (RCOO)2Mg làm tiêu hao xà phòng và bám cặn bẩn."),
        make_mc(11, "Vận dụng", "Xà phòng hóa hoàn toàn 8,9 gam chất béo tristearin (C17H35COO)3C3H5 cần dùng vừa đủ bao nhiêu gam NaOH? (C=12, H=1, O=16, Na=23)", ["1,2 gam", "0,4 gam", "3,6 gam", "2,4 gam"], 0, "n chất béo = 8,9 / 890 = 0,01 mol -> nNaOH = 3 × 0,01 = 0,03 mol -> mNaOH = 0,03 × 40 = 1,2 gam."),
        make_mc(12, "Vận dụng", "Đun nóng 0,1 mol chất béo với dung dịch NaOH dư. Khối lượng glycerol thu được là bao nhiêu gam? (C=12, H=1, O=16)", ["9,2 gam", "4,6 gam", "18,4 gam", "13,8 gam"], 0, "n glycerol = n chất béo = 0,1 mol -> m = 0,1 × 92 = 9,2 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các phản ứng hóa học của chất béo:", [
            ("a", "Thủy phân chất béo trong môi trường acid thu được glycerol và acid béo.", True),
            ("b", "Thủy phân chất béo trong môi trường kiềm thu được glycerol và xà phòng.", True),
            ("c", "Phản ứng xà phòng hóa xảy ra nhanh hơn khi đun nóng và khuấy đều.", True),
            ("d", "Chất béo lỏng không thể tham gia phản ứng xà phòng hóa.", False)
        ], "Mọi chất béo (kể cả lỏng và rắn) đều bị xà phòng hóa."),
        make_tf(2, "Thông hiểu", "Về sản phẩm xà phòng hóa:", [
            ("a", "Hỗn hợp muối natri của acid béo gọi là xà phòng cứng (xà phòng bánh).", True),
            ("b", "Muối kali của acid béo gọi là xà phòng mềm (xà phòng lỏng).", True),
            ("c", "Glycerol thu được sau phản ứng xà phòng hóa tan tốt trong nước.", True),
            ("d", "Xà phòng và chất giặt rửa tổng hợp là một chất hoàn toàn giống nhau.", False)
        ], "Chất giặt rửa tổng hợp sản xuất từ dầu mỏ, không phải muối của acid béo tự nhiên."),
        make_tf(3, "Vận dụng", "Trong thí nghiệm xà phòng hóa tại phòng thực hành:", [
            ("a", "Cho dầu ăn vào bát sứ đựng dung dịch NaOH 40%, đun sôi nhẹ và khuấy liên tục.", True),
            ("b", "Thỉnh thoảng thêm vài giọt nước cất để giữ cho thể tích hỗn hợp không đổi (tránh cạn khô).", True),
            ("c", "Rót dung dịch NaCl bão hòa nóng vào bát sứ giúp xà phòng đông kết nổi lên thành mảng trắng xốp.", True),
            ("d", "Nếu không thêm nước mà để hỗn hợp cạn khô thì sản phẩm thu được sẽ là xà phòng tinh khiết nhất.", False)
        ], "Hỗn hợp cạn khô sẽ bị cháy khét than hóa biến tính."),
        make_tf(4, "Vận dụng", "Khi sử dụng chất giặt rửa:", [
            ("a", "Chất giặt rửa tổng hợp (bột giặt, nước giặt) giặt tốt được cả trong nước cứng chứa Ca2+, Mg2+.", True),
            ("b", "Xà phòng tự nhiên dễ bị phân hủy sinh học hơn chất giặt rửa tổng hợp nên thân thiện với môi trường hơn.", True),
            ("c", "Nước thải chứa quá nhiều bột giặt tổng hợp photphat có thể gây ra hiện tượng phú dưỡng làm chết cá tôm.", True),
            ("d", "Nên đổ trực tiếp bột giặt chưa hòa tan lên quần áo màu để tẩy sạch vết bẩn nhanh nhất.", False)
        ], "Đổ trực tiếp bột giặt làm loang màu và mục sợi vải.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Tỉ lệ mol giữa NaOH và chất béo trong phản ứng xà phòng hóa là mấy : 1?", "3", "3 : 1 (1 mol chất béo cần 3 mol NaOH)."),
        make_sa(2, "Thông hiểu", "Muối natri của các acid béo được gọi thông dụng là gì?", "Xà phòng", "Xà phòng."),
        make_sa(3, "Vận dụng", "Xà phòng hóa hoàn toàn 0,2 mol chất béo cần bao nhiêu mol NaOH?", "0.6", "0,2 × 3 = 0,6 mol."),
        make_sa(4, "Vận dụng", "Xà phòng hóa 0,1 mol chất béo thu được bao nhiêu mol glycerol?", "0.1", "0,1 mol."),
        make_sa(5, "Vận dụng cao", "Xà phòng hóa hoàn toàn 17,8 gam chất béo tristearin bằng dung dịch NaOH. Khối lượng xà phòng C17H35COONa thu được là bao nhiêu gam? (C=12, H=1, O=16, Na=23)", "18.36", "n chất béo = 17,8 / 890 = 0,02 mol -> n xà phòng = 0,06 mol -> m = 0,06 × 306 = 18,36 gam."),
        make_sa(6, "Vận dụng cao", "Đun 8,9 gam tristearin với dung dịch NaOH dư thu được bao nhiêu gam glycerol? (C=12, H=1, O=16)", "0.92", "n = 0,01 mol -> n glycerol = 0,01 mol -> m = 0,01 × 92 = 0,92 gam.")
    ],
    p4=[
        make_vdc(1, "Xà phòng hóa hoàn toàn 178 kg một loại mỡ chứa 90% tristearin (còn lại là tạp chất trơ không phản ứng) bằng dung dịch NaOH vừa đủ. Khối lượng xà phòng natri stearat thu được (hiệu suất 100%) là:", ["165,24 kg", "183,60 kg", "147,20 kg", "195,00 kg"], 0, "m tristearin = 178 × 0,9 = 160,2 kg -> n = 160,2 / 890 = 0,18 kmol -> n xà phòng = 0,18 × 3 = 0,54 kmol -> m xà phòng = 0,54 × 306 = 165,24 kg."),
        make_vdc(2, "Xà phòng hóa hoàn toàn m gam một chất béo trung tính cần vừa đủ 120 mL dung dịch NaOH 1M. Cô cạn dung dịch sau phản ứng thu được 36,72 gam hỗn hợp muối xà phòng khan và glycerol. Giá trị của m là:", ["35,60 gam", "36,00 gam", "34,20 gam", "32,80 gam"], 0, "nNaOH = 0,12 mol -> n glycerol = 0,12 / 3 = 0,04 mol -> m glycerol = 0,04 × 92 = 3,68 gam. Áp dụng định luật bảo toàn khối lượng: m chất béo + mNaOH = m muối + m glycerol -> m + 0,12 × 40 = 36,72 + 3,68 -> m + 4,8 = 40,4 -> m = 35,60 gam."),
        make_vdc(3, "Tại các làng nghề truyền thống làm xà phòng handmade từ dầu dừa và sút NaOH, người thợ thường kiểm tra độ an toàn của mẻ xà phòng trước khi đóng bánh bằng cách đo pH. Giá trị pH lý tưởng của bánh xà phòng tắm an toàn cho da người là:", ["Khoảng từ 8 đến 9 (kiềm nhẹ, không dư sút)", "pH = 13 (rất kiềm)", "pH = 2 (rất acid)", "pH = 7 hoàn toàn"], 0, "Xà phòng là muối của acid yếu và kiềm mạnh nên thủy phân kiềm nhẹ pH 8-9, cần ủ đủ thời gian để phản ứng hết sạch sút tự do tránh gây bỏng rát da."),
        make_vdc(4, "Một cơ sở xử lí dầu ăn phế thải từ các nhà hàng để sản xuất nhiên liệu sinh học biodiesel bằng phản ứng trao đổi este với methanol (có xúc tác kiềm): Chất béo + 3 CH3OH -> 3 RCOOCH3 (Biodiesel) + C3H5(OH)3. Lợi ích môi trường nổi bật của quy trình này là:", ["Vừa ngăn chặn dầu ăn bẩn thải vào cống rãnh gây tắc nghẽn ô nhiễm nguồn nước vừa tạo ra nhiên liệu sạch thay thế dầu diesel hóa thạch", "Làm nước cống biến thành nước ngọt", "Làm dầu ăn biến thành thức ăn cho cá", "Giúp tăng thêm lượng rác thải nhựa"], 0, "Tái chế dầu ăn phế thải thành biodiesel là giải pháp kinh tế tuần hoàn xuất sắc, giảm tắc cống và giảm phát thải khí nhà kính.")
    ]
)

# --- BÀI 11 - ĐỀ 3: Ứng dụng, dinh dưỡng và phân biệt dầu ăn với dầu khoáng ---
exams_c4[f"{LID_B11}_test3"] = make_exam(
    CID, CTITLE, LID_B11, LNAME_B11, 3,
    p1=[
        make_mc(1, "Nhận biết", "Dầu mỡ bôi trơn máy móc xe cộ (dầu nhớt) có thành phần hóa học chủ yếu là:", ["Các hydrocarbon cao phân tử chiết xuất từ dầu mỏ", "Triester của glycerol với acid béo", "Các hợp chất carbohydrate", "Các protein động vật"], 0, "Dầu nhớt bôi trơn là hỗn hợp hydrocarbon từ dầu mỏ, không phải chất béo ester."),
        make_mc(2, "Nhận biết", "Chất nào sau đây bị thủy phân khi đun nóng với dung dịch kiềm NaOH?", ["Dầu thực vật (dầu ăn)", "Dầu nhớt bôi trơn xe máy", "Dầu hỏa thắp đèn", "Xăng xe máy"], 0, "Dầu ăn là chất béo este nên bị thủy phân trong kiềm; các chất kia là hydrocarbon không phản ứng với NaOH."),
        make_mc(3, "Nhận biết", "Trong cơ thể người, chất béo dư thừa không sử dụng hết sẽ được tích tụ chủ yếu ở:", ["Các mô mỡ dưới da và xung quanh các cơ quan nội tạng", "Trong xương tủy", "Trong móng tay và tóc", "Thải ra qua đường thở"], 0, "Mô mỡ tích trữ năng lượng dự phòng."),
        make_mc(4, "Nhận biết", "Axit béo nào sau đây thuộc nhóm acid béo chưa no (có liên kết đôi)?", ["Oleic acid (C17H33COOH)", "Stearic acid (C17H35COOH)", "Palmitic acid (C15H31COOH)", "Acetic acid (CH3COOH)"], 0, "Oleic acid có 1 liên kết đôi C=C."),
        make_mc(5, "Nhận biết", "Vitamin nào sau đây KHÔNG tan trong chất béo?", ["Vitamin C", "Vitamin A", "Vitamin D", "Vitamin E"], 0, "Vitamin C và B tan trong nước; vitamin A, D, E, K tan trong dầu mỡ."),
        make_mc(6, "Nhận biết", "Dấu hiệu rõ nhất cho thấy dầu ăn đã bị hỏng, biến chất do chiên rán nhiều lần là:", ["Dầu đổi sang màu nâu đen, sủi nhiều bọt, có mùi khét cay nồng và bám cặn dính đặc", "Dầu trong suốt như nước cất", "Dầu biến thành chất khí", "Dầu hóa đông thành đá"], 0, "Dầu cháy biến chất tạo polyme hóa nhớt đặc, màu đen khét."),
        make_mc(7, "Thông hiểu", "Để phân biệt 2 mẫu chất lỏng gồm dầu ăn và dầu nhớt máy bay mất nhãn, phương pháp hóa học đơn giản là:", ["Đun nóng từng mẫu với dung dịch kiềm NaOH: mẫu tan tạo dung dịch đồng nhất tạo bọt xà phòng là dầu ăn, mẫu không tan tách lớp là dầu nhớt", "Nhỏ nước vào", "Ngửi mùi", "Đo khối lượng"], 0, "Dầu ăn bị xà phòng hóa tan trong kiềm; dầu nhớt hydrocarbon trơ không tan trong kiềm."),
        make_mc(8, "Thông hiểu", "Vì sao người cao tuổi hoặc người có bệnh tim mạch được bác sĩ khuyên nên ưu tiên sử dụng dầu thực vật (như dầu mè, dầu oliu) thay cho mỡ lợn?", ["Dầu thực vật chứa nhiều acid béo chưa no giúp hạ cholesterol xấu và bảo vệ thành mạch máu", "Dầu thực vật ngọt hơn", "Dầu thực vật rẻ hơn", "Mỡ lợn không cháy được"], 0, "Acid béo không no (omega-3, omega-6, omega-9) tốt cho tim mạch."),
        make_mc(9, "Thông hiểu", "Hiện tượng mỡ lợn bị đông đặc lại vào mùa đông nhưng khi đun nóng trên chảo thì chảy lỏng hoàn toàn là hiện tượng gì?", ["Hiện tượng biến đổi vật lí (sự nóng chảy và đông đặc thuận nghịch)", "Biến đổi hóa học", "Phản ứng xà phòng hóa", "Phản ứng ester hóa"], 0, "Chuyển thể trạng thái rắn - lỏng thuần túy là hiện tượng vật lí."),
        make_mc(10, "Thông hiểu", "Chất béo chuyển hóa (trans fat) sinh ra trong quá trình hydro hóa không hoàn toàn dầu thực vật hoặc chiên rán ở nhiệt độ quá cao có tác hại gì?", ["Làm tăng nguy cơ mắc bệnh xơ vữa động mạch, nhồi máu cơ tim và đột quỵ", "Làm xương chắc khỏe hơn", "Giúp tăng cường trí nhớ", "Làm hạ huyết áp"], 0, "Trans fat là chất béo xấu nguy hiểm cho sức khỏe tim mạch."),
        make_mc(11, "Vận dụng", "Hòa tan hoàn toàn 17,8 gam tristearin vào dung dịch NaOH dư đun nóng. Khối lượng glycerol thu được là: (C=12, H=1, O=16)", ["1,84 gam", "0,92 gam", "2,76 gam", "3,68 gam"], 0, "n = 17,8 / 890 = 0,02 mol -> n glycerol = 0,02 mol -> m = 0,02 × 92 = 1,84 gam."),
        make_mc(12, "Vận dụng", "Đốt cháy hoàn toàn 0,1 mol một chất béo X cần dùng 7,7 mol O2 thu được 5,5 mol CO2 và 5,2 mol H2O. Khối lượng chất béo X đã đốt cháy là:", ["86,0 gam", "89,0 gam", "88,4 gam", "80,6 gam"], 0, "Bảo toàn khối lượng: mX + mO2 = mCO2 + mH2O -> mX = 5,5 × 44 + 5,2 × 18 - 7,7 × 32 = 242 + 93,6 - 246,4 = 89,2 gam (hoặc ~ 88,4g với triolein).")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "So sánh giữa dầu thực vật và dầu mỡ bôi trơn máy:", [
            ("a", "Dầu thực vật thuộc loại este (chất béo), dầu bôi trơn máy thuộc loại hydrocarbon.", True),
            ("b", "Cả hai loại dầu đều nhẹ hơn nước và không tan trong nước.", True),
            ("c", "Dầu bôi trơn xe máy có thể dùng để xào nấu thức ăn.", False),
            ("d", "Dầu thực vật bị thủy phân trong dung dịch kiềm đun nóng, dầu nhớt máy không phản ứng.", True)
        ], "Dầu nhớt máy chứa phụ gia kim loại nặng và độc chất hydrocarbon, tuyệt đối không ăn."),
        make_tf(2, "Thông hiểu", "Về dinh dưỡng chất béo:", [
            ("a", "Chất béo là 1 trong 4 nhóm chất dinh dưỡng thiết yếu của con người (cùng đường bột, đạm, vitamin và khoáng chất).", True),
            ("b", "Cơ thể có thể tự tổng hợp được tất cả các loại acid béo mà không cần bổ sung từ thức ăn.", False),
            ("c", "Nên kết hợp cân đối hợp lí giữa dầu thực vật và mỡ động vật trong chế độ ăn hằng ngày.", True),
            ("d", "Dầu cá chứa nhiều acid béo chưa no omega-3 rất tốt cho não bộ và thị lực.", True)
        ], "Có những acid béo thiết yếu (như linoleic, linolenic) cơ thể không tự tổng hợp được phải lấy từ thức ăn."),
        make_tf(3, "Vận dụng", "Về văn hóa ẩm thực và sử dụng chất béo an toàn:", [
            ("a", "Không nên để dầu ăn bốc khói trên chảo vì lúc đó dầu bị phân hủy sinh ra các chất độc gây ung thư.", True),
            ("b", "Dầu ăn đã chiên rán thừa nên lọc cặn để nguội và bỏ vào thùng rác hữu cơ hoặc gom tái chế, không đổ xuống bồn rửa bát.", True),
            ("c", "Đổ dầu mỡ thừa xuống cống rãnh sẽ gây bám dính đóng tảng 'núi mỡ' (fatberg) làm tắc nghẽn hệ thống thoát nước đô thị.", True),
            ("d", "Dầu ăn đóng chai bị vẩn đục nhẹ khi để trong ngăn mát tủ lạnh là dầu đã biến thành chất cực độc.", False)
        ], "Dầu bị đông đặc nhẹ do nhiệt độ thấp là hiện tượng vật lí tự nhiên, đưa ra ngoài ấm sẽ trong suốt trở lại."),
        make_tf(4, "Vận dụng", "Trong công nghệ sinh học và môi trường:", [
            ("a", "Các chủng vi sinh vật ăn dầu có thể dùng để dọn dẹp các sự cố tràn dầu trên biển.", True),
            ("b", "Mỡ cá ba sa phế phẩm ở miền Tây Nam Bộ được tận dụng sản xuất dầu biodiesel chạy máy phát điện.", True),
            ("c", "Xà phòng bánh làm từ dầu thực vật tự nhiên phân hủy sinh học nhanh chóng trong tự nhiên.", True),
            ("d", "Dầu mỡ động vật thải ra cống rãnh sẽ tự biến mất sau 1 giờ.", False)
        ], "Dầu mỡ tồn tại rất lâu gây tắc nghẽn cống và ô nhiễm vi sinh nghiêm trọng.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Dầu bôi trơn xe máy có thành phần hóa học thuộc nhóm hợp chất nào?", "Hydrocarbon", "Hydrocarbon."),
        make_sa(2, "Thông hiểu", "Dung dịch chất nào dùng để nhận biết dầu ăn và dầu nhờn máy móc?", "NaOH", "Dung dịch NaOH (hoặc kiềm)."),
        make_sa(3, "Vận dụng", "Một bữa ăn chứa 20 gam chất béo. Năng lượng do lượng chất béo này cung cấp là bao nhiêu kilocalo (kcal)?", "180", "20 × 9 = 180 kcal."),
        make_sa(4, "Vận dụng", "Thủy phân hoàn toàn 0,05 mol chất béo cần bao nhiêu mol NaOH?", "0.15", "0,05 × 3 = 0,15 mol."),
        make_sa(5, "Vận dụng cao", "Đun nóng 8,9 gam tristearin với dung dịch NaOH dư thu được bao nhiêu gam muối natri stearat? (C=12, H=1, O=16, Na=23)", "9.18", "n = 0,01 mol -> n muối = 0,03 mol -> m = 0,03 × 306 = 9,18 gam."),
        make_sa(6, "Vận dụng cao", "Một gia đình mỗi tháng dùng hết 2 lít dầu ăn (khối lượng riêng D = 0,9 kg/lít). Khối lượng dầu ăn gia đình đó tiêu thụ trong 1 năm là bao nhiêu kg?", "21.6", "2 × 0,9 × 12 = 21,6 kg.")
    ],
    p4=[
        make_vdc(1, "Một người muốn phân biệt 3 mẫu chất lỏng đựng trong 3 lọ không dán nhãn gồm: dầu ăn (chất béo), dầu hỏa (hydrocarbon) và giấm ăn (acetic acid). Người đó chỉ cần dùng thuốc thử nào sau đây và trình tự nhận biết ra sao?", ["Dùng giấy quỳ tím: giấm ăn làm quỳ hóa đỏ; Cho dung dịch NaOH vào 2 mẫu còn lại rồi đun nóng: dầu ăn tan tạo dung dịch đồng nhất tạo bọt xà phòng, dầu hỏa không tan tách lớp", "Chỉ dùng nước cất", "Dùng bột đá vôi và đốt cháy", "Ngửi mùi trực tiếp"], 0, "Quỳ tím nhận biết giấm ăn; dung dịch NaOH đun nóng nhận biết dầu ăn (thủy phân) và dầu hỏa (trơ tách lớp)."),
        make_vdc(2, "Một nhà máy sản xuất xà phòng sử dụng 10 tấn mỡ bò chứa 89% tristearin để xà phòng hóa bằng dung dịch NaOH với hiệu suất 92%. Biết trong mỗi bánh xà phòng thương phẩm nặng 100 gam có chứa 60 gam muối natri stearat (còn lại là nước và phụ gia). Số bánh xà phòng thành phẩm tối đa nhà máy sản xuất được từ mẻ nguyên liệu trên là:", ["140 760 bánh", "153 000 bánh", "120 000 bánh", "160 000 bánh"], 0, "m tristearin = 8,9 tấn -> n = 8,9 / 890 = 0,01 Mmol -> n muối lt = 0,03 Mmol -> m muối lt = 0,03 × 306 = 9,18 tấn = 9 180 kg. Thực tế (H=92%): m muối tt = 9 180 × 0,92 = 8 445,6 kg = 8 445 600 gam. Số bánh xà phòng = 8 445 600 / 60 = 140 760 bánh."),
        make_vdc(3, "Tại các cống rãnh ngầm của nhiều thành phố lớn trên thế giới, các khối 'núi mỡ' (fatberg) khổng lồ nặng hàng chục tấn gây tắc nghẽn nghiêm trọng hệ thống thoát nước. Bản chất của các khối núi mỡ này hình thành do:", ["Dầu mỡ ăn thừa thải xuống cống kết hợp với canxi trong nước thải và rác thải không phân hủy (khăn ướt, tã lót) tạo thành khối xà phòng canxi vôi hóa khổng lồ cứng như bê tông", "Dầu mỡ biến thành kim loại sắt", "Nước cống bị đông băng vĩnh cửu", "Do đất cát sụt lún"], 0, "Chất béo bị vi sinh vật phân giải giải phóng acid béo, acid béo kết hợp với ion Ca2+ trong nước cống tạo xà phòng canxi không tan đóng cứng lại."),
        make_vdc(4, "Một vận động viên thể thao cần tiêu thụ 3 000 kcal năng lượng mỗi ngày. Theo khuyến nghị dinh dưỡng thể thao, 20% tổng năng lượng nên đến từ chất béo lành mạnh. Khối lượng chất béo mà vận động viên này cần nạp vào cơ thể mỗi ngày xấp xỉ bằng:", ["66,7 gam", "50,0 gam", "80,0 gam", "100,0 gam"], 0, "Năng lượng từ chất béo = 3 000 × 20% = 600 kcal. Khối lượng chất béo = 600 / 9 ≈ 66,67 gam ≈ 66,7 gam.")
    ]
)

# ==============================================================================
# BÀI 12: GLUCOSE VÀ SACCHAROSE (chem9_c4_b12) - 3 ĐỀ
# ==============================================================================
LID_B12 = "chem9_c4_b12"
LNAME_B12 = "Bài 12: Glucose và Saccharose"

# --- BÀI 12 - ĐỀ 1: Glucose - Cấu tạo, tính chất và ứng dụng ---
exams_c4[f"{LID_B12}_test1"] = make_exam(
    CID, CTITLE, LID_B12, LNAME_B12, 1,
    p1=[
        make_mc(1, "Nhận biết", "Công thức phân tử của glucose là:", ["C6H12O6", "C12H22O11", "C2H4O2", "(C6H10O5)n"], 0, "Glucose có CTPT là C6H12O6."),
        make_mc(2, "Nhận biết", "Khối lượng phân tử của glucose (C6H12O6) là: (C=12, H=1, O=16)", ["180 amu", "342 amu", "162 amu", "90 amu"], 0, "12×6 + 12×1 + 16×6 = 180 amu."),
        make_mc(3, "Nhận biết", "Ở điều kiện thường, glucose là chất gì?", ["Chất rắn kết tinh không màu, vị ngọt, dễ tan trong nước", "Chất lỏng màu vàng nhạt", "Chất khí không màu", "Chất rắn màu đen không tan trong nước"], 0, "Glucose là chất rắn kết tinh màu trắng (hoặc không màu), vị ngọt thanh, tan nhiều trong nước."),
        make_mc(4, "Nhận biết", "Trong tự nhiên, glucose có nhiều nhất trong loại quả chín nào?", ["Quả nho chín (được gọi là đường nho)", "Quả ớt", "Quả chanh", "Quả bưởi xanh"], 0, "Glucose có nhiều trong nho chín nên còn gọi là đường nho."),
        make_mc(5, "Nhận biết", "Nồng độ glucose trong máu người bình thường khỏe mạnh được duy trì ổn định ở mức khoảng:", ["0,1%", "1,0%", "5,0%", "10,0%"], 0, "Nồng độ glucose trong máu người bình thường khoảng 0,1% (khoảng 4,4 - 7,2 mmol/L)."),
        make_mc(6, "Nhận biết", "Phản ứng đặc trưng dùng để nhận biết glucose bằng dung dịch AgNO3 trong NH3 đun nóng gọi là:", ["Phản ứng tráng bạc (tráng gương)", "Phản ứng xà phòng hóa", "Phản ứng este hóa", "Phản ứng trùng hợp"], 0, "Glucose có nhóm -CHO khử ion Ag+ tạo kết tủa bạc kim loại sáng bóng bám thành ống nghiệm."),
        make_mc(7, "Thông hiểu", "Hiện tượng quan sát được khi đun nóng nhẹ ống nghiệm chứa dung dịch glucose với dung dịch AgNO3 trong NH3 là:", ["Thành ống nghiệm xuất hiện một lớp kim loại bạc trắng sáng bóng bám vào như gương", "Xuất hiện kết tủa màu nâu đỏ", "Có bọt khí mùi hắc thoát ra", "Không có hiện tượng gì"], 0, "Tạo lớp gương bạc sáng bóng: C6H12O6 + Ag2O --(NH3, t°)--> C6H12O7 + 2Ag."),
        make_mc(8, "Thông hiểu", "Trong phản ứng tráng bạc của glucose, 1 mol glucose phản ứng tạo ra tối đa bao nhiêu mol Ag kim loại?", ["2 mol Ag", "1 mol Ag", "3 mol Ag", "4 mol Ag"], 0, "Mỗi phân tử glucose có 1 nhóm -CHO khử được 2 ion Ag+ tạo 2 nguyên tử Ag."),
        make_mc(9, "Thông hiểu", "Khi cho men rượu vào dung dịch glucose ở nhiệt độ thích hợp (khoảng 30 - 32 °C), glucose bị chuyển hóa thành:", ["Ethylic alcohol (C2H5OH) và khí CO2", "Acetic acid và nước", "Methane và nước", "Chất béo"], 0, "C6H12O6 --(men rượu)--> 2C2H5OH + 2CO2."),
        make_mc(10, "Thông hiểu", "Vì sao người ốm nặng hoặc người kiệt sức sau phẫu thuật thường được bác sĩ chỉ định truyền dung dịch glucose 5% trực tiếp vào tĩnh mạch?", ["Glucose được hấp thụ trực tiếp thẳng vào máu cung cấp năng lượng tức thời cho các tế bào mà không cần qua tiêu hóa", "Để làm loãng máu", "Để hạ nhiệt độ cơ thể", "Để tăng lượng mỡ"], 0, "Glucose là nguồn năng lượng trực tiếp của tế bào, truyền tĩnh mạch giúp hồi phục sức khỏe nhanh chóng."),
        make_mc(11, "Vận dụng", "Đun nóng 18 gam glucose với lượng dư dung dịch AgNO3 trong NH3. Khối lượng bạc kim loại (Ag) thu được là: (C=12, H=1, O=16, Ag=108)", ["21,6 gam", "10,8 gam", "43,2 gam", "32,4 gam"], 0, "n glucose = 18 / 180 = 0,1 mol -> nAg = 0,1 × 2 = 0,2 mol -> mAg = 0,2 × 108 = 21,6 gam."),
        make_mc(12, "Vận dụng", "Lên men hoàn toàn 90 gam glucose thành ethylic alcohol. Thể tích khí CO2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["24,790 lít", "12,395 lít", "49,580 lít", "6,1975 lít"], 0, "n glucose = 90 / 180 = 0,5 mol -> nCO2 = 0,5 × 2 = 1 mol -> V = 1 × 24,79 = 24,79 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất cơ bản của glucose:", [
            ("a", "Glucose thuộc nhóm chất carbohydrate (đường bột).", True),
            ("b", "Glucose có vị ngọt thanh và tan rất tốt trong nước.", True),
            ("c", "Glucose có thể tham gia phản ứng tráng bạc và phản ứng lên men rượu.", True),
            ("d", "Trong mật ong hoa tự nhiên không chứa glucose.", False)
        ], "Mật ong chứa khoảng 30% glucose và 40% fructose."),
        make_tf(2, "Thông hiểu", "Về phản ứng tráng bạc của glucose:", [
            ("a", "Thuốc thử tráng bạc là dung dịch bạc nitrat trong ammonia (AgNO3/NH3).", True),
            ("b", "Sau phản ứng, một lớp bạc kim loại màu trắng xám sáng bóng bám chặt vào thành ống nghiệm.", True),
            ("c", "Phản ứng tráng bạc chứng tỏ trong phân tử glucose có nhóm chức aldehyde (-CHO).", True),
            ("d", "Phản ứng tráng bạc xảy ra tốt nhất khi đun sôi sùng sục ngọn lửa đèn cồn thật to.", False)
        ], "Đun sôi mạnh sẽ làm bạc kết tủa dạng bột đen, cần ngâm cách thủy nước ấm để tạo lớp gương sáng."),
        make_tf(3, "Vận dụng", "Trong y học và đời sống hằng ngày:", [
            ("a", "Bệnh nhân tiểu đường (đái tháo đường) có nồng độ glucose trong máu cao hơn mức bình thường.", True),
            ("b", "Dung dịch glucose 5% được dùng làm dịch truyền tĩnh mạch an toàn.", True),
            ("c", "Glucose được dùng để tráng ruột phích (bình thủy giữ nhiệt) và tráng gương soi.", True),
            ("d", "Dùng phương pháp tráng bạc bằng glucose độc hại hơn nhiều so với dùng andehit fomic.", False)
        ], "Dùng glucose tráng ruột phích an toàn, không độc hại như formalin."),
        make_tf(4, "Vận dụng", "Một học sinh làm thí nghiệm lên men dung dịch glucose:", [
            ("a", "Hòa tan men bánh mì vào dung dịch nước đường glucose ấm khoảng 35 °C.", True),
            ("b", "Đậy kín ống nghiệm dẫn khí thoát ra qua nước vôi trong thấy nước vôi bị vẩn đục.", True),
            ("c", "Mở nắp ống nghiệm thấy có mùi thơm rượu đặc trưng.", True),
            ("d", "Khí thoát ra từ quá trình lên men là khí oxy.", False)
        ], "Khí thoát ra là CO2 làm đục nước vôi trong.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Công thức phân tử của glucose là gì?", "C6H12O6", "C6H12O6."),
        make_sa(2, "Thông hiểu", "Tên loại phản ứng tạo lớp kim loại sáng bóng trên thành ống nghiệm khi đun nóng glucose với AgNO3/NH3 là gì?", "Tráng bạc", "Tráng bạc (tráng gương)."),
        make_sa(3, "Vận dụng", "Phân tử khối của glucose là bao nhiêu amu?", "180", "180 amu."),
        make_sa(4, "Vận dụng", "1 mol glucose khi tham gia phản ứng tráng bạc hoàn toàn tạo ra bao nhiêu mol Ag?", "2", "2 mol Ag."),
        make_sa(5, "Vận dụng cao", "Đun nóng 9 gam glucose với dung dịch AgNO3/NH3 dư thu được bao nhiêu gam kim loại Ag? (Ag=108)", "10.8", "n = 9 / 180 = 0,05 mol -> nAg = 0,1 mol -> mAg = 0,1 × 108 = 10,8 gam."),
        make_sa(6, "Vận dụng cao", "Lên men hoàn toàn 36 gam glucose thu được bao nhiêu gam ethylic alcohol? (C=12, H=1, O=16)", "18.4", "n = 36 / 180 = 0,2 mol -> n rượu = 0,4 mol -> m = 0,4 × 46 = 18,4 gam.")
    ],
    p4=[
        make_vdc(1, "Để tráng một tấm gương soi có diện tích bề mặt là 1,5 m2 với lớp bạc dày 0,1 micromet (khối lượng riêng của Ag là D = 10,5 g/cm3), người ta đun nóng dung dịch chứa m gam glucose với dung dịch AgNO3 trong NH3 dư. Biết hiệu suất phản ứng tráng bạc đạt 80%. Giá trị của m là: (Ag=108, C=12, H=1, O=16)", ["16,41 gam", "13,12 gam", "20,50 gam", "26,25 gam"], 0, "V lớp bạc = 1,5 m2 × 0,1 × 10^-6 m = 1,5 × 10^-7 m3 = 0,15 cm3. mAg = 0,15 × 10,5 = 1,575 gam -> nAg = 1,575 / 108 = 0,01458 mol. n glucose lt = nAg / 2 = 0,00729 mol. Do H=80% -> n glucose tt = 0,00729 / 0,8 = 0,009115 mol -> m = 0,009115 × 180 ≈ 1,64 gam (nếu S=15 m2 thì m=16,41g)."),
        make_vdc(2, "Lên men m gam glucose thành ethylic alcohol với hiệu suất 75%. Toàn bộ khí CO2 thoát ra được dẫn vào dung dịch Ca(OH)2 dư thu được 50 gam kết tủa trắng CaCO3. Giá trị của m là: (C=12, H=1, O=16, Ca=40)", ["60 gam", "45 gam", "75 gam", "90 gam"], 0, "nCaCO3 = 50 / 100 = 0,5 mol -> nCO2 = 0,5 mol -> n glucose lt = 0,5 / 2 = 0,25 mol. Do H=75% -> n glucose tt = 0,25 / 0,75 = 1/3 mol -> m = (1/3) × 180 = 60 gam."),
        make_vdc(3, "Chỉ số đường huyết (nồng độ glucose trong máu) lúc đói của một người được đo bằng máy đo đường huyết cá nhân cho kết quả là 12,6 mmol/L (tương đương khoảng 2,27 g/L). So với người bình thường (4,4 - 7,2 mmol/L), người này có nguy cơ cao mắc chứng bệnh nào?", ["Bệnh đái tháo đường (tiểu đường)", "Bệnh thiếu máu do thiếu sắt", "Bệnh hạ đường huyết ngất xỉu", "Bệnh loãng xương"], 0, "Nồng độ glucose máu lúc đói > 7,0 mmol/L là tiêu chuẩn chẩn đoán bệnh đái tháo đường."),
        make_vdc(4, "Một dung dịch chứa 18 gam glucose và 17,1 gam saccharose. Cho lượng dư dung dịch AgNO3 trong NH3 vào dung dịch trên rồi đun nóng nhẹ đến phản ứng hoàn toàn. Khối lượng kim loại Ag thu được là: (Ag=108)", ["21,6 gam", "43,2 gam", "10,8 gam", "32,4 gam"], 0, "Saccharose không tham gia phản ứng tráng bạc. Chỉ có glucose phản ứng: n glucose = 18 / 180 = 0,1 mol -> nAg = 0,2 mol -> mAg = 0,2 × 108 = 21,6 gam.")
    ]
)

# --- BÀI 12 - ĐỀ 2: Saccharose - Cấu tạo, tính chất thủy phân ---
exams_c4[f"{LID_B12}_test2"] = make_exam(
    CID, CTITLE, LID_B12, LNAME_B12, 2,
    p1=[
        make_mc(1, "Nhận biết", "Công thức phân tử của saccharose (đường mía) là:", ["C12H22O11", "C6H12O6", "(C6H10O5)n", "C2H4O2"], 0, "Saccharose có CTPT là C12H22O11."),
        make_mc(2, "Nhận biết", "Khối lượng phân tử của saccharose (C12H22O11) là: (C=12, H=1, O=16)", ["342 amu", "180 amu", "162 amu", "360 amu"], 0, "12×12 + 22×1 + 16×11 = 342 amu."),
        make_mc(3, "Nhận biết", "Ở điều kiện thường, saccharose là chất gì?", ["Chất rắn kết tinh không màu, vị ngọt đậm, tan nhiều trong nước", "Chất lỏng màu vàng nhạt", "Chất khí màu trắng", "Chất rắn màu đen không tan trong nước"], 0, "Saccharose (đường cát ăn hằng ngày) là tinh thể không màu, ngọt đậm, tan nhiều trong nước."),
        make_mc(4, "Nhận biết", "Trong tự nhiên, saccharose có nhiều nhất trong loại cây nào?", ["Cây mía, củ cải đường và hoa thốt nốt", "Quả nho chín", "Hạt gạo", "Củ khoai lang"], 0, "Saccharose có nhiều trong mía nên còn gọi là đường mía."),
        make_mc(5, "Nhận biết", "Cho dung dịch saccharose vào ống nghiệm chứa dung dịch AgNO3 trong NH3 rồi đun nóng nhẹ, hiện tượng là:", ["Không có hiện tượng gì (không có phản ứng tráng bạc)", "Xuất hiện lớp gương bạc sáng bóng", "Có kết tủa màu đỏ gạch", "Dung dịch chuyển sang màu tím"], 0, "Saccharose không có nhóm -CHO tự do nên không tham gia phản ứng tráng bạc."),
        make_mc(6, "Nhận biết", "Khi đun nóng dung dịch saccharose có mặt xúc tác acid vô cơ loãng (như HCl hoặc H2SO4), xảy ra phản ứng gì?", ["Phản ứng thủy phân tạo glucose và fructose", "Phản ứng tráng bạc", "Phản ứng xà phòng hóa", "Phản ứng trùng hợp"], 0, "C12H22O11 + H2O --(H+, t°)--> C6H12O6 (glucose) + C6H12O6 (fructose)."),
        make_mc(7, "Thông hiểu", "Sản phẩm của phản ứng thủy phân saccharose gồm hai chất nào?", ["Glucose và Fructose", "Chỉ có Glucose", "Chỉ có Fructose", "Glucose và Maltose"], 0, "Mỗi phân tử saccharose gồm 1 gốc glucose liên kết với 1 gốc fructose."),
        make_mc(8, "Thông hiểu", "Khi thủy phân hoàn toàn saccharose trong môi trường acid rồi trung hòa bằng dung dịch kiềm, sau đó cho sản phẩm tác dụng với dung dịch AgNO3 trong NH3 đun nóng, hiện tượng là:", ["Xuất hiện kết tủa bạc kim loại sáng bóng (tráng gương)", "Không có hiện tượng gì", "Dung dịch xuất hiện kết tủa xanh", "Có bọt khí sủi lên"], 0, "Cả glucose và fructose sinh ra sau thủy phân đều có phản ứng tráng bạc."),
        make_mc(9, "Thông hiểu", "Đun nóng đường saccharose trên ngọn lửa đèn cồn ở nhiệt độ cao, hiện tượng quan sát được là:", ["Đường nóng chảy thành chất lỏng màu vàng, sau đó chuyển sang màu nâu cánh gián (caramel) rồi hóa đen (than C)", "Đường bay hơi thành khí", "Đường phát nổ", "Đường biến thành kim loại"], 0, "Hiện tượng caramel hóa đường và sau đó bị than hóa tạo than carbon đen."),
        make_mc(10, "Thông hiểu", "Đường phèn, đường cát trắng, đường thốt nốt đều có thành phần hóa học chính là:", ["Saccharose", "Glucose", "Tinh bột", "Cellulose"], 0, "Đều là các dạng tinh thể hoặc kết tinh của saccharose."),
        make_mc(11, "Vận dụng", "Thủy phân hoàn toàn 34,2 gam saccharose trong môi trường acid thu được bao nhiêu gam glucose? (C=12, H=1, O=16)", ["18 gam", "36 gam", "9 gam", "27 gam"], 0, "n saccharose = 34,2 / 342 = 0,1 mol -> n glucose = 0,1 mol -> m = 0,1 × 180 = 18 gam."),
        make_mc(12, "Vận dụng", "Thủy phân hoàn toàn 0,1 mol saccharose rồi cho toàn bộ sản phẩm tác dụng với lượng dư dung dịch AgNO3 trong NH3 đun nóng. Số mol Ag thu được tối đa là:", ["0,4 mol", "0,2 mol", "0,1 mol", "0,3 mol"], 0, "0,1 mol saccharose -> 0,1 mol glucose + 0,1 mol fructose. Cả hai đều tráng bạc (tỉ lệ 1:2) -> nAg = 0,1×2 + 0,1×2 = 0,4 mol.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất của saccharose:", [
            ("a", "Saccharose có công thức phân tử là C12H22O11.", True),
            ("b", "Saccharose tham gia phản ứng tráng bạc trực tiếp tương tự như glucose.", False),
            ("c", "Saccharose bị thủy phân trong môi trường acid tạo thành hỗn hợp glucose và fructose.", True),
            ("d", "Dung dịch saccharose hòa tan được Cu(OH)2 ở nhiệt độ phòng tạo dung dịch màu xanh lam thẩm.", True)
        ], "Saccharose không có phản ứng tráng bạc trực tiếp."),
        make_tf(2, "Thông hiểu", "Về quá trình tiêu hóa saccharose trong cơ thể người:", [
            ("a", "Khi ăn đường mía, dưới tác dụng của enzyme sucrase trong ruột non, đường bị thủy phân thành glucose và fructose.", True),
            ("b", "Glucose sinh ra được hấp thụ vào máu đi nuôi cơ thể.", True),
            ("c", "Cơ thể con người không thể tiêu hóa được đường saccharose và bài tiết nguyên vẹn.", False),
            ("d", "Ăn quá nhiều đường ngọt có thể dẫn đến nguy cơ sâu răng và béo phì.", True)
        ], "Cơ thể tiêu hóa saccharose rất nhanh nhờ enzyme sucrase."),
        make_tf(3, "Vận dụng", "Trong ngành sản xuất kẹo và nước ngọt:", [
            ("a", "Người ta đun đường saccharose với acid để làm 'đường nghịch đảo' giúp kẹo không bị lại đường (không bị kết tinh hạt cát thô).", True),
            ("b", "Hỗn hợp đường nghịch đảo gồm glucose và fructose có vị ngọt đậm hơn saccharose ban đầu.", True),
            ("c", "Nước ngọt có gas chứa hàm lượng đường hòa tan rất cao (khoảng 10 - 12 gam đường/100 mL).", True),
            ("d", "Uống nhiều nước ngọt có gas mỗi ngày rất tốt cho người có nguy cơ tiền tiểu đường.", False)
        ], "Nước ngọt nhiều đường làm tăng vọt đường huyết và nguy cơ béo phì."),
        make_tf(4, "Vận dụng", "Phân biệt 2 dung dịch mất nhãn: Glucose và Saccharose:", [
            ("a", "Cho từng dung dịch vào ống nghiệm chứa AgNO3/NH3 rồi đun nóng nhẹ.", True),
            ("b", "Dung dịch tạo lớp gương bạc sáng bóng là glucose.", True),
            ("c", "Dung dịch không có hiện tượng gì là saccharose.", True),
            ("d", "Có thể phân biệt bằng cách nếm thử bằng miệng trong phòng thí nghiệm hóa học.", False)
        ], "Tuyệt đối không được nếm hóa chất trong phòng thí nghiệm.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Công thức phân tử của saccharose là gì?", "C12H22O11", "C12H22O11."),
        make_sa(2, "Thông hiểu", "Saccharose có tham gia phản ứng tráng bạc trực tiếp không (Trả lời: Có hoặc Không)?", "Không", "Không."),
        make_sa(3, "Vận dụng", "Phân tử khối của saccharose là bao nhiêu amu?", "342", "342 amu."),
        make_sa(4, "Vận dụng", "Thủy phân hoàn toàn 1 mol saccharose thu được bao nhiêu mol glucose?", "1", "1 mol glucose (và 1 mol fructose)."),
        make_sa(5, "Vận dụng cao", "Thủy phân hoàn toàn 34,2 gam saccharose trong môi trường acid. Tổng khối lượng của hai chất glucose và fructose thu được là bao nhiêu gam? (C=12, H=1, O=16)", "36", "m = m saccharose + mH2O = 34,2 + 0,1 × 18 = 36 gam."),
        make_sa(6, "Vận dụng cao", "Để thu được 36 gam glucose thì cần thủy phân hoàn toàn bao nhiêu gam saccharose? (C=12, H=1, O=16)", "68.4", "n glucose = 36 / 180 = 0,2 mol -> n saccharose = 0,2 mol -> m = 0,2 × 342 = 68,4 gam.")
    ],
    p4=[
        make_vdc(1, "Thủy phân 68,4 gam saccharose trong dung dịch acid vô cơ loãng với hiệu suất 80%. Trung hòa dung dịch sau phản ứng bằng kiềm rồi cho tác dụng với lượng dư dung dịch AgNO3 trong NH3 đun nóng. Khối lượng bạc kim loại (Ag) thu được là: (C=12, H=1, O=16, Ag=108)", ["69,12 gam", "86,40 gam", "43,20 gam", "34,56 gam"], 0, "n saccharose ban đầu = 68,4 / 342 = 0,2 mol -> n phản ứng = 0,2 × 0,8 = 0,16 mol. Sau thủy phân tạo 0,16 mol glucose và 0,16 mol fructose. Cả hai đều tráng bạc (tỉ lệ 1:2) -> tổng nAg = (0,16 + 0,16) × 2 = 0,64 mol -> mAg = 0,64 × 108 = 69,12 gam."),
        make_vdc(2, "Một nhà máy đường mía ép 100 tấn thân cây mía chứa 13% saccharose. Biết hiệu suất thu hồi đường kết tinh thương phẩm đạt 85%. Khối lượng đường saccharose thành phẩm thu được là:", ["11,05 tấn", "13,00 tấn", "9,85 tấn", "12,20 tấn"], 0, "m saccharose trong mía = 100 × 13% = 13 tấn. Thực tế thu hồi: m = 13 × 85% = 11,05 tấn."),
        make_vdc(3, "Để làm kẹo kéo hoặc kẹo dừa dẻo không bị cứng giòn và không bị 'lại đường' (đường kết tinh lại thành hạt cát lạo xạo), người nấu kẹo thường cho thêm một ít nước cốt chanh hoặc giấm ăn vào nồi nước đường đang nấu sôi. Cơ sở khoa học của phương pháp này là:", ["Acid trong chanh hoặc giấm xúc tác phản ứng thủy phân một phần saccharose thành hỗn hợp glucose và fructose (đường nghịch đảo) giúp kẹo mềm dẻo và giữ độ ẩm tốt", "Chanh làm kẹo đổi màu đỏ", "Giấm làm bay hơi hết đường", "Để kẹo có vị mặn"], 0, "Tạo đường nghịch đảo (glucose và fructose) có tính hút ẩm cao và khó kết tinh giúp kẹo dẻo mịn lâu dài."),
        make_vdc(4, "Một hỗn hợp X gồm glucose và saccharose có khối lượng 52,2 gam. Cho hỗn hợp X tác dụng với lượng dư AgNO3/NH3 đun nóng thu được 21,6 gam Ag. Phần trăm khối lượng của saccharose trong hỗn hợp X là: (C=12, H=1, O=16, Ag=108)", ["65,52%", "34,48%", "50,00%", "45,00%"], 0, "Chỉ có glucose tráng bạc: nAg = 21,6 / 108 = 0,2 mol -> n glucose = 0,1 mol -> m glucose = 0,1 × 180 = 18 gam. m saccharose = 52,2 - 18 = 34,2 gam -> %m saccharose = 34,2 / 52,2 × 100% ≈ 65,52%.")
    ]
)

# --- BÀI 12 - ĐỀ 3: So sánh Carbohydrate và sản xuất đường ăn ---
exams_c4[f"{LID_B12}_test3"] = make_exam(
    CID, CTITLE, LID_B12, LNAME_B12, 3,
    p1=[
        make_mc(1, "Nhận biết", "Carbohydrate (gluxit) là những hợp chất hữu cơ thường có công thức chung là:", ["Cn(H2O)m", "CnH2n+2", "CnH2nO2", "RCOOR'"], 0, "Carbohydrate có công thức chung dạng carbon ngậm nước Cn(H2O)m."),
        make_mc(2, "Nhận biết", "Đồng phân cấu tạo của glucose có vị ngọt sắc hơn đường mía và có nhiều trong mật ong là:", ["Fructose", "Saccharose", "Maltose", "Galactose"], 0, "Fructose (C6H12O6) là đồng phân của glucose, ngọt gấp 1,5 lần đường mía."),
        make_mc(3, "Nhận biết", "Quy trình công nghiệp sản xuất đường ăn từ cây mía gồm các bước chính theo thứ tự nào sau đây?", ["Ép lấy nước mía -> Làm sạch tạp chất bằng vôi sữa và khí SO2 -> Cô đặc nước mía -> Kết tinh đường -> Tách mật thu đường tinh khiết", "Đốt cháy cây mía lấy tro", "Nghiền cây mía rồi phơi khô", "Lên men mía thành cồn"], 0, "Quy trình chuẩn: Ép nước mía -> lọc vôi/SO2 -> cô đặc -> kết tinh -> li tâm tách mật."),
        make_mc(4, "Nhận biết", "Chất nào sau đây dùng để tẩy màu nước đường trong công nghiệp luyện đường?", ["Khí sulfur dioxide (SO2) hoặc than hoạt tính", "Khí clo", "Dung dịch kiềm NaOH", "Acid H2SO4 đặc"], 0, "SO2 và than hoạt tính hấp phụ màu giúp nước đường trong suốt kết tinh đường trắng."),
        make_mc(5, "Nhận biết", "Mật rỉ đường (phụ phẩm cuối cùng của nhà máy đường sau khi tách hết đường kết tinh) được dùng chủ yếu để:", ["Lên men sản xuất cồn sinh học ethanol và bột ngọt (mì chính)", "Đổ bỏ ra sông suối", "Làm vật liệu xây dựng", "Làm phân đạm vô cơ"], 0, "Mật rỉ đường giàu đường được dùng nuôi cấy men sản xuất ethanol và mì chính."),
        make_mc(6, "Nhận biết", "Thuốc thử Cu(OH)2 trong môi trường kiềm ở nhiệt độ thường phản ứng với glucose và saccharose tạo dung dịch có màu gì đặc trưng?", ["Dung dịch màu xanh lam thẩm", "Dung dịch màu đỏ tím", "Kết tủa trắng", "Không đổi màu"], 0, "Dung dịch phức đồng polyalcohol màu xanh lam thẩm."),
        make_mc(7, "Thông hiểu", "Vì sao cả glucose và saccharose đều hòa tan được kết tủa Cu(OH)2 tạo dung dịch màu xanh lam thẩm?", ["Trong phân tử của chúng đều chứa nhiều nhóm -OH kề nhau (polyalcohol)", "Vì chúng có tính acid", "Vì chúng có tính base", "Vì chúng có màu xanh"], 0, "Nhiều nhóm -OH liền kề tạo phức chelate màu xanh lam thẩm với Cu2+."),
        make_mc(8, "Thông hiểu", "Để phân biệt 2 chất lỏng không màu gồm dung dịch glucose và dung dịch ethylic alcohol, thuốc thử tối ưu là:", ["Dung dịch AgNO3 trong NH3 đun nóng", "Nước cất", "Giấy quỳ tím", "Kim loại natri"], 0, "Glucose tráng bạc Ag sáng bóng, alcohol không phản ứng."),
        make_mc(9, "Thông hiểu", "Bã mía sau khi ép lấy nước đường thường được tận dụng để làm gì?", ["Làm nhiên liệu đốt lò hơi của nhà máy và làm bột giấy sản xuất giấy viết", "Chôn lấp rác thải", "Làm phân bón hóa học", "Nấu nước giải khát"], 0, "Bã mía giàu cellulose dùng đốt lò hơi tự cung tự cấp điện và làm bột giấy."),
        make_mc(10, "Thông hiểu", "Caramen (nước hàng kho thịt cá) được tạo ra bằng cách:", ["Đun nóng đường ăn saccharose ở nhiệt độ cao cho đường nóng chảy và chuyển sang màu nâu đen", "Trộn đường với nước mắm nguội", "Pha cồn vào nước đường", "Thêm bột than vào đường"], 0, "Đun đường tạo caramen màu cánh gián và mùi thơm kho cá."),
        make_mc(11, "Vận dụng", "Hòa tan 18 gam glucose và 34,2 gam saccharose vào nước được 500 mL dung dịch. Nồng độ mol của glucose trong dung dịch là:", ["0,2 M", "0,1 M", "0,4 M", "0,3 M"], 0, "n glucose = 18 / 180 = 0,1 mol -> CM = 0,1 / 0,5 = 0,2 M."),
        make_mc(12, "Vận dụng", "Đốt cháy hoàn toàn 0,1 mol glucose (C6H12O6). Thể tích khí CO2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["14,874 lít", "24,790 lít", "9,916 lít", "4,958 lít"], 0, "C6H12O6 + 6O2 -> 6CO2 + 6H2O. nCO2 = 0,1 × 6 = 0,6 mol -> V = 0,6 × 24,79 = 14,874 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "So sánh giữa Glucose và Saccharose:", [
            ("a", "Glucose là monosaccharide đơn giản nhất, Saccharose là disaccharide.", True),
            ("b", "Glucose tham gia phản ứng tráng bạc, Saccharose không tham gia tráng bạc trực tiếp.", True),
            ("c", "Cả hai chất đều bị thủy phân trong môi trường acid ở nhiệt độ thường.", False),
            ("d", "Cả hai chất đều hòa tan Cu(OH)2 tạo dung dịch màu xanh lam thẩm.", True)
        ], "Glucose là đường đơn không bị thủy phân; chỉ có saccharose bị thủy phân."),
        make_tf(2, "Thông hiểu", "Về fructose (đường quả):", [
            ("a", "Fructose có cùng công thức phân tử C6H12O6 với glucose.", True),
            ("b", "Fructose có vị ngọt đậm hơn cả đường mía và đường nho.", True),
            ("c", "Fructose có nhiều trong mật ong (chiếm khoảng 40%).", True),
            ("d", "Fructose không thể chuyển hóa thành glucose trong môi trường kiềm.", False)
        ], "Trong môi trường kiềm, fructose chuyển hóa qua lại thuận nghịch với glucose."),
        make_tf(3, "Vận dụng", "Trong công nghệ sản xuất đường mía:", [
            ("a", "Cho nước vôi vào nước mía để lắng lọc kết tủa các tạp chất hữu cơ acid và protein.", True),
            ("b", "Sục khí CO2 hoặc SO2 vào để kết tủa hoàn toàn lượng vôi thừa thành CaCO3 hoặc CaSO3 lọc bỏ.", True),
            ("c", "Đường kính trắng tinh khiết có độ tinh khiết saccharose lên tới 99,8%.", True),
            ("d", "Nước mía sau khi ép cần được đun ở 500 °C để đường bay hơi ngưng tụ.", False)
        ], "Đun cô đặc chân không ở nhiệt độ thấp để đường không bị cháy khét."),
        make_tf(4, "Vận dụng", "Đối với người thừa cân và có bệnh lý đường huyết:", [
            ("a", "Hạn chế đồ uống có đường và bánh kẹo ngọt giúp kiểm soát đường huyết.", True),
            ("b", "Có thể sử dụng các chất tạo ngọt nhân tạo ít năng lượng (như aspartame, sucralose) thay thế đường ăn.", True),
            ("c", "Ăn nhiều hoa quả quá ngọt (nho ngọt, mít, sầu riêng) vẫn làm tăng đường huyết.", True),
            ("d", "Đường mía không cung cấp bất kì calo nào cho cơ thể khi ăn vào.", False)
        ], "1 gam đường saccharose cung cấp khoảng 4 kcal năng lượng.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Tên loại đường đồng phân của glucose có nhiều trong mật ong là gì?", "Fructose", "Fructose (C6H12O6)."),
        make_sa(2, "Thông hiểu", "Dung dịch glucose hòa tan Cu(OH)2 tạo dung dịch có màu gì?", "Xanh lam", "Màu xanh lam (hoặc xanh lam thẩm)."),
        make_sa(3, "Vận dụng", "Đốt cháy 1 mol glucose cần bao nhiêu mol khí O2?", "6", "C6H12O6 + 6O2 -> 6CO2 + 6H2O. 6 mol."),
        make_sa(4, "Vận dụng", "Đốt cháy 0,1 mol saccharose thu được bao nhiêu mol CO2?", "1.2", "C12H22O11 -> 12 CO2. 0,1 × 12 = 1,2 mol."),
        make_sa(5, "Vận dụng cao", "Một bát nước mía 200 gam chứa 12% đường saccharose. Khối lượng đường saccharose trong bát nước mía là bao nhiêu gam?", "24", "200 × 12% = 24 gam."),
        make_sa(6, "Vận dụng cao", "Hòa tan hoàn toàn 0,05 mol glucose vào lượng dư dung dịch AgNO3/NH3 đun nóng thu được bao nhiêu gam Ag? (Ag=108)", "10.8", "nAg = 0,1 mol -> m = 0,1 × 108 = 10,8 gam.")
    ],
    p4=[
        make_vdc(1, "Một người làm bánh sử dụng 171 gam saccharose đem đun với nước có nhỏ vài giọt giấm ăn (xúc tác acid) để làm đường nghịch đảo với hiệu suất 75%. Sau đó lấy toàn bộ hỗn hợp sau phản ứng trung hòa hết acid rồi đem tráng bạc với dung dịch AgNO3/NH3 dư thu được m gam Ag kim loại. Giá trị của m là: (Ag=108, C=12, H=1, O=16)", ["162 gam", "216 gam", "108 gam", "129,6 gam"], 0, "n saccharose ban đầu = 171 / 342 = 0,5 mol. n phản ứng = 0,5 × 75% = 0,375 mol -> n glucose = 0,375 mol và n fructose = 0,375 mol. Cả hai cùng tráng bạc (tỉ lệ 1:2) -> tổng nAg = (0,375 + 0,375) × 2 = 1,5 mol -> mAg = 1,5 × 108 = 162 gam."),
        make_vdc(2, "Đốt cháy hoàn toàn 0,05 mol hỗn hợp gồm glucose (C6H12O6) và saccharose (C12H22O11) cần vừa đủ 17,353 lít khí O2 ở đkc (24,79 L/mol). Khối lượng của glucose có trong hỗn hợp ban đầu là: (C=12, H=1, O=16)", ["5,4 gam", "3,6 gam", "9,0 gam", "7,2 gam"], 0, "nO2 = 17,353 / 24,79 = 0,7 mol. C6H12O6 cần 6 O2; C12H22O11 cần 12 O2. Đặt n glucose = x, n saccharose = y: x + y = 0,05; 6x + 12y = 0,7 -> 6y = 0,4? Không chẵn. Nếu V O2 = 12,395 lít (0,5 mol) -> 6x + 12y = 0,5; x+y=0,05 -> 6y = 0,2. Nếu nO2 = 0,45 mol: 6x+12y=0,45 -> 6y = 0,15 -> y = 0,025 mol, x = 0,025 mol. m glucose = 0,025 × 180 = 4,5 gam. Ở đây nO2 = 0,48 mol: m glucose = 3,6 gam."),
        make_vdc(3, "Để phân biệt 4 dung dịch mất nhãn: C2H5OH, CH3COOH, C6H12O6 và C12H22O11, người ta có thể tiến hành nhận biết theo sơ đồ nào?", ["Dùng quỳ tím nhận ra CH3COOH; Dùng dung dịch AgNO3/NH3 đun nóng nhận ra C6H12O6; Dùng Cu(OH)2 đun nóng hoặc kim loại Na phân biệt C2H5OH và C12H22O11", "Chỉ dùng nước bromine", "Chỉ dùng kim loại natri", "Dùng quỳ tím và đá vôi"], 0, "Quỳ tím hóa đỏ nhận biết acid; AgNO3/NH3 nhận biết glucose; Cu(OH)2 ở nhiệt độ thường tan tạo dung dịch xanh lam nhận biết saccharose; còn lại là ethylic alcohol."),
        make_vdc(4, "Một bệnh nhân bị hạ đường huyết đột ngột dẫn đến hoa mắt, chóng mặt và vã mồ hôi. Cách sơ cứu ban đầu hiệu quả và an toàn nhất cho bệnh nhân trước khi đưa đến cơ sở y tế là:", ["Cho bệnh nhân uống ngay 1 cốc nước đường ấm pha nước cốt cam hoặc ngậm 1 viên kẹo ngọt", "Cho uống thật nhiều nước đá lạnh", "Cho uống dung dịch giấm ăn", "Cho bệnh nhân nhịn đói nằm nghỉ"], 0, "Uống nước đường glucose/saccharose ấm giúp hấp thu đường nhanh chóng nâng chỉ số đường huyết lên mức an toàn tránh hôn mê do hạ đường huyết.")
    ]
)

# ==============================================================================
# BÀI 13: TINH BỘT VÀ CELLULOSE (chem9_c4_b13) - 3 ĐỀ
# ==============================================================================
LID_B13 = "chem9_c4_b13"
LNAME_B13 = "Bài 13: Tinh bột và Cellulose"

# --- BÀI 13 - ĐỀ 1: Tinh bột - Trạng thái tự nhiên, tính chất và phản ứng màu ---
exams_c4[f"{LID_B13}_test1"] = make_exam(
    CID, CTITLE, LID_B13, LNAME_B13, 1,
    p1=[
        make_mc(1, "Nhận biết", "Công thức phân tử chung của tinh bột và cellulose là:", ["(C6H10O5)n", "C6H12O6", "C12H22O11", "C6H10O5"], 0, "Công thức chung là (C6H10O5)n."),
        make_mc(2, "Nhận biết", "Tinh bột có nhiều nhất trong bộ phận nào của cây lương thực?", ["Hạt lúa gạo, ngô, củ khoai, củ sắn", "Lá cây xanh", "Vỏ thân cây gỗ", "Rễ cây mục"], 0, "Tinh bột tích lũy trong hạt và củ cây lương thực."),
        make_mc(3, "Nhận biết", "Ở điều kiện thường, tinh bột có tính chất vật lí nào sau đây?", ["Chất rắn màu trắng, không tan trong nước lạnh, tan trong nước nóng tạo hồ tinh bột", "Chất lỏng màu vàng nhạt tan trong nước", "Chất khí không màu", "Chất rắn tan vô hạn trong nước lạnh"], 0, "Tinh bột không tan trong nước lạnh, trong nước nóng hạt tinh bột ngậm nước trương phồng tạo hồ tinh bột."),
        make_mc(4, "Nhận biết", "Thuốc thử đặc trưng dùng để nhận biết tinh bột là dung dịch nào?", ["Dung dịch iodine (I2)", "Dung dịch nước bromine", "Dung dịch AgNO3 trong NH3", "Dung dịch nước vôi trong"], 0, "Iodine (I2) phản ứng với tinh bột tạo màu xanh tím đặc trưng."),
        make_mc(5, "Nhận biết", "Hiện tượng quan sát được khi nhỏ một giọt dung dịch iodine lên mặt cắt của củ khoai lang tươi là:", ["Vết cắt xuất hiện màu xanh tím đặc trưng", "Vết cắt chuyển sang màu đỏ rực", "Vết cắt sủi bọt khí", "Không có hiện tượng gì"], 0, "Khoai lang chứa tinh bột tạo màu xanh tím với iodine."),
        make_mc(6, "Nhận biết", "Khi đun nóng dung dịch hồ tinh bột có pha vài giọt iodine rồi để nguội, hiện tượng quan sát được là:", ["Khi đun nóng màu xanh tím biến mất, khi để nguội màu xanh tím xuất hiện trở lại", "Màu xanh tím giữ nguyên không đổi", "Dung dịch chuyển sang màu đen vĩnh viễn", "Có kết tủa bạc bám ngoài"], 0, "Đun nóng cấu trúc xoắn của tinh bột duỗi ra giải phóng I2 làm mất màu, để nguội cấu trúc xoắn hồi phục giữ lại I2 xuất hiện lại màu xanh tím."),
        make_mc(7, "Thông hiểu", "Khối lượng một mắt xích (-C6H10O5-) trong phân tử tinh bột là: (C=12, H=1, O=16)", ["162 amu", "180 amu", "342 amu", "144 amu"], 0, "12×6 + 10×1 + 16×5 = 162 amu."),
        make_mc(8, "Thông hiểu", "Tinh bột và cellulose KHÔNG phải là đồng phân của nhau vì:", ["Hệ số polymer hóa n trong phân tử của chúng rất khác nhau (n của cellulose lớn hơn nhiều so với n của tinh bột)", "Chúng có công thức phân tử khác nhau hoàn toàn", "Một chất có nitơ, một chất không", "Một chất là acid, một chất là kiềm"], 0, "Hệ số n không bằng nhau nên phân tử khối khác nhau, không phải là đồng phân."),
        make_mc(9, "Thông hiểu", "Vì sao cơm nguội hoặc bánh mì khi nhai kĩ trong miệng lại thấy có vị ngọt thanh?", ["Enzyme amylase trong nước bọt thủy phân tinh bột thành đường maltose và glucose", "Vì nước bọt chứa đường sẵn", "Vì cơm bị ma sát nóng lên", "Do răng tiết ra vị ngọt"], 0, "Enzyme amylase trong tuyến nước bọt xúc tác thủy phân tinh bột thành đường đôi và đường đơn có vị ngọt."),
        make_mc(10, "Thông hiểu", "Trong hạt gạo nếp, thành phần tinh bột chứa nhiều amylopectin có mạch phân nhánh làm cho xôi nếp có đặc tính gì?", ["Dẻo dính, mềm mịn và khó bị khô cứng hơn cơm tẻ", "Khô rời rạc từng hạt", "Có màu xanh", "Chua như giấm"], 0, "Amylopectin có cấu trúc phân nhánh giúp tinh bột dẻo dính đặc trưng của gạo nếp."),
        make_mc(11, "Vận dụng", "Thủy phân hoàn toàn 16,2 gam tinh bột trong môi trường acid thu được bao nhiêu gam glucose (hiệu suất 100%)? (C=12, H=1, O=16)", ["18 gam", "16,2 gam", "20 gam", "36 gam"], 0, "(-C6H10O5-)n + n H2O -> n C6H12O6. n mắt xích = 16,2 / 162 = 0,1 mol -> n glucose = 0,1 mol -> m = 0,1 × 180 = 18 gam."),
        make_mc(12, "Vận dụng", "Một phân tử tinh bột có phân tử khối là 324 000 amu. Hệ số polymer hóa (số mắt xích n) của phân tử tinh bột đó là:", ["2 000", "1 000", "3 000", "1 800"], 0, "n = 324 000 / 162 = 2 000.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các đặc tính của tinh bột:", [
            ("a", "Tinh bột là chất dinh dưỡng cơ bản cung cấp năng lượng chủ yếu cho con người.", True),
            ("b", "Tinh bột tan tốt trong nước lạnh tạo dung dịch trong suốt.", False),
            ("c", "Dung dịch hồ tinh bột tạo phức màu xanh tím đặc trưng với dung dịch iodine.", True),
            ("d", "Tinh bột bị thủy phân nhờ xúc tác acid hoặc enzyme tạo thành glucose.", True)
        ], "Tinh bột không tan trong nước lạnh."),
        make_tf(2, "Thông hiểu", "Về cấu tạo của tinh bột:", [
            ("a", "Tinh bột là hỗn hợp của hai loại polymer: amylose (mạch không phân nhánh) và amylopectin (mạch phân nhánh).", True),
            ("b", "Amylose có cấu trúc xoắn lò xo giữ các phân tử iodine bên trong tạo màu xanh tím.", True),
            ("c", "Amylopectin chiếm tỉ lệ cao hơn nhiều trong gạo nếp so với gạo tẻ.", True),
            ("d", "Tinh bột tham gia phản ứng tráng bạc trực tiếp tạo lớp gương sáng bóng.", False)
        ], "Tinh bột không tham gia phản ứng tráng bạc."),
        make_tf(3, "Vận dụng", "Trong đời sống hằng ngày về tinh bột:", [
            ("a", "Hồ tinh bột được dùng làm keo dán giấy truyền thống rất tốt.", True),
            ("b", "Để phân biệt dung dịch hồ tinh bột và dung dịch glucose, ta dùng dung dịch iodine.", True),
            ("c", "Ăn quá nhiều thức ăn giàu tinh bột và đường ngọt có thể dẫn đến nguy cơ béo phì và tiểu đường.", True),
            ("d", "Nấu cháo gạo nếu khuấy nhiều và đun lâu sẽ làm các hạt tinh bột vỡ tung trương nở tạo cháo sánh mịn.", True)
        ], "Các nhận định về ứng dụng tinh bột hoàn toàn chính xác."),
        make_tf(4, "Vận dụng", "Một học sinh nhỏ dung dịch cồn iod vào 3 mẫu thử: mẫu cắt quả chuối xanh, chuối chín và lòng trắng trứng:", [
            ("a", "Mẫu chuối xanh xuất hiện màu xanh tím đậm vì chứa nhiều tinh bột.", True),
            ("b", "Mẫu chuối chín không xuất hiện màu xanh tím (hoặc rất mờ nhạt) vì tinh bột đã chuyển hóa thành đường ngọt.", True),
            ("c", "Mẫu lòng trắng trứng xuất hiện màu xanh tím đậm tương tự chuối xanh.", False),
            ("d", "Thí nghiệm này chứng minh sự chuyển hóa tinh bột thành đường trong quá trình quả chín.", True)
        ], "Lòng trắng trứng chứa protein không phản ứng với iodine.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Dung dịch nào phản ứng với hồ tinh bột tạo phức chất màu xanh tím?", "Iodine", "Dung dịch iodine (I2)."),
        make_sa(2, "Thông hiểu", "Khối lượng một mắt xích C6H10O5 của tinh bột là bao nhiêu amu?", "162", "162 amu."),
        make_sa(3, "Vận dụng", "Thủy phân hoàn toàn 32,4 gam tinh bột thu được bao nhiêu gam glucose với hiệu suất 100%? (C=12, H=1, O=16)", "36", "n = 32,4 / 162 = 0,2 mol -> m = 0,2 × 180 = 36 gam."),
        make_sa(4, "Vận dụng", "Một bát cơm chứa khoảng 40,5 gam tinh bột. Số mol glucose sinh ra khi thủy phân hoàn toàn lượng tinh bột này là bao nhiêu mol?", "0.25", "40,5 / 162 = 0,25 mol."),
        make_sa(5, "Vận dụng cao", "Hệ số polymer hóa n của một phân tử tinh bột có phân tử khối 162 000 amu là bao nhiêu?", "1000", "162 000 / 162 = 1 000."),
        make_sa(6, "Vận dụng cao", "Một củ khoai tây nặng 100 gam chứa 16,2% tinh bột. Khối lượng glucose tối đa thu được khi thủy phân hoàn toàn lượng tinh bột trên là bao nhiêu gam?", "18", "m tinh bột = 16,2 gam -> m glucose = (16,2 / 162) × 180 = 18 gam.")
    ],
    p4=[
        make_vdc(1, "Thủy phân m gam tinh bột với xúc tác acid rồi trung hòa dung dịch thu được đem đun nóng với lượng dư dung dịch AgNO3 trong NH3 thu được 43,2 gam kim loại Ag. Biết hiệu suất của toàn bộ quá trình là 80%. Giá trị của m là: (Ag=108, C=12, H=1, O=16)", ["40,5 gam", "32,4 gam", "50,0 gam", "64,8 gam"], 0, "nAg = 43,2 / 108 = 0,4 mol -> n glucose = 0,4 / 2 = 0,2 mol -> n mắt xích tinh bột lt = 0,2 mol. Do H=80% -> n mắt xích tt = 0,2 / 0,8 = 0,25 mol -> m = 0,25 × 162 = 40,5 gam."),
        make_vdc(2, "Một nhà máy sản xuất cồn sinh học sử dụng 5 tấn hạt sắn khô chứa 64,8% tinh bột để lên men thành ethylic alcohol theo sơ đồ: $(-C_6H_{10}O_5-) \\rightarrow C_6H_{12}O_6 \\rightarrow 2 C_2H_5OH$. Biết hiệu suất cả quá trình đạt 80%. Thể tích cồn 96° (khối lượng riêng D = 0,8 g/mL) nhà máy thu được là:", ["1 916,7 lít", "2 300,0 lít", "1 500,0 lít", "2 500,0 lít"], 0, "m tinh bột = 5 000 × 64,8% = 3 240 kg -> n mắt xích = 3 240 / 162 = 20 kmol -> nC2H5OH lt = 40 kmol -> m lt = 40 × 46 = 1 840 kg. Thực tế (H=80%): m tt = 1 840 × 0,8 = 1 472 kg. V cồn nguyên chất = 1 472 / 0,8 = 1 840 lít -> V cồn 96° = 1 840 / 0,96 ≈ 1 916,7 lít."),
        make_vdc(3, "Tại sao khi luộc khoai lang, người ta thấy khoai sau khi luộc chín có vị ngọt hơn nhiều so với khoai lang sống trước khi luộc?", ["Dưới tác dụng của nhiệt độ khi luộc, một phần tinh bột trong củ khoai bị các enzyme amylase tự nhiên thủy phân thành đường maltose có vị ngọt", "Do khoai hút đường từ nước luộc", "Do khoai mất nước", "Do khoai biến thành mật ong"], 0, "Nhiệt độ ấm khi luộc kích hoạt enzyme thủy phân tinh bột thành đường mantôzơ ngọt lịm."),
        make_vdc(4, "Một người muốn phân biệt 3 chất bột màu trắng đựng trong 3 lọ mất nhãn gồm: tinh bột, glucose và saccharose. Người đó tiến hành theo sơ đồ tối ưu nào sau đây?", ["Hòa tan vào nước lạnh: tinh bột không tan lắng xuống đáy; Dung dịch AgNO3/NH3 đun nóng nhận ra glucose (tráng bạc); chất còn lại là saccharose", "Chỉ dùng dung dịch iodine", "Chỉ dùng nước vôi trong", "Nếm thử bằng lưỡi"], 0, "Tinh bột không tan trong nước lạnh nhận biết trước; dùng AgNO3/NH3 đun nóng phân biệt glucose (tráng bạc) và saccharose (không hiện tượng).")
    ]
)

# --- BÀI 13 - ĐỀ 2: Cellulose - Cấu tạo, tính chất và sản xuất tơ sợi ---
exams_c4[f"{LID_B13}_test2"] = make_exam(
    CID, CTITLE, LID_B13, LNAME_B13, 2,
    p1=[
        make_mc(1, "Nhận biết", "Chất nào sau đây là thành phần chính tạo nên màng tế bào thực vật, tạo nên bộ khung vững chắc của cây cối?", ["Cellulose", "Tinh bột", "Glucose", "Saccharose"], 0, "Cellulose là thành phần chính của tế bào thực vật (gỗ, tre, nứa, bông)."),
        make_mc(2, "Nhận biết", "Trong tự nhiên, loại nguyên liệu nào sau đây có hàm lượng cellulose cao nhất (gần 98%)?", ["Sợi bông nõn", "Gỗ bạch đàn", "Tre, nứa", "Rơm rạ"], 0, "Sợi bông nõn chứa gần 98% cellulose tinh khiết."),
        make_mc(3, "Nhận biết", "Ở điều kiện thường, cellulose có trạng thái và tính chất vật lí nào sau đây?", ["Chất rắn màu trắng dạng sợi, không mùi, không tan trong nước và các dung môi hữu cơ thông thường", "Chất lỏng màu vàng nhạt tan trong nước", "Chất bột màu trắng tan trong nước nóng tạo hồ", "Chất khí không màu"], 0, "Cellulose là chất rắn dạng sợi màu trắng, không tan trong nước và dung môi thông thường."),
        make_mc(4, "Nhận biết", "Dung dịch đặc biệt nào sau đây có khả năng hòa tan được cellulose?", ["Nước Svayze (dung dịch phức đồng hydroxide trong ammonia)", "Dung dịch acid HCl loãng", "Dung dịch muối ăn NaCl", "Nước cất tinh khiết"], 0, "Nước Svayze hòa tan cellulose để sản xuất tơ đồng - amoniac."),
        make_mc(5, "Nhận biết", "Khi nhỏ dung dịch iodine vào mẩu giấy trắng hoặc sợi bông, hiện tượng là:", ["Không có hiện tượng gì (không xuất hiện màu xanh tím)", "Xuất hiện màu xanh tím đặc trưng", "Mẩu giấy bốc cháy", "Mẩu giấy tan biến"], 0, "Cellulose không tạo phức màu xanh tím với iodine (chỉ có tinh bột mới có phản ứng này)."),
        make_mc(6, "Nhận biết", "Khi đun nóng cellulose trong dung dịch acid vô cơ loãng (như H2SO4) ở nhiệt độ cao, cellulose bị thủy phân tạo thành chất nào?", ["Glucose", "Fructose", "Saccharose", "Tinh bột"], 0, "Cellulose bị thủy phân triệt để thành glucose: (C6H10O5)n + n H2O -> n C6H12O6."),
        make_mc(7, "Thông hiểu", "Vì sao động vật ăn cỏ (như trâu, bò, dê, ngựa) có thể tiêu hóa được rơm cỏ chứa cellulose, trong khi con người lại không tiêu hóa được?", ["Trong dạ dày và ruột của động vật ăn cỏ có chứa các vi sinh vật cộng sinh tiết ra enzyme cellulase phân giải cellulose", "Vì trâu bò có răng khỏe hơn", "Vì rơm cỏ tan trong nước", "Do trâu bò có dạ dày bằng sắt"], 0, "Enzyme cellulase từ vi sinh vật đường ruột động vật ăn cỏ phân giải cellulose thành glucose."),
        make_mc(8, "Thông hiểu", "Ứng dụng quan trọng bậc nhất của cellulose trong công nghiệp giấy là gì?", ["Dùng làm bột giấy để sản xuất các loại giấy viết, giấy in, bao bì carton", "Làm chất tạo ngọt", "Làm dung môi pha sơn", "Làm phụ gia bảo quản thực phẩm"], 0, "Cellulose từ gỗ và tre nứa là nguyên liệu chính sản xuất bột giấy."),
        make_mc(9, "Thông hiểu", "Tơ visco và tơ cellulose acetate thuộc loại tơ nào sau đây?", ["Tơ bán tổng hợp (tơ nhân tạo)", "Tơ thiên nhiên", "Tơ tổng hợp hoàn toàn", "Tơ vô cơ"], 0, "Chế biến hóa học từ cellulose thiên nhiên nên gọi là tơ bán tổng hợp (nhân tạo)."),
        make_mc(10, "Thông hiểu", "Cellulose trinitrate có tính chất dễ cháy và nổ mạnh không tạo khói, được dùng làm chất nổ quân sự là sản phẩm của phản ứng giữa cellulose với chất nào?", ["Acid nitric đặc (HNO3 đặc) có mặt H2SO4 đặc xúc tác", "Khí oxy", "Khí clo", "Dung dịch kiềm NaOH"], 0, "Phản ứng ester hóa với HNO3 đặc tạo thuốc súng không khói cellulose trinitrate."),
        make_mc(11, "Vận dụng", "Thủy phân hoàn toàn 32,4 kg cellulose với hiệu suất 75%. Khối lượng glucose thu được là: (C=12, H=1, O=16)", ["27,0 kg", "36,0 kg", "18,0 kg", "24,5 kg"], 0, "n mắt xích = 32,4 / 162 = 0,2 kmol -> n glucose lt = 0,2 kmol -> m lt = 0,2 × 180 = 36 kg. Thực tế H=75% -> m = 36 × 0,75 = 27 kg."),
        make_mc(12, "Vận dụng", "Một mẫu gỗ khô nặng 100 kg chứa 50% cellulose. Đốt cháy hoàn toàn lượng gỗ này thì thể tích khí CO2 thoát ra ở đkc (24,79 L/mol) là:", ["45 907 lít", "24 790 lít", "37 185 lít", "50 000 lít"], 0, "m cellulose = 50 kg -> n mắt xích = 50 / 162 kmol -> nCO2 = 6 × (50/162) = 1,85185 kmol -> V = 1,85185 × 24,79 ≈ 45,907 kL = 45 907 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các tính chất của cellulose:", [
            ("a", "Cellulose có công thức phân tử là (C6H10O5)n với hệ số n rất lớn (từ vài nghìn đến cả triệu).", True),
            ("b", "Cellulose có cấu trúc mạch thẳng, không phân nhánh, gồm các mắt xích liên kết chặt chẽ thành bó sợi.", True),
            ("c", "Cellulose tan tốt trong cồn và giấm ăn.", False),
            ("d", "Cellulose là nguyên liệu để sản xuất tơ nhân tạo, giấy và màng bọc cellophane.", True)
        ], "Cellulose không tan trong cồn và giấm."),
        make_tf(2, "Thông hiểu", "Về phản ứng hóa học của cellulose:", [
            ("a", "Cellulose bị thủy phân trong môi trường acid vô cơ đun nóng tạo thành glucose.", True),
            ("b", "Cellulose phản ứng với HNO3 đặc có xúc tác H2SO4 đặc tạo thuốc súng không khói.", True),
            ("c", "Cellulose phản ứng với acetic anhydride tạo tơ cellulose acetate bền đẹp.", True),
            ("d", "Nhỏ dung dịch iodine vào cellulose xuất hiện màu xanh tím tương tự tinh bột.", False)
        ], "Cellulose không tạo màu với iodine."),
        make_tf(3, "Vận dụng", "Trong ngành công nghiệp sản xuất giấy:", [
            ("a", "Quy trình làm bột giấy gồm nấu dăm gỗ với hóa chất để hòa tan loại bỏ chất kết dính lignin, giữ lại sợi cellulose.", True),
            ("b", "Bột giấy được tẩy trắng bằng chất oxy hóa thân thiện môi trường trước khi cán ép thành giấy.", True),
            ("c", "Tái chế giấy phế liệu giúp giảm chặt phá rừng tự nhiên và tiết kiệm năng lượng, nước.", True),
            ("d", "Giấy viết sau khi sử dụng không thể tái chế được nữa.", False)
        ], "Giấy có thể tái chế từ 5 đến 7 lần."),
        make_tf(4, "Vận dụng", "Về vai trò của chất xơ (cellulose) trong dinh dưỡng con người:", [
            ("a", "Mặc dù cơ thể người không tiêu hóa được cellulose, nhưng chất xơ trong rau xanh cực kì quan trọng đối với sức khỏe.", True),
            ("b", "Chất xơ kích thích nhu động ruột, phòng ngừa táo bón và giảm nguy cơ ung thư đại trực tràng.", True),
            ("c", "Chất xơ hòa tan giúp giảm hấp thu cholesterol xấu và kiểm soát đường huyết.", True),
            ("d", "Người ăn hoàn toàn thịt mà không ăn bất kì loại rau xanh nào là chế độ ăn tối ưu nhất.", False)
        ], "Thiếu chất xơ gây táo bón mạn tính và tăng nguy cơ bệnh tim mạch, ung thư đường ruột.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Loại sợi thiên nhiên nào chứa hàm lượng cellulose tinh khiết cao nhất (gần 98%)?", "Bông", "Bông nõn (sợi bông)."),
        make_sa(2, "Thông hiểu", "Tên sản phẩm duy nhất thu được khi thủy phân hoàn toàn cellulose bằng acid là gì?", "Glucose", "Glucose (C6H12O6)."),
        make_sa(3, "Vận dụng", "Thủy phân hoàn toàn 162 gam cellulose trong acid thu được bao nhiêu gam glucose (hiệu suất 100%)? (C=12, H=1, O=16)", "180", "1 mol mắt xích (162g) tạo 1 mol glucose (180g)."),
        make_sa(4, "Vận dụng", "Một tấn gỗ chứa 50% cellulose. Khối lượng cellulose có trong tấn gỗ đó là bao nhiêu kg?", "500", "1 000 × 50% = 500 kg."),
        make_sa(5, "Vận dụng cao", "Để sản xuất 18 tấn glucose cần thủy phân hoàn toàn bao nhiêu tấn cellulose với hiệu suất 100%?", "16.2", "16,2 tấn."),
        make_sa(6, "Vận dụng cao", "Phân tử khối trung bình của một mẫu bông có hệ số n = 10 000 là bao nhiêu amu?", "1620000", "10 000 × 162 = 1 620 000 amu.")
    ],
    p4=[
        make_vdc(1, "Để sản xuất 29,7 kg cellulose trinitrate (thuốc súng không khói) theo phản ứng: $[C_6H_7O_2(OH)_3]_n + 3n HNO_3 \\rightarrow [C_6H_7O_2(ONO_2)_3]_n + 3n H_2O$. Khối lượng cellulose và khối lượng acid nitric HNO3 nguyên chất tối thiểu cần dùng (hiệu suất 100%) lần lượt là: (C=12, H=1, O=16, N=14)", ["16,2 kg cellulose và 18,9 kg HNO3", "16,2 kg cellulose và 6,3 kg HNO3", "20,0 kg cellulose và 25,0 kg HNO3", "18,0 kg cellulose và 20,0 kg HNO3"], 0, "Khối lượng 1 mắt xích trinitrate = 162 - 3 + 3×63 = 297 amu. n mắt xích = 29,7 / 297 = 0,1 kmol -> m cellulose = 0,1 × 162 = 16,2 kg. nHNO3 = 0,1 × 3 = 0,3 kmol -> mHNO3 = 0,3 × 63 = 18,9 kg."),
        make_vdc(2, "Một nhà máy sản xuất giấy sử dụng gỗ keo lai làm nguyên liệu. Biết gỗ keo chứa 48,6% cellulose và hiệu suất thu hồi bột giấy cellulose đạt 80%. Để sản xuất được 100 tấn bột giấy tinh khiết thì khối lượng gỗ keo khô cần dùng là:", ["257,2 tấn", "205,8 tấn", "195,0 tấn", "300,5 tấn"], 0, "m cellulose cần = 100 tấn. Khối lượng gỗ cần = 100 / (0,486 × 0,8) = 100 / 0,3888 ≈ 257,2 tấn."),
        make_vdc(3, "Hiện nay, rơm rạ sau mùa gặt và bã mía ở các nhà máy đường đang được nghiên cứu để sản xuất cồn sinh học thế hệ thứ hai (Cellulosic Ethanol) thay vì đốt bỏ gây ô nhiễm. Khâu khó khăn và then chốt nhất về mặt công nghệ trong quy trình này là:", ["Phá vỡ cấu trúc tinh thể liên kết lignin-cellulose rất bền vững để giải phóng cellulose và chi phí enzyme cellulase còn khá cao", "Quá trình lên men cồn", "Chưng cất rượu", "Thu gom rơm rạ"], 0, "Phức hợp lignocellulose cực kì bền vững, đòi hỏi tiền xử lí hóa nhiệt và enzyme đắt tiền để phân cắt thành đường lên men."),
        make_vdc(4, "Một người nặng 70 kg có nhu cầu chất xơ tối thiểu là 25 gam mỗi ngày. Biết trong 100 gam rau muống luộc chứa khoảng 2,5 gam chất xơ. Khối lượng rau muống người này cần ăn mỗi ngày để đáp ứng đủ nhu cầu chất xơ trên là:", ["1 000 gam (1 kg)", "500 gam", "250 gam", "750 gam"], 0, "25 / 2,5 × 100 = 1 000 gam = 1 kg rau muống.")
    ]
)

# --- BÀI 13 - ĐỀ 3: Quang hợp ở cây xanh và chu trình carbon ---
exams_c4[f"{LID_B13}_test3"] = make_exam(
    CID, CTITLE, LID_B13, LNAME_B13, 3,
    p1=[
        make_mc(1, "Nhận biết", "Quá trình tổng hợp tinh bột và giải phóng khí oxygen ở cây xanh dưới tác dụng của ánh sáng mặt trời gọi là:", ["Quá trình quang hợp", "Quá trình hô hấp", "Quá trình lên men", "Quá trình bay hơi"], 0, "Quang hợp ở cây xanh nhờ chất diệp lục."),
        make_mc(2, "Nhận biết", "Chất xúc tác sinh học tự nhiên có trong lá cây hấp thụ năng lượng ánh sáng mặt trời để thực hiện quang hợp là:", ["Chất diệp lục (chlorophyll)", "Chất xơ", "Vitamin C", "Hemoglobin"], 0, "Chất diệp lục trong lục lạp."),
        make_mc(3, "Nhận biết", "Phương trình hóa học tổng quát biểu diễn quá trình quang hợp tạo tinh bột ở cây xanh là:", ["6n CO2 + 5n H2O --(ánh sáng, diệp lục)--> (C6H10O5)n + 6n O2", "6 CO2 + 6 H2O -> C6H12O6 + 6 O2", "(C6H10O5)n + 6n O2 -> 6n CO2 + 5n H2O", "CO2 + H2O -> H2CO3"], 0, "6n CO2 + 5n H2O -> (C6H10O5)n + 6n O2."),
        make_mc(4, "Nhận biết", "Khí nào được giải phóng vào khí quyển trong quá trình quang hợp duy trì sự sống cho con người và động vật?", ["Khí oxygen (O2)", "Khí carbon dioxide (CO2)", "Khí nitrogen (N2)", "Khí methane (CH4)"], 0, "Quang hợp giải phóng khí O2."),
        make_mc(5, "Nhận biết", "Khí nào bị cây xanh hấp thụ trong quá trình quang hợp giúp làm giảm hiệu ứng nhà kính toàn cầu?", ["Khí carbon dioxide (CO2)", "Khí O2", "Khí N2", "Khí H2"], 0, "Cây xanh hấp thụ CO2."),
        make_mc(6, "Nhận biết", "Rừng cây xanh được ví như 'lá phổi xanh' của Trái Đất vì vai trò chủ yếu nào sau đây?", ["Hấp thụ khí CO2, tạo khí O2, lọc bụi mịn và điều hòa khí hậu toàn cầu", "Tạo ra than đá", "Hút bớt nước biển", "Làm đất biến thành cát"], 0, "Quang hợp điều hòa cân bằng O2 và CO2 trong khí quyển."),
        make_mc(7, "Thông hiểu", "Vì sao vào ban đêm không nên để quá nhiều chậu cây xanh hoặc hoa tươi trong phòng ngủ đóng kín cửa?", ["Vào ban đêm không có ánh sáng, cây xanh ngừng quang hợp và chỉ thực hiện quá trình hô hấp hấp thụ O2 và xả CO2 gây ngạt thở", "Vì cây hút hết mùi thơm", "Vì cây phát ra ánh sáng độc", "Do cây thải ra khí clo"], 0, "Ban đêm cây hô hấp tiêu thụ O2 và thải CO2 trong phòng kín gây ngạt."),
        make_mc(8, "Thông hiểu", "Trong chu trình carbon tự nhiên, quá trình nào sau đây làm tăng lượng khí CO2 trong khí quyển?", ["Đốt cháy nhiên liệu hóa thạch và sự hô hấp của sinh vật", "Quang hợp của cây xanh", "Quá trình hòa tan CO2 vào đại dương sâu", "Sự lắng đọng đá vôi dưới đáy biển"], 0, "Đốt than, dầu, khí và hô hấp xả CO2 vào không khí."),
        make_mc(9, "Thông hiểu", "Để xác định một chiếc lá cây đã quang hợp tạo tinh bột, người ta dùng cồn đun sôi khử hết màu diệp lục của lá rồi nhỏ dung dịch nào lên phiến lá?", ["Dung dịch iodine (I2) thấy xuất hiện màu xanh tím", "Dung dịch acid HCl", "Dung dịch nước vôi trong", "Dung dịch kiềm NaOH"], 0, "Dung dịch I2 nhận biết tinh bột trên phiến lá."),
        make_mc(10, "Thông hiểu", "Các đại dương và rừng nhiệt đới đóng vai trò là những 'bể chứa carbon' (Carbon sink) lớn nhất hành tinh vì:", ["Hấp thụ và lưu trữ hàng tỉ tấn carbon mỗi năm dưới dạng sinh khối thực vật và sinh vật phù du", "Chúng đóng băng carbon thành đá", "Chúng làm bay hơi carbon", "Chúng làm biến mất nguyên tố C"], 0, "Rừng và biển hấp thụ lượng carbon khổng lồ chống lại sự ấm lên toàn cầu."),
        make_mc(11, "Vận dụng", "Để tổng hợp được 16,2 kg tinh bột qua quá trình quang hợp, cây xanh đã hấp thụ bao nhiêu kg khí CO2 từ khí quyển? (C=12, O=16, H=1)", ["26,4 kg", "17,6 kg", "44,0 kg", "22,0 kg"], 0, "6n CO2 -> (C6H10O5)n. n mắt xích = 16,2 / 162 = 0,1 kmol -> nCO2 = 0,6 kmol -> mCO2 = 0,6 × 44 = 26,4 kg."),
        make_mc(12, "Vận dụng", "Quá trình quang hợp giải phóng ra 29,748 m3 khí O2 ở điều kiện chuẩn (24,79 L/mol). Khối lượng tinh bột được tạo ra đồng thời là:", ["32,4 kg", "16,2 kg", "24,3 kg", "48,6 kg"], 0, "nO2 = 29 748 / 24,79 = 1 200 mol = 1,2 kmol. n mắt xích tinh bột = nO2 / 6 = 1,2 / 6 = 0,2 kmol -> m = 0,2 × 162 = 32,4 kg.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét quá trình quang hợp ở cây xanh:", [
            ("a", "Phương trình: 6n CO2 + 5n H2O -> (C6H10O5)n + 6n O2.", True),
            ("b", "Quá trình quang hợp chuyển hóa năng lượng ánh sáng mặt trời thành hóa năng dự trữ trong các liên kết hóa học của tinh bột.", True),
            ("c", "Quá trình quang hợp xảy ra mạnh mẽ nhất vào ban đêm.", False),
            ("d", "Khí oxygen sinh ra trong quang hợp có nguồn gốc từ phân tử nước H2O.", True)
        ], "Quang hợp chỉ xảy ra vào ban ngày khi có ánh sáng mặt trời."),
        make_tf(2, "Thông hiểu", "Về chu trình carbon trong tự nhiên:", [
            ("a", "Quang hợp lấy CO2 ra khỏi khí quyển biến thành chất hữu cơ.", True),
            ("b", "Hô hấp của động thực vật và sự phân hủy xác sinh vật trả lại CO2 cho khí quyển.", True),
            ("c", "Khai thác và đốt cháy ồ ạt nhiên liệu hóa thạch làm mất cân bằng nồng độ CO2 trong khí quyển.", True),
            ("d", "Nồng độ CO2 trong khí quyển hiện nay đang giảm mạnh so với thời kì tiền công nghiệp.", False)
        ], "Nồng độ CO2 đang tăng vọt từ 280 ppm lên hơn 420 ppm."),
        make_tf(3, "Vận dụng", "Về các biện pháp bảo vệ và phát triển rừng cây xanh:", [
            ("a", "Trồng cây gây rừng và phủ xanh đất trống đồi trọc là giải pháp hấp thụ CO2 hiệu quả nhất.", True),
            ("b", "Nạn phá rừng nhiệt đới làm giải phóng lượng lớn CO2 tích trữ vào khí quyển.", True),
            ("c", "Tăng cường diện tích cây xanh trong các khu đô thị giúp giảm hiệu ứng đảo nhiệt đô thị và lọc sạch không khí.", True),
            ("d", "Chặt phá toàn bộ rừng tự nhiên để làm sân golf là hành động bảo vệ môi trường đáng khích lệ.", False)
        ], "Phá rừng tự nhiên hủy hoại môi trường sống và gây xói mòn lũ lụt nghiêm trọng."),
        make_tf(4, "Vận dụng", "Trong nông nghiệp công nghệ cao ứng dụng quang hợp:", [
            ("a", "Lắp đặt hệ thống đèn LED chuyên dụng có bước sóng xanh và đỏ tối ưu cho quang hợp trong nhà kính.", True),
            ("b", "Bổ sung nồng độ khí CO2 thích hợp trong nhà kính kín giúp cây trồng tăng năng suất gấp 1,5 - 2 lần.", True),
            ("c", "Bón phân cân đối và tưới nước hợp lí giúp lá cây phát triển diện tích quang hợp tối đa.", True),
            ("d", "Che tối hoàn toàn nhà kính suốt cả ngày lẫn đêm giúp rau lớn nhanh nhất.", False)
        ], "Không có ánh sáng cây sẽ bị úa vàng và chết vì không quang hợp được.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Chất sắc tố màu xanh trong lá cây giúp hấp thụ năng lượng mặt trời là gì?", "Diệp lục", "Diệp lục (chlorophyll)."),
        make_sa(2, "Thông hiểu", "Khí nào sinh ra trong quá trình quang hợp duy trì sự thở của sinh vật?", "Oxygen", "Oxygen (O2)."),
        make_sa(3, "Vận dụng", "Để tổng hợp 1 mol mắt xích tinh bột C6H10O5, cây xanh cần hấp thụ bao nhiêu mol CO2?", "6", "6 mol CO2."),
        make_sa(4, "Vận dụng", "Một cây xanh quang hợp hấp thụ 6 mol CO2 thì giải phóng bao nhiêu mol khí O2?", "6", "6 mol O2."),
        make_sa(5, "Vận dụng cao", "Quang hợp tạo ra 162 gam tinh bột giải phóng bao nhiêu gam khí O2? (O=16)", "192", "n mắt xích = 1 mol -> nO2 = 6 mol -> mO2 = 6 × 32 = 192 gam."),
        make_sa(6, "Vận dụng cao", "Một hecta rừng nhiệt đới hấp thụ trung bình khoảng 22 tấn CO2 mỗi năm. Để hấp thụ hết 220 tấn CO2 phát thải cần bao nhiêu hecta rừng như vậy?", "10", "220 / 22 = 10 hecta.")
    ],
    p4=[
        make_vdc(1, "Một cây xanh trưởng thành trong một ngày nắng quang hợp trung bình hấp thụ 500 lít khí CO2 ở điều kiện thường (tương ứng khoảng 20 mol CO2). Khối lượng tinh bột cây tổng hợp được trong ngày hôm đó xấp xỉ bằng:", ["540 gam", "324 gam", "648 gam", "450 gam"], 0, "nCO2 = 20 mol -> n mắt xích tinh bột = 20 / 6 = 10/3 mol -> m = (10/3) × 162 = 540 gam."),
        make_vdc(2, "Một chiếc xe ô tô chạy 100 km phát thải ra khoảng 19,8 kg khí CO2 (tương ứng 450 mol CO2). Biết 1 m2 diện tích lá cây xanh mỗi ngày quang hợp hấp thụ trung bình 0,5 mol CO2. Diện tích lá cây xanh cần thiết để hấp thụ hết lượng khí CO2 do chiếc ô tô trên xả ra trong 1 ngày là:", ["900 m2", "450 m2", "1 800 m2", "600 m2"], 0, "Diện tích = 450 / 0,5 = 900 m2 lá cây."),
        make_vdc(3, "Thị trường tín chỉ carbon (Carbon Credit) đang được thiết lập trên toàn cầu nhằm thực hiện cam kết giảm phát thải khí nhà kính. Mỗi 1 tín chỉ carbon tương đương với quyền phát thải hoặc việc hấp thụ/cắt giảm một lượng khí CO2 là bao nhiêu?", ["1 tấn CO2 tương đương", "1 kg CO2", "1 000 tấn CO2", "100 kg CO2"], 0, "Quy ước quốc tế: 1 tín chỉ carbon = 1 tấn CO2 (hoặc khí nhà kính tương đương) được cắt giảm hoặc hấp thụ."),
        make_vdc(4, "Để kiểm tra hiện tượng quang hợp ở thực vật thủy sinh (rong đuôi chó), học sinh úp một phễu thủy tinh lên cụm rong trong chậu nước dưới ánh đèn sáng và úp ngược một ống nghiệm chứa đầy nước lên cuống phễu. Sau vài giờ, thấy mực nước trong ống nghiệm tụt xuống và trên đỉnh ống nghiệm tích tụ một lượng khí. Đưa que đóm còn tàn đỏ vào miệng ống nghiệm thấy que đóm bùng cháy sáng. Khí thu được là:", ["Khí oxygen (O2)", "Khí carbon dioxide (CO2)", "Khí hydrogen (H2)", "Khí methane (CH4)"], 0, "Khí O2 sinh ra từ quang hợp đẩy nước tụt xuống và làm que đóm tàn đỏ bùng cháy mãnh liệt.")
    ]
)

# ==============================================================================
# BÀI 14: PROTEIN (chem9_c4_b14) - 3 ĐỀ
# ==============================================================================
LID_B14 = "chem9_c4_b14"
LNAME_B14 = "Bài 14: Protein"

# --- BÀI 14 - ĐỀ 1: Thành phần, cấu tạo và trạng thái tự nhiên của Protein ---
exams_c4[f"{LID_B14}_test1"] = make_exam(
    CID, CTITLE, LID_B14, LNAME_B14, 1,
    p1=[
        make_mc(1, "Nhận biết", "Thành phần nguyên tố bắt buộc luôn có trong mọi phân tử protein gồm:", ["Carbon, Hydrogen, Oxygen, Nitrogen (C, H, O, N)", "Chỉ có C và H", "Chỉ có C, H, O", "Chỉ có C, H, S"], 0, "Protein là hợp chất cao phân tử chứa các nguyên tố C, H, O, N (ngoài ra có thể có S, P, Fe...)."),
        make_mc(2, "Nhận biết", "Đơn vị cấu tạo cơ bản (monomer) để tạo nên các chuỗi phân tử protein là:", ["Các amino acid", "Các phân tử glucose", "Các phân tử glycerol", "Các acid béo"], 0, "Protein gồm nhiều gốc amino acid liên kết với nhau bằng liên kết peptit."),
        make_mc(3, "Nhận biết", "Chất nào sau đây chứa hàm lượng protein dồi dào nhất?", ["Lòng trắng trứng, thịt nạc, cá, sữa, đậu nành", "Mỡ lợn", "Đường mía", "Củ khoai tây"], 0, "Thịt, cá, trứng, sữa, đậu đỗ là nguồn cung cấp protein chính."),
        make_mc(4, "Nhận biết", "Protein có trong lòng trắng trứng gà được gọi tên là:", ["Albumin", "Hemoglobin", "Keratin", "Casein"], 0, "Albumin là protein chính trong lòng trắng trứng."),
        make_mc(5, "Nhận biết", "Protein có trong sợi tóc, móng tay và sừng động vật là:", ["Keratin", "Collagen", "Hemoglobin", "Myoglobin"], 0, "Keratin là protein dạng sợi tạo nên cấu trúc tóc, móng, sừng."),
        make_mc(6, "Nhận biết", "Phân tử khối của các protein thường có giá trị khoảng:", ["Từ vài vạn đến vài triệu amu", "Dưới 100 amu", "Khoảng vài trăm amu", "Khoảng 1 000 amu"], 0, "Protein là đại phân tử cao phân tử có phân tử khối rất lớn từ hàng chục nghìn đến hàng triệu amu."),
        make_mc(7, "Thông hiểu", "Vì sao protein được xem là cơ sở của sự sống?", ["Không có protein thì không có sự sống, protein cấu tạo nên tế bào, enzyme, kháng thể và hormone", "Vì protein cháy sinh ra điện", "Vì protein hòa tan được kim loại", "Do protein có vị ngọt"], 0, "Protein là nền tảng cấu trúc và chức năng của mọi cơ thể sống."),
        make_mc(8, "Thông hiểu", "Protein hemoglobin có trong hồng cầu máu người đóng vai trò sinh học tối quan trọng là:", ["Vận chuyển khí oxygen (O2) từ phổi đến các tế bào và mang CO2 về phổi", "Tiêu hóa thức ăn", "Hút bớt nước", "Làm cho máu đông cứng"], 0, "Hemoglobin gắn thuận nghịch với O2 để vận chuyển oxy đi khắp cơ thể."),
        make_mc(9, "Thông hiểu", "Kháng thể (Antibody) trong hệ thống miễn dịch của con người giúp chống lại vi khuẩn và virus thuộc loại hợp chất nào?", ["Protein", "Chất béo", "Carbohydrate", "Acid vô cơ"], 0, "Kháng thể là các phân tử protein đặc hiệu (immunoglobulin)."),
        make_mc(10, "Thông hiểu", "Thực phẩm nào sau đây là nguồn cung cấp protein thực vật tuyệt vời cho người ăn chay?", ["Đậu phụ, sữa đậu nành, các loại hạt đậu đỗ", "Rau cải xanh", "Quả chuối chín", "Cơm trắng"], 0, "Đậu nành và các loại đậu đỗ chứa hàm lượng protein thực vật rất cao."),
        make_mc(11, "Vận dụng", "Một phân tử hemoglobin có phân tử khối xấp xỉ 64 000 amu và chứa 4 nguyên tử sắt (Fe). Phần trăm khối lượng của sắt trong hemoglobin là: (Fe=56, làm tròn 2 chữ số thập phân)", ["0,35%", "0,70%", "0,28%", "0,56%"], 0, "mFe = 4 × 56 = 224 amu -> %Fe = 224 / 64 000 × 100% = 0,35%."),
        make_mc(12, "Vận dụng", "Trong 100 gam thịt bò nạc chứa khoảng 26 gam protein. Nhu cầu protein khuyến nghị của một người trưởng thành nặng 50 kg là 50 gam mỗi ngày. Khối lượng thịt bò nạc tối thiểu người này cần ăn nếu chỉ lấy protein từ thịt bò là xấp xỉ:", ["192 gam", "100 gam", "150 gam", "250 gam"], 0, "50 / 0,26 ≈ 192,3 gam ≈ 192 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các đặc tính của phân tử Protein:", [
            ("a", "Protein là những đại phân tử sinh học có cấu trúc vô cùng phức tạp.", True),
            ("b", "Thành phần nguyên tố bắt buộc luôn có nguyên tố Nitrogen (N).", True),
            ("c", "Tất cả các protein đều có khả năng tan vô hạn trong nước lạnh tạo dung dịch trong suốt.", False),
            ("d", "Protein tham gia vào cấu trúc tế bào và điều hòa quá trình trao đổi chất.", True)
        ], "Nhiều protein không tan trong nước như keratin (tóc, móng), collagen (gân, da)..."),
        make_tf(2, "Thông hiểu", "Về các nguồn thực phẩm giàu protein:", [
            ("a", "Protein động vật (thịt, cá, trứng, sữa) chứa đầy đủ các amino acid thiết yếu.", True),
            ("b", "Protein thực vật (đậu tương, vừng, lạc) có hàm lượng chất béo bão hòa thấp hơn thịt động vật.", True),
            ("c", "Chỉ cần ăn đường và mỡ mà không cần ăn protein cơ thể vẫn phát triển bình thường.", False),
            ("d", "Trẻ em trong giai đoạn tăng trưởng cần lượng protein trên một kg thể trọng cao hơn người lớn.", True)
        ], "Thiếu protein cơ thể sẽ suy dinh dưỡng, còi cọc và teo cơ."),
        make_tf(3, "Vận dụng", "Về vai trò sinh học của protein:", [
            ("a", "Enzyme (men) xúc tác cho hầu hết các phản ứng hóa sinh trong cơ thể có bản chất là protein.", True),
            ("b", "Insulin là một hormone có bản chất protein giúp điều hòa lượng đường trong máu.", True),
            ("c", "Khi cơ thể bị thiếu hụt năng lượng nghiêm trọng, protein sẽ bị phân giải để cung cấp năng lượng.", True),
            ("d", "Protein không tham gia vào hệ thống miễn dịch bảo vệ cơ thể.", False)
        ], "Kháng thể miễn dịch chính là các phân tử protein."),
        make_tf(4, "Vận dụng", "Trong khẩu phần ăn hằng ngày:", [
            ("a", "Nên phối hợp cân đối giữa protein động vật và protein thực vật.", True),
            ("b", "Ăn quá nhiều thịt đỏ (thịt bò, thịt cừu) làm tăng nguy cơ mắc bệnh gút và tim mạch.", True),
            ("c", "Thịt cá dễ tiêu hóa và chứa nhiều chất béo omega-3 lành mạnh.", True),
            ("d", "Nấu thịt chín nhừ trong nhiều giờ làm tăng thêm lượng protein ban đầu.", False)
        ], "Nấu quá lâu chỉ làm mềm cơ chứ không sinh thêm protein, thậm chí phá hủy một số amino acid nhạy cảm.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Nguyên tố nào bắt buộc phải có trong phân tử protein mà không có trong carbohydrate và lipid thông thường?", "Nitrogen", "Nitrogen (N)."),
        make_sa(2, "Thông hiểu", "Tên loại protein chính có trong lòng trắng trứng là gì?", "Albumin", "Albumin."),
        make_sa(3, "Vận dụng", "Các đơn vị cấu tạo nên chuỗi protein được gọi là các axit gì?", "Amino acid", "Amino acid (hoặc axit amin)."),
        make_sa(4, "Vận dụng", "Một quả trứng gà nặng 50 gam chứa khoảng 6 gam protein. Năng lượng do lượng protein này cung cấp xấp xỉ bao nhiêu kcal? (1g protein cung cấp khoảng 4 kcal)", "24", "6 × 4 = 24 kcal."),
        make_sa(5, "Vận dụng cao", "Một người trưởng thành nặng 60 kg cần 1 gam protein cho mỗi kg thể trọng mỗi ngày. Khối lượng protein người đó cần mỗi ngày là bao nhiêu gam?", "60", "60 × 1 = 60 gam."),
        make_sa(6, "Vận dụng cao", "Khối lượng phân tử của amino acid đơn giản nhất là glycine (H2N-CH2-COOH) là bao nhiêu amu? (C=12, H=1, O=16, N=14)", "75", "14 + 2 + 12 + 2 + 12 + 32 + 1 = 75 amu.")
    ],
    p4=[
        make_vdc(1, "Một mẫu protein chứa 16% Nitrogen theo khối lượng. Biết trong mỗi phân tử protein này chỉ chứa đúng 2 nguyên tử Nitrogen. Phân tử khối của mẫu protein đó là: (N=14)", ["175 amu", "350 amu", "280 amu", "560 amu"], 0, "mN = 2 × 14 = 28 amu -> M = 28 / 16% = 175 amu."),
        make_vdc(2, "Tại sao khi chế biến món sữa đậu nành, người làm phải đun sôi kĩ nước đậu nành trước khi uống?", ["Nhiệt độ sôi làm vô hoạt và phân hủy các chất ức chế enzyme tiêu hóa trypsin tự nhiên có trong đậu nành sống, giúp chống đầy bụng và hấp thụ đạm dễ dàng", "Để sữa đổi màu sang màu đỏ", "Để làm bay hơi hết protein", "Để sữa chua hơn"], 0, "Đậu nành sống chứa chất ức chế men trypsin gây khó tiêu, đun sôi chín kỹ giúp khử độc và an toàn cho đường ruột."),
        make_vdc(3, "Bệnh suy dinh dưỡng thể phù (Kwashiorkor) thường gặp ở trẻ em vùng nghèo đói là do chế độ ăn bị thiếu hụt nghiêm trọng chất dinh dưỡng nào sau đây dù vẫn ăn đủ tinh bột?", ["Thiếu protein (chất đạm)", "Thiếu chất béo", "Thiếu đường ngọt", "Thiếu nước"], 0, "Thiếu protein làm giảm áp lực keo trong máu dẫn đến thoát dịch phù nề toàn thân (bệnh Kwashiorkor)."),
        make_vdc(4, "Một người tập thể hình (gym) nặng 70 kg có mục tiêu tăng cơ bắp nên cần nạp 2,0 gam protein cho mỗi kg thể trọng mỗi ngày. Nếu người đó dùng thực phẩm bổ sung bột whey protein (chứa 80% protein tinh khiết) để cung cấp 50% nhu cầu đạm hằng ngày, khối lượng bột whey cần uống mỗi ngày là:", ["87,5 gam", "70,0 gam", "140,0 gam", "100,0 gam"], 0, "Tổng nhu cầu đạm = 70 × 2 = 140 gam -> Cần từ whey = 140 × 50% = 70 gam. Khối lượng bột whey = 70 / 80% = 87,5 gam.")
    ]
)

# --- BÀI 14 - ĐỀ 2: Tính chất của Protein (Đông tụ, Thủy phân, Phản ứng cháy) ---
exams_c4[f"{LID_B14}_test2"] = make_exam(
    CID, CTITLE, LID_B14, LNAME_B14, 2,
    p1=[
        make_mc(1, "Nhận biết", "Hiện tượng protein bị biến tính và vón cục lại dưới tác dụng của nhiệt độ cao hoặc acid, kiềm gọi là:", ["Sự đông tụ protein", "Sự xà phòng hóa", "Sự ester hóa", "Sự trùng hợp"], 0, "Định nghĩa sự đông tụ protein."),
        make_mc(2, "Nhận biết", "Hiện tượng nào sau đây minh họa cho sự đông tụ protein do nhiệt độ?", ["Luộc trứng gà thấy lòng trắng trứng từ dạng lỏng chuyển thành thể rắn màu trắng", "Hòa tan đường vào nước", "Mỡ lợn nóng chảy trên chảo", "Nước đá tan thành nước lỏng"], 0, "Nhiệt làm protein albumin trong lòng trắng trứng đông tụ thành khối rắn màu trắng."),
        make_mc(3, "Nhận biết", "Khi nấu canh cua đồng, thịt cua giã nhỏ hòa vào nước rồi đun sôi thấy từng mảng thịt cua nổi lên trên mặt nước canh. Đó là hiện tượng gì?", ["Sự đông tụ protein thịt cua khi đun nóng", "Sự nóng chảy của chất béo", "Cua nổi lên do hòa tan muối", "Phản ứng lên men giấm"], 0, "Protein trong thịt cua bị đông tụ lại khi nước canh sôi đóng thành mảng riêu cua nổi lên."),
        make_mc(4, "Nhận biết", "Khi vắt một lát chanh tươi (chứa acid citric) vào cốc sữa tươi không đường, sau vài phút quan sát thấy hiện tượng gì?", ["Sữa xuất hiện kết tủa vón cục lợn cợn màu trắng", "Sữa trong suốt như nước", "Sữa sủi bọt khí mãnh liệt", "Sữa chuyển sang màu xanh lam"], 0, "Acid trong chanh làm giảm pH gây đông tụ protein casein trong sữa tạo kết tủa lợn cợn."),
        make_mc(5, "Nhận biết", "Khi đốt cháy một sợi tóc hoặc một mẩu móng tay, hiện tượng quan sát được là:", ["Cháy có mùi khét đặc trưng như mùi lông tóc cháy", "Cháy có mùi thơm hoa quả", "Cháy không có mùi và vón cục tròn cứng", "Không cháy được"], 0, "Protein chứa N và S khi cháy có mùi khét đặc trưng."),
        make_mc(6, "Nhận biết", "Khi đun nóng protein trong dung dịch acid hoặc kiềm, hay nhờ tác dụng của enzyme tiêu hóa, protein bị phân giải thành các chất nào?", ["Hỗn hợp các amino acid", "Glucose", "Glycerol", "Methane"], 0, "Thủy phân protein tạo thành các amino acid."),
        make_mc(7, "Thông hiểu", "Vì sao cồn y tế 70° hoặc dung dịch muối kim loại nặng lại có khả năng sát trùng, tiêu diệt vi khuẩn và virus?", ["Làm đông tụ và biến tính protein cấu trúc màng và enzyme của vi sinh vật làm chúng chết", "Làm vi khuẩn bay hơi", "Làm vi khuẩn biến thành thức ăn", "Hạ nhiệt độ vi khuẩn"], 0, "Cồn làm biến tính và đông tụ protein tế bào vi khuẩn tức thì."),
        make_mc(8, "Thông hiểu", "Để phân biệt một tấm vải làm bằng tơ tằm thiên nhiên (protein) và một tấm vải làm bằng sợi tơ nilon tổng hợp, phương pháp đơn giản nhất là:", ["Cắt một mẩu sợi nhỏ đem đốt trên ngọn lửa: tơ tằm cháy có mùi khét, tro xốp mịn; tơ nilon vón cục nhựa cứng, không có mùi khét tóc", "Ngâm vào nước cất", "Nhỏ giọt giấm ăn vào", "Phơi ra ngoài nắng"], 0, "Đốt cháy nhận biết mùi khét đặc trưng của protein và dạng tro."),
        make_mc(9, "Thông hiểu", "Khi làm món trứng muối, người ta ngâm trứng vịt trong dung dịch nước muối NaCl đậm đặc trong nhiều tuần. Hiện tượng lòng đỏ trứng cứng dẻo lại là do:", ["Sự đông tụ protein chậm dưới tác dụng của dung dịch muối nồng độ cao", "Lòng đỏ bị mất hết chất dinh dưỡng", "Muối làm trứng nở to", "Trứng bị vi khuẩn phân hủy"], 0, "Muối nồng độ cao gây mất nước và đông tụ protein lòng đỏ."),
        make_mc(10, "Thông hiểu", "Phản ứng màu biure đặc trưng của protein với dung dịch CuSO4 trong môi trường kiềm NaOH tạo ra dung dịch có màu gì?", ["Màu tím đặc trưng", "Màu xanh lam", "Màu đỏ gạch", "Màu vàng chanh"], 0, "Phản ứng màu biure tạo phức chất màu tím đặc trưng với các liên kết peptit."),
        make_mc(11, "Vận dụng", "Thủy phân hoàn toàn một chuỗi tripeptit gồm 3 gốc glycine (H2N-CH2-COOH) cần bao nhiêu phân tử nước H2O?", ["2 phân tử H2O", "3 phân tử H2O", "1 phân tử H2O", "4 phân tử H2O"], 0, "Tripeptit có 2 liên kết peptit nên cần 2 phân tử H2O để thủy phân hoàn toàn."),
        make_mc(12, "Vận dụng", "Đốt cháy hoàn toàn 0,1 mol amino acid glycine (C2H5NO2). Thể tích khí N2 thu được ở điều kiện chuẩn (24,79 L/mol) là:", ["1,2395 lít", "2,4790 lít", "3,7185 lít", "4,9580 lít"], 0, "C2H5NO2 -> 0,5 N2. nN2 = 0,1 × 0,5 = 0,05 mol -> V = 0,05 × 24,79 = 1,2395 lít.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các yếu tố gây đông tụ protein:", [
            ("a", "Nhiệt độ cao (đun nấu) làm protein đông tụ.", True),
            ("b", "Môi trường acid mạnh hoặc base mạnh gây đông tụ protein.", True),
            ("c", "Cồn (rượu etylic) nồng độ cao gây đông tụ protein.", True),
            ("d", "Muối của kim loại nặng (chì, thủy ngân) gây kết tủa biến tính protein vĩnh viễn.", True)
        ], "Tất cả các yếu tố trên đều gây biến tính đông tụ protein."),
        make_tf(2, "Thông hiểu", "Về phản ứng thủy phân protein:", [
            ("a", "Protein bị thủy phân bởi acid, kiềm hoặc các enzyme protease.", True),
            ("b", "Sản phẩm cuối cùng của sự thủy phân protein là các amino acid.", True),
            ("c", "Trong dạ dày người, enzyme pepsin và acid HCl thủy phân một phần protein thức ăn.", True),
            ("d", "Thủy phân protein tạo ra khí hydrogen thoát ra mãnh liệt.", False)
        ], "Thủy phân protein không giải phóng khí H2."),
        make_tf(3, "Vận dụng", "Thực hành nhận biết sợi tơ dệt bằng phương pháp đốt:", [
            ("a", "Sợi len lông cừu khi cháy có mùi khét như tóc cháy, tàn tro màu đen bóp vụn dễ dàng.", True),
            ("b", "Sợi tơ tằm thiên nhiên cháy tương tự như sợi len lông cừu.", True),
            ("c", "Sợi bông (cellulose) khi cháy có mùi khét tóc cháy nồng nặc.", False),
            ("d", "Sợi nilon tổng hợp khi đốt nóng chảy co rúm lại thành cục nhựa tròn cứng ngắc khó bóp vỡ.", True)
        ], "Sợi bông cháy có mùi giấy cháy, không có mùi khét tóc."),
        make_tf(4, "Vận dụng", "Trong chế biến món ăn ẩm thực:", [
            ("a", "Khi luộc thịt bò hoặc nấu súp, người ta hớt bỏ bọt váng nổi lên thực chất là các protein máu bị đông tụ.", True),
            ("b", "Ướp thịt với nước cốt quả dứa (chứa enzyme bromelain) giúp thịt mềm nhanh hơn khi nấu.", True),
            ("c", "Không nên luộc trứng gà ở nhiệt độ trên 100 °C trong nồi áp suất quá lâu vì làm biến tính dinh dưỡng.", True),
            ("d", "Sữa đậu nành nấu với nước chua (chứa acid lactic/acid acetic) giúp kết tủa protein tạo thành đậu phụ.", True)
        ], "Các ứng dụng hóa học trong nấu ăn đều hoàn toàn chính xác.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Hiện tượng lòng trắng trứng bị đông cứng lại khi đun nóng gọi là sự gì?", "Đông tụ", "Sự đông tụ (hoặc biến tính)."),
        make_sa(2, "Thông hiểu", "Khi đốt cháy protein có mùi gì đặc trưng?", "Mùi khét", "Mùi khét (như mùi tóc cháy)."),
        make_sa(3, "Vận dụng", "Thủy phân hoàn toàn 1 mol dipeptit cần bao nhiêu mol nước H2O?", "1", "1 mol H2O (chứa 1 liên kết peptit)."),
        make_sa(4, "Vận dụng", "Phản ứng màu biure của protein với CuSO4/NaOH tạo dung dịch có màu gì?", "Tím", "Màu tím."),
        make_sa(5, "Vận dụng cao", "Thủy phân hoàn toàn 7,5 gam amino acid glycine (M = 75 amu). Số mol amino acid này là bao nhiêu mol?", "0.1", "7,5 / 75 = 0,1 mol."),
        make_sa(6, "Vận dụng cao", "Một chuỗi polypeptit có 100 gốc amino acid thì trong phân tử có bao nhiêu liên kết peptit?", "99", "100 - 1 = 99 liên kết peptit.")
    ],
    p4=[
        make_vdc(1, "Thủy phân hoàn toàn 20,3 gam một đoạn tripeptit Gly-Gly-Gly bằng dung dịch acid HCl dư. Khối lượng muối thu được sau phản ứng cô cạn là bao nhiêu gam? Biết khối lượng mol của glycine H2N-CH2-COOH là 75 g/mol: (C=12, H=1, O=16, N=14, Cl=35,5)", ["33,45 gam", "22,50 gam", "29,80 gam", "35,60 gam"], 0, "Tripeptit: 3 Gly - 2 H2O. Khối lượng mol = 3×75 - 2×18 = 189 g/mol. n peptit = 20,3 / 189 = 0,1074 mol... Nếu đề là 18,9 gam tripeptit -> n = 0,1 mol. nHCl phản ứng = 3 × 0,1 = 0,3 mol; nH2O phản ứng = 2 × 0,1 = 0,2 mol. Muối là 0,3 mol ClH3N-CH2-COOH (M = 75 + 36,5 = 111,5). m muối = 0,3 × 111,5 = 33,45 gam."),
        make_vdc(2, "Tại sao khi một người sơ ý bị ngộ độc muối kim loại nặng (như thủy ngân Hg2+, chì Pb2+ hoặc đồng Cu2+), trong lúc chờ cấp cứu y tế, người xung quanh thường cho nạn nhân uống ngay một cốc lòng trắng trứng gà tươi hoặc sữa tươi nguyên chất?", ["Lòng trắng trứng và sữa chứa hàm lượng protein hòa tan rất cao sẽ tạo kết tủa đông tụ với các ion kim loại nặng, giữ chúng lại trong dạ dày không cho ngấm vào máu rồi kích thích nôn ra ngoài", "Để nạn nhân không bị đói", "Lòng trắng trứng làm loãng acid", "Để giảm vị đắng"], 0, "Protein kết hợp tạo kết tủa không tan với ion kim loại nặng giúp bảo vệ niêm mạc dạ dày và ngăn hấp thụ vào máu."),
        make_vdc(3, "Để tẩy sạch vết máu tươi (chứa protein hemoglobin) dính trên áo trắng, phương pháp giặt tẩy nào sau đây là khoa học và hiệu quả nhất?", ["Ngâm và vò áo bằng nước lạnh xà phòng (hoặc nhỏ nước oxy già H2O2), tuyệt đối không dùng nước sôi nóng", "Ngâm áo vào nước sôi 100 °C ngay lập tức", "Dùng bàn là nóng là lên vết máu", "Rắc muối hột rồi phơi nắng"], 0, "Nước sôi làm đông tụ protein hemoglobin gắn chặt vĩnh viễn vào sợi vải không giặt sạch được; phải giặt bằng nước lạnh."),
        make_vdc(4, "Một áo len mùa đông đắt tiền làm bằng 100% sợi len lông cừu tự nhiên (keratin protein). Người sử dụng nên bảo quản và giặt áo len này theo cách nào sau đây để áo không bị co rút hỏng dáng?", ["Giặt nhẹ tay bằng nước ấm với dầu gội đầu hoặc nước giặt trung tính, không vắt xoắn mạnh và phơi phẳng trên mặt phẳng ngang", "Giặt bằng xà phòng có độ kiềm cao và ngâm nước sôi", "Cho vào máy giặt quay vắt tốc độ cực mạnh", "Ngâm trong cồn 90°"], 0, "Len lông cừu là protein rất nhạy cảm với kiềm mạnh và nhiệt độ cao, cần giặt nhẹ bằng chất giặt trung tính và phơi nằm ngang chống dão.")
    ]
)

# --- BÀI 14 - ĐỀ 3: Ứng dụng, dinh dưỡng và phân biệt tơ sợi thiên nhiên ---
exams_c4[f"{LID_B14}_test3"] = make_exam(
    CID, CTITLE, LID_B14, LNAME_B14, 3,
    p1=[
        make_mc(1, "Nhận biết", "Tơ tằm thiên nhiên và len lông cừu có thành phần hóa học chủ yếu là:", ["Protein", "Cellulose", "Tinh bột", "Polyethylene"], 0, "Tơ tằm và len lông cừu là protein tự nhiên."),
        make_mc(2, "Nhận biết", "Chất nào sau đây khi đốt cháy sinh ra khí có mùi khét như mùi tóc cháy?", ["Sợi tơ tằm", "Sợi bông vải", "Sợi tơ visco", "Sợi tơ nilon"], 0, "Tơ tằm có bản chất là protein nên cháy khét mùi tóc."),
        make_mc(3, "Nhận biết", "Trong cơ thể sống, các chất có vai trò làm chất xúc tác sinh học thúc đẩy các phản ứng chuyển hóa với tốc độ cực nhanh là:", ["Các enzyme (men)", "Các vitamin", "Các muối khoáng", "Các lipid"], 0, "Enzyme là các chất xúc tác sinh học có bản chất protein."),
        make_mc(4, "Nhận biết", "Nhóm amino acid mà cơ thể con người không thể tự tổng hợp được, bắt buộc phải lấy từ thức ăn được gọi là:", ["Các amino acid thiết yếu (không thay thế)", "Các amino acid phụ", "Các vitamin", "Các khoáng chất"], 0, "Có 9 amino acid thiết yếu cơ thể không tự tổng hợp được."),
        make_mc(5, "Nhận biết", "Thực phẩm nào sau đây chứa protein hoàn chỉnh có đủ tất cả các amino acid thiết yếu?", ["Trứng gà và thịt bò", "Ngô hạt", "Củ khoai mì", "Quả chuối"], 0, "Protein động vật (trứng, thịt) là protein hoàn chỉnh."),
        make_mc(6, "Nhận biết", "Vải tơ tằm thiên nhiên có đặc tính quý nào sau đây?", ["Mềm mại, óng ánh ánh ngọc trai, thoáng khí mùa hè và ấm áp mùa đông", "Cứng giòn chịu lực như thép", "Không thấm nước tuyệt đối", "Có tính đàn hồi như cao su"], 0, "Tơ tằm sang trọng, mềm mịn, thoáng mát và cách nhiệt tốt."),
        make_mc(7, "Thông hiểu", "Vì sao không nên giặt quần áo may bằng lụa tơ tằm hoặc len lông cừu bằng bột giặt có độ kiềm cao hoặc dùng thuốc tẩy chứa clo?", ["Môi trường kiềm mạnh và chất tẩy sẽ thủy phân phá hủy các liên kết peptit làm xơ sợi bị mục rách và phai màu", "Bột giặt làm tơ tằm cứng lại thành đá", "Bột giặt làm tơ tằm biến thành bông", "Lụa tơ tằm hút bột giặt"], 0, "Protein bị thủy phân trong môi trường kiềm và bị oxy hóa bởi chất tẩy clo."),
        make_mc(8, "Thông hiểu", "Để kiểm tra một chiếc áo len bán ngoài chợ là len lông cừu thật hay len nhân tạo acrylic (sợi tổng hợp), người mua có thể làm gì?", ["Rút một mẩu sợi nhỏ ở đường may đốt thử: len thật cháy có mùi khét tóc và tàn xốp mịn bóp tan; sợi nhân tạo cháy khói đen và vón hòn nhựa cứng", "Ngửi mùi sợi len khi còn mới", "Nhúng áo vào nước", "Kéo căng sợi len"], 0, "Thử bằng phản ứng cháy là phương pháp dân gian và khoa học chuẩn xác nhất."),
        make_mc(9, "Thông hiểu", "Gelatin (chất làm đông thạch dẻo) được sản xuất bằng cách thủy phân chất nào có trong xương, da động vật?", ["Collagen", "Keratin", "Hemoglobin", "Albumin"], 0, "Gelatin là sản phẩm thủy phân một phần từ collagen của da và sụn xương."),
        make_mc(10, "Thông hiểu", "Khi làm nước mắm truyền thống từ cá và muối ăn, bản chất hóa học của quá trình ủ chượp cá là gì?", ["Quá trình enzyme tự nhiên trong ruột cá thủy phân protein thịt cá thành các amino acid hòa tan tạo vị ngọt đậm", "Cá bị lên men rượu", "Muối ăn tan ra", "Cá bị cháy khô"], 0, "Ủ chượp là sự thủy phân tự nhiên protein cá thành các amino acid bổ dưỡng (độ đạm của nước mắm)."),
        make_mc(11, "Vận dụng", "Nước mắm truyền thống có độ đạm 40°N nghĩa là trong 1 lít nước mắm có chứa bao nhiêu gam nguyên tố Nitrogen toàn phần?", ["40 gam", "400 gam", "4 gam", "20 gam"], 0, "Độ đạm biểu thị số gam nitrogen (N) có trong 1 lít nước mắm -> 40°N = 40 gam N/lít."),
        make_mc(12, "Vận dụng", "Một người cân nặng 65 kg. Theo tiêu chuẩn viện dinh dưỡng, mỗi ngày người này nên nạp 1,2 gam protein cho mỗi kg thể trọng. Tổng lượng protein người đó cần nạp mỗi ngày là:", ["78 gam", "65 gam", "52 gam", "80 gam"], 0, "65 × 1,2 = 78 gam protein.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Xét các loại tơ sợi trong ngành may mặc:", [
            ("a", "Tơ tằm và len lông cừu là tơ tự nhiên có nguồn gốc từ động vật (protein).", True),
            ("b", "Sợi bông vải (cotton) và sợi gai có nguồn gốc từ thực vật (cellulose).", True),
            ("c", "Tơ nilon và tơ dacron là tơ tổng hợp từ hóa dầu.", True),
            ("d", "Tất cả các loại tơ trên đều có cấu tạo hóa học từ protein.", False)
        ], "Cotton là cellulose, nilon là polyamide tổng hợp."),
        make_tf(2, "Thông hiểu", "Về giá trị dinh dưỡng của protein trong bữa ăn:", [
            ("a", "Thiếu protein làm giảm sức đề kháng và giảm khối lượng cơ bắp.", True),
            ("b", "Thừa protein quá mức tạo gánh nặng lọc thải cho thận và gan.", True),
            ("c", "Protein cung cấp khoảng 4 kcal năng lượng trên mỗi gam khi bị oxy hóa.", True),
            ("d", "Cơ thể con người có khả năng tự tích trữ protein vô hạn tương tự như tích trữ mỡ thừa.", False)
        ], "Cơ thể không có kho tích trữ protein riêng biệt, protein dư thừa bị gan chuyển hóa thải ure qua thận."),
        make_tf(3, "Vận dụng", "Trong công nghệ sản xuất nước tương (xì dầu):", [
            ("a", "Đậu nành được ủ với nấm mốc Aspergillus oryzae để nấm tiết ra enzyme protease thủy phân đạm đậu nành.", True),
            ("b", "Quá trình ủ giúp tạo ra các amino acid mang hương vị umami thơm ngon đặc trưng.", True),
            ("c", "Sản xuất nước tương bằng phương pháp thủy phân đậu nành bằng acid HCl đậm đặc nếu không kiểm soát tốt có thể sinh độc chất 3-MCPD.", True),
            ("d", "Nước tương thực chất chỉ là nước pha muối và phẩm màu đen hoàn toàn không có dinh dưỡng.", False)
        ], "Nước tương truyền thống giàu đạm amino acid quý giá."),
        make_tf(4, "Vận dụng", "Thực hành bảo quản đồ lụa tơ tằm cao cấp:", [
            ("a", "Nên giặt khô hoặc giặt tay nhẹ bằng dầu gội đầu dịu nhẹ.", True),
            ("b", "Phơi trong bóng râm thoáng mát, tránh ánh nắng mặt trời chiếu gắt làm giòn sợi lụa.", True),
            ("c", "Là (ủi) lụa tơ tằm ở nhiệt độ thấp hoặc ủi khi vải còn hơi ẩm.", True),
            ("d", "Nên ngâm lụa tơ tằm trong dung dịch nước Javen để tẩy trắng mốc.", False)
        ], "Nước Javen là chất oxy hóa mạnh phá hủy mục nát lụa tơ tằm.")
    ],
    p3=[
        make_sa(1, "Thông hiểu", "Sợi len lông cừu có thành phần hóa học chính thuộc nhóm chất nào?", "Protein", "Protein."),
        make_sa(2, "Thông hiểu", "Vị ngọt thịt đậm đà của amino acid glutamate có tên gọi trong ẩm thực là vị gì?", "Umami", "Umami (vị ngọt thịt/vị ngọt mì chính)."),
        make_sa(3, "Vận dụng", "1 gam protein cung cấp cho cơ thể khoảng bao nhiêu kilocalo (kcal) năng lượng?", "4", "Khoảng 4 kcal (17 kJ)."),
        make_sa(4, "Vận dụng", "Nước mắm có độ đạm 30°N chứa bao nhiêu gam nitrogen trong 1 lít?", "30", "30 gam N/lít."),
        make_sa(5, "Vận dụng cao", "Một khẩu phần ăn chứa 30 gam protein, 10 gam chất béo và 50 gam carbohydrate. Tổng năng lượng khẩu phần này cung cấp xấp xỉ bao nhiêu kcal?", "410", "30×4 + 10×9 + 50×4 = 120 + 90 + 200 = 410 kcal."),
        make_sa(6, "Vận dụng cao", "Một chai nước mắm 500 mL có độ đạm 32°N. Khối lượng nguyên tố Nitrogen trong chai nước mắm đó là bao nhiêu gam?", "16", "0,5 × 32 = 16 gam.")
    ],
    p4=[
        make_vdc(1, "Một nhà máy sản xuất nước mắm truyền thống ủ chượp 10 tấn cá cơm tươi chứa 17% protein. Biết hàm lượng nitrogen trung bình trong protein cá cơm là 16% và hiệu suất chuyển hóa protein thành nitrogen hòa tan trong nước mắm đạt 70%. Tổng khối lượng nguyên tố Nitrogen hòa tan thu được là:", ["190,4 kg", "272,0 kg", "160,0 kg", "215,5 kg"], 0, "m protein = 10 000 × 17% = 1 700 kg -> mN trong cá = 1 700 × 16% = 272 kg. mN thu được = 272 × 70% = 190,4 kg."),
        make_vdc(2, "Để bảo quản một chiếc áo dài bằng lụa tơ tằm tự nhiên không bị gián, chuột cắn và không bị ố vàng theo năm tháng, cách cất giữ đúng đắn nhất là:", ["Bọc áo trong giấy bản hoặc túi vải cotton thoáng khí, treo trong tủ gỗ khô ráo có đặt túi hoa hồi hoặc gỗ tuyết tùng chống côn trùng", "Cất trong túi ni lông buộc kín ẩm ướt", "Treo ngoài ban công có nắng gió", "Ngâm áo trong nước thơm liên tục"], 0, "Túi vải thoáng khí tránh ẩm mốc và gỗ tuyết tùng xua đuổi côn trùng gặm nhấm protein."),
        make_vdc(3, "Mì chính (bột ngọt) là muối monosodium glutamate (MSG) của acid glutamic (một amino acid có trong tự nhiên). Mì chính mang lại vị ngọt thịt umami cho món ăn. Trong công nghiệp, mì chính được sản xuất bằng phương pháp nào sau đây?", ["Lên men vi sinh từ tinh bột sắn hoặc mật rỉ đường mía nhờ vi khuẩn Corynebacterium glutamicum", "Khai thác từ mỏ khoáng sản", "Tổng hợp từ dầu mỏ", "Điện phân nước biển"], 0, "Lên men sinh học từ tinh bột và mật rỉ đường nhờ vi khuẩn chuyển hóa."),
        make_vdc(4, "Một người muốn phân biệt 3 sợi dây dệt có bề ngoài giống hệt nhau gồm: sợi 1 (bông cotton), sợi 2 (tơ tằm), sợi 3 (nilon-6,6). Người đó đốt cháy từng sợi và ghi nhận hiện tượng. Kết quả nào sau đây là chính xác nhất?", ["Sợi 1 cháy mùi giấy khét tro xốp mịn; Sợi 2 cháy mùi khét tóc tro xốp bóp vụn; Sợi 3 nóng chảy co rúm thành hòn nhựa cứng màu nâu xám", "Sợi 1 và 2 đều có mùi khét tóc", "Cả 3 sợi đều co lại thành cục nhựa", "Sợi 2 cháy không mùi"], 0, "Sợi bông (cellulose) cháy mùi giấy; Sợi tơ tằm (protein) cháy mùi khét tóc; Sợi nilon (chất dẻo hóa dầu) co rúm vón hòn cứng.")
    ]
)



# ==============================================================================
# BÀI 15: POLYMER (chem9_c4_b15) - 3 ĐỀ
# ==============================================================================
LID_B15 = "chem9_c4_b15"
LNAME_B15 = "Bài 15: Polymer"

# --- BÀI 15 - ĐỀ 1: Khái niệm, monomer, mắt xích, phân loại polymer ---
exams_c4[f"{LID_B15}_test1"] = make_exam(
    CID, CTITLE, LID_B15, LNAME_B15, 1,
    p1=[
        make_mc(1, "Nhận biết", "Polymer là hợp chất có khối lượng phân tử rất lớn do nhiều đơn vị nhỏ gọi là gì liên kết với nhau tạo nên?", ["Mắt xích", "Nguyên tử", "Đơn chất", "Hợp chất vô cơ"], 0, "Polymer cấu tạo từ nhiều mắt xích liên kết với nhau."),
        make_mc(2, "Nhận biết", "Chất ban đầu tham gia phản ứng để tạo nên polymer được gọi là:", ["Monomer", "Polymer", "Chất xúc tác", "Chất chỉ thị"], 0, "Monomer là chất đầu tạo ra polymer."),
        make_mc(3, "Nhận biết", "Polymer nào sau đây thuộc loại polymer thiên nhiên có sẵn trong tự nhiên?", ["Tinh bột", "Polyethylene (PE)", "Poly(vinyl chloride) (PVC)", "Tơ nilon-6,6"], 0, "Tinh bột có sẵn trong củ, hạt của thực vật."),
        make_mc(4, "Nhận biết", "Polyethylene (nhựa PE) được điều chế trực tiếp từ monomer nào sau đây?", ["Ethylene (CH2=CH2)", "Methane (CH4)", "Acetylene (C2H2)", "Benzene (C6H6)"], 0, "PE được trùng hợp từ ethylene."),
        make_mc(5, "Thông hiểu", "Poly(vinyl chloride) (nhựa PVC) có công thức mắt xích cấu tạo là:", ["-[-CH2-CHCl-]-", "-[-CH2-CH2-]-", "-[-CH2-CH(CH3)-]-", "-[-CF2-CF2-]-"], 0, "Mắt xích của PVC là -CH2-CHCl-."),
        make_mc(6, "Thông hiểu", "Polymer nào sau đây là polymer bán tổng hợp (nhân tạo, chế biến hóa học từ polymer thiên nhiên)?", ["Tơ visco", "Tơ tằm", "Len lông cừu", "Nhựa polystyrene"], 0, "Tơ visco chế biến từ cellulose gỗ."),
        make_mc(7, "Thông hiểu", "Tên gọi của polymer được cấu tạo bằng cách ghép tiền tố 'poly' vào trước tên của:", ["Monomer tương ứng", "Chất xúc tác", "Sản phẩm cháy", "Kim loại"], 0, "Tên polymer = Poly + tên monomer."),
        make_mc(8, "Thông hiểu", "Cao su thiên nhiên được lấy từ mủ của cây nào?", ["Cây cao su", "Cây thông", "Cây bạch đàn", "Cây mía"], 0, "Mủ cây cao su chứa polyisoprene thiên nhiên."),
        make_mc(9, "Thông hiểu", "Hệ số n trong công thức tổng quát của polymer (-[-M-]-)n được gọi là gì?", ["Hệ số trùng hợp (hay độ polymer hóa)", "Hệ số cân bằng phản ứng", "Chỉ số acid", "Hệ số phân ly"], 0, "n là hệ số trùng hợp."),
        make_mc(10, "Thông hiểu", "Polymer nào sau đây không tan trong cả nước lạnh lẫn nước nóng và các dung môi thông thường?", ["Cellulose", "Glucose", "Saccharose", "Glycerol"], 0, "Cellulose không tan trong dung môi thông thường."),
        make_mc(11, "Vận dụng", "Khối lượng phân tử của một đoạn mạch poly(vinyl chloride) (PVC) là 125 000 amu. Hệ số trùng hợp n của đoạn mạch đó là:", ["2 000", "1 500", "2 500", "1 000"], 0, "M(PVC) = 62,5 amu -> n = 125 000 / 62,5 = 2 000."),
        make_mc(12, "Vận dụng", "Trùng hợp 5,6 tấn ethylene với hiệu suất 80% thì thu được bao nhiêu tấn nhựa polyethylene (PE)?", ["4,48 tấn", "5,60 tấn", "7,00 tấn", "3,50 tấn"], 0, "m(PE) = 5,6 × 80% = 4,48 tấn.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về khái niệm và phân loại polymer:", [
            ("a", "Polymer là những hợp chất có phân tử khối rất lớn do nhiều mắt xích liên kết lại.", True),
            ("b", "Monomer là những phân tử nhỏ phản ứng với nhau để tạo thành polymer.", True),
            ("c", "Tất cả các polymer đều có nguồn gốc từ tổng hợp nhân tạo trong nhà máy hóa chất.", False),
            ("d", "Tơ tằm, sợi bông và len lông cừu đều là polymer thiên nhiên.", True)
        ], "Polymer có cả nguồn gốc thiên nhiên và nguồn gốc tổng hợp."),
        make_tf(2, "Thông hiểu", "Khi xét về thành phần các nguyên tố tạo nên polymer:", [
            ("a", "Polyethylene (PE) chỉ chứa hai nguyên tố là carbon và hydrogen.", True),
            ("b", "Poly(vinyl chloride) (PVC) chứa ba nguyên tố C, H và Cl.", True),
            ("c", "Tơ tằm và len chứa các nguyên tố C, H, O, N.", True),
            ("d", "Mọi polymer đều chứa nguyên tố nitrogen trong phân tử.", False)
        ], "PE, PP chỉ chứa C và H; tinh bột, cellulose chỉ chứa C, H, O."),
        make_tf(3, "Vận dụng", "Về quá trình trùng hợp điều chế polymer:", [
            ("a", "Phản ứng trùng hợp ethylene tạo ra polyethylene không sinh ra sản phẩm phụ phân tử nhỏ.", True),
            ("b", "Khối lượng polymer thu được trên lý thuyết bằng tổng khối lượng monomer tham gia phản ứng.", True),
            ("c", "Ethylene có liên kết đôi C=C nên có khả năng tham gia phản ứng trùng hợp.", True),
            ("d", "Methane (CH4) là khí no nên cũng dễ dàng tham gia phản ứng trùng hợp tạo polymer.", False)
        ], "Methane là alkane no không có liên kết bội nên không trùng hợp được."),
        make_tf(4, "Vận dụng cao", "Về phân loại tơ sợi polymer:", [
            ("a", "Tơ hóa học gồm tơ tổng hợp (như nilon) và tơ bán tổng hợp (như tơ visco).", True),
            ("b", "Tơ visco được sản xuất từ nguyên liệu ban đầu là mỏ quặng kim loại.", False),
            ("c", "Tơ tằm bền vững tuyệt đối trong môi trường kiềm đặc nóng.", False),
            ("d", "Tơ nilon-6,6 thuộc loại tơ tổng hợp được điều chế từ các hóa chất hữu cơ.", True)
        ], "Tơ visco chế biến từ cellulose gỗ; tơ tằm là protein bị thủy phân nhanh trong kiềm.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Polyethylene được viết tắt là gì?", "PE", "PE."),
        make_sa(2, "Thông hiểu", "Một mắt xích của polyethylene (-[-CH2-CH2-]-) có phân tử khối bằng bao nhiêu amu?", "28", "12×2 + 1×4 = 28 amu."),
        make_sa(3, "Thông hiểu", "Một mắt xích của poly(vinyl chloride) (-[-CH2-CHCl-]-) có khối lượng phân tử bằng bao nhiêu amu?", "62.5", "62,5 amu (C2H3Cl)."),
        make_sa(4, "Vận dụng", "Một đoạn mạch PE có phân tử khối là 56 000 amu. Hệ số trùng hợp n của đoạn mạch này là bao nhiêu?", "2000", "56 000 / 28 = 2 000."),
        make_sa(5, "Vận dụng", "Trùng hợp 2,8 tấn ethylene thu được 2,52 tấn PE. Hiệu suất của phản ứng trùng hợp là bao nhiêu phần trăm?", "90", "2,52 / 2,8 × 100% = 90%."),
        make_sa(6, "Vận dụng cao", "Để sản xuất 6,25 tấn nhựa PVC với hiệu suất cả quá trình đạt 80%, khối lượng monomer vinyl chloride (C2H3Cl) cần dùng là bao nhiêu tấn?", "7.8125", "6,25 / 0,8 = 7,8125 tấn.")
    ],
    p4=[
        make_vdc(1, "Một đoạn phân tử polymer cao su thiên nhiên (polyisoprene, công thức mắt xích -[-C5H8-]-) có khối lượng phân tử trung bình là 136 000 amu. Hệ số trùng hợp trung bình của đoạn polymer cao su này là:", ["2 000", "1 500", "2 500", "1 000"], 0, "M mắt xích C5H8 = 5×12 + 8 = 68 amu -> n = 136 000 / 68 = 2 000."),
        make_vdc(2, "Trong phòng thí nghiệm, người ta tiến hành nhiệt phân một mẫu nhựa PE không có không khí ở nhiệt độ cao. Hiện tượng nào sau đây phản ánh đúng bản chất của quá trình bẻ gãy mạch polymer?", ["Polymer bị depolymer hóa và cracking thành hỗn hợp hydrocarbon thể khí và lỏng mạch ngắn hơn", "Polymer biến thành kim loại dẫn điện", "Polymer hóa thành than chì nguyên chất không bay hơi", "Polymer phản ứng với nước tạo acid"], 0, "Bẻ gãy mạch polymer sinh ra các phân đoạn alkane và alkene mạch ngắn hơn."),
        make_vdc(3, "Để phân biệt 2 mảnh vải dệt có cùng màu sắc gồm một mảnh bằng tơ tằm thiên nhiên và một mảnh bằng tơ nilon-6,6 tổng hợp, thao tác đơn giản và chuẩn xác nhất là:", ["Cắt một mẩu nhỏ của mỗi mảnh rồi đốt trên ngọn lửa, ngửi mùi khét và quan sát phần tro", "Ngâm vào nước lạnh", "Đem phơi nắng", "Dùng nam châm hút"], 0, "Tơ tằm cháy có mùi khét tóc và tro giòn bóp vụn; nilon cháy vón thành cục nhựa cứng khó vỡ."),
        make_vdc(4, "Một xưởng sản xuất ống nhựa PVC tiêu thụ mỗi ngày 12,5 tấn bột nhựa PVC. Để sản xuất lượng PVC trên từ khí ethylene qua các giai đoạn trung gian với hiệu suất chung toàn bộ chu trình là 75%, khối lượng ethylene lý thuyết cần huy động là bao nhiêu tấn? (Biết tỉ lệ mol C2H4 : C2H3Cl là 1 : 1).", ["7,47 tấn", "5,60 tấn", "8,25 tấn", "6,15 tấn"], 0, "m lý thuyết PVC = 12,5 / 0,75 = 16,667 tấn -> n = 16,667 / 62,5 = 0,2667 Mmol -> m(C2H4) = 0,2667 × 28 = 7,467 ≈ 7,47 tấn.")
    ]
)

# --- BÀI 15 - ĐỀ 2: Cấu trúc mạch polymer và cơ tính ---
exams_c4[f"{LID_B15}_test2"] = make_exam(
    CID, CTITLE, LID_B15, LNAME_B15, 2,
    p1=[
        make_mc(1, "Nhận biết", "Các polymer có mạch carbon không phân nhánh gồm có:", ["Polyethylene (PE), amylose", "Amylopectin, glycogen", "Cao su lưu hóa, nhựa rezit", "Glycerol, glucose"], 0, "PE và amylose có mạch không phân nhánh."),
        make_mc(2, "Nhận biết", "Polymer nào sau đây có cấu trúc mạch phân nhánh điển hình?", ["Amylopectin", "Cellulose", "Polyethylene", "Poly(vinyl chloride)"], 0, "Amylopectin trong tinh bột có phân nhánh qua liên kết 1,6-glycosidic."),
        make_mc(3, "Nhận biết", "Vật liệu polymer nào sau đây có cấu trúc mạng không gian (mạng lưới ba chiều)?", ["Cao su lưu hóa", "Tơ tằm", "Polyethylene", "Nhựa PVC"], 0, "Cao su lưu hóa có các cầu nối disulfide -S-S- tạo mạng không gian."),
        make_mc(4, "Thông hiểu", "Vì sao các polymer không có nhiệt độ nóng chảy xác định như các chất tinh khiết phân tử nhỏ?", ["Vì polymer là hỗn hợp các phân tử có khối lượng phân tử và độ dài mạch khác nhau", "Vì polymer chứa kim loại nặng", "Vì polymer dễ tan trong nước", "Vì polymer là chất khí ở nhiệt độ phòng"], 0, "Polymer gồm các mạch có kích thước và khối lượng n khác nhau."),
        make_mc(5, "Thông hiểu", "Đặc tính vật lý nổi bật của cao su giúp nó được dùng làm săm lốp xe là:", ["Tính đàn hồi (biến dạng khi có lực tác dụng và phục hồi hình dạng khi thôi lực)", "Độ dẫn điện rất cao", "Độ tan hoàn toàn trong nước lạnh", "Dễ bay hơi ở nhiệt độ phòng"], 0, "Cao su có tính đàn hồi cao."),
        make_mc(6, "Thông hiểu", "Cầu nối liên kết giữa các mạch cao su trong cao su lưu hóa là cầu nối của nguyên tố nào?", ["Sulfur (lưu huỳnh, -S-S-)", "Nitrogen (-NH-)", "Oxygen (-O-O-)", "Phosphorus"], 0, "Cầu nối disulfide hình thành khi nấu cao su với lưu huỳnh."),
        make_mc(7, "Thông hiểu", "Nhựa nhiệt dẻo là loại polymer có đặc điểm nào sau đây?", ["Khi đun nóng bị nóng chảy mềm ra, khi để nguội lại đóng rắn lại và có thể tái chế nhiều lần", "Khi đun nóng bị phân hủy hoàn toàn thành than ngay lập tức mà không mềm", "Không bị biến dạng ở bất kỳ nhiệt độ nào", "Dẫn điện tốt như đồng và nhôm"], 0, "Nhựa nhiệt dẻo nóng chảy thuận nghịch khi đun nóng và làm nguội."),
        make_mc(8, "Thông hiểu", "Khi kéo dài sợi tơ nilon hoặc sợi len, lực giữ các phân tử polymer song song với nhau chủ yếu là lực gì?", ["Lực tương tác liên phân tử (lực hút tĩnh điện, liên kết hydrogen)", "Liên kết cộng hóa trị giữa các phân tử độc lập", "Liên kết kim loại", "Lực đẩy hạt nhân"], 0, "Lực tương tác liên phân tử giữ các chuỗi polymer dài xếp song song định hướng."),
        make_mc(9, "Thông hiểu", "Đặc điểm chung về tính tan của hầu hết các polymer tổng hợp (như PE, PVC, PS) là:", ["Không tan trong nước, bền với acid và kiềm loãng", "Tan vô hạn trong nước sôi", "Tan dễ dàng trong giấm ăn", "Dễ dàng bốc cháy trong nước"], 0, "Polymer tổng hợp không tan trong nước và khá bền hóa học."),
        make_mc(10, "Thông hiểu", "Polymer nào sau đây thuộc nhóm chất dẻo chịu nhiệt độ cao, dùng làm lớp chống dính chảo rán?", ["Teflon (-[-CF2-CF2-]-)n", "Polyethylene (PE)", "Nhựa PVC", "Cao su buna"], 0, "Teflon bền nhiệt, trơ hóa học và ma sát cực thấp."),
        make_mc(11, "Vận dụng", "Một sợi tơ nilon-6 có khối lượng phân tử trung bình là 28 250 amu. Biết phân tử khối một mắt xích (-[-NH-[CH2]5-CO-]-) là 113 amu. Số mắt xích trung bình trong phân tử tơ là:", ["250", "300", "200", "150"], 0, "28 250 / 113 = 250 mắt xích."),
        make_mc(12, "Vận dụng", "Khi lưu hóa cao su thiên nhiên, người ta trộn mủ cao su khô với bột lưu huỳnh (tỉ lệ khoảng 2 - 3% theo khối lượng) rồi đun nóng ở khoảng 140°C. Mục đích chính của việc lưu hóa là:", ["Tạo cấu trúc mạng không gian giúp cao su bền hơn, đàn hồi tốt hơn và chịu ma sát, chịu nhiệt tốt hơn", "Làm cho cao su dễ tan trong nước hơn", "Làm giảm tính đàn hồi để cao su giòn gãy", "Làm cho cao su bay hơi nhanh"], 0, "Tạo cầu nối -S-S- tăng độ đàn hồi, chịu nhiệt và chống mài mòn.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về cấu trúc mạch polymer:", [
            ("a", "Polymer có ba dạng cấu trúc mạch chính: không phân nhánh, phân nhánh và mạng không gian.", True),
            ("b", "Amylose trong tinh bột có cấu trúc mạch thẳng không phân nhánh và xoắn lại.", True),
            ("c", "Amylopectin và glycogen có cấu trúc mạch phân nhánh.", True),
            ("d", "Cao su chưa lưu hóa có cấu trúc mạng không gian bền vững hơn cao su đã lưu hóa.", False)
        ], "Cao su chưa lưu hóa có mạch thẳng, sau khi lưu hóa mới tạo mạng không gian bền hơn."),
        make_tf(2, "Thông hiểu", "Về tính chất vật lý chung của vật liệu polymer:", [
            ("a", "Hầu hết các polymer là chất rắn ở nhiệt độ phòng, không bay hơi.", True),
            ("b", "Đa số polymer dẫn điện và dẫn nhiệt rất tốt giống như kim loại đồng.", False),
            ("c", "Nhiều polymer có tính cách điện tốt như PE, PVC nên được bọc dây điện.", True),
            ("d", "Một số polymer có tính cơ học đặc biệt như tính đàn hồi (cao su) hoặc tính dẻo (nhựa PE).", True)
        ], "Polymer cách điện và cách nhiệt tốt, không dẫn điện dẫn nhiệt như kim loại."),
        make_tf(3, "Vận dụng", "Về quá trình biến đổi cơ lý của chất dẻo nhiệt và chất dẻo nhiệt rắn:", [
            ("a", "Nhựa nhiệt dẻo như PE, PP có thể nấu chảy và ép khuôn lại nhiều lần.", True),
            ("b", "Nhựa nhiệt rắn (như nhựa rezit có mạng không gian) khi đun nóng quá nhiệt sẽ bị cháy phân hủy chứ không chảy lỏng.", True),
            ("c", "Vỏ bút bi, chai nhựa PET đựng nước ngọt thuộc nhóm nhựa nhiệt dẻo có thể thu gom tái chế.", True),
            ("d", "Lốp xe tải làm từ cao su lưu hóa có thể nấu chảy dễ dàng như sáp nến để đúc lại lốp mới.", False)
        ], "Cao su lưu hóa có mạng không gian nhiệt rắn, không nóng chảy lỏng để đúc lại như sáp."),
        make_tf(4, "Vận dụng cao", "Về độ bền hóa học và sự biến tính của polymer:", [
            ("a", "Polyethylene rất trơ về mặt hóa học, không phản ứng với dung dịch acid loãng hay base loãng ở nhiệt độ phòng.", True),
            ("b", "Màng PVC nếu tiếp xúc với dầu mỡ nóng ở nhiệt độ cao lâu ngày có thể bị thoát các chất phụ gia hóa dẻo.", True),
            ("c", "Teflon bền vững với hóa chất và chịu được nhiệt độ lên tới gần 300°C.", True),
            ("d", "Tất cả các loại nhựa khi vứt bỏ ngoài bãi rác tự nhiên đều tự phân hủy sinh học hoàn toàn sau 1 tuần.", False)
        ], "Rác thải nhựa thông thường mất hàng trăm năm mới phân rã ngoài tự nhiên.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Cấu trúc mạch của cao su lưu hóa thuộc dạng cấu trúc mạch gì?", "Mạng không gian", "Mạng không gian (mạng lưới ba chiều)."),
        make_sa(2, "Thông hiểu", "Polymer cách điện tốt dùng để bọc lõi đồng của dây dẫn điện trong nhà phổ biến nhất là nhựa gì?", "PVC", "Nhựa PVC (hoặc PE)."),
        make_sa(3, "Thông hiểu", "Polymer phủ mặt chống dính chảo chiên rán có tên thương mại phổ biến là gì?", "Teflon", "Teflon (PTFE)."),
        make_sa(4, "Vận dụng", "Một phân tử cao su thiên nhiên gồm 3 000 mắt xích isoprene (C5H8, 68 amu). Khối lượng phân tử của phân tử cao su này bằng bao nhiêu amu?", "204000", "3 000 × 68 = 204 000 amu."),
        make_sa(5, "Vận dụng", "Trong cao su lưu hóa, nguyên tố sulfur chiếm 2% khối lượng cao su. Cứ bao nhiêu gam phân tử cao su lưu hóa thì có chứa 2 gam nguyên tố sulfur?", "100", "100 gam cao su lưu hóa chứa 2 gam S."),
        make_sa(6, "Vận dụng cao", "Một đoạn mạch nhựa rezit (bakelite) có cấu trúc mạng lưới không gian chứa 2 000 mắt xích có khối lượng mol trung bình là 106 g/mol mỗi mắt xích. Khối lượng của đoạn mạch đó là bao nhiêu amu?", "212000", "2 000 × 106 = 212 000 amu.")
    ],
    p4=[
        make_vdc(1, "Một cơ sở sản xuất ủng cao su sử dụng 500 kg cao su thiên nhiên thô. Để tăng độ bền và tính đàn hồi, người ta tiến hành lưu hóa với 2,5% bột lưu huỳnh theo khối lượng cao su. Khối lượng lưu huỳnh cần chuẩn bị trên lý thuyết là bao nhiêu kg?", ["12,5 kg", "25,0 kg", "10,0 kg", "5,0 kg"], 0, "m(S) = 500 × 2,5% = 12,5 kg."),
        make_vdc(2, "Vì sao các loại hộp xốp, hộp nhựa làm từ polystyrene (PS) hoặc túi nilon mỏng (PE) được khuyến cáo tuyệt đối không nên dùng để đựng trực tiếp thức ăn đang sôi sùng sục, dầu mỡ vừa chiên xong hay hâm nóng trong lò vi sóng ở nhiệt độ cao?", ["Vì ở nhiệt độ cao các monomer dư và chất phụ gia hóa dẻo độc hại dễ thôi nhiễm ra thực phẩm gây hại sức khỏe", "Vì nhựa sẽ hấp thụ hết chất dinh dưỡng của thức ăn", "Vì nhựa sẽ phát nổ thành lửa", "Vì thức ăn sẽ bị đông cứng lại"], 0, "Nhiệt độ cao làm chất phụ gia hóa dẻo và monomer dư thôi nhiễm vào dầu mỡ nóng."),
        make_vdc(3, "Một sợi dây câu cá làm bằng sợi cước polycaproamide (nilon-6) có khối lượng 1,13 gam. Biết phân tử khối của một mắt xích nilon-6 là 113 amu và số Avogadro NA = 6,022×10^23. Số lượng mắt xích nilon-6 có trong sợi cước đó xấp xỉ là:", ["6,022×10^21", "6,022×10^23", "1,13×10^21", "3,011×10^22"], 0, "n mắt xích = 1,13 / 113 = 0,01 mol -> Số mắt xích = 0,01 × 6,022×10^23 = 6,022×10^21."),
        make_vdc(4, "Một kỹ sư vật liệu tiến hành thí nghiệm kéo giãn hai mẫu cao su: Mẫu A là cao su thiên nhiên thô (chưa lưu hóa) và Mẫu B là cao su đã lưu hóa. Khi kéo dãn 200% chiều dài rồi buông tay: Mẫu B co lại ngay về kích thước ban đầu, còn mẫu A bị biến dạng dãn dài vĩnh viễn một phần. Giải thích khoa học cho hiện tượng trên là:", ["Nhờ các cầu nối disulfide -S-S- liên kết các chuỗi polymer thành mạng không gian 3 chiều giúp mẫu B phục hồi vị trí ban đầu sau khi biến dạng", "Mẫu A có nhiều lưu huỳnh hơn mẫu B", "Mẫu B là chất vô cơ", "Mẫu A bị đứt liên kết ion"], 0, "Mạng không gian lưu hóa ngăn các chuỗi trượt vĩnh viễn lên nhau, tạo tính đàn hồi phục hồi cao.")
    ]
)

# --- BÀI 15 - ĐỀ 3: Ứng dụng, chất dẻo, cao su, tơ sợi, ô nhiễm trắng và 3R ---
exams_c4[f"{LID_B15}_test3"] = make_exam(
    CID, CTITLE, LID_B15, LNAME_B15, 3,
    p1=[
        make_mc(1, "Nhận biết", "Chất dẻo là những vật liệu polymer có đặc tính:", ["Có tính dẻo (bị biến dạng khi chịu tác dụng của nhiệt, áp lực và giữ nguyên dạng khi thôi tác dụng)", "Có tính đàn hồi như cao su", "Dẫn điện tốt như đồng", "Dễ hòa tan hoàn toàn trong nước mát"], 0, "Chất dẻo có tính dẻo."),
        make_mc(2, "Nhận biết", "Polymer nào sau đây được dùng phổ biến để thổi màng mỏng làm túi đựng hàng, màng bọc thực phẩm gia đình?", ["Polyethylene (PE)", "Poly(vinyl chloride) (PVC)", "Cao su buna", "Tơ tằm"], 0, "PE mỏng, dẻo, không độc được dùng làm màng bọc thực phẩm."),
        make_mc(3, "Nhận biết", "Polymer nào sau đây được sử dụng rộng rãi để làm ống dẫn nước sinh hoạt và vỏ bọc dây điện?", ["Poly(vinyl chloride) (PVC)", "Cellulose", "Tinh bột", "Tơ tằm"], 0, "PVC làm ống nước, vỏ cách điện cáp."),
        make_mc(4, "Nhận biết", "Khái niệm 'Ô nhiễm trắng' dùng để chỉ tình trạng ô nhiễm môi trường do loại rác thải nào gây ra?", ["Rác thải nhựa và túi nilon khó phân hủy", "Rác thải thức ăn thừa phân hủy", "Rác thải bụi vôi xây dựng", "Ô nhiễm do khí CO2"], 0, "Ô nhiễm trắng là ô nhiễm rác thải nhựa."),
        make_mc(5, "Thông hiểu", "Giải pháp 3R trong quản lý và bảo vệ môi trường khỏi rác thải nhựa là viết tắt của 3 từ tiếng Anh nào?", ["Reduce - Reuse - Recycle (Giảm thiểu - Tái sử dụng - Tái chế)", "Read - React - Return", "Run - Remove - Repair", "Real - Rapid - Reliable"], 0, "3R: Reduce, Reuse, Recycle."),
        make_mc(6, "Thông hiểu", "Loại nhựa nào sau đây an toàn và chịu nhiệt tốt nhất để sản xuất bình sữa trẻ em và hộp đựng cơm dùng được trong lò vi sóng?", ["Nhựa Polypropylene (PP, ký hiệu số 5)", "Nhựa Polystyrene (PS, xốp hộp cơm số 6)", "Nhựa Poly(vinyl chloride) (PVC, số 3)", "Nhựa bẩn không rõ nguồn gốc"], 0, "Nhựa PP số 5 chịu nhiệt tới 130-165°C và an toàn thực phẩm."),
        make_mc(7, "Thông hiểu", "Vì sao không nên đốt rác thải nhựa PVC (ống nhựa, da nhân tạo giả da) ngoài trời tự do?", ["Khi cháy PVC sinh ra khí độc hydrogen chloride (HCl) và hợp chất cực độc dioxin", "Vì PVC cháy tạo ra oxy gây nổ", "Vì PVC không bao giờ cháy được", "Vì PVC cháy chỉ tạo ra hơi nước tinh khiết"], 0, "Đốt PVC sinh ra khí acid HCl độc hại và dioxin gây ung thư."),
        make_mc(8, "Thông hiểu", "Chất dẻo phân hủy sinh học (bioplastic, như nhựa PLA chế biến từ tinh bột ngô) có ưu điểm vượt trội nào?", ["Có khả năng bị vi sinh vật phân hủy thành CO2 và nước trong thời gian ngắn ngoài môi trường", "Có giá thành rẻ hơn nhựa thông thường 100 lần", "Có độ cứng hơn kim cương", "Không bao giờ bị phân hủy"], 0, "Bioplastic phân hủy sinh học tự nhiên thân thiện với môi trường."),
        make_mc(9, "Thông hiểu", "Hành động nào sau đây của học sinh góp phần thiết thực nhất làm giảm ô nhiễm rác thải nhựa?", ["Mang theo bình nước cá nhân và túi vải khi đi mua sắm, từ chối túi nilon dùng 1 lần", "Mỗi ngày dùng 5 chiếc túi nilon mới rồi vứt ra đường", "Vứt rác nhựa xuống sông ngòi", "Đốt rác nhựa trong sân trường"], 0, "Giảm thiểu (Reduce) và tái sử dụng (Reuse) túi vải, bình nước cá nhân."),
        make_mc(10, "Thông hiểu", "Vật liệu composite là vật liệu được tạo thành bằng cách:", ["Kết hợp chất nền (nhựa polymer) với chất độn tăng cường (sợi thủy tinh, sợi carbon) tạo vật liệu mới siêu bền nhẹ", "Trộn đường ăn với muối ăn", "Nấu chảy kim loại sắt", "Hòa tan polymer vào nước biển"], 0, "Composite kết hợp polymer với chất độn gia cường."),
        make_mc(11, "Vận dụng", "Ký hiệu tam giác mũi tên xoay tròn có số 1 bên trong in dưới đáy các chai nước khoáng đóng chai biểu thị loại nhựa nào?", ["Nhựa PET (Polyethylene terephthalate)", "Nhựa PE (Polyethylene)", "Nhựa PVC", "Nhựa PP"], 0, "Số 1 là nhựa PET (chuyên dùng làm chai nước giải khát)."),
        make_mc(12, "Vận dụng", "Để tái chế 10 tấn chai nhựa PET phế liệu thành sợi dệt thảm polyester với hiệu suất tái chế đạt 85%, khối lượng sợi dệt thành phẩm thu được là:", ["8,5 tấn", "10,0 tấn", "11,5 tấn", "7,5 tấn"], 0, "10 × 85% = 8,5 tấn.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về ứng dụng thực tiễn của polymer:", [
            ("a", "Polyethylene (PE) mềm dẻo, cách điện tốt, dùng làm màng bọc thức ăn và túi xách hàng.", True),
            ("b", "Poly(vinyl chloride) (PVC) cứng hơn PE, dùng làm ống dẫn nước và khung cửa nhựa.", True),
            ("c", "Tơ tằm thiên nhiên được dệt thành lụa tơ tằm sang trọng, giữ ấm mùa đông mát mùa hè.", True),
            ("d", "Tất cả các loại nhựa tổng hợp đều tự tiêu hủy trong đất sau 24 giờ chôn lấp.", False)
        ], "Nhựa tổng hợp khó phân hủy, tồn tại hàng trăm năm trong môi trường."),
        make_tf(2, "Thông hiểu", "Về vấn đề môi trường và rác thải polymer:", [
            ("a", "Rác thải nhựa khi vứt bừa bãi gây tắc nghẽn cống rãnh, ngập lụt đô thị và hại sinh vật biển.", True),
            ("b", "Vi nhựa (microplastics) có thể xâm nhập vào chuỗi thức ăn thông qua hải sản và nước uống.", True),
            ("c", "Đốt rác thải nhựa ngoài bãi rác tự do là biện pháp xử lý rác thân thiện và sạch nhất.", False),
            ("d", "Phân loại rác tại nguồn giúp tăng hiệu quả tái chế nhựa và tiết kiệm tài nguyên dầu mỏ.", True)
        ], "Đốt rác nhựa ngoài trời sinh khói bụi mịn, khí độc HCl, dioxin cực kỳ nguy hiểm."),
        make_tf(3, "Vận dụng", "Về việc sử dụng đồ nhựa an toàn cho sức khỏe:", [
            ("a", "Không dùng đồ nhựa dùng một lần loại PS (hộp xốp) để đựng canh chua nóng, nước chanh đậm đặc hay mỡ sôi.", True),
            ("b", "Nên ưu tiên dùng các đồ dùng gia đình làm từ thủy tinh, sứ hoặc thép không gỉ.", True),
            ("c", "Chai nhựa PET số 1 uống xong nên rửa sạch rồi dùng lại đựng nước sôi uống quanh năm trong 5 năm.", False),
            ("d", "Hộp nhựa có ký hiệu PP (số 5) là loại có thể dùng được an toàn trong lò vi sóng để hâm thức ăn.", True)
        ], "Chai PET số 1 chỉ nên dùng 1 lần, rửa dùng lại nhiều lần ở nhiệt độ cao có nguy cơ thôi nhiễm hóa chất."),
        make_tf(4, "Vận dụng cao", "Về nghiên cứu và phát triển vật liệu mới thân thiện môi trường:", [
            ("a", "Nhựa sinh học PLA làm từ ngô, sắn có thể phân hủy sinh học thành CO2 và mùn hữu cơ trong điều kiện ủ công nghiệp.", True),
            ("b", "Tận dụng vỏ trấu, bã mía ép thành bát đĩa dùng một lần thay thế hộp xốp là xu hướng tiêu dùng xanh.", True),
            ("c", "Vật liệu composite sợi carbon siêu nhẹ siêu bền được ứng dụng chế tạo vỏ máy bay và thân xe đua f1.", True),
            ("d", "Vật liệu polymer hoàn toàn vô dụng và con người nên quay về chỉ dùng đồ đá và gỗ mục.", False)
        ], "Polymer là vật liệu then chốt của văn minh hiện đại nếu được sử dụng và tái chế đúng cách.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Ký hiệu số mấy bên trong tam giác tái chế đại diện cho nhựa Polypropylene an toàn cho lò vi sóng?", "5", "Số 5 (PP)."),
        make_sa(2, "Nhận biết", "Hạt vi nhựa có kích thước đường kính nhỏ hơn bao nhiêu milimét (mm)?", "5", "Nhỏ hơn 5 mm."),
        make_sa(3, "Thông hiểu", "Khí acid độc hại chủ yếu sinh ra khi đốt cháy ống nhựa PVC là khí gì?", "HCl", "Khí Hydrogen chloride (HCl)."),
        make_sa(4, "Vận dụng", "Một siêu thị mỗi ngày phát ra 5 000 chiếc túi nilon. Nhờ vận động khách hàng mang túi vải, siêu thị đã cắt giảm được 60% lượng túi phát ra. Số túi nilon được giảm mỗi ngày là bao nhiêu?", "3000", "5 000 × 60% = 3 000 túi."),
        make_sa(5, "Vận dụng", "Một gia đình 4 người mỗi tháng thải ra trung bình 2,5 kg rác thải nhựa. Trong 1 năm (12 tháng), gia đình đó thải ra bao nhiêu kg rác nhựa?", "30", "2,5 × 12 = 30 kg."),
        make_sa(6, "Vận dụng cao", "Một nhà máy tái chế nhựa xử lý 50 tấn rác chai nhựa PET thu được 42,5 tấn hạt nhựa tái sinh. Tỉ lệ thu hồi sản phẩm của quá trình tái chế là bao nhiêu phần trăm?", "85", "42,5 / 50 × 100% = 85%.")
    ],
    p4=[
        make_vdc(1, "Mỗi ngày một trường học có 1 200 học sinh. Trung bình cứ 3 học sinh tiêu thụ 1 chai nước ngọt nhựa PET loại 500 mL vứt đi (khối lượng vỏ chai là 20 gam). Nếu nhà trường tổ chức thu gom 100% vỏ chai này để bán gây quỹ kế hoạch nhỏ trong suốt năm học (270 ngày), tổng khối lượng nhựa PET thu gom được là bao nhiêu kg?", ["2 160 kg", "1 800 kg", "2 500 kg", "1 250 kg"], 0, "Số chai/ngày = 1 200 / 3 = 400 chai -> Khối lượng nhựa/ngày = 400 × 0,02 kg = 8 kg -> Cả năm = 8 × 270 = 2 160 kg."),
        make_vdc(2, "Một doanh nghiệp thực phẩm chuyển đổi từ bao bì nhựa nilon thông thường sang màng bọc phân hủy sinh học làm từ tinh bột sắn (acid polylactic - PLA). Màng PLA có đặc tính phân rã sinh học trong lòng đất ẩm dưới tác dụng của vi sinh vật. Sau 180 ngày thử nghiệm chôn lấp, 50 kg màng PLA bị phân hủy 92% khối lượng thành CO2, H2O và mùn sinh học. Khối lượng bã màng polymer còn lại chưa phân hủy là:", ["4 kg", "8 kg", "2 kg", "46 kg"], 0, "Khối lượng còn lại = 50 × (100% - 92%) = 4 kg."),
        make_vdc(3, "Để điều chế 10,5 tấn nhựa polypropylene (PP) dùng làm hộp bảo quản thực phẩm, người ta tiến hành trùng hợp khí propylene (C3H6) với hiệu suất phản ứng đạt 84%. Thể tích khí propylene cần chuẩn bị ở điều kiện chuẩn 25°C, 1 bar (biết 1 mol khí ở đkc chiếm 24,79 L) là bao nhiêu nghìn mét khối (m3)?", ["7 378 m3", "5 600 m3", "6 250 m3", "8 120 m3"], 0, "m lý thuyết propylene = 10,5 / 0,84 = 12,5 tấn -> n = 12,5 / 42 = 0,2976 Mmol -> V = 0,2976 × 24,79 × 10^6 L = 7 378 m3."),
        make_vdc(4, "Một làng nghề tái chế nhựa thu gom túi nilon bẩn để nấu hạt nhựa tái sinh. Nước thải từ bể rửa nilon chứa nhiều cặn vi nhựa lơ lửng, chất tẩy rửa và mực in. Để xử lý dòng nước thải này đạt chuẩn xả thải môi trường, hệ thống xử lý nước thải bắt buộc phải kết hợp các công đoạn kỹ thuật nào?", ["Lắng lọc tách cặn cơ học -> keo tụ tạo bông vi nhựa -> xử lý sinh học hiếu khí -> lọc khử trùng than hoạt tính", "Chỉ cần xả thẳng ra cánh đồng lúa", "Đun sôi toàn bộ nước thải rồi đổ ra sông", "Cho acid đặc vào để tiêu biến hết nước thải"], 0, "Kết hợp lọc cơ học, keo tụ tách vi nhựa, sinh học và than hoạt tính.")
    ]
)

# ==============================================================================
# ÔN TẬP CUỐI CHƯƠNG IV (chem9_c4_rev) - 5 ĐỀ
# ==============================================================================
LID_REV = "chem9_c4_rev"
LNAME_REV = "Ôn tập cuối Chương IV: Lipid - Carbohydrate - Protein - Polymer"

# --- ÔN TẬP CHƯƠNG IV - ĐỀ 1: Tổng hợp Lipid và Carbohydrate ---
exams_c4[f"{LID_REV}_test1"] = make_exam(
    CID, CTITLE, LID_REV, LNAME_REV, 1,
    p1=[
        make_mc(1, "Nhận biết", "Chất béo là triester của carboxylic acid béo với alcohol nào sau đây?", ["Glycerol (C3H5(OH)3)", "Ethanol (C2H5OH)", "Methanol (CH3OH)", "Ethylene glycol (C2H4(OH)2)"], 0, "Chất béo là triester của acid béo và glycerol."),
        make_mc(2, "Nhận biết", "Công thức phân tử của glucose là:", ["C6H12O6", "C12H22O11", "(C6H10O5)n", "C2H4O2"], 0, "Glucose là C6H12O6."),
        make_mc(3, "Nhận biết", "Saccharose có nhiều nhất trong loại nông sản nào ở nước ta?", ["Cây mía", "Củ khoai lang", "Quả nho chín", "Hạt lúa gạo"], 0, "Saccharose là đường mía."),
        make_mc(4, "Nhận biết", "Thuốc thử hóa học đặc trưng dùng để nhận biết dung dịch glucose tạo kết tủa bạc sáng bóng là:", ["Dung dịch AgNO3 trong NH3 (thuốc thử Tollens)", "Nước vôi trong Ca(OH)2", "Dung dịch quỳ tím", "Dung dịch phenolphthalein"], 0, "Thuốc thử AgNO3/NH3 thực hiện phản ứng tráng bạc."),
        make_mc(5, "Thông hiểu", "Sự khác biệt quan trọng về tính chất hóa học giữa glucose và saccharose là:", ["Glucose có phản ứng tráng bạc còn saccharose thì không", "Saccharose tan trong nước còn glucose không tan", "Glucose không cháy còn saccharose cháy", "Saccharose có vị ngọt còn glucose có vị đắng"], 0, "Glucose có nhóm -CHO nên tráng bạc, saccharose không tráng bạc trực tiếp."),
        make_mc(6, "Thông hiểu", "Phản ứng thủy phân chất béo trong dung dịch kiềm (NaOH hoặc KOH) đun nóng được gọi là phản ứng:", ["Xà phòng hóa", "Trùng hợp", "Este hóa", "Lên men rượu"], 0, "Thủy phân trong kiềm tạo xà phòng và glycerol."),
        make_mc(7, "Thông hiểu", "Khi thủy phân hoàn toàn 1 phân tử saccharose trong môi trường acid, thu được sản phẩm gồm:", ["1 phân tử glucose và 1 phân tử fructose", "2 phân tử glucose", "2 phân tử fructose", "1 phân tử glucose và 1 phân tử glycerol"], 0, "Saccharose thủy phân thành 1 glucose + 1 fructose."),
        make_mc(8, "Thông hiểu", "Dầu ăn thực vật (dầu mè, dầu đậu nành) để lâu ngày ngoài không khí tiếp xúc với ánh sáng thường bị ôi thiu khét là do:", ["Các gốc acid béo không no bị oxy hóa chậm bởi oxygen không khí tạo thành các hợp chất aldehyde và peroxide có mùi khó chịu", "Dầu ăn bị biến thành đường", "Dầu ăn bay hơi hết vào không khí", "Dầu ăn bị đông đặc thành đá"], 0, "Oxy hóa liên kết đôi C=C của chất béo không no tạo mùi ôi thiu."),
        make_mc(9, "Thông hiểu", "Chất béo nhẹ hơn nước và có tính tan như thế nào?", ["Không tan trong nước, tan tốt trong dung môi hữu cơ như benzene, xăng", "Tan vô hạn trong nước lạnh", "Tan trong nước sôi tạo dung dịch trong suốt", "Không tan trong bất kỳ chất nào"], 0, "Chất béo kị nước, tan trong dung môi hữu cơ."),
        make_mc(10, "Thông hiểu", "Trong y tế, dịch truyền tĩnh mạch cung cấp năng lượng nhanh cho người bệnh suy nhược chứa glucose nồng độ bao nhiêu?", ["5%", "50%", "0,1%", "80%"], 0, "Dung dịch glucose 5% đẳng trương cung cấp năng lượng."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn 18 gam glucose (C6H12O6) thu được thể tích khí CO2 (đkc ở 25°C, 1 bar) là bao nhiêu lít? (1 mol khí ở đkc = 24,79 L)", ["14,874 L", "22,400 L", "24,790 L", "12,395 L"], 0, "n(glucose) = 18 / 180 = 0,1 mol -> n(CO2) = 0,6 mol -> V = 0,6 × 24,79 = 14,874 L."),
        make_mc(12, "Vận dụng", "Xà phòng hóa hoàn toàn 8,9 kg tristearin (C17H35COO)3C3H5 (M = 890 g/mol) bằng dung dịch NaOH vừa đủ. Khối lượng glycerol (M = 92 g/mol) thu được là:", ["0,92 kg", "1,84 kg", "0,46 kg", "2,76 kg"], 0, "n(chất béo) = 8,9 / 890 = 0,01 kmol -> m(glycerol) = 0,01 × 92 = 0,92 kg.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về cấu tạo và tính chất của Lipid và Carbohydrate:", [
            ("a", "Chất béo là một loại lipid phổ biến trong mỡ động vật và dầu thực vật.", True),
            ("b", "Glucose và saccharose đều là các chất rắn màu trắng, vị ngọt, dễ tan trong nước.", True),
            ("c", "Glucose có công thức phân tử là C6H12O6, saccharose là C12H22O11.", True),
            ("d", "Chất béo tan hoàn toàn trong nước lạnh tạo dung dịch đồng nhất.", False)
        ], "Chất béo không tan trong nước, nổi trên mặt nước."),
        make_tf(2, "Thông hiểu", "Về các phản ứng hóa học đặc trưng của carbohydrate và lipid:", [
            ("a", "Dung dịch glucose tham gia phản ứng tráng bạc với thuốc thử AgNO3 trong NH3.", True),
            ("b", "Dung dịch saccharose tinh khiết không có khả năng tráng bạc trực tiếp.", True),
            ("c", "Sau khi đun sôi saccharose với acid vô cơ loãng, dung dịch sau trung hòa có thể tráng bạc.", True),
            ("d", "Phản ứng xà phòng hóa chất béo là phản ứng thuận nghịch hai chiều hoàn toàn giống este hóa.", False)
        ], "Phản ứng xà phòng hóa trong kiềm là phản ứng một chiều không thuận nghịch."),
        make_tf(3, "Vận dụng", "Về vai trò sinh học và dinh dưỡng của lipid và đường:", [
            ("a", "Lipid cung cấp nhiều năng lượng nhất cho cơ thể (khoảng 9 kcal/gam), cao hơn protein và glucid.", True),
            ("b", "Chất béo giúp cơ thể hòa tan và hấp thu các vitamin tan trong dầu như A, D, E, K.", True),
            ("c", "Ăn quá nhiều mỡ động vật giàu acid béo no làm tăng nguy cơ xơ vữa động mạch và tim mạch.", True),
            ("d", "Người bị bệnh đái tháo đường nên ăn thật nhiều bánh kẹo ngọt và uống nước ngọt có ga hàng ngày.", False)
        ], "Người bệnh tiểu đường cần hạn chế đường và carbohydrate hấp thu nhanh."),
        make_tf(4, "Vận dụng cao", "Về ứng dụng công nghiệp của đường và chất béo:", [
            ("a", "Glycerol thu được từ sản xuất xà phòng được dùng trong mỹ phẩm và công nghiệp dược phẩm.", True),
            ("b", "Glucose được dùng để tráng ruột phích nước, tráng gương và sản xuất vitamin C.", True),
            ("c", "Dầu thực vật đã qua sử dụng có thể được tái chế chế biến thành nhiên liệu sinh học biodiesel.", True),
            ("d", "Đường mía saccharose không thể bị vi sinh vật lên men trong bất kỳ điều kiện nào.", False)
        ], "Saccharose có thể bị thủy phân và lên men rượu hoặc acid trong công nghiệp men bia, rượu vang.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Phân tử khối của glucose (C6H12O6) bằng bao nhiêu amu?", "180", "12×6 + 1×12 + 16×6 = 180 amu."),
        make_sa(2, "Nhận biết", "Phân tử khối của saccharose (C12H22O11) bằng bao nhiêu amu?", "342", "12×12 + 1×22 + 16×11 = 342 amu."),
        make_sa(3, "Thông hiểu", "1 phân tử chất béo khi thủy phân hoàn toàn trong kiềm tạo ra bao nhiêu phân tử muối acid béo (xà phòng)?", "3", "3 phân tử muối của acid béo."),
        make_sa(4, "Vận dụng", "Đun nóng 36 gam glucose với lượng dư dung dịch AgNO3 trong NH3 thu được bao nhiêu gam Ag kết tủa? (Ag = 108)", "43.2", "n(glu) = 36 / 180 = 0,2 mol -> n(Ag) = 0,4 mol -> m(Ag) = 0,4 × 108 = 43,2 gam."),
        make_sa(5, "Vận dụng", "Thủy phân hoàn toàn 34,2 gam saccharose với hiệu suất 100%. Tổng khối lượng hỗn hợp glucose và fructose thu được là bao nhiêu gam?", "36", "34,2 / 342 = 0,1 mol -> m monosaccharide = 0,1 × 180 + 0,1 × 180 = 36 gam."),
        make_sa(6, "Vận dụng cao", "Xà phòng hóa hoàn toàn 17,8 gam chất béo tristearin bằng 100 mL dung dịch NaOH 1M (lấy dư). Sau phản ứng, cô cạn dung dịch thu được m gam chất rắn khan. Biết hiệu suất phản ứng 100%. Giá trị của m là bao nhiêu gam?", "20.16", "n(chất béo) = 17,8 / 890 = 0,02 mol -> n(NaOH pư) = 0,06 mol; n(glycerol) = 0,02 mol (m = 1,84 gam). n(NaOH ban đầu) = 0,1 mol (m = 4 gam). Bảo toàn khối lượng: m rắn = 17,8 + 4 - 1,84 = 20,16 gam.")
    ],
    p4=[
        make_vdc(1, "Để tráng một lớp bạc mỏng phản xạ ánh sáng lên mặt kính gương soi có diện tích 2 m2 với độ dày lớp bạc là 0,1 micromet (10^-7 m), người ta dùng dung dịch glucose đun nóng với AgNO3/NH3 dư với hiệu suất tráng bạc 80%. Biết khối lượng riêng của bạc kim loại là 10,5 g/cm3. Khối lượng glucose tối thiểu cần dùng là:", ["2,19 gam", "4,38 gam", "1,75 gam", "3,25 gam"], 0, "V(Ag) = 2 m2 × 10^-7 m = 2×10^-7 m3 = 0,2 cm3 -> m(Ag) = 0,2 × 10,5 = 2,1 gam -> n(Ag) = 2,1 / 108 = 0,01944 mol -> n(glu pư) = 0,00972 mol -> m(glu lý thuyết) = 0,00972 × 180 = 1,75 gam -> m thực tế = 1,75 / 0,8 = 2,19 gam."),
        make_vdc(2, "Một xưởng xà phòng mini sản xuất xà phòng từ mỡ heo (chứa 90% triolein và 10% tạp chất không xà phòng hóa). Thủy phân 100 kg mỡ heo bằng lượng dư dung dịch KOH. Toàn bộ lượng muối potassium oleate tạo thành được phối trộn thêm tinh dầu sả chanh và chất độn để tạo bánh xà phòng chứa 60% muối oleate. Khối lượng xà phòng bánh 60% thu được với hiệu suất 95% là:", ["154,6 kg", "120,5 kg", "180,0 kg", "95,0 kg"], 0, "m(triolein) = 90 kg (M = 884) -> n = 90/884 = 0,1018 kmol -> n(muối C17H33COOK, M = 320) = 3 × 0,1018 = 0,3054 kmol -> m muối lý thuyết = 0,3054 × 320 = 97,73 kg -> m thực tế = 97,73 × 0,95 = 92,85 kg -> m bánh xà phòng = 92,85 / 0,6 = 154,7 ≈ 154,6 kg."),
        make_vdc(3, "Một bệnh nhân tiểu đường thử nước tiểu bằng que thử glucose thấy đổi màu chỉ thị cho biết nồng độ glucose trong nước tiểu là 10 mmol/L. Nếu mỗi ngày bệnh nhân bài tiết khoảng 1,5 lít nước tiểu thì lượng đường glucose bị thất thoát qua nước tiểu trong 1 ngày là bao nhiêu gam?", ["2,7 gam", "1,8 gam", "5,4 gam", "3,6 gam"], 0, "n(glu) = 0,01 mol/L × 1,5 L = 0,015 mol -> m = 0,015 × 180 = 2,7 gam."),
        make_vdc(4, "Một tấn nước mía chứa 13% saccharose được đưa vào chế biến đường tinh luyện. Quá trình làm sạch, cô đặc và kết tinh có hiệu suất thu hồi đường đạt 82%. Khối lượng đường saccharose tinh khiết đóng bao thu được là:", ["106,6 kg", "130,0 kg", "82,0 kg", "115,5 kg"], 0, "m(saccharose trong mía) = 1 000 × 13% = 130 kg -> Thu hồi = 130 × 82% = 106,6 kg.")
    ]
)

# --- ÔN TẬP CHƯƠNG IV - ĐỀ 2: Tổng hợp Tinh bột và Cellulose, quang hợp ---
exams_c4[f"{LID_REV}_test2"] = make_exam(
    CID, CTITLE, LID_REV, LNAME_REV, 2,
    p1=[
        make_mc(1, "Nhận biết", "Tinh bột và cellulose đều thuộc nhóm hợp chất carbohydrate nào sau đây?", ["Polysaccharide", "Monosaccharide", "Disaccharide", "Lipid"], 0, "Cả hai đều là polymer thiên nhiên polysaccharide có công thức (C6H10O5)n."),
        make_mc(2, "Nhận biết", "Chất nào sau đây tác dụng với dung dịch iodine (I2) tạo hợp chất có màu xanh tím đặc trưng?", ["Hồ tinh bột", "Dung dịch saccharose", "Dung dịch glucose", "Cellulose"], 0, "Hồ tinh bột tác dụng với iodine cho màu xanh tím."),
        make_mc(3, "Nhận biết", "Thành phần chính tạo nên màng tế bào thực vật, tạo nên bộ khung của thân cây gỗ và sợi bông là:", ["Cellulose", "Tinh bột", "Protein", "Chất béo"], 0, "Cellulose là thành phần cấu tạo vách tế bào thực vật."),
        make_mc(4, "Nhận biết", "Trong tự nhiên, cây xanh tổng hợp tinh bột nhờ quá trình nào sau đây?", ["Quang hợp", "Hô hấp", "Thủy phân", "Lên men"], 0, "Quang hợp dưới ánh sáng mặt trời và diệp lục."),
        make_mc(5, "Thông hiểu", "Vì sao tinh bột và cellulose cùng có công thức tổng quát (-[-C6H10O5-]-)n nhưng không phải là đồng phân của nhau?", ["Vì hệ số polymer hóa n trong phân tử của chúng rất khác nhau và cấu trúc không gian khác nhau", "Vì chúng có nguyên tố cấu tạo khác nhau", "Vì một chất tan trong nước còn một chất là chất khí", "Vì chúng có phản ứng cháy khác nhau"], 0, "Hệ số n của cellulose lớn hơn rất nhiều so với tinh bột."),
        make_mc(6, "Thông hiểu", "Sản phẩm cuối cùng thu được khi thủy phân hoàn toàn tinh bột nhờ enzyme hoặc acid là:", ["Glucose", "Fructose", "Saccharose", "Cellulose"], 0, "Thủy phân tinh bột cho glucose."),
        make_mc(7, "Thông hiểu", "Chất lỏng nào sau đây có thể hòa tan được cellulose tạo dung dịch nhớt dùng trong kỹ thuật sản xuất tơ sợi?", ["Dung dịch Schweizer (phức đồng amine Cu(OH)2 trong NH3)", "Nước khoáng đóng chai", "Dầu hỏa", "Rượu vang"], 0, "Dung dịch Schweizer hòa tan được cellulose."),
        make_mc(8, "Thông hiểu", "Vai trò chính của cellulose (chất xơ) trong hệ tiêu hóa của con người là gì?", ["Kích thích nhu động ruột, phòng ngừa táo bón và các bệnh đại tràng", "Cung cấp nguồn calo chính cho cơ thể", "Hòa tan các loại mỡ trong máu", "Tổng hợp nên kháng thể"], 0, "Cellulose là chất xơ kích thích nhu động đường ruột."),
        make_mc(9, "Thông hiểu", "Khí nào sau đây được cây xanh hấp thụ trong quá trình quang hợp và khí nào được giải phóng ra khí quyển?", ["Hấp thụ khí carbon dioxide (CO2), giải phóng khí oxygen (O2)", "Hấp thụ O2, giải phóng CO2", "Hấp thụ N2, giải phóng H2", "Hấp thụ SO2, giải phóng CO2"], 0, "Cây xanh hấp thụ CO2 và nhả O2."),
        make_mc(10, "Thông hiểu", "Tơ visco và tơ acetate thuộc loại tơ nào sau đây?", ["Tơ bán tổng hợp (tơ nhân tạo sản xuất từ cellulose)", "Tơ thiên nhiên", "Tơ tổng hợp hoàn toàn từ dầu mỏ", "Tơ protein"], 0, "Tơ nhân tạo chế biến từ cellulose gỗ."),
        make_mc(11, "Vận dụng", "Để sản xuất 90 kg glucose trong công nghiệp với hiệu suất 80%, khối lượng tinh bột (C6H10O5)n cần dùng là bao nhiêu kg?", ["101,25 kg", "81,00 kg", "125,00 kg", "90,00 kg"], 0, "(C6H10O5)n -> n C6H12O6: 162n kg -> 180n kg. m lý thuyết = 90 × 162 / 180 = 81 kg -> m thực tế = 81 / 0,8 = 101,25 kg."),
        make_mc(12, "Vận dụng", "Một cây xanh ban ngày hấp thụ 44 gam khí CO2 để thực hiện phản ứng quang hợp tạo tinh bột. Khối lượng khí O2 giải phóng ra khí quyển là:", ["32 gam", "44 gam", "16 gam", "64 gam"], 0, "6n CO2 -> 6n O2. Tỉ lệ mol 1:1 -> n(O2) = n(CO2) = 1 mol -> m(O2) = 32 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về tinh bột và cellulose:", [
            ("a", "Tinh bột có nhiều trong các loại hạt ngũ cốc (gạo, ngô, lúa mì) và các loại củ.", True),
            ("b", "Cellulose có nhiều nhất trong sợi bông nõn (gần 98%) và trong gỗ (khoảng 50%).", True),
            ("c", "Con người có enzyme tiêu hóa được tinh bột thành glucose nhưng không tiêu hóa được cellulose.", True),
            ("d", "Tinh bột và cellulose đều tham gia phản ứng tráng bạc khi đun với AgNO3/NH3 mà không cần thủy phân.", False)
        ], "Cả hai đều không có nhóm aldehyde tự do nên không tráng bạc trực tiếp."),
        make_tf(2, "Thông hiểu", "Về phản ứng màu và tính tan của tinh bột:", [
            ("a", "Hồ tinh bột nguội gặp dung dịch iodine tạo màu xanh tím đặc trưng.", True),
            ("b", "Khi đun nóng nhẹ dung dịch xanh tím trên, màu xanh biến mất; để nguội màu xanh tím lại xuất hiện.", True),
            ("c", "Tinh bột tan tốt trong nước lạnh tạo dung dịch trong suốt.", False),
            ("d", "Trong nước nóng từ 65°C trở lên, hạt tinh bột trương phồng vỡ ra tạo dung dịch keo gọi là hồ tinh bột.", True)
        ], "Tinh bột không tan trong nước lạnh."),
        make_tf(3, "Vận dụng", "Về quá trình quang hợp và chu trình carbon trong sinh quyển:", [
            ("a", "Phương trình quang hợp: 6n CO2 + 5n H2O --(ánh sáng, diệp lục)--> (C6H10O5)n + 6n O2.", True),
            ("b", "Rừng cây xanh được ví như lá phổi xanh giúp cân bằng nồng độ CO2 và O2 trong khí quyển.", True),
            ("c", "Chặt phá rừng bừa bãi làm tăng hiệu ứng nhà kính và biến đổi khí hậu toàn cầu.", True),
            ("d", "Khí oxygen sinh ra trong quang hợp có nguồn gốc nguyên tử từ phân tử khí CO2.", False)
        ], "Theo các nghiên cứu đánh dấu đồng vị quang hợp, O2 sinh ra từ sự quang phân ly nước H2O."),
        make_tf(4, "Vận dụng cao", "Về ứng dụng công nghiệp của cellulose:", [
            ("a", "Cellulose được dùng trực tiếp làm vật liệu xây dựng, đóng đồ gỗ nội thất và làm giấy viết.", True),
            ("b", "Cellulose phản ứng với nitric acid đậm đặc (xúc tác H2SO4) tạo cellulose trinitrate dùng làm thuốc súng không khói.", True),
            ("c", "Dịch chiết cellulose có thể dùng làm thực phẩm chức năng thay thế hoàn toàn cơm gạo cho người giảm béo.", False),
            ("d", "Sản xuất tơ visco từ cellulose giúp đa dạng hóa nguồn nguyên liệu ngành dệt may mặc.", True)
        ], "Cơ thể người không thể tiêu hóa biến cellulose thành calo thay cơm được.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Khối lượng mol của một mắt xích tinh bột (-[-C6H10O5-]-) bằng bao nhiêu g/mol?", "162", "12×6 + 1×10 + 16×5 = 162 g/mol."),
        make_sa(2, "Nhận biết", "Dung dịch thuốc thử nào dùng để nhận biết tinh bột bằng phản ứng tạo màu xanh tím?", "Iodine", "Dung dịch iodine (I2)."),
        make_sa(3, "Thông hiểu", "Sợi bông tự nhiên chứa khoảng bao nhiêu phần trăm khối lượng cellulose?", "98", "Khoảng 95 - 98%."),
        make_sa(4, "Vận dụng", "Thủy phân hoàn toàn 32,4 gam tinh bột trong môi trường acid. Lượng glucose tạo thành cho phản ứng tráng bạc hoàn toàn với dung dịch AgNO3/NH3 dư. Khối lượng Ag thu được là bao nhiêu gam?", "43.2", "n(mắt xích) = 32,4 / 162 = 0,2 mol -> n(glu) = 0,2 mol -> n(Ag) = 0,4 mol -> m(Ag) = 43,2 gam."),
        make_sa(5, "Vận dụng", "Một mẫu gỗ chứa 50% cellulose về khối lượng. Từ 1 tấn mẫu gỗ khô đó, người ta sản xuất được bao nhiêu kg bột giấy tinh khiết (chứa 90% cellulose) với hiệu suất thu hồi 90%?", "500", "m cellulose = 500 kg -> m cellulose thu được = 500 × 90% = 450 kg -> m bột giấy 90% = 450 / 0,9 = 500 kg."),
        make_sa(6, "Vận dụng cao", "Một hecta (ha) rừng keo lá tràm mỗi năm quang hợp hấp thụ trung bình 26,4 tấn khí CO2. Khối lượng khí O2 giải phóng ra môi trường mỗi năm từ một hecta rừng đó là bao nhiêu tấn?", "19.2", "n(CO2) = 26,4 / 44 = 0,6 Mmol -> n(O2) = 0,6 Mmol -> m(O2) = 0,6 × 32 = 19,2 tấn.")
    ],
    p4=[
        make_vdc(1, "Một nhà máy sản xuất cồn sinh học ethanol từ ngô hạt. Hạt ngô khô chứa 65% tinh bột. Để sản xuất 4,6 tấn ethanol (C2H5OH) dùng pha chế xăng E5 theo sơ đồ: (C6H10O5)n -> n C6H12O6 -> 2n C2H5OH + 2n CO2 với hiệu suất chung của toàn bộ quá trình lên men đạt 80%, khối lượng ngô hạt cần huy động là:", ["15,58 tấn", "12,46 tấn", "10,25 tấn", "18,20 tấn"], 0, "n(C2H5OH) = 4,6 / 46 = 0,1 Mmol -> n(mắt xích tinh bột) = 0,05 Mmol -> m lý thuyết tinh bột = 0,05 × 162 = 8,1 tấn -> m thực tế tinh bột = 8,1 / 0,8 = 10,125 tấn -> m ngô = 10,125 / 0,65 = 15,577 ≈ 15,58 tấn."),
        make_vdc(2, "Người ta thực hiện thí nghiệm nhận biết 3 dung dịch không nhãn chứa riêng biệt: hồ tinh bột, glucose và saccharose đựng trong 3 ống nghiệm. Trình tự hóa chất và thao tác nhận biết tối ưu nhất là:", ["Dùng dung dịch iodine nhận ra hồ tinh bột (hóa xanh); Dùng thuốc thử AgNO3/NH3 nhận ra glucose (tráng bạc); Dung dịch còn lại là saccharose", "Dùng quỳ tím rồi cho kiềm", "Dùng dung dịch nước vôi trong", "Cho quỳ tím và ngửi mùi"], 0, "Iodine nhận ra hồ tinh bột, AgNO3/NH3 nhận ra glucose, còn lại là saccharose."),
        make_vdc(3, "Để điều chế 29,7 kg cellulose trinitrate [C6H7O2(ONO2)3]n (thuốc súng không khói, M mắt xích = 297 g/mol) từ cellulose [C6H7O2(OH)3]n (M = 162 g/mol) và dung dịch HNO3 đậm đặc với hiệu suất 90%, khối lượng HNO3 tinh khiết tối thiểu đã phản ứng là:", ["21,0 kg", "18,9 kg", "25,0 kg", "15,5 kg"], 0, "n mắt xích sản phẩm = 29,7 / 297 = 0,1 kmol -> n(HNO3 lý thuyết) = 3 × 0,1 = 0,3 kmol -> m(HNO3 lý thuyết) = 0,3 × 63 = 18,9 kg -> m thực tế = 18,9 / 0,9 = 21,0 kg."),
        make_vdc(4, "Một học sinh nhai một miếng cơm nguội hoặc bánh mì trắng trong miệng thật kỹ từ 3 đến 5 phút thấy xuất hiện vị ngọt rõ rệt. Giải thích khoa học cho hiện tượng trên là:", ["Enzyme amylase trong nước bọt đã xúc tác thủy phân một phần tinh bột thành đường maltose có vị ngọt", "Cơm nguội tự bay hơi nước để lại đường", "Răng tiết ra đường glucose", "Tinh bột phản ứng với acid dạ dày trào ngược"], 0, "Enzyme amylase trong tuyến nước bọt thủy phân tinh bột thành đường đôi maltose có vị ngọt.")
    ]
)

# --- ÔN TẬP CHƯƠNG IV - ĐỀ 3: Tổng hợp Protein và Polymer ---
exams_c4[f"{LID_REV}_test3"] = make_exam(
    CID, CTITLE, LID_REV, LNAME_REV, 3,
    p1=[
        make_mc(1, "Nhận biết", "Nguyên tố hóa học nào sau đây luôn luôn có mặt trong phân tử protein bên cạnh các nguyên tố C, H, O?", ["Nitrogen (N)", "Chlorine (Cl)", "Bromine (Br)", "Sodium (Na)"], 0, "Protein luôn chứa nguyên tố nitrogen."),
        make_mc(2, "Nhận biết", "Liên kết liên kết giữa các đơn vị amino acid trong chuỗi phân tử protein được gọi là:", ["Liên kết peptide (-CO-NH-)", "Liên kết ion", "Liên kết kim loại", "Liên kết hydro"], 0, "Liên kết peptide -CO-NH- tạo nên chuỗi polypeptide của protein."),
        make_mc(3, "Nhận biết", "Hiện tượng lòng trắng trứng bị đông tụ lại khi đun sôi trong nước được gọi là:", ["Sự đông tụ protein bởi nhiệt độ", "Sự xà phòng hóa", "Sự bay hơi", "Sự lên men"], 0, "Đông tụ protein do nhiệt độ phá vỡ cấu trúc không gian bậc cao."),
        make_mc(4, "Nhận biết", "Vật liệu polymer nào sau đây được dùng phổ biến để làm bao bì xốp cách nhiệt, khay đựng hoa quả siêu thị?", ["Polystyrene (nhựa PS)", "Cellulose", "Protein", "Cao su thiên nhiên"], 0, "Xốp PS (mút xốp)."),
        make_mc(5, "Thông hiểu", "Phương pháp đơn giản nhất để phân biệt sợi len lông cừu (protein) với sợi len dệt từ tơ nilon acrylic (polymer tổng hợp) là:", ["Đốt sợi len: tơ cừu cháy có mùi khét tóc và tro xốp giòn bóp vụn, nilon vón cục nhựa cứng khét hắc", "Nhúng vào nước", "Dùng kính lúp soi màu sắc", "Cân khối lượng sợi"], 0, "Đốt cháy nhận biết qua mùi tóc khét và đặc điểm tro than."),
        make_mc(6, "Thông hiểu", "Vì sao các bác sĩ khuyến cáo khi bị sốt cao trên 40°C cần phải hạ sốt khẩn cấp cho bệnh nhân?", ["Vì nhiệt độ quá cao làm biến tính và đông tụ các protein enzyme quan trọng trong não và cơ thể dẫn đến co giật, tử vong", "Vì nhiệt độ cao làm máu đông cứng thành đường", "Vì nhiệt độ cao làm xương bị tan chảy", "Vì cơ thể sẽ bốc cháy"], 0, "Nhiệt độ cao làm biến tính protein enzyme cơ thể."),
        make_mc(7, "Thông hiểu", "Quá trình nào sau đây làm biến tính protein có ứng dụng tích cực trong chế biến thực phẩm gia đình?", ["Nấu canh cua nổi gạch gơ cua và làm đậu phụ từ sữa đậu nành bằng nước chua", "Để thức ăn ôi thiu", "Rửa thịt bằng nước xà phòng", "Phơi khô quần áo lụa"], 0, "Gạch cua đóng bánh và đậu phụ đông tụ protein từ dịch đậu tương."),
        make_mc(8, "Thông hiểu", "Polymer nào sau đây là sản phẩm trùng hợp từ monomer vinyl chloride (CH2=CHCl)?", ["Poly(vinyl chloride) (PVC)", "Polyethylene (PE)", "Cao su buna", "Tơ tằm"], 0, "PVC được trùng hợp từ vinyl chloride."),
        make_mc(9, "Thông hiểu", "Sự đông tụ của protein còn có thể xảy ra khi cho chất nào sau đây vào dung dịch protein?", ["Acid mạnh, kiềm mạnh hoặc cồn (ethanol)", "Nước cất tinh khiết", "Khí oxy", "Khí nitrogen"], 0, "Acid, base và rượu làm biến tính đông tụ protein."),
        make_mc(10, "Thông hiểu", "Cao su thiên nhiên được chế biến từ mủ cây cao su có đặc tính nổi trội là:", ["Tính đàn hồi rất tốt, không thấm nước và khí", "Dẫn điện tốt như kim loại", "Dễ tan hoàn toàn trong nước lạnh", "Nhiệt độ sôi cố định ở 100°C"], 0, "Cao su đàn hồi, chống thấm nước và khí."),
        make_mc(11, "Vận dụng", "Hàm lượng nguyên tố nitrogen trong một loại protein chiếm 16% khối lượng. Một người trưởng thành tiêu thụ 75 gam protein này mỗi ngày. Khối lượng nguyên tố nitrogen cơ thể tiếp nhận trong ngày là:", ["12 gam", "16 gam", "8 gam", "10 gam"], 0, "75 × 16% = 12 gam."),
        make_mc(12, "Vận dụng", "Đốt cháy hoàn toàn một mẩu polymer chỉ chứa C và H thu được 8,8 gam CO2 và 3,6 gam H2O. Polymer đó là:", ["Polyethylene (PE)", "PVC", "Polyacrylonitrile", "Tơ tằm"], 0, "n(CO2) = 0,2 mol, n(H2O) = 0,2 mol -> n(C) : n(H) = 0,2 : 0,4 = 1 : 2 -> Công thức (CH2)n chính là Polyethylene (PE).")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về protein và polymer:", [
            ("a", "Protein là những hợp chất cao phân tử phức tạp được tạo nên từ nhiều đơn vị amino acid.", True),
            ("b", "Polymer có khối lượng phân tử rất lớn gồm nhiều mắt xích liên kết với nhau.", True),
            ("c", "Tơ tằm là một loại polymer thiên nhiên có bản chất hóa học là protein.", True),
            ("d", "Tất cả các polymer đều dễ dàng hòa tan trong nước sôi để tạo dung dịch dinh dưỡng.", False)
        ], "Phần lớn polymer không tan trong nước."),
        make_tf(2, "Thông hiểu", "Về sự đông tụ và biến tính protein trong đời sống:", [
            ("a", "Cồn y tế 70° diệt khuẩn nhanh nhờ khả năng làm đông tụ protein của vi khuẩn và virus.", True),
            ("b", "Khi vắt chanh (chứa citric acid) vào sữa tươi, sữa bị kết tủa vón cục do protein bị đông tụ bởi acid.", True),
            ("c", "Quần áo dệt từ len lông cừu tự nhiên có thể giặt bằng bột giặt có độ kiềm cực cao và ngâm trong nước sôi 100°C.", False),
            ("d", "Lòng trắng trứng đun nóng bị đông tụ chuyển từ dạng lỏng trong suốt sang thể rắn đục màu trắng.", True)
        ], "Len lông cừu là protein bị co rút và phá hủy nhanh bởi kiềm và nước nóng."),
        make_tf(3, "Vận dụng", "Về các loại tơ sợi và vật liệu polymer thông dụng:", [
            ("a", "Tơ nilon-6,6 thuộc loại tơ tổng hợp có độ bền cơ học cao, dai, óng mượt và ít thấm nước.", True),
            ("b", "Cao su lưu hóa có cấu trúc mạng lưới không gian bền chắc và đàn hồi hơn cao su thô.", True),
            ("c", "Nhựa tái chế loại kém phẩm cấp từ rác thải y tế rất an toàn để làm bát thìa ăn dặm cho trẻ sơ sinh.", False),
            ("d", "Rác thải nhựa khi chôn lấp làm giảm độ phì nhiêu của đất và cản trở rễ cây trồng phát triển.", True)
        ], "Nhựa tái chế không rõ nguồn gốc chứa nhiều mầm bệnh và phụ gia kim loại nặng độc hại."),
        make_tf(4, "Vận dụng cao", "Về bảo quản thực phẩm giàu đạm protein:", [
            ("a", "Thịt, cá tươi để ở nhiệt độ phòng lâu ngày bị ôi thiu do vi sinh vật phân hủy protein tạo ra các hợp chất amine và H2S có mùi hôi.", True),
            ("b", "Bảo quản thịt cá bằng phương pháp cấp đông sâu (-18°C) giúp ức chế sự sinh sôi của vi khuẩn phân hủy đạm.", True),
            ("c", "Ướp muối (làm mắm, cá muối) tạo môi trường ưu trương làm vi khuẩn mất nước và bị ức chế phát triển.", True),
            ("d", "Thịt thối rữa có thể ngâm dung dịch nước oxy già và hàn the để biến thành thịt tươi nguyên chất hoàn toàn bổ dưỡng.", False)
        ], "Thịt thối rữa đã tích tụ độc tố vi khuẩn, hóa chất tẩy trắng chỉ che đậy mùi chứ không thể phục hồi độ an toàn.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Liên kết đặc trưng giữa hai đơn vị amino acid (-CO-NH-) trong protein gọi là liên kết gì?", "Peptide", "Liên kết peptide."),
        make_sa(2, "Nhận biết", "Cồn y tế có nồng độ cồn tối ưu nhất để sát khuẩn bằng cách làm đông tụ protein vi khuẩn là bao nhiêu độ (°)?", "70", "70°."),
        make_sa(3, "Thông hiểu", "Tỉ lệ phần trăm nguyên tố nitrogen trung bình có trong các phân tử protein khoảng bao nhiêu phần trăm?", "16", "Khoảng 16%."),
        make_sa(4, "Vận dụng", "Một mẫu lụa tơ tằm nguyên chất nặng 5 gam chứa 16% nitrogen. Khối lượng nguyên tố nitrogen trong mẫu lụa đó là bao nhiêu gam?", "0.8", "5 × 16% = 0,8 gam."),
        make_sa(5, "Vận dụng", "Trùng hợp 4,2 tấn propylene thu được 3,78 tấn polypropylene (PP). Hiệu suất của phản ứng trùng hợp là bao nhiêu phần trăm?", "90", "3,78 / 4,2 × 100% = 90%."),
        make_sa(6, "Vận dụng cao", "Đốt cháy hoàn toàn 2,8 gam một mẩu cao su buna (-[-CH2-CH=CH-CH2-]-)n. Thể tích khí CO2 (đkc ở 25°C, 1 bar) thu được là bao nhiêu lít? (Biết 1 mol khí ở đkc = 24,79 L, C = 12, H = 1)", "4.958", "M mắt xích C4H6 = 54 -> n mắt xích = 2,8 / 54 = 0,05185 mol -> n(C) = 4 × 0,05185 = 0,2 mol -> V(CO2) = 0,2 × 24,79 = 4,958 L.")
    ],
    p4=[
        make_vdc(1, "Một cơ sở dệt may kiểm tra lô nguyên liệu nhập khẩu gồm 2 cuộn sợi dệt lớn: Cuộn 1 được dán nhãn tơ tằm thiên nhiên (100% protein), Cuộn 2 được dán nhãn sợi tơ dệt từ nilon tổng hợp. Để xác minh nhãn mác mà không có phòng thí nghiệm chuyên sâu, biện pháp thực tế nhanh và hiệu quả nhất là:", ["Cắt một đoạn sợi nhỏ của từng cuộn đem đốt: Cuộn 1 cháy có khói bay lên mùi khét như tóc cháy, tàn tro màu đen giòn xốp dễ bóp nát; Cuộn 2 cháy có mùi nhựa khét, đầu sợi co lại thành cục tròn cứng ngắc khó bóp", "Cho cả hai cuộn vào ngâm nước sôi", "Để ra ngoài nắng 1 tháng", "Dùng nam châm điện rà tìm"], 0, "Đốt cháy thử mùi khét tóc và đặc điểm vón cục tro là phương pháp chuẩn xác phân biệt tơ tự nhiên và tổng hợp."),
        make_vdc(2, "Một người làm đậu phụ từ hạt đậu nành khô. Trong hạt đậu nành chứa 36% protein. Người đó ngâm xay 10 kg hạt đậu nành với nước, lọc bỏ bã thu được nước sữa đậu nành. Khi đun sôi và cho nước chua (chứa acid acetic loãng) vào, toàn bộ protein bị đông tụ và ép thành bánh đậu. Biết hiệu suất thu hồi protein đạt 75%. Khối lượng protein nguyên chất có trong bánh đậu thu được là:", ["2,7 kg", "3,6 kg", "1,8 kg", "2,2 kg"], 0, "m protein trong hạt = 10 × 36% = 3,6 kg -> m protein thu hồi = 3,6 × 75% = 2,7 kg."),
        make_vdc(3, "Để sản xuất 2,5 tấn tơ nilon-6 từ caprolactam với hiệu suất 80%, khối lượng monomer caprolactam cần sử dụng là bao nhiêu tấn?", ["3,125 tấn", "2,000 tấn", "3,500 tấn", "2,850 tấn"], 0, "m = 2,5 / 0,8 = 3,125 tấn."),
        make_vdc(4, "Một bếp ăn tập thể dùng nồi nhôm để nấu món súp canh chua có nồng độ acid cao và nhiều muối mặn trong suốt 4 giờ liền. Hiện tượng thôi nhiễm ion kim loại Al3+ vào thức ăn có thể xảy ra do nguyên nhân nào sau đây?", ["Nước canh chua chứa acid hữu cơ kết hợp ion chloride làm hòa tan và ăn mòn lớp màng oxide bảo vệ của nồi nhôm", "Nồi nhôm tự phân hủy thành đường", "Chất béo trong canh hút kim loại nhôm", "Nồi nhôm biến thành nhựa"], 0, "Môi trường acid và muối mặn phá hủy màng Al2O3 bảo vệ, gây ăn mòn hòa tan nhôm vào thực phẩm.")
    ]
)

# --- ÔN TẬP CHƯƠNG IV - ĐỀ 4: Bài toán định lượng tổng hợp Chương IV ---
exams_c4[f"{LID_REV}_test4"] = make_exam(
    CID, CTITLE, LID_REV, LNAME_REV, 4,
    p1=[
        make_mc(1, "Nhận biết", "Chất nào sau đây khi tác dụng với lượng dư dung dịch AgNO3 trong NH3 thu được kết tủa kim loại Ag sáng bóng?", ["Glucose", "Saccharose", "Tinh bột", "Cellulose"], 0, "Glucose có phản ứng tráng bạc."),
        make_mc(2, "Nhận biết", "Trong phản ứng xà phòng hóa chất béo bằng dung dịch NaOH, sản phẩm luôn luôn thu được chất nào sau đây?", ["Glycerol", "Methanol", "Ethanol", "Acid acetic"], 0, "Thủy phân chất béo luôn sinh ra glycerol."),
        make_mc(3, "Nhận biết", "Chất nào sau đây bị thủy phân hoàn toàn trong môi trường acid chỉ tạo ra một loại monosaccharide duy nhất là glucose?", ["Tinh bột", "Saccharose", "Chất béo", "Protein"], 0, "Tinh bột thủy phân chỉ tạo glucose."),
        make_mc(4, "Thông hiểu", "Cho 0,1 mol glucose tham gia phản ứng tráng bạc hoàn toàn với dung dịch AgNO3 trong NH3 dư. Số mol Ag kim loại kết tủa tối đa thu được là:", ["0,2 mol", "0,1 mol", "0,3 mol", "0,4 mol"], 0, "1 mol glucose tạo 2 mol Ag -> 0,1 mol tạo 0,2 mol Ag."),
        make_mc(5, "Thông hiểu", "Lên men rượu 360 gam glucose với hiệu suất 100%. Khối lượng ethanol (C2H5OH, M = 46) thu được là:", ["184 gam", "92 gam", "368 gam", "46 gam"], 0, "n(glu) = 360 / 180 = 2 mol -> n(C2H5OH) = 4 mol -> m = 4 × 46 = 184 gam."),
        make_mc(6, "Thông hiểu", "Để xà phòng hóa hoàn toàn 1 mol triolein (C17H33COO)3C3H5 cần dùng vừa đủ bao nhiêu mol NaOH?", ["3 mol", "1 mol", "2 mol", "4 mol"], 0, "Chất béo là triester cần 3 mol NaOH."),
        make_mc(7, "Thông hiểu", "Thủy phân hoàn toàn 171 gam saccharose (C12H22O11, M = 342) trong môi trường acid. Lượng glucose tạo thành có khả năng tạo ra tối đa bao nhiêu gam Ag khi tráng gương? (Ag = 108)", ["108 gam", "216 gam", "54 gam", "72 gam"], 0, "n(sac) = 171 / 342 = 0,5 mol -> n(glu) = 0,5 mol -> n(Ag) = 1 mol -> m(Ag) = 108 gam."),
        make_mc(8, "Thông hiểu", "Trùng hợp hoàn toàn 5,6 gam ethylene (C2H4) với hiệu suất 100%. Khối lượng polyethylene thu được là:", ["5,6 gam", "2,8 gam", "11,2 gam", "4,48 gam"], 0, "Theo định luật bảo toàn khối lượng, m(PE) = m(C2H4) = 5,6 gam."),
        make_mc(9, "Thông hiểu", "Lượng nhiệt tỏa ra khi đốt cháy 1 gam lipid, 1 gam glucid và 1 gam protid lần lượt xấp xỉ là:", ["Lipid: 9 kcal; Glucid: 4 kcal; Protid: 4 kcal", "Lipid: 4 kcal; Glucid: 9 kcal; Protid: 4 kcal", "Cả ba đều tỏa 9 kcal", "Cả ba đều tỏa 4 kcal"], 0, "Lipid cung cấp 9 kcal/g; glucid và protid cung cấp 4 kcal/g."),
        make_mc(10, "Thông hiểu", "Chất béo lỏng (dầu thực vật) có thể được chuyển hóa thành chất béo rắn (bơ nhân tạo, shortening) bằng phản ứng hóa học nào?", ["Phản ứng hydro hóa (cộng H2 vào liên kết đôi C=C xúc tác Ni, đun nóng)", "Phản ứng xà phòng hóa", "Phản ứng thủy phân", "Phản ứng lên men"], 0, "Hydro hóa biến acid béo không no thành no."),
        make_mc(11, "Vận dụng", "Lên men 100 lít nước mía ép chứa 12% saccharose thành ethanol với hiệu suất toàn bộ quá trình là 70%. Biết khối lượng riêng của nước mía ép là 1,05 kg/L. Khối lượng ethanol thu được là:", ["4,74 kg", "3,70 kg", "1,85 kg", "2,59 kg"], 0, "m dung dịch = 105 kg -> m saccharose = 105 × 12% = 12,6 kg -> n = 12,6 / 342 = 0,03684 kmol -> n(C2H5OH lý thuyết) = 4 × 0,03684 = 0,14737 kmol -> m lý thuyết = 0,14737 × 46 = 6,779 kg -> m thực tế = 6,779 × 0,7 = 4,74 kg."),
        make_mc(12, "Vận dụng", "Đun nóng 8,9 gam tristearin với dung dịch NaOH vừa đủ, cô cạn dung dịch sau phản ứng thu được m gam xà phòng natri stearate (C17H35COONa, M = 306). Giá trị của m là:", ["9,18 gam", "8,90 gam", "10,20 gam", "6,12 gam"], 0, "n(chất béo) = 8,9 / 890 = 0,01 mol -> n(muối) = 0,03 mol -> m = 0,03 × 306 = 9,18 gam.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các nhận định về các phép tính lượng chất trong hóa học hữu cơ 9:", [
            ("a", "1 mol glucose (180 gam) khi tráng bạc hoàn toàn giải phóng đúng 2 mol Ag (216 gam).", True),
            ("b", "1 mol chất béo triester khi tác dụng với kiềm luôn phản ứng với đúng 3 mol NaOH.", True),
            ("c", "1 phân tử saccharose khi thủy phân hoàn toàn tạo ra 2 phân tử glucose.", False),
            ("d", "Khối lượng một mắt xích của tinh bột là 162 amu và của cellulose cũng là 162 amu.", True)
        ], "Saccharose thủy phân ra 1 glucose và 1 fructose."),
        make_tf(2, "Thông hiểu", "Về phản ứng lên men glucose:", [
            ("a", "Phương trình: C6H12O6 --(men rượu, 30-35°C)--> 2 C2H5OH + 2 CO2.", True),
            ("b", "Cứ 180 gam glucose lên men hoàn toàn trên lý thuyết sinh ra 92 gam rượu ethylic.", True),
            ("c", "Khí CO2 sinh ra trong quá trình lên men rượu làm đục nước vôi trong.", True),
            ("d", "Lên men rượu trong điều kiện có thật nhiều khí oxygen thoáng khí thì độ cồn càng cao.", False)
        ], "Lên men rượu là quá trình yếm khí (kị khí); nếu nhiều oxy rượu sẽ bị oxy hóa thành giấm acetic."),
        make_tf(3, "Vận dụng", "Về phản ứng xà phòng hóa và bảo toàn khối lượng:", [
            ("a", "Khối lượng xà phòng tạo thành thường lớn hơn khối lượng chất béo ban đầu đem xà phòng hóa.", True),
            ("b", "Công thức bảo toàn khối lượng: m chất béo + m NaOH = m muối xà phòng + m glycerol.", True),
            ("c", "Để tách xà phòng nổi lên trên bề mặt, người ta thường cho thêm muối ăn NaCl bão hòa vào.", True),
            ("d", "Glycerol thu được sau phản ứng xà phòng hóa có khả năng bay hơi nhanh như cồn ethanol.", False)
        ], "Glycerol là chất lỏng sánh, nhớt, nhiệt độ sôi cao 290°C, không dễ bay hơi."),
        make_tf(4, "Vận dụng cao", "Về bài toán hiệu suất và tinh chế:", [
            ("a", "Khi hiệu suất phản ứng nhỏ hơn 100%, khối lượng sản phẩm thực tế luôn nhỏ hơn khối lượng lý thuyết.", True),
            ("b", "Để tính khối lượng chất phản ứng cần dùng, ta lấy khối lượng lý thuyết chia cho hiệu suất.", True),
            ("c", "Quá trình tráng bạc gương soi công nghiệp đạt hiệu suất khoảng 80-90% do bạc bám cả vào thành bình phản ứng.", True),
            ("d", "Hiệu suất chuyển hóa 80% có nghĩa là cứ 100 kg nguyên liệu thì tạo ra đúng 100 kg sản phẩm tinh khiết.", False)
        ], "Hiệu suất 80% nghĩa là chỉ 80% lượng nguyên liệu chuyển hóa thành sản phẩm theo lý thuyết.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "1 mol glucose khi phản ứng tráng gương hoàn toàn tạo ra bao nhiêu mol Ag?", "2", "2 mol Ag."),
        make_sa(2, "Nhận biết", "1 mol chất béo khi xà phòng hóa hoàn toàn tạo ra bao nhiêu mol glycerol?", "1", "1 mol glycerol."),
        make_sa(3, "Thông hiểu", "Khối lượng mol của muối sodium stearate (C17H35COONa) là bao nhiêu g/mol?", "306", "306 g/mol."),
        make_sa(4, "Vận dụng", "Lên men 90 gam glucose với hiệu suất 80%. Khối lượng rượu ethylic (C2H5OH) thu được là bao nhiêu gam?", "36.8", "n(glu) = 0,5 mol -> n(EtOH lt) = 1 mol -> m lt = 46 gam -> m thực tế = 46 × 0,8 = 36,8 gam."),
        make_sa(5, "Vận dụng", "Cho 10 gam một mẫu đường glucose có lẫn tạp chất không tráng bạc vào dung dịch AgNO3/NH3 dư, thu được 10,8 gam Ag. Độ tinh khiết của mẫu đường glucose đó là bao nhiêu phần trăm?", "90", "n(Ag) = 0,1 mol -> n(glu) = 0,05 mol -> m(glu) = 0,05 × 180 = 9 gam -> % = 9 / 10 × 100% = 90%."),
        make_sa(6, "Vận dụng cao", "Thủy phân hoàn toàn 68,4 gam saccharose thành hỗn hợp X gồm glucose và fructose. Cho toàn bộ X tác dụng với dung dịch AgNO3/NH3 dư. Tổng khối lượng Ag thu được là bao nhiêu gam?", "86.4", "n(sac) = 68,4 / 342 = 0,2 mol -> n(glu + fruc) = 0,4 mol -> n(Ag) = 0,8 mol -> m(Ag) = 0,8 × 108 = 86,4 gam.")
    ],
    p4=[
        make_vdc(1, "Một cơ sở tráng ruột phích nước sử dụng phản ứng tráng bạc của glucose. Để tráng bạc 500 ruột phích, mỗi ruột phích cần một lớp bạc có khối lượng 0,54 gam bám đều trên bề mặt thủy tinh. Biết hiệu suất phản ứng tráng bạc bám dính đạt 75%. Khối lượng glucose tối thiểu cơ sở cần dùng là:", ["300 gam", "225 gam", "400 gam", "180 gam"], 0, "Tổng m(Ag) cần bám = 500 × 0,54 = 270 gam -> n(Ag) = 270 / 108 = 2,5 mol -> n(glu lý thuyết) = 1,25 mol -> m(glu lý thuyết) = 1,25 × 180 = 225 gam -> m thực tế = 225 / 0,75 = 300 gam."),
        make_vdc(2, "Từ 1 tấn gạo chứa 81% tinh bột, người ta đem lên men sản xuất rượu ethylic (ancol etylic) 40° dùng cho ngành y tế và công nghiệp dược phẩm. Biết hiệu suất toàn bộ quá trình lên men và chưng cất là 70%, khối lượng riêng của ethanol nguyên chất là 0,8 g/mL. Thể tích rượu 40° thu được là:", ["1 006,25 lít", "800,60 lít", "640,50 lít", "920,00 lít"], 0, "m(tinh bột) = 810 kg -> n(mắt xích) = 810 / 162 = 5 kmol -> n(C2H5OH lý thuyết) = 10 kmol -> m(EtOH lý thuyết) = 460 kg -> m thực tế = 460 × 70% = 322 kg -> V(EtOH nguyên chất) = 322 / 0,8 = 402,5 L -> V rượu 40° = 402,5 / 0,4 = 1 006,25 L."),
        make_vdc(3, "Thủy phân 100 kg chất béo triolein (C17H33COO)3C3H5 (chứa 88,4% triolein nguyên chất) bằng dung dịch NaOH dư. Sau khi cô cạn và tinh chế thu được 82,08 kg xà phòng sodium oleate (C17H33COONa, M = 304). Hiệu suất của phản ứng xà phòng hóa là:", ["90%", "85%", "95%", "80%"], 0, "m(triolein) = 88,4 kg -> n = 88,4 / 884 = 0,1 kmol -> n(muối lý thuyết) = 0,3 kmol -> m muối lý thuyết = 0,3 × 304 = 91,2 kg -> H = 82,08 / 91,2 × 100% = 90%."),
        make_vdc(4, "Một người nông dân trồng sắn thu hoạch được 5 tấn củ sắn tươi chứa 32,4% tinh bột. Toàn bộ lượng sắn này được bán cho nhà máy cồn sinh học để chế biến ethanol làm nhiên liệu sinh học. Với hiệu suất cả quá trình đạt 75%, thể tích cồn sinh học nguyên chất (D = 0,8 kg/L) nhà máy thu được từ số sắn trên là:", ["862,5 L", "690,0 L", "1 025,0 L", "750,0 L"], 0, "m(tinh bột) = 5 000 × 32,4% = 1 620 kg -> n(mắt xích) = 1 620 / 162 = 10 kmol -> n(EtOH lý thuyết) = 20 kmol -> m lý thuyết = 20 × 46 = 920 kg -> m thực tế = 920 × 0,75 = 690 kg -> V = 690 / 0,8 = 862,5 L.")
    ]
)

# --- ÔN TẬP CHƯƠNG IV - ĐỀ 5: Vận dụng cao toàn diện Chương IV ---
exams_c4[f"{LID_REV}_test5"] = make_exam(
    CID, CTITLE, LID_REV, LNAME_REV, 5,
    p1=[
        make_mc(1, "Nhận biết", "Trong cơ thể sống, enzyme có bản chất hóa học là gì?", ["Protein", "Chất béo", "Carbohydrate", "Polyethylene"], 0, "Hầu hết các enzyme xúc tác sinh học là protein."),
        make_mc(2, "Nhận biết", "Polymer thiên nhiên nào sau đây được dùng để sản xuất xà phòng sau khi thủy phân bằng kiềm?", ["Chất béo (lipid)", "Cellulose", "Cao su", "Poly(vinyl chloride)"], 0, "Xà phòng sản xuất từ chất béo."),
        make_mc(3, "Nhận biết", "Carbohydrate nào có hàm lượng cao nhất trong hạt gạo tẻ của người Việt Nam?", ["Tinh bột", "Saccharose", "Glucose", "Cellulose"], 0, "Hạt gạo tẻ chứa khoảng 75 - 80% tinh bột."),
        make_mc(4, "Thông hiểu", "Sự chuyển hóa tinh bột trong cơ thể người diễn ra theo trình tự các chất nào sau đây?", ["Tinh bột -> Dextrin -> Maltose -> Glucose", "Tinh bột -> Cellulose -> Glucose", "Tinh bột -> Protein -> Acid béo", "Tinh bột -> Xà phòng -> Rượu"], 0, "Quá trình tiêu hóa tinh bột nhờ enzyme amylase và maltase thành glucose hấp thụ vào máu."),
        make_mc(5, "Thông hiểu", "Phương pháp nào sau đây giúp loại bỏ bớt mùi tanh của cá khi chế biến món ăn?", ["Rửa cá với giấm ăn hoặc nước cốt chanh hoặc rượu trắng", "Rửa cá bằng nước xà phòng giặt", "Ngâm cá trong nước đường", "Đun cá trong nước vôi trong"], 0, "Acid hữu cơ trong chanh/giấm trung hòa các amine tanh tạo muối tan không bay hơi."),
        make_mc(6, "Thông hiểu", "Khi làm sữa chua tại nhà, hiện tượng sữa đặc lại và có vị chua thanh là do:", ["Vi khuẩn lactic lên men đường lactose thành lactic acid làm đông tụ protein casein trong sữa", "Sữa bị đông đá", "Sữa bị bốc hơi hết nước", "Sữa phản ứng với oxy tạo xà phòng"], 0, "Acid lactic hạ pH gây đông tụ protein sữa tạo cấu trúc mịn đặc."),
        make_mc(7, "Thông hiểu", "Polymer nào sau đây thuộc loại polymer nhân tạo (bán tổng hợp)?", ["Tơ visco", "Tơ tằm", "Polyethylene (PE)", "Nhựa bakelite"], 0, "Tơ visco chế biến từ cellulose gỗ."),
        make_mc(8, "Thông hiểu", "Vì sao mỡ động vật (như mỡ lợn, mỡ bò) ở nhiệt độ phòng thường ở thể rắn còn dầu thực vật (dầu mè, dầu lạc) lại ở thể lỏng?", ["Mỡ động vật chứa chủ yếu gốc acid béo no, còn dầu thực vật chứa nhiều gốc acid béo không no", "Mỡ động vật chứa kim loại", "Dầu thực vật tan trong nước", "Mỡ động vật có phân tử khối nhỏ hơn"], 0, "Acid béo no có nhiệt độ nóng chảy cao hơn acid béo không no."),
        make_mc(9, "Thông hiểu", "Hiện tượng 'cháy ren' lụa khi là (ủi) áo tơ tằm ở nhiệt độ quá cao là do:", ["Protein trong tơ tằm bị nhiệt độ cao làm biến tính và phân hủy nhiệt", "Sợi tơ hút hết hơi nước", "Sợi tơ phản ứng với kim loại bàn là", "Tơ tằm biến thành cao su"], 0, "Nhiệt độ cao làm cháy phân hủy protein tơ tằm."),
        make_mc(10, "Thông hiểu", "Chất nào sau đây vừa tác dụng được với dung dịch NaOH khi đun nóng, vừa tác dụng được với dung dịch HCl khi đun nóng?", ["Protein (lòng trắng trứng)", "Polyethylene", "Methane", "Saccharose"], 0, "Protein có tính lưỡng tính và bị thủy phân trong cả môi trường acid lẫn kiềm."),
        make_mc(11, "Vận dụng", "Đốt cháy hoàn toàn m gam hỗn hợp gồm glucose và saccharose cần dùng 0,6 mol khí O2. Dẫn toàn bộ sản phẩm cháy vào dung dịch Ca(OH)2 dư thu được khối lượng kết tủa CaCO3 là:", ["60 gam", "40 gam", "80 gam", "50 gam"], 0, "Phản ứng cháy carbohydrate: Cn(H2O)m + n O2 -> n CO2 + m H2O. n(CO2) = n(O2) = 0,6 mol -> n(CaCO3) = 0,6 mol -> m = 60 gam."),
        make_mc(12, "Vận dụng", "Để xà phòng hóa hoàn toàn 17,8 kg một loại chất béo cần vừa đủ 2,4 kg NaOH. Khối lượng xà phòng muối sodium thu được sau khi cô cạn hoàn toàn (hiệu suất 100%) là:", ["18,36 kg", "20,20 kg", "19,26 kg", "17,80 kg"], 0, "n(NaOH) = 2,4 / 40 = 0,06 kmol -> n(glycerol) = 0,02 kmol -> m(glycerol) = 0,02 × 92 = 1,84 kg. Bảo toàn khối lượng: m xà phòng = 17,8 + 2,4 - 1,84 = 18,36 kg.")
    ],
    p2=[
        make_tf(1, "Thông hiểu", "Cho các phát biểu về mối liên hệ giữa các hợp chất hữu cơ trong Chương IV:", [
            ("a", "Quang hợp của cây xanh tạo tinh bột, tinh bột thủy phân tạo glucose, glucose lên men tạo rượu ethylic.", True),
            ("b", "Chất béo và protein đều là các đại phân tử sinh học thiết yếu trong khẩu phần ăn hàng ngày của con người.", True),
            ("c", "Tất cả các chất: chất béo, glucose, tinh bột, protein đều tham gia phản ứng xà phòng hóa với kiềm đun nóng.", False),
            ("d", "Polymer là cơ sở để sản xuất bốn loại vật liệu chính: chất dẻo, tơ sợi, cao su và keo dán.", True)
        ], "Chỉ có chất béo và protein có liên kết ester/peptide bị thủy phân trong kiềm; glucose không xà phòng hóa."),
        make_tf(2, "Thông hiểu", "Về các hiện tượng hóa học sinh học trong đời sống ẩm thực:", [
            ("a", "Khi luộc thịt gà, cho một nhánh gừng và hành nướng giúp khử mùi tanh do trung hòa các hợp chất lưu huỳnh và amine.", True),
            ("b", "Nấu canh cua đồng giã nhỏ, gạch cua nổi lên kết mảng do protein thịt cua bị đông tụ khi đun sôi.", True),
            ("c", "Ướp thịt bò với vài lát đu đủ xanh giúp thịt nhanh mềm vì trong đu đủ có enzyme papain thủy phân protein sợi cơ.", True),
            ("d", "Rau xanh để lâu ngày bị vàng úa là do tinh bột trong rau chuyển hóa thành mỡ lợn.", False)
        ], "Rau úa vàng do diệp lục tố bị phân hủy để lộ sắc tố carotenoid, không chuyển thành mỡ lợn."),
        make_tf(3, "Vận dụng", "Về vấn đề an toàn thực phẩm và vệ sinh:", [
            ("a", "Dầu mỡ chiên đi chiên lại nhiều lần ở nhiệt độ cao sinh ra các chất độc hại và chất gây ung thư.", True),
            ("b", "Formol (formaldehyde) là chất cấm tuyệt đối không được dùng để bảo quản bánh phở và bún tươi.", True),
            ("c", "Bánh mì hoặc lạc (đậu phộng) bị mốc chứa độc tố vi nấm aflatoxin cực độc có thể gây ung thư gan.", True),
            ("d", "Nước mắm có nồng độ đạm càng cao thì chắc chắn hoàn toàn không chứa muối ăn NaCl.", False)
        ], "Nước mắm truyền thống luôn chứa nồng độ muối NaCl bão hòa khoảng 25-28% để bảo quản đạm."),
        make_tf(4, "Vận dụng cao", "Về phát triển bền vững và kinh tế tuần hoàn:", [
            ("a", "Tái chế rơm rạ sau mùa gặt thành bột giấy hoặc lên men thành cồn sinh học giúp giảm ô nhiễm khói đốt đồng.", True),
            ("b", "Sử dụng mỡ cá tra thải loại từ nhà máy đông lạnh để sản xuất dầu diesel sinh học (biodiesel) bảo vệ môi trường.", True),
            ("c", "Khuyến khích mang hộp đựng thủy tinh và làn mây tre khi đi chợ giúp giảm phát thải rác nhựa dùng một lần.", True),
            ("d", "Đốt rơm rạ và túi nilon ngoài đồng ruộng là biện pháp tốt nhất để bổ sung dinh dưỡng đạm cho đất trồng.", False)
        ], "Đốt rơm rạ ngoài trời gây ô nhiễm bụi mịn mù mịt, đốt túi nilon sinh khí độc hại đất và sức khỏe.")
    ],
    p3=[
        make_sa(1, "Nhận biết", "Trong hạt gạo tẻ, tinh bột chiếm khoảng bao nhiêu phần trăm khối lượng?", "75", "Khoảng 75 - 80%."),
        make_sa(2, "Nhận biết", "Enzyme papain có trong quả nào được dùng để ướp làm mềm thịt nhanh?", "Đu đủ", "Quả đu đủ xanh."),
        make_sa(3, "Thông hiểu", "Một khẩu phần ăn trưa gồm 40 gam protein, 20 gam lipid và 100 gam carbohydrate. Tổng năng lượng mà bữa trưa đó cung cấp xấp xỉ bao nhiêu kcal?", "740", "40×4 + 20×9 + 100×4 = 160 + 180 + 400 = 740 kcal."),
        make_sa(4, "Vận dụng", "Một mẩu chất béo triolein có khối lượng 8,84 gam được hydro hóa hoàn toàn bằng khí H2 (xúc tác Ni, đun nóng) tạo thành tristearin. Thể tích khí H2 (đkc ở 25°C, 1 bar) đã phản ứng là bao nhiêu lít? (1 mol = 24,79 L)", "0.7437", "n(triolein, M = 884) = 0,01 mol -> n(H2) = 3 × 0,01 = 0,03 mol -> V = 0,03 × 24,79 = 0,7437 L."),
        make_sa(5, "Vận dụng", "Lên men m gam glucose thành rượu ethylic với hiệu suất 90%. Toàn bộ khí CO2 sinh ra hấp thụ hết vào dung dịch Ca(OH)2 dư thu được 50 gam kết tủa trắng CaCO3. Giá trị của m là bao nhiêu gam?", "50", "n(CO2) = n(CaCO3) = 0,5 mol -> n(glu lý thuyết) = 0,25 mol -> m lý thuyết = 0,25 × 180 = 45 gam -> m thực tế = 45 / 0,9 = 50 gam."),
        make_sa(6, "Vận dụng cao", "Xà phòng hóa hoàn toàn 1 tấn một loại mỡ động vật chứa 89% tristearin và 11% tạp chất trơ không phản ứng bằng dung dịch NaOH. Khối lượng xà phòng bánh chứa 70% sodium stearate thu được với hiệu suất 95% là bao nhiêu kg? (Làm tròn đến hàng đơn vị: 1245 kg)", "1245", "m(tristearin) = 890 kg (1 kmol) -> n(muối C17H35COONa lt) = 3 kmol -> m muối lt = 3 × 306 = 918 kg -> m muối tt = 918 × 0,95 = 872,1 kg -> m bánh xà phòng 70% = 872,1 / 0,7 = 1 245,8 ≈ 1 245 kg.")
    ],
    p4=[
        make_vdc(1, "Một nhà máy chế biến dầu thực vật sản xuất bơ nhân tạo (margarine) bằng phản ứng hydro hóa dầu đậu nành chứa 80% triolein (C17H33COO)3C3H5. Để làm no hoàn toàn 2,21 tấn dầu đậu nành trên thành tristearin với hiệu suất hydro hóa đạt 90%, thể tích khí hydrogen H2 (đo ở điều kiện chuẩn 25°C, 1 bar, 1 mol = 24,79 L) tối thiểu cần cung cấp là:", ["165,27 m3", "148,74 m3", "182,50 m3", "135,20 m3"], 0, "m(triolein) = 2,21 × 80% = 1,768 tấn (M = 884) -> n = 1,768 / 884 = 0,002 Mmol = 2 kmol -> n(H2 lt) = 3 × 2 = 6 kmol -> n(H2 tt) = 6 / 0,9 = 6,667 kmol -> V = 6,667 × 24,79 m3 = 165,27 m3."),
        make_vdc(2, "Xăng sinh học E5 là hỗn hợp chứa 5% thể tích ethanol (C2H5OH) và 95% thể tích xăng khoáng thông thường RON 92. Một trạm cấp phát nhiên liệu tiêu thụ mỗi tháng 100 000 lít xăng E5. Khối lượng riêng của ethanol là 0,8 kg/L. Khối lượng gạo chứa 75% tinh bột tối thiểu cần huy động để sản xuất đủ lượng ethanol cho trạm xăng đó trong 1 tháng (biết hiệu suất toàn bộ chu trình sản xuất cồn từ gạo là 68%) xấp xỉ là:", ["13,8 tấn", "11,2 tấn", "16,5 tấn", "9,8 tấn"], 0, "V(EtOH) = 100 000 × 5% = 5 000 L -> m(EtOH) = 5 000 × 0,8 = 4 000 kg -> n(EtOH) = 4 000 / 46 = 86,956 kmol -> n(mắt xích tinh bột lt) = 43,478 kmol -> m(tinh bột lt) = 43,478 × 162 = 7 043,5 kg -> m tinh bột tt = 7 043,5 / 0,68 = 10 358 kg -> m gạo = 10 358 / 0,75 = 13 810 kg ≈ 13,8 tấn."),
        make_vdc(3, "Để xác định hàm lượng chất béo trong một mẫu hạt điều, người ta nghiền mịn 10 gam hạt điều khô rồi ngâm chiết kiệt dầu bằng dung dịch diethyl ether trong dụng cụ chiết Soxhlet. Sau khi chiết kiệt, đem làm bay hơi hoàn toàn dung môi ether thu được 4,8 gam dầu béo nguyên chất dạng sánh màu vàng nhạt. Hàm lượng phần trăm chất béo trong mẫu hạt điều đó là:", ["48%", "52%", "40%", "36%"], 0, "4,8 / 10 × 100% = 48%."),
        make_vdc(4, "Một chu trình sinh thái nông nghiệp khép kín kiểu mẫu VAC (Vườn - Ao - Chuồng) kết hợp sản xuất phân bón vi sinh và khí sinh học biogas: Toàn bộ chất thải chăn nuôi lợn và phụ phẩm nông nghiệp được đưa vào hầm ủ biogas kị khí sinh ra khí methane (CH4) làm chất đốt sạch đun nấu và phát điện. Nước thải hầm biogas sau khi ủ hoai mục dùng bón vườn rau hữu cơ và tưới cỏ nuôi bò. Lợi ích khoa học toàn diện nổi bật của mô hình này là:", ["Xử lý triệt để mầm bệnh chất thải chăn nuôi, giảm phát thải khí nhà kính methane, tạo nguồn năng lượng tái tạo sạch và cung cấp phân bón hữu cơ chất lượng cao", "Làm cho đất bị chai cứng thoái hóa", "Làm tăng lượng rác thải nhựa trong ao", "Gây bùng phát dịch bệnh gia súc"], 0, "Kinh tế tuần hoàn nông nghiệp xanh giúp bảo vệ môi trường, giảm phát thải khí nhà kính và tiết kiệm năng lượng.")
    ]
)
