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


class Scene2KienThuc(Scene):
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

        header = Text("PHẦN 2: HÌNH THÀNH KIẾN THỨC MỚI", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_EMERALD)
        header_line = Line(LEFT * 5.6, RIGHT * 5.6, stroke_width=2, color=COLOR_EMERALD)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # ----------------- SLIDE 1 -----------------
        t_s1 = timing.get("scene2_slide1", 28.0)
        c1_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        c1_title = safe_text("1. TÍNH CHẤT PHÉP CỘNG", font_size=28, weight=BOLD, color=COLOR_CYAN, max_width=10.6)
        c1_sub = safe_text("Giao hoán, kết hợp và cộng với số 0", font_size=23, weight=SEMIBOLD, color=COLOR_TEXT_MUTED, max_width=10.6)
        line1 = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_CYAN)
        itms_1 = []
        itms_1.append(safe_text("• Giao hoán: a + b = b + a", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4))
        itms_1.append(safe_text("• Kết hợp: (a + b) + c = a + (b + c)", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4))
        itms_1.append(safe_text("• Cộng với 0: a + 0 = 0 + a = a", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4))
        itms_1.append(safe_text("• Ghép nhóm tạo số tròn chục, tròn trăm.", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4))
        c1_content = VGroup(c1_title, c1_sub, line1, *itms_1).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        c1_content.move_to(c1_box.get_center())
        card1 = VGroup(c1_box, c1_content)

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(c1_title, shift=DOWN*0.1), FadeIn(c1_sub, shift=UP*0.1), run_time=1.0)
        for itm in itms_1:
            self.play(FadeIn(itm, shift=RIGHT*0.2), run_time=0.4)

        rem_s1 = max(0.5, t_s1 - (1.8 + len(itms_1) * 0.4))
        self.wait(rem_s1)
        self.play(FadeOut(card1, shift=UP*0.3), run_time=0.8)

        # ----------------- SLIDE 2 -----------------
        t_s2 = timing.get("scene2_slide2", 28.0)
        c2_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        c2_title = safe_text("2. PHÉP TRỪ SỐ TỰ NHIÊN", font_size=28, weight=BOLD, color=COLOR_EMERALD, max_width=10.6)
        c2_sub = safe_text("Điều kiện để thực hiện được phép trừ", font_size=23, weight=SEMIBOLD, color=COLOR_TEXT_MUTED, max_width=10.6)
        line2 = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_EMERALD)
        itms_2 = []
        itms_2.append(safe_text("• Cho hai số a và b. Nếu a ≥ b thì tồn tại số x sao cho b + x = a.", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4))
        itms_2.append(safe_text("• Ký hiệu: a - b = x (a là số bị trừ, b là số trừ, x là hiệu).", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4))
        itms_2.append(safe_text("• Trong tập N: a - b chỉ thực hiện được khi a ≥ b.", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4))
        itms_2.append(safe_text("• a - a = 0 ; a - 0 = a.", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4))
        c2_content = VGroup(c2_title, c2_sub, line2, *itms_2).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        c2_content.move_to(c2_box.get_center())
        card2 = VGroup(c2_box, c2_content)

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(c2_title, shift=DOWN*0.1), FadeIn(c2_sub, shift=UP*0.1), run_time=1.0)
        for itm in itms_2:
            self.play(FadeIn(itm, shift=RIGHT*0.2), run_time=0.4)

        rem_s2 = max(0.5, t_s2 - (1.8 + len(itms_2) * 0.4))
        self.wait(rem_s2)
        self.play(FadeOut(card2, shift=UP*0.3), run_time=0.8)

if __name__ == "__main__":
    pass
