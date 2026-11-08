"""
ANIMATION ENGINE (CÔNG CỤ ĐỒ HỌA TOÁN HỌC TRỰC QUAN AI)
Sử dụng Manim Community Edition (manimce v0.22+)
Thiết kế tối ưu đồ họa độ phân giải cao 1080p, bảng đen hiện đại (Dark Slate)
Tự động hỗ trợ tiếng Việt có dấu và ký hiệu toán học Unicode (∈, ∉, ℕ, ≤, ≥, °...)
"""

import sys
import os
import json
from pathlib import Path
from manim import *

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ==============================================================================
# HỆ THỐNG MÀU SẮC ĐỒ HỌA HIỆN ĐẠI (COLOR PALETTE)
# ==============================================================================
COLOR_BG = "#0b1120"          # Nền tối sang trọng (Dark Slate/Navy)
COLOR_CARD = "#1e293b"        # Nền thẻ nổi
COLOR_CYAN = "#38bdf8"        # Xanh ngọc phát sáng (Primary Accent)
COLOR_EMERALD = "#34d399"     # Xanh lá thành công (Thuộc ∈)
COLOR_AMBER = "#fbbf24"       # Vàng hổ phách (Chú ý / Ký hiệu)
COLOR_ROSE = "#f87171"        # Đỏ san hô (Không thuộc ∉)
COLOR_INDIGO = "#818cf8"      # Tím indigo thương hiệu
COLOR_TEXT_MAIN = "#f8fafc"   # Chữ trắng sáng
COLOR_TEXT_MUTED = "#94a3b8"  # Chữ xám ghi chú
FONT_FAMILY = "Arial"         # Font chữ chuẩn hỗ trợ trọn vẹn tiếng Việt có dấu


class BaseMathScene(Scene):
    """Lớp phân cảnh cơ sở cung cấp khung nền, thanh tiêu đề và thương hiệu"""
    def setup(self):
        self.camera.background_color = COLOR_BG
        self.target_duration = getattr(self, "audio_duration", 10.0)
        self.start_sim_time = 0.0

    def add_watermark_brand(self, teacher_name="Thầy Thuấn Phan"):
        """Đính kèm thương hiệu kênh ở góc trên màn hình"""
        brand_dot = Dot(radius=0.08, color=COLOR_CYAN)
        brand_text = Text(
            f"HỌC TOÁN CÙNG {teacher_name.upper()}",
            font=FONT_FAMILY,
            font_size=18,
            weight=BOLD,
            color=COLOR_TEXT_MUTED
        )
        brand_group = VGroup(brand_dot, brand_text).arrange(RIGHT, buff=0.2)
        brand_group.to_corner(UR, buff=0.4)
        self.add(brand_group)
        return brand_group


