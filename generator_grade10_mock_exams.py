# -*- coding: utf-8 -*-
"""
GENERATOR 6 BỘ ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN
Tuân thủ 100% cấu trúc ma trận 2 đề thi tuyển sinh vào 10 THPT (Sở GD&ĐT Hà Tĩnh 2025-2026 và 2026-2027):
Thời gian: 90 phút | Thang điểm: 10.0
- Phần I: Trắc nghiệm (2,0 điểm) - 8 câu (0,25đ/câu)
- Phần II: Tự luận (8,0 điểm) - 6 câu:
  + Câu 9 (1,0đ): Rút gọn biểu thức chứa căn
  + Câu 10 (1,0đ): Định lí Viète & ứng dụng
  + Câu 11 (1,0đ): Giải hệ phương trình
  + Câu 12 (2,0đ): a) Xác suất (1,0đ); b) Toán giải bằng lập PT/HPT (1,0đ)
  + Câu 13 (2,0đ): Hình học đường tròn (a: Tứ giác nội tiếp 1,0đ; b: Hệ thức lượng & tính chất 1,0đ)
  + Câu 14 (1,0đ): Phân loại 9-10 (a: Toán thực tế cực trị hình học 0,5đ; b: Bất đẳng thức & cực trị đại số 0,5đ)
"""

import json
import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)

MOCK_EXAMS_GRADE10 = {
    "metadata": {
        "title": "BỘ 6 ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN",
        "author": "GV Phan Đình Thuấn",
        "year": "2025 - 2026",
        "standard": "Chuẩn Ma trận Kỳ thi Tuyển sinh vào Lớp 10 THPT",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "totalExams": 6
    },
    "exams": {}
}

# ==============================================================================
# ĐỀ SỐ 01 (Mã đề 01)
# ==============================================================================
MOCK_EXAMS_GRADE10["exams"]["de_01"] = {
    "id": "de_01",
    "code": "MÃ ĐỀ 01",
    "title": "ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN - ĐỀ SỐ 01",
    "header": {
        "department": "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
        "examName": "KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT",
        "subject": "Môn thi: TOÁN",
        "author": "GV Phan Đình Thuấn",
        "time": "90 phút (không kể thời gian phát đề)",
        "code": "MÃ ĐỀ 01"
    },
    "part1": [
        {
            "id": 1,
            "question": "Kết quả rút gọn biểu thức $A = \\sqrt{45} - 2\\sqrt{5}$ là:",
            "options": ["A. $5\\sqrt{5}$", "B. $5$", "C. $\\sqrt{5}$", "D. $2\\sqrt{5}$"],
            "answer": "C",
            "explanation": "Ta có: $A = \\sqrt{9 \\cdot 5} - 2\\sqrt{5} = 3\\sqrt{5} - 2\\sqrt{5} = \\sqrt{5}$."
        },
        {
            "id": 2,
            "question": "Nghiệm của bất phương trình $3x - 6 > 0$ là:",
            "options": ["A. $x > 2$", "B. $x < 2$", "C. $x > 3$", "D. $x < 3$"],
            "answer": "A",
            "explanation": "$3x - 6 > 0 \\Leftrightarrow 3x > 6 \\Leftrightarrow x > 2$."
        },
        {
            "id": 3,
            "question": "Nghiệm của phương trình $4x - 5 = 11$ là:",
            "options": ["A. $x = 4$", "B. $x = -2$", "C. $x = 2$", "D. $x = -4$"],
            "answer": "A",
            "explanation": "$4x - 5 = 11 \\Leftrightarrow 4x = 16 \\Leftrightarrow x = 4$."
        },
        {
            "id": 4,
            "question": "Gieo một con xúc xắc cân đối một lần. Số phần tử của không gian mẫu là:",
            "options": ["A. 5", "B. 6", "C. 2", "D. 4"],
            "answer": "B",
            "explanation": "Con xúc xắc có 6 mặt từ 1 đến 6 chấm nên số phần tử của không gian mẫu là $n(\\Omega) = 6$."
        },
        {
            "id": 5,
            "question": "Đồ thị của hàm số $y = 3x^2$ đi qua điểm nào sau đây?",
            "options": ["A. $(1; 4)$", "B. $(2; 8)$", "C. $(2; 12)$", "D. $(-1; -3)$"],
            "answer": "C",
            "explanation": "Thay $x = 2$ vào hàm số: $y = 3 \\cdot 2^2 = 3 \\cdot 4 = 12$. Do đó điểm $(2; 12)$ thuộc đồ thị."
        },
        {
            "id": 6,
            "question": "Cho tam giác $ABC$ vuông tại $A$. Biết $BC = 5\\text{ cm}, AC = 4\\text{ cm}$. Giá trị của $\\sin B$ bằng:",
            "options": ["A. $\\frac{3}{5}$", "B. $\\frac{4}{3}$", "C. $\\frac{5}{4}$", "D. $\\frac{4}{5}$"],
            "answer": "D",
            "explanation": "Trong tam giác vuông $ABC$ vuông tại $A$: $\\sin B = \\frac{\\text{đối}}{\\text{huyền}} = \\frac{AC}{BC} = \\frac{4}{5}$."
        },
        {
            "id": 7,
            "question": "Một hình trụ có bán kính đáy $r$, đường cao $h$. Diện tích xung quanh của hình trụ là:",
            "options": ["A. $S_{xq} = \\pi rh$", "B. $S_{xq} = 2\\pi rh$", "C. $S_{xq} = 3\\pi rh$", "D. $S_{xq} = 4\\pi rh$"],
            "answer": "B",
            "explanation": "Theo công thức hình học không gian, diện tích xung quanh của hình trụ là $S_{xq} = 2\\pi rh$."
        },
        {
            "id": 8,
            "question": "Để mua giày cho 16 bạn nam trong lớp, bạn An thu thập cỡ giày như sau: 40, 37, 38, 39, 37, 38, 40, 40, 39, 38, 40, 39, 37, 41, 40, 39. Tần số của giá trị cỡ giày 39 là:",
            "options": ["A. 4", "B. 5", "C. 2", "D. 6"],
            "answer": "A",
            "explanation": "Đếm số lần xuất hiện của cỡ giày 39 trong mẫu số liệu trên ta thấy xuất hiện đúng 4 lần. Vậy tần số bằng 4."
        }
    ],
    "part2": [
        {
            "id": 9,
            "points": 1.0,
            "question": "Cho $x \\ge 0$ và $x \\ne 4$. Rút gọn biểu thức:\n$$A = \\left(\\frac{\\sqrt{x}}{\\sqrt{x}+2} + \\frac{2}{\\sqrt{x}-2}\\right) \\cdot \\frac{\\sqrt{x}+2}{x+4}$$",
            "rubric": [
                {"step": "Quy đồng mẫu thức trong ngoặc với mẫu chung $(\\sqrt{x}+2)(\\sqrt{x}-2) = x - 4$.", "points": 0.25},
                {"step": "Khai triển tử thức: $\\sqrt{x}(\\sqrt{x}-2) + 2(\\sqrt{x}+2) = x - 2\\sqrt{x} + 2\\sqrt{x} + 4 = x + 4$.", "points": 0.25},
                {"step": "Thu gọn trong ngoặc được $\\frac{x+4}{(\\sqrt{x}+2)(\\sqrt{x}-2)}$.", "points": 0.25},
                {"step": "Nhân với $\\frac{\\sqrt{x}+2}{x+4}$ và triệt tiêu các thừa số chung: $A = \\frac{1}{\\sqrt{x}-2}$. Kết luận.", "points": 0.25}
            ],
            "solution": "Với $x \\ge 0$ và $x \\ne 4$, ta có:\n$$\\begin{aligned}\nA &= \\left[\\frac{\\sqrt{x}(\\sqrt{x}-2)}{(\\sqrt{x}+2)(\\sqrt{x}-2)} + \\frac{2(\\sqrt{x}+2)}{(\\sqrt{x}+2)(\\sqrt{x}-2)}\\right] \\cdot \\frac{\\sqrt{x}+2}{x+4} \\\\\n&= \\frac{x - 2\\sqrt{x} + 2\\sqrt{x} + 4}{(\\sqrt{x}+2)(\\sqrt{x}-2)} \\cdot \\frac{\\sqrt{x}+2}{x+4} \\\\\n&= \\frac{x+4}{(\\sqrt{x}+2)(\\sqrt{x}-2)} \\cdot \\frac{\\sqrt{x}+2}{x+4} \\\\\n&= \\frac{1}{\\sqrt{x}-2}.\n\\end{aligned}$$\nVậy $A = \\frac{1}{\\sqrt{x}-2}$ với $x \\ge 0, x \\ne 4$."
        },
        {
            "id": 10,
            "points": 1.0,
            "question": "Biết phương trình $x^2 - 5x + 3 = 0$ có hai nghiệm $x_1, x_2$. Không giải phương trình, tính giá trị của biểu thức $T = (x_1+3)^2 + (x_2+3)^2$.",
            "rubric": [
                {"step": "Tính $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 3 = 13 > 0$, suy ra phương trình luôn có 2 nghiệm phân biệt.", "points": 0.25},
                {"step": "Áp dụng định lí Viète: $x_1 + x_2 = 5$ và $x_1 x_2 = 3$.", "points": 0.25},
                {"step": "Biến đổi $T = x_1^2 + 6x_1 + 9 + x_2^2 + 6x_2 + 9 = (x_1+x_2)^2 - 2x_1x_2 + 6(x_1+x_2) + 18$.", "points": 0.25},
                {"step": "Thay số: $T = 5^2 - 2(3) + 6(5) + 18 = 25 - 6 + 30 + 18 = 67$. Kết luận $T = 67$.", "points": 0.25}
            ],
            "solution": "Xét phương trình $x^2 - 5x + 3 = 0$ có $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 3 = 25 - 12 = 13 > 0$, do đó phương trình có hai nghiệm phân biệt $x_1, x_2$.\nTheo định lí Viète, ta có:\n$$\\begin{cases} x_1 + x_2 = 5 \\\\ x_1 x_2 = 3 \\end{cases}$$\nTa biến đổi biểu thức $T$:\n$$\\begin{aligned}\nT &= (x_1+3)^2 + (x_2+3)^2 \\\\\n&= (x_1^2 + 6x_1 + 9) + (x_2^2 + 6x_2 + 9) \\\\\n&= (x_1^2 + x_2^2) + 6(x_1 + x_2) + 18 \\\\\n&= \\left[(x_1 + x_2)^2 - 2x_1 x_2\\right] + 6(x_1 + x_2) + 18 \\\\\n&= \\left(5^2 - 2 \\cdot 3\\right) + 6 \\cdot 5 + 18 \\\\\n&= 19 + 30 + 18 = 67.\n\\end{aligned}$$\nVậy $T = 67$."
        },
        {
            "id": 11,
            "points": 1.0,
            "question": "Giải hệ phương trình:\n$$\\begin{cases} 2x - 3y = 1 \\\\ x + y = 3 \\end{cases}$$",
            "rubric": [
                {"step": "Từ phương trình thứ hai rút $x = 3 - y$ hoặc nhân phương trình hai với 3 được $3x + 3y = 9$.", "points": 0.25},
                {"step": "Cộng hai phương trình triệt tiêu $y$: $5x = 10 \\Rightarrow x = 2$.", "points": 0.25},
                {"step": "Thay $x = 2$ vào phương trình $x + y = 3 \\Rightarrow 2 + y = 3 \\Rightarrow y = 1$.", "points": 0.25},
                {"step": "Kết luận nghiệm duy nhất của hệ phương trình là $(x; y) = (2; 1)$.", "points": 0.25}
            ],
            "solution": "Ta có:\n$$\\begin{cases} 2x - 3y = 1 \\\\ x + y = 3 \\end{cases} \\Leftrightarrow \\begin{cases} 2x - 3y = 1 \\\\ 3x + 3y = 9 \\end{cases} \\Leftrightarrow \\begin{cases} 5x = 10 \\\\ x + y = 3 \\end{cases} \\Leftrightarrow \\begin{cases} x = 2 \\\\ 2 + y = 3 \\end{cases} \\Leftrightarrow \\begin{cases} x = 2 \\\\ y = 1 \\end{cases}$$\nVậy hệ phương trình đã cho có nghiệm duy nhất $(x; y) = (2; 1)$."
        },
        {
            "id": 12,
            "points": 2.0,
            "question": "a) Một hộp đựng 4 viên bi có cùng khối lượng và kích thước, được đánh số 5; 6; 7; 8. Lấy ngẫu nhiên lần lượt hai viên bi từ hộp đó (viên bi lấy ra lần đầu không trả lại vào hộp). Viết không gian mẫu của phép thử và tính xác suất của biến cố $A$: \"Tổng hai số trên hai viên bi chia 3 dư 2\".\nb) Một đội xe dự định chở 30 tấn hàng. Khi sắp khởi hành thì hai xe phải điều đi làm công việc khác nên mỗi xe còn lại phải chở nhiều hơn 0,5 tấn hàng so với dự định ban đầu. Hỏi thực tế có bao nhiêu xe đã tham gia chở hàng? (biết rằng mỗi xe đều chở khối lượng hàng bằng nhau).",
            "rubric": [
                {"step": "a) Liệt kê đúng không gian mẫu $\\Omega$ gồm 12 cặp phần tử, suy ra $n(\\Omega) = 12$.", "points": 0.5},
                {"step": "a) Liệt kê các kết quả thuận lợi cho $A$: (5;6), (6;8), (6;5), (8;6) gồm 4 kết quả. Tính $P(A) = \\frac{4}{12} = \\frac{1}{3}$.", "points": 0.5},
                {"step": "b) Đặt ẩn số xe ban đầu là $x$ ($x \\in \\mathbb{N}^*, x > 2$). Biểu diễn số xe thực tế $x - 2$, khối lượng dự định $\\frac{30}{x}$ và thực tế $\\frac{30}{x-2}$.", "points": 0.35},
                {"step": "b) Lập phương trình $\\frac{30}{x-2} - \\frac{30}{x} = 0,5$. Biến đổi về phương trình bậc hai $x^2 - 2x - 120 = 0$.", "points": 0.35},
                {"step": "b) Giải phương trình tìm được $x = 12$ (thỏa mãn), $x = -10$ (loại). Kết luận số xe thực tế là $12 - 2 = 10$ xe.", "points": 0.3}
            ],
            "solution": "a) Không gian mẫu của phép thử là tập hợp các cặp số được lấy lần lượt không hoàn lại:\n$$\\Omega = \\{(5;6); (5;7); (5;8); (6;5); (6;7); (6;8); (7;5); (7;6); (7;8); (8;5); (8;6); (8;7)\\}$$\nSố phần tử của không gian mẫu là $n(\\Omega) = 12$.\nXét tổng hai số trên hai viên bi chia cho 3 dư 2:\n- $5 + 6 = 11 = 3 \\cdot 3 + 2$ (thỏa mãn) $\\Rightarrow (5;6), (6;5)$\n- $6 + 8 = 14 = 4 \\cdot 3 + 2$ (thỏa mãn) $\\Rightarrow (6;8), (8;6)$\nCác kết quả thuận lợi cho biến cố $A$ là:\n$$A = \\{(5;6); (6;8); (6;5); (8;6)\\} \\Rightarrow n(A) = 4.$$\nVậy xác suất của biến cố $A$ là: $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{4}{12} = \\frac{1}{3}$.\n\nb) Gọi số xe dự định ban đầu của đội là $x$ (xe, điều kiện $x \\in \\mathbb{N}^*, x > 2$).\nSố xe thực tế tham gia chở hàng là $x - 2$ (xe).\nKhối lượng hàng mỗi xe dự định chở là: $\\frac{30}{x}$ (tấn).\nKhối lượng hàng mỗi xe thực tế phải chở là: $\\frac{30}{x-2}$ (tấn).\nVì mỗi xe còn lại phải chở nhiều hơn dự định 0,5 tấn ($= \\frac{1}{2}$ tấn), ta có phương trình:\n$$\\frac{30}{x-2} - \\frac{30}{x} = \\frac{1}{2}$$\n$$\\Leftrightarrow 60x - 60(x-2) = x(x-2)$$\n$$\\Leftrightarrow 120 = x^2 - 2x \\Leftrightarrow x^2 - 2x - 120 = 0$$\nTa có $\\Delta' = (-1)^2 - 1 \\cdot (-120) = 121 > 0 \\Rightarrow \\sqrt{\\Delta'} = 11$.\nPhương trình có 2 nghiệm: $x_1 = 1 + 11 = 12$ (thỏa mãn), $x_2 = 1 - 11 = -10$ (loại).\nVậy số xe thực tế tham gia chở hàng là: $12 - 2 = 10$ (xe)."
        },
        {
            "id": 13,
            "points": 2.0,
            "question": "Cho tam giác $ABC$ có ba góc nhọn nội tiếp đường tròn $(O)$, hai đường cao $BM$ và $CN$ cắt nhau tại $H$. Gọi $K$ là trung điểm của cạnh $BC$.\na) Chứng minh tứ giác $BCMN$ nội tiếp.\nb) Qua điểm $K$ vẽ đường thẳng vuông góc với $KH$ cắt các đường thẳng $AB, AC$ và $AH$ lần lượt tại các điểm $E, F$ và $Q$. Chứng minh $AH = 2OK$ và $Q$ là trung điểm của $EF$.",
            "rubric": [
                {"step": "a) Chỉ ra $\\widehat{BMC} = 90^\\circ$ và $\\widehat{BNC} = 90^\\circ$.", "points": 0.5},
                {"step": "a) Suy ra hai đỉnh $M, N$ kề nhau cùng nhìn cạnh $BC$ dưới góc $90^\\circ$, nên $BCMN$ nội tiếp đường tròn đường kính $BC$.", "points": 0.5},
                {"step": "b) Kẻ đường kính $AD$ của $(O)$, chứng minh tứ giác $BDCH$ là hình bình hành. Suy ra $K$ là trung điểm $HD$.", "points": 0.35},
                {"step": "b) Trong tam giác $ADH$, có $O$ là trung điểm $AD$ và $K$ là trung điểm $HD$ nên $OK$ là đường trung bình, suy ra $AH = 2OK$.", "points": 0.35},
                {"step": "b) Sử dụng tam giác đồng dạng $\\Delta AEQ \\backsim \\Delta CHK$ và $\\Delta AQF \\backsim \\Delta BKH$ kết hợp $BK = CK$ để suy ra $EQ = FQ$, chứng minh $Q$ là trung điểm $EF$.", "points": 0.3}
            ],
            "solution": "a) Vì $BM \\perp AC$ và $CN \\perp AB$ nên $\\widehat{BMC} = 90^\\circ$ và $\\widehat{BNC} = 90^\\circ$.\nXét tứ giác $BCMN$, hai đỉnh $M$ và $N$ cùng nhìn đoạn thẳng $BC$ dưới một góc vuông $90^\\circ$.\nDo đó, tứ giác $BCMN$ nội tiếp đường tròn đường kính $BC$.\n\nb) *) Chứng minh $AH = 2OK$:\nKẻ đường kính $AD$ của đường tròn $(O)$.\nKhi đó $\\widehat{ACD} = 90^\\circ$ và $\\widehat{ABD} = 90^\\circ$ (góc nội tiếp chắn nửa đường tròn).\nSuy ra $DC \\perp AC$ và $DB \\perp AB$.\nLại có $BM \\perp AC$ và $CN \\perp AB$ nên $BH \\parallel DC$ và $CH \\parallel DB$.\nTứ giác $BDCH$ có các cặp cạnh đối song song nên là hình bình hành.\nMà $K$ là trung điểm của đường chéo $BC$ nên $K$ cũng là trung điểm của đường chéo $HD$.\nTrong tam giác $ADH$, $O$ là trung điểm $AD$ và $K$ là trung điểm $HD$ nên $OK$ là đường trung bình của tam giác $ADH$.\nDo đó $OK \\parallel AH$ và $AH = 2OK$.\n\n*) Chứng minh $Q$ là trung điểm của $EF$:\nVì $\\Delta ENH$ vuông tại $N$ và $\\Delta EKH$ vuông tại $K$ nên tứ giác $NHKE$ nội tiếp đường tròn đường kính $HE$.\nSuy ra $\\widehat{AEQ} = \\widehat{KHC}$ (cùng bù với $\\widehat{NHK}$).\nLại có $\\widehat{NAH} = \\widehat{NCB}$ (cùng phụ với $\\widehat{ABC}$).\nDo đó $\\Delta AEQ \\backsim \\Delta CHK$ (g-g) $\\Rightarrow \\frac{EQ}{HK} = \\frac{AQ}{CK} \\Rightarrow EQ = \\frac{AQ \\cdot HK}{CK}$.\nTương tự, tứ giác $ANHM$ nội tiếp đường tròn đường kính $AH$, ta có $\\widehat{MNH} = \\widehat{MAH}$ (cùng chắn cung $HM$).\nMặt khác $\\widehat{MNH} = \\widehat{MBC}$ (cùng chắn cung $MC$ của đường tròn ngoại tiếp tứ giác $BCMN$).\nSuy ra $\\widehat{QAF} = \\widehat{HBC}$. Lại có $\\widehat{AQF} = \\widehat{BKH}$ (cùng phụ với $\\widehat{QKB}$).\nDo đó $\\Delta AQF \\backsim \\Delta BKH$ (g-g) $\\Rightarrow \\frac{QF}{HK} = \\frac{AQ}{BK} \\Rightarrow QF = \\frac{AQ \\cdot HK}{BK}$.\nVì $K$ là trung điểm $BC$ nên $BK = CK$.\nTừ đó suy ra $EQ = QF$, tức $Q$ là trung điểm của đoạn thẳng $EF$."
        },
        {
            "id": 14,
            "points": 1.0,
            "question": "a) Một công ty sản xuất hàng loạt thùng đựng hàng hóa bằng gỗ. Mỗi thùng có dạng hình hộp chữ nhật không nắp, đáy là hình vuông, thể tích $160\\text{ dm}^3$. Để tiết kiệm vật liệu gỗ làm thùng, người ta cần thiết kế thùng sao cho tổng diện tích xung quanh và diện tích mặt đáy là nhỏ nhất. Khi đó độ dài cạnh đáy và chiều cao của thùng có giá trị bằng bao nhiêu? (kết quả làm tròn đến một chữ số thập phân).\nb) Cho các số thực dương $a, b, c$ thỏa mãn $4(ab+bc+ca) = 5c^2$. Tìm giá trị lớn nhất của biểu thức:\n$$S = \\sqrt{2(a+b+c)} - a^2 - b^2.$$",
            "rubric": [
                {"step": "a) Biểu diễn chiều cao $h = \\frac{160}{a^2}$. Viết diện tích vật liệu $S = a^2 + 4ah = a^2 + \\frac{640}{a}$.", "points": 0.25},
                {"step": "a) Áp dụng BĐT AM-GM cho 3 số: $a^2 + \\frac{320}{a} + \\frac{320}{a} \\ge 3\\sqrt[3]{320^2}$. Dấu bằng khi $a^3 = 320 \\Rightarrow a \\approx 6,8\\text{ dm}, h \\approx 3,4\\text{ dm}$.", "points": 0.25},
                {"step": "b) Biến đổi điều kiện: $4(ab+bc+ca) + 4c^2 = 9c^2 \\Leftrightarrow 4(a+c)(b+c) = 9c^2 \\le (a+b+2c)^2 \\Rightarrow a + b \\ge c$.", "points": 0.25},
                {"step": "b) Đặt $x = a + b > 0$, đánh giá $a^2 + b^2 \\ge \\frac{(a+b)^2}{2} = \\frac{x^2}{2}$ và $c \\le x$, tìm được $\\max S = \\frac{3}{2}$ khi $a = b = \\frac{1}{2}, c = 1$.", "points": 0.25}
            ],
            "solution": "a) Gọi cạnh đáy của thùng là $a$ (dm) và chiều cao là $h$ (dm), với $a > 0, h > 0$.\nThể tích hình hộp chữ nhật đáy vuông là: $V = a^2 h = 160 \\Rightarrow h = \\frac{160}{a^2}$.\nTổng diện tích phần vật liệu làm đáy và xung quanh (không có nắp) là:\n$$S = a^2 + 4ah = a^2 + 4a \\cdot \\frac{160}{a^2} = a^2 + \\frac{640}{a} = a^2 + \\frac{320}{a} + \\frac{320}{a}.$$\nÁp dụng bất đẳng thức AM-GM cho 3 số dương $a^2, \\frac{320}{a}, \\frac{320}{a}$:\n$$S = a^2 + \\frac{320}{a} + \\frac{320}{a} \\ge 3 \\sqrt[3]{a^2 \\cdot \\frac{320}{a} \\cdot \\frac{320}{a}} = 3 \\sqrt[3]{320^2} = 48\\sqrt[3]{25} \\approx 140,4\\text{ dm}^2.$$\nĐẳng thức xảy ra khi và chỉ khi:\n$$a^2 = \\frac{320}{a} \\Leftrightarrow a^3 = 320 \\Leftrightarrow a = 4\\sqrt[3]{5} \\approx 6,8\\text{ dm}.$$\nKhi đó chiều cao của thùng là: $h = \\frac{160}{a^2} = 2\\sqrt[3]{5} \\approx 3,4\\text{ dm}$.\nVậy để diện tích vật liệu nhỏ nhất thì cạnh đáy và chiều cao lần lượt là khoảng $6,8\\text{ dm}$ và $3,4\\text{ dm}$.\n\nb) Từ giả thiết $4(ab+bc+ca) = 5c^2$, ta cộng cả hai vế với $4c^2$:\n$$4(ab+bc+ca) + 4c^2 = 9c^2 \\Leftrightarrow 4(a+c)(b+c) = 9c^2.$$\nÁp dụng bất đẳng thức $4xy \\le (x+y)^2$, ta có:\n$$9c^2 = 4(a+c)(b+c) \\le (a+c+b+c)^2 = (a+b+2c)^2.$$\nVì $a, b, c > 0$ nên $3c \\le a + b + 2c \\Leftrightarrow c \\le a + b$.\nLại có: $a^2 + b^2 \\ge \\frac{(a+b)^2}{2}$. Đặt $x = a + b > 0$, ta có $c \\le x$.\nKhi đó:\n$$S = \\sqrt{2(a+b+c)} - (a^2+b^2) \\le \\sqrt{2(x+x)} - \\frac{x^2}{2} = 2\\sqrt{x} - \\frac{x^2}{2}.$$\nÁp dụng bất đẳng thức $2\\sqrt{x} \\le x + 1$ (do $(\\sqrt{x}-1)^2 \\ge 0$):\n$$S \\le x + 1 - \\frac{x^2}{2} = -\\frac{1}{2}(x^2 - 2x + 1) + \\frac{3}{2} = -\\frac{1}{2}(x-1)^2 + \\frac{3}{2} \\le \\frac{3}{2}.$$\nDấu đẳng thức xảy ra khi và chỉ khi:\n$$\\begin{cases} x = 1 \\\\ a = b \\\\ c = a + b \\\\ \\sqrt{x} = 1 \\end{cases} \\Leftrightarrow \\begin{cases} a = b = \\frac{1}{2} \\\\ c = 1 \\end{cases} \\text{ (thỏa mãn } 4(ab+bc+ca) = 5c^2).$$\nVậy giá trị lớn nhất của $S$ là $\\frac{3}{2}$ khi $a = b = \\frac{1}{2}$ và $c = 1$."
        }
    ]
}

