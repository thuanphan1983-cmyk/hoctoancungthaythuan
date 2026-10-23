# -*- coding: utf-8 -*-
"""
==============================================================================
EXPORT TO PDF - BỘ BIÊN DỊCH VÀ XUẤT ĐỀ THI TOÁN THCS SANG LATEX VÀ PDF
Tự động quét thư mục src/data/generated/, đọc các file JSON đề thi,
lắp ráp nội dung vào template LaTeX chuẩn Bộ GD&ĐT 2025 (chuẩn font tiếng Việt,
hỗ trợ XeLaTeX / pdfLaTeX, đầy đủ amsmath, amssymb, khung bảng điểm chuẩn).
Sử dụng thư viện subprocess để biên dịch tự động sang file PDF trong src/data/pdf/
với cơ chế try-except chịu lỗi cao: lỗi đề nào bỏ qua và chạy tiếp đề khác.
==============================================================================
"""

import os
import sys
import re
import json
import shutil
import argparse
import subprocess
from datetime import datetime

# Đảm bảo hiển thị Unicode tiếng Việt trên Terminal Windows
sys.stdout.reconfigure(encoding='utf-8')

# Định nghĩa các đường dẫn mặc định
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, "src", "data")
GENERATED_DIR = os.path.join(DATA_DIR, "generated")
PDF_DIR = os.path.join(DATA_DIR, "pdf")
TEX_DIR = os.path.join(PDF_DIR, "tex")


# ==============================================================================
# 1. HÀM XỬ LÝ CHUỖI & ESCAPE LATEX AN TOÀN
# ==============================================================================
def escape_latex(text):
    """
    Escape các ký tự đặc biệt của LaTeX trong phần văn bản thông thường,
    nhưng GIỮ NGUYÊN các công thức toán học nằm trong $...$ hoặc $$...$$.
    """
    if not text:
        return ""
    
    text = str(text).strip()
    
    # Tách chuỗi theo các khối toán học $...$ hoặc $$...$$
    pattern = r'(\$\$.*?\$\$|\$.*?\$)'
    tokens = re.split(pattern, text, flags=re.DOTALL)
    
    result = []
    for token in tokens:
        if token.startswith('$') and token.endswith('$'):
            # Giữ nguyên khối toán học LaTeX
            result.append(token)
        else:
            # Thoát ký tự đặc biệt ngoài môi trường toán
            t = token
            # Thoát & (% # _ chỉ khi chưa được thoát bằng backslash)
            t = re.sub(r'(?<!\\)&', r'\&', t)
            t = re.sub(r'(?<!\\)%', r'\%', t)
            t = re.sub(r'(?<!\\)#', r'\#', t)
            t = re.sub(r'(?<!\\)_', r'\_', t)
            
            # Xử lý xuống dòng trong văn bản thông thường
            lines = t.split('\n')
            escaped_lines = []
            for line in lines:
                l = line.strip()
                if l:
                    escaped_lines.append(l)
            t = "\\par\\noindent ".join(escaped_lines)
            result.append(t)
            
    return "".join(result).strip()


def sanitize_filename(name):
    """Làm sạch tên file để tránh lỗi hệ điều hành"""
    name = re.sub(r'[\\/*?:"<>|]', '_', name)
    name = re.sub(r'\s+', '_', name).strip('_')
    return name


# ==============================================================================
# 2. XÁC ĐỊNH TRÌNH BIÊN DỊCH LATEX TRÊN HỆ THỐNG
# ==============================================================================
def find_latex_compiler(preferred_engine=None):
    """
    Tìm kiếm và xác định đường dẫn thực thi của xelatex / pdflatex / lualatex.
    Ưu tiên: xelatex (hỗ trợ Unicode tiếng Việt tốt nhất) > pdflatex > lualatex.
    """
    candidates = []
    if preferred_engine and preferred_engine != "auto":
        candidates.append(preferred_engine)
    else:
        candidates = ["xelatex", "pdflatex", "lualatex"]

    # 1. Kiểm tra qua PATH hệ thống
    for cand in candidates:
        cmd_path = shutil.which(cand)
        if cmd_path:
            return cand, cmd_path

    # 2. Kiểm tra các thư mục cài đặt tiêu chuẩn phổ biến trên Windows
    common_win_paths = [
        # MiKTeX standard paths
        r"C:\Program Files\MiKTeX\miktex\bin\x64",
        r"C:\Program Files (x86)\MiKTeX\miktex\bin",
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64"),
        os.path.expandvars(r"%USERPROFILE%\AppData\Local\Programs\MiKTeX\miktex\bin\x64"),
        # TeX Live standard paths
        r"C:\texlive\2026\bin\windows",
        r"C:\texlive\2025\bin\windows",
        r"C:\texlive\2024\bin\windows",
        r"C:\texlive\2023\bin\windows",
        r"C:\texlive\2022\bin\win32",
    ]

    for cand in candidates:
        exe_name = f"{cand}.exe"
        for base in common_win_paths:
            full_path = os.path.join(base, exe_name)
            if os.path.isfile(full_path):
                return cand, full_path

    return None, None


