"""
CONCAT LESSON PIPELINE & ORCHESTRATOR (14-16 PHÚT)
Bài 2: Cách ghi số tự nhiên (Toán 6 - Kết nối tri thức)
Xuất bản video tiết học hoàn chỉnh: Toan6_Bai2_HoanChinh.mp4
"""

import os
import sys
import glob
import json
import shutil
import tempfile
import subprocess
from mutagen.mp3 import MP3

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(CURRENT_DIR, "audio")
OUTPUT_DIR = os.path.join(CURRENT_DIR, "output_scenes_full")
FINAL_OUTPUT = os.path.join(CURRENT_DIR, "Toan6_Bai2_HoanChinh.mp4")

PUBLIC_VIDEOS = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "..", "public", "videos"))
DIST_VIDEOS = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "..", "dist", "videos"))
GALLERY_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "generated_videos"))

SCENE_DEFS = [
    {
        "id": "scene1",
        "file": "scene1_khoidong.py",
        "class": "Scene1KhoiDong",
        "audio": "scene1_full.mp3",
        "title": "Phần 1: Đặt Vấn Đề & Khởi Động Thực Tế"
    },
    {
        "id": "scene2",
        "file": "scene2_kienthuc.py",
        "class": "Scene2KienThuc",
        "audio": "scene2_full.mp3",
        "title": "Phần 2: Hình Thành Kiến Thức Mới Cặn Kẽ"
    },
    {
        "id": "scene3",
        "file": "scene3_vidu.py",
        "class": "Scene3ViDu",
        "audio": "scene3_full.mp3",
        "title": "Phần 3: Ba Ví Dụ Minh Họa & Đếm Ngược 45s"
    },
    {
        "id": "scene4",
        "file": "scene4_canhbao.py",
        "class": "Scene4CanhBao",
        "audio": "scene4_full.mp3",
        "title": "Phần 4: 4 Lỗi Sai Kinh Điển Khi Làm Bài Thi"
    },
    {
        "id": "scene5",
        "file": "scene5_tongket.py",
        "class": "Scene5TongKet",
        "audio": "scene5_full.mp3",
        "title": "Phần 5: Sơ Đồ Tư Duy Tổng Kết & Dặn Dò BTVN"
    }
]


