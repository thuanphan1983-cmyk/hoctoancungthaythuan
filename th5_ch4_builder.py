# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 4: HÌNH PHẲNG VÀ HÌNH KHỐI (BÀI 22 ĐẾN BÀI 25) - TOÁN 5 KNTT
Gồm 4 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 22: Hình tam giác. Diện tích hình tam giác (th5_b22_test1, th5_b22_test2, th5_b22_test3)
- Bài 23: Hình thang. Diện tích hình thang (th5_b23_test1, th5_b23_test2, th5_b23_test3)
- Bài 24: Hình tròn. Chu vi và diện tích hình tròn (th5_b24_test1, th5_b24_test2, th5_b24_test3)
- Bài 25: Luyện tập chung Chủ đề 4 (th5_b25_test1, th5_b25_test2, th5_b25_test3)
Tổng cộng: 12 đề kiểm tra chất lượng cao, độc lập 100%.
"""

def make_mc(qid, question, options, correct, explanation):
    q_text = question if question.startswith(f"**Câu {qid}:** ") else f"**Câu {qid}:** {question}"
    return {
        "id": qid,
        "question": q_text,
        "options": options,
        "choices": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question, solution, answer, lineCount=4, points=1.0):
    p_text = question if question.startswith(f"**Bài {qid}:** ") else f"**Bài {qid}:** {question}"
    sol = solution if "Đáp số" in solution else f"{solution}\nĐáp số: {answer}."
    return {
        "id": qid,
        "question": p_text,
        "solution": sol,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_exams():
    exams = {}

    # =========================================================================
    # BÀI 22: HÌNH TAM GIÁC. DIỆN TÍCH HÌNH TAM GIÁC
    # =========================================================================

    # --- Bài 22 - Đề 1 ---
    exams["th5_b22_test1"] = {
        "id": "th5_b22_test1",
        "lessonId": "th5_b22",
        "lessonNum": 22,
        "testNum": 1,
        "title": "Bài 22: Hình tam giác. Diện tích hình tam giác - Đề số 1",
        "topic": "Hình tam giác. Diện tích hình tam giác",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Công thức tính diện tích hình tam giác có độ dài đáy $a$ và chiều cao $h$ (cùng đơn vị đo) là:", ["$S = a \\times h$", "$S = a \\times h : 2$", "$S = (a + h) : 2$", "$S = a \\times h \\times 2$"], 1, "Diện tích tam giác bằng độ dài đáy nhân chiều cao chia 2."),
            make_mc(2, "Một hình tam giác có độ dài đáy $12\\text{ cm}$ và chiều cao $8\\text{ cm}$. Diện tích của hình tam giác đó là:", ["$96\\text{ cm}^2$", "$48\\text{ cm}^2$", "$20\\text{ cm}^2$", "$40\\text{ cm}^2$"], 1, "$S = 12 \\times 8 : 2 = 48\\text{ cm}^2$."),
            make_mc(3, "Hình tam giác vuông có hai cạnh góc vuông dài $6\\text{ cm}$ và $8\\text{ cm}$. Diện tích của nó là:", ["$48\\text{ cm}^2$", "$24\\text{ cm}^2$", "$14\\text{ cm}^2$", "$28\\text{ cm}^2$"], 1, "$S = 6 \\times 8 : 2 = 24\\text{ cm}^2$."),
            make_mc(4, "Một tam giác có diện tích $30\\text{ cm}^2$, chiều cao $6\\text{ cm}$. Độ dài cạnh đáy tương ứng là:", ["5 cm", "10 cm", "15 cm", "20 cm"], 1, "Độ dài đáy là: $30 \\times 2 : 6 = 10\\text{ cm}$."),
            make_mc(5, "Đổi: $2,5\\text{ dm} = \\dots\\text{ cm}$:", ["25", "250", "0,25", "205"], 0, "$2,5\\text{ dm} = 25\\text{ cm}$."),
            make_mc(6, "Nếu tăng độ dài cạnh đáy của hình tam giác lên gấp đôi và giữ nguyên chiều cao thì diện tích tăng lên:", ["2 lần", "4 lần", "Không đổi", "8 lần"], 0, "Vì $S = a \\times h : 2$, khi $a$ tăng 2 lần thì $S$ tăng 2 lần.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích hình tam giác có:\na) Độ dài đáy $15\\text{ cm}$, chiều cao $8\\text{ cm}$.\nb) Độ dài đáy $3,6\\text{ m}$, chiều cao $2,5\\text{ m}$.", "a) $S = 15 \\times 8 : 2 = 60\\text{ (cm}^2)$\nb) $S = 3,6 \\times 2,5 : 2 = 4,5\\text{ (m}^2)$", "a) 60 cm²; b) 4,5 m²", 4, 1.0),
            make_essay(2, "Tính diện tích hình tam giác vuông có độ dài hai cạnh góc vuông là $4,5\\text{ dm}$ và $6\\text{ dm}$.", "Diện tích hình tam giác vuông là:\n$4,5 \\times 6 : 2 = 13,5\\text{ (dm}^2)$\nĐáp số: $13,5\\text{ dm}^2$.", "13,5 dm²", 4, 1.0),
            make_essay(3, "Một hình tam giác có diện tích $45\\text{ cm}^2$ và độ dài đáy là $12\\text{ cm}$. Tính chiều cao tương ứng với cạnh đáy đó.", "Chiều cao của hình tam giác là:\n$45 \\times 2 : 12 = 7,5\\text{ (cm)}$\nĐáp số: 7,5 cm.", "7,5 cm", 4, 1.0),
            make_essay(4, "Một mảnh đất hình tam giác có độ dài đáy là $28\\text{ m}$, chiều cao bằng $\\frac{3}{4}$ độ dài đáy.\na) Tính chiều cao của mảnh đất hình tam giác đó.\nb) Tính diện tích mảnh đất hình tam giác đó.", "Bài giải:\na) Chiều cao mảnh đất hình tam giác là:\n$28 \\times 3 : 4 = 21\\text{ (m)}$\nb) Diện tích mảnh đất là:\n$28 \\times 21 : 2 = 294\\text{ (m}^2)$\nĐáp số:\na) 21 m;\nb) $294\\text{ m}^2$.", "a) 21 m; b) 294 m²", 5, 1.5),
            make_essay(5, "Một chiếc khăn quàng đỏ hình tam giác có đáy dài $100\\text{ cm}$ và chiều cao tương ứng dài $30\\text{ cm}$.\na) Tính diện tích chiếc khăn quàng đỏ đó.\nb) Người ta may 50 chiếc khăn quàng đỏ như thế. Hỏi cần dùng ít nhất bao nhiêu mét vuông vải (không kể đường viền mép)?", "Bài giải:\na) Diện tích chiếc khăn quàng đỏ là:\n$100 \\times 30 : 2 = 1500\\text{ (cm}^2)$\nb) Diện tích vải cần dùng để may 50 chiếc khăn là:\n$1500 \\times 50 = 75\\,000\\text{ (cm}^2)$\nĐổi: $75\\,000\\text{ cm}^2 = 7,5\\text{ m}^2$.\nĐáp số:\na) $1500\\text{ cm}^2$;\nb) $7,5\\text{ m}^2$.", "a) 1500 cm²; b) 7,5 m²", 5, 1.5),
            make_essay(6, "Cho hình tam giác ABC có diện tích $60\\text{ cm}^2$. Trên cạnh BC lấy điểm M sao cho $BM = \\frac{1}{3} BC$. Tính diện tích hình tam giác ABM.", "Bài giải:\nHai tam giác ABM và ABC có chung đường cao hạ từ đỉnh A xuống đáy BC.\nĐáy $BM = \\frac{1}{3} BC$ nên diện tích tam giác ABM bằng $\\frac{1}{3}$ diện tích tam giác ABC.\nDiện tích tam giác ABM là:\n$60 \\times \\frac{1}{3} = 20\\text{ (cm}^2)$\nĐáp số: $20\\text{ cm}^2$.", "20 cm²", 5, 1.0)
        ]
    }

    # --- Bài 22 - Đề 2 ---
    exams["th5_b22_test2"] = {
        "id": "th5_b22_test2",
        "lessonId": "th5_b22",
        "lessonNum": 22,
        "testNum": 2,
        "title": "Bài 22: Hình tam giác. Diện tích hình tam giác - Đề số 2",
        "topic": "Hình tam giác. Diện tích hình tam giác",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hình tam giác có độ dài đáy $14\\text{ dm}$ và chiều cao $9\\text{ dm}$. Diện tích của nó là:", ["$126\\text{ dm}^2$", "$63\\text{ dm}^2$", "$46\\text{ dm}^2$", "$72\\text{ dm}^2$"], 1, "$S = 14 \\times 9 : 2 = 63\\text{ dm}^2$."),
            make_mc(2, "Một tam giác có đáy $1,8\\text{ m}$ và chiều cao $1,2\\text{ m}$. Diện tích tam giác là:", ["$1,08\\text{ m}^2$", "$2,16\\text{ m}^2$", "$3\\text{ m}^2$", "$1,5\\text{ m}^2$"], 0, "$S = 1,8 \\times 1,2 : 2 = 1,08\\text{ m}^2$."),
            make_mc(3, "Tam giác vuông có diện tích $20\\text{ cm}^2$, một cạnh góc vuông dài $5\\text{ cm}$. Cạnh góc vuông còn lại dài:", ["4 cm", "8 cm", "10 cm", "6 cm"], 1, "Cạnh còn lại: $20 \\times 2 : 5 = 8\\text{ cm}$."),
            make_mc(4, "Một hình tam giác có diện tích $54\\text{ cm}^2$, đáy dài $12\\text{ cm}$. Chiều cao của tam giác là:", ["4,5 cm", "9 cm", "8 cm", "6 cm"], 1, "Chiều cao: $54 \\times 2 : 12 = 9\\text{ cm}$."),
            make_mc(5, "Đổi: $45\\text{ cm} = \\dots\\text{ m}$:", ["4,5", "0,45", "0,045", "450"], 1, "$45\\text{ cm} = 0,45\\text{ m}$."),
            make_mc(6, "Cắt một hình chữ nhật kích thước $6\\text{ cm} \\times 4\\text{ cm}$ theo đường chéo, ta được hai hình tam giác có diện tích mỗi hình là:", ["$24\\text{ cm}^2$", "$12\\text{ cm}^2$", "$10\\text{ cm}^2$", "$16\\text{ cm}^2$"], 1, "$S = 6 \\times 4 : 2 = 12\\text{ cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích hình tam giác có:\na) Đáy $16\\text{ cm}$, chiều cao $11\\text{ cm}$.\nb) Đáy $4,2\\text{ dm}$, chiều cao $3,5\\text{ dm}$.", "a) $S = 16 \\times 11 : 2 = 88\\text{ (cm}^2)$\nb) $S = 4,2 \\times 3,5 : 2 = 7,35\\text{ (dm}^2)$", "a) 88 cm²; b) 7,35 dm²", 4, 1.0),
            make_essay(2, "Một lá cờ hình tam giác vuông có độ dài hai cạnh góc vuông là $25\\text{ cm}$ và $40\\text{ cm}$. Tính diện tích lá cờ đó.", "Diện tích lá cờ hình tam giác vuông là:\n$25 \\times 40 : 2 = 500\\text{ (cm}^2)$\nĐáp số: $500\\text{ cm}^2$.", "500 cm²", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình tam giác có diện tích $84\\text{ m}^2$, chiều cao đo được là $14\\text{ m}$. Tính độ dài cạnh đáy tương ứng của mảnh vườn đó.", "Độ dài cạnh đáy mảnh vườn là:\n$84 \\times 2 : 14 = 12\\text{ (m)}$\nĐáp số: 12 m.", "12 m", 4, 1.0),
            make_essay(4, "Một thửa ruộng hình tam giác có cạnh đáy dài $35\\text{ m}$, chiều cao kém cạnh đáy $11\\text{ m}$.\na) Tính diện tích thửa ruộng đó.\nb) Cứ mỗi $100\\text{ m}^2$ thu hoạch được $70\\text{ kg}$ thóc. Hỏi trên cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?", "Bài giải:\na) Chiều cao thửa ruộng là:\n$35 - 11 = 24\\text{ (m)}$\nDiện tích thửa ruộng là:\n$35 \\times 24 : 2 = 420\\text{ (m}^2)$\nb) Số ki-lô-gam thóc thu hoạch được là:\n$420 : 100 \\times 70 = 294\\text{ (kg)}$\nĐổi: $294\\text{ kg} = 2,94\\text{ tạ}$.\nĐáp số:\na) $420\\text{ m}^2$;\nb) $2,94\\text{ tạ thóc}$.", "a) 420 m²; b) 2,94 tạ", 5, 1.5),
            make_essay(5, "Người ta quét sơn một tấm biển quảng cáo hình tam giác có đáy $3,2\\text{ m}$ và chiều cao $1,8\\text{ m}$. Người ta sơn cả hai mặt của tấm biển đó.\na) Tính diện tích một mặt của tấm biển quảng cáo.\nb) Biết tiền công sơn mỗi mét vuông là $30\\,000$ đồng. Hỏi sơn tấm biển đó hết bao nhiêu tiền?", "Bài giải:\na) Diện tích một mặt của tấm biển là:\n$3,2 \\times 1,8 : 2 = 2,88\\text{ (m}^2)$\nb) Diện tích cần sơn cả hai mặt là:\n$2,88 \\times 2 = 5,76\\text{ (m}^2)$\nSố tiền sơn tấm biển là:\n$5,76 \\times 30\\,000 = 172\\,800\\text{ (đồng)}$\nĐáp số:\na) $2,88\\text{ m}^2$;\nb) $172\\,800\\text{ đồng}$.", "a) 2,88 m²; b) 172 800 đồng", 5, 1.5),
            make_essay(6, "Cho hình tam giác ABC. Kéo dài cạnh đáy BC về phía C một đoạn CD dài $4\\text{ cm}$ thì diện tích tam giác tăng thêm $18\\text{ cm}^2$. Biết cạnh đáy BC dài $12\\text{ cm}$. Tính diện tích tam giác ABC ban đầu.", "Bài giải:\nTam giác ACD có đáy $CD = 4\\text{ cm}$ và diện tích $18\\text{ cm}^2$.\nChiều cao hạ từ đỉnh A xuống đáy BC là:\n$18 \\times 2 : 4 = 9\\text{ (cm)}$\nDiện tích hình tam giác ABC ban đầu là:\n$12 \\times 9 : 2 = 54\\text{ (cm}^2)$\nĐáp số: $54\\text{ cm}^2$.", "54 cm²", 5, 1.0)
        ]
    }

    # --- Bài 22 - Đề 3 ---
    exams["th5_b22_test3"] = {
        "id": "th5_b22_test3",
        "lessonId": "th5_b22",
        "lessonNum": 22,
        "testNum": 3,
        "title": "Bài 22: Hình tam giác. Diện tích hình tam giác - Đề số 3",
        "topic": "Hình tam giác. Diện tích hình tam giác",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình tam giác có đáy $18\\text{ cm}$, chiều cao $10\\text{ cm}$. Diện tích là:", ["$180\\text{ cm}^2$", "$90\\text{ cm}^2$", "$45\\text{ cm}^2$", "$100\\text{ cm}^2$"], 1, "$S = 18 \\times 10 : 2 = 90\\text{ cm}^2$."),
            make_mc(2, "Một hình tam giác vuông có hai cạnh góc vuông là $5\\text{ dm}$ và $12\\text{ dm}$. Diện tích của nó là:", ["$60\\text{ dm}^2$", "$30\\text{ dm}^2$", "$17\\text{ dm}^2$", "$34\\text{ dm}^2$"], 1, "$S = 5 \\times 12 : 2 = 30\\text{ dm}^2$."),
            make_mc(3, "Diện tích tam giác có đáy $2,4\\text{ m}$ và chiều cao $1,5\\text{ m}$ là:", ["$3,6\\text{ m}^2$", "$1,8\\text{ m}^2$", "$7,2\\text{ m}^2$", "$2\\text{ m}^2$"], 1, "$S = 2,4 \\times 1,5 : 2 = 1,8\\text{ m}^2$."),
            make_mc(4, "Một tam giác có diện tích $40\\text{ cm}^2$, chiều cao $8\\text{ cm}$. Cạnh đáy là:", ["5 cm", "10 cm", "12 cm", "15 cm"], 1, "Đáy là $40 \\times 2 : 8 = 10\\text{ cm}$."),
            make_mc(5, "Nếu giảm chiều cao hình tam giác đi một nửa và giữ nguyên đáy thì diện tích tam giác sẽ:", ["Giảm đi một nửa", "Giảm đi 4 lần", "Không đổi", "Tăng gấp đôi"], 0, "Diện tích tỉ lệ thuận với chiều cao nên giảm đi một nửa."),
            make_mc(6, "Một tấm bìa tam giác có đáy $16\\text{ cm}$ và chiều cao $7,5\\text{ cm}$. Diện tích tấm bìa là:", ["$120\\text{ cm}^2$", "$60\\text{ cm}^2$", "$80\\text{ cm}^2$", "$45\\text{ cm}^2$"], 1, "$S = 16 \\times 7,5 : 2 = 60\\text{ cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích hình tam giác có:\na) Đáy $24\\text{ cm}$, chiều cao $15\\text{ cm}$.\nb) Đáy $5\\text{ m}$, chiều cao $3,4\\text{ m}$.", "a) $S = 24 \\times 15 : 2 = 180\\text{ (cm}^2)$\nb) $S = 5 \\times 3,4 : 2 = 8,5\\text{ (m}^2)$", "a) 180 cm²; b) 8,5 m²", 4, 1.0),
            make_essay(2, "Tính diện tích hình tam giác có đáy $2,5\\text{ dm}$ và chiều cao $18\\text{ cm}$. (Viết kết quả theo xăng-ti-mét vuông).", "Đổi: $2,5\\text{ dm} = 25\\text{ cm}$.\nDiện tích tam giác là:\n$25 \\times 18 : 2 = 225\\text{ (cm}^2)$\nĐáp số: $225\\text{ cm}^2$.", "225 cm²", 4, 1.0),
            make_essay(3, "Một mảnh đất hình tam giác có diện tích $75\\text{ m}^2$, cạnh đáy dài $15\\text{ m}$. Tính chiều cao tương ứng với cạnh đáy đó.", "Chiều cao của mảnh đất hình tam giác là:\n$75 \\times 2 : 15 = 10\\text{ (m)}$\nĐáp số: 10 m.", "10 m", 4, 1.0),
            make_essay(4, "Một mảnh đất hình tam giác vuông có hai cạnh góc vuông là $30\\text{ m}$ và $40\\text{ m}$. Cạnh huyền đối diện góc vuông dài $50\\text{ m}$.\na) Tính diện tích mảnh đất đó.\nb) Tính chiều cao hạ từ đỉnh góc vuông xuống cạnh huyền.", "Bài giải:\na) Diện tích mảnh đất hình tam giác vuông là:\n$30 \\times 40 : 2 = 600\\text{ (m}^2)$\nb) Chiều cao hạ từ góc vuông xuống cạnh huyền là:\n$600 \\times 2 : 50 = 24\\text{ (m)}$\nĐáp số:\na) $600\\text{ m}^2$;\nb) 24 m.", "a) 600 m²; b) 24 m", 5, 1.5),
            make_essay(5, "Một khu vườn hình chữ nhật có chiều dài $24\\text{ m}$, chiều rộng $16\\text{ m}$. Người ta ngăn một góc vườn thành một khu đất hình tam giác có đáy $10\\text{ m}$ và chiều cao $8\\text{ m}$ để trồng hoa, diện tích còn lại trồng rau.\na) Tính diện tích phần đất trồng hoa.\nb) Tính diện tích phần đất trồng rau.", "Bài giải:\na) Diện tích phần đất trồng hoa là:\n$10 \\times 8 : 2 = 40\\text{ (m}^2)$\nb) Diện tích toàn bộ khu vườn là:\n$24 \\times 16 = 384\\text{ (m}^2)$\nDiện tích phần đất trồng rau là:\n$384 - 40 = 344\\text{ (m}^2)$\nĐáp số:\na) $40\\text{ m}^2$;\nb) $344\\text{ m}^2$.", "a) 40 m²; b) 344 m²", 5, 1.5),
            make_essay(6, "Cho tam giác ABC có diện tích $90\\text{ cm}^2$. Điểm M là trung điểm của cạnh BC. Tính diện tích hình tam giác ABM.", "Bài giải:\nHai tam giác ABM và ACM có chung chiều cao hạ từ đỉnh A xuống đáy BC và có đáy $BM = MC = \\frac{1}{2} BC$.\nDo đó, diện tích tam giác ABM bằng một nửa diện tích tam giác ABC:\n$S_{ABM} = 90 : 2 = 45\\text{ (cm}^2)$\nĐáp số: $45\\text{ cm}^2$.", "45 cm²", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 23: HÌNH THANG. DIỆN TÍCH HÌNH THANG
    # =========================================================================

    # --- Bài 23 - Đề 1 ---
    exams["th5_b23_test1"] = {
        "id": "th5_b23_test1",
        "lessonId": "th5_b23",
        "lessonNum": 23,
        "testNum": 1,
        "title": "Bài 23: Hình thang. Diện tích hình thang - Đề số 1",
        "topic": "Hình thang. Diện tích hình thang",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Công thức tính diện tích hình thang có hai đáy $a, b$ và chiều cao $h$ (cùng đơn vị đo) là:", ["$S = (a + b) \\times h$", "$S = (a + b) \\times h : 2$", "$S = a \\times b \\times h : 2$", "$S = (a + b) : 2$"], 1, "Diện tích hình thang bằng tổng hai đáy nhân chiều cao rồi chia cho 2."),
            make_mc(2, "Một hình thang có đáy lớn $10\\text{ cm}$, đáy bé $6\\text{ cm}$, chiều cao $5\\text{ cm}$. Diện tích của nó là:", ["$80\\text{ cm}^2$", "$40\\text{ cm}^2$", "$30\\text{ cm}^2$", "$50\\text{ cm}^2$"], 1, "$S = (10 + 6) \\times 5 : 2 = 40\\text{ cm}^2$."),
            make_mc(3, "Hình thang có đặc điểm gì?", ["Có hai cặp cạnh đối diện song song", "Có một cặp cạnh đối diện song song", "Có 4 góc vuông", "Có 4 cạnh bằng nhau"], 1, "Hình thang có một cặp cạnh đối diện song song (gọi là hai đáy)."),
            make_mc(4, "Một hình thang có diện tích $60\\text{ cm}^2$, chiều cao $6\\text{ cm}$. Tổng độ dài hai đáy của nó là:", ["10 cm", "20 cm", "30 cm", "15 cm"], 1, "Tổng hai đáy là: $60 \\times 2 : 6 = 20\\text{ cm}$."),
            make_mc(5, "Hình thang vuông là hình thang có:", ["Hai cạnh bên bằng nhau", "Một cạnh bên vuông góc với hai đáy", "Bốn góc vuông", "Hai đường chéo bằng nhau"], 1, "Hình thang vuông có một cạnh bên vuông góc với hai đáy (chính là chiều cao)."),
            make_mc(6, "Đáy lớn $1,2\\text{ m}$, đáy bé $0,8\\text{ m}$, chiều cao $0,5\\text{ m}$. Diện tích hình thang là:", ["$1\\text{ m}^2$", "$0,5\\text{ m}^2$", "$2\\text{ m}^2$", "$0,8\\text{ m}^2$"], 1, "$S = (1,2 + 0,8) \\times 0,5 : 2 = 0,5\\text{ m}^2$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích hình thang có:\na) Đáy lớn $14\\text{ cm}$, đáy bé $8\\text{ cm}$, chiều cao $6\\text{ cm}$.\nb) Đáy lớn $3,5\\text{ m}$, đáy bé $2,5\\text{ m}$, chiều cao $1,8\\text{ m}$.", "a) $S = (14 + 8) \\times 6 : 2 = 66\\text{ (cm}^2)$\nb) $S = (3,5 + 2,5) \\times 1,8 : 2 = 5,4\\text{ (m}^2)$", "a) 66 cm²; b) 5,4 m²", 4, 1.0),
            make_essay(2, "Một hình thang có tổng độ dài hai đáy là $25\\text{ dm}$, chiều cao là $12\\text{ dm}$. Tính diện tích hình thang đó.", "Diện tích hình thang là:\n$25 \\times 12 : 2 = 150\\text{ (dm}^2)$\nĐáp số: $150\\text{ dm}^2$.", "150 dm²", 4, 1.0),
            make_essay(3, "Một hình thang có diện tích là $90\\text{ cm}^2$, chiều cao là $9\\text{ cm}$. Đáy lớn hơn đáy bé $4\\text{ cm}$. Tính độ dài đáy lớn và đáy bé của hình thang.", "Tổng độ dài hai đáy là:\n$90 \\times 2 : 9 = 20\\text{ (cm)}$\nĐộ dài đáy lớn là:\n$(20 + 4) : 2 = 12\\text{ (cm)}$\nĐộ dài đáy bé là:\n$20 - 12 = 8\\text{ (cm)}$\nĐáp số: Đáy lớn 12 cm, Đáy bé 8 cm.", "Đáy lớn 12 cm; Đáy bé 8 cm", 4, 1.0),
            make_essay(4, "Một thửa ruộng hình thang có đáy lớn $40\\text{ m}$, đáy bé bằng $\\frac{3}{5}$ đáy lớn, chiều cao bằng $20\\text{ m}$.\na) Tính diện tích thửa ruộng hình thang đó.\nb) Người ta cấy lúa trên thửa ruộng đó, cứ $100\\text{ m}^2$ thu được $65\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?", "Bài giải:\na) Độ dài đáy bé của thửa ruộng là:\n$40 \\times 3 : 5 = 24\\text{ (m)}$\nDiện tích thửa ruộng hình thang là:\n$(40 + 24) \\times 20 : 2 = 640\\text{ (m}^2)$\nb) Số ki-lô-gam thóc thu được là:\n$640 : 100 \\times 65 = 416\\text{ (kg)}$\nĐổi: $416\\text{ kg} = 4,16\\text{ tạ}$.\nĐáp số:\na) $640\\text{ m}^2$;\nb) $4,16\\text{ tạ thóc}$.", "a) 640 m²; b) 4,16 tạ", 5, 1.5),
            make_essay(5, "Một mảnh đất hình thang có đáy lớn $32\\text{ m}$, đáy bé $18\\text{ m}$. Người ta mở rộng đáy lớn thêm $5\\text{ m}$ thì diện tích mảnh đất tăng thêm $45\\text{ m}^2$.\na) Tính chiều cao của mảnh đất hình thang đó.\nb) Tính diện tích mảnh đất hình thang ban đầu.", "Bài giải:\na) Diện tích tăng thêm chính là diện tích tam giác có đáy $5\\text{ m}$ và chiều cao bằng chiều cao hình thang.\nChiều cao của mảnh đất là:\n$45 \\times 2 : 5 = 18\\text{ (m)}$\nb) Diện tích mảnh đất hình thang ban đầu là:\n$(32 + 18) \\times 18 : 2 = 450\\text{ (m}^2)$\nĐáp số:\na) 18 m;\nb) $450\\text{ m}^2$.", "a) 18 m; b) 450 m²", 5, 1.5),
            make_essay(6, "Cho hình thang vuông ABCD (vuông tại A và D) có $AB = 4\\text{ cm}, CD = 9\\text{ cm}, AD = 6\\text{ cm}$. Nối B với D, chia hình thang thành hai tam giác ABD và BCD. Tính diện tích hình tam giác BCD.", "Bài giải:\nDiện tích hình thang ABCD là:\n$(4 + 9) \\times 6 : 2 = 39\\text{ (cm}^2)$\nDiện tích hình tam giác vuông ABD là:\n$4 \\times 6 : 2 = 12\\text{ (cm}^2)$\nDiện tích hình tam giác BCD là:\n$39 - 12 = 27\\text{ (cm}^2)$\nĐáp số: $27\\text{ cm}^2$.", "27 cm²", 5, 1.0)
        ]
    }

    # --- Bài 23 - Đề 2 ---
    exams["th5_b23_test2"] = {
        "id": "th5_b23_test2",
        "lessonId": "th5_b23",
        "lessonNum": 23,
        "testNum": 2,
        "title": "Bài 23: Hình thang. Diện tích hình thang - Đề số 2",
        "topic": "Hình thang. Diện tích hình thang",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình thang có đáy lớn $15\\text{ cm}$, đáy bé $9\\text{ cm}$ và chiều cao $8\\text{ cm}$. Diện tích của nó là:", ["$192\\text{ cm}^2$", "$96\\text{ cm}^2$", "$120\\text{ cm}^2$", "$108\\text{ cm}^2$"], 1, "$S = (15 + 9) \\times 8 : 2 = 96\\text{ cm}^2$."),
            make_mc(2, "Trung bình cộng hai đáy của một hình thang là $12\\text{ cm}$, chiều cao là $7\\text{ cm}$. Diện tích hình thang là:", ["$42\\text{ cm}^2$", "$84\\text{ cm}^2$", "$168\\text{ cm}^2$", "$96\\text{ cm}^2$"], 1, "$S = 12 \\times 7 = 84\\text{ cm}^2$."),
            make_mc(3, "Hình thang có đáy lớn $2\\text{ m}$, đáy bé $1,5\\text{ m}$, chiều cao $0,8\\text{ m}$. Diện tích là:", ["$1,4\\text{ m}^2$", "$2,8\\text{ m}^2$", "$1,6\\text{ m}^2$", "$2,1\\text{ m}^2$"], 0, "$S = (2 + 1,5) \\times 0,8 : 2 = 1,4\\text{ m}^2$."),
            make_mc(4, "Một hình thang có diện tích $48\\text{ cm}^2$, tổng hai đáy là $16\\text{ cm}$. Chiều cao của nó là:", ["3 cm", "6 cm", "8 cm", "4 cm"], 1, "$h = 48 \\times 2 : 16 = 6\\text{ cm}$."),
            make_mc(5, "Đổi: $1,5\\text{ m} = \\dots\\text{ dm}$:", ["15", "150", "0,15", "105"], 0, "$1,5\\text{ m} = 15\\text{ dm}$."),
            make_mc(6, "Cắt một hình thang thành một hình chữ nhật và hai hình tam giác. Tổng diện tích của ba hình đó:", ["Lớn hơn diện tích hình thang", "Bé hơn diện tích hình thang", "Bằng diện tích hình thang", "Không xác định"], 2, "Tổng diện tích các phần bằng diện tích hình thang ban đầu.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích hình thang có:\na) Đáy lớn $20\\text{ cm}$, đáy bé $12\\text{ cm}$, chiều cao $7\\text{ cm}$.\nb) Đáy lớn $4,8\\text{ m}$, đáy bé $3,2\\text{ m}$, chiều cao $2,5\\text{ m}$.", "a) $S = (20 + 12) \\times 7 : 2 = 112\\text{ (cm}^2)$\nb) $S = (4,8 + 3,2) \\times 2,5 : 2 = 10\\text{ (m}^2)$", "a) 112 cm²; b) 10 m²", 4, 1.0),
            make_essay(2, "Một hình thang có diện tích $72\\text{ dm}^2$, chiều cao $8\\text{ dm}$. Tính trung bình cộng hai đáy của hình thang đó.", "Tổng hai đáy là: $72 \\times 2 : 8 = 18\\text{ (dm)}$.\nTrung bình cộng hai đáy là:\n$18 : 2 = 9\\text{ (dm)}$\nĐáp số: 9 dm.", "9 dm", 4, 1.0),
            make_essay(3, "Một mảnh đất hình thang có đáy lớn $24\\text{ m}$, đáy bé $16\\text{ m}$, chiều cao bằng một nửa đáy lớn. Tính diện tích mảnh đất đó.", "Chiều cao mảnh đất là:\n$24 : 2 = 12\\text{ (m)}$\nDiện tích mảnh đất là:\n$(24 + 16) \\times 12 : 2 = 240\\text{ (m}^2)$\nĐáp số: $240\\text{ m}^2$.", "240 m²", 4, 1.0),
            make_essay(4, "Một thửa ruộng hình thang có diện tích $800\\text{ m}^2$, chiều cao $20\\text{ m}$. Đáy lớn hơn đáy bé $10\\text{ m}$.\na) Tính tổng độ dài hai đáy của thửa ruộng.\nb) Tính độ dài đáy lớn và đáy bé của thửa ruộng đó.", "Bài giải:\na) Tổng độ dài hai đáy của thửa ruộng là:\n$800 \\times 2 : 20 = 80\\text{ (m)}$\nb) Độ dài đáy lớn là:\n$(80 + 10) : 2 = 45\\text{ (m)}$\nĐộ dài đáy bé là:\n$80 - 45 = 35\\text{ (m)}$\nĐáp số:\na) 80 m;\nb) Đáy lớn: 45 m; Đáy bé: 35 m.", "a) 80 m; b) Đáy lớn 45 m, đáy bé 35 m", 5, 1.5),
            make_essay(5, "Một khu đất hình thang có đáy lớn $50\\text{ m}$, đáy bé $30\\text{ m}$, chiều cao $25\\text{ m}$. Người ta dùng $30\\%$ diện tích để đào ao thả cá, diện tích còn lại trồng cây ăn quả.\na) Tính diện tích khu đất hình thang đó.\nb) Tính diện tích phần đất dùng để trồng cây ăn quả.", "Bài giải:\na) Diện tích khu đất hình thang là:\n$(50 + 30) \\times 25 : 2 = 1000\\text{ (m}^2)$\nb) Tỉ số phần trăm diện tích trồng cây ăn quả là:\n$100\\% - 30\\% = 70\\%$\nDiện tích phần đất trồng cây ăn quả là:\n$1000 \\times 70 : 100 = 700\\text{ (m}^2)$\nĐáp số:\na) $1000\\text{ m}^2$;\nb) $700\\text{ m}^2$.", "a) 1000 m²; b) 700 m²", 5, 1.5),
            make_essay(6, "Một hình thang có đáy bé $15\\text{ cm}$, đáy lớn $25\\text{ cm}$. Nếu kéo dài đáy lớn thêm $5\\text{ cm}$ thì diện tích hình thang tăng thêm $30\\text{ cm}^2$. Tính diện tích hình thang ban đầu.", "Bài giải:\nChiều cao hình thang là:\n$30 \\times 2 : 5 = 12\\text{ (cm)}$\nDiện tích hình thang ban đầu là:\n$(15 + 25) \\times 12 : 2 = 240\\text{ (cm}^2)$\nĐáp số: $240\\text{ cm}^2$.", "240 cm²", 5, 1.0)
        ]
    }

    # --- Bài 23 - Đề 3 ---
    exams["th5_b23_test3"] = {
        "id": "th5_b23_test3",
        "lessonId": "th5_b23",
        "lessonNum": 23,
        "testNum": 3,
        "title": "Bài 23: Hình thang. Diện tích hình thang - Đề số 3",
        "topic": "Hình thang. Diện tích hình thang",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình thang có đáy lớn $18\\text{ cm}$, đáy bé $12\\text{ cm}$, chiều cao $9\\text{ cm}$. Diện tích của nó là:", ["$270\\text{ cm}^2$", "$135\\text{ cm}^2$", "$150\\text{ cm}^2$", "$162\\text{ cm}^2$"], 1, "$S = (18 + 12) \\times 9 : 2 = 135\\text{ cm}^2$."),
            make_mc(2, "Đáy lớn $3\\text{ m}$, đáy bé $2\\text{ m}$, chiều cao $1,5\\text{ m}$. Diện tích hình thang là:", ["$3,75\\text{ m}^2$", "$7,5\\text{ m}^2$", "$4,5\\text{ m}^2$", "$5\\text{ m}^2$"], 0, "$S = (3 + 2) \\times 1,5 : 2 = 3,75\\text{ m}^2$."),
            make_mc(3, "Một hình thang có diện tích $80\\text{ cm}^2$, tổng hai đáy là $20\\text{ cm}$. Chiều cao của hình thang là:", ["4 cm", "8 cm", "10 cm", "16 cm"], 1, "$h = 80 \\times 2 : 20 = 8\\text{ cm}$."),
            make_mc(4, "Một mảnh đất hình thang có đáy lớn $16\\text{ m}$, đáy bé $10\\text{ m}$. Trung bình cộng hai đáy là:", ["12 m", "13 m", "14 m", "15 m"], 1, "$(16 + 10) : 2 = 13\\text{ m}$."),
            make_mc(5, "Nếu gấp đôi cả hai đáy và chiều cao của hình thang thì diện tích tăng lên:", ["2 lần", "4 lần", "6 lần", "8 lần"], 1, "Tổng hai đáy tăng 2 lần, chiều cao tăng 2 lần nên diện tích tăng $2 \\times 2 = 4$ lần."),
            make_mc(6, "Hình thang cân là hình thang có:", ["Hai cạnh đáy vuông góc", "Hai cạnh bên bằng nhau", "Bốn cạnh bằng nhau", "Hai góc tù"], 1, "Hình thang cân có hai cạnh bên bằng nhau và hai góc kề một đáy bằng nhau.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích hình thang có:\na) Đáy lớn $22\\text{ cm}$, đáy bé $14\\text{ cm}$, chiều cao $8\\text{ cm}$.\nb) Đáy lớn $5,4\\text{ m}$, đáy bé $3,6\\text{ m}$, chiều cao $2\\text{ m}$.", "a) $S = (22 + 14) \\times 8 : 2 = 144\\text{ (cm}^2)$\nb) $S = (5,4 + 3,6) \\times 2 : 2 = 9\\text{ (m}^2)$", "a) 144 cm²; b) 9 m²", 4, 1.0),
            make_essay(2, "Một hình thang có đáy bé $8\\text{ cm}$, đáy lớn gấp đôi đáy bé, chiều cao $6\\text{ cm}$. Tính diện tích hình thang đó.", "Đáy lớn là: $8 \\times 2 = 16\\text{ (cm)}$.\nDiện tích hình thang là:\n$(16 + 8) \\times 6 : 2 = 72\\text{ (cm}^2)$\nĐáp số: $72\\text{ cm}^2$.", "72 cm²", 4, 1.0),
            make_essay(3, "Một thửa ruộng hình thang có diện tích $540\\text{ m}^2$, chiều cao $18\\text{ m}$. Tính trung bình cộng hai đáy của thửa ruộng đó.", "Tổng độ dài hai đáy là:\n$540 \\times 2 : 18 = 60\\text{ (m)}$\nTrung bình cộng hai đáy là:\n$60 : 2 = 30\\text{ (m)}$\nĐáp số: 30 m.", "30 m", 4, 1.0),
            make_essay(4, "Một mảnh đất hình thang có đáy bé $18\\text{ m}$, đáy lớn bằng $\\frac{4}{3}$ đáy bé, chiều cao bằng $15\\text{ m}$.\na) Tính diện tích mảnh đất hình thang đó.\nb) Người ta đào một cái ao hình tròn có bán kính $2\\text{ m}$ trên mảnh đất đó. Tính diện tích phần đất còn lại.", "Bài giải:\na) Đáy lớn mảnh đất là:\n$18 \\times 4 : 3 = 24\\text{ (m)}$\nDiện tích mảnh đất hình thang là:\n$(24 + 18) \\times 15 : 2 = 315\\text{ (m}^2)$\nb) Diện tích cái ao hình tròn là:\n$2 \\times 2 \\times 3,14 = 12,56\\text{ (m}^2)$\nDiện tích phần đất còn lại là:\n$315 - 12,56 = 302,44\\text{ (m}^2)$\nĐáp số:\na) $315\\text{ m}^2$;\nb) $302,44\\text{ m}^2$.", "a) 315 m²; b) 302,44 m²", 5, 1.5),
            make_essay(5, "Một khu đất hình thang có tổng độ dài hai đáy là $90\\text{ m}$, chiều cao bằng $\\frac{1}{3}$ tổng hai đáy.\na) Tính diện tích khu đất hình thang đó.\nb) Người ta trồng bắp cải trên khu đất, trung bình cứ $10\\text{ m}^2$ thu được $35\\text{ kg}$ bắp cải. Hỏi toàn bộ khu đất thu hoạch được bao nhiêu tấn bắp cải?", "Bài giải:\na) Chiều cao khu đất là:\n$90 \\times 1 : 3 = 30\\text{ (m)}$\nDiện tích khu đất là:\n$90 \\times 30 : 2 = 1350\\text{ (m}^2)$\nb) Số ki-lô-gam bắp cải thu hoạch được là:\n$1350 : 10 \\times 35 = 4725\\text{ (kg)}$\nĐổi: $4725\\text{ kg} = 4,725\\text{ tấn}$.\nĐáp số:\na) $1350\\text{ m}^2$;\nb) $4,725\\text{ tấn bắp cải}$.", "a) 1350 m²; b) 4,725 tấn", 5, 1.5),
            make_essay(6, "Cho hình thang ABCD có đáy nhỏ $AB = 6\\text{ cm}$, đáy lớn $CD = 10\\text{ cm}$. Chiều cao hình thang là $4\\text{ cm}$. Hai đường chéo AC và BD cắt nhau tại O. Tính diện tích tam giác ABD và diện tích tam giác BCD.", "Bài giải:\nDiện tích tam giác ABD (đáy AB, chiều cao bằng chiều cao hình thang) là:\n$6 \\times 4 : 2 = 12\\text{ (cm}^2)$\nDiện tích tam giác BCD (đáy CD, chiều cao bằng chiều cao hình thang) là:\n$10 \\times 4 : 2 = 20\\text{ (cm}^2)$\nĐáp số: $S_{ABD} = 12\\text{ cm}^2; S_{BCD} = 20\\text{ cm}^2$.", "S(ABD)=12 cm²; S(BCD)=20 cm²", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 24: HÌNH TRÒN. CHU VI VÀ DIỆN TÍCH HÌNH TRÒN
    # =========================================================================

    # --- Bài 24 - Đề 1 ---
    exams["th5_b24_test1"] = {
        "id": "th5_b24_test1",
        "lessonId": "th5_b24",
        "lessonNum": 24,
        "testNum": 1,
        "title": "Bài 24: Hình tròn. Chu vi và diện tích hình tròn - Đề số 1",
        "topic": "Hình tròn. Chu vi và diện tích hình tròn",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Công thức tính chu vi hình tròn có bán kính $r$ là:", ["$C = r \\times 3,14$", "$C = r \\times 2 \\times 3,14$", "$C = r \\times r \\times 3,14$", "$C = r \\times 4$"], 1, "Chu vi hình tròn là $C = r \\times 2 \\times 3,14$."),
            make_mc(2, "Công thức tính diện tích hình tròn có bán kính $r$ là:", ["$S = r \\times 2 \\times 3,14$", "$S = r \\times r \\times 3,14$", "$S = d \\times 3,14$", "$S = r \\times 3,14$"], 1, "Diện tích hình tròn là $S = r \\times r \\times 3,14$."),
            make_mc(3, "Chu vi của một hình tròn có đường kính $d = 10\\text{ cm}$ là:", ["$31,4\\text{ cm}$", "$62,8\\text{ cm}$", "$78,5\\text{ cm}$", "$15,7\\text{ cm}$"], 0, "$C = 10 \\times 3,14 = 31,4\\text{ cm}$."),
            make_mc(4, "Diện tích hình tròn có bán kính $r = 4\\text{ cm}$ là:", ["$25,12\\text{ cm}^2$", "$50,24\\text{ cm}^2$", "$12,56\\text{ cm}^2$", "$16\\text{ cm}^2$"], 1, "$S = 4 \\times 4 \\times 3,14 = 50,24\\text{ cm}^2$."),
            make_mc(5, "Một hình tròn có chu vi $18,84\\text{ cm}$. Bán kính của nó là:", ["2 cm", "3 cm", "4 cm", "6 cm"], 1, "$r = 18,84 : 3,14 : 2 = 3\\text{ cm}$."),
            make_mc(6, "Nếu bán kính của hình tròn tăng lên 2 lần thì diện tích của nó tăng lên:", ["2 lần", "4 lần", "6 lần", "8 lần"], 1, "$S = (2r) \\times (2r) \\times 3,14 = 4 \\times (r \\times r \\times 3,14)$, tăng 4 lần.")
        ],
        "part2": [
            make_essay(1, "Tính chu vi và diện tích hình tròn có:\na) Bán kính $r = 5\\text{ cm}$.\nb) Đường kính $d = 8\\text{ dm}$.", "a) $C = 5 \\times 2 \\times 3,14 = 31,4\\text{ (cm)}$; $S = 5 \\times 5 \\times 3,14 = 78,5\\text{ (cm}^2)$\nb) $r = 8 : 2 = 4\\text{ (dm)}$; $C = 8 \\times 3,14 = 25,12\\text{ (dm)}$; $S = 4 \\times 4 \\times 3,14 = 50,24\\text{ (dm}^2)$", "a) C=31,4 cm, S=78,5 cm²; b) C=25,12 dm, S=50,24 dm²", 4, 1.0),
            make_essay(2, "Một chiếc đĩa hình tròn có chu vi là $62,8\\text{ cm}$. Tính diện tích của chiếc đĩa đó.", "Bán kính của chiếc đĩa là:\n$62,8 : 3,14 : 2 = 10\\text{ (cm)}$\nDiện tích chiếc đĩa là:\n$10 \\times 10 \\times 3,14 = 314\\text{ (cm}^2)$\nĐáp số: $314\\text{ cm}^2$.", "314 cm²", 4, 1.0),
            make_essay(3, "Một bánh xe đạp có đường kính là $0,65\\text{ m}$. Hỏi khi bánh xe lăn được 100 vòng trên mặt đất thì người đi xe đạp đi được quãng đường dài bao nhiêu mét?", "Chu vi của bánh xe là:\n$0,65 \\times 3,14 = 2,041\\text{ (m)}$\nQuãng đường đi được khi bánh xe lăn 100 vòng là:\n$2,041 \\times 100 = 204,1\\text{ (m)}$\nĐáp số: 204,1 m.", "204,1 m", 4, 1.0),
            make_essay(4, "Một bồn hoa hình tròn có đường kính là $6\\text{ m}$. Người ta làm một lối đi rộng $1\\text{ m}$ xung quanh bồn hoa đó.\na) Tính diện tích của bồn hoa hình tròn.\nb) Tính diện tích của lối đi xung quanh bồn hoa.", "Bài giải:\na) Bán kính bồn hoa là: $6 : 2 = 3\\text{ (m)}$.\nDiện tích bồn hoa hình tròn là:\n$3 \\times 3 \\times 3,14 = 28,26\\text{ (m}^2)$\nb) Bán kính hình tròn gồm cả bồn hoa và lối đi là:\n$3 + 1 = 4\\text{ (m)}$\nDiện tích hình tròn lớn là:\n$4 \\times 4 \\times 3,14 = 50,24\\text{ (m}^2)$\nDiện tích lối đi là:\n$50,24 - 28,26 = 21,98\\text{ (m}^2)$\nĐáp số:\na) $28,26\\text{ m}^2$;\nb) $21,98\\text{ m}^2$.", "a) 28,26 m²; b) 21,98 m²", 5, 1.5),
            make_essay(5, "Một mảnh đất hình chữ nhật có chiều dài $20\\text{ m}$, chiều rộng $15\\text{ m}$. Ở chính giữa mảnh đất, người ta đào một cái ao nuôi cá hình tròn có bán kính $3\\text{ m}$. Phần đất còn lại dùng để trồng cỏ.\na) Tính diện tích mảnh đất hình chữ nhật.\nb) Tính diện tích phần đất dùng để trồng cỏ.", "Bài giải:\na) Diện tích mảnh đất hình chữ nhật là:\n$20 \\times 15 = 300\\text{ (m}^2)$\nb) Diện tích cái ao hình tròn là:\n$3 \\times 3 \\times 3,14 = 28,26\\text{ (m}^2)$\nDiện tích đất trồng cỏ là:\n$300 - 28,26 = 271,74\\text{ (m}^2)$\nĐáp số:\na) $300\\text{ m}^2$;\nb) $271,74\\text{ m}^2$.", "a) 300 m²; b) 271,74 m²", 5, 1.5),
            make_essay(6, "Cho hai hình tròn đồng tâm: hình tròn lớn có bán kính $5\\text{ cm}$, hình tròn bé có bán kính $3\\text{ cm}$. Tính diện tích phần hình vành khuyên nằm giữa hai hình tròn đó.", "Bài giải:\nDiện tích hình tròn lớn là:\n$5 \\times 5 \\times 3,14 = 78,5\\text{ (cm}^2)$\nDiện tích hình tròn bé là:\n$3 \\times 3 \\times 3,14 = 28,26\\text{ (cm}^2)$\nDiện tích phần hình vành khuyên là:\n$78,5 - 28,26 = 50,24\\text{ (cm}^2)$\nĐáp số: $50,24\\text{ cm}^2$.", "50,24 cm²", 5, 1.0)
        ]
    }

    # --- Bài 24 - Đề 2 ---
    exams["th5_b24_test2"] = {
        "id": "th5_b24_test2",
        "lessonId": "th5_b24",
        "lessonNum": 24,
        "testNum": 2,
        "title": "Bài 24: Hình tròn. Chu vi và diện tích hình tròn - Đề số 2",
        "topic": "Hình tròn. Chu vi và diện tích hình tròn",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hình tròn có bán kính $r = 6\\text{ cm}$. Chu vi của nó là:", ["$18,84\\text{ cm}$", "$37,68\\text{ cm}$", "$113,04\\text{ cm}$", "$28,26\\text{ cm}$"], 1, "$C = 6 \\times 2 \\times 3,14 = 37,68\\text{ cm}$."),
            make_mc(2, "Hình tròn có đường kính $d = 6\\text{ dm}$. Diện tích của nó là:", ["$113,04\\text{ dm}^2$", "$28,26\\text{ dm}^2$", "$18,84\\text{ dm}^2$", "$56,52\\text{ dm}^2$"], 1, "$r = 3\\text{ dm} \\implies S = 3 \\times 3 \\times 3,14 = 28,26\\text{ dm}^2$."),
            make_mc(3, "Một mặt bàn hình tròn có chu vi $47,1\\text{ dm}$. Đường kính mặt bàn là:", ["10 dm", "15 dm", "20 dm", "7,5 dm"], 1, "$d = 47,1 : 3,14 = 15\\text{ dm}$."),
            make_mc(4, "Một hình vuông có cạnh $10\\text{ cm}$, diện tích hình tròn nội tiếp có đường kính $10\\text{ cm}$ là:", ["$100\\text{ cm}^2$", "$78,5\\text{ cm}^2$", "$31,4\\text{ cm}^2$", "$50\\text{ cm}^2$"], 1, "$r = 5\\text{ cm} \\implies S = 5 \\times 5 \\times 3,14 = 78,5\\text{ cm}^2$."),
            make_mc(5, "Đường kính của hình tròn gấp mấy lần bán kính của hình tròn đó?", ["1 lần", "2 lần", "3,14 lần", "4 lần"], 1, "Đường kính bằng 2 lần bán kính: $d = 2r$."),
            make_mc(6, "Bánh xe lăn 10 vòng đi được $21,98\\text{ m}$. Chu vi bánh xe là:", ["2,198 m", "21,98 m", "0,2198 m", "219,8 m"], 0, "$21,98 : 10 = 2,198\\text{ m}$.")
        ],
        "part2": [
            make_essay(1, "Tính chu vi và diện tích hình tròn có:\na) Bán kính $r = 2,5\\text{ cm}$.\nb) Đường kính $d = 12\\text{ dm}$.", "a) $C = 2,5 \\times 2 \\times 3,14 = 15,7\\text{ (cm)}$; $S = 2,5 \\times 2,5 \\times 3,14 = 19,625\\text{ (cm}^2)$\nb) $r = 6\\text{ dm}$; $C = 12 \\times 3,14 = 37,68\\text{ (dm)}$; $S = 6 \\times 6 \\times 3,14 = 113,04\\text{ (dm}^2)$", "a) C=15,7 cm, S=19,625 cm²; b) C=37,68 dm, S=113,04 dm²", 4, 1.0),
            make_essay(2, "Một hình tròn có diện tích là $12,56\\text{ cm}^2$. Tính bán kính và chu vi của hình tròn đó.", "Ta có: $r \\times r = 12,56 : 3,14 = 4$.\nVì $2 \\times 2 = 4$ nên bán kính hình tròn là $r = 2\\text{ cm}$.\nChu vi hình tròn là:\n$2 \\times 2 \\times 3,14 = 12,56\\text{ (cm)}$\nĐáp số: Bán kính 2 cm; Chu vi 12,56 cm.", "r = 2 cm; C = 12,56 cm", 4, 1.0),
            make_essay(3, "Một bánh xe ô tô có bán kính $0,35\\text{ m}$. Tính quãng đường ô tô đi được khi bánh xe đó lăn được 500 vòng.", "Chu vi của bánh xe ô tô là:\n$0,35 \\times 2 \\times 3,14 = 2,198\\text{ (m)}$\nQuãng đường ô tô đi được sau 500 vòng lăn là:\n$2,198 \\times 500 = 1099\\text{ (m)}$\nĐáp số: 1099 m.", "1099 m", 4, 1.0),
            make_essay(4, "Một cái hồ hình tròn có bán kính $15\\text{ m}$. Người ta trồng cây xung quanh bờ hồ, cứ cách $3,14\\text{ m}$ thì trồng một cây.\na) Tính chu vi bờ hồ hình tròn.\nb) Hỏi người ta trồng được tất cả bao nhiêu cây xung quanh bờ hồ?", "Bài giải:\na) Chu vi bờ hồ hình tròn là:\n$15 \\times 2 \\times 3,14 = 94,2\\text{ (m)}$\nb) Số cây trồng xung quanh bờ hồ là:\n$94,2 : 3,14 = 30\\text{ (cây)}$\nĐáp số:\na) 94,2 m;\nb) 30 cây.", "a) 94,2 m; b) 30 cây", 5, 1.5),
            make_essay(5, "Một tấm bìa hình vuông có cạnh $20\\text{ cm}$. Người ta vẽ một hình tròn nội tiếp có đường kính bằng cạnh hình vuông rồi cắt bỏ phần hình tròn đó.\na) Tính diện tích tấm bìa hình vuông.\nb) Tính diện tích phần bìa còn lại sau khi cắt bỏ hình tròn.", "Bài giải:\na) Diện tích tấm bìa hình vuông là:\n$20 \\times 20 = 400\\text{ (cm}^2)$\nb) Bán kính của hình tròn là: $20 : 2 = 10\\text{ (cm)}$.\nDiện tích hình tròn bị cắt bỏ là:\n$10 \\times 10 \\times 3,14 = 314\\text{ (cm}^2)$\nDiện tích phần bìa còn lại là:\n$400 - 314 = 86\\text{ (cm}^2)$\nĐáp số:\na) $400\\text{ cm}^2$;\nb) $86\\text{ cm}^2$.", "a) 400 cm²; b) 86 cm²", 5, 1.5),
            make_essay(6, "Bán kính hình tròn B gấp 3 lần bán kính hình tròn A. Hỏi diện tích hình tròn B gấp mấy lần diện tích hình tròn A?", "Bài giải:\nGọi bán kính hình tròn A là $r$, diện tích hình tròn A là $S_A = r \\times r \\times 3,14$.\nBán kính hình tròn B là $r \\times 3$, diện tích hình tròn B là:\n$S_B = (r \\times 3) \\times (r \\times 3) \\times 3,14 = 9 \\times (r \\times r \\times 3,14) = 9 \\times S_A$.\nVậy diện tích hình tròn B gấp 9 lần diện tích hình tròn A.\nĐáp số: 9 lần.", "9 lần", 5, 1.0)
        ]
    }

    # --- Bài 24 - Đề 3 ---
    exams["th5_b24_test3"] = {
        "id": "th5_b24_test3",
        "lessonId": "th5_b24",
        "lessonNum": 24,
        "testNum": 3,
        "title": "Bài 24: Hình tròn. Chu vi và diện tích hình tròn - Đề số 3",
        "topic": "Hình tròn. Chu vi và diện tích hình tròn",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình tròn có bán kính $r = 7\\text{ cm}$. Chu vi của nó là:", ["$43,96\\text{ cm}$", "$21,98\\text{ cm}$", "$153,86\\text{ cm}$", "$14\\text{ cm}$"], 0, "$C = 7 \\times 2 \\times 3,14 = 43,96\\text{ cm}$."),
            make_mc(2, "Diện tích hình tròn có bán kính $r = 7\\text{ cm}$ là:", ["$43,96\\text{ cm}^2$", "$153,86\\text{ cm}^2$", "$76,93\\text{ cm}^2$", "$49\\text{ cm}^2$"], 1, "$S = 7 \\times 7 \\times 3,14 = 153,86\\text{ cm}^2$."),
            make_mc(3, "Hình tròn có chu vi $25,12\\text{ dm}$. Đường kính của nó là:", ["4 dm", "8 dm", "6 dm", "10 dm"], 1, "$d = 25,12 : 3,14 = 8\\text{ dm}$."),
            make_mc(4, "Một cái giếng hình tròn có đường kính miệng giếng $1,4\\text{ m}$. Bán kính miệng giếng là:", ["0,7 m", "2,8 m", "0,14 m", "7 m"], 0, "$r = 1,4 : 2 = 0,7\\text{ m}$."),
            make_mc(5, "Diện tích một nửa hình tròn có bán kính $2\\text{ cm}$ là:", ["$12,56\\text{ cm}^2$", "$6,28\\text{ cm}^2$", "$3,14\\text{ cm}^2$", "$25,12\\text{ cm}^2$"], 1, "$S = 2 \\times 2 \\times 3,14 : 2 = 6,28\\text{ cm}^2$."),
            make_mc(6, "Bánh xe có bán kính $0,25\\text{ m}$. Khi lăn 200 vòng bánh xe đi được:", ["157 m", "314 m", "78,5 m", "628 m"], 1, "$C = 0,25 \\times 2 \\times 3,14 = 1,57\\text{ m}$. Quãng đường: $1,57 \\times 200 = 314\\text{ m}$.")
        ],
        "part2": [
            make_essay(1, "Tính chu vi và diện tích hình tròn có:\na) Bán kính $r = 10\\text{ cm}$.\nb) Đường kính $d = 5\\text{ dm}$.", "a) $C = 10 \\times 2 \\times 3,14 = 62,8\\text{ (cm)}$; $S = 10 \\times 10 \\times 3,14 = 314\\text{ (cm}^2)$\nb) $r = 2,5\\text{ dm}$; $C = 5 \\times 3,14 = 15,7\\text{ (dm)}$; $S = 2,5 \\times 2,5 \\times 3,14 = 19,625\\text{ (dm}^2)$", "a) C=62,8 cm, S=314 cm²; b) C=15,7 dm, S=19,625 dm²", 4, 1.0),
            make_essay(2, "Một bồn hoa hình tròn có diện tích $28,26\\text{ m}^2$. Tính chu vi của bồn hoa đó.", "Ta có: $r \\times r = 28,26 : 3,14 = 9$.\nVì $3 \\times 3 = 9$ nên bán kính bồn hoa là $r = 3\\text{ m}$.\nChu vi của bồn hoa là:\n$3 \\times 2 \\times 3,14 = 18,84\\text{ (m)}$\nĐáp số: 18,84 m.", "18,84 m", 4, 1.0),
            make_essay(3, "Một sợi dây thép uốn thành một hình tròn có bán kính $15\\text{ cm}$. Hỏi sợi dây thép đó dài bao nhiêu xăng-ti-mét?", "Độ dài sợi dây thép chính là chu vi hình tròn:\n$15 \\times 2 \\times 3,14 = 94,2\\text{ (cm)}$\nĐáp số: 94,2 cm.", "94,2 cm", 4, 1.0),
            make_essay(4, "Một cái hồ hình tròn có bán kính $8\\text{ m}$. Người ta xây một lối đi xung quanh hồ rộng $2\\text{ m}$.\na) Tính diện tích mặt nước của cái hồ.\nb) Tính diện tích của lối đi xung quanh hồ.", "Bài giải:\na) Diện tích mặt nước của cái hồ là:\n$8 \\times 8 \\times 3,14 = 200,96\\text{ (m}^2)$\nb) Bán kính hình tròn gồm cả hồ và lối đi là:\n$8 + 2 = 10\\text{ (m)}$\nDiện tích hình tròn lớn là:\n$10 \\times 10 \\times 3,14 = 314\\text{ (m}^2)$\nDiện tích của lối đi xung quanh hồ là:\n$314 - 200,96 = 113,04\\text{ (m}^2)$\nĐáp số:\na) $200,96\\text{ m}^2$;\nb) $113,04\\text{ m}^2$.", "a) 200,96 m²; b) 113,04 m²", 5, 1.5),
            make_essay(5, "Đường kính của một bánh xe đạp là $0,7\\text{ m}$.\na) Tính chu vi của bánh xe đạp đó.\nb) Người đi xe đạp đi từ nhà đến trường bánh xe lăn được đúng 1000 vòng. Hỏi quãng đường từ nhà đến trường dài bao nhiêu ki-lô-mét?", "Bài giải:\na) Chu vi của bánh xe đạp là:\n$0,7 \\times 3,14 = 2,198\\text{ (m)}$\nb) Quãng đường từ nhà đến trường là:\n$2,198 \\times 1000 = 2198\\text{ (m)}$\nĐổi: $2198\\text{ m} = 2,198\\text{ km}$.\nĐáp số:\na) 2,198 m;\nb) 2,198 km.", "a) 2,198 m; b) 2,198 km", 5, 1.5),
            make_essay(6, "Một mảnh vườn hình vuông có chu vi $40\\text{ m}$. Người ta trồng hoa ở bốn góc vườn, mỗi góc là một phần tư hình tròn có bán kính $3\\text{ m}$. Tính diện tích phần đất còn lại ở giữa vườn.", "Bài giải:\nCạnh của mảnh vườn hình vuông là: $40 : 4 = 10\\text{ (m)}$.\nDiện tích mảnh vườn hình vuông là:\n$10 \\times 10 = 100\\text{ (m}^2)$\nBốn phần tư hình tròn ở 4 góc ghép lại thành một hình tròn hoàn chỉnh có bán kính $3\\text{ m}$.\nTổng diện tích 4 góc trồng hoa là:\n$3 \\times 3 \\times 3,14 = 28,26\\text{ (m}^2)$\nDiện tích phần đất còn lại ở giữa là:\n$100 - 28,26 = 71,74\\text{ (m}^2)$\nĐáp số: $71,74\\text{ m}^2$.", "71,74 m²", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 25: LUYỆN TẬP CHUNG CHỦ ĐỀ 4
    # =========================================================================

    # --- Bài 25 - Đề 1 ---
    exams["th5_b25_test1"] = {
        "id": "th5_b25_test1",
        "lessonId": "th5_b25",
        "lessonNum": 25,
        "testNum": 1,
        "title": "Bài 25: Luyện tập chung Chủ đề 4 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 4",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình tam giác có đáy $15\\text{ cm}$, chiều cao $12\\text{ cm}$. Diện tích là:", ["$180\\text{ cm}^2$", "$90\\text{ cm}^2$", "$45\\text{ cm}^2$", "$120\\text{ cm}^2$"], 1, "$S = 15 \\times 12 : 2 = 90\\text{ cm}^2$."),
            make_mc(2, "Một hình thang có đáy lớn $14\\text{ m}$, đáy bé $10\\text{ m}$, chiều cao $6\\text{ m}$. Diện tích là:", ["$144\\text{ m}^2$", "$72\\text{ m}^2$", "$60\\text{ m}^2$", "$84\\text{ m}^2$"], 1, "$S = (14 + 10) \\times 6 : 2 = 72\\text{ m}^2$."),
            make_mc(3, "Diện tích hình tròn có bán kính $r = 6\\text{ cm}$ là:", ["$37,68\\text{ cm}^2$", "$113,04\\text{ cm}^2$", "$18,84\\text{ cm}^2$", "$56,52\\text{ cm}^2$"], 1, "$S = 6 \\times 6 \\times 3,14 = 113,04\\text{ cm}^2$."),
            make_mc(4, "Một hình thang có diện tích $100\\text{ cm}^2$, chiều cao $10\\text{ cm}$. Tổng hai đáy là:", ["10 cm", "20 cm", "30 cm", "40 cm"], 1, "$100 \\times 2 : 10 = 20\\text{ cm}$."),
            make_mc(5, "Chu vi hình tròn có đường kính $d = 20\\text{ cm}$ là:", ["$31,4\\text{ cm}$", "$62,8\\text{ cm}$", "$125,6\\text{ cm}$", "$314\\text{ cm}$"], 1, "$C = 20 \\times 3,14 = 62,8\\text{ cm}$."),
            make_mc(6, "Hình tam giác có diện tích $24\\text{ cm}^2$, đáy dài $8\\text{ cm}$. Chiều cao của tam giác là:", ["3 cm", "6 cm", "4 cm", "8 cm"], 1, "$h = 24 \\times 2 : 8 = 6\\text{ cm}$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích của:\na) Hình tam giác có đáy $16\\text{ cm}$, chiều cao $7,5\\text{ cm}$.\nb) Hình thang có đáy lớn $18\\text{ m}$, đáy bé $12\\text{ m}$, chiều cao $9\\text{ m}$.", "a) $S = 16 \\times 7,5 : 2 = 60\\text{ (cm}^2)$\nb) $S = (18 + 12) \\times 9 : 2 = 135\\text{ (m}^2)$", "a) 60 cm²; b) 135 m²", 4, 1.0),
            make_essay(2, "Tính chu vi và diện tích hình tròn có bán kính $r = 8\\text{ cm}$.", "Chu vi: $C = 8 \\times 2 \\times 3,14 = 50,24\\text{ (cm)}$\nDiện tích: $S = 8 \\times 8 \\times 3,14 = 200,96\\text{ (cm}^2)$", "C = 50,24 cm; S = 200,96 cm²", 4, 1.0),
            make_essay(3, "Một mảnh đất hình tam giác có diện tích $120\\text{ m}^2$, chiều cao $12\\text{ m}$. Người ta kéo dài cạnh đáy thêm $3\\text{ m}$. Hỏi diện tích mảnh đất tăng thêm bao nhiêu mét vuông?", "Diện tích tăng thêm là:\n$3 \\times 12 : 2 = 18\\text{ (m}^2)$\nĐáp số: $18\\text{ m}^2$.", "18 m²", 4, 1.0),
            make_essay(4, "Một thửa ruộng hình thang có đáy lớn $45\\text{ m}$, đáy bé bằng $\\frac{2}{3}$ đáy lớn, chiều cao bằng $24\\text{ m}$.\na) Tính diện tích thửa ruộng đó.\nb) Cứ mỗi $100\\text{ m}^2$ thu hoạch được $65\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?", "Bài giải:\na) Đáy bé của thửa ruộng là:\n$45 \\times 2 : 3 = 30\\text{ (m)}$\nDiện tích thửa ruộng là:\n$(45 + 30) \\times 24 : 2 = 900\\text{ (m}^2)$\nb) Số ki-lô-gam thóc thu hoạch được là:\n$900 : 100 \\times 65 = 585\\text{ (kg)}$\nĐổi: $585\\text{ kg} = 5,85\\text{ tạ}$.\nĐáp số:\na) $900\\text{ m}^2$;\nb) $5,85\\text{ tạ thóc}$.", "a) 900 m²; b) 5,85 tạ", 5, 1.5),
            make_essay(5, "Một khu đất gồm một hình chữ nhật ABCD có chiều dài $30\\text{ m}$, chiều rộng $20\\text{ m}$ và một hình bán nguyệt (nửa hình tròn) có đường kính chính là chiều rộng BC của hình chữ nhật.\na) Tính diện tích hình chữ nhật ABCD.\nb) Tính diện tích toàn bộ khu đất đó.", "Bài giải:\na) Diện tích hình chữ nhật ABCD là:\n$30 \\times 20 = 600\\text{ (m}^2)$\nb) Bán kính của nửa hình tròn là: $20 : 2 = 10\\text{ (m)}$.\nDiện tích nửa hình tròn là:\n$10 \\times 10 \\times 3,14 : 2 = 157\\text{ (m}^2)$\nDiện tích toàn bộ khu đất là:\n$600 + 157 = 757\\text{ (m}^2)$\nĐáp số:\na) $600\\text{ m}^2$;\nb) $757\\text{ m}^2$.", "a) 600 m²; b) 757 m²", 5, 1.5),
            make_essay(6, "Bánh xe của một đầu máy xe lửa có đường kính $1,4\\text{ m}$. Hỏi khi đầu máy xe lửa chạy được quãng đường $4396\\text{ m}$ thì bánh xe đó đã quay được bao nhiêu vòng?", "Bài giải:\nChu vi của bánh xe đầu máy xe lửa là:\n$1,4 \\times 3,14 = 4,396\\text{ (m)}$\nSố vòng quay của bánh xe là:\n$4396 : 4,396 = 1000\\text{ (vòng)}$\nĐáp số: 1000 vòng.", "1000 vòng", 5, 1.0)
        ]
    }

    # --- Bài 25 - Đề 2 ---
    exams["th5_b25_test2"] = {
        "id": "th5_b25_test2",
        "lessonId": "th5_b25",
        "lessonNum": 25,
        "testNum": 2,
        "title": "Bài 25: Luyện tập chung Chủ đề 4 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 4",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình tam giác vuông có hai cạnh góc vuông là $8\\text{ cm}$ và $15\\text{ cm}$. Diện tích của nó là:", ["$120\\text{ cm}^2$", "$60\\text{ cm}^2$", "$46\\text{ cm}^2$", "$30\\text{ cm}^2$"], 1, "$S = 8 \\times 15 : 2 = 60\\text{ cm}^2$."),
            make_mc(2, "Một hình thang có đáy lớn $25\\text{ dm}$, đáy bé $15\\text{ dm}$, chiều cao $10\\text{ dm}$. Diện tích là:", ["$200\\text{ dm}^2$", "$400\\text{ dm}^2$", "$150\\text{ dm}^2$", "$250\\text{ dm}^2$"], 0, "$S = (25 + 15) \\times 10 : 2 = 200\\text{ dm}^2$."),
            make_mc(3, "Hình tròn có chu vi $31,4\\text{ cm}$. Bán kính của nó là:", ["10 cm", "5 cm", "2,5 cm", "15,7 cm"], 1, "$r = 31,4 : 3,14 : 2 = 5\\text{ cm}$."),
            make_mc(4, "Diện tích hình tròn có đường kính $d = 4\\text{ dm}$ là:", ["$50,24\\text{ dm}^2$", "$12,56\\text{ dm}^2$", "$25,12\\text{ dm}^2$", "$6,28\\text{ dm}^2$"], 1, "$r = 2\\text{ dm} \\implies S = 2 \\times 2 \\times 3,14 = 12,56\\text{ dm}^2$."),
            make_mc(5, "Một hình thang có diện tích $75\\text{ m}^2$, chiều cao $5\\text{ m}$. Tổng hai đáy là:", ["15 m", "30 m", "25 m", "20 m"], 1, "Tổng hai đáy: $75 \\times 2 : 5 = 30\\text{ m}$."),
            make_mc(6, "Bánh xe có đường kính $0,5\\text{ m}$. Khi lăn 100 vòng bánh xe đi được:", ["157 m", "314 m", "15,7 m", "50 m"], 0, "$C = 0,5 \\times 3,14 = 1,57\\text{ m}$. $1,57 \\times 100 = 157\\text{ m}$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích của:\na) Hình tam giác có đáy $18\\text{ cm}$, chiều cao $12,5\\text{ cm}$.\nb) Hình thang có đáy lớn $15\\text{ dm}$, đáy bé $9\\text{ dm}$, chiều cao $8\\text{ dm}$.", "a) $S = 18 \\times 12,5 : 2 = 112,5\\text{ (cm}^2)$\nb) $S = (15 + 9) \\times 8 : 2 = 96\\text{ (dm}^2)$", "a) 112,5 cm²; b) 96 dm²", 4, 1.0),
            make_essay(2, "Một hình tròn có chu vi là $15,7\\text{ dm}$. Tính diện tích của hình tròn đó.", "Bán kính hình tròn là:\n$15,7 : 3,14 : 2 = 2,5\\text{ (dm)}$\nDiện tích hình tròn là:\n$2,5 \\times 2,5 \\times 3,14 = 19,625\\text{ (dm}^2)$\nĐáp số: $19,625\\text{ dm}^2$.", "19,625 dm²", 4, 1.0),
            make_essay(3, "Một mảnh đất hình thang có diện tích $360\\text{ m}^2$, chiều cao $15\\text{ m}$. Đáy bé bằng $\\frac{3}{5}$ đáy lớn. Tính độ dài mỗi đáy của mảnh đất.", "Tổng hai đáy là: $360 \\times 2 : 15 = 48\\text{ (m)}$.\nTổng số phần bằng nhau: $3 + 5 = 8\\text{ (phần)}$.\nĐáy bé là: $48 : 8 \\times 3 = 18\\text{ (m)}$.\nĐáy lớn là: $48 - 18 = 30\\text{ (m)}$.\nĐáp số: Đáy bé 18 m, Đáy lớn 30 m.", "Đáy bé 18 m; Đáy lớn 30 m", 4, 1.0),
            make_essay(4, "Một bồn hoa hình thang có đáy lớn $12\\text{ m}$, đáy bé $8\\text{ m}$, chiều cao $5\\text{ m}$. Người ta trồng hoa hồng trên bồn hoa đó, cứ $1\\text{ m}^2$ trồng được 8 cây hoa.\na) Tính diện tích bồn hoa hình thang đó.\nb) Hỏi người ta trồng được tất cả bao nhiêu cây hoa hồng trên bồn hoa đó?", "Bài giải:\na) Diện tích bồn hoa hình thang là:\n$(12 + 8) \\times 5 : 2 = 50\\text{ (m}^2)$\nb) Số cây hoa hồng trồng được là:\n$50 \\times 8 = 400\\text{ (cây)}$\nĐáp số:\na) $50\\text{ m}^2$;\nb) 400 cây hoa hồng.", "a) 50 m²; b) 400 cây", 5, 1.5),
            make_essay(5, "Một tấm bìa hình vuông có cạnh dài $14\\text{ cm}$. Người ta vẽ một hình tròn có đường kính bằng cạnh hình vuông rồi tô màu hình tròn đó.\na) Tính diện tích tấm bìa hình vuông.\nb) Tính diện tích phần tấm bìa không được tô màu.", "Bài giải:\na) Diện tích tấm bìa hình vuông là:\n$14 \\times 14 = 196\\text{ (cm}^2)$\nb) Bán kính hình tròn là: $14 : 2 = 7\\text{ (cm)}$.\nDiện tích phần hình tròn được tô màu là:\n$7 \\times 7 \\times 3,14 = 153,86\\text{ (cm}^2)$\nDiện tích phần bìa không được tô màu là:\n$196 - 153,86 = 42,14\\text{ (cm}^2)$\nĐáp số:\na) $196\\text{ cm}^2$;\nb) $42,14\\text{ cm}^2$.", "a) 196 cm²; b) 42,14 cm²", 5, 1.5),
            make_essay(6, "Cho hình tam giác ABC có diện tích $120\\text{ cm}^2$. Kéo dài đáy BC về phía C thêm đoạn CD sao cho $CD = \\frac{1}{2} BC$. Tính diện tích hình tam giác ABD.", "Bài giải:\nTam giác ACD và tam giác ABC có chung chiều cao hạ từ đỉnh A xuống đường thẳng BD.\nVì đáy $CD = \\frac{1}{2} BC$ nên diện tích tam giác ACD bằng một nửa diện tích tam giác ABC:\n$S_{ACD} = 120 : 2 = 60\\text{ (cm}^2)$\nDiện tích tam giác ABD là:\n$S_{ABD} = S_{ABC} + S_{ACD} = 120 + 60 = 180\\text{ (cm}^2)$\nĐáp số: $180\\text{ cm}^2$.", "180 cm²", 5, 1.0)
        ]
    }

    # --- Bài 25 - Đề 3 ---
    exams["th5_b25_test3"] = {
        "id": "th5_b25_test3",
        "lessonId": "th5_b25",
        "lessonNum": 25,
        "testNum": 3,
        "title": "Bài 25: Luyện tập chung Chủ đề 4 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 4",
        "chapter": "Chủ đề 4: Hình phẳng và hình khối",
        "grade": "5",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình tam giác có diện tích $36\\text{ cm}^2$, chiều cao $6\\text{ cm}$. Cạnh đáy là:", ["6 cm", "12 cm", "8 cm", "18 cm"], 1, "Đáy là: $36 \\times 2 : 6 = 12\\text{ cm}$."),
            make_mc(2, "Một hình thang có hai đáy lần lượt là $9\\text{ cm}$ và $7\\text{ cm}$, chiều cao $4\\text{ cm}$. Diện tích là:", ["$32\\text{ cm}^2$", "$64\\text{ cm}^2$", "$28\\text{ cm}^2$", "$36\\text{ cm}^2$"], 0, "$S = (9 + 7) \\times 4 : 2 = 32\\text{ cm}^2$."),
            make_mc(3, "Hình tròn có bán kính $r = 1,5\\text{ m}$. Chu vi của nó là:", ["$4,71\\text{ m}$", "$9,42\\text{ m}$", "$7,065\\text{ m}$", "$3\\text{ m}$"], 1, "$C = 1,5 \\times 2 \\times 3,14 = 9,42\\text{ m}$."),
            make_mc(4, "Diện tích hình tròn ở Câu 3 là:", ["$7,065\\text{ m}^2$", "$14,13\\text{ m}^2$", "$9,42\\text{ m}^2$", "$4,71\\text{ m}^2$"], 0, "$S = 1,5 \\times 1,5 \\times 3,14 = 7,065\\text{ m}^2$."),
            make_mc(5, "Đáy lớn $35\\text{ m}$, đáy bé $25\\text{ m}$, chiều cao $16\\text{ m}$. Diện tích hình thang là:", ["$480\\text{ m}^2$", "$960\\text{ m}^2$", "$450\\text{ m}^2$", "$500\\text{ m}^2$"], 0, "$S = (35 + 25) \\times 16 : 2 = 480\\text{ m}^2$."),
            make_mc(6, "Bánh xe có bán kính $0,4\\text{ m}$. Khi lăn 50 vòng quãng đường đi được là:", ["125,6 m", "62,8 m", "251,2 m", "12,56 m"], 0, "$C = 0,4 \\times 2 \\times 3,14 = 2,512\\text{ m}$. $2,512 \\times 50 = 125,6\\text{ m}$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích của:\na) Hình tam giác vuông có hai cạnh góc vuông dài $9\\text{ cm}$ và $14\\text{ cm}$.\nb) Hình thang có hai đáy $16\\text{ m}$ và $10\\text{ m}$, chiều cao $7,5\\text{ m}$.", "a) $S = 9 \\times 14 : 2 = 63\\text{ (cm}^2)$\nb) $S = (16 + 10) \\times 7,5 : 2 = 97,5\\text{ (m}^2)$", "a) 63 cm²; b) 97,5 m²", 4, 1.0),
            make_essay(2, "Tính chu vi và diện tích của hình tròn có đường kính $d = 16\\text{ cm}$.", "Bán kính: $r = 16 : 2 = 8\\text{ (cm)}$.\nChu vi: $C = 16 \\times 3,14 = 50,24\\text{ (cm)}$.\nDiện tích: $S = 8 \\times 8 \\times 3,14 = 200,96\\text{ (cm}^2)$.", "C = 50,24 cm; S = 200,96 cm²", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình thang có đáy lớn $28\\text{ m}$, đáy bé $18\\text{ m}$. Chiều cao bằng trung bình cộng của hai đáy. Tính diện tích mảnh vườn đó.", "Chiều cao mảnh vườn là:\n$(28 + 18) : 2 = 23\\text{ (m)}$\nDiện tích mảnh vườn là:\n$(28 + 18) \\times 23 : 2 = 529\\text{ (m}^2)$\nĐáp số: $529\\text{ m}^2$.", "529 m²", 4, 1.0),
            make_essay(4, "Một cái hồ hình tròn có đường kính $20\\text{ m}$. Người ta làm một con đường bê tông chạy vòng quanh bờ hồ rộng $1,5\\text{ m}$.\na) Tính diện tích mặt hồ hình tròn.\nb) Tính diện tích con đường bê tông xung quanh hồ.", "Bài giải:\na) Bán kính mặt hồ là: $20 : 2 = 10\\text{ (m)}$.\nDiện tích mặt hồ là:\n$10 \\times 10 \\times 3,14 = 314\\text{ (m}^2)$\nb) Bán kính hình tròn gồm cả hồ và con đường là:\n$10 + 1,5 = 11,5\\text{ (m)}$\nDiện tích hình tròn lớn là:\n$11,5 \\times 11,5 \\times 3,14 = 415,265\\text{ (m}^2)$\nDiện tích con đường bê tông là:\n$415,265 - 314 = 101,265\\text{ (m}^2)$\nĐáp số:\na) $314\\text{ m}^2$;\nb) $101,265\\text{ m}^2$.", "a) 314 m²; b) 101,265 m²", 5, 1.5),
            make_essay(5, "Một thửa ruộng hình thang có đáy lớn $60\\text{ m}$, đáy bé $40\\text{ m}$, chiều cao $30\\text{ m}$. Người ta dành $20\\%$ diện tích để đào mương dẫn nước, phần diện tích còn lại cấy lúa.\na) Tính diện tích thửa ruộng hình thang đó.\nb) Tính diện tích phần đất cấy lúa.", "Bài giải:\na) Diện tích thửa ruộng hình thang là:\n$(60 + 40) \\times 30 : 2 = 1500\\text{ (m}^2)$\nb) Tỉ số phần trăm diện tích cấy lúa là:\n$100\\% - 20\\% = 80\\%$\nDiện tích phần đất cấy lúa là:\n$1500 \\times 80 : 100 = 1200\\text{ (m}^2)$\nĐáp số:\na) $1500\\text{ m}^2$;\nb) $1200\\text{ m}^2$.", "a) 1500 m²; b) 1200 m²", 5, 1.5),
            make_essay(6, "Cho hình vuông ABCD có cạnh dài $10\\text{ cm}$. Vẽ 4 góc phần tư hình tròn có tâm lần lượt là A, B, C, D và có bán kính bằng nửa cạnh hình vuông ($5\\text{ cm}$). Tính diện tích phần hình vuông nằm ngoài 4 góc phần tư hình tròn đó.", "Bài giải:\nDiện tích hình vuông ABCD là:\n$10 \\times 10 = 100\\text{ (cm}^2)$\nBốn góc phần tư hình tròn ghép lại thành một hình tròn hoàn chỉnh có bán kính $5\\text{ cm}$.\nDiện tích hình tròn đó là:\n$5 \\times 5 \\times 3,14 = 78,5\\text{ (cm}^2)$\nDiện tích phần hình vuông nằm ngoài hình tròn là:\n$100 - 78,5 = 21,5\\text{ (cm}^2)$\nĐáp số: $21,5\\text{ cm}^2$.", "21,5 cm²", 5, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 4: {len(ex)} (Kỳ vọng: 12 đề)")
    for eid, e in ex.items():
        print(f"[{eid}] {e['title']} - Part 1: {len(e['part1'])}, Part 2: {len(e['part2'])}")
