"""
SCENE 4: LỖI SAI & CẢNH BÁO BẪY THI
Bài 1: Tập hợp - Phần tử của tập hợp (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Thời lượng đồng bộ audio: ~75.12s
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


class Scene4CanhBao(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        audio_file = os.path.join(cur_dir, "audio", "scene4_voice.mp3")
        target_duration = 75.12
        if os.path.exists(audio_file):
            try:
                target_duration = float(MP3(audio_file).info.length)
            except Exception:
                pass

        header = Text("PHẦN 4: 5 SAI LẦM PHỔ BIẾN & CẢNH BÁO BẪY THI", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_ROSE)
        header_line = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=1.5, color=COLOR_ROSE)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.4)
        self.play(FadeIn(header_group), run_time=1.0)
        self.wait(3.5)  # Thầy dặn dò lưu ý 5 lỗi

        # -------------------------------------------------------------
        # 3 LỖI ĐẦU TIÊN (3.5s -> 40s)
        # -------------------------------------------------------------
        def create_trap_row(num_str, title_str, wrong_str, right_str):
            num_t = Text(num_str, font=FONT_FAMILY, font_size=17, weight=BOLD, color=COLOR_AMBER)
            title_t = Text(title_str, font=FONT_FAMILY, font_size=16, color=COLOR_TEXT_MAIN)
            head_grp = VGroup(num_t, title_t).arrange(RIGHT, buff=0.2)
            
            w_grp = VGroup(Text("❌ SAI: ", font=FONT_FAMILY, font_size=15, weight=BOLD, color=COLOR_ROSE),
                           Text(wrong_str, font=FONT_FAMILY, font_size=15, color=COLOR_TEXT_MUTED)).arrange(RIGHT, buff=0.1)
            r_grp = VGroup(Text("✔️ ĐÚNG: ", font=FONT_FAMILY, font_size=15, weight=BOLD, color=COLOR_EMERALD),
                           Text(right_str, font=FONT_FAMILY, font_size=15, weight=BOLD, color=COLOR_CYAN)).arrange(RIGHT, buff=0.1)
            comp_grp = VGroup(w_grp, r_grp).arrange(RIGHT, buff=0.8)
            
            box = RoundedRectangle(corner_radius=0.2, width=12.0, height=1.5, stroke_color=COLOR_ROSE, stroke_width=1.2, fill_color=COLOR_CARD, fill_opacity=0.9)
            content = VGroup(head_grp, comp_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            return VGroup(box, content)

        row1 = create_trap_row("1.", "Đặt tên tập hợp bằng chữ thường:", "a = { 1; 2 } (Sai quy ước)", "A = { 1; 2 } (Bắt buộc chữ in hoa)")
        row2 = create_trap_row("2.", "Lặp lại phần tử trong ngoặc nhọn:", "{ N; H; A; T; R; A; N; G } (Lặp chữ A, N)", "{ N; H; A; T; R; G } (Mỗi phần tử viết 1 lần)")
        row3 = create_trap_row("3.", "Dùng dấu phẩy thay dấu chấm phẩy giữa các số:", "{ 1, 2 } (Người chấm đọc nhầm là số thập phân 1,2)", "{ 1; 2 } (Bắt buộc dùng dấu chấm phẩy ;)")

        t_group1 = VGroup(row1, row2, row3).arrange(DOWN, buff=0.25).next_to(header_group, DOWN, buff=0.3)
        self.play(FadeIn(row1, shift=DOWN), run_time=1.0)
        self.wait(10.0)
        self.play(FadeIn(row2, shift=DOWN), run_time=1.0)
        self.wait(10.0)
        self.play(FadeIn(row3, shift=DOWN), run_time=1.0)
        self.wait(10.0)

        # -------------------------------------------------------------
        # 2 LỖI TIẾP THEO: NGOẶC VÀ ĐIỀU KIỆN BIÊN (40s -> 75s)
        # -------------------------------------------------------------
        self.play(FadeOut(t_group1), run_time=1.0)

        row4 = create_trap_row("4.", "Dùng sai loại dấu ngoặc:", "( 1; 2; 3 )  hoặc  [ 1; 2; 3 ]", "{ 1; 2; 3 } (Chỉ dùng duy nhất ngoặc nhọn { })")
        row5 = create_trap_row("5.", "Bẫy điều kiện biên (dấu < và ≤):", "x < 5 mà vẫn ghi số 5 vào tập hợp", "x < 5 chỉ lấy đến 4; x ≤ 5 mới lấy số 5")

        tip_box = RoundedRectangle(corner_radius=0.2, width=12.0, height=1.6, stroke_color=COLOR_EMERALD, stroke_width=1.5, fill_color=COLOR_CARD, fill_opacity=0.95)
        tip_title = Text("💡 LỜI KHUYÊN CỦA THẦY THUẤN PHAN KHI LÀM BÀI:", font=FONT_FAMILY, font_size=17, weight=BOLD, color=COLOR_AMBER)
        tip_desc = Text("Luôn đọc kỹ dấu bất đẳng thức ( < hay ≤ ) và đếm kỹ số lượng phần tử trước khi kết luận!", font=FONT_FAMILY, font_size=15, color=COLOR_TEXT_MAIN)
        tip_group = VGroup(tip_box, VGroup(tip_title, tip_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.2))

        t_group2 = VGroup(row4, row5, tip_group).arrange(DOWN, buff=0.25).next_to(header_group, DOWN, buff=0.3)
        self.play(FadeIn(row4, shift=DOWN), run_time=1.0)
        self.wait(9.0)
        self.play(FadeIn(row5, shift=DOWN), run_time=1.0)
        self.wait(10.0)
        self.play(FadeIn(tip_group, scale=0.95), run_time=1.0)

        rem_time = max(1.0, target_duration - 68.0)
        self.wait(rem_time)


if __name__ == "__main__":
    pass
