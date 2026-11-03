# -*- coding: utf-8 -*-
"""
HỆ THỐNG 8 ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN LỚP 4
Bộ sách: Kết nối tri thức với cuộc sống
Mã kỳ thi: th4_gk2 (Đề 01 đến Đề 08)
Phạm vi kiến thức:
- Phép chia cho số có 1, 2 chữ số (chia hết, chia có dư, tính giá trị biểu thức)
- Dấu hiệu chia hết cho 2, 5, 9, 3
- Khái niệm phân số, tử số và mẫu số, phân số bằng nhau, rút gọn, quy đồng mẫu số, so sánh phân số
- Hình học & đo lường: hình bình hành, diện tích hình bình hành, đơn vị đo diện tích
- Giải bài toán có lời văn: rút về đơn vị, tìm thành phần chưa biết, bài toán thực tế.
Chuẩn mực sư phạm:
- Thời gian làm bài: 40 phút, Thang điểm: 10.0
- Phần 1 (3.0đ): 6 câu trắc nghiệm (0.5đ/câu), tiêu đề strictly '**Câu [Số]:** '
- Phần 2 (7.0đ): 6 câu tự luận (1.0, 1.0, 1.0, 1.5, 1.5, 1.0đ), tiêu đề strictly '**Bài [Số]:** '
"""

def make_mc(qid, question, options, correct, explanation, level="Thông hiểu"):
    q_text = question if question.startswith(f"**Câu {qid}:** ") else f"**Câu {qid}:** {question}"
    return {
        "id": qid,
        "question": q_text,
        "options": options,
        "choices": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5,
        "level": level
    }

def make_essay(qid, question, solution, answer, lineCount=4, points=1.0, level="Thông hiểu"):
    p_text = question if question.startswith(f"**Bài {qid}:** ") else f"**Bài {qid}:** {question}"
    sol = solution if "Đáp số" in solution else f"{solution}\nĐáp số: {answer}."
    return {
        "id": qid,
        "question": p_text,
        "solution": sol,
        "answer": answer,
        "lineCount": lineCount,
        "points": points,
        "level": level
    }