# ==============================================================================
# PHÂN CẢNH 1: GIỚI THIỆU BÀI GIẢNG (INTRO SCENE)
# ==============================================================================
class IntroScene(BaseMathScene):
    def construct(self):
        cfg = getattr(self, "scene_config", {})
        teacher_name = cfg.get("teacher_name", "Thầy Thuấn Phan")
        channel_title = cfg.get("channel_title", "HỌC TOÁN CÙNG THẦY THUẤN PHAN")
        subject_title = cfg.get("subject_title", "TOÁN 6 • KẾT NỐI TRI THỨC VỚI CUỘC SỐNG")
        lesson_name = cfg.get("lesson_name", "BÀI 1: TẬP HỢP")
        lesson_sub = cfg.get("lesson_sub", "Khái niệm tập hợp & Phần tử của tập hợp")
        duration = getattr(self, "audio_duration", 8.0)

        # 1. Khung trang trí viền phát sáng
        border = RoundedRectangle(
            corner_radius=0.4,
            width=13.0,
            height=7.2,
            stroke_width=2,
            stroke_color=COLOR_INDIGO,
            stroke_opacity=0.4,
            fill_opacity=0
        )
        self.add(border)

        # 2. Header thương hiệu kênh
        brand = Text(
            channel_title,
            font=FONT_FAMILY,
            font_size=22,
            weight=BOLD,
            color=COLOR_AMBER
        )
        brand_line = Line(LEFT * 4, RIGHT * 4, stroke_width=2, color=COLOR_AMBER)
        brand_group = VGroup(brand, brand_line).arrange(DOWN, buff=0.15).to_edge(UP, buff=1.0)

        # 3. Huy hiệu môn học
        subject_badge = RoundedRectangle(
            corner_radius=0.2,
            width=6.5,
            height=0.6,
            stroke_width=1.5,
            stroke_color=COLOR_CYAN,
            fill_color=COLOR_CARD,
            fill_opacity=0.8
        )
        subject_text = Text(
            subject_title,
            font=FONT_FAMILY,
            font_size=16,
            weight=BOLD,
            color=COLOR_CYAN
        ).move_to(subject_badge.get_center())
        subject_group = VGroup(subject_badge, subject_text).next_to(brand_group, DOWN, buff=0.5)

        # 4. Tên bài giảng chính (Tiêu đề lớn nổi bật)
        main_title = Text(
            lesson_name,
            font=FONT_FAMILY,
            font_size=54,
            weight=BOLD,
            color=COLOR_TEXT_MAIN
        ).next_to(subject_group, DOWN, buff=0.6)

        # 5. Phụ đề nội dung bài học
        sub_title = Text(
            lesson_sub,
            font=FONT_FAMILY,
            font_size=24,
            color=COLOR_TEXT_MUTED
        ).next_to(main_title, DOWN, buff=0.35)

        # 6. Đồ họa toán học sinh động làm điểm nhấn (Vòng tròn tập hợp thu nhỏ xoay nhẹ)
        decor_ring = Circle(radius=0.6, stroke_width=3, color=COLOR_CYAN)
        decor_dots = VGroup(*[
            Dot(radius=0.06, color=c).move_to(
                decor_ring.point_at_angle(a)
            ) for a, c in zip([0, PI/2, PI, 3*PI/2], [COLOR_AMBER, COLOR_EMERALD, COLOR_ROSE, COLOR_CYAN])
        ])
        decor_group = VGroup(decor_ring, decor_dots).next_to(sub_title, DOWN, buff=0.6)

        # --- CHẠY HIỆU ỨNG ANIMATIONS (ĐỒNG BỘ THEO GIỌNG NÓI) ---
        t_used = 0.0

        self.play(FadeIn(brand_group, shift=DOWN * 0.3), run_time=1.0)
        t_used += 1.0

        self.play(Create(subject_group), run_time=0.8)
        t_used += 0.8

        self.play(Write(main_title), run_time=1.4)
        t_used += 1.4

        self.play(FadeIn(sub_title, shift=UP * 0.2), FadeIn(decor_group, scale=0.8), run_time=1.0)
        t_used += 1.0

        # Xoay nhẹ vòng trang trí trong thời gian còn lại của audio
        remaining = max(1.0, duration - t_used)
        self.play(
            Rotate(decor_group, angle=2 * PI, run_time=remaining, rate_func=linear)
        )