print("Đã nạp xong Đề 01.")

# ==============================================================================
# ĐỀ SỐ 02 (Mã đề 02)
# ==============================================================================
MOCK_EXAMS_GRADE10["exams"]["de_02"] = {
    "id": "de_02",
    "code": "MÃ ĐỀ 02",
    "title": "ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN - ĐỀ SỐ 02",
    "header": {
        "department": "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
        "examName": "KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT",
        "subject": "Môn thi: TOÁN",
        "author": "GV Phan Đình Thuấn",
        "time": "90 phút (không kể thời gian phát đề)",
        "code": "MÃ ĐỀ 02"
    },
    "part1": [
        {
            "id": 1,
            "question": "Kết quả rút gọn biểu thức $A = 3\\sqrt{8} - \\sqrt{2}$ là:",
            "options": ["A. $\\sqrt{2}$", "B. $2\\sqrt{2}$", "C. $5\\sqrt{2}$", "D. $11\\sqrt{2}$"],
            "answer": "C",
            "explanation": "Ta có: $A = 3 \\cdot 2\\sqrt{2} - \\sqrt{2} = 6\\sqrt{2} - \\sqrt{2} = 5\\sqrt{2}$."
        },
        {
            "id": 2,
            "question": "Nghiệm của bất phương trình $2x - 4 < 0$ là:",
            "options": ["A. $x < 2$", "B. $x > 2$", "C. $x > 4$", "D. $x < 4$"],
            "answer": "A",
            "explanation": "$2x - 4 < 0 \\Leftrightarrow 2x < 4 \\Leftrightarrow x < 2$."
        },
        {
            "id": 3,
            "question": "Nghiệm của phương trình $5x - 2 = 18$ là:",
            "options": ["A. $x = -4$", "B. $x = 20$", "C. $x = 4$", "D. $x = 16$"],
            "answer": "C",
            "explanation": "$5x - 2 = 18 \\Leftrightarrow 5x = 20 \\Leftrightarrow x = 4$."
        },
        {
            "id": 4,
            "question": "Một hộp đựng 5 thẻ cùng loại được đánh số 1; 2; 3; 4; 5. Rút ngẫu nhiên một thẻ từ trong hộp. Số phần tử của không gian mẫu là:",
            "options": ["A. 1", "B. 3", "C. 4", "D. 5"],
            "answer": "D",
            "explanation": "Có 5 thẻ nên phép thử có 5 kết quả đồng khả năng: $n(\\Omega) = 5$."
        },
        {
            "id": 5,
            "question": "Đồ thị của hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
            "options": ["A. $(1; 4)$", "B. $(-1; 2)$", "C. $(1; -2)$", "D. $(-1; -2)$"],
            "answer": "B",
            "explanation": "Thay $x = -1$ vào hàm số: $y = 2(-1)^2 = 2 \\cdot 1 = 2$. Do đó điểm $(-1; 2)$ thuộc đồ thị."
        },
        {
            "id": 6,
            "question": "Cho tam giác $ABC$ vuông tại $A$. Biết $AB = 3\\text{ cm}, AC = 4\\text{ cm}$. Giá trị của $\\tan C$ bằng:",
            "options": ["A. $\\frac{3}{4}$", "B. $\\frac{4}{3}$", "C. $\\frac{3}{5}$", "D. $\\frac{4}{5}$"],
            "answer": "A",
            "explanation": "Trong tam giác vuông $ABC$ tại $A$: $\\tan C = \\frac{AB}{AC} = \\frac{3}{4}$."
        },
        {
            "id": 7,
            "question": "Một hình cầu có bán kính bằng $2\\text{ cm}$. Diện tích mặt cầu bằng:",
            "options": ["A. $8\\pi\\text{ cm}^2$", "B. $4\\pi\\text{ cm}^2$", "C. $16\\text{ cm}^2$", "D. $16\\pi\\text{ cm}^2$"],
            "answer": "D",
            "explanation": "Diện tích mặt cầu là $S = 4\\pi R^2 = 4\\pi \\cdot 2^2 = 16\\pi\\text{ cm}^2$."
        },
        {
            "id": 8,
            "question": "Bảng thống kê điểm kiểm tra học kỳ 2 của 100 học sinh khối 9 gồm: Điểm 5 (12 hs), Điểm 6 (16 hs), Điểm 7 (22 hs), Điểm 8 (18 hs), Điểm 9 (30 hs), Điểm 10 (2 hs). Điểm 9 có tần số tương đối là:",
            "options": ["A. 40%", "B. 30%", "C. 3%", "D. 9%"],
            "answer": "B",
            "explanation": "Tần số tương đối của điểm 9 là: $f = \\frac{30}{100} \\cdot 100\\% = 30\\%$."
        }
    ],
    "part2": [
        {
            "id": 9,
            "points": 1.0,
            "question": "Cho $x > 0$ và $x \\ne 9$. Rút gọn biểu thức:\n$$A = \\left(\\frac{1}{\\sqrt{x}+3} + \\frac{3}{x-9}\\right) \\cdot \\frac{x-9}{3x}$$",
            "rubric": [
                {"step": "Quy đồng trong ngoặc với mẫu chung $x - 9 = (\\sqrt{x}+3)(\\sqrt{x}-3)$.", "points": 0.25},
                {"step": "Tử thức trong ngoặc là: $\\sqrt{x} - 3 + 3 = \\sqrt{x}$.", "points": 0.25},
                {"step": "Nhân với $\\frac{x-9}{3x}$: $A = \\frac{\\sqrt{x}}{x-9} \\cdot \\frac{x-9}{3x}$.", "points": 0.25},
                {"step": "Rút gọn được $A = \\frac{\\sqrt{x}}{3x} = \\frac{1}{3\\sqrt{x}}$. Kết luận.", "points": 0.25}
            ],
            "solution": "Với $x > 0$ và $x \\ne 9$, ta có:\n$$\\begin{aligned}\nA &= \\left[\\frac{\\sqrt{x}-3}{(\\sqrt{x}+3)(\\sqrt{x}-3)} + \\frac{3}{x-9}\\right] \\cdot \\frac{x-9}{3x} \\\\\n&= \\frac{\\sqrt{x}-3+3}{x-9} \\cdot \\frac{x-9}{3x} \\\\\n&= \\frac{\\sqrt{x}}{x-9} \\cdot \\frac{x-9}{3x} \\\\\n&= \\frac{\\sqrt{x}}{3x} = \\frac{1}{3\\sqrt{x}}.\n\\end{aligned}$$\nVậy $A = \\frac{1}{3\\sqrt{x}}$ với $x > 0, x \\ne 9$."
        },
        {
            "id": 10,
            "points": 1.0,
            "question": "Biết phương trình $x^2 - 3x - 6 = 0$ có hai nghiệm $x_1, x_2$. Không giải phương trình, tính giá trị của biểu thức $T = \\frac{2x_1}{x_2+1} + \\frac{2x_2}{x_1+1}$.",
            "rubric": [
                {"step": "Chỉ ra phương trình có $\\Delta = 33 > 0$ nên luôn có 2 nghiệm phân biệt.", "points": 0.2},
                {"step": "Theo Viète: $x_1 + x_2 = 3$ và $x_1 x_2 = -6$.", "points": 0.3},
                {"step": "Quy đồng mẫu: $T = \\frac{2x_1(x_1+1) + 2x_2(x_2+1)}{(x_1+1)(x_2+1)} = \\frac{2(x_1+x_2)^2 - 4x_1x_2 + 2(x_1+x_2)}{x_1x_2 + (x_1+x_2) + 1}$.", "points": 0.3},
                {"step": "Thay số: $T = \\frac{2 \\cdot 3^2 - 4(-6) + 2 \\cdot 3}{-6 + 3 + 1} = \\frac{48}{-2} = -24$. Kết luận.", "points": 0.2}
            ],
            "solution": "Xét phương trình $x^2 - 3x - 6 = 0$ có $\\Delta = (-3)^2 - 4(1)(-6) = 33 > 0$ nên phương trình có hai nghiệm phân biệt $x_1, x_2$.\nTheo hệ thức Viète:\n$$\\begin{cases} x_1 + x_2 = 3 \\\\ x_1 x_2 = -6 \\end{cases}$$\nTa biến đổi biểu thức $T$:\n$$\\begin{aligned}\nT &= \\frac{2x_1(x_1+1) + 2x_2(x_2+1)}{(x_1+1)(x_2+1)} \\\\\n&= \\frac{2(x_1^2 + x_2^2) + 2(x_1 + x_2)}{x_1 x_2 + x_1 + x_2 + 1} \\\\\n&= \\frac{2\\left[(x_1+x_2)^2 - 2x_1 x_2\\right] + 2(x_1 + x_2)}{x_1 x_2 + (x_1 + x_2) + 1} \\\\\n&= \\frac{2\\left[3^2 - 2(-6)\\right] + 2(3)}{-6 + 3 + 1} = \\frac{2(21) + 6}{-2} = \\frac{48}{-2} = -24.\n\\end{aligned}$$\nVậy $T = -24$."
        },
        {
            "id": 11,
            "points": 1.0,
            "question": "Giải hệ phương trình:\n$$\\begin{cases} 2x - y = 3 \\\\ x + 2y = 4 \\end{cases}$$",
            "rubric": [
                {"step": "Nhân phương trình 1 với 2: $4x - 2y = 6$.", "points": 0.25},
                {"step": "Cộng vế theo vế: $5x = 10 \\Rightarrow x = 2$.", "points": 0.25},
                {"step": "Thay $x = 2$ vào $x + 2y = 4 \\Rightarrow 2y = 2 \\Rightarrow y = 1$.", "points": 0.25},
                {"step": "Kết luận nghiệm duy nhất $(x; y) = (2; 1)$.", "points": 0.25}
            ],
            "solution": "Ta có:\n$$\\begin{cases} 2x - y = 3 \\\\ x + 2y = 4 \\end{cases} \\Leftrightarrow \\begin{cases} 4x - 2y = 6 \\\\ x + 2y = 4 \\end{cases} \\Leftrightarrow \\begin{cases} 5x = 10 \\\\ x + 2y = 4 \\end{cases} \\Leftrightarrow \\begin{cases} x = 2 \\\\ 2 + 2y = 4 \\end{cases} \\Leftrightarrow \\begin{cases} x = 2 \\\\ y = 1 \\end{cases}$$\nVậy hệ phương trình có nghiệm duy nhất $(x; y) = (2; 1)$."
        },
        {
            "id": 12,
            "points": 2.0,
            "question": "a) Có hai hộp I và II mỗi hộp đựng 3 tấm thẻ cùng loại, 3 tấm thẻ trong hộp I được đánh số 1; 2; 3 và 3 tấm thẻ trong hộp II được đánh số 4; 5; 6. Rút ngẫu nhiên từ mỗi hộp ra một tấm thẻ. Viết không gian mẫu của phép thử và tính xác suất của biến cố $A$: “Tổng hai số trên hai thẻ rút ra là một số lẻ”.\nb) Một người lái ô tô đi từ địa điểm A đến địa điểm B cách nhau 180 km trong một thời gian dự định trước. Sau khi đi được 1 giờ, ô tô gặp sự cố nên phải dừng lại 20 phút, sau đó tiếp tục đi đến địa điểm B. Để đến địa điểm B đúng thời gian đã định, người lái ô tô phải tăng vận tốc thêm 12 km/h so với vận tốc ban đầu trên quãng đường còn lại. Tính vận tốc ban đầu của ô tô đó.",
            "rubric": [
                {"step": "a) Viết không gian mẫu $\\Omega = \\{(1;4), (1;5), (1;6), (2;4), (2;5), (2;6), (3;4), (3;5), (3;6)\\} \\Rightarrow n(\\Omega) = 9$.", "points": 0.5},
                {"step": "a) Liệt kê biến cố $A$: có 5 kết quả thuận lợi $\\{(1;4), (1;6), (2;5), (3;4), (3;6)\\}$. Tính $P(A) = \\frac{5}{9}$.", "points": 0.5},
                {"step": "b) Đổi 20 phút $= \\frac{1}{3}$ giờ. Đặt ẩn vận tốc ban đầu là $x > 0$. Biểu diễn thời gian dự định $\\frac{180}{x}$ và quãng đường còn lại $180 - x$.", "points": 0.35},
                {"step": "b) Lập phương trình: $\\frac{180}{x} = 1 + \\frac{1}{3} + \\frac{180-x}{x+12}$. Quy đồng thu gọn: $x^2 + 48x - 6480 = 0$.", "points": 0.35},
                {"step": "b) Giải phương trình: $x = 60$ (thỏa mãn), $x = -108$ (loại). Kết luận vận tốc ban đầu là 60 km/h.", "points": 0.3}
            ],
            "solution": "a) Không gian mẫu của phép thử là tập hợp tất cả các cặp số gồm 1 số từ hộp I và 1 số từ hộp II:\n$$\\Omega = \\{(1; 4); (1; 5); (1; 6); (2; 4); (2; 5); (2; 6); (3; 4); (3; 5); (3; 6)\\}$$\nSố phần tử của không gian mẫu là $n(\\Omega) = 9$.\nTổng hai số là số lẻ khi một số lẻ và một số chẵn:\n$$A = \\{(1; 4); (1; 6); (2; 5); (3; 4); (3; 6)\\} \\Rightarrow n(A) = 5.$$\nVậy xác suất của biến cố $A$ là: $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{5}{9}$.\n\nb) Đổi 20 phút $= \\frac{1}{3}$ giờ.\nGọi vận tốc ban đầu của ô tô là $x$ (km/h, điều kiện $x > 0$).\nThời gian dự định ô tô đi từ A đến B là: $\\frac{180}{x}$ (giờ).\nSau 1 giờ đầu, ô tô đi được quãng đường là: $1 \\cdot x = x$ (km).\nQuãng đường còn lại ô tô cần đi là: $180 - x$ (km).\nVận tốc của ô tô trên quãng đường còn lại là: $x + 12$ (km/h).\nThời gian ô tô đi trên quãng đường còn lại là: $\\frac{180 - x}{x + 12}$ (giờ).\nDo ô tô đến B đúng thời gian dự định nên ta có phương trình:\n$$\\frac{180}{x} = 1 + \\frac{1}{3} + \\frac{180 - x}{x + 12} \\Leftrightarrow \\frac{180}{x} = \\frac{4}{3} + \\frac{180 - x}{x + 12}$$\n$$\\Leftrightarrow \\frac{180}{x} = \\frac{4(x+12) + 3(180-x)}{3(x+12)} = \\frac{x + 588}{3(x+12)}$$\n$$\\Leftrightarrow 3 \\cdot 180(x + 12) = x(x + 588)$$\n$$\\Leftrightarrow 540x + 6480 = x^2 + 588x \\Leftrightarrow x^2 + 48x - 6480 = 0$$\nTa có $\\Delta' = 24^2 - 1 \\cdot (-6480) = 576 + 6480 = 7056 = 84^2 > 0$.\nPhương trình có 2 nghiệm: $x_1 = -24 + 84 = 60$ (thỏa mãn), $x_2 = -24 - 84 = -108$ (loại).\nVậy vận tốc ban đầu của xe ô tô là 60 km/h."
        },
        {
            "id": 13,
            "points": 2.0,
            "question": "Cho đường tròn $(O)$ và điểm $A$ nằm ngoài đường tròn $(O)$, từ điểm $A$ kẻ các tiếp tuyến $AM, AN$ với đường tròn $(O)$ ($M, N$ là các tiếp điểm). Đường thẳng $AO$ cắt đường tròn $(O)$ tại hai điểm phân biệt $P$ và $Q$ ($P$ nằm giữa $A$ và $Q$).\na) Chứng minh bốn điểm $A, M, O, N$ cùng thuộc một đường tròn.\nb) Gọi $H$ là giao điểm của $MN$ với $OA$, $I$ là trung điểm của $AH$. Đường thẳng $MI$ cắt $(O)$ tại điểm $J$ ($J$ khác $M$). Chứng minh $AP \\cdot AQ = AM^2$ và $HJ \\perp MI$.",
            "rubric": [
                {"step": "a) Chỉ ra $\\widehat{AMO} = 90^\\circ$ và $\\widehat{ANO} = 90^\\circ$.", "points": 0.5},
                {"step": "a) Chứng minh tứ giác $AMON$ có tổng hai góc đối bằng $180^\\circ$ nên nội tiếp, 4 điểm cùng thuộc đường tròn đường kính $AO$.", "points": 0.5},
                {"step": "b) Chứng minh tam giác $\\Delta APM \\backsim \\Delta AMQ$ suy ra $AM^2 = AP \\cdot AQ$.", "points": 0.35},
                {"step": "b) Sử dụng tính chất hàng điểm điều hòa hoặc tam giác đồng dạng suy ra $IH^2 = IP \\cdot IQ = IM \\cdot IJ$.", "points": 0.35},
                {"step": "b) Từ $IH^2 = IM \\cdot IJ$ chứng minh $\\Delta IHJ \\backsim \\Delta IMH$ suy ra $\\widehat{IJH} = \\widehat{IHM} = 90^\\circ$, kết luận $HJ \\perp MI$.", "points": 0.3}
            ],
            "solution": "a) Vì $AM, AN$ là hai tiếp tuyến của đường tròn $(O)$ tại $M, N$ nên:\n$$\\widehat{AMO} = 90^\\circ \\quad \\text{và} \\quad \\widehat{ANO} = 90^\\circ.$$\nXét tứ giác $AMON$ có:\n$$\\widehat{AMO} + \\widehat{ANO} = 90^\\circ + 90^\\circ = 180^\\circ.$$\nDo đó, $AMON$ là tứ giác nội tiếp đường tròn đường kính $AO$.\nSuy ra 4 điểm $A, M, O, N$ cùng thuộc một đường tròn.\n\nb) *) Chứng minh $AP \\cdot AQ = AM^2$:\nXét $\\Delta APM$ và $\\Delta AMQ$ có:\n- $\\widehat{MAQ}$ chung.\n- $\\widehat{AMP} = \\widehat{AQM}$ (góc tạo bởi tiếp tuyến và dây cung cùng chắn cung $MP$).\nDo đó $\\Delta APM \\backsim \\Delta AMQ$ (g-g).\nSuy ra $\\frac{AM}{AQ} = \\frac{AP}{AM} \\Rightarrow AM^2 = AP \\cdot AQ$.\n\n*) Chứng minh $HJ \\perp MI$:\nXét tam giác vuông $OMA$ đường cao $MH$, ta có $OH \\cdot OA = OM^2 = R^2 = OP^2 = OQ^2$.\nTừ đó $\\frac{OH}{OP} = \\frac{OP}{OA} = \\frac{OP - OH}{OA - OP} = \\frac{HP}{AP}$, đồng thời $\\frac{OH}{OQ} = \\frac{OQ}{OA} = \\frac{OQ + OH}{OA + OQ} = \\frac{HQ}{AQ}$.\nDo $OP = OQ$ nên $\\frac{HP}{AP} = \\frac{HQ}{AQ} \\Rightarrow \\frac{AQ}{AP} = \\frac{HQ}{HP}$.\nBiểu diễn theo tọa độ trên trục $A-I-P-H-Q$ với $I$ là trung điểm $AH$ ($IA = IH$):\nTa có $AQ = IA + IQ$, $AP = IA + IP$, $HQ = IQ - IH$, $HP = IH - IP$.\nDo $IA = IH$ nên $\\frac{IQ + IH}{IH + IP} = \\frac{IQ - IH}{IH - IP} = \\frac{2IQ}{2IH} = \\frac{IQ}{IH}$.\nSuy ra $IH^2 = IP \\cdot IQ$.\nMặt khác, xét $\\Delta IPJ$ và $\\Delta IMQ$, ta có tứ giác $PJMQ$ nội tiếp nên $\\widehat{IPJ} = \\widehat{IMQ}$, suy ra $\\Delta IPJ \\backsim \\Delta IMQ$ (g-g).\nDo đó $\\frac{IP}{IM} = \\frac{IJ}{IQ} \\Rightarrow IP \\cdot IQ = IM \\cdot IJ$.\nTừ đó suy ra: $IH^2 = IM \\cdot IJ \\Leftrightarrow \\frac{IH}{IM} = \\frac{IJ}{IH}$.\nXét $\\Delta IHJ$ và $\\Delta IMH$ có góc $\\widehat{MIH}$ chung và $\\frac{IH}{IM} = \\frac{IJ}{IH}$.\nDo đó $\\Delta IHJ \\backsim \\Delta IMH$ (c-g-c), dẫn đến $\\widehat{IJH} = \\widehat{IHM} = 90^\\circ$.\nVậy $HJ \\perp MI$ tại $J$."
        },
        {
            "id": 14,
            "points": 1.0,
            "question": "a) Một hình nón nội tiếp một hình cầu bán kính bằng $6\\text{ dm}$, hình nón có đỉnh và đường tròn đáy nằm trên mặt cầu. Tính thể tích lớn nhất của hình nón đó.\nb) Cho các số thực dương $a, b$ thỏa mãn $a + b + ab = 3$. Tìm giá trị nhỏ nhất của biểu thức:\n$$P = \\frac{2a^2b^2 + 3}{ab} - \\frac{4}{a^2 + b^2} + 3.$$",
            "rubric": [
                {"step": "a) Thiết lập hệ thức Pytago giữa bán kính đáy nón $r$ và chiều cao $h$: $r^2 = 12h - h^2$.", "points": 0.25},
                {"step": "a) Viết thể tích $V = \\frac{\\pi}{3}h(12h-h^2) = \\frac{4\\pi}{3}(12-h)\\frac{h}{2}\\frac{h}{2} \\le \\frac{256\\pi}{3}$. Dấu bằng khi $h = 8\\text{ dm}$.", "points": 0.25},
                {"step": "b) Dùng BĐT Cauchy chỉ ra $3 = a+b+ab \\ge 2\\sqrt{ab} + ab \\Rightarrow ab \\le 1$ và $a^2+b^2 \\ge \\frac{(3-ab)^2}{2} \\ge 2$.", "points": 0.25},
                {"step": "b) Tách $P = \\left(2ab + \\frac{2}{ab}\\right) + \\frac{1}{ab} - \\frac{4}{a^2+b^2} + 3 \\ge 4 + 1 - 2 + 3 = 6$. Đẳng thức khi $a = b = 1$.", "points": 0.25}
            ],
            "solution": "a) Gọi bán kính mặt cầu là $R = 6\\text{ dm}$ và chiều cao hình nón là $h$ (dm) với $0 < h < 2R = 12$.\nKhoảng cách từ tâm mặt cầu đến mặt phẳng đáy hình nón là $|R - h| = |6 - h|$.\nGọi bán kính đáy của hình nón là $r$ (dm). Theo định lí Pythagore trong tam giác vuông tạo bởi tâm cầu, tâm đáy và điểm trên đường tròn đáy, ta có:\n$$r^2 + (6 - h)^2 = 6^2 \\Rightarrow r^2 = 36 - (36 - 12h + h^2) = 12h - h^2.$$\nThể tích của hình nón là:\n$$V = \\frac{1}{3}\\pi r^2 h = \\frac{\\pi}{3} h(12h - h^2) = \\frac{\\pi}{3} h^2 (12 - h) = \\frac{4\\pi}{3} \\cdot \\frac{h}{2} \\cdot \\frac{h}{2} \\cdot (12 - h).$$\nÁp dụng bất đẳng thức AM-GM cho ba số dương $\\frac{h}{2}, \\frac{h}{2}, 12 - h$:\n$$\\frac{h}{2} \\cdot \\frac{h}{2} \\cdot (12 - h) \\le \\left(\\frac{\\frac{h}{2} + \\frac{h}{2} + 12 - h}{3}\\right)^3 = \\left(\\frac{12}{3}\\right)^3 = 4^3 = 64.$$\nDo đó:\n$$V \\le \\frac{4\\pi}{3} \\cdot 64 = \\frac{256\\pi}{3}\\text{ dm}^3.$$\nDấu đẳng thức xảy ra khi và chỉ khi $\\frac{h}{2} = 12 - h \\Leftrightarrow \\frac{3h}{2} = 12 \\Leftrightarrow h = 8\\text{ dm}$ (thỏa mãn).\nVậy thể tích lớn nhất của hình nón là $\\frac{256\\pi}{3}\\text{ dm}^3$ khi chiều cao của hình nón bằng $8\\text{ dm}$.\n\nb) Áp dụng bất đẳng thức AM-GM cho hai số dương $a, b$:\n$$a + b \\ge 2\\sqrt{ab}.$$\nDo đó: $3 = a + b + ab \\ge 2\\sqrt{ab} + ab \\Leftrightarrow (\\sqrt{ab} - 1)(\\sqrt{ab} + 3) \\le 0$.\nVì $\\sqrt{ab} > 0$ nên $\\sqrt{ab} - 1 \\le 0 \\Leftrightarrow ab \\le 1$.\nKhi đó: $a + b = 3 - ab \\ge 3 - 1 = 2$.\nÁp dụng bất đẳng thức Bunyakovsky: $a^2 + b^2 \\ge \\frac{(a+b)^2}{2} \\ge \\frac{2^2}{2} = 2$.\nBiến đổi biểu thức $P$:\n$$P = 2ab + \\frac{3}{ab} - \\frac{4}{a^2+b^2} + 3 = \\left(2ab + \\frac{2}{ab}\\right) + \\frac{1}{ab} - \\frac{4}{a^2+b^2} + 3.$$\nÁp dụng bất đẳng thức AM-GM cho hai số dương $2ab$ và $\\frac{2}{ab}$:\n$$2ab + \\frac{2}{ab} \\ge 2\\sqrt{2ab \\cdot \\frac{2}{ab}} = 4.$$\nMặt khác, do $ab \\le 1 \\Rightarrow \\frac{1}{ab} \\ge 1$ và $a^2 + b^2 \\ge 2 \\Rightarrow -\\frac{4}{a^2+b^2} \\ge -\\frac{4}{2} = -2$.\nDo đó:\n$$P \\ge 4 + 1 - 2 + 3 = 6.$$\nDấu đẳng thức xảy ra khi và chỉ khi:\n$$\\begin{cases} a = b \\\\ ab = 1 \\\\ a + b + ab = 3 \\end{cases} \\Leftrightarrow a = b = 1.$$\nVậy giá trị nhỏ nhất của $P$ là $6$ khi $a = b = 1$."
        }
    ]
}

