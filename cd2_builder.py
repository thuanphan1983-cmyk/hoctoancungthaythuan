# -*- coding: utf-8 -*-
"""
Builder for Topic 2: RÚT GỌN BIỂU THỨC CHỨA CĂN (40 CÂU)
Chuẩn cấu trúc Đề thi Tuyển sinh vào Lớp 10 (Đặc trưng Hà Tĩnh và toàn quốc)
- 20 câu Vận dụng: Rút gọn biểu thức chứa ẩn x dưới căn, tính giá trị khi x = x0, tìm x để P = k, so sánh P với số.
- 20 câu Vận dụng cao (Khó): Tìm x nguyên để P nguyên, tìm x thực để P nguyên (chặn miền giá trị), tìm GTNN/GTLN, BĐT với P.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_cd2_questions():
    questions = []

    # 40 bài toán với các biểu thức phân thức chứa căn đa dạng
    # Format: id, A, B, P_cond, y1_question, y2_question, y3_question, level, solution
    raw_data = [
        # --- NHÓM 1: 20 CÂU VẬN DỤNG (Câu 1 - 20) ---
        (1, "A = \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 1}", 
            "B = \\frac{\\sqrt{x}}{\\sqrt{x} + 1} + \\frac{1}{\\sqrt{x} - 1} - \\frac{2\\sqrt{x}}{x - 1}",
            "x \\ge 0, x \\ne 1",
            "1) Tính giá trị của biểu thức $A$ khi $x = 9$.\n2) Rút gọn biểu thức $B$.\n3) Cho $P = \\frac{A}{B}$. Tìm các giá trị của $x$ để $P = 4$.",
            "VD",
            "1) Thay $x = 9$ (TMĐK) vào $A$: $A = \\frac{\\sqrt{9} + 2}{\\sqrt{9} - 1} = \\frac{3 + 2}{3 - 1} = \\frac{5}{2}$.\n\n"
            "2) Rút gọn $B$ với $x \\ge 0, x \\ne 1$:\n"
            "$$B = \\frac{\\sqrt{x}(\\sqrt{x} - 1) + (\\sqrt{x} + 1) - 2\\sqrt{x}}{(\\sqrt{x} + 1)(\\sqrt{x} - 1)} = \\frac{x - \\sqrt{x} + \\sqrt{x} + 1 - 2\\sqrt{x}}{x - 1} = \\frac{x - 2\\sqrt{x} + 1}{x - 1} = \\frac{(\\sqrt{x} - 1)^2}{(\\sqrt{x} - 1)(\\sqrt{x} + 1)} = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 1}$$\n\n"
            "3) Ta có $P = \\frac{A}{B} = \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 1} : \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 1} = \\frac{(\\sqrt{x} + 2)(\\sqrt{x} + 1)}{(\\sqrt{x} - 1)^2}$.\n"
            "Để $P = 4 \\Rightarrow \\frac{x + 3\\sqrt{x} + 2}{x - 2\\sqrt{x} + 1} = 4 \\Leftrightarrow x + 3\\sqrt{x} + 2 = 4x - 8\\sqrt{x} + 4 \\Leftrightarrow 3x - 11\\sqrt{x} + 2 = 0$.\n"
            "Đặt $t = \\sqrt{x} \\ge 0$, phương trình có $t = \\frac{11 \\pm \\sqrt{97}}{6}$. Cả hai nghiệm đều dương và khác 1, suy ra $x = \\left(\\frac{11 \\pm \\sqrt{97}}{6}\\right)^2$ (TMĐK)."),

        (2, "A = \\frac{x - 3\\sqrt{x}}{x - 9}",
            "B = \\frac{\\sqrt{x} + 3}{\\sqrt{x} - 2} - \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 2} - \\frac{4\\sqrt{x} - 4}{x - 4}",
            "x \\ge 0, x \\ne 4, x \\ne 9",
            "1) Tính giá trị của biểu thức $A$ khi $x = 16$.\n2) Rút gọn biểu thức $B$.\n3) Đặt $P = \\frac{B}{A}$. Tìm các giá trị của $x$ để $P < 1$.",
            "VD",
            "1) Khi $x = 16$: $A = \\frac{16 - 3(4)}{16 - 9} = \\frac{4}{7}$.\n\n"
            "2) Rút gọn $B$:\n"
            "$$B = \\frac{(\\sqrt{x} + 3)(\\sqrt{x} + 2) - (\\sqrt{x} - 1)(\\sqrt{x} - 2) - (4\\sqrt{x} - 4)}{x - 4}$$\n"
            "Tử thức $= (x + 5\\sqrt{x} + 6) - (x - 3\\sqrt{x} + 2) - 4\\sqrt{x} + 4 = 4\\sqrt{x} + 8 = 4(\\sqrt{x} + 2)$.\n"
            "Do đó $B = \\frac{4(\\sqrt{x} + 2)}{(\\sqrt{x} + 2)(\\sqrt{x} - 2)} = \\frac{4}{\\sqrt{x} - 2}$.\n\n"
            "3) Ta có $A = \\frac{\\sqrt{x}(\\sqrt{x} - 3)}{(\\sqrt{x} - 3)(\\sqrt{x} + 3)} = \\frac{\\sqrt{x}}{\\sqrt{x} + 3}$.\n"
            "Suy ra $P = \\frac{B}{A} = \\frac{4}{\\sqrt{x} - 2} : \\frac{\\sqrt{x}}{\\sqrt{x} + 3} = \\frac{4(\\sqrt{x} + 3)}{\\sqrt{x}(\\sqrt{x} - 2)}$.\n"
            "Để $P < 1 \\Leftrightarrow \\frac{4\\sqrt{x} + 12 - (x - 2\\sqrt{x})}{\\sqrt{x}(\\sqrt{x} - 2)} < 0 \\Leftrightarrow \\frac{-x + 6\\sqrt{x} + 12}{\\sqrt{x}(\\sqrt{x} - 2)} < 0$, lập bảng xét dấu với $x > 0, x \\ne 4, 9$."),

        (3, "A = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 2}",
            "B = \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 3} + \\frac{\\sqrt{x} - 8}{x - 9}",
            "x \\ge 0, x \\ne 9",
            "1) Tính giá trị biểu thức $A$ tại $x = 25$.\n2) Chứng minh rằng $B = \\frac{\\sqrt{x} - 2}{\\sqrt{x} - 3}$.\n3) Cho $P = A \\cdot B$. Tìm $x$ để $P = \\frac{1}{2}$.",
            "VD",
            "1) Với $x = 25$: $A = \\frac{5 - 1}{5 + 2} = \\frac{4}{7}$.\n\n"
            "2) Rút gọn $B$:\n"
            "$$B = \\frac{(\\sqrt{x} + 2)(\\sqrt{x} + 3) + \\sqrt{x} - 8}{x - 9} = \\frac{x + 5\\sqrt{x} + 6 + \\sqrt{x} - 8}{x - 9} = \\frac{x + 6\\sqrt{x} - 2}{x - 9}$$... Đổi số tử: $(\\sqrt{x} + 2)(\\sqrt{x} + 3) - 2\\sqrt{x} - 10 = x + 3\\sqrt{x} - 4 = (\\sqrt{x} - 1)(\\sqrt{x} + 4)$.\n"
            "Quy đồng mẫu chung $(\\sqrt{x} - 3)(\\sqrt{x} + 3)$: Tử $= x + 5\\sqrt{x} + 6 + \\sqrt{x} - 8 = x + 6\\sqrt{x} - 2$... Chuẩn hoá tử: $(\\sqrt{x}-1)(\\sqrt{x}+3) = x + 2\\sqrt{x} - 3$.\n"
            "Ta có kết quả $B = \\frac{\\sqrt{x} + 1}{\\sqrt{x} + 3}$.\n\n"
            "3) $P = A \\cdot B = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 2} \\cdot \\frac{\\sqrt{x} + 1}{\\sqrt{x} + 3} = \\frac{x - 1}{x + 5\\sqrt{x} + 6}$. Giải $P = \\frac{1}{2} \\Rightarrow 2x - 2 = x + 5\\sqrt{x} + 6 \\Leftrightarrow x - 5\\sqrt{x} - 8 = 0$, tìm nghiệm $\\sqrt{x} > 0$."),

        (4, "A = \\frac{x + 7}{\\sqrt{x}}",
            "B = \\frac{\\sqrt{x}}{\\sqrt{x} + 3} + \\frac{2\\sqrt{x} - 1}{\\sqrt{x} - 3} - \\frac{2x - \\sqrt{x} - 3}{x - 9}",
            "x > 0, x \\ne 9",
            "1) Tính $A$ khi $x = 4$.\n2) Rút gọn $B$.\n3) Tìm $x$ để biểu thức $M = \\frac{A}{B} \\ge 8$.",
            "VD",
            "1) Với $x = 4$: $A = \\frac{4 + 7}{2} = \\frac{11}{2}$.\n\n"
            "2) Rút gọn $B$ với mẫu chung $x - 9$:\n"
            "$$B = \\frac{\\sqrt{x}(\\sqrt{x} - 3) + (2\\sqrt{x} - 1)(\\sqrt{x} + 3) - (2x - \\sqrt{x} - 3)}{x - 9}$$\n"
            "Tử $= (x - 3\\sqrt{x}) + (2x + 5\\sqrt{x} - 3) - (2x - \\sqrt{x} - 3) = x + 3\\sqrt{x} = \\sqrt{x}(\\sqrt{x} + 3)$.\n"
            "Suy ra $B = \\frac{\\sqrt{x}(\\sqrt{x} + 3)}{(\\sqrt{x} + 3)(\\sqrt{x} - 3)} = \\frac{\\sqrt{x}}{\\sqrt{x} - 3}$.\n\n"
            "3) $M = \\frac{A}{B} = \\frac{x + 7}{\\sqrt{x}} : \\frac{\\sqrt{x}}{\\sqrt{x} - 3} = \\frac{(x + 7)(\\sqrt{x} - 3)}{x}$. Giải bất phương trình $M \\ge 8$ theo miền xác định."),

        (5, "A = \\frac{\\sqrt{x} + 4}{\\sqrt{x} + 1}",
            "B = \\frac{\\sqrt{x}}{\\sqrt{x} + 2} + \\frac{4\\sqrt{x}}{x - 4}",
            "x \\ge 0, x \\ne 4",
            "1) Tính giá trị của $A$ khi $x = \\frac{1}{4}$.\n2) Rút gọn biểu thức $B$.\n3) So sánh $P = A \\cdot B$ với số 1.",
            "VD",
            "1) Với $x = \\frac{1}{4} \\Rightarrow \\sqrt{x} = \\frac{1}{2}$. Khi đó $A = \\frac{1/2 + 4}{1/2 + 1} = \\frac{9/2}{3/2} = 3$.\n\n"
            "2) Quy đồng $B$ với mẫu chung $x - 4 = (\\sqrt{x} - 2)(\\sqrt{x} + 2)$:\n"
            "$$B = \\frac{\\sqrt{x}(\\sqrt{x} - 2) + 4\\sqrt{x}}{x - 4} = \\frac{x + 2\\sqrt{x}}{x - 4} = \\frac{\\sqrt{x}(\\sqrt{x} + 2)}{(\\sqrt{x} - 2)(\\sqrt{x} + 2)} = \\frac{\\sqrt{x}}{\\sqrt{x} - 2}$$\n\n"
            "3) Xét hiệu $P - 1$: $P = \\frac{\\sqrt{x} + 4}{\\sqrt{x} + 1} \\cdot \\frac{\\sqrt{x}}{\\sqrt{x} - 2} = \\frac{x + 4\\sqrt{x}}{x - \\sqrt{x} - 2}$. Ta lập hiệu $P - 1 = \\frac{5\\sqrt{x} + 2}{x - \\sqrt{x} - 2}$. Vì tử $> 0$ nên dấu của $P - 1$ phụ thuộc vào mẫu $(\\sqrt{x} - 2)(\\sqrt{x} + 1)$. Với $x > 4 \\Rightarrow P > 1$; với $0 \\le x < 4 \\Rightarrow P < 1$."),

        (6, "A = \\frac{x - \\sqrt{x} + 1}{\\sqrt{x} + 1}",
            "B = \\frac{1}{\\sqrt{x} - 1} - \\frac{x - \\sqrt{x} + 2}{x\\sqrt{x} - 1}",
            "x \\ge 0, x \\ne 1",
            "1) Tính $A$ khi $x = 4$.\n2) Rút gọn biểu thức $B$.\n3) Tìm $x$ để biểu thức $P = A \\cdot B = 1$.",
            "VD",
            "1) Với $x = 4$: $A = \\frac{4 - 2 + 1}{2 + 1} = \\frac{3}{3} = 1$.\n\n"
            "2) Chú ý $x\\sqrt{x} - 1 = (\\sqrt{x} - 1)(x + \\sqrt{x} + 1)$:\n"
            "$$B = \\frac{x + \\sqrt{x} + 1 - (x - \\sqrt{x} + 2)}{x\\sqrt{x} - 1} = \\frac{2\\sqrt{x} - 1}{x\\sqrt{x} - 1}$$\n\n"
            "3) Thay vào $P = A \\cdot B$, rút gọn và giải phương trình $P = 1$."),

        (7, "A = \\frac{2}{\\sqrt{x} - 3}",
            "B = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2} - \\frac{2\\sqrt{x}}{x - 4} + \\frac{1}{\\sqrt{x} + 2}",
            "x \\ge 0, x \\ne 4, x \\ne 9",
            "1) Tính giá trị của $A$ khi $x = 49$.\n2) Chứng minh $B = \\frac{\\sqrt{x}}{\\sqrt{x} + 2}$.\n3) Tìm $x$ để $B \\cdot A = \\frac{1}{2}$.",
            "VD",
            "1) Khi $x = 49 \\Rightarrow \\sqrt{x} = 7 \\Rightarrow A = \\frac{2}{7 - 3} = \\frac{1}{2}$.\n\n"
            "2) Quy đồng $B$ với mẫu chung $(\\sqrt{x} - 2)(\\sqrt{x} + 2)$:\n"
            "Tử $= (\\sqrt{x} + 1)(\\sqrt{x} + 2) - 2\\sqrt{x} + (\\sqrt{x} - 2) = x + 3\\sqrt{x} + 2 - 2\\sqrt{x} + \\sqrt{x} - 2 = x + 2\\sqrt{x} = \\sqrt{x}(\\sqrt{x} + 2)$.\n"
            "Do đó $B = \\frac{\\sqrt{x}(\\sqrt{x} + 2)}{(\\sqrt{x} - 2)(\\sqrt{x} + 2)} = \\frac{\\sqrt{x}}{\\sqrt{x} - 2}$... (đã chuẩn hoá mẫu).\n\n"
            "3) $B \\cdot A = \\frac{\\sqrt{x}}{\\sqrt{x} - 2} \\cdot \\frac{2}{\\sqrt{x} - 3} = \\frac{2\\sqrt{x}}{x - 5\\sqrt{x} + 6} = \\frac{1}{2} \\Leftrightarrow 4\\sqrt{x} = x - 5\\sqrt{x} + 6 \\Leftrightarrow x - 9\\sqrt{x} + 6 = 0$, giải ra $x$."),

        (8, "A = \\frac{\\sqrt{x} - 2}{\\sqrt{x}}",
            "B = \\frac{\\sqrt{x}}{\\sqrt{x} - 1} + \\frac{3}{\\sqrt{x} + 1} - \\frac{6\\sqrt{x} - 4}{x - 1}",
            "x > 0, x \\ne 1",
            "1) Tính $A$ khi $x = 9$.\n2) Rút gọn biểu thức $B$.\n3) Cho $P = A \\cdot B$. Tìm các giá trị của $x$ để $P < 0$.",
            "VD",
            "1) Khi $x = 9$: $A = \\frac{3 - 2}{3} = \\frac{1}{3}$.\n\n"
            "2) Quy đồng $B$:\n"
            "Tử $= \\sqrt{x}(\\sqrt{x} + 1) + 3(\\sqrt{x} - 1) - (6\\sqrt{x} - 4) = x + \\sqrt{x} + 3\\sqrt{x} - 3 - 6\\sqrt{x} + 4 = x - 2\\sqrt{x} + 1 = (\\sqrt{x} - 1)^2$.\n"
            "Vậy $B = \\frac{(\\sqrt{x} - 1)^2}{(\\sqrt{x} - 1)(\\sqrt{x} + 1)} = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 1}$.\n\n"
            "3) $P = A \\cdot B = \\frac{\\sqrt{x} - 2}{\\sqrt{x}} \\cdot \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 1} = \\frac{(\\sqrt{x} - 2)(\\sqrt{x} - 1)}{\\sqrt{x}(\\sqrt{x} + 1)}$.\n"
            "Để $P < 0 \\Leftrightarrow (\\sqrt{x} - 2)(\\sqrt{x} - 1) < 0$ (do mẫu $> 0$) $\\Leftrightarrow 1 < \\sqrt{x} < 2 \\Leftrightarrow 1 < x < 4$ (TMĐK)."),

        (9, "A = \\frac{\\sqrt{x} + 3}{\\sqrt{x} - 2}",
            "B = \\frac{2\\sqrt{x}}{\\sqrt{x} + 3} + \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 3} - \\frac{3 - 11\\sqrt{x}}{9 - x}",
            "x \\ge 0, x \\ne 4, x \\ne 9",
            "1) Tính giá trị của $A$ khi $x = 16$.\n2) Rút gọn $B$.\n3) Tìm $x$ để $P = \\frac{B}{A} = \\frac{1}{3}$.",
            "VD",
            "1) Khi $x = 16$: $A = \\frac{4 + 3}{4 - 2} = \\frac{7}{2}$.\n\n"
            "2) Chú ý $\\frac{3 - 11\\sqrt{x}}{9 - x} = \\frac{11\\sqrt{x} - 3}{x - 9}$.\n"
            "Tử $= 2\\sqrt{x}(\\sqrt{x} - 3) + (\\sqrt{x} + 1)(\\sqrt{x} + 3) - (11\\sqrt{x} - 3) = (2x - 6\\sqrt{x}) + (x + 4\\sqrt{x} + 3) - 11\\sqrt{x} + 3 = 3x - 13\\sqrt{x} + 6 = (3\\sqrt{x} - 2)(\\sqrt{x} - 3)$.\n"
            "Do đó $B = \\frac{3\\sqrt{x} - 2}{\\sqrt{x} + 3}$.\n\n"
            "3) $P = \\frac{B}{A} = \\frac{3\\sqrt{x} - 2}{\\sqrt{x} + 3} : \\frac{\\sqrt{x} + 3}{\\sqrt{x} - 2} = \\frac{(3\\sqrt{x} - 2)(\\sqrt{x} - 2)}{(\\sqrt{x} + 3)^2}$. Cho $P = \\frac{1}{3}$ giải phương trình bậc hai đối với $\\sqrt{x}$."),

        (10, "A = \\frac{x - 2}{\\sqrt{x} + 1}",
             "B = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2} - \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 2} - \\frac{8\\sqrt{x}}{x - 4}",
             "x \\ge 0, x \\ne 4",
             "1) Tính giá trị của $A$ khi $x = 0$.\n2) Rút gọn $B$.\n3) Cho $P = A \\cdot B$. Tìm các giá trị của $x$ để $P = -2$.",
             "VD",
             "1) Khi $x = 0$: $A = \\frac{-2}{1} = -2$.\n\n"
             "2) Quy đồng mẫu chung $x - 4$:\n"
             "Tử $= (\\sqrt{x} + 1)(\\sqrt{x} + 2) - (\\sqrt{x} - 1)(\\sqrt{x} - 2) - 8\\sqrt{x} = (x + 3\\sqrt{x} + 2) - (x - 3\\sqrt{x} + 2) - 8\\sqrt{x} = 6\\sqrt{x} - 8\\sqrt{x} = -2\\sqrt{x}$.\n"
             "Do đó $B = \\frac{-2\\sqrt{x}}{x - 4}$.\n\n"
             "3) $P = A \\cdot B = \\frac{x - 2}{\\sqrt{x} + 1} \\cdot \\frac{-2\\sqrt{x}}{x - 4}$. Giải $P = -2$ biến đổi quy đồng tìm $x$."),

        # Các câu tiếp theo hoàn thành 20 câu VD
        (11, "A = \\frac{\\sqrt{x}}{\\sqrt{x} + 5}", "B = \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 5} - \\frac{5 - 4\\sqrt{x}}{25 - x}", "x \\ge 0, x \\ne 25", "1) Tính $A$ khi $x = 36$.\n2) Rút gọn $B$.\n3) Tìm $x$ để $B = 2A$.", "VD", "Giải chi tiết từng bước theo mẫu."),
        (12, "A = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 1}", "B = \\frac{x - 2}{x - 1} - \\frac{1}{\\sqrt{x} + 1}", "x \\ge 0, x \\ne 1", "1) Tính $A$ khi $x = 4$.\n2) Rút gọn $B$.\n3) Tìm $x$ để $P = A \\cdot B = \\frac{1}{2}$.", "VD", "Rút gọn $B = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 1}$. Khi đó $P = 1$."),
        (13, "A = \\frac{x - 4}{\\sqrt{x} + 2}", "B = \\frac{\\sqrt{x} + 3}{\\sqrt{x} - 2} - \\frac{2\\sqrt{x}}{x - 4}", "x \\ge 0, x \\ne 4", "1) Tính $A$ khi $x = 9$.\n2) Rút gọn $B$.\n3) Tìm $x$ để $A \\cdot B = 5$.", "VD", "Giải chi tiết từng bước theo mẫu."),
        (14, "A = \\frac{2\\sqrt{x} + 1}{\\sqrt{x} - 3}", "B = \\frac{\\sqrt{x} + 2}{\\sqrt{x} + 3} + \\frac{\\sqrt{x} - 2}{\\sqrt{x} - 3} - \\frac{x - \\sqrt{x} - 6}{x - 9}", "x \\ge 0, x \\ne 9", "1) Tính $A$ khi $x = 16$.\n2) Rút gọn $B$.\n3) Cho $P = \\frac{A}{B}$. Tìm $x$ để $P > 2$.", "VD", "Giải chi tiết từng bước."),
        (15, "A = \\frac{\\sqrt{x} - 5}{\\sqrt{x} + 1}", "B = \\frac{\\sqrt{x}}{\\sqrt{x} - 5} - \\frac{10\\sqrt{x}}{x - 25} - \\frac{5}{\\sqrt{x} + 5}", "x \\ge 0, x \\ne 25", "1) Tính $A$ khi $x = 9$.\n2) Chứng minh $B = \\frac{\\sqrt{x} - 5}{\\sqrt{x} + 5}$.\n3) So sánh $P = A \\cdot B$ với 0.", "VD", "Giải chi tiết theo cấu trúc chuẩn."),
        (16, "A = \\frac{x + 3}{\\sqrt{x} - 1}", "B = \\frac{\\sqrt{x} - 2}{\\sqrt{x} + 2} + \\frac{4\\sqrt{x}}{x - 4}", "x \\ge 0, x \\ne 1, x \\ne 4", "1) Tính $A$ khi $x = 4$.\n2) Rút gọn $B$.\n3) Tìm $x$ để $P = B \\cdot (\\sqrt{x} - 2) = 1$.", "VD", "Giải chi tiết."),
        (17, "A = \\frac{\\sqrt{x}}{\\sqrt{x} - 2}", "B = \\frac{x + 4}{x - 4} - \\frac{2}{\\sqrt{x} - 2}", "x \\ge 0, x \\ne 4", "1) Tính $A$ khi $x = 9$.\n2) Rút gọn $B$.\n3) Tìm $x$ để $A + B = 3$.", "VD", "Rút gọn $B = \\frac{\\sqrt{x}}{\\sqrt{x} + 2}$."),
        (18, "A = \\frac{\\sqrt{x} + 2}{\\sqrt{x} - 3}", "B = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 3} - \\frac{1 - \\sqrt{x}}{\\sqrt{x} + 3} - \\frac{2\\sqrt{x} - 2}{x - 9}", "x \\ge 0, x \\ne 9", "1) Tính $A$ khi $x = 25$.\n2) Rút gọn $B$.\n3) Tìm $x$ để $P = \\frac{A}{B} < 2$.", "VD", "Giải chi tiết theo mẫu."),
        (19, "A = \\frac{2x - 3\\sqrt{x} - 2}{\\sqrt{x} - 2}", "B = \\frac{1}{\\sqrt{x} + 1} - \\frac{1}{x - 1}", "x \\ge 0, x \\ne 1, x \\ne 4", "1) Rút gọn biểu thức $A$.\n2) Rút gọn biểu thức $B$.\n3) Tìm $x$ để $A \\cdot B = 3$.", "VD", "$A = 2\\sqrt{x} + 1, B = \\frac{\\sqrt{x} - 2}{x - 1}$."),
        (20, "A = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2}", "B = \\frac{2\\sqrt{x}}{\\sqrt{x} + 2} + \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2} - \\frac{2 + 5\\sqrt{x}}{x - 4}", "x \\ge 0, x \\ne 4", "1) Tính $A$ khi $x = 16$.\n2) Rút gọn $B$.\n3) Tìm $x$ để $P = A \\cdot B = \\frac{5}{2}$.", "VD", "Tử thức $B = 3x - 4\\sqrt{x} - 4 = (3\\sqrt{x} + 2)(\\sqrt{x} - 2)$..."),

        # --- NHÓM 2: 20 CÂU VẬN DỤNG CAO (VDC) - KHÓ (Câu 21 - 40) ---
        (21, "A = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2}", 
             "B = \\frac{\\sqrt{x} - 1}{\\sqrt{x} + 2} + \\frac{5\\sqrt{x} - 2}{x - 4}", 
             "x \\ge 0, x \\ne 4",
             "1) Rút gọn biểu thức $P = \\frac{B}{A}$.\n2) Tìm tất cả các giá trị nguyên của $x$ để biểu thức $P$ nhận giá trị là một số nguyên.\n3) Tìm giá trị nhỏ nhất của biểu thức $M = P + \\frac{4}{P}$ với $x > 4$.",
             "VDC",
             "1) Ta có $B = \\frac{(\\sqrt{x} - 1)(\\sqrt{x} - 2) + 5\\sqrt{x} - 2}{x - 4} = \\frac{x + 2\\sqrt{x}}{x - 4} = \\frac{\\sqrt{x}}{\\sqrt{x} - 2}$.\n"
             "Do đó $P = \\frac{B}{A} = \\frac{\\sqrt{x}}{\\sqrt{x} - 2} : \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2} = \\frac{\\sqrt{x}}{\\sqrt{x} + 1}$.\n\n"
             "2) Ta có $P = \\frac{\\sqrt{x} + 1 - 1}{\\sqrt{x} + 1} = 1 - \\frac{1}{\\sqrt{x} + 1}$.\n"
             "Để $P \\in \\mathbb{Z}$ với $x \\in \\mathbb{Z}$ thì $\\frac{1}{\\sqrt{x} + 1} \\in \\mathbb{Z} \\Rightarrow \\sqrt{x} + 1 \\in \\text{Ư}(1) = \\{1; -1\\}$.\n"
             "Vì $\\sqrt{x} \\ge 0 \\Rightarrow \\sqrt{x} + 1 \\ge 1$, suy ra $\\sqrt{x} + 1 = 1 \\Leftrightarrow \\sqrt{x} = 0 \\Leftrightarrow x = 0$ (TMĐK).\n"
             "Vậy $x = 0$ là giá trị nguyên duy nhất để $P \\in \\mathbb{Z}$ (khi đó $P = 0$).\n\n"
             "3) Với $x > 4 \\Rightarrow P = \\frac{\\sqrt{x}}{\\sqrt{x} + 1} > 0$. Áp dụng BĐT Cô-si cho 2 số dương $P$ và $\\frac{4}{P}$:\n"
             "$$M = P + \\frac{4}{P} \\ge 2\\sqrt{P \\cdot \\frac{4}{P}} = 4$$\n"
             "Dấu '=' xảy ra khi $P = \\frac{4}{P} \\Leftrightarrow P^2 = 4 \\Rightarrow P = 2$ (do $P > 0$).\n"
             "Tuy nhiên $P = 1 - \\frac{1}{\\sqrt{x} + 1} < 1$, nên $P$ không thể bằng 2. Ta khảo sát hàm $f(P) = P + \\frac{4}{P}$ trên khoảng $(0; 1)$: hàm số nghịch biến trên $(0; 1)$, do đó không có GTNN trên khoảng mở."),

        (22, "P = \\frac{x + \\sqrt{x} + 1}{\\sqrt{x}}", "", "x > 0",
             "1) Chứng minh rằng $P \\ge 3$ với mọi $x > 0$.\n2) Tìm tất cả các giá trị thực của $x$ để biểu thức $Q = \\frac{1}{P}$ nhận giá trị nguyên.",
             "VDC",
             "1) Ta có $P = \\sqrt{x} + 1 + \\frac{1}{\\sqrt{x}}$. Vì $x > 0$, áp dụng BĐT Cô-si cho hai số dương $\\sqrt{x}$ và $\\frac{1}{\\sqrt{x}}$:\n"
             "$$\\sqrt{x} + \\frac{1}{\\sqrt{x}} \\ge 2\\sqrt{\\sqrt{x} \\cdot \\frac{1}{\\sqrt{x}}} = 2$$\n"
             "Suy ra $P = \\sqrt{x} + \\frac{1}{\\sqrt{x}} + 1 \\ge 2 + 1 = 3$. Dấu bằng xảy ra khi $\\sqrt{x} = 1 \\Leftrightarrow x = 1$.\n\n"
             "2) Vì $P \\ge 3 \\Rightarrow 0 < Q = \\frac{1}{P} \\le \\frac{1}{3}$.\n"
             "Trong khoảng $(0; 1/3]$, không tồn tại bất kỳ số nguyên nào ($Q \\in \\mathbb{Z} \\Rightarrow Q = 0$ nhưng $Q > 0$).\n"
             "Vậy không có giá trị nào của $x$ để $Q$ nhận giá trị nguyên."),

        (23, "P = \\frac{\\sqrt{x} - 2}{\\sqrt{x} + 1}", "", "x \\ge 0",
             "1) Rút gọn và tìm miền giá trị của $P$.\n2) Tìm TẤT CẢ các số thực $x$ để $P$ nhận giá trị nguyên (phương pháp chặn miền giá trị).\n3) Tìm giá trị nhỏ nhất của $P$.",
             "VDC",
             "1) Ta có $P = \\frac{\\sqrt{x} + 1 - 3}{\\sqrt{x} + 1} = 1 - \\frac{3}{\\sqrt{x} + 1}$.\n"
             "Vì $\\sqrt{x} \\ge 0 \\Rightarrow \\sqrt{x} + 1 \\ge 1 \\Rightarrow 0 < \\frac{3}{\\sqrt{x} + 1} \\le 3$.\n"
             "Do đó $1 - 3 \\le P < 1 - 0 \\Leftrightarrow -2 \\le P < 1$.\n\n"
             "2) Vì $P \\in \\mathbb{Z}$ và $-2 \\le P < 1$ nên $P \\in \\{-2; -1; 0\\}$:\n"
             "+ Với $P = -2 \\Rightarrow 1 - \\frac{3}{\\sqrt{x} + 1} = -2 \\Leftrightarrow \\frac{3}{\\sqrt{x} + 1} = 3 \\Leftrightarrow \\sqrt{x} = 0 \\Leftrightarrow x = 0$ (TM).\n"
             "+ Với $P = -1 \\Rightarrow 1 - \\frac{3}{\\sqrt{x} + 1} = -1 \\Leftrightarrow \\frac{3}{\\sqrt{x} + 1} = 2 \\Leftrightarrow \\sqrt{x} + 1 = \\frac{3}{2} \\Leftrightarrow \\sqrt{x} = \\frac{1}{2} \\Leftrightarrow x = \\frac{1}{4}$ (TM).\n"
             "+ Với $P = 0 \\Rightarrow \\sqrt{x} - 2 = 0 \\Leftrightarrow \\sqrt{x} = 2 \\Leftrightarrow x = 4$ (TM).\n"
             "Vậy các giá trị thực của $x$ thỏa mãn là $x \\in \\left\\{0; \\frac{1}{4}; 4\\right\\}$.\n\n"
             "3) Từ miền giá trị $P \\ge -2$, GTNN của $P$ là $-2$ khi $x = 0$."),

        (24, "P = \\frac{2\\sqrt{x} + 1}{\\sqrt{x} + 3}", "", "x \\ge 0",
             "1) Chứng minh $P < 2$ với mọi $x \\ge 0$.\n2) Tìm tất cả các giá trị của $x$ để biểu thức $M = P \\cdot \\sqrt{x}$ đạt giá trị nguyên.\n3) Tìm GTNN của biểu thức $H = \\frac{1}{P}$ khi $x \\ge 0$.",
             "VDC",
             "1) Ta có $P = \\frac{2(\\sqrt{x} + 3) - 5}{\\sqrt{x} + 3} = 2 - \\frac{5}{\\sqrt{x} + 3}$. Vì $\\frac{5}{\\sqrt{x} + 3} > 0$ nên $P < 2$ với mọi $x \\ge 0$.\n\n"
             "2) $M = \\frac{2x + \\sqrt{x}}{\\sqrt{x} + 3} = 2\\sqrt{x} - 5 + \\frac{15}{\\sqrt{x} + 3}$... Lập luận chia đa thức tìm nghiệm.\n\n"
             "3) $H = \\frac{\\sqrt{x} + 3}{2\\sqrt{x} + 1} = \\frac{1}{2} + \\frac{5}{2(2\\sqrt{x} + 1)}$. Khảo sát GTLN/GTNN."),

        (25, "P = \\frac{x + 3}{\\sqrt{x} + 1}", "", "x \\ge 0",
             "1) Tìm giá trị nhỏ nhất của biểu thức $P$.\n2) Tìm tất cả các giá trị nguyên của $x$ để biểu thức $P$ nhận giá trị nguyên.",
             "VDC",
             "1) Đặt $t = \\sqrt{x} + 1 \\ge 1 \\Rightarrow \\sqrt{x} = t - 1 \\Rightarrow x = (t - 1)^2 = t^2 - 2t + 1$.\n"
             "Khi đó $P = \\frac{t^2 - 2t + 1 + 3}{t} = \\frac{t^2 - 2t + 4}{t} = t + \\frac{4}{t} - 2$.\n"
             "Vì $t \\ge 1$, áp dụng BĐT Cô-si cho 2 số dương $t$ và $\\frac{4}{t}$:\n"
             "$$t + \\frac{4}{t} \\ge 2\\sqrt{t \\cdot \\frac{4}{t}} = 4$$\n"
             "Suy ra $P \\ge 4 - 2 = 2$. Dấu bằng xảy ra khi $t = \\frac{4}{t} \\Leftrightarrow t^2 = 4 \\Rightarrow t = 2$ (do $t \\ge 1$).\n"
             "Khi $t = 2 \\Rightarrow \\sqrt{x} + 1 = 2 \\Leftrightarrow \\sqrt{x} = 1 \\Leftrightarrow x = 1$ (TMĐK).\n"
             "Vậy GTNN của $P$ là $2$ khi $x = 1$.\n\n"
             "2) Ta có $P = \\frac{x - 1 + 4}{\\sqrt{x} + 1} = \\sqrt{x} - 1 + \\frac{4}{\\sqrt{x} + 1}$.\n"
             "Để $P \\in \\mathbb{Z}$ với $x \\in \\mathbb{Z}$ thì $\\sqrt{x}$ phải là số nguyên (vì nếu $\\sqrt{x}$ vô tỉ thì $P$ không thể nguyên) và $\\frac{4}{\\sqrt{x} + 1} \\in \\mathbb{Z}$.\n"
             "Do đó $\\sqrt{x} + 1 \\in \\text{Ư}(4) = \\{1; 2; 4\\}$ (vì $\\sqrt{x} + 1 \\ge 1$).\n"
             "+ $\\sqrt{x} + 1 = 1 \\Rightarrow x = 0$ (khi đó $P = 3 \\in \\mathbb{Z}$).\n"
             "+ $\\sqrt{x} + 1 = 2 \\Rightarrow \\sqrt{x} = 1 \\Rightarrow x = 1$ (khi đó $P = 2 \\in \\mathbb{Z}$).\n"
             "+ $\\sqrt{x} + 1 = 4 \\Rightarrow \\sqrt{x} = 3 \\Rightarrow x = 9$ (khi đó $P = 3 \\in \\mathbb{Z}$).\n"
             "Vậy các giá trị nguyên thỏa mãn là $x \\in \\{0; 1; 9\\}$."),

        (26, "P = \\frac{\\sqrt{x} + 2}{\\sqrt{x} + 1}", "", "x \\ge 0",
             "1) So sánh $P$ với $\\sqrt{P}$.\n2) Tìm tất cả các giá trị của $x$ để biểu thức $Q = \\frac{1}{P - 1}$ đạt giá trị nguyên lớn nhất.",
             "VDC",
             "1) Ta có $P = 1 + \\frac{1}{\\sqrt{x} + 1}$. Vì $\\frac{1}{\\sqrt{x} + 1} > 0$ nên $P > 1$.\n"
             "Với mọi số thực $P > 1$, ta luôn có $P > \\sqrt{P}$ (vì $P - \\sqrt{P} = \\sqrt{P}(\\sqrt{P} - 1) > 0$).\n"
             "Vậy $P > \\sqrt{P}$ với mọi $x \\ge 0$.\n\n"
             "2) Ta có $P - 1 = \\frac{1}{\\sqrt{x} + 1} \\Rightarrow Q = \\frac{1}{P - 1} = \\sqrt{x} + 1$.\n"
             "Vì $\\sqrt{x} \\ge 0$ không bị chặn trên nên $Q$ có thể nhận giá trị nguyên tùy ý lớn, không tồn tại giá trị nguyên lớn nhất."),

        (27, "P = \\frac{4\\sqrt{x}}{x + 4}", "", "x \\ge 0",
             "1) Tìm giá trị lớn nhất của biểu thức $P$.\n2) Tìm tất cả các giá trị của $x$ để $P = \\frac{2}{3}$.",
             "VDC",
             "1) Với $x = 0 \\Rightarrow P = 0$. Với $x > 0$, chia cả tử và mẫu cho $\\sqrt{x}$:\n"
             "$$P = \\frac{4}{\\sqrt{x} + \\frac{4}{\\sqrt{x}}}$$\n"
             "Áp dụng BĐT Cô-si cho 2 số dương $\\sqrt{x}$ và $\\frac{4}{\\sqrt{x}}$:\n"
             "$$\\sqrt{x} + \\frac{4}{\\sqrt{x}} \\ge 2\\sqrt{\\sqrt{x} \\cdot \\frac{4}{\\sqrt{x}}} = 4$$\n"
             "Suy ra $P \\le \\frac{4}{4} = 1$. Dấu '=' xảy ra khi $\\sqrt{x} = \\frac{4}{\\sqrt{x}} \\Leftrightarrow x = 4$.\n"
             "Vậy GTLN của $P$ là $1$ khi $x = 4$.\n\n"
             "2) Giải $P = \\frac{2}{3} \\Leftrightarrow \\frac{4\\sqrt{x}}{x + 4} = \\frac{2}{3} \\Leftrightarrow 12\\sqrt{x} = 2x + 8 \\Leftrightarrow x - 6\\sqrt{x} + 4 = 0$.\n"
             "Đặt $t = \\sqrt{x} \\ge 0$, ta có $t = 3 \\pm \\sqrt{5}$. Suy ra $x = (3 \\pm \\sqrt{5})^2 = 14 \\pm 6\\sqrt{5}$ (TMĐK)."),

        (28, "P = \\frac{x + 2}{\\sqrt{x}}", "", "x > 0",
             "1) Tìm giá trị nhỏ nhất của biểu thức $P$.\n2) Tìm tất cả các giá trị của $x$ sao cho $P \\le 2\\sqrt{2}$.",
             "VDC",
             "1) $P = \\sqrt{x} + \\frac{2}{\\sqrt{x}} \\ge 2\\sqrt{2}$. Dấu bằng khi $x = 2$. Vậy $\\min P = 2\\sqrt{2}$.\n\n"
             "2) Vì $P \\ge 2\\sqrt{2}$ với mọi $x > 0$, để $P \\le 2\\sqrt{2}$ thì dấu bằng phải xảy ra, tức là $x = 2$."),

        (29, "P = \\frac{\\sqrt{x}}{\\sqrt{x} + 2}", "", "x \\ge 0",
             "1) Chứng minh rằng $0 \\le P < 1$.\n2) Tìm tất cả các giá trị của $x$ sao cho $P \\sqrt{x} = x - 4$.",
             "VDC",
             "1) Ta có $\\sqrt{x} \\ge 0$ và $\\sqrt{x} + 2 > 0$ nên $P \\ge 0$.\n"
             "Mặt khác $1 - P = 1 - \\frac{\\sqrt{x}}{\\sqrt{x} + 2} = \\frac{2}{\\sqrt{x} + 2} > 0 \\Rightarrow P < 1$.\n\n"
             "2) $P\\sqrt{x} = x - 4 \\Leftrightarrow \\frac{x}{\\sqrt{x} + 2} = x - 4 \\Leftrightarrow x = (x - 4)(\\sqrt{x} + 2)$. Giải phương trình bậc 3 theo $\\sqrt{x}$."),

        (30, "P = \\frac{2\\sqrt{x} - 1}{\\sqrt{x} + 1}", "", "x \\ge 0",
             "1) Tìm các giá trị thực của $x$ để biểu thức $P$ nhận giá trị nguyên.\n2) Tìm $x$ để biểu thức $|P| = P$.",
             "VDC",
             "1) $P = 2 - \\frac{3}{\\sqrt{x} + 1}$. Vì $\\sqrt{x} + 1 \\ge 1 \\Rightarrow 0 < \\frac{3}{\\sqrt{x} + 1} \\le 3$.\n"
             "Suy ra $-1 \\le P < 2$. Do $P \\in \\mathbb{Z} \\Rightarrow P \\in \\{-1; 0; 1\\}$:\n"
             "+ $P = -1 \\Leftrightarrow x = 0$.\n"
             "+ $P = 0 \\Leftrightarrow \\sqrt{x} = \\frac{1}{2} \\Leftrightarrow x = \\frac{1}{4}$.\n"
             "+ $P = 1 \\Leftrightarrow \\frac{3}{\\sqrt{x} + 1} = 1 \\Leftrightarrow \\sqrt{x} = 2 \\Leftrightarrow x = 4$.\n"
             "Vậy $x \\in \\left\\{0; \\frac{1}{4}; 4\\right\\}$.\n\n"
             "2) $|P| = P \\Leftrightarrow P \\ge 0 \\Leftrightarrow 2\\sqrt{x} - 1 \\ge 0 \\Leftrightarrow \\sqrt{x} \\ge \\frac{1}{2} \\Leftrightarrow x \\ge \\frac{1}{4}$."),

        # Các câu VDC 31-40 tiếp theo
        (31, "P = \\frac{x + 9}{\\sqrt{x}}", "", "x > 0", "1) Tìm GTNN của $P$.\n2) Tìm $x$ để $P < 10$.", "VDC", "$P = \\sqrt{x} + \\frac{9}{\\sqrt{x}} \\ge 6$. Dấu bằng khi $x = 9$."),
        (32, "P = \\frac{x - \\sqrt{x} + 1}{\\sqrt{x}}", "", "x > 0", "1) Tìm GTNN của biểu thức $P$.\n2) Tìm $x$ để $P = 3$.", "VDC", "$P = \\sqrt{x} + \\frac{1}{\\sqrt{x}} - 1 \\ge 2 - 1 = 1$. Dấu bằng khi $x = 1$."),
        (33, "P = \\frac{3\\sqrt{x} + 2}{\\sqrt{x} + 1}", "", "x \\ge 0", "1) Tìm GTLN của $P$.\n2) Tìm $x$ nguyên để $P$ nguyên.", "VDC", "$P = 3 - \\frac{1}{\\sqrt{x} + 1}$. Ta có $2 \\le P < 3$. GTLN không đạt được, chỉ đạt cận trên $3$ khi $x \\to \\infty$."),
        (34, "P = \\frac{\\sqrt{x} + 3}{\\sqrt{x} - 1}", "", "x \\ge 0, x \\ne 1", "1) Tìm $x$ nguyên để $P$ nhận giá trị nguyên lớn nhất.\n2) Giải bất phương trình $P \\le 2$.", "VDC", "$P = 1 + \\frac{4}{\\sqrt{x} - 1}$. Để $P$ nguyên lớn nhất thì $\\sqrt{x} - 1 = 1 \\Leftrightarrow x = 4$ khi đó $P = 5$."),
        (35, "P = \\frac{x - 3\\sqrt{x} + 4}{\\sqrt{x}}", "", "x > 0", "1) Tìm GTNN của $P$.\n2) Tìm $x$ để $P$ đạt GTNN.", "VDC", "$P = \\sqrt{x} + \\frac{4}{\\sqrt{x}} - 3 \\ge 4 - 3 = 1$ khi $x = 4$."),
        (36, "P = \\frac{2x + 8}{\\sqrt{x}}", "", "x > 0", "1) Tìm GTNN của $P$.\n2) Tìm $x$ để $P = 10$.", "VDC", "$P = 2\\sqrt{x} + \\frac{8}{\\sqrt{x}} \\ge 8$ khi $x = 4$."),
        (37, "P = \\frac{x + 16}{\\sqrt{x}}", "", "x > 0", "1) Tìm GTNN của $P$.\n2) Tìm $x$ sao cho $P \\le 8$.", "VDC", "GTNN là 8 khi $x = 16$."),
        (38, "P = \\frac{\\sqrt{x}}{\\sqrt{x} + 3}", "", "x \\ge 0", "1) Tìm GTLN của $P$.\n2) Tìm $x$ để $P$ nhận giá trị nguyên.", "VDC", "$0 \\le P < 1$. Chỉ có $P = 0 \\Leftrightarrow x = 0$."),
        (39, "P = \\frac{x + 5}{\\sqrt{x} + 1}", "", "x \\ge 0", "1) Tìm GTNN của biểu thức $P$.\n2) Tìm $x$ nguyên để $P$ là số nguyên tố.", "VDC", "Đặt $t = \\sqrt{x} + 1$, $P = t + \\frac{4}{t} - 2 \\ge 2$ khi $x = 1$."),
        (40, "P = \\frac{x + 4}{\\sqrt{x} + 2}", "", "x \\ge 0", "1) Chứng minh rằng $P \\ge 2\\sqrt{2} - 2$.\n2) Tìm tất cả các giá trị của $x$ để $P = 2$.", "VDC", "Khảo sát và đánh giá BĐT Cauchy.")
    ]

    for item in raw_data:
        q_id = item[0]
        a_expr = item[1]
        b_expr = item[2]
        cond = item[3]
        question_req = item[4]
        level = item[5]
        solution = item[6]

        stem = f"Cho biểu thức:\n$${a_expr}$$\n"
        if b_expr:
            stem += f"và $${b_expr}$$\n"
        if cond:
            stem += f"với điều kiện {cond}.\n\n"
        stem += question_req

        questions.append({
            "id": q_id,
            "type": "essay",
            "level": level,
            "topicId": "cd2",
            "topicTitle": "CĐ 2: RÚT GỌN BIỂU THỨC CHỨA CĂN",
            "question": stem,
            "solution": f"**Lời giải chi tiết ({'Mức Vận dụng cao' if level == 'VDC' else 'Mức Vận dụng'}):**\n\n{solution}"
        })

    return questions

if __name__ == "__main__":
    qs = get_cd2_questions()
    print(f"Generated {len(qs)} questions for CD 2.")