# ==============================================================================
# PHÂN CẢNH 2: TRỰC QUAN HÓA SƠ ĐỒ VEN & PHẦN TỬ THUỘC / KHÔNG THUỘC (BÀI 1)
# ==============================================================================
class VennDiagramScene(BaseMathScene):
    def construct(self):
        cfg = getattr(self, "scene_config", {})
        title_text = cfg.get("title", "TRỰC QUAN HÓA: SƠ ĐỒ VEN & PHẦN TỬ CỦA TẬP HỢP")
        set_name = cfg.get("set_name", "A")
        set_meaning = cfg.get("set_meaning", "Tập hợp các số tự nhiên nhỏ hơn 5")
        elements = cfg.get("elements_inside", ["0", "1", "2", "3", "4"])
        duration = getattr(self, "audio_duration", 16.0)

        self.add_watermark_brand()

        # 1. Tiêu đề phân cảnh
        scene_title = Text(
            title_text,
            font=FONT_FAMILY,
            font_size=24,
            weight=BOLD,
            color=COLOR_AMBER
        ).to_edge(UP, buff=0.45)
        title_bar = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=2, color=COLOR_AMBER).next_to(scene_title, DOWN, buff=0.15)
        self.play(FadeIn(scene_title, shift=DOWN * 0.2), Create(title_bar), run_time=0.9)
        t_used = 0.9

        # 2. Tạo Sơ đồ Ven (Vòng elip phát sáng)
        venn_center = LEFT * 3.0 + DOWN * 0.3
        venn_circle = Ellipse(
            width=5.2,
            height=4.6,
            stroke_width=3.5,
            stroke_color=COLOR_CYAN,
            fill_color=COLOR_CYAN,
            fill_opacity=0.12
        ).move_to(venn_center)

        set_label = Text(
            set_name,
            font=FONT_FAMILY,
            font_size=38,
            weight=BOLD,
            color=COLOR_CYAN
        ).next_to(venn_circle.get_corner(UL), DR, buff=0.25)

        self.play(Create(venn_circle), Write(set_label), run_time=1.2)
        t_used += 1.2

        # 3. Các vị trí tọa độ của 5 phần tử bên trong Sơ đồ Ven
        inner_coords = [
            venn_center + UP * 0.9 + LEFT * 0.7,    # 0
            venn_center + UP * 0.8 + RIGHT * 0.8,   # 1
            venn_center + DOWN * 0.1 + LEFT * 1.1,  # 2
            venn_center + DOWN * 0.1 + RIGHT * 0.6, # 3
            venn_center + DOWN * 1.1 + LEFT * 0.1   # 4
        ]

        # Khởi tạo các phần tử từ vị trí rải rác bên ngoài, rồi bay vào trong
        elem_mobjects = []
        scatter_coords = [
            UP * 2.8 + LEFT * 6,
            UP * 1.5 + LEFT * 6.2,
            DOWN * 2.2 + LEFT * 6.0,
            DOWN * 0.5 + LEFT * 6.2,
            DOWN * 2.8 + LEFT * 4.5
        ]

        for i, val in enumerate(elements):
            t_num = Text(val, font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_TEXT_MAIN)
            dot = Dot(radius=0.18, color=COLOR_CARD, fill_opacity=0.9, stroke_width=1.5, stroke_color=COLOR_CYAN)
            dot_num = VGroup(dot, t_num).move_to(scatter_coords[i])
            elem_mobjects.append(dot_num)

        # Hiệu ứng các số xuất hiện và bay vào Sơ đồ Ven
        self.play(
            LaggedStart(*[FadeIn(em, scale=0.5) for em in elem_mobjects], lag_ratio=0.15),
            run_time=1.2
        )
        t_used += 1.2

        self.play(
            *[elem_mobjects[i].animate.move_to(inner_coords[i]) for i in range(len(elements))],
            run_time=1.5
        )
        t_used += 1.5

        # 4. Khu vực giải thích và minh họa ký hiệu (Bên phải màn hình)
        right_panel_center = RIGHT * 3.4 + DOWN * 0.3
        
        # Thẻ 1: Minh họa 3 ∈ A (Số 3 nằm bên trong)
        belong_box = RoundedRectangle(
            corner_radius=0.25,
            width=5.8,
            height=1.5,
            stroke_width=2,
            stroke_color=COLOR_EMERALD,
            fill_color=COLOR_CARD,
            fill_opacity=0.85
        ).move_to(right_panel_center + UP * 1.5)

        t_belong_sym = Text("3 ∈ A", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_EMERALD)
        t_belong_explain = Text("Số 3 thuộc tập hợp A", font=FONT_FAMILY, font_size=18, color=COLOR_TEXT_MAIN)
        t_belong_note = Text("(Ký hiệu: ∈ nghĩa là 'thuộc')", font=FONT_FAMILY, font_size=14, color=COLOR_TEXT_MUTED)
        belong_content = VGroup(t_belong_sym, t_belong_explain, t_belong_note).arrange(DOWN, buff=0.12).move_to(belong_box.get_center())

        # Highlight số 3 bên trong Sơ đồ Ven
        idx_3 = elements.index("3")
        target_3 = elem_mobjects[idx_3]

        self.play(
            target_3[0].animate.set_stroke(color=COLOR_EMERALD, width=3).set_fill(color="#064e3b"),
            target_3[1].animate.set_color(COLOR_EMERALD).scale(1.2),
            FadeIn(belong_box, shift=LEFT * 0.4),
            FadeIn(belong_content, shift=LEFT * 0.4),
            run_time=1.8
        )
        t_used += 1.8

        # 5. Thẻ 2: Minh họa 5 ∉ A (Số 5 nằm bên ngoài)
        not_belong_box = RoundedRectangle(
            corner_radius=0.25,
            width=5.8,
            height=1.5,
            stroke_width=2,
            stroke_color=COLOR_ROSE,
            fill_color=COLOR_CARD,
            fill_opacity=0.85
        ).move_to(right_panel_center + DOWN * 0.25)

        t_not_sym = Text("5 ∉ A", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_ROSE)
        t_not_explain = Text("Số 5 không thuộc tập hợp A", font=FONT_FAMILY, font_size=18, color=COLOR_TEXT_MAIN)
        t_not_note = Text("(Ký hiệu: ∉ nghĩa là 'không thuộc')", font=FONT_FAMILY, font_size=14, color=COLOR_TEXT_MUTED)
        not_content = VGroup(t_not_sym, t_not_explain, t_not_note).arrange(DOWN, buff=0.12).move_to(not_belong_box.get_center())

        # Số 5 xuất hiện bên ngoài đường cong Sơ đồ Ven
        pos_5 = venn_center + RIGHT * 2.8 + DOWN * 1.5
        dot_5 = Dot(radius=0.22, color="#450a0a", stroke_width=2, stroke_color=COLOR_ROSE)
        num_5 = Text("5", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_ROSE)
        obj_5 = VGroup(dot_5, num_5).move_to(pos_5)

        self.play(
            FadeIn(obj_5, scale=1.4),
            FadeIn(not_belong_box, shift=LEFT * 0.4),
            FadeIn(not_content, shift=LEFT * 0.4),
            run_time=1.8
        )
        t_used += 1.8

        # 6. Thẻ 3: Biểu diễn dạng liệt kê dưới đáy màn hình
        roster_box = RoundedRectangle(
            corner_radius=0.2,
            width=5.8,
            height=0.9,
            stroke_width=1.5,
            stroke_color=COLOR_AMBER,
            fill_color=COLOR_CARD,
            fill_opacity=0.9
        ).move_to(right_panel_center + DOWN * 1.65)

        roster_text = Text(
            "Cách viết:  A = { 0 ; 1 ; 2 ; 3 ; 4 }",
            font=FONT_FAMILY,
            font_size=18,
            weight=BOLD,
            color=COLOR_AMBER
        ).move_to(roster_box.get_center())

        self.play(Create(roster_box), Write(roster_text), run_time=1.4)
        t_used += 1.4

        # Chờ thời lượng audio còn lại để thuyết minh kết thúc tự nhiên
        remaining = max(1.0, duration - t_used)
        self.wait(remaining)