# ==============================================================================
# 3. LẮP RÁP NỘI DUNG VÀO TEMPLATE LATEX CHUẨN MA TRẬN 2025
# ==============================================================================
def generate_latex_code(exam_id, exam_data, grade=None):
    """
    Tạo mã nguồn file .tex hoàn chỉnh cho một đề thi.
    Đầy đủ cấu trúc: Tiêu đề hành chính, Phần I, Phần II, Phần III, Phần IV,
    và trang Hướng dẫn chấm / Đáp án chi tiết.
    """
    title = exam_data.get("title", f"Đề kiểm tra Toán - Mã đề: {exam_id}")
    
    # Xác định khối lớp từ đề bài hoặc tham số
    grade_str = grade or "8"
    if "Toán 6" in title or "grade6" in exam_id or "c1_6" in exam_id or "c2_6" in exam_id or "c3_6" in exam_id:
        grade_str = "6"
    elif "Toán 7" in title or "grade7" in exam_id or "c1_7" in exam_id or "c2_7" in exam_id:
        grade_str = "7"
    elif "Toán 8" in title or "grade8" in exam_id or "c1_8" in exam_id or "c2_8" in exam_id:
        grade_str = "8"
    elif "Toán 9" in title or "grade9" in exam_id or "c1_9" in exam_id or "c2_9" in exam_id:
        grade_str = "9"

    # Xác định thời gian làm bài
    is_long_exam = "cuối chương" in title.lower() or "học kì" in title.lower() or "chương" in title.lower()
    duration = "90 phút" if is_long_exam else "45 phút"

    # Phân loại mức độ đề
    level_tag = "ĐỀ THI ĐỊNH KỲ"
    if "Cơ bản" in title or "test1" in exam_id:
        level_tag = "MỨC ĐỘ 1: CƠ BẢN"
    elif "Khá" in title or "test2" in exam_id:
        level_tag = "MỨC ĐỘ 2: KHÁ"
    elif "Nâng cao" in title or "test3" in exam_id:
        level_tag = "MỨC ĐỘ 3: NÂNG CAO"

    escaped_title = escape_latex(title)

    # Bắt đầu xây dựng văn bản LaTeX
    tex = []
    tex.append(r"""\documentclass[11pt,a4paper]{article}

% --- THIẾT LẬP LỀ TRANG & KHỔ GIẤY ---
\usepackage[top=1.8cm,bottom=1.8cm,left=1.8cm,right=1.8cm]{geometry}

% --- HỖ TRỢ ĐA DẠNG TRÌNH BIÊN DỊCH (XeLaTeX / pdfLaTeX / LuaLaTeX) ---
\usepackage{iftex}
\ifXeTeX
  \usepackage{fontspec}
  \usepackage[vietnamese]{babel}
  \defaultfontfeatures{Ligatures=TeX}
\else
  \usepackage[utf8]{inputenc}
  \usepackage[T5,T1]{fontenc}
  \usepackage[vietnamese]{babel}
  \usepackage{mathptmx}
\fi

% --- CÁC GÓI TOÁN HỌC CHUẨN AMS ---
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{mathtools}
\usepackage{bm}

% --- BẢNG BIỂU, DANH SÁCH & TRANG TRÍ ---
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{enumitem}
\usepackage{multicol}
\usepackage{fancyhdr}
\usepackage{xcolor}

% --- THIẾT LẬP HEADER & FOOTER ---
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\lfoot{\textit{\small Bộ đề kiểm tra Toán THCS KNTT - Mã: """ + escape_latex(exam_id) + r"""}}
\rfoot{\textit{\small Trang \thepage}}

\begin{document}

% ==============================================================================
% PHẦN ĐẦU ĐỀ THI (HEADER TIÊU CHUẨN BỘ GD&ĐT)
% ==============================================================================
\noindent
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}lr@{}}
\textbf{SỞ GD\&ĐT ........................} & \textbf{ĐỀ KIỂM TRA ĐỊNH KỲ NĂM HỌC 2025 - 2026} \\
\textbf{TRƯỜNG THCS ........................} & \textbf{Môn: TOÁN - LỚP """ + grade_str + r"""} \\
\textit{(Đề thi chuẩn ma trận 2025)} & \textit{Thời gian làm bài: """ + duration + r""" (không kể giao đề)}
\end{tabular*}

\vspace{6pt}
\begin{center}
{\Large\bfseries """ + escaped_title + r"""}\\[4pt]
{\bfseries [ """ + level_tag + r""" - Mã đề: \texttt{""" + escape_latex(exam_id) + r"""} ]}
\end{center}

\vspace{4pt}
\noindent
\rule{\textwidth}{0.8pt}\\[3pt]
Họ và tên thí sinh: \dotfill\ Lớp: \dots\dots\ SBD: \dots\dots\\[-6pt]
\rule{\textwidth}{0.8pt}

\vspace{10pt}
""")

    # ==========================================================================
    # PHẦN I: TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (3.0 ĐIỂM - 12 CÂU)
    # ==========================================================================
    part1 = exam_data.get("part1", [])
    tex.append(r"""
% ==============================================================================
% PHẦN I: TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN (3,0 ĐIỂM)
% ==============================================================================
\noindent
\textbf{\large PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (3,0 điểm)}\\
\textit{\small Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án đúng nhất.}
\vspace{6pt}
""")

    for q in part1:
        q_id = q.get("id", "")
        level = q.get("level", "")
        level_str = f" [{level}]" if level else ""
        q_text = escape_latex(q.get("question", ""))
        options = q.get("options", [])
        
        tex.append(f"\\noindent\\textbf{{Câu {q_id}.}}{level_str} {q_text}\\par\\vspace{{2pt}}\n")

        if len(options) == 4:
            opt_a = escape_latex(options[0])
            opt_b = escape_latex(options[1])
            opt_c = escape_latex(options[2])
            opt_d = escape_latex(options[3])

            raw_len_max = max(len(str(o)) for o in options)
            if raw_len_max <= 18:
                # 4 đáp án trên 1 dòng
                tex.append(
                    r"\noindent\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}llll@{}}" + "\n"
                    f"\\textbf{{A.}} {opt_a} & \\textbf{{B.}} {opt_b} & \\textbf{{C.}} {opt_c} & \\textbf{{D.}} {opt_d}\n"
                    r"\end{tabular*}\par\vspace{5pt}" + "\n\n"
                )
            elif raw_len_max <= 42:
                # 2 cột x 2 dòng
                tex.append(
                    r"\noindent\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}p{0.48\textwidth}p{0.48\textwidth}@{}}" + "\n"
                    f"\\textbf{{A.}} {opt_a} & \\textbf{{B.}} {opt_b} \\\\\n"
                    f"\\textbf{{C.}} {opt_c} & \\textbf{{D.}} {opt_d}\n"
                    r"\end{tabular*}\par\vspace{5pt}" + "\n\n"
                )
            else:
                # 4 dòng riêng biệt
                tex.append(
                    f"\\noindent\\textbf{{A.}} {opt_a}\\par\\vspace{{1pt}}\n"
                    f"\\noindent\\textbf{{B.}} {opt_b}\\par\\vspace{{1pt}}\n"
                    f"\\noindent\\textbf{{C.}} {opt_c}\\par\\vspace{{1pt}}\n"
                    f"\\noindent\\textbf{{D.}} {opt_d}\\par\\vspace{{5pt}}\n\n"
                )
        else:
            for idx, opt in enumerate(options):
                opt_letter = chr(65 + idx)
                tex.append(f"\\noindent\\textbf{{{opt_letter}.}} {escape_latex(opt)}\\par\\vspace{{1pt}}\n")
            tex.append("\\vspace{5pt}\n\n")

    # ==========================================================================
    # PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI (2.0 ĐIỂM - 2 CÂU)
    # ==========================================================================
    part2 = exam_data.get("part2", [])
    tex.append(r"""
% ==============================================================================
% PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI (2,0 ĐIỂM)
% ==============================================================================
\vspace{6pt}
\noindent
\textbf{\large PHẦN II. Câu trắc nghiệm đúng sai (2,0 điểm)}\\
\textit{\small Thí sinh trả lời từ câu 1 đến câu 2. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}\\
\textit{\small (Quy tắc tính điểm: Đúng 1 ý được 0,1đ; đúng 2 ý được 0,25đ; đúng 3 ý được 0,5đ; đúng 4 ý được 1,0đ).}
\vspace{6pt}
""")

    for q in part2:
        q_id = q.get("id", "")
        stem = escape_latex(q.get("stem", ""))
        tex.append(f"\\noindent\\textbf{{Câu {q_id}.}} {stem}\\par\\vspace{{2pt}}\n")
        tex.append(r"\begin{enumerate}[label=\textbf{\alph*)}, leftmargin=1.2cm, itemsep=2pt, topsep=2pt]" + "\n")
        
        for st in q.get("statements", []):
            st_text = escape_latex(st.get("text", ""))
            st_level = st.get("level", "")
            # Đảm bảo có khoảng trắng trước ngoặc vuông để LaTeX không nhầm với nhãn tùy chọn của \item
            level_tag = f" \\textnormal{{[{st_level}]}}" if st_level else ""
            tex.append(f"  \\item{level_tag} {st_text}\n")
        
        tex.append(r"\end{enumerate}" + "\n\\vspace{6pt}\n\n")

    # ==========================================================================
    # PHẦN III: TRẮC NGHIỆM TRẢ LỜI NGẮN (2.0 ĐIỂM - 4 CÂU)
    # ==========================================================================
    part3 = exam_data.get("part3", [])
    tex.append(r"""
% ==============================================================================
% PHẦN III: TRẮC NGHIỆM TRẢ LỜI NGẮN (2,0 ĐIỂM)
% ==============================================================================
\vspace{6pt}
\noindent
\textbf{\large PHẦN III. Câu trắc nghiệm trả lời ngắn (2,0 điểm)}\\
\textit{\small Thí sinh trả lời từ câu 1 đến câu 4. Mỗi câu trả lời đúng thí sinh được 0,5 điểm.}
\vspace{6pt}
""")

    for q in part3:
        q_id = q.get("id", "")
        level = q.get("level", "")
        level_str = f" [{level}]" if level else ""
        q_text = escape_latex(q.get("question", ""))
        tex.append(
            f"\\noindent\\textbf{{Câu {q_id}.}}{level_str} {q_text}\\par\\vspace{{2pt}}\n"
            r"\noindent\textit{Đáp số:} \dotfill\par\vspace{6pt}" + "\n\n"
        )

    # ==========================================================================
    # PHẦN IV: TỰ LUẬN (3.0 ĐIỂM - 3 CÂU)
    # ==========================================================================
    part4 = exam_data.get("part4", [])
    tex.append(r"""
% ==============================================================================
% PHẦN IV: TỰ LUẬN (3,0 ĐIỂM)
% ==============================================================================
\vspace{6pt}
\noindent
\textbf{\large PHẦN IV. Tự luận (3,0 điểm)}\\
\textit{\small Thí sinh trình bày chi tiết các bước giải từ câu 1 đến câu 3 vào giấy làm bài.}
\vspace{6pt}
""")

    for q in part4:
        q_id = q.get("id", "")
        level = q.get("level", "")
        level_str = f" [{level}]" if level else ""
        q_text = escape_latex(q.get("question", ""))
        tex.append(
            f"\\noindent\\textbf{{Bài {q_id} (1,0 điểm).}}{level_str} {q_text}\\par\\vspace{{8pt}}\n\n"
        )

    # Dòng kết thúc đề thi
    tex.append(r"""
\begin{center}
\textbf{---------- HẾT ----------}\\
\textit{\small Cán bộ coi thi không giải thích gì thêm.}
\end{center}
""")

    # ==========================================================================
    # PHẦN ĐÁP ÁN VÀ HƯỚNG DẪN CHẤM CHI TIẾT
    # ==========================================================================
    tex.append(r"""
\newpage
% ==============================================================================
% HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN CHI TIẾT
% ==============================================================================
\begin{center}
{\Large\bfseries HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN CHI TIẾT}\\[4pt]
{\large\bfseries """ + escaped_title + r"""}\\[2pt]
{\bfseries Mã đề: \texttt{""" + escape_latex(exam_id) + r"""}}
\end{center}

\vspace{10pt}
\noindent\textbf{\large 1. ĐÁP ÁN PHẦN I: TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN (3,0 điểm)}
\vspace{4pt}
""")

    # Bảng đáp án Phần I
    if part1:
        tex.append(r"\begin{center}" + "\n")
        tex.append(r"\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|}" + "\n")
        tex.append(r"\hline" + "\n")
        header_q = " & ".join([f"\\textbf{{{q.get('id', i+1)}}}" for i, q in enumerate(part1)])
        tex.append(f"{header_q} \\\\\n\\hline\n")
        answers_p1 = []
        for q in part1:
            corr = q.get("correct", 0)
            if isinstance(corr, int) and 0 <= corr < 4:
                answers_p1.append(chr(65 + corr))
            elif str(corr).upper() in ["A", "B", "C", "D"]:
                answers_p1.append(str(corr).upper())
            else:
                answers_p1.append(str(corr))
        header_ans = " & ".join([f"\\textbf{{{ans}}}" for ans in answers_p1])
        tex.append(f"{header_ans} \\\\\n\\hline\n")
        tex.append(r"\end{tabular}" + "\n")
        tex.append(r"\end{center}" + "\n\\vspace{6pt}\n\n")

    # Bảng đáp án Phần II
    tex.append(r"""
\noindent\textbf{\large 2. ĐÁP ÁN PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI (2,0 điểm)}
\vspace{4pt}
""")
    if part2:
        tex.append(r"\begin{center}" + "\n")
        tex.append(r"\begin{tabular}{|c|c|c|c|c|}" + "\n")
        tex.append(r"\hline" + "\n")
        tex.append(r"\textbf{Câu hỏi} & \textbf{Ý a)} & \textbf{Ý b)} & \textbf{Ý c)} & \textbf{Ý d)} \\" + "\n")
        tex.append(r"\hline" + "\n")
        
        for q in part2:
            q_id = q.get("id", "")
            statements = q.get("statements", [])
            row_items = [f"\\textbf{{Câu {q_id}}}"]
            for st in statements:
                corr = st.get("correct")
                if corr is True or str(corr).lower() in ["true", "đ", "đúng", "1"]:
                    row_items.append(r"\textbf{Đúng}")
                else:
                    row_items.append(r"\textbf{Sai}")
            while len(row_items) < 5:
                row_items.append("-")
            tex.append(" & ".join(row_items) + " \\\\\n\\hline\n")
        tex.append(r"\end{tabular}" + "\n")
        tex.append(r"\end{center}" + "\n\\vspace{6pt}\n\n")

    # Bảng đáp án Phần III
    tex.append(r"""
\noindent\textbf{\large 3. ĐÁP ÁN PHẦN III: TRẢ LỜI NGẮN (2,0 điểm)}
\vspace{4pt}
""")
    if part3:
        tex.append(r"\begin{center}" + "\n")
        tex.append(r"\begin{tabular}{|c|m{11cm}|c|}" + "\n")
        tex.append(r"\hline" + "\n")
        tex.append(r"\textbf{Câu} & \textbf{Tóm tắt yêu cầu} & \textbf{Đáp số chính xác} \\" + "\n")
        tex.append(r"\hline" + "\n")
        for q in part3:
            q_id = q.get("id", "")
            q_short = escape_latex(q.get("question", "")[:80])
            if len(q.get("question", "")) > 80:
                q_short += "..."
            ans_str = escape_latex(q.get("answer", ""))
            tex.append(f"\\textbf{{Câu {q_id}}} & {q_short} & \\textbf{{{ans_str}}} \\\\\n\\hline\n")
        tex.append(r"\end{tabular}" + "\n")
        tex.append(r"\end{center}" + "\n\\vspace{6pt}\n\n")

    # Lời giải chi tiết & Biểu điểm Phần IV
    tex.append(r"""
\noindent\textbf{\large 4. LỜI GIẢI CHI TIẾT VÀ BIỂU ĐIỂM TỰ LUẬN (3,0 điểm)}
\vspace{4pt}
""")
    if part4:
        for q in part4:
            q_id = q.get("id", "")
            rubric_text = escape_latex(q.get("rubric", "Thực hiện theo các bước chuẩn bài toán."))
            tex.append(
                f"\\noindent\\textbf{{\\underline{{Bài {q_id} (1,0 điểm):}}}}\\par\\vspace{{3pt}}\n"
                f"{rubric_text}\\par\\vspace{{8pt}}\n\n"
            )

    tex.append(r"\end{document}" + "\n")
    return "".join(tex)