def render_scene(scene_def: dict, quality_flag: str = "-ql") -> str:
    """Render 1 Scene Manim và lồng ghép audio đồng bộ thành file synced.mp4"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    sc_id = scene_def["id"]
    sc_file = os.path.join(CURRENT_DIR, scene_def["file"])
    sc_class = scene_def["class"]
    sc_audio = os.path.join(AUDIO_DIR, scene_def["audio"])
    synced_output = os.path.join(OUTPUT_DIR, f"{sc_id}_synced.mp4")

    print(f"\n🎬 [RENDER] {scene_def['title']} ({sc_class})...")

    # Dùng thư mục tạm ngắn tránh MAX_PATH trên Windows
    temp_media = os.path.join(tempfile.gettempdir(), f"mnm_{sc_id}")
    if os.path.exists(temp_media):
        shutil.rmtree(temp_media, ignore_errors=True)
    os.makedirs(temp_media, exist_ok=True)

    cmd = [
        "manim",
        quality_flag,
        sc_file,
        sc_class,
        "--media_dir", temp_media
    ]

    print(f"   Command: {' '.join(cmd)}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        print(f"   ❌ Lỗi Manim render {sc_id} (code {res.returncode}):\n{res.stderr[-500:]}")
        raise RuntimeError(f"Manim render failed for {sc_id}")

    # Tìm file mp4 đã xuất ra
    mp4_files = glob.glob(os.path.join(temp_media, "**", f"{sc_class}.mp4"), recursive=True)
    if not mp4_files:
        mp4_files = glob.glob(os.path.join(temp_media, "**", "*.mp4"), recursive=True)
        mp4_files = [f for f in mp4_files if "partial_movie_files" not in f]

    if not mp4_files:
        raise FileNotFoundError(f"Không tìm thấy file mp4 sau khi render {sc_class} tại {temp_media}")

    raw_video = mp4_files[0]
    print(f"   -> Video gốc: {raw_video} ({os.path.getsize(raw_video)/1024:.1f} KB)")

    # Ghép audio vào video bằng ffmpeg
    if os.path.exists(synced_output):
        os.remove(synced_output)

    print(f"   -> Đang lồng ghép audio: {os.path.basename(sc_audio)}...")
    mux_cmd = [
        "ffmpeg", "-y",
        "-i", raw_video,
        "-i", sc_audio,
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        synced_output
    ]
    mux_res = subprocess.run(mux_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if mux_res.returncode != 0 or not os.path.exists(synced_output):
        mux_cmd = [
            "ffmpeg", "-y",
            "-i", raw_video,
            "-i", sc_audio,
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-shortest",
            synced_output
        ]
        subprocess.run(mux_cmd, check=True)

    print(f"   ✅ Đã tạo video phân cảnh hoàn chỉnh: {os.path.basename(synced_output)} ({os.path.getsize(synced_output)/1024:.1f} KB)")
    shutil.rmtree(temp_media, ignore_errors=True)
    return synced_output


def concat_all_scenes(synced_files: list) -> str:
    """Ghép nối 5 phân cảnh thành video bài giảng hoàn chỉnh 14-16 phút"""
    print("\n🎞️ [CONCAT PIPELINE] Bắt đầu ghép nối 5 phân cảnh bài học...")
    os.makedirs(os.path.dirname(FINAL_OUTPUT), exist_ok=True)
    
    list_file = os.path.join(OUTPUT_DIR, "concat_list.txt")
    with open(list_file, "w", encoding="utf-8") as f:
        for p in synced_files:
            safe_p = p.replace("\\", "/")
            f.write(f"file '{safe_p}'\n")

    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", list_file,
        "-c", "copy",
        FINAL_OUTPUT
    ]
    res = subprocess.run(concat_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0 or not os.path.exists(FINAL_OUTPUT) or os.path.getsize(FINAL_OUTPUT) == 0:
        print("   ⚠️ Concat copy không thành công, chuyển sang encode lại stream...")
        concat_cmd = [
            "ffmpeg", "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", list_file,
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            FINAL_OUTPUT
        ]
        subprocess.run(concat_cmd, check=True)

    final_size_mb = os.path.getsize(FINAL_OUTPUT) / (1024 * 1024)
    print(f"\n🎉 HOÀN THÀNH XUẤT BẢN BÀI GIẢNG TOÀN DIỆN BÀI 2!")
    print(f"   📁 Tệp đầu ra: {FINAL_OUTPUT}")
    print(f"   📦 Dung lượng: {final_size_mb:.2f} MB")

    # Đo thời lượng thực tế
    try:
        dur_sec = float(MP3(FINAL_OUTPUT).info.length)
    except Exception:
        # Dùng ffprobe
        probe_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", FINAL_OUTPUT]
        probe_res = subprocess.run(probe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        dur_sec = float(probe_res.stdout.strip()) if probe_res.stdout.strip() else 0.0

    mins = int(dur_sec // 60)
    secs = int(dur_sec % 60)
    print(f"   ⏱️ Thời lượng video: {mins:02d}:{secs:02d} ({dur_sec:.1f} giây)")

    # Sao chép vào public/videos và dist/videos
    for dest_dir in [PUBLIC_VIDEOS, DIST_VIDEOS, GALLERY_DIR]:
        if os.path.exists(dest_dir):
            target_file = os.path.join(dest_dir, "Toan6_Bai2_HoanChinh.mp4")
            shutil.copy2(FINAL_OUTPUT, target_file)
            print(f"   🚀 Đã sao chép vào: {target_file}")
            # Thêm alias Toan6_TietDay_Bai2_Full15m.mp4
            alias_file = os.path.join(dest_dir, "Toan6_TietDay_Bai2_Full15m.mp4")
            shutil.copy2(FINAL_OUTPUT, alias_file)

    return FINAL_OUTPUT


def run_pipeline(quality_flag: str = "-ql"):
    print("=" * 70)
    print("   HỆ THỐNG XUẤT BẢN BÀI GIẢNG TOÀN DIỆN BÀI 2 (14-16 PHÚT)")
    print(f"   Chất lượng render: {quality_flag}")
    print("=" * 70)

    synced_scenes = []
    for sc in SCENE_DEFS:
        synced_path = render_scene(sc, quality_flag)
        synced_scenes.append(synced_path)

    concat_all_scenes(synced_scenes)


if __name__ == "__main__":
    q_flag = "-ql"
    if len(sys.argv) > 1:
        q_flag = sys.argv[1]
    run_pipeline(q_flag)
