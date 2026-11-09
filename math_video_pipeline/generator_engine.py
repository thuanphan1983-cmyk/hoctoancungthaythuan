"""
GENERATOR ENGINE CHO TỪNG BÀI HỌC TOÁN 6
Tự động sinh trọn bộ mã nguồn Manim (scene1 -> scene5) và concat_lesson.py
Tuân thủ tuyệt đối quy chuẩn:
1. Strict Safe-Zone & Auto-Scale (fit_safe_box, wrap_text, surround buff=0.40, margins >= 1.2 x 0.8).
2. Audio-Visual Sync chính xác từng mili-giây (mutagen MP3 get_audio_duration, không số cứng, 1:1 sync).
3. Font Arial Unicode MS & Segoe UI Symbol (zero hex boxes, không gọi LaTeX/dvisvgm).
4. Đồng hồ đếm ngược 45s góc trên bên phải UR (.to_corner(UR, buff=0.45)), font Segoe UI.
5. Đề bài giữ nguyên vẹn trên màn hình khi hiển thị lời giải chi tiết (không đè chữ, không tràn biên).
"""

import os
import sys

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
MATH_FONT = "Segoe UI Symbol"

def math_text(expr, font_size=24, color=COLOR_TEXT_MAIN, weight=BOLD):
    return Text(expr, font=MATH_FONT, font_size=font_size, weight=weight, color=color)

def wrap_text(text: str, max_chars: int = 54) -> str:
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

def safe_text(txt, font=FONT_FAMILY, font_size=24, weight=NORMAL, color=COLOR_TEXT_MAIN, max_width=10.6, max_chars=54):
    if len(txt) > max_chars and "\\n" not in txt:
        txt = wrap_text(txt, max_chars=max_chars)
    t = Text(txt, font=font, font_size=font_size, weight=weight, color=color, line_spacing=0.85)
    if t.width > max_width:
        t.scale_to_fit_width(max_width)
    return t

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

        header = Text("PHẦN 1: ĐẶT VẤN ĐỀ & KHỞI ĐỘNG THỰC TẾ", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_CYAN)
        header_line = Line(LEFT * 5.6, RIGHT * 5.6, stroke_width=2, color=COLOR_CYAN)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
'''

    colors = ["COLOR_AMBER", "COLOR_CYAN", "COLOR_EMERALD", "COLOR_INDIGO"]
    for idx, sl in enumerate(slides):
        col = colors[idx % len(colors)]
        s_num = idx + 1
        heading = sl.get("heading", f"SLIDE {s_num}").replace('"', '\\"')
        sub = sl.get("sub", "").replace('"', '\\"')
        bullets = sl.get("bullets", [])

        code += f'''
        # ----------------- SLIDE {s_num} -----------------
        a_file_{s_num} = os.path.join(audio_dir, "scene1_slide{s_num}.mp3")
        t_s{s_num} = get_audio_duration(a_file_{s_num}, fallback=timing.get("scene1_slide{s_num}", 25.0))

        c{s_num}_title = safe_text("{heading}", font_size=28, weight=BOLD, color={col}, max_width=10.4)
        c{s_num}_sub = safe_text("{sub}", font_size=23, weight=SEMIBOLD, color=COLOR_TEXT_MUTED, max_width=10.4)
        line{s_num} = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color={col})
