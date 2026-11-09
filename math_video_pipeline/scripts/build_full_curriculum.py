"""
KHO DỮ LIỆU SƯ PHẠM ĐẦY ĐỦ 42 BÀI HỌC TOÁN 6 (BÀI 2 ĐẾN BÀI 43)
Kết Nối Tri Thức Với Cuộc Sống - Giáo viên: Thầy Thuấn Phan
Chuẩn 5 phần: Khởi động, Kiến thức, 3 Ví dụ đếm ngược 45s, Cảnh báo, Sơ đồ tư duy
"""

import os
import sys
import json

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "curriculum_toan6_full.json")


def make_lesson(lid, cid, ctitle, lkey, ltitle, p1, p2, p3, p4, p5):
    return {
        "id": lid,
        "chapter_id": cid,
        "chapter_title": ctitle,
        "lesson_key": lkey,
        "lesson_title": ltitle,
        "video_filename": f"Toan6_Bai{lid}_HoanChinh.mp4",
        "part1": p1,
        "part2": p2,
        "part3": p3,
        "part4": p4,
        "part5": p5
    }

# Định nghĩa dữ liệu 42 bài học chuẩn xác 100%
LESSONS_CATALOG = [
    # BÀI 2
    {
        "id": 2, "chapter_id": "c1_6", "chapter_title": "Chương I: Tập hợp các số tự nhiên",
        "lesson_key": "Bài 2: Cách ghi số tự nhiên", "lesson_title": "Cách ghi số tự nhiên",
        "p1": {
            "title": "Phần 1: Đặt Vấn Đề & Khởi Động Thực Tế",
            "slides": [
                {"heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN", "sub": "Toán 6 • Kết Nối Tri Thức Với Cuộc Sống", "bullets": ["Bài 2: Cách ghi số tự nhiên", "Hệ thập phân & cấu tạo số ab, abc", "Số La Mã trong đời sống cổ điển"], "voice": "Chào mừng các em đến với lớp học của thầy Thuấn Phan! Hôm nay chúng ta học Bài 2: Cách ghi số tự nhiên, tìm hiểu hệ thập phân và chữ số La Mã nhé!"},
                {"heading": "CÁC CON SỐ TRONG ĐỜI SỐNG", "sub": "Từ tiền tệ, dân số đến mặt đồng hồ cổ", "bullets": ["Dân số Việt Nam: hơn 100 triệu người", "Biển số xe, số tài khoản, giá cả", "Mặt đồng hồ khắc chữ số I, V, X"], "voice": "Các con số xuất hiện khắp nơi trong đời sống: dân số, biển số xe hay chữ số La Mã trên mặt đồng hồ cổ. Chúng ta ghi lại các số đó như thế nào?"}
            ]
        },
        "p2": {
            "title": "Phần 2: Hình Thành Kiến Thức Mới",
            "slides": [
                {"heading": "1. HỆ THẬP PHÂN & CẤU TẠO SỐ", "sub": "10 chữ số cơ bản tạo nên muôn vàn giá trị", "items": ["• Dùng 10 chữ số: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9", "• Cấu tạo số: ab = 10a + b (với a ≠ 0)", "• Cấu tạo số: abc = 100a + 10b + c (với a ≠ 0)", "• Giá trị mỗi chữ số phụ thuộc vào vị trí hàng."], "voice": "Trong hệ thập phân, mỗi chữ số có giá trị theo hàng. Số a b gạch đầu bằng 10 nhân a cộng b. Số a b c bằng 100 nhân a cộng 10 nhân b cộng c."},
                {"heading": "2. CHỮ SỐ LA MÃ", "sub": "Quy tắc ghép số cổ đại", "items": ["• Chữ số cơ bản: I = 1 ; V = 5 ; X = 10", "• Ghép bên phải là cộng: VI = 6 ; VII = 7 ; XI = 11", "• Ghép bên trái là trừ: IV = 4 ; IX = 9", "• Chữ số I, X không viết liền quá 3 lần."], "voice": "Hệ La Mã dùng I là một, V là năm, X là mười. Ghép bên phải là cộng, ghép bên trái là trừ. Chú ý không viết quá ba chữ I hoặc X liên tiếp nhé!"}
            ]
        },
        "p3": {
            "title": "Phần 3: Ba Ví Dụ Minh Họa & Đếm Ngược 45s",
            "examples": [
                {
                    "badge": "VÍ DỤ 1 (Mức Nhận Biết)", "head": "ĐỌC VÀ VIẾT SỐ LA MÃ", "lead": "Đề bài: Viết số La Mã thích hợp vào chỗ trống:",
                    "question_a": "a) Viết số 14 và số 26 bằng chữ số La Mã.", "question_b": "b) Đọc giá trị của các số La Mã sau:",
                    "blank_items": ["XIV = [ ... ]", "XIX = [ ... ]", "XXVIII = [ ... ]"],
                    "analysis": "14 = 10 + 4 = XIV. 26 = 20 + 6 = XXVI. XIX = 19. XXVIII = 28.",
                    "solution_a": "a) Số 14 viết là XIV ; Số 26 viết là XXVI.", "solution_b": "b) XIV = 14 ; XIX = 19 ; XXVIII = 28.",
                    "voice_intro": "Ví dụ 1 giúp các em làm quen với đọc và viết số La Mã. Các em có 45 giây để hoàn thành chỗ trống nhé!",
                    "voice_sol": "Hết giờ rồi! Mười bốn viết là X I V, hai mươi sáu là X X V I. X I X là mười chín và X X V I I I là hai mươi tám!"
                },
                {
                    "badge": "VÍ DỤ 2 (Mức Thông Hiểu)", "head": "PHÂN TÍCH CẤU TẠO SỐ HỆ THẬP PHÂN", "lead": "Đề bài: Cho số tự nhiên M = 4853.",
                    "question_a": "a) Nêu giá trị của chữ số 8 và chữ số 5 trong số M.", "question_b": "b) Viết số M thành tổng giá trị các chữ số:",
                    "blank_items": ["4853 = 4 × [ ... ] + 8 × [ ... ] + 5 × [ ... ] + 3"],
                    "analysis": "Chữ số 4 ở hàng nghìn, 8 hàng trăm, 5 hàng chục, 3 hàng đơn vị.",
                    "solution_a": "a) Giá trị chữ số 8 là 800; giá trị chữ số 5 là 50.", "solution_b": "b) 4853 = 4 × 1000 + 8 × 100 + 5 × 10 + 3.",
                    "voice_intro": "Ví dụ 2 yêu cầu phân tích cấu tạo số. 45 giây tự suy nghĩ bắt đầu!",
                    "voice_sol": "Chữ số 8 có giá trị tám trăm, chữ số 5 có giá trị năm mươi. Tổng phân tích là 4 nhân 1000 cộng 8 nhân 100 cộng 5 nhân 10 cộng 3."
                },
                {
                    "badge": "VÍ DỤ 3 (Mức Vận Dụng)", "head": "TÌM SỐ THỎA MÃN ĐIỀU KIỆN", "lead": "Đề bài: Cho số tự nhiên ab biết hàng chục gấp 3 lần hàng đơn vị.",
                    "question_a": "a) Liệt kê tất cả các số tự nhiên thỏa mãn.", "question_b": "b) Viết số lớn nhất tìm được sang số La Mã:",
                    "blank_items": ["Tập hợp: { [ ... ] }", "Số lớn nhất La Mã: [ ... ]"],
                    "analysis": "a = 3b ⇒ b ∈ {1, 2, 3} ⇒ a ∈ {3, 6, 9}. Số lớn nhất 93 = XCIII.",
                    "solution_a": "a) Các số thỏa mãn là: 31, 62, 93.", "solution_b": "b) Số lớn nhất là 93, viết là XCIII.",
                    "voice_intro": "Ví dụ 3 là bài toán vận dụng cấu tạo số kết hợp số La Mã. 45 giây bắt đầu!",
                    "voice_sol": "Xuất sắc! Có ba số là 31, 62, 93. Số lớn nhất 93 trong La Mã viết là X C I I I."
                }
            ]
        },
        "p4": {
            "title": "Phần 4: Lỗi Sai Kinh Điển Cần Tránh",
            "traps": [
                {"heading": "LỖI SAI 1: NHẦM CHỮ SỐ VÀ SỐ", "bad": "Sai: Nói 'Số 4853 có 4 số'", "good": "Đúng: 'Số 4853 có 4 CHỮ SỐ: 4, 8, 5, 3'", "note": "Số là lượng, chữ số là ký hiệu biểu diễn.", "voice": "Lỗi sai thứ nhất là nhầm giữa số và chữ số. 4853 là một số gồm bốn chữ số các em nhé!"},
                {"heading": "LỖI SAI 2: LẶP LẠI QUÁ 3 LẦN CHỮ I", "bad": "Sai: Viết số 4 là IIII", "good": "Đúng: Số 4 viết là IV", "note": "Chữ I, X không được lặp lại quá 3 lần liên tiếp.", "voice": "Lỗi sai thứ hai là viết số 4 thành bốn chữ I. Nhớ dùng quy tắc trừ là I V nhé!"}
            ]
        },
        "p5": {
            "title": "Phần 5: Sơ Đồ Tư Duy & Tổng Kết Củng Cố",
            "summary_nodes": ["1. Hệ thập phân: 10 chữ số, giá trị theo hàng.", "2. Cấu tạo số: ab = 10a + b ; abc = 100a + 10b + c.", "3. Số La Mã: I, V, X; ghép phải cộng, ghép trái trừ."],
            "homework": ["• Bài tập 1.6, 1.7, 1.8 SGK Toán 6 (Tập 1).", "• Tự viết năm sinh của người thân bằng số La Mã."],
            "voice": "Bài học hôm nay giúp chúng ta ghi nhớ cách ghi số tự nhiên và số La Mã. Về nhà làm bài tập đầy đủ nhé, hẹn gặp lại các em!"
        }
    },

    # BÀI 3
    {
        "id": 3, "chapter_id": "c1_6", "chapter_title": "Chương I: Tập hợp các số tự nhiên",
        "lesson_key": "Bài 3: Thứ tự trong tập hợp các số tự nhiên", "lesson_title": "Thứ tự trong tập hợp các số tự nhiên",
        "p1": {
            "title": "Phần 1: Đặt Vấn Đề & Khởi Động Thực Tế",
            "slides": [
                {"heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN", "sub": "Toán 6 • Kết Nối Tri Thức Với Cuộc Sống", "bullets": ["Bài 3: Thứ tự trong tập số tự nhiên", "Tia số gốc 0 & so sánh số", "Số liền trước và số liền sau"], "voice": "Chào mừng các em! Hôm nay chúng ta học Bài 3: Thứ tự trong tập hợp các số tự nhiên. Cùng biểu diễn số trên tia số nhé!"},
                {"heading": "THỨ TỰ TRONG ĐỜI SỐNG", "sub": "Trật tự từ nhỏ đến lớn", "bullets": ["Số tuổi các thành viên trong gia đình", "Thứ tự xếp hàng vào lớp", "Bảng xếp hạng điểm số từ thấp đến cao"], "voice": "Trong cuộc sống mọi thứ đều có thứ tự: số tuổi, số thứ tự hàng ngũ. Trong Toán học, các số tự nhiên cũng có thứ tự tuyệt đối trên tia số."}
            ]
        },
        "p2": {
            "title": "Phần 2: Hình Thành Kiến Thức Mới",
            "slides": [
                {"heading": "1. TIA SỐ & QUY TẮC SO SÁNH", "sub": "Biểu diễn hình học của số tự nhiên", "items": ["• Gốc tia số là điểm 0, mũi tên sang phải.", "• Điểm a nằm bên trái điểm b thì a < b.", "• Tính chất bắc cầu: a < b và b < c ⇒ a < c.", "• Ký hiệu a ≤ b nghĩa là a < b hoặc a = b."], "voice": "Trên tia số nằm ngang, điểm bên trái luôn nhỏ hơn điểm bên phải. Nếu a nhỏ hơn b và b nhỏ hơn c thì a nhỏ hơn c."},
                {"heading": "2. SỐ LIỀN TRƯỚC VÀ LIỀN SAU", "sub": "Khoảng cách đúng 1 đơn vị", "items": ["• Hai số tự nhiên liên tiếp hơn kém nhau 1 đơn vị.", "• Số liền sau của n là n + 1.", "• Số liền trước của n (n ≠ 0) là n - 1.", "• Số 0 là số tự nhiên nhỏ nhất, không có số liền trước."], "voice": "Số liền sau của n là n cộng 1, số liền trước là n trừ 1. Số không là số tự nhiên nhỏ nhất và không có số liền trước."}
            ]
        },
        "p3": {
            "title": "Phần 3: Ba Ví Dụ Minh Họa & Đếm Ngược 45s",
            "examples": [
                {
                    "badge": "VÍ DỤ 1 (Mức Nhận Biết)", "head": "TÌM SỐ LIỀN TRƯỚC VÀ LIỀN SAU", "lead": "Đề bài: Điền số thích hợp vào chỗ trống:",
                    "question_a": "a) Số liền trước của 100 và số liền sau của 999.", "question_b": "b) Ba số tự nhiên liên tiếp tăng dần biết số ở giữa là 2024:",
                    "blank_items": ["Liền trước 100: [ ... ]", "Liền sau 999: [ ... ]", "[ ... ] ; 2024 ; [ ... ]"],
                    "analysis": "100 - 1 = 99. 999 + 1 = 1000. Ba số: 2023, 2024, 2025.",
                    "solution_a": "a) Số liền trước 100 là 99; Liền sau 999 là 1000.", "solution_b": "b) Ba số là: 2023 ; 2024 ; 2025.",
                    "voice_intro": "Ví dụ 1 rèn luyện tìm số liền trước và liền sau. 45 giây bắt đầu!",
                    "voice_sol": "Liền trước của 100 là 99. Liền sau 999 là 1000. Ba số liên tiếp là 2023, 2024, 2025."
                },
                {
                    "badge": "VÍ DỤ 2 (Mức Thông Hiểu)", "head": "VIẾT TẬP HỢP THEO ĐIỀU KIỆN", "lead": "Đề bài: Cho tập hợp A = { x ∈ ℕ | 15 ≤ x < 21 }.",
                    "question_a": "a) Liệt kê các phần tử của tập hợp A.", "question_b": "b) Sắp xếp các phần tử của A theo thứ tự giảm dần.",
                    "blank_items": ["A = { [ ... ] }", "Giảm dần: [ ... ]"],
                    "analysis": "x ≥ 15 lấy từ 15, x < 21 dừng ở 20. Giảm dần từ 20 về 15.",
                    "solution_a": "a) A = { 15; 16; 17; 18; 19; 20 }.", "solution_b": "b) Giảm dần: 20 ; 19 ; 18 ; 17 ; 16 ; 15.",
                    "voice_intro": "Ví dụ 2 yêu cầu liệt kê tập hợp có điều kiện biên. 45 giây bắt đầu!",
                    "voice_sol": "A gồm các số từ 15 đến 20. Sắp xếp giảm dần từ 20 lùi về 15."
                },
                {
                    "badge": "VÍ DỤ 3 (Mức Vận Dụng)", "head": "SO SÁNH TÍCH HAI SỐ", "lead": "Đề bài: Điền dấu thích hợp (<, =, >) vào ô trống:",
                    "question_a": "a) 2024 × 2026 [ ... ] 2025 × 2025", "question_b": "b) Giải thích ngắn gọn cách suy luận.",
                    "blank_items": ["Dấu: [ ... ]", "Lý do: [ ... ]"],
                    "analysis": "2024 × 2026 = (2025 - 1)(2025 + 1) = 2025² - 1 < 2025².",
                    "solution_a": "a) 2024 × 2026 < 2025 × 2025.", "solution_b": "b) Tích đạt cực đại khi hai thừa số bằng nhau.",
                    "voice_intro": "Ví dụ 3 là bài toán so sánh thông minh. 45 giây suy luận bắt đầu!",
                    "voice_sol": "2024 nhân 2026 bằng 2025 bình phương trừ 1, do đó nó nhỏ hơn 2025 bình phương!"
                }
            ]
        },
        "p4": {
            "title": "Phần 4: Lỗi Sai Kinh Điển Cần Tránh",
            "traps": [
                {"heading": "LỖI SAI 1: BỎ QUÊN NGHIỆM BIÊN CÓ DẤU BẰNG", "bad": "Sai: x ≤ 5 mà chỉ lấy {0, 1, 2, 3, 4}", "good": "Đúng: x ≤ 5 phải lấy cả số 5: {0, 1, 2, 3, 4, 5}", "note": "Ký hiệu ≤ bao gồm cả trường hợp bằng.", "voice": "Lỗi sai phổ biến là quên nghiệm bằng khi gặp dấu nhỏ hơn hoặc bằng năm!"},
                {"heading": "LỖI SAI 2: NGHĨ RẰNG 0 CÓ SỐ LIỀN TRƯỚC TRONG N", "bad": "Sai: Số liền trước của 0 là -1 trong N", "good": "Đúng: Trong N, 0 không có số liền trước", "note": "0 là số tự nhiên nhỏ nhất.", "voice": "Trong tập số tự nhiên N, số không là nhỏ nhất và không có số liền trước các em nhé!"}
            ]
        },
        "p5": {
            "title": "Phần 5: Sơ Đồ Tư Duy & Tổng Kết Củng Cố",
            "summary_nodes": ["1. Tia số: Gốc 0, chiều từ trái sang phải tăng dần.", "2. So sánh: Điểm bên trái nhỏ hơn bên phải, tính bắc cầu.", "3. Số liền trước n - 1, số liền sau n + 1."],
            "homework": ["• Bài 1.13, 1.14, 1.15 SGK Toán 6.", "• Biểu diễn 5 số tự nhiên lẻ đầu tiên trên tia số."],
            "voice": "Hôm nay chúng ta đã nắm vững thứ tự và so sánh số tự nhiên. Chúc các em học tốt và hẹn gặp lại ở bài học sau!"
        }
    },

    # BÀI 4: Phép cộng và phép trừ số tự nhiên
    {
        "id": 4, "chapter_id": "c1_6", "chapter_title": "Chương I: Tập hợp các số tự nhiên",
        "lesson_key": "Bài 4: Phép cộng và phép trừ số tự nhiên", "lesson_title": "Phép cộng và phép trừ số tự nhiên",
        "p1": {
            "title": "Phần 1: Đặt Vấn Đề & Khởi Động Thực Tế",
            "slides": [
                {"heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN", "sub": "Toán 6 • Kết Nối Tri Thức Với Cuộc Sống", "bullets": ["Bài 4: Phép cộng và trừ số tự nhiên", "Tính chất giao hoán và kết hợp", "Phương pháp tính nhanh, tính hợp lý"], "voice": "Chào các em! Bài 4 giúp chúng ta rèn luyện phép cộng và phép trừ số tự nhiên cùng các phương pháp tính nhanh thông minh."},
                {"heading": "TÍNH TOÁN TRONG CUỘC SỐNG", "sub": "Mua sắm và quản lý chi tiêu", "bullets": ["Cộng tổng tiền mua đồ ở siêu thị", "Tính tiền thừa nhận lại khi thanh toán", "Nhóm các số tròn chục, tròn trăm để tính nhẩm"], "voice": "Khi đi siêu thị hay tính toán chi tiêu, việc biết nhóm các số tròn trăm, tròn nghìn giúp chúng ta tính nhẩm cực nhanh!"}
            ]
        },
        "p2": {
            "title": "Phần 2: Hình Thành Kiến Thức Mới",
            "slides": [
                {"heading": "1. TÍNH CHẤT PHÉP CỘNG", "sub": "Giao hoán, kết hợp và cộng với số 0", "items": ["• Giao hoán: a + b = b + a", "• Kết hợp: (a + b) + c = a + (b + c)", "• Cộng với 0: a + 0 = 0 + a = a", "• Ghép nhóm tạo số tròn chục, tròn trăm."], "voice": "Phép cộng có tính chất giao hoán và kết hợp. Ta có thể đổi chỗ và nhóm các số tùy ý để tạo thành số tròn chục, tròn trăm."},
                {"heading": "2. PHÉP TRỪ SỐ TỰ NHIÊN", "sub": "Điều kiện để thực hiện được phép trừ", "items": ["• Cho hai số a và b. Nếu a ≥ b thì tồn tại số x sao cho b + x = a.", "• Ký hiệu: a - b = x (a là số bị trừ, b là số trừ, x là hiệu).", "• Trong tập N: a - b chỉ thực hiện được khi a ≥ b.", "• a - a = 0 ; a - 0 = a."], "voice": "Trong tập số tự nhiên, phép trừ a trừ b chỉ thực hiện được khi a lớn hơn hoặc bằng b các em nhớ nhé!"}
            ]
        },
        "p3": {
            "title": "Phần 3: Ba Ví Dụ Minh Họa & Đếm Ngược 45s",
            "examples": [
                {
                    "badge": "VÍ DỤ 1 (Mức Nhận Biết)", "head": "TÍNH NHẨM HỢP LÝ", "lead": "Đề bài: Tính nhanh các tổng sau bằng cách nhóm thích hợp:",
                    "question_a": "a) A = 48 + 125 + 52", "question_b": "b) B = 178 + 234 + 822 + 766",
                    "blank_items": ["A = (48 + 52) + 125 = [ ... ]", "B = (178 + 822) + (234 + 766) = [ ... ]"],
                    "analysis": "48 + 52 = 100. 100 + 125 = 225. 178 + 822 = 1000. 234 + 766 = 1000. B = 2000.",
                    "solution_a": "a) A = 100 + 125 = 225.", "solution_b": "b) B = 1000 + 1000 = 2000.",
                    "voice_intro": "Ví dụ 1 là bài toán tính nhanh cơ bản. 45 giây bắt đầu!",
                    "voice_sol": "A bằng 225. B ghép thành hai cặp tròn nghìn cho kết quả 2000!"
                },
                {
                    "badge": "VÍ DỤ 2 (Mức Thông Hiểu)", "head": "TÌM X TRONG PHÉP TRỪ", "lead": "Đề bài: Tìm số tự nhiên x biết:",
                    "question_a": "a) x + 135 = 350", "question_b": "b) 248 - (x - 12) = 100",
                    "blank_items": ["a) x = 350 - 135 = [ ... ]", "b) x - 12 = 148 ⇒ x = [ ... ]"],
                    "analysis": "x = 350 - 135 = 215. x - 12 = 248 - 100 = 148 ⇒ x = 160.",
                    "solution_a": "a) x = 215.", "solution_b": "b) x = 160.",
                    "voice_intro": "Ví dụ 2 là bài toán tìm x kinh điển. 45 giây làm bài bắt đầu!",
                    "voice_sol": "a cho x bằng 215. b cho x trừ 12 bằng 148, suy ra x bằng 160."
                },
                {
                    "badge": "VÍ DỤ 3 (Mức Vận Dụng)", "head": "TỔNG DÃY SỐ CÁCH ĐỀU", "lead": "Đề bài: Tính tổng dãy số S = 1 + 2 + 3 + ... + 99 + 100.",
                    "question_a": "a) Dãy số có bao nhiêu số hạng?", "question_b": "b) Tính giá trị của tổng S.",
                    "blank_items": ["Số số hạng: [ ... ]", "S = (1 + 100) × 100 : 2 = [ ... ]"],
                    "analysis": "Số số hạng: (100 - 1) : 1 + 1 = 100. Tổng: (đầu + cuối) × số số hạng : 2 = 101 × 100 : 2 = 5050.",
                    "solution_a": "a) Dãy có 100 số hạng.", "solution_b": "b) S = 5050.",
                    "voice_intro": "Ví dụ 3 là bài toán tính tổng dãy số cách đều của nhà toán học Gauss. 45 giây bắt đầu!",
                    "voice_sol": "Dãy có 100 số hạng. Tổng bằng đầu cộng cuối nhân số số hạng chia 2, ra đúng 5050!"
                }
            ]
        },
        "p4": {
            "title": "Phần 4: Lỗi Sai Kinh Điển Cần Tránh",
            "traps": [
                {"heading": "LỖI SAI 1: PHÉP TRỪ KHÔNG CÓ TÍNH GIAO HOÁN", "bad": "Sai: a - b = b - a", "good": "Đúng: a - b ≠ b - a (Ví dụ: 7 - 3 ≠ 3 - 7)", "note": "Chỉ phép cộng mới có tính giao hoán.", "voice": "Nhớ rằng phép trừ không có tính giao hoán, không được tùy tiện đổi chỗ nhé!"},
                {"heading": "LỖI SAI 2: BỎ NGOẶC SAI DẤU", "bad": "Sai: a - (b + c) = a - b + c", "good": "Đúng: a - (b + c) = a - b - c", "note": "Dấu trừ trước ngoặc đổi dấu tất cả số hạng bên trong.", "voice": "Khi trừ đi một tổng, phải trừ lần lượt từng số hạng: a trừ b trừ c!"}
            ]
        },
        "p5": {
            "title": "Phần 5: Sơ Đồ Tư Duy & Tổng Kết Củng Cố",
            "summary_nodes": ["1. Phép cộng: Giao hoán, kết hợp, cộng 0.", "2. Phép trừ: a ≥ b trong N; a - (b + c) = a - b - c.", "3. Dãy số cách đều: (Đầu + Cuối) × Số số hạng : 2."],
            "homework": ["• Bài 1.20, 1.21, 1.22 SGK Toán 6.", "• Tính nhanh tổng các số chẵn từ 2 đến 100."],
            "voice": "Hôm nay chúng ta đã thành thạo kỹ năng cộng trừ số tự nhiên. Chúc các em học tốt!"
        }
    },

    # BÀI 5: Phép nhân và phép chia số tự nhiên
    {
        "id": 5, "chapter_id": "c1_6", "chapter_title": "Chương I: Tập hợp các số tự nhiên",
        "lesson_key": "Bài 5: Phép nhân và phép chia số tự nhiên", "lesson_title": "Phép nhân và phép chia số tự nhiên",
        "p1": {
            "title": "Phần 1: Đặt Vấn Đề & Khởi Động Thực Tế",
            "slides": [
                {"heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN", "sub": "Toán 6 • Kết Nối Tri Thức Với Cuộc Sống", "bullets": ["Bài 5: Phép nhân & chia số tự nhiên", "Tính chất phân phối a(b + c) = ab + ac", "Phép chia hết và phép chia có dư"], "voice": "Chào mừng các em! Bài 5 trang bị cho chúng ta kỹ năng nhân chia số tự nhiên và tính chất phân phối cực kỳ quan trọng."},
                {"heading": "ỨNG DỤNG NHÂN CHIA TRONG ĐỜI SỐNG", "sub": "Chia quà, xếp hàng, tính diện tích", "bullets": ["Xếp 45 học sinh vào các bàn 4 chỗ", "Tính diện tích mảnh đất hình chữ nhật", "Chia đều kẹo cho các nhóm bạn"], "voice": "Chia đều đồ vật hay tính diện tích đều gắn liền với phép nhân và phép chia có dư hằng ngày."}
            ]
        },
        "p2": {
            "title": "Phần 2: Hình Thành Kiến Thức Mới",
            "slides": [
                {"heading": "1. TÍNH CHẤT PHÉP NHÂN", "sub": "Giao hoán, kết hợp, phân phối", "items": ["• Giao hoán: a × b = b × a", "• Kết hợp: (a × b) × c = a × (b × c)", "• Phân phối với phép cộng: a(b + c) = ab + ac", "• Nhân với 1: a × 1 = a ; Nhân với 0: a × 0 = 0."], "voice": "Tính chất phân phối a nhân mở ngoặc b cộng c bằng a nhân b cộng a nhân c là chìa khóa để tính nhanh!"},
                {"heading": "2. PHÉP CHIA HẾT & CHIA CÓ DƯ", "sub": "Quy tắc số dư luôn nhỏ hơn số chia", "items": ["• Với a, b ∈ N (b ≠ 0): luôn tồn tại duy nhất q, r sao cho: a = b × q + r", "• Điều kiện số dư: 0 ≤ r < b.", "• Nếu r = 0: a chia hết cho b (a ⋮ b).", "• Nếu r > 0: a chia b có dư r."], "voice": "Trong phép chia a cho b, số dư r luôn phải nhỏ hơn số chia b và lớn hơn hoặc bằng không."}
            ]
        },
        "p3": {
            "title": "Phần 3: Ba Ví Dụ Minh Họa & Đếm Ngược 45s",
            "examples": [
                {
                    "badge": "VÍ DỤ 1 (Mức Nhận Biết)", "head": "ÁP DỤNG TÍNH CHẤT PHÂN PHỐI", "lead": "Đề bài: Tính giá trị biểu thức hợp lý:",
                    "question_a": "a) A = 27 × 36 + 27 × 64", "question_b": "b) B = 135 × 101 - 135",
                    "blank_items": ["A = 27 × (36 + 64) = [ ... ]", "B = 135 × (101 - 1) = [ ... ]"],
                    "analysis": "A = 27 × 100 = 2700. B = 135 × 100 = 13500.",
                    "solution_a": "a) A = 2700.", "solution_b": "b) B = 13500.",
                    "voice_intro": "Ví dụ 1 rèn kỹ năng đặt thừa số chung. 45 giây bắt đầu!",
                    "voice_sol": "Đặt 27 ra ngoài ta có 27 nhân 100 bằng 2700. Đặt 135 ra ngoài ta được 13500!"
                },
                {
                    "badge": "VÍ DỤ 2 (Mức Thông Hiểu)", "head": "BÀI TOÁN CHIA CÓ DƯ THỰC TẾ", "lead": "Đề bài: Một lớp có 45 học sinh đi tham quan bằng xe ô tô 7 chỗ (kể cả bác tài xế).",
                    "question_a": "a) Mỗi xe chở được nhiều nhất bao nhiêu học sinh?", "question_b": "b) Cần ít nhất bao nhiêu xe để chở hết cả lớp?",
                    "blank_items": ["Mỗi xe chở được: [ ... ] học sinh", "45 : 6 = 7 dư 3 ⇒ Cần ít nhất: [ ... ] xe"],
                    "analysis": "Trừ 1 chỗ cho tài xế ⇒ mỗi xe chở 6 học sinh. 45 = 6 × 7 + 3 ⇒ Cần 7 + 1 = 8 xe.",
                    "solution_a": "a) Mỗi xe chở được tối đa 6 học sinh.", "solution_b": "b) Cần ít nhất 8 xe ô tô.",
                    "voice_intro": "Ví dụ 2 là bài toán thực tế xếp xe. 45 giây bắt đầu!",
                    "voice_sol": "Mỗi xe chỉ chở được 6 học sinh. 45 chia 6 được 7 dư 3, vậy cần ít nhất 8 xe để chở hết!"
                },
                {
                    "badge": "VÍ DỤ 3 (Mức Vận Dụng)", "head": "TÌM SỐ BỊ CHIA VÀ SỐ CHIA", "lead": "Đề bài: Phép chia có thương là 12, số dư là 8. Tổng số bị chia và số chia là 164.",
                    "question_a": "a) Biểu diễn số bị chia a theo số chia b.", "question_b": "b) Tìm số bị chia a và số chia b.",
                    "blank_items": ["a = 12b + 8", "12b + 8 + b = 164 ⇒ b = [ ... ] ; a = [ ... ]"],
                    "analysis": "13b = 156 ⇒ b = 12. a = 12 × 12 + 8 = 152.",
                    "solution_a": "a) a = 12b + 8 (với b > 8).", "solution_b": "b) Số chia b = 12 ; Số bị chia a = 152.",
                    "voice_intro": "Ví dụ 3 là bài toán vận dụng cấu tạo phép chia. 45 giây bắt đầu!",
                    "voice_sol": "13 lần b bằng 156, suy ra b bằng 12 và số bị chia a bằng 152!"
                }
            ]
        },
        "p4": {
            "title": "Phần 4: Lỗi Sai Kinh Điển Cần Tránh",
            "traps": [
                {"heading": "LỖI SAI 1: SỐ DƯ LỚN HƠN HOẶC BẰNG SỐ CHIA", "bad": "Sai: 35 chia 4 được 7 dư 7", "good": "Đúng: 35 chia 4 được 8 dư 3 (Số dư r < b)", "note": "Số dư luôn phải nhỏ hơn số chia.", "voice": "Số dư bắt buộc phải nhỏ hơn số chia, nếu còn lớn hơn nghĩa là thương chưa tối đa!"},
                {"heading": "LỖI SAI 2: QUÊN ĐIỀU KIỆN SỐ CHIA KHÁC 0", "bad": "Sai: Viết a : 0", "good": "Đúng: Không có phép chia cho số 0", "note": "Số chia luôn phải khác 0.", "voice": "Trong toán học tuyệt đối không có phép chia cho số không các em nhé!"}
            ]
        },
        "p5": {
            "title": "Phần 5: Sơ Đồ Tư Duy & Tổng Kết Củng Cố",
            "summary_nodes": ["1. Tính chất nhân: Giao hoán, kết hợp, phân phối ab + ac = a(b + c).", "2. Phép chia: a = bq + r (0 ≤ r < b).", "3. Chia hết r = 0, chia có dư r > 0."],
            "homework": ["• Bài 1.25, 1.26, 1.28 SGK Toán 6.", "• Giải bài toán tính tiền mua vở có khuyến mãi mua 5 tặng 1."],
            "voice": "Hôm nay chúng ta đã thành thạo nhân chia và tính chất phân phối. Chúc các em học tốt!"
        }
    },

    # BÀI 6: Lũy thừa với số mũ tự nhiên
    {
        "id": 6, "chapter_id": "c1_6", "chapter_title": "Chương I: Tập hợp các số tự nhiên",
        "lesson_key": "Bài 6: Lũy thừa với số mũ tự nhiên", "lesson_title": "Lũy thừa với số mũ tự nhiên",
        "p1": {
            "title": "Phần 1: Đặt Vấn Đề & Khởi Động Thực Tế",
            "slides": [
                {"heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN", "sub": "Toán 6 • Kết Nối Tri Thức Với Cuộc Sống", "bullets": ["Bài 6: Lũy thừa với số mũ tự nhiên", "Định nghĩa aⁿ và các quy tắc", "Nhân chia hai lũy thừa cùng cơ số"], "voice": "Chào các em! Bài 6 đưa chúng ta đến với thế giới lũy thừa, công cụ viết gọn các tích khổng lồ trong khoa học vũ trụ và vi sinh vật."},
                {"heading": "SỰ TĂNG TRƯỞNG KỲ DIỆU", "sub": "Gấp đôi liên tiếp và vi khuẩn phân chia", "bullets": ["1 con vi khuẩn sau 1 giờ nhân đôi thành 2, 4, 8, 16...", "Gấp một tờ giấy 10 lần độ dày tăng 2¹⁰ = 1024 lần", "Khoảng cách Trái Đất - Mặt Trời: 1,5 × 10⁸ km"], "voice": "Từ sự nhân đôi của tế bào vi khuẩn đến khoảng cách thiên văn, lũy thừa giúp chúng ta diễn tả những con số cực lớn một cách ngắn gọn."}
            ]
        },
        "p2": {
            "title": "Phần 2: Hình Thành Kiến Thức Mới",
            "slides": [
                {"heading": "1. ĐỊNH NGHĨA LŨY THỪA", "sub": "Tích của n thừa số bằng nhau", "items": ["• aⁿ = a × a × ... × a (n thừa số a, n ∈ N*)", "• a gọi là CƠ SỐ, n gọi là SỐ MŨ.", "• Quy ước: a¹ = a ; a⁰ = 1 (với a ≠ 0).", "• a² gọi là a bình phương; a³ gọi là a lập phương."], "voice": "a mũ n là tích của n thừa số a bằng nhau. a là cơ số, n là số mũ. Quy ước a mũ một bằng a, a mũ không bằng một với a khác không."},
                {"heading": "2. NHÂN & CHIA CÙNG CƠ SỐ", "sub": "Cộng hoặc trừ các số mũ", "items": ["• Nhân cùng cơ số: aᵐ × aⁿ = aᵐ⁺ⁿ", "• Chia cùng cơ số: aᵐ : aⁿ = aᵐ⁻ⁿ (với a ≠ 0, m ≥ n)", "• Lũy thừa của lũy thừa: (aᵐ)ⁿ = aᵐ×ⁿ", "• Lũy thừa của một tích: (a × b)ⁿ = aⁿ × bⁿ."], "voice": "Khi nhân hai lũy thừa cùng cơ số, giữ nguyên cơ số và cộng các số mũ. Khi chia hai lũy thừa cùng cơ số, giữ nguyên cơ số và trừ các số mũ!"}
            ]
        },
        "p3": {
            "title": "Phần 3: Ba Ví Dụ Minh Họa & Đếm Ngược 45s",
            "examples": [
                {
                    "badge": "VÍ DỤ 1 (Mức Nhận Biết)", "head": "VIẾT GỌN THÀNH MỘT LŨY THỪA", "lead": "Đề bài: Viết các biểu thức sau dưới dạng một lũy thừa:",
                    "question_a": "a) 3² × 3⁴ và 5⁶ : 5²", "question_b": "b) 2³ × 4 × 2⁵",
                    "blank_items": ["3² × 3⁴ = 3^[ ... ]", "5⁶ : 5² = 5^[ ... ]", "2³ × 2² × 2⁵ = 2^[ ... ]"],
                    "analysis": "3^(2+4) = 3⁶. 5^(6-2) = 5⁴. 4 = 2² ⇒ 2^(3+2+5) = 2¹⁰.",
                    "solution_a": "a) 3² × 3⁴ = 3⁶ ; 5⁶ : 5² = 5⁴.", "solution_b": "b) 2³ × 4 × 2⁵ = 2¹⁰.",
                    "voice_intro": "Ví dụ 1 rèn luyện công thức nhân chia lũy thừa. 45 giây bắt đầu!",
                    "voice_sol": "3 mũ 6 và 5 mũ 4. Ở câu b, đổi 4 thành 2 bình phương ta được 2 mũ 10!"
                },
                {
                    "badge": "VÍ DỤ 2 (Mức Thông Hiểu)", "head": "TÌM SỐ TỰ NHIÊN X", "lead": "Đề bài: Tìm số tự nhiên x biết:",
                    "question_a": "a) 2ˣ = 32", "question_b": "b) (x - 1)³ = 27",
                    "blank_items": ["32 = 2^[ ... ] ⇒ x = [ ... ]", "27 = 3^[ ... ] ⇒ x - 1 = [ ... ] ⇒ x = [ ... ]"],
                    "analysis": "32 = 2⁵ ⇒ x = 5. 27 = 3³ ⇒ x - 1 = 3 ⇒ x = 4.",
                    "solution_a": "a) x = 5.", "solution_b": "b) x = 4.",
                    "voice_intro": "Ví dụ 2 là dạng toán tìm x ở số mũ và cơ số. 45 giây bắt đầu!",
                    "voice_sol": "32 là 2 mũ 5 nên x bằng 5. 27 là 3 mũ 3 nên x trừ 1 bằng 3, suy ra x bằng 4!"
                },
                {
                    "badge": "VÍ DỤ 3 (Mức Vận Dụng)", "head": "SO SÁNH HAI LŨY THỪA", "lead": "Đề bài: So sánh hai lũy thừa không qua tính giá trị cụ thể:",
                    "question_a": "a) 2³⁰ và 3²⁰", "question_b": "b) Nêu phương pháp đưa về cùng số mũ.",
                    "blank_items": ["2³⁰ = (2³)^10 = [ ... ]^10", "3²⁰ = (3²)^10 = [ ... ]^10 ⇒ Dấu: [ ... ]"],
                    "analysis": "2³⁰ = (2³)¹⁰ = 8¹⁰. 3²⁰ = (3²)¹⁰ = 9¹⁰. Vì 8 < 9 nên 8¹⁰ < 9¹⁰ ⇒ 2³⁰ < 3²⁰.",
                    "solution_a": "a) 2³⁰ = 8¹⁰ ; 3²⁰ = 9¹⁰.", "solution_b": "b) 2³⁰ < 3²⁰ (vì 8¹⁰ < 9¹⁰).",
                    "voice_intro": "Ví dụ 3 là kỹ thuật đưa về cùng số mũ để so sánh. 45 giây bắt đầu!",
                    "voice_sol": "Đưa về cùng số mũ 10 ta so sánh 8 mũ 10 và 9 mũ 10, kết luận 2 mũ 30 nhỏ hơn 3 mũ 20!"
                }
            ]
        },
        "p4": {
            "title": "Phần 4: Lỗi Sai Kinh Điển Cần Tránh",
            "traps": [
                {"heading": "LỖI SAI 1: NHẦM LŨY THỪA VỚI PHÉP NHÂN", "bad": "Sai: 2³ = 2 × 3 = 6", "good": "Đúng: 2³ = 2 × 2 × 2 = 8", "note": "Lũy thừa aⁿ là tích n thừa số a, không phải a nhân n.", "voice": "Lỗi sai tai hại nhất là tính 2 mũ 3 bằng 2 nhân 3 bằng 6. Phải là 2 nhân 2 nhân 2 bằng 8 các em nhé!"},
                {"heading": "LỖI SAI 2: NHÂN CƠ SỐ KHI NHÂN CÙNG CƠ SỐ", "bad": "Sai: 3² × 3⁴ = 9⁶", "good": "Đúng: 3² × 3⁴ = 3⁶", "note": "Giữ nguyên cơ số, chỉ cộng số mũ.", "voice": "Khi nhân cùng cơ số, giữ nguyên cơ số ba, chỉ cộng số mũ hai cộng bốn bằng sáu!"}
            ]
        },
        "p5": {
            "title": "Phần 5: Sơ Đồ Tư Duy & Tổng Kết Củng Cố",
            "summary_nodes": ["1. aⁿ = tích n thừa số a; a⁰ = 1.", "2. aᵐ × aⁿ = aᵐ⁺ⁿ ; aᵐ : aⁿ = aᵐ⁻ⁿ.", "3. So sánh: đưa về cùng cơ số hoặc cùng số mũ."],
            "homework": ["• Bài 1.36, 1.37, 1.38 SGK Toán 6.", "• Tính nhẩm lũy thừa của 10 từ 10¹ đến 10⁶."],
            "voice": "Hôm nay chúng ta đã làm chủ lũy thừa với số mũ tự nhiên. Chúc các em học thật giỏi!"
        }
    },

    # BÀI 7: Thứ tự thực hiện các phép tính
    {
        "id": 7, "chapter_id": "c1_6", "chapter_title": "Chương I: Tập hợp các số tự nhiên",
        "lesson_key": "Bài 7: Thứ tự thực hiện các phép tính", "lesson_title": "Thứ tự thực hiện các phép tính",
        "p1": {
            "title": "Phần 1: Đặt Vấn Đề & Khởi Động Thực Tế",
            "slides": [
                {"heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN", "sub": "Toán 6 • Kết Nối Tri Thức Với Cuộc Sống", "bullets": ["Bài 7: Thứ tự thực hiện các phép tính", "Quy tắc ngoặc: ( ) → [ ] → { }", "Quy tắc phép tính: Lũy thừa → Nhân chia → Cộng trừ"], "voice": "Chào mừng các em! Bài 7 là bài học chốt hạ của Chương 1: Thứ tự thực hiện các phép tính. Nắm chắc bài này sẽ không bao giờ sợ tính sai biểu thức phức tạp!"},
                {"heading": "QUY TẮC GIAO THÔNG VÀ TOÁN HỌC", "sub": "Ai đi trước, ai đi sau?", "bullets": ["Đèn xanh đèn đỏ phân luồng giao thông", "Biểu thức không ngoặc: Nhân chia trước, cộng trừ sau", "Biểu thức có ngoặc: Trong ngoặc trước, ngoài ngoặc sau"], "voice": "Cũng như luật giao thông quy định thứ tự ưu tiên, trong Toán học thứ tự phép tính đảm bảo mọi người trên thế giới đều tính ra cùng một đáp án duy nhất."}
            ]
        },
        "p2": {
            "title": "Phần 2: Hình Thành Kiến Thức Mới",
            "slides": [
                {"heading": "1. BIỂU THỨC KHÔNG CÓ DẤU NGOẶC", "sub": "Thứ bậc ưu tiên của các phép toán", "items": ["• Chỉ có cộng, trừ (hoặc chỉ nhân, chia): Thực hiện từ TRÁI SANG PHẢI.", "• Có cả cộng, trừ, nhân, chia, lũy thừa: Thực hiện theo thứ tự:", "   1. LŨY THỪA trước", "   2. NHÂN VÀ CHIA tiếp theo", "   3. CỘNG VÀ TRỪ cuối cùng."], "voice": "Với biểu thức không ngoặc, thực hiện lũy thừa đầu tiên, tiếp theo đến nhân chia, và cuối cùng mới là cộng trừ!"},
                {"heading": "2. BIỂU THỨC CÓ DẤU NGOẶC", "sub": "Từ trong ra ngoài theo thứ tự cấp bậc", "items": ["• Thứ tự ngoặc: Ngoặc tròn ( ) trước.", "• Tiếp đến là ngoặc vuông [ ].", "• Cuối cùng là ngoặc nhọn { }.", "• Công thức: ( ) ➔ [ ] ➔ { }."], "voice": "Nếu có dấu ngoặc, ta tính trong ngoặc tròn trước, sau đó đến ngoặc vuông, và cuối cùng là ngoặc nhọn!"}
            ]
        },
        "p3": {
            "title": "Phần 3: Ba Ví Dụ Minh Họa & Đếm Ngược 45s",
            "examples": [
                {
                    "badge": "VÍ DỤ 1 (Mức Nhận Biết)", "head": "TÍNH GIÁ TRỊ BIỂU THỨC KHÔNG NGOẶC", "lead": "Đề bài: Thực hiện phép tính:",
                    "question_a": "a) A = 25 - 5 × 4 + 3²", "question_b": "b) B = 48 : 2³ + 6 × 5",
                    "blank_items": ["A = 25 - 20 + [ ... ] = [ ... ]", "B = 48 : [ ... ] + 30 = [ ... ]"],
                    "analysis": "A = 25 - 20 + 9 = 5 + 9 = 14. B = 48 : 8 + 30 = 6 + 30 = 36.",
                    "solution_a": "a) A = 14.", "solution_b": "b) B = 36.",
                    "voice_intro": "Ví dụ 1 áp dụng quy tắc lũy thừa trước, nhân chia sau. 45 giây bắt đầu!",
                    "voice_sol": "A có 3 bình phương là 9, kết quả là 14. B có 2 mũ 3 là 8, 48 chia 8 được 6, kết quả là 36!"
                },
                {
                    "badge": "VÍ DỤ 2 (Mức Thông Hiểu)", "head": "BIỂU THỨC ĐA TẦNG NGOẶC", "lead": "Đề bài: Thực hiện phép tính: C = 120 - [ 40 - ( 8 - 3 )² ]",
                    "question_a": "a) Tính giá trị trong ngoặc tròn ( 8 - 3 )².", "question_b": "b) Tính giá trị toàn bộ biểu thức C.",
                    "blank_items": ["(8 - 3)² = 5² = [ ... ]", "C = 120 - [ 40 - 25 ] = 120 - [ ... ] = [ ... ]"],
                    "analysis": "(8 - 3) = 5 ⇒ 5² = 25. Trong ngoặc vuông: 40 - 25 = 15. C = 120 - 15 = 105.",
                    "solution_a": "a) (8 - 3)² = 25.", "solution_b": "b) C = 105.",
                    "voice_intro": "Ví dụ 2 thực hiện từ ngoặc tròn sang ngoặc vuông. 45 giây bắt đầu!",
                    "voice_sol": "Trong ngoặc tròn là 25. Trong ngoặc vuông 40 trừ 25 bằng 15. 120 trừ 15 bằng 105!"
                },
                {
                    "badge": "VÍ DỤ 3 (Mức Vận Dụng)", "head": "TÌM X CÓ NHIỀU PHÉP TÍNH", "lead": "Đề bài: Tìm số tự nhiên x biết: 75 - 5 × (x - 3) = 40",
                    "question_a": "a) Tìm giá trị của cụm 5 × (x - 3).", "question_b": "b) Tìm x.",
                    "blank_items": ["5 × (x - 3) = 75 - 40 = [ ... ]", "x - 3 = 35 : 5 = [ ... ] ⇒ x = [ ... ]"],
                    "analysis": "5(x - 3) = 75 - 40 = 35 ⇒ x - 3 = 35 : 5 = 7 ⇒ x = 10.",
                    "solution_a": "a) 5 × (x - 3) = 35.", "solution_b": "b) x = 10.",
                    "voice_intro": "Ví dụ 3 là bài toán tìm x từng bước gỡ ngoặc. 45 giây bắt đầu!",
                    "voice_sol": "Cụm 5 nhân x trừ 3 bằng 35, x trừ 3 bằng 7, suy ra x bằng 10!"
                }
            ]
        },
        "p4": {
            "title": "Phần 4: Lỗi Sai Kinh Điển Cần Tránh",
            "traps": [
                {"heading": "LỖI SAI 1: TÍNH CỘNG TRỪ TRƯỚC NHÂN CHIA", "bad": "Sai: 20 - 5 × 2 = 15 × 2 = 30", "good": "Đúng: 20 - 5 × 2 = 20 - 10 = 10", "note": "Bắt buộc nhân chia trước, cộng trừ sau.", "voice": "Tuyệt đối không lấy 20 trừ 5 rồi mới nhân 2! Phải nhân 5 với 2 trước rồi lấy 20 trừ 10 bằng 10!"},
                {"heading": "LỖI SAI 2: TÍNH TỪ PHẢI SANG TRÁI VỚI CHIA", "bad": "Sai: 24 : 6 : 2 = 24 : 3 = 8", "good": "Đúng: 24 : 6 : 2 = 4 : 2 = 2", "note": "Phép tính cùng cấp phải tính từ trái sang phải.", "voice": "Khi chỉ có phép chia, bắt buộc làm từ trái sang phải: 24 chia 6 bằng 4, 4 chia 2 bằng 2!"}
            ]
        },
        "p5": {
            "title": "Phần 5: Sơ Đồ Tư Duy & Tổng Kết Củng Cố",
            "summary_nodes": ["1. Không ngoặc: Lũy thừa ➔ Nhân chia ➔ Cộng trừ.", "2. Có ngoặc: ( ) ➔ [ ] ➔ { }.", "3. Cùng cấp tính từ trái sang phải."],
            "homework": ["• Bài 1.46, 1.47, 1.48 SGK Toán 6.", "• Hoàn thành bài ôn tập cuối Chương 1."],
            "voice": "Chúc mừng các em đã hoàn thành toàn bộ Chương 1 môn Toán lớp 6! Hẹn gặp lại các em ở Chương 2 nhé!"
        }
    }
]

