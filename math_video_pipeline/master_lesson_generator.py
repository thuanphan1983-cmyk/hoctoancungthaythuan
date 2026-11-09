"""
MASTER LESSON GENERATOR (MANIM + MASCOT + STRICT SAFE-ZONE + AUDIO-VISUAL SYNC)
Tự động sinh trọn bộ mã nguồn Manim (scene1 -> scene5) và concat_lesson.py
Quy chuẩn sản xuất:
1. MASCOT CHIBI THẦY THUẬN (.to_corner(DL, buff=0.35)):
   - Scene 1, 2, 4: thay_giang.png (giảng bài, đồng hành suốt tiết học).
   - Scene 3 lúc đếm ngược 45s: thay_suynghi.png (thầy cùng suy ngẫm với học sinh).
   - Scene 3 lúc chữa bài: thay_khen.png (thầy khen ngợi xuất sắc với sao vàng & má hồng).
   - Scene 5 tổng kết & dặn dò: thay_giang -> thay_khen (chúc mừng các em hoàn thành tiết học).
2. STRICT SAFE-ZONE (Không tràn viền, không đè mascot):
   - Thẻ nội dung đặt tại x = 0.65, max_width = 9.4 -> Mép trái >= -4.45 (cách mascot >= 0.55 đơn vị).
   - fit_safe_box và wrap_text tự động.
3. AUDIO-VISUAL SYNC 1:1 TỪNG MILI-GIÂY (mutagen MP3 get_audio_duration).
4. ĐỒNG HỒ ĐẾM NGƯỢC 45S GÓC TRÊN PHẢI UR (font Segoe UI, không che đề bài).
"""

import os
import sys
import json
import shutil

HEADER_IMPORTS = '''import os
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
    return "\\n".join(lines)

def safe_text(txt, font=FONT_FAMILY, font_size=24, weight=NORMAL, color=COLOR_TEXT_MAIN, max_width=9.5, max_chars=50):
    if len(txt) > max_chars and "\\n" not in txt:
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
'''


def build_scene1_code(lesson: dict) -> str:
    p1 = lesson["part1"]
    slides = p1.get("slides", [])

    code = HEADER_IMPORTS + f'''

class Scene1KhoiDong(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        audio_dir = os.path.join(os.path.dirname(__file__), "audio")
        timing_file = os.path.join(audio_dir, "timing_data.json")
        timing = {{}}
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
'''

    colors = ["COLOR_AMBER", "COLOR_CYAN", "COLOR_EMERALD", "COLOR_INDIGO"]
    for idx, sl in enumerate(slides):
        col = colors[idx % len(colors)]
        s_num = idx + 1
        heading = sl.get("heading", f"SLIDE {s_num}").replace('"', '\\"')
        sub = sl.get("sub", "").replace('"', '\\"')
        items = sl.get("items", [])

        code += f'''
        # ----------------- SLIDE {s_num} -----------------
        a_s{s_num} = os.path.join(audio_dir, "scene1_slide{s_num}.mp3")
        t_s{s_num} = get_audio_duration(a_s{s_num}, fallback=timing.get("scene1_slide{s_num}", 22.0))

        c{s_num}_title = safe_text("{heading}", font_size=26, weight=BOLD, color={col}, max_width=9.2)
        c{s_num}_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color={col})
        c{s_num}_sub = safe_text("{sub}", font_size=20, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
'''

        code += f"        itms_{s_num} = []\n"
        for itm in items:
            safe_itm = itm.replace('"', '\\"')
            code += f'        itms_{s_num}.append(safe_text("• {safe_itm}", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))\n'

        code += f'''
        c{s_num}_content = VGroup(c{s_num}_title, c{s_num}_line, c{s_num}_sub, *itms_{s_num}).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(c{s_num}_content, max_width=9.4, max_height=4.6)
        c{s_num}_content.move_to([0.65, -0.35, 0])

        c{s_num}_box = RoundedRectangle(corner_radius=0.3, width=c{s_num}_content.width + 0.6, height=c{s_num}_content.height + 0.6, stroke_color={col}, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c{s_num}_content.get_center())
        card{s_num} = VGroup(c{s_num}_box, c{s_num}_content)

        anim_base = 0.5 + 0.6 + len(itms_{s_num}) * 0.3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_s{s_num} - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.6 * anim_scale
        rt_item = 0.3 * anim_scale

        self.play(FadeIn(c{s_num}_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(c{s_num}_title, shift=DOWN*0.1), FadeIn(c{s_num}_sub, shift=UP*0.1), run_time=rt_head)
        for itm in itms_{s_num}:
            self.play(FadeIn(itm, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + len(itms_{s_num}) * rt_item
        rem_s{s_num} = max(0.15, avail_time - actual_anim)
        self.wait(rem_s{s_num})
        self.play(FadeOut(card{s_num}, shift=UP*0.25), run_time=fade_out_dur)
'''

    code += '''
        if mascot:
            self.play(FadeOut(mascot, shift=DOWN*0.2), run_time=0.5)

if __name__ == "__main__":
    pass
'''
    return code