'''
        code += f"        b_items_{s_num} = []\n"
        for b in bullets:
            safe_b = b.replace('"', '\\"')
            code += f'        b_items_{s_num}.append(safe_text("• {safe_b}", font_size=24, color=COLOR_TEXT_MAIN, max_width=10.4, max_chars=52))\n'

        code += f'''        c{s_num}_content = VGroup(c{s_num}_title, c{s_num}_sub, line{s_num}, *b_items_{s_num}).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        fit_safe_box(c{s_num}_content, max_width=10.8, max_height=4.8)
        c{s_num}_content.move_to([0, -0.4, 0])

        c{s_num}_box = RoundedRectangle(corner_radius=0.3, width=c{s_num}_content.width + 0.8, height=c{s_num}_content.height + 0.7, stroke_color={col}, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c{s_num}_content.get_center())
        card{s_num} = VGroup(c{s_num}_box, c{s_num}_content)

        # Tính toán runtime animation động khớp 1:1 với audio
        anim_base = 0.6 + 0.8 + len(b_items_{s_num}) * 0.35
        fade_out_dur = 0.6
        avail_time = max(0.2, t_s{s_num} - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.6 * anim_scale
        rt_head = 0.8 * anim_scale
        rt_item = 0.35 * anim_scale

        self.play(FadeIn(c{s_num}_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(c{s_num}_title, shift=DOWN*0.1), FadeIn(c{s_num}_sub, shift=UP*0.1), run_time=rt_head)
        for bitm in b_items_{s_num}:
            self.play(FadeIn(bitm, shift=RIGHT*0.2), run_time=rt_item)

        actual_anim = rt_box + rt_head + len(b_items_{s_num}) * rt_item
        rem_s{s_num} = max(0.15, avail_time - actual_anim)
        self.wait(rem_s{s_num})
        self.play(FadeOut(card{s_num}, shift=UP*0.25), run_time=fade_out_dur)
'''

    code += '''
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

        header = Text("PHẦN 2: HÌNH THÀNH KIẾN THỨC MỚI", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_EMERALD)
        header_line = Line(LEFT * 5.6, RIGHT * 5.6, stroke_width=2, color=COLOR_EMERALD)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
'''

    colors = ["COLOR_CYAN", "COLOR_EMERALD", "COLOR_AMBER", "COLOR_ROSE"]
    for idx, sl in enumerate(slides):
        col = colors[idx % len(colors)]
        s_num = idx + 1
        heading = sl.get("heading", f"KIẾN THỨC {s_num}").replace('"', '\\"')
        sub = sl.get("sub", "").replace('"', '\\"')
        items = sl.get("items", [])

        code += f'''
        # ----------------- SLIDE {s_num} -----------------
        a_file_{s_num} = os.path.join(audio_dir, "scene2_slide{s_num}.mp3")
        t_s{s_num} = get_audio_duration(a_file_{s_num}, fallback=timing.get("scene2_slide{s_num}", 28.0))

        c{s_num}_title = safe_text("{heading}", font_size=28, weight=BOLD, color={col}, max_width=10.4)
        c{s_num}_sub = safe_text("{sub}", font_size=23, weight=SEMIBOLD, color=COLOR_TEXT_MUTED, max_width=10.4)
        line{s_num} = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color={col})
'''
        code += f"        itms_{s_num} = []\n"
        for it in items:
            safe_it = it.replace('"', '\\"')
            code += f'        itms_{s_num}.append(safe_text("{safe_it}", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4, max_chars=54))\n'

        code += f'''        c{s_num}_content = VGroup(c{s_num}_title, c{s_num}_sub, line{s_num}, *itms_{s_num}).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit_safe_box(c{s_num}_content, max_width=10.8, max_height=4.8)
        c{s_num}_content.move_to([0, -0.4, 0])

        c{s_num}_box = RoundedRectangle(corner_radius=0.3, width=c{s_num}_content.width + 0.8, height=c{s_num}_content.height + 0.7, stroke_color={col}, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c{s_num}_content.get_center())
        card{s_num} = VGroup(c{s_num}_box, c{s_num}_content)

        anim_base = 0.6 + 0.8 + len(itms_{s_num}) * 0.35
        fade_out_dur = 0.6
        avail_time = max(0.2, t_s{s_num} - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.6 * anim_scale
        rt_head = 0.8 * anim_scale
        rt_item = 0.35 * anim_scale

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
        self.play(FadeIn(header_group, shift=RIGHT), run_time=1.0)
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

        # Khung chứa lớn toàn phần
        c{e_num}_box = RoundedRectangle(corner_radius=0.3, width=12.0, height=5.6, stroke_color={col}, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.45, 0])

        badge{e_num} = Text("{badge}", font=FONT_FAMILY, font_size=22, weight=BOLD, color={col})
        head{e_num} = safe_text("{head}", font_size=25, weight=BOLD, color=COLOR_AMBER, max_width=10.4)
        sep{e_num} = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color={col})
        q{e_num}_lead = safe_text("{lead}", font_size=22, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=10.4, max_chars=54)
        q{e_num}_a = safe_text("{qa}", font_size=21, color=COLOR_TEXT_MAIN, max_width=10.4, max_chars=54)
        q{e_num}_b = safe_text("{qb}", font_size=21, color=COLOR_TEXT_MAIN, max_width=10.4, max_chars=54)
