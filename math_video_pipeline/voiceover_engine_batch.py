"""
VOICEOVER BATCH ENGINE (EDGE-TTS + TIMING JSON)
Tự động sinh trọn bộ audio 5 phân cảnh khớp chính xác kịch bản bài học
Tốc độ đọc giọng AI: rate="-18%" chuẩn sư phạm truyền cảm
Hỗ trợ cache thông minh (bỏ qua file đã có) và timeout chống treo mạng.
"""

import os
import sys
import wave
import math
import json
import struct
import shutil
import asyncio
import tempfile
import subprocess
import edge_tts
from mutagen.mp3 import MP3

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

DEFAULT_VOICE = "vi-VN-NamMinhNeural"
SPEECH_RATE = "-18%"


def get_duration(audio_path: str) -> float:
    """Đo thời lượng file mp3 theo giây"""
    if not os.path.exists(audio_path) or os.path.getsize(audio_path) == 0:
        return 0.0
    try:
        return float(MP3(audio_path).info.length)
    except Exception:
        return 5.0


def generate_tick_audio(output_mp3_path: str, duration_sec: int = 45):
    """Sinh file mp3 tiếng tích tắc đồng hồ 45s nếu chưa có"""
    if os.path.exists(output_mp3_path) and os.path.getsize(output_mp3_path) > 1000:
        return output_mp3_path

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
            if sec_sample < int(0.035 * sample_rate):
                t = sec_sample / sample_rate
                freq = 880 if ((s // sample_rate) % 2 == 0) else 660
                envelope = math.exp(-t * 110)
                val = int(envelope * 6500 * math.sin(2 * math.pi * freq * t))
            else:
                val = 0
            samples.append(struct.pack("<h", val))
        wav.writeframes(b"".join(samples))

    cmd = ["ffmpeg", "-y", "-i", wav_path, "-c:a", "libmp3lame", "-b:a", "64k", output_mp3_path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    if os.path.exists(wav_path):
        os.remove(wav_path)
    return output_mp3_path


def split_text_into_subsentences(text: str, max_chars: int = 180) -> list:
    """Chia văn bản thành từng câu ngắn dưới 180 ký tự để tránh nghẽn websocket"""
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


async def generate_chunk_audio(chunk_text: str, output_path: str, voice=DEFAULT_VOICE, rate=SPEECH_RATE) -> bool:
    if os.path.exists(output_path) and os.path.getsize(output_path) > 500:
        return True

    for attempt in range(1, 4):
        try:
            communicate = edge_tts.Communicate(text=chunk_text, voice=voice, rate=rate)
            await asyncio.wait_for(communicate.save(output_path), timeout=35.0)
            if os.path.exists(output_path) and os.path.getsize(output_path) > 100:
                await asyncio.sleep(0.4)
                return True
        except Exception:
            await asyncio.sleep(1.0 * attempt)

    # CLI fallback with explicit = flag to prevent argparse argument error
    try:
        rate_arg = f"--rate={rate}" if rate else "--rate=+0%"
        cmd = ["edge-tts", "--voice", voice, rate_arg, "--text", chunk_text, "--write-media", output_path]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=40)
        if res.returncode == 0 and os.path.exists(output_path) and os.path.getsize(output_path) > 100:
            return True
    except Exception:
        pass
    return False


async def generate_voice_for_text(text: str, output_path: str, voice=DEFAULT_VOICE, rate=SPEECH_RATE) -> str:
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        return output_path

    chunks = split_text_into_subsentences(text, max_chars=180)
    temp_dir = tempfile.mkdtemp(prefix="tts_parts_")
    part_files = []
    for idx, c in enumerate(chunks):
        p_path = os.path.join(temp_dir, f"part_{idx:03d}.mp3")
        ok = await generate_chunk_audio(c, p_path, voice=voice, rate=rate)
        if not ok:
            await generate_chunk_audio(c, p_path, voice=voice, rate=None)
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


def concat_audio_files(file_list: list, output_path: str) -> str:
    if os.path.exists(output_path) and os.path.getsize(output_path) > 2000:
        return output_path

    temp_dir = tempfile.mkdtemp(prefix="audio_concat_")
    list_file = os.path.join(temp_dir, "concat.txt")
    with open(list_file, "w", encoding="utf-8") as f:
        for fpath in file_list:
            safe_p = fpath.replace("\\", "/")
            f.write(f"file '{safe_p}'\n")
    if os.path.exists(output_path):
        os.remove(output_path)
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", output_path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    shutil.rmtree(temp_dir, ignore_errors=True)
    return output_path


def generate_lesson_audio(lesson_data: dict, audio_dir: str) -> dict:
    """Tự động sinh toàn bộ audio cho 1 bài học và lưu timing_data.json"""
    os.makedirs(audio_dir, exist_ok=True)
    timing_data = {}

    # 1. Đếm ngược 45s (tick45.mp3)
    tick_file = os.path.join(audio_dir, "tick45.mp3")
    generate_tick_audio(tick_file, duration_sec=45)

    # 2. Scene 1 (Khởi động)
    s1_parts = []
    p1_slides = lesson_data.get("part1", {}).get("slides", [])
    for idx, sl in enumerate(p1_slides):
        p_out = os.path.join(audio_dir, f"scene1_slide{idx+1}.mp3")
        asyncio.run(generate_voice_for_text(sl["voice"], p_out))
        dur = get_duration(p_out)
        s1_parts.append(p_out)
        timing_data[f"scene1_slide{idx+1}"] = dur
    s1_full = os.path.join(audio_dir, "scene1_full.mp3")
    concat_audio_files(s1_parts, s1_full)
    timing_data["scene1"] = get_duration(s1_full)

    # 3. Scene 2 (Kiến thức)
    s2_parts = []
    p2_slides = lesson_data.get("part2", {}).get("slides", [])
    for idx, sl in enumerate(p2_slides):
        p_out = os.path.join(audio_dir, f"scene2_slide{idx+1}.mp3")
        asyncio.run(generate_voice_for_text(sl["voice"], p_out))
        dur = get_duration(p_out)
        s2_parts.append(p_out)
        timing_data[f"scene2_slide{idx+1}"] = dur
    s2_full = os.path.join(audio_dir, "scene2_full.mp3")
    concat_audio_files(s2_parts, s2_full)
    timing_data["scene2"] = get_duration(s2_full)

    # 4. Scene 3 (3 Ví dụ + 45s)
    s3_parts = []
    examples = lesson_data.get("part3", {}).get("examples", [])
    for idx, ex in enumerate(examples):
        i = idx + 1
        intro_out = os.path.join(audio_dir, f"scene3_ex{i}_intro.mp3")
        sol_out = os.path.join(audio_dir, f"scene3_ex{i}_sol.mp3")
        asyncio.run(generate_voice_for_text(ex.get("voice_intro", "Các em hãy suy nghĩ trong 45 giây nhé!"), intro_out))
        asyncio.run(generate_voice_for_text(ex.get("voice_sol", "Cùng đối chiếu lời giải chi tiết nhé!"), sol_out))
        
        t_intro = get_duration(intro_out)
        t_sol = get_duration(sol_out)
        timing_data[f"scene3_ex{i}_intro"] = t_intro
        timing_data[f"scene3_ex{i}_timer"] = 45.0
        timing_data[f"scene3_ex{i}_sol"] = t_sol

        s3_parts.extend([intro_out, tick_file, sol_out])

    s3_full = os.path.join(audio_dir, "scene3_full.mp3")
    concat_audio_files(s3_parts, s3_full)
    timing_data["scene3"] = get_duration(s3_full)

    # 5. Scene 4 (Cảnh báo bẫy thi)
    s4_parts = []
    traps = lesson_data.get("part4", {}).get("traps", [])
    for idx, tr in enumerate(traps):
        p_out = os.path.join(audio_dir, f"scene4_trap{idx+1}.mp3")
        asyncio.run(generate_voice_for_text(tr.get("voice", "Chú ý không mắc phải lỗi sai này nhé!"), p_out))
        dur = get_duration(p_out)
        s4_parts.append(p_out)
        timing_data[f"scene4_trap{idx+1}"] = dur
    s4_full = os.path.join(audio_dir, "scene4_full.mp3")
    concat_audio_files(s4_parts, s4_full)
    timing_data["scene4"] = get_duration(s4_full)

    # 6. Scene 5 (Sơ đồ tư duy & Tổng kết)
    s5_full = os.path.join(audio_dir, "scene5_full.mp3")
    p5_voice = lesson_data.get("part5", {}).get("voice", "Bài học hôm nay đến đây là kết thúc, hẹn gặp lại các em!")
    asyncio.run(generate_voice_for_text(p5_voice, s5_full))
    timing_data["scene5"] = get_duration(s5_full)

    # Lưu timing_data.json
    timing_file = os.path.join(audio_dir, "timing_data.json")
    with open(timing_file, "w", encoding="utf-8") as f:
        json.dump(timing_data, f, indent=2)

    return timing_data
