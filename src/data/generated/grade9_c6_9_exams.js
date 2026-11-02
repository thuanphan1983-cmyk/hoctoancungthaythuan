// ==============================================================================
// NGÂN HÀNG ĐỀ KIỂM TRA CHƯƠNG VI: HÀM SỐ $Y = AX^2$ ($A \NEQ 0$). PHƯƠNG TRÌNH BẬC HAI MỘT ẨN - TOÁN 9 (KNTT)
// Chuẩn ma trận khảo thí 2025: Đề 1 & 2 (Khá 40/30/20/10), Đề 3 (Khá Giỏi 20/30/30/20)
// Cập nhật lúc: 2026-11-02 06:43:13
// ==============================================================================

const EXAMS_9_C6_9 = {
  "c6_9_bai1_test1": {
    "title": "Toán 9 (KNTT) - Bài 18: Hàm số y = ax^2 (a != 0) - Đề số 1 (🌿 Mức độ Khá (Đề 1))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai1_test2": {
    "title": "Toán 9 (KNTT) - Bài 18: Hàm số y = ax^2 (a != 0) - Đề số 2 (🌿 Mức độ Khá (Đề 2))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai1_test3": {
    "title": "Toán 9 (KNTT) - Bài 18: Hàm số y = ax^2 (a != 0) - Đề số 3 (🚀 Mức độ Khá Giỏi)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai2_test1": {
    "title": "Toán 9 (KNTT) - Bài 19: Phương trình bậc hai một ẩn - Đề số 1 (🌿 Mức độ Khá (Đề 1))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai2_test2": {
    "title": "Toán 9 (KNTT) - Bài 19: Phương trình bậc hai một ẩn - Đề số 2 (🌿 Mức độ Khá (Đề 2))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai2_test3": {
    "title": "Toán 9 (KNTT) - Bài 19: Phương trình bậc hai một ẩn - Đề số 3 (🚀 Mức độ Khá Giỏi)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai3_test1": {
    "title": "Toán 9 (KNTT) - Bài 20: Định lí Viète và ứng dụng - Đề số 1 (🌿 Mức độ Khá (Đề 1))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai3_test2": {
    "title": "Toán 9 (KNTT) - Bài 20: Định lí Viète và ứng dụng - Đề số 2 (🌿 Mức độ Khá (Đề 2))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai3_test3": {
    "title": "Toán 9 (KNTT) - Bài 20: Định lí Viète và ứng dụng - Đề số 3 (🚀 Mức độ Khá Giỏi)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai4_test1": {
    "title": "Toán 9 (KNTT) - Bài 21: Giải bài toán bằng cách lập phương trình - Đề số 1 (🌿 Mức độ Khá (Đề 1))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai4_test2": {
    "title": "Toán 9 (KNTT) - Bài 21: Giải bài toán bằng cách lập phương trình - Đề số 2 (🌿 Mức độ Khá (Đề 2))",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai4_test3": {
    "title": "Toán 9 (KNTT) - Bài 21: Giải bài toán bằng cách lập phương trình - Đề số 3 (🚀 Mức độ Khá Giỏi)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là:",
        "options": [
          "Một đường cong Parabol đi qua gốc tọa độ $O$",
          "Một đường thẳng",
          "Một đường tròn",
          "Một đường hyperbol"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hàm số $y = ax^2$ với $a > 0$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) có biệt thức $\\Delta$ bằng:",
        "options": [
          "$b^2 - 4ac$",
          "$b^2 + 4ac$",
          "$4ac - b^2$",
          "$b - 4ac$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có 2 nghiệm phân biệt khi:",
        "options": [
          "$\\Delta > 0$",
          "$\\Delta = 0$",
          "$\\Delta < 0$",
          "$\\Delta \\le 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có nghiệm kép khi:",
        "options": [
          "$\\Delta = 0$",
          "$\\Delta > 0$",
          "$\\Delta < 0$",
          "$a = c$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Theo định lí Viète, nếu $x_1, x_2$ là hai nghiệm của $ax^2 + bx + c = 0$ thì $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{b}{a}$",
          "$\\frac{b}{a}$",
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tích hai nghiệm $x_1 \\cdot x_2$ theo định lí Viète bằng:",
        "options": [
          "$\\frac{c}{a}$",
          "$-\\frac{c}{a}$",
          "$\\frac{b}{a}$",
          "$-\\frac{b}{a}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nếu $a + b + c = 0$ thì phương trình $ax^2 + bx + c = 0$ có một nghiệm là:",
        "options": [
          "$x_1 = 1, x_2 = \\frac{c}{a}$",
          "$x_1 = -1, x_2 = -\\frac{c}{a}$",
          "$x_1 = 0$",
          "$x_1 = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Tìm các nghiệm của phương trình $x^2 - 5x + 6 = 0$:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = -3$",
          "$x_1 = 1, x_2 = 6$",
          "$x_1 = -1, x_2 = -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Đồ thị hàm số $y = 2x^2$ đi qua điểm nào sau đây?",
        "options": [
          "$A(1; 2)$",
          "$B(2; 4)$",
          "$C(-1; -2)$",
          "$D(0; 2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Biết $x_1, x_2$ là nghiệm của phương trình $x^2 - 7x + 10 = 0$. Giá trị của $x_1^2 + x_2^2$ bằng:",
        "options": [
          "$29$",
          "$49$",
          "$39$",
          "$19$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Tìm $m$ để phương trình $x^2 - 2x + m = 0$ có hai nghiệm phân biệt:",
        "options": [
          "$m < 1$",
          "$m > 1$",
          "$m = 1$",
          "$m \\le 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho parabol (P): y = x² và đường thẳng (d): y = 2x + 3:",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Parabol (P) có đỉnh tại gốc tọa độ O(0; 0) và trục đối xứng là trục Oy.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Nhận biết",
            "text": "Hàm số y = x² nghịch biến khi x < 0 và đồng biến khi x > 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình hoành độ giao điểm của (P) và (d) là x² - 2x - 3 = 0.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Đường thẳng (d) cắt (P) tại hai điểm phân biệt có tọa độ là (-1; 1) và (3; 9).",
            "correct": true,
            "explanation": "Ý D là **Đúng** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho phương trình bậc hai: x² - 2(m - 1)x + m² - 4 = 0 (với m là tham số):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hệ số a = 1, b' = -(m - 1), c = m² - 4.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biệt thức thu gọn: Δ' = (m - 1)² - (m² - 4) = -2m + 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình có 2 nghiệm phân biệt khi và chỉ khi m < 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Để phương trình có hai nghiệm cùng dấu thì m phải thỏa mãn m > 2 hoặc m < -2.",
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
        "question": "Tính tổng hai nghiệm của phương trình bậc hai $2x^2 - 8x + 3 = 0$:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tính tích hai nghiệm của phương trình $x^2 + 5x - 6 = 0$:",
        "answer": "-6",
        "acceptableAnswers": [
          "-6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **-6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị của $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép:",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một thửa ruộng hình chữ nhật có chu vi $100\\text{ m}$, diện tích $600\\text{ m}^2$. Chiều dài của thửa ruộng bằng bao nhiêu mét?",
        "answer": "30",
        "acceptableAnswers": [
          "30"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **30**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Giải các phương trình bậc hai sau: a) $x^2 - 6x + 8 = 0$; b) $2x^2 - 3x - 5 = 0$.",
        "rubric": "a) Δ' = 9 - 8 = 1 > 0. Phương trình có 2 nghiệm x1 = 3 + 1 = 4; x2 = 3 - 1 = 2 (0.5đ). b) Ta có a - b + c = 2 - (-3) + (-5) = 0 nên x1 = -1; x2 = -c/a = 5/2 (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ sản xuất theo kế hoạch phải làm 300 sản phẩm. Nhờ cải tiến kỹ thuật, mỗi ngày tổ làm thêm được 5 sản phẩm nên đã hoàn thành sớm hơn dự định 3 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải làm bao nhiêu sản phẩm?",
        "rubric": "Gọi số sản phẩm làm mỗi ngày theo kế hoạch là x (x > 0) (0.25đ). Thời gian kế hoạch: 300/x. Thực tế mỗi ngày làm x + 5, thời gian thực tế: 300/(x + 5). Phương trình: 300/x - 300/(x + 5) = 3 (0.5đ). Giải ra x = 20 sản phẩm/ngày (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 2(m + 1)x + 2m = 0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 - x_1 x_2 = 7$.",
        "rubric": "Theo Vi-ét: x1 + x2 = 2(m + 1); x1*x2 = 2m (0.25đ). Biến đổi biểu thức: (x1 + x2)² - 3x1*x2 = 7 <=> 4(m + 1)² - 6m - 7 = 0 (0.25đ). Tương đương 4m² + 2m - 3 = 0. Giải phương trình bậc hai tìm ra m (0.5đ)."
      }
    ]
  },
  "c6_9_bai5_test1": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VI: Hàm số $y = ax^2$ và Phương trình bậc hai một ẩn - Đề số 01",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hàm số $y = 1x^2$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = -1x^2$ có đỉnh tại gốc tọa độ $O(0;0)$ và:",
        "options": [
          "Nằm phía dưới trục hoành",
          "Nằm phía trên trục hoành",
          "Nằm bên phải trục tung",
          "Nằm bên trái trục tung"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Biệt thức $\\Delta$ của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) được tính bởi:",
        "options": [
          "$\\Delta = b^2 - 4ac$",
          "$\\Delta = b^2 - ac$",
          "$\\Delta = b^2 + 4ac$",
          "$\\Delta = 4ac - b^2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Theo định lí Vi-ét, nếu phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có hai nghiệm $x_1, x_2$ thì tổng $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{{b}}{{a}}$",
          "$\\frac{{b}}{{a}}$",
          "$\\frac{{c}}{{a}}$",
          "$-\\frac{{c}}{{a}}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Nghiệm của phương trình $x^2 - 3x + 2 = 0$ là:",
        "options": [
          "$x_1 = 1, x_2 = 2$",
          "$x_1 = -1, x_2 = 2$",
          "$x_1 = 1, x_2 = -2$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Điểm nào sau đây thuộc đồ thị hàm số $y = 1x^2$?",
        "options": [
          "$(1; 1)$",
          "$(1; 1)$",
          "$(1; -1)$",
          "$(-1; -1)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phương trình $x^2 - 4 = 0$ có hai nghiệm là:",
        "options": [
          "$x = \\pm 2$",
          "$x = 2$",
          "$x = \\pm 4$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hai số có tổng bằng $6$ và tích bằng $5$ là nghiệm của phương trình:",
        "options": [
          "$x^2 - 6x + 5 = 0$",
          "$x^2 + 6x + 5 = 0$",
          "$x^2 - 5x + 6 = 0$",
          "$x^2 + 6x - 5 = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một mảnh đất hình chữ nhật có diện tích $100\\text{ m}^2$, chiều dài hơn chiều rộng $15\\text{ m}$. Chiều dài của mảnh đất là:",
        "options": [
          "$20\\text{ m}$",
          "12 m",
          "15 m",
          "20 m"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một vật rơi tự do từ độ cao $5\\text{ m}$ xuống đất theo công thức $s = 5t^2$. Thời gian để vật chạm đất là:",
        "options": [
          "$1\\text{ giây}$",
          "$2\\text{ giây}$",
          "$1\\text{ giây}$",
          "5 giây"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng cơ khí dự định làm $120$ sản phẩm trong một thời gian quy định. Do cải tiến kỹ thuật, mỗi ngày xưởng làm thêm được 5 sản phẩm nên hoàn thành sớm hơn 1 ngày. Phương trình tìm số sản phẩm làm mỗi ngày theo kế hoạch $x$ là:",
        "options": [
          "$\\frac{120}{x} - \\frac{120}{x+5} = 1$",
          "$\\frac{120}{x+5} - \\frac{120}{x} = 1$",
          "$\\frac{x}{100} - \\frac{x+5}{100} = 1$",
          "$(x+5) - x = 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 5x + 4 = 0$ có hai nghiệm $x_1, x_2$. Giá trị biểu thức $A = x_1^2 + x_2^2$ là:",
        "options": [
          "$17$",
          "$25$",
          "$4$",
          "$10$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho phương trình bậc hai $x^2 - 4x + 3 = 0$ (Đề 01):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình có các hệ số a = 1, b = -(2t + 2), c = 2t + 1.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phương trình có dạng a + b + c = 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Hai nghiệm của phương trình là x1 = 1 và x2 = 3.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tích của hai nghiệm bằng số chẵn.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế chuyển động (Mã đề 01): Một tàu tuần tra chạy xuôi dòng 30 km rồi ngược dòng 30 km hết tổng cộng 2,5 giờ. Biết vận tốc dòng nước là 2 km/h.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Gọi vận tốc riêng của tàu tuần tra là v (v > 2, km/h).",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Vận tốc xuôi dòng là v + 2 và ngược dòng là v - 2 (km/h).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình lập được là: 30/(v + 2) + 30/(v - 2) = 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Vận tốc riêng của tàu tuần tra là 20 km/h.",
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
        "question": "Giải phương trình: x^2 - 4 = 0. Tìm nghiệm dương của phương trình.",
        "answer": "2",
        "acceptableAnswers": [
          "2"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **2**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm x1 . x2 của phương trình: 2x^2 - 7x + 6 = 0.",
        "answer": "3",
        "acceptableAnswers": [
          "3"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **3**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một mảnh vườn hình chữ nhật có diện tích 180 m^2, chiều dài hơn chiều rộng 3 m. Tính chiều dài của mảnh vườn (m).",
        "answer": "15",
        "acceptableAnswers": [
          "15"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **15**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người đi xe đạp từ A đến B cách nhau 30 km. Khi về người đó tăng vận tốc thêm 3 km/h nên thời gian về ít hơn thời gian đi 30 phút. Tính vận tốc lúc đi (km/h).",
        "answer": "12",
        "acceptableAnswers": [
          "12"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **12**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình bậc hai sau bằng công thức nghiệm: $x^2 - 5x + 4 = 0$.",
        "rubric": "Hệ số: a = 1, b = -(5), c = 4 (0.25đ).\nDelta = b^2 - 4ac = (5)^2 - 4(4) = 4t^2 + 12t + 9 - 8t - 8 = 4t^2 + 4t + 1 = (2t + 1)^2 >= 0 (0.25đ).\nNghiệm: x1 = (5 + 2t + 1)/2 = 2t + 2; x2 = (5 - 2t - 1)/2 = 1 (0.25đ).\nKết luận tập nghiệm S = {1; 4} (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ công nhân theo kế hoạch phải may 600 chiếc khẩu trang trong thời gian quy định. Nhờ tăng năng suất mỗi ngày may thêm được 10 chiếc nên tổ đã hoàn thành kế hoạch sớm hơn 2 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải may bao nhiêu chiếc khẩu trang?",
        "rubric": "Gọi số khẩu trang may mỗi ngày theo kế hoạch là x (chiếc) (x nguyên dương) (0.25đ).\nThời gian theo kế hoạch là 600/x (ngày), thực tế là 600/(x + 10) (ngày) (0.25đ).\nTheo bài ra ta có pt: 600/x - 600/(x + 10) = 2 <=> x(x + 10) = 3000 <=> x^2 + 10x - 3000 = 0 (0.25đ).\nGiải phương trình được: x1 = 50 (nhận), x2 = -60 (loại). Vậy theo kế hoạch mỗi ngày may 50 chiếc (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 5x + 3 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $B = x_1^3 + x_2^3$.",
        "rubric": "Theo định lí Vi-ét ta có: S = x1 + x2 = 5 và P = x1 . x2 = 3 (0.25đ).\nBiến đổi: B = x1^3 + x2^3 = (x1 + x2)(x1^2 - x1 x2 + x2^2) = (x1 + x2)[(x1 + x2)^2 - 3 x1 x2] (0.25đ).\nThay S = 5 và P = 3 vào: B = 5 . [5^2 - 3 . 3] = 5 . (25 - 9) = 5 . 16 = 80 (0.25đ).\nKết luận giá trị của B là 80 (0.25đ)."
      }
    ]
  },
  "c6_9_bai5_test2": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VI: Hàm số $y = ax^2$ và Phương trình bậc hai một ẩn - Đề số 02",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hàm số $y = 2x^2$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = -2x^2$ có đỉnh tại gốc tọa độ $O(0;0)$ và:",
        "options": [
          "Nằm phía dưới trục hoành",
          "Nằm phía trên trục hoành",
          "Nằm bên phải trục tung",
          "Nằm bên trái trục tung"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Biệt thức $\\Delta$ của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) được tính bởi:",
        "options": [
          "$\\Delta = b^2 - 4ac$",
          "$\\Delta = b^2 - ac$",
          "$\\Delta = b^2 + 4ac$",
          "$\\Delta = 4ac - b^2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Theo định lí Vi-ét, nếu phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có hai nghiệm $x_1, x_2$ thì tổng $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{{b}}{{a}}$",
          "$\\frac{{b}}{{a}}$",
          "$\\frac{{c}}{{a}}$",
          "$-\\frac{{c}}{{a}}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Nghiệm của phương trình $x^2 - 5x + 6 = 0$ là:",
        "options": [
          "$x_1 = 2, x_2 = 3$",
          "$x_1 = -2, x_2 = 3$",
          "$x_1 = 2, x_2 = -3$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Điểm nào sau đây thuộc đồ thị hàm số $y = 2x^2$?",
        "options": [
          "$(1; 2)$",
          "$(2; 1)$",
          "$(1; -2)$",
          "$(-1; -2)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phương trình $x^2 - 8 = 0$ có hai nghiệm là:",
        "options": [
          "$x = \\pm 4$",
          "$x = 4$",
          "$x = \\pm 8$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hai số có tổng bằng $7$ và tích bằng $10$ là nghiệm của phương trình:",
        "options": [
          "$x^2 - 7x + 10 = 0$",
          "$x^2 + 7x + 10 = 0$",
          "$x^2 - 10x + 7 = 0$",
          "$x^2 + 7x - 10 = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một mảnh đất hình chữ nhật có diện tích $32\\text{ m}^2$, chiều dài hơn chiều rộng $4\\text{ m}$. Chiều dài của mảnh đất là:",
        "options": [
          "$8\\text{ m}$",
          "12 m",
          "15 m",
          "20 m"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một vật rơi tự do từ độ cao $20\\text{ m}$ xuống đất theo công thức $s = 5t^2$. Thời gian để vật chạm đất là:",
        "options": [
          "$2\\text{ giây}$",
          "$4\\text{ giây}$",
          "$4\\text{ giây}$",
          "5 giây"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng cơ khí dự định làm $140$ sản phẩm trong một thời gian quy định. Do cải tiến kỹ thuật, mỗi ngày xưởng làm thêm được 5 sản phẩm nên hoàn thành sớm hơn 1 ngày. Phương trình tìm số sản phẩm làm mỗi ngày theo kế hoạch $x$ là:",
        "options": [
          "$\\frac{140}{x} - \\frac{140}{x+5} = 1$",
          "$\\frac{140}{x+5} - \\frac{140}{x} = 1$",
          "$\\frac{x}{100} - \\frac{x+5}{100} = 1$",
          "$(x+5) - x = 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 7x + 10 = 0$ có hai nghiệm $x_1, x_2$. Giá trị biểu thức $A = x_1^2 + x_2^2$ là:",
        "options": [
          "$29$",
          "$49$",
          "$10$",
          "$10$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho phương trình bậc hai $x^2 - 6x + 5 = 0$ (Đề 02):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình có các hệ số a = 1, b = -(2t + 2), c = 2t + 1.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phương trình có dạng a + b + c = 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Hai nghiệm của phương trình là x1 = 1 và x2 = 5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tích của hai nghiệm bằng số chẵn.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế chuyển động (Mã đề 02): Một tàu tuần tra chạy xuôi dòng 30 km rồi ngược dòng 30 km hết tổng cộng 2,5 giờ. Biết vận tốc dòng nước là 2 km/h.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Gọi vận tốc riêng của tàu tuần tra là v (v > 2, km/h).",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Vận tốc xuôi dòng là v + 2 và ngược dòng là v - 2 (km/h).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình lập được là: 30/(v + 2) + 30/(v - 2) = 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Vận tốc riêng của tàu tuần tra là 20 km/h.",
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
        "question": "Giải phương trình: x^2 - 16 = 0. Tìm nghiệm dương của phương trình.",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm x1 . x2 của phương trình: 2x^2 - 7x + 12 = 0.",
        "answer": "6",
        "acceptableAnswers": [
          "6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một mảnh vườn hình chữ nhật có diện tích 180 m^2, chiều dài hơn chiều rộng 3 m. Tính chiều dài của mảnh vườn (m).",
        "answer": "15",
        "acceptableAnswers": [
          "15"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **15**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người đi xe đạp từ A đến B cách nhau 30 km. Khi về người đó tăng vận tốc thêm 3 km/h nên thời gian về ít hơn thời gian đi 30 phút. Tính vận tốc lúc đi (km/h).",
        "answer": "12",
        "acceptableAnswers": [
          "12"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **12**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình bậc hai sau bằng công thức nghiệm: $x^2 - 7x + 6 = 0$.",
        "rubric": "Hệ số: a = 1, b = -(7), c = 6 (0.25đ).\nDelta = b^2 - 4ac = (7)^2 - 4(6) = 4t^2 + 12t + 9 - 8t - 8 = 4t^2 + 4t + 1 = (2t + 1)^2 >= 0 (0.25đ).\nNghiệm: x1 = (7 + 2t + 1)/2 = 2t + 2; x2 = (7 - 2t - 1)/2 = 1 (0.25đ).\nKết luận tập nghiệm S = {1; 6} (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ công nhân theo kế hoạch phải may 600 chiếc khẩu trang trong thời gian quy định. Nhờ tăng năng suất mỗi ngày may thêm được 10 chiếc nên tổ đã hoàn thành kế hoạch sớm hơn 2 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải may bao nhiêu chiếc khẩu trang?",
        "rubric": "Gọi số khẩu trang may mỗi ngày theo kế hoạch là x (chiếc) (x nguyên dương) (0.25đ).\nThời gian theo kế hoạch là 600/x (ngày), thực tế là 600/(x + 10) (ngày) (0.25đ).\nTheo bài ra ta có pt: 600/x - 600/(x + 10) = 2 <=> x(x + 10) = 3000 <=> x^2 + 10x - 3000 = 0 (0.25đ).\nGiải phương trình được: x1 = 50 (nhận), x2 = -60 (loại). Vậy theo kế hoạch mỗi ngày may 50 chiếc (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 5x + 3 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $B = x_1^3 + x_2^3$.",
        "rubric": "Theo định lí Vi-ét ta có: S = x1 + x2 = 5 và P = x1 . x2 = 3 (0.25đ).\nBiến đổi: B = x1^3 + x2^3 = (x1 + x2)(x1^2 - x1 x2 + x2^2) = (x1 + x2)[(x1 + x2)^2 - 3 x1 x2] (0.25đ).\nThay S = 5 và P = 3 vào: B = 5 . [5^2 - 3 . 3] = 5 . (25 - 9) = 5 . 16 = 80 (0.25đ).\nKết luận giá trị của B là 80 (0.25đ)."
      }
    ]
  },
  "c6_9_bai5_test3": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VI: Hàm số $y = ax^2$ và Phương trình bậc hai một ẩn - Đề số 03",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hàm số $y = 3x^2$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = -3x^2$ có đỉnh tại gốc tọa độ $O(0;0)$ và:",
        "options": [
          "Nằm phía dưới trục hoành",
          "Nằm phía trên trục hoành",
          "Nằm bên phải trục tung",
          "Nằm bên trái trục tung"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Biệt thức $\\Delta$ của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) được tính bởi:",
        "options": [
          "$\\Delta = b^2 - 4ac$",
          "$\\Delta = b^2 - ac$",
          "$\\Delta = b^2 + 4ac$",
          "$\\Delta = 4ac - b^2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Theo định lí Vi-ét, nếu phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có hai nghiệm $x_1, x_2$ thì tổng $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{{b}}{{a}}$",
          "$\\frac{{b}}{{a}}$",
          "$\\frac{{c}}{{a}}$",
          "$-\\frac{{c}}{{a}}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Nghiệm của phương trình $x^2 - 7x + 12 = 0$ là:",
        "options": [
          "$x_1 = 3, x_2 = 4$",
          "$x_1 = -3, x_2 = 4$",
          "$x_1 = 3, x_2 = -4$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Điểm nào sau đây thuộc đồ thị hàm số $y = 3x^2$?",
        "options": [
          "$(1; 3)$",
          "$(3; 1)$",
          "$(1; -3)$",
          "$(-1; -3)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phương trình $x^2 - 12 = 0$ có hai nghiệm là:",
        "options": [
          "$x = \\pm 6$",
          "$x = 6$",
          "$x = \\pm 12$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hai số có tổng bằng $8$ và tích bằng $15$ là nghiệm của phương trình:",
        "options": [
          "$x^2 - 8x + 15 = 0$",
          "$x^2 + 8x + 15 = 0$",
          "$x^2 - 15x + 8 = 0$",
          "$x^2 + 8x - 15 = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một mảnh đất hình chữ nhật có diện tích $320\\text{ m}^2$, chiều dài hơn chiều rộng $76\\text{ m}$. Chiều dài của mảnh đất là:",
        "options": [
          "$80\\text{ m}$",
          "12 m",
          "15 m",
          "20 m"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một vật rơi tự do từ độ cao $45\\text{ m}$ xuống đất theo công thức $s = 5t^2$. Thời gian để vật chạm đất là:",
        "options": [
          "$3\\text{ giây}$",
          "$6\\text{ giây}$",
          "$9\\text{ giây}$",
          "5 giây"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng cơ khí dự định làm $160$ sản phẩm trong một thời gian quy định. Do cải tiến kỹ thuật, mỗi ngày xưởng làm thêm được 5 sản phẩm nên hoàn thành sớm hơn 1 ngày. Phương trình tìm số sản phẩm làm mỗi ngày theo kế hoạch $x$ là:",
        "options": [
          "$\\frac{160}{x} - \\frac{160}{x+5} = 1$",
          "$\\frac{160}{x+5} - \\frac{160}{x} = 1$",
          "$\\frac{x}{100} - \\frac{x+5}{100} = 1$",
          "$(x+5) - x = 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 9x + 18 = 0$ có hai nghiệm $x_1, x_2$. Giá trị biểu thức $A = x_1^2 + x_2^2$ là:",
        "options": [
          "$45$",
          "$81$",
          "$18$",
          "$10$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho phương trình bậc hai $x^2 - 8x + 7 = 0$ (Đề 03):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình có các hệ số a = 1, b = -(2t + 2), c = 2t + 1.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phương trình có dạng a + b + c = 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Hai nghiệm của phương trình là x1 = 1 và x2 = 7.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tích của hai nghiệm bằng số chẵn.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế chuyển động (Mã đề 03): Một tàu tuần tra chạy xuôi dòng 30 km rồi ngược dòng 30 km hết tổng cộng 2,5 giờ. Biết vận tốc dòng nước là 2 km/h.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Gọi vận tốc riêng của tàu tuần tra là v (v > 2, km/h).",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Vận tốc xuôi dòng là v + 2 và ngược dòng là v - 2 (km/h).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình lập được là: 30/(v + 2) + 30/(v - 2) = 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Vận tốc riêng của tàu tuần tra là 20 km/h.",
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
        "question": "Giải phương trình: x^2 - 36 = 0. Tìm nghiệm dương của phương trình.",
        "answer": "6",
        "acceptableAnswers": [
          "6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **6**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm x1 . x2 của phương trình: 2x^2 - 7x + 18 = 0.",
        "answer": "9",
        "acceptableAnswers": [
          "9"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **9**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một mảnh vườn hình chữ nhật có diện tích 180 m^2, chiều dài hơn chiều rộng 3 m. Tính chiều dài của mảnh vườn (m).",
        "answer": "15",
        "acceptableAnswers": [
          "15"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **15**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người đi xe đạp từ A đến B cách nhau 30 km. Khi về người đó tăng vận tốc thêm 3 km/h nên thời gian về ít hơn thời gian đi 30 phút. Tính vận tốc lúc đi (km/h).",
        "answer": "12",
        "acceptableAnswers": [
          "12"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **12**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình bậc hai sau bằng công thức nghiệm: $x^2 - 9x + 8 = 0$.",
        "rubric": "Hệ số: a = 1, b = -(9), c = 8 (0.25đ).\nDelta = b^2 - 4ac = (9)^2 - 4(8) = 4t^2 + 12t + 9 - 8t - 8 = 4t^2 + 4t + 1 = (2t + 1)^2 >= 0 (0.25đ).\nNghiệm: x1 = (9 + 2t + 1)/2 = 2t + 2; x2 = (9 - 2t - 1)/2 = 1 (0.25đ).\nKết luận tập nghiệm S = {1; 8} (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ công nhân theo kế hoạch phải may 600 chiếc khẩu trang trong thời gian quy định. Nhờ tăng năng suất mỗi ngày may thêm được 10 chiếc nên tổ đã hoàn thành kế hoạch sớm hơn 2 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải may bao nhiêu chiếc khẩu trang?",
        "rubric": "Gọi số khẩu trang may mỗi ngày theo kế hoạch là x (chiếc) (x nguyên dương) (0.25đ).\nThời gian theo kế hoạch là 600/x (ngày), thực tế là 600/(x + 10) (ngày) (0.25đ).\nTheo bài ra ta có pt: 600/x - 600/(x + 10) = 2 <=> x(x + 10) = 3000 <=> x^2 + 10x - 3000 = 0 (0.25đ).\nGiải phương trình được: x1 = 50 (nhận), x2 = -60 (loại). Vậy theo kế hoạch mỗi ngày may 50 chiếc (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 5x + 3 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $B = x_1^3 + x_2^3$.",
        "rubric": "Theo định lí Vi-ét ta có: S = x1 + x2 = 5 và P = x1 . x2 = 3 (0.25đ).\nBiến đổi: B = x1^3 + x2^3 = (x1 + x2)(x1^2 - x1 x2 + x2^2) = (x1 + x2)[(x1 + x2)^2 - 3 x1 x2] (0.25đ).\nThay S = 5 và P = 3 vào: B = 5 . [5^2 - 3 . 3] = 5 . (25 - 9) = 5 . 16 = 80 (0.25đ).\nKết luận giá trị của B là 80 (0.25đ)."
      }
    ]
  },
  "c6_9_bai5_test4": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VI: Hàm số $y = ax^2$ và Phương trình bậc hai một ẩn - Đề số 04",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hàm số $y = 4x^2$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = -4x^2$ có đỉnh tại gốc tọa độ $O(0;0)$ và:",
        "options": [
          "Nằm phía dưới trục hoành",
          "Nằm phía trên trục hoành",
          "Nằm bên phải trục tung",
          "Nằm bên trái trục tung"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Biệt thức $\\Delta$ của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) được tính bởi:",
        "options": [
          "$\\Delta = b^2 - 4ac$",
          "$\\Delta = b^2 - ac$",
          "$\\Delta = b^2 + 4ac$",
          "$\\Delta = 4ac - b^2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Theo định lí Vi-ét, nếu phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có hai nghiệm $x_1, x_2$ thì tổng $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{{b}}{{a}}$",
          "$\\frac{{b}}{{a}}$",
          "$\\frac{{c}}{{a}}$",
          "$-\\frac{{c}}{{a}}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Nghiệm của phương trình $x^2 - 9x + 20 = 0$ là:",
        "options": [
          "$x_1 = 4, x_2 = 5$",
          "$x_1 = -4, x_2 = 5$",
          "$x_1 = 4, x_2 = -5$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Điểm nào sau đây thuộc đồ thị hàm số $y = 4x^2$?",
        "options": [
          "$(1; 4)$",
          "$(4; 1)$",
          "$(1; -4)$",
          "$(-1; -4)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phương trình $x^2 - 16 = 0$ có hai nghiệm là:",
        "options": [
          "$x = \\pm 8$",
          "$x = 8$",
          "$x = \\pm 16$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hai số có tổng bằng $9$ và tích bằng $20$ là nghiệm của phương trình:",
        "options": [
          "$x^2 - 9x + 20 = 0$",
          "$x^2 + 9x + 20 = 0$",
          "$x^2 - 20x + 9 = 0$",
          "$x^2 + 9x - 20 = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một mảnh đất hình chữ nhật có diện tích $216\\text{ m}^2$, chiều dài hơn chiều rộng $6\\text{ m}$. Chiều dài của mảnh đất là:",
        "options": [
          "$18\\text{ m}$",
          "12 m",
          "15 m",
          "20 m"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một vật rơi tự do từ độ cao $80\\text{ m}$ xuống đất theo công thức $s = 5t^2$. Thời gian để vật chạm đất là:",
        "options": [
          "$4\\text{ giây}$",
          "$8\\text{ giây}$",
          "$16\\text{ giây}$",
          "5 giây"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng cơ khí dự định làm $180$ sản phẩm trong một thời gian quy định. Do cải tiến kỹ thuật, mỗi ngày xưởng làm thêm được 5 sản phẩm nên hoàn thành sớm hơn 1 ngày. Phương trình tìm số sản phẩm làm mỗi ngày theo kế hoạch $x$ là:",
        "options": [
          "$\\frac{180}{x} - \\frac{180}{x+5} = 1$",
          "$\\frac{180}{x+5} - \\frac{180}{x} = 1$",
          "$\\frac{x}{100} - \\frac{x+5}{100} = 1$",
          "$(x+5) - x = 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 11x + 28 = 0$ có hai nghiệm $x_1, x_2$. Giá trị biểu thức $A = x_1^2 + x_2^2$ là:",
        "options": [
          "$65$",
          "$121$",
          "$28$",
          "$10$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho phương trình bậc hai $x^2 - 10x + 9 = 0$ (Đề 04):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình có các hệ số a = 1, b = -(2t + 2), c = 2t + 1.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phương trình có dạng a + b + c = 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Hai nghiệm của phương trình là x1 = 1 và x2 = 9.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tích của hai nghiệm bằng số chẵn.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế chuyển động (Mã đề 04): Một tàu tuần tra chạy xuôi dòng 30 km rồi ngược dòng 30 km hết tổng cộng 2,5 giờ. Biết vận tốc dòng nước là 2 km/h.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Gọi vận tốc riêng của tàu tuần tra là v (v > 2, km/h).",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Vận tốc xuôi dòng là v + 2 và ngược dòng là v - 2 (km/h).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình lập được là: 30/(v + 2) + 30/(v - 2) = 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Vận tốc riêng của tàu tuần tra là 20 km/h.",
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
        "question": "Giải phương trình: x^2 - 64 = 0. Tìm nghiệm dương của phương trình.",
        "answer": "8",
        "acceptableAnswers": [
          "8"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **8**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm x1 . x2 của phương trình: 2x^2 - 7x + 24 = 0.",
        "answer": "12",
        "acceptableAnswers": [
          "12"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **12**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một mảnh vườn hình chữ nhật có diện tích 180 m^2, chiều dài hơn chiều rộng 3 m. Tính chiều dài của mảnh vườn (m).",
        "answer": "15",
        "acceptableAnswers": [
          "15"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **15**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người đi xe đạp từ A đến B cách nhau 30 km. Khi về người đó tăng vận tốc thêm 3 km/h nên thời gian về ít hơn thời gian đi 30 phút. Tính vận tốc lúc đi (km/h).",
        "answer": "12",
        "acceptableAnswers": [
          "12"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **12**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình bậc hai sau bằng công thức nghiệm: $x^2 - 11x + 10 = 0$.",
        "rubric": "Hệ số: a = 1, b = -(11), c = 10 (0.25đ).\nDelta = b^2 - 4ac = (11)^2 - 4(10) = 4t^2 + 12t + 9 - 8t - 8 = 4t^2 + 4t + 1 = (2t + 1)^2 >= 0 (0.25đ).\nNghiệm: x1 = (11 + 2t + 1)/2 = 2t + 2; x2 = (11 - 2t - 1)/2 = 1 (0.25đ).\nKết luận tập nghiệm S = {1; 10} (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ công nhân theo kế hoạch phải may 600 chiếc khẩu trang trong thời gian quy định. Nhờ tăng năng suất mỗi ngày may thêm được 10 chiếc nên tổ đã hoàn thành kế hoạch sớm hơn 2 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải may bao nhiêu chiếc khẩu trang?",
        "rubric": "Gọi số khẩu trang may mỗi ngày theo kế hoạch là x (chiếc) (x nguyên dương) (0.25đ).\nThời gian theo kế hoạch là 600/x (ngày), thực tế là 600/(x + 10) (ngày) (0.25đ).\nTheo bài ra ta có pt: 600/x - 600/(x + 10) = 2 <=> x(x + 10) = 3000 <=> x^2 + 10x - 3000 = 0 (0.25đ).\nGiải phương trình được: x1 = 50 (nhận), x2 = -60 (loại). Vậy theo kế hoạch mỗi ngày may 50 chiếc (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 5x + 3 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $B = x_1^3 + x_2^3$.",
        "rubric": "Theo định lí Vi-ét ta có: S = x1 + x2 = 5 và P = x1 . x2 = 3 (0.25đ).\nBiến đổi: B = x1^3 + x2^3 = (x1 + x2)(x1^2 - x1 x2 + x2^2) = (x1 + x2)[(x1 + x2)^2 - 3 x1 x2] (0.25đ).\nThay S = 5 và P = 3 vào: B = 5 . [5^2 - 3 . 3] = 5 . (25 - 9) = 5 . 16 = 80 (0.25đ).\nKết luận giá trị của B là 80 (0.25đ)."
      }
    ]
  },
  "c6_9_bai5_test5": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VI: Hàm số $y = ax^2$ và Phương trình bậc hai một ẩn - Đề số 05",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hàm số $y = 5x^2$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = -5x^2$ có đỉnh tại gốc tọa độ $O(0;0)$ và:",
        "options": [
          "Nằm phía dưới trục hoành",
          "Nằm phía trên trục hoành",
          "Nằm bên phải trục tung",
          "Nằm bên trái trục tung"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Biệt thức $\\Delta$ của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) được tính bởi:",
        "options": [
          "$\\Delta = b^2 - 4ac$",
          "$\\Delta = b^2 - ac$",
          "$\\Delta = b^2 + 4ac$",
          "$\\Delta = 4ac - b^2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Theo định lí Vi-ét, nếu phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có hai nghiệm $x_1, x_2$ thì tổng $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{{b}}{{a}}$",
          "$\\frac{{b}}{{a}}$",
          "$\\frac{{c}}{{a}}$",
          "$-\\frac{{c}}{{a}}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Nghiệm của phương trình $x^2 - 11x + 30 = 0$ là:",
        "options": [
          "$x_1 = 5, x_2 = 6$",
          "$x_1 = -5, x_2 = 6$",
          "$x_1 = 5, x_2 = -6$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Điểm nào sau đây thuộc đồ thị hàm số $y = 5x^2$?",
        "options": [
          "$(1; 5)$",
          "$(5; 1)$",
          "$(1; -5)$",
          "$(-1; -5)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phương trình $x^2 - 20 = 0$ có hai nghiệm là:",
        "options": [
          "$x = \\pm 10$",
          "$x = 10$",
          "$x = \\pm 20$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hai số có tổng bằng $10$ và tích bằng $25$ là nghiệm của phương trình:",
        "options": [
          "$x^2 - 10x + 25 = 0$",
          "$x^2 + 10x + 25 = 0$",
          "$x^2 - 25x + 10 = 0$",
          "$x^2 + 10x - 25 = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một mảnh đất hình chữ nhật có diện tích $2000\\text{ m}^2$, chiều dài hơn chiều rộng $10\\text{ m}$. Chiều dài của mảnh đất là:",
        "options": [
          "$50\\text{ m}$",
          "12 m",
          "15 m",
          "20 m"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một vật rơi tự do từ độ cao $125\\text{ m}$ xuống đất theo công thức $s = 5t^2$. Thời gian để vật chạm đất là:",
        "options": [
          "$5\\text{ giây}$",
          "$10\\text{ giây}$",
          "$25\\text{ giây}$",
          "5 giây"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng cơ khí dự định làm $200$ sản phẩm trong một thời gian quy định. Do cải tiến kỹ thuật, mỗi ngày xưởng làm thêm được 5 sản phẩm nên hoàn thành sớm hơn 1 ngày. Phương trình tìm số sản phẩm làm mỗi ngày theo kế hoạch $x$ là:",
        "options": [
          "$\\frac{200}{x} - \\frac{200}{x+5} = 1$",
          "$\\frac{200}{x+5} - \\frac{200}{x} = 1$",
          "$\\frac{x}{100} - \\frac{x+5}{100} = 1$",
          "$(x+5) - x = 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 13x + 40 = 0$ có hai nghiệm $x_1, x_2$. Giá trị biểu thức $A = x_1^2 + x_2^2$ là:",
        "options": [
          "$89$",
          "$169$",
          "$40$",
          "$10$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho phương trình bậc hai $x^2 - 12x + 11 = 0$ (Đề 05):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình có các hệ số a = 1, b = -(2t + 2), c = 2t + 1.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phương trình có dạng a + b + c = 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Hai nghiệm của phương trình là x1 = 1 và x2 = 11.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tích của hai nghiệm bằng số chẵn.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế chuyển động (Mã đề 05): Một tàu tuần tra chạy xuôi dòng 30 km rồi ngược dòng 30 km hết tổng cộng 2,5 giờ. Biết vận tốc dòng nước là 2 km/h.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Gọi vận tốc riêng của tàu tuần tra là v (v > 2, km/h).",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Vận tốc xuôi dòng là v + 2 và ngược dòng là v - 2 (km/h).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình lập được là: 30/(v + 2) + 30/(v - 2) = 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Vận tốc riêng của tàu tuần tra là 20 km/h.",
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
        "question": "Giải phương trình: x^2 - 100 = 0. Tìm nghiệm dương của phương trình.",
        "answer": "10",
        "acceptableAnswers": [
          "10"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **10**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm x1 . x2 của phương trình: 2x^2 - 7x + 30 = 0.",
        "answer": "15",
        "acceptableAnswers": [
          "15"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **15**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một mảnh vườn hình chữ nhật có diện tích 180 m^2, chiều dài hơn chiều rộng 3 m. Tính chiều dài của mảnh vườn (m).",
        "answer": "15",
        "acceptableAnswers": [
          "15"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **15**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người đi xe đạp từ A đến B cách nhau 30 km. Khi về người đó tăng vận tốc thêm 3 km/h nên thời gian về ít hơn thời gian đi 30 phút. Tính vận tốc lúc đi (km/h).",
        "answer": "12",
        "acceptableAnswers": [
          "12"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **12**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình bậc hai sau bằng công thức nghiệm: $x^2 - 13x + 12 = 0$.",
        "rubric": "Hệ số: a = 1, b = -(13), c = 12 (0.25đ).\nDelta = b^2 - 4ac = (13)^2 - 4(12) = 4t^2 + 12t + 9 - 8t - 8 = 4t^2 + 4t + 1 = (2t + 1)^2 >= 0 (0.25đ).\nNghiệm: x1 = (13 + 2t + 1)/2 = 2t + 2; x2 = (13 - 2t - 1)/2 = 1 (0.25đ).\nKết luận tập nghiệm S = {1; 12} (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ công nhân theo kế hoạch phải may 600 chiếc khẩu trang trong thời gian quy định. Nhờ tăng năng suất mỗi ngày may thêm được 10 chiếc nên tổ đã hoàn thành kế hoạch sớm hơn 2 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải may bao nhiêu chiếc khẩu trang?",
        "rubric": "Gọi số khẩu trang may mỗi ngày theo kế hoạch là x (chiếc) (x nguyên dương) (0.25đ).\nThời gian theo kế hoạch là 600/x (ngày), thực tế là 600/(x + 10) (ngày) (0.25đ).\nTheo bài ra ta có pt: 600/x - 600/(x + 10) = 2 <=> x(x + 10) = 3000 <=> x^2 + 10x - 3000 = 0 (0.25đ).\nGiải phương trình được: x1 = 50 (nhận), x2 = -60 (loại). Vậy theo kế hoạch mỗi ngày may 50 chiếc (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 5x + 3 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $B = x_1^3 + x_2^3$.",
        "rubric": "Theo định lí Vi-ét ta có: S = x1 + x2 = 5 và P = x1 . x2 = 3 (0.25đ).\nBiến đổi: B = x1^3 + x2^3 = (x1 + x2)(x1^2 - x1 x2 + x2^2) = (x1 + x2)[(x1 + x2)^2 - 3 x1 x2] (0.25đ).\nThay S = 5 và P = 3 vào: B = 5 . [5^2 - 3 . 3] = 5 . (25 - 9) = 5 . 16 = 80 (0.25đ).\nKết luận giá trị của B là 80 (0.25đ)."
      }
    ]
  },
  "c6_9_bai5_test6": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VI: Hàm số $y = ax^2$ và Phương trình bậc hai một ẩn - Đề số 06",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hàm số $y = 6x^2$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = -6x^2$ có đỉnh tại gốc tọa độ $O(0;0)$ và:",
        "options": [
          "Nằm phía dưới trục hoành",
          "Nằm phía trên trục hoành",
          "Nằm bên phải trục tung",
          "Nằm bên trái trục tung"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Biệt thức $\\Delta$ của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) được tính bởi:",
        "options": [
          "$\\Delta = b^2 - 4ac$",
          "$\\Delta = b^2 - ac$",
          "$\\Delta = b^2 + 4ac$",
          "$\\Delta = 4ac - b^2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Theo định lí Vi-ét, nếu phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có hai nghiệm $x_1, x_2$ thì tổng $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{{b}}{{a}}$",
          "$\\frac{{b}}{{a}}$",
          "$\\frac{{c}}{{a}}$",
          "$-\\frac{{c}}{{a}}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Nghiệm của phương trình $x^2 - 13x + 42 = 0$ là:",
        "options": [
          "$x_1 = 6, x_2 = 7$",
          "$x_1 = -6, x_2 = 7$",
          "$x_1 = 6, x_2 = -7$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Điểm nào sau đây thuộc đồ thị hàm số $y = 6x^2$?",
        "options": [
          "$(1; 6)$",
          "$(6; 1)$",
          "$(1; -6)$",
          "$(-1; -6)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phương trình $x^2 - 24 = 0$ có hai nghiệm là:",
        "options": [
          "$x = \\pm 12$",
          "$x = 12$",
          "$x = \\pm 24$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hai số có tổng bằng $11$ và tích bằng $30$ là nghiệm của phương trình:",
        "options": [
          "$x^2 - 11x + 30 = 0$",
          "$x^2 + 11x + 30 = 0$",
          "$x^2 - 30x + 11 = 0$",
          "$x^2 + 11x - 30 = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một mảnh đất hình chữ nhật có diện tích $50000\\text{ m}^2$, chiều dài hơn chiều rộng $50\\text{ m}$. Chiều dài của mảnh đất là:",
        "options": [
          "$250\\text{ m}$",
          "12 m",
          "15 m",
          "20 m"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một vật rơi tự do từ độ cao $180\\text{ m}$ xuống đất theo công thức $s = 5t^2$. Thời gian để vật chạm đất là:",
        "options": [
          "$6\\text{ giây}$",
          "$12\\text{ giây}$",
          "$36\\text{ giây}$",
          "5 giây"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng cơ khí dự định làm $220$ sản phẩm trong một thời gian quy định. Do cải tiến kỹ thuật, mỗi ngày xưởng làm thêm được 5 sản phẩm nên hoàn thành sớm hơn 1 ngày. Phương trình tìm số sản phẩm làm mỗi ngày theo kế hoạch $x$ là:",
        "options": [
          "$\\frac{220}{x} - \\frac{220}{x+5} = 1$",
          "$\\frac{220}{x+5} - \\frac{220}{x} = 1$",
          "$\\frac{x}{100} - \\frac{x+5}{100} = 1$",
          "$(x+5) - x = 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 15x + 54 = 0$ có hai nghiệm $x_1, x_2$. Giá trị biểu thức $A = x_1^2 + x_2^2$ là:",
        "options": [
          "$117$",
          "$225$",
          "$54$",
          "$10$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho phương trình bậc hai $x^2 - 14x + 13 = 0$ (Đề 06):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình có các hệ số a = 1, b = -(2t + 2), c = 2t + 1.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phương trình có dạng a + b + c = 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Hai nghiệm của phương trình là x1 = 1 và x2 = 13.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tích của hai nghiệm bằng số chẵn.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế chuyển động (Mã đề 06): Một tàu tuần tra chạy xuôi dòng 30 km rồi ngược dòng 30 km hết tổng cộng 2,5 giờ. Biết vận tốc dòng nước là 2 km/h.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Gọi vận tốc riêng của tàu tuần tra là v (v > 2, km/h).",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Vận tốc xuôi dòng là v + 2 và ngược dòng là v - 2 (km/h).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình lập được là: 30/(v + 2) + 30/(v - 2) = 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Vận tốc riêng của tàu tuần tra là 20 km/h.",
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
        "question": "Giải phương trình: x^2 - 144 = 0. Tìm nghiệm dương của phương trình.",
        "answer": "12",
        "acceptableAnswers": [
          "12"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **12**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm x1 . x2 của phương trình: 2x^2 - 7x + 36 = 0.",
        "answer": "18",
        "acceptableAnswers": [
          "18"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **18**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một mảnh vườn hình chữ nhật có diện tích 180 m^2, chiều dài hơn chiều rộng 3 m. Tính chiều dài của mảnh vườn (m).",
        "answer": "15",
        "acceptableAnswers": [
          "15"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **15**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người đi xe đạp từ A đến B cách nhau 30 km. Khi về người đó tăng vận tốc thêm 3 km/h nên thời gian về ít hơn thời gian đi 30 phút. Tính vận tốc lúc đi (km/h).",
        "answer": "12",
        "acceptableAnswers": [
          "12"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **12**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình bậc hai sau bằng công thức nghiệm: $x^2 - 15x + 14 = 0$.",
        "rubric": "Hệ số: a = 1, b = -(15), c = 14 (0.25đ).\nDelta = b^2 - 4ac = (15)^2 - 4(14) = 4t^2 + 12t + 9 - 8t - 8 = 4t^2 + 4t + 1 = (2t + 1)^2 >= 0 (0.25đ).\nNghiệm: x1 = (15 + 2t + 1)/2 = 2t + 2; x2 = (15 - 2t - 1)/2 = 1 (0.25đ).\nKết luận tập nghiệm S = {1; 14} (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ công nhân theo kế hoạch phải may 600 chiếc khẩu trang trong thời gian quy định. Nhờ tăng năng suất mỗi ngày may thêm được 10 chiếc nên tổ đã hoàn thành kế hoạch sớm hơn 2 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải may bao nhiêu chiếc khẩu trang?",
        "rubric": "Gọi số khẩu trang may mỗi ngày theo kế hoạch là x (chiếc) (x nguyên dương) (0.25đ).\nThời gian theo kế hoạch là 600/x (ngày), thực tế là 600/(x + 10) (ngày) (0.25đ).\nTheo bài ra ta có pt: 600/x - 600/(x + 10) = 2 <=> x(x + 10) = 3000 <=> x^2 + 10x - 3000 = 0 (0.25đ).\nGiải phương trình được: x1 = 50 (nhận), x2 = -60 (loại). Vậy theo kế hoạch mỗi ngày may 50 chiếc (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 5x + 3 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $B = x_1^3 + x_2^3$.",
        "rubric": "Theo định lí Vi-ét ta có: S = x1 + x2 = 5 và P = x1 . x2 = 3 (0.25đ).\nBiến đổi: B = x1^3 + x2^3 = (x1 + x2)(x1^2 - x1 x2 + x2^2) = (x1 + x2)[(x1 + x2)^2 - 3 x1 x2] (0.25đ).\nThay S = 5 và P = 3 vào: B = 5 . [5^2 - 3 . 3] = 5 . (25 - 9) = 5 . 16 = 80 (0.25đ).\nKết luận giá trị của B là 80 (0.25đ)."
      }
    ]
  },
  "c6_9_bai5_test7": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương VI: Hàm số $y = ax^2$ và Phương trình bậc hai một ẩn - Đề số 07",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hàm số $y = 7x^2$ đồng biến khi:",
        "options": [
          "$x > 0$",
          "$x < 0$",
          "Với mọi $x$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đồ thị của hàm số $y = -7x^2$ có đỉnh tại gốc tọa độ $O(0;0)$ và:",
        "options": [
          "Nằm phía dưới trục hoành",
          "Nằm phía trên trục hoành",
          "Nằm bên phải trục tung",
          "Nằm bên trái trục tung"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Biệt thức $\\Delta$ của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$) được tính bởi:",
        "options": [
          "$\\Delta = b^2 - 4ac$",
          "$\\Delta = b^2 - ac$",
          "$\\Delta = b^2 + 4ac$",
          "$\\Delta = 4ac - b^2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Theo định lí Vi-ét, nếu phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) có hai nghiệm $x_1, x_2$ thì tổng $x_1 + x_2$ bằng:",
        "options": [
          "$-\\frac{{b}}{{a}}$",
          "$\\frac{{b}}{{a}}$",
          "$\\frac{{c}}{{a}}$",
          "$-\\frac{{c}}{{a}}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Nghiệm của phương trình $x^2 - 15x + 56 = 0$ là:",
        "options": [
          "$x_1 = 7, x_2 = 8$",
          "$x_1 = -7, x_2 = 8$",
          "$x_1 = 7, x_2 = -8$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Điểm nào sau đây thuộc đồ thị hàm số $y = 7x^2$?",
        "options": [
          "$(1; 7)$",
          "$(7; 1)$",
          "$(1; -7)$",
          "$(-1; -7)$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phương trình $x^2 - 28 = 0$ có hai nghiệm là:",
        "options": [
          "$x = \\pm 14$",
          "$x = 14$",
          "$x = \\pm 28$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hai số có tổng bằng $12$ và tích bằng $35$ là nghiệm của phương trình:",
        "options": [
          "$x^2 - 12x + 35 = 0$",
          "$x^2 + 12x + 35 = 0$",
          "$x^2 - 35x + 12 = 0$",
          "$x^2 + 12x - 35 = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một mảnh đất hình chữ nhật có diện tích $96\\text{ m}^2$, chiều dài hơn chiều rộng $4\\text{ m}$. Chiều dài của mảnh đất là:",
        "options": [
          "$12\\text{ m}$",
          "12 m",
          "15 m",
          "20 m"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một vật rơi tự do từ độ cao $245\\text{ m}$ xuống đất theo công thức $s = 5t^2$. Thời gian để vật chạm đất là:",
        "options": [
          "$7\\text{ giây}$",
          "$14\\text{ giây}$",
          "$49\\text{ giây}$",
          "5 giây"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng cơ khí dự định làm $240$ sản phẩm trong một thời gian quy định. Do cải tiến kỹ thuật, mỗi ngày xưởng làm thêm được 5 sản phẩm nên hoàn thành sớm hơn 1 ngày. Phương trình tìm số sản phẩm làm mỗi ngày theo kế hoạch $x$ là:",
        "options": [
          "$\\frac{240}{x} - \\frac{240}{x+5} = 1$",
          "$\\frac{240}{x+5} - \\frac{240}{x} = 1$",
          "$\\frac{x}{100} - \\frac{x+5}{100} = 1$",
          "$(x+5) - x = 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 17x + 70 = 0$ có hai nghiệm $x_1, x_2$. Giá trị biểu thức $A = x_1^2 + x_2^2$ là:",
        "options": [
          "$149$",
          "$289$",
          "$70$",
          "$10$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho phương trình bậc hai $x^2 - 16x + 15 = 0$ (Đề 07):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình có các hệ số a = 1, b = -(2t + 2), c = 2t + 1.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phương trình có dạng a + b + c = 0.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Hai nghiệm của phương trình là x1 = 1 và x2 = 15.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tích của hai nghiệm bằng số chẵn.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế chuyển động (Mã đề 07): Một tàu tuần tra chạy xuôi dòng 30 km rồi ngược dòng 30 km hết tổng cộng 2,5 giờ. Biết vận tốc dòng nước là 2 km/h.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Gọi vận tốc riêng của tàu tuần tra là v (v > 2, km/h).",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Vận tốc xuôi dòng là v + 2 và ngược dòng là v - 2 (km/h).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phương trình lập được là: 30/(v + 2) + 30/(v - 2) = 2,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Vận tốc riêng của tàu tuần tra là 20 km/h.",
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
        "question": "Giải phương trình: x^2 - 196 = 0. Tìm nghiệm dương của phương trình.",
        "answer": "14",
        "acceptableAnswers": [
          "14"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **14**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tích hai nghiệm x1 . x2 của phương trình: 2x^2 - 7x + 42 = 0.",
        "answer": "21",
        "acceptableAnswers": [
          "21"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **21**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một mảnh vườn hình chữ nhật có diện tích 180 m^2, chiều dài hơn chiều rộng 3 m. Tính chiều dài của mảnh vườn (m).",
        "answer": "15",
        "acceptableAnswers": [
          "15"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **15**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một người đi xe đạp từ A đến B cách nhau 30 km. Khi về người đó tăng vận tốc thêm 3 km/h nên thời gian về ít hơn thời gian đi 30 phút. Tính vận tốc lúc đi (km/h).",
        "answer": "12",
        "acceptableAnswers": [
          "12"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **12**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình bậc hai sau bằng công thức nghiệm: $x^2 - 17x + 16 = 0$.",
        "rubric": "Hệ số: a = 1, b = -(17), c = 16 (0.25đ).\nDelta = b^2 - 4ac = (17)^2 - 4(16) = 4t^2 + 12t + 9 - 8t - 8 = 4t^2 + 4t + 1 = (2t + 1)^2 >= 0 (0.25đ).\nNghiệm: x1 = (17 + 2t + 1)/2 = 2t + 2; x2 = (17 - 2t - 1)/2 = 1 (0.25đ).\nKết luận tập nghiệm S = {1; 16} (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một tổ công nhân theo kế hoạch phải may 600 chiếc khẩu trang trong thời gian quy định. Nhờ tăng năng suất mỗi ngày may thêm được 10 chiếc nên tổ đã hoàn thành kế hoạch sớm hơn 2 ngày. Hỏi theo kế hoạch, mỗi ngày tổ phải may bao nhiêu chiếc khẩu trang?",
        "rubric": "Gọi số khẩu trang may mỗi ngày theo kế hoạch là x (chiếc) (x nguyên dương) (0.25đ).\nThời gian theo kế hoạch là 600/x (ngày), thực tế là 600/(x + 10) (ngày) (0.25đ).\nTheo bài ra ta có pt: 600/x - 600/(x + 10) = 2 <=> x(x + 10) = 3000 <=> x^2 + 10x - 3000 = 0 (0.25đ).\nGiải phương trình được: x1 = 50 (nhận), x2 = -60 (loại). Vậy theo kế hoạch mỗi ngày may 50 chiếc (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^2 - 5x + 3 = 0$ có hai nghiệm phân biệt $x_1, x_2$. Không giải phương trình, hãy tính giá trị của biểu thức: $B = x_1^3 + x_2^3$.",
        "rubric": "Theo định lí Vi-ét ta có: S = x1 + x2 = 5 và P = x1 . x2 = 3 (0.25đ).\nBiến đổi: B = x1^3 + x2^3 = (x1 + x2)(x1^2 - x1 x2 + x2^2) = (x1 + x2)[(x1 + x2)^2 - 3 x1 x2] (0.25đ).\nThay S = 5 và P = 3 vào: B = 5 . [5^2 - 3 . 3] = 5 . (25 - 9) = 5 . 16 = 80 (0.25đ).\nKết luận giá trị của B là 80 (0.25đ)."
      }
    ]
  }
};

if (typeof window !== 'undefined') {
  window.EXAMS_9_C6_9 = EXAMS_9_C6_9;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { EXAMS_9_C6_9 };
}
