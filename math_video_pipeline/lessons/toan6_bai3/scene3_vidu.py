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


def build_timer_widget(theme_color=COLOR_AMBER):
    badge = RoundedRectangle(corner_radius=0.15, width=2.4, height=0.85, stroke_color=theme_color, stroke_width=2, fill_color="#0f172a", fill_opacity=0.95).to_corner(UR, buff=0.45)
    vt = ValueTracker(45)
    timer_text = always_redraw(lambda: Text(f"⏱ {int(round(vt.get_value())):02d}s", font="Segoe UI", font_size=24, weight=BOLD, color=theme_color).move_to(badge.get_center() + UP * 0.1))
    pbar_bg = Rectangle(width=2.1, height=0.08, fill_color="#334155", fill_opacity=1, stroke_width=0).move_to(badge.get_center() + DOWN * 0.25)
    def get_pfill():
        val = max(0.0, min(45.0, vt.get_value()))
        w = max(0.01, 2.1 * (val / 45.0))
        rect = Rectangle(width=w, height=0.08, fill_color=theme_color, fill_opacity=1, stroke_width=0)
        rect.move_to(pbar_bg.get_center())
        rect.align_to(pbar_bg, LEFT)
        return rect
    pbar_fill = always_redraw(get_pfill)
    return badge, vt, timer_text, pbar_bg, pbar_fill


