"""
SYNC ENGINE (ĐỒNG BỘ HÓA HÌNH ẢNH & GIỌNG NÓI AI)
Ghép nối video Manim và audio thuyết minh Edge-TTS
Sử dụng FFmpeg tối ưu tốc độ xử lý (Stream Copy / AAC Encoding)
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def get_ffmpeg_path():
    """Lấy đường dẫn ffmpeg khả dụng nhất"""
    # 1. Thử trong PATH
    which_ffmpeg = shutil.which("ffmpeg")
    if which_ffmpeg:
        return which_ffmpeg

    # 2. Thử từ imageio_ffmpeg
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        pass

    # 3. Thử thư mục Python Scripts
    scripts_dir = os.path.dirname(shutil.which("pip") or "")
    candidate = os.path.join(scripts_dir, "ffmpeg.exe")
    if os.path.exists(candidate):
        return candidate

    return "ffmpeg"


class SyncEngine:
    def __init__(self, temp_dir="temp", output_dir="generated_videos"):
        self.temp_dir = os.path.abspath(temp_dir)
        self.output_dir = os.path.abspath(output_dir)
        self.ffmpeg = get_ffmpeg_path()
        os.makedirs(self.temp_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def mux_scene_video_audio(self, video_path: str, audio_path: str, output_path: str) -> str:
        """Ghép video manim và audio thuyết minh thành phân cảnh hoàn chỉnh"""
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Không tìm thấy video phân cảnh: {video_path}")
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Không tìm thấy audio phân cảnh: {audio_path}")

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

        # Lệnh ffmpeg ghép video và audio chuẩn xác:
        # -c:v copy: Giữ nguyên khung hình 1080p manim, siêu tốc độ không encode lại
        # -c:a aac: Mã hóa âm thanh chuẩn AAC 192k tương thích mọi thiết bị và trình duyệt
        cmd = [
            self.ffmpeg, "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            output_path
        ]

        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
        if res.returncode != 0:
            # Fallback nếu copy bị lỗi timestamp: encode lại video ngắn
            cmd_fallback = [
                self.ffmpeg, "-y",
                "-i", video_path,
                "-i", audio_path,
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                "-c:a", "aac",
                "-b:a", "192k",
                "-shortest",
                output_path
            ]
            res_fb = subprocess.run(cmd_fallback, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
            if res_fb.returncode != 0:
                raise RuntimeError(f"Lỗi FFmpeg khi ghép audio/video:\n{res_fb.stderr}")

        return output_path

    def concatenate_scenes(self, scene_video_list: list, final_output_path: str) -> str:
        """Nối tất cả các phân cảnh thành 1 video bài học trọn vẹn duy nhất"""
        if not scene_video_list:
            raise ValueError("Danh sách video phân cảnh rỗng!")

        os.makedirs(os.path.dirname(os.path.abspath(final_output_path)), exist_ok=True)

        # Tạo file danh sách nối (concat list) cho ffmpeg
        concat_txt = os.path.join(self.temp_dir, "concat_scenes.txt")
        with open(concat_txt, "w", encoding="utf-8") as f:
            for s_path in scene_video_list:
                # Format an toàn đường dẫn cho ffmpeg
                p_safe = s_path.replace("\\", "/")
                f.write(f"file '{p_safe}'\n")

        cmd = [
            self.ffmpeg, "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", concat_txt,
            "-c", "copy",
            final_output_path
        ]

        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
        if res.returncode != 0:
            # Fallback re-encode nếu ghép trực tiếp không khớp codecs
            cmd_reencode = [
                self.ffmpeg, "-y",
                "-f", "concat",
                "-safe", "0",
                "-i", concat_txt,
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                "-c:a", "aac",
                "-b:a", "192k",
                final_output_path
            ]
            res_re = subprocess.run(cmd_reencode, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
            if res_re.returncode != 0:
                raise RuntimeError(f"Lỗi FFmpeg khi nối các phân cảnh:\n{res_re.stderr}")

        return final_output_path


if __name__ == "__main__":
    sync = SyncEngine()
    print("SyncEngine đã sẵn sàng với FFmpeg:", sync.ffmpeg)