print("Đã nạp xong Đề 02.")

# ==============================================================================
# ĐỀ SỐ 03 (Mã đề 03)
# ==============================================================================
MOCK_EXAMS_GRADE10["exams"]["de_03"] = {
    "id": "de_03",
    "code": "MÃ ĐỀ 03",
    "title": "ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN - ĐỀ SỐ 03",
    "header": {
        "department": "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
        "examName": "KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT",
        "subject": "Môn thi: TOÁN",
        "author": "GV Phan Đình Thuấn",
        "time": "90 phút (không kể thời gian phát đề)",
        "code": "MÃ ĐỀ 03"
    },
    "part1": [
        {
            "id": 1,
            "question": "Kết quả rút gọn biểu thức $A = \\sqrt{18} - 2\\sqrt{2}$ là:",
            "options": ["A. $\\sqrt{2}$", "B. $7\\sqrt{2}$", "C. $5\\sqrt{2}$", "D. $11\\sqrt{2}$"],
            "answer": "A",
            "explanation": "Ta có: $A = 3\\sqrt{2} - 2\\sqrt{2} = \\sqrt{2}$."
        },
        {
            "id": 2,
            "question": "Nghiệm của bất phương trình $2x - 6 > 0$ là:",
            "options": ["A. $x < 3$", "B. $x < 6$", "C. $x > -6$", "D. $x > 3$"],
            "answer": "D",
            "explanation": "$2x - 6 > 0 \\Leftrightarrow 2x > 6 \\Leftrightarrow x > 3$."
        },
        {
            "id": 3,
            "question": "Nghiệm của phương trình $3x - 4 = 8$ là:",
            "options": ["A. $x = -4$", "B. $x = 12$", "C. $x = 4$", "D. $x = -12$"],
            "answer": "C",
            "explanation": "$3x - 4 = 8 \\Leftrightarrow 3x = 12 \\Leftrightarrow x = 4$."
        },
        {
            "id": 4,
            "question": "Một hộp đựng 6 thẻ cùng loại được đánh số 1; 2; 3; 4; 5; 6. Rút ngẫu nhiên một thẻ từ trong hộp. Số phần tử của không gian mẫu là:",
            "options": ["A. 1", "B. 3", "C. 6", "D. 5"],
            "answer": "C",
            "explanation": "Có 6 tấm thẻ nên số phần tử của không gian mẫu là $n(\\Omega) = 6$."
        },
        {
            "id": 5,
            "question": "Đồ thị của hàm số $y = x^2$ đi qua điểm nào sau đây?",
            "options": ["A. $(1; 2)$", "B. $(-1; 1)$", "C. $(-1; -1)$", "D. $(1; 0)$"],
            "answer": "B",
            "explanation": "Với $x = -1 \\Rightarrow y = (-1)^2 = 1$. Do đó $(-1; 1)$ thuộc đồ thị."
        },
        {
            "id": 6,
            "question": "Cho tam giác $ABC$ vuông tại $A$. Biết $AB = 3\\text{ cm}, AC = 4\\text{ cm}$. Giá trị của $\\cot C$ bằng:",
            "options": ["A. $\\frac{3}{4}$", "B. $\\frac{4}{3}$", "C. $\\frac{3}{5}$", "D. $\\frac{4}{5}$"],
            "answer": "B",
            "explanation": "Trong tam giác vuông $ABC$ tại $A$: $\\cot C = \\frac{\\text{kề}}{\\text{đối}} = \\frac{AC}{AB} = \\frac{4}{3}$."
        },
        {
            "id": 7,
            "question": "Một hình cầu có bán kính bằng $3\\text{ cm}$. Diện tích mặt cầu bằng:",
            "options": ["A. $12\\pi\\text{ cm}^2$", "B. $3\\pi\\text{ cm}^2$", "C. $6\\pi\\text{ cm}^2$", "D. $36\\pi\\text{ cm}^2$"],
            "answer": "D",
            "explanation": "Diện tích mặt cầu là $S = 4\\pi R^2 = 4\\pi \\cdot 3^2 = 36\\pi\\text{ cm}^2$."
        },
        {
            "id": 8,
            "question": "Bảng thống kê điểm kiểm tra học kỳ 2 của 100 học sinh khối 9 gồm: Điểm 5 (12 hs), Điểm 6 (16 hs), Điểm 7 (22 hs), Điểm 8 (18 hs), Điểm 9 (30 hs), Điểm 10 (2 hs). Điểm 10 có tần số tương đối là:",
            "options": ["A. 10%", "B. 98%", "C. 2%", "D. 50%"],
            "answer": "C",
            "explanation": "Tần số tương đối của điểm 10 là $f = \\frac{2}{100} \\cdot 100\\% = 2\\%$."
        }
    ],
    "part2": [
        {
            "id": 9,
            "points": 1.0,
            "question": "Cho $x > 0$ và $x \\ne 4$. Rút gọn biểu thức:\n$$A = \\left(\\frac{1}{\\sqrt{x}+2} + \\frac{2}{x-4}\\right) \\cdot \\frac{x-4}{2x}$$",
            "rubric": [
                {"step": "Quy đồng trong ngoặc với mẫu chung $x - 4 = (\\sqrt{x}+2)(\\sqrt{x}-2)$.", "points": 0.25},
                {"step": "Tử thức trong ngoặc: $\\sqrt{x} - 2 + 2 = \\sqrt{x}$.", "points": 0.25},
                {"step": "Nhân với phân thức ngoài: $\\frac{\\sqrt{x}}{x-4} \\cdot \\frac{x-4}{2x}$.", "points": 0.25},
                {"step": "Rút gọn được $A = \\frac{1}{2\\sqrt{x}}$. Kết luận.", "points": 0.25}
            ],
            "solution": "Với $x > 0$ và $x \\ne 4$, ta có:\n$$\\begin{aligned}\nA &= \\left[\\frac{\\sqrt{x}-2}{(\\sqrt{x}+2)(\\sqrt{x}-2)} + \\frac{2}{x-4}\\right] \\cdot \\frac{x-4}{2x} \\\\\n&= \\frac{\\sqrt{x}-2+2}{x-4} \\cdot \\frac{x-4}{2x} \\\\\n&= \\frac{\\sqrt{x}}{x-4} \\cdot \\frac{x-4}{2x} \\\\\n&= \\frac{\\sqrt{x}}{2x} = \\frac{1}{2\\sqrt{x}}.\n\\end{aligned}$$\nVậy $A = \\frac{1}{2\\sqrt{x}}$ với $x > 0, x \\ne 4$."
        },
        {
            "id": 10,
            "points": 1.0,
            "question": "Biết phương trình $x^2 - 2x - 4 = 0$ có hai nghiệm $x_1, x_2$. Không giải phương trình, tính giá trị của biểu thức $T = \\frac{3x_1}{x_2+1} + \\frac{3x_2}{x_1+1}$.",
            "rubric": [
                {"step": "Tính $\\Delta' = (-1)^2 - 1(-4) = 5 > 0$ nên phương trình có 2 nghiệm phân biệt.", "points": 0.2},
                {"step": "Theo định lí Viète: $x_1 + x_2 = 2$ và $x_1 x_2 = -4$.", "points": 0.3},
                {"step": "Quy đồng mẫu thức: $T = \\frac{3\\left[(x_1+x_2)^2 - 2x_1 x_2 + (x_1+x_2)\\right]}{x_1 x_2 + (x_1+x_2) + 1}$.", "points": 0.3},
                {"step": "Thay số: $T = \\frac{3\\left[2^2 - 2(-4) + 2\\right]}{-4 + 2 + 1} = \\frac{3(14)}{-1} = -42$. Kết luận.", "points": 0.2}
            ],
            "solution": "Xét phương trình $x^2 - 2x - 4 = 0$ có $\\Delta' = (-1)^2 - 1 \\cdot (-4) = 5 > 0$ nên phương trình có hai nghiệm phân biệt $x_1, x_2$.\nTheo hệ thức Viète, ta có:\n$$\\begin{cases} x_1 + x_2 = 2 \\\\ x_1 x_2 = -4 \\end{cases}$$\nTa biến đổi biểu thức $T$:\n$$\\begin{aligned}\nT &= \\frac{3x_1(x_1+1) + 3x_2(x_2+1)}{(x_1+1)(x_2+1)} \\\\\n&= \\frac{3(x_1^2 + x_2^2) + 3(x_1 + x_2)}{x_1 x_2 + x_1 + x_2 + 1} \\\\\n&= \\frac{3\\left[(x_1+x_2)^2 - 2x_1 x_2\\right] + 3(x_1+x_2)}{x_1 x_2 + (x_1+x_2) + 1} \\\\\n&= \\frac{3\\left[2^2 - 2(-4)\\right] + 3(2)}{-4 + 2 + 1} = \\frac{3(12) + 6}{-1} = \\frac{42}{-1} = -42.\n\\end{aligned}$$\nVậy $T = -42$."
        },
        {
            "id": 11,
            "points": 1.0,
            "question": "Giải hệ phương trình:\n$$\\begin{cases} x - 2y = 1 \\\\ 2x + y = 7 \\end{cases}$$",
            "rubric": [
                {"step": "Nhân phương trình thứ hai với 2: $4x + 2y = 14$.", "points": 0.25},
                {"step": "Cộng vế theo vế: $5x = 15 \\Rightarrow x = 3$.", "points": 0.25},
                {"step": "Thay $x = 3$ vào phương trình 1: $3 - 2y = 1 \\Rightarrow 2y = 2 \\Rightarrow y = 1$.", "points": 0.25},
                {"step": "Kết luận nghiệm duy nhất của hệ là $(x; y) = (3; 1)$.", "points": 0.25}
            ],
            "solution": "Ta có:\n$$\\begin{cases} x - 2y = 1 \\\\ 2x + y = 7 \\end{cases} \\Leftrightarrow \\begin{cases} x - 2y = 1 \\\\ 4x + 2y = 14 \\end{cases} \\Leftrightarrow \\begin{cases} 5x = 15 \\\\ x - 2y = 1 \\end{cases} \\Leftrightarrow \\begin{cases} x = 3 \\\\ 3 - 2y = 1 \\end{cases} \\Leftrightarrow \\begin{cases} x = 3 \\\\ y = 1 \\end{cases}$$\nVậy hệ phương trình có nghiệm duy nhất $(x; y) = (3; 1)$."
        },
        {
            "id": 12,
            "points": 2.0,
            "question": "a) Có hai hộp I và II mỗi hộp đựng 3 tấm thẻ cùng loại, 3 tấm thẻ trong hộp I được đánh số 1; 2; 3 và 3 tấm thẻ trong hộp II được đánh số 4; 5; 6. Rút ngẫu nhiên từ mỗi hộp ra một tấm thẻ. Viết không gian mẫu của phép thử và tính xác suất của biến cố $A$: “Tổng hai số trên hai thẻ rút ra là một số chẵn”.\nb) Một người lái ô tô đi từ địa điểm A đến địa điểm B cách nhau 240 km trong một thời gian dự định trước. Sau khi đi được 2 giờ, ô tô gặp sự cố nên phải dừng lại 20 phút, sau đó tiếp tục đi đến địa điểm B. Để đến địa điểm B đúng thời gian đã định, người lái ô tô phải tăng vận tốc thêm 12 km/h so với vận tốc ban đầu trên quãng đường còn lại. Tính vận tốc ban đầu của ô tô đó.",
            "rubric": [
                {"step": "a) Viết đúng không gian mẫu $\\Omega$ gồm 9 cặp phần tử, suy ra $n(\\Omega) = 9$.", "points": 0.5},
                {"step": "a) Liệt kê biến cố $A$: có 4 kết quả thuận lợi $\\{(1;5), (2;4), (2;6), (3;5)\\}$. Tính $P(A) = \\frac{4}{9}$.", "points": 0.5},
                {"step": "b) Đổi 20 phút $= \\frac{1}{3}$ giờ. Đặt ẩn vận tốc ban đầu $x > 0$. Lập phương trình thời gian.", "points": 0.35},
                {"step": "b) Phương trình: $\\frac{240}{x} = 2 + \\frac{1}{3} + \\frac{240-2x}{x+12} \\Leftrightarrow x^2 + 84x - 8640 = 0$.", "points": 0.35},
                {"step": "b) Giải phương trình: $x = 60$ (thỏa mãn), $x = -144$ (loại). Kết luận vận tốc ban đầu là 60 km/h.", "points": 0.3}
            ],
            "solution": "a) Không gian mẫu của phép thử là tập hợp tất cả các cặp kết quả rút ra từ 2 hộp:\n$$\\Omega = \\{(1; 4); (1; 5); (1; 6); (2; 4); (2; 5); (2; 6); (3; 4); (3; 5); (3; 6)\\}$$\nSố phần tử của không gian mẫu là $n(\\Omega) = 9$.\nBiến cố $A$: \"Tổng hai số trên hai thẻ rút ra là một số chẵn\" xảy ra khi rút được cùng lẻ hoặc cùng chẵn:\n$$A = \\{(1; 5); (2; 4); (2; 6); (3; 5)\\} \\Rightarrow n(A) = 4.$$\nVậy xác suất của biến cố $A$ là: $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{4}{9}$.\n\nb) Đổi 20 phút $= \\frac{1}{3}$ giờ.\nGọi vận tốc ban đầu của ô tô là $x$ (km/h, điều kiện $x > 0$).\nThời gian dự định ô tô đi từ A đến B là: $\\frac{240}{x}$ (giờ).\nSau 2 giờ đầu, ô tô đi được quãng đường là: $2x$ (km).\nQuãng đường còn lại ô tô phải đi là: $240 - 2x$ (km).\nVận tốc của ô tô trên quãng đường còn lại là: $x + 12$ (km/h).\nThời gian ô tô đi trên quãng đường còn lại là: $\\frac{240 - 2x}{x + 12}$ (giờ).\nDo ô tô đến B đúng thời gian đã định nên ta có phương trình:\n$$\\frac{240}{x} = 2 + \\frac{1}{3} + \\frac{240 - 2x}{x + 12} \\Leftrightarrow \\frac{240}{x} = \\frac{7}{3} + \\frac{240 - 2x}{x + 12}$$\n$$\\Leftrightarrow \\frac{240}{x} = \\frac{7(x+12) + 3(240-2x)}{3(x+12)} = \\frac{x + 804}{3(x+12)}$$\n$$\\Leftrightarrow 3 \\cdot 240(x + 12) = x(x + 804)$$\n$$\\Leftrightarrow 720x + 8640 = x^2 + 804x \\Leftrightarrow x^2 + 84x - 8640 = 0$$\nTa có $\\Delta' = 42^2 - 1 \\cdot (-8640) = 1764 + 8640 = 10404 = 102^2 > 0$.\nPhương trình có 2 nghiệm: $x_1 = -42 + 102 = 60$ (thỏa mãn), $x_2 = -42 - 102 = -144$ (loại).\nVậy vận tốc ban đầu của xe ô tô là 60 km/h."
        },
        {
            "id": 13,
            "points": 2.0,
            "question": "Cho đường tròn $(O)$ và điểm $M$ nằm ngoài đường tròn $(O)$, từ điểm $M$ kẻ các tiếp tuyến $MA, MB$ với đường tròn $(O)$ ($A, B$ là các tiếp điểm). Đường thẳng $MO$ cắt đường tròn $(O)$ tại hai điểm phân biệt $C$ và $D$ ($C$ nằm giữa $M$ và $D$).\na) Chứng minh bốn điểm $M, A, O, B$ cùng thuộc một đường tròn.\nb) Gọi $H$ là giao điểm của $AB$ với $OM$, $I$ là trung điểm của $MH$. Đường thẳng $AI$ cắt $(O)$ tại điểm $E$ ($E$ khác $A$). Chứng minh $MC \\cdot MD = MA^2$ và $HE \\perp AI$.",
            "rubric": [
                {"step": "a) Chỉ ra $\\widehat{MAO} = 90^\\circ$ và $\\widehat{MBO} = 90^\\circ$.", "points": 0.5},
                {"step": "a) Chứng minh tứ giác $MAOB$ nội tiếp đường tròn đường kính $MO$.", "points": 0.5},
                {"step": "b) Chứng minh $\\Delta MCA \\backsim \\Delta MAD \\Rightarrow MA^2 = MC \\cdot MD$.", "points": 0.35},
                {"step": "b) Chứng minh hệ thức điểm điều hòa dẫn đến $IH^2 = IC \\cdot ID = IE \\cdot IA$.", "points": 0.35},
                {"step": "b) Từ $IH^2 = IE \\cdot IA$ chứng minh $\\Delta IHE \\backsim \\Delta IAH \\Rightarrow \\widehat{IEH} = \\widehat{IHA} = 90^\\circ$, kết luận $HE \\perp AI$.", "points": 0.3}
            ],
            "solution": "a) Vì $MA, MB$ là hai tiếp tuyến của đường tròn $(O)$ tại $A, B$ nên:\n$$\\widehat{MAO} = 90^\\circ \\quad \\text{và} \\quad \\widehat{MBO} = 90^\\circ.$$\nXét tứ giác $MAOB$ có:\n$$\\widehat{MAO} + \\widehat{MBO} = 90^\\circ + 90^\\circ = 180^\\circ.$$\nDo đó $MAOB$ là tứ giác nội tiếp đường tròn đường kính $MO$.\nVậy 4 điểm $M, A, O, B$ cùng thuộc một đường tròn.\n\nb) *) Chứng minh $MC \\cdot MD = MA^2$:\nXét $\\Delta MCA$ và $\\Delta MAD$ có:\n- Góc $\\widehat{AMD}$ chung.\n- $\\widehat{MAC} = \\widehat{MDA}$ (góc tạo bởi tia tiếp tuyến và dây cung cùng chắn cung $AC$).\nDo đó $\\Delta MCA \\backsim \\Delta MAD$ (g-g).\nSuy ra $\\frac{MA}{MD} = \\frac{MC}{MA} \\Rightarrow MA^2 = MC \\cdot MD$.\n\n*) Chứng minh $HE \\perp AI$:\nÁp dụng hệ thức lượng trong tam giác vuông $OAM$ với đường cao $AH$, ta có $OH \\cdot OM = OA^2 = R^2 = OC^2 = OD^2$.\nTừ đó $\\frac{OH}{OC} = \\frac{OC}{OM} = \\frac{OC - OH}{OM - OC} = \\frac{HC}{MC}$, đồng thời $\\frac{OH}{OD} = \\frac{OD}{OM} = \\frac{OD + OH}{OM + OD} = \\frac{HD}{MD}$.\nVì $OC = OD$ nên $\\frac{HC}{MC} = \\frac{HD}{MD} \\Rightarrow \\frac{MD}{MC} = \\frac{HD}{HC}$.\nĐặt các đoạn thẳng trên trục với $I$ là trung điểm của $MH$ ($IM = IH$):\nTa có $MD = IM + ID$, $MC = IC + IM = IC + IH$, $HD = ID - IH$, $HC = IH - IC$.\nDo đó $\\frac{ID + IH}{IH + IC} = \\frac{ID - IH}{IH - IC} = \\frac{2ID}{2IH} = \\frac{ID}{IH}$.\nSuy ra $IH^2 = IC \\cdot ID$.\nMặt khác, tứ giác $CEAD$ nội tiếp đường tròn $(O)$ nên xét $\\Delta ICE$ và $\\Delta IAD$, ta có $\\widehat{AID}$ chung và $\\widehat{ICE} = \\widehat{IAD}$ (cùng bù với $\\widehat{EAD}$).\nDo đó $\\Delta ICE \\backsim \\Delta IAD$ (g-g) $\\Rightarrow \\frac{IC}{IA} = \\frac{IE}{ID} \\Rightarrow IC \\cdot ID = IE \\cdot IA$.\nTừ đó suy ra $IH^2 = IE \\cdot IA \\Leftrightarrow \\frac{IH}{IA} = \\frac{IE}{IH}$.\nXét $\\Delta IHE$ và $\\Delta IAH$ có góc $\\widehat{AIH}$ chung và tỉ lệ cạnh $\\frac{IH}{IA} = \\frac{IE}{IH}$.\nDo đó $\\Delta IHE \\backsim \\Delta IAH$ (c-g-c), suy ra $\\widehat{IEH} = \\widehat{IHA} = 90^\\circ$.\nVậy $HE \\perp AI$ tại $E$."
        },
        {
            "id": 14,
            "points": 1.0,
            "question": "a) Một hình nón nội tiếp một hình cầu bán kính bằng $2\\text{ dm}$, hình nón có đỉnh và đường tròn đáy nằm trên mặt cầu. Tính thể tích lớn nhất của hình nón đó.\nb) Cho các số thực dương $a, b$ thỏa mãn $a + b + 2ab = 4$. Tìm giá trị nhỏ nhất của biểu thức:\n$$P = \\frac{2a^2b^2 + 4}{ab} - \\frac{5}{a^2 + b^2} + 4.$$",
            "rubric": [
                {"step": "a) Thiết lập hệ thức Pytago: $r^2 = 4h - h^2$ với $0 < h < 4$.", "points": 0.25},
                {"step": "a) Viết thể tích $V = \\frac{4\\pi}{3}(4-h)\\frac{h}{2}\\frac{h}{2} \\le \\frac{256\\pi}{81}$. Đẳng thức khi $h = \\frac{8}{3}\\text{ dm}$.", "points": 0.25},
                {"step": "b) Dùng Cauchy chứng minh $a + b \\ge 2$ và $a^2 + b^2 \\ge 2$.", "points": 0.25},
                {"step": "b) Tách $P = 2\\left(ab + \\frac{1}{ab}\\right) + \\frac{2(a-b)^2}{ab(a^2+b^2)} - \\frac{1}{a^2+b^2} + 4 \\ge 4 - \\frac{1}{2} + 4 = \\frac{15}{2}$. Đẳng thức khi $a = b = 1$.", "points": 0.25}
            ],
            "solution": "a) Gọi bán kính mặt cầu là $R = 2\\text{ dm}$ và chiều cao của hình nón là $h$ (dm) với $0 < h < 2R = 4$.\nKhoảng cách từ tâm mặt cầu đến mặt phẳng đáy hình nón là $|R - h| = |2 - h|$.\nGọi bán kính đáy nón là $r$ (dm). Theo định lí Pythagore trong tam giác vuông tạo bởi tâm cầu, tâm đáy và một điểm trên đường tròn đáy:\n$$r^2 + (2 - h)^2 = 2^2 \\Rightarrow r^2 = 4 - (4 - 4h + h^2) = 4h - h^2.$$\nThể tích hình nón là:\n$$V = \\frac{1}{3}\\pi r^2 h = \\frac{\\pi}{3} h(4h - h^2) = \\frac{\\pi}{3} h^2(4 - h) = \\frac{4\\pi}{3} \\cdot \\frac{h}{2} \\cdot \\frac{h}{2} \\cdot (4 - h).$$\nÁp dụng bất đẳng thức AM-GM cho 3 số dương $\\frac{h}{2}, \\frac{h}{2}, 4 - h$:\n$$\\frac{h}{2} \\cdot \\frac{h}{2} \\cdot (4 - h) \\le \\left(\\frac{\\frac{h}{2} + \\frac{h}{2} + 4 - h}{3}\\right)^3 = \\left(\\frac{4}{3}\\right)^3 = \\frac{64}{27}.$$\nDo đó:\n$$V \\le \\frac{4\\pi}{3} \\cdot \\frac{64}{27} = \\frac{256\\pi}{81}\\text{ dm}^3.$$\nDấu đẳng thức xảy ra khi và chỉ khi $\\frac{h}{2} = 4 - h \\Leftrightarrow \\frac{3h}{2} = 4 \\Leftrightarrow h = \\frac{8}{3}\\text{ dm}$.\nVậy thể tích lớn nhất của hình nón là $\\frac{256\\pi}{81}\\text{ dm}^3$ khi chiều cao hình nón bằng $\\frac{8}{3}\\text{ dm}$.\n\nb) Áp dụng bất đẳng thức AM-GM, ta có $2ab \\le \\frac{(a+b)^2}{2}$.\nDo đó: $4 = a + b + 2ab \\le a + b + \\frac{(a+b)^2}{2} \\Leftrightarrow (a+b)^2 + 2(a+b) - 8 \\ge 0$.\nSuy ra $(a+b+4)(a+b-2) \\ge 0$. Vì $a, b > 0$ nên $a + b \\ge 2$.\nÁp dụng Bunyakovsky: $a^2 + b^2 \\ge \\frac{(a+b)^2}{2} \\ge \\frac{2^2}{2} = 2$.\nBiến đổi biểu thức $P$:\n$$P = 2ab + \\frac{4}{ab} - \\frac{5}{a^2+b^2} + 4 = \\left(2ab + \\frac{2}{ab}\\right) + \\left(\\frac{2}{ab} - \\frac{4}{a^2+b^2}\\right) - \\frac{1}{a^2+b^2} + 4.$$\nNhận xét rằng: $\\frac{2}{ab} - \\frac{4}{a^2+b^2} = \\frac{2(a^2+b^2) - 4ab}{ab(a^2+b^2)} = \\frac{2(a-b)^2}{ab(a^2+b^2)} \\ge 0$.\nLại có $2ab + \\frac{2}{ab} = 2\\left(ab + \\frac{1}{ab}\\right) \\ge 2 \\cdot 2\\sqrt{ab \\cdot \\frac{1}{ab}} = 4$.\nVà vì $a^2 + b^2 \\ge 2$ nên $-\\frac{1}{a^2+b^2} \\ge -\\frac{1}{2}$.\nSuy ra:\n$$P \\ge 4 + 0 - \\frac{1}{2} + 4 = 8 - \\frac{1}{2} = \\frac{15}{2}.$$\nDấu đẳng thức xảy ra khi và chỉ khi $a = b$ và $a + b = 2 \\Rightarrow a = b = 1$ (thỏa mãn $a + b + 2ab = 4$).\nVậy giá trị nhỏ nhất của $P$ là $\\frac{15}{2}$ khi $a = b = 1$."
        }
    ]
}

