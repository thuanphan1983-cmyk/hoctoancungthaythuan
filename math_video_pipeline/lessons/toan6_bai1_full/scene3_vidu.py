"""
SCENE 3: BA VÍ DỤ MINH HỌA & ĐỒNG HỒ ĐẾM NGƯỢC 45 GIÂY
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn: 3 ví dụ lớn, 3 lần đếm ngược 45s kèm thanh progress bar, Font size >= 28
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


class Scene3ViDu(Scene):
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

        header = Text("PHẦN 3: BA VÍ DỤ MINH HỌA & TỰ RÈN LUYỆN", font=FONT_FAMILY, font_size=34, weight=BOLD, color=COLOR_AMBER)
        header_line = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=COLOR_AMBER)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # =============================================================
        # VÍ DỤ 1 (Nhận biết): TỪ "HỌC TOÁN"
        # =============================================================
        t_ex1_intro = timing.get("scene3_ex1_intro", 28.0)
        t_ex1_sol = timing.get("scene3_ex1_sol", 46.0)

        # 1. Đề bài VD1
        c1_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        badge1 = Text("VÍ DỤ 1 (Mức Nhận Biết)", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_CYAN)
        head1 = Text("CÁC CHỮ CÁI TRONG CỤM TỪ 'HỌC TOÁN'", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_AMBER)
        q1_t1 = Text("Đề bài: Viết tập hợp M gồm các chữ cái trong cụm từ 'HỌC TOÁN'", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        q1_t2 = Text("và điền ký hiệu thuộc (∈), không thuộc (∉) thích hợp vào chỗ trống.", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        
        top1 = VGroup(badge1, head1, q1_t1, q1_t2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        top1.move_to([0, 0.7, 0])

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(top1), run_time=1.2)
        
        rem_intro1 = max(1.0, t_ex1_intro - 2.0)
        self.wait(rem_intro1)

        # 2. Thanh đếm ngược 45s
        t_bar_bg = RoundedRectangle(corner_radius=0.15, width=8.2, height=0.45, stroke_color=COLOR_AMBER, stroke_width=1, fill_color="#0f172a", fill_opacity=0.8).move_to([0, -0.7, 0])
        t_bar_fill = Rectangle(width=8.0, height=0.35, fill_color=COLOR_AMBER, fill_opacity=0.9, stroke_width=0).move_to([0, -0.7, 0])
        t_label = Text("⏰ THỜI GIAN TỰ SUY NGHĨ: 45 GIÂY", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_AMBER).next_to(t_bar_bg, UP, buff=0.15)
        timer1_grp = VGroup(t_bar_bg, t_bar_fill, t_label)

        self.play(FadeIn(timer1_grp), run_time=0.8)
        # Rút ngắn thanh thời gian trong 44.2 giây (khớp 45s audio)
        self.play(t_bar_fill.animate.stretch_to_fit_width(0.01, about_edge=LEFT), run_time=44.2, rate_func=linear)

        # Hết giờ đếm ngược
        t_done = Text("⏰ HẾT GIỜ! CÙNG QUAN SÁT LỜI GIẢI CHI TIẾT", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_EMERALD).move_to(t_label.get_center())
        self.play(Transform(t_label, t_done), run_time=0.8)
        self.wait(1.5)

        # 3. Lời giải VD1 (Thu gọn phần đề để hiển thị lời giải)
        self.play(FadeOut(timer1_grp), top1.animate.shift(UP * 0.4).scale(0.95), run_time=0.8)

        sol1_1 = Text("✓ Lời giải:  M = { H; O; C; T; A; N }  (Chữ O lặp lại → ghi 1 lần)", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_EMERALD)
        sol1_2 = Text("✓ Điền ký hiệu:   H ∈ M  ;   T ∈ M  ;   B ∉ M  ;   K ∉ M", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN)
        sol1_grp = VGroup(sol1_1, sol1_2).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -1.0, 0])

        self.play(FadeIn(sol1_grp, shift=UP), run_time=1.2)
        rem_sol1 = max(1.0, t_ex1_sol - 4.3)
        self.wait(rem_sol1)

        # Chuyển slide sang VD2
        self.play(FadeOut(c1_box), FadeOut(top1), FadeOut(sol1_grp), run_time=0.8)

        # =============================================================
        # VÍ DỤ 2 (Thông hiểu): ĐIỀU KIỆN BIÊN CỦA SỐ TỰ NHIÊN
        # =============================================================
        t_ex2_intro = timing.get("scene3_ex2_intro", 28.0)
        t_ex2_sol = timing.get("scene3_ex2_sol", 46.0)

        c2_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        badge2 = Text("VÍ DỤ 2 (Mức Thông Hiểu)", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_EMERALD)
        head2 = Text("ĐIỀU KIỆN BIÊN CỦA TẬP HỢP SỐ TỰ NHIÊN", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_CYAN)
        q2_t1 = Text("Đề bài: Cho tập hợp  A = { x ∈ ℕ | 12 ≤ x < 18 }.", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_AMBER)
        q2_t2 = Text("Hãy viết tập hợp A bằng cách liệt kê phần tử và tính số phần tử của A.", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)

        top2 = VGroup(badge2, head2, q2_t1, q2_t2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        top2.move_to([0, 0.7, 0])

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(top2), run_time=1.2)

        rem_intro2 = max(1.0, t_ex2_intro - 2.0)
        self.wait(rem_intro2)

        # Đếm ngược 45s VD2
        t_bar_fill2 = Rectangle(width=8.0, height=0.35, fill_color=COLOR_EMERALD, fill_opacity=0.9, stroke_width=0).move_to([0, -0.7, 0])
        t_label2 = Text("⏰ THỜI GIAN TỰ SUY NGHĨ: 45 GIÂY", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_EMERALD).next_to(t_bar_bg, UP, buff=0.15)
        timer2_grp = VGroup(t_bar_bg, t_bar_fill2, t_label2)

        self.play(FadeIn(timer2_grp), run_time=0.8)
        self.play(t_bar_fill2.animate.stretch_to_fit_width(0.01, about_edge=LEFT), run_time=44.2, rate_func=linear)

        t_done2 = Text("⏰ HẾT GIỜ! CÙNG QUAN SÁT LỜI GIẢI CHI TIẾT", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_AMBER).move_to(t_label2.get_center())
        self.play(Transform(t_label2, t_done2), run_time=0.8)
        self.wait(1.5)

        # Lời giải VD2
        self.play(FadeOut(timer2_grp), top2.animate.shift(UP * 0.4).scale(0.95), run_time=0.8)

        sol2_1 = Text("• Phân tích: x ≥ 12 (lấy số 12)  và  x < 18 (dừng ở 17)", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        sol2_2 = Text("✓ Lời giải:  A = { 12; 13; 14; 15; 16; 17 }", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_CYAN)
        sol2_3 = Text("✓ Kết luận: Tập hợp A có đúng 6 phần tử.", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_EMERALD)
        sol2_grp = VGroup(sol2_1, sol2_2, sol2_3).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to([0, -1.0, 0])

        self.play(FadeIn(sol2_grp, shift=UP), run_time=1.2)
        rem_sol2 = max(1.0, t_ex2_sol - 4.3)
        self.wait(rem_sol2)

        # Chuyển slide sang VD3
        self.play(FadeOut(c2_box), FadeOut(top2), FadeOut(sol2_grp), run_time=0.8)

        # =============================================================
        # VÍ DỤ 3 (Vận dụng): TẬP HỢP SỐ CÓ QUY LUẬT CHỮ SỐ
        # =============================================================
        t_ex3_intro = timing.get("scene3_ex3_intro", 30.0)
        t_ex3_sol = timing.get("scene3_ex3_sol", 52.0)

        c3_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        badge3 = Text("VÍ DỤ 3 (Mức Vận Dụng Cao)", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_ROSE)
        head3 = Text("SỐ TỰ NHIÊN THỎA MÃN ĐIỀU KIỆN CHỮ SỐ", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_AMBER)
        q3_t1 = Text("Đề bài: Viết tập hợp B các số tự nhiên có hai chữ số", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        q3_t2 = Text("sao cho chữ số hàng chục gấp 2 lần chữ số hàng đơn vị.", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN)

        top3 = VGroup(badge3, head3, q3_t1, q3_t2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        top3.move_to([0, 0.7, 0])

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(top3), run_time=1.2)

        rem_intro3 = max(1.0, t_ex3_intro - 2.0)
        self.wait(rem_intro3)

        # Đếm ngược 45s VD3
        t_bar_fill3 = Rectangle(width=8.0, height=0.35, fill_color=COLOR_ROSE, fill_opacity=0.9, stroke_width=0).move_to([0, -0.7, 0])
        t_label3 = Text("⏰ THỜI GIAN TỰ SUY NGHĨ: 45 GIÂY", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_ROSE).next_to(t_bar_bg, UP, buff=0.15)
        timer3_grp = VGroup(t_bar_bg, t_bar_fill3, t_label3)

        self.play(FadeIn(timer3_grp), run_time=0.8)
        self.play(t_bar_fill3.animate.stretch_to_fit_width(0.01, about_edge=LEFT), run_time=44.2, rate_func=linear)

        t_done3 = Text("⏰ HẾT GIỜ! CÙNG QUAN SÁT LỜI GIẢI CHI TIẾT", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_CYAN).move_to(t_label3.get_center())
        self.play(Transform(t_label3, t_done3), run_time=0.8)
        self.wait(1.5)

        # Lời giải VD3
        self.play(FadeOut(timer3_grp), top3.animate.shift(UP * 0.4).scale(0.95), run_time=0.8)

        sol3_1 = Text("• Phân tích: Số dạng ab (a ≠ 0 ; a = 2b ; a ≤ 9)", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        sol3_2 = Text("• Các trường hợp: b ∈ {1; 2; 3; 4} → a ∈ {2; 4; 6; 8}", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        sol3_3 = Text("✓ Lời giải:   B = { 21; 42; 63; 84 }   (Đúng 4 phần tử)", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_EMERALD)
        sol3_grp = VGroup(sol3_1, sol3_2, sol3_3).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to([0, -1.0, 0])

        self.play(FadeIn(sol3_grp, shift=UP), run_time=1.2)
        rem_sol3 = max(1.0, t_ex3_sol - 4.3)
        self.wait(rem_sol3)


if __name__ == "__main__":
    pass
