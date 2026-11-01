# -*- coding: utf-8 -*-
"""
BIÊN SOẠN BỔ SUNG 4 ĐỀ CUỐI CHƯƠNG (ĐỀ 4, 5, 6, 7) - TOÁN 6
Chuẩn ma trận Bộ GD&ĐT 2025: 30% Nhận biết, 30% Thông hiểu, 20% Vận dụng, 20% Vận dụng cao.
Gồm 9 chương: c1_6 đến c9_6.
Mỗi đề gồm:
- Phần I: 12 câu trắc nghiệm (3.0 điểm)
- Phần II: 2 câu Đúng/Sai (4.0 điểm), mỗi câu đúng 1 ý Vận dụng
- Phần III: 4 câu Trả lời ngắn (2.0 điểm), đúng 2 câu Vận dụng/VDC
- Phần IV: 3 bài Tự luận (1.0 điểm), có ý Vận dụng cao chốt điểm 10
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')
PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package, OUTPUT_DIR

def load_existing_exams(grade, chapter_id):
    json_path = os.path.join(OUTPUT_DIR, f"grade{grade}_{chapter_id}_exams.json")
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("chapterTitle", ""), data.get("exams", {})
    return "", {}

def build_c1_6_exams():
    """Chương 1: Tập hợp các số tự nhiên (Bài 8: Bài kiểm tra cuối chương I)"""
    chap_id = "c1_6"
    l_idx = 8
    exams = {}
    
    # ĐỀ 4 (🎯 Toàn diện Chuẩn ma trận 30-30-20-20)
    p1_t4 = [
        make_mc(1, "Nhận biết", "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid 5 \\le x < 9\\}$. Viết tập hợp $M$ bằng cách liệt kê các phần tử:", ["$M = \\{5; 6; 7; 8\\}$", "$M = \\{5; 6; 7; 8; 9\\}$", "$M = \\{6; 7; 8\\}$", "$M = \\{6; 7; 8; 9\\}$"], 0),
        make_mc(2, "Nhận biết", "Số La Mã XIX biểu diễn số tự nhiên nào sau đây?", ["$19$", "$21$", "$11$", "$15$"], 0),
        make_mc(3, "Nhận biết", "Kết quả của phép tính $5^3 \\cdot 5^4$ viết dưới dạng một lũy thừa là:", ["$5^7$", "$5^{12}$", "$25^7$", "$5^1$"], 0),
        make_mc(4, "Nhận biết", "Thứ tự thực hiện phép tính đối với biểu thức không có dấu ngoặc là:", ["Lũy thừa $\\to$ Nhân và chia $\\to$ Cộng và trừ", "Cộng và trừ $\\to$ Nhân và chia $\\to$ Lũy thừa", "Nhân và chia $\\to$ Lũy thừa $\\to$ Cộng và trừ", "Từ trái sang phải không phân biệt"], 0),
        make_mc(5, "Thông hiểu", "Tìm số tự nhiên $x$, biết $2x + 15 = 45$:", ["$x = 15$", "$x = 30$", "$x = 12$", "$x = 10$"], 0),
        make_mc(6, "Thông hiểu", "Giá trị của biểu thức $P = 4^3 : 2^2 + 3^2 \\cdot 2$ là:", ["$34$", "$26$", "$30$", "$42$"], 0),
        make_mc(7, "Thông hiểu", "Cho tập hợp $A = \\{x \\in \\mathbb{N}^* \\mid x \\le 50\\}$. Số phần tử của tập hợp $A$ là:", ["$50$", "$49$", "$51$", "$25$"], 0),
        make_mc(8, "Thông hiểu", "Tập hợp các chữ số của số tự nhiên $2026$ có số phần tử là:", ["$3$ (gồm các chữ số $0; 2; 6$)", "$4$", "$2$", "$5$"], 0),
        make_mc(9, "Vận dụng", "Tính tổng nhanh $S = 24 \\cdot 37 + 24 \\cdot 63 + 76 \\cdot 100$:", ["$10\\,000$", "$2\\,400$", "$7\\,600$", "$12\\,400$"], 0),
        make_mc(10, "Vận dụng", "Tìm số tự nhiên $x$, biết $3^{x+1} - 3^x = 162$:", ["$x = 4$", "$x = 3$", "$x = 5$", "$x = 2$"], 0),
        make_mc(11, "Vận dụng", "Một phòng học có 12 bộ bàn ghế, mỗi bộ có 2 học sinh ngồi. Hỏi 25 phòng học như vậy có thể xếp chỗ cho tối đa bao nhiêu học sinh?", ["$600$ học sinh", "$300$ học sinh", "$500$ học sinh", "$720$ học sinh"], 0),
        make_mc(12, "Vận dụng cao", "Chữ số tận cùng của lũy thừa $7^{2026}$ là:", ["$9$", "$7$", "$1$", "$3$"], 0)
    ]
    p2_t4 = [
        make_tf(1, "Cho biểu thức $A = 25 \\cdot 18 - 25 \\cdot 8$ và tập hợp $B = \\{x \\in \\mathbb{N} \\mid 20 < x \\le 25\\}$:", [
            {"key": "a", "level": "Thông hiểu", "text": "Giá trị của biểu thức $A$ bằng $250$.", "correct": True},
            {"key": "b", "level": "Thông hiểu", "text": "Tập hợp $B$ gồm 5 phần tử là: $21; 22; 23; 24; 25$.", "correct": True},
            {"key": "c", "level": "Thông hiểu", "text": "Phần tử $20$ thuộc tập hợp $B$ ($20 \\in B$).", "correct": False},
            {"key": "d", "level": "Vận dụng", "text": "Giá trị của biểu thức $A$ chia hết cho mọi phần tử của tập hợp $B$.", "correct": False}
        ]),
        make_tf(2, "Cho biểu thức $M = 3 + 3^2 + 3^3 + \\dots + 3^{60}$:", [
            {"key": "a", "level": "Thông hiểu", "text": "Tổng $M$ có tất cả $60$ số hạng.", "correct": True},
            {"key": "b", "level": "Thông hiểu", "text": "Số hạng đầu tiên của $M$ là $3$ và số hạng cuối cùng là $3^{60}$.", "correct": True},
            {"key": "c", "level": "Thông hiểu", "text": "Biểu thức $2M + 3$ có thể viết gọn thành $3^{61}$.", "correct": True},
            {"key": "d", "level": "Vận dụng", "text": "Tổng $M$ chia hết cho $13$.", "correct": True}
        ])
    ]
    p3_t4 = [
        make_sa(1, "Thông hiểu", "Tính giá trị biểu thức: $45 + 15 : 3 - 2^3$.", "42"),
        make_sa(2, "Thông hiểu", "Tìm số tự nhiên $x$ thỏa mãn: $125 - 5(x - 3) = 100$.", "8"),
        make_sa(3, "Vận dụng", "Tính tổng dãy số tự nhiên cách đều: $S = 2 + 5 + 8 + \\dots + 98$.", "1650"),
        make_sa(4, "Vận dụng cao", "Tìm số tự nhiên $n$ nhỏ nhất để $2^n - 1$ chia hết cho 7.", "3")
    ]
    p4_t4 = [
        make_essay(1, "Thông hiểu", "Thực hiện phép tính hợp lý: $A = 135 \\cdot 78 + 135 \\cdot 22 - 3500$.", "A = 135.(78 + 22) - 3500 = 135.100 - 3500 = 13500 - 3500 = 10000 (0.25đ)."),
        make_essay(2, "Vận dụng", "Một trường học dự định đưa 420 học sinh khối 6 đi tham quan dã ngoại bằng xe buýt. Mỗi xe buýt chở được tối đa 45 học sinh. Nhà trường cần thuê ít nhất bao nhiêu xe buýt cùng loại để chở hết số học sinh trên?", "Ta thực hiện phép chia có dư: 420 : 45 = 9 (dư 15) (0.25đ).\nNhư vậy 9 xe chỉ chở được 405 em, còn thừa 15 em cần thêm 1 xe nữa.\nVậy nhà trường cần thuê ít nhất: 9 + 1 = 10 xe (0.25đ)."),
        make_essay(3, "Vận dụng cao", "Chứng minh rằng với mọi số tự nhiên $n$, tích $P = n(n + 1)(2n + 1)$ luôn chia hết cho 6.", "Trong hai số tự nhiên liên tiếp n và n+1 luôn có 1 số chẵn nên P chia hết cho 2 (0.25đ).\nXét n chia cho 3: nếu n chia hết cho 3 hoặc n+1 chia hết cho 3 thì P chia hết cho 3. Nếu n = 3k+1 thì 2n+1 = 6k+3 chia hết cho 3. Do đó P chia hết cho 3. Vì ƯCLN(2,3)=1 nên P chia hết cho 6 (0.25đ).")
    ]
    exams[f"{chap_id}_bai{l_idx}_test4"] = {
        "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương I: Tập hợp các số tự nhiên - Bài kiểm tra số 4 (🎯 Toàn diện Chuẩn ma trận 30-30-20-20)",
        "duration": "90 phút",
        "totalScore": 10.0,
        "part1": p1_t4,
        "part2": p2_t4,
        "part3": p3_t4,
        "part4": p4_t4
    }

    # ĐỀ 5 (💡 Vận dụng thực tế)
    p1_t5 = [
        make_mc(1, "Nhận biết", "Số tự nhiên liền trước của số $1000$ là:", ["$999$", "$1001$", "$998$", "$1000$"], 0),
        make_mc(2, "Nhận biết", "Tập hợp $\\mathbb{N}^*$ khác tập hợp $\\mathbb{N}$ ở điểm nào?", ["Không chứa số $0$", "Không chứa số chẵn", "Không chứa số lẻ", "Chỉ chứa số nguyên tố"], 0),
        make_mc(3, "Nhận biết", "Lũy thừa $2^5$ có giá trị bằng:", ["$32$", "$10$", "$16$", "$64$"], 0),
        make_mc(4, "Nhận biết", "Kết quả của phép chia $7^8 : 7^2$ viết dưới dạng lũy thừa là:", ["$7^6$", "$7^4$", "$7^{10}$", "$1^6$"], 0),
        make_mc(5, "Thông hiểu", "Tìm số tự nhiên $x$, biết $3x - 12 = 33$:", ["$x = 15$", "$x = 7$", "$x = 11$", "$x = 9$"], 0),
        make_mc(6, "Thông hiểu", "Giá trị của biểu thức $100 - [60 - (9 - 2)^2]$ là:", ["$89$", "$90$", "$78$", "$95$"], 0),
        make_mc(7, "Thông hiểu", "Cho tập hợp $E = \\{x \\in \\mathbb{N} \\mid 10 < x < 99\\}$. Số phần tử của tập hợp $E$ là:", ["$88$", "$89$", "$90$", "$87$"], 0),
        make_mc(8, "Thông hiểu", "Tích $25 \\cdot 4 \\cdot 37$ có kết quả là:", ["$3700$", "$370$", "$37000$", "$1480$"], 0),
        make_mc(9, "Vận dụng", "Bạn Nam mua 5 quyển vở giá 12 000 đồng/quyển và 3 cây bút bi giá 6 000 đồng/cây. Nam đưa cho cô thu ngân tờ tiền 100 000 đồng. Cô thu ngân phải trả lại Nam bao nhiêu tiền?", ["$22\\,000$ đồng", "$78\\,000$ đồng", "$32\\,000$ đồng", "$18\\,000$ đồng"], 0),
        make_mc(10, "Vận dụng", "Tìm số tự nhiên $x$, biết $2^{x+2} + 2^x = 80$:", ["$x = 4$", "$x = 3$", "$x = 5$", "$x = 2$"], 0),
        make_mc(11, "Vận dụng", "Một đoàn tàu chở hàng gồm 1 đầu máy và 15 toa xe. Mỗi toa xe chở được 32 tấn hàng. Tổng khối lượng hàng đoàn tàu chở được là:", ["$480$ tấn", "$450$ tấn", "$500$ tấn", "$512$ tấn"], 0),
        make_mc(12, "Vận dụng cao", "Chữ số tận cùng của tổng $S = 2 + 2^2 + 2^3 + \\dots + 2^{2024}$ là:", ["$0$", "$2$", "$4$", "$6$"], 0)
    ]
    p2_t5 = [
        make_tf(1, "Bác An đi siêu thị mua hàng gồm: 3 kg gạo với giá 25 000 đồng/kg, 2 chai dầu ăn với giá 48 000 đồng/chai và 1 hộp bánh quy giá 35 000 đồng:", [
            {"key": "a", "level": "Thông hiểu", "text": "Số tiền mua 3 kg gạo là $75\\,000$ đồng.", "correct": True},
            {"key": "b", "level": "Thông hiểu", "text": "Số tiền mua 2 chai dầu ăn là $96\\,000$ đồng.", "correct": True},
            {"key": "c", "level": "Thông hiểu", "text": "Tổng số tiền Bác An phải trả là $206\\,000$ đồng.", "correct": True},
            {"key": "d", "level": "Vận dụng", "text": "Nếu Bác An có phiếu giảm giá $10\\%$ trên tổng hóa đơn thì số tiền được giảm là $25\\,000$ đồng.", "correct": False}
        ]),
        make_tf(2, "Cho tập hợp $X$ gồm các số tự nhiên có hai chữ số chia hết cho 5:", [
            {"key": "a", "level": "Thông hiểu", "text": "Phần tử nhỏ nhất của tập hợp $X$ là $10$.", "correct": True},
            {"key": "b", "level": "Thông hiểu", "text": "Phần tử lớn nhất của tập hợp $X$ là $95$.", "correct": True},
            {"key": "c", "level": "Thông hiểu", "text": "Tập hợp $X$ có đúng $18$ phần tử.", "correct": True},
            {"key": "d", "level": "Vận dụng", "text": "Tổng của tất cả các phần tử trong tập hợp $X$ bằng $1000$.", "correct": False}
        ])
    ]
    p3_t5 = [
        make_sa(1, "Thông hiểu", "Tính giá trị biểu thức: $120 : (15 + 5) \\cdot 3$.", "18"),
        make_sa(2, "Thông hiểu", "Tìm số tự nhiên $x$ thỏa mãn: $4(x - 5) + 12 = 52$.", "15"),
        make_sa(3, "Vận dụng", "Một thư viện trường học có 4 giá sách, mỗi giá có 5 ngăn, mỗi ngăn xếp được 28 cuốn sách. Hỏi thư viện có tất cả bao nhiêu cuốn sách?", "560"),
        make_sa(4, "Vận dụng cao", "Tìm số tự nhiên $x$ thỏa mãn: $1 + 3 + 5 + \\dots + (2x - 1) = 144$.", "12")
    ]
    p4_t5 = [
        make_essay(1, "Thông hiểu", "Thực hiện phép tính hợp lý: $B = 72 \\cdot 64 + 72 \\cdot 36 - 1200$.", "B = 72.(64 + 36) - 1200 = 72.100 - 1200 = 7200 - 1200 = 6000 (0.25đ)."),
        make_essay(2, "Vận dụng", "Mẹ cho Lan 200 000 đồng đi nhà sách. Lan mua 1 cuốn sách tham khảo giá 65 000 đồng, 8 cuốn vở giá 11 000 đồng/cuốn. Hỏi Lan còn lại bao nhiêu tiền?", "Số tiền Lan mua 8 cuốn vở: 8 x 11 000 = 88 000 (đồng) (0.25đ).\nTổng số tiền Lan đã mua: 65 000 + 88 000 = 153 000 (đồng).\nSố tiền còn lại: 200 000 - 153 000 = 47 000 (đồng) (0.25đ)."),
        make_essay(3, "Vận dụng cao", "Tìm chữ số tận cùng của lũy thừa $A = 2^{2025} + 3^{2025}$.", "2^4 = 16 tận cùng 6 nên 2^2024 tận cùng 6 => 2^2025 tận cùng 2 (0.25đ).\n3^4 = 81 tận cùng 1 nên 3^2024 tận cùng 1 => 3^2025 tận cùng 3.\nVậy chữ số tận cùng của A là: 2 + 3 = 5 (0.25đ).")
    ]
    exams[f"{chap_id}_bai{l_idx}_test5"] = {
        "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương I: Tập hợp các số tự nhiên - Bài kiểm tra số 5 (💡 Vận dụng thực tế)",
        "duration": "90 phút",
        "totalScore": 10.0,
        "part1": p1_t5,
        "part2": p2_t5,
        "part3": p3_t5,
        "part4": p4_t5
    }

    # ĐỀ 6 (🔥 Phân hóa Nâng cao)
    p1_t6 = [
        make_mc(1, "Nhận biết", "Số phần tử của tập hợp các số tự nhiên chẵn nhỏ hơn 20 là:", ["$10$", "$9$", "$11$", "$20$"], 0),
        make_mc(2, "Nhận biết", "Số La Mã XXIV tương ứng với số tự nhiên nào?", ["$24$", "$26$", "$19$", "$29$"], 0),
        make_mc(3, "Nhận biết", "Tích $3^2 \\cdot 3^3$ bằng:", ["$3^5 = 243$", "$3^6$", "$9^5$", "$27$"], 0),
        make_mc(4, "Nhận biết", "Thương $10^9 : 10^3$ dưới dạng lũy thừa cơ số 10 là:", ["$10^6$", "$10^3$", "$10^{12}$", "$1^6$"], 0),
        make_mc(5, "Thông hiểu", "Tìm số tự nhiên $x$, biết $5x - 35 = 65$:", ["$x = 20$", "$x = 10$", "$x = 25$", "$x = 15$"], 0),
        make_mc(6, "Thông hiểu", "Giá trị của biểu thức $A = 2^4 \\cdot 5 - [131 - (13 - 4)^2]$ là:", ["$30$", "$40$", "$25$", "$35$"], 0),
        make_mc(7, "Thông hiểu", "Số các số tự nhiên có ba chữ số là:", ["$900$", "$899$", "$901$", "$999$"], 0),
        make_mc(8, "Thông hiểu", "Kết quả phép tính $45 \\cdot 11$ là:", ["$495$", "$450$", "$505$", "$465$"], 0),
        make_mc(9, "Vận dụng", "Tính giá trị tổng $S = 1 + 2 + 3 + \\dots + 50$:", ["$1275$", "$1250$", "$1300$", "$2550$"], 0),
        make_mc(10, "Vận dụng", "Tìm $x \\in \\mathbb{N}$, biết $5^{x+1} - 5^x = 500$:", ["$x = 3$", "$x = 2$", "$x = 4$", "$x = 5$"], 0),
        make_mc(11, "Vận dụng", "Một gia đình dự định lát nền một căn phòng hình chữ nhật có kích thước $6\\text{ m} \\times 4\\text{ m}$ bằng gạch vuông cạnh $40\\text{ cm}$. Số viên gạch cần mua là:", ["$150$ viên", "$120$ viên", "$200$ viên", "$240$ viên"], 0),
        make_mc(12, "Vận dụng cao", "Tìm số tự nhiên $n$ để phân số $\\frac{n+7}{n+2}$ là số tự nhiên:", ["$n = 3$ (hoặc $n=0$)", "$n = 4$", "$n = 5$", "$n = 2$"], 0)
    ]
    p2_t6 = [
        make_tf(1, "Cho biểu thức $P = 1 + 4 + 4^2 + 4^3 + \\dots + 4^{20}$:", [
            {"key": "a", "level": "Thông hiểu", "text": "Tổng $P$ có tất cả $21$ số hạng.", "correct": True},
            {"key": "b", "level": "Thông hiểu", "text": "Biểu thức $3P + 1$ có giá trị bằng $4^{21}$.", "correct": True},
            {"key": "c", "level": "Thông hiểu", "text": "Tổng $P$ là một số lẻ.", "correct": True},
            {"key": "d", "level": "Vận dụng", "text": "Tổng $P$ chia hết cho $5$.", "correct": False}
        ]),
        make_tf(2, "Cho số tự nhiên có hai chữ số $\\overline{ab}$ thỏa mãn $a - b = 3$ và $\\overline{ab}$ chia hết cho 5:", [
            {"key": "a", "level": "Thông hiểu", "text": "Chữ số tận cùng $b$ chỉ có thể là $0$ hoặc $5$.", "correct": True},
            {"key": "b", "level": "Thông hiểu", "text": "Nếu $b = 0$ thì chữ số $a = 3$, ta được số $30$.", "correct": True},
            {"key": "c", "level": "Thông hiểu", "text": "Nếu $b = 5$ thì chữ số $a = 8$, ta được số $85$.", "correct": True},
            {"key": "d", "level": "Vận dụng", "text": "Tổng của hai số tự nhiên tìm được ở trên là một số chia hết cho 9.", "correct": False}
        ])
    ]
    p3_t6 = [
        make_sa(1, "Thông hiểu", "Tính giá trị biểu thức: $2^3 \\cdot 15 - [115 - (12 - 5)^2]$.", "54"),
        make_sa(2, "Thông hiểu", "Tìm số tự nhiên $x$ thỏa mãn: $(2x - 8) : 3 = 14$.", "25"),
        make_sa(3, "Vận dụng", "Tính tổng dãy số lẻ cách đều: $S = 1 + 3 + 5 + \\dots + 49$.", "625"),
        make_sa(4, "Vận dụng cao", "Tìm số tự nhiên $x$ nhỏ nhất sao cho $x$ chia 3 dư 2, chia 5 dư 3, chia 7 dư 4.", "53")
    ]
    p4_t6 = [
        make_essay(1, "Thông hiểu", "Thực hiện phép tính hợp lý: $C = 28 \\cdot 45 + 28 \\cdot 55 - 1800$.", "C = 28.(45 + 55) - 1800 = 28.100 - 1800 = 2800 - 1800 = 1000 (0.25đ)."),
        make_essay(2, "Vận dụng", "Một kho gạo có 150 tấn gạo. Ngày thứ nhất xuất đi 35 tấn, ngày thứ hai xuất đi gấp đôi ngày thứ nhất. Hỏi trong kho còn lại bao nhiêu tấn gạo?", "Ngày thứ hai xuất: 35 x 2 = 70 (tấn) (0.25đ).\nCả hai ngày xuất: 35 + 70 = 105 (tấn).\nTrong kho còn lại: 150 - 105 = 45 (tấn) (0.25đ)."),
        make_essay(3, "Vận dụng cao", "Tìm tất cả các cặp số tự nhiên $(x, y)$ thỏa mãn: $(x + 1)(2y - 1) = 15$.", "Vì 2y - 1 là số lẻ và là ước của 15 nên 2y - 1 in {1; 3; 5; 15} (0.25đ).\nTH1: 2y - 1 = 1 => y = 1; x + 1 = 15 => x = 14.\nTH2: 2y - 1 = 3 => y = 2; x + 1 = 5 => x = 4.\nTH3: 2y - 1 = 5 => y = 3; x + 1 = 3 => x = 2.\nTH4: 2y - 1 = 15 => y = 8; x + 1 = 1 => x = 0.\nVậy các cặp (x, y) là: (14, 1); (4, 2); (2, 3); (0, 8) (0.25đ).")
    ]
    exams[f"{chap_id}_bai{l_idx}_test6"] = {
        "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương I: Tập hợp các số tự nhiên - Bài kiểm tra số 6 (🚀 Phân hóa Nâng cao)",
        "duration": "90 phút",
        "totalScore": 10.0,
        "part1": p1_t6,
        "part2": p2_t6,
        "part3": p3_t6,
        "part4": p4_t6
    }

    # ĐỀ 7 (🏆 Chinh phục điểm 10)
    p1_t7 = [
        make_mc(1, "Nhận biết", "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid 12 < x \\le 16\\}$. Phần tử nào sau đây thuộc tập $A$?", ["$16$", "$12$", "$11$", "$17$"], 0),
        make_mc(2, "Nhận biết", "Số La Mã XXVIII tương ứng với số tự nhiên nào?", ["$28$", "$27$", "$29$", "$33$"], 0),
        make_mc(3, "Nhận biết", "Lũy thừa $3^4$ có giá trị bằng:", ["$81$", "$12$", "$64$", "$27$"], 0),
        make_mc(4, "Nhận biết", "Thương $6^9 : 6^3$ bằng:", ["$6^6$", "$6^3$", "$1^6$", "$6^{12}$"], 0),
        make_mc(5, "Thông hiểu", "Tìm số tự nhiên $x$, biết $7x - 21 = 49$:", ["$x = 10$", "$x = 7$", "$x = 8$", "$x = 12$"], 0),
        make_mc(6, "Thông hiểu", "Giá trị của biểu thức $A = 50 - [30 - (6 - 2)^2]$ là:", ["$36$", "$40$", "$24$", "$46$"], 0),
        make_mc(7, "Thông hiểu", "Số phần tử của tập hợp $K = \\{x \\in \\mathbb{N} \\mid 20 \\le x \\le 80\\}$ là:", ["$61$", "$60$", "$59$", "$62$"], 0),
        make_mc(8, "Thông hiểu", "Tính nhẩm $125 \\cdot 8 \\cdot 19$ ta được kết quả là:", ["$19\\,000$", "$1900$", "$190\\,000$", "$15\\,200$"], 0),
        make_mc(9, "Vận dụng", "Tính giá trị tổng $S = 2 + 4 + 6 + \\dots + 60$:", ["$930$", "$900$", "$960$", "$1860$"], 0),
        make_mc(10, "Vận dụng", "Tìm $x \\in \\mathbb{N}$, biết $2^{x+3} - 2^x = 112$:", ["$x = 4$", "$x = 3$", "$x = 5$", "$x = 2$"], 0),
        make_mc(11, "Vận dụng", "Một cửa hàng ngày đầu bán được 24 chiếc quạt máy, mỗi chiếc lãi 85 000 đồng. Ngày thứ hai bán được 36 chiếc quạt cùng loại. Tổng số tiền lãi của cửa hàng trong hai ngày là:", ["$5\\,100\\,000$ đồng", "$4\\,500\\,000$ đồng", "$6\\,000\\,000$ đồng", "$3\\,060\\,000$ đồng"], 0),
        make_mc(12, "Vận dụng cao", "Tìm số tự nhiên $n$ lớn nhất có hai chữ số sao cho $2n + 1$ là bội của $n - 2$:", ["$n = 7$", "$n = 99$", "$n = 5$", "$n = 8$"], 0)
    ]
    p2_t7 = [
        make_tf(1, "Cho số tự nhiên $A = 1 + 2 + 2^2 + 2^3 + \\dots + 2^{2024}$:", [
            {"key": "a", "level": "Thông hiểu", "text": "Tổng $A$ có $2025$ số hạng.", "correct": True},
            {"key": "b", "level": "Thông hiểu", "text": "Giá trị của biểu thức $A + 1$ bằng $2^{2025}$.", "correct": True},
            {"key": "c", "level": "Thông hiểu", "text": "Số $A$ là một số lẻ.", "correct": True},
            {"key": "d", "level": "Vận dụng", "text": "Số $A$ chia hết cho 3.", "correct": False}
        ]),
        make_tf(2, "Cho số tự nhiên có ba chữ số $\\overline{abc}$ thỏa mãn $a + b + c = 7$ và $\\overline{abc}$ chia hết cho 5:", [
            {"key": "a", "level": "Thông hiểu", "text": "Chữ số $c$ chỉ có thể nhận giá trị $0$ hoặc $5$.", "correct": True},
            {"key": "b", "level": "Thông hiểu", "text": "Nếu $c = 5$ thì $a + b = 2$, có 2 số thỏa mãn là $115$ và $205$.", "correct": True},
            {"key": "c", "level": "Thông hiểu", "text": "Nếu $c = 0$ thì $a + b = 7$, có 7 số thỏa mãn (từ $160$ đến $700$).", "correct": True},
            {"key": "d", "level": "Vận dụng", "text": "Tổng số các số thỏa mãn yêu cầu đề bài là đúng 9 số.", "correct": True}
        ])
    ]
    p3_t7 = [
        make_sa(1, "Thông hiểu", "Tính giá trị biểu thức: $3^4 : 3^2 + 2^3 \\cdot 5 - 1$.", "48"),
        make_sa(2, "Thông hiểu", "Tìm số tự nhiên $x$ thỏa mãn: $150 - 5(x + 4) = 75$.", "11"),
        make_sa(3, "Vận dụng", "Tính tổng các số tự nhiên có hai chữ số chia hết cho 3: $S = 12 + 15 + \\dots + 99$.", "1665"),
        make_sa(4, "Vận dụng cao", "Tìm số tự nhiên $n$ sao cho $n^2 + 2n + 4$ chia hết cho $n + 1$.", "2")
    ]
    p4_t7 = [
        make_essay(1, "Thông hiểu", "Thực hiện phép tính hợp lý: $D = 43 \\cdot 57 + 43 \\cdot 43 - 2300$.", "D = 43.(57 + 43) - 2300 = 43.100 - 2300 = 4300 - 2300 = 2000 (0.25đ)."),
        make_essay(2, "Vận dụng", "Bác Ba muốn rào xung quanh một mảnh vườn hình chữ nhật có chiều dài 25 m và chiều rộng 15 m bằng lưới B40. Biết cổng vào rộng 3 m không rào. Hỏi Bác Ba cần bao nhiêu mét lưới B40?", "Chu vi mảnh vườn: (25 + 15) x 2 = 80 (m) (0.25đ).\nSố mét lưới B40 cần dùng: 80 - 3 = 77 (m) (0.25đ)."),
        make_essay(3, "Vận dụng cao", "Cho $S = 5 + 5^2 + 5^3 + \\dots + 5^{100}$. Chứng minh rằng $4S + 5$ là một lũy thừa của 5.", "Nhân cả hai vế với 5: 5S = 5^2 + 5^3 + ... + 5^101 (0.25đ).\nLấy 5S - S = 5^101 - 5 => 4S = 5^101 - 5.\nDo đó: 4S + 5 = 5^101 là lũy thừa của 5 (0.25đ).")
    ]
    exams[f"{chap_id}_bai{l_idx}_test7"] = {
        "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương I: Tập hợp các số tự nhiên - Bài kiểm tra số 7 (🏆 Chinh phục điểm 10)",
        "duration": "90 phút",
        "totalScore": 10.0,
        "part1": p1_t7,
        "part2": p2_t7,
        "part3": p3_t7,
        "part4": p4_t7
    }

    return chap_id, exams

print("Module build_grade6_chapter_ends created successfully.")