# ==============================================================================
# 4. HÀM BIÊN DỊCH BẰNG SUBPROCESS VỚI TRY-EXCEPT VỮNG CHẮC
# ==============================================================================
def compile_latex_to_pdf(tex_filepath, output_pdf_dir, compiler_cmd):
    """
    Sử dụng subprocess để biên dịch file .tex thành file .pdf.
    Bao bọc hoàn toàn trong try-except, tự động phân tích và bắt lỗi nếu quá trình biên dịch thất bại.
    """
    tex_dir = os.path.dirname(tex_filepath)
    tex_filename = os.path.basename(tex_filepath)
    base_name = os.path.splitext(tex_filename)[0]
    expected_pdf = os.path.join(output_pdf_dir, f"{base_name}.pdf")

    # Tham số dòng lệnh biên dịch chuẩn
    cmd = [
        compiler_cmd,
        "-interaction=nonstopmode",
        f"-output-directory={output_pdf_dir}",
        tex_filepath
    ]

    try:
        proc = subprocess.run(
            cmd,
            cwd=tex_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60,
            encoding='utf-8',
            errors='replace'
        )

        if proc.returncode == 0 and os.path.exists(expected_pdf):
            return True, expected_pdf, None
        else:
            # Thu thập thông tin lỗi từ log hoặc stdout
            log_file = os.path.join(output_pdf_dir, f"{base_name}.log")
            error_snippet = ""
            if os.path.exists(log_file):
                try:
                    with open(log_file, "r", encoding="utf-8", errors="replace") as f:
                        log_lines = f.readlines()
                    error_lines = [l for l in log_lines if l.startswith("!") or "Fatal error" in l]
                    error_snippet = "".join(error_lines[:6])
                except Exception:
                    pass
            if not error_snippet:
                error_snippet = proc.stdout[-500:] if proc.stdout else proc.stderr[-500:]
            return False, None, error_snippet

    except subprocess.TimeoutExpired:
        return False, None, "Quá thời gian biên dịch (Timeout > 60s)"
    except Exception as e:
        return False, None, str(e)