'''

        code += f"        bl_sub_{e_num} = []\n"
        for bi in blank_items:
            safe_bi = bi.replace('"', '\\"')
            code += f'        bl_sub_{e_num}.append(Text("{safe_bi}", font=FONT_FAMILY, font_size=21, weight=BOLD, color=COLOR_AMBER))\n'

        code += f'''        if bl_sub_{e_num}:
            def sep(): return Text("  ;  ", font=FONT_FAMILY, font_size=20, color=COLOR_TEXT_MUTED)
            bl_row = VGroup()
            for i_b, b_elem in enumerate(bl_sub_{e_num}):
                if i_b > 0:
                    bl_row.add(sep())
                bl_row.add(b_elem)
            bl_row.arrange(RIGHT, buff=0.1)
            fit_safe_box(bl_row, max_width=10.0, max_height=0.45)
            bl_box = RoundedRectangle(corner_radius=0.15, width=bl_row.width + 0.5, height=0.50, stroke_color=COLOR_AMBER, stroke_width=1, fill_color="#0f172a", fill_opacity=0.9).move_to(bl_row.get_center())
            q{e_num}_blank_grp = VGroup(bl_box, bl_row)
            problem{e_num}_grp = VGroup(badge{e_num}, head{e_num}, sep{e_num}, q{e_num}_lead, q{e_num}_a, q{e_num}_b, q{e_num}_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.10)
        else:
            problem{e_num}_grp = VGroup(badge{e_num}, head{e_num}, sep{e_num}, q{e_num}_lead, q{e_num}_a, q{e_num}_b).arrange(DOWN, aligned_edge=LEFT, buff=0.11)

        fit_safe_box(problem{e_num}_grp, max_width=11.0, max_height=2.5)
        problem{e_num}_grp.move_to([0, 0.85, 0])

        # BƯỚC 1: Hiện Đề bài khớp 1:1 thời lượng voice intro
        self.play(FadeIn(c{e_num}_box, scale=0.96), run_time=0.6)
        self.play(FadeIn(problem{e_num}_grp, shift=DOWN * 0.15), run_time=1.0)
        rem_intro{e_num} = max(0.15, t_ex{e_num}_intro - 1.6)
        self.wait(rem_intro{e_num})

        # BƯỚC 2: Đồng hồ đếm ngược 45s góc trên bên phải UR (không che đề)
        badge_t{e_num}, vt{e_num}, text_t{e_num}, pbg_t{e_num}, pfill_t{e_num} = build_timer_widget({col})
        timer_grp{e_num} = VGroup(badge_t{e_num}, pbg_t{e_num}, pfill_t{e_num}, text_t{e_num})
        self.play(FadeIn(timer_grp{e_num}, shift=DOWN*0.3), run_time=0.6)
        self.play(vt{e_num}.animate.set_value(0), run_time=max(1.0, t_ex{e_num}_timer - 1.2), rate_func=linear)
        self.play(FadeOut(timer_grp{e_num}, shift=UP*0.2), run_time=0.6)

        # BƯỚC 3: Lời giải chi tiết (Đề bài giữ nguyên ở nửa trên, lời giải ở nửa dưới không đè)
        sol{e_num}_head = Text("✓ HƯỚNG DẪN GIẢI CHI TIẾT:", font=FONT_FAMILY, font_size=20, weight=BOLD, color=COLOR_EMERALD)
        sol{e_num}_anal = safe_text("• Phân tích: {analysis}", font_size=19, color=COLOR_TEXT_MUTED, max_width=10.4, max_chars=58)
        sol{e_num}_a = safe_text("• a) {sola}", font_size=20, color=COLOR_TEXT_MAIN, max_width=10.4, max_chars=58)
        sol{e_num}_b = safe_text("• b) {solb}", font_size=20, weight=BOLD, color=COLOR_CYAN, max_width=10.4, max_chars=58)

        sol{e_num}_content = VGroup(sol{e_num}_head, sol{e_num}_anal, sol{e_num}_a, sol{e_num}_b).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        fit_safe_box(sol{e_num}_content, max_width=10.8, max_height=1.85)
        sol{e_num}_content.move_to([0, -1.95, 0])

        sol{e_num}_box = RoundedRectangle(corner_radius=0.2, width=11.4, height=sol{e_num}_content.height + 0.35, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color="#0f172a", fill_opacity=0.95).move_to(sol{e_num}_content.get_center())
        sol{e_num}_card = VGroup(sol{e_num}_box, sol{e_num}_content)

        self.play(FadeIn(sol{e_num}_card, shift=UP * 0.2), run_time=0.8)
        rem_sol{e_num} = max(0.15, t_ex{e_num}_sol - 1.4)
        self.wait(rem_sol{e_num})

        self.play(FadeOut(c{e_num}_box), FadeOut(problem{e_num}_grp), FadeOut(sol{e_num}_card), run_time=0.6)
