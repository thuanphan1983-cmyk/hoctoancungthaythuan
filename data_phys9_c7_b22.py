# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI VẬT LÝ 9 - BÀI 22: TỪ TRƯỜNG CỦA ỐNG DÂY CÓ DÒNG ĐIỆN. NAM CHÂM ĐIỆN
Bao gồm 3 đề thi độc lập 100%: phys9_c7_b22_test1, phys9_c7_b22_test2, phys9_c7_b22_test3
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_phys9_c6 import make_mc, make_tf, make_sa, make_vdc, make_exam

exams = {}

CH_ID = "phys9_c7"
CH_TITLE = "Chương VII: Điện từ"

# =============================================================================
# BÀI 22: TỪ TRƯỜNG CỦA ỐNG DÂY CÓ DÒNG ĐIỆN. NAM CHÂM ĐIỆN (3 ĐỀ)
# =============================================================================

# --- phys9_c7_b22_test1 ---
p1_b22_t1 = [
    make_mc(1, "Nhận biết", "Từ phổ ở bên ngoài của một ống dây có dòng điện chạy qua có hình dạng tương tự như từ phổ của:", [
        "Một thanh nam châm thẳng",
        "Một nam châm chữ U",
        "Một thanh đồng hình trụ",
        "Một quả cầu kim loại tích điện"
    ], 0, "Từ phổ bên ngoài ống dây có dòng điện giống hệt từ phổ của thanh nam châm thẳng."),
    make_mc(2, "Nhận biết", "Quy tắc nắm tay phải dùng để xác định:", [
        "Chiều của đường sức từ trong lòng ống dây có dòng điện chạy qua",
        "Chiều của lực điện từ tác dụng lên dây dẫn",
        "Chiều của dòng điện cảm ứng",
        "Chiều quay của cánh quạt điện"
    ], 0, "Quy tắc nắm tay phải dùng để xác định chiều đường sức từ trong lòng ống dây có dòng điện."),
    make_mc(3, "Nhận biết", "Trong quy tắc nắm tay phải, chiều từ cổ tay đến bốn ngón tay uốn cong theo chiều của:", [
        "Dòng điện chạy qua các vòng dây của ống dây",
        "Đường sức từ ngoài không gian",
        "Lực hút từ trường",
        "Trục quay của ống dây"
    ], 0, "Bốn ngón tay nắm lại chỉ theo chiều dòng điện chạy qua các vòng dây."),
    make_mc(4, "Nhận biết", "Cấu tạo cơ bản của một nam châm điện gồm:", [
        "Một ống dây dẫn có dòng điện chạy qua và một lõi sắt non đặt trong lòng ống dây",
        "Một thanh nam châm vĩnh cửu gắn pin",
        "Hai thanh đồng kẹp một thanh thép",
        "Một bóng đèn sợi đốt nối với tụ điện"
    ], 0, "Nam châm điện gồm ống dây dẫn có dòng điện và lõi sắt non bên trong."),
    make_mc(5, "Nhận biết", "Tác dụng cốt lõi của lõi sắt non đặt trong lòng ống dây có dòng điện là:", [
        "Làm tăng từ trường của ống dây lên rất nhiều lần",
        "Làm ống dây không bị nóng khi có dòng điện",
        "Làm đổi màu lớp vỏ dây dẫn",
        "Làm ngắt dòng điện trong mạch"
    ], 0, "Sắt non bị nhiễm từ mạnh, làm tăng từ trường của ống dây lên hàng nghìn lần."),
    make_mc(6, "Nhận biết", "Biện pháp nào sau đây giúp làm tăng lực từ của một nam châm điện?", [
        "Tăng cường độ dòng điện chạy qua các vòng dây hoặc tăng số vòng dây của ống dây",
        "Giảm số vòng dây của ống dây đi một nửa",
        "Thay lõi sắt non bằng lõi gỗ khô",
        "Giảm hiệu điện thế đặt vào hai đầu cuộn dây"
    ], 0, "Tăng I và tăng số vòng dây N làm tăng từ trường của nam châm điện."),
    make_mc(7, "Thông hiểu", "Khi ngắt dòng điện chạy qua ống dây của nam châm điện có lõi sắt non thì:", [
        "Lõi sắt non mất hết từ tính ngay lập tức",
        "Lõi sắt non biến thành nam châm vĩnh cửu hút sắt vĩnh viễn",
        "Lõi sắt non tự phát sáng trong bóng tối",
        "Lõi sắt non bị nổ tung"
    ], 0, "Sắt non có đặc tính mất từ tính ngay khi ngắt dòng điện."),
    make_mc(8, "Thông hiểu", "Tại sao người ta dùng lõi sắt non chứ KHÔNG dùng lõi thép để chế tạo nam châm điện dùng trong cần cẩu phế liệu?", [
        "Vì thép sau khi nhiễm từ sẽ giữ từ tính lâu thành nam châm vĩnh cửu, không thể nhả phế liệu ra khi ngắt điện",
        "Vì thép không bị nhiễm từ trong từ trường",
        "Vì thép nặng hơn sắt non gấp trăm lần",
        "Vì thép dẫn điện kém hơn gỗ"
    ], 0, "Thép giữ từ tính lâu nên khi ngắt điện vẫn hút dính phế liệu, không thả vật xuống được."),
    make_mc(9, "Thông hiểu", "Dùng quy tắc nắm tay phải cho một ống dây: nếu ngón tay cái choãi ra chỉ về đầu A của ống dây thì đầu A là:", [
        "Cực Bắc (N) của ống dây",
        "Cực Nam (S) của ống dây",
        "Cực dương của nguồn điện",
        "Cực âm của nguồn điện"
    ], 0, "Ngón tay cái choãi ra chỉ chiều đường sức từ trong lòng ống dây (hướng từ cực Nam ra cực Bắc ở đầu ló ra)."),
    make_mc(10, "Thông hiểu", "Một kim nam châm nhỏ tự do đặt gần một đầu của ống dây có dòng điện. Khi đổi chiều dòng điện chạy qua ống dây thì kim nam châm sẽ:", [
        "Quay 180 độ (đổi đầu cực hút đẩy)",
        "Đứng yên không hề dịch chuyển",
        "Bị nóng chảy tức thì",
        "Mất hết từ tính hoàn toàn"
    ], 0, "Đổi chiều dòng điện làm đảo cực từ của ống dây, khiến kim nam châm quay 180° đảo cực tương tác."),
    make_mc(11, "Thông hiểu", "Thiết bị điện nào sau đây trong đời sống KHÔNG ứng dụng nam châm điện?", [
        "Bàn là điện gia đình",
        "Rơ le điện từ đóng ngắt mạch tự động",
        "Cần cẩu dọn phế liệu kim loại ở nhà máy thép",
        "Chuông báo động điện"
    ], 0, "Bàn là điện hoạt động dựa trên tác dụng nhiệt của dòng điện qua dây mayso, không dùng nam châm điện."),
    make_mc(12, "Thông hiểu", "Một nam châm điện có thể hút được các vật làm từ chất liệu nào sau đây?", [
        "Sắt, thép, niken, coban",
        "Nhôm, đồng, bạc, vàng",
        "Gỗ khô, nhựa tổng hợp",
        "Thủy tinh, sứ, cao su"
    ], 0, "Nam châm chỉ hút các vật liệu từ tính (vật liệu sắt từ: sắt, thép, niken, coban).")
]

