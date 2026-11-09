"""
CONCAT LESSON PIPELINE CHO BÀI 3: Thứ tự trong tập hợp các số tự nhiên
Khớp 1:1 từng mili-giây giữa Video Manim và Audio Thuyết Minh
"""

import os
import sys
import glob
import shutil
import tempfile
import subprocess
import re
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
FINAL_OUTPUT = os.path.join(CURRENT_DIR, "Toan6_Bai3_HoanChinh.mp4")
PUBLIC_VIDEOS = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "..", "public", "videos"))
DIST_VIDEOS = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "..", "dist", "videos"))

os.makedirs(OUTPUT_DIR, exist_ok=True)

SCENE_DEFS = [
    {"py": "scene1_khoidong.py", "scene": "Scene1KhoiDong", "audio": "scene1_full.mp3", "out": "scene1_synced.mp4"},
    {"py": "scene2_kienthuc.py", "scene": "Scene2KienThuc", "audio": "scene2_full.mp3", "out": "scene2_synced.mp4"},
    {"py": "scene3_vidu.py",     "scene": "Scene3ViDu",     "audio": "scene3_full.mp3", "out": "scene3_synced.mp4"},
    {"py": "scene4_canhbao.py",  "scene": "Scene4CanhBao",  "audio": "scene4_full.mp3", "out": "scene4_synced.mp4"},
    {"py": "scene5_tongket.py",  "scene": "Scene5TongKet",  "audio": "scene5_full.mp3", "out": "scene5_synced.mp4"},
]


def render_scene(sc_def, quality_flag="-ql"):
    py_file = os.path.join(CURRENT_DIR, sc_def["py"])
    scene_name = sc_def["scene"]
    audio_file = os.path.join(AUDIO_DIR, sc_def["audio"])
    if not os.path.exists(audio_file):
        alt_audio = os.path.join(AUDIO_DIR, sc_def["audio"].replace("_full.mp3", "_voice.mp3"))
        if os.path.exists(alt_audio):
            audio_file = alt_audio
    out_synced = os.path.join(OUTPUT_DIR, sc_def["out"])

    print(f"\n[RENDER] Dang render", py_file, "->", scene_name, quality_flag, "...")
    res = subprocess.run(["manim", quality_flag, py_file, scene_name], cwd=CURRENT_DIR)
    if res.returncode != 0:
        raise RuntimeError("Loi render manim: " + scene_name)

    v_pattern = os.path.join(CURRENT_DIR, "media", "videos", sc_def["py"].replace(".py", ""), "*", scene_name + ".mp4")
    v_matches = glob.glob(v_pattern)
    if not v_matches:
        raise FileNotFoundError("Khong tim thay video render: " + v_pattern)

    raw_video = v_matches[0]
    print("  -> Video raw:", raw_video)

    if os.path.exists(audio_file):
        a_len = float(MP3(audio_file).info.length)
        print("  -> Audio:", audio_file, "(" + str(round(a_len, 2)) + "s)")
        cmd = [
            "ffmpeg", "-y",
            "-i", raw_video,
            "-i", audio_file,
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-t", str(a_len),
            "-movflags", "+faststart",
            out_synced
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0:
            raise RuntimeError("Loi ghep audio: " + str(res.stderr))
    else:
        shutil.copy2(raw_video, out_synced)

    return out_synced


def concat_scenes(synced_files):
    print("\n[CONCAT] Dang ghep noi", len(synced_files), "scenes...")
    list_txt = os.path.join(OUTPUT_DIR, "concat_list.txt")
    with open(list_txt, "w", encoding="utf-8") as f:
        for sf in synced_files:
            clean_p = sf.replace("\\", "/")
            f.write("file '" + clean_p + "'\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", list_txt,
        "-c", "copy",
        "-movflags", "+faststart",
        FINAL_OUTPUT
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0:
        raise RuntimeError("Loi concat: " + str(res.stderr))

    dur_str = "00:00"
    try:
        chk = subprocess.run(["ffmpeg", "-i", FINAL_OUTPUT], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors="replace")
        m = re.search(r"Duration:\s*(\d+):(\d+):([0-9.]+)", chk.stderr)
        if m:
            mins = int(m.group(1)) * 60 + int(m.group(2))
            secs = int(float(m.group(3)))
            dur_str = "%02d:%02d" % (mins, secs)
    except Exception:
        pass

    size_mb = os.path.getsize(FINAL_OUTPUT) / (1024 * 1024)
    print("\n=======================================================")
    print("🎉 XUAT BAN THANH CONG:", FINAL_OUTPUT)
    print("   Thoi luong:", dur_str, "| Dung luong: %.2f MB" % size_mb)
    print("=======================================================")

    for pub_dir in [PUBLIC_VIDEOS, DIST_VIDEOS]:
        if os.path.exists(pub_dir):
            try:
                dest = os.path.join(pub_dir, os.path.basename(FINAL_OUTPUT))
                shutil.copy2(FINAL_OUTPUT, dest)
                print("   -> Da copy sang:", dest)
            except Exception as e:
                print("   -> Canh bao copy", pub_dir, ":", e)

    return FINAL_OUTPUT


def run(quality_flag="-ql"):
    synced = []
    for sc in SCENE_DEFS:
        synced.append(render_scene(sc, quality_flag))
    out = concat_scenes(synced)
    print("DONE:", out)


if __name__ == "__main__":
    q_flag = "-ql"
    if len(sys.argv) > 1:
        q_flag = sys.argv[1]
    run(q_flag)
