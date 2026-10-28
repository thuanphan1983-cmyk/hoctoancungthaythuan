// ==============================================================================
// NGÂN HÀNG ĐỀ KIỂM TRA CHƯƠNG VII: TẦN SỐ VÀ TẦN SỐ TƯƠNG ĐỐI - TOÁN 9 (KNTT)
// Chuẩn ma trận khảo thí 2025: Đề 1 & 2 (Khá 40/30/20/10), Đề 3 (Khá Giỏi 20/30/30/20)
// Cập nhật lúc: 2026-10-28 08:29:30
// ==============================================================================

const EXAMS_9_C7_9 = {
  "c7_9_bai1_test1": {
    "title": "Toán 9 (KNTT) - Bài 22: Bảng tần số và biểu đồ tần số - Đề số 1 (🌿 Mức độ Khá (Đề 1))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai1_test2": {
    "title": "Toán 9 (KNTT) - Bài 22: Bảng tần số và biểu đồ tần số - Đề số 2 (🌿 Mức độ Khá (Đề 2))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai1_test3": {
    "title": "Toán 9 (KNTT) - Bài 22: Bảng tần số và biểu đồ tần số - Đề số 3 (🚀 Mức độ Khá Giỏi)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai2_test1": {
    "title": "Toán 9 (KNTT) - Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối - Đề số 1 (🌿 Mức độ Khá (Đề 1))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai2_test2": {
    "title": "Toán 9 (KNTT) - Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối - Đề số 2 (🌿 Mức độ Khá (Đề 2))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai2_test3": {
    "title": "Toán 9 (KNTT) - Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối - Đề số 3 (🚀 Mức độ Khá Giỏi)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai3_test1": {
    "title": "Toán 9 (KNTT) - Bài 24: Bảng tần số ghép nhóm và biểu đồ - Đề số 1 (🌿 Mức độ Khá (Đề 1))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai3_test2": {
    "title": "Toán 9 (KNTT) - Bài 24: Bảng tần số ghép nhóm và biểu đồ - Đề số 2 (🌿 Mức độ Khá (Đề 2))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai3_test3": {
    "title": "Toán 9 (KNTT) - Bài 24: Bảng tần số ghép nhóm và biểu đồ - Đề số 3 (🚀 Mức độ Khá Giỏi)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai4_test1": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số 1 (🌿 Mức độ Khá (Đề 1))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai4_test2": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số 2 (🌿 Mức độ Khá (Đề 2))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  },
  "c7_9_bai4_test3": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số 3 (🚀 Mức độ Khá Giỏi)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Số lần xuất hiện của một giá trị trong tập dữ liệu gọi là:",
        "options": [
          "Tần số của giá trị đó",
          "Tần số tương đối",
          "Mốt",
          "Trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tỉ số giữa tần số của một giá trị và kích thước mẫu $N$ gọi là:",
        "options": [
          "Tần số tương đối của giá trị đó",
          "Tần số tuyệt đối",
          "Tỉ số truyền",
          "Phương sai"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong một mẫu dữ liệu luôn bằng:",
        "options": [
          "$100\\%$ (hoặc $1$)",
          "$50\\%$",
          "$0\\%$",
          "$200\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ nào thường dùng để biểu diễn tần số tương đối?",
        "options": [
          "Biểu đồ hình quạt tròn hoặc biểu đồ cột",
          "Biểu đồ đường chéo",
          "Biểu đồ hình nón",
          "Biểu đồ hàm số"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Trong bảng ghép nhóm $[a; b)$, giá trị đại diện của nhóm là:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$b - a$",
          "$a$",
          "$b$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Độ rộng của nhóm $[10; 20)$ là:",
        "options": [
          "$10$",
          "$20$",
          "$15$",
          "$30$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Mẫu số liệu có kích thước $N = 50$, giá trị $x = 8$ có tần số $m = 15$. Tần số tương đối của $x = 8$ là:",
        "options": [
          "$30\\%$",
          "$15\\%$",
          "$50\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hình quạt tròn có góc ở tâm tương ứng với tần số tương đối $25\\%$ là:",
        "options": [
          "$90^\\circ$",
          "$45^\\circ$",
          "$180^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Góc ở tâm tương ứng với tần số tương đối $f = 40\\%$ trong biểu đồ quạt tròn là:",
        "options": [
          "$144^\\circ$",
          "$40^\\circ$",
          "$100^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian tự học của 100 học sinh: nhóm $[2; 4)$ giờ có 35 bạn. Tần số tương đối của nhóm này là:",
        "options": [
          "$35\\%$",
          "$20\\%$",
          "$40\\%$",
          "$70\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một bảng tần số có 4 giá trị với các tần số tương đối là $20\\%, 35\\%, 25\\%$ và $f_4$. Giá trị $f_4$ bằng:",
        "options": [
          "$20\\%$",
          "$15\\%$",
          "$10\\%$",
          "$25\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Điều tra điểm kiểm tra của 40 học sinh: điểm 8 có tần số tương đối là $25\\%$. Số học sinh đạt điểm 8 là:",
        "options": [
          "$10$ học sinh",
          "$8$ học sinh",
          "$12$ học sinh",
          "$15$ học sinh"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Một lớp học có 40 học sinh được xếp loại học lực: Giỏi: 10 bạn; Khá: 18 bạn; Đạt: 10 bạn; Chưa đạt: 2 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng tần số của các nhóm bằng kích thước mẫu N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Giỏi là 10/40 = 25%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của học sinh Khá là 45%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm tương ứng với nhóm học sinh Chưa đạt trên biểu đồ quạt tròn là 18°.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng ghép nhóm thời gian làm bài kiểm tra (phút) của 50 học sinh: [10; 15): 8 bạn; [15; 20): 20 bạn; [20; 25): 16 bạn; [25; 30): 6 bạn:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Mỗi nhóm ghép đều có độ rộng bằng 5 phút.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị đại diện của nhóm [15; 20) là 17,5 phút.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối của nhóm [15; 20) chiếm 40%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tần số tương đối của các học sinh hoàn thành bài từ 20 phút trở lên là 44%.",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một mẫu số liệu có $N = 80$. Giá trị $x_1$ có tần số $m_1 = 20$. Tính tần số tương đối của $x_1$ theo đơn vị phần trăm (%):",
        "answer": "25%",
        "acceptableAnswers": [
          "25%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25%**."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tính giá trị đại diện của nhóm số liệu $[20; 30)$:",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong biểu đồ hình quạt tròn, một hình quạt có góc ở tâm bằng $72^\\circ$. Tần số tương đối tương ứng là bao nhiêu phần trăm (%):",
        "answer": "20%",
        "acceptableAnswers": [
          "20%"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **20%**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một trường có 500 học sinh. Khảo sát thấy tỉ lệ cận thị là $32\\%$. Số học sinh bị cận thị của trường là bao nhiêu em?",
        "answer": "160",
        "acceptableAnswers": [
          "160"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **160**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Bảng thống kê số điểm kiểm tra 1 tiết của lớp 9A: Điểm 6: 6 bạn; Điểm 7: 12 bạn; Điểm 8: 14 bạn; Điểm 9: 6 bạn; Điểm 10: 2 bạn. a) Lập bảng tần số tương đối; b) Tính số phần trăm học sinh đạt điểm khá - giỏi (từ điểm 7 trở lên).",
        "rubric": "a) Tổng số HS: 40 bạn. Tần số tương đối: Điểm 6: 15%; Điểm 7: 30%; Điểm 8: 35%; Điểm 9: 15%; Điểm 10: 5% (0.5đ). b) Số HS đạt điểm từ 7 trở lên: 12 + 14 + 6 + 2 = 34 bạn. Tỉ lệ: (34/40)*100% = 85% (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Vẽ biểu đồ tần số tương đối dạng hình quạt tròn hoặc nêu cách tính góc ở tâm cho mẫu dữ liệu có tỉ lệ: Loại A: $40\\%$; Loại B: $35\\%$; Loại C: $25\\%$.",
        "rubric": "Công thức tính góc ở tâm: α = f * 360° (0.25đ). Loại A: 40% * 360° = 144° (0.25đ). Loại B: 35% * 360° = 126° (0.25đ). Loại C: 25% * 360° = 90° (0.25đ). Tổng các góc: 144° + 126° + 90° = 360°."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bảng ghép nhóm cự ly chạy 100m của 40 học sinh được phân vào 4 nhóm: [12; 13): a bạn; [13; 14): 18 bạn; [14; 15): 10 bạn; [15; 16): 4 bạn. Tìm a và tính thời gian chạy trung bình của học sinh lớp 9 này bằng cách sử dụng giá trị đại diện của các nhóm.",
        "rubric": "Tổng số HS là 40 nên a = 40 - 18 - 10 - 4 = 8 bạn (0.25đ). Giá trị đại diện các nhóm: 12.5; 13.5; 14.5; 15.5 (0.25đ). Thời gian trung bình: X = (8*12.5 + 18*13.5 + 10*14.5 + 4*15.5) / 40 = (100 + 243 + 145 + 62) / 40 = 550 / 40 = 13.75 giây (0.5đ)."
      }
    ]
  }
};

if (typeof window !== 'undefined') {
  window.EXAMS_9_C7_9 = EXAMS_9_C7_9;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { EXAMS_9_C7_9 };
}
