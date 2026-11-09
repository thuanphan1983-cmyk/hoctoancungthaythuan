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

        header = Text("PHẦN 4: CẢNH BÁO CÁC BẪY SAI LẦM PHỔ BIẾN", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_ROSE)
        header_line = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=2, color=COLOR_ROSE)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=0.8)

        mascot = get_mascot("thay_giang.png")
        if mascot:
            self.play(FadeIn(mascot, shift=UP*0.2), run_time=0.6)

        # ----------------- BẪY 1 -----------------
        a_t1 = os.path.join(audio_dir, "scene4_trap1.mp3")
        t_t1 = get_audio_duration(a_t1, fallback=timing.get("scene4_trap1", 24.0))

        t1_title = Text("BẪY 1: TÌM SỐ LIỀN TRƯỚC CỦA SỐ 0", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_ROSE)
        t1_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_ROSE)
        t1_w = safe_text("✗ Sai lầm: Cho rằng số liền trước của 0 là -1 hoặc khẳng định số 0 có số liền trước", font_size=20, weight=BOLD, color=COLOR_ROSE, max_width=9.2, max_chars=48)
        t1_r = safe_text("• Nguyên nhân: Trong tập số tự nhiên N = {0; 1; 2; ...}, số 0 là phần tử nhỏ nhất đứng đầu tia số", font_size=19, color=COLOR_TEXT_MUTED, max_width=9.2, max_chars=48)
        t1_c = safe_text("✓ Cách làm đúng: Khẳng định chuẩn xác: Số 0 KHÔNG CÓ số liền trước trong tập hợp các số tự nhiên N", font_size=20, weight=BOLD, color=COLOR_EMERALD, max_width=9.2, max_chars=48)

        t1_content = VGroup(t1_title, t1_line, t1_w, t1_r, t1_c).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(t1_content, max_width=9.4, max_height=4.6)
        t1_content.move_to([0.65, -0.35, 0])

        t1_box = RoundedRectangle(corner_radius=0.3, width=t1_content.width + 0.6, height=t1_content.height + 0.6, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(t1_content.get_center())
        card1 = VGroup(t1_box, t1_content)

        anim_base = 0.5 + 0.5 + 0.35 * 3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_t1 - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.5 * anim_scale
        rt_item = 0.35 * anim_scale

        self.play(FadeIn(t1_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(t1_title, shift=DOWN*0.1), run_time=rt_head)
        self.play(FadeIn(t1_w, shift=RIGHT*0.2), run_time=rt_item)
        self.play(FadeIn(t1_r, shift=RIGHT*0.2), run_time=rt_item)
        self.play(FadeIn(t1_c, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + 3 * rt_item
        rem_t1 = max(0.15, avail_time - actual_anim)
        self.wait(rem_t1)
        self.play(FadeOut(card1, shift=UP*0.25), run_time=fade_out_dur)

        # ----------------- BẪY 2 -----------------
        a_t2 = os.path.join(audio_dir, "scene4_trap2.mp3")
        t_t2 = get_audio_duration(a_t2, fallback=timing.get("scene4_trap2", 24.0))

        t2_title = Text("BẪY 2: HIỂU SAI KÝ HIỆU NHỎ HƠN HOẶC BẰNG (<=)", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_ROSE)
        t2_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_ROSE)
        t2_w = safe_text("✗ Sai lầm: Cho rằng số a <= b bắt buộc phải vừa nhỏ hơn vừa bằng b (vô lý)", font_size=20, weight=BOLD, color=COLOR_ROSE, max_width=9.2, max_chars=48)
        t2_r = safe_text("• Nguyên nhân: Ký hiệu <= mang ý nghĩa quan hệ tuyển logic: hoặc là a < b, HOẶC là a = b", font_size=19, color=COLOR_TEXT_MUTED, max_width=9.2, max_chars=48)
        t2_c = safe_text("✓ Cách làm đúng: Chỉ cần một trong hai điều kiện xảy ra thì khẳng định a <= b là hoàn toàn đúng", font_size=20, weight=BOLD, color=COLOR_EMERALD, max_width=9.2, max_chars=48)

        t2_content = VGroup(t2_title, t2_line, t2_w, t2_r, t2_c).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(t2_content, max_width=9.4, max_height=4.6)
        t2_content.move_to([0.65, -0.35, 0])

        t2_box = RoundedRectangle(corner_radius=0.3, width=t2_content.width + 0.6, height=t2_content.height + 0.6, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(t2_content.get_center())
        card2 = VGroup(t2_box, t2_content)

        anim_base = 0.5 + 0.5 + 0.35 * 3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_t2 - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.5 * anim_scale
        rt_item = 0.35 * anim_scale

        self.play(FadeIn(t2_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(t2_title, shift=DOWN*0.1), run_time=rt_head)
        self.play(FadeIn(t2_w, shift=RIGHT*0.2), run_time=rt_item)
        self.play(FadeIn(t2_r, shift=RIGHT*0.2), run_time=rt_item)
        self.play(FadeIn(t2_c, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + 3 * rt_item
        rem_t2 = max(0.15, avail_time - actual_anim)
        self.wait(rem_t2)
        self.play(FadeOut(card2, shift=UP*0.25), run_time=fade_out_dur)

        # ----------------- BẪY 3 -----------------
        a_t3 = os.path.join(audio_dir, "scene4_trap3.mp3")
        t_t3 = get_audio_duration(a_t3, fallback=timing.get("scene4_trap3", 24.0))

        t3_title = Text("BẪY 3: QUÊN ĐẾM SỐ CHỮ SỐ KHI SO SÁNH", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_ROSE)
        t3_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_ROSE)
        t3_w = safe_text("✗ Sai lầm: So sánh 9999 và 10001 lại vội kết luận 9999 > 10001 vì thấy chữ số 9 > 1", font_size=20, weight=BOLD, color=COLOR_ROSE, max_width=9.2, max_chars=48)
        t3_r = safe_text("• Nguyên nhân: Chưa thực hiện Bước 1: Đếm số chữ số mà đã vội vàng so sánh chữ số hàng đầu", font_size=19, color=COLOR_TEXT_MUTED, max_width=9.2, max_chars=48)
        t3_c = safe_text("✓ Cách làm đúng: Luôn đếm số chữ số trước: 9999 có 4 chữ số, 10001 có 5 chữ số nên 9999 < 10001", font_size=20, weight=BOLD, color=COLOR_EMERALD, max_width=9.2, max_chars=48)

        t3_content = VGroup(t3_title, t3_line, t3_w, t3_r, t3_c).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(t3_content, max_width=9.4, max_height=4.6)
        t3_content.move_to([0.65, -0.35, 0])

        t3_box = RoundedRectangle(corner_radius=0.3, width=t3_content.width + 0.6, height=t3_content.height + 0.6, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(t3_content.get_center())
        card3 = VGroup(t3_box, t3_content)

        anim_base = 0.5 + 0.5 + 0.35 * 3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_t3 - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.5 * anim_scale
        rt_item = 0.35 * anim_scale

        self.play(FadeIn(t3_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(t3_title, shift=DOWN*0.1), run_time=rt_head)
        self.play(FadeIn(t3_w, shift=RIGHT*0.2), run_time=rt_item)
        self.play(FadeIn(t3_r, shift=RIGHT*0.2), run_time=rt_item)
        self.play(FadeIn(t3_c, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + 3 * rt_item
        rem_t3 = max(0.15, avail_time - actual_anim)
        self.wait(rem_t3)
        self.play(FadeOut(card3, shift=UP*0.25), run_time=fade_out_dur)

        # ----------------- BẪY 4 -----------------
        a_t4 = os.path.join(audio_dir, "scene4_trap4.mp3")
        t_t4 = get_audio_duration(a_t4, fallback=timing.get("scene4_trap4", 24.0))

        t4_title = Text("BẪY 4: BỎ SÓT HOẶC THỪA ĐẦU MÚT TRONG BẤT ĐẲNG THỨC KÉP", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_ROSE)
        t4_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_ROSE)
        t4_w = safe_text("✗ Sai lầm: Liệt kê x trong điều kiện a <= x < b nhưng lại bỏ quên a hoặc lấy luôn cả b", font_size=20, weight=BOLD, color=COLOR_ROSE, max_width=9.2, max_chars=48)
        t4_r = safe_text("• Nguyên nhân: Không phân biệt rạch ròi giữa dấu có gạch dưới (<=, lấy đầu mút) và dấu không có gạch (<, bỏ đầu mút)", font_size=19, color=COLOR_TEXT_MUTED, max_width=9.2, max_chars=48)
        t4_c = safe_text("✓ Cách làm đúng: Quy tắc: Có dấu bằng (=) thì LẤY giá trị đó; Không có dấu bằng thì BỎ QUA giá trị đó", font_size=20, weight=BOLD, color=COLOR_EMERALD, max_width=9.2, max_chars=48)

        t4_content = VGroup(t4_title, t4_line, t4_w, t4_r, t4_c).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(t4_content, max_width=9.4, max_height=4.6)
        t4_content.move_to([0.65, -0.35, 0])

        t4_box = RoundedRectangle(corner_radius=0.3, width=t4_content.width + 0.6, height=t4_content.height + 0.6, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(t4_content.get_center())
        card4 = VGroup(t4_box, t4_content)

        anim_base = 0.5 + 0.5 + 0.35 * 3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_t4 - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.5 * anim_scale
        rt_item = 0.35 * anim_scale

        self.play(FadeIn(t4_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(t4_title, shift=DOWN*0.1), run_time=rt_head)
        self.play(FadeIn(t4_w, shift=RIGHT*0.2), run_time=rt_item)
        self.play(FadeIn(t4_r, shift=RIGHT*0.2), run_time=rt_item)
        self.play(FadeIn(t4_c, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + 3 * rt_item
        rem_t4 = max(0.15, avail_time - actual_anim)
        self.wait(rem_t4)
        self.play(FadeOut(card4, shift=UP*0.25), run_time=fade_out_dur)

        if mascot:
            self.play(FadeOut(mascot, shift=DOWN*0.2), run_time=0.5)

if __name__ == "__main__":
    pass
