"""
GIÁO ÁN TOÀN DIỆN TIẾT HỌC 15-20 PHÚT: BÀI 1: TẬP HỢP - PHẦN TỬ CỦA TẬP HỢP
Bộ sách: Toán 6 - Kết nối tri thức với cuộc sống
Giáo viên giảng dạy: Thầy Thuấn Phan
Tốc độ đọc giọng AI: rate="-18%" (Chậm rãi, truyền cảm, chuẩn sư phạm học đường)
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
SPEECH_RATE = "-18%"  # Chuẩn tốc độ đọc sư phạm chậm rãi, rõ ràng

# ==============================================================================
# HÀM SINH ÂM THANH ĐẾM NGƯỢC 45 GIÂY (SOFT TICK-TOCK AUDIO)
# ==============================================================================
def generate_tick_audio(output_mp3_path: str, duration_sec: int = 45):
    """Sinh file mp3 tiếng tích tắc đồng hồ êm dịu cho khoảng thời gian tự suy nghĩ"""
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
            # Tích tắc trong 35ms đầu mỗi giây
            if sec_sample < int(0.035 * sample_rate):
                t = sec_sample / sample_rate
                freq = 880 if ((s // sample_rate) % 2 == 0) else 660
                envelope = math.exp(-t * 110)
                val = int(envelope * 6500 * math.sin(2 * math.pi * freq * t))
            else:
                val = 0
            samples.append(struct.pack("<h", val))
            
        wav.writeframes(b"".join(samples))

    # Chuyển đổi sang mp3 bằng ffmpeg
    cmd = ["ffmpeg", "-y", "-i", wav_path, "-c:a", "libmp3lame", "-b:a", "64k", output_mp3_path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    if os.path.exists(wav_path):
        os.remove(wav_path)
    return output_mp3_path


# ==============================================================================
# KỊCH BẢN CHI TIẾT 5 PHẦN BÀI HỌC (THỜI LƯỢNG 15-20 PHÚT)
# ==============================================================================
LESSON_SCRIPTS = {
    # --------------------------------------------------------------------------
    # SCENE 1: ĐẶT VẤN ĐỀ & KHỞI ĐỘNG THỰC TẾ (~2.8 phút)
    # --------------------------------------------------------------------------
    "scene1": {
        "title": "Phần 1: Đặt Vấn Đề & Tình Huống Thực Tế",
        "slides": [
            {
                "id": "s1_intro",
                "heading": "HỌC TOÁN CÙNG THẦY THUẤN PHAN",
                "sub": "Toán 6 • Kết Nối Tri Thức Với Cuộc Sống",
                "bullets": [
                    "Bài 1: Tập hợp và phần tử của tập hợp",
                    "Học tập trực quan - Phát triển tư duy",
                    "Chuẩn quy chuẩn sư phạm Bộ Giáo dục"
                ],
                "voice": (
                    "Chào mừng tất cả các em học sinh thân yêu đã đến với lớp học Toán trực tuyến cùng thầy Thuấn Phan! "
                    "Hôm nay, thầy trò chúng ta sẽ cùng nhau bắt đầu một hành trình khám phá môn Toán lớp 6, "
                    "bộ sách Kết nối tri thức với cuộc sống. "
                    "Bài học mở đầu của chương trình là Bài 1: Tập hợp, phần tử của tập hợp. "
                    "Đây là nền móng vô cùng quan trọng cho toàn bộ chương trình Toán Trung học cơ sở các em nhé!"
                )
            },
            {
                "id": "s1_life1",
                "heading": "TẬP HỢP TRONG ĐỜI SỐNG HẰNG NGÀY",
                "sub": "Quan sát các nhóm sự vật quen thuộc",
                "bullets": [
                    "Nhóm 1: Các bạn học sinh trong lớp 6A",
                    "Nhóm 2: Các cuốn sách giáo khoa trên bàn học",
                    "Đặc điểm chung: Cùng thuộc một nhóm xác định"
                ],
                "voice": (
                    "Trong đời sống hằng ngày, các em rất thường xuyên bắt gặp những nhóm đồ vật hay con người có chung đặc điểm. "
                    "Thầy lấy ví dụ: Tập hợp tất cả các bạn học sinh trong lớp 6A của chúng ta. "
                    "Hay khi các em ngồi vào góc học tập, trên giá sách có tập hợp các cuốn sách giáo khoa lớp 6: "
                    "Toán, Ngữ văn, Khoa học tự nhiên, Lịch sử và Địa lí. "
                    "Mỗi nhóm này đều tạo nên một tập hợp rất tự nhiên."
                )
            },
            {
                "id": "s1_life2",
                "heading": "TẬP HỢP XUNG QUANH CHÚNG TA",
                "sub": "Những ví dụ trực quan sinh động",
                "bullets": [
                    "Bàn tay: Tập hợp năm ngón tay trên một bàn tay",
                    "Đất nước: Tập hợp 5 thành phố trực thuộc Trung ương",
                    "Hà Nội, TP.HCM, Hải Phòng, Đà Nẵng, Cần Thơ"
                ],
                "voice": (
                    "Một ví dụ gần gũi nữa: Bàn tay của mỗi chúng ta gồm có tập hợp năm ngón tay: ngón cái, ngón trỏ, ngón giữa, ngón áp út và ngón út. "
                    "Hoặc về mặt địa lí, đất nước Việt Nam thân yêu của chúng ta có tập hợp 5 thành phố trực thuộc Trung ương, "
                    "đó là: Thủ đô Hà Nội, Thành phố Hồ Chí Minh, Hải Phòng, Đà Nẵng và Cần Thơ. "
                    "Tất cả những nhóm đối tượng này đều là các tập hợp trong thực tế."
                )
            },
            {
                "id": "s1_trans",
                "heading": "DẪN NHẬP VÀO KIẾN THỨC MỚI",
                "sub": "Từ đời sống bước vào Toán học",
                "bullets": [
                    "Khái niệm mở đầu: Tập hợp (Set)",
                    "Ký hiệu và cách biểu diễn một tập hợp",
                    "Mời các em bước vào PHẦN 2: HÌNH THÀNH KIẾN THỨC!"
                ],
                "voice": (
                    "Vậy trong Toán học, một tập hợp được định nghĩa và ký hiệu như thế nào? "
                    "Làm sao để biểu diễn các phần tử bên trong nó một cách ngắn gọn, chính xác tuyệt đối? "
                    "Thầy mời các em cùng mở vở ghi bài và bước sang Phần 2: Hình thành kiến thức mới nhé!"
                )
            }
        ]
    },

    # --------------------------------------------------------------------------
    # SCENE 2: HÌNH THÀNH KIẾN THỨC MỚI CẶN KẼ (~6.0 phút)
    # --------------------------------------------------------------------------
    "scene2": {
        "title": "Phần 2: Hình Thành Kiến Thức Mới Cặn Kẽ",
        "slides": [
            {
                "id": "s2_name",
                "heading": "1. QUY ƯỚC ĐẶT TÊN TẬP HỢP",
                "sub": "Quy tắc chữ cái IN HOA",
                "bullets": [
                    "Tên tập hợp: Dùng chữ cái IN HOA: A, B, C, X, Y...",
                    "Phần tử: Các đối tượng bên trong tập hợp",
                    "Ví dụ: Tập hợp A gồm các số tự nhiên nhỏ hơn 5"
                ],
                "voice": (
                    "Nội dung trọng tâm thứ nhất: Tên của tập hợp thường được đặt bằng các chữ cái in hoa. "
                    "Các em có thể dùng chữ cái A lớn, B lớn, C lớn, hoặc X, Y... "
                    "Các đối tượng nằm bên trong tập hợp thì được gọi là các phần tử của tập hợp đó. "
                    "Chẳng hạn: Tập hợp A gồm các số tự nhiên nhỏ hơn 5. Khi đó, mỗi số 0, 1, 2, 3, 4 là một phần tử của tập hợp A."
                )
            },
            {
                "id": "s2_method1",
                "heading": "2. CÁCH 1: LIỆT KÊ CÁC PHẦN TỬ",
                "sub": "3 quy tắc vàng bắt buộc ghi nhớ",
                "bullets": [
                    "Quy tắc 1: Viết các phần tử trong cặp dấu ngoặc nhọn { }",
                    "Quy tắc 2: Ngăn cách nhau bằng dấu chấm phẩy (;)",
                    "Quy tắc 3: Mỗi phần tử chỉ viết ĐÚNG 1 LẦN, thứ tự tùy ý"
                ],
                "voice": (
                    "Nội dung trọng tâm thứ hai: Để biểu diễn một tập hợp, ta có hai cách thông dụng. "
                    "Cách một là Liệt kê các phần tử của tập hợp. "
                    "Các em hãy ghi nhớ 3 quy tắc vàng: "
                    "Quy tắc 1: Tất cả các phần tử phải được đặt bên trong một cặp dấu ngoặc nhọn. "
                    "Quy tắc 2: Các phần tử được ngăn cách nhau bằng dấu chấm phẩy, tuyệt đối không dùng dấu phẩy khi phần tử là các con số. "
                    "Và quy tắc 3: Mỗi phần tử chỉ được viết đúng một lần duy nhất, còn thứ tự xuất hiện là tùy ý."
                )
            },
            {
                "id": "s2_example1",
                "heading": "VÍ DỤ VỀ CÁCH LIỆT KÊ",
                "sub": "Minh họa công thức chuẩn mực",
                "bullets": [
                    "Tập hợp A các số tự nhiên nhỏ hơn 5:",
                    "A = { 0; 1; 2; 3; 4 }",
                    "Thứ tự tùy ý: A = { 4; 0; 3; 1; 2 } vẫn đúng!"
                ],
                "voice": (
                    "Thầy lấy ví dụ cụ thể: Tập hợp A gồm các số tự nhiên nhỏ hơn 5. "
                    "Ta viết: A bằng, mở ngoặc nhọn, 0 chấm phẩy 1 chấm phẩy 2 chấm phẩy 3 chấm phẩy 4, đóng ngoặc nhọn. "
                    "Vì thứ tự là tùy ý, nên nếu các em viết A bằng mở ngoặc nhọn 4 chấm phẩy 0 chấm phẩy 3 chấm phẩy 1 chấm phẩy 2 thì vẫn hoàn toàn chính xác."
                )
            },
            {
                "id": "s2_method2",
                "heading": "3. CÁCH 2: CHỈ RA TÍNH CHẤT ĐẶC TRƯNG",
                "sub": "Nêu quy luật chung của phần tử",
                "bullets": [
                    "Cách làm: Nêu tính chất mà chỉ các phần tử của tập hợp thỏa mãn",
                    "Công thức: A = { x ∈ ℕ | x < 5 }",
                    "Ý nghĩa: x là số tự nhiên và x nhỏ hơn 5"
                ],
                "voice": (
                    "Cách thứ hai để cho một tập hợp là: Chỉ ra tính chất đặc trưng cho các phần tử của tập hợp. "
                    "Nghĩa là chúng ta nêu lên một quy luật chung mà chỉ có các phần tử của tập hợp đó mới thỏa mãn, còn các đối tượng khác thì không. "
                    "Ví dụ, vẫn là tập hợp A các số tự nhiên nhỏ hơn 5, ta viết theo cách đặc trưng như sau: "
                    "A bằng, mở ngoặc nhọn, x thuộc N, gạch đứng, x nhỏ hơn 5, đóng ngoặc nhọn. "
                    "Ký hiệu này có nghĩa là: x là số tự nhiên sao cho x nhỏ hơn 5."
                )
            },
            {
                "id": "s2_belong",
                "heading": "4. KÝ HIỆU THUỘC (∈) VÀ KHÔNG THUỘC (∉)",
                "sub": "Quan hệ giữa phần tử và tập hợp",
                "bullets": [
                    "Ký hiệu ∈ (Thuộc):  3 ∈ A  → '3 thuộc tập hợp A'",
                    "Ký hiệu ∉ (Không thuộc):  5 ∉ A  → '5 không thuộc tập A'",
                    "Lưu ý: Ký hiệu ∈ và ∉ chỉ dùng giữa PHẦN TỬ và TẬP HỢP"
                ],
                "voice": (
                    "Nội dung trọng tâm thứ tư là Mối quan hệ giữa phần tử và tập hợp. "
                    "Chúng ta có hai ký hiệu cốt lõi: "
                    "Nếu số 3 là một phần tử của tập hợp A, ta dùng ký hiệu thuộc, viết là: 3 thuộc A. "
                    "Nếu số 5 không phải là phần tử của tập hợp A, ta dùng ký hiệu không thuộc, viết là: 5 không thuộc A. "
                    "Các em lưu ý: Ký hiệu thuộc và không thuộc chỉ được dùng để nối giữa một phần tử với một tập hợp, chứ không dùng giữa hai tập hợp với nhau."
                )
            },
            {
                "id": "s2_venn",
                "heading": "5. MINH HỌA BẰNG SƠ ĐỒ VEN",
                "sub": "Phương pháp hình học trực quan của John Venn",
                "bullets": [
                    "Biểu diễn tập hợp bằng một đường cong khép kín",
                    "Mỗi điểm nằm BÊN TRONG đường cong là một phần tử thuộc tập hợp",
                    "Mỗi điểm nằm BÊN NGOÀI đường cong không thuộc tập hợp"
                ],
                "voice": (
                    "Nội dung trọng tâm thứ năm: Nhà toán học người Anh John Venn đã phát minh ra cách minh họa tập hợp rất trực quan gọi là Sơ đồ Ven. "
                    "Người ta vẽ một đường cong khép kín, thường là hình tròn hoặc hình elip, để tượng trưng cho tập hợp. "
                    "Mỗi phần tử thuộc tập hợp sẽ được chấm một điểm ở bên trong vòng cong. "
                    "Còn các phần tử không thuộc tập hợp thì nằm hoàn toàn ở phía bên ngoài."
                )
            }
        ]
    },

    # --------------------------------------------------------------------------
    # SCENE 3: HỆ THỐNG 3 VÍ DỤ LỚN + ĐẾM NGƯỢC TỰ LÀM (~8.0 phút)
    # --------------------------------------------------------------------------
    "scene3": {
        "title": "Phần 3: Ba Ví Dụ Minh Họa & Đếm Ngược Tự Làm",
        "examples": [
            {
                "id": "ex1",
                "badge": "VÍ DỤ 1 (Mức Nhận Biết)",
                "heading": "CÁC CHỮ CÁI TRONG TỪ 'HỌC TOÁN'",
                "question": "Cho từ 'HỌC TOÁN'. Viết tập hợp M các chữ cái trong từ này và điền ký hiệu ∈, ∉ thích hợp.",
                "intro_voice": (
                    "Bây giờ, chúng ta cùng bước vào Ví dụ số 1, ở mức độ Nhận biết. "
                    "Đề bài như sau: Cho cụm từ HỌC TOÁN. Hãy viết tập hợp M gồm các chữ cái trong cụm từ này, "
                    "sau đó điền ký hiệu thuộc hoặc không thuộc thích hợp vào chỗ trống. "
                    "Bây giờ, các em hãy tạm dừng màn hình hoặc dành 45 giây để tự nháp câu trả lời vào vở trước khi thầy hướng dẫn nhé!"
                ),
                "timer_sec": 45,
                "solution_voice": (
                    "Đã hết 45 giây làm bài! Thầy khen các em đã hoàn thành phần nháp. Bây giờ cùng đối chiếu lời giải với thầy nào! "
                    "Quan sát cụm từ HỌC TOÁN, ta thấy có các chữ cái: H, O, C, T, O, A, N. "
                    "Trong đó, chữ O xuất hiện hai lần. Theo đúng quy tắc số 3, mỗi phần tử chỉ được viết một lần duy nhất. "
                    "Do đó, tập hợp M gồm 6 phần tử: H, O, C, T, A, N. "
                    "Về ký hiệu: Chữ H thuộc M, chữ T thuộc M, nhưng chữ B không thuộc M, và chữ K không thuộc M."
                ),
                "solution_bullets": [
                    "Phân tích: Các chữ cái: H, O, C, T, O, A, N (chữ O lặp lại)",
                    "Lời giải:  M = { H; O; C; T; A; N }  (Gồm 6 phần tử)",
                    "Điền ký hiệu:  H ∈ M ;  T ∈ M ;  B ∉ M ;  K ∉ M"
                ]
            },
            {
                "id": "ex2",
                "badge": "VÍ DỤ 2 (Mức Thông Hiểu)",
                "heading": "ĐIỀU KIỆN BIÊN CỦA SỐ TỰ NHIÊN",
                "question": "Cho tập hợp  A = { x ∈ ℕ | 12 ≤ x < 18 }. Viết tập hợp A dưới dạng liệt kê và tính số phần tử.",
                "intro_voice": (
                    "Tiếp theo là Ví dụ số 2, ở mức độ Thông hiểu. "
                    "Đề bài: Cho tập hợp A gồm các số tự nhiên x sao cho x lớn hơn hoặc bằng 12 và nhỏ hơn 18. "
                    "Hãy viết tập hợp A bằng cách liệt kê các phần tử và xác định tập hợp A có bao nhiêu phần tử. "
                    "Thầy dành cho các em 45 giây để tự giải vào vở bắt đầu từ bây giờ!"
                ),
                "timer_sec": 45,
                "solution_voice": (
                    "Hết giờ suy nghĩ! Các em cùng chú ý lên màn hình để nghe thầy phân tích bẫy điều kiện biên nhé. "
                    "Đề bài cho: x lớn hơn hoặc bằng 12. Vì có dấu bằng nên ta phải lấy cả số 12. "
                    "Đồng thời, x nhỏ hơn 18, không có dấu bằng, nên ta phải dừng lại ở số 17. "
                    "Như vậy, các số thỏa mãn là: 12, 13, 14, 15, 16 và 17. "
                    "Lời giải: A bằng mở ngoặc nhọn: 12; 13; 14; 15; 16; 17 đóng ngoặc nhọn. "
                    "Tập hợp A có đúng 6 phần tử. Em nào tìm ra đúng 6 phần tử là rất xuất sắc!"
                ),
                "solution_bullets": [
                    "Phân tích: x ≥ 12 (lấy 12) và x < 18 (dừng ở 17)",
                    "Lời giải:  A = { 12; 13; 14; 15; 16; 17 }",
                    "Kết luận: Tập hợp A có đúng 6 phần tử"
                ]
            },
            {
                "id": "ex3",
                "badge": "VÍ DỤ 3 (Mức Vận Dụng Thực Tế)",
                "heading": "SỐ TỰ NHIÊN THỎA MÃN ĐIỀU KIỆN CHỮ SỐ",
                "question": "Viết tập hợp B các số tự nhiên có hai chữ số mà chữ số hàng chục gấp 2 lần chữ số hàng đơn vị.",
                "intro_voice": (
                    "Chúng ta cùng bước sang Ví dụ số 3, mức độ Vận dụng. Đây là dạng bài toán rất hay gặp trong các đề kiểm tra định kỳ. "
                    "Đề bài: Viết tập hợp B gồm các số tự nhiên có hai chữ số, sao cho chữ số hàng chục gấp 2 lần chữ số hàng đơn vị. "
                    "Bây giờ, thầy dành 45 giây để các em suy nghĩ và tìm ra tất cả các số thỏa mãn nhé!"
                ),
                "timer_sec": 45,
                "solution_voice": (
                    "Đã hết thời gian làm bài! Các em hãy cùng thầy lập luận chặt chẽ bài toán này nào. "
                    "Gọi số có hai chữ số cần tìm có dạng là a b có gạch ngang trên đầu. "
                    "Vì là số có hai chữ số nên chữ số hàng chục a phải khác 0. "
                    "Theo đề bài, a bằng 2 lần b. Vì a là chữ số từ 1 đến 9 nên b chỉ có thể nhận các giá trị từ 1 đến 4. "
                    "Nếu b bằng 1 thì a bằng 2, ta được số 21. "
                    "Nếu b bằng 2 thì a bằng 4, ta được số 42. "
                    "Nếu b bằng 3 thì a bằng 6, ta được số 63. "
                    "Nếu b bằng 4 thì a bằng 8, ta được số 84. "
                    "Nếu b bằng 5 thì a bằng 10, vượt quá một chữ số nên ta loại. "
                    "Vậy tập hợp B gồm đúng 4 phần tử: 21, 42, 63 và 84."
                ),
                "solution_bullets": [
                    "Phân tích: Số dạng ab (a ≠ 0; a = 2b; a ≤ 9)",
                    "Các trường hợp của b: b ∈ { 1; 2; 3; 4 } → a ∈ { 2; 4; 6; 8 }",
                    "Lời giải:  B = { 21; 42; 63; 84 }  (Gồm 4 phần tử)"
                ]
            }
        ]
    },

    # --------------------------------------------------------------------------
    # SCENE 4: CẢNH BÁO 4 LỖI SAI KINH ĐIỂN KHI THI (~2.3 phút)
    # --------------------------------------------------------------------------
    "scene4": {
        "title": "Phần 4: Cảnh Báo 4 Lỗi Sai Kinh Điển Khi Làm Bài Thi",
        "traps": [
            {
                "id": "t1",
                "title": "LỖI 1: ĐẶT TÊN BẰNG CHỮ THƯỜNG",
                "wrong": "❌ SAI:  a = { 1; 2; 3 }  (Dùng chữ cái in thường)",
                "right": "✔️ ĐÚNG:  A = { 1; 2; 3 }  (Bắt buộc chữ cái IN HOA)",
                "voice": (
                    "Sang Phần 4, thầy muốn lưu ý các em 4 sai lầm kinh điển mà học sinh rất hay bị trừ điểm trong bài kiểm tra. "
                    "Lỗi sai thứ nhất: Đặt tên tập hợp bằng chữ cái thường. "
                    "Viết a nhỏ bằng mở ngoặc 1 chấm phẩy 2 là sai quy ước toán học! Bắt buộc phải dùng chữ in hoa như A lớn, B lớn các em nhé."
                )
            },
            {
                "id": "t2",
                "title": "LỖI 2: LẶP LẠI PHẦN TỬ TRONG NGOẶC NHỌN",
                "wrong": "❌ SAI:  E = { N; H; A; T; R; A; N; G } (Lặp chữ A, N)",
                "right": "✔️ ĐÚNG:  E = { N; H; A; T; R; G }  (Chỉ ghi 1 lần)",
                "voice": (
                    "Lỗi sai thứ hai: Lặp lại phần tử trong ngoặc nhọn. "
                    "Khi viết tập hợp các chữ cái trong từ NHA TRANG, nhiều bạn ghi hai chữ A và hai chữ N vào trong ngoặc. "
                    "Đây là lỗi sai phổ biến! Quy tắc quy định: Mỗi phần tử chỉ xuất hiện đúng một lần duy nhất."
                )
            },
            {
                "id": "t3",
                "title": "LỖI 3: DÙNG DẤU PHẨY THAY CHO CHẤM PHẨY",
                "wrong": "❌ SAI:  { 1, 2 }  (Dễ bị đọc nhầm thành số thập phân 1,2)",
                "right": "✔️ ĐÚNG:  { 1; 2 }  (Với phần tử là số, bắt buộc dùng ;)",
                "voice": (
                    "Lỗi sai thứ ba: Dùng dấu phẩy thay cho dấu chấm phẩy giữa các số. "
                    "Nếu các em viết mở ngoặc 1 phẩy 2 đóng ngoặc, người chấm bài có thể đọc nhầm thành số thập phân một phẩy hai. "
                    "Do đó, khi phần tử là các con số, bắt buộc phải dùng dấu chấm phẩy để ngăn cách."
                )
            },
            {
                "id": "t4",
                "title": "LỖI 4: BẪY ĐIỀU KIỆN BIÊN BẤT ĐẲNG THỨC",
                "wrong": "❌ SAI:  x < 5  mà vẫn ghi cả số 5 vào tập hợp",
                "right": "✔️ ĐÚNG:  x < 5 chỉ lấy đến 4; khi x ≤ 5 mới lấy số 5",
                "voice": (
                    "Và lỗi sai thứ tư là Bẫy điều kiện biên. "
                    "Khi đề bài yêu cầu x nhỏ hơn 5, nhiều bạn quen tay vẫn ghi cả số 5 vào. "
                    "Các em nhớ nhé: Chỉ khi nào đề bài có dấu nhỏ hơn hoặc bằng, ta mới lấy số 5; còn dấu nhỏ hơn thì phải dừng lại ở số 4."
                )
            }
        ]
    },

    # --------------------------------------------------------------------------
    # SCENE 5: SƠ ĐỒ TƯ DUY TỔNG KẾT & DẶN DÒ BTVN (~1.7 phút)
    # --------------------------------------------------------------------------
    "scene5": {
        "title": "Phần 5: Sơ Đồ Tư Duy Tổng Kết & Dặn Dò Bài Tập Về Nhà",
        "slides": [
            {
                "id": "s5_mindmap",
                "heading": "SƠ ĐỒ TƯ DUY TỔNG KẾT BÀI 1",
                "sub": "4 Nhánh kiến thức trọng tâm cần khắc cốt ghi tâm",
                "bullets": [
                    "Nhánh 1: Tên in hoa (A, B, C...) • Đối tượng là phần tử",
                    "Nhánh 2: Hai cách viết (Liệt kê { } & Dấu hiệu đặc trưng)",
                    "Nhánh 3: Hai ký hiệu cốt lõi (∈ Thuộc & ∉ Không thuộc)",
                    "Nhánh 4: Sơ đồ Ven (Đường cong khép kín trực quan)"
                ],
                "voice": (
                    "Như vậy, thầy trò chúng ta đã hoàn thành trọn vẹn tiết học ngày hôm nay. "
                    "Các em hãy cùng thầy tổng kết lại bài học qua sơ đồ tư duy bốn nhánh: "
                    "Nhánh 1: Tên tập hợp viết in hoa, đối tượng bên trong là phần tử. "
                    "Nhánh 2: Hai cách cho tập hợp: Liệt kê phần tử trong ngoặc nhọn và Nêu tính chất đặc trưng. "
                    "Nhánh 3: Hai ký hiệu quan trọng: thuộc và không thuộc. "
                    "Và Nhánh 4: Minh họa trực quan bằng Sơ đồ Ven."
                )
            },
            {
                "id": "s5_homework",
                "heading": "NHIỆM VỤ TỰ HỌC VỀ NHÀ",
                "sub": "Rèn luyện kỹ năng và chuẩn bị bài mới",
                "bullets": [
                    "1. Vẽ lại sơ đồ tư duy Bài 1 vào vở ghi",
                    "2. Hoàn thành bài tập 1.1 đến 1.5 trong SGK Toán 6",
                    "3. Đón xem BÀI 2: CÁCH GHI SỐ TỰ NHIÊN trên kênh Thầy Thuấn Phan!"
                ],
                "voice": (
                    "Về nhà, thầy dặn dò các em hai nhiệm vụ: "
                    "Thứ nhất: Vẽ lại sơ đồ tư duy bốn nhánh vào vở ghi bài. "
                    "Thứ hai: Làm đầy đủ các bài tập từ 1.1 đến 1.5 trong Sách giáo khoa Toán 6 Kết nối tri thức. "
                    "Cảm ơn các em đã chú ý lắng nghe tiết học. Thầy chúc các em học tập thật tốt, yêu thích môn Toán và hẹn gặp lại các em trong video tiếp theo: Bài 2, Cách ghi số tự nhiên. "
                    "Xin chào và hẹn gặp lại tất cả các em!"
                )
            }
        ]
    }
}


# ==============================================================================
# QUY TRÌNH TỰ ĐỘNG SINH AUDIO TỪNG PHẦN BẰNG EDGE-TTS VỚI DELAY VÀ RETRY
# ==============================================================================
async def generate_chunk_audio(chunk_text: str, output_path: str, voice=DEFAULT_VOICE, rate=SPEECH_RATE) -> bool:
    """Sinh audio cho 1 đoạn nhỏ có retry và độ trễ ngắt nghỉ"""
    for attempt in range(1, 4):
        try:
            communicate = edge_tts.Communicate(text=chunk_text, voice=voice, rate=rate)
            await communicate.save(output_path)
            if os.path.exists(output_path) and os.path.getsize(output_path) > 100:
                await asyncio.sleep(0.4)
                return True
        except Exception:
            await asyncio.sleep(1.0 * attempt)
            
    # Thử qua CLI
    try:
        cmd = ["edge-tts", "--voice", voice, "--rate", rate, "--text", chunk_text, "--write-media", output_path]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode == 0 and os.path.exists(output_path) and os.path.getsize(output_path) > 100:
            await asyncio.sleep(0.4)
            return True
    except Exception:
        pass
        
    return False


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


async def generate_voice_for_text(text: str, output_path: str, voice=DEFAULT_VOICE, rate=SPEECH_RATE) -> str:
    """Sinh voice cho một đoạn text dài bằng cách ghép các câu nhỏ"""
    chunks = split_text_into_subsentences(text, max_chars=180)
    temp_dir = tempfile.mkdtemp(prefix="tts_sub_")
    part_files = []
    
    for idx, c in enumerate(chunks):
        p_path = os.path.join(temp_dir, f"part_{idx:03d}.mp3")
        ok = await generate_chunk_audio(c, p_path, voice=voice, rate=rate)
        if not ok:
            # Retry không rate
            ok = await generate_chunk_audio(c, p_path, voice=voice, rate=None)
        part_files.append(p_path)
        
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


def generate_all_lesson_audios(audio_dir: str):
    """Sinh toàn bộ các file audio cho 5 scene theo kịch bản mở rộng 15-20 phút"""
    os.makedirs(audio_dir, exist_ok=True)
    timing_data = {}
    print("=" * 70)
    print("🎙️ BẮT ĐẦU SINH BỘ AUDIO MỞ RỘNG (15-20 PHÚT) VỚI RATE = -18%")
    print("=" * 70)

    # 1. Âm thanh đếm ngược 45s (dùng chung cho Scene 3)
    tick_file = os.path.join(audio_dir, "tick45.mp3")
    print("\n⏰ [TIMER] Đang sinh âm thanh đếm ngược 45s (tick45.mp3)...")
    generate_tick_audio(tick_file, duration_sec=45)
    print(f"   -> Xong! Thời lượng: {get_duration(tick_file):.2f}s")

    # 2. Sinh Audio Scene 1
    print("\n▶️ [SCENE 1] Đang sinh audio 4 slide...")
    s1_parts = []
    for idx, sl in enumerate(LESSON_SCRIPTS["scene1"]["slides"]):
        part_out = os.path.join(audio_dir, f"scene1_slide{idx+1}.mp3")
        asyncio.run(generate_voice_for_text(sl["voice"], part_out))
        dur = get_duration(part_out)
        s1_parts.append(part_out)
        timing_data[f"scene1_slide{idx+1}"] = dur
        print(f"   - Slide {idx+1} ({sl['heading']}): {dur:.2f}s")
    
    # Ghép toàn bộ Scene 1
    s1_full = os.path.join(audio_dir, "scene1_full.mp3")
    concat_audio_files(s1_parts, s1_full)
    s1_dur = get_duration(s1_full)
    timing_data["scene1"] = s1_dur
    print(f"   ✅ Hoàn thành Scene 1! Tổng thời lượng: {s1_dur:.2f}s ({s1_dur/60:.2f} phút)")

    # 3. Sinh Audio Scene 2
    print("\n▶️ [SCENE 2] Đang sinh audio 6 slide...")
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

    # 4. Sinh Audio Scene 3 (Kèm 3 đoạn tick45)
    print("\n▶️ [SCENE 3] Đang sinh audio 3 ví dụ lớn + 3 lần đếm ngược 45s...")
    s3_parts = []
    for idx, ex in enumerate(LESSON_SCRIPTS["scene3"]["examples"]):
        # Lời dẫn và đọc đề
        intro_out = os.path.join(audio_dir, f"scene3_ex{idx+1}_intro.mp3")
        asyncio.run(generate_voice_for_text(ex["intro_voice"], intro_out))
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
        asyncio.run(generate_voice_for_text(ex["solution_voice"], sol_out))
        sol_dur = get_duration(sol_out)
        s3_parts.append(sol_out)
        timing_data[f"scene3_ex{idx+1}_sol"] = sol_dur
        print(f"   - VD{idx+1} Solution: {sol_dur:.2f}s")

    s3_full = os.path.join(audio_dir, "scene3_full.mp3")
    concat_audio_files(s3_parts, s3_full)
    s3_dur = get_duration(s3_full)
    timing_data["scene3"] = s3_dur
    print(f"   ✅ Hoàn thành Scene 3! Tổng thời lượng: {s3_dur:.2f}s ({s3_dur/60:.2f} phút)")

    # 5. Sinh Audio Scene 4
    print("\n▶️ [SCENE 4] Đang sinh audio 4 bẫy đề thi...")
    s4_parts = []
    for idx, tr in enumerate(LESSON_SCRIPTS["scene4"]["traps"]):
        part_out = os.path.join(audio_dir, f"scene4_trap{idx+1}.mp3")
        asyncio.run(generate_voice_for_text(tr["voice"], part_out))
        dur = get_duration(part_out)
        s4_parts.append(part_out)
        timing_data[f"scene4_trap{idx+1}"] = dur
        print(f"   - Trap {idx+1} ({tr['title']}): {dur:.2f}s")

    s4_full = os.path.join(audio_dir, "scene4_full.mp3")
    concat_audio_files(s4_parts, s4_full)
    s4_dur = get_duration(s4_full)
    timing_data["scene4"] = s4_dur
    print(f"   ✅ Hoàn thành Scene 4! Tổng thời lượng: {s4_dur:.2f}s ({s4_dur/60:.2f} phút)")

    # 6. Sinh Audio Scene 5
    print("\n▶️ [SCENE 5] Đang sinh audio tổng kết & BTVN...")
    s5_parts = []
    for idx, sl in enumerate(LESSON_SCRIPTS["scene5"]["slides"]):
        part_out = os.path.join(audio_dir, f"scene5_slide{idx+1}.mp3")
        asyncio.run(generate_voice_for_text(sl["voice"], part_out))
        dur = get_duration(part_out)
        s5_parts.append(part_out)
        timing_data[f"scene5_slide{idx+1}"] = dur
        print(f"   - Slide {idx+1} ({sl['heading']}): {dur:.2f}s")

    s5_full = os.path.join(audio_dir, "scene5_full.mp3")
    concat_audio_files(s5_parts, s5_full)
    s5_dur = get_duration(s5_full)
    timing_data["scene5"] = s5_dur
    print(f"   ✅ Hoàn thành Scene 5! Tổng thời lượng: {s5_dur:.2f}s ({s5_dur/60:.2f} phút)")

    total_all = s1_dur + s2_dur + s3_dur + s4_dur + s5_dur
    print("\n" + "=" * 70)
    print(f"🎉 TỔNG THỜI LƯỢNG TOÀN TIẾT HỌC: {total_all:.2f} GIÂY (~{total_all/60:.2f} PHÚT)")
    print("=" * 70)

    # Lưu timing data ra JSON để các Scene Manim đọc chính xác
    timing_json = os.path.join(audio_dir, "timing_data.json")
    import json
    with open(timing_json, "w", encoding="utf-8") as f:
        json.dump(timing_data, f, indent=2, ensure_ascii=False)
    print(f"📁 Đã lưu dữ liệu thời lượng tại: {timing_json}")
    return timing_data


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


if __name__ == "__main__":
    audio_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")
    generate_all_lesson_audios(audio_dir)
