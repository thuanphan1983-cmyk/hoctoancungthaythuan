"""
SCENE 5: SƠ ĐỒ TƯ DUY TỔNG KẾT & DẶN DÒ BTVN (BÀI 2 FULL)
Bài 2: Cách ghi số tự nhiên (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn:
- Strict Safe-Zone & Auto-Scale: fit_safe_box (max_width=10.8, max_height=4.8, margins >= 1.2 x 0.8)
- Audio-Visual Sync chính xác từng mili-giây (mutagen MP3 get_audio_duration)
- Sơ đồ tư duy 4 nhánh & Hướng dẫn tự học, Font Arial Unicode MS (Zero Hex Boxes)
"""

import os
import sys
import json
from mutagen.mp3 import MP3
from manim import *

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

COLOR_BG = "#0b1120"
COLOR_CARD = "#1e293b"
COLOR_CYAN = "#38bdf8"
COLOR_EMERALD = "#34d399"
COLOR_AMBER = "#fbbf24"
COLOR_ROSE = "#f87171"
COLOR_INDIGO = "#818cf8"
COLOR_TEXT_MAIN = "#f8fafc"
COLOR_TEXT_MUTED = "#94a3b8"

FONT_FAMILY = "Arial Unicode MS"


def fit_safe_box(content_mobject, max_width=11.0, max_height=5.2):
    """Auto-scale helper: Giữ toàn bộ nội dung nằm tuyệt đối trong vùng an toàn"""
    if content_mobject.width > max_width:
        content_mobject.scale(max_width / content_mobject.width)
    if content_mobject.height > max_height:
        content_mobject.scale(max_height / content_mobject.height)
    return content_mobject


def get_audio_duration(audio_path, fallback=10.0):
    """Đo thời lượng thực tế của file âm thanh bằng mutagen chính xác từng mili-giây"""
    if os.path.exists(audio_path):
        try:
            return float(MP3(audio_path).info.length)
        except Exception:
            pass
    return fallback


