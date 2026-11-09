"""
GENERATOR ENGINE (ALIASED TO MASTER LESSON GENERATOR)
Bảo đảm tính tương thích ngược cho toàn bộ hệ thống
"""

import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

from master_lesson_generator import (
    HEADER_IMPORTS,
    build_scene1_code,
    build_scene2_code,
    build_scene3_code,
    build_scene4_code,
    build_scene5_code,
    build_concat_code,
    generate_lesson_package,
    get_mascot,
    fit_safe_box,
    wrap_text,
    safe_text,
    math_text
)
