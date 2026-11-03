# -*- coding: utf-8 -*-
"""
BUILD MASTER DATABASE CHO TOÁN TIỂU HỌC (LỚP 4 & LỚP 5 - KNTT)
Tổng hợp toàn bộ:
1. Toán 5: 32 đề định kỳ + 180 đề theo bài = 212 đề
2. Toán 4: 32 đề định kỳ + đề theo bài học SGK
Xuất ra:
- tieuhocExamsData.js (thư mục gốc)
- dist/tieuhocExamsData.js
- src/data/tieuhocExamsData.js
- src/data/generated/tieuhocExamsData.js
- tieuhoc_exams_data.json
"""

import sys
import os
import json
import importlib
import re
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

from tieuhoc_curriculum_def import TIEUHOC_CURRICULUM

def build_all():
    print("=== BẮT ĐẦU TỔNG HỢP MASTER DATABASE TOÁN TIỂU HỌC (LỚP 1 ĐẾN 5) ===")
    all_exams = {}

    # =========================================================================
    # 1. TOÁN 1
    # =========================================================================
    try:
        import generator_th1_periodic
        e1 = generator_th1_periodic.get_th1_exams()
        all_exams.update(e1)
        print(f"-> [Toán 1] Nạp {len(e1)} đề định kỳ từ generator_th1_periodic")
    except Exception as e:
        print(f"Lỗi nạp Toán 1: {e}")

    # =========================================================================
    # 2. TOÁN 2
    # =========================================================================
    try:
        import generator_th2_periodic
        e2 = generator_th2_periodic.get_th2_exams()
        all_exams.update(e2)
        print(f"-> [Toán 2] Nạp {len(e2)} đề định kỳ từ generator_th2_periodic")
    except Exception as e:
        print(f"Lỗi nạp Toán 2: {e}")

    # =========================================================================
    # 3. TOÁN 3
    # =========================================================================
    try:
        import generator_th3_periodic
        e3 = generator_th3_periodic.get_th3_exams()
        all_exams.update(e3)
        print(f"-> [Toán 3] Nạp {len(e3)} đề định kỳ từ generator_th3_periodic")
    except Exception as e:
        print(f"Lỗi nạp Toán 3: {e}")

    # =========================================================================
    # 4. TOÁN 4
    # =========================================================================
    # a. Định kỳ Toán 4
    for term_code in ["gk1", "ck1", "gk2", "ck2"]:
        mod_name = f"generator_th4_{term_code}"
        try:
            mod = importlib.import_module(mod_name)
            func_name = f"get_th4_{term_code}_exams"
            if hasattr(mod, func_name):
                exams = getattr(mod, func_name)()
                all_exams.update(exams)
                print(f"-> [Toán 4] Nạp {len(exams)} đề từ {mod_name}")
        except Exception as e:
            pass

    # b. Theo bài SGK Toán 4 (Chủ đề 1 đến 13)
    for ch_idx in range(1, 14):
        mod_name = f"th4_ch{ch_idx}_builder"
        try:
            mod = importlib.import_module(mod_name)
            for fname in [f"get_all_ch{ch_idx}_exams", f"get_ch{ch_idx}_exams", "get_exams", "get_all_exams"]:
                if hasattr(mod, fname):
                    exams = getattr(mod, fname)()
                    all_exams.update(exams)
                    print(f"-> [Toán 4] Nạp {len(exams)} đề từ {mod_name}.{fname}()")
                    break
        except Exception as e:
            pass

    # =========================================================================
    # 5. TOÁN 5
    # =========================================================================
    # a. Định kỳ Toán 5
    for term_code in ["gk1", "ck1", "gk2", "ck2"]:
        mod_name = f"generator_th5_{term_code}"
        try:
            mod = importlib.import_module(mod_name)
            func_name = f"get_th5_{term_code}_exams"
            if hasattr(mod, func_name):
                exams = getattr(mod, func_name)()
                all_exams.update(exams)
                print(f"-> [Toán 5] Nạp {len(exams)} đề từ {mod_name}")
        except Exception as e:
            pass

    # b. Theo bài SGK Toán 5 (Chủ đề 1 đến 11)
    for ch_idx in range(1, 12):
        mod_name = f"th5_ch{ch_idx}_builder"
        try:
            mod = importlib.import_module(mod_name)
            for fname in [f"get_all_ch{ch_idx}_exams", f"get_ch{ch_idx}_exams", "get_exams", "get_all_exams"]:
                if hasattr(mod, fname):
                    exams = getattr(mod, fname)()
                    all_exams.update(exams)
                    print(f"-> [Toán 5] Nạp {len(exams)} đề từ {mod_name}.{fname}()")
                    break
        except Exception as e:
            pass

    print(f"\n=> TỔNG SỐ ĐỀ ĐÃ NẠP: {len(all_exams)}")

    # CHUẨN HÓA TIÊU ĐỀ THEO ĐÚNG RULE[user_global]
    # **Câu [Số]:** và **Bài [Số]:**
    for eid, ex in all_exams.items():
        # Chuẩn hóa Part 1
        for idx, q in enumerate(ex.get("part1", [])):
            q_num = q.get("id", idx + 1)
            q_text = q.get("question", "").strip()
            q_text = re.sub(r"^\*\*(Câu|Bài)\s*\d+[:\.]*\*\*\s*", "", q_text, flags=re.IGNORECASE)
            q_text = re.sub(r"^(Câu|Bài)\s*\d+[:\.]*\s*", "", q_text, flags=re.IGNORECASE)
            q["question"] = f"**Câu {q_num}:** {q_text}"

        # Chuẩn hóa Part 2
        for idx, q in enumerate(ex.get("part2", [])):
            q_num = q.get("id", idx + 1)
            q_text = q.get("question", "").strip()
            q_text = re.sub(r"^\*\*(Câu|Bài)\s*\d+[:\.]*\*\*\s*", "", q_text, flags=re.IGNORECASE)
            q_text = re.sub(r"^(Câu|Bài)\s*\d+[:\.]*\s*", "", q_text, flags=re.IGNORECASE)
            q["question"] = f"**Bài {q_num}:** {q_text}"

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Ghi file JSON
    json_path = os.path.join(BASE_DIR, "tieuhoc_exams_data.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_exams, f, ensure_ascii=False, indent=2)
    print(f"-> Đã ghi: {json_path}")

    # Ghi file JS cho trình duyệt
    js_content = f"""// DỮ LIỆU ĐỀ THI TOÁN TIỂU HỌC (LỚP 4 & LỚP 5 - KNTT)
// Cập nhật lúc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
// Bao gồm: Đề kiểm tra theo bài SGK & Đề kiểm tra định kỳ (GK1, CK1, GK2, CK2)

window.TIEUHOC_CURRICULUM = {json.dumps(TIEUHOC_CURRICULUM, ensure_ascii=False, indent=2)};

window.TIEUHOC_EXAMS_DATA = {json.dumps(all_exams, ensure_ascii=False)};
"""

    targets = [
        os.path.join(BASE_DIR, "tieuhocExamsData.js"),
        os.path.join(BASE_DIR, "dist", "tieuhocExamsData.js"),
        os.path.join(BASE_DIR, "src", "data", "tieuhocExamsData.js"),
        os.path.join(BASE_DIR, "src", "data", "generated", "tieuhocExamsData.js")
    ]

    for p in targets:
        os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"-> Đã ghi file JS: {p}")

    print("=== HOÀN TẤT BUILD MASTER DATABASE ===")
    return len(all_exams)

if __name__ == "__main__":
    build_all()