class Scene5TongKet(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        audio_dir = os.path.join(os.path.dirname(__file__), "audio")
        timing_file = os.path.join(audio_dir, "timing_data.json")
        timing = {}
        if os.path.exists(timing_file):
            try:
                with open(timing_file, "r", encoding="utf-8") as f:
                    timing = json.load(f)
            except Exception:
                pass

        a_s5 = os.path.join(audio_dir, "scene5_full.mp3")
        total_s5 = get_audio_duration(a_s5, fallback=timing.get("scene5", 58.56))
        t_slide1 = total_s5 * 0.58
        t_slide2 = total_s5 * 0.42

        header = Text("PHẦN 5: TỔNG KẾT BÀI HỌC & DẶN DÒ TỰ HỌC", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # -------------------------------------------------------------
        # SLIDE 5.1: SƠ ĐỒ TƯ DUY 4 NHÁNH TRỌNG TÂM
        # -------------------------------------------------------------
        c1_title = Text("SƠ ĐỒ TƯ DUY 4 NHÁNH TRỌNG TÂM BÀI 2", font=FONT_FAMILY, font_size=29, weight=BOLD, color=COLOR_AMBER)
        b1_1 = Text("🌿 Nhánh 1: HỆ THẬP PHÂN", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_CYAN)
        b1_1_sub = Text("   + 10 chữ số (0 đến 9) • Phân chia theo từng hàng và lớp", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        b1_2 = Text("🌿 Nhánh 2: CẤU TẠO SỐ TỔNG QUÁT", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_EMERALD)
        b1_2_sub = Text("   + ab = 10a + b  ;  abc = 100a + 10b + c (với a ≠ 0)", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        b1_3 = Text("🌿 Nhánh 3: CHỮ SỐ LA MÃ", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_AMBER)
        b1_3_sub = Text("   + I (1), V (5), X (10) • Ghép phải CỘNG, ghép trái TRỪ", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        b1_4 = Text("🌿 Nhánh 4: QUY TẮC CẤM LẶP", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_ROSE)
        b1_4_sub = Text("   + Tuyệt đối không viết quá 3 lần chữ I, X liên tiếp (IV = 4, IX = 9)", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)

        c1_content = VGroup(
            c1_title, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_CYAN),
            b1_1, b1_1_sub,
            b1_2, b1_2_sub,
            b1_3, b1_3_sub,
            b1_4, b1_4_sub
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        fit_safe_box(c1_content, max_width=10.8, max_height=4.8)
        c1_content.move_to([0, -0.4, 0])

        c1_box = RoundedRectangle(corner_radius=0.3, width=c1_content.width + 0.8, height=c1_content.height + 0.65, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c1_content.get_center())
        card1 = VGroup(c1_box, c1_content)

        anim_sl1 = 0.6 + 0.6 + 0.7 + 0.7 + 0.7 + 0.7
        fade_dur = 0.6
        avail_sl1 = max(0.2, t_slide1 - fade_dur)
        scale_sl1 = min(1.0, (avail_sl1 - 0.2) / max(0.1, anim_sl1)) if anim_sl1 > avail_sl1 else 1.0

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.6 * scale_sl1)
        self.play(Write(c1_title), run_time=0.6 * scale_sl1)
        self.play(FadeIn(b1_1, shift=RIGHT), FadeIn(b1_1_sub), run_time=0.7 * scale_sl1)
        self.play(FadeIn(b1_2, shift=RIGHT), FadeIn(b1_2_sub), run_time=0.7 * scale_sl1)
        self.play(FadeIn(b1_3, shift=RIGHT), FadeIn(b1_3_sub), run_time=0.7 * scale_sl1)
        self.play(FadeIn(b1_4, shift=RIGHT), FadeIn(b1_4_sub), run_time=0.7 * scale_sl1)

        actual_anim1 = anim_sl1 * scale_sl1
        rem_sl1 = max(0.15, avail_sl1 - actual_anim1)
        self.wait(rem_sl1)
        self.play(FadeOut(card1, shift=UP*0.25), run_time=fade_dur)

        # -------------------------------------------------------------
        # SLIDE 5.2: HƯỚNG DẪN TỰ HỌC & DẶN DÒ BTVN
        # -------------------------------------------------------------
        c2_title = Text("HƯỚNG DẪN TỰ HỌC VÀ DẶN DÒ VỀ NHÀ", font=FONT_FAMILY, font_size=29, weight=BOLD, color=COLOR_EMERALD)
        hw1 = Text("📝 Nhiệm vụ 1: Vẽ lại sơ đồ tư duy 4 nhánh vào vở ghi bài", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_TEXT_MAIN)
        hw2 = Text("📚 Nhiệm vụ 2: Hoàn thành bài tập 1.6, 1.7, 1.8, 1.9 (Trang 12 SGK)", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_CYAN)
        hw3 = Text("🔥 Thử thách thực tế: Viết ngày tháng năm sinh của em bằng số La Mã", font=FONT_FAMILY, font_size=26, color=COLOR_AMBER)
        bye = Text("CẢM ƠN CÁC EM ĐÃ CHÚ Ý LẮNG NGHE! HẸN GẶP LẠI Ở BÀI 3!", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_TEXT_MAIN)

        c2_content = VGroup(
            c2_title, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD),
            hw1, hw2, hw3,
            Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD),
            bye
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fit_safe_box(c2_content, max_width=10.8, max_height=4.8)
        c2_content.move_to([0, -0.4, 0])

        c2_box = RoundedRectangle(corner_radius=0.3, width=c2_content.width + 0.8, height=c2_content.height + 0.65, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c2_content.get_center())
        card2 = VGroup(c2_box, c2_content)

        anim_sl2 = 0.6 + 0.6 + 0.7 + 0.7 + 0.6 + 0.8
        avail_sl2 = max(0.2, t_slide2)
        scale_sl2 = min(1.0, (avail_sl2 - 0.2) / max(0.1, anim_sl2)) if anim_sl2 > avail_sl2 else 1.0

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.6 * scale_sl2)
        self.play(Write(c2_title), run_time=0.6 * scale_sl2)
        self.play(FadeIn(hw1, shift=RIGHT), FadeIn(hw2, shift=RIGHT), run_time=0.7 * scale_sl2)
        self.play(FadeIn(hw3, shift=RIGHT), run_time=0.6 * scale_sl2)
        self.play(FadeIn(bye, scale=1.03), run_time=0.8 * scale_sl2)

        actual_anim2 = anim_sl2 * scale_sl2
        rem_sl2 = max(0.15, avail_sl2 - actual_anim2)
        self.wait(rem_sl2)


if __name__ == "__main__":
    pass
