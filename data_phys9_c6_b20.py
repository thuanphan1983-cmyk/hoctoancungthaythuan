# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 20: THỰC HÀNH XÁC ĐỊNH TIÊU CỰ CỦA THẤU KÍNH HỘI TỤ
Bao gồm 3 đề thi độc lập 100%: phys9_c6_b20_test1, phys9_c6_b20_test2, phys9_c6_b20_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c6"
CH_TITLE = "Chương VI: Ánh sáng"

# =============================================================================
# BÀI 20: THỰC HÀNH XÁC ĐỊNH TIÊU CỰ CỦA THẤU KÍNH HỘI TỤ (3 ĐỀ)
# =============================================================================

# --- phys9_c6_b20_test1 ---
p1_b20_t1 = [
    make_mc(1, "Nhận biết", "Trong bộ dụng cụ thí nghiệm thực hành xác định tiêu cự của thấu kính hội tụ, dụng cụ nào dùng để hứng hình ảnh của vật sáng?", [
        "Màn chắn có màu trắng đục",
        "Gương phẳng tráng bạc",
        "Thước kẹp cơ khí",
        "Lăng kính tam giác"
    ], 0, "Màn chắn trắng đục dùng để hứng và quan sát ảnh thật."),
    make_mc(2, "Nhận biết", "Vật sáng thường được sử dụng trong thí nghiệm thực hành đo tiêu cự thấu kính hội tụ là:", [
        "Tấm chắn có khoét chữ F hoặc hình mũi tên đặt sát trước nguồn sáng",
        "Một hòn sỏi tròn",
        "Một chiếc gương cầu lõm",
        "Một cuộn dây đồng"
    ], 0, "Tấm khoét chữ F hoặc mũi tên giúp dễ quan sát chiều và độ sắc nét của ảnh."),
    make_mc(3, "Nhận biết", "Phương pháp Silbermann để xác định tiêu cự của thấu kính hội tụ dựa trên tính chất khi vật và màn đặt ở vị trí:", [
        "d = d' = 2f (ảnh thật bằng vật)",
        "d = f (ảnh ở vô cực)",
        "d = 0,5f (ảnh ảo gấp đôi vật)",
        "d = 3f (ảnh thật bằng một phần ba vật)"
    ], 0, "Phương pháp Silbermann dùng tính chất d = d' = 2f để đo f = (d + d') / 4."),
    make_mc(4, "Nhận biết", "Để kết quả đo tiêu cự thấu kính hội tụ chính xác nhất, các dụng cụ (nguồn sáng, vật, thấu kính, màn hứng) trên giá quang học phải:", [
        "Có tâm nằm trên cùng một đường thẳng song song với giá quang học (đồng trục)",
        "Đặt sole lệch nhau càng xa càng tốt",
        "Đặt nghiêng các góc 45 độ so với trục chính",
        "Xoay liên tục trong khi đo"
    ], 0, "Các tâm phải cùng nằm trên trục chính để ảnh rõ nét, không bị méo lệch."),
    make_mc(5, "Nhận biết", "Khi dùng ánh sáng mặt trời chiếu vào thấu kính hội tụ để đo tiêu cự sơ bộ, tiêu cự của thấu kính xấp xỉ bằng:", [
        "Khoảng cách từ thấu kính đến điểm sáng hội tụ gom nhỏ nhất trên tờ giấy hứng",
        "Đường kính của vành thấu kính",
        "Hai lần khoảng cách từ thấu kính đến tờ giấy",
        "Bề dày của phần giữa thấu kính"
    ], 0, "Ánh sáng mặt trời là chùm song song nên hội tụ tại tiêu điểm F', f bằng khoảng cách từ thấu kính đến điểm sáng nhỏ nhất."),
    make_mc(6, "Nhận biết", "Trong thí nghiệm, công thức liên hệ giữa khoảng cách từ vật đến thấu kính (d), khoảng cách từ thấu kính đến ảnh (d') và tiêu cự (f) là:", [
        "1/f = 1/d + 1/d'",
        "f = d + d'",
        "f = d × d'",
        "1/f = 1/d - 1/d'"
    ], 0, "Công thức thấu kính hội tụ cho ảnh thật: 1/f = 1/d + 1/d'."),
    make_mc(7, "Thông hiểu", "Trong thí nghiệm đo tiêu cự bằng phương pháp ảnh thật bằng vật, người ta đo được khoảng cách từ vật sáng đến màn hứng ảnh là L = 48 cm. Tiêu cự f của thấu kính là:", [
        "12 cm",
        "24 cm",
        "48 cm",
        "6 cm"
    ], 0, "Khoảng cách ngắn nhất giữa vật và màn khi ảnh bằng vật là L = 4f => f = L / 4 = 48 / 4 = 12 cm."),
    make_mc(8, "Thông hiểu", "Khi làm thí nghiệm với thấu kính hội tụ, bạn An dịch chuyển màn chắn dọc giá quang học nhưng không thể tìm thấy ảnh rõ nét của vật trên màn. Nguyên nhân có thể là:", [
        "Vật sáng đặt trong khoảng tiêu cự của thấu kính (d < f) nên tạo ảnh ảo",
        "Phòng thí nghiệm quá nhiều gió",
        "Màn chắn làm bằng bìa màu trắng",
        "Thước đo bị cong"
    ], 0, "Khi d < f, thấu kính cho ảnh ảo nên không hứng được trên màn chắn."),
    make_mc(9, "Thông hiểu", "Để giảm sai số ngẫu nhiên trong bài thực hành đo tiêu cự, học sinh cần thực hiện biện pháp nào?", [
        "Thực hiện đo lặp lại nhiều lần (ít nhất 3 đến 5 lần) rồi tính giá trị trung bình",
        "Chỉ đo một lần duy nhất thật nhanh",
        "Đo bằng nhiều cây thước nhựa khác nhau cùng lúc",
        "Tăng độ sáng của đèn lên mức tối đa có thể"
    ], 0, "Đo lặp lại nhiều lần và lấy giá trị trung bình là nguyên tắc giảm sai số ngẫu nhiên."),
    make_mc(10, "Thông hiểu", "Trong thí nghiệm, khi cố định khoảng cách giữa vật và màn là L = 80 cm, người ta tìm được hai vị trí đặt thấu kính đều cho ảnh rõ nét trên màn. Đây là phương pháp đo tiêu cự nổi tiếng có tên gọi là:", [
        "Phương pháp Bessel",
        "Phương pháp Newton",
        "Phương pháp Ohm",
        "Phương pháp Joule"
    ], 0, "Phương pháp Bessel đo tiêu cự dựa trên hai vị trí của thấu kính cho ảnh rõ nét trên màn cố định."),
    make_mc(11, "Thông hiểu", "Một nhóm học sinh đo khoảng cách từ vật đến thấu kính d = 30 cm thì thu được ảnh rõ nét trên màn cách thấu kính d' = 60 cm. Tiêu cự của thấu kính đo được là:", [
        "20 cm",
        "90 cm",
        "45 cm",
        "15 cm"
    ], 0, "1/f = 1/30 + 1/60 = 3/60 = 1/20 => f = 20 cm."),
    make_mc(12, "Thông hiểu", "Sau khi kết thúc buổi thực hành quang học, thao tác an toàn và bảo quản thiết bị đúng quy chuẩn là:", [
        "Tắt nguồn điện cấp cho đèn chiếu sáng, để nguội đèn rồi cất cẩn thận thấu kính vào hộp xốp chống trầy xước",
        "Rút phích cắm mạnh tay khi đèn đang nóng rực",
        "Lau bề mặt thấu kính bằng giấy nhám kim loại",
        "Để nguyên đèn sáng và ra về"
    ], 0, "Tắt nguồn đèn, để nguội và cất thấu kính cẩn thận vào hộp chống trầy xước.")
]

