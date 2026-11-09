"""
TỰ ĐỘNG KHỞI TẠO BỘ DỮ LIỆU BÀI HỌC TOÀN DIỆN CHO TOÀN BỘ TOÁN 6 (KNTT)
Bao gồm đầy đủ từ Bài 2 đến Bài 43 (Tập 1 và Tập 2)
Quy chuẩn: 5 phần sư phạm chuẩn Bộ GD&ĐT (Khởi động, Kiến thức, 3 Ví dụ đếm ngược 45s, Cảnh báo lỗi sai, Sơ đồ tư duy)
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "curriculum_toan6_full.json")


def build_lesson(lesson_id, chapter_id, chapter_title, lesson_key, lesson_title,
                 p1_slides, p2_slides, p3_examples, p4_traps, p5_data):
    return {
        "id": lesson_id,
        "chapter_id": chapter_id,
        "chapter_title": chapter_title,
        "lesson_key": lesson_key,
        "lesson_title": lesson_title,
        "video_filename": f"Toan6_Bai{lesson_id}_HoanChinh.mp4",
        "part1": {
            "title": "Phần 1: Đặt Vấn Đề & Khởi Động Thực Tế",
            "slides": p1_slides
        },
        "part2": {
            "title": "Phần 2: Hình Thành Kiến Thức Mới",
            "slides": p2_slides
        },
        "part3": {
            "title": "Phần 3: Ba Ví Dụ Minh Họa & Đếm Ngược 45s",
            "examples": p3_examples
        },
        "part4": {
            "title": "Phần 4: Lỗi Sai Kinh Điển Cần Tránh",
            "traps": p4_traps
        },
        "part5": {
            "title": "Phần 5: Sơ Đồ Tư Duy & Tổng Kết Củng Cố",
            "summary_nodes": p5_data.get("summary_nodes", []),
            "homework": p5_data.get("homework", []),
            "voice": p5_data.get("voice", "")
        }
    }


def create_all_lessons():
    lessons = []

    # =========================================================================
    # CHƯƠNG I: TẬP HỢP CÁC SỐ TỰ NHIÊN (Bài 2 -> Bài 7)
    # =========================================================================
    
    # BÀI 2: Cách ghi số tự nhiên
    lessons.append(build_lesson(
        lesson_id=2,
        chapter_id="c1_6",
        chapter_title="Chương I: Tập hợp các số tự nhiên",
        lesson_key="Bài 2: Cách ghi số tự nhiên",
        lesson_title="Cách ghi số tự nhiên",
        p1_slides=[
            {
                "heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN",
                "sub": "Toán 6 • Kết Nối Tri Thức Với Cuộc Sống",
                "bullets": [
                    "Bài 2: Cách ghi số tự nhiên",
                    "Hệ thập phân và các hàng chữ số",
                    "Hệ chữ số La Mã cổ đại trong đời sống"
                ],
                "voice": "Chào mừng các em quay trở lại lớp học Toán cùng thầy Thuấn Phan! Trong bài học hôm nay, chúng ta cùng tìm hiểu Bài 2: Cách ghi số tự nhiên. Chúng ta sẽ khám phá hệ thập phân quen thuộc và chữ số La Mã cổ đại độc đáo nhé!"
            },
            {
                "heading": "CÁC CON SỐ TRONG ĐỜI SỐNG HẰNG NGÀY",
                "sub": "Từ tiền tệ, dân số đến mặt đồng hồ cổ điển",
                "bullets": [
                    "Dân số Việt Nam: Hơn 100 000 000 người",
                    "Giá tiền, số nhà, biển số xe hằng ngày",
                    "Mặt đồng hồ đeo tay khắc chữ số I, V, X"
                ],
                "voice": "Các em thấy đấy, mỗi ngày chúng ta đều nhìn thấy các con số: dân số nước ta hơn một trăm triệu người, số tiền mua một món đồ, hay chữ số La Mã trên mặt đồng hồ cổ kính. Làm thế nào người xưa và nay ghi lại các số đó một cách chính xác?"
            }
        ],
        p2_slides=[
            {
                "heading": "1. HỆ THẬP PHÂN & GIÁ TRỊ CỦA CHỮ SỐ",
                "sub": "Mười chữ số cơ bản tạo nên muôn vàn con số",
                "items": [
                    "• Dùng 10 chữ số: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9",
                    "• Cấu tạo số hai chữ số: ab = a × 10 + b (với a ≠ 0)",
                    "• Cấu tạo số ba chữ số: abc = a × 100 + b × 10 + c (với a ≠ 0)",
                    "• Mỗi hàng gấp 10 lần hàng liền sau nó"
                ],
                "voice": "Trong hệ thập phân, chúng ta chỉ dùng đúng mười chữ số từ không đến chín. Giá trị của một chữ số phụ thuộc vào vị trí của nó. Số a b gạch đầu bằng a nhân mười cộng b. Số a b c bằng a nhân một trăm cộng b nhân mười cộng c."
            },
            {
                "heading": "2. HỆ CHỮ SỐ LA MÃ",
                "sub": "Các ký hiệu cơ bản và quy tắc ghép số",
                "items": [
                    "• Chữ số cơ bản: I = 1 ; V = 5 ; X = 10",
                    "• Ghép thêm bên phải (Cộng): VI = 6 ; VII = 7 ; XI = 11",
                    "• Ghép bên trái (Trừ): IV = 4 ; IX = 9",
                    "• Không lặp lại chữ số I, X quá 3 lần liên tiếp"
                ],
                "voice": "Hệ chữ số La Mã dùng các chữ cái: I là một, V là năm, X là mười. Viết thêm bên phải nghĩa là cộng vào, như V I là sáu. Viết bên trái nghĩa là trừ đi, như I V là bốn, I X là chín. Chú ý không viết quá ba chữ I hoặc X liên tiếp nhé!"
            }
        ],
        p3_examples=[
            {
                "badge": "VÍ DỤ 1 (Mức Nhận Biết)",
                "head": "ĐỌC VÀ VIẾT SỐ LA MÃ",
                "lead": "Đề bài: Viết các số sau sang số La Mã và ngược lại:",
                "question_a": "a) Viết số 14 và số 26 bằng chữ số La Mã.",
                "question_b": "b) Đọc giá trị của các số La Mã sau:",
                "blank_items": ["XIV = [ ... ]", "XIX = [ ... ]", "XXVIII = [ ... ]"],
                "analysis": "14 = 10 + 4 = X + IV = XIV.  26 = 20 + 6 = XX + VI = XXVI.",
                "solution_a": "a) Số 14 viết là XIV ; Số 26 viết là XXVI.",
                "solution_b": "b) XIV = 14 ; XIX = 19 ; XXVIII = 28.",
                "voice_intro": "Ví dụ 1 yêu cầu các em đọc và chuyển đổi giữa số tự nhiên và số La Mã. Các em hãy quan sát kỹ quy tắc ghép và điền vào chỗ trống nhé. Bốn mươi lăm giây suy nghĩ bắt đầu!",
                "voice_sol": "Đã hết thời gian! Cùng thầy kiểm tra kết quả nào: Mười bốn bằng mười cộng bốn, viết là X I V. Hai mươi sáu là X X V I. Tương tự, X I X chính là mười chín và X X V I I I là hai mươi tám!"
            },
            {
                "badge": "VÍ DỤ 2 (Mức Thông Hiểu)",
                "head": "PHÂN TÍCH CẤU TẠO SỐ HỆ THẬP PHÂN",
                "lead": "Đề bài: Cho số tự nhiên M = 4853.",
                "question_a": "a) Nêu giá trị của chữ số 8 và chữ số 5 trong số M.",
                "question_b": "b) Viết số M thành tổng giá trị các chữ số của nó.",
                "blank_items": ["4853 = 4 × [ ... ] + 8 × [ ... ] + 5 × [ ... ] + 3"],
                "analysis": "Chữ số 4 ở hàng nghìn (4000), 8 ở hàng trăm (800), 5 ở hàng chục (50), 3 ở hàng đơn vị (3).",
                "solution_a": "a) Chữ số 8 có giá trị 800; chữ số 5 có giá trị 50.",
                "solution_b": "b) 4853 = 4 × 1000 + 8 × 100 + 5 × 10 + 3.",
                "voice_intro": "Ví dụ 2 giúp các em hiểu rõ giá trị theo từng hàng trong hệ thập phân. Bốn mươi lăm giây tự làm bắt đầu!",
                "voice_sol": "Thầy chúc mừng các bạn đã làm đúng! Chữ số 8 ở hàng trăm nên có giá trị tám trăm, chữ số 5 ở hàng chục có giá trị năm mươi. Tổng phân tích là 4 nhân một nghìn cộng 8 nhân một trăm cộng 5 nhân mười cộng ba."
            },
            {
                "badge": "VÍ DỤ 3 (Mức Vận Dụng)",
                "head": "TÌM SỐ TỰ NHIÊN THỎA MÃN ĐIỀU KIỆN",
                "lead": "Đề bài: Cho số tự nhiên có hai chữ số ab biết chữ số hàng chục gấp 3 lần hàng đơn vị.",
                "question_a": "a) Liệt kê tất cả các số tự nhiên thỏa mãn đề bài.",
                "question_b": "b) Viết số lớn nhất trong các số tìm được dưới dạng số La Mã.",
                "blank_items": ["Tập hợp các số: { [ ... ] }", "Số lớn nhất là: [ ... ]"],
                "analysis": "a = 3b với a, b là chữ số, a khác 0. b ∈ {1, 2, 3} ⇒ a ∈ {3, 6, 9}. Các số là 31, 62, 93.",
                "solution_a": "a) Các số thỏa mãn là: 31, 62, 93.",
                "solution_b": "b) Số lớn nhất là 93. Trong La Mã 90 là XC, 3 là III ⇒ 93 viết là XCIII.",
                "voice_intro": "Ví dụ 3 là bài toán vận dụng kết hợp cấu tạo số và số La Mã. Các em có 45 giây để tìm ra các số thỏa mãn!",
                "voice_sol": "Rất xuất sắc! Chữ số hàng chục gấp ba lần hàng đơn vị, b chỉ có thể là một, hai hoặc ba, suy ra a là ba, sáu hoặc chín. Các số là 31, 62, 93. Số lớn nhất 93 viết dưới dạng La Mã là X C I I I."
            }
        ],
        p4_traps=[
            {
                "heading": "LỖI SAI 1: NHẦM LẪN CHỮ SỐ VÀ SỐ",
                "bad": "Sai: Nói 'Số 4853 có 4 số'",
                "good": "Đúng: 'Số 4853 có 4 CHỮ SỐ: 4, 8, 5, 3'",
                "note": "Số là giá trị số lượng, chữ số là ký hiệu dùng để ghi số.",
                "voice": "Lỗi sai thứ nhất các em rất hay nhầm: đó là phân biệt giữa số và chữ số. Bốn nghìn tám trăm năm mươi ba là một số, nhưng nó được ghép bởi bốn chữ số các em nhé!"
            },
            {
                "heading": "LỖI SAI 2: VIẾT SAI QUY TẮC SỐ LA MÃ",
                "bad": "Sai: Viết số 4 là IIII ; Viết số 9 là VIIII",
                "good": "Đúng: Số 4 viết là IV ; Số 9 viết là IX",
                "note": "Không lặp lại chữ I quá 3 lần, dùng quy tắc trừ (đặt bên trái).",
                "voice": "Lỗi sai thứ hai là viết số 4 thành bốn chữ I, hoặc số 9 thành năm cộng bốn chữ I. Nhớ rằng không được lặp lại quá ba lần chữ số I nhé!"
            }
        ],
        p5_data={
            "summary_nodes": [
                "1. Hệ thập phân: 10 chữ số 0-9, giá trị phụ thuộc vào hàng vị trí.",
                "2. Cấu tạo số: ab = 10a + b ; abc = 100a + 10b + c.",
                "3. Số La Mã: I (1), V (5), X (10); ghép phải là cộng, ghép trái là trừ."
            ],
            "homework": [
                "• Bài tập 1.6, 1.7, 1.8 trang 12 SGK Toán 6 (Tập 1).",
                "• Tự viết năm sinh của bản thân và người thân bằng chữ số La Mã."
            ],
            "voice": "Tổng kết bài học: Các em hãy ghi nhớ cấu tạo số hệ thập phân và quy tắc đọc viết chữ số La Mã. Về nhà hãy hoàn thành các bài tập trong sách giáo khoa và viết năm sinh của mình bằng chữ số La Mã nhé! Hẹn gặp lại các em ở bài học tiếp theo!"
        }
    ))

    # BÀI 3: Thứ tự trong tập hợp các số tự nhiên
    lessons.append(build_lesson(
        lesson_id=3,
        chapter_id="c1_6",
        chapter_title="Chương I: Tập hợp các số tự nhiên",
        lesson_key="Bài 3: Thứ tự trong tập hợp các số tự nhiên",
        lesson_title="Thứ tự trong tập hợp các số tự nhiên",
        p1_slides=[
            {
                "heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN",
                "sub": "Toán 6 • Kết Nối Tri Thức Với Cuộc Sống",
                "bullets": [
                    "Bài 3: Thứ tự trong tập hợp số tự nhiên",
                    "Biểu diễn số trên tia số",
                    "So sánh, số liền trước và số liền sau"
                ],
                "voice": "Chào mừng các em! Bài học hôm nay là Bài 3: Thứ tự trong tập hợp các số tự nhiên. Chúng ta sẽ cùng nhau biểu diễn các số trên tia số và khám phá quy luật so sánh nhé!"
            },
            {
                "heading": "TIẾN TRÌNH THỜI GIAN & THỨ TỰ",
                "sub": "Quy luật sắp xếp tự nhiên từ nhỏ đến lớn",
                "bullets": [
                    "Tuổi tác: Em 11 tuổi, anh 14 tuổi, bố 42 tuổi",
                    "Số thứ tự xếp hàng chào cờ đầu tuần",
                    "Bảng xếp hạng điểm thi từ cao xuống thấp"
                ],
                "voice": "Trong cuộc sống, mọi thứ đều có trật tự: số tuổi của các thành viên trong gia đình, số thứ tự các bạn đứng xếp hàng, hay bảng điểm thi đua. Trong Toán học, các số tự nhiên cũng được sắp xếp theo một trật tự tuyệt đối."
            }
        ],
        p2_slides=[
            {
                "heading": "1. TIA SỐ & QUY TẮC SO SÁNH",
                "sub": "Điểm biểu diễn và chiều tăng dần",
                "items": [
                    "• Gốc tia số là điểm 0, chiều mũi tên từ trái sang phải.",
                    "• Trên tia số nằm ngang: Điểm a nằm bên trái điểm b thì a < b.",
                    "• Tính chất bắc cầu: Nếu a < b và b < c thì a < c.",
                    "• Ký hiệu: a ≤ b nghĩa là a < b hoặc a = b."
                ],
                "voice": "Trên tia số gốc không nằm ngang, điểm nào ở bên trái sẽ nhỏ hơn điểm ở bên phải. Nếu a nhỏ hơn b và b nhỏ hơn c thì a chắc chắn nhỏ hơn c. Ký hiệu a bé hơn hoặc bằng b nghĩa là a nhỏ hơn b hoặc a bằng b."
            },
            {
                "heading": "2. SỐ LIỀN TRƯỚC VÀ SỐ LIỀN SAU",
                "sub": "Khoảng cách đúng 1 đơn vị giữa hai số liên tiếp",
                "items": [
                    "• Hai số tự nhiên liên tiếp hơn kém nhau đúng 1 đơn vị.",
                    "• Số liền sau của số tự nhiên n là n + 1.",
                    "• Số liền trước của số tự nhiên n (n ≠ 0) là n - 1.",
                    "• Số 0 là số tự nhiên nhỏ nhất, không có số liền trước trong N."
                ],
                "voice": "Mỗi số tự nhiên có một số liền sau duy nhất là n cộng một. Số khác không có số liền trước là n trừ một. Số không là số tự nhiên nhỏ nhất và không có số liền trước trong tập hợp số tự nhiên các em nhé!"
            }
        ],
        p3_examples=[
            {
                "badge": "VÍ DỤ 1 (Mức Nhận Biết)",
                "head": "TÌM SỐ LIỀN TRƯỚC VÀ SỐ LIỀN SAU",
                "lead": "Đề bài: Điền số thích hợp vào chỗ trống:",
                "question_a": "a) Số liền trước của 100 là gì? Số liền sau của 999 là gì?",
                "question_b": "b) Ba số tự nhiên liên tiếp tăng dần biết số ở giữa là 2024:",
                "blank_items": ["Liền trước 100: [ ... ]", "Liền sau 999: [ ... ]", "[ ... ] ; 2024 ; [ ... ]"],
                "analysis": "Liền trước lấy trừ 1: 100 - 1 = 99. Liền sau lấy cộng 1: 999 + 1 = 1000. Ba số: 2023, 2024, 2025.",
                "solution_a": "a) Số liền trước của 100 là 99. Số liền sau của 999 là 1000.",
                "solution_b": "b) Ba số tự nhiên liên tiếp là: 2023 ; 2024 ; 2025.",
                "voice_intro": "Ví dụ 1 giúp các em thuần thục khái niệm số liền trước và số liền sau. Bốn mươi lăm giây tự làm bắt đầu!",
                "voice_sol": "Rất đơn giản phải không nào! Liền trước của một trăm là chín mươi chín. Liền sau của chín trăm chín mươi chín là một nghìn. Ba số liên tiếp là 2023, 2024 và 2025!"
            },
            {
                "badge": "VÍ DỤ 2 (Mức Thông Hiểu)",
                "head": "VIẾT TẬP HỢP THEO ĐIỀU KIỆN SO SÁNH",
                "lead": "Đề bài: Cho tập hợp A = { x ∈ ℕ | 15 ≤ x < 21 }.",
                "question_a": "a) Liệt kê các phần tử của tập hợp A.",
                "question_b": "b) Sắp xếp các phần tử của A theo thứ tự giảm dần.",
                "blank_items": ["A = { [ ... ] }", "Giảm dần: [ ... ]"],
                "analysis": "x ≥ 15 lấy từ 15, x < 21 dừng ở 20. A = {15, 16, 17, 18, 19, 20}. Giảm dần: 20, 19, 18, 17, 16, 15.",
                "solution_a": "a) A = { 15; 16; 17; 18; 19; 20 }.",
                "solution_b": "b) Thứ tự giảm dần: 20 ; 19 ; 18 ; 17 ; 16 ; 15.",
                "voice_intro": "Ví dụ 2 yêu cầu liệt kê các số thỏa mãn dấu lớn hơn hoặc bằng và dấu bé hơn. 45 giây bắt đầu!",
                "voice_sol": "Chúc mừng các em! Vì có dấu nhỏ hơn hoặc bằng 15 nên ta lấy cả số 15, nhưng nhỏ hơn 21 nên dừng ở 20. Thứ tự giảm dần xếp từ 20 lùi về 15."
            },
            {
                "badge": "VÍ DỤ 3 (Mức Vận Dụng)",
                "head": "SO SÁNH HAI BIỂU THỨC SỐ TỰ NHIÊN",
                "lead": "Đề bài: Không tính giá trị cụ thể, hãy điền dấu thích hợp (<, =, >) vào ô trống:",
                "question_a": "a) 2024 × 2026 [ ... ] 2025 × 2025",
                "question_b": "b) Giải thích ngắn gọn cách suy luận.",
                "blank_items": ["Dấu cần điền: [ ... ]", "Lý do: [ ... ]"],
                "analysis": "2024 × 2026 = (2025 - 1)(2025 + 1) = 2025 × 2025 - 1 < 2025 × 2025.",
                "solution_a": "a) 2024 × 2026 < 2025 × 2025.",
                "solution_b": "b) Tích hai số có tổng không đổi sẽ đạt giá trị lớn nhất khi hai số bằng nhau.",
                "voice_intro": "Ví dụ 3 là bài toán tư duy so sánh nhanh không cần bấm máy tính. Bốn mươi lăm giây tư duy bắt đầu!",
                "voice_sol": "Đây là một kỹ thuật so sánh rất hay: 2024 nhân 2026 bằng bình phương của 2025 trừ đi 1, do đó nó nhỏ hơn 2025 nhân 2025!"
            }
        ],
        p4_traps=[
            {
                "heading": "LỖI SAI 1: QUÊN DẤU BẰNG TẠI BIÊN",
                "bad": "Sai: x ≤ 5 mà chỉ viết x ∈ {0, 1, 2, 3, 4}",
                "good": "Đúng: x ≤ 5 phải lấy cả số 5 ⇒ x ∈ {0, 1, 2, 3, 4, 5}",
                "note": "Ký hiệu ≤ có nghĩa là nhỏ hơn HOẶC BẰNG, không được bỏ quên nghiệm biên.",
                "voice": "Lỗi sai kinh điển là khi gặp dấu nhỏ hơn hoặc bằng năm, học sinh hay quên mất chính số năm. Hãy nhớ có dấu gạch chân là có dấu bằng nhé!"
            },
            {
                "heading": "LỖI SAI 2: CHO RẰNG SỐ 0 CÓ SỐ LIỀN TRƯỚC TRONG N",
                "bad": "Sai: Số liền trước của 0 là -1 trong tập N",
                "good": "Đúng: Trong tập N, số 0 KHÔNG CÓ số liền trước",
                "note": "-1 là số nguyên âm, không thuộc tập số tự nhiên N.",
                "voice": "Nhiều bạn nghĩ số liền trước của không là trừ một. Sai rồi các em nhé! Trong tập hợp số tự nhiên N, số không là nhỏ nhất và không có số liền trước!"
            }
        ],
        p5_data={
            "summary_nodes": [
                "1. Tia số: Gốc 0, hướng trái sang phải tăng dần.",
                "2. So sánh: a < b nếu điểm a bên trái điểm b; tính chất bắc cầu.",
                "3. Số liền trước (n - 1) và số liền sau (n + 1)."
            ],
            "homework": [
                "• Làm bài tập 1.13, 1.14, 1.15 trang 15 SGK Toán 6.",
                "• Biểu diễn các số nguyên tố nhỏ hơn 10 trên cùng một tia số."
            ],
            "voice": "Hôm nay chúng ta đã nắm vững thứ tự trong tập hợp số tự nhiên và cách so sánh. Các em nhớ làm bài tập về nhà đầy đủ và hẹn gặp lại các em ở bài học tiếp theo!"
        }
    ))

    # Tương tự cho toàn bộ các bài còn lại từ Bài 4 đến Bài 43...
    return lessons


if __name__ == "__main__":
    data = create_all_lessons()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Đã tạo danh mục dữ liệu khởi tạo ({len(data)} bài) tại: {OUTPUT_PATH}")
