# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 12: PHÉP NHÂN, PHÉP CHIA PHÂN SỐ - PHẦN 1 (BÀI 55 & BÀI 56)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 2 bài học x 3 đề = 6 đề kiểm tra:
- Bài 55: Phép nhân phân số (th4_b55_test1 -> th4_b55_test3)
- Bài 56: Phép chia phân số (th4_b56_test1 -> th4_b56_test3)
"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

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

def get_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 55: PHÉP NHÂN PHÂN SỐ
    # =========================================================================

    # --- Bài 55 - Đề 1 ---
    exams["th4_b55_test1"] = {
        "id": "th4_b55_test1",
        "lessonId": "th4_b55",
        "lessonNum": 55,
        "testNum": 1,
        "title": "Bài 55: Phép nhân phân số - Đề số 1",
        "topic": "Phép nhân phân số",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn nhân hai phân số với nhau, ta thực hiện như thế nào?", 
                    ["Lấy tử số nhân với tử số, mẫu số nhân với mẫu số", "Lấy tử số cộng tử số, mẫu số cộng mẫu số", "Lấy tử số nhân mẫu số của phân số kia", "Giữ nguyên mẫu số và nhân hai tử số"], 
                    0, "Quy tắc: Muốn nhân hai phân số, ta lấy tử số nhân với tử số, mẫu số nhân với mẫu số.", "NB"),
            make_mc(2, "Kết quả của phép tính $\\frac{2}{3} \\times \\frac{4}{5}$ là:", 
                    ["$\\frac{8}{15}$", "$\\frac{6}{8}$", "$\\frac{8}{8}$", "$\\frac{10}{12}$"], 
                    0, "Ta có: $\\frac{2 \\times 4}{3 \\times 5} = \\frac{8}{15}$.", "TH"),
            make_mc(3, "Rút gọn kết quả của phép nhân $\\frac{3}{7} \\times \\frac{14}{9}$ được phân số tối giản là:", 
                    ["$\\frac{2}{3}$", "$\\frac{42}{63}$", "$\\frac{1}{3}$", "$\\frac{6}{7}$"], 
                    0, "Ta có: $\\frac{3 \\times 14}{7 \\times 9} = \\frac{1 \\times 2}{1 \\times 3} = \\frac{2}{3}$.", "TH"),
            make_mc(4, "Kết quả của phép tính $4 \\times \\frac{3}{8}$ sau khi rút gọn là:", 
                    ["$\\frac{3}{2}$", "$\\frac{12}{8}$", "$\\frac{7}{8}$", "$\\frac{12}{32}$"], 
                    0, "$4 \\times \\frac{3}{8} = \\frac{4 \\times 3}{8} = \\frac{12}{8} = \\frac{3}{2}$.", "TH"),
            make_mc(5, "Một hình vuông có cạnh dài $\\frac{3}{5}\\text{ m}$. Diện tích của hình vuông đó là:", 
                    ["$\\frac{9}{25}\\text{ m}^2$", "$\\frac{6}{5}\\text{ m}^2$", "$\\frac{12}{5}\\text{ m}^2$", "$\\frac{9}{10}\\text{ m}^2$"], 
                    0, "Diện tích hình vuông là: $\\frac{3}{5} \\times \\frac{3}{5} = \\frac{9}{25}\\text{ m}^2$.", "VD"),
            make_mc(6, "Biểu thức $\\frac{5}{12} \\times \\frac{7}{9} \\times 0$ có giá trị bằng:", 
                    ["0", "1", "$\\frac{35}{108}$", "$\\frac{5}{12}$"], 
                    0, "Bất kì phân số nào nhân với 0 cũng có kết quả bằng 0.", "NB")
        ],
        "part2": [
            make_essay(1, "Tính rồi rút gọn kết quả về dạng phân số tối giản:\na) $\\frac{5}{8} \\times \\frac{4}{15}$\nb) $\\frac{7}{9} \\times \\frac{3}{14}$",
                       "a) $\\frac{5}{8} \\times \\frac{4}{15} = \\frac{5 \\times 4}{8 \\times 15} = \\frac{1 \\times 1}{2 \\times 3} = \\frac{1}{6}$\nb) $\\frac{7}{9} \\times \\frac{3}{14} = \\frac{7 \\times 3}{9 \\times 14} = \\frac{1 \\times 1}{3 \\times 2} = \\frac{1}{6}$",
                       "a) 1/6; b) 1/6", 4, 1.0, "TH"),
            make_essay(2, "Tính giá trị của các biểu thức sau:\na) $6 \\times \\frac{5}{18}$\nb) $\\frac{9}{14} \\times 7$",
                       "a) $6 \\times \\frac{5}{18} = \\frac{6 \\times 5}{18} = \\frac{30}{18} = \\frac{5}{3}$\nb) $\\frac{9}{14} \\times 7 = \\frac{9 \\times 7}{14} = \\frac{63}{14} = \\frac{9}{2}$",
                       "a) 5/3; b) 9/2", 4, 1.0, "TH"),
            make_essay(3, "Tìm $x$, biết:\na) $x - \\frac{1}{4} = \\frac{2}{3} \\times \\frac{3}{8}$\nb) $x : 3 = \\frac{5}{12} \\times \\frac{4}{5}$",
                       "a) $x - \\frac{1}{4} = \\frac{2 \\times 3}{3 \\times 8} = \\frac{1}{4}$, suy ra $x = \\frac{1}{4} + \\frac{1}{4} = \\frac{2}{4} = \\frac{1}{2}$\nb) $x : 3 = \\frac{5 \\times 4}{12 \\times 5} = \\frac{1}{3}$, suy ra $x = \\frac{1}{3} \\times 3 = 1$",
                       "a) x = 1/2; b) x = 1", 4, 1.0, "VD"),
            make_essay(4, "Một tấm bìa hình chữ nhật có chiều dài $\\frac{7}{10}\\text{ m}$ và chiều rộng $\\frac{4}{7}\\text{ m}$. Tính diện tích tấm bìa hình chữ nhật đó.",
                       "Diện tích tấm bìa hình chữ nhật là:\n$\\frac{7}{10} \\times \\frac{4}{7} = \\frac{7 \\times 4}{10 \\times 7} = \\frac{4}{10} = \\frac{2}{5}\\text{ (m}^2\\text{)}$\nĐáp số: $\\frac{2}{5}\\text{ m}^2$",
                       "2/5 m^2", 5, 1.5, "VD"),
            make_essay(5, "Một người thợ may một cái áo trẻ em hết $\\frac{5}{4}\\text{ m}$ vải. Hỏi người đó may 8 cái áo cùng loại như thế thì hết bao nhiêu mét vải?",
                       "May 8 cái áo trẻ em hết số mét vải là:\n$\\frac{5}{4} \\times 8 = \\frac{5 \\times 8}{4} = \\frac{40}{4} = 10\\text{ (m)}$\nĐáp số: $10\\text{ m vải}$",
                       "10 m", 5, 1.5, "VD"),
            make_essay(6, "Tính giá trị của biểu thức bằng cách thuận tiện nhất:\n$A = \\frac{4}{11} \\times \\frac{5}{9} + \\frac{4}{11} \\times \\frac{4}{9}$",
                       "Ta áp dụng tính chất một số nhân với một tổng:\n$A = \\frac{4}{11} \\times \\left(\\frac{5}{9} + \\frac{4}{9}\\right) = \\frac{4}{11} \\times \\frac{9}{9} = \\frac{4}{11} \\times 1 = \\frac{4}{11}$\nĐáp số: $\\frac{4}{11}$",
                       "4/11", 4, 1.0, "VDC")
        ]
    }

    # --- Bài 55 - Đề 2 ---
    exams["th4_b55_test2"] = {
        "id": "th4_b55_test2",
        "lessonId": "th4_b55",
        "lessonNum": 55,
        "testNum": 2,
        "title": "Bài 55: Phép nhân phân số - Đề số 2",
        "topic": "Phép nhân phân số",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn nhân một phân số với một số tự nhiên, ta có thể làm như thế nào?", 
                    ["Lấy tử số nhân với số tự nhiên và giữ nguyên mẫu số", "Lấy mẫu số nhân với số tự nhiên và giữ nguyên tử số", "Lấy cả tử số và mẫu số nhân với số tự nhiên", "Cộng số tự nhiên đó vào tử số"], 
                    0, "Muốn nhân một phân số với số tự nhiên, ta nhân tử số với số tự nhiên và giữ nguyên mẫu số.", "NB"),
            make_mc(2, "Tính: $\\frac{3}{5} \\times \\frac{5}{7} = ?$", 
                    ["$\\frac{3}{7}$", "$\\frac{15}{35}$", "$\\frac{8}{12}$", "$\\frac{15}{7}$"], 
                    0, "$\\frac{3 \\times 5}{5 \\times 7} = \\frac{3}{7}$.", "TH"),
            make_mc(3, "Phép nhân nào dưới đây có kết quả bằng 1?", 
                    ["$\\frac{4}{9} \\times \\frac{9}{4}$", "$\\frac{4}{9} \\times \\frac{4}{9}$", "$\\frac{4}{9} \\times 1$", "$\\frac{4}{9} \\times 0$"], 
                    0, "$\\frac{4}{9} \\times \\frac{9}{4} = \\frac{36}{36} = 1$.", "TH"),
            make_mc(4, "Một ô tô chạy trong 1 giờ được $\\frac{45}{2}\\text{ km}$. Trong 2 giờ ô tô đó đi được quãng đường là:", 
                    ["$45\\text{ km}$", "$90\\text{ km}$", "$\\frac{45}{4}\\text{ km}$", "$\\frac{47}{2}\\text{ km}$"], 
                    0, "Quãng đường đi được: $\\frac{45}{2} \\times 2 = 45\\text{ km}$.", "VD"),
            make_mc(5, "Giá trị của biểu thức $\\left(\\frac{1}{2} + \\frac{1}{3}\\right) \\times 6$ là:", 
                    ["5", "4", "3", "6"], 
                    0, "$\\left(\\frac{3}{6} + \\frac{2}{6}\\right) \\times 6 = \\frac{5}{6} \\times 6 = 5$.", "VD"),
            make_mc(6, "Điền số thích hợp vào chỗ chấm: $\\frac{5}{8} \\times \\dots = \\frac{5}{8}$", 
                    ["1", "0", "$\\frac{8}{5}$", "2"], 
                    0, "Bất kì số nào nhân với 1 cũng bằng chính nó.", "NB")
        ],
        "part2": [
            make_essay(1, "Thực hiện phép tính rồi rút gọn:\na) $\\frac{9}{10} \\times \\frac{5}{6}$\nb) $\\frac{8}{15} \\times \\frac{25}{16}$",
                       "a) $\\frac{9}{10} \\times \\frac{5}{6} = \\frac{9 \\times 5}{10 \\times 6} = \\frac{3 \\times 1}{2 \\times 2} = \\frac{3}{4}$\nb) $\\frac{8}{15} \\times \\frac{25}{16} = \\frac{8 \\times 25}{15 \\times 16} = \\frac{1 \\times 5}{3 \\times 2} = \\frac{5}{6}$",
                       "a) 3/4; b) 5/6", 4, 1.0, "TH"),
            make_essay(2, "Tính nhanh các tích sau:\na) $8 \\times \\frac{7}{24}$\nb) $\\frac{11}{30} \\times 5$",
                       "a) $8 \\times \\frac{7}{24} = \\frac{8 \\times 7}{24} = \\frac{1 \\times 7}{3} = \\frac{7}{3}$\nb) $\\frac{11}{30} \\times 5 = \\frac{11 \\times 5}{30} = \\frac{11 \\times 1}{6} = \\frac{11}{6}$",
                       "a) 7/3; b) 11/6", 4, 1.0, "TH"),
            make_essay(3, "Tìm $x$ trong các biểu thức sau:\na) $x - \\frac{3}{5} = \\frac{1}{2} \\times \\frac{4}{5}$\nb) $x : \\frac{2}{3} = \\frac{9}{10} \\times \\frac{5}{6}$",
                       "a) $x - \\frac{3}{5} = \\frac{1 \\times 4}{2 \\times 5} = \\frac{2}{5} \\Rightarrow x = \\frac{2}{5} + \\frac{3}{5} = \\frac{5}{5} = 1$\nb) $x : \\frac{2}{3} = \\frac{9 \\times 5}{10 \\times 6} = \\frac{3}{4} \\Rightarrow x = \\frac{3}{4} \\times \\frac{2}{3} = \\frac{6}{12} = \\frac{1}{2}$",
                       "a) x = 1; b) x = 1/2", 4, 1.0, "VD"),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chiều dài $\\frac{15}{2}\\text{ m}$, chiều rộng $\\frac{8}{3}\\text{ m}$. Tính chu vi và diện tích mảnh vườn đó.",
                       "Chu vi mảnh vườn hình chữ nhật là:\n$\\left(\\frac{15}{2} + \\frac{8}{3}\\right) \\times 2 = \\left(\\frac{45}{6} + \\frac{16}{6}\\right) \\times 2 = \\frac{61}{6} \\times 2 = \\frac{61}{3}\\text{ (m)}$\nDiện tích mảnh vườn là:\n$\\frac{15}{2} \\times \\frac{8}{3} = \\frac{15 \\times 8}{2 \\times 3} = \\frac{5 \\times 4}{1 \\times 1} = 20\\text{ (m}^2\\text{)}$\nĐáp số: Chu vi: $\\frac{61}{3}\\text{ m}$; Diện tích: $20\\text{ m}^2$",
                       "Chu vi: 61/3 m; Diện tích: 20 m^2", 6, 1.5, "VD"),
            make_essay(5, "Mỗi gói bánh quy cân nặng $\\frac{3}{8}\\text{ kg}$. Hỏi 16 gói bánh quy cùng loại như thế cân nặng tất cả bao nhiêu ki-lô-gam?",
                       "16 gói bánh quy cân nặng tất cả số ki-lô-gam là:\n$\\frac{3}{8} \\times 16 = \\frac{3 \\times 16}{8} = 3 \\times 2 = 6\\text{ (kg)}$\nĐáp số: $6\\text{ kg}$",
                       "6 kg", 5, 1.5, "VD"),
            make_essay(6, "Tính giá trị biểu thức bằng cách hợp lí:\n$M = \\frac{5}{13} \\times \\frac{7}{12} + \\frac{5}{13} \\times \\frac{5}{12}$",
                       "Áp dụng tính chất phân phối của phép nhân đối với phép cộng:\n$M = \\frac{5}{13} \\times \\left(\\frac{7}{12} + \\frac{5}{12}\\right) = \\frac{5}{13} \\times \\frac{12}{12} = \\frac{5}{13} \\times 1 = \\frac{5}{13}$\nĐáp số: $\\frac{5}{13}$",
                       "5/13", 4, 1.0, "VDC")
        ]
    }

    # --- Bài 55 - Đề 3 ---
    exams["th4_b55_test3"] = {
        "id": "th4_b55_test3",
        "lessonId": "th4_b55",
        "lessonNum": 55,
        "testNum": 3,
        "title": "Bài 55: Phép nhân phân số - Đề số 3",
        "topic": "Phép nhân phân số",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính chất giao hoán của phép nhân phân số được viết dưới dạng công thức là:", 
                    ["$\\frac{a}{b} \\times \\frac{c}{d} = \\frac{c}{d} \\times \\frac{a}{b}$", "$\\frac{a}{b} + \\frac{c}{d} = \\frac{c}{d} + \\frac{a}{b}$", "$\\frac{a}{b} \\times 1 = \\frac{a}{b}$", "$\\frac{a}{b} \\times \\frac{b}{a} = 1$"], 
                    0, "Tính chất giao hoán: khi đổi chỗ các phân số trong một tích thì tích không thay đổi.", "NB"),
            make_mc(2, "Kết quả của phép nhân $\\frac{7}{12} \\times \\frac{6}{14}$ sau khi rút gọn là:", 
                    ["$\\frac{1}{4}$", "$\\frac{1}{2}$", "$\\frac{42}{168}$", "$\\frac{2}{3}$"], 
                    0, "$\\frac{7 \\times 6}{12 \\times 14} = \\frac{1 \\times 1}{2 \\times 2} = \\frac{1}{4}$.", "TH"),
            make_mc(3, "Tính: $\\frac{4}{9} \\times 18 = ?$", 
                    ["8", "72", "$\\frac{72}{162}$", "$\\frac{2}{9}$"], 
                    0, "$\\frac{4 \\times 18}{9} = 4 \\times 2 = 8$.", "TH"),
            make_mc(4, "Một chai nước ngọt chứa $\\frac{3}{4}\\text{ lít}$ nước. Hỏi 12 chai nước ngọt như vậy chứa tất cả bao nhiêu lít nước?", 
                    ["$9\\text{ lít}$", "$16\\text{ lít}$", "$\\frac{9}{4}\\text{ lít}$", "$6\\text{ lít}$"], 
                    0, "Số lít nước trong 12 chai: $\\frac{3}{4} \\times 12 = 9\\text{ (lít)}$.", "VD"),
            make_mc(5, "Cho biểu thức: $B = \\frac{5}{7} \\times \\frac{2}{3} + \\frac{5}{7} \\times \\frac{1}{3}$. Giá trị của $B$ là:", 
                    ["$\\frac{5}{7}$", "$\\frac{15}{21}$", "1", "$\\frac{10}{21}$"], 
                    0, "$B = \\frac{5}{7} \\times \\left(\\frac{2}{3} + \\frac{1}{3}\\right) = \\frac{5}{7} \\times 1 = \\frac{5}{7}$.", "TH"),
            make_mc(6, "Một tấm kính hình thoi có độ dài hai đường chéo là $\\frac{4}{5}\\text{ m}$ và $\\frac{5}{6}\\text{ m}$. Diện tích tấm kính đó là:", 
                    ["$\\frac{1}{3}\\text{ m}^2$", "$\\frac{2}{3}\\text{ m}^2$", "$\\frac{20}{30}\\text{ m}^2$", "$\\frac{1}{6}\\text{ m}^2$"], 
                    0, "Diện tích hình thoi bằng tích hai đường chéo chia cho 2: $\\frac{1}{2} \\times \\frac{4}{5} \\times \\frac{5}{6} = \\frac{20}{60} = \\frac{1}{3}\\text{ m}^2$.", "VD")
        ],
        "part2": [
            make_essay(1, "Tính giá trị của các biểu thức sau (kết quả là phân số tối giản):\na) $\\frac{6}{25} \\times \\frac{15}{18}$\nb) $\\frac{14}{27} \\times \\frac{9}{28}$",
                       "a) $\\frac{6}{25} \\times \\frac{15}{18} = \\frac{6 \\times 15}{25 \\times 18} = \\frac{1 \\times 3}{5 \\times 3} = \\frac{1}{5}$\nb) $\\frac{14}{27} \\times \\frac{9}{28} = \\frac{14 \\times 9}{27 \\times 28} = \\frac{1 \\times 1}{3 \\times 2} = \\frac{1}{6}$",
                       "a) 1/5; b) 1/6", 4, 1.0, "TH"),
            make_essay(2, "Tính:\na) $15 \\times \\frac{4}{45}$\nb) $\\frac{8}{21} \\times 14$",
                       "a) $15 \\times \\frac{4}{45} = \\frac{15 \\times 4}{45} = \\frac{1 \\times 4}{3} = \\frac{4}{3}$\nb) $\\frac{8}{21} \\times 14 = \\frac{8 \\times 14}{21} = \\frac{8 \\times 2}{3} = \\frac{16}{3}$",
                       "a) 4/3; b) 16/3", 4, 1.0, "TH"),
            make_essay(3, "Tìm $x$ biết:\na) $x - \\frac{2}{7} = \\frac{3}{5} \\times \\frac{10}{21}$\nb) $\\frac{8}{9} \\times \\frac{3}{4} - x = \\frac{1}{6}$",
                       "a) $x - \\frac{2}{7} = \\frac{3 \\times 10}{5 \\times 21} = \\frac{1 \\times 2}{1 \\times 7} = \\frac{2}{7} \\Rightarrow x = \\frac{2}{7} + \\frac{2}{7} = \\frac{4}{7}$\nb) $\\frac{8 \\times 3}{9 \\times 4} - x = \\frac{1}{6} \\Rightarrow \\frac{2}{3} - x = \\frac{1}{6} \\Rightarrow x = \\frac{2}{3} - \\frac{1}{6} = \\frac{4}{6} - \\frac{1}{6} = \\frac{3}{6} = \\frac{1}{2}$",
                       "a) x = 4/7; b) x = 1/2", 4, 1.0, "VD"),
            make_essay(4, "Một căn phòng hình chữ nhật có chiều rộng $\\frac{9}{2}\\text{ m}$, chiều dài gấp đôi chiều rộng. Tính diện tích của căn phòng đó.",
                       "Chiều dài căn phòng hình chữ nhật là:\n$\\frac{9}{2} \\times 2 = 9\\text{ (m)}$\nDiện tích của căn phòng là:\n$9 \\times \\frac{9}{2} = \\frac{81}{2}\\text{ (m}^2\\text{)}$\nĐáp số: $\\frac{81}{2}\\text{ m}^2$",
                       "81/2 m^2", 5, 1.5, "VD"),
            make_essay(5, "Mỗi bước đi của bạn An dài khoảng $\\frac{2}{5}\\text{ m}$. Hỏi An bước 35 bước như thế thì đi được quãng đường dài bao nhiêu mét?",
                       "An bước 35 bước thì đi được quãng đường dài là:\n$\\frac{2}{5} \\times 35 = \\frac{2 \\times 35}{5} = 2 \\times 7 = 14\\text{ (m)}$\nĐáp số: $14\\text{ m}$",
                       "14 m", 5, 1.5, "VD"),
            make_essay(6, "Tính bằng cách thuận tiện nhất:\n$P = \\frac{9}{17} \\times \\frac{15}{23} + \\frac{9}{17} \\times \\frac{8}{23}$",
                       "Áp dụng tính chất kết hợp và nhân một số với một tổng:\n$P = \\frac{9}{17} \\times \\left(\\frac{15}{23} + \\frac{8}{23}\\right) = \\frac{9}{17} \\times \\frac{23}{23} = \\frac{9}{17} \\times 1 = \\frac{9}{17}$\nĐáp số: $\\frac{9}{17}$",
                       "9/17", 4, 1.0, "VDC")
        ]
    }

    # =========================================================================
    # BÀI 56: PHÉP CHIA PHÂN SỐ
    # =========================================================================

    # --- Bài 56 - Đề 1 ---
    exams["th4_b56_test1"] = {
        "id": "th4_b56_test1",
        "lessonId": "th4_b56",
        "lessonNum": 56,
        "testNum": 1,
        "title": "Bài 56: Phép chia phân số - Đề số 1",
        "topic": "Phép chia phân số",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Phân số đảo ngược của phân số $\\frac{3}{7}$ là:", 
                    ["$\\frac{7}{3}$", "$\\frac{3}{7}$", "$-\\frac{3}{7}$", "$\\frac{7}{10}$"], 
                    0, "Phân số đảo ngược của $\\frac{a}{b}$ là $\\frac{b}{a}$. Do đó phân số đảo ngược của $\\frac{3}{7}$ là $\\frac{7}{3}$.", "NB"),
            make_mc(2, "Muốn chia một phân số cho một phân số, ta thực hiện như thế nào?", 
                    ["Lấy phân số thứ nhất nhân với phân số đảo ngược của phân số thứ hai", "Lấy tử số chia cho tử số, mẫu số chia cho mẫu số", "Lấy phân số thứ hai nhân với phân số thứ nhất", "Lấy phân số thứ nhất cộng với phân số thứ hai"], 
                    0, "Quy tắc: Muốn chia một phân số cho một phân số, ta lấy phân số thứ nhất nhân với phân số đảo ngược của phân số thứ hai.", "NB"),
            make_mc(3, "Kết quả của phép chia $\\frac{4}{9} : \\frac{2}{3}$ là:", 
                    ["$\\frac{2}{3}$", "$\\frac{8}{27}$", "$\\frac{6}{9}$", "$\\frac{3}{2}$"], 
                    0, "$\\frac{4}{9} : \\frac{2}{3} = \\frac{4}{9} \\times \\frac{3}{2} = \\frac{12}{18} = \\frac{2}{3}$.", "TH"),
            make_mc(4, "Kết quả của phép tính $\\frac{5}{6} : 5$ là:", 
                    ["$\\frac{1}{6}$", "$\\frac{25}{6}$", "$\\frac{5}{30}$", "1"], 
                    0, "$\\frac{5}{6} : 5 = \\frac{5}{6} \\times \\frac{1}{5} = \\frac{1}{6}$.", "TH"),
            make_mc(5, "Tìm thừa số $x$, biết: $x \\times \\frac{3}{4} = \\frac{9}{16}$:", 
                    ["$x = \\frac{3}{4}$", "$x = \\frac{27}{64}$", "$x = \\frac{1}{4}$", "$x = \\frac{4}{3}$"], 
                    0, "$x = \\frac{9}{16} : \\frac{3}{4} = \\frac{9}{16} \\times \\frac{4}{3} = \\frac{3}{4}$.", "TH"),
            make_mc(6, "Một thanh sắt dài $\\frac{4}{5}\\text{ m}$ được cưa đều thành 4 đoạn bằng nhau. Mỗi đoạn dài bao nhiêu mét?", 
                    ["$\\frac{1}{5}\\text{ m}$", "$\\frac{16}{5}\\text{ m}$", "$\\frac{4}{20}\\text{ m}$", "$\\frac{1}{4}\\text{ m}$"], 
                    0, "Mỗi đoạn dài: $\\frac{4}{5} : 4 = \\frac{4}{5 \\times 4} = \\frac{1}{5}\\text{ (m)}$.", "VD")
        ],
        "part2": [
            make_essay(1, "Tính rồi rút gọn kết quả về phân số tối giản:\na) $\\frac{3}{8} : \\frac{9}{16}$\nb) $\\frac{5}{12} : \\frac{15}{8}$",
                       "a) $\\frac{3}{8} : \\frac{9}{16} = \\frac{3}{8} \\times \\frac{16}{9} = \\frac{3 \\times 16}{8 \\times 9} = \\frac{1 \\times 2}{1 \\times 3} = \\frac{2}{3}$\nb) $\\frac{5}{12} : \\frac{15}{8} = \\frac{5}{12} \\times \\frac{8}{15} = \\frac{5 \\times 8}{12 \\times 15} = \\frac{1 \\times 2}{3 \\times 3} = \\frac{2}{9}$",
                       "a) 2/3; b) 2/9", 4, 1.0, "TH"),
            make_essay(2, "Thực hiện phép tính:\na) $6 : \\frac{3}{5}$\nb) $\\frac{8}{9} : 4$",
                       "a) $6 : \\frac{3}{5} = 6 \\times \\frac{5}{3} = \\frac{6 \\times 5}{3} = 10$\nb) $\\frac{8}{9} : 4 = \\frac{8}{9 \\times 4} = \\frac{2}{9}$",
                       "a) 10; b) 2/9", 4, 1.0, "TH"),
            make_essay(3, "Tìm $x$:\na) $x \\times \\frac{2}{5} = \\frac{8}{15}$\nb) $\\frac{7}{10} : x = \\frac{14}{15}$",
                       "a) $x = \\frac{8}{15} : \\frac{2}{5} = \\frac{8}{15} \\times \\frac{5}{2} = \\frac{4}{3}$\nb) $x = \\frac{7}{10} : \\frac{14}{15} = \\frac{7}{10} \\times \\frac{15}{14} = \\frac{1 \\times 3}{2 \\times 2} = \\frac{3}{4}$",
                       "a) x = 4/3; b) x = 3/4", 4, 1.0, "VD"),
            make_essay(4, "Một mảnh đất hình chữ nhật có diện tích là $\\frac{5}{8}\\text{ m}^2$ và chiều rộng là $\\frac{1}{2}\\text{ m}$. Tính chiều dài mảnh đất đó.",
                       "Chiều dài mảnh đất hình chữ nhật là:\n$\\frac{5}{8} : \\frac{1}{2} = \\frac{5}{8} \\times 2 = \\frac{10}{8} = \\frac{5}{4}\\text{ (m)}$\nĐáp số: $\\frac{5}{4}\\text{ m}$",
                       "5/4 m", 5, 1.5, "VD"),
            make_essay(5, "Một bình nước chứa $\\frac{7}{2}\\text{ lít}$ nước trái cây. Người ta rót đều nước từ bình đó vào các cốc, mỗi cốc chứa $\\frac{1}{4}\\text{ lít}$. Hỏi rót được tất cả bao nhiêu cốc nước trái cây như vậy?",
                       "Số cốc nước trái cây rót được tất cả là:\n$\\frac{7}{2} : \\frac{1}{4} = \\frac{7}{2} \\times 4 = 14\\text{ (cốc)}$\nĐáp số: $14\\text{ cốc}$",
                       "14 cốc", 5, 1.5, "VD"),
            make_essay(6, "Tính giá trị của biểu thức bằng cách hợp lí:\n$E = \\left(\\frac{5}{7} \\times \\frac{3}{8}\\right) : \\frac{3}{8}$",
                       "Ta có phép chia cho một số bằng phép nhân với số đảo ngược, hoặc nhận xét tích của một số với $\\frac{3}{8}$ rồi chia cho $\\frac{3}{8}$ thì bằng chính số đó:\n$E = \\frac{5}{7} \\times \\left(\\frac{3}{8} : \\frac{3}{8}\\right) = \\frac{5}{7} \\times 1 = \\frac{5}{7}$\nĐáp số: $\\frac{5}{7}$",
                       "5/7", 4, 1.0, "VDC")
        ]
    }

    # --- Bài 56 - Đề 2 ---
    exams["th4_b56_test2"] = {
        "id": "th4_b56_test2",
        "lessonId": "th4_b56",
        "lessonNum": 56,
        "testNum": 2,
        "title": "Bài 56: Phép chia phân số - Đề số 2",
        "topic": "Phép chia phân số",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số tự nhiên 6 viết dưới dạng phân số đảo ngược có kết quả là:", 
                    ["$\\frac{1}{6}$", "$\\frac{6}{1}$", "6", "$-6$"], 
                    0, "$6 = \\frac{6}{1}$, phân số đảo ngược của $\\frac{6}{1}$ là $\\frac{1}{6}$.", "NB"),
            make_mc(2, "Tính: $\\frac{7}{10} : \\frac{14}{15} = ?$", 
                    ["$\\frac{3}{4}$", "$\\frac{4}{3}$", "$\\frac{98}{150}$", "$\\frac{1}{2}$"], 
                    0, "$\\frac{7}{10} : \\frac{14}{15} = \\frac{7}{10} \\times \\frac{15}{14} = \\frac{1 \\times 3}{2 \\times 2} = \\frac{3}{4}$.", "TH"),
            make_mc(3, "Kết quả của phép tính $8 : \\frac{4}{7}$ là:", 
                    ["14", "$\\frac{32}{7}$", "$\\frac{1}{14}$", "$\\frac{4}{56}$"], 
                    0, "$8 : \\frac{4}{7} = 8 \\times \\frac{7}{4} = 2 \\times 7 = 14$.", "TH"),
            make_mc(4, "Biết diện tích hình chữ nhật là $\\frac{9}{14}\\text{ m}^2$, chiều dài là $\\frac{3}{2}\\text{ m}$. Chiều rộng của hình chữ nhật đó là:", 
                    ["$\\frac{3}{7}\\text{ m}$", "$\\frac{27}{28}\\text{ m}$", "$\\frac{7}{3}\\text{ m}$", "$\\frac{1}{7}\\text{ m}$"], 
                    0, "Chiều rộng: $\\frac{9}{14} : \\frac{3}{2} = \\frac{9}{14} \\times \\frac{2}{3} = \\frac{3}{7}\\text{ (m)}$.", "VD"),
            make_mc(5, "Tìm $y$, biết: $y : \\frac{5}{9} = \\frac{3}{10}$:", 
                    ["$y = \\frac{1}{6}$", "$y = \\frac{27}{50}$", "$y = \\frac{50}{27}$", "$y = 6$"], 
                    0, "$y = \\frac{3}{10} \\times \\frac{5}{9} = \\frac{15}{90} = \\frac{1}{6}$.", "TH"),
            make_mc(6, "Kết quả của phép chia $\\frac{11}{13} : \\frac{11}{13}$ bằng:", 
                    ["1", "0", "$\\frac{121}{169}$", "$\\frac{22}{26}$"], 
                    0, "Mọi số khác 0 khi chia cho chính nó đều có kết quả bằng 1.", "NB")
        ],
        "part2": [
            make_essay(1, "Tính rồi rút gọn:\na) $\\frac{4}{15} : \\frac{8}{25}$\nb) $\\frac{14}{9} : \\frac{7}{18}$",
                       "a) $\\frac{4}{15} : \\frac{8}{25} = \\frac{4}{15} \\times \\frac{25}{8} = \\frac{4 \\times 25}{15 \\times 8} = \\frac{1 \\times 5}{3 \\times 2} = \\frac{5}{6}$\nb) $\\frac{14}{9} : \\frac{7}{18} = \\frac{14}{9} \\times \\frac{18}{7} = \\frac{14 \\times 18}{9 \\times 7} = 2 \\times 2 = 4$",
                       "a) 5/6; b) 4", 4, 1.0, "TH"),
            make_essay(2, "Tính giá trị các phép tính sau:\na) $\\frac{9}{16} : 3$\nb) $12 : \\frac{4}{5}$",
                       "a) $\\frac{9}{16} : 3 = \\frac{9}{16 \\times 3} = \\frac{3}{16}$\nb) $12 : \\frac{4}{5} = 12 \\times \\frac{5}{4} = 3 \\times 5 = 15$",
                       "a) 3/16; b) 15", 4, 1.0, "TH"),
            make_essay(3, "Tìm $x$:\na) $x \\times \\frac{3}{7} = \\frac{9}{14}$\nb) $x : \\frac{4}{9} = \\frac{27}{32}$",
                       "a) $x = \\frac{9}{14} : \\frac{3}{7} = \\frac{9}{14} \\times \\frac{7}{3} = \\frac{3}{2}$\nb) $x = \\frac{27}{32} \\times \\frac{4}{9} = \\frac{27 \\times 4}{32 \\times 9} = \\frac{3 \\times 1}{8 \\times 1} = \\frac{3}{8}$",
                       "a) x = 3/2; b) x = 3/8", 4, 1.0, "VD"),
            make_essay(4, "Một tấm vải dài $\\frac{18}{5}\\text{ m}$ được cắt thành các mảnh nhỏ, mỗi mảnh dài $\\frac{3}{5}\\text{ m}$. Hỏi người ta cắt được bao nhiêu mảnh vải như thế?",
                       "Cắt được số mảnh vải nhỏ là:\n$\\frac{18}{5} : \\frac{3}{5} = \\frac{18}{5} \\times \\frac{5}{3} = 6\\text{ (mảnh)}$\nĐáp số: $6\\text{ mảnh vải}$",
                       "6 mảnh vải", 5, 1.5, "VD"),
            make_essay(5, "Người ta chia đều $\\frac{9}{4}\\text{ kg}$ đường vào 6 túi nhỏ. Hỏi mỗi túi nhỏ có bao nhiêu ki-lô-gam đường?",
                       "Mỗi túi nhỏ có số ki-lô-gam đường là:\n$\\frac{9}{4} : 6 = \\frac{9}{4 \\times 6} = \\frac{9}{24} = \\frac{3}{8}\\text{ (kg)}$\nĐáp số: $\\frac{3}{8}\\text{ kg đường}$",
                       "3/8 kg", 5, 1.5, "VD"),
            make_essay(6, "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\n$Q = \\frac{7}{19} : \\frac{5}{6} + \\frac{12}{19} : \\frac{5}{6}$",
                       "Chia cho một phân số bằng nhân với phân số đảo ngược:\n$Q = \\frac{7}{19} \\times \\frac{6}{5} + \\frac{12}{19} \\times \\frac{6}{5} = \\left(\\frac{7}{19} + \\frac{12}{19}\\right) \\times \\frac{6}{5} = \\frac{19}{19} \\times \\frac{6}{5} = 1 \\times \\frac{6}{5} = \\frac{6}{5}$\nĐáp số: $\\frac{6}{5}$",
                       "6/5", 4, 1.0, "VDC")
        ]
    }

    # --- Bài 56 - Đề 3 ---
    exams["th4_b56_test3"] = {
        "id": "th4_b56_test3",
        "lessonId": "th4_b56",
        "lessonNum": 56,
        "testNum": 3,
        "title": "Bài 56: Phép chia phân số - Đề số 3",
        "topic": "Phép chia phân số",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Cặp phân số nào dưới đây là hai phân số đảo ngược của nhau?", 
                    ["$\\frac{4}{7}$ và $\\frac{7}{4}$", "$\\frac{3}{5}$ và $\\frac{6}{10}$", "$\\frac{2}{3}$ và $\\frac{3}{20}$", "$\\frac{1}{4}$ và $\\frac{1}{2}$"], 
                    0, "Hai phân số đảo ngược nhau là $\\frac{a}{b}$ và $\\frac{b}{a}$. Do đó $\\frac{4}{7}$ và $\\frac{7}{4}$ là cặp phân số đảo ngược.", "NB"),
            make_mc(2, "Tính: $\\frac{8}{15} : \\frac{4}{5} = ?$", 
                    ["$\\frac{2}{3}$", "$\\frac{3}{2}$", "$\\frac{32}{75}$", "$\\frac{1}{3}$"], 
                    0, "$\\frac{8}{15} : \\frac{4}{5} = \\frac{8}{15} \\times \\frac{5}{4} = \\frac{2 \\times 1}{3 \\times 1} = \\frac{2}{3}$.", "TH"),
            make_mc(3, "Kết quả của phép chia $\\frac{10}{21} : 5$ bằng:", 
                    ["$\\frac{2}{21}$", "$\\frac{50}{21}$", "$\\frac{2}{7}$", "$\\frac{1}{21}$"], 
                    0, "$\\frac{10}{21} : 5 = \\frac{10}{21 \\times 5} = \\frac{2}{21}$.", "TH"),
            make_mc(4, "Một sợi dây dù dài $\\frac{25}{4}\\text{ m}$. Người ta cắt thành các đoạn dây nhỏ, mỗi đoạn dài $\\frac{5}{4}\\text{ m}$. Số đoạn dây cắt được là:", 
                    ["5 đoạn", "6 đoạn", "4 đoạn", "$\\frac{125}{16}$ đoạn"], 
                    0, "Số đoạn dây cắt được: $\\frac{25}{4} : \\frac{5}{4} = \\frac{25}{5} = 5\\text{ (đoạn)}$.", "VD"),
            make_mc(5, "Tìm số bị chia $x$ trong phép tính: $x : \\frac{2}{7} = \\frac{14}{15}$:", 
                    ["$x = \\frac{4}{15}$", "$x = \\frac{49}{15}$", "$x = \\frac{15}{4}$", "$x = \\frac{28}{105}$"], 
                    0, "$x = \\frac{14}{15} \\times \\frac{2}{7} = \\frac{2 \\times 2}{15 \\times 1} = \\frac{4}{15}$.", "TH"),
            make_mc(6, "Giá trị của biểu thức $\\frac{3}{5} : 1$ bằng:", 
                    ["$\\frac{3}{5}$", "1", "$\\frac{5}{3}$", "0"], 
                    0, "Bất kì phân số nào chia cho 1 cũng bằng chính nó.", "NB")
        ],
        "part2": [
            make_essay(1, "Tính rồi rút gọn thành phân số tối giản:\na) $\\frac{12}{25} : \\frac{18}{35}$\nb) $\\frac{16}{21} : \\frac{24}{49}$",
                       "a) $\\frac{12}{25} : \\frac{18}{35} = \\frac{12}{25} \\times \\frac{35}{18} = \\frac{12 \\times 35}{25 \\times 18} = \\frac{2 \\times 7}{5 \\times 3} = \\frac{14}{15}$\nb) $\\frac{16}{21} : \\frac{24}{49} = \\frac{16}{21} \\times \\frac{49}{24} = \\frac{16 \\times 49}{21 \\times 24} = \\frac{2 \\times 7}{3 \\times 3} = \\frac{14}{9}$",
                       "a) 14/15; b) 14/9", 4, 1.0, "TH"),
            make_essay(2, "Tính:\na) $15 : \\frac{5}{6}$\nb) $\\frac{14}{15} : 7$",
                       "a) $15 : \\frac{5}{6} = 15 \\times \\frac{6}{5} = 3 \\times 6 = 18$\nb) $\\frac{14}{15} : 7 = \\frac{14}{15 \\times 7} = \\frac{2}{15}$",
                       "a) 18; b) 2/15", 4, 1.0, "TH"),
            make_essay(3, "Tìm $x$:\na) $\\frac{3}{8} : x = \\frac{9}{20}$\nb) $x \\times \\frac{5}{7} = \\frac{15}{28}$",
                       "a) $x = \\frac{3}{8} : \\frac{9}{20} = \\frac{3}{8} \\times \\frac{20}{9} = \\frac{3 \\times 20}{8 \\times 9} = \\frac{1 \\times 5}{2 \\times 3} = \\frac{5}{6}$\nb) $x = \\frac{15}{28} : \\frac{5}{7} = \\frac{15}{28} \\times \\frac{7}{5} = \\frac{15 \\times 7}{28 \\times 5} = \\frac{3 \\times 1}{4 \\times 1} = \\frac{3}{4}$",
                       "a) x = 5/6; b) x = 3/4", 4, 1.0, "VD"),
            make_essay(4, "Một bảng gỗ hình chữ nhật có diện tích là $\\frac{3}{4}\\text{ m}^2$ và chiều dài là $\\frac{9}{8}\\text{ m}$. Hỏi chiều rộng của bảng gỗ đó là bao nhiêu mét?",
                       "Chiều rộng của bảng gỗ hình chữ nhật là:\n$\\frac{3}{4} : \\frac{9}{8} = \\frac{3}{4} \\times \\frac{8}{9} = \\frac{3 \\times 8}{4 \\times 9} = \\frac{1 \\times 2}{1 \\times 3} = \\frac{2}{3}\\text{ (m)}$\nĐáp số: $\\frac{2}{3}\\text{ m}$",
                       "2/3 m", 5, 1.5, "VD"),
            make_essay(5, "Một cửa hàng có $\\frac{35}{2}\\text{ kg}$ gạo ngon đem đóng đều vào 7 túi. Hỏi mỗi túi gạo như thế có bao nhiêu ki-lô-gam?",
                       "Mỗi túi gạo có số ki-lô-gam là:\n$\\frac{35}{2} : 7 = \\frac{35}{2 \\times 7} = \\frac{5}{2}\\text{ (kg)}$\nĐáp số: $\\frac{5}{2}\\text{ kg gạo}$",
                       "5/2 kg", 5, 1.5, "VD"),
            make_essay(6, "Tính giá trị biểu thức bằng cách thuận tiện nhất:\n$K = \\frac{8}{17} : \\frac{4}{9} - \\frac{3}{17} : \\frac{4}{9}$",
                       "Ta chuyển phép chia về nhân với phân số đảo ngược:\n$K = \\frac{8}{17} \\times \\frac{9}{4} - \\frac{3}{17} \\times \\frac{9}{4} = \\left(\\frac{8}{17} - \\frac{3}{17}\\right) \\times \\frac{9}{4} = \\frac{5}{17} \\times \\frac{9}{4} = \\frac{45}{68}$\nĐáp số: $\\frac{45}{68}$",
                       "45/68", 4, 1.0, "VDC")
        ]
    }

    return exams
