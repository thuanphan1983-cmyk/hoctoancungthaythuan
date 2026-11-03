# -*- coding: utf-8 -*-
"""
ĐỊNH NGHĨA KHUNG CHƯƠNG TRÌNH TOÁN TIỂU HỌC (LỚP 2 - KẾT NỐI TRI THỨC VỚI CUỘC SỐNG)
Bao gồm:
1. Đề kiểm tra định kỳ: GK1, CK1, GK2, CK2 (8 đề/kỳ)
2. Khung chủ đề bài học theo SGK Toán 2
"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

TOAN2_CURRICULUM = {
    "grade": "2",
    "gradeName": "Lớp 2",
    "subject": "math",
    "subjectName": "Toán học",
    "bookSeries": "Kết nối tri thức với cuộc sống",
    "periodic": {
        "title": "Hệ thống Đề kiểm tra định kỳ Toán 2",
        "terms": [
            {
                "id": "th2_gk1",
                "code": "GK1",
                "name": "Kiểm tra Giữa học kì 1",
                "time": "35 phút",
                "totalTests": 8,
                "scope": "Ôn tập các số đến 100; Phép cộng, trừ qua 10 trong phạm vi 20; Điểm, đoạn thẳng, đường cong; Đề-xi-mét (dm)",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th2_ck1",
                "code": "CK1",
                "name": "Kiểm tra Cuối học kì 1",
                "time": "35 phút",
                "totalTests": 8,
                "scope": "Phép cộng, trừ có nhớ trong phạm vi 100; Đơn vị đo ki-lô-gam (kg), lít (l); Đường gấp khúc; Ngày - giờ, giờ - phút; Ôn tập học kì 1",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th2_gk2",
                "code": "GK2",
                "name": "Kiểm tra Giữa học kì 2",
                "time": "35 phút",
                "totalTests": 8,
                "scope": "Phép nhân, phép chia; Bảng nhân 2, 5; Bảng chia 2, 5; Khối trụ, khối cầu; Các số trong phạm vi 1000",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th2_ck2",
                "code": "CK2",
                "name": "Kiểm tra Cuối học kì 2 (Cuối năm)",
                "time": "35 phút",
                "totalTests": 8,
                "scope": "Phép cộng, trừ trong phạm vi 1000; Đơn vị đo mét (m), ki-lô-mét (km); Tiền Việt Nam; Thu thập, phân loại, kiểm đếm số liệu; Ôn tập cuối năm",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            }
        ]
    },
    "chapters": [
        {
            "id": "th2_ch1",
            "title": "Chủ đề 1: Ôn tập và bổ sung",
            "term": "hk1",
            "lessons": [
                {"id": "th2_b1", "num": 1, "name": "Bài 1: Ôn tập các số đến 100"},
                {"id": "th2_b2", "num": 2, "name": "Bài 2: Tia số. Số liền trước, số liền sau"},
                {"id": "th2_b3", "num": 3, "name": "Bài 3: Các thành phần của phép cộng, phép trừ"}
            ]
        },
        {
            "id": "th2_ch2",
            "title": "Chủ đề 2: Phép cộng, phép trừ trong phạm vi 20",
            "term": "hk1",
            "lessons": [
                {"id": "th2_b4", "num": 4, "name": "Bài 4: Bảng cộng (qua 10)"},
                {"id": "th2_b5", "num": 5, "name": "Bài 5: Bảng trừ (qua 10)"},
                {"id": "th2_b6", "num": 6, "name": "Bài 6: Luyện tập chung phép cộng, trừ phạm vi 20", "isReview": True}
            ]
        },
        {
            "id": "th2_ch3",
            "title": "Chủ đề 3: Làm quen với khối lượng, dung tích",
            "term": "hk1",
            "lessons": [
                {"id": "th2_b7", "num": 7, "name": "Bài 7: Ki-lô-gam (kg)"},
                {"id": "th2_b8", "num": 8, "name": "Bài 8: Lít (l)"}
            ]
        },
        {
            "id": "th2_ch4",
            "title": "Chủ đề 4: Phép cộng, phép trừ có nhớ trong phạm vi 100",
            "term": "hk1",
            "lessons": [
                {"id": "th2_b9", "num": 9, "name": "Bài 9: Phép cộng có nhớ trong phạm vi 100"},
                {"id": "th2_b10", "num": 10, "name": "Bài 10: Phép trừ có nhớ trong phạm vi 100"}
            ]
        },
        {
            "id": "th2_ch5",
            "title": "Chủ đề 5: Làm quen với hình phẳng",
            "term": "hk1",
            "lessons": [
                {"id": "th2_b11", "num": 11, "name": "Bài 11: Điểm, đoạn thẳng, đường cong"},
                {"id": "th2_b12", "num": 12, "name": "Bài 12: Đường gấp khúc, độ dài đường gấp khúc"},
                {"id": "th2_b13", "num": 13, "name": "Bài 13: Ba điểm thẳng hàng"}
            ]
        },
        {
            "id": "th2_ch6",
            "title": "Chủ đề 6: Ngày - giờ, giờ - phút, ngày - tháng",
            "term": "hk1",
            "lessons": [
                {"id": "th2_b14", "num": 14, "name": "Bài 14: Ngày - giờ, giờ - phút"},
                {"id": "th2_b15", "num": 15, "name": "Bài 15: Ngày - tháng"}
            ]
        },
        {
            "id": "th2_ch7",
            "title": "Chủ đề 7: Ôn tập học kì 1",
            "term": "hk1",
            "lessons": [
                {"id": "th2_b16", "num": 16, "name": "Bài 16: Ôn tập học kì 1", "isReview": True}
            ]
        },
        {
            "id": "th2_ch8",
            "title": "Chủ đề 8: Phép nhân và phép chia",
            "term": "hk2",
            "lessons": [
                {"id": "th2_b17", "num": 17, "name": "Bài 17: Phép nhân, thừa số và tích"},
                {"id": "th2_b18", "num": 18, "name": "Bài 18: Bảng nhân 2, bảng nhân 5"},
                {"id": "th2_b19", "num": 19, "name": "Bài 19: Phép chia, số bị chia, số chia, thương"},
                {"id": "th2_b20", "num": 20, "name": "Bài 20: Bảng chia 2, bảng chia 5"}
            ]
        },
        {
            "id": "th2_ch9",
            "title": "Chủ đề 9: Làm quen với hình khối",
            "term": "hk2",
            "lessons": [
                {"id": "th2_b21", "num": 21, "name": "Bài 21: Khối trụ, khối cầu"}
            ]
        },
        {
            "id": "th2_ch10",
            "title": "Chủ đề 10: Các số trong phạm vi 1000",
            "term": "hk2",
            "lessons": [
                {"id": "th2_b22", "num": 22, "name": "Bài 22: Đơn vị, chục, trăm, nghìn"},
                {"id": "th2_b23", "num": 23, "name": "Bài 23: Các số có ba chữ số"},
                {"id": "th2_b24", "num": 24, "name": "Bài 24: So sánh các số có ba chữ số"}
            ]
        },
        {
            "id": "th2_ch11",
            "title": "Chủ đề 11: Độ dài và đơn vị đo độ dài",
            "term": "hk2",
            "lessons": [
                {"id": "th2_b25", "num": 25, "name": "Bài 25: Mét (m), ki-lô-mét (km)"},
                {"id": "th2_b26", "num": 26, "name": "Bài 26: Mi-li-mét (mm)"}
            ]
        },
        {
            "id": "th2_ch12",
            "title": "Chủ đề 12: Phép cộng, phép trừ trong phạm vi 1000",
            "term": "hk2",
            "lessons": [
                {"id": "th2_b27", "num": 27, "name": "Bài 27: Phép cộng trong phạm vi 1000"},
                {"id": "th2_b28", "num": 28, "name": "Bài 28: Phép trừ trong phạm vi 1000"}
            ]
        },
        {
            "id": "th2_ch13",
            "title": "Chủ đề 13: Tiền Việt Nam và thống kê",
            "term": "hk2",
            "lessons": [
                {"id": "th2_b29", "num": 29, "name": "Bài 29: Tiền Việt Nam"},
                {"id": "th2_b30", "num": 30, "name": "Bài 30: Thu thập, phân loại, kiểm đếm số liệu"}
            ]
        },
        {
            "id": "th2_ch14",
            "title": "Chủ đề 14: Ôn tập cuối năm",
            "term": "hk2",
            "lessons": [
                {"id": "th2_b31", "num": 31, "name": "Bài 31: Ôn tập phép tính cuối năm"},
                {"id": "th2_b32", "num": 32, "name": "Bài 32: Ôn tập hình học và đo lường cuối năm", "isReview": True}
            ]
        }
    ]
}

if __name__ == "__main__":
    print(f"TOAN2: {len(TOAN2_CURRICULUM['chapters'])} chu de, {len(TOAN2_CURRICULUM['periodic']['terms'])} dot dinh ky")
