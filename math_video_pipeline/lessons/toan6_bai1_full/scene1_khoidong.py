"""
SCENE 1: ĐẶT VẤN ĐỀ & KHỞI ĐỘNG THỰC TẾ (CHUẨN CUỐN CHIẾU 15-20 PHÚT)
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn: Vùng an toàn 12x6, Font size >= 28, Chuyển slide từng phần
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


class Scene1KhoiDong(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Đọc dữ liệu thời lượng nếu có
        timing_file = os.path.join(os.path.dirname(__file__), "audio", "timing_data.json")
        timing = {}
        if os.path.exists(timing_file):
            try:
                with open(timing_file, "r", encoding="utf-8") as f:
                    timing = json.load(f)
            except Exception:
                pass

        # -------------------------------------------------------------
        # TIÊU ĐỀ CỐ ĐỊNH PHÍA TRÊN MÀN HÌNH (y = 3.25)
        # -------------------------------------------------------------
        header = Text("PHẦN 1: ĐẶT VẤN ĐỀ & KHỞI ĐỘNG THỰC TẾ", font=FONT_FAMILY, font_size=34, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # -------------------------------------------------------------
        # SLIDE 1: GIỚI THIỆU KHÓA HỌC & BÀI DẠY (Cuốn chiếu)
        # -------------------------------------------------------------
        t_s1 = timing.get("scene1_slide1", 38.0)
        c1_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c1_title = Text("HỌC TOÁN CÙNG THẦY THUẤN PHAN", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        c1_sub = Text("Toán 6 • Kết Nối Tri Thức Với Cuộc Sống", font=FONT_FAMILY, font_size=26, weight=SEMIBOLD, color=COLOR_CYAN)
        
        b1_1 = Text("• Bài 1: Tập hợp và các phần tử của tập hợp", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN)
        b1_2 = Text("• Phương pháp học tập trực quan - Phát triển tư duy", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        b1_3 = Text("• Nền tảng mở đầu quan trọng cho toàn bộ cấp THCS", font=FONT_FAMILY, font_size=28, color=COLOR_EMERALD)
        
        c1_content = VGroup(c1_title, c1_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_AMBER), b1_1, b1_2, b1_3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        c1_content.move_to(c1_box.get_center())
        card1 = VGroup(c1_box, c1_content)

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(Write(c1_title), FadeIn(c1_sub, shift=UP), run_time=1.2)
        self.play(FadeIn(b1_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b1_2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b1_3, shift=RIGHT), run_time=0.8)
        
        # Chờ trọn vẹn giọng đọc slide 1
        rem_s1 = max(1.0, t_s1 - 4.4)
        self.wait(rem_s1)
        self.play(FadeOut(card1, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2: TÌNH HUỐNG THỰC TẾ 1 - LỚP HỌC & GIÁ SÁCH
        # -------------------------------------------------------------
        t_s2 = timing.get("scene1_slide2", 42.0)
        c2_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c2_title = Text("TẬP HỢP TRONG ĐỜI SỐNG HẰNG NGÀY", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_CYAN)
        c2_sub = Text("Quan sát những nhóm đồ vật và con người gần gũi", font=FONT_FAMILY, font_size=26, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        b2_1 = Text("👥 Tình huống 1: Tập hợp các bạn học sinh trong lớp 6A", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN)
        b2_2 = Text("📚 Tình huống 2: Tập hợp các cuốn sách giáo khoa trên bàn:", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        b2_3 = Text("   Toán, Ngữ văn, KHTN, Lịch sử và Địa lí...", font=FONT_FAMILY, font_size=28, color=COLOR_AMBER)
        b2_4 = Text("➔ Điểm chung: Đều tạo thành một NHÓM XÁC ĐỊNH rõ ràng", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_EMERALD)
        
        c2_content = VGroup(c2_title, c2_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_CYAN), b2_1, b2_2, b2_3, b2_4).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        c2_content.move_to(c2_box.get_center())
        card2 = VGroup(c2_box, c2_content)

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(Write(c2_title), FadeIn(c2_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b2_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b2_2, shift=RIGHT), FadeIn(b2_3, shift=RIGHT), run_time=1.0)
        self.play(FadeIn(b2_4, scale=1.05), run_time=0.8)

        rem_s2 = max(1.0, t_s2 - 4.4)
        self.wait(rem_s2)
        self.play(FadeOut(card2, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 3: TÌNH HUỐNG THỰC TẾ 2 - BÀN TAY & THÀNH PHỐ
        # -------------------------------------------------------------
        t_s3 = timing.get("scene1_slide3", 44.0)
        c3_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c3_title = Text("TẬP HỢP XUNG QUANH CHÚNG TA", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_EMERALD)
        c3_sub = Text("Những ví dụ trực quan sinh động", font=FONT_FAMILY, font_size=26, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        b3_1 = Text("🖐️ Bàn tay: Tập hợp năm ngón tay trên một bàn tay", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        b3_2 = Text("   (ngón cái, ngón trỏ, ngón giữa, ngón áp út, ngón út)", font=FONT_FAMILY, font_size=26, color=COLOR_TEXT_MUTED)
        b3_3 = Text("🇻🇳 Đất nước: Tập hợp 5 thành phố trực thuộc Trung ương:", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN)
        b3_4 = Text("   Hà Nội, TP. Hồ Chí Minh, Hải Phòng, Đà Nẵng, Cần Thơ", font=FONT_FAMILY, font_size=28, color=COLOR_CYAN)
        
        c3_content = VGroup(c3_title, c3_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD), b3_1, b3_2, b3_3, b3_4).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c3_content.move_to(c3_box.get_center())
        card3 = VGroup(c3_box, c3_content)

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.8)
        self.play(Write(c3_title), FadeIn(c3_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b3_1, shift=RIGHT), FadeIn(b3_2), run_time=1.0)
        self.play(FadeIn(b3_3, shift=RIGHT), FadeIn(b3_4, shift=UP), run_time=1.2)

        rem_s3 = max(1.0, t_s3 - 4.8)
        self.wait(rem_s3)
        self.play(FadeOut(card3, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 4: DẪN NHẬP VÀO KIẾN THỨC MỚI
        # -------------------------------------------------------------
        t_s4 = timing.get("scene1_slide4", 36.0)
        c4_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c4_title = Text("TỪ ĐỜI SỐNG BƯỚC VÀO TOÁN HỌC", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        c4_sub = Text("Khái niệm cơ bản & Mở đầu quan trọng", font=FONT_FAMILY, font_size=26, weight=SEMIBOLD, color=COLOR_CYAN)
        
        b4_1 = Text("• Khái niệm mở đầu: TẬP HỢP (Set trong tiếng Anh)", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN)
        b4_2 = Text("• Cách viết, cách ký hiệu và biểu diễn chuẩn xác", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        b4_3 = Text("Mời các em bước vào PHẦN 2: HÌNH THÀNH KIẾN THỨC MỚI!", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_EMERALD)
        
        c4_content = VGroup(c4_title, c4_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_INDIGO), b4_1, b4_2, b4_3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        c4_content.move_to(c4_box.get_center())
        card4 = VGroup(c4_box, c4_content)

        self.play(FadeIn(c4_box, scale=0.96), run_time=0.8)
        self.play(Write(c4_title), FadeIn(c4_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b4_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b4_2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b4_3, scale=1.05), run_time=1.0)

        rem_s4 = max(1.0, t_s4 - 4.4)
        self.wait(rem_s4)


if __name__ == "__main__":
    pass
