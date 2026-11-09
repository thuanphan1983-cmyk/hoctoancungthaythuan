"""
SCENE 2: HÌNH THÀNH KIẾN THỨC MỚI CẶN KẼ (BÀI 2 FULL 14-16 PHÚT)
Bài 2: Cách ghi số tự nhiên (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn: Vùng an toàn 12x6, Font Arial Unicode MS, Chuyển slide từng phần
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
MATH_FONT = "Segoe UI Symbol"


def math_text(expr, font_size=28, color=COLOR_TEXT_MAIN, weight=BOLD):
    """Render biểu thức và ký hiệu toán học chuẩn xác, sắc nét"""
    return Text(expr, font=FONT_FAMILY, font_size=font_size, weight=weight, color=color)


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

        header = Text("PHẦN 2: HÌNH THÀNH KIẾN THỨC MỚI CẶN KẼ", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # -------------------------------------------------------------
        # SLIDE 2.1: TẬP HỢP SỐ TỰ NHIÊN N VÀ N*
        # -------------------------------------------------------------
        t_s1 = timing.get("scene2_slide1", 42.0)
        c1_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c1_title = Text("1. TẬP HỢP SỐ TỰ NHIÊN ℕ VÀ ℕ*", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_AMBER)
        c1_sub = Text("Ký hiệu chuẩn xác theo chương trình GDPT 2018", font=FONT_FAMILY, font_size=24, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        b1_1 = Text("• Tập hợp các số tự nhiên được ký hiệu là ℕ:", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_TEXT_MAIN)
        b1_2 = Text("   ℕ = { 0; 1; 2; 3; 4; 5; 6; 7; ... }", font=FONT_FAMILY, font_size=27, color=COLOR_CYAN)
        b1_3 = Text("• Tập hợp các số tự nhiên KHÁC 0 được ký hiệu là ℕ*:", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_TEXT_MAIN)
        b1_4 = Text("   ℕ* = { 1; 2; 3; 4; 5; 6; 7; ... }", font=FONT_FAMILY, font_size=27, color=COLOR_EMERALD)
        b1_5 = Text("• Ký hiệu: x ∈ ℕ nghĩa là x là một số tự nhiên bất kỳ.", font=FONT_FAMILY, font_size=27, color=COLOR_AMBER)
        
        c1_content = VGroup(c1_title, c1_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_AMBER), b1_1, b1_2, b1_3, b1_4, b1_5).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        c1_content.move_to(c1_box.get_center())
        card1 = VGroup(c1_box, c1_content)

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(Write(c1_title), FadeIn(c1_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b1_1, shift=RIGHT), FadeIn(b1_2, shift=RIGHT), run_time=1.2)
        self.play(FadeIn(b1_3, shift=RIGHT), FadeIn(b1_4, shift=RIGHT), run_time=1.2)
        self.play(FadeIn(b1_5, scale=1.03), run_time=0.8)

        rem_s1 = max(1.0, t_s1 - 5.0)
        self.wait(rem_s1)
        self.play(FadeOut(card1, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2.2: HỆ THẬP PHÂN & 10 CHỮ SỐ CƠ BẢN
        # -------------------------------------------------------------
        t_s2 = timing.get("scene2_slide2", 40.0)
        c2_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c2_title = Text("2. HỆ THẬP PHÂN & 10 CHỮ SỐ CƠ BẢN", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_CYAN)
        c2_sub = Text("Hệ đếm theo cơ số 10 thông dụng nhất nhân loại", font=FONT_FAMILY, font_size=24, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        b2_1 = Text("• Hệ thập phân sử dụng đúng 10 chữ số: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_TEXT_MAIN)
        b2_2 = Text("• Cứ 10 đơn vị ở một hàng thì làm thành 1 đơn vị ở hàng liền trước nó.", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MAIN)
        b2_3 = Text("• Quy tắc nhóm: Số có từ 4 chữ số trở lên tách từng cụm 3 chữ số từ phải sang trái:", font=FONT_FAMILY, font_size=26, color=COLOR_AMBER)
        b2_4 = Text("   Ví dụ: 12 345 678 (Mười hai triệu ba trăm bốn mươi lăm nghìn sáu trăm bảy tám)", font=FONT_FAMILY, font_size=24, color=COLOR_EMERALD)
        
        c2_content = VGroup(c2_title, c2_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_CYAN), b2_1, b2_2, b2_3, b2_4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        c2_content.move_to(c2_box.get_center())
        card2 = VGroup(c2_box, c2_content)

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(Write(c2_title), FadeIn(c2_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b2_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b2_2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b2_3, shift=RIGHT), FadeIn(b2_4, shift=UP), run_time=1.2)

        rem_s2 = max(1.0, t_s2 - 4.6)
        self.wait(rem_s2)
        self.play(FadeOut(card2, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2.3: CẤU TRÚC HÀNG VÀ LỚP
        # -------------------------------------------------------------
        t_s3 = timing.get("scene2_slide3", 44.0)
        c3_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c3_title = Text("3. CẤU TRÚC HÀNG VÀ LỚP TRONG HỆ THẬP PHÂN", font=FONT_FAMILY, font_size=29, weight=BOLD, color=COLOR_EMERALD)
        c3_sub = Text("Mỗi lớp gồm đúng 3 hàng liền kề (tính từ phải sang trái)", font=FONT_FAMILY, font_size=24, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        b3_1 = Text("• Lớp đơn vị: Hàng đơn vị, Hàng chục, Hàng trăm", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MAIN)
        b3_2 = Text("• Lớp nghìn: Hàng nghìn, Hàng chục nghìn, Hàng trăm nghìn", font=FONT_FAMILY, font_size=26, color=COLOR_CYAN)
        b3_3 = Text("• Lớp triệu: Hàng triệu, Hàng chục triệu, Hàng trăm triệu", font=FONT_FAMILY, font_size=26, color=COLOR_AMBER)
        b3_4 = Text("➔ Giá trị của mỗi chữ số phụ thuộc hoàn toàn vào VỊ TRÍ HÀNG của nó!", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_EMERALD)
        
        c3_content = VGroup(c3_title, c3_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD), b3_1, b3_2, b3_3, b3_4).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c3_content.move_to(c3_box.get_center())
        card3 = VGroup(c3_box, c3_content)

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.8)
        self.play(Write(c3_title), FadeIn(c3_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b3_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b3_2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b3_3, shift=RIGHT), FadeIn(b3_4, scale=1.03), run_time=1.2)

        rem_s3 = max(1.0, t_s3 - 4.6)
        self.wait(rem_s3)
        self.play(FadeOut(card3, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2.4: CẤU TẠO SỐ TỔNG QUÁT
        # -------------------------------------------------------------
        t_s4 = timing.get("scene2_slide4", 42.0)
        c4_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c4_title = Text("4. CẤU TẠO SỐ TỔNG QUÁT", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_AMBER)
        c4_sub = Text("Biểu diễn đại số nền tảng cho các bài toán tìm x và chữ số", font=FONT_FAMILY, font_size=24, weight=SEMIBOLD, color=COLOR_CYAN)
        
        b4_1 = Text("• Số có hai chữ số: ab = 10a + b  (với a ∈ ℕ*, a ≠ 0)", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_TEXT_MAIN)
        b4_2 = Text("• Số có ba chữ số: abc = 100a + 10b + c  (với a ≠ 0)", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_TEXT_MAIN)
        b4_3 = Text("• Số có bốn chữ số: abcd = 1000a + 100b + 10c + d  (với a ≠ 0)", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_TEXT_MAIN)
        b4_4 = Text("💡 Ghi nhớ: Dấu gạch ngang biểu thị số được ghép bởi các chữ số thành phần.", font=FONT_FAMILY, font_size=25, color=COLOR_EMERALD)
        
        c4_content = VGroup(c4_title, c4_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_INDIGO), b4_1, b4_2, b4_3, b4_4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        c4_content.move_to(c4_box.get_center())
        card4 = VGroup(c4_box, c4_content)

        self.play(FadeIn(c4_box, scale=0.96), run_time=0.8)
        self.play(Write(c4_title), FadeIn(c4_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b4_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b4_2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b4_3, shift=RIGHT), FadeIn(b4_4, shift=UP), run_time=1.2)

        rem_s4 = max(1.0, t_s4 - 4.6)
        self.wait(rem_s4)
        self.play(FadeOut(card4, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2.5: CHỮ SỐ LA MÃ CỔ ĐẠI & 3 KÝ HIỆU CƠ BẢN
        # -------------------------------------------------------------
        t_s5 = timing.get("scene2_slide5", 46.0)
        c5_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c5_title = Text("5. CHỮ SỐ LA MÃ CỔ ĐẠI & 3 KÝ HIỆU CƠ BẢN", font=FONT_FAMILY, font_size=29, weight=BOLD, color=COLOR_AMBER)
        c5_sub = Text("3 ký hiệu gốc: I (1), V (5), X (10) và quy tắc ghép", font=FONT_FAMILY, font_size=24, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        b5_1 = Text("• Ký hiệu cơ bản: I = 1  ;  V = 5  ;  X = 10", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_CYAN)
        b5_2 = Text("• Ghép bên PHẢI là CỘNG: VI = 5 + 1 = 6  ;  XI = 10 + 1 = 11", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MAIN)
        b5_3 = Text("• Ghép bên TRÁI là TRỪ:  IV = 5 - 1 = 4  ;  IX = 10 - 1 = 9", font=FONT_FAMILY, font_size=26, color=COLOR_ROSE)
        b5_4 = Text("⚠️ QUY TẮC CẤM: Không viết quá 3 lần chữ I, X liên tiếp (không có IIII hay XXXX)", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_AMBER)
        
        c5_content = VGroup(c5_title, c5_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_AMBER), b5_1, b5_2, b5_3, b5_4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        c5_content.move_to(c5_box.get_center())
        card5 = VGroup(c5_box, c5_content)

        self.play(FadeIn(c5_box, scale=0.96), run_time=0.8)
        self.play(Write(c5_title), FadeIn(c5_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b5_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b5_2, shift=RIGHT), FadeIn(b5_3, shift=RIGHT), run_time=1.2)
        self.play(FadeIn(b5_4, scale=1.03), run_time=0.8)

        rem_s5 = max(1.0, t_s5 - 4.6)
        self.wait(rem_s5)
        self.play(FadeOut(card5, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2.6: BẢNG TRA CỨU SỐ LA MÃ TỪ 1 ĐẾN 30
        # -------------------------------------------------------------
        t_s6 = timing.get("scene2_slide6", 42.0)
        c6_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c6_title = Text("6. BẢNG TRA CỨU SỐ LA MÃ TỪ 1 ĐẾN 30", font=FONT_FAMILY, font_size=29, weight=BOLD, color=COLOR_EMERALD)
        c6_sub = Text("Bảng tổng hợp chuẩn mực theo sách giáo khoa", font=FONT_FAMILY, font_size=24, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        b6_1 = Text("• Từ 1 đến 10:  I, II, III, IV, V, VI, VII, VIII, IX, X", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MAIN)
        b6_2 = Text("• Từ 11 đến 20: XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX", font=FONT_FAMILY, font_size=25, color=COLOR_CYAN)
        b6_3 = Text("• Từ 21 đến 30: XXI, XXII, XXIII, XXIV, XXV, XXVI, XXVII, XXVIII, XXIX, XXX", font=FONT_FAMILY, font_size=24, color=COLOR_AMBER)
        b6_4 = Text("💡 Ghi nhớ: Ghép hàng chục trước (X, XX), rồi ghép hàng đơn vị sau.", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_EMERALD)
        
        c6_content = VGroup(c6_title, c6_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD), b6_1, b6_2, b6_3, b6_4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        c6_content.move_to(c6_box.get_center())
        card6 = VGroup(c6_box, c6_content)

        self.play(FadeIn(c6_box, scale=0.96), run_time=0.8)
        self.play(Write(c6_title), FadeIn(c6_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b6_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b6_2, shift=RIGHT), FadeIn(b6_3, shift=RIGHT), run_time=1.2)
        self.play(FadeIn(b6_4, scale=1.03), run_time=0.8)

        rem_s6 = max(1.0, t_s6 - 4.6)
        self.wait(rem_s6)


if __name__ == "__main__":
    pass
