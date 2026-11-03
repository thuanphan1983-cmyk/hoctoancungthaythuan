# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 13: ÔN TẬP CUỐI NĂM (PHẦN 1: BÀI 59 ĐẾN BÀI 61)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 3 bài học x 3 đề độc lập = 9 đề thi (th4_b59_test1 -> th4_b61_test3)
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

def get_ch13_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 59: ÔN TẬP SỐ TỰ NHIÊN VÀ PHÂN SỐ
    # =========================================================================

    # --- Bài 59 - Đề 1 ---
    exams["th4_b59_test1"] = {
        "id": "th4_b59_test1",
        "lessonId": "th4_b59",
        "lessonNum": 59,
        "testNum": 1,
        "title": "Bài 59: Ôn tập số tự nhiên và phân số - Đề số 1",
        "topic": "Ôn tập số tự nhiên và phân số",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 3 triệu, 5 trăm nghìn, 7 chục và 4 đơn vị viết là:", ["3 500 074", "3 050 074", "3 500 740", "350 074"], 0, "3 500 074."),
            make_mc(2, "Phân số nào dưới đây bằng phân số $\\frac{3}{5}$?", ["$\\frac{9}{15}$", "$\\frac{6}{15}$", "$\\frac{12}{25}$", "$\\frac{5}{3}$"], 0, "3/5 = (3x3)/(5x3) = 9/15."),
            make_mc(3, "Rút gọn phân số $\\frac{24}{36}$ về phân số tối giản ta được:", ["$\\frac{2}{3}$", "$\\frac{4}{6}$", "$\\frac{3}{4}$", "$\\frac{12}{18}$"], 0, "24/36 = (24:12)/(36:12) = 2/3."),
            make_mc(4, "Trong các phân số $\\frac{4}{5}, \\frac{7}{6}, \\frac{8}{8}, \\frac{2}{3}$, phân số lớn hơn 1 là:", ["$\\frac{7}{6}$", "$\\frac{4}{5}$", "$\\frac{8}{8}$", "$\\frac{2}{3}$"], 0, "Phân số có tử số lớn hơn mẫu số thì lớn hơn 1: 7/6 > 1."),
            make_mc(5, "Làm tròn số 824 675 đến hàng chục nghìn ta được:", ["820 000", "830 000", "825 000", "800 000"], 0, "Chữ số hàng nghìn là 4 < 5 nên làm tròn xuống 820 000."),
            make_mc(6, "Phân số chỉ phần đã tô màu gồm 3 ô vuông trong tổng số 8 ô vuông bằng nhau là:", ["$\\frac{3}{8}$", "$\\frac{5}{8}$", "$\\frac{8}{3}$", "$\\frac{3}{5}$"], 0, "Tô màu 3 trong 8 ô là 3/8.")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau thành phân số tối giản:\na) $\\frac{18}{27}$\nb) $\\frac{30}{45}$", "a) $\\frac{18}{27} = \\frac{18 : 9}{27 : 9} = \\frac{2}{3}$.\nb) $\\frac{30}{45} = \\frac{30 : 15}{45 : 15} = \\frac{2}{3}$.", "a) 2/3; b) 2/3", 4, 1.0),
            make_essay(2, "Quy đồng mẫu số các phân số sau:\na) $\\frac{2}{3}$ và $\\frac{5}{6}$\nb) $\\frac{3}{4}$ và $\\frac{2}{5}$", "a) MSC = 6: $\\frac{2}{3} = \\frac{4}{6}$, giữ nguyên $\\frac{5}{6}$.\nb) MSC = 20: $\\frac{3}{4} = \\frac{15}{20}$; $\\frac{2}{5} = \\frac{8}{20}$.", "a) 4/6 và 5/6; b) 15/20 và 8/20", 4, 1.0),
            make_essay(3, "Sắp xếp các phân số sau theo thứ tự từ bé đến lớn:\n$\\frac{1}{2}; \\frac{2}{3}; \\frac{3}{4}; \\frac{1}{4}$", "Quy đồng mẫu số chung là 12:\n$\\frac{1}{4} = \\frac{3}{12}; \\frac{1}{2} = \\frac{6}{12}; \\frac{2}{3} = \\frac{8}{12}; \\frac{3}{4} = \\frac{9}{12}$.\nVì $\\frac{3}{12} < \\frac{6}{12} < \\frac{8}{12} < \\frac{9}{12}$ nên thứ tự là: $\\frac{1}{4}; \\frac{1}{2}; \\frac{2}{3}; \\frac{3}{4}$.", "1/4; 1/2; 2/3; 3/4", 4, 1.0),
            make_essay(4, "Một lớp học có 32 học sinh, trong đó có 18 học sinh nữ.\na) Viết phân số chỉ số phần học sinh nữ trong tổng số học sinh cả lớp.\nb) Viết phân số chỉ số phần học sinh nam trong tổng số học sinh cả lớp (rút gọn thành phân số tối giản).", "a) Phân số chỉ số học sinh nữ là: $\\frac{18}{32} = \\frac{9}{16}$.\nb) Số học sinh nam là: $32 - 18 = 14\\text{ (học sinh)}$.\nPhân số chỉ số học sinh nam là: $\\frac{14}{32} = \\frac{7}{16}$.", "a) 9/16; b) 7/16", 5, 1.5),
            make_essay(5, "Tìm số tự nhiên $x$ biết:\na) $\\frac{x}{7} = \\frac{12}{28}$\nb) $\\frac{5}{x} = \\frac{25}{40}$", "a) Ta có: $\\frac{12}{28} = \\frac{12 : 4}{28 : 4} = \\frac{3}{7}$. Do đó $x = 3$.\nb) Ta có: $\\frac{25}{40} = \\frac{25 : 5}{40 : 5} = \\frac{5}{8}$. Do đó $x = 8$.", "a) x = 3; b) x = 8", 5, 1.5),
            make_essay(6, "Tìm một phân số có mẫu số bằng 15, biết rằng phân số đó lớn hơn $\\frac{1}{3}$ và nhỏ hơn $\\frac{3}{5}$.", "Quy đồng mẫu số các phân số về mẫu số chung là 15:\n$\\frac{1}{3} = \\frac{5}{15}$; $\\frac{3}{5} = \\frac{9}{15}$.\nPhân số cần tìm có dạng $\\frac{a}{15}$ với $5 < a < 9$.\nCác giá trị của a có thể là 6; 7; 8.\nVậy các phân số thỏa mãn là: $\\frac{6}{15}, \\frac{7}{15}, \\frac{8}{15}$ (ví dụ chọn $\\frac{7}{15}$).", "7/15 (hoặc 6/15, 8/15)", 4, 1.0)
        ]
    }

    # --- Bài 59 - Đề 2 ---
    exams["th4_b59_test2"] = {
        "id": "th4_b59_test2",
        "lessonId": "th4_b59",
        "lessonNum": 59,
        "testNum": 2,
        "title": "Bài 59: Ôn tập số tự nhiên và phân số - Đề số 2",
        "topic": "Ôn tập số tự nhiên và phân số",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Giá trị của chữ số 8 trong số 18 425 600 là:", ["8 000 000", "800 000", "80 000 000", "80 000"], 0, "Chữ số 8 ở hàng triệu có giá trị 8 000 000."),
            make_mc(2, "Phân số nào sau đây tối giản?", ["$\\frac{7}{9}$", "$\\frac{6}{8}$", "$\\frac{9}{12}$", "$\\frac{10}{25}$"], 0, "7/9 có tử số và mẫu số nguyên tố cùng nhau."),
            make_mc(3, "Phân số bé nhất trong các phân số $\\frac{2}{3}, \\frac{3}{4}, \\frac{1}{6}, \\frac{5}{12}$ là:", ["$\\frac{1}{6}$", "$\\frac{2}{3}$", "$\\frac{3}{4}$", "$\\frac{5}{12}$"], 0, "1/6 = 2/12 nhỏ nhất."),
            make_mc(4, "Một rổ có 35 quả cam, mẹ đã biếu bà 15 quả cam. Phân số chỉ số cam biếu bà là:", ["$\\frac{3}{7}$", "$\\frac{4}{7}$", "$\\frac{15}{20}$", "$\\frac{1}{2}$"], 0, "15/35 = 3/7."),
            make_mc(5, "Số lớn nhất có 7 chữ số là:", ["9 999 999", "1 000 000", "9 876 543", "10 000 000"], 0, "9 999 999."),
            make_mc(6, "Hai phân số $\\frac{a}{b}$ và $\\frac{c}{d}$ bằng nhau khi:", ["a x d = b x c", "a x c = b x d", "a + d = b + c", "a - d = b - c"], 0, "Tính chất cơ bản: a/b = c/d khi a x d = b x c.")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau:\na) $\\frac{20}{35}$\nb) $\\frac{42}{56}$", "a) $\\frac{20}{35} = \\frac{20 : 5}{35 : 5} = \\frac{4}{7}$.\nb) $\\frac{42}{56} = \\frac{42 : 14}{56 : 14} = \\frac{3}{4}$.", "a) 4/7; b) 3/4", 4, 1.0),
            make_essay(2, "So sánh các phân số sau:\na) $\\frac{4}{7}$ và $\\frac{5}{7}$\nb) $\\frac{3}{5}$ và $\\frac{4}{7}$", "a) Vì $4 < 5$ nên $\\frac{4}{7} < \\frac{5}{7}$.\nb) Quy đồng: $\\frac{3}{5} = \\frac{21}{35}; \\frac{4}{7} = \\frac{20}{35}$. Vì $\\frac{21}{35} > \\frac{20}{35}$ nên $\\frac{3}{5} > \\frac{4}{7}$.", "a) 4/7 < 5/7; b) 3/5 > 4/7", 4, 1.0),
            make_essay(3, "Viết các phân số sau theo thứ tự từ lớn đến bé:\n$\\frac{5}{6}; \\frac{2}{3}; \\frac{7}{12}; \\frac{3}{4}$", "Quy đồng mẫu số chung là 12:\n$\\frac{5}{6} = \\frac{10}{12}; \\frac{2}{3} = \\frac{8}{12}; \\frac{7}{12}; \\frac{3}{4} = \\frac{9}{12}$.\nVì $\\frac{10}{12} > \\frac{9}{12} > \\frac{8}{12} > \\frac{7}{12}$ nên thứ tự từ lớn đến bé là:\n$\\frac{5}{6}; \\frac{3}{4}; \\frac{2}{3}; \\frac{7}{12}$.", "5/6; 3/4; 2/3; 7/12", 4, 1.0),
            make_essay(4, "Một trang trại nuôi 120 con gà và vịt, trong đó có 45 con vịt.\na) Tìm tỉ số của số con vịt và tổng số con gà, vịt.\nb) Tìm tỉ số của số con gà và số con vịt (viết dưới dạng phân số tối giản).", "a) Tỉ số của số con vịt và tổng đàn là: $\\frac{45}{120} = \\frac{3}{8}$.\nb) Số con gà là: $120 - 45 = 75\\text{ (con)}$.\nTỉ số của số con gà và số con vịt là: $\\frac{75}{45} = \\frac{5}{3}$.", "a) 3/8; b) 5/3", 5, 1.5),
            make_essay(5, "Tìm số tự nhiên $y$ biết:\na) $\\frac{18}{y} = \\frac{2}{3}$\nb) $\\frac{y}{24} = \\frac{5}{8}$", "a) $\\frac{2}{3} = \\frac{2 \\times 9}{3 \\times 9} = \\frac{18}{27} \\Rightarrow y = 27$.\nb) $\\frac{5}{8} = \\frac{5 \\times 3}{8 \\times 3} = \\frac{15}{24} \\Rightarrow y = 15$.", "a) y = 27; b) y = 15", 5, 1.5),
            make_essay(6, "Viết tất cả các phân số nhỏ hơn 1 có tích của tử số và mẫu số bằng 24.", "Phân tích $24 = 1 \\times 24 = 2 \\times 12 = 3 \\times 8 = 4 \\times 6$.\nVì phân số nhỏ hơn 1 nên tử số phải nhỏ hơn mẫu số.\nCác phân số thỏa mãn là: $\\frac{1}{24}; \\frac{2}{12}; \\frac{3}{8}; \\frac{4}{6}$.", "1/24; 2/12; 3/8; 4/6", 4, 1.0)
        ]
    }

    # --- Bài 59 - Đề 3 ---
    exams["th4_b59_test3"] = {
        "id": "th4_b59_test3",
        "lessonId": "th4_b59",
        "lessonNum": 59,
        "testNum": 3,
        "title": "Bài 59: Ôn tập số tự nhiên và phân số - Đề số 3",
        "topic": "Ôn tập số tự nhiên và phân số",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số chẵn bé nhất có 6 chữ số khác nhau là:", ["102 346", "102 345", "100 000", "123 456"], 0, "102 346 có 6 chữ số khác nhau và tận cùng bằng 6 (số chẵn)."),
            make_mc(2, "Phân số bằng 1 khi:", ["Tử số bằng mẫu số (khác 0)", "Tử số lớn hơn mẫu số", "Tử số bé hơn mẫu số", "Tử số bằng 0"], 0, "a/a = 1 với a khác 0."),
            make_mc(3, "Quy đồng mẫu số hai phân số $\\frac{3}{8}$ và $\\frac{5}{12}$ ta được mẫu số chung nhỏ nhất là:", ["24", "48", "96", "12"], 0, "24 chia hết cho cả 8 và 12."),
            make_mc(4, "Trong các phân số $\\frac{5}{9}, \\frac{7}{9}, \\frac{4}{9}, \\frac{8}{9}$, phân số lớn nhất là:", ["$\\frac{8}{9}$", "$\\frac{7}{9}$", "$\\frac{5}{9}$", "$\\frac{4}{9}$"], 0, "Cùng mẫu số, phân số có tử lớn nhất là lớn nhất."),
            make_mc(5, "Số liền trước của 10 000 000 là:", ["9 999 999", "10 000 001", "9 999 990", "9 000 000"], 0, "10 000 000 - 1 = 9 999 999."),
            make_mc(6, "Có bao nhiêu phân số có tổng của tử số và mẫu số bằng 5 (tử số và mẫu số là số tự nhiên, mẫu số khác 0)?", ["4 phân số", "5 phân số", "3 phân số", "6 phân số"], 0, "Các phân số: 0/5, 1/4, 2/3, 3/2, 4/1 => 5 phân số (hoặc nếu tử > 0 là 4 phân số: 1/4, 2/3, 3/2, 4/1).")
        ],
        "part2": [
            make_essay(1, "Rút gọn các phân số sau thành phân số tối giản:\na) $\\frac{36}{48}$\nb) $\\frac{25}{100}$", "a) $\\frac{36}{48} = \\frac{36 : 12}{48 : 12} = \\frac{3}{4}$.\nb) $\\frac{25}{100} = \\frac{25 : 25}{100 : 25} = \\frac{1}{4}$.", "a) 3/4; b) 1/4", 4, 1.0),
            make_essay(2, "Điền dấu thích hợp ($>$, $<$, $=$) vào chỗ chấm:\na) $\\frac{5}{8} \\dots \\frac{5}{9}$\nb) $\\frac{8}{11} \\dots \\frac{16}{22}$", "a) Hai phân số cùng tử số, phân số nào có mẫu số bé hơn thì lớn hơn: $\\frac{5}{8} > \\frac{5}{9}$.\nb) $\\frac{16}{22} = \\frac{16 : 2}{22 : 2} = \\frac{8}{11}$ nên $\\frac{8}{11} = \\frac{16}{22}$.", "a) >; b) =", 4, 1.0),
            make_essay(3, "Một mảnh đất có diện tích $360\\text{ m}^2$. Người ta dùng $\\frac{1}{3}$ diện tích để làm nhà, $\\frac{2}{5}$ diện tích để trồng cây ăn quả, phần còn lại làm sân và lối đi. Tính diện tích phần đất làm sân và lối đi.", "Diện tích làm nhà là: $360 \\times \\frac{1}{3} = 120\\text{ (m}^2)$.\nDiện tích trồng cây ăn quả là: $360 \\times \\frac{2}{5} = 144\\text{ (m}^2)$.\nDiện tích làm sân và lối đi là:\n$360 - (120 + 144) = 96\\text{ (m}^2)$.", "96 m²", 4, 1.0),
            make_essay(4, "Một giá sách có 80 quyển sách gồm sách Toán và sách Tiếng Việt. Biết số sách Toán bằng $\\frac{3}{5}$ tổng số sách.\na) Tính số sách Toán.\nb) Tính số sách Tiếng Việt.", "a) Số sách Toán trên giá sách là:\n$80 \\times 3 : 5 = 48\\text{ (quyển)}$.\nb) Số sách Tiếng Việt trên giá sách là:\n$80 - 48 = 32\\text{ (quyển)}$.", "a) 48 quyển; b) 32 quyển", 5, 1.5),
            make_essay(5, "Tìm số tự nhiên $x$ biết: $\\frac{2}{5} < \\frac{x}{15} < \\frac{4}{5}$.", "Quy đồng mẫu số chung là 15:\n$\\frac{2}{5} = \\frac{6}{15}$; $\\frac{4}{5} = \\frac{12}{15}$.\nTa có: $\\frac{6}{15} < \\frac{x}{15} < \\frac{12}{15} \\Rightarrow 6 < x < 12$.\nVì x là số tự nhiên nên $x \\in \\{7; 8; 9; 10; 11\\}$.", "x ∈ {7; 8; 9; 10; 11}", 5, 1.5),
            make_essay(6, "Cho phân số $\\frac{13}{17}$. Cần thêm vào cả tử số và mẫu số cùng một số tự nhiên $a$ nào để được phân số mới bằng $\\frac{4}{5}$?", "Khi thêm cùng một số $a$ vào cả tử số và mẫu số thì hiệu giữa mẫu số và tử số không đổi:\nHiệu là: $17 - 13 = 4$.\nỞ phân số mới $\\frac{4}{5}$, hiệu giữa mẫu số và tử số là $5 - 4 = 1\\text{ (phần)}$.\nTử số mới là: $4 \\times 4 = 16$.\nSố tự nhiên $a$ cần tìm là: $16 - 13 = 3$.\nKiểm tra: $\\frac{13+3}{17+3} = \\frac{16}{20} = \\frac{4}{5}$ (đúng).", "a = 3", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 60: ÔN TẬP CÁC PHÉP TÍNH VỚI SỐ TỰ NHIÊN VÀ PHÂN SỐ
    # =========================================================================

    # --- Bài 60 - Đề 1 ---
    exams["th4_b60_test1"] = {
        "id": "th4_b60_test1",
        "lessonId": "th4_b60",
        "lessonNum": 60,
        "testNum": 1,
        "title": "Bài 60: Ôn tập các phép tính với số tự nhiên và phân số - Đề số 1",
        "topic": "Ôn tập các phép tính với số tự nhiên và phân số",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép nhân $\\frac{3}{4} \\times \\frac{2}{5}$ là:", ["$\\frac{3}{10}$", "$\\frac{6}{20}$", "$\\frac{5}{9}$", "$\\frac{6}{9}$"], 0, "6/20 = 3/10."),
            make_mc(2, "Kết quả của phép chia $\\frac{5}{7} : \\frac{2}{3}$ là:", ["$\\frac{15}{14}$", "$\\frac{10}{21}$", "$\\frac{7}{10}$", "$\\frac{14}{15}$"], 0, "5/7 x 3/2 = 15/14."),
            make_mc(3, "Tính: $\\frac{2}{5} + \\frac{1}{10} = \\dots$:", ["$\\frac{1}{2}$", "$\\frac{3}{15}$", "$\\frac{3}{10}$", "$\\frac{2}{50}$"], 0, "4/10 + 1/10 = 5/10 = 1/2."),
            make_mc(4, "Một tấm vải dài 45 m. Người ta cắt lấy $\\frac{2}{3}$ tấm vải để may rèm. Số mét vải may rèm là:", ["30 m", "15 m", "25 m", "35 m"], 0, "45 x 2 : 3 = 30 m."),
            make_mc(5, "Tính nhanh: $25 \\times 48 \\times 4$:", ["4 800", "480", "2 400", "1 200"], 0, "(25 x 4) x 48 = 100 x 48 = 4 800."),
            make_mc(6, "Tìm $x$ biết $x \\times \\frac{3}{5} = \\frac{9}{10}$:", ["$\\frac{3}{2}$", "$\\frac{27}{50}$", "$\\frac{2}{3}$", "$\\frac{6}{5}$"], 0, "x = 9/10 : 3/5 = 9/10 x 5/3 = 45/30 = 3/2.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị của các biểu thức sau:\na) $\\frac{4}{7} \\times \\frac{5}{8} : \\frac{5}{14}$\nb) $\\left(\\frac{1}{2} + \\frac{1}{3}\\right) \\times \\frac{6}{5}$", "a) $\\frac{4}{7} \\times \\frac{5}{8} \\times \\frac{14}{5} = \\frac{4 \\times 5 \\times 14}{7 \\times 8 \\times 5} = \\frac{14}{14} = 1$.\nb) $\\frac{1}{2} + \\frac{1}{3} = \\frac{5}{6}$. Ta có: $\\frac{5}{6} \\times \\frac{6}{5} = 1$.", "a) 1; b) 1", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) $\\frac{3}{5} \\times \\frac{7}{9} + \\frac{3}{5} \\times \\frac{2}{9}$\nb) $125 \\times 34 \\times 8$", "a) $\\frac{3}{5} \\times \\left(\\frac{7}{9} + \\frac{2}{9}\\right) = \\frac{3}{5} \\times 1 = \\frac{3}{5}$.\nb) $(125 \\times 8) \\times 34 = 1000 \\times 34 = 34\\,000$.", "a) 3/5; b) 34 000", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình chữ nhật có chiều dài 24 m, chiều rộng bằng $\\frac{3}{4}$ chiều dài. Tính chu vi và diện tích mảnh vườn đó.", "Chiều rộng mảnh vườn là:\n$24 \\times 3 : 4 = 18\\text{ (m)}$.\nChu vi mảnh vườn là:\n$(24 + 18) \\times 2 = 84\\text{ (m)}$.\nDiện tích mảnh vườn là:\n$24 \\times 18 = 432\\text{ (m}^2)$.", "Chu vi: 84 m; Diện tích: 432 m²", 4, 1.0),
            make_essay(4, "Một kho thóc có 48 tấn thóc. Ngày thứ nhất xuất đi $\\frac{1}{4}$ số thóc trong kho. Ngày thứ hai xuất đi $\\frac{2}{3}$ số thóc còn lại sau ngày thứ nhất. Hỏi sau hai ngày, trong kho còn lại bao nhiêu tấn thóc?", "Số thóc xuất trong ngày thứ nhất là:\n$48 \\times \\frac{1}{4} = 12\\text{ (tấn)}$.\nSố thóc còn lại sau ngày thứ nhất là:\n$48 - 12 = 36\\text{ (tấn)}$.\nSố thóc xuất trong ngày thứ hai là:\n$36 \\times \\frac{2}{3} = 24\\text{ (tấn)}$.\nSố thóc còn lại trong kho sau hai ngày là:\n$36 - 24 = 12\\text{ (tấn)}$.", "12 tấn thóc", 5, 1.5),
            make_essay(5, "Tìm $x$:\na) $x : \\frac{2}{5} = \\frac{3}{4} + \\frac{1}{2}$\nb) $\\frac{7}{8} - x \\times \\frac{2}{3} = \\frac{1}{4}$", "a) $\\frac{3}{4} + \\frac{1}{2} = \\frac{5}{4}$. Do đó: $x = \\frac{5}{4} \\times \\frac{2}{5} = \\frac{1}{2}$.\nb) $x \\times \\frac{2}{3} = \\frac{7}{8} - \\frac{1}{4} = \\frac{5}{8}$. Do đó: $x = \\frac{5}{8} : \\frac{2}{3} = \\frac{5}{8} \\times \\frac{3}{2} = \\frac{15}{16}$.", "a) x = 1/2; b) x = 15/16", 5, 1.5),
            make_essay(6, "Tính giá trị biểu thức sau bằng cách nhanh nhất:\n$M = \\left(1 - \\frac{1}{2}\\right) \\times \\left(1 - \\frac{1}{3}\\right) \\times \\left(1 - \\frac{1}{4}\\right) \\times \\left(1 - \\frac{1}{5}\\right)$.", "Ta có:\n$M = \\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{3}{4} \\times \\frac{4}{5} = \\frac{1 \\times 2 \\times 3 \\times 4}{2 \\times 3 \\times 4 \\times 5} = \\frac{1}{5}$.", "1/5", 4, 1.0)
        ]
    }

    # --- Bài 60 - Đề 2 ---
    exams["th4_b60_test2"] = {
        "id": "th4_b60_test2",
        "lessonId": "th4_b60",
        "lessonNum": 60,
        "testNum": 2,
        "title": "Bài 60: Ôn tập các phép tính với số tự nhiên và phân số - Đề số 2",
        "topic": "Ôn tập các phép tính với số tự nhiên và phân số",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{5}{9} \\times 3 = \\dots$:", ["$\\frac{5}{3}$", "$\\frac{15}{27}$", "$\\frac{8}{9}$", "$\\frac{15}{3}$"], 0, "5/9 x 3 = 15/9 = 5/3."),
            make_mc(2, "Kết quả của phép tính $4 : \\frac{2}{5}$ là:", ["10", "$\\frac{8}{5}$", "$\\frac{2}{5}$", "$\\frac{1}{10}$"], 0, "4 x 5/2 = 10."),
            make_mc(3, "Tìm phân số nghịch đảo của $\\frac{3}{7}$:", ["$\\frac{7}{3}$", "$-\\frac{3}{7}$", "$\\frac{1}{3}$", "$\\frac{3}{7}$"], 0, "Nghịch đảo của a/b là b/a: 7/3."),
            make_mc(4, "Một rổ táo có 40 quả, chị Mai đã ăn $\\frac{1}{5}$ số táo, anh Nam ăn $\\frac{1}{4}$ số táo. Cả hai người đã ăn số quả táo là:", ["18 quả", "10 quả", "8 quả", "20 quả"], 0, "Mai ăn: 40:5 = 8 quả. Nam ăn: 40:4 = 10 quả. Tổng = 18 quả."),
            make_mc(5, "Tính: $\\frac{3}{4} \\times \\frac{4}{5} \\times \\frac{5}{6} = \\dots$:", ["$\\frac{1}{2}$", "$\\frac{3}{6}$", "$\\frac{60}{120}$", "1"], 0, "(3 x 4 x 5)/(4 x 5 x 6) = 3/6 = 1/2."),
            make_mc(6, "Số thích hợp điền vào chỗ chấm: $\\frac{2}{3} : \\dots = \\frac{4}{9}$ là:", ["$\\frac{3}{2}$", "$\\frac{8}{27}$", "$\\frac{2}{3}$", "$\\frac{1}{2}$"], 0, "2/3 : 4/9 = 2/3 x 9/4 = 18/12 = 3/2.")
        ],
        "part2": [
            make_essay(1, "Tính:\na) $\\frac{7}{10} \\times \\frac{5}{14}$\nb) $\\frac{8}{15} : \\frac{4}{5}$", "a) $\\frac{7 \\times 5}{10 \\times 14} = \\frac{1 \\times 1}{2 \\times 2} = \\frac{1}{4}$.\nb) $\\frac{8}{15} \\times \\frac{5}{4} = \\frac{8 \\times 5}{15 \\times 4} = \\frac{2 \\times 1}{3 \\times 1} = \\frac{2}{3}$.", "a) 1/4; b) 2/3", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) $\\frac{4}{7} \\times \\frac{3}{5} + \\frac{4}{7} \\times \\frac{2}{5}$\nb) $250 \\times 16$", "a) $\\frac{4}{7} \\times (\\frac{3}{5} + \\frac{2}{5}) = \\frac{4}{7} \\times 1 = \\frac{4}{7}$.\nb) $250 \\times 4 \\times 4 = 1000 \\times 4 = 4000$.", "a) 4/7; b) 4000", 4, 1.0),
            make_essay(3, "Một hình chữ nhật có diện tích $\\frac{8}{15}\\text{ m}^2$, chiều rộng là $\\frac{2}{3}\\text{ m}$. Tính chiều dài và chu vi của hình chữ nhật đó.", "Chiều dài hình chữ nhật là:\n$\\frac{8}{15} : \\frac{2}{3} = \\frac{8}{15} \\times \\frac{3}{2} = \\frac{4}{5}\\text{ (m)}$.\nChu vi hình chữ nhật là:\n$\\left(\\frac{4}{5} + \\frac{2}{3}\\right) \\times 2 = \\left(\\frac{12}{15} + \\frac{10}{15}\\right) \\times 2 = \\frac{22}{15} \\times 2 = \\frac{44}{15}\\text{ (m)}$.", "Chiều dài: 4/5 m; Chu vi: 44/15 m", 4, 1.0),
            make_essay(4, "Một cửa hàng buổi sáng bán được 180 kg gạo, buổi chiều bán được số gạo bằng $\\frac{2}{3}$ số gạo bán buổi sáng. Giá mỗi ki-lô-gam gạo là 18 000 đồng. Hỏi cả ngày hôm đó cửa hàng thu được bao nhiêu tiền bán gạo?", "Số ki-lô-gam gạo bán buổi chiều là:\n$180 \\times 2 : 3 = 120\\text{ (kg)}$.\nTổng số gạo bán trong cả ngày là:\n$180 + 120 = 300\\text{ (kg)}$.\nSố tiền cửa hàng thu được là:\n$300 \\times 18\\,000 = 5\\,400\\,000\\text{ (đồng)}$.", "5 400 000 đồng", 5, 1.5),
            make_essay(5, "Tìm $y$:\na) $y \\times \\frac{3}{8} = \\frac{9}{16}$\nb) $y : \\frac{5}{6} = \\frac{12}{25}$", "a) $y = \\frac{9}{16} : \\frac{3}{8} = \\frac{9}{16} \\times \\frac{8}{3} = \\frac{3}{2}$.\nb) $y = \\frac{12}{25} \\times \\frac{5}{6} = \\frac{2}{5}$.", "a) y = 3/2; b) y = 2/5", 5, 1.5),
            make_essay(6, "Tính tích sau:\n$P = \\left(1 - \\frac{1}{2}\\right) \\times \\left(1 - \\frac{1}{3}\\right) \\times \\left(1 - \\frac{1}{4}\\right) \\times \\dots \\times \\left(1 - \\frac{1}{10}\\right)$.", "Ta biến đổi từng thừa số:\n$P = \\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{3}{4} \\times \\dots \\times \\frac{9}{10} = \\frac{1}{10}$.", "1/10", 4, 1.0)
        ]
    }

    # --- Bài 60 - Đề 3 ---
    exams["th4_b60_test3"] = {
        "id": "th4_b60_test3",
        "lessonId": "th4_b60",
        "lessonNum": 60,
        "testNum": 3,
        "title": "Bài 60: Ôn tập các phép tính với số tự nhiên và phân số - Đề số 3",
        "topic": "Ôn tập các phép tính với số tự nhiên và phân số",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{9}{14} : 3 = \\dots$:", ["$\\frac{3}{14}$", "$\\frac{27}{14}$", "$\\frac{3}{42}$", "$\\frac{9}{42}$"], 0, "9/14 x 1/3 = 3/14."),
            make_mc(2, "Kết quả của phép nhân $\\frac{4}{9} \\times \\frac{3}{8}$ là:", ["$\\frac{1}{6}$", "$\\frac{12}{72}$", "$\\frac{7}{17}$", "$\\frac{2}{3}$"], 0, "12/72 = 1/6."),
            make_mc(3, "Tìm $\\frac{3}{5}$ của 150 kg:", ["90 kg", "60 kg", "50 kg", "100 kg"], 0, "150 x 3 : 5 = 90 kg."),
            make_mc(4, "Một hình vuông có cạnh $\\frac{3}{4}\\text{ m}$. Diện tích hình vuông đó là:", ["$\\frac{9}{16}\\text{ m}^2$", "$\\frac{6}{4}\\text{ m}^2$", "3 m²", "$\\frac{12}{16}\\text{ m}^2$"], 0, "3/4 x 3/4 = 9/16 m²."),
            make_mc(5, "Tính: $\\left(\\frac{2}{3} + \\frac{1}{3}\\right) : \\frac{5}{7}$:", ["$\\frac{7}{5}$", "$\\frac{5}{7}$", "1", "$\\frac{2}{5}$"], 0, "1 : 5/7 = 7/5."),
            make_mc(6, "Giá trị của biểu thức $15 \\times (120 : 6)$ là:", ["300", "250", "350", "400"], 0, "15 x 20 = 300.")
        ],
        "part2": [
            make_essay(1, "Tính giá trị biểu thức:\na) $\\frac{5}{8} \\times \\frac{4}{15} + \\frac{7}{12}$\nb) $\\frac{9}{10} : \\frac{3}{5} - \\frac{1}{2}$", "a) $\\frac{5}{8} \\times \\frac{4}{15} = \\frac{1}{6}$. Ta có: $\\frac{1}{6} + \\frac{7}{12} = \\frac{2}{12} + \\frac{7}{12} = \\frac{9}{12} = \\frac{3}{4}$.\nb) $\\frac{9}{10} \\times \\frac{5}{3} = \\frac{3}{2}$. Ta có: $\\frac{3}{2} - \\frac{1}{2} = 1$.", "a) 3/4; b) 1", 4, 1.0),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) $\\frac{5}{13} \\times \\frac{8}{17} + \\frac{5}{13} \\times \\frac{9}{17}$\nb) $\\frac{11}{12} \\times \\frac{5}{7} - \\frac{11}{12} \\times \\frac{2}{7}$", "a) $\\frac{5}{13} \\times (\\frac{8}{17} + \\frac{9}{17}) = \\frac{5}{13} \\times 1 = \\frac{5}{13}$.\nb) $\\frac{11}{12} \\times (\\frac{5}{7} - \\frac{2}{7}) = \\frac{11}{12} \\times \\frac{3}{7} = \\frac{11}{28}$.", "a) 5/13; b) 11/28", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình chữ nhật có chiều rộng 15 m, chiều dài gấp đôi chiều rộng. Người ta dùng $\\frac{2}{5}$ diện tích mảnh vườn để trồng rau xanh. Tính diện tích phần đất trồng rau xanh.", "Chiều dài mảnh vườn là: $15 \\times 2 = 30\\text{ (m)}$.\nDiện tích cả mảnh vườn là: $30 \\times 15 = 450\\text{ (m}^2)$.\nDiện tích phần đất trồng rau xanh là:\n$450 \\times \\frac{2}{5} = 180\\text{ (m}^2)$.", "180 m²", 4, 1.0),
            make_essay(4, "Một đoàn tàu chở hàng gồm 8 toa, mỗi toa chở 35 tấn hàng. Đến một nhà máy, người ta dỡ xuống $\\frac{3}{7}$ số hàng trên tàu. Hỏi đoàn tàu còn lại bao nhiêu tấn hàng?", "Tổng số tấn hàng cả đoàn tàu chở là:\n$35 \\times 8 = 280\\text{ (tấn)}$.\nSố tấn hàng đã dỡ xuống là:\n$280 \\times 3 : 7 = 120\\text{ (tấn)}$.\nSố tấn hàng còn lại trên đoàn tàu là:\n$280 - 120 = 160\\text{ (tấn)}$.", "160 tấn hàng", 5, 1.5),
            make_essay(5, "Tìm $x$:\na) $x \\times \\frac{4}{7} = \\frac{8}{21}$\nb) $x : \\frac{3}{5} = \\frac{5}{9} \\times \\frac{3}{10}$", "a) $x = \\frac{8}{21} : \\frac{4}{7} = \\frac{8}{21} \\times \\frac{7}{4} = \\frac{2}{3}$.\nb) $\\frac{5}{9} \\times \\frac{3}{10} = \\frac{1}{6}$. Do đó: $x = \\frac{1}{6} \\times \\frac{3}{5} = \\frac{1}{10}$.", "a) x = 2/3; b) x = 1/10", 5, 1.5),
            make_essay(6, "Tính giá trị biểu thức:\n$K = \\left(1 + \\frac{1}{2}\\right) \\times \\left(1 + \\frac{1}{3}\\right) \\times \\left(1 + \\frac{1}{4}\\right) \\times \\dots \\times \\left(1 + \\frac{1}{9}\\right)$.", "Ta biến đổi từng thừa số:\n$K = \\frac{3}{2} \\times \\frac{4}{3} \\times \\frac{5}{4} \\times \\dots \\times \\frac{10}{9}$.\nRút gọn các thừa số giống nhau ở tử số và mẫu số:\n$K = \\frac{10}{2} = 5$.", "5", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 61: ÔN TẬP HÌNH HỌC VÀ ĐO LƯỜNG
    # =========================================================================

    # --- Bài 61 - Đề 1 ---
    exams["th4_b61_test1"] = {
        "id": "th4_b61_test1",
        "lessonId": "th4_b61",
        "lessonNum": 61,
        "testNum": 1,
        "title": "Bài 61: Ôn tập hình học và đo lường - Đề số 1",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình bình hành có độ dài đáy 18 cm, chiều cao 10 cm. Diện tích của nó là:", ["180 cm²", "90 cm²", "360 cm²", "56 cm²"], 0, "18 x 10 = 180 cm²."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $5\\text{ m}^2 \\text{ } 8\\text{ dm}^2 = \\dots \\text{ dm}^2$ là:", ["508", "580", "5 008", "58"], 0, "500 + 8 = 508 dm²."),
            make_mc(3, "Đổi $3\\text{ tấn } 45\\text{ kg} = \\dots \\text{ kg}$:", ["3 045", "3 450", "345", "34 500"], 0, "3 000 + 45 = 3 045 kg."),
            make_mc(4, "Một hình thoi có độ dài hai đường chéo là 12 cm và 16 cm. Diện tích hình thoi là:", ["96 cm²", "192 cm²", "28 cm²", "48 cm²"], 0, "(12 x 16) : 2 = 96 cm²."),
            make_mc(5, "Góc có số đo lớn hơn góc vuông và nhỏ hơn góc bẹt là:", ["Góc tù", "Góc nhọn", "Góc bẹt", "Góc vuông"], 0, "Định nghĩa góc tù."),
            make_mc(6, "Bác Hồ sinh năm 1890. Năm đó thuộc thế kỉ nào?", ["XIX", "XX", "XVIII", "XVII"], 0, "Năm 1890 thuộc thế kỉ XIX.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $4\\text{ thế kỉ } 20\\text{ năm} = \\dots \\text{ năm}$\nb) $7\\text{ dm}^2 \\text{ } 35\\text{ mm}^2 = \\dots \\text{ mm}^2$", "a) $4 \\times 100 + 20 = 420\\text{ năm}$.\nb) $7 \\times 10\\,000 + 35 = 70\\,035\\text{ mm}^2$.", "a) 420; b) 70 035", 4, 1.0),
            make_essay(2, "Cho hình thoi MNPQ có hai đường chéo MP = 20 cm và NQ = 14 cm. Tính diện tích của hình thoi MNPQ.", "Diện tích của hình thoi MNPQ là:\n$20 \\times 14 : 2 = 140\\text{ (cm}^2)$.", "140 cm²", 4, 1.0),
            make_essay(3, "Một mảnh đất hình bình hành có độ dài đáy là 40 m, chiều cao tương ứng bằng $\\frac{3}{5}$ độ dài đáy. Tính diện tích mảnh đất đó.", "Chiều cao mảnh đất hình bình hành là:\n$40 \\times 3 : 5 = 24\\text{ (m)}$.\nDiện tích mảnh đất là:\n$40 \\times 24 = 960\\text{ (m}^2)$.", "960 m²", 4, 1.0),
            make_essay(4, "Một thửa ruộng hình chữ nhật có chu vi 160 m, chiều dài hơn chiều rộng 20 m. Người ta trồng lúa trên thửa ruộng đó, cứ $100\\text{ m}^2$ thu hoạch được 60 kg thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?", "Nửa chu vi thửa ruộng là: $160 : 2 = 80\\text{ (m)}$.\nChiều dài thửa ruộng là: $(80 + 20) : 2 = 50\\text{ (m)}$.\nChiều rộng thửa ruộng là: $80 - 50 = 30\\text{ (m)}$.\nDiện tích thửa ruộng là: $50 \\times 30 = 1500\\text{ (m}^2)$.\nSố ki-lô-gam thóc thu hoạch được là:\n$1500 : 100 \\times 60 = 900\\text{ (kg)}$.\nĐổi: $900\\text{ kg} = 9\\text{ tạ}$.", "9 tạ thóc", 5, 1.5),
            make_essay(5, "Một căn phòng hình chữ nhật dài 8 m, rộng 6 m. Người ta dùng các viên gạch men hình vuông cạnh 4 dm để lát kín nền phòng. Biết giá mỗi viên gạch là 35 000 đồng. Tính tổng số tiền mua gạch để lát nền căn phòng đó.", "Diện tích căn phòng là: $8 \\times 6 = 48\\text{ (m}^2) = 4800\\text{ dm}^2$.\nDiện tích một viên gạch men là: $4 \\times 4 = 16\\text{ (dm}^2)$.\nSố viên gạch cần mua là: $4800 : 16 = 300\\text{ (viên)}$.\nTổng số tiền mua gạch là:\n$300 \\times 35\\,000 = 10\\,500\\,000\\text{ (đồng)}$.", "10 500 000 đồng", 5, 1.5),
            make_essay(6, "Cho hình vuông ABCD có cạnh 14 cm. Người ta vẽ 4 cung tròn hoặc chia thành 4 hình vuông nhỏ cạnh 7 cm rồi dựng một hình thoi MNPQ có 4 đỉnh là trung điểm của 4 cạnh hình vuông ABCD. Tính diện tích hình thoi MNPQ.", "Hai đường chéo của hình thoi MNPQ bằng đúng cạnh của hình vuông ABCD, tức là: $MP = NQ = 14\\text{ cm}$.\nDiện tích hình thoi MNPQ là:\n$14 \\times 14 : 2 = 98\\text{ (cm}^2)$.\n(Hoặc diện tích hình thoi bằng một nửa diện tích hình vuông: $14 \\times 14 : 2 = 98\\text{ cm}^2$).", "98 cm²", 4, 1.0)
        ]
    }

    # --- Bài 61 - Đề 2 ---
    exams["th4_b61_test2"] = {
        "id": "th4_b61_test2",
        "lessonId": "th4_b61",
        "lessonNum": 61,
        "testNum": 2,
        "title": "Bài 61: Ôn tập hình học và đo lường - Đề số 2",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Công thức tính diện tích hình thoi có độ dài hai đường chéo $m$ và $n$ là:", ["S = (m x n) : 2", "S = m x n", "S = (m + n) x 2", "S = (m + n) : 2"], 0, "S = (m x n) : 2."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $6\\text{ tấn } 5\\text{ tạ} = \\dots \\text{ yến}$ là:", ["650", "65", "6 500", "605"], 0, "65 tạ = 650 yến."),
            make_mc(3, "Đổi $800\\text{ dm}^2 = \\dots \\text{ m}^2$:", ["8", "80", "8000", "0,8"], 0, "100 dm² = 1 m² nên 800 dm² = 8 m²."),
            make_mc(4, "Một mảnh đất hình bình hành có đáy 25 m, chiều cao 16 m. Diện tích mảnh đất là:", ["400 m²", "200 m²", "82 m²", "41 m²"], 0, "25 x 16 = 400 m²."),
            make_mc(5, "Góc tạo bởi hai kim đồng hồ lúc 6 giờ đúng là:", ["Góc bẹt", "Góc vuông", "Góc tù", "Góc nhọn"], 0, "Lúc 6 giờ góc là 180° = góc bẹt."),
            make_mc(6, "Năm 1010 Lý Thái Tổ dời đô về Thăng Long thuộc thế kỉ nào?", ["XI", "X", "IX", "XII"], 0, "Năm 1010 thuộc thế kỉ XI.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $3\\text{ phút } 45\\text{ giây} = \\dots \\text{ giây}$\nb) $9\\text{ m}^2 \\text{ } 24\\text{ dm}^2 = \\dots \\text{ dm}^2$", "a) $3 \\times 60 + 45 = 225\\text{ giây}$.\nb) $9 \\times 100 + 24 = 924\\text{ dm}^2$.", "a) 225; b) 924", 4, 1.0),
            make_essay(2, "Một tấm kính hình thoi có độ dài hai đường chéo là 15 dm và 8 dm. Tính diện tích của tấm kính đó.", "Diện tích của tấm kính hình thoi là:\n$15 \\times 8 : 2 = 60\\text{ (dm}^2)$.", "60 dm²", 4, 1.0),
            make_essay(3, "Một khu đất hình bình hành có chiều cao 18 m, độ dài đáy gấp đôi chiều cao. Tính diện tích khu đất đó.", "Độ dài đáy khu đất hình bình hành là:\n$18 \\times 2 = 36\\text{ (m)}$.\nDiện tích khu đất là:\n$36 \\times 18 = 648\\text{ (m}^2)$.", "648 m²", 4, 1.0),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chiều dài 35 m, chiều rộng bằng $\\frac{3}{5}$ chiều dài. Người ta dành $150\\text{ m}^2$ để đào ao thả cá, phần đất còn lại dùng để trồng cây ăn quả. Tính diện tích phần đất trồng cây ăn quả.", "Chiều rộng mảnh vườn là:\n$35 \\times 3 : 5 = 21\\text{ (m)}$.\nDiện tích cả mảnh vườn là:\n$35 \\times 21 = 735\\text{ (m}^2)$.\nDiện tích phần đất trồng cây ăn quả là:\n$735 - 150 = 585\\text{ (m}^2)$.", "585 m²", 5, 1.5),
            make_essay(5, "Một đoàn xe chở 12 tấn 6 tạ phân bón cho hợp tác xã. Đợt đầu có 2 xe chở mỗi xe 25 tạ. Đợt hai có 4 xe nhỏ chở số hàng còn lại. Hỏi trung bình mỗi xe nhỏ ở đợt hai chở được bao nhiêu tạ phân bón?", "Đổi: $12\\text{ tấn } 6\\text{ tạ} = 126\\text{ tạ}$.\n2 xe đợt đầu chở được số tạ hàng là:\n$25 \\times 2 = 50\\text{ (tạ)}$.\nSố hàng còn lại cho đợt hai là:\n$126 - 50 = 76\\text{ (tạ)}$.\nTrung bình mỗi xe nhỏ ở đợt hai chở được là:\n$76 : 4 = 19\\text{ (tạ)}$.", "19 tạ", 5, 1.5),
            make_essay(6, "Một tấm tôn hình chữ nhật có chu vi 44 dm, chiều dài hơn chiều rộng 6 dm. Người ta cắt từ tấm tôn đó một miếng tôn hình thoi có hai đường chéo bằng đúng chiều dài và chiều rộng của tấm tôn. Tính diện tích miếng tôn hình thoi.", "Nửa chu vi tấm tôn là: $44 : 2 = 22\\text{ (dm)}$.\nChiều dài tấm tôn là: $(22 + 6) : 2 = 14\\text{ (dm)}$.\nChiều rộng tấm tôn là: $22 - 14 = 8\\text{ (dm)}$.\nĐộ dài hai đường chéo hình thoi lần lượt là 14 dm và 8 dm.\nDiện tích miếng tôn hình thoi là:\n$14 \\times 8 : 2 = 56\\text{ (dm}^2)$.", "56 dm²", 4, 1.0)
        ]
    }

    # --- Bài 61 - Đề 3 ---
    exams["th4_b61_test3"] = {
        "id": "th4_b61_test3",
        "lessonId": "th4_b61",
        "lessonNum": 61,
        "testNum": 3,
        "title": "Bài 61: Ôn tập hình học và đo lường - Đề số 3",
        "topic": "Ôn tập hình học và đo lường",
        "chapter": "Chủ đề 13: Ôn tập cuối năm",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình bình hành có đáy 30 cm, chiều cao bằng $\\frac{1}{2}$ đáy. Diện tích hình bình hành là:", ["450 cm²", "900 cm²", "225 cm²", "75 cm²"], 0, "Chiều cao = 15 cm. Diện tích = 30 x 15 = 450 cm²."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $4\\text{ tấn } 50\\text{ kg} = \\dots \\text{ kg}$ là:", ["4 050", "4 500", "450", "40 500"], 0, "4 000 + 50 = 4 050 kg."),
            make_mc(3, "Đổi $12\\text{ m}^2 = \\dots \\text{ dm}^2$:", ["1 200", "120", "12 000", "12"], 0, "12 x 100 = 1 200 dm²."),
            make_mc(4, "Một hình thoi có độ dài hai đường chéo là 8 dm và 25 dm. Diện tích hình thoi là:", ["100 dm²", "200 dm²", "50 dm²", "33 dm²"], 0, "(8 x 25) : 2 = 100 dm²."),
            make_mc(5, "Hai đường thẳng vuông góc với nhau tạo thành:", ["4 góc vuông", "2 góc vuông", "1 góc vuông", "2 góc bẹt"], 0, "Tạo thành 4 góc vuông xung quanh giao điểm."),
            make_mc(6, "Năm 1945 Chủ tịch Hồ Chí Minh đọc bản Tuyên ngôn Độc lập. Năm đó thuộc thế kỉ:", ["XX", "XIX", "XXI", "XVIII"], 0, "Năm 1945 thuộc thế kỉ XX.")
        ],
        "part2": [
            make_essay(1, "Viết số thích hợp vào chỗ chấm:\na) $5\\text{ thế kỉ } = \\dots \\text{ năm}$\nb) $6\\text{ dm}^2 \\text{ } 80\\text{ mm}^2 = \\dots \\text{ mm}^2$", "a) $5 \\times 100 = 500\\text{ năm}$.\nb) $6 \\times 10\\,000 + 80 = 60\\,080\\text{ mm}^2$.", "a) 500; b) 60 080", 4, 1.0),
            make_essay(2, "Một tấm thảm hình thoi có hai đường chéo dài 18 dm và 12 dm. Người ta may đường diềm ren bao quanh thảm. Biết mỗi đề-xi-mét vuông thảm có giá 45 000 đồng. Tính tổng giá trị của tấm thảm đó.", "Diện tích tấm thảm hình thoi là:\n$18 \\times 12 : 2 = 108\\text{ (dm}^2)$.\nGiá trị của tấm thảm là:\n$108 \\times 45\\,000 = 4\\,860\\,000\\text{ (đồng)}$.", "4 860 000 đồng", 4, 1.0),
            make_essay(3, "Một mảnh đất hình bình hành có đáy dài 28 m, chiều cao bằng $\\frac{3}{4}$ đáy. Người ta trồng rau trên mảnh đất đó, cứ mỗi mét vuông thu được 4 kg rau. Hỏi cả mảnh đất thu hoạch được bao nhiêu ki-lô-gam rau?", "Chiều cao mảnh đất là: $28 \\times 3 : 4 = 21\\text{ (m)}$.\nDiện tích mảnh đất là: $28 \\times 21 = 588\\text{ (m}^2)$.\nSố ki-lô-gam rau thu hoạch được là:\n$588 \\times 4 = 2352\\text{ (kg)}$.", "2352 kg rau", 4, 1.0),
            make_essay(4, "Một sân trường hình chữ nhật có chu vi 240 m, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Người ta lát gạch men hình vuông cạnh 5 dm toàn bộ mặt sân trường. Tính số viên gạch cần dùng để lát sân trường đó.", "Nửa chu vi sân trường là: $240 : 2 = 120\\text{ (m)}$.\nTổng số phần bằng nhau là: $2 + 3 = 5\\text{ (phần)}$.\nChiều rộng sân trường là: $120 : 5 \\times 2 = 48\\text{ (m)}$.\nChiều dài sân trường là: $120 - 48 = 72\\text{ (m)}$.\nDiện tích sân trường là: $72 \\times 48 = 3456\\text{ (m}^2) = 345\\,600\\text{ dm}^2$.\nDiện tích một viên gạch men là: $5 \\times 5 = 25\\text{ (dm}^2)$.\nSố viên gạch cần dùng là: $345\\,600 : 25 = 13\\,824\\text{ (viên)}$.", "13 824 viên gạch", 5, 1.5),
            make_essay(5, "Một kho hàng có 15 tấn hàng. Người ta dùng 3 xe lớn mỗi xe chở 25 tạ hàng và 4 xe nhỏ mỗi xe chở 15 tạ hàng để chuyển hàng ra cảng. Hỏi sau chuyến chở hàng của cả đoàn xe đó, trong kho còn lại bao nhiêu tạ hàng?", "Đổi: $15\\text{ tấn} = 150\\text{ tạ}$.\n3 xe lớn chở được số tạ hàng là: $25 \\times 3 = 75\\text{ (tạ)}$.\n4 xe nhỏ chở được số tạ hàng là: $15 \\times 4 = 60\\text{ (tạ)}$.\nCả đoàn xe chở được số tạ hàng là: $75 + 60 = 135\\text{ (tạ)}$.\nSố hàng còn lại trong kho là: $150 - 135 = 15\\text{ (tạ)}$.", "15 tạ", 5, 1.5),
            make_essay(6, "Cho hình chữ nhật ABCD có chiều dài 20 cm, chiều rộng 12 cm. Lấy M, N, P, Q lần lượt là trung điểm của các cạnh AB, BC, CD, DA. Nối các điểm đó lại ta được hình thoi MNPQ. Tính diện tích hình thoi MNPQ và so sánh với diện tích hình chữ nhật ABCD.", "Diện tích hình chữ nhật ABCD là:\n$20 \\times 12 = 240\\text{ (cm}^2)$.\nHình thoi MNPQ có độ dài hai đường chéo lần lượt bằng chiều rộng và chiều dài của hình chữ nhật: $MP = 12\\text{ cm}$ (đoạn nối N, Q dài 20 cm, MP dài 12 cm).\nDiện tích hình thoi MNPQ là:\n$20 \\times 12 : 2 = 120\\text{ (cm}^2)$.\nVậy diện tích hình thoi MNPQ bằng một nửa diện tích hình chữ nhật ABCD.", "Diện tích hình thoi = 120 cm², bằng 1/2 diện tích hình chữ nhật", 4, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_ch13_part1_exams()
    print(f"Tổng số đề Chủ đề 13 (Phần 1): {len(ex)} (Kỳ vọng: 9)")
    for b in range(59, 62):
        for t in range(1, 4):
            key = f"th4_b{b}_test{t}"
            assert key in ex, f"Thiếu {key}"
            assert len(ex[key]["part1"]) == 6
            assert len(ex[key]["part2"]) == 6
            p1_pts = sum(q["points"] for q in ex[key]["part1"])
            p2_pts = sum(q["points"] for q in ex[key]["part2"])
            assert abs(p1_pts - 3.0) < 1e-6
            assert abs(p2_pts - 7.0) < 1e-6
    print("Phần 1 của Chủ đề 13 hoàn hảo 100%!")
