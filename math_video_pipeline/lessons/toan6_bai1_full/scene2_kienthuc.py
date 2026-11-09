"""
SCENE 2: HÌNH THÀNH KIẾN THỨC MỚI CẶN KẼ (CHUẨN CUỐN CHIẾU 15-20 PHÚT)
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn: 6 Slide cuốn chiếu độc lập, Font size >= 28, Ký hiệu toán học Segoe UI Symbol 100% sắc nét
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


def math_text(expr, font_size=32, color=COLOR_TEXT_MAIN, weight=BOLD):
    """Tạo biểu thức toán học với font Segoe UI Symbol sắc nét, không bao giờ lỗi font"""
    return Text(expr, font=MATH_FONT, font_size=font_size, weight=weight, color=color)


class Scene2KienThuc(Scene):
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

        header = Text("PHẦN 2: HÌNH THÀNH KIẾN THỨC MỚI CẶN KẼ", font=FONT_FAMILY, font_size=34, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # -------------------------------------------------------------
        # SLIDE 2.1: QUY ƯỚC ĐẶT TÊN VÀ PHẦN TỬ
        # -------------------------------------------------------------
        t_s1 = timing.get("scene2_slide1", 42.0)
        c1_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c1_title = Text("1. QUY ƯỚC ĐẶT TÊN TẬP HỢP & PHẦN TỬ", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        c1_sub = Text("Quy tắc chữ cái IN HOA trong Toán học", font=FONT_FAMILY, font_size=26, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        b1_1 = Text("• Tên tập hợp: Được đặt bằng chữ cái IN HOA: A, B, C, X, Y...", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN)
        b1_2 = Text("• Phần tử: Các đối tượng nằm bên trong tập hợp", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        b1_3 = Text("• Ví dụ: Tập hợp A gồm các số tự nhiên nhỏ hơn 5", font=FONT_FAMILY, font_size=28, color=COLOR_CYAN)
        b1_4 = Text("   Mỗi số 0, 1, 2, 3, 4 là một PHẦN TỬ của tập hợp A", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_EMERALD)
        
        c1_content = VGroup(c1_title, c1_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_AMBER), b1_1, b1_2, b1_3, b1_4).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        c1_content.move_to(c1_box.get_center())
        card1 = VGroup(c1_box, c1_content)

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(Write(c1_title), FadeIn(c1_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b1_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b1_2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b1_3, shift=RIGHT), FadeIn(b1_4, shift=UP), run_time=1.2)

        rem_s1 = max(1.0, t_s1 - 4.6)
        self.wait(rem_s1)
        self.play(FadeOut(card1, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2.2: CÁCH 1 - LIỆT KÊ CÁC PHẦN TỬ (3 QUY TẮC VÀNG)
        # -------------------------------------------------------------
        t_s2 = timing.get("scene2_slide2", 48.0)
        c2_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c2_title = Text("2. CÁCH 1: LIỆT KÊ CÁC PHẦN TỬ", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_CYAN)
        c2_sub = Text("3 quy tắc vàng bắt buộc khắc cốt ghi tâm", font=FONT_FAMILY, font_size=26, weight=SEMIBOLD, color=COLOR_AMBER)
        
        b2_1 = VGroup(Text("1. Viết tất cả các phần tử trong cặp dấu ngoặc nhọn: ", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN),
                      math_text("{ }", font_size=32, color=COLOR_AMBER)).arrange(RIGHT, buff=0.15)
        b2_2 = Text("2. Ngăn cách nhau bằng DẤU CHẤM PHẨY ( ; )", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_EMERALD)
        b2_3 = Text("   (Tuyệt đối không dùng dấu phẩy khi phần tử là số)", font=FONT_FAMILY, font_size=26, color=COLOR_ROSE)
        b2_4 = Text("3. Mỗi phần tử chỉ viết ĐÚNG MỘT LẦN, thứ tự tùy ý", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN)
        
        c2_content = VGroup(c2_title, c2_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_CYAN), b2_1, b2_2, b2_3, b2_4).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c2_content.move_to(c2_box.get_center())
        card2 = VGroup(c2_box, c2_content)

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(Write(c2_title), FadeIn(c2_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b2_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b2_2, shift=RIGHT), FadeIn(b2_3), run_time=1.0)
        self.play(FadeIn(b2_4, shift=RIGHT), run_time=0.8)

        rem_s2 = max(1.0, t_s2 - 4.4)
        self.wait(rem_s2)
        self.play(FadeOut(card2, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2.3: VÍ DỤ MINH HỌA CÁCH LIỆT KÊ
        # -------------------------------------------------------------
        t_s3 = timing.get("scene2_slide3", 38.0)
        c3_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c3_title = Text("VÍ DỤ VỀ CÁCH LIỆT KÊ PHẦN TỬ", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_EMERALD)
        c3_sub = Text("Biểu diễn tập hợp A các số tự nhiên nhỏ hơn 5", font=FONT_FAMILY, font_size=26, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        f3_1 = math_text("A = { 0; 1; 2; 3; 4 }", font_size=36, color=COLOR_AMBER)
        b3_2 = Text("• Nhận xét 1: Đủ 5 phần tử: 0, 1, 2, 3, 4", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        b3_3 = Text("• Nhận xét 2: Ngăn cách bởi dấu chấm phẩy ;", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        f3_4 = VGroup(Text("• Thứ tự tùy ý:  ", font=FONT_FAMILY, font_size=28, color=COLOR_CYAN),
                      math_text("A = { 4; 0; 3; 1; 2 }", font_size=32, color=COLOR_CYAN),
                      Text("  vẫn hoàn toàn ĐÚNG!", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN)).arrange(RIGHT, buff=0.15)
        
        c3_content = VGroup(c3_title, c3_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD), f3_1, b3_2, b3_3, f3_4).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        c3_content.move_to(c3_box.get_center())
        card3 = VGroup(c3_box, c3_content)

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.8)
        self.play(Write(c3_title), FadeIn(c3_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(f3_1, scale=1.08), run_time=1.0)
        self.play(FadeIn(b3_2, shift=RIGHT), FadeIn(b3_3, shift=RIGHT), run_time=1.0)
        self.play(FadeIn(f3_4, shift=UP), run_time=0.8)

        rem_s3 = max(1.0, t_s3 - 4.6)
        self.wait(rem_s3)
        self.play(FadeOut(card3, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2.4: CÁCH 2 - CHỈ RA TÍNH CHẤT ĐẶC TRƯNG
        # -------------------------------------------------------------
        t_s4 = timing.get("scene2_slide4", 45.0)
        c4_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c4_title = Text("3. CÁCH 2: CHỈ RA TÍNH CHẤT ĐẶC TRƯNG", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        c4_sub = Text("Nêu quy luật chung mà chỉ các phần tử thỏa mãn", font=FONT_FAMILY, font_size=26, weight=SEMIBOLD, color=COLOR_CYAN)
        
        f4_1 = math_text("A = { x ∈ ℕ | x < 5 }", font_size=36, color=COLOR_EMERALD)
        b4_2 = Text("• Giải mã từng ký hiệu:", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN)
        b4_3 = VGroup(math_text("x ∈ ℕ :", font_size=30, color=COLOR_CYAN),
                      Text(" x là số tự nhiên", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)).arrange(RIGHT, buff=0.2)
        b4_4 = Text("   + Dấu gạch đứng | :  đọc là 'sao cho'", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        b4_5 = Text("   + x < 5 :  điều kiện x phải nhỏ hơn 5", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        
        c4_content = VGroup(c4_title, c4_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_INDIGO), f4_1, b4_2, b4_3, b4_4, b4_5).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        c4_content.move_to(c4_box.get_center())
        card4 = VGroup(c4_box, c4_content)

        self.play(FadeIn(c4_box, scale=0.96), run_time=0.8)
        self.play(Write(c4_title), FadeIn(c4_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(f4_1, scale=1.08), run_time=1.0)
        self.play(FadeIn(b4_2, shift=RIGHT), FadeIn(b4_3, shift=RIGHT), run_time=1.0)
        self.play(FadeIn(b4_4, shift=RIGHT), FadeIn(b4_5, shift=RIGHT), run_time=1.0)

        rem_s4 = max(1.0, t_s4 - 4.8)
        self.wait(rem_s4)
        self.play(FadeOut(card4, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2.5: KÝ HIỆU THUỘC (∈) VÀ KHÔNG THUỘC (∉)
        # -------------------------------------------------------------
        t_s5 = timing.get("scene2_slide5", 46.0)
        c5_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c5_title = VGroup(
            Text("4. KÝ HIỆU THUỘC (", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN),
            math_text("∈", font_size=30, color=COLOR_CYAN),
            Text(") VÀ KHÔNG THUỘC (", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN),
            math_text("∉", font_size=30, color=COLOR_CYAN),
            Text(")", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN),
        ).arrange(RIGHT, buff=0.08)
        c5_sub = Text("Mối quan hệ cốt lõi giữa phần tử và tập hợp", font=FONT_FAMILY, font_size=25, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        row_in = VGroup(
            Text("• Ký hiệu Thuộc: ", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_EMERALD),
            math_text("3 ∈ A", font_size=32, color=COLOR_EMERALD)
        ).arrange(RIGHT, buff=0.2)
        desc_in = Text("   → Đọc là: '3 thuộc tập hợp A' (3 là phần tử của A)", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MAIN)
        
        row_out = VGroup(
            Text("• Ký hiệu Không thuộc: ", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_ROSE),
            math_text("5 ∉ A", font_size=32, color=COLOR_ROSE)
        ).arrange(RIGHT, buff=0.2)
        desc_out = Text("   → Đọc là: '5 không thuộc tập A' (5 không là phần tử của A)", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MAIN)
        
        warn = VGroup(
            Text("• Chú ý:  ", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_AMBER),
            math_text("∈", font_size=28, color=COLOR_EMERALD),
            Text("  và  ", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_AMBER),
            math_text("∉", font_size=28, color=COLOR_ROSE),
            Text("  chỉ dùng giữa PHẦN TỬ và TẬP HỢP", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_AMBER)
        ).arrange(RIGHT, buff=0.08)
        
        c5_content = VGroup(c5_title, c5_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD), row_in, desc_in, row_out, desc_out, warn).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        c5_content.move_to(c5_box.get_center())
        card5 = VGroup(c5_box, c5_content)

        self.play(FadeIn(c5_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(c5_title, shift=DOWN*0.1), FadeIn(c5_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(row_in, shift=RIGHT), FadeIn(desc_in, shift=RIGHT), run_time=1.0)
        self.play(FadeIn(row_out, shift=RIGHT), FadeIn(desc_out, shift=RIGHT), run_time=1.0)
        self.play(FadeIn(warn, scale=1.05), run_time=0.8)

        rem_s5 = max(1.0, t_s5 - 4.6)
        self.wait(rem_s5)
        self.play(FadeOut(card5, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2.6: MINH HỌA BẰNG SƠ ĐỒ VEN
        # -------------------------------------------------------------
        t_s6 = timing.get("scene2_slide6", 44.0)
        c6_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c6_title = Text("5. MINH HỌA BẰNG SƠ ĐỒ VEN (JOHN VENN)", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        
        ellipse = Ellipse(width=4.8, height=3.0, color=COLOR_CYAN, stroke_width=3, fill_color=COLOR_CYAN, fill_opacity=0.15)
        el_label = Text("Tập hợp A", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_CYAN).next_to(ellipse, UP, buff=0.1)
        
        d0 = VGroup(Dot(radius=0.08, color=COLOR_EMERALD), math_text("0", font_size=24)).arrange(RIGHT, buff=0.1).move_to(ellipse.get_center() + LEFT*1.2 + UP*0.5)
        d1 = VGroup(Dot(radius=0.08, color=COLOR_EMERALD), math_text("1", font_size=24)).arrange(RIGHT, buff=0.1).move_to(ellipse.get_center() + RIGHT*1.0 + UP*0.4)
        d2 = VGroup(Dot(radius=0.08, color=COLOR_EMERALD), math_text("2", font_size=24)).arrange(RIGHT, buff=0.1).move_to(ellipse.get_center() + DOWN*0.5)
        d3 = VGroup(Dot(radius=0.08, color=COLOR_EMERALD), math_text("3", font_size=24)).arrange(RIGHT, buff=0.1).move_to(ellipse.get_center() + LEFT*0.9 + DOWN*0.4)
        d4 = VGroup(Dot(radius=0.08, color=COLOR_EMERALD), math_text("4", font_size=24)).arrange(RIGHT, buff=0.1).move_to(ellipse.get_center() + RIGHT*0.9 + DOWN*0.5)
        
        d5 = VGroup(Dot(radius=0.08, color=COLOR_ROSE), Text("5 (ngoài A)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_ROSE)).arrange(RIGHT, buff=0.1).move_to(ellipse.get_center() + RIGHT*3.4 + UP*0.8)
        
        venn_graphic = VGroup(ellipse, el_label, d0, d1, d2, d3, d4, d5).move_to([0, -0.6, 0])
        card6 = VGroup(c6_box, c6_title.move_to([0, 1.7, 0]), venn_graphic)

        self.play(FadeIn(c6_box, scale=0.96), run_time=0.8)
        self.play(Write(c6_title), run_time=1.0)
        self.play(Create(ellipse), FadeIn(el_label), run_time=1.2)
        self.play(FadeIn(d0), FadeIn(d1), FadeIn(d2), FadeIn(d3), FadeIn(d4), run_time=1.2)
        self.play(FadeIn(d5, shift=LEFT), run_time=0.8)

        rem_s6 = max(1.0, t_s6 - 5.0)
        self.wait(rem_s6)


if __name__ == "__main__":
    pass