# ==============================================================================
# PHÂN CẢNH 3: TỔNG KẾT KIẾN THỨC TRỌNG TÂM (SUMMARY SCENE)
# ==============================================================================
class SummaryScene(BaseMathScene):
    def construct(self):
        cfg = getattr(self, "scene_config", {})
        title_text = cfg.get("title", "KIẾN THỨC TRỌNG TÂM CẦN GHI NHỚ")
        rules = cfg.get("rules", [
            "1. Tên tập hợp: Được viết bằng chữ cái in hoa (A, B, C, X, Y...)",
            "2. Cách viết: Liệt kê các phần tử trong cặp dấu ngoặc nhọn { }",
            "3. Phân cách: Các phần tử ngăn cách nhau bởi dấu chấm phẩy (;)",
            "4. Tính duy nhất: Mỗi phần tử chỉ được liệt kê một lần duy nhất",
            "5. Ký hiệu chuẩn: a ∈ A (a thuộc A) | b ∉ A (b không thuộc A)"
        ])
        duration = getattr(self, "audio_duration", 14.0)

        self.add_watermark_brand()

        # 1. Header hộp tổng kết
        header = Text(
            f"💡 {title_text}",
            font=FONT_FAMILY,
            font_size=26,
            weight=BOLD,
            color=COLOR_AMBER
        ).to_edge(UP, buff=0.5)

        header_line = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2.5, color=COLOR_AMBER).next_to(header, DOWN, buff=0.15)
        self.play(FadeIn(header, shift=DOWN * 0.2), Create(header_line), run_time=0.9)
        t_used = 0.9

        # 2. Bảng bao quát nội dung (Container Card)
        card = RoundedRectangle(
            corner_radius=0.3,
            width=12.2,
            height=4.8,
            stroke_width=2,
            stroke_color=COLOR_INDIGO,
            fill_color=COLOR_CARD,
            fill_opacity=0.7
        ).move_to(DOWN * 0.4)
        self.play(FadeIn(card, scale=0.95), run_time=0.8)
        t_used += 0.8

        # 3. Tạo các dòng quy tắc với bullet icons
        rule_mobjects = []
        colors = [COLOR_CYAN, COLOR_EMERALD, COLOR_AMBER, COLOR_INDIGO, COLOR_ROSE]

        for idx, rule in enumerate(rules):
            color = colors[idx % len(colors)]
            badge = Dot(radius=0.12, color=color)
            r_text = Text(
                rule,
                font=FONT_FAMILY,
                font_size=18,
                weight=MEDIUM,
                color=COLOR_TEXT_MAIN
            )
            item_group = VGroup(badge, r_text).arrange(RIGHT, buff=0.3)
            rule_mobjects.append(item_group)

        rules_container = VGroup(*rule_mobjects).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(card.get_center())

        # Xuất hiện từng dòng quy tắc mượt mà
        self.play(
            LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rule_mobjects], lag_ratio=0.25),
            run_time=3.5
        )
        t_used += 3.5

        # Chờ thời lượng audio kết thúc
        remaining = max(1.0, duration - t_used)
        self.wait(remaining)


