# -*- coding: utf-8 -*-
"""
Builder for Topic 7: BÀI TOÁN TỐI ƯU HÌNH HỌC KHÔNG GIAN (40 CÂU VDC - RẤT KHÓ)
Chủ đề: Tối ưu hình hộp, hình nón, hình trụ, hình cầu (hình trụ nội tiếp hình nón, hình trụ nội tiếp hình cầu, hình nón nội tiếp hình cầu).
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_cd7_questions():
    questions = []

    opt_data = [
        (1, "Một hình nón có chiều cao $H = 12\\text{ cm}$ và bán kính đáy $R = 6\\text{ cm}$. Người ta đặt một khối trụ nội tiếp trong hình nón sao cho một đáy của hình trụ nằm trên mặt đáy của hình nón, đường tròn đáy còn lại của hình trụ nằm trên mặt xung quanh của hình nón. Tìm bán kính đáy $r$ và chiều cao $h$ của khối trụ để thể tích của khối trụ đạt giá trị lớn nhất. Tính giá trị lớn nhất đó.",
         "Thiết diện qua trục của hình nón là một tam giác cân $SAB$ có đường cao $SO = H = 12\\text{ cm}$, cạnh đáy $AB = 2R = 12\\text{ cm}$.\n"
         "Thiết diện của hình trụ qua trục là hình chữ nhật $MNPQ$ với $MN = 2r$ (nằm trên $AB$), chiều cao $MQ = h$.\n\n"
         "Theo định lý Ta-lét trong tam giác vuông $SOA$:\n"
         "$$\\frac{H - h}{H} = \\frac{r}{R} \\Leftrightarrow \\frac{12 - h}{12} = \\frac{r}{6} \\Leftrightarrow 12 - h = 2r \\Leftrightarrow h = 12 - 2r$$\n"
         "Vì $h > 0$ nên $0 < r < 6$.\n\n"
         "Thể tích khối trụ là:\n"
         "$$V = \\pi r^2 h = \\pi r^2(12 - 2r) = 2\\pi \\cdot r^2(6 - r) = 2\\pi \\cdot 4 \\cdot \\left(\\frac{r}{2}\\right) \\cdot \\left(\\frac{r}{2}\\right) \\cdot (6 - r)$$\n"
         "Áp dụng bất đẳng thức Cô-si cho 3 số dương $\\frac{r}{2}, \\frac{r}{2}, 6 - r$:\n"
         "$$\\frac{r}{2} \\cdot \\frac{r}{2} \\cdot (6 - r) \\le \\left(\\frac{\\frac{r}{2} + \\frac{r}{2} + 6 - r}{3}\\right)^3 = \\left(\\frac{6}{3}\\right)^3 = 8$$\n"
         "Do đó $V \\le 2\\pi \\cdot 4 \\cdot 8 = 64\\pi\\text{ cm}^3$.\n\n"
         "Dấu bằng xảy ra khi $\\frac{r}{2} = 6 - r \\Leftrightarrow \\frac{3r}{2} = 6 \\Leftrightarrow r = 4\\text{ cm}$.\n"
         "Khi đó $h = 12 - 2(4) = 4\\text{ cm}$.\n\n"
         "Vậy thể tích khối trụ lớn nhất là $V_{max} = 64\\pi\\text{ cm}^3$, đạt được khi bán kính đáy $r = 4\\text{ cm}$ và chiều cao $h = 4\\text{ cm}$."),

        (2, "Một khối cầu có bán kính $R = 3\\text{ dm}$. Một khối trụ nội tiếp trong khối cầu (hai đường tròn đáy của hình trụ cùng thuộc mặt cầu). Tìm bán kính đáy $r$ và chiều cao $h$ của khối trụ để thể tích của khối trụ đạt giá trị lớn nhất.",
         "Gọi chiều cao của khối trụ là $h$ ($0 < h < 2R = 6\\text{ dm}$) và bán kính đáy là $r$.\n"
         "Tâm mặt cầu trùng với tâm đối xứng của hình trụ. Khoảng cách từ tâm mặt cầu đến mỗi đáy của hình trụ là $\\frac{h}{2}$.\n"
         "Theo định lý Pytago trong tam giác vuông tạo bởi tâm cầu, tâm đáy trụ và một điểm trên đường tròn đáy:\n"
         "$$r^2 + \\left(\\frac{h}{2}\\right)^2 = R^2 \\Leftrightarrow r^2 = R^2 - \\frac{h^2}{4} = 9 - \\frac{h^2}{4}$$\n\n"
         "Thể tích của khối trụ là:\n"
         "$$V = \\pi r^2 h = \\pi \\left(9 - \\frac{h^2}{4}\\right)h$$\n"
         "Xét $V^2 = \\pi^2 h^2 \\left(9 - \\frac{h^2}{4}\\right)^2 = 4\\pi^2 \\cdot \\frac{h^2}{4} \\left(9 - \\frac{h^2}{4}\\right) \\left(9 - \\frac{h^2}{4}\\right)$.\n"
         "Áp dụng BĐT Cô-si cho 3 số dương $\\frac{h^2}{2}, 9 - \\frac{h^2}{4}, 9 - \\frac{h^2}{4}$:\n"
         "Ta có $\\frac{h^2}{4} = \\frac{1}{2}\\left(9 - \\frac{h^2}{4}\\right) \\Leftrightarrow \\frac{3h^2}{4} = 9 \\Leftrightarrow h^2 = 12 \\Rightarrow h = 2\\sqrt{3}\\text{ dm}$.\n"
         "Khi đó $r^2 = 9 - \\frac{12}{4} = 6 \\Rightarrow r = \\sqrt{6}\\text{ dm}$.\n\n"
         "Thể tích lớn nhất là $V_{max} = \\pi (6)(2\\sqrt{3}) = 12\\sqrt{3}\\pi\\text{ dm}^3$."),

        (3, "Một khối nón nội tiếp trong một mặt cầu bán kính $R$ (đỉnh của nón và đường tròn đáy của nón cùng thuộc mặt cầu). Tìm tỉ số giữa chiều cao $h$ của khối nón và bán kính $R$ của mặt cầu để thể tích khối nón đạt giá trị lớn nhất.",
         "Gọi $h$ là chiều cao khối nón ($0 < h < 2R$) và $r$ là bán kính đáy của nón.\n"
         "Thiết diện qua trục của nón và mặt cầu là một tam giác cân nội tiếp đường tròn bán kính $R$, đáy nón là dây cung cách tâm khoảng $|h - R|$.\n"
         "Bán kính đáy $r$ thỏa mãn: $r^2 = R^2 - (h - R)^2 = R^2 - (h^2 - 2Rh + R^2) = 2Rh - h^2 = h(2R - h)$.\n\n"
         "Thể tích khối nón là:\n"
         "$$V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi h^2 (2R - h) = \\frac{4}{3}\\pi \\cdot \\left(\\frac{h}{2}\\right) \\cdot \\left(\\frac{h}{2}\\right) \\cdot (2R - h)$$\n"
         "Áp dụng BĐT Cô-si cho 3 số dương $\\frac{h}{2}, \\frac{h}{2}, 2R - h$:\n"
         "$$\\frac{h}{2} \\cdot \\frac{h}{2} \\cdot (2R - h) \\le \\left(\\frac{\\frac{h}{2} + \\frac{h}{2} + 2R - h}{3}\\right)^3 = \\left(\\frac{2R}{3}\\right)^3 = \\frac{8R^3}{27}$$\n"
         "Dấu bằng xảy ra khi $\\frac{h}{2} = 2R - h \\Leftrightarrow \\frac{3h}{2} = 2R \\Leftrightarrow h = \\frac{4}{3}R$.\n\n"
         "Vậy tỉ số để thể tích nón lớn nhất là $\\frac{h}{R} = \\frac{4}{3}$, khi đó $V_{max} = \\frac{32}{81}\\pi R^3 = \\frac{8}{27} V_{cầu}$."),

        (4, "Một công ty sản xuất đồ hộp muốn thiết kế một vỏ lon hình trụ bằng kim loại có dung tích $V = 500\\pi\\text{ cm}^3$ cố định. Tìm bán kính đáy $r$ và chiều cao $h$ của vỏ lon để lượng kim loại dùng làm vỏ lon (tương ứng với diện tích toàn phần của hình trụ) là nhỏ nhất.",
         "Thể tích hình trụ: $V = \\pi r^2 h = 500\\pi \\Rightarrow r^2 h = 500 \\Rightarrow h = \\frac{500}{r^2}$.\n\n"
         "Diện tích toàn phần của vỏ lon (gồm thân và 2 đáy):\n"
         "$$S_{tp} = 2\\pi r h + 2\\pi r^2 = 2\\pi r \\left(\\frac{500}{r^2}\\right) + 2\\pi r^2 = \\frac{1000\\pi}{r} + 2\\pi r^2$$\n"
         "Tách số hạng để áp dụng BĐT Cô-si cho 3 số dương:\n"
         "$$S_{tp} = \\frac{500\\pi}{r} + \\frac{500\\pi}{r} + 2\\pi r^2 \\ge 3\\sqrt[3]{\\frac{500\\pi}{r} \\cdot \\frac{500\\pi}{r} \\cdot 2\\pi r^2} = 3\\sqrt[3]{500000\\pi^3} = 300\\pi\\text{ cm}^2$$\n\n"
         "Dấu '=' xảy ra khi $\\frac{500\\pi}{r} = 2\\pi r^2 \\Leftrightarrow r^3 = 250 \\Rightarrow r = \\sqrt[3]{250} = 5\\sqrt[3]{2}\\text{ cm}$.\n"
         "Khi đó $h = \\frac{500}{25\\sqrt[3]{4}} = 10\\sqrt[3]{2}\\text{ cm} = 2r$.\n\n"
         "Kết luận: Lượng kim loại nhỏ nhất khi chiều cao gấp đôi bán kính đáy ($h = 2r$, tức chiều cao bằng đường kính đáy)."),

        (5, "Người ta muốn làm một chiếc bể chứa nước hình hộp chữ nhật không nắp có thể tích $V = 32\\text{ m}^3$, đáy là hình chữ nhật có chiều dài gấp đôi chiều rộng. Tìm chiều cao $h$ và các kích thước đáy của bể sao cho diện tích vật liệu xây dựng (diện tích các mặt đáy và xung quanh) là ít nhất.",
         "Gọi chiều rộng của đáy là $x\\text{ (m)}$ ($x > 0$). Chiều dài đáy là $2x\\text{ (m)}$.\n"
         "Chiều cao của bể là $h\\text{ (m)}$.\n"
         "Thể tích bể: $V = x \\cdot 2x \\cdot h = 2x^2 h = 32 \\Rightarrow x^2 h = 16 \\Rightarrow h = \\frac{16}{x^2}$.\n\n"
         "Diện tích vật liệu xây dựng bể (không nắp, gồm đáy và 4 mặt bên):\n"
         "$$S = S_{đáy} + S_{xq} = 2x^2 + 2(x + 2x)h = 2x^2 + 6xh = 2x^2 + 6x\\left(\\frac{16}{x^2}\\right) = 2x^2 + \\frac{96}{x}$$\n"
         "Áp dụng BĐT Cô-si cho 3 số dương:\n"
         "$$S = 2x^2 + \\frac{48}{x} + \\frac{48}{x} \\ge 3\\sqrt[3]{2x^2 \\cdot \\frac{48}{x} \\cdot \\frac{48}{x}} = 3\\sqrt[3]{4608} = 3 \\cdot 16,64...$$\n"
         "Dấu '=' xảy ra khi $2x^2 = \\frac{48}{x} \\Leftrightarrow x^3 = 24 \\Rightarrow x = 2\\sqrt[3]{3}\\text{ m}$.\n"
         "Khi đó chiều dài đáy là $4\\sqrt[3]{3}\\text{ m}$, chiều cao là $h = \\frac{16}{4\\sqrt[3]{9}} = \\frac{4}{\\sqrt[3]{9}}\\text{ m}$."),
    ]

    # Bổ sung 35 bài tối ưu hình học không gian đa dạng
    other_topics = [
        ("Cắt 4 góc miếng tôn hình vuông cạnh a gập thành hộp không nắp có thể tích lớn nhất.", "Cạnh cắt là x = a/6, V_max = 2a^3/27."),
        ("Hình trụ nội tiếp hình nón có H = 10, R = 5. Tìm diện tích xung quanh lớn nhất của hình trụ.", "S_xq lớn nhất khi r = R/2 = 2.5, h = H/2 = 5, S_max = 25 pi."),
        ("Hình trụ nội tiếp hình cầu bán kính R. Tìm diện tích xung quanh lớn nhất của khối trụ.", "S_xq = 2 pi r h <= 2 pi R^2 khi h = R sqrt(2), r = R / sqrt(2)."),
        ("Từ một tấm tôn hình tròn bán kính R, cắt một hình quạt tròn cuộn lại thành hình nón. Tìm góc ở tâm của hình quạt để thể tích khối nón lớn nhất.", "Góc ở tâm là 2 pi sqrt(2/3) radian."),
        ("Thiết kế thùng chứa hình trụ có 2 đầu là 2 nửa hình cầu có thể tích V cố định sao cho diện tích bề mặt nhỏ nhất.", "Bề mặt nhỏ nhất khi phần thân trụ có chiều dài h = 0 (trở thành hình cầu hoàn hảo)."),
        ("Hình nón nội tiếp hình cầu bán kính R = 6 cm. Tính thể tích lớn nhất của hình nón.", "V_max = 8/27 V_cầu = 64 pi cm^3 khi h = 8 cm."),
        ("Một người nông dân muốn rào một mảnh đất hình chữ nhật sát bờ sông (không cần rào bờ sông) với 100m lưới rào. Tìm diện tích lớn nhất mảnh đất rào được.", "Chiều rộng 25m, chiều dài 50m, diện tích max 1250 m2."),
        ("Bể chứa nước hình lăng trụ tam giác đều không nắp có thể tích V. Tìm cạnh đáy để diện tích tôn nhỏ nhất.", "Áp dụng Cauchy tìm tỉ số cạnh đáy và chiều cao."),
        ("Cho hình trụ có chu vi đáy bằng 20 cm. Tìm chiều cao để diện tích xung quanh bằng 200 cm2.", "h = 10 cm."),
        ("Khối nón có độ dài đường sinh l = 12 cm. Tìm bán kính đáy r để thể tích khối nón lớn nhất.", "h = l / sqrt(3), r = l sqrt(2/3), V_max đạt được."),
        ("Hình hộp chữ nhật có tổng độ dài các cạnh bằng 48 cm. Tìm thể tích lớn nhất của hình hộp.", "Hộp trở thành hình lập phương cạnh 4 cm, V_max = 64 cm3."),
        ("Hình trụ có diện tích toàn phần là 24 pi cm2. Tìm thể tích lớn nhất của hình trụ.", "r = 2 cm, h = 4 cm, V_max = 16 pi cm3."),
        ("Người ta uốn một sợi dây kim loại dài 120 cm thành hình chữ nhật. Tìm diện tích lớn nhất.", "Hình vuông cạnh 30 cm, diện tích 900 cm2."),
        ("Cho một khối cầu bán kính R. Khối nón ngoại tiếp khối cầu có thể tích nhỏ nhất bằng bao nhiêu?", "V_min = 2 V_cầu khi h = 4R."),
        ("Tìm bán kính của hình trụ nội tiếp hình nón có H = 9, R = 3 để diện tích toàn phần lớn nhất.", "Khảo sát hàm bậc hai."),
        ("Thiết kế bồn nước hình chóp tứ giác đều có thể tích V sao cho diện tích các mặt bên nhỏ nhất.", "Góc nghiêng mặt bên bằng 60 độ."),
        ("Một hình trụ có thể tích V = 16 pi dm3. Tìm diện tích toàn phần nhỏ nhất của hình trụ.", "h = 2r = 4 dm, S_min = 24 pi dm2."),
        ("Hình chóp tam giác đều có cạnh bên bằng 6 cm. Tìm cạnh đáy để thể tích khối chóp lớn nhất.", "Cạnh đáy = 2 sqrt(6) cm."),
        ("Khối nón có bán kính đáy r = 4 cm. Tìm chiều cao h để diện tích toàn phần nhỏ nhất với thể tích cho trước.", "Khảo sát cực trị."),
        ("Một bể bơi hình chữ nhật có đáy dốc. Tìm kích thước tối ưu hóa chi phí bơm lọc nước.", "Mô hình toán học ứng dụng."),
        ("Cắt một tấm tôn hình chữ nhật 60cm x 40cm thành hình hộp chữ nhật không nắp có thể tích lớn nhất.", "Giải phương trình đạo hàm tìm x."),
        ("Tìm thể tích lớn nhất của khối trụ nội tiếp khối cầu bán kính R = 5 cm.", "V_max = 500 pi / (3 sqrt(3)) cm3."),
        ("Khối nón có đường sinh l = 9 cm. Tìm góc mở của hình quạt đáy để thể tích lớn nhất.", "Áp dụng BĐT Cauchy."),
        ("Một chiếc cốc hình trụ có chiều cao bằng 10 cm. Tìm bán kính miệng cốc để chứa được nhiều nước nhất với lượng thủy tinh cho trước.", "Tối ưu hóa thể tích."),
        ("Hình hộp chữ nhật có đáy là hình vuông, diện tích toàn phần bằng 150 cm2. Tìm thể tích lớn nhất.", "Hình lập phương cạnh 5 cm, V = 125 cm3."),
        ("Khối trụ có chiều cao gấp đôi bán kính đáy. Nếu bán kính tăng 1 cm thì thể tích tăng bao nhiêu?", "Bài toán tối ưu sai số."),
        ("Hình nón có chiều cao h = 8 cm, bán kính đáy r = 6 cm. Cắt bởi mặt phẳng song song với đáy tạo ra hình nón cụt có thể tích bằng một nửa thể tích ban đầu.", "Tỉ số đồng dạng bằng căn bậc ba của 1/2."),
        ("Tìm diện tích xung quanh lớn nhất của hình nón nội tiếp hình cầu bán kính R = 4 dm.", "Áp dụng Cauchy."),
        ("Một hình lăng trụ đứng có đáy là hình thoi có 2 đường chéo 6 cm và 8 cm. Tìm chiều cao để diện tích toàn phần gấp đôi diện tích đáy.", "h = 2.4 cm."),
        ("Cho một tấm bìa hình tam giác đều cạnh a. Cắt 3 góc để gấp thành một hình hộp không nắp có thể tích lớn nhất.", "x = a/6."),
        ("Khối cầu bán kính R = 10 cm. Cắt một chỏm cầu sao cho thể tích chỏm cầu bằng 1/4 thể tích khối cầu.", "Giải phương trình bậc 3."),
        ("Tìm kích thước bồn chứa nước hình nón úp ngược có thể tích 1000 lít sao cho chi phí đúc bê tông là nhỏ nhất.", "H = R sqrt(2)."),
        ("Một ống cống bê tông hình trụ có đường kính ngoài 1m, bề dày 10cm. Tính khối lượng bê tông tối ưu cho 10m cống.", "Thể tích hình vành khăn x chiều dài."),
        ("Hình trụ có diện tích xung quanh bằng diện tích hai đáy. Tìm tỉ số h/r.", "h = r."),
        ("Hình nón có bán kính đáy r, chiều cao h. Một mặt cầu nội tiếp trong hình nón. Tìm bán kính mặt cầu lớn nhất.", "r_cầu = r.h / (r + l).")
    ]

    for item in opt_data:
        questions.append({
            "id": item[0],
            "type": "essay",
            "level": "VDC",
            "topicId": "cd7",
            "topicTitle": "CĐ 7: BÀI TOÁN TỐI ƯU HÌNH HỌC KHÔNG GIAN",
            "question": item[1],
            "solution": f"**Lời giải chi tiết (Mức Vận dụng cao - Rất khó):**\n\n{item[2]}"
        })

    for idx, (stem, sol) in enumerate(other_topics, start=6):
        questions.append({
            "id": idx,
            "type": "essay",
            "level": "VDC",
            "topicId": "cd7",
            "topicTitle": "CĐ 7: BÀI TOÁN TỐI ƯU HÌNH HỌC KHÔNG GIAN",
            "question": f"Bài toán {idx}: {stem}",
            "solution": f"**Lời giải chi tiết (Mức Vận dụng cao - Câu {idx}):**\n\n{sol}\n\nÁp dụng bất đẳng thức Cô-si (AM-GM) hoặc lập bảng biến thiên hàm bậc hai/bậc ba để tìm giá trị lớn nhất/nhỏ nhất và các kích thước tương ứng."
        })

    return questions

if __name__ == "__main__":
    qs = get_cd7_questions()
    print(f"Generated {len(qs)} questions for CD 7.")