p2_b20_t1 = [
    make_tf(1, "Thông hiểu", "Xét các bước chuẩn bị thí nghiệm thực hành đo tiêu cự thấu kính hội tụ:", [
        ("a", "Giá quang học phải được đặt nằm ngang thăng bằng trên bàn thí nghiệm.", True),
        ("b", "Nguồn sáng, vật sáng chữ F, thấu kính và màn chắn phải được gắn chắc chắn trên các con trượt.", True),
        ("c", "Chiều cao tâm quang học của thấu kính phải bằng chiều cao tâm vật sáng và tâm màn hứng.", True),
        ("d", "Bắt buộc phải tiến hành thí nghiệm dưới ánh sáng mặt trời gay gắt ngoài trời.", False)
    ], "Thí nghiệm thường làm trong phòng học tối hoặc che bớt ánh sáng môi trường để ảnh rõ nét."),
    make_tf(2, "Thông hiểu", "Phương pháp Silbermann xác định tiêu cự thấu kính hội tụ:", [
        ("a", "Dựa trên tính chất khi d = 2f thì d' = 2f và kích thước ảnh bằng kích thước vật.", True),
        ("b", "Khoảng cách giữa vật và màn hứng khi đó là L = d + d' = 4f.", True),
        ("c", "Ảnh thu được trên màn trong phương pháp này là ảnh ảo cùng chiều với vật.", False),
        ("d", "Tiêu cự được tính theo công thức f = L / 4.", True)
    ], "Ảnh thu được trên màn là ảnh thật, ngược chiều với vật."),
    make_tf(3, "Vận dụng", "Bảng kết quả đo khoảng cách vật và màn (d + d') của một nhóm học sinh khi ảnh thật bằng vật qua 3 lần đo lần lượt là: L1 = 40,2 cm; L2 = 39,8 cm; L3 = 40,0 cm:", [
        ("a", "Giá trị trung bình khoảng cách vật - màn là L_tb = 40,0 cm.", True),
        ("b", "Tiêu cự trung bình của thấu kính hội tụ là f_tb = 10,0 cm.", True),
        ("c", "Sai số tuyệt đối của lần đo thứ nhất là 0,2 cm.", True),
        ("d", "Nếu thấu kính bị nứt vỡ thì tiêu cự đo được không thay đổi.", False)
    ], "L_tb = (40,2 + 39,8 + 40,0) / 3 = 40,0 cm => f_tb = 40,0 / 4 = 10,0 cm. Sai số ΔL1 = |40,2 - 40,0| = 0,2 cm."),
    make_tf(4, "Vận dụng", "Trong thí nghiệm đo tiêu cự, khi dịch chuyển vật từ d = 2f ra xa thấu kính (d > 2f):", [
        ("a", "Để hứng được ảnh rõ nét, màn chắn phải được dịch chuyển lại gần thấu kính hơn.", True),
        ("b", "Kích thước ảnh thật thu được trên màn ngày càng nhỏ hơn vật.", True),
        ("c", "Độ sáng của ảnh thu được ngày càng tăng lên.", False),
        ("d", "Khoảng cách từ thấu kính đến màn d' luôn lớn hơn tiêu cự f và nhỏ hơn 2f.", True)
    ], "Khi d > 2f thì f < d' < 2f, ảnh nhỏ dần và độ rọi sáng phân tán.")
]