def build_scene2_code(lesson: dict) -> str:
    p2 = lesson["part2"]
    slides = p2.get("slides", [])

    code = HEADER_IMPORTS + f'''

class Scene2KienThuc(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        audio_dir = os.path.join(os.path.dirname(__file__), "audio")
        timing_file = os.path.join(audio_dir, "timing_data.json")
        timing = {{}}
        if os.path.exists(timing_file):
            try:
                with open(timing_file, "r", encoding="utf-8") as f:
                    timing = json.load(f)
            except Exception:
                pass

        header = Text("PHẦN 2: KIẾN THỨC TRỌNG TÂM & QUY TẮC TOÁN HỌC", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=2, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=0.8)

        mascot = get_mascot("thay_giang.png")
        if mascot:
            self.play(FadeIn(mascot, shift=UP*0.2), run_time=0.6)
'''

    colors = ["COLOR_EMERALD", "COLOR_AMBER", "COLOR_CYAN", "COLOR_INDIGO", "COLOR_ROSE", "COLOR_EMERALD"]
    for idx, sl in enumerate(slides):
        col = colors[idx % len(colors)]
        s_num = idx + 1
        heading = sl.get("heading", f"MỤC {s_num}").replace('"', '\\"')
        sub = sl.get("sub", "").replace('"', '\\"')
        items = sl.get("items", [])

        code += f'''
        # ----------------- SLIDE {s_num} -----------------
        a_s{s_num} = os.path.join(audio_dir, "scene2_slide{s_num}.mp3")
        t_s{s_num} = get_audio_duration(a_s{s_num}, fallback=timing.get("scene2_slide{s_num}", 25.0))

        c{s_num}_title = safe_text("{heading}", font_size=26, weight=BOLD, color={col}, max_width=9.2)
        c{s_num}_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color={col})
        c{s_num}_sub = safe_text("{sub}", font_size=20, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
'''

        code += f"        itms_{s_num} = []\n"
        for itm in items:
            safe_itm = itm.replace('"', '\\"')
            code += f'        itms_{s_num}.append(safe_text("• {safe_itm}", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))\n'

        code += f'''
        c{s_num}_content = VGroup(c{s_num}_title, c{s_num}_line, c{s_num}_sub, *itms_{s_num}).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(c{s_num}_content, max_width=9.4, max_height=4.6)
        c{s_num}_content.move_to([0.65, -0.35, 0])

        c{s_num}_box = RoundedRectangle(corner_radius=0.3, width=c{s_num}_content.width + 0.6, height=c{s_num}_content.height + 0.6, stroke_color={col}, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c{s_num}_content.get_center())
        card{s_num} = VGroup(c{s_num}_box, c{s_num}_content)

        anim_base = 0.5 + 0.6 + len(itms_{s_num}) * 0.3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_s{s_num} - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.6 * anim_scale
        rt_item = 0.3 * anim_scale

        self.play(FadeIn(c{s_num}_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(c{s_num}_title, shift=DOWN*0.1), FadeIn(c{s_num}_sub, shift=UP*0.1), run_time=rt_head)
        for itm in itms_{s_num}:
            self.play(FadeIn(itm, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + len(itms_{s_num}) * rt_item
        rem_s{s_num} = max(0.15, avail_time - actual_anim)
        self.wait(rem_s{s_num})
        self.play(FadeOut(card{s_num}, shift=UP*0.25), run_time=fade_out_dur)
'''

    code += '''
        if mascot:
            self.play(FadeOut(mascot, shift=DOWN*0.2), run_time=0.5)

if __name__ == "__main__":
    pass
'''
    return code


