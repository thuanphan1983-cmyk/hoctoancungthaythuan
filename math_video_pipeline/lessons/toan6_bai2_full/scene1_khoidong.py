"""
SCENE 1: ĐẶT VẤN ĐỀ & KHỞI ĐỘNG THỰC TẾ (BÀI 2 FULL 14-16 PHÚT)
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


class Scene1KhoiDong(Scene):
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

        # -------------------------------------------------------------
        # TIÊU ĐỀ CỐ ĐỊNH PHÍA TRÊN MÀN HÌNH (y = 3.25)
        # -------------------------------------------------------------
        header = Text("PHẦN 1: ĐẶT VẤN ĐỀ & KHỞI ĐỘNG THỰC TẾ", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # -------------------------------------------------------------
        # SLIDE 1: GIỚI THIỆU KHÓA HỌC & BÀI DẠY
        # -------------------------------------------------------------
        t_s1 = timing.get("scene1_slide1", 38.0)
        c1_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c1_title = Text("HỌC TOÁN CÙNG THẦY THUẤN PHAN", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        c1_sub = Text("Toán 6 • Kết Nối Tri Thức Với Cuộc Sống", font=FONT_FAMILY, font_size=26, weight=SEMIBOLD, color=COLOR_CYAN)
        
        b1_1 = Text("• Bài 2: Cách ghi số tự nhiên", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN)
        b1_2 = Text("• Hệ thập phân & Cấu tạo số tự nhiên", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        b1_3 = Text("• Chữ số La Mã cổ đại trong đời sống hiện đại", font=FONT_FAMILY, font_size=28, color=COLOR_EMERALD)
        
        c1_content = VGroup(c1_title, c1_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_AMBER), b1_1, b1_2, b1_3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        c1_content.move_to(c1_box.get_center())
        card1 = VGroup(c1_box, c1_content)

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(Write(c1_title), FadeIn(c1_sub, shift=UP), run_time=1.2)
        self.play(FadeIn(b1_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b1_2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b1_3, shift=RIGHT), run_time=0.8)
        
        rem_s1 = max(1.0, t_s1 - 4.4)
        self.wait(rem_s1)
        self.play(FadeOut(card1, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 2: CÁC CON SỐ KHỔNG LỒ TRONG ĐỜI SỐNG
        # -------------------------------------------------------------
        t_s2 = timing.get("scene1_slide2", 42.0)
        c2_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c2_title = Text("CÁC CON SỐ KHỔNG LỒ TRONG ĐỜI SỐNG", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_CYAN)
        c2_sub = Text("Từ tiền tệ, dân số đến khoảng cách thiên văn", font=FONT_FAMILY, font_size=25, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        b2_1 = Text("👥 Dân số Việt Nam: Hơn 100 000 000 người", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_TEXT_MAIN)
        b2_2 = Text("🚀 Khoảng cách Trái Đất - Mặt Trăng: 384 400 km", font=FONT_FAMILY, font_size=27, color=COLOR_TEXT_MAIN)
        b2_3 = Text("💳 Căn cước công dân 12 chữ số, biển số xe, mã vạch", font=FONT_FAMILY, font_size=27, color=COLOR_AMBER)
        b2_4 = Text("➔ Làm thế nào để ghi và đọc chính xác mọi số tự nhiên?", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_EMERALD)
        
        c2_content = VGroup(c2_title, c2_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_CYAN), b2_1, b2_2, b2_3, b2_4).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
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
        # SLIDE 3: PHÂN BIỆT RÕ: SỐ VÀ CHỮ SỐ
        # -------------------------------------------------------------
        t_s3 = timing.get("scene1_slide3", 44.0)
        c3_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c3_title = Text("PHÂN BIỆT RÕ: SỐ VÀ CHỮ SỐ", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_EMERALD)
        c3_sub = Text("Bản chất toán học nền tảng không thể nhầm lẫn", font=FONT_FAMILY, font_size=25, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        
        b3_1 = Text("📖 Ngôn ngữ: 29 chữ cái ghép thành hàng vạn từ ngữ phong phú", font=FONT_FAMILY, font_size=27, color=COLOR_TEXT_MAIN)
        b3_2 = Text("🔢 Toán học: Đúng 10 chữ số (0, 1, 2, ..., 9) tạo nên vô tận số", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_CYAN)
        b3_3 = Text("💡 Ví dụ: Năm 2026 là một SỐ, được viết bởi 4 CHỮ SỐ: 2, 0, 2, 6", font=FONT_FAMILY, font_size=27, color=COLOR_AMBER)
        
        c3_content = VGroup(c3_title, c3_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD), b3_1, b3_2, b3_3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        c3_content.move_to(c3_box.get_center())
        card3 = VGroup(c3_box, c3_content)

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.8)
        self.play(Write(c3_title), FadeIn(c3_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b3_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b3_2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b3_3, shift=RIGHT), run_time=1.0)

        rem_s3 = max(1.0, t_s3 - 4.4)
        self.wait(rem_s3)
        self.play(FadeOut(card3, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # SLIDE 4: DẤU ẤN LỊCH SỬ: CHỮ SỐ LA MÃ
        # -------------------------------------------------------------
        t_s4 = timing.get("scene1_slide4", 36.0)
        c4_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        c4_title = Text("DẤU ẤN LỊCH SỬ: CHỮ SỐ LA MÃ", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_AMBER)
        c4_sub = Text("Di sản văn hóa cổ đại vẫn hiện diện hằng ngày", font=FONT_FAMILY, font_size=25, weight=SEMIBOLD, color=COLOR_CYAN)
        
        b4_1 = Text("⏰ Mặt đồng hồ đeo tay và đồng hồ treo tường cổ điển: I, II, III, IV...", font=FONT_FAMILY, font_size=27, color=COLOR_TEXT_MAIN)
        b4_2 = Text("📜 Ký hiệu thế kỷ lịch sử: Thế kỷ XXI (thế kỷ 21)", font=FONT_FAMILY, font_size=27, color=COLOR_TEXT_MAIN)
        b4_3 = Text("📚 Đánh số thứ tự các chương, phần: Chương I, Chương II", font=FONT_FAMILY, font_size=27, color=COLOR_AMBER)
        b4_4 = Text("Mời các em bước vào PHẦN 2: HÌNH THÀNH KIẾN THỨC MỚI!", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_EMERALD)
        
        c4_content = VGroup(c4_title, c4_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_INDIGO), b4_1, b4_2, b4_3, b4_4).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c4_content.move_to(c4_box.get_center())
        card4 = VGroup(c4_box, c4_content)

        self.play(FadeIn(c4_box, scale=0.96), run_time=0.8)
        self.play(Write(c4_title), FadeIn(c4_sub, shift=UP), run_time=1.0)
        self.play(FadeIn(b4_1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(b4_2, shift=RIGHT), FadeIn(b4_3, shift=RIGHT), run_time=1.0)
        self.play(FadeIn(b4_4, scale=1.05), run_time=1.0)

        rem_s4 = max(1.0, t_s4 - 4.6)
        self.wait(rem_s4)


if __name__ == "__main__":
    pass
