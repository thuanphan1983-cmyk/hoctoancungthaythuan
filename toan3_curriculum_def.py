# -*- coding: utf-8 -*-
"""
ĐỊNH NGHĨA KHUNG CHƯƠNG TRÌNH TOÁN TIỂU HỌC (LỚP 3 - KẾT NỐI TRI THỨC VỚI CUỘC SỐNG)
Bao gồm:
1. Đề kiểm tra định kỳ: GK1, CK1, GK2, CK2 (8 đề/kỳ)
2. Khung chủ đề bài học theo SGK Toán 3
"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

TOAN3_CURRICULUM = {
    "grade": "3",
    "gradeName": "Lớp 3",
    "subject": "math",
    "subjectName": "Toán học",
    "bookSeries": "Kết nối tri thức với cuộc sống",
    "periodic": {
        "title": "Hệ thống Đề kiểm tra định kỳ Toán 3",
        "terms": [
            {
                "id": "th3_gk1",
                "code": "GK1",
                "name": "Kiểm tra Giữa học kì 1",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Bảng nhân, bảng chia từ 3 đến 9; Gấp một số lên một số lần, giảm đi một số lần; Hình tam giác, tứ giác, khối trụ, khối cầu",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th3_ck1",
                "code": "CK1",
                "name": "Kiểm tra Cuối học kì 1",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Nhân số có 2, 3 chữ số với số có 1 chữ số; Chia số có 2, 3 chữ số cho số có 1 chữ số; Gam (g), mi-li-lít (ml), nhiệt độ; Hình tròn, tâm, đường kính, bán kính; Ôn tập học kì 1",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th3_gk2",
                "code": "GK2",
                "name": "Kiểm tra Giữa học kì 2",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Các số trong phạm vi 10 000; Phép cộng, phép trừ trong phạm vi 10 000; Chu vi tam giác, tứ giác, hình chữ nhật, hình vuông; Tháng - năm",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th3_ck2",
                "code": "CK2",
                "name": "Kiểm tra Cuối học kì 2 (Cuối năm)",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Các số trong phạm vi 100 000; Phép cộng, trừ, nhân, chia phạm vi 100 000; Diện tích hình chữ nhật, hình vuông; Tiền Việt Nam; Bảng số liệu, khả năng xảy ra của sự kiện; Ôn tập cuối năm",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            }
        ]
    },
    "chapters": [
        {
            "id": "th3_ch1",
            "title": "Chủ đề 1: Bảng nhân, bảng chia (3, 4, 6, 7, 8, 9)",
            "term": "hk1",
            "lessons": [
                {"id": "th3_b1", "num": 1, "name": "Bài 1: Ôn tập bảng nhân 2, 5; bảng chia 2, 5"},
                {"id": "th3_b2", "num": 2, "name": "Bài 2: Bảng nhân 3, bảng chia 3"},
                {"id": "th3_b3", "num": 3, "name": "Bài 3: Bảng nhân 4, bảng chia 4"}
            ]
        },
        {
            "id": "th3_ch2",
            "title": "Chủ đề 2: Bảng nhân, chia tiếp theo",
            "term": "hk1",
            "lessons": [
                {"id": "th3_b4", "num": 4, "name": "Bài 4: Bảng nhân 6, 7; bảng chia 6, 7"},
                {"id": "th3_b5", "num": 5, "name": "Bài 5: Bảng nhân 8, 9; bảng chia 8, 9"},
                {"id": "th3_b6", "num": 6, "name": "Bài 6: Gấp một số lên nhiều lần, giảm đi nhiều lần"}
            ]
        },
        {
            "id": "th3_ch3",
            "title": "Chủ đề 3: Làm quen với hình phẳng, hình khối",
            "term": "hk1",
            "lessons": [
                {"id": "th3_b7", "num": 7, "name": "Bài 7: Góc vuông, góc không vuông"},
                {"id": "th3_b8", "num": 8, "name": "Bài 8: Hình tròn, tâm, bán kính, đường kính"}
            ]
        },
        {
            "id": "th3_ch4",
            "title": "Chủ đề 4: Phép nhân, chia trong phạm vi 1000",
            "term": "hk1",
            "lessons": [
                {"id": "th3_b9", "num": 9, "name": "Bài 9: Nhân số có hai, ba chữ số với số có một chữ số"},
                {"id": "th3_b10", "num": 10, "name": "Bài 10: Chia số có hai, ba chữ số cho số có một chữ số"}
            ]
        },
        {
            "id": "th3_ch5",
            "title": "Chủ đề 5: Một số đơn vị đo đại lượng",
            "term": "hk1",
            "lessons": [
                {"id": "th3_b11", "num": 11, "name": "Bài 11: Gam (g)"},
                {"id": "th3_b12", "num": 12, "name": "Bài 12: Mi-li-lít (ml)"},
                {"id": "th3_b13", "num": 13, "name": "Bài 13: Nhiệt độ, đo nhiệt độ"}
            ]
        },
        {
            "id": "th3_ch6",
            "title": "Chủ đề 6: Ôn tập học kì 1",
            "term": "hk1",
            "lessons": [
                {"id": "th3_b14", "num": 14, "name": "Bài 14: Ôn tập học kì 1", "isReview": True}
            ]
        },
        {
            "id": "th3_ch7",
            "title": "Chủ đề 7: Các số trong phạm vi 10 000",
            "term": "hk2",
            "lessons": [
                {"id": "th3_b15", "num": 15, "name": "Bài 15: Các số có bốn chữ số"},
                {"id": "th3_b16", "num": 16, "name": "Bài 16: So sánh các số trong phạm vi 10 000"}
            ]
        },
        {
            "id": "th3_ch8",
            "title": "Chủ đề 8: Chu vi và diện tích",
            "term": "hk2",
            "lessons": [
                {"id": "th3_b17", "num": 17, "name": "Bài 17: Chu vi hình tam giác, hình tứ giác"},
                {"id": "th3_b18", "num": 18, "name": "Bài 18: Chu vi hình chữ nhật, hình vuông"},
                {"id": "th3_b19", "num": 19, "name": "Bài 19: Diện tích hình chữ nhật, hình vuông"}
            ]
        },
        {
            "id": "th3_ch9",
            "title": "Chủ đề 9: Các số trong phạm vi 100 000",
            "term": "hk2",
            "lessons": [
                {"id": "th3_b20", "num": 20, "name": "Bài 20: Các số có năm chữ số"},
                {"id": "th3_b21", "num": 21, "name": "Bài 21: So sánh các số trong phạm vi 100 000"}
            ]
        },
        {
            "id": "th3_ch10",
            "title": "Chủ đề 10: Phép cộng, trừ, nhân, chia phạm vi 100 000",
            "term": "hk2",
            "lessons": [
                {"id": "th3_b22", "num": 22, "name": "Bài 22: Phép cộng, phép trừ trong phạm vi 100 000"},
                {"id": "th3_b23", "num": 23, "name": "Bài 23: Phép nhân, phép chia trong phạm vi 100 000"}
            ]
        },
        {
            "id": "th3_ch11",
            "title": "Chủ đề 11: Tiền Việt Nam",
            "term": "hk2",
            "lessons": [
                {"id": "th3_b24", "num": 24, "name": "Bài 24: Tiền Việt Nam"}
            ]
        },
        {
            "id": "th3_ch12",
            "title": "Chủ đề 12: Thống kê và xác suất",
            "term": "hk2",
            "lessons": [
                {"id": "th3_b25", "num": 25, "name": "Bài 25: Bảng số liệu và khả năng xảy ra của một sự kiện"}
            ]
        },
        {
            "id": "th3_ch13",
            "title": "Chủ đề 13: Ôn tập cuối năm",
            "term": "hk2",
            "lessons": [
                {"id": "th3_b26", "num": 26, "name": "Bài 26: Ôn tập phép tính cuối năm"},
                {"id": "th3_b27", "num": 27, "name": "Bài 27: Ôn tập hình học và giải toán cuối năm", "isReview": True}
            ]
        }
    ]
}

if __name__ == "__main__":
    print(f"TOAN3: {len(TOAN3_CURRICULUM['chapters'])} chu de, {len(TOAN3_CURRICULUM['periodic']['terms'])} dot dinh ky")
