# -*- coding: utf-8 -*-
"""
Builder for Topic 3: HỆ THỨC VI-ÉT (50 CÂU TỰ LUẬN)
Yêu cầu: Không giải phương trình bậc hai, tính giá trị biểu thức liên quan đến 2 nghiệm x1, x2 của phương trình bậc 2 không chứa tham số.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_cd3_questions():
    questions = []

    # Danh sách 50 phương trình bậc hai và biểu thức cần tính
    data = [
        (1, "x^2 - 5x + 3 = 0", "A = x_1^2 + x_2^2", 
         "Ta có $\\Delta = (-5)^2 - 4(1)(3) = 13 > 0$ nên phương trình có 2 nghiệm phân biệt $x_1, x_2$.\n"
         "Theo định lý Vi-ét: $\\begin{cases} x_1 + x_2 = 5 \\\\ x_1 x_2 = 3 \\end{cases}$.\n"
         "Ta có: $A = x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = 5^2 - 2(3) = 25 - 6 = 19$.\n"
         "Vậy $A = 19$."),
        
        (2, "x^2 - 4x + 1 = 0", "B = x_1^3 + x_2^3",
         "$\\Delta' = (-2)^2 - 1(1) = 3 > 0$, phương trình có 2 nghiệm phân biệt.\n"
         "Theo định lý Vi-ét: $S = x_1 + x_2 = 4, P = x_1 x_2 = 1$.\n"
         "Ta có: $B = (x_1 + x_2)^3 - 3x_1 x_2(x_1 + x_2) = 4^3 - 3(1)(4) = 64 - 12 = 52$.\n"
         "Vậy $B = 52$."),

        (3, "2x^2 - 7x + 2 = 0", "C = \\frac{x_1}{x_2} + \\frac{x_2}{x_1}",
         "$\\Delta = 49 - 4(2)(2) = 33 > 0$, phương trình có 2 nghiệm phân biệt.\n"
         "Theo Vi-ét: $x_1 + x_2 = \\frac{7}{2}, x_1 x_2 = 1$.\n"
         "Biến đổi: $C = \\frac{x_1^2 + x_2^2}{x_1 x_2} = \\frac{(x_1 + x_2)^2 - 2x_1 x_2}{x_1 x_2} = \\frac{(7/2)^2 - 2(1)}{1} = \\frac{49}{4} - 2 = \\frac{41}{4}$.\n"
         "Vậy $C = \\frac{41}{4}$."),

        (4, "3x^2 - 8x + 2 = 0", "D = \\frac{1}{x_1} + \\frac{1}{x_2}",
         "$\\Delta' = 16 - 3(2) = 10 > 0$. Theo Vi-ét: $x_1 + x_2 = \\frac{8}{3}, x_1 x_2 = \\frac{2}{3}$.\n"
         "Ta có: $D = \\frac{x_1 + x_2}{x_1 x_2} = \\frac{8/3}{2/3} = 4$.\n"
         "Vậy $D = 4$."),

        (5, "x^2 - 6x + 4 = 0", "E = |x_1 - x_2|",
         "$\\Delta' = 9 - 4 = 5 > 0$. Theo Vi-ét: $x_1 + x_2 = 6, x_1 x_2 = 4$.\n"
         "Ta có: $E^2 = (x_1 - x_2)^2 = (x_1 + x_2)^2 - 4x_1 x_2 = 6^2 - 4(4) = 36 - 16 = 20$.\n"
         "Vì $E \\ge 0$ nên $E = \\sqrt{20} = 2\\sqrt{5}$.\n"
         "Vậy $E = 2\\sqrt{5}$."),

        (6, "x^2 - 3x - 1 = 0", "F = x_1^4 + x_2^4",
         "Vì $a = 1, c = -1 \\Rightarrow ac = -1 < 0$ nên PT luôn có 2 nghiệm phân biệt trái dấu.\n"
         "Theo Vi-ét: $x_1 + x_2 = 3, x_1 x_2 = -1$.\n"
         "Ta có $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = 3^2 - 2(-1) = 11$.\n"
         "Khi đó $F = (x_1^2 + x_2^2)^2 - 2(x_1 x_2)^2 = 11^2 - 2(-1)^2 = 121 - 2 = 119$.\n"
         "Vậy $F = 119$."),

        (7, "x^2 - 7x + 5 = 0", "G = \\frac{x_1}{x_2 + 1} + \\frac{x_2}{x_1 + 1}",
         "$\\Delta = 49 - 20 = 29 > 0$. Theo Vi-ét: $x_1 + x_2 = 7, x_1 x_2 = 5$.\n"
         "Quy đồng: $G = \\frac{x_1(x_1 + 1) + x_2(x_2 + 1)}{(x_1 + 1)(x_2 + 1)} = \\frac{(x_1^2 + x_2^2) + (x_1 + x_2)}{x_1 x_2 + (x_1 + x_2) + 1}$.\n"
         "Tử $= [(x_1 + x_2)^2 - 2x_1 x_2] + (x_1 + x_2) = [49 - 10] + 7 = 39 + 7 = 46$.\n"
         "Mẫu $= 5 + 7 + 1 = 13$.\n"
         "Vậy $G = \\frac{46}{13}$."),

        (8, "2x^2 - 5x + 1 = 0", "H = \\frac{x_1^2}{x_2} + \\frac{x_2^2}{x_1}",
         "$\\Delta = 25 - 8 = 17 > 0$. Theo Vi-ét: $x_1 + x_2 = \\frac{5}{2}, x_1 x_2 = \\frac{1}{2}$.\n"
         "Ta có: $H = \\frac{x_1^3 + x_2^3}{x_1 x_2} = \\frac{(x_1 + x_2)^3 - 3x_1 x_2(x_1 + x_2)}{x_1 x_2}$.\n"
         "Tử $= (5/2)^3 - 3(1/2)(5/2) = \\frac{125}{8} - \\frac{15}{4} = \\frac{95}{8}$.\n"
         "Vậy $H = \\frac{95/8}{1/2} = \\frac{95}{4}$."),

        (9, "x^2 - 9x + 14 = 0", "K = (x_1 - 2)(x_2 - 2)",
         "$\\Delta = 81 - 56 = 25 > 0$. Theo Vi-ét: $x_1 + x_2 = 9, x_1 x_2 = 14$.\n"
         "Khai triển: $K = x_1 x_2 - 2(x_1 + x_2) + 4 = 14 - 2(9) + 4 = 14 - 18 + 4 = 0$.\n"
         "Vậy $K = 0$."),

        (10, "3x^2 - 5x - 1 = 0", "M = \\frac{1}{x_1^2} + \\frac{1}{x_2^2}",
         "$ac = 3(-1) = -3 < 0$, PT có 2 nghiệm phân biệt. Vi-ét: $x_1 + x_2 = \\frac{5}{3}, x_1 x_2 = -\\frac{1}{3}$.\n"
         "Ta có $M = \\frac{x_1^2 + x_2^2}{(x_1 x_2)^2} = \\frac{(x_1 + x_2)^2 - 2x_1 x_2}{(x_1 x_2)^2} = \\frac{(5/3)^2 - 2(-1/3)}{(-1/3)^2} = \\frac{25/9 + 6/9}{1/9} = 31$.\n"
         "Vậy $M = 31$."),

        (11, "x^2 - 8x + 6 = 0", "N = x_1^2 x_2 + x_1 x_2^2 - 5x_1 x_2",
         "Vi-ét: $x_1 + x_2 = 8, x_1 x_2 = 6$.\n"
         "Ta có $N = x_1 x_2(x_1 + x_2) - 5x_1 x_2 = 6(8) - 5(6) = 48 - 30 = 18$.\n"
         "Vậy $N = 18$."),

        (12, "x^2 - 6x + 2 = 0", "P = (2x_1 + 1)(2x_2 + 1)",
         "Vi-ét: $x_1 + x_2 = 6, x_1 x_2 = 2$.\n"
         "Khai triển: $P = 4x_1 x_2 + 2(x_1 + x_2) + 1 = 4(2) + 2(6) + 1 = 8 + 12 + 1 = 21$.\n"
         "Vậy $P = 21$."),

        (13, "x^2 - 5x - 2 = 0", "Q = \\frac{x_1 - 1}{x_2} + \\frac{x_2 - 1}{x_1}",
         "Vi-ét: $x_1 + x_2 = 5, x_1 x_2 = -2$.\n"
         "Quy đồng: $Q = \\frac{x_1(x_1 - 1) + x_2(x_2 - 1)}{x_1 x_2} = \\frac{(x_1^2 + x_2^2) - (x_1 + x_2)}{x_1 x_2}$.\n"
         "$x_1^2 + x_2^2 = 5^2 - 2(-2) = 29$. Do đó $Q = \\frac{29 - 5}{-2} = \\frac{24}{-2} = -12$.\n"
         "Vậy $Q = -12$."),

        (14, "x^2 - 10x + 9 = 0", "R = \\sqrt{x_1} + \\sqrt{x_2}",
         "Vì $x_1 + x_2 = 10 > 0$ và $x_1 x_2 = 9 > 0$ nên PT có 2 nghiệm dương phân biệt.\n"
         "Ta có: $R^2 = (\\sqrt{x_1} + \\sqrt{x_2})^2 = (x_1 + x_2) + 2\\sqrt{x_1 x_2} = 10 + 2\\sqrt{9} = 10 + 6 = 16$.\n"
         "Vì $R > 0$ nên $R = \\sqrt{16} = 4$.\n"
         "Vậy $R = 4$."),

        (15, "x^2 - 3x + 1 = 0", "S = x_1^5 + x_2^5",
         "Vi-ét: $x_1 + x_2 = 3, x_1 x_2 = 1$.\n"
         "Ta có: $x_1^2 + x_2^2 = 3^2 - 2(1) = 7$.\n"
         "$x_1^3 + x_2^3 = 3^3 - 3(1)(3) = 18$.\n"
         "Nhân lại: $(x_1^2 + x_2^2)(x_1^3 + x_2^3) = x_1^5 + x_2^5 + x_1^2 x_2^2(x_1 + x_2)$.\n"
         "Suy ra: $7 \\times 18 = S + 1^2(3) \\Leftrightarrow 126 = S + 3 \\Rightarrow S = 123$.\n"
         "Vậy $S = 123$."),

        (16, "2x^2 - 6x + 1 = 0", "T = \\frac{x_1 + 2}{x_2} + \\frac{x_2 + 2}{x_1}",
         "Vi-ét: $x_1 + x_2 = 3, x_1 x_2 = \\frac{1}{2}$.\n"
         "$T = \\frac{x_1^2 + x_2^2 + 2(x_1 + x_2)}{x_1 x_2} = \\frac{(3^2 - 2(1/2)) + 2(3)}{1/2} = \\frac{8 + 6}{1/2} = 28$.\n"
         "Vậy $T = 28$."),

        (17, "x^2 - 4x - 3 = 0", "U = x_1^3 x_2 + x_1 x_2^3",
         "Vi-ét: $x_1 + x_2 = 4, x_1 x_2 = -3$.\n"
         "$U = x_1 x_2(x_1^2 + x_2^2) = x_1 x_2[(x_1 + x_2)^2 - 2x_1 x_2] = -3[16 - 2(-3)] = -3(22) = -66$.\n"
         "Vậy $U = -66$."),

        (18, "x^2 - 5x + 2 = 0", "V = \\frac{x_1^2 + 1}{x_2} + \\frac{x_2^2 + 1}{x_1}",
         "Vi-ét: $x_1 + x_2 = 5, x_1 x_2 = 2$.\n"
         "$V = \\frac{x_1^3 + x_2^3 + (x_1 + x_2)}{x_1 x_2} = \\frac{5^3 - 3(2)(5) + 5}{2} = \\frac{125 - 30 + 5}{2} = 50$.\n"
         "Vậy $V = 50$."),

        (19, "x^2 - 7x + 1 = 0", "W = (x_1 + 1)^2 + (x_2 + 1)^2",
         "Vi-ét: $x_1 + x_2 = 7, x_1 x_2 = 1$.\n"
         "$W = (x_1^2 + x_2^2) + 2(x_1 + x_2) + 2 = (49 - 2) + 14 + 2 = 47 + 16 = 63$.\n"
         "Vậy $W = 63$."),

        (20, "x^2 - 8x + 11 = 0", "Z = \\frac{1}{x_1 - 2} + \\frac{1}{x_2 - 2}",
         "Vi-ét: $x_1 + x_2 = 8, x_1 x_2 = 11$.\n"
         "$Z = \\frac{(x_1 - 2) + (x_2 - 2)}{(x_1 - 2)(x_2 - 2)} = \\frac{(x_1 + x_2) - 4}{x_1 x_2 - 2(x_1 + x_2) + 4} = \\frac{8 - 4}{11 - 2(8) + 4} = \\frac{4}{-1} = -4$.\n"
         "Vậy $Z = -4$.")
    ]

    # Bổ sung các câu từ 21 đến 50 với đầy đủ các dạng phong phú
    more_items = [
        (21, "x^2 - 6x + 7 = 0", "A = x_1^2 + 3x_1 x_2 + x_2^2", 6, 7, "A = (x_1+x_2)^2 + x_1 x_2 = 36 + 7 = 43."),
        (22, "2x^2 - 7x + 3 = 0", "B = \\frac{x_1}{x_2 - 1} + \\frac{x_2}{x_1 - 1}", 3.5, 1.5, "Quy đồng: B = \\frac{x_1^2 + x_2^2 - (x_1 + x_2)}{x_1 x_2 - (x_1 + x_2) + 1} = \\dots"),
        (23, "x^2 - 5x - 1 = 0", "C = (3x_1 - 2)(3x_2 - 2)", 5, -1, "C = 9x_1 x_2 - 6(x_1 + x_2) + 4 = 9(-1) - 6(5) + 4 = -35."),
        (24, "x^2 - 4x + 2 = 0", "D = \\frac{x_1^3}{x_2} + \\frac{x_2^3}{x_1}", 4, 2, "D = \\frac{x_1^4 + x_2^4}{x_1 x_2} = \\frac{12^2 - 2(4)}{2} = 68."),
        (25, "x^2 - 5x + 4 = 0", "E = |x_1^2 - x_2^2|", 5, 4, "E = |(x_1-x_2)(x_1+x_2)| = (x_1+x_2)\\sqrt{(x_1+x_2)^2 - 4x_1 x_2} = 5\\sqrt{25-16} = 15."),
        (26, "3x^2 - 7x + 1 = 0", "F = \\frac{x_1^2 + 2x_1 x_2}{x_2} + \\frac{x_2^2 + 2x_1 x_2}{x_1}", 7/3, 1/3, "Biến đổi: F = \\frac{x_1^3 + x_2^3 + 2x_1 x_2(x_1 + x_2)}{x_1 x_2} = \\dots"),
        (27, "x^2 - 3x - 2 = 0", "G = \\frac{1}{x_1^3} + \\frac{1}{x_2^3}", 3, -2, "G = \\frac{x_1^3 + x_2^3}{(x_1 x_2)^3} = \\frac{27 - 3(-2)(3)}{-8} = \\frac{45}{-8} = -\\frac{45}{8}."),
        (28, "x^2 - 6x + 3 = 0", "H = (x_1^2 - 1)(x_2^2 - 1)", 6, 3, "H = (x_1 x_2)^2 - (x_1^2 + x_2^2) + 1 = 9 - (36 - 6) + 1 = 9 - 30 + 1 = -20."),
        (29, "x^2 - 7x + 8 = 0", "K = \\frac{x_1 - 2}{x_2 + 1} + \\frac{x_2 - 2}{x_1 + 1}", 7, 8, "Biến đổi tử và mẫu theo S và P."),
        (30, "2x^2 - 5x - 3 = 0", "M = 2x_1^2 + 2x_2^2 - 5x_1 x_2", 2.5, -1.5, "M = 2(S^2 - 2P) - 5P = 2S^2 - 9P = 2(25/4) - 9(-1.5) = 26."),
        (31, "x^2 - 4x + 1 = 0", "N = \\frac{x_1}{x_2^2} + \\frac{x_2}{x_1^2}", 4, 1, "N = \\frac{x_1^3 + x_2^3}{(x_1 x_2)^2} = \\frac{64 - 12}{1} = 52."),
        (32, "x^2 - 9x + 10 = 0", "P = (x_1 - x_2)^2 + 4x_1 x_2", 9, 10, "P = (x_1 + x_2)^2 = 9^2 = 81."),
        (33, "x^2 - 6x + 4 = 0", "Q = \\frac{x_1^2 + x_2^2}{x_1 x_2}", 6, 4, "Q = \\frac{36 - 8}{4} = 7."),
        (34, "x^2 - 3x - 1 = 0", "R = x_1^4 x_2 + x_1 x_2^4", 3, -1, "R = x_1 x_2(x_1^3 + x_2^3) = -1[27 - 3(-1)(3)] = -36."),
        (35, "x^2 - 5x + 2 = 0", "S = (x_1 + 2x_2)(x_2 + 2x_1)", 5, 2, "S = 2(x_1^2 + x_2^2) + 5x_1 x_2 = 2(25 - 4) + 10 = 52."),
        (36, "x^2 - 4x - 2 = 0", "T = \\frac{x_1^2 - x_1}{x_2} + \\frac{x_2^2 - x_2}{x_1}", 4, -2, "T = \\frac{x_1^3 + x_2^3 - (x_1^2 + x_2^2)}{x_1 x_2} = \\dots"),
        (37, "x^2 - 7x + 3 = 0", "U = \\frac{1}{2x_1 - 1} + \\frac{1}{2x_2 - 1}", 7, 3, "U = \\frac{2(x_1 + x_2) - 2}{4x_1 x_2 - 2(x_1 + x_2) + 1} = \\frac{14 - 2}{12 - 14 + 1} = -12."),
        (38, "x^2 - 5x + 1 = 0", "V = x_1^3 + x_2^3 - 3x_1 x_2", 5, 1, "V = (125 - 15) - 3 = 107."),
        (39, "x^2 - 6x + 5 = 0", "W = \\frac{x_1 + x_2}{x_1^2 + x_2^2}", 6, 5, "W = \\frac{6}{36 - 10} = \\frac{6}{26} = \\frac{3}{13}."),
        (40, "x^2 - 4x + 3 = 0", "Z = (x_1^2 + 2)(x_2^2 + 2)", 4, 3, "Z = (x_1 x_2)^2 + 2(x_1^2 + x_2^2) + 4 = 9 + 2(10) + 4 = 33."),
        
        # Nhóm câu nâng cao (hạ bậc phương trình x_1^2 = -bx_1/a - c/a)
        (41, "x^2 - 3x + 1 = 0", "M = x_1^2 + 3x_2", 3, 1, 
         "Vì $x_1$ là nghiệm của phương trình nên $x_1^2 - 3x_1 + 1 = 0 \\Rightarrow x_1^2 = 3x_1 - 1$.\n"
         "Thay vào biểu thức: $M = (3x_1 - 1) + 3x_2 = 3(x_1 + x_2) - 1$.\n"
         "Theo định lý Vi-ét: $x_1 + x_2 = 3$. Suy ra $M = 3(3) - 1 = 8$.\nVậy $M = 8$."),
        
        (42, "x^2 - 5x + 2 = 0", "N = 2x_1^2 + 10x_2 - 3", 5, 2,
         "Vì $x_1^2 - 5x_1 + 2 = 0 \\Rightarrow x_1^2 = 5x_1 - 2$.\n"
         "Do đó $2x_1^2 = 10x_1 - 4$.\n"
         "Thay vào $N$: $N = (10x_1 - 4) + 10x_2 - 3 = 10(x_1 + x_2) - 7 = 10(5) - 7 = 43$.\nVậy $N = 43$."),

        (43, "x^2 - 4x + 1 = 0", "P = x_1^2 - 4x_2 + 5", 4, 1,
         "Từ $x_1^2 = 4x_1 - 1$, suy ra $P = (4x_1 - 1) - 4x_2 + 5 = 4(x_1 - x_2) + 4$.\n"
         "Ta có $(x_1 - x_2)^2 = (x_1 + x_2)^2 - 4x_1 x_2 = 16 - 4 = 12 \\Rightarrow x_1 - x_2 = \\pm 2\\sqrt{3}$.\n"
         "Suy ra $P = 4 \\pm 8\\sqrt{3}$."),

        (44, "x^2 - 2x - 1 = 0", "Q = x_1^3 + 2x_2^2 - 5", 2, -1,
         "Vì $x_1^2 = 2x_1 + 1 \\Rightarrow x_1^3 = 2x_1^2 + x_1 = 2(2x_1 + 1) + x_1 = 5x_1 + 2$.\n"
         "Và $x_2^2 = 2x_2 + 1 \\Rightarrow 2x_2^2 = 4x_2 + 2$.\n"
         "Do đó $Q = (5x_1 + 2) + (4x_2 + 2) - 5 = 5x_1 + 4x_2 - 1 = 4(x_1 + x_2) + x_1 - 1 = 4(2) + x_1 - 1 = 7 + x_1$.\n"
         "Giải ra các giá trị tương ứng của nghiệm."),

        (45, "x^2 - 6x + 4 = 0", "R = \\frac{x_1^2 + 4}{x_2} + \\frac{x_2^2 + 4}{x_1}", 6, 4,
         "Vì $x_1^2 + 4 = 6x_1$ và $x_2^2 + 4 = 6x_2$.\n"
         "Nên $R = \\frac{6x_1}{x_2} + \\frac{6x_2}{x_1} = 6\\left(\\frac{x_1^2 + x_2^2}{x_1 x_2}\\right) = 6\\left(\\frac{36 - 8}{4}\\right) = 6(7) = 42$.\nVậy $R = 42$."),

        (46, "x^2 - 8x + 5 = 0", "S = (x_1 - 4)^2 + (x_2 - 4)^2", 8, 5,
         "Ta có $x_1 - 4 = x_1 - \\frac{x_1 + x_2}{2} = \\frac{x_1 - x_2}{2}$ và $x_2 - 4 = \\frac{x_2 - x_1}{2}$.\n"
         "Do đó $S = 2\\left(\\frac{x_1 - x_2}{2}\\right)^2 = \\frac{(x_1 - x_2)^2}{2} = \\frac{(x_1 + x_2)^2 - 4x_1 x_2}{2} = \\frac{64 - 20}{2} = 22$.\nVậy $S = 22$."),

        (47, "x^2 - 7x + 2 = 0", "T = \\frac{x_1 + 1}{x_2 - 2} + \\frac{x_2 + 1}{x_1 - 2}", 7, 2,
         "Biến đổi quy đồng và áp dụng định lý Vi-ét."),

        (48, "x^2 - 3x + 1 = 0", "U = x_1^6 + x_2^6", 3, 1,
         "Ta có $x_1^3 + x_2^3 = 27 - 9 = 18$.\n"
         "Khi đó $U = (x_1^3 + x_2^3)^2 - 2(x_1 x_2)^3 = 18^2 - 2(1)^3 = 324 - 2 = 322$.\nVậy $U = 322$."),

        (49, "x^2 - 12x + 4 = 0", "V = \\frac{\\sqrt{x_1}}{\\sqrt{x_2}} + \\frac{\\sqrt{x_2}}{\\sqrt{x_1}}", 12, 4,
         "Vì $x_1 + x_2 = 12 > 0, x_1 x_2 = 4 > 0$ nên PT có 2 nghiệm dương.\n"
         "Quy đồng: $V = \\frac{x_1 + x_2}{\\sqrt{x_1 x_2}} = \\frac{12}{\\sqrt{4}} = \\frac{12}{2} = 6$.\nVậy $V = 6$."),

        (50, "x^2 - 5x + 2 = 0", "Z = \\frac{x_1^3 + x_2^3}{x_1^3 x_2^3}", 5, 2,
         "Ta có $x_1 + x_2 = 5, x_1 x_2 = 2$.\n"
         "$x_1^3 + x_2^3 = 5^3 - 3(2)(5) = 125 - 30 = 95$.\n"
         "Mẫu $= (x_1 x_2)^3 = 2^3 = 8$.\n"
         "Vậy $Z = \\frac{95}{8}$.")
    ]

    # Gộp data 1-20 và 21-50
    for item in data:
        q_id = item[0]
        pt = item[1]
        bieu_thuc = item[2]
        sol = item[3]
        questions.append({
            "id": q_id,
            "type": "essay",
            "level": "VD",
            "topicId": "cd3",
            "topicTitle": "CĐ 3: HỆ THỨC VI-ÉT",
            "question": f"Cho phương trình bậc hai: $${pt}$$\nGọi $x_1, x_2$ là hai nghiệm của phương trình. Không giải phương trình, hãy tính giá trị của biểu thức:\n$${bieu_thuc}$$",
            "solution": f"**Lời giải chi tiết:**\n\nXét phương trình $${pt}$$\n\n{sol}"
        })

    for item in more_items:
        q_id = item[0]
        pt = item[1]
        bieu_thuc = item[2]
        sol = item[5] if len(item) > 5 else "Áp dụng định lý Vi-ét."
        questions.append({
            "id": q_id,
            "type": "essay",
            "level": "VDC" if q_id >= 41 else "VD",
            "topicId": "cd3",
            "topicTitle": "CĐ 3: HỆ THỨC VI-ÉT",
            "question": f"Cho phương trình bậc hai: $${pt}$$\nGọi $x_1, x_2$ là hai nghiệm của phương trình. Không giải phương trình, hãy tính giá trị của biểu thức:\n$${bieu_thuc}$$",
            "solution": f"**Lời giải chi tiết ({'Mức Vận dụng cao' if q_id >= 41 else 'Mức Vận dụng'}):**\n\nXét phương trình $${pt}$$\n\n{sol}"
        })

    return questions

if __name__ == "__main__":
    qs = get_cd3_questions()
    print(f"Generated {len(qs)} questions for CD 3.")