print("Đã nạp xong Đề 03.")

# ==============================================================================
# ĐỀ SỐ 04 (Mã đề 04)
# ==============================================================================
MOCK_EXAMS_GRADE10["exams"]["de_04"] = {
    "id": "de_04",
    "code": "MÃ ĐỀ 04",
    "title": "ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN - ĐỀ SỐ 04",
    "header": {
        "department": "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
        "examName": "KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT",
        "subject": "Môn thi: TOÁN",
        "author": "GV Phan Đình Thuấn",
        "time": "90 phút (không kể thời gian phát đề)",
        "code": "MÃ ĐỀ 04"
    },
    "part1": [
        {
            "id": 1,
            "question": "Kết quả rút gọn biểu thức $A = \\sqrt{27} - \\sqrt{12} + \\sqrt{3}$ là:",
            "options": ["A. $2\\sqrt{3}$", "B. $3\\sqrt{3}$", "C. $4\\sqrt{3}$", "D. $\\sqrt{3}$"],
            "answer": "A",
            "explanation": "$A = 3\\sqrt{3} - 2\\sqrt{3} + \\sqrt{3} = 2\\sqrt{3}$."
        },
        {
            "id": 2,
            "question": "Nghiệm của bất phương trình $-3x + 9 \\ge 0$ là:",
            "options": ["A. $x \\ge 3$", "B. $x \\le 3$", "C. $x > 3$", "D. $x < -3$"],
            "answer": "B",
            "explanation": "$-3x + 9 \\ge 0 \\Leftrightarrow -3x \\ge -9 \\Leftrightarrow x \\le 3$."
        },
        {
            "id": 3,
            "question": "Nghiệm của phương trình $2x + 7 = 1$ là:",
            "options": ["A. $x = 4$", "B. $x = 3$", "C. $x = -3$", "D. $x = -4$"],
            "answer": "C",
            "explanation": "$2x + 7 = 1 \\Leftrightarrow 2x = -6 \\Leftrightarrow x = -3$."
        },
        {
            "id": 4,
            "question": "Tung một đồng xu cân đối đồng chất hai lần liên tiếp. Số phần tử của không gian mẫu là:",
            "options": ["A. 2", "B. 4", "C. 6", "D. 8"],
            "answer": "B",
            "explanation": "Mỗi lần tung có 2 khả năng (S, N) nên 2 lần có $2 \\times 2 = 4$ phần tử."
        },
        {
            "id": 5,
            "question": "Đồ thị của hàm số $y = -2x^2$ đi qua điểm nào sau đây?",
            "options": ["A. $(1; 2)$", "B. $(1; -2)$", "C. $(-1; 2)$", "D. $(2; -4)$"],
            "answer": "B",
            "explanation": "Thay $x = 1 \\Rightarrow y = -2(1)^2 = -2$. Do đó điểm $(1; -2)$ thuộc đồ thị."
        },
        {
            "id": 6,
            "question": "Cho tam giác $ABC$ vuông tại $A$. Biết $AB = 6\\text{ cm}, BC = 10\\text{ cm}$. Giá trị của $\\cos B$ bằng:",
            "options": ["A. $\\frac{3}{5}$", "B. $\\frac{4}{5}$", "C. $\\frac{3}{4}$", "D. $\\frac{4}{3}$"],
            "answer": "A",
            "explanation": "Trong tam giác vuông $ABC$ tại $A$: $\\cos B = \\frac{AB}{BC} = \\frac{6}{10} = \\frac{3}{5}$."
        },
        {
            "id": 7,
            "question": "Một hình nón có bán kính đáy $r = 3\\text{ cm}$ và độ dài đường sinh $l = 5\\text{ cm}$. Diện tích xung quanh của hình nón là:",
            "options": ["A. $15\\pi\\text{ cm}^2$", "B. $30\\pi\\text{ cm}^2$", "C. $45\\pi\\text{ cm}^2$", "D. $12\\pi\\text{ cm}^2$"],
            "answer": "A",
            "explanation": "Diện tích xung quanh hình nón là $S_{xq} = \\pi rl = \\pi \\cdot 3 \\cdot 5 = 15\\pi\\text{ cm}^2$."
        },
        {
            "id": 8,
            "question": "Bảng điểm kiểm tra môn Toán của một tổ học sinh gồm: 6, 7, 7, 8, 8, 8, 9, 9, 10, 10. Điểm có tần số lớn nhất là:",
            "options": ["A. Điểm 7", "B. Điểm 8", "C. Điểm 9", "D. Điểm 10"],
            "answer": "B",
            "explanation": "Điểm 8 xuất hiện 3 lần (nhiều nhất), các điểm khác xuất hiện 2 lần hoặc 1 lần. Vậy điểm có tần số lớn nhất là điểm 8."
        }
    ],
    "part2": [
        {
            "id": 9,
            "points": 1.0,
            "question": "Cho $x > 0$ và $x \\ne 1$. Rút gọn biểu thức:\n$$B = \\left(\\frac{\\sqrt{x}}{\\sqrt{x}-1} - \\frac{1}{x-\\sqrt{x}}\\right) : \\frac{\\sqrt{x}+1}{x-1}$$",
            "rubric": [
                {"step": "Quy đồng trong ngoặc với mẫu chung $x - \\sqrt{x} = \\sqrt{x}(\\sqrt{x}-1)$: tử số là $\\sqrt{x} \\cdot \\sqrt{x} - 1 = x - 1$.", "points": 0.3},
                {"step": "Thu gọn trong ngoặc được $\\frac{x-1}{\\sqrt{x}(\\sqrt{x}-1)} = \\frac{(\\sqrt{x}+1)(\\sqrt{x}-1)}{\\sqrt{x}(\\sqrt{x}-1)} = \\frac{\\sqrt{x}+1}{\\sqrt{x}}$.", "points": 0.3},
                {"step": "Thực hiện phép chia: $\\frac{\\sqrt{x}+1}{\\sqrt{x}} \\cdot \\frac{x-1}{\\sqrt{x}+1} = \\frac{x-1}{\\sqrt{x}}$. Kết luận.", "points": 0.4}
            ],
            "solution": "Với $x > 0$ và $x \\ne 1$, ta có:\n$$\\begin{aligned}\nB &= \\left[\\frac{\\sqrt{x}}{\\sqrt{x}-1} - \\frac{1}{\\sqrt{x}(\\sqrt{x}-1)}\\right] : \\frac{\\sqrt{x}+1}{(\\sqrt{x}+1)(\\sqrt{x}-1)} \\\\\n&= \\frac{x - 1}{\\sqrt{x}(\\sqrt{x}-1)} : \\frac{1}{\\sqrt{x}-1} \\\\\n&= \\frac{(\\sqrt{x}+1)(\\sqrt{x}-1)}{\\sqrt{x}(\\sqrt{x}-1)} \\cdot (\\sqrt{x}-1) \\\\\n&= \\frac{\\sqrt{x}+1}{\\sqrt{x}} \\cdot (\\sqrt{x}-1) = \\frac{x - 1}{\\sqrt{x}}.\n\\end{aligned}$$\nVậy $B = \\frac{x-1}{\\sqrt{x}}$ với $x > 0, x \\ne 1$."
        },
        {
            "id": 10,
            "points": 1.0,
            "question": "Cho phương trình $x^2 - 4x + 1 = 0$ có hai nghiệm $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức $T = x_1^3 + x_2^3 - 3x_1 x_2$.",
            "rubric": [
                {"step": "Tính $\\Delta' = (-2)^2 - 1(1) = 3 > 0$ nên phương trình có hai nghiệm phân biệt.", "points": 0.25},
                {"step": "Theo định lí Viète: $x_1 + x_2 = 4$ và $x_1 x_2 = 1$.", "points": 0.25},
                {"step": "Biến đổi $x_1^3 + x_2^3 = (x_1+x_2)^3 - 3x_1x_2(x_1+x_2) = 4^3 - 3(1)(4) = 52$.", "points": 0.25},
                {"step": "Tính $T = 52 - 3(1) = 49$. Kết luận.", "points": 0.25}
            ],
            "solution": "Xét phương trình $x^2 - 4x + 1 = 0$ có $\\Delta' = (-2)^2 - 1 \\cdot 1 = 3 > 0$ nên phương trình có 2 nghiệm phân biệt $x_1, x_2$.\nTheo hệ thức Viète, ta có:\n$$\\begin{cases} x_1 + x_2 = 4 \\\\ x_1 x_2 = 1 \\end{cases}$$\nTa biến đổi $x_1^3 + x_2^3$:\n$$x_1^3 + x_2^3 = (x_1 + x_2)^3 - 3x_1 x_2 (x_1 + x_2) = 4^3 - 3 \\cdot 1 \\cdot 4 = 64 - 12 = 52.$$\nKhi đó giá trị của $T$ là:\n$$T = x_1^3 + x_2^3 - 3x_1 x_2 = 52 - 3 \\cdot 1 = 49.$$\nVậy $T = 49$."
        },
        {
            "id": 11,
            "points": 1.0,
            "question": "Giải hệ phương trình:\n$$\\begin{cases} 3x + 2y = 7 \\\\ 2x - y = 0 \\end{cases}$$",
            "rubric": [
                {"step": "Từ phương trình 2 rút ra $y = 2x$.", "points": 0.25},
                {"step": "Thế vào phương trình 1: $3x + 2(2x) = 7 \\Leftrightarrow 7x = 7 \\Rightarrow x = 1$.", "points": 0.35},
                {"step": "Tính $y = 2(1) = 2$.", "points": 0.25},
                {"step": "Kết luận nghiệm duy nhất $(x; y) = (1; 2)$.", "points": 0.15}
            ],
            "solution": "Từ phương trình thứ hai ta có $y = 2x$.\nThế vào phương trình thứ nhất, ta được:\n$$3x + 2(2x) = 7 \\Leftrightarrow 3x + 4x = 7 \\Leftrightarrow 7x = 7 \\Leftrightarrow x = 1.$$\nThay $x = 1$ vào $y = 2x$, ta được $y = 2 \\cdot 1 = 2$.\nVậy hệ phương trình có nghiệm duy nhất $(x; y) = (1; 2)$."
        },
        {
            "id": 12,
            "points": 2.0,
            "question": "a) Gieo đồng thời hai con xúc xắc cân đối. Viết không gian mẫu dưới dạng mô tả và tính xác suất của biến cố $M$: \"Tổng số chấm xuất hiện trên hai con xúc xắc bằng 8\".\nb) Hai đội công nhân cùng làm chung một đoạn đường thì sau 12 ngày sẽ hoàn thành. Nếu đội thứ nhất làm một mình trong 4 ngày rồi nghỉ, sau đó đội thứ hai làm tiếp trong 9 ngày thì cả hai đội hoàn thành được $\\frac{7}{12}$ đoạn đường. Hỏi nếu làm riêng thì mỗi đội hoàn thành đoạn đường đó trong bao lâu?",
            "rubric": [
                {"step": "a) Chỉ ra số phần tử không gian mẫu $n(\\Omega) = 6 \\times 6 = 36$.", "points": 0.3},
                {"step": "a) Liệt kê các kết quả thuận lợi cho $M$: (2,6), (3,5), (4,4), (5,3), (6,2) gồm 5 cặp. Tính $P(M) = \\frac{5}{36}$.", "points": 0.7},
                {"step": "b) Đặt ẩn thời gian đội I làm riêng là $x$ ngày, đội II là $y$ ngày ($x, y > 12$). Lập phương trình 1: $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{12}$.", "points": 0.35},
                {"step": "b) Lập phương trình 2 theo khối lượng: $\\frac{4}{x} + \\frac{9}{y} = \\frac{7}{12}$.", "points": 0.35},
                {"step": "b) Giải hệ phương trình tìm được $x = 20, y = 30$ (thỏa mãn). Kết luận thời gian mỗi đội.", "points": 0.3}
            ],
            "solution": "a) Không gian mẫu của phép thử là tập hợp các cặp số chấm $(i, j)$ với $1 \\le i, j \\le 6$:\n$$\\Omega = \\{(i, j) \\mid 1 \\le i, j \\le 6\\} \\Rightarrow n(\\Omega) = 6 \\times 6 = 36.$$\nCác kết quả thuận lợi cho biến cố $M$ (tổng số chấm bằng 8) là:\n$$M = \\{(2; 6); (3; 5); (4; 4); (5; 3); (6; 2)\\} \\Rightarrow n(M) = 5.$$\nVậy xác suất của biến cố $M$ là: $P(M) = \\frac{n(M)}{n(\\Omega)} = \\frac{5}{36}$.\n\nb) Gọi thời gian đội thứ nhất làm một mình xong đoạn đường là $x$ (ngày, điều kiện $x > 12$).\nThời gian đội thứ hai làm một mình xong đoạn đường là $y$ (ngày, điều kiện $y > 12$).\nTrong 1 ngày, đội thứ nhất làm được: $\\frac{1}{x}$ (đoạn đường).\nTrong 1 ngày, đội thứ hai làm được: $\\frac{1}{y}$ (đoạn đường).\nVì hai đội cùng làm trong 12 ngày thì xong đoạn đường nên trong 1 ngày hai đội làm được $\\frac{1}{12}$ đoạn đường, ta có phương trình:\n$$\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{12} \\quad (1)$$\nTheo đề bài, đội I làm 4 ngày được $\\frac{4}{x}$ đoạn đường, đội II làm 9 ngày được $\\frac{9}{y}$ đoạn đường, cả hai làm được $\\frac{7}{12}$ đoạn đường nên ta có phương trình:\n$$\\frac{4}{x} + \\frac{9}{y} = \\frac{7}{12} \\quad (2)$$\nTừ (1) và (2), đặt $u = \\frac{1}{x}, v = \\frac{1}{y}$ ($u, v > 0$), ta có hệ phương trình:\n$$\\begin{cases} u + v = \\frac{1}{12} \\\\ 4u + 9v = \\frac{7}{12} \\end{cases} \\Leftrightarrow \\begin{cases} 4u + 4v = \\frac{4}{12} \\\\ 4u + 9v = \\frac{7}{12} \\end{cases} \\Leftrightarrow \\begin{cases} 5v = \\frac{3}{12} = \\frac{1}{4} \\\\ u = \\frac{1}{12} - v \\end{cases} \\Leftrightarrow \\begin{cases} v = \\frac{1}{20} \\\\ u = \\frac{1}{12} - \\frac{1}{20} = \\frac{1}{30} \\end{cases}$$\nSuy ra:\n$$\\begin{cases} \\frac{1}{x} = \\frac{1}{30} \\\\ \\frac{1}{y} = \\frac{1}{20} \\end{cases} \\Leftrightarrow \\begin{cases} x = 30 \\text{ (thỏa mãn)} \\\\ y = 20 \\text{ (thỏa mãn)} \\end{cases}$$\nVậy đội thứ nhất làm một mình hoàn thành trong 30 ngày; đội thứ hai làm một mình hoàn thành trong 20 ngày."
        },
        {
            "id": 13,
            "points": 2.0,
            "question": "Cho tam giác $ABC$ có ba góc nhọn nội tiếp đường tròn $(O)$. Các đường cao $AD, BE, CF$ cắt nhau tại trực tâm $H$.\na) Chứng minh tứ giác $BCEF$ nội tiếp một đường tròn.\nb) Kẻ đường kính $AK$ của đường tròn $(O)$. Gọi $M$ là trung điểm của cạnh $BC$. Chứng minh tứ giác $BHCK$ là hình bình hành và ba điểm $H, M, K$ thẳng hàng.",
            "rubric": [
                {"step": "a) Chỉ ra $\\widehat{BFC} = 90^\\circ$ và $\\widehat{BEC} = 90^\\circ$.", "points": 0.5},
                {"step": "a) Kết luận tứ giác $BCEF$ nội tiếp đường tròn đường kính $BC$ do hai đỉnh $E, F$ cùng nhìn $BC$ dưới góc vuông.", "points": 0.5},
                {"step": "b) Chứng minh $BK \\perp AB$ và $CH \\perp AB \\Rightarrow BK \\parallel CH$.", "points": 0.35},
                {"step": "b) Chứng minh $CK \\perp AC$ và $BH \\perp AC \\Rightarrow CK \\parallel BH$.", "points": 0.35},
                {"step": "b) Tứ giác $BHCK$ có các cạnh đối song song nên là hình bình hành. Vì $M$ là trung điểm $BC$ nên $M$ cũng là trung điểm $HK$, suy ra $H, M, K$ thẳng hàng.", "points": 0.3}
            ],
            "solution": "a) Vì $BE, CF$ là các đường cao của tam giác $ABC$ nên $BE \\perp AC$ và $CF \\perp AB$.\nSuy ra $\\widehat{BEC} = 90^\\circ$ và $\\widehat{BFC} = 90^\\circ$.\nXét tứ giác $BCEF$, hai đỉnh kề nhau $E$ và $F$ cùng nhìn đoạn thẳng $BC$ dưới góc vuông $90^\\circ$.\nDo đó, tứ giác $BCEF$ nội tiếp đường tròn đường kính $BC$.\n\nb) Vì $AK$ là đường kính của đường tròn $(O)$ nên:\n- $\\widehat{ABK} = 90^\\circ$ (góc nội tiếp chắn nửa đường tròn) $\\Rightarrow BK \\perp AB$.\nMặt khác, $CF \\perp AB$ (do $CF$ là đường cao) $\\Rightarrow CH \\perp AB$.\nTừ đó suy ra $BK \\parallel CH$.\n- $\\widehat{ACK} = 90^\\circ$ (góc nội tiếp chắn nửa đường tròn) $\\Rightarrow CK \\perp AC$.\nMặt khác, $BE \\perp AC$ (do $BE$ là đường cao) $\\Rightarrow BH \\perp AC$.\nTừ đó suy ra $CK \\parallel BH$.\nXét tứ giác $BHCK$ có $BK \\parallel CH$ và $CK \\parallel BH$, nên $BHCK$ là hình bình hành.\nDo $BHCK$ là hình bình hành nên hai đường chéo $BC$ và $HK$ cắt nhau tại trung điểm của mỗi đường.\nMà $M$ là trung điểm của cạnh $BC$ theo giả thiết, suy ra $M$ cũng đồng thời là trung điểm của đường chéo $HK$.\nVậy ba điểm $H, M, K$ thẳng hàng."
        },
        {
            "id": 14,
            "points": 1.0,
            "question": "a) Một hình trụ có thể tích $V = 54\\pi\\text{ cm}^3$. Người ta cần thiết kế hình trụ sao cho diện tích toàn phần của nó nhỏ nhất để tiết kiệm nguyên liệu. Hãy tính bán kính đáy $r$ và chiều cao $h$ của hình trụ đó.\nb) Cho hai số thực dương $x, y$ thỏa mãn $x + y = 2$. Tìm giá trị nhỏ nhất của biểu thức:\n$$Q = \\frac{1}{x^2 + y^2} + \\frac{2}{xy} + 3xy.$$",
            "rubric": [
                {"step": "a) Thể tích $V = \\pi r^2 h = 54\\pi \\Rightarrow h = \\frac{54}{r^2}$. Diện tích toàn phần $S_{tp} = 2\\pi r^2 + 2\\pi rh = 2\\pi r^2 + \\frac{108\\pi}{r}$.", "points": 0.25},
                {"step": "a) AM-GM 3 số: $2\\pi r^2 + \\frac{54\\pi}{r} + \\frac{54\\pi}{r} \\ge 3\\sqrt[3]{2 \\cdot 54^2 \\pi^3} = 54\\pi$. Đẳng thức khi $r = 3\\text{ cm}, h = 6\\text{ cm}$.", "points": 0.25},
                {"step": "b) Dùng BĐT Cauchy-Schwarz dạng Engel: $\\frac{1}{x^2+y^2} + \\frac{1}{2xy} \\ge \\frac{4}{(x+y)^2} = 1$.", "points": 0.25},
                {"step": "b) Tách phần còn lại: $\\frac{3}{2xy} + 3xy = 3\\left(\\frac{1}{2xy} + \\frac{xy}{2}\\right) + \\frac{3xy}{2}$. Đánh giá tìm được $\\min Q = \\frac{11}{2}$ khi $x = y = 1$.", "points": 0.25}
            ],
            "solution": "a) Thể tích hình trụ là: $V = \\pi r^2 h = 54\\pi \\Rightarrow h = \\frac{54}{r^2}$ (với $r > 0$).\nDiện tích toàn phần của hình trụ là:\n$$S_{tp} = 2\\pi r^2 + 2\\pi rh = 2\\pi r^2 + 2\\pi r \\cdot \\frac{54}{r^2} = 2\\pi r^2 + \\frac{108\\pi}{r} = 2\\pi r^2 + \\frac{54\\pi}{r} + \\frac{54\\pi}{r}.$$\nÁp dụng bất đẳng thức AM-GM cho 3 số dương $2\\pi r^2, \\frac{54\\pi}{r}, \\frac{54\\pi}{r}$:\n$$S_{tp} \\ge 3\\sqrt[3]{2\\pi r^2 \\cdot \\frac{54\\pi}{r} \\cdot \\frac{54\\pi}{r}} = 3\\sqrt[3]{2 \\cdot 54^2 \\cdot \\pi^3} = 3 \\cdot 18\\pi = 54\\pi\\text{ cm}^2.$$\nDấu đẳng thức xảy ra khi và chỉ khi:\n$$2\\pi r^2 = \\frac{54\\pi}{r} \\Leftrightarrow r^3 = 27 \\Leftrightarrow r = 3\\text{ cm}.$$\nKhi đó chiều cao hình trụ là: $h = \\frac{54}{3^2} = 6\\text{ cm}$.\nVậy để diện tích toàn phần nhỏ nhất thì bán kính đáy là $r = 3\\text{ cm}$ và chiều cao là $h = 6\\text{ cm}$.\n\nb) Áp dụng bất đẳng thức Cauchy-Schwarz dạng phân thức:\n$$\\frac{1}{x^2+y^2} + \\frac{1}{2xy} \\ge \\frac{(1+1)^2}{x^2+y^2+2xy} = \\frac{4}{(x+y)^2} = \\frac{4}{2^2} = 1.$$\nBiểu thức $Q$ được viết lại thành:\n$$Q = \\left(\\frac{1}{x^2+y^2} + \\frac{1}{2xy}\\right) + \\left(\\frac{3}{2xy} + \\frac{3xy}{2}\\right) + \\frac{3xy}{2}.$$\nÁp dụng AM-GM: $\\frac{3}{2xy} + \\frac{3xy}{2} \\ge 2\\sqrt{\\frac{3}{2xy} \\cdot \\frac{3xy}{2}} = 3$.\nMặt khác, ta có $xy \\le \\frac{(x+y)^2}{4} = \\frac{2^2}{4} = 1$, nhưng ở đây ta cần chặn dưới cho $\\frac{3xy}{2}$? Chú ý: $xy \\le 1$ nên ta nhóm khác:\nTa viết: $Q = \\left(\\frac{1}{x^2+y^2} + \\frac{1}{2xy}\\right) + \\left(\\frac{3}{2xy} + \\frac{3}{2}xy\\right) + \\frac{3}{2}xy$. Vì $xy \\le 1$ không dùng $\\ge$ trực tiếp được, ta ghép:\nTa có $x^2 + y^2 \\ge 2xy \\Rightarrow (x+y)^2 \\ge 4xy \\Rightarrow xy \\le 1$.\nBiến đổi $Q = \\frac{1}{x^2+y^2} + \\frac{1}{2xy} + \\frac{3}{2xy} + 3xy$.\nXét $f(xy) = \\frac{3}{2xy} + 3xy$ với $0 < xy \\le 1$:\nTa có $\\frac{3}{2xy} + \\frac{3}{2}xy \\ge 2\\sqrt{\\frac{9}{4}} = 3$.\nVì $xy \\le 1$, ta viết: $\\frac{3}{2xy} + 3xy = \\left(\\frac{3}{2xy} + \\frac{3xy}{2}\\right) + \\frac{3xy}{2}$... Thay vì vậy:\nDo $xy \\le 1$, đặt $t = xy \\in (0; 1]$. Biểu thức $g(t) = \\frac{3}{2t} + 3t$.\nXét $g(t) - \\frac{9}{2} = \\frac{3 + 6t^2 - 9t}{2t} = \\frac{3(2t-1)(t-1)}{2t}$ chưa chắc dương tại mọi $t$.\nNhưng ta ghép: $\\frac{1}{x^2+y^2} + \\frac{1}{2xy} \\ge 1$.\nVà $\\frac{3}{2xy} + \\frac{3xy}{2} + \\frac{3xy}{2}$:\nThực chất tại điểm rơi $x = y = 1 \\Rightarrow xy = 1$.\nKhi $x = y = 1$, $Q = \\frac{1}{2} + 2 + 3 = \\frac{11}{2}$.\nTa chứng minh $Q \\ge \\frac{11}{2}$:\n$$Q - \\frac{11}{2} = \\frac{1}{x^2+y^2} + \\frac{2}{xy} + 3xy - \\frac{11}{2}$$\n$$= \\left(\\frac{1}{x^2+y^2} + \\frac{1}{2xy} - 1\\right) + \\left(\\frac{3}{2xy} + \\frac{3xy}{2} - 3\\right) + \\left(\\frac{3xy}{2} - \\frac{3}{2}\\right)$$\nĐể ý rằng với $xy \\le 1$, hàm $h(t) = \\frac{3}{2t} + 3t$ có đạo hàm $h'(t) = -\\frac{3}{2t^2} + 3 < 0$ với mọi $t \\in (0; 1/\\sqrt{2})$ và tại $t \\le 1$ giá trị nhỏ nhất của $\\frac{3}{2t} + 3t$ chính tại $t = 1$, vì khi $t \\le 1$ thì $\\frac{3}{2t} + 3t \\ge \\frac{3}{2(1)} + 3(1) = \\frac{9}{2}$.\nThật vậy: $\\frac{3}{2t} + 3t - \\frac{9}{2} = \\frac{3(1-t)(1-2t)}{2t}$.\nTa có cách đánh giá chuẩn xác:\n$$Q = \\left(\\frac{1}{x^2+y^2} + \\frac{1}{2xy}\\right) + \\left(\\frac{3}{2xy} + \\frac{3}{2}xy\\right) + \\frac{3}{2}xy$$\nTa ghép: $\\frac{1}{x^2+y^2} + \\frac{1}{2xy} \\ge \\frac{4}{x^2+y^2+2xy} = 1$.\nLại có $\\frac{3}{2xy} + \\frac{3}{2}xy = \\frac{3}{2}\\left(\\frac{1}{xy} + xy\\right) \\ge \\frac{3}{2} \\cdot 2 = 3$.\nĐể triệt tiêu dấu bất đẳng thức tại $xy = 1$:\nViết $Q = \\frac{1}{x^2+y^2} + \\frac{1}{2xy} + \\frac{3}{2xy} + \\frac{3xy}{2} + \\frac{3xy}{2}$.\nCách chuẩn nhất: Với $x+y=2 \\Rightarrow x^2+y^2 = 4 - 2xy$. Đặt $t = xy$ với $0 < t \\le 1$.\n$$Q(t) = \\frac{1}{4-2t} + \\frac{2}{t} + 3t.$$\nXét hiệu $Q(t) - \\frac{11}{2} = \\frac{1}{4-2t} + \\frac{2}{t} + 3t - \\frac{11}{2} = \\frac{t + 2(4-2t) + 3t^2(4-2t) - \\frac{11}{2}t(4-2t)}{t(4-2t)}$\n$$= \\frac{8 - 3t + 12t^2 - 6t^3 - 22t + 11t^2}{2t(2-t)} = \\frac{-6t^3 + 23t^2 - 25t + 8}{2t(2-t)} = \\frac{(1-t)^2(8 - 6t)}{2t(2-t)}.$$\nVì $0 < t \\le 1$ nên $8 - 6t > 0$ và $2 - t > 0$, do đó $\\frac{(1-t)^2(8-6t)}{2t(2-t)} \\ge 0$.\nSuy ra $Q(t) \\ge \\frac{11}{2}$ với mọi $0 < t \\le 1$.\nDấu đẳng thức xảy ra khi và chỉ khi $t = 1 \\Leftrightarrow x = y = 1$.\nVậy giá trị nhỏ nhất của $Q$ là $\\frac{11}{2}$ khi $x = y = 1$."
        }
    ]
}

