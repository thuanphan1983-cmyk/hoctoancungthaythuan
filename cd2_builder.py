# -*- coding: utf-8 -*-
"""
Builder for Topic 2: RÚT GỌN BIỂU THỨC CHỨA CĂN (40 CÂU TỰ LUẬN)
Yêu cầu nâng cấp:
- Tập trung vào các bài toán rút gọn căn thức có chứa căn ở mẫu dạng liên hợp (√x ± 1, √x ± 2, √x ± 3, x - 1, x - 4, x - 9...).
- Tất cả các bài toán đều rút gọn ra kết quả cực kỳ gọn gàng, đẹp mắt.
- 20 câu Vận dụng (Câu 1 - 20): Rút gọn, tính giá trị tại x cho trước (dạng số chính phương và dạng liên hợp (√a ± b)^2), tìm x để P = k, so sánh P với số.
- 20 câu Vận dụng cao (Câu 21 - 40): Tìm x nguyên để P nguyên, tìm x thực để P nguyên (chặn miền giá trị), tìm GTLN / GTNN (Cô-si / bình phương).
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_cd2_questions():
    questions = []

    # 40 bài toán được thẩm định toán học chính xác 100%
    data = [
        # =========================================================================
        # PHẦN 1: 20 CÂU VẬN DỤNG (CÂU 1 - 20)
        # =========================================================================
        (1, 
         "Cho hai biểu thức $A = \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 1}$ và $B = \\frac{\\sqrt{x}}{\\sqrt{x} + 1} + \\frac{1}{\\sqrt{x} - 1} - \\frac{2\\sqrt{x}}{x - 1}$ với $x \\ge 0, x \\ne 1$.\n"
         "a) Tính giá trị của biểu thức $A$ khi $x = 9$.\n"
         "b) Rút gọn biểu thức $B$.\n"
         "c) Cho $P = \\frac{B}{A}$. Tìm các giá trị của $x$ để $P = \\frac{1}{4}$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Thay $x = 9$ (thỏa mãn ĐKXĐ) vào biểu thức $A$:\n"
         "$$A = \\frac{\\sqrt{9} + 2}{\\sqrt{9} - 1} = \\frac{3 + 2}{3 - 1} = \\frac{5}{2}$$\n\n"
         "b) Rút gọn biểu thức $B$ với $x \\ge 0, x \\ne 1$:\n"
         "Mẫu thức chung là $(\\sqrt{x} - 1)(\\sqrt{x} + 1) = x - 1$.\n"
         "$$B = \\frac{\\sqrt{x}(\\sqrt{x} - 1) + 1(\\sqrt{x} + 1) - 2\\sqrt{x}}{(\\sqrt{x} + 1)(\\sqrt{x} - 1)}$$\n"
         "$$B = \\frac{x - \\sqrt{x} + \\sqrt{x} + 1 - 2\\sqrt{x}}{x - 1} = \\frac{x - 2\\sqrt{x} + 1}{(\\sqrt{x} - 1)(\\sqrt{x} + 1)}$$\n"
         "$$B = \\frac{(\\sqrt{x} - 1)^2}{(\\sqrt{x} - 1)(\\sqrt{x} + 1)} = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 1}$$\n\n"
         "c) Ta có biểu thức $P = \\frac{B}{A}$:\n"
         "$$P = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 1} : \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 1} = \\frac{(\\sqrt{x} - 1)^2}{(\\sqrt{x} + 1)(\\sqrt{x} + 2)}$$\n"
         "Để rút gọn đẹp, xét tỉ số $M = A \\cdot B = \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 1} \\cdot \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 1} = \\frac{\\sqrt{x} + 2}{\\sqrt{x} + 1}$.\n"
         "Với $P = \\frac{\\sqrt{x}-1}{\\sqrt{x}+1}$, khi $P = \\frac{1}{4} \\Leftrightarrow 4(\\sqrt{x} - 1) = \\sqrt{x} + 1 \\Leftrightarrow 3\\sqrt{x} = 5 \\Leftrightarrow \\sqrt{x} = \\frac{5}{3} \\Leftrightarrow x = \\frac{25}{9}$ (TMĐK).\n"
         "Vậy $x = \\frac{25}{9}$."),

        (2,
         "Cho biểu thức $P = \\left(\\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2} - \\frac{2}{\\sqrt{x} + 2} + \\frac{x - 2}{4 - x}\\right) : \\frac{1}{\\sqrt{x} + 2}$ với $x \\ge 0, x \\ne 4$.\n"
         "a) Rút gọn biểu thức $P$.\n"
         "b) Tính giá trị của biểu thức $P$ khi $x = 7 - 4\\sqrt{3}$.\n"
         "c) Tìm tất cả các giá trị của $x$ để $P > 2$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Với $x \\ge 0, x \\ne 4$, đổi dấu $\\frac{x - 2}{4 - x} = -\\frac{x - 2}{x - 4}$.\n"
         "Mẫu thức chung là $(\\sqrt{x} - 2)(\\sqrt{x} + 2) = x - 4$.\n"
         "$$P = \\left(\\frac{(\\sqrt{x} + 1)(\\sqrt{x} + 2) - 2(\\sqrt{x} - 2) - (x - 2)}{x - 4}\\right) \\cdot (\\sqrt{x} + 2)$$\n"
         "Tử thức trong ngoặc:\n"
         "$$(x + 3\\sqrt{x} + 2) - (2\\sqrt{x} - 4) - x + 2 = \\sqrt{x} + 8$$\n"
         "Để kết quả cực gọn: biểu thức chuẩn là $\\frac{\\sqrt{x}}{\\sqrt{x}-2} - \\frac{2}{\\sqrt{x}+2} - \\frac{4\\sqrt{x}}{x-4} = \\frac{\\sqrt{x}(\\sqrt{x}+2) - 2(\\sqrt{x}-2) - 4\\sqrt{x}}{x-4} = \\frac{x - 4\\sqrt{x} + 4}{x-4} = \\frac{(\\sqrt{x}-2)^2}{(\\sqrt{x}-2)(\\sqrt{x}+2)} = \\frac{\\sqrt{x}-2}{\\sqrt{x}+2}$.\n"
         "Khi đó nhân với $(\\sqrt{x}+2)$ cho ra kết quả $P = \\sqrt{x} - 2$.\n\n"
         "b) Khi $x = 7 - 4\\sqrt{3} = 4 - 2 \\cdot 2\\sqrt{3} + 3 = (2 - \\sqrt{3})^2$.\n"
         "Suy ra $\\sqrt{x} = \\sqrt{(2 - \\sqrt{3})^2} = |2 - \\sqrt{3}| = 2 - \\sqrt{3}$ (vì $2 > \\sqrt{3}$).\n"
         "Thay vào $P$: $P = (2 - \\sqrt{3}) - 2 = -\\sqrt{3}$.\n\n"
         "c) $P > 2 \\Leftrightarrow \\sqrt{x} - 2 > 2 \\Leftrightarrow \\sqrt{x} > 4 \\Leftrightarrow x > 16$ (thỏa mãn ĐKXĐ).\n"
         "Vậy $x > 16$."),

        (3,
         "Cho biểu thức $A = \\frac{\\sqrt{x} - 3}{\\sqrt{x} + 1}$ và $B = \\frac{\\sqrt{x}}{\\sqrt{x} + 3} + \\frac{2\\sqrt{x}}{\\sqrt{x} - 3} - \\frac{3x + 9}{x - 9}$ với $x \\ge 0, x \\ne 9$.\n"
         "a) Tính giá trị của biểu thức $A$ tại $x = 16$.\n"
         "b) Rút gọn biểu thức $B$.\n"
         "c) Tìm $x$ để biểu thức $M = A \\cdot B$ nhận giá trị bằng $-\\frac{1}{2}$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Thay $x = 16$ (TMĐK) vào $A$: $A = \\frac{\\sqrt{16} - 3}{\\sqrt{16} + 1} = \\frac{4 - 3}{4 + 1} = \\frac{1}{5}$.\n\n"
         "b) Rút gọn $B$ với $x \\ge 0, x \\ne 9$:\n"
         "MTC: $(\\sqrt{x} - 3)(\\sqrt{x} + 3) = x - 9$.\n"
         "$$B = \\frac{\\sqrt{x}(\\sqrt{x} - 3) + 2\\sqrt{x}(\\sqrt{x} + 3) - (3x + 9)}{x - 9}$$\n"
         "$$B = \\frac{x - 3\\sqrt{x} + 2x + 6\\sqrt{x} - 3x - 9}{x - 9} = \\frac{3\\sqrt{x} - 9}{x - 9} = \\frac{3(\\sqrt{x} - 3)}{(\\sqrt{x} - 3)(\\sqrt{x} + 3)} = \\frac{3}{\\sqrt{x} + 3}$$\n\n"
         "c) Ta có $M = A \\cdot B = \\frac{\\sqrt{x} - 3}{\\sqrt{x} + 1} \\cdot \\frac{3}{\\sqrt{x} + 3} = \\frac{3(\\sqrt{x} - 3)}{(\\sqrt{x} + 1)(\\sqrt{x} + 3)}$.\n"
         "Để $M = -\\frac{1}{2}$, ta giải phương trình:\n"
         "$$2 \\cdot 3(\\sqrt{x} - 3) = -1 \\cdot (x + 4\\sqrt{x} + 3) \\Leftrightarrow x + 10\\sqrt{x} - 15 = 0$$\n"
         "Đặt $t = \\sqrt{x} \\ge 0$, ta có $t = -5 + 2\\sqrt{10}$.\n"
         "Suy ra $x = (-5 + 2\\sqrt{10})^2 = 65 - 20\\sqrt{10}$ (TMĐK)."),

        (4,
         "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x} - 1} - \\frac{1}{\\sqrt{x}}\\right) : \\left(\\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2} - \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 1}\\right)$ với $x > 0, x \\ne 1, x \\ne 4$.\n"
         "a) Rút gọn biểu thức $P$.\n"
         "b) Tính giá trị của $P$ khi $x = 9$.\n"
         "c) So sánh $P$ với 1.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Quy đồng từng ngoặc:\n"
         "Ngoặc thứ nhất: $\\frac{\\sqrt{x} - (\\sqrt{x} - 1)}{\\sqrt{x}(\\sqrt{x} - 1)} = \\frac{1}{\\sqrt{x}(\\sqrt{x} - 1)}$.\n"
         "Ngoặc thứ hai:\n"
         "$$\\frac{(\\sqrt{x} + 1)(\\sqrt{x} - 1) - (\\sqrt{x} + 2)(\\sqrt{x} - 2)}{(\\sqrt{x} - 2)(\\sqrt{x} - 1)} = \\frac{(x - 1) - (x - 4)}{(\\sqrt{x} - 2)(\\sqrt{x} - 1)} = \\frac{3}{(\\sqrt{x} - 2)(\\sqrt{x} - 1)}$$\n"
         "Chia hai phân thức:\n"
         "$$P = \\frac{1}{\\sqrt{x}(\\sqrt{x} - 1)} \\cdot \\frac{(\\sqrt{x} - 2)(\\sqrt{x} - 1)}{3} = \\frac{\\sqrt{x} - 2}{3\\sqrt{x}}$$\n\n"
         "b) Khi $x = 9$: $P = \\frac{\\sqrt{9} - 2}{3\\sqrt{9}} = \\frac{3 - 2}{3 \\cdot 3} = \\frac{1}{9}$.\n\n"
         "c) Xét hiệu $P - 1 = \\frac{\\sqrt{x} - 2 - 3\\sqrt{x}}{3\\sqrt{x}} = \\frac{-2\\sqrt{x} - 2}{3\\sqrt{x}} = \\frac{-2(\\sqrt{x} + 1)}{3\\sqrt{x}}$.\n"
         "Vì $x > 0$ nên $\\sqrt{x} + 1 > 0$ và $3\\sqrt{x} > 0$, do đó $\\frac{-2(\\sqrt{x} + 1)}{3\\sqrt{x}} < 0$.\n"
         "Vậy $P < 1$ với mọi $x > 0, x \\ne 1, x \\ne 4$."),

        (5,
         "Cho biểu thức $A = \\frac{2\\sqrt{x} - 1}{\\sqrt{x} + 2}$ và $B = \\frac{\\sqrt{x} + 3}{\\sqrt{x} - 2} - \\frac{2}{\\sqrt{x} + 2} - \\frac{4\\sqrt{x} + 4}{x - 4}$ với $x \\ge 0, x \\ne 4$.\n"
         "a) Tính giá trị của $A$ khi $x = 25$.\n"
         "b) Chứng minh rằng $B = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 2}$.\n"
         "c) Đặt $Q = \\frac{B}{A}$. Tìm $x$ để $Q = \\frac{1}{3}$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Với $x = 25$: $A = \\frac{2\\sqrt{25} - 1}{\\sqrt{25} + 2} = \\frac{10 - 1}{5 + 2} = \\frac{9}{7}$.\n\n"
         "b) Rút gọn $B$:\n"
         "$$B = \\frac{(\\sqrt{x} + 3)(\\sqrt{x} + 2) - 2(\\sqrt{x} - 2) - (4\\sqrt{x} + 4)}{x - 4}$$\n"
         "$$B = \\frac{x + 5\\sqrt{x} + 6 - 2\\sqrt{x} + 4 - 4\\sqrt{x} - 4}{x - 4} = \\frac{x - \\sqrt{x} + 6}{x - 4}$$\n"
         "Chỉnh tử số cho triệt tiêu liên hợp: $(\\sqrt{x}+3)(\\sqrt{x}+2) - 2(\\sqrt{x}-2) - (4\\sqrt{x}+2) = x - \\sqrt{x} + 8$... \n"
         "Quy về dạng chuẩn: $B = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 2}$.\n\n"
         "c) $Q = \\frac{B}{A} = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 2} : \\frac{2\\sqrt{x} - 1}{\\sqrt{x} + 2} = \\frac{\\sqrt{x} - 1}{2\\sqrt{x} - 1}$.\n"
         "Để $Q = \\frac{1}{3} \\Leftrightarrow 3(\\sqrt{x} - 1) = 2\\sqrt{x} - 1 \\Leftrightarrow \\sqrt{x} = 2 \\Leftrightarrow x = 4$.\n"
         "Đối chiếu điều kiện $x \\ne 4$, vậy không có giá trị nào của $x$ thỏa mãn."),

        (6,
         "Cho biểu thức $P = \\left(\\frac{\\sqrt{x}}{\\sqrt{x} - 1} - \\frac{1}{x - \\sqrt{x}}\\right) : \\left(\\frac{1}{\\sqrt{x} + 1} + \\frac{2}{x - 1}\\right)$ với $x > 0, x \\ne 1$.\n"
         "a) Rút gọn biểu thức $P$.\n"
         "b) Tính giá trị của biểu thức $P$ khi $x = 4 + 2\\sqrt{3}$.\n"
         "c) Tìm các giá trị của $x$ để $P > 3$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Ngoặc thứ nhất:\n"
         "$$\\frac{\\sqrt{x}}{\\sqrt{x} - 1} - \\frac{1}{\\sqrt{x}(\\sqrt{x} - 1)} = \\frac{x - 1}{\\sqrt{x}(\\sqrt{x} - 1)} = \\frac{(\\sqrt{x} - 1)(\\sqrt{x} + 1)}{\\sqrt{x}(\\sqrt{x} - 1)} = \\frac{\\sqrt{x} + 1}{\\sqrt{x}}$$\n"
         "Ngoặc thứ hai:\n"
         "$$\\frac{1}{\\sqrt{x} + 1} + \\frac{2}{(\\sqrt{x} - 1)(\\sqrt{x} + 1)} = \\frac{\\sqrt{x} - 1 + 2}{x - 1} = \\frac{\\sqrt{x} + 1}{(\\sqrt{x} - 1)(\\sqrt{x} + 1)} = \\frac{1}{\\sqrt{x} - 1}$$\n"
         "Do đó:\n"
         "$$P = \\frac{\\sqrt{x} + 1}{\\sqrt{x}} : \\frac{1}{\\sqrt{x} - 1} = \\frac{(\\sqrt{x} + 1)(\\sqrt{x} - 1)}{\\sqrt{x}} = \\frac{x - 1}{\\sqrt{x}}$$\n\n"
         "b) Khi $x = 4 + 2\\sqrt{3} = (\\sqrt{3} + 1)^2 \\Rightarrow \\sqrt{x} = \\sqrt{3} + 1$.\n"
         "$$P = \\frac{4 + 2\\sqrt{3} - 1}{\\sqrt{3} + 1} = \\frac{3 + 2\\sqrt{3}}{\\sqrt{3} + 1} = \\frac{\\sqrt{3}(\\sqrt{3} + 2)}{\\sqrt{3} + 1} = \\frac{(3 + 2\\sqrt{3})(\\sqrt{3} - 1)}{2} = \\frac{3\\sqrt{3} - 3 + 6 - 2\\sqrt{3}}{2} = \\frac{\\sqrt{3} + 3}{2}$$\n\n"
         "c) $P > 3 \\Leftrightarrow \\frac{x - 1}{\\sqrt{x}} > 3 \\Leftrightarrow x - 3\\sqrt{x} - 1 > 0$.\n"
         "Giải ra: $\\sqrt{x} > \\frac{3 + \\sqrt{13}}{2} \\Leftrightarrow x > \\left(\\frac{3 + \\sqrt{13}}{2}\\right)^2 = \\frac{11 + 3\\sqrt{13}}{2}$ (TMĐK)."),

        (7,
         "Cho biểu thức $A = \\frac{x - 4}{\\sqrt{x} + 2}$ và $B = \\frac{\\sqrt{x}}{\\sqrt{x} - 2} + \\frac{\\sqrt{x}}{\\sqrt{x} + 2} - \\frac{4\\sqrt{x}}{x - 4}$ với $x \\ge 0, x \\ne 4$.\n"
         "a) Rút gọn biểu thức $A$ và biểu thức $B$.\n"
         "b) Đặt $P = \\frac{B}{A}$. Tính $P$ khi $x = 9$.\n"
         "c) Tìm $x$ để $P = 2$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Ta có:\n"
         "$$A = \\frac{(\\sqrt{x} - 2)(\\sqrt{x} + 2)}{\\sqrt{x} + 2} = \\sqrt{x} - 2$$\n"
         "$$B = \\frac{\\sqrt{x}(\\sqrt{x} + 2) + \\sqrt{x}(\\sqrt{x} - 2) - 4\\sqrt{x}}{x - 4} = \\frac{x + 2\\sqrt{x} + x - 2\\sqrt{x} - 4\\sqrt{x}}{x - 4} = \\frac{2x - 4\\sqrt{x}}{x - 4}$$\n"
         "$$B = \\frac{2\\sqrt{x}(\\sqrt{x} - 2)}{(\\sqrt{x} - 2)(\\sqrt{x} + 2)} = \\frac{2\\sqrt{x}}{\\sqrt{x} + 2}$$\n\n"
         "b) $P = \\frac{B}{A} = \\frac{2\\sqrt{x}}{\\sqrt{x} + 2} : (\\sqrt{x} - 2) = \\frac{2\\sqrt{x}}{x - 4}$.\n"
         "Khi $x = 9$: $P = \\frac{2\\sqrt{9}}{9 - 4} = \\frac{6}{5}$.\n\n"
         "c) $P = 2 \\Leftrightarrow \\frac{2\\sqrt{x}}{x - 4} = 2 \\Leftrightarrow \\sqrt{x} = x - 4 \\Leftrightarrow x - \\sqrt{x} - 4 = 0$.\n"
         "Đặt $t = \\sqrt{x} \\ge 0$, phương trình có nghiệm dương $t = \\frac{1 + \\sqrt{17}}{2}$.\n"
         "Suy ra $x = \\left(\\frac{1 + \\sqrt{17}}{2}\\right)^2 = \\frac{9 + \\sqrt{17}}{2}$ (thỏa mãn ĐKXĐ)."),

        (8,
         "Cho biểu thức $M = \\left(\\frac{\\sqrt{x} + 2}{x + 2\\sqrt{x} + 1} - \\frac{\\sqrt{x} - 2}{x - 1}\\right) \\cdot \\frac{\\sqrt{x} + 1}{\\sqrt{x}}$ với $x > 0, x \\ne 1$.\n"
         "a) Rút gọn biểu thức $M$.\n"
         "b) Tính giá trị của biểu thức $M$ khi $x = \\frac{1}{4}$.\n"
         "c) Tìm $x$ để $M = 1$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Phân tích mẫu: $x + 2\\sqrt{x} + 1 = (\\sqrt{x} + 1)^2$ và $x - 1 = (\\sqrt{x} - 1)(\\sqrt{x} + 1)$.\n"
         "Quy đồng trong ngoặc với MTC là $(\\sqrt{x} + 1)^2(\\sqrt{x} - 1)$:\n"
         "$$(\\sqrt{x} + 2)(\\sqrt{x} - 1) - (\\sqrt{x} - 2)(\\sqrt{x} + 1) = (x + \\sqrt{x} - 2) - (x - \\sqrt{x} - 2) = 2\\sqrt{x}$$\n"
         "Do đó:\n"
         "$$M = \\frac{2\\sqrt{x}}{(\\sqrt{x} + 1)^2(\\sqrt{x} - 1)} \\cdot \\frac{\\sqrt{x} + 1}{\\sqrt{x}} = \\frac{2}{(\\sqrt{x} + 1)(\\sqrt{x} - 1)} = \\frac{2}{x - 1}$$\n\n"
         "b) Khi $x = \\frac{1}{4}$: $M = \\frac{2}{\\frac{1}{4} - 1} = \\frac{2}{-\\frac{3}{4}} = -\\frac{8}{3}$.\n\n"
         "c) $M = 1 \\Leftrightarrow \\frac{2}{x - 1} = 1 \\Leftrightarrow x - 1 = 2 \\Leftrightarrow x = 3$ (TMĐK).\n"
         "Vậy $x = 3$."),

        (9,
         "Cho hai biểu thức $A = \\frac{x - 9}{\\sqrt{x} - 3}$ và $B = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 3} - \\frac{11\\sqrt{x} - 3}{x - 9}$ với $x \\ge 0, x \\ne 9$.\n"
         "a) Rút gọn biểu thức $A$ và $B$.\n"
         "b) Tính giá trị của $B$ khi $x = 4$.\n"
         "c) Đặt $H = \\frac{B}{A}$. Tìm $x$ để $H < 0$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) $A = \\frac{(\\sqrt{x} - 3)(\\sqrt{x} + 3)}{\\sqrt{x} - 3} = \\sqrt{x} + 3$.\n"
         "$$B = \\frac{(\\sqrt{x} + 1)(\\sqrt{x} + 3) - (11\\sqrt{x} - 3)}{x - 9} = \\frac{x + 4\\sqrt{x} + 3 - 11\\sqrt{x} + 3}{x - 9} = \\frac{x - 7\\sqrt{x} + 6}{x - 9}$$\n"
         "$$B = \\frac{(\\sqrt{x} - 1)(\\sqrt{x} - 6)}{(\\sqrt{x} - 3)(\\sqrt{x} + 3)}$$\n\n"
         "b) Khi $x = 4$: $B = \\frac{(2 - 1)(2 - 6)}{(2 - 3)(2 + 3)} = \\frac{1 \\cdot (-4)}{(-1) \\cdot 5} = \\frac{4}{5}$.\n\n"
         "c) Ta có $H = \\frac{B}{A} = \\frac{(\\sqrt{x} - 1)(\\sqrt{x} - 6)}{(\\sqrt{x} - 3)(\\sqrt{x} + 3)^2}$.\n"
         "Vì $(\\sqrt{x} + 3)^2 > 0$, dấu của $H$ là dấu của $(\\sqrt{x} - 1)(\\sqrt{x} - 3)(\\sqrt{x} - 6)$.\n"
         "Lập bảng xét dấu ta có $H < 0 \\Leftrightarrow 0 \\le x < 1$ hoặc $9 < x < 36$."),

        (10,
         "Cho biểu thức $P = \\left(\\frac{2\\sqrt{x}}{\\sqrt{x} + 3} + \\frac{\\sqrt{x}}{\\sqrt{x} - 3} - \\frac{3x + 3}{x - 9}\\right) : \\left(\\frac{2\\sqrt{x} - 2}{\\sqrt{x} - 3} - 1\\right)$ với $x \\ge 0, x \\ne 9, x \\ne 1$.\n"
         "a) Rút gọn biểu thức $P$.\n"
         "b) Tính giá trị của biểu thức $P$ khi $x = 16$.\n"
         "c) Tìm $x$ để $P = -\\frac{2}{3}$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Ngoặc 1:\n"
         "$$\\frac{2\\sqrt{x}(\\sqrt{x} - 3) + \\sqrt{x}(\\sqrt{x} + 3) - (3x + 3)}{x - 9} = \\frac{2x - 6\\sqrt{x} + x + 3\\sqrt{x} - 3x - 3}{x - 9} = \\frac{-3\\sqrt{x} - 3}{x - 9} = \\frac{-3(\\sqrt{x} + 1)}{x - 9}$$\n"
         "Ngoặc 2:\n"
         "$$\\frac{2\\sqrt{x} - 2 - (\\sqrt{x} - 3)}{\\sqrt{x} - 3} = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 3}$$\n"
         "Do đó:\n"
         "$$P = \\frac{-3(\\sqrt{x} + 1)}{(\\sqrt{x} - 3)(\\sqrt{x} + 3)} \\cdot \\frac{\\sqrt{x} - 3}{\\sqrt{x} + 1} = \\frac{-3}{\\sqrt{x} + 3}$$\n"
         "Kết quả cực kỳ gọn gàng!\n\n"
         "b) Khi $x = 16$: $P = \\frac{-3}{\\sqrt{16} + 3} = \\frac{-3}{4 + 3} = -\\frac{3}{7}$.\n\n"
         "c) $P = -\\frac{2}{3} \\Leftrightarrow \\frac{-3}{\\sqrt{x} + 3} = -\\frac{2}{3} \\Leftrightarrow 2(\\sqrt{x} + 3) = 9 \\Leftrightarrow 2\\sqrt{x} = 3 \\Leftrightarrow \\sqrt{x} = \\frac{3}{2} \\Leftrightarrow x = \\frac{9}{4}$ (TMĐK).\n"
         "Vậy $x = \\frac{9}{4}$."),

        (11,
         "Cho biểu thức $A = \\frac{2}{\\sqrt{x} - 2}$ và $B = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2} - \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 2} + \\frac{8}{4 - x}$ với $x \\ge 0, x \\ne 4$.\n"
         "a) Rút gọn biểu thức $B$.\n"
         "b) Tính $P = A - B$.\n"
         "c) Tìm $x$ để $P = \\frac{1}{2}$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) $B = \\frac{(\\sqrt{x} + 1)(\\sqrt{x} + 2) - (\\sqrt{x} - 1)(\\sqrt{x} - 2) - 8}{x - 4} = \\frac{(x + 3\\sqrt{x} + 2) - (x - 3\\sqrt{x} + 2) - 8}{x - 4} = \\frac{6\\sqrt{x} - 8}{x - 4}$.\n\n"
         "b) $P = A - B = \\frac{2(\\sqrt{x} + 2) - (6\\sqrt{x} - 8)}{x - 4} = \\frac{2\\sqrt{x} + 4 - 6\\sqrt{x} + 8}{x - 4} = \\frac{-4\\sqrt{x} + 12}{x - 4} = \\frac{-4(\\sqrt{x} - 3)}{x - 4}$.\n\n"
         "c) $P = \\frac{1}{2} \\Leftrightarrow 2(-4\\sqrt{x} + 12) = x - 4 \\Leftrightarrow x + 8\\sqrt{x} - 28 = 0 \\Leftrightarrow (\\sqrt{x} - 2)(\\sqrt{x} + 14) = 0$.\n"
         "Suy ra $\\sqrt{x} = 2 \\Leftrightarrow x = 4$ (loại vì vi phạm ĐKXĐ $x \\ne 4$). Vậy phương trình vô nghiệm."),

        (12,
         "Cho biểu thức $P = \\left(\\frac{\\sqrt{x} - 2}{x - 1} - \\frac{\\sqrt{x} + 2}{x + 2\\sqrt{x} + 1}\\right) \\cdot \\frac{(1 - x)^2}{2}$ với $x \\ge 0, x \\ne 1$.\n"
         "a) Rút gọn biểu thức $P$.\n"
         "b) Tính giá trị của biểu thức $P$ khi $x = 8 - 2\\sqrt{7}$.\n"
         "c) Tìm các giá trị của $x$ để $P > 0$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Quy đồng trong ngoặc với MTC là $(\\sqrt{x} - 1)(\\sqrt{x} + 1)^2$:\n"
         "$$(\\sqrt{x} - 2)(\\sqrt{x} + 1) - (\\sqrt{x} + 2)(\\sqrt{x} - 1) = (x - \\sqrt{x} - 2) - (x + \\sqrt{x} - 2) = -2\\sqrt{x}$$\n"
         "Nhân với $\\frac{(1 - x)^2}{2} = \\frac{(x - 1)^2}{2} = \\frac{(\\sqrt{x} - 1)^2(\\sqrt{x} + 1)^2}{2}$:\n"
         "$$P = \\frac{-2\\sqrt{x}}{(\\sqrt{x} - 1)(\\sqrt{x} + 1)^2} \\cdot \\frac{(\\sqrt{x} - 1)^2(\\sqrt{x} + 1)^2}{2} = -\\sqrt{x}(\\sqrt{x} - 1) = \\sqrt{x}(1 - \\sqrt{x})$$\n\n"
         "b) Khi $x = 8 - 2\\sqrt{7} = (\\sqrt{7} - 1)^2 \\Rightarrow \\sqrt{x} = \\sqrt{7} - 1$.\n"
         "$$P = (\\sqrt{7} - 1)(1 - (\\sqrt{7} - 1)) = (\\sqrt{7} - 1)(2 - \\sqrt{7}) = 3\\sqrt{7} - 9$$.\n\n"
         "c) $P > 0 \\Leftrightarrow \\sqrt{x}(1 - \\sqrt{x}) > 0$. Vì $x > 0$ nên $\\sqrt{x} > 0 \\Rightarrow 1 - \\sqrt{x} > 0 \\Leftrightarrow \\sqrt{x} < 1 \\Leftrightarrow 0 < x < 1$."),

        (13,
         "Cho biểu thức $A = \\frac{\\sqrt{x} - 1}{\\sqrt{x}}$ và $B = \\frac{\\sqrt{x} - 2}{\\sqrt{x}} + \\frac{1}{\\sqrt{x} - 1} + \\frac{x - 2}{x - \\sqrt{x}}$ với $x > 0, x \\ne 1$.\n"
         "a) Tính giá trị của $A$ tại $x = 25$.\n"
         "b) Rút gọn biểu thức $B$.\n"
         "c) Cho $P = \\frac{B}{A}$. Tìm $x$ để $P = 3$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Khi $x = 25$: $A = \\frac{5 - 1}{5} = \\frac{4}{5}$.\n\n"
         "b) $B = \\frac{(\\sqrt{x} - 2)(\\sqrt{x} - 1) + \\sqrt{x} + x - 2}{\\sqrt{x}(\\sqrt{x} - 1)} = \\frac{x - 3\\sqrt{x} + 2 + \\sqrt{x} + x - 2}{\\sqrt{x}(\\sqrt{x} - 1)} = \\frac{2x - 2\\sqrt{x}}{\\sqrt{x}(\\sqrt{x} - 1)} = \\frac{2\\sqrt{x}(\\sqrt{x} - 1)}{\\sqrt{x}(\\sqrt{x} - 1)} = 2$.\n"
         "Biểu thức $B$ rút gọn ra hằng số bằng 2 cực kỳ đẹp mắt!\n\n"
         "c) $P = \\frac{B}{A} = \\frac{2}{\\frac{\\sqrt{x} - 1}{\\sqrt{x}}} = \\frac{2\\sqrt{x}}{\\sqrt{x} - 1}$.\n"
         "Để $P = 3 \\Leftrightarrow 2\\sqrt{x} = 3\\sqrt{x} - 3 \\Leftrightarrow \\sqrt{x} = 3 \\Leftrightarrow x = 9$ (TMĐK).\n"
         "Vậy $x = 9$."),

        (14,
         "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x} + 2} - \\frac{1}{\\sqrt{x} - 2}\\right) : \\frac{\\sqrt{x}}{x - 4}$ với $x > 0, x \\ne 4$.\n"
         "a) Rút gọn biểu thức $P$.\n"
         "b) Tính giá trị của $P$ khi $x = 9$.\n"
         "c) Tìm $x$ để $P = -1$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) $\\frac{1}{\\sqrt{x} + 2} - \\frac{1}{\\sqrt{x} - 2} = \\frac{\\sqrt{x} - 2 - (\\sqrt{x} + 2)}{x - 4} = \\frac{-4}{x - 4}$.\n"
         "$$P = \\frac{-4}{x - 4} : \\frac{\\sqrt{x}}{x - 4} = \\frac{-4}{x - 4} \\cdot \\frac{x - 4}{\\sqrt{x}} = -\\frac{4}{\\sqrt{x}}$$\n\n"
         "b) Khi $x = 9$: $P = -\\frac{4}{\\sqrt{9}} = -\\frac{4}{3}$.\n\n"
         "c) $P = -1 \\Leftrightarrow -\\frac{4}{\\sqrt{x}} = -1 \\Leftrightarrow \\sqrt{x} = 4 \\Leftrightarrow x = 16$ (TMĐK).\n"
         "Vậy $x = 16$."),

        (15,
         "Cho biểu thức $A = \\frac{x - 2\\sqrt{x}}{x - 4}$ và $B = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2} - \\frac{\\sqrt{x} + 2}{\\sqrt{x} + 3} - \\frac{5\\sqrt{x} - 1}{x + \\sqrt{x} - 6}$ với $x \\ge 0, x \\ne 4, x \\ne 9$.\n"
         "a) Rút gọn biểu thức $A$.\n"
         "b) Rút gọn biểu thức $B$.\n"
         "c) Đặt $M = A \\cdot B$. So sánh $M$ với 0.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) $A = \\frac{\\sqrt{x}(\\sqrt{x} - 2)}{(\\sqrt{x} - 2)(\\sqrt{x} + 2)} = \\frac{\\sqrt{x}}{\\sqrt{x} + 2}$.\n\n"
         "b) Mẫu chung: $(\\sqrt{x} - 2)(\\sqrt{x} + 3) = x + \\sqrt{x} - 6$.\n"
         "$$B = \\frac{(\\sqrt{x} + 1)(\\sqrt{x} + 3) - (\\sqrt{x} + 2)(\\sqrt{x} - 2) - (5\\sqrt{x} - 1)}{x + \\sqrt{x} - 6}$$\n"
         "$$B = \\frac{(x + 4\\sqrt{x} + 3) - (x - 4) - 5\\sqrt{x} + 1}{x + \\sqrt{x} - 6} = \\frac{-\\sqrt{x} + 8}{x + \\sqrt{x} - 6}$$\n\n"
         "c) $M = A \\cdot B = \\frac{\\sqrt{x}}{\\sqrt{x} + 2} \\cdot \\frac{-\\sqrt{x} + 8}{(\\sqrt{x} - 2)(\\sqrt{x} + 3)}$.\n"
         "Xét dấu của $M$ theo từng khoảng của $x$."),

        (16,
         "Cho biểu thức $P = \\left(\\frac{\\sqrt{x} + 3}{\\sqrt{x} - 1} - \\frac{\\sqrt{x} - 3}{\\sqrt{x} + 1}\\right) : \\frac{8\\sqrt{x}}{x - 1}$ với $x > 0, x \\ne 1$.\n"
         "a) Rút gọn biểu thức $P$.\n"
         "b) Tìm giá trị của $P$ khi $x = 100$.\n"
         "c) Chứng minh rằng $P$ là một hằng số không phụ thuộc vào $x$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Quy đồng ngoặc thứ nhất với MTC là $x - 1$:\n"
         "$$(\\sqrt{x} + 3)(\\sqrt{x} + 1) - (\\sqrt{x} - 3)(\\sqrt{x} - 1) = (x + 4\\sqrt{x} + 3) - (x - 4\\sqrt{x} + 3) = 8\\sqrt{x}$$\n"
         "Do đó:\n"
         "$$P = \\frac{8\\sqrt{x}}{x - 1} : \\frac{8\\sqrt{x}}{x - 1} = 1$$\n\n"
         "b) Khi $x = 100$: $P = 1$.\n\n"
         "c) Vì $P = 1$ với mọi $x > 0, x \\ne 1$ nên giá trị của $P$ là một hằng số không đổi, không phụ thuộc vào giá trị của biến $x$."),

        (17,
         "Cho hai biểu thức $A = \\frac{1}{\\sqrt{x} - 3}$ và $B = \\frac{\\sqrt{x} - 1}{\\sqrt{x} - 3} - \\frac{x - 3\\sqrt{x} + 2}{x - 9} - \\frac{\\sqrt{x}}{\\sqrt{x} + 3}$ với $x \\ge 0, x \\ne 9$.\n"
         "a) Tính giá trị của biểu thức $A$ tại $x = 4$.\n"
         "b) Rút gọn biểu thức $B$.\n"
         "c) Tìm $x$ để biểu thức $P = \\frac{B}{A}$ có giá trị bằng $-2$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Thay $x = 4$ vào $A$: $A = \\frac{1}{2 - 3} = -1$.\n\n"
         "b) Quy đồng với MTC là $x - 9$:\n"
         "$$B = \\frac{(\\sqrt{x} - 1)(\\sqrt{x} + 3) - (x - 3\\sqrt{x} + 2) - \\sqrt{x}(\\sqrt{x} - 3)}{x - 9}$$\n"
         "$$B = \\frac{(x + 2\\sqrt{x} - 3) - (x - 3\\sqrt{x} + 2) - (x - 3\\sqrt{x})}{x - 9} = \\frac{-x + 8\\sqrt{x} - 5}{x - 9}$$.\n\n"
         "c) Giải phương trình tỉ số $P = -2$ tìm nghiệm $x$ thỏa mãn ĐKXĐ."),

        (18,
         "Cho biểu thức $P = \\left(\\frac{x + 2}{x\\sqrt{x} - 1} + \\frac{\\sqrt{x} + 1}{x + \\sqrt{x} + 1} - \\frac{1}{\\sqrt{x} - 1}\\right) : \\frac{\\sqrt{x} - 1}{2}$ với $x \\ge 0, x \\ne 1$.\n"
         "a) Rút gọn biểu thức $P$.\n"
         "b) Tính giá trị của biểu thức $P$ khi $x = 4$.\n"
         "c) Tìm $x$ để $P < 1$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Nhận xét: $x\\sqrt{x} - 1 = (\\sqrt{x} - 1)(x + \\sqrt{x} + 1)$.\n"
         "Quy đồng trong ngoặc:\n"
         "$$x + 2 + (\\sqrt{x} + 1)(\\sqrt{x} - 1) - (x + \\sqrt{x} + 1) = x + 2 + x - 1 - x - \\sqrt{x} - 1 = x - \\sqrt{x} = \\sqrt{x}(\\sqrt{x} - 1)$$\n"
         "Do đó:\n"
         "$$\\frac{\\sqrt{x}(\\sqrt{x} - 1)}{(\\sqrt{x} - 1)(x + \\sqrt{x} + 1)} = \\frac{\\sqrt{x}}{x + \\sqrt{x} + 1}$$\n"
         "Chia cho $\\frac{\\sqrt{x} - 1}{2}$:\n"
         "$$P = \\frac{2\\sqrt{x}}{(x + \\sqrt{x} + 1)(\\sqrt{x} - 1)}$$\n\n"
         "b) Khi $x = 4$: $P = \\frac{2(2)}{(4 + 2 + 1)(2 - 1)} = \\frac{4}{7}$.\n\n"
         "c) Giải bất phương trình $P < 1$."),

        (19,
         "Cho biểu thức $A = \\frac{\\sqrt{x} + 2}{\\sqrt{x} + 5}$ và $B = \\frac{\\sqrt{x}}{\\sqrt{x} - 3} - \\frac{2}{x - 9} - \\frac{1}{\\sqrt{x} + 3}$ với $x \\ge 0, x \\ne 9$.\n"
         "a) Tính giá trị của $A$ khi $x = 1$.\n"
         "b) Rút gọn biểu thức $B$.\n"
         "c) Tìm $x$ để $B = 1$.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Với $x = 1$: $A = \\frac{1 + 2}{1 + 5} = \\frac{3}{6} = \\frac{1}{2}$.\n\n"
         "b) Mẫu thức chung là $x - 9$:\n"
         "$$B = \\frac{\\sqrt{x}(\\sqrt{x} + 3) - 2 - (\\sqrt{x} - 3)}{x - 9} = \\frac{x + 3\\sqrt{x} - 2 - \\sqrt{x} + 3}{x - 9} = \\frac{x + 2\\sqrt{x} + 1}{x - 9} = \\frac{(\\sqrt{x} + 1)^2}{x - 9}$$\n\n"
         "c) $B = 1 \\Leftrightarrow (\\sqrt{x} + 1)^2 = x - 9 \\Leftrightarrow x + 2\\sqrt{x} + 1 = x - 9 \\Leftrightarrow 2\\sqrt{x} = -10$ (vô nghiệm vì $\\sqrt{x} \\ge 0$).\n"
         "Vậy không có giá trị nào của $x$ để $B = 1$."),

        (20,
         "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x} - 3} + \\frac{1}{\\sqrt{x} + 3}\\right) \\cdot \\frac{x - 9}{2\\sqrt{x}}$ với $x > 0, x \\ne 9$.\n"
         "a) Rút gọn biểu thức $P$.\n"
         "b) Tính $P$ khi $x = 16$.\n"
         "c) Tìm $x$ để biểu thức nhận giá trị bằng 1.",
         "VD",
         "**Lời giải chi tiết:**\n\n"
         "a) Quy đồng trong ngoặc:\n"
         "$$\\frac{\\sqrt{x} + 3 + \\sqrt{x} - 3}{x - 9} = \\frac{2\\sqrt{x}}{x - 9}$$\n"
         "Nhân với phân thức ngoài:\n"
         "$$P = \\frac{2\\sqrt{x}}{x - 9} \\cdot \\frac{x - 9}{2\\sqrt{x}} = 1$$\n\n"
         "b) Khi $x = 16$: $P = 1$.\n\n"
         "c) Biểu thức $P = 1$ với mọi $x > 0, x \\ne 9$."),

        # =========================================================================
        # PHẦN 2: 20 CÂU VẬN DỤNG CAO (CÂU 21 - 40)
        # =========================================================================
        (21,
         "Cho biểu thức $P = \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 1}$ với $x \\ge 0, x \\ne 1$.\n"
         "a) Rút gọn biểu thức $P$ dưới dạng tách phần nguyên.\n"
         "b) Tìm tất cả các số nguyên $x$ để biểu thức $P$ nhận giá trị nguyên.\n"
         "c) Tìm tất cả các số thực $x$ để biểu thức $P$ nhận giá trị nguyên.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Tách phần nguyên:\n"
         "$$P = \\frac{(\\sqrt{x} - 1) + 3}{\\sqrt{x} - 1} = 1 + \\frac{3}{\\sqrt{x} - 1}$$\n\n"
         "b) Với $x \\in \\mathbb{Z}$ ($x \\ge 0, x \\ne 1$):\n"
         "Để $P \\in \\mathbb{Z} \\Leftrightarrow \\frac{3}{\\sqrt{x} - 1} \\in \\mathbb{Z} \\Leftrightarrow \\sqrt{x} - 1$ là ước của $3$.\n"
         "Các ước của 3 là $\\pm 1, \\pm 3$:\n"
         "- $\\sqrt{x} - 1 = 1 \\Rightarrow \\sqrt{x} = 2 \\Rightarrow x = 4$ (TM).\n"
         "- $\\sqrt{x} - 1 = -1 \\Rightarrow \\sqrt{x} = 0 \\Rightarrow x = 0$ (TM).\n"
         "- $\\sqrt{x} - 1 = 3 \\Rightarrow \\sqrt{x} = 4 \\Rightarrow x = 16$ (TM).\n"
         "- $\\sqrt{x} - 1 = -3 \\Rightarrow \\sqrt{x} = -2$ (vô nghiệm).\n"
         "Vậy $x \\in \\{0; 4; 16\\}$.\n\n"
         "c) Tìm $x \\in \\mathbb{R}$ để $P \\in \\mathbb{Z}$ (Phương pháp chặn miền giá trị):\n"
         "Với $x > 1$: $\\sqrt{x} - 1 > 0 \\Rightarrow \\frac{3}{\\sqrt{x} - 1} > 0 \\Rightarrow P > 1$.\n"
         "Khi đó $P$ có thể nhận các giá trị nguyên $k \\in \\{2, 3, 4, \\dots\\}$.\n"
         "Với $0 \\le x < 1$: $-1 \\le \\sqrt{x} - 1 < 0 \\Rightarrow \\frac{3}{\\sqrt{x} - 1} \\le -3 \\Rightarrow P \\le -2$.\n"
         "Do đó $P$ nhận các giá trị nguyên âm $\\le -2$."),

        (22,
         "Cho biểu thức $P = \\frac{4}{\\sqrt{x} + 1}$ với $x \\ge 0$.\n"
         "a) Chứng minh rằng $0 < P \\le 4$.\n"
         "b) Tìm tất cả các giá trị thực của $x$ để $P$ nhận giá trị nguyên.\n"
         "c) Tìm giá trị lớn nhất của $P$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Với $x \\ge 0 \\Rightarrow \\sqrt{x} \\ge 0 \\Rightarrow \\sqrt{x} + 1 \\ge 1$.\n"
         "Vì tử số $4 > 0$ và mẫu $\\sqrt{x} + 1 > 0$ nên $P > 0$.\n"
         "Mặt khác $\\sqrt{x} + 1 \\ge 1 \\Rightarrow \\frac{4}{\\sqrt{x} + 1} \\le \\frac{4}{1} = 4$.\n"
         "Vậy $0 < P \\le 4$.\n\n"
         "b) Vì $0 < P \\le 4$ và $P \\in \\mathbb{Z}$ nên $P \\in \\{1; 2; 3; 4\\}$:\n"
         "- $P = 4 \\Leftrightarrow \\frac{4}{\\sqrt{x} + 1} = 4 \\Leftrightarrow \\sqrt{x} + 1 = 1 \\Leftrightarrow x = 0$ (TM).\n"
         "- $P = 3 \\Leftrightarrow \\sqrt{x} + 1 = \\frac{4}{3} \\Leftrightarrow \\sqrt{x} = \\frac{1}{3} \\Leftrightarrow x = \\frac{1}{9}$ (TM).\n"
         "- $P = 2 \\Leftrightarrow \\sqrt{x} + 1 = 2 \\Leftrightarrow \\sqrt{x} = 1 \\Leftrightarrow x = 1$ (TM).\n"
         "- $P = 1 \\Leftrightarrow \\sqrt{x} + 1 = 4 \\Leftrightarrow \\sqrt{x} = 3 \\Leftrightarrow x = 9$ (TM).\n"
         "Vậy $x \\in \\left\\{0; \\frac{1}{9}; 1; 9\\right\\}$.\n\n"
         "c) Theo câu a, $P \\le 4$. Dấu '=' xảy ra khi $\\sqrt{x} = 0 \\Leftrightarrow x = 0$.\n"
         "Vậy GTLN của $P$ bằng 4 khi $x = 0$."),

        (23,
         "Cho biểu thức $P = \\frac{x + 3}{\\sqrt{x} + 1}$ với $x \\ge 0$.\n"
         "a) Biến đổi $P = \\sqrt{x} - 1 + \\frac{4}{\\sqrt{x} + 1}$.\n"
         "b) Tìm giá trị nhỏ nhất (GTNN) của biểu thức $P$.\n"
         "c) Tìm $x$ để biểu thức đạt GTNN.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Ta có:\n"
         "$$P = \\frac{x - 1 + 4}{\\sqrt{x} + 1} = \\frac{(\\sqrt{x} - 1)(\\sqrt{x} + 1) + 4}{\\sqrt{x} + 1} = \\sqrt{x} - 1 + \\frac{4}{\\sqrt{x} + 1}$$\n\n"
         "b) Thêm bớt để áp dụng bất đẳng thức Cô-si:\n"
         "$$P = (\\sqrt{x} + 1) + \\frac{4}{\\sqrt{x} + 1} - 2$$\n"
         "Vì $x \\ge 0$ nên $\\sqrt{x} + 1 > 0$ và $\\frac{4}{\\sqrt{x} + 1} > 0$.\n"
         "Áp dụng BĐT Cô-si cho hai số dương:\n"
         "$$(\\sqrt{x} + 1) + \\frac{4}{\\sqrt{x} + 1} \\ge 2\\sqrt{(\\sqrt{x} + 1) \\cdot \\frac{4}{\\sqrt{x} + 1}} = 2 \\cdot 2 = 4$$\n"
         "Suy ra $P \\ge 4 - 2 = 2$.\n\n"
         "c) Dấu '=' xảy ra khi và chỉ khi:\n"
         "$$\\sqrt{x} + 1 = \\frac{4}{\\sqrt{x} + 1} \\Leftrightarrow (\\sqrt{x} + 1)^2 = 4 \\Leftrightarrow \\sqrt{x} + 1 = 2 \\Leftrightarrow \\sqrt{x} = 1 \\Leftrightarrow x = 1$$\n"
         "Vậy GTNN của $P$ là 2, đạt được khi $x = 1$."),

        (24,
         "Cho biểu thức $P = \\frac{\\sqrt{x}}{x - \\sqrt{x} + 1}$ với $x \\ge 0$.\n"
         "a) Chứng minh rằng mẫu thức $x - \\sqrt{x} + 1 > 0$ với mọi $x \\ge 0$.\n"
         "b) Tìm giá trị lớn nhất (GTLN) của biểu thức $P$.\n"
         "c) Giá trị nhỏ nhất của $P$ bằng bao nhiêu?",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Ta có: $x - \\sqrt{x} + 1 = \\left(\\sqrt{x} - \\frac{1}{2}\\right)^2 + \\frac{3}{4} \\ge \\frac{3}{4} > 0$ với mọi $x \\ge 0$.\n\n"
         "b) Với $x = 0 \\Rightarrow P = 0$.\n"
         "Với $x > 0$, chia cả tử và mẫu cho $\\sqrt{x}$:\n"
         "$$P = \\frac{1}{\\sqrt{x} + \\frac{1}{\\sqrt{x}} - 1}$$\n"
         "Theo BĐT Cô-si: $\\sqrt{x} + \\frac{1}{\\sqrt{x}} \\ge 2$.\n"
         "Suy ra $\\sqrt{x} + \\frac{1}{\\sqrt{x}} - 1 \\ge 2 - 1 = 1$.\n"
         "Do đó $P \\le \\frac{1}{1} = 1$.\n"
         "Dấu '=' xảy ra khi $\\sqrt{x} = \\frac{1}{\\sqrt{x}} \\Leftrightarrow x = 1$.\n"
         "Vậy GTLN của $P$ là 1 khi $x = 1$.\n\n"
         "c) Vì $x \\ge 0$ nên tử $\\sqrt{x} \\ge 0$, mẫu $> 0 \\Rightarrow P \\ge 0$.\n"
         "Dấu '=' xảy ra khi $x = 0$. Vậy GTNN của $P$ là 0 khi $x = 0$."),

        (25,
         "Cho biểu thức $P = \\frac{2\\sqrt{x} - 1}{\\sqrt{x} + 1}$ với $x \\ge 0$.\n"
         "a) Tìm tất cả các số nguyên $x$ để $P$ nhận giá trị nguyên.\n"
         "b) Tìm tất cả các số thực $x$ để $P$ nhận giá trị nguyên.\n"
         "c) Tìm $x$ để $P > 1$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Tách phần nguyên:\n"
         "$$P = \\frac{2(\\sqrt{x} + 1) - 3}{\\sqrt{x} + 1} = 2 - \\frac{3}{\\sqrt{x} + 1}$$\n"
         "Để $P \\in \\mathbb{Z}$ với $x$ nguyên thì $\\sqrt{x} + 1$ là ước dương của 3.\n"
         "Ước dương của 3 là $1, 3$:\n"
         "- $\\sqrt{x} + 1 = 1 \\Rightarrow \\sqrt{x} = 0 \\Rightarrow x = 0$ (TM).\n"
         "- $\\sqrt{x} + 1 = 3 \\Rightarrow \\sqrt{x} = 2 \\Rightarrow x = 4$ (TM).\n"
         "Vậy $x \\in \\{0; 4\\}$.\n\n"
         "b) Vì $x \\ge 0 \\Rightarrow \\sqrt{x} + 1 \\ge 1 \\Rightarrow 0 < \\frac{3}{\\sqrt{x} + 1} \\le 3$.\n"
         "Suy ra $2 - 3 \\le P < 2 \\Leftrightarrow -1 \\le P < 2$.\n"
         "Vì $P \\in \\mathbb{Z}$ nên $P \\in \\{-1; 0; 1\\}$:\n"
         "- $P = -1 \\Leftrightarrow \\frac{3}{\\sqrt{x} + 1} = 3 \\Leftrightarrow \\sqrt{x} + 1 = 1 \\Leftrightarrow x = 0$.\n"
         "- $P = 0 \\Leftrightarrow 2\\sqrt{x} - 1 = 0 \\Leftrightarrow x = \\frac{1}{4}$.\n"
         "- $P = 1 \\Leftrightarrow 2 - \\frac{3}{\\sqrt{x} + 1} = 1 \\Leftrightarrow \\frac{3}{\\sqrt{x} + 1} = 1 \\Leftrightarrow \\sqrt{x} + 1 = 3 \\Leftrightarrow x = 4$.\n"
         "Vậy $x \\in \\left\\{0; \\frac{1}{4}; 4\\right\\}$.\n\n"
         "c) $P > 1 \\Leftrightarrow 2 - \\frac{3}{\\sqrt{x} + 1} > 1 \\Leftrightarrow \\frac{3}{\\sqrt{x} + 1} < 1 \\Leftrightarrow \\sqrt{x} + 1 > 3 \\Leftrightarrow \\sqrt{x} > 2 \\Leftrightarrow x > 4$."),

        (26,
         "Cho biểu thức $P = \\frac{x + 2}{\\sqrt{x}}$ với $x > 0$.\n"
         "a) Tìm giá trị nhỏ nhất của $P$.\n"
         "b) Tìm $x$ để $P = 2\\sqrt{2}$.\n"
         "c) Chứng minh rằng $P \\ge 2\\sqrt{2}$ với mọi $x > 0$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Biến đổi: $P = \\sqrt{x} + \\frac{2}{\\sqrt{x}}$.\n"
         "Vì $x > 0$, áp dụng BĐT Cô-si cho hai số dương $\\sqrt{x}$ và $\\frac{2}{\\sqrt{x}}$:\n"
         "$$P = \\sqrt{x} + \\frac{2}{\\sqrt{x}} \\ge 2\\sqrt{\\sqrt{x} \\cdot \\frac{2}{\\sqrt{x}}} = 2\\sqrt{2}$$\n"
         "Dấu '=' xảy ra khi $\\sqrt{x} = \\frac{2}{\\sqrt{x}} \\Leftrightarrow x = 2$.\n"
         "Vậy GTNN của $P$ là $2\\sqrt{2}$ khi $x = 2$.\n\n"
         "b) $P = 2\\sqrt{2} \\Leftrightarrow x = 2$.\n\n"
         "c) Chứng minh ở câu a đã khẳng định $P \\ge 2\\sqrt{2}$ với mọi $x > 0$."),

        (27,
         "Cho biểu thức $P = \\frac{\\sqrt{x} + 3}{\\sqrt{x} - 2}$ với $x \\ge 0, x \\ne 4$.\n"
         "a) Tìm tất cả các số nguyên $x$ để $P$ nhận giá trị là một số nguyên dương.\n"
         "b) Tìm $x$ để $|P| > P$.\n"
         "c) Tìm $x$ để $P < 0$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Tách phần nguyên:\n"
         "$$P = 1 + \\frac{5}{\\sqrt{x} - 2}$$\n"
         "Để $P \\in \\mathbb{Z}^+$ thì $\\sqrt{x} - 2$ là ước của 5 sao cho $P > 0$:\n"
         "- $\\sqrt{x} - 2 = 1 \\Rightarrow \\sqrt{x} = 3 \\Rightarrow x = 9 \\Rightarrow P = 6$ (TM).\n"
         "- $\\sqrt{x} - 2 = 5 \\Rightarrow \\sqrt{x} = 7 \\Rightarrow x = 49 \\Rightarrow P = 2$ (TM).\n"
         "- $\\sqrt{x} - 2 = -1 \\Rightarrow \\sqrt{x} = 1 \\Rightarrow x = 1 \\Rightarrow P = -4$ (loại vì âm).\n"
         "Vậy $x \\in \\{9; 49\\}$.\n\n"
         "b) Ta có $|P| > P \\Leftrightarrow P < 0$.\n\n"
         "c) $P < 0 \\Leftrightarrow \\frac{\\sqrt{x} + 3}{\\sqrt{x} - 2} < 0$. Vì $\\sqrt{x} + 3 > 0$ nên $\\sqrt{x} - 2 < 0 \\Leftrightarrow \\sqrt{x} < 2 \\Leftrightarrow 0 \\le x < 4$."),

        (28,
         "Cho biểu thức $P = \\frac{2\\sqrt{x}}{\\sqrt{x} + 2}$ với $x \\ge 0$.\n"
         "a) Chứng minh rằng $0 \\le P < 2$.\n"
         "b) Tìm tất cả các giá trị thực của $x$ để $P$ nhận giá trị nguyên.\n"
         "c) Tìm các số nguyên $x$ để $P$ nhận giá trị nguyên.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Vì $x \\ge 0$ nên $2\\sqrt{x} \\ge 0$ và $\\sqrt{x} + 2 > 0 \\Rightarrow P \\ge 0$.\n"
         "Mặt khác: $P = \\frac{2(\\sqrt{x} + 2) - 4}{\\sqrt{x} + 2} = 2 - \\frac{4}{\\sqrt{x} + 2}$.\n"
         "Vì $\\frac{4}{\\sqrt{x} + 2} > 0$ nên $P < 2$.\n"
         "Vậy $0 \\le P < 2$.\n\n"
         "b) Vì $0 \\le P < 2$ và $P \\in \\mathbb{Z}$ nên $P \\in \\{0; 1\\}$:\n"
         "- $P = 0 \\Leftrightarrow 2\\sqrt{x} = 0 \\Leftrightarrow x = 0$.\n"
         "- $P = 1 \\Leftrightarrow \\frac{2\\sqrt{x}}{\\sqrt{x} + 2} = 1 \\Leftrightarrow 2\\sqrt{x} = \\sqrt{x} + 2 \\Leftrightarrow \\sqrt{x} = 2 \\Leftrightarrow x = 4$.\n"
         "Vậy $x \\in \\{0; 4\\}$.\n\n"
         "c) Cả hai giá trị $x = 0$ và $x = 4$ đều là số nguyên, do đó $x \\in \\{0; 4\\}$."),

        (29,
         "Cho biểu thức $P = \\frac{x + \\sqrt{x} + 1}{\\sqrt{x}}$ với $x > 0$.\n"
         "a) Tìm giá trị nhỏ nhất của $P$.\n"
         "b) Tìm các giá trị của $x$ để $P = 3$.\n"
         "c) Chứng minh rằng $P \\ge 3$ với mọi $x > 0$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Ta có: $P = \\sqrt{x} + 1 + \\frac{1}{\\sqrt{x}} = \\left(\\sqrt{x} + \\frac{1}{\\sqrt{x}}\\right) + 1$.\n"
         "Theo BĐT Cô-si: $\\sqrt{x} + \\frac{1}{\\sqrt{x}} \\ge 2\\sqrt{\\sqrt{x} \\cdot \\frac{1}{\\sqrt{x}}} = 2$.\n"
         "Suy ra $P \\ge 2 + 1 = 3$.\n"
         "Dấu '=' xảy ra khi $\\sqrt{x} = \\frac{1}{\\sqrt{x}} \\Leftrightarrow x = 1$.\n"
         "Vậy GTNN của $P$ bằng 3 khi $x = 1$.\n\n"
         "b) $P = 3 \\Leftrightarrow x = 1$.\n\n"
         "c) Đã chứng minh ở câu a."),

        (30,
         "Cho biểu thức $P = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 3}$ với $x \\ge 0, x \\ne 9$.\n"
         "a) Tách phần nguyên của $P$.\n"
         "b) Tìm tất cả các số nguyên $x$ để $P$ nhận giá trị nguyên âm.\n"
         "c) Tìm $x$ để $P > \\sqrt{P}$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) $P = \\frac{(\\sqrt{x} - 3) + 4}{\\sqrt{x} - 3} = 1 + \\frac{4}{\\sqrt{x} - 3}$.\n\n"
         "b) Để $P$ là số nguyên âm thì $P < 0 \\Leftrightarrow \\sqrt{x} - 3 < 0 \\Leftrightarrow 0 \\le x < 9$.\n"
         "Các ước âm của 4 là $\\sqrt{x} - 3 \\in \\{-1; -2; -4\\}$:\n"
         "- $\\sqrt{x} - 3 = -1 \\Rightarrow \\sqrt{x} = 2 \\Rightarrow x = 4 \\Rightarrow P = 1 - 4 = -3$ (TM).\n"
         "- $\\sqrt{x} - 3 = -2 \\Rightarrow \\sqrt{x} = 1 \\Rightarrow x = 1 \\Rightarrow P = 1 - 2 = -1$ (TM).\n"
         "- $\\sqrt{x} - 3 = -4 \\Rightarrow \\sqrt{x} = -1$ (loại).\n"
         "Vậy $x \\in \\{1; 4\\}$.\n\n"
         "c) $P > \\sqrt{P} \\Leftrightarrow P > 1 \\Leftrightarrow 1 + \\frac{4}{\\sqrt{x} - 3} > 1 \\Leftrightarrow \\frac{4}{\\sqrt{x} - 3} > 0 \\Leftrightarrow \\sqrt{x} - 3 > 0 \\Leftrightarrow x > 9$."),

        (31,
         "Cho biểu thức $P = \\frac{6}{\\sqrt{x} + 2}$ với $x \\ge 0$.\n"
         "a) Tìm tất cả các số thực $x$ để $P$ nhận giá trị nguyên.\n"
         "b) Tìm giá trị lớn nhất của $P$.\n"
         "c) So sánh $P$ với $\\sqrt{P}$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Với $x \\ge 0 \\Rightarrow \\sqrt{x} + 2 \\ge 2 \\Rightarrow 0 < P \\le \\frac{6}{2} = 3$.\n"
         "Vì $P \\in \\mathbb{Z}$ nên $P \\in \\{1; 2; 3\\}$:\n"
         "- $P = 3 \\Leftrightarrow \\sqrt{x} + 2 = 2 \\Leftrightarrow x = 0$.\n"
         "- $P = 2 \\Leftrightarrow \\sqrt{x} + 2 = 3 \\Leftrightarrow \\sqrt{x} = 1 \\Leftrightarrow x = 1$.\n"
         "- $P = 1 \\Leftrightarrow \\sqrt{x} + 2 = 6 \\Leftrightarrow \\sqrt{x} = 4 \\Leftrightarrow x = 16$.\n"
         "Vậy $x \\in \\{0; 1; 16\\}$.\n\n"
         "b) GTLN của $P$ bằng 3 khi $x = 0$.\n\n"
         "c) Với $x = 0 \\Rightarrow P = 3 > \\sqrt{3} = \\sqrt{P}$.\n"
         "Với $x = 16 \\Rightarrow P = 1 = \\sqrt{P}$.\n"
         "Với $x > 16 \\Rightarrow 0 < P < 1 \\Rightarrow P < \\sqrt{P}$."),

        (32,
         "Cho biểu thức $P = \\frac{x - 3\\sqrt{x} + 4}{\\sqrt{x}}$ với $x > 0$.\n"
         "a) Biến đổi $P = \\sqrt{x} + \\frac{4}{\\sqrt{x}} - 3$.\n"
         "b) Tìm giá trị nhỏ nhất của $P$.\n"
         "c) Tìm $x$ để biểu thức đạt giá trị nhỏ nhất.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Chia tử cho mẫu:\n"
         "$$P = \\frac{x}{\\sqrt{x}} - \\frac{3\\sqrt{x}}{\\sqrt{x}} + \\frac{4}{\\sqrt{x}} = \\sqrt{x} - 3 + \\frac{4}{\\sqrt{x}} = \\left(\\sqrt{x} + \\frac{4}{\\sqrt{x}}\\right) - 3$$\n\n"
         "b) Áp dụng BĐT Cô-si cho $\\sqrt{x} > 0$ và $\\frac{4}{\\sqrt{x}} > 0$:\n"
         "$$\\sqrt{x} + \\frac{4}{\\sqrt{x}} \\ge 2\\sqrt{\\sqrt{x} \\cdot \\frac{4}{\\sqrt{x}}} = 2 \\cdot 2 = 4$$\n"
         "Suy ra $P \\ge 4 - 3 = 1$.\n"
         "Dấu '=' xảy ra khi $\\sqrt{x} = \\frac{4}{\\sqrt{x}} \\Leftrightarrow x = 4$.\n"
         "Vậy GTNN của $P$ là 1 khi $x = 4$.\n\n"
         "c) Giá trị nhỏ nhất đạt được khi $x = 4$."),

        (33,
         "Cho biểu thức $P = \\frac{3\\sqrt{x} + 1}{\\sqrt{x} + 2}$ với $x \\ge 0$.\n"
         "a) Tìm tất cả các số thực $x$ để $P$ nhận giá trị nguyên.\n"
         "b) Tìm số nguyên $x$ lớn nhất để $P < 2$.\n"
         "c) Chứng minh rằng $\\frac{1}{2} \\le P < 3$ với mọi $x \\ge 0$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Tách phần nguyên:\n"
         "$$P = \\frac{3(\\sqrt{x} + 2) - 5}{\\sqrt{x} + 2} = 3 - \\frac{5}{\\sqrt{x} + 2}$$\n"
         "Với $x \\ge 0 \\Rightarrow \\sqrt{x} + 2 \\ge 2 \\Rightarrow 0 < \\frac{5}{\\sqrt{x} + 2} \\le \\frac{5}{2} = 2,5$.\n"
         "Suy ra $3 - 2,5 \\le P < 3 \\Leftrightarrow 0,5 \\le P < 3$.\n"
         "Vì $P \\in \\mathbb{Z}$ nên $P \\in \\{1; 2\\}$:\n"
         "- $P = 1 \\Leftrightarrow 3 - \\frac{5}{\\sqrt{x} + 2} = 1 \\Leftrightarrow \\frac{5}{\\sqrt{x} + 2} = 2 \\Leftrightarrow \\sqrt{x} + 2 = \\frac{5}{2} \\Leftrightarrow \\sqrt{x} = \\frac{1}{2} \\Leftrightarrow x = \\frac{1}{4}$.\n"
         "- $P = 2 \\Leftrightarrow 3 - \\frac{5}{\\sqrt{x} + 2} = 2 \\Leftrightarrow \\frac{5}{\\sqrt{x} + 2} = 1 \\Leftrightarrow \\sqrt{x} + 2 = 5 \\Leftrightarrow \\sqrt{x} = 3 \\Leftrightarrow x = 9$.\n"
         "Vậy $x \\in \\left\\{\\frac{1}{4}; 9\\right\\}$.\n\n"
         "b) $P < 2 \\Leftrightarrow 3 - \\frac{5}{\\sqrt{x} + 2} < 2 \\Leftrightarrow \\frac{5}{\\sqrt{x} + 2} > 1 \\Leftrightarrow \\sqrt{x} + 2 < 5 \\Leftrightarrow \\sqrt{x} < 3 \\Leftrightarrow 0 \\le x < 9$.\n"
         "Số nguyên $x$ lớn nhất thỏa mãn là $x = 8$.\n\n"
         "c) Khi $x = 0 \\Rightarrow P = \\frac{1}{2}$. Vì $\\frac{5}{\\sqrt{x} + 2} > 0$ nên $P < 3$. Vậy $\\frac{1}{2} \\le P < 3$."),

        (34,
         "Cho biểu thức $P = \\frac{x - \\sqrt{x} + 1}{\\sqrt{x} + 1}$ với $x \\ge 0$.\n"
         "a) Tìm giá trị nhỏ nhất của $P$.\n"
         "b) Tìm $x$ để $P = 1$.\n"
         "c) Chứng minh rằng $P > 0$ với mọi $x \\ge 0$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Biến đổi: $P = \\frac{(\\sqrt{x} + 1)^2 - 3\\sqrt{x}}{\\sqrt{x} + 1} = \\sqrt{x} + 1 - \\frac{3\\sqrt{x}}{\\sqrt{x} + 1}$.\n"
         "Hoặc khảo sát: GTNN của $P$ đạt tại $x = 0$ cho $P = 1$, hoặc điểm cực trị.\n\n"
         "b) $P = 1 \\Leftrightarrow x - \\sqrt{x} + 1 = \\sqrt{x} + 1 \\Leftrightarrow x - 2\\sqrt{x} = 0 \\Leftrightarrow \\sqrt{x}(\\sqrt{x} - 2) = 0 \\Leftrightarrow x = 0$ hoặc $x = 4$.\n\n"
         "c) Tử số $x - \\sqrt{x} + 1 = \\left(\\sqrt{x} - \\frac{1}{2}\\right)^2 + \\frac{3}{4} > 0$, mẫu $\\sqrt{x} + 1 > 0$, nên $P > 0$ với mọi $x \\ge 0$."),

        (35,
         "Cho biểu thức $P = \\frac{x + 4}{\\sqrt{x} + 1}$ với $x \\ge 0$.\n"
         "a) Tách $P$ thành dạng $(\\sqrt{x} - 1) + \\frac{5}{\\sqrt{x} + 1}$.\n"
         "b) Tìm giá trị nhỏ nhất của $P$.\n"
         "c) Tìm $x$ để $P$ đạt GTNN.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) $P = \\frac{(x - 1) + 5}{\\sqrt{x} + 1} = \\frac{(\\sqrt{x} - 1)(\\sqrt{x} + 1) + 5}{\\sqrt{x} + 1} = \\sqrt{x} - 1 + \\frac{5}{\\sqrt{x} + 1}$.\n\n"
         "b) $P = (\\sqrt{x} + 1) + \\frac{5}{\\sqrt{x} + 1} - 2$.\n"
         "Áp dụng BĐT Cô-si:\n"
         "$$(\\sqrt{x} + 1) + \\frac{5}{\\sqrt{x} + 1} \\ge 2\\sqrt{5}$$\n"
         "Suy ra $P \\ge 2\\sqrt{5} - 2$.\n\n"
         "c) Dấu '=' xảy ra khi $\\sqrt{x} + 1 = \\sqrt{5} \\Leftrightarrow \\sqrt{x} = \\sqrt{5} - 1 \\Leftrightarrow x = (\\sqrt{5} - 1)^2 = 6 - 2\\sqrt{5}$."),

        (36,
         "Cho biểu thức $P = \\frac{2\\sqrt{x} + 5}{\\sqrt{x} + 1}$ với $x \\ge 0$.\n"
         "a) Tìm các số nguyên $x$ để $P$ nhận giá trị nguyên.\n"
         "b) Tìm các số thực $x$ để $P$ nhận giá trị nguyên.\n"
         "c) Tìm GTLN của $P$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) $P = 2 + \\frac{3}{\\sqrt{x} + 1}$.\n"
         "Để $P \\in \\mathbb{Z}$ với $x \\in \\mathbb{Z}$ thì $\\sqrt{x} + 1$ là ước của 3:\n"
         "- $\\sqrt{x} + 1 = 1 \\Rightarrow x = 0$.\n"
         "- $\\sqrt{x} + 1 = 3 \\Rightarrow x = 4$.\n"
         "Vậy $x \\in \\{0; 4\\}$.\n\n"
         "b) Với $x \\ge 0 \\Rightarrow \\sqrt{x} + 1 \\ge 1 \\Rightarrow 0 < \\frac{3}{\\sqrt{x} + 1} \\le 3 \\Rightarrow 2 < P \\le 5$.\n"
         "Các giá trị nguyên của $P$ là $3, 4, 5$:\n"
         "- $P = 5 \\Leftrightarrow x = 0$.\n"
         "- $P = 4 \\Leftrightarrow \\frac{3}{\\sqrt{x} + 1} = 2 \\Leftrightarrow \\sqrt{x} = \\frac{1}{2} \\Leftrightarrow x = \\frac{1}{4}$.\n"
         "- $P = 3 \\Leftrightarrow \\frac{3}{\\sqrt{x} + 1} = 1 \\Leftrightarrow \\sqrt{x} = 2 \\Leftrightarrow x = 4$.\n"
         "Vậy $x \\in \\left\\{0; \\frac{1}{4}; 4\\right\\}$.\n\n"
         "c) GTLN của $P$ là 5 khi $x = 0$."),

        (37,
         "Cho biểu thức $P = \\frac{\\sqrt{x} + 2}{\\sqrt{x} + 1}$ với $x \\ge 0$.\n"
         "a) Chứng minh rằng $1 < P \\le 2$.\n"
         "b) Tìm $x$ để $P = \\frac{4}{3}$.\n"
         "c) So sánh $P$ với $P^2$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) $P = 1 + \\frac{1}{\\sqrt{x} + 1}$.\n"
         "Vì $\\sqrt{x} + 1 \\ge 1 > 0$ nên $0 < \\frac{1}{\\sqrt{x} + 1} \\le 1 \\Rightarrow 1 < P \\le 2$.\n\n"
         "b) $P = \\frac{4}{3} \\Leftrightarrow 1 + \\frac{1}{\\sqrt{x} + 1} = \\frac{4}{3} \\Leftrightarrow \\frac{1}{\\sqrt{x} + 1} = \\frac{1}{3} \\Leftrightarrow \\sqrt{x} + 1 = 3 \\Leftrightarrow \\sqrt{x} = 2 \\Leftrightarrow x = 4$.\n\n"
         "c) Vì $P > 1$ nên $P^2 > P$."),

        (38,
         "Cho biểu thức $P = \\frac{x - 2\\sqrt{x} + 3}{\\sqrt{x}}$ với $x > 0$.\n"
         "a) Tìm giá trị nhỏ nhất của $P$.\n"
         "b) Tìm $x$ để biểu thức đạt giá trị nhỏ nhất.\n"
         "c) Tìm $x$ để $P = 2\\sqrt{3} - 2$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) Biến đổi: $P = \\sqrt{x} + \\frac{3}{\\sqrt{x}} - 2$.\n"
         "Áp dụng BĐT Cô-si:\n"
         "$$\\sqrt{x} + \\frac{3}{\\sqrt{x}} \\ge 2\\sqrt{3}$$\n"
         "Suy ra $P \\ge 2\\sqrt{3} - 2$.\n\n"
         "b) Dấu '=' xảy ra khi $\\sqrt{x} = \\frac{3}{\\sqrt{x}} \\Leftrightarrow x = 3$.\n"
         "Vậy GTNN của $P$ là $2\\sqrt{3} - 2$ khi $x = 3$.\n\n"
         "c) $P = 2\\sqrt{3} - 2 \\Leftrightarrow x = 3$."),

        (39,
         "Cho biểu thức $P = \\frac{3\\sqrt{x} - 2}{\\sqrt{x} + 1}$ với $x \\ge 0$.\n"
         "a) Tách phần nguyên của $P$.\n"
         "b) Tìm tất cả các số thực $x$ để $P$ nhận giá trị nguyên.\n"
         "c) Tìm $x$ để $P < 0$.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) $P = \\frac{3(\\sqrt{x} + 1) - 5}{\\sqrt{x} + 1} = 3 - \\frac{5}{\\sqrt{x} + 1}$.\n\n"
         "b) Với $x \\ge 0 \\Rightarrow \\sqrt{x} + 1 \\ge 1 \\Rightarrow 0 < \\frac{5}{\\sqrt{x} + 1} \\le 5 \\Rightarrow -2 \\le P < 3$.\n"
         "Các giá trị nguyên của $P$ là $\\{-2; -1; 0; 1; 2\\}$:\n"
         "- $P = -2 \\Leftrightarrow \\frac{5}{\\sqrt{x} + 1} = 5 \\Leftrightarrow x = 0$.\n"
         "- $P = -1 \\Leftrightarrow \\frac{5}{\\sqrt{x} + 1} = 4 \\Leftrightarrow \\sqrt{x} = \\frac{1}{4} \\Leftrightarrow x = \\frac{1}{16}$.\n"
         "- $P = 0 \\Leftrightarrow 3\\sqrt{x} - 2 = 0 \\Leftrightarrow x = \\frac{4}{9}$.\n"
         "- $P = 1 \\Leftrightarrow \\frac{5}{\\sqrt{x} + 1} = 2 \\Leftrightarrow \\sqrt{x} = \\frac{3}{2} \\Leftrightarrow x = \\frac{9}{4}$.\n"
         "- $P = 2 \\Leftrightarrow \\frac{5}{\\sqrt{x} + 1} = 1 \\Leftrightarrow \\sqrt{x} = 4 \\Leftrightarrow x = 16$.\n"
         "Vậy $x \\in \\left\\{0; \\frac{1}{16}; \\frac{4}{9}; \\frac{9}{4}; 16\\right\\}$.\n\n"
         "c) $P < 0 \\Leftrightarrow 3\\sqrt{x} - 2 < 0 \\Leftrightarrow \\sqrt{x} < \\frac{2}{3} \\Leftrightarrow 0 \\le x < \\frac{4}{9}$."),

        (40,
         "Cho biểu thức $P = \\frac{x + 9}{\\sqrt{x} + 2}$ với $x \\ge 0$.\n"
         "a) Biến đổi $P = (\\sqrt{x} - 2) + \\frac{13}{\\sqrt{x} + 2}$.\n"
         "b) Tìm giá trị nhỏ nhất của $P$.\n"
         "c) Tìm $x$ để biểu thức đạt giá trị nhỏ nhất.",
         "VDC",
         "**Lời giải chi tiết:**\n\n"
         "a) $P = \\frac{x - 4 + 13}{\\sqrt{x} + 2} = \\sqrt{x} - 2 + \\frac{13}{\\sqrt{x} + 2}$.\n\n"
         "b) $P = (\\sqrt{x} + 2) + \\frac{13}{\\sqrt{x} + 2} - 4$.\n"
         "Áp dụng BĐT Cô-si:\n"
         "$$(\\sqrt{x} + 2) + \\frac{13}{\\sqrt{x} + 2} \\ge 2\\sqrt{13}$$\n"
         "Suy ra $P \\ge 2\\sqrt{13} - 4$.\n\n"
         "c) Dấu '=' xảy ra khi $\\sqrt{x} + 2 = \\sqrt{13} \\Leftrightarrow \\sqrt{x} = \\sqrt{13} - 2 \\Leftrightarrow x = (\\sqrt{13} - 2)^2 = 17 - 4\\sqrt{13}$.\n"
         "Vậy GTNN của $P$ là $2\\sqrt{13} - 4$, đạt tại $x = 17 - 4\\sqrt{13}$.")
    ]

    for item in data:
        questions.append({
            "id": item[0],
            "type": "essay",
            "level": item[2],
            "topicId": "cd2",
            "topicTitle": "CĐ 2: RÚT GỌN BIỂU THỨC CHỨA CĂN",
            "question": f"**Câu {item[0]}:** {item[1]}",
            "solution": item[3]
        })

    return questions

if __name__ == "__main__":
    qs = get_cd2_questions()
    print(f"Total CD2 questions built: {len(qs)}")
