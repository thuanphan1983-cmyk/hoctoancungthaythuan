"""
AUTONOMOUS BATCH PIPELINE: TỰ ĐỘNG TẠO TOÀN BỘ VIDEO BÀI GIẢNG TOÁN 6
Bộ sách: Kết Nối Tri Thức Với Cuộc Sống (Cả Tập 1 và Tập 2)
Tự động chạy liên tục từ Bài 2 đến Bài 43 không dừng lại.
"""

import os
import sys
import json
import shutil
import traceback
import subprocess
import re

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Check if running from root or math_video_pipeline
if os.path.exists(os.path.join(CURRENT_DIR, "math_video_pipeline")):
    PIPELINE_DIR = os.path.join(CURRENT_DIR, "math_video_pipeline")
    ROOT_DIR = CURRENT_DIR
else:
    PIPELINE_DIR = CURRENT_DIR
    ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))

DATA_FILE = os.path.join(PIPELINE_DIR, "data", "curriculum_toan6_full.json")
ERROR_LOG = os.path.join(ROOT_DIR, "error_log.txt")
PUBLIC_VIDEOS = os.path.join(ROOT_DIR, "public", "videos")
DIST_VIDEOS = os.path.join(ROOT_DIR, "dist", "videos")

sys.path.append(PIPELINE_DIR)
from voiceover_engine_batch import generate_lesson_audio
from master_lesson_generator import generate_lesson_package
from scripts.update_curriculum import update_curriculum


def get_video_duration_str(video_path: str) -> str:
    """Đo thời lượng video bằng ffmpeg và trả về mm:ss"""
    try:
        res = subprocess.run(
            ["ffmpeg", "-i", video_path],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            errors="replace"
        )
        m = re.search(r"Duration:\s*(\d{2}):(\d{2}):(\d{2})", res.stderr)
        if m:
            hours, minutes, seconds = int(m.group(1)), int(m.group(2)), int(m.group(3))
            total_minutes = hours * 60 + minutes
            return f"{total_minutes:02d}:{seconds:02d}"
    except Exception:
        pass
    return "14:30"


def git_commit_and_push_chapter(chapter_title: str):
    """Tự động build và push git khi xong 1 chương"""
    print(f"\n🚀 [GIT SYNC] Đã hoàn thành {chapter_title}! Đang build web và đẩy lên GitHub...")
    try:
        subprocess.run("npm run build", shell=True, cwd=ROOT_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        subprocess.run(["git", "add", "-A"], cwd=ROOT_DIR, check=True)
        commit_msg = f"feat(video): complete AI classroom videos for {chapter_title}"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=ROOT_DIR, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=ROOT_DIR, check=True)
        print(f"✅ [GIT SYNC OK] Đã đẩy thành công {chapter_title} lên GitHub!\n")
    except Exception as e:
        print(f"⚠️ [GIT SYNC NOTICE] Bỏ qua git push ({e}), tiếp tục tiến trình pipeline...")


