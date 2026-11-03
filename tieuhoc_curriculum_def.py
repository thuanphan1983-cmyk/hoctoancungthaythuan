# -*- coding: utf-8 -*-
"""
ĐỊNH NGHĨA KHUNG CHƯƠNG TRÌNH TOÁN TIỂU HỌC (LỚP 5 - BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG)
Bao gồm:
1. Đề kiểm tra theo bài học SGK (mỗi bài có 3 đề kiểm tra độc lập: 6 TN + 6 TL)
2. Đề kiểm tra định kỳ (Giữa kì 1, Cuối kì 1, Giữa kì 2, Cuối kì 2; mỗi kỳ có 8 đề độc lập: 6 TN + 6 TL)
"""

TIEUHOC_CURRICULUM = {
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
                {"id": "th5_b18", "num": 18, "name": "Bài 18: Nhân số thập phân với 10, 100, 1000... hoặc với 0,1; 0,01; 0,001..."},
                {"id": "th5_b19", "num": 19, "name": "Bài 19: Phép chia số thập phân"},
                {"id": "th5_b20", "num": 20, "name": "Bài 20: Chia số thập phân cho 10, 100, 1000... hoặc cho 0,1; 0,01; 0,001..."},
                {"id": "th5_b21", "num": 21, "name": "Bài 21: Luyện tập chung Chủ đề 3", "isReview": True}
            ]
        },
        {
            "id": "th5_ch4",
            "title": "Chủ đề 4: Hình phẳng và hình khối",
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
                {"id": "th5_b26", "num": 26, "name": "Bài 26: Ôn tập số và các phép tính"},
                {"id": "th5_b27", "num": 27, "name": "Bài 27: Ôn tập hình học và đo lường"},
                {"id": "th5_b28", "num": 28, "name": "Bài 28: Ôn tập một số yếu tố xác suất và thống kê"},
                {"id": "th5_b29", "num": 29, "name": "Bài 29: Luyện tập chung Học kì 1", "isReview": True}
            ]
        },
        {
            "id": "th5_ch6",
            "title": "Chủ đề 6: Tỉ số phần trăm",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b30", "num": 30, "name": "Bài 30: Tỉ số và tỉ số phần trăm"},
                {"id": "th5_b31", "num": 31, "name": "Bài 31: Tìm tỉ số phần trăm của hai số"},
                {"id": "th5_b32", "num": 32, "name": "Bài 32: Tìm giá trị phần trăm của một số"},
                {"id": "th5_b33", "num": 33, "name": "Bài 33: Sử dụng máy tính cầm tay"},
                {"id": "th5_b34", "num": 34, "name": "Bài 34: Luyện tập chung Chủ đề 6", "isReview": True}
            ]
        },
        {
            "id": "th5_ch7",
            "title": "Chủ đề 7: Thể tích. Đơn vị đo thể tích",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b35", "num": 35, "name": "Bài 35: Khái niệm về thể tích. Xăng-ti-mét khối"},
                {"id": "th5_b36", "num": 36, "name": "Bài 36: Đề-xi-mét khối. Mét khối"},
                {"id": "th5_b37", "num": 37, "name": "Bài 37: Luyện tập chung Chủ đề 7", "isReview": True}
            ]
        },
        {
            "id": "th5_ch8",
            "title": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b38", "num": 38, "name": "Bài 38: Hình hộp chữ nhật, hình lập phương"},
                {"id": "th5_b39", "num": 39, "name": "Bài 39: Diện tích xung quanh và toàn phần hình hộp chữ nhật"},
                {"id": "th5_b40", "num": 40, "name": "Bài 40: Diện tích xung quanh và toàn phần hình lập phương"},
                {"id": "th5_b41", "num": 41, "name": "Bài 41: Thể tích hình hộp chữ nhật"},
                {"id": "th5_b42", "num": 42, "name": "Bài 42: Thể tích hình lập phương"},
                {"id": "th5_b43", "num": 43, "name": "Bài 43: Giới thiệu hình trụ"},
                {"id": "th5_b44", "num": 44, "name": "Bài 44: Luyện tập chung Chủ đề 8", "isReview": True}
            ]
        },
        {
            "id": "th5_ch9",
            "title": "Chủ đề 9: Số đo thời gian. Vận tốc, quãng đường, thời gian",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b45", "num": 45, "name": "Bài 45: Bảng đơn vị đo thời gian"},
                {"id": "th5_b46", "num": 46, "name": "Bài 46: Cộng, trừ số đo thời gian"},
                {"id": "th5_b47", "num": 47, "name": "Bài 47: Nhân, chia số đo thời gian với một số"},
                {"id": "th5_b48", "num": 48, "name": "Bài 48: Vận tốc"},
                {"id": "th5_b49", "num": 49, "name": "Bài 49: Quãng đường"},
                {"id": "th5_b50", "num": 50, "name": "Bài 50: Thời gian"},
                {"id": "th5_b51", "num": 51, "name": "Bài 51: Bài toán chuyển động đều"},
                {"id": "th5_b52", "num": 52, "name": "Bài 52: Luyện tập chung Chủ đề 9", "isReview": True}
            ]
        },
        {
            "id": "th5_ch10",
            "title": "Chủ đề 10: Một số yếu tố thống kê và xác suất",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b53", "num": 53, "name": "Bài 53: Biểu đồ hình quạt tròn"},
                {"id": "th5_b54", "num": 54, "name": "Bài 54: Tỉ số mô tả số lần lặp lại của một khả năng xảy ra"},
                {"id": "th5_b55", "num": 55, "name": "Bài 55: Luyện tập chung Chủ đề 10", "isReview": True}
            ]
        },
        {
            "id": "th5_ch11",
            "title": "Chủ đề 11: Ôn tập cuối năm",
            "term": "hk2",
            "lessons": [
                {"id": "th5_b56", "num": 56, "name": "Bài 56: Ôn tập về số tự nhiên, phân số, số thập phân"},
                {"id": "th5_b57", "num": 57, "name": "Bài 57: Ôn tập các phép tính với số đo đại lượng"},
                {"id": "th5_b58", "num": 58, "name": "Bài 58: Ôn tập hình học và đo lường"},
                {"id": "th5_b59", "num": 59, "name": "Bài 59: Ôn tập toán chuyển động đều"},
                {"id": "th5_b60", "num": 60, "name": "Bài 60: Ôn tập chung toàn diện", "isReview": True}
            ]
        }
    ]
}

if __name__ == "__main__":
    print(f"Tổng số chủ đề: {len(TIEUHOC_CURRICULUM['chapters'])}")
    total_lessons = sum(len(c['lessons']) for c in TIEUHOC_CURRICULUM['chapters'])
    print(f"Tổng số bài học: {total_lessons}")
    print(f"Đợt kiểm tra định kỳ: {len(TIEUHOC_CURRICULUM['periodic']['terms'])}")
