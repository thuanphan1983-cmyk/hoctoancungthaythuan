"""
SCENE 2: HÌNH THÀNH KIẾN THỨC MỚI
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Thời lượng đồng bộ audio: ~95.09s
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


class Scene2KienThuc(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        audio_file = os.path.join(cur_dir, "audio", "scene2_voice.mp3")
        target_duration = 95.09
        if os.path.exists(audio_file):
            try:
                target_duration = float(MP3(audio_file).info.length)
            except Exception:
                pass

        # Header cố định
        header = Text("PHẦN 2: HÌNH THÀNH KIẾN THỨC TRỌNG TÂM", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=1.5, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.4)
        self.play(FadeIn(header_group), run_time=1.0)
        self.wait(2.5)  # Thầy giới thiệu 4 nội dung

        # -------------------------------------------------------------
        # KHỐI 1: TÊN TẬP HỢP VÀ PHẦN TỬ (3.5s -> 18s)
        # -------------------------------------------------------------
        k1_rect = RoundedRectangle(corner_radius=0.25, width=11.5, height=2.2, stroke_color=COLOR_INDIGO, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.9)
        k1_title = Text("1. Ký hiệu tên và phần tử của tập hợp", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER)
        k1_txt1 = Text("• Tên tập hợp: Được đặt bằng chữ cái IN HOA:  A, B, C, X, Y...", font=FONT_FAMILY, font_size=18, color=COLOR_TEXT_MAIN)
        k1_txt2 = Text("• Phần tử: Các đối tượng nằm bên trong tập hợp được gọi là phần tử của tập hợp.", font=FONT_FAMILY, font_size=17, color=COLOR_TEXT_MUTED)
        k1_content = VGroup(k1_title, k1_txt1, k1_txt2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        k1_box = VGroup(k1_rect, k1_content).next_to(header_group, DOWN, buff=0.3)

        self.play(FadeIn(k1_box, shift=DOWN), run_time=1.2)
        self.wait(10.5)  # Thầy giảng giải khối 1

        # -------------------------------------------------------------
        # KHỐI 2: HAI CÁCH VIẾT TẬP HỢP (18s -> 52s)
        # -------------------------------------------------------------
        # Thu nhỏ khối 1 để lấy không gian cho khối 2
        self.play(k1_box.animate.scale(0.85).to_edge(LEFT, buff=0.6).shift(UP * 0.8), run_time=1.0)

        k2_rect = RoundedRectangle(corner_radius=0.25, width=11.5, height=3.6, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95)
        k2_title = Text("2. Hai cách cho một tập hợp", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER)
        
        c1_title = Text("Cách 1: Liệt kê các phần tử", font=FONT_FAMILY, font_size=17, weight=BOLD, color=COLOR_CYAN)
        c1_desc = Text("• Viết vào ngoặc nhọn { }, ngăn cách bởi dấu chấm phẩy (;)\n• Mỗi phần tử chỉ viết 1 lần duy nhất, thứ tự tùy ý.", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT_MAIN)
        c1_ex = Text("Ví dụ:  A = {0; 1; 2; 3; 4}", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_EMERALD)
        
        c2_title = Text("Cách 2: Chỉ ra tính chất đặc trưng", font=FONT_FAMILY, font_size=17, weight=BOLD, color=COLOR_CYAN)
        c2_desc = Text("• Nêu quy luật chung mà chỉ các phần tử của tập hợp thỏa mãn.", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT_MAIN)
        c2_ex = Text("Ví dụ:  A = { x ∈ ℕ | x < 5 }", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_EMERALD)

        col1 = VGroup(c1_title, c1_desc, c1_ex).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        col2 = VGroup(c2_title, c2_desc, c2_ex).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        cols = VGroup(col1, col2).arrange(RIGHT, buff=0.6)

        k2_content = VGroup(k2_title, cols).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        k2_box = VGroup(k2_rect, k2_content).move_to([0, -0.9, 0])

        self.play(FadeIn(k2_box, scale=0.95), run_time=1.2)
        self.wait(26.0)  # Thầy giảng chi tiết 2 cách viết và ví dụ cụ thể

        # -------------------------------------------------------------
        # KHỐI 3 & 4: KÝ HIỆU THUỘC / KHÔNG THUỘC VÀ SƠ ĐỒ VEN (52s -> 95s)
        # -------------------------------------------------------------
        self.play(FadeOut(k1_box), FadeOut(k2_box), run_time=1.0)

        # Cột trái: Ký hiệu thuộc/không thuộc
        sym_rect = RoundedRectangle(corner_radius=0.25, width=5.8, height=4.6, stroke_color=COLOR_EMERALD, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.9)
        sym_title = Text("3. Ký hiệu Thuộc & Không thuộc", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_AMBER)
        
        row_in = VGroup(
            Text("3 ∈ A", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_EMERALD),
            Text("→ '3 thuộc tập hợp A'\n(3 là phần tử của A)", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT_MAIN)
        ).arrange(RIGHT, buff=0.4)
        
        row_out = VGroup(
            Text("5 ∉ A", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_ROSE),
            Text("→ '5 không thuộc tập A'\n(5 không là phần tử của A)", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT_MAIN)
        ).arrange(RIGHT, buff=0.4)

        sym_content = VGroup(sym_title, row_in, row_out).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        sym_box = VGroup(sym_rect, sym_content).move_to([-3.2, -0.6, 0])

        # Cột phải: Sơ đồ Ven hình elip
        venn_rect = RoundedRectangle(corner_radius=0.25, width=5.8, height=4.6, stroke_color=COLOR_CYAN, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.9)
        venn_title = Text("4. Minh họa bằng Sơ đồ Ven", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_AMBER)
        
        ellipse = Ellipse(width=3.6, height=2.4, color=COLOR_CYAN, stroke_width=3, fill_color=COLOR_CYAN, fill_opacity=0.15)
        venn_label = Text("Tập hợp A", font=FONT_FAMILY, font_size=15, weight=BOLD, color=COLOR_CYAN).next_to(ellipse, UP, buff=0.1)

        # Các điểm bên trong elip
        p0 = VGroup(Dot(radius=0.07, color=COLOR_EMERALD), Text("0", font_size=16, weight=BOLD)).arrange(RIGHT, buff=0.08).move_to(ellipse.get_center() + LEFT*0.9 + UP*0.4)
        p1 = VGroup(Dot(radius=0.07, color=COLOR_EMERALD), Text("1", font_size=16, weight=BOLD)).arrange(RIGHT, buff=0.08).move_to(ellipse.get_center() + RIGHT*0.8 + UP*0.3)
        p2 = VGroup(Dot(radius=0.07, color=COLOR_EMERALD), Text("2", font_size=16, weight=BOLD)).arrange(RIGHT, buff=0.08).move_to(ellipse.get_center() + DOWN*0.4)
        p3 = VGroup(Dot(radius=0.07, color=COLOR_EMERALD), Text("3", font_size=16, weight=BOLD)).arrange(RIGHT, buff=0.08).move_to(ellipse.get_center() + LEFT*0.7 + DOWN*0.3)
        p4 = VGroup(Dot(radius=0.07, color=COLOR_EMERALD), Text("4", font_size=16, weight=BOLD)).arrange(RIGHT, buff=0.08).move_to(ellipse.get_center() + RIGHT*0.7 + DOWN*0.4)

        # Điểm bên ngoài elip
        p5 = VGroup(Dot(radius=0.07, color=COLOR_ROSE), Text("5", font_size=16, weight=BOLD, color=COLOR_ROSE)).arrange(RIGHT, buff=0.08).move_to(ellipse.get_center() + RIGHT*2.2 + UP*0.8)
        p5_note = Text("(ngoài A)", font=FONT_FAMILY, font_size=12, color=COLOR_ROSE).next_to(p5, DOWN, buff=0.05)

        venn_diag = VGroup(ellipse, venn_label, p0, p1, p2, p3, p4, p5, p5_note).scale(0.85)
        venn_content = VGroup(venn_title, venn_diag).arrange(DOWN, buff=0.25)
        venn_box = VGroup(venn_rect, venn_content).move_to([3.2, -0.6, 0])

        self.play(FadeIn(sym_box, shift=RIGHT), run_time=1.2)
        self.wait(10.0)  # Thầy giảng ký hiệu thuộc / không thuộc

        self.play(FadeIn(venn_box, shift=LEFT), run_time=1.2)
        self.wait(14.0)  # Thầy giảng Sơ đồ Ven John Venn

        # Chờ phần thời gian còn lại khớp target_duration
        # Khoảng ~88s đã trôi qua
        rem_time = max(1.0, target_duration - 87.0)
        self.wait(rem_time)


if __name__ == "__main__":
    pass