'''

    code += '''
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

        header = Text("PHẦN 4: LỖI SAI KINH ĐIỂN CẦN TRÁNH", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_ROSE)
        header_line = Line(LEFT * 5.6, RIGHT * 5.6, stroke_width=2, color=COLOR_ROSE)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
'''

    for idx, tr in enumerate(traps):
        t_num = idx + 1
        heading = tr.get("heading", f"LỖI SAI {t_num}").replace('"', '\\"')
        bad = tr.get("bad", "").replace('"', '\\"')
        good = tr.get("good", "").replace('"', '\\"')
        note = tr.get("note", "").replace('"', '\\"')

        code += f'''
        # ----------------- TRAP {t_num} -----------------
        a_file_{t_num} = os.path.join(audio_dir, "scene4_trap{t_num}.mp3")
        t_tr{t_num} = get_audio_duration(a_file_{t_num}, fallback=timing.get("scene4_trap{t_num}", 22.0))

        c{t_num}_title = safe_text("{heading}", font_size=26, weight=BOLD, color=COLOR_ROSE, max_width=10.4)
        line{t_num} = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_ROSE)

        bad_{t_num} = VGroup(math_text("✗", font_size=26, color=COLOR_ROSE), safe_text("  {bad}", font_size=23, weight=BOLD, color=COLOR_ROSE, max_width=9.8, max_chars=50)).arrange(RIGHT, buff=0.08)
        good_{t_num} = VGroup(math_text("✓", font_size=26, color=COLOR_EMERALD), safe_text("  {good}", font_size=23, weight=BOLD, color=COLOR_EMERALD, max_width=9.8, max_chars=50)).arrange(RIGHT, buff=0.08)
        note_{t_num} = safe_text("• Lời khuyên: {note}", font_size=22, color=COLOR_TEXT_MUTED, max_width=10.4, max_chars=54)

        c{t_num}_content = VGroup(c{t_num}_title, line{t_num}, bad_{t_num}, good_{t_num}, note_{t_num}).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fit_safe_box(c{t_num}_content, max_width=10.8, max_height=4.6)
        c{t_num}_content.move_to([0, -0.4, 0])

        c{t_num}_box = RoundedRectangle(corner_radius=0.3, width=c{t_num}_content.width + 0.8, height=c{t_num}_content.height + 0.7, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c{t_num}_content.get_center())
        card{t_num} = VGroup(c{t_num}_box, c{t_num}_content)

        anim_base = 0.6 + 0.6 + 0.6 + 0.6 + 0.5
        fade_out_dur = 0.6
        avail_time = max(0.2, t_tr{t_num} - fade_out_dur)
        anim_scale = min(1.0, (avail_time - 0.2) / max(0.1, anim_base)) if anim_base > avail_time else 1.0

        rt_box = 0.6 * anim_scale
        rt_head = 0.6 * anim_scale
        rt_bad = 0.6 * anim_scale
        rt_good = 0.6 * anim_scale
        rt_note = 0.5 * anim_scale

        self.play(FadeIn(c{t_num}_box, scale=0.96), run_time=rt_box)
        self.play(FadeIn(c{t_num}_title, shift=DOWN*0.1), run_time=rt_head)
        self.play(FadeIn(bad_{t_num}, shift=RIGHT*0.2), run_time=rt_bad)
        self.play(FadeIn(good_{t_num}, shift=RIGHT*0.2), run_time=rt_good)
        self.play(FadeIn(note_{t_num}, shift=UP*0.1), run_time=rt_note)

        actual_anim = rt_box + rt_head + rt_bad + rt_good + rt_note
        rem_tr{t_num} = max(0.15, avail_time - actual_anim)
        self.wait(rem_tr{t_num})
        self.play(FadeOut(card{t_num}, shift=UP*0.25), run_time=fade_out_dur)
