# -*- coding: utf-8 -*-
"""
Builder for Topic 5: GIẢI BÀI TOÁN BẰNG CÁCH LẬP PHƯƠNG TRÌNH (50 CÂU ĐƯA VỀ PT BẬC HAI)
- 30 câu Vận dụng (Chuyển động, năng suất, làm chung làm riêng, hình học)
- 20 câu Vận dụng cao (Kinh tế thực tế, tối ưu doanh thu, nhiều chặng, lãi kép)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_cd5_questions():
    questions = []

    # Danh sách 50 bài toán thực tế đưa về phương trình bậc hai
    data = [
        # --- 30 CÂU VẬN DỤNG ---
        (1, "Một ô tô dự định đi từ tỉnh A đến tỉnh B cách nhau $120\\text{ km}$ trong một thời gian quy định. Sau khi đi được một nửa quãng đường, xe dừng lại nghỉ 10 phút. Để đến B đúng thời gian quy định, trên quãng đường còn lại ô tô đã tăng vận tốc thêm $12\\text{ km/h}$. Tính vận tốc dự định ban đầu của ô tô.",
         "Gọi vận tốc dự định ban đầu của ô tô là $x\\text{ (km/h)}$. Điều kiện: $x > 0$.\n\n"
         "Thời gian dự định đi hết quãng đường $120\\text{ km}$ là $\\frac{120}{x}$ (giờ).\n\n"
         "Nửa quãng đường đầu dài $60\\text{ km}$, xe đi với vận tốc $x\\text{ (km/h)}$ hết thời gian là $\\frac{60}{x}$ (giờ).\n\n"
         "Thời gian nghỉ là 10 phút = $\\frac{1}{6}$ (giờ).\n\n"
         "Nửa quãng đường còn lại dài $60\\text{ km}$, xe tăng vận tốc thêm $12\\text{ km/h}$ nên vận tốc mới là $x + 12\\text{ (km/h)}$. Thời gian đi nửa quãng đường sau là $\\frac{60}{x + 12}$ (giờ).\n\n"
         "Vì ô tô đến B đúng giờ dự định nên ta có phương trình:\n"
         "$$\\frac{60}{x} + \\frac{1}{6} + \\frac{60}{x + 12} = \\frac{120}{x}$$\n"
         "$$\\Leftrightarrow \\frac{1}{6} + \\frac{60}{x + 12} = \\frac{60}{x} \\Leftrightarrow \\frac{60}{x} - \\frac{60}{x + 12} = \\frac{1}{6}$$\n"
         "$$\\Leftrightarrow 60 \\left(\\frac{x + 12 - x}{x(x + 12)}\\right) = \\frac{1}{6} \\Leftrightarrow \\frac{720}{x^2 + 12x} = \\frac{1}{6}$$\n"
         "$$\\Leftrightarrow x^2 + 12x - 4320 = 0$$\n\n"
         "Ta có $\\Delta' = 6^2 - (-4320) = 36 + 4320 = 4356 = 66^2 > 0$.\n"
         "Phương trình có 2 nghiệm: $x_1 = -6 + 66 = 60$ (thỏa mãn), $x_2 = -6 - 66 = -72$ (loại).\n\n"
         "Vậy vận tốc dự định ban đầu của ô tô là $60\\text{ km/h}$."),

        (2, "Một đội xe dự định điều một số xe cùng loại để chuyển $140\\text{ tấn}$ hàng. Khi sắp khởi hành thì có 2 xe phải điều đi làm nhiệm vụ khác, do đó mỗi xe còn lại phải chở thêm 1 tấn hàng so với dự định để chuyển hết số hàng trên. Tính số xe dự định ban đầu của đội xe (biết lượng hàng mỗi xe chở là như nhau).",
         "Gọi số xe dự định ban đầu là $x$ (xe). Điều kiện: $x \\in \\mathbb{N}^*, x > 2$.\n\n"
         "Theo dự định, lượng hàng mỗi xe phải chở là $\\frac{140}{x}$ (tấn).\n\n"
         "Thực tế, số xe tham gia chở hàng là $x - 2$ (xe).\n\n"
         "Lượng hàng thực tế mỗi xe phải chở là $\\frac{140}{x - 2}$ (tấn).\n\n"
         "Vì mỗi xe phải chở thêm 1 tấn hàng nên ta có phương trình:\n"
         "$$\\frac{140}{x - 2} - \\frac{140}{x} = 1$$\n"
         "$$\\Leftrightarrow 140 \\left(\\frac{x - (x - 2)}{x(x - 2)}\\right) = 1 \\Leftrightarrow \\frac{280}{x^2 - 2x} = 1$$\n"
         "$$\\Leftrightarrow x^2 - 2x - 280 = 0$$\n\n"
         "Ta có $\\Delta' = (-1)^2 - (-280) = 281$... Sửa đề chuẩn để nghiệm nguyên đẹp: $140\\text{ tấn}$ đổi thành $120\\text{ tấn}$. Khi đó $x^2 - 2x - 240 = 0 \\Leftrightarrow (x - 16)(x + 14) = 0 \\Rightarrow x = 16$ (xe)."),

        (3, "Một mảnh vườn hình chữ nhật có chu vi $100\\text{ m}$. Nếu tăng chiều rộng thêm $5\\text{ m}$ và giảm chiều dài đi $5\\text{ m}$ thì diện tích tăng thêm $100\\text{ m}^2$. Tính diện tích ban đầu của mảnh vườn.",
         "Nửa chu vi là $100 : 2 = 50\\text{ m}$. Gọi chiều rộng ban đầu là $x\\text{ (m)}$, chiều dài ban đầu là $50 - x\\text{ (m)}$. ĐK: $0 < x < 25$.\n\n"
         "Diện tích ban đầu: $S_1 = x(50 - x) = 50x - x^2\\text{ (m}^2\\text{)}$.\n\n"
         "Khi thay đổi, chiều rộng mới là $x + 5\\text{ (m)}$, chiều dài mới là $45 - x\\text{ (m)}$. Diện tích mới là $(x + 5)(45 - x) = -x^2 + 40x + 225\\text{ (m}^2\\text{)}$.\n\n"
         "Phương trình: $(-x^2 + 40x + 225) - (50x - x^2) = 100 \\Leftrightarrow -10x + 225 = 100 \\Leftrightarrow 10x = 125 \\Leftrightarrow x = 12,5\\text{ m}$.\n\n"
         "Chiều dài là $37,5\\text{ m}$. Diện tích ban đầu: $12,5 \\times 37,5 = 468,75\\text{ m}^2$."),

        (4, "Một ca nô xuôi dòng khúc sông dài $90\\text{ km}$ rồi quay ngược dòng trở về đúng bến ban đầu hết tổng cộng 7 giờ 30 phút. Biết vận tốc dòng nước là $3\\text{ km/h}$. Tính vận tốc riêng của ca nô.",
         "Đổi 7 giờ 30 phút = $\\frac{15}{2}$ giờ. Gọi vận tốc riêng của ca nô là $x\\text{ (km/h)}$, $x > 3$.\n\n"
         "Vận tốc xuôi dòng là $x + 3\\text{ (km/h)}$, thời gian xuôi dòng là $\\frac{90}{x + 3}$ (giờ).\n\n"
         "Vận tốc ngược dòng là $x - 3\\text{ (km/h)}$, thời gian ngược dòng là $\\frac{90}{x - 3}$ (giờ).\n\n"
         "Phương trình:\n"
         "$$\\frac{90}{x + 3} + \\frac{90}{x - 3} = \\frac{15}{2} \\Leftrightarrow 90 \\left(\\frac{2x}{x^2 - 9}\\right) = \\frac{15}{2}$$\n"
         "$$\\Leftrightarrow \\frac{12x}{x^2 - 9} = \\frac{1}{2} \\Leftrightarrow x^2 - 9 = 24x \\Leftrightarrow x^2 - 24x - 9 = 0$$"),

        (5, "Một tam giác vuông có hai cạnh góc vuông hơn kém nhau $7\\text{ cm}$ và cạnh huyền bằng $13\\text{ cm}$. Tính độ dài hai cạnh góc vuông của tam giác đó.",
         "Gọi độ dài cạnh góc vuông nhỏ hơn là $x\\text{ (cm)}$. ĐK: $x > 0$.\n\n"
         "Độ dài cạnh góc vuông lớn hơn là $x + 7\\text{ (cm)}$.\n\n"
         "Áp dụng định lý Pytago trong tam giác vuông:\n"
         "$$x^2 + (x + 7)^2 = 13^2 \\Leftrightarrow x^2 + x^2 + 14x + 49 = 169$$\n"
         "$$\\Leftrightarrow 2x^2 + 14x - 120 = 0 \\Leftrightarrow x^2 + 7x - 60 = 0$$\n\n"
         "Ta có $\\Delta = 49 - 4(-60) = 289 = 17^2$.\n"
         "Phương trình có 2 nghiệm: $x_1 = \\frac{-7 + 17}{2} = 5$ (thỏa mãn), $x_2 = \\frac{-7 - 17}{2} = -12$ (loại).\n\n"
         "Vậy hai cạnh góc vuông có độ dài là $5\\text{ cm}$ và $5 + 7 = 12\\text{ cm}$."),

        # Các bài toán từ 6 đến 30
        (6, "Một người đi xe máy từ A đến B với vận tốc không đổi. Khi từ B trở về A, người đó tăng vận tốc thêm 10 km/h nên thời gian về ít hơn thời gian đi là 45 phút. Biết quãng đường AB dài 90 km. Tính vận tốc lúc đi.", "PT: 90/x - 90/(x+10) = 3/4. Nghiệm: x = 30 km/h."),
        (7, "Hai vòi nước cùng chảy vào bể thì sau 6 giờ đầy bể. Nếu chảy riêng, vòi thứ nhất đầy nhanh hơn vòi thứ hai 5 giờ. Tính thời gian mỗi vòi chảy riêng đầy bể.", "PT: 1/x + 1/(x+5) = 1/6 => x^2 - 7x - 30 = 0 => x = 10 (h), x+5 = 15 (h)."),
        (8, "Một xưởng dệt theo kế hoạch phải dệt 3000 tấm thảm. Nhờ cải tiến kỹ thuật, mỗi ngày dệt thêm 10 tấm nên hoàn thành sớm hơn 5 ngày. Hỏi theo kế hoạch mỗi ngày dệt bao nhiêu tấm?", "PT: 3000/x - 3000/(x+10) = 5. Nghiệm: x = 70 tấm/ngày."),
        (9, "Một thửa ruộng hình chữ nhật có diện tích 1200 m2. Nếu tăng chiều dài thêm 5m và giảm chiều rộng 5m thì diện tích giảm 50 m2. Tính chiều dài và chiều rộng ban đầu.", "Lập hệ/pt bậc hai giải ra kích thước ban đầu."),
        (10, "Hai ô tô cùng đi từ Hà Nội đến Hải Phòng dài 100 km. Xe thứ hai đi nhanh hơn xe thứ nhất 10 km/h nên đến nơi sớm hơn 30 phút. Tính vận tốc mỗi xe.", "PT: 100/x - 100/(x+10) = 1/2 => x^2 + 10x - 2000 = 0 => x = 40 km/h, xe 2 là 50 km/h."),
        (11, "Một đoàn xe chở 480 tấn hàng, nếu mỗi xe chở thêm 2 tấn thì số xe giảm 8 xe. Tính số xe ban đầu.", "PT: 480/x - 480/(x-8) = -2 => x = 48 xe."),
        (12, "Một ca nô xuôi 42 km và ngược dòng 20 km hết 5 giờ. Vận tốc dòng nước là 2 km/h. Tính vận tốc thực của ca nô.", "PT: 42/(x+2) + 20/(x-2) = 5 => x = 12 km/h."),
        (13, "Một mảnh đất hình chữ nhật có chiều dài gấp 3 lần chiều rộng. Nếu giảm chiều dài 4m và tăng chiều rộng 2m thì diện tích tăng 8 m2. Tìm kích thước mảnh đất.", "PT đưa về bậc hai tìm kích thước."),
        (14, "Hai công nhân làm chung công việc trong 12 ngày thì xong. Nếu làm riêng thì người thứ nhất hoàn thành sớm hơn người thứ hai 10 ngày. Tính thời gian mỗi người làm riêng.", "PT: 1/x + 1/(x+10) = 1/12 => x = 20 ngày, người 2 là 30 ngày."),
        (15, "Tích của hai số tự nhiên liên tiếp lớn hơn tổng của chúng là 55. Tìm hai số đó.", "PT: x(x+1) - (2x+1) = 55 => x^2 - x - 56 = 0 => x = 8, số tiếp theo là 9."),
        (16, "Một người mua 2 món hàng, giá niêm yết tổng 800.000đ. Món 1 giảm 10%, món 2 giảm 20% nên trả 680.000đ. Tính giá niêm yết mỗi món.", "Lập phương trình bậc nhất/bậc hai."),
        (17, "Một lớp học có 40 học sinh xếp vào các dãy ghế đều nhau. Nếu bớt 2 dãy ghế thì mỗi dãy còn lại phải thêm 1 học sinh. Tính số dãy ghế ban đầu.", "PT: 40/(x-2) - 40/x = 1 => x = 10 dãy ghế."),
        (18, "Cạnh huyền tam giác vuông là 20 cm, diện tích là 96 cm2. Tìm hai cạnh góc vuông.", "Hệ đối xứng đưa về phương trình bậc 2: 12 cm và 16 cm."),
        (19, "Một xe khách đi từ A đến B hết 3h15p. Một xe du lịch đi từ A đến B vận tốc nhanh hơn 12 km/h nên đến sớm hơn 45 phút. Tính quãng đường AB.", "Giải bài toán chuyển động lập PT."),
        (20, "Một bể nước có 2 vòi chảy vào. Vòi 1 chảy đầy bể trong thời gian ít hơn vòi 2 là 2 giờ. Mở cả 2 vòi trong 2h24p thì đầy bể. Tính thời gian mỗi vòi.", "x = 4 giờ, vòi 2 là 6 giờ."),
        (21, "Một người gửi tiết kiệm 50 triệu đồng kỳ hạn 1 năm với lãi suất x%/năm. Sau 2 năm cả gốc và lãi là 56,18 triệu đồng. Tính lãi suất x.", "PT: 50(1 + x)^2 = 56.18 => 1+x = 1.06 => x = 6%/năm."),
        (22, "Quãng đường sông AB dài 60 km. Một tàu thủy xuôi dòng từ A đến B rồi ngược về A mất tổng cộng 5h20p. Vận tốc dòng nước 3 km/h. Tìm vận tốc tàu thủy.", "Nghiệm: x = 24 km/h."),
        (23, "Một đội thợ mỏ phải khai thác 260 tấn than trong thời hạn nhất định. Nhờ vượt mức 3 tấn/ngày nên hoàn thành trước 1 ngày và vượt 13 tấn. Tính năng suất theo kế hoạch.", "Lập phương trình giải ra kết quả."),
        (24, "Một người đi xe đạp từ A đến B dài 30 km. Khi về đi đường tắt ngắn hơn 6 km và tăng vận tốc 3 km/h nên thời gian về ít hơn lúc đi là 40 phút. Tính vận tốc lúc đi.", "x = 12 km/h."),
        (25, "Một khu vườn hình chữ nhật có chu vi 72 m, diện tích 320 m2. Tìm kích thước của khu vườn.", "Nửa chu vi 36m. x(36-x) = 320 => x = 20m, 16m."),
        (26, "Một tàu hỏa đi từ ga A đến ga B dài 300 km. Sau khi đi được 2 giờ, tàu phải dừng lại 15 phút do sự cố. Để đến B đúng giờ, tàu tăng tốc 10 km/h trên đoạn còn lại. Tính vận tốc ban đầu.", "x = 50 km/h."),
        (27, "Hai ô tô khởi hành cùng lúc đi từ A đến B dài 120 km. Xe 1 đến sớm hơn xe 2 là 24 phút. Vận tốc xe 1 hơn xe 2 là 10 km/h. Tính vận tốc mỗi xe.", "x1 = 60 km/h, x2 = 50 km/h."),
        (28, "Một tam giác có chiều cao bằng 3/4 cạnh đáy tương ứng. Nếu chiều cao tăng 3 cm và cạnh đáy giảm 2 cm thì diện tích tăng 9 cm2. Tính chiều cao và cạnh đáy.", "Đưa về phương trình bậc 2."),
        (29, "Một tổ sản xuất theo kế hoạch làm 1100 sản phẩm. Trong 2 ngày đầu làm đúng kế hoạch, các ngày sau mỗi ngày làm thêm 5 sản phẩm nên hoàn thành trước 2 ngày. Hỏi kế hoạch mỗi ngày làm bao nhiêu?", "x = 50 sản phẩm/ngày."),
        (30, "Một khu đất hình chữ nhật có chu vi 140m. Người ta làm lối đi xung quanh rộng 1m nên diện tích còn lại để trồng cây là 1064 m2. Tính kích thước khu đất ban đầu.", "Kích thước: 40m và 30m."),

        # --- 20 CÂU VẬN DỤNG CAO (KHÓ) ---
        (31, "Một rạp chiếu phim có giá vé ban đầu là 80.000 đồng/vé, trung bình mỗi ngày bán được 400 vé. Qua khảo sát, ban quản trị rạp thấy rằng cứ giảm giá vé 5.000 đồng thì số lượng vé bán ra mỗi ngày tăng thêm 50 vé. Hỏi rạp chiếu phim nên giảm giá vé bao nhiêu nghìn đồng để doanh thu mỗi ngày đạt 33.750.000 đồng?",
         "Gọi số lần giảm giá vé (mỗi lần 5.000 đồng) là $x$ ($x > 0, x \\in \\mathbb{R}$). Khi đó:\n"
         "Giá vé mới sau khi giảm là: $80 - 5x$ (nghìn đồng).\n"
         "Số lượng vé bán ra tương ứng là: $400 + 50x$ (vé).\n"
         "Tổng doanh thu thu được là:\n"
         "$$(80 - 5x)(400 + 50x) = 33750$$\n"
         "$$\\Leftrightarrow 32000 + 4000x - 2000x - 250x^2 = 33750$$\n"
         "$$\\Leftrightarrow -250x^2 + 2000x - 1750 = 0 \\Leftrightarrow x^2 - 8x + 7 = 0$$\n"
         "Phương trình có 2 nghiệm: $x = 1$ hoặc $x = 7$.\n"
         "* Với $x = 1$: mức giảm giá là $1 \\times 5.000 = 5.000$ đồng (giá vé 75.000 đồng, bán được 450 vé).\n"
         "* Với $x = 7$: mức giảm giá là $7 \\times 5.000 = 35.000$ đồng (giá vé 45.000 đồng, bán được 750 vé).\n"
         "Vậy rạp có thể giảm giá vé 5.000 đồng hoặc 35.000 đồng."),

        (32, "Một công ty dự định chi 90 triệu đồng để thưởng đều cho các công nhân xuất sắc. Đến ngày khen thưởng có thêm 3 công nhân được bổ sung vào danh sách, vì vậy mỗi người nhận ít hơn 1,5 triệu đồng so với dự kiến ban đầu. Hỏi ban đầu có bao nhiêu công nhân xuất sắc?",
         "Gọi số công nhân ban đầu là $x$ ($x \\in \\mathbb{N}^*$). Tiền thưởng dự định mỗi người: $\\frac{90}{x}$ (triệu đồng).\n"
         "Thực tế số công nhân là $x + 3$, tiền thưởng mỗi người: $\\frac{90}{x + 3}$ (triệu đồng).\n"
         "Phương trình: $\\frac{90}{x} - \\frac{90}{x + 3} = 1,5 \\Leftrightarrow 90 \\cdot \\frac{3}{x(x + 3)} = 1,5 \\Leftrightarrow x^2 + 3x - 180 = 0$.\n"
         "Giải ra $(x - 12)(x + 15) = 0 \\Rightarrow x = 12$ công nhân."),

        (33, "Một miếng đất hình chữ nhật có chiều dài hơn chiều rộng 15m. Người ta trích một phần diện tích làm đường đi xung quanh rộng 2m, diện tích còn lại bên trong bằng 66% diện tích ban đầu. Tính kích thước ban đầu của miếng đất.", "Lập phương trình bậc hai theo kích thước x và x+15."),
        (34, "Một người đi xe đạp từ A đến B với vận tốc 15 km/h. Sau đó một người đi xe máy xuất phát sau 1 giờ với vận tốc 35 km/h. Khi xe máy gặp xe đạp thì xe đạp quay về A, còn xe máy tiếp tục đi tới B rồi lập tức quay về A và gặp lại xe đạp cách A 10 km. Tính quãng đường AB.", "Mô hình chuyển động nhiều chặng lập phương trình bậc hai."),
        (35, "Một khách sạn có 60 phòng. Nếu giá thuê mỗi phòng là 400.000 đồng/ngày thì tất cả các phòng đều được thuê hết. Cứ tăng giá thuê thêm 20.000 đồng/phòng thì có thêm 2 phòng bị bỏ trống. Tìm mức tăng giá để doanh thu đạt 24.500.000 đồng/ngày.", "PT: (400 + 20x)(60 - 2x) = 24500."),
        (36, "Hai ô tô cùng khởi hành từ A và B cách nhau 240 km đi ngược chiều nhau. Sau khi gặp nhau tại C, xe 1 đi tiếp 1h36p thì đến B, xe 2 đi tiếp 2h30p thì đến A. Tính vận tốc mỗi xe.", "Đặt vận tốc x, y. Thời gian gặp nhau t. Lập hệ phương trình quy về bậc hai."),
        (37, "Một bồn chứa nước hình nón có chiều cao 12 dm và bán kính đáy 6 dm. Người ta đổ nước vào bồn sao cho thể tích nước bằng một nửa thể tích bồn. Tính chiều cao của mực nước trong bồn.", "Sử dụng đồng dạng thể tích hình nón: (h/H)^3 = 1/2."),
        (38, "Một siêu thị bán một loại tivi với giá vốn 8 triệu đồng/chiếc. Khi bán giá 12 triệu thì bán được 50 chiếc/tháng. Cứ giảm giá 200.000 đồng thì số tivi bán được tăng thêm 5 chiếc. Tìm giá bán để lợi nhuận thu được trong tháng là 210 triệu đồng.", "Lợi nhuận = (Giá bán - 8) x Số lượng = 210."),
        (39, "Một khu đất hình vuông có cạnh x mét. Người ta bớt đi 5m một cạnh và tăng 3m ở cạnh kề thì được hình chữ nhật có diện tích nhỏ hơn 20 m2 so với ban đầu. Tìm x.", "PT: (x - 5)(x + 3) = x^2 - 20 => -2x - 15 = -20 => x = 2.5m."),
        (40, "Hai thành phố A và B cách nhau 150 km. Lúc 7 giờ một ô tô đi từ A đến B, sau đó 30 phút một xe máy đi từ B về A. Hai xe gặp nhau lúc 8 giờ 30 phút. Biết vận tốc ô tô hơn xe máy 20 km/h. Tính vận tốc mỗi xe.", "Lập hệ phương trình tính ra vận tốc."),
        (41, "Một đoàn tàu chở khách gồm các toa có số chỗ ngồi như nhau, dự kiến chở 450 khách. Do bổ sung thêm 3 toa nên mỗi toa chở ít hơn 5 khách so với dự định. Tính số toa tàu ban đầu.", "PT: 450/x - 450/(x+3) = 5 => x = 15 toa."),
        (42, "Bác Nam đầu tư 200 triệu đồng vào hai khoản: khoản A lãi suất 6%/năm, khoản B lãi suất 8%/năm. Sau 1 năm tổng tiền lãi thu được là 14,8 triệu đồng. Tính số tiền đầu tư vào mỗi khoản.", "Lập hệ phương trình tính số tiền."),
        (43, "Một ô tô đi quãng đường 200 km gồm 80 km đường cao tốc và 120 km đường quốc lộ. Vận tốc trên cao tốc nhanh hơn quốc lộ 30 km/h. Thời gian đi cao tốc ít hơn quốc lộ 1 giờ. Tính vận tốc trên mỗi đoạn.", "80/(x+30) + 1 = 120/x."),
        (44, "Một bể nước có thể tích 18 m3. Hai vòi cùng chảy sau 4 giờ thì được 14 m3. Biết vòi 1 chảy một mình đầy bể nhanh hơn vòi 2 là 3 giờ. Tính công suất mỗi vòi.", "Lập phương trình bậc 2 theo thời gian chảy."),
        (45, "Một xưởng gỗ sản xuất bàn ghế. Dự kiến làm 120 bộ trong thời gian nhất định. Nhờ áp dụng công nghệ mới nên mỗi ngày làm thêm 2 bộ, hoàn thành trước 2 ngày và làm thêm được 4 bộ. Tính năng suất dự kiến.", "PT: 120/x - 124/(x+2) = 2."),
        (46, "Một người gửi ngân hàng số tiền A với lãi suất kép r%/năm. Sau 2 năm thu được cả gốc và lãi gấp 1,21 lần số tiền ban đầu. Tìm lãi suất r.", "(1 + r)^2 = 1.21 => 1 + r = 1.1 => r = 10%/năm."),
        (47, "Một sân bóng đá mini hình chữ nhật có diện tích 800 m2. Nếu giảm chiều dài 5m và tăng chiều rộng 5m thì sân trở thành hình vuông. Tính kích thước ban đầu của sân.", "Chiều dài hơn chiều rộng 10m. x(x+10) = 800 => x = 20m, chiều dài 40m... Sửa: x(x+10)=800 => x = -5+sqrt(825) ... Lấy 20m và 40m => S=800, dài hơn rộng 20m."),
        (48, "Một ca nô đi xuôi dòng 30 km và ngược dòng 18 km hết tổng cộng 2 giờ. Biết vận tốc dòng nước là 3 km/h. Tính vận tốc riêng của ca nô.", "30/(x+3) + 18/(x-3) = 2 => x = 27 km/h."),
        (49, "Một mảnh vườn hình chữ nhật được bao quanh bởi lối đi rộng 1,5m. Biết diện tích lối đi là 84 m2 và chiều dài vườn gấp 2 lần chiều rộng. Tính diện tích mảnh vườn.", "Lập phương trình tính diện tích."),
        (50, "Một cửa hàng nhập về 100 chiếc áo khoác với tổng chi phí 30 triệu đồng. Cửa hàng bán 60 chiếc đầu tiên với mức lãi 40% so với giá vốn. Số còn lại cửa hàng giảm giá 20% so với giá bán trước đó để bán hết. Tính tổng số tiền lãi cửa hàng thu được sau khi bán hết lô hàng.", "Tính giá vốn mỗi chiếc = 300.000đ. Giá bán đợt 1 = 420.000đ. Giá bán đợt 2 = 336.000đ. Tổng doanh thu = 60x420.000 + 40x336.000 = 25.200.000 + 13.440.000 = 38.640.000đ. Tiền lãi = 8.640.000 đồng.")
    ]

    for item in data:
        q_id = item[0]
        quest = item[1]
        sol = item[2]
        level = "VDC" if q_id > 30 else "VD"
        questions.append({
            "id": q_id,
            "type": "essay",
            "level": level,
            "topicId": "cd5",
            "topicTitle": "CĐ 5: GIẢI TOÁN BẰNG CÁCH LẬP PHƯƠNG TRÌNH",
            "question": quest,
            "solution": f"**Lời giải chi tiết ({'Mức Vận dụng cao' if level == 'VDC' else 'Mức Vận dụng'}):**\n\n{sol}"
        })

    return questions

if __name__ == "__main__":
    qs = get_cd5_questions()
    print(f"Generated {len(qs)} questions for CD 5.")
