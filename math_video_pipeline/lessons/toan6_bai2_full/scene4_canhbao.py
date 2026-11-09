"""
SCENE 4: CẢNH BÁO 4 LỖI SAI KINH ĐIỂN KHI THI (BÀI 2 FULL)
Bài 2: Cách ghi số tự nhiên (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn: 4 slide bẫy đề thi độc lập, so sánh ✗ SAI vs ✓ ĐÚNG, Font Arial Unicode MS
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

        header = Text("PHẦN 4: 4 LỖI SAI KINH ĐIỂN KHI LÀM BÀI THI", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_ROSE)
        header_line = Line(LEFT * 5.8, RIGHT * 5.8, stroke_width=2, color=COLOR_ROSE)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # -------------------------------------------------------------
        # TRAP 1: NHẦM LẪN GIỮA SỐ VÀ CHỮ SỐ
        # -------------------------------------------------------------
        t_t1 = timing.get("scene4_trap1", 28.0)
        c1_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        t1_head = Text("LỖI SAI 1: NHẦM LẪN GIỮA 'SỐ' VÀ 'CHỮ SỐ'", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        w1 = Text("✗ SAI:   Nói 'Số 4853 có 4 số'", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_ROSE)
        r1 = Text("✓ ĐÚNG:  'Số 4853 có 4 CHỮ SỐ: 4, 8, 5, 3'", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_EMERALD)
        n1_1 = Text("💡 Lưu ý: Số biểu diễn số lượng (độ lớn), chữ số là ký hiệu dùng để ghi số.", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        n1_2 = Text("   Chỉ có đúng 10 chữ số (0 đến 9), nhưng có vô số các số tự nhiên!", font=FONT_FAMILY, font_size=24, color=COLOR_CYAN)
        
        c1_content = VGroup(t1_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_ROSE), w1, r1, n1_1, n1_2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c1_content.move_to(c1_box.get_center())
        card1 = VGroup(c1_box, c1_content)

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.8)
        self.play(Write(t1_head), run_time=0.8)
        self.play(FadeIn(w1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(r1, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(n1_1), FadeIn(n1_2), run_time=1.0)

        rem_t1 = max(1.0, t_t1 - 4.2)
        self.wait(rem_t1)
        self.play(FadeOut(card1, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # TRAP 2: VIẾT LẶP LẠI QUÁ 3 LẦN CHỮ I HOẶC X
        # -------------------------------------------------------------
        t_t2 = timing.get("scene4_trap2", 28.0)
        c2_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        t2_head = Text("LỖI SAI 2: VIẾT LẶP LẠI QUÁ 3 LẦN CHỮ I HOẶC X", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        w2 = Text("✗ SAI:   Số 4 viết là IIII  ;  Số 9 viết là VIIII  ;  Số 40 là XXXX", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_ROSE)
        r2 = Text("✓ ĐÚNG:  Số 4 viết là IV  ;  Số 9 viết là IX  ;  Số 40 viết là XL", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_EMERALD)
        n2_1 = Text("💡 Lưu ý: Tuyệt đối không được viết chữ I, X quá 3 lần liên tiếp.", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        n2_2 = Text("   Bắt buộc dùng quy tắc trừ: IV = 5 - 1  ;  IX = 10 - 1", font=FONT_FAMILY, font_size=24, color=COLOR_CYAN)
        
        c2_content = VGroup(t2_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_AMBER), w2, r2, n2_1, n2_2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c2_content.move_to(c2_box.get_center())
        card2 = VGroup(c2_box, c2_content)

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.8)
        self.play(Write(t2_head), run_time=0.8)
        self.play(FadeIn(w2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(r2, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(n2_1), FadeIn(n2_2), run_time=1.0)

        rem_t2 = max(1.0, t_t2 - 4.2)
        self.wait(rem_t2)
        self.play(FadeOut(card2, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # TRAP 3: QUÊN ĐIỀU KIỆN CHỮ SỐ ĐẦU TIÊN KHÁC 0
        # -------------------------------------------------------------
        t_t3 = timing.get("scene4_trap3", 28.0)
        c3_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        t3_head = Text("LỖI SAI 3: QUÊN ĐIỀU KIỆN CHỮ SỐ ĐẦU TIÊN KHÁC 0", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        w3 = Text("✗ SAI:   Tìm số ab mà cho chữ số hàng chục a = 0 (ví dụ số 05)", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_ROSE)
        r3 = Text("✓ ĐÚNG:  Chữ số hàng cao nhất bắt buộc phải khác 0 (a ∈ ℕ*, a ≠ 0)", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_EMERALD)
        n3_1 = Text("💡 Lưu ý: Số tự nhiên có 2 chữ số ab thì a phải từ 1 đến 9, b từ 0 đến 9.", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        n3_2 = Text("   Luôn đặt điều kiện a ≠ 0 để không bị mất điểm điều kiện trong bài tự luận!", font=FONT_FAMILY, font_size=24, color=COLOR_CYAN)
        
        c3_content = VGroup(t3_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_CYAN), w3, r3, n3_1, n3_2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c3_content.move_to(c3_box.get_center())
        card3 = VGroup(c3_box, c3_content)

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.8)
        self.play(Write(t3_head), run_time=0.8)
        self.play(FadeIn(w3, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(r3, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(n3_1), FadeIn(n3_2), run_time=1.0)

        rem_t3 = max(1.0, t_t3 - 4.2)
        self.wait(rem_t3)
        self.play(FadeOut(card3, shift=UP*0.3), run_time=0.8)

        # -------------------------------------------------------------
        # TRAP 4: ĐẶT KÝ HIỆU TRỪ LA MÃ SAI QUY TẮC
        # -------------------------------------------------------------
        t_t4 = timing.get("scene4_trap4", 28.0)
        c4_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        
        t4_head = Text("LỖI SAI 4: ĐẶT KÝ HIỆU TRỪ LA MÃ SAI QUY TẮC", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        w4 = Text("✗ SAI:   Viết 49 là IL (lấy 50 - 1)  ;  Viết 99 là IC (lấy 100 - 1)", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_ROSE)
        r4 = Text("✓ ĐÚNG:  49 = XLIX (40 + 9)  ;  99 = XCIX (90 + 9)", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_EMERALD)
        n4_1 = Text("💡 Lưu ý: Chữ I chỉ được phép đứng trước V và X mà thôi.", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        n4_2 = Text("   Bắt buộc tách theo hàng: Hàng chục trước rồi đến hàng đơn vị!", font=FONT_FAMILY, font_size=24, color=COLOR_CYAN)
        
        c4_content = VGroup(t4_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_INDIGO), w4, r4, n4_1, n4_2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c4_content.move_to(c4_box.get_center())
        card4 = VGroup(c4_box, c4_content)

        self.play(FadeIn(c4_box, scale=0.96), run_time=0.8)
        self.play(Write(t4_head), run_time=0.8)
        self.play(FadeIn(w4, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(r4, shift=RIGHT), run_time=0.8)
        self.play(FadeIn(n4_1), FadeIn(n4_2), run_time=1.0)

        rem_t4 = max(1.0, t_t4 - 4.2)
        self.wait(rem_t4)


if __name__ == "__main__":
    pass
