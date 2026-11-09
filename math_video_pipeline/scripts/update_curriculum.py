"""
CẬP NHẬT ĐƯỜNG DẪN VIDEO BÀI HỌC VÀO CURRICULUM.JS VÀ PUBLIC/CURRICULUM.JS
"""

import os
import sys
import re
import json

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))

CURRICULUM_FILES = [
    os.path.join(PROJECT_ROOT, "curriculum.js"),
    os.path.join(PROJECT_ROOT, "public", "curriculum.js"),
    os.path.join(PROJECT_ROOT, "index.html")
]


def update_curriculum(chapter_id: str, lesson_key: str, video_url: str, title: str, duration: str, description: str):
    new_entry_obj = {
        "type": "ai_video",
        "videoUrl": video_url,
        "title": title,
        "channel": "Học Toán Cùng Thầy Thuấn Phan • AI Animation",
        "duration": duration,
        "badge": "✨ BÀI GIẢNG TOÀN DIỆN 15 PHÚT THẦY THUẤN",
        "description": description
    }
    new_entry_str = json.dumps(new_entry_obj, ensure_ascii=False, indent=6)

    formatted_block = f'"{lesson_key}": {new_entry_str}'

    for fpath in CURRICULUM_FILES:
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Kiểm tra xem lesson_key đã có trong lessonVideos chưa
        key_escaped = re.escape(f'"{lesson_key}":')
        pattern = re.compile(rf'{key_escaped}\s*\{{[\s\S]*?\n\s*\}}(,)?', re.MULTILINE)

        if pattern.search(content):
            # Đã tồn tại -> Thay thế
            content = pattern.sub(formatted_block + r"\1", content, count=1)
        else:
            # Chưa tồn tại trong lessonVideos -> Chèn vào sau lessonVideos: { của chương đó
            ch_pattern = re.compile(rf'id:\s*"{re.escape(chapter_id)}"[^}}]*?lessonVideos:\s*\{{', re.DOTALL)
            m = ch_pattern.search(content)
            if m:
                insert_pos = m.end()
                content = content[:insert_pos] + "\n        " + formatted_block + "," + content[insert_pos:]
            else:
                # Tìm fallback theo lessonVideos: { đầu tiên sau chapter_id
                pass

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Đã cập nhật {lesson_key} vào: {fpath}")


if __name__ == "__main__":
    if len(sys.argv) >= 7:
        update_curriculum(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else:
        print("Usage: python update_curriculum.py <chapter_id> <lesson_key> <video_url> <title> <duration> <description>")
