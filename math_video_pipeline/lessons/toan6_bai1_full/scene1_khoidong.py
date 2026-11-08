"""
SCENE 1: ĐẶT VẤN ĐỀ & KHỞI ĐỘNG
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Thời lượng đồng bộ audio: ~58.34s
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

# Bảng màu chuẩn sư phạm
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

        # Xác định chính xác thời lượng audio
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        audio_file = os.path.join(cur_dir, "audio", "scene1_voice.mp3")
        target_duration = 58.34
        if os.path.exists(audio_file):
            try:
                target_duration = float(MP3(audio_file).info.length)
            except Exception:
                pass

        # -------------------------------------------------------------
        # 1. INTRO & THƯƠNG HIỆU (0s -> 12s)
        # -------------------------------------------------------------
        brand = Text("HỌC TOÁN CÙNG THẦY THUẤN PHAN", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_AMBER)
        brand_line = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=2, color=COLOR_AMBER)
        brand_group = VGroup(brand, brand_line).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.5)

        badge_rect = RoundedRectangle(corner_radius=0.2, width=7.0, height=0.6, stroke_color=COLOR_CYAN, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.9)
        badge_text = Text("TOÁN 6 • KẾT NỐI TRI THỨC VỚI CUỘC SỐNG", font=FONT_FAMILY, font_size=18, weight=BOLD, color=COLOR_CYAN)
        badge = VGroup(badge_rect, badge_text).next_to(brand_group, DOWN, buff=0.35)

        title = Text("BÀI 1: TẬP HỢP - PHẦN TỬ CỦA TẬP HỢP", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_TEXT_MAIN)
        title.next_to(badge, DOWN, buff=0.5)

        sub_title = Text("PHẦN 1: ĐẶT VẤN ĐỀ & KHỞI ĐỘNG TIẾT DẠY", font=FONT_FAMILY, font_size=20, weight=SEMIBOLD, color=COLOR_INDIGO)
        sub_title.next_to(title, DOWN, buff=0.25)

        self.play(FadeIn(brand_group, shift=DOWN), run_time=1.2)
        self.play(FadeIn(badge, scale=0.9), run_time=1.0)
        self.play(Write(title), run_time=1.8)
        self.play(FadeIn(sub_title, shift=UP), run_time=1.0)
        self.wait(7.0)  # Thầy chào hỏi và giới thiệu bài học

        # Thu gọn tiêu đề lên góc để hiển thị ví dụ thực tế
        intro_all = VGroup(badge, title, sub_title)
        self.play(FadeOut(intro_all), brand_group.animate.scale(0.8).to_corner(UL, buff=0.4), run_time=1.2)

        # -------------------------------------------------------------
        # 2. BỐN TÌNH HUỐNG THỰC TẾ TRỰC QUAN (12s -> 45s)
        # -------------------------------------------------------------
        sec_title = Text("TẬP HỢP TRONG ĐỜI SỐNG HẰNG NGÀY", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_CYAN)
        sec_title.to_edge(UP, buff=0.5)
        self.play(Write(sec_title), run_time=1.0)

        # Khung thẻ 1: Lớp 6A
        c1 = RoundedRectangle(corner_radius=0.2, width=5.8, height=1.6, stroke_color=COLOR_CYAN, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.85)
        t1_icon = Text("👥", font_size=26)
        t1_txt = Text("Tập hợp các bạn học sinh\ntrong lớp 6A", font=FONT_FAMILY, font_size=18, color=COLOR_TEXT_MAIN)
        card1 = VGroup(c1, VGroup(t1_icon, t1_txt).arrange(RIGHT, buff=0.3)).move_to([-3.2, 1.3, 0])

        # Khung thẻ 2: Giá sách
        c2 = RoundedRectangle(corner_radius=0.2, width=5.8, height=1.6, stroke_color=COLOR_AMBER, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.85)
        t2_icon = Text("📚", font_size=26)
        t2_txt = Text("Tập hợp các cuốn sách giáo khoa\ntrên giá sách", font=FONT_FAMILY, font_size=18, color=COLOR_TEXT_MAIN)
        card2 = VGroup(c2, VGroup(t2_icon, t2_txt).arrange(RIGHT, buff=0.3)).move_to([3.2, 1.3, 0])

        # Khung thẻ 3: Bàn tay
        c3 = RoundedRectangle(corner_radius=0.2, width=5.8, height=1.6, stroke_color=COLOR_EMERALD, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.85)
        t3_icon = Text("🖐️", font_size=26)
        t3_txt = Text("Tập hợp năm ngón tay\ntrên một bàn tay", font=FONT_FAMILY, font_size=18, color=COLOR_TEXT_MAIN)
        card3 = VGroup(c3, VGroup(t3_icon, t3_txt).arrange(RIGHT, buff=0.3)).move_to([-3.2, -0.7, 0])

        # Khung thẻ 4: 5 thành phố TW
        c4 = RoundedRectangle(corner_radius=0.2, width=5.8, height=1.6, stroke_color=COLOR_ROSE, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.85)
        t4_icon = Text("🇻🇳", font_size=26)
        t4_txt = Text("Tập hợp 5 thành phố trực thuộc TW:\nHà Nội, TP.HCM, Hải Phòng, ĐN, Cần Thơ", font=FONT_FAMILY, font_size=16, color=COLOR_TEXT_MAIN)
        card4 = VGroup(c4, VGroup(t4_icon, t4_txt).arrange(RIGHT, buff=0.3)).move_to([3.2, -0.7, 0])

        self.play(FadeIn(card1, shift=RIGHT), run_time=1.2)
        self.wait(4.0)
        self.play(FadeIn(card2, shift=LEFT), run_time=1.2)
        self.wait(4.0)
        self.play(FadeIn(card3, shift=RIGHT), run_time=1.2)
        self.wait(4.0)
        self.play(FadeIn(card4, shift=LEFT), run_time=1.2)
        self.wait(7.0)

        # -------------------------------------------------------------
        # 3. KẾT LUẬN & DẪN DẮT VÀO PHẦN 2 (45s -> 58.34s)
        # -------------------------------------------------------------
        all_cards = VGroup(card1, card2, card3, card4, sec_title)
        self.play(FadeOut(all_cards), run_time=1.2)

        trans_box = RoundedRectangle(corner_radius=0.3, width=10.5, height=2.8, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95)
        trans_line1 = Text("KHÁI NIỆM TRỌNG TÂM: TẬP HỢP", font=FONT_FAMILY, font_size=26, weight=BOLD, color=COLOR_AMBER)
        trans_line2 = Text("Một tập hợp được biểu diễn như thế nào?", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT_MAIN)
        trans_line3 = Text("Mời các em cùng bước sang PHẦN 2: HÌNH THÀNH KIẾN THỨC MỚI!", font=FONT_FAMILY, font_size=19, weight=BOLD, color=COLOR_EMERALD)
        trans_content = VGroup(trans_line1, trans_line2, trans_line3).arrange(DOWN, buff=0.3)
        trans_group = VGroup(trans_box, trans_content).move_to(ORIGIN)

        self.play(FadeIn(trans_group, scale=0.95), run_time=1.5)

        # Căn chỉnh chính xác thời gian còn lại đến target_duration
        # Hiện tại xấp xỉ ~52s, chờ thêm đến đủ thời lượng
        rem_time = max(1.0, target_duration - 52.0)
        self.wait(rem_time)


if __name__ == "__main__":
    pass
