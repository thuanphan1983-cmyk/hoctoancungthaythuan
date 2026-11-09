"""
SCENE 3: BA VÍ DỤ MINH HỌA & ĐỒNG HỒ ĐẾM NGƯỢC 45 GIÂY (BÀI 2 FULL)
Bài 2: Cách ghi số tự nhiên (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn:
- 3 ví dụ lớn phân cấp Nhận biết -> Thông hiểu -> Vận dụng cao
- Đồng hồ đếm ngược nhỏ gọn, tinh tế ở GÓC TRÊN BÊN PHẢI (UR), không che đề bài
- Đề bài và chỗ trống hiển thị nguyên vẹn trong suốt thời gian học sinh tự làm bài
- Căn chỉnh an toàn độ rộng chữ <= 11.2, không tràn viền bo góc
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

FONT_FAMILY = "Arial Unicode MS"


def build_timer_widget(theme_color=COLOR_AMBER):
    """Tạo đồng hồ đếm ngược 45s nhỏ gọn tinh tế ở góc trên bên phải (UR)"""
    badge = RoundedRectangle(
        corner_radius=0.2,
        width=2.5,
        height=0.9,
        stroke_color=theme_color,
        stroke_width=2,
        fill_color="#0f172a",
        fill_opacity=0.95
    ).to_corner(UR, buff=0.45)

    vt = ValueTracker(45)
    timer_text = always_redraw(
        lambda: Text(
            f"⏱ {max(0, int(round(vt.get_value()))):02d}s",
            font="Segoe UI",
            font_size=26,
            weight=BOLD,
            color=theme_color
        ).move_to(badge.get_center() + UP * 0.1)
    )

    pbar_bg = Rectangle(
        width=2.1,
        height=0.08,
        fill_color="#334155",
        fill_opacity=1,
        stroke_width=0
    ).move_to(badge.get_center() + DOWN * 0.25)

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

        # =============================================================
        # VÍ DỤ 1 (Nhận biết): ĐỌC VÀ VIẾT SỐ LA MÃ
        # =============================================================
        t_ex1_intro = timing.get("scene3_ex1_intro", 25.0)
        t_ex1_timer = timing.get("scene3_ex1_timer", 45.0)
        t_ex1_sol = timing.get("scene3_ex1_sol", 35.0)

        c1_box = RoundedRectangle(
            corner_radius=0.3,
            width=12.2,
            height=5.6,
            stroke_color=COLOR_CYAN,
            stroke_width=2,
            fill_color=COLOR_CARD,
            fill_opacity=0.95
        ).move_to([0, -0.45, 0])

        badge1 = Text("VÍ DỤ 1 (Mức Nhận Biết)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_CYAN)
        head1 = Text("ĐỌC VÀ VIẾT CHỮ SỐ LA MÃ CHUẨN XÁC", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_AMBER)
        sep1 = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_CYAN)

        q1_lead = Text("Đề bài: Cho các số La Mã: XIV, XIX, XXIV, XXVIII.", font=FONT_FAMILY, font_size=23, weight=BOLD, color=COLOR_TEXT_MAIN)
        q1_a = Text("a) Đọc giá trị số tự nhiên tương ứng của từng số La Mã trên.", font=FONT_FAMILY, font_size=22, color=COLOR_TEXT_MAIN)
        q1_b = Text("b) Điền giá trị thích hợp vào chỗ trống:", font=FONT_FAMILY, font_size=22, color=COLOR_TEXT_MAIN)

        b_1 = Text("XIV = [ ... ]", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        b_2 = Text("XIX = [ ... ]", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        b_3 = Text("XXIV = [ ... ]", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        b_4 = Text("XXVIII = [ ... ]", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        def sep(): return Text(" ; ", font=FONT_FAMILY, font_size=22, color=COLOR_TEXT_MUTED)
        q1_blank_txt = VGroup(b_1, sep(), b_2, sep(), b_3, sep(), b_4).arrange(RIGHT, buff=0.15)
        q1_blank_box = RoundedRectangle(
            corner_radius=0.15,
            width=q1_blank_txt.width + 0.5,
            height=0.55,
            stroke_color=COLOR_AMBER,
            stroke_width=1,
            fill_color="#0f172a",
            fill_opacity=0.9
        ).move_to(q1_blank_txt.get_center())
        q1_blank_grp = VGroup(q1_blank_box, q1_blank_txt)

        prob1_grp = VGroup(badge1, head1, sep1, q1_lead, q1_a, q1_b, q1_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        prob1_grp.move_to([0, 0.85, 0])

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(badge1), FadeIn(head1), Create(sep1), run_time=0.8)
        self.play(FadeIn(q1_lead, shift=RIGHT), FadeIn(q1_a, shift=RIGHT), run_time=1.0)
        self.play(FadeIn(q1_b, shift=RIGHT), FadeIn(q1_blank_grp, scale=1.03), run_time=1.0)

        rem_ex1_intro = max(1.0, t_ex1_intro - 3.6)
        self.wait(rem_ex1_intro)

        # Đồng hồ đếm ngược 45s
        t_badge1, vt1, t_txt1, pb_bg1, pb_fill1 = build_timer_widget(COLOR_AMBER)
        t_grp1 = VGroup(t_badge1, pb_bg1, pb_fill1, t_txt1)
        self.play(FadeIn(t_grp1, shift=DOWN*0.5), run_time=0.8)
        self.play(vt1.animate.set_value(0), run_time=t_ex1_timer - 0.8, rate_func=linear)
        self.play(FadeOut(t_grp1, shift=UP*0.3), run_time=0.6)

        # LỜI GIẢI CHI TIẾT VÍ DỤ 1
        sol1_box = RoundedRectangle(
            corner_radius=0.2,
            width=11.6,
            height=2.2,
            stroke_color=COLOR_EMERALD,
            stroke_width=2,
            fill_color="#0f172a",
            fill_opacity=0.95
        ).move_to([0, -1.95, 0])

        sol1_head = Text("✓ HƯỚNG DẪN GIẢI CHI TIẾT:", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_EMERALD)
        sol1_a = Text("• a) XIV: Mười bốn ; XIX: Mười chín ; XXIV: Hai mươi tư ; XXVIII: Hai mươi tám", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT_MAIN)
        sol1_b = Text("• b) Điền:  XIV = 14  ;  XIX = 19  ;  XXIV = 24  ;  XXVIII = 28", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_CYAN)
        sol1_tip = Text("💡 Nhận xét: Tách hàng chục trước, hàng đơn vị sau: XXIV = 20 + 4 = 24", font=FONT_FAMILY, font_size=19, color=COLOR_AMBER)

        sol1_content = VGroup(sol1_head, sol1_a, sol1_b, sol1_tip).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        sol1_content.move_to(sol1_box.get_center())
        sol1_grp = VGroup(sol1_box, sol1_content)

        self.play(FadeIn(sol1_grp, shift=UP*0.3), run_time=0.8)
        rem_ex1_sol = max(1.0, t_ex1_sol - 0.8)
        self.wait(rem_ex1_sol)

        self.play(FadeOut(sol1_grp), FadeOut(prob1_grp), FadeOut(c1_box), run_time=0.8)

        # =============================================================
        # VÍ DỤ 2 (Thông hiểu): CẤU TẠO SỐ HỆ THẬP PHÂN
        # =============================================================
        t_ex2_intro = timing.get("scene3_ex2_intro", 25.0)
        t_ex2_timer = timing.get("scene3_ex2_timer", 45.0)
        t_ex2_sol = timing.get("scene3_ex2_sol", 35.0)

        c2_box = RoundedRectangle(
            corner_radius=0.3,
            width=12.2,
            height=5.6,
            stroke_color=COLOR_EMERALD,
            stroke_width=2,
            fill_color=COLOR_CARD,
            fill_opacity=0.95
        ).move_to([0, -0.45, 0])

        badge2 = Text("VÍ DỤ 2 (Mức Thông Hiểu)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_EMERALD)
        head2 = Text("PHÂN TÍCH CẤU TẠO SỐ HỆ THẬP PHÂN", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_AMBER)
        sep2 = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_EMERALD)

        q2_lead = Text("Đề bài: Cho hai số tự nhiên M = 4853 và N = 7029.", font=FONT_FAMILY, font_size=23, weight=BOLD, color=COLOR_TEXT_MAIN)
        q2_a = Text("a) Nêu vị trí hàng và giá trị của chữ số 8 trong M, chữ số 2 trong N.", font=FONT_FAMILY, font_size=22, color=COLOR_TEXT_MAIN)
        q2_b = Text("b) Điền số thích hợp vào chỗ trống để viết dạng tổng giá trị chữ số:", font=FONT_FAMILY, font_size=22, color=COLOR_TEXT_MAIN)

        b2_row1 = Text("4853 = 4 × [ ... ] + 8 × [ ... ] + 5 × [ ... ] + 3", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        b2_row2 = Text("7029 = 7 × [ ... ] + 2 × [ ... ] + 9", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_CYAN)
        q2_blank_txt = VGroup(b2_row1, b2_row2).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        q2_blank_box = RoundedRectangle(
            corner_radius=0.15,
            width=q2_blank_txt.width + 0.5,
            height=1.05,
            stroke_color=COLOR_AMBER,
            stroke_width=1,
            fill_color="#0f172a",
            fill_opacity=0.9
        ).move_to(q2_blank_txt.get_center())
        q2_blank_grp = VGroup(q2_blank_box, q2_blank_txt)

        prob2_grp = VGroup(badge2, head2, sep2, q2_lead, q2_a, q2_b, q2_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.11)
        prob2_grp.move_to([0, 0.85, 0])

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(badge2), FadeIn(head2), Create(sep2), run_time=0.8)
        self.play(FadeIn(q2_lead, shift=RIGHT), FadeIn(q2_a, shift=RIGHT), run_time=1.0)
        self.play(FadeIn(q2_b, shift=RIGHT), FadeIn(q2_blank_grp, scale=1.03), run_time=1.0)

        rem_ex2_intro = max(1.0, t_ex2_intro - 3.6)
        self.wait(rem_ex2_intro)

        # Đồng hồ đếm ngược 45s
        t_badge2, vt2, t_txt2, pb_bg2, pb_fill2 = build_timer_widget(COLOR_EMERALD)
        t_grp2 = VGroup(t_badge2, pb_bg2, pb_fill2, t_txt2)
        self.play(FadeIn(t_grp2, shift=DOWN*0.5), run_time=0.8)
        self.play(vt2.animate.set_value(0), run_time=t_ex2_timer - 0.8, rate_func=linear)
        self.play(FadeOut(t_grp2, shift=UP*0.3), run_time=0.6)

        # LỜI GIẢI CHI TIẾT VÍ DỤ 2
        sol2_box = RoundedRectangle(
            corner_radius=0.2,
            width=11.6,
            height=2.2,
            stroke_color=COLOR_CYAN,
            stroke_width=2,
            fill_color="#0f172a",
            fill_opacity=0.95
        ).move_to([0, -1.95, 0])

        sol2_head = Text("✓ HƯỚNG DẪN GIẢI CHI TIẾT:", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_EMERALD)
        sol2_a = Text("• a) Số 4853: Chữ số 8 thuộc hàng trăm (giá trị 800). Số 7029: Chữ số 2 thuộc hàng chục (giá trị 20).", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT_MAIN)
        sol2_b = Text("• b) 4853 = 4 × 1000 + 8 × 100 + 5 × 10 + 3   ;   7029 = 7 × 1000 + 2 × 10 + 9", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_CYAN)
        sol2_tip = Text("💡 Nhận xét: Trong 7029, chữ số hàng trăm bằng 0 nên có thể viết gọn bỏ qua 0 × 100.", font=FONT_FAMILY, font_size=19, color=COLOR_AMBER)

        sol2_content = VGroup(sol2_head, sol2_a, sol2_b, sol2_tip).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        sol2_content.move_to(sol2_box.get_center())
        sol2_grp = VGroup(sol2_box, sol2_content)

        self.play(FadeIn(sol2_grp, shift=UP*0.3), run_time=0.8)
        rem_ex2_sol = max(1.0, t_ex2_sol - 0.8)
        self.wait(rem_ex2_sol)

        self.play(FadeOut(sol2_grp), FadeOut(prob2_grp), FadeOut(c2_box), run_time=0.8)

        # =============================================================
        # VÍ DỤ 3 (Vận dụng cao): TÌM SỐ TỰ NHIÊN THỎA MÃN ĐIỀU KIỆN
        # =============================================================
        t_ex3_intro = timing.get("scene3_ex3_intro", 25.0)
        t_ex3_timer = timing.get("scene3_ex3_timer", 45.0)
        t_ex3_sol = timing.get("scene3_ex3_sol", 45.0)

        c3_box = RoundedRectangle(
            corner_radius=0.3,
            width=12.2,
            height=5.6,
            stroke_color=COLOR_ROSE,
            stroke_width=2,
            fill_color=COLOR_CARD,
            fill_opacity=0.95
        ).move_to([0, -0.45, 0])

        badge3 = Text("VÍ DỤ 3 (Mức Vận Dụng Cao)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_ROSE)
        head3 = Text("TÌM SỐ TỰ NHIÊN THỎA MÃN ĐIỀU KIỆN CHỮ SỐ", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_AMBER)
        sep3 = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_ROSE)

        q3_lead = Text("Đề bài: Tìm số tự nhiên có 2 chữ số ab biết a = 3b và ab - ba = 54. Viết số đó bằng chữ số La Mã.", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_TEXT_MAIN)
        q3_a = Text("a) Khai triển hiệu ab - ba theo cấu tạo số để tìm quan hệ giữa a và b.", font=FONT_FAMILY, font_size=21, color=COLOR_TEXT_MAIN)
        q3_b = Text("b) Điền số thích hợp vào chỗ trống:", font=FONT_FAMILY, font_size=21, color=COLOR_TEXT_MAIN)

        b3_row1 = Text("a - b = 54 : 9 = [ ... ]   ;   b = [ ... ]  ;  a = [ ... ]", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_AMBER)
        b3_row2 = Text("Số tự nhiên: ab = [ ... ]   ;   Chữ số La Mã = [ ... ]", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_CYAN)
        q3_blank_txt = VGroup(b3_row1, b3_row2).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        q3_blank_box = RoundedRectangle(
            corner_radius=0.15,
            width=q3_blank_txt.width + 0.5,
            height=1.05,
            stroke_color=COLOR_AMBER,
            stroke_width=1,
            fill_color="#0f172a",
            fill_opacity=0.9
        ).move_to(q3_blank_txt.get_center())
        q3_blank_grp = VGroup(q3_blank_box, q3_blank_txt)

        prob3_grp = VGroup(badge3, head3, sep3, q3_lead, q3_a, q3_b, q3_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.11)
        prob3_grp.move_to([0, 0.85, 0])

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(badge3), FadeIn(head3), Create(sep3), run_time=0.8)
        self.play(FadeIn(q3_lead, shift=RIGHT), FadeIn(q3_a, shift=RIGHT), run_time=1.0)
        self.play(FadeIn(q3_b, shift=RIGHT), FadeIn(q3_blank_grp, scale=1.03), run_time=1.0)

        rem_ex3_intro = max(1.0, t_ex3_intro - 3.6)
        self.wait(rem_ex3_intro)

        # Đồng hồ đếm ngược 45s
        t_badge3, vt3, t_txt3, pb_bg3, pb_fill3 = build_timer_widget(COLOR_ROSE)
        t_grp3 = VGroup(t_badge3, pb_bg3, pb_fill3, t_txt3)
        self.play(FadeIn(t_grp3, shift=DOWN*0.5), run_time=0.8)
        self.play(vt3.animate.set_value(0), run_time=t_ex3_timer - 0.8, rate_func=linear)
        self.play(FadeOut(t_grp3, shift=UP*0.3), run_time=0.6)

        # LỜI GIẢI CHI TIẾT VÍ DỤ 3
        sol3_box = RoundedRectangle(
            corner_radius=0.2,
            width=11.6,
            height=2.2,
            stroke_color=COLOR_EMERALD,
            stroke_width=2,
            fill_color="#0f172a",
            fill_opacity=0.95
        ).move_to([0, -1.95, 0])

        sol3_head = Text("✓ HƯỚNG DẪN GIẢI CHI TIẾT:", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_EMERALD)
        sol3_a = Text("• Khai triển: ab - ba = (10a + b) - (10b + a) = 9(a - b) = 54  ⇒  a - b = 6", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT_MAIN)
        sol3_b = Text("• Vì a = 3b  ⇒  3b - b = 6  ⇒  2b = 6  ⇒  b = 3  và  a = 9.  Số cần tìm là 93.", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_CYAN)
        sol3_tip = Text("• Viết dạng La Mã: 93 = 90 + 3 = XC + III = XCIII.", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER)

        sol3_content = VGroup(sol3_head, sol3_a, sol3_b, sol3_tip).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        sol3_content.move_to(sol3_box.get_center())
        sol3_grp = VGroup(sol3_box, sol3_content)

        self.play(FadeIn(sol3_grp, shift=UP*0.3), run_time=0.8)
        rem_ex3_sol = max(1.0, t_ex3_sol - 0.8)
        self.wait(rem_ex3_sol)

        self.play(FadeOut(sol3_grp), FadeOut(prob3_grp), FadeOut(c3_box), run_time=0.8)


if __name__ == "__main__":
    pass
