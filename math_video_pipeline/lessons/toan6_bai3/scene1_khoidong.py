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

COLOR_BG = "#0f172a"
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

def math_text(expr, font_size=24, color=COLOR_TEXT_MAIN, weight=BOLD):
    return Text(expr, font=MATH_FONT, font_size=font_size, weight=weight, color=color)

def wrap_text(text: str, max_chars: int = 50) -> str:
    """Tự động ngắt dòng thông minh không cắt ngang từ"""
    words = text.split()
    lines = []
    cur_line = []
    cur_len = 0
    for w in words:
        if cur_len + len(w) + (1 if cur_line else 0) <= max_chars:
            cur_line.append(w)
            cur_len += len(w) + (1 if len(cur_line) > 1 else 0)
        else:
            if cur_line:
                lines.append(" ".join(cur_line))
            cur_line = [w]
            cur_len = len(w)
    if cur_line:
        lines.append(" ".join(cur_line))
    return "\n".join(lines)

def safe_text(txt, font=FONT_FAMILY, font_size=24, weight=NORMAL, color=COLOR_TEXT_MAIN, max_width=9.5, max_chars=50):
    if len(txt) > max_chars and "\n" not in txt:
        txt = wrap_text(txt, max_chars=max_chars)
    t = Text(txt, font=font, font_size=font_size, weight=weight, color=color, line_spacing=0.85)
    if t.width > max_width:
        t.scale_to_fit_width(max_width)
    return t

def fit_safe_box(content_mobject, max_width=9.6, max_height=4.8):
    """Auto-scale helper: Giữ toàn bộ nội dung nằm an toàn ở phần bên phải mascot"""
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