p3_b20_t1 = [
    make_sa(1, "Thông hiểu", "Trong thí nghiệm đo tiêu cự theo phương pháp Silbermann, khi ảnh thật bằng vật thì khoảng cách giữa vật và màn gấp mấy lần tiêu cự?", "4", "L = 4f."),
    make_sa(2, "Thông hiểu", "Khi đo tiêu cự sơ bộ bằng ánh sáng mặt trời, điểm hội tụ nhỏ nhất trên màn chắn cách thấu kính 14 cm. Tiêu cự thấu kính là bao nhiêu cm?", "14", "f = 14 cm."),
    make_sa(3, "Vận dụng", "Khoảng cách giữa vật sáng và màn hứng ảnh đo được là L = 60 cm khi ảnh thật ngược chiều bằng vật. Tiêu cự f của thấu kính bằng bao nhiêu cm?", "15", "f = L / 4 = 60 / 4 = 15 cm."),
    make_sa(4, "Vận dụng", "Học sinh đo khoảng cách từ vật đến thấu kính d = 25 cm và từ thấu kính đến màn d' = 25 cm khi ảnh rõ nét bằng vật. Tiêu cự thấu kính bằng bao nhiêu cm? (Lấy số thập phân)", "12.5", "d = 2f = 25 cm => f = 12,5 cm."),
    make_sa(5, "Vận dụng cao", "Trong thí nghiệm xác định tiêu cự, khoảng cách từ vật đến thấu kính là d = 20 cm, khoảng cách từ thấu kính đến ảnh thật là d' = 30 cm. Tiêu cự f của thấu kính bằng bao nhiêu cm?", "12", "f = (d × d') / (d + d') = (20 × 30) / (20 + 30) = 600 / 50 = 12 cm."),
    make_sa(6, "Vận dụng cao", "Một học sinh đo tiêu cự qua 3 lần đo được các giá trị f1 = 15,2 cm; f2 = 14,8 cm; f3 = 15,0 cm. Giá trị tiêu cự trung bình của thấu kính là bao nhiêu cm?", "15", "f_tb = (15,2 + 14,8 + 15,0) / 3 = 15,0 cm.")
]

p4_b20_t1 = [
    make_vdc(1, "Khi tiến hành thí nghiệm đo tiêu cự của thấu kính hội tụ, nếu dùng một tấm bìa đen che khuất nửa phần trên của thấu kính thì hình ảnh ngọn nến trên màn chắn sẽ thay đổi như thế nào?", [
        "Hình ảnh ngọn nến vẫn còn đầy đủ nguyên vẹn nhưng độ sáng của ảnh bị giảm đi một nửa",
        "Chỉ còn nhìn thấy nửa phần dưới của ngọn nến",
        "Chỉ còn nhìn thấy nửa phần trên của ngọn nến",
        "Hình ảnh ngọn nến biến mất hoàn toàn"
    ], 0, "Mỗi phần của thấu kính đều cho ảnh hoàn chỉnh của vật. Che nửa trên thì ánh sáng qua thấu kính giảm đi một nửa làm ảnh tối đi nhưng vẫn đầy đủ."),
    make_vdc(2, "Trong phương pháp Bessel xác định tiêu cự thấu kính hội tụ, người ta giữ cố định khoảng cách giữa vật và màn là L = 100 cm. Khi dịch chuyển thấu kính dọc theo khoảng giữa vật và màn, có hai vị trí của thấu kính cho ảnh rõ nét trên màn cách nhau một khoảng e = 20 cm. Công thức Bessel tính tiêu cự là f = (L^2 - e^2) / (4L). Tiêu cự của thấu kính đo được là:", [
        "24 cm",
        "25 cm",
        "20 cm",
        "15 cm"
    ], 0, "f = (100^2 - 20^2) / (4 × 100) = (10000 - 400) / 400 = 9600 / 400 = 24 cm."),
    make_vdc(3, "Để đo tiêu cự của một thấu kính phân kì trong phòng thí nghiệm (vốn không tạo được ảnh thật trên màn), các bạn học sinh đã nghĩ ra giải pháp ghép thấu kính phân kì sát với một thấu kính hội tụ bổ trợ có tiêu cự f1 đã biết (với |f_phân_kì| > f1). Bản chất của giải pháp này là:", [
        "Tạo ra một hệ thấu kính ghép tương đương có tính chất hội tụ để đo được tiêu cự hệ, từ đó suy ra tiêu cự thấu kính phân kì",
        "Biến thấu kính phân kì thành gương phẳng",
        "Làm tăng độ cong của thấu kính phân kì",
        "Loại bỏ hoàn toàn hiện tượng khúc xạ ánh sáng"
    ], 0, "Ghép TKPK với TKHT mạnh hơn để hệ là hội tụ (1/f_hệ = 1/f1 + 1/f2 > 0), đo f_hệ rồi tính ra f2 của TKPK."),
    make_vdc(4, "Một nhóm học sinh làm thí nghiệm đo tiêu cự nhưng quên ghi lại khoảng cách d và d', chỉ nhớ rằng khoảng cách từ vật đến màn là L = 90 cm và ảnh thật trên màn cao gấp đôi vật sáng. Tiêu cự f của thấu kính này là:", [
        "20 cm",
        "30 cm",
        "15 cm",
        "45 cm"
    ], 0, "k = d'/d = 2 => d' = 2d. L = d + d' = 3d = 90 cm => d = 30 cm, d' = 60 cm. 1/f = 1/30 + 1/60 = 1/20 => f = 20 cm.")
]

exams["phys9_c6_b20_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b20", "Bài 20: Thực hành xác định tiêu cự của thấu kính hội tụ", 1, p1_b20_t1, p2_b20_t1, p3_b20_t1, p4_b20_t1)