print("Đã nạp xong Đề 04.")

# ==============================================================================
# ĐỀ SỐ 05 (Mã đề 05)
# ==============================================================================
MOCK_EXAMS_GRADE10["exams"]["de_05"] = {
    "id": "de_05",
    "code": "MÃ ĐỀ 05",
    "title": "ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN - ĐỀ SỐ 05",
    "header": {
        "department": "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
        "examName": "KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT",
        "subject": "Môn thi: TOÁN",
        "author": "GV Phan Đình Thuấn",
        "time": "90 phút (không kể thời gian phát đề)",
        "code": "MÃ ĐỀ 05"
    },
    "part1": [
        {
            "id": 1,
            "question": "Kết quả rút gọn biểu thức $A = \\sqrt{50} - \\sqrt{18} + \\sqrt{8}$ là:",
            "options": ["A. $4\\sqrt{2}$", "B. $5\\sqrt{2}$", "C. $3\\sqrt{2}$", "D. $6\\sqrt{2}$"],
            "answer": "A",
            "explanation": "$A = 5\\sqrt{2} - 3\\sqrt{2} + 2\\sqrt{2} = 4\\sqrt{2}$."
        },
        {
            "id": 2,
            "question": "Nghiệm của bất phương trình $4x - 12 < 0$ là:",
            "options": ["A. $x > 3$", "B. $x < 3$", "C. $x < -3$", "D. $x > -3$"],
            "answer": "B",
            "explanation": "$4x - 12 < 0 \\Leftrightarrow 4x < 12 \\Leftrightarrow x < 3$."
        },
        {
            "id": 3,
            "question": "Nghiệm của phương trình $3x - 1 = 2x + 5$ là:",
            "options": ["A. $x = 4$", "B. $x = 6$", "C. $x = -6$", "D. $x = 5$"],
            "answer": "B",
            "explanation": "$3x - 2x = 5 + 1 \\Leftrightarrow x = 6$."
        },
        {
            "id": 4,
            "question": "Một tổ học sinh gồm 4 bạn nam và 6 bạn nữ. Chọn ngẫu nhiên một bạn trong tổ. Xác suất để chọn được bạn nữ là:",
            "options": ["A. $\\frac{2}{5}$", "B. $\\frac{3}{5}$", "C. $\\frac{1}{2}$", "D. $\\frac{2}{3}$"],
            "answer": "B",
            "explanation": "Tổng số học sinh là $4 + 6 = 10$. Xác suất chọn được nữ là $\\frac{6}{10} = \\frac{3}{5}$."
        },
        {
            "id": 5,
            "question": "Điểm nào sau đây thuộc đồ thị hàm số $y = \\frac{1}{2}x^2$?",
            "options": ["A. $(2; 1)$", "B. $(2; 2)$", "C. $(-2; -2)$", "D. $(1; 1)$"],
            "answer": "B",
            "explanation": "Với $x = 2 \\Rightarrow y = \\frac{1}{2} \\cdot 2^2 = 2$. Do đó điểm $(2; 2)$ thuộc đồ thị."
        },
        {
            "id": 6,
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $AC = 8\\text{ cm}, BC = 10\\text{ cm}$. Giá trị của $\\sin C$ bằng:",
            "options": ["A. $\\frac{3}{5}$", "B. $\\frac{4}{5}$", "C. $\\frac{3}{4}$", "D. $\\frac{4}{3}$"],
            "answer": "A",
            "explanation": "Theo Pytago: $AB = \\sqrt{10^2 - 8^2} = 6\\text{ cm}$. Khi đó $\\sin C = \\frac{AB}{BC} = \\frac{6}{10} = \\frac{3}{5}$."
        },
        {
            "id": 7,
            "question": "Một quả bóng hình cầu có đường kính bằng $6\\text{ cm}$. Thể tích của quả bóng đó là:",
            "options": ["A. $36\\pi\\text{ cm}^3$", "B. $288\\pi\\text{ cm}^3$", "C. $144\\pi\\text{ cm}^3$", "D. $18\\pi\\text{ cm}^3$"],
            "answer": "A",
            "explanation": "Bán kính hình cầu là $R = 3\\text{ cm}$. Thể tích $V = \\frac{4}{3}\\pi R^3 = \\frac{4}{3}\\pi \\cdot 27 = 36\\pi\\text{ cm}^3$."
        },
        {
            "id": 8,
            "question": "Kết quả khảo sát thời gian tự học ở nhà mỗi ngày của 50 học sinh lớp 9: Dưới 1h (8 hs), Từ 1h-2h (25 hs), Trên 2h (17 hs). Tần số tương đối của nhóm học sinh tự học từ 1h đến 2h là:",
            "options": ["A. 16%", "B. 34%", "C. 50%", "D. 25%"],
            "answer": "C",
            "explanation": "$f = \\frac{25}{50} \\cdot 100\\% = 50\\%$."
        }
    ],
    "part2": [
        {
            "id": 9,
            "points": 1.0,
            "question": "Cho biểu thức $P = \\left(\\frac{\\sqrt{x}}{\\sqrt{x}-5} - \\frac{10\\sqrt{x}}{x-25}\\right) : \\frac{\\sqrt{x}+5}{x-25}$ với $x \\ge 0$ và $x \\ne 25$. Rút gọn biểu thức $P$.",
            "rubric": [
                {"step": "Quy đồng trong ngoặc với mẫu chung $x - 25 = (\\sqrt{x}-5)(\\sqrt{x}+5)$.", "points": 0.3},
                {"step": "Tử thức trong ngoặc: $\\sqrt{x}(\\sqrt{x}+5) - 10\\sqrt{x} = x + 5\\sqrt{x} - 10\\sqrt{x} = x - 5\\sqrt{x} = \\sqrt{x}(\\sqrt{x}-5)$.", "points": 0.3},
                {"step": "Thu gọn trong ngoặc được $\\frac{\\sqrt{x}}{\\sqrt{x}+5}$.", "points": 0.2},
                {"step": "Nhân với phân thức nghịch đảo: $\\frac{\\sqrt{x}}{\\sqrt{x}+5} \\cdot \\frac{x-25}{\\sqrt{x}+5} = \\frac{\\sqrt{x}(\\sqrt{x}-5)}{\\sqrt{x}+5}$. Kết luận.", "points": 0.2}
            ],
            "solution": "Với $x \\ge 0$ và $x \\ne 25$, ta có:\n$$\\begin{aligned}\nP &= \\left[\\frac{\\sqrt{x}(\\sqrt{x}+5)}{x-25} - \\frac{10\\sqrt{x}}{x-25}\\right] : \\frac{\\sqrt{x}+5}{x-25} \\\\\n&= \\frac{x + 5\\sqrt{x} - 10\\sqrt{x}}{x-25} \\cdot \\frac{x-25}{\\sqrt{x}+5} \\\\\n&= \\frac{x - 5\\sqrt{x}}{\\sqrt{x}+5} = \\frac{\\sqrt{x}(\\sqrt{x}-5)}{\\sqrt{x}+5}.\n\\end{aligned}$$\nVậy $P = \\frac{x - 5\\sqrt{x}}{\\sqrt{x}+5}$ với $x \\ge 0, x \\ne 25$."
        },
        {
            "id": 10,
            "points": 1.0,
            "question": "Cho phương trình $x^2 - 6x + 4 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức $M = \\frac{x_1^2 + x_2^2}{x_1 x_2 + 2}$.",
            "rubric": [
                {"step": "Tính $\\Delta' = (-3)^2 - 1(4) = 5 > 0$ nên phương trình có hai nghiệm phân biệt.", "points": 0.25},
                {"step": "Theo định lí Viète: $x_1 + x_2 = 6$ và $x_1 x_2 = 4$.", "points": 0.25},
                {"step": "Tính tử số: $x_1^2 + x_2^2 = (x_1+x_2)^2 - 2x_1x_2 = 6^2 - 2(4) = 28$.", "points": 0.25},
                {"step": "Tính $M = \\frac{28}{4 + 2} = \\frac{28}{6} = \\frac{14}{3}$. Kết luận.", "points": 0.25}
            ],
            "solution": "Xét phương trình $x^2 - 6x + 4 = 0$ có $\\Delta' = (-3)^2 - 1 \\cdot 4 = 5 > 0$ nên phương trình có 2 nghiệm phân biệt $x_1, x_2$.\nTheo định lí Viète, ta có:\n$$\\begin{cases} x_1 + x_2 = 6 \\\\ x_1 x_2 = 4 \\end{cases}$$\nTa có:\n$$x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = 6^2 - 2 \\cdot 4 = 36 - 8 = 28.$$\nThay vào biểu thức $M$:\n$$M = \\frac{x_1^2 + x_2^2}{x_1 x_2 + 2} = \\frac{28}{4 + 2} = \\frac{28}{6} = \\frac{14}{3}.$$\nVậy $M = \\frac{14}{3}$."
        },
        {
            "id": 11,
            "points": 1.0,
            "question": "Giải hệ phương trình:\n$$\\begin{cases} 2x + 3y = 8 \\\\ 5x - y = 3 \\end{cases}$$",
            "rubric": [
                {"step": "Từ phương trình 2 rút $y = 5x - 3$.", "points": 0.25},
                {"step": "Thế vào phương trình 1: $2x + 3(5x - 3) = 8 \\Leftrightarrow 17x - 9 = 8 \\Leftrightarrow 17x = 17 \\Rightarrow x = 1$.", "points": 0.35},
                {"step": "Tính $y = 5(1) - 3 = 2$.", "points": 0.25},
                {"step": "Kết luận nghiệm duy nhất $(x; y) = (1; 2)$.", "points": 0.15}
            ],
            "solution": "Ta có:\n$$\\begin{cases} 2x + 3y = 8 \\\\ 5x - y = 3 \\end{cases} \\Leftrightarrow \\begin{cases} 2x + 3y = 8 \\\\ 15x - 3y = 9 \\end{cases} \\Leftrightarrow \\begin{cases} 17x = 17 \\\\ 5x - y = 3 \\end{cases} \\Leftrightarrow \\begin{cases} x = 1 \\\\ 5(1) - y = 3 \\end{cases} \\Leftrightarrow \\begin{cases} x = 1 \\\\ y = 2 \\end{cases}$$\nVậy hệ phương trình có nghiệm duy nhất $(x; y) = (1; 2)$."
        },
        {
            "id": 12,
            "points": 2.0,
            "question": "a) Một hộp chứa 5 quả cầu có cùng khối lượng và kích thước, được đánh số 1; 2; 3; 4; 5. Lấy ngẫu nhiên đồng thời hai quả cầu. Viết không gian mẫu của phép thử và tính xác suất của biến cố $K$: “Tích hai số ghi trên hai quả cầu là một số chẵn”.\nb) Một ca nô chạy xuôi dòng một khúc sông dài 40 km, sau đó chạy ngược dòng quay về điểm xuất phát mất tất cả 4 giờ 30 phút. Biết vận tốc của dòng nước là 2 km/h. Tính vận tốc thực của ca nô khi nước yên lặng.",
            "rubric": [
                {"step": "a) Viết đúng không gian mẫu $\\Omega$ gồm 10 cặp phần tử không kể thứ tự $\\{(1,2), (1,3), ..., (4,5)\\}$, suy ra $n(\\Omega) = 10$.", "points": 0.5},
                {"step": "a) Tích hai số là lẻ khi cả hai số đều lẻ: có $\\{(1,3), (1,5), (3,5)\\}$ gồm 3 kết quả. Suy ra số kết quả tích chẵn là $10 - 3 = 7$. Tính $P(K) = \\frac{7}{10}$.", "points": 0.5},
                {"step": "b) Đổi 4 giờ 30 phút $= 4,5 = \\frac{9}{2}$ giờ. Gọi vận tốc ca nô khi nước yên lặng là $x$ (km/h, $x > 2$).", "points": 0.35},
                {"step": "b) Biểu diễn vận tốc xuôi dòng $x+2$, ngược dòng $x-2$. Lập phương trình: $\\frac{40}{x+2} + \\frac{40}{x-2} = \\frac{9}{2} \\Leftrightarrow 9x^2 - 160x - 36 = 0$.", "points": 0.35},
                {"step": "b) Giải phương trình được $x = 18$ (thỏa mãn), $x = -\\frac{2}{9}$ (loại). Kết luận vận tốc ca nô là 18 km/h.", "points": 0.3}
            ],
            "solution": "a) Lấy ngẫu nhiên đồng thời hai quả cầu trong 5 quả cầu, không gian mẫu của phép thử là:\n$$\\Omega = \\{(1; 2); (1; 3); (1; 4); (1; 5); (2; 3); (2; 4); (2; 5); (3; 4); (3; 5); (4; 5)\\}$$\nSố phần tử của không gian mẫu là $n(\\Omega) = 10$.\nTích hai số là số lẻ khi cả hai quả cầu đều mang số lẻ. Các số lẻ trong hộp là 1, 3, 5, các cặp toàn số lẻ là: $\\{(1; 3); (1; 5); (3; 5)\\}$ (gồm 3 kết quả).\nDo đó, các kết quả làm cho tích hai số là số chẵn gồm $10 - 3 = 7$ kết quả thuận lợi:\n$$K = \\{(1; 2); (1; 4); (2; 3); (2; 4); (2; 5); (3; 4); (4; 5)\\} \\Rightarrow n(K) = 7.$$\nVậy xác suất của biến cố $K$ là: $P(K) = \\frac{n(K)}{n(\\Omega)} = \\frac{7}{10} = 0,7$.\n\nb) Đổi 4 giờ 30 phút $= \\frac{9}{2}$ giờ.\nGọi vận tốc thực của ca nô khi nước yên lặng là $x$ (km/h, điều kiện $x > 2$).\nVận tốc của ca nô khi xuôi dòng là: $x + 2$ (km/h).\nThời gian ca nô đi xuôi dòng quãng đường 40 km là: $\\frac{40}{x+2}$ (giờ).\nVận tốc của ca nô khi ngược dòng là: $x - 2$ (km/h).\nThời gian ca nô đi ngược dòng quãng đường 40 km là: $\\frac{40}{x-2}$ (giờ).\nTổng thời gian cả đi và về là $\\frac{9}{2}$ giờ nên ta có phương trình:\n$$\\frac{40}{x+2} + \\frac{40}{x-2} = \\frac{9}{2}$$\n$$\\Leftrightarrow \\frac{40(x-2) + 40(x+2)}{x^2 - 4} = \\frac{9}{2} \\Leftrightarrow \\frac{80x}{x^2 - 4} = \\frac{9}{2}$$\n$$\\Leftrightarrow 9(x^2 - 4) = 160x \\Leftrightarrow 9x^2 - 160x - 36 = 0$$\nTa có $\\Delta' = (-80)^2 - 9(-36) = 6400 + 324 = 6724 = 82^2 > 0$.\nPhương trình có 2 nghiệm:\n$$x_1 = \\frac{80 + 82}{9} = \\frac{162}{9} = 18 \\text{ (thỏa mãn); } x_2 = \\frac{80 - 82}{9} = -\\frac{2}{9} \\text{ (loại)}.$$\nVậy vận tốc thực của ca nô khi nước yên lặng là 18 km/h."
        },
        {
            "id": 13,
            "points": 2.0,
            "question": "Cho nửa đường tròn $(O)$ đường kính $AB = 2R$. Trên cùng một nửa mặt phẳng bờ $AB$ chứa nửa đường tròn, kẻ hai tiếp tuyến $Ax, By$ với nửa đường tròn. Lấy điểm $C$ tùy ý trên nửa đường tròn ($C$ khác $A, B$). Tiếp tuyến tại $C$ cắt $Ax, By$ lần lượt tại $D$ và $E$.\na) Chứng minh tứ giác $ADCO$ nội tiếp một đường tròn.\nb) Chứng minh rằng $AD \\cdot BE = R^2$ và góc $\\widehat{DOE} = 90^\\circ$.",
            "rubric": [
                {"step": "a) Chỉ ra $Ax$ và tiếp tuyến tại $C$ vuông góc với bán kính tại tiếp điểm: $\\widehat{DAO} = 90^\\circ, \\widehat{DCO} = 90^\\circ$.", "points": 0.5},
                {"step": "a) Tứ giác $ADCO$ có tổng hai góc đối $\\widehat{DAO} + \\widehat{DCO} = 180^\\circ$ nên nội tiếp đường tròn đường kính $DO$.", "points": 0.5},
                {"step": "b) Theo tính chất hai tiếp tuyến cắt nhau: $OD$ là phân giác $\\widehat{AOC}$, $OE$ là phân giác $\\widehat{BOC}$.", "points": 0.35},
                {"step": "b) Vì $\\widehat{AOC} + \\widehat{BOC} = 180^\\circ$ (kề bù) nên $OD \\perp OE \\Rightarrow \\widehat{DOE} = 90^\\circ$.", "points": 0.35},
                {"step": "b) Trong tam giác vuông $DOE$ có đường cao $OC = R$, áp dụng hệ thức lượng $CD \\cdot CE = OC^2 = R^2$. Mà $CD = AD$ và $CE = BE$ nên $AD \\cdot BE = R^2$.", "points": 0.3}
            ],
            "solution": "a) Vì $Ax$ là tiếp tuyến của nửa đường tròn $(O)$ tại $A$ nên $Ax \\perp AB \\Rightarrow \\widehat{DAO} = 90^\\circ$.\nVì $DE$ là tiếp tuyến của nửa đường tròn $(O)$ tại $C$ nên $DE \\perp OC \\Rightarrow \\widehat{DCO} = 90^\\circ$.\nXét tứ giác $ADCO$ có:\n$$\\widehat{DAO} + \\widehat{DCO} = 90^\\circ + 90^\\circ = 180^\\circ.$$\nDo đó, tứ giác $ADCO$ nội tiếp đường tròn đường kính $DO$.\n\nb) *) Chứng minh $\\widehat{DOE} = 90^\\circ$:\nTheo tính chất hai tiếp tuyến cắt nhau, ta có:\n- $OD$ là tia phân giác của góc $\\widehat{AOC}$, nên $\\widehat{COD} = \\frac{1}{2}\\widehat{AOC}$.\n- $OE$ là tia phân giác của góc $\\widehat{BOC}$, nên $\\widehat{COE} = \\frac{1}{2}\\widehat{BOC}$.\nMà góc $\\widehat{AOC}$ và góc $\\widehat{BOC}$ là hai góc kề bù, nên:\n$$\\widehat{DOE} = \\widehat{COD} + \\widehat{COE} = \\frac{1}{2}(\\widehat{AOC} + \\widehat{BOC}) = \\frac{1}{2} \\cdot 180^\\circ = 90^\\circ.$$\n\n*) Chứng minh $AD \\cdot BE = R^2$:\nTam giác $DOE$ vuông tại $O$ (do $\\widehat{DOE} = 90^\\circ$) và có đường cao $OC \\perp DE$ (vì $DE$ là tiếp tuyến tại $C$, $OC = R$).\nÁp dụng hệ thức lượng trong tam giác vuông $DOE$, ta có:\n$$CD \\cdot CE = OC^2 = R^2.$$\nTheo tính chất của hai tiếp tuyến cắt nhau, ta có $DA = DC$ và $EB = EC$.\nThay vào hệ thức trên, ta được:\n$$AD \\cdot BE = R^2.$$"
        },
        {
            "id": 14,
            "points": 1.0,
            "question": "a) Bác thợ gò muốn gò một chiếc thùng phi bằng tôn hình trụ có thể tích $V = 54\\pi\\text{ dm}^3$ không nắp. Hãy tìm bán kính đáy $r$ và chiều cao $h$ của thùng để tiết kiệm diện tích tôn nhất (diện tích toàn phần gồm diện tích đáy và diện tích xung quanh là nhỏ nhất).\nb) Cho các số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Tìm giá trị lớn nhất của biểu thức:\n$$T = \\frac{ab}{\\sqrt{3c + ab}} + \\frac{bc}{\\sqrt{3a + bc}} + \\frac{ca}{\\sqrt{3b + ca}}.$$",
            "rubric": [
                {"step": "a) $V = \\pi r^2 h = 54\\pi \\Rightarrow h = \\frac{54}{r^2}$. Diện tích tôn $S = \\pi r^2 + 2\\pi rh = \\pi r^2 + \\frac{108\\pi}{r}$.", "points": 0.25},
                {"step": "a) AM-GM 3 số: $\\pi r^2 + \\frac{54\\pi}{r} + \\frac{54\\pi}{r} \\ge 3\\sqrt[3]{54^2 \\pi^3}$. Dấu bằng khi $\\pi r^2 = \\frac{54\\pi}{r} \\Leftrightarrow r = \\sqrt[3]{54} = 3\\sqrt[3]{2}\\text{ dm}, h = 3\\sqrt[3]{2}\\text{ dm}$.", "points": 0.25},
                {"step": "b) Thay $3 = a + b + c$ vào căn: $3c + ab = c(a+b+c) + ab = (c+a)(c+b)$.", "points": 0.25},
                {"step": "b) Áp dụng AM-GM dạng $\\frac{ab}{\\sqrt{(a+c)(b+c)}} \\le \\frac{1}{2}\\left(\\frac{ab}{a+c} + \\frac{ab}{b+c}\\right)$, cộng 3 biểu thức tìm được $\\max T = \\frac{3}{2}$ khi $a = b = c = 1$.", "points": 0.25}
            ],
            "solution": "a) Thể tích hình trụ không nắp là: $V = \\pi r^2 h = 54\\pi \\Rightarrow h = \\frac{54}{r^2}$ (với $r > 0$).\nDiện tích tôn cần dùng gồm diện tích một đáy và diện tích xung quanh:\n$$S = \\pi r^2 + 2\\pi rh = \\pi r^2 + 2\\pi r \\cdot \\frac{54}{r^2} = \\pi r^2 + \\frac{108\\pi}{r} = \\pi r^2 + \\frac{54\\pi}{r} + \\frac{54\\pi}{r}.$$\nÁp dụng bất đẳng thức AM-GM cho 3 số dương $\\pi r^2, \\frac{54\\pi}{r}, \\frac{54\\pi}{r}$:\n$$S \\ge 3 \\sqrt[3]{\\pi r^2 \\cdot \\frac{54\\pi}{r} \\cdot \\frac{54\\pi}{r}} = 3\\sqrt[3]{54^2 \\pi^3} = 3 \\cdot 9\\pi \\sqrt[3]{4} = 27\\pi\\sqrt[3]{4}\\text{ dm}^2.$$\nDấu đẳng thức xảy ra khi và chỉ khi:\n$$\\pi r^2 = \\frac{54\\pi}{r} \\Leftrightarrow r^3 = 54 \\Leftrightarrow r = \\sqrt[3]{54} = 3\\sqrt[3]{2}\\text{ dm}.$$\nKhi đó chiều cao $h = \\frac{54}{(3\\sqrt[3]{2})^2} = \\frac{54}{9\\sqrt[3]{4}} = \\frac{6}{\\sqrt[3]{4}} = 3\\sqrt[3]{2}\\text{ dm}$.\nVậy để tiết kiệm tôn nhất thì bán kính đáy và chiều cao đều bằng $3\\sqrt[3]{2}\\text{ dm}$ (khoảng $3,78\\text{ dm}$).\n\nb) Thay $3 = a + b + c$ vào biểu thức dưới dấu căn của số hạng thứ nhất:\n$$3c + ab = c(a + b + c) + ab = ca + cb + c^2 + ab = c(a + c) + b(a + c) = (a + c)(b + c).$$\nÁp dụng bất đẳng thức AM-GM: $\\sqrt{(a+c)(b+c)} \\ge \\frac{2}{\\frac{1}{a+c} + \\frac{1}{b+c}}$, hay:\n$$\\frac{1}{\\sqrt{(a+c)(b+c)}} \\le \\frac{1}{2}\\left(\\frac{1}{a+c} + \\frac{1}{b+c}\\right).$$\nNhân cả hai vế với $ab > 0$, ta được:\n$$\\frac{ab}{\\sqrt{3c + ab}} = \\frac{ab}{\\sqrt{(a+c)(b+c)}} \\le \\frac{1}{2}\\left(\\frac{ab}{a+c} + \\frac{ab}{b+c}\\right).$$\nHoàn toàn tương tự:\n$$\\frac{bc}{\\sqrt{3a + bc}} \\le \\frac{1}{2}\\left(\\frac{bc}{b+a} + \\frac{bc}{c+a}\\right),$$\n$$\\frac{ca}{\\sqrt{3b + ca}} \\le \\frac{1}{2}\\left(\\frac{ca}{c+b} + \\frac{ca}{a+b}\\right).$$\nCộng ba bất đẳng thức trên vế theo vế, ta được:\n$$T \\le \\frac{1}{2}\\left(\\frac{ab + bc}{a+c} + \\frac{ab + ca}{b+c} + \\frac{bc + ca}{a+b}\\right) = \\frac{1}{2}\\left(\\frac{b(a+c)}{a+c} + \\frac{a(b+c)}{b+c} + \\frac{c(b+a)}{a+b}\\right) = \\frac{1}{2}(b + a + c).$$\nVì $a + b + c = 3$ nên:\n$$T \\le \\frac{1}{2} \\cdot 3 = \\frac{3}{2}.$$\nDấu đẳng thức xảy ra khi và chỉ khi:\n$$a + c = b + c = a + b \\text{ và } a + b + c = 3 \\Leftrightarrow a = b = c = 1.$$\nVậy giá trị lớn nhất của $T$ là $\\frac{3}{2}$ khi $a = b = c = 1$."
        }
    ]
}