p2_b22_t1 = [
    make_tf(1, "Thông hiểu", "Xét các tính chất của từ trường ống dây có dòng điện chạy qua:", [
        ("a", "Đường sức từ ở bên trong lòng ống dây là những đường thẳng song song cách đều nhau (từ trường đều).", True),
        ("b", "Chiều của đường sức từ trong lòng ống dây phụ thuộc vào chiều của dòng điện chạy qua các vòng dây.", True),
        ("c", "Ống dây có dòng điện có hai cực từ: cực Bắc và cực Nam.", True),
        ("d", "Nếu đổi chiều dòng điện qua ống dây thì các cực từ của ống dây vẫn giữ nguyên không đổi.", False)
    ], "Đổi chiều dòng điện thì chiều đường sức từ đổi hướng, hai cực từ bị đảo ngược."),
    make_tf(2, "Thông hiểu", "So sánh nam châm điện và nam châm vĩnh cửu:", [
        ("a", "Từ trường của nam châm điện có thể điều chỉnh mạnh yếu dễ dàng bằng cách thay đổi cường độ dòng điện.", True),
        ("b", "Nam châm điện có thể tắt hoặc bật từ tính dễ dàng bằng cách ngắt hoặc đóng công tắc điện.", True),
        ("c", "Cực từ của nam châm điện không thể đảo chiều.", False),
        ("d", "Nam châm điện được dùng phổ biến trong công nghiệp bốc dỡ kim loại nặng.", True)
    ], "Cực từ nam châm điện đảo chiều dễ dàng bằng cách đảo cực nguồn điện."),
    make_tf(3, "Vận dụng", "Một ống dây dài có dòng điện chạy qua, ống dây có đầu bên trái là A và đầu bên phải là B. Nhìn từ phía ngoài vào đầu B thấy dòng điện chạy theo chiều kim đồng hồ:", [
        ("a", "Đầu B của ống dây là cực Nam (S).", True),
        ("b", "Đầu A của ống dây là cực Bắc (N).", True),
        ("c", "Bên trong lòng ống dây, đường sức từ đi từ đầu B sang đầu A.", True),
        ("d", "Nếu đưa cực Bắc của một thanh nam châm lại gần đầu B thì chúng sẽ đẩy nhau.", False)
    ], "Đầu B là cực Nam (S) nên khi đưa cực Bắc (N) lại gần thì chúng hút nhau."),
    make_tf(4, "Vận dụng", "Thí nghiệm khảo sát lực từ của một nam châm điện dùng đinh sắt non quấn 100 vòng dây đồng có dòng điện I = 1 A hút được 15 chiếc kẹp ghim sắt:", [
        ("a", "Nếu tăng cường độ dòng điện lên I = 2 A thì số kẹp ghim hút được sẽ tăng lên.", True),
        ("b", "Nếu quấn thêm 100 vòng dây nữa (thành 200 vòng) với I = 1 A thì lực từ của nam châm điện tăng lên.", True),
        ("c", "Nếu rút lõi đinh sắt ra ngoài thì số kẹp ghim hút được sẽ tăng lên gấp đôi.", False),
        ("d", "Khi ngắt hoàn toàn nguồn điện, các kẹp ghim sắt lập tức rơi xuống.", True)
    ], "Rút lõi sắt ra làm từ trường giảm đi hàng nghìn lần, gần như không hút được kẹp ghim nữa.")
]

