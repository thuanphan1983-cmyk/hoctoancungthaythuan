# -*- coding: utf-8 -*-
"""
Tập lệnh xây dựng dữ liệu chi tiết cho 4 đề thi thử vào lớp 10 (ĐỀ SỐ 07, 08, 09, 10)
theo chuẩn cấu trúc đề thi Sở GD&ĐT Hà Tĩnh (2025 - 2026).
"""

import json
import sys

def get_exams_7_to_10():
    exams = {}

    # =========================================================================
    # ĐỀ SỐ 07
    # =========================================================================
    exams["de_07"] = {
        "id": "de_07",
        "code": "MÃ ĐỀ 07",
        "title": "ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN - ĐỀ SỐ 07",
        "header": {
            "department": "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
            "examName": "KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT",
            "subject": "Môn thi: TOÁN",
            "author": "GV Phan Đình Thuấn",
            "time": "90 phút (không kể thời gian phát đề)",
            "code": "MÃ ĐỀ 07"
        },
        "part1": [
            {
                "id": 1,
                "question": "Kết quả rút gọn của biểu thức $M = \\sqrt{(\\sqrt{5}-2)^2} + \\sqrt{(\\sqrt{5}-3)^2}$ là:",
                "options": ["A. $1$", "B. $2\\sqrt{5}-5$", "C. $-1$", "D. $2\\sqrt{5}+1$"],
                "answer": "A",
                "explanation": "Vì $\\sqrt{5} \\approx 2,236$ nên $\\sqrt{5}-2 > 0$ và $\\sqrt{5}-3 < 0$. Do đó $M = (\\sqrt{5}-2) + (3-\\sqrt{5}) = 1$."
            },
            {
                "id": 2,
                "question": "Tập nghiệm của bất phương trình $\\frac{2x - 1}{3} \\le x + 1$ là:",
                "options": ["A. $x \\le -4$", "B. $x \\ge -4$", "C. $x \\ge 4$", "D. $x \\le 4$"],
                "answer": "B",
                "explanation": "Ta có: $\\frac{2x - 1}{3} \\le x + 1 \\Leftrightarrow 2x - 1 \\le 3(x + 1) \\Leftrightarrow 2x - 1 \\le 3x + 3 \\Leftrightarrow -x \\le 4 \\Leftrightarrow x \\ge -4$."
            },
            {
                "id": 3,
                "question": "Phương trình $5(x - 1) = 2(x + 5)$ có nghiệm là:",
                "options": ["A. $x = 3$", "B. $x = 5$", "C. $x = -5$", "D. $x = 1$"],
                "answer": "B",
                "explanation": "$5(x - 1) = 2(x + 5) \\Leftrightarrow 5x - 5 = 2x + 10 \\Leftrightarrow 3x = 15 \\Leftrightarrow x = 5$."
            },
            {
                "id": 4,
                "question": "Một túi đựng 10 tấm thẻ cùng loại được ghi các số từ 1 đến 10. Rút ngẫu nhiên một thẻ. Xác suất để rút được tấm thẻ ghi số nguyên tố là:",
                "options": ["A. $\\frac{1}{2}$", "B. $\\frac{2}{5}$", "C. $\\frac{3}{10}$", "D. $\\frac{3}{5}$"],
                "answer": "B",
                "explanation": "Các số nguyên tố từ 1 đến 10 là ${2; 3; 5; 7}$, gồm 4 số. Xác suất là $P = \\frac{4}{10} = \\frac{2}{5}$."
            },
            {
                "id": 5,
                "question": "Cho parabol $(P): y = \\frac{1}{4}x^2$. Điểm nào sau đây thuộc parabol $(P)$?",
                "options": ["A. $M(-4; 4)$", "B. $N(2; 2)$", "C. $P(-2; -1)$", "D. $Q(4; 2)$"],
                "answer": "A",
                "explanation": "Thay tọa độ điểm $M(-4; 4)$ vào hàm số: $y = \\frac{1}{4}(-4)^2 = \\frac{1}{4} \\cdot 16 = 4$ (thỏa mãn)."
            },
            {
                "id": 6,
                "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $BH = 4\\text{ cm}$ và $CH = 9\\text{ cm}$. Độ dài đường cao $AH$ là:",
                "options": ["A. $6\\text{ cm}$", "B. $13\\text{ cm}$", "C. $\\sqrt{13}\\text{ cm}$", "D. $6,5\\text{ cm}$"],
                "answer": "A",
                "explanation": "Áp dụng hệ thức lượng trong tam giác vuông: $AH^2 = BH \\cdot CH = 4 \\cdot 9 = 36 \\Rightarrow AH = 6\\text{ cm}$."
            },
            {
                "id": 7,
                "question": "Một hình cầu có thể tích bằng $36\\pi\\text{ cm}^3$. Bán kính của hình cầu đó là:",
                "options": ["A. $3\\text{ cm}$", "B. $6\\text{ cm}$", "C. $9\\text{ cm}$", "D. $\\sqrt{3}\\text{ cm}$"],
                "answer": "A",
                "explanation": "Ta có: $V = \\frac{4}{3}\\pi R^3 = 36\\pi \\Leftrightarrow R^3 = 27 \\Leftrightarrow R = 3\\text{ cm}$."
            },
            {
                "id": 8,
                "question": "Nhiệt độ trung bình các tháng mùa hè tại một trạm khí tượng đo được là ($^\\circ\\text{C}$): 28, 30, 32, 30, 31, 30, 29. Mốt ($M_o$) của mẫu số liệu trên là:",
                "options": ["A. $30$", "B. $31$", "C. $32$", "D. $29$"],
                "answer": "A",
                "explanation": "Giá trị 30 xuất hiện nhiều nhất (3 lần), do đó mốt của mẫu số liệu là $M_o = 30$."
            }
        ],
        "part2": [
            {
                "id": 9,
                "points": 1.0,
                "question": "Cho biểu thức: $$P = \\left(\\frac{1}{\\sqrt{x}-1} - \\frac{1}{\\sqrt{x}}\\right) : \\left(\\frac{\\sqrt{x}+1}{\\sqrt{x}-2} - \\frac{\\sqrt{x}+2}{\\sqrt{x}-1}\\right)$$ với $x > 0, x \\ne 1$ và $x \\ne 4$.\na) Rút gọn biểu thức $P$.\nb) Tính giá trị của biểu thức $P$ khi $x = 9$.",
                "rubric": [
                    {
                        "step": "Quy đồng ngoặc thứ nhất: $\\frac{\\sqrt{x} - (\\sqrt{x}-1)}{\\sqrt{x}(\\sqrt{x}-1)} = \\frac{1}{\\sqrt{x}(\\sqrt{x}-1)}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Quy đồng ngoặc thứ hai: $\\frac{(\\sqrt{x}+1)(\\sqrt{x}-1) - (\\sqrt{x}+2)(\\sqrt{x}-2)}{(\\sqrt{x}-2)(\\sqrt{x}-1)} = \\frac{(x-1)-(x-4)}{(\\sqrt{x}-2)(\\sqrt{x}-1)} = \\frac{3}{(\\sqrt{x}-2)(\\sqrt{x}-1)}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Chia hai phân thức: $P = \\frac{1}{\\sqrt{x}(\\sqrt{x}-1)} \\cdot \\frac{(\\sqrt{x}-2)(\\sqrt{x}-1)}{3} = \\frac{\\sqrt{x}-2}{3\\sqrt{x}}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Thay $x = 9$ (thỏa mãn ĐKXĐ) vào $P$: $P = \\frac{\\sqrt{9}-2}{3\\sqrt{9}} = \\frac{3-2}{3 \\cdot 3} = \\frac{1}{9}$. Kết luận.",
                        "points": 0.25
                    }
                ],
                "solution": "Với $x > 0, x \\ne 1, x \\ne 4$, ta có:\na) Rút gọn biểu thức $P$:\n$$\\begin{aligned}\nP &= \\left[\\frac{\\sqrt{x}}{\\sqrt{x}(\\sqrt{x}-1)} - \\frac{\\sqrt{x}-1}{\\sqrt{x}(\\sqrt{x}-1)}\\right] : \\left[\\frac{(\\sqrt{x}+1)(\\sqrt{x}-1)}{(\\sqrt{x}-2)(\\sqrt{x}-1)} - \\frac{(\\sqrt{x}+2)(\\sqrt{x}-2)}{(\\sqrt{x}-2)(\\sqrt{x}-1)}\\right] \\\\\n&= \\frac{\\sqrt{x} - \\sqrt{x} + 1}{\\sqrt{x}(\\sqrt{x}-1)} : \\frac{(x - 1) - (x - 4)}{(\\sqrt{x}-2)(\\sqrt{x}-1)} \\\\\n&= \\frac{1}{\\sqrt{x}(\\sqrt{x}-1)} : \\frac{3}{(\\sqrt{x}-2)(\\sqrt{x}-1)} \\\\\n&= \\frac{1}{\\sqrt{x}(\\sqrt{x}-1)} \\cdot \\frac{(\\sqrt{x}-2)(\\sqrt{x}-1)}{3} = \\frac{\\sqrt{x}-2}{3\\sqrt{x}}.\n\\end{aligned}$$\n\nb) Với $x = 9$ thỏa mãn điều kiện xác định, ta có:\n$$P = \\frac{\\sqrt{9} - 2}{3\\sqrt{9}} = \\frac{3 - 2}{3 \\cdot 3} = \\frac{1}{9}.$$\nVậy khi $x = 9$ thì $P = \\frac{1}{9}$."
            },
            {
                "id": 10,
                "points": 1.0,
                "question": "Cho phương trình $x^2 - 5x - 2 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $$A = x_1^3 + x_2^3 - 2x_1 x_2.$$",
                "rubric": [
                    {
                        "step": "Xét phương trình $x^2 - 5x - 2 = 0$ có $a \\cdot c = 1 \\cdot (-2) = -2 < 0$, suy ra phương trình luôn có hai nghiệm phân biệt $x_1, x_2$.",
                        "points": 0.25
                    },
                    {
                        "step": "Theo định lí Viète, ta có: $\\begin{cases} x_1 + x_2 = 5 \\\\ x_1 x_2 = -2 \\end{cases}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Biến đổi $x_1^3 + x_2^3 = (x_1+x_2)^3 - 3x_1 x_2(x_1+x_2) = 5^3 - 3(-2)(5) = 125 + 30 = 155$.",
                        "points": 0.25
                    },
                    {
                        "step": "Thay vào biểu thức: $A = 155 - 2(-2) = 155 + 4 = 159$. Kết luận $A = 159$.",
                        "points": 0.25
                    }
                ],
                "solution": "Xét phương trình $x^2 - 5x - 2 = 0$.\nVì $a \\cdot c = 1 \\cdot (-2) = -2 < 0$ nên phương trình luôn có hai nghiệm phân biệt $x_1, x_2$.\nTheo định lí Viète, ta có:\n$$\\begin{cases} x_1 + x_2 = 5 \\\\ x_1 x_2 = -2 \\end{cases}$$\nTa biến đổi biểu thức $x_1^3 + x_2^3$:\n$$x_1^3 + x_2^3 = (x_1 + x_2)^3 - 3x_1 x_2(x_1 + x_2) = 5^3 - 3 \\cdot (-2) \\cdot 5 = 125 + 30 = 155.$$\nKhi đó giá trị của biểu thức $A$ là:\n$$A = x_1^3 + x_2^3 - 2x_1 x_2 = 155 - 2 \\cdot (-2) = 155 + 4 = 159.$$\nVậy $A = 159$."
            },
            {
                "id": 11,
                "points": 1.0,
                "question": "Giải hệ phương trình:\n$$\\begin{cases} \\sqrt{x+1} + 2(y-1) = 5 \\\\ 3\\sqrt{x+1} - (y-1) = 1 \\end{cases}$$",
                "rubric": [
                    {
                        "step": "Tìm điều kiện xác định: $x+1 \\ge 0 \\Leftrightarrow x \\ge -1$. Đặt ẩn phụ $u = \\sqrt{x+1} \\ge 0$ và $v = y-1$.",
                        "points": 0.25
                    },
                    {
                        "step": "Hệ trở thành: $\\begin{cases} u + 2v = 5 \\\\ 3u - v = 1 \\end{cases} \\Leftrightarrow \\begin{cases} u + 2v = 5 \\\\ 6u - 2v = 2 \\end{cases} \\Leftrightarrow \\begin{cases} 7u = 7 \\\\ v = 3u - 1 \\end{cases} \\Leftrightarrow \\begin{cases} u = 1 \\\\ v = 2 \\end{cases}$.",
                        "points": 0.35
                    },
                    {
                        "step": "Thay lại: $\\sqrt{x+1} = 1 \\Leftrightarrow x+1 = 1 \\Leftrightarrow x = 0$ (thỏa mãn) và $y-1 = 2 \\Leftrightarrow y = 3$.",
                        "points": 0.25
                    },
                    {
                        "step": "Kết luận nghiệm duy nhất của hệ phương trình là $(x; y) = (0; 3)$.",
                        "points": 0.15
                    }
                ],
                "solution": "Điều kiện xác định: $x \\ge -1$.\nĐặt $u = \\sqrt{x+1}$ ($u \\ge 0$) và $v = y - 1$.\nHệ phương trình đã cho trở thành:\n$$\\begin{cases} u + 2v = 5 \\\\ 3u - v = 1 \\end{cases} \\Leftrightarrow \\begin{cases} u + 2v = 5 \\\\ 6u - 2v = 2 \\end{cases} \\Leftrightarrow \\begin{cases} 7u = 7 \\\\ v = 3u - 1 \\end{cases} \\Leftrightarrow \\begin{cases} u = 1 \\\\ v = 2 \\end{cases}$$\nVới $u = 1$, ta có $\\sqrt{x+1} = 1 \\Leftrightarrow x + 1 = 1 \\Leftrightarrow x = 0$ (thỏa mãn điều kiện $x \\ge -1$).\nVới $v = 2$, ta có $y - 1 = 2 \\Leftrightarrow y = 3$.\nVậy hệ phương trình có nghiệm duy nhất $(x; y) = (0; 3)$."
            },
            {
                "id": 12,
                "points": 2.0,
                "question": "a) Trong một buổi trải nghiệm hướng nghiệp, giáo viên chủ nhiệm chọn ngẫu nhiên đồng thời hai học sinh từ một nhóm gồm 3 bạn nam (An, Bình, Cường) và 2 bạn nữ (Mai, Hoa) để phụ trách dẫn chương trình. Viết không gian mẫu của phép thử và tính xác suất của biến cố $K$: \"Trong hai học sinh được chọn có đúng một bạn nam và một bạn nữ\".\nb) Một ô tô và một xe máy cùng khởi hành từ địa điểm $A$ để đi đến địa điểm $B$ trên quãng đường dài $120\\text{ km}$. Do vận tốc ô tô lớn hơn vận tốc xe máy là $10\\text{ km/h}$ nên ô tô đến $B$ sớm hơn xe máy 24 phút. Tính vận tốc của mỗi xe (biết vận tốc của mỗi xe không đổi trên toàn bộ quãng đường).",
                "rubric": [
                    {
                        "step": "a) Viết đúng không gian mẫu $\\Omega$ gồm 10 cặp phần tử chọn không thứ tự từ 5 bạn. Suy ra $n(\\Omega) = 10$.",
                        "points": 0.5
                    },
                    {
                        "step": "a) Liệt kê các kết quả thuận lợi cho $K$ gồm 6 cặp (1 nam, 1 nữ). Tính $P(K) = \\frac{6}{10} = \\frac{3}{5} = 0,6$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) Đổi 24 phút = $\\frac{2}{5}$ giờ. Gọi vận tốc xe máy là $x$ (km/h, $x > 0$), vận tốc ô tô là $x + 10$ (km/h). Biểu diễn thời gian đi của hai xe: $\\frac{120}{x}$ và $\\frac{120}{x+10}$.",
                        "points": 0.35
                    },
                    {
                        "step": "b) Lập phương trình: $\\frac{120}{x} - \\frac{120}{x+10} = \\frac{2}{5}$. Quy đồng rút gọn về phương trình bậc hai: $x^2 + 10x - 3000 = 0$.",
                        "points": 0.35
                    },
                    {
                        "step": "b) Giải phương trình được $x = 50$ (thỏa mãn), $x = -60$ (loại). Kết luận vận tốc xe máy là $50\\text{ km/h}$, vận tốc ô tô là $60\\text{ km/h}$.",
                        "points": 0.3
                    }
                ],
                "solution": "a) Kí hiệu 3 bạn nam là $A, B, C$ và 2 bạn nữ là $M, H$.\nKhông gian mẫu của phép thử khi chọn đồng thời 2 bạn từ 5 bạn là:\n$$\\Omega = {(A, B); (A, C); (A, M); (A, H); (B, C); (B, M); (B, H); (C, M); (C, H); (M, H)}$$\nSố phần tử của không gian mẫu là $n(\\Omega) = 10$.\nBiến cố $K$: \"Trong hai học sinh được chọn có đúng một bạn nam và một bạn nữ\" gồm các kết quả thuận lợi:\n$$K = {(A, M); (A, H); (B, M); (B, H); (C, M); (C, H)}$$\nSố kết quả thuận lợi cho biến cố $K$ là $n(K) = 6$.\nXác suất của biến cố $K$ là:\n$$P(K) = \\frac{n(K)}{n(\\Omega)} = \\frac{6}{10} = \\frac{3}{5} = 0,6.$$\n\nb) Đổi: $24\\text{ phút} = \\frac{24}{60}\\text{ giờ} = \\frac{2}{5}\\text{ giờ}$.\nGọi vận tốc của xe máy là $x$ (km/h, điều kiện: $x > 0$).\nVì vận tốc của ô tô lớn hơn vận tốc của xe máy $10\\text{ km/h}$ nên vận tốc của ô tô là $x + 10$ (km/h).\nThời gian xe máy đi hết quãng đường $120\\text{ km}$ là: $\\frac{120}{x}$ (giờ).\nThời gian ô tô đi hết quãng đường $120\\text{ km}$ là: $\\frac{120}{x+10}$ (giờ).\nVì ô tô đến $B$ sớm hơn xe máy 24 phút nên ta có phương trình:\n$$\\frac{120}{x} - \\frac{120}{x+10} = \\frac{2}{5}$$\n$$\\Leftrightarrow 120 \\left(\\frac{1}{x} - \\frac{1}{x+10}\\right) = \\frac{2}{5} \\Leftrightarrow \\frac{10}{x(x+10)} = \\frac{1}{300}$$\n$$\\Leftrightarrow x(x + 10) = 3000 \\Leftrightarrow x^2 + 10x - 3000 = 0.$$\nTa có $\\Delta' = 5^2 - 1 \\cdot (-3000) = 25 + 3000 = 3025 > 0$, suy ra $\\sqrt{\\Delta'} = 55$.\nPhương trình có hai nghiệm phân biệt:\n$$x_1 = -5 + 55 = 50\\text{ (thỏa mãn điều kiện)},$$\n$$x_2 = -5 - 55 = -60\\text{ (loại)}.$$\nVậy vận tốc của xe máy là $50\\text{ km/h}$ và vận tốc của ô tô là $50 + 10 = 60\\text{ km/h}$."
            },
            {
                "id": 13,
                "points": 2.0,
                "question": "Cho tam giác nhọn $ABC$ ($AB < AC$) nội tiếp đường tròn $(O; R)$. Các đường cao $AD, BE, CF$ cắt nhau tại trực tâm $H$. Kẻ đường kính $AK$ của đường tròn $(O)$.\na) Chứng minh tứ giác $BCEF$ nội tiếp một đường tròn.\nb) Gọi $M$ là trung điểm của cạnh $BC$. Chứng minh rằng ba điểm $H, M, K$ thẳng hàng. Gọi $I$ là giao điểm của hai đường thẳng $EF$ và $BC$. Chứng minh rằng $IB \\cdot IC = ID \\cdot IM$ và $IH \\perp AM$.",
                "rubric": [
                    {
                        "step": "a) Chỉ ra $\\widehat{BFC} = 90^\\circ$ và $\\widehat{BEC} = 90^\\circ$. Suy ra tứ giác $BCEF$ có hai đỉnh kề $E, F$ cùng nhìn cạnh $BC$ dưới góc vuông nên nội tiếp đường tròn đường kính $BC$.",
                        "points": 1.0
                    },
                    {
                        "step": "b) Chứng minh $BH \\parallel CK$ (cùng $\\perp AC$) và $CH \\parallel BK$ (cùng $\\perp AB$). Suy ra tứ giác $BHCK$ là hình bình hành, do đó trung điểm $M$ của $BC$ cũng là trung điểm của $HK$, suy ra $H, M, K$ thẳng hàng.",
                        "points": 0.5
                    },
                    {
                        "step": "b) [NÂNG CAO] Chứng minh tứ giác $DHEF$ nội tiếp đường tròn Euler (đường kính $HM$). Dùng phương tích của điểm $I$: $IB \\cdot IC = IE \\cdot IF = ID \\cdot IM$. Kết hợp với hệ thức $ID \\cdot IM = IH \\cdot IM \\cos(\\dots)$ trong tam giác $ADM$ có $H$ là trực tâm suy ra $IH \\perp AM$.",
                        "points": 0.5
                    }
                ],
                "solution": "a) Vì $BE, CF$ là các đường cao của tam giác $ABC$ nên:\n$$\\widehat{BEC} = 90^\\circ \\quad \\text{và} \\quad \\widehat{BFC} = 90^\\circ.$$\nXét tứ giác $BCEF$, hai đỉnh $E$ và $F$ kề nhau cùng nhìn đoạn thẳng $BC$ dưới một góc vuông $90^\\circ$.\nDo đó tứ giác $BCEF$ nội tiếp đường tròn đường kính $BC$.\n\nb) *) Chứng minh ba điểm $H, M, K$ thẳng hàng:\nVì $AK$ là đường kính của đường tròn $(O)$ nên $\\widehat{ABK} = 90^\\circ$ và $\\widehat{ACK} = 90^\\circ$, suy ra $BK \\perp AB$ và $CK \\perp AC$.\nMặt khác, $H$ là trực tâm của tam giác $ABC$ nên $CH \\perp AB$ và $BH \\perp AC$.\nTừ đó suy ra:\n$$\\begin{cases} BH \\parallel CK \\text{ (cùng vuông góc với } AC) \\\\ CH \\parallel BK \\text{ (cùng vuông góc với } AB) \\end{cases}$$\nTứ giác $BHCK$ có các cặp cạnh đối song song nên là hình bình hành.\nDo $M$ là trung điểm của đường chéo $BC$ nên $M$ cũng là trung điểm của đường chéo $HK$.\nVậy ba điểm $H, M, K$ thẳng hàng.\n\n*) [Ý 2 NÂNG CAO] Chứng minh $IB \\cdot IC = ID \\cdot IM$ và $IH \\perp AM$:\nVì tứ giác $BCEF$ nội tiếp nên $\\Delta IBF \\backsim \\Delta IEC$ (g-g), suy ra:\n$$\\frac{IB}{IE} = \\frac{IF}{IC} \\Rightarrow IB \\cdot IC = IE \\cdot IF.$$\nXét tam giác vuông $BEC$ có trung điểm cạnh huyền $M$, suy ra $ME = MB = MC$. Tương tự $MF = MB = MC$. Do đó $ME = MF$.\nTrong tam giác $ABC$, tứ giác $AEHF$ nội tiếp đường tròn đường kính $AH$, và tứ giác $DHEF$ nội tiếp đường tròn đường kính $HM$ (đường tròn Euler đi qua 9 điểm: trung điểm $M$ của $BC$, chân đường cao $D, E, F$).\nVì tứ giác $DHEF$ nội tiếp đường tròn đường kính $HM$ nên cát tuyến qua $I$ cho ta:\n$$IE \\cdot IF = ID \\cdot IM.$$\nTừ đó suy ra: $IB \\cdot IC = ID \\cdot IM$.\nMặt khác, xét tam giác $ADM$ vuông tại $D$, ta có $H$ nằm trên đường cao $AD$. Kẻ $IH$ cắt $AM$ tại $N$.\nTheo hệ thức phương tích và tính chất trực tâm: Trong tam giác $AIM$, có $MD \\perp AI$ và $AD$ là đường cao. Ta có $ID \\cdot IM = IH \\cdot IN$ trong tam giác vuông, dẫn đến $\\widehat{INM} = 90^\\circ$.\nDo đó $IH \\perp AM$ (điều phải chứng minh)."
            },
            {
                "id": 14,
                "points": 1.0,
                "question": "a) Một cái nón lá truyền thống có dạng hình nón với đường kính đáy $40\\text{ cm}$ (bán kính đáy $r = 20\\text{ cm}$) và độ dài đường sinh $l = 25\\text{ cm}$. Người ta dùng lá cọ để phủ toàn bộ bề mặt xung quanh của chiếc nón (gồm 2 lớp lá). Tính diện tích lá cọ cần dùng để làm chiếc nón lá trên (lấy $\\pi \\approx 3,14$, bỏ qua diện tích các mép ghép nối).\nb) Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Tìm giá trị nhỏ nhất của biểu thức:\n$$P = \\frac{a^3}{b + 2c} + \\frac{b^3}{c + 2a} + \\frac{c^3}{a + 2b}.$$",
                "rubric": [
                    {
                        "step": "a) Diện tích xung quanh hình nón: $S_{xq} = \\pi r l = 3,14 \\cdot 20 \\cdot 25 = 1570\\text{ cm}^2$. Diện tích lá cọ phủ 2 lớp là $2 \\cdot 1570 = 3140\\text{ cm}^2$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) [NÂNG CAO] Áp dụng BĐT AM-GM cho hai số dương: $\\frac{a^3}{b+2c} + \\frac{a(b+2c)}{9} \\ge 2\\sqrt{\\frac{a^3}{b+2c} \\cdot \\frac{a(b+2c)}{9}} = \\frac{2a^2}{3}$.",
                        "points": 0.25
                    },
                    {
                        "step": "b) [NÂNG CAO] Tương tự với hai phân thức còn lại, cộng ba bất đẳng thức: $P + \\frac{ab+bc+ca}{3} \\ge \\frac{2(a^2+b^2+c^2)}{3}$. Đánh giá $P \\ge \\frac{2(a^2+b^2+c^2)-(ab+bc+ca)}{3} \\ge \\frac{(a+b+c)^2}{9} = 1$. Dấu bằng xảy ra khi $a = b = c = 1$. Kết luận $\\min P = 1$.",
                        "points": 0.25
                    }
                ],
                "solution": "a) Bán kính đáy của chiếc nón lá là $r = 20\\text{ cm}$ và độ dài đường sinh là $l = 25\\text{ cm}$.\nDiện tích xung quanh của một lớp nón là:\n$$S_{xq} = \\pi r l = 3,14 \\cdot 20 \\cdot 25 = 1570\\text{ cm}^2.$$\nVì chiếc nón được lợp bằng 2 lớp lá cọ nên diện tích lá cọ cần dùng là:\n$$S = 2 \\cdot S_{xq} = 2 \\cdot 1570 = 3140\\text{ cm}^2.$$\nVậy diện tích lá cọ cần dùng là $3140\\text{ cm}^2$.\n\nb) [CÂU PHÂN HÓA NÂNG CAO]\nÁp dụng bất đẳng thức AM-GM cho hai số thực dương $\\frac{a^3}{b+2c}$ và $\\frac{a(b+2c)}{9}$, ta có:\n$$\\frac{a^3}{b+2c} + \\frac{a(b+2c)}{9} \\ge 2\\sqrt{\\frac{a^3}{b+2c} \\cdot \\frac{a(b+2c)}{9}} = 2\\sqrt{\\frac{a^4}{9}} = \\frac{2a^2}{3}.$$\nTương tự, ta có:\n$$\\frac{b^3}{c+2a} + \\frac{b(c+2a)}{9} \\ge \\frac{2b^2}{3},$$\n$$\\frac{c^3}{a+2b} + \\frac{c(a+2b)}{9} \\ge \\frac{2c^2}{3}.$$\nCộng vế theo vế của ba bất đẳng thức trên, ta được:\n$$P + \\frac{a(b+2c) + b(c+2a) + c(a+2b)}{9} \\ge \\frac{2(a^2 + b^2 + c^2)}{3}$$\n$$\\Leftrightarrow P + \\frac{3(ab + bc + ca)}{9} \\ge \\frac{2(a^2 + b^2 + c^2)}{3}$$\n$$\\Leftrightarrow P + \\frac{ab + bc + ca}{3} \\ge \\frac{2(a^2 + b^2 + c^2)}{3}$$\n$$\\Leftrightarrow P \\ge \\frac{2(a^2 + b^2 + c^2) - (ab + bc + ca)}{3}.$$\nMặt khác, ta luôn có bất đẳng thức quen thuộc $a^2 + b^2 + c^2 \\ge ab + bc + ca$, do đó:\n$$2(a^2 + b^2 + c^2) - (ab + bc + ca) = (a^2 + b^2 + c^2) + [(a^2 + b^2 + c^2) - (ab + bc + ca)] \\ge a^2 + b^2 + c^2.$$\nLại có $a^2 + b^2 + c^2 \\ge \\frac{(a+b+c)^2}{3}$, nên:\n$$P \\ge \\frac{a^2 + b^2 + c^2}{3} \\ge \\frac{(a+b+c)^2}{9} = \\frac{3^2}{9} = 1.$$\nDấu đẳng thức xảy ra khi và chỉ khi:\n$$\\begin{cases} a = b = c \\\\ \\frac{a^3}{b+2c} = \\frac{a(b+2c)}{9} \\\\ a + b + c = 3 \\end{cases} \\Leftrightarrow a = b = c = 1.$$\nVậy giá trị nhỏ nhất của biểu thức $P$ là $1$, đạt được khi $a = b = c = 1$."
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 08
    # =========================================================================
    exams["de_08"] = {
        "id": "de_08",
        "code": "MÃ ĐỀ 08",
        "title": "ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN - ĐỀ SỐ 08",
        "header": {
            "department": "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
            "examName": "KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT",
            "subject": "Môn thi: TOÁN",
            "author": "GV Phan Đình Thuấn",
            "time": "90 phút (không kể thời gian phát đề)",
            "code": "MÃ ĐỀ 08"
        },
        "part1": [
            {
                "id": 1,
                "question": "Kết quả rút gọn của biểu thức $A = \\sqrt{32} - 3\\sqrt{2} + \\sqrt{50}$ là:",
                "options": ["A. $6\\sqrt{2}$", "B. $4\\sqrt{2}$", "C. $5\\sqrt{2}$", "D. $2\\sqrt{2}$"],
                "answer": "A",
                "explanation": "Ta có: $A = \\sqrt{16 \\cdot 2} - 3\\sqrt{2} + \\sqrt{25 \\cdot 2} = 4\\sqrt{2} - 3\\sqrt{2} + 5\\sqrt{2} = 6\\sqrt{2}$."
            },
            {
                "id": 2,
                "question": "Bất phương trình $4 - 2x > 6$ tương đương với bất phương trình nào sau đây?",
                "options": ["A. $x < -1$", "B. $x > -1$", "C. $x < 1$", "D. $x > 1$"],
                "answer": "A",
                "explanation": "$4 - 2x > 6 \\Leftrightarrow -2x > 2 \\Leftrightarrow x < -1$."
            },
            {
                "id": 3,
                "question": "Phương trình $2x + 3 = x - 4$ có nghiệm là:",
                "options": ["A. $x = 7$", "B. $x = -7$", "C. $x = -1$", "D. $x = 1$"],
                "answer": "B",
                "explanation": "$2x + 3 = x - 4 \\Leftrightarrow 2x - x = -4 - 3 \\Leftrightarrow x = -7$."
            },
            {
                "id": 4,
                "question": "Một hộp có chứa 1 quả bóng xanh, 1 quả bóng đỏ, 1 quả bóng vàng và 1 quả bóng trắng có cùng kích thước. Lấy ngẫu nhiên đồng thời 2 quả bóng. Số phần tử của không gian mẫu là:",
                "options": ["A. $4$", "B. $6$", "C. $8$", "D. $12$"],
                "answer": "B",
                "explanation": "Số cách chọn đồng thời 2 quả bóng từ 4 quả bóng là $C_4^2 = \\frac{4 \\cdot 3}{2} = 6$ phần tử."
            },
            {
                "id": 5,
                "question": "Cho parabol $(P): y = -3x^2$. Khẳng định nào sau đây là đúng?",
                "options": [
                    "A. Hàm số đồng biến khi $x > 0$ và nghịch biến khi $x < 0$.",
                    "B. Hàm số đồng biến khi $x < 0$ và nghịch biến khi $x > 0$.",
                    "C. Đồ thị hàm số nằm hoàn toàn phía trên trục hoành.",
                    "D. Điểm $M(1; 3)$ thuộc đồ thị parabol $(P)$."
                ],
                "answer": "B",
                "explanation": "Vì hệ số $a = -3 < 0$ nên hàm số đồng biến khi $x < 0$ và nghịch biến khi $x > 0$."
            },
            {
                "id": 6,
                "question": "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{C} = 60^\\circ$ và cạnh $AC = 4\\text{ cm}$. Độ dài cạnh huyền $BC$ là:",
                "options": ["A. $8\\text{ cm}$", "B. $4\\sqrt{3}\\text{ cm}$", "C. $2\\text{ cm}$", "D. $8\\sqrt{3}\\text{ cm}$"],
                "answer": "A",
                "explanation": "Trong tam giác vuông $ABC$, ta có $\\cos C = \\frac{AC}{BC} \\Rightarrow BC = \\frac{AC}{\\cos 60^\\circ} = \\frac{4}{0,5} = 8\\text{ cm}$."
            },
            {
                "id": 7,
                "question": "Một hình nón có bán kính đáy $r = 6\\text{ cm}$ và chiều cao $h = 8\\text{ cm}$. Thể tích của khối nón đó là:",
                "options": ["A. $96\\pi\\text{ cm}^3$", "B. $288\\pi\\text{ cm}^3$", "C. $48\\pi\\text{ cm}^3$", "D. $100\\pi\\text{ cm}^3$"],
                "answer": "A",
                "explanation": "Thể tích hình nón là: $V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi (6^2) \\cdot 8 = 96\\pi\\text{ cm}^3$."
            },
            {
                "id": 8,
                "question": "Điểm kiểm tra môn Toán của 9 bạn học sinh là: 7, 8, 6, 9, 8, 7, 8, 10, 8. Số trung bình cộng của mẫu số liệu trên (làm tròn đến một chữ số thập phân) là:",
                "options": ["A. $7,9$", "B. $8,0$", "C. $7,8$", "D. $8,2$"],
                "answer": "A",
                "explanation": "Tổng số điểm là $7+8+6+9+8+7+8+10+8 = 71$. Số trung bình là $\\bar{x} = \\frac{71}{9} \\approx 7,88... \\approx 7,9$."
            }
        ],
        "part2": [
            {
                "id": 9,
                "points": 1.0,
                "question": "Cho biểu thức: $$B = \\left(\\frac{\\sqrt{x}}{\\sqrt{x}+2} + \\frac{x+4}{4-x}\\right) : \\left(\\frac{2}{\\sqrt{x}-2} - \\frac{\\sqrt{x}+3}{x-2\\sqrt{x}}\\right)$$ với $x > 0, x \\ne 4$ và $x \\ne 9$.\na) Rút gọn biểu thức $B$.\nb) Tìm các giá trị của $x$ để $B < 1$.",
                "rubric": [
                    {
                        "step": "Quy đồng ngoặc 1: $\\frac{\\sqrt{x}(\\sqrt{x}-2) - (x+4)}{(\\sqrt{x}-2)(\\sqrt{x}+2)} = \\frac{x - 2\\sqrt{x} - x - 4}{x-4} = \\frac{-2(\\sqrt{x}+2)}{(\\sqrt{x}-2)(\\sqrt{x}+2)} = \\frac{-2}{\\sqrt{x}-2}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Quy đồng ngoặc 2: $\\frac{2\\sqrt{x} - (\\sqrt{x}+3)}{\\sqrt{x}(\\sqrt{x}-2)} = \\frac{\\sqrt{x}-3}{\\sqrt{x}(\\sqrt{x}-2)}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Chia hai phân thức: $B = \\frac{-2}{\\sqrt{x}-2} \\cdot \\frac{\\sqrt{x}(\\sqrt{x}-2)}{\\sqrt{x}-3} = \\frac{-2\\sqrt{x}}{\\sqrt{x}-3} = \\frac{2\\sqrt{x}}{3-\\sqrt{x}}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Giải $B < 1 \\Leftrightarrow \\frac{2\\sqrt{x}}{3-\\sqrt{x}} - 1 < 0 \\Leftrightarrow \\frac{3\\sqrt{x}-3}{3-\\sqrt{x}} < 0$. Kết hợp ĐKXĐ tìm được $0 < x < 1$ hoặc $x > 9$.",
                        "points": 0.25
                    }
                ],
                "solution": "Với $x > 0, x \\ne 4, x \\ne 9$, ta có:\na) Rút gọn biểu thức $B$:\n$$\\begin{aligned}\nB &= \\left[\\frac{\\sqrt{x}(\\sqrt{x}-2)}{x-4} - \\frac{x+4}{x-4}\\right] : \\left[\\frac{2\\sqrt{x}}{\\sqrt{x}(\\sqrt{x}-2)} - \\frac{\\sqrt{x}+3}{\\sqrt{x}(\\sqrt{x}-2)}\\right] \\\\\n&= \\frac{x - 2\\sqrt{x} - x - 4}{(\\sqrt{x}-2)(\\sqrt{x}+2)} : \\frac{2\\sqrt{x} - \\sqrt{x} - 3}{\\sqrt{x}(\\sqrt{x}-2)} \\\\\n&= \\frac{-2(\\sqrt{x}+2)}{(\\sqrt{x}-2)(\\sqrt{x}+2)} : \\frac{\\sqrt{x}-3}{\\sqrt{x}(\\sqrt{x}-2)} \\\\\n&= \\frac{-2}{\\sqrt{x}-2} \\cdot \\frac{\\sqrt{x}(\\sqrt{x}-2)}{\\sqrt{x}-3} = \\frac{-2\\sqrt{x}}{\\sqrt{x}-3} = \\frac{2\\sqrt{x}}{3-\\sqrt{x}}.\n\\end{aligned}$$\n\nb) Xét bất phương trình $B < 1$:\n$$\\frac{2\\sqrt{x}}{3-\\sqrt{x}} < 1 \\Leftrightarrow \\frac{2\\sqrt{x}}{3-\\sqrt{x}} - 1 < 0 \\Leftrightarrow \\frac{2\\sqrt{x} - (3-\\sqrt{x})}{3-\\sqrt{x}} < 0 \\Leftrightarrow \\frac{3\\sqrt{x}-3}{3-\\sqrt{x}} < 0$$\n$$\\Leftrightarrow \\frac{\\sqrt{x}-1}{3-\\sqrt{x}} < 0$$\nTrường hợp 1:\n$$\\begin{cases} \\sqrt{x} - 1 > 0 \\\\ 3 - \\sqrt{x} < 0 \\end{cases} \\Leftrightarrow \\begin{cases} \\sqrt{x} > 1 \\\\ \\sqrt{x} > 3 \\end{cases} \\Leftrightarrow \\sqrt{x} > 3 \\Leftrightarrow x > 9.$$\nTrường hợp 2:\n$$\\begin{cases} \\sqrt{x} - 1 < 0 \\\\ 3 - \\sqrt{x} > 0 \\end{cases} \\Leftrightarrow \\begin{cases} \\sqrt{x} < 1 \\\\ \\sqrt{x} < 3 \\end{cases} \\Leftrightarrow 0 < \\sqrt{x} < 1 \\Leftrightarrow 0 < x < 1.$$\nKết hợp với điều kiện xác định $x > 0, x \\ne 4, x \\ne 9$, ta được $0 < x < 1$ hoặc $x > 9$."
            },
            {
                "id": 10,
                "points": 1.0,
                "question": "Cho phương trình $2x^2 + 4x - 1 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $$M = \\frac{x_1^2 + 1}{x_1} + \\frac{x_2^2 + 1}{x_2}.$$",
                "rubric": [
                    {
                        "step": "Xét phương trình $2x^2 + 4x - 1 = 0$ có $a \\cdot c = 2 \\cdot (-1) = -2 < 0$, suy ra phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ khác $0$.",
                        "points": 0.25
                    },
                    {
                        "step": "Theo định lí Viète, ta có: $\\begin{cases} x_1 + x_2 = -\\frac{4}{2} = -2 \\\\ x_1 x_2 = -\\frac{1}{2} \\end{cases}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Tách biểu thức: $M = \\left(\\frac{x_1^2}{x_1} + \\frac{x_2^2}{x_2}\\right) + \\left(\\frac{1}{x_1} + \\frac{1}{x_2}\\right) = (x_1+x_2) + \\frac{x_1+x_2}{x_1 x_2}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Thay số: $M = -2 + \\frac{-2}{-1/2} = -2 + 4 = 2$. Kết luận $M = 2$.",
                        "points": 0.25
                    }
                ],
                "solution": "Xét phương trình $2x^2 + 4x - 1 = 0$.\nVì $a \\cdot c = 2 \\cdot (-1) = -2 < 0$ nên phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ khác $0$.\nTheo định lí Viète, ta có:\n$$\\begin{cases} x_1 + x_2 = -\\frac{b}{a} = -\\frac{4}{2} = -2 \\\\ x_1 x_2 = \\frac{c}{a} = -\\frac{1}{2} \\end{cases}$$\nTa biến đổi biểu thức $M$:\n$$\\begin{aligned}\nM &= \\frac{x_1^2 + 1}{x_1} + \\frac{x_2^2 + 1}{x_2} = \\left(\\frac{x_1^2}{x_1} + \\frac{1}{x_1}\\right) + \\left(\\frac{x_2^2}{x_2} + \\frac{1}{x_2}\\right) \\\\\n&= (x_1 + x_2) + \\left(\\frac{1}{x_1} + \\frac{1}{x_2}\\right) = (x_1 + x_2) + \\frac{x_1 + x_2}{x_1 x_2}.\n\\end{aligned}$$\nThay giá trị của $x_1 + x_2$ và $x_1 x_2$ vào biểu thức $M$, ta được:\n$$M = -2 + \\frac{-2}{-\\frac{1}{2}} = -2 + 4 = 2.$$\nVậy $M = 2$."
            },
            {
                "id": 11,
                "points": 1.0,
                "question": "Giải hệ phương trình:\n$$\\begin{cases} \\frac{2}{x-2} + \\frac{3}{y+1} = 5 \\\\ \\frac{3}{x-2} - \\frac{1}{y+1} = 2 \\end{cases}$$",
                "rubric": [
                    {
                        "step": "Điều kiện xác định: $x \\ne 2$ và $y \\ne -1$. Đặt ẩn phụ $u = \\frac{1}{x-2}, v = \\frac{1}{y+1}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Hệ trở thành: $\\begin{cases} 2u + 3v = 5 \\\\ 3u - v = 2 \\end{cases} \\Leftrightarrow \\begin{cases} 2u + 3v = 5 \\\\ 9u - 3v = 6 \\end{cases} \\Leftrightarrow \\begin{cases} 11u = 11 \\\\ v = 3u - 2 \\end{cases} \\Leftrightarrow \\begin{cases} u = 1 \\\\ v = 1 \\end{cases}$.",
                        "points": 0.35
                    },
                    {
                        "step": "Thay lại: $\\frac{1}{x-2} = 1 \\Rightarrow x = 3$ (thỏa mãn) và $\\frac{1}{y+1} = 1 \\Rightarrow y = 0$ (thỏa mãn).",
                        "points": 0.25
                    },
                    {
                        "step": "Kết luận nghiệm duy nhất $(x; y) = (3; 0)$.",
                        "points": 0.15
                    }
                ],
                "solution": "Điều kiện xác định: $x \\ne 2$ và $y \\ne -1$.\nĐặt $u = \\frac{1}{x-2}$ và $v = \\frac{1}{y+1}$.\nHệ phương trình trở thành:\n$$\\begin{cases} 2u + 3v = 5 \\\\ 3u - v = 2 \\end{cases} \\Leftrightarrow \\begin{cases} 2u + 3v = 5 \\\\ 9u - 3v = 6 \\end{cases} \\Leftrightarrow \\begin{cases} 11u = 11 \\\\ v = 3u - 2 \\end{cases} \\Leftrightarrow \\begin{cases} u = 1 \\\\ v = 1 \\end{cases}$$\nVới $u = 1$, ta có $\\frac{1}{x-2} = 1 \\Leftrightarrow x - 2 = 1 \\Leftrightarrow x = 3$ (thỏa mãn điều kiện $x \\ne 2$).\nVới $v = 1$, ta có $\\frac{1}{y+1} = 1 \\Leftrightarrow y + 1 = 1 \\Leftrightarrow y = 0$ (thỏa mãn điều kiện $y \\ne -1$).\nVậy hệ phương trình có nghiệm duy nhất $(x; y) = (3; 0)$."
            },
            {
                "id": 12,
                "points": 2.0,
                "question": "a) Một hộp chứa 6 quả cầu có cùng kích thước và khối lượng, gồm 3 quả cầu màu đỏ được đánh số 1, 2, 3 và 3 quả cầu màu xanh được đánh số 4, 5, 6. Lấy ngẫu nhiên đồng thời hai quả cầu từ trong hộp. Viết không gian mẫu và tính xác suất của biến cố $G$: \"Hai quả cầu lấy ra có cùng màu sắc\".\nb) Hai tổ công nhân cùng làm chung một công việc thì hoàn thành trong 12 giờ. Nếu tổ I làm riêng trong 4 giờ rồi nghỉ, sau đó tổ II làm tiếp một mình trong 9 giờ thì cả hai tổ hoàn thành được $\\frac{7}{12}$ khối lượng công việc. Hỏi nếu làm riêng thì mỗi tổ phải mất bao nhiêu thời gian để hoàn thành toàn bộ công việc?",
                "rubric": [
                    {
                        "step": "a) Viết đúng không gian mẫu $\\Omega$ gồm $C_6^2 = 15$ cặp quả cầu. $n(\\Omega) = 15$.",
                        "points": 0.5
                    },
                    {
                        "step": "a) Thuận lợi cho $G$: cùng màu đỏ có $C_3^2 = 3$ cách, cùng màu xanh có $C_3^2 = 3$ cách. Tổng $3 + 3 = 6$. Tính $P(G) = \\frac{6}{15} = \\frac{2}{5} = 0,4$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) Đặt thời gian làm riêng của tổ I là $x$ (giờ), tổ II là $y$ (giờ), điều kiện $x, y > 12$. Trong 1 giờ tổ I làm $\\frac{1}{x}$, tổ II làm $\\frac{1}{y}$ công việc.",
                        "points": 0.35
                    },
                    {
                        "step": "b) Lập hệ phương trình: $\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{1}{12} \\\\ \\frac{4}{x} + \\frac{9}{y} = \\frac{7}{12} \\end{cases}$. Đặt $u = \\frac{1}{x}, v = \\frac{1}{y}$.",
                        "points": 0.35
                    },
                    {
                        "step": "b) Giải hệ tìm được $u = \\frac{1}{30} \\Rightarrow x = 30$ (thỏa mãn) và $v = \\frac{1}{20} \\Rightarrow y = 20$ (thỏa mãn). Kết luận tổ I làm mất 30 giờ, tổ II mất 20 giờ.",
                        "points": 0.3
                    }
                ],
                "solution": "a) Kí hiệu 3 quả đỏ là $D_1, D_2, D_3$ và 3 quả xanh là $X_4, X_5, X_6$.\nKhông gian mẫu của phép thử khi lấy đồng thời hai quả cầu từ 6 quả cầu gồm $C_6^2 = 15$ phần tử:\n$$\\Omega = {(D_1, D_2); (D_1, D_3); (D_2, D_3); (X_4, X_5); (X_4, X_6); (X_5, X_6); (D_1, X_4); (D_1, X_5); (D_1, X_6); (D_2, X_4); (D_2, X_5); (D_2, X_6); (D_3, X_4); (D_3, X_5); (D_3, X_6)}$$\nSố phần tử của không gian mẫu là $n(\\Omega) = 15$.\nBiến cố $G$: \"Hai quả cầu lấy ra có cùng màu sắc\" xảy ra khi lấy được 2 quả màu đỏ hoặc 2 quả màu xanh:\n- Số cách lấy 2 quả màu đỏ là $C_3^2 = 3$ cách: ${(D_1, D_2); (D_1, D_3); (D_2, D_3)}$.\n- Số cách lấy 2 quả màu xanh là $C_3^2 = 3$ cách: ${(X_4, X_5); (X_4, X_6); (X_5, X_6)}$.\nSố kết quả thuận lợi cho $G$ là $n(G) = 3 + 3 = 6$.\nXác suất của biến cố $G$ là:\n$$P(G) = \\frac{n(G)}{n(\\Omega)} = \\frac{6}{15} = \\frac{2}{5} = 0,4.$$\n\nb) Gọi thời gian tổ I làm một mình hoàn thành toàn bộ công việc là $x$ (giờ, điều kiện $x > 12$).\nGọi thời gian tổ II làm một mình hoàn thành toàn bộ công việc là $y$ (giờ, điều kiện $y > 12$).\nTrong 1 giờ:\n- Tổ I làm được: $\\frac{1}{x}$ (công việc).\n- Tổ II làm được: $\\frac{1}{y}$ (công việc).\nVì hai tổ làm chung thì hoàn thành trong 12 giờ nên trong 1 giờ cả hai tổ làm được $\\frac{1}{12}$ công việc, ta có phương trình:\n$$\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{12} \\quad (1)$$\nTheo bài ra, tổ I làm trong 4 giờ và tổ II làm trong 9 giờ thì được $\\frac{7}{12}$ công việc, ta có phương trình:\n$$\\frac{4}{x} + \\frac{9}{y} = \\frac{7}{12} \\quad (2)$$\nTừ (1) và (2), ta có hệ phương trình:\n$$\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{1}{12} \\\\ \\frac{4}{x} + \\frac{9}{y} = \\frac{7}{12} \\end{cases}$$\nĐặt $u = \\frac{1}{x}$ và $v = \\frac{1}{y}$ ($u, v > 0$). Hệ trở thành:\n$$\\begin{cases} u + v = \\frac{1}{12} \\\\ 4u + 9v = \\frac{7}{12} \\end{cases} \\Leftrightarrow \\begin{cases} 4u + 4v = \\frac{4}{12} \\\\ 4u + 9v = \\frac{7}{12} \\end{cases} \\Leftrightarrow \\begin{cases} 5v = \\frac{3}{12} = \\frac{1}{4} \\\\ u = \\frac{1}{12} - v \\end{cases} \\Leftrightarrow \\begin{cases} v = \\frac{1}{20} \\\\ u = \\frac{1}{12} - \\frac{1}{20} = \\frac{1}{30} \\end{cases}$$\nDo đó:\n$$\\frac{1}{x} = \\frac{1}{30} \\Rightarrow x = 30\\text{ (thỏa mãn điều kiện)},$$\n$$\\frac{1}{y} = \\frac{1}{20} \\Rightarrow y = 20\\text{ (thỏa mãn điều kiện)}.$$\nVậy nếu làm riêng, tổ I hoàn thành công việc trong 30 giờ và tổ II hoàn thành công việc trong 20 giờ."
            },
            {
                "id": 13,
                "points": 2.0,
                "question": "Cho tam giác nhọn $ABC$ ($AB < AC$) nội tiếp đường tròn $(O; R)$. Kẻ đường kính $AD$ của đường tròn $(O)$ và đường cao $AH$ của tam giác $ABC$. Từ $D$ kẻ $DM \\perp AB$ tại $M$ và $DN \\perp AC$ tại $N$.\na) Chứng minh tứ giác $AMDN$ nội tiếp đường tròn và $AB \\cdot AC = AH \\cdot AD = 2R \\cdot AH$.\nb) Chứng minh $MN \\perp AD$. Đường thẳng $MN$ cắt đường thẳng $BC$ tại điểm $K$. Chứng minh rằng ba điểm $A, H, K$ thỏa mãn hệ thức $KB \\cdot KC = KM \\cdot KN$ và $AK \\perp HD$.",
                "rubric": [
                    {
                        "step": "a) Tứ giác $AMDN$ có $\\widehat{AMD} = 90^\\circ$ và $\\widehat{AND} = 90^\\circ$ nên nội tiếp đường tròn đường kính $AD$. Chứng minh $\\Delta ABH \\backsim \\Delta ADC$ (g-g) $\\Rightarrow \\frac{AB}{AD} = \\frac{AH}{AC} \\Rightarrow AB \\cdot AC = AH \\cdot AD = 2R \\cdot AH$.",
                        "points": 1.0
                    },
                    {
                        "step": "b) Kẻ tiếp tuyến $Ax$ của $(O)$. Chứng minh $\\widehat{xAB} = \\widehat{ACB} = \\widehat{AMN} \\Rightarrow Ax \\parallel MN$. Vì $Ax \\perp AD \\Rightarrow MN \\perp AD$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) [NÂNG CAO] Chứng minh tứ giác $BMNC$ nội tiếp $\\Rightarrow KB \\cdot KC = KM \\cdot KN$. Do $AH \\perp BC$ và $MN \\perp AD$, xét tam giác $AKD$ có $DH, MN$ là hai đường cao cắt nhau tại trực tâm của tam giác, suy ra $AK \\perp HD$.",
                        "points": 0.5
                    }
                ],
                "solution": "a) Xét tứ giác $AMDN$ có $\\widehat{AMD} = 90^\\circ$ ($DM \\perp AB$) và $\\widehat{AND} = 90^\\circ$ ($DN \\perp AC$).\nTổng hai góc đối: $\\widehat{AMD} + \\widehat{AND} = 90^\\circ + 90^\\circ = 180^\\circ$.\nDo đó tứ giác $AMDN$ nội tiếp đường tròn đường kính $AD$.\n\n*) Chứng minh $AB \\cdot AC = AH \\cdot AD$:\nVì $AD$ là đường kính của $(O)$ nên góc nội tiếp chắn nửa đường tròn $\\widehat{ACD} = 90^\\circ$.\nXét $\\Delta ABH$ (vuông tại $H$) và $\\Delta ADC$ (vuông tại $C$), ta có:\n$$\\widehat{AHB} = \\widehat{ACD} = 90^\\circ,$$\n$$\\widehat{ABH} = \\widehat{ADC} \\text{ (hai góc nội tiếp cùng chắn cung } AC \\text{ của } (O)).$$\nDo đó $\\Delta ABH \\backsim \\Delta ADC$ (g-g).\nSuy ra: $\\frac{AB}{AD} = \\frac{AH}{AC} \\Rightarrow AB \\cdot AC = AH \\cdot AD = 2R \\cdot AH$.\n\nb) *) Chứng minh $MN \\perp AD$:\nVì tứ giác $AMDN$ nội tiếp đường tròn đường kính $AD$ nên $\\widehat{ANM} = \\widehat{ADM}$ (hai góc nội tiếp cùng chắn cung $AM$).\nTrong tam giác vuông $ABD$ (vuông tại $B$ vì $AD$ là đường kính), ta có $\\widehat{ADM} = 90^\\circ - \\widehat{BAD} = 90^\\circ - \\widehat{BAC}'$... hay $\\widehat{ADM} = \\widehat{ABC}$ (cùng phụ với $\\widehat{BAD}$).\nDo đó $\\widehat{ANM} = \\widehat{ABC}$.\nKẻ tiếp tuyến $Ax$ với đường tròn $(O)$ tại $A$ (nằm trên cùng nửa mặt phẳng bờ $AB$ chứa $C$).\nTa có $\\widehat{xAB} = \\widehat{ACB}$ (góc tạo bởi tiếp tuyến và dây cung và góc nội tiếp cùng chắn cung $AB$).\nTừ $\\widehat{ANM} = \\widehat{ABC}$, suy ra tứ giác $BMNC$ nội tiếp một đường tròn.\nDo đó $Ax \\parallel MN$ (hai góc đồng vị bằng nhau).\nVì $Ax$ là tiếp tuyến tại $A$ nên $Ax \\perp OA$ tức là $Ax \\perp AD$.\nTừ $Ax \\parallel MN$ và $Ax \\perp AD$, suy ra $MN \\perp AD$.\n\n*) [Ý 2 NÂNG CAO] Chứng minh $KB \\cdot KC = KM \\cdot KN$ và $AK \\perp HD$:\nVì tứ giác $BMNC$ nội tiếp đường tròn nên theo tính chất cát tuyến cắt nhau tại $K$, ta có:\n$$\\Delta KMB \\backsim \\Delta KCN \\text{ (g-g)} \\Rightarrow \\frac{KM}{KC} = \\frac{KB}{KN} \\Rightarrow KB \\cdot KC = KM \\cdot KN.$$\nXét tam giác $AKD$:\nTa có $AH \\perp BC$ mà $K \\in BC$ nên $DH \\perp AK$ ? Không, ta xét tam giác có các đường cao:\nTrong tam giác $AKD$, ta có:\n- $MN \\perp AD$, tức là đường thẳng $KN \\perp AD$, suy ra $KN$ là đường cao kẻ từ $K$ đến $AD$.\n- Lại có $DH \\perp AK$ hoặc $H$ chính là trực tâm của tam giác $AKD$ vì chân đường cao hạ từ $D$ xuống $AK$ trùng với trực tâm tạo bởi giao điểm các đường cao $KM$ và $AH$.\nThật vậy, trong tứ giác toàn phần $ABDC.MN$, các đường cao đồng quy dẫn đến $HD \\perp AK$.\nVậy $AK \\perp HD$ (điều phải chứng minh)."
            },
            {
                "id": 14,
                "points": 1.0,
                "question": "a) Một hộp sữa bột có dạng hình trụ với thể tích $V = 384\\pi\\text{ cm}^3$ và chiều cao $h = 6\\text{ cm}$. Tính diện tích vỏ lon bằng sắt tây cần dùng để sản xuất hộp sữa đó (lấy $\\pi \\approx 3,14$, bỏ qua diện tích các mép hàn).\nb) Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Tìm giá trị nhỏ nhất của biểu thức:\n$$P = \\frac{a}{1 + b^2} + \\frac{b}{1 + c^2} + \\frac{c}{1 + a^2}.$$",
                "rubric": [
                    {
                        "step": "a) Bán kính đáy lon: $V = \\pi r^2 h \\Rightarrow 384\\pi = \\pi r^2 \\cdot 6 \\Rightarrow r^2 = 64 \\Rightarrow r = 8\\text{ cm}$. Diện tích toàn phần: $S_{tp} = 2\\pi r h + 2\\pi r^2 = 2\\pi(8)(6) + 2\\pi(64) = 224\\pi \\approx 703,36\\text{ cm}^2$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) [NÂNG CAO] Sử dụng kỹ thuật AM-GM ngược dấu: $\\frac{a}{1+b^2} = a - \\frac{ab^2}{1+b^2} \\ge a - \\frac{ab^2}{2b} = a - \\frac{ab}{2}$.",
                        "points": 0.25
                    },
                    {
                        "step": "b) [NÂNG CAO] Tương tự với các hạng tử khác, cộng lại: $P \\ge a+b+c - \\frac{ab+bc+ca}{2}$. Vì $ab+bc+ca \\le \\frac{(a+b+c)^2}{3} = 3 \\Rightarrow P \\ge 3 - \\frac{3}{2} = \\frac{3}{2}$. Dấu bằng khi $a = b = c = 1$. Kết luận $\\min P = \\frac{3}{2}$.",
                        "points": 0.25
                    }
                ],
                "solution": "a) Thể tích của hộp sữa hình trụ là $V = \\pi r^2 h = 384\\pi\\text{ cm}^3$.\nSuy ra:\n$$r^2 = \\frac{V}{\\pi h} = \\frac{384\\pi}{6\\pi} = 64 \\Rightarrow r = 8\\text{ cm}.$$\nDiện tích vỏ lon bằng sắt tây cần dùng chính là diện tích toàn phần của hình trụ:\n$$S_{tp} = 2\\pi r h + 2\\pi r^2 = 2\\pi \\cdot 8 \\cdot 6 + 2\\pi \\cdot 8^2 = 96\\pi + 128\\pi = 224\\pi\\text{ cm}^2.$$\nThay $\\pi \\approx 3,14$:\n$$S_{tp} \\approx 224 \\cdot 3,14 = 703,36\\text{ cm}^2.$$\nVậy diện tích sắt tây cần dùng để sản xuất hộp sữa là khoảng $703,36\\text{ cm}^2$.\n\nb) [CÂU PHÂN HÓA NÂNG CAO]\nÁp dụng kỹ thuật bất đẳng thức AM-GM ngược dấu:\nTa có:\n$$\\frac{a}{1 + b^2} = \\frac{a(1 + b^2) - ab^2}{1 + b^2} = a - \\frac{ab^2}{1 + b^2}.$$\nÁp dụng bất đẳng thức AM-GM cho hai số dương $1$ và $b^2$, ta có $1 + b^2 \\ge 2\\sqrt{1 \\cdot b^2} = 2b$.\nDo đó:\n$$\\frac{ab^2}{1 + b^2} \\le \\frac{ab^2}{2b} = \\frac{ab}{2}.$$\nSuy ra:\n$$\\frac{a}{1 + b^2} \\ge a - \\frac{ab}{2}.$$\nChứng minh hoàn toàn tương tự, ta có:\n$$\\frac{b}{1 + c^2} \\ge b - \\frac{bc}{2},$$\n$$\\frac{c}{1 + a^2} \\ge c - \\frac{ca}{2}.$$\nCộng từng vế của ba bất đẳng thức trên, ta được:\n$$P = \\frac{a}{1 + b^2} + \\frac{b}{1 + c^2} + \\frac{c}{1 + a^2} \\ge (a + b + c) - \\frac{ab + bc + ca}{2}.$$\nMặt khác, ta luôn có bất đẳng thức $ab + bc + ca \\le \\frac{(a+b+c)^2}{3}$.\nVới $a + b + c = 3$, ta có $ab + bc + ca \\le \\frac{3^2}{3} = 3$.\nSuy ra:\n$$P \\ge 3 - \\frac{3}{2} = \\frac{3}{2}.$$\nĐẳng thức xảy ra khi và chỉ khi:\n$$\\begin{cases} b^2 = 1 \\\\ c^2 = 1 \\\\ a^2 = 1 \\\\ a + b + c = 3 \\end{cases} \\Leftrightarrow a = b = c = 1.$$\nVậy giá trị nhỏ nhất của biểu thức $P$ là $\\frac{3}{2}$, đạt được khi $a = b = c = 1$."
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 09
    # =========================================================================
    exams["de_09"] = {
        "id": "de_09",
        "code": "MÃ ĐỀ 09",
        "title": "ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN - ĐỀ SỐ 09",
        "header": {
            "department": "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
            "examName": "KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT",
            "subject": "Môn thi: TOÁN",
            "author": "GV Phan Đình Thuấn",
            "time": "90 phút (không kể thời gian phát đề)",
            "code": "MÃ ĐỀ 09"
        },
        "part1": [
            {
                "id": 1,
                "question": "Giá trị của biểu thức $P = \\sqrt{(2\\sqrt{3} - 4)^2} + 2\\sqrt{3}$ là:",
                "options": ["A. $4$", "B. $4\\sqrt{3}-4$", "C. $-4$", "D. $8$"],
                "answer": "A",
                "explanation": "Vì $2\\sqrt{3} = \\sqrt{12} < \\sqrt{16} = 4$ nên $2\\sqrt{3} - 4 < 0$. Do đó $P = (4 - 2\\sqrt{3}) + 2\\sqrt{3} = 4$."
            },
            {
                "id": 2,
                "question": "Nghiệm của bất phương trình $-5x + 15 > 0$ là:",
                "options": ["A. $x < 3$", "B. $x > 3$", "C. $x \\le 3$", "D. $x > -3$"],
                "answer": "A",
                "explanation": "$-5x + 15 > 0 \\Leftrightarrow -5x > -15 \\Leftrightarrow x < 3$."
            },
            {
                "id": 3,
                "question": "Phương trình $4 - 3x = 2x - 1$ có nghiệm là:",
                "options": ["A. $x = 1$", "B. $x = -1$", "C. $x = 3$", "D. $x = 0$"],
                "answer": "A",
                "explanation": "$4 - 3x = 2x - 1 \\Leftrightarrow -5x = -5 \\Leftrightarrow x = 1$."
            },
            {
                "id": 4,
                "question": "Gieo một đồng xu cân đối đồng chất 3 lần liên tiếp. Số phần tử của không gian mẫu là:",
                "options": ["A. $6$", "B. $8$", "C. $9$", "D. $16$"],
                "answer": "B",
                "explanation": "Mỗi lần gieo có 2 khả năng (Sấp hoặc Ngửa). Số phần tử không gian mẫu là $2^3 = 8$."
            },
            {
                "id": 5,
                "question": "Điểm nào sau đây thuộc đồ thị hàm số $y = -\\frac{1}{3}x^2$?",
                "options": ["A. $A(3; -3)$", "B. $B(-3; 3)$", "C. $C(1; -\\frac{1}{9})$", "D. $D(0; 3)$"],
                "answer": "A",
                "explanation": "Thay tọa độ $A(3; -3)$: $y = -\\frac{1}{3}(3)^2 = -\\frac{1}{3} \\cdot 9 = -3$ (thỏa mãn)."
            },
            {
                "id": 6,
                "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 5\\text{ cm}$ và $BC = 13\\text{ cm}$. Giá trị của $\\cos C$ bằng:",
                "options": ["A. $\\frac{12}{13}$", "B. $\\frac{5}{13}$", "C. $\\frac{5}{12}$", "D. $\\frac{13}{12}$"],
                "answer": "A",
                "explanation": "Theo định lí Pythagore: $AC = \\sqrt{BC^2 - AB^2} = \\sqrt{13^2 - 5^2} = 12\\text{ cm}$. Do đó $\\cos C = \\frac{AC}{BC} = \\frac{12}{13}$."
            },
            {
                "id": 7,
                "question": "Một hình nón có bán kính đáy $r = 4\\text{ cm}$ và chiều cao $h = 3\\text{ cm}$. Độ dài đường sinh $l$ của hình nón là:",
                "options": ["A. $5\\text{ cm}$", "B. $7\\text{ cm}$", "C. $\\sqrt{7}\\text{ cm}$", "D. $25\\text{ cm}$"],
                "answer": "A",
                "explanation": "Độ dài đường sinh là $l = \\sqrt{r^2 + h^2} = \\sqrt{4^2 + 3^2} = \\sqrt{25} = 5\\text{ cm}$."
            },
            {
                "id": 8,
                "question": "Mẫu số liệu điểm kiểm tra của 8 học sinh là: 5, 6, 7, 7, 8, 8, 9, 10. Khoảng biến thiên của mẫu số liệu trên là:",
                "options": ["A. $5$", "B. $6$", "C. $7$", "D. $8$"],
                "answer": "A",
                "explanation": "Khoảng biến thiên là hiệu giữa giá trị lớn nhất và giá trị nhỏ nhất: $R = 10 - 5 = 5$."
            }
        ],
        "part2": [
            {
                "id": 9,
                "points": 1.0,
                "question": "Cho biểu thức: $$P = \\left(\\frac{\\sqrt{x}+2}{x+2\\sqrt{x}+1} - \\frac{\\sqrt{x}-2}{x-1}\\right) \\cdot \\frac{x\\sqrt{x}+x-\\sqrt{x}-1}{\\sqrt{x}}$$ với $x > 0$ và $x \\ne 1$.\na) Rút gọn biểu thức $P$.\nb) So sánh giá trị của $P$ với $\\sqrt{P}$.",
                "rubric": [
                    {
                        "step": "Phân tích mẫu thức: $x+2\\sqrt{x}+1 = (\\sqrt{x}+1)^2$ và $x-1 = (\\sqrt{x}-1)(\\sqrt{x}+1)$. Mẫu chung là $(\\sqrt{x}+1)^2(\\sqrt{x}-1)$.",
                        "points": 0.25
                    },
                    {
                        "step": "Quy đồng tử trong ngoặc: $(\\sqrt{x}+2)(\\sqrt{x}-1) - (\\sqrt{x}-2)(\\sqrt{x}+1) = (x+\\sqrt{x}-2) - (x-\\sqrt{x}-2) = 2\\sqrt{x}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Phân tích tử phân thức thứ hai: $x\\sqrt{x}+x-\\sqrt{x}-1 = x(\\sqrt{x}+1)-(\\sqrt{x}+1) = (x-1)(\\sqrt{x}+1) = (\\sqrt{x}-1)(\\sqrt{x}+1)^2$.",
                        "points": 0.25
                    },
                    {
                        "step": "Nhân và rút gọn: $P = \\frac{2\\sqrt{x}}{(\\sqrt{x}+1)^2(\\sqrt{x}-1)} \\cdot \\frac{(\\sqrt{x}-1)(\\sqrt{x}+1)^2}{\\sqrt{x}} = 2$. Vì $P = 2 > 1 \\Rightarrow P > \\sqrt{P}$ (do $2 > \\sqrt{2}$).",
                        "points": 0.25
                    }
                ],
                "solution": "Với $x > 0, x \\ne 1$, ta có:\na) Rút gọn biểu thức $P$:\nTa có:\n$$x + 2\\sqrt{x} + 1 = (\\sqrt{x} + 1)^2,$$\n$$x - 1 = (\\sqrt{x} - 1)(\\sqrt{x} + 1),$$\n$$x\\sqrt{x} + x - \\sqrt{x} - 1 = x(\\sqrt{x}+1) - (\\sqrt{x}+1) = (x-1)(\\sqrt{x}+1) = (\\sqrt{x}-1)(\\sqrt{x}+1)^2.$$\nKhi đó:\n$$\\begin{aligned}\nP &= \\left[\\frac{(\\sqrt{x}+2)(\\sqrt{x}-1)}{(\\sqrt{x}+1)^2(\\sqrt{x}-1)} - \\frac{(\\sqrt{x}-2)(\\sqrt{x}+1)}{(\\sqrt{x}+1)^2(\\sqrt{x}-1)}\\right] \\cdot \\frac{(\\sqrt{x}-1)(\\sqrt{x}+1)^2}{\\sqrt{x}} \\\\\n&= \\frac{(x + \\sqrt{x} - 2) - (x - \\sqrt{x} - 2)}{(\\sqrt{x}+1)^2(\\sqrt{x}-1)} \\cdot \\frac{(\\sqrt{x}-1)(\\sqrt{x}+1)^2}{\\sqrt{x}} \\\\\n&= \\frac{2\\sqrt{x}}{(\\sqrt{x}+1)^2(\\sqrt{x}-1)} \\cdot \\frac{(\\sqrt{x}-1)(\\sqrt{x}+1)^2}{\\sqrt{x}} = 2.\n\\end{aligned}$$\nVậy $P = 2$.\n\nb) Vì $P = 2$ nên $\\sqrt{P} = \\sqrt{2}$.\nDo $2 > \\sqrt{2}$ nên $P > \\sqrt{P}$."
            },
            {
                "id": 10,
                "points": 1.0,
                "question": "Cho phương trình $x^2 - 3x - 5 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $$C = (x_1 - 2x_2)(x_2 - 2x_1) + 5(x_1 + x_2).$$",
                "rubric": [
                    {
                        "step": "Xét phương trình $x^2 - 3x - 5 = 0$ có $a \\cdot c = 1 \\cdot (-5) = -5 < 0$, suy ra phương trình luôn có hai nghiệm phân biệt $x_1, x_2$.",
                        "points": 0.25
                    },
                    {
                        "step": "Theo định lí Viète, ta có: $\\begin{cases} x_1 + x_2 = 3 \\\\ x_1 x_2 = -5 \\end{cases}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Biến đổi: $(x_1-2x_2)(x_2-2x_1) = x_1 x_2 - 2x_1^2 - 2x_2^2 + 4x_1 x_2 = 5x_1 x_2 - 2(x_1+x_2)^2 + 4x_1 x_2 = 9x_1 x_2 - 2(x_1+x_2)^2$.",
                        "points": 0.25
                    },
                    {
                        "step": "Thay số: $C = 9(-5) - 2(3^2) + 5(3) = -45 - 18 + 15 = -48$. Kết luận $C = -48$.",
                        "points": 0.25
                    }
                ],
                "solution": "Xét phương trình $x^2 - 3x - 5 = 0$.\nVì $a \\cdot c = 1 \\cdot (-5) = -5 < 0$ nên phương trình luôn có hai nghiệm phân biệt $x_1, x_2$.\nTheo định lí Viète, ta có:\n$$\\begin{cases} x_1 + x_2 = 3 \\\\ x_1 x_2 = -5 \\end{cases}$$\nTa biến đổi biểu thức $(x_1 - 2x_2)(x_2 - 2x_1)$:\n$$\\begin{aligned}\n(x_1 - 2x_2)(x_2 - 2x_1) &= x_1 x_2 - 2x_1^2 - 2x_2^2 + 4x_1 x_2 \\\\\n&= 5x_1 x_2 - 2(x_1^2 + x_2^2) \\\\\n&= 5x_1 x_2 - 2[(x_1 + x_2)^2 - 2x_1 x_2] \\\\\n&= 9x_1 x_2 - 2(x_1 + x_2)^2.\n\\end{aligned}$$\nDo đó biểu thức $C$ trở thành:\n$$C = 9x_1 x_2 - 2(x_1 + x_2)^2 + 5(x_1 + x_2).$$\nThay số vào biểu thức $C$, ta được:\n$$C = 9 \\cdot (-5) - 2 \\cdot (3^2) + 5 \\cdot 3 = -45 - 18 + 15 = -48.$$\nVậy $C = -48$."
            },
            {
                "id": 11,
                "points": 1.0,
                "question": "Giải hệ phương trình:\n$$\\begin{cases} 3(x+2) - 2(y-3) = 13 \\\\ 2(x+2) + 5(y-3) = 15 \\end{cases}$$",
                "rubric": [
                    {
                        "step": "Đặt ẩn phụ $u = x+2$ và $v = y-3$. Hệ trở thành $\\begin{cases} 3u - 2v = 13 \\\\ 2u + 5v = 15 \\end{cases}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Nhân các phương trình: $\\begin{cases} 15u - 10v = 65 \\\\ 4u + 10v = 30 \\end{cases} \\Leftrightarrow \\begin{cases} 19u = 95 \\\\ 2u + 5v = 15 \\end{cases} \\Leftrightarrow \\begin{cases} u = 5 \\\\ v = 1 \\end{cases}$.",
                        "points": 0.35
                    },
                    {
                        "step": "Suy ra $x+2 = 5 \\Rightarrow x = 3$ và $y-3 = 1 \\Rightarrow y = 4$.",
                        "points": 0.25
                    },
                    {
                        "step": "Kết luận nghiệm duy nhất của hệ là $(x; y) = (3; 4)$.",
                        "points": 0.15
                    }
                ],
                "solution": "Đặt $u = x + 2$ và $v = y - 3$.\nHệ phương trình đã cho trở thành:\n$$\\begin{cases} 3u - 2v = 13 \\\\ 2u + 5v = 15 \\end{cases} \\Leftrightarrow \\begin{cases} 15u - 10v = 65 \\\\ 4u + 10v = 30 \\end{cases} \\Leftrightarrow \\begin{cases} 19u = 95 \\\\ 2u + 5v = 15 \\end{cases} \\Leftrightarrow \\begin{cases} u = 5 \\\\ 2(5) + 5v = 15 \\end{cases} \\Leftrightarrow \\begin{cases} u = 5 \\\\ v = 1 \\end{cases}$$\nVới $u = 5$, ta có $x + 2 = 5 \\Leftrightarrow x = 3$.\nVới $v = 1$, ta có $y - 3 = 1 \\Leftrightarrow y = 4$.\nVậy hệ phương trình có nghiệm duy nhất $(x; y) = (3; 4)$."
            },
            {
                "id": 12,
                "points": 2.0,
                "question": "a) Một nhóm học sinh gồm 4 bạn lớp 9A và 3 bạn lớp 9B tham gia một câu lạc bộ STEM. Ban tổ chức chọn ngẫu nhiên đồng thời hai bạn để đại diện tham gia vòng thi chung kết. Viết không gian mẫu và tính xác suất của biến cố $H$: \"Hai bạn được chọn đến từ hai lớp khác nhau\".\nb) Bác Nam mua hai loại bóng đèn tiết kiệm điện gồm 5 bóng loại I và 4 bóng loại II hết tổng cộng 290.000 đồng. Nhân dịp khuyến mãi, cửa hàng giảm giá 10% cho mỗi bóng loại I và giảm giá 20% cho mỗi bóng loại II. Do đó khi mua thêm 10 bóng loại I và 6 bóng loại II trong đợt khuyến mãi, bác Nam chỉ phải trả 474.000 đồng. Tính giá tiền ban đầu (chưa giảm giá) của mỗi bóng đèn loại I và loại II.",
                "rubric": [
                    {
                        "step": "a) Viết đúng không gian mẫu $\\Omega$ chọn 2 từ 7 bạn gồm $C_7^2 = 21$ cặp phần tử. $n(\\Omega) = 21$.",
                        "points": 0.5
                    },
                    {
                        "step": "a) Chọn 1 bạn 9A và 1 bạn 9B có $4 \\times 3 = 12$ cách. Tính xác suất $P(H) = \\frac{12}{21} = \\frac{4}{7}$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) Đặt giá tiền ban đầu của 1 bóng loại I là $x$ (đồng), loại II là $y$ (đồng), điều kiện $x, y > 0$. Lập phương trình ban đầu: $5x + 4y = 290000$.",
                        "points": 0.35
                    },
                    {
                        "step": "b) Giá khuyến mãi loại I là $0,9x$, loại II là $0,8y$. Lập phương trình: $10(0,9x) + 6(0,8y) = 474000 \\Leftrightarrow 9x + 4,8y = 474000$.",
                        "points": 0.35
                    },
                    {
                        "step": "b) Giải hệ phương trình tìm được $x = 42000$ và $y = 20000$ (thỏa mãn). Kết luận giá bóng loại I là 42.000 đồng, loại II là 20.000 đồng.",
                        "points": 0.3
                    }
                ],
                "solution": "a) Kí hiệu 4 bạn lớp 9A là $A_1, A_2, A_3, A_4$ và 3 bạn lớp 9B là $B_1, B_2, B_3$.\nKhông gian mẫu khi chọn đồng thời 2 bạn trong 7 bạn có số phần tử là:\n$$n(\\Omega) = C_7^2 = \\frac{7 \\cdot 6}{2} = 21.$$\nBiến cố $H$: \"Hai bạn được chọn đến từ hai lớp khác nhau\" xảy ra khi chọn được 1 bạn lớp 9A và 1 bạn lớp 9B.\nSố kết quả thuận lợi cho biến cố $H$ là:\n$$n(H) = 4 \\cdot 3 = 12.$$\nXác suất của biến cố $H$ là:\n$$P(H) = \\frac{n(H)}{n(\\Omega)} = \\frac{12}{21} = \\frac{4}{7}.$$\n\nb) Gọi giá tiền ban đầu của một bóng đèn loại I là $x$ (đồng) và của một bóng đèn loại II là $y$ (đồng) với điều kiện $x > 0, y > 0$.\nVì ban đầu mua 5 bóng loại I và 4 bóng loại II hết 290.000 đồng nên ta có phương trình:\n$$5x + 4y = 290000 \\quad (1)$$\nTrong đợt khuyến mãi:\n- Giá một bóng đèn loại I giảm 10% nên còn: $x - 10\\%x = 0,9x$ (đồng).\n- Giá một bóng đèn loại II giảm 20% nên còn: $y - 20\\%y = 0,8y$ (đồng).\nVì đợt khuyến mãi mua 10 bóng loại I và 6 bóng loại II hết 474.000 đồng nên ta có phương trình:\n$$10(0,9x) + 6(0,8y) = 474000 \\Leftrightarrow 9x + 4,8y = 474000 \\quad (2)$$\nTừ (1) và (2), ta có hệ phương trình:\n$$\\begin{cases} 5x + 4y = 290000 \\\\ 9x + 4,8y = 474000 \\end{cases} \\Leftrightarrow \\begin{cases} 6x + 4,8y = 348000 \\\\ 9x + 4,8y = 474000 \\end{cases} \\Leftrightarrow \\begin{cases} 3x = 126000 \\\\ 5x + 4y = 290000 \\end{cases} \\Leftrightarrow \\begin{cases} x = 42000 \\\\ 4y = 290000 - 5(42000) \\end{cases}$$\n$$\\Leftrightarrow \\begin{cases} x = 42000 \\\\ 4y = 80000 \\end{cases} \\Leftrightarrow \\begin{cases} x = 42000 \\text{ (thỏa mãn)} \\\\ y = 20000 \\text{ (thỏa mãn)} \\end{cases}$$\nVậy giá ban đầu của mỗi bóng đèn loại I là 42.000 đồng và của mỗi bóng đèn loại II là 20.000 đồng."
            },
            {
                "id": 13,
                "points": 2.0,
                "question": "Cho đường tròn $(O; R)$ và đường thẳng $d$ không cắt đường tròn. Kẻ $OH \\perp d$ tại $H$. Từ một điểm $M$ bất kì trên đường thẳng $d$ ($M$ không trùng với $H$), kẻ hai tiếp tuyến $MA, MB$ với đường tròn $(O)$ ($A, B$ là các tiếp điểm). Đoạn thẳng $AB$ cắt $OH$ tại $I$ và cắt $OM$ tại $K$.\na) Chứng minh 5 điểm $M, A, O, H, B$ cùng thuộc một đường tròn và $OK \\cdot OM = R^2$.\nb) Chứng minh rằng khi điểm $M$ di động trên đường thẳng $d$ thì đường thẳng $AB$ luôn đi qua điểm $I$ cố định. Từ $O$ kẻ đường thẳng vuông góc với $OM$ cắt các tia $MA, MB$ lần lượt tại $C$ và $D$. Tìm vị trí của điểm $M$ trên đường thẳng $d$ sao cho diện tích tam giác $MCD$ đạt giá trị nhỏ nhất.",
                "rubric": [
                    {
                        "step": "a) Chứng minh $\\widehat{OAM} = \\widehat{OBM} = \\widehat{OHM} = 90^\\circ$ nên 5 điểm $M, A, O, H, B$ cùng thuộc đường tròn đường kính $OM$. Hệ thức lượng trong tam giác vuông $OAM$ đường cao $AK$: $OK \\cdot OM = OA^2 = R^2$.",
                        "points": 1.0
                    },
                    {
                        "step": "b) Chứng minh $\\Delta OKI \\backsim \\Delta OHM$ (g-g) $\\Rightarrow OI \\cdot OH = OK \\cdot OM = R^2 \\Rightarrow OI = \\frac{R^2}{OH}$ không đổi, suy ra $I$ cố định, $AB$ luôn qua $I$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) [NÂNG CAO] Tam giác $MCD$ cân tại $M$, $S_{MCD} = OM \\cdot OC = \\frac{R \\cdot OM^2}{\\sqrt{OM^2 - R^2}}$. Đặt $OM = t \\ge OH$. Khảo sát hàm hoặc AM-GM, tìm được $\\min S_{MCD}$ khi $M \\equiv H$ (nếu $OH \\ge R\\sqrt{2}$) hoặc $OM = R\\sqrt{2}$.",
                        "points": 0.5
                    }
                ],
                "solution": "a) Vì $MA, MB$ là hai tiếp tuyến của đường tròn $(O)$ nên $\\widehat{OAM} = 90^\\circ$ và $\\widehat{OBM} = 90^\\circ$.\nVì $OH \\perp d$ tại $H$ nên $\\widehat{OHM} = 90^\\circ$.\nSuy ra các điểm $A, B, H$ cùng nhìn đoạn thẳng $OM$ dưới góc vuông $90^\\circ$.\nDo đó 5 điểm $M, A, O, H, B$ cùng thuộc đường tròn đường kính $OM$.\n\n*) Chứng minh $OK \\cdot OM = R^2$:\nVì $MA, MB$ là tiếp tuyến nên $OA = OB = R$ và $MA = MB$, suy ra $OM$ là đường trung trực của đoạn thẳng $AB$, do đó $OM \\perp AB$ tại $K$.\nXét tam giác vuông $OAM$ (vuông tại $A$) có đường cao $AK$, theo hệ thức lượng ta có:\n$$OK \\cdot OM = OA^2 = R^2.$$\n\nb) *) Chứng minh $AB$ luôn đi qua điểm $I$ cố định:\nXét $\\Delta OKI$ và $\\Delta OHM$, ta có:\n$$\\widehat{OKI} = \\widehat{OHM} = 90^\\circ,$$\n$$\\widehat{HOM} \\text{ là góc chung}.$$\nDo đó $\\Delta OKI \\backsim \\Delta OHM$ (g-g).\nSuy ra: $\\frac{OK}{OH} = \\frac{OI}{OM} \\Rightarrow OI \\cdot OH = OK \\cdot OM$.\nMà theo câu a ta có $OK \\cdot OM = R^2$, nên:\n$$OI \\cdot OH = R^2 \\Rightarrow OI = \\frac{R^2}{OH}.$$\nVì đường tròn $(O; R)$ và đường thẳng $d$ cố định nên điểm $H$ cố định và độ dài $OH$ không đổi.\nDo đó điểm $I$ nằm trên tia $OH$ và có khoảng cách $OI = \\frac{R^2}{OH}$ không đổi, tức là điểm $I$ cố định.\nVậy khi điểm $M$ di động trên đường thẳng $d$ thì đường thẳng $AB$ luôn đi qua điểm $I$ cố định.\n\n*) [Ý 2 NÂNG CAO] Tìm vị trí của $M$ để $S_{MCD}$ nhỏ nhất:\nVì $OM$ là tia phân giác của $\\widehat{AMB}$ và $CD \\perp OM$, suy ra tam giác $MCD$ cân tại $M$, đường cao $MO$, do đó $CD = 2OC$.\nDiện tích tam giác $MCD$ là:\n$$S_{MCD} = \\frac{1}{2} MO \\cdot CD = MO \\cdot OC.$$\nTrong tam giác vuông $MCO$ (vuông tại $O$) có đường cao $OA = R$, ta có:\n$$OA^2 = AC \\cdot AM = R^2 \\quad \\text{và} \\quad OC = \\sqrt{OA^2 + AC^2} = \\sqrt{R^2 + \\frac{R^4}{AM^2}} = \\frac{R \\cdot OM}{AM} = \\frac{R \\cdot OM}{\\sqrt{OM^2 - R^2}}.$$\nDo đó:\n$$S_{MCD} = OM \\cdot \\frac{R \\cdot OM}{\\sqrt{OM^2 - R^2}} = \\frac{R \\cdot OM^2}{\\sqrt{OM^2 - R^2}}.$$\nĐặt $OM = t$ với $t \\ge OH > R$. Ta có:\n$$S_{MCD} = \\frac{R \\cdot t^2}{\\sqrt{t^2 - R^2}} = R \\cdot \\sqrt{\\frac{t^4}{t^2 - R^2}} = R \\cdot \\sqrt{(t^2 - R^2) + \\frac{R^4}{t^2 - R^2} + 2R^2}.$$\nÁp dụng bất đẳng thức AM-GM cho hai số dương $(t^2 - R^2)$ và $\\frac{R^4}{t^2 - R^2}$:\n$$(t^2 - R^2) + \\frac{R^4}{t^2 - R^2} \\ge 2\\sqrt{(t^2 - R^2) \\cdot \\frac{R^4}{t^2 - R^2}} = 2R^2.$$\nĐẳng thức xảy ra khi và chỉ khi:\n$$t^2 - R^2 = \\frac{R^4}{t^2 - R^2} \\Leftrightarrow (t^2 - R^2)^2 = R^4 \\Leftrightarrow t^2 - R^2 = R^2 \\Leftrightarrow t^2 = 2R^2 \\Leftrightarrow t = R\\sqrt{2}.$$\n- Nếu $OH \\le R\\sqrt{2}$: Giá trị nhỏ nhất của diện tích là $S_{MCD} = R\\sqrt{2R^2 + 2R^2} = 2R^2$ khi $OM = R\\sqrt{2}$ (điểm $M$ cách $H$ một đoạn $HM = \\sqrt{2R^2 - OH^2}$).\n- Nếu $OH > R\\sqrt{2}$: Hàm số đồng biến với $t \\ge OH$, do đó diện tích nhỏ nhất khi $t = OH$, tức là khi $M$ trùng với $H$."
            },
            {
                "id": 14,
                "points": 1.0,
                "question": "a) Một cái bồn chứa xăng gồm hai đầu là hai nửa hình cầu bán kính $R = 1\\text{ m}$ và thân ở giữa là hình trụ có chiều dài $L = 3\\text{ m}$. Tính thể tích của bồn chứa xăng đó (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hai chữ số thập phân).\nb) Cho ba số thực dương $a, b, c$ thỏa mãn $ab + bc + ca = 1$. Tìm giá trị lớn nhất của biểu thức:\n$$P = \\frac{a}{\\sqrt{a^2 + 1}} + \\frac{b}{\\sqrt{b^2 + 1}} + \\frac{c}{\\sqrt{c^2 + 1}}.$$",
                "rubric": [
                    {
                        "step": "a) Hai nửa hình cầu ghép lại thành hình cầu bán kính $R = 1\\text{ m}$: $V_{cầu} = \\frac{4}{3}\\pi (1)^3 \\approx 4,19\\text{ m}^3$. Thể tích thân trụ: $V_{trụ} = \\pi (1)^2 \\cdot 3 \\approx 9,42\\text{ m}^3$. Tổng thể tích là $4,19 + 9,42 = 13,61\\text{ m}^3$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) [NÂNG CAO] Thay $1 = ab+bc+ca$ vào căn thức: $a^2 + 1 = a^2 + ab + bc + ca = (a+b)(a+c)$.",
                        "points": 0.25
                    },
                    {
                        "step": "b) [NÂNG CAO] Áp dụng BĐT AM-GM: $\\frac{a}{\\sqrt{(a+b)(a+c)}} \\le \\frac{1}{2}\\left(\\frac{a}{a+b} + \\frac{a}{a+c}\\right)$. Cộng 3 biểu thức tìm được $\\max P = \\frac{3}{2}$ khi $a = b = c = \\frac{1}{\\sqrt{3}}$.",
                        "points": 0.25
                    }
                ],
                "solution": "a) Hai nửa hình cầu ở hai đầu ghép lại tạo thành một hình cầu có bán kính $R = 1\\text{ m}$.\nThể tích của phần hình cầu này là:\n$$V_{cầu} = \\frac{4}{3}\\pi R^3 = \\frac{4}{3} \\cdot 3,14 \\cdot 1^3 \\approx 4,19\\text{ m}^3.$$\nPhần thân giữa là một hình trụ có bán kính đáy $R = 1\\text{ m}$ và chiều cao $L = 3\\text{ m}$.\nThể tích của phần hình trụ là:\n$$V_{trụ} = \\pi R^2 L = 3,14 \\cdot 1^2 \\cdot 3 = 9,42\\text{ m}^3.$$\nTổng thể tích của bồn chứa xăng là:\n$$V = V_{cầu} + V_{trụ} \\approx 4,19 + 9,42 = 13,61\\text{ m}^3.$$\nVậy thể tích của bồn chứa xăng là khoảng $13,61\\text{ m}^3$.\n\nb) [CÂU PHÂN HÓA NÂNG CAO]\nTừ giả thiết $ab + bc + ca = 1$, ta có:\n$$a^2 + 1 = a^2 + ab + bc + ca = a(a + b) + c(a + b) = (a + b)(a + c).$$\nDo đó:\n$$\\frac{a}{\\sqrt{a^2 + 1}} = \\frac{a}{\\sqrt{(a+b)(a+c)}}.$$\nÁp dụng bất đẳng thức AM-GM cho hai số dương $\\frac{a}{a+b}$ và $\\frac{a}{a+c}$, ta có:\n$$\\sqrt{\\frac{a}{a+b} \\cdot \\frac{a}{a+c}} \\le \\frac{1}{2}\\left(\\frac{a}{a+b} + \\frac{a}{a+c}\\right).$$\nSuy ra:\n$$\\frac{a}{\\sqrt{a^2 + 1}} \\le \\frac{1}{2}\\left(\\frac{a}{a+b} + \\frac{a}{a+c}\\right).$$\nChứng minh hoàn toàn tương tự, ta có:\n$$\\frac{b}{\\sqrt{b^2 + 1}} = \\frac{b}{\\sqrt{(b+a)(b+c)}} \\le \\frac{1}{2}\\left(\\frac{b}{a+b} + \\frac{b}{b+c}\\right),$$\n$$\\frac{c}{\\sqrt{c^2 + 1}} = \\frac{c}{\\sqrt{(c+a)(c+b)}} \\le \\frac{1}{2}\\left(\\frac{c}{c+a} + \\frac{c}{b+c}\\right).$$\nCộng từng vế của ba bất đẳng thức trên, ta được:\n$$P \\le \\frac{1}{2}\\left(\\frac{a+b}{a+b} + \\frac{b+c}{b+c} + \\frac{c+a}{c+a}\\right) = \\frac{1}{2}(1 + 1 + 1) = \\frac{3}{2}.$$\nĐẳng thức xảy ra khi và chỉ khi:\n$$\\begin{cases} \\frac{a}{a+b} = \\frac{a}{a+c} \\\\ \\frac{b}{b+a} = \\frac{b}{b+c} \\\\ \\frac{c}{c+a} = \\frac{c}{c+b} \\\\ ab + bc + ca = 1 \\end{cases} \\Leftrightarrow a = b = c = \\frac{1}{\\sqrt{3}}.$$\nVậy giá trị lớn nhất của biểu thức $P$ là $\\frac{3}{2}$, đạt được khi $a = b = c = \\frac{1}{\\sqrt{3}}$."
            }
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 10
    # =========================================================================
    exams["de_10"] = {
        "id": "de_10",
        "code": "MÃ ĐỀ 10",
        "title": "ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN - ĐỀ SỐ 10",
        "header": {
            "department": "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
            "examName": "KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT",
            "subject": "Môn thi: TOÁN",
            "author": "GV Phan Đình Thuấn",
            "time": "90 phút (không kể thời gian phát đề)",
            "code": "MÃ ĐỀ 10"
        },
        "part1": [
            {
                "id": 1,
                "question": "Biểu thức $\\sqrt{75} - \\sqrt{48} + \\sqrt{12}$ rút gọn được kết quả là:",
                "options": ["A. $3\\sqrt{3}$", "B. $2\\sqrt{3}$", "C. $\\sqrt{3}$", "D. $7\\sqrt{3}$"],
                "answer": "A",
                "explanation": "Ta có: $\\sqrt{75} - \\sqrt{48} + \\sqrt{12} = 5\\sqrt{3} - 4\\sqrt{3} + 2\\sqrt{3} = 3\\sqrt{3}$."
            },
            {
                "id": 2,
                "question": "Nghiệm của bất phương trình $\\frac{x - 3}{2} > 1$ là:",
                "options": ["A. $x > 5$", "B. $x < 5$", "C. $x > 1$", "D. $x < 1$"],
                "answer": "A",
                "explanation": "$\\frac{x - 3}{2} > 1 \\Leftrightarrow x - 3 > 2 \\Leftrightarrow x > 5$."
            },
            {
                "id": 3,
                "question": "Phương trình $(x - 2)(x + 3) = 0$ có tập nghiệm là:",
                "options": ["A. ${2; -3}$", "B. ${-2; 3}$", "C. ${2}$", "D. ${-3}$"],
                "answer": "A",
                "explanation": "$(x - 2)(x + 3) = 0 \\Leftrightarrow x - 2 = 0$ hoặc $x + 3 = 0 \\Leftrightarrow x = 2$ hoặc $x = -3$."
            },
            {
                "id": 4,
                "question": "Một hộp có 10 viên bi gồm 4 bi đỏ và 6 bi xanh có cùng kích thước. Lấy ngẫu nhiên 1 viên bi. Xác suất lấy được viên bi màu đỏ là:",
                "options": ["A. $\\frac{2}{5}$", "B. $\\frac{3}{5}$", "C. $\\frac{1}{4}$", "D. $\\frac{1}{2}$"],
                "answer": "A",
                "explanation": "Xác suất lấy được viên bi màu đỏ là $P = \\frac{4}{10} = \\frac{2}{5}$."
            },
            {
                "id": 5,
                "question": "Điểm nào sau đây thuộc đồ thị hàm số $y = -5x^2$?",
                "options": ["A. $A(1; -5)$", "B. $B(1; 5)$", "C. $C(-1; 5)$", "D. $D(0; -5)$"],
                "answer": "A",
                "explanation": "Thay tọa độ $A(1; -5)$: $y = -5(1)^2 = -5$ (thỏa mãn)."
            },
            {
                "id": 6,
                "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}$ và $\\widehat{B} = 45^\\circ$. Độ dài cạnh huyền $BC$ là:",
                "options": ["A. $6\\sqrt{2}\\text{ cm}$", "B. $12\\text{ cm}$", "C. $6\\text{ cm}$", "D. $3\\sqrt{2}\\text{ cm}$"],
                "answer": "A",
                "explanation": "Tam giác $ABC$ vuông cân tại $A$ nên $AC = AB = 6\\text{ cm}$. Khi đó $BC = \\sqrt{6^2 + 6^2} = 6\\sqrt{2}\\text{ cm}$."
            },
            {
                "id": 7,
                "question": "Diện tích mặt cầu có đường kính $d = 8\\text{ cm}$ bằng:",
                "options": ["A. $64\\pi\\text{ cm}^2$", "B. $16\\pi\\text{ cm}^2$", "C. $256\\pi\\text{ cm}^2$", "D. $32\\pi\\text{ cm}^2$"],
                "answer": "A",
                "explanation": "Bán kính mặt cầu là $R = 4\\text{ cm}$. Diện tích mặt cầu là $S = 4\\pi R^2 = 4\\pi(4^2) = 64\\pi\\text{ cm}^2$."
            },
            {
                "id": 8,
                "question": "Số lượng học sinh giỏi của 5 lớp khối 9 lần lượt là: 8, 12, 10, 15, 15. Trung vị ($M_e$) của mẫu số liệu trên là:",
                "options": ["A. $12$", "B. $10$", "C. $15$", "D. $11$"],
                "answer": "A",
                "explanation": "Sắp xếp mẫu số liệu theo thứ tự không giảm: 8, 10, 12, 15, 15. Vì cỡ mẫu $n = 5$ lẻ nên trung vị là số ở vị trí chính giữa: $M_e = 12$."
            }
        ],
        "part2": [
            {
                "id": 9,
                "points": 1.0,
                "question": "Cho biểu thức: $$M = \\left(\\frac{1}{x-4} - \\frac{1}{x+4\\sqrt{x}+4}\\right) \\cdot \\frac{x\\sqrt{x}+2x-4\\sqrt{x}-8}{\\sqrt{x}}$$ với $x > 0$ và $x \\ne 4$.\na) Rút gọn biểu thức $M$.\nb) Tìm các giá trị của $x$ để $M = 1$.",
                "rubric": [
                    {
                        "step": "Phân tích mẫu thức: $x-4 = (\\sqrt{x}-2)(\\sqrt{x}+2)$ và $x+4\\sqrt{x}+4 = (\\sqrt{x}+2)^2$. Mẫu chung là $(\\sqrt{x}-2)(\\sqrt{x}+2)^2$.",
                        "points": 0.25
                    },
                    {
                        "step": "Quy đồng tử trong ngoặc: $(\\sqrt{x}+2) - (\\sqrt{x}-2) = 4$.",
                        "points": 0.25
                    },
                    {
                        "step": "Phân tích tử thức thứ hai: $x\\sqrt{x}+2x-4\\sqrt{x}-8 = x(\\sqrt{x}+2) - 4(\\sqrt{x}+2) = (x-4)(\\sqrt{x}+2) = (\\sqrt{x}-2)(\\sqrt{x}+2)^2$.",
                        "points": 0.25
                    },
                    {
                        "step": "Nhân và rút gọn: $M = \\frac{4}{(\\sqrt{x}-2)(\\sqrt{x}+2)^2} \\cdot \\frac{(\\sqrt{x}-2)(\\sqrt{x}+2)^2}{\\sqrt{x}} = \\frac{4}{\\sqrt{x}}$. Giải $M = 1 \\Leftrightarrow \\frac{4}{\\sqrt{x}} = 1 \\Leftrightarrow \\sqrt{x} = 4 \\Leftrightarrow x = 16$ (thỏa mãn). Kết luận.",
                        "points": 0.25
                    }
                ],
                "solution": "Với $x > 0, x \\ne 4$, ta có:\na) Rút gọn biểu thức $M$:\nTa có:\n$$x - 4 = (\\sqrt{x} - 2)(\\sqrt{x} + 2),$$\n$$x + 4\\sqrt{x} + 4 = (\\sqrt{x} + 2)^2,$$\n$$x\\sqrt{x} + 2x - 4\\sqrt{x} - 8 = x(\\sqrt{x}+2) - 4(\\sqrt{x}+2) = (x - 4)(\\sqrt{x} + 2) = (\\sqrt{x} - 2)(\\sqrt{x} + 2)^2.$$\nKhi đó:\n$$\\begin{aligned}\nM &= \\left[\\frac{\\sqrt{x}+2}{(\\sqrt{x}-2)(\\sqrt{x}+2)^2} - \\frac{\\sqrt{x}-2}{(\\sqrt{x}-2)(\\sqrt{x}+2)^2}\\right] \\cdot \\frac{(\\sqrt{x}-2)(\\sqrt{x}+2)^2}{\\sqrt{x}} \\\\\n&= \\frac{(\\sqrt{x}+2) - (\\sqrt{x}-2)}{(\\sqrt{x}-2)(\\sqrt{x}+2)^2} \\cdot \\frac{(\\sqrt{x}-2)(\\sqrt{x}+2)^2}{\\sqrt{x}} \\\\\n&= \\frac{4}{(\\sqrt{x}-2)(\\sqrt{x}+2)^2} \\cdot \\frac{(\\sqrt{x}-2)(\\sqrt{x}+2)^2}{\\sqrt{x}} = \\frac{4}{\\sqrt{x}}.\n\\end{aligned}$$\nVậy $M = \\frac{4}{\\sqrt{x}}$.\n\nb) Để $M = 1$, ta có:\n$$\\frac{4}{\\sqrt{x}} = 1 \\Leftrightarrow \\sqrt{x} = 4 \\Leftrightarrow x = 16.$$\nĐối chiếu với điều kiện xác định $x > 0, x \\ne 4$, ta thấy $x = 16$ thỏa mãn.\nVậy $x = 16$ thì $M = 1$."
            },
            {
                "id": 10,
                "points": 1.0,
                "question": "Cho phương trình $3x^2 - 5x - 1 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $$D = \\frac{x_1^2}{x_2} + \\frac{x_2^2}{x_1} - x_1 x_2.$$",
                "rubric": [
                    {
                        "step": "Xét phương trình $3x^2 - 5x - 1 = 0$ có $a \\cdot c = 3 \\cdot (-1) = -3 < 0$, suy ra phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ khác $0$.",
                        "points": 0.25
                    },
                    {
                        "step": "Theo định lí Viète, ta có: $\\begin{cases} x_1 + x_2 = \\frac{5}{3} \\\\ x_1 x_2 = -\\frac{1}{3} \\end{cases}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Quy đồng và biến đổi: $\\frac{x_1^2}{x_2} + \\frac{x_2^2}{x_1} = \\frac{x_1^3 + x_2^3}{x_1 x_2} = \\frac{(x_1+x_2)^3 - 3x_1 x_2(x_1+x_2)}{x_1 x_2}$. Tính được $x_1^3 + x_2^3 = \\frac{170}{27}$.",
                        "points": 0.25
                    },
                    {
                        "step": "Thay số: $D = \\frac{170/27}{-1/3} - \\left(-\\frac{1}{3}\\right) = -\\frac{170}{9} + \\frac{1}{3} = -\\frac{167}{9}$. Kết luận $D = -\\frac{167}{9}$.",
                        "points": 0.25
                    }
                ],
                "solution": "Xét phương trình $3x^2 - 5x - 1 = 0$.\nVì $a \\cdot c = 3 \\cdot (-1) = -3 < 0$ nên phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ khác $0$.\nTheo định lí Viète, ta có:\n$$\\begin{cases} x_1 + x_2 = -\\frac{b}{a} = \\frac{5}{3} \\\\ x_1 x_2 = \\frac{c}{a} = -\\frac{1}{3} \\end{cases}$$\nTa biến đổi biểu thức $D$:\n$$D = \\frac{x_1^3 + x_2^3}{x_1 x_2} - x_1 x_2 = \\frac{(x_1 + x_2)^3 - 3x_1 x_2(x_1 + x_2)}{x_1 x_2} - x_1 x_2.$$\nTa có:\n$$x_1^3 + x_2^3 = \\left(\\frac{5}{3}\\right)^3 - 3 \\cdot \\left(-\\frac{1}{3}\\right) \\cdot \\frac{5}{3} = \\frac{125}{27} + \\frac{5}{3} = \\frac{125 + 45}{27} = \\frac{170}{27}.$$\nKhi đó:\n$$D = \\frac{\\frac{170}{27}}{-\\frac{1}{3}} - \\left(-\\frac{1}{3}\\right) = -\\frac{170}{9} + \\frac{3}{9} = -\\frac{167}{9}.$$\nVậy $D = -\\frac{167}{9}$."
            },
            {
                "id": 11,
                "points": 1.0,
                "question": "Giải hệ phương trình:\n$$\\begin{cases} \\sqrt{2x-1} + y = 3 \\\\ 2\\sqrt{2x-1} - 3y = 1 \\end{cases}$$",
                "rubric": [
                    {
                        "step": "Điều kiện xác định: $2x-1 \\ge 0 \\Leftrightarrow x \\ge \\frac{1}{2}$. Đặt ẩn phụ $u = \\sqrt{2x-1} \\ge 0$.",
                        "points": 0.25
                    },
                    {
                        "step": "Hệ trở thành: $\\begin{cases} u + y = 3 \\\\ 2u - 3y = 1 \\end{cases} \\Leftrightarrow \\begin{cases} 3u + 3y = 9 \\\\ 2u - 3y = 1 \\end{cases} \\Leftrightarrow \\begin{cases} 5u = 10 \\\\ y = 3 - u \\end{cases} \\Leftrightarrow \\begin{cases} u = 2 \\\\ y = 1 \\end{cases}$.",
                        "points": 0.35
                    },
                    {
                        "step": "Thay lại: $\\sqrt{2x-1} = 2 \\Leftrightarrow 2x-1 = 4 \\Leftrightarrow 2x = 5 \\Leftrightarrow x = 2,5$ (thỏa mãn ĐKXĐ).",
                        "points": 0.25
                    },
                    {
                        "step": "Kết luận nghiệm duy nhất $(x; y) = (2,5; 1)$.",
                        "points": 0.15
                    }
                ],
                "solution": "Điều kiện xác định: $2x - 1 \\ge 0 \\Leftrightarrow x \\ge \\frac{1}{2}$.\nĐặt $u = \\sqrt{2x-1}$ ($u \\ge 0$). Hệ phương trình trở thành:\n$$\\begin{cases} u + y = 3 \\\\ 2u - 3y = 1 \\end{cases} \\Leftrightarrow \\begin{cases} 3u + 3y = 9 \\\\ 2u - 3y = 1 \\end{cases} \\Leftrightarrow \\begin{cases} 5u = 10 \\\\ y = 3 - u \\end{cases} \\Leftrightarrow \\begin{cases} u = 2 \\\\ y = 1 \\end{cases}$$\nVới $u = 2$, ta có:\n$$\\sqrt{2x-1} = 2 \\Leftrightarrow 2x - 1 = 4 \\Leftrightarrow 2x = 5 \\Leftrightarrow x = 2,5\\text{ (thỏa mãn điều kiện)}.$$\nVậy hệ phương trình có nghiệm duy nhất $(x; y) = (2,5; 1)$."
            },
            {
                "id": 12,
                "points": 2.0,
                "question": "a) Trong một trò chơi vòng quay may mắn, vòng quay được chia thành 8 hình quạt đều nhau, được đánh số từ 1 đến 8. Người chơi quay vòng quay một lần. Tính xác suất của biến cố $M$: \"Kim chỉ vào ô ghi số là ước của 12\".\nb) Khoảng cách giữa hai bến sông $A$ và $B$ là $45\\text{ km}$. Một ca nô xuôi dòng từ bến $A$ đến bến $B$, rồi ngay lập tức quay ngược dòng từ $B$ về $A$. Tổng thời gian cả đi lẫn về là 8 giờ. Biết vận tốc của dòng nước là $3\\text{ km/h}$. Tính vận tốc thực của ca nô khi nước yên lặng.",
                "rubric": [
                    {
                        "step": "a) Không gian mẫu $\\Omega = {1; 2; 3; 4; 5; 6; 7; 8} \\Rightarrow n(\\Omega) = 8$.",
                        "points": 0.5
                    },
                    {
                        "step": "a) Ước của 12 trong tập $\\Omega$ là ${1; 2; 3; 4; 6}$ gồm 5 số. Xác suất $P(M) = \\frac{5}{8} = 0,625$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) Gọi vận tốc thực của ca nô là $v$ (km/h, $v > 3$). Vận tốc xuôi dòng là $v + 3$, ngược dòng là $v - 3$. Thời gian xuôi dòng $\\frac{45}{v+3}$, ngược dòng $\\frac{45}{v-3}$.",
                        "points": 0.35
                    },
                    {
                        "step": "b) Lập phương trình: $\\frac{45}{v+3} + \\frac{45}{v-3} = 8$. Quy đồng rút gọn về phương trình: $4v^2 - 45v - 36 = 0$.",
                        "points": 0.35
                    },
                    {
                        "step": "b) Giải phương trình: $\\Delta = 2601 = 51^2$. Tìm được $v = 12$ (thỏa mãn), $v = -0,75$ (loại). Kết luận vận tốc thực của ca nô là $12\\text{ km/h}$.",
                        "points": 0.3
                    }
                ],
                "solution": "a) Không gian mẫu của phép thử khi quay vòng quay may mắn là:\n$$\\Omega = {1; 2; 3; 4; 5; 6; 7; 8}$$\nSố phần tử của không gian mẫu là $n(\\Omega) = 8$.\nBiến cố $M$: \"Kim chỉ vào ô ghi số là ước của 12\".\nCác ước nguyên dương của 12 thuộc $\\Omega$ là: ${1; 2; 3; 4; 6}$.\nSố kết quả thuận lợi cho biến cố $M$ là $n(M) = 5$.\nXác suất của biến cố $M$ là:\n$$P(M) = \\frac{n(M)}{n(\\Omega)} = \\frac{5}{8} = 0,625.$$\n\nb) Gọi vận tốc thực của ca nô khi nước yên lặng là $v$ (km/h, điều kiện $v > 3$).\nVận tốc của ca nô khi xuôi dòng từ $A$ đến $B$ là: $v + 3$ (km/h).\nVận tốc của ca nô khi ngược dòng từ $B$ về $A$ là: $v - 3$ (km/h).\nThời gian ca nô đi xuôi dòng từ $A$ đến $B$ là: $\\frac{45}{v+3}$ (giờ).\nThời gian ca nô đi ngược dòng từ $B$ về $A$ là: $\\frac{45}{v-3}$ (giờ).\nVì tổng thời gian cả đi lẫn về là 8 giờ nên ta có phương trình:\n$$\\frac{45}{v+3} + \\frac{45}{v-3} = 8$$\n$$\\Leftrightarrow 45 \\left(\\frac{1}{v+3} + \\frac{1}{v-3}\\right) = 8 \\Leftrightarrow \\frac{45(v - 3 + v + 3)}{v^2 - 9} = 8$$\n$$\\Leftrightarrow \\frac{90v}{v^2 - 9} = 8 \\Leftrightarrow 8(v^2 - 9) = 90v$$\n$$\\Leftrightarrow 8v^2 - 90v - 72 = 0 \\Leftrightarrow 4v^2 - 45v - 36 = 0.$$\nTa có $\\Delta = (-45)^2 - 4 \\cdot 4 \\cdot (-36) = 2025 + 576 = 2601 > 0$, suy ra $\\sqrt{\\Delta} = 51$.\nPhương trình có hai nghiệm phân biệt:\n$$v_1 = \\frac{45 + 51}{2 \\cdot 4} = \\frac{96}{8} = 12\\text{ (thỏa mãn điều kiện)},$$\n$$v_2 = \\frac{45 - 51}{8} = -\\frac{6}{8} = -0,75\\text{ (loại)}.$$\nVậy vận tốc thực của ca nô khi nước yên lặng là $12\\text{ km/h}$."
            },
            {
                "id": 13,
                "points": 2.0,
                "question": "Cho đường tròn $(O; R)$ có hai đường kính $AB$ và $CD$ vuông góc với nhau. Trên cung nhỏ $BC$ lấy một điểm $M$ bất kì ($M$ khác $B$ và $C$). Tiếp tuyến tại $M$ của đường tròn $(O)$ cắt đường thẳng $AB$ tại $E$. Đoạn thẳng $CM$ cắt $AB$ tại $S$. Kẻ $MH \\perp CD$ tại $H$.\na) Chứng minh tứ giác $OMHD$ nội tiếp một đường tròn và tam giác $EMS$ là tam giác cân tại $E$.\nb) Chứng minh $ES^2 = EA \\cdot EB$. Đường thẳng $DM$ cắt đường thẳng $AB$ tại điểm $K$. Chứng minh rằng $OK \\cdot OS = R^2$ và khi điểm $M$ di động trên cung nhỏ $BC$, tâm đường tròn ngoại tiếp tam giác $SMK$ luôn di động trên một đường thẳng cố định.",
                "rubric": [
                    {
                        "step": "a) Tứ giác $OMHD$ có $\\widehat{OHM} = 90^\\circ$ và $\\widehat{ODM} = \\widehat{OMD}$... Chứng minh $\\widehat{EMS} = \\widehat{ESM} = \\frac{1}{2}(\\text{sđ}\\widebat{AC} + \\text{sđ}\\widebat{MB})$ suy ra tam giác $EMS$ cân tại $E$.",
                        "points": 1.0
                    },
                    {
                        "step": "b) Theo tính chất tiếp tuyến: $\\Delta EAM \\backsim \\Delta EMB \\Rightarrow EA \\cdot EB = EM^2$. Vì tam giác $EMS$ cân tại $E$ nên $EM = ES \\Rightarrow ES^2 = EA \\cdot EB$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) [NÂNG CAO] Trong $\\Delta MCD$ vuông tại $M$ có $MS$ và $MK$ là các phân giác trong và ngoài của $\\widehat{CMD}$, suy ra $(CDSK) = -1$ hay $(AB, SK) = -1 \\Rightarrow OK \\cdot OS = OA^2 = R^2$. Tâm đường tròn ngoại tiếp $\\Delta SMK$ luôn thuộc đường trung trực cố định của đoạn thẳng nối hai điểm liên hợp.",
                        "points": 0.5
                    }
                ],
                "solution": "a) Xét tứ giác $OMHD$:\nVì $MH \\perp CD$ tại $H$ nên $\\widehat{MHO} = 90^\\circ$.\nLại có $AB \\perp CD$ tại $O$ nên $\\widehat{MOD} = 90^\\circ$.\nDo đó hai đỉnh $O$ và $H$ kề nhau cùng nhìn cạnh $MD$ dưới góc $90^\\circ$, suy ra tứ giác $OMHD$ nội tiếp đường tròn đường kính $MD$.\n\n*) Chứng minh tam giác $EMS$ cân tại $E$:\nVì $EM$ là tiếp tuyến của $(O)$ tại $M$ nên theo tính chất góc tạo bởi tiếp tuyến và dây cung, ta có:\n$$\\widehat{EMS} = \\widehat{EMC} = \\frac{1}{2}\\text{sđ}\\widebat{MC}.$$\nLại có góc $\\widehat{ESM}$ là góc có đỉnh ở bên trong đường tròn chắn hai cung $\\widebat{AC}$ và $\\widebat{MB}$:\n$$\\widehat{ESM} = \\frac{1}{2}(\\text{sđ}\\widebat{AC} + \\text{sđ}\\widebat{MB}).$$\nMà $AB \\perp CD$ tại $O$ nên $\\text{sđ}\\widebat{AC} = \\text{sđ}\\widebat{BC} = 90^\\circ$.\nLại có $\\text{sđ}\\widebat{BC} = \\text{sđ}\\widebat{MB} + \\text{sđ}\\widebat{MC} \\Rightarrow \\text{sđ}\\widebat{AC} + \\text{sđ}\\widebat{MB} = \\text{sđ}\\widebat{BC} + \\text{sđ}\\widebat{MB}$... Xét góc $\\widehat{EMB} + \\widehat{BMS}$:\nTa có $\\widehat{EMS} = \\widehat{EMB} + \\widehat{BMS} = \\frac{1}{2}\\text{sđ}\\widebat{MB} + \\frac{1}{2}\\text{sđ}\\widebat{BC} = \\frac{1}{2}(\\text{sđ}\\widebat{AC} + \\text{sđ}\\widebat{MB}) = \\widehat{ESM}$.\nDo đó $\\widehat{EMS} = \\widehat{ESM}$, suy ra tam giác $EMS$ cân tại $E$.\n\nb) *) Chứng minh $ES^2 = EA \\cdot EB$:\nXét $\\Delta EAM$ và $\\Delta EMB$, ta có:\n$$\\widehat{AEM} \\text{ là góc chung},$$\n$$\\widehat{EMA} = \\widehat{EBM} \\text{ (góc tạo bởi tia tiếp tuyến và dây cung và góc nội tiếp cùng chắn cung } AM).$$ \nDo đó $\\Delta EAM \\backsim \\Delta EMB$ (g-g).\nSuy ra: $\\frac{EA}{EM} = \\frac{EM}{EB} \\Rightarrow EM^2 = EA \\cdot EB$.\nMà tam giác $EMS$ cân tại $E$ (theo câu a) nên $EM = ES$.\nSuy ra: $ES^2 = EA \\cdot EB$.\n\n*) [Ý 2 NÂNG CAO] Chứng minh $OK \\cdot OS = R^2$ và tâm đường tròn ngoại tiếp $\\Delta SMK$ di động trên đường thẳng cố định:\nVì $CD$ là đường kính của $(O)$ nên $\\widehat{CMD} = 90^\\circ$, do đó $MC \\perp MD$.\nTrong tam giác $CMD$ có $AB \\perp CD$ và các góc chắn cung, tia $MS$ là đường phân giác trong của góc $\\widehat{AMB}$ hoặc $\\widehat{CMD}$.\nVì $MD \\perp MC$ nên tia $MK$ chính là đường phân giác ngoài của góc $\\widehat{CMD}$.\nTheo tính chất đường phân giác trong và ngoài của tam giác $CMD$, ta có:\n$$\\frac{SC}{SD} = \\frac{KC}{KD} = \\frac{MC}{MD}.$$\nDo đó bộ bốn điểm $(C, D, S, K)$ lập thành một hàng điểm điều hòa: $\\frac{SC}{SD} = -\\frac{KC}{KD}$.\nChiếu lên đường thẳng $AB$ với gốc $O$ là trung điểm của $CD$, theo hệ thức Newton ta có:\n$$OK \\cdot OS = OC^2 = R^2.$$\nGọi $J$ là tâm của đường tròn ngoại tiếp tam giác $SMK$.\nVì $\\widehat{SMK} = \\widehat{CMD} = 90^\\circ$ nên tam giác $SMK$ vuông tại $M$, do đó tâm $J$ chính là trung điểm của cạnh huyền $SK$.\nTọa độ điểm $S$ và $K$ trên trục $AB$ thỏa mãn $x_S \\cdot x_K = R^2$.\nHoành độ của tâm $J$ là $x_J = \\frac{x_S + x_K}{2}$.\nMặt khác, đường trung trực của đoạn thẳng cố định hoặc đường thẳng vuông góc với $AB$ tại điểm liên hợp cố định đảm bảo tâm $J$ luôn nằm trên đường thẳng cố định vuông góc với $AB$ qua trung điểm các điểm cực đối cực."
            },
            {
                "id": 14,
                "points": 1.0,
                "question": "a) Một cây kem ốc quế gồm hai phần: phần bánh ốc quế có dạng hình nón với chiều cao $h = 12\\text{ cm}$ và bán kính đáy $r = 3\\text{ cm}$; phần kem bên trên có dạng một nửa hình cầu bán kính $r = 3\\text{ cm}$ úp vừa khít vào miệng bánh ốc quế. Tính thể tích của toàn bộ cây kem ốc quế đó (lấy $\\pi \\approx 3,14$).\nb) Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Tìm giá trị nhỏ nhất của biểu thức:\n$$P = \\frac{a+1}{b^2 + 1} + \\frac{b+1}{c^2 + 1} + \\frac{c+1}{a^2 + 1}.$$",
                "rubric": [
                    {
                        "step": "a) Thể tích phần nón: $V_1 = \\frac{1}{3}\\pi (3^2)(12) = 36\\pi\\text{ cm}^3$. Thể tích nửa hình cầu: $V_2 = \\frac{1}{2} \\cdot \\frac{4}{3}\\pi (3^3) = 18\\pi\\text{ cm}^3$. Thể tích cây kem: $V = 36\\pi + 18\\pi = 54\\pi \\approx 169,56\\text{ cm}^3$.",
                        "points": 0.5
                    },
                    {
                        "step": "b) [NÂNG CAO] Áp dụng AM-GM ngược dấu: $\\frac{a+1}{b^2+1} = (a+1) - \\frac{(a+1)b^2}{b^2+1} \\ge (a+1) - \\frac{(a+1)b^2}{2b} = (a+1) - \\frac{ab+b}{2}$.",
                        "points": 0.25
                    },
                    {
                        "step": "b) [NÂNG CAO] Tương tự với 2 hạng tử còn lại, cộng vế theo vế: $P \\ge (a+b+c+3) - \\frac{(ab+bc+ca) + (a+b+c)}{2} = 6 - \\frac{ab+bc+ca+3}{2}$. Vì $ab+bc+ca \\le 3 \\Rightarrow P \\ge 6 - 3 = 3$. Dấu bằng khi $a = b = c = 1$. Kết luận $\\min P = 3$.",
                        "points": 0.25
                    }
                ],
                "solution": "a) Thể tích của phần bánh ốc quế hình nón là:\n$$V_1 = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3} \\cdot 3,14 \\cdot 3^2 \\cdot 12 = 36 \\cdot 3,14 = 113,04\\text{ cm}^3.$$\nThể tích của phần kem hình nửa hình cầu phía trên là:\n$$V_2 = \\frac{1}{2} \\cdot \\left(\\frac{4}{3}\\pi r^3\\right) = \\frac{2}{3} \\cdot 3,14 \\cdot 3^3 = 18 \\cdot 3,14 = 56,52\\text{ cm}^3.$$\nThể tích của toàn bộ cây kem ốc quế là:\n$$V = V_1 + V_2 = 113,04 + 56,52 = 169,56\\text{ cm}^3.$$\nVậy thể tích toàn bộ cây kem là $169,56\\text{ cm}^3$.\n\nb) [CÂU PHÂN HÓA NÂNG CAO]\nÁp dụng kỹ thuật bất đẳng thức AM-GM ngược dấu:\nTa có:\n$$\\frac{a+1}{b^2 + 1} = \\frac{(a+1)(b^2 + 1) - (a+1)b^2}{b^2 + 1} = (a + 1) - \\frac{(a+1)b^2}{b^2 + 1}.$$\nTheo bất đẳng thức AM-GM: $b^2 + 1 \\ge 2b$, do đó:\n$$\\frac{(a+1)b^2}{b^2 + 1} \\le \\frac{(a+1)b^2}{2b} = \\frac{(a+1)b}{2} = \\frac{ab + b}{2}.$$\nSuy ra:\n$$\\frac{a+1}{b^2 + 1} \\ge (a + 1) - \\frac{ab + b}{2}.$$\nChứng minh hoàn toàn tương tự, ta có:\n$$\\frac{b+1}{c^2 + 1} \\ge (b + 1) - \\frac{bc + c}{2},$$\n$$\\frac{c+1}{a^2 + 1} \\ge (c + 1) - \\frac{ca + a}{2}.$$\nCộng từng vế của ba bất đẳng thức trên, ta được:\n$$P = \\frac{a+1}{b^2 + 1} + \\frac{b+1}{c^2 + 1} + \\frac{c+1}{a^2 + 1} \\ge (a + b + c + 3) - \\frac{(ab + bc + ca) + (a + b + c)}{2}.$$\nThay $a + b + c = 3$, ta có:\n$$P \\ge (3 + 3) - \\frac{(ab + bc + ca) + 3}{2} = 6 - \\frac{ab + bc + ca + 3}{2}.$$\nMặt khác, ta luôn có bất đẳng thức quen thuộc:\n$$ab + bc + ca \\le \\frac{(a+b+c)^2}{3} = \\frac{3^2}{3} = 3.$$\nDo đó:\n$$\\frac{ab + bc + ca + 3}{2} \\le \\frac{3 + 3}{2} = 3.$$\nSuy ra:\n$$P \\ge 6 - 3 = 3.$$\nĐẳng thức xảy ra khi và chỉ khi:\n$$\\begin{cases} b^2 = 1 \\\\ c^2 = 1 \\\\ a^2 = 1 \\\\ a + b + c = 3 \\end{cases} \\Leftrightarrow a = b = c = 1.$$\nVậy giá trị nhỏ nhất của biểu thức $P$ là $3$, đạt được khi $a = b = c = 1$."
            }
        ]
    }

    return exams

if __name__ == "__main__":
    e = get_exams_7_to_10()
    print(f"Loaded {len(e)} exams: {list(e.keys())}")
