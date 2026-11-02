// ==============================================================================
// NGÂN HÀNG ĐỀ KIỂM TRA CHƯƠNG VII: TẦN SỐ VÀ TẦN SỐ TƯƠNG ĐỐI - TOÁN 9 (KNTT)
// Chuẩn ma trận khảo thí 2025: Đề 1 & 2 (Khá 40/30/20/10), Đề 3 (Khá Giỏi 20/30/30/20)
// Cập nhật lúc: 2026-11-02 06:43:13
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
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số 01",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tần số của một giá trị trong mẫu số liệu là:",
        "options": [
          "Số lần xuất hiện của giá trị đó trong mẫu",
          "Tỉ số phần trăm của giá trị đó",
          "Giá trị lớn nhất của mẫu",
          "Số trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tần số tương đối $f_i$ của giá trị $x_i$ có tần số $m_i$ trong mẫu kích thước $N$ là:",
        "options": [
          "$f_i = \\frac{m_i}{N} \\cdot 100\\%$",
          "$f_i = \\frac{N}{m_i} \\cdot 100\\%$",
          "$f_i = m_i \\cdot N$",
          "$f_i = m_i + N$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong mẫu số liệu luôn bằng:",
        "options": [
          "$100\\%$",
          "$50\\%$",
          "$10\\%$",
          "$1\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ hình quạt tròn thường được dùng để biểu diễn:",
        "options": [
          "Cơ cấu tỉ lệ phần trăm các thành phần",
          "Sự thay đổi số liệu theo thời gian",
          "Tần số tuyệt đối của từng giá trị",
          "Giá trị lớn nhất và nhỏ nhất"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về thời gian tự học mỗi ngày của 40 học sinh lớp 9A. Có 4 người chọn mức 1. Tần số tương đối của nhóm này là:",
        "options": [
          "$10.0\\%$",
          "$0.1\\%$",
          "$4\\%$",
          "$40\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bảng tần số ghép nhóm thường dùng khi dữ liệu thống kê:",
        "options": [
          "Có quy mô lớn hoặc là biến liên tục",
          "Chỉ có từ 2 đến 3 giá trị",
          "Là dữ liệu định tính không đo lường được",
          "Có tần số bằng nhau"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong bảng phân bố tần số ghép nhóm $[20; 30)$, giá trị đại diện của nhóm này là:",
        "options": [
          "$25$",
          "$20$",
          "$30$",
          "$50$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho mẫu số liệu có tổng tần số $N = 40$. Nhóm có tần số tương đối $20\\%$ thì tần số của nhóm đó là:",
        "options": [
          "$8$",
          "$4$",
          "$40$",
          "$20$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Khảo sát điểm kiểm tra của 40 học sinh. Số học sinh đạt điểm Giỏi (từ 8 đến 10) là 16. Tần số tương đối của học sinh đạt điểm Giỏi là:",
        "options": [
          "$40\\%$",
          "$30\\%$",
          "$50\\%$",
          "$20\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trên biểu đồ hình quạt tròn thể hiện kết quả điều tra, một hình quạt tròn có góc ở tâm bằng $82^\\circ$. Tần số tương đối tương ứng của nhóm này là:",
        "options": [
          "$22.8\\%$",
          "$20\\%$",
          "$25\\%$",
          "$30\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Điều tra mức lương của 100 công nhân. Nhóm lương từ 8 đến 10 triệu đồng chiếm $35\\%$, nhóm từ 10 đến 12 triệu chiếm $40\\%$. Số công nhân có mức lương từ 8 đến 12 triệu đồng là:",
        "options": [
          "$75$ công nhân",
          "$35$ công nhân",
          "$40$ công nhân",
          "$25$ công nhân"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Nếu tăng gấp đôi tất cả các tần số của một mẫu số liệu thì tần số tương đối của từng giá trị sẽ:",
        "options": [
          "Không đổi",
          "Tăng gấp đôi",
          "Giảm đi một nửa",
          "Tăng thêm 100%"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về tần số và tần số tương đối (Đề 01):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng các tần số của tất cả các giá trị bằng quy mô mẫu N.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng các tần số tương đối bằng 100%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối fi luôn là số không âm và không vượt quá 100%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Biểu đồ đoạn thẳng không thể dùng để biểu diễn tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng khảo sát thời gian tự học mỗi ngày của 40 học sinh lớp 9A gồm 40 đối tượng điều tra:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Kích thước mẫu số liệu là N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Mỗi giá trị có tần số mi tương ứng với số đối tượng đạt giá trị đó.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối cho biết tỉ lệ phần trăm của từng nhóm trong toàn bộ mẫu.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm trên biểu đồ quạt tròn tỉ lệ nghịch với tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một lớp có 40 học sinh, trong đó có 10 bạn giỏi Toán. Tính tần số tương đối (%) của học sinh giỏi Toán.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Trên biểu đồ quạt tròn, nhóm A chiếm góc 90 độ ở tâm. Tính tần số tương đối (%) của nhóm A.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát 200 khách hàng mua sắm tại siêu thị, có 70 người thanh toán bằng mã QR. Tính tần số tương đối (%) thanh toán bằng QR.",
        "answer": "35",
        "acceptableAnswers": [
          "35"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **35**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong bảng phân bố tần số ghép nhóm có nhóm [10; 20) với tần số 30 và tổng cỡ mẫu là 120. Tính tần số tương đối (%) của nhóm này.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về số con trong 30 gia đình tại một thôn cho kết quả: 1 con: 6 gia đình; 2 con: 18 gia đình; 3 con: 6 gia đình. Hãy lập bảng tần số tương đối.",
        "rubric": "Cỡ mẫu N = 30 (0.25đ).\nTần số tương đối gia đình 1 con: f1 = 6/30 . 100% = 20% (0.25đ).\nTần số tương đối gia đình 2 con: f2 = 18/30 . 100% = 60% (0.25đ).\nTần số tương đối gia đình 3 con: f3 = 6/30 . 100% = 20% (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian xem tivi mỗi ngày của 50 học sinh: Dưới 1 giờ: 15 bạn; Từ 1 đến 2 giờ: 25 bạn; Trên 2 giờ: 10 bạn. Hãy tính số đo cung hình quạt tròn tương ứng với từng nhóm để vẽ biểu đồ quạt tròn.",
        "rubric": "Nhóm dưới 1 giờ: tỉ lệ 15/50 = 30% => Góc ở tâm = 30% . 360 độ = 108 độ (0.25đ).\nNhóm từ 1 đến 2 giờ: tỉ lệ 25/50 = 50% => Góc ở tâm = 50% . 360 độ = 180 độ (0.25đ).\nNhóm trên 2 giờ: tỉ lệ 10/50 = 20% => Góc ở tâm = 20% . 360 độ = 72 độ (0.25đ).\nTổng số đo các góc = 108 + 180 + 72 = 360 độ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một trạm khí tượng đo lượng mưa trong 30 ngày của tháng 7. Biết lượng mưa trung bình là 15 mm/ngày. Nếu bỏ đi 2 ngày có lượng mưa đột biến là 45 mm và 55 mm thì lượng mưa trung bình của 28 ngày còn lại là bao nhiêu?",
        "rubric": "Tổng lượng mưa trong 30 ngày là: 30 . 15 = 450 (mm) (0.25đ).\nTổng lượng mưa của 2 ngày đột biến là: 45 + 55 = 100 (mm) (0.25đ).\nTổng lượng mưa của 28 ngày còn lại là: 450 - 100 = 350 (mm) (0.25đ).\nLượng mưa trung bình của 28 ngày còn lại là: 350 / 28 = 12,5 (mm/ngày) (0.25đ)."
      }
    ]
  },
  "c7_9_bai4_test2": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số 02",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tần số của một giá trị trong mẫu số liệu là:",
        "options": [
          "Số lần xuất hiện của giá trị đó trong mẫu",
          "Tỉ số phần trăm của giá trị đó",
          "Giá trị lớn nhất của mẫu",
          "Số trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tần số tương đối $f_i$ của giá trị $x_i$ có tần số $m_i$ trong mẫu kích thước $N$ là:",
        "options": [
          "$f_i = \\frac{m_i}{N} \\cdot 100\\%$",
          "$f_i = \\frac{N}{m_i} \\cdot 100\\%$",
          "$f_i = m_i \\cdot N$",
          "$f_i = m_i + N$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong mẫu số liệu luôn bằng:",
        "options": [
          "$100\\%$",
          "$50\\%$",
          "$10\\%$",
          "$1\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ hình quạt tròn thường được dùng để biểu diễn:",
        "options": [
          "Cơ cấu tỉ lệ phần trăm các thành phần",
          "Sự thay đổi số liệu theo thời gian",
          "Tần số tuyệt đối của từng giá trị",
          "Giá trị lớn nhất và nhỏ nhất"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về điểm kiểm tra giữa kỳ môn Toán của 45 học sinh. Có 8 người chọn mức 1. Tần số tương đối của nhóm này là:",
        "options": [
          "$17.8\\%$",
          "$0.2\\%$",
          "$8\\%$",
          "$45\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bảng tần số ghép nhóm thường dùng khi dữ liệu thống kê:",
        "options": [
          "Có quy mô lớn hoặc là biến liên tục",
          "Chỉ có từ 2 đến 3 giá trị",
          "Là dữ liệu định tính không đo lường được",
          "Có tần số bằng nhau"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong bảng phân bố tần số ghép nhóm $[20; 30)$, giá trị đại diện của nhóm này là:",
        "options": [
          "$25$",
          "$20$",
          "$30$",
          "$50$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho mẫu số liệu có tổng tần số $N = 45$. Nhóm có tần số tương đối $20\\%$ thì tần số của nhóm đó là:",
        "options": [
          "$9$",
          "$4$",
          "$45$",
          "$20$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Khảo sát điểm kiểm tra của 45 học sinh. Số học sinh đạt điểm Giỏi (từ 8 đến 10) là 18. Tần số tương đối của học sinh đạt điểm Giỏi là:",
        "options": [
          "$40\\%$",
          "$30\\%$",
          "$50\\%$",
          "$20\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trên biểu đồ hình quạt tròn thể hiện kết quả điều tra, một hình quạt tròn có góc ở tâm bằng $92^\\circ$. Tần số tương đối tương ứng của nhóm này là:",
        "options": [
          "$25.6\\%$",
          "$20\\%$",
          "$25\\%$",
          "$30\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Điều tra mức lương của 100 công nhân. Nhóm lương từ 8 đến 10 triệu đồng chiếm $35\\%$, nhóm từ 10 đến 12 triệu chiếm $40\\%$. Số công nhân có mức lương từ 8 đến 12 triệu đồng là:",
        "options": [
          "$75$ công nhân",
          "$35$ công nhân",
          "$40$ công nhân",
          "$25$ công nhân"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Nếu tăng gấp đôi tất cả các tần số của một mẫu số liệu thì tần số tương đối của từng giá trị sẽ:",
        "options": [
          "Không đổi",
          "Tăng gấp đôi",
          "Giảm đi một nửa",
          "Tăng thêm 100%"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về tần số và tần số tương đối (Đề 02):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng các tần số của tất cả các giá trị bằng quy mô mẫu N.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng các tần số tương đối bằng 100%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối fi luôn là số không âm và không vượt quá 100%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Biểu đồ đoạn thẳng không thể dùng để biểu diễn tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng khảo sát điểm kiểm tra giữa kỳ môn Toán của 45 học sinh gồm 45 đối tượng điều tra:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Kích thước mẫu số liệu là N = 45.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Mỗi giá trị có tần số mi tương ứng với số đối tượng đạt giá trị đó.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối cho biết tỉ lệ phần trăm của từng nhóm trong toàn bộ mẫu.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm trên biểu đồ quạt tròn tỉ lệ nghịch với tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một lớp có 40 học sinh, trong đó có 10 bạn giỏi Toán. Tính tần số tương đối (%) của học sinh giỏi Toán.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Trên biểu đồ quạt tròn, nhóm A chiếm góc 90 độ ở tâm. Tính tần số tương đối (%) của nhóm A.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát 200 khách hàng mua sắm tại siêu thị, có 70 người thanh toán bằng mã QR. Tính tần số tương đối (%) thanh toán bằng QR.",
        "answer": "35",
        "acceptableAnswers": [
          "35"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **35**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong bảng phân bố tần số ghép nhóm có nhóm [10; 20) với tần số 30 và tổng cỡ mẫu là 120. Tính tần số tương đối (%) của nhóm này.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về số con trong 30 gia đình tại một thôn cho kết quả: 1 con: 6 gia đình; 2 con: 18 gia đình; 3 con: 6 gia đình. Hãy lập bảng tần số tương đối.",
        "rubric": "Cỡ mẫu N = 30 (0.25đ).\nTần số tương đối gia đình 1 con: f1 = 6/30 . 100% = 20% (0.25đ).\nTần số tương đối gia đình 2 con: f2 = 18/30 . 100% = 60% (0.25đ).\nTần số tương đối gia đình 3 con: f3 = 6/30 . 100% = 20% (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian xem tivi mỗi ngày của 50 học sinh: Dưới 1 giờ: 15 bạn; Từ 1 đến 2 giờ: 25 bạn; Trên 2 giờ: 10 bạn. Hãy tính số đo cung hình quạt tròn tương ứng với từng nhóm để vẽ biểu đồ quạt tròn.",
        "rubric": "Nhóm dưới 1 giờ: tỉ lệ 15/50 = 30% => Góc ở tâm = 30% . 360 độ = 108 độ (0.25đ).\nNhóm từ 1 đến 2 giờ: tỉ lệ 25/50 = 50% => Góc ở tâm = 50% . 360 độ = 180 độ (0.25đ).\nNhóm trên 2 giờ: tỉ lệ 10/50 = 20% => Góc ở tâm = 20% . 360 độ = 72 độ (0.25đ).\nTổng số đo các góc = 108 + 180 + 72 = 360 độ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một trạm khí tượng đo lượng mưa trong 30 ngày của tháng 7. Biết lượng mưa trung bình là 15 mm/ngày. Nếu bỏ đi 2 ngày có lượng mưa đột biến là 45 mm và 55 mm thì lượng mưa trung bình của 28 ngày còn lại là bao nhiêu?",
        "rubric": "Tổng lượng mưa trong 30 ngày là: 30 . 15 = 450 (mm) (0.25đ).\nTổng lượng mưa của 2 ngày đột biến là: 45 + 55 = 100 (mm) (0.25đ).\nTổng lượng mưa của 28 ngày còn lại là: 450 - 100 = 350 (mm) (0.25đ).\nLượng mưa trung bình của 28 ngày còn lại là: 350 / 28 = 12,5 (mm/ngày) (0.25đ)."
      }
    ]
  },
  "c7_9_bai4_test3": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số 03",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tần số của một giá trị trong mẫu số liệu là:",
        "options": [
          "Số lần xuất hiện của giá trị đó trong mẫu",
          "Tỉ số phần trăm của giá trị đó",
          "Giá trị lớn nhất của mẫu",
          "Số trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tần số tương đối $f_i$ của giá trị $x_i$ có tần số $m_i$ trong mẫu kích thước $N$ là:",
        "options": [
          "$f_i = \\frac{m_i}{N} \\cdot 100\\%$",
          "$f_i = \\frac{N}{m_i} \\cdot 100\\%$",
          "$f_i = m_i \\cdot N$",
          "$f_i = m_i + N$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong mẫu số liệu luôn bằng:",
        "options": [
          "$100\\%$",
          "$50\\%$",
          "$10\\%$",
          "$1\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ hình quạt tròn thường được dùng để biểu diễn:",
        "options": [
          "Cơ cấu tỉ lệ phần trăm các thành phần",
          "Sự thay đổi số liệu theo thời gian",
          "Tần số tuyệt đối của từng giá trị",
          "Giá trị lớn nhất và nhỏ nhất"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về chiều cao tính bằng cm của 50 cây giống bạch đàn. Có 12 người chọn mức 1. Tần số tương đối của nhóm này là:",
        "options": [
          "$24.0\\%$",
          "$0.2\\%$",
          "$12\\%$",
          "$50\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bảng tần số ghép nhóm thường dùng khi dữ liệu thống kê:",
        "options": [
          "Có quy mô lớn hoặc là biến liên tục",
          "Chỉ có từ 2 đến 3 giá trị",
          "Là dữ liệu định tính không đo lường được",
          "Có tần số bằng nhau"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong bảng phân bố tần số ghép nhóm $[20; 30)$, giá trị đại diện của nhóm này là:",
        "options": [
          "$25$",
          "$20$",
          "$30$",
          "$50$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho mẫu số liệu có tổng tần số $N = 50$. Nhóm có tần số tương đối $20\\%$ thì tần số của nhóm đó là:",
        "options": [
          "$10$",
          "$5$",
          "$50$",
          "$20$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Khảo sát điểm kiểm tra của 50 học sinh. Số học sinh đạt điểm Giỏi (từ 8 đến 10) là 20. Tần số tương đối của học sinh đạt điểm Giỏi là:",
        "options": [
          "$40\\%$",
          "$30\\%$",
          "$50\\%$",
          "$20\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trên biểu đồ hình quạt tròn thể hiện kết quả điều tra, một hình quạt tròn có góc ở tâm bằng $102^\\circ$. Tần số tương đối tương ứng của nhóm này là:",
        "options": [
          "$28.3\\%$",
          "$20\\%$",
          "$25\\%$",
          "$30\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Điều tra mức lương của 100 công nhân. Nhóm lương từ 8 đến 10 triệu đồng chiếm $35\\%$, nhóm từ 10 đến 12 triệu chiếm $40\\%$. Số công nhân có mức lương từ 8 đến 12 triệu đồng là:",
        "options": [
          "$75$ công nhân",
          "$35$ công nhân",
          "$40$ công nhân",
          "$25$ công nhân"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Nếu tăng gấp đôi tất cả các tần số của một mẫu số liệu thì tần số tương đối của từng giá trị sẽ:",
        "options": [
          "Không đổi",
          "Tăng gấp đôi",
          "Giảm đi một nửa",
          "Tăng thêm 100%"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về tần số và tần số tương đối (Đề 03):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng các tần số của tất cả các giá trị bằng quy mô mẫu N.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng các tần số tương đối bằng 100%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối fi luôn là số không âm và không vượt quá 100%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Biểu đồ đoạn thẳng không thể dùng để biểu diễn tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng khảo sát chiều cao tính bằng cm của 50 cây giống bạch đàn gồm 50 đối tượng điều tra:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Kích thước mẫu số liệu là N = 50.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Mỗi giá trị có tần số mi tương ứng với số đối tượng đạt giá trị đó.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối cho biết tỉ lệ phần trăm của từng nhóm trong toàn bộ mẫu.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm trên biểu đồ quạt tròn tỉ lệ nghịch với tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một lớp có 40 học sinh, trong đó có 10 bạn giỏi Toán. Tính tần số tương đối (%) của học sinh giỏi Toán.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Trên biểu đồ quạt tròn, nhóm A chiếm góc 90 độ ở tâm. Tính tần số tương đối (%) của nhóm A.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát 200 khách hàng mua sắm tại siêu thị, có 70 người thanh toán bằng mã QR. Tính tần số tương đối (%) thanh toán bằng QR.",
        "answer": "35",
        "acceptableAnswers": [
          "35"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **35**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong bảng phân bố tần số ghép nhóm có nhóm [10; 20) với tần số 30 và tổng cỡ mẫu là 120. Tính tần số tương đối (%) của nhóm này.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về số con trong 30 gia đình tại một thôn cho kết quả: 1 con: 6 gia đình; 2 con: 18 gia đình; 3 con: 6 gia đình. Hãy lập bảng tần số tương đối.",
        "rubric": "Cỡ mẫu N = 30 (0.25đ).\nTần số tương đối gia đình 1 con: f1 = 6/30 . 100% = 20% (0.25đ).\nTần số tương đối gia đình 2 con: f2 = 18/30 . 100% = 60% (0.25đ).\nTần số tương đối gia đình 3 con: f3 = 6/30 . 100% = 20% (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian xem tivi mỗi ngày của 50 học sinh: Dưới 1 giờ: 15 bạn; Từ 1 đến 2 giờ: 25 bạn; Trên 2 giờ: 10 bạn. Hãy tính số đo cung hình quạt tròn tương ứng với từng nhóm để vẽ biểu đồ quạt tròn.",
        "rubric": "Nhóm dưới 1 giờ: tỉ lệ 15/50 = 30% => Góc ở tâm = 30% . 360 độ = 108 độ (0.25đ).\nNhóm từ 1 đến 2 giờ: tỉ lệ 25/50 = 50% => Góc ở tâm = 50% . 360 độ = 180 độ (0.25đ).\nNhóm trên 2 giờ: tỉ lệ 10/50 = 20% => Góc ở tâm = 20% . 360 độ = 72 độ (0.25đ).\nTổng số đo các góc = 108 + 180 + 72 = 360 độ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một trạm khí tượng đo lượng mưa trong 30 ngày của tháng 7. Biết lượng mưa trung bình là 15 mm/ngày. Nếu bỏ đi 2 ngày có lượng mưa đột biến là 45 mm và 55 mm thì lượng mưa trung bình của 28 ngày còn lại là bao nhiêu?",
        "rubric": "Tổng lượng mưa trong 30 ngày là: 30 . 15 = 450 (mm) (0.25đ).\nTổng lượng mưa của 2 ngày đột biến là: 45 + 55 = 100 (mm) (0.25đ).\nTổng lượng mưa của 28 ngày còn lại là: 450 - 100 = 350 (mm) (0.25đ).\nLượng mưa trung bình của 28 ngày còn lại là: 350 / 28 = 12,5 (mm/ngày) (0.25đ)."
      }
    ]
  },
  "c7_9_bai4_test4": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số 04",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tần số của một giá trị trong mẫu số liệu là:",
        "options": [
          "Số lần xuất hiện của giá trị đó trong mẫu",
          "Tỉ số phần trăm của giá trị đó",
          "Giá trị lớn nhất của mẫu",
          "Số trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tần số tương đối $f_i$ của giá trị $x_i$ có tần số $m_i$ trong mẫu kích thước $N$ là:",
        "options": [
          "$f_i = \\frac{m_i}{N} \\cdot 100\\%$",
          "$f_i = \\frac{N}{m_i} \\cdot 100\\%$",
          "$f_i = m_i \\cdot N$",
          "$f_i = m_i + N$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong mẫu số liệu luôn bằng:",
        "options": [
          "$100\\%$",
          "$50\\%$",
          "$10\\%$",
          "$1\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ hình quạt tròn thường được dùng để biểu diễn:",
        "options": [
          "Cơ cấu tỉ lệ phần trăm các thành phần",
          "Sự thay đổi số liệu theo thời gian",
          "Tần số tuyệt đối của từng giá trị",
          "Giá trị lớn nhất và nhỏ nhất"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về số lượng sản phẩm lỗi mỗi ngày trong tháng của phân xưởng. Có 16 người chọn mức 1. Tần số tương đối của nhóm này là:",
        "options": [
          "$53.3\\%$",
          "$0.5\\%$",
          "$16\\%$",
          "$30\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bảng tần số ghép nhóm thường dùng khi dữ liệu thống kê:",
        "options": [
          "Có quy mô lớn hoặc là biến liên tục",
          "Chỉ có từ 2 đến 3 giá trị",
          "Là dữ liệu định tính không đo lường được",
          "Có tần số bằng nhau"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong bảng phân bố tần số ghép nhóm $[20; 30)$, giá trị đại diện của nhóm này là:",
        "options": [
          "$25$",
          "$20$",
          "$30$",
          "$50$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho mẫu số liệu có tổng tần số $N = 30$. Nhóm có tần số tương đối $20\\%$ thì tần số của nhóm đó là:",
        "options": [
          "$6$",
          "$3$",
          "$30$",
          "$20$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Khảo sát điểm kiểm tra của 30 học sinh. Số học sinh đạt điểm Giỏi (từ 8 đến 10) là 12. Tần số tương đối của học sinh đạt điểm Giỏi là:",
        "options": [
          "$40\\%$",
          "$30\\%$",
          "$50\\%$",
          "$20\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trên biểu đồ hình quạt tròn thể hiện kết quả điều tra, một hình quạt tròn có góc ở tâm bằng $112^\\circ$. Tần số tương đối tương ứng của nhóm này là:",
        "options": [
          "$31.1\\%$",
          "$20\\%$",
          "$25\\%$",
          "$30\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Điều tra mức lương của 100 công nhân. Nhóm lương từ 8 đến 10 triệu đồng chiếm $35\\%$, nhóm từ 10 đến 12 triệu chiếm $40\\%$. Số công nhân có mức lương từ 8 đến 12 triệu đồng là:",
        "options": [
          "$75$ công nhân",
          "$35$ công nhân",
          "$40$ công nhân",
          "$25$ công nhân"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Nếu tăng gấp đôi tất cả các tần số của một mẫu số liệu thì tần số tương đối của từng giá trị sẽ:",
        "options": [
          "Không đổi",
          "Tăng gấp đôi",
          "Giảm đi một nửa",
          "Tăng thêm 100%"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về tần số và tần số tương đối (Đề 04):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng các tần số của tất cả các giá trị bằng quy mô mẫu N.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng các tần số tương đối bằng 100%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối fi luôn là số không âm và không vượt quá 100%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Biểu đồ đoạn thẳng không thể dùng để biểu diễn tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng khảo sát số lượng sản phẩm lỗi mỗi ngày trong tháng của phân xưởng gồm 30 đối tượng điều tra:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Kích thước mẫu số liệu là N = 30.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Mỗi giá trị có tần số mi tương ứng với số đối tượng đạt giá trị đó.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối cho biết tỉ lệ phần trăm của từng nhóm trong toàn bộ mẫu.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm trên biểu đồ quạt tròn tỉ lệ nghịch với tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một lớp có 40 học sinh, trong đó có 10 bạn giỏi Toán. Tính tần số tương đối (%) của học sinh giỏi Toán.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Trên biểu đồ quạt tròn, nhóm A chiếm góc 90 độ ở tâm. Tính tần số tương đối (%) của nhóm A.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát 200 khách hàng mua sắm tại siêu thị, có 70 người thanh toán bằng mã QR. Tính tần số tương đối (%) thanh toán bằng QR.",
        "answer": "35",
        "acceptableAnswers": [
          "35"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **35**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong bảng phân bố tần số ghép nhóm có nhóm [10; 20) với tần số 30 và tổng cỡ mẫu là 120. Tính tần số tương đối (%) của nhóm này.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về số con trong 30 gia đình tại một thôn cho kết quả: 1 con: 6 gia đình; 2 con: 18 gia đình; 3 con: 6 gia đình. Hãy lập bảng tần số tương đối.",
        "rubric": "Cỡ mẫu N = 30 (0.25đ).\nTần số tương đối gia đình 1 con: f1 = 6/30 . 100% = 20% (0.25đ).\nTần số tương đối gia đình 2 con: f2 = 18/30 . 100% = 60% (0.25đ).\nTần số tương đối gia đình 3 con: f3 = 6/30 . 100% = 20% (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian xem tivi mỗi ngày của 50 học sinh: Dưới 1 giờ: 15 bạn; Từ 1 đến 2 giờ: 25 bạn; Trên 2 giờ: 10 bạn. Hãy tính số đo cung hình quạt tròn tương ứng với từng nhóm để vẽ biểu đồ quạt tròn.",
        "rubric": "Nhóm dưới 1 giờ: tỉ lệ 15/50 = 30% => Góc ở tâm = 30% . 360 độ = 108 độ (0.25đ).\nNhóm từ 1 đến 2 giờ: tỉ lệ 25/50 = 50% => Góc ở tâm = 50% . 360 độ = 180 độ (0.25đ).\nNhóm trên 2 giờ: tỉ lệ 10/50 = 20% => Góc ở tâm = 20% . 360 độ = 72 độ (0.25đ).\nTổng số đo các góc = 108 + 180 + 72 = 360 độ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một trạm khí tượng đo lượng mưa trong 30 ngày của tháng 7. Biết lượng mưa trung bình là 15 mm/ngày. Nếu bỏ đi 2 ngày có lượng mưa đột biến là 45 mm và 55 mm thì lượng mưa trung bình của 28 ngày còn lại là bao nhiêu?",
        "rubric": "Tổng lượng mưa trong 30 ngày là: 30 . 15 = 450 (mm) (0.25đ).\nTổng lượng mưa của 2 ngày đột biến là: 45 + 55 = 100 (mm) (0.25đ).\nTổng lượng mưa của 28 ngày còn lại là: 450 - 100 = 350 (mm) (0.25đ).\nLượng mưa trung bình của 28 ngày còn lại là: 350 / 28 = 12,5 (mm/ngày) (0.25đ)."
      }
    ]
  },
  "c7_9_bai4_test5": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số 05",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tần số của một giá trị trong mẫu số liệu là:",
        "options": [
          "Số lần xuất hiện của giá trị đó trong mẫu",
          "Tỉ số phần trăm của giá trị đó",
          "Giá trị lớn nhất của mẫu",
          "Số trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tần số tương đối $f_i$ của giá trị $x_i$ có tần số $m_i$ trong mẫu kích thước $N$ là:",
        "options": [
          "$f_i = \\frac{m_i}{N} \\cdot 100\\%$",
          "$f_i = \\frac{N}{m_i} \\cdot 100\\%$",
          "$f_i = m_i \\cdot N$",
          "$f_i = m_i + N$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong mẫu số liệu luôn bằng:",
        "options": [
          "$100\\%$",
          "$50\\%$",
          "$10\\%$",
          "$1\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ hình quạt tròn thường được dùng để biểu diễn:",
        "options": [
          "Cơ cấu tỉ lệ phần trăm các thành phần",
          "Sự thay đổi số liệu theo thời gian",
          "Tần số tuyệt đối của từng giá trị",
          "Giá trị lớn nhất và nhỏ nhất"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về số km đi làm mỗi ngày của 35 cán bộ công nhân viên. Có 20 người chọn mức 1. Tần số tương đối của nhóm này là:",
        "options": [
          "$57.1\\%$",
          "$0.6\\%$",
          "$20\\%$",
          "$35\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bảng tần số ghép nhóm thường dùng khi dữ liệu thống kê:",
        "options": [
          "Có quy mô lớn hoặc là biến liên tục",
          "Chỉ có từ 2 đến 3 giá trị",
          "Là dữ liệu định tính không đo lường được",
          "Có tần số bằng nhau"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong bảng phân bố tần số ghép nhóm $[20; 30)$, giá trị đại diện của nhóm này là:",
        "options": [
          "$25$",
          "$20$",
          "$30$",
          "$50$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho mẫu số liệu có tổng tần số $N = 35$. Nhóm có tần số tương đối $20\\%$ thì tần số của nhóm đó là:",
        "options": [
          "$7$",
          "$3$",
          "$35$",
          "$20$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Khảo sát điểm kiểm tra của 35 học sinh. Số học sinh đạt điểm Giỏi (từ 8 đến 10) là 14. Tần số tương đối của học sinh đạt điểm Giỏi là:",
        "options": [
          "$40\\%$",
          "$30\\%$",
          "$50\\%$",
          "$20\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trên biểu đồ hình quạt tròn thể hiện kết quả điều tra, một hình quạt tròn có góc ở tâm bằng $122^\\circ$. Tần số tương đối tương ứng của nhóm này là:",
        "options": [
          "$33.9\\%$",
          "$20\\%$",
          "$25\\%$",
          "$30\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Điều tra mức lương của 100 công nhân. Nhóm lương từ 8 đến 10 triệu đồng chiếm $35\\%$, nhóm từ 10 đến 12 triệu chiếm $40\\%$. Số công nhân có mức lương từ 8 đến 12 triệu đồng là:",
        "options": [
          "$75$ công nhân",
          "$35$ công nhân",
          "$40$ công nhân",
          "$25$ công nhân"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Nếu tăng gấp đôi tất cả các tần số của một mẫu số liệu thì tần số tương đối của từng giá trị sẽ:",
        "options": [
          "Không đổi",
          "Tăng gấp đôi",
          "Giảm đi một nửa",
          "Tăng thêm 100%"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về tần số và tần số tương đối (Đề 05):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng các tần số của tất cả các giá trị bằng quy mô mẫu N.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng các tần số tương đối bằng 100%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối fi luôn là số không âm và không vượt quá 100%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Biểu đồ đoạn thẳng không thể dùng để biểu diễn tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng khảo sát số km đi làm mỗi ngày của 35 cán bộ công nhân viên gồm 35 đối tượng điều tra:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Kích thước mẫu số liệu là N = 35.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Mỗi giá trị có tần số mi tương ứng với số đối tượng đạt giá trị đó.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối cho biết tỉ lệ phần trăm của từng nhóm trong toàn bộ mẫu.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm trên biểu đồ quạt tròn tỉ lệ nghịch với tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một lớp có 40 học sinh, trong đó có 10 bạn giỏi Toán. Tính tần số tương đối (%) của học sinh giỏi Toán.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Trên biểu đồ quạt tròn, nhóm A chiếm góc 90 độ ở tâm. Tính tần số tương đối (%) của nhóm A.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát 200 khách hàng mua sắm tại siêu thị, có 70 người thanh toán bằng mã QR. Tính tần số tương đối (%) thanh toán bằng QR.",
        "answer": "35",
        "acceptableAnswers": [
          "35"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **35**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong bảng phân bố tần số ghép nhóm có nhóm [10; 20) với tần số 30 và tổng cỡ mẫu là 120. Tính tần số tương đối (%) của nhóm này.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về số con trong 30 gia đình tại một thôn cho kết quả: 1 con: 6 gia đình; 2 con: 18 gia đình; 3 con: 6 gia đình. Hãy lập bảng tần số tương đối.",
        "rubric": "Cỡ mẫu N = 30 (0.25đ).\nTần số tương đối gia đình 1 con: f1 = 6/30 . 100% = 20% (0.25đ).\nTần số tương đối gia đình 2 con: f2 = 18/30 . 100% = 60% (0.25đ).\nTần số tương đối gia đình 3 con: f3 = 6/30 . 100% = 20% (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian xem tivi mỗi ngày của 50 học sinh: Dưới 1 giờ: 15 bạn; Từ 1 đến 2 giờ: 25 bạn; Trên 2 giờ: 10 bạn. Hãy tính số đo cung hình quạt tròn tương ứng với từng nhóm để vẽ biểu đồ quạt tròn.",
        "rubric": "Nhóm dưới 1 giờ: tỉ lệ 15/50 = 30% => Góc ở tâm = 30% . 360 độ = 108 độ (0.25đ).\nNhóm từ 1 đến 2 giờ: tỉ lệ 25/50 = 50% => Góc ở tâm = 50% . 360 độ = 180 độ (0.25đ).\nNhóm trên 2 giờ: tỉ lệ 10/50 = 20% => Góc ở tâm = 20% . 360 độ = 72 độ (0.25đ).\nTổng số đo các góc = 108 + 180 + 72 = 360 độ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một trạm khí tượng đo lượng mưa trong 30 ngày của tháng 7. Biết lượng mưa trung bình là 15 mm/ngày. Nếu bỏ đi 2 ngày có lượng mưa đột biến là 45 mm và 55 mm thì lượng mưa trung bình của 28 ngày còn lại là bao nhiêu?",
        "rubric": "Tổng lượng mưa trong 30 ngày là: 30 . 15 = 450 (mm) (0.25đ).\nTổng lượng mưa của 2 ngày đột biến là: 45 + 55 = 100 (mm) (0.25đ).\nTổng lượng mưa của 28 ngày còn lại là: 450 - 100 = 350 (mm) (0.25đ).\nLượng mưa trung bình của 28 ngày còn lại là: 350 / 28 = 12,5 (mm/ngày) (0.25đ)."
      }
    ]
  },
  "c7_9_bai4_test6": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số 06",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tần số của một giá trị trong mẫu số liệu là:",
        "options": [
          "Số lần xuất hiện của giá trị đó trong mẫu",
          "Tỉ số phần trăm của giá trị đó",
          "Giá trị lớn nhất của mẫu",
          "Số trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tần số tương đối $f_i$ của giá trị $x_i$ có tần số $m_i$ trong mẫu kích thước $N$ là:",
        "options": [
          "$f_i = \\frac{m_i}{N} \\cdot 100\\%$",
          "$f_i = \\frac{N}{m_i} \\cdot 100\\%$",
          "$f_i = m_i \\cdot N$",
          "$f_i = m_i + N$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong mẫu số liệu luôn bằng:",
        "options": [
          "$100\\%$",
          "$50\\%$",
          "$10\\%$",
          "$1\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ hình quạt tròn thường được dùng để biểu diễn:",
        "options": [
          "Cơ cấu tỉ lệ phần trăm các thành phần",
          "Sự thay đổi số liệu theo thời gian",
          "Tần số tuyệt đối của từng giá trị",
          "Giá trị lớn nhất và nhỏ nhất"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về lượng nước sinh hoạt tiêu thụ m^3 của 40 hộ gia đình. Có 24 người chọn mức 1. Tần số tương đối của nhóm này là:",
        "options": [
          "$60.0\\%$",
          "$0.6\\%$",
          "$24\\%$",
          "$40\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bảng tần số ghép nhóm thường dùng khi dữ liệu thống kê:",
        "options": [
          "Có quy mô lớn hoặc là biến liên tục",
          "Chỉ có từ 2 đến 3 giá trị",
          "Là dữ liệu định tính không đo lường được",
          "Có tần số bằng nhau"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong bảng phân bố tần số ghép nhóm $[20; 30)$, giá trị đại diện của nhóm này là:",
        "options": [
          "$25$",
          "$20$",
          "$30$",
          "$50$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho mẫu số liệu có tổng tần số $N = 40$. Nhóm có tần số tương đối $20\\%$ thì tần số của nhóm đó là:",
        "options": [
          "$8$",
          "$4$",
          "$40$",
          "$20$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Khảo sát điểm kiểm tra của 40 học sinh. Số học sinh đạt điểm Giỏi (từ 8 đến 10) là 16. Tần số tương đối của học sinh đạt điểm Giỏi là:",
        "options": [
          "$40\\%$",
          "$30\\%$",
          "$50\\%$",
          "$20\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trên biểu đồ hình quạt tròn thể hiện kết quả điều tra, một hình quạt tròn có góc ở tâm bằng $132^\\circ$. Tần số tương đối tương ứng của nhóm này là:",
        "options": [
          "$36.7\\%$",
          "$20\\%$",
          "$25\\%$",
          "$30\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Điều tra mức lương của 100 công nhân. Nhóm lương từ 8 đến 10 triệu đồng chiếm $35\\%$, nhóm từ 10 đến 12 triệu chiếm $40\\%$. Số công nhân có mức lương từ 8 đến 12 triệu đồng là:",
        "options": [
          "$75$ công nhân",
          "$35$ công nhân",
          "$40$ công nhân",
          "$25$ công nhân"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Nếu tăng gấp đôi tất cả các tần số của một mẫu số liệu thì tần số tương đối của từng giá trị sẽ:",
        "options": [
          "Không đổi",
          "Tăng gấp đôi",
          "Giảm đi một nửa",
          "Tăng thêm 100%"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về tần số và tần số tương đối (Đề 06):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng các tần số của tất cả các giá trị bằng quy mô mẫu N.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng các tần số tương đối bằng 100%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối fi luôn là số không âm và không vượt quá 100%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Biểu đồ đoạn thẳng không thể dùng để biểu diễn tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng khảo sát lượng nước sinh hoạt tiêu thụ m^3 của 40 hộ gia đình gồm 40 đối tượng điều tra:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Kích thước mẫu số liệu là N = 40.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Mỗi giá trị có tần số mi tương ứng với số đối tượng đạt giá trị đó.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối cho biết tỉ lệ phần trăm của từng nhóm trong toàn bộ mẫu.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm trên biểu đồ quạt tròn tỉ lệ nghịch với tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một lớp có 40 học sinh, trong đó có 10 bạn giỏi Toán. Tính tần số tương đối (%) của học sinh giỏi Toán.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Trên biểu đồ quạt tròn, nhóm A chiếm góc 90 độ ở tâm. Tính tần số tương đối (%) của nhóm A.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát 200 khách hàng mua sắm tại siêu thị, có 70 người thanh toán bằng mã QR. Tính tần số tương đối (%) thanh toán bằng QR.",
        "answer": "35",
        "acceptableAnswers": [
          "35"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **35**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong bảng phân bố tần số ghép nhóm có nhóm [10; 20) với tần số 30 và tổng cỡ mẫu là 120. Tính tần số tương đối (%) của nhóm này.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về số con trong 30 gia đình tại một thôn cho kết quả: 1 con: 6 gia đình; 2 con: 18 gia đình; 3 con: 6 gia đình. Hãy lập bảng tần số tương đối.",
        "rubric": "Cỡ mẫu N = 30 (0.25đ).\nTần số tương đối gia đình 1 con: f1 = 6/30 . 100% = 20% (0.25đ).\nTần số tương đối gia đình 2 con: f2 = 18/30 . 100% = 60% (0.25đ).\nTần số tương đối gia đình 3 con: f3 = 6/30 . 100% = 20% (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian xem tivi mỗi ngày của 50 học sinh: Dưới 1 giờ: 15 bạn; Từ 1 đến 2 giờ: 25 bạn; Trên 2 giờ: 10 bạn. Hãy tính số đo cung hình quạt tròn tương ứng với từng nhóm để vẽ biểu đồ quạt tròn.",
        "rubric": "Nhóm dưới 1 giờ: tỉ lệ 15/50 = 30% => Góc ở tâm = 30% . 360 độ = 108 độ (0.25đ).\nNhóm từ 1 đến 2 giờ: tỉ lệ 25/50 = 50% => Góc ở tâm = 50% . 360 độ = 180 độ (0.25đ).\nNhóm trên 2 giờ: tỉ lệ 10/50 = 20% => Góc ở tâm = 20% . 360 độ = 72 độ (0.25đ).\nTổng số đo các góc = 108 + 180 + 72 = 360 độ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một trạm khí tượng đo lượng mưa trong 30 ngày của tháng 7. Biết lượng mưa trung bình là 15 mm/ngày. Nếu bỏ đi 2 ngày có lượng mưa đột biến là 45 mm và 55 mm thì lượng mưa trung bình của 28 ngày còn lại là bao nhiêu?",
        "rubric": "Tổng lượng mưa trong 30 ngày là: 30 . 15 = 450 (mm) (0.25đ).\nTổng lượng mưa của 2 ngày đột biến là: 45 + 55 = 100 (mm) (0.25đ).\nTổng lượng mưa của 28 ngày còn lại là: 450 - 100 = 350 (mm) (0.25đ).\nLượng mưa trung bình của 28 ngày còn lại là: 350 / 28 = 12,5 (mm/ngày) (0.25đ)."
      }
    ]
  },
  "c7_9_bai4_test7": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VII: Tần số và tần số tương đối - Đề số 07",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tần số của một giá trị trong mẫu số liệu là:",
        "options": [
          "Số lần xuất hiện của giá trị đó trong mẫu",
          "Tỉ số phần trăm của giá trị đó",
          "Giá trị lớn nhất của mẫu",
          "Số trung bình cộng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tần số tương đối $f_i$ của giá trị $x_i$ có tần số $m_i$ trong mẫu kích thước $N$ là:",
        "options": [
          "$f_i = \\frac{m_i}{N} \\cdot 100\\%$",
          "$f_i = \\frac{N}{m_i} \\cdot 100\\%$",
          "$f_i = m_i \\cdot N$",
          "$f_i = m_i + N$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tổng tất cả các tần số tương đối của các giá trị trong mẫu số liệu luôn bằng:",
        "options": [
          "$100\\%$",
          "$50\\%$",
          "$10\\%$",
          "$1\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Biểu đồ hình quạt tròn thường được dùng để biểu diễn:",
        "options": [
          "Cơ cấu tỉ lệ phần trăm các thành phần",
          "Sự thay đổi số liệu theo thời gian",
          "Tần số tuyệt đối của từng giá trị",
          "Giá trị lớn nhất và nhỏ nhất"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về số tin nhắn điện tử khách hàng gửi đến trung tâm hỗ trợ. Có 28 người chọn mức 1. Tần số tương đối của nhóm này là:",
        "options": [
          "$56.0\\%$",
          "$0.6\\%$",
          "$28\\%$",
          "$50\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bảng tần số ghép nhóm thường dùng khi dữ liệu thống kê:",
        "options": [
          "Có quy mô lớn hoặc là biến liên tục",
          "Chỉ có từ 2 đến 3 giá trị",
          "Là dữ liệu định tính không đo lường được",
          "Có tần số bằng nhau"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong bảng phân bố tần số ghép nhóm $[20; 30)$, giá trị đại diện của nhóm này là:",
        "options": [
          "$25$",
          "$20$",
          "$30$",
          "$50$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho mẫu số liệu có tổng tần số $N = 50$. Nhóm có tần số tương đối $20\\%$ thì tần số của nhóm đó là:",
        "options": [
          "$10$",
          "$5$",
          "$50$",
          "$20$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Khảo sát điểm kiểm tra của 50 học sinh. Số học sinh đạt điểm Giỏi (từ 8 đến 10) là 20. Tần số tương đối của học sinh đạt điểm Giỏi là:",
        "options": [
          "$40\\%$",
          "$30\\%$",
          "$50\\%$",
          "$20\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trên biểu đồ hình quạt tròn thể hiện kết quả điều tra, một hình quạt tròn có góc ở tâm bằng $142^\\circ$. Tần số tương đối tương ứng của nhóm này là:",
        "options": [
          "$39.4\\%$",
          "$20\\%$",
          "$25\\%$",
          "$30\\%$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Điều tra mức lương của 100 công nhân. Nhóm lương từ 8 đến 10 triệu đồng chiếm $35\\%$, nhóm từ 10 đến 12 triệu chiếm $40\\%$. Số công nhân có mức lương từ 8 đến 12 triệu đồng là:",
        "options": [
          "$75$ công nhân",
          "$35$ công nhân",
          "$40$ công nhân",
          "$25$ công nhân"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Nếu tăng gấp đôi tất cả các tần số của một mẫu số liệu thì tần số tương đối của từng giá trị sẽ:",
        "options": [
          "Không đổi",
          "Tăng gấp đôi",
          "Giảm đi một nửa",
          "Tăng thêm 100%"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về tần số và tần số tương đối (Đề 07):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng các tần số của tất cả các giá trị bằng quy mô mẫu N.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng các tần số tương đối bằng 100%.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối fi luôn là số không âm và không vượt quá 100%.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Biểu đồ đoạn thẳng không thể dùng để biểu diễn tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bảng khảo sát số tin nhắn điện tử khách hàng gửi đến trung tâm hỗ trợ gồm 50 đối tượng điều tra:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Kích thước mẫu số liệu là N = 50.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Mỗi giá trị có tần số mi tương ứng với số đối tượng đạt giá trị đó.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tần số tương đối cho biết tỉ lệ phần trăm của từng nhóm trong toàn bộ mẫu.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Góc ở tâm trên biểu đồ quạt tròn tỉ lệ nghịch với tần số tương đối.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một lớp có 40 học sinh, trong đó có 10 bạn giỏi Toán. Tính tần số tương đối (%) của học sinh giỏi Toán.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Trên biểu đồ quạt tròn, nhóm A chiếm góc 90 độ ở tâm. Tính tần số tương đối (%) của nhóm A.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khảo sát 200 khách hàng mua sắm tại siêu thị, có 70 người thanh toán bằng mã QR. Tính tần số tương đối (%) thanh toán bằng QR.",
        "answer": "35",
        "acceptableAnswers": [
          "35"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **35**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong bảng phân bố tần số ghép nhóm có nhóm [10; 20) với tần số 30 và tổng cỡ mẫu là 120. Tính tần số tương đối (%) của nhóm này.",
        "answer": "25",
        "acceptableAnswers": [
          "25"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **25**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một cuộc điều tra về số con trong 30 gia đình tại một thôn cho kết quả: 1 con: 6 gia đình; 2 con: 18 gia đình; 3 con: 6 gia đình. Hãy lập bảng tần số tương đối.",
        "rubric": "Cỡ mẫu N = 30 (0.25đ).\nTần số tương đối gia đình 1 con: f1 = 6/30 . 100% = 20% (0.25đ).\nTần số tương đối gia đình 2 con: f2 = 18/30 . 100% = 60% (0.25đ).\nTần số tương đối gia đình 3 con: f3 = 6/30 . 100% = 20% (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Khảo sát thời gian xem tivi mỗi ngày của 50 học sinh: Dưới 1 giờ: 15 bạn; Từ 1 đến 2 giờ: 25 bạn; Trên 2 giờ: 10 bạn. Hãy tính số đo cung hình quạt tròn tương ứng với từng nhóm để vẽ biểu đồ quạt tròn.",
        "rubric": "Nhóm dưới 1 giờ: tỉ lệ 15/50 = 30% => Góc ở tâm = 30% . 360 độ = 108 độ (0.25đ).\nNhóm từ 1 đến 2 giờ: tỉ lệ 25/50 = 50% => Góc ở tâm = 50% . 360 độ = 180 độ (0.25đ).\nNhóm trên 2 giờ: tỉ lệ 10/50 = 20% => Góc ở tâm = 20% . 360 độ = 72 độ (0.25đ).\nTổng số đo các góc = 108 + 180 + 72 = 360 độ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một trạm khí tượng đo lượng mưa trong 30 ngày của tháng 7. Biết lượng mưa trung bình là 15 mm/ngày. Nếu bỏ đi 2 ngày có lượng mưa đột biến là 45 mm và 55 mm thì lượng mưa trung bình của 28 ngày còn lại là bao nhiêu?",
        "rubric": "Tổng lượng mưa trong 30 ngày là: 30 . 15 = 450 (mm) (0.25đ).\nTổng lượng mưa của 2 ngày đột biến là: 45 + 55 = 100 (mm) (0.25đ).\nTổng lượng mưa của 28 ngày còn lại là: 450 - 100 = 350 (mm) (0.25đ).\nLượng mưa trung bình của 28 ngày còn lại là: 350 / 28 = 12,5 (mm/ngày) (0.25đ)."
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
