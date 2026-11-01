# -*- coding: utf-8 -*-
"""
Builder for Topic 3: HỆ THỨC VI-ÉT (50 CÂU TỰ LUẬN)
Yêu cầu nâng cấp:
- Câu 1 đến 40: Tập trung vào bài toán tính giá trị biểu thức dạng PHÂN THỨC liên quan đến 2 nghiệm x1, x2 của phương trình bậc 2 không chứa tham số.
- Câu 41 đến 50: 10 bài biểu thức KHÔNG ĐỐI XỨNG giữa x1 và x2 (dùng phương pháp hạ bậc nghiệm từ phương trình ban đầu).
- Tất cả các câu đều có lời giải chi tiết, tính toán chuẩn xác 100%, thỏa mãn Quy tắc 1 (**Câu [Số]:** ).
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_cd3_questions():
    questions = []

    # 40 bài biểu thức phân thức (Câu 1 - 40)
    frac_data = [
        (1, "x^2 - 5x + 3 = 0", "A = \\frac{1}{x_1} + \\frac{1}{x_2}",
         "Ta có $\\Delta = (-5)^2 - 4(1)(3) = 25 - 12 = 13 > 0$ nên phương trình có hai nghiệm phân biệt $x_1, x_2$.\n"
         "Theo định lí Vi-ét, ta có:\n"
         "$$\\begin{cases} x_1 + x_2 = 5 \\\\ x_1 x_2 = 3 \\end{cases}$$\n"
         "Quy đồng mẫu số biểu thức $A$:\n"
         "$$A = \\frac{x_1 + x_2}{x_1 x_2} = \\frac{5}{3}$$\n"
         "Vậy $A = \\frac{5}{3}$."),

        (2, "2x^2 - 7x + 2 = 0", "B = \\frac{x_1}{x_2} + \\frac{x_2}{x_1}",
         "Ta có $\\Delta = (-7)^2 - 4(2)(2) = 49 - 16 = 33 > 0$ nên phương trình có hai nghiệm phân biệt $x_1, x_2$.\n"
         "Theo định lí Vi-ét:\n"
         "$$\\begin{cases} x_1 + x_2 = \\frac{7}{2} \\\\ x_1 x_2 = \\frac{2}{2} = 1 \\end{cases}$$\n"
         "Biến đổi biểu thức $B$:\n"
         "$$B = \\frac{x_1^2 + x_2^2}{x_1 x_2} = \\frac{(x_1 + x_2)^2 - 2x_1 x_2}{x_1 x_2} = \\frac{\\left(\\frac{7}{2}\\right)^2 - 2(1)}{1} = \\frac{49}{4} - 2 = \\frac{41}{4}$$\n"
         "Vậy $B = \\frac{41}{4}$."),

        (3, "x^2 - 4x + 1 = 0", "C = \\frac{x_1^2}{x_2} + \\frac{x_2^2}{x_1}",
         "Ta có $\\Delta' = (-2)^2 - 1(1) = 3 > 0$ nên phương trình có hai nghiệm phân biệt.\n"
         "Theo định lí Vi-ét:\n"
         "$$\\begin{cases} x_1 + x_2 = 4 \\\\ x_1 x_2 = 1 \\end{cases}$$\n"
         "Quy đồng mẫu số biểu thức $C$:\n"
         "$$C = \\frac{x_1^3 + x_2^3}{x_1 x_2} = \\frac{(x_1 + x_2)^3 - 3x_1 x_2(x_1 + x_2)}{x_1 x_2}$$\n"
         "Thay số vào ta được:\n"
         "$$C = \\frac{4^3 - 3(1)(4)}{1} = 64 - 12 = 52$$\n"
         "Vậy $C = 52$."),

        (4, "3x^2 - 8x + 2 = 0", "D = \\frac{1}{x_1^2} + \\frac{1}{x_2^2}",
         "Ta có $\\Delta' = (-4)^2 - 3(2) = 16 - 6 = 10 > 0$. Phương trình có hai nghiệm phân biệt.\n"
         "Theo định lí Vi-ét:\n"
         "$$\\begin{cases} x_1 + x_2 = \\frac{8}{3} \\\\ x_1 x_2 = \\frac{2}{3} \\end{cases}$$\n"
         "Biến đổi biểu thức $D$:\n"
         "$$D = \\frac{x_1^2 + x_2^2}{(x_1 x_2)^2} = \\frac{(x_1 + x_2)^2 - 2x_1 x_2}{(x_1 x_2)^2} = \\frac{\\left(\\frac{8}{3}\\right)^2 - 2\\left(\\frac{2}{3}\\right)}{\\left(\\frac{2}{3}\\right)^2} = \\frac{\\frac{64}{9} - \\frac{12}{9}}{\\frac{4}{9}} = \\frac{52}{4} = 13$$\n"
         "Vậy $D = 13$."),

        (5, "x^2 - 6x + 4 = 0", "E = \\frac{x_1 - 1}{x_2} + \\frac{x_2 - 1}{x_1}",
         "Ta có $\\Delta' = (-3)^2 - 1(4) = 5 > 0$. Theo định lí Vi-ét:\n"
         "$$\\begin{cases} x_1 + x_2 = 6 \\\\ x_1 x_2 = 4 \\end{cases}$$\n"
         "Quy đồng mẫu số:\n"
         "$$E = \\frac{x_1(x_1 - 1) + x_2(x_2 - 1)}{x_1 x_2} = \\frac{x_1^2 + x_2^2 - (x_1 + x_2)}{x_1 x_2}$$\n"
         "Ta có $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = 6^2 - 2(4) = 36 - 8 = 28$.\n"
         "Suy ra:\n"
         "$$E = \\frac{28 - 6}{4} = \\frac{22}{4} = \\frac{11}{2}$$\n"
         "Vậy $E = \\frac{11}{2}$."),

        (6, "x^2 - 7x + 5 = 0", "F = \\frac{1}{x_1 - 1} + \\frac{1}{x_2 - 1}",
         "Ta có $\\Delta = (-7)^2 - 4(1)(5) = 29 > 0$. Theo định lí Vi-ét:\n"
         "$$\\begin{cases} x_1 + x_2 = 7 \\\\ x_1 x_2 = 5 \\end{cases}$$\n"
         "Quy đồng mẫu số biểu thức $F$:\n"
         "$$F = \\frac{(x_2 - 1) + (x_1 - 1)}{(x_1 - 1)(x_2 - 1)} = \\frac{x_1 + x_2 - 2}{x_1 x_2 - (x_1 + x_2) + 1}$$\n"
         "Thay số:\n"
         "$$F = \\frac{7 - 2}{5 - 7 + 1} = \\frac{5}{-1} = -5$$\n"
         "Vậy $F = -5$."),

        (7, "2x^2 - 5x + 1 = 0", "G = \\frac{x_1}{x_2 + 1} + \\frac{x_2}{x_1 + 1}",
         "Ta có $\\Delta = 25 - 8 = 17 > 0$. Theo Vi-ét:\n"
         "$$\\begin{cases} x_1 + x_2 = \\frac{5}{2} \\\\ x_1 x_2 = \\frac{1}{2} \\end{cases}$$\n"
         "Quy đồng mẫu số:\n"
         "$$G = \\frac{x_1(x_1 + 1) + x_2(x_2 + 1)}{(x_1 + 1)(x_2 + 1)} = \\frac{(x_1^2 + x_2^2) + (x_1 + x_2)}{x_1 x_2 + (x_1 + x_2) + 1}$$\n"
         "Tử thức: $x_1^2 + x_2^2 + (x_1 + x_2) = \\left[\\left(\\frac{5}{2}\\right)^2 - 2\\left(\\frac{1}{2}\\right)\\right] + \\frac{5}{2} = \\left(\\frac{25}{4} - 1\\right) + \\frac{5}{2} = \\frac{21}{4} + \\frac{10}{4} = \\frac{31}{4}$.\n"
         "Mẫu thức: $\\frac{1}{2} + \\frac{5}{2} + 1 = 3 + 1 = 4$.\n"
         "Suy ra $G = \\frac{31/4}{4} = \\frac{31}{16}$.\n"
         "Vậy $G = \\frac{31}{16}$."),

        (8, "x^2 - 3x - 2 = 0", "H = \\frac{x_1 + 1}{x_2} + \\frac{x_2 + 1}{x_1}",
         "Vì $a = 1, c = -2 \\Rightarrow ac = -2 < 0$ nên PT luôn có 2 nghiệm phân biệt khác dấu.\n"
         "Theo Vi-ét: $x_1 + x_2 = 3$ và $x_1 x_2 = -2$.\n"
         "Quy đồng:\n"
         "$$H = \\frac{x_1(x_1 + 1) + x_2(x_2 + 1)}{x_1 x_2} = \\frac{(x_1^2 + x_2^2) + (x_1 + x_2)}{x_1 x_2}$$\n"
         "Ta có $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = 3^2 - 2(-2) = 13$.\n"
         "Do đó: $H = \\frac{13 + 3}{-2} = \\frac{16}{-2} = -8$.\n"
         "Vậy $H = -8$."),

        (9, "x^2 - 6x + 2 = 0", "K = \\frac{1}{x_1 + 2} + \\frac{1}{x_2 + 2}",
         "$\\Delta' = 9 - 2 = 7 > 0$. Theo Vi-ét: $x_1 + x_2 = 6, x_1 x_2 = 2$.\n"
         "Quy đồng:\n"
         "$$K = \\frac{(x_2 + 2) + (x_1 + 2)}{(x_1 + 2)(x_2 + 2)} = \\frac{x_1 + x_2 + 4}{x_1 x_2 + 2(x_1 + x_2) + 4}$$\n"
         "Thay số:\n"
         "$$K = \\frac{6 + 4}{2 + 2(6) + 4} = \\frac{10}{2 + 12 + 4} = \\frac{10}{18} = \\frac{5}{9}$$\n"
         "Vậy $K = \\frac{5}{9}$."),

        (10, "3x^2 - 7x + 1 = 0", "M = \\frac{x_1^2 + 1}{x_2} + \\frac{x_2^2 + 1}{x_1}",
         "$\\Delta = 49 - 12 = 37 > 0$. Theo Vi-ét: $x_1 + x_2 = \\frac{7}{3}, x_1 x_2 = \\frac{1}{3}$.\n"
         "Quy đồng:\n"
         "$$M = \\frac{x_1(x_1^2 + 1) + x_2(x_2^2 + 1)}{x_1 x_2} = \\frac{(x_1^3 + x_2^3) + (x_1 + x_2)}{x_1 x_2}$$\n"
         "Ta có $x_1^3 + x_2^3 = (x_1 + x_2)^3 - 3x_1 x_2(x_1 + x_2) = \\left(\\frac{7}{3}\\right)^3 - 3\\left(\\frac{1}{3}\\right)\\left(\\frac{7}{3}\\right) = \\frac{343}{27} - \\frac{7}{3} = \\frac{280}{27}$.\n"
         "Tử thức $= \\frac{280}{27} + \\frac{7}{3} = \\frac{343}{27}$.\n"
         "Mẫu thức $= \\frac{1}{3}$.\n"
         "Suy ra $M = \\frac{343/27}{1/3} = \\frac{343}{9}$.\n"
         "Vậy $M = \\frac{343}{9}$."),

        (11, "x^2 - 4x - 1 = 0", "N = \\frac{x_1}{x_2^2} + \\frac{x_2}{x_1^2}",
         "Vì $ac = -1 < 0$ nên PT có 2 nghiệm phân biệt trái dấu. Theo Vi-ét: $x_1 + x_2 = 4, x_1 x_2 = -1$.\n"
         "Quy đồng:\n"
         "$$N = \\frac{x_1^3 + x_2^3}{(x_1 x_2)^2} = \\frac{(x_1 + x_2)^3 - 3x_1 x_2(x_1 + x_2)}{(x_1 x_2)^2}$$\n"
         "Thay số:\n"
         "$$N = \\frac{4^3 - 3(-1)(4)}{(-1)^2} = \\frac{64 + 12}{1} = 76$$\n"
         "Vậy $N = 76$."),

        (12, "2x^2 - 9x + 4 = 0", "P = \\frac{x_1 - 2}{x_2} + \\frac{x_2 - 2}{x_1}",
         "$\\Delta = 81 - 32 = 49 > 0$. Theo Vi-ét: $x_1 + x_2 = \\frac{9}{2}, x_1 x_2 = 2$.\n"
         "Quy đồng:\n"
         "$$P = \\frac{x_1(x_1 - 2) + x_2(x_2 - 2)}{x_1 x_2} = \\frac{(x_1^2 + x_2^2) - 2(x_1 + x_2)}{x_1 x_2}$$\n"
         "Ta có $x_1^2 + x_2^2 = \\left(\\frac{9}{2}\\right)^2 - 2(2) = \\frac{81}{4} - 4 = \\frac{65}{4}$.\n"
         "Tử thức $= \\frac{65}{4} - 2\\left(\\frac{9}{2}\\right) = \\frac{65}{4} - 9 = \\frac{29}{4}$.\n"
         "Suy ra $P = \\frac{29/4}{2} = \\frac{29}{8}$.\n"
         "Vậy $P = \\frac{29}{8}$."),

        (13, "x^2 - 5x + 1 = 0", "Q = \\frac{1}{x_1^3} + \\frac{1}{x_2^3}",
         "$\\Delta = 25 - 4 = 21 > 0$. Theo Vi-ét: $x_1 + x_2 = 5, x_1 x_2 = 1$.\n"
         "Quy đồng:\n"
         "$$Q = \\frac{x_1^3 + x_2^3}{(x_1 x_2)^3} = \\frac{(x_1 + x_2)^3 - 3x_1 x_2(x_1 + x_2)}{(x_1 x_2)^3}$$\n"
         "Thay số: $Q = \\frac{5^3 - 3(1)(5)}{1^3} = 125 - 15 = 110$.\n"
         "Vậy $Q = 110$."),

        (14, "x^2 - 8x + 3 = 0", "R = \\frac{x_1 + 2}{x_2} + \\frac{x_2 + 2}{x_1}",
         "$\\Delta' = 16 - 3 = 13 > 0$. Theo Vi-ét: $x_1 + x_2 = 8, x_1 x_2 = 3$.\n"
         "Quy đồng: $R = \\frac{(x_1^2 + x_2^2) + 2(x_1 + x_2)}{x_1 x_2}$.\n"
         "Ta có $x_1^2 + x_2^2 = 8^2 - 2(3) = 58$.\n"
         "Suy ra $R = \\frac{58 + 2(8)}{3} = \\frac{74}{3}$.\n"
         "Vậy $R = \\frac{74}{3}$."),

        (15, "x^2 - 6x - 3 = 0", "S = \\frac{x_1^2 - 1}{x_2} + \\frac{x_2^2 - 1}{x_1}",
         "Vì $ac = -3 < 0$ nên PT có 2 nghiệm phân biệt trái dấu. Theo Vi-ét: $x_1 + x_2 = 6, x_1 x_2 = -3$.\n"
         "Quy đồng: $S = \\frac{x_1(x_1^2 - 1) + x_2(x_2^2 - 1)}{x_1 x_2} = \\frac{(x_1^3 + x_2^3) - (x_1 + x_2)}{x_1 x_2}$.\n"
         "Ta có $x_1^3 + x_2^3 = 6^3 - 3(-3)(6) = 216 + 54 = 270$.\n"
         "Suy ra $S = \\frac{270 - 6}{-3} = \\frac{264}{-3} = -88$.\n"
         "Vậy $S = -88$."),

        (16, "4x^2 - 10x + 1 = 0", "T = \\frac{2x_1 - 1}{x_2} + \\frac{2x_2 - 1}{x_1}",
         "$\\Delta' = 25 - 4 = 21 > 0$. Theo Vi-ét: $x_1 + x_2 = \\frac{5}{2}, x_1 x_2 = \\frac{1}{4}$.\n"
         "Quy đồng: $T = \\frac{2(x_1^2 + x_2^2) - (x_1 + x_2)}{x_1 x_2}$.\n"
         "Ta có $x_1^2 + x_2^2 = \\left(\\frac{5}{2}\\right)^2 - 2\\left(\\frac{1}{4}\\right) = \\frac{25}{4} - \\frac{2}{4} = \\frac{23}{4}$.\n"
         "Tử thức $= 2\\left(\\frac{23}{4}\\right) - \\frac{5}{2} = \\frac{23}{2} - \\frac{5}{2} = \\frac{18}{2} = 9$.\n"
         "Suy ra $T = \\frac{9}{1/4} = 36$.\n"
         "Vậy $T = 36$."),

        (17, "x^2 - 4x + 2 = 0", "U = \\frac{x_1}{x_2 - 1} + \\frac{x_2}{x_1 - 1}",
         "$\\Delta' = 4 - 2 = 2 > 0$. Theo Vi-ét: $x_1 + x_2 = 4, x_1 x_2 = 2$.\n"
         "Quy đồng: $U = \\frac{x_1(x_1 - 1) + x_2(x_2 - 1)}{(x_1 - 1)(x_2 - 1)} = \\frac{(x_1^2 + x_2^2) - (x_1 + x_2)}{x_1 x_2 - (x_1 + x_2) + 1}$.\n"
         "Ta có $x_1^2 + x_2^2 = 4^2 - 2(2) = 12$.\n"
         "Tử thức $= 12 - 4 = 8$.\n"
         "Mẫu thức $= 2 - 4 + 1 = -1$.\n"
         "Suy ra $U = \\frac{8}{-1} = -8$.\n"
         "Vậy $U = -8$."),

        (18, "x^2 - 7x + 2 = 0", "V = \\frac{1}{x_1 - 2} + \\frac{1}{x_2 - 2}",
         "$\\Delta = 49 - 8 = 41 > 0$. Theo Vi-ét: $x_1 + x_2 = 7, x_1 x_2 = 2$.\n"
         "Quy đồng: $V = \\frac{x_1 + x_2 - 4}{x_1 x_2 - 2(x_1 + x_2) + 4}$.\n"
         "Thay số: $V = \\frac{7 - 4}{2 - 2(7) + 4} = \\frac{3}{2 - 14 + 4} = \\frac{3}{-8} = -\\frac{3}{8}$.\n"
         "Vậy $V = -\\frac{3}{8}$."),

        (19, "2x^2 - 6x + 3 = 0", "W = \\frac{x_1^2}{x_2^2} + \\frac{x_2^2}{x_1^2}",
         "$\\Delta' = 9 - 6 = 3 > 0$. Theo Vi-ét: $x_1 + x_2 = 3, x_1 x_2 = \\frac{3}{2}$.\n"
         "Ta có $\\frac{x_1}{x_2} + \\frac{x_2}{x_1} = \\frac{(x_1+x_2)^2 - 2x_1x_2}{x_1x_2} = \\frac{3^2 - 2(3/2)}{3/2} = \\frac{6}{3/2} = 4$.\n"
         "Khi đó: $W = \\left(\\frac{x_1}{x_2} + \\frac{x_2}{x_1}\\right)^2 - 2 = 4^2 - 2 = 14$.\n"
         "Vậy $W = 14$."),

        (20, "x^2 - 5x - 4 = 0", "Y = \\frac{x_1 - 3}{x_2} + \\frac{x_2 - 3}{x_1}",
         "Vì $ac = -4 < 0$ nên PT có 2 nghiệm phân biệt trái dấu. Theo Vi-ét: $x_1 + x_2 = 5, x_1 x_2 = -4$.\n"
         "Quy đồng: $Y = \\frac{(x_1^2 + x_2^2) - 3(x_1 + x_2)}{x_1 x_2}$.\n"
         "Ta có $x_1^2 + x_2^2 = 5^2 - 2(-4) = 33$.\n"
         "Suy ra $Y = \\frac{33 - 3(5)}{-4} = \\frac{18}{-4} = -\\frac{9}{2}$.\n"
         "Vậy $Y = -\\frac{9}{2}$."),

        (21, "3x^2 - 5x + 1 = 0", "A_1 = \\frac{1}{x_1 + 1} + \\frac{1}{x_2 + 1}",
         "$\\Delta = 25 - 12 = 13 > 0$. Theo Vi-ét: $x_1 + x_2 = \\frac{5}{3}, x_1 x_2 = \\frac{1}{3}$.\n"
         "Quy đồng: $A_1 = \\frac{x_1 + x_2 + 2}{x_1 x_2 + x_1 + x_2 + 1} = \\frac{\\frac{5}{3} + 2}{\\frac{1}{3} + \\frac{5}{3} + 1} = \\frac{11/3}{3} = \\frac{11}{9}$.\n"
         "Vậy $A_1 = \\frac{11}{9}$."),

        (22, "x^2 - 6x + 7 = 0", "B_1 = \\frac{x_1 - 2}{x_2 + 1} + \\frac{x_2 - 2}{x_1 + 1}",
         "$\\Delta' = 9 - 7 = 2 > 0$. Theo Vi-ét: $x_1 + x_2 = 6, x_1 x_2 = 7$.\n"
         "Quy đồng:\n"
         "Tử $= (x_1 - 2)(x_1 + 1) + (x_2 - 2)(x_2 + 1) = (x_1^2 - x_1 - 2) + (x_2^2 - x_2 - 2) = (x_1^2 + x_2^2) - (x_1 + x_2) - 4$.\n"
         "Ta có $x_1^2 + x_2^2 = 6^2 - 2(7) = 22$. Do đó Tử $= 22 - 6 - 4 = 12$.\n"
         "Mẫu $= x_1 x_2 + x_1 + x_2 + 1 = 7 + 6 + 1 = 14$.\n"
         "Suy ra $B_1 = \\frac{12}{14} = \\frac{6}{7}$.\n"
         "Vậy $B_1 = \\frac{6}{7}$."),

        (23, "x^2 - 3x + 1 = 0", "C_1 = \\frac{x_1 + x_2}{x_1^2 + x_2^2}",
         "$\\Delta = 9 - 4 = 5 > 0$. Theo Vi-ét: $x_1 + x_2 = 3, x_1 x_2 = 1$.\n"
         "Ta có $x_1^2 + x_2^2 = 3^2 - 2(1) = 7$.\n"
         "Suy ra $C_1 = \\frac{3}{7}$.\n"
         "Vậy $C_1 = \\frac{3}{7}$."),

        (24, "2x^2 - 7x + 1 = 0", "D_1 = \\frac{x_1^2 + x_2^2}{x_1^3 + x_2^3}",
         "$\\Delta = 49 - 8 = 41 > 0$. Theo Vi-ét: $x_1 + x_2 = \\frac{7}{2}, x_1 x_2 = \\frac{1}{2}$.\n"
         "Tử $= \\left(\\frac{7}{2}\\right)^2 - 2\\left(\\frac{1}{2}\\right) = \\frac{49}{4} - 1 = \\frac{45}{4}$.\n"
         "Mẫu $= \\left(\\frac{7}{2}\\right)^3 - 3\\left(\\frac{1}{2}\\right)\\left(\\frac{7}{2}\\right) = \\frac{343}{8} - \\frac{21}{4} = \\frac{301}{8}$.\n"
         "Suy ra $D_1 = \\frac{45/4}{301/8} = \\frac{90}{301}$.\n"
         "Vậy $D_1 = \\frac{90}{301}$."),

        (25, "x^2 - 8x + 5 = 0", "E_1 = \\frac{x_1 - 1}{x_2 - 1} + \\frac{x_2 - 1}{x_1 - 1}",
         "$\\Delta' = 16 - 5 = 11 > 0$. Theo Vi-ét: $x_1 + x_2 = 8, x_1 x_2 = 5$.\n"
         "Quy đồng:\n"
         "Tử $= (x_1 - 1)^2 + (x_2 - 1)^2 = (x_1^2 + x_2^2) - 2(x_1 + x_2) + 2$.\n"
         "Ta có $x_1^2 + x_2^2 = 8^2 - 2(5) = 54$. Tử $= 54 - 2(8) + 2 = 40$.\n"
         "Mẫu $= x_1 x_2 - (x_1 + x_2) + 1 = 5 - 8 + 1 = -2$.\n"
         "Suy ra $E_1 = \\frac{40}{-2} = -20$.\n"
         "Vậy $E_1 = -20$."),

        (26, "x^2 - 5x - 2 = 0", "F_1 = \\frac{x_1 + 3}{x_2} + \\frac{x_2 + 3}{x_1}",
         "Vì $ac = -2 < 0$ nên PT có 2 nghiệm phân biệt trái dấu. Theo Vi-ét: $x_1 + x_2 = 5, x_1 x_2 = -2$.\n"
         "Quy đồng: $F_1 = \\frac{(x_1^2 + x_2^2) + 3(x_1 + x_2)}{x_1 x_2}$.\n"
         "Ta có $x_1^2 + x_2^2 = 5^2 - 2(-2) = 29$.\n"
         "Suy ra $F_1 = \\frac{29 + 3(5)}{-2} = \\frac{44}{-2} = -22$.\n"
         "Vậy $F_1 = -22$."),

        (27, "x^2 - 6x + 1 = 0", "G_1 = \\frac{1}{x_1^2 - 1} + \\frac{1}{x_2^2 - 1}",
         "$\\Delta' = 9 - 1 = 8 > 0$. Theo Vi-ét: $x_1 + x_2 = 6, x_1 x_2 = 1$.\n"
         "Quy đồng: $G_1 = \\frac{x_1^2 + x_2^2 - 2}{(x_1 x_2)^2 - (x_1^2 + x_2^2) + 1}$.\n"
         "Ta có $x_1^2 + x_2^2 = 6^2 - 2(1) = 34$.\n"
         "Tử $= 34 - 2 = 32$.\n"
         "Mẫu $= 1^2 - 34 + 1 = -32$.\n"
         "Suy ra $G_1 = \\frac{32}{-32} = -1$.\n"
         "Vậy $G_1 = -1$."),

        (28, "3x^2 - 11x + 2 = 0", "H_1 = \\frac{x_1}{2x_2 + 1} + \\frac{x_2}{2x_1 + 1}",
         "$\\Delta = 121 - 24 = 97 > 0$. Theo Vi-ét: $x_1 + x_2 = \\frac{11}{3}, x_1 x_2 = \\frac{2}{3}$.\n"
         "Quy đồng:\n"
         "Tử $= 2(x_1^2 + x_2^2) + (x_1 + x_2) = 2\\left[\\left(\\frac{11}{3}\\right)^2 - 2\\left(\\frac{2}{3}\\right)\\right] + \\frac{11}{3} = 2\\left(\\frac{109}{9}\\right) + \\frac{33}{9} = \\frac{251}{9}$.\n"
         "Mẫu $= 4x_1 x_2 + 2(x_1 + x_2) + 1 = 4\\left(\\frac{2}{3}\\right) + 2\\left(\\frac{11}{3}\\right) + 1 = \\frac{8 + 22 + 3}{3} = 11 = \\frac{99}{9}$.\n"
         "Suy ra $H_1 = \\frac{251}{99}$.\n"
         "Vậy $H_1 = \\frac{251}{99}$."),

        (29, "x^2 - 4x + 3 = 0", "K_1 = \\frac{x_1^2 + 2}{x_2} + \\frac{x_2^2 + 2}{x_1}",
         "Ta có $x_1 + x_2 = 4, x_1 x_2 = 3$.\n"
         "Quy đồng: $K_1 = \\frac{(x_1^3 + x_2^3) + 2(x_1 + x_2)}{x_1 x_2}$.\n"
         "Ta có $x_1^3 + x_2^3 = 4^3 - 3(3)(4) = 64 - 36 = 28$.\n"
         "Suy ra $K_1 = \\frac{28 + 2(4)}{3} = \\frac{36}{3} = 12$.\n"
         "Vậy $K_1 = 12$."),

        (30, "x^2 - 7x + 4 = 0", "M_1 = \\frac{x_1 - 3}{x_2 - 1} + \\frac{x_2 - 3}{x_1 - 1}",
         "$\\Delta = 49 - 16 = 33 > 0$. Theo Vi-ét: $x_1 + x_2 = 7, x_1 x_2 = 4$.\n"
         "Quy đồng:\n"
         "Tử $= (x_1 - 3)(x_1 - 1) + (x_2 - 3)(x_2 - 1) = (x_1^2 + x_2^2) - 4(x_1 + x_2) + 6$.\n"
         "Ta có $x_1^2 + x_2^2 = 7^2 - 2(4) = 41$. Tử $= 41 - 4(7) + 6 = 19$.\n"
         "Mẫu $= x_1 x_2 - (x_1 + x_2) + 1 = 4 - 7 + 1 = -2$.\n"
         "Suy ra $M_1 = -\\frac{19}{2}$.\n"
         "Vậy $M_1 = -\\frac{19}{2}$."),

        (31, "2x^2 - 5x - 3 = 0", "N_1 = \\frac{x_1^2}{x_2} + \\frac{x_2^2}{x_1}",
         "Vì $ac = -6 < 0$ nên PT có 2 nghiệm phân biệt trái dấu. Theo Vi-ét: $x_1 + x_2 = \\frac{5}{2}, x_1 x_2 = -\\frac{3}{2}$.\n"
         "Ta có $x_1^3 + x_2^3 = \\left(\\frac{5}{2}\\right)^3 - 3\\left(-\\frac{3}{2}\\right)\\left(\\frac{5}{2}\\right) = \\frac{125}{8} + \\frac{45}{4} = \\frac{215}{8}$.\n"
         "Suy ra $N_1 = \\frac{215/8}{-3/2} = -\\frac{215}{12}$.\n"
         "Vậy $N_1 = -\\frac{215}{12}$."),

        (32, "x^2 - 5x + 5 = 0", "P_1 = \\frac{x_1^2 + x_1 x_2}{x_2} + \\frac{x_2^2 + x_1 x_2}{x_1}",
         "$\\Delta = 25 - 20 = 5 > 0$. Theo Vi-ét: $x_1 + x_2 = 5, x_1 x_2 = 5$.\n"
         "Biến đổi: $\\frac{x_1(x_1 + x_2)}{x_2} + \\frac{x_2(x_1 + x_2)}{x_1} = (x_1 + x_2)\\left(\\frac{x_1}{x_2} + \\frac{x_2}{x_1}\\right)$.\n"
         "Ta có $\\frac{x_1}{x_2} + \\frac{x_2}{x_1} = \\frac{5^2 - 2(5)}{5} = \\frac{15}{5} = 3$.\n"
         "Suy ra $P_1 = 5 \\times 3 = 15$.\n"
         "Vậy $P_1 = 15$."),

        (33, "x^2 - 9x + 2 = 0", "Q_1 = \\frac{1}{x_1 + 3} + \\frac{1}{x_2 + 3}",
         "$\\Delta = 81 - 8 = 73 > 0$. Theo Vi-ét: $x_1 + x_2 = 9, x_1 x_2 = 2$.\n"
         "Quy đồng: $Q_1 = \\frac{x_1 + x_2 + 6}{x_1 x_2 + 3(x_1 + x_2) + 9} = \\frac{9 + 6}{2 + 3(9) + 9} = \\frac{15}{38}$.\n"
         "Vậy $Q_1 = \\frac{15}{38}$."),

        (34, "x^2 - 6x + 3 = 0", "R_1 = \\frac{x_1^2}{x_2 + 1} + \\frac{x_2^2}{x_1 + 1}",
         "$\\Delta' = 9 - 3 = 6 > 0$. Theo Vi-ét: $x_1 + x_2 = 6, x_1 x_2 = 3$.\n"
         "Quy đồng:\n"
         "Tử $= x_1^2(x_1 + 1) + x_2^2(x_2 + 1) = (x_1^3 + x_2^3) + (x_1^2 + x_2^2)$.\n"
         "Ta có $x_1^2 + x_2^2 = 6^2 - 2(3) = 30$.\n"
         "$x_1^3 + x_2^3 = 6^3 - 3(3)(6) = 216 - 54 = 162$.\n"
         "Tử $= 162 + 30 = 192$.\n"
         "Mẫu $= x_1 x_2 + (x_1 + x_2) + 1 = 3 + 6 + 1 = 10$.\n"
         "Suy ra $R_1 = \\frac{192}{10} = \\frac{96}{5}$.\n"
         "Vậy $R_1 = \\frac{96}{5}$."),

        (35, "2x^2 - 8x + 1 = 0", "S_1 = \\frac{1}{(x_1 - 1)^2} + \\frac{1}{(x_2 - 1)^2}",
         "$\\Delta' = 16 - 2 = 14 > 0$. Theo Vi-ét: $x_1 + x_2 = 4, x_1 x_2 = \\frac{1}{2}$.\n"
         "Đặt $y_1 = x_1 - 1, y_2 = x_2 - 1$. Ta có $y_1 + y_2 = (x_1 + x_2) - 2 = 2$.\n"
         "$y_1 y_2 = x_1 x_2 - (x_1 + x_2) + 1 = \\frac{1}{2} - 4 + 1 = -\\frac{5}{2}$.\n"
         "Suy ra $S_1 = \\frac{y_1^2 + y_2^2}{(y_1 y_2)^2} = \\frac{(y_1 + y_2)^2 - 2y_1 y_2}{(y_1 y_2)^2} = \\frac{2^2 - 2(-5/2)}{(-5/2)^2} = \\frac{4 + 5}{25/4} = \\frac{9}{25/4} = \\frac{36}{25}$.\n"
         "Vậy $S_1 = \\frac{36}{25}$."),

        (36, "x^2 - 5x - 1 = 0", "T_1 = \\frac{x_1^3 + 1}{x_2} + \\frac{x_2^3 + 1}{x_1}",
         "Vì $ac = -1 < 0$ nên PT có 2 nghiệm phân biệt trái dấu. Theo Vi-ét: $x_1 + x_2 = 5, x_1 x_2 = -1$.\n"
         "Quy đồng: $T_1 = \\frac{(x_1^4 + x_2^4) + (x_1 + x_2)}{x_1 x_2}$.\n"
         "Ta có $x_1^2 + x_2^2 = 5^2 - 2(-1) = 27$.\n"
         "$x_1^4 + x_2^4 = (x_1^2 + x_2^2)^2 - 2(x_1 x_2)^2 = 27^2 - 2(-1)^2 = 729 - 2 = 727$.\n"
         "Suy ra $T_1 = \\frac{727 + 5}{-1} = -732$.\n"
         "Vậy $T_1 = -732$."),

        (37, "3x^2 - 6x + 2 = 0", "U_1 = \\frac{x_1}{x_2} + \\frac{x_2}{x_1} + \\frac{1}{x_1 x_2}",
         "$\\Delta' = 9 - 6 = 3 > 0$. Theo Vi-ét: $x_1 + x_2 = 2, x_1 x_2 = \\frac{2}{3}$.\n"
         "Ta có $\\frac{x_1^2 + x_2^2 + 1}{x_1 x_2} = \\frac{(x_1+x_2)^2 - 2x_1x_2 + 1}{x_1 x_2} = \\frac{2^2 - 2(2/3) + 1}{2/3} = \\frac{4 - 4/3 + 1}{2/3} = \\frac{11/3}{2/3} = \\frac{11}{2}$.\n"
         "Vậy $U_1 = \\frac{11}{2}$."),

        (38, "x^2 - 4x + 1 = 0", "V_1 = \\frac{x_1 - 1}{x_1 + 1} + \\frac{x_2 - 1}{x_2 + 1}",
         "$\\Delta' = 4 - 1 = 3 > 0$. Theo Vi-ét: $x_1 + x_2 = 4, x_1 x_2 = 1$.\n"
         "Quy đồng:\n"
         "Tử $= (x_1 - 1)(x_2 + 1) + (x_2 - 1)(x_1 + 1) = (x_1 x_2 + x_1 - x_2 - 1) + (x_1 x_2 + x_2 - x_1 - 1) = 2x_1 x_2 - 2$.\n"
         "Thay $x_1 x_2 = 1 \\Rightarrow$ Tử $= 2(1) - 2 = 0$.\n"
         "Mẫu $= x_1 x_2 + (x_1 + x_2) + 1 = 1 + 4 + 1 = 6 \\ne 0$.\n"
         "Suy ra $V_1 = \\frac{0}{6} = 0$.\n"
         "Vậy $V_1 = 0$."),

        (39, "x^2 - 7x + 6 = 0", "W_1 = \\frac{x_1^2 + x_2^2 + 2}{x_1 + x_2}",
         "Phương trình có $x_1 + x_2 = 7, x_1 x_2 = 6$.\n"
         "Ta có $x_1^2 + x_2^2 = 7^2 - 2(6) = 37$.\n"
         "Suy ra $W_1 = \\frac{37 + 2}{7} = \\frac{39}{7}$.\n"
         "Vậy $W_1 = \\frac{39}{7}$."),

        (40, "2x^2 - 4x - 1 = 0", "Z_1 = \\frac{x_1^2 - 2}{x_2} + \\frac{x_2^2 - 2}{x_1}",
         "Vì $ac = -2 < 0$ nên PT có 2 nghiệm phân biệt trái dấu. Theo Vi-ét: $x_1 + x_2 = 2, x_1 x_2 = -\\frac{1}{2}$.\n"
         "Quy đồng: $Z_1 = \\frac{(x_1^3 + x_2^3) - 2(x_1 + x_2)}{x_1 x_2}$.\n"
         "Ta có $x_1^3 + x_2^3 = 2^3 - 3(-1/2)(2) = 8 + 3 = 11$.\n"
         "Suy ra $Z_1 = \\frac{11 - 2(2)}{-1/2} = \\frac{7}{-1/2} = -14$.\n"
         "Vậy $Z_1 = -14$.")
    ]

    for item in frac_data:
        questions.append({
            "id": item[0],
            "type": "essay",
            "level": "VD",
            "topicId": "cd3",
            "topicTitle": "CĐ 3: HỆ THỨC VI-ÉT",
            "question": f"**Câu {item[0]}:** Không giải phương trình bậc hai, hãy tính giá trị của biểu thức phân thức sau liên quan đến hai nghiệm $x_1, x_2$ của phương trình ${item[1]}$:\n$${item[2]}$$",
            "solution": f"**Lời giải chi tiết:**\n\n{item[3]}"
        })

    # =========================================================================
    # 10 BÀI BIỂU THỨC KHÔNG ĐỐI XỨNG GIỮA x1 VÀ x2 (CÂU 41 - 50)
    # Phương pháp: Hạ bậc nghiệm từ phương trình gốc
    # =========================================================================
    asym_data = [
        (41, "x^2 - 3x + 1 = 0", "M = x_1^2 + 3x_2",
         "Ta có $\\Delta = (-3)^2 - 4(1)(1) = 5 > 0$ nên phương trình có hai nghiệm phân biệt $x_1, x_2$.\n"
         "Theo định lí Vi-ét, ta có:\n"
         "$$\\begin{cases} x_1 + x_2 = 3 \\\\ x_1 x_2 = 1 \\end{cases}$$\n\n"
         "**Phương pháp hạ bậc nghiệm:**\n"
         "Vì $x_1$ là một nghiệm của phương trình $x^2 - 3x + 1 = 0$ nên ta có:\n"
         "$$x_1^2 - 3x_1 + 1 = 0 \\Leftrightarrow x_1^2 = 3x_1 - 1$$\n\n"
         "Thế vào biểu thức $M$ ta được:\n"
         "$$M = (3x_1 - 1) + 3x_2 = 3(x_1 + x_2) - 1$$\n"
         "Thay $x_1 + x_2 = 3$ vào ta có:\n"
         "$$M = 3(3) - 1 = 9 - 1 = 8$$\n"
         "Vậy giá trị của biểu thức $M$ là $8$."),

        (42, "x^2 - 5x + 2 = 0", "N = x_1^2 + 5x_2 - 2x_1 x_2",
         "Ta có $\\Delta = 25 - 8 = 17 > 0$. Phương trình có 2 nghiệm phân biệt.\n"
         "Theo định lí Vi-ét:\n"
         "$$\\begin{cases} x_1 + x_2 = 5 \\\\ x_1 x_2 = 2 \\end{cases}$$\n\n"
         "Vì $x_1$ là nghiệm của phương trình nên:\n"
         "$$x_1^2 - 5x_1 + 2 = 0 \\Leftrightarrow x_1^2 = 5x_1 - 2$$\n\n"
         "Thế vào biểu thức $N$ ta có:\n"
         "$$N = (5x_1 - 2) + 5x_2 - 2x_1 x_2 = 5(x_1 + x_2) - 2 - 2x_1 x_2$$\n"
         "Thay các giá trị theo Vi-ét vào:\n"
         "$$N = 5(5) - 2 - 2(2) = 25 - 2 - 4 = 19$$\n"
         "Vậy $N = 19$."),

        (43, "2x^2 - 6x + 1 = 0", "P = 2x_1^2 + 6x_2 + 4x_1 x_2",
         "Ta có $\\Delta' = (-3)^2 - 2(1) = 7 > 0$. Theo định lí Vi-ét:\n"
         "$$\\begin{cases} x_1 + x_2 = 3 \\\\ x_1 x_2 = \\frac{1}{2} \\end{cases}$$\n\n"
         "Vì $x_1$ là nghiệm của phương trình nên $2x_1^2 - 6x_1 + 1 = 0 \\Leftrightarrow 2x_1^2 = 6x_1 - 1$.\n\n"
         "Thay vào biểu thức $P$:\n"
         "$$P = (6x_1 - 1) + 6x_2 + 4x_1 x_2 = 6(x_1 + x_2) - 1 + 4x_1 x_2$$\n"
         "$$P = 6(3) - 1 + 4\\left(\\frac{1}{2}\\right) = 18 - 1 + 2 = 19$$\n"
         "Vậy $P = 19$."),

        (44, "x^2 - 4x + 1 = 0", "Q = x_1^2 + 4x_2 + 3x_1 x_2",
         "Ta có $\\Delta' = 4 - 1 = 3 > 0$. Theo định lí Vi-ét: $x_1 + x_2 = 4, x_1 x_2 = 1$.\n\n"
         "Vì $x_1$ là nghiệm của phương trình nên:\n"
         "$$x_1^2 - 4x_1 + 1 = 0 \\Leftrightarrow x_1^2 = 4x_1 - 1$$\n\n"
         "Thế vào $Q$:\n"
         "$$Q = (4x_1 - 1) + 4x_2 + 3x_1 x_2 = 4(x_1 + x_2) - 1 + 3x_1 x_2 = 4(4) - 1 + 3(1) = 16 - 1 + 3 = 18$$\n"
         "Vậy $Q = 18$."),

        (45, "x^2 - 7x + 3 = 0", "K = x_1^2 + 7x_2 + 2x_1 x_2",
         "Ta có $\\Delta = 49 - 12 = 37 > 0$. Theo Vi-ét: $x_1 + x_2 = 7, x_1 x_2 = 3$.\n\n"
         "Do $x_1$ là nghiệm của phương trình nên $x_1^2 = 7x_1 - 3$.\n\n"
         "Thay vào biểu thức $K$:\n"
         "$$K = (7x_1 - 3) + 7x_2 + 2x_1 x_2 = 7(x_1 + x_2) - 3 + 2x_1 x_2$$\n"
         "$$K = 7(7) - 3 + 2(3) = 49 - 3 + 6 = 52$$\n"
         "Vậy $K = 52$."),

        (46, "3x^2 - 8x - 2 = 0", "H = 3x_1^2 + 8x_2 - 6x_1 x_2",
         "Vì $ac = 3(-2) = -6 < 0$ nên PT có 2 nghiệm phân biệt trái dấu. Theo Vi-ét: $x_1 + x_2 = \\frac{8}{3}, x_1 x_2 = -\\frac{2}{3}$.\n\n"
         "Vì $x_1$ là nghiệm nên $3x_1^2 - 8x_1 - 2 = 0 \\Leftrightarrow 3x_1^2 = 8x_1 + 2$.\n\n"
         "Thế vào $H$:\n"
         "$$H = (8x_1 + 2) + 8x_2 - 6x_1 x_2 = 8(x_1 + x_2) + 2 - 6x_1 x_2$$\n"
         "$$H = 8\\left(\\frac{8}{3}\\right) + 2 - 6\\left(-\\frac{2}{3}\\right) = \\frac{64}{3} + 2 + 4 = \\frac{64}{3} + 6 = \\frac{82}{3}$$\n"
         "Vậy $H = \\frac{82}{3}$."),

        (47, "x^2 - 6x + 4 = 0", "T = x_1(x_1 - 2) + 4x_2",
         "Ta có $\\Delta' = 9 - 4 = 5 > 0$. Theo Vi-ét: $x_1 + x_2 = 6, x_1 x_2 = 4$.\n\n"
         "Khai triển: $T = x_1^2 - 2x_1 + 4x_2$.\n"
         "Vì $x_1$ là nghiệm nên $x_1^2 = 6x_1 - 4$.\n"
         "Suy ra $x_1^2 - 2x_1 = 6x_1 - 4 - 2x_1 = 4x_1 - 4$.\n\n"
         "Do đó:\n"
         "$$T = (4x_1 - 4) + 4x_2 = 4(x_1 + x_2) - 4 = 4(6) - 4 = 24 - 4 = 20$$\n"
         "Vậy $T = 20$."),

        (48, "x^2 - 2x - 5 = 0", "V = x_1^2 + 2x_2 + (x_1 - x_2)^2",
         "Vì $ac = -5 < 0$ nên PT luôn có 2 nghiệm phân biệt. Theo Vi-ét: $x_1 + x_2 = 2, x_1 x_2 = -5$.\n\n"
         "Vì $x_1$ là nghiệm nên $x_1^2 = 2x_1 + 5$.\n"
         "Do đó $x_1^2 + 2x_2 = (2x_1 + 5) + 2x_2 = 2(x_1 + x_2) + 5 = 2(2) + 5 = 9$.\n\n"
         "Mặt khác: $(x_1 - x_2)^2 = (x_1 + x_2)^2 - 4x_1 x_2 = 2^2 - 4(-5) = 4 + 20 = 24$.\n"
         "Suy ra:\n"
         "$$V = 9 + 24 = 33$$\n"
         "Vậy $V = 33$."),

        (49, "2x^2 - 5x + 1 = 0", "U = 2x_1^2 + 5x_2 + 6x_1 x_2",
         "Ta có $\\Delta = 25 - 8 = 17 > 0$. Theo Vi-ét: $x_1 + x_2 = \\frac{5}{2}, x_1 x_2 = \\frac{1}{2}$.\n\n"
         "Vì $x_1$ là nghiệm nên $2x_1^2 - 5x_1 + 1 = 0 \\Leftrightarrow 2x_1^2 = 5x_1 - 1$.\n\n"
         "Thế vào $U$:\n"
         "$$U = (5x_1 - 1) + 5x_2 + 6x_1 x_2 = 5(x_1 + x_2) - 1 + 6x_1 x_2$$\n"
         "$$U = 5\\left(\\frac{5}{2}\\right) - 1 + 6\\left(\\frac{1}{2}\\right) = \\frac{25}{2} - 1 + 3 = \\frac{25}{2} + 2 = \\frac{29}{2}$$\n"
         "Vậy $U = \\frac{29}{2}$."),

        (50, "x^2 - 5x + 1 = 0", "W = x_1^3 - 5x_1^2 + 2x_1 + x_2",
         "Ta có $\\Delta = 25 - 4 = 21 > 0$. Phương trình có 2 nghiệm phân biệt.\n"
         "Theo định lí Vi-ét: $x_1 + x_2 = 5, x_1 x_2 = 1$.\n\n"
         "Vì $x_1$ là nghiệm của phương trình $x^2 - 5x + 1 = 0$ nên ta có:\n"
         "$$x_1^2 - 5x_1 + 1 = 0$$\n"
         "Nhân cả hai vế với $x_1$:\n"
         "$$x_1(x_1^2 - 5x_1 + 1) = 0 \\Leftrightarrow x_1^3 - 5x_1^2 + x_1 = 0$$\n\n"
         "Tách biểu thức $W$:\n"
         "$$W = (x_1^3 - 5x_1^2 + x_1) + x_1 + x_2 = 0 + (x_1 + x_2)$$\n"
         "Thay $x_1 + x_2 = 5$ vào ta được:\n"
         "$$W = 5$$\n"
         "Vậy $W = 5$.")
    ]

    for item in asym_data:
        questions.append({
            "id": item[0],
            "type": "essay",
            "level": "VDC",
            "topicId": "cd3",
            "topicTitle": "CĐ 3: HỆ THỨC VI-ÉT",
            "question": f"**Câu {item[0]}:** Cho phương trình bậc hai ${item[1]}$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức không đối xứng sau bằng phương pháp hạ bậc nghiệm:\n$${item[2]}$$",
            "solution": item[3]
        })

    return questions

if __name__ == "__main__":
    qs = get_cd3_questions()
    print(f"Total CD3 questions built: {len(qs)}")