def clean_aux_files(output_dir, base_name):
    """Dọn dẹp các file phụ sinh ra trong quá trình biên dịch LaTeX"""
    aux_extensions = [".aux", ".log", ".out", ".toc", ".synctex.gz"]
    for ext in aux_extensions:
        aux_file = os.path.join(output_dir, f"{base_name}{ext}")
        if os.path.exists(aux_file):
            try:
                os.remove(aux_file)
            except Exception:
                pass


# ==============================================================================
# 5. BỘ QUÉT VÀ TRÍCH XUẤT ĐỀ THI TỪ CÁC FILE JSON TRONG SRC/DATA/GENERATED
# ==============================================================================
def discover_exams(generated_dir):
    """
    Quét toàn bộ các file JSON trong thư mục generated_dir
    Hỗ trợ linh hoạt cả:
    1. Chapter container JSON: { grade, chapterId, exams: { key: exam_obj } }
    2. Flat dictionary: { key: exam_obj }
    3. Single exam object: { title, part1, part2, ... }
    """
    discovered = {}
    if not os.path.exists(generated_dir):
        return discovered

    json_files = [f for f in os.listdir(generated_dir) if f.endswith(".json") and f != "manifest.json"]

    for fname in json_files:
        fpath = os.path.join(generated_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, dict):
                # Trường hợp 1: Có trường "exams"
                if "exams" in data and isinstance(data["exams"], dict):
                    grade = data.get("grade")
                    for k, v in data["exams"].items():
                        if isinstance(v, dict) and "part1" in v:
                            discovered[k] = {
                                "exam_id": k,
                                "grade": grade,
                                "source_file": fname,
                                "data": v
                            }
                # Trường hợp 2: Dictionary chứa các exam key trực tiếp
                elif any(isinstance(v, dict) and "part1" in v for v in data.values()):
                    for k, v in data.items():
                        if isinstance(v, dict) and "part1" in v:
                            discovered[k] = {
                                "exam_id": k,
                                "grade": None,
                                "source_file": fname,
                                "data": v
                            }
                # Trường hợp 3: Bản thân JSON là 1 exam duy nhất
                elif "part1" in data:
                    key = os.path.splitext(fname)[0]
                    discovered[key] = {
                        "exam_id": key,
                        "grade": None,
                        "source_file": fname,
                        "data": data
                    }

        except Exception as e:
            print(f"⚠️ Không đọc được file {fname}: {e}")

    return discovered


