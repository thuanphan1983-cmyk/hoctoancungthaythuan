# -*- coding: utf-8 -*-
"""
Master Builder for Grade 10 Topics Data.
Compiles all 8 topics (360 questions) into:
- grade10TopicsData.js (for direct script tag loading)
- src/data/generated/grade10_topics_data.json (for JSON imports / API)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from cd1_builder import get_cd1_questions
from cd2_builder import get_cd2_questions
from cd3_builder import get_cd3_questions
from cd4_builder import get_cd4_questions
from cd5_builder import get_cd5_questions
from cd6_builder import get_cd6_questions
from cd7_builder import get_cd7_questions
from cd8_builder import get_cd8_questions

def build_all_topics():
    print("Collecting questions from 8 topic builders...")
    cd1 = get_cd1_questions()
    cd2 = get_cd2_questions()
    cd3 = get_cd3_questions()
    cd4 = get_cd4_questions()
    cd5 = get_cd5_questions()
    cd6 = get_cd6_questions()
    cd7 = get_cd7_questions()
    cd8 = get_cd8_questions()

    topics_meta = [
        {
            "id": "cd1",
            "title": "Chủ đề 1: Giải hệ phương trình bậc nhất 2 ẩn",
            "shortTitle": "CĐ 1: Hệ phương trình bậc nhất 2 ẩn",
            "icon": "⚡",
            "badge": "50 câu (40 VD + 10 VDC)",
            "description": "Giải hệ phương trình bậc nhất hai ẩn, hệ phương trình đặt ẩn phụ và giải bài toán bằng cách lập hệ phương trình (trong đó có 10 câu VDC khó).",
            "count": len(cd1),
            "questions": cd1
        },
        {
            "id": "cd2",
            "title": "Chủ đề 2: Rút gọn biểu thức chứa căn",
            "shortTitle": "CĐ 2: Rút gọn biểu thức chứa căn",
            "icon": "📐",
            "badge": "40 câu (20 VD + 20 VDC)",
            "description": "Rút gọn biểu thức chứa căn bậc hai có ẩn x dưới căn, tính giá trị, tìm x nguyên/thực để P nguyên, tìm GTLN/GTNN (chuẩn đề thi vào 10 Hà Tĩnh 2026).",
            "count": len(cd2),
            "questions": cd2
        },
        {
            "id": "cd3",
            "title": "Chủ đề 3: Hệ thức Vi-ét",
            "shortTitle": "CĐ 3: Hệ thức Vi-ét",
            "icon": "🎯",
            "badge": "50 câu tự luận",
            "description": "Không giải phương trình bậc hai, tính giá trị của biểu thức đối xứng và biểu thức liên quan đến 2 nghiệm x1, x2 của phương trình bậc 2 không chứa tham số.",
            "count": len(cd3),
            "questions": cd3
        },
        {
            "id": "cd4",
            "title": "Chủ đề 4: Xác suất",
            "shortTitle": "CĐ 4: Xác suất (Dạng liệt kê)",
            "icon": "🎲",
            "badge": "40 câu tự luận",
            "description": "Tính xác suất bằng phương pháp liệt kê không gian mẫu và các kết quả thuận lợi cho biến cố (gieo xúc xắc, tung đồng xu, rút thẻ, bốc bi).",
            "count": len(cd4),
            "questions": cd4
        },
        {
            "id": "cd5",
            "title": "Chủ đề 5: Giải bài toán bằng cách lập phương trình",
            "shortTitle": "CĐ 5: Lập PT bậc hai",
            "icon": "🚀",
            "badge": "50 câu (30 VD + 20 VDC)",
            "description": "Giải bài toán bằng cách đưa về phương trình bậc hai: chuyển động, năng suất, làm chung làm riêng, hình học và bài toán kinh tế thực tế.",
            "count": len(cd5),
            "questions": cd5
        },
        {
            "id": "cd6",
            "title": "Chủ đề 6: Hình học",
            "shortTitle": "CĐ 6: Hình học (Đường tròn & Tiếp tuyến)",
            "icon": "⭕",
            "badge": "50 bài toán (Mỗi câu 3 ý)",
            "description": "50 bài toán tự luận đường tròn, tiếp tuyến. Mỗi câu có 3 ý chuẩn đề thi: a) Chứng minh tứ giác nội tiếp có 2 góc vuông; b) Hệ thức tam giác đồng dạng; c) Thẳng hàng, vuông góc.",
            "count": len(cd6),
            "questions": cd6
        },
        {
            "id": "cd7",
            "title": "Chủ đề 7: Bài toán tối ưu hình học không gian",
            "shortTitle": "CĐ 7: Bài toán tối ưu",
            "icon": "📦",
            "badge": "40 câu VDC rất khó",
            "description": "Tối ưu hóa thể tích, diện tích hình hộp, hình nón, hình trụ, hình cầu (hình trụ nội tiếp hình nón, hình trụ nội tiếp hình cầu, hình nón nội tiếp hình cầu - mức VDC rất khó).",
            "count": len(cd7),
            "questions": cd7
        },
        {
            "id": "cd8",
            "title": "Chủ đề 8: Bài toán bất đẳng thức",
            "shortTitle": "CĐ 8: Bất đẳng thức & Cực trị",
            "icon": "🏆",
            "badge": "40 câu điểm 10 rất khó",
            "description": "Các bài toán chứng minh bất đẳng thức và tìm giá trị lớn nhất, giá trị nhỏ nhất chọn lọc dành cho câu phân hóa điểm 10 tuyển sinh vào lớp 10.",
            "count": len(cd8),
            "questions": cd8
        }
    ]

    total_q = sum(t["count"] for t in topics_meta)
    print(f"Total topics: {len(topics_meta)}, total questions: {total_q}")

    bundle = {
        "version": "2026.1",
        "title": "HỆ THỐNG CHUYÊN ĐỀ ÔN THI TUYỂN SINH VÀO LỚP 10 THPT",
        "author": "GV Phan Đình Thuấn",
        "totalTopics": len(topics_meta),
        "totalQuestions": total_q,
        "topics": topics_meta
    }

    # 1. Ghi ra grade10TopicsData.js
    js_content = f"// ==============================================================================\n" \
                 f"// DỮ LIỆU 8 CHUYÊN ĐỀ ÔN THI VÀO LỚP 10 MÔN TOÁN (360 CÂU TỰ LUẬN CHUẨN MA TRẬN)\n" \
                 f"// GV PHAN ĐÌNH THUẤN - HỆ THỐNG KIỂM TRA TOÁN THCS KẾT NỐI TRI THỨC\n" \
                 f"// ==============================================================================\n\n" \
                 f"window.GRADE10_TOPICS_DATA = {json.dumps(bundle, ensure_ascii=False, indent=2)};\n"
    
    with open("grade10TopicsData.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Exported grade10TopicsData.js successfully!")

    # 2. Ghi ra src/data/generated/grade10_topics_data.json
    out_dir = os.path.join("src", "data", "generated")
    os.makedirs(out_dir, exist_ok=True)
    json_path = os.path.join(out_dir, "grade10_topics_data.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)
    print(f"Exported {json_path} successfully!")

if __name__ == "__main__":
    build_all_topics()
