# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 12: PHÉP NHÂN, PHÉP CHIA PHÂN SỐ - PHẦN 2 (BÀI 57 & BÀI 58)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 2 bài học x 3 đề = 6 đề kiểm tra:
- Bài 57: Tìm phân số của một số (th4_b57_test1 -> th4_b57_test3)
- Bài 58: Luyện tập chung Chủ đề 12 (th4_b58_test1 -> th4_b58_test3)
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

def get_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 57: TÌM PHÂN SỐ CỦA MỘT SỐ
    # =========================================================================

    # --- Bài 57 - Đề 1 ---
    exams["th4_b57_test1"] = {
        "id": "th4_b57_test1",
        "lessonId": "th4_b57",
        "lessonNum": 57,
        "testNum": 1,
        "title": "Bài 57: Tìm phân số của một số - Đề số 1",
        "topic": "Tìm phân số của một số",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn tìm $\\frac{3}{5}$ của số 45, ta thực hiện phép tính nào?", 
                    ["$45 \\times \\frac{3}{5}$", "$45 : \\frac{3}{5}$", "$45 + \\frac{3}{5}$", "$45 - \\frac{3}{5}$"], 
                    0, "Quy tắc: Muốn tìm phân số của một số, ta lấy số đó nhân với phân số.", "NB"),
            make_mc(2, "Giá trị của $\\frac{2}{3}$ của 18 quả cam là:", 
                    ["12 quả cam", "6 quả cam", "9 quả cam", "27 quả cam"], 
                    0, "Ta có: $18 \\times \\frac{2}{3} = 12\\text{ (quả)}$.", "TH"),
            make_mc(3, "Tìm $\\frac{3}{4}$ của 60 phút được kết quả là:", 
                    ["45 phút", "15 phút", "20 phút", "50 phút"], 
                    0, "$60 \\times \\frac{3}{4} = 45\\text{ (phút)}$.", "TH"),
            make_mc(4, "Một lớp học có 35 học sinh, trong đó $\\frac{3}{7}$ số học sinh là học sinh nam. Số học sinh nam của lớp đó là:", 
                    ["15 học sinh", "20 học sinh", "12 học sinh", "21 học sinh"], 
                    0, "Số học sinh nam là: $35 \\times \\frac{3}{7} = 15\\text{ (học sinh)}$.", "VD"),
            make_mc(5, "Tìm $\\frac{5}{8}$ của $\\frac{16}{25}$ được phân số tối giản là:", 
                    ["$\\frac{2}{5}$", "$\\frac{10}{25}$", "$\\frac{80}{200}$", "$\\frac{1}{2}$"], 
                    0, "$\\frac{16}{25} \\times \\frac{5}{8} = \\frac{16 \\times 5}{25 \\times 8} = \\frac{2 \\times 1}{5 \\times 1} = \\frac{2}{5}$.", "TH"),
            make_mc(6, "Một thùng chứa 80 lít dầu, người ta đã lấy ra $\\frac{3}{10}$ số dầu đó. Số lít dầu đã lấy ra là:", 
                    ["$24\\text{ lít}$", "$56\\text{ lít}$", "$8\\text{ lít}$", "$30\\text{ lít}$"], 
                    0, "Số lít dầu lấy ra: $80 \\times \\frac{3}{10} = 24\\text{ (lít)}$.", "VD")
        ],
        "part2": [
            make_essay(1, "Tìm:\na) $\\frac{3}{7}$ của $42\\text{ kg}$\nb) $\\frac{5}{6}$ của $72\\text{ m}$",
                       "a) $\\frac{3}{7}$ của $42\\text{ kg}$ là: $42 \\times \\frac{3}{7} = 18\\text{ (kg)}$\nb) $\\frac{5}{6}$ của $72\\text{ m}$ là: $72 \\times \\frac{5}{6} = 60\\text{ (m)}$",
                       "a) 18 kg; b) 60 m", 4, 1.0, "TH"),
            make_essay(2, "Tính:\na) $\\frac{4}{9}$ của $\\frac{27}{32}$\nb) $\\frac{7}{10}$ của $150\\text{ lít}$",
                       "a) $\\frac{4}{9}$ của $\\frac{27}{32}$ là: $\\frac{27}{32} \\times \\frac{4}{9} = \\frac{27 \\times 4}{32 \\times 9} = \\frac{3}{8}$\nb) $\\frac{7}{10}$ của $150\\text{ lít}$ là: $150 \\times \\frac{7}{10} = 105\\text{ (lít)}$",
                       "a) 3/8; b) 105 lít", 4, 1.0, "TH"),
            make_essay(3, "Một rổ trứng có 48 quả trứng gà. Mẹ đã dùng $\\frac{3}{8}$ số quả trứng đó để làm bánh. Hỏi trong rổ còn lại bao nhiêu quả trứng gà?",
                       "Số quả trứng mẹ đã dùng để làm bánh là:\n$48 \\times \\frac{3}{8} = 18\\text{ (quả)}$\nTrong rổ còn lại số quả trứng gà là:\n$48 - 18 = 30\\text{ (quả)}$\nĐáp số: $30\\text{ quả trứng gà}$",
                       "30 quả trứng", 5, 1.0, "VD"),
            make_essay(4, "Một mảnh đất hình chữ nhật có chiều dài $24\\text{ m}$, chiều rộng bằng $\\frac{5}{8}$ chiều dài. Tính diện tích mảnh đất hình chữ nhật đó.",
                       "Chiều rộng của mảnh đất hình chữ nhật là:\n$24 \\times \\frac{5}{8} = 15\\text{ (m)}$\nDiện tích mảnh đất hình chữ nhật là:\n$24 \\times 15 = 360\\text{ (m}^2\\text{)}$\nĐáp số: $360\\text{ m}^2$",
                       "360 m^2", 5, 1.5, "VD"),
            make_essay(5, "Một cửa hàng nhập về $180\\text{ kg}$ gạo gồm gạo nếp và gạo tẻ. Trong đó số gạo nếp chiếm $\\frac{2}{5}$ tổng số gạo. Hỏi cửa hàng nhập về bao nhiêu ki-lô-gam gạo tẻ?",
                       "Cửa hàng nhập về số ki-lô-gam gạo nếp là:\n$180 \\times \\frac{2}{5} = 72\\text{ (kg)}$\nCửa hàng nhập về số ki-lô-gam gạo tẻ là:\n$180 - 72 = 108\\text{ (kg)}$\nĐáp số: $108\\text{ kg gạo tẻ}$",
                       "108 kg gạo tẻ", 5, 1.5, "VD"),
            make_essay(6, "Bạn Nam đọc một cuốn truyện dày 120 trang trong ba ngày. Ngày thứ nhất Nam đọc được $\\frac{1}{3}$ số trang sách. Ngày thứ hai Nam đọc được $\\frac{2}{5}$ số trang còn lại. Hỏi sau hai ngày Nam còn phải đọc bao nhiêu trang sách nữa thì xong cuốn truyện?",
                       "Ngày thứ nhất Nam đọc được số trang là:\n$120 \\times \\frac{1}{3} = 40\\text{ (trang)}$\nSố trang sách còn lại sau ngày thứ nhất là:\n$120 - 40 = 80\\text{ (trang)}$\nNgày thứ hai Nam đọc được số trang là:\n$80 \\times \\frac{2}{5} = 32\\text{ (trang)}$\nSau hai ngày Nam còn phải đọc số trang sách nữa là:\n$80 - 32 = 48\\text{ (trang)}$\nĐáp số: $48\\text{ trang}$",
                       "48 trang", 6, 1.0, "VDC")
        ]
    }

    # --- Bài 57 - Đề 2 ---
    exams["th4_b57_test2"] = {
        "id": "th4_b57_test2",
        "lessonId": "th4_b57",
        "lessonNum": 57,
        "testNum": 2,
        "title": "Bài 57: Tìm phân số của một số - Đề số 2",
        "topic": "Tìm phân số của một số",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tìm $\\frac{4}{5}$ của $100\\text{ kg}$ ta được kết quả là:", 
                    ["$80\\text{ kg}$", "$20\\text{ kg}$", "$25\\text{ kg}$", "$75\\text{ kg}$"], 
                    0, "$100 \\times \\frac{4}{5} = 80\\text{ (kg)}$.", "NB"),
            make_mc(2, "Một đội văn nghệ có 24 bạn, trong đó có $\\frac{5}{8}$ số bạn là nữ. Đội văn nghệ đó có bao nhiêu bạn nữ?", 
                    ["15 bạn", "9 bạn", "16 bạn", "12 bạn"], 
                    0, "Số bạn nữ: $24 \\times \\frac{5}{8} = 15\\text{ (bạn)}$.", "TH"),
            make_mc(3, "Đoạn đường dài $63\\text{ m}$, người ta đã rải nhựa được $\\frac{2}{7}$ đoạn đường. Đoạn đường đã rải nhựa dài:", 
                    ["$18\\text{ m}$", "$9\\text{ m}$", "$14\\text{ m}$", "$45\\text{ m}$"], 
                    0, "$63 \\times \\frac{2}{7} = 18\\text{ (m)}$.", "TH"),
            make_mc(4, "Một ngày có 24 giờ. Thời gian $\\frac{3}{8}$ của một ngày bằng bao nhiêu giờ?", 
                    ["9 giờ", "8 giờ", "6 giờ", "12 giờ"], 
                    0, "$24 \\times \\frac{3}{8} = 9\\text{ (giờ)}$.", "TH"),
            make_mc(5, "Một bình chứa $500\\text{ ml}$ sữa, bạn Mai uống hết $\\frac{3}{5}$ lượng sữa đó. Mai đã uống số mi-li-lít sữa là:", 
                    ["$300\\text{ ml}$", "$200\\text{ ml}$", "$100\\text{ ml}$", "$400\\text{ ml}$"], 
                    0, "Lượng sữa Mai uống: $500 \\times \\frac{3}{5} = 300\\text{ (ml)}$.", "VD"),
            make_mc(6, "Tìm $\\frac{2}{3}$ của phân số $\\frac{9}{10}$ ta được kết quả tối giản là:", 
                    ["$\\frac{3}{5}$", "$\\frac{18}{30}$", "$\\frac{6}{10}$", "$\\frac{1}{3}$"], 
                    0, "$\\frac{9}{10} \\times \\frac{2}{3} = \\frac{9 \\times 2}{10 \\times 3} = \\frac{3}{5}$.", "TH")
        ],
        "part2": [
            make_essay(1, "Tính:\na) $\\frac{4}{7}$ của số 56\nb) $\\frac{3}{5}$ của $85\\text{ lít}$",
                       "a) $\\frac{4}{7}$ của số 56 là: $56 \\times \\frac{4}{7} = 32$\nb) $\\frac{3}{5}$ của $85\\text{ lít}$ là: $85 \\times \\frac{3}{5} = 51\\text{ (lít)}$",
                       "a) 32; b) 51 lít", 4, 1.0, "TH"),
            make_essay(2, "Đổi các đơn vị đo sau:\na) $\\frac{2}{3}$ giờ = ... phút\nb) $\\frac{3}{4}$ tấn = ... kg",
                       "a) Vì 1 giờ = 60 phút nên: $60 \\times \\frac{2}{3} = 40\\text{ (phút)}$\nb) Vì 1 tấn = 1000 kg nên: $1000 \\times \\frac{3}{4} = 750\\text{ (kg)}$",
                       "a) 40 phút; b) 750 kg", 4, 1.0, "TH"),
            make_essay(3, "Một trang trại nuôi 150 con gà, trong đó số gà mái chiếm $\\frac{3}{5}$ tổng số gà. Hỏi trang trại đó nuôi bao nhiêu con gà trống?",
                       "Trang trại đó nuôi số con gà mái là:\n$150 \\times \\frac{3}{5} = 90\\text{ (con)}$\nTrang trại đó nuôi số con gà trống là:\n$150 - 90 = 60\\text{ (con)}$\nĐáp số: $60\\text{ con gà trống}$",
                       "60 con gà trống", 5, 1.0, "VD"),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chu vi $140\\text{ m}$, chiều dài là $45\\text{ m}$. Người ta dành $\\frac{1}{5}$ diện tích mảnh vườn để trồng hoa hồng. Tính diện tích phần đất trồng hoa hồng.",
                       "Nửa chu vi mảnh vườn hình chữ nhật là:\n$140 : 2 = 70\\text{ (m)}$\nChiều rộng mảnh vườn hình chữ nhật là:\n$70 - 45 = 25\\text{ (m)}$\nDiện tích cả mảnh vườn là:\n$45 \\times 25 = 1125\\text{ (m}^2\\text{)}$\nDiện tích đất trồng hoa hồng là:\n$1125 \\times \\frac{1}{5} = 225\\text{ (m}^2\\text{)}$\nĐáp số: $225\\text{ m}^2$",
                       "225 m^2", 6, 1.5, "VD"),
            make_essay(5, "Quãng đường từ nhà bạn Lan đến trường dài $1200\\text{ m}$. Lan đã đi bộ được $\\frac{2}{3}$ quãng đường đó thì dừng lại đợi bạn. Hỏi Lan còn phải đi tiếp bao nhiêu mét nữa thì tới trường?",
                       "Lan đã đi được số mét đường là:\n$1200 \\times \\frac{2}{3} = 800\\text{ (m)}$\nLan còn phải đi tiếp số mét nữa là:\n$1200 - 800 = 400\\text{ (m)}$\nĐáp số: $400\\text{ m}$",
                       "400 m", 5, 1.5, "VD"),
            make_essay(6, "Bác An thu hoạch được $240\\text{ kg}$ quả bưởi Da Xanh. Buổi sáng bác bán được $\\frac{3}{8}$ số bưởi đó. Buổi chiều bác bán được $\\frac{2}{5}$ số bưởi còn lại sau buổi sáng. Hỏi bác An còn lại bao nhiêu ki-lô-gam bưởi chưa bán?",
                       "Buổi sáng bác An bán được số ki-lô-gam bưởi là:\n$240 \\times \\frac{3}{8} = 90\\text{ (kg)}$\nSố ki-lô-gam bưởi còn lại sau buổi sáng là:\n$240 - 90 = 150\\text{ (kg)}$\nBuổi chiều bác An bán được số ki-lô-gam bưởi là:\n$150 \\times \\frac{2}{5} = 60\\text{ (kg)}$\nBác An còn lại số ki-lô-gam bưởi chưa bán là:\n$150 - 60 = 90\\text{ (kg)}$\nĐáp số: $90\\text{ kg bưởi}$",
                       "90 kg bưởi", 6, 1.0, "VDC")
        ]
    }

    # --- Bài 57 - Đề 3 ---
    exams["th4_b57_test3"] = {
        "id": "th4_b57_test3",
        "lessonId": "th4_b57",
        "lessonNum": 57,
        "testNum": 3,
        "title": "Bài 57: Tìm phân số của một số - Đề số 3",
        "topic": "Tìm phân số của một số",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một tuần lễ có 7 ngày. Phân số $\\frac{2}{7}$ của một tuần lễ tương ứng với:", 
                    ["2 ngày", "5 ngày", "3 ngày", "4 ngày"], 
                    0, "$7 \\times \\frac{2}{7} = 2\\text{ (ngày)}$.", "NB"),
            make_mc(2, "Tìm $\\frac{5}{9}$ của 72 chiếc bút chì màu:", 
                    ["40 chiếc bút", "35 chiếc bút", "45 chiếc bút", "36 chiếc bút"], 
                    0, "$72 \\times \\frac{5}{9} = 40\\text{ (chiếc)}$.", "TH"),
            make_mc(3, "Độ dài $\\frac{3}{4}$ của $200\\text{ m}$ là:", 
                    ["$150\\text{ m}$", "$50\\text{ m}$", "$100\\text{ m}$", "$75\\text{ m}$"], 
                    0, "$200 \\times \\frac{3}{4} = 150\\text{ (m)}$.", "TH"),
            make_mc(4, "Một bể nước có dung tích $1200\\text{ lít}$, hiện trong bể đang chứa lượng nước bằng $\\frac{5}{6}$ dung tích bể. Trong bể hiện có số lít nước là:", 
                    ["$1000\\text{ lít}$", "$200\\text{ lít}$", "$800\\text{ lít}$", "$1100\\text{ lít}$"], 
                    0, "Số lít nước trong bể: $1200 \\times \\frac{5}{6} = 1000\\text{ (lít)}$.", "VD"),
            make_mc(5, "Tìm $\\frac{4}{7}$ của phân số $\\frac{21}{32}$ ta được phân số tối giản là:", 
                    ["$\\frac{3}{8}$", "$\\frac{84}{224}$", "$\\frac{1}{2}$", "$\\frac{3}{4}$"], 
                    0, "$\\frac{21}{32} \\times \\frac{4}{7} = \\frac{21 \\times 4}{32 \\times 7} = \\frac{3 \\times 1}{8 \\times 1} = \\frac{3}{8}$.", "TH"),
            make_mc(6, "Lớp 4A có 32 học sinh, trong đó $\\frac{1}{4}$ số học sinh tham gia câu lạc bộ Cờ vua. Số học sinh tham gia cờ vua là:", 
                    ["8 học sinh", "6 học sinh", "10 học sinh", "12 học sinh"], 
                    0, "$32 \\times \\frac{1}{4} = 8\\text{ (học sinh)}$.", "NB")
        ],
        "part2": [
            make_essay(1, "Tính giá trị của:\na) $\\frac{5}{8}$ của số 64\nb) $\\frac{4}{11}$ của $88\\text{ kg}$",
                       "a) $\\frac{5}{8}$ của số 64 là: $64 \\times \\frac{5}{8} = 40$\nb) $\\frac{4}{11}$ của $88\\text{ kg}$ là: $88 \\times \\frac{4}{11} = 32\\text{ (kg)}$",
                       "a) 40; b) 32 kg", 4, 1.0, "TH"),
            make_essay(2, "Điền số thích hợp vào chỗ chấm:\na) $\\frac{7}{12}$ của 1 năm = ... tháng\nb) $\\frac{3}{5}$ của $1\\text{ km}$ = ... mét",
                       "a) 1 năm có 12 tháng nên: $12 \\times \\frac{7}{12} = 7\\text{ (tháng)}$\nb) $1\\text{ km} = 1000\\text{ m}$ nên: $1000 \\times \\frac{3}{5} = 600\\text{ (m)}$",
                       "a) 7 tháng; b) 600 m", 4, 1.0, "TH"),
            make_essay(3, "Một cửa hàng hoa nhập về 160 bông hoa hồng đỏ. Ngày lễ Tình nhân, cửa hàng đã bán được $\\frac{3}{10}$ số hoa đó. Hỏi cửa hàng còn lại bao nhiêu bông hoa hồng đỏ?",
                       "Cửa hàng đã bán được số bông hoa hồng đỏ là:\n$160 \\times \\frac{3}{10} = 48\\text{ (bông)}$\nCửa hàng còn lại số bông hoa hồng đỏ là:\n$160 - 48 = 112\\text{ (bông)}$\nĐáp số: $112\\text{ bông hoa hồng đỏ}$",
                       "112 bông hoa hồng", 5, 1.0, "VD"),
            make_essay(4, "Một thửa ruộng hình chữ nhật có chiều dài $60\\text{ m}$, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Người ta cấy lúa trên thửa ruộng đó, trung bình cứ $1\\text{ m}^2$ thu hoạch được $\\frac{3}{5}\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu ki-lô-gam thóc?",
                       "Chiều rộng của thửa ruộng hình chữ nhật là:\n$60 \\times \\frac{2}{3} = 40\\text{ (m)}$\nDiện tích thửa ruộng hình chữ nhật là:\n$60 \\times 40 = 2400\\text{ (m}^2\\text{)}$\nCả thửa ruộng thu hoạch được số ki-lô-gam thóc là:\n$2400 \\times \\frac{3}{5} = 1440\\text{ (kg)}$\nĐáp số: $1440\\text{ kg thóc}$",
                       "1440 kg thóc", 6, 1.5, "VD"),
            make_essay(5, "Một xe ô tô chở 75 tạ hàng cứu trợ vùng cao. Lần đầu xe dỡ xuống $\\frac{2}{5}$ số hàng. Lần sau xe dỡ xuống tiếp $\\frac{1}{3}$ số hàng ban đầu. Hỏi trên xe ô tô còn lại bao nhiêu tạ hàng cứu trợ?",
                       "Lần đầu xe dỡ xuống số tạ hàng là:\n$75 \\times \\frac{2}{5} = 30\\text{ (tạ)}$\nLần sau xe dỡ xuống số tạ hàng là:\n$75 \\times \\frac{1}{3} = 25\\text{ (tạ)}$\nTrên xe ô tô còn lại số tạ hàng cứu trợ là:\n$75 - (30 + 25) = 20\\text{ (tạ)}$\nĐáp số: $20\\text{ tạ hàng}$",
                       "20 tạ", 5, 1.5, "VD"),
            make_essay(6, "Ba bạn An, Bình, Chi cùng chia nhau một túi kẹo gồm 90 chiếc kẹo dẻo. An lấy $\\frac{2}{9}$ tổng số kẹo. Sau đó, Bình lấy $\\frac{2}{5}$ số kẹo còn lại trong túi. Số kẹo còn lại cuối cùng được dành cho Chi. Hỏi bạn Chi nhận được bao nhiêu chiếc kẹo?",
                       "Bạn An nhận được số chiếc kẹo là:\n$90 \\times \\frac{2}{9} = 20\\text{ (chiếc kẹo)}$\nSố chiếc kẹo còn lại trong túi sau khi An lấy là:\n$90 - 20 = 70\\text{ (chiếc kẹo)}$\nBạn Bình nhận được số chiếc kẹo là:\n$70 \\times \\frac{2}{5} = 28\\text{ (chiếc kẹo)}$\nBạn Chi nhận được số chiếc kẹo là:\n$70 - 28 = 42\\text{ (chiếc kẹo)}$\nĐáp số: $42\\text{ chiếc kẹo}$",
                       "42 chiếc kẹo", 6, 1.0, "VDC")
        ]
    }

    # =========================================================================
    # BÀI 58: LUYỆN TẬP CHUNG CHỦ ĐỀ 12
    # =========================================================================

    # --- Bài 58 - Đề 1 ---
    exams["th4_b58_test1"] = {
        "id": "th4_b58_test1",
        "lessonId": "th4_b58",
        "lessonNum": 58,
        "testNum": 1,
        "title": "Bài 58: Luyện tập chung Chủ đề 12 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 12",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của phép tính $\\frac{3}{8} \\times \\frac{4}{9} : \\frac{2}{3}$ là:", 
                    ["$\\frac{1}{4}$", "$\\frac{1}{6}$", "$\\frac{1}{9}$", "$\\frac{2}{3}$"], 
                    0, "$\\frac{3}{8} \\times \\frac{4}{9} = \\frac{1}{6}$; $\\frac{1}{6} : \\frac{2}{3} = \\frac{1}{6} \\times \\frac{3}{2} = \\frac{3}{12} = \\frac{1}{4}$.", "TH"),
            make_mc(2, "Tính giá trị biểu thức: $1 - \\frac{2}{5} \\times \\frac{5}{4}$:", 
                    ["$\\frac{1}{2}$", "$\\frac{3}{5}$", "0", "1"], 
                    0, "$1 - \\frac{2}{4} = 1 - \\frac{1}{2} = \\frac{1}{2}$.", "TH"),
            make_mc(3, "Phân số nào thích hợp điền vào chỗ chấm: $\\dots \\times \\frac{3}{7} = \\frac{6}{35}$?", 
                    ["$\\frac{2}{5}$", "$\\frac{5}{2}$", "$\\frac{18}{245}$", "$\\frac{3}{5}$"], 
                    0, "Số cần tìm: $\\frac{6}{35} : \\frac{3}{7} = \\frac{6}{35} \\times \\frac{7}{3} = \\frac{2}{5}$.", "TH"),
            make_mc(4, "Một mảnh vườn hình vuông có chu vi là $\\frac{8}{3}\\text{ m}$. Diện tích mảnh vườn đó là:", 
                    ["$\\frac{4}{9}\\text{ m}^2$", "$\\frac{16}{9}\\text{ m}^2$", "$\\frac{64}{9}\\text{ m}^2$", "$\\frac{2}{3}\\text{ m}^2$"], 
                    0, "Cạnh hình vuông: $\\frac{8}{3} : 4 = \\frac{2}{3}\\text{ (m)}$. Diện tích: $\\frac{2}{3} \\times \\frac{2}{3} = \\frac{4}{9}\\text{ m}^2$.", "VD"),
            make_mc(5, "Một lớp có 40 học sinh, trong đó $\\frac{3}{5}$ số học sinh đạt danh hiệu Học sinh Giỏi. Số học sinh đạt danh hiệu Học sinh Giỏi là:", 
                    ["24 học sinh", "20 học sinh", "16 học sinh", "28 học sinh"], 
                    0, "$40 \\times \\frac{3}{5} = 24\\text{ (học sinh)}$.", "TH"),
            make_mc(6, "Biểu thức nào có kết quả lớn nhất trong các biểu thức sau?", 
                    ["$\\frac{3}{4} \\times 2$", "$\\frac{3}{4} : 2$", "$\\frac{3}{4} + 2$", "$2 - \\frac{3}{4}$"], 
                    2, "$\\frac{3}{4} + 2 = \\frac{11}{4} = 2\\frac{3}{4}$; $\\frac{3}{4} \\times 2 = \\frac{3}{2} = 1\\frac{1}{2}$; $2 - \\frac{3}{4} = \\frac{5}{4} = 1\\frac{1}{4}$; $\\frac{3}{4} : 2 = \\frac{3}{8}$. Lớn nhất là phép cộng.", "VD")
        ],
        "part2": [
            make_essay(1, "Tính giá trị của các biểu thức sau:\na) $\\frac{5}{6} \\times \\frac{9}{10} + \\frac{1}{4}$\nb) $\\frac{7}{8} : \\frac{3}{4} - \\frac{5}{6}$",
                       "a) $\\frac{5}{6} \\times \\frac{9}{10} = \\frac{5 \\times 9}{6 \\times 10} = \\frac{3}{4}$. Biểu thức $= \\frac{3}{4} + \\frac{1}{4} = \\frac{4}{4} = 1$\nb) $\\frac{7}{8} : \\frac{3}{4} = \\frac{7}{8} \\times \\frac{4}{3} = \\frac{7}{6}$. Biểu thức $= \\frac{7}{6} - \\frac{5}{6} = \\frac{2}{6} = \\frac{1}{3}$",
                       "a) 1; b) 1/3", 4, 1.0, "TH"),
            make_essay(2, "Tính giá trị của biểu thức bằng cách thuận tiện nhất:\na) $\\frac{4}{7} \\times \\frac{5}{9} + \\frac{4}{7} \\times \\frac{4}{9}$\nb) $\\frac{13}{18} : \\frac{5}{7} - \\frac{7}{18} : \\frac{5}{7}$",
                       "a) $\\frac{4}{7} \\times \\left(\\frac{5}{9} + \\frac{4}{9}\\right) = \\frac{4}{7} \\times 1 = \\frac{4}{7}$\nb) $\\left(\\frac{13}{18} - \\frac{7}{18}\\right) : \\frac{5}{7} = \\frac{6}{18} : \\frac{5}{7} = \\frac{1}{3} \\times \\frac{7}{5} = \\frac{7}{15}$",
                       "a) 4/7; b) 7/15", 4, 1.0, "TH"),
            make_essay(3, "Tìm $x$:\na) $x \\times \\frac{3}{5} = \\frac{9}{20}$\nb) $x : \\frac{4}{7} = \\frac{21}{16}$",
                       "a) $x = \\frac{9}{20} : \\frac{3}{5} = \\frac{9}{20} \\times \\frac{5}{3} = \\frac{3}{4}$\nb) $x = \\frac{21}{16} \\times \\frac{4}{7} = \\frac{21 \\times 4}{16 \\times 7} = \\frac{3}{4}$",
                       "a) x = 3/4; b) x = 3/4", 4, 1.0, "VD"),
            make_essay(4, "Một mảnh đất hình chữ nhật có chu vi $60\\text{ m}$, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Tính diện tích của mảnh đất hình chữ nhật đó.",
                       "Nửa chu vi mảnh đất là:\n$60 : 2 = 30\\text{ (m)}$\nTổng số phần bằng nhau là:\n$2 + 3 = 5\\text{ (phần)}$\nChiều dài mảnh đất là:\n$30 : 5 \\times 3 = 18\\text{ (m)}$\nChiều rộng mảnh đất là:\n$30 - 18 = 12\\text{ (m)}$\nDiện tích mảnh đất là:\n$18 \\times 12 = 216\\text{ (m}^2\\text{)}$\nĐáp số: $216\\text{ m}^2$",
                       "216 m^2", 6, 1.5, "VD"),
            make_essay(5, "Một cửa hàng có $250\\text{ kg}$ đường. Ngày thứ nhất cửa hàng bán được $\\frac{2}{5}$ số đường đó. Ngày thứ hai cửa hàng bán được $\\frac{1}{2}$ số đường còn lại sau ngày thứ nhất. Hỏi sau hai ngày cửa hàng còn lại bao nhiêu ki-lô-gam đường?",
                       "Ngày thứ nhất cửa hàng bán được số ki-lô-gam đường là:\n$250 \\times \\frac{2}{5} = 100\\text{ (kg)}$\nSố đường còn lại sau ngày thứ nhất là:\n$250 - 100 = 150\\text{ (kg)}$\nNgày thứ hai cửa hàng bán được số ki-lô-gam đường là:\n$150 \\times \\frac{1}{2} = 75\\text{ (kg)}$\nSau hai ngày cửa hàng còn lại số ki-lô-gam đường là:\n$150 - 75 = 75\\text{ (kg)}$\nĐáp số: $75\\text{ kg đường}$",
                       "75 kg đường", 6, 1.5, "VD"),
            make_essay(6, "Tính nhanh giá trị của biểu thức sau:\n$T = \\left(1 - \\frac{1}{2}\\right) \\times \\left(1 - \\frac{1}{3}\\right) \\times \\left(1 - \\frac{1}{4}\\right) \\times \\left(1 - \\frac{1}{5}\\right)$",
                       "Ta tính giá trị trong từng ngoặc đơn:\n$T = \\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{3}{4} \\times \\frac{4}{5}$\nRút gọn các thừa số giống nhau ở tử số và mẫu số:\n$T = \\frac{1 \\times 2 \\times 3 \\times 4}{2 \\times 3 \\times 4 \\times 5} = \\frac{1}{5}$\nĐáp số: $\\frac{1}{5}$",
                       "1/5", 4, 1.0, "VDC")
        ]
    }

    # --- Bài 58 - Đề 2 ---
    exams["th4_b58_test2"] = {
        "id": "th4_b58_test2",
        "lessonId": "th4_b58",
        "lessonNum": 58,
        "testNum": 2,
        "title": "Bài 58: Luyện tập chung Chủ đề 12 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 12",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Tính: $\\frac{4}{7} : \\frac{8}{21} \\times \\frac{2}{3} = ?$", 
                    ["1", "$\\frac{4}{9}$", "$\\frac{1}{3}$", "$\\frac{3}{2}$"], 
                    0, "$\\frac{4}{7} : \\frac{8}{21} = \\frac{4}{7} \\times \\frac{21}{8} = \\frac{3}{2}$; $\\frac{3}{2} \\times \\frac{2}{3} = 1$.", "TH"),
            make_mc(2, "Giá trị của biểu thức $\\left(\\frac{1}{3} + \\frac{1}{4}\\right) \\times \\frac{12}{7}$ là:", 
                    ["1", "$\\frac{7}{12}$", "$\\frac{5}{7}$", "$\\frac{12}{7}$"], 
                    0, "$\\left(\\frac{4}{12} + \\frac{3}{12}\\right) \\times \\frac{12}{7} = \\frac{7}{12} \\times \\frac{12}{7} = 1$.", "TH"),
            make_mc(3, "Tìm $x$, biết: $x : \\frac{5}{6} = \\frac{18}{25}$:", 
                    ["$x = \\frac{3}{5}$", "$x = \\frac{25}{18}$", "$x = \\frac{1}{3}$", "$x = \\frac{5}{6}$"], 
                    0, "$x = \\frac{18}{25} \\times \\frac{5}{6} = \\frac{18 \\times 5}{25 \\times 6} = \\frac{3}{5}$.", "TH"),
            make_mc(4, "Một tấm kính hình thoi có hai đường chéo dài $\\frac{6}{5}\\text{ m}$ và $\\frac{5}{4}\\text{ m}$. Diện tích tấm kính đó là:", 
                    ["$\\frac{3}{4}\\text{ m}^2$", "$\\frac{3}{2}\\text{ m}^2$", "$\\frac{6}{4}\\text{ m}^2$", "$\\frac{15}{20}\\text{ m}^2$"], 
                    0, "Diện tích: $\\frac{1}{2} \\times \\frac{6}{5} \\times \\frac{5}{4} = \\frac{30}{40} = \\frac{3}{4}\\text{ m}^2$.", "VD"),
            make_mc(5, "Đoàn vận động viên có 45 người, trong đó số nữ chiếm $\\frac{4}{9}$ tổng số người. Số nam trong đoàn là:", 
                    ["25 người", "20 người", "30 người", "15 người"], 
                    0, "Số nữ: $45 \\times \\frac{4}{9} = 20\\text{ (người)}$. Số nam: $45 - 20 = 25\\text{ (người)}$.", "VD"),
            make_mc(6, "Tìm giá trị của $k$, biết: $\\frac{5}{12} \\times k = 0$:", 
                    ["$k = 0$", "$k = 1$", "$k = \\frac{12}{5}$", "$k = \\frac{5}{12}$"], 
                    0, "Mọi số nhân với 0 đều có kết quả bằng 0.", "NB")
        ],
        "part2": [
            make_essay(1, "Tính giá trị của các biểu thức sau:\na) $\\frac{8}{15} \\times \\frac{5}{12} + \\frac{7}{9}$\nb) $\\frac{9}{14} : \\frac{3}{7} - \\frac{5}{6}$",
                       "a) $\\frac{8}{15} \\times \\frac{5}{12} = \\frac{8 \\times 5}{15 \\times 12} = \\frac{2 \\times 1}{3 \\times 3} = \\frac{2}{9}$. Biểu thức $= \\frac{2}{9} + \\frac{7}{9} = \\frac{9}{9} = 1$\nb) $\\frac{9}{14} : \\frac{3}{7} = \\frac{9}{14} \\times \\frac{7}{3} = \\frac{3}{2} = \\frac{9}{6}$. Biểu thức $= \\frac{9}{6} - \\frac{5}{6} = \\frac{4}{6} = \\frac{2}{3}$",
                       "a) 1; b) 2/3", 4, 1.0, "TH"),
            make_essay(2, "Tính nhanh:\na) $\\frac{7}{15} \\times \\frac{8}{11} + \\frac{7}{15} \\times \\frac{3}{11}$\nb) $\\frac{19}{24} : \\frac{4}{9} - \\frac{7}{24} : \\frac{4}{9}$",
                       "a) $\\frac{7}{15} \\times \\left(\\frac{8}{11} + \\frac{3}{11}\\right) = \\frac{7}{15} \\times 1 = \\frac{7}{15}$\nb) $\\left(\\frac{19}{24} - \\frac{7}{24}\\right) : \\frac{4}{9} = \\frac{12}{24} \\times \\frac{9}{4} = \\frac{1}{2} \\times \\frac{9}{4} = \\frac{9}{8}$",
                       "a) 7/15; b) 9/8", 4, 1.0, "TH"),
            make_essay(3, "Tìm $x$:\na) $\\frac{5}{7} : x = \\frac{15}{28}$\nb) $x \\times \\frac{2}{3} = \\frac{8}{9} - \\frac{2}{9}$",
                       "a) $x = \\frac{5}{7} : \\frac{15}{28} = \\frac{5}{7} \\times \\frac{28}{15} = \\frac{1 \\times 4}{1 \\times 3} = \\frac{4}{3}$\nb) $x \\times \\frac{2}{3} = \\frac{6}{9} = \\frac{2}{3} \\Rightarrow x = \\frac{2}{3} : \\frac{2}{3} = 1$",
                       "a) x = 4/3; b) x = 1", 4, 1.0, "VD"),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chiều dài $30\\text{ m}$, chiều rộng bằng $\\frac{3}{5}$ chiều dài. Người ta dùng $\\frac{1}{3}$ diện tích mảnh vườn để đào ao nuôi cá. Tính diện tích phần ao nuôi cá đó.",
                       "Chiều rộng của mảnh vườn là:\n$30 \\times \\frac{3}{5} = 18\\text{ (m)}$\nDiện tích cả mảnh vườn hình chữ nhật là:\n$30 \\times 18 = 540\\text{ (m}^2\\text{)}$\nDiện tích phần ao nuôi cá là:\n$540 \\times \\frac{1}{3} = 180\\text{ (m}^2\\text{)}$\nĐáp số: $180\\text{ m}^2$",
                       "180 m^2", 5, 1.5, "VD"),
            make_essay(5, "Một kho lương thực có $360\\text{ tạ}$ thóc. Ngày thứ nhất kho xuất đi $\\frac{3}{8}$ số thóc đó. Ngày thứ hai kho xuất tiếp $\\frac{2}{5}$ số thóc còn lại sau ngày thứ nhất. Hỏi sau hai ngày kho lương thực còn lại bao nhiêu tạ thóc?",
                       "Ngày thứ nhất kho xuất đi số tạ thóc là:\n$360 \\times \\frac{3}{8} = 135\\text{ (tạ)}$\nSố tạ thóc còn lại sau ngày thứ nhất là:\n$360 - 135 = 225\\text{ (tạ)}$\nNgày thứ hai kho xuất đi số tạ thóc là:\n$225 \\times \\frac{2}{5} = 90\\text{ (tạ)}$\nSau hai ngày kho lương thực còn lại số tạ thóc là:\n$225 - 90 = 135\\text{ (tạ)}$\nĐáp số: $135\\text{ tạ thóc}$",
                       "135 tạ", 6, 1.5, "VD"),
            make_essay(6, "Tính giá trị biểu thức sau một cách thuận tiện:\n$S = \\left(1 - \\frac{1}{3}\\right) \\times \\left(1 - \\frac{1}{4}\\right) \\times \\left(1 - \\frac{1}{5}\\right) \\times \\left(1 - \\frac{1}{6}\\right)$",
                       "Ta thực hiện phép tính trong từng ngoặc đơn:\n$S = \\frac{2}{3} \\times \\frac{3}{4} \\times \\frac{4}{5} \\times \\frac{5}{6}$\nRút gọn các thừa số chung:\n$S = \\frac{2 \\times 3 \\times 4 \\times 5}{3 \\times 4 \\times 5 \\times 6} = \\frac{2}{6} = \\frac{1}{3}$\nĐáp số: $\\frac{1}{3}$",
                       "1/3", 4, 1.0, "VDC")
        ]
    }

    # --- Bài 58 - Đề 3 ---
    exams["th4_b58_test3"] = {
        "id": "th4_b58_test3",
        "lessonId": "th4_b58",
        "lessonNum": 58,
        "testNum": 3,
        "title": "Bài 58: Luyện tập chung Chủ đề 12 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 12",
        "chapter": "Chủ đề 12: Phép nhân, phép chia phân số",
        "grade": "4",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kết quả của biểu thức $\\frac{5}{8} : \\frac{5}{6} \\times \\frac{2}{3}$ là:", 
                    ["$\\frac{1}{2}$", "$\\frac{2}{3}$", "$\\frac{3}{4}$", "1"], 
                    0, "$\\frac{5}{8} \\times \\frac{6}{5} = \\frac{3}{4}$; $\\frac{3}{4} \\times \\frac{2}{3} = \\frac{2}{4} = \\frac{1}{2}$.", "TH"),
            make_mc(2, "Tính: $\\left(\\frac{5}{6} - \\frac{1}{2}\\right) \\times \\frac{9}{4} = ?$", 
                    ["$\\frac{3}{4}$", "$\\frac{1}{3}$", "$\\frac{9}{8}$", "$\\frac{1}{4}$"], 
                    0, "$\\left(\\frac{5}{6} - \\frac{3}{6}\\right) \\times \\frac{9}{4} = \\frac{2}{6} \\times \\frac{9}{4} = \\frac{1}{3} \\times \\frac{9}{4} = \\frac{3}{4}$.", "TH"),
            make_mc(3, "Tìm thừa số $y$, biết: $y \\times \\frac{4}{9} = \\frac{16}{27}$:", 
                    ["$y = \\frac{4}{3}$", "$y = \\frac{3}{4}$", "$y = \\frac{64}{243}$", "$y = \\frac{2}{3}$"], 
                    0, "$y = \\frac{16}{27} : \\frac{4}{9} = \\frac{16}{27} \\times \\frac{9}{4} = \\frac{4}{3}$.", "TH"),
            make_mc(4, "Một tấm thảm hình vuông có cạnh dài $\\frac{4}{5}\\text{ m}$. Chu vi tấm thảm đó là:", 
                    ["$\\frac{16}{5}\\text{ m}$", "$\\frac{16}{25}\\text{ m}$", "$\\frac{8}{5}\\text{ m}$", "$4\\text{ m}$"], 
                    0, "Chu vi hình vuông: $\\frac{4}{5} \\times 4 = \\frac{16}{5}\\text{ (m)}$.", "TH"),
            make_mc(5, "Một đàn gà có 60 con, trong đó số gà ri chiếm $\\frac{3}{4}$ cả đàn. Hỏi đàn gà đó có bao nhiêu con gà ri?", 
                    ["45 con", "15 con", "50 con", "30 con"], 
                    0, "$60 \\times \\frac{3}{4} = 45\\text{ (con)}$.", "NB"),
            make_mc(6, "So sánh hai giá trị: $A = \\frac{3}{5} \\times \\frac{5}{3}$ và $B = \\frac{7}{9} : \\frac{7}{9}$:", 
                    ["$A = B$", "$A > B$", "$A < B$", "Không thể so sánh"], 
                    0, "$A = 1$ và $B = 1$, do đó $A = B$.", "TH")
        ],
        "part2": [
            make_essay(1, "Thực hiện phép tính (kết quả là phân số tối giản):\na) $\\frac{9}{16} \\times \\frac{4}{15} + \\frac{7}{20}$\nb) $\\frac{15}{14} : \\frac{5}{7} - \\frac{2}{3}$",
                       "a) $\\frac{9}{16} \\times \\frac{4}{15} = \\frac{9 \\times 4}{16 \\times 15} = \\frac{3 \\times 1}{4 \\times 5} = \\frac{3}{20}$. Biểu thức $= \\frac{3}{20} + \\frac{7}{20} = \\frac{10}{20} = \\frac{1}{2}$\nb) $\\frac{15}{14} : \\frac{5}{7} = \\frac{15}{14} \\times \\frac{7}{5} = \\frac{3 \\times 1}{2 \\times 1} = \\frac{3}{2}$. Biểu thức $= \\frac{3}{2} - \\frac{2}{3} = \\frac{9}{6} - \\frac{4}{6} = \\frac{5}{6}$",
                       "a) 1/2; b) 5/6", 4, 1.0, "TH"),
            make_essay(2, "Tính bằng cách thuận tiện nhất:\na) $\\frac{5}{14} \\times \\frac{9}{13} + \\frac{5}{14} \\times \\frac{4}{13}$\nb) $\\frac{17}{21} : \\frac{5}{8} - \\frac{2}{21} : \\frac{5}{8}$",
                       "a) $\\frac{5}{14} \\times \\left(\\frac{9}{13} + \\frac{4}{13}\\right) = \\frac{5}{14} \\times 1 = \\frac{5}{14}$\nb) $\\left(\\frac{17}{21} - \\frac{2}{21}\\right) : \\frac{5}{8} = \\frac{15}{21} \\times \\frac{8}{5} = \\frac{5}{7} \\times \\frac{8}{5} = \\frac{8}{7}$",
                       "a) 5/14; b) 8/7", 4, 1.0, "TH"),
            make_essay(3, "Tìm $x$ biết:\na) $x : \\frac{3}{8} = \\frac{16}{21} \\times \\frac{7}{12}$\nb) $\\frac{4}{5} \\times x = \\frac{1}{2} + \\frac{3}{10}$",
                       "a) $x : \\frac{3}{8} = \\frac{16 \\times 7}{21 \\times 12} = \\frac{4 \\times 1}{3 \\times 3} = \\frac{4}{9} \\Rightarrow x = \\frac{4}{9} \\times \\frac{3}{8} = \\frac{12}{72} = \\frac{1}{6}$\nb) $\\frac{4}{5} \\times x = \\frac{5}{10} + \\frac{3}{10} = \\frac{8}{10} = \\frac{4}{5} \\Rightarrow x = \\frac{4}{5} : \\frac{4}{5} = 1$",
                       "a) x = 1/6; b) x = 1", 4, 1.0, "VD"),
            make_essay(4, "Một mảnh đất hình chữ nhật có chu vi $84\\text{ m}$, chiều rộng bằng $\\frac{3}{4}$ chiều dài. Tính diện tích mảnh đất hình chữ nhật đó.",
                       "Nửa chu vi mảnh đất là:\n$84 : 2 = 42\\text{ (m)}$\nTổng số phần bằng nhau là:\n$3 + 4 = 7\\text{ (phần)}$\nChiều dài mảnh đất là:\n$42 : 7 \\times 4 = 24\\text{ (m)}$\nChiều rộng mảnh đất là:\n$42 - 24 = 18\\text{ (m)}$\nDiện tích mảnh đất hình chữ nhật là:\n$24 \\times 18 = 432\\text{ (m}^2\\text{)}$\nĐáp số: $432\\text{ m}^2$",
                       "432 m^2", 6, 1.5, "VD"),
            make_essay(5, "Một cửa hàng bán gạo có $420\\text{ kg}$ gạo tám thơm. Buổi sáng cửa hàng bán được $\\frac{2}{7}$ số gạo đó. Buổi chiều bán được $\\frac{3}{5}$ số gạo còn lại sau buổi sáng. Hỏi sau cả ngày bán, cửa hàng còn lại bao nhiêu ki-lô-gam gạo tám thơm?",
                       "Buổi sáng cửa hàng bán được số ki-lô-gam gạo là:\n$420 \\times \\frac{2}{7} = 120\\text{ (kg)}$\nSố gạo còn lại sau buổi sáng là:\n$420 - 120 = 300\\text{ (kg)}$\nBuổi chiều cửa hàng bán được số ki-lô-gam gạo là:\n$300 \\times \\frac{3}{5} = 180\\text{ (kg)}$\nSau cả ngày bán, cửa hàng còn lại số ki-lô-gam gạo tám thơm là:\n$300 - 180 = 120\\text{ (kg)}$\nĐáp số: $120\\text{ kg gạo}$",
                       "120 kg gạo", 6, 1.5, "VD"),
            make_essay(6, "Tính giá trị của biểu thức bằng cách nhanh nhất:\n$H = \\left(1 + \\frac{1}{2}\\right) \\times \\left(1 + \\frac{1}{3}\\right) \\times \\left(1 + \\frac{1}{4}\\right) \\times \\left(1 + \\frac{1}{5}\\right)$",
                       "Ta tính kết quả trong từng ngoặc đơn:\n$H = \\frac{3}{2} \\times \\frac{4}{3} \\times \\frac{5}{4} \\times \\frac{6}{5}$\nNhận xét tử số của phân số trước triệt tiêu cho mẫu số của phân số sau liền kề:\n$H = \\frac{3 \\times 4 \\times 5 \\times 6}{2 \\times 3 \\times 4 \\times 5} = \\frac{6}{2} = 3$\nĐáp số: $3$",
                       "3", 4, 1.0, "VDC")
        ]
    }

    return exams