def build_scene3_code(lesson: dict) -> str:
    p3 = lesson["part3"]
    examples = p3.get("examples", [])

    code = HEADER_IMPORTS + f'''

def build_timer_widget(theme_color=COLOR_AMBER):
    badge = RoundedRectangle(corner_radius=0.15, width=2.4, height=0.85, stroke_color=theme_color, stroke_width=2, fill_color="#0f172a", fill_opacity=0.95).to_corner(UR, buff=0.45)
    vt = ValueTracker(45)
    timer_text = always_redraw(lambda: Text(f"⏱ {{int(round(vt.get_value())):02d}}s", font="Segoe UI", font_size=24, weight=BOLD, color=theme_color).move_to(badge.get_center() + UP * 0.1))
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
        timing = {{}}
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
'''

    colors = ["COLOR_CYAN", "COLOR_EMERALD", "COLOR_AMBER"]
    for idx, ex in enumerate(examples):
        e_num = idx + 1
        col = colors[idx % len(colors)]
        badge = ex.get("badge", f"VÍ DỤ {e_num}").replace('"', '\\"')
        head = ex.get("head", "").replace('"', '\\"')
        lead = ex.get("lead", "").replace('"', '\\"')
        qa = ex.get("question_a", "").replace('"', '\\"')
        qb = ex.get("question_b", "").replace('"', '\\"')
        blank_items = ex.get("blank_items", [])
        analysis = ex.get("analysis", "").replace('"', '\\"')
        sola = ex.get("solution_a", "").replace('"', '\\"')
        solb = ex.get("solution_b", "").replace('"', '\\"')

        code += f'''
        # ==================== VÍ DỤ {e_num} ====================
        a_intro_{e_num} = os.path.join(audio_dir, "scene3_ex{e_num}_intro.mp3")
        a_tick = os.path.join(audio_dir, "tick45.mp3")
        a_sol_{e_num} = os.path.join(audio_dir, "scene3_ex{e_num}_sol.mp3")

        t_ex{e_num}_intro = get_audio_duration(a_intro_{e_num}, fallback=timing.get("scene3_ex{e_num}_intro", 25.0))
        t_ex{e_num}_timer = get_audio_duration(a_tick, fallback=timing.get("scene3_ex{e_num}_timer", 45.0))
        t_ex{e_num}_sol = get_audio_duration(a_sol_{e_num}, fallback=timing.get("scene3_ex{e_num}_sol", 40.0))

        # Khung chứa lớn nửa trên (đặt tại x = 0.65, không đè mascot)
        c{e_num}_box = RoundedRectangle(corner_radius=0.3, width=10.2, height=5.6, stroke_color={col}, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0.65, -0.45, 0])

        badge{e_num} = Text("{badge}", font=FONT_FAMILY, font_size=22, weight=BOLD, color={col})
        head{e_num} = safe_text("{head}", font_size=24, weight=BOLD, color=COLOR_AMBER, max_width=9.2)
        sep{e_num} = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color={col})
        q{e_num}_lead = safe_text("{lead}", font_size=21, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        q{e_num}_a = safe_text("{qa}", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
        q{e_num}_b = safe_text("{qb}", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48)
'''

        code += f"        bl_sub_{e_num} = []\n"
        for bi in blank_items:
            safe_bi = bi.replace('"', '\\"')
            code += f'        bl_sub_{e_num}.append(Text("{safe_bi}", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_AMBER))\n'

        code += f'''        if bl_sub_{e_num}:
            def sep(): return Text("  ;  ", font=FONT_FAMILY, font_size=19, color=COLOR_TEXT_MUTED)
            bl_row = VGroup()
            for i_b, b_elem in enumerate(bl_sub_{e_num}):
                if i_b > 0:
                    bl_row.add(sep())
                bl_row.add(b_elem)
            bl_row.arrange(RIGHT, buff=0.1)
            fit_safe_box(bl_row, max_width=9.0, max_height=0.45)
            bl_box = RoundedRectangle(corner_radius=0.15, width=bl_row.width + 0.4, height=0.48, stroke_color=COLOR_AMBER, stroke_width=1, fill_color="#0f172a", fill_opacity=0.9).move_to(bl_row.get_center())
            q{e_num}_blank_grp = VGroup(bl_box, bl_row)
            problem{e_num}_grp = VGroup(badge{e_num}, head{e_num}, sep{e_num}, q{e_num}_lead, q{e_num}_a, q{e_num}_b, q{e_num}_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.10)
        else:
            problem{e_num}_grp = VGroup(badge{e_num}, head{e_num}, sep{e_num}, q{e_num}_lead, q{e_num}_a, q{e_num}_b).arrange(DOWN, aligned_edge=LEFT, buff=0.11)

        fit_safe_box(problem{e_num}_grp, max_width=9.4, max_height=2.5)
        problem{e_num}_grp.move_to([0.65, 0.95, 0])

        # BƯỚC 1: Hiện Đề bài (Thầy giảng bài)
        self.play(FadeIn(c{e_num}_box, scale=0.96), run_time=0.6)
        self.play(FadeIn(problem{e_num}_grp, shift=DOWN * 0.15), run_time=0.8)
        rem_intro{e_num} = max(0.15, t_ex{e_num}_intro - 1.4)
        self.wait(rem_intro{e_num})

        # BƯỚC 2: Đồng hồ đếm ngược 45s góc trên phải UR & Thầy đổi sang biểu cảm SUY NGHĨ
        badge_t{e_num}, vt{e_num}, text_t{e_num}, pbg_t{e_num}, pfill_t{e_num} = build_timer_widget({col})
        timer_grp{e_num} = VGroup(badge_t{e_num}, pbg_t{e_num}, pfill_t{e_num}, text_t{e_num})
        
        mascot_think_{e_num} = get_mascot("thay_suynghi.png")
        if cur_mascot and mascot_think_{e_num}:
            self.play(FadeIn(timer_grp{e_num}, shift=DOWN*0.3), ReplacementTransform(cur_mascot, mascot_think_{e_num}), run_time=0.6)
            cur_mascot = mascot_think_{e_num}
        else:
            self.play(FadeIn(timer_grp{e_num}, shift=DOWN*0.3), run_time=0.6)

        self.play(vt{e_num}.animate.set_value(0), run_time=max(1.0, t_ex{e_num}_timer - 1.2), rate_func=linear)
        self.play(FadeOut(timer_grp{e_num}, shift=UP*0.2), run_time=0.6)

        # BƯỚC 3: Lời giải chi tiết & Thầy đổi sang biểu cảm KHEN NGỢI (Xuất sắc! ⭐)
        sol{e_num}_head = Text("✓ HƯỚNG DẪN GIẢI CHI TIẾT:", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_EMERALD)
        sol{e_num}_anal = safe_text("• Phân tích: {analysis}", font_size=19, color=COLOR_TEXT_MUTED, max_width=9.2, max_chars=50)
        sol{e_num}_a = safe_text("• a) {sola}", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=50)
        sol{e_num}_b = safe_text("• b) {solb}", font_size=20, weight=BOLD, color=COLOR_CYAN, max_width=9.2, max_chars=50)

        sol{e_num}_content = VGroup(sol{e_num}_head, sol{e_num}_anal, sol{e_num}_a, sol{e_num}_b).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        fit_safe_box(sol{e_num}_content, max_width=9.4, max_height=1.85)
        sol{e_num}_content.move_to([0.65, -1.95, 0])

        sol{e_num}_box = RoundedRectangle(corner_radius=0.2, width=9.8, height=sol{e_num}_content.height + 0.35, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color="#0f172a", fill_opacity=0.95).move_to(sol{e_num}_content.get_center())
        sol{e_num}_card = VGroup(sol{e_num}_box, sol{e_num}_content)

        mascot_praise_{e_num} = get_mascot("thay_khen.png")
        if cur_mascot and mascot_praise_{e_num}:
            self.play(FadeIn(sol{e_num}_card, shift=UP * 0.2), ReplacementTransform(cur_mascot, mascot_praise_{e_num}), run_time=0.8)
            cur_mascot = mascot_praise_{e_num}
        else:
            self.play(FadeIn(sol{e_num}_card, shift=UP * 0.2), run_time=0.8)

        rem_sol{e_num} = max(0.15, t_ex{e_num}_sol - 1.4)
        self.wait(rem_sol{e_num})

        # Dọn dẹp chuyển sang ví dụ kế tiếp hoặc kết thúc
        mascot_giang_next_{e_num} = get_mascot("thay_giang.png")
        if {idx} < {len(examples) - 1} and cur_mascot and mascot_giang_next_{e_num}:
            self.play(FadeOut(sol{e_num}_card, shift=DOWN * 0.2), FadeOut(problem{e_num}_grp, shift=UP * 0.2), FadeOut(c{e_num}_box), ReplacementTransform(cur_mascot, mascot_giang_next_{e_num}), run_time=0.6)
            cur_mascot = mascot_giang_next_{e_num}
        else:
            self.play(FadeOut(sol{e_num}_card, shift=DOWN * 0.2), FadeOut(problem{e_num}_grp, shift=UP * 0.2), FadeOut(c{e_num}_box), run_time=0.6)
'''

    code += '''
        if cur_mascot:
            self.play(FadeOut(cur_mascot, shift=DOWN*0.2), run_time=0.5)

if __name__ == "__main__":
    pass
'''
    return code


