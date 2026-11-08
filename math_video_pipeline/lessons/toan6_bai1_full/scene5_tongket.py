"""
SCENE 5: TỔNG KẾT & CỦNG CỐ
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Thời lượng đồng bộ audio: ~52.82s
"""

import os
import sys
from manim import *
from mutagen.mp3 import MP3

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


class Scene5TongKet(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        audio_file = os.path.join(cur_dir, "audio", "scene5_voice.mp3")
        target_duration = 52.82
        if os.path.exists(audio_file):
            try:
                target_duration = float(MP3(audio_file).info.length)
            except Exception:
                pass

        header = Text("PHẦN 5: TỔNG KẾT & SƠ ĐỒ TƯ DUY TOÀN BÀI", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=1.5, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.4)
        self.play(FadeIn(header_group), run_time=1.0)
        self.wait(3.0)  # Thầy giới thiệu sơ đồ tư duy

        # -------------------------------------------------------------
        # SƠ ĐỒ TƯ DUY 4 NHÁNH (3s -> 35s)
        # -------------------------------------------------------------
        def create_branch(num_str, title_str, desc_str, border_color):
            b = RoundedRectangle(corner_radius=0.2, width=5.8, height=1.6, stroke_color=border_color, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.9)
            h = Text(f"Nhánh {num_str}: {title_str}", font=FONT_FAMILY, font_size=16, weight=BOLD, color=border_color)
            d = Text(desc_str, font=FONT_FAMILY, font_size=14, color=COLOR_TEXT_MAIN)
            c = VGroup(h, d).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            return VGroup(b, c)

        b1 = create_branch("1", "Tên & Phần tử", "Tên viết HOA (A, B, C...)\nĐối tượng bên trong là phần tử", COLOR_CYAN).move_to([-3.2, 1.3, 0])
        b2 = create_branch("2", "2 Cách biểu diễn", "Liệt kê { 0; 1; 2; 3; 4 }\nNêu tính chất { x ∈ ℕ | x < 5 }", COLOR_AMBER).move_to([3.2, 1.3, 0])
        b3 = create_branch("3", "2 Ký hiệu cốt lõi", "∈ (Thuộc tập hợp: 3 ∈ A)\n∉ (Không thuộc: 5 ∉ A)", COLOR_EMERALD).move_to([-3.2, -0.7, 0])
        b4 = create_branch("4", "Sơ đồ Ven", "Đường cong khép kín (John Venn)\nĐiểm trong thuộc, điểm ngoài không thuộc", COLOR_INDIGO).move_to([3.2, -0.7, 0])

        self.play(FadeIn(b1, shift=RIGHT), run_time=1.0)
        self.wait(4.0)
        self.play(FadeIn(b2, shift=LEFT), run_time=1.0)
        self.wait(5.0)
        self.play(FadeIn(b3, shift=RIGHT), run_time=1.0)
        self.wait(4.0)
        self.play(FadeIn(b4, shift=LEFT), run_time=1.0)
        self.wait(6.0)

        # -------------------------------------------------------------
        # DẶN DÒ BTVN & LỜI CHÀO KẾT THÚC (35s -> 52.82s)
        # -------------------------------------------------------------
        mindmap_grp = VGroup(b1, b2, b3, b4)
        self.play(FadeOut(mindmap_grp), run_time=1.0)

        foot_box = RoundedRectangle(corner_radius=0.3, width=11.5, height=3.0, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95)
        foot_t1 = Text("📝 NHIỆM VỤ VỀ NHÀ DÀNH CHO CÁC EM:", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER)
        foot_t2 = Text("1. Xem kỹ lại video bài giảng và ghi chép sơ đồ tư duy vào vở.", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT_MAIN)
        foot_t3 = Text("2. Hoàn thành các bài tập 1.1 đến 1.5 trong Sách giáo khoa Toán 6 (KNTT).", font=FONT_FAMILY, font_size=16, color=COLOR_CYAN)
        foot_t4 = Text("HẸN GẶP LẠI CÁC EM TRONG BÀI 2: CÁCH GHI SỐ TỰ NHIÊN!", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_EMERALD)
        
        foot_content = VGroup(foot_t1, foot_t2, foot_t3, foot_t4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        foot_all = VGroup(foot_box, foot_content).move_to([0, -0.2, 0])

        self.play(FadeIn(foot_all, scale=0.95), run_time=1.2)

        rem_time = max(1.0, target_duration - 46.0)
        self.wait(rem_time)


if __name__ == "__main__":
    pass
