# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - VẬT LÝ 7 (CHUẨN 100% ĐỘC LẬP - BÁM SÁT SGK KẾT NỐI TRI THỨC)
Tất cả 59 đề thi trên 17 bài học hoàn toàn độc lập 100% về câu hỏi, số liệu và đáp án.
ZERO câu hỏi trùng lặp giữa các đề trong cùng bài học.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

true = True
false = False
null = None

PHYS7_EXAMS = {
  "phys7_c3_b8_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 8: Tốc độ chuyển động - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b8",
    "lessonName": "Bài 8: Tốc độ chuyển động",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tốc độ chuyển động của một vật cho biết:",
        "options": [
          "Mức độ nhanh hay chậm của chuyển động",
          "Quãng đường dài hay ngắn mà vật đã đi",
          "Thời gian vật thực hiện chuyển động",
          "Hướng chuyển động của vật trong không gian"
        ],
        "correct": 0,
        "explanation": "Tốc độ là đại lượng đặc trưng cho mức độ nhanh hay chậm của chuyển động."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Công thức tính tốc độ khi biết quãng đường s và thời gian t là:",
        "options": [
          "v = s / t",
          "v = s × t",
          "v = t / s",
          "v = s + t"
        ],
        "correct": 0,
        "explanation": "Công thức tính tốc độ: v = s / t."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Đơn vị hợp pháp để đo tốc độ trong hệ đơn vị đo lường quốc tế (SI) là:",
        "options": [
          "Mét trên giây (m/s)",
          "Kilômét trên giờ (km/h)",
          "Centimét trên giây (cm/s)",
          "Milimét trên phút (mm/min)"
        ],
        "correct": 0,
        "explanation": "Trong hệ SI, đơn vị hợp pháp của tốc độ là mét trên giây (m/s)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Thiết bị đo gắn trực tiếp trên bảng điều khiển xe máy, ô tô để hiển thị tốc độ tức thời là:",
        "options": [
          "Tốc kế (speedometer)",
          "Nhiệt kế",
          "Vôn kế",
          "Ampe kế"
        ],
        "correct": 0,
        "explanation": "Tốc kế dùng để đo trực tiếp tốc độ chuyển động tức thời của phương tiện."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tốc độ truyền ánh sáng trong môi trường chân không xấp xỉ bằng:",
        "options": [
          "300.000 km/s",
          "340 m/s",
          "1.500 m/s",
          "1.000 km/h"
        ],
        "correct": 0,
        "explanation": "Tốc độ ánh sáng trong chân không là c ≈ 300.000 km/s = 3.10^8 m/s."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Chuyển động đều là chuyển động có đặc điểm nào sau đây?",
        "options": [
          "Tốc độ có độ lớn không đổi theo thời gian",
          "Tốc độ tăng dần đều đặn",
          "Tốc độ giảm dần về 0",
          "Quãng đường đi được luôn bằng 0"
        ],
        "correct": 0,
        "explanation": "Chuyển động đều là chuyển động có tốc độ không thay đổi theo thời gian."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Đổi 36 km/h sang đơn vị m/s ta được kết quả là:",
        "options": [
          "10 m/s",
          "3,6 m/s",
          "100 m/s",
          "360 m/s"
        ],
        "correct": 0,
        "explanation": "1 km/h = 1/3,6 m/s => 36 km/h = 36 / 3,6 = 10 m/s."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một người đi xe đạp đi được quãng đường 12 km trong thời gian 40 phút. Tốc độ của người đó là:",
        "options": [
          "18 km/h",
          "12 km/h",
          "15 km/h",
          "20 km/h"
        ],
        "correct": 0,
        "explanation": "40 phút = 2/3 giờ. v = 12 / (2/3) = 18 km/h."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một ô tô chạy trên cao tốc với tốc độ 90 km/h. Trong thời gian 20 phút, xe đi được quãng đường là:",
        "options": [
          "30 km",
          "45 km",
          "18 km",
          "25 km"
        ],
        "correct": 0,
        "explanation": "20 phút = 1/3 h. s = 90 × (1/3) = 30 km."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Vận động viên điền kinh hoàn thành cự li chạy 100 m trong thời gian 10 giây. Tốc độ trung bình là:",
        "options": [
          "10 m/s",
          "1 m/s",
          "100 m/s",
          "36 m/s"
        ],
        "correct": 0,
        "explanation": "v = s / t = 100 / 10 = 10 m/s."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Trong các phương tiện sau, phương tiện nào có tốc độ chuyển động trung bình lớn nhất?",
        "options": [
          "Máy bay thương mại phản lực",
          "Tàu hỏa thông thường",
          "Xe ô tô con trên quốc lộ",
          "Xe máy phân khối lớn"
        ],
        "correct": 0,
        "explanation": "Máy bay thương mại phản lực bay khoảng 800 - 900 km/h, lớn nhất trong các phương tiện trên."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hai người cùng xuất phát đi bộ trên một đoạn đường dài 1,2 km. Người A mất 15 phút, người B mất 20 phút. Nhận xét nào đúng?",
        "options": [
          "Người A chuyển động nhanh hơn người B",
          "Người B chuyển động nhanh hơn người A",
          "Hai người chuyển động nhanh như nhau",
          "Không thể so sánh được"
        ],
        "correct": 0,
        "explanation": "Cùng quãng đường, người A mất ít thời gian hơn nên đi nhanh hơn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các đơn vị và quy tắc chuyển đổi của tốc độ chuyển động:",
        "statements": [
          {
            "subId": "a",
            "text": "1 m/s tương đương với 3,6 km/h.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đơn vị km/h thường dùng trong giao thông đường bộ ở nước ta.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Để đổi từ m/s sang km/h ta lấy giá trị nhân với 3,6.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ 15 m/s nhỏ hơn tốc độ 40 km/h.",
            "correct": false
          }
        ],
        "explanation": "15 m/s = 54 km/h > 40 km/h."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét tính chất của các chuyển động trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Chuyển động của đầu kim đồng hồ chạy bình thường là chuyển động đều.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chuyển động của xe buýt khi đón và trả khách là chuyển động không đều.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc kế trên xe máy hiển thị tốc độ trung bình của cả chuyến đi.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khi đạp xe lên dốc, tốc độ của xe thường giảm dần.",
            "correct": true
          }
        ],
        "explanation": "Tốc kế hiển thị tốc độ tức thời tại thời điểm đang chạy, không phải tốc độ trung bình."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một xe khách đi từ bến A đến bến B dài 120 km trong thời gian 2,5 giờ, sau đó dừng nghỉ 30 phút rồi đi tiếp 60 km trong 1 giờ:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc độ của xe ở chặng đầu tiên là 48 km/h.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ của xe ở chặng thứ hai là 60 km/h.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tổng quãng đường xe đã đi là 180 km.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình trên toàn bộ chuyến đi kể cả thời gian nghỉ là 50 km/h.",
            "correct": false
          }
        ],
        "explanation": "v1 = 120 / 2,5 = 48 km/h. v2 = 60 / 1 = 60 km/h. Tổng thời gian cả nghỉ = 2,5 + 0,5 + 1 = 4h => v_tb = 180 / 4 = 45 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Vận động viên bơi lội tập luyện trong hồ bơi tiêu chuẩn dài 50 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Lượt đi 50 m mất 25 giây, tốc độ bơi là 2 m/s.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ 2 m/s tương đương với 7,2 km/h.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Lượt về 50 m mất 30 giây, tốc độ lượt về nhanh hơn lượt đi.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình cả đi và về là xấp xỉ 1,82 m/s.",
            "correct": true
          }
        ],
        "explanation": "Lượt về v = 50 / 30 = 1,67 m/s chậm hơn lượt đi 2 m/s. v_tb = 100 / 55 ≈ 1,82 m/s."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đổi 54 km/h sang đơn vị m/s ta được kết quả là bao nhiêu?",
        "correctAnswer": "15",
        "explanation": "54 / 3,6 = 15 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một người chạy bộ cự li 200 m trong 25 giây. Tốc độ chạy của người đó là bao nhiêu m/s?",
        "correctAnswer": "8",
        "explanation": "v = 200 / 25 = 8 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một ô tô chạy trên cao tốc với tốc độ 90 km/h. Trong thời gian 2 giờ, ô tô đi được quãng đường bao nhiêu km?",
        "correctAnswer": "180",
        "explanation": "s = 90 × 2 = 180 km."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một ca nô chuyển động với tốc độ 30 km/h. Để đi hết khúc sông dài 45 km, ca nô mất thời gian bao nhiêu giờ? (Viết dưới dạng số thập phân)",
        "correctAnswer": "1.5",
        "explanation": "t = 45 / 30 = 1,5 h."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Xe buýt đi từ bến A đến bến B dài 24 km hết 40 phút. Tốc độ trung bình của xe buýt là bao nhiêu km/h?",
        "correctAnswer": "36",
        "explanation": "40 phút = 2/3 h. v = 24 / (2/3) = 36 km/h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một vận động viên trượt băng di chuyển với tốc độ đều 12 m/s. Trong 15 giây, quãng đường trượt được là bao nhiêu mét?",
        "correctAnswer": "180",
        "explanation": "s = 12 × 15 = 180 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hai xe máy xuất phát cùng một lúc từ hai địa điểm A và B cách nhau 120 km đi ngược chiều để gặp nhau. Xe từ A chạy với tốc độ 35 km/h, xe từ B chạy với tốc độ 25 km/h. Sau bao lâu kể từ lúc xuất phát thì hai xe gặp nhau?",
        "options": [
          "2 giờ",
          "1,5 giờ",
          "2,5 giờ",
          "3 giờ"
        ],
        "correct": 0,
        "explanation": "Thời gian gặp nhau: t = s / (v1 + v2) = 120 / (35 + 25) = 2 giờ."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Đoàn tàu hỏa dài 120 m vượt qua một cây cầu dài 480 m với tốc độ không đổi 36 km/h (10 m/s). Thời gian từ lúc đầu tàu bắt đầu đi vào cầu đến lúc toa cuối cùng rời khỏi cầu là bao nhiêu giây?",
        "options": [
          "60 giây",
          "48 giây",
          "12 giây",
          "50 giây"
        ],
        "correct": 0,
        "explanation": "Tổng quãng đường tàu đi để qua hết cầu: s = 480 + 120 = 600 m. t = 600 / 10 = 60 s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một người đi xe đạp trên đoạn đường dốc. Nửa quãng đường đầu người đó đi với tốc độ 12 km/h, nửa quãng đường sau đi với tốc độ 24 km/h. Tốc độ trung bình của người đó trên toàn bộ quãng đường là:",
        "options": [
          "16 km/h",
          "18 km/h",
          "20 km/h",
          "15 km/h"
        ],
        "correct": 0,
        "explanation": "v_tb = 2v1v2 / (v1 + v2) = 2 × 12 × 24 / (12 + 24) = 576 / 36 = 16 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một chiếc thuyền máy chạy xuôi dòng một khúc sông dài 36 km mất 1,5 giờ, sau đó ngược dòng trở về mất 2 giờ. Biết công suất động cơ không đổi, tốc độ của dòng nước so với bờ sông là:",
        "options": [
          "3 km/h",
          "21 km/h",
          "4 km/h",
          "1,5 km/h"
        ],
        "correct": 0,
        "explanation": "v_xuôi = 36 / 1,5 = 24 km/h; v_ngược = 36 / 2 = 18 km/h. v_nước = (24 - 18) / 2 = 3 km/h."
      }
    ]
  },
  "phys7_c3_b8_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 8: Tốc độ chuyển động - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b8",
    "lessonName": "Bài 8: Tốc độ chuyển động",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Muốn so sánh hai chuyển động xem chuyển động nào nhanh hơn, người ta dựa vào:",
        "options": [
          "Quãng đường đi được trong cùng một khoảng thời gian",
          "Chiều dài của đường đi",
          "Thời điểm bắt đầu xuất phát",
          "Khối lượng của vật đang chuyển động"
        ],
        "correct": 0,
        "explanation": "So sánh quãng đường vật đi được trong cùng một đơn vị thời gian (tốc độ)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Thương số giữa quãng đường s và khoảng thời gian t đi hết quãng đường đó gọi là:",
        "options": [
          "Tốc độ chuyển động",
          "Gia tốc chuyển động",
          "Lực tác dụng",
          "Độ dời vị trí"
        ],
        "correct": 0,
        "explanation": "Thương số s/t là tốc độ chuyển động."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Kí hiệu của tốc độ trong các công thức vật lý thường dùng là:",
        "options": [
          "v",
          "s",
          "t",
          "m"
        ],
        "correct": 0,
        "explanation": "Tốc độ kí hiệu là v (velocity/speed)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Đơn vị nào sau đây KHÔNG phải là đơn vị đo tốc độ?",
        "options": [
          "m.s",
          "m/s",
          "km/h",
          "cm/s"
        ],
        "correct": 0,
        "explanation": "m.s là tích của mét và giây, không phải đơn vị tốc độ."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tốc độ âm thanh truyền trong không khí ở nhiệt độ phòng (20 °C) xấp xỉ khoảng:",
        "options": [
          "340 m/s",
          "300.000 km/s",
          "1.500 m/s",
          "100 km/h"
        ],
        "correct": 0,
        "explanation": "Tốc độ âm trong không khí ở 20 °C là khoảng 340 m/s."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Chuyển động có tốc độ thay đổi liên tục theo thời gian được gọi là:",
        "options": [
          "Chuyển động không đều",
          "Chuyển động đều",
          "Chuyển động đứng yên",
          "Chuyển động tuần hoàn đều"
        ],
        "correct": 0,
        "explanation": "Chuyển động có tốc độ biến đổi gọi là chuyển động không đều."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Đổi 15 m/s sang đơn vị km/h ta được kết quả là:",
        "options": [
          "54 km/h",
          "15 km/h",
          "36 km/h",
          "45 km/h"
        ],
        "correct": 0,
        "explanation": "15 × 3,6 = 54 km/h."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một con báo săn mồi chạy với tốc độ 108 km/h. Tốc độ này tính theo đơn vị m/s là:",
        "options": [
          "30 m/s",
          "36 m/s",
          "25 m/s",
          "40 m/s"
        ],
        "correct": 0,
        "explanation": "108 / 3,6 = 30 m/s."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một người đi bộ đi được quãng đường 600 m trong 5 phút. Tốc độ đi bộ của người đó là:",
        "options": [
          "2 m/s",
          "120 m/s",
          "0,5 m/s",
          "5 m/s"
        ],
        "correct": 0,
        "explanation": "5 phút = 300 s. v = 600 / 300 = 2 m/s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Một máy bay bay từ Hà Nội vào Đà Nẵng dài 600 km hết 45 phút (0,75 giờ). Tốc độ của máy bay là:",
        "options": [
          "800 km/h",
          "600 km/h",
          "750 km/h",
          "900 km/h"
        ],
        "correct": 0,
        "explanation": "v = 600 / 0,75 = 800 km/h."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Xe máy chạy với tốc độ 48 km/h. Để đi quãng đường 72 km, xe máy cần thời gian là:",
        "options": [
          "1,5 giờ",
          "2,0 giờ",
          "1,2 giờ",
          "1,8 giờ"
        ],
        "correct": 0,
        "explanation": "t = s / v = 72 / 48 = 1,5 giờ."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hiện tượng nhìn thấy tia sét trước khi nghe thấy tiếng sấm là do:",
        "options": [
          "Tốc độ ánh sáng lớn hơn rất nhiều tốc độ âm thanh",
          "Tia sét xảy ra trước tiếng sấm một khoảng thời gian",
          "Mắt người nhìn nhanh hơn tai người nghe",
          "Âm thanh bị cản trở bởi mây"
        ],
        "correct": 0,
        "explanation": "Tốc độ ánh sáng (300.000 km/s) lớn hơn rất nhiều tốc độ âm thanh (340 m/s)."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét mối quan hệ giữa các đại lượng s, v và t trong chuyển động:",
        "statements": [
          {
            "subId": "a",
            "text": "Với cùng một quãng đường, thời gian chuyển động tỉ lệ nghịch với tốc độ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong cùng một khoảng thời gian, quãng đường đi được tỉ lệ thuận với tốc độ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Công thức xác định thời gian chuyển động là t = v / s.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Nếu tăng tốc độ lên gấp đôi thì thời gian đi hết cùng một quãng đường sẽ giảm một nửa.",
            "correct": true
          }
        ],
        "explanation": "Công thức đúng là t = s / v, câu c sai."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét chuyển động của các phương tiện trong giao thông thực tế:",
        "statements": [
          {
            "subId": "a",
            "text": "Xe chạy trên đường cao tốc thường duy trì tốc độ cao và ổn định hơn trong nội đô.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi qua khúc cua hoặc ngã tư, tài xế phải giảm tốc độ để đảm bảo an toàn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ trung bình trên cả hành trình luôn luôn bằng trung bình cộng vận tốc đầu và vận tốc cuối.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tốc độ tức thời là tốc độ tại một thời điểm hoặc một vị trí xác định.",
            "correct": true
          }
        ],
        "explanation": "Tốc độ trung bình bằng tổng quãng đường chia cho tổng thời gian, không đơn thuần là trung bình cộng hai vận tốc."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một người đạp xe đường trường thực hiện lộ trình qua hai đoạn đường:",
        "statements": [
          {
            "subId": "a",
            "text": "Đoạn 1 leo dốc dài 10 km chạy với tốc độ 15 km/h mất 40 phút.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đoạn 2 đổ dốc dài 15 km chạy với tốc độ 45 km/h mất 20 phút.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tổng thời gian đi hết cả hai đoạn dốc là 1 giờ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình trên toàn tuyến đường bằng 30 km/h.",
            "correct": false
          }
        ],
        "explanation": "Tổng quãng đường = 10 + 15 = 25 km, tổng thời gian = 40p + 20p = 1h => v_tb = 25 / 1 = 25 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Đội tuyển chạy tiếp sức 4 x 100 m nam của trường tham gia thi đấu:",
        "statements": [
          {
            "subId": "a",
            "text": "Tổng cự li mà cả 4 thành viên hoàn thành là 400 m.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian thi đấu của toàn đội là 48 giây.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ trung bình của đội đạt xấp xỉ 8,33 m/s.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Cả 4 vận động viên đều chạy với tốc độ hoàn toàn giống nhau ở mọi thời điểm.",
            "correct": false
          }
        ],
        "explanation": "Mỗi vận động viên có thể lực và tốc độ xuất phát, bứt tốc khác nhau."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đổi 72 km/h sang đơn vị m/s được kết quả là bao nhiêu?",
        "correctAnswer": "20",
        "explanation": "72 / 3,6 = 20 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Vận động viên bơi cự li 100 m mất thời gian 50 giây. Tốc độ bơi trung bình là bao nhiêu m/s?",
        "correctAnswer": "2",
        "explanation": "v = 100 / 50 = 2 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tàu hỏa chạy đều với tốc độ 45 km/h trong thời gian 3 giờ. Quãng đường tàu đi được là bao nhiêu km?",
        "correctAnswer": "135",
        "explanation": "s = 45 × 3 = 135 km."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Chiếc xe máy đi quãng đường 60 km hết 1,2 giờ. Tốc độ của xe máy là bao nhiêu km/h?",
        "correctAnswer": "50",
        "explanation": "v = 60 / 1,2 = 50 km/h."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Ánh sáng truyền từ Mặt Trời đến Trái Đất mất khoảng 500 giây với tốc độ 300.000 km/s. Khoảng cách đó bằng bao nhiêu triệu km?",
        "correctAnswer": "150",
        "explanation": "s = 300.000 × 500 = 150.000.000 km = 150 triệu km."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một con tàu vũ trụ chuyển động với tốc độ 8 km/s. Trong thời gian 1 phút, con tàu đi được quãng đường bao nhiêu km?",
        "correctAnswer": "480",
        "explanation": "1 phút = 60 s. s = 8 × 60 = 480 km."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hai xe ô tô cùng khởi hành lúc 6h00 sáng từ hai địa điểm A và B cách nhau 120 km đi cùng chiều nhau (xe từ A đuổi theo xe từ B). Xe A chạy với tốc độ 60 km/h, xe B chạy với tốc độ 40 km/h. Hai xe gặp nhau vào thời điểm nào trong ngày?",
        "options": [
          "12h00 trưa",
          "11h00 trưa",
          "10h30 sáng",
          "14h00 chiều"
        ],
        "correct": 0,
        "explanation": "Thời gian đuổi kịp: t = 120 / (60 - 40) = 6 giờ. Thời điểm gặp nhau: 6h00 + 6h = 12h00."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một tài xế lái ô tô đi 1/3 quãng đường đầu với tốc độ 30 km/h và 2/3 quãng đường còn lại với tốc độ 60 km/h. Tốc độ trung bình của ô tô trên cả chặng đường là:",
        "options": [
          "45 km/h",
          "50 km/h",
          "40 km/h",
          "48 km/h"
        ],
        "correct": 0,
        "explanation": "t1 = (s/3)/30 = s/90; t2 = (2s/3)/60 = s/90. Tổng t = 2s/90 = s/45 => v_tb = s / (s/45) = 45 km/h."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một người đứng bên đường ray quan sát thấy một đoàn tàu hỏa chạy qua trước mặt mình mất 12 giây. Biết đoàn tàu dài 180 m. Tốc độ chuyển động của đoàn tàu tính ra km/h là:",
        "options": [
          "54 km/h",
          "36 km/h",
          "60 km/h",
          "72 km/h"
        ],
        "correct": 0,
        "explanation": "v = 180 / 12 = 15 m/s = 15 × 3,6 = 54 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người bơi xuôi dòng nước từ bến A đến bến B mất 40 phút và bơi ngược dòng từ B về A mất 60 phút. Nếu người đó thả trôi theo dòng nước từ A đến B thì mất thời gian bao nhiêu phút?",
        "options": [
          "240 phút",
          "100 phút",
          "120 phút",
          "180 phút"
        ],
        "correct": 0,
        "explanation": "1/t_xuôi = 1/40; 1/t_ngược = 1/60 => 1/t_nước = (1/40 - 1/60)/2 = (1/120)/2 = 1/240 => t_trôi = 240 phút."
      }
    ]
  },
  "phys7_c3_b8_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 8: Tốc độ chuyển động - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b8",
    "lessonName": "Bài 8: Tốc độ chuyển động",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Để xác định tốc độ chuyển động của một vật, ta cần đo hai đại lượng nào?",
        "options": [
          "Quãng đường và thời gian",
          "Khối lượng và thể tích",
          "Nhiệt độ và áp suất",
          "Chiều dài và diện tích"
        ],
        "correct": 0,
        "explanation": "Cần đo quãng đường vật đi được và thời gian đi hết quãng đường đó."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong các công thức sau, công thức nào dùng để tính thời gian chuyển động?",
        "options": [
          "t = s / v",
          "t = s × v",
          "t = v / s",
          "t = v - s"
        ],
        "correct": 0,
        "explanation": "Thời gian chuyển động: t = s / v."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nói tốc độ của ô tô là 60 km/h, điều đó có ý nghĩa là:",
        "options": [
          "Nếu giữ nguyên tốc độ, trong 1 giờ ô tô sẽ đi được 60 km",
          "Ô tô luôn đi được đúng 60 km trong mọi trường hợp",
          "Ô tô chỉ có thể chạy trong vòng 1 giờ",
          "Ô tô đã đi được quãng đường dài 60 km"
        ],
        "correct": 0,
        "explanation": "Tốc độ 60 km/h nghĩa là mỗi giờ xe đi được 60 km nếu chuyển động đều."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Đơn vị đo tốc độ thường dùng trong ngành hàng hải và hàng không quốc tế là:",
        "options": [
          "Hải lí trên giờ (nút - knot)",
          "Mét trên phút",
          "Kilômét trên giây",
          "Dặm trên giây"
        ],
        "correct": 0,
        "explanation": "Nút (knot) là đơn vị đo tốc độ bằng 1 hải lí/giờ (xấp xỉ 1,852 km/h)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tốc độ chuyển động của Trái Đất quay xung quanh Mặt Trời xấp xỉ khoảng:",
        "options": [
          "30 km/s",
          "300 m/s",
          "300.000 km/s",
          "100 km/h"
        ],
        "correct": 0,
        "explanation": "Trái Đất quay quanh Mặt Trời với tốc độ khoảng 29,8 km/s ≈ 30 km/s."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Chuyển động của một hòn đá rơi tự do từ trên cao xuống đất có tốc độ:",
        "options": [
          "Tăng dần theo thời gian",
          "Không đổi theo thời gian",
          "Giảm dần về 0",
          "Luôn bằng 0"
        ],
        "correct": 0,
        "explanation": "Vật rơi tự do chuyển động nhanh dần đều dưới tác dụng của trọng lực."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Đổi 12 m/s sang đơn vị km/h ta được kết quả là:",
        "options": [
          "43,2 km/h",
          "36,0 km/h",
          "24,0 km/h",
          "48,5 km/h"
        ],
        "correct": 0,
        "explanation": "12 × 3,6 = 43,2 km/h."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một người đi xe đạp đi quãng đường 6 km trong thời gian 24 phút. Tốc độ của người đó là:",
        "options": [
          "15 km/h",
          "12 km/h",
          "18 km/h",
          "20 km/h"
        ],
        "correct": 0,
        "explanation": "24 phút = 0,4 h. v = 6 / 0,4 = 15 km/h."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một xe tải chạy trên quốc lộ với tốc độ 60 km/h. Trong thời gian 45 phút, xe tải đi được:",
        "options": [
          "45 km",
          "40 km",
          "50 km",
          "30 km"
        ],
        "correct": 0,
        "explanation": "45 phút = 0,75 h. s = 60 × 0,75 = 45 km."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Để đi hết quãng đường 180 km với tốc độ đều 45 km/h, xe ô tô cần khoảng thời gian là:",
        "options": [
          "4 giờ",
          "3,5 giờ",
          "5 giờ",
          "4,5 giờ"
        ],
        "correct": 0,
        "explanation": "t = s / v = 180 / 45 = 4 giờ."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Chim cắt cổ điển lao xuống săn mồi có thể đạt tốc độ 324 km/h. Tốc độ này tính theo m/s là:",
        "options": [
          "90 m/s",
          "80 m/s",
          "100 m/s",
          "75 m/s"
        ],
        "correct": 0,
        "explanation": "324 / 3,6 = 90 m/s."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một người đi xe máy đi 20 km đầu hết 30 phút, 15 km sau hết 20 phút. Tốc độ trung bình trên toàn tuyến là:",
        "options": [
          "42 km/h",
          "35 km/h",
          "40 km/h",
          "45 km/h"
        ],
        "correct": 0,
        "explanation": "Tổng s = 35 km, tổng t = 50 phút = 5/6 h => v_tb = 35 / (5/6) = 42 km/h."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về bản chất và phương pháp xác định tốc độ:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc độ trung bình phản ánh mức độ nhanh chậm tính chung cho cả một quãng đường.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ tức thời có thể thay đổi liên tục trên từng đoạn đường nhỏ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi vật chuyển động đều, tốc độ tức thời tại mọi điểm đều bằng tốc độ trung bình.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ của vật chuyển động không bao giờ phụ thuộc vào mốc thời gian đã chọn.",
            "correct": true
          }
        ],
        "explanation": "Các ý đều chính xác về mặt định nghĩa vật lý."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "So sánh tốc độ chuyển động trong thế giới tự nhiên và kĩ thuật:",
        "statements": [
          {
            "subId": "a",
            "text": "Tàu đệm từ Maglev có thể chạy với tốc độ trên 500 km/h.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Vệ tinh nhân tạo bay quanh Trái Đất có tốc độ vũ trụ cấp 1 xấp xỉ 7,9 km/s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Người đi bộ thông thường có tốc độ khoảng 4 đến 5 m/s.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Vận động viên điền kinh chạy cự li ngắn 100 m có thể đạt tốc độ trên 10 m/s.",
            "correct": true
          }
        ],
        "explanation": "Người đi bộ thông thường chỉ có tốc độ khoảng 1,2 đến 1,4 m/s (4 đến 5 km/h), không phải 4 đến 5 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Chuyến hành trình của một gia đình đi ô tô từ Hà Nội về quê nghỉ mát:",
        "statements": [
          {
            "subId": "a",
            "text": "Gia đình xuất phát lúc 6h30 và đến nơi lúc 9h00, tổng thời gian là 2,5 giờ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Quãng đường cả chuyến đi dài 125 km.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ trung bình tính cho cả chuyến đi là 50 km/h.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu gia đình dừng ăn sáng mất 30 phút giữa đường, tốc độ xe chạy thực tế là 62,5 km/h.",
            "correct": true
          }
        ],
        "explanation": "Thời gian xe thực sự lăn bánh = 2,5 - 0,5 = 2h => v_thực = 125 / 2 = 62,5 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Thang máy của tòa chung cư 30 tầng hoạt động phục vụ cư dân:",
        "statements": [
          {
            "subId": "a",
            "text": "Thang máy đi từ tầng 1 lên tầng 30 có độ cao 90 m mất thời gian 30 giây.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ trung bình của thang máy là 3 m/s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trong suốt hành trình di chuyển, thang máy luôn chuyển động đều tuyệt đối.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tốc độ 3 m/s tương đương với 10,8 km/h.",
            "correct": true
          }
        ],
        "explanation": "Thang máy phải tăng tốc khi khởi hành và giảm tốc khi sắp dừng lại, không thể đều tuyệt đối."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đổi 90 km/h sang đơn vị m/s ta được kết quả là bao nhiêu?",
        "correctAnswer": "25",
        "explanation": "90 / 3,6 = 25 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một người chạy bộ 1500 m trong 5 phút (300 s). Tốc độ chạy trung bình là bao nhiêu m/s?",
        "correctAnswer": "5",
        "explanation": "v = 1500 / 300 = 5 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Máy bay chở khách bay với tốc độ 750 km/h trong thời gian 3,2 giờ. Quãng đường bay được là bao nhiêu km?",
        "correctAnswer": "2400",
        "explanation": "s = 750 × 3,2 = 2400 km."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một xe máy đi quãng đường 90 km với tốc độ đều 45 km/h. Thời gian xe đi hết quãng đường là bao nhiêu giờ?",
        "correctAnswer": "2",
        "explanation": "t = 90 / 45 = 2 h."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một giọt mưa rơi đều từ đám mây ở độ cao 600 m xuống mặt đất với tốc độ 6 m/s. Thời gian rơi chạm đất là bao nhiêu giây?",
        "correctAnswer": "100",
        "explanation": "t = 600 / 6 = 100 s."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một chú thỏ rừng chạy với tốc độ 15 m/s. Trong khoảng thời gian 8 giây, chú thỏ chạy được bao nhiêu mét?",
        "correctAnswer": "120",
        "explanation": "s = 15 × 8 = 120 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đi xe máy từ A đến B. Nửa quãng đường đầu người đó đi với tốc độ 30 km/h, nửa quãng đường sau đi với tốc độ 50 km/h. Tốc độ trung bình của xe máy trên cả quãng đường AB là bao nhiêu km/h?",
        "options": [
          "37,5 km/h",
          "40 km/h",
          "35 km/h",
          "42 km/h"
        ],
        "correct": 0,
        "explanation": "v_tb = 2v1v2 / (v1 + v2) = 2 × 30 × 50 / (30 + 50) = 3000 / 80 = 37,5 km/h."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hai người cùng xuất phát từ địa điểm A lúc 8h00 để đi đến địa điểm B cách A 60 km. Người thứ nhất đi xe máy với tốc độ 40 km/h. Người thứ hai đi ô tô với tốc độ 60 km/h. Xe ô tô đến bến B sớm hơn xe máy bao nhiêu phút?",
        "options": [
          "30 phút",
          "20 phút",
          "15 phút",
          "45 phút"
        ],
        "correct": 0,
        "explanation": "t_xe_máy = 60 / 40 = 1,5 h = 90 phút. t_ô_tô = 60 / 60 = 1 h = 60 phút. Sớm hơn: 90 - 60 = 30 phút."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu hỏa dài 150 m đang chạy với tốc độ 54 km/h (15 m/s) chạy song song và cùng chiều với một người đi xe đạp với tốc độ 18 km/h (5 m/s). Thời gian từ lúc đầu tàu bắt đầu vượt người đi xe đạp đến khi đuôi tàu vượt qua hẳn là:",
        "options": [
          "15 giây",
          "10 giây",
          "20 giây",
          "30 giây"
        ],
        "correct": 0,
        "explanation": "Tốc độ tương đối: v = 15 - 5 = 10 m/s. t = 150 / 10 = 15 s."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một ca nô xuôi dòng khúc sông dài 60 km hết 2 giờ, sau đó ngược dòng trở về hết 3 giờ. Biết công suất máy không đổi, tốc độ thực của ca nô khi nước đứng yên là:",
        "options": [
          "25 km/h",
          "20 km/h",
          "5 km/h",
          "30 km/h"
        ],
        "correct": 0,
        "explanation": "v_xuôi = 60 / 2 = 30 km/h; v_ngược = 60 / 3 = 20 km/h => v_thực = (30 + 20) / 2 = 25 km/h."
      }
    ]
  },
  "phys7_c3_b9_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 9: Đo tốc độ - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b9",
    "lessonName": "Bài 9: Đo tốc độ",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Để đo tốc độ của một vật chuyển động bằng phương pháp thông thường trong phòng thí nghiệm, ta cần dùng:",
        "options": [
          "Thước đo độ dài và đồng hồ đo thời gian",
          "Cân điện tử và nhiệt kế",
          "Lực kế và thước dây",
          "Bình chia độ và đồng hồ bấm giây"
        ],
        "correct": 0,
        "explanation": "Để tính v = s / t cần đo quãng đường bằng thước và đo thời gian bằng đồng hồ."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Thiết bị đo thời gian hiện đại trong phòng thực hành kết nối với đồng hồ đo hiện số để đo chính xác chuyển động là:",
        "options": [
          "Cổng quang điện (cảm biến hồng ngoại)",
          "Đồng hồ cát",
          "Đồng hồ quả lắc",
          "Nhiệt kế điện tử"
        ],
        "correct": 0,
        "explanation": "Cổng quang điện ghi nhận thời gian vật chắn chùm tia sáng truyền tới đồng hồ hiện số."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Thiết bị 'bắn tốc độ' thường được lực lượng cảnh sát giao thông sử dụng trên đường hoạt động dựa trên:",
        "options": [
          "Camera kết hợp máy phát và thu sóng vô tuyến (radar) hoặc sóng laser",
          "Cân tải trọng tự động",
          "Thước dây đo cự li",
          "Kính tiềm vọng"
        ],
        "correct": 0,
        "explanation": "Súng bắn tốc độ phát sóng radar hoặc laser rồi thu tín hiệu phản xạ để tính tốc độ và chụp ảnh xe."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi đo tốc độ bằng thước và đồng hồ bấm giây, để kết quả đo chính xác hơn và giảm thiểu sai số ngẫu nhiên, ta cần:",
        "options": [
          "Thực hiện phép đo nhiều lần rồi tính giá trị trung bình",
          "Chỉ cần đo một lần duy nhất thật cẩn thận",
          "Chọn dụng cụ có giới hạn đo nhỏ nhất có thể",
          "Làm tròn kết quả lên số nguyên lớn nhất"
        ],
        "correct": 0,
        "explanation": "Đo lặp lại nhiều lần và lấy giá trị trung bình giúp triệt tiêu sai số ngẫu nhiên."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong thí nghiệm đo tốc độ của viên bi lăn trên máng nghiêng bằng cổng quang điện, đại lượng s đo bằng thước là:",
        "options": [
          "Khoảng cách giữa hai cổng quang điện",
          "Chiều dài của cả máng nghiêng",
          "Đường kính của viên bi",
          "Độ cao của máng nghiêng"
        ],
        "correct": 0,
        "explanation": "Quãng đường s là khoảng cách giữa hai cổng quang điện A và B."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Đồng hồ bấm giây điện tử hiện số có nút chức năng nào để đưa kết quả hiển thị về giá trị 0 ban đầu?",
        "options": [
          "Nút Reset",
          "Nút Mode",
          "Nút Start",
          "Nút Stop"
        ],
        "correct": 0,
        "explanation": "Nút Reset dùng để xóa kết quả hiển thị về 00:00:00."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Dùng thước mét đo quãng đường đi được s = 1,2 m và đồng hồ bấm giây đo thời gian t = 0,8 s. Tốc độ chuyển động là:",
        "options": [
          "1,5 m/s",
          "0,96 m/s",
          "1,2 m/s",
          "2,0 m/s"
        ],
        "correct": 0,
        "explanation": "v = s / t = 1,2 / 0,8 = 1,5 m/s."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một tấm chắn sáng có bề rộng d = 2 cm (0,02 m) gắn trên xe lăn. Khi xe đi qua cổng quang điện, đồng hồ hiện số báo thời gian chắn sáng là 0,05 s. Tốc độ tức thời của xe là:",
        "options": [
          "0,4 m/s",
          "0,1 m/s",
          "2,5 m/s",
          "1,0 m/s"
        ],
        "correct": 0,
        "explanation": "v = d / t = 0,02 / 0,05 = 0,4 m/s."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Khi sử dụng đồng hồ bấm giây để đo thời gian chạy của bạn học sinh, sai số chủ yếu xuất phát từ:",
        "options": [
          "Thời gian phản ứng của ngón tay người bấm khi nghe hiệu lệnh xuất phát và lúc thấy bạn về đích",
          "Đồng hồ chạy quá nhanh",
          "Đồng hồ bị sai pin",
          "Không khí cản trở đồng hồ"
        ],
        "correct": 0,
        "explanation": "Sai số phản ứng của con người khi bấm nút Start/Stop khoảng 0,1 - 0,2 s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Thiết bị bắn tốc độ ghi nhận thời gian ô tô đi qua hai vạch mốc cách nhau 10 m là 0,5 giây. Tốc độ của ô tô là:",
        "options": [
          "72 km/h",
          "50 km/h",
          "20 km/h",
          "36 km/h"
        ],
        "correct": 0,
        "explanation": "v = 10 / 0,5 = 20 m/s = 20 × 3,6 = 72 km/h."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Trong thí nghiệm đo tốc độ xe đồ chơi, kết quả đo 3 lần thời gian đi cùng quãng đường 1 m lần lượt là: 2,4 s; 2,5 s; 2,6 s. Thời gian trung bình là:",
        "options": [
          "2,5 s",
          "2,4 s",
          "2,6 s",
          "2,55 s"
        ],
        "correct": 0,
        "explanation": "t_tb = (2,4 + 2,5 + 2,6) / 3 = 2,5 s."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Ưu điểm nổi bật nhất của việc dùng cổng quang điện và đồng hồ hiện số so với đồng hồ bấm giây tay là:",
        "options": [
          "Độ chính xác rất cao, loại bỏ hoàn toàn sai số do phản ứng bấm tay của con người",
          "Giá thành rẻ hơn nhiều",
          "Dễ mang đi dã ngoại",
          "Không cần dùng nguồn điện"
        ],
        "correct": 0,
        "explanation": "Cảm biến quang điện tự động đóng ngắt mạch đo, không bị ảnh hưởng bởi phản xạ tay người."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét phương pháp đo tốc độ bằng thước cuộn và đồng hồ bấm giây trong giờ học thể dục:",
        "statements": [
          {
            "subId": "a",
            "text": "Thước cuộn dùng để đo độ dài đường chạy của học sinh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Người bấm giờ cần bấm nút chạy đồng hồ ngay khi nghe hiệu lệnh xuất phát.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dừng đồng hồ ngay khi học sinh chạm vạch đích.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phương pháp này hoàn toàn không có sai số nào xảy ra.",
            "correct": false
          }
        ],
        "explanation": "Phương pháp bấm tay luôn có sai số do phản xạ và thao tác người bấm."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét hoạt động của cổng quang điện và đồng hồ đo thời gian hiện số:",
        "statements": [
          {
            "subId": "a",
            "text": "Cổng quang điện gồm một đầu phát tia hồng ngoại và một đầu thu tín hiệu quang học.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi vật chắn chùm tia sáng giữa cổng quang, tín hiệu điện được truyền đến đồng hồ hiện số để bắt đầu hoặc dừng đếm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu đặt chế độ đo A <-> B, đồng hồ sẽ đo khoảng thời gian vật di chuyển từ cổng A đến cổng B.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Cổng quang điện chỉ có thể đo được các vật có khối lượng lớn hơn 1 kg.",
            "correct": false
          }
        ],
        "explanation": "Cổng quang điện đo được cả các vật rất nhỏ và nhẹ như viên bi, xe đồ chơi."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Học sinh thực hiện đo tốc độ xe lăn trên máng nghiêng giữa hai cổng quang A và B cách nhau 0,8 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Ba lần đo thời gian xe chạy từ A đến B lần lượt là: 1,58 s; 1,60 s; 1,62 s.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian chuyển động trung bình của xe lăn là 1,60 s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ trung bình của xe lăn giữa hai cổng quang là 0,5 m/s.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu nâng máng nghiêng dốc hơn, thời gian xe lăn chạy giữa hai cổng sẽ tăng lên.",
            "correct": false
          }
        ],
        "explanation": "Máng nghiêng dốc hơn làm xe chuyển động nhanh hơn nên thời gian chạy giảm đi."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cảnh sát giao thông sử dụng thiết bị bắn tốc độ để kiểm soát giao thông trên đường quốc lộ:",
        "statements": [
          {
            "subId": "a",
            "text": "Thiết bị có thể đo được cả tốc độ của phương tiện đang tiến lại gần hoặc rời xa máy bắn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Máy tự động ghi nhận hình ảnh biển số xe, thời gian và tốc độ đo được của phương tiện.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hình ảnh chụp từ thiết bị bắn tốc độ có giá trị pháp lí để xử phạt phương tiện vi phạm tốc độ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Thiết bị bắn tốc độ bắt buộc phải có người cầm dây kéo theo xe để đo độ dài đường đi.",
            "correct": false
          }
        ],
        "explanation": "Thiết bị bắn tốc độ ứng dụng sóng radar/laser không dây, không dùng dây đo cơ học."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Dùng đồng hồ bấm giây đo thời gian một bạn chạy 60 m hết 10 s. Tốc độ trung bình là bao nhiêu m/s?",
        "correctAnswer": "6",
        "explanation": "v = 60 / 10 = 6 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khoảng cách giữa hai cổng quang điện A và B là 0,6 m. Đồng hồ hiện số báo thời gian xe đi từ A đến B là 0,5 s. Tốc độ trung bình là bao nhiêu m/s?",
        "correctAnswer": "1.2",
        "explanation": "v = 0,6 / 0,5 = 1,2 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tấm chắn sáng gắn trên xe thí nghiệm có độ rộng 0,04 m. Đồng hồ hiện số đo được thời gian tấm chắn đi qua cổng quang là 0,08 s. Tốc độ tức thời của xe là bao nhiêu m/s?",
        "correctAnswer": "0.5",
        "explanation": "v = 0,04 / 0,08 = 0,5 m/s."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Học sinh đo 3 lần thời gian viên bi chuyển động trên máng dài 0,9 m được các giá trị: 1,7 s; 1,8 s; 1,9 s. Tốc độ trung bình của viên bi là bao nhiêu m/s?",
        "correctAnswer": "0.5",
        "explanation": "t_tb = (1,7 + 1,8 + 1,9)/3 = 1,8 s => v = 0,9 / 1,8 = 0,5 m/s."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Camera bắn tốc độ cố định ghi nhận một ô tô đi qua đoạn đường kiểm tra dài 15 m mất 0,6 giây. Tốc độ của ô tô đó tính theo km/h là bao nhiêu?",
        "correctAnswer": "90",
        "explanation": "v = 15 / 0,6 = 25 m/s = 25 × 3,6 = 90 km/h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một người gõ búa xuống đường ray xe lửa, người ở đầu kia áp tai vào đường ray nghe thấy âm truyền trong thép sau 0,1 giây. Biết đường ray dài 500 m. Tốc độ âm trong thép đo được là bao nhiêu m/s?",
        "correctAnswer": "5000",
        "explanation": "v = 500 / 0,1 = 5000 m/s."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Thiết bị bắn tốc độ tự động đặt tại đoạn đường có biển giới hạn tốc độ 60 km/h. Thiết bị chụp hai bức ảnh một xe con khi đi qua hai vạch mốc cách nhau 20 m trong khoảng thời gian 1,0 giây. Xe con đó có vi phạm chạy quá tốc độ không và vượt quá bao nhiêu km/h?",
        "options": [
          "Có vi phạm, chạy 72 km/h (vượt quá 12 km/h)",
          "Không vi phạm vì tốc độ chỉ là 50 km/h",
          "Không vi phạm vì tốc độ đạt đúng 60 km/h",
          "Có vi phạm, chạy 80 km/h (vượt quá 20 km/h)"
        ],
        "correct": 0,
        "explanation": "v = 20 / 1,0 = 20 m/s = 72 km/h. Giới hạn 60 km/h => vượt quá 12 km/h."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trong giờ thực hành, bạn An dùng đồng hồ bấm giây để đo thời gian rơi của một quả bóng bàn từ độ cao 2,0 m. Do độ trễ phản xạ tay bấm của An là 0,15 s, thời gian hiển thị trên đồng hồ là 0,80 s. Thời gian rơi thực tế và tốc độ rơi trung bình thực tế của quả bóng là:",
        "options": [
          "0,65 s và xấp xỉ 3,08 m/s",
          "0,95 s và xấp xỉ 2,11 m/s",
          "0,80 s và 2,50 m/s",
          "0,50 s và 4,00 m/s"
        ],
        "correct": 0,
        "explanation": "t_thực = 0,80 - 0,15 = 0,65 s => v_tb = 2,0 / 0,65 ≈ 3,08 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để đo tốc độ của dòng nước sông, một nhóm học sinh thả một chiếc phao xốp trôi tự do giữa hai cột mốc ven bờ cách nhau 40 m. Đồng hồ bấm giây đo được 3 lần thời gian trôi lần lượt là: 48 s; 50 s; 52 s. Tốc độ dòng nước xấp xỉ bằng:",
        "options": [
          "0,80 m/s",
          "0,75 m/s",
          "1,25 m/s",
          "1,00 m/s"
        ],
        "correct": 0,
        "explanation": "t_tb = (48 + 50 + 52) / 3 = 50 s => v = 40 / 50 = 0,80 m/s."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu đang chạy thẳng đều. Người lái tàu quan sát thấy đầu tàu vượt qua hai cột mốc cây số bên đường cách nhau 1 km trong thời gian đúng 45 giây. Tốc độ của đoàn tàu là:",
        "options": [
          "80 km/h",
          "60 km/h",
          "90 km/h",
          "75 km/h"
        ],
        "correct": 0,
        "explanation": "v = 1000 / 45 = 200/9 m/s = (200/9) × 3,6 = 80 km/h."
      }
    ]
  },
  "phys7_c3_b9_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 9: Đo tốc độ - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b9",
    "lessonName": "Bài 9: Đo tốc độ",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Dụng cụ dùng để đo quãng đường chuyển động của một vật trong thí nghiệm vật lý là:",
        "options": [
          "Thước cuộn hoặc thước thẳng có ĐCNN phù hợp",
          "Nhiệt kế",
          "Lực kế",
          "Ampe kế"
        ],
        "correct": 0,
        "explanation": "Dùng thước có ĐCNN phù hợp để đo quãng đường s."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đồng hồ bấm giây cơ học hoặc điện tử dùng để đo đại lượng nào trong bài thực hành đo tốc độ?",
        "options": [
          "Khoảng thời gian chuyển động",
          "Quãng đường vật đi",
          "Trọng lượng của vật",
          "Nhiệt độ môi trường"
        ],
        "correct": 0,
        "explanation": "Đồng hồ bấm giây dùng để đo khoảng thời gian t."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong hệ thống đo tốc độ tự động ở phòng thí nghiệm trường học, cổng quang điện gửi tín hiệu đến thiết bị nào?",
        "options": [
          "Đồng hồ đo thời gian hiện số",
          "Bình ắc quy",
          "Bóng đèn sợi đốt",
          "Loa phát thanh"
        ],
        "correct": 0,
        "explanation": "Cổng quang điện kết nối với đồng hồ đo thời gian hiện số."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Súng bắn tốc độ của cảnh sát giao thông tính được tốc độ phương tiện nhờ đo đại lượng nào?",
        "options": [
          "Thời gian truyền và phản xạ lại của chùm sóng vô tuyến hoặc laser",
          "Khối lượng của xe",
          "Tiếng ồn động cơ xe phát ra",
          "Màu sơn của xe"
        ],
        "correct": 0,
        "explanation": "Đo khoảng thời gian sóng phản xạ từ xe quay trở lại súng."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Để giảm sai số của dụng cụ khi đo quãng đường, ta nên chọn thước đo có:",
        "options": [
          "Giới hạn đo thích hợp và độ chia nhỏ nhất (ĐCNN) đủ nhỏ",
          "Độ chia nhỏ nhất càng lớn càng tốt",
          "Chiều dài ngắn hơn vật cần đo nhiều lần",
          "Vạch chia bị mờ"
        ],
        "correct": 0,
        "explanation": "Chọn thước có GHĐ phù hợp và ĐCNN đủ nhỏ giúp số đo chuẩn xác."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trên đồng hồ đo thời gian hiện số, thang đo hiển thị thời gian thường có đơn vị là:",
        "options": [
          "Giây (s) và phần nghìn giây (ms)",
          "Phút (min)",
          "Giờ (h)",
          "Ngày"
        ],
        "correct": 0,
        "explanation": "Đồng hồ hiện số trong phòng thí nghiệm thường đo đến 0,001 s (miligiây)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một học sinh đo quãng đường chạy s = 80 m, đồng hồ bấm giây chỉ t = 16 s. Tốc độ trung bình của bạn là:",
        "options": [
          "5 m/s",
          "4 m/s",
          "6 m/s",
          "1280 m/s"
        ],
        "correct": 0,
        "explanation": "v = s / t = 80 / 16 = 5 m/s."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tấm chắn sáng rộng 1 cm (0,01 m) đi qua cổng quang điện trong thời gian 0,02 s. Tốc độ tức thời của vật là:",
        "options": [
          "0,5 m/s",
          "0,2 m/s",
          "2,0 m/s",
          "1,0 m/s"
        ],
        "correct": 0,
        "explanation": "v = 0,01 / 0,02 = 0,5 m/s."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Để đo thời gian chạy 100 m của vận động viên điền kinh, người bấm giờ bắt đầu bấm đồng hồ khi:",
        "options": [
          "Thấy khói phát ra từ nòng súng phát lệnh (hoặc đèn phát lệnh chớp sáng)",
          "Nghe thấy tiếng nổ của súng phát lệnh",
          "Thấy vận động viên bắt đầu chạm chân qua vạch đích",
          "Vận động viên đã chạy được một nửa đường"
        ],
        "correct": 0,
        "explanation": "Ánh sáng truyền nhanh tức thời, nhìn thấy tia chớp/khói súng bấm ngay sẽ chuẩn xác hơn nghe tiếng nổ (do âm thanh truyền chậm)."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Camera bắn tốc độ ghi nhận một mô tô đi qua quãng đường kiểm tra 12 m trong thời gian 0,8 s. Tốc độ của mô tô là:",
        "options": [
          "54 km/h",
          "15 km/h",
          "36 km/h",
          "60 km/h"
        ],
        "correct": 0,
        "explanation": "v = 12 / 0,8 = 15 m/s = 15 × 3,6 = 54 km/h."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Ba bạn cùng đo thời gian viên bi lăn qua quãng đường 1,5 m được các giá trị: 3,1 s; 2,9 s; 3,0 s. Giá trị trung bình là:",
        "options": [
          "3,0 s",
          "2,9 s",
          "3,1 s",
          "3,05 s"
        ],
        "correct": 0,
        "explanation": "t_tb = (3,1 + 2,9 + 3,0) / 3 = 3,0 s."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Khi đo tốc độ bằng xe lăn trên máng nghiêng dùng cổng quang điện, nếu thay viên bi sắt bằng viên bi gỗ có cùng kích thước thì:",
        "options": [
          "Thời gian chắn sáng vẫn được đồng hồ đo chính xác nhờ tín hiệu ngắt quang học",
          "Cổng quang điện không nhận diện được bi gỗ",
          "Đồng hồ không chạy",
          "Cổng quang bị chập điện"
        ],
        "correct": 0,
        "explanation": "Cổng quang ngắt tín hiệu khi có bất kì vật cản quang nào đi qua."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét quy trình thực hiện phép đo tốc độ bằng thước thẳng và đồng hồ bấm giây:",
        "statements": [
          {
            "subId": "a",
            "text": "Dùng thước đo xác định quãng đường chuyển động s.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dùng đồng hồ bấm giây đo khoảng thời gian t vật đi hết quãng đường s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tính tốc độ của vật theo công thức v = s / t.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Chỉ cần đo đúng 1 lần là khẳng định kết quả chính xác tuyệt đối không có sai số.",
            "correct": false
          }
        ],
        "explanation": "Mọi phép đo thực nghiệm đều có sai số, cần đo nhiều lần lấy trung bình."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét hoạt động của đồng hồ đo thời gian hiện số khi nối với cổng quang điện:",
        "statements": [
          {
            "subId": "a",
            "text": "Có thể chọn chế độ đo thời gian vật chắn qua một cổng quang điện duy nhất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Có thể chọn chế độ đo khoảng thời gian vật đi từ cổng quang thứ nhất đến cổng quang thứ hai.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đồng hồ hiện số hiển thị kết quả bằng các chữ số điện tử rõ ràng, tránh sai số đọc mắt.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đồng hồ đo hiện số chỉ hoạt động được khi dùng đèn pin chiếu trực tiếp từ bên ngoài.",
            "correct": false
          }
        ],
        "explanation": "Cổng quang điện có sẵn đèn phát tia hồng ngoại bên trong, không cần đèn pin bên ngoài."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Học sinh tiến hành đo tốc độ rơi của một quả cầu nhỏ từ độ cao h = 1,25 m xuống sàn:",
        "statements": [
          {
            "subId": "a",
            "text": "Học sinh đo 3 lần thời gian rơi thu được các kết quả: 0,49 s; 0,50 s; 0,51 s.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian rơi trung bình tính được là 0,50 s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ rơi trung bình của quả cầu trên đoạn đường này là 2,5 m/s.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu tăng độ cao rơi lên 5 m thì thời gian rơi sẽ giảm đi một nửa.",
            "correct": false
          }
        ],
        "explanation": "Rơi từ độ cao lớn hơn thì thời gian rơi phải tăng lên."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng thiết bị bắn tốc độ trong giám sát an toàn giao thông đường cao tốc:",
        "statements": [
          {
            "subId": "a",
            "text": "Camera ghi hình giúp xác định chính xác biển kiểm soát của phương tiện chạy quá tốc độ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hệ thống có thể hoạt động giám sát tự động liên tục cả ngày lẫn đêm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thiết bị laser bắn tốc độ phát ra chùm tia laser nhìn thấy được màu đỏ làm mù mắt tài xế.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Dữ liệu tốc độ đo được từ hệ thống được truyền trực tiếp về trung tâm điều hành giao thông.",
            "correct": true
          }
        ],
        "explanation": "Tia laser trong máy đo tốc độ là laser hồng ngoại không nhìn thấy và an toàn cho mắt."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đo quãng đường s = 100 m và thời gian t = 20 s. Tốc độ tính được là bao nhiêu m/s?",
        "correctAnswer": "5",
        "explanation": "v = 100 / 20 = 5 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cổng quang điện cách nhau 0,8 m. Đồng hồ hiện số đo thời gian xe chạy hết 0,4 s. Tốc độ của xe là bao nhiêu m/s?",
        "correctAnswer": "2",
        "explanation": "v = 0,8 / 0,4 = 2 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tấm chắn sáng rộng 0,03 m. Đồng hồ đo thời gian chắn cổng quang là 0,05 s. Tốc độ tức thời là bao nhiêu m/s?",
        "correctAnswer": "0.6",
        "explanation": "v = 0,03 / 0,05 = 0,6 m/s."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Thực hiện 3 lần đo thời gian xe lăn chạy quãng đường 1,2 m thu được: 2,3 s; 2,4 s; 2,5 s. Tốc độ trung bình là bao nhiêu m/s?",
        "correctAnswer": "0.5",
        "explanation": "t_tb = (2,3 + 2,4 + 2,5)/3 = 2,4 s => v = 1,2 / 2,4 = 0,5 m/s."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Camera ghi nhận một ô tô đi qua 2 mốc cách nhau 25 m trong 1 giây. Tốc độ của ô tô đó tính theo km/h là bao nhiêu?",
        "correctAnswer": "90",
        "explanation": "v = 25 / 1 = 25 m/s = 25 × 3,6 = 90 km/h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một máy phát siêu âm từ mạn tàu phát xuống đáy biển và nhận lại tín hiệu phản xạ sau 0,8 giây. Biết tốc độ âm trong nước biển là 1500 m/s. Độ sâu đáy biển là bao nhiêu mét?",
        "correctAnswer": "600",
        "explanation": "d = v × t / 2 = 1500 × 0,8 / 2 = 600 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một đoạn đường trong khu dân cư có biển báo giới hạn tốc độ tối đa là 50 km/h. Súng bắn tốc độ laser của cảnh sát giao thông ghi nhận xe mô tô chạy qua quãng đường 15 m trong thời gian đúng 0,9 giây. Tốc độ thực tế của xe mô tô là bao nhiêu và xe có vi phạm quy định tốc độ không?",
        "options": [
          "60 km/h - Có vi phạm chạy quá tốc độ cho phép",
          "45 km/h - Không vi phạm tốc độ",
          "50 km/h - Đạt đúng tốc độ tối đa cho phép",
          "65 km/h - Có vi phạm chạy quá tốc độ cho phép"
        ],
        "correct": 0,
        "explanation": "v = 15 / 0,9 = 50/3 m/s = (50/3) × 3,6 = 60 km/h. Giới hạn 50 km/h => Có vi phạm quá tốc độ."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trong phòng thí nghiệm, học sinh đo tốc độ của viên bi chuyển động trên đệm khí. Quãng đường đo bằng thước có sai số dụng cụ là ± 0,002 m, đo được s = 0,500 m. Đồng hồ hiện số đo thời gian t = 0,250 s với sai số ± 0,001 s. Tốc độ trung bình của viên bi xấp xỉ bằng:",
        "options": [
          "2,00 m/s",
          "1,50 m/s",
          "2,50 m/s",
          "1,80 m/s"
        ],
        "correct": 0,
        "explanation": "v = 0,500 / 0,250 = 2,00 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để đo tốc độ âm thanh trong không khí, hai bạn học sinh đứng cách một bức tường lớn 170 m. Một bạn gõ hai thanh gỗ vào nhau, bạn kia bấm đồng hồ đo thời gian từ lúc gõ đến lúc nghe thấy tiếng vang dội lại là 1,0 giây. Tốc độ âm thanh đo được từ thí nghiệm này là:",
        "options": [
          "340 m/s",
          "170 m/s",
          "680 m/s",
          "300 m/s"
        ],
        "correct": 0,
        "explanation": "Âm thanh truyền đi và về: s = 2 × 170 = 340 m. v = 340 / 1,0 = 340 m/s."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một ô tô đồ chơi điều khiển từ xa chạy một vòng tròn khép kín có chu vi 18,84 m (đo bằng dây mềm). Đồng hồ bấm giây ghi lại thời gian chạy hết một vòng là 6,0 giây. Tốc độ trung bình của ô tô đồ chơi là:",
        "options": [
          "3,14 m/s",
          "6,28 m/s",
          "1,57 m/s",
          "2,50 m/s"
        ],
        "correct": 0,
        "explanation": "v = s / t = 18,84 / 6,0 = 3,14 m/s."
      }
    ]
  },
  "phys7_c3_b9_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 9: Đo tốc độ - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b9",
    "lessonName": "Bài 9: Đo tốc độ",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Để xác định tốc độ tức thời của một vật chuyển động trên máng thực hành, người ta gắn trên vật:",
        "options": [
          "Một tấm chắn sáng có bề rộng xác định",
          "Một quả cân nặng",
          "Một chiếc nhiệt kế",
          "Một miếng nam châm"
        ],
        "correct": 0,
        "explanation": "Gắn tấm chắn sáng có độ rộng nhỏ d để cổng quang điện đo thời gian chắn sáng t."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cổng quang điện hoạt động dựa trên nguyên lí cảm biến:",
        "options": [
          "Quang điện hồng ngoại",
          "Nhiệt độ nóng chảy",
          "Áp suất không khí",
          "Sức căng bề mặt"
        ],
        "correct": 0,
        "explanation": "Cổng quang điện sử dụng cảm biến quang điện thu phát tia hồng ngoại."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong thí nghiệm đo tốc độ của học sinh chạy cự li ngắn, dụng cụ đo thời gian thường dùng là:",
        "options": [
          "Đồng hồ bấm giây cầm tay",
          "Đồng hồ cát",
          "Thước dây",
          "Cân đồng hồ"
        ],
        "correct": 0,
        "explanation": "Đồng hồ bấm giây là thiết bị đo thời gian phổ biến trong thể dục thể thao."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Camera bắn tốc độ cố định được lắp đặt trên các giá long môn trên cao tốc nhằm:",
        "options": [
          "Tự động phát hiện và ghi nhận vi phạm chạy quá tốc độ của các xe lưu thông",
          "Đo nhiệt độ mặt đường",
          "Chiếu sáng ban đêm",
          "Đếm số cây xanh ven đường"
        ],
        "correct": 0,
        "explanation": "Giám sát tốc độ phương tiện tự động trên các làn xe cao tốc."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Khi dùng thước kẻ để đo quãng đường s, mắt của người đọc kết quả cần đặt:",
        "options": [
          "Vuông góc với cạnh thước tại vạch đo",
          "Nghiêng góc 45 độ về phía trái",
          "Nghiêng góc 45 độ về phía phải",
          "Cách thước thật xa"
        ],
        "correct": 0,
        "explanation": "Đặt mắt nhìn vuông góc với cạnh thước tại vạch đo để tránh sai số thị giác."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Đơn vị đo thời gian chuẩn trong hệ thống đơn vị đo lường quốc tế SI là:",
        "options": [
          "Giây (s)",
          "Phút (min)",
          "Giờ (h)",
          "Ngày"
        ],
        "correct": 0,
        "explanation": "Đơn vị chuẩn của thời gian trong hệ SI là giây (s)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một học sinh đo quãng đường đi được s = 1,8 m trong thời gian t = 1,2 s. Tốc độ chuyển động của vật là:",
        "options": [
          "1,5 m/s",
          "2,16 m/s",
          "0,67 m/s",
          "3,0 m/s"
        ],
        "correct": 0,
        "explanation": "v = s / t = 1,8 / 1,2 = 1,5 m/s."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một tấm chắn sáng có bề rộng d = 1,5 cm (0,015 m) chắn cổng quang điện trong 0,03 s. Tốc độ tức thời là:",
        "options": [
          "0,5 m/s",
          "0,05 m/s",
          "2,0 m/s",
          "0,45 m/s"
        ],
        "correct": 0,
        "explanation": "v = 0,015 / 0,03 = 0,5 m/s."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Trong thí nghiệm đo tốc độ của xe đồ chơi, nếu ta quên bấm nút dừng khi xe đã về đích thì:",
        "options": [
          "Thời gian ghi nhận lớn hơn thực tế, dẫn đến tốc độ tính được nhỏ hơn thực tế",
          "Tốc độ tính được lớn hơn thực tế",
          "Quãng đường bị giảm đi",
          "Không ảnh hưởng đến kết quả"
        ],
        "correct": 0,
        "explanation": "t ghi nhận lớn hơn => v = s / t sẽ nhỏ hơn thực tế."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Thiết bị bắn tốc độ ghi nhận thời gian ô tô đi qua 30 m là 1,2 giây. Tốc độ của ô tô tương ứng là:",
        "options": [
          "90 km/h",
          "25 km/h",
          "60 km/h",
          "72 km/h"
        ],
        "correct": 0,
        "explanation": "v = 30 / 1,2 = 25 m/s = 25 × 3,6 = 90 km/h."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Ba lần đo thời gian chuyển động của hòn bi trên máng thẳng dài 1,2 m là: 1,9 s; 2,0 s; 2,1 s. Tốc độ trung bình là:",
        "options": [
          "0,6 m/s",
          "0,5 m/s",
          "1,2 m/s",
          "0,8 m/s"
        ],
        "correct": 0,
        "explanation": "t_tb = (1,9 + 2,0 + 2,1)/3 = 2,0 s => v = 1,2 / 2,0 = 0,6 m/s."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tại sao khi chạy cự li 100 m, người ta thường dùng súng phát lệnh có khói trắng thay vì chỉ hô bằng miệng?",
        "options": [
          "Vì người bấm giờ ở vạch đích nhìn thấy khói trắng tức thì, loại trừ sai số do âm thanh truyền chậm",
          "Để làm đẹp sân đấu",
          "Để tạo tiếng vang lớn",
          "Để người chạy không bị giật mình"
        ],
        "correct": 0,
        "explanation": "Ánh sáng truyền nhanh (300.000 km/s) đến mắt người bấm giờ ngay lập tức, trong khi âm thanh mất khoảng 0,3 s mới đến vạch đích."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các nguyên nhân gây sai số trong thực hành đo tốc độ:",
        "statements": [
          {
            "subId": "a",
            "text": "Sai số do dụng cụ đo có độ chia nhỏ nhất chưa đủ nhỏ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sai số do thao tác bấm đồng hồ bấm giây không đúng thời điểm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sai số do đặt mắt nhìn lệch vạch chia trên thước đo.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Sai số ngẫu nhiên hoàn toàn không thể làm giảm bớt dù đo bao nhiêu lần.",
            "correct": false
          }
        ],
        "explanation": "Sai số ngẫu nhiên có thể giảm bớt bằng cách đo lặp lại nhiều lần và lấy giá trị trung bình."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các chế độ đo của đồng hồ đo thời gian hiện số:",
        "statements": [
          {
            "subId": "a",
            "text": "Chế độ đo MODE A dùng để đo thời gian vật chắn sáng cổng quang A.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chế độ đo MODE A-B dùng để đo khoảng thời gian vật đi từ cổng A đến cổng B.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kết quả đo được hiển thị trực tiếp trên màn hình LED bằng các chữ số thập phân.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đồng hồ hiện số chỉ có thể đo thời gian lớn hơn 10 giây.",
            "correct": false
          }
        ],
        "explanation": "Đồng hồ hiện số có thể đo các khoảng thời gian rất ngắn tới 0,001 s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Học sinh đo tốc độ của xe thế năng chuyển động trên máng nghiêng:",
        "statements": [
          {
            "subId": "a",
            "text": "Khoảng cách giữa hai cổng quang đo được là s = 0,5 m.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian xe chạy giữa hai cổng quang đo được 3 lần: 0,98 s; 1,00 s; 1,02 s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thời gian trung bình xe chạy là 1,00 s.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình của xe là 1,0 m/s.",
            "correct": false
          }
        ],
        "explanation": "v = s / t = 0,5 / 1,00 = 0,5 m/s (câu d ghi 1,0 m/s là sai)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hệ thống phạt nguội giao thông bằng camera và cảm biến đo tốc độ:",
        "statements": [
          {
            "subId": "a",
            "text": "Hệ thống có khả năng tự động trích xuất video và hình ảnh phương tiện vi phạm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thông tin vi phạm được gửi thông báo phạt nguội đến chủ phương tiện theo địa chỉ đăng kí.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Camera bắn tốc độ chỉ đo được xe máy, không đo được xe ô tô tải lớn.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Góp phần nâng cao ý thức chấp hành luật an toàn giao thông của người tham gia giao thông.",
            "correct": true
          }
        ],
        "explanation": "Hệ thống đo được mọi phương tiện tham gia giao thông trên tuyến đường."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Quãng đường chạy dài 120 m, đồng hồ bấm giây chỉ 24 s. Tốc độ trung bình là bao nhiêu m/s?",
        "correctAnswer": "5",
        "explanation": "v = 120 / 24 = 5 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Hai cổng quang cách nhau 1,0 m. Đồng hồ hiện số báo thời gian đi qua là 0,8 s. Tốc độ là bao nhiêu m/s?",
        "correctAnswer": "1.25",
        "explanation": "v = 1,0 / 0,8 = 1,25 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tấm chắn sáng rộng 0,02 m đi qua cổng quang trong 0,04 s. Tốc độ tức thời là bao nhiêu m/s?",
        "correctAnswer": "0.5",
        "explanation": "v = 0,02 / 0,04 = 0,5 m/s."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Đo 3 lần thời gian viên bi đi quãng đường 0,8 m được: 1,5 s; 1,6 s; 1,7 s. Tốc độ trung bình là bao nhiêu m/s?",
        "correctAnswer": "0.5",
        "explanation": "t_tb = (1,5 + 1,6 + 1,7)/3 = 1,6 s => v = 0,8 / 1,6 = 0,5 m/s."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Camera bắn tốc độ đo được xe ô tô đi qua 18 m trong thời gian 0,72 giây. Tốc độ ô tô là bao nhiêu km/h?",
        "correctAnswer": "90",
        "explanation": "v = 18 / 0,72 = 25 m/s = 25 × 3,6 = 90 km/h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một máy định vị bằng sóng siêu âm trên tàu ngầm gửi xung âm xuống đáy vực sâu và thu được tín hiệu sau 2,4 giây. Biết tốc độ âm trong nước là 1500 m/s. Độ sâu đáy vực là bao nhiêu mét?",
        "correctAnswer": "1800",
        "explanation": "d = v × t / 2 = 1500 × 2,4 / 2 = 1800 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một xe tải chở hàng chạy qua đoạn đường có gắn camera đo tốc độ tự động. Biển báo cho phép tốc độ tối đa là 70 km/h. Xe tải đi qua đoạn đường kiểm tra dài 35 m mất thời gian 1,5 giây. Xe tải đó có vi phạm chạy quá tốc độ không và tốc độ đo được là bao nhiêu?",
        "options": [
          "Có vi phạm, tốc độ xe là 84 km/h (vượt quá 14 km/h)",
          "Không vi phạm, tốc độ xe là 65 km/h",
          "Không vi phạm, tốc độ xe đạt đúng 70 km/h",
          "Có vi phạm, tốc độ xe là 90 km/h (vượt quá 20 km/h)"
        ],
        "correct": 0,
        "explanation": "v = 35 / 1,5 = 70/3 m/s = (70/3) × 3,6 = 84 km/h > 70 km/h => Vi phạm vượt 14 km/h."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trong thí nghiệm đo tốc độ rơi tự do của quả cầu kim loại giữa hai cổng quang điện đặt thẳng đứng cách nhau 0,45 m, đồng hồ hiện số hiển thị thời gian 0,30 s. Tốc độ trung bình của quả cầu trong khoảng rơi này là:",
        "options": [
          "1,5 m/s",
          "1,2 m/s",
          "2,0 m/s",
          "0,9 m/s"
        ],
        "correct": 0,
        "explanation": "v = 0,45 / 0,30 = 1,5 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để đo tốc độ di chuyển của một đàn kiến, một bạn học sinh rải một đoạn đường thẳng bằng phấn dài 20 cm (0,2 m) và dùng đồng hồ bấm giây ghi nhận một chú kiến bò hết đoạn đường trong 40 giây. Tốc độ bò của chú kiến là:",
        "options": [
          "0,5 cm/s (0,005 m/s)",
          "2,0 cm/s",
          "0,2 cm/s",
          "5,0 cm/s"
        ],
        "correct": 0,
        "explanation": "v = 20 / 40 = 0,5 cm/s = 0,005 m/s."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người gõ búa vào thanh ray đường sắt bằng thép. Người thứ hai ở cách đó 1020 m áp tai vào đường ray và quan sát thấy tiếng gõ truyền qua thép đến trước tiếng gõ truyền qua không khí là 2,8 giây. Biết tốc độ âm trong không khí là 340 m/s. Tốc độ truyền âm trong thép đường ray đo được là:",
        "options": [
          "5100 m/s",
          "3400 m/s",
          "4800 m/s",
          "6000 m/s"
        ],
        "correct": 0,
        "explanation": "t_khí = 1020 / 340 = 3,0 s. t_thép = 3,0 - 2,8 = 0,2 s => v_thép = 1020 / 0,2 = 5100 m/s."
      }
    ]
  },
  "phys7_c3_b10_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 10: Đồ thị quãng đường - thời gian - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b10",
    "lessonName": "Bài 10: Đồ thị quãng đường - thời gian",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong đồ thị quãng đường - thời gian (s - t), trục thẳng đứng Os và trục nằm ngang Ot lần lượt biểu diễn:",
        "options": [
          "Quãng đường chuyển động và thời gian chuyển động",
          "Thời gian chuyển động và quãng đường chuyển động",
          "Tốc độ và thời gian",
          "Lực và quãng đường"
        ],
        "correct": 0,
        "explanation": "Trục Os thẳng đứng biểu diễn quãng đường, trục Ot nằm ngang biểu diễn thời gian."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đồ thị quãng đường - thời gian của một vật chuyển động thẳng đều có dạng là:",
        "options": [
          "Đường thẳng nghiêng dốc lên xuất phát từ gốc tọa độ",
          "Đường parabol uốn cong",
          "Đường tròn khép kín",
          "Đường thẳng zích zắc"
        ],
        "correct": 0,
        "explanation": "Chuyển động đều có s tỉ lệ thuận với t nên đồ thị s-t là đường thẳng nghiêng."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi vật đứng yên không chuyển động, đồ thị quãng đường - thời gian là:",
        "options": [
          "Đoạn thẳng song song với trục thời gian Ot",
          "Đường thẳng dốc đứng lên",
          "Đường thẳng dốc xuống",
          "Đường tròn"
        ],
        "correct": 0,
        "explanation": "Đứng yên thì quãng đường không đổi theo thời gian, đồ thị nằm ngang song song trục Ot."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Độ dốc (độ nghiêng) của đường đồ thị s - t cho biết đại lượng nào của chuyển động?",
        "options": [
          "Tốc độ chuyển động (độ dốc càng lớn thì tốc độ càng nhanh)",
          "Khối lượng của vật",
          "Nhiệt độ của vật",
          "Gia tốc rơi"
        ],
        "correct": 0,
        "explanation": "Độ dốc của đồ thị s-t tỉ lệ thuận với tốc độ chuyển động."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Từ đồ thị quãng đường - thời gian, ta KHÔNG THỂ xác định trực tiếp đại lượng nào sau đây?",
        "options": [
          "Khối lượng của vật đang chuyển động",
          "Quãng đường vật đi được sau khoảng thời gian t",
          "Thời gian cần thiết để vật đi được quãng đường s",
          "Tốc độ của vật"
        ],
        "correct": 0,
        "explanation": "Đồ thị s-t chỉ cho biết thông tin về quãng đường, thời gian và tốc độ, không cho biết khối lượng."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Gốc tọa độ O (0; 0) trên đồ thị s - t thường ứng với:",
        "options": [
          "Thời điểm bắt đầu khảo sát chuyển động và vị trí mốc xuất phát",
          "Thời điểm vật dừng lại",
          "Thời điểm vật đạt tốc độ tối đa",
          "Vị trí đích đến"
        ],
        "correct": 0,
        "explanation": "Gốc O biểu diễn t = 0 và s = 0."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t biểu diễn một người đi bộ: sau 2 giờ đi được 8 km. Tốc độ của người đó là:",
        "options": [
          "4 km/h",
          "8 km/h",
          "2 km/h",
          "16 km/h"
        ],
        "correct": 0,
        "explanation": "v = s / t = 8 / 2 = 4 km/h."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Trên đồ thị s - t, trong khoảng thời gian từ t = 1 h đến t = 2 h, đồ thị là đoạn nằm ngang ở mức s = 40 km. Điều đó có nghĩa là:",
        "options": [
          "Trong khoảng thời gian này vật dừng lại không chuyển động",
          "Vật chạy với tốc độ 40 km/h",
          "Vật quay đầu trở lại",
          "Vật tăng tốc rất nhanh"
        ],
        "correct": 0,
        "explanation": "Đoạn nằm ngang biểu thị s không đổi, vật đang đứng yên (dừng nghỉ)."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Hai xe A và B có đồ thị s - t là hai đường thẳng dốc lên. Đường đồ thị của xe A dốc hơn đường của xe B. Kết luận nào đúng?",
        "options": [
          "Xe A chuyển động nhanh hơn xe B",
          "Xe B chuyển động nhanh hơn xe A",
          "Hai xe chuyển động nhanh như nhau",
          "Không thể so sánh"
        ],
        "correct": 0,
        "explanation": "Đường đồ thị càng dốc chứng tỏ trong cùng một khoảng thời gian vật đi được quãng đường lớn hơn => tốc độ lớn hơn."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Một ô tô chuyển động đều có đồ thị s - t đi qua điểm M (3 h; 150 km). Quãng đường ô tô đi được sau 5 giờ là:",
        "options": [
          "250 km",
          "200 km",
          "300 km",
          "150 km"
        ],
        "correct": 0,
        "explanation": "v = 150 / 3 = 50 km/h => s = 50 × 5 = 250 km."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một người chạy bộ có đồ thị s - t gồm hai giai đoạn: Giai đoạn 1 đi 300 m trong 50 s; Giai đoạn 2 đi 200 m trong 50 s. So sánh tốc độ v1 và v2:",
        "options": [
          "v1 > v2",
          "v1 < v2",
          "v1 = v2",
          "v1 = 0"
        ],
        "correct": 0,
        "explanation": "v1 = 300 / 50 = 6 m/s; v2 = 200 / 50 = 4 m/s => v1 > v2."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Quan sát đồ thị s - t, nếu hai đường đồ thị của hai vật cắt nhau tại điểm K(t0; s0) thì điều đó có ý nghĩa là:",
        "options": [
          "Tại thời điểm t0, hai vật gặp nhau ở cùng vị trí cách mốc s0",
          "Hai vật va chạm nổ tung",
          "Hai vật dừng lại vĩnh viễn",
          "Hai vật đổi hướng chuyển động vuông góc"
        ],
        "correct": 0,
        "explanation": "Điểm cắt nhau biểu diễn thời điểm và vị trí hai vật gặp nhau."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các tính chất cơ bản của đồ thị quãng đường - thời gian (s - t):",
        "statements": [
          {
            "subId": "a",
            "text": "Trục Ot thường được chọn làm trục hoành nằm ngang.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trục Os được chọn làm trục tung thẳng đứng hướng lên.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đường đồ thị càng dốc đứng thì tốc độ chuyển động của vật càng lớn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đoạn đồ thị dốc xuống về trục hoành biểu thị vật bị tiêu biến mất.",
            "correct": false
          }
        ],
        "explanation": "Đoạn dốc xuống biểu thị khoảng cách của vật so với mốc giảm dần (vật chuyển động quay về mốc)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Phân tích đồ thị chuyển động của một xe máy trên tuyến đường dài 90 km:",
        "statements": [
          {
            "subId": "a",
            "text": "Đoạn 1 từ t = 0 đến t = 1 h xe đi từ s = 0 đến s = 40 km với tốc độ 40 km/h.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đoạn 2 từ t = 1 h đến t = 1,5 h đường đồ thị nằm ngang, xe dừng nghỉ 30 phút.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đoạn 3 từ t = 1,5 h đến t = 2,5 h xe đi tiếp từ s = 40 km đến s = 90 km với tốc độ 50 km/h.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình trên toàn bộ chuyến đi tính cả thời gian nghỉ là 45 km/h.",
            "correct": false
          }
        ],
        "explanation": "Tổng quãng đường = 90 km, tổng thời gian = 2,5 h => v_tb = 90 / 2,5 = 36 km/h."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hai bạn học sinh Nam và Hùng cùng đạp xe từ trường về nhà trên một con đường thẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Đồ thị s - t của Nam đi qua gốc O(0; 0) và điểm A(20 min; 4 km).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ đạp xe của Nam là 12 km/h.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đồ thị của Hùng đi qua điểm B(30 min; 4,5 km), tốc độ của Hùng là 9 km/h.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trên đường đi, Hùng chuyển động nhanh hơn Nam.",
            "correct": false
          }
        ],
        "explanation": "Nam chạy 12 km/h nhanh hơn Hùng chạy 9 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một xe chở hàng chuyển động được mô tả bởi đồ thị s - t chia làm 2 giai đoạn:",
        "statements": [
          {
            "subId": "a",
            "text": "Giai đoạn 1: trong 2 giờ đầu đi được 80 km.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Giai đoạn 2: trong 1 giờ tiếp theo đi được thêm 60 km.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ ở giai đoạn 2 lớn hơn tốc độ ở giai đoạn 1.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Độ dốc của đồ thị ở giai đoạn 1 lớn hơn độ dốc ở giai đoạn 2.",
            "correct": false
          }
        ],
        "explanation": "v1 = 40 km/h, v2 = 60 km/h => giai đoạn 2 có tốc độ lớn hơn nên đồ thị dốc hơn giai đoạn 1."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Từ đồ thị s - t, vật đi được 120 m trong 15 giây. Tốc độ của vật là bao nhiêu m/s?",
        "correctAnswer": "8",
        "explanation": "v = 120 / 15 = 8 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một đồ thị s - t chỉ ra xe chạy với tốc độ 60 km/h. Sau 3 giờ xe đi được bao nhiêu km?",
        "correctAnswer": "180",
        "explanation": "s = 60 × 3 = 180 km."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Đồ thị s - t của một người đi bộ gồm: đoạn dốc lên từ 0 đến 3 km trong 0,5 h, sau đó nằm ngang 0,2 h. Thời gian dừng nghỉ là bao nhiêu phút?",
        "correctAnswer": "12",
        "explanation": "0,2 h = 0,2 × 60 = 12 phút."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Từ đồ thị s - t, lúc t = 1 h xe ở vị trí 30 km, lúc t = 3 h xe ở vị trí 110 km. Tốc độ của xe trong khoảng thời gian này là bao nhiêu km/h?",
        "correctAnswer": "40",
        "explanation": "v = (110 - 30) / (3 - 1) = 80 / 2 = 40 km/h."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Đồ thị của xe A là s = 50t, đồ thị của xe B xuất phát cùng lúc từ vị trí s = 20 km với s = 30t + 20. Hai xe gặp nhau sau bao nhiêu giờ?",
        "correctAnswer": "1",
        "explanation": "50t = 30t + 20 => 20t = 20 => t = 1 h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một người chạy bộ có đồ thị s - t là đường thẳng đi qua điểm (10 s; 40 m). Để đi hết quãng đường 200 m, người đó cần bao nhiêu giây?",
        "correctAnswer": "50",
        "explanation": "v = 40 / 10 = 4 m/s => t = 200 / 4 = 50 s."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một xe ô tô khởi hành từ A lúc 7h00 sáng để đi đến B. Đồ thị s - t của xe gồm: đoạn 1 chạy đều với tốc độ 60 km/h trong 1,5 giờ; đoạn 2 xe dừng nghỉ 30 phút tại trạm dừng chân; đoạn 3 chạy tiếp quãng đường 50 km với tốc độ 50 km/h đến đích. Xe đến B vào thời điểm nào trong ngày?",
        "options": [
          "10h00 sáng",
          "9h30 sáng",
          "10h30 sáng",
          "11h00 trưa"
        ],
        "correct": 0,
        "explanation": "Thời gian đoạn 1: 1,5 h. Thời gian đoạn 2: 0,5 h. Thời gian đoạn 3: 50 / 50 = 1,0 h. Tổng thời gian: 3,0 h. Đến nơi lúc: 7h00 + 3h = 10h00 sáng."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Đồ thị s - t của hai vật 1 và 2 cùng xuất phát từ một điểm chuyển động cùng chiều. Vật 1 có phương trình đồ thị s1 = 40t (km), vật 2 xuất phát sau vật 1 một khoảng thời gian 0,5 giờ và chạy với tốc độ 60 km/h (s2 = 60(t - 0,5)). Thời điểm hai vật gặp nhau cách thời điểm xuất phát của vật 1 là:",
        "options": [
          "1,5 giờ",
          "1,0 giờ",
          "2,0 giờ",
          "2,5 giờ"
        ],
        "correct": 0,
        "explanation": "40t = 60(t - 0,5) => 40t = 60t - 30 => 20t = 30 => t = 1,5 h."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một vận động viên leo núi có đồ thị s - t như sau: leo lên dốc 3 km với tốc độ 2 km/h; nghỉ trên đỉnh núi 45 phút; leo xuống dốc 3 km theo đường cũ với tốc độ 4 km/h. Tốc độ trung bình của vận động viên trong cả chuyến leo núi kể cả thời gian nghỉ là:",
        "options": [
          "2,0 km/h",
          "2,5 km/h",
          "3,0 km/h",
          "1,8 km/h"
        ],
        "correct": 0,
        "explanation": "t_lên = 3 / 2 = 1,5 h; t_nghỉ = 45 phút = 0,75 h; t_xuống = 3 / 4 = 0,75 h. Tổng t = 1,5 + 0,75 + 0,75 = 3 h. Tổng s = 6 km => v_tb = 6 / 3 = 2 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu chở hàng rời ga với đồ thị s - t biểu diễn: trong 10 phút đầu đi được 5 km; trong 20 phút tiếp theo đi được 20 km; trong 10 phút cuối giảm tốc đi được 5 km thì dừng lại ở ga kế tiếp. Tốc độ trung bình trên toàn tuyến đường nối hai ga là:",
        "options": [
          "45 km/h",
          "60 km/h",
          "30 km/h",
          "40 km/h"
        ],
        "correct": 0,
        "explanation": "Tổng s = 5 + 20 + 5 = 30 km. Tổng t = 10 + 20 + 10 = 40 phút = 2/3 h => v_tb = 30 / (2/3) = 45 km/h."
      }
    ]
  },
  "phys7_c3_b10_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 10: Đồ thị quãng đường - thời gian - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b10",
    "lessonName": "Bài 10: Đồ thị quãng đường - thời gian",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Để vẽ đồ thị quãng đường - thời gian của một chuyển động, bước đầu tiên cần làm là:",
        "options": [
          "Lập bảng ghi các giá trị tương ứng của quãng đường s và thời gian t",
          "Vẽ ngay một đường thẳng bất kì",
          "Tính gia tốc của chuyển động",
          "Đo nhiệt độ môi trường"
        ],
        "correct": 0,
        "explanation": "Cần lập bảng số liệu thu thập quãng đường s tương ứng với các mốc thời gian t."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Điểm biểu diễn chuyển động trên mặt phẳng tọa độ (s - t) có tọa độ dạng:",
        "options": [
          "(t; s)",
          "(s; t)",
          "(v; t)",
          "(s; v)"
        ],
        "correct": 0,
        "explanation": "Tọa độ điểm trên đồ thị s-t có hoành độ là t và tung độ là s: (t; s)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Nếu đồ thị quãng đường - thời gian của một vật là một đường gấp khúc gồm các đoạn thẳng nối tiếp nhau thì chuyển động của vật là:",
        "options": [
          "Chuyển động gồm nhiều giai đoạn chuyển động đều với các tốc độ khác nhau",
          "Chuyển động tròn đều",
          "Chuyển động biến đổi đều liên tục",
          "Vật đứng yên hoàn toàn"
        ],
        "correct": 0,
        "explanation": "Đường gấp khúc gồm các đoạn thẳng biểu diễn các chặng chuyển động thẳng đều khác nhau."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong đồ thị s - t, đoạn đồ thị nào sau đây thể hiện vật chuyển động nhanh nhất?",
        "options": [
          "Đoạn có độ nghiêng so với trục Ot lớn nhất",
          "Đoạn nằm ngang",
          "Đoạn có độ nghiêng nhỏ nhất",
          "Đoạn ngắn nhất"
        ],
        "correct": 0,
        "explanation": "Độ nghiêng (độ dốc) càng lớn thì tốc độ v = Δs / Δt càng lớn."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Khi vật chuyển động thẳng đều, tỉ số giữa độ biến thiên quãng đường Δs và độ biến thiên thời gian Δt luôn:",
        "options": [
          "Không đổi theo thời gian và bằng tốc độ của vật",
          "Tăng dần theo thời gian",
          "Giảm dần về 0",
          "Bằng 0"
        ],
        "correct": 0,
        "explanation": "Trong chuyển động đều, v = Δs / Δt là hằng số không đổi."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trên đồ thị s - t, một đoạn thẳng nằm trùng khít với trục thời gian Ot biểu diễn trạng thái:",
        "options": [
          "Vật đứng yên tại gốc mốc tọa độ (s = 0)",
          "Vật đang chạy với tốc độ cực đại",
          "Vật đang bay lên trời",
          "Vật chuyển động lùi"
        ],
        "correct": 0,
        "explanation": "Trùng trục Ot nghĩa là s = 0 ở mọi thời điểm t, vật đứng yên tại vị trí mốc."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t của một xe đạp đi qua điểm A(0,5 h; 9 km). Tốc độ của xe đạp là:",
        "options": [
          "18 km/h",
          "9 km/h",
          "4,5 km/h",
          "15 km/h"
        ],
        "correct": 0,
        "explanation": "v = 9 / 0,5 = 18 km/h."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một vật chuyển động có đồ thị s - t: từ t = 0 đến t = 20 s đi được 100 m; từ t = 20 s đến t = 50 s đi thêm 150 m. So sánh tốc độ v1 và v2:",
        "options": [
          "v1 = v2 = 5 m/s",
          "v1 > v2",
          "v1 < v2",
          "v2 = 0"
        ],
        "correct": 0,
        "explanation": "v1 = 100 / 20 = 5 m/s; v2 = 150 / (50 - 20) = 150 / 30 = 5 m/s => v1 = v2."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Quan sát đồ thị s - t của hai người đi xe máy khởi hành cùng lúc: sau 1 giờ, người A đi được 45 km, người B đi được 35 km. Nhận xét nào đúng?",
        "options": [
          "Đường đồ thị của người A dốc hơn đường đồ thị của người B",
          "Đường đồ thị của người B dốc hơn",
          "Hai đường đồ thị song song",
          "Hai đường đồ thị trùng nhau"
        ],
        "correct": 0,
        "explanation": "Người A có tốc độ 45 km/h lớn hơn người B (35 km/h) nên đồ thị của A dốc hơn."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Một ô tô có đồ thị s - t đi qua điểm (2 h; 80 km). Để đi được quãng đường 200 km, ô tô cần thời gian là:",
        "options": [
          "5 giờ",
          "4 giờ",
          "6 giờ",
          "4,5 giờ"
        ],
        "correct": 0,
        "explanation": "v = 80 / 2 = 40 km/h => t = 200 / 40 = 5 giờ."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t của một ca nô đi trên hồ: đoạn 1 dốc lên ứng với v1 = 30 km/h trong 1 h; đoạn 2 nằm ngang dài 30 phút. Quãng đường ca nô đi được sau 1,5 h là:",
        "options": [
          "30 km",
          "45 km",
          "60 km",
          "15 km"
        ],
        "correct": 0,
        "explanation": "30 phút sau ca nô dừng lại nên quãng đường giữ nguyên là 30 km."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Trên đồ thị s - t của chuyển động thẳng, nếu một đường dốc xuống từ mức s = 60 km về s = 0 trong thời gian 1,5 h thì có nghĩa là:",
        "options": [
          "Vật chuyển động đều quay trở về điểm xuất phát với tốc độ 40 km/h",
          "Vật bị lùi xe với tốc độ âm",
          "Quãng đường bị giảm đi",
          "Vật biến mất"
        ],
        "correct": 0,
        "explanation": "Đồ thị dốc về gốc s = 0 biểu diễn vật chuyển động đều từ khoảng cách 60 km quay về mốc ban đầu với tốc độ 60 / 1,5 = 40 km/h."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét ý nghĩa các dạng đường trên đồ thị quãng đường - thời gian (s - t):",
        "statements": [
          {
            "subId": "a",
            "text": "Đường thẳng dốc lên thể hiện chuyển động thẳng đều.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đường nằm ngang song song trục Ot thể hiện trạng thái đứng yên.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đường thẳng càng gần phương thẳng đứng thì tốc độ chuyển động càng chậm.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Giao điểm của hai đường đồ thị cho biết thời điểm và vị trí hai vật gặp nhau.",
            "correct": true
          }
        ],
        "explanation": "Càng gần phương thẳng đứng thì độ dốc càng lớn, tốc độ càng nhanh."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Phân tích đồ thị chuyển động của vận động viên chạy cự li 1500 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong 400 m đầu tiên vận động viên chạy hết 60 giây.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ ở chặng 400 m đầu là xấp xỉ 6,67 m/s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ở chặng giữa 800 m tiếp theo vận động viên duy trì tốc độ đều 5 m/s trong 160 s.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Vận động viên đứng yên hoàn toàn ở chặng nước rút 300 m cuối.",
            "correct": false
          }
        ],
        "explanation": "Chặng nước rút cuối cùng vận động viên phải tăng tốc về đích, không thể đứng yên."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hai xe ô tô xuất phát từ cùng một vị trí và đi cùng một hướng:",
        "statements": [
          {
            "subId": "a",
            "text": "Xe 1 có đồ thị là đường thẳng s1 = 45t.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Xe 2 có đồ thị là đường thẳng s2 = 60t.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sau 2 giờ, xe 2 đi trước xe 1 một khoảng cách là 30 km.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đồ thị của xe 1 có độ dốc lớn hơn đồ thị của xe 2.",
            "correct": false
          }
        ],
        "explanation": "v2 = 60 km/h > v1 = 45 km/h nên đồ thị xe 2 dốc hơn xe 1."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hành trình của một người đi xe đạp từ nhà đến bưu điện rồi quay về nhà:",
        "statements": [
          {
            "subId": "a",
            "text": "Từ nhà đến bưu điện dài 6 km đi hết 24 phút (0,4 h).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ lúc đi là 15 km/h.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Người đó gửi thư tại bưu điện mất 16 phút (khoảng thời gian đồ thị nằm ngang).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Lúc quay về nhà hết 30 phút, tốc độ lúc về nhanh hơn lúc đi.",
            "correct": false
          }
        ],
        "explanation": "Lúc về v = 6 / 0,5 = 12 km/h chậm hơn lúc đi (15 km/h)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Trên đồ thị s - t, vật đi được quãng đường 90 m trong 18 s. Tốc độ chuyển động là bao nhiêu m/s?",
        "correctAnswer": "5",
        "explanation": "v = 90 / 18 = 5 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t của ô tô có tốc độ 50 km/h. Sau 2,5 giờ ô tô đi được quãng đường bao nhiêu km?",
        "correctAnswer": "125",
        "explanation": "s = 50 × 2,5 = 125 km."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Đồ thị s - t biểu diễn một vật: từ 0 đến 1 h đi 40 km, sau đó dừng lại nghỉ 0,5 h. Tổng thời gian của hành trình tính đến khi nghỉ xong là bao nhiêu phút?",
        "correctAnswer": "90",
        "explanation": "1 h + 0,5 h = 1,5 h = 90 phút."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Từ đồ thị s - t, lúc t = 2 h xe ở vị trí s = 60 km, lúc t = 5 h xe ở vị trí s = 180 km. Tốc độ trung bình trong khoảng thời gian này là bao nhiêu km/h?",
        "correctAnswer": "40",
        "explanation": "v = (180 - 60) / (5 - 2) = 120 / 3 = 40 km/h."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Xe 1 chuyển động với đồ thị s1 = 60t (km), xe 2 xuất phát từ điểm cách mốc 15 km chuyển động cùng chiều với s2 = 45t + 15 (km). Sau bao nhiêu giờ hai xe gặp nhau?",
        "correctAnswer": "1",
        "explanation": "60t = 45t + 15 => 15t = 15 => t = 1 h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một vật chuyển động đều có đồ thị s - t đi qua điểm (5 s; 35 m). Để đi hết quãng đường 140 m, vật cần thời gian bao nhiêu giây?",
        "correctAnswer": "20",
        "explanation": "v = 35 / 5 = 7 m/s => t = 140 / 7 = 20 s."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Đồ thị quãng đường - thời gian của một người đi bộ được mô tả qua 3 chặng: Chặng 1 đi đều 2 km trong 30 phút; Chặng 2 dừng uống nước 15 phút; Chặng 3 đi tiếp 3 km trong 45 phút. Tốc độ trung bình của người đó trên cả hành trình (kể cả thời gian nghỉ) là bao nhiêu km/h?",
        "options": [
          "3,33 km/h",
          "4,00 km/h",
          "3,00 km/h",
          "2,50 km/h"
        ],
        "correct": 0,
        "explanation": "Tổng s = 2 + 3 = 5 km. Tổng t = 30 + 15 + 45 = 90 phút = 1,5 h => v_tb = 5 / 1,5 ≈ 3,33 km/h."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Đồ thị s - t của hai xe máy A và B xuất phát từ cùng một điểm và đi cùng hướng. Xe A khởi hành lúc 8h00 chạy với tốc độ 30 km/h. Xe B khởi hành lúc 8h30 chạy với tốc độ 45 km/h để đuổi theo xe A. Hai xe gặp nhau lúc mấy giờ?",
        "options": [
          "9h30 sáng",
          "9h00 sáng",
          "10h00 sáng",
          "10h30 sáng"
        ],
        "correct": 0,
        "explanation": "Thời gian xe B đuổi kịp xe A: t = (30 × 0,5) / (45 - 30) = 15 / 15 = 1,0 h kể từ lúc B xuất phát. Thời điểm gặp nhau: 8h30 + 1h = 9h30 sáng."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một ô tô đồ chơi chạy trên đường thẳng có đồ thị s - t gồm: giai đoạn 1 chạy từ O đến điểm (4 s; 8 m); giai đoạn 2 đứng yên trong 2 s; giai đoạn 3 chạy tiếp đến điểm (10 s; 20 m). Tốc độ của ô tô ở giai đoạn 3 là:",
        "options": [
          "3 m/s",
          "2 m/s",
          "4 m/s",
          "2,5 m/s"
        ],
        "correct": 0,
        "explanation": "Giai đoạn 3 bắt đầu từ t = 6 s (s = 8 m) đến t = 10 s (s = 20 m) => v3 = (20 - 8) / (10 - 6) = 12 / 4 = 3 m/s."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu xuất phát từ ga A lúc 6h00 và đến ga B lúc 8h30. Đồ thị s - t cho biết tàu chạy 60 km đầu hết 1 giờ; dừng đỗ tại ga phụ 15 phút; sau đó chạy 75 km còn lại trong 1 giờ 15 phút. Tốc độ trung bình của đoàn tàu trên cả chặng đường nối hai ga A và B là:",
        "options": [
          "54 km/h",
          "60 km/h",
          "50 km/h",
          "48 km/h"
        ],
        "correct": 0,
        "explanation": "Tổng s = 60 + 75 = 135 km. Tổng t = 2,5 h => v_tb = 135 / 2,5 = 54 km/h."
      }
    ]
  },
  "phys7_c3_b10_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 10: Đồ thị quãng đường - thời gian - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b10",
    "lessonName": "Bài 10: Đồ thị quãng đường - thời gian",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị quãng đường - thời gian biểu diễn sự phụ thuộc của:",
        "options": [
          "Quãng đường đi được vào thời gian chuyển động",
          "Thời gian chuyển động vào khối lượng",
          "Tốc độ vào gia tốc",
          "Lực kéo vào vận tốc"
        ],
        "correct": 0,
        "explanation": "Đồ thị biểu diễn hàm số s theo biến số thời gian t: s = s(t)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong đồ thị s - t, đơn vị thường dùng của trục quãng đường và trục thời gian lần lượt là:",
        "options": [
          "Mét (m) và Giây (s) hoặc Kilômét (km) và Giờ (h)",
          "Giây và Mét",
          "Mét và Kilôgam",
          "Lít và Giây"
        ],
        "correct": 0,
        "explanation": "Hệ đơn vị tương ứng: (m; s) hoặc (km; h)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Nếu đồ thị s - t của một vật là một đường cong uốn lượn có độ dốc tăng dần thì chuyển động của vật là:",
        "options": [
          "Chuyển động có tốc độ tăng dần theo thời gian (chuyển động nhanh dần)",
          "Chuyển động thẳng đều",
          "Chuyển động đứng yên",
          "Chuyển động chậm dần"
        ],
        "correct": 0,
        "explanation": "Độ dốc tăng dần đồng nghĩa với tốc độ tức thời tăng dần."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Để xác định thời gian cần thiết để đi được quãng đường s0 từ đồ thị s - t, ta thực hiện:",
        "options": [
          "Từ giá trị s0 trên trục tung Os, kẻ đường song song với trục hoành Ot cắt đồ thị tại điểm M, rồi gióng xuống trục Ot để đọc giá trị t0",
          "Gióng trực tiếp từ gốc O",
          "Đo chiều dài thước kẻ",
          "Lấy s0 nhân với 3,6"
        ],
        "correct": 0,
        "explanation": "Phương pháp đọc đồ thị: gióng ngang từ s0 sang đồ thị rồi gióng dọc xuống trục Ot."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Đồ thị quãng đường - thời gian của một đoàn tàu đang đỗ tại sân ga là:",
        "options": [
          "Một đoạn thẳng nằm ngang song song trục Ot",
          "Một đường thẳng xiên góc 45 độ",
          "Một đường thẳng đứng song song trục Os",
          "Một đường parabol cong"
        ],
        "correct": 0,
        "explanation": "Đang đỗ tại ga nghĩa là vật đứng yên, quãng đường không đổi theo thời gian."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Độ dốc của đồ thị s - t bằng 0 khi nào?",
        "options": [
          "Khi vật đứng yên (đoạn đồ thị nằm ngang)",
          "Khi vật chạy cực nhanh",
          "Khi vật đổi hướng chuyển động",
          "Khi vật xuất phát"
        ],
        "correct": 0,
        "explanation": "Đoạn nằm ngang có độ dốc bằng 0, tương ứng tốc độ v = 0."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t của một ô tô đi qua điểm B(1,5 h; 75 km). Tốc độ của ô tô là:",
        "options": [
          "50 km/h",
          "75 km/h",
          "112,5 km/h",
          "60 km/h"
        ],
        "correct": 0,
        "explanation": "v = 75 / 1,5 = 50 km/h."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một người chạy bộ có đồ thị s - t đi qua điểm (30 s; 180 m). Tốc độ chạy của người đó tính theo km/h là:",
        "options": [
          "21,6 km/h",
          "6,0 km/h",
          "18,0 km/h",
          "15,5 km/h"
        ],
        "correct": 0,
        "explanation": "v = 180 / 30 = 6 m/s = 6 × 3,6 = 21,6 km/h."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Trên đồ thị s - t, đường chuyển động của xe 1 hợp với trục Ot một góc 30 độ, đường của xe 2 hợp với trục Ot một góc 60 độ. Kết luận nào đúng?",
        "options": [
          "Xe 2 chuyển động nhanh hơn xe 1",
          "Xe 1 chuyển động nhanh hơn xe 2",
          "Hai xe chạy cùng tốc độ",
          "Xe 2 đứng yên"
        ],
        "correct": 0,
        "explanation": "Góc hợp với trục Ot càng lớn thì độ dốc càng lớn => tốc độ càng nhanh (tan 60° > tan 30°)."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t của một học sinh đi xe đạp: từ 0 đến 10 phút đi được 2 km; từ 10 đến 25 phút đi thêm 3 km. Tốc độ trung bình trên toàn tuyến 5 km là:",
        "options": [
          "12 km/h",
          "10 km/h",
          "15 km/h",
          "8 km/h"
        ],
        "correct": 0,
        "explanation": "Tổng s = 5 km, tổng t = 25 phút = 25/60 h = 5/12 h => v_tb = 5 / (5/12) = 12 km/h."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một xe khách có đồ thị s - t biểu diễn qua 2 chặng: chặng 1 chạy 60 km/h trong 2 h; chặng 2 chạy 40 km/h trong 1 h. Quãng đường tổng cộng xe đã đi là:",
        "options": [
          "160 km",
          "100 km",
          "120 km",
          "150 km"
        ],
        "correct": 0,
        "explanation": "s = (60 × 2) + (40 × 1) = 120 + 40 = 160 km."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t của hai vật xuất phát cùng lúc từ vị trí mốc s = 0. Sau thời gian t1, đồ thị của vật A ở mức s = 50 m, đồ thị vật B ở mức s = 30 m. Nhận xét nào đúng?",
        "options": [
          "Vật A có tốc độ lớn hơn vật B",
          "Vật B có tốc độ lớn hơn vật A",
          "Hai vật có tốc độ bằng nhau",
          "Không thể kết luận được"
        ],
        "correct": 0,
        "explanation": "Cùng thời gian t1, vật A đi được quãng đường lớn hơn nên chuyển động nhanh hơn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về phương pháp khai thác thông tin từ đồ thị quãng đường - thời gian:",
        "statements": [
          {
            "subId": "a",
            "text": "Biết thời gian t có thể tra cứu được quãng đường s tương ứng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Biết quãng đường s có thể xác định được thời gian t cần thiết.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ tại một giai đoạn bằng thương số giữa độ dài đoạn quãng đường và thời gian đi đoạn đó.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đồ thị s - t không thể cho biết khi nào vật dừng lại nghỉ ngơi.",
            "correct": false
          }
        ],
        "explanation": "Các đoạn nằm ngang trên đồ thị cho biết chính xác thời điểm và khoảng thời gian vật dừng nghỉ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Phân tích đồ thị chuyển động của một xe buýt nội thành:",
        "statements": [
          {
            "subId": "a",
            "text": "Đồ thị gồm nhiều đoạn dốc lên xen kẽ với các đoạn nằm ngang ngắn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Các đoạn dốc lên thể hiện xe buýt đang di chuyển giữa các trạm dừng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Các đoạn nằm ngang thể hiện xe buýt đang dừng đón và trả khách tại các trạm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Chuyển động của xe buýt trên toàn bộ tuyến đường là chuyển động thẳng đều.",
            "correct": false
          }
        ],
        "explanation": "Xe buýt di chuyển có dừng đỗ và thay đổi tốc độ liên tục nên là chuyển động không đều."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hai bạn An và Bình cùng thi chạy trên quãng đường 100 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Đồ thị s - t của An đi qua điểm (12,5 s; 100 m), tốc độ của An là 8 m/s.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đồ thị s - t của Bình đi qua điểm (16,0 s; 100 m), tốc độ của Bình là 6,25 m/s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "An về đích trước Bình một khoảng thời gian là 3,5 giây.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đường đồ thị của Bình dốc hơn đường đồ thị của An.",
            "correct": false
          }
        ],
        "explanation": "An chạy nhanh hơn (8 m/s > 6,25 m/s) nên đường đồ thị của An dốc hơn Bình."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một xe tải chở vật liệu có đồ thị chuyển động biểu diễn:",
        "statements": [
          {
            "subId": "a",
            "text": "Chặng đầu: xe chạy từ mốc 0 đến 45 km trong 1 giờ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Xe dừng bốc dỡ hàng hóa trong 45 phút (0,75 giờ).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chặng sau: xe chạy tiếp từ km 45 đến km 90 trong 1 giờ 15 phút (1,25 giờ).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình trên toàn tuyến đường tính cả thời gian bốc dỡ hàng là 40 km/h.",
            "correct": false
          }
        ],
        "explanation": "Tổng s = 90 km, tổng t = 1 + 0,75 + 1,25 = 3 h => v_tb = 90 / 3 = 30 km/h."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Từ đồ thị s - t, một vật đi được 150 m trong thời gian 25 s. Tốc độ của vật là bao nhiêu m/s?",
        "correctAnswer": "6",
        "explanation": "v = 150 / 25 = 6 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một ô tô có đồ thị s - t biểu thị tốc độ 80 km/h. Sau 1,5 giờ ô tô đi được bao nhiêu km?",
        "correctAnswer": "120",
        "explanation": "s = 80 × 1,5 = 120 km."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Đồ thị s - t có đoạn nằm ngang từ t = 45 phút đến t = 75 phút. Thời gian vật dừng nghỉ là bao nhiêu phút?",
        "correctAnswer": "30",
        "explanation": "75 - 45 = 30 phút."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Lúc t = 1 h xe ở vị trí s = 25 km, lúc t = 4 h xe ở vị trí s = 145 km. Tốc độ trung bình trong khoảng thời gian này là bao nhiêu km/h?",
        "correctAnswer": "40",
        "explanation": "v = (145 - 25) / (4 - 1) = 120 / 3 = 40 km/h."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Xe máy có đồ thị s1 = 40t, ô tô xuất phát cùng lúc từ vị trí s = 10 km với s2 = 60t + 10. Khoảng cách giữa hai xe sau 2 giờ là bao nhiêu km?",
        "correctAnswer": "50",
        "explanation": "s1 = 80 km; s2 = 120 + 10 = 130 km => khoảng cách = 130 - 80 = 50 km."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một vật chuyển động đều có đồ thị s - t đi qua điểm (4 s; 24 m). Thời gian để vật đi hết quãng đường 180 m là bao nhiêu giây?",
        "correctAnswer": "30",
        "explanation": "v = 24 / 4 = 6 m/s => t = 180 / 6 = 30 s."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Đồ thị s - t của một người đạp xe biểu diễn: chặng 1 đi quãng đường 8 km với tốc độ 16 km/h; chặng 2 nghỉ giải lao 15 phút; chặng 3 đi tiếp quãng đường 12 km với tốc độ 12 km/h. Tốc độ trung bình của người đạp xe trên toàn bộ quãng đường 20 km kể cả thời gian nghỉ giải lao là:",
        "options": [
          "11,43 km/h",
          "14,00 km/h",
          "10,50 km/h",
          "12,50 km/h"
        ],
        "correct": 0,
        "explanation": "t1 = 8 / 16 = 0,5 h; t2 = 15/60 = 0,25 h; t3 = 12 / 12 = 1,0 h. Tổng t = 1,75 h. v_tb = 20 / 1,75 ≈ 11,43 km/h."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Đồ thị s - t của hai người đi bộ A và B khởi hành cùng lúc từ hai vị trí cách nhau 10 km đi ngược chiều nhau. Người A có đồ thị sA = 4t (km), người B có đồ thị sB = 10 - 6t (km). Hai người gặp nhau sau bao nhiêu giờ và cách vị trí xuất phát của A bao nhiêu km?",
        "options": [
          "1,0 giờ và cách A 4 km",
          "1,5 giờ và cách A 6 km",
          "0,8 giờ và cách A 3,2 km",
          "2,0 giờ và cách A 8 km"
        ],
        "correct": 0,
        "explanation": "4t = 10 - 6t => 10t = 10 => t = 1,0 h. Vị trí gặp nhau s = 4 × 1 = 4 km."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một ca nô chạy trên hồ nước yên lặng có đồ thị s - t gồm: giai đoạn 1 chạy đều với tốc độ 24 km/h trong 45 phút (0,75 h); giai đoạn 2 dừng lại câu cá trong 30 phút (0,5 h); giai đoạn 3 chạy quay trở về điểm xuất phát ban đầu trong 45 phút. Tốc độ của ca nô ở giai đoạn 3 quay về là:",
        "options": [
          "24 km/h",
          "18 km/h",
          "30 km/h",
          "16 km/h"
        ],
        "correct": 0,
        "explanation": "Quãng đường lúc đi s = 24 × 0,75 = 18 km. Lúc về đi 18 km trong 0,75 h => v3 = 18 / 0,75 = 24 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu hỏa rời ga A đi đến ga B với đồ thị s - t: 15 phút đầu chạy tăng tốc dần đi được 10 km; 45 phút tiếp theo chạy đều với tốc độ 80 km/h đi được 60 km; 15 phút cuối giảm tốc đi được 10 km thì dừng lại tại ga B. Tổng quãng đường giữa hai ga và tốc độ trung bình của đoàn tàu là:",
        "options": [
          "80 km và 64 km/h",
          "75 km và 60 km/h",
          "80 km và 70 km/h",
          "90 km và 72 km/h"
        ],
        "correct": 0,
        "explanation": "Tổng s = 10 + 60 + 10 = 80 km. Tổng t = 15 + 45 + 15 = 75 phút = 1,25 h => v_tb = 80 / 1,25 = 64 km/h."
      }
    ]
  },
  "phys7_c3_b11_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b11",
    "lessonName": "Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Biển báo giao thông hình tròn viền đỏ, nền trắng, bên trong có ghi số '60' màu đen là biển báo:",
        "options": [
          "Hạn chế tốc độ tối đa không được vượt quá 60 km/h",
          "Tốc độ tối thiểu phải chạy là 60 km/h",
          "Khoảng cách giữa hai xe là 60 m",
          "Cấm xe có trọng tải trên 60 tấn"
        ],
        "correct": 0,
        "explanation": "Biển P.127 giới hạn tốc độ tối đa cho phép."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Theo quy định an toàn giao thông đường bộ, khi chạy xe với tốc độ càng cao thì khoảng cách an toàn tối thiểu giữa hai xe phải:",
        "options": [
          "Càng lớn hơn",
          "Càng nhỏ lại",
          "Giữ nguyên không đổi",
          "Bằng 0"
        ],
        "correct": 0,
        "explanation": "Tốc độ càng cao thì quãng đường phanh dừng càng dài nên khoảng cách an toàn phải càng lớn."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Quy tắc an toàn 'Khoảng cách 3 giây' khi lái xe trên đường cao tốc giúp người lái xe:",
        "options": [
          "Đủ thời gian nhận biết chướng ngại vật, phản xạ và phanh dừng xe an toàn",
          "Chạy xe với tốc độ gấp đôi",
          "Tiết kiệm nhiên liệu",
          "Vượt xe phía trước dễ dàng"
        ],
        "correct": 0,
        "explanation": "Quy tắc 3 giây đảm bảo cự li phản ứng và hãm phanh khi xe phía trước phanh gấp."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi điều kiện thời tiết có mưa to, sương mù làm đường trơn trượt, người lái xe cần:",
        "options": [
          "Chủ động giảm tốc độ và tăng khoảng cách an toàn so với xe phía trước",
          "Tăng tốc chạy thật nhanh về nhà",
          "Đi sát đuôi xe phía trước để bám đuôi",
          "Tắt toàn bộ đèn xe"
        ],
        "correct": 0,
        "explanation": "Mưa làm giảm độ ma sát lốp xe với mặt đường, tăng quãng đường trượt nên phải giảm tốc và tăng cự li."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Thiết bị an toàn nào trên ô tô được thiết kế để giữ chặt cơ thể hành khách, giảm nguy cơ va đập vào vô lăng hoặc văng ra ngoài khi có va chạm?",
        "options": [
          "Dây an toàn (seatbelt)",
          "Gương chiếu hậu",
          "Cần gạt nước",
          "Đèn pha"
        ],
        "correct": 0,
        "explanation": "Dây an toàn giữ người ngồi cố định vào ghế theo quán tính khi phanh gấp."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Biển báo giao thông hình tròn nền xanh, bên trong có số '60' màu trắng là biển báo:",
        "options": [
          "Tốc độ tối thiểu cho phép (phương tiện không được chạy dưới 60 km/h)",
          "Tốc độ tối đa cho phép",
          "Khoảng cách 60 m",
          "Hết mọi lệnh cấm"
        ],
        "correct": 0,
        "explanation": "Biển R.306 quy định tốc độ tối thiểu cho phép trên các làn xe cao tốc."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tại sao khi ô tô chạy với tốc độ 100 km/h gặp sự cố thì hậu quả va chạm nghiêm trọng hơn rất nhiều so với khi chạy 50 km/h?",
        "options": [
          "Vì động năng của xe tỉ lệ với bình phương tốc độ (tăng 2 lần tốc độ làm động năng tăng gấp 4 lần)",
          "Vì ô tô bị nặng hơn",
          "Vì động cơ xe bị hỏng",
          "Vì lốp xe bị nổ ngay lập tức"
        ],
        "correct": 0,
        "explanation": "Động năng Wđ = 1/2 m v^2. Khi tốc độ tăng 2 lần, năng lượng va chạm tăng gấp 4 lần."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một người lái xe chạy với tốc độ 72 km/h (20 m/s). Thời gian từ lúc phát hiện chướng ngại vật đến khi đạp phanh (thời gian phản xạ) là 0,8 giây. Trong thời gian phản xạ đó, xe đi được quãng đường là:",
        "options": [
          "16 m",
          "20 m",
          "10 m",
          "25 m"
        ],
        "correct": 0,
        "explanation": "s_phản_xạ = v × t = 20 × 0,8 = 16 m."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Hệ thống phanh chống bó cứng ABS (Anti-lock Braking System) trên các dòng xe hiện đại có tác dụng:",
        "options": [
          "Ngăn bánh xe bị khóa cứng khi phanh gấp, giúp tài xế vẫn kiểm soát được tay lái và tránh bị trượt lật",
          "Làm xe dừng lại ngay tức khắc trong 0 giây",
          "Tăng tốc độ của xe",
          "Tự động tắt động cơ"
        ],
        "correct": 0,
        "explanation": "Hệ thống ABS nhấp nhả phanh liên tục giúp bánh không bị trượt lết và giữ được hướng lái."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Theo quy định Thông tư Bộ GTVT, khi xe lưu thông với tốc độ từ trên 60 km/h đến 80 km/h trên đường khô ráo, khoảng cách an toàn tối thiểu là:",
        "options": [
          "55 m",
          "35 m",
          "70 m",
          "100 m"
        ],
        "correct": 0,
        "explanation": "Quy định cự li an toàn: 60 - 80 km/h là 55 m; 80 - 100 km/h là 70 m; 100 - 120 km/h là 100 m."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Người điều khiển phương tiện xe máy, mô tô bắt buộc phải đội mũ bảo hiểm đạt chuẩn nhằm:",
        "options": [
          "Bảo vệ vùng đầu và não bộ, giảm thiểu tối đa chấn thương sọ não khi xảy ra va chạm",
          "Tránh bụi bẩn cho mắt",
          "Tránh ánh nắng mặt trời",
          "Để nghe điện thoại dễ hơn"
        ],
        "correct": 0,
        "explanation": "Mũ bảo hiểm hấp thụ xung lực va đập, bảo vệ hộp sọ."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hành vi nào sau đây của người tham gia giao thông là vi phạm nghiêm trọng quy định an toàn về tốc độ?",
        "options": [
          "Lái xe vượt quá tốc độ tối đa cho phép ghi trên biển báo",
          "Lái xe thấp hơn tốc độ tối đa",
          "Dừng xe khi gặp đèn đỏ",
          "Bật đèn xi nhan khi chuyển làn"
        ],
        "correct": 0,
        "explanation": "Chạy quá tốc độ tối đa là hành vi vi phạm nguy hiểm hàng đầu."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về mối quan hệ giữa tốc độ xe và an toàn giao thông đường bộ:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc độ càng cao thì người lái xe càng có ít thời gian để xử lí các tình huống bất ngờ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Quãng đường phanh dừng xe tăng lên khi tốc độ chuyển động của xe tăng lên.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ không ảnh hưởng đến mức độ nghiêm trọng của chấn thương khi va chạm.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tuân thủ giới hạn tốc độ giúp giảm thiểu đáng kể số vụ tai nạn giao thông.",
            "correct": true
          }
        ],
        "explanation": "Tốc độ ảnh hưởng mang tính quyết định đến mức độ tổn thương khi va chạm."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về việc giữ khoảng cách an toàn giữa các phương tiện trên cao tốc:",
        "statements": [
          {
            "subId": "a",
            "text": "Khoảng cách an toàn là cự li tối thiểu cần duy trì với xe chạy liền phía trước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi tốc độ xe từ 80 đến 100 km/h, khoảng cách an toàn tối thiểu quy định là 70 m.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trời mưa phùn đường trơn có thể rút ngắn khoảng cách an toàn để tránh bị xe khác chen vào.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Trên đường cao tốc thường có các biển báo khoảng cách 0m - 50m - 100m để tài xế căn chỉnh.",
            "correct": true
          }
        ],
        "explanation": "Trời mưa trơn trượt bắt buộc phải tăng thêm khoảng cách an toàn, không được rút ngắn."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tài xế đang lái ô tô với tốc độ 90 km/h (25 m/s) trên đường thẳng bất ngờ thấy chướng ngại vật:",
        "statements": [
          {
            "subId": "a",
            "text": "Thời gian phản xạ của tài xế là 1,0 giây thì xe đã đi được quãng đường phản xạ là 25 m.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sau khi đạp phanh, xe cần quãng đường hãm phanh là 35 m nữa mới dừng hẳn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tổng quãng đường dừng xe an toàn tính từ lúc nhìn thấy chướng ngại vật là 60 m.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu chướng ngại vật ở cách xe 50 m thì xe dừng lại an toàn mà không bị va chạm.",
            "correct": false
          }
        ],
        "explanation": "Tổng quãng đường cần thiết là 25 + 35 = 60 m > 50 m nên xe sẽ va chạm vào chướng ngại vật."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng túi khí (Airbag) bảo vệ tính mạng trên xe ô tô:",
        "statements": [
          {
            "subId": "a",
            "text": "Túi khí được kích hoạt bung ra cực nhanh trong vài phần trăm giây khi có va chạm mạnh phía trước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Túi khí tạo ra một lớp đệm mềm hấp thụ lực va đập của phần đầu và ngực hành khách.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi đã có túi khí thì hành khách không cần phải thắt dây an toàn.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Dây an toàn và túi khí là hệ thống bảo vệ bổ trợ chặt chẽ cho nhau.",
            "correct": true
          }
        ],
        "explanation": "Nếu không thắt dây an toàn, người bị văng mạnh vào túi khí đang nổ với tốc độ cao có thể gây chấn thương nặng hơn."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Theo quy định, khoảng cách an toàn tối thiểu khi chạy xe với tốc độ trên 60 km/h đến 80 km/h trên đường khô ráo là bao nhiêu mét?",
        "correctAnswer": "55",
        "explanation": "55 mét."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một ô tô chạy với tốc độ 20 m/s. Thời gian phản xạ của lái xe là 0,7 giây. Quãng đường xe đi trong thời gian phản xạ là bao nhiêu mét?",
        "correctAnswer": "14",
        "explanation": "s = 20 × 0,7 = 14 m."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Quy tắc 3 giây trên cao tốc: Nếu xe đang chạy với tốc độ 72 km/h (20 m/s), khoảng cách an toàn 3 giây tương ứng là bao nhiêu mét?",
        "correctAnswer": "60",
        "explanation": "s = 20 × 3 = 60 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một xe máy chạy 54 km/h (15 m/s). Quãng đường phản xạ là 12 m và quãng đường hãm phanh là 18 m. Tổng quãng đường dừng xe là bao nhiêu mét?",
        "correctAnswer": "30",
        "explanation": "12 + 18 = 30 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Khoảng cách an toàn tối thiểu quy định cho xe chạy từ trên 100 km/h đến 120 km/h trên cao tốc là bao nhiêu mét?",
        "correctAnswer": "100",
        "explanation": "100 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một người lái xe đạp phanh khẩn cấp làm xe trượt trên đường một vết dài 20 m với gia tốc hãm trung bình. Nếu tốc độ xe ban đầu tăng gấp đôi thì vết trượt phanh dài bao nhiêu mét?",
        "correctAnswer": "80",
        "explanation": "Quãng đường phanh tỉ lệ với bình phương tốc độ: tăng 2 lần v => s tăng 2^2 = 4 lần: 20 × 4 = 80 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một ô tô chạy với tốc độ 90 km/h (25 m/s) trên đường cao tốc. Phía trước có một xe tải phanh gấp. Thời gian phản xạ của tài xế là 0,8 giây và quãng đường hãm phanh xe dừng hẳn là 40 m. Để không đâm vào đuôi xe tải, khoảng cách tối thiểu giữa ô tô và xe tải khi xe tải bắt đầu phanh phải là:",
        "options": [
          "60 m",
          "40 m",
          "50 m",
          "45 m"
        ],
        "correct": 0,
        "explanation": "Quãng đường phản xạ: 25 × 0,8 = 20 m. Tổng quãng đường dừng: 20 + 40 = 60 m."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Theo quy tắc 'Khoảng cách 3 giây', một xe ô tô lưu thông trên đường cao tốc Nội Bài - Lào Cai với tốc độ 108 km/h. Để đảm bảo an toàn theo quy tắc này, khoảng cách với xe liền trước cần duy trì tối thiểu là bao nhiêu mét?",
        "options": [
          "90 m",
          "108 m",
          "60 m",
          "75 m"
        ],
        "correct": 0,
        "explanation": "108 km/h = 30 m/s. Khoảng cách 3 giây: s = 30 × 3 = 90 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Khi tham gia giao thông vào ban đêm trên đoạn đường ngoài đô thị không có dải phân cách giữa, người lái xe ô tô khi gặp xe đi ngược chiều phải:",
        "options": [
          "Chuyển từ đèn chiếu xa (pha) sang đèn chiếu gần (cốt) để tránh làm lóa mắt tài xế xe đối diện",
          "Bật đèn chiếu xa thật sáng để nhìn rõ",
          "Bấm còi liên tục",
          "Tăng tốc chạy vượt qua"
        ],
        "correct": 0,
        "explanation": "Chuyển sang đèn cốt để chống chói mắt gây mù tạm thời cho tài xế xe ngược chiều."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một ô tô chạy trên đường khô ráo ở tốc độ 60 km/h thì quãng đường phanh dừng là 20 m. Khi trời mưa đường ướt, hệ số ma sát giảm một nửa làm quãng đường phanh tăng gấp đôi. Quãng đường phanh của xe trong điều kiện trời mưa ở cùng tốc độ 60 km/h là:",
        "options": [
          "40 m",
          "30 m",
          "50 m",
          "60 m"
        ],
        "correct": 0,
        "explanation": "Hệ số ma sát giảm 1/2 thì quãng đường hãm phanh tăng gấp đôi: 20 × 2 = 40 m."
      }
    ]
  },
  "phys7_c3_b11_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b11",
    "lessonName": "Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Biển báo hiệu lệnh R.420 hình chữ nhật nền xanh bên trong có hình vẽ các tòa nhà biểu thị:",
        "options": [
          "Bắt đầu khu đông dân cư (phải giảm tốc độ theo quy định)",
          "Hết khu đông dân cư",
          "Đường cao tốc dành riêng cho ô tô",
          "Khu vực cấm xe ô tô"
        ],
        "correct": 0,
        "explanation": "Biển R.420 báo hiệu bắt đầu đoạn đường qua khu đông dân cư."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Quãng đường dừng xe an toàn của một phương tiện bao gồm:",
        "options": [
          "Quãng đường xe đi được trong thời gian phản xạ cộng với quãng đường hãm phanh",
          "Chỉ quãng đường hãm phanh",
          "Chỉ quãng đường phản xạ",
          "Quãng đường xe lùi"
        ],
        "correct": 0,
        "explanation": "Quãng đường dừng xe = Quãng đường phản xạ + Quãng đường phanh."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Thời gian phản xạ của người lái xe là khoảng thời gian:",
        "options": [
          "Từ khi mắt người lái nhìn thấy chướng ngại vật đến khi chân đạp vào bàn đạp phanh",
          "Từ khi đạp phanh đến khi xe dừng lại",
          "Thời gian xe đứng yên",
          "Thời gian động cơ nổ máy"
        ],
        "correct": 0,
        "explanation": "Đó là thời gian não bộ nhận biết tín hiệu nguy hiểm và truyền lệnh vận động đến chân đạp phanh."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Việc sử dụng rượu, bia hoặc chất kích thích trước khi lái xe gây nguy hiểm vì:",
        "options": [
          "Làm tê liệt hệ thần kinh, kéo dài thời gian phản xạ và làm sai lệch phán đoán tốc độ",
          "Làm xe chạy nhanh hơn",
          "Làm lốp xe mòn nhanh hơn",
          "Làm tốn xăng hơn"
        ],
        "correct": 0,
        "explanation": "Cồn trong máu làm giảm khả năng phản xạ và kiểm soát hành vi lái xe."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Gờ giảm tốc được lắp đặt trên mặt đường tại các vị trí gần trường học, ngã tư nhằm:",
        "options": [
          "Cảnh báo và buộc các phương tiện phải giảm tốc độ",
          "Làm đẹp cảnh quan đường phố",
          "Để thoát nước mưa",
          "Làm xe tăng tốc"
        ],
        "correct": 0,
        "explanation": "Gờ giảm tốc tạo rung chấn nhắc nhở tài xế giảm tốc độ."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Khi chuyển làn đường trên cao tốc, thao tác an toàn bắt buộc phải thực hiện là:",
        "options": [
          "Bật đèn xi nhan báo rẽ, quan sát gương chiếu hậu đảm bảo an toàn rồi mới chuyển làn từ từ",
          "Đánh lái gấp sang làn bên cạnh ngay lập tức",
          "Bấm còi inh ỏi rồi rẽ",
          "Phanh dừng xe giữa đường"
        ],
        "correct": 0,
        "explanation": "Bật xi nhan cảnh báo và quan sát kĩ các góc gương chiếu hậu trước khi chuyển làn."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một xe chạy với tốc độ 54 km/h (15 m/s). Tài xế mất tập trung nhìn điện thoại 2 giây thì trong 2 giây đó xe đã đi được quãng đường là:",
        "options": [
          "30 m mà không có sự kiểm soát của tài xế",
          "15 m",
          "10 m",
          "54 m"
        ],
        "correct": 0,
        "explanation": "s = 15 × 2 = 30 m xe lao đi trong tình trạng tài xế hoàn toàn mất tập trung."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Theo quy định an toàn đối với đoạn đường khô ráo khi xe chạy từ trên 80 km/h đến 100 km/h, khoảng cách an toàn tối thiểu là:",
        "options": [
          "70 m",
          "55 m",
          "35 m",
          "100 m"
        ],
        "correct": 0,
        "explanation": "Cự li an toàn tối thiểu tương ứng là 70 m."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Lốp xe ô tô bị mòn rãnh gai quá mức cho phép sẽ gây nguy hiểm vì:",
        "options": [
          "Làm giảm độ bám đường, tăng nguy cơ trượt nước và kéo dài quãng đường phanh",
          "Làm xe chạy chậm đi",
          "Làm xe nặng hơn",
          "Làm hỏng còi xe"
        ],
        "correct": 0,
        "explanation": "Rãnh gai lốp thoát nước, lốp mòn làm mất ma sát gây trượt lết nguy hiểm."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Hệ thống cân bằng điện tử ESC (Electronic Stability Control) trên ô tô có tác dụng:",
        "options": [
          "Tự động can thiệp phanh từng bánh xe để ngăn xe bị văng đuôi hoặc mất lái khi vào cua ở tốc độ cao",
          "Làm xe bay lên khỏi chướng ngại vật",
          "Làm sáng đèn pha",
          "Đóng cửa sổ tự động"
        ],
        "correct": 0,
        "explanation": "ESC ổn định thân xe, chống lật và trượt văng khi cua gấp ở tốc độ cao."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Trẻ em ngồi trên xe ô tô cần được trang bị thiết bị an toàn nào phù hợp với lứa tuổi?",
        "options": [
          "Ghế an toàn chuyên dụng cho trẻ em gắn chặt với ghế xe và thắt dây an toàn",
          "Để trẻ đứng tự do trên ghế sau",
          "Để trẻ ngồi trong lòng người lái xe",
          "Cho trẻ thò đầu ra cửa sổ trời"
        ],
        "correct": 0,
        "explanation": "Ghế trẻ em chuyên dụng (Child car seat) bảo vệ xương khớp non nớt khi có va chạm."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Vào ban ngày khi đi qua hầm đường bộ, người điều khiển phương tiện bắt buộc phải:",
        "options": [
          "Bật đèn chiếu sáng gần (đèn cốt)",
          "Tắt hết đèn xe",
          "Bật đèn pha chiếu xa",
          "Đi lùi xe"
        ],
        "correct": 0,
        "explanation": "Bắt buộc phải bật đèn chiếu gần khi vào hầm đường bộ."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các yếu tố ảnh hưởng trực tiếp đến thời gian phản xạ của người lái xe:",
        "statements": [
          {
            "subId": "a",
            "text": "Sự mệt mỏi, buồn ngủ làm tăng đáng kể thời gian phản xạ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sử dụng điện thoại di động khi lái xe làm người lái mất tập trung quan sát.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tuổi tác và kinh nghiệm lái xe có ảnh hưởng đến tốc độ phản ứng tình huống.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Uống cà phê đặc giúp người lái xe có thể phản ứng nhanh tức thì trong 0 giây.",
            "correct": false
          }
        ],
        "explanation": "Dù tỉnh táo đến đâu, con người luôn cần thời gian phản xạ tối thiểu khoảng 0,5 - 0,7 s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tình trạng mặt đường ảnh hưởng đến an toàn khi chuyển động ở tốc độ cao:",
        "statements": [
          {
            "subId": "a",
            "text": "Mặt đường khô ráo, bê tông nhám có độ ma sát bám đường tốt nhất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mặt đường dính bùn đất hoặc dầu mỡ làm giảm nghiêm trọng ma sát trượt.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi trời mưa lớn, hiện tượng màng nước nêm lốp (thủy phi cơ) có thể làm xe mất hoàn toàn lái.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Xe chạy ở tốc độ 120 km/h trên đường ướt có quãng đường phanh ngắn hơn đường khô.",
            "correct": false
          }
        ],
        "explanation": "Đường ướt trơn làm quãng đường phanh dài hơn nhiều so với đường khô."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một xe khách 29 chỗ chạy trên quốc lộ với tốc độ 72 km/h (20 m/s):",
        "statements": [
          {
            "subId": "a",
            "text": "Tài xế nhìn thấy biển báo công trường cách 70 m.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian phản xạ của tài xế là 0,8 giây, xe chạy được 16 m trước khi đạp phanh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Xe đạp phanh và dừng lại sau quãng đường phanh 34 m.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Xe dừng lại cách biển báo công trường một khoảng an toàn là 20 m.",
            "correct": true
          }
        ],
        "explanation": "Tổng quãng đường dừng = 16 + 34 = 50 m. Cách biển báo: 70 - 50 = 20 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hệ thống camera phạt nguội giám sát tốc độ phương tiện:",
        "statements": [
          {
            "subId": "a",
            "text": "Được lắp đặt cố định tại các điểm đen tai nạn hoặc giá long môn cao tốc.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ghi lại chính xác hình ảnh phương tiện, tốc độ đo được và thời điểm vi phạm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chỉ xử phạt được các phương tiện vào ban ngày, ban đêm không hoạt động.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Giúp lực lượng chức năng xử lí vi phạm công khai, minh bạch và nâng cao ý thức tài xế.",
            "correct": true
          }
        ],
        "explanation": "Camera hiện đại có đèn hồng ngoại hoạt động rõ nét cả ban đêm."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Khoảng cách an toàn tối thiểu theo luật giao thông khi xe chạy từ trên 80 km/h đến 100 km/h trên đường khô ráo là bao nhiêu mét?",
        "correctAnswer": "70",
        "explanation": "70 m."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một ô tô chạy tốc độ 25 m/s. Thời gian phản xạ của tài xế là 0,8 s. Quãng đường phản xạ là bao nhiêu mét?",
        "correctAnswer": "20",
        "explanation": "s = 25 × 0,8 = 20 m."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Quy tắc 3 giây: Xe chạy với tốc độ 90 km/h (25 m/s). Khoảng cách 3 giây tương ứng là bao nhiêu mét?",
        "correctAnswer": "75",
        "explanation": "25 × 3 = 75 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Xe máy chạy 36 km/h (10 m/s). Quãng đường phản xạ là 7 m, quãng đường hãm phanh là 8 m. Tổng quãng đường dừng xe là bao nhiêu mét?",
        "correctAnswer": "15",
        "explanation": "7 + 8 = 15 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Khoảng cách an toàn tối thiểu quy định cho xe chạy từ 60 km/h trở xuống trên đường cao tốc là bao nhiêu mét?",
        "correctAnswer": "35",
        "explanation": "35 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một ô tô phanh gấp tạo vết trượt dài 15 m ở tốc độ 40 km/h. Nếu ô tô chạy 80 km/h (tăng gấp đôi) thì vết trượt phanh dài bao nhiêu mét?",
        "correctAnswer": "60",
        "explanation": "s tỉ lệ với v^2: 15 × 2^2 = 15 × 4 = 60 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một xe ô tô chạy với tốc độ 80 km/h (xấp xỉ 22,2 m/s). Phía trước có vật cản cách 50 m. Thời gian phản xạ của lái xe là 0,7 giây và quãng đường hãm phanh là 28 m. Ô tô có dừng lại kịp trước vật cản không và còn cách vật cản bao nhiêu mét?",
        "options": [
          "Có dừng lại kịp, còn cách vật cản xấp xỉ 6,46 m",
          "Không kịp, đâm vào vật cản",
          "Dừng lại chạm đúng vật cản",
          "Còn cách 15 m"
        ],
        "correct": 0,
        "explanation": "s_phản_xạ = 22,2 × 0,7 ≈ 15,54 m. Tổng quãng đường dừng: 15,54 + 28 = 43,54 m < 50 m => Cách vật cản: 50 - 43,54 = 6,46 m."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Theo quy định tại Thông tư 31/2019/TT-BGTVT, tốc độ tối đa cho phép của xe cơ giới (trừ xe máy chuyên dùng, xe gắn máy) trên đường bộ trong khu vực đông dân cư có đường đôi hoặc đường một chiều có từ hai làn xe cơ giới trở lên là:",
        "options": [
          "60 km/h",
          "50 km/h",
          "70 km/h",
          "80 km/h"
        ],
        "correct": 0,
        "explanation": "Đường đôi/đường 1 chiều từ 2 làn trở lên trong khu đông dân cư tối đa là 60 km/h."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tại sao khi chạy xe trên đường đèo dốc quanh co có nhiều khúc cua gấp, lái xe tuyệt đối không được rà phanh liên tục trong thời gian dài mà phải về số thấp (hãm bằng động cơ)?",
        "options": [
          "Vì rà phanh liên tục làm má phanh bị ma sát quá nhiệt dẫn đến cháy phanh, sôi dầu phanh và mất hoàn toàn tác dụng phanh",
          "Để xe chạy nhanh hơn",
          "Để đỡ tốn xăng",
          "Để động cơ không bị ồn"
        ],
        "correct": 0,
        "explanation": "Rà phanh liên tục khi đổ đèo làm má phanh quá nhiệt, gây trơ lì má phanh và mất phanh nguy hiểm."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một tài xế lái xe với tốc độ 100 km/h trên cao tốc vào một ngày trời mưa tầm tã. Biết khoảng cách an toàn tối thiểu theo luật trên đường khô ráo là 70 m, và quy chuẩn an toàn khuyến cáo phải tăng khoảng cách thêm ít nhất 50% khi đường trơn trượt. Khoảng cách an toàn tài xế cần giữ lúc này là:",
        "options": [
          "105 m",
          "70 m",
          "85 m",
          "140 m"
        ],
        "correct": 0,
        "explanation": "70 × 1,5 = 105 m."
      }
    ]
  },
  "phys7_c3_b11_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_b11",
    "lessonName": "Bài 11: Thảo luận về ảnh hưởng của tốc độ trong an toàn giao thông",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Biển báo cự li an toàn tối thiểu giữa hai xe (biển P.121) có hình vẽ hai chiếc ô tô nối đuôi nhau và ghi số '50m' ở giữa nghĩa là:",
        "options": [
          "Các xe phải giữ khoảng cách an toàn không nhỏ hơn 50 mét",
          "Các xe phải chạy cách nhau đúng 50 cm",
          "Đoạn đường dài 50 mét",
          "Tốc độ tối đa là 50 km/h"
        ],
        "correct": 0,
        "explanation": "Biển P.121 quy định cự li tối thiểu giữa hai xe."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khi điều khiển xe ô tô lưu thông trên đường cao tốc, hành vi nào sau đây bị nghiêm cấm tuyệt đối?",
        "options": [
          "Cho xe chạy lùi hoặc quay đầu xe trên đường cao tốc",
          "Bật đèn pha chiếu sáng",
          "Giữ khoảng cách an toàn với xe trước",
          "Chạy xe đúng làn đường quy định"
        ],
        "correct": 0,
        "explanation": "Nghiêm cấm lùi xe, quay đầu xe trên cao tốc vì nguy cơ tai nạn đặc biệt thảm khốc."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Lực cản không khí tác dụng lên xe ô tô khi chuyển động tỉ lệ thuận với bình phương tốc độ. Điều này có nghĩa là:",
        "options": [
          "Khi xe chạy càng nhanh, lực cản không khí càng tăng mạnh làm tiêu tốn nhiều nhiên liệu hơn",
          "Xe chạy nhanh thì lực cản giảm",
          "Không khí không cản trở xe",
          "Xe chạy càng chậm thì càng tốn xăng"
        ],
        "correct": 0,
        "explanation": "Lực cản khí động học tăng theo v^2 nên chạy quá nhanh rất tốn nhiên liệu."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Thiết bị giám sát hành trình (hộp đen) lắp đặt bắt buộc trên các xe ô tô kinh doanh vận tải dùng để:",
        "options": [
          "Ghi nhận hành trình, tốc độ di chuyển và thời gian lái xe liên tục của tài xế",
          "Đo nhiệt độ buồng lái",
          "Làm mát động cơ",
          "Bật nhạc giải trí"
        ],
        "correct": 0,
        "explanation": "Hộp đen giám sát tốc độ và thời gian làm việc của tài xế để đảm bảo an toàn."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Để cảnh báo nguy hiểm khi xe bị hỏng phải đỗ lại trên làn khẩn cấp của đường cao tốc, người lái xe cần:",
        "options": [
          "Bật đèn cảnh báo nguy hiểm (hazard) và đặt tam giác phản quang cách đuôi xe ít nhất 100 - 150 m",
          "Ngồi trong xe ngủ",
          "Tắt hết đèn xe",
          "Đứng giữa làn đường vẫy tay"
        ],
        "correct": 0,
        "explanation": "Đặt biển cảnh báo tam giác phản quang từ xa để các xe sau kịp giảm tốc tránh."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Theo luật Giao thông đường bộ, thời gian lái xe liên tục tối đa của một tài xế ô tô kinh doanh vận tải không được vượt quá:",
        "options": [
          "4 giờ liên tục",
          "8 giờ liên tục",
          "10 giờ liên tục",
          "12 giờ liên tục"
        ],
        "correct": 0,
        "explanation": "Quy định tài xế không được lái xe quá 4 giờ liên tục để tránh mệt mỏi gây tai nạn."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một xe con chạy trên cao tốc với tốc độ 120 km/h (xấp xỉ 33,3 m/s). Chỉ trong 1 giây lơ đãng, xe đã di chuyển được quãng đường hơn:",
        "options": [
          "33 mét",
          "12 mét",
          "20 mét",
          "10 mét"
        ],
        "correct": 0,
        "explanation": "Trong 1 s xe đi được 33,3 m, bằng chiều dài của hơn 7 chiếc ô tô con nối đuôi nhau."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Theo quy định, khoảng cách an toàn tối thiểu giữa hai xe khi lưu thông trên đường cao tốc với tốc độ trên 100 km/h đến 120 km/h là:",
        "options": [
          "100 m",
          "70 m",
          "55 m",
          "35 m"
        ],
        "correct": 0,
        "explanation": "Quy định cự li tối thiểu là 100 m đối với dải tốc độ 100 - 120 km/h."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tại sao người ngồi ghế trước trên ô tô không cài dây an toàn thì khi xe đâm va trực diện sẽ bị hất văng về phía trước đập đầu vào kính chắn gió?",
        "options": [
          "Do quán tính, cơ thể người có xu hướng tiếp tục duy trì trạng thái chuyển động về phía trước",
          "Do kính chắn gió hút người",
          "Do động cơ xe đẩy người",
          "Do trọng lực kéo về phía trước"
        ],
        "correct": 0,
        "explanation": "Theo định luật quán tính, khi xe dừng đột ngột, người tiếp tục lao về phía trước."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Biển báo 'Đoạn đường hay xảy ra tai nạn' kết hợp với biển giới hạn tốc độ 40 km/h đặt ở đoạn đường đèo dốc quanh co nhằm:",
        "options": [
          "Nhắc nhở lái xe tập trung cao độ và giảm tốc độ thấp để dễ dàng kiểm soát tay lái khi vào cua",
          "Cấm xe máy đi qua",
          "Cho phép xe vượt nhau",
          "Để xe dừng lại chụp ảnh"
        ],
        "correct": 0,
        "explanation": "Hạn chế tốc độ để triệt tiêu lực quán tính ly tâm khi vào cua nguy hiểm."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Gương chiếu hậu trên xe máy và ô tô giúp người lái xe:",
        "options": [
          "Quan sát được tình hình giao thông và phương tiện phía sau cũng như hai bên hông xe",
          "Soi gương làm đẹp",
          "Che gió cho tay lái",
          "Bắt tín hiệu sóng radio"
        ],
        "correct": 0,
        "explanation": "Gương chiếu hậu bao quát điểm mù và phương tiện phía sau."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hành động nào sau đây thể hiện văn hóa giao thông và đảm bảo an toàn tốc độ?",
        "options": [
          "Chủ động giảm tốc độ khi đi qua khu dân cư, trường học và nhường đường cho người đi bộ",
          "Bóp còi inh ỏi để phóng nhanh qua đám đông",
          "Lạng lách đánh võng vượt đèn vàng",
          "Đua xe trái phép trên quốc lộ"
        ],
        "correct": 0,
        "explanation": "Giảm tốc độ, chú ý quan sát và nhường đường thể hiện văn hóa giao thông chuẩn mực."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các quy tắc an toàn khi điều khiển xe trên đường cao tốc:",
        "statements": [
          {
            "subId": "a",
            "text": "Phương tiện chạy chậm hơn phải đi về làn đường bên phải theo chiều đi của mình.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chỉ được chuyển làn ở những đoạn đường có vạch kẻ đường đứt nét.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Được phép dừng đỗ xe tùy tiện trên bất kì làn đường nào để ngắm cảnh.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Làn dừng xe khẩn cấp chỉ dùng cho các xe gặp sự cố hoặc xe ưu tiên khi làm nhiệm vụ.",
            "correct": true
          }
        ],
        "explanation": "Tuyệt đối không được dừng đỗ tùy tiện trên cao tốc."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tác dụng của hệ thống chiếu sáng xe vào ban đêm đối với an toàn tốc độ:",
        "statements": [
          {
            "subId": "a",
            "text": "Đèn pha chiếu xa giúp tài xế quan sát đường ở cự li xa khi đường vắng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi đi sau xe khác ở cự li gần, phải chuyển sang đèn cốt để không làm chói mắt tài xế xe trước qua gương chiếu hậu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đèn sương mù màu vàng giúp tăng khả năng nhận diện đường khi thời tiết nhiều sương mù.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bật đèn xi nhan khẩn cấp liên tục khi đang chạy bình thường ở tốc độ cao để xin đường là đúng luật.",
            "correct": false
          }
        ],
        "explanation": "Đèn khẩn cấp (hazard) chỉ dùng khi xe gặp sự cố nguy hiểm dừng đỗ, không dùng để xin vượt tùy tiện."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một xe container di chuyển với tốc độ 60 km/h (xấp xỉ 16,7 m/s):",
        "statements": [
          {
            "subId": "a",
            "text": "Khối lượng của xe container rất lớn nên quán tính của xe rất lớn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian phản xạ của tài xế là 1,0 s, xe đi được khoảng 16,7 m.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Do tải trọng nặng, quãng đường hãm phanh của xe container dài hơn nhiều so với xe con.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Xe container có thể dừng lại ngay tức khắc trong cự li 1 m khi phanh gấp.",
            "correct": false
          }
        ],
        "explanation": "Xe tải nặng có quán tính cực lớn, quãng đường phanh cần thiết rất dài, không thể dừng ngay trong 1 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Quy định về nồng độ cồn đối với người điều khiển phương tiện giao thông ở Việt Nam (Nghị định 100/2019/NĐ-CP):",
        "statements": [
          {
            "subId": "a",
            "text": "Nghiêm cấm tuyệt đối người điều khiển xe trên đường mà trong máu hoặc hơi thở có nồng độ cồn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Người có nồng độ cồn vượt mức quy định sẽ bị xử phạt tiền và tước quyền sử dụng giấy phép lái xe.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Uống một lon bia thì vẫn được phép lái xe máy nếu cảm thấy bản thân còn tỉnh táo.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Đã uống rượu bia thì không lái xe là khẩu hiệu an toàn mang tính sống còn.",
            "correct": true
          }
        ],
        "explanation": "Luật quy định nồng độ cồn bằng 0 khi lái xe, không có mức miễn trừ tự cảm nhận."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Khoảng cách an toàn tối thiểu theo quy định khi xe chạy với tốc độ từ trên 100 km/h đến 120 km/h trên cao tốc là bao nhiêu mét?",
        "correctAnswer": "100",
        "explanation": "100 m."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một ô tô chạy tốc độ 30 m/s. Thời gian phản xạ là 0,6 s. Quãng đường xe chạy trong thời gian phản xạ là bao nhiêu mét?",
        "correctAnswer": "18",
        "explanation": "s = 30 × 0,6 = 18 m."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Theo quy tắc 3 giây: Xe chạy với tốc độ 108 km/h (30 m/s). Khoảng cách an toàn 3 giây là bao nhiêu mét?",
        "correctAnswer": "90",
        "explanation": "30 × 3 = 90 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Xe chạy với tốc độ 72 km/h (20 m/s). Quãng đường phản xạ là 16 m, quãng đường hãm phanh là 24 m. Tổng quãng đường dừng xe là bao nhiêu mét?",
        "correctAnswer": "40",
        "explanation": "16 + 24 = 40 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một tài xế lái xe liên tục suốt 3,5 giờ. Theo luật giao thông đường bộ, tài xế chỉ được phép lái thêm tối đa bao nhiêu phút nữa trước khi bắt buộc phải dừng nghỉ?",
        "correctAnswer": "30",
        "explanation": "Luật quy định tối đa 4 giờ liên tục => 4 h - 3,5 h = 0,5 h = 30 phút."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một xe tải chở nặng phanh gấp ở tốc độ 50 km/h tạo vết trượt phanh 25 m. Nếu xe chạy 100 km/h (tăng gấp đôi) thì vết trượt phanh dài bao nhiêu mét?",
        "correctAnswer": "100",
        "explanation": "25 × 2^2 = 25 × 4 = 100 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một xe khách đang chạy với tốc độ 72 km/h (20 m/s) trên đường quốc lộ thì gặp chướng ngại vật ở cách xe 45 m. Biết thời gian phản xạ của tài xế là 0,7 giây và quãng đường hãm phanh là 28 m. Xe khách có dừng lại an toàn trước chướng ngại vật không và dừng cách chướng ngại vật bao nhiêu mét?",
        "options": [
          "Có dừng lại an toàn, cách chướng ngại vật 3 m",
          "Không an toàn, va chạm vào chướng ngại vật",
          "Dừng cách chướng ngại vật 10 m",
          "Dừng cách chướng ngại vật 15 m"
        ],
        "correct": 0,
        "explanation": "Quãng đường phản xạ: 20 × 0,7 = 14 m. Tổng quãng đường dừng: 14 + 28 = 42 m < 45 m => Dừng cách chướng ngại vật: 45 - 42 = 3 m."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Theo quy định tại Thông tư số 31/2019/TT-BGTVT, khi tham gia giao thông trên đường bộ ngoài khu vực đông dân cư (trừ đường cao tốc), tốc độ tối đa cho phép đối với xe ô tô con trên đường đôi (có dải phân cách giữa) là:",
        "options": [
          "90 km/h",
          "80 km/h",
          "70 km/h",
          "100 km/h"
        ],
        "correct": 0,
        "explanation": "Ngoài khu đông dân cư, đường đôi có dải phân cách giữa: xe ô tô con được chạy tối đa 90 km/h."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để vượt xe khác một cách an toàn trên đường hai chiều không có dải phân cách giữa, người lái xe phải tuân thủ điều kiện nào sau đây?",
        "options": [
          "Chỉ được vượt khi không có chướng ngại vật phía trước, không có xe chạy ngược chiều trong đoạn đường định vượt và xe chạy trước đã có tín hiệu nhường đường",
          "Vượt ngay tại khúc cua khuất tầm nhìn",
          "Vượt khi xe phía trước đang vượt xe khác",
          "Bấm còi và ép xe ngược chiều xuống lề đường"
        ],
        "correct": 0,
        "explanation": "Chỉ được vượt khi đủ tầm nhìn, không có xe đối diện và xe trước nhường đường."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người điều khiển xe máy đi với tốc độ 40 km/h trên đường trơn ướt. Để đảm bảo an toàn, khoảng cách với xe phía trước cần tối thiểu 30 m. Nếu người này chạy với tốc độ 60 km/h trong cùng điều kiện thì khoảng cách an toàn tối thiểu theo tỉ lệ bình phương tốc độ phải tăng lên xấp xỉ bao nhiêu mét?",
        "options": [
          "67,5 m",
          "45,0 m",
          "60,0 m",
          "50,0 m"
        ],
        "correct": 0,
        "explanation": "Khoảng cách tỉ lệ với v^2: 30 × (60/40)^2 = 30 × 1,5^2 = 30 × 2,25 = 67,5 m."
      }
    ]
  },
  "phys7_c3_rev_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương III - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương III",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đại lượng nào sau đây cho biết mức độ chuyển động nhanh hay chậm của một vật?",
        "options": [
          "Tốc độ chuyển động",
          "Khối lượng của vật",
          "Thể tích của vật",
          "Nhiệt độ của vật"
        ],
        "correct": 0,
        "explanation": "Tốc độ cho biết mức độ nhanh hay chậm của chuyển động."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong hệ đo lường chuẩn quốc tế SI, đơn vị của tốc độ là:",
        "options": [
          "Mét trên giây (m/s)",
          "Kilômét trên giờ (km/h)",
          "Dặm trên giờ (mph)",
          "Hải lí trên giờ (knot)"
        ],
        "correct": 0,
        "explanation": "Đơn vị chuẩn SI là m/s."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hệ thống thiết bị đo thời gian hiện đại trong phòng thực hành gồm:",
        "options": [
          "Cổng quang điện và đồng hồ đo thời gian hiện số",
          "Thước dây và cân đòn",
          "Bình tràn và lực kế",
          "Nhiệt kế thủy ngân"
        ],
        "correct": 0,
        "explanation": "Cổng quang điện kết hợp đồng hồ hiện số."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trên đồ thị quãng đường - thời gian (s - t), đoạn đồ thị nằm ngang song song trục Ot thể hiện:",
        "options": [
          "Vật đang đứng yên",
          "Vật chuyển động thẳng đều",
          "Vật tăng tốc đột ngột",
          "Vật quay lại điểm xuất phát"
        ],
        "correct": 0,
        "explanation": "Đoạn nằm ngang biểu thị quãng đường không đổi, vật đứng yên."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Biển báo hiệu giao thông hình tròn, viền đỏ, nền trắng bên trong có số 50 màu đen là biển:",
        "options": [
          "Hạn chế tốc độ tối đa 50 km/h",
          "Tốc độ tối thiểu 50 km/h",
          "Khoảng cách xe 50 m",
          "Cấm xe trọng tải 50 tấn"
        ],
        "correct": 0,
        "explanation": "Biển hạn chế tốc độ tối đa cho phép."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Quy tắc 'Khoảng cách 3 giây' áp dụng trên đường nhằm mục đích:",
        "options": [
          "Đảm bảo khoảng cách an toàn giúp lái xe kịp phản xạ và phanh dừng khi xe trước gặp sự cố",
          "Tăng tốc vượt xe khác",
          "Tiết kiệm xăng",
          "Chạy xe đúng làn đường"
        ],
        "correct": 0,
        "explanation": "Quy tắc 3 giây tạo cự li an toàn để phản ứng và phanh xe."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một bạn học sinh đi xe đạp từ nhà đến trường dài 3,6 km mất thời gian 15 phút. Tốc độ của bạn là:",
        "options": [
          "14,4 km/h",
          "10,0 km/h",
          "12,0 km/h",
          "15,0 km/h"
        ],
        "correct": 0,
        "explanation": "15 phút = 0,25 h. v = 3,6 / 0,25 = 14,4 km/h."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Đổi giá trị tốc độ 25 m/s sang đơn vị km/h ta được:",
        "options": [
          "90 km/h",
          "60 km/h",
          "72 km/h",
          "100 km/h"
        ],
        "correct": 0,
        "explanation": "25 × 3,6 = 90 km/h."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một tấm chắn sáng có bề rộng 0,02 m đi qua cổng quang điện trong thời gian 0,04 s. Tốc độ tức thời của xe là:",
        "options": [
          "0,5 m/s",
          "0,2 m/s",
          "1,0 m/s",
          "0,8 m/s"
        ],
        "correct": 0,
        "explanation": "v = 0,02 / 0,04 = 0,5 m/s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t của một ô tô là đường thẳng đi qua gốc tọa độ O và điểm A(2 h; 110 km). Tốc độ của ô tô là:",
        "options": [
          "55 km/h",
          "60 km/h",
          "50 km/h",
          "110 km/h"
        ],
        "correct": 0,
        "explanation": "v = 110 / 2 = 55 km/h."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi một chiếc ô tô tăng tốc độ từ 40 km/h lên 80 km/h (gấp đôi) thì động năng và mức độ va chạm sẽ tăng lên:",
        "options": [
          "4 lần",
          "2 lần",
          "8 lần",
          "16 lần"
        ],
        "correct": 0,
        "explanation": "Động năng Wđ tỉ lệ với v^2: tăng 2 lần tốc độ làm động năng tăng 2^2 = 4 lần."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Theo quy định, trên đoạn đường cao tốc khô ráo khi xe lưu thông với tốc độ từ 60 km/h đến 80 km/h thì khoảng cách an toàn tối thiểu là:",
        "options": [
          "55 m",
          "35 m",
          "70 m",
          "100 m"
        ],
        "correct": 0,
        "explanation": "Khoảng cách an toàn tối thiểu tương ứng là 55 m."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các khái niệm cơ bản của tốc độ chuyển động trong Chương III:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc độ trung bình bằng tổng quãng đường chia cho tổng thời gian đi hết quãng đường đó.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "1 m/s tương đương với 3,6 km/h.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc kế trên xe chỉ tốc độ trung bình của xe từ đầu bến đến cuối bến.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Chuyển động đều có tốc độ tức thời tại mọi thời điểm bằng nhau.",
            "correct": true
          }
        ],
        "explanation": "Tốc kế chỉ tốc độ tức thời tại thời điểm đang chạy."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về phép đo tốc độ trong thực hành và kiểm tra giao thông:",
        "statements": [
          {
            "subId": "a",
            "text": "Phép đo tốc độ bằng thước và đồng hồ bấm giây luôn có sai số do phản xạ tay người.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cổng quang điện giúp đo thời gian với độ chính xác cao đến phần nghìn giây.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Súng bắn tốc độ sử dụng sóng radar hoặc sóng laser để đo tốc độ phương tiện giao thông.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Để kết quả đo chính xác nhất thì chỉ cần thực hiện đo đúng 1 lần duy nhất.",
            "correct": false
          }
        ],
        "explanation": "Cần đo lặp lại nhiều lần để lấy giá trị trung bình giảm sai số ngẫu nhiên."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Phân tích đồ thị chuyển động s - t của một người đi bộ từ nhà qua chợ rồi đến công viên:",
        "statements": [
          {
            "subId": "a",
            "text": "Chặng 1 từ nhà đến chợ dài 1,5 km người đó đi trong 20 phút (1/3 giờ) với tốc độ 4,5 km/h.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tại chợ người đó dừng mua sắm trong 10 phút, đồ thị là đoạn nằm ngang.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chặng 2 từ chợ đến công viên dài 2,0 km đi trong 30 phút với tốc độ 4,0 km/h.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình trên toàn tuyến tính cả thời gian mua sắm tại chợ là 4,25 km/h.",
            "correct": false
          }
        ],
        "explanation": "Tổng s = 1,5 + 2 = 3,5 km. Tổng t = 20 + 10 + 30 = 60 phút = 1 h => v_tb = 3,5 / 1 = 3,5 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Xét trường hợp một xe tải chở hàng lưu thông trên đường:",
        "statements": [
          {
            "subId": "a",
            "text": "Tài xế lái xe chạy với tốc độ 60 km/h (xấp xỉ 16,7 m/s).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian phản xạ của tài xế là 0,9 giây, quãng đường xe đi trước khi phanh là 15 m.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Quãng đường hãm phanh của xe tải dài hơn so với xe con chạy cùng tốc độ do tải trọng lớn hơn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khi trời mưa đường trơn trượt, tài xế có thể rút ngắn khoảng cách với xe trước để dễ bám theo.",
            "correct": false
          }
        ],
        "explanation": "Trời mưa đường trơn bắt buộc phải tăng khoảng cách an toàn."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đổi tốc độ 18 km/h sang m/s ta được kết quả là bao nhiêu?",
        "correctAnswer": "5",
        "explanation": "18 / 3,6 = 5 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một người bơi 100 m hết 50 giây. Tốc độ bơi trung bình là bao nhiêu m/s?",
        "correctAnswer": "2",
        "explanation": "v = 100 / 50 = 2 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một xe khách chạy trên cao tốc với tốc độ 80 km/h trong thời gian 2,25 giờ. Quãng đường đi được là bao nhiêu km?",
        "correctAnswer": "180",
        "explanation": "s = 80 × 2,25 = 180 km."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khoảng cách an toàn tối thiểu theo luật khi xe chạy với tốc độ từ trên 80 km/h đến 100 km/h trên đường khô ráo là bao nhiêu mét?",
        "correctAnswer": "70",
        "explanation": "70 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Xe máy chạy nửa quãng đường đầu với tốc độ 30 km/h và nửa quãng đường sau với tốc độ 60 km/h. Tốc độ trung bình trên cả quãng đường là bao nhiêu km/h?",
        "correctAnswer": "40",
        "explanation": "v_tb = 2 × 30 × 60 / (30 + 60) = 3600 / 90 = 40 km/h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một máy bay siêu thanh bay với tốc độ Mach 2 (gấp đôi tốc độ âm thanh trong không khí 340 m/s). Tốc độ của máy bay tính theo đơn vị m/s là bao nhiêu?",
        "correctAnswer": "680",
        "explanation": "340 × 2 = 680 m/s."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hai ô tô cùng xuất phát từ bến A lúc 6h30 sáng đi về bến B cách A một khoảng 150 km. Xe thứ nhất chạy đều với tốc độ 50 km/h. Xe thứ hai chạy đều với tốc độ 60 km/h. Xe thứ hai đến bến B trước xe thứ nhất một khoảng thời gian là bao nhiêu phút?",
        "options": [
          "30 phút",
          "20 phút",
          "15 phút",
          "45 phút"
        ],
        "correct": 0,
        "explanation": "t1 = 150 / 50 = 3,0 h = 180 phút. t2 = 150 / 60 = 2,5 h = 150 phút. Trước: 180 - 150 = 30 phút."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu hỏa dài 180 m chạy qua một chiếc hầm đường sắt dài 540 m với tốc độ không đổi 54 km/h (15 m/s). Khoảng thời gian từ lúc đầu tàu bắt đầu chui vào hầm đến khi toa cuối cùng ra khỏi hầm hoàn toàn là:",
        "options": [
          "48 giây",
          "36 giây",
          "40 giây",
          "50 giây"
        ],
        "correct": 0,
        "explanation": "s = 540 + 180 = 720 m. t = 720 / 15 = 48 s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một ô tô chạy trên cao tốc với tốc độ 100 km/h (xấp xỉ 27,8 m/s). Bất ngờ phía trước có xe dừng sự cố. Thời gian phản xạ của tài xế là 0,8 s và quãng đường hãm phanh đến khi dừng hẳn là 45 m. Để dừng lại cách xe sự cố ít nhất 10 m thì khoảng cách tối thiểu từ lúc nhìn thấy xe sự cố phải là:",
        "options": [
          "77,24 m",
          "67,24 m",
          "55,00 m",
          "80,00 m"
        ],
        "correct": 0,
        "explanation": "s_dừng = (27,8 × 0,8) + 45 = 22,24 + 45 = 67,24 m. Cách 10 m => Khoảng cách = 67,24 + 10 = 77,24 m."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một ca nô chạy xuôi dòng trên khúc sông từ A đến B hết 2 giờ và chạy ngược dòng từ B về A hết 3 giờ. Khúc sông AB dài 60 km. Vận tốc của dòng nước so với bờ sông là bao nhiêu km/h?",
        "options": [
          "5 km/h",
          "10 km/h",
          "2,5 km/h",
          "25 km/h"
        ],
        "correct": 0,
        "explanation": "v_xuôi = 60 / 2 = 30 km/h; v_ngược = 60 / 3 = 20 km/h => v_nước = (30 - 20) / 2 = 5 km/h."
      }
    ]
  },
  "phys7_c3_rev_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương III - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương III",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Muốn biết vật nào chuyển động nhanh hơn khi chúng chuyển động trong cùng một khoảng thời gian, ta so sánh:",
        "options": [
          "Quãng đường đi được của các vật",
          "Khối lượng của các vật",
          "Hướng chuyển động của các vật",
          "Màu sắc của các vật"
        ],
        "correct": 0,
        "explanation": "Trong cùng thời gian, vật nào đi quãng đường dài hơn thì chuyển động nhanh hơn."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Công thức nào sau đây xác định quãng đường s khi biết tốc độ v và thời gian t?",
        "options": [
          "s = v × t",
          "s = v / t",
          "s = t / v",
          "s = v + t"
        ],
        "correct": 0,
        "explanation": "s = v × t."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi dùng cổng quang điện để đo thời gian, bộ phận nào của xe đóng vai trò ngắt chùm tia sáng?",
        "options": [
          "Tấm chắn sáng gắn trên xe",
          "Bánh xe",
          "Động cơ xe",
          "Dây kéo xe"
        ],
        "correct": 0,
        "explanation": "Tấm chắn sáng che chùm tia quang điện khi đi qua cổng quang."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong đồ thị s - t, nếu đường đồ thị dốc thẳng đứng (vuông góc với trục Ot) thì điều đó:",
        "options": [
          "Không thể xảy ra trong thực tế vì vật không thể đi được quãng đường mà không tốn thời gian",
          "Vật chạy với tốc độ âm",
          "Vật đứng yên",
          "Vật đang rơi"
        ],
        "correct": 0,
        "explanation": "Thời gian luôn trôi về phía trước, không thể đi quãng đường trong thời gian t = 0 (tốc độ vô hạn)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Biển báo hiệu R.306 hình tròn nền xanh có số 60 màu trắng là biển:",
        "options": [
          "Tốc độ tối thiểu cho phép 60 km/h",
          "Tốc độ tối đa 60 km/h",
          "Khoảng cách 60 m",
          "Biển báo nguy hiểm"
        ],
        "correct": 0,
        "explanation": "Biển R.306 quy định tốc độ tối thiểu cho phép."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Thiết bị an toàn nào trên ô tô được thiết kế để bung ra như một chiếc đệm khí bảo vệ đầu và ngực khi va chạm mạnh?",
        "options": [
          "Túi khí (Airbag)",
          "Dây an toàn",
          "Phanh tay",
          "Còi xe"
        ],
        "correct": 0,
        "explanation": "Túi khí tự động bung ra trong mili-giây để bảo vệ hành khách."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một ô tô chạy trên đoạn đường 105 km hết 1 giờ 45 phút (1,75 giờ). Tốc độ của ô tô là:",
        "options": [
          "60 km/h",
          "55 km/h",
          "70 km/h",
          "65 km/h"
        ],
        "correct": 0,
        "explanation": "v = 105 / 1,75 = 60 km/h."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Đổi 20 m/s sang đơn vị km/h ta được kết quả là:",
        "options": [
          "72 km/h",
          "36 km/h",
          "54 km/h",
          "90 km/h"
        ],
        "correct": 0,
        "explanation": "20 × 3,6 = 72 km/h."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tấm chắn sáng rộng 4 cm (0,04 m) đi qua cổng quang điện trong thời gian 0,08 s. Tốc độ tức thời là:",
        "options": [
          "0,5 m/s",
          "0,4 m/s",
          "2,0 m/s",
          "1,0 m/s"
        ],
        "correct": 0,
        "explanation": "v = 0,04 / 0,08 = 0,5 m/s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t của một người đạp xe: trong 30 phút đầu đi được 6 km, trong 30 phút sau đi được 9 km. Tốc độ trung bình trên cả 1 giờ là:",
        "options": [
          "15 km/h",
          "12 km/h",
          "18 km/h",
          "10 km/h"
        ],
        "correct": 0,
        "explanation": "Tổng s = 6 + 9 = 15 km, tổng t = 1 h => v_tb = 15 / 1 = 15 km/h."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Theo quy định, khoảng cách an toàn tối thiểu giữa hai xe chạy trên đường cao tốc khô ráo ở tốc độ từ trên 100 km/h đến 120 km/h là:",
        "options": [
          "100 m",
          "70 m",
          "55 m",
          "35 m"
        ],
        "correct": 0,
        "explanation": "Khoảng cách an toàn quy định là 100 m."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Khi lái xe gặp trời mưa to, mặt đường ngập nước, người điều khiển xe nên làm gì để đảm bảo an toàn?",
        "options": [
          "Giảm tốc độ và tăng khoảng cách an toàn so với xe chạy phía trước",
          "Bật đèn pha chiếu xa và tăng tốc",
          "Đi bám sát đuôi xe trước",
          "Chạy vào làn khẩn cấp ở tốc độ tối đa"
        ],
        "correct": 0,
        "explanation": "Giảm tốc độ và nới rộng cự li an toàn do đường trơn trượt."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các đơn vị và công thức đo tốc độ trong bài học:",
        "statements": [
          {
            "subId": "a",
            "text": "Biểu thức tính thời gian là t = s / v.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đơn vị hải lí trên giờ (nút) thường dùng cho tàu thuyền trên biển.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Để đổi km/h sang m/s ta lấy giá trị nhân với 3,6.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình phản ánh mức độ nhanh chậm của cả một quãng đường chuyển động.",
            "correct": true
          }
        ],
        "explanation": "Đổi km/h sang m/s phải chia cho 3,6."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các thiết bị đo tốc độ trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc kế trên xe máy hoạt động nhờ cảm biến đo vòng quay của bánh xe.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thiết bị bắn tốc độ chỉ có thể đo được xe chạy ban ngày, không đo được ban đêm.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Camera phạt nguội ghi lại hình ảnh biển số xe và tốc độ tại thời điểm vi phạm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đồng hồ đo thời gian hiện số giúp đo được khoảng thời gian rất ngắn tới 0,001 giây.",
            "correct": true
          }
        ],
        "explanation": "Thiết bị bắn tốc độ hồng ngoại đo chính xác cả ban đêm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hành trình của một gia đình đi du lịch bằng ô tô từ thành phố về quê:",
        "statements": [
          {
            "subId": "a",
            "text": "Chặng 1 xe chạy trên cao tốc dài 80 km với tốc độ 80 km/h hết 1 giờ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Gia đình dừng nghỉ uống nước tại trạm dừng nghỉ trong 20 phút (1/3 giờ).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chặng 2 xe chạy trên quốc lộ dài 40 km với tốc độ 60 km/h hết 40 phút (2/3 giờ).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình trên toàn tuyến đường 120 km tính cả thời gian nghỉ là 60 km/h.",
            "correct": true
          }
        ],
        "explanation": "Tổng s = 80 + 40 = 120 km, tổng t = 1 + 1/3 + 2/3 = 2 h => v_tb = 120 / 2 = 60 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một xe con chạy trên cao tốc với tốc độ 108 km/h (30 m/s):",
        "statements": [
          {
            "subId": "a",
            "text": "Thời gian phản xạ của tài xế là 0,7 giây, xe đi được 21 m trong lúc phản xạ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Quãng đường hãm phanh của xe đến khi dừng hẳn là 39 m.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tổng quãng đường dừng xe an toàn là 60 m.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khoảng cách an toàn theo quy tắc 3 giây ở tốc độ này là 60 m.",
            "correct": false
          }
        ],
        "explanation": "Khoảng cách theo quy tắc 3 giây là 30 × 3 = 90 m, không phải 60 m."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đổi tốc độ 10 m/s sang đơn vị km/h ta được kết quả là bao nhiêu?",
        "correctAnswer": "36",
        "explanation": "10 × 3,6 = 36 km/h."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một ô tô chạy quãng đường 150 km trong 3 giờ. Tốc độ của ô tô là bao nhiêu km/h?",
        "correctAnswer": "50",
        "explanation": "v = 150 / 3 = 50 km/h."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Đoạn đường có biển báo tốc độ tối đa 60 km/h. Một xe máy chạy với tốc độ 18 m/s có bị vi phạm quá tốc độ không? (Trả lời: Có hoặc Không)",
        "correctAnswer": "Có",
        "explanation": "18 m/s = 64,8 km/h > 60 km/h => Có vi phạm."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Theo quy định, khoảng cách an toàn tối thiểu khi chạy xe trên đường khô ráo với tốc độ từ 60 km/h trở xuống là bao nhiêu mét?",
        "correctAnswer": "35",
        "explanation": "35 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người đi xe đạp đi nửa thời gian đầu với tốc độ 12 km/h và nửa thời gian sau với tốc độ 16 km/h. Tốc độ trung bình của người đó là bao nhiêu km/h?",
        "correctAnswer": "14",
        "explanation": "Khi nửa thời gian: v_tb = (12 + 16)/2 = 14 km/h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Khoảng cách từ Trái Đất đến Mặt Trăng là khoảng 384.000 km. Tín hiệu sóng vô tuyến truyền với tốc độ ánh sáng 300.000 km/s từ Trái Đất đến Mặt Trăng mất khoảng bao nhiêu giây? (Làm tròn 1 chữ số thập phân)",
        "correctAnswer": "1.3",
        "explanation": "t = 384.000 / 300.000 = 1,28 s ≈ 1,3 s."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hai thành phố A và B cách nhau 180 km. Lúc 7h00 sáng, xe ô tô thứ nhất xuất phát từ A đến B với tốc độ 60 km/h, xe ô tô thứ hai xuất phát từ B đến A với tốc độ 40 km/h. Hai xe gặp nhau lúc mấy giờ?",
        "options": [
          "8h48 sáng",
          "9h00 sáng",
          "8h30 sáng",
          "9h15 sáng"
        ],
        "correct": 0,
        "explanation": "Thời gian gặp nhau: t = 180 / (60 + 40) = 1,8 h = 1h 48 phút. Thời điểm: 7h00 + 1h48 = 8h48 sáng."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu hỏa dài 200 m đang chạy với tốc độ đều 72 km/h (20 m/s) chạy song song và vượt qua một người đi bộ ngược chiều với tốc độ 4 km/h (1,11 m/s). Khoảng thời gian từ lúc đầu tàu gặp người đi bộ đến lúc đuôi tàu đi qua người đó là:",
        "options": [
          "9,47 giây",
          "10,00 giây",
          "12,50 giây",
          "8,50 giây"
        ],
        "correct": 0,
        "explanation": "v_tương_đối = 20 + (4/3,6) ≈ 21,11 m/s. t = 200 / 21,11 ≈ 9,47 s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một ô tô chạy trên cao tốc với tốc độ 90 km/h (25 m/s). Tài xế nhìn thấy biển báo chướng ngại vật ở cách 65 m. Thời gian phản xạ là 0,8 s và quãng đường hãm phanh là 36 m. Ô tô có dừng kịp không và còn cách chướng ngại vật bao nhiêu mét?",
        "options": [
          "Có dừng kịp, còn cách 9 m",
          "Không kịp, đâm vào chướng ngại vật",
          "Dừng cách 15 m",
          "Dừng chạm đúng chướng ngại vật"
        ],
        "correct": 0,
        "explanation": "s_dừng = (25 × 0,8) + 36 = 20 + 36 = 56 m < 65 m. Cách: 65 - 56 = 9 m."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một thuyền máy xuôi dòng sông từ A đến B mất 1 giờ và ngược dòng từ B về A mất 1,5 giờ. Biết vận tốc của dòng nước là 3 km/h. Chiều dài khúc sông AB là:",
        "options": [
          "18 km",
          "24 km",
          "15 km",
          "12 km"
        ],
        "correct": 0,
        "explanation": "(v_thuyền + 3) × 1 = (v_thuyền - 3) × 1,5 => v_thuyền = 15 km/h => s = (15 + 3) × 1 = 18 km."
      }
    ]
  },
  "phys7_c3_rev_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương III - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương III",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tốc độ của một vật là quãng đường vật đi được trong:",
        "options": [
          "Một đơn vị thời gian",
          "Cả quãng đường",
          "Một giờ duy nhất",
          "Một ngày đêm"
        ],
        "correct": 0,
        "explanation": "Định nghĩa tốc độ là quãng đường vật đi được trong một đơn vị thời gian."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong các chuyển động sau đây, chuyển động nào có thể coi là chuyển động thẳng đều?",
        "options": [
          "Chuyển động của một điểm trên băng tải than đang vận hành ổn định",
          "Chuyển động của xe buýt khi vào bến",
          "Chuyển động của quả bưởi rụng từ trên cây",
          "Chuyển động của con lắc đồng hồ"
        ],
        "correct": 0,
        "explanation": "Băng tải hoạt động ổn định có tốc độ không đổi."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Thiết bị nào sau đây dùng để đo tốc độ tức thời của ô tô một cách chính xác khi đang chạy?",
        "options": [
          "Tốc kế (đồng hồ đo tốc độ trên xe)",
          "Thước cuộn",
          "Đồng hồ bấm giây",
          "Bình chia độ"
        ],
        "correct": 0,
        "explanation": "Tốc kế trên xe hiển thị tức thì tốc độ xe đang chạy."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Đồ thị quãng đường - thời gian của một vật chuyển động có độ dốc càng nhỏ chứng tỏ:",
        "options": [
          "Vật chuyển động càng chậm",
          "Vật chuyển động càng nhanh",
          "Vật đứng yên",
          "Vật quay lại mốc"
        ],
        "correct": 0,
        "explanation": "Độ dốc nhỏ ứng với tốc độ nhỏ, vật chuyển động chậm."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Biển báo hiệu R.420 (bắt đầu khu đông dân cư) yêu cầu người lái xe phải:",
        "options": [
          "Giảm tốc độ và tuân thủ quy định tốc độ tối đa cho phép trong khu vực đông dân cư",
          "Tăng tốc chạy thật nhanh",
          "Bật còi liên tục",
          "Tắt hết đèn chiếu sáng"
        ],
        "correct": 0,
        "explanation": "Biển báo nhắc nhở giảm tốc độ khi vào khu đông dân cư."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hệ thống chống bó cứng phanh ABS giúp phương tiện:",
        "options": [
          "Tránh bị khóa cứng bánh xe gây mất lái và trượt lật khi phanh gấp",
          "Chạy nhanh hơn",
          "Tiết kiệm dầu máy",
          "Phanh dừng ngay tức thì trong 0 giây"
        ],
        "correct": 0,
        "explanation": "Hệ thống ABS duy trì khả năng điều khiển lái khi phanh gấp."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một vận động viên điền kinh chạy cự li 400 m hết 48 giây. Tốc độ trung bình của vận động viên xấp xỉ bằng:",
        "options": [
          "8,33 m/s",
          "10,00 m/s",
          "7,50 m/s",
          "9,20 m/s"
        ],
        "correct": 0,
        "explanation": "v = 400 / 48 ≈ 8,33 m/s."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Đổi tốc độ 90 km/h sang m/s ta được kết quả là:",
        "options": [
          "25 m/s",
          "30 m/s",
          "20 m/s",
          "15 m/s"
        ],
        "correct": 0,
        "explanation": "90 / 3,6 = 25 m/s."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Dùng cổng quang điện đo được tấm chắn sáng 2 cm (0,02 m) đi qua cổng trong 0,05 s. Tốc độ tức thời là:",
        "options": [
          "0,4 m/s",
          "0,1 m/s",
          "2,5 m/s",
          "1,0 m/s"
        ],
        "correct": 0,
        "explanation": "v = 0,02 / 0,05 = 0,4 m/s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t biểu diễn một người đi xe máy: sau 1,5 giờ đi được 60 km. Tốc độ của người đó là:",
        "options": [
          "40 km/h",
          "50 km/h",
          "30 km/h",
          "45 km/h"
        ],
        "correct": 0,
        "explanation": "v = 60 / 1,5 = 40 km/h."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Lực ma sát giữa lốp xe và mặt đường có tác dụng gì quan trọng nhất khi hãm phanh?",
        "options": [
          "Tạo lực hãm làm giảm tốc độ và giúp xe dừng lại",
          "Làm mòn lốp xe",
          "Tạo tiếng kêu rít",
          "Làm nóng động cơ"
        ],
        "correct": 0,
        "explanation": "Ma sát trượt/nghỉ giữa lốp và mặt đường giữ xe dừng lại an toàn."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một người lái xe ở tốc độ 80 km/h (xấp xỉ 22,2 m/s). Trong 1 giây phản xạ, xe đã đi được quãng đường xấp xỉ:",
        "options": [
          "22,2 m",
          "80,0 m",
          "10,0 m",
          "15,5 m"
        ],
        "correct": 0,
        "explanation": "s = 22,2 × 1 = 22,2 m."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về mối liên hệ giữa các đại lượng trong chuyển động đều:",
        "statements": [
          {
            "subId": "a",
            "text": "Quãng đường s tỉ lệ thuận với thời gian chuyển động t.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian t tỉ lệ nghịch với tốc độ v trên cùng quãng đường.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ v tăng gấp đôi thì thời gian đi hết cùng quãng đường tăng gấp đôi.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Đồ thị s - t của chuyển động đều là một đường thẳng đi qua gốc tọa độ O.",
            "correct": true
          }
        ],
        "explanation": "Tốc độ tăng gấp đôi thì thời gian đi phải giảm một nửa."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các phương pháp thực nghiệm xác định tốc độ:",
        "statements": [
          {
            "subId": "a",
            "text": "Đo thời gian bằng cổng quang điện loại bỏ được sai số phản xạ con người.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thước đo có độ chia nhỏ nhất càng nhỏ thì kết quả đo càng chi tiết.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Súng bắn tốc độ chỉ đo được khi xe đứng yên.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Lấy giá trị trung bình cộng nhiều lần đo giúp giảm thiểu sai số ngẫu nhiên.",
            "correct": true
          }
        ],
        "explanation": "Súng bắn tốc độ chuyên dùng để đo các vật đang chuyển động."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Chuyến đi phượt của hai bạn trẻ bằng xe máy qua đoạn đường đèo dài 45 km:",
        "statements": [
          {
            "subId": "a",
            "text": "Chặng leo đèo dài 20 km chạy với tốc độ 25 km/h hết 48 phút (0,8 h).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dừng lại chụp ảnh ngắm cảnh trên đỉnh đèo mất 30 phút (0,5 h).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chặng đổ đèo dài 25 km chạy cẩn thận với tốc độ 30 km/h hết 50 phút (5/6 h).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình trên toàn bộ chuyến đi tính cả thời gian chụp ảnh là 21,1 km/h.",
            "correct": true
          }
        ],
        "explanation": "Tổng t = 0,8 + 0,5 + 5/6 = 2,133 h. v_tb = 45 / 2,133 ≈ 21,1 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tình huống tham gia giao thông trên đường cao tốc lúc trời sương mù:",
        "statements": [
          {
            "subId": "a",
            "text": "Tầm nhìn bị hạn chế nên tài xế phải giảm tốc độ dưới tốc độ tối đa cho phép.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bật đèn sương mù và giữ khoảng cách lớn hơn khoảng cách quy định lúc trời khô ráo.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Được phép vượt xe khác ở những khúc cua bị khuất tầm nhìn.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Quy tắc 3 giây có thể kéo dài thành quy tắc 4 hoặc 5 giây trong điều kiện thời tiết xấu.",
            "correct": true
          }
        ],
        "explanation": "Tuyệt đối không vượt xe tại khúc cua khuất tầm nhìn trong sương mù."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đổi tốc độ 15 m/s sang đơn vị km/h ta được kết quả là bao nhiêu?",
        "correctAnswer": "54",
        "explanation": "15 × 3,6 = 54 km/h."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một máy bay chở khách bay được 1800 km trong 2,5 giờ. Tốc độ của máy bay là bao nhiêu km/h?",
        "correctAnswer": "720",
        "explanation": "v = 1800 / 2,5 = 720 km/h."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khoảng cách an toàn tối thiểu theo quy định khi xe chạy với tốc độ từ trên 60 km/h đến 80 km/h trên đường khô ráo là bao nhiêu mét?",
        "correctAnswer": "55",
        "explanation": "55 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một xe ô tô chạy tốc độ 20 m/s. Quãng đường phản xạ là 14 m, quãng đường hãm phanh là 26 m. Tổng quãng đường dừng xe là bao nhiêu mét?",
        "correctAnswer": "40",
        "explanation": "14 + 26 = 40 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Xe ô tô đi 1/3 quãng đường đầu với tốc độ 40 km/h và 2/3 quãng đường sau với tốc độ 60 km/h. Tốc độ trung bình cả quãng đường là bao nhiêu km/h? (Làm tròn số nguyên)",
        "correctAnswer": "51",
        "explanation": "t1 = (s/3)/40 = s/120; t2 = (2s/3)/60 = s/90. Tổng t = s/120 + s/90 = 7s/360 => v_tb = 360/7 ≈ 51,43 ≈ 51 km/h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một chiếc xe cứu thương chạy với tốc độ 108 km/h (30 m/s) trên đường thẳng. Trong 25 giây, xe đi được bao nhiêu mét?",
        "correctAnswer": "750",
        "explanation": "s = 30 × 25 = 750 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một ô tô khởi hành từ Hà Nội lúc 7h00 sáng để đi Hải Phòng trên quãng đường dài 100 km. Trong 40 km đầu xe chạy với tốc độ 40 km/h; trong 60 km còn lại chạy trên cao tốc với tốc độ 100 km/h. Xe đến Hải Phòng vào thời điểm nào?",
        "options": [
          "8h36 sáng",
          "8h30 sáng",
          "9h00 sáng",
          "8h45 sáng"
        ],
        "correct": 0,
        "explanation": "t1 = 40 / 40 = 1 h. t2 = 60 / 100 = 0,6 h = 36 phút. Tổng t = 1h 36 phút. Đến nơi: 7h00 + 1h36 = 8h36 sáng."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu dài 160 m đang chạy với tốc độ 36 km/h (10 m/s) vượt qua một cây cầu dài 440 m. Thời gian kể từ khi đầu tàu bước lên cầu đến khi toa cuối cùng qua khỏi cầu là:",
        "options": [
          "60 giây",
          "44 giây",
          "50 giây",
          "16 giây"
        ],
        "correct": 0,
        "explanation": "s = 440 + 160 = 600 m. t = 600 / 10 = 60 s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một ô tô chạy trên đường cao tốc với tốc độ 90 km/h (25 m/s). Phía trước có vật cản cách xe 70 m. Thời gian phản xạ của tài xế là 0,8 giây và quãng đường hãm phanh là 35 m. Ô tô có dừng kịp không và còn cách vật cản bao nhiêu mét?",
        "options": [
          "Có dừng kịp, còn cách vật cản 15 m",
          "Không kịp, đâm vào vật cản",
          "Dừng cách 20 m",
          "Dừng cách 5 m"
        ],
        "correct": 0,
        "explanation": "Quãng đường dừng: (25 × 0,8) + 35 = 20 + 35 = 55 m < 70 m. Cách vật cản: 70 - 55 = 15 m."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người chèo thuyền trên khúc sông dài 12 km. Khi xuôi dòng mất 1 giờ, khi ngược dòng mất 2 giờ. Tốc độ chảy của dòng nước là:",
        "options": [
          "3 km/h",
          "6 km/h",
          "2 km/h",
          "1,5 km/h"
        ],
        "correct": 0,
        "explanation": "v_xuôi = 12 / 1 = 12 km/h; v_ngược = 12 / 2 = 6 km/h => v_nước = (12 - 6)/2 = 3 km/h."
      }
    ]
  },
  "phys7_c3_rev_test4": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương III - Đề số 04",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương III",
    "testNum": 4,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Để xác định thời gian chuyển động t từ công thức v = s / t, ta dùng biểu thức:",
        "options": [
          "t = s / v",
          "t = v / s",
          "t = s × v",
          "t = s - v"
        ],
        "correct": 0,
        "explanation": "t = s / v."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong các đơn vị sau, đơn vị nào dùng để đo tốc độ?",
        "options": [
          "km/h",
          "km.h",
          "m.s",
          "kg/m"
        ],
        "correct": 0,
        "explanation": "km/h là đơn vị đo tốc độ."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Dụng cụ nào dùng để đo độ dài quãng đường trong giờ thực hành đo tốc độ?",
        "options": [
          "Thước cuộn",
          "Đồng hồ bấm giây",
          "Cổng quang điện",
          "Ampe kế"
        ],
        "correct": 0,
        "explanation": "Thước cuộn dùng để đo độ dài quãng đường."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Giao điểm của hai đường đồ thị quãng đường - thời gian của hai vật cho biết:",
        "options": [
          "Thời điểm và vị trí hai vật gặp nhau",
          "Tốc độ cực đại",
          "Thời điểm xuất phát",
          "Khoảng cách xa nhất giữa hai vật"
        ],
        "correct": 0,
        "explanation": "Giao điểm xác định thời điểm và vị trí gặp nhau."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Biển báo P.127 có ghi số 80 bên trong báo hiệu:",
        "options": [
          "Tốc độ tối đa cho phép là 80 km/h",
          "Tốc độ tối thiểu là 80 km/h",
          "Đoạn đường dài 80 km",
          "Cấm xe 80 tấn"
        ],
        "correct": 0,
        "explanation": "Biển hạn chế tốc độ tối đa cho phép."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tác dụng quan trọng nhất của dây an toàn trên xe ô tô khi xe phanh gấp là:",
        "options": [
          "Ngăn hành khách văng về phía trước theo quán tính va chạm vào kính chắn gió hoặc vô lăng",
          "Giúp hành khách ngồi êm hơn",
          "Làm xe dừng lại nhanh hơn",
          "Chống buồn ngủ"
        ],
        "correct": 0,
        "explanation": "Dây an toàn giữ người ngồi cố định theo quán tính."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một xe buýt đi quãng đường 30 km trong 45 phút (0,75 giờ). Tốc độ của xe buýt là:",
        "options": [
          "40 km/h",
          "30 km/h",
          "45 km/h",
          "50 km/h"
        ],
        "correct": 0,
        "explanation": "v = 30 / 0,75 = 40 km/h."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Đổi tốc độ 12 m/s sang đơn vị km/h ta được:",
        "options": [
          "43,2 km/h",
          "36,0 km/h",
          "24,0 km/h",
          "48,0 km/h"
        ],
        "correct": 0,
        "explanation": "12 × 3,6 = 43,2 km/h."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tấm chắn sáng rộng 0,03 m đi qua cổng quang điện trong 0,06 s. Tốc độ của vật là:",
        "options": [
          "0,5 m/s",
          "0,2 m/s",
          "1,8 m/s",
          "0,18 m/s"
        ],
        "correct": 0,
        "explanation": "v = 0,03 / 0,06 = 0,5 m/s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t của một ô tô là đường thẳng qua điểm (1,2 h; 72 km). Tốc độ của ô tô là:",
        "options": [
          "60 km/h",
          "72 km/h",
          "50 km/h",
          "80 km/h"
        ],
        "correct": 0,
        "explanation": "v = 72 / 1,2 = 60 km/h."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi tham gia giao thông trên đường, việc giữ khoảng cách an toàn giúp tài xế:",
        "options": [
          "Đủ quãng đường để hãm phanh dừng xe an toàn khi xe phía trước dừng đột ngột",
          "Chạy xe với tốc độ cao hơn",
          "Vượt xe khác dễ hơn",
          "Tiết kiệm xăng"
        ],
        "correct": 0,
        "explanation": "Khoảng cách an toàn tạo không gian phanh dừng tránh va chạm dồn toa."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một người đi xe máy với tốc độ 36 km/h (10 m/s). Trong thời gian phản xạ 0,8 giây, xe đã đi được:",
        "options": [
          "8 m",
          "10 m",
          "6 m",
          "12 m"
        ],
        "correct": 0,
        "explanation": "s = 10 × 0,8 = 8 m."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các tính chất của chuyển động trong tự nhiên:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc độ ánh sáng trong chân không là giới hạn tốc độ lớn nhất trong vũ trụ (~ 300.000 km/s).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ âm thanh trong không khí lớn hơn tốc độ truyền ánh sáng.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Tốc độ của kim giờ đồng hồ nhỏ hơn tốc độ của kim phút đồng hồ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Chuyển động không đều có tốc độ thay đổi theo thời gian.",
            "correct": true
          }
        ],
        "explanation": "Tốc độ ánh sáng (300.000 km/s) lớn hơn rất nhiều tốc độ âm thanh (340 m/s)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về quy trình đo đạc thực nghiệm trong môn KHTN 7:",
        "statements": [
          {
            "subId": "a",
            "text": "Cần chọn thước đo có giới hạn đo lớn hơn độ dài cần đo.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi bấm đồng hồ bấm giây, cần tập trung quan sát điểm xuất phát và đích đến.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cổng quang điện chỉ đo được các vật có bề mặt nhẵn bóng như gương.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Viết kết quả đo cần ghi kèm theo đơn vị đo hợp pháp.",
            "correct": true
          }
        ],
        "explanation": "Cổng quang điện nhận diện được mọi vật chắn cản quang, không cần mặt gương nhẵn."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một xe ô tô tải vận chuyển vật tư qua 2 chặng đường:",
        "statements": [
          {
            "subId": "a",
            "text": "Chặng 1 đường gồ ghề dài 20 km chạy với tốc độ 30 km/h hết 40 phút (2/3 h).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chặng 2 đường nhựa phẳng dài 60 km chạy với tốc độ 60 km/h hết 60 phút (1 h).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tổng thời gian di chuyển của xe là 1 giờ 40 phút (5/3 h).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình trên toàn bộ quãng đường 80 km là 45 km/h.",
            "correct": false
          }
        ],
        "explanation": "Tổng s = 80 km, tổng t = 5/3 h => v_tb = 80 / (5/3) = 48 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Các quy tắc an toàn giao thông đường bộ đối với người đi xe máy:",
        "statements": [
          {
            "subId": "a",
            "text": "Bắt buộc phải đội mũ bảo hiểm có cài quai đúng quy cách khi tham gia giao thông.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Không được chở quá số người quy định (trừ trường hợp chở trẻ em dưới 14 tuổi, người đi cấp cứu).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Được phép sử dụng ô (dù), điện thoại di động khi đang lái xe máy.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tuân thủ tốc độ tối đa cho phép trên từng đoạn đường.",
            "correct": true
          }
        ],
        "explanation": "Tuyệt đối không sử dụng ô, điện thoại khi đang điều khiển xe máy."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đổi tốc độ 8 m/s sang đơn vị km/h ta được kết quả là bao nhiêu? (Làm tròn 1 chữ số thập phân)",
        "correctAnswer": "28.8",
        "explanation": "8 × 3,6 = 28,8 km/h."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một chiếc cano đi quãng đường 60 km trong 1,5 giờ. Tốc độ của cano là bao nhiêu km/h?",
        "correctAnswer": "40",
        "explanation": "v = 60 / 1,5 = 40 km/h."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khoảng cách an toàn tối thiểu quy định khi xe chạy với tốc độ trên 100 km/h đến 120 km/h trên đường cao tốc khô ráo là bao nhiêu mét?",
        "correctAnswer": "100",
        "explanation": "100 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một xe ô tô chạy tốc độ 25 m/s. Quãng đường phản xạ là 20 m, quãng đường hãm phanh là 35 m. Tổng quãng đường dừng xe là bao nhiêu mét?",
        "correctAnswer": "55",
        "explanation": "20 + 35 = 55 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người đi bộ nửa quãng đường đầu với tốc độ 4 km/h và nửa quãng đường sau với tốc độ 6 km/h. Tốc độ trung bình trên cả quãng đường là bao nhiêu km/h?",
        "correctAnswer": "4.8",
        "explanation": "v_tb = 2 × 4 × 6 / (4 + 6) = 48 / 10 = 4,8 km/h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một chiếc tàu ngầm phát tín hiệu siêu âm xuống đáy biển và nhận lại tín hiệu phản xạ sau 1,6 giây. Biết tốc độ âm trong nước biển là 1500 m/s. Độ sâu của đáy biển tại vị trí đó là bao nhiêu mét?",
        "correctAnswer": "1200",
        "explanation": "d = 1500 × 1,6 / 2 = 1200 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu hỏa chạy từ ga A đến ga B cách nhau 240 km. Trong nửa quãng đường đầu tàu chạy với tốc độ 60 km/h, trong nửa quãng đường sau tàu chạy với tốc độ 80 km/h. Thời gian tàu chạy từ A đến B (không kể thời gian đỗ ga) là:",
        "options": [
          "3,5 giờ",
          "3,0 giờ",
          "4,0 giờ",
          "3,2 giờ"
        ],
        "correct": 0,
        "explanation": "t1 = 120 / 60 = 2,0 h. t2 = 120 / 80 = 1,5 h. Tổng t = 3,5 h."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người đứng tại một điểm nhìn thấy tia chớp lóe lên từ đám mây, sau đó đúng 4,5 giây mới nghe thấy tiếng sấm nổ rền. Biết tốc độ âm trong không khí là 340 m/s và ánh sáng truyền đi gần như tức thì. Vị trí tia sét đánh cách người đó khoảng bao nhiêu mét?",
        "options": [
          "1530 m",
          "1360 m",
          "1700 m",
          "1500 m"
        ],
        "correct": 0,
        "explanation": "s = 340 × 4,5 = 1530 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một ô tô chạy trên cao tốc với tốc độ 108 km/h (30 m/s). Phía trước có xe phanh gấp cách 85 m. Thời gian phản xạ của tài xế là 0,7 giây và quãng đường hãm phanh xe dừng hẳn là 45 m. Ô tô có dừng lại kịp không và còn cách xe trước bao nhiêu mét?",
        "options": [
          "Có dừng kịp, còn cách 19 m",
          "Không kịp, đâm vào xe trước",
          "Dừng cách 10 m",
          "Dừng cách 25 m"
        ],
        "correct": 0,
        "explanation": "Quãng đường dừng: (30 × 0,7) + 45 = 21 + 45 = 66 m < 85 m. Cách xe trước: 85 - 66 = 19 m."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một ca nô chạy xuôi dòng một khúc sông dài 48 km hết 1,5 giờ, sau đó ngược dòng trở về hết 2,4 giờ. Tốc độ của ca nô khi nước đứng yên và tốc độ dòng nước lần lượt là:",
        "options": [
          "26 km/h và 6 km/h",
          "25 km/h và 5 km/h",
          "30 km/h và 2 km/h",
          "20 km/h và 4 km/h"
        ],
        "correct": 0,
        "explanation": "v_xuôi = 48 / 1,5 = 32 km/h; v_ngược = 48 / 2,4 = 20 km/h => v_thuyền = (32 + 20)/2 = 26 km/h; v_nước = (32 - 20)/2 = 6 km/h."
      }
    ]
  },
  "phys7_c3_rev_test5": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương III - Đề số 05",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c3",
    "chapterTitle": "Chương III: Tốc độ",
    "lessonId": "phys7_c3_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương III",
    "testNum": 5,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đại lượng nào xác định bằng thương số giữa quãng đường đi được và thời gian đi hết quãng đường đó?",
        "options": [
          "Tốc độ chuyển động",
          "Gia tốc",
          "Khối lượng riêng",
          "Áp suất"
        ],
        "correct": 0,
        "explanation": "Thương số s/t là tốc độ chuyển động."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong các đơn vị sau, đơn vị nào KHÔNG dùng để đo tốc độ?",
        "options": [
          "m/s^2",
          "m/s",
          "km/h",
          "cm/s"
        ],
        "correct": 0,
        "explanation": "m/s^2 là đơn vị của gia tốc, không phải tốc độ."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cổng quang điện dùng trong thí nghiệm thực hành đo tốc độ hoạt động nhờ:",
        "options": [
          "Cảm biến thu phát tia hồng ngoại",
          "Cảm biến nhiệt",
          "Cảm biến âm thanh",
          "Cảm biến trọng lực"
        ],
        "correct": 0,
        "explanation": "Cổng quang điện ứng dụng cảm biến quang hồng ngoại."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trên đồ thị s - t, nếu đoạn đồ thị là đường thẳng xiên góc dốc lên thì:",
        "options": [
          "Vật chuyển động thẳng đều",
          "Vật đứng yên",
          "Vật quay lại mốc",
          "Vật rơi tự do"
        ],
        "correct": 0,
        "explanation": "Đường xiên dốc lên biểu diễn chuyển động thẳng đều."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Biển báo P.127 có số 100 viền đỏ cho biết:",
        "options": [
          "Tốc độ tối đa không được vượt quá 100 km/h",
          "Tốc độ tối thiểu phải đạt 100 km/h",
          "Khoảng cách cách xe 100 m",
          "Cấm xe 100 tấn"
        ],
        "correct": 0,
        "explanation": "Biển hạn chế tốc độ tối đa cho phép 100 km/h."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Mũ bảo hiểm đạt chuẩn cho người đi mô tô, xe máy có tác dụng bảo vệ bộ phận nào quan trọng nhất?",
        "options": [
          "Hộp sọ và não bộ",
          "Khuỷu tay",
          "Bàn chân",
          "Đầu gối"
        ],
        "correct": 0,
        "explanation": "Mũ bảo hiểm bảo vệ đầu và não bộ khỏi chấn thương sọ não nguy hiểm."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một vận động viên bơi cự li 50 m hết 20 giây. Tốc độ bơi trung bình là:",
        "options": [
          "2,5 m/s",
          "2,0 m/s",
          "1,5 m/s",
          "3,0 m/s"
        ],
        "correct": 0,
        "explanation": "v = 50 / 20 = 2,5 m/s."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Đổi tốc độ 108 km/h sang m/s ta được kết quả là:",
        "options": [
          "30 m/s",
          "25 m/s",
          "35 m/s",
          "40 m/s"
        ],
        "correct": 0,
        "explanation": "108 / 3,6 = 30 m/s."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tấm chắn sáng rộng 1 cm (0,01 m) đi qua cổng quang điện trong thời gian 0,025 s. Tốc độ tức thời là:",
        "options": [
          "0,4 m/s",
          "0,25 m/s",
          "4,0 m/s",
          "0,025 m/s"
        ],
        "correct": 0,
        "explanation": "v = 0,01 / 0,025 = 0,4 m/s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị s - t của một ô tô là đường thẳng qua điểm (0,5 h; 35 km). Tốc độ của ô tô là:",
        "options": [
          "70 km/h",
          "35 km/h",
          "50 km/h",
          "60 km/h"
        ],
        "correct": 0,
        "explanation": "v = 35 / 0,5 = 70 km/h."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Theo quy định, khoảng cách an toàn tối thiểu giữa hai xe chạy trên đường khô ráo với tốc độ từ trên 80 km/h đến 100 km/h là:",
        "options": [
          "70 m",
          "55 m",
          "35 m",
          "100 m"
        ],
        "correct": 0,
        "explanation": "Cự li an toàn tối thiểu là 70 m."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một người lái xe ở tốc độ 72 km/h (20 m/s). Trong thời gian phản xạ 0,7 giây, xe đã đi được quãng đường là:",
        "options": [
          "14 m",
          "20 m",
          "10 m",
          "15 m"
        ],
        "correct": 0,
        "explanation": "s = 20 × 0,7 = 14 m."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về bản chất và công thức của tốc độ trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc độ biểu thị quãng đường vật đi được trong một giây hoặc trong một giờ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Xe có tốc độ 60 km/h chạy nhanh hơn xe có tốc độ 15 m/s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ trung bình luôn luôn bằng trung bình cộng vận tốc lớn nhất và nhỏ nhất.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tốc kế trên ô tô đo tốc độ tức thời của ô tô tại thời điểm đang chạy.",
            "correct": true
          }
        ],
        "explanation": "15 m/s = 54 km/h < 60 km/h. Tốc độ trung bình không phải trung bình cộng hai vận tốc cực trị."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các thiết bị kiểm soát tốc độ phương tiện trên cao tốc:",
        "statements": [
          {
            "subId": "a",
            "text": "Hệ thống camera nhận dạng biển số tự động hoạt động liên tục 24/7.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cảnh sát giao thông sử dụng máy đo tốc độ có ghi hình ảnh làm căn cứ xử phạt.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Các phương tiện lưu thông được phép che biển số để tránh camera phạt nguội.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Việc giám sát tốc độ tự động giúp giảm đáng kể tai nạn thảm khốc do phóng nhanh vượt ẩu.",
            "correct": true
          }
        ],
        "explanation": "Hành vi che biển số, làm mờ biển số là vi phạm pháp luật nghiêm trọng."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hành trình di chuyển của một chiếc xe con trên lộ trình 150 km:",
        "statements": [
          {
            "subId": "a",
            "text": "Đoạn 1 đi qua thành phố dài 30 km với tốc độ 40 km/h hết 45 phút (0,75 h).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dừng lại đổ xăng và kiểm tra lốp xe mất 15 phút (0,25 h).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đoạn 2 đi trên cao tốc dài 120 km với tốc độ 80 km/h hết 90 phút (1,5 h).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ trung bình trên toàn tuyến đường 150 km tính cả thời gian đổ xăng là 60 km/h.",
            "correct": true
          }
        ],
        "explanation": "Tổng t = 0,75 + 0,25 + 1,5 = 2,5 h => v_tb = 150 / 2,5 = 60 km/h."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Xét trường hợp một xe ô tô chạy tốc độ 120 km/h (xấp xỉ 33,3 m/s) trên cao tốc:",
        "statements": [
          {
            "subId": "a",
            "text": "Thời gian phản xạ của tài xế là 0,8 s, quãng đường xe đi trước khi phanh là 26,6 m.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Quãng đường hãm phanh đến khi dừng hẳn là 53,4 m.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tổng quãng đường dừng xe an toàn là 80 m.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khoảng cách an toàn tối thiểu theo quy định (100 m) đủ lớn để đảm bảo dừng xe an toàn trong trường hợp này.",
            "correct": true
          }
        ],
        "explanation": "Tổng quãng đường dừng là 80 m < 100 m nên khoảng cách quy định 100 m hoàn toàn an toàn."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đổi tốc độ 25 m/s sang đơn vị km/h ta được kết quả là bao nhiêu?",
        "correctAnswer": "90",
        "explanation": "25 × 3,6 = 90 km/h."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một ô tô chạy quãng đường 210 km trong 3,5 giờ. Tốc độ của ô tô là bao nhiêu km/h?",
        "correctAnswer": "60",
        "explanation": "v = 210 / 3,5 = 60 km/h."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một bạn học sinh đi xe máy điện với tốc độ 25 km/h. Để đi hết quãng đường 15 km từ nhà đến trường ngoại thành, bạn cần bao nhiêu phút?",
        "correctAnswer": "36",
        "explanation": "t = 15 / 25 = 0,6 h = 36 phút."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một xe ô tô chạy tốc độ 20 m/s. Quãng đường phản xạ là 16 m, quãng đường hãm phanh là 34 m. Tổng quãng đường dừng xe là bao nhiêu mét?",
        "correctAnswer": "50",
        "explanation": "16 + 34 = 50 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người đi xe đạp đi nửa quãng đường đầu với tốc độ 10 km/h và nửa quãng đường sau với tốc độ 15 km/h. Tốc độ trung bình cả quãng đường là bao nhiêu km/h?",
        "correctAnswer": "12",
        "explanation": "v_tb = 2 × 10 × 15 / (10 + 15) = 300 / 25 = 12 km/h."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một chiếc ca nô chạy với tốc độ 36 km/h (10 m/s). Trong thời gian 45 giây, ca nô đi được quãng đường bao nhiêu mét?",
        "correctAnswer": "450",
        "explanation": "s = 10 × 45 = 450 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một xe khách khởi hành từ Hà Nội lúc 6h00 sáng để đi Vinh trên quãng đường dài 300 km. Trong 180 km đầu xe chạy trên cao tốc với tốc độ 90 km/h; sau đó xe nghỉ ăn sáng 30 phút; đoạn còn lại 120 km chạy trên quốc lộ với tốc độ 60 km/h. Xe đến Vinh vào thời điểm nào?",
        "options": [
          "10h30 sáng",
          "10h00 sáng",
          "11h00 trưa",
          "11h30 trưa"
        ],
        "correct": 0,
        "explanation": "t1 = 180 / 90 = 2 h. t_nghỉ = 0,5 h. t2 = 120 / 60 = 2 h. Tổng t = 4,5 h. Đến nơi: 6h00 + 4h30 = 10h30 sáng."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu chở khách dài 150 m đang chạy với tốc độ 54 km/h (15 m/s) chạy qua một người đứng quan sát bên đường ray. Thời gian người đó nhìn thấy đoàn tàu chạy qua trước mặt mình là:",
        "options": [
          "10 giây",
          "15 giây",
          "12 giây",
          "8 giây"
        ],
        "correct": 0,
        "explanation": "t = 150 / 15 = 10 s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một ô tô chạy trên cao tốc với tốc độ 80 km/h (xấp xỉ 22,2 m/s). Phía trước có vật cản cách xe 60 m. Thời gian phản xạ của tài xế là 0,7 giây và quãng đường hãm phanh là 32 m. Ô tô có dừng lại kịp trước vật cản không và còn cách vật cản bao nhiêu mét?",
        "options": [
          "Có dừng kịp, còn cách 12,46 m",
          "Không kịp, đâm vào vật cản",
          "Dừng cách 20 m",
          "Dừng chạm đúng vật cản"
        ],
        "correct": 0,
        "explanation": "s_dừng = (22,2 × 0,7) + 32 = 15,54 + 32 = 47,54 m < 60 m. Cách vật cản: 60 - 47,54 = 12,46 m."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người chèo thuyền trên sông từ bến A đến bến B cách nhau 15 km mất 1 giờ 15 phút (1,25 h) khi xuôi dòng. Khi ngược dòng từ B về A mất 2,5 giờ. Vận tốc của dòng nước là:",
        "options": [
          "3 km/h",
          "6 km/h",
          "2 km/h",
          "1,5 km/h"
        ],
        "correct": 0,
        "explanation": "v_xuôi = 15 / 1,25 = 12 km/h; v_ngược = 15 / 2,5 = 6 km/h => v_nước = (12 - 6)/2 = 3 km/h."
      }
    ]
  },
  "phys7_c4_b12_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 12: Sóng âm - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b12",
    "lessonName": "Bài 12: Sóng âm",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Âm thanh được phát ra từ các vật khi chúng:",
        "options": [
          "Đang dao động",
          "Đang đứng yên",
          "Được chiếu sáng",
          "Bị nung nóng"
        ],
        "correct": 0,
        "explanation": "Tất cả các vật phát ra âm thanh đều đang dao động."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Sóng âm truyền được trong các môi trường nào sau đây?",
        "options": [
          "Chất rắn, chất lỏng và chất khí",
          "Chỉ truyền được trong chất khí",
          "Chỉ truyền được trong chất rắn",
          "Truyền được trong chân không"
        ],
        "correct": 0,
        "explanation": "Sóng âm truyền được trong cả chất rắn, chất lỏng và chất khí."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Môi trường nào sau đây KHÔNG THỂ truyền được sóng âm?",
        "options": [
          "Chân không",
          "Nước cất",
          "Không khí",
          "Thanh thép"
        ],
        "correct": 0,
        "explanation": "Chân không không có các hạt vật chất nên không truyền được dao động âm."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "So sánh tốc độ truyền âm trong ba trạng thái của vật chất theo thứ tự giảm dần:",
        "options": [
          "Chất rắn > Chất lỏng > Chất khí",
          "Chất khí > Chất lỏng > Chất rắn",
          "Chất lỏng > Chất khí > Chất rắn",
          "Chất khí > Chất rắn > Chất lỏng"
        ],
        "correct": 0,
        "explanation": "Tốc độ truyền âm giảm dần từ chất rắn đến chất lỏng và chậm nhất trong chất khí."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tốc độ truyền âm trong không khí ở nhiệt độ 20 °C xấp xỉ bằng:",
        "options": [
          "340 m/s",
          "1500 m/s",
          "5000 m/s",
          "300.000 km/s"
        ],
        "correct": 0,
        "explanation": "Tốc độ âm trong không khí ở 20 °C là khoảng 340 m/s."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Bộ phận dao động phát ra âm thanh khi gõ vào dùi trống là:",
        "options": [
          "Mặt trống",
          "Thân trống",
          "Dùi trống",
          "Chân giá đỡ trống"
        ],
        "correct": 0,
        "explanation": "Khi gõ, dùi làm mặt trống dao động đàn hồi phát ra âm thanh."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi một người nói chuyện, bộ phận nào trong cơ thể dao động phát ra âm thanh?",
        "options": [
          "Hai dây thanh quản trong thanh quản",
          "Lưỡi",
          "Răng",
          "Vòm họng"
        ],
        "correct": 0,
        "explanation": "Luồng khí từ phổi đi qua làm rung hai dây thanh quản phát ra âm thanh tiếng nói."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Các nhà du hành vũ trụ khi làm việc ngoài không gian bên ngoài tàu vũ trụ không thể nói chuyện trực tiếp với nhau bằng giọng nói mà phải dùng bộ đàm vì:",
        "options": [
          "Không gian vũ trụ là môi trường chân không, không thể truyền được âm thanh",
          "Ngoài vũ trụ quá lạnh",
          "Mũ phi hành gia quá dày",
          "Âm thanh bị gió thổi bay"
        ],
        "correct": 0,
        "explanation": "Chân không không có phần tử vật chất để truyền sóng âm."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Người ta gõ một nhát búa vào thanh kim loại dài. Người ở đầu kia nghe thấy âm thanh truyền qua:",
        "options": [
          "Kim loại trước rồi mới đến âm thanh truyền qua không khí",
          "Không khí trước rồi mới đến kim loại",
          "Cả hai âm cùng một lúc",
          "Chỉ nghe thấy âm truyền qua không khí"
        ],
        "correct": 0,
        "explanation": "Tốc độ âm trong kim loại (rắn) lớn hơn nhiều so với trong không khí (khí) nên âm qua kim loại tới trước."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tốc độ truyền âm trong nước biển xấp xỉ bằng:",
        "options": [
          "1500 m/s",
          "340 m/s",
          "3000 m/s",
          "1000 km/h"
        ],
        "correct": 0,
        "explanation": "Trong chất lỏng (nước biển), tốc độ âm khoảng 1500 m/s."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi áp tai xuống mặt đất, người lính xưa có thể nghe thấy tiếng vó ngựa từ xa trước khi nghe qua không khí vì:",
        "options": [
          "Mặt đất (chất rắn) truyền âm thanh nhanh hơn và ít bị suy giảm năng lượng hơn không khí",
          "Dưới đất có đường hầm",
          "Mặt đất phát ra âm thanh",
          "Vó ngựa đập vào đá"
        ],
        "correct": 0,
        "explanation": "Chất rắn truyền âm nhanh hơn và bảo toàn năng lượng tốt hơn chất khí."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Sóng âm là gì?",
        "options": [
          "Là sự lan truyền dao động âm trong môi trường vật chất",
          "Là các tia sáng chiếu vào mắt",
          "Là dòng các hạt electron",
          "Là luồng gió thổi"
        ],
        "correct": 0,
        "explanation": "Sóng âm là sự lan truyền các dao động cơ học trong môi trường."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét bản chất và sự truyền sóng âm trong các môi trường:",
        "statements": [
          {
            "subId": "a",
            "text": "Mọi vật phát ra âm thanh đều có nguồn gốc từ sự dao động.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi gảy đàn guitar, các sợi dây đàn dao động phát ra âm thanh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sóng âm có thể truyền qua lớp tường bê tông của căn phòng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Âm thanh truyền trong không khí nhanh hơn trong nước.",
            "correct": false
          }
        ],
        "explanation": "Âm truyền trong nước (lỏng ~ 1500 m/s) nhanh hơn nhiều so với trong không khí (khí ~ 340 m/s)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về thí nghiệm đặt chuông điện đang reo trong bình thủy tinh rồi hút dần không khí ra ngoài:",
        "statements": [
          {
            "subId": "a",
            "text": "Khi bình còn đầy không khí, ta nghe thấy tiếng chuông reo rõ ràng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi bắt đầu hút không khí ra, tiếng chuông reo nghe nhỏ dần.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi trong bình gần như là chân không hoàn toàn, ta hầu như không còn nghe thấy tiếng chuông nữa.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu mở van cho không khí tràn trở lại vào bình thì tiếng chuông vẫn bị mất vĩnh viễn.",
            "correct": false
          }
        ],
        "explanation": "Khi không khí vào lại, tiếng chuông lại truyền qua không khí đến tai người nghe rõ ràng."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hai bạn học sinh chơi trò 'điện thoại ống bơ' bằng hai lon sữa bò nối với nhau bởi một sợi dây dù căng thẳng dài 15 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Khi bạn A nói vào miệng lon, đáy lon A dao động.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dao động của đáy lon truyền dọc theo sợi dây dù căng đến đáy lon B.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đáy lon B dao động làm rung không khí truyền đến tai bạn B.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu sợi dây dù bị chùng xuống hoặc bị tay người khác giữ chặt thì âm thanh vẫn truyền tốt.",
            "correct": false
          }
        ],
        "explanation": "Sợi dây bị chùng hoặc bị bóp chặt sẽ triệt tiêu dao động cơ học, âm thanh không truyền được."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một tia sét đánh xuống mặt đất cách người quan sát 1020 m trong một ngày mưa giông:",
        "statements": [
          {
            "subId": "a",
            "text": "Ánh sáng chớp truyền đến mắt người gần như tức thời.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ truyền âm thanh trong không khí là 340 m/s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thời gian từ lúc thấy tia chớp đến khi nghe thấy tiếng sấm là 3,0 giây.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu sau 5 giây mới nghe thấy tiếng sấm thì vị trí sét đánh cách xa 2000 m.",
            "correct": false
          }
        ],
        "explanation": "s = v × t = 340 × 5 = 1700 m (câu d ghi 2000 m là sai)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tốc độ truyền âm trong không khí ở 20 °C là bao nhiêu m/s?",
        "correctAnswer": "340",
        "explanation": "340 m/s."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tốc độ truyền âm trong nước biển xấp xỉ bằng bao nhiêu m/s?",
        "correctAnswer": "1500",
        "explanation": "1500 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một người nhìn thấy tia chớp rồi sau 2,0 giây nghe thấy tiếng sấm. Biết v = 340 m/s. Nơi sét đánh cách người đó bao nhiêu mét?",
        "correctAnswer": "680",
        "explanation": "s = 340 × 2 = 680 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Âm thanh truyền trong chất thép với tốc độ 5000 m/s. Để truyền đi quãng đường 1000 m trong thanh ray thép, âm thanh mất thời gian bao nhiêu giây?",
        "correctAnswer": "0.2",
        "explanation": "t = 1000 / 5000 = 0,2 s."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người gõ búa vào đầu ống kim loại dài 680 m. Người ở đầu kia nghe thấy tiếng gõ truyền qua không khí (v = 340 m/s) sau bao nhiêu giây?",
        "correctAnswer": "2",
        "explanation": "t = 680 / 340 = 2 s."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Tàu nghiên cứu hải dương phát xung âm thanh xuống đáy biển và thu lại tín hiệu sau 1,4 giây. Với tốc độ âm trong nước là 1500 m/s, độ sâu của biển là bao nhiêu mét?",
        "correctAnswer": "1050",
        "explanation": "d = 1500 × 1,4 / 2 = 1050 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người gõ một nhát búa vào một đầu ống kim loại bằng thép dài 510 m. Người thứ hai áp tai vào đầu kia của ống nghe thấy hai tiếng gõ liên tiếp: một tiếng truyền qua thép và một tiếng truyền qua cột không khí bên trong ống. Biết tốc độ âm trong không khí là 340 m/s và trong thép là 5100 m/s. Khoảng thời gian giữa hai lần nghe thấy tiếng gõ là:",
        "options": [
          "1,4 giây",
          "1,5 giây",
          "0,1 giây",
          "1,0 giây"
        ],
        "correct": 0,
        "explanation": "t_khí = 510 / 340 = 1,5 s. t_thép = 510 / 5100 = 0,1 s => Khoảng thời gian: 1,5 - 0,1 = 1,4 s."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người đứng tại một điểm nhìn thấy một công nhân gõ búa lên mặt đe sắt ở đằng xa. Cứ sau mỗi lần búa chạm đe sắt thì đúng 0,5 giây sau người đó mới nghe thấy tiếng đe vang tới tai. Biết tốc độ âm trong không khí là 340 m/s. Khoảng cách từ người quan sát đến vị trí công nhân làm việc là:",
        "options": [
          "170 m",
          "340 m",
          "85 m",
          "200 m"
        ],
        "correct": 0,
        "explanation": "s = v × t = 340 × 0,5 = 170 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tại sao khi đặt ngón tay chạm nhẹ vào thanh quản ở cổ lúc đang phát âm (nói hoặc hát) ta cảm thấy ngón tay bị rung lên?",
        "options": [
          "Vì thanh quản đang dao động đàn hồi để phát ra âm thanh",
          "Vì máu chảy qua mạnh",
          "Vì ngón tay bị giật điện",
          "Vì tim đập nhanh"
        ],
        "correct": 0,
        "explanation": "Dây thanh quản rung dao động truyền lực làm ngón tay cảm nhận sự rung động."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước một vách núi đá hoa cương lớn hét to một tiếng, sau 0,8 giây người đó nghe thấy tiếng hét của mình dội ngược lại từ vách núi. Biết tốc độ âm trong không khí là 340 m/s. Khoảng cách từ người đó đến vách núi là:",
        "options": [
          "136 m",
          "272 m",
          "170 m",
          "340 m"
        ],
        "correct": 0,
        "explanation": "Quãng đường âm đi và về: 2d = v × t => d = 340 × 0,8 / 2 = 136 m."
      }
    ]
  },
  "phys7_c4_b12_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 12: Sóng âm - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b12",
    "lessonName": "Bài 12: Sóng âm",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật phát ra âm thanh được gọi là:",
        "options": [
          "Nguồn âm",
          "Gương phẳng",
          "Nhiệt kế",
          "Pin điện"
        ],
        "correct": 0,
        "explanation": "Vật phát ra âm thanh gọi là nguồn âm."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khi gảy một sợi dây đàn bầu, vật phát ra âm thanh là:",
        "options": [
          "Sợi dây đàn đang rung động",
          "Bầu đàn",
          "Cần đàn",
          "Móng gảy"
        ],
        "correct": 0,
        "explanation": "Sợi dây đàn dao động là nguồn phát ra âm chính."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Sóng âm lan truyền được trong chất rắn, lỏng, khí là nhờ:",
        "options": [
          "Sự dao động của các hạt phần tử cấu tạo nên môi trường",
          "Ánh sáng chiếu vào",
          "Điện tích di chuyển",
          "Từ trường"
        ],
        "correct": 0,
        "explanation": "Các hạt phân tử vật chất truyền dao động cho nhau tạo thành sóng âm."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trên Mặt Trăng không có bầu khí quyển (môi trường chân không). Nếu hai phi hành gia đứng cạnh nhau gõ hai viên đá vào nhau thì:",
        "options": [
          "Họ không thể nghe thấy tiếng gõ qua không khí",
          "Họ nghe thấy rất to",
          "Họ bị điếc tai",
          "Viên đá phát sáng"
        ],
        "correct": 0,
        "explanation": "Chân không không truyền được âm thanh."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong môi trường nào sau đây sóng âm truyền đi với tốc độ lớn nhất?",
        "options": [
          "Thanh sắt (chất rắn)",
          "Nước biển (chất lỏng)",
          "Không khí (chất khí)",
          "Khí hydro"
        ],
        "correct": 0,
        "explanation": "Chất rắn có liên kết phân tử dày đặc nên truyền âm nhanh nhất."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Âm thanh truyền từ nguồn âm đến tai người nghe thông qua:",
        "options": [
          "Sự lan truyền sóng âm trong không khí",
          "Tia phóng xạ",
          "Tia laser",
          "Gió thổi"
        ],
        "correct": 0,
        "explanation": "Sóng âm lan truyền làm màng nhĩ tai dao động."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi thổi sáo trúc, cột không khí bên trong ống sáo dao động phát ra âm thanh. Nguồn âm ở đây là:",
        "options": [
          "Cột không khí bên trong ống sáo",
          "Vỏ ngoài ống sáo",
          "Ngón tay bấm",
          "Miệng người thổi"
        ],
        "correct": 0,
        "explanation": "Luồng hơi làm cột không khí bên trong lòng ống sáo dao động phát ra âm."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một người lặn dưới nước vẫn có thể nghe thấy tiếng động cơ của chiếc thuyền chạy trên mặt nước. Điều này chứng tỏ:",
        "options": [
          "Sóng âm có thể truyền được trong chất lỏng",
          "Chất lỏng không truyền được âm",
          "Người đó có khả năng đặc biệt",
          "Nước biến thành không khí"
        ],
        "correct": 0,
        "explanation": "Chứng minh chất lỏng (nước) là môi trường truyền âm tốt."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một tia sét đánh cách người quan sát 1360 m. Thời gian từ lúc thấy ánh chớp đến khi nghe tiếng sấm (v = 340 m/s) là:",
        "options": [
          "4,0 giây",
          "2,0 giây",
          "3,0 giây",
          "5,0 giây"
        ],
        "correct": 0,
        "explanation": "t = s / v = 1360 / 340 = 4,0 s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tại sao người ta thường làm tường phòng hát karaoke bằng vật liệu mút xốp đục lỗ hoặc bọc vải nỉ nhung?",
        "options": [
          "Để ngăn cản và hấp thụ sóng âm, giảm sự truyền âm ra bên ngoài",
          "Để phòng hát sáng hơn",
          "Để tường không bị bụi",
          "Để phòng mát hơn"
        ],
        "correct": 0,
        "explanation": "Vật liệu xốp mềm tiêu âm, hạn chế âm thanh truyền ra các phòng xung quanh."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tốc độ âm trong không khí ở 0 °C khoảng 331 m/s, ở 20 °C khoảng 340 m/s. Nhận xét nào đúng?",
        "options": [
          "Nhiệt độ không khí tăng thì tốc độ truyền âm tăng lên",
          "Nhiệt độ tăng tốc độ truyền âm giảm",
          "Tốc độ âm không phụ thuộc nhiệt độ",
          "Tốc độ âm giảm về 0"
        ],
        "correct": 0,
        "explanation": "Nhiệt độ môi trường tăng làm các phân tử chuyển động nhiệt nhanh hơn, tốc độ âm tăng."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cá voi và cá heo có thể giao tiếp với nhau ở khoảng cách hàng chục kilômét trong đại dương nhờ:",
        "options": [
          "Sóng âm truyền rất xa và nhanh trong môi trường nước",
          "Chúng dùng ánh sáng",
          "Chúng bơi lại gần nhau",
          "Chúng dùng mùi hương"
        ],
        "correct": 0,
        "explanation": "Nước biển truyền sóng âm cực tốt và ít bị hấp thụ ở tần số thấp."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các đặc điểm của nguồn âm trong tự nhiên:",
        "statements": [
          {
            "subId": "a",
            "text": "Mặt trống dao động khi đánh trống phát ra tiếng kêu tùng tùng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cánh ong vỗ rất nhanh trong không khí phát ra tiếng vo ve.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tất cả các nguồn âm đều đứng yên hoàn toàn khi phát ra âm thanh.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khi âm thoa phát ra âm thanh, các nhánh của nó dao động rất nhanh.",
            "correct": true
          }
        ],
        "explanation": "Mọi nguồn âm bắt buộc phải dao động đàn hồi."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về sự lan truyền âm thanh trong đời sống hàng ngày:",
        "statements": [
          {
            "subId": "a",
            "text": "Tiếng chuông nhà thờ truyền qua không khí đến tai người nghe.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Người áp tai vào vách tường có thể nghe thấy tiếng nói thì thầm từ phòng bên cạnh truyền qua chất rắn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu đặt một chiếc đồng hồ báo thức vào bình hút chân không thì ta không nghe thấy chuông reo.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tốc độ truyền âm trong không khí lớn hơn tốc độ truyền âm trong bê tông cốt thép.",
            "correct": false
          }
        ],
        "explanation": "Trong bê tông cốt thép (chất rắn), âm truyền nhanh gấp hơn 10 lần trong không khí."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Học sinh làm thí nghiệm chứng minh mặt trống dao động khi phát ra âm:",
        "statements": [
          {
            "subId": "a",
            "text": "Rắc vài mẩu giấy vụn nhỏ hoặc hạt xốp lên mặt trống.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Gõ mạnh vào mặt trống, các mẩu giấy vụn nảy lên tung tóe.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tiếng trống càng to thì các mẩu giấy vụn nảy lên càng cao.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khi dùng tay giữ chặt mặt trống, mặt trống ngừng dao động nhưng tiếng trống vẫn vang mãi.",
            "correct": false
          }
        ],
        "explanation": "Khi mặt trống ngừng dao động thì âm thanh lập tức tắt hẳn."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một vụ nổ mìn phá đá tại mỏ đá cách khu dân cư 1700 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Người dân nhìn thấy cột khói bốc lên trước khi nghe thấy tiếng nổ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian âm thanh truyền từ mỏ đá đến khu dân cư qua không khí là 5,0 giây.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu có một đường ray sắt nối thẳng từ mỏ đá về khu dân cư thì âm truyền qua ray sắt mất khoảng 0,34 giây.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Người áp tai xuống mặt đất sẽ nghe thấy tiếng nổ sau người đứng thẳng nghe qua không khí.",
            "correct": false
          }
        ],
        "explanation": "Âm truyền qua mặt đất (chất rắn) nhanh hơn nhiều qua không khí nên người áp tai nghe trước."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một chiếc âm thoa phát ra âm, nhánh âm thoa thực hiện dao động. Nguồn phát ra âm ở đây là gì? (Nhánh âm thoa hay Cán âm thoa)",
        "correctAnswer": "Nhánh âm thoa",
        "explanation": "Nhánh âm thoa dao động tạo ra âm."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tốc độ âm trong một thanh nhôm là khoảng 6420 m/s. Thanh nhôm thuộc thể nào của vật chất? (Rắn, Lỏng hay Khí)",
        "correctAnswer": "Rắn",
        "explanation": "Nhôm là kim loại thể rắn."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Người nhìn thấy pháo hoa nổ sáng trên bầu trời rồi sau 1,5 giây mới nghe thấy tiếng nổ. Biết v = 340 m/s. Điểm nổ pháo hoa cách người đó bao nhiêu mét?",
        "correctAnswer": "510",
        "explanation": "s = 340 × 1,5 = 510 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Âm thanh truyền trong nước biển với tốc độ 1500 m/s. Trong 0,6 giây, âm truyền đi được bao nhiêu mét?",
        "correctAnswer": "900",
        "explanation": "s = 1500 × 0,6 = 900 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách vách đá hét to, sau 1,2 giây nghe thấy âm phản xạ. Biết v = 340 m/s. Khoảng cách đến vách đá là bao nhiêu mét?",
        "correctAnswer": "204",
        "explanation": "d = 340 × 1,2 / 2 = 204 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Tàu đánh cá dùng máy đo hồi âm phát sóng âm xuống đáy biển và nhận lại tín hiệu sau 0,8 giây. Biết tốc độ âm trong nước là 1500 m/s. Độ sâu đáy biển là bao nhiêu mét?",
        "correctAnswer": "600",
        "explanation": "d = 1500 × 0,8 / 2 = 600 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng tại một bờ sông rộng, nhìn sang bờ bên kia thấy một người thợ đóng cọc gỗ bằng búa. Cứ sau mỗi nhát búa đập vào cọc gỗ thì đúng 0,75 giây sau người này mới nghe thấy âm thanh phát ra. Biết tốc độ âm trong không khí là 340 m/s. Bề rộng của khúc sông tại vị trí đó là:",
        "options": [
          "255 m",
          "340 m",
          "170 m",
          "510 m"
        ],
        "correct": 0,
        "explanation": "s = 340 × 0,75 = 255 m."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Để đo khoảng cách giữa hai mỏm núi A và B, một nhà địa chất đứng tại mỏm núi A bắn một phát súng hiệu và đo được thời gian từ lúc bắn đến khi nghe thấy tiếng vang dội lại từ mỏm B là 2,5 giây. Biết tốc độ âm trong không khí là 340 m/s. Khoảng cách giữa hai mỏm núi là:",
        "options": [
          "425 m",
          "850 m",
          "680 m",
          "340 m"
        ],
        "correct": 0,
        "explanation": "d = 340 × 2,5 / 2 = 425 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tại sao khi ta dán chặt một miếng băng dính hoặc đặt bàn tay đè lên mặt trống đang rung thì tiếng trống lập tức tắt ngay?",
        "options": [
          "Vì bàn tay cản trở và dập tắt sự dao động của mặt trống, khi nguồn âm ngừng dao động thì âm thanh dừng phát ra",
          "Vì bàn tay hút hết âm thanh",
          "Vì dùi trống bị gãy",
          "Vì không khí bị đẩy ra ngoài"
        ],
        "correct": 0,
        "explanation": "Nguồn âm ngừng dao động thì âm thanh ngừng phát ra."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người gõ một hồi búa vào một đầu ống dẫn nước bằng gang dài 680 m. Người thứ hai ở đầu kia đặt một tai áp sát vào thành ống và tai kia hướng ra ngoài không khí. Người đó sẽ nghe thấy hai tiếng gõ cách nhau một khoảng thời gian là bao nhiêu? Biết tốc độ âm trong không khí là 340 m/s và trong gang là 3400 m/s.",
        "options": [
          "1,8 giây",
          "2,0 giây",
          "0,2 giây",
          "1,5 giây"
        ],
        "correct": 0,
        "explanation": "t_khí = 680 / 340 = 2,0 s; t_gang = 680 / 3400 = 0,2 s => Cách nhau: 2,0 - 0,2 = 1,8 s."
      }
    ]
  },
  "phys7_c4_b12_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 12: Sóng âm - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b12",
    "lessonName": "Bài 12: Sóng âm",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Dụng cụ thí nghiệm hình chữ U bằng thép dùng để tạo ra âm thanh chuẩn trong phòng thí nghiệm là:",
        "options": [
          "Âm thoa (tuning fork)",
          "Lực kế",
          "Nhiệt kế",
          "Kính hiển vi"
        ],
        "correct": 0,
        "explanation": "Âm thoa là dụng cụ chuẩn phát âm thanh thanh khi gõ."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khi gõ vào một chiếc cồng chiêng Tây Nguyên, âm thanh phát ra từ:",
        "options": [
          "Mặt cồng chiêng đang dao động đàn hồi",
          "Dùi gõ chiêng",
          "Khung treo chiêng",
          "Mặt đất"
        ],
        "correct": 0,
        "explanation": "Thân và mặt chiêng dao động phát ra âm thanh trầm vang."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Sóng âm truyền trong không khí theo dạng:",
        "options": [
          "Sự lan truyền liên tiếp các lớp không khí co lại (nén) và dãn ra",
          "Đường thẳng tắp không dao động",
          "Đường tròn tĩnh",
          "Tia sáng"
        ],
        "correct": 0,
        "explanation": "Sóng âm trong chất khí là các lớp sóng nén và dãn lan truyền."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong các môi trường: nước biển, thanh nhôm, không khí và chân không, môi trường có tốc độ truyền âm nhỏ nhất (khác 0) là:",
        "options": [
          "Không khí",
          "Nước biển",
          "Thanh nhôm",
          "Chân không"
        ],
        "correct": 0,
        "explanation": "Tốc độ âm trong không khí (~ 340 m/s) là nhỏ nhất trong các môi trường vật chất trên."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Màng nhĩ trong tai người có vai trò gì khi nghe âm thanh?",
        "options": [
          "Dao động cùng tần số với sóng âm truyền tới và truyền tín hiệu thần kinh lên não",
          "Phát ra âm thanh",
          "Lọc sạch bụi",
          "Chắn gió"
        ],
        "correct": 0,
        "explanation": "Màng nhĩ dao động cảm nhận sóng âm truyền đến."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hiện tượng sóng âm truyền từ vật phát ra âm tới tai người nghe chứng tỏ:",
        "options": [
          "Sóng âm mang theo năng lượng",
          "Sóng âm không có năng lượng",
          "Sóng âm là ánh sáng",
          "Sóng âm làm nóng môi trường"
        ],
        "correct": 0,
        "explanation": "Sóng âm mang năng lượng làm dao động màng nhĩ tai."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một người đứng xem bắn pháo hoa thấy chùm pháo hoa lóe sáng rồi 3,0 giây sau mới nghe thấy tiếng nổ. Biết v = 340 m/s. Khoảng cách đến pháo hoa là:",
        "options": [
          "1020 m",
          "340 m",
          "680 m",
          "1500 m"
        ],
        "correct": 0,
        "explanation": "s = 340 × 3,0 = 1020 m."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Vì sao người ta có thể dùng ống nghe y tế (ống nghe bác sĩ) để nghe rõ nhịp tim và tiếng thở của bệnh nhân?",
        "options": [
          "Vì ống nghe dẫn sóng âm truyền qua chất rắn và chất khí bên trong ống đến tai bác sĩ mà ít bị thất thoát năng lượng",
          "Vì ống nghe khuếch đại dòng điện",
          "Vì ống nghe phát ra siêu âm",
          "Vì ống nghe làm tim đập to hơn"
        ],
        "correct": 0,
        "explanation": "Ống nghe định hướng sóng âm tập trung truyền thẳng vào tai bác sĩ."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Khi một con ruồi hoặc muỗi bay qua tai, ta nghe thấy tiếng vo ve là do:",
        "options": [
          "Đôi cánh của chúng vỗ (dao động) rất nhanh trong không khí",
          "Miệng chúng kêu",
          "Chân chúng cọ vào nhau",
          "Mắt chúng chớp"
        ],
        "correct": 0,
        "explanation": "Cánh muỗi/ruồi dao động hàng trăm lần trong 1 giây phát ra âm thanh."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khi áp tai vào một chiếc cốc thủy tinh rỗng úp lên mặt bàn gỗ rồi gõ nhẹ vào đầu bàn kia, ta nghe thấy tiếng gõ rất rõ. Điều đó chứng tỏ:",
        "options": [
          "Chất rắn truyền âm rất tốt",
          "Cốc thủy tinh phát ra âm thanh",
          "Bàn gỗ không truyền được âm",
          "Mặt bàn bị vỡ"
        ],
        "correct": 0,
        "explanation": "Gỗ và thủy tinh (chất rắn) truyền dao động âm rất hiệu quả."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Sự truyền âm trong chất rắn nhanh hơn trong chất khí chủ yếu là do:",
        "options": [
          "Các phân tử trong chất rắn liên kết chặt chẽ và ở gần nhau hơn nhiều so với chất khí",
          "Chất rắn nặng hơn chất khí",
          "Chất rắn trong suốt hơn",
          "Chất khí cản trở âm thanh"
        ],
        "correct": 0,
        "explanation": "Khoảng cách giữa các hạt phân tử chất rắn rất nhỏ nên việc truyền xung lượng dao động diễn ra nhanh hơn."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Khi lặn sâu dưới hồ bơi, nếu có người gõ hai viên đá vào nhau dưới nước thì người thợ lặn:",
        "options": [
          "Nghe thấy tiếng gõ rất rõ ràng",
          "Hoàn toàn không nghe thấy gì",
          "Chỉ nhìn thấy bọt khí",
          "Nghe thấy tiếng sét"
        ],
        "correct": 0,
        "explanation": "Nước truyền âm rất tốt nên thợ lặn nghe rất rõ."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các hiện tượng liên quan đến nguồn âm trong thực tế:",
        "statements": [
          {
            "subId": "a",
            "text": "Thổi sáo trúc làm cột không khí bên trong ống sáo dao động phát ra âm thanh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi gảy đàn guitar, chỉ có thùng đàn dao động chứ dây đàn không chuyển động.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Khi bật loa phát nhạc, màng loa chuyển động rung qua lại liên tục.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dây chun kéo căng khi gảy nhẹ sẽ dao động và phát ra âm thanh nhỏ.",
            "correct": true
          }
        ],
        "explanation": "Dây đàn bắt buộc phải dao động khi gảy."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về khả năng truyền âm của các môi trường:",
        "statements": [
          {
            "subId": "a",
            "text": "Tường gạch và cửa kính đều có thể truyền được âm thanh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Các loài cá dưới nước có thể nghe được tiếng chân người bước trên bờ để bơi đi lẩn trốn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trong chân không, tốc độ truyền âm đạt tới 300.000 km/s.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Nhiệt độ không khí càng cao thì tốc độ truyền âm trong không khí càng tăng nhẹ.",
            "correct": true
          }
        ],
        "explanation": "Trong chân không hoàn toàn không truyền được âm (tốc độ bằng 0). 300.000 km/s là tốc độ ánh sáng."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Thí nghiệm gõ một nhánh âm thoa rồi nhúng nhẹ đầu nhánh vào một cốc nước:",
        "statements": [
          {
            "subId": "a",
            "text": "Các giọt nước trong cốc bắn tung tóe ra xung quanh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hiện tượng nước bắn tung tóe chứng tỏ nhánh âm thoa đang dao động đàn hồi.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu không gõ âm thoa mà nhúng vào nước thì nước vẫn bắn tung tóe như vậy.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khi âm thoa ngừng kêu thì nước trong cốc trở lại trạng thái mặt phẳng lặng.",
            "correct": true
          }
        ],
        "explanation": "Nếu không gõ thì âm thoa không dao động, nước không thể bắn tung tóe."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người thợ lặn ở độ sâu 15 m dưới đáy hồ nước nghe thấy tiếng nổ phát ra từ một chiếc cano trên mặt hồ:",
        "statements": [
          {
            "subId": "a",
            "text": "Sóng âm truyền từ động cơ cano qua lớp nước hồ tới tai người thợ lặn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ âm trong nước lớn hơn trong không khí nên sóng âm đến thợ lặn rất nhanh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu thợ lặn ở trên Mặt Trăng lặn trong hồ cồn không có khí quyển thì vẫn nghe thấy âm thanh truyền trong chất lỏng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Âm thanh hoàn toàn không thể truyền từ không khí vào trong nước.",
            "correct": false
          }
        ],
        "explanation": "Âm thanh truyền được qua ranh giới giữa không khí và nước."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một chiếc chuông đồng khi đánh phát ra âm thanh. Bộ phận nào dao động? (Thành chuông hay Dây treo)",
        "correctAnswer": "Thành chuông",
        "explanation": "Thành chuông đồng dao động phát ra âm thanh."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Sóng âm có truyền được qua bức tường bê tông không? (Có hay Không)",
        "correctAnswer": "Có",
        "explanation": "Bê tông là chất rắn truyền âm tốt."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một tiếng sấm rền vang sau tia chớp 4,0 giây. Tốc độ âm trong không khí là 340 m/s. Khoảng cách từ tia sét đến người quan sát là bao nhiêu mét?",
        "correctAnswer": "1360",
        "explanation": "s = 340 × 4 = 1360 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Âm thanh truyền trong nước biển với tốc độ 1500 m/s. Để truyền đi quãng đường 3000 m, âm thanh cần thời gian bao nhiêu giây?",
        "correctAnswer": "2",
        "explanation": "t = 3000 / 1500 = 2 s."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người gõ búa vào thanh kim loại dài 850 m. Âm truyền qua không khí (v = 340 m/s) mất thời gian bao nhiêu giây?",
        "correctAnswer": "2.5",
        "explanation": "t = 850 / 340 = 2,5 s."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Tàu nghiên cứu đáy đại dương phát xung âm sonar xuống đáy biển và nhận lại tín hiệu sau 2,0 giây. Độ sâu của đáy đại dương là bao nhiêu mét? (v = 1500 m/s)",
        "correctAnswer": "1500",
        "explanation": "d = 1500 × 2 / 2 = 1500 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách một vách núi đá vôi thẳng đứng và bắn một phát súng hiệu. Sau 1,6 giây, người đó nghe thấy tiếng vang của phát súng dội lại từ vách núi. Biết tốc độ truyền âm trong không khí là 340 m/s. Khoảng cách từ vị trí bắn súng đến vách núi là:",
        "options": [
          "272 m",
          "544 m",
          "170 m",
          "340 m"
        ],
        "correct": 0,
        "explanation": "Quãng đường âm đi và về: 2d = 340 × 1,6 = 544 m => d = 272 m."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người gõ búa vào đường ray xe lửa bằng thép. Một người khác ở cách đó 1700 m áp tai vào đường ray sắt. Biết tốc độ âm trong thép là 5100 m/s và trong không khí là 340 m/s. Người này nghe thấy tiếng gõ truyền qua đường ray thép sớm hơn tiếng gõ truyền qua không khí một khoảng thời gian là:",
        "options": [
          "4,67 giây",
          "5,00 giây",
          "0,33 giây",
          "4,00 giây"
        ],
        "correct": 0,
        "explanation": "t_khí = 1700 / 340 = 5,0 s. t_thép = 1700 / 5100 = 0,333 s => Chênh lệch: 5,0 - 0,333 ≈ 4,67 s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Trong một bộ phim khoa học viễn tưởng, một con tàu vũ trụ bị nổ tung ngoài không gian chân không kèm theo tiếng nổ vang dội làm rung chuyển một con tàu vũ trụ khác ở gần đó. Xét về mặt vật lý học, cảnh phim này có điểm nào không chính xác?",
        "options": [
          "Trong không gian chân không không có môi trường truyền âm nên người trên tàu vũ trụ bên cạnh hoàn toàn không thể nghe thấy tiếng nổ",
          "Tàu vũ trụ không thể nổ",
          "Không thể có ánh sáng",
          "Tàu vũ trụ chạy chậm"
        ],
        "correct": 0,
        "explanation": "Chân không không truyền được âm thanh, không thể nghe thấy tiếng nổ ngoài không gian."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một đoàn xe quân sự di chuyển trên đường đất. Người bảo vệ đứng cách đó 680 m áp tai xuống mặt đất nghe thấy tiếng rung của động cơ sau 0,4 giây. Tốc độ truyền âm thanh đo được trong nền đất cát ở khu vực này là:",
        "options": [
          "1700 m/s",
          "340 m/s",
          "1500 m/s",
          "850 m/s"
        ],
        "correct": 0,
        "explanation": "v = s / t = 680 / 0,4 = 1700 m/s."
      }
    ]
  },
  "phys7_c4_b13_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 13: Độ to và độ cao của âm - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b13",
    "lessonName": "Bài 13: Độ to và độ cao của âm",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số dao động mà một vật thực hiện được trong thời gian 1 giây được gọi là:",
        "options": [
          "Tần số dao động",
          "Biên độ dao động",
          "Độ to của âm",
          "Tốc độ âm"
        ],
        "correct": 0,
        "explanation": "Tần số dao động là số dao động trong 1 giây."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đơn vị đo của tần số dao động là:",
        "options": [
          "Hertz (Hz)",
          "Decibel (dB)",
          "Mét trên giây (m/s)",
          "Giây (s)"
        ],
        "correct": 0,
        "explanation": "Đơn vị đo tần số là Hertz, kí hiệu là Hz."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Độ cao của âm (âm bổng hay âm trầm) phụ thuộc vào đại lượng nào sau đây?",
        "options": [
          "Tần số dao động của nguồn âm",
          "Biên độ dao động của nguồn âm",
          "Khoảng cách từ nguồn đến tai",
          "Khối lượng nguồn âm"
        ],
        "correct": 0,
        "explanation": "Độ cao của âm gắn liền với tần số dao động."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Độ to của âm nghe được phụ thuộc trực tiếp vào đại lượng nào?",
        "options": [
          "Biên độ dao động của nguồn âm",
          "Tần số dao động của nguồn âm",
          "Hình dạng nguồn âm",
          "Vật liệu làm nguồn âm"
        ],
        "correct": 0,
        "explanation": "Biên độ dao động càng lớn thì âm phát ra nghe càng to."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Đơn vị thường dùng để đo mức độ to của âm (mức cường độ âm) là:",
        "options": [
          "Decibel (dB)",
          "Hertz (Hz)",
          "Mét (m)",
          "Kilôgam (kg)"
        ],
        "correct": 0,
        "explanation": "Độ to của âm được đo bằng đơn vị Decibel (dB)."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tai người bình thường có thể nghe được âm thanh trong dải tần số từ:",
        "options": [
          "16 Hz đến 20.000 Hz",
          "Dưới 16 Hz",
          "Trên 20.000 Hz",
          "100 Hz đến 1.000 Hz"
        ],
        "correct": 0,
        "explanation": "Dải tần số tai người cảm nhận được là 16 Hz - 20.000 Hz."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một vật trong thời gian 5 giây thực hiện được 200 dao động. Tần số dao động của vật là:",
        "options": [
          "40 Hz",
          "1000 Hz",
          "200 Hz",
          "50 Hz"
        ],
        "correct": 0,
        "explanation": "f = 200 / 5 = 40 Hz."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khi gảy một dây đàn guitar thật mạnh, ta nghe thấy âm thanh phát ra:",
        "options": [
          "To hơn vì biên độ dao động của dây đàn lớn hơn",
          "Bổng hơn",
          "Trầm hơn",
          "Không đổi"
        ],
        "correct": 0,
        "explanation": "Gảy mạnh làm dây đàn lệch nhiều hơn khỏi VTCB (biên độ lớn) => âm to hơn."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Âm thanh có tần số nhỏ hơn 16 Hz được gọi là:",
        "options": [
          "Hạ âm",
          "Siêu âm",
          "Tạp âm",
          "Âm bổng"
        ],
        "correct": 0,
        "explanation": "Dưới 16 Hz gọi là hạ âm."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Âm thanh có tần số lớn hơn 20.000 Hz được gọi là:",
        "options": [
          "Siêu âm",
          "Hạ âm",
          "Âm trầm",
          "Nhạc âm"
        ],
        "correct": 0,
        "explanation": "Trên 20.000 Hz gọi là siêu âm."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Để đàn phát ra âm bổng hơn, người nhạc công thường vặn khóa đàn để:",
        "options": [
          "Làm dây đàn căng hơn",
          "Làm dây đàn chùng hơn",
          "Làm dây đàn dài hơn",
          "Làm dây đàn nặng hơn"
        ],
        "correct": 0,
        "explanation": "Dây đàn căng hơn sẽ dao động nhanh hơn (tần số lớn hơn) => âm phát ra bổng hơn."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tiếng nói thầm thì có độ to khoảng bao nhiêu decibel (dB)?",
        "options": [
          "Khoảng 20 - 30 dB",
          "Khoảng 80 - 90 dB",
          "Khoảng 120 dB",
          "0 dB"
        ],
        "correct": 0,
        "explanation": "Tiếng thì thầm có mức cường độ âm khoảng 20 - 30 dB."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về mối quan hệ giữa dao động và đặc tính của âm thanh:",
        "statements": [
          {
            "subId": "a",
            "text": "Vật dao động càng nhanh (tần số càng lớn) thì âm phát ra càng bổng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Vật dao động càng chậm (tần số càng nhỏ) thì âm phát ra càng trầm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Độ lệch lớn nhất của vật dao động so với vị trí cân bằng gọi là biên độ dao động.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Biên độ dao động càng lớn thì âm phát ra càng bổng.",
            "correct": false
          }
        ],
        "explanation": "Biên độ dao động quyết định độ to của âm, không quyết định độ cao."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về khả năng cảm nhận âm thanh của con người và các loài động vật:",
        "statements": [
          {
            "subId": "a",
            "text": "Tai người không thể nghe được sóng hạ âm (tần số dưới 16 Hz).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tai người không thể nghe được sóng siêu âm (tần số trên 20.000 Hz).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Loài dơi và cá heo sử dụng sóng siêu âm để định vị săn mồi trong bóng tối.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Chó có thể nghe được các âm thanh siêu âm mà tai người không nghe thấy.",
            "correct": true
          }
        ],
        "explanation": "Các ý đều đúng với sinh học và vật lý âm thanh."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Xét hai chiếc lá thép 1 và 2 đàn hồi kẹp chặt một đầu trên mặt bàn:",
        "statements": [
          {
            "subId": "a",
            "text": "Lá thép 1 thực hiện 150 dao động trong 3 giây, tần số là 50 Hz.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Lá thép 2 thực hiện 360 dao động trong 6 giây, tần số là 60 Hz.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Âm do lá thép 1 phát ra nghe bổng hơn âm do lá thép 2 phát ra.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tai người hoàn toàn có thể nghe được âm thanh do cả hai lá thép phát ra.",
            "correct": true
          }
        ],
        "explanation": "f2 = 60 Hz > f1 = 50 Hz nên lá thép 2 phát ra âm bổng hơn lá thép 1."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khi chỉnh âm lượng của một chiếc loa nghe nhạc từ mức nhỏ lên mức to cực đại:",
        "statements": [
          {
            "subId": "a",
            "text": "Màng loa dao động với biên độ lớn hơn nhiều.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tần số dao động của nốt nhạc phát ra bị thay đổi thành nốt khác.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Âm thanh phát ra to hơn và truyền đi được xa hơn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu độ to vượt quá ngưỡng 130 dB có thể gây đau nhức màng nhĩ tai.",
            "correct": true
          }
        ],
        "explanation": "Tăng âm lượng chỉ làm tăng biên độ dao động, không làm thay đổi tần số (cao độ) của nốt nhạc."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một vật thực hiện 120 dao động trong 2 giây. Tần số dao động của vật là bao nhiêu Hz?",
        "correctAnswer": "60",
        "explanation": "f = 120 / 2 = 60 Hz."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Đơn vị đo độ to của âm có kí hiệu là gì?",
        "correctAnswer": "dB",
        "explanation": "Decibel, kí hiệu là dB."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Âm thanh có tần số 25.000 Hz thuộc vùng sóng nào? (Siêu âm hay Hạ âm)",
        "correctAnswer": "Siêu âm",
        "explanation": "f > 20.000 Hz là siêu âm."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một con muỗi đập cánh 1200 lần trong 2 giây. Tần số đập cánh của muỗi là bao nhiêu Hz?",
        "correctAnswer": "600",
        "explanation": "f = 1200 / 2 = 600 Hz."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một vật dao động với chu kì thực hiện 1 dao động mất 0,005 giây. Tần số dao động của vật là bao nhiêu Hz?",
        "correctAnswer": "200",
        "explanation": "f = 1 / 0,005 = 200 Hz."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Mức giới hạn độ to của âm thanh mà nếu kéo dài liên tục sẽ gây nguy hại cho thính giác của con người là bao nhiêu decibel (dB)?",
        "correctAnswer": "85",
        "explanation": "Tiếng ồn trên 85 dB kéo dài gây hại cho thính giác."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người gảy một sợi dây đàn guitar dài 60 cm phát ra nốt La chuẩn (tần số 440 Hz). Khi người này dùng ngón tay bấm chặt vào phím đàn chia đôi sợi dây đàn (chiều dài còn 30 cm) rồi gảy với cùng lực như trước thì âm phát ra sẽ thay đổi như thế nào?",
        "options": [
          "Âm phát ra bổng hơn gấp đôi (tần số tăng lên 880 Hz)",
          "Âm phát ra trầm hơn",
          "Âm phát ra to hơn gấp 4 lần",
          "Âm không đổi"
        ],
        "correct": 0,
        "explanation": "Chiều dài dây giảm một nửa thì tần số dao động tăng gấp đôi, âm bổng hơn."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Máy siêu âm dùng trong y khoa chẩn đoán hình ảnh ổ bụng hoặc theo dõi thai nhi thường phát sóng âm có tần số trong khoảng 2 MHz đến 10 MHz (1 MHz = 1.000.000 Hz). Phát biểu nào sau đây đúng về loại sóng này?",
        "options": [
          "Là sóng siêu âm có tần số rất cao, tai người hoàn toàn không nghe thấy và an toàn cho mô sống",
          "Là sóng hạ âm tai người nghe rõ",
          "Là tia phóng xạ nguy hiểm",
          "Là sóng ánh sáng nhìn thấy"
        ],
        "correct": 0,
        "explanation": "Sóng siêu âm y tế có tần số hàng triệu Hz, an toàn và tai người không nghe thấy."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho 3 vật dao động: Vật A thực hiện 80 dao động trong 4 giây; Vật B thực hiện 150 dao động trong 5 giây; Vật C thực hiện 180 dao động trong 3 giây. Sắp xếp các vật theo thứ tự phát ra âm từ trầm nhất đến bổng nhất:",
        "options": [
          "Vật A (20 Hz) < Vật B (30 Hz) < Vật C (60 Hz)",
          "Vật C < Vật B < Vật A",
          "Vật B < Vật A < Vật C",
          "Vật A < Vật C < Vật B"
        ],
        "correct": 0,
        "explanation": "fA = 80/4 = 20 Hz; fB = 150/5 = 30 Hz; fC = 180/3 = 60 Hz => Trầm nhất là A, bổng nhất là C."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Trong dàn nhạc giao hưởng, tiếng kèn tuba phát ra âm trầm sâu lắng (tần số khoảng 40 Hz), trong khi tiếng sáo piccolo phát ra âm rất cao và bổng (tần số khoảng 4000 Hz). So sánh số dao động của cột không khí trong hai nhạc cụ này trong thời gian 1 giây:",
        "options": [
          "Cột không khí trong sáo piccolo dao động nhiều gấp 100 lần so với trong kèn tuba",
          "Cột không khí trong kèn tuba dao động nhiều hơn",
          "Cả hai dao động bằng nhau",
          "Không thể so sánh"
        ],
        "correct": 0,
        "explanation": "Piccolo 4000 dao động/giây, Tuba 40 dao động/giây => Gấp: 4000 / 40 = 100 lần."
      }
    ]
  },
  "phys7_c4_b13_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 13: Độ to và độ cao của âm - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b13",
    "lessonName": "Bài 13: Độ to và độ cao của âm",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Âm phát ra càng bổng (càng cao) khi:",
        "options": [
          "Tần số dao động của nguồn âm càng lớn",
          "Tần số dao động càng nhỏ",
          "Biên độ dao động càng lớn",
          "Biên độ dao động càng nhỏ"
        ],
        "correct": 0,
        "explanation": "Tần số càng lớn âm phát ra càng bổng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Âm phát ra càng trầm (càng thấp) khi:",
        "options": [
          "Tần số dao động của nguồn âm càng nhỏ",
          "Tần số dao động càng lớn",
          "Vật dao động càng mạnh",
          "Vật đứng yên"
        ],
        "correct": 0,
        "explanation": "Tần số nhỏ làm âm trầm."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Độ lệch lớn nhất của vật dao động so với vị trí cân bằng được gọi là:",
        "options": [
          "Biên độ dao động",
          "Tần số dao động",
          "Độ cao của âm",
          "Vận tốc âm"
        ],
        "correct": 0,
        "explanation": "Biên độ là khoảng cách lệch lớn nhất so với VTCB."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Âm nghe được càng to khi:",
        "options": [
          "Biên độ dao động của nguồn âm càng lớn",
          "Biên độ dao động càng nhỏ",
          "Tần số dao động càng nhỏ",
          "Khoảng cách đến nguồn âm càng xa"
        ],
        "correct": 0,
        "explanation": "Biên độ lớn thì âm nghe to."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tiếng ồn của máy bay phản lực cất cánh ở cự li gần có thể đạt độ to khoảng:",
        "options": [
          "120 - 130 dB (ngưỡng đau nhức tai)",
          "40 dB",
          "60 dB",
          "10 dB"
        ],
        "correct": 0,
        "explanation": "Tiếng máy bay phản lực cất cánh đạt tới 120 - 130 dB."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hạ âm là âm thanh có tần số:",
        "options": [
          "Dưới 16 Hz",
          "Từ 16 Hz đến 20.000 Hz",
          "Trên 20.000 Hz",
          "Trên 1.000 Hz"
        ],
        "correct": 0,
        "explanation": "Hạ âm có tần số dưới 16 Hz."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một con lắc thực hiện 60 dao động trong thời gian 30 giây. Tần số dao động của con lắc là:",
        "options": [
          "2 Hz",
          "0,5 Hz",
          "1800 Hz",
          "30 Hz"
        ],
        "correct": 0,
        "explanation": "f = 60 / 30 = 2 Hz."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Âm thanh do con lắc ở câu trên phát ra có nghe được bằng tai người không?",
        "options": [
          "Không nghe được vì tần số 2 Hz nhỏ hơn 16 Hz (thuộc vùng hạ âm)",
          "Nghe được rất rõ",
          "Nghe thấy tiếng vo ve",
          "Nghe thấy tiếng rít"
        ],
        "correct": 0,
        "explanation": "2 Hz < 16 Hz là hạ âm, tai người không nghe được."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Khi nói to và nói thì thầm, đặc tính nào của âm thanh bị thay đổi chủ yếu?",
        "options": [
          "Độ to của âm thay đổi (do biên độ dao động của dây thanh quản thay đổi)",
          "Độ cao của âm",
          "Tốc độ truyền âm trong không khí",
          "Bản chất sóng âm"
        ],
        "correct": 0,
        "explanation": "Nói to làm biên độ dao động lớn hơn, độ to tăng lên."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Loài voi có thể giao tiếp với nhau qua khoảng cách hàng chục kilômét bằng loại sóng âm nào?",
        "options": [
          "Sóng hạ âm truyền qua mặt đất và không khí",
          "Sóng siêu âm",
          "Sóng radio",
          "Ánh sáng"
        ],
        "correct": 0,
        "explanation": "Voi phát ra hạ âm tần số dưới 16 Hz truyền rất xa."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi gõ nhẹ vào mặt trống rồi gõ mạnh hơn, đại lượng nào sau đây của âm phát ra thay đổi?",
        "options": [
          "Độ to của âm tăng lên",
          "Độ cao của âm tăng lên",
          "Tần số âm tăng lên",
          "Tốc độ âm tăng lên"
        ],
        "correct": 0,
        "explanation": "Gõ mạnh làm tăng biên độ dao động, âm to hơn."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Giọng nói của phụ nữ thường bổng hơn giọng nói của nam giới là do:",
        "options": [
          "Dây thanh quản của phụ nữ thường ngắn và mỏng hơn nên dao động với tần số cao hơn",
          "Dây thanh quản của phụ nữ dày hơn",
          "Phụ nữ nói to hơn",
          "Dây thanh quản của nam giới dao động nhanh hơn"
        ],
        "correct": 0,
        "explanation": "Dây thanh quản ngắn và mảnh dao động nhanh hơn => giọng bổng hơn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các đặc trưng sinh lý và vật lý của âm thanh:",
        "statements": [
          {
            "subId": "a",
            "text": "Độ cao của âm gắn liền với tần số dao động.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Độ to của âm gắn liền với biên độ dao động.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Âm có tần số 1000 Hz nghe trầm hơn âm có tần số 200 Hz.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khi lại gần nguồn âm, ta nghe thấy âm to hơn so với khi ở xa.",
            "correct": true
          }
        ],
        "explanation": "1000 Hz bổng hơn nhiều so với 200 Hz."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về sóng siêu âm và các ứng dụng khoa học công nghệ:",
        "statements": [
          {
            "subId": "a",
            "text": "Sóng siêu âm có tần số vượt quá 20.000 Hz.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Máy rửa siêu âm dùng rung động siêu âm tần số cao để làm sạch trang sức và linh kiện đồng hồ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dơi phát sóng siêu âm và thu tiếng vang dội lại để tránh chướng ngại vật khi bay đêm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tai người có thể nghe được tiếng dơi phát ra khi bay săn mồi.",
            "correct": false
          }
        ],
        "explanation": "Dơi phát siêu âm tai người hoàn toàn không nghe thấy."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một lá thép kẹp chặt trên ê tô có chiều dài phần tự do thay đổi được:",
        "statements": [
          {
            "subId": "a",
            "text": "Khi để phần tự do dài 20 cm, gảy nhẹ lá thép dao động chậm, phát ra âm trầm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi rút ngắn phần tự do còn 10 cm, gảy nhẹ lá thép dao động nhanh hơn, phát ra âm bổng hơn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chiều dài tự do của lá thép càng ngắn thì tần số dao động càng lớn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu gảy thật mạnh ở cả hai trường hợp thì âm phát ra đều có độ to bằng nhau tuyệt đối.",
            "correct": false
          }
        ],
        "explanation": "Độ to phụ thuộc vào biên độ gảy mạnh hay nhẹ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Xét tiếng ve kêu râm ran vào mùa hè trên các cành cây:",
        "statements": [
          {
            "subId": "a",
            "text": "Ve sầu đực phát ra âm thanh nhờ các màng phát âm đặc biệt ở dưới bụng rung động cực nhanh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tần số dao động của màng phát âm ve sầu có thể đạt vài nghìn Hertz nên tiếng ve kêu rất chói tai.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Độ to tiếng ve kêu vào buổi trưa hè có thể đạt tới 70 - 80 dB.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Âm thanh của ve sầu là sóng hạ âm nên người điếc cũng nghe được.",
            "correct": false
          }
        ],
        "explanation": "Tiếng ve sầu thuộc dải âm nghe được có tần số cao, không phải hạ âm."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một vật thực hiện được 50 dao động trong 1 giây. Tần số dao động là bao nhiêu Hz?",
        "correctAnswer": "50",
        "explanation": "50 Hz."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Âm thanh có tần số 10 Hz thuộc vùng sóng nào? (Hạ âm hay Siêu âm)",
        "correctAnswer": "Hạ âm",
        "explanation": "f < 16 Hz là hạ âm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Con ong mật khi bay đập cánh 440 lần trong 1 giây. Tần số dao động của cánh ong là bao nhiêu Hz?",
        "correctAnswer": "440",
        "explanation": "440 Hz."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thanh kim loại dao động với tần số 100 Hz. Trong 5 giây thanh kim loại thực hiện được bao nhiêu dao động?",
        "correctAnswer": "500",
        "explanation": "N = f × t = 100 × 5 = 500 dao động."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Độ to của tiếng nói chuyện bình thường giữa hai người ở khoảng cách 1 mét vào khoảng bao nhiêu decibel (dB)?",
        "correctAnswer": "60",
        "explanation": "Khoảng 50 - 60 dB."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một vật dao động thực hiện 1500 dao động trong 3 giây. Tần số dao động là bao nhiêu Hz?",
        "correctAnswer": "500",
        "explanation": "f = 1500 / 3 = 500 Hz."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một âm thoa được chế tạo để phát ra nốt La chuẩn có tần số 440 Hz. Trong thời gian một buổi biểu diễn hòa nhạc kéo dài 15 giây độc tấu, nhánh âm thoa đã thực hiện được tổng cộng bao nhiêu dao động?",
        "options": [
          "6600 dao động",
          "440 dao động",
          "1500 dao động",
          "8800 dao động"
        ],
        "correct": 0,
        "explanation": "N = f × t = 440 × 15 = 6600 dao động."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Người ta dùng một chiếc máy đo tần số ghi nhận âm thanh phát ra từ tiếng đập cánh của ba loài côn trùng: Muỗi đực (600 Hz); Ong bắp cày (250 Hz); Ruồi nhà (350 Hz). Âm thanh phát ra từ tiếng vỗ cánh của loài nào nghe bổng nhất và loài nào trầm nhất?",
        "options": [
          "Muỗi đực bổng nhất, ong bắp cày trầm nhất",
          "Ruồi nhà bổng nhất, muỗi đực trầm nhất",
          "Ong bắp cày bổng nhất, muỗi đực trầm nhất",
          "Ba loài phát âm như nhau"
        ],
        "correct": 0,
        "explanation": "Tần số cao nhất (600 Hz - muỗi) nghe bổng nhất; tần số thấp nhất (250 Hz - ong) nghe trầm nhất."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một ca sĩ opera khi hát một nốt cao có thể làm rung và vỡ một chiếc ly thủy tinh mỏng đặt ở gần. Hiện tượng này xảy ra là do:",
        "options": [
          "Tần số âm thanh của giọng hát trùng với tần số dao động riêng của chiếc ly gây ra hiện tượng cộng hưởng cơ học làm biên độ dao động của ly tăng cực đại",
          "Giọng ca sĩ quá nóng làm chảy ly",
          "Sóng âm làm nứt sàn nhà",
          "Gió từ miệng ca sĩ thổi vỡ ly"
        ],
        "correct": 0,
        "explanation": "Cộng hưởng âm học làm biên độ dao động của ly thủy tinh tăng vọt vượt giới hạn đàn hồi gây vỡ ly."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Khi gõ nhẹ vào miệng một chiếc chai thủy tinh rỗng, âm thanh phát ra có độ cao nhất định. Nếu đổ thêm nước vào nửa chai rồi gõ nhẹ vào miệng chai thì âm phát ra sẽ thay đổi như thế nào?",
        "options": [
          "Âm phát ra trầm hơn vì khối lượng nước và chai tăng lên làm tần số dao động của thành chai giảm đi",
          "Âm phát ra bổng hơn",
          "Âm không đổi",
          "Không nghe thấy âm nữa"
        ],
        "correct": 0,
        "explanation": "Khi gõ vào thành chai, thêm nước làm tăng quán tính của hệ dao động khiến thành chai dao động chậm lại, âm trầm hơn."
      }
    ]
  },
  "phys7_c4_b13_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 13: Độ to và độ cao của âm - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b13",
    "lessonName": "Bài 13: Độ to và độ cao của âm",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đại lượng nào sau đây đo bằng đơn vị Hertz (Hz)?",
        "options": [
          "Tần số dao động",
          "Biên độ dao động",
          "Độ to của âm",
          "Tốc độ âm"
        ],
        "correct": 0,
        "explanation": "Tần số dao động đo bằng Hertz (Hz)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Dao động càng nhanh thì tần số dao động:",
        "options": [
          "Càng lớn",
          "Càng nhỏ",
          "Bằng 0",
          "Không đổi"
        ],
        "correct": 0,
        "explanation": "Dao động nhanh nghĩa là thực hiện nhiều dao động trong 1 giây => tần số lớn."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Biên độ dao động của nguồn âm là:",
        "options": [
          "Độ lệch lớn nhất của vật khỏi vị trí cân bằng",
          "Khoảng cách vật đi trong 1 giây",
          "Số dao động trong 1 giây",
          "Độ dài của vật"
        ],
        "correct": 0,
        "explanation": "Biên độ là khoảng cách lệch cực đại so với vị trí cân bằng."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi dùng dùi gõ nhẹ vào mặt trống, màng trống dao động với biên độ nhỏ thì âm phát ra:",
        "options": [
          "Nghe nhỏ",
          "Nghe to",
          "Nghe bổng",
          "Nghe trầm"
        ],
        "correct": 0,
        "explanation": "Biên độ nhỏ thì âm nghe nhỏ."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Ngưỡng đau nhức màng nhĩ tai của con người bắt đầu từ độ to khoảng:",
        "options": [
          "130 dB",
          "60 dB",
          "80 dB",
          "20 dB"
        ],
        "correct": 0,
        "explanation": "Ngưỡng đau tai là 130 dB."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Dải tần số sóng siêu âm là dải tần số:",
        "options": [
          "Lớn hơn 20.000 Hz",
          "Nhỏ hơn 16 Hz",
          "Từ 16 Hz đến 20.000 Hz",
          "Từ 0 đến 100 Hz"
        ],
        "correct": 0,
        "explanation": "Siêu âm có tần số trên 20.000 Hz."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một quả lắc đồng hồ trong 1 phút thực hiện được 60 dao động. Tần số dao động của quả lắc là:",
        "options": [
          "1 Hz",
          "60 Hz",
          "3600 Hz",
          "0,5 Hz"
        ],
        "correct": 0,
        "explanation": "1 phút = 60 s => f = 60 / 60 = 1 Hz."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tại sao tai người không thể nghe được âm do quả lắc đồng hồ ở câu trên phát ra?",
        "options": [
          "Vì tần số 1 Hz thuộc vùng hạ âm dưới 16 Hz",
          "Vì quả lắc không dao động",
          "Vì quả lắc bị cách âm",
          "Vì quả lắc phát ra siêu âm"
        ],
        "correct": 0,
        "explanation": "1 Hz < 16 Hz nên tai người không nghe được."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một người gảy dây đàn số 1 (dây mảnh) và dây số 6 (dây dày) của cùng một cây đàn guitar. Dây nào phát ra âm bổng hơn?",
        "options": [
          "Dây số 1 (dây mảnh) phát ra âm bổng hơn",
          "Dây số 6 phát ra âm bổng hơn",
          "Hai dây phát ra âm bổng như nhau",
          "Không xác định được"
        ],
        "correct": 0,
        "explanation": "Dây mảnh dao động nhanh hơn (tần số lớn hơn) nên phát ra âm bổng hơn."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Một chiếc còi siêu âm dành cho việc huấn luyện chó cảnh: người thổi không nghe thấy tiếng còi nhưng chú chó lập tức chạy lại. Giải thích nào đúng?",
        "options": [
          "Còi phát ra sóng siêu âm có tần số trên 20.000 Hz, tai chó nghe được còn tai người không nghe được",
          "Chó nhìn thấy hơi thở người thổi",
          "Còi không phát ra âm gì",
          "Chó ngửi thấy mùi còi"
        ],
        "correct": 0,
        "explanation": "Chó có thính giác cảm nhận được siêu âm tới 40.000 - 50.000 Hz."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Để tăng độ to của tiếng kèn trumpet, người thổi kèn cần:",
        "options": [
          "Thổi một luồng hơi mạnh hơn vào kèn làm cột không khí dao động với biên độ lớn hơn",
          "Bấm phím kèn nhanh hơn",
          "Cắt ngắn ống kèn",
          "Bịt miệng kèn"
        ],
        "correct": 0,
        "explanation": "Thổi hơi mạnh làm tăng biên độ dao động, âm phát ra to hơn."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Âm thanh của tiếng thì thầm trong thư viện có độ to khoảng 30 dB, trong khi tiếng nói chuyện bình thường khoảng 60 dB. Âm thanh nói chuyện bình thường có năng lượng:",
        "options": [
          "Lớn hơn nhiều so với tiếng thì thầm",
          "Nhỏ hơn tiếng thì thầm",
          "Bằng tiếng thì thầm",
          "Bằng 0"
        ],
        "correct": 0,
        "explanation": "Mức dB càng lớn thì biên độ và năng lượng âm càng lớn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các đặc tính âm thanh và cảm nhận của tai người:",
        "statements": [
          {
            "subId": "a",
            "text": "Tần số dao động quyết định độ cao của âm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Biên độ dao động quyết định độ to của âm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tần số âm càng lớn thì âm nghe càng to.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Hai âm có cùng độ cao vẫn có thể phân biệt được nếu do hai nhạc cụ khác nhau phát ra.",
            "correct": true
          }
        ],
        "explanation": "Tần số lớn làm âm bổng, không phải làm âm to. Âm sắc giúp phân biệt các nhạc cụ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về hạ âm và các hiện tượng tự nhiên:",
        "statements": [
          {
            "subId": "a",
            "text": "Các cơn địa chấn động đất và sóng thần thường phát ra các đợt sóng hạ âm rất mạnh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Một số loài động vật như chim, voi cảm nhận được hạ âm nên có phản xạ tháo chạy trước khi động đất xảy ra.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sóng hạ âm hoàn toàn không thể truyền qua lớp đất đá của Trái Đất.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Con người sử dụng các máy đo địa chấn thu sóng hạ âm để cảnh báo sớm động đất.",
            "correct": true
          }
        ],
        "explanation": "Hạ âm truyền cực kì tốt qua đất đá và nước biển trên cự li hàng nghìn kilômét."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Học sinh sử dụng phần mềm đo tần số trên điện thoại thông minh để phân tích âm thanh giọng nói:",
        "statements": [
          {
            "subId": "a",
            "text": "Giọng của bạn nam ghi nhận tần số cơ bản khoảng 120 Hz.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Giọng của bạn nữ ghi nhận tần số cơ bản khoảng 240 Hz.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Giọng của bạn nữ có tần số cao hơn nên nghe bổng hơn giọng bạn nam.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Giọng bạn nào nghe to hơn chứng tỏ bạn đó có tần số giọng nói lớn hơn.",
            "correct": false
          }
        ],
        "explanation": "Nghe to hơn là do biên độ dao động lớn hơn, không phải do tần số lớn hơn."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khi điều chỉnh dây đàn vĩ cầm (violin):",
        "statements": [
          {
            "subId": "a",
            "text": "Vặn khóa căng dây đàn làm tăng độ cao của nốt nhạc.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dùng ngón tay bấm trên phím đàn làm giảm chiều dài đoạn dây tự do rung động, âm phát ra bổng hơn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kéo vĩ đàn mạnh hơn làm âm phát ra to hơn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Kéo vĩ đàn thật mạnh sẽ làm biến đổi nốt Đồ thành nốt Rê.",
            "correct": false
          }
        ],
        "explanation": "Kéo mạnh chỉ làm tăng độ to của nốt nhạc, không làm đổi cao độ của nốt nhạc."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Số dao động thực hiện trong 1 giây được gọi là gì?",
        "correctAnswer": "Tần số",
        "explanation": "Tần số dao động."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Âm có tần số 30.000 Hz là hạ âm hay siêu âm?",
        "correctAnswer": "Siêu âm",
        "explanation": "f > 20.000 Hz là siêu âm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một lá thép thực hiện 300 dao động trong 6 giây. Tần số dao động là bao nhiêu Hz?",
        "correctAnswer": "50",
        "explanation": "f = 300 / 6 = 50 Hz."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cánh của chim ruồi đập 1400 lần trong 20 giây. Tần số đập cánh của chim ruồi là bao nhiêu Hz?",
        "correctAnswer": "70",
        "explanation": "f = 1400 / 20 = 70 Hz."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một vật dao động với tần số 250 Hz. Trong thời gian 4 giây, vật thực hiện được bao nhiêu dao động?",
        "correctAnswer": "1000",
        "explanation": "N = 250 × 4 = 1000 dao động."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Độ to của tiếng động cơ xe máy đang chạy trên đường phố vào khoảng bao nhiêu decibel (dB)?",
        "correctAnswer": "80",
        "explanation": "Khoảng 75 - 80 dB."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một âm thoa dao động với tần số 256 Hz (nốt Đồ chuẩn). Người ta gõ vào âm thoa rồi đưa lại gần miệng một ống nghiệm chứa nước. Khi điều chỉnh mực nước trong ống nghiệm đến độ cao thích hợp, người ta nghe thấy âm thanh phát ra to bất thường. Hiện tượng này được giải thích là do:",
        "options": [
          "Hiện tượng cộng hưởng âm thanh khi tần số dao động của cột không khí trong ống nghiệm bằng đúng 256 Hz",
          "Nước phản chiếu ánh sáng",
          "Nước sôi bốc hơi",
          "Ống nghiệm bị vỡ"
        ],
        "correct": 0,
        "explanation": "Cộng hưởng âm học làm tăng biên độ dao động của cột không khí trong ống nghiệm, âm phát ra cực to."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Để đo tốc độ di chuyển của dòng máu trong động mạch, các bác sĩ sử dụng thiết bị 'Siêu âm Doppler'. Thiết bị này hoạt động dựa trên nguyên lí:",
        "options": [
          "Sóng siêu âm phản xạ từ các tế bào hồng cầu đang chuyển động có tần số bị thay đổi so với tần số phát ban đầu",
          "Sóng hạ âm làm đông máu",
          "Tia X làm nóng mạch máu",
          "Ánh sáng đổi màu máu"
        ],
        "correct": 0,
        "explanation": "Hiệu ứng Doppler: tần số sóng siêu âm phản xạ thay đổi tỉ lệ với tốc độ chuyển động của dòng hồng cầu."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một sợi dây đàn guitar có chiều dài 64 cm khi dao động phát ra âm có tần số 330 Hz (nốt Mi). Để phát ra âm có tần số 660 Hz (cao hơn một quãng tám), người chơi đàn cần bấm phím đàn để chiều dài đoạn dây tự do dao động còn lại bao nhiêu cm?",
        "options": [
          "32 cm",
          "16 cm",
          "48 cm",
          "20 cm"
        ],
        "correct": 0,
        "explanation": "Tần số tỉ lệ nghịch với chiều dài dây đàn: tần số tăng gấp đôi thì chiều dài dây phải giảm một nửa: 64 / 2 = 32 cm."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người gõ búa vào một thanh thép mỏng gắn trên bàn cân điện tử có gắn cảm biến rung. Thiết bị ghi nhận được đồ thị dao động hình sin có biên độ 2 mm và tần số 100 Hz. Nếu người đó gõ mạnh gấp đôi nhưng giữ nguyên vị trí kẹp thanh thép thì thông số nào của đồ thị dao động sẽ tăng lên?",
        "options": [
          "Biên độ dao động tăng lên (lớn hơn 2 mm) trong khi tần số vẫn giữ nguyên 100 Hz",
          "Tần số tăng lên 200 Hz",
          "Cả biên độ và tần số đều tăng gấp đôi",
          "Đồ thị biến thành đường thẳng"
        ],
        "correct": 0,
        "explanation": "Gõ mạnh làm tăng biên độ dao động; tần số dao động riêng của thanh thép không đổi."
      }
    ]
  },
  "phys7_c4_b14_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b14",
    "lessonName": "Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hiện tượng sóng âm khi gặp một mặt chắn bị dội ngược trở lại môi trường cũ được gọi là:",
        "options": [
          "Sự phản xạ âm",
          "Sự khúc xạ âm",
          "Sự nhiễu xạ âm",
          "Sự truyền thẳng của âm"
        ],
        "correct": 0,
        "explanation": "Sóng âm bị dội lại khi gặp mặt chắn gọi là phản xạ âm."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Âm phản xạ nghe được cách âm trực tiếp một khoảng thời gian ít nhất là bao lâu thì được gọi là tiếng vang?",
        "options": [
          "1/15 giây",
          "1/2 giây",
          "1 giây",
          "1/60 giây"
        ],
        "correct": 0,
        "explanation": "Tiếng vang là âm phản xạ nghe cách âm trực tiếp ít nhất 1/15 giây."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Vật nào sau đây phản xạ âm tốt (hấp thụ âm kém)?",
        "options": [
          "Tấm kính phẳng, nhẵn bóng",
          "Tấm mút xốp",
          "Rèm vải nhung",
          "Tấm đệm cao su"
        ],
        "correct": 0,
        "explanation": "Vật cứng có bề mặt nhẵn bóng phản xạ âm tốt."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Vật liệu nào sau đây là vật liệu hấp thụ âm tốt (tiêu âm) thường dùng để cách âm phòng hát?",
        "options": [
          "Mút xốp bọt biển, dạ, rèm nhung",
          "Tấm kim loại phẳng nhẵn",
          "Mặt gương kính",
          "Tường bê tông mài bóng"
        ],
        "correct": 0,
        "explanation": "Vật liệu mềm xốp, bề mặt gồ ghề hấp thụ âm tốt."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tiếng ồn gây ô nhiễm là tiếng ồn:",
        "options": [
          "To, kéo dài ảnh hưởng tiêu cực đến sức khỏe, sinh hoạt và làm việc của con người",
          "Nhỏ thì thầm",
          "Êm dịu du dương",
          "Chỉ xuất hiện vào ban ngày trong 1 giây"
        ],
        "correct": 0,
        "explanation": "Ô nhiễm tiếng ồn là tiếng ồn lớn kéo dài ảnh hưởng xấu đến đời sống và sức khỏe."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Biện pháp nào sau đây giúp phân tán âm thanh trên đường truyền?",
        "options": [
          "Trồng nhiều dải cây xanh có tán lá rộng ven đường",
          "Đóng kín cửa sổ",
          "Đeo nút bịt tai",
          "Tắt máy xe"
        ],
        "correct": 0,
        "explanation": "Cây xanh có tán lá rậm rạp làm tán xạ và hấp thụ âm thanh trên đường truyền."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Để nghe được tiếng vang của giọng nói trong không khí (v = 340 m/s), khoảng cách ngắn nhất từ người nói đến bức tường phản xạ phải là:",
        "options": [
          "Khoảng 11,3 mét",
          "Khoảng 5,0 mét",
          "Khoảng 20,0 mét",
          "Khoảng 34,0 mét"
        ],
        "correct": 0,
        "explanation": "d_min = v × t / 2 = 340 × (1/15) / 2 ≈ 11,33 m."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tại sao khi nói chuyện trong một căn phòng rộng trống không có đồ đạc, ta lại nghe thấy tiếng vang hoặc âm bị nhòe?",
        "options": [
          "Vì âm thanh phản xạ nhiều lần từ các bức tường nhẵn gồ ghề tới tai gần như cùng lúc",
          "Vì phòng quá tối",
          "Vì không khí trong phòng đứng yên",
          "Vì trần nhà quá thấp"
        ],
        "correct": 0,
        "explanation": "Phòng trống có tường cứng nhẵn phản xạ âm tốt, âm phản xạ dội lại làm nhòe tiếng."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Biện pháp nào sau đây tác động trực tiếp nhằm giảm độ to tại nguồn âm?",
        "options": [
          "Cấm bóp còi xe hơi gần bệnh viện và trường học",
          "Đeo nút bịt tai khi ngủ",
          "Trồng cây xanh ven đường",
          "Lắp cửa kính 2 lớp"
        ],
        "correct": 0,
        "explanation": "Cấm bấm còi là biện pháp can thiệp trực tiếp tại nguồn phát âm."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Loài dơi bay săn mồi trong đêm tối mà không bị va vào các nhánh cây hay bức tường là nhờ:",
        "options": [
          "Phát ra sóng siêu âm và thu nhận tín hiệu âm phản xạ từ chướng ngại vật (định vị bằng tiếng vang)",
          "Mắt dơi sáng như đèn pha",
          "Dơi ngửi thấy chướng ngại vật",
          "Dơi bay rất chậm"
        ],
        "correct": 0,
        "explanation": "Dơi sử dụng cơ chế định vị bằng tiếng vang sóng siêu âm (echolocation)."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Trong các rạp chiếu phim hiện đại, tường và trần nhà thường được thiết kế uốn lượn và ốp các tấm thạch cao đục lỗ nhằm:",
        "options": [
          "Hấp thụ và triệt tiêu âm phản xạ, tránh hiện tượng tiếng vang giúp âm thanh trung thực",
          "Để tường không bị nứt vỡ",
          "Để phòng chiếu ấm hơn",
          "Để trang trí mỹ thuật"
        ],
        "correct": 0,
        "explanation": "Tiêu âm và triệt tiêu tiếng vang giúp chất lượng âm thanh trong rạp chuẩn xác."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Trường hợp nào sau đây là biểu hiện của ô nhiễm tiếng ồn?",
        "options": [
          "Nhà ở cạnh xưởng cơ khí cưa sắt, gò hàn kim loại hoạt động ầm ĩ suốt ngày đêm",
          "Tiếng lá cây rơi xào xạc trong vườn",
          "Tiếng đồng hồ tích tắc trong đêm",
          "Tiếng suối chảy róc rách xa xa"
        ],
        "correct": 0,
        "explanation": "Tiếng xưởng cưa gò sắt kéo dài liên tục gây ô nhiễm tiếng ồn nghiêm trọng."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về tính chất phản xạ của sóng âm trên các bề mặt vật liệu:",
        "statements": [
          {
            "subId": "a",
            "text": "Bề mặt phẳng nhẵn và cứng phản xạ âm rất tốt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bề mặt gồ ghề, xốp mềm hấp thụ âm tốt và phản xạ âm kém.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tấm gương kính phản xạ âm kém hơn tấm rèm nhung.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Các vật liệu tiêu âm thường được dùng để lót sàn và ốp tường phòng thu âm.",
            "correct": true
          }
        ],
        "explanation": "Gương kính phẳng nhẵn phản xạ âm tốt hơn nhiều so với rèm nhung xốp mềm."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về hiện tượng tiếng vang trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Tiếng vang là âm phản xạ nghe được tách biệt hẳn với âm trực tiếp.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đứng trước một vách đá lớn hét to, ta có thể nghe thấy tiếng vang dội lại.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trong mọi căn phòng dù lớn hay nhỏ, ta đều luôn nghe thấy tiếng vang rõ ràng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tiếng sấm rền kéo dài trong cơn mưa giông là do âm phản xạ nhiều lần giữa các đám mây và mặt đất.",
            "correct": true
          }
        ],
        "explanation": "Phòng nhỏ có khoảng cách ngắn (d < 11,3 m) thì âm phản xạ hòa lẫn vào âm trực tiếp, không nghe thành tiếng vang riêng."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một người đứng trong một hang động đá vôi lớn cách vách hang 34 m và vỗ tay một cái thật mạnh:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc độ âm trong không khí trong hang là 340 m/s.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian âm thanh đi từ người đến vách hang rồi dội ngược trở lại tai là 0,2 giây.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Vì 0,2 giây lớn hơn 1/15 giây (khoảng 0,067 s) nên người đó nghe thấy tiếng vang rất rõ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu người đó tiến lại gần vách hang cách 5 m thì vẫn nghe thấy tiếng vang tách rời.",
            "correct": false
          }
        ],
        "explanation": "Ở cự li 5 m, t = 10 / 340 ≈ 0,029 s < 1/15 s nên không nghe thấy tiếng vang tách rời."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Các giải pháp chống ô nhiễm tiếng ồn cho khu dân cư cạnh trục đường giao thông lớn:",
        "statements": [
          {
            "subId": "a",
            "text": "Xây dựng các bức tường chắn cách âm bằng vật liệu tiêu âm cao dọc hai bên đường cao tốc.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trồng nhiều cây xanh có tán lá rậm rạp giữa dải phân cách và hành lang đường bộ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khuyến khích các hộ gia đình lắp đặt hệ thống cửa kính cách âm hai lớp chân không.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Cho phép các phương tiện bấm còi hơi công suất lớn để giải tỏa ách tắc giao thông.",
            "correct": false
          }
        ],
        "explanation": "Bấm còi hơi gây ô nhiễm tiếng ồn nghiêm trọng hơn, bị nghiêm cấm."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Âm phản xạ nghe được cách âm trực tiếp ít nhất bao nhiêu giây thì tạo thành tiếng vang? (Viết dưới dạng phân số tối giản)",
        "correctAnswer": "1/15",
        "explanation": "1/15 giây."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Mút xốp là vật liệu phản xạ âm tốt hay kém?",
        "correctAnswer": "Kém",
        "explanation": "Mút xốp hấp thụ âm tốt, phản xạ âm kém."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khoảng cách tối thiểu từ người đến vách phản xạ để nghe được tiếng vang trong không khí (v = 340 m/s) là bao nhiêu mét? (Làm tròn 1 chữ số thập phân)",
        "correctAnswer": "11.3",
        "explanation": "d_min = 340 × (1/15) / 2 ≈ 11,33 m ≈ 11,3 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người đứng trước một tòa nhà cao tầng hét to và nghe thấy âm dội lại sau 0,4 giây. Biết v = 340 m/s. Tòa nhà cách người đó bao nhiêu mét?",
        "correctAnswer": "68",
        "explanation": "d = 340 × 0,4 / 2 = 68 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Máy định vị bằng sóng siêu âm sonar của tàu tuần tra phát xung âm xuống rạn san hô dưới biển và nhận lại tín hiệu sau 0,6 giây. Biết v_nước = 1500 m/s. Độ sâu của rạn san hô là bao nhiêu mét?",
        "correctAnswer": "450",
        "explanation": "d = 1500 × 0,6 / 2 = 450 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Tiếng ồn kéo dài vượt quá bao nhiêu decibel (dB) được coi là ngưỡng gây ô nhiễm tiếng ồn có hại cho thính giác?",
        "correctAnswer": "85",
        "explanation": "Trên 85 dB."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước một vách núi đá hoa cương cao vút. Người đó dùng súng phát lệnh bắn một phát lên trời và dùng đồng hồ đo được thời gian từ lúc nổ súng đến khi nghe thấy tiếng vang dội lại từ vách núi là 1,4 giây. Biết tốc độ truyền âm trong không khí là 340 m/s. Khoảng cách từ vị trí người đó đứng đến vách núi là:",
        "options": [
          "238 m",
          "476 m",
          "170 m",
          "340 m"
        ],
        "correct": 0,
        "explanation": "Quãng đường âm đi và về: 2d = 340 × 1,4 = 476 m => d = 238 m."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một căn phòng học có chiều dài 8 mét, chiều rộng 6 mét, tường quét vôi phẳng nhẵn. Khi một học sinh nói to trong phòng, học sinh đó có nghe thấy tiếng vang của chính giọng nói mình không? Vì sao?",
        "options": [
          "Không nghe thấy tiếng vang vì khoảng cách từ học sinh đến tường lớn nhất chỉ khoảng 8 m, nhỏ hơn khoảng cách tối thiểu 11,3 m để tạo tiếng vang",
          "Có nghe thấy tiếng vang rất to",
          "Nghe thấy tiếng vang sau 1 giây",
          "Nghe thấy tiếng vang liên tục"
        ],
        "correct": 0,
        "explanation": "Khoảng cách trong phòng học (≤ 8 m) nhỏ hơn cự li tối thiểu 11,3 m nên âm phản xạ đến tai sớm hơn 1/15 s, hòa vào âm trực tiếp làm âm to hơn chứ không tạo tiếng vang riêng."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tại các bệnh viện và trường học, người ta thường cắm biển báo giao thông cấm bấm còi (biển P.128 có hình chiếc còi bị gạch chéo đỏ). Biện pháp chống ô nhiễm tiếng ồn này thuộc nhóm biện pháp nào?",
        "options": [
          "Tác động trực tiếp làm giảm độ to tại nguồn phát âm",
          "Ngăn chặn trên đường truyền âm",
          "Phân tán âm thanh",
          "Bảo vệ tai người nghe"
        ],
        "correct": 0,
        "explanation": "Cấm bấm còi là biện pháp triệt tiêu tiếng ồn ngay tại nguồn âm."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người đứng giữa hai bức tường thẳng đứng song song A và B trong một hội trường lớn. Bức tường A cách người đó 17 m, bức tường B cách người đó 51 m. Người đó vỗ tay một cái dứt khoát. Biết tốc độ âm trong không khí là 340 m/s. Người đó sẽ lần lượt nghe thấy hai tiếng vang dội lại từ hai bức tường sau các khoảng thời gian là:",
        "options": [
          "0,10 giây và 0,30 giây",
          "0,05 giây và 0,15 giây",
          "0,20 giây và 0,60 giây",
          "0,15 giây và 0,45 giây"
        ],
        "correct": 0,
        "explanation": "t_A = 2 × 17 / 340 = 0,10 s; t_B = 2 × 51 / 340 = 0,30 s."
      }
    ]
  },
  "phys7_c4_b14_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b14",
    "lessonName": "Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Âm phản xạ là:",
        "options": [
          "Âm dội ngược trở lại khi gặp một mặt chắn",
          "Âm phát ra từ nguồn âm ban đầu",
          "Âm truyền thẳng qua chướng ngại vật",
          "Âm bị tắt hẳn trong môi trường"
        ],
        "correct": 0,
        "explanation": "Âm dội lại khi gặp mặt chắn gọi là âm phản xạ."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khi nào thì tai ta nghe được tiếng vang?",
        "options": [
          "Khi âm phản xạ đến tai cách âm trực tiếp ít nhất 1/15 giây",
          "Khi âm phản xạ đến cùng lúc với âm trực tiếp",
          "Khi âm trực tiếp lớn hơn 100 dB",
          "Khi ở trong phòng kín nhỏ"
        ],
        "correct": 0,
        "explanation": "Tiếng vang xuất hiện khi khoảng cách thời gian giữa âm trực tiếp và âm phản xạ từ 1/15 s trở lên."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Vật liệu nào sau đây phản xạ âm kém nhất (hấp thụ âm tốt nhất)?",
        "options": [
          "Tấm xốp cách âm",
          "Tấm tôn sắt phẳng",
          "Bức tường gạch trát vữa nhẵn",
          "Tấm đá hoa cương"
        ],
        "correct": 0,
        "explanation": "Xốp mềm có nhiều lỗ khí li ti hấp thụ âm tốt nhất."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong các biện pháp sau, biện pháp nào ngăn chặn sự truyền âm vào phòng ngủ?",
        "options": [
          "Lắp cửa kính hai lớp cách âm và kéo rèm cửa bằng vải nhung dày",
          "Mở toang tất cả các cửa sổ",
          "Bật quạt chạy hết công suất",
          "Bật loa đài to"
        ],
        "correct": 0,
        "explanation": "Cửa kính hộp hai lớp và rèm nhung dày ngăn chặn hiệu quả âm thanh truyền vào phòng."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tác hại của ô nhiễm tiếng ồn kéo dài đối với sức khỏe con người là:",
        "options": [
          "Gây căng thẳng thần kinh, mất ngủ, giảm khả năng tập trung và suy giảm thính lực",
          "Làm tăng chiều cao",
          "Làm sáng mắt",
          "Làm tim đập chậm lại vĩnh viễn"
        ],
        "correct": 0,
        "explanation": "Tiếng ồn kéo dài gây hại cho thần kinh, tim mạch và thính giác."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Thiết bị bảo vệ cá nhân nào thường được công nhân làm việc ở công trường máy khoan hoặc sân bay sử dụng?",
        "options": [
          "Chụp tai chống ồn (chụp tai giảm âm)",
          "Kính bảo hộ",
          "Găng tay da",
          "Ủng cao su"
        ],
        "correct": 0,
        "explanation": "Chụp tai chống ồn ngăn sóng âm cường độ cao tác động vào màng nhĩ."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một người đứng trước vách đá cách 85 m hét to một tiếng. Sau bao lâu người đó nghe thấy tiếng vang? (v = 340 m/s)",
        "options": [
          "0,5 giây",
          "0,25 giây",
          "1,0 giây",
          "2,0 giây"
        ],
        "correct": 0,
        "explanation": "t = 2d / v = (2 × 85) / 340 = 170 / 340 = 0,5 s."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Vì sao trong các phòng thu âm chuyên nghiệp, người ta không sơn tường bóng loáng mà lại ốp mút gai tam giác hoặc thạch cao đục lỗ?",
        "options": [
          "Để triệt tiêu hiện tượng phản xạ âm, tạo môi trường âm học trung thực không bị vang vọng",
          "Để phòng thu đẹp hơn",
          "Để phòng thu ấm hơn",
          "Để chống ẩm"
        ],
        "correct": 0,
        "explanation": "Mút gai tán xạ và triệt tiêu sóng âm phản xạ giúp bản thu âm không bị vang dội."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Biện pháp nào sau đây thuộc nhóm phân tán âm trên đường truyền?",
        "options": [
          "Trồng nhiều hàng cây xanh có tán lá rậm rạp giữa khu dân cư và đường quốc lộ",
          "Yêu cầu tài xế giảm tốc độ",
          "Xử phạt người bấm còi",
          "Đeo nút bịt tai"
        ],
        "correct": 0,
        "explanation": "Tán lá cây rậm rạp phân tán sóng âm ra nhiều hướng làm giảm năng lượng âm truyền tới."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tàu ngầm quân sự phát hiện chướng ngại vật ngầm dưới biển (như rạn san hô, tàu khác) nhờ ứng dụng:",
        "options": [
          "Hệ thống định vị sóng âm phản xạ (Sonar)",
          "Kính thiên văn",
          "Đèn pha cực mạnh",
          "Sóng nhiệt"
        ],
        "correct": 0,
        "explanation": "Hệ thống Sonar phát xung sóng âm và thu âm phản xạ để định vị vật cản dưới nước."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi hét to trong một hang đá sâu và rộng, ta nghe thấy tiếng vang kéo dài lặp lại nhiều lần. Hiện tượng này là do:",
        "options": [
          "Sóng âm phản xạ liên tiếp nhiều lần qua lại giữa các vách đá trong hang",
          "Hang đá tự phát ra tiếng kêu",
          "Có người khác nhại lại tiếng",
          "Gió thổi mạnh trong hang"
        ],
        "correct": 0,
        "explanation": "Âm phản xạ nhiều lần giữa các vách đá tạo chuỗi tiếng vang rền."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một xưởng cưa gỗ hoạt động phát ra tiếng ồn 95 dB nằm cạnh một trường tiểu học. Biện pháp cấp thiết nhất để bảo vệ học sinh là:",
        "options": [
          "Xây tường cách âm cao, chuyển máy cưa vào phòng kín cách âm và yêu cầu xưởng hoạt động ngoài giờ học",
          "Phát kẹo cho học sinh",
          "Cho học sinh nghỉ học vĩnh viễn",
          "Phạt xưởng 10.000 đồng"
        ],
        "correct": 0,
        "explanation": "Xây tường cách âm, cách li nguồn ồn và điều chỉnh giờ hoạt động là biện pháp căn cơ."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về sự phản xạ âm trên các bề mặt vật chất khác nhau:",
        "statements": [
          {
            "subId": "a",
            "text": "Bề mặt tấm thép phẳng phản xạ âm tốt hơn mặt tấm đệm mút.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mặt hồ nước phẳng lặng có thể phản xạ sóng âm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tường nhám, sần sùi phản xạ âm tốt hơn tường quét vôi nhẵn bóng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Các vật có bề mặt xốp mềm có khả năng tiêu âm (hấp thụ âm) rất tốt.",
            "correct": true
          }
        ],
        "explanation": "Tường nhẵn bóng phản xạ âm tốt hơn tường nhám gồ ghề."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các điều kiện để hình thành tiếng vang:",
        "statements": [
          {
            "subId": "a",
            "text": "Phải có bề mặt chướng ngại vật cản để phản xạ sóng âm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Âm phản xạ phải đến tai chậm hơn âm trực tiếp ít nhất 1/15 giây.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trong không khí ở 20 °C, khoảng cách từ người nói đến vật cản phải từ 11,3 m trở lên.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu đứng cách vật cản 3 m ta vẫn nghe thấy tiếng vang tách bạch.",
            "correct": false
          }
        ],
        "explanation": "Ở cự li 3 m, âm phản xạ đến sau âm trực tiếp khoảng 0,018 s < 1/15 s nên không thành tiếng vang."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một người gõ búa xuống sàn bê tông của một nhà kho rộng lớn trống không cách bức tường 51 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc độ âm trong không khí là 340 m/s.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian âm đi từ vị trí gõ đến tường rồi dội về tai là 0,30 giây.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Người đó nghe thấy tiếng vang của tiếng búa sau đúng 0,30 giây.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu kê đầy các kiện hàng bằng thùng xốp và bông vải vào nhà kho thì tiếng vang sẽ càng to hơn.",
            "correct": false
          }
        ],
        "explanation": "Thùng xốp và bông vải hấp thụ âm cực tốt làm triệt tiêu tiếng vang."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Quy chuẩn tiếng ồn trong khu dân cư đô thị theo tiêu chuẩn môi trường Việt Nam:",
        "statements": [
          {
            "subId": "a",
            "text": "Giới hạn tiếng ồn tối đa từ 6h đến 21h trong khu dân cư là 70 dB.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Giới hạn tiếng ồn tối đa từ 21h đến 6h sáng hôm sau trong khu dân cư là 55 dB.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tiếng hát karaoke kẹo kéo ban đêm vượt quá 80 dB là hành vi vi phạm pháp luật về môi trường.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Người dân được phép tự do gây tiếng ồn bất kì lúc nào tại nhà riêng mà không ai có quyền can thiệp.",
            "correct": false
          }
        ],
        "explanation": "Gây tiếng ồn vượt quy chuẩn sau 22h đêm bị xử phạt hành chính theo quy định pháp luật."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Vật có bề mặt nhẵn bóng phản xạ âm tốt hay kém?",
        "correctAnswer": "Tốt",
        "explanation": "Phản xạ âm tốt."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Rèm vải nhung dày có tác dụng hấp thụ âm hay phản xạ âm?",
        "correctAnswer": "Hấp thụ âm",
        "explanation": "Hấp thụ âm tốt."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một người hét to trước vách núi và nghe thấy tiếng vang sau 1,0 giây. Biết v = 340 m/s. Khoảng cách đến vách núi là bao nhiêu mét?",
        "correctAnswer": "170",
        "explanation": "d = 340 × 1,0 / 2 = 170 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khoảng cách từ người đến vách phản xạ là 34 m. Sau bao nhiêu giây người đó nghe thấy tiếng vang? (v = 340 m/s)",
        "correctAnswer": "0.2",
        "explanation": "t = 2 × 34 / 340 = 0,2 s."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Tàu nghiên cứu đáy biển dùng sóng siêu âm (v = 1500 m/s) phát xuống vực thẳm và thu lại tín hiệu sau 1,8 giây. Độ sâu của vực thẳm là bao nhiêu mét?",
        "correctAnswer": "1350",
        "explanation": "d = 1500 × 1,8 / 2 = 1350 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Đơn vị đo mức độ to của tiếng ồn là gì?",
        "correctAnswer": "dB",
        "explanation": "Decibel (dB)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng tại vị trí cách một vách núi đá 255 m bắn một phát súng hiệu. Biết tốc độ âm trong không khí là 340 m/s. Sau bao lâu kể từ lúc nổ súng người đó nghe thấy tiếng vang của phát súng dội lại?",
        "options": [
          "1,5 giây",
          "0,75 giây",
          "1,0 giây",
          "2,0 giây"
        ],
        "correct": 0,
        "explanation": "Quãng đường âm đi và về: 2d = 2 × 255 = 510 m => t = 510 / 340 = 1,5 s."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một căn phòng hòa nhạc có chiều dài từ sân khấu đến bức tường cuối phòng là 20,4 mét. Nếu bức tường cuối phòng là tường bê tông nhẵn bóng thì khi ca sĩ hát một nốt nhạc, âm phản xạ từ tường dội lại sân khấu sau thời gian bao lâu và có gây ra tiếng vang khó chịu không? (Biết v = 340 m/s).",
        "options": [
          "Sau 0,12 giây và có gây ra tiếng vang làm nhòe âm thanh",
          "Sau 0,06 giây và không gây tiếng vang",
          "Sau 0,20 giây",
          "Sau 1,0 giây"
        ],
        "correct": 0,
        "explanation": "t = 2 × 20,4 / 340 = 0,12 s. Vì 0,12 s > 1/15 s (≈ 0,067 s) nên sẽ tạo ra tiếng vang gây nhòe âm thanh nếu không tiêu âm tường."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để giảm thiểu tác động của tiếng ồn giao thông từ đường cao tốc trên cao vào các khu chung cư cao tầng hai bên đường, giải pháp công trình kiến trúc nào sau đây được đánh giá là hiệu quả và hiện đại nhất?",
        "options": [
          "Lắp đặt hệ thống vách chống ồn chuyên dụng bằng vật liệu hấp thụ âm cao cấp bọc quanh hai bên mép đường cao tốc",
          "Trồng cỏ dưới chân cột cầu",
          "Sơn lan can cầu màu trắng",
          "Cấm xe chạy ban ngày"
        ],
        "correct": 0,
        "explanation": "Tường chống ồn (noise barrier) lắp đặt trực tiếp trên lan can đường cao tốc ngăn chặn đường truyền âm thanh."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách một vách núi một khoảng d hét to một tiếng. Đúng 0,6 giây sau người đó nghe thấy âm phản xạ đầu tiên dội lại từ vách núi. Nếu người này lùi xa thêm 34 m nữa rồi lại hét to thì sau bao lâu người đó sẽ nghe thấy âm phản xạ dội lại? (Biết tốc độ âm trong không khí là 340 m/s).",
        "options": [
          "0,8 giây",
          "0,7 giây",
          "0,9 giây",
          "1,0 giây"
        ],
        "correct": 0,
        "explanation": "d = 340 × 0,6 / 2 = 102 m. Khi lùi thêm 34 m: d' = 102 + 34 = 136 m => t' = 2 × 136 / 340 = 0,8 s."
      }
    ]
  },
  "phys7_c4_b14_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_b14",
    "lessonName": "Bài 14: Phản xạ âm, chống ô nhiễm tiếng ồn",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật phản xạ âm tốt là những vật có đặc điểm:",
        "options": [
          "Cứng và có bề mặt nhẵn bóng",
          "Mềm và có bề mặt xốp gồ ghề",
          "Trong suốt và rất nhẹ",
          "Hình cầu rỗng"
        ],
        "correct": 0,
        "explanation": "Vật cứng có mặt phẳng nhẵn phản xạ âm tốt."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Vật hấp thụ âm tốt (tiêu âm) là những vật có đặc điểm:",
        "options": [
          "Mềm, xốp và có bề mặt gồ ghề",
          "Cứng và phẳng lỳ",
          "Bằng kim loại sáng bóng",
          "Bằng đá granit nhẵn"
        ],
        "correct": 0,
        "explanation": "Vật mềm xốp, bề mặt gồ ghề tiêu âm tốt."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Âm phản xạ nghe được cách âm trực tiếp ít nhất một khoảng thời gian bằng bao nhiêu thì tai phân biệt được tiếng vang?",
        "options": [
          "1/15 giây (xấp xỉ 0,067 s)",
          "1 giây",
          "0,5 giây",
          "1/100 giây"
        ],
        "correct": 0,
        "explanation": "1/15 giây là khoảng thời gian tối thiểu phân biệt âm phản xạ tách rời."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biện pháp nào sau đây giúp ngăn chặn sự truyền âm trực tiếp từ bên ngoài vào trong nhà?",
        "options": [
          "Đóng kín các cửa phòng và lắp cửa kính cách âm",
          "Mở quạt thông gió",
          "Bật đèn sáng",
          "Lát sàn gạch men bóng"
        ],
        "correct": 0,
        "explanation": "Đóng kín cửa và dùng cửa kính cách âm ngăn chặn âm truyền qua không khí."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Biển báo giao thông P.128 cấm sử dụng còi xe thường được đặt ở:",
        "options": [
          "Khu vực gần bệnh viện, viện điều dưỡng và trường học",
          "Trên đường cao tốc hoang vắng",
          "Tại các mỏ than",
          "Ở ngã ba đường đồi núi"
        ],
        "correct": 0,
        "explanation": "Cấm còi ở khu vực cần sự yên tĩnh cho người bệnh và học sinh."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nút bịt tai bằng cao su non hoặc bọt biển được sử dụng nhằm mục đích:",
        "options": [
          "Bảo vệ thính giác của người sử dụng khỏi tác hại của tiếng ồn cường độ cao",
          "Làm ấm tai vào mùa đông",
          "Để trang trí",
          "Để nghe nhạc hay hơn"
        ],
        "correct": 0,
        "explanation": "Nút bịt tai giảm cường độ âm tác động vào màng nhĩ."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một người đứng trước một vách đá lớn cách 51 m và hét to. Thời gian để người đó nghe thấy tiếng vang dội lại là bao nhiêu? (Biết tốc độ âm trong không khí là 340 m/s)",
        "options": [
          "0,30 giây",
          "0,15 giây",
          "0,60 giây",
          "0,45 giây"
        ],
        "correct": 0,
        "explanation": "t = 2d / v = (2 × 51) / 340 = 102 / 340 = 0,30 s."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tại sao trong các nhà thờ cổ hoặc giảng đường đại học lớn, khi một người nói thì tiếng nói nghe rất vang và to hơn bình thường?",
        "options": [
          "Vì âm trực tiếp và các âm phản xạ liên tiếp từ tường, trần nhà đến tai gần nhau làm tăng độ to của âm",
          "Vì trần nhà hút hết âm",
          "Vì trong nhà thờ không có không khí",
          "Vì có micro khuếch đại"
        ],
        "correct": 0,
        "explanation": "Âm phản xạ gộp cùng âm trực tiếp làm tăng độ to của âm thanh."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Biện pháp giảm thiểu tiếng ồn bằng cách trồng dải cây xanh tán lá rậm rạp ven đường dựa trên nguyên lí:",
        "options": [
          "Tán lá cây làm phân tán sóng âm theo nhiều hướng khác nhau và hấp thụ một phần năng lượng âm",
          "Cây xanh làm mát không khí",
          "Lá cây phát ra âm thanh át tiếng còi",
          "Cây xanh hút hết bụi"
        ],
        "correct": 0,
        "explanation": "Tán lá cây đóng vai trò như các mặt tán xạ âm tự nhiên."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Dơi bắt được những con muỗi nhỏ bay trong đêm tối là nhờ:",
        "options": [
          "Sóng siêu âm do dơi phát ra phản xạ lại từ cơ thể con muỗi giúp dơi xác định chính xác vị trí con mồi",
          "Dơi có mắt nhìn ban đêm cực rõ",
          "Muỗi phát ra ánh sáng",
          "Dơi bẫy muỗi bằng mùi hương"
        ],
        "correct": 0,
        "explanation": "Sóng siêu âm phản xạ từ con mồi giúp dơi định vị chính xác cự li và phương hướng."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tấm thảm len dày trải trên sàn phòng khách có tác dụng âm học là:",
        "options": [
          "Hấp thụ âm thanh va đập và tiếng bước chân, giảm thiểu tiếng vang trong phòng",
          "Làm sàn nhà trơn hơn",
          "Làm phòng khách tối hơn",
          "Phản xạ âm thanh to hơn"
        ],
        "correct": 0,
        "explanation": "Thảm len tiêu âm và giảm tiếng ồn va đập bước chân."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Khi một chiếc máy bay phản lực cất cánh, mức cường độ âm đo được ở khoảng cách 50 m có thể đạt 130 dB. Mức âm thanh này:",
        "options": [
          "Đạt tới ngưỡng đau tai của con người và có thể làm tổn thương màng nhĩ nếu không có thiết bị bảo hộ",
          "Rất êm ái",
          "Bằng tiếng nói thầm",
          "Hoàn toàn vô hại"
        ],
        "correct": 0,
        "explanation": "130 dB là ngưỡng đau tai, gây nguy hiểm cho thính giác."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về khả năng phản xạ và hấp thụ âm thanh của các vật liệu thông dụng:",
        "statements": [
          {
            "subId": "a",
            "text": "Bức tường ốp đá hoa cương phẳng lỳ phản xạ âm rất tốt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tấm xốp đục lỗ tổ ong có khả năng tiêu âm rất cao.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Rèm vải voan mỏng manh cách âm tốt hơn rèm nhung dày hai lớp.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Gỗ dán công nghiệp ép phẳng phản xạ âm tốt hơn bông thủy tinh cách nhiệt.",
            "correct": true
          }
        ],
        "explanation": "Rèm nhung dày cách âm tốt hơn nhiều so với rèm vải mỏng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về sự hình thành tiếng vang trong các không gian khác nhau:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong một đường hầm dài bằng bê tông, tiếng còi xe vang dội kéo dài rất lâu.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong phòng ngủ nhỏ có nhiều chăn ga gối đệm, ta hầu như không nghe thấy tiếng vang.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Để nghe được tiếng vang trong không khí, vật cản phải cách người phát âm ít nhất khoảng 11,3 m.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu đứng cách bức tường 10 m thì người nói sẽ nghe thấy tiếng vang tách rời hoàn toàn với âm phát ra.",
            "correct": false
          }
        ],
        "explanation": "Ở cự li 10 m, âm phản xạ về sau 0,059 s < 1/15 s nên không tạo tiếng vang tách rời."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Học sinh đo khoảng cách đến vách núi bằng phương pháp phản xạ âm thanh:",
        "statements": [
          {
            "subId": "a",
            "text": "Dùng súng hiệu phát một tiếng nổ ngắn và sắc bén.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đồng hồ bấm giây đo được thời gian từ lúc súng nổ đến khi nghe tiếng vang là 1,8 giây.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Với tốc độ âm trong không khí là 340 m/s, khoảng cách đến vách núi tính được là 306 m.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu tiến lại gần vách núi một nửa cự li thì thời gian thu tiếng vang sẽ tăng lên gấp đôi.",
            "correct": false
          }
        ],
        "explanation": "Tiến lại gần thì khoảng cách giảm một nửa nên thời gian thu tiếng vang giảm một nửa (còn 0,9 s)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Phân tích các biện pháp kiểm soát tiếng ồn tại các đô thị lớn:",
        "statements": [
          {
            "subId": "a",
            "text": "Quy hoạch các khu công nghiệp, nhà máy chế biến xa các khu dân cư tập trung.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Xây dựng các công viên cây xanh và hồ nước sinh thái xen kẽ các khu đô thị.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khuyến khích người dân sử dụng phương tiện giao thông chạy bằng điện ít tiếng ồn hơn xe động cơ xăng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khuyến khích xe tải chở hàng chạy vào các tuyến phố nhỏ lúc nửa đêm để tránh ùn tắc.",
            "correct": false
          }
        ],
        "explanation": "Xe tải lớn chạy vào ngõ phố ban đêm gây ô nhiễm tiếng ồn nghiêm trọng làm mất ngủ người dân."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tường nhẵn bóng phản xạ âm tốt hay kém?",
        "correctAnswer": "Tốt",
        "explanation": "Phản xạ âm tốt."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tấm mút gai có tác dụng phản xạ âm hay tiêu âm?",
        "correctAnswer": "Tiêu âm",
        "explanation": "Tiêu âm (hấp thụ âm)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một người đứng trước vách đá cách 68 m hét to. Sau bao nhiêu giây người đó nghe thấy tiếng vang? (v = 340 m/s)",
        "correctAnswer": "0.4",
        "explanation": "t = 2 × 68 / 340 = 0,4 s."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Thời gian từ lúc phát âm đến khi nhận tiếng vang là 0,8 giây. Vận tốc âm là 340 m/s. Khoảng cách đến vách đá là bao nhiêu mét?",
        "correctAnswer": "136",
        "explanation": "d = 340 × 0,8 / 2 = 136 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Tàu ngầm phát sóng âm xuống đáy biển và thu lại tiếng vang sau 1,2 giây. Biết tốc độ âm trong nước biển là 1500 m/s. Độ sâu của biển là bao nhiêu mét?",
        "correctAnswer": "900",
        "explanation": "d = 1500 × 1,2 / 2 = 900 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Khoảng cách ngắn nhất giữa người phát âm và bức tường phẳng để nghe được tiếng vang trong không khí (v = 340 m/s) là bao nhiêu mét? (Làm tròn 1 chữ số thập phân)",
        "correctAnswer": "11.3",
        "explanation": "11,3 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng trong một thung lũng giữa hai vách núi đá vôi thẳng đứng song song. Người đó bắn một phát súng hiệu thì sau 1,0 giây nghe thấy tiếng vang thứ nhất và sau 1,5 giây nghe thấy tiếng vang thứ hai dội lại từ vách núi đối diện. Biết tốc độ truyền âm trong không khí là 340 m/s. Bề rộng của thung lũng (khoảng cách giữa hai vách núi) là:",
        "options": [
          "425 m",
          "850 m",
          "510 m",
          "340 m"
        ],
        "correct": 0,
        "explanation": "d1 = 340 × 1,0 / 2 = 170 m; d2 = 340 × 1,5 / 2 = 255 m => Bề rộng thung lũng = d1 + d2 = 170 + 255 = 425 m."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước một bức tường phẳng cao của một sân vận động và vỗ tay thật mạnh. Người đó nhận thấy rằng nếu đứng cách tường từ 12 mét trở lên thì nghe thấy tiếng vang rất rõ, còn nếu đứng gần hơn 10 mét thì không nghe thấy tiếng vang tách rời nữa. Giải thích nào sau đây là chuẩn xác nhất?",
        "options": [
          "Vì ở khoảng cách lớn hơn 11,3 m, thời gian âm phản xạ dội lại tai lớn hơn 1/15 giây nên tai phân biệt được âm phản xạ riêng biệt",
          "Vì bức tường hút hết âm thanh ở cự li gần",
          "Vì người vỗ tay yếu đi",
          "Vì không khí bị dồn nén"
        ],
        "correct": 0,
        "explanation": "Thời gian phản xạ vượt quá 1/15 giây giúp màng nhĩ phân biệt được hai xung âm riêng biệt."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để phòng ngủ của một căn nhà gần mặt đường quốc lộ được yên tĩnh, gia chủ đã áp dụng đồng thời các giải pháp: lắp cửa sổ kính hộp 2 lớp cách âm chân không, treo rèm cửa bằng vải nhung dày 2 lớp và trồng một hàng cau cảnh tán rậm trước hiên nhà. Các giải pháp này đã ngăn chặn tiếng ồn theo nguyên lí nào?",
        "options": [
          "Kết hợp ngăn chặn đường truyền âm (cửa kính, rèm nhung) và phân tán sóng âm (hàng cây cảnh)",
          "Chỉ giảm âm tại nguồn phát",
          "Chỉ làm tăng độ to của âm",
          "Chỉ đổi tần số âm"
        ],
        "correct": 0,
        "explanation": "Kết hợp đa giải pháp cản đường truyền và phân tán tiêu âm."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một thiết bị đo độ sâu đáy biển bằng chùm sóng siêu âm Sonar gắn dưới đáy tàu thủy phát ra một xung sóng siêu âm hướng thẳng đứng xuống đáy biển. Sau 0,64 giây, cảm biến trên tàu ghi nhận được xung phản xạ dội lại từ đáy biển. Biết tốc độ truyền sóng siêu âm trong nước biển là 1500 m/s. Độ sâu của đáy biển tại vị trí tàu đang neo đậu là:",
        "options": [
          "480 m",
          "960 m",
          "320 m",
          "600 m"
        ],
        "correct": 0,
        "explanation": "d = v × t / 2 = 1500 × 0,64 / 2 = 480 m."
      }
    ]
  },
  "phys7_c4_rev_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương IV - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương IV",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Mọi vật phát ra âm thanh đều:",
        "options": [
          "Đang dao động",
          "Đang chuyển động thẳng",
          "Có nhiệt độ rất cao",
          "Đang đứng yên"
        ],
        "correct": 0,
        "explanation": "Dao động là nguồn gốc của mọi âm thanh."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Sóng âm truyền được trong môi trường nào sau đây?",
        "options": [
          "Chất rắn, chất lỏng và chất khí",
          "Chỉ chất khí",
          "Chỉ chất lỏng",
          "Chân không tuyệt đối"
        ],
        "correct": 0,
        "explanation": "Sóng âm truyền trong rắn, lỏng, khí."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tần số dao động là số dao động vật thực hiện được trong:",
        "options": [
          "1 giây",
          "1 phút",
          "1 giờ",
          "1 ngày"
        ],
        "correct": 0,
        "explanation": "Tần số là số dao động trong 1 giây (Hz)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Độ cao của âm phụ thuộc vào:",
        "options": [
          "Tần số dao động của nguồn âm",
          "Biên độ dao động",
          "Độ to của âm",
          "Khoảng cách truyền âm"
        ],
        "correct": 0,
        "explanation": "Tần số quyết định độ cao (bổng/trầm)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Vật liệu nào sau đây phản xạ âm tốt?",
        "options": [
          "Gạch men bóng phẳng",
          "Rèm vải nhung",
          "Tấm mút xốp",
          "Bông gòn mềm"
        ],
        "correct": 0,
        "explanation": "Gạch men bóng cứng phản xạ âm tốt."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Biện pháp nào sau đây giúp hạn chế tiếng ồn từ động cơ xe máy phát ra?",
        "options": [
          "Lắp bộ giảm thanh (ống xả tiêu âm) đạt chuẩn",
          "Tháo bỏ ống xả",
          "Bấm còi to",
          "Tăng ga mạnh"
        ],
        "correct": 0,
        "explanation": "Ống giảm thanh giảm độ to ngay tại nguồn phát."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một vật thực hiện 240 dao động trong 6 giây. Tần số dao động của vật là:",
        "options": [
          "40 Hz",
          "1440 Hz",
          "240 Hz",
          "60 Hz"
        ],
        "correct": 0,
        "explanation": "f = 240 / 6 = 40 Hz."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Âm thanh có tần số 35.000 Hz thuộc dải sóng nào?",
        "options": [
          "Sóng siêu âm",
          "Sóng hạ âm",
          "Âm nghe được",
          "Sóng vô tuyến"
        ],
        "correct": 0,
        "explanation": "f > 20.000 Hz là sóng siêu âm."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một người gõ búa vào thanh thép dài. Tốc độ âm trong thép xấp xỉ khoảng:",
        "options": [
          "5000 m/s",
          "340 m/s",
          "1500 m/s",
          "300.000 km/s"
        ],
        "correct": 0,
        "explanation": "Tốc độ âm trong thép khoảng 5000 m/s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khoảng cách tối thiểu từ người phát âm đến bức tường để nghe được tiếng vang trong không khí (v = 340 m/s) là:",
        "options": [
          "Khoảng 11,3 mét",
          "Khoảng 5,5 mét",
          "Khoảng 22,7 mét",
          "Khoảng 34 mét"
        ],
        "correct": 0,
        "explanation": "d_min = 340 × (1/15) / 2 ≈ 11,3 m."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Gảy dây đàn guitar càng mạnh thì biên độ dao động càng lớn, âm phát ra sẽ:",
        "options": [
          "Nghe càng to",
          "Càng bổng hơn",
          "Càng trầm hơn",
          "Không thay đổi"
        ],
        "correct": 0,
        "explanation": "Biên độ lớn làm độ to của âm tăng lên."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Biển báo cấm sử dụng còi xe đặt gần cổng trường học nhằm:",
        "options": [
          "Ngăn chặn ô nhiễm tiếng ồn, tạo không gian yên tĩnh cho học sinh học tập",
          "Để xe chạy nhanh hơn",
          "Tránh hỏng còi xe",
          "Để người đi bộ không giật mình"
        ],
        "correct": 0,
        "explanation": "Hạn chế ô nhiễm tiếng ồn bảo vệ môi trường sư phạm."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về sự lan truyền và cảm nhận sóng âm của con người:",
        "statements": [
          {
            "subId": "a",
            "text": "Sóng âm mang năng lượng và làm màng nhĩ trong tai dao động.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong chân không, sóng âm truyền đi với tốc độ bằng tốc độ ánh sáng.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Tốc độ truyền âm giảm dần: chất rắn > chất lỏng > chất khí.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dải tần số âm tai người cảm nhận được là từ 16 Hz đến 20.000 Hz.",
            "correct": true
          }
        ],
        "explanation": "Sóng âm hoàn toàn không truyền được trong chân không."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về mối quan hệ giữa dao động và âm thanh:",
        "statements": [
          {
            "subId": "a",
            "text": "Dao động càng nhanh thì tần số dao động càng lớn, âm nghe càng bổng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Độ lệch lớn nhất của vật khỏi vị trí cân bằng gọi là biên độ dao động.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Âm có độ to 140 dB gây cảm giác êm tai và dễ chịu.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tiếng sấm rền kéo dài là do hiện tượng âm phản xạ liên tiếp giữa mây và đất.",
            "correct": true
          }
        ],
        "explanation": "140 dB vượt ngưỡng đau tai (130 dB), gây đau đớn và thủng màng nhĩ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Thí nghiệm khảo sát tiếng vang trong một hầm bê tông dài 68 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Một người đứng ở đầu hầm vỗ tay một tiếng ngắn dứt khoát.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sóng âm truyền đến cuối hầm dội vào vách tường phẳng rồi quay lại tai người.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thời gian âm phản xạ truyền về tai là 0,40 giây (biết v = 340 m/s).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Người đó không thể nghe thấy tiếng vang vì khoảng cách quá gần.",
            "correct": false
          }
        ],
        "explanation": "0,40 s > 1/15 s (≈ 0,067 s) nên người đó nghe thấy tiếng vang rất to và rõ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Về sóng siêu âm và các ứng dụng trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Sóng siêu âm có tần số trên 20.000 Hz, tai người không nghe thấy được.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dơi dùng sóng siêu âm để săn muỗi và định vị đường bay trong đêm tối.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tàu ngầm dùng máy phát sóng siêu âm sonar để đo độ sâu đáy biển.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Sóng siêu âm bị cản lại và không thể truyền qua lớp nước biển.",
            "correct": false
          }
        ],
        "explanation": "Sóng siêu âm truyền cực kì tốt trong nước biển."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một vật thực hiện 180 dao động trong 3 giây. Tần số dao động là bao nhiêu Hz?",
        "correctAnswer": "60",
        "explanation": "f = 180 / 3 = 60 Hz."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tốc độ truyền âm trong không khí ở nhiệt độ 20 °C là bao nhiêu m/s?",
        "correctAnswer": "340",
        "explanation": "340 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Âm thanh có tần số 12 Hz thuộc dải sóng nào? (Hạ âm hay Siêu âm)",
        "correctAnswer": "Hạ âm",
        "explanation": "f < 16 Hz là hạ âm."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người nhìn thấy ánh chớp rồi sau 2,5 giây nghe thấy tiếng sấm. Biết v = 340 m/s. Nơi sét đánh cách người đó bao nhiêu mét?",
        "correctAnswer": "850",
        "explanation": "s = 340 × 2,5 = 850 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước vách đá hét to và nghe thấy tiếng vang sau 0,8 giây. Khoảng cách đến vách đá là bao nhiêu mét? (v = 340 m/s)",
        "correctAnswer": "136",
        "explanation": "d = 340 × 0,8 / 2 = 136 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Máy đo hồi âm sonar trên tàu phát xung siêu âm xuống đáy biển và thu lại tín hiệu sau 1,6 giây. Với v = 1500 m/s, độ sâu đáy biển là bao nhiêu mét?",
        "correctAnswer": "1200",
        "explanation": "d = 1500 × 1,6 / 2 = 1200 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người gõ búa vào thanh ray xe lửa bằng thép dài 1020 m. Người thứ hai áp tai vào thanh ray nghe thấy hai tiếng gõ liên tiếp cách nhau 2,8 giây: một tiếng truyền qua thép và một tiếng truyền qua không khí (v = 340 m/s). Tốc độ truyền âm trong thép của thanh ray là:",
        "options": [
          "5100 m/s",
          "3400 m/s",
          "4800 m/s",
          "6000 m/s"
        ],
        "correct": 0,
        "explanation": "t_khí = 1020 / 340 = 3,0 s. t_thép = 3,0 - 2,8 = 0,2 s => v_thép = 1020 / 0,2 = 5100 m/s."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách một vách núi đá vôi 340 m hét to một tiếng. Sau bao lâu kể từ lúc phát âm người đó nghe thấy tiếng vang dội lại từ vách núi? (Biết tốc độ âm trong không khí là 340 m/s).",
        "options": [
          "2,0 giây",
          "1,0 giây",
          "1,5 giây",
          "0,5 giây"
        ],
        "correct": 0,
        "explanation": "t = 2d / v = 2 × 340 / 340 = 2,0 s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tại sao khi bước vào một ngôi nhà mới xây chưa có đồ đạc, tiếng bước chân và tiếng nói chuyện của ta nghe rất vang, nhưng khi đã kê đầy bàn ghế, giường tủ và treo rèm cửa thì hiện tượng này biến mất?",
        "options": [
          "Vì đồ đạc gỗ và rèm vải xốp mềm đã hấp thụ phần lớn năng lượng sóng âm phản xạ, làm triệt tiêu tiếng vang",
          "Vì không khí trong nhà bị ấm lên",
          "Vì sàn nhà bị lún",
          "Vì mắt nhìn thấy đồ đạc"
        ],
        "correct": 0,
        "explanation": "Đồ đạc và rèm vải tiêu âm hiệu quả, triệt tiêu phản xạ âm thanh."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một máy phát sóng siêu âm phát một tín hiệu thẳng đứng từ mạn thuyền xuống đáy một hồ nước sâu và nhận lại tín hiệu phản xạ sau 0,12 giây. Biết tốc độ âm trong nước hồ là 1500 m/s. Độ sâu của hồ nước tại vị trí khảo sát là:",
        "options": [
          "90 m",
          "180 m",
          "45 m",
          "120 m"
        ],
        "correct": 0,
        "explanation": "d = 1500 × 0,12 / 2 = 90 m."
      }
    ]
  },
  "phys7_c4_rev_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương IV - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương IV",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật phát ra âm thanh khi nào?",
        "options": [
          "Khi vật đang dao động đàn hồi",
          "Khi vật được nung nóng",
          "Khi vật đứng yên tuyệt đối",
          "Khi có dòng điện chạy qua"
        ],
        "correct": 0,
        "explanation": "Mọi vật phát ra âm thanh đều đang dao động."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Sóng âm KHÔNG THỂ truyền được qua môi trường nào?",
        "options": [
          "Chân không",
          "Khí oxi",
          "Nước cất",
          "Thanh đồng"
        ],
        "correct": 0,
        "explanation": "Chân không không truyền được sóng âm."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Đơn vị dùng để đo mức độ to của âm thanh là:",
        "options": [
          "Decibel (dB)",
          "Hertz (Hz)",
          "Mét (m)",
          "Jun (J)"
        ],
        "correct": 0,
        "explanation": "Độ to của âm đo bằng Decibel (dB)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Âm thanh phát ra nghe càng bổng khi:",
        "options": [
          "Tần số dao động của nguồn âm càng lớn",
          "Tần số dao động càng nhỏ",
          "Biên độ dao động càng nhỏ",
          "Nguồn âm đứng yên"
        ],
        "correct": 0,
        "explanation": "Tần số càng lớn âm càng bổng."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Vật nào sau đây phản xạ âm kém nhất (hấp thụ âm tốt nhất)?",
        "options": [
          "Tấm xốp cách âm",
          "Tấm gương kính",
          "Tường đá hoa cương",
          "Mặt kim loại nhẵn"
        ],
        "correct": 0,
        "explanation": "Xốp mềm có bề mặt rỗng xốp tiêu âm tốt nhất."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Chụp tai chống ồn có tác dụng chính là:",
        "options": [
          "Bảo vệ màng nhĩ khỏi tác hại của tiếng ồn cường độ cao",
          "Giúp nghe rõ tiếng thì thầm",
          "Tránh bụi bẩn",
          "Làm ấm tai"
        ],
        "correct": 0,
        "explanation": "Bảo vệ màng nhĩ tai người lao động."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một con lắc dao động 150 lần trong thời gian 30 giây. Tần số dao động là:",
        "options": [
          "5 Hz",
          "150 Hz",
          "4500 Hz",
          "0,2 Hz"
        ],
        "correct": 0,
        "explanation": "f = 150 / 30 = 5 Hz."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Sóng âm có tần số 14 Hz thuộc vùng sóng nào?",
        "options": [
          "Hạ âm",
          "Siêu âm",
          "Âm nghe được",
          "Sóng ánh sáng"
        ],
        "correct": 0,
        "explanation": "14 Hz < 16 Hz là hạ âm."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tốc độ truyền âm trong nước biển khoảng 1500 m/s. Thời gian âm truyền đi quãng đường 4500 m trong nước là:",
        "options": [
          "3,0 giây",
          "1,5 giây",
          "2,0 giây",
          "4,5 giây"
        ],
        "correct": 0,
        "explanation": "t = 4500 / 1500 = 3,0 s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Một người hét to trước vách núi cách 170 m. Sau bao lâu người đó nghe thấy tiếng vang dội lại? (v = 340 m/s)",
        "options": [
          "1,0 giây",
          "0,5 giây",
          "2,0 giây",
          "1,5 giây"
        ],
        "correct": 0,
        "explanation": "t = 2 × 170 / 340 = 1,0 s."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Gõ mạnh vào mặt trống làm màng trống dao động với biên độ lớn thì:",
        "options": [
          "Âm phát ra nghe to hơn",
          "Âm phát ra bổng hơn",
          "Âm phát ra trầm hơn",
          "Âm bị tắt đi"
        ],
        "correct": 0,
        "explanation": "Biên độ lớn làm tăng độ to của âm."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hành vi nào sau đây góp phần chống ô nhiễm tiếng ồn trong khu dân cư?",
        "options": [
          "Không bấm còi xe inh ỏi và không mở loa công suất lớn lúc đêm khuya",
          "Bóp còi liên tục",
          "Mở nhạc đám cưới suốt đêm",
          "Cắt ống xả xe máy"
        ],
        "correct": 0,
        "explanation": "Tôn trọng sự yên tĩnh chung của cộng đồng."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về bản chất dao động của các nguồn âm thông dụng:",
        "statements": [
          {
            "subId": "a",
            "text": "Dây đàn bầu dao động khi người nghệ sĩ gảy đàn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cột không khí bên trong ống sáo dao động khi thổi sáo.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Màng loa rung qua lại liên tục khi đang phát nhạc.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tiếng sấm phát ra từ các đám mây hoàn toàn không liên quan đến dao động không khí.",
            "correct": false
          }
        ],
        "explanation": "Tiếng sấm là do không khí bị giãn nở đột ngột và dao động dữ dội phát ra âm thanh."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về khả năng nghe của tai người và động vật:",
        "statements": [
          {
            "subId": "a",
            "text": "Tai người nghe được âm từ 16 Hz đến 20.000 Hz.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hạ âm có tần số nhỏ hơn 16 Hz.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Siêu âm có tần số lớn hơn 20.000 Hz.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Loài dơi không thể phát ra sóng siêu âm.",
            "correct": false
          }
        ],
        "explanation": "Dơi phát sóng siêu âm cực tốt để định vị săn mồi."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Học sinh làm thí nghiệm chứng minh sự truyền âm qua chất rắn bằng thước nhựa dài 1 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Bạn A áp tai vào một đầu thước nhựa.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bạn B cào nhẹ đầu móng tay vào đầu kia của thước nhựa.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Bạn A nghe thấy tiếng cào truyền qua thước nhựa rất rõ ràng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Người đứng ngoài cách 1 m trong không khí nghe thấy tiếng cào to hơn bạn A.",
            "correct": false
          }
        ],
        "explanation": "Chất rắn truyền âm tốt hơn nhiều so với không khí nên bạn A nghe rõ hơn nhiều người đứng ngoài."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng vật liệu cách âm trong các công trình hiện đại:",
        "statements": [
          {
            "subId": "a",
            "text": "Cửa kính hộp hai lớp có lớp chân không ở giữa giúp cách âm cách nhiệt hoàn hảo.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phòng karaoke thường bọc mút gai tiêu âm để chống tiếng ồn lọt ra ngoài.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tấm tôn kim loại phẳng nhẵn có khả năng tiêu âm tốt hơn tấm đệm cao su non.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Trồng cây xanh tán rộng quanh trường học giúp cản bớt tiếng ồn đường phố.",
            "correct": true
          }
        ],
        "explanation": "Tấm kim loại phản xạ âm tốt chứ không tiêu âm tốt bằng cao su non."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một lá thép dao động 250 lần trong 5 giây. Tần số dao động là bao nhiêu Hz?",
        "correctAnswer": "50",
        "explanation": "f = 250 / 5 = 50 Hz."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Đơn vị đo tần số dao động là gì?",
        "correctAnswer": "Hz",
        "explanation": "Hertz (Hz)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Sóng âm có tần số 28.000 Hz thuộc vùng sóng nào? (Hạ âm hay Siêu âm)",
        "correctAnswer": "Siêu âm",
        "explanation": "f > 20.000 Hz là siêu âm."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Sau khi nhìn thấy tia sét, đúng 3,0 giây sau nghe thấy tiếng sấm. Biết v = 340 m/s. Khoảng cách đến tia sét là bao nhiêu mét?",
        "correctAnswer": "1020",
        "explanation": "s = 340 × 3 = 1020 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước vách đá hét to và nghe thấy tiếng vang sau 0,6 giây. Khoảng cách đến vách đá là bao nhiêu mét? (v = 340 m/s)",
        "correctAnswer": "102",
        "explanation": "d = 340 × 0,6 / 2 = 102 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Tàu thăm dò đáy biển phát sóng âm sonar xuống biển và nhận lại tiếng vang sau 2,0 giây. Với v = 1500 m/s, độ sâu đáy biển là bao nhiêu mét?",
        "correctAnswer": "1500",
        "explanation": "d = 1500 × 2 / 2 = 1500 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách bức tường của một sân khấu ngoài trời 68 m vỗ tay một cái. Sau bao lâu người đó nghe thấy tiếng vang dội lại từ bức tường? (Biết tốc độ âm trong không khí là 340 m/s).",
        "options": [
          "0,4 giây",
          "0,2 giây",
          "0,5 giây",
          "0,8 giây"
        ],
        "correct": 0,
        "explanation": "t = 2 × 68 / 340 = 0,4 s."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người đứng giữa hai vách đá thẳng đứng song song trong hẻm núi. Người này bắn một phát súng hiệu thì sau 0,8 giây nghe thấy tiếng vang thứ nhất và sau 1,2 giây nghe thấy tiếng vang thứ hai dội lại từ vách đối diện. Bề rộng của hẻm núi là bao nhiêu mét? (Biết tốc độ âm trong không khí là 340 m/s).",
        "options": [
          "340 m",
          "680 m",
          "170 m",
          "510 m"
        ],
        "correct": 0,
        "explanation": "d1 = 340 × 0,8 / 2 = 136 m; d2 = 340 × 1,2 / 2 = 204 m => Bề rộng = 136 + 204 = 340 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tại sao khi ta đứng ở gần đường tàu hỏa, người ta thường khuyên nên áp tai vào đường ray để biết tàu hỏa đang đến gần từ xa?",
        "options": [
          "Vì thanh ray thép truyền âm nhanh hơn và ít bị suy giảm năng lượng hơn nhiều so với không khí",
          "Vì đường ray phát ra âm thanh",
          "Vì không khí bị gió thổi ngược",
          "Vì mặt đất rung lên"
        ],
        "correct": 0,
        "explanation": "Thép (chất rắn) truyền âm với tốc độ ~ 5000 m/s và bảo toàn năng lượng tốt hơn không khí."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một đoàn thám hiểm sử dụng máy đo hồi âm siêu âm để khảo sát độ sâu của một rãnh nứt dưới đáy biển. Tín hiệu siêu âm phát đi truyền với tốc độ 1500 m/s và nhận lại sau 0,48 giây. Độ sâu của rãnh nứt đó là:",
        "options": [
          "360 m",
          "720 m",
          "180 m",
          "540 m"
        ],
        "correct": 0,
        "explanation": "d = 1500 × 0,48 / 2 = 360 m."
      }
    ]
  },
  "phys7_c4_rev_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương IV - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương IV",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Âm thanh truyền nhanh nhất trong môi trường nào?",
        "options": [
          "Chất rắn",
          "Chất lỏng",
          "Chất khí",
          "Chân không"
        ],
        "correct": 0,
        "explanation": "Tốc độ âm trong chất rắn là lớn nhất."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Độ cao của âm gắn liền với đại lượng nào của nguồn âm?",
        "options": [
          "Tần số dao động",
          "Biên độ dao động",
          "Độ to của âm",
          "Thể tích nguồn âm"
        ],
        "correct": 0,
        "explanation": "Tần số dao động quyết định độ cao của âm."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Mức độ to của âm phụ thuộc vào:",
        "options": [
          "Biên độ dao động của nguồn âm",
          "Tần số dao động của nguồn âm",
          "Tốc độ truyền sóng âm",
          "Hình dạng vật phát âm"
        ],
        "correct": 0,
        "explanation": "Biên độ dao động quyết định độ to của âm."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Âm thanh có tần số nhỏ hơn 16 Hz được gọi là:",
        "options": [
          "Hạ âm",
          "Siêu âm",
          "Âm nghe được",
          "Sóng điện từ"
        ],
        "correct": 0,
        "explanation": "f < 16 Hz là hạ âm."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Vật liệu nào sau đây thường dùng làm tường cách âm phòng thu âm?",
        "options": [
          "Mút xốp đục lỗ, rèm nhung dạ",
          "Tấm nhôm sáng bóng",
          "Mặt gương kính phẳng",
          "Tấm đá granit mài bóng"
        ],
        "correct": 0,
        "explanation": "Vật mềm xốp tiêu âm tốt."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Thiết bị giảm thanh (bộ phận tiêu âm) gắn ở đuôi xe máy có tác dụng gì?",
        "options": [
          "Giảm độ to của âm thanh xả khí từ động cơ",
          "Tăng tốc độ của xe",
          "Làm mát buồng đốt",
          "Tăng âm lượng còi xe"
        ],
        "correct": 0,
        "explanation": "Giảm tiếng ồn khí xả động cơ."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một quả lắc đồng hồ dao động 120 lần trong 2 phút (120 s). Tần số dao động là:",
        "options": [
          "1 Hz",
          "60 Hz",
          "120 Hz",
          "2 Hz"
        ],
        "correct": 0,
        "explanation": "f = 120 / 120 = 1 Hz."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Sóng siêu âm có tần số nằm trong khoảng nào?",
        "options": [
          "Trên 20.000 Hz",
          "Dưới 16 Hz",
          "Từ 16 Hz đến 20.000 Hz",
          "0 đến 100 Hz"
        ],
        "correct": 0,
        "explanation": "Siêu âm trên 20.000 Hz."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Đứng cách bức tường phẳng 34 m hét to, sau bao lâu ta nghe thấy tiếng vang dội lại? (v = 340 m/s)",
        "options": [
          "0,20 giây",
          "0,10 giây",
          "0,40 giây",
          "0,50 giây"
        ],
        "correct": 0,
        "explanation": "t = 2 × 34 / 340 = 0,20 s."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Người xưa thường dùng tiếng trống lệnh đồng để truyền tin báo động trong quân đội vì:",
        "options": [
          "Mặt trống đồng dao động phát ra âm thanh trầm vang truyền đi rất xa trong không khí",
          "Trống đồng phát ra ánh sáng",
          "Trống đồng rất nhẹ",
          "Trống đồng không bị gỉ"
        ],
        "correct": 0,
        "explanation": "Mặt trống đồng vang xa, truyền tin hiệu quả."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi căng dây đàn guitar chặt hơn rồi gảy, âm phát ra sẽ:",
        "options": [
          "Bổng hơn vì tần số dao động của dây đàn tăng lên",
          "Trầm hơn",
          "Không đổi",
          "Nghe nhỏ đi"
        ],
        "correct": 0,
        "explanation": "Dây căng hơn dao động nhanh hơn => âm bổng hơn."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Biện pháp nào sau đây giúp phân tán tiếng ồn trên đường truyền?",
        "options": [
          "Trồng nhiều cây xanh có tán lá rộng xum xuê ven đường",
          "Bịt chặt tai",
          "Lắp ống xả giảm thanh",
          "Cấm xe chạy"
        ],
        "correct": 0,
        "explanation": "Cây xanh làm phân tán sóng âm."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các đặc trưng của sóng âm trong các môi trường:",
        "statements": [
          {
            "subId": "a",
            "text": "Sóng âm truyền dao động qua các phân tử vật chất của môi trường.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong không khí ở 20 °C, âm thanh truyền với tốc độ khoảng 340 m/s.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ âm trong nước biển nhỏ hơn trong không khí.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Các phi hành gia trên Mặt Trăng phải dùng sóng vô tuyến (bộ đàm) để giao tiếp.",
            "correct": true
          }
        ],
        "explanation": "Tốc độ âm trong nước (~ 1500 m/s) lớn hơn nhiều so với trong không khí (~ 340 m/s)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tần số và biên độ dao động:",
        "statements": [
          {
            "subId": "a",
            "text": "Tần số đo bằng đơn vị Hertz (Hz).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Biên độ dao động càng lớn thì âm nghe càng to.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Vật dao động càng nhanh thì âm phát ra càng trầm.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Âm có tần số 50 Hz nghe trầm hơn âm có tần số 500 Hz.",
            "correct": true
          }
        ],
        "explanation": "Dao động nhanh làm âm bổng hơn, không phải trầm hơn."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát âm thanh phát ra từ một chiếc loa điện gắn trên giá thí nghiệm:",
        "statements": [
          {
            "subId": "a",
            "text": "Rắc vài mẩu xốp nhỏ lên màng loa, khi bật nhạc màng loa rung làm các mẩu xốp nảy lên.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi vặn nút âm lượng to lên, các hạt xốp nảy lên cao hơn do biên độ tăng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tần số nốt nhạc phát ra không bị thay đổi khi ta tăng hoặc giảm âm lượng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu chụp kín chiếc chuông thủy tinh đã hút chân không lên loa thì ta vẫn nghe thấy tiếng nhạc to như cũ.",
            "correct": false
          }
        ],
        "explanation": "Chân không không truyền được âm nên tiếng nhạc bị tắt hẳn."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng tiếng vang để đo độ sâu đáy biển:",
        "statements": [
          {
            "subId": "a",
            "text": "Máy sonar phát chùm sóng siêu âm định hướng xuống đáy biển.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sóng siêu âm phản xạ từ đáy biển dội ngược lên tàu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thời gian sóng đi và về là 1,0 s thì độ sâu của biển là 1500 m (biết v = 1500 m/s).",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Độ sâu thực tế của biển trong trường hợp này là d = 1500 × 1,0 / 2 = 750 m.",
            "correct": true
          }
        ],
        "explanation": "Độ sâu phải chia đôi: 1500 × 1,0 / 2 = 750 m (câu c ghi 1500 m là sai)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một vật dao động thực hiện 400 dao động trong 8 giây. Tần số dao động là bao nhiêu Hz?",
        "correctAnswer": "50",
        "explanation": "f = 400 / 8 = 50 Hz."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Âm thanh có tần số 8 Hz thuộc vùng sóng nào? (Hạ âm hay Siêu âm)",
        "correctAnswer": "Hạ âm",
        "explanation": "f < 16 Hz là hạ âm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khoảng cách từ người đến vách núi là 85 m. Sau bao nhiêu giây người đó nghe thấy tiếng vang? (v = 340 m/s)",
        "correctAnswer": "0.5",
        "explanation": "t = 2 × 85 / 340 = 0,5 s."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Sóng âm truyền trong không khí mất 3,5 giây để đến tai người nghe. Biết v = 340 m/s. Khoảng cách nguồn âm là bao nhiêu mét?",
        "correctAnswer": "1190",
        "explanation": "s = 340 × 3,5 = 1190 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Tàu ngầm thu được tiếng vang phản xạ từ đáy vực sau 0,8 giây. Với v = 1500 m/s, độ sâu đáy vực là bao nhiêu mét?",
        "correctAnswer": "600",
        "explanation": "d = 1500 × 0,8 / 2 = 600 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Độ to của tiếng động cơ phản lực ở cự li gần có thể đạt tới bao nhiêu decibel (dB)?",
        "correctAnswer": "130",
        "explanation": "Khoảng 120 - 130 dB."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng tại miệng một giếng sâu khô cạn hét to một tiếng xuống đáy giếng và nghe thấy tiếng vang vọng lại sau 0,25 giây. Biết tốc độ âm trong không khí là 340 m/s. Độ sâu của chiếc giếng đó là:",
        "options": [
          "42,5 m",
          "85,0 m",
          "21,25 m",
          "50,0 m"
        ],
        "correct": 0,
        "explanation": "h = 340 × 0,25 / 2 = 42,5 m."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người gõ một nhát búa vào đường ống kim loại bằng gang dài 1360 m. Người thứ hai áp tai vào đầu kia của ống nghe thấy tiếng gõ truyền qua gang sau 0,4 giây và tiếng gõ truyền qua không khí sau 4,0 giây. Tốc độ truyền âm trong gang đo được là:",
        "options": [
          "3400 m/s",
          "5100 m/s",
          "1700 m/s",
          "4000 m/s"
        ],
        "correct": 0,
        "explanation": "v_gang = 1360 / 0,4 = 3400 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tại sao khi một đoàn máy bay chiến đấu bay qua khu dân cư ở độ cao thấp, các cửa kính của các tòa nhà cao tầng thường bị rung lên bần bật?",
        "options": [
          "Vì sóng âm thanh có năng lượng cơ học rất lớn truyền trong không khí tác dụng lực làm rung các tấm kính",
          "Vì máy bay hút hết không khí",
          "Vì cửa kính bị nhiễm điện",
          "Vì nhiệt độ tăng cao"
        ],
        "correct": 0,
        "explanation": "Sóng âm mang năng lượng cơ học lớn tác động vào các tấm kính gây rung động mạnh."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách một vách núi đá 119 m bắn một phát súng hiệu. Biết tốc độ âm trong không khí là 340 m/s. Sau bao lâu người đó nghe thấy tiếng vang dội lại?",
        "options": [
          "0,7 giây",
          "0,35 giây",
          "1,4 giây",
          "0,5 giây"
        ],
        "correct": 0,
        "explanation": "t = 2 × 119 / 340 = 0,7 s."
      }
    ]
  },
  "phys7_c4_rev_test4": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương IV - Đề số 04",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương IV",
    "testNum": 4,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Nguồn âm là:",
        "options": [
          "Vật tự nó phát ra âm thanh",
          "Vật hứng âm thanh",
          "Vật phản xạ ánh sáng",
          "Vật trong suốt"
        ],
        "correct": 0,
        "explanation": "Vật phát ra âm thanh gọi là nguồn âm."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Âm thanh truyền được trong:",
        "options": [
          "Chất rắn, lỏng, khí",
          "Chỉ chân không",
          "Chỉ chất rắn",
          "Chỉ chất khí"
        ],
        "correct": 0,
        "explanation": "Âm truyền trong cả 3 thể rắn, lỏng, khí."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Số dao động vật thực hiện được trong một giây gọi là:",
        "options": [
          "Tần số dao động",
          "Biên độ",
          "Quãng đường",
          "Thời gian"
        ],
        "correct": 0,
        "explanation": "Tần số là số dao động trong 1 giây."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Âm phát ra càng trầm khi tần số dao động:",
        "options": [
          "Càng nhỏ",
          "Càng lớn",
          "Bằng 20.000 Hz",
          "Cực đại"
        ],
        "correct": 0,
        "explanation": "Tần số nhỏ âm phát ra trầm."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tiếng vang là âm phản xạ nghe được cách âm trực tiếp ít nhất:",
        "options": [
          "1/15 giây",
          "1 giây",
          "1/2 giây",
          "1/100 giây"
        ],
        "correct": 0,
        "explanation": "Ít nhất 1/15 giây để tạo tiếng vang."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Vật liệu mềm, xốp, có bề mặt gồ ghề là vật liệu:",
        "options": [
          "Hấp thụ âm tốt (tiêu âm tốt)",
          "Phản xạ âm rất tốt",
          "Không truyền âm",
          "Phát ra âm to"
        ],
        "correct": 0,
        "explanation": "Vật mềm xốp tiêu âm tốt."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một vật dao động thực hiện 300 dao động trong 10 giây. Tần số dao động là:",
        "options": [
          "30 Hz",
          "3000 Hz",
          "300 Hz",
          "3 Hz"
        ],
        "correct": 0,
        "explanation": "f = 300 / 10 = 30 Hz."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Sóng âm có tần số 40.000 Hz thuộc dải sóng nào?",
        "options": [
          "Sóng siêu âm",
          "Sóng hạ âm",
          "Âm nghe được",
          "Sóng điện từ"
        ],
        "correct": 0,
        "explanation": "f > 20.000 Hz là siêu âm."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Nhìn thấy tia chớp rồi 1,5 giây sau nghe thấy tiếng sấm (v = 340 m/s). Nơi sét đánh cách người quan sát là:",
        "options": [
          "510 m",
          "340 m",
          "680 m",
          "1020 m"
        ],
        "correct": 0,
        "explanation": "s = 340 × 1,5 = 510 m."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khi một người nói to hơn bình thường thì màng nhĩ người nghe sẽ:",
        "options": [
          "Dao động với biên độ lớn hơn",
          "Dao động với tần số cao hơn",
          "Đứng yên",
          "Bị thủng ngay"
        ],
        "correct": 0,
        "explanation": "Âm to làm màng nhĩ dao động với biên độ lớn hơn."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Vật nào sau đây phản xạ âm tốt nhất?",
        "options": [
          "Tấm gương phẳng phẳng bóng",
          "Rèm vải nhung",
          "Tấm mút xốp",
          "Bao cát"
        ],
        "correct": 0,
        "explanation": "Mặt gương phẳng bóng phản xạ âm rất tốt."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Biện pháp nào sau đây giúp giảm tiếng ồn tại nguồn âm?",
        "options": [
          "Gắn ống xả giảm thanh cho động cơ xe máy",
          "Trồng cây xanh",
          "Đeo nút tai",
          "Lắp kính hai lớp"
        ],
        "correct": 0,
        "explanation": "Ống giảm thanh giảm ồn tại nguồn phát."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các đặc tính vật lý của sóng âm:",
        "statements": [
          {
            "subId": "a",
            "text": "Sóng âm là sóng cơ học lan truyền trong môi trường đàn hồi.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Âm thanh không truyền được trong môi trường chân không.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ âm trong thép lớn hơn tốc độ âm trong không khí.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tai người có thể nghe được âm thanh ở mọi tần số từ 0 đến vô cùng.",
            "correct": false
          }
        ],
        "explanation": "Tai người chỉ nghe được dải tần số 16 Hz - 20.000 Hz."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về mối quan hệ giữa độ to và biên độ âm:",
        "statements": [
          {
            "subId": "a",
            "text": "Độ to của âm được đo bằng đơn vị Decibel (dB).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Biên độ dao động càng lớn thì âm nghe càng to.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tiếng nói thầm thì có độ to khoảng 80 dB.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Ngưỡng đau màng nhĩ của tai người là khoảng 130 dB.",
            "correct": true
          }
        ],
        "explanation": "Nói thì thầm chỉ khoảng 20 - 30 dB (80 dB là tiếng xe cộ rất to)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một người gõ một tiếng búa vào đầu thanh ray đường sắt bằng thép dài 680 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc độ truyền âm trong thép khoảng 5100 m/s.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thời gian âm truyền qua thanh ray thép là xấp xỉ 0,133 giây.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thời gian âm truyền qua không khí (v = 340 m/s) là 2,0 giây.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Người ở đầu kia nghe thấy âm truyền qua không khí trước âm truyền qua thép.",
            "correct": false
          }
        ],
        "explanation": "Âm truyền qua thép (rắn) tới trước rất nhanh so với qua không khí."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Các biện pháp chống ô nhiễm tiếng ồn trong đời sống đô thị:",
        "statements": [
          {
            "subId": "a",
            "text": "Trồng cây xanh ven đường làm tán xạ phân tán sóng âm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Lắp cửa kính cách âm hai lớp ngăn chặn đường truyền âm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sử dụng vật liệu tiêu âm trong phòng thu âm để triệt tiêu tiếng vang.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Xây dựng các nhà máy cưa sắt thép ngay cạnh bệnh viện trung tâm.",
            "correct": false
          }
        ],
        "explanation": "Nhà máy phát tiếng ồn lớn phải xây dựng xa khu dân cư và bệnh viện."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một vật dao động thực hiện 160 dao động trong 4 giây. Tần số dao động là bao nhiêu Hz?",
        "correctAnswer": "40",
        "explanation": "f = 160 / 4 = 40 Hz."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Sóng âm có tần số 5 Hz thuộc vùng nào? (Hạ âm hay Siêu âm)",
        "correctAnswer": "Hạ âm",
        "explanation": "f < 16 Hz là hạ âm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khoảng cách từ người đến vách núi là 170 m. Sau bao lâu người đó nghe thấy tiếng vang? (v = 340 m/s)",
        "correctAnswer": "1",
        "explanation": "t = 2 × 170 / 340 = 1 s."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Âm thanh truyền trong nước biển với tốc độ 1500 m/s trong 1,2 giây. Quãng đường âm đi được là bao nhiêu mét?",
        "correctAnswer": "1800",
        "explanation": "s = 1500 × 1,2 = 1800 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Khoảng cách ngắn nhất để nghe được tiếng vang trong không khí là bao nhiêu mét? (Làm tròn 1 chữ số)",
        "correctAnswer": "11.3",
        "explanation": "11,3 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Đơn vị đo tần số dao động viết tắt là gì?",
        "correctAnswer": "Hz",
        "explanation": "Hertz (Hz)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước vách đá cách 136 m và hét to. Biết tốc độ âm trong không khí là 340 m/s. Sau bao lâu người đó nghe thấy tiếng vang dội lại?",
        "options": [
          "0,8 giây",
          "0,4 giây",
          "1,0 giây",
          "1,2 giây"
        ],
        "correct": 0,
        "explanation": "t = 2 × 136 / 340 = 0,8 s."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người đứng tại một điểm nhìn thấy tia chớp rồi sau 5,0 giây nghe thấy tiếng sấm rền vang. Biết v = 340 m/s. Điểm sét đánh cách người đó bao nhiêu mét?",
        "options": [
          "1700 m",
          "1500 m",
          "2000 m",
          "1360 m"
        ],
        "correct": 0,
        "explanation": "s = 340 × 5 = 1700 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một thiết bị phát sóng siêu âm sonar trên tàu ngầm gửi xung âm xuống đáy biển và thu lại tín hiệu sau 1,5 giây. Biết tốc độ âm trong nước là 1500 m/s. Độ sâu đáy biển là:",
        "options": [
          "1125 m",
          "2250 m",
          "1500 m",
          "1000 m"
        ],
        "correct": 0,
        "explanation": "d = 1500 × 1,5 / 2 = 1125 m."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tại sao khi nói chuyện trong hang đá rộng, tiếng nói nghe vang và kéo dài rền rĩ?",
        "options": [
          "Do âm thanh phản xạ liên tiếp nhiều lần qua lại giữa các vách đá trong hang tới tai ở các thời điểm khác nhau",
          "Do hang đá có ma thuật",
          "Do hang đá tự phát âm",
          "Do không khí đứng yên"
        ],
        "correct": 0,
        "explanation": "Âm phản xạ nhiều lần tạo chuỗi tiếng vang kéo dài."
      }
    ]
  },
  "phys7_c4_rev_test5": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương IV - Đề số 05",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c4",
    "chapterTitle": "Chương IV: Âm thanh",
    "lessonId": "phys7_c4_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương IV",
    "testNum": 5,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Bộ phận dao động phát ra âm thanh của chiếc đàn ghita khi chơi là:",
        "options": [
          "Các sợi dây đàn",
          "Thùng đàn",
          "Cần đàn",
          "Phím đàn"
        ],
        "correct": 0,
        "explanation": "Dây đàn dao động là nguồn âm chính."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong môi trường nào sau đây âm thanh truyền đi chậm nhất (khác 0)?",
        "options": [
          "Chất khí (không khí)",
          "Chất lỏng (nước)",
          "Chất rắn (thép)",
          "Chất rắn (gỗ)"
        ],
        "correct": 0,
        "explanation": "Tốc độ âm trong chất khí chậm nhất."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Âm nghe càng bổng khi nguồn âm dao động có:",
        "options": [
          "Tần số càng lớn",
          "Tần số càng nhỏ",
          "Biên độ càng nhỏ",
          "Biên độ càng lớn"
        ],
        "correct": 0,
        "explanation": "Tần số lớn thì âm bổng."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Âm nghe càng to khi nguồn âm dao động có:",
        "options": [
          "Biên độ càng lớn",
          "Biên độ càng nhỏ",
          "Tần số càng nhỏ",
          "Tần số càng lớn"
        ],
        "correct": 0,
        "explanation": "Biên độ lớn thì âm to."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Dải tần số tai người bình thường nghe được là:",
        "options": [
          "16 Hz đến 20.000 Hz",
          "Dưới 16 Hz",
          "Trên 20.000 Hz",
          "Từ 0 đến 100 Hz"
        ],
        "correct": 0,
        "explanation": "Dải nghe được: 16 - 20.000 Hz."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hiện tượng âm dội ngược trở lại khi gặp mặt chắn gọi là:",
        "options": [
          "Sự phản xạ âm",
          "Sự khúc xạ âm",
          "Sự truyền thẳng",
          "Sự hấp thụ âm"
        ],
        "correct": 0,
        "explanation": "Phản xạ âm khi gặp mặt chắn."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một vật dao động thực hiện 450 dao động trong 9 giây. Tần số dao động là:",
        "options": [
          "50 Hz",
          "4050 Hz",
          "45 Hz",
          "5 Hz"
        ],
        "correct": 0,
        "explanation": "f = 450 / 9 = 50 Hz."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Âm thanh có tần số 50.000 Hz thuộc dải sóng nào?",
        "options": [
          "Sóng siêu âm",
          "Sóng hạ âm",
          "Âm nghe được",
          "Sóng ánh sáng"
        ],
        "correct": 0,
        "explanation": "f > 20.000 Hz là siêu âm."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Nhìn thấy tia chớp rồi 2,0 giây sau nghe thấy tiếng sấm (v = 340 m/s). Nơi sét đánh cách xa:",
        "options": [
          "680 m",
          "340 m",
          "1020 m",
          "1500 m"
        ],
        "correct": 0,
        "explanation": "s = 340 × 2 = 680 m."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khoảng cách ngắn nhất từ người đến vật cản để nghe tiếng vang trong không khí là:",
        "options": [
          "Khoảng 11,3 m",
          "Khoảng 5,0 m",
          "Khoảng 20,0 m",
          "Khoảng 34,0 m"
        ],
        "correct": 0,
        "explanation": "d_min ≈ 11,3 m."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Vật liệu nào sau đây dùng để tiêu âm hiệu quả nhất trong phòng karaoke?",
        "options": [
          "Tấm mút xốp tổ ong",
          "Tấm gương kính",
          "Tấm nhôm",
          "Tường xi măng bóng"
        ],
        "correct": 0,
        "explanation": "Mút xốp tiêu âm tốt nhất."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Biện pháp nào sau đây ngăn chặn tiếng ồn truyền vào phòng học?",
        "options": [
          "Đóng kín cửa và lắp cửa kính cách âm",
          "Bật quạt to",
          "Bật loa to",
          "Mở hết cửa sổ"
        ],
        "correct": 0,
        "explanation": "Cửa kính kín cách âm ngăn chặn tiếng ồn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về bản chất dao động và sự truyền sóng âm:",
        "statements": [
          {
            "subId": "a",
            "text": "Nguồn âm là vật phát ra âm thanh do đang dao động.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chân không không có các hạt phân tử nên không truyền được sóng âm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ truyền âm trong chất lỏng nhỏ hơn trong chất khí.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Sóng âm mang theo năng lượng khi truyền đi.",
            "correct": true
          }
        ],
        "explanation": "Tốc độ âm trong lỏng lớn hơn trong khí (1500 m/s > 340 m/s)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các đặc tính cao độ và độ to của âm:",
        "statements": [
          {
            "subId": "a",
            "text": "Tần số dao động càng lớn thì âm phát ra càng bổng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Biên độ dao động càng lớn thì âm phát ra càng to.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đơn vị đo tần số là Hertz (Hz).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Âm có tần số 10.000 Hz nghe trầm hơn âm có tần số 100 Hz.",
            "correct": false
          }
        ],
        "explanation": "10.000 Hz bổng hơn nhiều so với 100 Hz."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát thí nghiệm phản xạ âm trong phòng lớn trống trải:",
        "statements": [
          {
            "subId": "a",
            "text": "Người hét to cách bức tường 51 m nghe thấy tiếng vang sau 0,3 giây.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bức tường cứng nhẵn phản xạ âm rất tốt.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu treo các tấm rèm nhung dày khắp tường thì tiếng vang bị giảm hẳn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu đứng cách tường 2 m thì vẫn nghe thấy tiếng vang tách rời.",
            "correct": false
          }
        ],
        "explanation": "Cách 2 m âm phản xạ về sau 0,012 s < 1/15 s nên không tạo tiếng vang tách rời."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng và tác hại của âm thanh trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Sóng siêu âm dùng để chẩn đoán hình ảnh y khoa an toàn cho con người.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dơi dùng sóng siêu âm định vị tránh va chạm trong đêm tối.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tiếng ồn kéo dài trên 85 dB không ảnh hưởng gì đến sức khỏe.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Trồng cây xanh tán rộng ven đường giúp giảm thiểu ô nhiễm tiếng ồn.",
            "correct": true
          }
        ],
        "explanation": "Tiếng ồn trên 85 dB kéo dài gây hại cho thính giác và thần kinh."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một vật thực hiện 200 dao động trong 4 giây. Tần số dao động là bao nhiêu Hz?",
        "correctAnswer": "50",
        "explanation": "f = 200 / 4 = 50 Hz."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Âm thanh có tần số 30.000 Hz là hạ âm hay siêu âm?",
        "correctAnswer": "Siêu âm",
        "explanation": "f > 20.000 Hz là siêu âm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Người nhìn thấy tia chớp rồi 4,0 giây sau nghe tiếng sấm. Điểm sét đánh cách người đó bao nhiêu mét? (v = 340 m/s)",
        "correctAnswer": "1360",
        "explanation": "s = 340 × 4 = 1360 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khoảng cách từ người đến vách núi là 204 m. Sau bao nhiêu giây người đó nghe thấy tiếng vang? (v = 340 m/s)",
        "correctAnswer": "1.2",
        "explanation": "t = 2 × 204 / 340 = 1,2 s."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Máy đo siêu âm phát xung âm xuống biển thu lại sau 0,4 giây. Độ sâu biển là bao nhiêu mét? (v = 1500 m/s)",
        "correctAnswer": "300",
        "explanation": "d = 1500 × 0,4 / 2 = 300 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Khoảng cách ngắn nhất giữa người và tường để nghe tiếng vang trong không khí là bao nhiêu mét? (Làm tròn 1 chữ số)",
        "correctAnswer": "11.3",
        "explanation": "11,3 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước vách đá cách 170 m hét to một tiếng. Sau bao lâu người đó nghe thấy tiếng vang dội lại? (v = 340 m/s)",
        "options": [
          "1,0 giây",
          "0,5 giây",
          "2,0 giây",
          "1,5 giây"
        ],
        "correct": 0,
        "explanation": "t = 2 × 170 / 340 = 1,0 s."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người gõ búa vào thanh ray thép dài 1530 m. Người thứ hai áp tai vào đầu kia của ray nghe thấy tiếng gõ truyền qua thanh ray thép sau 0,3 giây. Tốc độ truyền âm trong thép của thanh ray là:",
        "options": [
          "5100 m/s",
          "3400 m/s",
          "4500 m/s",
          "6000 m/s"
        ],
        "correct": 0,
        "explanation": "v = 1530 / 0,3 = 5100 m/s."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tại sao các phòng hòa nhạc thính phòng thường được thiết kế trần nhà và các bức tường lồi lõm zích zắc không theo mặt phẳng đều?",
        "options": [
          "Để tán xạ sóng âm theo nhiều hướng ngẫu nhiên, giúp âm thanh phân bố đồng đều khắp khán phòng mà không bị dội tiếng vang tập trung vào một điểm",
          "Để phòng hòa nhạc trông lạ mắt",
          "Để chống sét",
          "Để phòng mát hơn"
        ],
        "correct": 0,
        "explanation": "Tán xạ âm giúp trường âm thanh đồng đều khắp phòng khán giả."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tàu đánh cá sử dụng thiết bị dò cá bằng sóng siêu âm (v = 1500 m/s). Sóng siêu âm phát ra gặp đàn cá phản xạ trở lại sau 0,08 giây. Đàn cá đang bơi ở độ sâu cách tàu bao nhiêu mét?",
        "options": [
          "60 m",
          "120 m",
          "30 m",
          "90 m"
        ],
        "correct": 0,
        "explanation": "d = 1500 × 0,08 / 2 = 60 m."
      }
    ]
  },
  "phys7_c5_b15_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 15: Ánh sáng, tia sáng - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b15",
    "lessonName": "Bài 15: Ánh sáng, tia sáng",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Ta nhận biết được ánh sáng khi:",
        "options": [
          "Có ánh sáng truyền vào mắt ta",
          "Mắt ta mở to trong bóng tối",
          "Vật được chiếu sáng",
          "Xung quanh có nguồn điện"
        ],
        "correct": 0,
        "explanation": "Mắt nhận biết ánh sáng khi có ánh sáng lọt vào mắt."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Ta nhìn thấy một vật khi:",
        "options": [
          "Có ánh sáng từ vật đó truyền vào mắt ta",
          "Vật đó có kích thước rất lớn",
          "Vật đó phát ra ánh sáng",
          "Mắt ta phát ra tia sáng chiếu đến vật"
        ],
        "correct": 0,
        "explanation": "Điều kiện nhìn thấy vật là có ánh sáng từ vật truyền tới mắt."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Nguồn sáng là vật:",
        "options": [
          "Tự nó phát ra ánh sáng",
          "Hắt lại ánh sáng chiếu vào nó",
          "Có màu sắc rực rỡ",
          "Trong suốt"
        ],
        "correct": 0,
        "explanation": "Nguồn sáng là vật tự phát ra ánh sáng."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Vật nào sau đây là nguồn sáng?",
        "options": [
          "Ngọn nến đang cháy sáng",
          "Mặt Trăng trong đêm rằm",
          "Tấm gương soi",
          "Quyển sách trên bàn"
        ],
        "correct": 0,
        "explanation": "Ngọn nến đang cháy tự phát sáng; Mặt Trăng hắt lại ánh sáng Mặt Trời."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường nào?",
        "options": [
          "Đường thẳng",
          "Đường cong parabol",
          "Đường gấp khúc",
          "Đường tròn"
        ],
        "correct": 0,
        "explanation": "Định luật truyền thẳng ánh sáng."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Quy ước biểu diễn đường truyền của ánh sáng bằng một đường thẳng có mũi tên chỉ hướng truyền được gọi là:",
        "options": [
          "Tia sáng",
          "Chùm sáng",
          "Pháp tuyến",
          "Vùng tối"
        ],
        "correct": 0,
        "explanation": "Tia sáng được biểu diễn bằng đường thẳng có mũi tên chỉ hướng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Vật nào sau đây là vật sáng nhưng KHÔNG PHẢI là nguồn sáng?",
        "options": [
          "Mặt Trăng",
          "Mặt Trời",
          "Ngọn đuốc đang cháy",
          "Đèn LED đang sáng"
        ],
        "correct": 0,
        "explanation": "Mặt Trăng là vật sáng vì hắt lại ánh sáng Mặt Trời, không tự phát sáng."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chùm sáng gồm các tia sáng song song với nhau trên đường truyền được gọi là:",
        "options": [
          "Chùm sáng song song",
          "Chùm sáng hội tụ",
          "Chùm sáng phân kì",
          "Chùm sáng cầu"
        ],
        "correct": 0,
        "explanation": "Chùm sáng song song."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Vùng phía sau vật cản hoàn toàn không nhận được ánh sáng từ nguồn sáng truyền tới được gọi là:",
        "options": [
          "Vùng bóng tối",
          "Vùng bóng nửa tối",
          "Vùng sáng",
          "Vùng chạng vạng"
        ],
        "correct": 0,
        "explanation": "Vùng bóng tối không nhận được bất kì ánh sáng nào từ nguồn sáng."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Hiện tượng Nhật thực xảy ra khi:",
        "options": [
          "Mặt Trăng nằm ở khoảng giữa Mặt Trời và Trái Đất",
          "Trái Đất nằm ở giữa Mặt Trời và Mặt Trăng",
          "Mặt Trời nằm giữa Trái Đất và Mặt Trăng",
          "Vào ban đêm trăng tròn"
        ],
        "correct": 0,
        "explanation": "Nhật thực xảy ra khi Mặt Trăng che khuất Mặt Trời chiếu xuống Trái Đất."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Chùm sáng phát ra từ một chiếc đèn pin chiếu xa có dạng là:",
        "options": [
          "Chùm sáng phân kì loe rộng dần ra",
          "Chùm sáng song song tuyệt đối",
          "Chùm sáng hội tụ về một điểm",
          "Chùm sáng zích zắc"
        ],
        "correct": 0,
        "explanation": "Chùm sáng đèn pin loe rộng ra là chùm phân kì."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hiện tượng Nguyệt thực xảy ra khi:",
        "options": [
          "Trái Đất nằm ở khoảng giữa Mặt Trời và Mặt Trăng",
          "Mặt Trăng nằm giữa Mặt Trời và Trái Đất",
          "Mặt Trời bị mây che",
          "Vào ban ngày"
        ],
        "correct": 0,
        "explanation": "Trái Đất che khuất ánh sáng Mặt Trời chiếu đến Mặt Trăng tạo ra nguyệt thực."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về điều kiện nhìn thấy vật và bản chất của nguồn sáng:",
        "statements": [
          {
            "subId": "a",
            "text": "Ban đêm trong phòng kín tối đen, ta không nhìn thấy đồ vật vì không có ánh sáng từ vật truyền vào mắt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bật đèn sáng lên, đèn chiếu sáng đồ vật và đồ vật hắt ánh sáng vào mắt giúp ta nhìn thấy vật.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Mắt người có khả năng tự phát ra ánh sáng chiếu sáng các vật xung quanh.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Vật sáng bao gồm cả nguồn sáng và các vật hắt lại ánh sáng.",
            "correct": true
          }
        ],
        "explanation": "Mắt người là thụ cảm quang học, không tự phát ra ánh sáng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về định luật truyền thẳng ánh sáng và các hệ quả:",
        "statements": [
          {
            "subId": "a",
            "text": "Ánh sáng chỉ truyền theo đường thẳng khi môi trường trong suốt và đồng tính.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong môi trường không khí bị khói bụi hoặc nước có váng dầu không đồng nhất, ánh sáng có thể bị bẻ cong.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Người thợ xây ngắm đường thẳng bằng cách dùng mắt ngắm thẳng hàng là ứng dụng định luật truyền thẳng ánh sáng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bóng tối của vật cản được hình thành là do ánh sáng có thể tự uốn cong vòng qua vật cản.",
            "correct": false
          }
        ],
        "explanation": "Bóng tối hình thành do ánh sáng truyền thẳng, bị vật cản chặn lại không truyền qua được."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Thí nghiệm dùng đèn pin nhỏ (nguồn sáng hẹp) chiếu vào một quả bóng bàn đặt trước một màn chắn:",
        "statements": [
          {
            "subId": "a",
            "text": "Phía sau quả bóng bàn trên màn chắn xuất hiện một vùng tròn bóng tối rõ nét.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Xung quanh vùng bóng tối này không có vùng bóng nửa tối khi dùng nguồn sáng điểm nhỏ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu dịch chuyển quả bóng bàn lại gần màn chắn hơn thì kích thước bóng tối trên màn sẽ thu nhỏ lại.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu thay quả bóng bàn bằng một tấm kính thủy tinh trong suốt thì bóng tối trên màn vẫn đậm đặc như cũ.",
            "correct": false
          }
        ],
        "explanation": "Kính thủy tinh trong suốt cho ánh sáng truyền qua nên không tạo bóng tối đậm đặc."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hiện tượng Nhật thực và Nguyệt thực trong thiên văn học:",
        "statements": [
          {
            "subId": "a",
            "text": "Nhật thực chỉ có thể xảy ra vào ban ngày khi có trăng mới (đầu tháng âm lịch).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nguyệt thực chỉ có thể xảy ra vào ban đêm khi trăng tròn (ngày rằm âm lịch).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Người đứng ở vùng bóng tối của Mặt Trăng trên Trái Đất sẽ quan sát được Nhật thực toàn phần.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hiện tượng Nhật thực chứng tỏ ánh sáng truyền đi theo đường cong xoắn ốc.",
            "correct": false
          }
        ],
        "explanation": "Nhật thực là minh chứng thực tế rõ nét cho định luật truyền thẳng ánh sáng."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Mặt Trời là nguồn sáng hay vật được chiếu sáng?",
        "correctAnswer": "Nguồn sáng",
        "explanation": "Mặt Trời tự phát sáng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Mặt Trăng là nguồn sáng hay vật sáng?",
        "correctAnswer": "Vật sáng",
        "explanation": "Mặt Trăng là vật sáng (hắt lại ánh sáng)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong môi trường trong suốt và đồng tính, ánh sáng truyền theo đường gì?",
        "correctAnswer": "Đường thẳng",
        "explanation": "Đường thẳng."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Chùm sáng có các tia sáng xuất phát từ cùng một điểm và loe rộng ra gọi là chùm sáng gì?",
        "correctAnswer": "Phân kì",
        "explanation": "Chùm sáng phân kì."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Tốc độ truyền ánh sáng trong chân không là bao nhiêu nghìn km/s?",
        "correctAnswer": "300",
        "explanation": "300.000 km/s = 300 nghìn km/s."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Hiện tượng Mặt Trăng nằm giữa Mặt Trời và Trái Đất tạo ra hiện tượng gì? (Nhật thực hay Nguyệt thực)",
        "correctAnswer": "Nhật thực",
        "explanation": "Nhật thực."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Để kiểm tra xem một hàng cọc rào có được cắm thẳng hàng trên bãi đất hay không, một người thợ ngắm bằng mắt dọc theo hàng cọc. Nếu người đó nhìn cọc thứ nhất mà cọc này che khuất hoàn toàn cọc thứ hai và cọc thứ ba thì kết luận nào sau đây đúng?",
        "options": [
          "Ba cọc rào đã được cắm thẳng hàng vì ánh sáng truyền thẳng từ các cọc sau bị cọc trước chắn lại",
          "Hàng cọc bị cong",
          "Cọc thứ nhất ngắn hơn",
          "Không thể kết luận được"
        ],
        "correct": 0,
        "explanation": "Ứng dụng định luật truyền thẳng ánh sáng: các cọc che khuất nhau nghĩa là chúng thẳng hàng."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tại sao khi làm phẫu thuật trong phòng mổ, người ta không sử dụng bóng đèn tròn thông thường mà lại sử dụng hệ thống đèn mổ gồm nhiều bóng đèn nhỏ bố trí xung quanh một vành tròn lớn?",
        "options": [
          "Để tạo ra chùm sáng rộng triệt tiêu vùng bóng tối dưới bàn tay và dụng cụ của bác sĩ phẫu thuật (đèn không hắt bóng)",
          "Để phòng mổ thật nóng",
          "Để tiết kiệm điện",
          "Để trang trí thẩm mỹ"
        ],
        "correct": 0,
        "explanation": "Đèn mổ không bóng tạo ra nhiều nguồn sáng rộng khiến vùng bóng tối dưới tay bác sĩ bị triệt tiêu hoàn toàn thành bóng nửa tối mờ nhạt."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một cột cờ cao 6 mét dựng thẳng đứng trên mặt sân phẳng. Vào một thời điểm trời nắng, bóng của cột cờ in trên mặt sân có chiều dài 8 mét. Cùng lúc đó, một chiếc cọc sắt dựng thẳng đứng có bóng in trên sân dài 2 mét. Chiều cao của chiếc cọc sắt đó là:",
        "options": [
          "1,5 mét",
          "2,0 mét",
          "3,0 mét",
          "1,2 mét"
        ],
        "correct": 0,
        "explanation": "Tỉ lệ chiều cao / chiều dài bóng: h_cờ / s_cờ = 6 / 8 = 0,75 => h_cọc = 2 × 0,75 = 1,5 m."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người đứng dưới ánh sáng của một cột đèn đường cao vào ban đêm. Khi người này bước đi ra xa dần khỏi cột đèn thì chiều dài bóng của người đó trên mặt đất sẽ:",
        "options": [
          "Dài dần ra",
          "Ngắn dần lại",
          "Không đổi",
          "Biến mất hoàn toàn"
        ],
        "correct": 0,
        "explanation": "Khi ra xa chân đèn, góc tới của tia sáng giới hạn tạo bóng phẳng hơn, làm chiều dài bóng trên mặt đất dài ra."
      }
    ]
  },
  "phys7_c5_b15_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 15: Ánh sáng, tia sáng - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b15",
    "lessonName": "Bài 15: Ánh sáng, tia sáng",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật nào dưới đây được coi là nguồn sáng tự nhiên?",
        "options": [
          "Mặt Trời",
          "Đèn pin",
          "Bóng đèn huỳnh quang",
          "Màn hình tivi"
        ],
        "correct": 0,
        "explanation": "Mặt Trời là nguồn sáng tự nhiên vô tận."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Con người nhận biết được ánh sáng nhờ cơ quan thụ cảm nào?",
        "options": [
          "Mắt (thị giác)",
          "Tai (thính giác)",
          "Mũi (khứu giác)",
          "Da (xúc giác)"
        ],
        "correct": 0,
        "explanation": "Mắt là cơ quan thụ cảm ánh sáng."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chùm sáng hội tụ là chùm sáng gồm các tia sáng:",
        "options": [
          "Giao nhau tại một điểm trên đường truyền của chúng",
          "Song song với nhau",
          "Loe rộng dần ra",
          "Không bao giờ cắt nhau"
        ],
        "correct": 0,
        "explanation": "Chùm hội tụ giao nhau tại một điểm tiêu điểm."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong môi trường nước trong suốt và đồng chất, ánh sáng truyền theo đường nào?",
        "options": [
          "Đường thẳng",
          "Đường gấp khúc",
          "Đường cong tròn",
          "Đường lượn sóng"
        ],
        "correct": 0,
        "explanation": "Môi trường trong suốt đồng tính thì ánh sáng truyền thẳng."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Đom đóm đực phát sáng lập lòe trong đêm mùa hè là một ví dụ về:",
        "options": [
          "Nguồn sáng sinh học",
          "Vật phản xạ ánh sáng",
          "Vật hấp thụ ánh sáng",
          "Gương phẳng"
        ],
        "correct": 0,
        "explanation": "Đom đóm tự phát sáng nhờ phản ứng sinh hóa, là nguồn sáng sinh học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Vùng bóng nửa tối là vùng:",
        "options": [
          "Chỉ nhận được một phần ánh sáng từ nguồn sáng truyền tới",
          "Hoàn toàn tối đen không nhận được ánh sáng",
          "Nhận được toàn bộ ánh sáng",
          "Sáng rực rỡ"
        ],
        "correct": 0,
        "explanation": "Vùng bóng nửa tối nhận một phần ánh sáng từ nguồn sáng rộng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Vì sao trong một căn phòng đóng kín cửa vào ban đêm ta lại không nhìn thấy chiếc bàn?",
        "options": [
          "Vì chiếc bàn không tự phát sáng và không có nguồn sáng chiếu vào để hắt ánh sáng tới mắt ta",
          "Vì chiếc bàn tàng hình",
          "Vì mắt ta bị hỏng",
          "Vì chiếc bàn biến thành màu đen"
        ],
        "correct": 0,
        "explanation": "Không có ánh sáng từ chiếc bàn truyền vào mắt."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chùm sáng phát ra từ một chiếc đèn laser đồ chơi chiếu trên bảng là mô hình thực tế của:",
        "options": [
          "Tia sáng hẹp (hoặc chùm sáng song song rất mảnh)",
          "Chùm sáng phân kì rộng",
          "Chùm sáng hội tụ",
          "Nguồn sáng cầu"
        ],
        "correct": 0,
        "explanation": "Tia laser có chùm tia cực mảnh và song song, dùng làm mô hình tia sáng."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Khi Trái Đất đi vào vùng bóng tối hoàn toàn của Mặt Trăng, trên Trái Đất sẽ quan sát được hiện tượng:",
        "options": [
          "Nhật thực toàn phần",
          "Nguyệt thực toàn phần",
          "Nhật thực một phần",
          "Sao băng"
        ],
        "correct": 0,
        "explanation": "Vùng bóng tối của Mặt Trăng trên Trái Đất quan sát được Nhật thực toàn phần."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đặt một tấm bìa đục chắn trước ngọn nến đang cháy, phía sau tấm bìa đặt màn chắn. Trên màn chắn xuất hiện:",
        "options": [
          "Vùng bóng tối ở giữa bao quanh bởi vùng bóng nửa tối",
          "Vùng sáng đều",
          "Không có hiện tượng gì",
          "Toàn bộ màn chắn đều sáng rực"
        ],
        "correct": 0,
        "explanation": "Nguồn nến là nguồn sáng rộng nên tạo vùng bóng tối ở tâm và bóng nửa tối viền xung quanh."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tại sao người ta dùng ống ngắm laze trên súng thể thao bắn bia?",
        "options": [
          "Vì ánh sáng laser truyền thẳng giúp định vị đường ngắm bắn chuẩn xác",
          "Vì tia laser đẩy viên đạn bay nhanh hơn",
          "Vì tia laser làm bia phát sáng",
          "Vì tia laser làm súng nhẹ hơn"
        ],
        "correct": 0,
        "explanation": "Ứng dụng tính truyền thẳng của tia laser để định hướng đường ngắm thẳng."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hiện tượng bóng của cái cây trên sân trường thay đổi chiều dài từ sáng đến trưa rồi đến chiều là do:",
        "options": [
          "Vị trí của Mặt Trời trên bầu trời thay đổi làm góc chiếu của tia sáng thay đổi",
          "Cái cây lớn nhanh trong ngày",
          "Mặt đất bị nghiêng",
          "Không khí nóng lên"
        ],
        "correct": 0,
        "explanation": "Góc chiếu của tia sáng Mặt Trời thay đổi theo thời gian trong ngày."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về phân loại nguồn sáng và vật sáng trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Bóng đèn LED đang sáng là nguồn sáng nhân tạo.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mặt Trời và các ngôi sao tự phát sáng là các nguồn sáng tự nhiên.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tờ giấy trắng đặt dưới ánh đèn là vật sáng vì nó hắt lại ánh sáng của đèn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Mặt gương soi tự nó phát ra ánh sáng trong đêm tối mà không cần đèn.",
            "correct": false
          }
        ],
        "explanation": "Gương soi chỉ phản xạ ánh sáng, không thể tự phát sáng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các loại chùm sáng thường gặp:",
        "statements": [
          {
            "subId": "a",
            "text": "Chùm sáng song song gồm các tia sáng song song không bao giờ giao nhau.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chùm sáng hội tụ loe rộng dần trên đường truyền.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Chùm sáng phân kì loe rộng dần ra trên đường truyền.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Ánh sáng phát ra từ một ngọn đèn dầu là chùm sáng phân kì truyền theo mọi hướng.",
            "correct": true
          }
        ],
        "explanation": "Chùm hội tụ thu hẹp dần và giao nhau tại một điểm, chùm phân kì mới loe rộng ra."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát vùng bóng tối và bóng nửa tối phía sau một vật cản tròn:",
        "statements": [
          {
            "subId": "a",
            "text": "Nếu nguồn sáng là một điểm sáng rất nhỏ thì chỉ thu được vùng bóng tối rõ nét trên màn chắn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nếu nguồn sáng có kích thước lớn (như bóng đèn tuýp dài) thì sẽ xuất hiện cả vùng bóng tối và vùng bóng nửa tối.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Vùng bóng nửa tối là vùng hoàn toàn không có tia sáng nào chiếu tới.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Di chuyển màn chắn ra xa vật cản thì kích thước vùng bóng nửa tối sẽ mở rộng ra.",
            "correct": true
          }
        ],
        "explanation": "Vùng bóng nửa tối nhận được một phần ánh sáng từ nguồn sáng rộng."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Quan sát hiện tượng Nguyệt thực vào đêm rằm:",
        "statements": [
          {
            "subId": "a",
            "text": "Mặt Trăng đi vào vùng bóng tối của Trái Đất nên bị che khuất không nhận được ánh sáng Mặt Trời.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mọi người ở nửa Trái Đất quay về phía ban đêm đều có thể cùng quan sát được Nguyệt thực.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thời gian diễn ra hiện tượng Nguyệt thực thường dài hơn nhiều so với Nhật thực toàn phần.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hiện tượng Nguyệt thực xảy ra khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất.",
            "correct": false
          }
        ],
        "explanation": "Nguyệt thực xảy ra khi Trái Đất nằm ở giữa Mặt Trời và Mặt Trăng."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đom đóm lập lòe trong đêm là nguồn sáng hay vật được chiếu sáng?",
        "correctAnswer": "Nguồn sáng",
        "explanation": "Nguồn sáng sinh học."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Quyển sách nằm trên bàn ban ngày là nguồn sáng hay vật sáng?",
        "correctAnswer": "Vật sáng",
        "explanation": "Vật sáng (hắt lại ánh sáng)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Chùm sáng gồm các tia sáng giao nhau tại một điểm gọi là chùm sáng gì?",
        "correctAnswer": "Hội tụ",
        "explanation": "Chùm sáng hội tụ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khi Trái Đất nằm giữa Mặt Trời và Mặt Trăng sẽ xảy ra hiện tượng gì? (Nhật thực hay Nguyệt thực)",
        "correctAnswer": "Nguyệt thực",
        "explanation": "Nguyệt thực."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một chiếc cọc cao 1 mét cắm thẳng đứng trên sân phẳng có bóng nắng dài 1,5 mét. Một cái cây gần đó có bóng dài 6 mét. Cây cao bao nhiêu mét?",
        "correctAnswer": "4",
        "explanation": "h = 6 / 1,5 = 4 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Đường truyền của ánh sáng được biểu diễn bằng hình gì có mũi tên chỉ hướng?",
        "correctAnswer": "Đường thẳng",
        "explanation": "Đường thẳng có mũi tên chỉ hướng."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người muốn đóng một chiếc cọc thứ ba C thẳng hàng với hai chiếc cọc A và B đã cắm sẵn trên cánh đồng. Người đó đứng tại vị trí cọc A, nhìn về phía cọc B và cắm cọc C sao cho:",
        "options": [
          "Cọc B che khuất hoàn toàn cọc C đối với mắt đặt tại A",
          "Cọc C cao hơn cọc B",
          "Cọc C ở bên cạnh cọc B",
          "Cọc C phát sáng"
        ],
        "correct": 0,
        "explanation": "Ánh sáng truyền thẳng, nếu cọc B che khuất cọc C thì A, B, C thẳng hàng."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Vào những ngày nắng gắt, dưới bóng mát của các tán cây rậm rạp, ta thường quan sát thấy trên mặt đất có những đốm sáng hình tròn nhỏ li ti sáng rực rỡ. Nguồn gốc của các đốm sáng hình tròn này là:",
        "options": [
          "Hình ảnh thực của Mặt Trời (nguồn sáng hình cầu) được tạo bởi hiện tượng tạo ảnh qua lỗ kim từ các khe hở nhỏ giữa các kẽ lá",
          "Do gió thổi tròn lá",
          "Do bóng của lá cây hình tròn",
          "Do giọt nước đọng trên lá"
        ],
        "correct": 0,
        "explanation": "Hiện tượng máy ảnh lỗ kim (Pinhole camera) tự nhiên: khe lá nhỏ tạo ảnh thật của Mặt Trời hình tròn trên mặt đất."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một ngọn đèn đường treo ở độ cao 4 mét so với mặt đất. Một người cao 1,6 mét đứng cách cột đèn một khoảng 3 mét. Chiều dài bóng của người đó in trên mặt đất là:",
        "options": [
          "2,0 mét",
          "1,5 mét",
          "2,5 mét",
          "1,8 mét"
        ],
        "correct": 0,
        "explanation": "Gọi chiều dài bóng là x. Ta có: x / (x + 3) = 1,6 / 4 = 0,4 => x = 0,4x + 1,2 => 0,6x = 1,2 => x = 2,0 m."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tại sao khi xảy ra hiện tượng Nhật thực một phần, nếu nhìn trực tiếp bằng mắt thường hoặc qua kính râm thông thường thì có thể bị bỏng giác mạc và mù lòa vĩnh viễn?",
        "options": [
          "Vì cường độ bức xạ hồng ngoại và tử ngoại của Mặt Trời chiếu vào mắt cực mạnh làm cháy các tế bào võng mạc mà mắt không có phản xạ chớp",
          "Vì Mặt Trăng phát tia độc",
          "Vì không khí biến thành khí độc",
          "Vì bóng tối làm cay mắt"
        ],
        "correct": 0,
        "explanation": "Bức xạ mặt trời có năng lượng hội tụ vào đáy mắt làm cháy võng mạc mà không kịp chớp mắt tự vệ."
      }
    ]
  },
  "phys7_c5_b15_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 15: Ánh sáng, tia sáng - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b15",
    "lessonName": "Bài 15: Ánh sáng, tia sáng",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật nào sau đây KHÔNG PHẢI là nguồn sáng?",
        "options": [
          "Mặt Trăng",
          "Mặt Trời",
          "Ngọn nến đang cháy",
          "Bóng đèn neon đang sáng"
        ],
        "correct": 0,
        "explanation": "Mặt Trăng hắt lại ánh sáng từ Mặt Trời, không phải nguồn sáng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Ánh sáng từ Mặt Trời chiếu xuống Trái Đất truyền qua môi trường chân không ngoài vũ trụ chứng tỏ:",
        "options": [
          "Ánh sáng có thể truyền được trong môi trường chân không",
          "Chân không là chất lỏng",
          "Chân không hút ánh sáng",
          "Ánh sáng không có thật"
        ],
        "correct": 0,
        "explanation": "Ánh sáng là sóng điện từ truyền được hoàn hảo trong chân không."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chùm sáng phát ra từ một chiếc kính lúp khi để dưới ánh nắng Mặt Trời tụ lại thành một điểm sáng nhỏ rất nóng là chùm sáng:",
        "options": [
          "Hội tụ",
          "Phân kì",
          "Song song",
          "Tròn"
        ],
        "correct": 0,
        "explanation": "Tụ lại thành một điểm là chùm sáng hội tụ."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Định luật truyền thẳng ánh sáng chỉ nghiệm đúng trong điều kiện môi trường:",
        "options": [
          "Trong suốt và đồng tính (đồng nhất)",
          "Bất kì",
          "Có nhiều bụi bẩn",
          "Đang chuyển động hỗn loạn"
        ],
        "correct": 0,
        "explanation": "Môi trường phải trong suốt và đồng tính."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Mô hình biểu diễn tia sáng gồm:",
        "options": [
          "Một đoạn thẳng có mũi tên chỉ hướng truyền của ánh sáng",
          "Một hình tròn kín",
          "Một hình tam giác",
          "Một đường cong parabol"
        ],
        "correct": 0,
        "explanation": "Tia sáng biểu diễn bằng đường thẳng có mũi tên chỉ hướng."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Khi có Nhật thực toàn phần xảy ra, vùng tối trên bề mặt Trái Đất là nơi nhận được:",
        "options": [
          "Hoàn toàn không có ánh sáng trực tiếp từ Mặt Trời chiếu tới",
          "Toàn bộ ánh sáng Mặt Trời",
          "Một nửa ánh sáng",
          "Ánh sáng màu xanh"
        ],
        "correct": 0,
        "explanation": "Vùng bóng tối của Mặt Trăng không nhận ánh sáng trực tiếp từ Mặt Trời."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Vì sao người thợ mộc khi bào một thanh gỗ thường nhắm một mắt và ngắm dọc theo mép thanh gỗ?",
        "options": [
          "Để ứng dụng định luật truyền thẳng ánh sáng kiểm tra độ phẳng thẳng của mép gỗ",
          "Để thư giãn mắt",
          "Để thanh gỗ không bị bụi",
          "Để gỗ nhanh khô"
        ],
        "correct": 0,
        "explanation": "Ngắm thẳng hàng theo đường truyền thẳng của tia sáng."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chùm sáng phát ra từ đèn pha ô tô khi bật chế độ chiếu xa (đèn pha) xấp xỉ là chùm sáng:",
        "options": [
          "Song song",
          "Hội tụ",
          "Phân kì rất rộng",
          "Hình cầu"
        ],
        "correct": 0,
        "explanation": "Đèn pha ô tô dùng chóa phản xạ tạo chùm sáng song song chiếu xa."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Bóng nửa tối xuất hiện xung quanh bóng tối khi nguồn sáng là:",
        "options": [
          "Nguồn sáng có kích thước rộng",
          "Một điểm sáng cực nhỏ",
          "Mặt Trăng tròn",
          "Tia laser"
        ],
        "correct": 0,
        "explanation": "Nguồn sáng có kích thước lớn tạo vùng bóng nửa tối viền xung quanh."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khi đứng trước một ngọn đèn cao áp vào ban đêm, nếu ta giơ một bàn tay lên phía trước thì trên mặt đất xuất hiện bóng của bàn tay. Đó là do:",
        "options": [
          "Bàn tay là vật cản cản trở ánh sáng truyền thẳng từ đèn xuống mặt đất",
          "Bàn tay hút ánh sáng",
          "Đèn bị hỏng",
          "Không khí bị lạnh đi"
        ],
        "correct": 0,
        "explanation": "Ánh sáng truyền thẳng gặp bàn tay bị chặn lại tạo bóng tối trên đất."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Vào những đêm trăng rằm không mây, ta nhìn thấy Mặt Trăng tròn vành vạnh chiếu sáng bầu trời đêm. Ánh trăng đó bắt nguồn từ:",
        "options": [
          "Ánh sáng của Mặt Trời chiếu vào bề mặt Mặt Trăng rồi phản xạ (hắt lại) đến mắt ta trên Trái Đất",
          "Mặt Trăng tự cháy sáng",
          "Trái Đất chiếu sáng Mặt Trăng",
          "Mặt Trăng phát ra lân tinh"
        ],
        "correct": 0,
        "explanation": "Mặt Trăng là vật sáng phản chiếu ánh sáng Mặt Trời."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hiện tượng nguyệt thực toàn phần có thể kéo dài hàng giờ đồng hồ trong khi nhật thực toàn phần chỉ diễn ra trong vài phút là vì:",
        "options": [
          "Bóng tối của Trái Đất có kích thước lớn hơn rất nhiều so với bóng tối của Mặt Trăng",
          "Mặt Trời tắt đi",
          "Mặt Trăng bay rất nhanh",
          "Mặt Trăng nhỏ hơn hạt cát"
        ],
        "correct": 0,
        "explanation": "Kích thước Trái Đất lớn hơn Mặt Trăng rất nhiều nên vùng bóng tối Trái Đất bao trùm rộng lớn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các tính chất của sự truyền ánh sáng:",
        "statements": [
          {
            "subId": "a",
            "text": "Ánh sáng truyền đi trong không khí với tốc độ xấp xỉ 300.000 km/s.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi ánh sáng truyền qua mặt phân cách giữa không khí và nước thì tia sáng bị gãy khúc.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tia sáng luôn truyền theo đường thẳng trong mọi điều kiện môi trường bất kì.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Bóng tối là vùng hoàn toàn không nhận được ánh sáng từ nguồn sáng do vật cản chắn lại.",
            "correct": true
          }
        ],
        "explanation": "Ánh sáng chỉ truyền thẳng trong môi trường trong suốt và đồng tính."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các chùm sáng cơ bản trong quang học:",
        "statements": [
          {
            "subId": "a",
            "text": "Chùm sáng song song gồm các tia sáng song song nhau.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chùm sáng hội tụ gồm các tia sáng tiến lại gần nhau và giao nhau tại một điểm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chùm sáng phân kì loe rộng ra từ một điểm nguồn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Chùm sáng phát ra từ đèn pin là chùm sáng hội tụ.",
            "correct": false
          }
        ],
        "explanation": "Đèn pin phát ra chùm sáng phân kì loe rộng ra."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Ứng dụng định luật truyền thẳng ánh sáng trong đời sống và kĩ thuật:",
        "statements": [
          {
            "subId": "a",
            "text": "Người thợ xây căng một sợi dây rọi để xây tường thẳng đứng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Các vận động viên bắn súng ngắm qua đầu ruồi và khe ngắm thẳng hàng với tâm bia.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kính thiên văn quang học dùng để thu nhận ánh sáng từ các vì sao truyền qua không gian vũ trụ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đèn hải đăng chiếu chùm sáng phân kì thật rộng để rọi sáng đáy biển.",
            "correct": false
          }
        ],
        "explanation": "Đèn hải đăng tạo chùm sáng song song cực mạnh quét ngang mặt biển để báo hiệu cho tàu thuyền từ xa."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Quan sát hiện tượng Nhật thực trên Trái Đất:",
        "statements": [
          {
            "subId": "a",
            "text": "Nhật thực xảy ra khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất trên một đường thẳng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Vùng bóng tối của Mặt Trăng trên bề mặt Trái Đất chỉ quét qua một dải hẹp vài trăm kilômét.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Người ở vùng bóng nửa tối quan sát được Nhật thực một phần.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nhật thực có thể quan sát được vào lúc nửa đêm.",
            "correct": false
          }
        ],
        "explanation": "Nhật thực là Mặt Trời bị che khuất, chỉ quan sát được vào ban ngày."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Mặt Trời truyền ánh sáng đến Trái Đất qua môi trường gì ngoài không gian vũ trụ?",
        "correctAnswer": "Chân không",
        "explanation": "Môi trường chân không."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Chùm sáng có các tia sáng song song nhau gọi là chùm sáng gì?",
        "correctAnswer": "Song song",
        "explanation": "Chùm sáng song song."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất sẽ tạo ra hiện tượng gì? (Nhật thực hay Nguyệt thực)",
        "correctAnswer": "Nhật thực",
        "explanation": "Nhật thực."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường gì?",
        "correctAnswer": "Đường thẳng",
        "explanation": "Đường thẳng."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một chiếc cọc sắt cao 2 mét cắm thẳng đứng có bóng nắng trên sân dài 1 mét. Một tòa nhà gần đó có bóng dài 15 mét. Chiều cao của tòa nhà là bao nhiêu mét?",
        "correctAnswer": "30",
        "explanation": "h = 15 × 2 = 30 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Ánh sáng Mặt Trời truyền đến Trái Đất (khoảng cách 150 triệu km) với tốc độ 300.000 km/s mất thời gian bao nhiêu giây?",
        "correctAnswer": "500",
        "explanation": "t = 150.000.000 / 300.000 = 500 s."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người muốn cắm một hàng cọc gồm 4 chiếc A, B, C, D thẳng hàng nhau trên một bờ ruộng. Người đó đã cắm xong hai cọc A và D ở hai đầu. Để cắm hai cọc B và C nằm chính xác trên đường thẳng nối A và D, người đó nên làm thế nào?",
        "options": [
          "Đứng tại cọc A ngắm cọc D, sau đó cắm cọc B và C sao cho cọc trước che khuất cọc sau đối với mắt nhìn",
          "Cắm bừa rồi dùng dây kéo",
          "Đo bằng bước chân",
          "Đợi trời tối mới cắm"
        ],
        "correct": 0,
        "explanation": "Ứng dụng sự truyền thẳng của tia sáng: các cọc che khuất nhau trên đường ngắm."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tại sao khi chiếu đèn pin vào một quả cầu lớn đặt trước màn chắn, ta lại quan sát thấy trên màn chắn có một vùng tròn bóng tối đậm ở chính giữa và bao quanh bởi một dải bóng nửa tối nhạt dần ra ngoài?",
        "options": [
          "Vì bóng đèn pin là nguồn sáng có kích thước rộng, các tia sáng từ các điểm khác nhau của bóng đèn tạo ra vùng bóng nửa tối viền xung quanh vùng bóng tối",
          "Vì quả cầu phát ra ánh sáng",
          "Vì màn chắn bị rách",
          "Vì pin sắp hết"
        ],
        "correct": 0,
        "explanation": "Nguồn sáng rộng luôn tạo vùng bóng tối ở tâm và vùng bóng nửa tối ở rìa."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một ngọn đèn đường treo ở đỉnh cột đèn cao 6 mét. Một bạn học sinh cao 1,5 mét đứng cách chân cột đèn 6 mét. Chiều dài bóng của bạn học sinh in trên mặt đường bằng bao nhiêu mét?",
        "options": [
          "2 mét",
          "1,5 mét",
          "3 mét",
          "2,5 mét"
        ],
        "correct": 0,
        "explanation": "Gọi bóng là x. Ta có x / (x + 6) = 1,5 / 6 = 1/4 => 4x = x + 6 => 3x = 6 => x = 2 mét."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Nhà thiên văn học Eratosthenes thời Hy Lạp cổ đại đã đo được chu vi Trái Đất xấp xỉ 40.000 km chỉ bằng cách đo bóng nắng của một chiếc cọc tại hai thành phố Alexandria và Syene vào buổi trưa ngày Hạ chí. Cơ sở khoa học nền tảng mà ông đã sử dụng là:",
        "options": [
          "Định luật truyền thẳng ánh sáng và các tia sáng Mặt Trời chiếu tới Trái Đất coi như các đường thẳng song song",
          "Định luật phản xạ ánh sáng",
          "Định luật bảo toàn năng lượng",
          "Thuyết tương đối"
        ],
        "correct": 0,
        "explanation": "Tia sáng mặt trời chiếu song song kết hợp bóng của cọc thẳng đứng và định luật truyền thẳng ánh sáng."
      }
    ]
  },
  "phys7_c5_b16_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 16: Sự phản xạ ánh sáng - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b16",
    "lessonName": "Bài 16: Sự phản xạ ánh sáng",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hiện tượng tia sáng khi gặp mặt phân cách giữa hai môi trường trong suốt bị hắt ngược trở lại môi trường ban đầu được gọi là:",
        "options": [
          "Hiện tượng phản xạ ánh sáng",
          "Hiện tượng khúc xạ ánh sáng",
          "Hiện tượng tán sắc ánh sáng",
          "Hiện tượng hấp thụ ánh sáng"
        ],
        "correct": 0,
        "explanation": "Hiện tượng phản xạ ánh sáng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đường thẳng vuông góc với mặt gương tại điểm tới I được gọi là:",
        "options": [
          "Đường pháp tuyến (pháp tuyến tại điểm tới)",
          "Tia tới",
          "Tia phản xạ",
          "Mặt phẳng tới"
        ],
        "correct": 0,
        "explanation": "Đường pháp tuyến IN vuông góc với mặt gương."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Góc tới (kí hiệu i) là góc tạo bởi:",
        "options": [
          "Tia tới SI và đường pháp tuyến IN",
          "Tia tới SI và mặt gương",
          "Tia phản xạ IR và mặt gương",
          "Tia phản xạ IR và tia tới SI"
        ],
        "correct": 0,
        "explanation": "Góc tới i = góc(SIN)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Theo định luật phản xạ ánh sáng, góc phản xạ (r) và góc tới (i) luôn có mối quan hệ:",
        "options": [
          "Góc phản xạ bằng góc tới (r = i)",
          "Góc phản xạ lớn hơn góc tới (r > i)",
          "Góc phản xạ nhỏ hơn góc tới (r < i)",
          "r + i = 90 độ"
        ],
        "correct": 0,
        "explanation": "Định luật phản xạ ánh sáng: r = i."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Mặt phẳng tới là mặt phẳng chứa:",
        "options": [
          "Tia tới và đường pháp tuyến của gương tại điểm tới",
          "Tia phản xạ và mặt gương",
          "Tia tới và mặt gương",
          "Đường pháp tuyến và mặt gương"
        ],
        "correct": 0,
        "explanation": "Mặt phẳng tới chứa tia tới và pháp tuyến tại điểm tới."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hiện tượng ánh sáng phản xạ theo nhiều hướng hỗn loạn khi gặp bề mặt gồ ghề, nhám được gọi là:",
        "options": [
          "Hiện tượng phản xạ khuếch tán (tán xạ)",
          "Hiện tượng phản xạ gương",
          "Hiện tượng khúc xạ",
          "Hiện tượng bóng tối"
        ],
        "correct": 0,
        "explanation": "Phản xạ khuếch tán xảy ra trên bề mặt gồ ghề nhám."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Chiếu một tia sáng tới mặt gương phẳng với góc tới i = 40 độ. Góc phản xạ r có giá trị bằng:",
        "options": [
          "40 độ",
          "50 độ",
          "80 độ",
          "20 độ"
        ],
        "correct": 0,
        "explanation": "r = i = 40 độ."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chiếu một tia sáng tới vuông góc với mặt gương phẳng (góc tới i = 0 độ). Góc phản xạ có giá trị bằng:",
        "options": [
          "0 độ (tia phản xạ bật ngược trở lại theo phương cũ)",
          "90 độ",
          "45 độ",
          "180 độ"
        ],
        "correct": 0,
        "explanation": "i = 0° => r = 0°, tia phản xạ bật thẳng ngược trở lại trùng pháp tuyến."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một tia sáng tới hợp với mặt phẳng gương một góc 30 độ. Góc tới i của tia sáng bằng:",
        "options": [
          "60 độ",
          "30 độ",
          "90 độ",
          "120 độ"
        ],
        "correct": 0,
        "explanation": "Góc tới i = 90° - 30° = 60°."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Chiếu tia tới tới mặt gương với góc tới i = 45 độ. Góc hợp bởi tia tới và tia phản xạ bằng:",
        "options": [
          "90 độ",
          "45 độ",
          "180 độ",
          "60 độ"
        ],
        "correct": 0,
        "explanation": "Góc hợp bởi tia tới và phản xạ = i + r = 45° + 45° = 90°."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi tăng góc tới i thêm 10 độ thì góc phản xạ r sẽ:",
        "options": [
          "Tăng thêm 10 độ",
          "Giảm đi 10 độ",
          "Không đổi",
          "Tăng thêm 20 độ"
        ],
        "correct": 0,
        "explanation": "Vì r = i nên khi i tăng 10° thì r cũng tăng 10°."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hiện tượng nhìn thấy ảnh rõ nét của mình trong một chiếc gương soi phẳng là nhờ hiện tượng:",
        "options": [
          "Phản xạ gương trên bề mặt nhẵn bóng",
          "Phản xạ khuếch tán",
          "Khúc xạ ánh sáng",
          "Nhiễu xạ ánh sáng"
        ],
        "correct": 0,
        "explanation": "Phản xạ gương tạo ảnh rõ nét đối xứng."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về định luật phản xạ ánh sáng đối với gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Tia phản xạ luôn nằm trong mặt phẳng tới chứa tia tới và đường pháp tuyến.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Góc phản xạ luôn luôn bằng góc tới.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu tia sáng truyền theo chiều ngược lại của tia phản xạ thì nó sẽ phản xạ theo chiều tia tới ban đầu (tính thuận nghịch của ánh sáng).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Góc tới là góc tạo bởi tia tới và bề mặt của gương.",
            "correct": false
          }
        ],
        "explanation": "Góc tới là góc giữa tia tới và đường pháp tuyến vuông góc với gương."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về hiện tượng phản xạ gương và phản xạ khuếch tán:",
        "statements": [
          {
            "subId": "a",
            "text": "Phản xạ gương xảy ra trên bề mặt nhẵn bóng như mặt gương phẳng, mặt nước phẳng lặng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phản xạ gương cho ta nhìn thấy ảnh rõ nét của vật.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phản xạ khuếch tán xảy ra trên bề mặt gồ ghề nhám như mặt giấy, tường nhà.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phản xạ khuếch tán không tuân theo định luật phản xạ ánh sáng.",
            "correct": false
          }
        ],
        "explanation": "Tại mỗi điểm tới vi mô trên bề mặt gồ ghề, định luật phản xạ ánh sáng vẫn nghiệm đúng tuyệt đối."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Chiếu tia sáng SI tới gương phẳng nằm ngang, tia tới hợp với mặt gương một góc 35 độ:",
        "statements": [
          {
            "subId": "a",
            "text": "Đường pháp tuyến vuông góc với mặt gương tạo góc 90 độ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Góc tới i bằng 55 độ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Góc phản xạ r bằng 55 độ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Góc tạo bởi tia tới và tia phản xạ là 70 độ.",
            "correct": false
          }
        ],
        "explanation": "Góc tạo bởi tia tới và phản xạ là i + r = 55° + 55° = 110°."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một tia sáng chiếu tới mặt gương cố định. Giữ nguyên hướng tia tới, nếu quay mặt phẳng gương quanh trục qua điểm tới một góc 10 độ:",
        "statements": [
          {
            "subId": "a",
            "text": "Pháp tuyến của gương quay đi một góc 10 độ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Góc tới thay đổi một lượng 10 độ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tia phản xạ sẽ quay đi một góc 20 độ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tia phản xạ giữ nguyên hướng không hề thay đổi.",
            "correct": false
          }
        ],
        "explanation": "Khi quay gương một góc α, tia phản xạ quay đi một góc 2α = 20°."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Góc tới bằng 30 độ thì góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "30",
        "explanation": "r = i = 30 độ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tia tới hợp với pháp tuyến góc 50 độ. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "50",
        "explanation": "r = i = 50 độ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tia tới hợp với mặt gương phẳng góc 40 độ. Góc tới bằng bao nhiêu độ?",
        "correctAnswer": "50",
        "explanation": "i = 90 - 40 = 50 độ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Góc tới bằng 60 độ. Góc tạo bởi tia tới và tia phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "120",
        "explanation": "i + r = 60 + 60 = 120 độ."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Tia tới hợp với tia phản xạ một góc 80 độ. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "40",
        "explanation": "r = 80 / 2 = 40 độ."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Giữ nguyên tia tới, quay gương phẳng quanh trục qua điểm tới một góc 25 độ. Tia phản xạ quay đi một góc bao nhiêu độ?",
        "correctAnswer": "50",
        "explanation": "2α = 2 × 25 = 50 độ."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một tia sáng SI chiếu tới gương phẳng nằm ngang. Muốn có tia phản xạ IR hướng thẳng đứng từ dưới lên trên thì góc hợp bởi tia tới SI và mặt gương phải bằng bao nhiêu độ? Biết tia tới SI chiếu chếch từ trên xuống hợp với phương nằm ngang góc 40 độ.",
        "options": [
          "65 độ",
          "40 độ",
          "50 độ",
          "75 độ"
        ],
        "correct": 0,
        "explanation": "Góc giữa SI và IR = 90° + 40° = 130°. Góc tới i = 130° / 2 = 65°. Góc hợp bởi tia tới và mặt gương = 90° - 65° = 25° (hoặc gương đặt nghiêng góc thích hợp tạo góc 65°)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hai gương phẳng G1 và G2 đặt vuông góc với nhau (hợp với nhau góc 90 độ), mặt phản xạ quay vào nhau. Chiếu một tia sáng SI tới gương G1 với góc tới i1 bất kì (0 < i1 < 90°), tia phản xạ từ G1 đến đập vào gương G2 rồi phản xạ tiếp thành tia JR. Tia phản xạ cuối cùng JR có hướng như thế nào so với tia tới ban đầu SI?",
        "options": [
          "Luôn luôn song song và ngược chiều với tia tới ban đầu SI",
          "Vuông góc với tia tới ban đầu",
          "Trùng khít với tia tới",
          "Hợp với tia tới góc 45 độ"
        ],
        "correct": 0,
        "explanation": "Hệ hai gương vuông góc luôn phản xạ tia sáng quay ngược trở lại song song (nguyên lí tấm phản quang mắt mèo)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một căn phòng tối có một lỗ nhỏ trên mái nhà cho một tia sáng Mặt Trời lọt vào theo phương nghiêng hợp với phương nằm ngang một góc 60 độ. Để chiếu thẳng đứng tia sáng đó xuống đáy một chiếc giếng sâu dưới sàn phòng, người ta cần đặt một gương phẳng tại điểm tới nghiêng một góc bao nhiêu độ so với phương thẳng đứng?",
        "options": [
          "15 độ",
          "30 độ",
          "75 độ",
          "45 độ"
        ],
        "correct": 0,
        "explanation": "Góc giữa tia tới và tia phản xạ: 60° + 90° = 150°. Góc tới i = 150° / 2 = 75°. Pháp tuyến nghiêng 75° so với tia phản xạ (thẳng đứng), mặt gương nghiêng 90° - 75° = 15° so với phương thẳng đứng."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một ngọn nến đặt trước một tấm bìa đen có khoét một lỗ kim nhỏ, phía sau là một màn chắn. Nếu đặt thêm một chiếc gương phẳng ở phía sau lỗ kim hợp góc 45 độ thì đường truyền tia sáng phản xạ sẽ đổi hướng bao nhiêu độ?",
        "options": [
          "90 độ",
          "45 độ",
          "180 độ",
          "60 độ"
        ],
        "correct": 0,
        "explanation": "Gương nghiêng 45° đổi hướng tia sáng một góc 90°."
      }
    ]
  },
  "phys7_c5_b16_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 16: Sự phản xạ ánh sáng - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b16",
    "lessonName": "Bài 16: Sự phản xạ ánh sáng",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Góc phản xạ là góc tạo bởi:",
        "options": [
          "Tia phản xạ và đường pháp tuyến của gương tại điểm tới",
          "Tia phản xạ và mặt phẳng gương",
          "Tia tới và mặt phẳng gương",
          "Tia tới và tia phản xạ"
        ],
        "correct": 0,
        "explanation": "Góc phản xạ r = góc(NIR)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Kí hiệu thông thường của góc tới và góc phản xạ lần lượt là:",
        "options": [
          "i và r",
          "r và i",
          "α và β",
          "v và s"
        ],
        "correct": 0,
        "explanation": "Góc tới là i, góc phản xạ là r."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tia phản xạ nằm trong mặt phẳng nào sau đây?",
        "options": [
          "Mặt phẳng tới chứa tia tới và pháp tuyến tại điểm tới",
          "Mặt phẳng chứa gương",
          "Mặt phẳng vuông góc với tia tới",
          "Mặt phẳng ngang"
        ],
        "correct": 0,
        "explanation": "Tia phản xạ nằm trong mặt phẳng tới."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nếu chiếu tia tới SI vuông góc với mặt gương phẳng thì góc tới i bằng:",
        "options": [
          "0 độ",
          "90 độ",
          "45 độ",
          "180 độ"
        ],
        "correct": 0,
        "explanation": "Tia tới trùng pháp tuyến nên i = 0 độ."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Gương phẳng là:",
        "options": [
          "Một mặt phẳng nhẵn bóng có khả năng phản xạ hầu hết ánh sáng chiếu tới",
          "Một khối cầu trong suốt",
          "Một tấm kính mờ",
          "Một tấm kim loại gồ ghề"
        ],
        "correct": 0,
        "explanation": "Gương phẳng là mặt phẳng nhẵn bóng phản xạ tốt."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Khi có phản xạ khuếch tán, ta nhìn thấy bề mặt vật sáng:",
        "options": [
          "Được chiếu sáng từ mọi hướng nhưng không thấy ảnh rõ nét của nguồn sáng",
          "Như một chiếc gương soi",
          "Tối đen hoàn toàn",
          "Phát ra tia laser"
        ],
        "correct": 0,
        "explanation": "Phản xạ khuếch tán giúp ta nhìn thấy vật sáng từ mọi phía mà không thấy ảnh."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Chiếu một tia sáng tới gương phẳng với góc tới i = 25 độ. Góc phản xạ r bằng:",
        "options": [
          "25 độ",
          "50 độ",
          "65 độ",
          "75 độ"
        ],
        "correct": 0,
        "explanation": "r = i = 25 độ."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tia sáng tới hợp với mặt gương một góc 45 độ. Góc phản xạ r có giá trị bằng:",
        "options": [
          "45 độ",
          "90 độ",
          "30 độ",
          "60 độ"
        ],
        "correct": 0,
        "explanation": "Góc tới i = 90° - 45° = 45° => r = 45°."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Chiếu tia tới SI sao cho góc hợp bởi tia tới và tia phản xạ bằng 100 độ. Góc tới i có giá trị là:",
        "options": [
          "50 độ",
          "100 độ",
          "25 độ",
          "40 độ"
        ],
        "correct": 0,
        "explanation": "i = 100° / 2 = 50°."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nếu giảm góc tới i đi 15 độ thì góc tạo bởi tia tới và tia phản xạ sẽ:",
        "options": [
          "Giảm đi 30 độ",
          "Giảm đi 15 độ",
          "Tăng thêm 15 độ",
          "Không đổi"
        ],
        "correct": 0,
        "explanation": "Góc hợp bởi hai tia là 2i, khi i giảm 15° thì 2i giảm 30°."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi soi gương, ta có thể nhìn thấy dòng chữ trên áo mình in ngược là do:",
        "options": [
          "Hiện tượng phản xạ ánh sáng của gương phẳng tạo ảnh đối xứng trục trái phải",
          "Mắt người nhìn sai",
          "Áo in bị lỗi",
          "Gương bị cong"
        ],
        "correct": 0,
        "explanation": "Gương phẳng tạo ảnh đối xứng qua mặt phẳng gương, đổi hướng trái phải."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tấm phản quang gắn ở đuôi xe đạp có màu đỏ phát sáng khi đèn xe ô tô phía sau chiếu vào là nhờ cấu tạo:",
        "options": [
          "Nhiều góc vuông gồm các mặt phản xạ vuông góc với nhau hắt tia sáng ngược trở lại nguồn",
          "Bên trong có bóng đèn pin",
          "Sơn lân tinh tự sáng",
          "Pin năng lượng mặt trời"
        ],
        "correct": 0,
        "explanation": "Cấu tạo các hốc phản xạ góc vuông hắt tia sáng quay về nguồn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các quy tắc trong định luật phản xạ ánh sáng:",
        "statements": [
          {
            "subId": "a",
            "text": "Pháp tuyến là đường thẳng vuông góc với mặt gương tại điểm tới.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Góc phản xạ r luôn luôn bằng góc tới i.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tia phản xạ và tia tới luôn nằm cùng một phía so với đường pháp tuyến.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tia tới, tia phản xạ và đường pháp tuyến cùng nằm trong một mặt phẳng.",
            "correct": true
          }
        ],
        "explanation": "Tia tới và tia phản xạ nằm ở hai phía đối xứng qua đường pháp tuyến."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về ứng dụng của hiện tượng phản xạ ánh sáng:",
        "statements": [
          {
            "subId": "a",
            "text": "Gương chiếu hậu trên xe ô tô giúp tài xế quan sát các xe phía sau nhờ phản xạ ánh sáng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mặt biển phẳng lặng phản chiếu hình ảnh ngọn núi và bầu trời như một tấm gương khổng lồ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Mặt đường nhựa khô ráp phản xạ ánh sáng theo kiểu phản xạ gương rõ nét.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khi trời mưa, mặt đường đọng nước nhẵn bóng có thể gây lóa mắt tài xế do phản xạ gương ánh đèn.",
            "correct": true
          }
        ],
        "explanation": "Đường nhựa khô nhám gây phản xạ khuếch tán, khi ướt đọng nước mới tạo phản xạ gương làm chói lóa."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Chiếu tia sáng SI tới mặt gương nằm ngang, góc hợp bởi tia tới và mặt gương là 50 độ:",
        "statements": [
          {
            "subId": "a",
            "text": "Góc tới i bằng 40 độ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Góc phản xạ r bằng 40 độ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Góc hợp bởi tia phản xạ và mặt phẳng gương là 50 độ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Góc tạo bởi tia tới và tia phản xạ là 100 độ.",
            "correct": false
          }
        ],
        "explanation": "Góc hợp bởi tia tới và tia phản xạ là i + r = 40° + 40° = 80° (câu d ghi 100° là sai)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khảo sát tia sáng qua hai gương phẳng đặt song song có mặt phản xạ hướng vào nhau:",
        "statements": [
          {
            "subId": "a",
            "text": "Chiếu tia tới tới gương 1 với góc tới i1, tia phản xạ tới gương 2 với góc tới i2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Vì hai gương song song nên hai pháp tuyến song song, do đó i1 = i2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tia phản xạ ló ra từ gương 2 luôn song song và cùng chiều với tia tới ban đầu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu đổi góc tới thì tia phản xạ cuối cùng sẽ bị lệch vuông góc.",
            "correct": false
          }
        ],
        "explanation": "Hai gương phẳng song song luôn cho tia phản xạ cuối cùng song song với tia tới ban đầu."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Góc tới bằng 45 độ. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "45",
        "explanation": "r = i = 45 độ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Chiếu tia sáng vuông góc với gương phẳng. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "0",
        "explanation": "r = i = 0 độ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tia tới hợp với mặt phẳng gương góc 30 độ. Góc tới bằng bao nhiêu độ?",
        "correctAnswer": "60",
        "explanation": "i = 90 - 30 = 60 độ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Góc tới bằng 35 độ. Góc tạo bởi tia tới và tia phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "70",
        "explanation": "35 + 35 = 70 độ."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Góc tạo bởi tia tới và tia phản xạ bằng 60 độ. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "30",
        "explanation": "r = 60 / 2 = 30 độ."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Tia tới cố định, nếu quay mặt gương một góc 12 độ thì tia phản xạ quay đi một góc bao nhiêu độ?",
        "correctAnswer": "24",
        "explanation": "2 × 12 = 24 độ."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một tia sáng SI chiếu nghiêng hợp với phương nằm ngang một góc 30 độ truyền tới một điểm I trên mặt đất. Người ta đặt một gương phẳng tại I để hắt tia phản xạ IR truyền thẳng đứng xuống đáy một chiếc giếng sâu. Mặt gương phẳng cần đặt nghiêng một góc bao nhiêu độ so với phương thẳng đứng?",
        "options": [
          "30 độ",
          "60 độ",
          "15 độ",
          "45 độ"
        ],
        "correct": 0,
        "explanation": "Góc giữa SI và IR = 30° + 90° = 120°. Góc tới i = 120° / 2 = 60°. Mặt gương nghiêng 90° - 60° = 30° so với phương thẳng đứng."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một ngọn hải đăng phát ra một chùm tia sáng hẹp nằm ngang. Để chiếu chùm tia sáng đó xuống chiếu sáng một chiếc ca nô đang cứu nạn ở phương tạo với phương nằm ngang một góc 40 độ chếch xuống dưới, người ta đặt một tấm gương phẳng tại điểm đèn. Góc tới i của tia sáng tới mặt gương bằng:",
        "options": [
          "20 độ",
          "40 độ",
          "70 độ",
          "50 độ"
        ],
        "correct": 0,
        "explanation": "Góc giữa tia tới và tia phản xạ là 40°. Góc tới i = 40° / 2 = 20°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một căn phòng có hai gương phẳng treo trên hai bức tường đối diện song song nhau. Khi một người đứng giữa hai gương soi gương, người đó sẽ quan sát thấy:",
        "options": [
          "Vô số ảnh ảo của mình nối tiếp nhau thành một hàng sâu hun hút",
          "Chỉ duy nhất một ảnh",
          "Hai ảnh",
          "Bốn ảnh"
        ],
        "correct": 0,
        "explanation": "Hiện tượng phản xạ ánh sáng lặp đi lặp lại vô tận giữa hai gương phẳng song song tạo dãy vô số ảnh."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một tia sáng chiếu tới gương phẳng tại điểm I với góc tới i = 30 độ. Nếu giữ nguyên tia tới và quay gương một góc 15 độ quanh trục vuông góc với mặt phẳng tới thì góc hợp bởi tia tới và tia phản xạ mới có thể nhận giá trị nào sau đây?",
        "options": [
          "90 độ (hoặc 30 độ)",
          "60 độ",
          "45 độ",
          "120 độ"
        ],
        "correct": 0,
        "explanation": "Góc hợp ban đầu 2i = 60°. Khi quay gương 15°, tia phản xạ quay 2α = 30° => Góc mới: 60° + 30° = 90° (hoặc 60° - 30° = 30°)."
      }
    ]
  },
  "phys7_c5_b16_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 16: Sự phản xạ ánh sáng - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b16",
    "lessonName": "Bài 16: Sự phản xạ ánh sáng",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong định luật phản xạ ánh sáng, tia phản xạ nằm trong:",
        "options": [
          "Mặt phẳng tới chứa tia tới và đường pháp tuyến",
          "Mặt phẳng gương",
          "Bất kì mặt phẳng nào",
          "Mặt phẳng thẳng đứng"
        ],
        "correct": 0,
        "explanation": "Tia phản xạ nằm trong mặt phẳng tới."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Mối quan hệ giữa góc tới i và góc phản xạ r là:",
        "options": [
          "r = i",
          "r > i",
          "r < i",
          "r = 2i"
        ],
        "correct": 0,
        "explanation": "r = i."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Đường pháp tuyến của gương phẳng tại điểm tới là đường thẳng:",
        "options": [
          "Vuông góc với mặt gương tại điểm tới",
          "Song song với mặt gương",
          "Hợp với mặt gương góc 45 độ",
          "Trùng với tia tới"
        ],
        "correct": 0,
        "explanation": "Pháp tuyến vuông góc với mặt gương tại điểm tới."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hiện tượng ánh sáng bị hắt lại theo một hướng xác định từ bề mặt phẳng nhẵn được gọi là:",
        "options": [
          "Phản xạ gương",
          "Phản xạ khuếch tán",
          "Khúc xạ",
          "Hấp thụ"
        ],
        "correct": 0,
        "explanation": "Phản xạ gương định hướng tia sáng xác định."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Vật nào sau đây phản xạ ánh sáng theo định luật phản xạ ánh sáng?",
        "options": [
          "Mọi vật có bề mặt phản xạ (cả mặt nhẵn và mặt gồ ghề vi mô)",
          "Chỉ gương phẳng",
          "Chỉ mặt nước",
          "Chỉ kim loại"
        ],
        "correct": 0,
        "explanation": "Định luật phản xạ ánh sáng đúng tại mọi điểm tới của mọi bề mặt."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Góc hợp bởi tia tới và mặt gương có mối quan hệ với góc tới i là:",
        "options": [
          "Góc hợp = 90 độ - i",
          "Góc hợp = i",
          "Góc hợp = 180 độ - i",
          "Góc hợp = 2i"
        ],
        "correct": 0,
        "explanation": "Vì pháp tuyến vuông góc gương nên góc hợp với gương = 90° - i."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Chiếu tia tới tới gương phẳng với góc tới i = 60 độ. Góc phản xạ r bằng:",
        "options": [
          "60 độ",
          "30 độ",
          "120 độ",
          "90 độ"
        ],
        "correct": 0,
        "explanation": "r = i = 60 độ."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tia tới hợp với mặt phẳng gương một góc 20 độ. Góc phản xạ r bằng:",
        "options": [
          "70 độ",
          "20 độ",
          "40 độ",
          "80 độ"
        ],
        "correct": 0,
        "explanation": "i = 90° - 20° = 70° => r = 70°."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tia tới SI hợp với tia phản xạ IR một góc 140 độ. Góc tới i có độ lớn là:",
        "options": [
          "70 độ",
          "140 độ",
          "35 độ",
          "40 độ"
        ],
        "correct": 0,
        "explanation": "i = 140° / 2 = 70°."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khi một người dịch chuyển đèn pin lại gần gương sao cho góc tới i tăng từ 30 độ lên 50 độ thì góc phản xạ r sẽ:",
        "options": [
          "Tăng từ 30 độ lên 50 độ",
          "Giảm xuống 20 độ",
          "Không đổi",
          "Tăng lên 100 độ"
        ],
        "correct": 0,
        "explanation": "Góc phản xạ r luôn bằng góc tới i nên tăng lên 50°."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Kính tiềm vọng dùng trên tàu ngầm đơn giản nhất được cấu tạo bởi:",
        "options": [
          "Hai gương phẳng đặt song song nghiêng góc 45 độ so với trục ống ngắm",
          "Một thấu kính hội tụ",
          "Hai gương cầu lõm",
          "Một lăng kính tam giác"
        ],
        "correct": 0,
        "explanation": "Kính tiềm vọng gồm 2 gương phẳng song song nghiêng 45° phản xạ ánh sáng 2 lần góc 90°."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tại sao ban đêm đi trên đường nhựa khô ta nhìn rõ mặt đường, nhưng khi đường ướt sũng nước thì bị chói mắt bởi ánh đèn xe?",
        "options": [
          "Vì mặt đường ướt nhẵn bóng gây phản xạ gương làm chùm sáng phản xạ tập trung chiếu thẳng vào mắt người lái",
          "Vì nước phát sáng",
          "Vì đèn xe sáng hơn",
          "Vì đường bị mòn"
        ],
        "correct": 0,
        "explanation": "Nước đọng tạo bề mặt nhẵn bóng biến phản xạ khuếch tán thành phản xạ gương gây chói mắt."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các tính chất hình học của sự phản xạ ánh sáng:",
        "statements": [
          {
            "subId": "a",
            "text": "Tia phản xạ, tia tới và pháp tuyến cùng nằm trên một mặt phẳng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Góc phản xạ luôn luôn bằng góc tới.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu tia tới vuông góc với mặt gương (i = 0°) thì tia phản xạ bật ngược trở lại theo phương cũ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu góc tới là 90° thì tia sáng sẽ đâm xuyên thẳng qua gương.",
            "correct": false
          }
        ],
        "explanation": "Góc tới 90° nghĩa là tia sáng đi là là sát mặt phẳng gương."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về hiện tượng phản xạ khuếch tán trong tự nhiên:",
        "statements": [
          {
            "subId": "a",
            "text": "Nhờ có phản xạ khuếch tán mà ta có thể đọc được các chữ in trên trang sách từ nhiều góc nhìn khác nhau.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bức tường quét vôi trắng phản xạ khuếch tán ánh sáng giúp căn phòng sáng đều.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Mặt gương kính vỡ vụn gây phản xạ khuếch tán làm ánh sáng tán xạ lung linh.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phản xạ khuếch tán chỉ xảy ra trong phòng tối.",
            "correct": false
          }
        ],
        "explanation": "Phản xạ khuếch tán xảy ra ở bất kì nơi nào có ánh sáng chiếu vào bề mặt gồ ghề nhám."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Chiếu tia tới SI lên mặt gương phẳng, góc tạo bởi tia tới SI và tia phản xạ IR là 80 độ:",
        "statements": [
          {
            "subId": "a",
            "text": "Đường pháp tuyến là đường phân giác của góc tạo bởi tia tới và tia phản xạ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Góc tới i bằng 40 độ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Góc phản xạ r bằng 40 độ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Góc tạo bởi tia tới SI và mặt phẳng gương là 40 độ.",
            "correct": false
          }
        ],
        "explanation": "Góc tạo bởi SI và mặt gương là 90° - 40° = 50°."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Kính tiềm vọng (Periscope) quang học đơn giản:",
        "statements": [
          {
            "subId": "a",
            "text": "Ánh sáng từ mục tiêu truyền vào gương thứ nhất ở trên cao phản xạ một góc 90 độ xuống dưới.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Gương thứ hai ở dưới nhận tia phản xạ và tiếp tục phản xạ góc 90 độ vào mắt người quan sát.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hai gương phẳng trong kính tiềm vọng phải đặt nghiêng góc 45 độ so với trục ống ngắm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Ảnh quan sát được qua kính tiềm vọng bị lộn ngược đầu xuống đất.",
            "correct": false
          }
        ],
        "explanation": "Hai lần phản xạ gương phẳng cho ảnh cùng chiều thẳng đứng giúp quan sát rõ ràng mục tiêu."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Góc tới i = 70 độ. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "70",
        "explanation": "r = i = 70 độ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tia tới hợp với pháp tuyến góc 15 độ. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "15",
        "explanation": "r = i = 15 độ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tia tới hợp với mặt phẳng gương góc 55 độ. Góc tới bằng bao nhiêu độ?",
        "correctAnswer": "35",
        "explanation": "i = 90 - 55 = 35 độ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Góc tới bằng 20 độ. Góc tạo bởi tia tới và tia phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "40",
        "explanation": "20 + 20 = 40 độ."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Góc hợp bởi tia tới và tia phản xạ là 110 độ. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "55",
        "explanation": "r = 110 / 2 = 55 độ."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Giữ nguyên hướng tia tới, quay gương một góc 18 độ. Tia phản xạ quay đi một góc bao nhiêu độ?",
        "correctAnswer": "36",
        "explanation": "2 × 18 = 36 độ."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một tia sáng Mặt Trời chiếu nghiêng hợp với mặt đất nằm ngang một góc 50 độ. Để chiếu tia sáng này theo phương nằm ngang vào trong một hang động tối, người ta dùng một chiếc gương phẳng đặt tại điểm tới. Góc nghiêng của mặt phẳng gương so với phương nằm ngang là bao nhiêu độ?",
        "options": [
          "25 độ",
          "50 độ",
          "65 độ",
          "40 độ"
        ],
        "correct": 0,
        "explanation": "Góc giữa tia tới và tia phản xạ nằm ngang: 180° - 50° = 130°. Góc tới i = 130° / 2 = 65°. Pháp tuyến hợp với mặt đất góc 65° - 50° = 15°. Mặt gương hợp góc 90° - 65° = 25° so với phương nằm ngang."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hai gương phẳng G1 và G2 đặt hợp với nhau một góc nhọn α = 60 độ, mặt phản xạ quay vào nhau. Chiếu một tia sáng SI song song với gương G2 tới gương G1. Sau khi phản xạ lần thứ nhất trên G1, tia sáng đến đập vào gương G2 rồi phản xạ tiếp thành tia JR. Góc tới i2 trên gương G2 bằng:",
        "options": [
          "30 độ",
          "60 độ",
          "45 độ",
          "0 độ"
        ],
        "correct": 0,
        "explanation": "Tia SI song song G2 nên góc tới i1 = 30°. Tia phản xạ đập vào G2 với góc tới i2 = 0° (vuông góc với G2) rồi bật thẳng ngược trở lại."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Kính vạn hoa (Kaleidoscope) tạo ra những hoa văn rực rỡ biến hóa liên tục nhờ cấu tạo cốt lõi gồm:",
        "options": [
          "Ba tấm gương phẳng dài ghép lại thành hình lăng trụ tam giác đều phản xạ ánh sáng nhiều lần qua lại",
          "Một bóng đèn nhấp nháy",
          "Hai thấu kính phân kì",
          "Một quả cầu thủy tinh"
        ],
        "correct": 0,
        "explanation": "Hệ 3 gương phẳng nghiêng 60° phản xạ liên tiếp tạo các mẫu hoa văn đối xứng hình học tuyệt đẹp."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một tia sáng chiếu tới mặt gương phẳng nằm ngang với góc tới i = 40 độ. Nếu quay gương quanh trục tới một góc 10 độ làm cho góc tới tăng lên thành 50 độ thì góc hợp bởi tia tới và tia phản xạ mới sẽ tăng thêm bao nhiêu độ?",
        "options": [
          "20 độ",
          "10 độ",
          "30 độ",
          "40 độ"
        ],
        "correct": 0,
        "explanation": "Góc hợp ban đầu 2i = 80°, góc hợp mới 2i' = 100° => Tăng thêm: 100° - 80° = 20°."
      }
    ]
  },
  "phys7_c5_b17_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 17: Ảnh của một vật tạo bởi gương phẳng - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b17",
    "lessonName": "Bài 17: Ảnh của một vật tạo bởi gương phẳng",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Ảnh của một vật tạo bởi gương phẳng có tính chất nào sau đây?",
        "options": [
          "Là ảnh ảo, không hứng được trên màn chắn",
          "Là ảnh thật, hứng được trên màn chắn",
          "Là ảnh ảo lớn hơn vật",
          "Là ảnh thật nhỏ hơn vật"
        ],
        "correct": 0,
        "explanation": "Ảnh qua gương phẳng là ảnh ảo không hứng được trên màn chắn."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Độ lớn của ảnh của một vật tạo bởi gương phẳng:",
        "options": [
          "Bằng độ lớn của vật",
          "Lớn hơn độ lớn của vật",
          "Nhỏ hơn độ lớn của vật",
          "Gấp đôi độ lớn của vật"
        ],
        "correct": 0,
        "explanation": "Độ lớn ảnh luôn bằng độ lớn của vật."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khoảng cách từ một điểm trên vật đến gương phẳng và khoảng cách từ ảnh của điểm đó đến gương phẳng có mối quan hệ:",
        "options": [
          "Bằng nhau",
          "Khoảng cách từ ảnh lớn hơn",
          "Khoảng cách từ ảnh nhỏ hơn",
          "Không bằng nhau"
        ],
        "correct": 0,
        "explanation": "Vật và ảnh cách đều mặt phẳng gương."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Ảnh của một vật qua gương phẳng và vật có tính chất đối xứng với nhau qua:",
        "options": [
          "Mặt phẳng gương",
          "Trục thẳng đứng",
          "Đường pháp tuyến",
          "Điểm tới"
        ],
        "correct": 0,
        "explanation": "Vật và ảnh ảo đối xứng nhau qua mặt phẳng gương."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Vùng không gian mà mắt người quan sát có thể nhìn thấy ảnh của các vật qua gương phẳng được gọi là:",
        "options": [
          "Vùng quan sát của gương phẳng (thị trường của gương)",
          "Vùng bóng tối",
          "Vùng mù",
          "Tiêu cự"
        ],
        "correct": 0,
        "explanation": "Vùng quan sát (thị trường) của gương phẳng."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Bác sĩ nha khoa thường dùng một chiếc gương tròn nhỏ đưa vào miệng bệnh nhân nhằm:",
        "options": [
          "Quan sát ảnh của các góc khuất và mặt sau của răng",
          "Để đo nhiệt độ",
          "Để mài răng",
          "Để làm sáng mắt"
        ],
        "correct": 0,
        "explanation": "Gương nha sĩ quan sát ảnh của các góc khuất trong hàm răng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một ngọn nến đặt thẳng đứng cách gương phẳng 20 cm. Ảnh của ngọn nến cách gương phẳng một khoảng là:",
        "options": [
          "20 cm",
          "40 cm",
          "10 cm",
          "30 cm"
        ],
        "correct": 0,
        "explanation": "d' = d = 20 cm."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một vật đặt cách gương phẳng 50 cm. Khoảng cách giữa vật và ảnh của nó tạo bởi gương phẳng là:",
        "options": [
          "100 cm (1 mét)",
          "50 cm",
          "25 cm",
          "0 cm"
        ],
        "correct": 0,
        "explanation": "Khoảng cách giữa vật và ảnh = 2d = 2 × 50 = 100 cm = 1 m."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một bạn học sinh cao 1,6 mét đứng trước một chiếc gương phẳng treo thẳng đứng. Chiều cao ảnh của bạn học sinh trong gương là:",
        "options": [
          "1,6 mét",
          "0,8 mét",
          "3,2 mét",
          "1,2 mét"
        ],
        "correct": 0,
        "explanation": "Độ lớn ảnh bằng độ lớn vật nên chiều cao ảnh là 1,6 m."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Một người đứng cách gương phẳng 2 m, nếu người đó tiến lại gần gương thêm 0,5 m thì khoảng cách giữa người đó và ảnh của mình trong gương là:",
        "options": [
          "3,0 m",
          "1,5 m",
          "4,0 m",
          "2,5 m"
        ],
        "correct": 0,
        "explanation": "Khoảng cách mới đến gương: 2 - 0,5 = 1,5 m => Khoảng cách giữa người và ảnh: 2 × 1,5 = 3,0 m."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Vì sao trên đầu xe cứu thương (Ambulance), dòng chữ thường được in ngược (ꓱƆИA⅃UᙠMA)?",
        "options": [
          "Để khi tài xế xe phía trước nhìn qua gương chiếu hậu sẽ thấy dòng chữ xuôi chiều 'AMBULANCE' rõ ràng và kịp thời nhường đường",
          "Do máy in bị lỗi",
          "Là phong cách thẩm mỹ",
          "Để người đi bộ đọc dễ hơn"
        ],
        "correct": 0,
        "explanation": "Gương phẳng đảo trái phải, in ngược chữ giúp người nhìn qua gương thấy chữ xuôi."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Khi đưa một bàn tay phải đặt song song trước gương phẳng, ảnh của bàn tay trong gương giống như bàn tay nào của một người đối diện?",
        "options": [
          "Bàn tay trái",
          "Bàn tay phải",
          "Cả hai bàn tay",
          "Bàn chân"
        ],
        "correct": 0,
        "explanation": "Gương phẳng có tính chất đối xứng trục đảo ngược trái - phải."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các tính chất cơ bản của ảnh tạo bởi gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Ảnh tạo bởi gương phẳng là ảnh ảo, không hứng được trên màn chắn đặt phía sau gương.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Kích thước của ảnh luôn luôn bằng kích thước thật của vật.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu người lùi ra xa gương phẳng thì kích thước thật của ảnh trong gương sẽ nhỏ đi.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khoảng cách từ vật đến gương bằng khoảng cách từ ảnh đến gương.",
            "correct": true
          }
        ],
        "explanation": "Kích thước thật của ảnh luôn bằng vật, nhìn thấy nhỏ đi là do góc trông của mắt giảm khi ra xa."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về cách dựng ảnh của một điểm sáng S qua gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Từ S hạ đường vuông góc SH xuống mặt gương, kéo dài lấy đoạn HS' = SH thì S' là ảnh của S.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Từ S vẽ hai tia tới bất kì đến gương, vẽ hai tia phản xạ tương ứng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đường kéo dài của hai tia phản xạ cắt nhau tại điểm ảnh ảo S' phía sau gương.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Ảnh ảo S' được tạo bởi sự giao nhau trực tiếp của các tia phản xạ thực tế.",
            "correct": false
          }
        ],
        "explanation": "Ảnh ảo S' là giao điểm của đường kéo dài các tia phản xạ, không phải tia phản xạ thực tế giao nhau."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một người đứng trước gương phẳng treo thẳng đứng trên tường:",
        "statements": [
          {
            "subId": "a",
            "text": "Khoảng cách ban đầu từ người đến gương là 1,2 m thì ảnh cách người 2,4 m.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Người đó bước lùi xa gương thêm 0,4 m thì khoảng cách mới từ người đến gương là 1,6 m.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khoảng cách giữa người và ảnh lúc này là 3,2 m.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khoảng cách giữa người và ảnh đã tăng thêm 0,4 m so với ban đầu.",
            "correct": false
          }
        ],
        "explanation": "Khoảng cách ban đầu là 2,4 m, sau đó là 3,2 m => tăng thêm 0,8 m (câu d ghi 0,4 m là sai)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng gương phẳng trong thiết bị kính tiềm vọng (Periscope):",
        "statements": [
          {
            "subId": "a",
            "text": "Gồm hai gương phẳng đặt song song và nghiêng góc 45 độ so với trục ống.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Giúp người ngồi trong tàu ngầm quan sát các tàu bè trên mặt nước.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ảnh quan sát được qua kính tiềm vọng là ảnh cùng chiều với vật.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Kính tiềm vọng phóng to kích thước của vật lên gấp 100 lần.",
            "correct": false
          }
        ],
        "explanation": "Gương phẳng không có tác dụng phóng to kích thước vật như kính hiển vi."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Vật cách gương phẳng 40 cm. Ảnh của vật cách gương phẳng bao nhiêu cm?",
        "correctAnswer": "40",
        "explanation": "40 cm."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Ảnh tạo bởi gương phẳng là ảnh thật hay ảnh ảo?",
        "correctAnswer": "Ảnh ảo",
        "explanation": "Ảnh ảo."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một cây nến cao 15 cm đặt trước gương phẳng. Chiều cao của ảnh cây nến là bao nhiêu cm?",
        "correctAnswer": "15",
        "explanation": "15 cm."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người đứng cách gương phẳng 1,8 m. Khoảng cách giữa người đó và ảnh của mình là bao nhiêu mét?",
        "correctAnswer": "3.6",
        "explanation": "1,8 × 2 = 3,6 m."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một vật cách gương phẳng 30 cm. Nếu dịch chuyển vật ra xa gương thêm 10 cm thì khoảng cách giữa vật và ảnh lúc này là bao nhiêu cm?",
        "correctAnswer": "80",
        "explanation": "Khoảng cách mới d = 40 cm => 2d = 80 cm."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Để nhìn thấy toàn bộ cơ thể trong một chiếc gương phẳng treo thẳng đứng, chiều cao tối thiểu của tấm gương phải bằng bao nhiêu phần chiều cao cơ thể? (Viết dạng phân số tối giản)",
        "correctAnswer": "1/2",
        "explanation": "Chiều cao tối thiểu bằng 1/2 chiều cao người."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người cao 1,7 mét đứng thẳng trước một chiếc gương phẳng treo thẳng đứng trên tường. Mắt người cách đỉnh đầu 10 cm (0,1 m). Để người đó có thể nhìn thấy trọn vẹn toàn bộ cơ thể mình từ đỉnh đầu đến gót chân trong gương thì chiều cao tối thiểu của tấm gương và mép dưới của gương cách mặt sàn tối đa bao nhiêu mét?",
        "options": [
          "Gương cao tối thiểu 0,85 m và mép dưới cách sàn tối đa 0,80 m",
          "Gương cao 1,7 m và mép dưới chạm sàn",
          "Gương cao 0,9 m và mép dưới cách sàn 0,5 m",
          "Gương cao 1,0 m và mép dưới cách sàn 0,7 m"
        ],
        "correct": 0,
        "explanation": "Chiều cao gương tối thiểu = H / 2 = 1,7 / 2 = 0,85 m. Mép dưới cách sàn tối đa = (1,7 - 0,1) / 2 = 0,80 m."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một điểm sáng S đặt trước một chiếc gương phẳng nằm ngang. Nếu giữ nguyên điểm sáng S và dịch chuyển gương phẳng sang phải theo phương song song với mặt gương thì vị trí của ảnh ảo S' sẽ:",
        "options": [
          "Không hề thay đổi vị trí trong không gian",
          "Dịch chuyển sang phải theo gương",
          "Dịch chuyển lên trên",
          "Biến mất"
        ],
        "correct": 0,
        "explanation": "Vì mặt phẳng gương không đổi vị trí (chỉ tịnh tiến song song trong mặt phẳng của nó) nên trục đối xứng không đổi, ảnh S' đứng yên."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách gương phẳng 1 mét, nhìn thấy ảnh của một chiếc đồng hồ treo tường ở bức tường phía sau lưng mình. Biết bức tường cách gương 4 mét. Khoảng cách từ mắt người đó đến ảnh của chiếc đồng hồ trong gương là:",
        "options": [
          "5 mét",
          "4 mét",
          "3 mét",
          "6 mét"
        ],
        "correct": 0,
        "explanation": "Đồng hồ cách gương 4 m nên ảnh đồng hồ cách gương 4 m. Người cách gương 1 m (ở cùng phía với đồng hồ) => Khoảng cách từ mắt người đến ảnh = 1 + 4 = 5 m."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một chú mèo con đứng trước một chiếc gương phẳng. Khi chú mèo bước lại gần gương với tốc độ 0,2 m/s theo phương vuông góc với gương thì ảnh của chú mèo tiến lại gần chú mèo với tốc độ tương đối là bao nhiêu?",
        "options": [
          "0,4 m/s",
          "0,2 m/s",
          "0,1 m/s",
          "0,8 m/s"
        ],
        "correct": 0,
        "explanation": "Mèo tiến lại gần gương 0,2 m/s thì ảnh cũng tiến lại gương 0,2 m/s => Tốc độ tương đối giữa mèo và ảnh = 0,2 + 0,2 = 0,4 m/s."
      }
    ]
  },
  "phys7_c5_b17_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 17: Ảnh của một vật tạo bởi gương phẳng - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b17",
    "lessonName": "Bài 17: Ảnh của một vật tạo bởi gương phẳng",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Ảnh của một vật tạo bởi gương phẳng không hứng được trên màn chắn vì:",
        "options": [
          "Đó là ảnh ảo được tạo bởi đường kéo dài của các tia sáng phản xạ",
          "Ảnh quá nhỏ",
          "Ảnh quá mờ",
          "Gương hút hết ánh sáng"
        ],
        "correct": 0,
        "explanation": "Ảnh ảo là giao điểm của các đường kéo dài tia phản xạ, không có ánh sáng thực hội tụ nên không hứng được trên màn."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Nếu đặt một cây bút chì dài 12 cm trước gương phẳng thì chiều dài ảnh của cây bút chì là:",
        "options": [
          "12 cm",
          "6 cm",
          "24 cm",
          "18 cm"
        ],
        "correct": 0,
        "explanation": "Độ lớn của ảnh luôn bằng độ lớn của vật (12 cm)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Đoạn thẳng nối một điểm của vật với ảnh tương ứng của nó qua gương phẳng luôn:",
        "options": [
          "Vuông góc với mặt gương và bị mặt gương chia đôi",
          "Song song với mặt gương",
          "Hợp với mặt gương góc 45 độ",
          "Nằm trên mặt gương"
        ],
        "correct": 0,
        "explanation": "Tính chất đối xứng qua mặt phẳng gương: đoạn nối vuông góc với gương tại trung điểm."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi soi gương phẳng, ảnh của mắt phải của một người sẽ là:",
        "options": [
          "Mắt trái của ảnh người đó đối diện trong gương",
          "Mắt phải của ảnh",
          "Cả hai mắt",
          "Mũi"
        ],
        "correct": 0,
        "explanation": "Tính chất đối xứng đảo trục trái phải."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Khi tiến lại gần gương phẳng thì góc trông ảnh của mắt người quan sát sẽ:",
        "options": [
          "Tăng lên nên cảm thấy ảnh to hơn dù kích thước thật của ảnh không đổi",
          "Giảm đi",
          "Không đổi",
          "Biến mất"
        ],
        "correct": 0,
        "explanation": "Lại gần gương góc trông tăng lên làm ta có cảm giác ảnh to hơn."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Ứng dụng nào sau đây KHÔNG sử dụng gương phẳng?",
        "options": [
          "Kính lúp phóng to con kiến",
          "Gương soi trang điểm",
          "Kính tiềm vọng tàu ngầm",
          "Kính vạn hoa"
        ],
        "correct": 0,
        "explanation": "Kính lúp là thấu kính hội tụ, không dùng gương phẳng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một điểm sáng S cách mặt phẳng gương 35 cm. Ảnh S' của nó cách điểm sáng S một khoảng là:",
        "options": [
          "70 cm",
          "35 cm",
          "17,5 cm",
          "0 cm"
        ],
        "correct": 0,
        "explanation": "Khoảng cách SS' = 2d = 2 × 35 = 70 cm."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một vật đặt cách gương phẳng một đoạn d. Nếu dịch chuyển vật lại gần gương thêm 15 cm thì khoảng cách giữa vật và ảnh sẽ giảm đi:",
        "options": [
          "30 cm",
          "15 cm",
          "7,5 cm",
          "45 cm"
        ],
        "correct": 0,
        "explanation": "Vật lại gần 15 cm, ảnh lại gần 15 cm => khoảng cách vật và ảnh giảm 30 cm."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một người đứng trước gương phẳng nhìn thấy ảnh của mình cách mình 3 mét. Khoảng cách từ người đó đến gương phẳng là:",
        "options": [
          "1,5 mét",
          "3,0 mét",
          "0,75 mét",
          "6,0 mét"
        ],
        "correct": 0,
        "explanation": "d = 3 / 2 = 1,5 mét."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đặt một tấm bìa hình chữ cái 'L' trước một chiếc gương phẳng. Hình ảnh của tấm bìa trong gương có dạng giống chữ cái nào?",
        "options": [
          "Hình chữ L bị lật ngược trái phải (⅃)",
          "Chữ L xuôi",
          "Chữ T",
          "Chữ I"
        ],
        "correct": 0,
        "explanation": "Ảnh qua gương phẳng bị đảo trục trái - phải đối xứng."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Thị trường (vùng quan sát) của một chiếc gương phẳng sẽ mở rộng hơn khi:",
        "options": [
          "Người quan sát tiến lại gần gương hơn hoặc kích thước gương lớn hơn",
          "Người lùi xa gương",
          "Gương nhỏ đi",
          "Tắt bớt đèn"
        ],
        "correct": 0,
        "explanation": "Lại gần gương hoặc dùng gương lớn hơn làm mở rộng vùng quan sát."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Khi đứng bên bờ hồ nước phẳng lặng trong công viên vào ngày nắng, ta nhìn thấy hình ảnh ngọn tháp lộn ngược dưới mặt nước. Mặt nước đóng vai trò như:",
        "options": [
          "Một chiếc gương phẳng nằm ngang",
          "Một thấu kính phân kì",
          "Một tấm màn chắn",
          "Một nguồn sáng"
        ],
        "correct": 0,
        "explanation": "Mặt nước phẳng lặng hoạt động như một gương phẳng nằm ngang tạo ảnh đối xứng qua mặt nước."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về bản chất ảnh của vật tạo bởi gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Tia sáng từ vật chiếu đến gương phản xạ vào mắt người quan sát.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mắt nhìn thấy ảnh ảo vì các tia phản xạ đi vào mắt có đường kéo dài đi qua ảnh ảo.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu đặt một tấm bìa chắn phía sau gương tại vị trí của ảnh thì ảnh sẽ bị che khuất mất.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Ảnh ảo không thể chụp được bằng máy ảnh thông thường.",
            "correct": false
          }
        ],
        "explanation": "Máy ảnh đóng vai trò như mắt người, thu nhận chùm tia phản xạ nên hoàn toàn chụp được ảnh ảo trong gương."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tính chất khoảng cách và kích thước qua gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Vật cao 1 m thì ảnh trong gương phẳng cũng cao đúng 1 m.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nếu vật chuyển động với tốc độ 1 m/s vuông góc với gương thì ảnh cũng chuyển động với tốc độ 1 m/s đối với gương.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khoảng cách giữa vật và ảnh luôn gấp đôi khoảng cách từ vật đến gương.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu nghiêng gương một góc thì kích thước của ảnh sẽ bị co ngắn lại.",
            "correct": false
          }
        ],
        "explanation": "Gương phẳng luôn cho ảnh có kích thước bằng kích thước thật của vật, không bị co giãn."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một ngọn hải đăng cao 25 m xây dựng sát mép biển phẳng lặng:",
        "statements": [
          {
            "subId": "a",
            "text": "Mặt nước biển phẳng lặng phản chiếu ngọn hải đăng như một gương phẳng nằm ngang.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ảnh của đỉnh ngọn hải đăng nằm ở vị trí đối xứng qua mặt nước.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khoảng cách từ đỉnh ngọn hải đăng đến ảnh của nó dưới mặt nước là 50 m.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Ảnh của ngọn hải đăng dưới mặt nước là ảnh thật hứng được trên đáy biển.",
            "correct": false
          }
        ],
        "explanation": "Ảnh dưới mặt nước là ảnh ảo tạo bởi phản xạ của mặt nước."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khảo sát chuyển động của vật và ảnh qua gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Khi người đứng yên, gương dịch chuyển ra xa người 1 m thì ảnh dịch chuyển ra xa người 2 m.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi gương đứng yên, người dịch lại gần gương 0,5 m thì khoảng cách giữa người và ảnh giảm đi 1,0 m.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Người giơ tay trái lên thì ảnh trong gương giơ tay phải đối diện.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu nhắm mắt lại thì ảnh trong gương vẫn tiếp tục mở mắt nhìn.",
            "correct": false
          }
        ],
        "explanation": "Ảnh đối xứng chính xác mọi trạng thái biểu cảm cử động của vật tại cùng thời điểm."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Vật cách gương phẳng 25 cm. Khoảng cách từ ảnh đến gương phẳng là bao nhiêu cm?",
        "correctAnswer": "25",
        "explanation": "25 cm."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một chiếc hộp cao 10 cm. Độ cao của ảnh chiếc hộp trong gương phẳng là bao nhiêu cm?",
        "correctAnswer": "10",
        "explanation": "10 cm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khoảng cách giữa người và ảnh của mình trong gương phẳng là 2,4 m. Người cách gương phẳng bao nhiêu mét?",
        "correctAnswer": "1.2",
        "explanation": "d = 2,4 / 2 = 1,2 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một vật cách gương phẳng 60 cm. Nếu dịch gương lại gần vật 10 cm thì khoảng cách mới giữa vật và ảnh là bao nhiêu cm?",
        "correctAnswer": "100",
        "explanation": "d mới = 50 cm => 2d = 100 cm."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người lùi xa gương phẳng với tốc độ 0,5 m/s. Ảnh của người đó dịch chuyển ra xa người đó với tốc độ tương đối là bao nhiêu m/s?",
        "correctAnswer": "1",
        "explanation": "0,5 × 2 = 1,0 m/s."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Hai gương phẳng vuông góc với nhau tạo thành bao nhiêu ảnh ảo của một điểm sáng S đặt giữa hai gương?",
        "correctAnswer": "3",
        "explanation": "n = 360 / 90 - 1 = 4 - 1 = 3 ảnh."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước một chiếc gương phẳng treo thẳng đứng trên tường. Người đó nhận thấy có thể nhìn thấy ảnh của đầu và chân mình trong gương. Nếu người này bước lùi xa gương thêm 2 mét thì chiều cao phần gương tối thiểu để người đó nhìn thấy toàn bộ cơ thể mình sẽ:",
        "options": [
          "Không đổi (vẫn bằng một nửa chiều cao người đó)",
          "Tăng lên gấp đôi",
          "Giảm đi một nửa",
          "Tăng lên 2 mét"
        ],
        "correct": 0,
        "explanation": "Chiều cao tối thiểu của gương để nhìn thấy toàn thân luôn bằng H/2, hoàn toàn không phụ thuộc vào khoảng cách từ người đến gương."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một căn phòng có trần nhà cao 3,2 mét. Người ta gắn một chiếc gương phẳng tròn trên trần nhà. Trên sàn nhà ngay dưới gương đặt một ngọn nến cao 20 cm. Khoảng cách từ ngọn lửa của cây nến đến ảnh của ngọn lửa trong chiếc gương trên trần nhà là:",
        "options": [
          "6,0 mét",
          "6,4 mét",
          "3,0 mét",
          "3,2 mét"
        ],
        "correct": 0,
        "explanation": "Khoảng cách từ ngọn lửa đến gương trần: 3,2 - 0,2 = 3,0 m => Khoảng cách giữa ngọn lửa và ảnh: 2 × 3,0 = 6,0 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một diễn viên xiếc đứng thăng bằng trên một tấm ván gỗ trước một chiếc gương phẳng lớn. Diễn viên giơ một chiếc gậy dài 1,5 mét theo phương song song với mặt gương. Chiều dài ảnh của chiếc gậy trong gương và phương của ảnh chiếc gậy là:",
        "options": [
          "Dài 1,5 mét và song song với chiếc gậy",
          "Dài 3,0 mét và vuông góc",
          "Dài 0,75 mét và nghiêng",
          "Dài 1,5 mét và vuông góc"
        ],
        "correct": 0,
        "explanation": "Ảnh bằng vật (1,5 m) và song song với vật do vật đặt song song với mặt phẳng gương."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người lái xe ô tô quan sát qua gương phẳng chiếu hậu nhìn thấy một chiếc xe tải bám theo sau. Nếu xe tải đang chạy với tốc độ 60 km/h đuổi theo xe ô tô đang chạy với tốc độ 50 km/h thì qua gương chiếu hậu, tài xế ô tô sẽ thấy ảnh của chiếc xe tải đang tiến lại gần mình với tốc độ tương đối là:",
        "options": [
          "10 km/h",
          "20 km/h",
          "110 km/h",
          "5 km/h"
        ],
        "correct": 0,
        "explanation": "Tốc độ tương đối của xe tải so với ô tô là 60 - 50 = 10 km/h, nên ảnh xe tải qua gương tiến lại gần xe ô tô với tốc độ đúng bằng 10 km/h."
      }
    ]
  },
  "phys7_c5_b17_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 17: Ảnh của một vật tạo bởi gương phẳng - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_b17",
    "lessonName": "Bài 17: Ảnh của một vật tạo bởi gương phẳng",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Ảnh của một vật tạo bởi gương phẳng là:",
        "options": [
          "Ảnh ảo có kích thước bằng vật",
          "Ảnh thật có kích thước lớn hơn vật",
          "Ảnh thật có kích thước nhỏ hơn vật",
          "Ảnh ảo có kích thước gấp đôi vật"
        ],
        "correct": 0,
        "explanation": "Ảnh ảo, độ lớn bằng vật."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Nếu vật đặt cách gương phẳng 1 m thì ảnh của vật nằm ở vị trí nào sau gương?",
        "options": [
          "Ở phía sau gương cách gương 1 m",
          "Ở ngay trên mặt gương",
          "Ở trước gương 1 m",
          "Ở sau gương 2 m"
        ],
        "correct": 0,
        "explanation": "Ảnh ảo nằm sau gương, cách gương đúng 1 m."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Mặt gương phẳng chia đôi đoạn thẳng nối:",
        "options": [
          "Mỗi điểm của vật với ảnh tương ứng của nó",
          "Tia tới và tia phản xạ",
          "Đỉnh đầu và ngón chân",
          "Mặt trời và mặt trăng"
        ],
        "correct": 0,
        "explanation": "Mặt phẳng gương là mặt phẳng trung trực của đoạn thẳng nối vật và ảnh."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Dụng cụ quang học nào sau đây ứng dụng tính chất của gương phẳng để tạo ra các hoa văn đối xứng tuyệt đẹp khi xoay tròn?",
        "options": [
          "Kính vạn hoa",
          "Kính thiên văn",
          "Kính hiển vi",
          "Kính râm"
        ],
        "correct": 0,
        "explanation": "Kính vạn hoa ghép các gương phẳng tạo ảnh đối xứng."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Khi nhìn vào gương phẳng, ta thấy ảnh của mình chuyển động:",
        "options": [
          "Cùng tốc độ nhưng ngược chiều chuyển động của ta đối với gương",
          "Nhanh gấp đôi ta",
          "Chậm hơn ta",
          "Không chuyển động"
        ],
        "correct": 0,
        "explanation": "Ta tiến lại gần gương thì ảnh cũng tiến lại gần gương với cùng tốc độ đối với gương."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Kính tiềm vọng trang bị trên tàu ngầm dùng để:",
        "options": [
          "Quan sát quang cảnh và chướng ngại vật trên mặt nước khi tàu ngầm đang lặn",
          "Đo độ sâu biển",
          "Bắn ngư lôi",
          "Chiếu sáng đáy biển"
        ],
        "correct": 0,
        "explanation": "Quan sát trên mặt nước khi tàu đang lặn ngầm."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một bạn học sinh đứng cách gương phẳng 1,5 mét. Khoảng cách từ bạn học sinh đến ảnh của bạn là:",
        "options": [
          "3,0 mét",
          "1,5 mét",
          "0,75 mét",
          "4,5 mét"
        ],
        "correct": 0,
        "explanation": "2d = 2 × 1,5 = 3,0 m."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một ngọn nến đặt cách gương phẳng 10 cm. Nếu kéo ngọn nến lùi xa gương thêm 5 cm thì khoảng cách giữa ngọn nến và ảnh lúc này là:",
        "options": [
          "30 cm",
          "20 cm",
          "25 cm",
          "15 cm"
        ],
        "correct": 0,
        "explanation": "d mới = 10 + 5 = 15 cm => 2d = 30 cm."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một chiếc đồng hồ kim treo tường đối diện một gương phẳng đang chỉ 9 giờ đúng. Khi nhìn vào ảnh của chiếc đồng hồ trong gương, ta có cảm giác đồng hồ đang chỉ mấy giờ?",
        "options": [
          "3 giờ đúng",
          "9 giờ đúng",
          "6 giờ đúng",
          "12 giờ đúng"
        ],
        "correct": 0,
        "explanation": "Tính chất đảo trái phải của gương phẳng: kim giờ chỉ số 9 đối xứng thành số 3."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Một vật AB đặt song song với gương phẳng cách gương 20 cm. Ảnh A'B' của vật sẽ:",
        "options": [
          "Song song với AB và cách AB một khoảng 40 cm",
          "Vuông góc với AB",
          "Cắt AB",
          "Trùng với AB"
        ],
        "correct": 0,
        "explanation": "Vật song song với gương thì ảnh song song với vật và cách vật 2d = 40 cm."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Nếu ta bước lại gần gương phẳng một đoạn 30 cm thì khoảng cách giữa ta và ảnh của mình trong gương sẽ:",
        "options": [
          "Giảm đi 60 cm",
          "Giảm đi 30 cm",
          "Tăng lên 30 cm",
          "Không đổi"
        ],
        "correct": 0,
        "explanation": "Khoảng cách giảm: 2 × 30 = 60 cm."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một người nhìn thấy ảnh của ngọn đèn đường dưới một vũng nước mưa phẳng lặng trên sân. Điểm ảnh ảo của ngọn đèn nằm ở đâu?",
        "options": [
          "Ở dưới mặt đất (phía dưới đáy vũng nước một khoảng bằng độ cao ngọn đèn)",
          "Ở ngay trên mặt vũng nước",
          "Ở trên ngọn đèn",
          "Ở trong mắt người"
        ],
        "correct": 0,
        "explanation": "Ảnh ảo đối xứng qua mặt phẳng nước, nằm sâu phía dưới mặt nước một khoảng bằng độ cao ngọn đèn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các đặc điểm cơ bản của ảnh ảo qua gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Ảnh ảo không thể in hình lên một tấm bìa hay màn chắn đặt sau gương.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ảnh ảo cùng chiều với vật nhưng bị đảo ngược hướng trái - phải.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Độ lớn của ảnh luôn phụ thuộc vào chất lượng tráng bạc của gương phẳng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Vật và ảnh có cùng kích thước hình học 100%.",
            "correct": true
          }
        ],
        "explanation": "Chất lượng tráng bạc chỉ quyết định độ sáng rõ của ảnh, không quyết định kích thước ảnh."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về thị trường (vùng quan sát) của gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Thị trường của gương là vùng không gian phía trước gương mà mắt nhìn thấy ảnh của các vật trong đó.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Kích thước gương càng lớn thì thị trường quan sát càng rộng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Mắt càng đặt gần gương thì vùng quan sát được qua gương càng rộng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dịch chuyển mắt ra xa gương thì vùng quan sát qua gương mở rộng hơn.",
            "correct": false
          }
        ],
        "explanation": "Mắt ra xa gương thì góc trông gương thu hẹp lại, vùng quan sát bị thu nhỏ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát một biển báo chữ 'STOP' đặt đối diện một chiếc gương phẳng lớn:",
        "statements": [
          {
            "subId": "a",
            "text": "Chữ cái đầu tiên gần mép gương nhất cho ảnh gần gương nhất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thứ tự các chữ cái trong ảnh nhìn từ trái sang phải bị đảo ngược lại.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chữ 'O' và chữ 'T' có tính chất đối xứng trục nên ảnh của chúng không bị biến dạng hình dạng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Chữ 'S' và chữ 'P' trong ảnh sẽ hoàn toàn giống hệt chữ xuôi ban đầu.",
            "correct": false
          }
        ],
        "explanation": "Chữ 'S' và chữ 'P' không có trục đối xứng dọc nên ảnh bị đảo ngược trái phải rõ rệt."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một chú chim bói cá bay là là trên mặt hồ nước phẳng lặng ở độ cao 1,5 m:",
        "statements": [
          {
            "subId": "a",
            "text": "Ảnh của chú chim bói cá nằm dưới mặt nước cách mặt nước 1,5 m.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khoảng cách giữa chú chim và ảnh của nó là 3,0 m.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu chú chim sà xuống độ cao 0,5 m thì khoảng cách giữa chú chim và ảnh là 1,0 m.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khi chú chim chạm sát mặt nước thì ảnh của chú chim biến mất.",
            "correct": false
          }
        ],
        "explanation": "Khi chạm mặt nước d = 0 thì ảnh trùng khít với vật ngay tại mặt nước."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Vật cách gương phẳng 15 cm. Ảnh của vật cách gương phẳng bao nhiêu cm?",
        "correctAnswer": "15",
        "explanation": "15 cm."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một thanh sắt dài 50 cm. Ảnh của thanh sắt trong gương phẳng dài bao nhiêu cm?",
        "correctAnswer": "50",
        "explanation": "50 cm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khoảng cách giữa vật và ảnh qua gương phẳng là 80 cm. Vật cách gương bao nhiêu cm?",
        "correctAnswer": "40",
        "explanation": "d = 80 / 2 = 40 cm."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Vật cách gương phẳng 20 cm. Dịch chuyển vật ra xa thêm 15 cm thì khoảng cách vật - ảnh mới là bao nhiêu cm?",
        "correctAnswer": "70",
        "explanation": "d mới = 35 cm => 2d = 70 cm."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người tiến lại gần gương phẳng với tốc độ 1,2 m/s. Ảnh của người đó tiến lại gần người đó với tốc độ bao nhiêu m/s?",
        "correctAnswer": "2.4",
        "explanation": "1,2 × 2 = 2,4 m/s."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một chiếc gương phẳng treo thẳng đứng. Người cao 1,6 m cần một chiếc gương cao tối thiểu bao nhiêu mét để nhìn thấy toàn thân?",
        "correctAnswer": "0.8",
        "explanation": "H / 2 = 1,6 / 2 = 0,8 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách một bức tường có gắn một chiếc gương phẳng một khoảng 2 mét. Phía sau lưng người đó cách người đó 3 mét có một bức tranh phong cảnh treo trên tường đối diện. Người đó nhìn vào gương thì thấy ảnh của bức tranh. Khoảng cách từ mắt người đó đến ảnh của bức tranh trong gương là:",
        "options": [
          "7 mét",
          "5 mét",
          "8 mét",
          "4 mét"
        ],
        "correct": 0,
        "explanation": "Bức tranh cách gương: 2 + 3 = 5 mét => Ảnh bức tranh cách gương 5 mét. Mắt người cách gương 2 mét (ở giữa tranh và gương) => Khoảng cách từ mắt đến ảnh = 2 + 5 = 7 mét."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một điểm sáng S đặt trước gương phẳng cách gương 20 cm. Nếu cho gương phẳng quay một góc 30 độ quanh trục đi qua điểm tới thì quỹ đạo chuyển động của ảnh ảo S' sẽ là:",
        "options": [
          "Một cung tròn tâm tại trục quay bán kính 20 cm",
          "Một đường thẳng",
          "Một đường parabol",
          "Một hình elip"
        ],
        "correct": 0,
        "explanation": "Khoảng cách từ ảnh S' đến trục quay trên mặt phẳng gương luôn không đổi nên quỹ đạo là một cung tròn."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để đo chiều cao của một cột đèn chiếu sáng công cộng mà không cần trèo lên cột, một học sinh đặt một chiếc gương phẳng nhỏ nằm ngửa trên mặt đất tại điểm C cách chân cột đèn 6 mét. Học sinh lùi lại vị trí cách gương 1,5 mét và đứng thẳng thì nhìn thấy ảnh của đỉnh ngọn đèn trong gương. Biết mắt học sinh cách mặt đất 1,4 mét. Chiều cao của cột đèn là:",
        "options": [
          "5,6 mét",
          "4,2 mét",
          "6,0 mét",
          "7,0 mét"
        ],
        "correct": 0,
        "explanation": "Theo định luật phản xạ ánh sáng (tam giác đồng dạng): H / 6 = 1,4 / 1,5 => H = 1,4 × 6 / 1,5 = 5,6 mét."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước gương phẳng treo trên tường và nhìn thấy toàn thân. Nếu người đó đội thêm một chiếc mũ rộng vành cao 10 cm trên đầu thì để nhìn thấy toàn bộ từ chóp mũ đến gót chân, chiều cao tối thiểu của tấm gương cần phải tăng thêm ít nhất bao nhiêu cm?",
        "options": [
          "5 cm",
          "10 cm",
          "20 cm",
          "Không cần tăng"
        ],
        "correct": 0,
        "explanation": "Chiều cao tối thiểu của gương tăng thêm ΔH / 2 = 10 / 2 = 5 cm."
      }
    ]
  },
  "phys7_c5_rev_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương V - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương V",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Ta nhìn thấy một vật khi:",
        "options": [
          "Có ánh sáng từ vật đó truyền vào mắt ta",
          "Mắt ta mở to trong phòng tối",
          "Vật đó phát ra âm thanh",
          "Vật có màu đen"
        ],
        "correct": 0,
        "explanation": "Điều kiện nhìn thấy vật là có ánh sáng từ vật vào mắt."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Nguồn sáng là vật:",
        "options": [
          "Tự nó phát ra ánh sáng",
          "Hắt lại ánh sáng chiếu vào nó",
          "Trong suốt",
          "Màu đen"
        ],
        "correct": 0,
        "explanation": "Nguồn sáng tự nó phát ra ánh sáng."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong môi trường trong suốt và đồng tính, ánh sáng truyền theo đường nào?",
        "options": [
          "Đường thẳng",
          "Đường cong",
          "Đường gấp khúc",
          "Đường tròn"
        ],
        "correct": 0,
        "explanation": "Định luật truyền thẳng ánh sáng."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Theo định luật phản xạ ánh sáng, góc phản xạ r luôn:",
        "options": [
          "Bằng góc tới i",
          "Lớn hơn góc tới i",
          "Nhỏ hơn góc tới i",
          "Bằng 2 lần góc tới i"
        ],
        "correct": 0,
        "explanation": "Góc phản xạ luôn bằng góc tới: r = i."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Ảnh của một vật tạo bởi gương phẳng có tính chất:",
        "options": [
          "Là ảnh ảo, lớn bằng vật và đối xứng với vật qua mặt gương",
          "Là ảnh thật hứng được trên màn",
          "Là ảnh ảo nhỏ hơn vật",
          "Là ảnh thật lớn hơn vật"
        ],
        "correct": 0,
        "explanation": "Ảnh ảo qua gương phẳng lớn bằng vật và đối xứng qua gương."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hiện tượng Nhật thực xảy ra khi:",
        "options": [
          "Mặt Trăng nằm ở khoảng giữa Mặt Trời và Trái Đất",
          "Trái Đất nằm giữa Mặt Trời và Mặt Trăng",
          "Mặt Trời nằm giữa Trái Đất và Mặt Trăng",
          "Vào ban đêm"
        ],
        "correct": 0,
        "explanation": "Mặt Trăng che khuất Mặt Trời tạo ra nhật thực."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một vật sáng đặt cách gương phẳng 30 cm. Ảnh của vật cách gương phẳng một khoảng là:",
        "options": [
          "30 cm",
          "60 cm",
          "15 cm",
          "45 cm"
        ],
        "correct": 0,
        "explanation": "d' = d = 30 cm."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chiếu tia tới tới mặt gương phẳng với góc tới i = 35 độ. Góc phản xạ r bằng:",
        "options": [
          "35 độ",
          "70 độ",
          "55 độ",
          "90 độ"
        ],
        "correct": 0,
        "explanation": "r = i = 35 độ."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một người cao 1,65 mét đứng trước gương phẳng treo thẳng đứng. Chiều cao ảnh của người đó trong gương là:",
        "options": [
          "1,65 mét",
          "0,825 mét",
          "3,30 mét",
          "1,50 mét"
        ],
        "correct": 0,
        "explanation": "Độ lớn ảnh bằng vật: 1,65 m."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Chùm sáng phát ra từ một chiếc kính lúp khi đặt dưới ánh nắng Mặt Trời tụ lại một điểm là chùm sáng:",
        "options": [
          "Hội tụ",
          "Phân kì",
          "Song song",
          "Tròn"
        ],
        "correct": 0,
        "explanation": "Chùm sáng hội tụ."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tia tới hợp với mặt gương một góc 40 độ. Góc phản xạ r có giá trị bằng:",
        "options": [
          "50 độ",
          "40 độ",
          "80 độ",
          "100 độ"
        ],
        "correct": 0,
        "explanation": "i = 90° - 40° = 50° => r = 50°."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Kính tiềm vọng trang bị trên tàu ngầm được cấu tạo bởi:",
        "options": [
          "Hai gương phẳng đặt song song nghiêng góc 45 độ",
          "Một gương cầu lõm",
          "Hai thấu kính phân kì",
          "Một lăng kính ngũ giác"
        ],
        "correct": 0,
        "explanation": "Hai gương phẳng song song nghiêng 45° phản xạ ánh sáng hai lần."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về bản chất ánh sáng và sự truyền ánh sáng:",
        "statements": [
          {
            "subId": "a",
            "text": "Ánh sáng có thể truyền được trong môi trường chân không ngoài không gian vũ trụ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tia sáng được biểu diễn bằng một đoạn thẳng có mũi tên chỉ hướng truyền.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Bóng tối là vùng hoàn toàn không nhận được ánh sáng từ nguồn sáng do bị vật cản che khuất.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Mặt Trăng là nguồn sáng tự nhiên chiếu sáng Trái Đất vào ban đêm.",
            "correct": false
          }
        ],
        "explanation": "Mặt Trăng là vật sáng phản chiếu ánh sáng Mặt Trời, không phải nguồn sáng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các quy tắc trong định luật phản xạ ánh sáng của gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Tia phản xạ nằm trong mặt phẳng tới chứa tia tới và pháp tuyến.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đường pháp tuyến vuông góc với mặt gương tại điểm tới.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu tăng góc tới thì góc phản xạ cũng tăng theo một lượng tương ứng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu chiếu tia tới vuông góc với mặt gương thì góc tới bằng 90 độ.",
            "correct": false
          }
        ],
        "explanation": "Chiếu vuông góc với gương thì tia tới trùng pháp tuyến nên góc tới bằng 0 độ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một điểm sáng S đặt trước gương phẳng cách gương 40 cm:",
        "statements": [
          {
            "subId": "a",
            "text": "Ảnh ảo S' nằm phía sau gương cách gương 40 cm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khoảng cách giữa điểm sáng S và ảnh S' là 80 cm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu dịch chuyển S lại gần gương thêm 10 cm thì khoảng cách giữa S và S' là 60 cm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Ảnh S' có thể hứng được rõ nét trên một tấm bìa đặt tại vị trí của S'.",
            "correct": false
          }
        ],
        "explanation": "Ảnh S' là ảnh ảo không thể hứng được trên màn chắn."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hiện tượng thiên văn liên quan đến bóng tối trong vũ trụ:",
        "statements": [
          {
            "subId": "a",
            "text": "Nhật thực xảy ra khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nguyệt thực xảy ra khi Trái Đất nằm giữa Mặt Trời và Mặt Trăng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Vào ban đêm có thể quan sát được hiện tượng Nhật thực toàn phần.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Nguyệt thực toàn phần diễn ra khi Mặt Trăng đi hoàn toàn vào vùng bóng tối của Trái Đất.",
            "correct": true
          }
        ],
        "explanation": "Nhật thực chỉ có thể xảy ra vào ban ngày khi Mặt Trời xuất hiện trên bầu trời."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Ngọn nến đang cháy là nguồn sáng hay vật được chiếu sáng?",
        "correctAnswer": "Nguồn sáng",
        "explanation": "Nguồn sáng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Góc tới bằng 45 độ. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "45",
        "explanation": "r = 45 độ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Vật cách gương phẳng 50 cm. Khoảng cách giữa vật và ảnh là bao nhiêu cm?",
        "correctAnswer": "100",
        "explanation": "2d = 100 cm."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tia tới hợp với mặt gương góc 30 độ. Góc tới bằng bao nhiêu độ?",
        "correctAnswer": "60",
        "explanation": "i = 90 - 30 = 60 độ."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một người cao 1,7 mét đứng thẳng trước gương phẳng. Chiều cao tối thiểu của tấm gương để người đó nhìn thấy toàn thân là bao nhiêu mét? (Viết dưới dạng số thập phân)",
        "correctAnswer": "0.85",
        "explanation": "H / 2 = 1,7 / 2 = 0,85 m."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Giữ nguyên tia tới, quay gương phẳng quanh trục qua điểm tới một góc 15 độ. Tia phản xạ quay đi một góc bao nhiêu độ?",
        "correctAnswer": "30",
        "explanation": "2α = 30 độ."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Chiếu một tia sáng SI tới mặt phẳng gương nằm ngang với góc tới i = 40 độ. Muốn có tia phản xạ hướng thẳng đứng lên trên thì phải quay gương quanh trục qua điểm tới một góc bằng bao nhiêu độ?",
        "options": [
          "25 độ",
          "40 độ",
          "50 độ",
          "15 độ"
        ],
        "correct": 0,
        "explanation": "Tia tới hợp góc 40° với pháp tuyến (hợp góc 50° với phương nằm ngang). Muốn tia phản xạ thẳng đứng (90° so với ngang), góc hợp giữa tia tới và phản xạ = 50° + 90° = 140°. Góc tới mới i' = 70°. Góc quay gương = 70° - 40° = 30° hoặc 25° tùy chiều quay."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách một chiếc gương phẳng treo trên tường một khoảng 1,5 mét nhìn thấy ảnh của một bình hoa đặt sau lưng mình. Bình hoa cách người đó 2 mét. Khoảng cách từ mắt người đó đến ảnh của bình hoa trong gương là:",
        "options": [
          "5,0 mét",
          "3,5 mét",
          "4,0 mét",
          "7,0 mét"
        ],
        "correct": 0,
        "explanation": "Bình hoa cách gương: 1,5 + 2 = 3,5 m => Ảnh bình hoa cách gương 3,5 m. Người cách gương 1,5 m => Khoảng cách từ mắt đến ảnh = 1,5 + 3,5 = 5,0 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hai gương phẳng G1 và G2 đặt vuông góc với nhau (hợp góc 90 độ), mặt phản xạ quay vào nhau. Chiếu tia tới SI tới G1, sau khi phản xạ trên G1 tia sáng tiếp tục phản xạ trên G2 cho tia phản xạ JR. Nhận xét nào sau đây đúng về phương của tia JR so với tia SI?",
        "options": [
          "Tia JR luôn song song và ngược chiều với tia SI ban đầu với mọi góc tới",
          "Tia JR vuông góc với tia SI",
          "Tia JR hợp với tia SI góc 45 độ",
          "Tia JR trùng khít với tia SI"
        ],
        "correct": 0,
        "explanation": "Hệ hai gương vuông góc luôn phản xạ tia sáng quay ngược trở lại song song với tia tới."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một chú chó con chạy lại gần chiếc gương phẳng với tốc độ 0,5 m/s theo phương vuông góc với mặt gương. Tốc độ chuyển động tương đối của ảnh chú chó so với chú chó là:",
        "options": [
          "1,0 m/s",
          "0,5 m/s",
          "0,25 m/s",
          "2,0 m/s"
        ],
        "correct": 0,
        "explanation": "v_tương_đối = 0,5 + 0,5 = 1,0 m/s."
      }
    ]
  },
  "phys7_c5_rev_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương V - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương V",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật nào dưới đây là vật sáng?",
        "options": [
          "Gồm cả nguồn sáng và vật hắt lại ánh sáng chiếu vào nó",
          "Chỉ nguồn sáng",
          "Chỉ vật màu đen",
          "Chỉ gương soi"
        ],
        "correct": 0,
        "explanation": "Vật sáng gồm nguồn sáng và vật hắt lại ánh sáng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đường thẳng vuông góc với mặt phẳng gương tại điểm tới gọi là:",
        "options": [
          "Đường pháp tuyến",
          "Tia tới",
          "Tia phản xạ",
          "Trục chính"
        ],
        "correct": 0,
        "explanation": "Đường pháp tuyến vuông góc với mặt gương."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chùm sáng loe rộng ra từ một điểm phát sáng gọi là:",
        "options": [
          "Chùm sáng phân kì",
          "Chùm sáng hội tụ",
          "Chùm sáng song song",
          "Chùm tia laser"
        ],
        "correct": 0,
        "explanation": "Chùm phân kì loe rộng dần trên đường truyền."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Góc tạo bởi tia phản xạ và đường pháp tuyến gọi là:",
        "options": [
          "Góc phản xạ (r)",
          "Góc tới (i)",
          "Góc lệch",
          "Góc khúc xạ"
        ],
        "correct": 0,
        "explanation": "Góc phản xạ r."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Ảnh của một vật tạo bởi gương phẳng là ảnh ảo vì:",
        "options": [
          "Không hứng được trên màn chắn",
          "Hứng được trên màn chắn",
          "Lớn hơn vật",
          "Nhỏ hơn vật"
        ],
        "correct": 0,
        "explanation": "Ảnh ảo không hứng được trên màn chắn."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hiện tượng Nguyệt thực xảy ra khi:",
        "options": [
          "Trái Đất nằm ở giữa Mặt Trời và Mặt Trăng",
          "Mặt Trăng nằm giữa Mặt Trời và Trái Đất",
          "Mặt Trời nằm giữa Mặt Trăng và Trái Đất",
          "Vào ban ngày trưa hè"
        ],
        "correct": 0,
        "explanation": "Trái Đất che khuất ánh sáng Mặt Trời tới Mặt Trăng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một tia sáng chiếu tới gương phẳng với góc tới i = 50 độ. Góc hợp bởi tia tới và tia phản xạ là:",
        "options": [
          "100 độ",
          "50 độ",
          "25 độ",
          "80 độ"
        ],
        "correct": 0,
        "explanation": "i + r = 50° + 50° = 100°."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một vật cách gương phẳng 1,2 mét. Khoảng cách giữa vật và ảnh của nó trong gương phẳng là:",
        "options": [
          "2,4 mét",
          "1,2 mét",
          "0,6 mét",
          "3,6 mét"
        ],
        "correct": 0,
        "explanation": "2d = 2 × 1,2 = 2,4 m."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Chiếu tia tới hợp với mặt phẳng gương góc 45 độ. Góc phản xạ r bằng:",
        "options": [
          "45 độ",
          "90 độ",
          "30 độ",
          "60 độ"
        ],
        "correct": 0,
        "explanation": "i = 90° - 45° = 45° => r = 45°."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nếu người lùi ra xa gương phẳng thêm 0,5 m thì khoảng cách giữa người và ảnh sẽ:",
        "options": [
          "Tăng thêm 1,0 m",
          "Tăng thêm 0,5 m",
          "Giảm đi 0,5 m",
          "Không đổi"
        ],
        "correct": 0,
        "explanation": "Tăng thêm: 2 × 0,5 = 1,0 m."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tại sao chữ trên áo khi soi gương phẳng lại bị lật ngược trái phải?",
        "options": [
          "Do tính chất đối xứng trục của ảnh tạo bởi gương phẳng",
          "Do mắt người nhìn nhầm",
          "Do gương bị lỗi",
          "Do ánh sáng bị khúc xạ"
        ],
        "correct": 0,
        "explanation": "Ảnh qua gương phẳng đối xứng trục đảo hướng trái phải."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Vùng bóng nửa tối xuất hiện phía sau vật cản khi:",
        "options": [
          "Nguồn sáng có kích thước lớn",
          "Nguồn sáng là một điểm rất nhỏ",
          "Không có ánh sáng",
          "Vật cản trong suốt"
        ],
        "correct": 0,
        "explanation": "Nguồn sáng rộng tạo vùng bóng nửa tối."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các tính chất của đường truyền tia sáng:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong nước tinh khiết trong suốt đồng tính, tia sáng truyền theo đường thẳng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tia sáng truyền qua mặt phân cách giữa không khí và nước bị gãy khúc.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tia laser phát ra chùm sáng hội tụ về một điểm ở vô cực.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Bóng tối là hệ quả trực tiếp của định luật truyền thẳng ánh sáng.",
            "correct": true
          }
        ],
        "explanation": "Laser phát ra chùm sáng song song rất hẹp, không phải chùm hội tụ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về định luật phản xạ ánh sáng trên mặt gương:",
        "statements": [
          {
            "subId": "a",
            "text": "Góc phản xạ r luôn luôn bằng góc tới i.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tia phản xạ nằm trong mặt phẳng chứa tia tới và pháp tuyến.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tia tới và tia phản xạ nằm ở hai phía đối xứng qua đường pháp tuyến.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu quay gương một góc α thì tia phản xạ sẽ quay đi một góc đúng bằng α.",
            "correct": false
          }
        ],
        "explanation": "Khi quay gương một góc α thì tia phản xạ quay đi một góc 2α."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một cây nến cao 12 cm đặt thẳng đứng cách gương phẳng 25 cm:",
        "statements": [
          {
            "subId": "a",
            "text": "Ảnh của cây nến là ảnh ảo nằm sau gương 25 cm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chiều cao của ảnh cây nến trong gương là 12 cm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khoảng cách giữa cây nến và ảnh của nó là 50 cm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu đưa ngọn nến lại gần gương cách 10 cm thì chiều cao thật của ảnh sẽ tăng lên 24 cm.",
            "correct": false
          }
        ],
        "explanation": "Kích thước ảnh luôn bằng vật (12 cm), không phụ thuộc khoảng cách đến gương."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng gương phẳng trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Gương soi treo tường giúp mở rộng không gian phòng ở cảm quan.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bác sĩ nha khoa dùng gương nhỏ để khám các góc khuất của răng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kính vạn hoa tạo ra hoa văn đối xứng nhờ hệ gương phẳng đặt nghiêng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Gương phẳng được dùng làm kính lúp để phóng to chữ trong sách báo.",
            "correct": false
          }
        ],
        "explanation": "Kính lúp là thấu kính hội tụ phóng to ảnh, gương phẳng không phóng to kích thước vật."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tia sáng tới vuông góc với mặt gương phẳng thì góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "0",
        "explanation": "r = 0 độ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Mặt Trăng trong đêm rằm là nguồn sáng hay vật sáng?",
        "correctAnswer": "Vật sáng",
        "explanation": "Vật sáng."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Vật cách gương phẳng 1,5 mét. Ảnh của vật cách gương phẳng bao nhiêu mét?",
        "correctAnswer": "1.5",
        "explanation": "1,5 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tia tới hợp với pháp tuyến góc 25 độ. Góc hợp bởi tia tới và tia phản xạ là bao nhiêu độ?",
        "correctAnswer": "50",
        "explanation": "25 + 25 = 50 độ."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Khoảng cách giữa vật và ảnh là 70 cm. Vật cách gương bao nhiêu cm?",
        "correctAnswer": "35",
        "explanation": "70 / 2 = 35 cm."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một người cao 1,8 mét. Chiều cao tối thiểu của tấm gương để người đó nhìn thấy toàn thân là bao nhiêu mét?",
        "correctAnswer": "0.9",
        "explanation": "1,8 / 2 = 0,9 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước gương phẳng treo thẳng đứng. Người đó giơ tay phải lên chạm vào tai phải. Quan sát ảnh trong gương, ta thấy ảnh làm động tác gì đối diện?",
        "options": [
          "Giơ tay trái chạm vào tai trái của ảnh",
          "Giơ tay phải chạm tai phải",
          "Hai tay giơ lên",
          "Không cử động"
        ],
        "correct": 0,
        "explanation": "Tính chất đối xứng trục qua gương phẳng đảo trái phải: tay phải thành tay trái đối diện."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một tia sáng chiếu tới mặt gương phẳng nằm ngang tạo góc tới i = 30 độ. Nếu quay gương một góc 10 độ quanh trục tới sao cho góc tới tăng lên thành 40 độ thì tia phản xạ sẽ quay đi một góc bằng bao nhiêu độ so với phương tia phản xạ ban đầu?",
        "options": [
          "20 độ",
          "10 độ",
          "30 độ",
          "40 độ"
        ],
        "correct": 0,
        "explanation": "Góc quay của tia phản xạ = 2α = 2 × 10° = 20°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một bể bơi có đáy phẳng nằm ngang chứa đầy nước trong suốt sâu 1,5 mét. Đáy bể lát gạch hoa phản xạ ánh sáng như một chiếc gương phẳng. Một bóng đèn nhỏ gắn trên thành hồ cách mặt nước 0,5 mét chiếu xuống đáy hồ. Khoảng cách từ bóng đèn đến ảnh ảo của nó tạo bởi đáy hồ là:",
        "options": [
          "3,5 mét",
          "2,0 mét",
          "4,0 mét",
          "1,5 mét"
        ],
        "correct": 0,
        "explanation": "Khoảng cách từ đèn đến đáy hồ: 0,5 + 1,5 = 2,0 m => Khoảng cách giữa đèn và ảnh qua đáy hồ = 2 × 2,0 = 4,0 m."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người tiến lại gần gương phẳng với tốc độ 0,8 m/s theo phương vuông góc với mặt gương. Trong thời gian 5 giây, khoảng cách giữa người đó và ảnh của mình trong gương đã giảm đi bao nhiêu mét?",
        "options": [
          "8,0 mét",
          "4,0 mét",
          "2,0 mét",
          "16,0 mét"
        ],
        "correct": 0,
        "explanation": "Trong 5 s người đi được: 0,8 × 5 = 4,0 m => Khoảng cách người và ảnh giảm đi: 2 × 4,0 = 8,0 m."
      }
    ]
  },
  "phys7_c5_rev_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương V - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương V",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật nào sau đây là nguồn sáng?",
        "options": [
          "Ngọn đuốc đang cháy",
          "Mặt bàn gỗ",
          "Tấm gương soi",
          "Mảnh bìa trắng"
        ],
        "correct": 0,
        "explanation": "Ngọn đuốc đang cháy tự nó phát ra ánh sáng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi:",
        "options": [
          "Theo đường thẳng",
          "Theo đường zích zắc",
          "Theo đường tròn",
          "Theo đường elip"
        ],
        "correct": 0,
        "explanation": "Định luật truyền thẳng ánh sáng."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Mô hình biểu diễn một tia sáng là:",
        "options": [
          "Đường thẳng có mũi tên chỉ hướng truyền của ánh sáng",
          "Đường thẳng không có mũi tên",
          "Đường cong uốn lượn",
          "Hình chữ nhật"
        ],
        "correct": 0,
        "explanation": "Tia sáng là đường thẳng có mũi tên chỉ hướng."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Góc tới là góc tạo bởi:",
        "options": [
          "Tia tới và pháp tuyến tại điểm tới",
          "Tia tới và mặt gương",
          "Tia phản xạ và mặt gương",
          "Tia tới và tia phản xạ"
        ],
        "correct": 0,
        "explanation": "Góc tới i = góc(SIN)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Ảnh của một điểm sáng S qua gương phẳng được tạo bởi giao điểm của:",
        "options": [
          "Các đường kéo dài của các tia phản xạ",
          "Các tia phản xạ thực tế",
          "Các tia tới",
          "Đường pháp tuyến"
        ],
        "correct": 0,
        "explanation": "Giao điểm của các đường kéo dài tia phản xạ là ảnh ảo S'."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Kính vạn hoa tạo ra những hoa văn hình học biến hóa rực rỡ nhờ:",
        "options": [
          "Sự phản xạ ánh sáng nhiều lần qua hệ gương phẳng",
          "Bóng đèn led đổi màu",
          "Kính phóng đại",
          "Nước đổi màu"
        ],
        "correct": 0,
        "explanation": "Hệ gương phẳng phản xạ lặp đi lặp lại tạo hoa văn đối xứng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Chiếu tia tới tới mặt gương với góc tới i = 20 độ. Góc phản xạ r bằng:",
        "options": [
          "20 độ",
          "40 độ",
          "70 độ",
          "80 độ"
        ],
        "correct": 0,
        "explanation": "r = i = 20 độ."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một vật đặt cách gương phẳng 45 cm. Ảnh của vật cách vật một khoảng bằng:",
        "options": [
          "90 cm",
          "45 cm",
          "22,5 cm",
          "0 cm"
        ],
        "correct": 0,
        "explanation": "2d = 2 × 45 = 90 cm."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tia tới hợp với mặt gương một góc 50 độ. Góc tới i có giá trị là:",
        "options": [
          "40 độ",
          "50 độ",
          "80 độ",
          "20 độ"
        ],
        "correct": 0,
        "explanation": "i = 90° - 50° = 40°."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khi một người đứng cách gương phẳng 1 m và lùi xa gương thêm 1 m thì khoảng cách giữa người và ảnh là:",
        "options": [
          "4 mét",
          "2 mét",
          "3 mét",
          "1 mét"
        ],
        "correct": 0,
        "explanation": "Khoảng cách mới đến gương: 1 + 1 = 2 m => Khoảng cách người và ảnh: 2 × 2 = 4 m."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Vùng tối (bóng tối hoàn toàn) ở phía sau vật cản sáng là vùng:",
        "options": [
          "Hoàn toàn không nhận được ánh sáng từ nguồn sáng truyền tới",
          "Chỉ nhận được một phần ánh sáng từ nguồn sáng truyền tới",
          "Nhận được toàn bộ ánh sáng từ nguồn sáng",
          "Luôn phản chiếu ánh sáng mạnh mẽ"
        ],
        "correct": 0,
        "explanation": "Bóng tối nằm ở phía sau vật cản, hoàn toàn không nhận được ánh sáng từ nguồn sáng truyền tới."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Chùm sáng phát ra từ đèn pin rọi vào tường là chùm sáng:",
        "options": [
          "Phân kì",
          "Song song",
          "Hội tụ",
          "Tròn"
        ],
        "correct": 0,
        "explanation": "Chùm sáng loe rộng ra là chùm phân kì."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các hiện tượng quang học trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Bóng của cái cây in trên sân trường thay đổi chiều dài do vị trí Mặt Trời thay đổi.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ánh sáng từ ngọn đèn truyền thẳng trong không khí tĩnh lặng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nguyệt thực toàn phần diễn ra khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Vùng bóng nửa tối nhận được một phần ánh sáng từ nguồn sáng rộng.",
            "correct": true
          }
        ],
        "explanation": "Mặt Trăng ở giữa Mặt Trời và Trái Đất là Nhật thực, không phải Nguyệt thực."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về định luật phản xạ ánh sáng:",
        "statements": [
          {
            "subId": "a",
            "text": "Góc phản xạ luôn bằng góc tới: r = i.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tia phản xạ nằm trong mặt phẳng tới.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Góc hợp bởi tia tới và tia phản xạ bằng 2 lần góc tới: α = 2i.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu góc tới là 30 độ thì góc hợp bởi tia tới và mặt gương là 30 độ.",
            "correct": false
          }
        ],
        "explanation": "Góc hợp bởi tia tới và mặt gương là 90° - 30° = 60°."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát ảnh của một vật qua gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Vật cao 10 cm thì ảnh qua gương phẳng cũng cao đúng 10 cm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khoảng cách từ vật đến gương luôn bằng khoảng cách từ ảnh đến gương.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ảnh tạo bởi gương phẳng có thể in dấu lên tấm phim chụp ảnh đặt sau gương.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Người soi gương giơ tay trái thì ảnh giơ tay phải đối diện.",
            "correct": true
          }
        ],
        "explanation": "Ảnh ảo không thể in hình lên phim đặt phía sau gương vì không có ánh sáng hội tụ thực tế."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Kính tiềm vọng trên tàu ngầm quân sự:",
        "statements": [
          {
            "subId": "a",
            "text": "Sử dụng hai gương phẳng đặt nghiêng góc 45 độ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tia sáng phản xạ 2 lần đổi hướng tổng cộng 180 độ (xuống rồi ngang).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cho ảnh cùng chiều giúp quan sát dễ dàng các mục tiêu trên mặt nước.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Ảnh nhìn thấy qua kính tiềm vọng bị lộn ngược đầu.",
            "correct": false
          }
        ],
        "explanation": "Ảnh qua kính tiềm vọng là ảnh cùng chiều thẳng đứng."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Bóng đèn pin đang sáng là nguồn sáng hay vật sáng?",
        "correctAnswer": "Nguồn sáng",
        "explanation": "Nguồn sáng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Góc tới i = 50 độ. Góc phản xạ r bằng bao nhiêu độ?",
        "correctAnswer": "50",
        "explanation": "r = 50 độ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Vật cách gương phẳng 80 cm. Khoảng cách từ ảnh đến gương là bao nhiêu cm?",
        "correctAnswer": "80",
        "explanation": "80 cm."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tia tới hợp với mặt phẳng gương góc 60 độ. Góc tới bằng bao nhiêu độ?",
        "correctAnswer": "30",
        "explanation": "i = 90 - 60 = 30 độ."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Khoảng cách giữa vật và ảnh là 120 cm. Vật cách gương bao nhiêu cm?",
        "correctAnswer": "60",
        "explanation": "120 / 2 = 60 cm."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Người cao 1,5 mét cần chiếc gương phẳng treo tường cao tối thiểu bao nhiêu mét để nhìn thấy toàn thân?",
        "correctAnswer": "0.75",
        "explanation": "1,5 / 2 = 0,75 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một tia sáng chiếu tới mặt gương phẳng nằm ngang tạo góc tới i = 45 độ. Góc hợp bởi tia tới và tia phản xạ là bao nhiêu độ?",
        "options": [
          "90 độ",
          "45 độ",
          "180 độ",
          "60 độ"
        ],
        "correct": 0,
        "explanation": "i + r = 45° + 45° = 90°."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước gương phẳng cách gương 2 mét. Nếu người đó tiến lại gần gương thêm 0,5 mét thì khoảng cách giữa người đó và ảnh của mình trong gương lúc này là bao nhiêu mét?",
        "options": [
          "3,0 mét",
          "1,5 mét",
          "4,0 mét",
          "2,5 mét"
        ],
        "correct": 0,
        "explanation": "d mới = 2 - 0,5 = 1,5 m => 2d = 3,0 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để lấy ánh sáng Mặt Trời từ trên cao chiếu rọi thẳng đứng xuống đáy giếng sâu, biết tia sáng Mặt Trời chiếu nghiêng hợp với phương nằm ngang góc 40 độ. Cần đặt gương phẳng nghiêng góc bao nhiêu độ so với phương thẳng đứng?",
        "options": [
          "25 độ",
          "40 độ",
          "50 độ",
          "65 độ"
        ],
        "correct": 0,
        "explanation": "Góc giữa tia tới và tia phản xạ = 40° + 90° = 130°. Góc tới i = 65°. Mặt gương nghiêng 90° - 65° = 25° so với phương thẳng đứng."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người cao 1,6 m đứng trước gương phẳng treo thẳng đứng nhìn thấy toàn thân. Nếu người này bước lùi xa gương thêm 1 m thì kích thước thật của ảnh người đó trong gương:",
        "options": [
          "Vẫn bằng 1,6 m không hề thay đổi",
          "Bị nhỏ đi một nửa",
          "Tăng lên gấp đôi",
          "Tăng thêm 1 m"
        ],
        "correct": 0,
        "explanation": "Kích thước thật của ảnh luôn bằng kích thước vật (1,6 m)."
      }
    ]
  },
  "phys7_c5_rev_test4": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương V - Đề số 04",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương V",
    "testNum": 4,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Nguồn sáng tự nhiên lớn nhất cung cấp ánh sáng và sự sống cho Trái Đất là:",
        "options": [
          "Mặt Trời",
          "Mặt Trăng",
          "Ngọn đuốc",
          "Bóng đèn"
        ],
        "correct": 0,
        "explanation": "Mặt Trời là nguồn sáng tự nhiên vô tận."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo:",
        "options": [
          "Đường thẳng",
          "Đường cong",
          "Đường gãy khúc",
          "Đường sóng"
        ],
        "correct": 0,
        "explanation": "Định luật truyền thẳng ánh sáng."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chùm sáng song song gồm các tia sáng:",
        "options": [
          "Song song với nhau",
          "Giao nhau tại một điểm",
          "Loe rộng dần ra",
          "Cắt nhau vuông góc"
        ],
        "correct": 0,
        "explanation": "Các tia sáng song song với nhau."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Định luật phản xạ ánh sáng khẳng định:",
        "options": [
          "Góc phản xạ bằng góc tới",
          "Góc phản xạ lớn hơn góc tới",
          "Góc phản xạ nhỏ hơn góc tới",
          "Góc phản xạ luôn bằng 90 độ"
        ],
        "correct": 0,
        "explanation": "r = i."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Ảnh của một vật tạo bởi gương phẳng:",
        "options": [
          "Là ảnh ảo, độ lớn bằng vật",
          "Là ảnh thật, lớn hơn vật",
          "Là ảnh ảo, nhỏ hơn vật",
          "Là ảnh thật, nhỏ hơn vật"
        ],
        "correct": 0,
        "explanation": "Ảnh ảo, độ lớn bằng vật."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Vùng bóng tối là vùng phía sau vật cản:",
        "options": [
          "Hoàn toàn không nhận được ánh sáng từ nguồn sáng",
          "Nhận được một nửa ánh sáng",
          "Nhận được toàn bộ ánh sáng",
          "Sáng rực rỡ"
        ],
        "correct": 0,
        "explanation": "Không nhận được ánh sáng từ nguồn sáng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Chiếu tia tới tới gương phẳng với góc tới i = 55 độ. Góc phản xạ r bằng:",
        "options": [
          "55 độ",
          "35 độ",
          "110 độ",
          "90 độ"
        ],
        "correct": 0,
        "explanation": "r = i = 55 độ."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Vật đặt cách gương phẳng 70 cm. Ảnh của vật cách gương phẳng một khoảng là:",
        "options": [
          "70 cm",
          "140 cm",
          "35 cm",
          "0 cm"
        ],
        "correct": 0,
        "explanation": "d' = d = 70 cm."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tia tới hợp với mặt gương một góc 25 độ. Góc phản xạ r bằng:",
        "options": [
          "65 độ",
          "25 độ",
          "50 độ",
          "130 độ"
        ],
        "correct": 0,
        "explanation": "i = 90° - 25° = 65° => r = 65°."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khi một người tiến lại gần gương phẳng 0,4 m thì khoảng cách giữa người và ảnh giảm đi:",
        "options": [
          "0,8 m",
          "0,4 m",
          "0,2 m",
          "1,2 m"
        ],
        "correct": 0,
        "explanation": "Giảm: 2 × 0,4 = 0,8 m."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Hiện tượng nguyệt thực toàn phần diễn ra khi:",
        "options": [
          "Mặt Trăng đi vào vùng bóng tối của Trái Đất",
          "Mặt Trời đi vào bóng tối",
          "Trái Đất nằm giữa bóng Mặt Trăng",
          "Vào ban ngày"
        ],
        "correct": 0,
        "explanation": "Mặt Trăng bị bóng tối Trái Đất che khuất."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Kính vạn hoa tạo hoa văn đẹp mắt nhờ hiện tượng quang học nào?",
        "options": [
          "Hiện tượng phản xạ ánh sáng",
          "Hiện tượng khúc xạ ánh sáng",
          "Hiện tượng tán sắc ánh sáng",
          "Hiện tượng nhật thực"
        ],
        "correct": 0,
        "explanation": "Phản xạ ánh sáng liên tiếp qua hệ gương phẳng."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các đặc tính của tia sáng và nguồn sáng:",
        "statements": [
          {
            "subId": "a",
            "text": "Đom đóm tự phát sáng trong đêm là nguồn sáng sinh học.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ánh trăng là ánh sáng do Mặt Trăng tự phát ra.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Tia sáng được biểu diễn bằng đường thẳng có mũi tên định hướng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong chân không, ánh sáng truyền với tốc độ khoảng 300.000 km/s.",
            "correct": true
          }
        ],
        "explanation": "Mặt Trăng hắt lại ánh sáng Mặt Trời, không tự phát sáng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét các đặc điểm của hiện tượng phản xạ ánh sáng trên gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Tia phản xạ nằm trong mặt phẳng tới.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đường pháp tuyến vuông góc với mặt phẳng gương.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Góc tới tăng thì góc phản xạ cũng tăng theo.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tia phản xạ luôn luôn vuông góc với tia tới trong mọi trường hợp.",
            "correct": false
          }
        ],
        "explanation": "Chỉ vuông góc khi góc tới i = 45° (i + r = 90°)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát tính chất đối xứng của ảnh qua gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Vật và ảnh đối xứng nhau qua mặt phẳng gương.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khoảng cách từ vật đến gương bằng khoảng cách từ ảnh đến gương.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ảnh của bàn tay trái là bàn tay phải đối diện trong gương.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu đứng càng xa gương thì kích thước thật của ảnh sẽ teo nhỏ lại.",
            "correct": false
          }
        ],
        "explanation": "Kích thước thật của ảnh luôn bằng vật."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hiện tượng Nhật thực và Nguyệt thực trong tự nhiên:",
        "statements": [
          {
            "subId": "a",
            "text": "Nhật thực xảy ra khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nguyệt thực xảy ra khi Trái Đất nằm giữa Mặt Trời và Mặt Trăng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nhật thực toàn phần có thể quan sát được từ mọi nơi trên Trái Đất cùng lúc.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Bóng tối của Mặt Trăng trên Trái Đất tạo ra vùng nhật thực.",
            "correct": true
          }
        ],
        "explanation": "Vùng bóng tối của Mặt Trăng chỉ quét qua một dải hẹp trên Trái Đất."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Mặt gương phẳng là bề mặt phản xạ ánh sáng tốt hay kém?",
        "correctAnswer": "Tốt",
        "explanation": "Phản xạ rất tốt."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Góc tới bằng 65 độ. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "65",
        "explanation": "r = 65 độ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Vật cách gương phẳng 1 m. Khoảng cách giữa vật và ảnh là bao nhiêu mét?",
        "correctAnswer": "2",
        "explanation": "2d = 2 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tia tới hợp với mặt gương góc 45 độ. Góc tới bằng bao nhiêu độ?",
        "correctAnswer": "45",
        "explanation": "i = 90 - 45 = 45 độ."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Khoảng cách giữa vật và ảnh là 160 cm. Vật cách gương bao nhiêu cm?",
        "correctAnswer": "80",
        "explanation": "160 / 2 = 80 cm."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Người cao 1,74 m cần gương phẳng cao tối thiểu bao nhiêu mét để nhìn thấy toàn thân?",
        "correctAnswer": "0.87",
        "explanation": "1,74 / 2 = 0,87 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Chiếu một tia sáng SI tới mặt gương phẳng. Góc hợp bởi tia tới SI và tia phản xạ IR bằng 120 độ. Góc phản xạ r bằng:",
        "options": [
          "60 độ",
          "120 độ",
          "30 độ",
          "45 độ"
        ],
        "correct": 0,
        "explanation": "r = 120° / 2 = 60°."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách gương phẳng 1,6 m. Nếu người đó lùi xa gương thêm 0,4 m thì khoảng cách giữa người đó và ảnh của mình lúc này là bao nhiêu mét?",
        "options": [
          "4,0 mét",
          "2,0 mét",
          "3,2 mét",
          "3,6 mét"
        ],
        "correct": 0,
        "explanation": "d mới = 1,6 + 0,4 = 2,0 m => 2d = 4,0 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hai gương phẳng G1 và G2 đặt song song với nhau, mặt phản xạ quay vào nhau và cách nhau một khoảng 20 cm. Một điểm sáng S đặt chính giữa hai gương (cách mỗi gương 10 cm). Khoảng cách giữa hai ảnh ảo đầu tiên của điểm sáng S tạo bởi hai gương là:",
        "options": [
          "40 cm",
          "20 cm",
          "30 cm",
          "50 cm"
        ],
        "correct": 0,
        "explanation": "Ảnh S1 cách G1 là 10 cm (sau G1), ảnh S2 cách G2 là 10 cm (sau G2). Khoảng cách S1S2 = 10 + 20 + 10 = 40 cm."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tại sao khi chụp ảnh thẻ bằng gương phẳng, bức ảnh luôn bị lật ngược trái phải so với người thật ngoài đời?",
        "options": [
          "Do tính chất đối xứng trục qua mặt phẳng gương làm đảo ngược hướng trái - phải",
          "Do máy ảnh bị hỏng",
          "Do ánh sáng bị hấp thụ",
          "Do mắt người chụp nhìn sai"
        ],
        "correct": 0,
        "explanation": "Ảnh qua gương phẳng đối xứng trục đảo hướng trái phải."
      }
    ]
  },
  "phys7_c5_rev_test5": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương V - Đề số 05",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c5",
    "chapterTitle": "Chương V: Ánh sáng",
    "lessonId": "phys7_c5_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương V",
    "testNum": 5,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật nào sau đây tự nó phát ra ánh sáng?",
        "options": [
          "Ngọn nến đang cháy",
          "Mặt Trăng",
          "Mặt gương",
          "Mảnh bìa các-tông"
        ],
        "correct": 0,
        "explanation": "Ngọn nến đang cháy tự phát sáng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Ánh sáng truyền theo đường thẳng trong môi trường nào?",
        "options": [
          "Môi trường trong suốt và đồng tính",
          "Môi trường chân không có nhiều vật cản",
          "Môi trường nước đục",
          "Mọi môi trường"
        ],
        "correct": 0,
        "explanation": "Trong môi trường trong suốt và đồng tính."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chùm sáng hội tụ là chùm sáng gồm các tia sáng:",
        "options": [
          "Giao nhau tại một điểm",
          "Song song với nhau",
          "Loe rộng dần ra",
          "Không bao giờ cắt nhau"
        ],
        "correct": 0,
        "explanation": "Giao nhau tại một điểm."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Góc phản xạ là góc tạo bởi:",
        "options": [
          "Tia phản xạ và đường pháp tuyến tại điểm tới",
          "Tia phản xạ và mặt phẳng gương",
          "Tia tới và mặt phẳng gương",
          "Tia tới và tia phản xạ"
        ],
        "correct": 0,
        "explanation": "Góc phản xạ r = góc(NIR)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tính chất nào sau đây là của ảnh ảo tạo bởi gương phẳng?",
        "options": [
          "Là ảnh ảo, đối xứng với vật qua gương",
          "Là ảnh thật hứng được trên màn",
          "Là ảnh ảo lớn gấp đôi vật",
          "Là ảnh thật nhỏ hơn vật"
        ],
        "correct": 0,
        "explanation": "Ảnh ảo đối xứng với vật qua mặt gương."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Vùng bóng nửa tối là vùng:",
        "options": [
          "Chỉ nhận được một phần ánh sáng từ nguồn sáng",
          "Hoàn toàn tối đen",
          "Nhận đủ ánh sáng",
          "Sáng chói"
        ],
        "correct": 0,
        "explanation": "Chỉ nhận được một phần ánh sáng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Chiếu tia tới tới mặt gương với góc tới i = 75 độ. Góc phản xạ r bằng:",
        "options": [
          "75 độ",
          "15 độ",
          "150 độ",
          "90 độ"
        ],
        "correct": 0,
        "explanation": "r = i = 75 độ."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Vật đặt cách gương phẳng 1,1 mét. Ảnh của vật cách vật một khoảng là:",
        "options": [
          "2,2 mét",
          "1,1 mét",
          "0,55 mét",
          "3,3 mét"
        ],
        "correct": 0,
        "explanation": "2d = 2 × 1,1 = 2,2 m."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tia tới hợp với mặt gương một góc 35 độ. Góc tới i có giá trị là:",
        "options": [
          "55 độ",
          "35 độ",
          "70 độ",
          "110 độ"
        ],
        "correct": 0,
        "explanation": "i = 90° - 35° = 55°."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Một người đứng cách gương phẳng 2 mét, nếu tiến lại gần gương thêm 0,8 mét thì khoảng cách giữa người và ảnh là:",
        "options": [
          "2,4 mét",
          "1,2 mét",
          "3,2 mét",
          "1,6 mét"
        ],
        "correct": 0,
        "explanation": "d mới = 2 - 0,8 = 1,2 m => 2d = 2,4 m."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Hiện tượng nhật thực xảy ra vào thời điểm nào trong tháng âm lịch?",
        "options": [
          "Đầu tháng âm lịch (ngày trăng non)",
          "Ngày rằm âm lịch (ngày 15)",
          "Cuối tháng",
          "Bất kì ngày nào"
        ],
        "correct": 0,
        "explanation": "Nhật thực xảy ra vào ngày trăng non đầu tháng âm lịch khi Mặt Trăng ở giữa."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Kính tiềm vọng dùng hai gương phẳng nghiêng góc bao nhiêu độ so với trục ống ngắm?",
        "options": [
          "45 độ",
          "90 độ",
          "30 độ",
          "60 độ"
        ],
        "correct": 0,
        "explanation": "Nghiêng góc 45 độ."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các tính chất của sự truyền thẳng ánh sáng:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong không khí đồng tính, ánh sáng truyền đi theo đường thẳng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Người thợ xây ngắm dây rọi thẳng đứng là ứng dụng sự truyền thẳng ánh sáng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tia sáng truyền qua mặt nước không bị đổi hướng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Bóng tối của vật cản in trên tường là do ánh sáng truyền thẳng.",
            "correct": true
          }
        ],
        "explanation": "Khi truyền qua mặt nước (khúc xạ), tia sáng bị gãy khúc đổi hướng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các quy tắc phản xạ ánh sáng trên gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Góc phản xạ luôn luôn bằng góc tới.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tia phản xạ nằm trong mặt phẳng tới.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tia sáng tới vuông góc với mặt gương thì bật ngược trở lại theo phương cũ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Góc tới tăng thì góc phản xạ lại giảm đi.",
            "correct": false
          }
        ],
        "explanation": "Góc tới tăng thì góc phản xạ cũng tăng theo vì r = i."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát chuyển động của vật và ảnh qua gương phẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Người chạy lại gần gương 1 m thì ảnh cũng chạy lại gần gương 1 m.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ tương đối giữa người và ảnh gấp đôi tốc độ của người đối với gương.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kích thước của ảnh trong gương phẳng luôn bằng kích thước của người.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu soi gương trong phòng hoàn toàn tối đen không có ánh sáng thì ta vẫn nhìn thấy ảnh rõ nét.",
            "correct": false
          }
        ],
        "explanation": "Phải có ánh sáng chiếu vào người và hắt vào gương rồi tới mắt mới nhìn thấy ảnh."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hiện tượng bóng tối trong tự nhiên:",
        "statements": [
          {
            "subId": "a",
            "text": "Vùng bóng tối hoàn toàn không nhận được ánh sáng từ nguồn sáng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Vùng bóng nửa tối chỉ nhận được một phần ánh sáng từ nguồn sáng rộng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nguyệt thực xảy ra khi Trái Đất che khuất ánh sáng Mặt Trời tới Mặt Trăng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nhật thực toàn phần có thể nhìn thấy vào lúc nửa đêm.",
            "correct": false
          }
        ],
        "explanation": "Nhật thực chỉ quan sát được vào ban ngày."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Đèn pha ô tô đang sáng là nguồn sáng hay vật sáng?",
        "correctAnswer": "Nguồn sáng",
        "explanation": "Nguồn sáng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Góc tới bằng 80 độ. Góc phản xạ bằng bao nhiêu độ?",
        "correctAnswer": "80",
        "explanation": "r = 80 độ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Vật cách gương phẳng 1,2 mét. Khoảng cách giữa vật và ảnh là bao nhiêu mét?",
        "correctAnswer": "2.4",
        "explanation": "2d = 2,4 m."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tia tới hợp với mặt gương góc 10 độ. Góc tới bằng bao nhiêu độ?",
        "correctAnswer": "80",
        "explanation": "i = 90 - 10 = 80 độ."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Khoảng cách giữa vật và ảnh là 140 cm. Vật cách gương bao nhiêu cm?",
        "correctAnswer": "70",
        "explanation": "140 / 2 = 70 cm."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Người cao 1,68 mét cần chiếc gương phẳng treo tường cao tối thiểu bao nhiêu mét để nhìn thấy toàn thân?",
        "correctAnswer": "0.84",
        "explanation": "1,68 / 2 = 0,84 m."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Chiếu một tia sáng SI tới mặt gương phẳng nằm ngang. Góc hợp bởi tia tới SI và tia phản xạ IR là 80 độ. Góc tới i có độ lớn là:",
        "options": [
          "40 độ",
          "80 độ",
          "20 độ",
          "50 độ"
        ],
        "correct": 0,
        "explanation": "i = 80° / 2 = 40°."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người đứng cách gương phẳng 2,5 mét. Nếu người đó tiến lại gần gương thêm 1,0 mét thì khoảng cách giữa người đó và ảnh của mình trong gương lúc này là bao nhiêu mét?",
        "options": [
          "3,0 mét",
          "1,5 mét",
          "4,0 mét",
          "5,0 mét"
        ],
        "correct": 0,
        "explanation": "d mới = 2,5 - 1,0 = 1,5 m => 2d = 3,0 m."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một cây cột cờ cao 5 mét cắm thẳng đứng trên sân trường. Vào buổi trưa nắng, bóng của cột cờ in trên sân dài 2,5 mét. Một bạn học sinh đứng gần đó có bóng dài 0,75 mét. Chiều cao của bạn học sinh là:",
        "options": [
          "1,5 mét",
          "1,4 mét",
          "1,6 mét",
          "1,2 mét"
        ],
        "correct": 0,
        "explanation": "Tỉ lệ: 5 / 2,5 = 2 => Chiều cao bạn = 0,75 × 2 = 1,5 mét."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người đứng trước gương phẳng treo thẳng đứng và nhìn thấy toàn thân. Nếu người này bước lùi xa gương thêm 2 mét thì chiều cao tối thiểu của tấm gương để người đó vẫn nhìn thấy toàn thân sẽ:",
        "options": [
          "Không đổi (vẫn bằng một nửa chiều cao của người đó)",
          "Tăng lên gấp đôi",
          "Giảm đi một nửa",
          "Tăng thêm 2 mét"
        ],
        "correct": 0,
        "explanation": "Chiều cao tối thiểu của gương luôn bằng H/2 không phụ thuộc khoảng cách người đến gương."
      }
    ]
  },
  "phys7_c6_b18_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 18: Nam châm - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b18",
    "lessonName": "Bài 18: Nam châm",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Nam châm vĩnh cửu có khả năng hút mạnh các vật liệu làm từ chất nào sau đây?",
        "options": [
          "Sắt, thép, niken, coban",
          "Đồng, nhôm",
          "Vàng, bạc",
          "Nhựa, gỗ, cao su"
        ],
        "correct": 0,
        "explanation": "Nam châm hút các vật liệu từ như sắt, thép, niken, coban."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Mỗi thanh nam châm luôn luôn có bao nhiêu cực từ chính?",
        "options": [
          "2 cực (cực Bắc và cực Nam)",
          "1 cực duy nhất",
          "3 cực",
          "4 cực"
        ],
        "correct": 0,
        "explanation": "Nam châm luôn có hai cực từ: cực Bắc và cực Nam."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cực Bắc và cực Nam của nam châm thường được kí hiệu bằng các chữ cái in hoa lần lượt là:",
        "options": [
          "N (North) và S (South)",
          "S và N",
          "A và B",
          "P và Q"
        ],
        "correct": 0,
        "explanation": "N là North (Bắc), S là South (Nam)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi đưa hai cực cùng tên của hai thanh nam châm lại gần nhau thì chúng sẽ:",
        "options": [
          "Đẩy nhau",
          "Hút nhau",
          "Không tương tác",
          "Phát sáng"
        ],
        "correct": 0,
        "explanation": "Các cực cùng tên thì đẩy nhau."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Khi đưa hai cực khác tên của hai thanh nam châm lại gần nhau thì chúng sẽ:",
        "options": [
          "Hút nhau",
          "Đẩy nhau",
          "Không tương tác",
          "Làm mất từ tính"
        ],
        "correct": 0,
        "explanation": "Các cực khác tên thì hút nhau."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Thiết bị dùng để xác định phương hướng trên mặt đất dựa vào từ tính của kim nam châm là:",
        "options": [
          "La bàn",
          "Nhiệt kế",
          "Tốc kế",
          "Lực kế"
        ],
        "correct": 0,
        "explanation": "La bàn ứng dụng kim nam châm định hướng Bắc - Nam."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Vị trí nào trên một thanh nam châm thẳng có lực từ hút sắt mạnh nhất?",
        "options": [
          "Ở hai đầu cực của thanh nam châm",
          "Ở chính giữa thanh nam châm",
          "Ở mọi điểm đều bằng nhau",
          "Không có vị trí nào"
        ],
        "correct": 0,
        "explanation": "Lực từ mạnh nhất tập trung ở hai đầu cực, ở giữa hầu như bằng 0."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nếu bẻ gãy đôi một thanh nam châm thẳng thành hai nửa thì mỗi nửa sẽ:",
        "options": [
          "Trở thành một nam châm mới hoàn chỉnh có đủ hai cực Bắc và Nam",
          "Biến thành thanh sắt mất hết từ tính",
          "Chỉ còn một cực duy nhất",
          "Nổ tung"
        ],
        "correct": 0,
        "explanation": "Mỗi nửa gãy vẫn tạo thành một nam châm mới đầy đủ hai cực Bắc - Nam."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Kim nam châm tự do khi đứng cân bằng trên mặt đất luôn định hướng theo phương nào?",
        "options": [
          "Phương Bắc - Nam địa lí",
          "Phương Đông - Tây",
          "Phương thẳng đứng",
          "Phương ngẫu nhiên"
        ],
        "correct": 0,
        "explanation": "Kim nam châm luôn định hướng theo phương Bắc - Nam địa lí."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Vật nào sau đây KHÔNG BỊ nam châm hút?",
        "options": [
          "Một chiếc thìa bằng nhôm",
          "Một chiếc đinh sắt",
          "Một chiếc kẹp ghim bằng thép",
          "Một miếng niken"
        ],
        "correct": 0,
        "explanation": "Nhôm không phải là vật liệu từ nên không bị nam châm hút."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Để phân biệt một thanh sắt non chưa bị nhiễm từ và một thanh nam châm có hình dạng kích thước giống hệt nhau mà không dùng thêm vật dụng khác, người ta có thể:",
        "options": [
          "Đưa đầu thanh 1 chạm vào điểm chính giữa của thanh 2, nếu hút mạnh thì thanh 1 là nam châm",
          "Cân khối lượng",
          "Đo chiều dài",
          "Gõ vào nhau"
        ],
        "correct": 0,
        "explanation": "Đầu cực nam châm hút mạnh vào phần giữa của thanh sắt non, còn phần giữa nam châm không hút đầu thanh sắt."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tại sao người ta thường sơn màu đỏ cho cực Bắc (N) và màu xanh (hoặc trắng) cho cực Nam (S) của nam châm?",
        "options": [
          "Để người sử dụng dễ dàng nhận biết và phân biệt chính xác hai cực từ của nam châm",
          "Để chống gỉ sét",
          "Để nam châm hút mạnh hơn",
          "Là màu bắt buộc của kim loại"
        ],
        "correct": 0,
        "explanation": "Quy ước màu sơn giúp nhận biết nhanh hai cực từ."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các đặc điểm cơ bản của nam châm vĩnh cửu:",
        "statements": [
          {
            "subId": "a",
            "text": "Nam châm hút được các vật bằng sắt vụn, đinh thép, bột niken.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nam châm không hút được các vật bằng đồng đỏ, nhôm, bạc, vàng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tồn tại các thanh nam châm đơn cực chỉ có duy nhất một cực Bắc trong tự nhiên.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Lực hút từ của nam châm tác dụng xuyên qua được tấm bìa giấy mỏng hoặc tấm kính.",
            "correct": true
          }
        ],
        "explanation": "Trong tự nhiên không bao giờ tồn tại nam châm đơn cực (từ tích đơn cực)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tương tác giữa hai nam châm đặt gần nhau:",
        "statements": [
          {
            "subId": "a",
            "text": "Cực Bắc của nam châm 1 hút cực Nam của nam châm 2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cực Nam của nam châm 1 đẩy cực Nam của nam châm 2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cực Bắc của nam châm 1 đẩy cực Bắc của nam châm 2.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hai nam châm luôn luôn hút nhau trong mọi trường hợp đặt cạnh nhau.",
            "correct": false
          }
        ],
        "explanation": "Nếu đặt các cực cùng tên lại gần nhau thì chúng sẽ đẩy nhau."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Thí nghiệm treo một thanh nam châm bằng sợi chỉ mảnh ở giữa để thanh quay tự do:",
        "statements": [
          {
            "subId": "a",
            "text": "Sau khi dao động, thanh nam châm luôn dừng lại theo hướng Bắc - Nam.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đầu thanh nam châm chỉ về hướng Bắc địa lí gọi là cực Bắc của nam châm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu đưa một thanh đồng lại gần thì thanh nam châm sẽ bị hút xoay tít.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Nếu đưa cực Bắc của một nam châm khác lại gần cực Bắc của thanh đang treo thì thanh bị đẩy xoay đi.",
            "correct": true
          }
        ],
        "explanation": "Đồng không có từ tính nên không làm xoay nam châm."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng của nam châm trong đời sống hàng ngày:",
        "statements": [
          {
            "subId": "a",
            "text": "Miếng đệm từ ở cánh cửa tủ lạnh giúp cửa hít chặt vào thân tủ bảo toàn nhiệt độ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nắp hộp bút học sinh có gắn nam châm nhỏ giúp đóng mở nắp hộp dễ dàng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Bảng từ văn phòng sử dụng các viên nam châm nút nhỏ để đính giữ giấy tờ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nam châm vĩnh cửu có thể hút sạch các mảnh vỡ thủy tinh rơi trên sàn nhà.",
            "correct": false
          }
        ],
        "explanation": "Thủy tinh không có từ tính nên không thể dùng nam châm để hút."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cực Bắc của nam châm được kí hiệu bằng chữ cái in hoa nào?",
        "correctAnswer": "N",
        "explanation": "Chữ N (North)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cực Nam của nam châm được kí hiệu bằng chữ cái in hoa nào?",
        "correctAnswer": "S",
        "explanation": "Chữ S (South)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khi đưa hai cực Bắc của hai nam châm lại gần nhau, chúng hút nhau hay đẩy nhau?",
        "correctAnswer": "Đẩy nhau",
        "explanation": "Cùng tên thì đẩy nhau."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khi đưa cực Bắc của nam châm A lại gần cực Nam của nam châm B, chúng hút nhau hay đẩy nhau?",
        "correctAnswer": "Hút nhau",
        "explanation": "Khác tên thì hút nhau."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Kim la bàn bị lệch khỏi phương Bắc - Nam khi đưa vật nào lại gần? (Thanh sắt hay Thanh gỗ)",
        "correctAnswer": "Thanh sắt",
        "explanation": "Thanh sắt (hoặc nam châm) tương tác từ làm kim la bàn bị lệch."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một thanh nam châm bị bẻ gãy làm 3 đoạn ngắn. Tổng số cực từ của 3 đoạn ngắn đó là bao nhiêu cực?",
        "correctAnswer": "6",
        "explanation": "Mỗi đoạn có 2 cực => 3 × 2 = 6 cực."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Có một chiếc hộp đen kín bên trong chứa một vật bí ẩn. Khi đưa một cực của thanh nam châm lại gần chiếc hộp thì thấy chiếc hộp bị hút lại gần. Khi đảo đầu thanh nam châm và đưa lại gần thì chiếc hộp vẫn tiếp tục bị hút mãnh liệt. Vật chứa bên trong chiếc hộp đen có thể là vật nào sau đây?",
        "options": [
          "Một khối sắt non (chưa bị nhiễm từ)",
          "Một thanh nam châm vĩnh cửu",
          "Một miếng nhôm",
          "Một khối vàng"
        ],
        "correct": 0,
        "explanation": "Nếu là nam châm thì khi đổi đầu sẽ có một lần bị đẩy. Cả hai lần đều bị hút chứng tỏ vật trong hộp là chất từ tính (sắt non) chưa thành nam châm."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trong phòng thí nghiệm có một thanh kim loại chưa được đánh dấu cực. Khi đưa đầu A của thanh kim loại lại gần cực Bắc của một kim nam châm đang thăng bằng thì thấy cực Bắc của kim nam châm bị đẩy lùi ra xa. Kết luận nào sau đây chắc chắn đúng?",
        "options": [
          "Đầu A của thanh kim loại là cực Bắc của một thanh nam châm",
          "Đầu A chỉ là một thanh sắt thông thường",
          "Đầu A là cực Nam",
          "Thanh kim loại bằng nhôm"
        ],
        "correct": 0,
        "explanation": "Hiện tượng đẩy nhau là bằng chứng duy nhất và chắc chắn nhất chứng minh vật đó là nam châm và đầu A cùng tên với cực bị đẩy (cực Bắc)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tại sao khi sản xuất la bàn đi biển, vỏ hộp của chiếc la bàn luôn được làm bằng chất liệu đồng, nhôm hoặc nhựa cao cấp mà tuyệt đối không được làm bằng sắt hay thép?",
        "options": [
          "Vì sắt thép có từ tính sẽ làm lệch kim nam châm dẫn đến chỉ sai hướng định vị",
          "Vì sắt thép quá nặng",
          "Vì sắt thép đắt tiền hơn",
          "Vì nhựa trong suốt đẹp hơn"
        ],
        "correct": 0,
        "explanation": "Sắt thép gây nhiễu loạn từ trường bên trong la bàn làm kim nam châm chỉ sai."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người làm rơi một chiếc kim khâu bằng thép nhỏ xíu vào một thảm cỏ rậm rạp. Biện pháp thông minh và nhanh nhất để tìm lại chiếc kim khâu mà không làm đứt tay là:",
        "options": [
          "Dùng một thanh nam châm mạnh rà sát trên mặt thảm cỏ để nam châm hút dính chiếc kim thép lên",
          "Dùng kính lúp soi từng ngọn cỏ",
          "Tưới nước lên thảm cỏ",
          "Chờ ban đêm dùng đèn pin soi"
        ],
        "correct": 0,
        "explanation": "Kim khâu làm bằng thép có từ tính nên bị nam châm hút dính dễ dàng."
      }
    ]
  },
  "phys7_c6_b18_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 18: Nam châm - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b18",
    "lessonName": "Bài 18: Nam châm",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Nam châm hình móng ngựa (hình chữ U) có:",
        "options": [
          "Hai cực từ nằm ở hai đầu nhánh của chữ U",
          "Chỉ một cực ở đáy chữ U",
          "Không có cực từ",
          "Bốn cực từ"
        ],
        "correct": 0,
        "explanation": "Hai cực từ N và S nằm ở hai đầu nhánh chữ U."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Vật liệu nào sau đây là vật liệu từ bị nam châm hút mạnh?",
        "options": [
          "Coban (Cobalt)",
          "Gỗ thông",
          "Nhựa mica",
          "Thủy tinh hữu cơ"
        ],
        "correct": 0,
        "explanation": "Coban là chất từ tính mạnh bị nam châm hút."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Để xác định cực của một thanh nam châm bị mờ sơn kí hiệu, ta có thể dùng:",
        "options": [
          "Một chiếc la bàn đã biết rõ các cực",
          "Một chiếc nhiệt kế",
          "Một thanh nhôm",
          "Một cốc nước"
        ],
        "correct": 0,
        "explanation": "Dùng la bàn: cực Bắc của nam châm sẽ hút cực Nam của kim la bàn."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi treo tự do, đầu kim nam châm chỉ về hướng Nam địa lí được gọi là:",
        "options": [
          "Cực Nam của kim nam châm",
          "Cực Bắc của kim nam châm",
          "Cực Đông",
          "Cực Tây"
        ],
        "correct": 0,
        "explanation": "Đầu chỉ về hướng Nam là cực Nam (S)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Khi nung nóng một thanh nam châm vĩnh cửu lên nhiệt độ rất cao (trên điểm Curie) thì:",
        "options": [
          "Nam châm sẽ bị mất từ tính",
          "Nam châm hút mạnh hơn",
          "Nam châm phát nổ",
          "Nam châm đổi thành nam châm điện"
        ],
        "correct": 0,
        "explanation": "Nhiệt độ cao làm xáo trộn chuyển động nhiệt của các nguyên tử làm mất từ tính."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Chất nào sau đây KHÔNG BỊ nam châm hút trong mọi điều kiện?",
        "options": [
          "Đồng thau",
          "Sắt non",
          "Thép tôi",
          "Niken"
        ],
        "correct": 0,
        "explanation": "Đồng thau (hợp kim đồng - kẽm) không phải vật liệu từ."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Đặt hai thanh nam châm thẳng trên mặt bàn nhẵn sao cho cực Nam của thanh A đối diện với cực Nam của thanh B. Hiện tượng xảy ra là:",
        "options": [
          "Hai thanh nam châm đẩy nhau ra xa",
          "Hai thanh nam châm dính chặt vào nhau",
          "Hai thanh quay tròn",
          "Không có hiện tượng gì"
        ],
        "correct": 0,
        "explanation": "Các cực cùng tên (Nam - Nam) đẩy nhau."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một chiếc kim may bằng thép sau khi được cọ xát nhiều lần theo một chiều dọc theo thanh nam châm sẽ:",
        "options": [
          "Bị nhiễm từ và trở thành một chiếc kim nam châm nhỏ hút được ghim giấy",
          "Bị nóng chảy",
          "Bị mất khối lượng",
          "Biến thành vàng"
        ],
        "correct": 0,
        "explanation": "Phương pháp từ hóa: cọ xát làm thép bị nhiễm từ lâu dài thành nam châm."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tương tác từ giữa hai nam châm diễn ra thông qua:",
        "options": [
          "Từ trường tồn tại xung quanh mỗi nam châm",
          "Không khí thổi",
          "Ánh sáng chiếu vào",
          "Nhiệt độ phòng"
        ],
        "correct": 0,
        "explanation": "Từ trường là môi trường truyền tương tác từ."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khi một thanh nam châm hút một chiếc đinh sắt thì chiếc đinh sắt cũng:",
        "options": [
          "Tác dụng một lực hút trở lại thanh nam châm với độ lớn bằng lực nam châm hút nó",
          "Đẩy thanh nam châm",
          "Không tác dụng lực gì",
          "Làm thanh nam châm mất từ tính"
        ],
        "correct": 0,
        "explanation": "Theo định luật III Newton, hai vật tương tác lẫn nhau bằng hai lực trực đối."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tại sao đầu mũi của những chiếc tuốc-nơ-vít (tua vít) thợ sửa chữa hay dùng thường có từ tính nhẹ?",
        "options": [
          "Để hút dính giữ chặt các ốc vít bằng thép giúp thao tác vặn ốc ở các khe hẹp dễ dàng",
          "Để dẫn điện tốt hơn",
          "Để tránh bị mòn",
          "Để làm đẹp"
        ],
        "correct": 0,
        "explanation": "Đầu tua vít có từ tính giữ chặt đinh ốc bằng thép không bị rơi."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Nếu bẻ một thanh nam châm thành 4 đoạn ngắn thì ta thu được:",
        "options": [
          "4 thanh nam châm mới, mỗi thanh có đủ hai cực Bắc - Nam",
          "2 thanh có cực Bắc và 2 thanh có cực Nam",
          "Các thanh sắt vụn mất từ tính",
          "1 thanh nam châm lớn"
        ],
        "correct": 0,
        "explanation": "Mỗi đoạn cắt ra đều là một nam châm độc lập có đủ hai cực."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các tính chất đặc trưng của nam châm:",
        "statements": [
          {
            "subId": "a",
            "text": "Nam châm có khả năng hút các vật làm từ vật liệu từ tính.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Lực từ của nam châm có thể tác dụng từ xa mà không cần tiếp xúc trực tiếp.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nam châm có thể hút dính được các đồng tiền xu làm hoàn toàn bằng nhôm nguyên chất.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Hai cực cùng tên của nam châm thì đẩy nhau, khác tên thì hút nhau.",
            "correct": true
          }
        ],
        "explanation": "Nhôm không có từ tính nên nam châm không hút."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về cấu tạo và hoạt động của chiếc la bàn:",
        "statements": [
          {
            "subId": "a",
            "text": "Bộ phận cốt lõi của la bàn là một kim nam châm nhỏ có thể quay tự do trên một trục nhọn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mặt số của la bàn được chia thành 360 độ và ghi rõ các hướng chính Đông, Tây, Nam, Bắc.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi đặt la bàn gần một thanh nam châm mạnh, kim la bàn sẽ chỉ sai lệch hướng Bắc - Nam địa lí.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "La bàn chỉ có thể hoạt động chính xác vào ban ngày, ban đêm kim la bàn không quay.",
            "correct": false
          }
        ],
        "explanation": "Từ trường Trái Đất tồn tại liên tục ngày đêm nên la bàn hoạt động chính xác mọi lúc."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Học sinh thực hiện thí nghiệm xác định cực của một thanh nam châm cũ bị mất sơn màu:",
        "statements": [
          {
            "subId": "a",
            "text": "Treo thanh nam châm bằng sợi chỉ mảnh cho thăng bằng quay tự do trong phòng không có gió.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi thanh dừng lại, đầu thanh quay về hướng Bắc địa lí chính là cực Bắc của thanh nam châm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đầu thanh quay về hướng Nam địa lí chính là cực Nam của thanh nam châm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dù treo thanh ở bất kì vị trí nào cạnh cục sắt to thì thanh luôn chỉ đúng hướng Bắc địa lí.",
            "correct": false
          }
        ],
        "explanation": "Cạnh cục sắt hoặc nam châm khác có từ trường cục bộ làm thanh nam châm bị hút lệch hướng."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng nam châm vĩnh cửu trong thiết bị âm thanh (loa phóng thanh):",
        "statements": [
          {
            "subId": "a",
            "text": "Bên trong củ loa luôn có một khối nam châm vĩnh cửu hình xuyến mạnh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nam châm tương tác với cuộn dây mang dòng điện âm tần làm màng loa rung phát ra âm thanh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu tháo bỏ khối nam châm ra thì loa vẫn phát ra âm thanh to như cũ.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Lực từ của nam châm vĩnh cửu trong loa không đổi theo thời gian ở điều kiện bình thường.",
            "correct": true
          }
        ],
        "explanation": "Không có nam châm thì không có lực từ làm rung màng loa, loa không phát được âm thanh."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một thanh nam châm có bao nhiêu cực từ chính?",
        "correctAnswer": "2",
        "explanation": "2 cực (Bắc và Nam)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Kim nam châm tự do luôn định hướng theo phương nào? (Trả lời: Bắc - Nam hay Đông - Tây)",
        "correctAnswer": "Bắc - Nam",
        "explanation": "Phương Bắc - Nam."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Đưa cực Nam lại gần cực Nam của một nam châm khác thì chúng hút nhau hay đẩy nhau?",
        "correctAnswer": "Đẩy nhau",
        "explanation": "Đẩy nhau."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Đưa cực Nam của thanh nam châm lại gần cực Bắc của kim la bàn, chúng hút nhau hay đẩy nhau?",
        "correctAnswer": "Hút nhau",
        "explanation": "Khác tên hút nhau."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Dùng búa đập mạnh nhiều lần vào thanh nam châm có làm từ tính của nó giảm đi không? (Có hay Không)",
        "correctAnswer": "Có",
        "explanation": "Va đập cơ học mạnh làm xáo trộn các miền từ khiến từ tính bị suy giảm."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một thanh nam châm bị gãy làm 2 đoạn. Có tất cả bao nhiêu cực Bắc được tạo thành từ 2 đoạn đó?",
        "correctAnswer": "2",
        "explanation": "Mỗi đoạn có 1 cực Bắc => tổng có 2 cực Bắc."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Có hai thanh kim loại A và B bề ngoài giống hệt nhau. Một thanh là nam châm vĩnh cửu và một thanh là thép thường. Không dùng thêm bất kì dụng cụ nào khác, phương án tối ưu để xác định thanh nào là nam châm là:",
        "options": [
          "Lấy đầu của thanh A chạm vào điểm chính giữa của thanh B. Nếu đầu A hút mạnh thanh B thì thanh A là nam châm, nếu không hút thì thanh B là nam châm",
          "Gõ hai thanh vào nhau",
          "Thả rơi hai thanh",
          "Cọ xát hai thanh"
        ],
        "correct": 0,
        "explanation": "Chính giữa thanh nam châm không có từ tính, còn đầu thanh nam châm có từ tính mạnh nhất. Do đó đầu nam châm hút điểm giữa thanh thép, còn đầu thanh thép không bị điểm giữa nam châm hút."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người làm rơi chiếc nhẫn vàng 18K lẫn trong một đống cát và vụn sắt rỉ sét trên công trường. Người đó dùng một thanh nam châm mạnh rà trên đống cát. Kết quả thu được là gì?",
        "options": [
          "Nam châm sẽ hút sạch các vụn sắt rỉ sét ra khỏi đống cát, để lại chiếc nhẫn vàng trong cát giúp người đó tìm thấy dễ dàng",
          "Nam châm hút dính chiếc nhẫn vàng",
          "Nam châm hút cát",
          "Chiếc nhẫn vàng bị biến mất"
        ],
        "correct": 0,
        "explanation": "Vàng không bị nam châm hút, còn sắt bị hút sạch ra giúp tách nhẫn vàng dễ dàng."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Đặt ba thanh nam châm thẳng 1, 2, 3 nằm thẳng hàng trên mặt bàn nhẵn. Thanh 1 và thanh 2 hút nhau; thanh 2 và thanh 3 đẩy nhau. Nếu cực ngoài cùng bên trái của thanh 1 là cực Bắc thì cực ngoài cùng bên phải của thanh 3 là cực gì?",
        "options": [
          "Cực Bắc",
          "Cực Nam",
          "Không có cực",
          "Cả hai cực"
        ],
        "correct": 0,
        "explanation": "Thanh 1: [Bắc - Nam]. Vì hút thanh 2 => Thanh 2: [Bắc - Nam]. Vì thanh 2 và 3 đẩy nhau => Thanh 3: [Nam - Bắc] => Cực ngoài cùng bên phải của thanh 3 là cực Bắc."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tại sao các ổ đĩa cứng máy tính truyền thống (HDD), băng từ cát-xét và thẻ ngân hàng lại bị khuyến cáo tuyệt đối không được để gần các cục nam châm vĩnh cửu mạnh?",
        "options": [
          "Vì từ trường mạnh của nam châm sẽ làm xáo trộn và xóa sạch các mẫu dữ liệu từ tính nhị phân đã ghi trên bề mặt đĩa từ và thẻ",
          "Vì nam châm làm nóng chảy đĩa",
          "Vì nam châm làm thẻ bị đổi màu",
          "Vì thẻ bị dính chặt không gỡ ra được"
        ],
        "correct": 0,
        "explanation": "Từ trường mạnh phá hủy cấu trúc sắp xếp các hạt oxit từ tính mã hóa thông tin."
      }
    ]
  },
  "phys7_c6_b18_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 18: Nam châm - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b18",
    "lessonName": "Bài 18: Nam châm",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật nào sau đây có khả năng tương tác hút hoặc đẩy với một thanh nam châm khác?",
        "options": [
          "Một thanh nam châm thứ hai",
          "Một miếng gỗ khô",
          "Một cốc thủy tinh",
          "Một cục gôm tẩy"
        ],
        "correct": 0,
        "explanation": "Hai nam châm tương tác từ với nhau (hút hoặc đẩy)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tên gọi của hai cực từ của nam châm bắt nguồn từ:",
        "options": [
          "Khả năng định hướng theo hướng Bắc và hướng Nam của Trái Đất khi để tự do",
          "Tên nhà bác học phát minh",
          "Tên các hành tinh",
          "Màu sắc của sơn"
        ],
        "correct": 0,
        "explanation": "Định hướng theo cực Bắc và Nam của Trái Đất."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Vật liệu nào sau đây là vật liệu không có tính từ?",
        "options": [
          "Đồng nguyên chất",
          "Sắt",
          "Niken",
          "Thép"
        ],
        "correct": 0,
        "explanation": "Đồng là kim loại không có tính từ."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi treo lơ lửng một kim nam châm nhỏ thăng bằng thì trục của kim nam châm sẽ trùng với:",
        "options": [
          "Hướng Bắc - Nam địa lí",
          "Hướng Đông - Tây",
          "Đường xích đạo",
          "Phương thẳng đứng"
        ],
        "correct": 0,
        "explanation": "Trục kim nam châm định hướng theo phương Bắc - Nam."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong các trường hợp sau, trường hợp nào xảy ra lực đẩy giữa hai thanh nam châm?",
        "options": [
          "Đưa hai cực Nam lại gần nhau",
          "Đưa cực Bắc lại gần cực Nam",
          "Đưa cực Nam lại gần cực Bắc",
          "Đưa nam châm lại gần thanh sắt"
        ],
        "correct": 0,
        "explanation": "Cực cùng tên (Nam - Nam) đẩy nhau."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Bột mạt sắt rải đều trên một tờ bìa đặt trên thanh nam châm sẽ bị hút bám dày đặc nhất ở đâu?",
        "options": [
          "Ở hai đầu cực của thanh nam châm",
          "Ở giữa thanh",
          "Không bị hút",
          "Rải đều khắp nơi"
        ],
        "correct": 0,
        "explanation": "Mạt sắt bám nhiều nhất ở hai đầu cực nơi lực từ mạnh nhất."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Để bảo quản nam châm vĩnh cửu không bị suy giảm từ tính theo thời gian, người ta thường:",
        "options": [
          "Ghép hai cực khác tên của hai thanh nam châm bằng các miếng sắt non đệm ở đầu",
          "Nung nóng trong lửa",
          "Dùng búa đập thường xuyên",
          "Ngâm trong nước muối"
        ],
        "correct": 0,
        "explanation": "Dùng thanh sắt non nối hai cực khác tên khép kín mạch từ giúp bảo toàn từ tính."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một thanh sắt non được đặt tiếp xúc với cực Bắc của một thanh nam châm thì đầu kia của thanh sắt non sẽ:",
        "options": [
          "Trở thành cực Bắc tạm thời và có thể hút được các vụn sắt khác",
          "Trở thành cực Nam vĩnh viễn",
          "Mất hết tính chất",
          "Bị đẩy ra"
        ],
        "correct": 0,
        "explanation": "Sắt non bị nhiễm từ tạm thời do hưởng ứng từ, đầu xa mang từ tính cùng tên."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một chiếc kim khâu bằng thép khi bị rơi xuống khe sàn gỗ hẹp, dụng cụ tiện lợi nhất để lấy kim lên là:",
        "options": [
          "Một thanh nam châm nhỏ buộc vào đầu sợi dây",
          "Một chiếc đũa tre",
          "Một chiếc kẹp nhựa",
          "Một ống hút"
        ],
        "correct": 0,
        "explanation": "Nam châm hút kim thép dính chặt kéo lên."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Vì sao các cánh cửa tủ quần áo cao cấp thường lắp các miếng hít từ (nam châm nhỏ)?",
        "options": [
          "Để giữ cánh cửa luôn đóng khép chặt mà không cần chốt khóa cơ học phức tạp",
          "Để trang trí",
          "Để làm cửa nhẹ hơn",
          "Để mở cửa khó hơn"
        ],
        "correct": 0,
        "explanation": "Hút giữ cánh cửa êm ái và khép chặt."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Đặc điểm nào sau đây chứng minh một thanh kim loại ĐÃ BỊ NHIỄM TỪ thành nam châm?",
        "options": [
          "Nó có thể đẩy một cực xác định của kim nam châm tự do",
          "Nó có thể hút chiếc đinh sắt",
          "Nó có màu xám đen",
          "Nó dẫn điện tốt"
        ],
        "correct": 0,
        "explanation": "Lực đẩy là dấu hiệu duy nhất khẳng định vật đó là nam châm."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Các hạt mạt sắt dùng trong thí nghiệm từ học được làm từ chất nào?",
        "options": [
          "Sắt hoặc thép",
          "Nhôm",
          "Đồng",
          "Than chì"
        ],
        "correct": 0,
        "explanation": "Mạt sắt làm từ sắt/thép để nhiễm từ rõ nét."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về bản chất từ tính của vật chất:",
        "statements": [
          {
            "subId": "a",
            "text": "Sắt, thép, coban, niken là các vật liệu có tính chất từ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đồng, nhôm, gỗ, cao su là các vật liệu phi từ tính.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nam châm vĩnh cửu có thể hút được tất cả các kim loại có trong tự nhiên.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Lực từ có thể tác dụng xuyên qua chất lỏng và không khí.",
            "correct": true
          }
        ],
        "explanation": "Nam châm không hút được vàng, bạc, đồng, nhôm, chì..."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các cực từ của nam châm:",
        "statements": [
          {
            "subId": "a",
            "text": "Mỗi nam châm có ít nhất hai cực từ khác nhau.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cực Bắc sơn màu đỏ, kí hiệu chữ N.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cực Nam sơn màu xanh, kí hiệu chữ S.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hai cực cùng tên thì hút nhau mãnh liệt.",
            "correct": false
          }
        ],
        "explanation": "Cùng tên thì đẩy nhau."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Thí nghiệm nhiễm từ cho một thanh thép và một thanh sắt non:",
        "statements": [
          {
            "subId": "a",
            "text": "Sau khi cọ xát với nam châm, cả thanh sắt non và thép đều bị nhiễm từ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi đưa ra xa nam châm, thanh sắt non nhanh chóng mất hết từ tính.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thanh thép giữ được từ tính lâu dài và trở thành nam châm vĩnh cửu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Sắt non giữ từ tính tốt hơn thép nhiều lần.",
            "correct": false
          }
        ],
        "explanation": "Thép giữ từ tính lâu dài, sắt non khử từ rất nhanh."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng la bàn trong thám hiểm rừng rậm:",
        "statements": [
          {
            "subId": "a",
            "text": "La bàn giúp xác định phương hướng chính xác khi không nhìn thấy Mặt Trời.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cần giữ la bàn thăng bằng nằm ngang khi đọc số đo góc.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nên đặt la bàn cạnh một chiếc dao găm bằng thép lớn khi đo hướng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Đầu kim sơn đỏ của la bàn chỉ về hướng Bắc.",
            "correct": true
          }
        ],
        "explanation": "Dao găm bằng thép gây lệch kim la bàn, làm sai hướng."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cực mang kí hiệu chữ S của nam châm là cực gì? (Bắc hay Nam)",
        "correctAnswer": "Nam",
        "explanation": "Cực Nam (South)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Chất liệu sắt non có bị nam châm hút không? (Có hay Không)",
        "correctAnswer": "Có",
        "explanation": "Có bị hút mạnh."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hai cực Bắc của hai thanh nam châm để gần nhau sẽ hút hay đẩy?",
        "correctAnswer": "Đẩy",
        "explanation": "Đẩy nhau."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cực Bắc của nam châm hút cực nào của kim nam châm khác?",
        "correctAnswer": "Nam",
        "explanation": "Cực Nam."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một chiếc ghim giấy bằng thép dính vào nam châm có thể hút thêm một chiếc ghim khác không? (Có hay Không)",
        "correctAnswer": "Có",
        "explanation": "Ghim thép bị nhiễm từ tạm thời nên hút được ghim khác."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Vật liệu nào sau đây làm vỏ la bàn: Đồng hay Sắt?",
        "correctAnswer": "Đồng",
        "explanation": "Đồng (không nhiễm từ, không làm lệch kim la bàn)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu đệm từ Maglev chạy trên đường ray không ma sát nhờ hệ thống nam châm đặt ở gầm tàu và trên đường ray. Nguyên lí lực từ được ứng dụng ở đây là gì?",
        "options": [
          "Lực đẩy giữa các cực cùng tên của hệ thống nam châm điện nâng đoàn tàu lơ lửng trên mặt ray",
          "Lực hút của nam châm kéo tàu xuống",
          "Lực ma sát cực lớn",
          "Lực nâng khí động học"
        ],
        "correct": 0,
        "explanation": "Lực đẩy từ trường cùng tên nâng đoàn tàu bay lơ lửng cách mặt ray 1 - 2 cm triệt tiêu ma sát lăn."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một người có 3 thanh kim loại giống hệt nhau được đánh số 1, 2, 3. Khi đưa thanh 1 lại gần thanh 2 thì thấy chúng hút nhau. Khi đưa thanh 2 lại gần thanh 3 thì thấy chúng hút nhau. Khi đưa thanh 1 lại gần thanh 3 thì chúng đẩy nhau. Kết luận nào sau đây đúng nhất?",
        "options": [
          "Thanh 1 và thanh 3 là hai thanh nam châm, thanh 2 là thanh sắt",
          "Cả 3 thanh đều là nam châm",
          "Thanh 1 là sắt, thanh 2 và 3 là nam châm",
          "Cả 3 thanh đều là sắt"
        ],
        "correct": 0,
        "explanation": "1 và 3 đẩy nhau => 1 và 3 chắc chắn là nam châm. Cả 1 và 3 đều hút 2 ở mọi trường hợp => 2 là thanh sắt non."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Trong nhà máy tái chế rác thải công nghiệp, để tách các lon nước ngọt làm bằng sắt tây ra khỏi các lon nước ngọt làm bằng nhôm hỗn hợp, người ta sử dụng thiết bị nào sau đây hiệu quả nhất?",
        "options": [
          "Một băng chuyền chạy qua một tang trống từ tính (nam châm cực mạnh)",
          "Dùng quạt thổi gió",
          "Dùng sàng rung",
          "Dùng nước ngâm"
        ],
        "correct": 0,
        "explanation": "Tang trống từ tính hút giữ các lon sắt lại, còn lon nhôm không nhiễm từ rơi tự do ra ngoài giúp phân loại tự động."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một thanh nam châm thẳng được đặt trên một chiếc đĩa xốp nhẹ thả nổi trên chậu nước rộng. Khi đĩa xốp đứng yên thăng bằng, thanh nam châm sẽ nằm theo hướng nào?",
        "options": [
          "Trục thanh nam châm nằm theo hướng Bắc - Nam địa lí",
          "Nằm theo hướng Đông - Tây",
          "Quay tròn liên tục",
          "Chìm xuống đáy"
        ],
        "correct": 0,
        "explanation": "Đĩa xốp nổi giúp nam châm quay tự do như kim la bàn định hướng Bắc - Nam theo từ trường Trái Đất."
      }
    ]
  },
  "phys7_c6_b19_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 19: Từ trường - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b19",
    "lessonName": "Bài 19: Từ trường",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Không gian xung quanh nam châm hoặc xung quanh dòng điện có tồn tại một dạng vật chất gọi là:",
        "options": [
          "Từ trường",
          "Điện trường tĩnh",
          "Ánh sáng",
          "Nhiệt trường"
        ],
        "correct": 0,
        "explanation": "Xung quanh nam châm hoặc dòng điện có từ trường."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Dụng cụ dùng để nhận biết sự tồn tại của từ trường trong một vùng không gian là:",
        "options": [
          "Kim nam châm (nam châm thử)",
          "Nhiệt kế",
          "Vôn kế",
          "Thước đo"
        ],
        "correct": 0,
        "explanation": "Kim nam châm thử bị lệch hướng khi đặt trong từ trường."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hình ảnh các đường mạt sắt sắp xếp trật tự xung quanh nam châm được gọi là:",
        "options": [
          "Từ phổ",
          "Quang phổ",
          "Bản đồ nhiệt",
          "Sóng âm"
        ],
        "correct": 0,
        "explanation": "Từ phổ là hình ảnh các đường mạt sắt xung quanh nam châm."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Quy ước chiều của đường sức từ ở bên ngoài thanh nam châm thẳng đi:",
        "options": [
          "Ra từ cực Bắc (N), đi vào ở cực Nam (S)",
          "Ra từ cực Nam, đi vào ở cực Bắc",
          "Từ cực Đông sang cực Tây",
          "Từ dưới lên trên"
        ],
        "correct": 0,
        "explanation": "Quy ước chiều đường sức từ: 'Vào Nam Ra Bắc'."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Nơi nào có từ trường mạnh thì các đường sức từ ở đó sẽ:",
        "options": [
          "Dày (mau) hơn",
          "Thưa hơn",
          "Thẳng tắp",
          "Biến mất"
        ],
        "correct": 0,
        "explanation": "Từ trường mạnh thì đường sức từ mau (dày đặc)."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trái Đất của chúng ta hoạt động như một nam châm khổng lồ với cực từ nam nằm ở gần:",
        "options": [
          "Cực Bắc địa lí của Trái Đất",
          "Cực Nam địa lí của Trái Đất",
          "Đường xích đạo",
          "Tâm Trái Đất"
        ],
        "correct": 0,
        "explanation": "Cực từ nam của Trái Đất nằm ở vùng cực Bắc địa lí (do đó cực Bắc la bàn bị hút về cực Bắc địa lí)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Thí nghiệm lịch sử của nhà bác học Đan Mạch Oersted (Ơ-xtét) năm 1820 đã chứng minh:",
        "options": [
          "Xung quanh dòng điện có từ trường tác dụng lực từ làm lệch kim nam châm",
          "Dòng điện phát ra ánh sáng",
          "Nam châm phát ra điện",
          "Dòng điện có nhiệt độ"
        ],
        "correct": 0,
        "explanation": "Thí nghiệm Oersted phát hiện tác dụng từ của dòng điện."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Các đường sức từ có đặc điểm hình học nào sau đây?",
        "options": [
          "Là các đường cong khép kín không bao giờ cắt nhau",
          "Là các đoạn thẳng hở",
          "Là các đường tròn đồng tâm cắt nhau",
          "Là các đường xoắn ốc cắt nhau liên tục"
        ],
        "correct": 0,
        "explanation": "Đường sức từ là các đường cong khép kín không cắt nhau."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Hiện tượng Cực quang (Aurora) rực rỡ xuất hiện trên bầu trời hai vùng cực Trái Đất là kết quả của:",
        "options": [
          "Sự tương tác giữa các hạt mang điện từ gió Mặt Trời bị từ trường Trái Đất bẫy tương tác với khí quyển",
          "Ánh sáng phản chiếu từ băng tuyết",
          "Pháo hoa vũ trụ",
          "Đèn chiếu sáng"
        ],
        "correct": 0,
        "explanation": "Gió Mặt Trời tương tác với từ trường Trái Đất sinh ra cực quang."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tại sao từ trường Trái Đất lại có ý nghĩa sinh tử đối với sự sống của sinh quyển?",
        "options": [
          "Che chắn các luồng bức xạ hạt vũ trụ năng lượng cao nguy hiểm từ gió Mặt Trời",
          "Làm cho Trái Đất ấm lên",
          "Tạo ra oxy",
          "Tạo ra mưa rơi"
        ],
        "correct": 0,
        "explanation": "Từ quyển Trái Đất là lá chắn bảo vệ sinh quyển khỏi bức xạ hạt nguy hiểm."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi đặt một kim nam châm nhỏ trong từ trường của một thanh nam châm, kim nam châm sẽ:",
        "options": [
          "Định hướng theo phương của đường sức từ tại điểm đó",
          "Quay tròn liên tục không ngừng",
          "Bị rơi xuống đất",
          "Mất hết từ tính"
        ],
        "correct": 0,
        "explanation": "Kim nam châm định hướng dọc theo đường sức từ tại điểm đặt."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Nếu hai đường sức từ cắt nhau tại một điểm trong không gian thì tại điểm đó:",
        "options": [
          "Kim nam châm thử sẽ chỉ hai hướng khác nhau cùng lúc (điều này vô lí, chứng tỏ các đường sức từ không bao giờ cắt nhau)",
          "Kim nam châm đứng yên",
          "Từ trường bằng 0",
          "Nam châm phát nổ"
        ],
        "correct": 0,
        "explanation": "Tại mỗi điểm từ trường chỉ có một hướng duy nhất nên đường sức từ không cắt nhau."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về bản chất và tính chất của từ trường:",
        "statements": [
          {
            "subId": "a",
            "text": "Từ trường tồn tại xung quanh nam châm vĩnh cửu.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Từ trường tồn tại xung quanh dây dẫn có dòng điện chạy qua.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Từ trường tác dụng lực từ lên kim nam châm đặt trong nó.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Mắt người có thể trực tiếp nhìn thấy các đường từ trường trong không khí.",
            "correct": false
          }
        ],
        "explanation": "Từ trường là trường vật chất vô hình, mắt không nhìn thấy được."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về hình ảnh đường sức từ và từ phổ:",
        "statements": [
          {
            "subId": "a",
            "text": "Rắc mạt sắt lên tấm nhựa đặt trên nam châm rồi gõ nhẹ ta thu được từ phổ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đường sức từ có hướng đi ra từ cực Bắc và đi vào ở cực Nam bên ngoài nam châm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ở gần hai đầu cực của nam châm, các đường sức từ rất dày đặc chứng tỏ từ trường rất mạnh.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Ở càng xa nam châm, các đường sức từ càng mau hơn.",
            "correct": false
          }
        ],
        "explanation": "Càng xa nam châm thì từ trường càng yếu nên đường sức từ càng thưa thớt."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Thí nghiệm Oersted về tác dụng từ của dòng điện:",
        "statements": [
          {
            "subId": "a",
            "text": "Đặt một dây dẫn thẳng song song với trục của một kim nam châm đang thăng bằng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi chưa đóng công tắc điện, kim nam châm chỉ phương Bắc - Nam.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi đóng công tắc cho dòng điện chạy qua dây dẫn, kim nam châm bị lệch khỏi vị trí cân bằng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu ngắt dòng điện thì kim nam châm vẫn bị lệch mãi không quay về vị trí ban đầu.",
            "correct": false
          }
        ],
        "explanation": "Ngắt dòng điện thì từ trường của dây dẫn mất đi, kim nam châm quay về phương Bắc - Nam của Trái Đất."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Từ trường của Trái Đất (địa từ trường):",
        "statements": [
          {
            "subId": "a",
            "text": "Bắc cực từ của Trái Đất nằm ở vùng Nam cực địa lí.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nam cực từ của Trái Đất nằm ở vùng Bắc cực địa lí.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cực Bắc của kim la bàn bị hút về phía cực từ nam của Trái Đất (ở phương Bắc địa lí).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bão từ Mặt Trời hoàn toàn không ảnh hưởng gì đến mạng lưới truyền tải điện trên Trái Đất.",
            "correct": false
          }
        ],
        "explanation": "Bão từ mạnh có thể làm sập lưới điện và làm gián đoạn thông tin liên lạc vệ tinh."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Chiều đường sức từ ở bên ngoài thanh nam châm đi ra ở cực nào? (Bắc hay Nam)",
        "correctAnswer": "Bắc",
        "explanation": "Ra Bắc vào Nam."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Chiều đường sức từ ở bên ngoài thanh nam châm đi vào ở cực nào? (Bắc hay Nam)",
        "correctAnswer": "Nam",
        "explanation": "Đi vào ở cực Nam."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Xung quanh một dây dẫn có dòng điện chạy qua có tồn tại từ trường không? (Có hay Không)",
        "correctAnswer": "Có",
        "explanation": "Có từ trường (thí nghiệm Oersted)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hình ảnh các đường mạt sắt xung quanh nam châm được gọi là gì?",
        "correctAnswer": "Từ phổ",
        "explanation": "Từ phổ."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Nơi có từ trường mạnh thì các đường sức từ dày hay thưa?",
        "correctAnswer": "Dày",
        "explanation": "Dày (mau)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Hiện tượng dải ánh sáng rực rỡ trên bầu trời đêm vùng cực Trái Đất gọi là gì?",
        "correctAnswer": "Cực quang",
        "explanation": "Hiện tượng Cực quang (Aurora)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Tại sao khi một cơn bão từ (Geomagnetic storm) do các đợt bùng nổ bức xạ từ Mặt Trời quét qua Trái Đất, các thiết bị định vị GPS, sóng viễn thông vệ tinh và la bàn của tàu thuyền lại bị nhiễu loạn nghiêm trọng?",
        "options": [
          "Vì các hạt mang điện năng lượng cao từ gió Mặt Trời làm biến dạng mạnh mẽ từ trường Trái Đất, gây ra sự dao động hỗn loạn của kim la bàn và cản trở sóng điện từ",
          "Vì không khí bị bốc cháy",
          "Vì nước biển sôi lên",
          "Vì Trái Đất ngừng quay"
        ],
        "correct": 0,
        "explanation": "Bão từ làm biến dạng địa từ trường và ion hóa mạnh tầng điện li gây gián đoạn sóng vô tuyến."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một đoạn dây dẫn thẳng AB đặt theo phương nằm ngang có dòng điện một chiều không đổi chạy qua từ A sang B. Đặt một kim nam châm thử nhỏ ngay phía dưới dây dẫn. Khi dòng điện chạy qua, kim nam châm bị lệch góc 45 độ so với trục dây. Nếu đảo chiều dòng điện từ B sang A thì kim nam châm sẽ:",
        "options": [
          "Lệch theo chiều ngược lại so với ban đầu",
          "Vẫn lệch theo chiều cũ",
          "Không bị lệch nữa",
          "Quay tròn liên tục"
        ],
        "correct": 0,
        "explanation": "Đảo chiều dòng điện làm đảo chiều từ trường sinh ra xung quanh dây dẫn, do đó kim nam châm lệch theo chiều ngược lại."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nhiều loài chim di cư (như bồ câu, nhạn biển, ngỗng trời) và loài rùa biển có thể bay và bơi hàng nghìn kilômét xuyên lục địa và đại dương về đúng nơi sinh sản mà không bao giờ bị lạc đường. Khả năng định vị phi thường này chủ yếu dựa vào:",
        "options": [
          "Cơ quan cảm ứng từ sinh học nhạy cảm bên trong cơ thể giúp chúng cảm nhận được từ trường Trái Đất như một chiếc la bàn tự nhiên",
          "Chúng nhớ từng cái cây",
          "Chúng ngửi mùi gió",
          "Chúng bay theo đàn đông"
        ],
        "correct": 0,
        "explanation": "Các hạt tinh thể magnetit sinh học trong cơ thể chim và rùa biển hoạt động như la bàn sinh học định hướng theo địa từ trường."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Người ta rải mạt sắt lên một tấm kính đặt trên hai cực của một nam châm hình chữ U rồi gõ nhẹ. Kết quả quan sát thấy ở khoảng không gian giữa hai nhánh cực của nam châm hình chữ U, các đường mạt sắt là:",
        "options": [
          "Các đường thẳng song song và cách đều nhau (từ trường đều)",
          "Các vòng tròn đồng tâm",
          "Các đường zích zắc",
          "Các đám mạt sắt dồn vào một điểm"
        ],
        "correct": 0,
        "explanation": "Trong lòng khoảng không giữa hai cực nam châm chữ U là từ trường đều, các đường sức từ song song cách đều nhau."
      }
    ]
  },
  "phys7_c6_b19_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 19: Từ trường - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b19",
    "lessonName": "Bài 19: Từ trường",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tính chất cơ bản của từ trường là:",
        "options": [
          "Tác dụng lực từ lên kim nam châm đặt trong nó",
          "Làm nóng các vật",
          "Phát ra ánh sáng huỳnh quang",
          "Hút mọi vật bằng nhựa"
        ],
        "correct": 0,
        "explanation": "Tác dụng lực từ lên nam châm là đặc tính cơ bản của từ trường."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Để vẽ đường sức từ của một nam châm, người ta dựa vào:",
        "options": [
          "Hình ảnh các đường mạt sắt trong từ phổ",
          "Các tia sáng",
          "Hướng của gió",
          "Đường dây điện"
        ],
        "correct": 0,
        "explanation": "Đường sức từ mô phỏng từ phổ mạt sắt."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Quy tắc xác định chiều đường sức từ bên ngoài thanh nam châm là:",
        "options": [
          "Vào cực Nam, Ra cực Bắc",
          "Vào cực Bắc, Ra cực Nam",
          "Đi từ trong ra ngoài",
          "Đi từ dưới lên trên"
        ],
        "correct": 0,
        "explanation": "Chiều đường sức từ: 'Vào Nam Ra Bắc'."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nhà bác học nào đã phát hiện ra hiện tượng dòng điện tác dụng lực từ lên kim nam châm vào năm 1820?",
        "options": [
          "Oersted (Ơ-xtét)",
          "Newton",
          "Galileo",
          "Faraday"
        ],
        "correct": 0,
        "explanation": "Oersted phát hiện tác dụng từ của dòng điện năm 1820."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tại một điểm trong không gian, hướng của từ trường là hướng:",
        "options": [
          "Nam - Bắc của kim nam châm thử nằm cân bằng tại điểm đó",
          "Đông - Tây của kim nam châm",
          "Thẳng đứng",
          "Tùy ý"
        ],
        "correct": 0,
        "explanation": "Hướng từ trường là hướng Nam - Bắc của kim nam châm thử cân bằng."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Cực Bắc của kim la bàn định hướng về phía cực Bắc địa lí của Trái Đất là vì:",
        "options": [
          "Ở gần cực Bắc địa lí có cực từ Nam của Trái Đất hút cực Bắc của kim la bàn",
          "Ở cực Bắc có nhiều băng tuyết",
          "Ở cực Bắc lạnh hơn",
          "Trái Đất quay quanh trục"
        ],
        "correct": 0,
        "explanation": "Khác tên hút nhau: cực từ Nam của Trái Đất hút cực Bắc của kim la bàn."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi đưa kim nam châm thử lại gần một cuộn dây đang có dòng điện chạy qua, hiện tượng gì xảy ra?",
        "options": [
          "Kim nam châm bị quay lệch khỏi phương Bắc - Nam ban đầu",
          "Kim nam châm đứng yên",
          "Kim nam châm bị nóng chảy",
          "Không có hiện tượng gì"
        ],
        "correct": 0,
        "explanation": "Từ trường của dòng điện tác dụng lực từ làm quay kim nam châm."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Đặc điểm nào sau đây của đường sức từ là ĐÚNG?",
        "options": [
          "Mỗi điểm trong từ trường chỉ có một đường sức từ đi qua",
          "Các đường sức từ có thể cắt nhau",
          "Đường sức từ xuất phát từ cực Nam",
          "Đường sức từ là các đường thẳng hở"
        ],
        "correct": 0,
        "explanation": "Mỗi điểm chỉ có 1 đường sức từ đi qua, các đường không cắt nhau."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Ở hai cực của nam châm chữ U, các đường sức từ:",
        "options": [
          "Dày đặc và khép kín nối cực Bắc sang cực Nam",
          "Thưa thớt nhất",
          "Không đi qua hai cực",
          "Song song với thân nam châm"
        ],
        "correct": 0,
        "explanation": "Ở hai cực từ trường mạnh nhất nên đường sức từ tập trung dày đặc nhất."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Trái Đất có từ trường bao quanh tạo thành một vùng không gian bảo vệ gọi là:",
        "options": [
          "Từ quyển",
          "Khí quyển",
          "Thủy quyển",
          "Sinh quyển"
        ],
        "correct": 0,
        "explanation": "Từ quyển (Magnetosphere) bảo vệ Trái Đất."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Nếu ngắt dòng điện chạy qua dây dẫn thì từ trường xung quanh dây dẫn sẽ:",
        "options": [
          "Biến mất hoàn toàn",
          "Tồn tại vĩnh viễn",
          "Mạnh lên gấp đôi",
          "Đổi màu"
        ],
        "correct": 0,
        "explanation": "Ngắt điện thì từ trường của dòng điện lập tức biến mất."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tại sao các đường sức từ không bao giờ cắt nhau?",
        "options": [
          "Vì tại mỗi điểm trong từ trường, lực từ chỉ có một phương và một chiều xác định duy nhất",
          "Vì chúng rất thẳng",
          "Vì chúng bằng kim loại",
          "Vì chúng quá ngắn"
        ],
        "correct": 0,
        "explanation": "Từ trường tại mỗi điểm chỉ có một vectơ cảm ứng từ duy nhất xác định."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về không gian có từ trường:",
        "statements": [
          {
            "subId": "a",
            "text": "Từ trường tồn tại xung quanh thanh nam châm thẳng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Từ trường tồn tại xung quanh chiếc còi xe máy khi đang bấm còi có điện.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Xung quanh một cục pin đặt trên bàn chưa nối mạch điện có từ trường rất mạnh.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Xung quanh dây dẫn có dòng điện chạy qua có từ trường.",
            "correct": true
          }
        ],
        "explanation": "Cục pin chưa nối mạch (không có dòng điện chạy) thì không sinh ra từ trường xung quanh."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về quy ước chiều và hình dạng của đường sức từ:",
        "statements": [
          {
            "subId": "a",
            "text": "Đường sức từ là các đường cong có hướng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bên ngoài nam châm, chiều đường sức từ đi ra từ cực Bắc và đi vào ở cực Nam.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Bên trong lòng thanh nam châm, chiều đường sức từ đi từ cực Nam sang cực Bắc tạo thành vòng khép kín.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Các đường sức từ là những đường thẳng hở xuất phát từ vô cực.",
            "correct": false
          }
        ],
        "explanation": "Đường sức từ là các đường cong khép kín hoàn chỉnh."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát từ phổ của một nam châm thẳng bằng mạt sắt:",
        "statements": [
          {
            "subId": "a",
            "text": "Mạt sắt sau khi gõ nhẹ sẽ bị nhiễm từ trở thành các kim nam châm nhỏ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Các mạt sắt tự sắp xếp nối đuôi nhau thành các đường cong cong nối hai cực.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Mật độ các đường mạt sắt dày nhất ở hai đầu cực thanh nam châm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu thay mạt sắt bằng mạt nhôm mịn thì cũng thu được hình ảnh từ phổ y hệt.",
            "correct": false
          }
        ],
        "explanation": "Nhôm không phải chất từ tính nên không bị nhiễm từ và không sắp xếp thành từ phổ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng từ trường Trái Đất trong việc sử dụng la bàn quân sự:",
        "statements": [
          {
            "subId": "a",
            "text": "La bàn giúp chiến sĩ hành quân xác định mục tiêu trong đêm tối.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi sử dụng la bàn cần tránh xa các xe bọc thép, súng pháo và đường dây điện cao thế.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối thép lớn của xe tăng sẽ làm kim la bàn bị lệch hướng nghiêm trọng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "La bàn quân sự hoạt động tốt nhất khi đặt trực tiếp lên nắp hầm sắt thép.",
            "correct": false
          }
        ],
        "explanation": "Đặt lên nắp hầm bằng sắt sẽ làm kim la bàn bị hút lệch hoàn toàn."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Từ trường tác dụng lực gì lên kim nam châm đặt trong nó?",
        "correctAnswer": "Lực từ",
        "explanation": "Lực từ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tên nhà bác học người Đan Mạch làm thí nghiệm dòng điện làm lệch kim nam châm năm 1820 là ai?",
        "correctAnswer": "Oersted",
        "explanation": "Ơ-xtét (Oersted)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Bên ngoài nam châm, đường sức từ đi ra ở cực nào?",
        "correctAnswer": "Bắc",
        "explanation": "Cực Bắc."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Bên ngoài nam châm, đường sức từ đi vào ở cực nào?",
        "correctAnswer": "Nam",
        "explanation": "Cực Nam."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Các đường sức từ có cắt nhau tại điểm nào không? (Có hay Không)",
        "correctAnswer": "Không",
        "explanation": "Không bao giờ cắt nhau."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Vùng không gian bảo vệ bao quanh Trái Đất do từ trường tạo nên gọi là gì?",
        "correctAnswer": "Từ quyển",
        "explanation": "Từ quyển (Magnetosphere)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một sợi dây dẫn điện thẳng dài được chôn ngầm dưới lớp vữa của bức tường trong phòng. Để xác định chính xác vị trí sợi dây điện ngầm có dòng điện đang chạy qua mà không cần đục phá tường, người thợ điện có thể làm gì?",
        "options": [
          "Cầm một chiếc la bàn nhạy rà sát bề mặt tường, nơi nào kim la bàn bị lệch hướng mạnh nhất thì nơi đó có dây điện ngầm",
          "Dùng kính lúp soi tường",
          "Dùng búa gõ vào tường",
          "Dùng nhiệt kế đo tường"
        ],
        "correct": 0,
        "explanation": "Từ trường của dòng điện chạy trong dây dẫn ngầm sẽ tác dụng lực từ làm lệch kim la bàn khi rà sát."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Đặt hai thanh nam châm thẳng nằm thẳng hàng trên mặt bàn nhẵn sao cho hai cực Bắc quay vào nhau và cách nhau 5 cm. Rải mạt sắt lên tấm nhựa đặt phía trên hai cực và gõ nhẹ. Từ phổ quan sát được ở khoảng giữa hai cực Bắc có đặc điểm gì?",
        "options": [
          "Các đường mạt sắt bị bẻ cong tẽ ra hai bên và ở chính giữa có một điểm hoàn toàn không có mạt sắt bám (điểm trung hòa từ trường)",
          "Các đường mạt sắt nối thẳng giữa hai cực",
          "Mạt sắt dồn hết vào giữa",
          "Không có mạt sắt nào"
        ],
        "correct": 0,
        "explanation": "Hai cực cùng tên đẩy nhau tạo điểm trung hòa từ trường ở chính giữa, các đường sức từ tẽ cong ra ngoài không giao nhau."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Trạm vũ trụ quốc tế ISS bay quanh Trái Đất ở độ cao khoảng 400 km. Các phi hành gia trên trạm ISS vẫn được bảo vệ tương đối an toàn khỏi các bức xạ hạt nguy hiểm từ bão mặt trời là nhờ:",
        "options": [
          "Trạm ISS vẫn nằm trong phạm vi che chắn của từ quyển Trái Đất",
          "Trạm ISS có vỏ giáp dày 1 mét",
          "Không gian quanh ISS không có bức xạ",
          "ISS bay rất nhanh"
        ],
        "correct": 0,
        "explanation": "Từ quyển Trái Đất mở rộng ra không gian hàng chục nghìn kilômét, bao trùm và che chở trạm ISS."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một kim nam châm nhỏ thăng bằng trên trục nhọn. Người ta đưa một dây dẫn thẳng có dòng điện chạy qua đặt song song phía trên kim nam châm. Hiện tượng gì sẽ xảy ra nếu ta ngắt công tắc điện rồi lại đóng công tắc điện liên tục theo chu kì 1 giây?",
        "options": [
          "Kim nam châm sẽ dao động lắc qua lắc lại liên tục quanh trục thăng bằng",
          "Kim nam châm đứng yên",
          "Kim nam châm bị bay lên trần nhà",
          "Kim nam châm bị mất từ tính"
        ],
        "correct": 0,
        "explanation": "Đóng ngắt điện liên tục tạo ra từ trường biến thiên ngắt quãng tác dụng lực từ gián đoạn làm kim nam châm dao động lắc liên tục."
      }
    ]
  },
  "phys7_c6_b19_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 19: Từ trường - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b19",
    "lessonName": "Bài 19: Từ trường",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Từ trường là môi trường vật chất đặc biệt tồn tại xung quanh:",
        "options": [
          "Nam châm và dòng điện",
          "Các vật đứng yên bằng gỗ",
          "Cục than đá",
          "Bình chứa nước"
        ],
        "correct": 0,
        "explanation": "Xung quanh nam châm và dòng điện có từ trường."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Để phát hiện từ trường trong một căn phòng, dụng cụ đơn giản và hiệu quả nhất là:",
        "options": [
          "Kim nam châm thử",
          "Nhiệt kế thủy ngân",
          "Thước dây",
          "Cân đồng hồ"
        ],
        "correct": 0,
        "explanation": "Kim nam châm thử nhạy cảm với từ trường."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Các đường sức từ có chiều quy ước ở ngoài thanh nam châm là:",
        "options": [
          "Đi ra từ cực Bắc và đi vào ở cực Nam",
          "Đi ra từ cực Nam và đi vào ở cực Bắc",
          "Đi từ Đông sang Tây",
          "Không có chiều"
        ],
        "correct": 0,
        "explanation": "Quy ước: Ra Bắc Vào Nam."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tại vị trí nào xung quanh nam châm thì đường sức từ có mật độ dày đặc nhất?",
        "options": [
          "Gần hai cực từ của nam châm",
          "Ở rất xa nam châm",
          "Ở chính giữa thanh nam châm",
          "Ở phía trên cao"
        ],
        "correct": 0,
        "explanation": "Hai đầu cực có từ trường mạnh nhất nên đường sức từ dày đặc nhất."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Hiện tượng mạt sắt sắp xếp thành các đường cong nối hai cực của nam châm gọi là:",
        "options": [
          "Từ phổ",
          "Quang phổ",
          "Nhiệt phổ",
          "Âm phổ"
        ],
        "correct": 0,
        "explanation": "Hình ảnh mạt sắt sắp xếp gọi là từ phổ."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Bên ngoài Trái Đất, từ trường mở rộng ra không gian bao quanh địa cầu tạo thành:",
        "options": [
          "Từ quyển Trái Đất",
          "Tầng ozon",
          "Khí quyển",
          "Tầng đối lưu"
        ],
        "correct": 0,
        "explanation": "Từ quyển (Magnetosphere)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Thí nghiệm Oersted phát hiện mối liên hệ chặt chẽ giữa hai hiện tượng nào trong tự nhiên?",
        "options": [
          "Hiện tượng điện và hiện tượng từ",
          "Hiện tượng điện và nhiệt",
          "Hiện tượng quang và âm",
          "Hiện tượng cơ và hóa"
        ],
        "correct": 0,
        "explanation": "Thí nghiệm Oersted mở đầu cho thuyết điện từ học (mối liên hệ giữa điện và từ)."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Đường sức từ của nam châm chữ U trong khoảng không gian giữa hai nhánh cực là:",
        "options": [
          "Các đường thẳng song song cách đều nhau",
          "Các vòng tròn đồng tâm",
          "Các đường cong ngoằn ngoèo",
          "Các đường xoắn ốc"
        ],
        "correct": 0,
        "explanation": "Từ trường đều giữa hai cực gồm các đường thẳng song song cách đều."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cực từ bắc của Trái Đất nằm ở:",
        "options": [
          "Gần cực Nam địa lí của Trái Đất",
          "Gần cực Bắc địa lí",
          "Đường xích đạo",
          "Tâm địa cầu"
        ],
        "correct": 0,
        "explanation": "Cực từ bắc của Trái Đất nằm ở vùng cực Nam địa lí."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Vì sao các phi hành gia ngoài không gian khi đáp xuống Mặt Trăng lại không thể dùng la ban từ để định hướng?",
        "options": [
          "Vì Mặt Trăng không có từ trường toàn cầu mạnh như Trái Đất",
          "Vì Mặt Trăng quá nóng",
          "Vì la bàn bị nặng",
          "Vì không có oxy"
        ],
        "correct": 0,
        "explanation": "Mặt Trăng không có từ trường địa cầu mạnh nên kim la bàn không định hướng được."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một kim nam châm nhỏ tự do đặt trong từ trường sẽ luôn nằm theo phương:",
        "options": [
          "Tiếp tuyến với đường sức từ tại điểm đó",
          "Vuông góc với đường sức từ",
          "Hợp góc 45 độ với đường sức từ",
          "Thẳng đứng lên trời"
        ],
        "correct": 0,
        "explanation": "Trục kim nam châm trùng với tiếp tuyến của đường sức từ tại điểm đặt."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Nếu bẻ cong một thanh nam châm thẳng thành hình chữ U thì từ trường ở khoảng giữa hai đầu cực sẽ:",
        "options": [
          "Mạnh hơn nhiều so với khi để thẳng",
          "Bị biến mất hoàn toàn",
          "Yếu đi",
          "Không đổi"
        ],
        "correct": 0,
        "explanation": "Uốn cong hai cực lại gần nhau làm từ trường ở khe hở cực kỳ mạnh và tập trung."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các đặc trưng hình học của đường sức từ:",
        "statements": [
          {
            "subId": "a",
            "text": "Đường sức từ là những đường cong khép kín kín hoàn chỉnh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Các đường sức từ tuyệt đối không bao giờ cắt nhau.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nơi từ trường yếu thì các đường sức từ sắp xếp thưa thớt.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bên ngoài nam châm, đường sức từ đi ra từ cực Nam và đi vào cực Bắc.",
            "correct": false
          }
        ],
        "explanation": "Quy ước bên ngoài: đi ra ở cực Bắc và đi vào ở cực Nam."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về thí nghiệm đặt kim nam châm cạnh dây dẫn có dòng điện:",
        "statements": [
          {
            "subId": "a",
            "text": "Dòng điện sinh ra từ trường tác dụng lực từ làm quay kim nam châm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi đổi chiều dòng điện thì chiều quay của kim nam châm cũng bị đổi ngược lại.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dòng điện càng lớn thì lực từ tác dụng lên kim nam châm càng mạnh.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Thí nghiệm này chứng minh dòng điện phát ra sóng ánh sáng nhìn thấy.",
            "correct": false
          }
        ],
        "explanation": "Thí nghiệm chứng minh dòng điện sinh ra từ trường, không liên quan ánh sáng phát ra."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát từ phổ của hai thanh nam châm đặt khác tên gần nhau (Bắc đối diện Nam):",
        "statements": [
          {
            "subId": "a",
            "text": "Các đường mạt sắt nối liền giữa cực Bắc của thanh này sang cực Nam của thanh kia.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mật độ mạt sắt giữa hai cực rất dày đặc chứng tỏ lực hút rất mạnh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hai thanh nam châm hút chặt vào nhau nếu để tự do.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Các đường mạt sắt bị bẻ cong tẽ ra xa không nối nhau.",
            "correct": false
          }
        ],
        "explanation": "Khác tên hút nhau nên các đường mạt sắt nối liền liên tục giữa hai cực."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Từ trường Trái Đất và tác dụng bảo vệ sinh quyển:",
        "statements": [
          {
            "subId": "a",
            "text": "Lõi nóng chảy của Trái Đất quay tạo ra địa từ trường khổng lồ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Từ trường làm lệch hướng các hạt mang điện năng lượng cao từ gió Mặt Trời.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cực quang là dấu hiệu thị giác của sự tương tác bão từ tại hai cực Trái Đất.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu Trái Đất mất hoàn toàn từ trường thì bầu khí quyển vẫn không bị ảnh hưởng gì.",
            "correct": false
          }
        ],
        "explanation": "Nếu mất từ trường, gió Mặt Trời sẽ thổi bay khí quyển như đã từng xảy ra với Sao Hỏa."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Vùng không gian xung quanh dòng điện có tồn tại từ trường không? (Có hay Không)",
        "correctAnswer": "Có",
        "explanation": "Có từ trường."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Đường sức từ bên ngoài thanh nam châm đi ra ở cực nào?",
        "correctAnswer": "Bắc",
        "explanation": "Cực Bắc."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nơi từ trường yếu thì đường sức từ dày hay thưa?",
        "correctAnswer": "Thưa",
        "explanation": "Thưa."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hình ảnh mạt sắt sắp xếp quanh nam châm gọi là gì?",
        "correctAnswer": "Từ phổ",
        "explanation": "Từ phổ."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Kim nam châm dùng để thử từ trường gọi là nam châm gì?",
        "correctAnswer": "Nam châm thử",
        "explanation": "Nam châm thử."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Các đường sức từ có cắt nhau không? (Có hay Không)",
        "correctAnswer": "Không",
        "explanation": "Không bao giờ cắt nhau."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một bạn học sinh đặt một chiếc la bàn trên mặt bàn học. Bất ngờ bạn thấy kim la bàn quay lệch góc 30 độ khỏi hướng Bắc - Nam. Khi bạn nhấc chiếc laptop đang cắm sạc ra xa khỏi bàn thì kim la bàn lập tức quay trở về chỉ đúng hướng Bắc - Nam. Hiện tượng kim la bàn bị lệch lúc đầu là do:",
        "options": [
          "Bộ sạc và dòng điện chạy trong laptop đã tạo ra từ trường xung quanh tác dụng lực từ làm lệch kim la bàn",
          "Laptop quá nóng",
          "Màn hình laptop phát sáng",
          "Do pin laptop bị hỏng"
        ],
        "correct": 0,
        "explanation": "Dòng điện trong thiết bị điện tử sinh ra từ trường cục bộ làm lệch kim la bàn."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một khung dây tròn mang dòng điện không đổi đặt thẳng đứng trong mặt phẳng kinh tuyến từ của Trái Đất. Tại tâm của khung dây đặt một kim nam châm nhỏ thăng bằng. Khi đóng khóa điện, kim nam châm chịu tác dụng đồng thời của hai từ trường: từ trường Trái Đất và từ trường của dòng điện trong khung dây. Trục của kim nam châm sẽ định hướng như thế nào?",
        "options": [
          "Định hướng theo phương của từ trường tổng hợp của hai từ trường nói trên",
          "Chỉ theo hướng cũ",
          "Chỉ thẳng đứng",
          "Quay tròn liên tục"
        ],
        "correct": 0,
        "explanation": "Kim nam châm định hướng theo vectơ từ trường tổng hợp tại điểm đặt."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Các nhà địa chất học khi đi tìm kiếm các mỏ quặng sắt ngầm dưới lòng đất thường sử dụng thiết bị đo từ trường (từ kế) đo độ biến thiên địa từ trường trên mặt đất. Cơ sở khoa học của phương pháp thăm dò này là:",
        "options": [
          "Các mỏ quặng sắt có từ tính cao sẽ làm tăng cục bộ cường độ từ trường Trái Đất tại khu vực đó (gây dị thường từ)",
          "Quặng sắt phát ra nhiệt độ cao",
          "Quặng sắt làm đất đổi màu",
          "Quặng sắt phát ra sóng âm"
        ],
        "correct": 0,
        "explanation": "Dị thường từ (Magnetic anomaly): quặng sắt từ hóa làm tăng đột biến từ trường mặt đất giúp định vị mỏ quặng."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tại sao khi vẽ đường sức từ của một nam châm, người ta phải vẽ mũi tên định hướng trên mỗi đường cong mà không vẽ đường trơn không có mũi tên?",
        "options": [
          "Vì đường sức từ là đường có hướng, mũi tên thể hiện chiều quy ước của từ trường (đi ra từ cực Bắc và đi vào ở cực Nam)",
          "Để trang trí cho đẹp",
          "Để phân biệt với tia sáng",
          "Để đếm số lượng đường"
        ],
        "correct": 0,
        "explanation": "Đường sức từ có hướng xác định, mũi tên chỉ hướng của lực từ tác dụng lên cực Bắc của nam châm thử."
      }
    ]
  },
  "phys7_c6_b20_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 20: Chế tạo nam châm điện đơn giản - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b20",
    "lessonName": "Bài 20: Chế tạo nam châm điện đơn giản",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cấu tạo cơ bản của một nam châm điện đơn giản bao gồm những bộ phận nào?",
        "options": [
          "Một cuộn dây dẫn bọc cách điện quấn quanh một lõi sắt non và nguồn điện",
          "Hai thanh nam châm vĩnh cửu gắn đối diện nhau",
          "Một thanh đồng nối với hai cực của bóng đèn",
          "Một sợi dây cao su dẫn điện quấn quanh đinh nhôm"
        ],
        "correct": 0,
        "explanation": "Nam châm điện gồm cuộn dây dẫn bọc cách điện quấn quanh lõi sắt non, khi có dòng điện chạy qua thì sinh ra từ trường."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tác dụng nào của dòng điện được ứng dụng trực tiếp để chế tạo nam châm điện?",
        "options": [
          "Tác dụng từ",
          "Tác dụng nhiệt",
          "Tác dụng phát sáng",
          "Tác dụng hóa học"
        ],
        "correct": 0,
        "explanation": "Dòng điện chạy qua dây dẫn sinh ra từ trường xung quanh (tác dụng từ)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Bộ phận nào trong nam châm điện có vai trò làm tăng cường độ mạnh của từ trường lên rất nhiều lần?",
        "options": [
          "Lõi sắt non",
          "Lớp vỏ nhựa bọc ngoài",
          "Công tắc ngắt điện",
          "Dây chỉ buộc cố định"
        ],
        "correct": 0,
        "explanation": "Lõi sắt non bị nhiễm từ mạnh, tăng cường tác dụng từ của cuộn dây."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hiện tượng gì xảy ra với từ tính của nam châm điện có lõi sắt non khi ngắt dòng điện chạy qua cuộn dây?",
        "options": [
          "Từ tính biến mất gần như ngay lập tức",
          "Từ tính tăng gấp đôi",
          "Đảo ngược hai cực từ",
          "Vẫn giữ nguyên vĩnh viễn"
        ],
        "correct": 0,
        "explanation": "Khi ngắt dòng điện, lõi sắt non mất hầu hết từ tính ngay lập tức."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Để nhận biết cuộn dây dẫn quấn quanh đinh sắt đã trở thành nam châm điện hay chưa, ta có thể đưa đầu đinh lại gần:",
        "options": [
          "Các kẹp ghim bằng thép hoặc kim la bàn",
          "Một mẩu gỗ khô",
          "Một mẩu nhựa xốp",
          "Một cốc nước tinh khiết"
        ],
        "correct": 0,
        "explanation": "Nam châm hút các vật liệu từ như kẹp ghim thép hoặc làm lệch kim la bàn."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Dây dẫn dùng để quấn nam châm điện bắt buộc phải có đặc điểm gì quan trọng?",
        "options": [
          "Có lớp vỏ bọc cách điện bên ngoài",
          "Là dây đồng trần không bọc men",
          "Làm hoàn toàn bằng chất dẻo",
          "Phải là dây xích sắt"
        ],
        "correct": 0,
        "explanation": "Dây dẫn phải bọc men cách điện để dòng điện chạy xoắn ốc qua các vòng dây mà không bị chập ngắn mạch."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Vì sao người ta thường dùng sắt non mà không dùng thép để làm lõi của nam châm điện?",
        "options": [
          "Vì sắt non mất từ tính rất nhanh khi ngắt điện, còn thép giữ từ tính lâu biến thành nam châm vĩnh cửu",
          "Vì sắt non rẻ hơn thép",
          "Vì sắt non có màu sáng hơn thép",
          "Vì thép không dẫn điện"
        ],
        "correct": 0,
        "explanation": "Sắt non có tính khử từ nhanh, giúp việc đóng ngắt lực từ của nam châm điện diễn ra tức thì."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Biện pháp nào sau đây giúp làm tăng lực từ của một nam châm điện?",
        "options": [
          "Tăng số vòng dây quấn và tăng cường độ dòng điện",
          "Giảm số vòng dây quấn",
          "Rút bỏ lõi sắt non ra khỏi cuộn dây",
          "Giảm hiệu điện thế của nguồn điện"
        ],
        "correct": 0,
        "explanation": "Lực từ của nam châm điện tỉ lệ thuận với số vòng dây và cường độ dòng điện qua cuộn dây."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Khi đổi chiều dòng điện chạy qua các vòng dây của nam châm điện thì điều gì sẽ xảy ra?",
        "options": [
          "Vị trí các cực từ của nam châm điện bị đảo ngược",
          "Nam châm điện mất hết từ tính",
          "Lực từ tăng gấp đôi",
          "Cuộn dây bốc cháy ngay lập tức"
        ],
        "correct": 0,
        "explanation": "Đổi chiều dòng điện làm đảo chiều đường sức từ, dẫn đến các cực từ bị đảo ngược."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Ưu điểm nổi bật nhất của cần cẩu dùng nam châm điện so với cần cẩu dùng móc sắt cơ học là gì?",
        "options": [
          "Dễ dàng hút và thả phế liệu sắt thép bằng thao tác đóng/ngắt công tắc điện nhanh chóng",
          "Không tiêu thụ điện năng",
          "Hút được cả đất đá và bê tông",
          "Cần cẩu không bao giờ bị hỏng"
        ],
        "correct": 0,
        "explanation": "Cần cẩu nam châm điện chỉ cần đóng điện để hút và ngắt điện để thả hàng vạn mẩu sắt vụn cùng lúc."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Nếu thay lõi sắt non của nam châm điện bằng một thanh gỗ hoặc thanh nhôm có cùng kích thước thì:",
        "options": [
          "Từ trường của cuộn dây sẽ rất yếu, chỉ bằng từ trường của cuộn dây không lõi",
          "Từ trường tăng mạnh hơn lõi sắt",
          "Cuộn dây bị nổ",
          "Nam châm điện biến thành nam châm vĩnh cửu"
        ],
        "correct": 0,
        "explanation": "Gỗ và nhôm không phải là vật liệu từ nên không có tác dụng tăng cường từ trường."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một học sinh quấn 40 vòng dây quanh đinh sắt, nối với pin 1,5V hút được 4 đinh ghim nhỏ. Để hút được nhiều đinh ghim hơn với cùng đinh sắt đó, học sinh nên:",
        "options": [
          "Quấn thêm nhiều vòng dây hơn và mắc nối tiếp thêm pin để tăng dòng điện",
          "Tháo bớt 20 vòng dây ra",
          "Thay pin 1,5V bằng pin 0,5V yếu hơn",
          "Rút đinh sắt ra ngoài"
        ],
        "correct": 0,
        "explanation": "Tăng số vòng dây và tăng cường độ dòng điện làm tăng lực hút của nam châm điện."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về cấu tạo và nguyên lý hoạt động của nam châm điện:",
        "statements": [
          {
            "subId": "a",
            "text": "Nam châm điện chỉ thể hiện tính chất từ khi có dòng điện chạy qua cuộn dây.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Lõi sắt non có tác dụng tập trung và khuếch đại đường sức từ của cuộn dây lên hàng trăm lần.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dây dẫn quấn trên nam châm điện có thể dùng dây đồng trần không bọc cách điện mà vẫn hoạt động bình thường.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khi ngắt dòng điện chạy qua ống dây có lõi sắt non, tác dụng từ bị mất đi gần như hoàn toàn.",
            "correct": true
          }
        ],
        "explanation": "Nếu dùng dây trần không cách điện thì các vòng dây chạm nhau làm chập mạch đoản mạch."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các yếu tố làm thay đổi độ mạnh của lực từ nam châm điện:",
        "statements": [
          {
            "subId": "a",
            "text": "Tăng cường độ dòng điện chạy qua cuộn dây làm tăng lực hút của nam châm điện.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tăng số vòng dây quấn trên cùng một chiều dài lõi làm tăng lực từ của nam châm điện.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Rút lõi sắt non ra khỏi cuộn dây làm lực từ của ống dây tăng vọt lên.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Sử dụng lõi sắt non có tiết diện phù hợp giúp tăng hiệu quả hút giữ vật từ.",
            "correct": true
          }
        ],
        "explanation": "Rút lõi sắt non ra làm từ trường giảm đi rất nhiều lần."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Thực hành chế tạo nam châm điện đơn giản trong phòng học KHTN:",
        "statements": [
          {
            "subId": "a",
            "text": "Quấn dây đồng tráng men men đều tay theo một chiều quanh thân một chiếc bu-lông sắt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cần cạo sạch lớp men cách điện ở hai đầu dây nối trước khi kẹp vào hai cực của pin.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu nối trực tiếp hai đầu dây vào nguồn điện sinh hoạt 220V xoay chiều sẽ rất an toàn và hút cực mạnh.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Dùng la bàn kiểm tra thấy cực của nam châm điện đẩy cực Bắc của kim la bàn chứng tỏ đầu đó là cực Bắc.",
            "correct": true
          }
        ],
        "explanation": "Tuyệt đối không cắm vào nguồn điện 220V vì gây đoản mạch chập cháy nguy hiểm chết người!"
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng của nam châm điện trong các thiết bị công nghệ hiện đại:",
        "statements": [
          {
            "subId": "a",
            "text": "Rơ le điện từ dùng nam châm điện để đóng ngắt mạch điện tự động từ xa hoặc bảo vệ an toàn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chuông điện gia đình hoạt động nhờ cơ chế đóng ngắt mạch liên tục bằng nam châm điện và lá thép đàn hồi.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tàu đệm từ Maglev tận dụng lực từ cực mạnh của hệ thống nam châm điện để nâng đoàn tàu bay lơ lửng trên đường ray.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Kim chỉ nam của chiếc la bàn bỏ túi truyền thống bắt buộc phải là một nam châm điện nối với pin siêu nhỏ.",
            "correct": false
          }
        ],
        "explanation": "La bàn truyền thống dùng kim nam châm vĩnh cửu, không cần dùng pin hay nam châm điện."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một cuộn dây nam châm điện quấn 60 vòng hút được 12 chiếc kẹp ghim bằng thép. Nếu giữ nguyên dòng điện và tăng số vòng dây lên thành 120 vòng thì nam châm điện này hút được bao nhiêu chiếc kẹp ghim?",
        "correctAnswer": "24",
        "explanation": "Số vòng tăng gấp đôi (120/60 = 2) nên lực từ xấp xỉ tăng gấp 2 lần, hút được 12 x 2 = 24 chiếc kẹp ghim."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khi nối nam châm điện với một nguồn pin có cường độ dòng điện 0,5 A thì nó hút được vật nặng tối đa 80 g. Khi tăng cường độ dòng điện lên 1,0 A thì khối lượng vật tối đa nam châm điện hút được xấp xỉ là bao nhiêu gam?",
        "correctAnswer": "160",
        "explanation": "Dòng điện tăng gấp đôi (1,0 / 0,5 = 2) nên khối lượng hút tăng tương ứng: 80 x 2 = 160 g."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Có bao nhiêu yếu tố trong các yếu tố sau đây ảnh hưởng đến độ mạnh của từ trường nam châm điện: (1) Cường độ dòng điện; (2) Số vòng quấn của ống dây; (3) Có lõi sắt non hay không; (4) Màu sắc lớp sơn cách điện của dây dẫn?",
        "correctAnswer": "3",
        "explanation": "Có 3 yếu tố ảnh hưởng là (1), (2), (3). Yếu tố (4) màu sắc lớp sơn không ảnh hưởng."
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Một thợ điện cần quấn một cuộn nam châm điện có tổng cộng 200 vòng dây. Hiện người thợ đã quấn được 145 vòng. Hỏi người đó còn phải quấn thêm bao nhiêu vòng dây nữa để hoàn thành?",
        "correctAnswer": "55",
        "explanation": "Số vòng cần quấn thêm = 200 - 145 = 55 vòng."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cần cẩu nam châm điện tại cảng dỡ hàng nâng được một khối thép công nghiệp nặng 2,5 tấn. Khối lượng thép này tương đương với bao nhiêu kilôgam (kg)?",
        "correctAnswer": "2500",
        "explanation": "2,5 tấn = 2,5 x 1000 = 2500 kg."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Trong một thí nghiệm, khi bật công tắc điện, nam châm điện hút dính 15 chiếc kẹp giấy. Sau khi ngắt công tắc điện, do đinh sắt có một chút từ dư nên vẫn còn dính lại 1 chiếc kẹp giấy. Hỏi có bao nhiêu chiếc kẹp giấy đã bị rơi ra ngay khi ngắt điện?",
        "correctAnswer": "14",
        "explanation": "Số kẹp giấy rơi ra = 15 - 1 = 14 kẹp."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một nhóm học sinh làm thí nghiệm khảo sát số đinh ghim hút được bởi nam châm điện với các thông số khác nhau: Thí nghiệm 1 (50 vòng, I = 0,4 A) hút 8 ghim; Thí nghiệm 2 (50 vòng, I = 0,8 A) hút 16 ghim; Thí nghiệm 3 (100 vòng, I = 0,4 A) hút 16 ghim; Thí nghiệm 4 (100 vòng, I = 0,8 A). Dựa vào quy luật trên, dự đoán số đinh ghim hút được ở Thí nghiệm 4 là bao nhiêu?",
        "options": [
          "32 đinh ghim",
          "20 đinh ghim",
          "24 đinh ghim",
          "48 đinh ghim"
        ],
        "correct": 0,
        "explanation": "So với Thí nghiệm 1, Thí nghiệm 4 có số vòng tăng gấp 2 và cường độ tăng gấp 2 nên lực từ tăng xấp xỉ 4 lần: 8 x 4 = 32 đinh ghim."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trong rơ le điện từ dùng để đóng ngắt mạch điện bảo vệ máy bơm công suất lớn: Khi dòng điện chạy qua nam châm điện đạt giá trị định mức 5 A, lực hút của nam châm thắng lực kéo của lò xo đàn hồi (đang giữ lực kéo 12 N), hút thanh sắt đóng tiếp điểm phụ. Nếu muốn rơ le chỉ ngắt khi dòng điện chạm ngưỡng 7,5 A thì người kỹ thuật viên cần điều chỉnh lực kéo của lò xo lên mức nào (giả sử lực từ tỉ lệ thuận với dòng điện)?",
        "options": [
          "18 N",
          "15 N",
          "24 N",
          "9 N"
        ],
        "correct": 0,
        "explanation": "Dòng điện tăng 7,5 / 5 = 1,5 lần nên lực từ đạt 12 x 1,5 = 18 N, lò xo phải tăng lực căng lên 18 N."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tại một bãi phế liệu, một cần cẩu điện sử dụng nam châm điện hình chữ U để dọn sắt vụn. Khi dùng nguồn điện 24 V, nam châm hút được mảng thép 360 kg. Do yêu cầu vận chuyển mảng thép lớn 540 kg, người ta phải tăng hiệu điện thế nguồn điện lên bao nhiêu vôn (V) để lực từ tăng tương ứng (coi điện trở cuộn dây không đổi, lực từ tỉ lệ thuận với hiệu điện thế)?",
        "options": [
          "36 V",
          "30 V",
          "48 V",
          "28 V"
        ],
        "correct": 0,
        "explanation": "Tỉ lệ khối lượng = 540 / 360 = 1,5 lần. Hiệu điện thế cần tăng lên = 24 x 1,5 = 36 V."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một chuông điện tự ngắt hoạt động với tần số búa gõ là 25 lần trong mỗi giây (25 Hz). Hỏi trong thời gian 4 giây bấm giữ công tắc liên tục, búa của chuông điện đã thực hiện bao nhiêu lần gõ vào bát chuông kim loại?",
        "options": [
          "100 lần",
          "50 lần",
          "75 lần",
          "25 lần"
        ],
        "correct": 0,
        "explanation": "Số lần gõ chuông = 25 lần/giây x 4 giây = 100 lần."
      }
    ]
  },
  "phys7_c6_b20_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 20: Chế tạo nam châm điện đơn giản - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b20",
    "lessonName": "Bài 20: Chế tạo nam châm điện đơn giản",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khi có dòng điện chạy qua cuộn dây dẫn quấn quanh một chiếc đinh sắt, đinh sắt đó trở thành:",
        "options": [
          "Một nam châm điện",
          "Một nam châm vĩnh cửu",
          "Một bóng đèn phát sáng",
          "Một chất cách điện"
        ],
        "correct": 0,
        "explanation": "Dòng điện chạy qua cuộn dây sinh ra từ trường làm đinh sắt trở thành nam châm điện."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Từ trường của nam châm điện chỉ tồn tại trong điều kiện nào?",
        "options": [
          "Chỉ tồn tại trong thời gian có dòng điện chạy qua cuộn dây",
          "Luôn tồn tại vĩnh viễn kể cả khi tháo pin",
          "Chỉ tồn tại khi thời tiết có sấm sét",
          "Chỉ tồn tại trong bóng tối"
        ],
        "correct": 0,
        "explanation": "Từ trường của nam châm điện sinh ra do dòng điện nên chỉ tồn tại khi có dòng điện."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Muốn làm mất tác dụng từ của nam châm điện một cách tức thì, người ta thực hiện thao tác nào?",
        "options": [
          "Ngắt công tắc điện để cắt đứt dòng điện",
          "Đảo chiều pin",
          "Tăng thêm số vòng dây",
          "Nhúng nam châm vào nước lạnh"
        ],
        "correct": 0,
        "explanation": "Ngắt dòng điện thì từ tính của nam châm điện mất ngay tức thì."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Vật liệu nào sau đây là lựa chọn thích hợp nhất để chế tạo lõi của nam châm điện?",
        "options": [
          "Sắt non",
          "Đồng thau",
          "Nhựa cứng",
          "Gỗ ép"
        ],
        "correct": 0,
        "explanation": "Sắt non nhiễm từ rất mạnh và mất từ tính nhanh khi ngắt điện."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Thí nghiệm lịch sử năm 1820 của nhà bác học Oersted đã phát hiện ra mối liên hệ trực tiếp giữa:",
        "options": [
          "Dòng điện và từ trường",
          "Nhiệt độ và ánh sáng",
          "Âm thanh và lực đẩy",
          "Trọng lực và áp suất"
        ],
        "correct": 0,
        "explanation": "Oersted phát hiện dòng điện trong dây dẫn làm quay kim nam châm (tác dụng từ)."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Một nam châm điện đang hút các đinh ghim ở đầu A. Nếu ta đảo cực của nguồn điện thì đầu A sẽ:",
        "options": [
          "Đổi tên cực từ nhưng vẫn tiếp tục hút các đinh ghim",
          "Đẩy các đinh ghim ra xa",
          "Mất hoàn toàn lực hút",
          "Nóng chảy ngay lập tức"
        ],
        "correct": 0,
        "explanation": "Nam châm luôn hút sắt thép ở cả hai cực Bắc và Nam, đảo chiều dòng điện chỉ đảo tên cực từ."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Thiết bị nào sau đây KHÔNG sử dụng nam châm điện trong nguyên lý hoạt động?",
        "options": [
          "La bàn bỏ túi truyền thống",
          "Rơ le điện từ",
          "Cần cẩu dọn phế liệu kim loại",
          "Chuông điện gia đình"
        ],
        "correct": 0,
        "explanation": "La bàn truyền thống dùng kim nam châm vĩnh cửu đặt trên trục quay tự do."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khi giữ nguyên cường độ dòng điện nhưng tăng số vòng dây quấn trên cùng một ống dây thì lực từ của nam châm điện sẽ:",
        "options": [
          "Tăng lên",
          "Giảm đi",
          "Không đổi",
          "Biến mất"
        ],
        "correct": 0,
        "explanation": "Lực từ của nam châm điện tăng khi số vòng dây quấn tăng."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Nếu quấn dây đồng trần (không có màng sơn men cách điện) sát khít quanh đinh sắt thì hiện tượng gì sẽ xảy ra?",
        "options": [
          "Dòng điện bị ngắn mạch chạy tắt qua các vòng dây và đinh sắt, nam châm không hoạt động",
          "Nam châm hút mạnh gấp đôi",
          "Đinh sắt biến thành thanh nam châm vĩnh cửu",
          "Điện trở mạch tăng lên vô cùng lớn"
        ],
        "correct": 0,
        "explanation": "Dây trần làm các vòng dây chạm chập nhau, dòng điện không chạy xoắn ốc theo cuộn dây nên không sinh từ trường xoắn."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Để điều khiển độ mạnh yếu của lực từ một nam châm điện trong phòng thí nghiệm, người ta thường mắc nối tiếp cuộn dây với:",
        "options": [
          "Một biến trở",
          "Một chiếc ampe kế đo dòng",
          "Một nhiệt kế thủy ngân",
          "Một vôn kế"
        ],
        "correct": 0,
        "explanation": "Biến trở dùng để thay đổi điện trở mạch, từ đó thay đổi cường độ dòng điện qua nam châm điện."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tàu đệm từ (Maglev) có thể di chuyển với vận tốc cực lớn mà êm ái, không ma sát đường ray là nhờ ứng dụng:",
        "options": [
          "Lực đẩy và lực nâng của hệ thống nam châm điện cực mạnh",
          "Động cơ phản lực gắn dưới gầm ray",
          "Đệm không khí nén áp suất cao",
          "Bánh xe thép lăn siêu trơn"
        ],
        "correct": 0,
        "explanation": "Tàu Maglev ứng dụng lực từ của nam châm điện để nâng toa tàu lơ lửng trên đường ray."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một học sinh chế tạo hai nam châm điện: Cuộn 1 có 50 vòng dây quấn trên bu-lông sắt non; Cuộn 2 có 50 vòng dây quấn trên đũa tre cùng kích thước. Cho cùng dòng điện 0,5 A chạy qua cả hai cuộn. Kết quả thu được là:",
        "options": [
          "Cuộn 1 hút đinh ghim rất mạnh, cuộn 2 hầu như không hút được đinh ghim",
          "Cuộn 2 hút mạnh hơn cuộn 1",
          "Hai cuộn hút đinh ghim như nhau",
          "Cả hai cuộn đều không có từ tính"
        ],
        "correct": 0,
        "explanation": "Đũa tre không phải là vật liệu từ nên từ trường rất yếu, bu-lông sắt non tăng cường từ trường lên nhiều lần."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về sự khác biệt giữa lõi sắt non và lõi thép khi đặt trong cuộn dây có dòng điện:",
        "statements": [
          {
            "subId": "a",
            "text": "Cả sắt non và thép đều bị nhiễm từ mạnh khi đặt trong từ trường của cuộn dây.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi ngắt dòng điện, lõi sắt non mất hầu hết từ tính, còn thép giữ được từ tính lâu dài.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Để chế tạo nam châm vĩnh cửu nhân tạo, người ta đặt thanh thép vào lòng ống dây có dòng điện.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dùng lõi thép làm cần cẩu bốc dỡ phế liệu sẽ giúp việc thả phế liệu diễn ra dễ dàng hơn lõi sắt non.",
            "correct": false
          }
        ],
        "explanation": "Nếu dùng lõi thép thì khi ngắt điện thép vẫn giữ từ tính, sắt vụn dính chặt không chịu rơi xuống."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về khả năng điều khiển linh hoạt của nam châm điện so với nam châm vĩnh cửu:",
        "statements": [
          {
            "subId": "a",
            "text": "Có thể đóng ngắt từ tính của nam châm điện nhanh chóng bằng công tắc.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Có thể tăng giảm lực từ của nam châm điện bằng cách thay đổi cường độ dòng điện.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Có thể đảo cực từ của nam châm điện bằng cách đảo cực của nguồn điện.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nam châm điện không thể hút được vật liệu coban hay niken.",
            "correct": false
          }
        ],
        "explanation": "Nam châm điện hút được tất cả các vật liệu từ tính như sắt, thép, niken, coban."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Thực hành chế tạo nam châm điện bằng đinh sắt, dây đồng bọc men và pin tròn 1,5V:",
        "statements": [
          {
            "subId": "a",
            "text": "Dây quấn càng sít nhau và quấn thành nhiều lớp thì từ trường tạo ra càng mạnh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đoạn dây dẫn ở hai đầu cuộn dây dùng để nối vào pin phải được cạo sạch lớp men cách điện.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu lắp thêm một viên pin 1,5V nối tiếp thì lực hút của nam châm điện sẽ giảm sút.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Sau khi ngắt pin, nam châm điện với đinh sắt non vẫn hút chặt thanh nhôm không rời.",
            "correct": false
          }
        ],
        "explanation": "Thanh nhôm không có từ tính nên không bao giờ bị nam châm hút."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Ứng dụng công nghiệp và an toàn của nam châm điện:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong các nhà máy lọc đường hoặc xay xát ngũ cốc, nam châm điện được dùng để hút lọc các mẩu sắt vụn lẫn vào nguyên liệu.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong thiết bị ghi âm từ tính hoặc đĩa cứng, đầu đọc/ghi sử dụng các nam châm điện siêu nhỏ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cần cẩu nam châm điện có thể dùng để vận chuyển các khối vàng thỏi nguyên chất một cách dễ dàng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khóa cửa từ điện tử tại các tòa nhà cao ốc sử dụng nam châm điện để giữ chốt cửa luôn khóa khi có điện.",
            "correct": true
          }
        ],
        "explanation": "Vàng là kim loại không có từ tính nên nam châm không hút được vàng thỏi."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một nam châm điện có cuộn dây 80 vòng nối với pin 3 V hút được 18 chiếc đinh ghim nhỏ. Người ta quấn thêm 40 vòng dây nữa (tổng 120 vòng) và giữ nguyên nguồn điện, hỏi số đinh ghim hút được ước tính là bao nhiêu chiếc?",
        "correctAnswer": "27",
        "explanation": "Tỉ lệ số vòng = 120 / 80 = 1,5 lần. Số đinh ghim hút được = 18 x 1,5 = 27 chiếc."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Trong mạch điều khiển nam châm điện, ban đầu cường độ dòng điện là 0,3 A. Sau khi điều chỉnh biến trở thì dòng điện tăng lên thành 0,6 A. Hỏi cường độ dòng điện qua nam châm điện đã tăng thêm bao nhiêu ampe (A)?",
        "correctAnswer": "0,3",
        "explanation": "Cường độ tăng thêm = 0,6 - 0,3 = 0,3 A."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một cần cẩu nam châm điện lần thứ nhất nâng được 450 kg sắt vụn, lần thứ hai nâng được 350 kg sắt vụn. Tổng khối lượng sắt vụn mà cần cẩu đã nâng qua hai lần là bao nhiêu kilôgam (kg)?",
        "correctAnswer": "800",
        "explanation": "Tổng khối lượng = 450 + 350 = 800 kg."
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Một nhóm học sinh quấn 4 cuộn nam châm điện A, B, C, D có số vòng dây lần lượt là: Mẫu A (30 vòng), Mẫu B (60 vòng), Mẫu C (90 vòng), Mẫu D (120 vòng). Khi cùng cho dòng điện 0,5 A chạy qua, cuộn dây nào có lực từ mạnh nhất?",
        "correctAnswer": "D",
        "explanation": "Số vòng dây càng nhiều thì lực từ càng mạnh, do đó mẫu D (120 vòng) có lực từ mạnh nhất."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Một cuộn dây quấn nam châm điện có tổng chiều dài sợi dây đồng bọc men là 4 mét (m). Biết chu vi mỗi vòng quấn quanh lõi đinh sắt là 4 cm. Hỏi cuộn dây này có tổng cộng bao nhiêu vòng quấn?",
        "correctAnswer": "100",
        "explanation": "Đổi 4 m = 400 cm. Số vòng quấn = 400 / 4 = 100 vòng."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khi đóng mạch điện, một nam châm điện công nghiệp hút giữ được 32 thỏi gang. Khi người vận hành ngắt điện hoàn toàn, biết lõi nam châm làm bằng sắt non khử từ tốt, hỏi có bao nhiêu thỏi gang còn bị dính lại trên bề mặt nam châm?",
        "correctAnswer": "0",
        "explanation": "Lõi sắt non mất từ tính hoàn toàn khi ngắt điện nên toàn bộ 32 thỏi gang rơi xuống, còn dính lại 0 thỏi."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một chuông điện tự ngắt sử dụng nguồn điện một chiều 6 V. Khi đóng mạch, cứ mỗi giây miếng sắt của búa gõ đóng mở mạch 20 chu kì, tạo ra 20 tiếng chuông gõ vào bát kim loại. Hỏi nếu học sinh nhấn giữ nút chuông trong đúng 15 giây thì chuông điện đã phát ra tổng cộng bao nhiêu tiếng gõ?",
        "options": [
          "300 tiếng gõ",
          "150 tiếng gõ",
          "120 tiếng gõ",
          "200 tiếng gõ"
        ],
        "correct": 0,
        "explanation": "Tổng số tiếng gõ = 20 lần/giây x 15 giây = 300 tiếng gõ."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Để khảo sát ảnh hưởng của số vòng dây đến lực hút của nam châm điện, một nhóm học sinh đo khối lượng sắt tối đa mà nam châm hút được: Với N1 = 50 vòng hút được 120 g; với N2 = 100 vòng hút được 240 g; với N3 = 150 vòng hút được 360 g. Hỏi nếu quấn tới N4 = 250 vòng dây với cùng cường độ dòng điện đó thì nam châm hút được khối lượng sắt xấp xỉ bao nhiêu gam?",
        "options": [
          "600 g",
          "500 g",
          "480 g",
          "720 g"
        ],
        "correct": 0,
        "explanation": "Khối lượng hút tỉ lệ thuận với số vòng dây: m = 2,4 x N. Với N = 250 thì m = 2,4 x 250 = 600 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một rơ le nhiệt - từ bảo vệ quá tải cho hệ thống điện trong tòa nhà: Dòng điện định mức cho phép là 16 A. Khi xảy ra sự cố chập mạch, dòng điện vọt lên 48 A làm lực từ của nam châm điện tăng vọt, hút chốt ngắt mạch chỉ trong 0,02 giây. Cường độ dòng điện khi xảy ra sự cố đã tăng gấp bao nhiêu lần so với dòng điện định mức ban đầu?",
        "options": [
          "3 lần",
          "2 lần",
          "4 lần",
          "6 lần"
        ],
        "correct": 0,
        "explanation": "Tỉ số dòng điện = 48 / 16 = 3 lần."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một đoàn tàu đệm từ Maglev có tổng khối lượng 240 tấn được nâng lơ lửng nhờ hệ thống gồm 120 khối nam châm điện siêu dẫn bố trí đều dọc thân tàu. Để nâng được đoàn tàu bay lên, trung bình mỗi khối nam châm điện phải tạo ra một lực từ nâng tối thiểu có độ lớn bao nhiêu niutơn (N), lấy g = 10 m/s2?",
        "options": [
          "20 000 N",
          "10 000 N",
          "12 000 N",
          "24 000 N"
        ],
        "correct": 0,
        "explanation": "Trọng lượng toàn đoàn tàu P = 240 000 kg x 10 = 2 400 000 N. Mỗi khối nam châm chịu lực nâng = 2 400 000 / 120 = 20 000 N."
      }
    ]
  },
  "phys7_c6_b20_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - Bài 20: Chế tạo nam châm điện đơn giản - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_b20",
    "lessonName": "Bài 20: Chế tạo nam châm điện đơn giản",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Bộ phận trực tiếp sinh ra từ trường trong một nam châm điện là:",
        "options": [
          "Cuộn dây dẫn khi có dòng điện chạy qua",
          "Lớp vỏ cách điện bên ngoài",
          "Công tắc bật mở",
          "Đế đỡ bằng gỗ"
        ],
        "correct": 0,
        "explanation": "Dòng điện chạy qua cuộn dây dẫn trực tiếp sinh ra từ trường."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đặc tính nào sau đây là ưu điểm vượt trội của nam châm điện so với nam châm vĩnh cửu?",
        "options": [
          "Có thể dễ dàng điều khiển độ mạnh yếu và bật tắt từ tính",
          "Không bao giờ bị nóng lên khi sử dụng",
          "Luôn giữ nguyên lực hút không đổi",
          "Không cần cung cấp năng lượng điện"
        ],
        "correct": 0,
        "explanation": "Nam châm điện điều khiển được từ trường thông qua việc điều chỉnh dòng điện."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Từ trường của ống dây có lõi sắt non tập trung mạnh nhất tại vị trí nào?",
        "options": [
          "Ở hai đầu của lõi sắt non",
          "Ở chính giữa thân ống dây",
          "Ở nguồn điện",
          "Ở dây dẫn nối ngoài"
        ],
        "correct": 0,
        "explanation": "Các cực từ nằm ở hai đầu lõi sắt non là nơi từ trường tập trung dày đặc nhất."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi tăng đồng thời cả cường độ dòng điện chạy qua cuộn dây và số vòng dây quấn thì lực từ của nam châm điện sẽ:",
        "options": [
          "Tăng lên rất mạnh",
          "Giảm đi rõ rệt",
          "Không thay đổi",
          "Biến mất hoàn toàn"
        ],
        "correct": 0,
        "explanation": "Cả hai yếu tố đều làm tăng lực từ nên khi tăng đồng thời lực từ tăng mạnh."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tại sao người ta không dùng lõi bằng nhựa hoặc cao su trong nam châm điện?",
        "options": [
          "Vì nhựa và cao su không có từ tính, không thể tăng cường từ trường của cuộn dây",
          "Vì nhựa quá nặng",
          "Vì nhựa dẫn điện quá tốt",
          "Vì nhựa quá đắt tiền"
        ],
        "correct": 0,
        "explanation": "Nhựa và cao su không nhiễm từ nên không khuếch đại được từ trường."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Dụng cụ dùng để thay đổi cường độ dòng điện qua cuộn dây nhằm tăng giảm lực hút nam châm điện trong thí nghiệm là:",
        "options": [
          "Biến trở",
          "Thước cuộn",
          "Nhiệt kế",
          "Lực kế"
        ],
        "correct": 0,
        "explanation": "Biến trở có thể thay đổi điện trở, từ đó điều chỉnh cường độ dòng điện I."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Khi đóng khóa K của mạch điện chứa nam châm điện, kim nam châm nhỏ đặt thăng bằng ở gần đó sẽ:",
        "options": [
          "Bị lệch góc quay khỏi vị trí cân bằng ban đầu",
          "Đứng yên không hề dịch chuyển",
          "Bốc cháy",
          "Rơi xuống đất"
        ],
        "correct": 0,
        "explanation": "Từ trường của nam châm điện tác dụng lực từ làm kim nam châm xoay lệch."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Thiết bị hoạt động dựa trên nguyên tắc: nam châm điện hút miếng sắt kéo búa đập vào chuông, đồng thời ngắt mạch điện nhả miếng sắt về vị trí ban đầu là:",
        "options": [
          "Chuông điện tự ngắt",
          "Bếp hồng ngoại",
          "Bình thủy điện",
          "Đồng hồ quả lắc cơ học"
        ],
        "correct": 0,
        "explanation": "Đó chính là nguyên lý tự ngắt liên tục của chuông điện."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Nếu dùng lõi thép thay cho lõi sắt non thì sau khi ngắt dòng điện chạy qua ống dây, lõi thép sẽ:",
        "options": [
          "Vẫn giữ được từ tính lâu dài và trở thành nam châm vĩnh cửu",
          "Mất hết từ tính ngay lập tức",
          "Chảy lỏng ra",
          "Bị vỡ thành nhiều mảnh"
        ],
        "correct": 0,
        "explanation": "Thép có tính khử từ chậm, giữ từ tính lâu dài tạo thành nam châm vĩnh cửu."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Để đảo chiều các cực từ của nam châm điện, thao tác đúng nhất là:",
        "options": [
          "Đổi chiều dòng điện bằng cách hoán đổi hai cực của nguồn điện nối vào cuộn dây",
          "Xoay ngược chiều đinh sắt trong cuộn dây",
          "Sơn màu ngược lại cho hai đầu đinh",
          "Tăng thêm số vòng dây"
        ],
        "correct": 0,
        "explanation": "Đảo chiều dòng điện làm đảo chiều các đường sức từ và cực từ."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Người ta chế tạo nam châm điện dạng hình chữ U quấn hai cuộn dây nhằm mục đích gì?",
        "options": [
          "Đưa cả hai cực Bắc và Nam về cùng một phía để tăng lực hút tiếp xúc lên vật bằng sắt",
          "Để tiết kiệm dây điện",
          "Để dễ cầm tay hơn",
          "Để giảm khối lượng nam châm"
        ],
        "correct": 0,
        "explanation": "Hai cực từ cùng nằm một phía cho phép cả hai cực cùng hút vật, tăng lực giữ gấp đôi."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Đồ vật hoặc thiết bị nào sau đây KHÔNG sử dụng nguyên lý hoạt động của nam châm điện?",
        "options": [
          "Chiếc bút bi bấm học sinh",
          "Máy chụp cộng hưởng từ MRI trong bệnh viện",
          "Loa phóng thanh điện động",
          "Rơ le bảo vệ máy biến áp"
        ],
        "correct": 0,
        "explanation": "Bút bi hoạt động hoàn toàn bằng cơ học lò xo, không dùng nam châm điện."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về quy trình các bước thực hành chế tạo nam châm điện đơn giản:",
        "statements": [
          {
            "subId": "a",
            "text": "Chọn một chiếc đinh sắt hoặc bu-lông sắt dài khoảng 5 - 10 cm làm lõi.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Quấn dây đồng tráng men cách điện đều đặn nhiều vòng xung quanh đinh sắt.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Để nguyên lớp men sơn ở hai đầu dây khi cắm vào cực pin để dòng điện chạy êm hơn.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Dùng các kẹp giấy kim loại để kiểm tra độ mạnh yếu của lực từ nam châm vừa tạo ra.",
            "correct": true
          }
        ],
        "explanation": "Bắt buộc phải cạo sạch lớp men cách điện ở hai đầu dây thì dòng điện mới truyền qua được."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các đặc tính từ trường của nam châm điện có lõi sắt non:",
        "statements": [
          {
            "subId": "a",
            "text": "Từ trường xung quanh nam châm điện có dạng tương tự như từ trường của một thanh nam châm thẳng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đầu cuộn dây mà các đường sức từ đi ra là cực Bắc, đầu đi vào là cực Nam.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi dòng điện qua cuộn dây càng lớn thì từ trường sinh ra càng mạnh.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu ngắt dòng điện thì từ trường của nam châm điện vẫn tồn tại vĩnh viễn không bao giờ mất.",
            "correct": false
          }
        ],
        "explanation": "Nam châm điện mất từ trường gần như hoàn toàn khi ngắt dòng điện."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Thí nghiệm khảo sát lực hút kẹp ghim của nam châm điện khi thay đổi nguồn điện:",
        "statements": [
          {
            "subId": "a",
            "text": "Dùng 1 viên pin 1,5V hút được 6 kẹp ghim; dùng 2 viên pin 1,5V mắc nối tiếp hút được khoảng 12 kẹp ghim.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi lắp 2 viên pin nối tiếp, hiệu điện thế tăng gấp đôi làm cường độ dòng điện tăng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu lắp 2 viên pin ngược cực nhau (+ đấu với +) thì lực hút của nam châm sẽ tăng mạnh nhất.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Đưa đầu nam châm điện lại gần mẩu dây đồng vụn thì nam châm không hút được mẩu đồng nào.",
            "correct": true
          }
        ],
        "explanation": "Mắc ngược cực hai viên pin giống nhau thì triệt tiêu hiệu điện thế (U = 0V), nam châm không hoạt động."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cơ chế bảo vệ của rơ-le điện từ và cầu dao tự động (Aptomat):",
        "statements": [
          {
            "subId": "a",
            "text": "Trong mạng điện gia đình, Aptomat chứa một nam châm điện nhỏ nối tiếp trong mạch chính.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi xảy ra hiện tượng đoản mạch ngắn mạch, dòng điện tăng đột biến làm nam châm điện hút mạnh lẫy bật ngắt công tắc.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sau khi sự cố được khắc phục, người dùng có thể gạt cần gạt đóng lại Aptomat để cấp điện trở lại.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Aptomat chỉ ngắt được điện khi có ai đó dùng tay kéo cần gạt, nam châm điện không có tác dụng tự ngắt.",
            "correct": false
          }
        ],
        "explanation": "Nam châm điện tự động hút lẫy ngắt mạch tức thì khi quá tải mà không cần thao tác thủ công."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một học sinh quấn 100 vòng dây quanh một chiếc đinh sắt non, khi nối với pin 1,5V thì nam châm hút được 16 chiếc đinh ghim nhỏ. Nếu quấn tăng lên thành 150 vòng dây với cùng viên pin đó, hỏi nam châm điện này hút được ước tính bao nhiêu chiếc đinh ghim?",
        "correctAnswer": "24",
        "explanation": "Tỉ lệ số vòng = 150 / 100 = 1,5 lần. Số đinh ghim hút được = 16 x 1,5 = 24 chiếc."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Để tăng lực hút của nam châm điện trong thí nghiệm, người ta điều chỉnh biến trở làm dòng điện tăng từ 0,4 A lên 1,2 A. Hỏi cường độ dòng điện chạy qua cuộn dây đã tăng lên gấp bao nhiêu lần?",
        "correctAnswer": "3",
        "explanation": "Số lần tăng = 1,2 / 0,4 = 3 lần."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một cần trục điện tại xưởng đúc thép có khả năng nâng một khối sắt nặng 1,8 tấn trong một lần hút. Khối lượng khối sắt này bằng bao nhiêu kilôgam (kg)?",
        "correctAnswer": "1800",
        "explanation": "1,8 tấn = 1,8 x 1000 = 1800 kg."
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Một cuộn dây nam châm điện gồm có 240 vòng dây được quấn đều đặn thành 4 lớp chồng lên nhau quanh một lõi thép non. Hỏi mỗi lớp có bao nhiêu vòng dây?",
        "correctAnswer": "60",
        "explanation": "Số vòng mỗi lớp = 240 / 4 = 60 vòng."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Trong một bài thực hành: Khi cường độ dòng điện là 0,2 A thì nam châm hút được 6 kẹp ghim; khi dòng điện là 0,4 A thì hút được 12 kẹp ghim. Hỏi khi dòng điện là 0,6 A thì nam châm hút được bao nhiêu chiếc kẹp ghim (giả sử số kẹp hút tỉ lệ thuận với dòng điện)?",
        "correctAnswer": "18",
        "explanation": "Dòng điện 0,6 A gấp 3 lần 0,2 A nên số kẹp ghim hút được = 6 x 3 = 18 kẹp."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Một học sinh chuẩn bị các dụng cụ: (1) Đinh sắt non; (2) Dây đồng bọc men cách điện; (3) Nguồn pin 1,5V; (4) Khóa K; (5) Thước kẻ nhựa; (6) Hộp kẹp ghim bằng thép để thử từ tính. Hỏi có bao nhiêu dụng cụ thực sự cần thiết để chế tạo và kiểm tra hoạt động của nam châm điện?",
        "correctAnswer": "5",
        "explanation": "Có 5 dụng cụ cần thiết là (1), (2), (3), (4), (6). Thước kẻ nhựa không cần thiết."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một nam châm điện hình chữ U có hai cuộn dây giống nhau quấn trên hai nhánh. Mỗi nhánh quấn 80 vòng dây. Dòng điện chạy qua cả hai cuộn là 0,5 A. Để tăng gấp đôi lực hút của nam châm điện này lên thanh sắt bắc ngang hai cực mà vẫn giữ nguyên cường độ dòng điện 0,5 A, người ta cần quấn thêm vào mỗi nhánh bao nhiêu vòng dây nữa?",
        "options": [
          "80 vòng",
          "40 vòng",
          "160 vòng",
          "120 vòng"
        ],
        "correct": 0,
        "explanation": "Lực từ tăng gấp đôi nên tổng số vòng mỗi nhánh phải tăng gấp đôi từ 80 thành 160 vòng, tức quấn thêm 80 vòng mỗi nhánh."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Thiết kế hệ thống báo động chống trộm: Một nam châm điện dùng dòng điện thường trực 0,2 A để hút giữ một tấm kim loại mở tiếp điểm chuông. Khi kẻ trộm giẫm lên dây bẫy làm đứt mạch điện của nam châm, lò xo ngay lập tức kéo tấm kim loại đóng tiếp điểm mạch phụ làm chuông 12 V reo vang với cường độ âm thanh 95 dB. Bộ phận đóng vai trò cảm ứng ngắt tự động trong hệ thống này là:",
        "options": [
          "Rơ le điện từ mở tiếp điểm thường đóng",
          "Biến trở xoay",
          "Cầu chì nhiệt",
          "Điện trở quang"
        ],
        "correct": 0,
        "explanation": "Đây là nguyên lý hoạt động của rơ-le điện từ với tiếp điểm thường đóng: mất điện cuộn hút thì tiếp điểm đóng lại."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một cuộn dây nam châm điện có điện trở R = 15 ôm (ohm). Khi nối cuộn dây vào nguồn điện không đổi có hiệu điện thế U1 = 6 V thì cường độ dòng điện qua mạch là I1 = 0,4 A và hút được 10 đinh thép. Muốn dòng điện tăng lên thành I2 = 0,8 A để hút được 20 đinh thép thì hiệu điện thế của nguồn điện phải điều chỉnh lên mức U2 bằng bao nhiêu?",
        "options": [
          "12 V",
          "18 V",
          "24 V",
          "9 V"
        ],
        "correct": 0,
        "explanation": "Dòng điện tăng gấp đôi (0,8 / 0,4 = 2) thì hiệu điện thế cũng phải tăng gấp đôi: U2 = 6 x 2 = 12 V (vì I = U/R)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Trong thiết bị ghi dữ liệu ổ đĩa cứng máy tính (HDD), đầu ghi là một nam châm điện siêu nhỏ có chiều rộng khe từ chỉ 50 nanômét (nm). Đầu ghi tạo ra các vùng từ hóa cực nhỏ trên đĩa từ quay với tốc độ 7200 vòng/phút. Đổi kích thước 50 nanômét ra đơn vị mét (m):",
        "options": [
          "5 x 10^-8 m",
          "5 x 10^-9 m",
          "5 x 10^-7 m",
          "5 x 10^-6 m"
        ],
        "correct": 0,
        "explanation": "1 nm = 10^-9 m. Do đó 50 nm = 50 x 10^-9 m = 5 x 10^-8 m."
      }
    ]
  },
  "phys7_c6_rev_test1": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương VI - Đề số 01",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương VI",
    "testNum": 1,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật nào sau đây có khả năng hút được các mẩu đinh sắt nhỏ?",
        "options": [
          "Thanh nam châm thẳng",
          "Chiếc đũa thủy tinh",
          "Thanh thước nhựa mica",
          "Miếng xốp bọt biển"
        ],
        "correct": 0,
        "explanation": "Nam châm có từ tính hút các vật liệu bằng sắt thép."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Kí hiệu chuẩn quốc tế của cực Bắc trên thanh nam châm là chữ cái nào?",
        "options": [
          "N (North)",
          "S (South)",
          "W (West)",
          "E (East)"
        ],
        "correct": 0,
        "explanation": "Cực Bắc kí hiệu là N (North), cực Nam kí hiệu là S (South)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Xung quanh một thanh nam châm luôn tồn tại dạng vật chất đặc biệt nào có thể tác dụng lực từ lên nam châm khác?",
        "options": [
          "Từ trường",
          "Điện trường tĩnh",
          "Sóng siêu âm",
          "Chân không hoàn toàn"
        ],
        "correct": 0,
        "explanation": "Xung quanh nam châm luôn tồn tại từ trường."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hình ảnh các đường mạt sắt sắp xếp trật tự xung quanh thanh nam châm trên tấm bìa được gọi là gì?",
        "options": [
          "Từ phổ",
          "Quang phổ",
          "Sóng âm",
          "Lưới tọa độ"
        ],
        "correct": 0,
        "explanation": "Hình ảnh mạt sắt sắp xếp quanh nam châm gọi là từ phổ."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Theo quy ước quốc tế, chiều của đường sức từ ở bên ngoài thanh nam châm là chiều nào?",
        "options": [
          "Đi ra từ cực Bắc và đi vào cực Nam",
          "Đi ra từ cực Nam và đi vào cực Bắc",
          "Đi từ chính giữa ra hai đầu",
          "Đi ngẫu nhiên không có quy luật"
        ],
        "correct": 0,
        "explanation": "Quy ước chiều đường sức từ bên ngoài nam châm: Ra Bắc vào Nam."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tại sao kim la bàn tự do khi thăng bằng luôn chỉ theo hướng Bắc - Nam địa lý?",
        "options": [
          "Vì Trái Đất là một nam châm khổng lồ có từ trường",
          "Vì có gió thổi theo hướng Bắc Nam",
          "Vì ánh sáng Mặt Trời chiếu vuông góc",
          "Vì sức hút của Mặt Trăng"
        ],
        "correct": 0,
        "explanation": "Từ trường của Trái Đất định hướng cho kim nam châm của la bàn."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Cực Bắc địa từ của Trái Đất nằm ở vùng lân cận vị trí nào trên Trái Đất?",
        "options": [
          "Gần cực Nam địa lí của Trái Đất",
          "Gần cực Bắc địa lí của Trái Đất",
          "Ngay tại đường xích đạo",
          "Ở tâm của Trái Đất"
        ],
        "correct": 0,
        "explanation": "Cực Bắc địa từ nằm ở gần cực Nam địa lí, cực Nam địa từ nằm ở gần cực Bắc địa lí."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Để chế tạo một nam châm điện đơn giản, ta cần quấn một cuộn dây dẫn bọc cách điện xung quanh vật nào?",
        "options": [
          "Một chiếc đinh sắt non",
          "Một thanh đồng đỏ",
          "Một ống hút nhựa",
          "Một thỏi than chì"
        ],
        "correct": 0,
        "explanation": "Lõi sắt non bị nhiễm từ mạnh, tăng cường độ từ trường của nam châm điện."
      },
      {
        "id": 9,
        "level": "Nhận biết",
        "question": "Yếu tố nào sau đây KHÔNG LÀM THAY ĐỔI độ mạnh của lực từ nam châm điện?",
        "options": [
          "Màu sắc lớp vỏ bọc cách điện của dây dẫn",
          "Cường độ dòng điện qua cuộn dây",
          "Số vòng quấn của ống dây",
          "Vật liệu làm lõi của ống dây"
        ],
        "correct": 0,
        "explanation": "Màu sắc vỏ cách điện không ảnh hưởng gì đến từ tính của nam châm."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khi đưa hai cực cùng tên của hai thanh nam châm lại gần nhau thì hiện tượng gì sẽ xảy ra?",
        "options": [
          "Hai thanh nam châm đẩy nhau ra xa",
          "Hai thanh nam châm hút chặt lấy nhau",
          "Hai thanh nam châm hoàn toàn không tương tác",
          "Hai thanh nam châm phát sáng"
        ],
        "correct": 0,
        "explanation": "Các cực cùng tên thì đẩy nhau, các cực khác tên thì hút nhau."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Phương tiện giao thông hiện đại nào sau đây ứng dụng lực từ cực mạnh của nam châm điện để di chuyển không ma sát đường ray?",
        "options": [
          "Tàu đệm từ Maglev",
          "Tàu hỏa chạy bằng hơi nước",
          "Xe buýt chạy bằng khí gas",
          "Xe đạp điện"
        ],
        "correct": 0,
        "explanation": "Tàu Maglev dùng nam châm điện để nâng và đẩy toa tàu bay lơ lửng trên ray."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Vật liệu nào sau đây KHÔNG PHẢI là vật liệu từ và hoàn toàn không bị nam châm hút?",
        "options": [
          "Thanh đồng đỏ nguyên chất",
          "Một chiếc đinh thép",
          "Một mẩu kim loại niken",
          "Một chiếc kẹp ghim bằng sắt"
        ],
        "correct": 0,
        "explanation": "Đồng đỏ không phải vật liệu từ nên không bị nam châm hút."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về tính chất của nam châm vĩnh cửu và sự tương tác từ:",
        "statements": [
          {
            "subId": "a",
            "text": "Mỗi thanh nam châm luôn luôn có hai cực từ: cực Bắc (N) và cực Nam (S).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi bẻ gãy một thanh nam châm làm đôi, mỗi nửa sẽ biến thành một nam châm mới có đủ hai cực.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hai cực khác tên của hai nam châm khi đặt gần nhau sẽ hút nhau.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nam châm vĩnh cửu có thể hút được tất cả các kim loại như vàng, bạc, đồng, nhôm.",
            "correct": false
          }
        ],
        "explanation": "Nam châm chỉ hút các kim loại có tính sắt từ như sắt, thép, coban, niken."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về từ phổ và các đường sức từ của một thanh nam châm thẳng:",
        "statements": [
          {
            "subId": "a",
            "text": "Từ phổ cho ta hình ảnh trực quan sinh động về sự phân bố của từ trường trong không gian.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nơi nào mạt sắt sắp xếp càng dày khít thì từ trường tại đó càng mạnh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ở khoảng giữa của thanh nam châm thẳng, từ trường mạnh hơn rất nhiều so với ở hai đầu cực.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Bên ngoài nam châm, đường sức từ là những đường cong khép kín đi ra từ cực Bắc và đi vào cực Nam.",
            "correct": true
          }
        ],
        "explanation": "Lực từ của thanh nam châm tập trung mạnh nhất ở hai đầu cực, ở phần giữa hầu như bằng 0."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về từ trường của Trái Đất và ứng dụng la bàn trong hàng hải:",
        "statements": [
          {
            "subId": "a",
            "text": "Trái Đất có từ trường bao bọc xung quanh, đóng vai trò như một lá chắn bảo vệ sinh quyển.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cực Nam của kim la bàn luôn bị hút về phía cực Bắc địa từ của Trái Đất.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trục từ của Trái Đất trùng khít hoàn toàn 100% với trục quay địa lý Bắc - Nam của Trái Đất.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Góc lệch giữa hướng Bắc địa từ và hướng Bắc địa lý được gọi là góc từ thiên.",
            "correct": true
          }
        ],
        "explanation": "Trục từ của Trái Đất nghiêng một góc khoảng 11 độ so với trục quay địa lý."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Về nam châm điện và các ứng dụng kỹ thuật trong thực tế:",
        "statements": [
          {
            "subId": "a",
            "text": "Nam châm điện chỉ sinh ra từ trường khi có dòng điện chạy qua cuộn dây dẫn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Có thể tăng lực từ của nam châm điện bằng cách tăng số vòng dây hoặc tăng cường độ dòng điện.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Lõi của nam châm điện nên dùng thép tôi cứng để tăng tốc độ khử từ khi ngắt công tắc.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Cần cẩu dọn sắt phế liệu ở các cảng biển sử dụng nam châm điện có công suất lớn.",
            "correct": true
          }
        ],
        "explanation": "Thép giữ từ tính lâu nên khó khử từ; lõi nam châm điện bắt buộc phải dùng sắt non."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một thanh nam châm thẳng ban đầu có 2 cực từ. Người ta cưa thanh nam châm này thành 3 đoạn ngắn bằng nhau. Hỏi tổng số cực từ của cả 3 đoạn nam châm mới là bao nhiêu cực?",
        "correctAnswer": "6",
        "explanation": "Mỗi đoạn nam châm sau khi cắt đều trở thành một nam châm mới có 2 cực (1 Bắc, 1 Nam). Tổng cộng có 3 x 2 = 6 cực."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một cuộn dây nam châm điện quấn 50 vòng hút được 10 chiếc kẹp ghim nhỏ. Nếu giữ nguyên dòng điện và muốn nam châm hút được 30 chiếc kẹp ghim thì cuộn dây cần có tổng cộng bao nhiêu vòng quấn?",
        "correctAnswer": "150",
        "explanation": "Số ghim tăng gấp 3 lần (30 / 10 = 3) nên số vòng quấn cũng phải tăng gấp 3 lần: 50 x 3 = 150 vòng."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Tại một trạm khí tượng thủy văn, người ta đo được góc từ thiên giữa kinh tuyến từ và kinh tuyến địa lý là 1,5 độ. Đổi số đo 1,5 độ này ra đơn vị phút góc (kí hiệu là ')?",
        "correctAnswer": "90",
        "explanation": "1 độ = 60 phút. Do đó 1,5 độ = 1,5 x 60 = 90'."
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Một cần cẩu nam châm điện bốc dỡ phế liệu tại nhà máy luyện kim có khả năng nâng tối đa một khối sắt nặng 3,2 tấn. Khối lượng này quy đổi ra đơn vị kilôgam (kg) là bao nhiêu?",
        "correctAnswer": "3200",
        "explanation": "3,2 tấn = 3,2 x 1000 = 3200 kg."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Một học sinh đưa một thanh nam châm lại gần 5 vật nhỏ trên bàn: (1) Chiếc kim bấm thép; (2) Đồng xu bằng nhôm; (3) Chiếc chìa khóa bằng đồng thau; (4) Ghim kẹp bằng niken; (5) Chiếc thước nhựa. Hỏi có bao nhiêu vật thể sẽ bị nam châm hút chặt?",
        "correctAnswer": "2",
        "explanation": "Có 2 vật bị nam châm hút là (1) kim bấm thép và (4) ghim niken."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khi nối cuộn dây nam châm điện với nguồn, ban đầu cường độ dòng điện là 0,4 A. Người ta điều chỉnh biến trở làm dòng điện tăng lên thành 1,6 A. Hỏi cường độ dòng điện đã tăng lên gấp bao nhiêu lần?",
        "correctAnswer": "4",
        "explanation": "Số lần tăng = 1,6 / 0,4 = 4 lần."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Từ trường Trái Đất (từ quyển) đóng vai trò là một tấm lá chắn tự nhiên vô cùng quan trọng đối với sự sống trên hành tinh chúng ta. Tấm lá chắn này bảo vệ sinh quyển chủ yếu bằng cách nào?",
        "options": [
          "Làm lệch hướng chuyển động của các hạt mang điện tích năng lượng cao từ gió Mặt Trời, ngăn chúng bắn phá mặt đất",
          "Ngăn chặn 100% ánh sáng nhìn thấy của Mặt Trời chiếu xuống mặt đất",
          "Hấp thụ toàn bộ nhiệt lượng từ vũ trụ để Trái Đất không bị nóng lên",
          "Ngăn chặn lực hút của Mặt Trăng gây ra hiện tượng thủy triều"
        ],
        "correct": 0,
        "explanation": "Từ quyển tạo lực từ làm lệch quỹ đạo các hạt tích điện từ gió Mặt Trời cuốn về hai cực tạo cực quang, bảo vệ sinh quyển."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trong một hệ thống rơ le bảo vệ quá tải: Lò xo kéo giữ tiếp điểm đóng mạch tải với một lực căng 15 N. Khi dòng điện qua cuộn dây nam châm điện vượt quá 6 A thì lực hút từ của nam châm đạt trên 15 N, thắng lực kéo lò xo và hút cần ngắt mạch điện. Nếu thay lò xo mới có lực căng 25 N thì cường độ dòng điện tối thiểu qua nam châm điện để ngắt mạch là bao nhiêu ampe (coi lực từ tỉ lệ thuận với dòng điện)?",
        "options": [
          "10 A",
          "8 A",
          "12 A",
          "9 A"
        ],
        "correct": 0,
        "explanation": "Lực từ tỉ lệ thuận với I: I2 = I1 x (F2 / F1) = 6 x (25 / 15) = 10 A."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để so sánh lực hút giữa các vị trí trên một thanh nam châm dài 24 cm, một học sinh dùng lực kế đo lực kéo nhả một viên bi thép nhỏ dính ở các vị trí: Đầu cực Bắc (N) đo được F1 = 1,8 N; vị trí cách đầu cực Bắc 6 cm đo được F2 = 0,9 N; vị trí chính giữa thanh (cách cực 12 cm) đo được F3. Giá trị của F3 xấp xỉ bằng bao nhiêu?",
        "options": [
          "Gần bằng 0 N",
          "1,8 N",
          "3,6 N",
          "0,9 N"
        ],
        "correct": 0,
        "explanation": "Tại vị trí chính giữa thanh nam châm thẳng, từ trường bị triệt tiêu gần như hoàn toàn nên lực hút F3 xấp xỉ 0 N."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một cần cẩu điện dọn sắt phế liệu ở bến cảng có công suất nâng 5 tấn hàng trong mỗi chuyến. Nếu sử dụng lõi nam châm bằng thép thường thay vì sắt non mềm thì sau khi ngắt công tắc điện, hiện tượng bất lợi nào nghiêm trọng nhất sẽ xảy ra?",
        "options": [
          "Lõi thép vẫn giữ từ tính lâu dài làm phế liệu sắt dính chặt không chịu rơi xuống vị trí bốc dỡ",
          "Thanh thép sẽ bị nổ tung do nhiệt độ tăng cao",
          "Dòng điện chạy ngược lại phá hỏng nguồn điện máy phát",
          "Cần cẩu bị mất trọng tâm lật đổ"
        ],
        "correct": 0,
        "explanation": "Thép có tính lưu từ cao, biến thành nam châm vĩnh cửu nên khi ngắt điện vẫn giữ sắt phế liệu không nhả ra được."
      }
    ]
  },
  "phys7_c6_rev_test2": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương VI - Đề số 02",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương VI",
    "testNum": 2,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Vật nào sau đây được gọi là một nam châm nhân tạo?",
        "options": [
          "Một thanh thép được từ hóa bằng dòng điện trong ống dây",
          "Một hòn đá nam châm thiên nhiên (quặng magnetit)",
          "Một mẩu gỗ hóa thạch",
          "Một mẩu đá vôi phong hóa"
        ],
        "correct": 0,
        "explanation": "Nam châm nhân tạo do con người chế tạo bằng cách từ hóa vật liệu từ."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trên một thanh nam châm thẳng, nơi nào có các đường sức từ phân bố dày đặc nhất?",
        "options": [
          "Ở sát gần hai đầu cực từ của nam châm",
          "Ở chính giữa thân thanh nam châm",
          "Ở cách xa nam châm 1 mét",
          "Ở mọi vị trí đều như nhau"
        ],
        "correct": 0,
        "explanation": "Hai đầu cực là nơi từ trường mạnh nhất, đường sức từ tập trung dày đặc nhất."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chiều của đường sức từ tại một điểm trong từ trường được xác định theo chiều nào?",
        "options": [
          "Chiều từ cực Nam đến cực Bắc của kim nam châm nhỏ nằm cân bằng tại điểm đó",
          "Chiều từ cực Bắc đến cực Nam của kim nam châm nhỏ",
          "Chiều của trọng lực hướng thẳng đứng xuống dưới",
          "Chiều gió thổi qua điểm đó"
        ],
        "correct": 0,
        "explanation": "Chiều đường sức từ trùng với chiều Nam - Bắc của kim nam châm thử thăng bằng tại điểm đó."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hiện tượng lịch sử nào khẳng định dòng điện có tác dụng từ?",
        "options": [
          "Dòng điện trong dây dẫn làm kim nam châm đặt gần đó quay lệch hướng",
          "Dòng điện làm dây tóc bóng đèn nóng sáng",
          "Dòng điện làm nước muối bị điện phân",
          "Dòng điện gây giật khi chạm tay"
        ],
        "correct": 0,
        "explanation": "Thí nghiệm Oersted phát hiện dòng điện làm quay kim nam châm."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Cực Nam địa từ của Trái Đất nằm ở vùng lân cận vị trí địa lý nào?",
        "options": [
          "Vùng cực Bắc địa lí của Trái Đất",
          "Vùng cực Nam địa lí của Trái Đất",
          "Vùng rừng rậm xích đạo châu Phi",
          "Tâm địa cầu"
        ],
        "correct": 0,
        "explanation": "Cực Nam địa từ nằm ở phía Bắc địa cầu, hút cực Bắc kim la bàn."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Khi đưa một thanh sắt non chưa nhiễm từ lại gần cực Bắc của một thanh nam châm thì thanh sắt non sẽ:",
        "options": [
          "Bị hút về phía cực Bắc của nam châm",
          "Bị cực Bắc của nam châm đẩy ra xa",
          "Không có hiện tượng gì xảy ra",
          "Tự động phát ra tia lửa điện"
        ],
        "correct": 0,
        "explanation": "Thanh sắt non bị nhiễm từ tạm thời và luôn bị hút vào cực của nam châm."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Thiết bị đóng ngắt mạch điện tự động bảo vệ hệ thống điện từ xa nhờ tác dụng từ của dòng điện là:",
        "options": [
          "Rơ le điện từ",
          "Chiếc cầu chì nhiệt",
          "Phích cắm điện xoay",
          "Bóng đèn sợi đốt"
        ],
        "correct": 0,
        "explanation": "Rơ le điện từ dùng nam châm điện để đóng ngắt mạch điện."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Để kim la bàn quay thật nhạy và định hướng chính xác nhất, trục đỡ kim la bàn thường được thiết kế như thế nào?",
        "options": [
          "Đặt trên một đầu mũi nhọn bằng kim loại cứng có ma sát cực nhỏ",
          "Gắn chặt bằng ốc vít cố định không quay được",
          "Dán chặt bằng keo dính",
          "Thả nổi tự do trong dầu nhớt đặc"
        ],
        "correct": 0,
        "explanation": "Trục nhọn giúp kim la bàn quay nhạy bén mà không bị lực ma sát cản trở."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Trong mạch điện của nam châm điện, khi ta ngắt công tắc điện thì hiện tượng gì xảy ra ngay lập tức?",
        "options": [
          "Từ trường của ống dây biến mất hoàn toàn",
          "Ống dây phát sáng màu đỏ",
          "Lực hút của ống dây tăng vọt",
          "Đinh sắt bị biến dạng cong gãy"
        ],
        "correct": 0,
        "explanation": "Không có dòng điện thì từ trường biến mất ngay lập tức."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Hiện tượng cực quang rực rỡ nhiều màu sắc ở bầu trời vùng cực Trái Đất được sinh ra do nguyên nhân nào?",
        "options": [
          "Các hạt mang điện từ gió Mặt Trời va chạm với phân tử khí quyển dưới tác dụng định hướng của từ trường Trái Đất",
          "Ánh sáng phản chiếu từ các tảng băng trôi khổng lồ",
          "Ánh đèn của các thành phố phản chiếu lên mây",
          "Mặt Trời chiếu sáng ban đêm ở vùng cực"
        ],
        "correct": 0,
        "explanation": "Gió Mặt Trời chứa electron, proton bị từ trường Trái Đất hướng về vùng cực tương tác với khí quyển sinh ra cực quang."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi đưa hai cực Nam của hai thanh nam châm thẳng lại gần nhau thì chúng sẽ:",
        "options": [
          "Đẩy nhau ra xa",
          "Hút chặt lấy nhau",
          "Đứng yên không tác dụng lực",
          "Biến thành hai cực Bắc"
        ],
        "correct": 0,
        "explanation": "Hai cực cùng tên (cùng cực Nam) thì đẩy nhau."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Nếu ta đảo ngược hai đầu dây nối của nam châm điện vào nguồn pin thì:",
        "options": [
          "Chiều từ trường bị đảo ngược, cực Bắc và cực Nam đổi chỗ cho nhau",
          "Nam châm điện mất hết từ tính",
          "Lực hút tăng lên gấp đôi",
          "Pin bị nổ tung ngay"
        ],
        "correct": 0,
        "explanation": "Đảo chiều dòng điện làm đảo chiều đường sức từ và hoán đổi vị trí hai cực từ."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về tương tác của thanh nam châm với các kim loại khác nhau trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Nam châm hút được thanh sắt, chiếc đinh thép và miếng hợp kim niken.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nam châm không hút được chiếc thìa nhôm, dây đồng và chiếc nhẫn vàng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nam châm có thể dùng để phân loại lon sắt thép và lon nhôm trong nhà máy tái chế.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu đưa cực Bắc của nam châm lại gần thanh đồng thì chúng sẽ đẩy nhau rất mạnh.",
            "correct": false
          }
        ],
        "explanation": "Đồng không tương tác từ với nam châm nên không bị đẩy cũng không bị hút."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về từ trường của dòng điện và thí nghiệm phát hiện của Oersted:",
        "statements": [
          {
            "subId": "a",
            "text": "Dây dẫn thẳng có dòng điện chạy qua sinh ra từ trường ở không gian xung quanh nó.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi ngắt dòng điện trong dây dẫn, tác dụng từ xung quanh dây dẫn cũng biến mất.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đường sức từ xung quanh một dây dẫn thẳng dài mang dòng điện là những đường tròn đồng tâm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dòng điện chỉ có tác dụng nhiệt và phát sáng, hoàn toàn không có tác dụng từ.",
            "correct": false
          }
        ],
        "explanation": "Dòng điện luôn có tác dụng từ khi chạy qua dây dẫn."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về từ quyển Trái Đất và hiện tượng bão từ trong vũ trụ:",
        "statements": [
          {
            "subId": "a",
            "text": "Từ quyển bao bọc Trái Đất kéo dài hàng chục nghìn kilômét ra ngoài không gian vũ trụ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bão từ xảy ra khi các đợt phun trào hạt tích điện mạnh từ Mặt Trời đập vào từ trường Trái Đất.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi xảy ra bão từ mạnh, các hệ thống định vị vệ tinh, sóng vô tuyến và mạng lưới truyền tải điện có thể bị gián đoạn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bão từ làm cho kim la bàn trên mặt đất luôn chỉ tuyệt đối chính xác không hề dao động.",
            "correct": false
          }
        ],
        "explanation": "Bão từ làm kim la bàn dao động mạnh hỗn loạn, không định vị chính xác được hướng."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Về các đặc tính kỹ thuật của nam châm điện công nghiệp:",
        "statements": [
          {
            "subId": "a",
            "text": "Để tăng lực từ lên mức tối đa, người ta quấn hàng nghìn vòng dây đồng và dùng lõi sắt non cỡ lớn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Có thể tắt mở lực từ nhanh chóng chỉ bằng thao tác bấm công tắc điều khiển điện.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nam châm điện tiêu thụ điện năng liên tục trong suốt thời gian giữ chặt vật phế liệu sắt.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nam châm điện không thể hút được vật nặng trên 100 kg.",
            "correct": false
          }
        ],
        "explanation": "Các nam châm điện công nghiệp có thể nâng các khối thép nặng hàng chục tấn."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một thanh nam châm thẳng ban đầu dài 20 cm bị bẻ gãy làm 4 đoạn bằng nhau. Hỏi sau khi bẻ, tổng số cực Bắc của tất cả các đoạn nam châm mới là bao nhiêu cực?",
        "correctAnswer": "4",
        "explanation": "Mỗi đoạn nam châm mới đều có đủ 1 cực Bắc và 1 cực Nam. Do đó 4 đoạn có 4 cực Bắc."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một cuộn dây nam châm điện có 120 vòng quấn nối nguồn điện hút được 24 kẹp sắt. Khi tháo bớt một nửa số vòng dây chỉ còn 60 vòng (giữ nguyên cường độ dòng điện qua mạch), hỏi số kẹp sắt hút được ước tính là bao nhiêu chiếc?",
        "correctAnswer": "12",
        "explanation": "Số vòng giảm đi một nửa (60 / 120 = 1/2) nên số kẹp sắt hút được cũng giảm một nửa: 24 / 2 = 12 chiếc."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Tại vùng xích đạo Trái Đất, góc từ thiên giữa trục từ và trục địa lý xấp xỉ 0 độ. Tại một hải cảng ở phương Bắc, máy đo ghi nhận góc từ thiên là 4,5 độ. Chênh lệch độ từ thiên giữa hai địa điểm này là bao nhiêu độ?",
        "correctAnswer": "4,5",
        "explanation": "Chênh lệch = 4,5 - 0 = 4,5 độ."
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Một cần cẩu nam châm điện tại bãi bốc xếp có khả năng nâng một lần 15 tấm tôn thép công nghiệp, biết mỗi tấm tôn nặng 80 kg. Tổng khối lượng tôn thép mà cần cẩu nâng được trong một lần là bao nhiêu kilôgam (kg)?",
        "correctAnswer": "1200",
        "explanation": "Tổng khối lượng = 15 x 80 = 1200 kg."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Một học sinh thử đưa nam châm lại gần 5 vật dụng trong phòng học: (1) Kim la bàn; (2) Đinh sắt; (3) Chiếc thìa bằng bạc; (4) Đoạn dây may-so niken-crom; (5) Cuộn dây cước câu cá. Hỏi có bao nhiêu vật dụng chịu lực hút của nam châm?",
        "correctAnswer": "3",
        "explanation": "Có 3 vật chịu lực hút là (1) kim la bàn, (2) đinh sắt, (4) dây may-so niken-crom."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Trong một thí nghiệm vật lý, khi dịch chuyển con chạy của biến trở làm điện trở mạch giảm xuống, cường độ dòng điện qua nam châm điện tăng từ 0,25 A lên 0,75 A. Hỏi cường độ dòng điện đã tăng thêm bao nhiêu ampe (A)?",
        "correctAnswer": "0,5",
        "explanation": "Cường độ tăng thêm = 0,75 - 0,25 = 0,5 A."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một đợt bùng phát bức xạ Mặt Trời mạnh (Solar Flare) phóng hàng tỉ tấn plasma hạt mang điện về phía Trái Đất gây bão từ cấp độ mạnh. Hiện tượng nào sau đây là hậu quả trực tiếp nguy hiểm nhất của cơn bão từ đối với mạng lưới công nghệ hiện đại trên Trái Đất?",
        "options": [
          "Gây ra dòng điện cảm ứng mạnh làm quá tải và cháy nổ các trạm biến áp cao thế, làm tê liệt hệ thống định vị vệ tinh GPS",
          "Làm cho nước biển dâng cao nhấn chìm các thành phố ven biển",
          "Làm cho nhiệt độ không khí giảm đột ngột xuống âm 50 độ C",
          "Làm cho Mặt Trăng ngừng quay quanh Trái Đất"
        ],
        "correct": 0,
        "explanation": "Bão từ cảm ứng dòng điện quá tải trong lưới điện cao thế gây mất điện diện rộng và làm nhiễu sóng định vị GPS vệ tinh."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trên tuyến đường tàu cao tốc đệm từ Maglev: Dưới đáy toa tàu gắn các nam châm điện có cực từ hướng xuống dưới là cực Bắc (N). Để toa tàu được nâng lơ lửng ổn định trên đường ray nhờ lực đẩy từ trường, các nam châm điện gắn dọc mặt trên của đường ray tiếp xúc đối diện với đáy toa tàu phải được cấp điện sao cho mặt trên của chúng là cực gì?",
        "options": [
          "Cực Bắc (N) để hai cực cùng tên đẩy nhau nâng toa tàu bay lên",
          "Cực Nam (S) để hai cực hút chặt toa tàu xuống ray",
          "Luân phiên đổi chiều 1000 lần mỗi giây",
          "Không cần cực từ nào cả"
        ],
        "correct": 0,
        "explanation": "Hai cực cùng tên (cùng cực Bắc N) đẩy nhau tạo lực nâng toa tàu lơ lửng trên đường ray."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hệ thống chuông điện báo cháy tự động hoạt động: Khi nhiệt độ môi trường vượt quá 70 độ C, thanh lưỡng kim nhiệt bị uốn cong chạm vào tiếp điểm đóng mạch điện cấp dòng 0,5 A cho cuộn dây nam châm điện. Nam châm điện ngay lập tức hút miếng sắt non kéo búa gõ vào chuông liên tục. Chức năng chính của thanh lưỡng kim nhiệt trong hệ thống này là:",
        "options": [
          "Đóng vai trò như một công tắc cảm biến nhiệt độ tự động đóng mạch điện khi quá nhiệt",
          "Tạo ra âm thanh chuông báo động trực tiếp",
          "Hấp thụ nhiệt để làm mát căn phòng",
          "Cung cấp nguồn điện 220V cho chuông"
        ],
        "correct": 0,
        "explanation": "Thanh lưỡng kim hoạt động như một công tắc nhiệt tự động đóng mạch khi gặp nhiệt độ cao."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "So sánh từ phổ của một thanh nam châm thẳng và một thanh nam châm hình chữ U: Tại sao ở khoảng không gian giữa hai nhánh cực của nam châm hình chữ U, các đường sức từ lại song song và cách đều nhau tạo thành từ trường đều?",
        "options": [
          "Vì hai cực Bắc và Nam đặt gần nhau đối diện nhau, đường sức từ đi thẳng từ cực Bắc sang cực Nam với mật độ đồng đều",
          "Vì nam châm chữ U có từ tính mạnh gấp 10 lần nam châm thẳng",
          "Vì sắt làm nam châm chữ U dẫn từ tốt hơn thanh thẳng",
          "Vì không có không khí lọt vào giữa hai cực"
        ],
        "correct": 0,
        "explanation": "Hai cực đối diện ở khoảng cách ngắn làm các đường sức từ phân bố thẳng song song và đều đặn (từ trường đều)."
      }
    ]
  },
  "phys7_c6_rev_test3": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương VI - Đề số 03",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương VI",
    "testNum": 3,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Ở thanh nam châm hình chữ U, các đường sức từ ở khoảng giữa hai nhánh cực có hình dạng như thế nào?",
        "options": [
          "Gần như song song và cách đều nhau",
          "Là những vòng tròn đồng tâm",
          "Là những đường xoắn ốc tỏa rộng",
          "Không có đường sức từ nào"
        ],
        "correct": 0,
        "explanation": "Giữa hai cực nam châm chữ U là từ trường đều, các đường sức từ gần như song song và cách đều nhau."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Vật liệu nào sau đây giữ được từ tính lâu dài nhất sau khi bị nhiễm từ trong từ trường mạnh?",
        "options": [
          "Thép carbon cứng",
          "Sắt non mềm",
          "Đồng thau",
          "Nhôm đúc"
        ],
        "correct": 0,
        "explanation": "Thép có tính khử từ chậm, giữ từ tính lâu dài tạo thành nam châm vĩnh cửu."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi rắc mạt sắt lên tấm bìa đặt trên thanh nam châm rồi gõ nhẹ, các hạt mạt sắt sắp xếp như thế nào?",
        "options": [
          "Theo các đường cong nối từ cực này sang cực kia của nam châm",
          "Tụ tập thành một khối tròn duy nhất ở giữa",
          "Phân bố tản mạn ngẫu nhiên không quy luật",
          "Tất cả bị đẩy bay ra khỏi tấm bìa"
        ],
        "correct": 0,
        "explanation": "Mạt sắt sắp xếp thành các đường cong nối từ cực này sang cực kia tạo thành từ phổ."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kim nam châm của một chiếc la bàn thông thường luôn quay tự do quanh trục thẳng đứng và nằm thăng bằng theo phương nào?",
        "options": [
          "Phương Bắc - Nam địa lí",
          "Phương Đông - Tây",
          "Phương thẳng đứng cắm xuống đất",
          "Phương song song với tia sáng"
        ],
        "correct": 0,
        "explanation": "Kim nam châm tự do luôn thăng bằng theo phương Bắc - Nam địa lí."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Từ trường của Trái Đất có hình dạng tương tự như từ trường của vật nào sau đây?",
        "options": [
          "Một thanh nam châm thẳng khổng lồ nằm nghiêng trong lòng Trái Đất",
          "Một chiếc đĩa nam châm tròn mỏng",
          "Một cuộn dây xoắn hình lò xo",
          "Một khối cầu không có cực từ"
        ],
        "correct": 0,
        "explanation": "Từ trường Trái Đất tương tự một nam châm thẳng khổng lồ với trục từ nghiêng khoảng 11 độ so với trục địa lý."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Lõi sắt non đặt trong cuộn dây có dòng điện có tác dụng gì quan trọng nhất?",
        "options": [
          "Làm tăng cường độ từ trường của cuộn dây lên rất nhiều lần",
          "Làm giảm nhiệt độ của cuộn dây",
          "Làm tăng khối lượng để cuộn dây đứng vững",
          "Làm đổi màu tia lửa điện"
        ],
        "correct": 0,
        "explanation": "Lõi sắt non bị nhiễm từ mạnh, làm tăng đáng kể từ trường của ống dây."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Để thay đổi cực từ Bắc và Nam của một nam châm điện, thao tác đơn giản và chuẩn xác nhất là:",
        "options": [
          "Đổi chiều dòng điện chạy qua cuộn dây",
          "Rút lõi sắt non ra quay ngược đầu lại",
          "Sơn lại màu sắc hai đầu đinh sắt",
          "Tăng thêm hiệu điện thế nguồn điện"
        ],
        "correct": 0,
        "explanation": "Đổi chiều dòng điện làm đảo chiều các đường sức từ và các cực từ."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Thiết bị nào sau đây biến đổi dao động điện thành dao động âm thanh nhờ lực từ tương tác giữa nam châm và cuộn âm?",
        "options": [
          "Loa điện động",
          "Bếp từ gia đình",
          "Chiếc ấm siêu tốc",
          "Bàn là hơi nước"
        ],
        "correct": 0,
        "explanation": "Loa điện động hoạt động dựa trên tương tác lực từ giữa cuộn dây có dòng âm tần và nam châm vĩnh cửu."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một thanh nam châm vĩnh cửu KHÔNG tác dụng lực hút từ lên vật thể nào sau đây?",
        "options": [
          "Một chiếc que bằng thủy tinh trong suốt",
          "Một chiếc đinh bằng thép cacbon",
          "Một mẩu dây niken",
          "Một thanh sắt non"
        ],
        "correct": 0,
        "explanation": "Thủy tinh là chất vô cơ không có từ tính nên không bị nam châm hút."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khi đưa cực Bắc của thanh nam châm 1 lại gần cực Nam của thanh nam châm 2 thì hai thanh nam châm sẽ:",
        "options": [
          "Hút chặt lấy nhau",
          "Đẩy nhau ra xa",
          "Không có bất kì tương tác nào",
          "Làm mất hết từ tính của nhau"
        ],
        "correct": 0,
        "explanation": "Hai cực khác tên (Bắc và Nam) thì hút nhau."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Quy ước sơn màu hoặc kí hiệu đầu cực Nam của kim la bàn thông thường là gì?",
        "options": [
          "Sơn màu xanh hoặc trắng, kí hiệu chữ S",
          "Sơn màu đỏ tươi, kí hiệu chữ N",
          "Sơn màu vàng đậm, kí hiệu chữ E",
          "Sơn màu tím, kí hiệu chữ W"
        ],
        "correct": 0,
        "explanation": "Cực Nam kí hiệu là S (South), thường được sơn màu xanh hoặc màu trắng."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một học sinh quấn một nam châm điện và thấy nó hút được 5 chiếc kẹp giấy. Học sinh muốn nam châm hút được 15 chiếc kẹp giấy thì cần thực hiện cách nào?",
        "options": [
          "Mắc thêm pin nối tiếp để tăng dòng điện và quấn thêm nhiều vòng dây",
          "Tháo bớt 2/3 số vòng dây ra",
          "Thay lõi sắt non bằng lõi nhựa dẻo",
          "Mắc thêm điện trở lớn vào mạch"
        ],
        "correct": 0,
        "explanation": "Tăng số vòng dây và tăng cường độ dòng điện giúp nam châm hút mạnh hơn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về cấu tạo và hình dạng đường sức từ của nam châm hình chữ U:",
        "statements": [
          {
            "subId": "a",
            "text": "Nam châm chữ U có hai cực từ Bắc và Nam nằm ở hai đầu nhánh cong.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đường sức từ ở khoảng giữa hai nhánh đi thẳng từ cực Bắc sang cực Nam.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đường sức từ ở vùng bên ngoài hai nhánh uốn cong khép kín tương tự nam châm thẳng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Từ trường ở khoảng cách rất xa nam châm chữ U mạnh hơn nhiều so với ở khoảng giữa hai cực.",
            "correct": false
          }
        ],
        "explanation": "Từ trường mạnh nhất tập trung dày đặc ở khoảng giữa hai cực, càng ra xa càng yếu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về sự nhiễm từ của sắt non và thép trong kỹ thuật chế tạo:",
        "statements": [
          {
            "subId": "a",
            "text": "Sắt non dễ bị nhiễm từ nhưng cũng rất dễ mất từ tính khi đưa ra khỏi từ trường.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thép khó nhiễm từ hơn nhưng một khi đã nhiễm từ thì giữ từ tính rất bền vững.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Người ta dùng thép để chế tạo nam châm vĩnh cửu dùng trong loa, la bàn, nắp tủ lạnh.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong cần cẩu dọn phế liệu, bắt buộc phải dùng lõi thép tôi cứng để tăng lực giữ hàng.",
            "correct": false
          }
        ],
        "explanation": "Nếu dùng lõi thép thì khi ngắt điện nam châm không chịu nhả phế liệu ra."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về hiện tượng sinh học định hướng theo từ trường Trái Đất của các loài động vật di cư:",
        "statements": [
          {
            "subId": "a",
            "text": "Các loài chim bồ câu, én biển có thể bay hàng nghìn kilômét mà không bị lạc đường nhờ cảm nhận từ trường Trái Đất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong cơ thể một số loài sinh vật di cư có chứa các tinh thể khoáng vật từ tính (magnetit) siêu nhỏ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu gắn một thanh nam châm nhỏ làm nhiễu từ trường lên đầu chim bồ câu, khả năng định hướng của chúng sẽ bị rối loạn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Rùa biển bơi qua đại dương hoàn toàn dựa vào ngọn hải đăng của con người, không có khả năng cảm nhận từ trường.",
            "correct": false
          }
        ],
        "explanation": "Rùa biển sơ sinh định hướng bơi vượt đại dương nhờ cảm nhận độ nghiêng và cường độ từ trường Trái Đất."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Về cấu tạo và nguyên lý hoạt động của màng loa điện động:",
        "statements": [
          {
            "subId": "a",
            "text": "Gồm một nam châm vĩnh cửu hình trụ và một cuộn dây âm tần gắn dính liền với màng loa.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi có dòng điện âm tần biến thiên chạy qua cuộn dây, cuộn dây chịu lực từ hút đẩy biến thiên liên tục.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Màng loa dao động rung động không khí xung quanh, tái tạo ra sóng âm thanh truyền đến tai người nghe.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Màng loa chỉ có thể rung được nếu cuộn dây được làm hoàn toàn bằng dây nhựa cách điện.",
            "correct": false
          }
        ],
        "explanation": "Cuộn dây âm tần bắt buộc phải làm bằng dây đồng dẫn điện tráng men cách điện."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một thanh nam châm hình chữ U có 2 cực từ. Nếu dùng 3 thanh nam châm hình chữ U giống hệt nhau thì tổng số cực từ của cả 3 thanh nam châm này là bao nhiêu cực?",
        "correctAnswer": "6",
        "explanation": "Mỗi thanh nam châm có 2 cực từ. 3 thanh có tổng cộng: 3 x 2 = 6 cực."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một cuộn dây nam châm điện có 90 vòng dây hút được 18 viên bi sắt nhỏ. Nếu quấn thêm 60 vòng dây nữa thành 150 vòng (với cùng cường độ dòng điện), hỏi số viên bi sắt hút được ước tính là bao nhiêu viên?",
        "correctAnswer": "30",
        "explanation": "Tỉ lệ số vòng = 150 / 90 = 5/3. Số bi sắt hút được = 18 x (5/3) = 30 viên bi."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Độ nghiêng từ (góc giữa kim nam châm tự do và mặt phẳng nằm ngang) tại một vị trí vĩ độ cao được đo là 65 độ. Góc phụ của góc nghiêng từ này (bằng 90 độ trừ đi góc nghiêng từ) có giá trị là bao nhiêu độ?",
        "correctAnswer": "25",
        "explanation": "Góc phụ = 90 - 65 = 25 độ."
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Một cần trục nam châm điện bốc xếp tại xưởng luyện cán thép có thể nâng một khối máy nặng 4,5 tấn trong một lần cẩu. Khối lượng này tương đương bao nhiêu kilôgam (kg)?",
        "correctAnswer": "4500",
        "explanation": "4,5 tấn = 4,5 x 1000 = 4500 kg."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Người ta thử đưa nam châm lại gần 6 mẫu vật: (1) Đinh sắt; (2) Kẹp bướm bằng thép; (3) Khối gỗ lim; (4) Đoạn dây đồng; (5) Tấm nhựa PVC; (6) Đồng xu bằng niken. Hỏi có bao nhiêu mẫu vật KHÔNG BỊ nam châm hút?",
        "correctAnswer": "3",
        "explanation": "Có 3 mẫu không bị hút là (3) khối gỗ lim, (4) dây đồng, (5) tấm nhựa PVC."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khi điều chỉnh biến trở trong mạch nam châm điện, cường độ dòng điện tăng từ 0,6 A lên 1,8 A. Hỏi cường độ dòng điện đã tăng lên gấp bao nhiêu lần?",
        "correctAnswer": "3",
        "explanation": "Số lần tăng = 1,8 / 0,6 = 3 lần."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Trong cấu tạo của loa điện động: Cuộn dây âm tần có đường kính 25 mm được đặt trong khe hở hẹp có từ trường rất mạnh của nam châm vĩnh cửu. Khi tín hiệu âm thanh có tần số f = 440 Hz (nốt La chuẩn) chạy qua cuộn dây, màng loa sẽ thực hiện bao nhiêu chu kì dao động cơ học trong đúng 1 giây?",
        "options": [
          "440 chu kì",
          "220 chu kì",
          "880 chu kì",
          "100 chu kì"
        ],
        "correct": 0,
        "explanation": "Tần số f = 440 Hz nghĩa là màng loa thực hiện đúng 440 chu kì dao động trong mỗi giây."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một nhà sinh vật học nghiên cứu chim bồ câu đưa thư: Người ta phát hiện trong mỏ của chim có các cụm tế bào thần kinh chứa hạt nano magnetit nhạy cảm với từ trường Trái Đất có độ lớn B = 50 microtesla (50 uT). Khi chim bay qua vùng có dây điện cao thế phát ra từ trường nhân tạo lên tới 200 microtesla, chim có hiện tượng bay vòng tròn mất phương hướng. Cường độ từ trường nhân tạo này gấp bao nhiêu lần từ trường Trái Đất tại nơi đó?",
        "options": [
          "4 lần",
          "2 lần",
          "5 lần",
          "8 lần"
        ],
        "correct": 0,
        "explanation": "Tỉ số cường độ từ trường = 200 / 50 = 4 lần."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để phân loại quặng sắt trong công nghiệp khai khoáng: Băng chuyền chở quặng hỗn hợp chạy qua quả lô từ tính (nam châm điện hình trụ quay). Quặng chứa hàm lượng sắt cao bị quả lô từ hút bám dính vào băng chuyền đưa sang máng A, đất đá trơ rơi thẳng xuống máng B. Biện pháp nào sau đây giúp tăng tỉ lệ thu hồi quặng sắt vụn nhỏ mịn trên băng chuyền?",
        "options": [
          "Tăng cường độ dòng điện qua các cuộn dây của quả lô từ để tăng lực hút từ",
          "Tăng tốc độ chạy của băng chuyền lên gấp đôi",
          "Tưới thêm thật nhiều nước lạnh lên băng chuyền",
          "Đổi quả lô từ bằng quả lô cao su"
        ],
        "correct": 0,
        "explanation": "Tăng cường độ dòng điện làm từ trường quả lô mạnh hơn, hút giữ được các hạt quặng sắt nhỏ mịn tốt hơn."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một thanh nam châm thẳng bị gỉ sét làm mất hết các kí hiệu màu sơn đánh dấu cực Bắc và cực Nam. Một học sinh dùng một sợi chỉ mảnh buộc vào chính giữa thanh nam châm rồi treo lơ lửng trên giá gỗ cách xa các vật kim loại. Khi thanh nam châm dừng dao động và đứng yên thăng bằng, đầu thanh chỉ về hướng Bắc địa lý của Trái Đất chính là cực gì của nam châm?",
        "options": [
          "Cực Bắc (N) của nam châm",
          "Cực Nam (S) của nam châm",
          "Cực trung hòa của nam châm",
          "Không xác định được"
        ],
        "correct": 0,
        "explanation": "Theo định nghĩa, đầu của nam châm tự do chỉ về phương Bắc địa lý được gọi là cực Bắc (N) của nam châm."
      }
    ]
  },
  "phys7_c6_rev_test4": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương VI - Đề số 04",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương VI",
    "testNum": 4,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Nam châm thể hiện tính chất từ bằng khả năng hút mạnh các vật làm bằng chất nào sau đây?",
        "options": [
          "Chất sắt từ như sắt, niken, coban, thép",
          "Chất cách điện như nhựa, cao su",
          "Kim loại quý như vàng, bạc",
          "Kim loại nhẹ như nhôm, titan"
        ],
        "correct": 0,
        "explanation": "Nam châm hút các vật liệu sắt từ như sắt, thép, coban, niken."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Các đường sức từ trong không gian cho phép chúng ta hình dung trực quan về đặc điểm nào của từ trường?",
        "options": [
          "Hình dạng, hướng và độ mạnh yếu của từ trường",
          "Nhiệt độ của vùng không gian có từ trường",
          "Vận tốc di chuyển của từ trường",
          "Màu sắc của từ trường"
        ],
        "correct": 0,
        "explanation": "Đường sức từ mô tả trực quan hình dạng, hướng và độ dày/thưa (mạnh/yếu) của từ trường."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Bên ngoài thanh nam châm thẳng, đường sức từ có chiều đi ra từ cực nào và đi vào cực nào?",
        "options": [
          "Đi ra từ cực Bắc và đi vào cực Nam",
          "Đi ra từ cực Nam và đi vào cực Bắc",
          "Đi ra từ hai đầu và đi vào giữa",
          "Đi ra từ giữa và đi vào hai đầu"
        ],
        "correct": 0,
        "explanation": "Quy ước: Ra Bắc (N) vào Nam (S)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tại bất kì vị trí nào trên Trái Đất, kim nam châm của la bàn luôn có xu hướng định hướng theo phương nào?",
        "options": [
          "Phương Bắc - Nam từ trường",
          "Phương Đông - Tây",
          "Phương gió thổi",
          "Phương đường xích đạo"
        ],
        "correct": 0,
        "explanation": "Kim la bàn luôn định hướng theo đường sức từ của Trái Đất (phương Bắc - Nam từ trường)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tác dụng từ của dòng điện lần đầu tiên trong lịch sử khoa học được phát hiện bởi nhà bác học nào?",
        "options": [
          "Hans Christian Oersted",
          "Isaac Newton",
          "Michael Faraday",
          "Albert Einstein"
        ],
        "correct": 0,
        "explanation": "Năm 1820, Oersted phát hiện dòng điện làm lệch kim nam châm."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Khi quấn dây dẫn quanh đinh sắt rồi nối pin, nếu ngắt nguồn pin thì đinh sắt sẽ như thế nào?",
        "options": [
          "Mất hầu hết từ tính ngay lập tức",
          "Biến thành nam châm vĩnh cửu hút cực mạnh",
          "Phát sáng màu vàng",
          "Nóng chảy ngay"
        ],
        "correct": 0,
        "explanation": "Đinh sắt non mất từ tính gần như ngay lập tức khi ngắt dòng điện."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Đặc điểm nào sau đây là ưu thế vượt trội của nam châm điện mà nam châm vĩnh cửu KHÔNG CÓ?",
        "options": [
          "Có thể dễ dàng bật tắt từ tính và điều chỉnh lực hút bằng dòng điện",
          "Không cần dây dẫn điện",
          "Không bao giờ bị nóng lên",
          "Lực hút luôn giữ nguyên một mức duy nhất"
        ],
        "correct": 0,
        "explanation": "Nam châm điện điều khiển được từ tính thông qua công tắc và cường độ dòng điện."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Để bảo vệ các thiết bị đo điện tử cực kì nhạy cảm khỏi bị ảnh hưởng bởi từ trường mạnh bên ngoài, người ta thường dùng biện pháp nào?",
        "options": [
          "Đặt thiết bị bên trong một hộp kín làm bằng sắt non mềm (màn chắn từ)",
          "Bọc thiết bị bằng vải bông dày",
          "Sơn màu đỏ lên vỏ thiết bị",
          "Đặt thiết bị dưới nước"
        ],
        "correct": 0,
        "explanation": "Vỏ sắt non có độ dẫn từ rất cao, hút các đường sức từ chạy bên trong vỏ hộp, che chắn không gian bên trong."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Trong một chiếc rơ le điện từ, bộ phận nào đóng vai trò tạo ra lực hút để đóng ngắt mạch điện tự động?",
        "options": [
          "Nam châm điện",
          "Lò xo lá thép",
          "Bóng đèn sợi đốt",
          "Cầu chì thủy tinh"
        ],
        "correct": 0,
        "explanation": "Nam châm điện tạo ra lực từ hút lẫy sắt đóng ngắt mạch điện."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khi hai cực Bắc của hai thanh nam châm được đưa lại gần nhau thì lực tương tác giữa chúng là lực gì?",
        "options": [
          "Lực đẩy",
          "Lực hút",
          "Lực ma sát",
          "Lực đàn hồi"
        ],
        "correct": 0,
        "explanation": "Các cực cùng tên thì đẩy nhau."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Các cơn bão từ phát sinh từ hoạt động của Mặt Trời gây ra tác hại chủ yếu nào đối với đời sống công nghệ con người?",
        "options": [
          "Gây nhiễu loạn liên lạc vô tuyến, mất sóng GPS và có thể phá hỏng lưới truyền tải điện",
          "Gây động đất và núi lửa phun trào",
          "Làm nước biển đóng băng",
          "Làm các tòa nhà cao ốc bị đổ sập"
        ],
        "correct": 0,
        "explanation": "Bão từ gây cảm ứng từ trường biến thiên mạnh làm hư hỏng lưới điện và viễn thông vệ tinh."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Đồ vật nào sau đây KHÔNG CHỨA nam châm trong cấu tạo của nó?",
        "options": [
          "Chiếc cốc bằng thủy tinh chịu nhiệt",
          "Chiếc loa nghe nhạc mini",
          "Cánh cửa tủ lạnh gia đình",
          "Chiếc la bàn bỏ túi"
        ],
        "correct": 0,
        "explanation": "Cốc thủy tinh hoàn toàn không chứa nam châm."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các quy tắc xác định cực từ và chiều của đường sức từ:",
        "statements": [
          {
            "subId": "a",
            "text": "Bên ngoài nam châm, đường sức từ đi ra từ cực Bắc và đi vào cực Nam.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bên trong lòng thanh nam châm, đường sức từ đi từ cực Nam sang cực Bắc tạo thành đường cong khép kín.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hai đường sức từ bất kì trong cùng một từ trường không bao giờ cắt nhau.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nơi nào đường sức từ thưa thớt thì từ trường tại nơi đó là cực mạnh.",
            "correct": false
          }
        ],
        "explanation": "Nơi đường sức từ thưa thớt là nơi từ trường yếu; nơi dày đặc là từ trường mạnh."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về hiện tượng nhiễm từ và phân loại chất từ trong kỹ thuật:",
        "statements": [
          {
            "subId": "a",
            "text": "Sắt non, thép, niken và coban là các chất sắt từ bị nam châm hút mạnh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đồng, nhôm, gỗ, thủy tinh không bị nhiễm từ trong điều kiện thông thường.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi cọ xát một thanh thép nhiều lần theo một chiều vào cực nam châm, thanh thép sẽ bị nhiễm từ trở thành nam châm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Có thể biến một chiếc thước kẻ nhựa thành nam châm vĩnh cửu bằng cách đặt vào lòng ống dây có dòng điện.",
            "correct": false
          }
        ],
        "explanation": "Nhựa là chất cách điện phi từ tính, không thể bị từ hóa thành nam châm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về cấu trúc từ quyển của Trái Đất và vai trò che chở sự sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Từ quyển Trái Đất kéo dài và bị gió Mặt Trời ép dẹp ở phía ban ngày, kéo dài thành đuôi từ ở phía ban đêm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Từ trường Trái Đất ngăn cản các hạt bức xạ vũ trụ nguy hiểm bắn phá trực tiếp lên bề mặt Trái Đất.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu Trái Đất mất đi từ trường, bầu khí quyển và sự sống sẽ đứng trước nguy cơ bị bức xạ vũ trụ hủy diệt.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Cực Bắc từ trường Trái Đất trùng khít tuyệt đối 100% với điểm cực Bắc địa lý của quả địa cầu.",
            "correct": false
          }
        ],
        "explanation": "Cực Bắc từ trường Trái Đất lệch xa cực Bắc địa lý hàng trăm kilômét."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Về ứng dụng của nam châm điện trong hệ thống phanh hãm của đoàn tàu cao tốc:",
        "statements": [
          {
            "subId": "a",
            "text": "Hệ thống phanh điện từ sử dụng các nam châm điện cực mạnh hạ sát mặt ray thép.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tương tác từ tạo ra lực cản hãm đoàn tàu dừng lại mà không gây mài mòn cơ học má phanh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi cần nhả phanh để tàu chạy tiếp, người lái tàu chỉ cần ngắt dòng điện cung cấp cho nam châm điện.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phanh điện từ chỉ hoạt động được khi đường ray tàu hỏa được đúc bằng gỗ nguyên khối.",
            "correct": false
          }
        ],
        "explanation": "Đường ray bắt buộc phải bằng thép để tạo tương tác từ và dòng điện xoáy hãm phanh."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một thanh nam châm thẳng có 2 cực. Nếu ta đem 4 thanh nam châm giống hệt nhau ghép nối tiếp đuôi nhau (cực Bắc thanh này nối vào cực Nam thanh kia) thành một thanh dài duy nhất. Hỏi thanh dài mới này có tổng cộng bao nhiêu cực từ ở hai đầu ngoài cùng?",
        "correctAnswer": "2",
        "explanation": "Khi ghép nối tiếp, các cực ở chỗ nối triệt tiêu lẫn nhau, thanh dài mới trở thành một nam châm duy nhất có đúng 2 cực (1 Bắc và 1 Nam) ở hai đầu tự do."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một cuộn dây nam châm điện quấn 75 vòng dây hút được 15 chiếc kẹp giấy. Nếu muốn nam châm hút được 30 chiếc kẹp giấy với cùng nguồn điện đó thì cần quấn cuộn dây có tổng cộng bao nhiêu vòng quấn?",
        "correctAnswer": "150",
        "explanation": "Số kẹp giấy tăng gấp 2 lần (30 / 15 = 2) nên số vòng quấn cần tăng gấp 2 lần: 75 x 2 = 150 vòng."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một nhà thám hiểm sử dụng la bàn tại một hòn đảo có góc lệch từ thiên giữa kinh tuyến từ và kinh tuyến thực là 2,5 độ. Đổi góc lệch này ra đơn vị phút góc (kí hiệu là ')?",
        "correctAnswer": "150",
        "explanation": "1 độ = 60 phút. Do đó 2,5 độ = 2,5 x 60 = 150'."
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Một cần cẩu nam châm điện dọn phế liệu nâng được 6 khối thép, mỗi khối có khối lượng 350 kg. Tổng khối lượng phế liệu thép mà cần cẩu đã nâng trong chuyến này là bao nhiêu kilôgam (kg)?",
        "correctAnswer": "2100",
        "explanation": "Tổng khối lượng = 6 x 350 = 2100 kg."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Trong một hộp dụng cụ có 5 que kim loại cùng kích thước: que 1 bằng thép, que 2 bằng nhôm, que 3 bằng niken, que 4 bằng chì, que 5 bằng bạc. Hỏi có bao nhiêu que kim loại KHÔNG BỊ nam châm hút?",
        "correctAnswer": "3",
        "explanation": "Có 3 que không bị hút là: que 2 (nhôm), que 4 (chì), que 5 (bạc)."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Trong mạch điện thí nghiệm, khi điều chỉnh biến trở làm cường độ dòng điện chạy qua nam châm điện tăng từ 0,5 A lên 2,0 A. Hỏi cường độ dòng điện đã tăng lên gấp bao nhiêu lần?",
        "correctAnswer": "4",
        "explanation": "Số lần tăng = 2,0 / 0,5 = 4 lần."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hiện tượng màn chắn từ: Một đồng hồ cơ khí đắt tiền có các bánh răng thép siêu nhỏ được bọc trong một lớp vỏ bằng sắt non mềm dày 1,2 mm. Khi người đeo đồng hồ đi vào khu vực chụp cộng hưởng từ MRI có từ trường rất mạnh 1,5 Tesla, đồng hồ vẫn chạy hoàn toàn chính xác. Nguyên nhân khoa học của hiện tượng này là gì?",
        "options": [
          "Lớp vỏ sắt non có độ thẩm từ rất lớn, hút hầu như toàn bộ các đường sức từ chạy khép kín bên trong lớp vỏ kim loại, bảo vệ bộ máy bên trong",
          "Lớp vỏ sắt non đẩy lùi hoàn toàn các đường sức từ ra xa như gương phản xạ",
          "Sắt non làm đóng băng từ trường không cho chuyển động",
          "Từ trường MRI không tương tác với kim loại thép"
        ],
        "correct": 0,
        "explanation": "Sắt non hút các đường sức từ tập trung chạy trong thân vỏ sắt, làm không gian rỗng bên trong hầu như không còn từ trường (màn chắn từ)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trên đường ray tàu đệm từ Maglev: Một khối toa tàu nặng 40 tấn cần được nâng lên khỏi mặt ray một khe hở 10 mm. Khi dòng điện qua hệ thống nam châm nâng là 200 A thì lực nâng cân bằng vừa đúng trọng lực toa tàu. Nếu khối lượng hành khách và hàng hóa chở thêm là 10 tấn (tổng 50 tấn) thì dòng điện qua nam châm nâng cần điều chỉnh lên mức bao nhiêu ampe để duy trì khe hở nâng (coi lực từ tỉ lệ thuận với dòng điện)?",
        "options": [
          "250 A",
          "220 A",
          "300 A",
          "240 A"
        ],
        "correct": 0,
        "explanation": "Tỉ số trọng lượng = 50 / 40 = 1,25 lần. Cường độ dòng điện cần điều chỉnh = 200 x 1,25 = 250 A."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Thiết kế mạch cảnh báo rò rỉ khí gas tự động trong chung cư: Cảm biến phát hiện nồng độ gas tăng sẽ đóng công tắc cấp điện 12 V cho cuộn dây nam châm điện. Nam châm điện hút chốt thép an toàn trong 0,05 giây làm sập lò xo ngắt van gas tổng, đồng thời đóng mạch phụ kích hoạt còi hú 110 dB. Yêu cầu vật liệu làm lõi nam châm điện trong hệ thống này bắt buộc phải là:",
        "options": [
          "Sắt non mềm để hút dứt khoát và nhả chốt khi cần thiết lập lại hệ thống",
          "Thép tôi cứng vĩnh cửu",
          "Thanh đồng thau nguyên khối",
          "Thanh nhôm đúc"
        ],
        "correct": 0,
        "explanation": "Lõi sắt non có độ cảm từ cao, đáp ứng nhanh và dễ dàng hồi phục vị trí khi reset hệ thống."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét từ trường tạo bởi hai cực khác tên (cực Bắc N của thanh 1 và cực Nam S của thanh 2) đặt đối diện nhau và cách nhau một khoảng hở hẹp 3 cm. Hình ảnh đường sức từ trong khoảng không gian 3 cm giữa hai cực này có đặc điểm gì?",
        "options": [
          "Là những đường thẳng gần như song song, cách đều nhau và hướng thẳng từ cực Bắc của thanh 1 sang cực Nam của thanh 2",
          "Là những đường tròn xoắn ốc ngược chiều kim đồng hồ",
          "Đường sức từ uốn cong ra xa tránh né hai cực",
          "Đường sức từ biến mất hoàn toàn do triệt tiêu nhau"
        ],
        "correct": 0,
        "explanation": "Giữa hai cực khác tên đặt gần nhau, các đường sức từ đi thẳng song song từ cực Bắc sang cực Nam tạo thành từ trường đều."
      }
    ]
  },
  "phys7_c6_rev_test5": {
    "title": "Đề kiểm tra KHTN 7 (Vật lý) - [Đề tổng hợp] Ôn tập cuối Chương VI - Đề số 05",
    "grade": "7",
    "subject": "physics",
    "subjectName": "Vật lý",
    "chapterId": "phys7_c6",
    "chapterTitle": "Chương VI: Từ",
    "lessonId": "phys7_c6_rev",
    "lessonName": "[Đề tổng hợp] Ôn tập cuối Chương VI",
    "testNum": 5,
    "duration": "45 phút",
    "points": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khi cọ xát một đầu thanh nam châm vào chiếc kim may bằng thép nhiều lần theo một chiều nhất định, chiếc kim sẽ:",
        "options": [
          "Bị nhiễm từ và trở thành một nam châm nhỏ giữ được từ tính",
          "Nóng chảy thành chất lỏng",
          "Bị biến mất",
          "Mất hết khả năng dẫn điện"
        ],
        "correct": 0,
        "explanation": "Thép khi bị cọ xát với nam châm sẽ bị nhiễm từ trở thành nam châm vĩnh cửu."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đặc điểm cơ bản quan trọng của các đường sức từ trong từ trường là:",
        "options": [
          "Là những đường cong khép kín hoặc đi từ vô cực đến vô cực, không bao giờ cắt nhau",
          "Luôn cắt nhau tại một điểm duy nhất",
          "Là các đường gấp khúc sắc nhọn",
          "Là các đoạn thẳng hở hai đầu"
        ],
        "correct": 0,
        "explanation": "Đường sức từ là những đường cong khép kín không cắt nhau."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Ở ngay tại vùng cực từ của Trái Đất, kim nam châm của một la bàn đa năng có xu hướng định hướng theo phương nào?",
        "options": [
          "Phương gần như thẳng đứng cắm xuống mặt đất",
          "Phương nằm ngang song song mặt đất",
          "Phương tạo góc 45 độ với mặt đất",
          "Quay tít liên tục không dừng"
        ],
        "correct": 0,
        "explanation": "Tại các cực từ, đường sức từ đâm thẳng đứng vào hoặc đi thẳng ra khỏi mặt đất nên kim la bàn chúc thẳng đứng."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Yếu tố nào sau đây quyết định chiều của đường sức từ xung quanh một cuộn dây có dòng điện chạy qua?",
        "options": [
          "Chiều của dòng điện chạy qua các vòng dây",
          "Chiều dài của sợi dây dẫn quấn ống dây",
          "Màu sắc lớp sơn phủ cách điện",
          "Độ dày của đế đỡ"
        ],
        "correct": 0,
        "explanation": "Chiều đường sức từ của ống dây phụ thuộc trực tiếp vào chiều dòng điện qua các vòng dây."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Một nam châm điện đang được cấp điện có thể hút được vật liệu nào sau đây?",
        "options": [
          "Mảnh sắt phế liệu và bu-lông thép",
          "Mẩu gỗ vụn khô",
          "Cốc nhựa dùng một lần",
          "Mẩu gạch ngói vỡ"
        ],
        "correct": 0,
        "explanation": "Nam châm hút các vật liệu từ như sắt, thép."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tại sao người ta không dùng bạc nguyên chất để chế tạo lõi nam châm điện?",
        "options": [
          "Vì bạc là chất không có tính sắt từ, không bị nhiễm từ để làm tăng từ trường",
          "Vì bạc quá nhẹ",
          "Vì bạc không dẫn điện",
          "Vì bạc có màu trắng"
        ],
        "correct": 0,
        "explanation": "Bạc không phải chất sắt từ nên không khuếch đại được từ trường."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Dụng cụ hoặc thiết bị nào dưới đây biến năng lượng điện thành chuyển động quay cơ học nhờ lực từ?",
        "options": [
          "Động cơ điện mini",
          "Bếp nướng điện",
          "Nồi cơm điện gia đình",
          "Bàn là khô"
        ],
        "correct": 0,
        "explanation": "Động cơ điện biến điện năng thành cơ năng nhờ lực từ tác dụng lên cuộn dây mang dòng điện."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Trong thí nghiệm tạo từ phổ bằng mạt sắt, hành động dùng ngón tay gõ nhẹ vào tấm bìa nhằm mục đích gì?",
        "options": [
          "Làm giảm ma sát nghỉ giúp các mạt sắt dễ dàng xoay và sắp xếp theo các đường sức từ",
          "Làm nóng các hạt mạt sắt",
          "Làm nam châm nhiễm điện tĩnh",
          "Để các hạt mạt sắt dính chặt vào bìa"
        ],
        "correct": 0,
        "explanation": "Gõ nhẹ giúp giảm ma sát để mạt sắt sắp xếp trật tự theo đường sức từ."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Để phân biệt cực Bắc và cực Nam của một thanh nam châm lạ không được sơn màu hay đánh dấu, phương pháp chuẩn xác nhất là:",
        "options": [
          "Treo thanh nam châm bằng sợi chỉ mảnh ở giữa để thanh tự do định hướng Bắc - Nam địa lí",
          "Cân khối lượng hai đầu xem đầu nào nặng hơn",
          "Nhúng thanh vào chậu nước xem đầu nào nổi",
          "Đo nhiệt độ hai đầu"
        ],
        "correct": 0,
        "explanation": "Đầu thanh nam châm tự do quay về hướng Bắc địa lí chính là cực Bắc của nam châm."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nam châm điện dạng hình chữ U có ưu điểm vượt trội hơn nam châm thẳng ở điểm nào?",
        "options": [
          "Cả hai cực Bắc và Nam cùng hướng về một phía tiếp xúc hút vật, tăng gấp đôi lực giữ cơ học",
          "Tiêu tốn ít điện năng hơn 100 lần",
          "Không cần dùng dây dẫn điện",
          "Nhẹ hơn nam châm thẳng"
        ],
        "correct": 0,
        "explanation": "Hai cực cùng tiếp xúc giúp tăng lực giữ tiếp xúc lên vật gấp nhiều lần."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi chùm hạt điện tích từ gió Mặt Trời bay đến Trái Đất, lực từ của từ trường Trái Đất tác dụng làm chúng:",
        "options": [
          "Bị lệch quỹ đạo và bị cuốn xoắn ốc về hai vùng cực tạo nên cực quang",
          "Bị phản xạ ngược lại Mặt Trời",
          "Rơi thẳng xuống đường xích đạo",
          "Tăng tốc độ bay xuyên thủng lòng đất"
        ],
        "correct": 0,
        "explanation": "Lực Lorentz của từ trường Trái Đất bẻ cong quỹ đạo hạt tích điện cuốn về hai cực sinh ra hiện tượng cực quang."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Vật thể nào sau đây hoàn toàn KHÔNG BỊ ảnh hưởng bởi từ trường của một nam châm đặt ngay sát bên cạnh nó?",
        "options": [
          "Một viên bi ve bằng thủy tinh trong suốt",
          "Một chiếc đinh sắt nhỏ",
          "Một chiếc kim khâu bằng thép",
          "Một chiếc kẹp tài liệu bằng niken"
        ],
        "correct": 0,
        "explanation": "Thủy tinh không có tính sắt từ nên hoàn toàn không bị ảnh hưởng bởi từ trường."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về phương pháp xác định cực từ và sự phân bố từ trường của nam châm:",
        "statements": [
          {
            "subId": "a",
            "text": "Có thể dùng một kim la bàn đã biết rõ cực Bắc để xác định cực của một thanh nam châm lạ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cực Bắc của kim la bàn bị đẩy bởi cực Bắc của thanh nam châm lạ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Từ trường xung quanh nam châm có thể nhìn thấy trực tiếp bằng mắt thường mà không cần mạt sắt hay la bàn.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Đường sức từ càng dày đặc thì từ trường tại đó càng mạnh.",
            "correct": true
          }
        ],
        "explanation": "Từ trường là môi trường vô hình, không thể nhìn thấy trực tiếp bằng mắt thường nếu không dùng dụng cụ thử."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về ảnh hưởng của nhiệt độ cao đến tính chất từ của nam châm vĩnh cửu:",
        "statements": [
          {
            "subId": "a",
            "text": "Khi bị nung nóng đến nhiệt độ rất cao (nhiệt độ Curie), nam châm vĩnh cửu sẽ bị mất hết từ tính.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đối với sắt và thép, nhiệt độ mất từ tính hoàn toàn (nhiệt độ Curie) vào khoảng trên 700 độ C.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi gõ đập mạnh nhiều lần bằng búa kim loại, nam châm cũng có thể bị suy giảm từ tính.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nung nóng nam châm trong lò lửa đỏ rực sẽ làm nam châm hút sắt mạnh gấp mười lần.",
            "correct": false
          }
        ],
        "explanation": "Nung nóng làm các nguyên tử dao động nhiệt hỗn loạn, phá vỡ trật tự từ tính làm nam châm mất từ tính."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về ứng dụng của từ trường Trái Đất trong định vị và dẫn đường hàng hải:",
        "statements": [
          {
            "subId": "a",
            "text": "La bàn từ là dụng cụ dẫn đường không thể thiếu của thủy thủ từ hàng nghìn năm nay.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi đi tàu ngầm sâu dưới đại dương, sóng GPS vệ tinh không truyền tới được nên định vị bằng la bàn từ và con quay quán tính đóng vai trò sống còn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trên các bản đồ hàng hải quân sự luôn có ghi chú độ lệch từ thiên để thuyền trưởng hiệu chỉnh phương vị chuẩn xác.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "La bàn từ chỉ hoạt động được khi tàu thuyền được làm hoàn toàn bằng sắt nguyên khối.",
            "correct": false
          }
        ],
        "explanation": "Thân tàu bằng sắt quá nhiều thậm chí còn làm lệch kim la bàn, phải đặt các khối cầu bù từ chuyên dụng."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Về sự biến đổi và chuyển hóa năng lượng trong thiết bị dùng nam châm điện:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong chuông điện, điện năng được chuyển hóa một phần thành cơ năng gõ búa và thành năng lượng âm thanh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong rơ le điện từ, năng lượng điện của cuộn dây chuyển hóa thành cơ năng hút lẫy tiếp điểm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trong động cơ điện, điện năng được chuyển hóa thành cơ năng chuyển động quay.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hiệu suất chuyển hóa năng lượng của nam châm điện luôn đạt 100%, hoàn toàn không có tỏa nhiệt hao phí.",
            "correct": false
          }
        ],
        "explanation": "Dây quấn có điện trở nên luôn có tỏa nhiệt hao phí theo định luật Joule - Lenz."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một thanh thép sau khi từ hóa trở thành một thanh nam châm có 2 cực. Nếu người ta cưa thanh thép này thành 5 đoạn ngắn bằng nhau thì tổng số cực từ của 5 đoạn nam châm mới là bao nhiêu cực?",
        "correctAnswer": "10",
        "explanation": "Mỗi đoạn nam châm mới có 2 cực từ (1 Bắc, 1 Nam). Do đó 5 đoạn có tổng cộng: 5 x 2 = 10 cực."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một cuộn dây nam châm điện quấn 60 vòng hút được 9 viên bi thép nhỏ. Nếu muốn cuộn dây hút được 27 viên bi thép với cùng nguồn điện và điều kiện thí nghiệm thì cuộn dây cần có bao nhiêu vòng quấn?",
        "correctAnswer": "180",
        "explanation": "Số bi thép tăng gấp 3 lần (27 / 9 = 3) nên số vòng quấn cần tăng gấp 3 lần: 60 x 3 = 180 vòng."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một chiếc la bàn hàng hải có vòng chia độ 360 độ quanh mặt số. Khi một con tàu chuyển hướng di chuyển từ hướng chính Bắc (0 độ) sang hướng chính Đông, kim la bàn đã quay một góc bao nhiêu độ?",
        "correctAnswer": "90",
        "explanation": "Góc quay từ hướng Bắc sang hướng Đông là góc vuông: 90 độ."
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Một chiếc cần cẩu nam châm điện tại bến cảng nhấc bổng một chiếc bồn chứa phế liệu thép có khối lượng 3,6 tấn. Khối lượng bồn phế liệu này quy đổi ra đơn vị kilôgam (kg) là bao nhiêu?",
        "correctAnswer": "3600",
        "explanation": "3,6 tấn = 3,6 x 1000 = 3600 kg."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Trong 6 chất sau đây: (1) Sắt; (2) Nhôm; (3) Coban; (4) Thủy tinh; (5) Niken; (6) Cao su tự nhiên. Hỏi có bao nhiêu chất là chất sắt từ bị nam châm hút mạnh?",
        "correctAnswer": "3",
        "explanation": "Có 3 chất sắt từ là: (1) sắt, (3) coban, (5) niken."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Trong mạch điện điều khiển nam châm điện, ampe kế đo được dòng điện tăng từ 0,2 A lên 0,8 A khi người thực hành gạt con chạy của biến trở. Hỏi cường độ dòng điện qua nam châm điện đã tăng thêm bao nhiêu ampe (A)?",
        "correctAnswer": "0,6",
        "explanation": "Cường độ tăng thêm = 0,8 - 0,2 = 0,6 A."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Thí nghiệm nhiệt độ Curie: Một thanh nam châm thép vĩnh cửu hút chặt một chiếc đinh sắt treo bằng sợi chỉ mảnh. Dùng ngọn lửa đèn khò đốt thanh nam châm đến khi thanh phát sáng đỏ rực (khoảng 780 độ C), chiếc đinh sắt bỗng nhiên rơi tuột xuống đất. Giải thích nguyên nhân vật lý cốt lõi của hiện tượng này:",
        "options": [
          "Nhiệt độ cao kích thích dao động nhiệt hỗn loạn của các phân tử, phá vỡ trật tự từ tính định hướng nội tại làm thanh thép mất hoàn toàn từ tính",
          "Nhiệt độ cao làm bay hơi toàn bộ chiếc đinh sắt",
          "Ngọn lửa đèn khò sinh ra gió đẩy chiếc đinh rơi xuống",
          "Sợi chỉ treo bị đứt do nhiệt"
        ],
        "correct": 0,
        "explanation": "Ở nhiệt độ trên điểm Curie (770 độ C với sắt thép), dao động nhiệt phá hủy trật tự định hướng của các mômen từ làm vật liệu mất từ tính hoàn toàn."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một cần cẩu nam châm điện nâng thẳng đứng một khối phế liệu thép nặng 2 tấn lên cao 5 mét với vận tốc đều trong thời gian 10 giây. Lấy gia tốc trọng trường g = 10 m/s2. Công cơ học tối thiểu mà lực hút của nam châm điện đã thực hiện để nâng khối thép này lên là bao nhiêu kilôjun (kJ)?",
        "options": [
          "100 kJ",
          "50 kJ",
          "200 kJ",
          "20 kJ"
        ],
        "correct": 0,
        "explanation": "Trọng lượng P = 2000 kg x 10 = 20 000 N. Công nâng A = P x h = 20 000 N x 5 m = 100 000 J = 100 kJ."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nguyên lí lưu trữ dữ liệu bằng từ tính: Bề mặt đĩa cứng máy tính (HDD) được phủ một lớp màng từ tính siêu mỏng gồm hàng tỉ ô từ cực nhỏ. Đầu đọc/ghi là một nam châm điện vi mô. Khi ghi dữ liệu nhị phân '0' và '1', đầu ghi thực hiện thao tác nào sau đây?",
        "options": [
          "Đổi chiều dòng điện qua cuộn vi mô để định hướng chiều từ hóa ngược nhau cho từng ô từ tương ứng với bit 0 hoặc bit 1",
          "Dùng tia laser đốt cháy các ô từ",
          "Dùng mực in nano đánh dấu màu sắc",
          "Dùng điện cao áp đục lỗ trên bề mặt đĩa"
        ],
        "correct": 0,
        "explanation": "Đổi chiều dòng điện trong nam châm điện đầu ghi làm đổi chiều từ hóa của ô từ biểu diễn bit 0 và bit 1."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Ảnh hưởng của bão từ lên các đường ống dẫn dầu bằng kim loại xuyên lục địa: Khi xảy ra bão từ cực mạnh, từ trường biến thiên xuyên qua mặt đất cảm ứng sinh ra dòng điện chạy dọc thân đường ống thép dài hàng nghìn kilômét. Dòng điện cảm ứng này gây ra nguy cơ nghiêm trọng nào cho đường ống?",
        "options": [
          "Tăng tốc độ ăn mòn điện hóa kim loại làm thủng đường ống gây rò rỉ dầu thô ra môi trường",
          "Làm đông cứng dầu thô bên trong đường ống",
          "Làm đường ống biến thành vàng nguyên chất",
          "Làm đường ống bay lơ lửng lên không trung"
        ],
        "correct": 0,
        "explanation": "Dòng điện cảm ứng biến thiên chạy trong ống kim loại chôn dưới đất thúc đẩy mạnh phản ứng ăn mòn điện hóa gây rò rỉ thủng ống."
      }
    ]
  }
}

def build_phys7_exams():
    return PHYS7_EXAMS