def build_scene4_code(lesson: dict) -> str:
    p4 = lesson["part4"]
    traps = p4.get("traps", [])

    code = HEADER_IMPORTS + f'''

class Scene4CanhBao(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        audio_dir = os.path.join(os.path.dirname(__file__), "audio")
        timing_file = os.path.join(audio_dir, "timing_data.json")
        timing = {{}}
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
'''

    for idx, tp in enumerate(traps):
        s_num = idx + 1
        name = tp.get("name", f"BẪY {s_num}").replace('"', '\\"')
        wrong = tp.get("wrong", "").replace('"', '\\"')
        reason = tp.get("reason", "").replace('"', '\\"')
        correct = tp.get("correct", "").replace('"', '\\"')

        code += f'''
        # ----------------- BẪY {s_num} -----------------
        a_t{s_num} = os.path.join(audio_dir, "scene4_trap{s_num}.mp3")
        t_t{s_num} = get_audio_duration(a_t{s_num}, fallback=timing.get("scene4_trap{s_num}", 24.0))

        t{s_num}_title = Text("{name}", font=FONT_FAMILY, font_size=24, weight=BOLD, color=COLOR_ROSE)
        t{s_num}_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_ROSE)
        t{s_num}_w = safe_text("✗ Sai lầm: {wrong}", font_size=20, weight=BOLD, color=COLOR_ROSE, max_width=9.2, max_chars=48)
        t{s_num}_r = safe_text("• Nguyên nhân: {reason}", font_size=19, color=COLOR_TEXT_MUTED, max_width=9.2, max_chars=48)
        t{s_num}_c = safe_text("✓ Cách làm đúng: {correct}", font_size=20, weight=BOLD, color=COLOR_EMERALD, max_width=9.2, max_chars=48)

        t{s_num}_content = VGroup(t{s_num}_title, t{s_num}_line, t{s_num}_w, t{s_num}_r, t{s_num}_c).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(t{s_num}_content, max_width=9.4, max_height=4.6)
        t{s_num}_content.move_to([0.65, -0.35, 0])

        t{s_num}_box = RoundedRectangle(corner_radius=0.3, width=t{s_num}_content.width + 0.6, height=t{s_num}_content.height + 0.6, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(t{s_num}_content.get_center())
        card{s_num} = VGroup(t{s_num}_box, t{s_num}_content)

        anim_base = 0.5 + 0.5 + 0.35 * 3
        fade_out_dur = 0.5
        avail_time = max(0.2, t_t{s_num} - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.5 * anim_scale
        rt_head = 0.5 * anim_scale
        rt_item = 0.35 * anim_scale

        self.play(FadeIn(t{s_num}_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(t{s_num}_title, shift=DOWN*0.1), run_time=rt_head)
        self.play(FadeIn(t{s_num}_w, shift=RIGHT*0.2), run_time=rt_item)
        self.play(FadeIn(t{s_num}_r, shift=RIGHT*0.2), run_time=rt_item)
        self.play(FadeIn(t{s_num}_c, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + 3 * rt_item
        rem_t{s_num} = max(0.15, avail_time - actual_anim)
        self.wait(rem_t{s_num})
        self.play(FadeOut(card{s_num}, shift=UP*0.25), run_time=fade_out_dur)
'''

    code += '''
        if mascot:
            self.play(FadeOut(mascot, shift=DOWN*0.2), run_time=0.5)

if __name__ == "__main__":
    pass
'''
    return code


