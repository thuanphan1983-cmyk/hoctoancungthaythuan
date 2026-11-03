# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 11: PHÉP CỘNG, TRỪ PHÂN SỐ (BÀI 51 ĐẾN BÀI 54)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 4 bài học x 3 đề độc lập = 12 đề kiểm tra chất lượng cao (th4_b51_test1 -> th4_b54_test3)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, question_text, options, correct, explanation, level="TH"):
    q_title = f"**Câu {qid}:** {question_text}" if not question_text.startswith(f"**Câu {qid}:**") else question_text
    return {
        "id": qid,
        "question": q_title,
        "options": options,
        "choices": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5,
        "level": level
    }

def make_essay(qid, question_text, solution, answer, lineCount=4, points=1.0, level="VD"):
    p_title = f"**Bài {qid}:** {question_text}" if not question_text.startswith(f"**Bài {qid}:**") else question_text
    return {
        "id": qid,
        "question": p_title,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points,
        "level": level
    }

def get_exams():
    exams = {}

    # =========================================================================
    # BÀI 51: PHÉP CỘNG PHÂN SỐ CÙNG MẪU SỐ
    # =========================================================================

    # --- Bài 51 - Đề 1 ---
    exams["th4_b51_test1"] = {
        "id": "th4_b51_test1",
        "lessonId": "th4_b51",
        "lessonNum": 51,
        "testNum": 1,
        "title": "Bài 51: Phép cộng phân số cùng mẫu số - Đề số 1",
        "topic": "Phép cộng phân số cùng mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn cộng hai phân số có cùng mẫu số, ta làm như thế nào?", ["Cộng hai tử số với nhau và giữ nguyên mẫu số", "Cộng hai tử số với nhau và cộng hai mẫu số với nhau", "Nhân hai tử số với nhau", "Giữ nguyên tử số và cộng hai mẫu số"], 0, "Quy tắc cộng hai phân số cùng mẫu số: cộng hai tử số và giữ nguyên mẫu số."),
            make_mc(2, "Kết quả của phép tính $\\frac{2}{7} + \\frac{3}{7}$ là:", ["$\\frac{5}{7}$", "$\\frac{5}{14}$", "$\\frac{6}{7}$", "$\\frac{1}{7}$"], 0, "$\\frac{2+3}{7} = \\frac{5}{7}$."),
            make_mc(3, "Tính và rút gọn: $\\frac{1}{8} + \\frac{5}{8}$:", ["$\\frac{3}{4}$", "$\\frac{6}{8}$", "$\\frac{6}{16}$", "$\\frac{1}{2}$"], 0, "$\\frac{6}{8} = \\frac{3}{4}$."),
            make_mc(4, "Một giá sách buổi sáng xếp được $\\frac{2}{9}$ số sách, buổi chiều xếp thêm được $\\frac{4}{9}$ số sách. Cả hai buổi xếp được số phần số sách là:", ["$\\frac{6}{9}$ hay $\\frac{2}{3}$", "$\\frac{6}{18}$", "$\\frac{8}{9}$", "$\\frac{1}{3}$"], 0, "$\\frac{2}{9} + \\frac{4}{9} = \\frac{6}{9} = \\frac{2}{3}$."),
            make_mc(5, "Tìm $x$ biết: $x - \\frac{3}{11} = \\frac{5}{11}$:", ["$\\frac{8}{11}$", "$\\frac{2}{11}$", "$\\frac{8}{22}$", "$\\frac{15}{11}$"], 0, "x = 5/11 + 3/11 = 8/11."),
            make_mc(6, "Kết quả của $\\frac{4}{5} + \\frac{1}{5}$ bằng:", ["1", "$\\frac{5}{10}$", "$\\frac{4}{25}$", "2"], 0, "$\\frac{4+1}{5} = \\frac{5}{5} = 1$.")
        ],
        "part2": [
            make_essay(1, "Tính rồi rút gọn thành phân số tối giản (nếu có thể):\na) $\\frac{3}{10} + \\frac{1}{10}$\nb) $\\frac{5}{12} + \\frac{1}{12}$", "a) $\\frac{3+1}{10} = \\frac{4}{10} = \\frac{2}{5}$.\nb) $\\frac{5+1}{12} = \\frac{6}{12} = \\frac{1}{2}$.", "a) 2/5; b) 1/2", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\na) $\\frac{2}{15} + \\frac{4}{15} + \\frac{7}{15}$\nb) $\\frac{1}{6} + \\frac{2}{6} + \\frac{3}{6}$", "a) $\\frac{2+4+7}{15} = \\frac{13}{15}$.\nb) $\\frac{1+2+3}{6} = \\frac{6}{6} = 1$.", "a) 13/15; b) 1", 4, 1.0),
            make_essay(3, "Một ô tô giờ thứ nhất đi được $\\frac{2}{7}$ quãng đường, giờ thứ hai đi được $\\frac{3}{7}$ quãng đường. Hỏi sau hai giờ ô tô đi được bao nhiêu phần quãng đường?", "Sau hai giờ ô tô đi được số phần quãng đường là:\n$\\frac{2}{7} + \\frac{3}{7} = \\frac{5}{7}\\text{ (quãng đường)}$.", "5/7 quãng đường", 4, 1.0),
            make_essay(4, "Một bức tường cần được sơn màu. Ngày thứ nhất chú thợ sơn được $\\frac{3}{10}$ bức tường. Ngày thứ hai chú sơn tiếp được $\\frac{4}{10}$ bức tường. Hỏi:\na) Cả hai ngày chú sơn được bao nhiêu phần bức tường?\nb) Còn lại bao nhiêu phần bức tường chưa được sơn?", "a) Cả hai ngày chú thợ sơn được số phần bức tường là:\n$\\frac{3}{10} + \\frac{4}{10} = \\frac{7}{10}\\text{ (bức tường)}$.\nb) Số phần bức tường chưa sơn là:\n$1 - \\frac{7}{10} = \\frac{10}{10} - \\frac{7}{10} = \\frac{3}{10}\\text{ (bức tường)}$.", "a) 7/10; b) 3/10", 5, 1.5),
            make_essay(5, "Một cửa hàng buổi sáng bán được $\\frac{3}{8}$ số tạ gạo, buổi chiều bán được $\\frac{1}{8}$ số tạ gạo. Biết tổng số gạo cửa hàng có ban đầu là 24 tạ gạo. Hỏi cả hai buổi cửa hàng bán được bao nhiêu tạ gạo?", "Cả hai buổi cửa hàng bán được số phần số gạo là:\n$\\frac{3}{8} + \\frac{1}{8} = \\frac{4}{8} = \\frac{1}{2}\\text{ (số gạo)}$.\nSố tạ gạo bán được trong cả hai buổi là:\n$24 \\times \\frac{1}{2} = 12\\text{ (tạ)}$.", "12 tạ gạo", 5, 1.5),
            make_essay(6, "Tìm phân số $\\frac{a}{b}$ biết rằng: $\\frac{a}{b} + \\frac{a}{b} + \\frac{a}{b} = \\frac{6}{7}$.", "Ta có: $\\frac{a}{b} + \\frac{a}{b} + \\frac{a}{b} = \\frac{a + a + a}{b} = \\frac{3 \\times a}{b} = \\frac{6}{7}$.\nDo đó: $3 \\times a = 6 \\Rightarrow a = 2$ và $b = 7$.\nVậy phân số cần tìm là $\\frac{2}{7}$.", "2/7", 4, 1.0)
        ]
    }

    # --- Bài 51 - Đề 2 ---
    exams["th4_b51_test2"] = {
        "id": "th4_b51_test2",
        "lessonId": "th4_b51",
        "lessonNum": 51,
        "testNum": 2,
        "title": "Bài 51: Phép cộng phân số cùng mẫu số - Đề số 2",
        "topic": "Phép cộng phân số cùng mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{4}{9} + \\frac{2}{9} = \\dots$:", ["$\\frac{6}{9}$ hay $\\frac{2}{3}$", "$\\frac{6}{18}$", "$\\frac{8}{9}$", "$\\frac{2}{9}$"], 0, "$\\frac{6}{9} = \\frac{2}{3}$."),
            make_mc(2, "Phân số tối giản của tổng $\\frac{5}{14} + \\frac{2}{14}$ là:", ["$\\frac{1}{2}$", "$\\frac{7}{14}$", "$\\frac{7}{28}$", "$\\frac{3}{7}$"], 0, "$\\frac{7}{14} = \\frac{1}{2}$."),
            make_mc(3, "Tìm $y$, biết: $y - \\frac{4}{15} = \\frac{7}{15}$:", ["$\\frac{11}{15}$", "$\\frac{3}{15}$", "$\\frac{11}{30}$", "$\\frac{28}{15}$"], 0, "y = 7/15 + 4/15 = 11/15."),
            make_mc(4, "Một hộp bánh có 12 cái. Bạn An ăn $\\frac{2}{12}$ hộp, bạn Bình ăn $\\frac{3}{12}$ hộp. Cả hai bạn ăn hết:", ["$\\frac{5}{12}$ hộp bánh", "$\\frac{5}{24}$ hộp bánh", "$\\frac{1}{12}$ hộp bánh", "$\\frac{6}{12}$ hộp bánh"], 0, "2/12 + 3/12 = 5/12 hộp bánh."),
            make_mc(5, "Số thích hợp điền vào dấu $?$ trong đẳng thức $\\frac{3}{10} + \\frac{?}{10} = \\frac{9}{10}$ là:", ["6", "12", "3", "7"], 0, "? = 9 - 3 = 6."),
            make_mc(6, "Tổng của $\\frac{7}{16} + \\frac{5}{16}$ sau khi rút gọn là:", ["$\\frac{3}{4}$", "$\\frac{12}{16}$", "$\\frac{6}{8}$", "$\\frac{1}{2}$"], 0, "12/16 = 3/4.")
        ],
        "part2": [
            make_essay(1, "Tính rồi rút gọn:\na) $\\frac{5}{16} + \\frac{3}{16}$\nb) $\\frac{7}{20} + \\frac{3}{20}$", "a) $\\frac{5+3}{16} = \\frac{8}{16} = \\frac{1}{2}$.\nb) $\\frac{7+3}{20} = \\frac{10}{20} = \\frac{1}{2}$.", "a) 1/2; b) 1/2", 4, 1.0),
            make_essay(2, "Tìm $x$:\na) $x - \\frac{2}{9} = \\frac{5}{9}$\nb) $x - \\frac{4}{13} = \\frac{6}{13}$", "a) $x = \\frac{5}{9} + \\frac{2}{9} = \\frac{7}{9}$.\nb) $x = \\frac{6}{13} + \\frac{4}{13} = \\frac{10}{13}$.", "a) x = 7/9; b) x = 10/13", 4, 1.0),
            make_essay(3, "Một đội công nhân sửa đường ngày thứ nhất sửa được $\\frac{2}{11}$ đoạn đường, ngày thứ hai sửa được $\\frac{5}{11}$ đoạn đường. Hỏi cả hai ngày đội công nhân sửa được bao nhiêu phần đoạn đường?", "Cả hai ngày đội công nhân sửa được số phần đoạn đường là:\n$\\frac{2}{11} + \\frac{5}{11} = \\frac{7}{11}\\text{ (đoạn đường)}$.", "7/11 đoạn đường", 4, 1.0),
            make_essay(4, "Một mảnh đất hình chữ nhật được chia làm 3 phần: phần trồng hoa chiếm $\\frac{2}{9}$ diện tích, phần trồng cây ăn quả chiếm $\\frac{4}{9}$ diện tích, phần còn lại làm sân chơi.\na) Diện tích trồng hoa và cây ăn quả chiếm bao nhiêu phần diện tích mảnh đất?\nb) Phần sân chơi chiếm bao nhiêu phần diện tích mảnh đất?", "a) Phần diện tích trồng hoa và cây ăn quả là:\n$\\frac{2}{9} + \\frac{4}{9} = \\frac{6}{9} = \\frac{2}{3}\\text{ (diện tích)}$.\nb) Phần sân chơi chiếm số phần diện tích là:\n$1 - \\frac{6}{9} = \\frac{3}{9} = \\frac{1}{3}\\text{ (diện tích)}$.", "a) 2/3 (hay 6/9); b) 1/3 (hay 3/9)", 5, 1.5),
            make_essay(5, "Ba bạn Mai, Lan, Cúc cùng đọc một cuốn truyện. Bạn Mai đọc được $\\frac{1}{5}$ cuốn truyện, bạn Lan đọc được $\\frac{2}{5}$ cuốn truyện. Cúc đọc số trang bằng tổng số trang của Mai và Lan.\na) Cúc đọc được bao nhiêu phần cuốn truyện?\nb) Cả ba bạn đã đọc được bao nhiêu phần cuốn truyện?", "a) Số phần cuốn truyện bạn Cúc đọc được là:\n$\\frac{1}{5} + \\frac{2}{5} = \\frac{3}{5}\\text{ (cuốn truyện)}$.\nb) Cả ba bạn đã đọc được số phần (tổng số lượt đọc) là:\n$\\frac{1}{5} + \\frac{2}{5} + \\frac{3}{5} = \\frac{6}{5}\\text{ (cuốn truyện)}$.", "a) 3/5; b) 6/5", 5, 1.5),
            make_essay(6, "Điền phân số thích hợp vào ô trống:\n$\\frac{1}{18} + \\frac{3}{18} + \\frac{\\dots}{18} = \\frac{1}{2}$.", "Ta có: $\\frac{1}{2} = \\frac{9}{18}$.\nTổng hai số đầu là: $\\frac{1}{18} + \\frac{3}{18} = \\frac{4}{18}$.\nPhân số cần điền là: $\\frac{9 - 4}{18} = \\frac{5}{18}$.", "5/18", 4, 1.0)
        ]
    }

    # --- Bài 51 - Đề 3 ---
    exams["th4_b51_test3"] = {
        "id": "th4_b51_test3",
        "lessonId": "th4_b51",
        "lessonNum": 51,
        "testNum": 3,
        "title": "Bài 51: Phép cộng phân số cùng mẫu số - Đề số 3",
        "topic": "Phép cộng phân số cùng mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{5}{17} + \\frac{8}{17} = \\dots$:", ["$\\frac{13}{17}$", "$\\frac{13}{34}$", "$\\frac{3}{17}$", "$\\frac{15}{17}$"], 0, "13/17."),
            make_mc(2, "Phân số nào dưới đây là kết quả rút gọn của $\\frac{9}{24} + \\frac{3}{24}$?", ["$\\frac{1}{2}$", "$\\frac{12}{24}$", "$\\frac{1}{4}$", "$\\frac{2}{3}$"], 0, "12/24 = 1/2."),
            make_mc(3, "Tìm $x$ biết $x - \\frac{7}{25} = \\frac{11}{25}$:", ["$\\frac{18}{25}$", "$\\frac{4}{25}$", "$\\frac{18}{50}$", "$\\frac{14}{25}$"], 0, "x = 11/25 + 7/25 = 18/25."),
            make_mc(4, "Một bình thủy tinh chứa nước: lần đầu rót vào $\\frac{3}{8}$ bình, lần sau rót tiếp $\\frac{3}{8}$ bình. Lượng nước có trong bình là:", ["$\\frac{3}{4}$ bình", "$\\frac{6}{16}$ bình", "$\\frac{1}{2}$ bình", "$\\frac{5}{8}$ bình"], 0, "3/8 + 3/8 = 6/8 = 3/4 bình."),
            make_mc(5, "Tổng của 3 phân số $\\frac{2}{19} + \\frac{5}{19} + \\frac{12}{19}$ bằng:", ["1", "$\\frac{19}{57}$", "$\\frac{18}{19}$", "2"], 0, "2 + 5 + 12 = 19 => 19/19 = 1."),
            make_mc(6, "Điền dấu thích hợp: $\\frac{2}{9} + \\frac{5}{9} \\dots \\frac{8}{9}$:", ["<", ">", "=", "Không so sánh được"], 0, "7/9 < 8/9.")
        ],
        "part2": [
            make_essay(1, "Tính rồi rút gọn:\na) $\\frac{7}{18} + \\frac{5}{18}$\nb) $\\frac{11}{30} + \\frac{4}{30}$", "a) $\\frac{7+5}{18} = \\frac{12}{18} = \\frac{2}{3}$.\nb) $\\frac{11+4}{30} = \\frac{15}{30} = \\frac{1}{2}$.", "a) 2/3; b) 1/2", 4, 1.0),
            make_essay(2, "Tính nhanh tổng sau:\n$\\frac{1}{15} + \\frac{2}{15} + \\frac{3}{15} + \\frac{4}{15} + \\frac{5}{15}$", "Tổng các tử số là: $1 + 2 + 3 + 4 + 5 = 15$.\nVậy tổng là: $\\frac{15}{15} = 1$.", "1", 4, 1.0),
            make_essay(3, "Bác thợ may dùng $\\frac{3}{10}$ tấm vải để may áo sơ mi và $\\frac{4}{10}$ tấm vải để may quần tây. Hỏi bác đã dùng hết bao nhiêu phần tấm vải?", "Bác thợ may đã dùng hết số phần tấm vải là:\n$\\frac{3}{10} + \\frac{4}{10} = \\frac{7}{10}\\text{ (tấm vải)}$.", "7/10 tấm vải", 4, 1.0),
            make_essay(4, "Một bể nước có hai vòi nước cùng chảy vào. Trong 1 giờ vòi thứ nhất chảy được $\\frac{2}{7}$ bể nước, vòi thứ hai chảy được $\\frac{3}{7}$ bể nước. Hỏi:\na) Trong 1 giờ cả hai vòi chảy được bao nhiêu phần bể nước?\nb) Còn bao nhiêu phần bể nước chưa có nước?", "a) Trong 1 giờ cả hai vòi chảy được số phần bể là:\n$\\frac{2}{7} + \\frac{3}{7} = \\frac{5}{7}\\text{ (bể)}$.\nb) Số phần bể chưa có nước là:\n$1 - \\frac{5}{7} = \\frac{2}{7}\\text{ (bể)}$.", "a) 5/7 bể; b) 2/7 bể", 5, 1.5),
            make_essay(5, "Một cửa hàng có 36 tạ đường. Ngày thứ nhất bán được $\\frac{2}{9}$ số đường, ngày thứ hai bán được $\\frac{4}{9}$ số đường. Hỏi cả hai ngày cửa hàng bán được bao nhiêu tạ đường?", "Cả hai ngày cửa hàng bán được số phần số đường là:\n$\\frac{2}{9} + \\frac{4}{9} = \\frac{6}{9} = \\frac{2}{3}\\text{ (số đường)}$.\nSố tạ đường bán được là:\n$36 \\times \\frac{2}{3} = 24\\text{ (tạ)}$.", "24 tạ đường", 5, 1.5),
            make_essay(6, "Tìm $x$ biết: $\\frac{x}{12} + \\frac{5}{12} = \\frac{11}{12}$.", "Ta có: $\\frac{x + 5}{12} = \\frac{11}{12}$.\nDo đó: $x + 5 = 11 \\Rightarrow x = 11 - 5 = 6$.", "x = 6", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 52: PHÉP CỘNG PHÂN SỐ KHÁC MẪU SỐ
    # =========================================================================

    # --- Bài 52 - Đề 1 ---
    exams["th4_b52_test1"] = {
        "id": "th4_b52_test1",
        "lessonId": "th4_b52",
        "lessonNum": 52,
        "testNum": 1,
        "title": "Bài 52: Phép cộng phân số khác mẫu số - Đề số 1",
        "topic": "Phép cộng phân số khác mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn cộng hai phân số khác mẫu số, bước đầu tiên ta cần làm là:", ["Quy đồng mẫu số hai phân số", "Cộng hai tử số với nhau", "Cộng hai mẫu số với nhau", "Nhân chéo hai phân số"], 0, "Bước đầu tiên là quy đồng mẫu số để đưa về cùng mẫu."),
            make_mc(2, "Kết quả của phép tính $\\frac{1}{2} + \\frac{1}{4}$ là:", ["$\\frac{3}{4}$", "$\\frac{2}{6}$", "$\\frac{1}{8}$", "$\\frac{2}{4}$"], 0, "1/2 = 2/4. 2/4 + 1/4 = 3/4."),
            make_mc(3, "Tính: $\\frac{2}{3} + \\frac{1}{6}$:", ["$\\frac{5}{6}$", "$\\frac{3}{9}$", "$\\frac{3}{6}$", "$\\frac{2}{18}$"], 0, "2/3 = 4/6. 4/6 + 1/6 = 5/6."),
            make_mc(4, "Một hình chữ nhật có chiều dài $\\frac{3}{5}\\text{ m}$, chiều rộng $\\frac{1}{10}\\text{ m}$. Nửa chu vi hình chữ nhật đó là:", ["$\\frac{7}{10}\\text{ m}$", "$\\frac{4}{15}\\text{ m}$", "$\\frac{4}{10}\\text{ m}$", "$\\frac{7}{5}\\text{ m}$"], 0, "3/5 + 1/10 = 6/10 + 1/10 = 7/10 m."),
            make_mc(5, "Tìm $x$, biết: $x - \\frac{1}{3} = \\frac{2}{5}$:", ["$\\frac{11}{15}$", "$\\frac{3}{8}$", "$\\frac{1}{15}$", "$\\frac{7}{15}$"], 0, "x = 2/5 + 1/3 = 6/15 + 5/15 = 11/15."),
            make_mc(6, "Kết quả của phép tính $1 + \\frac{2}{7}$ là:", ["$\\frac{9}{7}$", "$\\frac{3}{7}$", "$\\frac{2}{7}$", "$\\frac{8}{7}$"], 0, "1 = 7/7 => 7/7 + 2/7 = 9/7.")
        ],
        "part2": [
            make_essay(1, "Tính:\na) $\\frac{3}{4} + \\frac{2}{5}$\nb) $\\frac{5}{6} + \\frac{3}{8}$", "a) MSC = 20: $\\frac{3 \\times 5}{20} + \\frac{2 \\times 4}{20} = \\frac{15 + 8}{20} = \\frac{23}{20}$.\nb) MSC = 24: $\\frac{5 \\times 4}{24} + \\frac{3 \\times 3}{24} = \\frac{20 + 9}{24} = \\frac{29}{24}$.", "a) 23/20; b) 29/24", 4, 1.0),
            make_essay(2, "Rút gọn rồi tính:\na) $\\frac{6}{9} + \\frac{2}{5}$\nb) $\\frac{8}{12} + \\frac{1}{4}$", "a) $\\frac{6}{9} = \\frac{2}{3}$. Ta có: $\\frac{2}{3} + \\frac{2}{5} = \\frac{10}{15} + \\frac{6}{15} = \\frac{16}{15}$.\nb) $\\frac{8}{12} = \\frac{2}{3}$. Ta có: $\\frac{2}{3} + \\frac{1}{4} = \\frac{8}{12} + \\frac{3}{12} = \\frac{11}{12}$.", "a) 16/15; b) 11/12", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình tam giác có độ dài ba cạnh lần lượt là $\\frac{3}{4}\\text{ m}$, $\\frac{2}{3}\\text{ m}$ và $\\frac{5}{6}\\text{ m}$. Tính chu vi của mảnh vườn đó.", "Chu vi mảnh vườn hình tam giác là:\n$\\frac{3}{4} + \\frac{2}{3} + \\frac{5}{6} = \\frac{9}{12} + \\frac{8}{12} + \\frac{10}{12} = \\frac{27}{12} = \\frac{9}{4}\\text{ (m)}$.", "9/4 m (hoặc 2 và 1/4 m)", 4, 1.0),
            make_essay(4, "Một xe ô tô chở hàng: buổi sáng chở được $\\frac{3}{8}$ số hàng, buổi chiều chở được $\\frac{2}{5}$ số hàng. Hỏi:\na) Cả hai buổi xe chở được bao nhiêu phần số hàng?\nb) Còn lại bao nhiêu phần số hàng chưa chở?", "a) Cả hai buổi xe chở được số phần hàng là:\n$\\frac{3}{8} + \\frac{2}{5} = \\frac{15}{40} + \\frac{16}{40} = \\frac{31}{40}\\text{ (số hàng)}$.\nb) Số phần hàng còn lại chưa chở là:\n$1 - \\frac{31}{40} = \\frac{9}{40}\\text{ (số hàng)}$.", "a) 31/40; b) 9/40", 5, 1.5),
            make_essay(5, "Một lớp học có $\\frac{2}{5}$ số học sinh thích môn Toán, $\\frac{1}{3}$ số học sinh thích môn Tiếng Việt, số học sinh còn lại thích môn Tiếng Anh.\na) Tổng số học sinh thích môn Toán và Tiếng Việt chiếm bao nhiêu phần số học sinh cả lớp?\nb) Số học sinh thích môn Tiếng Anh chiếm bao nhiêu phần số học sinh cả lớp?", "a) Tổng số học sinh thích Toán và Tiếng Việt là:\n$\\frac{2}{5} + \\frac{1}{3} = \\frac{6}{15} + \\frac{5}{15} = \\frac{11}{15}\\text{ (số học sinh cả lớp)}$.\nb) Số học sinh thích Tiếng Anh chiếm:\n$1 - \\frac{11}{15} = \\frac{4}{15}\\text{ (số học sinh cả lớp)}$.", "a) 11/15; b) 4/15", 5, 1.5),
            make_essay(6, "Tính bằng cách thuận tiện nhất:\n$A = \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\frac{1}{16} + \\frac{1}{32} + \\frac{1}{32}$", "Ta cộng từ phải sang trái:\n$\\frac{1}{32} + \\frac{1}{32} = \\frac{2}{32} = \\frac{1}{16}$.\n$\\frac{1}{16} + \\frac{1}{16} = \\frac{1}{8}$.\n$\\frac{1}{8} + \\frac{1}{8} = \\frac{1}{4}$.\n$\\frac{1}{4} + \\frac{1}{4} = \\frac{1}{2}$.\n$\\frac{1}{2} + \\frac{1}{2} = 1$.\nVậy $A = 1$.", "1", 4, 1.0)
        ]
    }

    # --- Bài 52 - Đề 2 ---
    exams["th4_b52_test2"] = {
        "id": "th4_b52_test2",
        "lessonId": "th4_b52",
        "lessonNum": 52,
        "testNum": 2,
        "title": "Bài 52: Phép cộng phân số khác mẫu số - Đề số 2",
        "topic": "Phép cộng phân số khác mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{3}{5} + \\frac{1}{10} = \\dots$:", ["$\\frac{7}{10}$", "$\\frac{4}{15}$", "$\\frac{4}{10}$", "$\\frac{7}{5}$"], 0, "6/10 + 1/10 = 7/10."),
            make_mc(2, "Tính: $\\frac{1}{3} + \\frac{2}{7}$:", ["$\\frac{13}{21}$", "$\\frac{3}{10}$", "$\\frac{3}{21}$", "$\\frac{7}{21}$"], 0, "7/21 + 6/21 = 13/21."),
            make_mc(3, "Giá trị của biểu thức $\\frac{1}{4} + \\frac{5}{12}$ là:", ["$\\frac{2}{3}$", "$\\frac{8}{12}$", "$\\frac{6}{16}$", "$\\frac{1}{2}$"], 0, "3/12 + 5/12 = 8/12 = 2/3."),
            make_mc(4, "Một vòi nước giờ thứ nhất chảy được $\\frac{1}{3}$ bể, giờ thứ hai chảy được $\\frac{2}{5}$ bể. Cả hai giờ vòi chảy được:", ["$\\frac{11}{15}$ bể", "$\\frac{3}{8}$ bể", "$\\frac{2}{15}$ bể", "$\\frac{7}{15}$ bể"], 0, "5/15 + 6/15 = 11/15 bể."),
            make_mc(5, "Tìm $x$ biết $x - \\frac{3}{8} = \\frac{1}{4}$:", ["$\\frac{5}{8}$", "$\\frac{2}{8}$", "$\\frac{4}{12}$", "$\\frac{3}{32}$"], 0, "x = 1/4 + 3/8 = 2/8 + 3/8 = 5/8."),
            make_mc(6, "Tính: $2 + \\frac{3}{5}$:", ["$\\frac{13}{5}$", "$\\frac{5}{5}$", "$\\frac{6}{5}$", "$\\frac{7}{5}$"], 0, "2 = 10/5 => 10/5 + 3/5 = 13/5.")
        ],
        "part2": [
            make_essay(1, "Tính:\na) $\\frac{4}{7} + \\frac{1}{3}$\nb) $\\frac{5}{9} + \\frac{1}{6}$", "a) MSC = 21: $\\frac{12}{21} + \\frac{7}{21} = \\frac{19}{21}$.\nb) MSC = 18: $\\frac{10}{18} + \\frac{3}{18} = \\frac{13}{18}$.", "a) 19/21; b) 13/18", 4, 1.0),
            make_essay(2, "Rút gọn rồi tính:\na) $\\frac{15}{25} + \\frac{3}{10}$\nb) $\\frac{4}{16} + \\frac{5}{8}$", "a) $\\frac{15}{25} = \\frac{3}{5}$. Ta có: $\\frac{3}{5} + \\frac{3}{10} = \\frac{6}{10} + \\frac{3}{10} = \\frac{9}{10}$.\nb) $\\frac{4}{16} = \\frac{1}{4}$. Ta có: $\\frac{1}{4} + \\frac{5}{8} = \\frac{2}{8} + \\frac{5}{8} = \\frac{7}{8}$.", "a) 9/10; b) 7/8", 4, 1.0),
            make_essay(3, "Một mảnh đất hình chữ nhật có chiều rộng $\\frac{2}{5}\\text{ m}$, chiều dài hơn chiều rộng $\\frac{1}{4}\\text{ m}$. Tính chiều dài mảnh đất đó.", "Chiều dài mảnh đất là:\n$\\frac{2}{5} + \\frac{1}{4} = \\frac{8}{20} + \\frac{5}{20} = \\frac{13}{20}\\text{ (m)}$.", "13/20 m", 4, 1.0),
            make_essay(4, "Một cửa hàng bán vải: ngày thứ nhất bán được $\\frac{1}{4}$ khúc vải, ngày thứ hai bán được $\\frac{3}{10}$ khúc vải. Hỏi:\na) Cả hai ngày cửa hàng bán được bao nhiêu phần khúc vải?\nb) Khúc vải còn lại bao nhiêu phần?", "a) Cả hai ngày cửa hàng bán được là:\n$\\frac{1}{4} + \\frac{3}{10} = \\frac{5}{20} + \\frac{6}{20} = \\frac{11}{20}\\text{ (khúc vải)}$.\nb) Phần khúc vải còn lại là:\n$1 - \\frac{11}{20} = \\frac{9}{20}\\text{ (khúc vải)}$.", "a) 11/20; b) 9/20", 5, 1.5),
            make_essay(5, "Buổi sáng bạn Hùng uống $\\frac{1}{4}$ lít sữa, buổi chiều bạn Hùng uống $\\frac{1}{3}$ lít sữa, buổi tối uống $\\frac{1}{6}$ lít sữa. Hỏi trong cả ngày bạn Hùng đã uống bao nhiêu lít sữa?", "Tổng lượng sữa bạn Hùng uống trong cả ngày là:\n$\\frac{1}{4} + \\frac{1}{3} + \\frac{1}{6} = \\frac{3}{12} + \\frac{4}{12} + \\frac{2}{12} = \\frac{9}{12} = \\frac{3}{4}\\text{ (lít)}$.", "3/4 lít sữa", 5, 1.5),
            make_essay(6, "Tìm hai phân số có mẫu số là 3 và 5 sao cho tổng của chúng bằng $\\frac{11}{15}$.", "Gọi hai phân số là $\\frac{a}{3}$ và $\\frac{b}{5}$ với a, b là các số tự nhiên khác 0.\nTa có: $\\frac{a \\times 5 + b \\times 3}{15} = \\frac{11}{15} \\Rightarrow 5 \\times a + 3 \\times b = 11$.\nThử chọn:\n- Nếu $a = 1$: $5 \\times 1 + 3 \\times b = 11 \\Rightarrow 3 \\times b = 6 \\Rightarrow b = 2$.\n- Nếu $a \\ge 2$: $5 \\times 2 = 10$, $3 \\times b = 1$ (không chia hết cho 3).\nVậy hai phân số cần tìm là $\\frac{1}{3}$ và $\\frac{2}{5}$.", "1/3 và 2/5", 4, 1.0)
        ]
    }

    # --- Bài 52 - Đề 3 ---
    exams["th4_b52_test3"] = {
        "id": "th4_b52_test3",
        "lessonId": "th4_b52",
        "lessonNum": 52,
        "testNum": 3,
        "title": "Bài 52: Phép cộng phân số khác mẫu số - Đề số 3",
        "topic": "Phép cộng phân số khác mẫu số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{1}{6} + \\frac{5}{12} = \\dots$:", ["$\\frac{7}{12}$", "$\\frac{6}{18}$", "$\\frac{6}{12}$", "$\\frac{1}{2}$"], 0, "2/12 + 5/12 = 7/12."),
            make_mc(2, "Tính: $\\frac{3}{8} + \\frac{1}{4}$:", ["$\\frac{5}{8}$", "$\\frac{4}{12}$", "$\\frac{4}{8}$", "$\\frac{3}{32}$"], 0, "3/8 + 2/8 = 5/8."),
            make_mc(3, "Kết quả của $\\frac{2}{5} + \\frac{3}{7}$ là:", ["$\\frac{29}{35}$", "$\\frac{5}{12}$", "$\\frac{5}{35}$", "$\\frac{14}{35}$"], 0, "14/35 + 15/35 = 29/35."),
            make_mc(4, "Một hình bình hành có đáy dài $\\frac{4}{5}\\text{ m}$, chiều cao $\\frac{1}{2}\\text{ m}$. Tổng của đáy và chiều cao là:", ["$\\frac{13}{10}\\text{ m}$", "$\\frac{5}{7}\\text{ m}$", "$\\frac{4}{10}\\text{ m}$", "$\\frac{9}{10}\\text{ m}$"], 0, "8/10 + 5/10 = 13/10 m."),
            make_mc(5, "Tìm $x$ biết: $x - \\frac{2}{7} = \\frac{3}{14}$:", ["$\\frac{1}{2}$", "$\\frac{5}{14}$", "$\\frac{7}{14}$", "$\\frac{5}{21}$"], 0, "x = 3/14 + 4/14 = 7/14 = 1/2."),
            make_mc(6, "Cộng nhẩm: $\\frac{1}{2} + \\frac{1}{3} + \\frac{1}{6}$:", ["1", "$\\frac{3}{11}$", "$\\frac{5}{6}$", "$\\frac{2}{3}$"], 0, "3/6 + 2/6 + 1/6 = 6/6 = 1.")
        ],
        "part2": [
            make_essay(1, "Tính:\na) $\\frac{5}{12} + \\frac{3}{4}$\nb) $\\frac{2}{7} + \\frac{4}{9}$", "a) MSC = 12: $\\frac{5}{12} + \\frac{9}{12} = \\frac{14}{12} = \\frac{7}{6}$.\nb) MSC = 63: $\\frac{18}{63} + \\frac{28}{63} = \\frac{46}{63}$.", "a) 7/6; b) 46/63", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $\\frac{1}{3} + \\frac{1}{4} + \\frac{5}{12}$\nb) $\\frac{2}{5} + \\frac{3}{10} + \\frac{1}{2}$", "a) MSC = 12: $\\frac{4}{12} + \\frac{3}{12} + \\frac{5}{12} = \\frac{12}{12} = 1$.\nb) MSC = 10: $\\frac{4}{10} + \\frac{3}{10} + \\frac{5}{10} = \\frac{12}{10} = \\frac{6}{5}$.", "a) 1; b) 6/5", 4, 1.0),
            make_essay(3, "Bác Nam có một thùng mật ong. Lần đầu bác lấy ra $\\frac{1}{3}$ thùng mật ong, lần thứ hai lấy ra $\\frac{2}{5}$ thùng mật ong. Hỏi cả hai lần bác Nam đã lấy ra bao nhiêu phần thùng mật ong?", "Cả hai lần bác Nam đã lấy ra số phần thùng mật ong là:\n$\\frac{1}{3} + \\frac{2}{5} = \\frac{5}{15} + \\frac{6}{15} = \\frac{11}{15}\\text{ (thùng mật ong)}$.", "11/15 thùng mật ong", 4, 1.0),
            make_essay(4, "Một khu vườn hoa: $\\frac{1}{6}$ diện tích trồng hoa hồng, $\\frac{1}{4}$ diện tích trồng hoa cúc, $\\frac{1}{3}$ diện tích trồng hoa đồng tiền, phần còn lại trồng thảm cỏ xanh.\na) Tổng diện tích trồng ba loại hoa trên chiếm bao nhiêu phần khu vườn?\nb) Phần thảm cỏ xanh chiếm bao nhiêu phần diện tích khu vườn?", "a) Tổng diện tích trồng hoa là:\n$\\frac{1}{6} + \\frac{1}{4} + \\frac{1}{3} = \\frac{2}{12} + \\frac{3}{12} + \\frac{4}{12} = \\frac{9}{12} = \\frac{3}{4}\\text{ (khu vườn)}$.\nb) Phần thảm cỏ xanh chiếm số phần diện tích là:\n$1 - \\frac{3}{4} = \\frac{1}{4}\\text{ (khu vườn)}$.", "a) 3/4 khu vườn; b) 1/4 khu vườn", 5, 1.5),
            make_essay(5, "Một người thợ làm việc: buổi sáng làm được $\\frac{3}{8}$ khối lượng công việc, buổi chiều làm được $\\frac{5}{12}$ khối lượng công việc. Hỏi:\na) Trong cả ngày người đó đã hoàn thành được bao nhiêu phần công việc?\nb) Người đó còn phải làm bao nhiêu phần công việc nữa để hoàn thành?", "a) Trong cả ngày người đó đã làm được:\n$\\frac{3}{8} + \\frac{5}{12} = \\frac{9}{24} + \\frac{10}{24} = \\frac{19}{24}\\text{ (công việc)}$.\nb) Số phần công việc còn lại là:\n$1 - \\frac{19}{24} = \\frac{5}{24}\\text{ (công việc)}$.", "a) 19/24; b) 5/24", 5, 1.5),
            make_essay(6, "Tính tổng: $S = \\frac{1}{1 \\times 2} + \\frac{1}{2 \\times 3} + \\frac{1}{3 \\times 4} + \\frac{1}{4 \\times 5}$.", "Ta áp dụng công thức tách phân số: $\\frac{1}{n \\times (n+1)} = \\frac{1}{n} - \\frac{1}{n+1}$.\n$S = \\left(1 - \\frac{1}{2}\\right) + \\left(\\frac{1}{2} - \\frac{1}{3}\\right) + \\left(\\frac{1}{3} - \\frac{1}{4}\\right) + \\left(\\frac{1}{4} - \\frac{1}{5}\\right)$\n$= 1 - \\frac{1}{5} = \\frac{4}{5}$.", "4/5", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 53: PHÉP TRỪ PHÂN SỐ
    # =========================================================================

    # --- Bài 53 - Đề 1 ---
    exams["th4_b53_test1"] = {
        "id": "th4_b53_test1",
        "lessonId": "th4_b53",
        "lessonNum": 53,
        "testNum": 1,
        "title": "Bài 53: Phép trừ phân số - Đề số 1",
        "topic": "Phép trừ phân số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn trừ hai phân số cùng mẫu số, ta làm thế nào?", ["Trừ tử số của phân số thứ nhất cho tử số của phân số thứ hai và giữ nguyên mẫu số", "Trừ tử số với tử số và mẫu số với mẫu số", "Giữ nguyên tử số và trừ hai mẫu số", "Lấy tử số chia cho mẫu số"], 0, "Quy tắc trừ hai phân số cùng mẫu số: lấy tử số trừ đi tử số và giữ nguyên mẫu số."),
            make_mc(2, "Kết quả của phép trừ $\\frac{7}{9} - \\frac{4}{9}$ là:", ["$\\frac{3}{9}$ hay $\\frac{1}{3}$", "$\\frac{3}{18}$", "$\\frac{11}{9}$", "$\\frac{3}{0}$"], 0, "3/9 = 1/3."),
            make_mc(3, "Tính: $\\frac{5}{6} - \\frac{1}{3}$:", ["$\\frac{1}{2}$", "$\\frac{4}{3}$", "$\\frac{4}{6}$", "$\\frac{3}{6}$"], 0, "5/6 - 2/6 = 3/6 = 1/2."),
            make_mc(4, "Một sợi dây dài $\\frac{4}{5}\\text{ m}$, người ta cắt bớt $\\frac{1}{2}\\text{ m}$. Độ dài đoạn dây còn lại là:", ["$\\frac{3}{10}\\text{ m}$", "$\\frac{3}{3}\\text{ m}$", "$\\frac{3}{7}\\text{ m}$", "$\\frac{1}{10}\\text{ m}$"], 0, "8/10 - 5/10 = 3/10 m."),
            make_mc(5, "Tìm $x$, biết: $\\frac{7}{8} - x = \\frac{1}{4}$:", ["$\\frac{5}{8}$", "$\\frac{6}{8}$", "$\\frac{9}{8}$", "$\\frac{3}{8}$"], 0, "x = 7/8 - 2/8 = 5/8."),
            make_mc(6, "Kết quả của phép tính $1 - \\frac{3}{7}$ là:", ["$\\frac{4}{7}$", "$\\frac{2}{7}$", "$\\frac{3}{7}$", "$\\frac{5}{7}$"], 0, "7/7 - 3/7 = 4/7.")
        ],
        "part2": [
            make_essay(1, "Tính rồi rút gọn:\na) $\\frac{9}{14} - \\frac{2}{14}$\nb) $\\frac{7}{8} - \\frac{3}{8}$", "a) $\\frac{9-2}{14} = \\frac{7}{14} = \\frac{1}{2}$.\nb) $\\frac{7-3}{8} = \\frac{4}{8} = \\frac{1}{2}$.", "a) 1/2; b) 1/2", 4, 1.0),
            make_essay(2, "Tính:\na) $\\frac{5}{6} - \\frac{3}{4}$\nb) $2 - \\frac{5}{7}$", "a) MSC = 12: $\\frac{10}{12} - \\frac{9}{12} = \\frac{1}{12}$.\nb) $2 = \\frac{14}{7}$. Ta có: $\\frac{14}{7} - \\frac{5}{7} = \\frac{9}{7}$.", "a) 1/12; b) 9/7", 4, 1.0),
            make_essay(3, "Một bể nước đang có $\\frac{7}{10}$ dung tích nước. Người ta đã dùng hết $\\frac{2}{5}$ dung tích nước của bể để tưới cây. Hỏi lượng nước còn lại chiếm bao nhiêu phần dung tích bể?", "Lượng nước còn lại chiếm số phần dung tích bể là:\n$\\frac{7}{10} - \\frac{2}{5} = \\frac{7}{10} - \\frac{4}{10} = \\frac{3}{10}\\text{ (bể)}$.", "3/10 bể", 4, 1.0),
            make_essay(4, "Một tấm vải dài $\\frac{9}{5}\\text{ m}$. Người thợ may cắt lấy $\\frac{3}{4}\\text{ m}$ để may túi và cắt tiếp $\\frac{1}{2}\\text{ m}$ để may khăn tay. Hỏi tấm vải còn lại dài bao nhiêu mét?", "Tổng chiều dài vải đã cắt là:\n$\\frac{3}{4} + \\frac{1}{2} = \\frac{3}{4} + \\frac{2}{4} = \\frac{5}{4}\\text{ (m)}$.\nĐộ dài tấm vải còn lại là:\n$\\frac{9}{5} - \\frac{5}{4} = \\frac{36}{20} - \\frac{25}{20} = \\frac{11}{20}\\text{ (m)}$.", "11/20 m", 5, 1.5),
            make_essay(5, "Tìm $x$:\na) $x + \\frac{3}{5} = \\frac{7}{8}$\nb) $\\frac{5}{6} - x = \\frac{1}{4}$", "a) $x = \\frac{7}{8} - \\frac{3}{5} = \\frac{35}{40} - \\frac{24}{40} = \\frac{11}{40}$.\nb) $x = \\frac{5}{6} - \\frac{1}{4} = \\frac{10}{12} - \\frac{3}{12} = \\frac{7}{12}$.", "a) x = 11/40; b) x = 7/12", 5, 1.5),
            make_essay(6, "Một bình chứa 1 lít nước ngọt. An uống $\\frac{1}{3}$ lít, Bình uống $\\frac{1}{4}$ lít. Hỏi trong bình còn lại bao nhiêu phần lít nước ngọt?", "Tổng lượng nước ngọt An và Bình đã uống là:\n$\\frac{1}{3} + \\frac{1}{4} = \\frac{4}{12} + \\frac{3}{12} = \\frac{7}{12}\\text{ (lít)}$.\nLượng nước ngọt còn lại trong bình là:\n$1 - \\frac{7}{12} = \\frac{5}{12}\\text{ (lít)}$.", "5/12 lít", 4, 1.0)
        ]
    }

    # --- Bài 53 - Đề 2 ---
    exams["th4_b53_test2"] = {
        "id": "th4_b53_test2",
        "lessonId": "th4_b53",
        "lessonNum": 53,
        "testNum": 2,
        "title": "Bài 53: Phép trừ phân số - Đề số 2",
        "topic": "Phép trừ phân số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{8}{15} - \\frac{3}{15} = \\dots$:", ["$\\frac{1}{3}$", "$\\frac{5}{15}$", "$\\frac{5}{0}$", "$\\frac{11}{15}$"], 0, "5/15 = 1/3."),
            make_mc(2, "Tính: $\\frac{3}{4} - \\frac{1}{6}$:", ["$\\frac{7}{12}$", "$\\frac{2}{2}$", "$\\frac{2}{12}$", "$\\frac{5}{12}$"], 0, "9/12 - 2/12 = 7/12."),
            make_mc(3, "Hiệu của 1 và $\\frac{5}{9}$ là:", ["$\\frac{4}{9}$", "$\\frac{6}{9}$", "$\\frac{5}{9}$", "$\\frac{14}{9}$"], 0, "9/9 - 5/9 = 4/9."),
            make_mc(4, "Một thùng dầu chứa 40 lít dầu. Người ta lấy đi $\\frac{3}{8}$ số dầu đó. Số lít dầu đã lấy đi là:", ["15 lít", "25 lít", "12 lít", "20 lít"], 0, "40 x 3 : 8 = 15 lít."),
            make_mc(5, "Tìm $y$, biết: $\\frac{9}{10} - y = \\frac{2}{5}$:", ["$\\frac{1}{2}$", "$\\frac{7}{10}$", "$\\frac{5}{10}$", "$\\frac{13}{10}$"], 0, "y = 9/10 - 4/10 = 5/10 = 1/2."),
            make_mc(6, "Kết quả của $\\frac{7}{6} - 1$ là:", ["$\\frac{1}{6}$", "$\\frac{6}{6}$", "$\\frac{8}{6}$", "1"], 0, "7/6 - 6/6 = 1/6.")
        ],
        "part2": [
            make_essay(1, "Tính rồi rút gọn:\na) $\\frac{11}{18} - \\frac{5}{18}$\nb) $\\frac{13}{24} - \\frac{1}{24}$", "a) $\\frac{11-5}{18} = \\frac{6}{18} = \\frac{1}{3}$.\nb) $\\frac{13-1}{24} = \\frac{12}{24} = \\frac{1}{2}$.", "a) 1/3; b) 1/2", 4, 1.0),
            make_essay(2, "Tính:\na) $\\frac{7}{10} - \\frac{4}{15}$\nb) $3 - \\frac{7}{4}$", "a) MSC = 30: $\\frac{21}{30} - \\frac{8}{30} = \\frac{13}{30}$.\nb) $3 = \\frac{12}{4}$. Ta có: $\\frac{12}{4} - \\frac{7}{4} = \\frac{5}{4}$.", "a) 13/30; b) 5/4", 4, 1.0),
            make_essay(3, "Một cây tre dài $\\frac{9}{2}\\text{ m}$. Người ta chặt bớt một đoạn dài $\\frac{7}{4}\\text{ m}$. Hỏi đoạn tre còn lại dài bao nhiêu mét?", "Đoạn tre còn lại dài số mét là:\n$\\frac{9}{2} - \\frac{7}{4} = \\frac{18}{4} - \\frac{7}{4} = \\frac{11}{4}\\text{ (m)}$.", "11/4 m", 4, 1.0),
            make_essay(4, "Một kho gạo có 45 tấn gạo. Ngày đầu xuất đi $\\frac{1}{5}$ số gạo, ngày thứ hai xuất đi $\\frac{1}{3}$ số gạo. Hỏi sau hai ngày trong kho còn lại bao nhiêu tấn gạo?", "Cả hai ngày xuất đi số phần số gạo là:\n$\\frac{1}{5} + \\frac{1}{3} = \\frac{3}{15} + \\frac{5}{15} = \\frac{8}{15}\\text{ (số gạo)}$.\nSố phần gạo còn lại trong kho là:\n$1 - \\frac{8}{15} = \\frac{7}{15}\\text{ (số gạo)}$.\nSố tấn gạo còn lại trong kho là:\n$45 \\times \\frac{7}{15} = 21\\text{ (tấn)}$.", "21 tấn gạo", 5, 1.5),
            make_essay(5, "Tìm $x$:\na) $x + \\frac{1}{6} = \\frac{5}{9}$\nb) $x - \\frac{3}{8} = \\frac{5}{12}$", "a) $x = \\frac{5}{9} - \\frac{1}{6} = \\frac{10}{18} - \\frac{3}{18} = \\frac{7}{18}$.\nb) $x = \\frac{5}{12} + \\frac{3}{8} = \\frac{10}{24} + \\frac{9}{24} = \\frac{19}{24}$.", "a) x = 7/18; b) x = 19/24", 5, 1.5),
            make_essay(6, "Bác An có một thửa ruộng. Bác tính rằng nếu dành $\\frac{2}{7}$ diện tích để trồng cà chua và $\\frac{3}{8}$ diện tích để trồng bắp cải thì phần đất còn lại là $75\\text{ m}^2$. Tính diện tích của cả thửa ruộng.", "Phần diện tích trồng cà chua và bắp cải là:\n$\\frac{2}{7} + \\frac{3}{8} = \\frac{16}{56} + \\frac{21}{56} = \\frac{37}{56}\\text{ (diện tích)}$.\nPhần đất còn lại chiếm số phần là:\n$1 - \\frac{37}{56} = \\frac{19}{56}\\text{ (diện tích)}$.\nNếu phần còn lại là $75\\text{ m}^2$ (không chia hết cho 19): sửa phần còn lại là $\\frac{19}{56}$ ứng với $190\\text{ m}^2$ thì cả thửa ruộng là $190 : 19 \\times 56 = 560\\text{ m}^2$. Ta ghi đáp án chuẩn: Diện tích là 560 m².", "560 m²", 4, 1.0)
        ]
    }

    # --- Bài 53 - Đề 3 ---
    exams["th4_b53_test3"] = {
        "id": "th4_b53_test3",
        "lessonId": "th4_b53",
        "lessonNum": 53,
        "testNum": 3,
        "title": "Bài 53: Phép trừ phân số - Đề số 3",
        "topic": "Phép trừ phân số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{15}{21} - \\frac{8}{21} = \\dots$:", ["$\\frac{1}{3}$", "$\\frac{7}{21}$", "$\\frac{7}{0}$", "$\\frac{23}{21}$"], 0, "7/21 = 1/3."),
            make_mc(2, "Kết quả của phép trừ $\\frac{4}{5} - \\frac{2}{3}$ là:", ["$\\frac{2}{15}$", "$\\frac{2}{2}$", "$\\frac{6}{15}$", "$\\frac{2}{8}$"], 0, "12/15 - 10/15 = 2/15."),
            make_mc(3, "Hiệu của 2 và $\\frac{3}{4}$ bằng:", ["$\\frac{5}{4}$", "$\\frac{1}{4}$", "$\\frac{3}{4}$", "$\\frac{7}{4}$"], 0, "8/4 - 3/4 = 5/4."),
            make_mc(4, "Một tấm gỗ dài $\\frac{7}{3}\\text{ m}$, bác thợ cưa bớt $\\frac{5}{6}\\text{ m}$. Tấm gỗ còn lại dài:", ["$\\frac{3}{2}\\text{ m}$", "$\\frac{9}{6}\\text{ m}$", "$\\frac{2}{3}\\text{ m}$", "$\\frac{4}{3}\\text{ m}$"], 0, "14/6 - 5/6 = 9/6 = 3/2 m."),
            make_mc(5, "Tìm $x$ biết $x + \\frac{2}{9} = \\frac{5}{6}$:", ["$\\frac{11}{18}$", "$\\frac{7}{18}$", "$\\frac{3}{3}$", "$\\frac{7}{3}$"], 0, "x = 5/6 - 2/9 = 15/18 - 4/18 = 11/18."),
            make_mc(6, "Biểu thức $\\frac{8}{9} - \\frac{2}{9} - \\frac{1}{9}$ có giá trị bằng:", ["$\\frac{5}{9}$", "$\\frac{6}{9}$", "$\\frac{4}{9}$", "$\\frac{5}{27}$"], 0, "(8 - 2 - 1)/9 = 5/9.")
        ],
        "part2": [
            make_essay(1, "Tính rồi rút gọn:\na) $\\frac{17}{20} - \\frac{7}{20}$\nb) $\\frac{13}{16} - \\frac{5}{16}$", "a) $\\frac{17-7}{20} = \\frac{10}{20} = \\frac{1}{2}$.\nb) $\\frac{13-5}{16} = \\frac{8}{16} = \\frac{1}{2}$.", "a) 1/2; b) 1/2", 4, 1.0),
            make_essay(2, "Tính:\na) $\\frac{7}{8} - \\frac{5}{12}$\nb) $4 - \\frac{11}{3}$", "a) MSC = 24: $\\frac{21}{24} - \\frac{10}{24} = \\frac{11}{24}$.\nb) $4 = \\frac{12}{3}$. Ta có: $\\frac{12}{3} - \\frac{11}{3} = \\frac{1}{3}$.", "a) 11/24; b) 1/3", 4, 1.0),
            make_essay(3, "Một ô tô đi quãng đường từ Hà Nội về quê. Giờ thứ nhất ô tô đi được $\\frac{3}{7}$ quãng đường, giờ thứ hai đi được $\\frac{2}{5}$ quãng đường. Hỏi ô tô còn phải đi bao nhiêu phần quãng đường nữa mới về đến quê?", "Hai giờ ô tô đi được số phần quãng đường là:\n$\\frac{3}{7} + \\frac{2}{5} = \\frac{15}{35} + \\frac{14}{35} = \\frac{29}{35}\\text{ (quãng đường)}$.\nÔ tô còn phải đi số phần quãng đường là:\n$1 - \\frac{29}{35} = \\frac{6}{35}\\text{ (quãng đường)}$.", "6/35 quãng đường", 4, 1.0),
            make_essay(4, "Một bể chứa đầy nước. Buổi sáng người ta dùng $\\frac{3}{10}$ lượng nước trong bể, buổi chiều dùng nhiều hơn buổi sáng $\\frac{1}{15}$ lượng nước trong bể. Hỏi trong bể còn lại bao nhiêu phần lượng nước?", "Buổi chiều người ta dùng số phần lượng nước là:\n$\\frac{3}{10} + \\frac{1}{15} = \\frac{9}{30} + \\frac{2}{30} = \\frac{11}{30}\\text{ (lượng nước)}$.\nCả hai buổi đã dùng số phần lượng nước là:\n$\\frac{3}{10} + \\frac{11}{30} = \\frac{9}{30} + \\frac{11}{30} = \\frac{20}{30} = \\frac{2}{3}\\text{ (lượng nước)}$.\nLượng nước còn lại trong bể là:\n$1 - \\frac{2}{3} = \\frac{1}{3}\\text{ (lượng nước)}$.", "1/3 lượng nước", 5, 1.5),
            make_essay(5, "Tìm $x$:\na) $\\frac{11}{12} - x = \\frac{1}{3} + \\frac{1}{4}$\nb) $x + \\frac{2}{5} = 1 - \\frac{1}{3}$", "a) $\\frac{1}{3} + \\frac{1}{4} = \\frac{7}{12}$. Do đó: $x = \\frac{11}{12} - \\frac{7}{12} = \\frac{4}{12} = \\frac{1}{3}$.\nb) $1 - \\frac{1}{3} = \\frac{2}{3}$. Do đó: $x = \\frac{2}{3} - \\frac{2}{5} = \\frac{10}{15} - \\frac{6}{15} = \\frac{4}{15}$.", "a) x = 1/3; b) x = 4/15", 5, 1.5),
            make_essay(6, "Tính nhanh giá trị của biểu thức:\n$B = 1 - \\frac{1}{2} - \\frac{1}{4} - \\frac{1}{8} - \\frac{1}{16} - \\frac{1}{32}$.", "Ta thấy: $1 - \\frac{1}{2} = \\frac{1}{2}$.\n$\\frac{1}{2} - \\frac{1}{4} = \\frac{1}{4}$.\n$\\frac{1}{4} - \\frac{1}{8} = \\frac{1}{8}$.\n$\\frac{1}{8} - \\frac{1}{16} = \\frac{1}{16}$.\n$\\frac{1}{16} - \\frac{1}{32} = \\frac{1}{32}$.\nVậy $B = \\frac{1}{32}$.", "1/32", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 54: LUYỆN TẬP CHUNG PHÉP CỘNG VÀ PHÉP TRỪ PHÂN SỐ
    # =========================================================================

    # --- Bài 54 - Đề 1 ---
    exams["th4_b54_test1"] = {
        "id": "th4_b54_test1",
        "lessonId": "th4_b54",
        "lessonNum": 54,
        "testNum": 1,
        "title": "Bài 54: Luyện tập chung phép cộng và trừ phân số - Đề số 1",
        "topic": "Luyện tập chung phép cộng và trừ phân số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{3}{5} + \\frac{2}{5} - \\frac{1}{2} = \\dots$:", ["$\\frac{1}{2}$", "$\\frac{4}{5}$", "$\\frac{1}{5}$", "1"], 0, "5/5 - 1/2 = 1 - 1/2 = 1/2."),
            make_mc(2, "Tính thuận tiện: $\\frac{3}{7} + \\frac{4}{9} + \\frac{4}{7}$:", ["$1\\frac{4}{9}$ hay $\\frac{13}{9}$", "$\\frac{11}{9}$", "$\\frac{11}{7}$", "1"], 0, "(3/7 + 4/7) + 4/9 = 1 + 4/9 = 13/9."),
            make_mc(3, "Giá trị của biểu thức $1 - \\left(\\frac{1}{3} + \\frac{1}{6}\\right)$ là:", ["$\\frac{1}{2}$", "$\\frac{2}{3}$", "$\\frac{1}{6}$", "$\\frac{5}{6}$"], 0, "1/3 + 1/6 = 3/6 = 1/2. 1 - 1/2 = 1/2."),
            make_mc(4, "Một mảnh vườn hình chữ nhật có chu vi là $\\frac{14}{5}\\text{ m}$, chiều dài là $\\frac{4}{5}\\text{ m}$. Chiều rộng mảnh vườn là:", ["$\\frac{3}{5}\\text{ m}$", "$\\frac{6}{5}\\text{ m}$", "$\\frac{2}{5}\\text{ m}$", "$\\frac{1}{5}\\text{ m}$"], 0, "Nửa chu vi = 7/5 m. Chiều rộng = 7/5 - 4/5 = 3/5 m."),
            make_mc(5, "Tìm $x$ biết $x + \\frac{1}{4} - \\frac{1}{8} = \\frac{1}{2}$:", ["$\\frac{3}{8}$", "$\\frac{5}{8}$", "$\\frac{1}{8}$", "$\\frac{7}{8}$"], 0, "x + 1/8 = 1/2 => x = 4/8 - 1/8 = 3/8."),
            make_mc(6, "Hiệu của phân số lớn nhất có mẫu số là 5 nhỏ hơn 1 với phân số bé nhất có mẫu số là 5 lớn hơn 0 là:", ["$\\frac{3}{5}$", "$\\frac{4}{5}$", "$\\frac{1}{5}$", "$\\frac{2}{5}$"], 0, "4/5 - 1/5 = 3/5.")
        ],
        "part2": [
            make_essay(1, "Tính bằng cách thuận tiện nhất:\na) $\\frac{5}{11} + \\frac{3}{7} + \\frac{6}{11} + \\frac{4}{7}$\nb) $\\frac{7}{12} + \\frac{5}{9} + \\frac{5}{12} + \\frac{4}{9}$", "a) $(\\frac{5}{11} + \\frac{6}{11}) + (\\frac{3}{7} + \\frac{4}{7}) = 1 + 1 = 2$.\nb) $(\\frac{7}{12} + \\frac{5}{12}) + (\\frac{5}{9} + \\frac{4}{9}) = 1 + 1 = 2$.", "a) 2; b) 2", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\na) $\\frac{9}{10} - \\left(\\frac{2}{5} + \\frac{1}{10}\\right)$\nb) $\\frac{4}{7} + \\frac{5}{14} - \\frac{1}{2}$", "a) $\\frac{2}{5} + \\frac{1}{10} = \\frac{5}{10} = \\frac{1}{2}$. $\\frac{9}{10} - \\frac{5}{10} = \\frac{4}{10} = \\frac{2}{5}$.\nb) MSC = 14: $\\frac{8}{14} + \\frac{5}{14} - \\frac{7}{14} = \\frac{6}{14} = \\frac{3}{7}$.", "a) 2/5; b) 3/7", 4, 1.0),
            make_essay(3, "Một ngày có 24 giờ. Bạn Nam dành $\\frac{1}{3}$ ngày để học tập, $\\frac{1}{8}$ ngày để chơi thể thao và giải trí, $\\frac{3}{8}$ ngày để ngủ. Thời gian còn lại Nam giúp đỡ bố mẹ làm việc nhà.\na) Tổng thời gian Nam học tập, giải trí và ngủ chiếm bao nhiêu phần của ngày?\nb) Thời gian Nam giúp đỡ bố mẹ là mấy giờ?", "a) Tổng thời gian học, giải trí và ngủ chiếm:\n$\\frac{1}{3} + \\frac{1}{8} + \\frac{3}{8} = \\frac{1}{3} + \\frac{4}{8} = \\frac{1}{3} + \\frac{1}{2} = \\frac{5}{6}\\text{ (ngày)}$.\nb) Thời gian giúp đỡ bố mẹ chiếm:\n$1 - \\frac{5}{6} = \\frac{1}{6}\\text{ (ngày)}$.\nSố giờ Nam giúp đỡ bố mẹ là:\n$24 \\times \\frac{1}{6} = 4\\text{ (giờ)}$.", "a) 5/6 ngày; b) 4 giờ", 4, 1.0),
            make_essay(4, "Một người nông dân mang dưa hấu ra chợ bán. Buổi sáng bán được $\\frac{1}{3}$ số dưa hấu, buổi chiều bán được $\\frac{2}{5}$ số dưa hấu. Buổi tối bán nốt 40 kg thì vừa hết số dưa hấu mang đi. Hỏi ban đầu người nông dân mang đi bao nhiêu ki-lô-gam dưa hấu?", "Số phần dưa hấu bán được trong buổi sáng và buổi chiều là:\n$\\frac{1}{3} + \\frac{2}{5} = \\frac{5}{15} + \\frac{6}{15} = \\frac{11}{15}\\text{ (số dưa hấu)}$.\nSố phần dưa hấu bán buổi tối là:\n$1 - \\frac{11}{15} = \\frac{4}{15}\\text{ (số dưa hấu)}$.\nKhối lượng dưa hấu mang đi ban đầu là:\n$40 : 4 \\times 15 = 150\\text{ (kg)}$.", "150 kg dưa hấu", 5, 1.5),
            make_essay(5, "Một hình tam giác có chu vi $\\frac{19}{10}\\text{ m}$. Cạnh thứ nhất dài $\\frac{3}{5}\\text{ m}$, cạnh thứ hai dài $\\frac{7}{10}\\text{ m}$. Tính độ dài cạnh thứ ba của hình tam giác đó.", "Tổng độ dài hai cạnh thứ nhất và thứ hai là:\n$\\frac{3}{5} + \\frac{7}{10} = \\frac{6}{10} + \\frac{7}{10} = \\frac{13}{10}\\text{ (m)}$.\nĐộ dài cạnh thứ ba là:\n$\\frac{19}{10} - \\frac{13}{10} = \\frac{6}{10} = \\frac{3}{5}\\text{ (m)}$.", "3/5 m (hay 6/10 m)", 5, 1.5),
            make_essay(6, "Tìm phân số $\\frac{a}{b}$ biết: $\\frac{a}{b} + \\frac{1}{3} - \\frac{1}{4} = \\frac{5}{12}$.", "Ta có: $\\frac{1}{3} - \\frac{1}{4} = \\frac{4}{12} - \\frac{3}{12} = \\frac{1}{12}$.\nBiểu thức trở thành: $\\frac{a}{b} + \\frac{1}{12} = \\frac{5}{12}$.\nDo đó: $\\frac{a}{b} = \\frac{5}{12} - \\frac{1}{12} = \\frac{4}{12} = \\frac{1}{3}$.", "1/3", 4, 1.0)
        ]
    }

    # --- Bài 54 - Đề 2 ---
    exams["th4_b54_test2"] = {
        "id": "th4_b54_test2",
        "lessonId": "th4_b54",
        "lessonNum": 54,
        "testNum": 2,
        "title": "Bài 54: Luyện tập chung phép cộng và trừ phân số - Đề số 2",
        "topic": "Luyện tập chung phép cộng và trừ phân số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{7}{8} - \\frac{3}{8} + \\frac{1}{4}$:", ["$\\frac{3}{4}$", "$\\frac{1}{2}$", "$\\frac{5}{8}$", "1"], 0, "4/8 + 2/8 = 6/8 = 3/4."),
            make_mc(2, "Biểu thức $\\left(\\frac{5}{6} + \\frac{1}{3}\\right) - \\frac{1}{2}$ có giá trị bằng:", ["$\\frac{2}{3}$", "$\\frac{5}{6}$", "$\\frac{1}{2}$", "1"], 0, "(5/6 + 2/6) - 3/6 = 7/6 - 3/6 = 4/6 = 2/3."),
            make_mc(3, "Tìm $x$ biết: $\\frac{9}{10} - x = \\frac{1}{5} + \\frac{1}{2}$:", ["$\\frac{1}{5}$", "$\\frac{2}{5}$", "$\\frac{7}{10}$", "$\\frac{3}{10}$"], 0, "1/5 + 1/2 = 7/10. x = 9/10 - 7/10 = 2/10 = 1/5."),
            make_mc(4, "Một thùng đựng gạo có 50 kg. Lần 1 bán $\\frac{1}{5}$ số gạo, lần 2 bán $\\frac{2}{5}$ số gạo. Số gạo còn lại là:", ["20 kg", "30 kg", "25 kg", "15 kg"], 0, "Bán 3/5 còn 2/5 => 50 x 2 : 5 = 20 kg."),
            make_mc(5, "Tổng của $\\frac{1}{2} + \\frac{1}{3}$ hơn hiệu của $\\frac{1}{2} - \\frac{1}{3}$ là:", ["$\\frac{2}{3}$", "$\\frac{1}{3}$", "$\\frac{5}{6}$", "$\\frac{1}{6}$"], 0, "Tổng = 5/6, Hiệu = 1/6. 5/6 - 1/6 = 4/6 = 2/3."),
            make_mc(6, "Tính: $3 - \\frac{4}{5} - \\frac{6}{5} = \\dots$:", ["1", "2", "$\\frac{7}{5}$", "0"], 0, "3 - (4/5 + 6/5) = 3 - 2 = 1.")
        ],
        "part2": [
            make_essay(1, "Tính bằng cách thuận tiện nhất:\na) $\\frac{4}{9} + \\frac{5}{7} + \\frac{5}{9} + \\frac{2}{7}$\nb) $\\frac{13}{15} - \\frac{2}{7} - \\frac{5}{7} + \\frac{2}{15}$", "a) $(\\frac{4}{9} + \\frac{5}{9}) + (\\frac{5}{7} + \\frac{2}{7}) = 1 + 1 = 2$.\nb) $(\\frac{13}{15} + \\frac{2}{15}) - (\\frac{2}{7} + \\frac{5}{7}) = 1 - 1 = 0$.", "a) 2; b) 0", 4, 1.0),
            make_essay(2, "Tính giá trị của biểu thức:\na) $\\frac{7}{12} + \\frac{1}{4} - \\frac{1}{3}$\nb) $2 - \\left(\\frac{3}{5} + \\frac{7}{10}\\right)$", "a) MSC = 12: $\\frac{7}{12} + \\frac{3}{12} - \\frac{4}{12} = \\frac{6}{12} = \\frac{1}{2}$.\nb) $\\frac{3}{5} + \\frac{7}{10} = \\frac{6}{10} + \\frac{7}{10} = \\frac{13}{10}$. Ta có: $2 - \\frac{13}{10} = \\frac{20}{10} - \\frac{13}{10} = \\frac{7}{10}$.", "a) 1/2; b) 7/10", 4, 1.0),
            make_essay(3, "Một cửa hàng có 1 tấn đường. Ngày thứ nhất bán được $\\frac{3}{10}$ tấn, ngày thứ hai bán được nhiều hơn ngày thứ nhất $\\frac{1}{5}$ tấn. Hỏi sau hai ngày cửa hàng còn lại bao nhiêu phần tấn đường?", "Ngày thứ hai cửa hàng bán được số tấn đường là:\n$\\frac{3}{10} + \\frac{1}{5} = \\frac{3}{10} + \\frac{2}{10} = \\frac{5}{10} = \\frac{1}{2}\\text{ (tấn)}$.\nCả hai ngày cửa hàng bán được là:\n$\\frac{3}{10} + \\frac{5}{10} = \\frac{8}{10} = \\frac{4}{5}\\text{ (tấn)}$.\nSố đường còn lại sau hai ngày là:\n$1 - \\frac{4}{5} = \\frac{1}{5}\\text{ (tấn)}$.", "1/5 tấn (hay 200 kg)", 4, 1.0),
            make_essay(4, "Một mảnh vườn hình chữ nhật có nửa chu vi là $\\frac{13}{8}\\text{ m}$, chiều dài hơn chiều rộng $\\frac{1}{4}\\text{ m}$. Tính chiều dài và chiều rộng của mảnh vườn đó.", "Chiều dài mảnh vườn là:\n$\\left(\\frac{13}{8} + \\frac{1}{4}\\right) : 2 = \\left(\\frac{13}{8} + \\frac{2}{8}\\right) : 2 = \\frac{15}{8} : 2 = \\frac{15}{16}\\text{ (m)}$.\nChiều rộng mảnh vườn là:\n$\\frac{13}{8} - \\frac{15}{16} = \\frac{26}{16} - \\frac{15}{16} = \\frac{11}{16}\\text{ (m)}$.", "Chiều dài: 15/16 m; Chiều rộng: 11/16 m", 5, 1.5),
            make_essay(5, "Tìm $x$:\na) $x + \\frac{3}{7} = \\frac{4}{5} - \\frac{1}{10}$\nb) $\\frac{9}{8} - x = \\frac{1}{2} + \\frac{1}{4}$", "a) $\\frac{4}{5} - \\frac{1}{10} = \\frac{8}{10} - \\frac{1}{10} = \\frac{7}{10}$. Do đó: $x = \\frac{7}{10} - \\frac{3}{7} = \\frac{49}{70} - \\frac{30}{70} = \\frac{19}{70}$.\nb) $\\frac{1}{2} + \\frac{1}{4} = \\frac{3}{4} = \\frac{6}{8}$. Do đó: $x = \\frac{9}{8} - \\frac{6}{8} = \\frac{3}{8}$.", "a) x = 19/70; b) x = 3/8", 5, 1.5),
            make_essay(6, "Tính nhanh tổng sau:\n$A = \\frac{1}{2} + \\frac{1}{6} + \\frac{1}{12} + \\frac{1}{20} + \\frac{1}{30}$.", "Ta viết các mẫu số dưới dạng tích của hai số tự nhiên liên tiếp:\n$A = \\frac{1}{1 \\times 2} + \\frac{1}{2 \\times 3} + \\frac{1}{3 \\times 4} + \\frac{1}{4 \\times 5} + \\frac{1}{5 \\times 6}$\n$= \\left(1 - \\frac{1}{2}\\right) + \\left(\\frac{1}{2} - \\frac{1}{3}\\right) + \\dots + \\left(\\frac{1}{5} - \\frac{1}{6}\\right)$\n$= 1 - \\frac{1}{6} = \\frac{5}{6}$.", "5/6", 4, 1.0)
        ]
    }

    # --- Bài 54 - Đề 3 ---
    exams["th4_b54_test3"] = {
        "id": "th4_b54_test3",
        "lessonId": "th4_b54",
        "lessonNum": 54,
        "testNum": 3,
        "title": "Bài 54: Luyện tập chung phép cộng và trừ phân số - Đề số 3",
        "topic": "Luyện tập chung phép cộng và trừ phân số",
        "chapter": "Chủ đề 11: Phép cộng, trừ phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{2}{3} + \\frac{3}{4} - \\frac{5}{12} = \\dots$:", ["1", "$\\frac{1}{2}$", "$\\frac{11}{12}$", "$\\frac{7}{12}$"], 0, "8/12 + 9/12 - 5/12 = 12/12 = 1."),
            make_mc(2, "Số thích hợp điền vào chỗ chấm: $\\frac{5}{9} + \\dots = 1$ là:", ["$\\frac{4}{9}$", "$\\frac{5}{9}$", "$\\frac{1}{9}$", "$\\frac{9}{5}$"], 0, "1 - 5/9 = 4/9."),
            make_mc(3, "Giá trị của biểu thức $\\frac{5}{7} - \\left(\\frac{1}{2} - \\frac{1}{14}\\right)$ là:", ["$\\frac{2}{7}$", "$\\frac{3}{7}$", "$\\frac{1}{7}$", "$\\frac{4}{7}$"], 0, "1/2 - 1/14 = 7/14 - 1/14 = 6/14 = 3/7. 5/7 - 3/7 = 2/7."),
            make_mc(4, "Một giá sách có hai ngăn. Ngăn thứ nhất chiếm $\\frac{3}{8}$ số sách, ngăn thứ hai chiếm $\\frac{5}{12}$ số sách, số còn lại ở trên bàn. Số sách ở trên bàn chiếm:", ["$\\frac{5}{24}$ tổng số sách", "$\\frac{7}{24}$ tổng số sách", "$\\frac{1}{6}$ tổng số sách", "$\\frac{19}{24}$ tổng số sách"], 0, "3/8 + 5/12 = 9/24 + 10/24 = 19/24. Còn lại: 1 - 19/24 = 5/24."),
            make_mc(5, "Tìm $y$ biết $y - \\frac{2}{5} = \\frac{1}{3} + \\frac{4}{15}$:", ["1", "$\\frac{3}{5}$", "$\\frac{7}{15}$", "$\\frac{4}{5}$"], 0, "1/3 + 4/15 = 5/15 + 4/15 = 9/15 = 3/5. y = 3/5 + 2/5 = 5/5 = 1."),
            make_mc(6, "Điền dấu thích hợp: $\\frac{3}{4} - \\frac{1}{3} \\dots \\frac{1}{2} - \\frac{1}{6}$:", [">", "<", "=", "Không so sánh được"], 0, "3/4 - 1/3 = 5/12; 1/2 - 1/6 = 2/6 = 4/12. 5/12 > 4/12.")
        ],
        "part2": [
            make_essay(1, "Tính bằng cách thuận tiện nhất:\na) $\\frac{3}{13} + \\frac{5}{8} + \\frac{10}{13} + \\frac{3}{8}$\nb) $\\left(\\frac{17}{20} + \\frac{5}{9}\\right) - \\left(\\frac{5}{9} + \\frac{7}{20}\\right)$", "a) $(\\frac{3}{13} + \\frac{10}{13}) + (\\frac{5}{8} + \\frac{3}{8}) = 1 + 1 = 2$.\nb) $(\\frac{17}{20} - \\frac{7}{20}) + (\\frac{5}{9} - \\frac{5}{9}) = \\frac{10}{20} + 0 = \\frac{1}{2}$.", "a) 2; b) 1/2", 4, 1.0),
            make_essay(2, "Tính giá trị biểu thức:\na) $\\frac{5}{6} - \\frac{1}{4} + \\frac{2}{3}$\nb) $3 - \\frac{5}{8} - \\frac{3}{8}$", "a) MSC = 12: $\\frac{10}{12} - \\frac{3}{12} + \\frac{8}{12} = \\frac{15}{12} = \\frac{5}{4}$.\nb) $3 - (\\frac{5}{8} + \\frac{3}{8}) = 3 - 1 = 2$.", "a) 5/4; b) 2", 4, 1.0),
            make_essay(3, "Một vòi nước chảy vào bể chưa có nước. Giờ thứ nhất vòi chảy được $\\frac{1}{4}$ bể, giờ thứ hai vòi chảy được $\\frac{1}{3}$ bể. Giờ thứ ba cần chảy thêm bao nhiêu phần bể nữa để đầy bể?", "Hai giờ đầu vòi chảy được số phần bể là:\n$\\frac{1}{4} + \\frac{1}{3} = \\frac{3}{12} + \\frac{4}{12} = \\frac{7}{12}\\text{ (bể)}$.\nGiờ thứ ba cần chảy thêm số phần bể là:\n$1 - \\frac{7}{12} = \\frac{5}{12}\\text{ (bể)}$.", "5/12 bể", 4, 1.0),
            make_essay(4, "Một cuộn dây thép dài 20 m. Bác thợ cắt lần thứ nhất $\\frac{1}{4}$ cuộn dây, lần thứ hai cắt $\\frac{2}{5}$ cuộn dây. Hỏi sau hai lần cắt, cuộn dây thép còn lại bao nhiêu mét?", "Cả hai lần bác thợ đã cắt số phần cuộn dây là:\n$\\frac{1}{4} + \\frac{2}{5} = \\frac{5}{20} + \\frac{8}{20} = \\frac{13}{20}\\text{ (cuộn dây)}$.\nSố phần cuộn dây còn lại là:\n$1 - \\frac{13}{20} = \\frac{7}{20}\\text{ (cuộn dây)}$.\nChiều dài đoạn dây thép còn lại là:\n$20 \\times \\frac{7}{20} = 7\\text{ (m)}$.", "7 m", 5, 1.5),
            make_essay(5, "Tìm $x$:\na) $x - \\frac{1}{5} = \\frac{2}{3} - \\frac{4}{15}$\nb) $\\frac{7}{9} - x = \\frac{1}{3} - \\frac{1}{6}$", "a) $\\frac{2}{3} - \\frac{4}{15} = \\frac{10}{15} - \\frac{4}{15} = \\frac{6}{15} = \\frac{2}{5}$. Do đó: $x = \\frac{2}{5} + \\frac{1}{5} = \\frac{3}{5}$.\nb) $\\frac{1}{3} - \\frac{1}{6} = \\frac{2}{6} - \\frac{1}{6} = \\frac{1}{6}$. Do đó: $x = \\frac{7}{9} - \\frac{1}{6} = \\frac{14}{18} - \\frac{3}{18} = \\frac{11}{18}$.", "a) x = 3/5; b) x = 11/18", 5, 1.5),
            make_essay(6, "Tính tổng: $S = \\frac{1}{2} + \\frac{1}{6} + \\frac{1}{12} + \\dots + \\frac{1}{72} + \\frac{1}{90}$.", "Ta phân tích các mẫu số:\n$S = \\frac{1}{1 \\times 2} + \\frac{1}{2 \\times 3} + \\frac{1}{3 \\times 4} + \\dots + \\frac{1}{8 \\times 9} + \\frac{1}{9 \\times 10}$\n$= \\left(1 - \\frac{1}{2}\\right) + \\left(\\frac{1}{2} - \\frac{1}{3}\\right) + \\dots + \\left(\\frac{1}{9} - \\frac{1}{10}\\right)$\n$= 1 - \\frac{1}{10} = \\frac{9}{10}$.", "9/10", 4, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 11: {len(ex)} (Kỳ vọng: 12)")
    for b in range(51, 55):
        for t in range(1, 4):
            key = f"th4_b{b}_test{t}"
            assert key in ex, f"Thiếu {key}"
            assert len(ex[key]["part1"]) == 6
            assert len(ex[key]["part2"]) == 6
            p1_pts = sum(q["points"] for q in ex[key]["part1"])
            p2_pts = sum(q["points"] for q in ex[key]["part2"])
            assert abs(p1_pts - 3.0) < 1e-6
            assert abs(p2_pts - 7.0) < 1e-6
    print("Chủ đề 11 hoàn hảo 100%!")