# --- phys9_c6_b20_test2 ---
p1_b20_t2 = [
    make_mc(1, "Nhận biết", "Dụng cụ đóng vai trò làm trục tọa độ định hướng và đo khoảng cách giữa các phần tử trong bài thực hành quang học là:", [
        "Giá quang học có gắn thước chia milimét",
        "Bình chia độ chất lỏng",
        "Lực kế lò xo",
        "Nhiệt kế điện tử"
    ], 0, "Giá quang học có thước chia giúp đọc trực tiếp vị trí các linh kiện quang học."),
    make_mc(2, "Nhận biết", "Khi quan sát ảnh của chữ F trên màn chắn qua thấu kính hội tụ trong điều kiện d = 2f, ảnh chữ F thu được có đặc điểm:", [
        "Bị lộn ngược đầu xuống dưới và quay sang trái",
        "Hoàn toàn xuôi chiều như chữ F ban đầu",
        "Biến thành hình tròn đặc",
        "Mất nét thẳng đứng chỉ còn nét ngang"
    ], 0, "Ảnh thật qua thấu kính hội tụ bị ngược chiều cả trên dưới và trái phải."),
    make_mc(3, "Nhận biết", "Khoảng cách ngắn nhất giữa một vật thật và ảnh thật của nó qua một thấu kính hội tụ có tiêu cự f là:", [
        "L_min = 4f",
        "L_min = 2f",
        "L_min = f",
        "L_min = 0,5f"
    ], 0, "Khoảng cách vật - ảnh thật ngắn nhất đạt được khi d = d' = 2f, lúc đó L_min = 4f."),
    make_mc(4, "Nhận biết", "Để xác định vị trí ảnh rõ nét nhất trên màn hứng ảnh, thao tác chuẩn xác của học sinh là:", [
        "Dịch chuyển màn chắn chậm rãi qua lại quanh vị trí ảnh cho đến khi viền ảnh sắc nét nhất",
        "Đẩy màn chắn thật mạnh từ đầu giá đến cuối giá",
        "Giữ cố định màn và rung lắc nhẹ thấu kính",
        "Quan sát bằng kính râm sẫm màu"
    ], 0, "Dịch chuyển từ từ qua lại để xác định đúng vị trí mép ảnh sắc nét nhất."),
    make_mc(5, "Nhận biết", "Đơn vị đo tiêu cự thông dụng trong phòng thí nghiệm trường học là:", [
        "Xentimét (cm) hoặc milimét (mm)",
        "Lít (L)",
        "Giây (s)",
        "Ampe (A)"
    ], 0, "Tiêu cự là độ dài, đo bằng cm hoặc mm."),
    make_mc(6, "Nhận biết", "Nếu khoảng cách giữa vật và màn chắn nhỏ hơn 4 lần tiêu cự (L < 4f) thì:", [
        "Không thể thu được ảnh thật của vật trên màn chắn ở bất kỳ vị trí nào của thấu kính",
        "Thu được hai ảnh thật cùng lúc",
        "Ảnh thật luôn lớn hơn vật",
        "Thấu kính tự động phát sáng"
    ], 0, "Điều kiện để có ảnh thật trên màn là L ≥ 4f. Nếu L < 4f thì không thể hứng được ảnh thật."),
    make_mc(7, "Thông hiểu", "Trong thí nghiệm đo tiêu cự, một học sinh đặt vật cách thấu kính d = 40 cm và đo được khoảng cách từ thấu kính đến màn d' = 40 cm khi ảnh nét rõ. Tiêu cự của thấu kính là:", [
        "20 cm",
        "40 cm",
        "80 cm",
        "10 cm"
    ], 0, "Vì d = d' = 40 cm nên d = 2f => f = 40 / 2 = 20 cm."),
    make_mc(8, "Thông hiểu", "Một nhóm học sinh đo được khoảng cách vật - màn là L = 72 cm khi kích thước ảnh bằng kích thước vật. Tiêu cự thấu kính là:", [
        "18 cm",
        "36 cm",
        "72 cm",
        "9 cm"
    ], 0, "f = L / 4 = 72 / 4 = 18 cm."),
    make_mc(9, "Thông hiểu", "Khi làm thí nghiệm với nguồn sáng đèn sợi đốt, sau một thời gian bóng đèn rất nóng. Quy tắc an toàn thí nghiệm nhắc nhở học sinh:", [
        "Không dùng tay chạm trực tiếp vào vỏ kim loại của đèn đang nóng để tránh bị bỏng",
        "Đổ nước lạnh trực tiếp lên bóng đèn đang sáng để làm mát",
        "Dùng giấy gói kín bóng đèn lại",
        "Thổi hơi cồn vào đèn"
    ], 0, "Đèn sợi đốt tỏa nhiệt cao, chạm vào dễ bị bỏng nên không chạm trực tiếp."),
    make_mc(10, "Thông hiểu", "Khi dịch chuyển thấu kính lại gần vật sáng (với f < d < 2f), để tiếp tục hứng được ảnh rõ nét trên màn, học sinh phải:", [
        "Dịch chuyển màn hứng ra xa thấu kính hơn",
        "Dịch chuyển màn hứng lại gần thấu kính hơn",
        "Giữ nguyên màn hứng ở vị trí cũ",
        "Tháo màn chắn ra ngoài"
    ], 0, "Khi d giảm (tiến về f) thì d' tăng (tiến về vô cực), do đó màn phải dời ra xa thấu kính."),
    make_mc(11, "Thông hiểu", "Trong thí nghiệm đo tiêu cự bằng phương pháp đo d và d', công thức tính tiêu cự f là:", [
        "f = (d × d') / (d + d')",
        "f = (d + d') / (d × d')",
        "f = d + d'",
        "f = d - d'"
    ], 0, "1/f = 1/d + 1/d' => f = (d × d') / (d + d')."),
    make_mc(12, "Thông hiểu", "Một bạn học sinh đặt thấu kính hội tụ lệch trục so với vật sáng (trục thấu kính không song song với trục giá quang học). Hiện tượng quan sát được trên màn là:", [
        "Ảnh bị méo dạng và mép ảnh bị mờ nhòe không đều",
        "Ảnh biến thành màu đen trắng hoàn hảo",
        "Không có bất kỳ ánh sáng nào qua thấu kính",
        "Ảnh vẫn sắc nét như khi đặt đồng trục"
    ], 0, "Lệch trục gây quang sai làm ảnh bị méo mó và nhòe mép.")
]

