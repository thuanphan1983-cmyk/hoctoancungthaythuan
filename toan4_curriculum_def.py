# -*- coding: utf-8 -*-
"""
ĐỊNH NGHĨA KHUNG CHƯƠNG TRÌNH TOÁN TIỂU HỌC (LỚP 4 - BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG)
Bao gồm:
1. Đề kiểm tra định kỳ: GK1 (8 đề), CK1 (8 đề), GK2 (8 đề), CK2 (8 đề) -> 32 đề
2. Đề kiểm tra theo bài học SGK: 63 bài học (mỗi bài có 3 đề độc lập: 6 TN + 6 TL)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

TOAN4_CURRICULUM = {
    "grade": "4",
    "gradeName": "Lớp 4",
    "subject": "math",
    "subjectName": "Toán học",
    "bookSeries": "Kết nối tri thức với cuộc sống",
    "periodic": {
        "title": "Hệ thống Đề kiểm tra định kỳ Toán 4",
        "terms": [
            {
                "id": "th4_gk1",
                "code": "GK1",
                "name": "Kiểm tra Giữa học kì 1",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Số có sáu chữ số, hàng và lớp; Làm tròn số; Góc nhọn, góc tù, góc bẹt; Đơn vị đo: yến, tạ, tấn, giây, thế kỉ; Đọc và biểu diễn bảng số liệu",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th4_ck1",
                "code": "CK1",
                "name": "Kiểm tra Cuối học kì 1",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Các phép tính cộng, trừ số có nhiều chữ số; Tính chất giao hoán, kết hợp; Tìm hai số khi biết tổng và hiệu; Đường thẳng vuông góc, đường thẳng song song; Nhân với số có 1, 2, 3 chữ số",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th4_gk2",
                "code": "GK2",
                "name": "Kiểm tra Giữa học kì 2",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Phép chia cho số có 1, 2 chữ số; Dấu hiệu chia hết cho 2, 5, 9, 3; Khái niệm phân số, phân số bằng nhau, rút gọn và quy đồng mẫu số các phân số; So sánh phân số",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            },
            {
                "id": "th4_ck2",
                "code": "CK2",
                "name": "Kiểm tra Cuối học kì 2 (Cuối năm)",
                "time": "40 phút",
                "totalTests": 8,
                "scope": "Phép cộng, trừ, nhân, chia phân số; Tìm phân số của một số; Tỉ số, tìm hai số khi biết tổng và tỉ số, hiệu và tỉ số; Đơn vị đo diện tích (dm², m², mm²); Ôn tập tổng hợp",
                "structure": "6 câu Trắc nghiệm khách quan + 6 bài Tự luận (có chừa dòng kẻ làm bài)"
            }
        ]
    },
    "chapters": [
        {
            "id": "th4_ch1",
            "title": "Chủ đề 1: Ôn tập và bổ sung",
            "term": "hk1",
            "lessons": [
                {"id": "th4_b1", "num": 1, "name": "Bài 1: Ôn tập các số đến 100 000"},
                {"id": "th4_b2", "num": 2, "name": "Bài 2: Ôn tập các phép tính trong phạm vi 100 000"},
                {"id": "th4_b3", "num": 3, "name": "Bài 3: Số chẵn, số lẻ"},
                {"id": "th4_b4", "num": 4, "name": "Bài 4: Biểu thức chứa chữ"},
                {"id": "th4_b5", "num": 5, "name": "Bài 5: Giải bài toán có ba bước tính"},
                {"id": "th4_b6", "num": 6, "name": "Bài 6: Luyện tập chung Chủ đề 1", "isReview": True}
            ]
        },
        {
            "id": "th4_ch2",
            "title": "Chủ đề 2: Góc và đơn vị đo góc",
            "term": "hk1",
            "lessons": [
                {"id": "th4_b7", "num": 7, "name": "Bài 7: Đo góc, đơn vị đo góc"},
                {"id": "th4_b8", "num": 8, "name": "Bài 8: Góc nhọn, góc tù, góc bẹt"},
                {"id": "th4_b9", "num": 9, "name": "Bài 9: Luyện tập chung Chủ đề 2", "isReview": True}
            ]
        },
        {
            "id": "th4_ch3",
            "title": "Chủ đề 3: Số có nhiều chữ số",
            "term": "hk1",
            "lessons": [
                {"id": "th4_b10", "num": 10, "name": "Bài 10: Số có sáu chữ số. Số 1 000 000"},
                {"id": "th4_b11", "num": 11, "name": "Bài 11: Hàng và lớp"},
                {"id": "th4_b12", "num": 12, "name": "Bài 12: Các số trong phạm vi lớp triệu"},
                {"id": "th4_b13", "num": 13, "name": "Bài 13: Làm tròn số đến hàng trăm nghìn"},
                {"id": "th4_b14", "num": 14, "name": "Bài 14: So sánh các số có nhiều chữ số"},
                {"id": "th4_b15", "num": 15, "name": "Bài 15: Làm quen với dãy số tự nhiên"},
                {"id": "th4_b16", "num": 16, "name": "Bài 16: Luyện tập chung Chủ đề 3", "isReview": True}
            ]
        },
        {
            "id": "th4_ch4",
            "title": "Chủ đề 4: Một số đơn vị đo đại lượng",
            "term": "hk1",
            "lessons": [
                {"id": "th4_b17", "num": 17, "name": "Bài 17: Yến, tạ, tấn"},
                {"id": "th4_b18", "num": 18, "name": "Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông"},
                {"id": "th4_b19", "num": 19, "name": "Bài 19: Giây, thế kỉ"},
                {"id": "th4_b20", "num": 20, "name": "Bài 20: Luyện tập chung Chủ đề 4", "isReview": True}
            ]
        },
        {
            "id": "th4_ch5",
            "title": "Chủ đề 5: Phép cộng và phép trừ",
            "term": "hk1",
            "lessons": [
                {"id": "th4_b21", "num": 21, "name": "Bài 21: Phép cộng và phép trừ số có nhiều chữ số"},
                {"id": "th4_b22", "num": 22, "name": "Bài 22: Tính chất giao hoán và kết hợp của phép cộng"},
                {"id": "th4_b23", "num": 23, "name": "Bài 23: Tìm hai số khi biết tổng và hiệu của hai số đó"},
                {"id": "th4_b24", "num": 24, "name": "Bài 24: Luyện tập chung Chủ đề 5", "isReview": True}
            ]
        },
        {
            "id": "th4_ch6",
            "title": "Chủ đề 6: Đường thẳng vuông góc. Đường thẳng song song",
            "term": "hk1",
            "lessons": [
                {"id": "th4_b25", "num": 25, "name": "Bài 25: Hai đường thẳng vuông góc"},
                {"id": "th4_b26", "num": 26, "name": "Bài 26: Hai đường thẳng song song"},
                {"id": "th4_b27", "num": 27, "name": "Bài 27: Thực hành vẽ hai đường thẳng vuông góc, song song"},
                {"id": "th4_b28", "num": 28, "name": "Bài 28: Luyện tập chung Chủ đề 6", "isReview": True}
            ]
        },
        {
            "id": "th4_ch7",
            "title": "Chủ đề 7: Ôn tập học kì 1",
            "term": "hk1",
            "lessons": [
                {"id": "th4_b29", "num": 29, "name": "Bài 29: Ôn tập số tự nhiên và các phép tính"},
                {"id": "th4_b30", "num": 30, "name": "Bài 30: Ôn tập hình học và đo lường"},
                {"id": "th4_b31", "num": 31, "name": "Bài 31: Luyện tập chung Học kì 1", "isReview": True}
            ]
        },
        {
            "id": "th4_ch8",
            "title": "Chủ đề 8: Phép nhân và phép chia",
            "term": "hk2",
            "lessons": [
                {"id": "th4_b32", "num": 32, "name": "Bài 32: Nhân với số có một chữ số"},
                {"id": "th4_b33", "num": 33, "name": "Bài 33: Tính chất giao hoán và kết hợp của phép nhân"},
                {"id": "th4_b34", "num": 34, "name": "Bài 34: Nhân với 10, 100, 1000... hoặc số tròn chục, tròn trăm"},
                {"id": "th4_b35", "num": 35, "name": "Bài 35: Nhân với số có hai chữ số"},
                {"id": "th4_b36", "num": 36, "name": "Bài 36: Chia cho số có một chữ số"},
                {"id": "th4_b37", "num": 37, "name": "Bài 37: Chia cho 10, 100, 1000... Chia cho số tròn chục, tròn trăm"},
                {"id": "th4_b38", "num": 38, "name": "Bài 38: Chia cho số có hai chữ số"},
                {"id": "th4_b39", "num": 39, "name": "Bài 39: Luyện tập chung Chủ đề 8", "isReview": True}
            ]
        },
        {
            "id": "th4_ch9",
            "title": "Chủ đề 9: Làm quen với yếu tố thống kê, xác suất",
            "term": "hk2",
            "lessons": [
                {"id": "th4_b40", "num": 40, "name": "Bài 40: Dãy số liệu thống kê"},
                {"id": "th4_b41", "num": 41, "name": "Bài 41: Biểu đồ cột"},
                {"id": "th4_b42", "num": 42, "name": "Bài 42: Số lần lặp lại của một khả năng xảy ra"},
                {"id": "th4_b43", "num": 43, "name": "Bài 43: Luyện tập chung Chủ đề 9", "isReview": True}
            ]
        },
        {
            "id": "th4_ch10",
            "title": "Chủ đề 10: Phân số",
            "term": "hk2",
            "lessons": [
                {"id": "th4_b44", "num": 44, "name": "Bài 44: Khái niệm phân số"},
                {"id": "th4_b45", "num": 45, "name": "Bài 45: Phân số và phép chia số tự nhiên"},
                {"id": "th4_b46", "num": 46, "name": "Bài 46: Tính chất cơ bản của phân số"},
                {"id": "th4_b47", "num": 47, "name": "Bài 47: Rút gọn phân số"},
                {"id": "th4_b48", "num": 48, "name": "Bài 48: Quy đồng mẫu số các phân số"},
                {"id": "th4_b49", "num": 49, "name": "Bài 49: So sánh hai phân số"},
                {"id": "th4_b50", "num": 50, "name": "Bài 50: Luyện tập chung Chủ đề 10", "isReview": True}
            ]
        },
        {
            "id": "th4_ch11",
            "title": "Chủ đề 11: Phép cộng, phép trừ phân số",
            "term": "hk2",
            "lessons": [
                {"id": "th4_b51", "num": 51, "name": "Bài 51: Phép cộng phân số cùng mẫu số và khác mẫu số"},
                {"id": "th4_b52", "num": 52, "name": "Bài 52: Phép trừ phân số cùng mẫu số và khác mẫu số"},
                {"id": "th4_b53", "num": 53, "name": "Bài 53: Tính chất phép cộng và phép trừ phân số"},
                {"id": "th4_b54", "num": 54, "name": "Bài 54: Luyện tập chung Chủ đề 11", "isReview": True}
            ]
        },
        {
            "id": "th4_ch12",
            "title": "Chủ đề 12: Phép nhân, phép chia phân số",
            "term": "hk2",
            "lessons": [
                {"id": "th4_b55", "num": 55, "name": "Bài 55: Phép nhân phân số"},
                {"id": "th4_b56", "num": 56, "name": "Bài 56: Phép chia phân số"},
                {"id": "th4_b57", "num": 57, "name": "Bài 57: Tìm phân số của một số"},
                {"id": "th4_b58", "num": 58, "name": "Bài 58: Luyện tập chung Chủ đề 12", "isReview": True}
            ]
        },
        {
            "id": "th4_ch13",
            "title": "Chủ đề 13: Ôn tập cuối năm",
            "term": "hk2",
            "lessons": [
                {"id": "th4_b59", "num": 59, "name": "Bài 59: Ôn tập số tự nhiên và phân số"},
                {"id": "th4_b60", "num": 60, "name": "Bài 60: Ôn tập các phép tính với số tự nhiên và phân số"},
                {"id": "th4_b61", "num": 61, "name": "Bài 61: Ôn tập hình học và đo lường"},
                {"id": "th4_b62", "num": 62, "name": "Bài 62: Ôn tập một số yếu tố thống kê và xác suất"},
                {"id": "th4_b63", "num": 63, "name": "Bài 63: Luyện tập chung cuối năm", "isReview": True}
            ]
        }
    ]
}

if __name__ == "__main__":
    print(f"Tổng số chủ đề Toán 4: {len(TOAN4_CURRICULUM['chapters'])}")
    total_l = sum(len(c['lessons']) for c in TOAN4_CURRICULUM['chapters'])
    print(f"Tổng số bài học Toán 4: {total_l}")
    print(f"Kỳ kiểm tra định kỳ: {len(TOAN4_CURRICULUM['periodic']['terms'])}")
