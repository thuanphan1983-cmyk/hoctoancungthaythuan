"""
SCENE 3: BA VÍ DỤ MINH HỌA & ĐỒNG HỒ ĐẾM NGƯỢC 45 GIÂY
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn:
- 3 ví dụ lớn phân cấp Nhận biết -> Thông hiểu -> Vận dụng
- Đồng hồ đếm ngược nhỏ gọn, tinh tế ở GÓC TRÊN BÊN PHẢI (UR), không che đề bài
- Đề bài và giả thiết (kèm câu hỏi điền khuyết) hiển thị nguyên vẹn 100% trong suốt thời gian làm bài
- Căn chỉnh an toàn độ rộng chữ width <= 11.0, không tràn viền bo góc
- Ký hiệu toán học ∈, ∉, ℕ, ≤, ≥, { }, ✓ dùng Segoe UI Symbol sắc nét 100%
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
MATH_FONT = "Segoe UI Symbol"


def math_text(expr, font_size=26, color=COLOR_TEXT_MAIN, weight=BOLD):
    """Render biểu thức và ký hiệu toán học chuẩn xác, sắc nét bằng Segoe UI Symbol"""
    return Text(expr, font=MATH_FONT, font_size=font_size, weight=weight, color=color)


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

        # Header cố định ở góc trên bên trái (UL), nhường góc phải (UR) cho đồng hồ đếm ngược
        header = Text("PHẦN 3: BA VÍ DỤ MINH HỌA & TỰ RÈN LUYỆN", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_AMBER).to_corner(UL, buff=0.45)
        header_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=2, color=COLOR_AMBER).next_to(header, DOWN, buff=0.1, aligned_edge=LEFT)
        header_group = VGroup(header, header_line)
        self.play(FadeIn(header_group, shift=RIGHT), run_time=1.0)

        # =============================================================
        # VÍ DỤ 1 (Nhận biết): TỪ "HỌC TOÁN"
        # =============================================================
        t_ex1_intro = timing.get("scene3_ex1_intro", 27.168)
        t_ex1_timer = timing.get("scene3_ex1_timer", 45.0)
        t_ex1_sol = timing.get("scene3_ex1_sol", 45.768)

        # Khung thẻ chính (chiều rộng 12.2, chiều cao 5.6, đặt tại y = -0.45)
        c1_box = RoundedRectangle(
            corner_radius=0.3,
            width=12.2,
            height=5.6,
            stroke_color=COLOR_CYAN,
            stroke_width=2,
            fill_color=COLOR_CARD,
            fill_opacity=0.95
        ).move_to([0, -0.45, 0])

        # BƯỚC 1: ĐỀ BÀI HOÀN CHỈNH KÈM CÂU HỎI ĐIỀN KHUYẾT
        badge1 = Text("VÍ DỤ 1 (Mức Nhận Biết)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_CYAN)
        head1 = Text("CÁC CHỮ CÁI TRONG CỤM TỪ 'HỌC TOÁN'", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_AMBER)
        sep1 = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_CYAN)

        q1_lead = Text("Đề bài: Cho cụm từ 'HỌC TOÁN'.", font=FONT_FAMILY, font_size=23, weight=BOLD, color=COLOR_TEXT_MAIN)
        q1_a = Text("a) Viết tập hợp M gồm các chữ cái trong cụm từ này.", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN)
        q1_b = VGroup(
            Text("b) Điền ký hiệu ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN),
            math_text("∈", font_size=25, color=COLOR_EMERALD),
            Text(" hoặc ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN),
            math_text("∉", font_size=25, color=COLOR_ROSE),
            Text(" thích hợp vào chỗ trống:", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN)
        ).arrange(RIGHT, buff=0.08)

        # Khung chứa các chỗ trống điền khuyết nổi bật
        b_h = Text("H [ ... ] M", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        b_t = Text("T [ ... ] M", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        b_b = Text("B [ ... ] M", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        b_k = Text("K [ ... ] M", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        def sep(): return Text(";", font=FONT_FAMILY, font_size=22, color=COLOR_TEXT_MUTED)
        q1_blank_txt = VGroup(b_h, sep(), b_t, sep(), b_b, sep(), b_k).arrange(RIGHT, buff=0.25)
        q1_blank_box = RoundedRectangle(
            corner_radius=0.15,
            width=q1_blank_txt.width + 0.6,
            height=0.55,
            stroke_color=COLOR_AMBER,
            stroke_width=1,
            fill_color="#0f172a",
            fill_opacity=0.9
        ).move_to(q1_blank_txt.get_center())
        q1_blank_grp = VGroup(q1_blank_box, q1_blank_txt)

        problem1_grp = VGroup(badge1, head1, sep1, q1_lead, q1_a, q1_b, q1_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        problem1_grp.move_to([0, 0.50, 0])

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(problem1_grp, shift=DOWN * 0.2), run_time=1.2)
        rem_intro1 = max(0.1, t_ex1_intro - 2.0)
        self.wait(rem_intro1)

        # BƯỚC 2: ĐỒNG HỒ ĐẾM NGƯỢC 45 GIÂY (Góc UR - Giữ nguyên đề bài & câu hỏi điền khuyết)
        badge_t1, vt1, text_t1, pbg_t1, pfill_t1 = build_timer_widget(COLOR_AMBER)
        self.play(FadeIn(badge_t1), FadeIn(pbg_t1), FadeIn(pfill_t1), FadeIn(text_t1), run_time=0.8)
        # Đếm ngược chạy lùi trong 44.2 giây (khớp chính xác 45s audio)
        self.play(vt1.animate.set_value(0), run_time=max(1.0, t_ex1_timer - 0.8), rate_func=linear)

        # BƯỚC 3: LỜI GIẢI CHI TIẾT SAU KHI HẾT GIỜ (Đề bài giữ nguyên vị trí, hiển thị lời giải ngay bên dưới)
        self.play(FadeOut(badge_t1), FadeOut(pbg_t1), FadeOut(pfill_t1), FadeOut(text_t1), run_time=0.8)

        sol1_sep = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_EMERALD)
        sol1_anal = VGroup(
            Text("• Phân tích: ", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_TEXT_MUTED),
            Text("Các chữ cái H, O, C, T, O, A, N (chữ O lặp lại → chỉ ghi 1 lần)", font=FONT_FAMILY, font_size=22, color=COLOR_TEXT_MAIN)
        ).arrange(RIGHT, buff=0.08)

        sol1_a = VGroup(
            math_text("✓", font_size=24, color=COLOR_EMERALD),
            Text(" Lời giải a:  ", font=FONT_FAMILY, font_size=23, weight=BOLD, color=COLOR_EMERALD),
            math_text("M = { H; O; C; T; A; N }", font_size=24, color=COLOR_AMBER),
            Text("  (Tập hợp M gồm đúng 6 phần tử)", font=FONT_FAMILY, font_size=21, color=COLOR_TEXT_MUTED)
        ).arrange(RIGHT, buff=0.1)

        sol1_b = VGroup(
            math_text("✓", font_size=24, color=COLOR_CYAN),
            Text(" Lời giải b:  ", font=FONT_FAMILY, font_size=23, weight=BOLD, color=COLOR_CYAN),
            math_text("H ∈ M", font_size=24, color=COLOR_EMERALD),
            Text("  ;  ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MUTED),
            math_text("T ∈ M", font_size=24, color=COLOR_EMERALD),
            Text("  ;  ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MUTED),
            math_text("B ∉ M", font_size=24, color=COLOR_ROSE),
            Text("  ;  ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MUTED),
            math_text("K ∉ M", font_size=24, color=COLOR_ROSE),
        ).arrange(RIGHT, buff=0.08)

        sol1_block = VGroup(sol1_sep, sol1_anal, sol1_a, sol1_b).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        sol1_block.move_to([0, -1.95, 0])

        self.play(FadeIn(sol1_block, shift=UP * 0.2), run_time=1.2)
        rem_sol1 = max(0.1, t_ex1_sol - 2.0)
        self.wait(rem_sol1)

        # Chuyển slide sang VD2
        self.play(FadeOut(c1_box), FadeOut(problem1_grp), FadeOut(sol1_block), run_time=0.8)

        # =============================================================
        # VÍ DỤ 2 (Thông hiểu): ĐIỀU KIỆN BIÊN CỦA SỐ TỰ NHIÊN
        # =============================================================
        t_ex2_intro = timing.get("scene3_ex2_intro", 25.848)
        t_ex2_timer = timing.get("scene3_ex2_timer", 45.0)
        t_ex2_sol = timing.get("scene3_ex2_sol", 51.408)

        c2_box = RoundedRectangle(
            corner_radius=0.3,
            width=12.2,
            height=5.5,
            stroke_color=COLOR_EMERALD,
            stroke_width=2,
            fill_color=COLOR_CARD,
            fill_opacity=0.95
        ).move_to([0, -0.45, 0])

        badge2 = Text("VÍ DỤ 2 (Mức Thông Hiểu)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_EMERALD)
        head2 = Text("ĐIỀU KIỆN BIÊN CỦA TẬP HỢP SỐ TỰ NHIÊN", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_CYAN)
        sep2 = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_EMERALD)
        q2_t1 = VGroup(
            Text("Đề bài: Cho tập hợp  ", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN),
            math_text("A = { x ∈ ℕ | 12 ≤ x < 18 }", font_size=26, color=COLOR_AMBER)
        ).arrange(RIGHT, buff=0.15)
        q2_t2 = Text("Hãy viết tập hợp A bằng cách liệt kê phần tử và tính số phần tử của A.", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN)

        top2 = VGroup(badge2, head2, sep2, q2_t1, q2_t2).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to([0, 0.85, 0])

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(top2, shift=DOWN * 0.2), run_time=1.2)
        rem_intro2 = max(0.1, t_ex2_intro - 2.0)
        self.wait(rem_intro2)

        # 2. Đồng hồ đếm ngược 45s tại góc trên bên phải (UR)
        badge_t2, vt2, text_t2, pbg_t2, pfill_t2 = build_timer_widget(COLOR_EMERALD)
        self.play(FadeIn(badge_t2), FadeIn(pbg_t2), FadeIn(pfill_t2), FadeIn(text_t2), run_time=0.8)
        self.play(vt2.animate.set_value(0), run_time=max(1.0, t_ex2_timer - 0.8), rate_func=linear)

        # 3. Lời giải VD2
        self.play(FadeOut(badge_t2), FadeOut(pbg_t2), FadeOut(pfill_t2), FadeOut(text_t2), run_time=0.8)

        sol2_1 = VGroup(
            Text("• Phân tích: ", font=FONT_FAMILY, font_size=23, weight=BOLD, color=COLOR_TEXT_MUTED),
            math_text("x ≥ 12", font_size=23, color=COLOR_CYAN),
            Text(" (lấy cả số 12)  và  ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN),
            math_text("x < 18", font_size=23, color=COLOR_CYAN),
            Text(" (dừng ở số 17)", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN)
        ).arrange(RIGHT, buff=0.1)

        sol2_2 = VGroup(
            math_text("✓", font_size=24, color=COLOR_CYAN),
            Text(" Liệt kê phần tử:  ", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_CYAN),
            math_text("A = { 12; 13; 14; 15; 16; 17 }", font_size=26, color=COLOR_AMBER)
        ).arrange(RIGHT, buff=0.15)

        sol2_3 = VGroup(
            math_text("✓", font_size=24, color=COLOR_EMERALD),
            Text(" Kết luận: Tập hợp A có đúng 6 phần tử.", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_EMERALD)
        ).arrange(RIGHT, buff=0.12)

        sol2_grp = VGroup(sol2_1, sol2_2, sol2_3).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to([0, -1.45, 0])

        self.play(FadeIn(sol2_grp, shift=UP * 0.3), run_time=1.2)
        rem_sol2 = max(0.1, t_ex2_sol - 2.8)
        self.wait(rem_sol2)

        # Chuyển slide sang VD3
        self.play(FadeOut(c2_box), FadeOut(top2), FadeOut(sol2_grp), run_time=0.8)

        # =============================================================
        # VÍ DỤ 3 (Vận dụng): TẬP HỢP SỐ CÓ QUY LUẬT CHỮ SỐ
        # =============================================================
        t_ex3_intro = timing.get("scene3_ex3_intro", 26.328)
        t_ex3_timer = timing.get("scene3_ex3_timer", 45.0)
        t_ex3_sol = timing.get("scene3_ex3_sol", 62.952)

        c3_box = RoundedRectangle(
            corner_radius=0.3,
            width=12.2,
            height=5.5,
            stroke_color=COLOR_AMBER,
            stroke_width=2,
            fill_color=COLOR_CARD,
            fill_opacity=0.95
        ).move_to([0, -0.45, 0])

        badge3 = Text("VÍ DỤ 3 (Mức Vận Dụng Cao)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_ROSE)
        head3 = Text("SỐ TỰ NHIÊN THỎA MÃN ĐIỀU KIỆN CHỮ SỐ", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_AMBER)
        sep3 = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_ROSE)
        q3_t1 = Text("Đề bài: Viết tập hợp B các số tự nhiên có hai chữ số sao cho", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        q3_t2 = Text("chữ số hàng chục gấp 2 lần chữ số hàng đơn vị.", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_CYAN)

        top3 = VGroup(badge3, head3, sep3, q3_t1, q3_t2).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to([0, 0.85, 0])

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(top3, shift=DOWN * 0.2), run_time=1.2)
        rem_intro3 = max(0.1, t_ex3_intro - 2.0)
        self.wait(rem_intro3)

        # 2. Đồng hồ đếm ngược 45s tại góc trên bên phải (UR)
        badge_t3, vt3, text_t3, pbg_t3, pfill_t3 = build_timer_widget(COLOR_ROSE)
        self.play(FadeIn(badge_t3), FadeIn(pbg_t3), FadeIn(pfill_t3), FadeIn(text_t3), run_time=0.8)
        self.play(vt3.animate.set_value(0), run_time=max(1.0, t_ex3_timer - 0.8), rate_func=linear)

        # 3. Lời giải VD3
        self.play(FadeOut(badge_t3), FadeOut(pbg_t3), FadeOut(pfill_t3), FadeOut(text_t3), run_time=0.8)

        sol3_1 = VGroup(
            Text("• Phân tích: Số hai chữ số dạng ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN),
            math_text("ab", font_size=23, color=COLOR_CYAN),
            Text(" với ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN),
            math_text("a ≠ 0", font_size=23, color=COLOR_CYAN),
            Text(", ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN),
            math_text("a = 2b", font_size=23, color=COLOR_AMBER),
            Text(", ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN),
            math_text("a ≤ 9", font_size=23, color=COLOR_CYAN)
        ).arrange(RIGHT, buff=0.08)

        sol3_2 = VGroup(
            Text("• Các giá trị: ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN),
            math_text("b ∈ { 1; 2; 3; 4 }", font_size=23, color=COLOR_CYAN),
            Text("  suy ra  ", font=FONT_FAMILY, font_size=23, color=COLOR_TEXT_MAIN),
            math_text("a ∈ { 2; 4; 6; 8 }", font_size=23, color=COLOR_CYAN)
        ).arrange(RIGHT, buff=0.1)

        sol3_3 = VGroup(
            math_text("✓", font_size=24, color=COLOR_EMERALD),
            Text(" Lời giải:  ", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_EMERALD),
            math_text("B = { 21; 42; 63; 84 }", font_size=26, color=COLOR_EMERALD),
            Text("  (Tập hợp B gồm đúng 4 phần tử)", font=FONT_FAMILY, font_size=22, color=COLOR_TEXT_MUTED)
        ).arrange(RIGHT, buff=0.15)

        sol3_grp = VGroup(sol3_1, sol3_2, sol3_3).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to([0, -1.45, 0])

        self.play(FadeIn(sol3_grp, shift=UP * 0.3), run_time=1.2)
        rem_sol3 = max(0.1, t_ex3_sol - 2.0)
        self.wait(rem_sol3)


if __name__ == "__main__":
    pass
