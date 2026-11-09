"""
SCENE 4: CẢNH BÁO 4 LỖI SAI KINH ĐIỂN KHI THI (BÀI 2 FULL)
Bài 2: Cách ghi số tự nhiên (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn:
- Strict Safe-Zone & Auto-Scale: fit_safe_box (max_width=10.8, max_height=4.6, margins >= 1.2 x 0.8)
- Audio-Visual Sync chính xác từng mili-giây (mutagen MP3 get_audio_duration)
- So sánh ✗ SAI (Red) vs ✓ ĐÚNG (Green), Font Arial Unicode MS (Zero Hex Boxes)
"""

import os
import sys
import json
from mutagen.mp3 import MP3
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


def fit_safe_box(content_mobject, max_width=11.0, max_height=5.2):
    """Auto-scale helper: Giữ toàn bộ nội dung nằm tuyệt đối trong vùng an toàn"""
    if content_mobject.width > max_width:
        content_mobject.scale(max_width / content_mobject.width)
    if content_mobject.height > max_height:
        content_mobject.scale(max_height / content_mobject.height)
    return content_mobject


def get_audio_duration(audio_path, fallback=10.0):
    """Đo thời lượng thực tế của file âm thanh bằng mutagen chính xác từng mili-giây"""
    if os.path.exists(audio_path):
        try:
            return float(MP3(audio_path).info.length)
        except Exception:
            pass
    return fallback


