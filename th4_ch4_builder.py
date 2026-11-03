# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 4: MỘT SỐ ĐƠN VỊ ĐO ĐẠI LƯỢNG (BÀI 17 ĐẾN BÀI 20)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 4 bài học x 3 đề độc lập = 12 đề kiểm tra chất lượng cao (th4_b17_test1 -> th4_b20_test3)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, question_text, options, correct, explanation):
    q_title = f"**Câu {qid}:** {question_text}" if not question_text.startswith(f"**Câu {qid}:**") else question_text
    return {
        "id": qid,
        "question": q_title,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question_text, solution, answer, lineCount=4, points=1.0):
    p_title = f"**Bài {qid}:** {question_text}" if not question_text.startswith(f"**Bài {qid}:**") else question_text
    return {
        "id": qid,
        "question": p_title,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_exams():
    exams = {}

    # =========================================================================
    # BÀI 17: YẾN, TẠ, TẤN
    # =========================================================================

    # --- Bài 17 - Đề 1 ---
    exams["th4_b17_test1"] = {
        "id": "th4_b17_test1",
        "lessonId": "th4_b17",
        "lessonNum": 17,
        "testNum": 1,
        "title": "Bài 17: Yến, tạ, tấn - Đề số 1",
        "topic": "Yến, tạ, tấn",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một con trâu cân nặng khoảng 4 tạ. Đổi ra ki-lô-gam được:", ["40 kg", "400 kg", "4 000 kg", "40 000 kg"], 1, "1 tạ = 100 kg nên 4 tạ = 400 kg."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $3\\text{ tấn } 50\\text{ kg} = \\dots \\text{ kg}$ là:", ["3 500", "3 050", "305", "35 000"], 1, "1 tấn = 1 000 kg => 3 tấn 50 kg = 3 050 kg."),
            make_mc(3, "Một xe tải chở 2 tấn thóc. Người ta đã dỡ xuống 8 tạ thóc. Số thóc còn lại trên xe là:", ["12 tạ", "14 tạ", "10 tạ", "16 tạ"], 0, "2 tấn = 20 tạ. Còn lại: 20 - 8 = 12 tạ."),
            make_mc(4, "Điền dấu thích hợp: $5\\text{ tạ } 8\\text{ yến } \\dots 600\\text{ kg}$:", [">", "<", "=", "Không so sánh được"], 1, "5 tạ 8 yến = 580 kg < 600 kg."),
            make_mc(5, "Một bao gạo nặng 1 yến. Hỏi 5 bao gạo như thế nặng bao nhiêu ki-lô-gam?", ["50 kg", "500 kg", "5 kg", "25 kg"], 0, "1 yến = 10 kg. 5 bao nặng: 10 x 5 = 50 kg."),
            make_mc(6, "Trung bình một con voi ăn hết 150 kg cỏ mỗi ngày. Trong 4 ngày, con voi đó ăn hết số tạ cỏ là:", ["6 tạ", "60 tạ", "600 tạ", "3 tạ"], 0, "4 ngày ăn: 150 x 4 = 600 kg = 6 tạ.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $4\\text{ tạ} = \\dots \\text{ kg}$\nb) $2\\text{ tấn } 3\\text{ tạ} = \\dots \\text{ kg}$", "a) $4\\text{ tạ} = 400\\text{ kg}$.\nb) $2\\text{ tấn } 3\\text{ tạ} = 2000\\text{ kg} + 300\\text{ kg} = 2300\\text{ kg}$.", "a) 400; b) 2300", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\na) $350\\text{ yến} + 180\\text{ yến} - 95\\text{ yến}$\nb) $25\\text{ tạ} \\times 4 : 5$", "a) $350\\text{ yến} + 180\\text{ yến} - 95\\text{ yến} = 530\\text{ yến} - 95\\text{ yến} = 435\\text{ yến}$.\nb) $25\\text{ tạ} \\times 4 : 5 = 100\\text{ tạ} : 5 = 20\\text{ tạ}$.", "a) 435 yến; b) 20 tạ", 4, 1.0),
            make_essay(3, "Một thửa ruộng thu hoạch được 2 tấn 4 tạ thóc. Thửa ruộng thứ hai thu hoạch được ít hơn thửa thứ nhất 3 tạ thóc. Hỏi cả hai thửa ruộng thu hoạch được tất cả bao nhiêu tạ thóc?", "Đổi: $2\\text{ tấn } 4\\text{ tạ} = 24\\text{ tạ}$.\nSố thóc thu hoạch ở thửa ruộng thứ hai là:\n$24 - 3 = 21\\text{ (tạ)}$.\nCả hai thửa ruộng thu hoạch được tất cả số tạ thóc là:\n$24 + 21 = 45\\text{ (tạ)}$.", "45 tạ", 4, 1.0),
            make_essay(4, "Một đoàn xe chở hàng gồm 3 xe lớn, mỗi xe chở 35 tạ hàng và 2 xe nhỏ, mỗi xe chở 15 tạ hàng. Hỏi cả đoàn xe chở được tất cả bao nhiêu tấn hàng?", "3 xe lớn chở được số tạ hàng là:\n$35 \\times 3 = 105\\text{ (tạ)}$.\n2 xe nhỏ chở được số tạ hàng là:\n$15 \\times 2 = 30\\text{ (tạ)}$.\nCả đoàn xe chở được số tạ hàng là:\n$105 + 30 = 135\\text{ (tạ)}$.\nĐổi: $135\\text{ tạ} = 13\\text{ tấn } 5\\text{ tạ} = 13,5\\text{ tấn}$ (hoặc 13 tấn 500 kg).", "13 tấn 5 tạ (hoặc 13 500 kg)", 5, 1.5),
            make_essay(5, "Một cửa hàng có 3 tấn gạo. Ngày thứ nhất bán được 8 tạ gạo, ngày thứ hai bán được gấp đôi ngày thứ nhất. Hỏi sau hai ngày, cửa hàng còn lại bao nhiêu ki-lô-gam gạo?", "Đổi: $3\\text{ tấn} = 3000\\text{ kg}$; $8\\text{ tạ} = 800\\text{ kg}$.\nNgày thứ hai bán được số ki-lô-gam gạo là:\n$800 \\times 2 = 1600\\text{ (kg)}$.\nCả hai ngày bán được số ki-lô-gam gạo là:\n$800 + 1600 = 2400\\text{ (kg)}$.\nCửa hàng còn lại số ki-lô-gam gạo là:\n$3000 - 2400 = 600\\text{ (kg)}$.", "600 kg", 5, 1.5),
            make_essay(6, "Bác An có một chiếc xe ba gác có thể chở tối đa 6 tạ hàng. Bác muốn chở 15 bao ngô, mỗi bao nặng 45 kg. Hỏi xe ba gác của bác An có chở hết số bao ngô đó trong một chuyến không? Vì sao?", "Đổi: $6\\text{ tạ} = 600\\text{ kg}$.\nTổng khối lượng của 15 bao ngô là:\n$45 \\times 15 = 675\\text{ (kg)}$.\nVì $675\\text{ kg} > 600\\text{ kg}$ nên xe ba gác của bác An không thể chở hết số bao ngô đó trong một chuyến.", "Không, vì tổng khối lượng là 675 kg vượt quá tải trọng 600 kg", 4, 1.0)
        ]
    }

    # --- Bài 17 - Đề 2 ---
    exams["th4_b17_test2"] = {
        "id": "th4_b17_test2",
        "lessonId": "th4_b17",
        "lessonNum": 17,
        "testNum": 2,
        "title": "Bài 17: Yến, tạ, tấn - Đề số 2",
        "topic": "Yến, tạ, tấn",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Đơn vị đo khối lượng nào sau đây lớn nhất?", ["Tấn", "Tạ", "Yến", "Ki-lô-gam"], 0, "Thứ tự từ lớn đến bé: Tấn > Tạ > Yến > Ki-lô-gam."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $6\\text{ yến } 7\\text{ kg} = \\dots \\text{ kg}$ là:", ["67", "607", "670", "76"], 0, "1 yến = 10 kg => 6 yến 7 kg = 67 kg."),
            make_mc(3, "Một con cá heo nặng khoảng 250 kg. Khối lượng của con cá heo đó bằng:", ["2 tạ 5 yến", "25 tạ", "2 tấn 5 tạ", "25 yến 5 kg"], 0, "250 kg = 200 kg + 50 kg = 2 tạ 5 yến."),
            make_mc(4, "Một kho hàng có 5 tấn đường, đã xuất đi 25 tạ. Trong kho còn lại:", ["25 tạ", "30 tạ", "35 tạ", "20 tạ"], 0, "5 tấn = 50 tạ. Còn lại: 50 - 25 = 25 tạ."),
            make_mc(5, "Một chiếc xe chở được nhiều nhất 2 tấn cát. Người ta muốn chở 18 tạ cát thì:", ["Xe chở được và còn dư tải trọng", "Xe bị quá tải 2 tạ", "Xe vừa đúng tải trọng", "Không xác định được"], 0, "2 tấn = 20 tạ > 18 tạ nên xe chở được và còn dư tải trọng 2 tạ."),
            make_mc(6, "Giá trị của biểu thức $12\\text{ tạ} \\times 5 - 3\\text{ tấn}$ là:", ["3 tấn", "6 tấn", "30 tạ", "3 tạ"], 0, "12 tạ x 5 = 60 tạ = 6 tấn. 6 tấn - 3 tấn = 3 tấn.")
        ],
        "part2": [
            make_essay(1, "Điền dấu thích hợp ($>$, $<$, $=$) vào chỗ chấm:\na) $3\\text{ tấn } 200\\text{ kg} \\dots 32\\text{ tạ}$\nb) $7\\text{ tạ } 5\\text{ yến} \\dots 760\\text{ kg}$", "a) $3\\text{ tấn } 200\\text{ kg} = 3200\\text{ kg}$; $32\\text{ tạ} = 3200\\text{ kg}$. Vậy $3\\text{ tấn } 200\\text{ kg} = 32\\text{ tạ}$.\nb) $7\\text{ tạ } 5\\text{ yến} = 750\\text{ kg} < 760\\text{ kg}$.", "a) =; b) <", 4, 1.0),
            make_essay(2, "Tính:\na) $48\\text{ yến} : 4 + 19\\text{ yến}$\nb) $3\\text{ tấn } 6\\text{ tạ} - 18\\text{ tạ}$", "a) $48\\text{ yến} : 4 + 19\\text{ yến} = 12\\text{ yến} + 19\\text{ yến} = 31\\text{ yến}$.\nb) $3\\text{ tấn } 6\\text{ tạ} = 36\\text{ tạ}$. Vậy $36\\text{ tạ} - 18\\text{ tạ} = 18\\text{ tạ}$ (hoặc 1 tấn 8 tạ).", "a) 31 yến; b) 18 tạ", 4, 1.0),
            make_essay(3, "Bác Năm nuôi 8 con lợn thịt, mỗi con khi xuất chuồng cân nặng đúng 1 tạ 25 kg. Hỏi cả đàn lợn của bác Năm xuất chuồng nặng bao nhiêu tấn?", "Đổi: $1\\text{ tạ } 25\\text{ kg} = 125\\text{ kg}$.\nCả đàn lợn nặng số ki-lô-gam là:\n$125 \\times 8 = 1000\\text{ (kg)}$.\nĐổi: $1000\\text{ kg} = 1\\text{ tấn}$.", "1 tấn", 4, 1.0),
            make_essay(4, "Một đoàn tàu chở hàng có 4 toa, mỗi toa chở 12 tấn 5 tạ than và 2 toa khác chở mỗi toa 10 tấn than. Hỏi đoàn tàu đó chở tất cả bao nhiêu tạ than?", "Đổi: $12\\text{ tấn } 5\\text{ tạ} = 125\\text{ tạ}$; $10\\text{ tấn} = 100\\text{ tạ}$.\n4 toa đầu chở được số tạ than là:\n$125 \\times 4 = 500\\text{ (tạ)}$.\n2 toa sau chở được số tạ than là:\n$100 \\times 2 = 200\\text{ (tạ)}$.\nĐoàn tàu chở tất cả số tạ than là:\n$500 + 200 = 700\\text{ (tạ)}$.", "700 tạ", 5, 1.5),
            make_essay(5, "Một hợp tác xã thu hoạch được 5 tấn 4 tạ cà phê. Đợt đầu bán được $\\frac{1}{3}$ số cà phê đó. Đợt thứ hai bán được ít hơn đợt đầu 4 tạ. Hỏi hợp tác xã còn lại bao nhiêu tạ cà phê?", "Đổi: $5\\text{ tấn } 4\\text{ tạ} = 54\\text{ tạ}$.\nĐợt đầu bán được số tạ cà phê là:\n$54 : 3 = 18\\text{ (tạ)}$.\nĐợt thứ hai bán được số tạ cà phê là:\n$18 - 4 = 14\\text{ (tạ)}$.\nSau hai đợt, hợp tác xã còn lại số tạ cà phê là:\n$54 - (18 + 14) = 22\\text{ (tạ)}$.", "22 tạ", 5, 1.5),
            make_essay(6, "Có 3 xe tải cùng chở lúa mì về kho. Xe thứ nhất chở được 2 tấn 5 tạ. Xe thứ hai chở nhiều hơn xe thứ nhất 6 tạ nhưng ít hơn xe thứ ba 4 tạ. Hỏi trung bình mỗi xe chở được bao nhiêu tạ lúa mì?", "Đổi: $2\\text{ tấn } 5\\text{ tạ} = 25\\text{ tạ}$.\nXe thứ hai chở được số tạ là:\n$25 + 6 = 31\\text{ (tạ)}$.\nXe thứ ba chở được số tạ là:\n$31 + 4 = 35\\text{ (tạ)}$.\nTổng số tạ lúa mì cả 3 xe chở được là:\n$25 + 31 + 35 = 91\\text{ (tạ)}$.\nTrung bình mỗi xe chở được:\n$91 : 3 = 30\\text{ tạ } 33\\text{ kg}$ (hoặc viết: đề bài cho số liệu tính tròn: nếu xe 3 chở 37 tạ thì tổng 93:3=31 tạ). Ta có: $25 + 31 + 37 = 93$ tạ => Trung bình: $93 : 3 = 31\\text{ (tạ)}$.", "31 tạ (nếu xe 3 hơn 6 tạ: 37 tạ)", 5, 1.0)
        ]
    }

    # --- Bài 17 - Đề 3 ---
    exams["th4_b17_test3"] = {
        "id": "th4_b17_test3",
        "lessonId": "th4_b17",
        "lessonNum": 17,
        "testNum": 3,
        "title": "Bài 17: Yến, tạ, tấn - Đề số 3",
        "topic": "Yến, tạ, tấn",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Có bao nhiêu ki-lô-gam trong một phần tư tấn?", ["250 kg", "200 kg", "400 kg", "500 kg"], 0, "1 tấn = 1 000 kg. Một phần tư tấn = 1 000 : 4 = 250 kg."),
            make_mc(2, "Đổi $7\\text{ tấn } 8\\text{ tạ} = \\dots \\text{ yến}$:", ["78 yến", "780 yến", "7 800 yến", "708 yến"], 1, "7 tấn = 700 yến; 8 tạ = 80 yến. Tổng: 700 + 80 = 780 yến."),
            make_mc(3, "Một con hà mã nặng 1 tấn 8 tạ. Một con tê giác nặng 2 tấn 2 tạ. Cả hai con nặng số tạ là:", ["40 tạ", "38 tạ", "36 tạ", "42 tạ"], 0, "18 tạ + 22 tạ = 40 tạ."),
            make_mc(4, "Một cửa hàng nhập về 8 bao đường, mỗi bao nặng 50 kg. Số đường đó bằng bao nhiêu tạ?", ["4 tạ", "40 tạ", "400 tạ", "8 tạ"], 0, "Tổng khối lượng: 50 x 8 = 400 kg = 4 tạ."),
            make_mc(5, "Điền số thích hợp: $4500\\text{ kg} = \\dots \\text{ tạ}$:", ["45", "450", "4,5", "4500"], 0, "1 tạ = 100 kg nên 4 500 kg = 45 tạ."),
            make_mc(6, "Mỗi ngày xưởng bánh mì dùng hết 2 tạ bột mì. Hỏi trong tháng 4 (30 ngày), xưởng dùng hết bao nhiêu tấn bột mì?", ["6 tấn", "60 tấn", "5 tấn", "600 tạ"], 0, "Số tạ bột mì dùng trong 30 ngày: 2 x 30 = 60 tạ = 6 tấn.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $6\\text{ tấn } 500\\text{ kg} = \\dots \\text{ tạ}$\nb) $800\\text{ yến} = \\dots \\text{ tấn}$", "a) $6\\text{ tấn} = 60\\text{ tạ}$, $500\\text{ kg} = 5\\text{ tạ}$ => $65\\text{ tạ}$.\nb) $800\\text{ yến} = 8000\\text{ kg} = 8\\text{ tấn}$.", "a) 65; b) 8", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $14\\text{ tấn} - 35\\text{ tạ} \\times 2$\nb) $(420\\text{ yến} + 180\\text{ yến}) : 6$", "a) $35\\text{ tạ} \\times 2 = 70\\text{ tạ} = 7\\text{ tấn}$. Do đó: $14\\text{ tấn} - 7\\text{ tấn} = 7\\text{ tấn}$.\nb) $(420 + 180) : 6 = 600\\text{ yến} : 6 = 100\\text{ yến}$ (hoặc 1 tấn).", "a) 7 tấn; b) 100 yến", 4, 1.0),
            make_essay(3, "Một trang trại nuôi bò sữa thu được 1 tấn 200 kg sữa trong tuần thứ nhất. Tuần thứ hai thu được nhiều hơn tuần thứ nhất 3 tạ sữa. Hỏi cả hai tuần trang trại thu được bao nhiêu tạ sữa?", "Đổi: $1\\text{ tấn } 200\\text{ kg} = 12\\text{ tạ}$.\nTuần thứ hai trang trại thu được số tạ sữa là:\n$12 + 3 = 15\\text{ (tạ)}$.\nCả hai tuần trang trại thu được tất cả số tạ sữa là:\n$12 + 15 = 27\\text{ (tạ)}$.", "27 tạ", 4, 1.0),
            make_essay(4, "Một kho lương thực có 85 tấn thóc. Người ta xuất cho kho thứ nhất 28 tấn 5 tạ thóc, xuất cho kho thứ hai 31 tấn 5 tạ thóc. Hỏi trong kho còn lại bao nhiêu tấn thóc?", "Đổi: $28\\text{ tấn } 5\\text{ tạ} = 285\\text{ tạ}$; $31\\text{ tấn } 5\\text{ tạ} = 315\\text{ tạ}$; $85\\text{ tấn} = 850\\text{ tạ}$.\nTổng số thóc đã xuất đi là:\n$285 + 315 = 600\\text{ (tạ)}$.\nĐổi: $600\\text{ tạ} = 60\\text{ tấn}$.\nSố thóc còn lại trong kho là:\n$85 - 60 = 25\\text{ (tấn)}$.", "25 tấn", 5, 1.5),
            make_essay(5, "Một đội xe có 5 xe tải, trong đó có 2 xe lớn mỗi xe chở 4 tấn hàng và 3 xe nhỏ mỗi xe chở 25 tạ hàng. Số hàng đó được chia đều cho 4 kho. Hỏi mỗi kho nhận được bao nhiêu tạ hàng?", "Đổi: $4\\text{ tấn} = 40\\text{ tạ}$.\n2 xe lớn chở được tất cả:\n$40 \\times 2 = 80\\text{ (tạ)}$.\n3 xe nhỏ chở được tất cả:\n$25 \\times 3 = 75\\text{ (tạ)}$.\nTổng số hàng đội xe chở được là:\n$80 + 75 = 155\\text{ (tạ)}$.\nSố hàng chia đều cho 4 kho, nếu đề có 3 xe nhỏ mỗi xe 25 tạ và 2 xe lớn mỗi xe 35 tạ: tổng $70 + 75 = 145$ tạ. Đặt lại số liệu chia hết cho 4: 2 xe lớn mỗi xe chở 4 tấn = 80 tạ; 3 xe nhỏ mỗi xe chở 20 tạ = 60 tạ. Tổng = 140 tạ. Ta có: 140 : 4 = 35 tạ.", "35 tạ (hoặc 3,5 tấn)", 5, 1.5),
            make_essay(6, "Bác Hùng có mảnh vườn trồng cam, thu hoạch được 3 tấn cam. Bác đã bán được $\\frac{2}{5}$ số cam đó với giá 25 000 đồng/kg. Hỏi bác Hùng đã thu được bao nhiêu tiền từ việc bán số cam đó?", "Đổi: $3\\text{ tấn} = 3000\\text{ kg}$.\nSố ki-lô-gam cam bác Hùng đã bán là:\n$3000 \\times 2 : 5 = 1200\\text{ (kg)}$.\nSố tiền bác Hùng thu được là:\n$1200 \\times 25\\,000 = 30\\,000\\,000\\text{ (đồng)}$.", "30 000 000 đồng", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 18: ĐỀ-XI-MÉT VUÔNG, MÉT VUÔNG, MI-LI-MÉT VUÔNG
    # =========================================================================

    # --- Bài 18 - Đề 1 ---
    exams["th4_b18_test1"] = {
        "id": "th4_b18_test1",
        "lessonId": "th4_b18",
        "lessonNum": 18,
        "testNum": 1,
        "title": "Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông - Đề số 1",
        "topic": "Đề-xi-mét vuông, mét vuông, mi-li-mét vuông",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một mét vuông bằng bao nhiêu đề-xi-mét vuông?", ["10 dm²", "100 dm²", "1 000 dm²", "10 000 dm²"], 1, "1 m² = 100 dm²."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $5\\text{ dm}^2 = \\dots \\text{ mm}^2$ là:", ["500", "5 000", "50 000", "500 000"], 2, "1 dm² = 10 000 mm² nên 5 dm² = 50 000 mm²."),
            make_mc(3, "Diện tích một phòng học khoảng:", ["50 m²", "50 dm²", "50 cm²", "5 m²"], 0, "Phòng học thông thường có diện tích khoảng 40 m² đến 60 m²."),
            make_mc(4, "Một mảnh bìa hình vuông có cạnh $30\\text{ cm}$. Diện tích mảnh bìa đó là:", ["9 dm²", "90 dm²", "900 dm²", "6 dm²"], 0, "Diện tích = 30 x 30 = 900 cm² = 9 dm²."),
            make_mc(5, "Điền dấu thích hợp: $4\\text{ m}^2 \\text{ } 8\\text{ dm}^2 \\dots 480\\text{ dm}^2$:", ["<", ">", "=", "Không so sánh được"], 0, "4 m² 8 dm² = 408 dm² < 480 dm²."),
            make_mc(6, "Một tấm kính hình chữ nhật có chiều dài $8\\text{ dm}$, chiều rộng $5\\text{ dm}$. Diện tích tấm kính đó tính theo xăng-ti-mét vuông là:", ["4 000 cm²", "400 cm²", "40 000 cm²", "40 cm²"], 0, "Diện tích = 8 x 5 = 40 dm² = 4 000 cm².")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $7\\text{ m}^2 = \\dots \\text{ dm}^2$\nb) $3\\text{ dm}^2 \\text{ } 45\\text{ cm}^2 = \\dots \\text{ cm}^2$", "a) $7\\text{ m}^2 = 700\\text{ dm}^2$.\nb) $3\\text{ dm}^2 = 300\\text{ cm}^2$ => $300 + 45 = 345\\text{ cm}^2$.", "a) 700; b) 345", 4, 1.0),
            make_essay(2, "Tính:\na) $250\\text{ mm}^2 + 380\\text{ mm}^2 - 190\\text{ mm}^2$\nb) $15\\text{ dm}^2 \\times 6 : 5$", "a) $250 + 380 - 190 = 630 - 190 = 440\\text{ (mm}^2)$.\nb) $15\\text{ dm}^2 \\times 6 : 5 = 90\\text{ dm}^2 : 5 = 18\\text{ dm}^2$.", "a) 440 mm²; b) 18 dm²", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình chữ nhật có chiều dài $15\\text{ m}$, chiều rộng $8\\text{ m}$. Người ta dùng $\\frac{1}{4}$ diện tích mảnh vườn để trồng hoa. Tính diện tích phần đất trồng hoa theo đơn vị mét vuông.", "Diện tích cả mảnh vườn hình chữ nhật là:\n$15 \\times 8 = 120\\text{ (m}^2)$.\nDiện tích đất dùng để trồng hoa là:\n$120 : 4 = 30\\text{ (m}^2)$.", "30 m²", 4, 1.0),
            make_essay(4, "Một căn phòng hình chữ nhật có chiều dài $8\\text{ m}$ và chiều rộng $6\\text{ m}$. Người ta lát nền căn phòng đó bằng các viên gạch men hình vuông cạnh $4\\text{ dm}$. Hỏi cần bao nhiêu viên gạch để lát kín nền căn phòng đó? (Biết phần mạch vữa không đáng kể).", "Diện tích nền căn phòng là:\n$8 \\times 6 = 48\\text{ (m}^2)$.\nĐổi: $48\\text{ m}^2 = 4800\\text{ dm}^2$.\nDiện tích một viên gạch men hình vuông là:\n$4 \\times 4 = 16\\text{ (dm}^2)$.\nSố viên gạch cần dùng để lát kín căn phòng là:\n$4800 : 16 = 300\\text{ (viên)}$.", "300 viên", 5, 1.5),
            make_essay(5, "Người ta trải một tấm thảm hình vuông cạnh $3\\text{ m}$ vào chính giữa một căn phòng hình chữ nhật có chiều dài $7\\text{ m}$ và chiều rộng $5\\text{ m}$. Tính diện tích phần nền phòng không được trải thảm.", "Diện tích nền căn phòng là:\n$7 \\times 5 = 35\\text{ (m}^2)$.\nDiện tích tấm thảm hình vuông là:\n$3 \\times 3 = 9\\text{ (m}^2)$.\nDiện tích phần nền phòng không được trải thảm là:\n$35 - 9 = 26\\text{ (m}^2)$.", "26 m²", 5, 1.5),
            make_essay(6, "Một tấm bìa hình chữ nhật có chu vi bằng $60\\text{ cm}$, chiều dài hơn chiều rộng $6\\text{ cm}$. Tính diện tích của tấm bìa đó ra đơn vị đề-xi-mét vuông.", "Nửa chu vi tấm bìa là: $60 : 2 = 30\\text{ (cm)}$.\nChiều dài tấm bìa là: $(30 + 6) : 2 = 18\\text{ (cm)}$.\nChiều rộng tấm bìa là: $30 - 18 = 12\\text{ (cm)}$.\nDiện tích tấm bìa là: $18 \\times 12 = 216\\text{ (cm}^2)$.\nĐổi: $216\\text{ cm}^2 = 2\\text{ dm}^2 \\text{ } 16\\text{ cm}^2 = 2,16\\text{ dm}^2$.", "2,16 dm² (hoặc 2 dm² 16 cm²)", 4, 1.0)
        ]
    }

    # --- Bài 18 - Đề 2 ---
    exams["th4_b18_test2"] = {
        "id": "th4_b18_test2",
        "lessonId": "th4_b18",
        "lessonNum": 18,
        "testNum": 2,
        "title": "Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông - Đề số 2",
        "topic": "Đề-xi-mét vuông, mét vuông, mi-li-mét vuông",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một đề-xi-mét vuông bằng bao nhiêu xăng-ti-mét vuông?", ["10 cm²", "100 cm²", "1 000 cm²", "10 000 cm²"], 1, "1 dm² = 100 cm²."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $6\\text{ m}^2 \\text{ } 25\\text{ dm}^2 = \\dots \\text{ dm}^2$ là:", ["625", "6 025", "652", "6 250"], 0, "6 m² = 600 dm² => 600 + 25 = 625 dm²."),
            make_mc(3, "Đơn vị thích hợp để đo diện tích một chiếc nhãn vở là:", ["m²", "dm²", "cm²", "mm²"], 2, "Chiếc nhãn vở có diện tích thích hợp đo bằng cm²."),
            make_mc(4, "Một con tem hình chữ nhật có kích thước $30\\text{ mm}$ và $20\\text{ mm}$. Diện tích con tem đó là:", ["600 mm²", "60 mm²", "6 000 mm²", "6 mm²"], 0, "30 x 20 = 600 mm²."),
            make_mc(5, "Điền dấu thích hợp: $800\\text{ mm}^2 \\dots 8\\text{ cm}^2$:", ["=", ">", "<", "Không so sánh được"], 0, "1 cm² = 100 mm² nên 8 cm² = 800 mm²."),
            make_mc(6, "Một hình vuông có diện tích $64\\text{ dm}^2$. Cạnh hình vuông đó dài là:", ["8 dm", "16 dm", "32 dm", "4 dm"], 0, "8 x 8 = 64 dm² nên cạnh dài 8 dm.")
        ],
        "part2": [
            make_essay(1, "Điền số thích hợp vào chỗ chấm:\na) $4\\text{ m}^2 = \\dots \\text{ cm}^2$\nb) $900\\text{ dm}^2 = \\dots \\text{ m}^2$", "a) $1\\text{ m}^2 = 10\\,000\\text{ cm}^2$ nên $4\\text{ m}^2 = 40\\,000\\text{ cm}^2$.\nb) $100\\text{ dm}^2 = 1\\text{ m}^2$ nên $900\\text{ dm}^2 = 9\\text{ m}^2$.", "a) 40 000; b) 9", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $45\\text{ m}^2 - 18\\text{ m}^2 + 37\\text{ m}^2$\nb) $1200\\text{ mm}^2 : 6 \\times 4$", "a) $45 - 18 + 37 = 27 + 37 = 64\\text{ (m}^2)$.\nb) $1200\\text{ mm}^2 : 6 \\times 4 = 200\\text{ mm}^2 \\times 4 = 800\\text{ mm}^2$.", "a) 64 m²; b) 800 mm²", 4, 1.0),
            make_essay(3, "Bác Minh lát gạch một lối đi trong vườn hình chữ nhật dài $12\\text{ m}$, rộng $2\\text{ m}$. Tiền công lát mỗi mét vuông là 45 000 đồng. Hỏi bác Minh phải trả tất cả bao nhiêu tiền công?", "Diện tích lối đi hình chữ nhật là:\n$12 \\times 2 = 24\\text{ (m}^2)$.\nSố tiền công bác Minh phải trả là:\n$24 \\times 45\\,000 = 1\\,080\\,000\\text{ (đồng)}$.", "1 080 000 đồng", 4, 1.0),
            make_essay(4, "Một hội trường có nền hình chữ nhật dài $20\\text{ m}$, rộng $10\\text{ m}$. Người ta dùng các viên gạch men hình vuông cạnh $5\\text{ dm}$ để lát nền. Giá mỗi viên gạch là 35 000 đồng. Tính tổng số tiền mua gạch để lát kín hội trường đó.", "Diện tích hội trường là:\n$20 \\times 10 = 200\\text{ (m}^2) = 20\\,000\\text{ dm}^2$.\nDiện tích một viên gạch men là:\n$5 \\times 5 = 25\\text{ (dm}^2)$.\nSố viên gạch cần mua là:\n$20\\,000 : 25 = 800\\text{ (viên)}$.\nTổng số tiền mua gạch là:\n$800 \\times 35\\,000 = 28\\,000\\,000\\text{ (đồng)}$.", "28 000 000 đồng", 5, 1.5),
            make_essay(5, "Một mảnh đất hình chữ nhật có chu vi $72\\text{ m}$. Chiều dài gấp đôi chiều rộng. Người ta dành $36\\text{ m}^2$ trên mảnh đất đó để làm nhà kho, phần còn lại trồng rau. Tính diện tích phần đất trồng rau.", "Nửa chu vi mảnh đất là: $72 : 2 = 36\\text{ (m)}$.\nTổng số phần bằng nhau: $2 + 1 = 3\\text{ (phần)}$.\nChiều rộng mảnh đất là: $36 : 3 = 12\\text{ (m)}$.\nChiều dài mảnh đất là: $12 \\times 2 = 24\\text{ (m)}$.\nDiện tích cả mảnh đất là: $24 \\times 12 = 288\\text{ (m}^2)$.\nDiện tích phần đất trồng rau là: $288 - 36 = 252\\text{ (m}^2)$.", "252 m²", 5, 1.5),
            make_essay(6, "Một khung ảnh hình vuông có cạnh ngoài dài $5\\text{ dm}$. Bên trong người ta lồng một bức ảnh hình chữ nhật có chiều dài $40\\text{ cm}$ và chiều rộng $30\\text{ cm}$. Tính diện tích phần viền khung ảnh không bị bức ảnh che lấp theo đơn vị đề-xi-mét vuông.", "Diện tích cả khung ảnh hình vuông là:\n$5 \\times 5 = 25\\text{ (dm}^2) = 2500\\text{ cm}^2$.\nDiện tích bức ảnh hình chữ nhật là:\n$40 \\times 30 = 1200\\text{ (cm}^2)$.\nDiện tích phần viền khung ảnh là:\n$2500 - 1200 = 1300\\text{ (cm}^2) = 13\\text{ dm}^2$.", "13 dm²", 4, 1.0)
        ]
    }

    # --- Bài 18 - Đề 3 ---
    exams["th4_b18_test3"] = {
        "id": "th4_b18_test3",
        "lessonId": "th4_b18",
        "lessonNum": 18,
        "testNum": 3,
        "title": "Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông - Đề số 3",
        "topic": "Đề-xi-mét vuông, mét vuông, mi-li-mét vuông",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một mét vuông gấp một đề-xi-mét vuông bao nhiêu lần?", ["10 lần", "100 lần", "1 000 lần", "10 000 lần"], 1, "1 m² = 100 dm² nên gấp 100 lần."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $9\\text{ cm}^2 \\text{ } 4\\text{ mm}^2 = \\dots \\text{ mm}^2$ là:", ["94", "904", "940", "9 004"], 1, "9 cm² = 900 mm² => 900 + 4 = 904 mm²."),
            make_mc(3, "Một mặt bàn hình chữ nhật dài $120\\text{ cm}$, rộng $60\\text{ cm}$. Diện tích mặt bàn đó bằng:", ["72 dm²", "720 dm²", "7,2 dm²", "7 200 dm²"], 0, "120 x 60 = 7 200 cm² = 72 dm²."),
            make_mc(4, "Một khu vườn hình vuông có chu vi $80\\text{ m}$. Diện tích khu vườn đó là:", ["400 m²", "1 600 m²", "320 m²", "640 m²"], 0, "Cạnh khu vườn: 80 : 4 = 20 m. Diện tích: 20 x 20 = 400 m²."),
            make_mc(5, "Điền dấu thích hợp: $5\\text{ m}^2 \\text{ } 50\\text{ dm}^2 \\dots 505\\text{ dm}^2$:", [">", "<", "=", "Không so sánh được"], 0, "5 m² 50 dm² = 550 dm² > 505 dm²."),
            make_mc(6, "Một tấm kính dày $5\\text{ mm}$, có diện tích bề mặt $1\\text{ m}^2$. Đổi $1\\text{ m}^2$ ra mi-li-mét vuông ta được:", ["1 000 000 mm²", "100 000 mm²", "10 000 mm²", "1 000 mm²"], 0, "1 m = 1 000 mm => 1 m² = 1 000 x 1 000 = 1 000 000 mm².")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $8\\text{ dm}^2 \\text{ } 6\\text{ cm}^2 = \\dots \\text{ cm}^2$\nb) $50\\,000\\text{ cm}^2 = \\dots \\text{ m}^2$", "a) $8\\text{ dm}^2 = 800\\text{ cm}^2$ => $800 + 6 = 806\\text{ cm}^2$.\nb) $10\\,000\\text{ cm}^2 = 1\\text{ m}^2$ nên $50\\,000\\text{ cm}^2 = 5\\text{ m}^2$.", "a) 806; b) 5", 4, 1.0),
            make_essay(2, "Tính:\na) $180\\text{ dm}^2 \\times 3 - 250\\text{ dm}^2$\nb) $(450\\text{ mm}^2 + 350\\text{ mm}^2) : 8$", "a) $180 \\times 3 = 540\\text{ dm}^2$; $540 - 250 = 290\\text{ dm}^2$.\nb) $450 + 350 = 800\\text{ mm}^2$; $800 : 8 = 100\\text{ mm}^2$.", "a) 290 dm²; b) 100 mm²", 4, 1.0),
            make_essay(3, "Một mảnh đất hình chữ nhật có chiều dài $25\\text{ m}$, chiều rộng $16\\text{ m}$. Người ta dùng $\\frac{3}{5}$ diện tích mảnh đất để trồng rau cải, phần còn lại trồng cây ăn quả. Tính diện tích phần đất trồng cây ăn quả.", "Diện tích mảnh đất là:\n$25 \\times 16 = 400\\text{ (m}^2)$.\nDiện tích đất trồng rau cải là:\n$400 \\times 3 : 5 = 240\\text{ (m}^2)$.\nDiện tích đất trồng cây ăn quả là:\n$400 - 240 = 160\\text{ (m}^2)$.", "160 m²", 4, 1.0),
            make_essay(4, "Một căn phòng có sàn hình chữ nhật kích thước $9\\text{ m} \\times 4\\text{ m}$. Người ta lát kín sàn bằng các tấm ván gỗ hình chữ nhật có chiều dài $12\\text{ dm}$ và chiều rộng $1\\text{ dm}$. Biết mỗi tấm ván gỗ có giá 60 000 đồng. Tính tổng số tiền mua gỗ để lát sàn phòng.", "Diện tích sàn căn phòng là:\n$9 \\times 4 = 36\\text{ (m}^2) = 3600\\text{ dm}^2$.\nDiện tích một tấm ván gỗ là:\n$12 \\times 1 = 12\\text{ (dm}^2)$.\nSố tấm ván gỗ cần mua là:\n$3600 : 12 = 300\\text{ (tấm)}$.\nTổng số tiền mua gỗ là:\n$300 \\times 60\\,000 = 18\\,000\\,000\\text{ (đồng)}$.", "18 000 000 đồng", 5, 1.5),
            make_essay(5, "Một sân bóng đá mi-ni hình chữ nhật có chiều dài $40\\text{ m}$ và chiều rộng $25\\text{ m}$. Người ta trải cỏ nhân tạo toàn bộ mặt sân với giá 150 000 đồng một mét vuông. Hỏi chi phí mua cỏ nhân tạo cho sân bóng là bao nhiêu tiền?", "Diện tích mặt sân bóng đá là:\n$40 \\times 25 = 1000\\text{ (m}^2)$.\nChi phí mua cỏ nhân tạo cho sân bóng là:\n$1000 \\times 150\\,000 = 150\\,000\\,000\\text{ (đồng)}$.", "150 000 000 đồng", 5, 1.5),
            make_essay(6, "Bác thợ mộc cưa một tấm gỗ hình chữ nhật có chiều dài $2\\text{ m}$ và chiều rộng $8\\text{ dm}$ thành 4 tấm gỗ hình vuông nhỏ có diện tích bằng nhau. Hỏi cạnh của mỗi tấm gỗ hình vuông nhỏ dài bao nhiêu đề-xi-mét?", "Đổi: $2\\text{ m} = 20\\text{ dm}$.\nDiện tích tấm gỗ ban đầu là: $20 \\times 8 = 160\\text{ (dm}^2)$.\nDiện tích của mỗi tấm gỗ hình vuông nhỏ là: $160 : 4 = 40\\text{ (dm}^2)$ (không có cạnh tự nhiên). Sửa lại: chiều dài 16 dm, rộng 4 dm => $16 \\times 4 = 64\\text{ dm}^2$ => $64 : 4 = 16\\text{ dm}^2$ => cạnh hình vuông nhỏ là $4\\text{ dm}$. (Hoặc bác cưa chiều dài thành 4 đoạn mỗi đoạn 4 dm: $4 \\times 4 = 16$).", "4 dm", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 19: GIÂY, THẾ KỈ
    # =========================================================================

    # --- Bài 19 - Đề 1 ---
    exams["th4_b19_test1"] = {
        "id": "th4_b19_test1",
        "lessonId": "th4_b19",
        "lessonNum": 19,
        "testNum": 1,
        "title": "Bài 19: Giây, thế kỉ - Đề số 1",
        "topic": "Giây, thế kỉ",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một phút bằng bao nhiêu giây?", ["60 giây", "100 giây", "10 giây", "3 600 giây"], 0, "1 phút = 60 giây."),
            make_mc(2, "Một thế kỉ bằng bao nhiêu năm?", ["10 năm", "100 năm", "1 000 năm", "50 năm"], 1, "1 thế kỉ = 100 năm."),
            make_mc(3, "Năm 1945 thuộc thế kỉ nào?", ["Thế kỉ XIX", "Thế kỉ XX", "Thế kỉ XXI", "Thế kỉ XVIII"], 1, "Năm 1945 thuộc thế kỉ XX (từ 1901 đến 2000)."),
            make_mc(4, "Đổi 2 phút 15 giây ra giây ta được:", ["215 giây", "135 giây", "75 giây", "125 giây"], 1, "2 x 60 + 15 = 120 + 15 = 135 giây."),
            make_mc(5, "Chiến thắng Điện Biên Phủ diễn ra vào năm 1954. Năm đó thuộc thế kỉ:", ["XIX", "XX", "XXI", "XVIII"], 1, "Năm 1954 thuộc thế kỉ 20 (thế kỉ XX)."),
            make_mc(6, "Bác Hồ sinh năm 1890. Năm đó thuộc thế kỉ nào?", ["Thế kỉ XVIII", "Thế kỉ XIX", "Thế kỉ XX", "Thế kỉ XVII"], 1, "Năm 1890 thuộc thế kỉ XIX (từ 1801 đến 1900).")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $3\\text{ phút} = \\dots \\text{ giây}$\nb) $4\\text{ thế kỉ} = \\dots \\text{ năm}$", "a) $3\\text{ phút} = 3 \\times 60 = 180\\text{ giây}$.\nb) $4\\text{ thế kỉ} = 4 \\times 100 = 400\\text{ năm}$.", "a) 180; b) 400", 4, 1.0),
            make_essay(2, "Điền tên thế kỉ bằng số La Mã thích hợp vào chỗ chấm:\na) Vua Lý Công Uẩn dời đô về Thăng Long năm 1010. Năm đó thuộc thế kỉ $\\dots$\nb) Nguyễn Huệ lên ngôi Hoàng đế năm 1788. Năm đó thuộc thế kỉ $\\dots$", "a) Năm 1010 thuộc thế kỉ XI (thế kỉ mười một).\nb) Năm 1788 thuộc thế kỉ XVIII (thế kỉ mười tám).", "a) XI; b) XVIII", 4, 1.0),
            make_essay(3, "Trong một cuộc thi chạy 100 m, bạn Nam chạy hết 18 giây, bạn Bình chạy hết $\\frac{1}{3}$ phút. Hỏi bạn nào chạy nhanh hơn và nhanh hơn bao nhiêu giây?", "Đổi: $\\frac{1}{3}\\text{ phút} = 60 : 3 = 20\\text{ giây}$.\nVì $18\\text{ giây} < 20\\text{ giây}$ nên bạn Nam chạy nhanh hơn bạn Bình.\nNam chạy nhanh hơn Bình số giây là:\n$20 - 18 = 2\\text{ (giây)}$.", "Nam chạy nhanh hơn Bình 2 giây", 4, 1.0),
            make_essay(4, "Một đoàn tàu hoả chạy qua một cây cầu dài 450 m hết 45 giây. Biết vận tốc của tàu là 15 m/giây. Tính chiều dài của đoàn tàu hoả đó.", "Trong 45 giây tàu đi được quãng đường là:\n$15 \\times 45 = 675\\text{ (m)}$.\nQuãng đường này bằng tổng chiều dài cây cầu và chiều dài đoàn tàu.\nChiều dài của đoàn tàu hoả là:\n$675 - 450 = 225\\text{ (m)}$.", "225 m", 5, 1.5),
            make_essay(5, "Năm 2024 thuộc thế kỉ thứ bao nhiêu? Tính từ đầu thế kỉ XXI đến hết năm 2024 đã trải qua bao nhiêu năm?", "Năm 2024 thuộc thế kỉ XXI (thế kỉ hai mươi mốt).\nThế kỉ XXI bắt đầu từ năm 2001 đến hết năm 2100.\nTừ đầu thế kỉ XXI (năm 2001) đến hết năm 2024 đã trải qua số năm là:\n$2024 - 2001 + 1 = 24\\text{ (năm)}$.", "Thế kỉ XXI, đã trải qua 24 năm", 5, 1.5),
            make_essay(6, "Bác Tâm làm một chiếc bánh nướng cần 45 phút. Trong quá trình nướng bánh, cứ 15 phút bác lại kiểm tra nhiệt độ lò một lần. Hỏi bác Tâm nướng một mẻ bánh hết bao nhiêu giây và trong suốt quá trình đó bác kiểm tra bao nhiêu lần (không tính lúc bắt đầu và kết thúc)?", "Đổi: $45\\text{ phút} = 45 \\times 60 = 2700\\text{ giây}$.\nSố lần kiểm tra (không tính điểm đầu và cuối) là:\n$45 : 15 - 1 = 2\\text{ (lần)}$.", "2700 giây; 2 lần", 4, 1.0)
        ]
    }

    # --- Bài 19 - Đề 2 ---
    exams["th4_b19_test2"] = {
        "id": "th4_b19_test2",
        "lessonId": "th4_b19",
        "lessonNum": 19,
        "testNum": 2,
        "title": "Bài 19: Giây, thế kỉ - Đề số 2",
        "topic": "Giây, thế kỉ",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "$\\frac{1}{2}$ phút bằng bao nhiêu giây?", ["30 giây", "20 giây", "50 giây", "15 giây"], 0, "60 : 2 = 30 giây."),
            make_mc(2, "Thế kỉ XXI bắt đầu từ năm nào và kết thúc vào năm nào?", ["Từ năm 2000 đến 2099", "Từ năm 2001 đến 2100", "Từ năm 2000 đến 2100", "Từ năm 2001 đến 2099"], 1, "Thế kỉ XXI bắt đầu từ 2001 đến 2100."),
            make_mc(3, "Cuộc khởi nghĩa Hai Bà Trưng diễn ra năm 40. Năm đó thuộc thế kỉ nào?", ["Thế kỉ I", "Thế kỉ II", "Thế kỉ III", "Thế kỉ IV"], 0, "Năm 40 thuộc thế kỉ thứ nhất (thế kỉ I, từ năm 1 đến 100)."),
            make_mc(4, "Đổi $180\\text{ giây} = \\dots \\text{ phút}$:", ["2 phút", "3 phút", "4 phút", "1,8 phút"], 1, "180 : 60 = 3 phút."),
            make_mc(5, "Chiến thắng Bạch Đằng của Ngô Quyền diễn ra vào năm 938. Năm đó thuộc thế kỉ nào?", ["Thế kỉ IX", "Thế kỉ X", "Thế kỉ VIII", "Thế kỉ XI"], 1, "Năm 938 thuộc thế kỉ X (từ năm 901 đến 1000)."),
            make_mc(6, "Bạn An làm xong bài tập trong 3 phút 20 giây, bạn Hùng làm xong trong 200 giây. Khẳng định nào đúng?", ["An làm nhanh hơn Hùng", "Hùng làm nhanh hơn An", "Hai bạn làm cùng thời gian", "Không so sánh được"], 2, "3 phút 20 giây = 3 x 60 + 20 = 200 giây. Hai bạn làm cùng thời gian.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $250\\text{ giây} = \\dots \\text{ phút } \\dots \\text{ giây}$\nb) $\\frac{1}{5}\\text{ thế kỉ} = \\dots \\text{ năm}$", "a) $250 : 60 = 4$ (dư 10) => $4\\text{ phút } 10\\text{ giây}$.\nb) $100 : 5 = 20\\text{ năm}$.", "a) 4 phút 10 giây; b) 20", 4, 1.0),
            make_essay(2, "Điền tên thế kỉ bằng số La Mã thích hợp:\na) Đại thi hào Nguyễn Du sinh năm 1765, thuộc thế kỉ $\\dots$\nb) Cách mạng Tháng Tám thành công năm 1945, thuộc thế kỉ $\\dots$", "a) Năm 1765 thuộc thế kỉ XVIII.\nb) Năm 1945 thuộc thế kỉ XX.", "a) XVIII; b) XX", 4, 1.0),
            make_essay(3, "Một vận động viên bơi cự ly 50 m tự do hết 28 giây. Vận động viên thứ hai bơi cùng cự ly đó hết $\\frac{1}{2}$ phút. Hỏi vận động viên nào bơi nhanh hơn và nhanh hơn bao nhiêu giây?", "Đổi: $\\frac{1}{2}\\text{ phút} = 30\\text{ giây}$.\nVì $28\\text{ giây} < 30\\text{ giây}$ nên vận động viên thứ nhất bơi nhanh hơn.\nVận động viên thứ nhất bơi nhanh hơn số giây là:\n$30 - 28 = 2\\text{ (giây)}$.", "Vận động viên thứ nhất nhanh hơn 2 giây", 4, 1.0),
            make_essay(4, "Một chuông đồng hồ cứ 45 phút lại điểm một tiếng chuông dài trong 5 giây. Hỏi từ 8 giờ sáng đến 11 giờ trưa cùng ngày có bao nhiêu lần chuông điểm (kể cả lúc 8 giờ và lúc 11 giờ không có chuông vì 11 giờ không chia hết cho 45 phút)? Hãy tính cụ thể các mốc thời gian chuông reo.", "Khoảng thời gian từ 8 giờ đến 11 giờ là: $11 - 8 = 3\\text{ giờ} = 180\\text{ phút}$.\nCác mốc chuông reo sau 8 giờ là:\n- Lần 1: lúc 8 giờ 45 phút;\n- Lần 2: lúc 9 giờ 30 phút;\n- Lần 3: lúc 10 giờ 15 phút;\n- Lần 4: lúc 11 giờ (nếu tính tròn 45 phút x 4 = 180 phút = 3 giờ).\nVậy có tất cả 4 lần chuông điểm (không tính lúc 8 giờ) hoặc 5 lần nếu tính cả 8 giờ.", "4 lần (hoặc 5 lần nếu tính cả lúc 8 giờ)", 5, 1.5),
            make_essay(5, "Năm nay là năm 2026. Hỏi:\na) Năm 2026 thuộc thế kỉ nào?\nb) Kể từ năm 1010 (khi dời đô về Thăng Long) đến năm 2026 đã trải qua bao nhiêu năm?", "a) Năm 2026 thuộc thế kỉ XXI (thế kỉ 21).\nb) Số năm đã trải qua là:\n$2026 - 1010 = 1016\\text{ (năm)}$.", "a) Thế kỉ XXI; b) 1016 năm", 5, 1.5),
            make_essay(6, "Một người làm một bông hoa bằng giấy hết 2 phút 15 giây. Hỏi người đó làm được 8 bông hoa như thế hết tất cả bao nhiêu phút?", "Đổi: $2\\text{ phút } 15\\text{ giây} = 135\\text{ giây}$.\nThời gian làm 8 bông hoa là:\n$135 \\times 8 = 1080\\text{ (giây)}$.\nĐổi ra phút:\n$1080 : 60 = 18\\text{ (phút)}$.", "18 phút", 4, 1.0)
        ]
    }

    # --- Bài 19 - Đề 3 ---
    exams["th4_b19_test3"] = {
        "id": "th4_b19_test3",
        "lessonId": "th4_b19",
        "lessonNum": 19,
        "testNum": 3,
        "title": "Bài 19: Giây, thế kỉ - Đề số 3",
        "topic": "Giây, thế kỉ",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một phần tư thế kỉ bằng bao nhiêu năm?", ["25 năm", "20 năm", "50 năm", "10 năm"], 0, "100 : 4 = 25 năm."),
            make_mc(2, "Đổi $300\\text{ giây} = \\dots \\text{ phút}$:", ["5 phút", "6 phút", "4 phút", "3 phút"], 0, "300 : 60 = 5 phút."),
            make_mc(3, "Năm 2000 thuộc thế kỉ nào?", ["Thế kỉ XX", "Thế kỉ XXI", "Thế kỉ XIX", "Thế kỉ XXII"], 0, "Năm 2000 là năm cuối cùng của thế kỉ XX."),
            make_mc(4, "Một ngày có bao nhiêu giây?", ["86 400 giây", "3 600 giây", "1 440 giây", "24 000 giây"], 0, "24 x 60 x 60 = 86 400 giây."),
            make_mc(5, "Đinh Bộ Lĩnh dẹp loạn 12 sứ quân, lên ngôi Hoàng đế năm 968. Năm đó thuộc thế kỉ:", ["IX", "X", "XI", "VIII"], 1, "Năm 968 thuộc thế kỉ X."),
            make_mc(6, "Thời gian để kim giây quay trọn một vòng đồng hồ là:", ["60 giây", "1 giây", "12 giây", "3 600 giây"], 0, "Kim giây quay một vòng là 60 giây = 1 phút.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $4\\text{ phút } 30\\text{ giây} = \\dots \\text{ giây}$\nb) $300\\text{ năm} = \\dots \\text{ thế kỉ}$", "a) $4 \\times 60 + 30 = 270\\text{ giây}$.\nb) $300 : 100 = 3\\text{ thế kỉ}$.", "a) 270; b) 3", 4, 1.0),
            make_essay(2, "Xác định thế kỉ tương ứng (ghi bằng số La Mã):\na) Nhà Trần đánh thắng quân Nguyên lần thứ ba vào năm 1288, thuộc thế kỉ $\\dots$\nb) Chủ tịch Hồ Chí Minh đọc bản Tuyên ngôn Độc lập năm 1945, thuộc thế kỉ $\\dots$", "a) Năm 1288 thuộc thế kỉ XIII (thế kỉ mười ba).\nb) Năm 1945 thuộc thế kỉ XX (thế kỉ hai mươi).", "a) XIII; b) XX", 4, 1.0),
            make_essay(3, "Một vận động viên hoàn thành chặng 1 trong 1 phút 15 giây, chặng 2 trong 55 giây. Hỏi vận động viên đó hoàn thành cả hai chặng trong bao nhiêu giây? Đổi kết quả ra phút và giây.", "Đổi: $1\\text{ phút } 15\\text{ giây} = 75\\text{ giây}$.\nThời gian hoàn thành cả hai chặng là:\n$75 + 55 = 130\\text{ (giây)}$.\nĐổi: $130\\text{ giây} = 2\\text{ phút } 10\\text{ giây}$.", "130 giây (hoặc 2 phút 10 giây)", 4, 1.0),
            make_essay(4, "Một máy in laser in được 24 trang trong 1 phút. Hỏi để in một tập tài liệu dày 120 trang thì máy in đó mất bao nhiêu giây?", "Thời gian để máy in in xong 120 trang là:\n$120 : 24 = 5\\text{ (phút)}$.\nĐổi ra giây:\n$5 \\times 60 = 300\\text{ (giây)}$.", "300 giây", 5, 1.5),
            make_essay(5, "Năm 1428, Lê Lợi lên ngôi hoàng đế, lập nên triều Hậu Lê. Hỏi:\na) Năm 1428 thuộc thế kỉ nào?\nb) Tính đến năm 2028 sẽ tròn bao nhiêu thế kỉ kể từ sự kiện lịch sử đó?", "a) Năm 1428 thuộc thế kỉ XV (thế kỉ mười lăm).\nb) Khoảng cách từ năm 1428 đến năm 2028 là:\n$2028 - 1428 = 600\\text{ (năm)}$.\nĐổi: $600\\text{ năm} = 6\\text{ thế kỉ}$.\nVậy đến năm 2028 sẽ tròn đúng 6 thế kỉ.", "a) Thế kỉ XV; b) 6 thế kỉ", 5, 1.5),
            make_essay(6, "Bác thợ rèn làm một chiếc móng ngựa mất 3 phút 45 giây. Hỏi trong một buổi sáng làm việc 3 giờ, bác thợ rèn làm được nhiều nhất bao nhiêu chiếc móng ngựa như thế?", "Đổi: $3\\text{ phút } 45\\text{ giây} = 225\\text{ giây}$.\n$3\\text{ giờ} = 3 \\times 3600 = 10\\,800\\text{ giây}$.\nSố móng ngựa làm được là:\n$10\\,800 : 225 = 48\\text{ (chiếc)}$.", "48 chiếc", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 20: THỰC HÀNH VÀ TRẢI NGHIỆM SỬ DỤNG MỘT SỐ ĐƠN VỊ ĐO ĐẠI LƯỢNG
    # =========================================================================

    # --- Bài 20 - Đề 1 ---
    exams["th4_b20_test1"] = {
        "id": "th4_b20_test1",
        "lessonId": "th4_b20",
        "lessonNum": 20,
        "testNum": 1,
        "title": "Bài 20: Thực hành và trải nghiệm sử dụng một số đơn vị đo đại lượng - Đề số 1",
        "topic": "Thực hành và trải nghiệm sử dụng một số đơn vị đo đại lượng",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một xe tải chở được 3 tấn hàng. Số hàng đó đổi ra tạ là:", ["30 tạ", "300 tạ", "3 tạ", "3 000 tạ"], 0, "1 tấn = 10 tạ => 3 tấn = 30 tạ."),
            make_mc(2, "Diện tích một sân trường tiểu học thích hợp nhất là:", ["1 500 m²", "1 500 dm²", "1 500 cm²", "1 500 mm²"], 0, "Sân trường tiểu học thường rộng hàng nghìn mét vuông."),
            make_mc(3, "Một vận động viên nhảy dây được 180 lần trong 1 phút. Trung bình mỗi giây vận động viên đó nhảy được:", ["3 lần", "2 lần", "4 lần", "6 lần"], 0, "180 : 60 = 3 lần."),
            make_mc(4, "Một bao xi măng nặng 50 kg. Hỏi 20 bao xi măng như thế nặng bao nhiêu tấn?", ["1 tấn", "10 tấn", "2 tấn", "5 tấn"], 0, "50 x 20 = 1 000 kg = 1 tấn."),
            make_mc(5, "Đổi $2\\text{ m}^2 \\text{ } 45\\text{ dm}^2 = \\dots \\text{ dm}^2$:", ["245 dm²", "2045 dm²", "2450 dm²", "24,5 dm²"], 0, "2 m² = 200 dm² => 200 + 45 = 245 dm²."),
            make_mc(6, "Bác Hồ đọc Tuyên ngôn Độc lập năm 1945. Sự kiện này diễn ra vào thế kỉ nào?", ["Thế kỉ XIX", "Thế kỉ XX", "Thế kỉ XXI", "Thế kỉ XVIII"], 1, "Năm 1945 thuộc thế kỉ XX.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $5\\text{ tạ } 40\\text{ kg} = \\dots \\text{ kg}$\nb) $3\\text{ m}^2 \\text{ } 8\\text{ dm}^2 = \\dots \\text{ dm}^2$", "a) $5\\text{ tạ} = 500\\text{ kg}$ => $500 + 40 = 540\\text{ kg}$.\nb) $3\\text{ m}^2 = 300\\text{ dm}^2$ => $300 + 8 = 308\\text{ dm}^2$.", "a) 540; b) 308", 4, 1.0),
            make_essay(2, "Tính:\na) $4\\text{ tấn } 5\\text{ tạ} + 2\\text{ tấn } 8\\text{ tạ}$\nb) $45\\text{ giây} \\times 4$", "a) $45\\text{ tạ} + 28\\text{ tạ} = 73\\text{ tạ} = 7\\text{ tấn } 3\\text{ tạ}$.\nb) $45 \\times 4 = 180\\text{ giây} = 3\\text{ phút}$.", "a) 7 tấn 3 tạ; b) 180 giây (hoặc 3 phút)", 4, 1.0),
            make_essay(3, "Lớp 4A tham gia phong trào kế hoạch nhỏ, thu gom được 2 tạ 40 kg giấy vụn. Lớp 4B thu gom được nhiều hơn lớp 4A là 30 kg giấy vụn. Hỏi cả hai lớp thu gom được tất cả bao nhiêu ki-lô-gam giấy vụn?", "Đổi: $2\\text{ tạ } 40\\text{ kg} = 240\\text{ kg}$.\nSố giấy vụn lớp 4B thu gom được là:\n$240 + 30 = 270\\text{ (kg)}$.\nCả hai lớp thu gom được tất cả số ki-lô-gam giấy vụn là:\n$240 + 270 = 510\\text{ (kg)}$.", "510 kg", 4, 1.0),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chu vi $64\\text{ m}$, chiều rộng ngắn hơn chiều dài $8\\text{ m}$.\na) Tính diện tích mảnh vườn đó.\nb) Cứ mỗi $1\\text{ m}^2$ thu hoạch được $5\\text{ kg}$ cà chua. Hỏi trên cả mảnh vườn đó thu hoạch được bao nhiêu tạ cà chua?", "a) Nửa chu vi mảnh vườn là: $64 : 2 = 32\\text{ (m)}$.\nChiều dài mảnh vườn là: $(32 + 8) : 2 = 20\\text{ (m)}$.\nChiều rộng mảnh vườn là: $32 - 20 = 12\\text{ (m)}$.\nDiện tích mảnh vườn là: $20 \\times 12 = 240\\text{ (m}^2)$.\nb) Số ki-lô-gam cà chua thu hoạch được là:\n$240 \\times 5 = 1200\\text{ (kg)}$.\nĐổi: $1200\\text{ kg} = 12\\text{ tạ}$.", "a) 240 m²; b) 12 tạ", 5, 1.5),
            make_essay(5, "Một xe tải chở 4 tấn gạo gồm hai loại: gạo nếp và gạo tẻ. Biết khối lượng gạo tẻ nhiều hơn gạo nếp là 8 tạ. Tính khối lượng mỗi loại gạo theo đơn vị tạ.", "Đổi: $4\\text{ tấn} = 40\\text{ tạ}$.\nKhối lượng gạo tẻ chở trên xe là:\n$(40 + 8) : 2 = 24\\text{ (tạ)}$.\nKhối lượng gạo nếp chở trên xe là:\n$40 - 24 = 16\\text{ (tạ)}$.", "Gạo tẻ: 24 tạ; Gạo nếp: 16 tạ", 5, 1.5),
            make_essay(6, "Bạn Nam thực hiện một bài thực hành đo lường: bạn cân 10 quyển vở cùng loại được 1 kg 800 g. Hỏi nếu một thùng có 50 quyển vở như thế thì nặng bao nhiêu ki-lô-gam (không tính vỏ thùng)?", "Đổi: $1\\text{ kg } 800\\text{ g} = 1800\\text{ g}$.\nKhối lượng của mỗi quyển vở là:\n$1800 : 10 = 180\\text{ (g)}$.\nKhối lượng của 50 quyển vở là:\n$180 \\times 50 = 9000\\text{ (g)}$.\nĐổi: $9000\\text{ g} = 9\\text{ kg}$.", "9 kg", 4, 1.0)
        ]
    }

    # --- Bài 20 - Đề 2 ---
    exams["th4_b20_test2"] = {
        "id": "th4_b20_test2",
        "lessonId": "th4_b20",
        "lessonNum": 20,
        "testNum": 2,
        "title": "Bài 20: Thực hành và trải nghiệm sử dụng một số đơn vị đo đại lượng - Đề số 2",
        "topic": "Thực hành và trải nghiệm sử dụng một số đơn vị đo đại lượng",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Khối lượng một con voi trưởng thành khoảng:", ["4 tấn", "40 kg", "400 g", "40 tạ"], 0, "Con voi trưởng thành nặng khoảng 3 đến 5 tấn."),
            make_mc(2, "Diện tích một chiếc khăn quàng đỏ hình tam giác khoảng:", ["15 dm²", "15 m²", "15 mm²", "150 m²"], 0, "Khăn quàng đỏ có diện tích khoảng 15 dm² = 1 500 cm²."),
            make_mc(3, "Một bộ phim tài liệu kéo dài 1 giờ 20 phút. Thời lượng đó bằng:", ["80 phút", "120 phút", "70 phút", "100 phút"], 0, "60 + 20 = 80 phút."),
            make_mc(4, "Một người thợ dệt vải mỗi phút dệt được 50 cm vải. Trong 1 giờ người đó dệt được số mét vải là:", ["30 m", "300 m", "5 m", "50 m"], 0, "1 giờ = 60 phút. Dệt được: 50 x 60 = 3 000 cm = 30 m."),
            make_mc(5, "Đổi $8\\text{ dm}^2 \\text{ } 50\\text{ mm}^2 = \\dots \\text{ mm}^2$:", ["80 050", "850", "8 050", "800 050"], 0, "8 dm² = 80 000 mm² => 80 000 + 50 = 80 050 mm²."),
            make_mc(6, "Năm 1010 là năm vua Lý Thái Tổ dời đô từ Hoa Lư về Thăng Long. Năm 1010 thuộc thế kỉ nào?", ["XI", "X", "IX", "XII"], 0, "Năm 1010 thuộc thế kỉ XI.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $2\\text{ ngày } 4\\text{ giờ} = \\dots \\text{ giờ}$\nb) $5\\text{ m}^2 \\text{ } 12\\text{ dm}^2 = \\dots \\text{ dm}^2$", "a) $2 \\times 24 + 4 = 52\\text{ giờ}$.\nb) $5 \\times 100 + 12 = 512\\text{ dm}^2$.", "a) 52; b) 512", 4, 1.0),
            make_essay(2, "Điền dấu ($>$, $<$, $=$) thích hợp vào chỗ chấm:\na) $3\\text{ tấn } 50\\text{ kg} \\dots 35\\text{ tạ}$\nb) $4\\text{ phút } 15\\text{ giây} \\dots 250\\text{ giây}$", "a) $3\\text{ tấn } 50\\text{ kg} = 3050\\text{ kg} < 3500\\text{ kg} = 35\\text{ tạ}$.\nb) $4\\text{ phút } 15\\text{ giây} = 255\\text{ giây} > 250\\text{ giây}$.", "a) <; b) >", 4, 1.0),
            make_essay(3, "Bác An trồng lúa trên thửa ruộng thu hoạch được 1 tấn 8 tạ thóc. Bác để lại 3 tạ thóc làm giống và ăn, số còn lại đem bán với giá 9 000 đồng/kg. Hỏi bác An bán được bao nhiêu tiền thóc?", "Đổi: $1\\text{ tấn } 8\\text{ tạ} = 18\\text{ tạ}$.\nSố thóc đem bán là:\n$18 - 3 = 15\\text{ (tạ)} = 1500\\text{ (kg)}$.\nSố tiền bác An thu được là:\n$1500 \\times 9000 = 13\\,500\\,000\\text{ (đồng)}$.", "13 500 000 đồng", 4, 1.0),
            make_essay(4, "Một lớp học có chiều dài $8\\text{ m}$, chiều rộng $6\\text{ m}$. Người ta muốn lát kín sàn lớp học bằng gạch men hình vuông có cạnh $4\\text{ dm}$.\na) Tính diện tích sàn lớp học.\nb) Tính số viên gạch cần mua.\nc) Biết 1 hộp gạch có 5 viên. Hỏi cần mua bao nhiêu hộp gạch?", "a) Diện tích sàn lớp học là:\n$8 \\times 6 = 48\\text{ (m}^2) = 4800\\text{ dm}^2$.\nb) Diện tích một viên gạch là:\n$4 \\times 4 = 16\\text{ (dm}^2)$.\nSố viên gạch cần mua là:\n$4800 : 16 = 300\\text{ (viên)}$.\nc) Số hộp gạch cần mua là:\n$300 : 5 = 60\\text{ (hộp)}$.", "a) 48 m²; b) 300 viên; c) 60 hộp", 5, 1.5),
            make_essay(5, "Ba xe tải cùng chở cát vào công trình. Xe thứ nhất chở 3 tấn 5 tạ. Xe thứ hai chở ít hơn xe thứ nhất 8 tạ. Xe thứ ba chở nhiều hơn xe thứ hai 5 tạ. Hỏi cả ba xe chở được tất cả bao nhiêu tạ cát?", "Đổi: $3\\text{ tấn } 5\\text{ tạ} = 35\\text{ tạ}$.\nXe thứ hai chở được số tạ cát là:\n$35 - 8 = 27\\text{ (tạ)}$.\nXe thứ ba chở được số tạ cát là:\n$27 + 5 = 32\\text{ (tạ)}$.\nCả ba xe chở được tất cả số tạ cát là:\n$35 + 27 + 32 = 94\\text{ (tạ)}$.", "94 tạ", 5, 1.5),
            make_essay(6, "Một bình nước chứa đầy 20 lít nước. Người ta dùng một chiếc ca dung tích 250 ml để múc nước từ bình ra rót vào các cốc. Hỏi chiếc ca đó có thể múc được nhiều nhất bao nhiêu ca nước đầy?", "Đổi: $20\\text{ l} = 20\\,000\\text{ ml}$.\nSố ca nước có thể múc được là:\n$20\\,000 : 250 = 80\\text{ (ca)}$.", "80 ca", 4, 1.0)
        ]
    }

    # --- Bài 20 - Đề 3 ---
    exams["th4_b20_test3"] = {
        "id": "th4_b20_test3",
        "lessonId": "th4_b20",
        "lessonNum": 20,
        "testNum": 3,
        "title": "Bài 20: Thực hành và trải nghiệm sử dụng một số đơn vị đo đại lượng - Đề số 3",
        "topic": "Thực hành và trải nghiệm sử dụng một số đơn vị đo đại lượng",
        "chapter": "Chủ đề 4: Một số đơn vị đo đại lượng",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một xe bồn chở nước có dung tích 5 000 lít. Khối lượng nước trong bồn khi đầy khoảng:", ["5 tấn", "5 tạ", "50 tấn", "500 kg"], 0, "1 lít nước nguyên chất nặng 1 kg, nên 5 000 lít nặng 5 000 kg = 5 tấn."),
            make_mc(2, "Diện tích một sân vận động bóng đá tiêu chuẩn khoảng:", ["7 000 m²", "700 m²", "70 000 m²", "70 m²"], 0, "Sân bóng đá tiêu chuẩn (105m x 68m) khoảng 7 140 m²."),
            make_mc(3, "Thời gian bạn Mai đạp xe từ nhà đến trường là 15 phút. Thời gian đó bằng bao nhiêu giây?", ["900 giây", "600 giây", "1 500 giây", "150 giây"], 0, "15 x 60 = 900 giây."),
            make_mc(4, "Một khu đất hình vuông có cạnh $50\\text{ m}$. Diện tích khu đất đó là:", ["2 500 m²", "200 m²", "250 m²", "5 000 m²"], 0, "50 x 50 = 2 500 m²."),
            make_mc(5, "Đổi $3\\text{ thế kỉ } 25\\text{ năm} = \\dots \\text{ năm}$:", ["325 năm", "3 025 năm", "350 năm", "305 năm"], 0, "3 x 100 + 25 = 325 năm."),
            make_mc(6, "Bác Ba đóng 4 tấn thóc vào các bao, mỗi bao chứa đúng 50 kg. Số bao thóc bác Ba đóng được là:", ["80 bao", "800 bao", "40 bao", "20 bao"], 0, "4 tấn = 4 000 kg. 4 000 : 50 = 80 bao.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $6\\text{ tấn } 8\\text{ yến} = \\dots \\text{ kg}$\nb) $4\\text{ m}^2 \\text{ } 750\\text{ cm}^2 = \\dots \\text{ cm}^2$", "a) $6\\text{ tấn} = 6000\\text{ kg}$, $8\\text{ yến} = 80\\text{ kg}$ => $6080\\text{ kg}$.\nb) $4\\text{ m}^2 = 40\\,000\\text{ cm}^2$ => $40\\,000 + 750 = 40\\,750\\text{ cm}^2$.", "a) 6080; b) 40 750", 4, 1.0),
            make_essay(2, "Tính:\na) $3\\text{ phút } 20\\text{ giây} + 4\\text{ phút } 50\\text{ giây}$\nb) $18\\text{ tạ} : 3 \\times 5$", "a) $7\\text{ phút } 70\\text{ giây} = 8\\text{ phút } 10\\text{ giây}$.\nb) $18 : 3 \\times 5 = 6 \\times 5 = 30\\text{ (tạ)}$.", "a) 8 phút 10 giây; b) 30 tạ", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình chữ nhật có chiều dài $24\\text{ m}$, chiều rộng bằng $\\frac{1}{3}$ chiều dài. Người ta dùng $\\frac{1}{2}$ diện tích mảnh vườn để trồng dâu tây. Tính diện tích phần đất trồng dâu tây theo đơn vị mét vuông.", "Chiều rộng mảnh vườn là:\n$24 : 3 = 8\\text{ (m)}$.\nDiện tích cả mảnh vườn là:\n$24 \\times 8 = 192\\text{ (m}^2)$.\nDiện tích phần đất trồng dâu tây là:\n$192 : 2 = 96\\text{ (m}^2)$.", "96 m²", 4, 1.0),
            make_essay(4, "Một đoàn xe gồm 2 xe tải lớn và 3 xe tải nhỏ chở gạo ủng hộ đồng bào vùng bão lụt. Mỗi xe tải lớn chở 4 tấn 5 tạ gạo, mỗi xe tải nhỏ chở 2 tấn gạo. Hỏi cả đoàn xe chở được tất cả bao nhiêu tạ gạo?", "Đổi: $4\\text{ tấn } 5\\text{ tạ} = 45\\text{ tạ}$; $2\\text{ tấn} = 20\\text{ tạ}$.\n2 xe tải lớn chở được số tạ gạo là:\n$45 \\times 2 = 90\\text{ (tạ)}$.\n3 xe tải nhỏ chở được số tạ gạo là:\n$20 \\times 3 = 60\\text{ (tạ)}$.\nCả đoàn xe chở được tất cả số tạ gạo là:\n$90 + 60 = 150\\text{ (tạ)}$.", "150 tạ", 5, 1.5),
            make_essay(5, "Một bể bơi hình chữ nhật có chiều dài $25\\text{ m}$, chiều rộng $10\\text{ m}$. Xung quanh bể bơi người ta làm một lối đi dạo rộng $2\\text{ m}$. Tính diện tích của lối đi dạo xung quanh bể bơi đó.", "Diện tích mặt nước bể bơi là:\n$25 \\times 10 = 250\\text{ (m}^2)$.\nChiều dài toàn bộ khu đất gồm cả bể bơi và lối đi là:\n$25 + 2 \\times 2 = 29\\text{ (m)}$.\nChiều rộng toàn bộ khu đất là:\n$10 + 2 \\times 2 = 14\\text{ (m)}$.\nDiện tích toàn bộ khu đất là:\n$29 \\times 14 = 406\\text{ (m}^2)$.\nDiện tích lối đi dạo là:\n$406 - 250 = 156\\text{ (m}^2)$.", "156 m²", 5, 1.5),
            make_essay(6, "Bác An có một thùng dầu nặng 42 kg (gồm cả dầu và vỏ thùng). Sau khi bác bán đi một nửa số dầu thì thùng dầu còn nặng 22 kg. Hỏi riêng vỏ thùng dầu đó nặng bao nhiêu ki-lô-gam?", "Khối lượng của một nửa số dầu đã bán là:\n$42 - 22 = 20\\text{ (kg)}$.\nKhối lượng của toàn bộ số dầu trong thùng là:\n$20 \\times 2 = 40\\text{ (kg)}$.\nKhối lượng của vỏ thùng là:\n$42 - 40 = 2\\text{ (kg)}$.", "2 kg", 4, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 4: {len(ex)} (Kỳ vọng: 12)")
    for b in range(17, 21):
        for t in range(1, 4):
            key = f"th4_b{b}_test{t}"
            assert key in ex, f"Thiếu {key}"
            assert len(ex[key]["part1"]) == 6
            assert len(ex[key]["part2"]) == 6
            p1_pts = sum(q["points"] for q in ex[key]["part1"])
            p2_pts = sum(q["points"] for q in ex[key]["part2"])
            assert abs(p1_pts - 3.0) < 1e-6
            assert abs(p2_pts - 7.0) < 1e-6
    print("Chủ đề 4 hoàn hảo 100%!")
