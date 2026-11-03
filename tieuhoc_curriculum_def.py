# -*- coding: utf-8 -*-
"""
TỔNG HỢP KHUNG CHƯƠNG TRÌNH TOÁN TIỂU HỌC TOÀN DIỆN (LỚP 1, 2, 3, 4, 5)
Bộ sách Kết nối tri thức với cuộc sống
"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

from toan1_curriculum_def import TOAN1_CURRICULUM
from toan2_curriculum_def import TOAN2_CURRICULUM
from toan3_curriculum_def import TOAN3_CURRICULUM
from toan4_curriculum_def import TOAN4_CURRICULUM

# Định nghĩa Lớp 5
TOAN5_CURRICULUM = {
    "grade": "5",
    "gradeName": "Lớp 5",
    "subject": "math",
    "subjectName": "Toán học",
    "bookSeries": "Kết nối tri thức với cuộc sống",
    "periodic": {
        "title": "Hệ thống Đề kiểm tra định kỳ Toán 5",
        "terms": [
            {
                "id": "th5_gk1",
                "code": "GK1",
                "name": "Kiểm tra Giữa học kì 1",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Ôn tập số tự nhiên, phân số, hỗn số, bài toán về tỉ số, phân số thập phân và khái niệm số thập phân",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th5_ck1",
                "code": "CK1",
                "name": "Kiểm tra Cuối học kì 1",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Các phép tính cộng, trừ, nhân, chia số thập phân; Viết số đo dưới dạng số thập phân; Diện tích tam giác, hình thang, hình tròn",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th5_gk2",
                "code": "GK2",
                "name": "Kiểm tra Giữa học kì 2",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Tỉ số phần trăm và các bài toán thực tế; Bảng đơn vị đo thể tích (cm³, dm³, m³); Diện tích và thể tích hình hộp chữ nhật, hình lập phương",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th5_ck2",
                "code": "CK2",
                "name": "Kiểm tra Cuối học kì 2 (Cuối năm)",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Bảng đơn vị đo thời gian; Toán chuyển động đều (vận tốc, quãng đường, thời gian); Biểu đồ hình quạt tròn; Ôn tập tổng hợp chuẩn bị vào lớp 6",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            }
        ]
    },
    "chapters": [
        {
            "id": "th5_ch1",
            "title": "Chủ đề 1: Ôn tập và bổ sung",
            "term": "hk1",
            "lessons": [
                {"id": "th5_b1", "num": 1, "name": "Bài 1: Ôn tập về số tự nhiên"},
                {"id": "th5_b2", "num": 2, "name": "Bài 2: Ôn tập các phép tính với số tự nhiên"},
                {"id": "th5_b3", "num": 3, "name": "Bài 3: Ôn tập phân số"},
                {"id": "th5_b4", "num": 4, "name": "Bài 4: Phân số thập phân"},
                {"id": "th5_b5", "num": 5, "name": "Bài 5: Ôn tập các phép tính với phân số"},
                {"id": "th5_b6", "num": 6, "name": "Bài 6: Bài toán liên quan đến tỉ số"},
                {"id": "th5_b7", "num": 7, "name": "Bài 7: Hỗn số"},
                {"id": "th5_b8", "num": 8, "name": "Bài 8: Ôn tập hình học và đo lường"},
                {"id": "th5_b9", "num": 9, "name": "Bài 9: Luyện tập chung Chủ đề 1", "isReview": True}
            ]
        },
        {
            "id": "th5_ch2",
            "title": "Chủ đề 2: Số thập phân",
            "term": "hk1",
            "lessons": [
                {"id": "th5_b10", "num": 10, "name": "Bài 10: Khái niệm số thập phân"},
                {"id": "th5_b11", "num": 11, "name": "Bài 11: So sánh các số thập phân"},
                {"id": "th5_b12", "num": 12, "name": "Bài 12: Viết số đo đại lượng dưới dạng số thập phân"},
                {"id": "th5_b13", "num": 13, "name": "Bài 13: Làm tròn số thập phân"},
                {"id": "th5_b14", "num": 14, "name": "Bài 14: Luyện tập chung Chủ đề 2", "isReview": True}
            ]
        },
        {
            "id": "th5_ch3",
            "title": "Chủ đề 3: Các phép tính với số thập phân",
            "term": "hk1",
            "lessons": [
                {"id": "th5_b15", "num": 15, "name": "Bài 15: Phép cộng số thập phân"},
                {"id": "th5_b16", "num": 16, "name": "Bài 16: Phép trừ số thập phân"},
                {"id": "th5_b17", "num": 17, "name": "Bài 17: Phép nhân số thập phân"},
                {"id": "th5_b18", "num": 18, "name": "Bài 18: Nhân số thập phân với 10, 100, 1000... hoặc với 0,1; 0,01..."},
                {"id": "th5_b19", "num": 19, "name": "Bài 19: Phép chia số thập phân"},
                {"id": "th5_b20", "num": 20, "name": "Bài 20: Chia số thập phân cho 10, 100, 1000... hoặc cho 0,1; 0,01..."},
                {"id": "th5_b21", "num": 21, "name": "Bài 21: Luyện tập chung Chủ đề 3", "isReview": True}
            ]
        },
        {
            "id": "th5_ch4",
            "title": "Chủ đề 4: Hình tam giác, hình thang, hình tròn",
            "term": "hk1",
            "lessons": [
                {"id": "th5_b22", "num": 22, "name": "Bài 22: Hình tam giác. Diện tích hình tam giác"},
                {"id": "th5_b23", "num": 23, "name": "Bài 23: Hình thang. Diện tích hình thang"},
                {"id": "th5_b24", "num": 24, "name": "Bài 24: Hình tròn. Chu vi và diện tích hình tròn"},
                {"id": "th5_b25", "num": 25, "name": "Bài 25: Luyện tập chung Chủ đề 4", "isReview": True}
            ]
        },
        {
            "id": "th5_ch5",
            "title": "Chủ đề 5: Ôn tập học kì 1",
            "term": "hk1",
            "lessons": [
                {"id": "th5_b26", "num": 26, "name": "Bài 26: Ôn tập số thập phân và các phép tính"},
                {"id": "th5_b27", "num": 27, "name": "Bài 27: Ôn tập hình học và đo lường"},
                {"id": "th5_b28", "num": 28, "name": "Bài 28: Ôn tập chung học kì 1", "isReview": True}
            ]
        },
        {
            "id": "th5_ch6",
            "title": "Chủ đề 6: Tỉ số phần trăm",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b29", "num": 29, "name": "Bài 29: Tỉ số phần trăm"},
                {"id": "th5_b30", "num": 30, "name": "Bài 30: Tìm tỉ số phần trăm của hai số"},
                {"id": "th5_b31", "num": 31, "name": "Bài 31: Tìm giá trị phần trăm của một số"},
                {"id": "th5_b32", "num": 32, "name": "Bài 32: Luyện tập chung Chủ đề 6", "isReview": True}
            ]
        },
        {
            "id": "th5_ch7",
            "title": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b33", "num": 33, "name": "Bài 33: Khái niệm thể tích. Xăng-ti-mét khối (cm³)"},
                {"id": "th5_b34", "num": 34, "name": "Bài 34: Đề-xi-mét khối (dm³), Mét khối (m³)"},
                {"id": "th5_b35", "num": 35, "name": "Bài 35: Luyện tập chung Chủ đề 7", "isReview": True}
            ]
        },
        {
            "id": "th5_ch8",
            "title": "Chủ đề 8: Diện tích, thể tích hình hộp chữ nhật, hình lập phương",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b36", "num": 36, "name": "Bài 36: Diện tích xung quanh và toàn phần hình hộp chữ nhật"},
                {"id": "th5_b37", "num": 37, "name": "Bài 37: Thể tích hình hộp chữ nhật"},
                {"id": "th5_b38", "num": 38, "name": "Bài 38: Diện tích xung quanh và toàn phần hình lập phương"},
                {"id": "th5_b39", "num": 39, "name": "Bài 39: Thể tích hình lập phương"},
                {"id": "th5_b40", "num": 40, "name": "Bài 40: Luyện tập chung Chủ đề 8", "isReview": True}
            ]
        },
        {
            "id": "th5_ch9",
            "title": "Chủ đề 9: Bảng đơn vị đo thời gian. Vận tốc, quãng đường, thời gian",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b41", "num": 41, "name": "Bài 41: Bảng đơn vị đo thời gian"},
                {"id": "th5_b42", "num": 42, "name": "Bài 42: Cộng, trừ số đo thời gian"},
                {"id": "th5_b43", "num": 43, "name": "Bài 43: Nhân, chia số đo thời gian"},
                {"id": "th5_b44", "num": 44, "name": "Bài 44: Vận tốc"},
                {"id": "th5_b45", "num": 45, "name": "Bài 45: Quãng đường"},
                {"id": "th5_b46", "num": 46, "name": "Bài 46: Thời gian"},
                {"id": "th5_b47", "num": 47, "name": "Bài 47: Luyện tập chung toán chuyển động", "isReview": True}
            ]
        },
        {
            "id": "th5_ch10",
            "title": "Chủ đề 10: Một số yếu tố xác suất và thống kê",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b48", "num": 48, "name": "Bài 48: Biểu đồ hình quạt tròn"},
                {"id": "th5_b49", "num": 49, "name": "Bài 49: Tỉ số mô tả số lần lặp lại của một khả năng xảy ra"},
                {"id": "th5_b50", "num": 50, "name": "Bài 50: Luyện tập chung Chủ đề 10", "isReview": True}
            ]
        },
        {
            "id": "th5_ch11",
            "title": "Chủ đề 11: Ôn tập cuối năm",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b51", "num": 51, "name": "Bài 51: Ôn tập số tự nhiên, phân số, số thập phân"},
                {"id": "th5_b52", "num": 52, "name": "Bài 52: Ôn tập các phép tính với số thập phân"},
                {"id": "th5_b53", "num": 53, "name": "Bài 53: Ôn tập hình học và đo lường"},
                {"id": "th5_b54", "num": 54, "name": "Bài 54: Ôn tập toán chuyển động đều"},
                {"id": "th5_b55", "num": 55, "name": "Bài 55: Ôn tập chung toàn diện cuối năm", "isReview": True}
            ]
        }
    ]
}

# TIEUHOC_CURRICULUM hỗ trợ đầy đủ cả 5 khối lớp Tiểu học (Lớp 1 đến Lớp 5)
TIEUHOC_CURRICULUM = {
    "grades": {
        "1": TOAN1_CURRICULUM,
        "2": TOAN2_CURRICULUM,
        "3": TOAN3_CURRICULUM,
        "4": TOAN4_CURRICULUM,
        "5": TOAN5_CURRICULUM
    },
    "1": TOAN1_CURRICULUM,
    "2": TOAN2_CURRICULUM,
    "3": TOAN3_CURRICULUM,
    "4": TOAN4_CURRICULUM,
    "5": TOAN5_CURRICULUM,
    # Mặc định tương thích ngược cho Lớp 5 nếu code cũ truy cập trực tiếp
    "grade": "5",
    "gradeName": "Lớp 5",
    "periodic": TOAN5_CURRICULUM["periodic"],
    "chapters": TOAN5_CURRICULUM["chapters"]
}

if __name__ == "__main__":
    print("=== TỔNG HỢP KHUNG CHƯƠNG TRÌNH TIỂU HỌC TOÀN CẤP (LỚP 1 - 5) ===")
    for g in ["1", "2", "3", "4", "5"]:
        c = TIEUHOC_CURRICULUM[g]
        p_count = sum(t["totalTests"] for t in c["periodic"]["terms"])
        ch_count = len(c["chapters"])
        l_count = sum(len(ch["lessons"]) for ch in c["chapters"])
        print(f"+ {c['gradeName']}: {ch_count} chủ đề, {l_count} bài học, {p_count} đề định kỳ")