def process_lesson(lesson: dict, index: int, total: int):
    lid = lesson["id"]
    lkey = lesson["lesson_key"]
    ltitle = lesson["lesson_title"]
    vid_name = lesson.get("video_filename", f"Toan6_Bai{lid}_HoanChinh.mp4")
    cid = lesson["chapter_id"]
    ctitle = lesson["chapter_title"]

    lesson_folder = os.path.join(PIPELINE_DIR, "lessons", f"toan6_bai{lid}")
    audio_dir = os.path.join(lesson_folder, "audio")
    os.makedirs(lesson_folder, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)

    print(f"\n[Đang xử lý Bài {index}/{total}: {lkey}]", end="", flush=True)

    # 1. Sinh Audio
    generate_lesson_audio(lesson, audio_dir)
    print(" -> [Audio OK]", end="", flush=True)

    # 2. Sinh mã nguồn Manim Scene
    generate_lesson_package(lesson, lesson_folder)

    # 3. Render Manim Scenes
    # Gọi trực tiếp concat_lesson.py trong lesson_folder
    concat_script = os.path.join(lesson_folder, "concat_lesson.py")
    res = subprocess.run([sys.executable, concat_script], cwd=lesson_folder, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Lỗi render Manim: {res.stderr[-500:]}")
    print(" -> [Render Manim OK]", end="", flush=True)

    # 4. Kiểm tra file video ghép nối hoàn chỉnh
    final_video = os.path.join(lesson_folder, vid_name)
    if not os.path.exists(final_video) or os.path.getsize(final_video) < 50000:
        raise FileNotFoundError(f"Không tìm thấy video đầu ra: {final_video}")
    print(" -> [Ghép nối OK]", end="", flush=True)

    # 5. Sao chép và cập nhật Web
    for d in [PUBLIC_VIDEOS, DIST_VIDEOS]:
        os.makedirs(d, exist_ok=True)
        target = os.path.join(d, vid_name)
        shutil.copy2(final_video, target)

    duration_str = get_video_duration_str(final_video)
    video_url = f"/videos/{vid_name}?v=1"
    desc = f"Tiết học trực quan toàn diện chuẩn sư phạm Bộ GD&ĐT ({duration_str}): (1) Khởi động thực tế, (2) Kiến thức cặn kẽ {ltitle}, (3) 3 Ví dụ đếm ngược 45s làm bài, (4) Cảnh báo lỗi sai, (5) Sơ đồ tư duy tổng kết."
    title = f"Toán 6 - {lkey} (Chuẩn sư phạm 15 phút)"

    update_curriculum(cid, lkey, video_url, title, duration_str, desc)
    print(" -> [Cập nhật Web OK]", flush=True)


def run_pipeline():
    print("=" * 80)
    print("🚀 HỆ THỐNG AUTONOMOUS BATCH PIPELINE TOÀN BỘ TOÁN 6 (KẾT NỐI TRI THỨC)")
    print("   Quy chuẩn: 5 phần sư phạm chuẩn Bộ GD&ĐT (Khởi động, Kiến thức, 3 Ví dụ 45s, Cảnh báo, Sơ đồ)")
    print("=" * 80)

    if not os.path.exists(DATA_FILE):
        print(f"❌ Không tìm thấy file dữ liệu: {DATA_FILE}")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        lessons = json.load(f)

    total_lessons = len(lessons)
    print(f"Tổng số bài học cần sản xuất: {total_lessons} bài.\n")

    current_chapter = None

    for idx, lesson in enumerate(lessons, 1):
        cid = lesson["chapter_id"]
        ctitle = lesson["chapter_title"]

        # Nếu chuyển sang chương mới và đã hoàn thành chương cũ -> Git sync chương cũ
        if current_chapter is not None and cid != current_chapter:
            git_commit_and_push_chapter(current_chapter_title)

        current_chapter = cid
        current_chapter_title = ctitle

        try:
            process_lesson(lesson, idx, total_lessons)
        except Exception as e:
            err_msg = f"[LỖI Bài {lesson.get('id')}: {lesson.get('lesson_key')}] {str(e)}\n{traceback.format_exc()}\n"
            print(f" -> ❌ [LỖI]: {str(e)[:120]}...", flush=True)
            with open(ERROR_LOG, "a", encoding="utf-8") as err_f:
                err_f.write(err_msg + "\n" + "="*50 + "\n")
            print("   -> Đã ghi error_log.txt, tự động chuyển sang bài tiếp theo.")
            continue

    # Commit chương cuối cùng
    if current_chapter is not None:
        git_commit_and_push_chapter(current_chapter_title)

    print("\n" + "=" * 80)
    print("🎉 HOÀN THÀNH TOÀN BỘ PIPELINE SẢN XUẤT VIDEO BÀI GIẢNG TOÁN 6!")
    print("=" * 80)


if __name__ == "__main__":
    run_pipeline()