p2_b20_t2 = [
    make_tf(1, "Thông hiểu", "Về cấu tạo giá quang học thí nghiệm Vật lý 9:", [
        ("a", "Thước đo gắn trên giá quang học thường có độ chia nhỏ nhất là 1 mm.", True),
        ("b", "Các đế trượt cho phép di chuyển các bộ phận dọc theo chiều dài giá dễ dàng.", True),
        ("c", "Vật sáng, thấu kính và màn chắn có thể xoay tự do nghiêng ngả mà không ảnh hưởng kết quả đo.", False),
        ("d", "Khóa hãm trên đế trượt dùng để cố định vị trí các linh kiện khi đọc số đo.", True)
    ], "Các linh kiện phải được chỉnh vuông góc với giá quang học và đồng trục chính để tránh sai số."),
    make_tf(2, "Thông hiểu", "Các yếu tố ảnh hưởng đến độ chính xác của phép đo tiêu cự:", [
        ("a", "Độ sắc nét của hình ảnh quan sát bằng mắt của người làm thí nghiệm.", True),
        ("b", "Độ chính xác khi đọc vạch chia milimét trên giá quang học.", True),
        ("c", "Màu sắc của lớp sơn trên thân giá quang học.", False),
        ("d", "Sự đồng trục giữa nguồn sáng, vật sáng, thấu kính và màn chắn.", True)
    ], "Màu sơn giá không ảnh hưởng đến độ chính xác quang học."),
    make_tf(3, "Vận dụng", "Học sinh đo khoảng cách từ thấu kính đến màn d' khi d = 30 cm trong 3 lần đo được kết quả: 59,5 cm; 60,5 cm; 60,0 cm:", [
        ("a", "Giá trị d' trung bình là 60,0 cm.", True),
        ("b", "Tiêu cự tính từ giá trị trung bình d = 30 cm và d'_tb = 60 cm là f = 20 cm.", True),
        ("c", "Ảnh thu được trên màn nhỏ hơn vật sáng.", False),
        ("d", "Độ phóng đại của ảnh trong trường hợp này bằng 2.", True)
    ], "d' = 60 cm > d = 30 cm nên k = d'/d = 2, ảnh lớn gấp 2 lần vật sáng."),
    make_tf(4, "Vận dụng", "Khi thực hành phương pháp Silbermann với thấu kính có tiêu cự f = 15 cm:", [
        ("a", "Khoảng cách ngắn nhất giữa vật và màn để có ảnh thật là 60 cm.", True),
        ("b", "Khi khoảng cách vật - màn là 50 cm thì vẫn tìm được 2 vị trí đặt thấu kính cho ảnh thật.", False),
        ("c", "Khi vật và màn cách nhau 60 cm thì chỉ có duy nhất 1 vị trí đặt thấu kính cho ảnh rõ nét.", True),
        ("d", "Tại vị trí d = 30 cm thì ảnh thật ngược chiều và bằng vật.", True)
    ], "L_min = 4f = 60 cm. Khi L = 50 cm < 60 cm thì không thể có ảnh thật trên màn.")
]

p3_b20_t2 = [
    make_sa(1, "Thông hiểu", "Để xác định tiêu cự của thấu kính hội tụ theo phương pháp Silbermann, học sinh cần điều chỉnh khoảng cách d và d' sao cho tỉ số d'/d bằng bao nhiêu?", "1", "Khi d = d' thì d'/d = 1."),
    make_sa(2, "Thông hiểu", "Khi di chuyển màn hứng ảnh trên giá quang học, khoảng cách giữa vật và màn đạt giá trị tối thiểu là 80 cm để có ảnh rõ nét. Tiêu cự của thấu kính là bao nhiêu cm?", "20", "L_min = 4f = 80 cm => f = 20 cm."),
    make_sa(3, "Vận dụng", "Học sinh đo được d = 36 cm và d' = 36 cm khi ảnh chữ F trên màn rõ nét và bằng chữ F thật. Tiêu cự thấu kính là bao nhiêu cm?", "18", "f = d / 2 = 36 / 2 = 18 cm."),
    make_sa(4, "Vận dụng", "Trong một bài thực hành, vật cách thấu kính d = 50 cm, thấu kính cách màn d' = 50 cm. Khoảng cách giữa vật và màn bằng bao nhiêu cm?", "100", "L = d + d' = 50 + 50 = 100 cm."),
    make_sa(5, "Vận dụng cao", "Khoảng cách từ vật đến màn là L = 100 cm. Thấu kính đặt cách vật d = 20 cm thì cho ảnh rõ nét trên màn. Tiêu cự của thấu kính là bao nhiêu cm?", "16", "d = 20 cm => d' = L - d = 80 cm. f = (20 × 80) / (20 + 80) = 1600 / 100 = 16 cm."),
    make_sa(6, "Vận dụng cao", "Một nhóm học sinh đo tiêu cự bằng phương pháp đo d và d' thu được d = 24 cm, d' = 48 cm. Tiêu cự của thấu kính là bao nhiêu cm?", "16", "f = (24 × 48) / (24 + 48) = 1152 / 72 = 16 cm.")
]

