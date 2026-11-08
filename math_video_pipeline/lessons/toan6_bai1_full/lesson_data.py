"""
GIÁO ÁN BÀI GIẢNG TOÀN DIỆN: BÀI 1: TẬP HỢP - PHẦN TỬ CỦA TẬP HỢP (TOÁN 6)
Bộ sách: Kết nối tri thức với cuộc sống
Giáo viên giảng dạy: Thầy Thuấn Phan
Quy chuẩn 5 phần bài dạy: Khởi động -> Kiến thức -> Ví dụ -> Cảnh báo -> Tổng kết
"""

import os
import sys
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
SPEECH_RATE = "-5%"  # Tốc độ đọc chậm rãi, sư phạm chuẩn mực cho tiết dạy

LESSON_SCRIPTS = {
    "scene1": {
        "title": "Phần 1: Đặt Vấn Đề & Khởi Động",
        "voice_text": (
            "Chào mừng tất cả các em học sinh thân yêu đã đến với tiết học Toán trực tuyến cùng thầy Thuấn Phan! "
            "Hôm nay, chúng ta cùng nhau bước vào bài học đầu tiên trong chương trình Toán lớp 6, bộ sách Kết nối tri thức với cuộc sống: "
            "Bài 1, Tập hợp và các phần tử của tập hợp. "
            "Trong cuộc sống hàng ngày, các em thường xuyên bắt gặp những nhóm đồ vật hoặc nhóm người có chung một đặc điểm. "
            "Chẳng hạn: tập hợp các bạn học sinh trong lớp 6A, tập hợp các cuốn sách giáo khoa trên giá sách, "
            "tập hợp năm ngón tay trên một bàn tay, hay tập hợp các thành phố trực thuộc Trung ương của đất nước Việt Nam chúng ta: "
            "gồm Hà Nội, Thành phố Hồ Chí Minh, Hải Phòng, Đà Nẵng và Cần Thơ. "
            "Tất cả những ví dụ thực tế này đều dẫn chúng ta đến một khái niệm mở đầu cơ bản nhưng cực kỳ quan trọng trong Toán học, "
            "đó chính là khái niệm Tập hợp. Vậy một tập hợp được viết như thế nào, và các thành phần bên trong nó có mối quan hệ ra sao? "
            "Thầy mời các em cùng bước sang Phần 2 để hình thành kiến thức mới nhé!"
        )
    },
    "scene2": {
        "title": "Phần 2: Hình Thành Kiến Thức Mới",
        "voice_text": (
            "Ở Phần 2, thầy và các em sẽ cùng nhau xây dựng 4 nội dung kiến thức trọng tâm của bài học. "
            "Thứ nhất: Tên của tập hợp thường được đặt bằng các chữ cái in hoa, ví dụ như chữ A, B, C, X, Y... "
            "Các đối tượng nằm bên trong tập hợp được gọi là các phần tử của tập hợp đó. "
            "Thứ hai: Để viết một tập hợp, chúng ta có hai cách thông dụng. "
            "Cách một là Liệt kê các phần tử: Các em viết tất cả các phần tử vào trong một cặp dấu ngoặc nhọn, "
            "ngăn cách nhau bằng dấu chấm phẩy. Chú ý rằng mỗi phần tử chỉ được viết đúng một lần duy nhất, và thứ tự các phần tử là tùy ý. "
            "Cách hai là Chỉ ra tính chất đặc trưng: Chúng ta nêu rõ quy luật chung mà chỉ các phần tử của tập hợp mới thỏa mãn. "
            "Ví dụ, tập hợp A gồm các số tự nhiên nhỏ hơn 5 có thể viết dưới dạng liệt kê là: A bằng, mở ngoặc nhọn, 0 chấm phẩy 1 chấm phẩy 2 chấm phẩy 3 chấm phẩy 4, đóng ngoặc nhọn. "
            "Hoặc viết theo tính chất đặc trưng: A gồm các số x thuộc N sao cho x nhỏ hơn 5. "
            "Thứ ba: Mối quan hệ giữa phần tử và tập hợp. "
            "Nếu số 3 là một phần tử thuộc tập hợp A, ta dùng ký hiệu thuộc, viết là: 3 thuộc A. "
            "Nếu số 5 không phải là phần tử của tập hợp A, ta dùng ký hiệu không thuộc, viết là: 5 không thuộc A. "
            "Cuối cùng, nhà toán học John Venn đã đưa ra cách minh họa tập hợp bằng một đường cong khép kín gọi là Sơ đồ Ven. "
            "Mỗi phần tử thuộc tập hợp được biểu diễn bằng một điểm nằm bên trong vòng tròn, còn các điểm nằm ngoài vòng tròn là các phần tử không thuộc tập hợp."
        )
    },
    "scene3": {
        "title": "Phần 3: Ví Dụ Minh Họa Áp Dụng",
        "voice_text": (
            "Bây giờ, thầy trò chúng ta cùng rèn luyện kỹ năng qua bốn ví dụ từ mức độ nhận biết đến vận dụng nâng cao. "
            "Ví dụ 1, ở mức Nhận biết: Viết tập hợp M gồm các chữ cái trong từ TOÁN HỌC. "
            "Quan sát từ TOÁN HỌC, ta thấy có các chữ: T, O, Á, N, H, O, C. Vì chữ O xuất hiện hai lần, nên theo đúng quy tắc, ta chỉ ghi chữ O đúng một lần duy nhất. "
            "Lời giải: Tập hợp M gồm các phần tử: T, O, Á, N, H, C. "
            "Ví dụ 2, mức Thông hiểu: Cho tập hợp B gồm các số tự nhiên x sao cho x lớn hơn hoặc bằng 10 và nhỏ hơn 15. "
            "Hãy viết tập hợp B bằng cách liệt kê phần tử, sau đó điền ký hiệu thuộc hoặc không thuộc thích hợp. "
            "Phân tích: Vì x lớn hơn hoặc bằng 10 nên ta lấy cả số 10. Nhưng vì x nhỏ hơn 15 nên ta dừng lại ở số 14. "
            "Vậy tập hợp B gồm: 10, 11, 12, 13, 14. Do đó: 10 thuộc B, 12 thuộc B, nhưng 15 không thuộc B và 9 không thuộc B. "
            "Ví dụ 3, Vận dụng thấp: Viết tập hợp C các tháng có đúng 30 ngày trong năm dương lịch. "
            "Các em quan sát lịch: Trong 12 tháng, chỉ có đúng 4 tháng có 30 ngày, đó là: Tháng 4, Tháng 6, Tháng 9 và Tháng 11. "
            "Ví dụ 4, Vận dụng nâng cao: Viết tập hợp D các số tự nhiên có hai chữ số mà tổng các chữ số bằng 5. "
            "Gọi số có hai chữ số là a b, chữ số hàng chục a phải khác 0. Ta có các cặp số có tổng bằng 5 là: 5 cộng 0, 4 cộng 1, 3 cộng 2, 2 cộng 3, và 1 cộng 4. "
            "Như vậy tập hợp D gồm 5 số: 14, 23, 32, 41 và 50."
        )
    },
    "scene4": {
        "title": "Phần 4: Lỗi Sai & Cảnh Báo Bẫy Thi",
        "voice_text": (
            "Trong quá trình chấm bài thi và kiểm tra, thầy nhận thấy học sinh thường mắc phải 5 sai lầm phổ biến sau đây. Các em hãy ghi chú cẩn thận để không bị mất điểm đáng tiếc nhé! "
            "Lỗi sai thứ nhất: Đặt tên tập hợp bằng chữ cái thường. Chẳng hạn viết tập hợp a nhỏ bằng mở ngoặc 1, 2 là sai quy ước! Bắt buộc phải dùng chữ in hoa như A lớn. "
            "Lỗi sai thứ hai: Lặp lại phần tử trong ngoặc nhọn. Ví dụ viết tập hợp chữ cái trong từ NHA TRANG mà ghi hai chữ A và hai chữ N là bị trừ điểm. Mỗi phần tử chỉ xuất hiện duy nhất một lần. "
            "Lỗi sai thứ ba: Dùng dấu phẩy thay vì dấu chấm phẩy giữa các số. Nếu các em viết mở ngoặc 1 phẩy 2 đóng ngoặc, người chấm sẽ đọc nhầm thành số thập phân 1 phẩy 2. Với các phần tử là số, bắt buộc phải dùng dấu chấm phẩy! "
            "Lỗi sai thứ tư: Dùng sai dấu ngoặc tròn hoặc ngoặc vuông thay cho ngoặc nhọn. Tập hợp chỉ được dùng ngoặc nhọn. "
            "Và lỗi sai thứ năm: Bẫy điều kiện biên. Khi đề bài cho x nhỏ hơn 5, nhiều bạn vẫn quen tay ghi cả số 5 vào. Chỉ khi nào có dấu nhỏ hơn hoặc bằng thì ta mới lấy số 5 các em nhé!"
        )
    },
    "scene5": {
        "title": "Phần 5: Tổng Kết & Củng Cố",
        "voice_text": (
            "Như vậy, trong tiết học ngày hôm nay, thầy trò chúng ta đã cùng nhau hoàn thành xuất sắc toàn bộ kiến thức của Bài 1: Tập hợp. "
            "Các em hãy cùng thầy tổng kết lại bài học qua sơ đồ tư duy bốn nhánh: "
            "Nhánh 1: Tên tập hợp viết in hoa, các đối tượng bên trong là phần tử. "
            "Nhánh 2: Hai cách cho tập hợp, gồm Liệt kê phần tử trong ngoặc nhọn và Chỉ ra dấu hiệu đặc trưng. "
            "Nhánh 3: Hai ký hiệu quan trọng: thuộc và không thuộc. "
            "Nhánh 4: Minh họa trực quan bằng Sơ đồ Ven. "
            "Về nhà, các em hãy xem lại video bài giảng, ghi chép đầy đủ các ví dụ vào vở và hoàn thành 3 bài tập rèn luyện trong sách giáo khoa. "
            "Cảm ơn các em đã chú ý lắng nghe. Thầy chúc các em học tập thật tốt và hẹn gặp lại các em trong tiết học tiếp theo: Bài 2, Cách ghi số tự nhiên. Xin chào và hẹn gặp lại!"
        )
    }
}