p3_b22_t1 = [
    make_sa(1, "Thông hiểu", "Ống dây có dòng điện chạy qua có mấy cực từ?", "2", "Có 2 cực từ: cực Bắc (N) và cực Nam (S)."),
    make_sa(2, "Thông hiểu", "Quy tắc nào được dùng để xác định chiều đường sức từ trong lòng ống dây có dòng điện?", "Nắm tay phải", "Quy tắc nắm tay phải."),
    make_sa(3, "Vận dụng", "Khi dòng điện qua ống dây tăng từ 1 A lên 3 A, lực hút của nam châm điện đối với vật bằng sắt tăng hay giảm?", "Tăng", "Lực từ tăng theo cường độ dòng điện."),
    make_sa(4, "Vận dụng", "Một nam châm điện có 500 vòng dây. Để tăng lực hút từ của nam châm này mà không thay đổi nguồn điện, người ta quấn thêm 300 vòng dây nữa. Tổng số vòng dây của nam châm điện lúc này là bao nhiêu?", "800", "500 + 300 = 800 vòng."),
    make_sa(5, "Vận dụng cao", "Một cuộn dây nam châm điện có điện trở R = 10 Ω được nối vào nguồn điện U = 12 V. Cường độ dòng điện chạy qua cuộn dây là bao nhiêu Ampe? (Lấy số thập phân)", "1.2", "I = U / R = 12 / 10 = 1,2 A."),
    make_sa(6, "Vận dụng cao", "Nếu giảm điện trở của cuộn dây nam châm điện từ 20 Ω xuống 10 Ω ở cùng hiệu điện thế U = 24 V, cường độ dòng điện chạy qua cuộn dây tăng thêm bao nhiêu Ampe?", "1.2", "I1 = 24 / 20 = 1,2 A; I2 = 24 / 10 = 2,4 A => Tăng thêm 2,4 - 1,2 = 1,2 A.")
]

p4_b22_t1 = [
    make_vdc(1, "Trong nhà máy cán thép hiện đại, cần cẩu điện sử dụng mâm nam châm điện khổng lồ có đường kính 2 mét để nhấc các tấm thép nặng hàng chục tấn từ bãi tập kết lên toa xe lửa. Để đảm bảo an toàn tuyệt đối khi xảy ra sự cố mất điện lưới đột ngột, hệ thống cần cẩu bắt buộc phải có thiết bị hỗ trợ nào sau đây?", [
        "Hệ thống ắc quy nguồn điện dự phòng tự động đóng mạch tức thì trong mili-giây để duy trì từ trường giữ chặt tấm thép không bị rơi",
        "Một chiếc quạt gió công suất lớn thổi giữ tấm thép",
        "Chuông reo báo động mà không cần giữ tấm thép",
        "Bộ giảm xóc lò xo dưới đất"
    ], 0, "Mất điện thì nam châm điện mất từ tính ngay lập tức. Cần nguồn ắc quy UPS đóng tức thời để cấp điện duy trì lực hút tránh tai nạn."),
    make_vdc(2, "Rơ le điện từ (Relay) được sử dụng rộng rãi trong các mạch điều khiển tự động (như mạch bật tắt máy bơm nước công suất lớn bằng công tắc phao nhỏ). Vai trò cốt lõi của rơ le điện từ trong trường hợp này là:", [
        "Dùng một mạch điện điều khiển có dòng điện nhỏ, điện áp thấp an toàn để đóng ngắt một mạch điện làm việc có dòng điện lớn và điện áp cao nguy hiểm",
        "Tạo ra điện năng miễn phí cho máy bơm chạy",
        "Làm tăng áp suất nước trong đường ống bơm",
        "Lọc sạch cặn bẩn trong nước"
    ], 0, "Rơle dùng mạch điều khiển công suất nhỏ điều khiển mạch tải công suất lớn, đảm bảo an toàn cho người vận hành."),
    make_vdc(3, "Chuông điện báo động chống trộm hoạt động dựa trên nguyên tắc: Khi có kẻ gian cậy cửa làm ngắt công tắc bảo vệ, nam châm điện của rơ le bị mất điện, lò xo kéo thanh sắt đóng mạch chuông kêu vang. Đây là ứng dụng của:", [
        "Sự mất từ tính tức thì của nam châm điện khi ngắt dòng điện điều khiển",
        "Tác dụng phát sáng của dòng điện",
        "Lực đẩy tĩnh điện",
        "Hiện tượng cảm ứng nhiệt"
    ], 0, "Mạch rơle thường đóng: mất điện cuộn hút thì tiếp điểm nhả đóng mạch báo động."),
    make_vdc(4, "Một kỹ sư thiết kế nam châm điện siêu dẫn dùng trong máy chụp cộng hưởng từ (MRI) y tế. Ống dây được làm từ hợp kim siêu dẫn ngâm trong heli lỏng (-269 độ C) để điện trở bằng 0. Ưu điểm vượt trội của nam châm điện siêu dẫn này là:", [
        "Tạo ra từ trường cực mạnh và ổn định mà hoàn toàn không bị tỏa nhiệt hao phí năng lượng trên cuộn dây",
        "Nam châm không cần khung đỡ cơ học",
        "Tự động phát ra tia X chụp xương",
        "Hoạt động không cần nguồn điện ban đầu"
    ], 0, "Dây siêu dẫn có R = 0 nên cho dòng điện hàng nghìn Ampe chạy qua sinh từ trường cực mạnh mà không tỏa nhiệt Php = I^2.R = 0.")
]

