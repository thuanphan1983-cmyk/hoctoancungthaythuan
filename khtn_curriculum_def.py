# -*- coding: utf-8 -*-
"""
KHTN Curriculum Definition (Bộ sách Kết nối tri thức với cuộc sống)
Lớp 7, 8, 9 - Phân môn Hóa học & Vật lý
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

KHTN_CURRICULUM = {
    "chemistry": {
        "id": "chemistry",
        "name": "Môn Hóa học",
        "icon": "🧪",
        "grades": {
            "7": {
                "title": "Hóa học 7",
                "chapters": [
                    {
                        "id": "chem7_c1",
                        "title": "Chương I: Nguyên tử - Sơ lược bảng tuần hoàn",
                        "lessons": [
                            {"id": "chem7_c1_b2", "num": 2, "name": "Bài 2: Nguyên tử", "isReview": False},
                            {"id": "chem7_c1_b3", "num": 3, "name": "Bài 3: Nguyên tố hóa học", "isReview": False},
                            {"id": "chem7_c1_b4", "num": 4, "name": "Bài 4: Sơ lược về bảng tuần hoàn các nguyên tố hóa học", "isReview": False},
                            {"id": "chem7_c1_rev", "num": 0, "name": "Ôn tập cuối Chương I", "isReview": True}
                        ]
                    },
                    {
                        "id": "chem7_c2",
                        "title": "Chương II: Phân tử - Liên kết hóa học",
                        "lessons": [
                            {"id": "chem7_c2_b5", "num": 5, "name": "Bài 5: Phân tử - Đơn chất - Hợp chất", "isReview": False},
                            {"id": "chem7_c2_b6", "num": 6, "name": "Bài 6: Giới thiệu về liên kết hóa học", "isReview": False},
                            {"id": "chem7_c2_b7", "num": 7, "name": "Bài 7: Hóa trị và công thức hóa học", "isReview": False},
                            {"id": "chem7_c2_rev", "num": 0, "name": "Ôn tập cuối Chương II", "isReview": True}
                        ]
                    }
                ]
            },
            "8": {
                "title": "Hóa học 8",
                "chapters": [
                    {
                        "id": "chem8_c1",
                        "title": "Chương I: Phản ứng hóa học",
                        "lessons": [
                            {"id": "chem8_c1_b2", "num": 2, "name": "Bài 2: Biến đổi vật lí và biến đổi hóa học", "isReview": False},
                            {"id": "chem8_c1_b3", "num": 3, "name": "Bài 3: Phản ứng hóa học", "isReview": False},
                            {"id": "chem8_c1_b4", "num": 4, "name": "Bài 4: Định luật bảo toàn khối lượng và phương trình hóa học", "isReview": False},
                            {"id": "chem8_c1_b5", "num": 5, "name": "Bài 5: Mol và tỉ khối của chất khí", "isReview": False},
                            {"id": "chem8_c1_b6", "num": 6, "name": "Bài 6: Nồng độ dung dịch", "isReview": False},
                            {"id": "chem8_c1_b7", "num": 7, "name": "Bài 7: Tốc độ phản ứng và chất xúc tác", "isReview": False},
                            {"id": "chem8_c1_rev", "num": 0, "name": "Ôn tập cuối Chương I", "isReview": True}
                        ]
                    },
                    {
                        "id": "chem8_c2",
                        "title": "Chương II: Một số hợp chất thông dụng",
                        "lessons": [
                            {"id": "chem8_c2_b8", "num": 8, "name": "Bài 8: Acid", "isReview": False},
                            {"id": "chem8_c2_b9", "num": 9, "name": "Bài 9: Base - Thang pH", "isReview": False},
                            {"id": "chem8_c2_b10", "num": 10, "name": "Bài 10: Oxide", "isReview": False},
                            {"id": "chem8_c2_b11", "num": 11, "name": "Bài 11: Muối", "isReview": False},
                            {"id": "chem8_c2_b12", "num": 12, "name": "Bài 12: Phân bón hóa học", "isReview": False},
                            {"id": "chem8_c2_rev", "num": 0, "name": "Ôn tập cuối Chương II", "isReview": True}
                        ]
                    }
                ]
            },
            "9": {
                "title": "Hóa học 9",
                "chapters": [
                    {
                        "id": "chem9_c1",
                        "title": "Chương I: Kim loại. Một số kim loại thông dụng",
                        "lessons": [
                            {"id": "chem9_c1_b1", "num": 1, "name": "Bài 1: Tính chất của kim loại", "isReview": False},
                            {"id": "chem9_c1_b2", "num": 2, "name": "Bài 2: Một số kim loại thông dụng (Al, Fe)", "isReview": False},
                            {"id": "chem9_c1_b3", "num": 3, "name": "Bài 3: Dãy hoạt động hóa học của kim loại", "isReview": False},
                            {"id": "chem9_c1_b4", "num": 4, "name": "Bài 4: Tách kim loại và sử dụng hợp kim", "isReview": False},
                            {"id": "chem9_c1_rev", "num": 0, "name": "Ôn tập cuối Chương I", "isReview": True}
                        ]
                    },
                    {
                        "id": "chem9_c2",
                        "title": "Chương II: Hợp chất hữu cơ. Hydrocarbon",
                        "lessons": [
                            {"id": "chem9_c2_b5", "num": 5, "name": "Bài 5: Giới thiệu về hợp chất hữu cơ", "isReview": False},
                            {"id": "chem9_c2_b6", "num": 6, "name": "Bài 6: Alkane", "isReview": False},
                            {"id": "chem9_c2_b7", "num": 7, "name": "Bài 7: Alkene", "isReview": False},
                            {"id": "chem9_c2_b8", "num": 8, "name": "Bài 8: Nguồn nhiên liệu", "isReview": False},
                            {"id": "chem9_c2_rev", "num": 0, "name": "Ôn tập cuối Chương II", "isReview": True}
                        ]
                    },
                    {
                        "id": "chem9_c3",
                        "title": "Chương III: Ethylic alcohol và Acetic acid",
                        "lessons": [
                            {"id": "chem9_c3_b9", "num": 9, "name": "Bài 9: Ethylic alcohol", "isReview": False},
                            {"id": "chem9_c3_b10", "num": 10, "name": "Bài 10: Acetic acid", "isReview": False},
                            {"id": "chem9_c3_rev", "num": 0, "name": "Ôn tập cuối Chương III", "isReview": True}
                        ]
                    },
                    {
                        "id": "chem9_c4",
                        "title": "Chương IV: Lipid - Carbohydrate - Protein - Polymer",
                        "lessons": [
                            {"id": "chem9_c4_b11", "num": 11, "name": "Bài 11: Lipid và chất béo", "isReview": False},
                            {"id": "chem9_c4_b12", "num": 12, "name": "Bài 12: Glucose và Saccharose", "isReview": False},
                            {"id": "chem9_c4_b13", "num": 13, "name": "Bài 13: Tinh bột và Cellulose", "isReview": False},
                            {"id": "chem9_c4_b14", "num": 14, "name": "Bài 14: Protein", "isReview": False},
                            {"id": "chem9_c4_b15", "num": 15, "name": "Bài 15: Polymer", "isReview": False},
                            {"id": "chem9_c4_rev", "num": 0, "name": "Ôn tập cuối Chương IV", "isReview": True}
                        ]
                    },
                    {
                        "id": "chem9_c5",
                        "title": "Chương V: Khai thác tài nguyên vỏ Trái Đất",
                        "lessons": [
                            {"id": "chem9_c5_b16", "num": 16, "name": "Bài 16: Sơ lược về hóa học vỏ Trái Đất và khai thác tài nguyên", "isReview": False},
                            {"id": "chem9_c5_rev", "num": 0, "name": "Ôn tập cuối Chương V", "isReview": True}
                        ]
                    }
                ]
            }
        }
    },
    "physics": {
        "id": "physics",
        "name": "Môn Vật lý",
        "icon": "⚡",
        "grades": {
            "7": {
                "title": "Vật lý 7",
                "chapters": [
                    {
                        "id": "phys7_c3",
                        "title": "Chương III: Tốc độ",
                        "lessons": [
                            {"id": "phys7_c3_b8", "num": 8, "name": "Bài 8: Tốc độ chuyển động", "isReview": False},
                            {"id": "phys7_c3_b9", "num": 9, "name": "Bài 9: Đo tốc độ", "isReview": False},
                            {"id": "phys7_c3_b10", "num": 10, "name": "Bài 10: Đồ thị quãng đường - thời gian", "isReview": False},
                            {"id": "phys7_c3_b11", "num": 11, "name": "Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông", "isReview": False},
                            {"id": "phys7_c3_rev", "num": 0, "name": "Ôn tập cuối Chương III", "isReview": True}
                        ]
                    },
                    {
                        "id": "phys7_c4",
                        "title": "Chương IV: Âm thanh",
                        "lessons": [
                            {"id": "phys7_c4_b12", "num": 12, "name": "Bài 12: Sóng âm", "isReview": False},
                            {"id": "phys7_c4_b13", "num": 13, "name": "Bài 13: Độ to và độ cao của âm", "isReview": False},
                            {"id": "phys7_c4_b14", "num": 14, "name": "Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn", "isReview": False},
                            {"id": "phys7_c4_rev", "num": 0, "name": "Ôn tập cuối Chương IV", "isReview": True}
                        ]
                    },
                    {
                        "id": "phys7_c5",
                        "title": "Chương V: Ánh sáng",
                        "lessons": [
                            {"id": "phys7_c5_b15", "num": 15, "name": "Bài 15: Ánh sáng, tia sáng", "isReview": False},
                            {"id": "phys7_c5_b16", "num": 16, "name": "Bài 16: Sự phản xạ ánh sáng", "isReview": False},
                            {"id": "phys7_c5_b17", "num": 17, "name": "Bài 17: Ảnh của một vật tạo bởi gương phẳng", "isReview": False},
                            {"id": "phys7_c5_rev", "num": 0, "name": "Ôn tập cuối Chương V", "isReview": True}
                        ]
                    },
                    {
                        "id": "phys7_c6",
                        "title": "Chương VI: Từ",
                        "lessons": [
                            {"id": "phys7_c6_b18", "num": 18, "name": "Bài 18: Nam châm", "isReview": False},
                            {"id": "phys7_c6_b19", "num": 19, "name": "Bài 19: Từ trường", "isReview": False},
                            {"id": "phys7_c6_b20", "num": 20, "name": "Bài 20: Chế tạo nam châm điện đơn giản", "isReview": False},
                            {"id": "phys7_c6_rev", "num": 0, "name": "Ôn tập cuối Chương VI", "isReview": True}
                        ]
                    }
                ]
            },
            "8": {
                "title": "Vật lý 8",
                "chapters": [
                    {
                        "id": "phys8_c3",
                        "title": "Chương III: Khối lượng riêng và áp suất",
                        "lessons": [
                            {"id": "phys8_c3_b13", "num": 13, "name": "Bài 13: Khối lượng riêng", "isReview": False},
                            {"id": "phys8_c3_b14", "num": 14, "name": "Bài 14: Thực hành xác định khối lượng riêng", "isReview": False},
                            {"id": "phys8_c3_b15", "num": 15, "name": "Bài 15: Áp suất trên một bề mặt", "isReview": False},
                            {"id": "phys8_c3_b16", "num": 16, "name": "Bài 16: Áp suất chất lỏng. Áp suất khí quyển", "isReview": False},
                            {"id": "phys8_c3_b17", "num": 17, "name": "Bài 17: Lực đẩy Archimedes", "isReview": False},
                            {"id": "phys8_c3_rev", "num": 0, "name": "Ôn tập cuối Chương III", "isReview": True}
                        ]
                    },
                    {
                        "id": "phys8_c4",
                        "title": "Chương IV: Tác dụng làm quay của lực",
                        "lessons": [
                            {"id": "phys8_c4_b18", "num": 18, "name": "Bài 18: Tác dụng làm quay của lực. Moment lực", "isReview": False},
                            {"id": "phys8_c4_b19", "num": 19, "name": "Bài 19: Đòn bẩy và ứng dụng", "isReview": False},
                            {"id": "phys8_c4_rev", "num": 0, "name": "Ôn tập cuối Chương IV", "isReview": True}
                        ]
                    },
                    {
                        "id": "phys8_c5",
                        "title": "Chương V: Điện",
                        "lessons": [
                            {"id": "phys8_c5_b20", "num": 20, "name": "Bài 20: Hiện tượng nhiễm điện do cọ xát", "isReview": False},
                            {"id": "phys8_c5_b21", "num": 21, "name": "Bài 21: Dòng điện, nguồn điện", "isReview": False},
                            {"id": "phys8_c5_b22", "num": 22, "name": "Bài 22: Mạch điện đơn giản", "isReview": False},
                            {"id": "phys8_c5_b23", "num": 23, "name": "Bài 23: Tác dụng của dòng điện", "isReview": False},
                            {"id": "phys8_c5_b24", "num": 24, "name": "Bài 24: Cường độ dòng điện và hiệu điện thế", "isReview": False},
                            {"id": "phys8_c5_b25", "num": 25, "name": "Bài 25: Thực hành đo cường độ dòng điện và hiệu điện thế", "isReview": False},
                            {"id": "phys8_c5_rev", "num": 0, "name": "Ôn tập cuối Chương V", "isReview": True}
                        ]
                    },
                    {
                        "id": "phys8_c6",
                        "title": "Chương VI: Nhiệt",
                        "lessons": [
                            {"id": "phys8_c6_b26", "num": 26, "name": "Bài 26: Năng lượng nhiệt và nội năng", "isReview": False},
                            {"id": "phys8_c6_b27", "num": 27, "name": "Bài 27: Thực hành đo năng lượng nhiệt bằng nhiệt lượng kế", "isReview": False},
                            {"id": "phys8_c6_b28", "num": 28, "name": "Bài 28: Sự truyền nhiệt", "isReview": False},
                            {"id": "phys8_c6_b29", "num": 29, "name": "Bài 29: Sự nở vì nhiệt", "isReview": False},
                            {"id": "phys8_c6_rev", "num": 0, "name": "Ôn tập cuối Chương VI", "isReview": True}
                        ]
                    }
                ]
            },
            "9": {
                "title": "Vật lý 9",
                "chapters": [
                    {
                        "id": "phys9_c6",
                        "title": "Chương VI: Ánh sáng",
                        "lessons": [
                            {"id": "phys9_c6_b17", "num": 17, "name": "Bài 17: Hiện tượng khúc xạ ánh sáng", "isReview": False},
                            {"id": "phys9_c6_b18", "num": 18, "name": "Bài 18: Hiện tượng phản xạ toàn phần", "isReview": False},
                            {"id": "phys9_c6_b19", "num": 19, "name": "Bài 19: Thấu kính", "isReview": False},
                            {"id": "phys9_c6_b20", "num": 20, "name": "Bài 20: Thực hành xác định tiêu cự của thấu kính hội tụ", "isReview": False},
                            {"id": "phys9_c6_b21", "num": 21, "name": "Bài 21: Kính lúp", "isReview": False},
                            {"id": "phys9_c6_rev", "num": 0, "name": "Ôn tập cuối Chương VI", "isReview": True}
                        ]
                    },
                    {
                        "id": "phys9_c7",
                        "title": "Chương VII: Điện từ",
                        "lessons": [
                            {"id": "phys9_c7_b22", "num": 22, "name": "Bài 22: Từ trường của ống dây có dòng điện. Nam châm điện", "isReview": False},
                            {"id": "phys9_c7_b23", "num": 23, "name": "Bài 23: Tác dụng của từ trường lên đoạn dây dẫn mang dòng điện", "isReview": False},
                            {"id": "phys9_c7_b24", "num": 24, "name": "Bài 24: Hiện tượng cảm ứng điện từ. Dòng điện xoay chiều", "isReview": False},
                            {"id": "phys9_c7_b25", "num": 25, "name": "Bài 25: Máy biến thế", "isReview": False},
                            {"id": "phys9_c7_rev", "num": 0, "name": "Ôn tập cuối Chương VII", "isReview": True}
                        ]
                    },
                    {
                        "id": "phys9_c8",
                        "title": "Chương VIII: Năng lượng và sự biến đổi năng lượng",
                        "lessons": [
                            {"id": "phys9_c8_b26", "num": 26, "name": "Bài 26: Vòng năng lượng trên Trái Đất. Năng lượng tái tạo", "isReview": False},
                            {"id": "phys9_c8_b27", "num": 27, "name": "Bài 27: Sự bảo toàn và chuyển hóa năng lượng", "isReview": False},
                            {"id": "phys9_c8_rev", "num": 0, "name": "Ôn tập cuối Chương VIII", "isReview": True}
                        ]
                    }
                ]
            }
        }
    }
}

if __name__ == "__main__":
    total_lessons = 0
    total_exams = 0
    for subj_k, subj in KHTN_CURRICULUM.items():
        print(f"=== {subj['name']} ===")
        for gr_k, gr in subj["grades"].items():
            gr_lessons = 0
            gr_exams = 0
            for ch in gr["chapters"]:
                for l in ch["lessons"]:
                    gr_lessons += 1
                    e_cnt = 5 if l["isReview"] else 3
                    gr_exams += e_cnt
            print(f"  {gr['title']}: {gr_lessons} bài/chương ôn tập => {gr_exams} đề")
            total_lessons += gr_lessons
            total_exams += gr_exams
    print(f"TOTAL: {total_lessons} entries, {total_exams} exams.")
