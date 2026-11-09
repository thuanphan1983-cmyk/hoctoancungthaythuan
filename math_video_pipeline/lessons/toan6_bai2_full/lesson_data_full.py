"""
GIÁO ÁN TOÀN DIỆN TIẾT HỌC 14-16 PHÚT: BÀI 2: CÁCH GHI SỐ TỰ NHIÊN
Bộ sách: Toán 6 - Kết nối tri thức với cuộc sống
Giáo viên giảng dạy: Thầy Thuấn Phan
Tốc độ đọc giọng AI: rate="-18%" (Chậm rãi, truyền cảm, chuẩn sư phạm học đường)
Tổng số từ kịch bản: > 2.200 từ
"""

import os
import sys
import wave
import math
import struct
import asyncio
import tempfile
import subprocess
import shutil
import edge_tts
from mutagen.mp3 import MP3

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

DEFAULT_VOICE = "vi-VN-NamMinhNeural"
SPEECH_RATE = "-18%"


def generate_tick_audio(output_mp3_path: str, duration_sec: int = 45):
    """Sinh file mp3 tiếng tích tắc đồng hồ 45s êm dịu"""
    if os.path.exists(output_mp3_path) and os.path.getsize(output_mp3_path) > 1000:
        return output_mp3_path

    wav_path = output_mp3_path.replace(".mp3", ".wav")
    sample_rate = 24000
    num_samples = sample_rate * duration_sec

    with wave.open(wav_path, "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        samples = []
        for s in range(num_samples):
            sec_sample = s % sample_rate
            if sec_sample < int(0.035 * sample_rate):
                t = sec_sample / sample_rate
                freq = 880 if ((s // sample_rate) % 2 == 0) else 660
                envelope = math.exp(-t * 110)
                val = int(envelope * 6500 * math.sin(2 * math.pi * freq * t))
            else:
                val = 0
            samples.append(struct.pack("<h", val))
        wav.writeframes(b"".join(samples))

    cmd = ["ffmpeg", "-y", "-i", wav_path, "-c:a", "libmp3lame", "-b:a", "64k", output_mp3_path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    if os.path.exists(wav_path):
        os.remove(wav_path)
    return output_mp3_path


# ==============================================================================
# KỊCH BẢN CHI TIẾT 5 PHẦN BÀI 2 (> 2.200 TỪ)
# ==============================================================================
LESSON_SCRIPTS = {
    "scene1": {
        "title": "Phần 1: Đặt Vấn Đề & Khởi Động Thực Tế",
        "slides": [
            {
                "id": "s1_intro",
                "heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN",
                "sub": "Toán 6 • Kết Nối Tri Thức Với Cuộc Sống",
                "bullets": [
                    "Bài 2: Cách ghi số tự nhiên",
                    "Hệ thập phân & Cấu tạo số tự nhiên",
                    "Chữ số La Mã cổ đại trong đời sống hiện đại"
                ],
                "voice": (
                    "Chào mừng tất cả các em học sinh thân yêu đã quay trở lại với lớp học Toán trực tuyến cùng thầy Thuấn Phan! "
                    "Ở bài học trước, thầy trò chúng ta đã cùng nhau làm quen với khái niệm mở đầu là tập hợp và phần tử của tập hợp. "
                    "Hôm nay, chúng ta sẽ bước sang một bài học vô cùng quan trọng và lý thú: Bài 2: Cách ghi số tự nhiên. "
                    "Bài học này sẽ giúp các em hiểu thấu đáo bản chất của hệ thập phân mà chúng ta sử dụng mỗi ngày, "
                    "cũng như khám phá nét độc đáo của hệ chữ số La Mã cổ đại đã tồn tại hàng nghìn năm lịch sử các em nhé!"
                )
            },
            {
                "id": "s1_life1",
                "heading": "CÁC CON SỐ KHỔNG LỒ TRONG ĐỜI SỐNG",
                "sub": "Từ tiền tệ, dân số đến khoảng cách thiên văn",
                "bullets": [
                    "Dân số Việt Nam: Hơn 100 000 000 người",
                    "Khoảng cách từ Trái Đất đến Mặt Trăng: 384 400 km",
                    "Số tiền trong ngân sách, số căn cước, biển số xe"
                ],
                "voice": (
                    "Trong thế giới hiện đại xung quanh chúng ta, các con số xuất hiện ở khắp mọi nơi. "
                    "Các em có biết dân số nước Việt Nam ta hiện nay đã vượt mốc một trăm triệu người? "
                    "Khoảng cách trung bình từ Trái Đất đến Mặt Trăng là khoảng ba trăm tám mươi tư nghìn bốn trăm ki-lô-mét. "
                    "Hay số căn cước công dân của các em gồm mười hai chữ số, biển số xe máy, giá cả hàng hóa trong siêu thị. "
                    "Làm thế nào mà con người có thể ghi lại và đọc chính xác những con số từ rất nhỏ đến khổng lồ như vậy?"
                )
            },
            {
                "id": "s1_life2",
                "heading": "PHÂN BIỆT RÕ: SỐ VÀ CHỮ SỐ",
                "sub": "Bản chất toán học nền tảng không thể nhầm lẫn",
                "bullets": [
                    "Ngôn ngữ: 29 chữ cái ghép thành hàng vạn từ ngữ",
                    "Toán học: Đúng 10 chữ số (0 đến 9) tạo nên vô tận số tự nhiên",
                    "Ví dụ: Số 2024 được ghi bởi 4 chữ số: 2, 0, 2, 4"
                ],
                "voice": (
                    "Để bắt đầu, thầy muốn các em phân biệt thật rành mạch giữa hai khái niệm: Số và Chữ số. "
                    "Các em hãy liên tưởng đến môn Ngữ văn: Bảng chữ cái tiếng Việt của chúng ta có hai mươi chín chữ cái, "
                    "nhưng khi ghép lại thì tạo nên hàng vạn từ ngữ phong phú. "
                    "Trong Toán học cũng kỳ diệu như vậy! Chỉ với đúng mười chữ số cơ bản từ không đến chín, "
                    "chúng ta có thể ghi lại vô tận các số tự nhiên trong vũ trụ. "
                    "Chẳng hạn, năm 2024 là một số, và số này được viết bởi bốn chữ số: hai, không, hai, bốn."
                )
            },
            {
                "id": "s1_life3",
                "heading": "DẤU ẤN LỊCH SỬ: CHỮ SỐ LA MÃ",
                "sub": "Di sản văn hóa cổ đại vẫn hiện diện hằng ngày",
                "bullets": [
                    "Mặt đồng hồ đeo tay và đồng hồ treo tường cổ điển",
                    "Ký hiệu thế kỷ: Thế kỷ XXI (thế kỷ 21)",
                    "Đánh số thứ tự các chương, phần trong sách vở"
                ],
                "voice": (
                    "Bên cạnh hệ thập phân quen thuộc, chắc hẳn các em đã không ít lần nhìn thấy những ký hiệu như chữ I, chữ V, chữ X. "
                    "Đó chính là chữ số La Mã cổ đại. "
                    "Chúng ta thấy chúng trên mặt đồng hồ đeo tay cổ kính, trên các văn bản ghi thế kỷ hai mươi mốt là X X I, "
                    "hay đầu đề mỗi chương trong sách giáo khoa là Chương một, Chương hai. "
                    "Hôm nay, thầy trò chúng ta sẽ cùng giải mã toàn bộ quy tắc đọc và viết hệ số độc đáo này!"
                )
            }
        ]
    },

    "scene2": {
        "title": "Phần 2: Hình Thành Kiến Thức Mới Cặn Kẽ",
        "slides": [
            {
                "id": "s2_tap_n",
                "heading": "1. TẬP HỢP SỐ TỰ NHIÊN N VÀ N*",
                "sub": "Ký hiệu chuẩn xác theo chương trình GDPT 2018",
                "items": [
                    "• Tập hợp các số tự nhiên được ký hiệu là N:",
                    "   N = { 0; 1; 2; 3; 4; 5; 6; 7; ... }",
                    "• Tập hợp các số tự nhiên KHÁC 0 được ký hiệu là N*:",
                    "   N* = { 1; 2; 3; 4; 5; 6; 7; ... }",
                    "• Ký hiệu: x ∈ N nghĩa là x là một số tự nhiên bất kỳ."
                ],
                "voice": (
                    "Kiến thức cốt lõi đầu tiên các em cần nắm chắc là hai tập hợp số tự nhiên: "
                    "Tập hợp tất cả các số tự nhiên được ký hiệu là chữ N in hoa nét đôi, "
                    "bắt đầu từ số không: N bằng mở ngoặc nhọn, không, một, hai, ba, bốn, chấm phẩy ba chấm, đóng ngoặc nhọn. "
                    "Khi cần xét các số tự nhiên khác không, người ta dùng ký hiệu N sao, có dấu hoa thị ở góc trên. "
                    "Tập N sao bắt đầu từ số một, tức là không chứa phần tử số không các em nhé!"
                )
            },
            {
                "id": "s2_hang_lop",
                "heading": "2. HỆ THẬP PHÂN: CÁC HÀNG VÀ LỚP",
                "sub": "Quy tắc gom nhóm 3 chữ số từ phải sang trái",
                "items": [
                    "• Lớp đơn vị: Hàng đơn vị, hàng chục, hàng trăm",
                    "• Lớp nghìn: Hàng nghìn, hàng chục nghìn, hàng trăm nghìn",
                    "• Lớp triệu: Hàng triệu, hàng chục triệu, hàng trăm triệu",
                    "• Quy tắc: Cứ 10 đơn vị ở một hàng thì tạo thành 1 đơn vị ở hàng liền trước nó."
                ],
                "voice": (
                    "Trong hệ thập phân, cứ mười đơn vị ở một hàng thì tạo thành một đơn vị ở hàng liền trước nó. "
                    "Mười đơn vị bằng một chục, mười chục bằng một trăm, mười trăm bằng một nghìn. "
                    "Để đọc các số có nhiều chữ số dễ dàng, người ta phân chia thành từng lớp từ phải qua trái, "
                    "mỗi lớp gồm đúng ba hàng: lớp đơn vị gồm hàng đơn vị, chục, trăm; "
                    "tiếp theo là lớp nghìn gồm nghìn, chục nghìn, trăm nghìn; rồi đến lớp triệu, lớp tỉ. "
                    "Khi viết, các em nên cách một khoảng nhỏ giữa các lớp để người đọc dễ theo dõi nhé!"
                )
            },
            {
                "id": "s2_gia_tri",
                "heading": "3. GIÁ TRỊ CỦA CHỮ SỐ THEO VỊ TRÍ HÀNG",
                "sub": "Cùng một chữ số nhưng giá trị hoàn toàn khác nhau",
                "items": [
                    "• Xét số 555 gồm 3 chữ số 5 giống hệt nhau:",
                    "   - Chữ số 5 ở hàng trăm có giá trị: 5 × 100 = 500",
                    "   - Chữ số 5 ở hàng chục có giá trị: 5 × 10 = 50",
                    "   - Chữ số 5 ở hàng đơn vị có giá trị: 5 × 1 = 5",
                    "• Kết luận: Vị trí của chữ số quyết định giá trị của nó."
                ],
                "voice": (
                    "Một đặc điểm vô cùng vi diệu của hệ thập phân là giá trị của mỗi chữ số phụ thuộc vào vị trí hàng mà nó đứng. "
                    "Thầy lấy ví dụ số năm trăm năm mươi lăm: Cả ba chữ số đều là số năm, "
                    "nhưng chữ số năm ngoài cùng bên trái đứng ở hàng trăm nên có giá trị là năm trăm; "
                    "chữ số năm ở giữa đứng ở hàng chục nên có giá trị là năm mươi; "
                    "còn chữ số năm bên phải ở hàng đơn vị chỉ có giá trị là năm đơn vị mà thôi!"
                )
            },
            {
                "id": "s2_cau_tao",
                "heading": "4. CẤU TẠO SỐ TỰ NHIÊN TỔNG QUÁT",
                "sub": "Công thức biểu diễn số bằng tổng các hàng",
                "items": [
                    "• Số có hai chữ số: ab = 10a + b (với a ∈ N*, a ≤ 9; b ∈ N, b ≤ 9)",
                    "• Số có ba chữ số: abc = 100a + 10b + c (với a ≠ 0)",
                    "• Số có bốn chữ số: abcd = 1000a + 100b + 10c + d (với a ≠ 0)",
                    "• Dấu gạch ngang trên đầu: Phân biệt với phép nhân a × b."
                ],
                "voice": (
                    "Trong đại số, khi viết a b liền nhau người ta hay hiểu là a nhân b. "
                    "Vì vậy, để biểu diễn số tự nhiên có hai chữ số, người ta bắt buộc phải đặt dấu gạch ngang trên đầu. "
                    "Số a b gạch đầu có cấu tạo bằng mười nhân a cộng b, với điều kiện a phải khác không. "
                    "Tương tự, số a b c gạch đầu bằng một trăm nhân a cộng mười nhân b cộng c. "
                    "Công thức cấu tạo số này sẽ theo các em suốt từ lớp sáu đến tận lớp chín khi giải bài toán bằng cách lập phương trình đấy!"
                )
            },
            {
                "id": "s2_la_ma_quy_tac",
                "heading": "5. CHỮ SỐ LA MÃ & QUY TẮC CỘNG TRỪ",
                "sub": "Quy tắc ghép số cổ đại độc đáo",
                "items": [
                    "• Ba chữ số cơ bản: I = 1 ; V = 5 ; X = 10",
                    "• Thêm bên phải là CỘNG: VI = 6 ; VII = 7 ; VIII = 8 ; XI = 11 ; XII = 12",
                    "• Thêm bên trái là TRỪ: IV = 5 - 1 = 4 ; IX = 10 - 1 = 9",
                    "• Quy tắc cấm lặp: Không viết chữ I hoặc chữ X quá 3 lần liên tiếp.",
                    "• Chữ V chỉ xuất hiện tối đa 1 lần, tuyệt đối không viết VV."
                ],
                "voice": (
                    "Bây giờ chúng ta sang phần chữ số La Mã: Người La Mã dùng ba chữ cái cơ bản: "
                    "chữ I là một, chữ V là năm, chữ X là mười. "
                    "Quy tắc ghép số rất thú vị: Viết chữ số nhỏ bên phải chữ số lớn nghĩa là CỘNG vào: "
                    "V I là năm cộng một bằng sáu; X I là mười cộng một bằng mười một. "
                    "Viết chữ số nhỏ bên trái chữ số lớn nghĩa là TRỪ đi: "
                    "I V là năm trừ một bằng bốn; I X là mười trừ một bằng chín. "
                    "Các em đặc biệt chú ý: Chữ I và chữ X không được lặp lại quá ba lần liên tiếp, "
                    "và chữ V chỉ xuất hiện một lần duy nhất, tuyệt đối không viết V V nhé!"
                )
            },
            {
                "id": "s2_la_ma_bang",
                "heading": "6. BẢNG TRA CỨU SỐ LA MÃ TỪ 1 ĐẾN 30",
                "sub": "Bảng tổng hợp chuẩn mực theo sách giáo khoa",
                "items": [
                    "• Từ 1 đến 10: I, II, III, IV, V, VI, VII, VIII, IX, X",
                    "• Từ 11 đến 20: XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX",
                    "• Từ 21 đến 30: XXI, XXII, XXIII, XXIV, XXV, XXVI, XXVII, XXVIII, XXIX, XXX",
                    "• Ghi nhớ: Ghép hàng chục trước (X, XX), rồi ghép hàng đơn vị sau."
                ],
                "voice": (
                    "Để đọc viết thành thạo, các em hãy ghi nhớ quy tắc: Viết hàng chục trước rồi ghép hàng đơn vị sau. "
                    "Ví dụ số hai mươi tư: Hai mươi là X X, số bốn là I V, ghép lại ta được X X I V. "
                    "Số hai mươi chín: Hai mươi là X X, số chín là I X, ghép lại là X X I X. "
                    "Nắm được bảng này là các em tự tin chinh phục mọi bài tập đọc viết số La Mã trong đề kiểm tra rồi!"
                )
            }
        ]
    },

    "scene3": {
        "title": "Phần 3: Ba Ví Dụ Minh Họa & Tự Rèn Luyện 45s",
        "examples": [
            {
                "id": "ex1",
                "badge": "VÍ DỤ 1 (Mức Nhận Biết)",
                "head": "ĐỌC VÀ VIẾT CHỮ SỐ LA MÃ CHUẨN XÁC",
                "lead": "Đề bài: Cho các số La Mã sau: XIV, XIX, XXIV, XXVIII.",
                "question_a": "a) Đọc giá trị số tự nhiên tương ứng của từng số La Mã trên.",
                "question_b": "b) Điền ký hiệu thích hợp vào chỗ trống:",
                "blank_items": ["XIV = [ ... ]", "XIX = [ ... ]", "XXIV = [ ... ]", "XXVIII = [ ... ]"],
                "analysis": "Tách thành hàng chục + hàng đơn vị: XIV = 10 + 4 = 14; XIX = 10 + 9 = 19; XXIV = 20 + 4 = 24; XXVIII = 20 + 8 = 28.",
                "solution_a": "a) XIV đọc là mười bốn; XIX là mười chín; XXIV là hai mươi tư; XXVIII là hai mươi tám.",
                "solution_b": "b) XIV = 14 ; XIX = 19 ; XXIV = 24 ; XXVIII = 28.",
                "voice_intro": (
                    "Ví dụ 1 là bài toán nhận biết cơ bản giúp các em rèn luyện kỹ năng đọc và chuyển đổi số La Mã. "
                    "Các em hãy quan sát kỹ từng cụm hàng chục và hàng đơn vị, "
                    "sau đó điền kết quả vào bốn chỗ trống trên màn hình. "
                    "Đồng hồ đếm ngược bốn mươi lăm giây ở góc trên bên phải bắt đầu chạy, các em hãy làm bài thật tập trung nhé!"
                ),
                "voice_sol": (
                    "Thời gian suy nghĩ bốn mươi lăm giây đã kết thúc! Thầy tin chắc các em đều đã có đáp án cho riêng mình. "
                    "Hãy cùng đối chiếu lời giải chi tiết với thầy nào: "
                    "Số đầu tiên X I V gồm mười cộng bốn, bằng mười bốn. "
                    "Số thứ hai X I X gồm mười cộng chín, bằng mười chín. "
                    "Số thứ ba X X I V gồm hai mươi cộng bốn, bằng hai mươi tư. "
                    "Và số cuối cùng X X V I I I gồm hai mươi cộng tám, bằng hai mươi tám. "
                    "Thầy chúc mừng tất cả các em đã làm đúng trọn vẹn cả bốn câu hỏi!"
                )
            },
            {
                "id": "ex2",
                "badge": "VÍ DỤ 2 (Mức Thông Hiểu)",
                "head": "PHÂN TÍCH CẤU TẠO SỐ HỆ THẬP PHÂN",
                "lead": "Đề bài: Cho hai số tự nhiên M = 4853 và N = 7029.",
                "question_a": "a) Nêu vị trí hàng và giá trị của chữ số 8 trong M, chữ số 2 trong N.",
                "question_b": "b) Viết số M và N dưới dạng tổng giá trị các chữ số của nó:",
                "blank_items": [
                    "4853 = 4 × [ ... ] + 8 × [ ... ] + 5 × [ ... ] + 3",
                    "7029 = 7 × [ ... ] + 2 × [ ... ] + 9"
                ],
                "analysis": "4853 có 4 ở hàng nghìn (4000), 8 hàng trăm (800), 5 hàng chục (50), 3 hàng đơn vị. 7029 có 7 hàng nghìn (7000), 0 hàng trăm, 2 hàng chục (20), 9 hàng đơn vị.",
                "solution_a": "a) Chữ số 8 thuộc hàng trăm, giá trị 800; Chữ số 2 thuộc hàng chục, giá trị 20.",
                "solution_b": "b) 4853 = 4 × 1000 + 8 × 100 + 5 × 10 + 3 ; 7029 = 7 × 1000 + 2 × 10 + 9.",
                "voice_intro": (
                    "Bước sang Ví dụ 2, chúng ta sẽ vận dụng kiến thức về hàng và lớp trong hệ thập phân. "
                    "Các em hãy xác định chính xác chữ số tám và chữ số hai nằm ở hàng nào và có giá trị bao nhiêu, "
                    "sau đó điền các số tròn nghìn, tròn trăm, tròn chục thích hợp vào hai dòng công thức cấu tạo số. "
                    "Bốn mươi lăm giây tự rèn luyện bắt đầu!"
                ),
                "voice_sol": (
                    "Đã hết thời gian làm bài! Hãy cùng thầy kiểm tra kết quả từng bước: "
                    "Ở câu a: Trong số M bằng bốn nghìn tám trăm năm mươi ba, chữ số tám đứng ở hàng trăm, "
                    "thuộc lớp đơn vị và mang giá trị là tám trăm. "
                    "Trong số N bằng bảy nghìn không trăm hai mươi chín, chữ số hai đứng ở hàng chục, mang giá trị là hai mươi. "
                    "Ở câu b: Ta phân tích bốn nghìn tám trăm năm mươi ba bằng 4 nhân 1000 cộng 8 nhân 100 cộng 5 nhân 10 cộng 3. "
                    "Còn bảy nghìn không trăm hai mươi chín có hàng trăm bằng không nên viết gọn là 7 nhân 1000 cộng 2 nhân 10 cộng 9. "
                    "Cách viết này phản ánh chính xác bản chất hệ thập phân các em nhé!"
                )
            },
            {
                "id": "ex3",
                "badge": "VÍ DỤ 3 (Mức Vận Dụng Cao)",
                "head": "TÌM SỐ TỰ NHIÊN THỎA MÃN ĐIỀU KIỆN CHỮ SỐ",
                "lead": "Đề bài: Tìm số tự nhiên có hai chữ số ab biết chữ số hàng chục gấp 3 lần chữ số hàng đơn vị và hiệu ab - ba = 54. Viết số đó bằng chữ số La Mã.",
                "question_a": "a) Biến đổi hiệu ab - ba theo cấu tạo số để tìm quan hệ giữa a và b.",
                "question_b": "b) Tìm số tự nhiên ab và viết số đó dưới dạng số La Mã:",
                "blank_items": ["a - b = 54 : 9 = [ ... ]", "b = [ ... ] ; a = [ ... ]", "ab = [ ... ] = [ ... ] (La Mã)"],
                "analysis": "ab - ba = (10a + b) - (10b + a) = 9(a - b) = 54 ⇒ a - b = 6. Mà a = 3b ⇒ 3b - b = 6 ⇒ 2b = 6 ⇒ b = 3 ⇒ a = 9. Số cần tìm là 93. Trong La Mã: 93 = 90 + 3 = XC + III = XCIII.",
                "solution_a": "a) ab - ba = 9(a - b) = 54 suy ra a - b = 6.",
                "solution_b": "b) Vì a = 3b nên 2b = 6 ⇒ b = 3 và a = 9. Số cần tìm là 93, viết là XCIII.",
                "voice_intro": (
                    "Ví dụ 3 là bài toán tư duy vận dụng cao, kết hợp biến đổi cấu tạo số đại số với chữ số La Mã. "
                    "Đây là dạng bài toán phân hóa thường xuất hiện trong đề kiểm tra giữa kỳ để lấy điểm chín, điểm mười. "
                    "Các em hãy vận dụng công thức a b gạch đầu bằng mười a cộng b để khai triển hiệu a b trừ b a. "
                    "Bốn mươi lăm giây thử thách tư duy bắt đầu!"
                ),
                "voice_sol": (
                    "Thầy khen ngợi những bạn đã kiên trì và tìm ra đáp số chính xác! Hãy cùng thầy phân tích lời giải mẫu: "
                    "Khai triển hiệu hai số: a b gạch đầu trừ b a gạch đầu bằng mở ngoặc 10 nhân a cộng b đóng ngoặc, "
                    "trừ đi mở ngoặc 10 nhân b cộng a đóng ngoặc. "
                    "Thu gọn lại ta được đúng 9 lần mở ngoặc a trừ b đóng ngoặc bằng năm mươi tư. "
                    "Từ đó ta suy ra hiệu a trừ b bằng năm mươi tư chia chín, bằng sáu. "
                    "Theo đề bài, chữ số hàng chục gấp ba lần hàng đơn vị, tức là a bằng ba lần b. "
                    "Thay vào ta có: ba b trừ b bằng hai b bằng sáu, suy ra b bằng ba. "
                    "Có b bằng ba thì a bằng chín. Vậy số tự nhiên cần tìm là số chín mươi ba. "
                    "Số 93 trong hệ La Mã tách thành chín mươi cộng ba. Chín mươi là X C, ba là I I I, "
                    "vậy số 93 viết dưới dạng La Mã là X C I I I! Một bài toán thật tuyệt vời đúng không các em!"
                )
            }
        ]
    },

    "scene4": {
        "title": "Phần 4: Lỗi Sai Kinh Điển Cần Tránh Khi Làm Bài Thi",
        "traps": [
            {
                "heading": "LỖI SAI 1: NHẦM LẪN GIỮA 'SỐ' VÀ 'CHỮ SỐ'",
                "bad": "Sai: Nói 'Số 4853 có 4 số'",
                "good": "Đúng: 'Số 4853 có 4 CHỮ SỐ: 4, 8, 5, 3'",
                "note": "Số biểu diễn độ lớn số lượng, chữ số là ký hiệu dùng để ghi số.",
                "voice": (
                    "Lỗi sai thứ nhất các em lớp sáu rất hay mất điểm oan trong bài kiểm tra trắc nghiệm: "
                    "Đó là nhầm lẫn khái niệm giữa số và chữ số. "
                    "Nhiều bạn nói số bốn nghìn tám trăm năm mươi ba có bốn số. Đó là câu nói sai hoàn toàn! "
                    "Chính xác phải là: Số 4853 là MỘT số, và nó được ghép bởi BỐN CHỮ SỐ: bốn, tám, năm, ba các em nhé!"
                )
            },
            {
                "heading": "LỖI SAI 2: VIẾT LẶP LẠI QUÁ 3 LẦN CHỮ I HOẶC X",
                "bad": "Sai: Viết số 4 là IIII ; Viết số 9 là VIIII ; Viết 40 là XXXX",
                "good": "Đúng: Số 4 viết là IV ; Số 9 viết là IX ; Số 40 viết là XL",
                "note": "Tuyệt đối không lặp lại chữ I, X quá 3 lần liên tiếp, bắt buộc dùng quy tắc trừ.",
                "voice": (
                    "Lỗi sai thứ hai là vi phạm quy tắc cấm lặp trong số La Mã. "
                    "Một số bạn quên quy tắc trừ nên viết số bốn thành bốn chữ I, số chín thành V kèm bốn chữ I. "
                    "Hãy nhớ quy tắc sắt son: Không được viết quá ba chữ I hoặc ba chữ X liên tiếp. "
                    "Số bốn bắt buộc phải lấy năm trừ một, viết là I V. Số chín phải lấy mười trừ một, viết là I X!"
                )
            },
            {
                "heading": "LỖI SAI 3: QUÊN ĐIỀU KIỆN CHỮ SỐ ĐẦU TIÊN KHÁC 0",
                "bad": "Sai: Tìm số ab mà cho a = 0 (ví dụ số 05)",
                "good": "Đúng: Chữ số hàng cao nhất bắt buộc phải khác 0 (a ∈ N*, a ≠ 0)",
                "note": "Số tự nhiên có hai chữ số thì chữ số hàng chục a phải từ 1 đến 9.",
                "voice": (
                    "Lỗi sai thứ ba thường gặp trong các bài toán tìm x và chữ số: "
                    "Khi tìm số tự nhiên có hai chữ số a b, chữ số hàng chục đứng đầu tiên bắt buộc phải khác không. "
                    "Không có số tự nhiên có hai chữ số nào là không năm hay không bảy cả. "
                    "Hãy luôn nhớ đặt điều kiện a khác không để không bị trừ điểm điều kiện nhé!"
                )
            },
            {
                "heading": "LỖI SAI 4: ĐẶT KÝ HIỆU TRỪ LA MÃ SAI QUY TẮC",
                "bad": "Sai: Viết 49 là IL (lấy 50 - 1) ; Viết 99 là IC (lấy 100 - 1)",
                "good": "Đúng: 49 = XLIX (40 + 9) ; 99 = XCIX (90 + 9)",
                "note": "Chữ I chỉ được đứng trước V và X. Phải tách theo hàng chục rồi đến hàng đơn vị.",
                "voice": (
                    "Lỗi sai thứ tư là viết tắt quy tắc trừ sai quy chuẩn: "
                    "Nhiều bạn nghĩ số bốn mươi chín bằng năm mươi trừ một nên viết là I L. "
                    "Hay số chín mươi chín bằng một trăm trừ một nên viết là I C. Như vậy là sai quy ước cổ đại! "
                    "Chữ I chỉ được phép đứng trước V và X mà thôi. "
                    "Bốn mươi chín phải tách thành bốn mươi cộng chín, viết là X L I X. "
                    "Chín mươi chín phải tách thành chín mươi cộng chín, viết là X C I X các em nhé!"
                )
            }
        ]
    },

    "scene5": {
        "title": "Phần 5: Sơ Đồ Tư Duy Tổng Kết & Dặn Dò Bài Tập",
        "nodes": [
            "1. Hệ thập phân: 10 chữ số (0 đến 9), giá trị phụ thuộc hàng và lớp.",
            "2. Cấu tạo số: ab = 10a + b ; abc = 100a + 10b + c (với a ≠ 0).",
            "3. Số La Mã: I (1), V (5), X (10); ghép phải CỘNG, ghép trái TRỪ.",
            "4. Quy tắc cấm lặp: Không viết quá 3 lần chữ I, X liên tiếp."
        ],
        "homework": [
            "• Hoàn thành các bài tập 1.6, 1.7, 1.8, 1.9 trang 12 SGK Toán 6 (Tập 1).",
            "• Thử thách thực tế: Viết ngày, tháng, năm sinh của bản thân và người thân bằng chữ số La Mã."
        ],
        "voice": (
            "Như vậy, trong tiết học ngày hôm nay, thầy trò chúng ta đã hoàn thành xuất sắc toàn bộ kiến thức của Bài 2: Cách ghi số tự nhiên. "
            "Các em hãy nhìn lên màn hình và khắc sâu sơ đồ tư duy bốn nhánh: "
            "Thứ nhất là hệ thập phân với mười chữ số cơ bản phân chia theo hàng và lớp. "
            "Thứ hai là công thức cấu tạo số tổng quát. "
            "Thứ ba là ba chữ số La Mã cơ bản I, V, X cùng quy tắc ghép cộng và ghép trừ. "
            "Và thứ tư là quy tắc cấm lặp quá ba lần. "
            "Về nhà, các em hãy làm đầy đủ bài tập trong sách giáo khoa từ bài 1.6 đến 1.9, "
            "và hãy thử thách bản thân bằng cách viết ngày tháng năm sinh của mình bằng chữ số La Mã gửi vào phần bình luận cho thầy xem nhé! "
            "Thầy chúc các em luôn học tập say mê, tiến bộ vượt bậc và hẹn gặp lại các em ở Bài 3 tiếp theo!"
        )
    }
}


# ==============================================================================
# HÀM BỔ TRỢ ĐO THỜI LƯỢNG VÀ XỬ LÝ TEXT
# ==============================================================================
def get_duration(audio_path: str) -> float:
    """Đo thời lượng file mp3 theo giây"""
    if not os.path.exists(audio_path) or os.path.getsize(audio_path) == 0:
        return 0.0
    try:
        return float(MP3(audio_path).info.length)
    except Exception:
        return 10.0


def split_text_into_subsentences(text: str, max_chars: int = 180) -> list:
    """Chia văn bản thành từng câu ngắn dưới 180 ký tự để tránh lỗi websocket"""
    normalized = text.replace("!", ".").replace("?", ".")
    raw_sentences = [s.strip() for s in normalized.split(".") if s.strip()]

    chunks = []
    current_chunk = ""
    for sentence in raw_sentences:
        if len(sentence) > max_chars:
            sub_parts = [p.strip() for p in sentence.replace(";", ",").split(",") if p.strip()]
            for sp in sub_parts:
                if len(current_chunk) + len(sp) + 2 <= max_chars:
                    current_chunk += (", " if current_chunk else "") + sp
                else:
                    if current_chunk:
                        chunks.append(current_chunk + ".")
                    current_chunk = sp
        else:
            if len(current_chunk) + len(sentence) + 2 <= max_chars:
                current_chunk += (". " if current_chunk else "") + sentence
            else:
                if current_chunk:
                    chunks.append(current_chunk + ".")
                current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk + ".")

    return chunks


async def generate_chunk_audio(chunk_text: str, output_path: str, voice=DEFAULT_VOICE, rate=SPEECH_RATE) -> bool:
    """Sinh audio cho 1 đoạn nhỏ có retry và độ trễ ngắt nghỉ"""
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        return True

    for attempt in range(1, 4):
        try:
            communicate = edge_tts.Communicate(text=chunk_text, voice=voice, rate=rate)
            await asyncio.wait_for(communicate.save(output_path), timeout=35.0)
            if os.path.exists(output_path) and os.path.getsize(output_path) > 100:
                await asyncio.sleep(0.35)
                return True
        except Exception:
            await asyncio.sleep(1.0 * attempt)

    # Fallback CLI
    try:
        cmd = ["edge-tts", "--voice", voice, f"--rate={rate}", "--text", chunk_text, "--write-media", output_path]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode == 0 and os.path.exists(output_path) and os.path.getsize(output_path) > 100:
            await asyncio.sleep(0.35)
            return True
    except Exception:
        pass

    return False


async def generate_voice_for_text(text: str, output_path: str, voice=DEFAULT_VOICE, rate=SPEECH_RATE) -> str:
    """Sinh voice cho một đoạn text dài bằng cách ghép các câu nhỏ"""
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        return output_path

    chunks = split_text_into_subsentences(text, max_chars=180)
    temp_dir = tempfile.mkdtemp(prefix="tts_sub_")
    part_files = []

    for idx, c in enumerate(chunks):
        p_path = os.path.join(temp_dir, f"part_{idx:03d}.mp3")
        ok = await generate_chunk_audio(c, p_path, voice=voice, rate=rate)
        if not ok:
            ok = await generate_chunk_audio(c, p_path, voice=voice, rate=None)
        if os.path.exists(p_path) and os.path.getsize(p_path) > 100:
            part_files.append(p_path)

    if not part_files:
        shutil.rmtree(temp_dir, ignore_errors=True)
        return output_path

    list_file = os.path.join(temp_dir, "list.txt")
    with open(list_file, "w", encoding="utf-8") as f:
        for p in part_files:
            safe_p = p.replace("\\", "/")
            f.write(f"file '{safe_p}'\n")

    if os.path.exists(output_path):
        os.remove(output_path)

    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", output_path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    shutil.rmtree(temp_dir, ignore_errors=True)
    return output_path


def concat_audio_files(file_list: list, output_path: str):
    """Ghép danh sách audio bằng ffmpeg concat demuxer"""
    temp_list = output_path + ".txt"
    with open(temp_list, "w", encoding="utf-8") as f:
        for p in file_list:
            safe_p = p.replace("\\", "/")
            f.write(f"file '{safe_p}'\n")
    if os.path.exists(output_path):
        os.remove(output_path)
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", temp_list, "-c", "copy", output_path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    if os.path.exists(temp_list):
        os.remove(temp_list)


def generate_all_lesson_audios(audio_dir: str):
    """Sinh toàn bộ các file audio cho 5 scene theo kịch bản mở rộng 14-16 phút"""
    os.makedirs(audio_dir, exist_ok=True)
    timing_data = {}
    print("=" * 70)
    print(f"🎙️ BẮT ĐẦU SINH BỘ AUDIO MỞ RỘNG BÀI 2 (14-16 PHÚT) VỚI RATE = {SPEECH_RATE}")
    print("=" * 70)

    # 1. Âm thanh đếm ngược 45s (dùng chung cho Scene 3)
    tick_file = os.path.join(audio_dir, "tick45.mp3")
    print("\n⏰ [TIMER] Đang sinh âm thanh đếm ngược 45s (tick45.mp3)...")
    generate_tick_audio(tick_file, duration_sec=45)
    print(f"   -> Xong! Thời lượng: {get_duration(tick_file):.2f}s")

    # 2. Sinh Audio Scene 1
    print("\n▶️ [SCENE 1] Đang sinh audio 4 slide khởi động...")
    s1_parts = []
    for idx, sl in enumerate(LESSON_SCRIPTS["scene1"]["slides"]):
        part_out = os.path.join(audio_dir, f"scene1_slide{idx+1}.mp3")
        asyncio.run(generate_voice_for_text(sl["voice"], part_out))
        dur = get_duration(part_out)
        s1_parts.append(part_out)
        timing_data[f"scene1_slide{idx+1}"] = dur
        print(f"   - Slide {idx+1} ({sl['heading']}): {dur:.2f}s")

    s1_full = os.path.join(audio_dir, "scene1_full.mp3")
    concat_audio_files(s1_parts, s1_full)
    s1_dur = get_duration(s1_full)
    timing_data["scene1"] = s1_dur
    print(f"   ✅ Hoàn thành Scene 1! Tổng thời lượng: {s1_dur:.2f}s ({s1_dur/60:.2f} phút)")

    # 3. Sinh Audio Scene 2
    print("\n▶️ [SCENE 2] Đang sinh audio 6 slide kiến thức mới...")
    s2_parts = []
    for idx, sl in enumerate(LESSON_SCRIPTS["scene2"]["slides"]):
        part_out = os.path.join(audio_dir, f"scene2_slide{idx+1}.mp3")
        asyncio.run(generate_voice_for_text(sl["voice"], part_out))
        dur = get_duration(part_out)
        s2_parts.append(part_out)
        timing_data[f"scene2_slide{idx+1}"] = dur
        print(f"   - Slide {idx+1} ({sl['heading']}): {dur:.2f}s")

    s2_full = os.path.join(audio_dir, "scene2_full.mp3")
    concat_audio_files(s2_parts, s2_full)
    s2_dur = get_duration(s2_full)
    timing_data["scene2"] = s2_dur
    print(f"   ✅ Hoàn thành Scene 2! Tổng thời lượng: {s2_dur:.2f}s ({s2_dur/60:.2f} phút)")

    # 4. Sinh Audio Scene 3 (3 ví dụ với intro, timer 45s, và solution)
    print("\n▶️ [SCENE 3] Đang sinh audio 3 ví dụ phân hóa & timer 45s...")
    s3_parts = []
    for idx, ex in enumerate(LESSON_SCRIPTS["scene3"]["examples"]):
        intro_out = os.path.join(audio_dir, f"scene3_ex{idx+1}_intro.mp3")
        asyncio.run(generate_voice_for_text(ex["voice_intro"], intro_out))
        intro_dur = get_duration(intro_out)
        s3_parts.append(intro_out)
        timing_data[f"scene3_ex{idx+1}_intro"] = intro_dur
        print(f"   - VD{idx+1} Intro: {intro_dur:.2f}s")

        # Đếm ngược 45s
        s3_parts.append(tick_file)
        timing_data[f"scene3_ex{idx+1}_timer"] = 45.0
        print(f"   - VD{idx+1} Timer 45s: 45.00s")

        # Lời giải chi tiết
        sol_out = os.path.join(audio_dir, f"scene3_ex{idx+1}_sol.mp3")
        asyncio.run(generate_voice_for_text(ex["voice_sol"], sol_out))
        sol_dur = get_duration(sol_out)
        s3_parts.append(sol_out)
        timing_data[f"scene3_ex{idx+1}_sol"] = sol_dur
        print(f"   - VD{idx+1} Solution: {sol_dur:.2f}s")

    s3_full = os.path.join(audio_dir, "scene3_full.mp3")
    concat_audio_files(s3_parts, s3_full)
    s3_dur = get_duration(s3_full)
    timing_data["scene3"] = s3_dur
    print(f"   ✅ Hoàn thành Scene 3! Tổng thời lượng: {s3_dur:.2f}s ({s3_dur/60:.2f} phút)")

    # 5. Sinh Audio Scene 4 (4 bẫy thi)
    print("\n▶️ [SCENE 4] Đang sinh audio 4 bẫy đề thi...")
    s4_parts = []
    for idx, tr in enumerate(LESSON_SCRIPTS["scene4"]["traps"]):
        part_out = os.path.join(audio_dir, f"scene4_trap{idx+1}.mp3")
        asyncio.run(generate_voice_for_text(tr["voice"], part_out))
        dur = get_duration(part_out)
        s4_parts.append(part_out)
        timing_data[f"scene4_trap{idx+1}"] = dur
        print(f"   - Trap {idx+1}: {dur:.2f}s")

    s4_full = os.path.join(audio_dir, "scene4_full.mp3")
    concat_audio_files(s4_parts, s4_full)
    s4_dur = get_duration(s4_full)
    timing_data["scene4"] = s4_dur
    print(f"   ✅ Hoàn thành Scene 4! Tổng thời lượng: {s4_dur:.2f}s ({s4_dur/60:.2f} phút)")

    # 6. Sinh Audio Scene 5 (Sơ đồ tư duy & Dặn dò)
    print("\n▶️ [SCENE 5] Đang sinh audio tổng kết & BTVN...")
    s5_out = os.path.join(audio_dir, "scene5_full.mp3")
    asyncio.run(generate_voice_for_text(LESSON_SCRIPTS["scene5"]["voice"], s5_out))
    s5_dur = get_duration(s5_out)
    timing_data["scene5"] = s5_dur
    print(f"   ✅ Hoàn thành Scene 5! Tổng thời lượng: {s5_dur:.2f}s ({s5_dur/60:.2f} phút)")

    total_all = s1_dur + s2_dur + s3_dur + s4_dur + s5_dur
    print("\n" + "=" * 70)
    print(f"🎉 TỔNG THỜI LƯỢNG TOÀN TIẾT HỌC BÀI 2: {total_all:.2f} GIÂY (~{total_all/60:.2f} PHÚT)")
    print("=" * 70)

    timing_json = os.path.join(audio_dir, "timing_data.json")
    import json
    with open(timing_json, "w", encoding="utf-8") as f:
        json.dump(timing_data, f, indent=2, ensure_ascii=False)
    print(f"📁 Đã lưu dữ liệu thời lượng tại: {timing_json}")
    return timing_data


if __name__ == "__main__":
    audio_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")
    generate_all_lesson_audios(audio_dir)
