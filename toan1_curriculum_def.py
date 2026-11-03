# -*- coding: utf-8 -*-
"""
ĐỊNH NGHĨA KHUNG CHƯƠNG TRÌNH TOÁN TIỂU HỌC (LỚP 1 - KẾT NỐI TRI THỨC VỚI CUỘC SỐNG)
Bao gồm:
1. Đề kiểm tra định kỳ: GK1, CK1, GK2, CK2 (8 đề/kỳ)
2. Khung chủ đề bài học theo SGK Toán 1
"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

TOAN1_CURRICULUM = {
    "grade": "1",
    "gradeName": "Lớp 1",
    "subject": "math",
    "subjectName": "Toán học",
    "bookSeries": "Kết nối tri thức với cuộc sống",
    "periodic": {
        "title": "Hệ thống Đề kiểm tra định kỳ Toán 1",
        "terms": [
            {
                "id": "th1_gk1",
                "code": "GK1",
                "name": "Kiểm tra Giữa học kì 1",
                "time": "35 phút",
                "totalTests": 8,
                "scope": "Các số từ 0 đến 10; So sánh số, nhiều hơn, ít hơn; Hình vuông, hình tròn, hình tam giác, hình chữ nhật",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th1_ck1",
                "code": "CK1",
                "name": "Kiểm tra Cuối học kì 1",
                "time": "35 phút",
                "totalTests": 8,
                "scope": "Phép cộng và phép trừ trong phạm vi 10; Bảng cộng, trừ trong phạm vi 10; Khối lập phương, khối hộp chữ nhật",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th1_gk2",
                "code": "GK2",
                "name": "Kiểm tra Giữa học kì 2",
                "time": "35 phút",
                "totalTests": 8,
                "scope": "Các số có hai chữ số trong phạm vi 100; Số chục, số đơn vị; Đo độ dài, xăng-ti-mét (cm)",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th1_ck2",
                "code": "CK2",
                "name": "Kiểm tra Cuối học kì 2 (Cuối năm)",
                "time": "35 phút",
                "totalTests": 8,
                "scope": "Phép cộng, trừ (không nhớ) trong phạm vi 100; Đọc giờ đúng trên đồng hồ; Ngày trong tuần; Ôn tập cuối năm",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            }
        ]
    },
    "chapters": [
        {
            "id": "th1_ch1",
            "title": "Chủ đề 1: Các số từ 0 đến 10",
            "term": "hk1",
            "lessons": [
                {"id": "th1_b1", "num": 1, "name": "Bài 1: Các số 0, 1, 2, 3, 4, 5"},
                {"id": "th1_b2", "num": 2, "name": "Bài 2: Các số 6, 7, 8, 9, 10"},
                {"id": "th1_b3", "num": 3, "name": "Bài 3: Nhiều hơn, ít hơn, bằng nhau"},
                {"id": "th1_b4", "num": 4, "name": "Bài 4: So sánh số"}
            ]
        },
        {
            "id": "th1_ch2",
            "title": "Chủ đề 2: Làm quen với một số hình phẳng",
            "term": "hk1",
            "lessons": [
                {"id": "th1_b5", "num": 5, "name": "Bài 5: Hình vuông, hình tròn, hình tam giác, hình chữ nhật"}
            ]
        },
        {
            "id": "th1_ch3",
            "title": "Chủ đề 3: Phép cộng, phép trừ trong phạm vi 10",
            "term": "hk1",
            "lessons": [
                {"id": "th1_b6", "num": 6, "name": "Bài 6: Phép cộng trong phạm vi 10"},
                {"id": "th1_b7", "num": 7, "name": "Bài 7: Phép trừ trong phạm vi 10"},
                {"id": "th1_b8", "num": 8, "name": "Bài 8: Luyện tập phép cộng, phép trừ trong phạm vi 10"}
            ]
        },
        {
            "id": "th1_ch4",
            "title": "Chủ đề 4: Làm quen với một số hình khối",
            "term": "hk1",
            "lessons": [
                {"id": "th1_b9", "num": 9, "name": "Bài 9: Khối lập phương, khối hộp chữ nhật"}
            ]
        },
        {
            "id": "th1_ch5",
            "title": "Chủ đề 5: Ôn tập học kì 1",
            "term": "hk1",
            "lessons": [
                {"id": "th1_b10", "num": 10, "name": "Bài 10: Ôn tập học kì 1", "isReview": True}
            ]
        },
        {
            "id": "th1_ch6",
            "title": "Chủ đề 6: Các số trong phạm vi 100",
            "term": "hk2",
            "lessons": [
                {"id": "th1_b11", "num": 11, "name": "Bài 11: Các số đến 20"},
                {"id": "th1_b12", "num": 12, "name": "Bài 12: Các số tròn chục"},
                {"id": "th1_b13", "num": 13, "name": "Bài 13: Các số có hai chữ số đến 100"},
                {"id": "th1_b14", "num": 14, "name": "Bài 14: So sánh các số trong phạm vi 100"}
            ]
        },
        {
            "id": "th1_ch7",
            "title": "Chủ đề 7: Độ dài và đo độ dài",
            "term": "hk2",
            "lessons": [
                {"id": "th1_b15", "num": 15, "name": "Bài 15: Dài hơn, ngắn hơn"},
                {"id": "th1_b16", "num": 16, "name": "Bài 16: Đơn vị đo độ dài: Xăng-ti-mét (cm)"}
            ]
        },
        {
            "id": "th1_ch8",
            "title": "Chủ đề 8: Phép cộng, phép trừ trong phạm vi 100",
            "term": "hk2",
            "lessons": [
                {"id": "th1_b17", "num": 17, "name": "Bài 17: Phép cộng trong phạm vi 100 (không nhớ)"},
                {"id": "th1_b18", "num": 18, "name": "Bài 18: Phép trừ trong phạm vi 100 (không nhớ)"}
            ]
        },
        {
            "id": "th1_ch9",
            "title": "Chủ đề 9: Thời gian, giờ và lịch",
            "term": "hk2",
            "lessons": [
                {"id": "th1_b19", "num": 19, "name": "Bài 19: Xem đồng hồ đúng giờ"},
                {"id": "th1_b20", "num": 20, "name": "Bài 20: Ngày trong tuần, xem lịch"}
            ]
        },
        {
            "id": "th1_ch10",
            "title": "Chủ đề 10: Ôn tập cuối năm",
            "term": "hk2",
            "lessons": [
                {"id": "th1_b21", "num": 21, "name": "Bài 21: Ôn tập các số trong phạm vi 100"},
                {"id": "th1_b22", "num": 22, "name": "Bài 22: Ôn tập phép tính và hình học cuối năm", "isReview": True}
            ]
        }
    ]
}

if __name__ == "__main__":
    print(f"TOAN1: {len(TOAN1_CURRICULUM['chapters'])} chu de, {len(TOAN1_CURRICULUM['periodic']['terms'])} dot dinh ky")