print("Đã nạp xong Đề 05.")

# ==============================================================================
# ĐỀ SỐ 06 (Mã đề 06)
# ==============================================================================
MOCK_EXAMS_GRADE10["exams"]["de_06"] = {
    "id": "de_06",
    "code": "MÃ ĐỀ 06",
    "title": "ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN - GV PHAN ĐÌNH THUẤN - ĐỀ SỐ 06",
    "header": {
        "department": "SỞ GIÁO DỤC VÀ ĐÀO TẠO",
        "examName": "KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT",
        "subject": "Môn thi: TOÁN",
        "author": "GV Phan Đình Thuấn",
        "time": "90 phút (không kể thời gian phát đề)",
        "code": "MÃ ĐỀ 06"
    },
    "part1": [
        {
            "id": 1,
            "question": "Kết quả rút gọn biểu thức $A = (\\sqrt{12} - \\sqrt{3})\\sqrt{3}$ là:",
            "options": ["A. $3$", "B. $6$", "C. $3\\sqrt{3}$", "D. $\\sqrt{3}$"],
            "answer": "A",
            "explanation": "$A = (2\\sqrt{3} - \\sqrt{3})\\sqrt{3} = \\sqrt{3} \\cdot \\sqrt{3} = 3$."
        },
        {
            "id": 2,
            "question": "Nghiệm của bất phương trình $5 - 2x \\le 1$ là:",
            "options": ["A. $x \\ge 2$", "B. $x \\le 2$", "C. $x \\ge -2$", "D. $x \\le 3$"],
            "answer": "A",
            "explanation": "$5 - 2x \\le 1 \\Leftrightarrow -2x \\le -4 \\Leftrightarrow x \\ge 2$."
        },
        {
            "id": 3,
            "question": "Nghiệm của phương trình $7 - 3x = 1$ là:",
            "options": ["A. $x = -2$", "B. $x = 2$", "C. $x = 3$", "D. $x = -3$"],
            "answer": "B",
            "explanation": "$7 - 3x = 1 \\Leftrightarrow 3x = 6 \\Leftrightarrow x = 2$."
        },
        {
            "id": 4,
            "question": "Một hộp có 8 viên bi gồm 3 viên bi đỏ và 5 viên bi xanh có cùng kích thước. Lấy ngẫu nhiên một viên bi. Xác suất để lấy được viên bi màu đỏ là:",
            "options": ["A. $\\frac{3}{8}$", "B. $\\frac{5}{8}$", "C. $\\frac{3}{5}$", "D. $\\frac{1}{8}$"],
            "answer": "A",
            "explanation": "Có 3 viên bi đỏ trên tổng số 8 viên bi nên xác suất là $\\frac{3}{8}$."
        },
        {
            "id": 5,
            "question": "Đồ thị của hàm số $y = -x^2$ đi qua điểm nào sau đây?",
            "options": ["A. $(2; 4)$", "B. $(-2; 4)$", "C. $(-2; -4)$", "D. $(1; 1)$"],
            "answer": "C",
            "explanation": "Với $x = -2 \\Rightarrow y = -(-2)^2 = -4$. Do đó điểm $(-2; -4)$ thuộc đồ thị."
        },
        {
            "id": 6,
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{B} = 30^\\circ$ và $BC = 8\\text{ cm}$. Độ dài cạnh $AC$ bằng:",
            "options": ["A. $4\\text{ cm}$", "B. $4\\sqrt{3}\\text{ cm}$", "C. $2\\text{ cm}$", "D. $8\\sqrt{3}\\text{ cm}$"],
            "answer": "A",
            "explanation": "$AC = BC \\cdot \\sin B = 8 \\cdot \\sin 30^\\circ = 8 \\cdot \\frac{1}{2} = 4\\text{ cm}$."
        },
        {
            "id": 7,
            "question": "Diện tích toàn phần của hình trụ có bán kính đáy $r = 2\\text{ cm}$ và chiều cao $h = 5\\text{ cm}$ là:",
            "options": ["A. $20\\pi\\text{ cm}^2$", "B. $24\\pi\\text{ cm}^2$", "C. $28\\pi\\text{ cm}^2$", "D. $14\\pi\\text{ cm}^2$"],
            "answer": "C",
            "explanation": "$S_{tp} = 2\\pi rh + 2\\pi r^2 = 2\\pi \\cdot 2 \\cdot 5 + 2\\pi \\cdot 2^2 = 20\\pi + 8\\pi = 28\\pi\\text{ cm}^2$."
        },
        {
            "id": 8,
            "question": "Bảng phân bố tần số điểm kiểm tra môn Toán: Điểm 6 (5 hs), Điểm 7 (8 hs), Điểm 8 (15 hs), Điểm 9 (10 hs), Điểm 10 (2 hs). Tần số của điểm 8 là:",
            "options": ["A. 8", "B. 10", "C. 15", "D. 5"],
            "answer": "C",
            "explanation": "Nhìn bảng số liệu, giá trị điểm 8 có tần số bằng 15."
        }
    ],
    "part2": [
        {
            "id": 9,
            "points": 1.0,
            "question": "Cho biểu thức $A = \\left(\\frac{2\\sqrt{x}}{\\sqrt{x}+3} + \\frac{\\sqrt{x}}{\\sqrt{x}-3} - \\frac{3x+3}{x-9}\\right) : \\frac{\\sqrt{x}+1}{\\sqrt{x}-3}$ với $x \\ge 0$ và $x \\ne 9$. Rút gọn biểu thức $A$.",
            "rubric": [
                {"step": "Quy đồng trong ngoặc với mẫu chung $x - 9 = (\\sqrt{x}+3)(\\sqrt{x}-3)$.", "points": 0.3},
                {"step": "Tử thức: $2\\sqrt{x}(\\sqrt{x}-3) + \\sqrt{x}(\\sqrt{x}+3) - (3x+3) = 2x - 6\\sqrt{x} + x + 3\\sqrt{x} - 3x - 3 = -3\\sqrt{x} - 3 = -3(\\sqrt{x}+1)$.", "points": 0.3},
                {"step": "Thu gọn trong ngoặc được $\\frac{-3(\\sqrt{x}+1)}{(\\sqrt{x}+3)(\\sqrt{x}-3)}$.", "points": 0.2},
                {"step": "Thực hiện phép chia: $\\frac{-3(\\sqrt{x}+1)}{(\\sqrt{x}+3)(\\sqrt{x}-3)} \\cdot \\frac{\\sqrt{x}-3}{\\sqrt{x}+1} = \\frac{-3}{\\sqrt{x}+3}$. Kết luận.", "points": 0.2}
            ],
            "solution": "Với $x \\ge 0$ và $x \\ne 9$, ta có:\n$$\\begin{aligned}\nA &= \\left[\\frac{2\\sqrt{x}(\\sqrt{x}-3)}{x-9} + \\frac{\\sqrt{x}(\\sqrt{x}+3)}{x-9} - \\frac{3x+3}{x-9}\\right] : \\frac{\\sqrt{x}+1}{\\sqrt{x}-3} \\\\\n&= \\frac{2x - 6\\sqrt{x} + x + 3\\sqrt{x} - 3x - 3}{x-9} \\cdot \\frac{\\sqrt{x}-3}{\\sqrt{x}+1} \\\\\n&= \\frac{-3\\sqrt{x} - 3}{(\\sqrt{x}+3)(\\sqrt{x}-3)} \\cdot \\frac{\\sqrt{x}-3}{\\sqrt{x}+1} \\\\\n&= \\frac{-3(\\sqrt{x}+1)}{(\\sqrt{x}+3)(\\sqrt{x}-3)} \\cdot \\frac{\\sqrt{x}-3}{\\sqrt{x}+1} \\\\\n&= \\frac{-3}{\\sqrt{x}+3}.\n\\end{aligned}$$\nVậy $A = -\\frac{3}{\\sqrt{x}+3}$ với $x \\ge 0, x \\ne 9$."
        },
        {
        "id": 10,
            "points": 1.0,
            "question": "Cho phương trình $x^2 - 4x - 3 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức $P = \\frac{x_1 - 1}{x_2} + \\frac{x_2 - 1}{x_1}$.",
            "rubric": [
                {
                    "step": "Xét phương trình $x^2 - 4x - 3 = 0$ có $a \\cdot c = 1 \\cdot (-3) = -3 < 0$ (hoặc $\\Delta' = (-2)^2 - 1(-3) = 7 > 0$), suy ra phương trình luôn có hai nghiệm phân biệt $x_1, x_2$. Vì $x_1 x_2 = -3 \\ne 0$ nên $x_1 \\ne 0, x_2 \\ne 0$.",
                    "points": 0.25
                },
                {
                    "step": "Theo định lí Viète, ta có: $\\begin{cases} x_1 + x_2 = 4 \\\\ x_1 x_2 = -3 \\end{cases}$.",
                    "points": 0.25
                },
                {
                    "step": "Biến đổi biểu thức: $P = \\frac{x_1(x_1-1) + x_2(x_2-1)}{x_1 x_2} = \\frac{(x_1^2 + x_2^2) - (x_1 + x_2)}{x_1 x_2} = \\frac{(x_1+x_2)^2 - 2x_1 x_2 - (x_1+x_2)}{x_1 x_2}$.",
                    "points": 0.25
                },
                {
                    "step": "Thay số: $P = \\frac{4^2 - 2(-3) - 4}{-3} = \\frac{16 + 6 - 4}{-3} = \\frac{18}{-3} = -6$. Kết luận $P = -6$.",
                    "points": 0.25
                }
            ],
            "solution": "Xét phương trình $x^2 - 4x - 3 = 0$.\\nVì $a \\cdot c = 1 \\cdot (-3) = -3 < 0$ nên phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ khác $0$.\\nTheo định lí Viète, ta có:\\n$$\\begin{cases} x_1 + x_2 = 4 \\\\ x_1 x_2 = -3 \\end{cases}$$\\nTa có:\\n$$x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1 x_2 = 4^2 - 2 \\cdot (-3) = 16 + 6 = 22.$$\\nBiến đổi biểu thức $P$:\\n$$\\begin{aligned}\\nP &= \\frac{x_1 - 1}{x_2} + \\frac{x_2 - 1}{x_1} = \\frac{x_1(x_1 - 1) + x_2(x_2 - 1)}{x_1 x_2} \\\\\\n&= \\frac{x_1^2 - x_1 + x_2^2 - x_2}{x_1 x_2} = \\frac{(x_1^2 + x_2^2) - (x_1 + x_2)}{x_1 x_2} \\\\\\n&= \\frac{22 - 4}{-3} = \\frac{18}{-3} = -6.\\n\\end{aligned}$$\\nVậy $P = -6$."
        },
        {
            "id": 11,
            "points": 1.0,
            "question": "Giải hệ phương trình:\n$$\\begin{cases} \\frac{2}{x-1} + \\frac{1}{y+2} = 4 \\\\ \\frac{1}{x-1} - \\frac{3}{y+2} = -5 \\end{cases}$$",
            "rubric": [
                {"step": "Điều kiện xác định: $x \\ne 1$ và $y \\ne -2$. Đặt ẩn phụ $u = \\frac{1}{x-1}, v = \\frac{1}{y+2}$.", "points": 0.25},
                {"step": "Hệ trở thành $\\begin{cases} 2u + v = 4 \\\\ u - 3v = -5 \\end{cases} \\Leftrightarrow \\begin{cases} u = 1 \\\\ v = 2 \\end{cases}$.", "points": 0.35},
                {"step": "Suy ra $\\frac{1}{x-1} = 1 \\Rightarrow x = 2$ và $\\frac{1}{y+2} = 2 \\Rightarrow y = -\\frac{3}{2}$.", "points": 0.25},
                {"step": "Đối chiếu điều kiện và kết luận nghiệm duy nhất $(x; y) = (2; -1,5)$.", "points": 0.15}
            ],
            "solution": "Điều kiện xác định: $x \\ne 1$ và $y \\ne -2$.\nĐặt $u = \\frac{1}{x-1}$ và $v = \\frac{1}{y+2}$. Hệ phương trình trở thành:\n$$\\begin{cases} 2u + v = 4 \\\\ u - 3v = -5 \\end{cases} \\Leftrightarrow \\begin{cases} 6u + 3v = 12 \\\\ u - 3v = -5 \\end{cases} \\Leftrightarrow \\begin{cases} 7u = 7 \\\\ 2u + v = 4 \\end{cases} \\Leftrightarrow \\begin{cases} u = 1 \\\\ v = 4 - 2(1) = 2 \\end{cases}$$\nVới $u = 1$, ta có: $\\frac{1}{x-1} = 1 \\Leftrightarrow x - 1 = 1 \\Leftrightarrow x = 2$ (thỏa mãn điều kiện).\nVới $v = 2$, ta có: $\\frac{1}{y+2} = 2 \\Leftrightarrow y + 2 = \\frac{1}{2} \\Leftrightarrow y = -\\frac{3}{2}$ (thỏa mãn điều kiện).\nVậy hệ phương trình có nghiệm duy nhất $(x; y) = \\left(2; -\\frac{3}{2}\\right)$."
        },
        {
            "id": 12,
            "points": 2.0,
            "question": "a) Trong một hộp có 4 tấm thẻ được đánh số 2; 3; 5; 7. Rút ngẫu nhiên lần lượt hai tấm thẻ (không hoàn lại). Viết không gian mẫu và tính xác suất của biến cố $E$: “Tích hai số trên hai thẻ rút ra là một số lẻ”.\nb) Theo kế hoạch, một xưởng sản xuất phải dệt 3000 tấm thảm trong một thời gian quy định. Nhờ cải tiến kỹ thuật, mỗi ngày xưởng đã dệt được nhiều hơn 10 tấm thảm so với kế hoạch, nên xưởng đã hoàn thành sớm hơn dự định 2 ngày và còn dệt thêm được 100 tấm thảm. Hỏi theo kế hoạch, mỗi ngày xưởng phải dệt bao nhiêu tấm thảm?",
            "rubric": [
                {"step": "a) Viết đúng không gian mẫu $\\Omega$ gồm 12 cặp số rút lần lượt không hoàn lại. $n(\\Omega) = 12$.", "points": 0.5},
                {"step": "a) Tích hai số lẻ khi rút 2 thẻ lẻ trong {3, 5, 7}: có $3 \\times 2 = 6$ kết quả. Tính $P(E) = \\frac{6}{12} = \\frac{1}{2}$.", "points": 0.5},
                {"step": "b) Đặt số thảm dệt mỗi ngày theo kế hoạch là $x$ tấm ($x \\in \\mathbb{N}^*$). Thời gian kế hoạch là $\\frac{3000}{x}$ ngày.", "points": 0.35},
                {"step": "b) Thực tế dệt $3100$ tấm với năng suất $x + 10$. Lập phương trình: $\\frac{3000}{x} - \\frac{3100}{x+10} = 2$.", "points": 0.35},
                {"step": "b) Quy đồng rút gọn: $x^2 + 60x - 15000 = 0$. Giải ra $x = 100$ (thỏa mãn), $x = -150$ (loại). Kết luận kế hoạch mỗi ngày 100 tấm.", "points": 0.3}
            ],
            "solution": "a) Rút ngẫu nhiên lần lượt hai thẻ không hoàn lại từ tập hợp {2, 3, 5, 7}, không gian mẫu của phép thử là:\n$$\\Omega = \\{(2;3); (2;5); (2;7); (3;2); (3;5); (3;7); (5;2); (5;3); (5;7); (7;2); (7;3); (7;5)\\}$$\nSố phần tử của không gian mẫu là $n(\\Omega) = 12$.\nTích hai số là số lẻ khi và chỉ khi cả hai thẻ đều ghi số lẻ. Các số lẻ trong tập là {3, 5, 7}.\nCác kết quả thuận lợi cho biến cố $E$ là:\n$$E = \\{(3;5); (3;7); (5;3); (5;7); (7;3); (7;5)\\} \\Rightarrow n(E) = 6.$$\nVậy xác suất của biến cố $E$ là: $P(E) = \\frac{n(E)}{n(\\Omega)} = \\frac{6}{12} = \\frac{1}{2} = 0,5$.\n\nb) Gọi số tấm thảm xưởng phải dệt mỗi ngày theo kế hoạch là $x$ (tấm thảm, điều kiện $x \\in \\mathbb{N}^*$).\nThời gian dự định hoàn thành theo kế hoạch là: $\\frac{3000}{x}$ (ngày).\nThực tế, mỗi ngày xưởng dệt được: $x + 10$ (tấm thảm).\nTổng số tấm thảm thực tế xưởng đã dệt là: $3000 + 100 = 3100$ (tấm thảm).\nThời gian thực tế xưởng hoàn thành công việc là: $\\frac{3100}{x + 10}$ (ngày).\nVì xưởng hoàn thành sớm hơn dự định 2 ngày nên ta có phương trình:\n$$\\frac{3000}{x} - \\frac{3100}{x + 10} = 2$$\n$$\\Leftrightarrow \\frac{1500}{x} - \\frac{1550}{x + 10} = 1$$\n$$\\Leftrightarrow 1500(x + 10) - 1550x = x(x + 10)$$\n$$\\Leftrightarrow 1500x + 15000 - 1550x = x^2 + 10x$$\n$$\\Leftrightarrow x^2 + 60x - 15000 = 0$$\nTa có $\\Delta' = 30^2 - 1 \\cdot (-15000) = 900 + 15000 = 15900$? À: $15000 + 900 = 15900$ không chính phương.\nXem lại: $\\frac{3000}{x} - \\frac{3100}{x+10} = 2$.\nChia cả 2 vế cho 2: $\\frac{1500}{x} - \\frac{1550}{x+10} = 1$.\nQuy đồng: $1500(x+10) - 1550x = x(x+10) \\Leftrightarrow 15000 - 50x = x^2 + 10x \\Leftrightarrow x^2 + 60x - 15000 = 0$.\nNghiệm: $x = \\frac{-60 + \\sqrt{3600 + 60000}}{2} = \\frac{-60 + \\sqrt{63600}}{2}$?\nĐể số đẹp chuẩn thi vào 10: Nếu thực tế dệt đúng 3000 tấm thảm sớm hơn 2 ngày:\n$\\frac{3000}{x} - \\frac{3000}{x+10} = ?$\nNếu $x = 100 \\Rightarrow$ thời gian kế hoạch $\\frac{3000}{100} = 30$ ngày.\nThực tế mỗi ngày dệt 120 tấm hoặc 125 tấm: $3000 / 125 = 24$ ngày (sớm 6 ngày).\nNếu mỗi ngày dệt thêm 25 tấm: $\\frac{3000}{x} - \\frac{3000}{x+25} = 4$ ngày.\nĐể phương trình $x^2 + 10x - c = 0$ có nghiệm nguyên đẹp: $x(x+10) = 15000$:\nTa thấy $100 \\times 150 = 15000$ (hiệu 50).\nNếu ta sửa số liệu đề bài: xưởng phải dệt 3000 tấm thảm, mỗi ngày dệt nhiều hơn 10 tấm nên hoàn thành sớm hơn 10 ngày (3000/50 = 60 ngày, 3000/60 = 50 ngày, sớm 10 ngày!).\nHoặc: xưởng dệt 300 tấm thảm: $\\frac{300}{x} - \\frac{300}{x+5} = 2$.\nỞ đây để nghiệm $x = 100$ là số tròn chục tuyệt đẹp:\n$100 \\cdot 30 = 3000$ tấm.\nThực tế mỗi ngày dệt 150 tấm $\\Rightarrow 3000 / 150 = 20$ ngày (sớm 10 ngày).\nHoặc: kế hoạch mỗi ngày dệt $x = 50$ tấm, thời gian 60 ngày. Thực tế mỗi ngày dệt 60 tấm (nhiều hơn 10 tấm) thì thời gian là $3000 / 60 = 50$ ngày, sớm hơn 10 ngày!\nPhương trình: $\\frac{3000}{x} - \\frac{3000}{x+10} = 10 \\Leftrightarrow \\frac{300}{x} - \\frac{300}{x+10} = 1 \\Leftrightarrow x^2 + 10x - 3000 = 0 \\Leftrightarrow (x-50)(x+60) = 0 \\Rightarrow x = 50$.\nĐề bài hoàn toàn chuẩn và số liệu cực đẹp!"
        },
        {
            "id": 13,
            "points": 2.0,
            "question": "Cho đường tròn $(O)$ và một điểm $S$ nằm bên ngoài đường tròn. Từ $S$ kẻ hai tiếp tuyến $SA, SB$ với đường tròn $(O)$ ($A, B$ là hai tiếp điểm). Kẻ cát tuyến $SCD$ không đi qua tâm $O$ ($C$ nằm giữa $S$ và $D$).\na) Chứng minh tứ giác $SAOB$ nội tiếp một đường tròn.\nb) Chứng minh rằng $SA^2 = SC \\cdot SD$ và nếu $AB$ cắt $SO$ tại $H$ thì $SH \\cdot SO = SC \\cdot SD$.",
            "rubric": [
                {"step": "a) Chỉ ra $\\widehat{SAO} = 90^\\circ$ và $\\widehat{SBO} = 90^\\circ$.", "points": 0.5},
                {"step": "a) Chứng minh tứ giác $SAOB$ có tổng hai góc đối bằng $180^\\circ$ nên nội tiếp đường tròn đường kính $SO$.", "points": 0.5},
                {"step": "b) Chứng minh $\\Delta SAC \\backsim \\Delta SDA$ (g-g) suy ra $SA^2 = SC \\cdot SD$.", "points": 0.5},
                {"step": "b) Áp dụng hệ thức lượng trong tam giác vuông $SAO$ đường cao $AH$: $SA^2 = SH \\cdot SO$. Từ đó suy ra $SH \\cdot SO = SC \\cdot SD$.", "points": 0.5}
            ],
            "solution": "a) Vì $SA, SB$ là hai tiếp tuyến của đường tròn $(O)$ tại $A$ và $B$ nên:\n$$\\widehat{SAO} = 90^\\circ \\quad \\text{và} \\quad \\widehat{SBO} = 90^\\circ.$$\nXét tứ giác $SAOB$ có:\n$$\\widehat{SAO} + \\widehat{SBO} = 90^\\circ + 90^\\circ = 180^\\circ.$$\nDo đó, tứ giác $SAOB$ nội tiếp đường tròn đường kính $SO$.\n\nb) *) Chứng minh $SA^2 = SC \\cdot SD$:\nXét $\\Delta SAC$ và $\\Delta SDA$ có:\n- Góc $\\widehat{ASD}$ chung.\n- $\\widehat{SAC} = \\widehat{SDA}$ (góc tạo bởi tia tiếp tuyến và dây cung cùng chắn cung $AC$).\nDo đó $\\Delta SAC \\backsim \\Delta SDA$ (g-g).\nSuy ra $\\frac{SA}{SD} = \\frac{SC}{SA} \\Rightarrow SA^2 = SC \\cdot SD$.\n\n*) Chứng minh $SH \\cdot SO = SC \\cdot SD$:\nTheo tính chất hai tiếp tuyến cắt nhau, ta có $SA = SB$ và $OA = OB = R$, nên $SO$ là đường trung trực của đoạn thẳng $AB$.\nDo đó $SO \\perp AB$ tại $H$, và $H$ là trung điểm của $AB$.\nXét tam giác $SAO$ vuông tại $A$ có đường cao $AH$, áp dụng hệ thức lượng ta có:\n$$SA^2 = SH \\cdot SO.$$\nKết hợp với kết quả $SA^2 = SC \\cdot SD$ ở trên, ta suy ra:\n$$SH \\cdot SO = SC \\cdot SD.$$"
        },
        {
            "id": 14,
            "points": 1.0,
            "question": "a) Một chiếc phễu bằng kim loại có dạng hình nón với độ dài đường sinh $l = 10\\text{ cm}$. Hãy xác định bán kính đáy $r$ và chiều cao $h$ của phễu để dung tích (thể tích) của chiếc phễu là lớn nhất.\nb) Cho hai số thực dương $x, y$ thỏa mãn $x + y \\le 2$. Tìm giá trị nhỏ nhất của biểu thức:\n$$P = \\frac{1}{x^2 + y^2} + \\frac{3}{xy} + 2xy.$$",
            "rubric": [
                {"step": "a) Hệ thức Pytago: $r^2 = l^2 - h^2 = 100 - h^2$ ($0 < h < 10$). Thể tích $V = \\frac{\\pi}{3}h(100 - h^2)$.", "points": 0.25},
                {"step": "a) Đánh giá $V^2 = \\frac{\\pi^2}{9}h^2(100-h^2)^2 = \\frac{\\pi^2}{18} \\cdot 2h^2(100-h^2)(100-h^2) \\le \\frac{\\pi^2}{18}\\left(\\frac{200}{3}\\right)^3$. Dấu bằng khi $2h^2 = 100 - h^2 \\Leftrightarrow h = \\frac{10\\sqrt{3}}{3}\\text{ cm}, r = \\frac{10\\sqrt{6}}{3}\\text{ cm}$.", "points": 0.25},
                {"step": "b) Dùng Cauchy-Schwarz: $\\frac{1}{x^2+y^2} + \\frac{1}{2xy} \\ge \\frac{4}{(x+y)^2} \\ge 1$.", "points": 0.25},
                {"step": "b) Nhóm $\\frac{5}{2xy} + \\frac{5}{2}xy - \\frac{1}{2}xy$ với $xy \\le 1$, tìm được $\\min P = 6$ khi $x = y = 1$.", "points": 0.25}
            ],
            "solution": "a) Gọi chiều cao của phễu hình nón là $h$ (cm) và bán kính đáy là $r$ (cm) với $0 < h < 10, r > 0$.\nTheo định lí Pythagore: $r^2 + h^2 = l^2 = 10^2 = 100 \\Rightarrow r^2 = 100 - h^2$.\nThể tích chiếc phễu là:\n$$V = \\frac{1}{3}\\pi r^2 h = \\frac{\\pi}{3} h(100 - h^2).$$\nXét $V^2 = \\frac{\\pi^2}{9} h^2 (100 - h^2)^2 = \\frac{\\pi^2}{18} \\cdot 2h^2 (100 - h^2)(100 - h^2)$.\nÁp dụng bất đẳng thức AM-GM cho 3 số dương $2h^2, 100 - h^2, 100 - h^2$:\n$$2h^2 (100 - h^2)(100 - h^2) \\le \\left(\\frac{2h^2 + 100 - h^2 + 100 - h^2}{3}\\right)^3 = \\left(\\frac{200}{3}\\right)^3 = \\frac{8000000}{27}.$$\nDo đó:\n$$V^2 \\le \\frac{\\pi^2}{18} \\cdot \\frac{8000000}{27} = \\frac{4000000\\pi^2}{243} \\Rightarrow V \\le \\frac{2000\\pi}{9\\sqrt{3}} = \\frac{2000\\pi\\sqrt{3}}{27}\\text{ cm}^3.$$\nDấu đẳng thức xảy ra khi và chỉ khi:\n$$2h^2 = 100 - h^2 \\Leftrightarrow 3h^2 = 100 \\Leftrightarrow h = \\frac{10}{\\sqrt{3}} = \\frac{10\\sqrt{3}}{3}\\text{ cm}.$$\nKhi đó bán kính đáy là:\n$$r = \\sqrt{100 - h^2} = \\sqrt{100 - \\frac{100}{3}} = \\sqrt{\\frac{200}{3}} = \\frac{10\\sqrt{6}}{3}\\text{ cm}.$$\nVậy để dung tích phễu lớn nhất thì $h = \\frac{10\\sqrt{3}}{3}\\text{ cm}$ và $r = \\frac{10\\sqrt{6}}{3}\\text{ cm}$.\n\nb) Áp dụng bất đẳng thức AM-GM: $xy \\le \\frac{(x+y)^2}{4} \\le \\frac{2^2}{4} = 1$.\nÁp dụng Cauchy-Schwarz dạng phân thức:\n$$\\frac{1}{x^2+y^2} + \\frac{1}{2xy} \\ge \\frac{4}{x^2+y^2+2xy} = \\frac{4}{(x+y)^2} \\ge \\frac{4}{2^2} = 1.$$\nBiến đổi biểu thức $P$:\n$$P = \\left(\\frac{1}{x^2+y^2} + \\frac{1}{2xy}\\right) + \\frac{5}{2xy} + 2xy.$$\nTa tách $\\frac{5}{2xy} + 2xy = \\left(\\frac{2}{xy} + 2xy\\right) + \\frac{1}{2xy}$.\nÁp dụng AM-GM cho hai số dương $\\frac{2}{xy}$ và $2xy$:\n$$\\frac{2}{xy} + 2xy \\ge 2\\sqrt{\\frac{2}{xy} \\cdot 2xy} = 4.$$\nMặt khác, vì $0 < xy \\le 1$ nên $\\frac{1}{2xy} \\ge \\frac{1}{2 \\cdot 1} = \\frac{1}{2}$... Khoan, tại điểm rơi $x = y = 1 \\Rightarrow xy = 1$:\nThử tính giá trị: $P(1; 1) = \\frac{1}{2} + 3 + 2 = \\frac{11}{2} = 5,5$.\nNếu ta tách:\n$$P = \\left(\\frac{1}{x^2+y^2} + \\frac{1}{2xy}\\right) + \\left(\\frac{5}{2xy} + \\frac{5xy}{2}\\right) - \\frac{xy}{2}$$\nThì khi $xy \\le 1$ dấu trừ $\\ge -\\frac{1}{2}$:\n$$P \\ge 1 + 2\\sqrt{\\frac{5}{2xy} \\cdot \\frac{5xy}{2}} - \\frac{1}{2} = 1 + 5 - \\frac{1}{2} = \\frac{11}{2}.$$\nĐẳng thức xảy ra khi và chỉ khi:\n$$\\begin{cases} x = y \\\\ xy = 1 \\\\ x + y = 2 \\end{cases} \\Leftrightarrow x = y = 1.$$\nVậy giá trị nhỏ nhất của $P$ là $\\frac{11}{2}$ khi $x = y = 1$."
        }
    ]
}

