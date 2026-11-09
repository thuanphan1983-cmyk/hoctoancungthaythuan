import os
import sys
import json
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
FONT_FAMILY = "Arial"
MATH_FONT = "Segoe UI Symbol"

def math_text(expr, font_size=24, color=COLOR_TEXT_MAIN, weight=BOLD):
    return Text(expr, font=MATH_FONT, font_size=font_size, weight=weight, color=color)

def safe_text(txt, font=FONT_FAMILY, font_size=24, weight=NORMAL, color=COLOR_TEXT_MAIN, max_width=10.6):
    t = Text(txt, font=font, font_size=font_size, weight=weight, color=color)
    if t.width > max_width:
        t.scale_to_fit_width(max_width)
    return t


class Scene4CanhBao(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        timing_file = os.path.join(os.path.dirname(__file__), "audio", "timing_data.json")
        timing = {}
        if os.path.exists(timing_file):
            try:
                with open(timing_file, "r", encoding="utf-8") as f:
                    timing = json.load(f)
            except Exception:
                pass

        header = Text("PHẦN 4: LỖI SAI KINH ĐIỂN CẦN TRÁNH", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_ROSE)
        header_line = Line(LEFT * 5.6, RIGHT * 5.6, stroke_width=2, color=COLOR_ROSE)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # ----------------- TRAP 1 -----------------
        t_tr1 = timing.get("scene4_trap1", 22.0)
        c1_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        c1_title = safe_text("LỖI SAI 1: BỎ QUÊN NGHIỆM BIÊN CÓ DẤU BẰNG", font_size=26, weight=BOLD, color=COLOR_ROSE, max_width=10.6)
        line1 = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_ROSE)

        bad_1 = VGroup(math_text("✗", font_size=26, color=COLOR_ROSE), safe_text("  Sai: x ≤ 5 mà chỉ lấy {0, 1, 2, 3, 4}", font_size=23, weight=BOLD, color=COLOR_ROSE, max_width=10.0)).arrange(RIGHT, buff=0.08)
        good_1 = VGroup(math_text("✓", font_size=26, color=COLOR_EMERALD), safe_text("  Đúng: x ≤ 5 phải lấy cả số 5: {0, 1, 2, 3, 4, 5}", font_size=23, weight=BOLD, color=COLOR_EMERALD, max_width=10.0)).arrange(RIGHT, buff=0.08)
        note_1 = safe_text("• Lời khuyên: Ký hiệu ≤ bao gồm cả trường hợp bằng.", font_size=22, color=COLOR_TEXT_MUTED, max_width=10.4)

        c1_content = VGroup(c1_title, line1, bad_1, good_1, note_1).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c1_content.move_to(c1_box.get_center())
        card1 = VGroup(c1_box, c1_content)

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(c1_title, shift=DOWN*0.1), run_time=0.8)
        self.play(FadeIn(bad_1, shift=RIGHT*0.2), run_time=0.8)
        self.play(FadeIn(good_1, shift=RIGHT*0.2), run_time=0.8)
        self.play(FadeIn(note_1, shift=UP*0.1), run_time=0.6)

        rem_tr1 = max(0.5, t_tr1 - 3.8)
        self.wait(rem_tr1)
        self.play(FadeOut(card1, shift=UP*0.3), run_time=0.8)

        # ----------------- TRAP 2 -----------------
        t_tr2 = timing.get("scene4_trap2", 22.0)
        c2_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        c2_title = safe_text("LỖI SAI 2: NGHĨ RẰNG 0 CÓ SỐ LIỀN TRƯỚC TRONG N", font_size=26, weight=BOLD, color=COLOR_ROSE, max_width=10.6)
        line2 = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_ROSE)

        bad_2 = VGroup(math_text("✗", font_size=26, color=COLOR_ROSE), safe_text("  Sai: Số liền trước của 0 là -1 trong N", font_size=23, weight=BOLD, color=COLOR_ROSE, max_width=10.0)).arrange(RIGHT, buff=0.08)
        good_2 = VGroup(math_text("✓", font_size=26, color=COLOR_EMERALD), safe_text("  Đúng: Trong N, 0 không có số liền trước", font_size=23, weight=BOLD, color=COLOR_EMERALD, max_width=10.0)).arrange(RIGHT, buff=0.08)
        note_2 = safe_text("• Lời khuyên: 0 là số tự nhiên nhỏ nhất.", font_size=22, color=COLOR_TEXT_MUTED, max_width=10.4)

        c2_content = VGroup(c2_title, line2, bad_2, good_2, note_2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c2_content.move_to(c2_box.get_center())
        card2 = VGroup(c2_box, c2_content)

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(c2_title, shift=DOWN*0.1), run_time=0.8)
        self.play(FadeIn(bad_2, shift=RIGHT*0.2), run_time=0.8)
        self.play(FadeIn(good_2, shift=RIGHT*0.2), run_time=0.8)
        self.play(FadeIn(note_2, shift=UP*0.1), run_time=0.6)

        rem_tr2 = max(0.5, t_tr2 - 3.8)
        self.wait(rem_tr2)
        self.play(FadeOut(card2, shift=UP*0.3), run_time=0.8)

if __name__ == "__main__":
    pass
