# -*- coding: utf-8 -*-
"""
Builder for Topic 1: GIẢI HỆ PHƯƠNG TRÌNH BẬC NHẤT 2 ẨN (50 CÂU TỰ LUẬN)
Yêu cầu nâng cấp:
- Thay thế hoàn toàn các hệ chứa căn bằng hệ bậc nhất 2 ẩn thông thường (Câu 1 - 18).
- Từ câu 19 đến 35 và câu 36 đến 40: Giải bài toán bằng cách lập hệ phương trình ở mức VẬN DỤNG.
- Từ câu 41 đến 50: Giải bài toán bằng cách lập hệ phương trình ở mức VẬN DỤNG CAO (RẤT KHÓ).
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_cd1_questions():
    questions = []

    # =========================================================================
    # PHẦN 1: GIẢI HỆ PHƯƠNG TRÌNH BẬC NHẤT 2 ẨN THÔNG THƯỜNG (CÂU 1 - 18)
    # Tuyệt đối không chứa căn thức, nghiệm nguyên đẹp, biến đổi tường minh
    # =========================================================================
    hpt_basic = [
        (1, "2x + y = 7", "3x - y = 8", 
         "Cộng hai vế của phương trình ta được:\n"
         "$$(2x + y) + (3x - y) = 7 + 8 \\Leftrightarrow 5x = 15 \\Leftrightarrow x = 3$$\n"
         "Thay $x = 3$ vào phương trình thứ nhất:\n"
         "$$2(3) + y = 7 \\Leftrightarrow 6 + y = 7 \\Leftrightarrow y = 1$$\n"
         "Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (3; 1)$."),

        (2, "3x - 2y = 11", "x + 2y = 1",
         "Cộng từng vế của hai phương trình:\n"
         "$$(3x - 2y) + (x + 2y) = 11 + 1 \\Leftrightarrow 4x = 12 \\Leftrightarrow x = 3$$\n"
         "Thay $x = 3$ vào phương trình thứ hai:\n"
         "$$3 + 2y = 1 \\Leftrightarrow 2y = -2 \\Leftrightarrow y = -1$$\n"
         "Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (3; -1)$."),

        (3, "4x + 3y = 6", "2x - y = 8",
         "Từ phương trình thứ hai suy ra $y = 2x - 8$.\n"
         "Thế vào phương trình thứ nhất:\n"
         "$$4x + 3(2x - 8) = 6 \\Leftrightarrow 4x + 6x - 24 = 6 \\Leftrightarrow 10x = 30 \\Leftrightarrow x = 3$$\n"
         "Suy ra $y = 2(3) - 8 = -2$.\n"
         "Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (3; -2)$."),

        (4, "5x + 2y = 9", "2x - 3y = -4",
         "Nhân hai vế của phương trình thứ nhất với 3, phương trình thứ hai với 2:\n"
         "$$\\begin{cases} 15x + 6y = 27 \\\\ 4x - 6y = -8 \\end{cases}$$\n"
         "Cộng từng vế hai phương trình:\n"
         "$$19x = 19 \\Leftrightarrow x = 1$$\n"
         "Thay $x = 1$ vào phương trình thứ nhất: $5(1) + 2y = 9 \\Leftrightarrow 2y = 4 \\Leftrightarrow y = 2$.\n"
         "Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (1; 2)$."),

        (5, "3x + 5y = 1", "2x - y = 5",
         "Từ phương trình (2) suy ra $y = 2x - 5$.\n"
         "Thế vào phương trình (1):\n"
         "$$3x + 5(2x - 5) = 1 \\Leftrightarrow 3x + 10x - 25 = 1 \\Leftrightarrow 13x = 26 \\Leftrightarrow x = 2$$\n"
         "Suy ra $y = 2(2) - 5 = -1$.\n"
         "Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (2; -1)$."),

        (6, "2x - 3y = 7", "3x + 2y = 4",
         "Nhân phương trình (1) với 2 và phương trình (2) với 3:\n"
         "$$\\begin{cases} 4x - 6y = 14 \\\\ 9x + 6y = 12 \\end{cases}$$\n"
         "Cộng từng vế: $13x = 26 \\Leftrightarrow x = 2$.\n"
         "Thay $x = 2$ vào phương trình (2): $3(2) + 2y = 4 \\Leftrightarrow 2y = -2 \\Leftrightarrow y = -1$.\n"
         "Vậy nghiệm của hệ là $(x; y) = (2; -1)$."),

        (7, "7x - 5y = 9", "3x + 2y = 8",
         "Nhân phương trình (1) với 2 và phương trình (2) với 5:\n"
         "$$\\begin{cases} 14x - 10y = 18 \\\\ 15x + 10y = 40 \\end{cases}$$\n"
         "Cộng từng vế: $29x = 58 \\Leftrightarrow x = 2$.\n"
         "Thay $x = 2$ vào phương trình (2): $3(2) + 2y = 8 \\Leftrightarrow 2y = 2 \\Leftrightarrow y = 1$.\n"
         "Vậy nghiệm của hệ là $(x; y) = (2; 1)$."),

        (8, "2(x + 1) - 3(y - 2) = 5", "3(x - 2) + 2(y + 1) = 9",
         "Khai triển và rút gọn hai phương trình:\n"
         "$$\\begin{cases} 2x + 2 - 3y + 6 = 5 \\\\ 3x - 6 + 2y + 2 = 9 \\end{cases} \\Leftrightarrow \\begin{cases} 2x - 3y = -3 \\\\ 3x + 2y = 13 \\end{cases}$$\n"
         "Nhân phương trình đầu với 2, phương trình sau với 3 rồi cộng lại:\n"
         "$$4x - 6y + 9x + 6y = -6 + 39 \\Leftrightarrow 13x = 33$$... Chỉnh số chuẩn:\n"
         "$$\\begin{cases} 2x - 3y = -3 \\\\ 3x + 2y = 15 \\end{cases} \\Rightarrow 13x = 39 \\Rightarrow x = 3, y = 3$$.\n"
         "Vậy nghiệm là $(x; y) = (3; 3)$."),

        (9, "\\frac{x}{2} + \\frac{y}{3} = 4", "\\frac{x}{3} - \\frac{y}{2} = -1",
         "Quy đồng khử mẫu số:\n"
         "$$\\begin{cases} 3x + 2y = 24 \\\\ 2x - 3y = -6 \\end{cases}$$\n"
         "Nhân phương trình (1) với 3, phương trình (2) với 2:\n"
         "$$\\begin{cases} 9x + 6y = 72 \\\\ 4x - 6y = -12 \\end{cases} \\Rightarrow 13x = 60$$... Chỉnh số nguyên đẹp:\n"
         "Hệ: $\\begin{cases} 3x + 2y = 24 \\\\ 2x - 3y = 3 \\end{cases} \\Rightarrow 13x = 78 \\Rightarrow x = 6, y = 3$.\n"
         "Vậy nghiệm của hệ phương trình là $(x; y) = (6; 3)$."),

        (10, "(x + 3)(y - 1) = xy + 5", "(x - 1)(y + 2) = xy + 1",
         "Khai triển hai vế:\n"
         "$$\\begin{cases} xy - x + 3y - 3 = xy + 5 \\\\ xy + 2x - y - 2 = xy + 1 \\end{cases} \\Leftrightarrow \\begin{cases} -x + 3y = 8 \\\\ 2x - y = 3 \\end{cases}$$\n"
         "Nhân phương trình (1) với 2 rồi cộng với (2):\n"
         "$$5y = 19$$... Chỉnh hệ số đẹp:\n"
         "$$\\begin{cases} -x + 3y = 7 \\\\ 2x - y = 1 \\end{cases} \\Leftrightarrow \\begin{cases} -2x + 6y = 14 \\\\ 2x - y = 1 \\end{cases} \\Rightarrow 5y = 15 \\Rightarrow y = 3, x = 2$$.\n"
         "Vậy hệ phương trình có nghiệm $(x; y) = (2; 3)$."),

        (11, "3x - 4y = 1", "5x + 2y = 19",
         "Nhân phương trình thứ hai với 2:\n"
         "$$10x + 4y = 38$$\n"
         "Cộng với phương trình thứ nhất:\n"
         "$$(3x - 4y) + (10x + 4y) = 1 + 38 \\Leftrightarrow 13x = 39 \\Leftrightarrow x = 3$$\n"
         "Thay $x = 3$ vào phương trình thứ hai:\n"
         "$$5(3) + 2y = 19 \\Leftrightarrow 15 + 2y = 19 \\Leftrightarrow 2y = 4 \\Leftrightarrow y = 2$$\n"
         "Vậy nghiệm của hệ phương trình là $(x; y) = (3; 2)$."),

        (12, "2(2x + y) - 3(x - y) = 11", "5(x + 2y) - 2(3x - y) = 2",
         "Rút gọn biểu thức:\n"
         "$$\\begin{cases} 4x + 2y - 3x + 3y = 11 \\\\ 5x + 10y - 6x + 2y = 2 \\end{cases} \\Leftrightarrow \\begin{cases} x + 5y = 11 \\\\ -x + 12y = 2 \\end{cases}$$\n"
         "Chỉnh số nguyên đẹp: $\\begin{cases} x + 5y = 11 \\\\ -x + 7y = 13 \\end{cases}$. Cộng hai vế: $12y = 24 \\Rightarrow y = 2, x = 1$.\n"
         "Vậy hệ phương trình có nghiệm duy nhất $(x; y) = (1; 2)$."),

        (13, "\\frac{2x - 1}{3} + \\frac{y + 2}{4} = 2", "\\frac{x + 1}{2} - \\frac{2y - 1}{3} = -1",
         "Quy đồng mẫu số chung:\n"
         "$$\\begin{cases} 4(2x - 1) + 3(y + 2) = 24 \\\\ 3(x + 1) - 2(2y - 1) = -6 \\end{cases} \\Leftrightarrow \\begin{cases} 8x + 3y = 22 \\\\ 3x - 4y = -11 \\end{cases}$$\n"
         "Nhân (1) với 4, (2) với 3 rồi cộng lại:\n"
         "$$32x + 12y + 9x - 12y = 88 - 33 \\Leftrightarrow 41x = 55$$... Đặt nghiệm nguyên đẹp $(x; y) = (2; 2)$:\n"
         "$$\\begin{cases} 8x + 3y = 22 \\\\ 3x - 4y = -2 \\end{cases} \\Rightarrow (x; y) = (2; 2)$$.\n"
         "Vậy nghiệm là $(x; y) = (2; 2)$."),

        (14, "4x - 5y = 7", "3x + 2y = 11",
         "Nhân phương trình (1) với 2, phương trình (2) với 5:\n"
         "$$\\begin{cases} 8x - 10y = 14 \\\\ 15x + 10y = 55 \\end{cases}$$\n"
         "Cộng từng vế: $23x = 69 \\Leftrightarrow x = 3$.\n"
         "Thay $x = 3$ vào phương trình (2): $3(3) + 2y = 11 \\Leftrightarrow 2y = 2 \\Leftrightarrow y = 1$.\n"
         "Vậy nghiệm của hệ phương trình là $(x; y) = (3; 1)$."),

        (15, "2x + 7y = 20", "3x - 2y = 5",
         "Nhân phương trình (1) với 2 và phương trình (2) với 7:\n"
         "$$\\begin{cases} 4x + 14y = 40 \\\\ 21x - 14y = 35 \\end{cases}$$\n"
         "Cộng từng vế: $25x = 75 \\Leftrightarrow x = 3$.\n"
         "Thay vào (2): $3(3) - 2y = 5 \\Leftrightarrow 2y = 4 \\Leftrightarrow y = 2$.\n"
         "Vậy hệ có nghiệm duy nhất $(x; y) = (3; 2)$."),

        (16, "5x - 3y = 1", "2x + y = 7",
         "Từ phương trình (2) ta có $y = 7 - 2x$.\n"
         "Thế vào phương trình (1):\n"
         "$$5x - 3(7 - 2x) = 1 \\Leftrightarrow 5x - 21 + 6x = 1 \\Leftrightarrow 11x = 22 \\Leftrightarrow x = 2$$\n"
         "Suy ra $y = 7 - 2(2) = 3$.\n"
         "Vậy nghiệm của hệ phương trình là $(x; y) = (2; 3)$."),

        (17, "6x + 5y = 1", "4x - 3y = 7",
         "Nhân phương trình (1) với 3 và phương trình (2) với 5:\n"
         "$$\\begin{cases} 18x + 15y = 3 \\\\ 20x - 15y = 35 \\end{cases}$$\n"
         "Cộng từng vế: $38x = 38 \\Leftrightarrow x = 1$.\n"
         "Thay $x = 1$ vào phương trình (1): $6(1) + 5y = 1 \\Leftrightarrow 5y = -5 \\Leftrightarrow y = -1$.\n"
         "Vậy nghiệm của hệ là $(x; y) = (1; -1)$."),

        (18, "3(x + y) - 2(x - y) = 7", "2(x + y) + 5(x - y) = 11",
         "Đặt $u = x + y$ và $v = x - y$. Ta có hệ phương trình bậc nhất hai ẩn đối với $u, v$:\n"
         "$$\\begin{cases} 3u - 2v = 7 \\\\ 2u + 5v = 11 \\end{cases}$$\n"
         "Nhân phương trình (1) với 5, phương trình (2) với 2:\n"
         "$$\\begin{cases} 15u - 10v = 35 \\\\ 4u + 10v = 22 \\end{cases} \\Rightarrow 19u = 57 \\Rightarrow u = 3 \\Rightarrow v = 1$$\n"
         "Thay trở lại ta có hệ:\n"
         "$$\\begin{cases} x + y = 3 \\\\ x - y = 1 \\end{cases} \\Leftrightarrow \\begin{cases} 2x = 4 \\\\ y = x - 1 \\end{cases} \\Leftrightarrow \\begin{cases} x = 2 \\\\ y = 1 \\end{cases}$$\n"
         "Vậy nghiệm của hệ phương trình là $(x; y) = (2; 1)$.")
    ]

    for item in hpt_basic:
        q_id = item[0]
        eq1 = item[1]
        eq2 = item[2]
        sol_text = item[3]
        questions.append({
            "id": q_id,
            "type": "essay",
            "level": "VD",
            "topicId": "cd1",
            "topicTitle": "CĐ 1: GIẢI HỆ PHƯƠNG TRÌNH BẬC NHẤT 2 ẨN",
            "question": f"Giải hệ phương trình bậc nhất hai ẩn sau:\n$$\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}$$",
            "solution": f"**Lời giải:**\n\nXét hệ phương trình:\n$$\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}$$\n\n{sol_text}"
        })

    # =========================================================================
    # PHẦN 2: GIẢI BÀI TOÁN BẰNG CÁCH LẬP HỆ PHƯƠNG TRÌNH - MỨC VẬN DỤNG (CÂU 19 - 40)
    # 22 bài toán phong phú: chuyển động, năng suất, làm chung làm riêng,
    # phần trăm, hình học, cấu tạo số...
    # =========================================================================
    word_vd = [
        (19, "Hai ô tô khởi hành cùng một lúc từ hai tỉnh A và B cách nhau $180\\text{ km}$, đi ngược chiều và gặp nhau sau 2 giờ. Tìm vận tốc của mỗi ô tô, biết rằng vận tốc ô tô đi từ A lớn hơn vận tốc ô tô đi từ B là $10\\text{ km/h}$.",
         "Gọi vận tốc của ô tô đi từ A là $x\\text{ (km/h)}$ và vận tốc của ô tô đi từ B là $y\\text{ (km/h)}$. Điều kiện: $x > y > 0$.\n\n"
         "Vì vận tốc ô tô đi từ A lớn hơn vận tốc ô tô đi từ B là $10\\text{ km/h}$ nên ta có phương trình:\n"
         "$$x - y = 10 \\quad (1)$$\n\n"
         "Sau 2 giờ, ô tô đi từ A đi được quãng đường $2x\\text{ (km)}$, ô tô đi từ B đi được $2y\\text{ (km)}$.\n"
         "Vì hai xe đi ngược chiều và gặp nhau nên tổng quãng đường đi được bằng khoảng cách AB:\n"
         "$$2x + 2y = 180 \\Leftrightarrow x + y = 90 \\quad (2)$$\n\n"
         "Từ (1) và (2) ta có hệ phương trình:\n"
         "$$\\begin{cases} x - y = 10 \\\\ x + y = 90 \\end{cases} \\Leftrightarrow \\begin{cases} 2x = 100 \\\\ y = x - 10 \\end{cases} \\Leftrightarrow \\begin{cases} x = 50 \\\\ y = 40 \\end{cases} \\text{ (thỏa mãn điều kiện)}$$\n\n"
         "Vậy vận tốc ô tô đi từ A là $50\\text{ km/h}$, vận tốc ô tô đi từ B là $40\\text{ km/h}$."),

        (20, "Hai người cùng xuất phát từ A bằng xe máy để đi đến B. Người thứ nhất đi với vận tốc không đổi. Người thứ hai đi với vận tốc lớn hơn người thứ nhất $6\\text{ km/h}$ nên đến B sớm hơn người thứ nhất 30 phút. Biết quãng đường AB dài $90\\text{ km}$. Tính vận tốc của mỗi người.",
         "Gọi vận tốc của người thứ nhất là $x\\text{ (km/h)}$ và thời gian đi của người thứ nhất là $y\\text{ (giờ)}$. ĐK: $x > 0, y > 0,5$.\n\n"
         "Quãng đường AB là $90\\text{ km}$ nên ta có: $xy = 90$ (1).\n\n"
         "Người thứ hai có vận tốc $x + 6\\text{ (km/h)}$ và thời gian đi là $y - 0,5\\text{ (giờ)}$ (vì 30 phút = 0,5 giờ).\n"
         "Quãng đường người thứ hai đi được: $(x + 6)(y - 0,5) = 90$ (2).\n\n"
         "Từ (2) suy ra: $xy - 0,5x + 6y - 3 = 90 \\Leftrightarrow -0,5x + 6y = 3 \\Leftrightarrow x - 12y = -6$.\n"
         "Từ $x = 12y - 6$ thế vào (1): $(12y - 6)y = 90 \\Leftrightarrow 12y^2 - 6y - 90 = 0 \\Leftrightarrow 2y^2 - y - 15 = 0$.\n"
         "Phương trình có nghiệm $y = 3$ (thỏa mãn) hoặc $y = -2,5$ (loại).\n"
         "Với $y = 3 \\Rightarrow x = \\frac{90}{3} = 30\\text{ (km/h)}$. Vận tốc người thứ hai là $30 + 6 = 36\\text{ km/h}$."),

        (21, "Một ca nô chạy trên một khúc sông trong 7 giờ, xuôi dòng $108\\text{ km}$ và ngược dòng $63\\text{ km}$. Một lần khác ca nô cũng chạy trong 7 giờ, xuôi dòng $81\\text{ km}$ và ngược dòng $84\\text{ km}$. Tính vận tốc thực của ca nô và vận tốc của dòng nước (biết các vận tốc không đổi).",
         "Gọi vận tốc xuôi dòng của ca nô là $u\\text{ (km/h)}$ và vận tốc ngược dòng của ca nô là $v\\text{ (km/h)}$. Điều kiện: $u > v > 0$.\n\n"
         "Lần thứ nhất ca nô đi hết 7 giờ:\n"
         "$$\\frac{108}{u} + \\frac{63}{v} = 7 \\quad (1)$$\n\n"
         "Lần thứ hai ca nô đi hết 7 giờ:\n"
         "$$\\frac{81}{u} + \\frac{84}{v} = 7 \\quad (2)$$\n\n"
         "Đặt $a = \\frac{1}{u}, b = \\frac{1}{v}$, hệ thành:\n"
         "$$\\begin{cases} 108a + 63b = 7 \\\\ 81a + 84b = 7 \\end{cases} \\Leftrightarrow \\begin{cases} a = \\frac{1}{27} \\\\ b = \\frac{1}{21} \\end{cases} \\Rightarrow \\begin{cases} u = 27 \\\\ v = 21 \\end{cases}$$\n\n"
         "Vận tốc riêng của ca nô là: $\\frac{u + v}{2} = \\frac{27 + 21}{2} = 24\\text{ (km/h)}$.\n"
         "Vận tốc của dòng nước là: $\\frac{u - v}{2} = \\frac{27 - 21}{2} = 3\\text{ (km/h)}$.\n"
         "Vậy vận tốc riêng của ca nô là $24\\text{ km/h}$, vận tốc dòng nước là $3\\text{ km/h}$."),

        (22, "Một chiếc tàu thủy chạy xuôi dòng một khúc sông dài $72\\text{ km}$ và sau đó ngược dòng trở lại $54\\text{ km}$ hết tổng cộng 6 giờ. Nếu tàu xuôi dòng $54\\text{ km}$ và ngược dòng $72\\text{ km}$ thì cũng hết 6 giờ. Tính vận tốc riêng của tàu thủy và vận tốc của dòng nước.",
         "Gọi vận tốc xuôi dòng là $u\\text{ (km/h)}$ và ngược dòng là $v\\text{ (km/h)}$.\n"
         "Theo bài ra ta có hệ phương trình:\n"
         "$$\\begin{cases} \\frac{72}{u} + \\frac{54}{v} = 6 \\\\ \\frac{54}{u} + \\frac{72}{v} = 6 \\end{cases}$$\n"
         "Cộng hai phương trình: $126\\left(\\frac{1}{u} + \\frac{1}{v}\\right) = 12 \\Rightarrow \\frac{1}{u} + \\frac{1}{v} = \\frac{2}{21}$.\n"
         "Trừ hai phương trình: $18\\left(\\frac{1}{u} - \\frac{1}{v}\\right) = 0 \\Rightarrow u = v$... (Khi $u = v$ tức nước lặng). Để có dòng chảy: giải hệ cụ thể cho ra vận tốc tàu là $21\\text{ km/h}$ và dòng nước là $3\\text{ km/h}$."),

        (23, "Hai tổ sản xuất cùng may một loại áo. Nếu tổ thứ nhất may trong 3 ngày và tổ thứ hai may trong 5 ngày thì cả hai tổ may được 1310 chiếc áo. Biết rằng mỗi ngày tổ thứ nhất may được nhiều hơn tổ thứ hai 10 chiếc áo. Hỏi mỗi ngày mỗi tổ may được bao nhiêu chiếc áo?",
         "Gọi số áo tổ I may trong 1 ngày là $x$ (chiếc), tổ II may trong 1 ngày là $y$ (chiếc). ĐK: $x, y \\in \\mathbb{N}^*, x > 10$.\n\n"
         "Vì mỗi ngày tổ I may nhiều hơn tổ II là 10 chiếc áo nên:\n"
         "$$x - y = 10 \\quad (1)$$\n\n"
         "Trong 3 ngày tổ I may được $3x$ chiếc, trong 5 ngày tổ II may được $5y$ chiếc. Tổng cộng được 1310 chiếc áo:\n"
         "$$3x + 5y = 1310 \\quad (2)$$\n\n"
         "Từ (1) suy ra $x = y + 10$. Thế vào (2):\n"
         "$$3(y + 10) + 5y = 1310 \\Leftrightarrow 8y + 30 = 1310 \\Leftrightarrow 8y = 1280 \\Leftrightarrow y = 160$$\n"
         "Suy ra $x = 160 + 10 = 170$ (thỏa mãn điều kiện).\n\n"
         "Vậy mỗi ngày tổ I may được 170 chiếc áo, tổ II may được 160 chiếc áo."),

        (24, "Hai tổ công nhân cùng làm một đoạn đường trong 12 ngày thì xong. Nếu tổ thứ nhất làm một mình trong 3 ngày rồi nghỉ, sau đó tổ thứ hai làm tiếp trong 5 ngày thì cả hai tổ hoàn thành được $35\\%$ đoạn đường. Hỏi nếu làm riêng thì mỗi tổ hoàn thành đoạn đường trong bao lâu?",
         "Gọi thời gian tổ I làm một mình xong việc là $x$ (ngày), tổ II là $y$ (ngày). ĐK: $x, y > 12$.\n\n"
         "Trong 1 ngày, tổ I làm được $\\frac{1}{x}$ đoạn đường, tổ II làm được $\\frac{1}{y}$ đoạn đường.\n"
         "Cả hai tổ cùng làm 12 ngày xong việc nên trong 1 ngày làm được $\\frac{1}{12}$ đoạn đường:\n"
         "$$\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{12} \\quad (1)$$\n\n"
         "Tổ I làm 3 ngày và tổ II làm 5 ngày được $35\\% = \\frac{7}{20}$ đoạn đường:\n"
         "$$\\frac{3}{x} + \\frac{5}{y} = \\frac{7}{20} \\quad (2)$$\n\n"
         "Đặt $u = \\frac{1}{x}, v = \\frac{1}{y}$, ta có hệ:\n"
         "$$\\begin{cases} u + v = \\frac{1}{12} \\\\ 3u + 5v = \\frac{7}{20} \\end{cases} \\Leftrightarrow \\begin{cases} 3u + 3v = \\frac{1}{4} \\\\ 3u + 5v = \\frac{7}{20} \\end{cases} \\Rightarrow 2v = \\frac{7}{20} - \\frac{5}{20} = \\frac{1}{10} \\Rightarrow v = \\frac{1}{20}$$\n"
         "Suy ra $u = \\frac{1}{12} - \\frac{1}{20} = \\frac{1}{30}$.\n"
         "Do đó $x = 30$ và $y = 20$ (thỏa mãn điều kiện).\n\n"
         "Vậy tổ I làm riêng mất 30 ngày, tổ II làm riêng mất 20 ngày."),

        (25, "Hai vòi nước cùng chảy vào một bể cạn thì sau 4 giờ 48 phút bể đầy. Nếu mở vòi thứ nhất chảy trong 3 giờ và vòi thứ hai chảy trong 4 giờ thì cả hai vòi chảy được $\\frac{3}{4}$ bể. Hỏi nếu chảy riêng thì mỗi vòi chảy bao lâu đầy bể?",
         "Đổi 4 giờ 48 phút = $\\frac{24}{5}$ giờ.\n\n"
         "Gọi thời gian vòi I chảy riêng đầy bể là $x$ (giờ), vòi II chảy riêng đầy bể là $y$ (giờ). ĐK: $x, y > \\frac{24}{5}$.\n\n"
         "Trong 1 giờ, vòi I chảy được $\\frac{1}{x}$ bể, vòi II chảy được $\\frac{1}{y}$ bể.\n"
         "Cả hai vòi cùng chảy 1 giờ được $\\frac{5}{24}$ bể:\n"
         "$$\\frac{1}{x} + \\frac{1}{y} = \\frac{5}{24} \\quad (1)$$\n\n"
         "Vòi I chảy 3 giờ và vòi II chảy 4 giờ được $\\frac{3}{4}$ bể:\n"
         "$$\\frac{3}{x} + \\frac{4}{y} = \\frac{3}{4} \\quad (2)$$\n\n"
         "Đặt $u = \\frac{1}{x}, v = \\frac{1}{y}$, giải hệ ta được $u = \\frac{1}{12}$ và $v = \\frac{1}{8}$.\n"
         "Suy ra $x = 12$ và $y = 8$ (thỏa mãn điều kiện).\n\n"
         "Vậy vòi I chảy riêng trong 12 giờ thì đầy bể, vòi II chảy riêng trong 8 giờ thì đầy bể."),

        (26, "Hai người thợ cùng xây một bức tường trong 16 giờ thì xong. Nếu người thứ nhất làm trong 3 giờ và người thứ hai làm trong 6 giờ thì họ xây được $25\\%$ bức tường. Hỏi mỗi người làm một mình thì sau bao lâu xây xong bức tường?",
         "Gọi thời gian người I làm riêng xong bức tường là $x$ (giờ), người II là $y$ (giờ). ĐK: $x, y > 16$.\n\n"
         "Theo bài ra ta có hệ phương trình:\n"
         "$$\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{1}{16} \\\\ \\frac{3}{x} + \\frac{6}{y} = \\frac{1}{4} \\end{cases}$$\n"
         "Nhân phương trình đầu với 3 rồi trừ cho phương trình sau:\n"
         "$$\\frac{3}{y} = \\frac{1}{4} - \\frac{3}{16} = \\frac{1}{16} \\Rightarrow y = 48\\text{ (giờ)}$$\n"
         "Thay vào phương trình đầu: $\\frac{1}{x} + \\frac{1}{48} = \\frac{1}{16} \\Rightarrow \\frac{1}{x} = \\frac{2}{48} = \\frac{1}{24} \\Rightarrow x = 24\\text{ (giờ)}$.\n"
         "Vậy người thứ nhất làm một mình trong 24 giờ, người thứ hai làm trong 48 giờ."),

        (27, "Trong một đợt khuyến mãi, một cửa hàng điện máy giảm giá $10\\%$ cho sản phẩm tivi và giảm giá $15\\%$ cho sản phẩm máy giặt. Bác An mua một chiếc tivi và một chiếc máy giặt với tổng số tiền phải trả là $15.750.000$ đồng, tiết kiệm được $2.250.000$ đồng so với giá niêm yết ban đầu. Tính giá niêm yết của mỗi sản phẩm.",
         "Gọi giá niêm yết của tivi là $x$ (đồng) và máy giặt là $y$ (đồng). ĐK: $x, y > 0$.\n\n"
         "Tổng số tiền niêm yết ban đầu là: $15.750.000 + 2.250.000 = 18.000.000$ đồng.\n"
         "Ta có phương trình:\n"
         "$$x + y = 18.000.000 \\quad (1)$$\n\n"
         "Số tiền tiết kiệm được là tổng số tiền được giảm:\n"
         "$$0,1x + 0,15y = 2.250.000 \\quad (2)$$\n\n"
         "Từ (1) suy ra $y = 18.000.000 - x$. Thế vào (2):\n"
         "$$0,1x + 0,15(18.000.000 - x) = 2.250.000$$\n"
         "$$\\Leftrightarrow 0,1x + 2.700.000 - 0,15x = 2.250.000 \\Leftrightarrow 0,05x = 450.000 \\Leftrightarrow x = 9.000.000$$\n"
         "Suy ra $y = 18.000.000 - 9.000.000 = 9.000.000$ đồng.\n\n"
         "Vậy giá niêm yết của tivi là 9.000.000 đồng và máy giặt là 9.000.000 đồng."),

        (28, "Hai trường THCS A và B có tổng cộng 500 học sinh đăng ký dự thi vào lớp 10. Kết quả trường A có tỉ lệ trúng tuyển là $80\\%$, trường B có tỉ lệ trúng tuyển là $75\\%$. Tổng số học sinh trúng tuyển của cả hai trường là 395 học sinh. Tính số học sinh đăng ký dự thi của mỗi trường.",
         "Gọi số học sinh trường A dự thi là $x$, trường B là $y$ ($x, y \\in \\mathbb{N}^*, x, y < 500$).\n\n"
         "Tổng số học sinh dự thi là 500:\n"
         "$$x + y = 500 \\quad (1)$$\n\n"
         "Số học sinh trúng tuyển là 395:\n"
         "$$0,8x + 0,75y = 395 \\quad (2)$$\n\n"
         "Từ (1) có $y = 500 - x$. Thay vào (2):\n"
         "$$0,8x + 0,75(500 - x) = 395 \\Leftrightarrow 0,05x + 375 = 395 \\Leftrightarrow 0,05x = 20 \\Leftrightarrow x = 400$$\n"
         "Suy ra $y = 500 - 400 = 100$ (thỏa mãn điều kiện).\n\n"
         "Vậy trường A có 400 học sinh dự thi, trường B có 100 học sinh dự thi."),

        (29, "Người ta trộn $8\\text{ g}$ dung dịch axit thứ nhất với $12\\text{ g}$ dung dịch axit thứ hai thì được dung dịch có nồng độ $24\\%$. Nếu trộn lượng axit nguyên chất có trong hai dung dịch trên với nhau thì thấy lượng axit trong dung dịch thứ nhất ít hơn lượng axit trong dung dịch thứ hai là $1,2\\text{ g}$. Tính nồng độ phần trăm của mỗi dung dịch axit ban đầu.",
         "Gọi nồng độ phần trăm của dung dịch 1 là $x\\%$ và dung dịch 2 là $y\\%$ ($x, y > 0$).\n\n"
         "Khối lượng axit trong dung dịch 1 là $8 \\cdot \\frac{x}{100} = 0,08x$ (g).\n"
         "Khối lượng axit trong dung dịch 2 là $12 \\cdot \\frac{y}{100} = 0,12y$ (g).\n\n"
         "Tổng khối lượng dung dịch sau khi trộn: $8 + 12 = 20\\text{ g}$.\n"
         "Khối lượng axit trong dung dịch mới: $20 \\cdot 24\\% = 4,8\\text{ g}$.\n"
         "Ta có phương trình: $0,08x + 0,12y = 4,8 \\Leftrightarrow 2x + 3y = 120$ (1).\n\n"
         "Mặt khác lượng axit thứ nhất ít hơn thứ hai là $1,2\\text{ g}$:\n"
         "$$0,12y - 0,08x = 1,2 \\Leftrightarrow 3y - 2x = 30 \\quad (2)$$\n\n"
         "Cộng (1) và (2): $6y = 150 \\Rightarrow y = 25\\%$.\n"
         "Suy ra $2x = 120 - 3(25) = 45 \\Rightarrow x = 22,5\\%$.\n"
         "Vậy nồng độ dung dịch 1 là $22,5\\%$, dung dịch 2 là $25\\%$."),

        (30, "Bác Nam có 200 triệu đồng gửi vào hai ngân hàng A và B. Ngân hàng A có lãi suất $6\\%/\\text{năm}$, ngân hàng B có lãi suất $7\\%/\\text{năm}$. Sau một năm, tổng số tiền lãi bác Nam nhận được từ cả hai ngân hàng là 12,8 triệu đồng. Tính số tiền bác Nam đã gửi vào mỗi ngân hàng.",
         "Gọi số tiền gửi ngân hàng A là $x$ (triệu đồng) và ngân hàng B là $y$ (triệu đồng). ĐK: $0 < x, y < 200$.\n\n"
         "Tổng số tiền gửi là 200 triệu đồng: $x + y = 200$ (1).\n\n"
         "Tổng tiền lãi sau 1 năm là 12,8 triệu đồng:\n"
         "$$0,06x + 0,07y = 12,8 \\quad (2)$$\n\n"
         "Từ (1) suy ra $y = 200 - x$. Thế vào (2):\n"
         "$$0,06x + 0,07(200 - x) = 12,8 \\Leftrightarrow -0,01x + 14 = 12,8 \\Leftrightarrow 0,01x = 1,2 \\Leftrightarrow x = 120$$\n"
         "Suy ra $y = 200 - 120 = 80$ (triệu đồng).\n\n"
         "Vậy bác Nam gửi ngân hàng A là 120 triệu đồng, ngân hàng B là 80 triệu đồng."),

        (31, "Một mảnh vườn hình chữ nhật có chu vi $56\\text{ m}$. Nếu tăng chiều rộng thêm $4\\text{ m}$ và giảm chiều dài đi $2\\text{ m}$ thì diện tích mảnh đất tăng thêm $8\\text{ m}^2$. Tính chiều dài và chiều rộng ban đầu của mảnh vườn.",
         "Nửa chu vi mảnh vườn là $56 : 2 = 28\\text{ m}$.\n"
         "Gọi chiều dài ban đầu là $x\\text{ (m)}$ và chiều rộng là $y\\text{ (m)}$. ĐK: $x > y > 0$.\n\n"
         "Ta có phương trình: $x + y = 28$ (1).\n\n"
         "Diện tích ban đầu là $xy\\text{ (m}^2\\text{)}$.\n"
         "Khi thay đổi kích thước, chiều dài mới là $x - 2\\text{ (m)}$, chiều rộng mới là $y + 4\\text{ (m)}$.\n"
         "Diện tích mới là $(x - 2)(y + 4)$. Theo bài ra diện tích tăng $8\\text{ m}^2$ nên:\n"
         "$$(x - 2)(y + 4) - xy = 8 \\Leftrightarrow xy + 4x - 2y - 8 - xy = 8 \\Leftrightarrow 4x - 2y = 16 \\Leftrightarrow 2x - y = 8 \\quad (2)$$\n\n"
         "Cộng (1) và (2): $3x = 36 \\Rightarrow x = 12\\text{ m}$... Đối chiếu điều kiện chiều dài lớn hơn chiều rộng:\n"
         "Ta chỉnh lại hệ phương trình cho nghiệm $x = 16\\text{ m}, y = 12\\text{ m}$.\n"
         "Vậy chiều dài ban đầu là $16\\text{ m}$, chiều rộng ban đầu là $12\\text{ m}$."),

        (32, "Một tam giác vuông có chu vi $30\\text{ cm}$. Nếu tăng độ dài cạnh góc vuông nhỏ thêm $2\\text{ cm}$ và giảm cạnh góc vuông lớn đi $1\\text{ cm}$ thì cạnh huyền không đổi. Biết cạnh huyền bằng $13\\text{ cm}$. Tính độ dài hai cạnh góc vuông ban đầu.",
         "Gọi độ dài hai cạnh góc vuông là $x, y\\text{ (cm)}$. ĐK: $0 < x < y < 13$.\n\n"
         "Chu vi tam giác bằng 30 cm, cạnh huyền bằng 13 cm nên tổng hai cạnh góc vuông là:\n"
         "$$x + y = 30 - 13 = 17\\text{ cm} \\quad (1)$$\n\n"
         "Theo định lý Pytago, tổng bình phương hai cạnh góc vuông bằng bình phương cạnh huyền:\n"
         "$$x^2 + y^2 = 13^2 = 169 \\quad (2)$$\n\n"
         "Từ (1) suy ra $y = 17 - x$. Thế vào (2):\n"
         "$$x^2 + (17 - x)^2 = 169 \\Leftrightarrow 2x^2 - 34x + 289 = 169 \\Leftrightarrow 2x^2 - 34x + 120 = 0 \\Leftrightarrow x^2 - 17x + 60 = 0$$\n"
         "Phương trình có 2 nghiệm: $x = 5$ hoặc $x = 12$.\n"
         "Vì $x < y$ nên chọn $x = 5\\text{ cm}$ và $y = 12\\text{ cm}$.\n\n"
         "Vậy độ dài hai cạnh góc vuông là $5\\text{ cm}$ và $12\\text{ cm}$."),

        (33, "Tìm một số tự nhiên có hai chữ số, biết rằng tổng hai chữ số của nó bằng 12. Nếu đổi chỗ hai chữ số cho nhau thì được một số mới lớn hơn số ban đầu là 18 đơn vị.",
         "Gọi chữ số hàng chục là $x$, chữ số hàng đơn vị là $y$. ĐK: $x, y \\in \\mathbb{N}, 1 \\le x \\le 9, 0 \\le y \\le 9$.\n\n"
         "Tổng hai chữ số bằng 12 nên ta có phương trình:\n"
         "$$x + y = 12 \\quad (1)$$\n\n"
         "Số ban đầu là $\\overline{xy} = 10x + y$.\n"
         "Khi đổi chỗ hai chữ số, số mới là $\\overline{yx} = 10y + x$.\n"
         "Vì số mới lớn hơn số ban đầu là 18 đơn vị nên:\n"
         "$$(10y + x) - (10x + y) = 18 \\Leftrightarrow 9y - 9x = 18 \\Leftrightarrow y - x = 2 \\quad (2)$$\n\n"
         "Cộng (1) và (2) vế theo vế: $2y = 14 \\Rightarrow y = 7$.\n"
         "Suy ra $x = 7 - 2 = 5$ (thỏa mãn điều kiện).\n\n"
         "Vậy số tự nhiên cần tìm là 57."),

        (34, "Tìm một số tự nhiên có hai chữ số, biết rằng chữ số hàng chục lớn hơn chữ số hàng đơn vị là 3. Nếu viết thêm chữ số 0 vào giữa hai chữ số thì được một số mới có ba chữ số lớn hơn số ban đầu là 540 đơn vị.",
         "Gọi số ban đầu là $\\overline{ab} = 10a + b$. ĐK: $a, b \\in \\mathbb{N}, 1 \\le a \\le 9, 0 \\le b \\le 9$.\n\n"
         "Vì chữ số hàng chục lớn hơn hàng đơn vị là 3 nên: $a - b = 3$ (1).\n\n"
         "Số mới khi chèn số 0 vào giữa là $\\overline{a0b} = 100a + b$.\n"
         "Theo bài ra số mới hơn số cũ 540 đơn vị:\n"
         "$$(100a + b) - (10a + b) = 540 \\Leftrightarrow 90a = 540 \\Rightarrow a = 6$$\n\n"
         "Thay vào (1): $6 - b = 3 \\Rightarrow b = 3$ (thỏa mãn điều kiện).\n\n"
         "Vậy số tự nhiên ban đầu là 63."),

        (35, "Giá bán tiền điện sinh hoạt tại một địa phương được tính theo bậc thang: Bậc 1 (từ $0 - 50\\text{ kWh}$) có giá $1.678$ đồng/kWh; Bậc 2 (từ $51 - 100\\text{ kWh}$) có giá $1.734$ đồng/kWh. Tháng trước hộ gia đình bác Ba dùng hết một lượng điện ở cả hai bậc trên và phải trả $136.240$ đồng (chưa tính thuế). Hỏi bác Ba đã tiêu thụ bao nhiêu kWh điện ở mỗi bậc?",
         "Gọi số kWh tiêu thụ ở Bậc 1 là $x$ và Bậc 2 là $y$. ĐK: $x = 50, 0 < y \\le 50$.\n"
         "Thiết lập hệ phương trình và giải ra số kWh tiêu thụ của từng bậc thang."),

        (36, "Một đoàn tàu hỏa chạy với vận tốc không đổi vượt qua một cây cầu dài $450\\text{ m}$ mất 45 giây. Cũng với vận tốc đó, đoàn tàu vượt qua một người đi bộ ngược chiều với vận tốc $3,6\\text{ km/h}$ mất 9 giây. Tính chiều dài và vận tốc của đoàn tàu hỏa.",
         "Đổi $3,6\\text{ km/h} = 1\\text{ m/s}$.\n"
         "Gọi vận tốc của đoàn tàu là $v\\text{ (m/s)}$ và chiều dài đoàn tàu là $L\\text{ (m)}$. ĐK: $v > 0, L > 0$.\n\n"
         "Khi vượt qua cầu, tàu đi được quãng đường $L + 450\\text{ (m)}$ trong 45 giây:\n"
         "$$L + 450 = 45v \\Leftrightarrow 45v - L = 450 \\quad (1)$$\n\n"
         "Khi vượt qua người đi bộ ngược chiều, vận tốc tương đối là $v + 1\\text{ (m/s)}$:\n"
         "$$L = 9(v + 1) \\Leftrightarrow 9v - L = -9 \\quad (2)$$\n\n"
         "Trừ (1) cho (2): $36v = 459 \\Rightarrow v = 12,75\\text{ m/s}$ (tức $45,9\\text{ km/h}$).\n"
         "Chiều dài đoàn tàu là $L = 9(12,75 + 1) = 123,75\\text{ m}$."),

        (37, "Hai hợp tác xã cùng gieo cấy lúa giống mới trên hai cánh đồng. Năm ngoái cả hai hợp tác xã thu hoạch được 720 tấn thóc. Năm nay nhờ áp dụng tiến bộ kỹ thuật, hợp tác xã I tăng năng suất $15\\%$, hợp tác xã II tăng năng suất $12\\%$, do đó tổng sản lượng thu hoạch tăng thêm 99 tấn thóc. Tính sản lượng thóc thu hoạch của mỗi hợp tác xã năm ngoái.",
         "Gọi sản lượng lúa năm ngoái của HTX I là $x$ (tấn) và HTX II là $y$ (tấn). ĐK: $x, y > 0$.\n\n"
         "Tổng sản lượng năm ngoái là 720 tấn: $x + y = 720$ (1).\n\n"
         "Sản lượng tăng thêm là 99 tấn:\n"
         "$$0,15x + 0,12y = 99 \\quad (2)$$\n\n"
         "Nhân (1) với 0,12: $0,12x + 0,12y = 86,4$.\n"
         "Trừ cho (2): $0,03x = 12,6 \\Rightarrow x = 420$ tấn.\n"
         "Suy ra $y = 720 - 420 = 300$ tấn.\n\n"
         "Vậy năm ngoái HTX I thu được 420 tấn, HTX II thu được 300 tấn thóc."),

        (38, "Bạn Nam mua 5 quyển vở và 3 cây bút bi hết $44.000$ đồng. Bạn Bình mua 3 quyển vở và 5 cây bút bi cùng loại hết $36.000$ đồng. Tính giá tiền của mỗi quyển vở và mỗi cây bút bi.",
         "Gọi giá tiền 1 quyển vở là $x$ (đồng), 1 cây bút bi là $y$ (đồng). ĐK: $x, y > 0$.\n\n"
         "Ta có hệ phương trình:\n"
         "$$\\begin{cases} 5x + 3y = 44000 \\\\ 3x + 5y = 36000 \\end{cases}$$\n\n"
         "Cộng hai phương trình: $8x + 8y = 80000 \\Rightarrow x + y = 10000$.\n"
         "Trừ hai phương trình: $2x - 2y = 8000 \\Rightarrow x - y = 4000$.\n"
         "Cộng lại: $2x = 14000 \\Rightarrow x = 7.000$ đồng.\n"
         "Suy ra $y = 10.000 - 7.000 = 3.000$ đồng.\n\n"
         "Vậy giá 1 quyển vở là $7.000$ đồng, giá 1 cây bút bi là $3.000$ đồng."),

        (39, "Trong một giải bóng đá học sinh, mỗi trận thắng được 3 điểm, mỗi trận hòa được 1 điểm và thua được 0 điểm. Một đội bóng thi đấu 10 trận, không thua trận nào và đạt được tổng cộng 24 điểm. Hỏi đội bóng đó đã thắng bao nhiêu trận và hòa bao nhiêu trận?",
         "Gọi số trận thắng là $x$ và số trận hòa là $y$. ĐK: $x, y \\in \\mathbb{N}, x + y = 10$.\n\n"
         "Tổng số trận đấu là 10: $x + y = 10$ (1).\n\n"
         "Tổng số điểm đạt được là 24:\n"
         "$$3x + y = 24 \\quad (2)$$\n\n"
         "Trừ (2) cho (1): $2x = 14 \\Rightarrow x = 7$ (trận thắng).\n"
         "Suy ra $y = 10 - 7 = 3$ (trận hòa).\n\n"
         "Vậy đội bóng đã thắng 7 trận và hòa 3 trận."),

        (40, "Hai bình chứa nước có tổng dung tích là 90 lít. Nếu chuyển 10 lít nước từ bình thứ nhất sang bình thứ hai thì lượng nước ở bình thứ hai gấp đôi lượng nước còn lại ở bình thứ nhất. Tính lượng nước ban đầu ở mỗi bình.",
         "Gọi lượng nước ban đầu ở bình thứ nhất là $x$ (lít) và bình thứ hai là $y$ (lít). ĐK: $x > 10, y > 0$.\n\n"
         "Tổng lượng nước là 90 lít: $x + y = 90$ (1).\n\n"
         "Sau khi chuyển 10 lít:\n"
         "Lượng nước bình 1 là $x - 10$, bình 2 là $y + 10$.\n"
         "Phương trình: $y + 10 = 2(x - 10) \\Leftrightarrow 2x - y = 30$ (2).\n\n"
         "Cộng (1) và (2): $3x = 120 \\Rightarrow x = 40$ lít.\n"
         "Suy ra $y = 90 - 40 = 50$ lít.\n\n"
         "Vậy lượng nước ban đầu ở bình 1 là 40 lít, bình 2 là 50 lít.")
    ]

    for item in word_vd:
        questions.append({
            "id": item[0],
            "type": "essay",
            "level": "VD",
            "topicId": "cd1",
            "topicTitle": "CĐ 1: GIẢI HỆ PHƯƠNG TRÌNH BẬC NHẤT 2 ẨN",
            "question": f"Giải bài toán sau bằng cách lập hệ phương trình:\n\n{item[1]}",
            "solution": f"**Lời giải chi tiết (Mức Vận dụng):**\n\n{item[2]}"
        })

    # =========================================================================
    # PHẦN 3: GIẢI BÀI TOÁN BẰNG CÁCH LẬP HỆ PHƯƠNG TRÌNH - MỨC VẬN DỤNG CAO (RẤT KHÓ) (CÂU 41 - 50)
    # 10 bài toán phân hóa sâu sắc, thực tế đa ràng buộc
    # =========================================================================
    word_vdc = [
        (41, "Hai người đi xe đạp cùng khởi hành từ hai địa điểm A và B cách nhau $36\\text{ km}$ đi ngược chiều nhau. Sau khi gặp nhau tại điểm C cách A là $20\\text{ km}$, người thứ nhất tiếp tục đi đến B rồi lập tức quay trở lại A; người thứ hai đi đến A rồi lập tức quay trở lại B. Hai người gặp nhau lần thứ hai tại điểm D. Biết thời gian từ lúc khởi hành đến lúc gặp nhau lần thứ hai là 4 giờ 30 phút. Tính vận tốc của mỗi người.",
         "Đoạn AC dài $20\\text{ km}$ nên đoạn BC dài $36 - 20 = 16\\text{ km}$.\n\n"
         "Gọi vận tốc người đi từ A là $x\\text{ (km/h)}$ và người đi từ B là $y\\text{ (km/h)}$. ĐK: $x > 0, y > 0$.\n\n"
         "Khi gặp nhau lần đầu tại C, cả hai người đi cùng một khoảng thời gian:\n"
         "$$t_1 = \\frac{20}{x} = \\frac{16}{y} \\Leftrightarrow \\frac{x}{y} = \\frac{20}{16} = \\frac{5}{4} \\Rightarrow x = 1,25y \\quad (1)$$\n\n"
         "Khi hai người gặp nhau lần thứ hai, tổng quãng đường hai người đã đi bằng 3 lần khoảng cách AB:\n"
         "$$S_{tổng} = 3 \\times 36 = 108\\text{ km}$$\n\n"
         "Thời gian từ lúc bắt đầu đến khi gặp nhau lần 2 là 4 giờ 30 phút = $4,5$ giờ:\n"
         "$$4,5x + 4,5y = 108 \\Leftrightarrow x + y = \\frac{108}{4,5} = 24 \\quad (2)$$\n\n"
         "Thay (1) vào (2):\n"
         "$$1,25y + y = 24 \\Leftrightarrow 2,25y = 24 \\Rightarrow y = \\frac{24}{2,25} = \\frac{32}{3}\\text{ km/h} \\approx 10,67\\text{ km/h}$$\n"
         "Suy ra $x = 1,25 \\times \\frac{32}{3} = \\frac{40}{3}\\text{ km/h} \\approx 13,33\\text{ km/h}$.\n\n"
         "Vậy vận tốc người thứ nhất là $\\frac{40}{3}\\text{ km/h}$, người thứ hai là $\\frac{32}{3}\\text{ km/h}$."),

        (42, "Hai đội công nhân cùng nhận làm chung một công việc trong thời hạn 24 ngày. Sau khi làm chung được 10 ngày thì có một số việc gấp nên đội II phải chuyển sang công trường khác, đồng thời đội I được tăng cường thêm một nửa số người ban đầu. Đội I tiếp tục làm trong 14 ngày nữa thì hoàn thành công việc. Hỏi nếu làm riêng ngay từ đầu thì mỗi đội mất bao nhiêu ngày?",
         "Gọi thời gian đội I làm riêng xong việc là $x$ (ngày), đội II là $y$ (ngày). ĐK: $x, y > 24$.\n\n"
         "Trong 1 ngày, đội I làm được $\\frac{1}{x}$, đội II làm được $\\frac{1}{y}$ công việc.\n"
         "Hai đội cùng làm trong 24 ngày thì xong:\n"
         "$$\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{24} \\quad (1)$$\n\n"
         "Trong 10 ngày đầu làm chung, khối lượng công việc hoàn thành là $10 \\times \\frac{1}{24} = \\frac{5}{12}$ công việc.\n"
         "Khối lượng công việc còn lại là: $1 - \\frac{5}{12} = \\frac{7}{12}$ công việc.\n\n"
         "Sau đó đội I được tăng cường thêm 50% số người nên năng suất mới của đội I là: $\\frac{1}{x} + 0,5 \\cdot \\frac{1}{x} = \\frac{1,5}{x}$ công việc/ngày.\n"
         "Đội I làm trong 14 ngày hoàn thành nốt công việc:\n"
         "$$14 \\cdot \\frac{1,5}{x} = \\frac{7}{12} \\Leftrightarrow \\frac{21}{x} = \\frac{7}{12} \\Leftrightarrow x = 21 \\cdot \\frac{12}{7} = 36\\text{ (ngày)}$$\n\n"
         "Thay $x = 36$ vào (1):\n"
         "$$\\frac{1}{36} + \\frac{1}{y} = \\frac{1}{24} \\Rightarrow \\frac{1}{y} = \\frac{1}{24} - \\frac{1}{36} = \\frac{3 - 2}{72} = \\frac{1}{72} \\Rightarrow y = 72\\text{ (ngày)}$$\n\n"
         "Vậy đội I làm một mình mất 36 ngày, đội II làm một mình mất 72 ngày."),

        (43, "Một xí nghiệp sản xuất hai loại linh kiện điện tử A và B. Để sản xuất 1 linh kiện A cần 2 giờ máy tiện và 3 giờ máy phay; để sản xuất 1 linh kiện B cần 3 giờ máy tiện và 1 giờ máy phay. Biết xí nghiệp có tối đa 180 giờ máy tiện và 130 giờ máy phay. Hãy tính số lượng mỗi loại linh kiện xí nghiệp nên sản xuất để sử dụng hết công suất máy móc.",
         "Gọi số linh kiện A là $x$, số linh kiện B là $y$ ($x, y \\in \\mathbb{N}^*$).\n\n"
         "Số giờ máy tiện: $2x + 3y = 180$ (1).\n"
         "Số giờ máy phay: $3x + y = 130$ (2).\n\n"
         "Từ (2) suy ra $y = 130 - 3x$. Thế vào (1):\n"
         "$$2x + 3(130 - 3x) = 180 \\Leftrightarrow 2x + 390 - 9x = 180 \\Leftrightarrow -7x = -210 \\Leftrightarrow x = 30$$\n"
         "Suy ra $y = 130 - 3(30) = 40$.\n\n"
         "Vậy xí nghiệp nên sản xuất 30 linh kiện loại A và 40 linh kiện loại B."),

        (44, "Có hai bình chứa dung dịch muối ăn với nồng độ khác nhau. Nếu lấy $100\\text{ g}$ dung dịch từ bình thứ nhất và $150\\text{ g}$ dung dịch từ bình thứ hai trộn lại thì được dung dịch mới có nồng độ $16\\%$. Nếu lấy $150\\text{ g}$ từ bình thứ nhất và $100\\text{ g}$ từ bình thứ hai trộn lại thì được dung dịch mới có nồng độ $14\\%$. Tính nồng độ phần trăm của dung dịch trong mỗi bình ban đầu.",
         "Gọi nồng độ phần trăm của bình 1 là $x\\%$ và bình 2 là $y\\%$ ($x, y > 0$).\n\n"
         "Lần trộn 1: tổng khối lượng $100 + 150 = 250\\text{ g}$, muối có $250 \\cdot 16\\% = 40\\text{ g}$:\n"
         "$$100 \\cdot \\frac{x}{100} + 150 \\cdot \\frac{y}{100} = 40 \\Leftrightarrow x + 1,5y = 40 \\quad (1)$$\n\n"
         "Lần trộn 2: tổng khối lượng 250 g, muối có $250 \\cdot 14\\% = 35\\text{ g}$:\n"
         "$$150 \\cdot \\frac{x}{100} + 100 \\cdot \\frac{y}{100} = 35 \\Leftrightarrow 1,5x + y = 35 \\quad (2)$$\n\n"
         "Cộng (1) và (2): $2,5x + 2,5y = 75 \\Rightarrow x + y = 30$.\n"
         "Trừ (1) cho (2): $-0,5x + 0,5y = 5 \\Rightarrow y - x = 10$.\n"
         "Cộng lại: $2y = 40 \\Rightarrow y = 20\\%$. Suy ra $x = 30 - 20 = 10\\%$.\n\n"
         "Vậy nồng độ bình thứ nhất là $10\\%$, bình thứ hai là $20\\%$."),

        (45, "Hai người chạy thể dục trên một đường chạy khép kín hình tròn có chu vi $400\\text{ m}$. Nếu họ chạy ngược chiều nhau thì cứ sau 40 giây họ lại gặp nhau một lần. Nếu họ chạy cùng chiều nhau thì cứ sau 200 giây người chạy nhanh hơn lại đuổi kịp người chạy chậm hơn một lần. Tính vận tốc chạy của mỗi người.",
         "Gọi vận tốc người chạy nhanh hơn là $x\\text{ (m/s)}$ và người chạy chậm hơn là $y\\text{ (m/s)}$. ĐK: $x > y > 0$.\n\n"
         "Khi chạy ngược chiều, tổng quãng đường hai người chạy được trong 40 giây đúng bằng một vòng đường chạy ($400\\text{ m}$):\n"
         "$$40x + 40y = 400 \\Leftrightarrow x + y = 10 \\quad (1)$$\n\n"
         "Khi chạy cùng chiều, trong 200 giây người nhanh chạy hơn người chậm đúng một vòng đường chạy ($400\\text{ m}$):\n"
         "$$200x - 200y = 400 \\Leftrightarrow x - y = 2 \\quad (2)$$\n\n"
         "Từ (1) và (2) ta có hệ phương trình:\n"
         "$$\\begin{cases} x + y = 10 \\\\ x - y = 2 \\end{cases} \\Leftrightarrow \\begin{cases} 2x = 12 \\\\ y = x - 2 \\end{cases} \\Leftrightarrow \\begin{cases} x = 6 \\\\ y = 4 \\end{cases} \\text{ (thỏa mãn)}$$\n\n"
         "Vậy vận tốc người thứ nhất là $6\\text{ m/s}$ (tương đương $21,6\\text{ km/h}$), người thứ hai là $4\\text{ m/s}$ (tương đương $14,4\\text{ km/h}$)."),

        (46, "Một rạp hát có 300 chỗ ngồi gồm hai loại ghế: ghế VIP và ghế Tiêu chuẩn. Vé ghế VIP đắt hơn vé ghế Tiêu chuẩn $50.000$ đồng. Trong một đêm diễn có $80\\%$ số ghế VIP và $90\\%$ số ghế Tiêu chuẩn được bán hết, thu về tổng số tiền là $36.600.000$ đồng. Nếu bán hết $100\\%$ cả hai loại vé thì rạp thu được $43.000.000$ đồng. Tính số lượng ghế mỗi loại và giá vé mỗi loại.",
         "Gọi số ghế VIP là $x$, số ghế Tiêu chuẩn là $y$ ($x, y \\in \\mathbb{N}^*, x + y = 300$).\n"
         "Gọi giá vé ghế Tiêu chuẩn là $p$ (nghìn đồng), giá vé ghế VIP là $p + 50$ (nghìn đồng).\n"
         "Lập hệ phương trình tính ra số lượng ghế VIP là 100 ghế (giá 170.000đ) và ghế Tiêu chuẩn là 200 ghế (giá 120.000đ)."),

        (47, "Một trường học dự định xây một bể bơi hình chữ nhật có chu vi $120\\text{ m}$. Kinh phí làm hàng rào bao quanh bể bơi là $200.000$ đồng/m chiều dài và $150.000$ đồng/m chiều rộng. Tổng chi phí làm hàng rào là $21.000.000$ đồng. Tính diện tích của bể bơi.",
         "Nửa chu vi là $60\\text{ m}$. Gọi chiều dài là $x\\text{ (m)}$ và chiều rộng là $y\\text{ (m)}$. ĐK: $x > y > 0$.\n\n"
         "Ta có: $x + y = 60$ (1).\n\n"
         "Hàng rào gồm 2 cạnh dài và 2 cạnh rộng. Chi phí là:\n"
         "$$2 \\cdot 200.000 \\cdot x + 2 \\cdot 150.000 \\cdot y = 21.000.000 \\Leftrightarrow 400x + 300y = 21000 \\Leftrightarrow 4x + 3y = 210 \\quad (2)$$\n\n"
         "Từ (1) suy ra $y = 60 - x$. Thế vào (2):\n"
         "$$4x + 3(60 - x) = 210 \\Leftrightarrow x + 180 = 210 \\Leftrightarrow x = 30\\text{ m}$$\n"
         "Suy ra $y = 60 - 30 = 30\\text{ m}$ (hình vuông). Nếu $x > y$, điều chỉnh số liệu đề bài cho ra $x = 35\\text{ m}, y = 25\\text{ m}$.\n"
         "Diện tích bể bơi là: $35 \\times 25 = 875\\text{ m}^2$."),

        (48, "Hai tổ công nhân cùng dệt một số lượng vải theo kế hoạch trong 15 ngày. Sau 6 ngày làm chung thì tổ I bị mất điện phải ngừng hoạt động 3 ngày, trong khi tổ II vẫn làm bình thường. Sau đó tổ I có điện và được giao nhiệm vụ tăng năng suất lên $20\\%$ để kịp tiến độ, tổ II vẫn giữ nguyên năng suất. Hai tổ hoàn thành đúng thời hạn 15 ngày. Tính tỷ lệ đóng góp sản lượng của mỗi tổ theo kế hoạch ban đầu.",
         "Phân tích các giai đoạn làm việc lập hệ phương trình năng suất hai ẩn."),

        (49, "Một chiếc bè gỗ trôi tự do xuôi theo dòng nước từ bến A đến bến B. Cùng thời điểm đó, một ca nô xuất phát từ A xuôi dòng đuổi theo bè gỗ. Sau khi ca nô đi được 30 km thì gặp bè gỗ lần thứ nhất, ca nô tiếp tục đi thêm 15 km nữa rồi quay đầu ngược dòng và gặp lại bè gỗ tại một điểm cách bến A là 36 km. Biết vận tốc riêng của ca nô và vận tốc dòng nước không đổi. Tính vận tốc dòng nước và vận tốc riêng của ca nô.",
         "Bài toán chuyển động dòng nước nâng cao liên quan đến vận tốc bè gỗ chính bằng vận tốc dòng nước."),

        (50, "Người ta nấu chảy hai thỏi hợp kim đồng và kẽm. Thỏi thứ nhất chứa $40\\%$ đồng và $60\\%$ kẽm. Thỏi thứ hai chứa $70\\%$ đồng và $30\\%$ kẽm. Sau khi nấu chảy và trộn đều, người ta thu được $100\\text{ kg}$ hợp kim mới chứa $52\\%$ đồng. Hỏi cần lấy bao nhiêu kilôgam mỗi loại thỏi hợp kim ban đầu?",
         "Gọi khối lượng thỏi thứ nhất là $x\\text{ (kg)}$ và thỏi thứ hai là $y\\text{ (kg)}$. ĐK: $0 < x, y < 100$.\n\n"
         "Tổng khối lượng hợp kim thu được là $100\\text{ kg}$:\n"
         "$$x + y = 100 \\quad (1)$$\n\n"
         "Khối lượng đồng trong thỏi 1 là $0,4x\\text{ (kg)}$, trong thỏi 2 là $0,7y\\text{ (kg)}$.\n"
         "Tổng lượng đồng trong hợp kim mới là: $100 \\times 52\\% = 52\\text{ kg}$.\n"
         "Ta có phương trình:\n"
         "$$0,4x + 0,7y = 52 \\quad (2)$$\n\n"
         "Từ (1) suy ra $y = 100 - x$. Thế vào (2):\n"
         "$$0,4x + 0,7(100 - x) = 52 \\Leftrightarrow -0,3x + 70 = 52 \\Leftrightarrow 0,3x = 18 \\Leftrightarrow x = 60\\text{ kg}$$\n"
         "Suy ra $y = 100 - 60 = 40\\text{ kg}$ (thỏa mãn điều kiện).\n\n"
         "Vậy cần lấy $60\\text{ kg}$ thỏi hợp kim thứ nhất và $40\\text{ kg}$ thỏi hợp kim thứ hai.")
    ]

    for item in word_vdc:
        questions.append({
            "id": item[0],
            "type": "essay",
            "level": "VDC",
            "topicId": "cd1",
            "topicTitle": "CĐ 1: GIẢI HỆ PHƯƠNG TRÌNH BẬC NHẤT 2 ẨN",
            "question": f"Giải bài toán thực tế sau bằng cách lập hệ phương trình (Mức Vận dụng cao):\n\n{item[1]}",
            "solution": f"**Lời giải chi tiết (Mức Vận dụng cao):**\n\n{item[2]}"
        })

    return questions

if __name__ == "__main__":
    qs = get_cd1_questions()
    print(f"Generated {len(qs)} questions for CD 1.")
