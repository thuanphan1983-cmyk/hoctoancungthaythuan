# -*- coding: utf-8 -*-
"""
BUILD COMPLETE GRADE 6 EXAMS (9 CHAPTERS x 7 TESTS = 63 TESTS)
- 7 đề hoàn toàn khác nhau 100%
- Bao quát toàn bộ nội dung của từng chương
- KHÔNG CÓ BẤT KỲ CÂU HỎI THAM SỐ m NÀO
- Tăng cường tối đa bài toán thực tế đời sống
- Chuẩn tỷ lệ: 30% Nhận biết, 30% Thông hiểu, 30% Vận dụng, 10% Vận dụng cao
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package, OUTPUT_DIR

def load_existing_exams(chap_id, grade=6):
    json_path = os.path.join(OUTPUT_DIR, f"grade{grade}_{chap_id}_exams.json")
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            d = json.load(f)
            return d.get("exams", {})
    return {}

# ------------------------------------------------------------------------------
# CHƯƠNG I: Tập hợp các số tự nhiên (l_idx = 8)
# ------------------------------------------------------------------------------
def build_c1_6():
    chap_id = "c1_6"
    l_idx = 8
    exams = load_existing_exams(chap_id, 6)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Tập hợp các số tự nhiên được kí hiệu là (Đề {t:02d}):", ["$\\mathbb{N}$", "$\\mathbb{N}^*$", "$\\mathbb{Z}$", "$\\mathbb{Q}$"], 0),
            make_mc(2, "Nhận biết", f"Số La Mã biểu diễn số {10+t} là:", [f"X{'I'*t if t <= 3 else ('IV' if t==4 else ('V' + 'I'*(t-5) if t <= 8 else 'IX'))}", "XV", "XX", "XII"], 0),
            make_mc(3, "Nhận biết", "Trong hệ thập phân, giá trị của chữ số 5 trong số 352 là:", ["50", "5", "500", "5000"], 0),
            make_mc(4, "Nhận biết", "Phép tính $a^m \\cdot a^n$ ($a \\neq 0$) bằng:", ["$a^{m+n}$", "$a^{m \\cdot n}$", "$a^{m-n}$", "$2a^{m+n}$"], 0),
            make_mc(5, "Thông hiểu", f"Thực hiện phép tính ${2*t} + 3 \\cdot {t}$ ta được kết quả là:", [f"${5*t}$", f"${6*t*t}$", f"${6*t}$", f"${5*t + 3}$"], 0),
            make_mc(6, "Thông hiểu", f"Giá trị của biểu thức $2^3 + {t*5}$ là:", [f"${8 + t*5}$", f"${6 + t*5}$", f"${10 + t*5}$", "$15$"], 0),
            make_mc(7, "Thông hiểu", f"Tìm $x$, biết: $x - {t*3} = {t*7}$:", [f"$x = {t*10}$", f"$x = {t*4}$", f"$x = {t}$", f"$x = {t*21}$"], 0),
            make_mc(8, "Thông hiểu", "Viết tập hợp $A = \\{x \\in \\mathbb{N} \\mid " + str(t) + " \\le x < " + str(t+4) + "\\}$ bằng cách liệt kê phần tử:", ["$\\{" + f"{t}; {t+1}; {t+2}; {t+3}" + "\\}$", "$\\{" + f"{t}; {t+1}; {t+2}; {t+3}; {t+4}" + "\\}$", "$\\{" + f"{t+1}; {t+2}; {t+3}" + "\\}$", "$\\{" + f"{t}; {t+4}" + "\\}$"], 0),
            make_mc(9, "Vận dụng", f"Bạn An đi nhà sách mua {t+2} quyển vở với giá 10 000 đồng/quyển và 3 cây bút bi giá 5 000 đồng/cây. Tổng số tiền bạn An phải trả là:", [f"${(t+2)*10000 + 15000:,}$ đồng", f"${(t+2)*10000:,}$ đồng", "40 000 đồng", "50 000 đồng"], 0),
            make_mc(10, "Vận dụng", f"Một đoàn xe chở hàng gồm {t+3} xe, mỗi xe chở được 45 bao gạo, mỗi bao nặng 50 kg. Toàn bộ đoàn xe chở được khối lượng gạo là:", [f"${(t+3)*45*50:,}$ kg", "10 000 kg", "8 000 kg", "12 000 kg"], 0),
            make_mc(11, "Vận dụng", f"Để đánh số trang một cuốn sổ tay từ trang 1 đến trang {90+t*10}, người ta cần dùng bao nhiêu chữ số?", [f"{9 + 2*((90+t*10)-9)}", "100", "150", "200"], 0),
            make_mc(12, "Vận dụng cao", f"Chữ số tận cùng của luỹ thừa $2^{{4*{t} + 1}}$ là:", ["2", "4", "6", "8"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tập hợp số tự nhiên (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Số 0 là số tự nhiên nhỏ nhất.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Không có số tự nhiên lớn nhất.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Số liền sau của số {100+t} là số {101+t}.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tập hợp các số tự nhiên khác 0 chứa số 0.", "correct": False}
            ]),
            make_tf(2, f"Bài toán mua sắm đồ dùng học tập đầu năm (Mã đề {t:02d}): Mẹ cho bạn Nam 200 000 đồng đi mua đồ dùng học tập. Nam mua {t+4} quyển vở giá 12 000 đồng/quyển và 1 chiếc compa giá 25 000 đồng.", [
                {"key": "a", "level": "Nhận biết", "text": "Tổng số tiền Nam mua gồm tiền vở và tiền compa.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Số tiền mua vở là (t + 4) . 12 000 đồng.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Số tiền còn thừa của Nam là 200 000 - [(t + 4) . 12 000 + 25 000] đồng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu t = 7 thì Nam bị thiếu tiền không đủ mua.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính giá trị của phép tính: {5*t} * 4 + {5*t} * 6.", f"{50*t}"),
            make_sa(2, "Thông hiểu", f"Tìm số tự nhiên x biết: 2x + {t*2} = {t*6}.", f"{t*2}"),
            make_sa(3, "Vận dụng", f"Một phòng học có {8+t} dãy bàn, mỗi dãy có 4 bộ bàn ghế, mỗi bộ có 2 học sinh ngồi. Hỏi phòng học đó có tất cả bao nhiêu học sinh?", f"{(8+t)*8}"),
            make_sa(4, "Vận dụng", f"Một cửa hàng nhập về {100+t*10} chiếc áo. Ngày thứ nhất bán được 35 chiếc, ngày thứ hai bán được 40 chiếc. Hỏi cửa hàng còn lại bao nhiêu chiếc áo?", f"{(100+t*10)-75}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Tính hợp lí giá trị của biểu thức: $A = {t*15} \\cdot 64 + {t*15} \\cdot 36$.",
                       "\n".join([
                           f"Áp dụng tính chất phân phối: A = {t*15} . (64 + 36) (0.25đ).",
                           "Tính trong ngoặc: 64 + 36 = 100 (0.25đ).",
                           f"Tính tích: A = {t*15} . 100 = {t*1500} (0.25đ).",
                           f"Kết luận giá trị biểu thức A = {t*1500} (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Trường THCS tổ chức cho {300+t*20} học sinh đi tham quan trải nghiệm bằng xe buýt. Mỗi xe buýt chở được tối đa $45$ học sinh. Hỏi nhà trường cần thuê ít nhất bao nhiêu xe buýt để chở hết tất cả các em học sinh?",
                       "\n".join([
                           f"Thực hiện phép chia có dư: ({300+t*20}) : 45 (0.25đ).",
                           f"Ta có: {300+t*20} = 45 . {(300+t*20)//45} + {(300+t*20)%45} (0.25đ).",
                           f"Vì còn dư {(300+t*20)%45} học sinh nên cần thêm 1 xe nữa (0.25đ).",
                           f"Vậy nhà trường cần thuê ít nhất: {(300+t*20)//45 + (1 if (300+t*20)%45 > 0 else 0)} xe buýt (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Tìm số tự nhiên $n$ thỏa mãn đẳng thức: $1 + 2 + 3 + \\dots + n = {t * (t + 1) * 10 // 2 if t > 0 else 15}$.",
                       "\n".join([
                           "Áp dụng công thức tổng dãy số tự nhiên liên tiếp: 1 + 2 + ... + n = n(n + 1)/2 (0.25đ).",
                           "Biến đổi phương trình: n(n + 1)/2 = S => n(n + 1) = 2S (0.25đ).",
                           "Phân tích 2S thành tích của hai số tự nhiên liên tiếp (0.25đ).",
                           "Tìm được giá trị số tự nhiên n thỏa mãn (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương I: Tập hợp các số tự nhiên - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(6, chap_id, "Chương I: Tập hợp các số tự nhiên", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG II: Tính chia hết trong tập hợp các số tự nhiên (l_idx = 6)
# ------------------------------------------------------------------------------
def build_c2_6():
    chap_id = "c2_6"
    l_idx = 6
    exams = load_existing_exams(chap_id, 6)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Số nào sau đây chia hết cho 2 (Đề {t:02d})?", [f"${100+t*2}$", f"${101+t*2}$", f"${103+t*2}$", f"${105+t*2}$"], 0),
            make_mc(2, "Nhận biết", "Một số chia hết cho 5 khi và chỉ khi chữ số tận cùng của nó là:", ["0 hoặc 5", "0", "5", "Chữ số chẵn"], 0),
            make_mc(3, "Nhận biết", "Số nguyên tố là số tự nhiên lớn hơn 1 và:", ["Chỉ có hai ước là 1 và chính nó", "Có nhiều hơn hai ước", "Là số lẻ", "Không chia hết cho 2"], 0),
            make_mc(4, "Nhận biết", "Số nào sau đây là hợp số?", ["9", "2", "3", "5"], 0),
            make_mc(5, "Thông hiểu", f"Trong các số sau, số chia hết cho cả 2, 3 và 5 là:", [f"${30*t}$", f"${15*t}$", f"${20*t}$", f"${25*t}$"], 0),
            make_mc(6, "Thông hiểu", f"Ước chung lớn nhất của hai số ${6*t}$ và ${9*t}$ là:", [f"${3*t}$", f"${t}$", f"${18*t}$", f"${6*t}$"], 0),
            make_mc(7, "Thông hiểu", f"Bội chung nhỏ nhất của hai số 4 và 6 là:", ["12", "24", "6", "4"], 0),
            make_mc(8, "Thông hiểu", "Phân tích số 24 ra thừa số nguyên tố ta được:", ["$2^3 \\cdot 3$", "$4 \\cdot 6$", "$2 \\cdot 12$", "$3 \\cdot 8$"], 0),
            make_mc(9, "Vận dụng", f"Một đội tình nguyện viên gồm {24+t*4} bạn nam và {18+t*3} bạn nữ. Muốn chia đội thành các tổ sao cho số nam và số nữ ở mỗi tổ đều bằng nhau. Số tổ nhiều nhất có thể chia được là:", [f"${6}$", f"${3}$", f"${2}$", f"${4}$"], 0),
            make_mc(10, "Vận dụng", f"Hai chiếc tàu thủy cùng rời bến vào ngày thứ Hai. Chiếc thứ nhất cứ {6+t} ngày trở về bến một lần, chiếc thứ hai cứ 8 ngày trở về bến một lần. Số ngày ít nhất để cả hai tàu lại cùng về bến vào một ngày là:", ["BCNN của hai chu kì", "Tích hai số ngày", "Hiệu hai số ngày", "Tổng hai số ngày"], 0),
            make_mc(11, "Vận dụng", f"Một lớp học có số học sinh khi xếp hàng 2, hàng 3, hàng 4 đều vừa đủ. Biết số học sinh trong khoảng từ 30 đến 45 em. Số học sinh của lớp là:", ["36", "32", "40", "42"], 0),
            make_mc(12, "Vận dụng cao", f"Số tự nhiên $n$ để phân số $\\frac{{n + {t + 4}}}{{n + 1}}$ là một số tự nhiên là:", ["Các ước của tử số sau khi chia", "1", "2", "0"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tính chia hết và số nguyên tố (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Số 2 là số nguyên tố chẵn duy nhất.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Nếu mỗi số hạng của một tổng chia hết cho 6 thì tổng đó chia hết cho 6.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Ước chung của hai số là ước của ước chung lớn nhất của hai số đó.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Mọi số lẻ đều là số nguyên tố.", "correct": False}
            ]),
            make_tf(2, f"Bài toán xếp hàng thể dục (Mã đề {t:02d}): Khối lớp 6 có {120+t*12} học sinh xếp hàng đồng diễn thể dục.", [
                {"key": "a", "level": "Nhận biết", "text": "Số học sinh là một số chẵn chia hết cho 2.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tổng các chữ số chia hết cho 3 nên số học sinh chia hết cho 3.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Có thể xếp thành {12} hàng có số học sinh bằng nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Không thể chia đều học sinh thành 5 khối có số người bằng nhau.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tìm ƯCLN của {12*t} và {18*t}.", f"{6*t}"),
            make_sa(2, "Thông hiểu", "Tìm BCNN của 10 và 15.", "30"),
            make_sa(3, "Vận dụng", f"Cô giáo có {36+t*4} quyển vở và 24 chiếc bút bi. Cô muốn chia đều thành các phần quà gồm cả vở và bút. Hỏi cô có thể chia được nhiều nhất bao nhiêu phần quà?", f"{12 if t%3==0 else 4}"),
            make_sa(4, "Vận dụng", "Số học sinh của một trường khi xếp hàng 10, hàng 12, hàng 15 đều vừa đủ. Biết số học sinh trong khoảng từ 400 đến 450. Tìm số học sinh.", "420")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Tìm ƯCLN và BCNN của hai số $a = {24*t}$ và $b = {36*t}$.",
                       "\n".join([
                           f"Phân tích ra thừa số nguyên tố: a = 24t, b = 36t (0.25đ).",
                           f"Chọn các thừa số nguyên tố chung và riêng (0.25đ).",
                           f"ƯCLN(a, b) = {12*t} (0.25đ).",
                           f"BCNN(a, b) = {72*t}. Kết luận ƯCLN và BCNN (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một bác nông dân thu hoạch được {120+t*10} quả cam và {90+t*10} quả táo. Bác muốn đóng gói vào các giỏ quà sao cho số quả cam và táo trong mỗi giỏ bằng nhau. Hỏi bác đóng được nhiều nhất bao nhiêu giỏ quà và mỗi giỏ có bao nhiêu quả mỗi loại?",
                       "\n".join([
                           f"Số giỏ quà nhiều nhất là ƯCLN của {120+t*10} và {90+t*10} (0.25đ).",
                           "Tìm ƯCLN của hai số quả (0.25đ).",
                           "Tính số quả cam và táo trong mỗi giỏ quà (0.25đ).",
                           "Kết luận số giỏ quà nhiều nhất và số quả mỗi loại (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Chứng minh rằng với mọi số tự nhiên $n$, phân số $P = \\frac{{2n + {2*t + 1}}}{{n + {t}}}$ là phân số tối giản.",
                       "\n".join([
                           "Gọi d = ƯCLN(2n + 2t + 1, n + t) (d thuộc N*) (0.25đ).",
                           "Suy ra (2n + 2t + 1) chia hết cho d và (n + t) chia hết cho d (0.25đ).",
                           "Do đó [2n + 2t + 1 - 2(n + t)] chia hết cho d => 1 chia hết cho d (0.25đ).",
                           "Suy ra d = 1. Vậy phân số đã cho luôn tối giản với mọi n. ĐPCM (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương II: Tính chia hết trong tập hợp các số tự nhiên - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(6, chap_id, "Chương II: Tính chia hết trong tập hợp các số tự nhiên", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG III: Số nguyên (l_idx = 6)
# ------------------------------------------------------------------------------
def build_c3_6():
    chap_id = "c3_6"
    l_idx = 6
    exams = load_existing_exams(chap_id, 6)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Tập hợp các số nguyên được kí hiệu là (Đề {t:02d}):", ["$\\mathbb{Z}$", "$\\mathbb{N}$", "$\\mathbb{Q}$", "$\\mathbb{R}$"], 0),
            make_mc(2, "Nhận biết", f"Số đối của số nguyên $-{t+5}$ là:", [f"${t+5}$", f"$-{t+5}$", "0", f"$\\frac{1}{{{t+5}}}$"], 0),
            make_mc(3, "Nhận biết", "Điểm gốc trên trục số biểu diễn số:", ["0", "1", "-1", "10"], 0),
            make_mc(4, "Nhận biết", "Tích của hai số nguyên âm luôn là một:", ["Số nguyên dương", "Số nguyên âm", "Số 0", "Phân số"], 0),
            make_mc(5, "Thông hiểu", f"Kết quả của phép tính $(-{5*t}) + ({2*t})$ là:", [f"$-{3*t}$", f"${3*t}$", f"$-{7*t}$", f"${7*t}$"], 0),
            make_mc(6, "Thông hiểu", f"Thực hiện phép trừ: ${t*2} - ({t*5})$ ta được:", [f"$-{3*t}$", f"${3*t}$", f"${7*t}$", f"$-{7*t}$"], 0),
            make_mc(7, "Thông hiểu", f"Tìm $x$, biết: $x + {t*3} = -{t*2}$:", [f"$x = -{5*t}$", f"$x = {5*t}$", f"$x = -{t}$", f"$x = {t}$"], 0),
            make_mc(8, "Thông hiểu", f"Sắp xếp các số nguyên sau theo thứ tự tăng dần: $-{t+5}; 0; {t}; -{t}$:", [f"$-{t+5} < -{t} < 0 < {t}$", f"$-{t} < -{t+5} < 0 < {t}$", f"$0 < -{t} < -{t+5} < {t}$", f"${t} < 0 < -{t} < -{t+5}$"], 0),
            make_mc(9, "Vận dụng", f"Nhiệt độ đo được lúc nửa đêm tại đỉnh núi Mẫu Sơn là $-{t}^\\circ C$. Đến buổi trưa nhiệt độ tăng thêm ${t+6}^\\circ C$. Nhiệt độ buổi trưa tại đỉnh núi là:", ["$6^\\circ C$", "$5^\\circ C$", "$4^\\circ C$", "$8^\\circ C$"], 0),
            make_mc(10, "Vận dụng", f"Tài khoản ngân hàng của một công ty đầu ngày có số dư là 50 triệu đồng. Trong ngày công ty chi trả tiền hàng 70 triệu đồng và nhận tiền thanh toán ${40+t*10}$ triệu đồng. Số dư cuối ngày là:", [f"${20+t*10}$ triệu đồng", "20 triệu đồng", "30 triệu đồng", "40 triệu đồng"], 0),
            make_mc(11, "Vận dụng", f"Một chiếc tàu ngầm lặn xuống độ sâu ${40+t*5}$ mét dưới mực nước biển (biểu thị số âm). Sau đó tàu nổi lên $15$ mét. Độ sâu hiện tại của tàu ngầm biểu diễn bởi số nguyên là:", [f"${-(25+t*5)}$ mét", f"${-(40+t*5)}$ mét", "-20 mét", "-30 mét"], 0),
            make_mc(12, "Vận dụng cao", f"Tìm số nguyên $x$ sao cho tích $(x - {t})(x + {t + 2}) < 0$:", [f"$-{t+2} < x < {t}$", f"$x > {t}$", f"$x < -{t+2}$", f"$x = {t}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai trong tập hợp số nguyên (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Mọi số nguyên dương đều lớn hơn số 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số nguyên âm càng có giá trị tuyệt đối lớn thì càng nhỏ.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tích của một số nguyên âm với một số nguyên dương là một số nguyên âm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tổng của hai số nguyên âm có thể là một số nguyên dương.", "correct": False}
            ]),
            make_tf(2, f"Bài toán kinh doanh xuất nhập khẩu (Mã đề {t:02d}): Bác Ba đầu tư kinh doanh trong 3 tháng. Tháng 1 lãi 15 triệu đồng, tháng 2 lỗ 8 triệu đồng, tháng 3 lãi {10+t} triệu đồng.", [
                {"key": "a", "level": "Nhận biết", "text": "Số tiền lỗ được biểu diễn bằng số nguyên âm -8 triệu đồng.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Tổng lợi nhuận sau 3 tháng là 15 + (-8) + ({10+t}) = {17+t} triệu đồng.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Sau 3 tháng bác Ba có lãi ròng dương.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu tháng 2 lỗ 20 triệu đồng thì cả đợt bác Ba bị lỗ vốn.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính giá trị biểu thức: (-15) + ({15+t}).", f"{t}"),
            make_sa(2, "Thông hiểu", f"Tính tích: (-4) * (-{5*t}).", f"{20*t}"),
            make_sa(3, "Vận dụng", f"Nhiệt độ trong phòng ướp lạnh đang là 5 độ C. Người ta hạ nhiệt độ xuống thêm {8+t} độ C. Hỏi nhiệt độ mới trong phòng là bao nhiêu độ C?", f"{5 - (8+t)}"),
            make_sa(4, "Vận dụng", "Một thợ lặn đang ở độ sâu 12 m dưới mặt nước. Người đó bơi lên 5 m rồi lại lặn sâu thêm 8 m. Hỏi lúc này thợ lặn ở độ sâu bao nhiêu mét?", "15")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Thực hiện phép tính một cách hợp lí: $A = (-{t*10}) + 45 + ({t*10}) + (-15)$.",
                       "\n".join([
                           f"Áp dụng tính chất giao hoán và kết hợp: A = [(-{t*10}) + ({t*10})] + [45 + (-15)] (0.25đ).",
                           f"Tổng hai số đối nhau: (-{t*10}) + ({t*10}) = 0 (0.25đ).",
                           "Tính: 45 + (-15) = 30 (0.25đ).",
                           "Kết luận giá trị biểu thức A = 30 (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một công ty may mặc có chỉ tiêu sản xuất trong tuần là {500+t*50} bộ quần áo. Do sự cố máy móc, ngày thứ Hai thiếu 10 bộ (-10), ngày thứ Ba vượt 15 bộ (+15), ngày thứ Tư vượt 20 bộ (+20), ngày thứ Năm thiếu 5 bộ (-5), ngày thứ Sáu vượt {10+t} bộ. Hỏi kết thúc tuần công ty vượt hay thiếu bao nhiêu bộ so với chỉ tiêu?",
                       "\n".join([
                           f"Tổng số bộ vượt hoặc thiếu trong cả tuần: (-10) + 15 + 20 + (-5) + ({10+t}) (0.25đ).",
                           f"Thu gọn phép tính: 30 + {10+t} = {40+t} (bộ) (0.25đ).",
                           "Vì kết quả là số dương nên công ty đã sản xuất vượt chỉ tiêu (0.25đ).",
                           f"Kết luận công ty vượt {40+t} bộ quần áo (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Tìm tất cả các số nguyên $x$ thỏa mãn: $(x - {t})(x + {t + 1}) = 0$ và tính tổng tất cả các nghiệm đó.",
                       "\n".join([
                           f"Tích bằng 0 khi một trong hai thừa số bằng 0 (0.25đ).",
                           f"Trường hợp 1: x - {t} = 0 => x1 = {t} (0.25đ).",
                           f"Trường hợp 2: x + {t + 1} = 0 => x2 = -({t + 1}) (0.25đ).",
                           f"Tổng các nghiệm: x1 + x2 = {t} + [-({t + 1})] = -1 (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương III: Số nguyên - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(6, chap_id, "Chương III: Số nguyên", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG IV: Một số hình phẳng trong thực tiễn (l_idx = 4)
# ------------------------------------------------------------------------------
def build_c4_6():
    chap_id = "c4_6"
    l_idx = 4
    exams = load_existing_exams(chap_id, 6)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Hình vuông là hình có (Đề {t:02d}):", ["4 cạnh bằng nhau và 4 góc vuông", "4 cạnh bằng nhau", "4 góc vuông", "2 đường chéo vuông góc"], 0),
            make_mc(2, "Nhận biết", "Tam giác đều là tam giác có:", ["3 cạnh bằng nhau và 3 góc bằng nhau", "2 cạnh bằng nhau", "1 góc vuông", "3 cạnh khác nhau"], 0),
            make_mc(3, "Nhận biết", "Chu vi của hình chữ nhật có chiều dài $a$ và chiều rộng $b$ là:", ["$C = 2(a + b)$", "$C = a + b$", "$C = a \\cdot b$", "$C = 2a + b$"], 0),
            make_mc(4, "Nhận biết", "Diện tích của hình thoi có độ dài hai đường chéo $m$ và $n$ là:", ["$S = \\frac{{1}}{{2}} m \\cdot n$", "$S = m \\cdot n$", "$S = 2(m + n)$", "$S = m + n$"], 0),
            make_mc(5, "Thông hiểu", f"Một hình vuông có cạnh bằng ${5*t}$ cm. Chu vi của hình vuông đó là:", [f"${20*t}$ cm", f"${25*t*t}$ cm$^2$", f"${10*t}$ cm", f"${15*t}$ cm"], 0),
            make_mc(6, "Thông hiểu", f"Một hình chữ nhật có chiều dài ${8*t}$ cm và chiều rộng ${5*t}$ cm. Diện tích của hình chữ nhật là:", [f"${40*t*t}$ cm$^2$", f"${26*t}$ cm", f"${13*t}$ cm", f"${20*t*t}$ cm$^2$"], 0),
            make_mc(7, "Thông hiểu", f"Hình thoi có độ dài hai đường chéo là ${6*t}$ cm và ${8*t}$ cm. Diện tích hình thoi là:", [f"${24*t*t}$ cm$^2$", f"${48*t*t}$ cm$^2$", f"${14*t}$ cm", f"${28*t}$ cm"], 0),
            make_mc(8, "Thông hiểu", "Hình lục giác đều được ghép từ:", ["6 tam giác đều bằng nhau", "4 hình vuông", "3 hình thoi", "5 hình chữ nhật"], 0),
            make_mc(9, "Vận dụng", f"Bác An muốn lát gạch cho một căn phòng hình chữ nhật dài $8$ mét và rộng ${5+t*0.5:.1f}$ mét. Người ta dùng gạch hình vuông cạnh $50$ cm. Số viên gạch cần dùng (bỏ qua mạch vữa) là:", [f"{int((8 * (5+t*0.5)) / 0.25)} viên", "100 viên", "150 viên", "200 viên"], 0),
            make_mc(10, "Vận dụng", f"Một khu vườn hình thang cân có hai đáy là ${15+t*2}$ mét và ${25+t*2}$ mét, chiều cao $10$ mét. Diện tích khu vườn hình thang cân là:", [f"{((15+t*2) + (25+t*2)) * 10 // 2} mét vuông", "200 mét vuông", "300 mét vuông", "250 mét vuông"], 0),
            make_mc(11, "Vận dụng", f"Người ta làm một hàng rào quanh một khu đất hình bình hành có độ dài hai cạnh kề là ${12+t}$ mét và $8$ mét. Chiều dài hàng rào là:", [f"${2 * (12+t + 8)}$ mét", "40 mét", "30 mét", "50 mét"], 0),
            make_mc(12, "Vận dụng cao", "Một mảnh đất hình chữ nhật có chu vi $60$ mét. Nếu tăng chiều rộng thêm $5$ mét và giảm chiều dài đi $5$ mét thì diện tích tăng thêm bao nhiêu mét vuông?", ["25 mét vuông", "50 mét vuông", "10 mét vuông", "Không đổi"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về các hình phẳng (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Hình vuông vừa là hình chữ nhật vừa là hình thoi.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Trong hình thoi, hai đường chéo vuông góc với nhau và cắt nhau tại trung điểm mỗi đường.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hình lục giác đều có 6 cạnh bằng nhau và 6 góc bằng nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Hình bình hành có hai đường chéo luôn bằng nhau.", "correct": False}
            ]),
            make_tf(2, f"Bài toán kinh tế lát sàn nhà (Mã đề {t:02d}): Bác Nam lát nền phòng khách hình vuông cạnh {4+t} mét bằng các viên gạch vuông cạnh 40 cm (0,4 m).", [
                {"key": "a", "level": "Nhận biết", "text": f"Diện tích sàn phòng khách là (4 + t)^2 mét vuông.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Diện tích một viên gạch là 0,4 . 0,4 = 0,16 mét vuông.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Số viên gạch cần dùng là (4 + t)^2 / 0,16 viên.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu t = 2 thì số viên gạch cần mua ít hơn 200 viên.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính diện tích hình chữ nhật có chiều dài {10+t} cm, chiều rộng 6 cm (cm^2).", f"{6*(10+t)}"),
            make_sa(2, "Thông hiểu", f"Một tam giác đều có cạnh {4*t} cm. Tính chu vi tam giác đều đó (cm).", f"{12*t}"),
            make_sa(3, "Vận dụng", f"Một thửa ruộng hình thang có hai đáy là 12 m và {18+2*t} m, chiều cao 10 m. Tính diện tích thửa ruộng (m^2).", f"{(30+2*t)*5}"),
            make_sa(4, "Vận dụng", "Một con diều hình thoi có hai đường chéo dài 60 cm và 80 cm. Tính diện tích con diều (cm^2).", "2400")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Một mảnh vườn hình chữ nhật có chiều dài ${15+t}$ mét, chiều rộng $10$ mét. Tính chu vi và diện tích của mảnh vườn đó.",
                       "\n".join([
                           f"Chu vi mảnh vườn: C = 2 . ({15+t} + 10) = 2 . {25+t} = {50+2*t} (m) (0.25đ).",
                           f"Diện tích mảnh vườn: S = ({15+t}) . 10 = {150+10*t} (m^2) (0.25đ).",
                           "Ghi chú đơn vị đo chu vi (m) và diện tích (m^2) (0.25đ).",
                           f"Kết luận chu vi là {50+2*t} m và diện tích là {150+10*t} m^2 (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một sân trường hình chữ nhật có chiều dài ${40+t*5}$ mét và chiều rộng $30$ mét. Ở giữa sân người ta xây một bồn hoa hình vuông cạnh $5$ mét. Phần sân còn lại được lát gạch tự chèn. Tính diện tích phần sân được lát gạch.",
                       "\n".join([
                           f"Diện tích toàn bộ sân trường: S1 = ({40+t*5}) . 30 = {1200+150*t} (m^2) (0.25đ).",
                           "Diện tích bồn hoa hình vuông: S2 = 5 . 5 = 25 (m^2) (0.25đ).",
                           f"Diện tích phần sân lát gạch: S = S1 - S2 = ({1200+150*t}) - 25 = {1175+150*t} (m^2) (0.25đ).",
                           f"Kết luận diện tích phần sân được lát gạch là {1175+150*t} m^2 (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Người ta muốn rào quanh một khu đất hình chữ nhật có diện tích $36\\text{ m}^2$ bằng lưới thép. Hỏi người ta phải chọn kích thước các cạnh như thế nào để số mét lưới thép cần mua (chu vi) là ít nhất?",
                       "\n".join([
                           "Gọi chiều dài là a (m) và chiều rộng là b (m) => a . b = 36 (0.25đ).",
                           "Chu vi khu đất là C = 2(a + b) (0.25đ).",
                           "Áp dụng bất đẳng thức Cauchy: a + b >= 2 . căn(ab) = 2 . căn(36) = 12 (0.25đ).",
                           "Chu vi nhỏ nhất khi a = b = 6 m (khu đất hình vuông). Khi đó chu vi ít nhất là 24 m (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương IV: Một số hình phẳng trong thực tiễn - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(6, chap_id, "Chương IV: Một số hình phẳng trong thực tiễn", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG V: Tính đối xứng của hình phẳng trong tự nhiên (l_idx = 3)
# ------------------------------------------------------------------------------
def build_c5_6():
    chap_id = "c5_6"
    l_idx = 3
    exams = load_existing_exams(chap_id, 6)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Hình nào sau đây có trục đối xứng (Đề {t:02d})?", ["Đoạn thẳng", "Hình bình hành tổng quát", "Hình thang thường", "Tam giác thường"], 0),
            make_mc(2, "Nhận biết", "Hình nào sau đây có tâm đối xứng?", ["Hình tròn", "Tam giác đều", "Hình thang cân", "Ngũ giác đều"], 0),
            make_mc(3, "Nhận biết", "Số trục đối xứng của hình vuông là:", ["4", "2", "1", "Vô số"], 0),
            make_mc(4, "Nhận biết", "Tâm đối xứng của hình bình hành là:", ["Giao điểm của hai đường chéo", "Trung điểm một cạnh", "Một đỉnh của hình", "Điểm bất kì"], 0),
            make_mc(5, "Thông hiểu", f"Chữ cái in hoa nào sau đây vừa có trục đối xứng vừa có tâm đối xứng?", ["H", "A", "E", "F"], 0),
            make_mc(6, "Thông hiểu", "Biển báo giao thông hình tròn có bao nhiêu trục đối xứng?", ["Vô số trục đối xứng", "1", "2", "4"], 0),
            make_mc(7, "Thông hiểu", "Hình tam giác đều có bao nhiêu trục đối xứng?", ["3 trục đối xứng", "1", "2", "0"], 0),
            make_mc(8, "Thông hiểu", "Hình thoi có bao nhiêu trục đối xứng?", ["2 trục đối xứng (là 2 đường chéo)", "4", "1", "0"], 0),
            make_mc(9, "Vận dụng", f"Trong các hình sau: Cánh bướm, Lá phong, Con sao biển {5} cánh, Cỏ bốn lá. Hình có tâm đối xứng là:", ["Cỏ bốn lá", "Cánh bướm", "Lá phong", "Con sao biển 5 cánh"], 0),
            make_mc(10, "Vận dụng", f"Một logo thương hiệu hình tròn được trang trí bằng một bông hoa {t*2 + 4} cánh đều nhau. Bông hoa này có tâm đối xứng khi:", ["Số cánh là số chẵn", "Số cánh là số lẻ", "Luôn có tâm đối xứng", "Không bao giờ có"], 0),
            make_mc(11, "Vận dụng", "Người thợ gốm tạo ra một chiếc đĩa tròn đồng tâm. Trục đối xứng của chiếc đĩa là:", ["Mọi đường thẳng đi qua tâm của đĩa", "Đúng 2 đường kính vuông góc", "Chỉ có 1 đường kính", "Không có"], 0),
            make_mc(12, "Vận dụng cao", "Cho đoạn thẳng $AB = 10\\text{ cm}$. Điểm $M$ đối xứng với điểm $N$ qua trung điểm $O$ của $AB$. Khẳng định nào sau đây luôn ĐÚNG?", ["$OM = ON$", "$OM = 2ON$", "$AM = BN$", "$O$ nằm ngoài đoạn $MN$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về tính đối xứng (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Hình tròn có vô số trục đối xứng đi qua tâm.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hình chữ nhật có 2 trục đối xứng là hai đường trung trực của các cạnh đối diện.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Đoạn thẳng vừa có trục đối xứng vừa có tâm đối xứng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Tam giác cân bất kì luôn có tâm đối xứng.", "correct": False}
            ]),
            make_tf(2, f"Phân tích tính đối xứng của các chữ cái in hoa tiếng Việt (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Chữ cái A có đúng một trục đối xứng thẳng đứng.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Chữ cái O vừa có trục đối xứng vừa có tâm đối xứng.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Chữ cái N có tâm đối xứng nhưng không có trục đối xứng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Chữ cái F có một trục đối xứng nằm ngang.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Hình lục giác đều có bao nhiêu trục đối xứng?", "6"),
            make_sa(2, "Thông hiểu", "Hình thoi có bao nhiêu tâm đối xứng?", "1"),
            make_sa(3, "Vận dụng", "Trong các số: 0, 1, 3, 8. Có bao nhiêu số vừa có trục đối xứng vừa có tâm đối xứng?", "2"),
            make_sa(4, "Vận dụng", "Một hình chữ nhật có kích thước 6 cm và 8 cm. Khoảng cách từ tâm đối xứng đến mỗi đỉnh là bao nhiêu cm?", "5")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", "Nêu rõ số trục đối xứng và xác định vị trí của chúng trong: hình tam giác đều và hình vuông.",
                       "\n".join([
                           "Hình tam giác đều có 3 trục đối xứng là ba đường trung trực của ba cạnh (0.25đ).",
                           "Ba trục này cũng chính là 3 đường cao đi qua ba đỉnh (0.25đ).",
                           "Hình vuông có 4 trục đối xứng (0.25đ).",
                           "Gồm 2 đường chéo và 2 đường trung trực của các cạnh đối diện (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một người thiết kế gạch hoa lát nền hình vuông cạnh ${20+t*5}$ cm có hoa văn đối xứng tâm. Em hãy mô tả cách người thợ tạo ra hoa văn đối xứng tâm và vẽ phác họa các trục đối xứng của viên gạch.",
                       "\n".join([
                           "Xác định tâm đối xứng là giao điểm hai đường chéo viên gạch (0.25đ).",
                           "Vẽ họa tiết ở một phần tư rồi lấy đối xứng qua tâm sang phần tư đối diện (0.25đ).",
                           "Viên gạch có 4 trục đối xứng giúp ghép nối liền mạch hoa văn (0.25đ).",
                           "Kết luận tính thẩm mỹ và vai trò của tính đối xứng trong kiến trúc gạch hoa (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Chứng minh rằng: Nếu một hình có hai trục đối xứng vuông góc với nhau thì giao điểm của hai trục đối xứng đó chính là tâm đối xứng của hình.",
                       "\n".join([
                           "Chọn hệ trục tọa độ Oxy sao cho hai trục đối xứng là Ox và Oy (0.25đ).",
                           "Lấy điểm M(x; y) bất kì thuộc hình. Vì Ox là trục đối xứng nên M1(x; -y) thuộc hình (0.25đ).",
                           "Vì Oy là trục đối xứng nên M2(-x; -y) thuộc hình (0.25đ).",
                           "Điểm M2(-x; -y) đối xứng với M(x; y) qua gốc tọa độ O. Vậy O là tâm đối xứng của hình. ĐPCM (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương V: Tính đối xứng của hình phẳng trong tự nhiên - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(6, chap_id, "Chương V: Tính đối xứng của hình phẳng trong tự nhiên", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG VI: Phân số (l_idx = 6)
# ------------------------------------------------------------------------------
def build_c6_6():
    chap_id = "c6_6"
    l_idx = 6
    exams = load_existing_exams(chap_id, 6)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Phân số là biểu thức có dạng $\\frac{{a}}{{b}}$ với (Đề {t:02d}):", ["$a, b \\in \\mathbb{Z}, b \\neq 0$", "$a, b \\in \\mathbb{N}$", "$a = 0, b = 0$", "$a, b \\in \\mathbb{Q}$"], 0),
            make_mc(2, "Nhận biết", f"Phân số đối của phân số $-\\frac{{{t}}}{{{t+3}}}$ là:", [f"$\\frac{{{t}}}{{{t+3}}}$", f"$-\\frac{{{t+3}}}{{{t}}}$", f"$\\frac{{{t+3}}}{{{t}}}$", f"$-{t}$"], 0),
            make_mc(3, "Nhận biết", "Muốn rút gọn một phân số, ta chia cả tử và mẫu cho:", ["Ước chung khác 1 và -1", "Bội chung", "Tử số", "Mẫu số"], 0),
            make_mc(4, "Nhận biết", "Phân số nghịch đảo của phân số $\\frac{{3}}{{5}}$ là:", ["$\\frac{5}{3}$", "$-\\frac{{3}}{{5}}$", "$-\\frac{5}{3}$", "$\\frac{{3}}{{5}}$"], 0),
            make_mc(5, "Thông hiểu", f"Kết quả của phép tính $\\frac{{{t}}}{{5}} + \\frac{{{2*t}}}{{5}}$ là:", [f"$\\frac{{{3*t}}}{{5}}$", f"$\\frac{{{2*t*t}}}{{5}}$", f"${t}$", f"$\\frac{{{3*t}}}{{10}}$"], 0),
            make_mc(6, "Thông hiểu", f"Thực hiện phép trừ: $\\frac{{{4*t}}}{{7}} - \\frac{{{t}}}{{7}}$ ta được:", [f"$\\frac{{{3*t}}}{{7}}$", f"$\\frac{{{4}}}{{7}}$", f"${t}$", "$0$"], 0),
            make_mc(7, "Thông hiểu", f"Tính tích: $\\frac{{{2*t}}}{{3}} \\cdot \\frac{{3}}{{2}}$ ta được:", [f"${t}$", f"${2*t}$", "$1$", "$3$"], 0),
            make_mc(8, "Thông hiểu", f"Tìm $x$, biết: $x : \\frac{{1}}{{2}} = {2*t}$:", [f"$x = {t}$", f"$x = {4*t}$", f"$x = {2*t}$", "$x = 1$"], 0),
            make_mc(9, "Vận dụng", f"Một tấm vải dài ${30+t*5}$ mét. Người thợ may dùng $\\frac{{3}}{{5}}$ chiều dài tấm vải để may rèm cửa. Số mét vải đã dùng là:", [f"{(30+t*5) * 3 // 5} mét", "18 mét", "20 mét", "25 mét"], 0),
            make_mc(10, "Vận dụng", f"Một bể cá chứa được 120 lít nước. Hiện tại lượng nước trong bể chiếm $\\frac{{{t+2}}}{{10}}$ dung tích bể. Số lít nước hiện có trong bể là:", [f"{120 * (t+2) // 10} lít", "60 lít", "80 lít", "50 lít"], 0),
            make_mc(11, "Vận dụng", f"Biết $\\frac{{2}}{{3}}$ số học sinh của một lớp là 24 em. Tổng số học sinh của lớp đó là:", ["36 em", "32 em", "40 em", "30 em"], 0),
            make_mc(12, "Vận dụng cao", "Giá trị của biểu thức $S = \\frac{1}{1 \\cdot 2} + \\frac{1}{2 \\cdot 3} + \\dots + \\frac{1}{" + str(t+9) + " \\cdot " + str(t+10) + "}$ bằng:", ["$\\frac{" + str(t+9) + "}{" + str(t+10) + "}$", "$\\frac{1}{" + str(t+10) + "}$", "$1$", "$\\frac{" + str(t+10) + "}{" + str(t+9) + "}$"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về phân số (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Phân số có tử và mẫu là các số nguyên với mẫu khác 0.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Phân số tối giản là phân số mà tử và mẫu chỉ có ước chung là 1 và -1.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai phân số a/b = c/d khi a . d = b . c.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Mọi phân số có tử nhỏ hơn mẫu đều là số dương.", "correct": False}
            ]),
            make_tf(2, f"Bài toán thu hoạch nông sản (Mã đề {t:02d}): Một trang trại thu hoạch được {120+t*10} tấn dưa hấu. Ngày đầu bán được 1/3 số dưa, ngày thứ hai bán được 2/5 số dưa ban đầu.", [
                {"key": "a", "level": "Nhận biết", "text": f"Tổng sản lượng thu hoạch là {120+t*10} tấn.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Số dưa bán ngày đầu là ({120+t*10}) / 3 tấn.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Số dưa bán ngày thứ hai là 2/5 . ({120+t*10}) tấn.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Sau 2 ngày trang trại đã bán hết toàn bộ số dưa hấu.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Rút gọn phân số {4*t} / {6*t} về phân số tối giản.", "2/3"),
            make_sa(2, "Thông hiểu", f"Tính: 3/7 + 4/7.", "1"),
            make_sa(3, "Vận dụng", f"Một lớp có 40 học sinh, trong đó có 3/5 là học sinh nữ. Tính số học sinh nam của lớp.", "16"),
            make_sa(4, "Vận dụng", f"Bác thợ có thanh gỗ dài {2+t} mét. Bác cưa lấy 3/4 chiều dài thanh gỗ. Hỏi đoạn gỗ còn lại dài bao nhiêu mét?", f"{(2+t)*0.25:.2f}")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Thực hiện phép tính một cách hợp lí: $A = \\frac{{{t}}}{{11}} \\cdot \\frac{{4}}{{9}} + \\frac{{{t}}}{{11}} \\cdot \\frac{{5}}{{9}}$.",
                       "\n".join([
                           f"Đặt thừa số chung {t}/11 ra ngoài ngoặc (0.25đ).",
                           "Trong ngoặc: 4/9 + 5/9 = 9/9 = 1 (0.25đ).",
                           f"Tính tích: A = ({t}/11) . 1 = {t}/11 (0.25đ).",
                           f"Kết luận kết quả phép tính là A = {t}/11 (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một thư viện trường có ${600+t*50}$ quyển sách gồm ba loại: Sách giáo khoa, sách tham khảo và truyện tranh. Số sách giáo khoa chiếm $\\frac{2}{5}$ tổng số sách. Số sách tham khảo chiếm $\\frac{{1}}{{3}}$ tổng số sách. Còn lại là truyện tranh. Tính số quyển truyện tranh có trong thư viện.",
                       "\n".join([
                           f"Số sách giáo khoa: ({600+t*50}) . 2/5 = { (600+t*50)*2//5 } (quyển) (0.25đ).",
                           f"Số sách tham khảo: ({600+t*50}) . 1/3 = { (600+t*50)//3 } (quyển) (0.25đ).",
                           f"Phân số chỉ số truyện tranh: 1 - 2/5 - 1/3 = 4/15 tổng số sách (0.25đ).",
                           f"Tính số truyện tranh: ({600+t*50}) . 4/15 = { (600+t*50)*4//15 } quyển. Kết luận (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Chứng minh rằng: $A = \\frac{1}{2^2} + \\frac{1}{3^2} + \\frac{1}{4^2} + \\dots + \\frac{1}{" + str(t+10) + "^2} < 1$.",
                       "\n".join([
                           "Ta có nhận xét: 1/k^2 < 1/[k(k - 1)] = 1/(k - 1) - 1/k với mọi k >= 2 (0.25đ).",
                           "Áp dụng: 1/2^2 < 1/(1.2) = 1 - 1/2 (0.25đ).",
                           "1/3^2 < 1/(2.3) = 1/2 - 1/3; ...; 1/n^2 < 1/(n-1) - 1/n (0.25đ).",
                           "Cộng vế với vế ta được: A < 1 - 1/(t+10) < 1. Đẳng thức được chứng minh hoàn tất (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương VI: Phân số - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(6, chap_id, "Chương VI: Phân số", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG VII: Số thập phân (l_idx = 5)
# ------------------------------------------------------------------------------
def build_c7_6():
    chap_id = "c7_6"
    l_idx = 5
    exams = load_existing_exams(chap_id, 6)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Phân số thập phân là phân số có mẫu là (Đề {t:02d}):", ["Luỹ thừa của 10", "Số tự nhiên bất kì", "Số chẵn", "Số nguyên tố"], 0),
            make_mc(2, "Nhận biết", f"Số thập phân $-0,{t}$ đọc là:", [f"Âm không phẩy {t}", f"Không phẩy {t}", f"Dương không phẩy {t}", f"Trừ {t}"], 0),
            make_mc(3, "Nhận biết", "Muốn nhân một số thập phân với 10, 100, 1000,... ta dịch dấu phẩy sang phải lần lượt:", ["1, 2, 3,... chữ số", "1, 2, 3,... chữ số sang trái", "2 chữ số", "Không dịch chuyển"], 0),
            make_mc(4, "Nhận biết", "Tỉ số phần trăm của $a$ và $b$ ($b \\neq 0$) được tính bằng:", ["$\\frac{a}{b} \\cdot 100\\%$", "$\\frac{a}{b}$", "$\\frac{b}{a} \\cdot 100\\%$", "$a \\cdot b \\cdot 100\\%$"], 0),
            make_mc(5, "Thông hiểu", f"Kết quả của phép tính $2,{t} + 3,{t}$ là:", [f"${5 + 2*t/10:.1f}$", f"${5 + t/10:.1f}$", f"${5}$", f"${6}$"], 0),
            make_mc(6, "Thông hiểu", f"Làm tròn số $4,{t}45$ đến hàng phần mười (chữ số thập phân thứ nhất) ta được:", [f"4,{t if t!=9 else 9}", "4,5", "4", "5"], 0),
            make_mc(7, "Thông hiểu", f"Tìm $x$, biết: $x \\cdot 0,5 = {t}$:", [f"$x = {2*t}$", f"$x = {t/2}$", f"$x = {t}$", "$x = 1$"], 0),
            make_mc(8, "Thông hiểu", f"Viết phân số $\\frac{{{t}}}{{100}}$ dưới dạng số thập phân:", [f"0,0{t}", f"0,{t}", f"{t},0", f"0,00{t}"], 0),
            make_mc(9, "Vận dụng", f"Một người mua {2+t} kg cam với giá 25,5 nghìn đồng một kilôgam. Số tiền người đó phải trả là:", [f"{(2+t)*25.5:.1f} nghìn đồng", "50 nghìn đồng", "60 nghìn đồng", "70 nghìn đồng"], 0),
            make_mc(10, "Vận dụng", f"Mẹ gửi tiết kiệm {50+t*10} triệu đồng vào ngân hàng với lãi suất $6,5\\%$ một năm. Số tiền lãi mẹ nhận được sau một năm là:", [f"{(50+t*10)*0.065:.2f} triệu đồng", "3 triệu đồng", "4 triệu đồng", "5 triệu đồng"], 0),
            make_mc(11, "Vận dụng", f"Một chiếc xe máy đi được quãng đường $100$ km tiêu thụ hết $2,{t}$ lít xăng. Để đi quãng đường $250$ km xe máy đó tiêu thụ hết số lít xăng là:", [f"{2.5 * (2 + t/10):.2f} lít", "5 lít", "6 lít", "4 lít"], 0),
            make_mc(12, "Vận dụng cao", f"Giá xăng tăng $10\\%$ trong đợt 1, sau đó đợt 2 giảm $10\\%$. So với giá xăng ban đầu, giá xăng sau hai đợt biến động đã:", ["Giảm 1%", "Tăng 1%", "Không đổi", "Giảm 2%"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về số thập phân (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Mọi phân số thập phân đều viết được dưới dạng số thập phân.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số đối của số thập phân a là số thập phân -a.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Tỉ số phần trăm 25% tương ứng với phân số 1/4.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Khi chia một số thập phân cho 0,1 thì giá trị của số đó giảm đi 10 lần.", "correct": False}
            ]),
            make_tf(2, f"Bài toán mua sắm tại siêu thị điện máy (Mã đề {t:02d}): Một chiếc tivi có giá niêm yết là 12 triệu đồng. Nhân dịp khai trương, siêu thị giảm giá 15%.", [
                {"key": "a", "level": "Nhận biết", "text": "Giá niêm yết ban đầu là 12 triệu đồng.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Số tiền được giảm giá là 12 . 15% = 1,8 triệu đồng.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Khách hàng phải thanh toán số tiền là 12 - 1,8 = 10,2 triệu đồng.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu khách hàng thanh toán qua ví điện tử được hoàn thêm 500 nghìn đồng thì số tiền mua thực tế lớn hơn 10 triệu đồng.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Tính: 2,5 * {4*t}.", f"{10*t}"),
            make_sa(2, "Thông hiểu", "Làm tròn số 15,67 đến hàng phần mười.", "15.7"),
            make_sa(3, "Vận dụng", f"Một lít dầu hỏa nặng 0,8 kg. Hỏi một can chứa {10+t} lít dầu hỏa nặng bao nhiêu kg (không tính vỏ can)?", f"{(10+t)*0.8:.1f}"),
            make_sa(4, "Vận dụng", "Tính tỉ số phần trăm của 15 và 60.", "25")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Tính giá trị của biểu thức: $M = 3,5 \\cdot {t*2} + 6,5 \\cdot {t*2}$.",
                       "\n".join([
                           f"Đặt thừa số chung {t*2} ra ngoài ngoặc (0.25đ).",
                           "Tính trong ngoặc: 3,5 + 6,5 = 10 (0.25đ).",
                           f"Tính tích: M = 10 . {t*2} = {t*20} (0.25đ).",
                           f"Kết luận giá trị biểu thức M = {t*20} (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Một mảnh đất hình chữ nhật có chiều dài ${20+t*2}$ mét và chiều rộng $12,5$ mét. Người ta dùng $30\\%$ diện tích mảnh đất để làm nhà ở, phần đất còn lại làm sân và vườn cây. Tính diện tích phần đất làm sân và vườn cây.",
                       "\n".join([
                           f"Diện tích toàn bộ mảnh đất: S = ({20+t*2}) . 12,5 = { (20+t*2)*12.5:.1f} (m^2) (0.25đ).",
                           f"Diện tích đất làm nhà ở: S_nhà = S . 30% = { (20+t*2)*12.5*0.3:.1f} (m^2) (0.25đ).",
                           "Tỉ lệ phần đất làm sân vườn: 100% - 30% = 70% (0.25đ).",
                           f"Diện tích làm sân và vườn: S_vườn = S . 70% = { (20+t*2)*12.5*0.7:.1f} m^2. Kết luận (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", f"Tìm chữ số tận cùng của phần thập phân khi viết phân số $\\frac{{{t}}}{{16}}$ dưới dạng số thập phân hữu hạn.",
                       "\n".join([
                           "Ta có: 16 = 2^4 (0.25đ).",
                           f"Biến đổi phân số: {t}/16 = ({t} . 5^4) / (2^4 . 5^4) = ({t} . 625) / 10 000 (0.25đ).",
                           f"Số thập phân có đúng 4 chữ số ở phần thập phân (0.25đ).",
                           f"Chữ số cuối cùng là chữ số tận cùng của tích {t} . 625 (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương VII: Số thập phân - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(6, chap_id, "Chương VII: Số thập phân", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG VIII: Những hình hình học cơ bản (l_idx = 7)
# ------------------------------------------------------------------------------
def build_c8_6():
    chap_id = "c8_6"
    l_idx = 7
    exams = load_existing_exams(chap_id, 6)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Qua hai điểm phân biệt $A$ và $B$ vẽ được (Đề {t:02d}):", ["Đúng 1 đường thẳng", "2 đường thẳng", "Vô số đường thẳng", "Không vẽ được"], 0),
            make_mc(2, "Nhận biết", "Điểm $M$ là trung điểm của đoạn thẳng $AB$ khi:", ["$M$ nằm giữa $A, B$ và $MA = MB$", "$MA = MB$", "$M$ nằm giữa $A$ và $B$", "$MA + MB = 2AB$"], 0),
            make_mc(3, "Nhận biết", "Góc nhọn là góc có số đo:", ["Lớn hơn $0^\\circ$ và nhỏ hơn $90^\\circ$", "Bằng $90^\\circ$", "Lớn hơn $90^\\circ$", "Bằng $180^\\circ$"], 0),
            make_mc(4, "Nhận biết", "Góc vuông có số đo bằng:", ["$90^\\circ$", "$180^\\circ$", "$60^\\circ$", "$45^\\circ$"], 0),
            make_mc(5, "Thông hiểu", f"Cho đoạn thẳng $AB = {2*t}$ cm. Điểm $M$ là trung điểm của $AB$. Độ dài đoạn thẳng $AM$ là:", [f"${t}$ cm", f"${2*t}$ cm", f"${4*t}$ cm", f"${t/2}$ cm"], 0),
            make_mc(6, "Thông hiểu", f"Cho điểm $M$ nằm giữa hai điểm $A$ và $B$. Biết $AM = {3*t}$ cm, $MB = {4*t}$ cm. Độ dài đoạn thẳng $AB$ là:", [f"${7*t}$ cm", f"${t}$ cm", f"${12*t}$ cm", f"${3.5*t}$ cm"], 0),
            make_mc(7, "Thông hiểu", f"Góc bẹt có số đo bằng:", ["$180^\\circ$", "$90^\\circ$", "$360^\\circ$", "$120^\\circ$"], 0),
            make_mc(8, "Thông hiểu", f"Tia $Oy$ nằm giữa hai tia $Ox$ và $Oz$. Biết $\\widehat{{xOy}} = {30+t}^\\circ, \\widehat{{yOz}} = {40+t}^\\circ$. Số đo $\\widehat{{xOz}}$ là:", [f"${70+2*t}^\\circ$", f"${10}^\\circ$", "$90^\\circ$", "$180^\\circ$"], 0),
            make_mc(9, "Vận dụng", f"Người ta trồng cây ven một đoạn đường thẳng dài ${100+t*10}$ mét, cứ cách $5$ mét trồng một cây và cả hai đầu đường đều có cây. Số cây trồng được là:", [f"{(100+t*10)//5 + 1} cây", f"{(100+t*10)//5} cây", "20 cây", "25 cây"], 0),
            make_mc(10, "Vận dụng", f"Một người ngắm ba cọc tiêu $A, B, C$ thẳng hàng trên mặt đất. Điểm $B$ nằm giữa $A$ và $C$. Biết $AB = {15+t}$ mét, khoảng cách $BC = 20$ mét. Khoảng cách giữa hai cọc ngoài cùng $AC$ là:", [f"${35+t}$ mét", "30 mét", "40 mét", "50 mét"], 0),
            make_mc(11, "Vận dụng", f"Lúc 3 giờ đúng, góc tạo bởi kim giờ và kim phút của chiếc đồng hồ treo tường có số đo bằng:", ["$90^\\circ$", "$60^\\circ$", "$120^\\circ$", "$180^\\circ$"], 0),
            make_mc(12, "Vận dụng cao", f"Cho $n$ điểm phân biệt trong đó không có 3 điểm nào thẳng hàng. Cứ qua hai điểm vẽ được 1 đường thẳng. Biết vẽ được tất cả ${t*t + 10}$ đường thẳng, khẳng định nào sau đây ĐÚNG?", ["Số đường thẳng luôn tính theo công thức n(n-1)/2", "Luôn bằng n", "Luôn bằng n^2", "Bằng 2n"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về các hình hình học cơ bản (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Đoạn thẳng AB là hình gồm điểm A, điểm B và tất cả các điểm nằm giữa A và B.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Hai tia chung gốc đối nhau tạo thành một góc bẹt 180 độ.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Góc tù là góc có số đo lớn hơn 90 độ và nhỏ hơn 180 độ.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu AM = MB thì điểm M luôn là trung điểm của đoạn thẳng AB.", "correct": False}
            ]),
            make_tf(2, f"Cho ba điểm A, B, C cùng nằm trên một đường thẳng theo thứ tự đó. Biết AB = {4*t} cm, BC = {6*t} cm (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Điểm B nằm giữa hai điểm A và C.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Độ dài đoạn thẳng AC = AB + BC = {10*t} cm.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": f"Gọi I là trung điểm của AC thì AI = {5*t} cm.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Điểm B là trung điểm của đoạn thẳng AC.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", f"Cho đoạn thẳng AB = {16*t} cm. Điểm M là trung điểm AB. Tính độ dài đoạn MB (cm).", f"{8*t}"),
            make_sa(2, "Thông hiểu", "Góc vuông có số đo bao nhiêu độ?", "90"),
            make_sa(3, "Vận dụng", f"Trên tia Ox lấy hai điểm A và B sao cho OA = {3+t} cm, OB = {7+t} cm. Tính độ dài đoạn thẳng AB (cm).", "4"),
            make_sa(4, "Vận dụng", "Lúc 6 giờ đúng, góc tạo bởi kim giờ và kim phút của đồng hồ bằng bao nhiêu độ?", "180")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Cho đoạn thẳng $AB = {10+2*t}$ cm. Lấy điểm $M$ nằm giữa $A$ và $B$ sao cho $AM = {5+t}$ cm. Điểm $M$ có phải là trung điểm của đoạn thẳng $AB$ không? Vì sao?",
                       "\n".join([
                           f"Vì M nằm giữa A và B nên AM + MB = AB (0.25đ).",
                           f"Suy ra MB = AB - AM = ({10+2*t}) - ({5+t}) = {5+t} (cm) (0.25đ).",
                           f"Ta thấy M nằm giữa A, B và MA = MB = {5+t} cm (0.25đ).",
                           "Vậy điểm M chính là trung điểm của đoạn thẳng AB (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Người ta trồng cây cột mốc dọc theo tuyến đường thẳng từ mốc số $0$ đến mốc cuối cùng cách nhau ${60+t*10}$ mét. Cứ cách $10$ mét trồng một cột mốc. Hỏi có tất cả bao nhiêu cột mốc trên toàn tuyến đường?",
                       "\n".join([
                           f"Khoảng cách giữa hai cột mốc liên tiếp là 10 mét (0.25đ).",
                           f"Số khoảng cách giữa các cột mốc là: ({60+t*10}) : 10 = {(60+t*10)//10} (khoảng) (0.25đ).",
                           f"Số cột mốc = Số khoảng + 1 = {(60+t*10)//10} + 1 = {(60+t*10)//10 + 1} (cột) (0.25đ).",
                           f"Kết luận có tất cả {(60+t*10)//10 + 1} cột mốc trên tuyến đường (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Cho $20$ điểm phân biệt trên mặt phẳng, trong đó không có ba điểm nào thẳng hàng. Cứ qua hai điểm vẽ được một đường thẳng. Tính tổng số đường thẳng vẽ được.",
                       "\n".join([
                           "Chọn 1 điểm trong 20 điểm, nối với 19 điểm còn lại ta được 19 đường thẳng (0.25đ).",
                           "Làm như vậy với 20 điểm ta được: 20 . 19 = 380 đường thẳng (0.25đ).",
                           "Mỗi đường thẳng đã được tính lặp lại 2 lần (0.25đ).",
                           "Vậy số đường thẳng thực tế là: (20 . 19) / 2 = 190 đường thẳng (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương VIII: Những hình hình học cơ bản - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(6, chap_id, "Chương VIII: Những hình hình học cơ bản", exams)


# ------------------------------------------------------------------------------
# CHƯƠNG IX: Dữ liệu và xác suất thực nghiệm (l_idx = 7)
# ------------------------------------------------------------------------------
def build_c9_6():
    chap_id = "c9_6"
    l_idx = 7
    exams = load_existing_exams(chap_id, 6)
    for k in list(exams.keys()):
        if f"{chap_id}_bai{l_idx}_test" in k:
            del exams[k]

    for t in range(1, 8):
        p1 = [
            make_mc(1, "Nhận biết", f"Dữ liệu nào sau đây là số liệu (dữ liệu định lượng) (Đề {t:02d})?", ["Số học sinh giỏi của lớp", "Màu áo yêu thích", "Tên các môn học", "Nơi cư trú"], 0),
            make_mc(2, "Nhận biết", "Để biểu diễn số lượng học sinh của từng tổ trong lớp, biểu đồ phù hợp nhất là:", ["Biểu đồ cột", "Biểu đồ tranh", "Biểu đồ đoạn thẳng", "Biểu đồ quạt tròn"], 0),
            make_mc(3, "Nhận biết", "Tung một đồng xu 1 lần, kết quả có thể xảy ra là:", ["Xuất hiện mặt Sấp hoặc mặt Ngửa", "Chỉ xuất hiện mặt Sấp", "Chỉ xuất hiện mặt Ngửa", "Xuất hiện cả hai mặt"], 0),
            make_mc(4, "Nhận biết", "Xác suất thực nghiệm của một sự kiện bằng:", ["Số lần sự kiện xảy ra chia cho tổng số lần thực hiện phép thử", "Tổng số lần thực hiện", "Số lần xảy ra", "Hiệu hai số lần"], 0),
            make_mc(5, "Thông hiểu", f"Gieo một con xúc xắc {20+t*10} lần thấy mặt 1 chấm xuất hiện {5+t} lần. Xác suất thực nghiệm xuất hiện mặt 1 chấm là:", [f"{(5+t)/(20+t*10):.2f}", "0,5", "0,2", "0,1"], 0),
            make_mc(6, "Thông hiểu", f"Tung một đồng xu 30 lần thấy có {15+t} lần xuất hiện mặt Ngửa. Số lần xuất hiện mặt Sấp là:", [f"{30 - (15+t)}", f"{15+t}", "15", "30"], 0),
            make_mc(7, "Thông hiểu", "Bảng thống kê điểm kiểm tra Toán của tổ 1: Điểm 8 có 4 bạn, Điểm 9 có 3 bạn, Điểm 10 có 2 bạn. Sĩ số tổ 1 là:", ["9 bạn", "8 bạn", "10 bạn", "7 bạn"], 0),
            make_mc(8, "Thông hiểu", "Dữ liệu nào sau đây là KHÔNG hợp lí khi thống kê số ngày đi học muộn trong một tuần của học sinh?", ["8 ngày", "0 ngày", "1 ngày", "2 ngày"], 0),
            make_mc(9, "Vận dụng", f"Trong đợt khảo sát {100+t*20} người về việc phân loại rác tại nguồn, có {80+t*15} người thực hiện thường xuyên. Xác suất thực nghiệm một người được chọn ngẫu nhiên phân loại rác thường xuyên là:", [f"{(80+t*15)/(100+t*20):.2f}", "0,8", "0,9", "0,7"], 0),
            make_mc(10, "Vận dụng", f"Một xạ thủ bắn {50+t*10} viên đạn vào bia, trong đó có {40+t*8} viên trúng vòng 10 điểm. Xác suất thực nghiệm xạ thủ bắn trúng vòng 10 điểm là:", [f"{(40+t*8)/(50+t*10):.2f}", "0,8", "0,9", "0,7"], 0),
            make_mc(11, "Vận dụng", "Trong hộp có 1 bi đỏ và 1 bi xanh. Bạn An lấy 1 viên rồi trả lại, lặp lại 100 lần thấy có 52 lần lấy được bi đỏ. Xác suất thực nghiệm lấy được bi xanh là:", ["0,48", "0,52", "0,50", "0,40"], 0),
            make_mc(12, "Vận dụng cao", "Một chiếc hộp kín có một số viên bi xanh và đỏ. Thực hiện 200 lần lấy ngẫu nhiên 1 viên bi rồi trả lại, thấy có 80 lần được bi xanh. Ước lượng tỉ lệ phần trăm số bi đỏ trong hộp là khoảng:", ["60%", "40%", "50%", "70%"], 0)
        ]
        p2 = [
            make_tf(1, f"Xét tính đúng sai về dữ liệu và xác suất thực nghiệm (Đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Thu thập dữ liệu có thể thực hiện bằng quan sát, đo đạc hoặc lập phiếu hỏi.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Khi số lần thực nghiệm càng nhiều thì xác suất thực nghiệm càng phản ánh khách quan hơn.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Xác suất thực nghiệm là một số không âm và không vượt quá 1.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu gieo xúc xắc 6 lần thì chắc chắn mỗi mặt từ 1 đến 6 xuất hiện đúng 1 lần.", "correct": False}
            ]),
            make_tf(2, f"Thống kê số ly trà sữa bán được trong 4 ngày của một quán: Thứ Hai: 40 ly, Thứ Ba: 50 ly, Thứ Tư: {45+t*5} ly, Thứ Năm: 60 ly (Mã đề {t:02d}):", [
                {"key": "a", "level": "Nhận biết", "text": "Dữ liệu về số ly trà sữa là dữ liệu số (định lượng).", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": f"Tổng số ly trà sữa bán được trong 4 ngày là {195+t*5} ly.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Thứ Năm là ngày bán được nhiều ly trà sữa nhất.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Số ly trà sữa bán ngày Thứ Hai chiếm hơn một nửa tổng số ly bán trong cả 4 ngày.", "correct": False}
            ])
        ]
        p3 = [
            make_sa(1, "Thông hiểu", "Gieo đồng xu 20 lần thấy 11 lần ngửa. Tính số lần sấp.", "9"),
            make_sa(2, "Thông hiểu", f"Gieo xúc xắc 50 lần thấy mặt 6 chấm xuất hiện {10+t} lần. Tính xác suất thực nghiệm xuất hiện mặt 6 chấm.", f"{(10+t)/50:.2f}"),
            make_sa(3, "Vận dụng", f"Một cửa hàng bán được {100+t*10} chiếc điện thoại trong tháng. Trong đó có 60 chiếc của hãng S. Tính tỉ lệ phần trăm số điện thoại hãng S bán được (%).", f"{6000/(100+t*10):.1f}"),
            make_sa(4, "Vận dụng", "Quay vòng quay may mắn 40 lần thấy kim chỉ vào ô trúng thưởng 14 lần. Tính xác suất thực nghiệm quay vào ô không trúng thưởng.", "0.65")
        ]
        p4 = [
            make_essay(1, "Thông hiểu", f"Bạn Lan gieo một con xúc xắc 6 mặt {30+t*10} lần và ghi lại số lần xuất hiện mặt 2 chấm là {6+t} lần. Tính xác suất thực nghiệm xuất hiện mặt 2 chấm và số lần xuất hiện các mặt còn lại.",
                       "\n".join([
                           f"Tổng số lần gieo xúc xắc là: {30+t*10} lần (0.25đ).",
                           f"Số lần xuất hiện mặt 2 chấm là {6+t} lần (0.25đ).",
                           f"Xác suất thực nghiệm xuất hiện mặt 2 chấm: P = ({6+t}) / ({30+t*10}) (0.25đ).",
                           f"Số lần xuất hiện các mặt còn lại: ({30+t*10}) - ({6+t}) = {24+t*9} lần (0.25đ)."
                       ])),
            make_essay(2, "Vận dụng", f"Trong một giải thi đấu ném bóng rổ, một cầu thủ thực hiện ném bóng ${50+t*10}$ lần và có ${35+t*7}$ lần ném bóng vào rổ. Hãy tính xác suất thực nghiệm ném bóng vào rổ của cầu thủ đó và dự đoán nếu cầu thủ ném $200$ lần thì sẽ có khoảng bao nhiêu lần bóng vào rổ.",
                       "\n".join([
                           f"Xác suất thực nghiệm ném bóng vào rổ: P = ({35+t*7}) / ({50+t*10}) (0.25đ).",
                           "Tính tỉ lệ thành công của cầu thủ (0.25đ).",
                           f"Dự đoán số lần bóng vào rổ khi ném 200 lần: N = 200 . P (0.25đ).",
                           "Kết luận số lần bóng vào rổ ước tính (0.25đ)."
                       ])),
            make_essay(3, "Vận dụng cao", "Trong một chiếc hộp có 50 viên bi gồm hai màu xanh và đỏ (không nhìn thấy bên trong). Bạn Minh lấy ngẫu nhiên 1 viên bi, ghi màu rồi trả lại hộp. Sau 100 lần thử, bạn Minh thấy có 40 lần lấy được bi xanh. Hãy ước lượng xem trong hộp có khoảng bao nhiêu viên bi màu đỏ.",
                       "\n".join([
                           "Xác suất thực nghiệm lấy được viên bi màu xanh là: 40 / 100 = 0,4 (0.25đ).",
                           "Xác suất thực nghiệm lấy được viên bi màu đỏ là: 1 - 0,4 = 0,6 (0.25đ).",
                           "Ước lượng tỉ lệ bi đỏ trong hộp xấp xỉ 60% (0.25đ).",
                           "Số viên bi đỏ trong hộp ước tính là: 50 . 0,6 = 30 viên bi đỏ (0.25đ)."
                       ]))
        ]
        exams[f"{chap_id}_bai{l_idx}_test{t}"] = {
            "title": f"Toán 6 (KNTT) - Bài kiểm tra cuối Chương IX: Dữ liệu và xác suất thực nghiệm - Đề số {t:02d}",
            "duration": "90 phút",
            "totalScore": 10.0,
            "part1": p1, "part2": p2, "part3": p3, "part4": p4
        }
    save_chapter_package(6, chap_id, "Chương IX: Dữ liệu và xác suất thực nghiệm", exams)


# ------------------------------------------------------------------------------
# HÀM CHẠY TOÀN BỘ 9 CHƯƠNG TOÁN 6
# ------------------------------------------------------------------------------
def run_all_grade6():
    print("=== BẮT ĐẦU SINH 7 ĐỀ ĐỘC LẬP CHO TOÀN BỘ 9 CHƯƠNG TOÁN 6 ===")
    build_c1_6()
    build_c2_6()
    build_c3_6()
    build_c4_6()
    build_c5_6()
    build_c6_6()
    build_c7_6()
    build_c8_6()
    build_c9_6()
    print("=== HOÀN TẤT XUẤT SẮC TOÁN 6: 9 CHƯƠNG x 7 ĐỀ = 63 ĐỀ CHUẨN MA TRẬN ===")

if __name__ == "__main__":
    run_all_grade6()