def build_scene5_code(lesson: dict) -> str:
    p5 = lesson["part5"]
    nodes = p5.get("mindmap_nodes", [])
    hw = p5.get("homework", [])

    code = HEADER_IMPORTS + f'''

class Scene5TongKet(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        audio_dir = os.path.join(os.path.dirname(__file__), "audio")
        timing_file = os.path.join(audio_dir, "timing_data.json")
        timing = {{}}
        if os.path.exists(timing_file):
            try:
                with open(timing_file, "r", encoding="utf-8") as f:
                    timing = json.load(f)
            except Exception:
                pass

        header = Text("PHẦN 5: SƠ ĐỒ TƯ DUY & HƯỚNG DẪN TỰ HỌC", font=FONT_FAMILY, font_size=30, weight=BOLD, color=COLOR_INDIGO)
        header_line = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=2, color=COLOR_INDIGO)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=0.8)

        mascot = get_mascot("thay_giang.png")
        if mascot:
            self.play(FadeIn(mascot, shift=UP*0.2), run_time=0.6)

        # SLIDE 1: SƠ ĐỒ TƯ DUY TỔNG KẾT
        a_sl1 = os.path.join(audio_dir, "scene5_slide1.mp3")
        t_sl1 = get_audio_duration(a_sl1, fallback=timing.get("scene5_slide1", 28.0))

        # SLIDE 2: BÀI TẬP VỀ NHÀ & DẶN DÒ
        a_sl2 = os.path.join(audio_dir, "scene5_slide2.mp3")
        t_sl2 = get_audio_duration(a_sl2, fallback=timing.get("scene5_slide2", 22.0))

        c1_title = safe_text("SƠ ĐỒ HỆ THỐNG HÓA KIẾN THỨC", font_size=26, weight=BOLD, color=COLOR_INDIGO, max_width=9.2)
        c1_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_INDIGO)
'''

    code += "        n_items = []\n"
    for n in nodes:
        safe_n = n.replace('"', '\\"')
        code += f'        n_items.append(safe_text("{safe_n}", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))\n'

    code += f'''
        c1_content = VGroup(c1_title, c1_line, *n_items).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        fit_safe_box(c1_content, max_width=9.4, max_height=4.6)
        c1_content.move_to([0.65, -0.35, 0])

        c1_box = RoundedRectangle(corner_radius=0.3, width=c1_content.width + 0.6, height=c1_content.height + 0.6, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c1_content.get_center())
        card1 = VGroup(c1_box, c1_content)

        anim_base1 = 0.5 + 0.5 + len(n_items) * 0.3
        fade_dur = 0.5
        avail_sl1 = max(0.2, t_sl1 - fade_dur)
        scale1 = min(1.0, (avail_sl1 - 0.2) / max(0.1, anim_base1)) if anim_base1 > avail_sl1 else 1.0

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.5*scale1)
        self.play(FadeIn(c1_title, shift=DOWN*0.1), run_time=0.5*scale1)
        for nitm in n_items:
            self.play(FadeIn(nitm, shift=RIGHT*0.2), run_time=0.3*scale1)

        act1 = (0.5 + 0.5 + len(n_items) * 0.3) * scale1
        rem_sl1 = max(0.15, avail_sl1 - act1)
        self.wait(rem_sl1)
        self.play(FadeOut(card1, shift=UP*0.25), run_time=fade_dur)

        # SLIDE 2: DẶN DÒ TỰ HỌC & BÀI TẬP VỀ NHÀ (Thầy chuyển sang biểu cảm khen ngợi)
        mascot_khen = get_mascot("thay_khen.png")
        if mascot and mascot_khen:
            self.play(ReplacementTransform(mascot, mascot_khen), run_time=0.6)
            mascot = mascot_khen

        c2_title = safe_text("HƯỚNG DẪN TỰ HỌC & DẶN DÒ VỀ NHÀ", font_size=25, weight=BOLD, color=COLOR_EMERALD, max_width=9.2)
        c2_line = Line(LEFT * 4.2, RIGHT * 4.2, stroke_width=1, color=COLOR_EMERALD)
'''

    code += "        hw_items = []\n"
    for h in hw:
        safe_h = h.replace('"', '\\"')
        code += f'        hw_items.append(safe_text("{safe_h}", font_size=20, color=COLOR_TEXT_MAIN, max_width=9.2, max_chars=48))\n'

    code += '''
        bye = safe_text("CẢM ƠN CÁC EM ĐÃ CHÚ Ý LẮNG NGHE! CHÚC CÁC EM HỌC TỐT!", font_size=22, weight=BOLD, color=COLOR_CYAN, max_width=9.2)
        c2_content = VGroup(c2_title, c2_line, *hw_items, Line(LEFT*4.2, RIGHT*4.2, stroke_width=1, color=COLOR_EMERALD), bye).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        fit_safe_box(c2_content, max_width=9.4, max_height=4.6)
        c2_content.move_to([0.65, -0.35, 0])

        c2_box = RoundedRectangle(corner_radius=0.3, width=c2_content.width + 0.6, height=c2_content.height + 0.6, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c2_content.get_center())
        card2 = VGroup(c2_box, c2_content)

        anim_base2 = 0.5 + 0.5 + len(hw_items) * 0.3 + 0.5
        avail_sl2 = max(0.2, t_sl2)
        scale2 = min(1.0, (avail_sl2 - 0.2) / max(0.1, anim_base2)) if anim_base2 > avail_sl2 else 1.0

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.5*scale2)
        self.play(FadeIn(c2_title, shift=DOWN*0.1), run_time=0.5*scale2)
        for hitm in hw_items:
            self.play(FadeIn(hitm, shift=RIGHT*0.2), run_time=0.3*scale2)
        self.play(FadeIn(bye, scale=1.03), run_time=0.5*scale2)

        act2 = (0.5 + 0.5 + len(hw_items) * 0.3 + 0.5) * scale2
        rem_sl2 = max(0.15, avail_sl2 - act2)
        self.wait(rem_sl2)

        if mascot:
            self.play(FadeOut(mascot, shift=DOWN*0.2), run_time=0.5)

if __name__ == "__main__":
    pass
'''
    return code


