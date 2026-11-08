#!/usr/bin/env python3
"""
==============================================================================
AI MATH VISUAL VIDEO PIPELINE - TOÀN DIỆN & TỰ ĐỘNG HÓA 100%
Tự động tạo video bài giảng toán học trực quan từ kịch bản SGK Kết nối tri thức
Tác giả: Thầy Thuấn Phan • Hệ thống Antigravity AI
==============================================================================
"""

import os
import sys
import json
import time
import shutil
import argparse
import subprocess
from pathlib import Path

# Đảm bảo in tiếng Việt chuẩn trong console Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Import các engine con
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from voiceover_engine import VoiceoverEngine
from sync_engine import SyncEngine, get_ffmpeg_path

# Mapping giữa type trong json và tên Class trong animation_engine.py
SCENE_CLASS_MAPPING = {
    "intro": "IntroScene",
    "venn_diagram": "VennDiagramScene",
    "summary": "SummaryScene",
    "geometry_shapes": "GeometryShapesScene"
}


def load_config(config_path: str) -> dict:
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Không tìm thấy file cấu hình: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def render_manim_scene(scene_name: str, audio_duration: float, scene_cfg: dict, quality: str, temp_dir: str) -> str:
    """Gọi Manim CLI để render phân cảnh đồ họa tương ứng (tối ưu đường dẫn ngắn tránh giới hạn MAX_PATH của Windows)"""
    import tempfile
    
    # 1. Tạo 1 file wrapper ngắn để tránh vượt quá 260 ký tự đường dẫn Windows
    wrapper_path = os.path.join(temp_dir, "run_sc.py")
    scene_cfg_json = json.dumps(scene_cfg, ensure_ascii=False).replace("\\", "\\\\").replace('"', '\\"')

    wrapper_code = f"""import sys
import json
sys.path.insert(0, r"{SCRIPT_DIR}")
import animation_engine
from manim import *

class RunScene(animation_engine.{scene_name}):
    audio_duration = {audio_duration}
    scene_config = json.loads("{scene_cfg_json}")
"""
    with open(wrapper_path, "w", encoding="utf-8") as f:
        f.write(wrapper_code)

    # 2. Dùng thư mục Temp hệ thống ngắn (khoảng 40 ký tự) cho media_dir
    media_dir = os.path.join(tempfile.gettempdir(), "mnm")
    os.makedirs(media_dir, exist_ok=True)

    quality_flag = f"-q{quality}"
    cmd = [
        "manim",
        quality_flag,
        "--media_dir", media_dir,
        wrapper_path,
        "RunScene"
    ]

    print(f"      [Manim] Bắt đầu kết xuất đồ họa '{scene_name}' ({quality_flag})...")
    t0 = time.time()
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
    t_render = time.time() - t0

    if res.returncode != 0:
        print("Lỗi Manim:", res.stderr)
        raise RuntimeError(f"Lỗi khi render Manim scene {scene_name}:\n{res.stderr}")

    # Tìm file mp4 đã kết xuất
    rendered_files = list(Path(media_dir).rglob("RunScene.mp4"))
    if not rendered_files:
        raise FileNotFoundError(f"Không tìm thấy video output của RunScene trong {media_dir}")

    # Lấy file mới nhất
    rendered_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    out_file = str(rendered_files[0])
    print(f"      -> Hoàn thành đồ họa ({t_render:.1f}s)! File: {os.path.basename(out_file)}")
    return out_file


