"""
GENERATOR ENGINE CHO TỪNG BÀI HỌC TOÁN 6
Tự động sinh trọn bộ mã nguồn Manim (scene1 -> scene5) và concat_lesson.py
Tuân thủ tuyệt đối quy chuẩn:
- Không dùng MathTex (tránh lỗi thiếu LaTeX trên Windows), dùng vector math_text Segoe UI Symbol.
- Đồng hồ đếm ngược 45s ở góc trên bên phải UR (.to_corner(UR, buff=0.45)), không che đề bài.
- Safe margins: width <= 11.0, không tràn viền bo góc.
- Câu hỏi điền khuyết rõ ràng và lời giải chi tiết từng dòng.
"""

import os
import sys

HEADER_IMPORTS = '''import os
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
MATH_FONT = "Segoe UI Symbol"

def math_text(expr, font_size=24, color=COLOR_TEXT_MAIN, weight=BOLD):
    return Text(expr, font=MATH_FONT, font_size=font_size, weight=weight, color=color)

def safe_text(txt, font=FONT_FAMILY, font_size=24, weight=NORMAL, color=COLOR_TEXT_MAIN, max_width=10.6):
    t = Text(txt, font=font, font_size=font_size, weight=weight, color=color)
    if t.width > max_width:
        t.scale_to_fit_width(max_width)
    return t
'''