class Scene4CanhBao(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        audio_dir = os.path.join(os.path.dirname(__file__), "audio")
        timing_file = os.path.join(audio_dir, "timing_data.json")
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

        fade_out_dur = 0.6

        # -------------------------------------------------------------
        # TRAP 1: NHẦM LẪN GIỮA SỐ VÀ CHỮ SỐ
        # -------------------------------------------------------------
        a_t1 = os.path.join(audio_dir, "scene4_trap1.mp3")
        t_t1 = get_audio_duration(a_t1, fallback=timing.get("scene4_trap1", 20.50))

        t1_head = Text("LỖI SAI 1: NHẦM LẪN GIỮA 'SỐ' VÀ 'CHỮ SỐ'", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        w1 = Text("✗ SAI:   Nói 'Số 4853 có 4 số'", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_ROSE)
        r1 = Text("✓ ĐÚNG:  'Số 4853 có 4 CHỮ SỐ: 4, 8, 5, 3'", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_EMERALD)
        n1_1 = Text("💡 Lưu ý: Số biểu diễn số lượng (độ lớn), chữ số là ký hiệu dùng để ghi số.", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        n1_2 = Text("   Chỉ có đúng 10 chữ số (0 đến 9), nhưng có vô số các số tự nhiên!", font=FONT_FAMILY, font_size=24, color=COLOR_CYAN)

        c1_content = VGroup(t1_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_ROSE), w1, r1, n1_1, n1_2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fit_safe_box(c1_content, max_width=10.8, max_height=4.6)
        c1_content.move_to([0, -0.4, 0])

        c1_box = RoundedRectangle(corner_radius=0.3, width=c1_content.width + 0.8, height=c1_content.height + 0.65, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c1_content.get_center())
        card1 = VGroup(c1_box, c1_content)

        anim_t1 = 0.6 + 0.6 + 0.6 + 0.6 + 0.7
        avail_t1 = max(0.2, t_t1 - fade_out_dur)
        scale_t1 = min(1.0, (avail_t1 - 0.2) / max(0.1, anim_t1)) if anim_t1 > avail_t1 else 1.0

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.6 * scale_t1)
        self.play(Write(t1_head), run_time=0.6 * scale_t1)
        self.play(FadeIn(w1, shift=RIGHT), run_time=0.6 * scale_t1)
        self.play(FadeIn(r1, shift=RIGHT), run_time=0.6 * scale_t1)
        self.play(FadeIn(n1_1), FadeIn(n1_2), run_time=0.7 * scale_t1)

        actual_anim1 = anim_t1 * scale_t1
        rem_t1 = max(0.15, avail_t1 - actual_anim1)
        self.wait(rem_t1)
        self.play(FadeOut(card1, shift=UP*0.25), run_time=fade_out_dur)

        # -------------------------------------------------------------
        # TRAP 2: VIẾT LẶP LẠI QUÁ 3 LẦN CHỮ I HOẶC X
        # -------------------------------------------------------------
        a_t2 = os.path.join(audio_dir, "scene4_trap2.mp3")
        t_t2 = get_audio_duration(a_t2, fallback=timing.get("scene4_trap2", 27.82))

        t2_head = Text("LỖI SAI 2: VIẾT LẶP LẠI QUÁ 3 LẦN CHỮ I HOẶC X", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        w2 = Text("✗ SAI:   Số 4 viết là IIII  ;  Số 9 viết là VIIII  ;  Số 40 là XXXX", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_ROSE)
        r2 = Text("✓ ĐÚNG:  Số 4 viết là IV  ;  Số 9 viết là IX  ;  Số 40 viết là XL", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_EMERALD)
        n2_1 = Text("💡 Lưu ý: Tuyệt đối không được viết chữ I, X quá 3 lần liên tiếp.", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        n2_2 = Text("   Bắt buộc dùng quy tắc trừ: IV = 5 - 1  ;  IX = 10 - 1", font=FONT_FAMILY, font_size=24, color=COLOR_CYAN)

        c2_content = VGroup(t2_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_AMBER), w2, r2, n2_1, n2_2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fit_safe_box(c2_content, max_width=10.8, max_height=4.6)
        c2_content.move_to([0, -0.4, 0])

        c2_box = RoundedRectangle(corner_radius=0.3, width=c2_content.width + 0.8, height=c2_content.height + 0.65, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c2_content.get_center())
        card2 = VGroup(c2_box, c2_content)

        anim_t2 = 0.6 + 0.6 + 0.6 + 0.6 + 0.7
        avail_t2 = max(0.2, t_t2 - fade_out_dur)
        scale_t2 = min(1.0, (avail_t2 - 0.2) / max(0.1, anim_t2)) if anim_t2 > avail_t2 else 1.0

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.6 * scale_t2)
        self.play(Write(t2_head), run_time=0.6 * scale_t2)
        self.play(FadeIn(w2, shift=RIGHT), run_time=0.6 * scale_t2)
        self.play(FadeIn(r2, shift=RIGHT), run_time=0.6 * scale_t2)
        self.play(FadeIn(n2_1), FadeIn(n2_2), run_time=0.7 * scale_t2)

        actual_anim2 = anim_t2 * scale_t2
        rem_t2 = max(0.15, avail_t2 - actual_anim2)
        self.wait(rem_t2)
        self.play(FadeOut(card2, shift=UP*0.25), run_time=fade_out_dur)

        # -------------------------------------------------------------
        # TRAP 3: QUÊN ĐIỀU KIỆN CHỮ SỐ ĐẦU TIÊN KHÁC 0
        # -------------------------------------------------------------
        a_t3 = os.path.join(audio_dir, "scene4_trap3.mp3")
        t_t3 = get_audio_duration(a_t3, fallback=timing.get("scene4_trap3", 11.28))

        t3_head = Text("LỖI SAI 3: QUÊN ĐIỀU KIỆN CHỮ SỐ ĐẦU TIÊN KHÁC 0", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        w3 = Text("✗ SAI:   Tìm số ab mà cho chữ số hàng chục a = 0 (ví dụ số 05)", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_ROSE)
        r3 = Text("✓ ĐÚNG:  Chữ số hàng cao nhất bắt buộc phải khác 0 (a ∈ ℕ*, a ≠ 0)", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_EMERALD)
        n3_1 = Text("💡 Lưu ý: Số tự nhiên có 2 chữ số ab thì a phải từ 1 đến 9, b từ 0 đến 9.", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        n3_2 = Text("   Luôn đặt điều kiện a ≠ 0 để không bị mất điểm điều kiện trong bài tự luận!", font=FONT_FAMILY, font_size=24, color=COLOR_CYAN)

        c3_content = VGroup(t3_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_CYAN), w3, r3, n3_1, n3_2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fit_safe_box(c3_content, max_width=10.8, max_height=4.6)
        c3_content.move_to([0, -0.4, 0])

        c3_box = RoundedRectangle(corner_radius=0.3, width=c3_content.width + 0.8, height=c3_content.height + 0.65, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c3_content.get_center())
        card3 = VGroup(c3_box, c3_content)

        anim_t3 = 0.6 + 0.6 + 0.6 + 0.6 + 0.7
        avail_t3 = max(0.2, t_t3 - fade_out_dur)
        scale_t3 = min(1.0, (avail_t3 - 0.2) / max(0.1, anim_t3)) if anim_t3 > avail_t3 else 1.0

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.6 * scale_t3)
        self.play(Write(t3_head), run_time=0.6 * scale_t3)
        self.play(FadeIn(w3, shift=RIGHT), run_time=0.6 * scale_t3)
        self.play(FadeIn(r3, shift=RIGHT), run_time=0.6 * scale_t3)
        self.play(FadeIn(n3_1), FadeIn(n3_2), run_time=0.7 * scale_t3)

        actual_anim3 = anim_t3 * scale_t3
        rem_t3 = max(0.15, avail_t3 - actual_anim3)
        self.wait(rem_t3)
        self.play(FadeOut(card3, shift=UP*0.25), run_time=fade_out_dur)

        # -------------------------------------------------------------
        # TRAP 4: ĐẶT KÝ HIỆU TRỪ LA MÃ SAI QUY TẮC
        # -------------------------------------------------------------
        a_t4 = os.path.join(audio_dir, "scene4_trap4.mp3")
        t_t4 = get_audio_duration(a_t4, fallback=timing.get("scene4_trap4", 32.33))

        t4_head = Text("LỖI SAI 4: ĐẶT KÝ HIỆU TRỪ LA MÃ SAI QUY TẮC", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_AMBER)
        w4 = Text("✗ SAI:   Viết 49 là IL (lấy 50 - 1)  ;  Viết 99 là IC (lấy 100 - 1)", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_ROSE)
        r4 = Text("✓ ĐÚNG:  49 = XLIX (40 + 9)  ;  99 = XCIX (90 + 9)", font=FONT_FAMILY, font_size=25, weight=BOLD, color=COLOR_EMERALD)
        n4_1 = Text("💡 Lưu ý: Chữ I chỉ được phép đứng trước V và X mà thôi.", font=FONT_FAMILY, font_size=24, color=COLOR_TEXT_MAIN)
        n4_2 = Text("   Bắt buộc tách theo hàng: Hàng chục trước rồi đến hàng đơn vị!", font=FONT_FAMILY, font_size=24, color=COLOR_CYAN)

        c4_content = VGroup(t4_head, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_INDIGO), w4, r4, n4_1, n4_2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fit_safe_box(c4_content, max_width=10.8, max_height=4.6)
        c4_content.move_to([0, -0.4, 0])

        c4_box = RoundedRectangle(corner_radius=0.3, width=c4_content.width + 0.8, height=c4_content.height + 0.65, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c4_content.get_center())
        card4 = VGroup(c4_box, c4_content)

        anim_t4 = 0.6 + 0.6 + 0.6 + 0.6 + 0.7
        avail_t4 = max(0.2, t_t4)
        scale_t4 = min(1.0, (avail_t4 - 0.2) / max(0.1, anim_t4)) if anim_t4 > avail_t4 else 1.0

        self.play(FadeIn(c4_box, scale=0.96), run_time=0.6 * scale_t4)
        self.play(Write(t4_head), run_time=0.6 * scale_t4)
        self.play(FadeIn(w4, shift=RIGHT), run_time=0.6 * scale_t4)
        self.play(FadeIn(r4, shift=RIGHT), run_time=0.6 * scale_t4)
        self.play(FadeIn(n4_1), FadeIn(n4_2), run_time=0.7 * scale_t4)

        actual_anim4 = anim_t4 * scale_t4
        rem_t4 = max(0.15, avail_t4 - actual_anim4)
        self.wait(rem_t4)


if __name__ == "__main__":
    pass
