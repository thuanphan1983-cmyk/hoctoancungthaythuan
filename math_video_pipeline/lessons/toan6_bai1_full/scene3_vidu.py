"""
SCENE 3: VÍ DỤ MINH HỌA ÁP DỤNG
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Thời lượng đồng bộ audio: ~114.91s
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


class Scene3ViDu(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        audio_file = os.path.join(cur_dir, "audio", "scene3_voice.mp3")
        target_duration = 114.91
        if os.path.exists(audio_file):
            try:
                target_duration = float(MP3(audio_file).info.length)
            except Exception:
                pass

        header = Text("PHẦN 3: BỐN VÍ DỤ MINH HỌA NÂNG CAO KỸ NĂNG", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_AMBER)
        header_line = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=1.5, color=COLOR_AMBER)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.4)
        self.play(FadeIn(header_group), run_time=1.0)
        self.wait(3.0)  # Thầy giới thiệu 4 ví dụ

        # -------------------------------------------------------------
        # VÍ DỤ 1 (Mức Nhận biết): Chữ cái trong từ "TOÁN HỌC" (~22s)
        # -------------------------------------------------------------
        vd1_rect = RoundedRectangle(corner_radius=0.25, width=12.0, height=2.4, stroke_color=COLOR_CYAN, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.9)
        vd1_badge = Text("VÍ DỤ 1 (Nhận biết):", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_CYAN)
        vd1_req = Text("Viết tập hợp M gồm các chữ cái trong từ 'TOÁN HỌC'.", font=FONT_FAMILY, font_size=17, color=COLOR_TEXT_MAIN)
        vd1_top = VGroup(vd1_badge, vd1_req).arrange(RIGHT, buff=0.3)
        
        vd1_sol_t = Text("• Phân tích: Từ TOÁN HỌC gồm: T, O, Á, N, H, O, C (Chữ O xuất hiện 2 lần → chỉ ghi 1 lần)", font=FONT_FAMILY, font_size=15, color=COLOR_AMBER)
        vd1_sol_ans = Text("✓ Lời giải:  M = { T; O; Á; N; H; C }", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_EMERALD)
        
        vd1_content = VGroup(vd1_top, vd1_sol_t, vd1_sol_ans).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        vd1_box = VGroup(vd1_rect, vd1_content).next_to(header_group, DOWN, buff=0.35)

        self.play(FadeIn(vd1_box, shift=DOWN), run_time=1.2)
        self.wait(18.0)  # Thầy giảng chi tiết VD1

        # -------------------------------------------------------------
        # VÍ DỤ 2 (Mức Thông hiểu): Liệt kê và điền ∈, ∉ (~25s)
        # -------------------------------------------------------------
        vd2_rect = RoundedRectangle(corner_radius=0.25, width=12.0, height=2.6, stroke_color=COLOR_EMERALD, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.9)
        vd2_badge = Text("VÍ DỤ 2 (Thông hiểu):", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_EMERALD)
        vd2_req = Text("Cho tập hợp  B = { x ∈ ℕ | 10 ≤ x < 15 }. Viết B dưới dạng liệt kê và điền ∈, ∉.", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT_MAIN)
        vd2_top = VGroup(vd2_badge, vd2_req).arrange(RIGHT, buff=0.3)
        
        vd2_sol1 = Text("• Lời giải:  B = { 10; 11; 12; 13; 14 }  (Lấy số 10 vì x ≥ 10; dừng ở 14 vì x < 15)", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT_MAIN)
        vd2_sol2 = Text("✓ Điền ký hiệu:   10 ∈ B      12 ∈ B      15 ∉ B      9 ∉ B", font=FONT_FAMILY, font_size=17, weight=BOLD, color=COLOR_CYAN)
        
        vd2_content = VGroup(vd2_top, vd2_sol1, vd2_sol2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        vd2_box = VGroup(vd2_rect, vd2_content).next_to(vd1_box, DOWN, buff=0.25)

        self.play(FadeIn(vd2_box, shift=UP), run_time=1.2)
        self.wait(22.0)  # Thầy giảng chi tiết VD2

        # Ẩn VD1, VD2 để làm không gian cho VD3, VD4
        self.play(FadeOut(vd1_box), FadeOut(vd2_box), run_time=1.0)

        # -------------------------------------------------------------
        # VÍ DỤ 3 (Mức Vận dụng thấp): Các tháng có 30 ngày (~20s)
        # -------------------------------------------------------------
        vd3_rect = RoundedRectangle(corner_radius=0.25, width=12.0, height=2.4, stroke_color=COLOR_INDIGO, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.9)
        vd3_badge = Text("VÍ DỤ 3 (Vận dụng):", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_INDIGO)
        vd3_req = Text("Viết tập hợp C các tháng có đúng 30 ngày trong năm dương lịch.", font=FONT_FAMILY, font_size=17, color=COLOR_TEXT_MAIN)
        vd3_top = VGroup(vd3_badge, vd3_req).arrange(RIGHT, buff=0.3)
        
        vd3_sol1 = Text("• Phân tích: Trong 12 tháng dương lịch, chỉ có đúng 4 tháng có đúng 30 ngày.", font=FONT_FAMILY, font_size=15, color=COLOR_AMBER)
        vd3_sol2 = Text("✓ Lời giải:  C = { Tháng 4; Tháng 6; Tháng 9; Tháng 11 }", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_EMERALD)
        
        vd3_content = VGroup(vd3_top, vd3_sol1, vd3_sol2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        vd3_box = VGroup(vd3_rect, vd3_content).next_to(header_group, DOWN, buff=0.35)

        self.play(FadeIn(vd3_box, shift=DOWN), run_time=1.2)
        self.wait(16.0)  # Thầy giảng VD3

        # -------------------------------------------------------------
        # VÍ DỤ 4 (Mức Vận dụng cao): Số có 2 chữ số tổng bằng 5 (~25s)
        # -------------------------------------------------------------
        vd4_rect = RoundedRectangle(corner_radius=0.25, width=12.0, height=2.6, stroke_color=COLOR_AMBER, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.9)
        vd4_badge = Text("VÍ DỤ 4 (Vận dụng cao):", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_AMBER)
        vd4_req = Text("Viết tập hợp D các số tự nhiên có hai chữ số mà tổng các chữ số bằng 5.", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT_MAIN)
        vd4_top = VGroup(vd4_badge, vd4_req).arrange(RIGHT, buff=0.3)
        
        vd4_sol1 = Text("• Phân tích: Số dạng ab (a ≠ 0, a + b = 5). Các cặp số: 5+0, 4+1, 3+2, 2+3, 1+4", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT_MAIN)
        vd4_sol2 = Text("✓ Lời giải:  D = { 14; 23; 32; 41; 50 }   (Gồm 5 phần tử)", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_CYAN)
        
        vd4_content = VGroup(vd4_top, vd4_sol1, vd4_sol2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        vd4_box = VGroup(vd4_rect, vd4_content).next_to(vd3_box, DOWN, buff=0.25)

        self.play(FadeIn(vd4_box, shift=UP), run_time=1.2)
        self.wait(20.0)  # Thầy giảng VD4

        # Chờ khớp đủ thời lượng
        rem_time = max(1.0, target_duration - 108.0)
        self.wait(rem_time)


if __name__ == "__main__":
    pass