p4_b20_t2 = [
    make_vdc(1, "Một nhóm học sinh làm thí nghiệm thực hành xác định tiêu cự của thấu kính hội tụ. Khi chỉnh cho ảnh thật rõ nét trên màn, một bạn vô tình dùng ngón tay chạm vào bề mặt thấu kính để lại một dấu vân tay nhờn. Hiện tượng nào sau đây phản ánh chính xác nhất ảnh hưởng của dấu vân tay đến ảnh trên màn?", [
        "Ảnh trên màn vẫn nguyên vẹn hình dáng chữ F nhưng độ sáng tổng thể giảm nhẹ và có thể hơi mờ ở vị trí tương ứng",
        "Ảnh chữ F lập tức bị biến dạng thành hình dấu vân tay",
        "Ảnh chữ F bị thủng một lỗ tròn ở chính giữa",
        "Ảnh bị mất hoàn toàn màu sắc biến thành vệt sáng trắng"
    ], 0, "Dấu vân tay chỉ chặn một phần nhỏ ánh sáng qua thấu kính, ảnh vẫn hình thành đầy đủ nhưng giảm nhẹ độ tương phản và độ sáng."),
    make_vdc(2, "Trong phòng thí nghiệm quang học, nguồn sáng chữ F được bật sáng. Thấu kính hội tụ có tiêu cự f = 15 cm đặt cách chữ F một khoảng d = 20 cm. Phía sau thấu kính, màn chắn được đặt ở vị trí cách thấu kính d' = 60 cm thì thu được ảnh rõ nét. Nếu dời màn chắn lại gần thấu kính một đoạn 20 cm (còn cách thấu kính 40 cm) thì vệt sáng trên màn sẽ như thế nào?", [
        "Vệt sáng bị mờ nhòe, không còn là ảnh rõ nét của chữ F",
        "Ảnh chữ F càng trở nên sắc nét hơn",
        "Ảnh chữ F bị thu nhỏ lại bằng một nửa",
        "Vệt sáng biến mất hoàn toàn"
    ], 0, "Vị trí ảnh nét duy nhất là d' = 60 cm. Khi dời màn về 40 cm, các chùm tia chưa hội tụ hoàn toàn nên tạo vệt nhòe."),
    make_vdc(3, "Để đo tiêu cự của một thấu kính hội tụ có tiêu cự khá lớn (khoảng 50 cm) nhưng giá quang học của phòng thí nghiệm chỉ dài 100 cm (ngắn hơn 4f = 200 cm), học sinh KHÔNG THỂ sử dụng phương pháp nào sau đây trên giá quang học này?", [
        "Phương pháp Silbermann (yêu cầu khoảng cách vật - màn tối thiểu L = 4f = 200 cm)",
        "Phương pháp dùng chùm tia sáng song song hội tụ tại tiêu điểm",
        "Phương pháp tạo ảnh ảo quan sát qua kính lúp",
        "Phương pháp phản xạ qua gương phẳng phụ trợ"
    ], 0, "Phương pháp Silbermann đòi hỏi L ≥ 4f = 200 cm, giá 100 cm không đủ độ dài để hứng ảnh thật bằng vật."),
    make_vdc(4, "Một thấu kính hội tụ mỏng được dùng trong bài thực hành quang học. Khi chiếu một chùm sáng laser đỏ song song trục chính thì đo được tiêu cự là f_đỏ = 20,2 cm. Nếu thay chùm laser đỏ bằng chùm laser tím song song trục chính thì tiêu cự f_tím đo được sẽ:", [
        "Nhỏ hơn 20,2 cm một chút do thủy tinh chiết quang mạnh hơn đối với ánh sáng tím",
        "Lớn hơn 20,2 cm rất nhiều",
        "Hoàn toàn bằng 20,2 cm vì tiêu cự là đại lượng cố định của thấu kính",
        "Bằng 0 cm vì ánh sáng tím bị hấp thụ hoàn toàn"
    ], 0, "Hiện tượng sắc sai: Chiết suất của thủy tinh đối với ánh sáng tím lớn hơn ánh sáng đỏ (n_tím > n_đỏ) nên ánh sáng tím bị bẻ gãy mạnh hơn, tiêu cự f_tím < f_đỏ.")
]

exams["phys9_c6_b20_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b20", "Bài 20: Thực hành xác định tiêu cự của thấu kính hội tụ", 2, p1_b20_t2, p2_b20_t2, p3_b20_t2, p4_b20_t2)

# --- phys9_c6_b20_test3 ---
p1_b20_t3 = [
    make_mc(1, "Nhận biết", "Trong thí nghiệm thực hành đo tiêu cự thấu kính hội tụ, điều kiện để có ảnh thật sắc nét trên màn chắn là:", [
        "Vật sáng phải đặt ngoài khoảng tiêu cự của thấu kính (d > f)",
        "Vật sáng phải đặt sát vào quang tâm O",
        "Vật sáng đặt trong khoảng tiêu cự (d < f)",
        "Khoảng cách vật đến thấu kính phải bằng 0"
    ], 0, "Muốn thu được ảnh thật trên màn thì d > f."),
    make_mc(2, "Nhận biết", "Độ phóng đại k của ảnh thật thu được trên màn trong thí nghiệm quang học được xác định bằng tỉ số:", [
        "k = A'B' / AB = d' / d",
        "k = AB / A'B'",
        "k = f / d",
        "k = (d + d') / f"
    ], 0, "Độ phóng đại ảnh thật k = chiều cao ảnh / chiều cao vật = d' / d."),
    make_mc(3, "Nhận biết", "Vật sáng chữ F có ưu điểm nổi bật hơn vật sáng dạng chấm tròn khi làm thí nghiệm là:", [
        "Giúp phân biệt rõ ràng chiều trên - dưới và chiều trái - phải của ảnh so với vật",
        "Phát sáng mạnh hơn chấm tròn gấp trăm lần",
        "Không tỏa nhiệt khi bật đèn",
        "Không bị hiện tượng khúc xạ ánh sáng"
    ], 0, "Chữ F có tính bất đối xứng nên dễ nhận biết ảnh thật bị lộn ngược cả trên dưới và trái phải."),
    make_mc(4, "Nhận biết", "Khi đo tiêu cự theo phương pháp Silbermann, nếu chiều cao vật sáng AB là 1,5 cm thì chiều cao ảnh thật A'B' trên màn hứng đo được là:", [
        "1,5 cm",
        "3,0 cm",
        "0,75 cm",
        "4,5 cm"
    ], 0, "Phương pháp Silbermann cho ảnh thật bằng vật: A'B' = AB = 1,5 cm."),
    make_mc(5, "Nhận biết", "Thao tác gắn thấu kính lên giá quang học cần lưu ý:", [
        "Mặt thấu kính phải vuông góc với thanh giá quang học",
        "Gắn nghiêng góc 30 độ",
        "Để thấu kính lắc lư tự do",
        "Dán băng dính che kín hai mặt thấu kính"
    ], 0, "Mặt thấu kính phải vuông góc với trục quang học để đường truyền chuẩn xác."),
    make_mc(6, "Nhận biết", "Để xác định sai số dụng cụ của thước đo trên giá quang học, ta thường lấy sai số bằng:", [
        "Một nửa độ chia nhỏ nhất hoặc bằng đúng một độ chia nhỏ nhất của thước",
        "Bằng tiêu cự của thấu kính",
        "Bằng 5 cm cố định",
        "Bằng 0"
    ], 0, "Sai số dụng cụ thường lấy bằng 1/2 ĐCNN hoặc 1 ĐCNN của thước đo."),
    make_mc(7, "Thông hiểu", "Một nhóm học sinh đo được khoảng cách từ vật đến màn là L = 56 cm khi ảnh thật ngược chiều bằng vật. Tiêu cự f của thấu kính là:", [
        "14 cm",
        "28 cm",
        "56 cm",
        "7 cm"
    ], 0, "f = L / 4 = 56 / 4 = 14 cm."),
    make_mc(8, "Thông hiểu", "Một thấu kính hội tụ có tiêu cự f = 10 cm. Khi đặt vật cách thấu kính d = 15 cm thì khoảng cách từ thấu kính đến màn hứng ảnh sắc nét là:", [
        "30 cm",
        "15 cm",
        "45 cm",
        "60 cm"
    ], 0, "1/d' = 1/10 - 1/15 = 1/30 => d' = 30 cm."),
    make_mc(9, "Thông hiểu", "Trong thí nghiệm, nếu màn chắn hứng được ảnh rõ nét nhưng ảnh nằm lệch hẳn lên phía trên mép màn chắn thì học sinh cần:", [
        "Nâng vật sáng lên cao hoặc hạ màn chắn xuống cho tâm ảnh về giữa màn",
        "Thay thấu kính khác có tiêu cự nhỏ hơn",
        "Tắt bớt đèn chiếu",
        "Đặt nghiêng giá quang học"
    ], 0, "Chỉnh độ cao của các bộ phận để tâm vật, thấu kính và màn cùng nằm trên một trục."),
    make_mc(10, "Thông hiểu", "Khi giữ nguyên vị trí vật và màn chắn (cách nhau L > 4f), có mấy vị trí đặt thấu kính cho ảnh rõ nét trên màn?", [
        "Có đúng hai vị trí đặt thấu kính đối xứng nhau qua trung điểm của đoạn nối vật và màn",
        "Chỉ có duy nhất một vị trí",
        "Có vô số vị trí",
        "Không có vị trí nào"
    ], 0, "Khi L > 4f, phương trình d(L - d) = L.f có hai nghiệm phân biệt đối xứng nhau."),
    make_mc(11, "Thông hiểu", "Nếu thấu kính hội tụ trong bài thực hành bị dính bụi bẩn mờ một phần, cách xử lý chuẩn mực là:", [
        "Dùng giấy lau kính chuyên dụng hoặc khăn bông mềm tẩm cồn quang học lau nhẹ nhàng",
        "Dùng mũi dao cạo sạch bụi bẩn",
        "Rửa thấu kính dưới vòi nước áp lực cực mạnh",
        "Đốt nóng thấu kính trên ngọn lửa đèn cồn"
    ], 0, "Dùng giấy lau kính chuyên dụng hoặc khăn mềm quang học để không làm xước mặt kính."),
    make_mc(12, "Thông hiểu", "Một học sinh đo tiêu cự qua 4 lần thu được các kết quả: 10,1 cm; 9,9 cm; 10,0 cm; 10,0 cm. Kết quả đo tiêu cự trung bình là:", [
        "10,0 cm",
        "10,1 cm",
        "9,9 cm",
        "40,0 cm"
    ], 0, "f_tb = (10,1 + 9,9 + 10,0 + 10,0) / 4 = 10,0 cm.")
]

