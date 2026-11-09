"""
SCENE 4: CẢNH BÁO 4 LỖI SAI KINH ĐIỂN KHI THI (CHUẨN CUỐN CHIẾU 15-20 PHÚT)
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn: 4 slide bẫy đề thi độc lập, so sánh ✗ SAI vs ✓ ĐÚNG, Font size >= 28
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


def math_text(expr, font_size=28, color=COLOR_TEXT_MAIN, weight=BOLD):
    return Text(expr, font=MATH_FONT, font_size=font_size, weight=weight, color=color)


def icon_wrong(font_size=28):
    return math_text("✗", font_size=font_size, color=COLOR_ROSE)


def icon_right(font_size=28):
    return math_text("✓", font_size=font_size, color=COLOR_EMERALD)


class Scene4CanhBao(Scene):
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

        header = Text("PHẦN 4: 4 LỖI SAI KINH ĐIỂN KHI LÀM BÀI THI", font=FONT_FAMILY, font_size=34, weight=BOLD, color=COLOR_ROSE)
        header_line = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=COLOR_ROSE)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # -------------------------------------------------------------
        # TRAP 1: ĐẶT TÊN BẰNG CHỮ THƯỜNG
        # -------------------------------------------------------------
        t_t1 = timing.get("scene4_trap1", 24.0)
        c1_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        t1_head = Text("BẪY 1: ĐẶT TÊN TẬP HỢP BẰNG CHỮ THƯỜNG", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        w1 = VGroup(
            icon_wrong(),
            Text(" SAI:   a = { 1; 2; 3 }    (Dùng chữ in thường là vi phạm quy ước)", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_ROSE)
        ).arrange(RIGHT, buff=0.12)
        
        r1 = VGroup(
            icon_right(),
            Text(" ĐÚNG:  A = { 1; 2; 3 }    (Bắt buộc dùng chữ cái IN HOA)", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_EMERALD)
        ).arrange(RIGHT, buff=0.12)
        
        note1 = Text("• Lưu ý: Chỉ dùng các chữ in hoa như A, B, C, M, N, X, Y...", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        
        c1_content = VGroup(t1_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_ROSE), w1, r1, note1).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        c1_content.move_to(c1_box.get_center())
        card1 = VGroup(c1_box, c1_content)

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(Write(t1_head), run_time=1.0)
        self.play(FadeIn(w1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(r1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(note1), run_time=0.8)

        rem_t1 = max(1.0, t_t1 - 4.2)
        self.wait(rem_t1)
        self.play(FadeOut(card1, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # TRAP 2: LẶP LẠI PHẦN TỬ TRONG NGOẶC NHỌN
        # -------------------------------------------------------------
        t_t2 = timing.get("scene4_trap2", 20.784)
        c2_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        t2_head = Text("BẪY 2: LẶP LẠI PHẦN TỬ TRONG NGOẶC NHỌN", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        w2 = VGroup(
            icon_wrong(),
            Text(" SAI:   E = { N; H; A; T; R; A; N; G }   (Lặp chữ A và chữ N)", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_ROSE)
        ).arrange(RIGHT, buff=0.12)
        
        r2 = VGroup(
            icon_right(),
            Text(" ĐÚNG:  E = { N; H; A; T; R; G }   (Mỗi phần tử viết đúng 1 lần)", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_EMERALD)
        ).arrange(RIGHT, buff=0.12)
        
        note2 = Text("• Quy tắc bất biến: Dù phần tử xuất hiện bao nhiêu lần trong từ,", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        note2_2 = Text("  khi viết vào tập hợp chỉ được ghi DUY NHẤT MỘT LẦN!", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN)
        
        c2_content = VGroup(t2_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_AMBER), w2, r2, note2, note2_2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        c2_content.move_to(c2_box.get_center())
        card2 = VGroup(c2_box, c2_content)

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(Write(t2_head), run_time=1.0)
        self.play(FadeIn(w2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(r2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(note2), FadeIn(note2_2), run_time=1.0)

        rem_t2 = max(1.0, t_t2 - 4.4)
        self.wait(rem_t2)
        self.play(FadeOut(card2, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # TRAP 3: DÙNG DẤU PHẨY THAY CHO CHẤM PHẨY
        # -------------------------------------------------------------
        t_t3 = timing.get("scene4_trap3", 20.304)
        c3_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        t3_head = Text("BẪY 3: DÙNG DẤU PHẨY THAY CHO CHẤM PHẨY", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_CYAN)
        w3 = VGroup(
            icon_wrong(),
            Text(" SAI:   { 1, 2 }    (Dễ bị đọc nhầm thành số thập phân 1,2)", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_ROSE)
        ).arrange(RIGHT, buff=0.12)
        
        r3 = VGroup(
            icon_right(),
            Text(" ĐÚNG:  { 1; 2 }    (Bắt buộc dùng dấu chấm phẩy ;)", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_EMERALD)
        ).arrange(RIGHT, buff=0.12)
        
        note3 = Text("• Khi các phần tử là số: Luôn dùng dấu chấm phẩy ( ; )", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        note3_2 = Text("  để phân biệt rành mạch, tránh nhầm lẫn đáng tiếc!", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        
        c3_content = VGroup(t3_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_CYAN), w3, r3, note3, note3_2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        c3_content.move_to(c3_box.get_center())
        card3 = VGroup(c3_box, c3_content)

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.8)
        self.play(Write(t3_head), run_time=1.0)
        self.play(FadeIn(w3, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(r3, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(note3), FadeIn(note3_2), run_time=1.0)

        rem_t3 = max(1.0, t_t3 - 4.4)
        self.wait(rem_t3)
        self.play(FadeOut(card3, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # TRAP 4: BẪY ĐIỀU KIỆN BIÊN BẤT ĐẲNG THỨC
        # -------------------------------------------------------------
        t_t4 = timing.get("scene4_trap4", 20.544)
        c4_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        t4_head = Text("BẪY 4: ĐIỀU KIỆN BIÊN CỦA DẤU BẤT ĐẲNG THỨC", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        w4 = VGroup(
            icon_wrong(),
            Text(" SAI:   x < 5 mà vẫn ghi số 5 vào:  { 0; 1; 2; 3; 4; 5 }", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_ROSE)
        ).arrange(RIGHT, buff=0.12)
        
        r4 = VGroup(
            icon_right(),
            Text(" ĐÚNG:  x < 5 chỉ lấy đến 4:  { 0; 1; 2; 3; 4 }", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_EMERALD)
        ).arrange(RIGHT, buff=0.12)
        
        note4 = VGroup(
            Text("• Chú ý: Dấu '<' không lấy số biên; Dấu ", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN),
            math_text("≤", font_size=30, color=COLOR_AMBER),
            Text(" mới được lấy số biên!", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_CYAN),
        ).arrange(RIGHT, buff=0.08)
        
        c4_content = VGroup(t4_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_INDIGO), w4, r4, note4).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        c4_content.move_to(c4_box.get_center())
        card4 = VGroup(c4_box, c4_content)

        self.play(FadeIn(c4_box, scale=0.96), run_time=0.8)
        self.play(Write(t4_head), run_time=1.0)
        self.play(FadeIn(w4, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(r4, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(note4, scale=1.05), run_time=0.8)

        rem_t4 = max(1.0, t_t4 - 4.2)
        self.wait(rem_t4)


if __name__ == "__main__":
    pass
