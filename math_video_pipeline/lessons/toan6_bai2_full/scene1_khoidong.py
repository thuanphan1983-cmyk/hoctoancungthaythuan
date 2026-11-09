"""
SCENE 1: ĐẶT VẤN ĐỀ & KHỞI ĐỘNG THỰC TẾ (BÀI 2 FULL 14-16 PHÚT)
Bài 2: Cách ghi số tự nhiên (Toán 6 - Kết nối tri thức)
Giáo viên: Thầy Thuấn Phan
Quy chuẩn:
- Strict Safe-Zone & Auto-Scale: fit_safe_box (max_width=10.8, max_height=4.8, margins >= 1.2 x 0.8)
- Audio-Visual Sync chính xác từng mili-giây (mutagen MP3 get_audio_duration, 1:1 sync)
- Font Arial Unicode MS (Zero Hex Boxes)
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


class Scene1KhoiDong(Scene):
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
        a_s1 = os.path.join(audio_dir, "scene1_slide1.mp3")
        t_s1 = get_audio_duration(a_s1, fallback=timing.get("scene1_slide1", 38.0))

        c1_title = Text("HỌC TOÁN CÙNG THẦY THUẤN PHAN", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_AMBER)
        c1_sub = Text("Toán 6 • Kết Nối Tri Thức Với Cuộc Sống", font=FONT_FAMILY, font_size=26, weight=SEMIBOLD, color=COLOR_CYAN)
        b1_1 = Text("• Bài 2: Cách ghi số tự nhiên", font=FONT_FAMILY, font_size=28, weight=BOLD, color=COLOR_TEXT_MAIN)
        b1_2 = Text("• Hệ thập phân & Cấu tạo số tự nhiên", font=FONT_FAMILY, font_size=28, color=COLOR_TEXT_MAIN)
        b1_3 = Text("• Chữ số La Mã cổ đại trong đời sống hiện đại", font=FONT_FAMILY, font_size=28, color=COLOR_EMERALD)

        c1_content = VGroup(c1_title, c1_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_AMBER), b1_1, b1_2, b1_3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_safe_box(c1_content, max_width=10.8, max_height=4.8)
        c1_content.move_to([0, -0.4, 0])

        c1_box = RoundedRectangle(corner_radius=0.3, width=c1_content.width + 0.8, height=c1_content.height + 0.65, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c1_content.get_center())
        card1 = VGroup(c1_box, c1_content)

        anim_s1 = 0.6 + 1.0 + 0.7 + 0.7 + 0.7
        fade_out_dur = 0.6
        avail_s1 = max(0.2, t_s1 - fade_out_dur)
        scale_s1 = min(1.0, (avail_s1 - 0.2) / max(0.1, anim_s1)) if anim_s1 > avail_s1 else 1.0

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.6 * scale_s1)
        self.play(Write(c1_title), FadeIn(c1_sub, shift=UP), run_time=1.0 * scale_s1)
        self.play(FadeIn(b1_1, shift=RIGHT), run_time=0.7 * scale_s1)
        self.play(FadeIn(b1_2, shift=RIGHT), run_time=0.7 * scale_s1)
        self.play(FadeIn(b1_3, shift=RIGHT), run_time=0.7 * scale_s1)

        actual_anim1 = anim_s1 * scale_s1
        rem_s1 = max(0.15, avail_s1 - actual_anim1)
        self.wait(rem_s1)
        self.play(FadeOut(card1, shift=UP*0.25), run_time=fade_out_dur)

        # -------------------------------------------------------------
        # SLIDE 2: CÁC CON SỐ KHỔNG LỒ TRONG ĐỜI SỐNG
        # -------------------------------------------------------------
        a_s2 = os.path.join(audio_dir, "scene1_slide2.mp3")
        t_s2 = get_audio_duration(a_s2, fallback=timing.get("scene1_slide2", 35.0))

        c2_title = Text("CÁC CON SỐ KHỔNG LỒ TRONG ĐỜI SỐNG", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_CYAN)
        c2_sub = Text("Từ tiền tệ, dân số đến khoảng cách thiên văn", font=FONT_FAMILY, font_size=25, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        b2_1 = Text("👥 Dân số Việt Nam: Hơn 100 000 000 người", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_TEXT_MAIN)
        b2_2 = Text("🚀 Khoảng cách Trái Đất - Mặt Trăng: 384 400 km", font=FONT_FAMILY, font_size=27, color=COLOR_TEXT_MAIN)
        b2_3 = Text("💳 Căn cước công dân 12 chữ số, biển số xe, mã vạch", font=FONT_FAMILY, font_size=27, color=COLOR_AMBER)
        b2_4 = Text("➔ Làm thế nào để ghi và đọc chính xác mọi số tự nhiên?", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_EMERALD)

        c2_content = VGroup(c2_title, c2_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_CYAN), b2_1, b2_2, b2_3, b2_4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fit_safe_box(c2_content, max_width=10.8, max_height=4.8)
        c2_content.move_to([0, -0.4, 0])

        c2_box = RoundedRectangle(corner_radius=0.3, width=c2_content.width + 0.8, height=c2_content.height + 0.65, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c2_content.get_center())
        card2 = VGroup(c2_box, c2_content)

        anim_s2 = 0.6 + 0.8 + 0.7 + 0.8 + 0.7
        avail_s2 = max(0.2, t_s2 - fade_out_dur)
        scale_s2 = min(1.0, (avail_s2 - 0.2) / max(0.1, anim_s2)) if anim_s2 > avail_s2 else 1.0

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.6 * scale_s2)
        self.play(Write(c2_title), FadeIn(c2_sub, shift=UP), run_time=0.8 * scale_s2)
        self.play(FadeIn(b2_1, shift=RIGHT), run_time=0.7 * scale_s2)
        self.play(FadeIn(b2_2, shift=RIGHT), FadeIn(b2_3, shift=RIGHT), run_time=0.8 * scale_s2)
        self.play(FadeIn(b2_4, scale=1.03), run_time=0.7 * scale_s2)

        actual_anim2 = anim_s2 * scale_s2
        rem_s2 = max(0.15, avail_s2 - actual_anim2)
        self.wait(rem_s2)
        self.play(FadeOut(card2, shift=UP*0.25), run_time=fade_out_dur)

        # -------------------------------------------------------------
        # SLIDE 3: PHÂN BIỆT RÕ: SỐ VÀ CHỮ SỐ
        # -------------------------------------------------------------
        a_s3 = os.path.join(audio_dir, "scene1_slide3.mp3")
        t_s3 = get_audio_duration(a_s3, fallback=timing.get("scene1_slide3", 40.0))

        c3_title = Text("PHÂN BIỆT RÕ: SỐ VÀ CHỮ SỐ", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_EMERALD)
        c3_sub = Text("Bản chất toán học nền tảng không thể nhầm lẫn", font=FONT_FAMILY, font_size=25, weight=SEMIBOLD, color=COLOR_TEXT_MUTED)
        b3_1 = Text("📖 Ngôn ngữ: 29 chữ cái ghép thành hàng vạn từ ngữ phong phú", font=FONT_FAMILY, font_size=27, color=COLOR_TEXT_MAIN)
        b3_2 = Text("🔢 Toán học: Đúng 10 chữ số (0, 1, 2, ..., 9) tạo nên vô tận số", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_CYAN)
        b3_3 = Text("💡 Ví dụ: Năm 2026 là một SỐ, được viết bởi 4 CHỮ SỐ: 2, 0, 2, 6", font=FONT_FAMILY, font_size=27, color=COLOR_AMBER)

        c3_content = VGroup(c3_title, c3_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD), b3_1, b3_2, b3_3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_safe_box(c3_content, max_width=10.8, max_height=4.8)
        c3_content.move_to([0, -0.4, 0])

        c3_box = RoundedRectangle(corner_radius=0.3, width=c3_content.width + 0.8, height=c3_content.height + 0.65, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c3_content.get_center())
        card3 = VGroup(c3_box, c3_content)

        anim_s3 = 0.6 + 0.8 + 0.7 + 0.7 + 0.8
        avail_s3 = max(0.2, t_s3 - fade_out_dur)
        scale_s3 = min(1.0, (avail_s3 - 0.2) / max(0.1, anim_s3)) if anim_s3 > avail_s3 else 1.0

        self.play(FadeIn(c3_box, scale=0.96), run_time=0.6 * scale_s3)
        self.play(Write(c3_title), FadeIn(c3_sub, shift=UP), run_time=0.8 * scale_s3)
        self.play(FadeIn(b3_1, shift=RIGHT), run_time=0.7 * scale_s3)
        self.play(FadeIn(b3_2, shift=RIGHT), run_time=0.7 * scale_s3)
        self.play(FadeIn(b3_3, shift=RIGHT), run_time=0.8 * scale_s3)

        actual_anim3 = anim_s3 * scale_s3
        rem_s3 = max(0.15, avail_s3 - actual_anim3)
        self.wait(rem_s3)
        self.play(FadeOut(card3, shift=UP*0.25), run_time=fade_out_dur)

        # -------------------------------------------------------------
        # SLIDE 4: DẤU ẤN LỊCH SỬ: CHỮ SỐ LA MÃ
        # -------------------------------------------------------------
        a_s4 = os.path.join(audio_dir, "scene1_slide4.mp3")
        t_s4 = get_audio_duration(a_s4, fallback=timing.get("scene1_slide4", 30.0))

        c4_title = Text("DẤU ẤN LỊCH SỬ: CHỮ SỐ LA MÃ", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_AMBER)
        c4_sub = Text("Di sản văn hóa cổ đại vẫn hiện diện hằng ngày", font=FONT_FAMILY, font_size=25, weight=SEMIBOLD, color=COLOR_CYAN)
        b4_1 = Text("⏰ Mặt đồng hồ đeo tay và đồng hồ treo tường cổ điển: I, II, III, IV...", font=FONT_FAMILY, font_size=27, color=COLOR_TEXT_MAIN)
        b4_2 = Text("📜 Ký hiệu thế kỷ lịch sử: Thế kỷ XXI (thế kỷ 21)", font=FONT_FAMILY, font_size=27, color=COLOR_TEXT_MAIN)
        b4_3 = Text("📚 Đánh số thứ tự các chương, phần: Chương I, Chương II", font=FONT_FAMILY, font_size=27, color=COLOR_AMBER)
        b4_4 = Text("Mời các em bước vào PHẦN 2: HÌNH THÀNH KIẾN THỨC MỚI!", font=FONT_FAMILY, font_size=27, weight=BOLD, color=COLOR_EMERALD)

        c4_content = VGroup(c4_title, c4_sub, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_INDIGO), b4_1, b4_2, b4_3, b4_4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fit_safe_box(c4_content, max_width=10.8, max_height=4.8)
        c4_content.move_to([0, -0.4, 0])

        c4_box = RoundedRectangle(corner_radius=0.3, width=c4_content.width + 0.8, height=c4_content.height + 0.65, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c4_content.get_center())
        card4 = VGroup(c4_box, c4_content)

        anim_s4 = 0.6 + 0.8 + 0.7 + 0.8 + 0.8
        avail_s4 = max(0.2, t_s4)
        scale_s4 = min(1.0, (avail_s4 - 0.2) / max(0.1, anim_s4)) if anim_s4 > avail_s4 else 1.0

        self.play(FadeIn(c4_box, scale=0.96), run_time=0.6 * scale_s4)
        self.play(Write(c4_title), FadeIn(c4_sub, shift=UP), run_time=0.8 * scale_s4)
        self.play(FadeIn(b4_1, shift=RIGHT), run_time=0.7 * scale_s4)
        self.play(FadeIn(b4_2, shift=RIGHT), FadeIn(b4_3, shift=RIGHT), run_time=0.8 * scale_s4)
        self.play(FadeIn(b4_4, scale=1.03), run_time=0.8 * scale_s4)

        actual_anim4 = anim_s4 * scale_s4
        rem_s4 = max(0.15, avail_s4 - actual_anim4)
        self.wait(rem_s4)


if __name__ == "__main__":
    pass