p2_b20_t3 = [
    make_tf(1, "Thông hiểu", "Về các phương pháp xác định tiêu cự của thấu kính hội tụ:", [
        ("a", "Phương pháp dùng chùm sáng song song cho phép xác định tiêu cự nhanh chóng nhưng độ chính xác phụ thuộc độ song song của chùm sáng.", True),
        ("b", "Phương pháp Silbermann cho ảnh thật bằng vật có độ chính xác cao và dễ xác định vị trí.", True),
        ("c", "Có thể dùng thấu kính hội tụ hứng ảnh thật của một vật đặt trong khoảng tiêu cự lên màn.", False),
        ("d", "Phương pháp đo d và d' cho phép đo tiêu cự ở nhiều vị trí đặt vật khác nhau.", True)
    ], "Vật đặt trong khoảng d < f chỉ cho ảnh ảo, không thể hứng trên màn."),
    make_tf(2, "Thông hiểu", "Quy trình thực hiện bài thực hành đo tiêu cự:", [
        ("a", "Lắp đặt các thiết bị thẳng hàng và đồng trục trên giá quang học.", True),
        ("b", "Bật nguồn điện đèn chiếu sáng vật.", True),
        ("c", "Dịch chuyển đồng thời cả vật, thấu kính và màn chạy lung tung để tìm ảnh.", False),
        ("d", "Ghi lại số đo vị trí trên thước khi ảnh trên màn đạt độ sắc nét tối đa.", True)
    ], "Phải dịch chuyển từng bộ phận có phương pháp, thường cố định vật và thấu kính rồi tinh chỉnh màn."),
    make_tf(3, "Vận dụng", "Trong một bài thực hành với thấu kính hội tụ có tiêu cự f = 12 cm, khoảng cách giữa vật và màn là L = 50 cm:", [
        ("a", "Khoảng cách L = 50 cm lớn hơn 4f = 48 cm nên có thể thu được ảnh thật trên màn.", True),
        ("b", "Sẽ có hai vị trí của thấu kính cho ảnh thật rõ nét trên màn.", True),
        ("c", "Khoảng cách giữa hai vị trí này của thấu kính là e = 10 cm.", True),
        ("d", "Cả hai vị trí đều cho ảnh có kích thước bằng đúng vật.", False)
    ], "d1.d2 = f.L = 12 × 50 = 600; d1 + d2 = 50 => d1 = 30 cm, d2 = 20 cm => e = |30 - 20| = 10 cm. Một vị trí ảnh phóng đại (k=1,5), một vị trí ảnh thu nhỏ (k=2/3)."),
    make_tf(4, "Vận dụng", "Kết quả thực hành đo tiêu cự của một nhóm học sinh ghi nhận: Lần 1: f1 = 20,1 cm; Lần 2: f2 = 19,8 cm; Lần 3: f3 = 20,1 cm:", [
        ("a", "Tiêu cự trung bình của thấu kính là f_tb = 20,0 cm.", True),
        ("b", "Sai số tuyệt đối trung bình là Δf_tb = 0,13 cm.", True),
        ("c", "Kết quả đo có thể viết là f = 20,0 ± 0,1 cm.", True),
        ("d", "Nếu đổi sang đo bằng đơn vị mét thì sai số tương đối sẽ tăng lên gấp 100 lần.", False)
    ], "Sai số tương đối δ = Δf / f là đại lượng không thứ nguyên, không đổi khi đổi đơn vị đo.")
]