class Scene3ViDu(Scene):
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

        header = Text("PHẦN 3: BA VÍ DỤ MINH HỌA & TỰ RÈN LUYỆN", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_AMBER).to_corner(UL, buff=0.45)
        header_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=2, color=COLOR_AMBER).next_to(header, DOWN, buff=0.1, aligned_edge=LEFT)
        header_group = VGroup(header, header_line)
        self.play(FadeIn(header_group, shift=RIGHT), run_time=0.8)

        # Khởi tạo Mascot Thầy Thuận giảng bài ở góc DL
        cur_mascot = get_mascot("thay_giang.png")
        if cur_mascot:
            self.play(FadeIn(cur_mascot, shift=UP*0.2), run_time=0.6)

        # ==================== VÍ DỤ 1 ====================
        a_intro_1 = os.path.join(audio_dir, "scene3_ex1_intro.mp3")
        a_tick = os.path.join(audio_dir, "tick45.mp3")
        a_sol_1 = os.path.join(audio_dir, "scene3_ex1_sol.mp3")

        t_ex1_intro = get_audio_duration(a_intro_1, fallback=timing.get("scene3_ex1_intro", 25.0))
        t_ex1_timer = get_audio_duration(a_tick, fallback=timing.get("scene3_ex1_timer", 45.0))
        t_ex1_sol = get_audio_duration(a_sol_1, fallback=timing.get("scene3_ex1_sol", 40.0))

        # Khung chứa lớn nửa trên (đặt tại x = 0.65, không đè mascot)
        c1_box = RoundedRectangle(corner_radius=0.3, width=10.2, height=5.6, stroke_color=COLOR_CYAN, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0.65, -0.45, 0])

        badge1 = Text("VÍ DỤ 1 (Mức Nhận Biết)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_CYAN)
        head1 = safe_text("ĐIỀN DẤU THÍCH HỢP VÀ TÌM SỐ LIỀN TRƯỚC, LIỀN SAU", font_size=24, weight=BOLD, color=COLOR_AMBER, max_width=9.2)
        sep1 = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_CYAN)
        q1_lead = safe_text("Cho các số tự nhiên: 2026; 2025; 1999 và 10000. Hãy thực hiện:", font_size=21, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        q1_a = safe_text("a) Điền dấu (<, >, =) thích hợp vào ô trống: 2026 ... 2025  và  1999 ... 10000", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        q1_b = safe_text("b) Tìm số liền trước của số 2026 và số liền sau của số 1999", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        bl_sub_1 = []
        bl_sub_1.append(Text("2026 [ ? ] 2025", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER))
        bl_sub_1.append(Text("1999 [ ? ] 10000", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER))
        bl_sub_1.append(Text("Liền trước 2026 = ?", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER))
        bl_sub_1.append(Text("Liền sau 1999 = ?", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER))
        if bl_sub_1:
            def sep(): return Text("  ;  ", font=FONT_FAMILY, font_size=19, color=COLOR_TEXT_MUTED)
            bl_row = VGroup()
            for i_b, b_elem in enumerate(bl_sub_1):
                if i_b > 0:
                    bl_row.add(sep())
                bl_row.add(b_elem)
            bl_row.arrange(RIGHT, buff=0.1)
            fit_safe_box(bl_row, max_width=9.0, max_height=0.45)
            bl_box = RoundedRectangle(corner_radius=0.15, width=bl_row.width + 0.4, height=0.48, stroke_color=COLOR_AMBER, stroke_width=1, fill_color="#0f172a", fill_opacity=0.9).move_to(bl_row.get_center())
            q1_blank_grp = VGroup(bl_box, bl_row)
            problem1_grp = VGroup(badge1, head1, sep1, q1_lead, q1_a, q1_b, q1_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.10)
        else:
            problem1_grp = VGroup(badge1, head1, sep1, q1_lead, q1_a, q1_b).arrange(DOWN, aligned_edge=LEFT, buff=0.11)

        fit_safe_box(problem1_grp, max_width=9.4, max_height=2.5)
        problem1_grp.move_to([0.65, 0.95, 0])

        # BƯỚC 1: Hiện Đề bài (Thầy giảng bài)
        self.play(FadeIn(c1_box, scale=0.96), run_time=0.6)
        self.play(FadeIn(problem1_grp, shift=DOWN * 0.15), run_time=0.8)
        rem_intro1 = max(0.15, t_ex1_intro - 1.4)
        self.wait(rem_intro1)

        # BƯỚC 2: Đồng hồ đếm ngược 45s góc trên phải UR & Thầy đổi sang biểu cảm SUY NGHĨ
        badge_t1, vt1, text_t1, pbg_t1, pfill_t1 = build_timer_widget(COLOR_CYAN)
        timer_grp1 = VGroup(badge_t1, pbg_t1, pfill_t1, text_t1)
        
        mascot_think_1 = get_mascot("thay_suynghi.png")
        if cur_mascot and mascot_think_1:
            self.play(FadeIn(timer_grp1, shift=DOWN*0.3), ReplacementTransform(cur_mascot, mascot_think_1), run_time=0.6)
            cur_mascot = mascot_think_1
        else:
            self.play(FadeIn(timer_grp1, shift=DOWN*0.3), run_time=0.6)

        self.play(vt1.animate.set_value(0), run_time=max(1.0, t_ex1_timer - 1.2), rate_func=linear)
        self.play(FadeOut(timer_grp1, shift=UP*0.2), run_time=0.6)

        # BƯỚC 3: Lời giải chi tiết & Thầy đổi sang biểu cảm KHEN NGỢI (Xuất sắc! ⭐)
        sol1_head = Text("✓ HƯỚNG DẪN GIẢI CHI TIẾT:", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_EMERALD)
        sol1_anal = safe_text("• Phân tích: Áp dụng quy tắc so sánh số chữ số, so sánh từ hàng cao nhất và công thức a - 1, a + 1.", font_size=19, color=COLOR_TEXT_MUTED, max_width=9.2, max_chars=50)
        sol1_a = safe_text("• a) 2026 > 2025 (cùng 4 chữ số, hàng đơn vị 6 > 5) ; 1999 < 10000 (4 chữ số < 5 chữ số).", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=50)
        sol1_b = safe_text("• b) Số liền trước của 2026 là 2026 - 1 = 2025 ; Số liền sau của 1999 là 1999 + 1 = 2000.", font_size=20, weight=BOLD, color=COLOR_CYAN, max_width=9.2, max_chars=50)

        sol1_content = VGroup(sol1_head, sol1_anal, sol1_a, sol1_b).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        fit_safe_box(sol1_content, max_width=9.4, max_height=1.85)
        sol1_content.move_to([0.65, -1.95, 0])

        sol1_box = RoundedRectangle(corner_radius=0.2, width=9.8, height=sol1_content.height + 0.35, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color="#0f172a", fill_opacity=0.95).move_to(sol1_content.get_center())
        sol1_card = VGroup(sol1_box, sol1_content)

        mascot_praise_1 = get_mascot("thay_khen.png")
        if cur_mascot and mascot_praise_1:
            self.play(FadeIn(sol1_card, shift=UP * 0.2), ReplacementTransform(cur_mascot, mascot_praise_1), run_time=0.8)
            cur_mascot = mascot_praise_1
        else:
            self.play(FadeIn(sol1_card, shift=UP * 0.2), run_time=0.8)

        rem_sol1 = max(0.15, t_ex1_sol - 1.4)
        self.wait(rem_sol1)

        # Dọn dẹp chuyển sang ví dụ kế tiếp hoặc kết thúc
        mascot_giang_next_1 = get_mascot("thay_giang.png")
        if 0 < 2 and cur_mascot and mascot_giang_next_1:
            self.play(FadeOut(sol1_card, shift=DOWN * 0.2), FadeOut(problem1_grp, shift=UP * 0.2), FadeOut(c1_box), ReplacementTransform(cur_mascot, mascot_giang_next_1), run_time=0.6)
            cur_mascot = mascot_giang_next_1
        else:
            self.play(FadeOut(sol1_card, shift=DOWN * 0.2), FadeOut(problem1_grp, shift=UP * 0.2), FadeOut(c1_box), run_time=0.6)

        # ==================== VÍ DỤ 2 ====================
        a_intro_2 = os.path.join(audio_dir, "scene3_ex2_intro.mp3")
        a_tick = os.path.join(audio_dir, "tick45.mp3")
        a_sol_2 = os.path.join(audio_dir, "scene3_ex2_sol.mp3")

        t_ex2_intro = get_audio_duration(a_intro_2, fallback=timing.get("scene3_ex2_intro", 25.0))
        t_ex2_timer = get_audio_duration(a_tick, fallback=timing.get("scene3_ex2_timer", 45.0))
        t_ex2_sol = get_audio_duration(a_sol_2, fallback=timing.get("scene3_ex2_sol", 40.0))

        # Khung chứa lớn nửa trên (đặt tại x = 0.65, không đè mascot)
        c2_box = RoundedRectangle(corner_radius=0.3, width=10.2, height=5.6, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0.65, -0.45, 0])

        badge2 = Text("VÍ DỤ 2 (Mức Thông Hiểu)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_EMERALD)
        head2 = safe_text("VIẾT TẬP HỢP THEO BẤT ĐẲNG THỨC KÉP VÀ BIỂU DIỄN TIA SỐ", font_size=24, weight=BOLD, color=COLOR_AMBER, max_width=9.2)
        sep2 = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_EMERALD)
        q2_lead = safe_text("Cho tập hợp A các số tự nhiên x thỏa mãn: 14 <= x < 19.", font_size=21, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        q2_a = safe_text("a) Viết tập hợp A bằng cách liệt kê tất cả các phần tử của tập hợp", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        q2_b = safe_text("b) Trong các phần tử của A, số nào là số nhỏ nhất? Số nào là số lớn nhất?", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        bl_sub_2 = []
        bl_sub_2.append(Text("A = { 14; 15; ... ; ? }", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER))
        bl_sub_2.append(Text("Số nhỏ nhất = ?", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER))
        bl_sub_2.append(Text("Số lớn nhất = ?", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER))
        if bl_sub_2:
            def sep(): return Text("  ;  ", font=FONT_FAMILY, font_size=19, color=COLOR_TEXT_MUTED)
            bl_row = VGroup()
            for i_b, b_elem in enumerate(bl_sub_2):
                if i_b > 0:
                    bl_row.add(sep())
                bl_row.add(b_elem)
            bl_row.arrange(RIGHT, buff=0.1)
            fit_safe_box(bl_row, max_width=9.0, max_height=0.45)
            bl_box = RoundedRectangle(corner_radius=0.15, width=bl_row.width + 0.4, height=0.48, stroke_color=COLOR_AMBER, stroke_width=1, fill_color="#0f172a", fill_opacity=0.9).move_to(bl_row.get_center())
            q2_blank_grp = VGroup(bl_box, bl_row)
            problem2_grp = VGroup(badge2, head2, sep2, q2_lead, q2_a, q2_b, q2_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.10)
        else:
            problem2_grp = VGroup(badge2, head2, sep2, q2_lead, q2_a, q2_b).arrange(DOWN, aligned_edge=LEFT, buff=0.11)

        fit_safe_box(problem2_grp, max_width=9.4, max_height=2.5)
        problem2_grp.move_to([0.65, 0.95, 0])

        # BƯỚC 1: Hiện Đề bài (Thầy giảng bài)
        self.play(FadeIn(c2_box, scale=0.96), run_time=0.6)
        self.play(FadeIn(problem2_grp, shift=DOWN * 0.15), run_time=0.8)
        rem_intro2 = max(0.15, t_ex2_intro - 1.4)
        self.wait(rem_intro2)

        # BƯỚC 2: Đồng hồ đếm ngược 45s góc trên phải UR & Thầy đổi sang biểu cảm SUY NGHĨ
        badge_t2, vt2, text_t2, pbg_t2, pfill_t2 = build_timer_widget(COLOR_EMERALD)
        timer_grp2 = VGroup(badge_t2, pbg_t2, pfill_t2, text_t2)
        
        mascot_think_2 = get_mascot("thay_suynghi.png")
        if cur_mascot and mascot_think_2:
            self.play(FadeIn(timer_grp2, shift=DOWN*0.3), ReplacementTransform(cur_mascot, mascot_think_2), run_time=0.6)
            cur_mascot = mascot_think_2
        else:
            self.play(FadeIn(timer_grp2, shift=DOWN*0.3), run_time=0.6)

        self.play(vt2.animate.set_value(0), run_time=max(1.0, t_ex2_timer - 1.2), rate_func=linear)
        self.play(FadeOut(timer_grp2, shift=UP*0.2), run_time=0.6)

        # BƯỚC 3: Lời giải chi tiết & Thầy đổi sang biểu cảm KHEN NGỢI (Xuất sắc! ⭐)
        sol2_head = Text("✓ HƯỚNG DẪN GIẢI CHI TIẾT:", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_EMERALD)
        sol2_anal = safe_text("• Phân tích: Dấu <= nghĩa là lấy cả giá trị đầu mút 14; dấu < nghĩa là không lấy giá trị 19 (x < 19).", font_size=19, color=COLOR_TEXT_MUTED, max_width=9.2, max_chars=50)
        sol2_a = safe_text("• a) Tập hợp A = {14; 15; 16; 17; 18} (lưu ý có lấy số 14 nhưng không lấy số 19).", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=50)
        sol2_b = safe_text("• b) Số nhỏ nhất trong tập hợp A là 14; số lớn nhất trong tập hợp A là 18.", font_size=20, weight=BOLD, color=COLOR_CYAN, max_width=9.2, max_chars=50)

        sol2_content = VGroup(sol2_head, sol2_anal, sol2_a, sol2_b).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        fit_safe_box(sol2_content, max_width=9.4, max_height=1.85)
        sol2_content.move_to([0.65, -1.95, 0])

        sol2_box = RoundedRectangle(corner_radius=0.2, width=9.8, height=sol2_content.height + 0.35, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color="#0f172a", fill_opacity=0.95).move_to(sol2_content.get_center())
        sol2_card = VGroup(sol2_box, sol2_content)

        mascot_praise_2 = get_mascot("thay_khen.png")
        if cur_mascot and mascot_praise_2:
            self.play(FadeIn(sol2_card, shift=UP * 0.2), ReplacementTransform(cur_mascot, mascot_praise_2), run_time=0.8)
            cur_mascot = mascot_praise_2
        else:
            self.play(FadeIn(sol2_card, shift=UP * 0.2), run_time=0.8)

        rem_sol2 = max(0.15, t_ex2_sol - 1.4)
        self.wait(rem_sol2)

        # Dọn dẹp chuyển sang ví dụ kế tiếp hoặc kết thúc
        mascot_giang_next_2 = get_mascot("thay_giang.png")
        if 1 < 2 and cur_mascot and mascot_giang_next_2:
            self.play(FadeOut(sol2_card, shift=DOWN * 0.2), FadeOut(problem2_grp, shift=UP * 0.2), FadeOut(c2_box), ReplacementTransform(cur_mascot, mascot_giang_next_2), run_time=0.6)
            cur_mascot = mascot_giang_next_2
        else:
            self.play(FadeOut(sol2_card, shift=DOWN * 0.2), FadeOut(problem2_grp, shift=UP * 0.2), FadeOut(c2_box), run_time=0.6)

        # ==================== VÍ DỤ 3 ====================
        a_intro_3 = os.path.join(audio_dir, "scene3_ex3_intro.mp3")
        a_tick = os.path.join(audio_dir, "tick45.mp3")
        a_sol_3 = os.path.join(audio_dir, "scene3_ex3_sol.mp3")

        t_ex3_intro = get_audio_duration(a_intro_3, fallback=timing.get("scene3_ex3_intro", 25.0))
        t_ex3_timer = get_audio_duration(a_tick, fallback=timing.get("scene3_ex3_timer", 45.0))
        t_ex3_sol = get_audio_duration(a_sol_3, fallback=timing.get("scene3_ex3_sol", 40.0))

        # Khung chứa lớn nửa trên (đặt tại x = 0.65, không đè mascot)
        c3_box = RoundedRectangle(corner_radius=0.3, width=10.2, height=5.6, stroke_color=COLOR_AMBER, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0.65, -0.45, 0])

        badge3 = Text("VÍ DỤ 3 (Mức Vận Dụng Thực Tế)", font=FONT_FAMILY, font_size=22, weight=BOLD, color=COLOR_AMBER)
        head3 = safe_text("BÀI TOÁN XẾP HẠNG DOANH THU CỬA HÀNG TIỆN LỢI", font_size=24, weight=BOLD, color=COLOR_AMBER, max_width=9.2)
        sep3 = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_AMBER)
        q3_lead = safe_text("Doanh thu 4 tuần của một cửa hàng sách lần lượt là (đơn vị: triệu đồng):", font_size=21, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        q3_a = safe_text("Tuần 1: 108 triệu; Tuần 2: 95 triệu; Tuần 3: 120 triệu; Tuần 4: 115 triệu.", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        q3_b = safe_text("a) Sắp xếp doanh thu theo thứ tự tăng dần.  b) Tuần nào có doanh thu cao nhất?", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        bl_sub_3 = []
        bl_sub_3.append(Text("Thứ tự tăng dần: ...", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER))
        bl_sub_3.append(Text("Doanh thu cao nhất: Tuần ?", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER))
        if bl_sub_3:
            def sep(): return Text("  ;  ", font=FONT_FAMILY, font_size=19, color=COLOR_TEXT_MUTED)
            bl_row = VGroup()
            for i_b, b_elem in enumerate(bl_sub_3):
                if i_b > 0:
                    bl_row.add(sep())
                bl_row.add(b_elem)
            bl_row.arrange(RIGHT, buff=0.1)
            fit_safe_box(bl_row, max_width=9.0, max_height=0.45)
            bl_box = RoundedRectangle(corner_radius=0.15, width=bl_row.width + 0.4, height=0.48, stroke_color=COLOR_AMBER, stroke_width=1, fill_color="#0f172a", fill_opacity=0.9).move_to(bl_row.get_center())
            q3_blank_grp = VGroup(bl_box, bl_row)
            problem3_grp = VGroup(badge3, head3, sep3, q3_lead, q3_a, q3_b, q3_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.10)
        else:
            problem3_grp = VGroup(badge3, head3, sep3, q3_lead, q3_a, q3_b).arrange(DOWN, aligned_edge=LEFT, buff=0.11)

        fit_safe_box(problem3_grp, max_width=9.4, max_height=2.5)
        problem3_grp.move_to([0.65, 0.95, 0])

        # BƯỚC 1: Hiện Đề bài (Thầy giảng bài)
        self.play(FadeIn(c3_box, scale=0.96), run_time=0.6)
        self.play(FadeIn(problem3_grp, shift=DOWN * 0.15), run_time=0.8)
        rem_intro3 = max(0.15, t_ex3_intro - 1.4)
        self.wait(rem_intro3)

        # BƯỚC 2: Đồng hồ đếm ngược 45s góc trên phải UR & Thầy đổi sang biểu cảm SUY NGHĨ
        badge_t3, vt3, text_t3, pbg_t3, pfill_t3 = build_timer_widget(COLOR_AMBER)
        timer_grp3 = VGroup(badge_t3, pbg_t3, pfill_t3, text_t3)
        
        mascot_think_3 = get_mascot("thay_suynghi.png")
        if cur_mascot and mascot_think_3:
            self.play(FadeIn(timer_grp3, shift=DOWN*0.3), ReplacementTransform(cur_mascot, mascot_think_3), run_time=0.6)
            cur_mascot = mascot_think_3
        else:
            self.play(FadeIn(timer_grp3, shift=DOWN*0.3), run_time=0.6)

        self.play(vt3.animate.set_value(0), run_time=max(1.0, t_ex3_timer - 1.2), rate_func=linear)
        self.play(FadeOut(timer_grp3, shift=UP*0.2), run_time=0.6)

        # BƯỚC 3: Lời giải chi tiết & Thầy đổi sang biểu cảm KHEN NGỢI (Xuất sắc! ⭐)
        sol3_head = Text("✓ HƯỚNG DẪN GIẢI CHI TIẾT:", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_EMERALD)
        sol3_anal = safe_text("• Phân tích: Áp dụng quy tắc so sánh số có 2 và 3 chữ số, dùng tính chất bắc cầu: 95 < 108 < 115 < 120.", font_size=19, color=COLOR_TEXT_MUTED, max_width=9.2, max_chars=50)
        sol3_a = safe_text("• a) Thứ tự doanh thu tăng dần là: 95 triệu < 108 triệu < 115 triệu < 120 triệu (Tuần 2 < Tuần 1 < Tuần 4 < Tuần 3).", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=50)
        sol3_b = safe_text("• b) Tuần có doanh thu cao nhất là Tuần 3 với 120 triệu đồng; thấp nhất là Tuần 2 với 95 triệu đồng.", font_size=20, weight=BOLD, color=COLOR_CYAN, max_width=9.2, max_chars=50)

        sol3_content = VGroup(sol3_head, sol3_anal, sol3_a, sol3_b).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        fit_safe_box(sol3_content, max_width=9.4, max_height=1.85)
        sol3_content.move_to([0.65, -1.95, 0])

        sol3_box = RoundedRectangle(corner_radius=0.2, width=9.8, height=sol3_content.height + 0.35, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color="#0f172a", fill_opacity=0.95).move_to(sol3_content.get_center())
        sol3_card = VGroup(sol3_box, sol3_content)

        mascot_praise_3 = get_mascot("thay_khen.png")
        if cur_mascot and mascot_praise_3:
            self.play(FadeIn(sol3_card, shift=UP * 0.2), ReplacementTransform(cur_mascot, mascot_praise_3), run_time=0.8)
            cur_mascot = mascot_praise_3
        else:
            self.play(FadeIn(sol3_card, shift=UP * 0.2), run_time=0.8)

        rem_sol3 = max(0.15, t_ex3_sol - 1.4)
        self.wait(rem_sol3)

        # Dọn dẹp chuyển sang ví dụ kế tiếp hoặc kết thúc
        mascot_giang_next_3 = get_mascot("thay_giang.png")
        if 2 < 2 and cur_mascot and mascot_giang_next_3:
            self.play(FadeOut(sol3_card, shift=DOWN * 0.2), FadeOut(problem3_grp, shift=UP * 0.2), FadeOut(c3_box), ReplacementTransform(cur_mascot, mascot_giang_next_3), run_time=0.6)
            cur_mascot = mascot_giang_next_3
        else:
            self.play(FadeOut(sol3_card, shift=DOWN * 0.2), FadeOut(problem3_grp, shift=UP * 0.2), FadeOut(c3_box), run_time=0.6)

        if cur_mascot:
            self.play(FadeOut(cur_mascot, shift=DOWN*0.2), run_time=0.5)

if __name__ == "__main__":
    pass