def build_scene1_code(lesson: dict) -> str:
    p1 = lesson["part1"]
    slides = p1.get("slides", [])
    
    code = HEADER_IMPORTS + f'''

class Scene1KhoiDong(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        timing_file = os.path.join(os.path.dirname(__file__), "audio", "timing_data.json")
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
        t_s{s_num} = timing.get("scene1_slide{s_num}", 25.0)
        c{s_num}_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color={col}, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        c{s_num}_title = safe_text("{heading}", font_size=28, weight=BOLD, color={col}, max_width=10.6)
        c{s_num}_sub = safe_text("{sub}", font_size=23, weight=SEMIBOLD, color=COLOR_TEXT_MUTED, max_width=10.6)
        line{s_num} = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color={col})
'''
        code += f"        b_items_{s_num} = []\n"
        for b in bullets:
            safe_b = b.replace('"', '\\"')
            code += f'        b_items_{s_num}.append(safe_text("• {safe_b}", font_size=24, color=COLOR_TEXT_MAIN, max_width=10.4))\n'

        code += f'''        c{s_num}_content = VGroup(c{s_num}_title, c{s_num}_sub, line{s_num}, *b_items_{s_num}).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        c{s_num}_content.move_to(c{s_num}_box.get_center())
        card{s_num} = VGroup(c{s_num}_box, c{s_num}_content)

        self.play(FadeIn(c{s_num}_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(c{s_num}_title, shift=DOWN*0.1), FadeIn(c{s_num}_sub, shift=UP*0.1), run_time=1.0)
        for bitm in b_items_{s_num}:
            self.play(FadeIn(bitm, shift=RIGHT*0.2), run_time=0.4)

        rem_s{s_num} = max(0.5, t_s{s_num} - (1.8 + len(b_items_{s_num}) * 0.4))
        self.wait(rem_s{s_num})
        self.play(FadeOut(card{s_num}, shift=UP*0.3), run_time=0.8)
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

        timing_file = os.path.join(os.path.dirname(__file__), "audio", "timing_data.json")
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
        t_s{s_num} = timing.get("scene2_slide{s_num}", 28.0)
        c{s_num}_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color={col}, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        c{s_num}_title = safe_text("{heading}", font_size=28, weight=BOLD, color={col}, max_width=10.6)
        c{s_num}_sub = safe_text("{sub}", font_size=23, weight=SEMIBOLD, color=COLOR_TEXT_MUTED, max_width=10.6)
        line{s_num} = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color={col})
'''
        code += f"        itms_{s_num} = []\n"
        for it in items:
            safe_it = it.replace('"', '\\"')
            code += f'        itms_{s_num}.append(safe_text("{safe_it}", font_size=23, color=COLOR_TEXT_MAIN, max_width=10.4))\n'

        code += f'''        c{s_num}_content = VGroup(c{s_num}_title, c{s_num}_sub, line{s_num}, *itms_{s_num}).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        c{s_num}_content.move_to(c{s_num}_box.get_center())
        card{s_num} = VGroup(c{s_num}_box, c{s_num}_content)

        self.play(FadeIn(c{s_num}_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(c{s_num}_title, shift=DOWN*0.1), FadeIn(c{s_num}_sub, shift=UP*0.1), run_time=1.0)
        for itm in itms_{s_num}:
            self.play(FadeIn(itm, shift=RIGHT*0.2), run_time=0.4)

        rem_s{s_num} = max(0.5, t_s{s_num} - (1.8 + len(itms_{s_num}) * 0.4))
        self.wait(rem_s{s_num})
        self.play(FadeOut(card{s_num}, shift=UP*0.3), run_time=0.8)
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
    timer_text = always_redraw(lambda: Text(f"⏱ {{int(vt.get_value()):02d}}s", font="Segoe UI", font_size=24, weight=BOLD, color=theme_color).move_to(badge.get_center() + UP * 0.1))
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

        timing_file = os.path.join(os.path.dirname(__file__), "audio", "timing_data.json")
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
        t_ex{e_num}_intro = timing.get("scene3_ex{e_num}_intro", 25.0)
        t_ex{e_num}_timer = timing.get("scene3_ex{e_num}_timer", 45.0)
        t_ex{e_num}_sol = timing.get("scene3_ex{e_num}_sol", 40.0)

        c{e_num}_box = RoundedRectangle(corner_radius=0.3, width=12.2, height=5.6, stroke_color={col}, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.45, 0])

        badge{e_num} = Text("{badge}", font=FONT_FAMILY, font_size=22, weight=BOLD, color={col})
        head{e_num} = safe_text("{head}", font_size=25, weight=BOLD, color=COLOR_AMBER, max_width=10.6)
        sep{e_num} = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color={col})
        q{e_num}_lead = safe_text("{lead}", font_size=23, weight=BOLD, color=COLOR_TEXT_MAIN, max_width=10.4)
        q{e_num}_a = safe_text("{qa}", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4)
        q{e_num}_b = safe_text("{qb}", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4)
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
            if bl_row.width > 10.2:
                bl_row.scale_to_fit_width(10.2)
            bl_box = RoundedRectangle(corner_radius=0.15, width=bl_row.width + 0.6, height=0.52, stroke_color=COLOR_AMBER, stroke_width=1, fill_color="#0f172a", fill_opacity=0.9).move_to(bl_row.get_center())
            q{e_num}_blank_grp = VGroup(bl_box, bl_row)
            problem{e_num}_grp = VGroup(badge{e_num}, head{e_num}, sep{e_num}, q{e_num}_lead, q{e_num}_a, q{e_num}_b, q{e_num}_blank_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        else:
            problem{e_num}_grp = VGroup(badge{e_num}, head{e_num}, sep{e_num}, q{e_num}_lead, q{e_num}_a, q{e_num}_b).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

        problem{e_num}_grp.move_to([0, 0.50, 0])

        self.play(FadeIn(c{e_num}_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(problem{e_num}_grp, shift=DOWN * 0.2), run_time=1.2)
        rem_intro{e_num} = max(0.1, t_ex{e_num}_intro - 2.0)
        self.wait(rem_intro{e_num})

        # BƯỚC 2: ĐỒNG HỒ ĐẾM NGƯỢC 45s GÓC TRÊN BÊN PHẢI UR
        badge_t{e_num}, vt{e_num}, text_t{e_num}, pbg_t{e_num}, pfill_t{e_num} = build_timer_widget({col})
        self.play(FadeIn(badge_t{e_num}), FadeIn(pbg_t{e_num}), FadeIn(pfill_t{e_num}), FadeIn(text_t{e_num}), run_time=0.8)
        self.play(vt{e_num}.animate.set_value(0), run_time=max(1.0, t_ex{e_num}_timer - 0.8), rate_func=linear)

        # BƯỚC 3: LỜI GIẢI CHI TIẾT (ĐỀ BÀI GIỮ NGUYÊN)
        self.play(FadeOut(badge_t{e_num}), FadeOut(pbg_t{e_num}), FadeOut(pfill_t{e_num}), FadeOut(text_t{e_num}), run_time=0.8)

        sol{e_num}_sep = Line(LEFT * 5.2, RIGHT * 5.2, stroke_width=1, color=COLOR_EMERALD)
        sol{e_num}_anal = safe_text("• Phân tích: {analysis}", font_size=21, color=COLOR_TEXT_MUTED, max_width=10.4)
        sol{e_num}_a = VGroup(math_text("✓", font_size=22, color=COLOR_EMERALD), safe_text(" {sola}", font_size=22, color=COLOR_EMERALD, max_width=10.0)).arrange(RIGHT, buff=0.08)
        sol{e_num}_b = VGroup(math_text("✓", font_size=22, color=COLOR_CYAN), safe_text(" {solb}", font_size=22, color=COLOR_CYAN, max_width=10.0)).arrange(RIGHT, buff=0.08)

        sol{e_num}_block = VGroup(sol{e_num}_sep, sol{e_num}_anal, sol{e_num}_a, sol{e_num}_b).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        sol{e_num}_block.move_to([0, -1.95, 0])

        self.play(FadeIn(sol{e_num}_block, shift=UP * 0.2), run_time=1.2)
        rem_sol{e_num} = max(0.1, t_ex{e_num}_sol - 2.0)
        self.wait(rem_sol{e_num})

        self.play(FadeOut(c{e_num}_box), FadeOut(problem{e_num}_grp), FadeOut(sol{e_num}_block), run_time=0.8)
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

        timing_file = os.path.join(os.path.dirname(__file__), "audio", "timing_data.json")
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
        t_tr{t_num} = timing.get("scene4_trap{t_num}", 22.0)
        c{t_num}_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_ROSE, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        c{t_num}_title = safe_text("{heading}", font_size=26, weight=BOLD, color=COLOR_ROSE, max_width=10.6)
        line{t_num} = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_ROSE)

        bad_{t_num} = VGroup(math_text("✗", font_size=26, color=COLOR_ROSE), safe_text("  {bad}", font_size=23, weight=BOLD, color=COLOR_ROSE, max_width=10.0)).arrange(RIGHT, buff=0.08)
        good_{t_num} = VGroup(math_text("✓", font_size=26, color=COLOR_EMERALD), safe_text("  {good}", font_size=23, weight=BOLD, color=COLOR_EMERALD, max_width=10.0)).arrange(RIGHT, buff=0.08)
        note_{t_num} = safe_text("• Lời khuyên: {note}", font_size=22, color=COLOR_TEXT_MUTED, max_width=10.4)

        c{t_num}_content = VGroup(c{t_num}_title, line{t_num}, bad_{t_num}, good_{t_num}, note_{t_num}).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        c{t_num}_content.move_to(c{t_num}_box.get_center())
        card{t_num} = VGroup(c{t_num}_box, c{t_num}_content)

        self.play(FadeIn(c{t_num}_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(c{t_num}_title, shift=DOWN*0.1), run_time=0.8)
        self.play(FadeIn(bad_{t_num}, shift=RIGHT*0.2), run_time=0.8)
        self.play(FadeIn(good_{t_num}, shift=RIGHT*0.2), run_time=0.8)
        self.play(FadeIn(note_{t_num}, shift=UP*0.1), run_time=0.6)

        rem_tr{t_num} = max(0.5, t_tr{t_num} - 3.8)
        self.wait(rem_tr{t_num})
        self.play(FadeOut(card{t_num}, shift=UP*0.3), run_time=0.8)
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

        timing_file = os.path.join(os.path.dirname(__file__), "audio", "timing_data.json")
        timing = {{}}
        if os.path.exists(timing_file):
            try:
                with open(timing_file, "r", encoding="utf-8") as f:
                    timing = json.load(f)
            except Exception:
                pass

        t_s5 = timing.get("scene5", 35.0)

        header = Text("PHẦN 5: SƠ ĐỒ TƯ DUY TỔNG KẾT & DẶN DÒ", font=FONT_FAMILY, font_size=32, weight=BOLD, color=COLOR_INDIGO)
        header_line = Line(LEFT * 5.6, RIGHT * 5.6, stroke_width=2, color=COLOR_INDIGO)
        header_group = VGroup(header, header_line).arrange(DOWN, buff=0.15).move_to([0, 3.25, 0])
        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)

        c_box = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.2, stroke_color=COLOR_INDIGO, stroke_width=2, fill_color=COLOR_CARD, fill_opacity=0.95).move_to([0, -0.4, 0])
        c_title = safe_text("TỔNG KẾT: {ltitle.upper()}", font_size=28, weight=BOLD, color=COLOR_INDIGO, max_width=10.6)
        c_line = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1, color=COLOR_INDIGO)
'''

    code += "        n_items = []\n"
    for n in nodes:
        safe_n = n.replace('"', '\\"')
        code += f'        n_items.append(safe_text("{safe_n}", font_size=22, color=COLOR_TEXT_MAIN, max_width=10.4))\n'

    code += "        hw_items = []\n"
    for h in hw:
        safe_h = h.replace('"', '\\"')
        code += f'        hw_items.append(safe_text("{safe_h}", font_size=22, color=COLOR_AMBER, max_width=10.4))\n'

    code += '''
        content = VGroup(c_title, c_line, *n_items, *hw_items).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        content.move_to(c_box.get_center())
        card = VGroup(c_box, content)

        self.play(FadeIn(c_box, scale=0.96), run_time=0.8)
        self.play(FadeIn(c_title, shift=DOWN*0.1), run_time=0.8)
        for nitm in n_items:
            self.play(FadeIn(nitm, shift=RIGHT*0.2), run_time=0.4)
        for hitm in hw_items:
            self.play(FadeIn(hitm, shift=RIGHT*0.2), run_time=0.4)

        rem_s5 = max(1.0, t_s5 - (1.6 + (len(n_items) + len(hw_items)) * 0.4))
        self.wait(rem_s5)

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
"""

import os
import sys
import glob
import shutil
import tempfile
import subprocess

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


def run():
    synced = []
    for sc in SCENE_DEFS:
        synced.append(render_scene(sc))
    out = concat_scenes(synced)
    print("DONE:", out)


if __name__ == "__main__":
    run()
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
