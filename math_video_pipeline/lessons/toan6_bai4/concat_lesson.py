"""
CONCAT LESSON PIPELINE CHO BÀI 4: Phép cộng và phép trừ số tự nhiên
"""

import os
import sys
import glob
import shutil
import tempfile
import subprocess

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(CURRENT_DIR, "audio")
OUTPUT_DIR = os.path.join(CURRENT_DIR, "output_scenes_full")
FINAL_OUTPUT = os.path.join(CURRENT_DIR, "Toan6_Bai4_HoanChinh.mp4")

PUBLIC_VIDEOS = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "..", "public", "videos"))
DIST_VIDEOS = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "..", "dist", "videos"))

SCENE_DEFS = [
    {"id": "scene1", "file": "scene1_khoidong.py", "class": "Scene1KhoiDong", "audio": "scene1_full.mp3"},
    {"id": "scene2", "file": "scene2_kienthuc.py", "class": "Scene2KienThuc", "audio": "scene2_full.mp3"},
    {"id": "scene3", "file": "scene3_vidu.py", "class": "Scene3ViDu", "audio": "scene3_full.mp3"},
    {"id": "scene4", "file": "scene4_canhbao.py", "class": "Scene4CanhBao", "audio": "scene4_full.mp3"},
    {"id": "scene5", "file": "scene5_tongket.py", "class": "Scene5TongKet", "audio": "scene5_full.mp3"}
]

def render_scene(sc_def, quality_flag="-ql"):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    sc_id = sc_def["id"]
    sc_file = os.path.join(CURRENT_DIR, sc_def["file"])
    sc_class = sc_def["class"]
    sc_audio = os.path.join(AUDIO_DIR, sc_def["audio"])
    synced_output = os.path.join(OUTPUT_DIR, f"{sc_id}_synced.mp4")

    temp_media = os.path.join(tempfile.gettempdir(), f"mnm_{sc_id}_4")
    if os.path.exists(temp_media):
        shutil.rmtree(temp_media, ignore_errors=True)
    os.makedirs(temp_media, exist_ok=True)

    cmd = ["manim", quality_flag, sc_file, sc_class, "--media_dir", temp_media]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        raise RuntimeError(f"Manim render failed for {sc_class}: {res.stderr[-400:]}")

    mp4_files = glob.glob(os.path.join(temp_media, "**", f"{sc_class}.mp4"), recursive=True)
    if not mp4_files:
        mp4_files = [f for f in glob.glob(os.path.join(temp_media, "**", "*.mp4"), recursive=True) if "partial_movie_files" not in f]
    if not mp4_files:
        raise FileNotFoundError(f"No mp4 found for {sc_class}")
    raw_video = mp4_files[0]

    if os.path.exists(synced_output):
        os.remove(synced_output)

    mux_cmd = ["ffmpeg", "-y", "-i", raw_video, "-i", sc_audio, "-c:v", "copy", "-c:a", "aac", "-shortest", synced_output]
    mux_res = subprocess.run(mux_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if mux_res.returncode != 0 or not os.path.exists(synced_output):
        mux_cmd = ["ffmpeg", "-y", "-i", raw_video, "-i", sc_audio, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", synced_output]
        subprocess.run(mux_cmd, check=True)

    shutil.rmtree(temp_media, ignore_errors=True)
    return synced_output


def concat_scenes(synced_files):
    os.makedirs(os.path.dirname(FINAL_OUTPUT), exist_ok=True)
    list_file = os.path.join(OUTPUT_DIR, "concat_list.txt")
    with open(list_file, "w", encoding="utf-8") as f:
        for p in synced_files:
            safe_p = p.replace("\\", "/")
            f.write(f"file '{safe_p}'\n")

    concat_cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", FINAL_OUTPUT]
    res = subprocess.run(concat_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0 or not os.path.exists(FINAL_OUTPUT) or os.path.getsize(FINAL_OUTPUT) == 0:
        concat_cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", FINAL_OUTPUT]
        subprocess.run(concat_cmd, check=True)

    for d in [PUBLIC_VIDEOS, DIST_VIDEOS]:
        os.makedirs(d, exist_ok=True)
        target = os.path.join(d, "Toan6_Bai4_HoanChinh.mp4")
        shutil.copy2(FINAL_OUTPUT, target)

    return FINAL_OUTPUT


def run():
    synced = []
    for sc in SCENE_DEFS:
        synced.append(render_scene(sc))
    out = concat_scenes(synced)
    print("DONE:", out)


if __name__ == "__main__":
    run()