def get_th4_gk2_exams():
    exams = {}

    # =========================================================================
    # ĐỀ SỐ 01 (th4_gk2_de01)
    # =========================================================================
    exams["th4_gk2_de01"] = {
        "id": "th4_gk2_de01",
        "code": "GK2-DE01",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 01)",
        "grade": "4",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Một hình tròn được chia thành 6 phần bằng nhau, người ta đã tô màu 5 phần. Phân số chỉ phần đã tô màu là:", ["5/6", "6/5", "1/6", "5/1"], 0, "Hình tròn chia làm 6 phần bằng nhau, tô màu 5 phần thì phân số chỉ phần tô màu là 5/6.", "Nhận biết"),
            make_mc(2, "Trong các số sau, số chia hết cho cả 2 và 5 là:", ["435", "430", "432", "437"], 1, "Số có chữ số tận cùng là 0 thì chia hết cho cả 2 và 5. Do đó số 430 chia hết cho cả 2 và 5.", "Nhận biết"),
            make_mc(3, "Rút gọn phân số 18/24 về phân số tối giản ta được:", ["9/12", "6/8", "3/4", "2/3"], 2, "Cả tử số và mẫu số cùng chia hết cho 6: 18 : 6 = 3; 24 : 6 = 4. Vậy tối giản là 3/4.", "Thông hiểu"),
            make_mc(4, "Kết quả của phép chia 4320 : 36 là:", ["12", "120", "102", "122"], 1, "432 : 36 = 12, hạ 0 được 0 : 36 = 0. Vậy 4320 : 36 = 120.", "Thông hiểu"),
            make_mc(5, "Quy đồng mẫu số hai phân số 2/3 và 3/5 với mẫu số chung 15 ta được hai phân số là:", ["10/15 và 9/15", "6/15 và 9/15", "10/15 và 6/15", "2/15 và 3/15"], 0, "2/3 = (2 x 5)/(3 x 5) = 10/15 và 3/5 = (3 x 3)/(5 x 3) = 9/15.", "Thông hiểu"),
            make_mc(6, "Một hình bình hành có độ dài đáy là 15 cm và chiều cao là 8 cm. Diện tích của hình bình hành đó là:", ["120 cm²", "60 cm²", "23 cm²", "46 cm²"], 0, "Diện tích hình bình hành = Đáy x Chiều cao = 15 x 8 = 120 (cm²).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 38 465 : 5\nb) 5472 : 18", "a) 38 465 : 5 = 7693\nb) 5472 : 18 = 304", "a) 7693; b) 304", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Rút gọn các phân số sau thành phân số tối giản:\na) 15/25\nb) 24/36", "a) 15/25 = (15 : 5)/(25 : 5) = 3/5\nb) 24/36 = (24 : 12)/(36 : 12) = 2/3", "a) 3/5; b) 2/3", 4, 1.0, "Thông hiểu"),
            make_essay(3, "So sánh hai phân số:\na) 4/7 và 6/7\nb) 3/4 và 5/8", "a) Vì hai phân số cùng mẫu số 7 và 4 < 6 nên 4/7 < 6/7.\nb) Quy đồng mẫu số: 3/4 = (3 x 2)/(4 x 2) = 6/8. Vì 6/8 > 5/8 nên 3/4 > 5/8.", "a) 4/7 < 6/7; b) 3/4 > 5/8", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một cửa hàng có 2480 kg gạo được đóng đều vào 40 bao. Cửa hàng đã bán được 15 bao gạo đó. Hỏi cửa hàng đã bán được bao nhiêu ki-lô-gam gạo?", "Mỗi bao chứa số ki-lô-gam gạo là:\n2480 : 40 = 62 (kg)\nCửa hàng đã bán được số ki-lô-gam gạo là:\n62 x 15 = 930 (kg)\nĐáp số: 930 kg gạo.", "930 kg", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh vườn hình bình hành có độ dài đáy là 36 m, chiều cao bằng 2/3 độ dài đáy. Tính diện tích của mảnh vườn đó.", "Chiều cao mảnh vườn hình bình hành là:\n36 x 2 : 3 = 24 (m)\nDiện tích mảnh vườn hình bình hành là:\n36 x 24 = 864 (m²)\nĐáp số: 864 m².", "864 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm chữ số thích hợp thay vào dấu * để số 5*2 chia hết cho 9.", "Để số 5*2 chia hết cho 9 thì tổng các chữ số phải chia hết cho 9:\n(5 + * + 2) chia hết cho 9 hay (7 + *) chia hết cho 9.\nVì * là chữ số từ 0 đến 9 nên * = 2 (do 7 + 2 = 9 chia hết cho 9).\nVậy chữ số cần tìm là 2.\nĐáp số: 2.", "2", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 02 (th4_gk2_de02)
    # =========================================================================
    exams["th4_gk2_de02"] = {
        "id": "th4_gk2_de02",
        "code": "GK2-DE02",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 02)",
        "grade": "4",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Trong các số sau, số nào chia hết cho cả 3 và 9?", ["345", "621", "512", "705"], 1, "Tổng các chữ số của 621 là 6 + 2 + 1 = 9 chia hết cho 9, do đó 621 chia hết cho cả 3 và 9.", "Nhận biết"),
            make_mc(2, "Tử số của phân số 7/12 là:", ["12", "7", "19", "5"], 1, "Phân số 7/12 có tử số là số viết trên gạch ngang, tức là số 7.", "Nhận biết"),
            make_mc(3, "Phân số nào dưới đây bằng phân số 3/5?", ["6/15", "9/20", "12/20", "15/30"], 2, "Ta có 3/5 = (3 x 4)/(5 x 4) = 12/20.", "Thông hiểu"),
            make_mc(4, "Thương của phép chia 7560 : 35 là:", ["216", "215", "206", "226"], 0, "75 : 35 = 2 dư 5; hạ 6 được 56 : 35 = 1 dư 21; hạ 0 được 210 : 35 = 6. Vậy thương là 216.", "Thông hiểu"),
            make_mc(5, "Một mảnh đất hình bình hành có độ dài đáy 20 m và chiều cao 14 m. Diện tích mảnh đất đó là:", ["140 m²", "280 m²", "68 m²", "340 m²"], 1, "Diện tích hình bình hành = 20 x 14 = 280 (m²).", "Thông hiểu"),
            make_mc(6, "Trong các phân số 1/2, 2/3, 3/4, 4/5, phân số lớn nhất là:", ["1/2", "2/3", "3/4", "4/5"], 3, "Phần bù tới 1 lần lượt là 1/2, 1/3, 1/4, 1/5. Vì 1/5 bé nhất nên 4/5 lớn nhất.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 75 840 : 6\nb) 8832 : 24", "a) 75 840 : 6 = 12 640\nb) 8832 : 24 = 368", "a) 12 640; b) 368", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) 2/5 = .../15\nb) 28/42 = 4/...", "a) 2/5 = (2 x 3)/(5 x 3) = 6/15 nên số cần điền là 6\nb) 28/42 = (28 : 7)/(42 : 7) = 4/6 nên số cần điền là 6", "a) 6; b) 6", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Quy đồng mẫu số hai phân số:\na) 5/6 và 7/12\nb) 3/7 và 4/5", "a) Chọn mẫu số chung là 12: 5/6 = (5 x 2)/(6 x 2) = 10/12 và giữ nguyên 7/12.\nb) Mẫu số chung là 35: 3/7 = (3 x 5)/(7 x 5) = 15/35 và 4/5 = (4 x 7)/(5 x 7) = 28/35.", "a) 10/12 và 7/12; b) 15/35 và 28/35", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Khối lớp 4 có 168 học sinh chia đều thành 24 nhóm tham gia hoạt động ngoại khóa. Hỏi 9 nhóm như vậy có bao nhiêu học sinh?", "Mỗi nhóm có số học sinh là:\n168 : 24 = 7 (học sinh)\n9 nhóm như vậy có số học sinh là:\n7 x 9 = 63 (học sinh)\nĐáp số: 63 học sinh.", "63 học sinh", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một khu đất hình bình hành có độ dài đáy là 45 m, chiều cao kém độ dài đáy 15 m. Tính diện tích của khu đất đó.", "Chiều cao của khu đất là:\n45 - 15 = 30 (m)\nDiện tích của khu đất hình bình hành là:\n45 x 30 = 1350 (m²)\nĐáp số: 1350 m².", "1350 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số tự nhiên x biết 36 chia hết cho x và 4 < x < 10.", "Vì 36 chia hết cho x nên x là ước của 36.\nCác ước của 36 là: 1, 2, 3, 4, 6, 9, 12, 18, 36.\nTheo đề bài 4 < x < 10 nên x nhận các giá trị là 6 hoặc 9.\nĐáp số: x = 6 hoặc x = 9.", "x = 6 hoặc x = 9", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 03 (th4_gk2_de03)
    # =========================================================================
    exams["th4_gk2_de03"] = {
        "id": "th4_gk2_de03",
        "code": "GK2-DE03",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 03)",
        "grade": "4",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Số 3450 chia hết cho những số nào trong các số: 2, 3, 5, 9?", ["Chia hết cho 2 và 5", "Chia hết cho 2, 3, 5", "Chia hết cho 2, 3, 5, 9", "Chia hết cho 3 và 9"], 1, "3450 tận cùng bằng 0 nên chia hết cho 2 và 5. Tổng các chữ số là 3+4+5+0 = 12 chia hết cho 3 nhưng không chia hết cho 9. Do đó chia hết cho 2, 3, 5.", "Thông hiểu"),
            make_mc(2, "Trong các phân số sau, phân số tối giản là:", ["6/9", "14/21", "7/11", "15/25"], 2, "Phân số 7/11 có tử số và mẫu số không cùng chia hết cho số tự nhiên nào lớn hơn 1 nên là phân số tối giản.", "Nhận biết"),
            make_mc(3, "Mẫu số chung nhỏ nhất của hai phân số 5/8 và 7/12 là:", ["96", "48", "24", "16"], 2, "24 chia hết cho cả 8 (24:8=3) và 12 (24:12=2) nên mẫu số chung nhỏ nhất là 24.", "Thông hiểu"),
            make_mc(4, "Kết quả của phép chia 9600 : 40 là:", ["2400", "240", "24", "204"], 1, "9600 : 40 = 960 : 4 = 240.", "Nhận biết"),
            make_mc(5, "Phân số nào dưới đây lớn hơn 1?", ["5/6", "8/8", "9/7", "3/4"], 2, "Phân số có tử số lớn hơn mẫu số thì lớn hơn 1. Ta có 9/7 > 1 vì 9 > 7.", "Nhận biết"),
            make_mc(6, "Một hình bình hành có diện tích 150 cm² và chiều cao 10 cm. Độ dài cạnh đáy tương ứng là:", ["15 cm", "30 cm", "25 cm", "1500 cm"], 0, "Độ dài đáy = Diện tích : Chiều cao = 150 : 10 = 15 (cm).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 49 320 : 8\nb) 9720 : 45", "a) 49 320 : 8 = 6165\nb) 9720 : 45 = 216", "a) 6165; b) 216", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Rút gọn các phân số sau:\na) 35/45\nb) 48/64", "a) 35/45 = (35 : 5)/(45 : 5) = 7/9\nb) 48/64 = (48 : 16)/(64 : 16) = 3/4", "a) 7/9; b) 3/4", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Sắp xếp các phân số sau theo thứ tự từ bé đến lớn: 2/5, 3/5, 1/5, 4/5.", "Các phân số có cùng mẫu số là 5. So sánh tử số: 1 < 2 < 3 < 4.\nVậy dãy phân số xếp từ bé đến lớn là: 1/5 ; 2/5 ; 3/5 ; 4/5.", "1/5 ; 2/5 ; 3/5 ; 4/5", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một xưởng may sản xuất được 3120 chiếc áo trong 13 ngày. Hỏi trong 25 ngày xưởng đó sản xuất được bao nhiêu chiếc áo, biết số áo sản xuất mỗi ngày như nhau?", "Mỗi ngày xưởng may sản xuất được số chiếc áo là:\n3120 : 13 = 240 (chiếc)\nTrong 25 ngày xưởng đó sản xuất được số chiếc áo là:\n240 x 25 = 6000 (chiếc)\nĐáp số: 6000 chiếc áo.", "6000 chiếc áo", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh đất hình bình hành có chiều cao 18 m, độ dài đáy gấp đôi chiều cao. Tính diện tích mảnh đất đó.", "Độ dài đáy mảnh đất hình bình hành là:\n18 x 2 = 36 (m)\nDiện tích mảnh đất hình bình hành là:\n36 x 18 = 648 (m²)\nĐáp số: 648 m².", "648 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm các chữ số a và b để số 4a5b chia hết cho cả 2, 5 và 9.", "Để 4a5b chia hết cho cả 2 và 5 thì chữ số tận cùng b = 0.\nThay b = 0 ta có số 4a50.\nĐể 4a50 chia hết cho 9 thì tổng các chữ số phải chia hết cho 9:\n(4 + a + 5 + 0) = (9 + a) chia hết cho 9.\nVì a là chữ số từ 0 đến 9 nên a = 0 hoặc a = 9.\nVậy các cặp chữ số (a, b) tìm được là: a = 0, b = 0 hoặc a = 9, b = 0.", "a = 0, b = 0 hoặc a = 9, b = 0", 5, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 04 (th4_gk2_de04)
    # =========================================================================
    exams["th4_gk2_de04"] = {
        "id": "th4_gk2_de04",
        "code": "GK2-DE04",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 04)",
        "grade": "4",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Một số chia hết cho 2 nhưng không chia hết cho 5 thì có chữ số tận cùng là:", ["0, 2, 4, 6, 8", "2, 4, 6, 8", "0, 5", "1, 3, 5, 7, 9"], 1, "Số chia hết cho 2 tận cùng là 0, 2, 4, 6, 8. Nếu không chia hết cho 5 thì không thể tận cùng bằng 0. Vậy tận cùng là 2, 4, 6, 8.", "Thông hiểu"),
            make_mc(2, "Trong các phân số sau, phân số nào bằng 1?", ["14/15", "15/14", "15/15", "1/15"], 2, "Phân số có tử số bằng mẫu số thì phân số đó bằng 1. Vậy 15/15 = 1.", "Nhận biết"),
            make_mc(3, "Kết quả của phép chia 14 580 : 54 là:", ["27", "270", "207", "275"], 1, "14 580 : 54 = 270.", "Thông hiểu"),
            make_mc(4, "Rút gọn phân số 40/60 về phân số tối giản ta được:", ["4/6", "2/3", "10/15", "1/2"], 1, "40/60 = (40 : 20)/(60 : 20) = 2/3.", "Thông hiểu"),
            make_mc(5, "So sánh hai phân số 5/9 và 5/11:", ["5/9 < 5/11", "5/9 > 5/11", "5/9 = 5/11", "Không so sánh được"], 1, "Hai phân số có cùng tử số là 5, mẫu số 9 < 11 nên phân số 5/9 > 5/11.", "Thông hiểu"),
            make_mc(6, "Diện tích hình bình hành có độ dài đáy 25 dm và chiều cao 16 dm là:", ["400 dm²", "200 dm²", "41 dm²", "82 dm²"], 0, "Diện tích hình bình hành = 25 x 16 = 400 (dm²).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 58 135 : 7\nb) 7820 : 34", "a) 58 135 : 7 = 8305\nb) 7820 : 34 = 230", "a) 8305; b) 230", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Quy đồng mẫu số các phân số:\na) 3/4 và 5/6\nb) 2/9 và 7/18", "a) Mẫu số chung là 12: 3/4 = (3 x 3)/(4 x 3) = 9/12; 5/6 = (5 x 2)/(6 x 2) = 10/12.\nb) Mẫu số chung là 18: 2/9 = (2 x 2)/(9 x 2) = 4/18; giữ nguyên phân số 7/18.", "a) 9/12 và 10/12; b) 4/18 và 7/18", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Điền dấu thích hợp (<, >, =) vào chỗ chấm:\na) 5/8 ... 7/8\nb) 4/5 ... 12/15\nc) 7/6 ... 1\nd) 8/9 ... 9/8", "a) 5/8 < 7/8 (vì 5 < 7)\nb) 4/5 = 12/15 (vì 4/5 = (4 x 3)/(5 x 3) = 12/15)\nc) 7/6 > 1 (vì tử số 7 > mẫu số 6)\nd) 8/9 < 1 mà 9/8 > 1 nên 8/9 < 9/8", "a) <; b) =; c) >; d) <", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một xe ô tô chở 45 bao hàng, mỗi bao nặng 50 kg. Sau đó người ta dỡ toàn bộ số hàng đó chia đều cho 15 cửa hàng. Hỏi mỗi cửa hàng nhận được bao nhiêu ki-lô-gam hàng?", "Tổng khối lượng hàng trên xe là:\n50 x 45 = 2250 (kg)\nMỗi cửa hàng nhận được số ki-lô-gam hàng là:\n2250 : 15 = 150 (kg)\nĐáp số: 150 kg.", "150 kg", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một tấm bìa hình bình hành có cạnh đáy 28 cm, chiều cao tương ứng bằng 3/4 cạnh đáy. Tính diện tích tấm bìa đó.", "Chiều cao của tấm bìa hình bình hành là:\n28 x 3 : 4 = 21 (cm)\nDiện tích tấm bìa hình bình hành là:\n28 x 21 = 588 (cm²)\nĐáp số: 588 cm².", "588 cm²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm một phân số có mẫu số là 25 và bằng phân số 3/5.", "Gọi tử số của phân số cần tìm là a.\nTheo đề bài ta có: a/25 = 3/5\nTa có: 3/5 = (3 x 5)/(5 x 5) = 15/25\nDo đó a = 15.\nVậy phân số cần tìm là 15/25.\nĐáp số: 15/25.", "15/25", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 05 (th4_gk2_de05)
    # =========================================================================
    exams["th4_gk2_de05"] = {
        "id": "th4_gk2_de05",
        "code": "GK2-DE05",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 05)",
        "grade": "4",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Khẳng định: \"Số 720 chia hết cho cả 2, 3, 5 và 9\" là đúng hay sai?", ["Đúng", "Sai", "Chỉ chia hết cho 2 và 5", "Chỉ chia hết cho 3 và 9"], 0, "720 có chữ số tận cùng 0 nên chia hết cho 2 và 5; tổng các chữ số 7+2+0=9 chia hết cho cả 3 và 9. Vậy khẳng định đúng.", "Thông hiểu"),
            make_mc(2, "Một hình vuông được chia đều làm 8 ô bằng nhau, người ta tô màu 3 ô. Phân số chỉ phần không tô màu là:", ["3/8", "5/8", "8/3", "5/3"], 1, "Số ô không tô màu là 8 - 3 = 5 ô. Phân số chỉ phần không tô màu là 5/8.", "Nhận biết"),
            make_mc(3, "Thương của phép chia 10 350 : 25 là:", ["414", "415", "412", "404"], 0, "10 350 : 25 = 414.", "Thông hiểu"),
            make_mc(4, "Phân số nào dưới đây bằng phân số 4/7?", ["8/21", "12/28", "16/28", "16/21"], 2, "4/7 = (4 x 4)/(7 x 4) = 16/28.", "Thông hiểu"),
            make_mc(5, "Một hình bình hành có diện tích 216 m² và độ dài đáy 18 m. Chiều cao của hình bình hành đó là:", ["12 m", "14 m", "16 m", "24 m"], 0, "Chiều cao = Diện tích : Đáy = 216 : 18 = 12 (m).", "Thông hiểu"),
            make_mc(6, "Trong các phân số 3/8, 5/8, 7/8, 1/8, phân số bé nhất là:", ["3/8", "5/8", "7/8", "1/8"], 3, "Các phân số cùng mẫu số 8, tử số bé nhất là 1 nên phân số bé nhất là 1/8.", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 63 945 : 9\nb) 8568 : 42", "a) 63 945 : 9 = 7105\nb) 8568 : 42 = 204", "a) 7105; b) 204", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Rút gọn các phân số sau:\na) 45/60\nb) 36/81", "a) 45/60 = (45 : 15)/(60 : 15) = 3/4\nb) 36/81 = (36 : 9)/(81 : 9) = 4/9", "a) 3/4; b) 4/9", 4, 1.0, "Thông hiểu"),
            make_essay(3, "So sánh hai phân số khác mẫu số:\na) 2/3 và 3/5\nb) 5/6 và 7/8", "a) Quy đồng: 2/3 = 10/15; 3/5 = 9/15. Vì 10/15 > 9/15 nên 2/3 > 3/5.\nb) Quy đồng mẫu số 24: 5/6 = 20/24; 7/8 = 21/24. Vì 20/24 < 21/24 nên 5/6 < 7/8.", "a) 2/3 > 3/5; b) 5/6 < 7/8", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một đội công nhân sửa được 2520 m đường trong 14 ngày. Hỏi với mức làm việc như vậy, trong 30 ngày đội công nhân đó sửa được bao nhiêu mét đường?", "Mỗi ngày đội công nhân sửa được số mét đường là:\n2520 : 14 = 180 (m)\nTrong 30 ngày đội công nhân sửa được số mét đường là:\n180 x 30 = 5400 (m)\nĐáp số: 5400 m đường.", "5400 m", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một thửa ruộng hình bình hành có độ dài đáy 32 m, chiều cao kém độ dài đáy 14 m. Người ta trồng ngô trên thửa ruộng đó, cứ 1 m² thu hoạch được 2 kg ngô. Hỏi cả thửa ruộng thu hoạch được bao nhiêu ki-lô-gam ngô?", "Chiều cao thửa ruộng là:\n32 - 14 = 18 (m)\nDiện tích thửa ruộng là:\n32 x 18 = 576 (m²)\nCả thửa ruộng thu hoạch được số ki-lô-gam ngô là:\n576 x 2 = 1152 (kg)\nĐáp số: 1152 kg ngô.", "1152 kg", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm số tự nhiên x biết: 15/x = 3/4.", "Ta có:\n3/4 = (3 x 5)/(4 x 5) = 15/20\nVì 15/x = 15/20 nên x = 20.\nĐáp số: x = 20.", "x = 20", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 06 (th4_gk2_de06)
    # =========================================================================
    exams["th4_gk2_de06"] = {
        "id": "th4_gk2_de06",
        "code": "GK2-DE06",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 06)",
        "grade": "4",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Số nào dưới đây chia hết cho 3 nhưng không chia hết cho 9?", ["180", "246", "369", "513"], 1, "246 có tổng các chữ số 2+4+6=12 chia hết cho 3 nhưng 12 không chia hết cho 9.", "Thông hiểu"),
            make_mc(2, "Trong phân số 11/17, số 17 được gọi là:", ["Tử số", "Mẫu số", "Thương số", "Số chia"], 1, "Số nằm dưới dấu gạch ngang của phân số được gọi là mẫu số.", "Nhận biết"),
            make_mc(3, "Kết quả của phép chia 9216 : 32 là:", ["288", "286", "298", "278"], 0, "9216 : 32 = 288.", "Thông hiểu"),
            make_mc(4, "Phân số nào dưới đây bé hơn 1?", ["7/6", "5/5", "6/7", "8/3"], 2, "Phân số có tử số bé hơn mẫu số thì bé hơn 1. Ta có 6 < 7 nên 6/7 < 1.", "Nhận biết"),
            make_mc(5, "Hai phân số 3/4 và 9/12 bằng nhau vì:", ["3 + 6 = 9 và 4 + 8 = 12", "Cùng nhân tử số và mẫu số của 3/4 với 3", "Cùng trừ tử số và mẫu số", "Không bằng nhau"], 1, "Khi nhân cả tử số và mẫu số của 3/4 với 3 ta được: (3 x 3)/(4 x 3) = 9/12.", "Nhận biết"),
            make_mc(6, "Một tấm kính hình bình hành có đáy 30 cm, chiều cao 15 cm. Diện tích của tấm kính đó là:", ["450 cm²", "225 cm²", "90 cm²", "45 cm²"], 0, "Diện tích = 30 x 15 = 450 (cm²).", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 42 756 : 6\nb) 9660 : 28", "a) 42 756 : 6 = 7126\nb) 9660 : 28 = 345", "a) 7126; b) 345", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết số thích hợp vào chỗ chấm:\na) 3/7 = 18/...\nb) 50/75 = .../3", "a) 18 : 3 = 6; vậy 3/7 = (3 x 6)/(7 x 6) = 18/42. Số cần điền là 42.\nb) 75 : 3 = 25; vậy 50/75 = (50 : 25)/(75 : 25) = 2/3. Số cần điền là 2.", "a) 42; b) 2", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Sắp xếp các phân số sau theo thứ tự từ lớn đến bé: 5/12, 11/12, 7/12, 1/12.", "Các phân số cùng mẫu số 12. So sánh tử số: 11 > 7 > 5 > 1.\nThứ tự từ lớn đến bé là: 11/12 ; 7/12 ; 5/12 ; 1/12.", "11/12 ; 7/12 ; 5/12 ; 1/12", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một trang trại có 1750 con gà được nuôi đều trong 25 chuồng. Người ta đã bán hết số gà ở 8 chuồng. Hỏi trang trại đó đã bán bao nhiêu con gà?", "Mỗi chuồng nuôi số con gà là:\n1750 : 25 = 70 (con)\nTrang trại đã bán số con gà là:\n70 x 8 = 560 (con)\nĐáp số: 560 con gà.", "560 con", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh đất hình bình hành có độ dài đáy là 40 m, chiều cao bằng 3/5 độ dài đáy. Tính diện tích mảnh đất đó.", "Chiều cao mảnh đất hình bình hành là:\n40 x 3 : 5 = 24 (m)\nDiện tích mảnh đất hình bình hành là:\n40 x 24 = 960 (m²)\nĐáp số: 960 m².", "960 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm các chữ số x và y để số 2x3y chia hết cho cả 2 và 5, đồng thời chia hết cho 3.", "Để 2x3y chia hết cho cả 2 và 5 thì y = 0. Ta được số 2x30.\nĐể 2x30 chia hết cho 3 thì (2 + x + 3 + 0) = (5 + x) chia hết cho 3.\nVì x là chữ số từ 0 đến 9 nên x có thể nhận các giá trị: 1, 4, 7.\nVậy các cặp chữ số (x, y) là: (1, 0); (4, 0); (7, 0).", "(x=1, y=0); (x=4, y=0); (x=7, y=0)", 5, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 07 (th4_gk2_de07)
    # =========================================================================
    exams["th4_gk2_de07"] = {
        "id": "th4_gk2_de07",
        "code": "GK2-DE07",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 07)",
        "grade": "4",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Dấu hiệu chia hết cho 5 là các số có chữ số tận cùng là:", ["0", "5", "0 hoặc 5", "Các chữ số chẵn"], 2, "Các số có chữ số tận cùng là 0 hoặc 5 thì chia hết cho 5.", "Nhận biết"),
            make_mc(2, "Trong các phân số 5/6, 6/5, 7/7, 8/9, phân số lớn hơn 1 là:", ["5/6", "6/5", "7/7", "8/9"], 1, "Phân số 6/5 có tử số lớn hơn mẫu số (6 > 5) nên 6/5 > 1.", "Nhận biết"),
            make_mc(3, "Kết quả của phép chia 12 768 : 42 là:", ["304", "34", "340", "314"], 0, "12 768 : 42 = 304.", "Thông hiểu"),
            make_mc(4, "Phân số tối giản của 36/48 là:", ["6/8", "9/12", "3/4", "18/24"], 2, "36/48 = (36 : 12)/(48 : 12) = 3/4.", "Thông hiểu"),
            make_mc(5, "Một hình bình hành có độ dài đáy 22 cm và chiều cao 15 cm. Diện tích của hình bình hành đó là:", ["330 cm²", "165 cm²", "37 cm²", "74 cm²"], 0, "Diện tích = 22 x 15 = 330 (cm²).", "Thông hiểu"),
            make_mc(6, "So sánh hai phân số 4/9 và 2/3:", ["4/9 > 2/3", "4/9 < 2/3", "4/9 = 2/3", "Không so sánh được"], 1, "Ta có 2/3 = 6/9. Vì 4/9 < 6/9 nên 4/9 < 2/3.", "Thông hiểu")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 56 480 : 8\nb) 11 088 : 36", "a) 56 480 : 8 = 7060\nb) 11 088 : 36 = 308", "a) 7060; b) 308", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Rút gọn các phân số sau:\na) 20/30\nb) 27/63", "a) 20/30 = (20 : 10)/(30 : 10) = 2/3\nb) 27/63 = (27 : 9)/(63 : 9) = 3/7", "a) 2/3; b) 3/7", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Quy đồng mẫu số hai phân số:\na) 4/5 và 3/10\nb) 2/3 và 5/7", "a) Mẫu số chung là 10: 4/5 = (4 x 2)/(5 x 2) = 8/10; giữ nguyên phân số 3/10.\nb) Mẫu số chung là 21: 2/3 = (2 x 7)/(3 x 7) = 14/21; 5/7 = (5 x 3)/(7 x 3) = 15/21.", "a) 8/10 và 3/10; b) 14/21 và 15/21", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một kho hàng nhập về 1920 thùng sữa chia đều cho 32 siêu thị. Mỗi thùng sữa chứa 24 hộp. Hỏi mỗi siêu thị nhận được bao nhiêu hộp sữa?", "Mỗi siêu thị nhận được số thùng sữa là:\n1920 : 32 = 60 (thùng)\nMỗi siêu thị nhận được số hộp sữa là:\n60 x 24 = 1440 (hộp)\nĐáp số: 1440 hộp sữa.", "1440 hộp", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một biển quảng cáo hình bình hành có độ dài đáy 50 dm, chiều cao bằng một nửa độ dài đáy. Tính diện tích của biển quảng cáo đó theo đơn vị đề-xi-mét vuông.", "Chiều cao của biển quảng cáo là:\n50 : 2 = 25 (dm)\nDiện tích của biển quảng cáo là:\n50 x 25 = 1250 (dm²)\nĐáp số: 1250 dm².", "1250 dm²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm một phân số có mẫu số là 12, biết rằng phân số đó lớn hơn 1/3 và bé hơn 1/2.", "Quy đồng mẫu số hai phân số 1/3 và 1/2 với mẫu số 12:\n1/3 = (1 x 4)/(3 x 4) = 4/12\n1/2 = (1 x 6)/(2 x 6) = 6/12\nPhân số có mẫu số là 12 nằm giữa 4/12 và 6/12 là 5/12.\nĐáp số: 5/12.", "5/12", 4, 1.0, "Vận dụng cao")
        ]
    }

    # =========================================================================
    # ĐỀ SỐ 08 (th4_gk2_de08)
    # =========================================================================
    exams["th4_gk2_de08"] = {
        "id": "th4_gk2_de08",
        "code": "GK2-DE08",
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KÌ 2 - TOÁN 4 (ĐỀ SỐ 08)",
        "grade": "4",
        "term": "gk2",
        "termName": "Giữa Học Kì 2",
        "duration": "40 phút",
        "points": 10.0,
        "totalPoints": 10.0,
        "part1": [
            make_mc(1, "Tổng các chữ số của số 4383 là:", ["15", "18", "16", "20"], 1, "4 + 3 + 8 + 3 = 18 (chia hết cho 9).", "Nhận biết"),
            make_mc(2, "Cho phân số 8/15. Cần cộng thêm vào tử số bao nhiêu đơn vị để được phân số bằng 1?", ["5", "7", "8", "15"], 1, "Để phân số bằng 1 thì tử số phải bằng 15. Ta cần cộng thêm: 15 - 8 = 7 đơn vị.", "Thông hiểu"),
            make_mc(3, "Kết quả của phép chia 15 870 : 69 là:", ["230", "23", "203", "235"], 0, "15 870 : 69 = 230.", "Thông hiểu"),
            make_mc(4, "Phân số nào sau đây bằng phân số 2/7?", ["4/21", "6/28", "10/35", "8/35"], 2, "2/7 = (2 x 5)/(7 x 5) = 10/35.", "Thông hiểu"),
            make_mc(5, "Một hình bình hành có diện tích 450 m² và chiều cao 15 m. Độ dài đáy tương ứng là:", ["30 m", "15 m", "45 m", "60 m"], 0, "Độ dài đáy = 450 : 15 = 30 (m).", "Thông hiểu"),
            make_mc(6, "Trong các phân số 1/3, 1/4, 1/5, 1/6, phân số lớn nhất là:", ["1/6", "1/5", "1/4", "1/3"], 3, "Các phân số cùng tử số là 1, mẫu số bé nhất là 3 nên phân số lớn nhất là 1/3.", "Nhận biết")
        ],
        "part2": [
            make_essay(1, "Đặt tính rồi tính:\na) 48 375 : 5\nb) 13 464 : 44", "a) 48 375 : 5 = 9675\nb) 13 464 : 44 = 306", "a) 9675; b) 306", 4, 1.0, "Thông hiểu"),
            make_essay(2, "Viết các phân số sau theo thứ tự từ bé đến lớn: 3/8, 5/8, 1/8, 7/8.", "Vì các phân số đều có mẫu số là 8, so sánh tử số: 1 < 3 < 5 < 7.\nThứ tự từ bé đến lớn là: 1/8 ; 3/8 ; 5/8 ; 7/8.", "1/8 ; 3/8 ; 5/8 ; 7/8", 4, 1.0, "Thông hiểu"),
            make_essay(3, "Rút gọn rồi so sánh hai phân số 6/10 và 12/20.", "Ta có:\n6/10 = (6 : 2)/(10 : 2) = 3/5\n12/20 = (12 : 4)/(20 : 4) = 3/5\nVì cùng rút gọn về phân số 3/5 nên 6/10 = 12/20.", "6/10 = 12/20", 4, 1.0, "Thông hiểu"),
            make_essay(4, "Một trường tiểu học có 1260 quyển sách được chia đều vào 28 giá sách của thư viện. Cô phụ trách thư viện đã chuyển sách từ 12 giá sách vào các lớp học. Hỏi cô đã chuyển đi bao nhiêu quyển sách?", "Mỗi giá sách chứa số quyển sách là:\n1260 : 28 = 45 (quyển)\nCô phụ trách thư viện đã chuyển đi số quyển sách là:\n45 x 12 = 540 (quyển)\nĐáp số: 540 quyển sách.", "540 quyển", 5, 1.5, "Vận dụng"),
            make_essay(5, "Một mảnh vườn hình bình hành có độ dài đáy là 25 m, chiều cao kém độ dài đáy 7 m. Tính diện tích của mảnh vườn đó.", "Chiều cao của mảnh vườn là:\n25 - 7 = 18 (m)\nDiện tích mảnh vườn hình bình hành là:\n25 x 18 = 450 (m²)\nĐáp số: 450 m².", "450 m²", 5, 1.5, "Vận dụng"),
            make_essay(6, "Tìm chữ số tận cùng của tích sau: 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9.", "Trong tích trên có thừa số 2 và thừa số 5. Mà 2 x 5 = 10.\nKhi nhân một số tự nhiên với 10 thì tích luôn có chữ số tận cùng là 0.\nDo đó tích 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 có chữ số tận cùng là 0.\nĐáp số: 0.", "0", 4, 1.0, "Vận dụng cao")
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_th4_gk2_exams()
    print(f"Tổng số đề GK2 Toán 4: {len(ex)} (Kỳ vọng: 8 đề)")
    for eid, e in ex.items():
        print(f"[{eid}] {e['title']} - Part 1: {len(e['part1'])}, Part 2: {len(e['part2'])}")