# ==============================================================================
# 6. ĐIỀU PHỐI VÀ THỰC THI CHÍNH (MAIN ORCHESTRATOR)
# ==============================================================================
def run_export(args):
    print("=" * 80)
    print("      🚀 HỆ THỐNG XUẤT ĐỀ THI TOÁN THCS SANG TEMPLATE LATEX VÀ PDF 🚀      ")
    print("=" * 80)

    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)
    tex_dir = os.path.abspath(args.tex_dir) if args.tex_dir else os.path.join(output_dir, "tex")

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(tex_dir, exist_ok=True)

    print(f"📂 Thư mục quét đề thi (JSON) : {input_dir}")
    print(f"📄 Thư mục lưu mã nguồn (.tex) : {tex_dir}")
    print(f"📕 Thư mục lưu file (.pdf)     : {output_dir}")

    # Tìm trình biên dịch
    engine_name, compiler_cmd = find_latex_compiler(args.engine)
    if compiler_cmd:
        print(f"⚡ Trình biên dịch LaTeX tìm thấy: [{engine_name.upper()}] tại: {compiler_cmd}")
    else:
        print("⚠️ [CẢNH BÁO] Không tìm thấy xelatex / pdflatex / lualatex trong hệ thống PATH!")
        print("   -> Kịch bản vẫn sẽ tự động tạo và lưu đầy đủ các file .tex chuẩn mực.")
        print("   -> Bạn có thể biên dịch chúng sau khi cài đặt MiKTeX hoặc TeX Live.")

    # Quét danh sách đề thi
    exams = discover_exams(input_dir)
    if not exams:
        print(f"\n❌ Không tìm thấy đề thi hợp lệ nào trong {input_dir}!")
        print("   Hãy chắc chắn rằng đã chạy auto_exam_generator.py để sinh các file JSON trước.")
        return

    print(f"\n✨ Đã tìm thấy {len(exams)} đề thi sẵn sàng xử lý.\n" + "-" * 80)

    # Thống kê tiến độ
    total = len(exams)
    success_tex = 0
    success_pdf = 0
    failed_compile = 0
    summary_report = []

    for idx, (exam_key, exam_info) in enumerate(exams.items(), 1):
        if args.exam_id and args.exam_id != exam_key:
            continue

        exam_data = exam_info["data"]
        grade = exam_info["grade"]
        title = exam_data.get("title", exam_key)
        
        print(f"\n[{idx}/{total}] 📝 Đang xử lý: {exam_key}")
        print(f"       Tiêu đề: {title[:70]}...")

        # 1. Tạo file .tex
        tex_filename = f"{exam_key}.tex"
        tex_filepath = os.path.join(tex_dir, tex_filename)

        try:
            tex_code = generate_latex_code(exam_key, exam_data, grade)
            with open(tex_filepath, "w", encoding="utf-8") as f:
                f.write(tex_code)
            success_tex += 1
            print(f"       ✅ Đã xuất mã nguồn LaTeX: {tex_filename}")
        except Exception as e:
            print(f"       ❌ Lỗi khi sinh mã LaTeX: {e}")
            summary_report.append({
                "exam_key": exam_key,
                "status": "TEX_FAILED",
                "error": str(e)
            })
            continue

        # 2. Biên dịch sang .pdf (nếu có trình biên dịch và không dùng cờ --tex-only)
        if args.tex_only or not compiler_cmd:
            summary_report.append({
                "exam_key": exam_key,
                "status": "TEX_GENERATED",
                "tex_path": tex_filepath
            })
            continue

        # Tiến hành biên dịch với try-except an toàn
        try:
            print(f"       ⚙️ Đang biên dịch PDF với {engine_name}...")
            ok, pdf_path, err_msg = compile_latex_to_pdf(tex_filepath, output_dir, compiler_cmd)

            if ok:
                success_pdf += 1
                print(f"       🎉 [THÀNH CÔNG] File PDF đã tạo: {os.path.basename(pdf_path)}")
                if args.clean_aux:
                    clean_aux_files(output_dir, exam_key)
                summary_report.append({
                    "exam_key": exam_key,
                    "status": "PDF_SUCCESS",
                    "pdf_path": pdf_path,
                    "tex_path": tex_filepath
                })
            else:
                failed_compile += 1
                print(f"       ⚠️ [BỎ QUA DO LỖI BIÊN DỊCH] {exam_key}: {err_msg[:120]}...")
                summary_report.append({
                    "exam_key": exam_key,
                    "status": "COMPILE_FAILED",
                    "error": err_msg,
                    "tex_path": tex_filepath
                })

        except Exception as exc:
            # Cơ chế chống văng lỗi tuyệt đối
            failed_compile += 1
            print(f"       ⚠️ [NGOẠI LỆ BIÊN DỊCH] Bỏ qua đề này và tiếp tục: {exc}")
            summary_report.append({
                "exam_key": exam_key,
                "status": "COMPILE_EXCEPTION",
                "error": str(exc),
                "tex_path": tex_filepath
            })

    # 3. Ghi báo cáo tổng hợp
    report_file = os.path.join(output_dir, "export_summary.json")
    try:
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_exams": total,
                "tex_generated": success_tex,
                "pdf_compiled": success_pdf,
                "compile_failed": failed_compile,
                "details": summary_report
            }, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    print("\n" + "=" * 80)
    print("                     📊 KẾT QUẢ TỔNG KẾT XUẤT ĐỀ THI 📊                     ")
    print("=" * 80)
    print(f"  • Tổng số đề thi đã quét          : {total}")
    print(f"  • Số file LaTeX (.tex) tạo thành công: {success_tex}")
    if compiler_cmd and not args.tex_only:
        print(f"  • Số file PDF (.pdf) biên dịch thành công: {success_pdf}")
        print(f"  • Số đề bị lỗi biên dịch (đã bỏ qua)  : {failed_compile}")
    else:
        print("  • Lưu ý: Chế độ xuất mã nguồn .tex hoàn tất (chưa biên dịch PDF do chưa có compiler).")
    print(f"  • Xem chi tiết file log tổng kết tại : {report_file}")
    print("=" * 80)