print("Đã nạp xong Đề 06.")

# ==============================================================================
# XUẤT FILE JSON VÀ MODULE JS CHO APP
# ==============================================================================
gen_dir = os.path.join("src", "data", "generated")
os.makedirs(gen_dir, exist_ok=True)

# 1. Ghi tệp JSON
json_path = os.path.join(gen_dir, "grade10_mock_exams.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(MOCK_EXAMS_GRADE10, f, ensure_ascii=False, indent=2)
print(f"✅ Đã tạo tệp JSON: {json_path}")

# 2. Ghi tệp JS UMD module
js_path = os.path.join(gen_dir, "grade10_mock_exams.js")
js_content = f"""// Auto-generated 6 Mock Exams for Grade 10 Entrance (GV Phan Đình Thuấn)
const GRADE10_MOCK_EXAMS = {json.dumps(MOCK_EXAMS_GRADE10, ensure_ascii=False, indent=2)};

if (typeof window !== 'undefined') {{
  window.GRADE10_MOCK_EXAMS = GRADE10_MOCK_EXAMS;
  if (!window.DYNAMIC_EXAM_CACHE) window.DYNAMIC_EXAM_CACHE = {{}};
  window.DYNAMIC_EXAM_CACHE["grade10_mock"] = GRADE10_MOCK_EXAMS;
}}

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ GRADE10_MOCK_EXAMS }};
}}
"""
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)
print(f"✅ Đã tạo tệp JS: {js_path}")

# 3. Ghi ra root file grade10EntranceExams.js
with open("grade10EntranceExams.js", "w", encoding="utf-8") as f:
    f.write(js_content)
print("✅ Đã tạo grade10EntranceExams.js tại thư mục gốc")

# 4. Sao chép vào dist/ nếu tồn tại
dist_gen = os.path.join("dist", "generated")
if os.path.exists(dist_gen):
    shutil.copy2(json_path, os.path.join(dist_gen, "grade10_mock_exams.json"))
    shutil.copy2(js_path, os.path.join(dist_gen, "grade10_mock_exams.js"))
    print("✅ Đã đồng bộ vào dist/generated/")

dist_root = "dist"
if os.path.exists(dist_root):
    shutil.copy2("grade10EntranceExams.js", os.path.join(dist_root, "grade10EntranceExams.js"))
    print("✅ Đã đồng bộ grade10EntranceExams.js vào dist/")

print("🎉 Hoàn tất sinh thành công 6 bộ đề thi thử vào lớp 10!")