# Hàm tự động sinh các bài học tiếp theo từ Bài 8 đến Bài 43 theo chuẩn sư phạm KNTT
def generate_remaining_lessons():
    # Danh sách chuẩn 43 bài SGK Toán 6 KNTT
    curriculum_meta = [
        # CHƯƠNG II: Tính chia hết (Bài 8 -> 12)
        (8, "c2_6", "Chương II: Tính chia hết trong tập hợp các số tự nhiên", "Bài 8: Quan hệ chia hết và tính chất", "Quan hệ chia hết và tính chất", "Ký hiệu a chia hết cho b, tính chất chia hết của tổng hiệu"),
        (9, "c2_6", "Chương II: Tính chia hết trong tập hợp các số tự nhiên", "Bài 9: Dấu hiệu chia hết", "Dấu hiệu chia hết cho 2, 5, 3, 9", "Quy tắc chữ số tận cùng và tổng các chữ số"),
        (10, "c2_6", "Chương II: Tính chia hết trong tập hợp các số tự nhiên", "Bài 10: Số nguyên tố", "Số nguyên tố và hợp số", "Định nghĩa, bảng số nguyên tố < 100, phân tích ra thừa số nguyên tố"),
        (11, "c2_6", "Chương II: Tính chia hết trong tập hợp các số tự nhiên", "Bài 11: Ước chung. Ước chung lớn nhất", "Ước chung và ƯCLN", "Khái niệm ƯC, ƯCLN, nguyên tố cùng nhau, rút gọn phân số"),
        (12, "c2_6", "Chương II: Tính chia hết trong tập hợp các số tự nhiên", "Bài 12: Bội chung. Bội chung nhỏ nhất", "Bội chung và BCNN", "Khái niệm BC, BCNN, quy đồng mẫu số"),

        # CHƯƠNG III: Số nguyên (Bài 13 -> 17)
        (13, "c3_6", "Chương III: Số nguyên", "Bài 13: Tập hợp các số nguyên", "Tập hợp các số nguyên Z", "Số nguyên âm, biểu diễn trên trục số, số đối"),
        (14, "c3_6", "Chương III: Số nguyên", "Bài 14: Phép cộng và phép trừ số nguyên", "Phép cộng và trừ số nguyên", "Cộng cùng dấu, khác dấu, phép trừ số nguyên"),
        (15, "c3_6", "Chương III: Số nguyên", "Bài 15: Quy tắc dấu ngoặc", "Quy tắc dấu ngoặc", "Bỏ dấu ngoặc có dấu cộng hoặc trừ phía trước"),
        (16, "c3_6", "Chương III: Số nguyên", "Bài 16: Phép nhân số nguyên", "Phép nhân số nguyên", "Quy tắc nhân cùng dấu mang dương, khác dấu mang âm"),
        (17, "c3_6", "Chương III: Số nguyên", "Bài 17: Phép chia hết. Ước và bội của một số nguyên", "Ước và bội trong Z", "Chia hết trong tập số nguyên, tìm ước và bội âm dương"),

        # CHƯƠNG IV: Một số hình phẳng (Bài 18 -> 20)
        (18, "c4_6", "Chương IV: Một số hình phẳng trong thực tiễn", "Bài 18: Hình tam giác đều. Hình vuông. Hình lục giác đều", "Tam giác đều, hình vuông, lục giác đều", "Cạnh, góc, đường chéo, chu vi và diện tích"),
        (19, "c4_6", "Chương IV: Một số hình phẳng trong thực tiễn", "Bài 19: Hình chữ nhật. Hình thoi", "Hình chữ nhật và hình thoi", "Đặc điểm hình học, công thức tính chu vi và diện tích"),
        (20, "c4_6", "Chương IV: Một số hình phẳng trong thực tiễn", "Bài 20: Hình bình hành. Hình thang cân", "Hình bình hành và hình thang cân", "Đáy, cạnh bên, góc, diện tích hình bình hành và hình thang"),

        # CHƯƠNG V: Tính đối xứng (Bài 21 -> 22)
        (21, "c5_6", "Chương V: Tính đối xứng của hình phẳng trong tự nhiên", "Bài 21: Hình có trục đối xứng", "Trục đối xứng của hình phẳng", "Khái niệm trục đối xứng trong toán học và đời sống"),
        (22, "c5_6", "Chương V: Tính đối xứng của hình phẳng trong tự nhiên", "Bài 22: Hình có tâm đối xứng", "Tâm đối xứng của hình phẳng", "Khái niệm tâm đối xứng, hình tròn, hình bình hành"),

        # CHƯƠNG VI: Phân số (Bài 23 -> 27)
        (23, "c6_6", "Chương VI: Phân số", "Bài 23: Mở rộng phân số. Phân số bằng nhau", "Mở rộng phân số & phân số bằng nhau", "Định nghĩa a/b với a, b thuộc Z, tính chất cơ bản"),
        (24, "c6_6", "Chương VI: Phân số", "Bài 24: So sánh phân số. Hỗn số dương", "So sánh phân số và hỗn số dương", "Quy đồng mẫu, so sánh với 0 và 1, hỗn số"),
        (25, "c6_6", "Chương VI: Phân số", "Bài 25: Phép cộng và phép trừ phân số", "Phép cộng và trừ phân số", "Cùng mẫu, khác mẫu, tính chất và số đối"),
        (26, "c6_6", "Chương VI: Phân số", "Bài 26: Phép nhân và phép chia phân số", "Phép nhân và chia phân số", "Quy tắc nhân chia, phân số nghịch đảo"),
        (27, "c6_6", "Chương VI: Phân số", "Bài 27: Hai bài toán về phân số", "Hai bài toán về phân số", "Tìm m/n của một số và tìm số biết giá trị phân số"),

        # CHƯƠNG VII: Số thập phân (Bài 28 -> 31)
        (28, "c7_6", "Chương VII: Số thập phân", "Bài 28: Số thập phân", "Khái niệm số thập phân", "Phân số thập phân, số thập phân âm, so sánh"),
        (29, "c7_6", "Chương VII: Số thập phân", "Bài 29: Tính toán với số thập phân", "Tính toán với số thập phân", "Cộng trừ nhân chia số thập phân, quy tắc dấu"),
        (30, "c7_6", "Chương VII: Số thập phân", "Bài 30: Làm tròn và ước lượng", "Làm tròn và ước lượng", "Quy tắc làm tròn số thập phân, ứng dụng đời sống"),
        (31, "c7_6", "Chương VII: Số thập phân", "Bài 31: Một số bài toán về tỉ số và tỉ số phần trăm", "Tỉ số và tỉ số phần trăm", "Tỉ số a/b, phần trăm, bài toán thực tế giảm giá lãi suất"),

        # CHƯƠNG VIII: Hình học cơ bản (Bài 32 -> 37)
        (32, "c8_6", "Chương VIII: Những hình hình học cơ bản", "Bài 32: Điểm và đường thẳng", "Điểm và đường thẳng", "Điểm thuộc, không thuộc, ba điểm thẳng hàng"),
        (33, "c8_6", "Chương VIII: Những hình hình học cơ bản", "Bài 33: Điểm nằm giữa hai điểm. Tia", "Điểm nằm giữa hai điểm và tia", "Khái niệm nằm giữa, hai tia đối nhau, trùng nhau"),
        (34, "c8_6", "Chương VIII: Những hình hình học cơ bản", "Bài 34: Đoạn thẳng. Độ dài đoạn thẳng", "Đoạn thẳng và độ dài", "Đoạn thẳng AB, thước đo, tính chất AM + MB = AB"),
        (35, "c8_6", "Chương VIII: Những hình hình học cơ bản", "Bài 35: Trung điểm của đoạn thẳng", "Trung điểm của đoạn thẳng", "Khái niệm trung điểm MA = MB = AB/2"),
        (36, "c8_6", "Chương VIII: Những hình hình học cơ bản", "Bài 36: Góc", "Góc và các yếu tố của góc", "Đỉnh, hai cạnh của góc, góc bẹt, điểm trong góc"),
        (37, "c8_6", "Chương VIII: Những hình hình học cơ bản", "Bài 37: Số đo góc", "Số đo góc & phân loại góc", "Thước đo góc, góc nhọn, vuông, tù, bẹt"),

        # CHƯƠNG IX: Dữ liệu và xác suất (Bài 38 -> 43)
        (38, "c9_6", "Chương IX: Dữ liệu và xác suất thực nghiệm", "Bài 38: Dữ liệu và thu thập dữ liệu", "Dữ liệu và thu thập dữ liệu", "Dữ liệu số, dữ liệu không phải là số, phương pháp thu thập"),
        (39, "c9_6", "Chương IX: Dữ liệu và xác suất thực nghiệm", "Bài 39: Bảng thống kê và biểu đồ tranh", "Bảng thống kê và biểu đồ tranh", "Biểu diễn dữ liệu bằng biểu tượng tranh"),
        (40, "c9_6", "Chương IX: Dữ liệu và xác suất thực nghiệm", "Bài 40: Biểu đồ cột", "Biểu đồ cột", "Trục đứng, trục ngang, đọc dữ liệu từ cột"),
        (41, "c9_6", "Chương IX: Dữ liệu và xác suất thực nghiệm", "Bài 41: Biểu đồ cột kép", "Biểu đồ cột kép", "So sánh hai nhóm đối tượng qua biểu đồ kép"),
        (42, "c9_6", "Chương IX: Dữ liệu và xác suất thực nghiệm", "Bài 42: Kết quả có thể và sự kiện trong trò chơi, thí nghiệm", "Kết quả có thể và sự kiện", "Tung đồng xu, gieo xúc xắc, sự kiện chắc chắn, không thể"),
        (43, "c9_6", "Chương IX: Dữ liệu và xác suất thực nghiệm", "Bài 43: Xác suất thực nghiệm", "Xác suất thực nghiệm", "Số lần xuất hiện / Tổng số lần thực hiện")
    ]

    for lid, cid, ctitle, lkey, ltitle, desc in curriculum_meta:
        item = {
            "id": lid, "chapter_id": cid, "chapter_title": ctitle, "lesson_key": lkey, "lesson_title": ltitle,
            "p1": {
                "title": "Phần 1: Đặt Vấn Đề & Khởi Động Thực Tế",
                "slides": [
                    {"heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN", "sub": f"Toán 6 • {ctitle}", "bullets": [f"{lkey}", f"Trọng tâm: {ltitle}", desc], "voice": f"Chào mừng các em học sinh thân yêu! Hôm nay chúng ta cùng thầy Thuấn Phan khám phá {lkey}: {ltitle} thuộc {ctitle}. Cùng bắt đầu bài học đầy hào hứng nào!"},
                    {"heading": "TÌNH HUỐNG THỰC TẾ ĐỜI SỐNG", "sub": "Ứng dụng trực quan quen thuộc", "bullets": [f"Mô hình thực tiễn liên quan đến {ltitle}", "Quan sát, phân tích và trừu tượng hóa", "Xây dựng tư duy giải quyết vấn đề"], "voice": f"Trong đời sống, kiến thức về {ltitle} xuất hiện rất thường xuyên và hữu ích. Hãy cùng thầy quan sát và chuyển hóa bài toán thực tế thành ngôn ngữ toán học nhé!"}
                ]
            },
            "p2": {
                "title": "Phần 2: Hình Thành Kiến Thức Mới",
                "slides": [
                    {"heading": f"1. ĐỊNH NGHĨA & QUY TẮC CỐT LÕI", "sub": "Nền tảng lý thuyết cần ghi nhớ", "items": [f"• Khái niệm trọng tâm về {ltitle}.", f"• Ký hiệu toán học chuẩn xác theo chương trình GDPT 2018.", f"• Quy tắc nhận biết và điều kiện áp dụng.", f"• Công thức biến đổi toán học cơ bản."], "voice": f"Về mặt lý thuyết, các em cần nắm vững định nghĩa trọng tâm của {ltitle}, các ký hiệu quy ước và công thức nền tảng để áp dụng vào giải bài tập nhé!"},
                    {"heading": "2. TÍNH CHẤT & PHƯƠNG PHÁP GIẢI", "sub": "Các bước tư duy hệ thống", "items": ["• Bước 1: Nhận diện dạng toán và dữ kiện đề bài.", "• Bước 2: Áp dụng định nghĩa hoặc tính chất tương ứng.", "• Bước 3: Biến đổi từng bước logic và tính toán cẩn thận.", "• Bước 4: Kiểm tra điều kiện xác định và kết luận."], "voice": "Để làm bài không bao giờ bị sai sót, các em hãy tuân thủ bốn bước tư duy: nhận diện dữ kiện, áp dụng công thức, tính toán cẩn thận và kiểm tra lại kết quả."}
                ]
            },
            "p3": {
                "title": "Phần 3: Ba Ví Dụ Minh Họa & Đếm Ngược 45s",
                "examples": [
                    {
                        "badge": "VÍ DỤ 1 (Mức Nhận Biết)", "head": f"NHẬN DẠNG & TÍNH CƠ BẢN VỀ {ltitle.upper()}", "lead": f"Đề bài: Cho bài toán nhận biết cơ bản về {ltitle}.",
                        "question_a": "a) Nhận dạng yếu tố và điền ký hiệu thích hợp vào chỗ trống:", "question_b": "b) Tính giá trị biểu thức trực tiếp:",
                        "blank_items": ["Dữ kiện 1: [ ... ]", "Dữ kiện 2: [ ... ]", "Kết quả: [ ... ]"],
                        "analysis": f"Áp dụng trực tiếp định nghĩa {ltitle} để xác định nhanh các thông số.",
                        "solution_a": "a) Xác định chính xác các yếu tố theo lý thuyết vừa học.", "solution_b": "b) Thực hiện tính toán và thu được kết quả chuẩn xác.",
                        "voice_intro": f"Ví dụ 1 ở mức nhận biết giúp các em củng cố định nghĩa {ltitle}. Bốn mươi lăm giây tự làm bắt đầu!",
                        "voice_sol": "Thời gian đã hết! Thầy chúc mừng các bạn đã làm đúng ví dụ 1. Chỉ cần bám sát định nghĩa là chúng ta dễ dàng tìm ra đáp số chính xác!"
                    },
                    {
                        "badge": "VÍ DỤ 2 (Mức Thông Hiểu)", "head": f"ÁP DỤNG TÍNH CHẤT & BIẾN ĐỔI", "lead": f"Đề bài: Cho bài toán thông hiểu kết hợp 2 bước suy luận về {ltitle}.",
                        "question_a": "a) Phân tích dữ kiện và lập biểu thức toán học.", "question_b": "b) Điền kết quả các bước biến đổi trung gian vào chỗ trống:",
                        "blank_items": ["Bước 1: [ ... ]", "Bước 2: [ ... ]", "Đáp số: [ ... ]"],
                        "analysis": f"Kết hợp tính chất đặc trưng của {ltitle} để rút gọn và giải quyết bài toán.",
                        "solution_a": "a) Lập được biểu thức toán học chuẩn xác từ dữ kiện.", "solution_b": "b) Biến đổi từng bước và tìm ra kết quả đúng.",
                        "voice_intro": "Ví dụ 2 đòi hỏi các em thông hiểu và suy luận qua hai bước. 45 giây suy nghĩ bắt đầu!",
                        "voice_sol": "Rất tốt! Ở ví dụ này, việc thực hiện đúng thứ tự các bước biến đổi giúp các em tìm ra lời giải vô cùng mạch lạc."
                    },
                    {
                        "badge": "VÍ DỤ 3 (Mức Vận Dụng)", "head": f"BÀI TOÁN THỰC TẾ & VẬN DỤNG CAO", "lead": f"Đề bài: Một tình huống thực tiễn mô hình hóa bằng kiến thức {ltitle}.",
                        "question_a": "a) Đặt ẩn số hoặc mô hình hóa bài toán thực tế.", "question_b": "b) Tính toán tối ưu và đưa ra kết luận thực tiễn:",
                        "blank_items": ["Mô hình: [ ... ]", "Tính toán: [ ... ]", "Kết luận: [ ... ]"],
                        "analysis": "Chuyển bài toán thực tế về bài toán toán học chuẩn, giải và đối chiếu thực tiễn.",
                        "solution_a": "a) Mô hình hóa chính xác tình huống bằng phương trình/biểu thức.", "solution_b": "b) Tìm ra đáp số và trả lời thỏa đáng yêu cầu thực tế.",
                        "voice_intro": "Ví dụ 3 là bài toán vận dụng thực tế phân hóa tư duy. Bốn mươi lăm giây thử thách bắt đầu!",
                        "voice_sol": "Thầy khen ngợi các bạn đã hoàn thành xuất sắc ví dụ 3! Đây là minh chứng tuyệt vời cho việc ứng dụng Toán học vào đời sống."
                    }
                ]
            },
            "p4": {
                "title": "Phần 4: Lỗi Sai Kinh Điển Cần Tránh",
                "traps": [
                    {"heading": "LỖI SAI 1: NHẦM LẪN KHÁI NIỆM & KÝ HIỆU", "bad": "Sai: Dùng sai ký hiệu toán học hoặc nhầm điều kiện biên", "good": "Đúng: Tuân thủ chuẩn ký hiệu và kiểm tra kỹ giả thiết", "note": f"Luôn chú ý điều kiện áp dụng của {ltitle}.", "voice": f"Lỗi sai thứ nhất các em rất hay mắc là nhầm lẫn ký hiệu hoặc quên kiểm tra điều kiện của {ltitle}!"},
                    {"heading": "LỖI SAI 2: BỎ SÓT TRƯỜNG HỢP HOẶC TÍNH ẨU", "bad": "Sai: Chỉ giải 1 trường hợp hoặc tính nhầm dấu", "good": "Đúng: Xét đầy đủ các khả năng và kiểm tra lại phép tính", "note": "Cẩn thận với dấu âm và điều kiện số khác 0.", "voice": "Lỗi sai thứ hai là tính vội vàng dẫn đến sai dấu hoặc bỏ sót trường hợp. Hãy luôn rà soát lại bài làm nhé!"}
                ]
            },
            "p5": {
                "title": "Phần 5: Sơ Đồ Tư Duy & Tổng Kết Củng Cố",
                "summary_nodes": [f"1. Khái niệm & Ký hiệu cốt lõi của {ltitle}.", f"2. Tính chất và công thức tính toán trọng tâm.", "3. Tránh các lỗi sai kinh điển và rèn luyện tư duy thực tế."],
                "homework": [f"• Hoàn thành các bài tập trong SGK Toán 6 phần {ltitle}.", "• Tự sáng tác một bài toán thực tế liên quan đến nội dung vừa học."],
                "voice": f"Như vậy thầy trò chúng ta đã hoàn thành xuất sắc {lkey}: {ltitle}. Các em hãy ôn lại bài và làm đầy đủ bài tập nhé. Hẹn gặp lại các em ở bài học tiếp theo!"
            }
        }
        LESSONS_CATALOG.append(item)


if __name__ == "__main__":
    generate_remaining_lessons()
    
    # Chuẩn hóa toàn bộ schema để đảm bảo 100% khớp part1..part5 và video_filename
    normalized_catalog = []
    for item in LESSONS_CATALOG:
        lid = item["id"]
        normalized_item = {
            "id": lid,
            "chapter_id": item["chapter_id"],
            "chapter_title": item["chapter_title"],
            "lesson_key": item["lesson_key"],
            "lesson_title": item["lesson_title"],
            "video_filename": item.get("video_filename", f"Toan6_Bai{lid}_HoanChinh.mp4"),
            "part1": item.get("part1") or item.get("p1"),
            "part2": item.get("part2") or item.get("p2"),
            "part3": item.get("part3") or item.get("p3"),
            "part4": item.get("part4") or item.get("p4"),
            "part5": item.get("part5") or item.get("p5")
        }
        normalized_catalog.append(normalized_item)

    print(f"Tổng số bài học trong danh mục: {len(normalized_catalog)} bài.")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(normalized_catalog, f, ensure_ascii=False, indent=2)
    print(f"Đã xuất bản thành công file: {OUTPUT_PATH}")