'''

    code += '''
if __name__ == "__main__":
    pass
'''
    return code


def build_scene5_code(lesson: dict) -> str:
    p5 = lesson["part5"]
    nodes = p5.get("summary_nodes", [])
    hw = p5.get("homework", [])
    ltitle = lesson.get("lesson_title", "Bài học").replace('"', '\\"')

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

        a_file_s5 = os.path.join(audio_dir, "scene5_full.mp3")
        t_s5 = get_audio_duration(a_file_s5, fallback=timing.get("scene5", 45.0))
        t_sl1 = t_s5 * 0.58
        t_sl2 = t_s5 * 0.42

        header = Text("PHẦN 5: SƠ ĐỒ TƯ DUY TỔNG KẾT & DẶN DÒ", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_INDIGO)
        header_line = Line(LEFT * 5.6, RIGHT * 5.6, stroke_width=2, color=COLOR_INDIGO)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        # SLIDE 1: SƠ ĐỒ TƯ DUY
        c1_title = safe_text("SƠ ĐỒ TƯ DUY TRỌNG TÂM: {ltitle.upper()}", font_size=27, weight=BOLD, color=COLOR_AMBER, max_width=10.4)
        c1_line = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_INDIGO)
'''

    code += "        n_items = []\n"
    for n in nodes:
        safe_n = n.replace('"', '\\"')
        code += f'        n_items.append(safe_text("{safe_n}", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4, max_chars=54))\n'

    code += f'''
        c1_content = VGroup(c1_title, c1_line, *n_items).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        fit_safe_box(c1_content, max_width=10.8, max_height=4.8)
        c1_content.move_to([0, -0.4, 0])

        c1_box = RoundedRectangle(corner_radius=0.3, width=c1_content.width + 0.8, height=c1_content.height + 0.7, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c1_content.get_center())
        card1 = VGroup(c1_box, c1_content)

        anim_base1 = 0.6 + 0.6 + len(n_items) * 0.35
        fade_dur = 0.6
        avail_sl1 = max(0.2, t_sl1 - fade_dur)
        scale1 = min(1.0, (avail_sl1 - 0.2) / max(0.1, anim_base1)) if anim_base1 > avail_sl1 else 1.0

        self.play(FadeIn(c1_box, scale=0.96), run_time=0.6*scale1)
        self.play(FadeIn(c1_title, shift=DOWN*0.1), run_time=0.6*scale1)
        for nitm in n_items:
            self.play(FadeIn(nitm, shift=RIGHT*0.2), run_time=0.35*scale1)

        act1 = (0.6 + 0.6 + len(n_items) * 0.35) * scale1
        rem_sl1 = max(0.15, avail_sl1 - act1)
        self.wait(rem_sl1)
        self.play(FadeOut(card1, shift=UP*0.25), run_time=fade_dur)

        # SLIDE 2: DẶN DÒ TỰ HỌC & BÀI TẬP VỀ NHÀ
        c2_title = safe_text("HƯỚNG DẪN TỰ HỌC & DẶN DÒ VỀ NHÀ", font_size=27, weight=BOLD, color=COLOR_EMERALD, max_width=10.4)
        c2_line = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_EMERALD)
'''

    code += "        hw_items = []\n"
    for h in hw:
        safe_h = h.replace('"', '\\"')
        code += f'        hw_items.append(safe_text("{safe_h}", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4, max_chars=54))\n'

    code += '''
        bye = safe_text("CẢM ƠN CÁC EM ĐÃ CHÚ Ý LẮNG NGHE! CHÚC CÁC EM HỌC TỐT!", font_size=24, weight=BOLD, color=COLOR_CYAN, max_width=10.4)
        c2_content = VGroup(c2_title, c2_line, *hw_items, Line(LEFT*4.5, RIGHT*4.5, stroke_width=1, color=COLOR_EMERALD), bye).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fit_safe_box(c2_content, max_width=10.8, max_height=4.8)
        c2_content.move_to([0, -0.4, 0])

        c2_box = RoundedRectangle(corner_radius=0.3, width=c2_content.width + 0.8, height=c2_content.height + 0.7, stroke_color=COLOR_EMERALD, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to(c2_content.get_center())
        card2 = VGroup(c2_box, c2_content)

        anim_base2 = 0.6 + 0.6 + len(hw_items) * 0.35 + 0.6
        avail_sl2 = max(0.2, t_sl2)
        scale2 = min(1.0, (avail_sl2 - 0.2) / max(0.1, anim_base2)) if anim_base2 > avail_sl2 else 1.0

        self.play(FadeIn(c2_box, scale=0.96), run_time=0.6*scale2)
        self.play(FadeIn(c2_title, shift=DOWN*0.1), run_time=0.6*scale2)
        for hitm in hw_items:
            self.play(FadeIn(hitm, shift=RIGHT*0.2), run_time=0.35*scale2)
        self.play(FadeIn(bye, scale=1.03), run_time=0.6*scale2)

        act2 = (0.6 + 0.6 + len(hw_items) * 0.35 + 0.6) * scale2
        rem_sl2 = max(0.15, avail_sl2 - act2)
        self.wait(rem_sl2)

if __name__ == "__main__":
    pass
'''
    return code