def build_concat_code(lesson: dict) -> str:
    lid = lesson["id"]
    ltitle = lesson["lesson_title"]
    vid_name = lesson.get("video_filename", f"Toan6_Bai{lid}_HoanChinh.mp4")

    return f'''"""
CONCAT LESSON PIPELINE CHO BÀI {lid}: {ltitle}
Khớp 1:1 từng mili-giây giữa Video Manim và Audio Thuyết Minh
"""

import os
import sys
import glob
import shutil
import tempfile
import subprocess
import re
from mutagen.mp3 import MP3

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(CURRENT_DIR, "audio")
OUTPUT_DIR = os.path.join(CURRENT_DIR, "output_scenes_full")
FINAL_OUTPUT = os.path.join(CURRENT_DIR, "{vid_name}")
PUBLIC_VIDEOS = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "..", "public", "videos"))
DIST_VIDEOS = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "..", "dist", "videos"))

os.makedirs(OUTPUT_DIR, exist_ok=True)

SCENE_DEFS = [
    {{"py": "scene1_khoidong.py", "scene": "Scene1KhoiDong", "audio": "scene1_full.mp3", "out": "scene1_synced.mp4"}},
    {{"py": "scene2_kienthuc.py", "scene": "Scene2KienThuc", "audio": "scene2_full.mp3", "out": "scene2_synced.mp4"}},
    {{"py": "scene3_vidu.py",     "scene": "Scene3ViDu",     "audio": "scene3_full.mp3", "out": "scene3_synced.mp4"}},
    {{"py": "scene4_canhbao.py",  "scene": "Scene4CanhBao",  "audio": "scene4_full.mp3", "out": "scene4_synced.mp4"}},
    {{"py": "scene5_tongket.py",  "scene": "Scene5TongKet",  "audio": "scene5_full.mp3", "out": "scene5_synced.mp4"}},
]


def render_scene(sc_def, quality_flag="-ql"):
    py_file = os.path.join(CURRENT_DIR, sc_def["py"])
    scene_name = sc_def["scene"]
    audio_file = os.path.join(AUDIO_DIR, sc_def["audio"])
    if not os.path.exists(audio_file):
        alt_audio = os.path.join(AUDIO_DIR, sc_def["audio"].replace("_full.mp3", "_voice.mp3"))
        if os.path.exists(alt_audio):
            audio_file = alt_audio
    out_synced = os.path.join(OUTPUT_DIR, sc_def["out"])

    print(f"\\n[RENDER] Dang render", py_file, "->", scene_name, quality_flag, "...")
    res = subprocess.run(["manim", quality_flag, py_file, scene_name], cwd=CURRENT_DIR)
    if res.returncode != 0:
        raise RuntimeError("Loi render manim: " + scene_name)

    v_pattern = os.path.join(CURRENT_DIR, "media", "videos", sc_def["py"].replace(".py", ""), "*", scene_name + ".mp4")
    v_matches = glob.glob(v_pattern)
    if not v_matches:
        raise FileNotFoundError("Khong tim thay video render: " + v_pattern)

    raw_video = v_matches[0]
    print("  -> Video raw:", raw_video)

    if os.path.exists(audio_file):
        a_len = float(MP3(audio_file).info.length)
        print("  -> Audio:", audio_file, "(" + str(round(a_len, 2)) + "s)")
        cmd = [
            "ffmpeg", "-y",
            "-i", raw_video,
            "-i", audio_file,
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-t", str(a_len),
            "-movflags", "+faststart",
            out_synced
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0:
            raise RuntimeError("Loi ghep audio: " + str(res.stderr))
    else:
        shutil.copy2(raw_video, out_synced)

    return out_synced


def concat_scenes(synced_files):
    print("\\n[CONCAT] Dang ghep noi", len(synced_files), "scenes...")
    list_txt = os.path.join(OUTPUT_DIR, "concat_list.txt")
    with open(list_txt, "w", encoding="utf-8") as f:
        for sf in synced_files:
            clean_p = sf.replace("\\\\", "/")
            f.write("file \'" + clean_p + "\'\\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", list_txt,
        "-c", "copy",
        "-movflags", "+faststart",
        FINAL_OUTPUT
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0:
        raise RuntimeError("Loi concat: " + str(res.stderr))

    dur_str = "00:00"
    try:
        chk = subprocess.run(["ffmpeg", "-i", FINAL_OUTPUT], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors="replace")
        m = re.search(r"Duration:\\s*(\\d+):(\\d+):([0-9.]+)", chk.stderr)
        if m:
            mins = int(m.group(1)) * 60 + int(m.group(2))
            secs = int(float(m.group(3)))
            dur_str = "%02d:%02d" % (mins, secs)
    except Exception:
        pass

    size_mb = os.path.getsize(FINAL_OUTPUT) / (1024 * 1024)
    print("\\n=======================================================")
    print("🎉 XUAT BAN THANH CONG:", FINAL_OUTPUT)
    print("   Thoi luong:", dur_str, "| Dung luong: %.2f MB" % size_mb)
    print("=======================================================")

    for pub_dir in [PUBLIC_VIDEOS, DIST_VIDEOS]:
        if os.path.exists(pub_dir):
            try:
                dest = os.path.join(pub_dir, os.path.basename(FINAL_OUTPUT))
                shutil.copy2(FINAL_OUTPUT, dest)
                print("   -> Da copy sang:", dest)
            except Exception as e:
                print("   -> Canh bao copy", pub_dir, ":", e)

    return FINAL_OUTPUT


def run(quality_flag="-ql"):
    synced = []
    for sc in SCENE_DEFS:
        synced.append(render_scene(sc, quality_flag))
    out = concat_scenes(synced)
    print("DONE:", out)


if __name__ == "__main__":
    q_flag = "-ql"
    if len(sys.argv) > 1:
        q_flag = sys.argv[1]
    run(q_flag)
'''


def generate_lesson_package(lesson: dict, output_dir: str):
    """Tự động xuất 5 file scene và concat_lesson.py cho bài học"""
    os.makedirs(output_dir, exist_ok=True)

    files = {
        "scene1_khoidong.py": build_scene1_code(lesson),
        "scene2_kienthuc.py": build_scene2_code(lesson),
        "scene3_vidu.py": build_scene3_code(lesson),
        "scene4_canhbao.py": build_scene4_code(lesson),
        "scene5_tongket.py": build_scene5_code(lesson),
        "concat_lesson.py": build_concat_code(lesson),
    }

    for fname, content in files.items():
        fpath = os.path.join(output_dir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  -> Đã tạo: {fpath}")

    print(f"✅ Hoàn tất sinh package Manim cho bài: {lesson.get('lesson_key')}")
