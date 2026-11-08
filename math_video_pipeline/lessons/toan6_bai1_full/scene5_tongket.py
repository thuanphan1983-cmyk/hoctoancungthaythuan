"""
SCENE 5: SƠ ĐỒ TƯ DUY TỔNG KẾT & DẶN DÒ BTVN (CHUẨN CUỐN CHIẾU 15-20 PHÚT)
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn: 2 slide cuốn chiếu, Mindmap 4 nhánh phát sáng, Font size >= 28
"""

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

        header = Text("PHẦN 5: TỔNG KẾT BÀI HỌC & DẶN DÒ TỰ HỌC", font=FONT_FAMILY, font_size=34, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # -------------------------------------------------------------
        # SLIDE 5.1: SƠ ĐỒ TƯ DUY 4 NHÁNH
        # -------------------------------------------------------------
        t_s1 = timing.get("scene5_slide1", 45.0)
        c1_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c1_title = Text("SƠ ĐỒ TƯ DUY 4 NHÁNH TRỌNG TÂM", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        
        b1_1 = Text("🌿 Nhánh 1: TÊN VÀ PHẦN TỬ", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN)
        b1_1_sub = Text("   + Tên viết HOA (A, B, C...) • Đối tượng là phần tử", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MAIN)
        
        b1_2 = Text("🌿 Nhánh 2: HAI CÁCH BIỂU DIỄN", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_EMERALD)
        b1_2_sub = Text("   + Liệt kê trong ngoặc nhọn { } • Nêu tính chất đặc trưng", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MAIN)
        
        b1_3 = Text("🌿 Nhánh 3: HAI KÝ HIỆU CỐT LÕI", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        b1_3_sub = Text("   + ∈ (Thuộc tập hợp) • ∉ (Không thuộc tập hợp)", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MAIN)
        
        b1_4 = Text("🌿 Nhánh 4: SƠ ĐỒ VEN", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_INDIGO)
        b1_4_sub = Text("   + Đường cong khép kín trực quan của John Venn", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MAIN)
        
        c1_content = VGroup(
            c1_title, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_CYAN),
            b1_1, b1_1_sub,
            b1_2, b1_2_sub,
            b1_3, b1_3_sub,
            b1_4, b1_4_sub
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        c1_content.move_to(c1_box.get_center())
        card1 = VGroup(c1_box, c1_content)

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(Write(c1_title), run_time=1.0)
        self.play(FadeIn(b1_1, shift=RIGHT), FadeIn(b1_1_sub), run_time=1.0)
        self.play(FadeIn(b1_2, shift=RIGHT), FadeIn(b1_2_sub), run_time=1.0)
        self.play(FadeIn(b1_3, shift=RIGHT), FadeIn(b1_3_sub), run_time=1.0)
        self.play(FadeIn(b1_4, shift=RIGHT), FadeIn(b1_4_sub), run_time=1.0)

        rem_s1 = max(1.0, t_s1 - 6.0)
        self.wait(rem_s1)
        self.play(FadeOut(card1, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 5.2: DẶN DÒ BTVN & LỜI CHÀO KẾT BÀI
        # -------------------------------------------------------------
        t_s2 = timing.get("scene5_slide2", 42.0)
        c2_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c2_title = Text("NHIỆM VỤ TỰ HỌC VỀ NHÀ DÀNH CHO CÁC EM", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_EMERALD)
        
        b2_1 = Text("📝 Nhiệm vụ 1: Vẽ lại sơ đồ tư duy 4 nhánh vào vở ghi bài", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN)
        b2_2 = Text("📝 Nhiệm vụ 2: Hoàn thành bài tập 1.1 đến 1.5 trong SGK Toán 6", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN)
        b2_3 = Text("   (Bộ sách Kết nối tri thức với cuộc sống)", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MUTED)
        b2_4 = Text("🚀 ĐÓN XEM TIẾT HỌC TIẾP THEO:", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        b2_5 = Text("   BÀI 2: CÁCH GHI SỐ TỰ NHIÊN", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        b2_6 = Text("Chúc các em luôn yêu thích môn Toán! Xin chào và hẹn gặp lại!", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_EMERALD)
        
        c2_content = VGroup(
            c2_title, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD),
            b2_1, b2_2, b2_3, b2_4, b2_5, b2_6
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        c2_content.move_to(c2_box.get_center())
        card2 = VGroup(c2_box, c2_content)

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(Write(c2_title), run_time=1.0)
        self.play(FadeIn(b2_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b2_2, shift=RIGHT), FadeIn(b2_3), run_time=0.8)
        self.play(FadeIn(b2_4, shift=UP), FadeIn(b2_5, scale=1.05), run_time=1.2)
        self.play(FadeIn(b2_6, scale=1.05), run_time=1.0)

        rem_s2 = max(1.0, t_s2 - 5.6)
        self.wait(rem_s2)


if __name__ == "__main__":
    pass