# ==============================================================================
# 7. ĐIỂM VÀO DÒNG LỆNH (CLI ENTRYPOINT)
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(
        description="Xuất ngân hàng đề kiểm tra Toán THCS từ JSON sang định dạng LaTeX chuẩn và tự động biên dịch sang PDF."
    )
    parser.add_argument(
        "--input-dir",
        default=GENERATED_DIR,
        help="Thư mục chứa các file JSON đề thi (mặc định: src/data/generated)"
    )
    parser.add_argument(
        "--output-dir",
        default=PDF_DIR,
        help="Thư mục lưu các file PDF xuất ra (mặc định: src/data/pdf)"
    )
    parser.add_argument(
        "--tex-dir",
        default=None,
        help="Thư mục lưu các file .tex (mặc định: src/data/pdf/tex)"
    )
    parser.add_argument(
        "--engine",
        default="auto",
        choices=["auto", "xelatex", "pdflatex", "lualatex"],
        help="Trình biên dịch LaTeX mong muốn (auto, xelatex, pdflatex, lualatex)"
    )
    parser.add_argument(
        "--exam-id",
        default=None,
        help="Chỉ xuất một mã đề cụ thể (ví dụ: --exam-id c1_6_bai1_test1)"
    )
    parser.add_argument(
        "--tex-only",
        action="store_true",
        help="Chỉ tạo file .tex, bỏ qua bước biên dịch sang PDF"
    )
    parser.add_argument(
        "--clean-aux",
        action="store_true",
        default=True,
        help="Tự động xóa các file tạm (.aux, .log, .out) sau khi biên dịch PDF thành công"
    )

    args = parser.parse_args()
    run_export(args)


if __name__ == "__main__":
    main()
