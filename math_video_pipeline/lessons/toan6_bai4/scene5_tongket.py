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


class Scene5TongKet(Scene):
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

        t_s5 = timing.get("scene5", 35.0)

        header = Text("PHẦN 5: SƠ ĐỒ TƯ DUY TỔNG KẾT & DẶN DÒ", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_INDIGO)
        header_line = Line(LEFT * 5.6, RIGHT * 5.6, stroke_width=2, color=COLOR_INDIGO)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        c_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        c_title = safe_text("TỔNG KẾT: PHÉP CỘNG VÀ PHÉP TRỪ SỐ TỰ NHIÊN", font_size=28, weight=BOLD, color=COLOR_INDIGO, max_width=10.6)
        c_line = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_INDIGO)
        n_items = []
        n_items.append(safe_text("1. Phép cộng: Giao hoán, kết hợp, cộng 0.", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4))
        n_items.append(safe_text("2. Phép trừ: a ≥ b trong N; a - (b + c) = a - b - c.", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4))
        n_items.append(safe_text("3. Dãy số cách đều: (Đầu + Cuối) × Số số hạng : 2.", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4))
        hw_items = []
        hw_items.append(safe_text("• Bài 1.20, 1.21, 1.22 SGK Toán 6.", font_size=22, color=COLOR_AMBER, max_width=10.4))
        hw_items.append(safe_text("• Tính nhanh tổng các số chẵn từ 2 đến 100.", font_size=22, color=COLOR_AMBER, max_width=10.4))

        content = VGroup(c_title, c_line, *n_items, *hw_items).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        content.move_to(c_box.get_center())
        card = VGroup(c_box, content)

        self.play(FadeIn(c_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(c_title, shift=DOWN*0.1), run_time=0.8)
        for nitm in n_items:
            self.play(FadeIn(nitm, shift=RIGHT*0.2), run_time=0.4)
        for hitm in hw_items:
            self.play(FadeIn(hitm, shift=RIGHT*0.2), run_time=0.4)

        rem_s5 = max(1.0, t_s5 - (1.6 + (len(n_items) + len(hw_items)) * 0.4))
        self.wait(rem_s5)

if __name__ == "__main__":
    pass
