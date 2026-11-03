# -*- coding: utf-8 -*-
"""
BUILD MASTER DATABASE CHO TOÁN TIỂU HỌC (LỚP 5 - KNTT)
Tổng hợp toàn bộ:
1. 4 Kỳ thi định kỳ: GK1 (8 đề), CK1 (8 đề), GK2 (8 đề), CK2 (8 đề) -> 32 đề
2. 11 Chủ đề bài học SGK (Bài 1 -> Bài 60, mỗi bài 3 đề) -> 180 đề
Xuất ra:
- tieuhocExamsData.js (thư mục gốc)
- src/data/tieuhocExamsData.js
- src/data/generated/tieuhocExamsData.js
- tieuhoc_exams_data.json
"""

import sys
import os
import json
import importlib
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

from tieuhoc_curriculum_def import TIEUHOC_CURRICULUM

def build_all():
    print("=== BẮT ĐẦU TỔNG HỢP MASTER DATABASE TOÁN 5 ===")
    all_exams = {}

    # 1. Thu thập Đề định kỳ GK1
    try:
        import generator_th5_gk1
        gk1 = generator_th5_gk1.get_th5_gk1_exams()
        all_exams.update(gk1)
        print(f"-> Nạp thành công {len(gk1)} đề Giữa học kì 1 (GK1)")
    except Exception as e:
        print(f"[!] Lỗi nạp GK1: {e}")

    # 2. Thu thập Đề định kỳ CK1
    try:
        import generator_th5_ck1
        ck1 = generator_th5_ck1.get_th5_ck1_exams()
        all_exams.update(ck1)
        print(f"-> Nạp thành công {len(ck1)} đề Cuối học kì 1 (CK1)")
    except Exception as e:
        print(f"[!] Lỗi nạp CK1: {e}")

    # 3. Thu thập Đề định kỳ GK2
    try:
        import generator_th5_gk2
        gk2 = generator_th5_gk2.get_th5_gk2_exams()
        all_exams.update(gk2)
        print(f"-> Nạp thành công {len(gk2)} đề Giữa học kì 2 (GK2)")
    except Exception as e:
        print(f"[!] Lỗi nạp GK2: {e}")

    # 4. Thu thập Đề định kỳ CK2
    try:
        import generator_th5_ck2
        ck2 = generator_th5_ck2.get_th5_ck2_exams()
        all_exams.update(ck2)
        print(f"-> Nạp thành công {len(ck2)} đề Cuối học kì 2 (CK2)")
    except Exception as e:
        print(f"[!] Lỗi nạp CK2: {e}")

    # 5. Thu thập Đề theo bài học SGK (Chủ đề 1 đến 11)
    for ch_idx in range(1, 12):
        builder_name = f"th5_ch{ch_idx}_builder"
        try:
            mod = importlib.import_module(builder_name)
            func_names = [
                f"get_all_ch{ch_idx}_exams",
                f"get_ch{ch_idx}_exams",
                f"get_th5_ch{ch_idx}_exams",
                "get_exams",
                "get_all_exams"
            ]
            loaded = False
            for fname in func_names:
                if hasattr(mod, fname):
                    ch_exams = getattr(mod, fname)()
                    all_exams.update(ch_exams)
                    print(f"-> Nạp thành công {len(ch_exams)} đề từ {builder_name}.{fname}()")
                    loaded = True
                    break
            if not loaded:
                print(f"[?] Không tìm thấy hàm xuất đề trong {builder_name}")
        except Exception as e:
            # Module chưa sẵn sàng hoặc đang tạo
            pass

    print(f"\n=> TỔNG SỐ ĐỀ ĐÃ NẠP: {len(all_exams)}")

    # CHUẨN HÓA TIÊU ĐỀ THEO ĐÚNG RULE[user_global]
    # **Câu [Số]:** và **Bài [Số]:**
    import re
    for eid, ex in all_exams.items():
        # Chuẩn hóa Part 1
        for idx, q in enumerate(ex.get("part1", [])):
            q_num = q.get("id", idx + 1)
            q_text = q.get("question", "").strip()
            # Xóa các định dạng sai nếu có
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
    js_content = f"""// DỮ LIỆU ĐỀ THI TOÁN TIỂU HỌC (LỚP 5 - KNTT)
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
