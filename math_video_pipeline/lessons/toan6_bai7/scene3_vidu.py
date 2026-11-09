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


def build_timer_widget(theme_color=COLOR_AMBER):
    badge = RoundedRectangle(corner_radius=0.15, width=2.4, height=0.85, stroke_color=theme_color, stroke_width=2, fill_color="#0f172a", fill_opacity=0.95).to_corner(UR, buff=0.45)
    vt = ValueTracker(45)
    timer_text = always_redraw(lambda: Text(f"⏱ {int(vt.get_value()):02d}s", font="Segoe UI", font_size=24, weight=BOLD, color=theme_color).move_to(badge.get_center() + UP * 0.1))
    pbar_bg = Rectangle(width=2.1, height=0.08, fill_color="#334155", fill_opacity=1, stroke_width=0).move_to(badge.get_center() + DOWN * 0.25)
    def get_pfill():
        val = max(0.0, min(45.0, vt.get_value()))
        w = max(0.01, 2.1 * (val / 45.0))
        rect = Rectangle(width=w, height=0.08, fill_color=theme_color, fill_opacity=1, stroke_width=0)
        rect.move_to(pbar_bg.get_center())
        rect.align_to(pbar_bg, LEFT)
        return rect
    pbar_fill = always_redraw(get_pfill)
    return badge, vt, timer_text, pbar_bg, pbar_fill


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

        header = Text("PHẦN 3: BA VÍ DỤ MINH HỌA & TỰ RÈN LUYỆN", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_AMBER).to_corner(UL, buff=0.45)
        header_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=2, color=COLOR_AMBER).next_to(header, DOWN, buff=0.1, aligned_edge=LEFT)
        header_group = VGroup(header, header_line)
        self.play(FadeIn(header_group, shift=RIGHT), run_time=1.0)

        # ==================== VÍ DỤ 1 ====================
        t_ex1_intro = timing.get("scene3_ex1_intro", 25.0)
        t_ex1_timer = timing.get("scene3_ex1_timer", 45.0)
        t_ex1_sol = timing.get("scene3_ex1_sol", 40.0)

        c1_box = RoundedRectangle(corner_radius=0.3, width=12.2, height=5.6, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.45, 0])

        badge1 = Text("VÍ DỤ 1 (Mức Nhận Biết)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_CYAN)
        head1 = safe_text("TÍNH GIÁ TRỊ BIỂU THỨC KHÔNG NGOẶC", font_size=25, weight=BOLD, color=COLOR_AMBER, max_width=10.6)
        sep1 = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_CYAN)
        q1_lead = safe_text("Đề bài: Thực hiện phép tính:", font_size=23, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=10.4)
        q1_a = safe_text("a) A = 25 - 5 × 4 + 3²", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4)
        q1_b = safe_text("b) B = 48 : 2³ + 6 × 5", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4)
        bl_sub_1 = []
        bl_sub_1.append(Text("A = 25 - 20 + [ ... ] = [ ... ]", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_AMBER))
        bl_sub_1.append(Text("B = 48 : [ ... ] + 30 = [ ... ]", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_AMBER))
        if bl_sub_1:
            def sep(): return Text("  ;  ", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT_MUTED)
            bl_row = VGroup()
            for i_b, b_elem in enumerate(bl_sub_1):
                if i_b > 0:
                    bl_row.add(sep())
                bl_row.add(b_elem)
            bl_row.arrange(RIGHT, buff=0.1)
            if bl_row.width > 10.2:
                bl_row.scale_to_fit_width(10.2)
            bl_box = RoundedRectangle(corner_radius=0.15, width=bl_row.width + 0.6, height=0.52, stroke_color=COLOR_AMBER, stroke_width=1, fill_color="#0f172a", fill_opacity=0.9).move_to(bl_row.get_center())
            q1_blank_grp = VGroup(bl_box, bl_row)
            problem1_grp = VGroup(badge1, head1, sep1, q1_lead, q1_a, q1_b, q1_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        else:
            problem1_grp = VGroup(badge1, head1, sep1, q1_lead, q1_a, q1_b).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

        problem1_grp.move_to([0, 0.50, 0])

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(problem1_grp, shift=DOWN * 0.2), run_time=1.2)
        rem_intro1 = max(0.1, t_ex1_intro - 2.0)
        self.wait(rem_intro1)

        # BƯỚC 2: ĐỒNG HỒ ĐẾM NGƯỢC 45s GÓC TRÊN BÊN PHẢI UR
        badge_t1, vt1, text_t1, pbg_t1, pfill_t1 = build_timer_widget(COLOR_CYAN)
        self.play(FadeIn(badge_t1), FadeIn(pbg_t1), FadeIn(pfill_t1), FadeIn(text_t1), run_time=0.8)
        self.play(vt1.animate.set_value(0), run_time=max(1.0, t_ex1_timer - 0.8), rate_func=linear)

        # BƯỚC 3: LỜI GIẢI CHI TIẾT (ĐỀ BÀI GIỮ NGUYÊN)
        self.play(FadeOut(badge_t1), FadeOut(pbg_t1), FadeOut(pfill_t1), FadeOut(text_t1), run_time=0.8)

        sol1_sep = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_EMERALD)
        sol1_anal = safe_text("• Phân tích: A = 25 - 20 + 9 = 5 + 9 = 14. B = 48 : 8 + 30 = 6 + 30 = 36.", font_size=21, color=COLOR_TEXT_MUTED, max_width=10.4)
        sol1_a = VGroup(math_text("✓", font_size=22, color=COLOR_EMERALD), safe_text(" a) A = 14.", font_size=22, color=COLOR_EMERALD, max_width=10.0)).arrange(RIGHT, buff=0.08)
        sol1_b = VGroup(math_text("✓", font_size=22, color=COLOR_CYAN), safe_text(" b) B = 36.", font_size=22, color=COLOR_CYAN, max_width=10.0)).arrange(RIGHT, buff=0.08)

        sol1_block = VGroup(sol1_sep, sol1_anal, sol1_a, sol1_b).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        sol1_block.move_to([0, -1.95, 0])

        self.play(FadeIn(sol1_block, shift=UP * 0.2), run_time=1.2)
        rem_sol1 = max(0.1, t_ex1_sol - 2.0)
        self.wait(rem_sol1)

        self.play(FadeOut(c1_box), FadeOut(problem1_grp), FadeOut(sol1_block), run_time=0.8)

        # ==================== VÍ DỤ 2 ====================
        t_ex2_intro = timing.get("scene3_ex2_intro", 25.0)
        t_ex2_timer = timing.get("scene3_ex2_timer", 45.0)
        t_ex2_sol = timing.get("scene3_ex2_sol", 40.0)

        c2_box = RoundedRectangle(corner_radius=0.3, width=12.2, height=5.6, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.45, 0])

        badge2 = Text("VÍ DỤ 2 (Mức Thông Hiểu)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_EMERALD)
        head2 = safe_text("BIỂU THỨC ĐA TẦNG NGOẶC", font_size=25, weight=BOLD, color=COLOR_AMBER, max_width=10.6)
        sep2 = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_EMERALD)
        q2_lead = safe_text("Đề bài: Thực hiện phép tính: C = 120 - [ 40 - ( 8 - 3 )² ]", font_size=23, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=10.4)
        q2_a = safe_text("a) Tính giá trị trong ngoặc tròn ( 8 - 3 )².", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4)
        q2_b = safe_text("b) Tính giá trị toàn bộ biểu thức C.", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4)
        bl_sub_2 = []
        bl_sub_2.append(Text("(8 - 3)² = 5² = [ ... ]", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_AMBER))
        bl_sub_2.append(Text("C = 120 - [ 40 - 25 ] = 120 - [ ... ] = [ ... ]", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_AMBER))
        if bl_sub_2:
            def sep(): return Text("  ;  ", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT_MUTED)
            bl_row = VGroup()
            for i_b, b_elem in enumerate(bl_sub_2):
                if i_b > 0:
                    bl_row.add(sep())
                bl_row.add(b_elem)
            bl_row.arrange(RIGHT, buff=0.1)
            if bl_row.width > 10.2:
                bl_row.scale_to_fit_width(10.2)
            bl_box = RoundedRectangle(corner_radius=0.15, width=bl_row.width + 0.6, height=0.52, stroke_color=COLOR_AMBER, stroke_width=1, fill_color="#0f172a", fill_opacity=0.9).move_to(bl_row.get_center())
            q2_blank_grp = VGroup(bl_box, bl_row)
            problem2_grp = VGroup(badge2, head2, sep2, q2_lead, q2_a, q2_b, q2_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        else:
            problem2_grp = VGroup(badge2, head2, sep2, q2_lead, q2_a, q2_b).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

        problem2_grp.move_to([0, 0.50, 0])

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(problem2_grp, shift=DOWN * 0.2), run_time=1.2)
        rem_intro2 = max(0.1, t_ex2_intro - 2.0)
        self.wait(rem_intro2)

        # BƯỚC 2: ĐỒNG HỒ ĐẾM NGƯỢC 45s GÓC TRÊN BÊN PHẢI UR
        badge_t2, vt2, text_t2, pbg_t2, pfill_t2 = build_timer_widget(COLOR_EMERALD)
        self.play(FadeIn(badge_t2), FadeIn(pbg_t2), FadeIn(pfill_t2), FadeIn(text_t2), run_time=0.8)
        self.play(vt2.animate.set_value(0), run_time=max(1.0, t_ex2_timer - 0.8), rate_func=linear)

        # BƯỚC 3: LỜI GIẢI CHI TIẾT (ĐỀ BÀI GIỮ NGUYÊN)
        self.play(FadeOut(badge_t2), FadeOut(pbg_t2), FadeOut(pfill_t2), FadeOut(text_t2), run_time=0.8)

        sol2_sep = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_EMERALD)
        sol2_anal = safe_text("• Phân tích: (8 - 3) = 5 ⇒ 5² = 25. Trong ngoặc vuông: 40 - 25 = 15. C = 120 - 15 = 105.", font_size=21, color=COLOR_TEXT_MUTED, max_width=10.4)
        sol2_a = VGroup(math_text("✓", font_size=22, color=COLOR_EMERALD), safe_text(" a) (8 - 3)² = 25.", font_size=22, color=COLOR_EMERALD, max_width=10.0)).arrange(RIGHT, buff=0.08)
        sol2_b = VGroup(math_text("✓", font_size=22, color=COLOR_CYAN), safe_text(" b) C = 105.", font_size=22, color=COLOR_CYAN, max_width=10.0)).arrange(RIGHT, buff=0.08)

        sol2_block = VGroup(sol2_sep, sol2_anal, sol2_a, sol2_b).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        sol2_block.move_to([0, -1.95, 0])

        self.play(FadeIn(sol2_block, shift=UP * 0.2), run_time=1.2)
        rem_sol2 = max(0.1, t_ex2_sol - 2.0)
        self.wait(rem_sol2)

        self.play(FadeOut(c2_box), FadeOut(problem2_grp), FadeOut(sol2_block), run_time=0.8)

        # ==================== VÍ DỤ 3 ====================
        t_ex3_intro = timing.get("scene3_ex3_intro", 25.0)
        t_ex3_timer = timing.get("scene3_ex3_timer", 45.0)
        t_ex3_sol = timing.get("scene3_ex3_sol", 40.0)

        c3_box = RoundedRectangle(corner_radius=0.3, width=12.2, height=5.6, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.45, 0])

        badge3 = Text("VÍ DỤ 3 (Mức Vận Dụng)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        head3 = safe_text("TÌM X CÓ NHIỀU PHÉP TÍNH", font_size=25, weight=BOLD, color=COLOR_AMBER, max_width=10.6)
        sep3 = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_AMBER)
        q3_lead = safe_text("Đề bài: Tìm số tự nhiên x biết: 75 - 5 × (x - 3) = 40", font_size=23, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=10.4)
        q3_a = safe_text("a) Tìm giá trị của cụm 5 × (x - 3).", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4)
        q3_b = safe_text("b) Tìm x.", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4)
        bl_sub_3 = []
        bl_sub_3.append(Text("5 × (x - 3) = 75 - 40 = [ ... ]", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_AMBER))
        bl_sub_3.append(Text("x - 3 = 35 : 5 = [ ... ] ⇒ x = [ ... ]", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_AMBER))
        if bl_sub_3:
            def sep(): return Text("  ;  ", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT_MUTED)
            bl_row = VGroup()
            for i_b, b_elem in enumerate(bl_sub_3):
                if i_b > 0:
                    bl_row.add(sep())
                bl_row.add(b_elem)
            bl_row.arrange(RIGHT, buff=0.1)
            if bl_row.width > 10.2:
                bl_row.scale_to_fit_width(10.2)
            bl_box = RoundedRectangle(corner_radius=0.15, width=bl_row.width + 0.6, height=0.52, stroke_color=COLOR_AMBER, stroke_width=1, fill_color="#0f172a", fill_opacity=0.9).move_to(bl_row.get_center())
            q3_blank_grp = VGroup(bl_box, bl_row)
            problem3_grp = VGroup(badge3, head3, sep3, q3_lead, q3_a, q3_b, q3_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        else:
            problem3_grp = VGroup(badge3, head3, sep3, q3_lead, q3_a, q3_b).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

        problem3_grp.move_to([0, 0.50, 0])

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(problem3_grp, shift=DOWN * 0.2), run_time=1.2)
        rem_intro3 = max(0.1, t_ex3_intro - 2.0)
        self.wait(rem_intro3)

        # BƯỚC 2: ĐỒNG HỒ ĐẾM NGƯỢC 45s GÓC TRÊN BÊN PHẢI UR
        badge_t3, vt3, text_t3, pbg_t3, pfill_t3 = build_timer_widget(COLOR_AMBER)
        self.play(FadeIn(badge_t3), FadeIn(pbg_t3), FadeIn(pfill_t3), FadeIn(text_t3), run_time=0.8)
        self.play(vt3.animate.set_value(0), run_time=max(1.0, t_ex3_timer - 0.8), rate_func=linear)

        # BƯỚC 3: LỜI GIẢI CHI TIẾT (ĐỀ BÀI GIỮ NGUYÊN)
        self.play(FadeOut(badge_t3), FadeOut(pbg_t3), FadeOut(pfill_t3), FadeOut(text_t3), run_time=0.8)

        sol3_sep = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_EMERALD)
        sol3_anal = safe_text("• Phân tích: 5(x - 3) = 75 - 40 = 35 ⇒ x - 3 = 35 : 5 = 7 ⇒ x = 10.", font_size=21, color=COLOR_TEXT_MUTED, max_width=10.4)
        sol3_a = VGroup(math_text("✓", font_size=22, color=COLOR_EMERALD), safe_text(" a) 5 × (x - 3) = 35.", font_size=22, color=COLOR_EMERALD, max_width=10.0)).arrange(RIGHT, buff=0.08)
        sol3_b = VGroup(math_text("✓", font_size=22, color=COLOR_CYAN), safe_text(" b) x = 10.", font_size=22, color=COLOR_CYAN, max_width=10.0)).arrange(RIGHT, buff=0.08)

        sol3_block = VGroup(sol3_sep, sol3_anal, sol3_a, sol3_b).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        sol3_block.move_to([0, -1.95, 0])

        self.play(FadeIn(sol3_block, shift=UP * 0.2), run_time=1.2)
        rem_sol3 = max(0.1, t_ex3_sol - 2.0)
        self.wait(rem_sol3)

        self.play(FadeOut(c3_box), FadeOut(problem3_grp), FadeOut(sol3_block), run_time=0.8)

if __name__ == "__main__":
    pass