# ==============================================================================
# PHÂN CẢNH HÌNH HỌC PHẲNG (BÀI 18: TAM GIÁC ĐỀU, HÌNH VUÔNG, LỤC GIÁC ĐỀU)
# ==============================================================================
class GeometryShapesScene(BaseMathScene):
    def construct(self):
        duration = getattr(self, "audio_duration", 15.0)
        self.add_watermark_brand()

        title = Text("TRỰC QUAN HÓA: BA HÌNH PHẲNG ĐỀU", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_AMBER).to_edge(UP, buff=0.45)
        title_bar = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=2, color=COLOR_AMBER).next_to(title, DOWN, buff=0.15)
        self.play(FadeIn(title, shift=DOWN * 0.2), Create(title_bar), run_time=0.9)
        t_used = 0.9

        # 1. Tam giác đều
        tri = RegularPolygon(n=3, radius=1.6, stroke_width=3, stroke_color=COLOR_CYAN, fill_color=COLOR_CYAN, fill_opacity=0.15)
        tri_label = Text("Tam giác đều\n(3 cạnh bằng nhau)", font=FONT_FAMILY, font_size=16, color=COLOR_CYAN).next_to(tri, DOWN, buff=0.3)
        g_tri = VGroup(tri, tri_label).move_to(LEFT * 4.2 + DOWN * 0.3)

        # 2. Hình vuông
        sq = Square(side_length=2.5, stroke_width=3, stroke_color=COLOR_EMERALD, fill_color=COLOR_EMERALD, fill_opacity=0.15)
        sq_label = Text("Hình vuông\n(4 góc vuông 90°)", font=FONT_FAMILY, font_size=16, color=COLOR_EMERALD).next_to(sq, DOWN, buff=0.3)
        g_sq = VGroup(sq, sq_label).move_to(DOWN * 0.3)

        # 3. Hình lục giác đều
        hex_shape = RegularPolygon(n=6, radius=1.6, stroke_width=3, stroke_color=COLOR_AMBER, fill_color=COLOR_AMBER, fill_opacity=0.15)
        hex_label = Text("Lục giác đều\n(6 góc bằng nhau)", font=FONT_FAMILY, font_size=16, color=COLOR_AMBER).next_to(hex_shape, DOWN, buff=0.3)
        g_hex = VGroup(hex_shape, hex_label).move_to(RIGHT * 4.2 + DOWN * 0.3)

        self.play(Create(tri), Write(tri_label), run_time=1.5)
        self.play(Create(sq), Write(sq_label), run_time=1.5)
        self.play(Create(hex_shape), Write(hex_label), run_time=1.5)
        t_used += 4.5

        # Hiệu ứng xoay nhẹ đồng thời để tạo cảm giác chuyển động mượt mà
        remaining = max(1.0, duration - t_used)
        self.play(
            Rotate(tri, angle=2*PI, run_time=remaining, rate_func=smooth),
            Rotate(sq, angle=-2*PI, run_time=remaining, rate_func=smooth),
            Rotate(hex_shape, angle=2*PI, run_time=remaining, rate_func=smooth),
        )