def split_text_into_chunks(text: str, max_chars: int = 220) -> list:
    """Tách văn bản thành các đoạn nhỏ dưới max_chars ký tự theo dấu câu"""
    # Thay dấu chấm than, hỏi bằng chấm để dễ tách câu
    normalized = text.replace("!", ".").replace("?", ".")
    raw_sentences = [s.strip() for s in normalized.split(".") if s.strip()]
    
    chunks = []
    current_chunk = ""
    for sentence in raw_sentences:
        # Nếu câu đơn lẻ quá dài (hiếm gặp), tách theo dấu phẩy hoặc chấm phẩy
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
    """Sinh audio cho 1 chunk có retry và delay 0.5s"""
    for attempt in range(1, 4):
        try:
            communicate = edge_tts.Communicate(text=chunk_text, voice=voice, rate=rate)
            await communicate.save(output_path)
            if os.path.exists(output_path) and os.path.getsize(output_path) > 100:
                await asyncio.sleep(0.5)  # Tránh nghẽn server và rate limit
                return True
        except Exception as e:
            await asyncio.sleep(1.0 * attempt)
            
    # Thử gọi qua CLI
    try:
        cmd = ["edge-tts", "--voice", voice, "--rate", rate, "--text", chunk_text, "--write-media", output_path]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode == 0 and os.path.exists(output_path) and os.path.getsize(output_path) > 100:
            await asyncio.sleep(0.5)
            return True
    except Exception:
        pass
        
    return False