def process_lesson(lesson: dict, quality="m", override_voice=None, temp_root="temp", output_dir="generated_videos") -> str:
    """Xử lý trọn gói 1 bài học từ kịch bản -> video AI hoàn chỉnh"""
    lesson_id = lesson["id"]
    lesson_title = lesson["lesson_title"]
    output_filename = lesson.get("output_filename", f"{lesson_id}.mp4")
    voice = override_voice or lesson.get("voice", "vi-VN-NamMinhNeural")
    speech_rate = lesson.get("speech_rate", "+0%")
    scenes = lesson.get("scenes", [])

    print("\n" + "=" * 70)
    print(f"🎬 BẮT ĐẦU TẠO VIDEO TOÁN HỌC AI CHO BÀI:")
    print(f"   📖 {lesson_title}")
    print(f"   🏷️ Khối lớp: {lesson.get('grade')} | Bộ sách: {lesson.get('chapter', '')}")
    print(f"   🗣️ Giọng đọc AI: {voice} | Chất lượng xuất: 1080p/HD (-q{quality})")
    print("=" * 70)

    lesson_temp_dir = os.path.join(temp_root, lesson_id)
    os.makedirs(lesson_temp_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # 1. BƯỚC 1: SINH TOÀN BỘ GIỌNG NÓI THUYẾT MINH AI (VOICEOVER)
    voice_engine = VoiceoverEngine(voice=voice, rate=speech_rate)
    audio_map = voice_engine.generate_lesson_voiceovers(lesson, lesson_temp_dir)

    # 2. BƯỚC 2: KẾT XUẤT ĐỒ HỌA HOẠT CẢNH & KHỚP TỪNG PHÂN ĐOẠN
    sync_engine = SyncEngine(temp_dir=lesson_temp_dir, output_dir=output_dir)
    synced_scene_videos = []

    print(f"\n🎨 [ANIMATION & SYNC] Bắt đầu vẽ đồ họa toán học khớp thời lượng...")
    for idx, sc in enumerate(scenes, 1):
        sc_id = sc.get("scene_id", f"scene_{idx}")
        sc_type = sc.get("type")
        class_name = SCENE_CLASS_MAPPING.get(sc_type)

        if not class_name:
            print(f"   [Cảnh báo] Bỏ qua phân cảnh {sc_id}: Không tìm thấy class ánh xạ cho type '{sc_type}'")
            continue

        audio_info = audio_map.get(sc_id)
        if not audio_info:
            print(f"   [Cảnh báo] Bỏ qua phân cảnh {sc_id}: Không có audio")
            continue

        audio_file = audio_info["file_path"]
        audio_dur = audio_info["duration"]

        print(f"\n   [{idx}/{len(scenes)}] Phân cảnh: '{sc_id}' (Lớp đồ họa: {class_name}) | Thời lượng: {audio_dur:.2f}s")
        # Kết xuất video Manim
        video_raw = render_manim_scene(
            scene_name=class_name,
            audio_duration=audio_dur,
            scene_cfg=sc,
            quality=quality,
            temp_dir=lesson_temp_dir
        )

        # Ghép audio vào video phân cảnh
        synced_scene_path = os.path.join(lesson_temp_dir, f"synced_{sc_id}.mp4")
        print(f"      [Sync] Ghép thuyết minh audio vào video phân cảnh...")
        sync_engine.mux_scene_video_audio(video_raw, audio_file, synced_scene_path)
        synced_scene_videos.append(synced_scene_path)

    # 3. BƯỚC 3: NỐI TẤT CẢ CÁC PHÂN CẢNH THÀNH VIDEO BÀI GIẢNG TRỌN VẸN
    print(f"\n🎞️ [FINAL RENDER] Nối toàn bộ {len(synced_scene_videos)} phân cảnh thành video bài giảng hoàn chỉnh...")
    final_output_path = os.path.join(output_dir, output_filename)
    sync_engine.concatenate_scenes(synced_scene_videos, final_output_path)

    # Đo thời lượng và dung lượng file cuối cùng
    file_size_mb = os.path.getsize(final_output_path) / (1024 * 1024)
    total_duration = sum(audio_map[sc["scene_id"]]["duration"] for sc in scenes if sc["scene_id"] in audio_map)

    print("\n" + "★" * 70)
    print(f"🎉 XUẤT BẢN THÀNH CÔNG VIDEO TOÁN HỌC TRỰC QUAN AI!")
    print(f"   📁 Tệp video hoàn chỉnh: {final_output_path}")
    print(f"   ⏱️ Tổng thời lượng bài giảng: {total_duration:.1f} giây")
    print(f"   💾 Dung lượng tệp: {file_size_mb:.2f} MB")
    print(f"   🚀 Sẵn sàng xem thử, nhúng vào website hoặc xuất bản lên mạng xã hội!")
    print("★" * 70)

    return final_output_path


def main():
    parser = argparse.ArgumentParser(description="Hệ thống tạo video bài giảng toán học trực quan tự động bằng AI.")
    parser.add_argument("--config", default=os.path.join(SCRIPT_DIR, "config", "lessons_config.json"), help="Đường dẫn file cấu hình lessons_config.json")
    parser.add_argument("--lesson", default="toan6_bai1", help="Mã bài học cần tạo (Ví dụ: toan6_bai1 hoặc 'all')")
    parser.add_argument("--quality", default="m", choices=["l", "m", "h", "k"], help="Chất lượng kết xuất: l (480p), m (720p - mặc định), h (1080p)")
    parser.add_argument("--voice", default=None, help="Ghi đè giọng đọc (vi-VN-NamMinhNeural hoặc vi-VN-HoaiMyNeural)")
    parser.add_argument("--list", action="store_true", help="Liệt kê danh sách các bài học hiện có trong file config")
    parser.add_argument("--clean-temp", action="store_true", help="Xóa thư mục tạm temp/ sau khi hoàn tất")
    args = parser.parse_args()

    data = load_config(args.config)
    lessons = data.get("lessons", [])

    if args.list:
        print("\n📋 DANH SÁCH BÀI HỌC CÓ SẴN TRONG HỆ THỐNG:")
        print("-" * 75)
        for idx, l in enumerate(lessons, 1):
            print(f" {idx}. [{l['id']}] {l['grade']} - {l['lesson_title']} ({len(l['scenes'])} phân cảnh)")
        print("-" * 75)
        return

    # Lọc bài học theo tham số
    target_lessons = []
    if args.lesson.lower() == "all":
        target_lessons = lessons
    else:
        target_lessons = [l for l in lessons if l["id"] == args.lesson]
        if not target_lessons:
            print(f"❌ Không tìm thấy bài học có mã: '{args.lesson}'. Dùng lệnh --list để xem danh sách.")
            sys.exit(1)

    temp_root = os.path.join(SCRIPT_DIR, "temp")
    output_dir = os.path.join(SCRIPT_DIR, "generated_videos")

    for l in target_lessons:
        process_lesson(
            lesson=l,
            quality=args.quality,
            override_voice=args.voice,
            temp_root=temp_root,
            output_dir=output_dir
        )

    if args.clean_temp and os.path.exists(temp_root):
        shutil.rmtree(temp_root)
        print("🧹 Đã dọn dẹp sạch thư mục tạm temp/.")


if __name__ == "__main__":
    main()