def get_mascot(name="thay_giang.png", height=2.45):
    """Tìm và trả về ImageMobject mascot Chibi Thầy Thuận ở góc DL"""
    candidates = [
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "mascot", name)),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "mascot", name)),
        os.path.abspath(os.path.join(os.getcwd(), "assets", "mascot", name)),
        os.path.abspath(os.path.join(os.getcwd(), "math_video_pipeline", "assets", "mascot", name)),
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                m = ImageMobject(p)
                m.set_height(height)
                m.to_corner(DL, buff=0.35)
                return m
            except Exception:
                pass
    return None


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

        header = Text("PHẦN 1: ĐẶT VẤN ĐỀ & KHỞI ĐỘNG THỰC TẾ", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=2, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=0.8)

        # Mascot Thầy Thuận giảng bài ở góc DL
        mascot = get_mascot("thay_giang.png")
        if mascot:
            self.play(FadeIn(mascot, shift=UP*0.2), run_time=0.6)

        # ----------------- SLIDE 1 -----------------
        a_s1 = os.path.join(audio_dir, "scene1_slide1.mp3")
        t_s1 = get_audio_duration(a_s1, fallback=timing.get("scene1_slide1", 22.0))

        c1_title = safe_text("1. KHỞI ĐỘNG: BẢNG XẾP HẠNG VÀ THỨ TỰ ĐỜI SỐNG", font_size=26, weight=BOLD, color=COLOR_AMBER, max_width=9.2)
        c1_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_AMBER)
        c1_sub = safe_text("Trong đời sống, việc so sánh và sắp xếp thứ tự diễn ra liên tục hàng ngày", font_size=20, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        itms_1 = []
        itms_1.append(safe_text("• Xếp thứ tự điểm số của các đội bóng trên bảng xếp hạng thể thao", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_1.append(safe_text("• Đo chiều cao các học sinh trong lớp để sắp xếp hàng tập thể dục", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_1.append(safe_text("• Thứ tự số thứ tự tại quầy bốc thăm, bệnh viện, sân bay hoặc ngân hàng", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_1.append(safe_text("• Làm thế nào để so sánh chuẩn xác hai số tự nhiên bất kỳ trong toán học?", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))

        c1_content = VGroup(c1_title, c1_line, c1_sub, *itms_1).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(c1_content, max_width=9.4, max_height=4.6)
        c1_content.move_to([0.65, -0.35, 0])

        c1_box = RoundedRectangle(corner_radius=0.3, width=c1_content.width + 0.6, height=c1_content.height + 0.6, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c1_content.get_center())
        card1 = VGroup(c1_box, c1_content)

        anim_base = 0.5 + 0.6 + len(itms_1) * 0.3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_s1 - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.6 * anim_scale
        rt_item = 0.3 * anim_scale

        self.play(FadeIn(c1_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(c1_title, shift=DOWN*0.1), FadeIn(c1_sub, shift=UP*0.1), run_time=rt_head)
        for itm in itms_1:
            self.play(FadeIn(itm, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + len(itms_1) * rt_item
        rem_s1 = max(0.15, avail_time - actual_anim)
        self.wait(rem_s1)
        self.play(FadeOut(card1, shift=UP*0.25), run_time=fade_out_dur)

        # ----------------- SLIDE 2 -----------------
        a_s2 = os.path.join(audio_dir, "scene1_slide2.mp3")
        t_s2 = get_audio_duration(a_s2, fallback=timing.get("scene1_slide2", 22.0))

        c2_title = safe_text("2. TÌNH HUỐNG THỰC TẾ: ĐỘ CAO CÁC ĐỈNH NÚI TẠI VIỆT NAM", font_size=26, weight=BOLD, color=COLOR_CYAN, max_width=9.2)
        c2_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_CYAN)
        c2_sub = safe_text("So sánh độ cao các đỉnh núi hùng vĩ của quê hương đất nước", font_size=20, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        itms_2 = []
        itms_2.append(safe_text("• Đỉnh Phan Xi Păng (Lào Cai): cao 3.143 mét so với mực nước biển", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_2.append(safe_text("• Đỉnh Pu Si Lung (Lai Châu): cao 3.083 mét", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_2.append(safe_text("• Đỉnh Pu Ta Leng (Lai Châu): cao 3.049 mét", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_2.append(safe_text("• Làm sao để biết đỉnh núi nào cao nhất và sắp xếp theo thứ tự giảm dần?", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))

        c2_content = VGroup(c2_title, c2_line, c2_sub, *itms_2).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(c2_content, max_width=9.4, max_height=4.6)
        c2_content.move_to([0.65, -0.35, 0])

        c2_box = RoundedRectangle(corner_radius=0.3, width=c2_content.width + 0.6, height=c2_content.height + 0.6, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c2_content.get_center())
        card2 = VGroup(c2_box, c2_content)

        anim_base = 0.5 + 0.6 + len(itms_2) * 0.3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_s2 - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.6 * anim_scale
        rt_item = 0.3 * anim_scale

        self.play(FadeIn(c2_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(c2_title, shift=DOWN*0.1), FadeIn(c2_sub, shift=UP*0.1), run_time=rt_head)
        for itm in itms_2:
            self.play(FadeIn(itm, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + len(itms_2) * rt_item
        rem_s2 = max(0.15, avail_time - actual_anim)
        self.wait(rem_s2)
        self.play(FadeOut(card2, shift=UP*0.25), run_time=fade_out_dur)

        # ----------------- SLIDE 3 -----------------
        a_s3 = os.path.join(audio_dir, "scene1_slide3.mp3")
        t_s3 = get_audio_duration(a_s3, fallback=timing.get("scene1_slide3", 22.0))

        c3_title = safe_text("3. TÌNH HUỐNG KINH TẾ: DÂN SỐ CÁC ĐÔ THỊ LỚN", font_size=26, weight=BOLD, color=COLOR_EMERALD, max_width=9.2)
        c3_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_EMERALD)
        c3_sub = safe_text("So sánh quy mô dân số và số lượng hàng hóa sản xuất", font_size=20, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        itms_3 = []
        itms_3.append(safe_text("• Quy mô dân số các thành phố lớn lên tới hàng triệu, chục triệu người", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_3.append(safe_text("• Khi các số có nhiều chữ số khác nhau, ta so sánh như thế nào?", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_3.append(safe_text("• Số có 7 chữ số luôn bé hơn số có 8 chữ số", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_3.append(safe_text("• Biểu diễn thứ tự giúp các nhà quản lý đưa ra quyết định chính xác", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))

        c3_content = VGroup(c3_title, c3_line, c3_sub, *itms_3).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(c3_content, max_width=9.4, max_height=4.6)
        c3_content.move_to([0.65, -0.35, 0])

        c3_box = RoundedRectangle(corner_radius=0.3, width=c3_content.width + 0.6, height=c3_content.height + 0.6, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c3_content.get_center())
        card3 = VGroup(c3_box, c3_content)

        anim_base = 0.5 + 0.6 + len(itms_3) * 0.3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_s3 - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.6 * anim_scale
        rt_item = 0.3 * anim_scale

        self.play(FadeIn(c3_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(c3_title, shift=DOWN*0.1), FadeIn(c3_sub, shift=UP*0.1), run_time=rt_head)
        for itm in itms_3:
            self.play(FadeIn(itm, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + len(itms_3) * rt_item
        rem_s3 = max(0.15, avail_time - actual_anim)
        self.wait(rem_s3)
        self.play(FadeOut(card3, shift=UP*0.25), run_time=fade_out_dur)

        # ----------------- SLIDE 4 -----------------
        a_s4 = os.path.join(audio_dir, "scene1_slide4.mp3")
        t_s4 = get_audio_duration(a_s4, fallback=timing.get("scene1_slide4", 22.0))

        c4_title = safe_text("4. MỤC TIÊU CẦN ĐẠT CỦA BÀI HỌC", font_size=26, weight=BOLD, color=COLOR_INDIGO, max_width=9.2)
        c4_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_INDIGO)
        c4_sub = safe_text("Chuẩn đầu ra môn Toán 6 theo chương trình giáo dục phổ thông 2018", font_size=20, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        itms_4 = []
        itms_4.append(safe_text("• Hiểu rõ khái niệm tia số và cách biểu diễn số tự nhiên trên tia số", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_4.append(safe_text("• Nắm vững quy tắc so sánh hai số tự nhiên trong hệ thập phân", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_4.append(safe_text("• Phân biệt thành thạo số liền trước, số liền sau và tính chất bắc cầu", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))
        itms_4.append(safe_text("• Vận dụng giải thành thạo bài toán thực tế và tránh mọi bẫy thi thường gặp", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))

        c4_content = VGroup(c4_title, c4_line, c4_sub, *itms_4).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(c4_content, max_width=9.4, max_height=4.6)
        c4_content.move_to([0.65, -0.35, 0])

        c4_box = RoundedRectangle(corner_radius=0.3, width=c4_content.width + 0.6, height=c4_content.height + 0.6, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c4_content.get_center())
        card4 = VGroup(c4_box, c4_content)

        anim_base = 0.5 + 0.6 + len(itms_4) * 0.3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_s4 - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.6 * anim_scale
        rt_item = 0.3 * anim_scale

        self.play(FadeIn(c4_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(c4_title, shift=DOWN*0.1), FadeIn(c4_sub, shift=UP*0.1), run_time=rt_head)
        for itm in itms_4:
            self.play(FadeIn(itm, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + len(itms_4) * rt_item
        rem_s4 = max(0.15, avail_time - actual_anim)
        self.wait(rem_s4)
        self.play(FadeOut(card4, shift=UP*0.25), run_time=fade_out_dur)

        if mascot:
            self.play(FadeOut(mascot, shift=DOWN*0.2), run_time=0.5)

if __name__ == "__main__":
    pass