async def generate_single_scene_audio(key: str, text: str, output_path: str, voice=DEFAULT_VOICE, rate=SPEECH_RATE):
    """Sinh trọn vẹn 1 file audio cho 1 Scene bằng phương pháp ghép chunk"""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    chunks = split_text_into_chunks(text, max_chars=220)
    
    temp_dir = os.path.join(tempfile.gettempdir(), f"audio_chunks_{key}")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)
    os.makedirs(temp_dir, exist_ok=True)
    
    part_files = []
    print(f"     [Tách {len(chunks)} câu] Đang sinh từng câu với độ trễ 0.5s...")
    for idx, chunk in enumerate(chunks):
        p_path = os.path.join(temp_dir, f"part_{idx:03d}.mp3")
        ok = await generate_chunk_audio(chunk, p_path, voice, rate)
        if not ok:
            print(f"       ⚠️ Thử lại chunk {idx+1}/{len(chunks)}...")
            # Thử lại không rate
            ok = await generate_chunk_audio(chunk, p_path, voice, None)
        part_files.append(p_path)
        
    # Ghép nối bằng ffmpeg concat
    list_file = os.path.join(temp_dir, "parts.txt")
    with open(list_file, "w", encoding="utf-8") as f:
        for p in part_files:
            # Escape path for ffmpeg
            safe_p = p.replace("\\", "/")
            f.write(f"file '{safe_p}'\n")
            
    if os.path.exists(output_path):
        os.remove(output_path)
        
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", output_path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    
    # Dọn dẹp thư mục tạm
    shutil.rmtree(temp_dir, ignore_errors=True)
    return output_path


def get_duration(audio_path: str) -> float:
    """Lấy thời lượng audio chính xác theo giây"""
    if not os.path.exists(audio_path) or os.path.getsize(audio_path) == 0:
        return 0.0
    try:
        audio = MP3(audio_path)
        return float(audio.info.length)
    except Exception:
        return 10.0


def generate_all_lesson_audios(output_dir: str) -> dict:
    """Sinh toàn bộ 5 file audio cho cả 5 phân cảnh bài học"""
    os.makedirs(output_dir, exist_ok=True)
    audio_info = {}
    print("\n🎙️ [VOICEOVER PIPELINE] Bắt đầu sinh giọng đọc AI cho toàn bộ 5 phần bài học:")
    
    for key, data in LESSON_SCRIPTS.items():
        out_file = os.path.join(output_dir, f"{key}_voice.mp3")
        text = data["voice_text"]
        print(f"\n   ▶️ Đang xử lý: {data['title']} (Độ dài: {len(text)} ký tự)...")
        
        asyncio.run(generate_single_scene_audio(key, text, out_file))
        dur = get_duration(out_file)
        print(f"     ✅ Hoàn thành {key}! Thời lượng: {dur:.2f}s ({dur/60:.2f} phút) | Dung lượng: {os.path.getsize(out_file)/1024:.1f} KB")
        audio_info[key] = {
            "path": out_file,
            "duration": dur,
            "title": data["title"]
        }
    
    total_time = sum(item["duration"] for item in audio_info.values())
    print(f"\n🎉 TẤT CẢ 5 FILE AUDIO ĐÃ SẴN SÀNG! Tổng thời lượng: {total_time:.2f}s (~{total_time/60:.2f} phút)")
    return audio_info


if __name__ == "__main__":
    audio_target_dir = os.path.join(os.path.dirname(__file__), "audio")
    generate_all_lesson_audios(audio_target_dir)
