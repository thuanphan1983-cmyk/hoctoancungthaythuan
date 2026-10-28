# -*- coding: utf-8 -*-
"""
HỆ THỐNG TỰ ĐỘNG BIÊN SOẠN ĐỀ KIỂM TRA TOÁN 7 (KẾT NỐI TRI THỨC)
Chương IX (6 bài) & Chương X (3 bài) - Tổng cộng 9 bài x 3 đề = 27 đề kiểm tra
Tuân thủ ma trận: Đề 1 & 2 (Khá 40/30/20/10), Đề 3 (Khá Giỏi 20/30/30/20)
Ràng buộc:
- Phần II: Đúng 1 ý Vận dụng / câu
- Phần III: Đúng 2 câu Vận dụng / 4 câu
"""

import sys
import os

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
if REPO_DIR not in sys.path:
    sys.path.insert(0, REPO_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package

def build_exams_c9_7():
    exams = {}
    
    # --------------------------------------------------------------------------
    # BÀI 31: QUAN HỆ GIỮA GÓC VÀ CẠNH ĐỐI DIỆN TRONG MỘT TAM GIÁC (c9_7_bai1)
    # --------------------------------------------------------------------------
    # ĐỀ 1 (Khá)
    exams["c9_7_bai1_test1"] = {
        "title": "Toán 7 (KNTT) - Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác - Đề số 1 (🌿 Mức độ Khá)",
        "part1": [
            make_mc(1, "Nhận biết", "Trong một tam giác, cạnh đối diện với góc lớn hơn là:", ["Cạnh lớn hơn", "Cạnh nhỏ hơn", "Cạnh bằng nhau", "Không so sánh được"], 0),
            make_mc(2, "Nhận biết", "Trong tam giác $ABC$, góc đối diện với cạnh $BC$ là:", ["Góc $A$", "Góc $B$", "Góc $C$", "Góc tù"], 0),
            make_mc(3, "Nhận biết", "Trong tam giác tù, cạnh có độ dài lớn nhất là:", ["Cạnh đối diện với góc tù", "Cạnh kề góc tù", "Cạnh góc vuông", "Không xác định"], 0),
            make_mc(4, "Nhận biết", "Trong tam giác vuông, cạnh đối diện với góc vuông được gọi là:", ["Cạnh huyền", "Cạnh góc vuông", "Đường cao", "Trung tuyến"], 0),
            make_mc(5, "Nhận biết", "Cạnh có độ dài lớn nhất trong tam giác vuông là:", ["Cạnh huyền", "Cạnh góc vuông lớn hơn", "Cạnh góc vuông nhỏ hơn", "Bằng nhau"], 0),
            make_mc(6, "Nhận biết", "Cho tam giác $MNP$ có $\\widehat{M} = 70^\\circ, \\widehat{N} = 60^\\circ, \\widehat{P} = 50^\\circ$. Cạnh lớn nhất là:", ["$NP$", "$MN$", "$MP$", "Cả 3 cạnh bằng nhau"], 0),
            make_mc(7, "Nhận biết", "Cho tam giác $DEF$ vuông tại $D$. Khẳng định nào sau đây đúng?", ["$EF > DE$ và $EF > DF$", "$DE > EF$", "$DF > EF$", "$DE = EF$"], 0),
            make_mc(8, "Nhận biết", "Góc đối diện với cạnh lớn nhất trong tam giác là:", ["Góc lớn nhất", "Góc nhỏ nhất", "Góc nhọn", "Góc vuông"], 0),
            make_mc(9, "Thông hiểu", "Cho tam giác $ABC$ có $AB = 5\\text{ cm}, AC = 7\\text{ cm}, BC = 8\\text{ cm}$. Khẳng định đúng về các góc là:", ["$\\widehat{A} > \\widehat{B} > \\widehat{C}$", "$\\widehat{C} > \\widehat{B} > \\widehat{A}$", "$\\widehat{B} > \\widehat{A} > \\widehat{C}$", "$\\widehat{A} > \\widehat{C} > \\widehat{B}$"], 0),
            make_mc(10, "Thông hiểu", "Cho $\\triangle ABC$ cân tại $A$ có $\\widehat{A} = 100^\\circ$. Khẳng định nào sau đây đúng?", ["$BC > AB$", "$AB > BC$", "$AB = BC$", "$AC > BC$"], 0),
            make_mc(11, "Thông hiểu", "Cho $\\triangle ABC$ có $\\widehat{B} = 45^\\circ, \\widehat{C} = 35^\\circ$. Cạnh lớn nhất của tam giác là:", ["$BC$", "$AB$", "$AC$", "$AB = AC$"], 0),
            make_mc(12, "Vận dụng", "Cho tam giác $ABC$ có $\\widehat{A} = 2\\widehat{B} = 4\\widehat{C}$. Sắp xếp thứ tự các cạnh từ nhỏ đến lớn là:", ["$AB < AC < BC$", "$BC < AC < AB$", "$AC < AB < BC$", "$AB < BC < AC$"], 0)
        ],
        "part2": [
            make_tf(1, "Cho tam giác ABC có AB = 6 cm, AC = 8 cm, BC = 10 cm:", [
                {"key": "a", "level": "Nhận biết", "text": "Tam giác ABC là tam giác vuông tại A.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Góc A là góc lớn nhất của tam giác ABC.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Trong tam giác ABC ta có góc B nhỏ hơn góc C.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Nếu lấy điểm D trên cạnh BC sao cho BD = 6 cm thì tam giác ABD là tam giác cân và góc BAD < 60°.", "correct": False}
            ]),
            make_tf(2, "Xét tam giác MNP có góc M = 80° và góc N = 50°:", [
                {"key": "a", "level": "Nhận biết", "text": "Số đo góc P bằng 50°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Tam giác MNP là tam giác cân tại M.", "correct": False},
                {"key": "c", "level": "Thông hiểu", "text": "Cạnh NP là cạnh lớn nhất trong tam giác MNP.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Trên cạnh NP lấy điểm K bất kì (K khác N, P), ta luôn có MK < NP.", "correct": True}
            ])
        ],
        "part3": [
            make_sa(1, "Thông hiểu", "Cho tam giác $ABC$ có $\\widehat{A} = 65^\\circ, \\widehat{B} = 55^\\circ$. Số đo góc $C$ bằng bao nhiêu độ?", "60"),
            make_sa(2, "Thông hiểu", "Cho tam giác $ABC$ có $AB = 4\\text{ cm}, AC = 6\\text{ cm}, BC = 7\\text{ cm}$. Góc nhỏ nhất của tam giác là góc nào (ghi rõ tên góc A, B hoặc C)?", "C"),
            make_sa(3, "Vận dụng", "Cho tam giác $ABC$ có $\\widehat{B} - \\widehat{C} = 20^\\circ$ và $\\widehat{A} = 80^\\circ$. Tính số đo góc $\\widehat{B}$ bằng bao nhiêu độ?", "60"),
            make_sa(4, "Vận dụng", "Cho $\\triangle ABC$ có $\\widehat{A} = 70^\\circ$, hai tia phân giác của góc $B$ và $C$ cắt nhau tại $I$. Tính số đo góc $\\widehat{BIC}$ (độ)?", "125")
        ],
        "part4": [
            make_essay(1, "Thông hiểu", "Cho tam giác $ABC$ có $\\widehat{A} = 80^\\circ, \\widehat{B} = 40^\\circ$. Tính góc $\\widehat{C}$ và so sánh độ dài 3 cạnh của tam giác $ABC$.", "Tính góc C = 180° - 80° - 40° = 60° (0.5đ). Vì góc B < góc C < góc A (40° < 60° < 80°) nên AC < AB < BC (0.5đ)."),
            make_essay(2, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$, kẻ đường cao $AH$. So sánh độ dài các đoạn thẳng: $AH, AB, BC$.", "Trong tam giác vuông ABH vuông tại H có cạnh huyền AB nên AH < AB (0.5đ). Trong tam giác ABC vuông tại A có cạnh huyền BC nên AB < BC. Vậy AH < AB < BC (0.5đ)."),
            make_essay(3, "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{B} > 90^\\circ$, điểm $D$ nằm giữa $A$ và $C$. Chứng minh rằng $BD < AC$.", "Góc B tù nên AC là cạnh lớn nhất trong tam giác ABC, suy ra BC < AC và AB < AC (0.5đ). Trong tam giác ABD hoặc CBD, góc B tù chứng minh được BD không thể lớn hơn AC, suy ra BD < AC (0.5đ).")
        ]
    }

    # ĐỀ 2 (Khá - Tương đương Đề 1, đổi số liệu)
    exams["c9_7_bai1_test2"] = {
        "title": "Toán 7 (KNTT) - Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác - Đề số 2 (🌿 Mức độ Khá)",
        "part1": [
            make_mc(1, "Nhận biết", "Trong một tam giác, góc đối diện với cạnh nhỏ nhất là:", ["Góc nhỏ nhất", "Góc lớn nhất", "Góc tù", "Góc vuông"], 0),
            make_mc(2, "Nhận biết", "Trong tam giác $XYZ$, cạnh đối diện với góc $Y$ là:", ["$XZ$", "$XY$", "$YZ$", "Đường chéo"], 0),
            make_mc(3, "Nhận biết", "Trong tam giác vuông $ABC$ vuông tại $B$, cạnh lớn nhất là:", ["$AC$", "$AB$", "$BC$", "Cả 3 cạnh bằng nhau"], 0),
            make_mc(4, "Nhận biết", "Trong tam giác nhọn, các góc đều là:", ["Góc nhọn", "Góc tù", "Góc vuông", "Góc bẹt"], 0),
            make_mc(5, "Nhận biết", "Nếu tam giác có hai góc bằng nhau thì tam giác đó là:", ["Tam giác cân", "Tam giác vuông", "Tam giác đều", "Tam giác tù"], 0),
            make_mc(6, "Nhận biết", "Cho tam giác $ABC$ có $\\widehat{A} = 80^\\circ, \\widehat{B} = 70^\\circ$. Cạnh nhỏ nhất của tam giác là:", ["$AB$", "$BC$", "$AC$", "Không có cạnh nhỏ nhất"], 0),
            make_mc(7, "Nhận biết", "Góc ngoài tại một đỉnh của tam giác lớn hơn:", ["Mỗi góc trong không kề với nó", "Góc kề với nó", "Tổng hai góc còn lại", "Góc bẹt"], 0),
            make_mc(8, "Nhận biết", "Cho $\\triangle ABC$ có $AB < AC < BC$. Góc lớn nhất của tam giác là:", ["$\\widehat{A}$", "$\\widehat{B}$", "$\\widehat{C}$", "Không xác định"], 0),
            make_mc(9, "Thông hiểu", "Cho $\\triangle MNP$ có $MN = 6\\text{ cm}, NP = 9\\text{ cm}, MP = 11\\text{ cm}$. Sắp xếp các góc theo thứ tự giảm dần:", ["$\\widehat{N} > \\widehat{M} > \\widehat{P}$", "$\\widehat{P} > \\widehat{M} > \\widehat{N}$", "$\\widehat{M} > \\widehat{N} > \\widehat{P}$", "$\\widehat{N} > \\widehat{P} > \\widehat{M}$"], 0),
            make_mc(10, "Thông hiểu", "Cho tam giác $ABC$ cân tại $B$ có $\\widehat{B} = 40^\\circ$. So sánh hai cạnh $AC$ và $AB$:", ["$AC < AB$", "$AC > AB$", "$AC = AB$", "$AB = 2AC$"], 0),
            make_mc(11, "Thông hiểu", "Cho $\\triangle ABC$ có $\\widehat{A} = 110^\\circ$. Khẳng định nào sau đây là khẳng định đúng?", ["$BC$ là cạnh dài nhất của tam giác", "$AB$ là cạnh dài nhất", "$AC$ là cạnh dài nhất", "Tam giác có 2 góc tù"], 0),
            make_mc(12, "Vận dụng", "Cho tam giác $ABC$ có $\\widehat{B} = 2\\widehat{C}$ và $\\widehat{A} = 3\\widehat{C}$. Cạnh dài nhất của tam giác là:", ["$BC$", "$AC$", "$AB$", "Ba cạnh bằng nhau"], 0)
        ],
        "part2": [
            make_tf(1, "Cho tam giác DEF có DE = 5 cm, DF = 12 cm, EF = 13 cm:", [
                {"key": "a", "level": "Nhận biết", "text": "Cạnh EF là cạnh dài nhất của tam giác DEF.", "correct": True},
                {"key": "b", "level": "Nhận biết", "text": "Góc D là góc đối diện với cạnh EF nên góc D là góc lớn nhất.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Vì 5² + 12² = 13² nên tam giác DEF vuông tại E.", "correct": False},
                {"key": "d", "level": "Vận dụng", "text": "Đường cao kẻ từ D có độ dài xấp xỉ 4,62 cm và nhỏ hơn cả DE và DF.", "correct": True}
            ]),
            make_tf(2, "Cho tam giác ABC có góc A = 70°, góc B = 60°:", [
                {"key": "a", "level": "Nhận biết", "text": "Số đo góc C của tam giác bằng 50°.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Trong ba cạnh, cạnh BC có độ dài nhỏ nhất.", "correct": False},
                {"key": "c", "level": "Thông hiểu", "text": "Thứ tự độ dài các cạnh tăng dần là AB < AC < BC.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Nếu kẻ đường phân giác AD của góc A thì BD < CD.", "correct": True}
            ])
        ],
        "part3": [
            make_sa(1, "Thông hiểu", "Cho tam giác $ABC$ có $\\widehat{B} = 75^\\circ, \\widehat{C} = 45^\\circ$. Tính số đo góc $\\widehat{A}$ (độ):", "60"),
            make_sa(2, "Thông hiểu", "Cho tam giác $DEF$ có $DE = 7\\text{ cm}, EF = 9\\text{ cm}, DF = 8\\text{ cm}$. Cạnh đối diện góc lớn nhất có độ dài bằng bao nhiêu cm?", "9"),
            make_sa(3, "Vận dụng", "Tam giác $ABC$ cân tại $A$ có góc đáy $\\widehat{B} = 50^\\circ$. Cạnh đáy $BC$ so với cạnh bên $AB$ là lớn hơn hay nhỏ hơn (điền 'lớn hơn' hoặc 'nhỏ hơn')?", "lớn hơn"),
            make_sa(4, "Vận dụng", "Cho tam giác $ABC$ có $\\widehat{A} = 50^\\circ$, tỉ số $\\widehat{B} : \\widehat{C} = 2 : 3$. Tính số đo góc $\\widehat{C}$ (độ):", "78")
        ],
        "part4": [
            make_essay(1, "Thông hiểu", "Cho tam giác $MNP$ có $\\widehat{M} = 75^\\circ, \\widehat{N} = 35^\\circ$. So sánh độ dài các cạnh của tam giác $MNP$.", "Tính góc P = 180° - 75° - 35° = 70° (0.5đ). Vì góc N (35°) < góc P (70°) < góc M (75°) nên MP < MN < NP (0.5đ)."),
            make_essay(2, "Vận dụng", "Cho tam giác $ABC$ có $AB < AC$. Kẻ đường phân giác $AD$ ($D \\in BC$). Chứng minh rằng $\\widehat{ADB} < \\widehat{ADC}$.", "Xét góc ngoài của tam giác: góc ADC = góc B + góc A1, góc ADB = góc C + góc A2 (0.5đ). Vì AB < AC nên góc C < góc B. Do A1 = A2 nên góc ADB < góc ADC (0.5đ)."),
            make_essay(3, "Vận dụng cao", "Cho điểm $M$ nằm bên trong tam giác $ABC$. Chứng minh rằng $MB + MC < AB + AC$.", "Kéo dài BM cắt AC tại K. Áp dụng bất đẳng thức tam giác trong tam giác ABK: BK < AB + AK, do đó MB + BK' < AB + AK (0.5đ). Tương tự trong tam giác KMC dẫn đến kết luận MB + MC < AB + AC (0.5đ).")
        ]
    }

    # ĐỀ 3 (Khá Giỏi: 20% NB, 30% TH, 30% VD, 20% VDC)
    exams["c9_7_bai1_test3"] = {
        "title": "Toán 7 (KNTT) - Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác - Đề số 3 (🚀 Mức độ Khá Giỏi)",
        "part1": [
            make_mc(1, "Nhận biết", "Trong tam giác đối diện với cạnh nhỏ nhất là góc:", ["Nhỏ nhất", "Lớn nhất", "Góc vuông", "Góc nhọn bất kì"], 0),
            make_mc(2, "Nhận biết", "Trong tam giác tù, góc tù đối diện với:", ["Cạnh lớn nhất", "Cạnh nhỏ nhất", "Cạnh góc vuông", "Không xác định"], 0),
            make_mc(3, "Nhận biết", "Cho tam giác $ABC$ có $\\widehat{A} = 90^\\circ$. Bất đẳng thức nào sau đây đúng?", ["$BC > AB$", "$AB > BC$", "$AC > BC$", "$AB = BC$"], 0),
            make_mc(4, "Nhận biết", "Tam giác có 3 cạnh bằng nhau thì các góc của tam giác có số đo là:", ["$60^\\circ$", "$90^\\circ$", "$45^\\circ$", "$120^\\circ$"], 0),
            make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $\\widehat{A} = 40^\\circ$, góc ngoài tại đỉnh $B$ bằng $110^\\circ$. So sánh các cạnh của $\\triangle ABC$:", ["$AB < BC < AC$", "$AC < BC < AB$", "$BC < AB < AC$", "$AB < AC < BC$"], 0),
            make_mc(6, "Thông hiểu", "Cho $\\triangle ABC$ có $AB = AC = 5\\text{ cm}, BC = 8\\text{ cm}$. Góc đối diện cạnh $BC$ là:", ["Góc lớn nhất và là góc tù hoặc nhọn > 60°", "Góc nhỏ nhất", "Góc vuông", "Góc 60°"], 0),
            make_mc(7, "Thông hiểu", "Cho tam giác vuông $ABC$ tại $A$ có $\\widehat{C} = 30^\\circ$. Mối liên hệ đúng giữa $AB$ và $BC$ là:", ["$AB = \\frac{1}{2}BC$", "$AB = BC$", "$AB = 2BC$", "$AC = \\frac{1}{2}BC$"], 0),
            make_mc(8, "Thông hiểu", "Cho tam giác $ABC$ có $\\widehat{B} > 90^\\circ$. Lấy điểm $D$ trên cạnh $BC$. Khẳng định nào sau đây đúng?", ["$AD > AB$", "$AD < AB$", "$AD = AB$", "Không so sánh được"], 0),
            make_mc(9, "Vận dụng", "Cho $\\triangle ABC$ có $AB < AC$. Trên tia đối của tia $BC$ lấy điểm $E$, trên tia đối của tia $CB$ lấy điểm $F$ sao cho $BE = CF$. So sánh $AE$ và $AF$:", ["$AE < AF$", "$AE > AF$", "$AE = AF$", "Không đủ điều kiện"], 0),
            make_mc(10, "Vận dụng", "Cho tam giác $ABC$ nhọn có đường cao $AH$. Khẳng định nào sau đây là khẳng định sai?", ["$BC > AH$", "$AB < AH$", "$AC > AH$", "$AB + AC > 2AH$"], 1),
            make_mc(11, "Vận dụng", "Cho $\\triangle ABC$ có $\\widehat{A} = 80^\\circ$, các tia phân giác trong góc $B$ và $C$ cắt nhau tại $I$. Cạnh lớn nhất trong $\\triangle IBC$ là:", ["$BC$", "$IB$", "$IC$", "$IB = IC$"], 0),
            make_mc(12, "Vận dụng cao", "Cho $\\triangle ABC$ có góc $\\widehat{A}$ tù. Trên cạnh $AB$ lấy điểm $M$, trên cạnh $AC$ lấy điểm $N$. So sánh độ dài $MN$ và $BC$:", ["$MN < BC$", "$MN > BC$", "$MN = BC$", "Tùy vị trí điểm"], 0)
        ],
        "part2": [
            make_tf(1, "Cho tam giác ABC có góc A tù và AB < AC. Kẻ đường cao AH:", [
                {"key": "a", "level": "Nhận biết", "text": "Cạnh BC là cạnh có độ dài lớn nhất trong tam giác ABC.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Điểm H nằm giữa hai điểm B và C.", "correct": False},
                {"key": "c", "level": "Thông hiểu", "text": "Ta có góc B > góc C.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Lấy điểm M nằm giữa B và C thì đoạn thẳng AM luôn thỏa mãn AM < AC.", "correct": True}
            ]),
            make_tf(2, "Cho tam giác nhọn ABC có AB < AC, kẻ trung tuyến AM:", [
                {"key": "a", "level": "Nhận biết", "text": "M là trung điểm của cạnh BC.", "correct": True},
                {"key": "b", "level": "Thông hiểu", "text": "Góc C < góc B.", "correct": True},
                {"key": "c", "level": "Thông hiểu", "text": "Hai tam giác ABM và ACM có diện tích bằng nhau.", "correct": True},
                {"key": "d", "level": "Vận dụng", "text": "Góc AMB luôn nhọn và nhỏ hơn góc AMC.", "correct": False}
            ])
        ],
        "part3": [
            make_sa(1, "Thông hiểu", "Cho tam giác $ABC$ có $\\widehat{A} = 2\\widehat{B}$ và $\\widehat{B} = 3\\widehat{C}$. Tính số đo góc $\\widehat{A}$ (độ):", "108"),
            make_sa(2, "Vận dụng", "Cho tam giác $ABC$ vuông cân tại $A$ có $AB = 6\\text{ cm}$. Điểm $M$ thuộc cạnh $BC$. Giá trị nhỏ nhất của độ dài đoạn thẳng $AM$ bằng bao nhiêu cm (làm tròn đến hàng phần mười hoặc dạng số thập phân)?", "4.24", acceptable=["4.2", "4.24", "3*sqrt(2)", "4,2", "4,24"]),
            make_sa(3, "Vận dụng", "Cho tam giác $ABC$ có chu vi bằng $18\\text{ cm}$. Cạnh lớn nhất gấp đôi cạnh nhỏ nhất và cạnh thứ ba hơn cạnh nhỏ nhất $2\\text{ cm}$. Độ dài cạnh lớn nhất bằng bao nhiêu cm?", "8"),
            make_sa(4, "Vận dụng cao", "Cho tam giác $ABC$ có $\\widehat{A} = 60^\\circ, AB = 5\\text{ cm}, AC = 8\\text{ cm}$. Kẻ phân giác $AD$. Tỉ số độ dài $BD : CD$ bằng phân số tối giản $a/b$. Giá trị của $a + b$ là:", "13")
        ],
        "part4": [
            make_essay(1, "Vận dụng", "Cho tam giác $ABC$ có $AB < AC$. Gọi $M$ là trung điểm của $BC$. Chứng minh rằng $\\widehat{MAB} > \\widehat{MAC}$.", "Lấy điểm D trên tia đối của MA sao cho MD = MA. Chứng minh tam giác MAB = tam giác MDC (c.g.c) (0.5đ). Suy ra CD = AB < AC, trong tam giác ACD có CD < AC nên góc CAD < góc CDA = góc MAB. Vậy góc MAB > góc MAC (0.5đ)."),
            make_essay(2, "Vận dụng", "Cho tam giác nhọn $ABC$ có $AB < AC$. Kẻ đường cao $AH$. Chứng minh rằng $HB < HC$ và $\\widehat{HAB} < \\widehat{HAC}$.", "Áp dụng định lí Pythagore: AB² - AH² = HB²; AC² - AH² = HC². Vì AB < AC nên HB < HC (0.5đ). Từ đó trong hai tam giác vuông ABH và ACH suy ra góc HAB < góc HAC (0.5đ)."),
            make_essay(3, "Vận dụng cao", "Cho tam giác $ABC$ có $AB < AC$. Trên tia đối của tia $BA$ lấy điểm $D$ sao cho $BD = BA$. Trên tia đối của tia $CA$ lấy điểm $E$ sao cho $CE = CA$. So sánh hai đoạn thẳng $CD$ và $BE$.", "Vẽ hình phụ hoặc chứng minh qua hai tam giác có 2 cặp cạnh bằng nhau và góc kẹp giữa khác nhau (0.5đ). Lập luận chặt chẽ dẫn đến kết luận CD < BE (0.5đ).")
        ]
    }

    return exams




# -*- coding: utf-8 -*-
"""
BUILDER SINH TRỌN BỘ ĐỀ KIỂM TRA TOÁN 7 (KẾT NỐI TRI THỨC)
Chương IX: Quan hệ giữa các yếu tố trong một tam giác (6 bài x 3 đề = 18 đề)
Chương X: Một số hình khối trong thực tiễn (3 bài x 3 đề = 9 đề)
Tổng cộng: 27 đề kiểm tra chuẩn ma trận 2025.
"""

import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package

def create_lesson_exams(grade, ch_id, ch_title, lesson_idx, lesson_name, topic_bank):
    """
    Sinh 3 đề cho 1 bài học từ ngân hàng chủ đề (topic_bank):
    - Đề 1 (Khá 40/30/20/10)
    - Đề 2 (Khá 40/30/20/10 - tương đương Đề 1)
    - Đề 3 (Khá Giỏi 20/30/30/20)
    """
    exams = {}
    for t_num in [1, 2, 3]:
        key = f"{ch_id}_bai{lesson_idx}_test{t_num}"
        tag = "🌿 Mức độ Khá" if t_num in [1, 2] else "🚀 Mức độ Khá Giỏi"
        title = f"Toán {grade} (KNTT) - {lesson_name} - Bài kiểm tra số {t_num} ({tag})"
        
        q_data = topic_bank(t_num)
        exams[key] = {
            "title": title,
            "part1": q_data["part1"],
            "part2": q_data["part2"],
            "part3": q_data["part3"],
            "part4": q_data["part4"]
        }
    return exams

# ==============================================================================
# NGÂN HÀNG DỮ LIỆU CHƯƠNG IX TOÁN 7
# ==============================================================================

# BÀI 31: Quan hệ giữa góc và cạnh đối diện
def get_bank_c9_bai1(t_num):
    all_c9 = build_exams_c9_7()
    return all_c9[f"c9_7_bai1_test{t_num}"]

# BÀI 32: Quan hệ giữa đường vuông góc và đường xiên
def get_bank_c9_bai2(t_num):
    if t_num == 1:
        return {
            "part1": [
                make_mc(1, "Nhận biết", "Trong các đường xiên và đường vuông góc kẻ từ một điểm nằm ngoài đường thẳng đến đường thẳng đó:", ["Đường vuông góc là đường ngắn nhất", "Đường xiên là đường ngắn nhất", "Đường xiên bằng đường vuông góc", "Không so sánh được"], 0),
                make_mc(2, "Nhận biết", "Đoạn thẳng vuông góc kẻ từ điểm $A$ đến đường thẳng $d$ gọi là:", ["Khoảng cách từ điểm $A$ đến đường thẳng $d$", "Đường xiên", "Hình chiếu", "Đoạn thẳng song song"], 0),
                make_mc(3, "Nhận biết", "Cho điểm $A$ nằm ngoài đường thẳng $d$, $AH \\perp d$ tại $H$, $B \\in d$ ($B \\neq H$). Đoạn thẳng $AB$ gọi là:", ["Đường xiên kẻ từ $A$ đến $d$", "Đường vuông góc", "Hình chiếu của $A$", "Khoảng cách"], 0),
                make_mc(4, "Nhận biết", "Hình chiếu của điểm $A$ nằm ngoài đường thẳng $d$ trên $d$ là:", ["Chân đường vuông góc kẻ từ $A$ đến $d$", "Điểm bất kì trên $d$", "Trung điểm của đoạn thẳng", "Điểm đối xứng"], 0),
                make_mc(5, "Nhận biết", "Hình chiếu của đường xiên $AB$ trên đường thẳng $d$ (với $AH \\perp d$) là:", ["Đoạn thẳng $HB$", "Đoạn thẳng $AH$", "Đoạn thẳng $AB$", "Điểm $H$"], 0),
                make_mc(6, "Nhận biết", "Nếu hai đường xiên kẻ từ một điểm đến một đường thẳng bằng nhau thì:", ["Hai hình chiếu của chúng bằng nhau", "Hai hình chiếu vuông góc", "Đường vuông góc bằng 0", "Không có hình chiếu"], 0),
                make_mc(7, "Nhận biết", "Trong hai đường xiên kẻ từ một điểm đến một đường thẳng, đường xiên nào có hình chiếu lớn hơn thì:", ["Lớn hơn", "Nhỏ hơn", "Bằng nhau", "Không xác định"], 0),
                make_mc(8, "Nhận biết", "Đường xiên lớn hơn thì có hình chiếu:", ["Lớn hơn", "Nhỏ hơn", "Bằng nhau", "Bằng 0"], 0),
                make_mc(9, "Thông hiểu", "Cho $AH \\perp d$ tại $H$. Lấy hai điểm $B, C \\in d$ sao cho $HB = 3\\text{ cm}, HC = 4\\text{ cm}$. So sánh $AB$ và $AC$:", ["$AB < AC$", "$AB > AC$", "$AB = AC$", "Không so sánh được"], 0),
                make_mc(10, "Thông hiểu", "Từ điểm $M$ nằm ngoài đường thẳng $a$, kẻ $MH \\perp a$ tại $H$ và đường xiên $MK$. Biết $MH = 6\\text{ cm}, MK = 10\\text{ cm}$. Độ dài hình chiếu $HK$ là:", ["$8\\text{ cm}$", "$4\\text{ cm}$", "$16\\text{ cm}$", "$64\\text{ cm}$"], 0),
                make_mc(11, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$. Hình chiếu của cạnh $AB$ trên đường thẳng $AC$ là:", ["Điểm $A$", "Đoạn thẳng $AC$", "Đoạn thẳng $BC$", "Đoạn thẳng $AB$"], 0),
                make_mc(12, "Vận dụng", "Cho hình chữ nhật $ABCD$. Từ $A$ kẻ đường thẳng vuông góc với $BD$ tại $H$. So sánh độ dài $AH$ và $AB$:", ["$AH < AB$", "$AH > AB$", "$AH = AB$", "Không so sánh được"], 0)
            ],
            "part2": [
                make_tf(1, "Cho điểm A nằm ngoài đường thẳng d. Kẻ AH vuông góc với d (H thuộc d). Lấy B, C thuộc d sao cho H nằm giữa B và C, HB = 5 cm, HC = 7 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "AH là khoảng cách từ A đến đường thẳng d.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Đoạn thẳng HB là hình chiếu của đường xiên AB trên d.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Vì HB < HC nên đường xiên AB < AC.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Góc BAH lớn hơn góc CAH.", "correct": False}
                ]),
                make_tf(2, "Cho tam giác ABC có góc B nhọn, góc C nhọn. Kẻ đường cao AH:", [
                    {"key": "a", "level": "Nhận biết", "text": "H nằm giữa B và C.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Đoạn thẳng HB là hình chiếu của AB trên BC.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Nếu AB = AC thì HB = HC.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu AB < AC thì chu vi tam giác ABH lớn hơn chu vi tam giác ACH.", "correct": False}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Cho điểm $A$ cách đường thẳng $d$ một khoảng bằng $12\\text{ cm}$. Đường xiên $AB$ kẻ từ $A$ đến $d$ có độ dài $13\\text{ cm}$. Tính độ dài hình chiếu của $AB$ trên $d$ (cm):", "5"),
                make_sa(2, "Thông hiểu", "Từ điểm $P$ nằm ngoài đường thẳng $m$, kẻ $PH \\perp m$ và hai đường xiên $PA = PB$. Biết hình chiếu $HA = 6\\text{ cm}$, độ dài hình chiếu $HB$ bằng bao nhiêu cm?", "6"),
                make_sa(3, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 9\\text{ cm}, AC = 12\\text{ cm}$. Kẻ đường cao $AH$. Độ dài khoảng cách từ $A$ đến cạnh $BC$ bằng bao nhiêu cm (dạng thập phân)?", "7.2", acceptable=["7.2", "7,2", "36/5"]),
                make_sa(4, "Vận dụng", "Cho đường thẳng $d$ và đoạn thẳng $AB = 10\\text{ cm}$ song song với $d$ và cách $d$ một khoảng $6\\text{ cm}$. Lấy điểm $M$ bất kì trên $d$. Tổng khoảng cách $MA + MB$ nhỏ nhất bằng bao nhiêu cm (làm tròn số nguyên)?", "16", acceptable=["15.6", "16", "15,6"])
            ],
            "part4": [
                make_essay(1, "Thông hiểu", "Cho tam giác $ABC$ cân tại $A$. Kẻ $AH \\perp BC$ ($H \\in BC$). Chứng minh rằng $HB = HC$.", "Trong tam giác ABC, AB và AC là hai đường xiên kẻ từ A đến BC (0.5đ). Vì tam giác ABC cân tại A nên AB = AC, suy ra hai hình chiếu tương ứng bằng nhau là HB = HC (0.5đ)."),
                make_essay(2, "Vận dụng", "Cho tam giác $ABC$ có $\\widehat{B} < 90^\\circ, \\widehat{C} < 90^\\circ$ và $AB < AC$. Kẻ $AH \\perp BC$. Chứng minh $\\widehat{BAH} < \\widehat{CAH}$.", "Vì AB < AC nên hình chiếu HB < HC (0.5đ). Trong hai tam giác vuông ABH và ACH, so sánh tỉ số hoặc góc nhọn suy ra góc BAH < góc CAH (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Cho đường thẳng $d$ và hai điểm $A, B$ nằm cùng phía đối với $d$. Tìm vị trí điểm $M \\in d$ sao cho $MA + MB$ đạt giá trị nhỏ nhất.", "Lấy A' đối xứng với A qua d. Khi đó với mọi M thuộc d ta có MA = MA' (0.5đ). Suy ra MA + MB = MA' + MB ≥ A'B. Dấu '=' xảy ra khi M là giao điểm của A'B với d (0.5đ).")
            ]
        }
    elif t_num == 2:
        return {
            "part1": [
                make_mc(1, "Nhận biết", "Trong một tam giác vuông, khoảng cách từ đỉnh góc vuông đến cạnh huyền là:", ["Độ dài đường cao kẻ từ đỉnh góc vuông", "Độ dài cạnh huyền", "Cạnh góc vuông", "Nửa cạnh huyền"], 0),
                make_mc(2, "Nhận biết", "Cho $M \\notin d$, $MH \\perp d$ tại $H$. Với mọi điểm $A \\in d$ ($A \\neq H$), luôn có:", ["$MA > MH$", "$MA < MH$", "$MA = MH$", "$MA \\le MH$"], 0),
                make_mc(3, "Nhận biết", "Hai đường xiên bằng nhau thì hai hình chiếu tương ứng:", ["Bằng nhau", "Khác nhau", "Vuông góc", "Gấp đôi nhau"], 0),
                make_mc(4, "Nhận biết", "Hình chiếu của một đoạn thẳng song song với đường thẳng $d$ lên $d$ có độ dài:", ["Bằng độ dài đoạn thẳng đó", "Lớn hơn", "Nhỏ hơn", "Bằng 0"], 0),
                make_mc(5, "Nhận biết", "Hình chiếu của một đoạn thẳng vuông góc với đường thẳng $d$ lên $d$ là:", ["Một điểm", "Một đoạn thẳng", "Một tia", "Đường thẳng"], 0),
                make_mc(6, "Nhận biết", "Đoạn thẳng nào ngắn nhất trong các đoạn nối từ 1 điểm đến 1 đường thẳng?", ["Đoạn vuông góc", "Đoạn xiên", "Đoạn song song", "Tất cả bằng nhau"], 0),
                make_mc(7, "Nhận biết", "Cho $AH \\perp d$ tại $H$, $B, C \\in d$. Nếu $HB > HC$ thì:", ["$AB > AC$", "$AB < AC$", "$AB = AC$", "Không so sánh được"], 0),
                make_mc(8, "Nhận biết", "Quan hệ giữa đường vuông góc và đường xiên cho ta biết:", ["Cạnh huyền luôn lớn hơn cạnh góc vuông", "Cạnh góc vuông lớn hơn cạnh huyền", "Đường trung tuyến lớn nhất", "Hai góc nhọn bù nhau"], 0),
                make_mc(9, "Thông hiểu", "Cho $AH \\perp d$ tại $H$. Biết $AB = 15\\text{ cm}, HB = 9\\text{ cm}$. Khoảng cách từ $A$ đến $d$ là:", ["$12\\text{ cm}$", "$6\\text{ cm}$", "$24\\text{ cm}$", "$18\\text{ cm}$"], 0),
                make_mc(10, "Thông hiểu", "Cho tam giác $ABC$ nhọn có đường cao $AH$. Khẳng định nào sau đây luôn đúng?", ["$AB > AH$ và $AC > AH$", "$AB = AH$", "$BC < AH$", "$AB + AC < 2AH$"], 0),
                make_mc(11, "Thông hiểu", "Từ điểm $O$ kẻ vuông góc $OH$ đến đường thẳng $xy$. Lấy $A, B$ trên $xy$ sao cho $H$ là trung điểm $AB$. Tam giác $OAB$ là:", ["Tam giác cân tại $O$", "Tam giác đều", "Tam giác vuông tại $O$", "Tam giác tù"], 0),
                make_mc(12, "Vận dụng", "Cho góc nhọn $xOy$ và điểm $A$ cố định bên trong góc. Điểm $M \\in Ox, N \\in Oy$. Chu vi tam giác $AMN$ nhỏ nhất khi:", ["$M, N$ nằm trên đoạn nối hai điểm đối xứng của $A$ qua hai cạnh", "$M$ là gốc tọa độ", "$N$ là gốc tọa độ", "$M, N$ tùy ý"], 0)
            ],
            "part2": [
                make_tf(1, "Cho tam giác ABC vuông tại A có đường cao AH kẻ đến cạnh huyền BC:", [
                    {"key": "a", "level": "Nhận biết", "text": "AH là khoảng cách từ điểm A đến đường thẳng BC.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "HB là hình chiếu của cạnh góc vuông AB trên cạnh huyền BC.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Ta luôn có AH > AB.", "correct": False},
                    {"key": "d", "level": "Vận dụng", "text": "Biết AB = 6 cm, AC = 8 cm thì hình chiếu HB = 3,6 cm.", "correct": True}
                ]),
                make_tf(2, "Cho đường thẳng d và hai điểm A, B nằm cùng phía đối với d sao cho AB không song song d:", [
                    {"key": "a", "level": "Nhận biết", "text": "Kẻ AH và BK vuông góc với d thì AH và BK song song với nhau.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Tứ giác ABKH là hình thang vuông.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Đoạn thẳng HK là hình chiếu của đoạn thẳng AB trên đường thẳng d.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Độ dài đoạn HK luôn lớn hơn độ dài đoạn thẳng AB.", "correct": False}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Từ điểm $S$ kẻ đường vuông góc $SO$ xuống mặt phẳng $d$ ($SO = 8\\text{ cm}$) và đường xiên $SA = 10\\text{ cm}$. Tính độ dài hình chiếu $OA$ (cm):", "6"),
                make_sa(2, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$, $AB = 6\\text{ cm}, BC = 10\\text{ cm}$. Khoảng cách từ điểm $C$ đến đường thẳng $AB$ bằng bao nhiêu cm?", "8"),
                make_sa(3, "Vận dụng", "Cho tam giác đều $ABC$ cạnh $6\\text{ cm}$. Khoảng cách từ trọng tâm $G$ đến cạnh $BC$ bằng bao nhiêu cm (dạng căn thức hoặc xấp xỉ 1.73 cm)?", "1.73", acceptable=["1.73", "1,73", "sqrt(3)", "1.7"]),
                make_sa(4, "Vận dụng", "Cho hình vuông $ABCD$ cạnh $4\\text{ cm}$. Điểm $M$ nằm trên cạnh $CD$. Tổng khoảng cách từ $M$ đến hai đường chéo $AC$ và $BD$ bằng bao nhiêu cm (dạng thập phân làm tròn 1 chữ số)?", "2.8", acceptable=["2.8", "2.83", "2,8", "2*sqrt(2)"])
            ],
            "part4": [
                make_essay(1, "Thông hiểu", "Cho điểm $A$ nằm ngoài đường thẳng $d$. Kẻ $AH \\perp d$. Lấy hai điểm $B, C \\in d$ sao cho $H$ là trung điểm của $BC$. Chứng minh tam giác $ABC$ cân tại $A$.", "Hai đoạn thẳng HB và HC là hình chiếu của AB và AC trên d (0.5đ). Vì HB = HC nên hai đường xiên AB = AC. Do đó tam giác ABC cân tại A (0.5đ)."),
                make_essay(2, "Vận dụng", "Cho góc vuông $xOy$ và điểm $A$ cố định bên trong góc. Kẻ $AH \\perp Ox, AK \\perp Oy$. Chứng minh rằng đoạn thẳng $HK$ bằng độ dài đoạn thẳng $OA$.", "Tứ giác AHOK có 3 góc vuông nên là hình chữ nhật (0.5đ). Hai đường chéo của hình chữ nhật bằng nhau nên HK = OA (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Cho tam giác $ABC$ nhọn. Tìm điểm $M$ bên trong tam giác sao cho tổng khoảng cách từ $M$ đến 3 cạnh của tam giác đạt giá trị nhỏ nhất hoặc đặc biệt.", "Sử dụng công thức diện tích tam giác S = 1/2*(a*d1 + b*d2 + c*d3) (0.5đ). Lập luận vị trí điểm M khi tam giác đều hoặc tam giác cân để tổng khoảng cách không đổi (0.5đ).")
            ]
        }
    else: # t_num == 3 (Khá Giỏi)
        return {
            "part1": [
                make_mc(1, "Nhận biết", "Khoảng cách giữa hai đường thẳng song song là:", ["Độ dài đoạn vuông góc kẻ từ 1 điểm trên đường này đến đường kia", "Độ dài đoạn xiên", "Vô cùng lớn", "Bằng 0"], 0),
                make_mc(2, "Nhận biết", "Trong các đoạn thẳng nối từ một điểm đến một đường tròn, đoạn thẳng có độ dài nhỏ nhất nằm trên:", ["Đường thẳng đi qua tâm", "Tiếp tuyến", "Dây cung bất kì", "Đường vuông góc"], 0),
                make_mc(3, "Nhận biết", "Cho $AH \\perp d$ tại $H$. Nếu $M$ di chuyển trên $d$ ra xa $H$ thì độ dài $AM$:", ["Càng tăng", "Càng giảm", "Không đổi", "Bằng 0"], 0),
                make_mc(4, "Nhận biết", "Hình chiếu của trọng tâm tam giác đều trên một cạnh trùng với:", ["Trung điểm của cạnh đó", "Đỉnh đối diện", "Điểm chia tỉ lệ 1:3", "Điểm bất kì"], 0),
                make_mc(5, "Thông hiểu", "Cho tam giác $ABC$ có $\\widehat{B} > 90^\\circ$. Chân đường vuông góc kẻ từ $A$ đến $BC$ nằm ở:", ["Trên tia đối của tia $BC$", "Giữa $B$ và $C$", "Trên tia đối của tia $CB$", "Trùng với $B$"], 0),
                make_mc(6, "Thông hiểu", "Cho điểm $A$ nằm ngoài đường thẳng $d$. Kẻ $AH \\perp d$. Lấy $B, C, D \\in d$ sao cho $HB < HC < HD$. Khẳng định đúng là:", ["$AH < AB < AC < AD$", "$AD < AC < AB < AH$", "$AB < AH < AC < AD$", "$AC < AB < AD$"], 0),
                make_mc(7, "Thông hiểu", "Cho tam giác cân $ABC$ ($AB = AC$). Kẻ $BD \\perp AC$ và $CE \\perp AB$. So sánh $BD$ và $CE$:", ["$BD = CE$", "$BD > CE$", "$BD < CE$", "Không so sánh được"], 0),
                make_mc(8, "Thông hiểu", "Trong một tam giác tù, trực tâm của tam giác nằm ở:", ["Bên ngoài tam giác", "Bên trong tam giác", "Trên cạnh lớn nhất", "Tại đỉnh góc tù"], 0),
                make_mc(9, "Vận dụng", "Cho tam giác nhọn $ABC$, kẻ đường cao $AH$. Khẳng định nào sau đây luôn đúng?", ["$AB + AC > AH + BC$", "$AB + AC < 2AH$", "$AH > \\frac{1}{2}(AB + AC)$", "$BC = 2AH$"], 0),
                make_mc(10, "Vận dụng", "Cho góc nhọn $xOy$ và điểm $A$ cố định trên tia $Ox$. Điểm $B$ di động trên tia $Oy$. Khoảng cách từ $A$ đến $OB$ lớn nhất khi:", ["$AB \\perp Oy$", "$B$ trùng $O$", "$B$ tiến ra vô cực", "$OA = OB$"], 0),
                make_mc(11, "Vận dụng", "Cho tam giác $ABC$ có $AB < AC$. Kẻ $AH \\perp BC$ và trung tuyến $AM$. Thứ tự các điểm trên đường thẳng $BC$ là:", ["$B, H, M, C$", "$B, M, H, C$", "$H, B, M, C$", "$B, H, C, M$"], 0),
                make_mc(12, "Vận dụng cao", "Cho tam giác $ABC$ có diện tích không đổi và cạnh đáy $BC$ cố định. Quỹ tích đỉnh $A$ sao cho khoảng cách từ $A$ đến $BC$ không đổi là:", ["Hai đường thẳng song song với $BC$ và cách $BC$ một khoảng $h$", "Một đường tròn", "Một đoạn thẳng", "Một điểm duy nhất"], 0)
            ],
            "part2": [
                make_tf(1, "Cho tam giác ABC nhọn có AB < AC. Kẻ đường cao AH và đường phân giác AD:", [
                    {"key": "a", "level": "Nhận biết", "text": "AH vuông góc với BC tại H.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Hình chiếu HB < HC.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Điểm H nằm giữa B và D.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Tia phân giác AD luôn nằm giữa tia đường cao AH và tia trung tuyến AM kẻ từ A.", "correct": True}
                ]),
                make_tf(2, "Cho góc vuông xOy và hai điểm A thuộc Ox, B thuộc Oy cố định. Lấy điểm M bất kì trên đoạn thẳng AB:", [
                    {"key": "a", "level": "Nhận biết", "text": "Khoảng cách từ O đến đường thẳng AB là độ dài đoạn vuông góc OH kẻ từ O đến AB.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Độ dài đoạn OM luôn thỏa mãn OM ≥ OH.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Độ dài đoạn thẳng OM lớn nhất khi M trùng với A hoặc M trùng với B.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu OA = 3 cm, OB = 4 cm thì giá trị nhỏ nhất của OM bằng 2,5 cm.", "correct": False}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 5\\text{ cm}, AC = 12\\text{ cm}$. Khoảng cách từ đỉnh $A$ đến cạnh huyền $BC$ bằng bao nhiêu cm (làm tròn 2 chữ số thập phân)?", "4.62", acceptable=["4.62", "4,62", "60/13", "4.6"]),
                make_sa(2, "Vận dụng", "Cho đoạn thẳng $AB = 8\\text{ cm}$. Điểm $M$ di động sao cho tam giác $MAB$ có diện tích bằng $24\\text{ cm}^2$. Khoảng cách từ $M$ đến đường thẳng $AB$ bằng bao nhiêu cm?", "6"),
                make_sa(3, "Vận dụng", "Cho hình vuông $ABCD$ cạnh $6\\text{ cm}$. Khoảng cách từ tâm đối xứng $O$ của hình vuông đến mỗi cạnh của nó bằng bao nhiêu cm?", "3"),
                make_sa(4, "Vận dụng cao", "Cho tam giác $ABC$ đều cạnh $a = 12\\text{ cm}$. Điểm $M$ nằm bên trong tam giác. Tổng khoảng cách từ $M$ đến ba cạnh của tam giác bằng bao nhiêu cm (làm tròn số nguyên)?", "10", acceptable=["10.39", "10.4", "10", "6*sqrt(3)"])
            ],
            "part4": [
                make_essay(1, "Vận dụng", "Cho tam giác nhọn $ABC$ có $AB < AC$. Kẻ đường cao $AH$. Lấy điểm $M$ bất kì trên đoạn $AH$. Chứng minh rằng $MB < MC$.", "Áp dụng định lí đường xiên và hình chiếu: AH vuông góc BC. Vì AB < AC nên hình chiếu HB < HC (0.5đ). Điểm M nằm trên đường thẳng AH vuông góc BC nên hình chiếu của MB, MC trên BC vẫn là HB và HC. Vì HB < HC nên MB < MC (0.5đ)."),
                make_essay(2, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$, kẻ đường cao $AH$. Gọi $D, E$ lần lượt là hình chiếu của $H$ trên $AB$ và $AC$. Chứng minh $DE = AH$.", "Tứ giác ADHE có góc A = góc D = góc E = 90° nên là hình chữ nhật (0.5đ). Trong hình chữ nhật ADHE, hai đường chéo bằng nhau nên DE = AH (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Chứng minh rằng trong một tam giác nhọn, tổng ba đường cao luôn nhỏ hơn chu vi tam giác đó.", "Trong tam giác vuông, cạnh góc vuông nhỏ hơn cạnh huyền: ha < c và ha < b suy ra ha < (b+c)/2 (0.5đ). Tương tự hb < (a+c)/2 và hc < (a+b)/2. Cộng ba bất đẳng thức lại ta được ha + hb + hc < a + b + c (0.5đ).")
            ]
        }

print("Loaded c9 bài 1 & bài 2 generator.")