exams["phys9_c7_b22_test1"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b22", "Bài 22: Từ trường của ống dây có dòng điện. Nam châm điện", 1, p1_b22_t1, p2_b22_t1, p3_b22_t1, p4_b22_t1)

# --- phys9_c7_b22_test2 ---
p1_b22_t2 = [
    make_mc(1, "Nhận biết", "Đường sức từ ở bên trong lòng ống dây có dòng điện chạy qua là những đường thẳng có đặc điểm:", [
        "Song song và cách đều nhau",
        "Cắt nhau tại tâm ống dây",
        "Gấp khúc ziczac",
        "Hình xoắn ốc tỏa rộng"
    ], 0, "Trong lòng ống dây, đường sức từ là những đường thẳng song song cách đều nhau (từ trường đều)."),
    make_mc(2, "Nhận biết", "Trong quy tắc nắm tay phải đối với ống dây, ngón tay cái choãi ra 90 độ chỉ chiều của:", [
        "Đường sức từ trong lòng ống dây",
        "Dòng điện trong các vòng dây",
        "Lực hút nam châm",
        "Điện trường ngoài"
    ], 0, "Ngón tay cái choãi ra chỉ chiều của đường sức từ trong lòng ống dây."),
    make_mc(3, "Nhận biết", "Lõi sắt non trong nam châm điện bị mất từ tính khi:", [
        "Ngắt dòng điện chạy qua ống dây",
        "Tăng cường độ dòng điện",
        "Đổi chiều dòng điện",
        "Tăng số vòng dây"
    ], 0, "Sắt non mất từ tính ngay khi ngắt dòng điện."),
    make_mc(4, "Nhận biết", "Nếu giữ nguyên số vòng dây của nam châm điện nhưng tăng cường độ dòng điện chạy qua cuộn dây thì lực từ của nam châm điện sẽ:", [
        "Tăng lên",
        "Giảm đi",
        "Không thay đổi",
        "Bằng 0"
    ], 0, "Lực từ tỉ lệ thuận với cường độ dòng điện I."),
    make_mc(5, "Nhận biết", "Để nhận biết từ trường của ống dây có dòng điện, dụng cụ đơn giản và nhạy nhất là:", [
        "Kim nam châm thử tự do",
        "Vôn kế xoay chiều",
        "Nhiệt kế thủy ngân",
        "Lực kế lò xo"
    ], 0, "Kim nam châm thử là dụng cụ nhạy nhất để phát hiện từ trường."),
    make_mc(6, "Nhận biết", "Vật liệu nào sau đây KHÔNG THỂ dùng làm lõi của nam châm điện?", [
        "Đồng hoặc nhôm",
        "Sắt non",
        "Thép kỹ thuật điện",
        "Gang xám"
    ], 0, "Đồng và nhôm không phải vật liệu sắt từ, không bị nhiễm từ nên không thể làm lõi nam châm điện."),
    make_mc(7, "Thông hiểu", "Một ống dây có dòng điện chạy qua đặt nằm ngang, đầu bên trái hút cực Nam (S) của kim nam châm thử. Đầu bên trái của ống dây là cực gì?", [
        "Cực Bắc (N)",
        "Cực Nam (S)",
        "Không có cực từ",
        "Cực âm điện thế"
    ], 0, "Hút cực Nam (S) thì đầu đó phải là cực Bắc (N) của ống dây."),
    make_mc(8, "Thông hiểu", "Khi muốn nhả một tấm phế liệu bằng sắt đang được cần cẩu nam châm điện nhấc bổng, người điều khiển chỉ cần:", [
        "Ngắt công tắc điện cấp cho nam châm điện",
        "Tăng điện áp lên cực đại",
        "Đảo chiều động cơ cần cẩu",
        "Phun nước vào nam châm điện"
    ], 0, "Ngắt điện thì nam châm điện mất từ tính lập tức, tấm sắt rơi ra."),
    make_mc(9, "Thông hiểu", "Một nam châm điện hoạt động với nguồn điện không đổi. Nếu quấn thêm dây làm tăng số vòng dây lên gấp đôi (giả sử cường độ dòng điện vẫn giữ không đổi) thì lực hút của nam châm điện sẽ:", [
        "Tăng lên đáng kể",
        "Giảm đi một nửa",
        "Không đổi",
        "Biến mất hoàn toàn"
    ], 0, "Tăng số vòng dây N làm tăng độ lớn từ trường B."),
    make_mc(10, "Thông hiểu", "Đầu nào của ống dây có dòng điện chạy qua có đường sức từ đi ra?", [
        "Cực Bắc (N)",
        "Cực Nam (S)",
        "Hai bên thành ống",
        "Chính giữa lòng ống"
    ], 0, "Quy ước đường sức từ: 'Vào Nam ra Bắc' (ra ở cực Bắc, vào ở cực Nam)."),
    make_mc(11, "Thông hiểu", "Chuông gọi cửa điện gia đình phát ra tiếng 'kính coong' khi bấm nút là nhờ nam châm điện:", [
        "Hút thanh búa sắt đập vào chuông kim loại, đồng thời tự ngắt mạch để nhả búa trở về vị trí cũ",
        "Tỏa nhiệt làm giãn nở thanh chuông",
        "Tích điện phóng tia lửa điện",
        "Quay một cánh quạt gió thổi vào chuông"
    ], 0, "Nam châm điện hút thanh búa gõ chuông, cơ cấu ngắt mạch tự động lặp lại chu kỳ."),
    make_mc(12, "Thông hiểu", "Vì sao khi chế tạo nam châm điện người ta không dùng lõi bằng thủy tinh?", [
        "Vì thủy tinh không bị nhiễm từ nên không có tác dụng tăng cường từ trường",
        "Vì thủy tinh dễ vỡ khi bị dòng điện đi qua",
        "Vì thủy tinh quá đắt tiền",
        "Vì thủy tinh tự hút nam châm vĩnh cửu"
    ], 0, "Thủy tinh là chất thuận từ/nghịch từ rất yếu, không phải chất sắt từ nên không làm tăng từ trường.")
]

p2_b22_t2 = [
    make_tf(1, "Thông hiểu", "Về quy tắc bàn tay và ống dây có dòng điện:", [
        ("a", "Quy tắc nắm tay phải dùng để xác định chiều đường sức từ trong lòng ống dây.", True),
        ("b", "Nắm bàn tay phải sao cho 4 ngón tay chỉ theo chiều dòng điện qua các vòng dây.", True),
        ("c", "Ngón tay cái choãi ra chỉ chiều của dòng điện trong mạch chính.", False),
        ("d", "Nếu đổi chiều dòng điện thì chiều ngón tay cái choãi ra bị đảo ngược.", True)
    ], "Ngón tay cái choãi ra chỉ chiều đường sức từ trong lòng ống dây."),
    make_tf(2, "Thông hiểu", "Xét các yếu tố quyết định từ tính của nam châm điện:", [
        ("a", "Số vòng dây của ống dây càng nhiều thì từ trường càng mạnh.", True),
        ("b", "Cường độ dòng điện qua các vòng dây càng lớn thì từ trường càng mạnh.", True),
        ("c", "Hình dạng lõi sắt non không ảnh hưởng đến khả năng hút sắt.", False),
        ("d", "Lõi sắt non có thể thay thế bằng thanh thép cứng để tạo nam châm điện nhả phế liệu tốt hơn.", False)
    ], "Lõi sắt non hình móng ngựa hoặc trụ tối ưu đường sức từ; thép cứng giữ từ tính không nhả phế liệu."),
    make_tf(3, "Vận dụng", "Một ống dây có 2 đầu C và D đặt cạnh một thanh nam châm thẳng SN (đầu S ở gần đầu D). Khi đóng điện, thấy ống dây đẩy thanh nam châm ra xa:", [
        ("a", "Đầu D của ống dây là cực Nam (S).", True),
        ("b", "Đầu C của ống dây là cực Bắc (N).", True),
        ("c", "Hai cực cùng tên (S và S) đẩy nhau.", True),
        ("d", "Nếu ngắt điện thì ống dây vẫn đẩy thanh nam châm với lực cũ.", False)
    ], "Ngắt điện thì ống dây mất từ tính, không còn lực đẩy."),
    make_tf(4, "Vận dụng", "Một nam châm điện được cấp điện từ nguồn pin 6V hút được một quả cân nặng 200 gam:", [
        ("a", "Nếu tăng hiệu điện thế nguồn pin lên 12V thì cường độ dòng điện trong cuộn dây tăng lên.", True),
        ("b", "Khi dòng điện tăng lên thì lực hút của nam châm điện tăng và có thể hút được quả cân nặng hơn 200 gam.", True),
        ("c", "Nếu đổi cực của pin thì nam châm điện sẽ đẩy quả cân sắt thay vì hút.", False),
        ("d", "Lực hút nam châm tác dụng lên sắt từ không phụ thuộc vào chiều cực từ của nam châm.", True)
    ], "Nam châm hút sắt không phụ thuộc vào cực Bắc hay Nam (cực nào cũng hút sắt).")
]

p3_b22_t2 = [
    make_sa(1, "Thông hiểu", "Đường sức từ đi ra ở cực Bắc hay cực Nam của ống dây?", "Cực Bắc", "Vào Nam ra Bắc."),
    make_sa(2, "Thông hiểu", "Dụng cụ dùng để đóng ngắt mạch điện tự động nhờ nam châm điện có tên là gì?", "Rơ le", "Rơ le điện từ (relay)."),
    make_sa(3, "Vận dụng", "Một nam châm điện có cường độ dòng điện chạy qua là 2 A. Nếu tăng cường độ dòng điện lên gấp 3 lần thì dòng điện qua nam châm lúc này là bao nhiêu Ampe?", "6", "2 × 3 = 6 A."),
    make_sa(4, "Vận dụng", "Cuộn dây của một nam châm điện có 200 vòng dây trên mỗi mét chiều dài. Nếu quấn thêm 300 vòng dây trên mỗi mét nữa thì mật độ vòng dây lúc này là bao nhiêu vòng/mét?", "500", "200 + 300 = 500 vòng/mét."),
    make_sa(5, "Vận dụng cao", "Một cuộn dây nam châm điện có điện trở 8 Ω được mắc vào hiệu điện thế 16 V. Cường độ dòng điện qua cuộn dây bằng bao nhiêu Ampe?", "2", "I = U / R = 16 / 8 = 2 A."),
    make_sa(6, "Vận dụng cao", "Một nam châm điện dùng nguồn U = 24 V, dòng điện chạy qua là I = 3 A. Điện trở của cuộn dây nam châm điện là bao nhiêu Ôm?", "8", "R = U / I = 24 / 3 = 8 Ω.")
]

p4_b22_t2 = [
    make_vdc(1, "Cơ cấu rơ le nhiệt điện từ bảo vệ quá tải cho động cơ máy giặt gia đình: Khi động cơ bị kẹt rác, dòng điện tăng vọt qua cuộn dây nam châm điện của rơ le. Hiện tượng gì sẽ xảy ra tiếp theo?", [
        "Từ trường của nam châm điện tăng mạnh đột ngột, hút tiếp điểm ngắt mạch điện cấp cho động cơ để chống cháy máy",
        "Động cơ tự quay nhanh gấp mười lần để xả rác",
        "Rơ le phun nước làm nguội động cơ",
        "Tiếp điểm hàn dính chặt mãi mãi"
    ], 0, "Dòng quá tải sinh lực từ mạnh thắng lực lò xo, hút tiếp điểm mở ngắt nguồn điện bảo vệ động cơ."),
    make_vdc(2, "Hệ thống tàu đệm từ trường (Maglev) chạy trên đệm từ không ma sát với tốc độ trên 450 km/h sử dụng các nam châm điện gắn dọc thân tàu và đường ray. Để giữ cho con tàu lơ lửng ổn định cách đường ray đúng 10 mm trong suốt hành trình, hệ thống điều khiển tự động phải liên tục:", [
        "Điều chỉnh cường độ dòng điện chạy qua các nam châm điện hàng nghìn lần mỗi giây dựa trên cảm biến khoảng cách",
        "Tắt hoàn toàn nguồn điện để tàu rơi tự do",
        "Bơm thêm không khí nén vào gầm tàu",
        "Đổi chiều đường ray liên tục"
    ], 0, "Hệ thống máy tính điều khiển dòng điện trong nam châm điện với tần số cao để duy trì khe hở từ tính chính xác 10 mm."),
    make_vdc(3, "Khóa cửa thông minh bằng nam châm điện (Magnetic Lock) dùng trong các tòa nhà cao tầng: Một nam châm điện gắn trên khung cửa giữ chặt một tấm sắt gắn trên cánh cửa bằng lực giữ lên tới 3000 N (300 kg). Để mở cửa từ bên trong khi xảy ra sự cố hỏa hoạn, nút bấm thoát hiểm khẩn cấp (Emergency Exit) sẽ tác động như thế nào?", [
        "Ngắt nguồn điện cấp cho nam châm điện làm nam châm mất từ tính ngay lập tức để người đẩy cửa chạy ra ngoài",
        "Tăng điện áp lên cực đại để khóa chặt hơn",
        "Bơm dầu bôi trơn lên mặt nam châm",
        "Đảo cực nguồn điện biến nam châm thành máy phát điện"
    ], 0, "Khóa từ là loại Fail-Safe: mất điện thì khóa nhả lập tức, đảm bảo thoát hiểm an toàn khi cháy."),
    make_vdc(4, "Một kỹ sư chế tạo một nam châm điện hình chữ U để hút các tấm phôi thép. So với nam châm điện dạng thanh thẳng có cùng kích thước và số vòng dây, nam châm điện hình chữ U có ưu điểm nổi bật là:", [
        "Cả hai cực từ (Bắc và Nam) cùng tiếp xúc trực tiếp vào tấm phôi thép tạo thành mạch từ kín, làm lực hút tăng lên gấp nhiều lần",
        "Tiêu tốn ít dây đồng hơn một nửa",
        "Không cần dùng dòng điện để hoạt động",
        "Tự động đổi màu cảnh báo nhiệt độ"
    ], 0, "Nam châm hình móng ngựa (chữ U) khép kín mạch từ qua phôi thép, triệt tiêu khe hở không khí làm lực từ cực đại.")
]

exams["phys9_c7_b22_test2"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b22", "Bài 22: Từ trường của ống dây có dòng điện. Nam châm điện", 2, p1_b22_t2, p2_b22_t2, p3_b22_t2, p4_b22_t2)

# --- phys9_c7_b22_test3 ---
p1_b22_t3 = [
    make_mc(1, "Nhận biết", "Trong lòng một ống dây có dòng điện một chiều chạy qua, từ trường có đặc tính là:", [
        "Từ trường đều (các đường sức từ song song và cách đều)",
        "Từ trường biến thiên hỗn loạn",
        "Từ trường bằng 0 tại mọi điểm",
        "Chỉ có từ trường tại hai đầu mép ống"
    ], 0, "Từ trường trong lòng ống dây dài là từ trường đều."),
    make_mc(2, "Nhận biết", "Để xác định cực Bắc của một ống dây có dòng điện, ta quan sát hướng chỉ của:", [
        "Ngón tay cái choãi ra khi nắm bàn tay phải theo chiều dòng điện",
        "Ngón tay trỏ bàn tay trái",
        "Ngón tay út bàn tay phải",
        "Lòng bàn tay trái"
    ], 0, "Ngón tay cái choãi ra chỉ chiều đường sức từ, hướng ra ở cực Bắc."),
    make_mc(3, "Nhận biết", "Vật liệu sắt từ được dùng làm lõi của nam châm điện thông dụng là:", [
        "Sắt non",
        "Đồng đỏ",
        "Thau vàng",
        "Chì đặc"
    ], 0, "Sắt non nhiễm từ mạnh và mất từ tính nhanh."),
    make_mc(4, "Nhận biết", "Cách làm nào sau đây làm GIẢM lực từ của nam châm điện?", [
        "Giảm cường độ dòng điện chạy qua các vòng dây",
        "Tăng số vòng dây của ống dây",
        "Tăng hiệu điện thế cấp nguồn",
        "Cho thêm một thanh sắt non vào lõi"
    ], 0, "Giảm cường độ dòng điện I làm giảm từ trường và lực từ."),
    make_mc(5, "Nhận biết", "Cực Nam của ống dây có dòng điện là đầu có đường sức từ:", [
        "Đi vào trong lòng ống dây",
        "Đi ra khỏi lòng ống dây",
        "Vuông góc với trục ống dây",
        "Xoắn ốc ngược chiều kim đồng hồ"
    ], 0, "Đường sức từ đi vào ở cực Nam, đi ra ở cực Bắc."),
    make_mc(6, "Nhận biết", "Trong các thiết bị sau, thiết bị nào KHÔNG sử dụng nam châm điện?", [
        "Bóng đèn sợi đốt thắp sáng",
        "Rơ le bảo vệ quá dòng",
        "Chuông báo cháy điện từ",
        "Cần cẩu hút sắt vụn"
    ], 0, "Bóng đèn sợi đốt hoạt động nhờ tác dụng nhiệt nung sáng vonfram, không dùng nam châm điện."),
    make_mc(7, "Thông hiểu", "Một ống dây có dòng điện chạy qua hút đầu Bắc (N) của kim nam châm thử. Đầu đó của ống dây là cực:", [
        "Cực Nam (S)",
        "Cực Bắc (N)",
        "Cực dương",
        "Cực trung hòa"
    ], 0, "Hút cực Bắc (N) thì đầu đó của ống dây phải là cực Nam (S)."),
    make_mc(8, "Thông hiểu", "Một nam châm điện đang hút các đinh sắt nhỏ. Nếu ngắt công tắc điện thì:", [
        "Các đinh sắt rơi xuống ngay lập tức vì lõi sắt non mất từ tính",
        "Các đinh sắt vẫn dính chặt mãi mãi",
        "Các đinh sắt bị đẩy bắn ra xa",
        "Các đinh sắt biến thành đồng"
    ], 0, "Ngắt điện thì lõi sắt non mất hết từ tính, các đinh sắt rơi xuống."),
    make_mc(9, "Thông hiểu", "Muốn đổi chiều từ trường trong lòng ống dây có dòng điện, ta phải làm cách nào?", [
        "Đổi chiều dòng điện chạy qua các vòng dây của ống dây",
        "Tăng gấp đôi số vòng dây",
        "Rút lõi sắt ra ngoài",
        "Sơn lại vỏ ống dây"
    ], 0, "Đổi chiều dòng điện làm đảo chiều các đường sức từ."),
    make_mc(10, "Thông hiểu", "Tại sao nam châm điện lại được ứng dụng rộng rãi hơn nam châm vĩnh cửu trong các dây chuyền tự động hóa công nghiệp?", [
        "Vì có thể dễ dàng điều khiển lực từ mạnh yếu và bật tắt từ tính tức thì bằng dòng điện",
        "Vì nam châm điện không tốn điện năng",
        "Vì nam châm điện làm bằng vàng nguyên chất",
        "Vì nam châm điện nhẹ hơn không khí"
    ], 0, "Nam châm điện điều khiển lực từ và bật/tắt linh hoạt bằng dòng điện."),
    make_mc(11, "Thông hiểu", "Khi mắc nam châm điện vào nguồn điện xoay chiều AC tần số 50 Hz thì cực từ của nam châm điện sẽ:", [
        "Luân phiên đổi cực liên tục với tần số 100 lần trong một giây",
        "Giữ nguyên cố định cực Bắc ở đầu bên phải",
        "Biến mất hoàn toàn không còn từ tính",
        "Chỉ có cực Nam ở cả hai đầu"
    ], 0, "Dòng AC đổi chiều 100 lần/giây (50 chu kỳ) làm cực từ của nam châm điện đảo chiều liên tục 100 lần/giây."),
    make_mc(12, "Thông hiểu", "Một ống dây dẫn có 1000 vòng dây mang dòng điện I = 0,5 A. Nếu quấn lại thành 500 vòng dây nhưng tăng dòng điện lên I = 1 A thì từ trường trong lòng ống dây sẽ:", [
        "Gần như không đổi (vì tích N × I = 500 không đổi)",
        "Tăng lên gấp 4 lần",
        "Giảm đi một nửa",
        "Biến mất về 0"
    ], 0, "Từ trường tỉ lệ với tích N × I (tích số ampe-vòng): 1000 × 0,5 = 500 vòng.A = 500 × 1 nên từ trường xấp xỉ không đổi.")
]

p2_b22_t3 = [
    make_tf(1, "Thông hiểu", "Về từ trường của dòng điện chạy trong ống dây:", [
        ("a", "Đường sức từ của ống dây là những đường cong khép kín.", True),
        ("b", "Bên ngoài ống dây, đường sức từ có chiều đi ra từ cực Bắc và đi vào ở cực Nam.", True),
        ("c", "Bên trong lòng ống dây, đường sức từ đi từ cực Nam sang cực Bắc.", True),
        ("d", "Từ trường trong lòng ống dây yếu hơn từ trường ở ngoài rất xa ống dây.", False)
    ], "Từ trường tập trung dày đặc nhất bên trong lòng ống dây (mạnh hơn bên ngoài rất nhiều)."),
    make_tf(2, "Thông hiểu", "Về cấu tạo và nguyên lý hoạt động của chuông điện báo động:", [
        ("a", "Nam châm điện là bộ phận chính tạo lực hút thanh gõ chuông.", True),
        ("b", "Lá thép đàn hồi có tác dụng kéo thanh gõ trở về vị trí ban đầu khi mạch bị ngắt.", True),
        ("c", "Tiếp điểm điện tự động ngắt mạch khi thanh gõ bị nam châm điện hút.", True),
        ("d", "Chuông điện chỉ có thể kêu một tiếng duy nhất rồi dừng lại mãi mãi.", False)
    ], "Cơ cấu đóng ngắt tự động tạo dao động gõ chuông liên hồi."),
    make_tf(3, "Vận dụng", "Một ống dây AB có dòng điện chạy qua, đầu A nối với cực dương (+) và đầu B nối với cực âm (-) của nguồn pin:", [
        ("a", "Dòng điện chạy từ cực dương sang cực âm của nguồn điện.", True),
        ("b", "Xác định được chiều dòng điện chạy qua các vòng dây của ống dây.", True),
        ("c", "Áp dụng quy tắc nắm tay phải xác định được đầu nào là cực Bắc, đầu nào là cực Nam.", True),
        ("d", "Nếu đổi cực của nguồn pin thì chiều đường sức từ trong ống dây không đổi.", False)
    ], "Đổi cực nguồn pin thì dòng điện đổi chiều, chiều đường sức từ bị đảo ngược."),
    make_tf(4, "Vận dụng", "Thí nghiệm so sánh khả năng hút đinh sắt của nam châm điện khi có lõi sắt non và lõi thép:", [
        ("a", "Khi đang có dòng điện chạy qua, cả hai đều hút được đinh sắt.", True),
        ("b", "Lõi sắt non hút đinh sắt mạnh hơn lõi thép trong cùng điều kiện dòng điện.", True),
        ("c", "Khi ngắt dòng điện, lõi sắt non nhả đinh sắt ngay lập tức.", True),
        ("d", "Khi ngắt dòng điện, lõi thép cũng nhả hết đinh sắt ngay lập tức như lõi sắt non.", False)
    ], "Thép bị nhiễm từ giữ từ tính lâu nên vẫn hút đinh sắt sau khi ngắt điện.")
]

p3_b22_t3 = [
    make_sa(1, "Thông hiểu", "Trong lòng ống dây có dòng điện, đường sức từ đi từ cực Bắc sang cực Nam hay từ cực Nam sang cực Bắc?", "Cực Nam sang cực Bắc", "Bên trong đi từ Nam sang Bắc (khép kín với bên ngoài từ Bắc sang Nam)."),
    make_sa(2, "Thông hiểu", "Lõi sắt non làm tăng từ trường của ống dây lên mấy lần? (Hàng chục, Hàng trăm hay Hàng nghìn)", "Hàng nghìn", "Lõi sắt non làm tăng từ trường lên hàng nghìn lần."),
    make_sa(3, "Vận dụng", "Một ống dây có chiều dài L = 0,2 m gồm 400 vòng dây. Số vòng dây trên một mét chiều dài của ống dây là bao nhiêu vòng/m?", "2000", "n = 400 / 0,2 = 2000 vòng/m."),
    make_sa(4, "Vận dụng", "Một nam châm điện có R = 5 Ω nối vào nguồn điện U = 10 V. Cường độ dòng điện qua cuộn dây bằng bao nhiêu Ampe?", "2", "I = 10 / 5 = 2 A."),
    make_sa(5, "Vận dụng cao", "Một cuộn dây nam châm điện có 600 vòng dây. Để tăng tích số ampe-vòng từ 300 A.vòng lên 600 A.vòng khi giữ nguyên I = 0,5 A thì cần quấn thêm bao nhiêu vòng dây nữa?", "600", "N_mới = 600 / 0,5 = 1200 vòng => Cần quấn thêm 1200 - 600 = 600 vòng."),
    make_sa(6, "Vận dụng cao", "Một nam châm điện hoạt động ở hiệu điện thế U = 12 V tiêu thụ công suất P = 24 W. Điện trở của cuộn dây nam châm điện là bao nhiêu Ôm?", "6", "P = U^2 / R => R = 12^2 / 24 = 144 / 24 = 6 Ω.")
]

p4_b22_t3 = [
    make_vdc(1, "Thiết bị phân loại kim loại rác thải tự động: Tại nhà máy xử lý rác, băng chuyền chở hỗn hợp rác (gồm nhựa, giấy, vỏ lon nhôm, đinh ốc sắt thép) đi qua một tang trống quay có gắn nam châm điện bên trong. Các phế liệu nào sẽ bị hút dính vào tang trống và rơi vào thùng thu hồi riêng?", [
        "Các đinh ốc và mảnh vụn bằng sắt thép",
        "Vỏ lon bằng nhôm",
        "Túi nilông và chai nhựa",
        "Giấy vụn và vỏ thủy tinh"
    ], 0, "Nam châm điện chỉ hút các vật liệu sắt từ (sắt thép), còn nhôm, nhựa, giấy rơi tự do xuống băng chuyền khác."),
    make_vdc(2, "Máy chụp cắt lớp cộng hưởng từ hạt nhân (MRI) trong bệnh viện sử dụng nam châm điện siêu dẫn để tạo từ trường có độ lớn lên tới 1,5 Tesla đến 3 Tesla (mạnh gấp hàng chục nghìn lần từ trường Trái Đất). Trước khi đưa bệnh nhân vào phòng chụp MRI, nhân viên y tế bắt buộc phải kiểm tra và loại bỏ:", [
        "Mọi vật dụng bằng kim loại từ tính (như đồng hồ, chìa khóa, trang sức sắt, máy tạo nhịp tim)",
        "Quần áo làm bằng vải cotton",
        "Kính áp tròng bằng nước",
        "Giày da thông thường"
    ], 0, "Từ trường cực mạnh của MRI sẽ hút các vật thể sắt từ bay với vận tốc lớn gây tai nạn và làm hỏng máy tạo nhịp tim."),
    make_vdc(3, "Trong hệ thống phanh điện từ của tàu cao tốc Shinkansen: Khi cần phanh khẩn cấp, các nam châm điện công suất lớn gắn dưới gầm tàu được đóng điện tạo từ trường cực mạnh tác dụng xuống đường ray thép tĩnh. Tàu giảm tốc độ nhanh chóng mà không làm mòn bánh xe là nhờ:", [
        "Lực cản từ trường sinh ra bởi dòng điện Foucault cảm ứng trong thanh ray thép phản kháng chuyển động của tàu",
        "Nam châm điện cọ xát cơ học làm tóe lửa đường ray",
        "Nam châm điện phun cát xuống đường ray",
        "Nam châm điện hút ngược tàu chạy lùi lại"
    ], 0, "Phanh từ dựa trên lực hãm Foucault không tiếp xúc, không gây mòn cơ học và hiệu quả cực cao ở tốc độ lớn."),
    make_vdc(4, "Một kỹ sư thiết kế bộ lọc từ tính (Magnetic Filter) lắp trên đường ống dẫn dầu bôi trơn động cơ ô tô. Lõi nam châm điện bên trong bộ lọc có tác dụng gì đối với việc kéo dài tuổi thọ động cơ?", [
        "Hút và giữ lại các mạt sắt kim loại li ti sinh ra do ma sát các chi tiết máy, ngăn không cho chúng quay lại làm xước piston và xi lanh",
        "Làm tăng nhiệt độ dầu bôi trơn lên mức sôi",
        "Hóa lỏng toàn bộ cặn dầu",
        "Tạo ra tia lửa đốt cháy muội than"
    ], 0, "Bẫy từ giữ lại các hạt mạt sắt siêu mịn trong nhớt, bảo vệ bề mặt xi lanh và piston không bị cào xước.")
]

exams["phys9_c7_b22_test3"] = make_exam(CH_ID, CH_TITLE, "phys9_c7_b22", "Bài 22: Từ trường của ống dây có dòng điện. Nam châm điện", 3, p1_b22_t3, p2_b22_t3, p3_b22_t3, p4_b22_t3)

print("Added phys9_c7_b22 (3 tests).")