p3_b20_t3 = [
    make_sa(1, "Thông hiểu", "Trong bài thực hành đo tiêu cự, khi thu được ảnh thật rõ nét bằng vật thì tỉ số chiều cao giữa ảnh và vật A'B'/AB bằng bao nhiêu?", "1", "A'B'/AB = 1."),
    make_sa(2, "Thông hiểu", "Học sinh đo khoảng cách từ vật sáng đến thấu kính d = 16 cm và từ thấu kính đến màn d' = 16 cm khi ảnh nét rõ. Tiêu cự f của thấu kính bằng bao nhiêu cm?", "8", "d = 2f = 16 cm => f = 8 cm."),
    make_sa(3, "Vận dụng", "Khoảng cách giữa vật và màn hứng ảnh đo được là L = 88 cm khi ảnh thật ngược chiều bằng vật. Tiêu cự thấu kính bằng bao nhiêu cm?", "22", "f = L / 4 = 88 / 4 = 22 cm."),
    make_sa(4, "Vận dụng", "Một thấu kính hội tụ có f = 16 cm. Đặt ngọn nến ở vị trí d = 2f. Khoảng cách giữa ngọn nến và màn hứng ảnh là bao nhiêu cm?", "64", "L = 4f = 4 × 16 = 64 cm."),
    make_sa(5, "Vận dụng cao", "Trong thí nghiệm đo tiêu cự, vật cách thấu kính d = 45 cm, màn hứng cách thấu kính d' = 90 cm. Tiêu cự f của thấu kính là bao nhiêu cm?", "30", "f = (45 × 90) / (45 + 90) = 4050 / 135 = 30 cm."),
    make_sa(6, "Vận dụng cao", "Khoảng cách vật - màn là 75 cm. Đặt thấu kính cách vật 25 cm thì thu được ảnh rõ nét trên màn. Tiêu cự thấu kính bằng bao nhiêu cm? (Làm tròn 1 chữ số thập phân)", "16.7", "d = 25 cm => d' = 50 cm. f = (25 × 50) / 75 = 1250 / 75 ≈ 16,67 ≈ 16,7 cm.")
]

p4_b20_t3 = [
    make_vdc(1, "Trong bài thực hành quang học, một nhóm học sinh sử dụng thấu kính hội tụ mỏng có tiêu cự f = 15 cm. Để tạo ra ảnh thật của chữ F trên màn hứng có kích thước lớn gấp 3 lần chữ F ban đầu, khoảng cách từ chữ F đến thấu kính phải được điều chỉnh bằng:", [
        "20 cm",
        "15 cm",
        "45 cm",
        "10 cm"
    ], 0, "k = d'/d = 3 => d' = 3d. 1/f = 1/d + 1/(3d) = 4/(3d) => 3d = 4f = 4 × 15 = 60 => d = 20 cm."),
    make_vdc(2, "Khi đo tiêu cự của thấu kính hội tụ theo phương pháp Silbermann, nếu học sinh đo nhầm khoảng cách giữa vật và màn L thiếu mất 4 cm (nghĩa là giá trị đọc nhỏ hơn thực tế 4 cm) thì tiêu cự tính ra sẽ:", [
        "Bị nhỏ hơn giá trị thực tế 1 cm",
        "Bị nhỏ hơn giá trị thực tế 4 cm",
        "Bị lớn hơn giá trị thực tế 1 cm",
        "Không bị ảnh hưởng chút nào"
    ], 0, "f = L / 4 nên khi L giảm 4 cm thì f giảm Δf = 4 / 4 = 1 cm."),
    make_vdc(3, "Một phòng thí nghiệm bị mất nhãn của hai thấu kính hội tụ L1 và L2. Để xác định nhanh thấu kính nào có tiêu cự ngắn hơn mà không cần lắp giá quang học phức tạp, học sinh có thể làm cách nào sau đây?", [
        "Cầm từng thấu kính hứng ánh sáng mặt trời chiếu xuống mặt bàn, thấu kính nào tạo điểm sáng hội tụ nhỏ nhất ở khoảng cách gần mặt bàn hơn là thấu kính có tiêu cự ngắn hơn",
        "Cân xem thấu kính nào nặng hơn",
        "Thả hai thấu kính vào chậu nước xem cái nào chìm nhanh hơn",
        "Đo đường kính ngoài của vành thấu kính"
    ], 0, "Hứng ánh sáng mặt trời: thấu kính hội tụ ánh sáng ở cự ly gần hơn chính là thấu kính có tiêu cự ngắn hơn."),
    make_vdc(4, "Một học sinh thực hiện thí nghiệm đo tiêu cự bằng phương pháp Bessel: Giữ vật và màn cố định cách nhau L = 90 cm. Di chuyển thấu kính thấy có hai vị trí cho ảnh rõ nét trên màn. Ở vị trí thứ nhất ảnh cao h1 = 8 cm, ở vị trí thứ hai ảnh cao h2 = 2 cm. Chiều cao h của vật sáng chữ F ban đầu bằng bao nhiêu cm?", [
        "4 cm",
        "5 cm",
        "6 cm",
        "10 cm"
    ], 0, "Theo tính chất phương pháp Bessel, chiều cao vật là trung bình nhân của hai ảnh: h = √(h1 × h2) = √(8 × 2) = √16 = 4 cm.")
]

exams["phys9_c6_b20_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c6_b20", "Bài 20: Thực hành xác định tiêu cự của thấu kính hội tụ", 3, p1_b20_t3, p2_b20_t3, p3_b20_t3, p4_b20_t3)

print("Added phys9_c6_b20 (3 tests).")