def build_concat_code(lesson: dict) -> str:
    lid = lesson["id"]
    ltitle = lesson["lesson_title"]
    vid_name = lesson["video_filename"]

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

SCENE_DEFS = [
    {{"id": "scene1", "file": "scene1_khoidong.py", "class": "Scene1KhoiDong", "audio": "scene1_full.mp3"}},
    {{"id": "scene2", "file": "scene2_kienthuc.py", "class": "Scene2KienThuc", "audio": "scene2_full.mp3"}},
    {{"id": "scene3", "file": "scene3_vidu.py", "class": "Scene3ViDu", "audio": "scene3_full.mp3"}},
    {{"id": "scene4", "file": "scene4_canhbao.py", "class": "Scene4CanhBao", "audio": "scene4_full.mp3"}},
    {{"id": "scene5", "file": "scene5_tongket.py", "class": "Scene5TongKet", "audio": "scene5_full.mp3"}}
]

def render_scene(sc_def, quality_flag="-ql"):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    sc_id = sc_def["id"]
    sc_file = os.path.join(CURRENT_DIR, sc_def["file"])
    sc_class = sc_def["class"]
    sc_audio = os.path.join(AUDIO_DIR, sc_def["audio"])
    synced_output = os.path.join(OUTPUT_DIR, f"{{sc_id}}_synced.mp4")

    temp_media = os.path.join(tempfile.gettempdir(), f"mnm_{{sc_id}}_{lid}")
    if os.path.exists(temp_media):
        shutil.rmtree(temp_media, ignore_errors=True)
    os.makedirs(temp_media, exist_ok=True)

    cmd = ["manim", quality_flag, sc_file, sc_class, "--media_dir", temp_media]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        raise RuntimeError(f"Manim render failed for {{sc_class}}: {{res.stderr[-400:]}}")

    mp4_files = glob.glob(os.path.join(temp_media, "**", f"{{sc_class}}.mp4"), recursive=True)
    if not mp4_files:
        mp4_files = [f for f in glob.glob(os.path.join(temp_media, "**", "*.mp4"), recursive=True) if "partial_movie_files" not in f]
    if not mp4_files:
        raise FileNotFoundError(f"No mp4 found for {{sc_class}}")
    raw_video = mp4_files[0]

    if os.path.exists(synced_output):
        os.remove(synced_output)

    mux_cmd = ["ffmpeg", "-y", "-i", raw_video, "-i", sc_audio, "-c:v", "copy", "-c:a", "aac", "-shortest", synced_output]
    mux_res = subprocess.run(mux_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if mux_res.returncode != 0 or not os.path.exists(synced_output):
        mux_cmd = ["ffmpeg", "-y", "-i", raw_video, "-i", sc_audio, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", synced_output]
        subprocess.run(mux_cmd, check=True)

    shutil.rmtree(temp_media, ignore_errors=True)
    return synced_output


def concat_scenes(synced_files):
    os.makedirs(os.path.dirname(FINAL_OUTPUT), exist_ok=True)
    list_file = os.path.join(OUTPUT_DIR, "concat_list.txt")
    with open(list_file, "w", encoding="utf-8") as f:
        for p in synced_files:
            safe_p = p.replace("\\\\", "/")
            f.write(f"file '{{safe_p}}'\\n")

    concat_cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", FINAL_OUTPUT]
    res = subprocess.run(concat_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0 or not os.path.exists(FINAL_OUTPUT) or os.path.getsize(FINAL_OUTPUT) == 0:
        concat_cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", FINAL_OUTPUT]
        subprocess.run(concat_cmd, check=True)

    for d in [PUBLIC_VIDEOS, DIST_VIDEOS]:
        os.makedirs(d, exist_ok=True)
        target = os.path.join(d, "{vid_name}")
        shutil.copy2(FINAL_OUTPUT, target)

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


def generate_lesson_package(lesson: dict, target_dir: str):
    """Sinh toàn bộ các file mã nguồn cho bài học vào target_dir"""
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "scene1_khoidong.py"), "w", encoding="utf-8") as f:
        f.write(build_scene1_code(lesson))
    with open(os.path.join(target_dir, "scene2_kienthuc.py"), "w", encoding="utf-8") as f:
        f.write(build_scene2_code(lesson))
    with open(os.path.join(target_dir, "scene3_vidu.py"), "w", encoding="utf-8") as f:
        f.write(build_scene3_code(lesson))
    with open(os.path.join(target_dir, "scene4_canhbao.py"), "w", encoding="utf-8") as f:
        f.write(build_scene4_code(lesson))
    with open(os.path.join(target_dir, "scene5_tongket.py"), "w", encoding="utf-8") as f:
        f.write(build_scene5_code(lesson))
    with open(os.path.join(target_dir, "concat_lesson.py"), "w", encoding="utf-8") as f:
        f.write(build_concat_code(lesson))
