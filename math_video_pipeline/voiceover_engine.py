"""
VOICEOVER ENGINE (TẠO GIỌNG NÓI THUYẾT MINH AI)
Học toán cùng thầy Thuấn Phan - Chuẩn ngữ điệu sư phạm tiếng Việt
Sử dụng Microsoft Edge TTS Neural Voices (vi-VN-NamMinhNeural / vi-VN-HoaiMyNeural)
"""

import os
import sys
import asyncio
import subprocess
from pathlib import Path
import edge_tts
from mutagen.mp3 import MP3

DEFAULT_VOICE = "vi-VN-NamMinhNeural"
BACKUP_VOICE = "vi-VN-HoaiMyNeural"


class VoiceoverEngine:
    def __init__(self, voice=DEFAULT_VOICE, rate=None, pitch=None):
        self.voice = voice or DEFAULT_VOICE
        self.rate = rate if (rate and rate != "+0%") else None
        self.pitch = pitch if (pitch and pitch != "+0Hz") else None

    async def _generate_async(self, text: str, output_path: str) -> str:
        """Sinh file mp3 từ văn bản tiếng Việt bất đồng bộ"""
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        kwargs = {"text": text, "voice": self.voice}
        if self.rate:
            kwargs["rate"] = self.rate
        if self.pitch:
            kwargs["pitch"] = self.pitch

        communicate = edge_tts.Communicate(**kwargs)
        await communicate.save(output_path)
        return output_path

    def generate_speech(self, text: str, output_path: str) -> str:
        """Hàm đồng bộ sinh file audio thuyết minh từ văn bản, có retry và fallback"""
        text = text.strip()
        if not text:
            raise ValueError("Văn bản thuyết minh không được để trống!")

        import time

        for attempt in range(1, 4):
            # 1. Thử sinh bằng thư viện edge-tts trực tiếp
            try:
                asyncio.run(self._generate_async(text, output_path))
                if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                    time.sleep(0.5)  # Tránh gửi request quá dồn dập
                    return output_path
            except Exception as e:
                pass

            # 2. Thử gọi qua CLI
            cmd = ["edge-tts", "--voice", self.voice, "--text", text, "--write-media", output_path]
            if self.rate:
                cmd.extend(["--rate", self.rate])
            if self.pitch:
                cmd.extend(["--pitch", self.pitch])

            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
            if res.returncode == 0 and os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                time.sleep(0.5)
                return output_path

            # 3. Thử với giọng nữ Hoài My
            if self.voice != BACKUP_VOICE:
                cmd[2] = BACKUP_VOICE
                subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
                if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                    time.sleep(0.5)
                    return output_path

            time.sleep(1.2 * attempt)

        raise RuntimeError(f"Lỗi: Không tạo được file audio thuyết minh tại {output_path}")

    @staticmethod
    def get_audio_duration(audio_path: str) -> float:
        """Đo thời lượng chính xác của file audio theo giây (độ chính xác mili-giây)"""
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"File audio không tồn tại: {audio_path}")

        try:
            audio = MP3(audio_path)
            return float(audio.info.length)
        except Exception:
            pass

        # Phương án dự phòng: Dùng ffmpeg
        try:
            import imageio_ffmpeg
            ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
            cmd = [ffmpeg_exe, "-i", audio_path, "-f", "null", "-"]
            res = subprocess.run(cmd, stderr=subprocess.PIPE, encoding="utf-8", errors="replace", timeout=10)
            for line in res.stderr.split("\n"):
                if "Duration:" in line:
                    time_str = line.split("Duration:")[1].split(",")[0].strip()
                    parts = time_str.split(":")
                    secs = float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
                    return secs
        except Exception as e:
            print(f"[Cảnh báo] Không thể đo thời lượng qua ffmpeg: {e}")

        return 5.0

    def generate_lesson_voiceovers(self, lesson_config: dict, temp_dir: str) -> dict:
        """Sinh toàn bộ audio cho tất cả các phân cảnh (scenes) trong 1 bài học"""
        os.makedirs(temp_dir, exist_ok=True)
        audio_map = {}
        scenes = lesson_config.get("scenes", [])
        lesson_id = lesson_config.get("id", "lesson")

        print(f"\n🎙️ [VOICEOVER] Bắt đầu sinh giọng đọc AI cho bài: {lesson_config.get('lesson_title')}")
        print(f"   - Giọng đọc: {self.voice} | Tốc độ: {self.rate or 'Mặc định'}")

        for idx, sc in enumerate(scenes, 1):
            sc_id = sc.get("scene_id", f"scene_{idx}")
            voice_text = sc.get("voiceover", "").strip()
            if not voice_text:
                continue

            audio_file = os.path.join(temp_dir, f"{lesson_id}_{sc_id}.mp3")
            print(f"   [{idx}/{len(scenes)}] Sinh audio: Phân cảnh '{sc_id}' ({len(voice_text)} ký tự)...")
            self.generate_speech(voice_text, audio_file)
            dur = self.get_audio_duration(audio_file)
            print(f"       -> Xong! Thời lượng: {dur:.2f}s | Lưu: {os.path.basename(audio_file)}")

            audio_map[sc_id] = {
                "file_path": audio_file,
                "duration": dur,
                "text": voice_text
            }

        return audio_map


if __name__ == "__main__":
    engine = VoiceoverEngine()
    test_out = "test_voiceover.mp3"
    engine.generate_speech(
        "Chào mừng các em học sinh đến với chuỗi bài giảng trực quan môn Toán cùng thầy Thuấn Phan!",
        test_out
    )
    duration = engine.get_audio_duration(test_out)
    print(f"✅ Kiểm thử thành công! File: {test_out}, Thời lượng: {duration:.2f}s")
    if os.path.exists(test_out):
        os.remove(test_out)
