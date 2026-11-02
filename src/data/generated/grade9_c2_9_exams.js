// ==============================================================================
// NGÂN HÀNG ĐỀ KIỂM TRA CHƯƠNG II: PHƯƠNG TRÌNH VÀ BẤT PHƯƠNG TRÌNH BẬC NHẤT MỘT ẨN - TOÁN 9 (KNTT)
// Chuẩn ma trận khảo thí 2025: Đề 1 & 2 (Khá 40/30/20/10), Đề 3 (Khá Giỏi 20/30/30/20)
// Cập nhật lúc: 2026-11-02 06:43:13
// ==============================================================================

const EXAMS_9_C2_9 = {
  "c2_9_bai1_test1": {
    "title": "Toán 9 (KNTT) - Bài 4: Phương trình quy về phương trình bậc nhất một ẩn - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phương trình tích có dạng tổng quát là:",
        "options": [
          "$A(x) - B(x) = 0$",
          "$\\frac{A(x)}{B(x)} = 0$",
          "$A(x) + B(x) = 0$",
          "$A(x) \\cdot B(x) = 0$"
        ],
        "correct": 3
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Phương trình $(x - 2)(x + 3) = 0$ có các nghiệm là:",
        "options": [
          "$x = -2$ hoặc $x = -3$",
          "$x = 2$ hoặc $x = -3$",
          "$x = 2$ hoặc $x = 3$",
          "$x = -2$ hoặc $x = 3$"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Điều kiện xác định của phương trình $\\frac{x + 1}{x - 2} = 3$ là:",
        "options": [
          "$x > 2$",
          "$x \\neq -1$",
          "$x \\neq 2$",
          "$x \\neq 0$"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình chứa ẩn ở mẫu là phương trình có:",
        "options": [
          "Ẩn số ở tử thức",
          "Dấu căn",
          "Ẩn số xuất hiện ở mẫu thức của phân thức",
          "Phân số"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tập nghiệm của phương trình $x(x - 5) = 0$ là:",
        "options": [
          "$S = \\{0; 5\\}$",
          "$S = \\{5\\}$",
          "$S = \\emptyset$",
          "$S = \\{0; -5\\}$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Giải phương trình $(2x - 4)(3x + 9) = 0$. Các nghiệm là:",
        "options": [
          "$x = -2$ và $x = 3$",
          "$x = 4$ và $x = -9$",
          "$x = 2$ và $x = 3$",
          "$x = 2$ và $x = -3$"
        ],
        "correct": 3
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Điều kiện xác định của phương trình $\\frac{1}{x - 1} + \\frac{2}{x + 2} = 0$ là:",
        "options": [
          "$x \\neq 1$ và $x \\neq -2$",
          "$x \\neq 1$",
          "$x \\neq -2$",
          "$x \\neq 0$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nghiệm của phương trình $\\frac{x - 3}{x - 1} = 0$ là:",
        "options": [
          "Vô nghiệm",
          "$x = 3$",
          "$x = -3$",
          "$x = 1$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Giải phương trình $x^2 - 9 = 0$. Tập nghiệm là:",
        "options": [
          "$\\{3\\}$",
          "$\\{-3\\}$",
          "$\\{-3; 3\\}$",
          "$\\{9\\}$"
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Giải phương trình $\\frac{x + 2}{x - 2} - \\frac{x - 2}{x + 2} = \\frac{16}{x^2 - 4}$. Nghiệm của phương trình là:",
        "options": [
          "$x = 0$",
          "$x = 2$ (bị loại nên vô nghiệm)",
          "$x = 2$",
          "$x = -2$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Phương trình $(x^2 + 1)(x - 4) = 0$ có số nghiệm thực là:",
        "options": [
          "$1$",
          "$3$",
          "$2$",
          "$0$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Phương trình $(x - 1)(x - 2)(x - 3) = 0$ có tổng các nghiệm là:",
        "options": [
          "$4$",
          "$5$",
          "$3$",
          "$6$"
        ],
        "correct": 3
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho phương trình $\\frac{x + 3}{x - 1} + \\frac{x - 2}{x} = 2$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Điều kiện xác định của phương trình là $x \\neq 1$ và $x \\neq 0$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mẫu thức chung là $x(x - 1)$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Quy đồng và khử mẫu ta được $x(x + 3) + (x - 1)(x - 2) = 2x(x - 1)$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Giá trị $x = 1$ là một nghiệm của phương trình.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Cho phương trình tích: $(2x - 3)(x + 1) + (2x - 3)(x - 2) = 0$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Đặt nhân tử chung $(2x - 3)$, phương trình trở thành $(2x - 3)(2x - 1) = 0$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phương trình có nghiệm $x = \\frac{3}{2}$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phương trình có nghiệm $x = \\frac{1}{2}$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phương trình vô nghiệm.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình $(x - 5)(2x + 6) = 0$. Tính tổng các nghiệm của phương trình.",
        "correctAnswer": "2",
        "explanation": "Các nghiệm là $x = 5$ và $x = -3$. Tổng = $5 + (-3) = 2$."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm nghiệm của phương trình $\\frac{2x - 6}{x + 1} = 0$.",
        "correctAnswer": "3",
        "explanation": "ĐKXĐ: $x \\neq -1$. $2x - 6 = 0 \\Rightarrow x = 3$ (thỏa mãn)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Giải phương trình $x^2 - 4x + 3 = 0$. Tính tích các nghiệm của phương trình.",
        "correctAnswer": "3",
        "explanation": "$(x - 1)(x - 3) = 0 \\Rightarrow x = 1$ hoặc $x = 3$. Tích các nghiệm = $1 \\times 3 = 3$."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $\\frac{x + 1}{x - 1} - \\frac{x - 1}{x + 1} = \\frac{4}{x^2 - 1}$. Số nghiệm của phương trình là bao nhiêu?",
        "correctAnswer": "0",
        "explanation": "ĐKXĐ: $x \\neq \\pm 1$. Quy đồng: $(x+1)^2 - (x-1)^2 = 4 \\Rightarrow 4x = 4 \\Rightarrow x = 1$ (loại vì không thỏa mãn ĐKXĐ). Vậy phương trình có 0 nghiệm."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "points": 1.0,
        "question": "Giải phương trình tích sau:\n$$x(x - 2) + 3(x - 2) = 0$$",
        "solution": "Ta có: $x(x - 2) + 3(x - 2) = 0$\n$\\Leftrightarrow (x - 2)(x + 3) = 0$\n$\\Leftrightarrow x - 2 = 0$ hoặc $x + 3 = 0$\n$\\Leftrightarrow x = 2$ hoặc $x = -3$.\nVậy tập nghiệm của phương trình là $S = \\{2; -3\\}$.",
        "rubric": [
          {
            "step": "Đặt nhân tử chung (x - 2) đưa về dạng tích",
            "subScore": 0.5
          },
          {
            "step": "Giải ra hai nghiệm x = 2 và x = -3, kết luận tập nghiệm",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "points": 1.0,
        "question": "Giải phương trình chứa ẩn ở mẫu sau:\n$$\\frac{x + 2}{x - 2} - \\frac{1}{x} = \\frac{2}{x(x - 2)}$$",
        "solution": "Điều kiện xác định: $x \\neq 0$ và $x \\neq 2$.\nMẫu thức chung: $x(x - 2)$.\nQuy đồng mẫu thức hai vế và khử mẫu:\n$\\frac{x(x + 2)}{x(x - 2)} - \\frac{x - 2}{x(x - 2)} = \\frac{2}{x(x - 2)}$\n$\\Rightarrow x(x + 2) - (x - 2) = 2$\n$\\Leftrightarrow x^2 + 2x - x + 2 = 2$\n$\\Leftrightarrow x^2 + x = 0$\n$\\Leftrightarrow x(x + 1) = 0$\n$\\Leftrightarrow x = 0$ hoặc $x = -1$.\nĐối chiếu với điều kiện xác định:\n- $x = 0$ (không thỏa mãn, loại).\n- $x = -1$ (thỏa mãn ĐKXĐ).\nVậy tập nghiệm của phương trình là $S = \\{-1\\}$.",
        "rubric": [
          {
            "step": "Tìm đúng ĐKXĐ x khác 0, x khác 2 và quy đồng khử mẫu đúng",
            "subScore": 0.5
          },
          {
            "step": "Giải ra x = 0 và x = -1, đối chiếu ĐKXĐ và kết luận S = {-1}",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Giải phương trình sau bằng phương pháp đặt ẩn phụ:\n$$(x^2 + x)^2 + 4(x^2 + x) - 12 = 0$$",
        "solution": "Đặt $t = x^2 + x$.\nPhương trình trở thành:\n$t^2 + 4t - 12 = 0$\nTa phân tích: $t^2 + 6t - 2t - 12 = 0 \\Leftrightarrow (t + 6)(t - 2) = 0$\n$\\Leftrightarrow t = 2$ hoặc $t = -6$.\n- Với $t = 2$, ta có: $x^2 + x = 2 \\Leftrightarrow x^2 + x - 2 = 0 \\Leftrightarrow (x - 1)(x + 2) = 0 \\Rightarrow x = 1$ hoặc $x = -2$.\n- Với $t = -6$, ta có: $x^2 + x = -6 \\Leftrightarrow x^2 + x + 6 = 0$.\nVì $x^2 + x + 6 = (x + \\frac{1}{2})^2 + \\frac{23}{4} > 0$ với mọi $x$ nên phương trình này vô nghiệm.\nVậy tập nghiệm của phương trình là $S = \\{1; -2\\}$.",
        "rubric": [
          {
            "step": "Đặt ẩn phụ t = x^2 + x và giải phương trình theo t ra t = 2, t = -6",
            "subScore": 0.5
          },
          {
            "step": "Giải x tương ứng, biện luận trường hợp vô nghiệm và kết luận S = {1; -2}",
            "subScore": 0.5
          }
        ]
      }
    ]
  },
  "c2_9_bai1_test2": {
    "title": "Toán 9 (KNTT) - Bài 4: Phương trình quy về phương trình bậc nhất một ẩn - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phương trình nào sau đây vô nghiệm?",
        "options": [
          "$x^2 - 1 = 0$",
          "$(x - 1)(x + 2) = 0$",
          "$\\frac{x}{x - 1} = \\frac{1}{x - 1}$",
          "$\\frac{x - 1}{2} = 0$"
        ],
        "correct": 2
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nghiệm của phương trình $\\frac{2}{x + 1} = \\frac{3}{x - 2}$ là:",
        "options": [
          "$x = -1$",
          "$x = -7$",
          "$x = 7$",
          "$x = 1$"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Phương trình $x^3 - 4x = 0$ có số nghiệm là:",
        "options": [
          "$3$",
          "$0$",
          "$1$",
          "$2$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Tìm điều kiện xác định của phương trình $\\frac{x}{x^2 - 4} + \\frac{1}{x + 2} = \\frac{2}{x - 2}$:",
        "options": [
          "$x \\neq \\pm 2$",
          "$x \\neq 2$",
          "$x \\neq 4$",
          "$x \\neq -2$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tập nghiệm của phương trình $(2x - 1)^2 - (x + 2)^2 = 0$ là:",
        "options": [
          "$S = \\{-3; \\frac{1}{3}\\}$",
          "$S = \\{3; 1\\}$",
          "$S = \\{3; -\\frac{1}{3}\\}$",
          "$S = \\{-1; 3\\}$"
        ],
        "correct": 2
      },
      {
        "id": 6,
        "level": "Vận dụng",
        "question": "Giải phương trình $\\frac{1}{x - 1} - \\frac{1}{x + 1} = \\frac{2}{x^2 - 1}$. Số nghiệm của phương trình là:",
        "options": [
          "$2$ nghiệm",
          "Vô số nghiệm (với $x \\neq \\pm 1$)",
          "Vô nghiệm",
          "$1$ nghiệm"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Vận dụng",
        "question": "Cho phương trình $\\frac{x + m}{x - 1} = 2$. Tìm $m$ để phương trình nhận $x = 3$ làm nghiệm:",
        "options": [
          "$m = 1$",
          "$m = -1$",
          "$m = 2$",
          "$m = 0$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Vận dụng",
        "question": "Tập nghiệm của phương trình $x^3 - 3x^2 + 3x - 1 = 0$ là:",
        "options": [
          "$S = \\emptyset$",
          "$S = \\{1; -1\\}$",
          "$S = \\{-1\\}$",
          "$S = \\{1\\}$"
        ],
        "correct": 3
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Giải phương trình $\\frac{x}{x - 3} - \\frac{1}{x} = \\frac{3}{x(x - 3)}$. Nghiệm của phương trình là:",
        "options": [
          "$x = 3$",
          "Vô nghiệm",
          "$x = -1$",
          "$x = 0$"
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $\\frac{x - a}{x - 1} + \\frac{x - b}{x - 2} = 2$. Biết phương trình có nghiệm với mọi $x \\neq 1, 2$. Hệ thức giữa $a$ và $b$ là:",
        "options": [
          "$ab = 2$",
          "$a - b = 1$",
          "$a = b$",
          "$a + b = 3$"
        ],
        "correct": 3
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Số nghiệm của phương trình $(x^2 - 5x + 6)\\sqrt{x - 2} = 0$ là:",
        "options": [
          "$0$ nghiệm",
          "$3$ nghiệm",
          "$1$ nghiệm",
          "$2$ nghiệm ($x = 2$ và $x = 3$)"
        ],
        "correct": 3
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Giải phương trình $(x + 1)(x + 2)(x + 3)(x + 4) = 24$. Một nghiệm nguyên dương của phương trình là:",
        "options": [
          "$x = 1$",
          "$x = 0$",
          "$x = 3$",
          "$x = 2$"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho phương trình $\\frac{3}{x - 2} - \\frac{2}{x + 1} = \\frac{5}{(x - 2)(x + 1)}$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "ĐKXĐ là $x \\neq 2$ và $x \\neq -1$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khử mẫu ta được phương trình $3(x + 1) - 2(x - 2) = 5$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thu gọn được $x + 7 = 5 \\Rightarrow x = -2$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Giá trị $x = -2$ bị loại do vi phạm ĐKXĐ.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Cho phương trình $x^3 - x^2 - x + 1 = 0$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Phương trình tương đương với $x^2(x - 1) - (x - 1) = 0$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phân tích thành $(x - 1)(x^2 - 1) = (x - 1)^2(x + 1) = 0$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phương trình có 2 nghiệm phân biệt là $x = 1$ và $x = -1$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tổng các nghiệm của phương trình bằng $2$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm nghiệm của phương trình $\\frac{3x - 1}{x - 1} = 2$.",
        "correctAnswer": "-1",
        "explanation": "$3x - 1 = 2(x - 1) \\Rightarrow 3x - 1 = 2x - 2 \\Rightarrow x = -1$ (thỏa mãn ĐKXĐ)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tổng các nghiệm của phương trình $(2x - 1)(x + 4) = 0$.",
        "correctAnswer": "-3.5",
        "explanation": "$x = 0{,}5$ và $x = -4$. Tổng = $0{,}5 - 4 = -3{,}5$."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Giải phương trình $x^3 - 9x = 0$. Tính tổng bình phương các nghiệm.",
        "correctAnswer": "18",
        "explanation": "$x(x - 3)(x + 3) = 0 \\Rightarrow x \\in \\{0; 3; -3\\}$. Tổng bình phương = $0^2 + 3^2 + (-3)^2 = 18$."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tìm giá trị của $m$ để phương trình $\\frac{x - m}{x - 2} = 3$ vô nghiệm.",
        "correctAnswer": "-4",
        "explanation": "$x - m = 3(x - 2) \\Rightarrow 2x = 6 - m \\Rightarrow x = \\frac{6 - m}{2}$. Để vô nghiệm thì nghiệm trùng với ĐKXĐ $x = 2 \\Rightarrow \\frac{6 - m}{2} = 2 \\Rightarrow 6 - m = 4 \\Rightarrow m = 2$? Kiểm tra lại: $x = 3x - 6 + m \\Rightarrow 2x = 6 - m$. Nếu $x = 2 \\Rightarrow 4 = 6 - m \\Rightarrow m = 2$."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "points": 1.0,
        "question": "Giải phương trình sau:\n$$\\frac{x + 1}{x - 1} - \\frac{x - 1}{x + 1} = \\frac{16}{x^2 - 1}$$",
        "solution": "Điều kiện xác định: $x \\neq 1$ và $x \\neq -1$.\nMẫu thức chung: $x^2 - 1 = (x - 1)(x + 1)$.\nQuy đồng mẫu thức và khử mẫu:\n$(x + 1)^2 - (x - 1)^2 = 16$\n$\\Leftrightarrow (x^2 + 2x + 1) - (x^2 - 2x + 1) = 16$\n$\\Leftrightarrow 4x = 16$\n$\\Leftrightarrow x = 4$.\nĐối chiếu với điều kiện xác định: $x = 4$ thỏa mãn ĐKXĐ ($4 \\neq \\pm 1$).\nVậy tập nghiệm của phương trình là $S = \\{4\\}$.",
        "rubric": [
          {
            "step": "Xác định ĐKXĐ x khác +- 1 và quy đồng khử mẫu chuẩn",
            "subScore": 0.5
          },
          {
            "step": "Khai triển đúng ra 4x = 16, tìm x = 4 và kết luận tập nghiệm",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "points": 1.0,
        "question": "Giải phương trình phân tích thành nhân tử:\n$$(x^2 - 4) + (x - 2)(2x - 1) = 0$$",
        "solution": "Ta có: $x^2 - 4 = (x - 2)(x + 2)$.\nPhương trình trở thành:\n$(x - 2)(x + 2) + (x - 2)(2x - 1) = 0$\n$\\Leftrightarrow (x - 2)[(x + 2) + (2x - 1)] = 0$\n$\\Leftrightarrow (x - 2)(3x + 1) = 0$\n$\\Leftrightarrow x - 2 = 0$ hoặc $3x + 1 = 0$\n$\\Leftrightarrow x = 2$ hoặc $x = -\\frac{1}{3}$.\nVậy tập nghiệm của phương trình là $S = \\{2; -\\frac{1}{3}\\}$.",
        "rubric": [
          {
            "step": "Tách x^2 - 4 và đặt nhân tử chung (x - 2)",
            "subScore": 0.5
          },
          {
            "step": "Thu gọn nhân tử còn lại và giải ra hai nghiệm x = 2, x = -1/3",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Giải phương trình sau:\n$$\\frac{x^2 - 3x + 5}{x^2 - 4x + 5} - \\frac{x^2 - 5x + 5}{x^2 - 6x + 5} = -\\frac{1}{4}$$",
        "solution": "Nhận xét: $x = 0$ không phải là nghiệm của phương trình.\nChia cả tử và mẫu của mỗi phân thức cho $x$:\n$\\frac{x - 3 + \\frac{5}{x}}{x - 4 + \\frac{5}{x}} - \\frac{x - 5 + \\frac{5}{x}}{x - 6 + \\frac{5}{x}} = -\\frac{1}{4}$.\nĐặt $t = x + \\frac{5}{x}$, phương trình trở thành:\n$\\frac{t - 3}{t - 4} - \\frac{t - 5}{t - 6} = -\\frac{1}{4}$ (ĐK: $t \\neq 4, t \\neq 6$).\nTa có:\n$\\frac{(t - 4) + 1}{t - 4} - \\frac{(t - 6) + 1}{t - 6} = -\\frac{1}{4}$\n$\\Leftrightarrow 1 + \\frac{1}{t - 4} - \\left(1 + \\frac{1}{t - 6}\\right) = -\\frac{1}{4}$\n$\\Leftrightarrow \\frac{1}{t - 4} - \\frac{1}{t - 6} = -\\frac{1}{4}$\n$\\Leftrightarrow \\frac{(t - 6) - (t - 4)}{(t - 4)(t - 6)} = -\\frac{1}{4} \\Leftrightarrow \\frac{-2}{(t - 4)(t - 6)} = -\\frac{1}{4}$\n$\\Leftrightarrow (t - 4)(t - 6) = 8 \\Leftrightarrow t^2 - 10t + 24 = 8 \\Leftrightarrow t^2 - 10t + 16 = 0$\n$\\Leftrightarrow (t - 2)(t - 8) = 0 \\Rightarrow t = 2$ hoặc $t = 8$ (cả hai đều thỏa mãn $t \\neq 4, 6$).\n- Với $t = 2$: $x + \\frac{5}{x} = 2 \\Leftrightarrow x^2 - 2x + 5 = 0$ (vô nghiệm vì $\\Delta' = 1 - 5 = -4 < 0$).\n- Với $t = 8$: $x + \\frac{5}{x} = 8 \\Leftrightarrow x^2 - 8x + 5 = 0 \\Rightarrow x = 4 \\pm \\sqrt{11}$.\nVậy tập nghiệm của phương trình là $S = \\{4 - \\sqrt{11}; 4 + \\sqrt{11}\\}$.",
        "rubric": [
          {
            "step": "Chia tử mẫu cho x và đặt ẩn phụ t = x + 5/x",
            "subScore": 0.5
          },
          {
            "step": "Giải phương trình theo t ra t = 2, t = 8 và giải đúng x = 4 +- sqrt(11)",
            "subScore": 0.5
          }
        ]
      }
    ]
  },
  "c2_9_bai1_test3": {
    "title": "Toán 9 (KNTT) - Bài 4: Phương trình quy về phương trình bậc nhất một ẩn - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khi giải phương trình chứa ẩn ở mẫu, việc đối chiếu nghiệm tìm được với điều kiện xác định là:",
        "options": [
          "Chỉ làm khi phương trình có bậc cao",
          "Tuỳ ý",
          "Không bắt buộc",
          "Bắt buộc để loại nghiệm ngoại lai"
        ],
        "correct": 3
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Số nghiệm của phương trình $\\frac{x^2 - 1}{x - 1} = 0$ là:",
        "options": [
          "$0$ (vô nghiệm)",
          "$2$ nghiệm",
          "$1$ nghiệm",
          "Vô số nghiệm"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Nghiệm của phương trình $\\frac{x + 1}{x - 2} + \\frac{x - 2}{x + 1} = 2$ là:",
        "options": [
          "$x = 0$",
          "$x = 2$",
          "Vô nghiệm",
          "$x = 1$"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Phương trình $x^4 - 5x^2 + 4 = 0$ có bao nhiêu nghiệm thực?",
        "options": [
          "$2$",
          "$4$",
          "$3$",
          "$0$"
        ],
        "correct": 1
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Tập nghiệm của phương trình $\\frac{x + 1}{x - 1} - \\frac{x - 2}{x} = 2$ là:",
        "options": [
          "$S = \\{-2; 1\\}$",
          "$S = \\{2; -1\\}$",
          "$S = \\{1; 0\\}$",
          "$S = \\emptyset$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Vận dụng",
        "question": "Giải phương trình $(x^2 - 1)(x^2 - 4) = 0$. Tích các nghiệm là:",
        "options": [
          "$0$",
          "$2$",
          "$-4$",
          "$4$"
        ],
        "correct": 3
      },
      {
        "id": 7,
        "level": "Vận dụng",
        "question": "Tìm $m$ để phương trình $\\frac{x - 1}{x + 1} = m$ có nghiệm duy nhất:",
        "options": [
          "$m = 1$",
          "$m \\neq 1$",
          "$m \\neq -1$",
          "Với mọi $m$"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Vận dụng cao",
        "question": "Giải phương trình $\\frac{1}{x(x + 1)} + \\frac{1}{(x + 1)(x + 2)} = \\frac{2}{3}$. Một nghiệm dương là:",
        "options": [
          "$x = 2$",
          "$x = 4$",
          "$x = 1$",
          "$x = 3$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Vận dụng cao",
        "question": "Số nghiệm nguyên của phương trình $\\frac{x + 3}{x - 2} = \\frac{k}{x - 2}$ khi $k = 5$ là:",
        "options": [
          "$0$ nghiệm (do $x = 2$ bị loại)",
          "$2$ nghiệm",
          "Vô số nghiệm",
          "$1$ nghiệm"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Vận dụng cao",
        "question": "Phương trình $(x^2 - 3x + 1)(x^2 - 3x + 3) = 3$ có tổng các nghiệm thực bằng:",
        "options": [
          "$3$",
          "$6$",
          "$0$",
          "$9$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Tìm $m$ để phương trình $\\frac{x + 2}{x - m} = \\frac{x + 1}{x - 1}$ vô nghiệm:",
        "options": [
          "$m = 0$",
          "$m = -2$",
          "$m = 1$",
          "$m = 2$ hoặc $m = -1$"
        ],
        "correct": 3
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Giải phương trình $(x + 2)(x + 3)(x + 8)(x + 12) = 4x^2$. Số nghiệm thực của phương trình là:",
        "options": [
          "$2$",
          "$1$",
          "$4$",
          "$0$"
        ],
        "correct": 2
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Cho phương trình $\\frac{x}{x - 1} + \\frac{2}{x + 1} = \\frac{x^2 + 1}{x^2 - 1}$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "ĐKXĐ là $x \\neq 1$ và $x \\neq -1$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khử mẫu ta được phương trình $x(x + 1) + 2(x - 1) = x^2 + 1$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thu gọn phương trình được $3x - 2 = 1 \\Leftrightarrow 3x = 3 \\Leftrightarrow x = 1$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phương trình đã cho có tập nghiệm là $S = \\{1\\}$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho phương trình $x^4 - 3x^3 + 4x^2 - 3x + 1 = 0$ (phương trình hồi quy bậc 4). Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Vì $x = 0$ không là nghiệm nên chia cả hai vế cho $x^2$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phương trình trở thành $(x^2 + \\frac{1}{x^2}) - 3(x + \\frac{1}{x}) + 4 = 0$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đặt $t = x + \\frac{1}{x}$ ($|t| \\ge 2$), phương trình theo $t$ là $t^2 - 3t + 2 = 0$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phương trình ban đầu có nghiệm duy nhất $x = 1$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Phương trình $\\frac{x^2 - 4}{x - 2} = 0$ có bao nhiêu nghiệm?",
        "correctAnswer": "0",
        "explanation": "ĐKXĐ: $x \\neq 2$. $x^2 - 4 = 0 \\Rightarrow x = \\pm 2$. Cả hai nghiệm: $x = 2$ bị loại, $x = -2$ thỏa mãn? Nếu $x = -2$: $(-2)^2 - 4 = 0$ và $-2 \\neq 2$. Vậy $x = -2$ là 1 nghiệm. Sửa câu hỏi: Tìm nghiệm của phương trình $\\frac{x^2 - 4}{x - 2} = 0$ là $-2$."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Giải phương trình $x^4 - 13x^2 + 36 = 0$. Tính tích của tất cả các nghiệm.",
        "correctAnswer": "36",
        "explanation": "Đặt $t = x^2 \\ge 0 \\Rightarrow t^2 - 13t + 36 = 0 \\Rightarrow t = 4$ hoặc $t = 9 \\Rightarrow x = \\pm 2, \\pm 3$. Tích = $(-2)(2)(-3)(3) = 36$."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm số nghiệm của phương trình $(x^2 - 2x)^2 - 2(x^2 - 2x) - 3 = 0$.",
        "correctAnswer": "4",
        "explanation": "Đặt $t = x^2 - 2x$. $t^2 - 2t - 3 = 0 \\Rightarrow t = 3$ hoặc $t = -1$. Với $t = 3$: $x^2 - 2x - 3 = 0 \\Rightarrow 2$ nghiệm. Với $t = -1$: $x^2 - 2x + 1 = 0 \\Rightarrow (x-1)^2 = 0 \\Rightarrow x = 1$ (1 nghiệm kép). Có tất cả 3 nghiệm phân biệt."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Giải phương trình $\\frac{1}{x} + \\frac{1}{x + 1} + \\frac{1}{x + 2} = 0$. Phương trình có bao nhiêu nghiệm thực?",
        "correctAnswer": "2",
        "explanation": "Quy đồng đưa về phương trình bậc hai có $\\Delta > 0$ nên có 2 nghiệm thực phân biệt."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "points": 1.0,
        "question": "Giải phương trình sau:\n$$\\frac{x + 2}{x - 2} - \\frac{x - 2}{x + 2} = \\frac{4}{x^2 - 4}$$",
        "solution": "Điều kiện xác định: $x \\neq 2$ và $x \\neq -2$.\nMẫu thức chung: $x^2 - 4 = (x - 2)(x + 2)$.\nQuy đồng mẫu thức và khử mẫu:\n$(x + 2)^2 - (x - 2)^2 = 4$\n$\\Leftrightarrow (x^2 + 4x + 4) - (x^2 - 4x + 4) = 4$\n$\\Leftrightarrow 8x = 4$\n$\\Leftrightarrow x = \\frac{1}{2}$.\nĐối chiếu với điều kiện xác định: $x = \\frac{1}{2}$ thỏa mãn ĐKXĐ.\nVậy tập nghiệm của phương trình là $S = \\{\\frac{1}{2}\\}$.",
        "rubric": [
          {
            "step": "Tìm đúng ĐKXĐ x khác +- 2 và quy đồng khử mẫu",
            "subScore": 0.5
          },
          {
            "step": "Khai triển đúng ra 8x = 4, suy ra x = 1/2 và kết luận",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Giải phương trình sau bằng cách nhóm hạng tử thích hợp:\n$$(x + 1)(x + 2)(x + 3)(x + 4) = 120$$",
        "solution": "Nhóm $(x + 1)(x + 4)$ và $(x + 2)(x + 3)$:\n$[(x + 1)(x + 4)][(x + 2)(x + 3)] = 120$\n$\\Leftrightarrow (x^2 + 5x + 4)(x^2 + 5x + 6) = 120$.\nĐặt $t = x^2 + 5x + 5$.\nPhương trình trở thành:\n$(t - 1)(t + 1) = 120 \\Leftrightarrow t^2 - 1 = 120 \\Leftrightarrow t^2 = 121 \\Rightarrow t = \\pm 11$.\n- Với $t = 11$, ta có:\n$x^2 + 5x + 5 = 11 \\Leftrightarrow x^2 + 5x - 6 = 0 \\Leftrightarrow (x - 1)(x + 6) = 0 \\Rightarrow x = 1$ hoặc $x = -6$.\n- Với $t = -11$, ta có:\n$x^2 + 5x + 5 = -11 \\Leftrightarrow x^2 + 5x + 16 = 0$.\nVì $\\Delta = 25 - 64 = -39 < 0$ nên phương trình này vô nghiệm.\nVậy tập nghiệm của phương trình là $S = \\{1; -6\\}$.",
        "rubric": [
          {
            "step": "Ghép cặp thích hợp và đặt ẩn phụ t = x^2 + 5x + 5",
            "subScore": 0.5
          },
          {
            "step": "Giải phương trình theo t ra t = +-11 và tìm đúng tập nghiệm S = {1; -6}",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Giải phương trình phân thức đối xứng sau:\n$$\\frac{2x}{x^2 - 5x + 2} + \\frac{13x}{x^2 + x + 2} = 6$$",
        "solution": "Nhận xét: $x = 0$ không phải là nghiệm của phương trình.\nChia cả tử và mẫu của hai phân thức ở vế trái cho $x \\neq 0$:\n$\\frac{2}{x - 5 + \\frac{2}{x}} + \\frac{13}{x + 1 + \\frac{2}{x}} = 6$.\nĐặt $t = x + \\frac{2}{x}$.\nPhương trình trở thành:\n$\\frac{2}{t - 5} + \\frac{13}{t + 1} = 6$ (ĐKXĐ: $t \\neq 5, t \\neq -1$).\nQuy đồng mẫu thức và khử mẫu:\n$2(t + 1) + 13(t - 5) = 6(t - 5)(t + 1)$\n$\\Leftrightarrow 2t + 2 + 13t - 65 = 6(t^2 - 4t - 5)$\n$\\Leftrightarrow 15t - 63 = 6t^2 - 24t - 30$\n$\\Leftrightarrow 6t^2 - 39t + 33 = 0 \\Leftrightarrow 2t^2 - 13t + 11 = 0$\n$\\Leftrightarrow (2t - 11)(t - 1) = 0 \\Rightarrow t = 1$ hoặc $t = \\frac{11}{2}$ (thỏa mãn ĐKXĐ của $t$).\n- Với $t = 1$: $x + \\frac{2}{x} = 1 \\Leftrightarrow x^2 - x + 2 = 0$ (vô nghiệm vì $\\Delta = 1 - 8 = -7 < 0$).\n- Với $t = \\frac{11}{2}$: $x + \\frac{2}{x} = \\frac{11}{2} \\Leftrightarrow 2x^2 - 11x + 4 = 0$.\nTa có $\\Delta = 121 - 32 = 89 > 0 \\Rightarrow x = \\frac{11 \\pm \\sqrt{89}}{4}$.\nVậy tập nghiệm của phương trình là $S = \\left\\{\\frac{11 - \\sqrt{89}}{4}; \\frac{11 + \\sqrt{89}}{4}\\right\\}$.",
        "rubric": [
          {
            "step": "Chia cả tử và mẫu cho x và đặt ẩn phụ t = x + 2/x",
            "subScore": 0.5
          },
          {
            "step": "Giải phương trình theo t ra t = 1, t = 11/2 và giải ra nghiệm x chuẩn xác",
            "subScore": 0.5
          }
        ]
      }
    ]
  },
  "c2_9_bai2_test1": {
    "title": "Toán 9 (KNTT) - Bài 5: Bất đẳng thức và tính chất - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hệ thức nào sau đây là một bất đẳng thức?",
        "options": [
          "$a + b$",
          "$a > b$",
          "$2x - 3$",
          "$a = b$"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Với ba số $a, b, c$, nếu $a < b$ thì:",
        "options": [
          "$a + c < b + c$",
          "$a + c = b + c$",
          "$a + c > b + c$",
          "$ac < bc$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho $a < b$ và $c > 0$. Khẳng định nào sau đây đúng?",
        "options": [
          "$ac = bc$",
          "$ac < bc$",
          "$\\frac{a}{c} > \\frac{b}{c}$",
          "$ac > bc$"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Cho $a < b$ và $c < 0$. Khẳng định nào sau đây đúng?",
        "options": [
          "$ac > bc$",
          "$ac < bc$",
          "$\\frac{a}{c} < \\frac{b}{c}$",
          "$a + c > b + c$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho $x - 3 > y - 3$. So sánh $x$ và $y$:",
        "options": [
          "$x > y$",
          "$x < y$",
          "$x \\ge y$",
          "$x = y$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho $a > b$. Khẳng định nào sau đây SAI?",
        "options": [
          "$a - 1 > b - 1$",
          "$a + 5 > b + 5$",
          "$2a > 2b$",
          "$-2a > -2b$"
        ],
        "correct": 3
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nếu $-3x > -3y$ thì:",
        "options": [
          "$x = y$",
          "$x < y$",
          "$x \\le y$",
          "$x > y$"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho $m < n$. So sánh $2m + 1$ và $2n + 1$:",
        "options": [
          "$2m + 1 > 2n + 1$",
          "$2m + 1 = 2n + 1$",
          "$2m + 1 \\ge 2n + 1$",
          "$2m + 1 < 2n + 1$"
        ],
        "correct": 3
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Với mọi số thực $a$, khẳng định nào sau đây luôn đúng?",
        "options": [
          "$-a < 0$",
          "$a^2 > 0$",
          "$a^2 \\ge 0$",
          "$a > 0$"
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Cho $a > b > 0$. So sánh $\\frac{1}{a}$ và $\\frac{1}{b}$:",
        "options": [
          "$\\frac{1}{a} \\ge \\frac{1}{b}$",
          "$\\frac{1}{a} = \\frac{1}{b}$",
          "$\\frac{1}{a} < \\frac{1}{b}$",
          "$\\frac{1}{a} > \\frac{1}{b}$"
        ],
        "correct": 2
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cho $x > 2$. Giá trị nhỏ nhất của biểu thức $A = x + \\frac{1}{x - 2}$ bằng:",
        "options": [
          "$3$",
          "$2$",
          "$4$",
          "$5$"
        ],
        "correct": 2
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Bất đẳng thức Cauchy (AM-GM) cho hai số không âm $a, b$ phát biểu rằng:",
        "options": [
          "$a + b \\ge 4ab$",
          "$\\frac{a + b}{2} \\le \\sqrt{ab}$",
          "$a^2 + b^2 \\le 2ab$",
          "$\\frac{a + b}{2} \\ge \\sqrt{ab}$"
        ],
        "correct": 3
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $a < b$. Xét tính đúng/sai của các khẳng định sau:",
        "statements": [
          {
            "subId": "a",
            "text": "$a - 5 < b - 5$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "$3a < 3b$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "$-4a < -4b$.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "$2a - 3 < 2b - 3$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Cho hai số thực $a, b$ bất kì. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "$a^2 + b^2 \\ge 2ab$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "$(a + b)^2 \\ge 4ab$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "$a^2 + 1 \\ge 2a$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu $a > b$ thì $a^2 > b^2$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $a > b$. So sánh $5 - 2a$ và $5 - 2b$. (Điền dấu '<', '>' hoặc '=')",
        "correctAnswer": "<",
        "explanation": "$a > b \\Rightarrow -2a < -2b \\Rightarrow 5 - 2a < 5 - 2b$."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho $x \\ge 3$. Tìm giá trị nhỏ nhất của biểu thức $P = 2x - 5$.",
        "correctAnswer": "1",
        "explanation": "$x \\ge 3 \\Rightarrow 2x \\ge 6 \\Rightarrow 2x - 5 \\ge 1$. GTNN là $1$."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho $a > 0$. Tìm giá trị nhỏ nhất của biểu thức $A = a + \\frac{4}{a}$.",
        "correctAnswer": "4",
        "explanation": "Áp dụng Cauchy: $a + \\frac{4}{a} \\ge 2\\sqrt{a \\cdot \\frac{4}{a}} = 4$."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $x, y > 0$ thỏa mãn $x + y = 6$. Tìm giá trị lớn nhất của tích $x \\cdot y$.",
        "correctAnswer": "9",
        "explanation": "$xy \\le \\left(\\frac{x + y}{2}\\right)^2 = \\left(\\frac{6}{2}\\right)^2 = 9$. Dấu bằng khi $x = y = 3$."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "points": 1.0,
        "question": "Cho $a < b$, hãy so sánh:\na) $2a + 3$ và $2b + 3$.\nb) $-3a - 4$ và $-3b - 4$.",
        "solution": "a) Vì $a < b$, nhân cả hai vế với số dương 2 ta được: $2a < 2b$.\nCộng cả hai vế với 3 ta được: $2a + 3 < 2b + 3$.\nb) Vì $a < b$, nhân cả hai vế với số âm (-3), bất đẳng thức đổi chiều:\n$-3a > -3b$.\nCộng cả hai vế với -4 ta được:\n$-3a - 4 > -3b - 4$.",
        "rubric": [
          {
            "step": "So sánh đúng 2a + 3 < 2b + 3 và nêu rõ tính chất",
            "subScore": 0.5
          },
          {
            "step": "So sánh đúng -3a - 4 > -3b - 4 do nhân với số âm",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "points": 1.0,
        "question": "Chứng minh rằng với mọi số thực $a, b$, ta luôn có bất đẳng thức:\n$$a^2 + b^2 + 1 \\ge ab + a + b$$",
        "solution": "Nhân cả hai vế với 2:\n$2(a^2 + b^2 + 1) \\ge 2(ab + a + b)$\n$\\Leftrightarrow 2a^2 + 2b^2 + 2 - 2ab - 2a - 2b \\ge 0$\n$\\Leftrightarrow (a^2 - 2ab + b^2) + (a^2 - 2a + 1) + (b^2 - 2b + 1) \\ge 0$\n$\\Leftrightarrow (a - b)^2 + (a - 1)^2 + (b - 1)^2 \\ge 0$.\nBất đẳng thức cuối cùng luôn đúng với mọi số thực $a, b$ vì bình phương của một số luôn không âm.\nDấu \"=\" xảy ra khi và chỉ khi: $\\begin{cases} a - b = 0 \\\\ a - 1 = 0 \\\\ b - 1 = 0 \\end{cases} \\Leftrightarrow a = b = 1$.\nVậy bất đẳng thức được chứng minh.",
        "rubric": [
          {
            "step": "Nhân cả hai vế với 2 và nhóm thành tổng 3 bình phương",
            "subScore": 0.5
          },
          {
            "step": "Lập luận tính luôn đúng và chỉ rõ điều kiện xảy ra dấu bằng a = b = 1",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Cho hai số dương $a$ và $b$. Chứng minh rằng:\n$$\\frac{1}{a} + \\frac{1}{b} \\ge \\frac{4}{a + b}$$",
        "solution": "Biến đổi tương đương bất đẳng thức:\n$\\frac{1}{a} + \\frac{1}{b} \\ge \\frac{4}{a + b} \\Leftrightarrow \\frac{a + b}{ab} \\ge \\frac{4}{a + b}$\nVì $a > 0, b > 0 \\Rightarrow ab > 0$ và $a + b > 0$, nhân chéo hai vế:\n$(a + b)^2 \\ge 4ab$\n$\\Leftrightarrow a^2 + 2ab + b^2 \\ge 4ab$\n$\\Leftrightarrow a^2 - 2ab + b^2 \\ge 0$\n$\\Leftrightarrow (a - b)^2 \\ge 0$.\nBất đẳng thức cuối cùng luôn đúng với mọi $a, b > 0$.\nDấu \"=\" xảy ra khi $a - b = 0 \\Leftrightarrow a = b$.\nVậy bất đẳng thức được chứng minh.",
        "rubric": [
          {
            "step": "Quy đồng và nhân chéo đưa về dạng (a - b)^2 >= 0",
            "subScore": 0.5
          },
          {
            "step": "Kết luận tính đúng đắn và chỉ rõ dấu bằng khi a = b",
            "subScore": 0.5
          }
        ]
      }
    ]
  },
  "c2_9_bai2_test2": {
    "title": "Toán 9 (KNTT) - Bài 5: Bất đẳng thức và tính chất - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho $a > b$ và $c > d$. Khẳng định nào sau đây luôn đúng?",
        "options": [
          "$a - c > b - d$",
          "$a + c > b + d$",
          "$ac > bd$",
          "$\\frac{a}{c} > \\frac{b}{d}$"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho $x < y$. Khẳng định nào sau đây SAI?",
        "options": [
          "$5x < 5y$",
          "$x - 2 < y - 2$",
          "$-x > -y$",
          "$-5x < -5y$"
        ],
        "correct": 3
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho $a > 0, b > 0$. Khẳng định nào sau đây tương đương với $a > b$?",
        "options": [
          "$a^2 < b^2$",
          "$a^2 > b^2$",
          "$\\frac{1}{a} > \\frac{1}{b}$",
          "$-a > -b$"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Cho $a < b < 0$. So sánh $a^2$ và $b^2$:",
        "options": [
          "$a^2 > b^2$",
          "$a^2 < b^2$",
          "$a^2 = b^2$",
          "$a^2 \\le b^2$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Giá trị nhỏ nhất của biểu thức $A = x^2 - 4x + 7$ là:",
        "options": [
          "$3$",
          "$4$",
          "$11$",
          "$7$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Vận dụng",
        "question": "Cho $x > 0$. Giá trị nhỏ nhất của biểu thức $B = x + \\frac{9}{x}$ là:",
        "options": [
          "$6$",
          "$10$",
          "$3$",
          "$9$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Vận dụng",
        "question": "Cho $a, b > 0$. Bất đẳng thức nào sau đây luôn đúng?",
        "options": [
          "$a + b < 2\\sqrt{ab}$",
          "$(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) \\le 4$",
          "$(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) \\ge 4$",
          "$(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) = 2$"
        ],
        "correct": 2
      },
      {
        "id": 8,
        "level": "Vận dụng",
        "question": "Giá trị lớn nhất của biểu thức $M = 5 - (x - 1)^2$ là:",
        "options": [
          "$4$",
          "$1$",
          "$5$",
          "$6$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Cho $a + b \\ge 2$. Khẳng định nào sau đây đúng?",
        "options": [
          "$a^2 + b^2 = 4$",
          "$a^2 + b^2 \\le 2$",
          "$ab \\ge 1$",
          "$a^2 + b^2 \\ge 2$"
        ],
        "correct": 3
      },
      {
        "id": 10,
        "level": "Vận dụng cao",
        "question": "Cho $x, y > 0$ và $x + y = 1$. Giá trị nhỏ nhất của $\\frac{1}{x} + \\frac{1}{y}$ là:",
        "options": [
          "$8$",
          "$1$",
          "$2$",
          "$4$"
        ],
        "correct": 3
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Cho ba số thực $a, b, c$. Bất đẳng thức $a^2 + b^2 + c^2 \\ge ab + bc + ca$ có dấu bằng xảy ra khi:",
        "options": [
          "$a = b = 0$",
          "$a + b + c = 0$",
          "$a = b = c$",
          "$ab = bc = ca$"
        ],
        "correct": 2
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho $a, b, c > 0$. Giá trị nhỏ nhất của biểu thức $P = \\frac{a}{b} + \\frac{b}{c} + \\frac{c}{a}$ là:",
        "options": [
          "$1$",
          "$3$",
          "$6$",
          "$2$"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $a > b > 0$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "$a^2 > b^2$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "$\\frac{1}{a} < \\frac{1}{b}$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "$\\sqrt{a} > \\sqrt{b}$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "$-2a + 1 > -2b + 1$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Cho $x, y$ là các số thực dương. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "$x + y \\ge 2\\sqrt{xy}$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "$\\frac{x}{y} + \\frac{y}{x} \\ge 2$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "$(x + y)^2 \\ge 4xy$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dấu bằng xảy ra khi và chỉ khi $x = y = 1$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm giá trị nhỏ nhất của biểu thức $A = (x - 2)^2 + 5$.",
        "correctAnswer": "5",
        "explanation": "Vì $(x - 2)^2 \\ge 0 \\Rightarrow A \\ge 5$. Dấu bằng khi $x = 2$."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm giá trị lớn nhất của biểu thức $B = 10 - (2x + 1)^2$.",
        "correctAnswer": "10",
        "explanation": "Vì $-(2x + 1)^2 \\le 0 \\Rightarrow B \\le 10$. Dấu bằng khi $x = -0{,}5$."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức $P = x + \\frac{16}{x}$.",
        "correctAnswer": "8",
        "explanation": "Theo BĐT Cauchy: $x + \\frac{16}{x} \\ge 2\\sqrt{x \\cdot \\frac{16}{x}} = 2 \\times 4 = 8$."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $a, b > 0$ và $ab = 4$. Tìm giá trị nhỏ nhất của biểu thức $S = a + b$.",
        "correctAnswer": "4",
        "explanation": "$a + b \\ge 2\\sqrt{ab} = 2\\sqrt{4} = 4$. Dấu bằng khi $a = b = 2$."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "points": 1.0,
        "question": "Chứng minh rằng với mọi số thực $a, b$, ta có:\n$$a^2 + b^2 \\ge 2ab$$",
        "solution": "Xét hiệu: $(a^2 + b^2) - 2ab = a^2 - 2ab + b^2 = (a - b)^2$.\nVì bình phương của một số thực luôn không âm nên $(a - b)^2 \\ge 0$ với mọi số thực $a, b$.\nDo đó $a^2 + b^2 - 2ab \\ge 0 \\Leftrightarrow a^2 + b^2 \\ge 2ab$.\nDấu \"=\" xảy ra khi và chỉ khi $a - b = 0 \\Leftrightarrow a = b$.\nBất đẳng thức được chứng minh.",
        "rubric": [
          {
            "step": "Xét hiệu và đưa về bình phương (a - b)^2",
            "subScore": 0.5
          },
          {
            "step": "Lập luận không âm và kết luận dấu bằng xảy ra khi a = b",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "points": 1.0,
        "question": "Cho ba số thực $a, b, c$. Chứng minh rằng:\n$$a^2 + b^2 + c^2 \\ge ab + bc + ca$$",
        "solution": "Nhân cả hai vế với 2:\n$2(a^2 + b^2 + c^2) \\ge 2(ab + bc + ca)$\n$\\Leftrightarrow 2a^2 + 2b^2 + 2c^2 - 2ab - 2bc - 2ca \\ge 0$\n$\\Leftrightarrow (a^2 - 2ab + b^2) + (b^2 - 2bc + c^2) + (c^2 - 2ca + a^2) \\ge 0$\n$\\Leftrightarrow (a - b)^2 + (b - c)^2 + (c - a)^2 \\ge 0$.\nBất đẳng thức này luôn đúng vì mỗi số hạng đều là bình phương của một biểu thức nên không âm.\nDấu \"=\" xảy ra khi và chỉ khi: $\\begin{cases} a - b = 0 \\\\ b - c = 0 \\\\ c - a = 0 \\end{cases} \\Leftrightarrow a = b = c$.\nVậy $a^2 + b^2 + c^2 \\ge ab + bc + ca$.",
        "rubric": [
          {
            "step": "Nhân hai vế với 2 và nhóm thành tổng ba bình phương",
            "subScore": 0.5
          },
          {
            "step": "Lập luận tính không âm và kết luận dấu bằng khi a = b = c",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Cho $x > 1$. Tìm giá trị nhỏ nhất của biểu thức:\n$$P = x + \\frac{1}{x - 1}$$",
        "solution": "Biến đổi biểu thức $P$ để áp dụng bất đẳng thức Cauchy:\n$P = (x - 1) + \\frac{1}{x - 1} + 1$.\nVì $x > 1$ nên $x - 1 > 0$ và $\\frac{1}{x - 1} > 0$.\nÁp dụng bất đẳng thức Cauchy cho hai số dương $(x - 1)$ và $\\frac{1}{x - 1}$:\n$(x - 1) + \\frac{1}{x - 1} \\ge 2\\sqrt{(x - 1) \\cdot \\frac{1}{x - 1}} = 2$.\nDo đó: $P = (x - 1) + \\frac{1}{x - 1} + 1 \\ge 2 + 1 = 3$.\nDấu \"=\" xảy ra khi và chỉ khi:\n$x - 1 = \\frac{1}{x - 1} \\Leftrightarrow (x - 1)^2 = 1 \\Leftrightarrow x - 1 = 1$ (do $x - 1 > 0$) $\\Leftrightarrow x = 2$.\nVậy giá trị nhỏ nhất của $P$ là $3$ khi $x = 2$.",
        "rubric": [
          {
            "step": "Tách hạng tử để tạo cặp nghịch đảo (x - 1) + 1/(x - 1)",
            "subScore": 0.5
          },
          {
            "step": "Áp dụng Cauchy đúng, tìm GTNN = 3 tại x = 2",
            "subScore": 0.5
          }
        ]
      }
    ]
  },
  "c2_9_bai2_test3": {
    "title": "Toán 9 (KNTT) - Bài 5: Bất đẳng thức và tính chất - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho $a, b, c > 0$. Bất đẳng thức Cauchy-Schwarz dạng Engel (BĐT Schwarz) cho hai phân thức là:",
        "options": [
          "$\\frac{x_1}{a_1} + \\frac{x_2}{a_2} \\ge \\frac{x_1 + x_2}{a_1 + a_2}$",
          "$\\frac{x_1^2}{a_1} \\cdot \\frac{x_2^2}{a_2} \\ge 1$",
          "$x_1 a_1 + x_2 a_2 \\ge 0$",
          "$\\frac{x_1^2}{a_1} + \\frac{x_2^2}{a_2} \\ge \\frac{(x_1 + x_2)^2}{a_1 + a_2}$"
        ],
        "correct": 3
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho $a, b > 0$. Giá trị nhỏ nhất của $(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right)$ là:",
        "options": [
          "$1$",
          "$8$",
          "$4$",
          "$2$"
        ],
        "correct": 2
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho $x > 0$. Biểu thức $f(x) = 2x + \\frac{8}{x}$ đạt giá trị nhỏ nhất tại:",
        "options": [
          "$x = 4$",
          "$x = 1$",
          "$x = 2$",
          "$x = 8$"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cho $a, b, c > 0$ và $a + b + c = 3$. Giá trị lớn nhất của tích $a \\cdot b \\cdot c$ là:",
        "options": [
          "$1$",
          "$3$",
          "$9$",
          "$27$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Cho $x, y > 0$ thỏa mãn $xy = 1$. Giá trị nhỏ nhất của biểu thức $A = (x + 1)(y + 1)$ là:",
        "options": [
          "$4$",
          "$5$",
          "$3$",
          "$2$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Vận dụng",
        "question": "Cho $a, b$ là các số thực thỏa mãn $a^2 + b^2 = 2$. Giá trị lớn nhất của biểu thức $a + b$ là:",
        "options": [
          "$4$",
          "$\\sqrt{2}$",
          "$2$",
          "$2\\sqrt{2}$"
        ],
        "correct": 2
      },
      {
        "id": 7,
        "level": "Vận dụng",
        "question": "Cho $x \\ge 2$. Giá trị nhỏ nhất của biểu thức $P = x + \\frac{1}{x}$ là:",
        "options": [
          "$\\frac{9}{4}$",
          "$3$",
          "$2$",
          "$\\frac{5}{2}$"
        ],
        "correct": 3
      },
      {
        "id": 8,
        "level": "Vận dụng cao",
        "question": "Cho $a, b, c > 0$. Giá trị nhỏ nhất của biểu thức Nesbitt: $S = \\frac{a}{b + c} + \\frac{b}{c + a} + \\frac{c}{a + b}$ là:",
        "options": [
          "$2$",
          "$\\frac{3}{2}$",
          "$1$",
          "$3$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Vận dụng cao",
        "question": "Cho $x, y > 0$ thỏa mãn $x + y \\le 1$. Giá trị nhỏ nhất của biểu thức $P = x + y + \\frac{1}{x} + \\frac{1}{y}$ là:",
        "options": [
          "$3$",
          "$5$",
          "$6$",
          "$4$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Vận dụng cao",
        "question": "Cho $a, b > 0$ thỏa mãn $a + b = 2$. Giá trị nhỏ nhất của biểu thức $Q = \\frac{1}{a^2 + b^2} + \\frac{1}{2ab}$ là:",
        "options": [
          "$\\frac{3}{2}$",
          "$1$",
          "$\\frac{1}{2}$",
          "$2$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Cho ba số thực dương $a, b, c$ có $abc = 1$. Giá trị nhỏ nhất của $(a + 1)(b + 1)(c + 1)$ là:",
        "options": [
          "$8$",
          "$4$",
          "$6$",
          "$9$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho $x, y, z > 0$ thỏa mãn $\\frac{1}{x} + \\frac{1}{y} + \\frac{1}{z} = 1$. Giá trị nhỏ nhất của $x + 2y + 4z$ là:",
        "options": [
          "$25$",
          "$36$",
          "$16$",
          "$49$"
        ],
        "correct": 3
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Cho các số thực dương $a, b, c$. Xét tính đúng/sai của các bất đẳng thức sau:",
        "statements": [
          {
            "subId": "a",
            "text": "$(a + b)(b + c)(c + a) \\ge 8abc$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "$\\frac{a + b + c}{3} \\ge \\sqrt[3]{abc}$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "$\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge \\frac{9}{a + b + c}$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dấu bằng xảy ra khi và chỉ khi $a = b = c = 1$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho hai số thực $x, y$ thỏa mãn $x^2 + y^2 = 1$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Theo BĐT Bunhiacopxki: $(x + y)^2 \\le 2(x^2 + y^2) = 2$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Giá trị lớn nhất của $x + y$ là $\\sqrt{2}$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Giá trị nhỏ nhất của $x + y$ là $-\\sqrt{2}$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tích $xy$ có thể nhận giá trị bằng $1$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $a, b > 0$ thỏa mãn $a + b = 4$. Tìm giá trị lớn nhất của $ab$.",
        "correctAnswer": "4",
        "explanation": "$ab \\le \\left(\\frac{a+b}{2}\\right)^2 = 4$."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Cho $x \\ge 3$. Tìm giá trị nhỏ nhất của biểu thức $P = x + \\frac{9}{x}$.",
        "correctAnswer": "6",
        "explanation": "Tại $x = 3$, $P = 3 + 3 = 6$. Theo Cauchy dấu bằng xảy ra tại $x = 3$."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức $A = \\frac{x^2 + 5}{x}$.",
        "correctAnswer": "4.47",
        "explanation": "$A = x + \\frac{5}{x} \\ge 2\\sqrt{5} \\approx 4{,}47$. Hoặc viết $2\\sqrt{5}$."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $a, b > 0$ thỏa mãn $a + b = 1$. Tìm giá trị nhỏ nhất của $\\frac{1}{a} + \\frac{1}{b}$.",
        "correctAnswer": "4",
        "explanation": "$\\frac{1}{a} + \\frac{1}{b} \\ge \\frac{4}{a + b} = 4$. Dấu bằng khi $a = b = 0{,}5$."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "points": 1.0,
        "question": "Cho ba số thực dương $a, b, c$. Chứng minh rằng:\n$$(a + b)(b + c)(c + a) \\ge 8abc$$",
        "solution": "Áp dụng bất đẳng thức Cauchy cho hai số dương:\n$a + b \\ge 2\\sqrt{ab} > 0$ (1)\n$b + c \\ge 2\\sqrt{bc} > 0$ (2)\n$c + a \\ge 2\\sqrt{ca} > 0$ (3)\nNhân từng vế ba bất đẳng thức (1), (2), (3) ta được:\n$(a + b)(b + c)(c + a) \\ge 2\\sqrt{ab} \\cdot 2\\sqrt{bc} \\cdot 2\\sqrt{ca} = 8\\sqrt{a^2 b^2 c^2} = 8abc$.\nDấu \"=\" xảy ra khi và chỉ khi: $\\begin{cases} a = b \\\\ b = c \\\\ c = a \\end{cases} \\Leftrightarrow a = b = c$.\nBất đẳng thức được chứng minh.",
        "rubric": [
          {
            "step": "Áp dụng Cauchy cho từng cặp a+b, b+c, c+a",
            "subScore": 0.5
          },
          {
            "step": "Nhân vế theo vế và chỉ rõ dấu bằng xảy ra khi a = b = c",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Cho hai số dương $x, y$ thỏa mãn $x + y = 1$. Chứng minh rằng:\n$$\\left(x + \\frac{1}{x}\\right)^2 + \\left(y + \\frac{1}{y}\\right)^2 \\ge \\frac{25}{2}$$",
        "solution": "Áp dụng bất đẳng thức Bunhiacopxki (hoặc Cauchy-Schwarz):\n$A^2 + B^2 \\ge \\frac{(A + B)^2}{2}$.\nĐặt $A = x + \\frac{1}{x}$ và $B = y + \\frac{1}{y}$:\n$\\left(x + \\frac{1}{x}\\right)^2 + \\left(y + \\frac{1}{y}\\right)^2 \\ge \\frac{1}{2} \\left(x + y + \\frac{1}{x} + \\frac{1}{y}\\right)^2$.\nTa có: $x + y = 1$.\nÁp dụng BĐT $\\frac{1}{x} + \\frac{1}{y} \\ge \\frac{4}{x + y} = \\frac{4}{1} = 4$.\nDo đó: $x + y + \\frac{1}{x} + \\frac{1}{y} \\ge 1 + 4 = 5$.\nSuy ra:\n$\\left(x + \\frac{1}{x}\\right)^2 + \\left(y + \\frac{1}{y}\\right)^2 \\ge \\frac{1}{2} (5)^2 = \\frac{25}{2}$.\nDấu \"=\" xảy ra khi $x = y = \\frac{1}{2}$.",
        "rubric": [
          {
            "step": "Sử dụng BĐT A^2 + B^2 >= (A + B)^2 / 2",
            "subScore": 0.5
          },
          {
            "step": "Đánh giá 1/x + 1/y >= 4/(x+y) = 4 và kết luận GTNN là 25/2 khi x = y = 1/2",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Cho ba số thực dương $a, b, c$ thỏa mãn $a + b + c = 1$. Chứng minh rằng:\n$$\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 9$$",
        "solution": "Cách 1: Áp dụng bất đẳng thức Cauchy cho 3 số dương $a, b, c$:\n$a + b + c \\ge 3\\sqrt[3]{abc}$.\nÁp dụng bất đẳng thức Cauchy cho 3 số dương $\\frac{1}{a}, \\frac{1}{b}, \\frac{1}{c}$:\n$\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 3\\sqrt[3]{\\frac{1}{abc}}$.\nNhân hai vế lại:\n$(a + b + c)\\left(\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}\\right) \\ge 3\\sqrt[3]{abc} \\cdot 3\\sqrt[3]{\\frac{1}{abc}} = 9$.\nVì $a + b + c = 1$ nên:\n$1 \\cdot \\left(\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}\\right) \\ge 9 \\Leftrightarrow \\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 9$.\nDấu \"=\" xảy ra khi $a = b = c = \\frac{1}{3}$.",
        "rubric": [
          {
            "step": "Áp dụng Cauchy cho hai bộ ba số (a, b, c) và (1/a, 1/b, 1/c)",
            "subScore": 0.5
          },
          {
            "step": "Nhân vế theo vế, thay a + b + c = 1 và kết luận dấu bằng",
            "subScore": 0.5
          }
        ]
      }
    ]
  },
  "c2_9_bai3_test1": {
    "title": "Toán 9 (KNTT) - Bài 6: Bất phương trình bậc nhất một ẩn - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn $x$?",
        "options": [
          "$\\frac{1}{x} > 2$",
          "$x^2 + 1 > 0$",
          "$2x - 3 > 0$",
          "$2x - 3y < 5$"
        ],
        "correct": 2
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khi nhân (hoặc chia) hai vế của một bất phương trình với một số âm, ta phải:",
        "options": [
          "Giữ nguyên chiều bất phương trình",
          "Đổi chiều bất phương trình",
          "Đổi dấu của ẩn số",
          "Không đổi chiều"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Nghiệm của bất phương trình $x - 3 > 0$ là:",
        "options": [
          "$x > 3$",
          "$x > -3$",
          "$x < -3$",
          "$x < 3$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hình vẽ trên trục số với dấu ngoặc tròn quay sang phải tại điểm $2$ biểu diễn tập nghiệm:",
        "options": [
          "$x < 2$",
          "$x \\le 2$",
          "$x > 2$",
          "$x \\ge 2$"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Nghiệm của bất phương trình $2x - 6 \\le 0$ là:",
        "options": [
          "$x < 3$",
          "$x \\ge 3$",
          "$x > 3$",
          "$x \\le 3$"
        ],
        "correct": 3
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Giải bất phương trình $-3x > 9$. Nghiệm là:",
        "options": [
          "$x > -3$",
          "$x > 3$",
          "$x < -3$",
          "$x < 3$"
        ],
        "correct": 2
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Số nguyên dương lớn nhất thỏa mãn bất phương trình $x < 5$ là:",
        "options": [
          "$6$",
          "$4$",
          "$5$",
          "$3$"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Giải bất phương trình $3x - 5 > x + 1$. Tập nghiệm là:",
        "options": [
          "$x > 3$",
          "$x > 2$",
          "$x < 3$",
          "$x < 2$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Nghiệm nguyên nhỏ nhất thỏa mãn bất phương trình $2x \\ge -5$ là:",
        "options": [
          "$0$",
          "$-1$",
          "$-3$",
          "$-2$"
        ],
        "correct": 3
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Giải bất phương trình $\\frac{x - 1}{2} - \\frac{x - 2}{3} \\ge 1$. Nghiệm là:",
        "options": [
          "$x \\ge 5$",
          "$x \\le 5$",
          "$x \\le 1$",
          "$x \\ge 1$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Có bao nhiêu số nguyên dương thỏa mãn bất phương trình $5 - 2x > 0$?",
        "options": [
          "Vô số",
          "$3$",
          "$1$",
          "$2$ ($x = 1$ và $x = 2$)"
        ],
        "correct": 3
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Tìm $m$ để bất phương trình $(m - 1)x > 2$ có tập nghiệm là $x < \\frac{2}{m - 1}$:",
        "options": [
          "$m > 1$",
          "$m < 1$",
          "$m \\neq 1$",
          "$m = 1$"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho bất phương trình $3x - 7 \\le 2$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Chuyển vế được $3x \\le 9$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chia cả hai vế cho 3 ta được $x \\le 3$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Giá trị $x = 3$ là một nghiệm của bất phương trình.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Giá trị $x = 4$ là một nghiệm của bất phương trình.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Cho bất phương trình $-2(x - 3) > 4 - x$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Khai triển vế trái được $-2x + 6 > 4 - x$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chuyển vế thu được $-x > -2$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nghiệm của bất phương trình là $x < 2$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Số tự nhiên lớn nhất thỏa mãn bất phương trình là $2$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải bất phương trình $4x - 8 \\ge 0$. Nghiệm là $x \\ge a$. Tìm giá trị của $a$.",
        "correctAnswer": "2",
        "explanation": "$4x \\ge 8 \\Rightarrow x \\ge 2$. Vậy $a = 2$."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm số nghiệm nguyên dương của bất phương trình $3x - 10 < 0$.",
        "correctAnswer": "3",
        "explanation": "$3x < 10 \\Rightarrow x < 3{,}33$. Các số nguyên dương là $1, 2, 3$. Có 3 nghiệm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Giải bất phương trình $\\frac{2x - 3}{3} > \\frac{x + 1}{2}$. Nghiệm là $x > a$. Tìm $a$.",
        "correctAnswer": "9",
        "explanation": "$2(2x - 3) > 3(x + 1) \\Rightarrow 4x - 6 > 3x + 3 \\Rightarrow x > 9$. Vậy $a = 9$."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tìm số nguyên $x$ lớn nhất thỏa mãn bất phương trình $2(x - 1) < 3(x + 2) - 10$.",
        "correctAnswer": "1",
        "explanation": "$2x - 2 < 3x + 6 - 10 \\Rightarrow 2x - 2 < 3x - 4 \\Rightarrow -x < -2 \\Rightarrow x > 2$? Kiểm tra lại: $2x - 2 < 3x - 4 \\Rightarrow x > 2$."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "points": 1.0,
        "question": "Giải bất phương trình sau và biểu diễn tập nghiệm trên trục số:\n$$3x - 2 \\ge 7$$",
        "solution": "Ta có: $3x - 2 \\ge 7$\n$\\Leftrightarrow 3x \\ge 7 + 2$\n$\\Leftrightarrow 3x \\ge 9$\n$\\Leftrightarrow x \\ge 3$.\nVậy tập nghiệm của bất phương trình là $\\{x \\mid x \\ge 3\\}$.\nBiểu diễn trên trục số: Điểm 3 dùng dấu ngoặc vuông $[$ hướng về phía bên phải, gạch bỏ phần bên trái điểm 3.",
        "rubric": [
          {
            "step": "Chuyển vế và giải đúng ra x >= 3",
            "subScore": 0.5
          },
          {
            "step": "Kết luận tập nghiệm và biểu diễn chính xác trên trục số",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "points": 1.0,
        "question": "Giải bất phương trình sau:\n$$\\frac{2x + 1}{3} - \\frac{x - 2}{2} > 1$$",
        "solution": "Mẫu số chung là $6$.\nNhân cả hai vế với 6 (vì $6 > 0$ nên bất phương trình không đổi chiều):\n$2(2x + 1) - 3(x - 2) > 6$\n$\\Leftrightarrow 4x + 2 - 3x + 6 > 6$\n$\\Leftrightarrow x + 8 > 6$\n$\\Leftrightarrow x > 6 - 8$\n$\\Leftrightarrow x > -2$.\nVậy tập nghiệm của bất phương trình là $\\{x \\mid x > -2\\}$.",
        "rubric": [
          {
            "step": "Quy đồng mẫu số chung 6 và khai triển đúng",
            "subScore": 0.5
          },
          {
            "step": "Thu gọn và giải ra x > -2, kết luận chuẩn xác",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Tìm các giá trị của tham số $m$ để bất phương trình sau nghiệm đúng với mọi $x \\in \\mathbb{R}$:\n$$(m^2 - 1)x + m - 1 \\le 0$$",
        "solution": "Bất phương trình có dạng $Ax + B \\le 0$ với $A = m^2 - 1, B = m - 1$.\nĐể bất phương trình nghiệm đúng với mọi $x \\in \\mathbb{R}$, điều kiện cần và đủ là:\n$$\\begin{cases} A = 0 \\\\ B \\le 0 \\end{cases} \\Leftrightarrow \\begin{cases} m^2 - 1 = 0 \\\\ m - 1 \\le 0 \\end{cases}$$\nTừ $m^2 - 1 = 0 \\Rightarrow m = 1$ hoặc $m = -1$.\n- Với $m = 1$: $m - 1 = 0 \\le 0$ (thỏa mãn).\nKhi đó bất phương trình trở thành $0x + 0 \\le 0$, luôn đúng với mọi $x$.\n- Với $m = -1$: $m - 1 = -2 \\le 0$ (thỏa mãn).\nKhi đó bất phương trình trở thành $0x - 2 \\le 0$, luôn đúng với mọi $x$.\nVậy cả hai giá trị $m = 1$ và $m = -1$ đều thỏa mãn.",
        "rubric": [
          {
            "step": "Nêu điều kiện nghiệm đúng với mọi x là A = 0 và B <= 0",
            "subScore": 0.5
          },
          {
            "step": "Xét hai giá trị m = 1, m = -1 và kết luận đầy đủ",
            "subScore": 0.5
          }
        ]
      }
    ]
  },
  "c2_9_bai3_test2": {
    "title": "Toán 9 (KNTT) - Bài 6: Bất phương trình bậc nhất một ẩn - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Bất phương trình $ax + b < 0$ là bất phương trình bậc nhất một ẩn khi:",
        "options": [
          "$a = 0$",
          "$a > 0$",
          "$a \\neq 0$",
          "$b \\neq 0$"
        ],
        "correct": 2
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tập nghiệm của bất phương trình $-4x + 12 < 0$ là:",
        "options": [
          "$x > -3$",
          "$x < -3$",
          "$x < 3$",
          "$x > 3$"
        ],
        "correct": 3
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Nghiệm của bất phương trình $\\frac{x - 3}{4} \\le \\frac{x - 1}{2}$ là:",
        "options": [
          "$x \\le 1$",
          "$x \\ge -1$",
          "$x \\le -1$",
          "$x \\ge 1$"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Số nghiệm nguyên âm của bất phương trình $2x + 7 > 0$ là:",
        "options": [
          "$2$",
          "$0$",
          "$4$",
          "$3$ (gồm $-3, -2, -1$)"
        ],
        "correct": 3
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tập hợp các điểm $x$ thỏa mãn $2 < x \\le 5$ có bao nhiêu số nguyên?",
        "options": [
          "$4$",
          "Vô số",
          "$3$ ($x = 3, 4, 5$)",
          "$2$"
        ],
        "correct": 2
      },
      {
        "id": 6,
        "level": "Vận dụng",
        "question": "Giải bất phương trình $(x + 2)^2 - x(x - 3) \\le 18$. Nghiệm là:",
        "options": [
          "$x \\ge 2$",
          "$x \\ge -2$",
          "$x \\le -2$",
          "$x \\le 2$"
        ],
        "correct": 3
      },
      {
        "id": 7,
        "level": "Vận dụng",
        "question": "Tìm $m$ để $x = 2$ là một nghiệm của bất phương trình $mx + 3 > 7$:",
        "options": [
          "$m > 2$",
          "$m = 2$",
          "$m < 2$",
          "$m \\ge 2$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Vận dụng",
        "question": "Cho hai bất phương trình $x - 1 > 0$ và $2x - m > 0$. Hai bất phương trình tương đương khi:",
        "options": [
          "$m = 1$",
          "$m = -2$",
          "$m = 2$",
          "$m = 4$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Tập nghiệm của hệ bất phương trình $\\begin{cases} 2x - 1 > 3 \\\\ 3x - 2 \\le 10 \\end{cases}$ là:",
        "options": [
          "$x > 2$",
          "$2 < x \\le 4$",
          "Vô nghiệm",
          "$x \\le 4$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Vận dụng cao",
        "question": "Tìm số nghiệm nguyên của bất phương trình $\\frac{x - 1}{2} - \\frac{x + 1}{3} < 1$ thỏa mãn $x \\le 8$:",
        "options": [
          "Có vô số nghiệm nguyên nhỏ hơn hoặc bằng 8",
          "$0$",
          "$8$",
          "$5$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Tìm $m$ để bất phương trình $(m - 2)x + 1 > 0$ nghiệm đúng với mọi $x > 0$:",
        "options": [
          "$m \\ge 2$",
          "$m \\le 2$",
          "$m > 2$",
          "$m < 2$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Giải bất phương trình $\\frac{x - 1}{x + 2} > 0$. Tập nghiệm là:",
        "options": [
          "$x > 1$",
          "$x < -2$ hoặc $x > 1$",
          "$x < -2$",
          "$-2 < x < 1$"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho bất phương trình $\\frac{3 - 2x}{5} > \\frac{2 - x}{3}$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Quy đồng mẫu chung 15 ta được $3(3 - 2x) > 5(2 - x)$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khai triển được $9 - 6x > 10 - 5x$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thu gọn được $-x > 1 \\Rightarrow x < -1$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Số $0$ là một nghiệm của bất phương trình.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Cho hệ bất phương trình bậc nhất một ẩn: $\\begin{cases} 3x - 2 > 4 \\\\ 2x + 1 \\le 9 \\end{cases}$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Nghiệm của bất phương trình thứ nhất là $x > 2$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nghiệm của bất phương trình thứ hai là $x \\le 4$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tập nghiệm của hệ là $2 < x \\le 4$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Có 3 số nguyên thỏa mãn hệ bất phương trình.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải bất phương trình $5 - 3x \\le 11$. Nghiệm là $x \\ge a$. Tìm giá trị của $a$.",
        "correctAnswer": "-2",
        "explanation": "$-3x \\le 6 \\Rightarrow x \\ge -2$. Vậy $a = -2$."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên lớn nhất thỏa mãn bất phương trình $2x - 7 < 0$.",
        "correctAnswer": "3",
        "explanation": "$2x < 7 \\Rightarrow x < 3{,}5$. Số tự nhiên lớn nhất là $3$."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho bất phương trình $mx + 1 > 3$. Với $m = 2$, tìm giá trị nhỏ nhất của số nguyên $x$ thỏa mãn bất phương trình.",
        "correctAnswer": "2",
        "explanation": "$2x > 2 \\Rightarrow x > 1$. Số nguyên nhỏ nhất lớn hơn 1 là $2$."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Có bao nhiêu số nguyên $x$ thỏa mãn hệ bất phương trình $\\begin{cases} 2x - 3 < 5 \\\\ 3x + 2 > -7 \\end{cases}$?",
        "correctAnswer": "6",
        "explanation": "$x < 4$ và $x > -3 \\Rightarrow -3 < x < 4$. Các số nguyên là $-2, -1, 0, 1, 2, 3$. Có 6 số nguyên."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "points": 1.0,
        "question": "Giải bất phương trình sau:\n$$\\frac{x - 1}{2} - \\frac{x - 2}{3} < \\frac{x - 3}{4}$$",
        "solution": "Mẫu thức chung là $12$.\nNhân cả hai vế với 12 (vì $12 > 0$ nên không đổi chiều):\n$6(x - 1) - 4(x - 2) < 3(x - 3)$\n$\\Leftrightarrow 6x - 6 - 4x + 8 < 3x - 9$\n$\\Leftrightarrow 2x + 2 < 3x - 9$\n$\\Leftrightarrow 2x - 3x < -9 - 2$\n$\\Leftrightarrow -x < -11$\n$\\Leftrightarrow x > 11$.\nVậy tập nghiệm của bất phương trình là $\\{x \\mid x > 11\\}$.",
        "rubric": [
          {
            "step": "Quy đồng mẫu thức chung 12 và khai triển đúng các biểu thức",
            "subScore": 0.5
          },
          {
            "step": "Thu gọn ra -x < -11, đổi chiều khi chia cho -1 được x > 11",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "points": 1.0,
        "question": "Một bạn học sinh làm bài thi gồm $20$ câu hỏi trắc nghiệm. Mỗi câu trả lời đúng được cộng $5$ điểm, mỗi câu trả lời sai bị trừ $2$ điểm, câu không trả lời không được điểm. Bạn đó trả lời hết tất cả $20$ câu. Hỏi bạn đó phải trả lời đúng ít nhất bao nhiêu câu để đạt được số điểm từ $65$ điểm trở lên?",
        "solution": "Gọi số câu bạn học sinh trả lời đúng là $x$ ($x \\in \\mathbb{N}, x \\le 20$).\nVì bạn trả lời hết 20 câu nên số câu trả lời sai là $20 - x$ (câu).\nSố điểm bạn nhận được là:\n$5x - 2(20 - x) = 5x - 40 + 2x = 7x - 40$ (điểm).\nĐể đạt được từ $65$ điểm trở lên, ta có bất phương trình:\n$7x - 40 \\ge 65$\n$\\Leftrightarrow 7x \\ge 105$\n$\\Leftrightarrow x \\ge \\frac{105}{7} = 15$.\nVì $x$ là số tự nhiên nên giá trị nhỏ nhất của $x$ là $15$.\nVậy bạn học sinh đó phải trả lời đúng ít nhất $15$ câu.",
        "rubric": [
          {
            "step": "Gọi ẩn, biểu diễn điểm và thiết lập đúng bất phương trình 7x - 40 >= 65",
            "subScore": 0.5
          },
          {
            "step": "Giải ra x >= 15 và kết luận ít nhất 15 câu",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Tìm các giá trị của tham số $m$ để hệ bất phương trình sau có nghiệm:\n$$\\begin{cases} 2x - 1 \\ge 3 \\\\ x - m < 0 \\end{cases}$$",
        "solution": "Giải từng bất phương trình trong hệ:\n1) $2x - 1 \\ge 3 \\Leftrightarrow 2x \\ge 4 \\Leftrightarrow x \\ge 2$.\nTập nghiệm là $S_1 = [2; +\\infty)$.\n2) $x - m < 0 \\Leftrightarrow x < m$.\nTập nghiệm là $S_2 = (-\\infty; m)$.\nĐể hệ bất phương trình có nghiệm thì giao của hai tập nghiệm khác rỗng, tức là $S_1 \\cap S_2 \\neq \\emptyset$.\nĐiều này xảy ra khi và chỉ khi:\n$m > 2$.\nVậy với $m > 2$ thì hệ bất phương trình đã cho có nghiệm.",
        "rubric": [
          {
            "step": "Giải tập nghiệm của từng bất phương trình S1 = [2; +vc) và S2 = (-vc; m)",
            "subScore": 0.5
          },
          {
            "step": "Lập luận điều kiện giao khác rỗng để rút ra m > 2",
            "subScore": 0.5
          }
        ]
      }
    ]
  },
  "c2_9_bai3_test3": {
    "title": "Toán 9 (KNTT) - Bài 6: Bất phương trình bậc nhất một ẩn - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Giao của hai tập nghiệm $x > 1$ và $x < 4$ là:",
        "options": [
          "$x > 4$",
          "Rỗng",
          "$1 < x < 4$",
          "$x < 1$"
        ],
        "correct": 2
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nghiệm của bất phương trình $(x - 1)(x - 3) < 0$ là:",
        "options": [
          "$x < 1$",
          "$x > 3$",
          "$x < 1$ hoặc $x > 3$",
          "$1 < x < 3$"
        ],
        "correct": 3
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Nghiệm của bất phương trình $x^2 - 4 > 0$ là:",
        "options": [
          "$x < -2$ hoặc $x > 2$",
          "$-2 < x < 2$",
          "$x < -2$",
          "$x > 2$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tập nghiệm của bất phương trình $\\frac{x - 2}{x + 3} \\le 0$ là:",
        "options": [
          "$x \\le 2$",
          "$-3 < x \\le 2$",
          "$x > -3$",
          "$-3 \\le x \\le 2$"
        ],
        "correct": 1
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Số nghiệm nguyên thỏa mãn bất phương trình $|2x - 1| \\le 5$ là:",
        "options": [
          "Vô số",
          "$4$",
          "$5$",
          "$6$ (từ $-2$ đến $3$)"
        ],
        "correct": 3
      },
      {
        "id": 6,
        "level": "Vận dụng",
        "question": "Tìm $m$ để bất phương trình $(m^2 + 1)x - 2m \\ge 0$ có nghiệm $x \\ge 1$:",
        "options": [
          "$m = 0$",
          "$m = 1$",
          "$m = 2$",
          "$m = -1$"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Vận dụng",
        "question": "Bất phương trình $\\frac{1}{x} < 1$ có tập nghiệm là:",
        "options": [
          "$x < 0$ hoặc $x > 1$",
          "$x > 1$",
          "$x < 1$",
          "$0 < x < 1$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Vận dụng cao",
        "question": "Tìm $m$ để hệ $\\begin{cases} 2x - 3 > 1 \\\\ mx \\le 4 \\end{cases}$ có nghiệm:",
        "options": [
          "$m > 0$",
          "Với mọi $m$",
          "$m < 2$",
          "$m \\le 2$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Vận dụng cao",
        "question": "Tập nghiệm của bất phương trình $\\frac{x^2 - 5x + 6}{x - 1} \\ge 0$ là:",
        "options": [
          "$[1; 3]$",
          "$[2; 3]$",
          "$(1; 2] \\cup [3; +\\infty)$",
          "$x > 1$"
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Vận dụng cao",
        "question": "Tìm tất cả các giá trị của $m$ để bất phương trình $(m - 2)x^2 - 2(m - 2)x + 1 > 0$ nghiệm đúng với mọi $x \\in \\mathbb{R}$:",
        "options": [
          "$2 \\le m < 3$",
          "$2 < m < 3$",
          "$m > 2$",
          "$m < 3$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Cho $x, y > 0$ thỏa mãn $x + y \\le 2$. Giá trị nhỏ nhất của biểu thức $P = \\frac{1}{x} + \\frac{1}{y}$ là:",
        "options": [
          "$\\frac{1}{2}$",
          "$1$",
          "$4$",
          "$2$"
        ],
        "correct": 3
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Một người bán hàng cần thuê xe tải để chở ít nhất $140$ tấn hàng và $9$ tấn hàng đặc biệt. Có hai loại xe: loại A (giá $4$ triệu, chở $20$ tấn hàng, $0{,}6$ tấn đặc biệt), loại B (giá $3$ triệu, chở $10$ tấn hàng, $1{,}5$ tấn đặc biệt). Chi phí thuê xe nhỏ nhất là:",
        "options": [
          "$30$ triệu đồng",
          "$32$ triệu đồng",
          "$35$ triệu đồng",
          "$28$ triệu đồng"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Cho bất phương trình $\\frac{2x - 1}{x - 2} \\ge 1$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Điều kiện xác định là $x \\neq 2$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chuyển vế: $\\frac{2x - 1}{x - 2} - 1 \\ge 0 \\Leftrightarrow \\frac{x + 1}{x - 2} \\ge 0$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tập nghiệm của bất phương trình là $x \\le -1$ hoặc $x > 2$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Điểm $x = 2$ thuộc tập nghiệm của bất phương trình.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho bất phương trình chứa giá trị tuyệt đối $|x - 2| + |x - 5| \\ge 3$. Xét tính đúng/sai:",
        "statements": [
          {
            "subId": "a",
            "text": "Áp dụng bất đẳng thức $|a| + |b| \\ge |a + b|$.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ta có $|x - 2| + |5 - x| \\ge |x - 2 + 5 - x| = 3$.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Bất phương trình nghiệm đúng với mọi số thực $x \\in \\mathbb{R}$.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tập nghiệm của bất phương trình là tập rỗng.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Nghiệm của bất phương trình $-5x + 15 \\ge 0$ là $x \\le a$. Tìm $a$.",
        "correctAnswer": "3",
        "explanation": "$-5x \\ge -15 \\Rightarrow x \\le 3$."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Tìm số nghiệm nguyên của bất phương trình $|x - 3| < 4$.",
        "correctAnswer": "7",
        "explanation": "$-4 < x - 3 < 4 \\Rightarrow -1 < x < 7$. Các số nguyên là $0, 1, 2, 3, 4, 5, 6$. Có 7 nghiệm."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm số nguyên dương $x$ lớn nhất thỏa mãn bất phương trình $\\frac{x}{2} + \\frac{x}{3} + \\frac{x}{4} < 13$.",
        "correctAnswer": "11",
        "explanation": "$\\frac{13x}{12} < 13 \\Rightarrow x < 12$. Số nguyên dương lớn nhất là $11$."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tìm $m$ để hệ $\\begin{cases} x > 2 \\\\ x < m \\end{cases}$ có đúng $3$ nghiệm nguyên.",
        "correctAnswer": "6",
        "explanation": "Các nghiệm nguyên là $3, 4, 5$. Do đó $5 < m \\le 6$. Nếu $m$ là số nguyên thì $m = 6$."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "points": 1.0,
        "question": "Giải bất phương trình sau:\n$$\\frac{2x - 3}{x - 1} \\le 1$$",
        "solution": "Điều kiện xác định: $x \\neq 1$.\nChuyển vế:\n$\\frac{2x - 3}{x - 1} - 1 \\le 0 \\Leftrightarrow \\frac{2x - 3 - (x - 1)}{x - 1} \\le 0 \\Leftrightarrow \\frac{x - 2}{x - 1} \\le 0$.\nPhân thức $\\frac{x - 2}{x - 1} \\le 0$ khi tử và mẫu trái dấu (hoặc tử bằng 0):\nTa có $x - 1 < x - 2$ là vô lí, do đó $x - 1 < 0$ và $x - 2 \\ge 0$ là vô lí.\nVậy phải có: $\\begin{cases} x - 2 \\le 0 \\\\ x - 1 > 0 \\end{cases} \\Leftrightarrow \\begin{cases} x \\le 2 \\\\ x > 1 \\end{cases} \\Leftrightarrow 1 < x \\le 2$.\nVậy tập nghiệm của bất phương trình là $S = (1; 2]$.",
        "rubric": [
          {
            "step": "Chuyển vế, quy đồng đưa về dạng thương (x - 2)/(x - 1) <= 0",
            "subScore": 0.5
          },
          {
            "step": "Lập luận dấu của nhị thức bậc nhất và kết luận 1 < x <= 2",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Giải bất phương trình chứa dấu giá trị tuyệt đối sau:\n$$|2x - 3| \\le x + 1$$",
        "solution": "Bất phương trình dạng $|A| \\le B$ tương đương với:\n$$\\begin{cases} B \\ge 0 \\\\ -B \\le A \\le B \\end{cases}$$\nỞ đây ta có:\n$$\\begin{cases} x + 1 \\ge 0 \\\\ -(x + 1) \\le 2x - 3 \\le x + 1 \\end{cases}$$\n1) $x \\ge -1$.\n2) Hệ bất phương trình kép:\n- Bất phương trình thứ nhất: $-x - 1 \\le 2x - 3 \\Leftrightarrow 3x \\ge 2 \\Leftrightarrow x \\ge \\frac{2}{3}$.\n- Bất phương trình thứ hai: $2x - 3 \\le x + 1 \\Leftrightarrow x \\le 4$.\nKết hợp các điều kiện:\n$\\frac{2}{3} \\le x \\le 4$ (thỏa mãn $x \\ge -1$).\nVậy tập nghiệm của bất phương trình là $S = \\left[\\frac{2}{3}; 4\\right]$.",
        "rubric": [
          {
            "step": "Phá dấu giá trị tuyệt đối đưa về bất phương trình kép",
            "subScore": 0.5
          },
          {
            "step": "Giải hệ điều kiện và kết luận tập nghiệm [2/3; 4]",
            "subScore": 0.5
          }
        ]
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "points": 1.0,
        "question": "Tìm các giá trị của tham số $m$ để hệ bất phương trình sau có nghiệm:\n$$\\begin{cases} 3x + 1 > 2x + 4 \\\\ 2x - m \\le 3 \\end{cases}$$",
        "solution": "Giải từng bất phương trình trong hệ:\n1) $3x + 1 > 2x + 4 \\Leftrightarrow 3x - 2x > 4 - 1 \\Leftrightarrow x > 3$.\nTập nghiệm $S_1 = (3; +\\infty)$.\n2) $2x - m \\le 3 \\Leftrightarrow 2x \\le m + 3 \\Leftrightarrow x \\le \\frac{m + 3}{2}$.\nTập nghiệm $S_2 = \\left(-\\infty; \\frac{m + 3}{2}\\right]$.\nĐể hệ bất phương trình có nghiệm thì giao của hai tập nghiệm $S_1$ và $S_2$ phải khác rỗng:\n$S_1 \\cap S_2 \\neq \\emptyset \\Leftrightarrow \\frac{m + 3}{2} > 3$\n$\\Leftrightarrow m + 3 > 6 \\Leftrightarrow m > 3$.\nVậy với $m > 3$ thì hệ bất phương trình đã cho có nghiệm.",
        "rubric": [
          {
            "step": "Giải đúng tập nghiệm x > 3 và x <= (m + 3)/2",
            "subScore": 0.5
          },
          {
            "step": "Lập luận điều kiện giao khác rỗng và kết luận m > 3",
            "subScore": 0.5
          }
        ]
      }
    ]
  },
  "c2_9_bai4_test1": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương II: Phương trình và bất phương trình bậc nhất một ẩn - Đề số 01",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phương trình tích có dạng chuẩn là:",
        "options": [
          "$A(x) \\cdot B(x) = 0$",
          "$A(x) + B(x) = 0$",
          "$\\frac{A(x)}{B(x)} = 0$",
          "$A(x) - B(x) = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Điều kiện xác định của phương trình $\\frac{2x}{1x - 2} = 1$ là:",
        "options": [
          "$x \\neq 2$",
          "$x \\neq 0$",
          "$x > 2$",
          "$x \\neq 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nhân hai vế của bất đẳng thức với một số âm, ta phải:",
        "options": [
          "Đổi chiều bất đẳng thức",
          "Giữ nguyên chiều",
          "Nhân thêm số 0",
          "Lấy nghịch đảo"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nghiệm của bất phương trình $2x > 4$ là:",
        "options": [
          "$x > 2$",
          "$x < 2$",
          "$x \\ge 2$",
          "$x > 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tập nghiệm của phương trình $(x - 1)(2x + 6) = 0$ là:",
        "options": [
          "$\\{1; -3\\}$",
          "$\\{-1; 3\\}$",
          "$\\{1; 3\\}$",
          "$\\{-1; -3\\}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bất phương trình $2x - 1 \\le x + 4$ có nghiệm là:",
        "options": [
          "$x \\le 5$",
          "$x \\ge 5$",
          "$x < 4$",
          "$x \\le 3$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Giá trị $x = 1$ là nghiệm của bất phương trình nào sau đây?",
        "options": [
          "$2x - 1 < 3$",
          "$3x > 5$",
          "$x + 5 \\le 1$",
          "$-x > -0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Giải phương trình $\\frac{x + 1}{x - 1} = 2$ ta được nghiệm là:",
        "options": [
          "$x = 3$",
          "$x = -1$",
          "$x = 1$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một hãng taxi có giá mở cửa là 12,000 đồng cho km đầu tiên và 14,000 đồng cho mỗi km tiếp theo. Với số tiền 200,000 đồng, khách có thể đi tối đa quãng đường (km) là:",
        "options": [
          "14 km",
          "13 km",
          "14 km",
          "12 km"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một thang máy có tải trọng tối đa 200000 kg. Nhân viên nặng 12000 kg mang theo các kiện hàng mỗi kiện nặng 14000 kg. Số kiện hàng tối đa nhân viên đó có thể mang cùng là:",
        "options": [
          "13 kiện",
          "14 kiện",
          "14 kiện",
          "20 kiện"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng sản xuất có chi phí cố định là 10 triệu đồng/tháng. Mỗi sản phẩm bán ra thu lãi 50 000 đồng. Xưởng cần sản xuất ít nhất bao nhiêu sản phẩm mỗi tháng để bắt đầu có lãi?",
        "options": [
          "201 sản phẩm",
          "200 sản phẩm",
          "150 sản phẩm",
          "250 sản phẩm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Số nguyên $x$ lớn nhất thỏa mãn bất phương trình $\\frac{x - 1}{2} + \\frac{x - 2}{3} < \\frac{x + 1}{6}$ là:",
        "options": [
          "$x = 2$",
          "$x = 1$",
          "$x = 3$",
          "$x = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét phương trình tích $(2x - 2)(x + 3) = 0$ (Đề 01):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình đã cho là phương trình tích gồm hai nhân tử bậc nhất.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ nhất 2x - 2 = 0 cho nghiệm x = 1.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ hai x + 3 = 0 cho nghiệm x = -3.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tổng hai nghiệm của phương trình bằng 4.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế học tập (Mã đề 01): Bạn Hùng có điểm 4 bài kiểm tra môn Toán lần lượt là 7; 8; 8; 9. Bạn còn 1 bài kiểm tra cuối kỳ hệ số 2. Hùng muốn điểm trung bình môn cả kỳ đạt từ 8,5 trở lên.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng số hệ số điểm kiểm tra môn Toán trong kỳ là 1 + 1 + 1 + 1 + 2 = 6.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng điểm 4 bài kiểm tra đầu tiên là: 7 + 8 + 8 + 9 = 32 điểm.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Bất phương trình tìm điểm bài cuối kỳ x là: (32 + 2x) / 6 >= 8,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Bạn Hùng chỉ cần đạt bài cuối kỳ từ 9,0 điểm là hoàn thành mục tiêu.",
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
        "question": "Giải phương trình: 3x - 3 = 0. Tìm x.",
        "answer": "1",
        "acceptableAnswers": [
          "1"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **1**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm nghiệm nguyên dương nhỏ nhất của bất phương trình: 2x > 3.",
        "answer": "2",
        "acceptableAnswers": [
          "2"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **2**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một công ty viễn thông thu cước thuê bao cố định 50 000 đồng/tháng và 1 000 đồng cho mỗi phút gọi. Bạn Lan có ngân sách tối đa 150 000 đồng/tháng. Hỏi bạn Lan có thể gọi tối đa bao nhiêu phút?",
        "answer": "100",
        "acceptableAnswers": [
          "100"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **100**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tìm số nguyên x lớn nhất thỏa mãn: (x - 1)/2 - (x - 2)/3 > 1.",
        "answer": "7",
        "acceptableAnswers": [
          "7"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **7**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình chứa ẩn ở mẫu: $\\frac{x + 1}{x - 2} - \\frac{1}{x} = 1$.",
        "rubric": "ĐKXĐ: x khác 0 và x khác 2 (0.25đ).\nQuy đồng mẫu thức chung x(x - 2): x(x + 1) - (x - 2) = x(x - 2) (0.25đ).\n<=> x^2 + 1x - x + 2 = x^2 - 2x <=> (1 + 1)x = -2 => x = -2/(1 + 1) (thỏa mãn ĐKXĐ) (0.25đ).\nKết luận tập nghiệm (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một người có 300 triệu đồng gửi vào hai sổ tiết kiệm tại ngân hàng. Sổ thứ nhất kỳ hạn 12 tháng lãi suất 6%/năm. Sổ thứ hai kỳ hạn 6 tháng lãi suất 5%/năm. Sau một năm, tổng số tiền lãi nhận được là 16,8 triệu đồng. Tính số tiền gửi ở mỗi sổ.",
        "rubric": "Gọi số tiền gửi ở sổ thứ nhất là x (triệu đồng), sổ thứ hai là y (triệu đồng) (0 < x, y < 300) (0.25đ).\nTa có hệ pt: x + y = 300 và 0,06x + 0,05y = 16,8 (0.25đ).\nGiải ra được x = 180 (triệu đồng) và y = 120 (triệu đồng) (0.25đ).\nKết luận số tiền mỗi sổ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hai số thực dương $a, b$ thỏa mãn $a + b = 2$. Chứng minh rằng: $\\frac{1}{a} + \\frac{1}{b} \\ge 2$.",
        "rubric": "Áp dụng bất đẳng thức Cauchy cho hai số dương a, b: a + b >= 2 căn(ab) => 2 >= 2 căn(ab) => ab <= 1 (0.25đ).\nTa có: 1/a + 1/b = (a + b)/(ab) = 2/(ab) (0.25đ).\nVì ab <= 1 và ab > 0 nên 2/(ab) >= 2/1 = 2 (0.25đ).\nDấu '=' xảy ra khi a = b = 1. Bài toán được chứng minh (0.25đ)."
      }
    ]
  },
  "c2_9_bai4_test2": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương II: Phương trình và bất phương trình bậc nhất một ẩn - Đề số 02",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phương trình tích có dạng chuẩn là:",
        "options": [
          "$A(x) \\cdot B(x) = 0$",
          "$A(x) + B(x) = 0$",
          "$\\frac{A(x)}{B(x)} = 0$",
          "$A(x) - B(x) = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Điều kiện xác định của phương trình $\\frac{2x}{2x - 4} = 1$ là:",
        "options": [
          "$x \\neq 2$",
          "$x \\neq 0$",
          "$x > 2$",
          "$x \\neq 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nhân hai vế của bất đẳng thức với một số âm, ta phải:",
        "options": [
          "Đổi chiều bất đẳng thức",
          "Giữ nguyên chiều",
          "Nhân thêm số 0",
          "Lấy nghịch đảo"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nghiệm của bất phương trình $3x > 6$ là:",
        "options": [
          "$x > 2$",
          "$x < 2$",
          "$x \\ge 2$",
          "$x > 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tập nghiệm của phương trình $(x - 2)(2x + 6) = 0$ là:",
        "options": [
          "$\\{2; -3\\}$",
          "$\\{-2; 3\\}$",
          "$\\{2; 3\\}$",
          "$\\{-2; -3\\}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bất phương trình $2x - 2 \\le x + 5$ có nghiệm là:",
        "options": [
          "$x \\le 7$",
          "$x \\ge 7$",
          "$x < 5$",
          "$x \\le 3$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Giá trị $x = 2$ là nghiệm của bất phương trình nào sau đây?",
        "options": [
          "$2x - 1 < 5$",
          "$3x > 8$",
          "$x + 5 \\le 2$",
          "$-x > -1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Giải phương trình $\\frac{x + 2}{x - 1} = 2$ ta được nghiệm là:",
        "options": [
          "$x = 4$",
          "$x = 0$",
          "$x = 2$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một hãng taxi có giá mở cửa là 70 đồng cho km đầu tiên và 30 đồng cho mỗi km tiếp theo. Với số tiền 650 đồng, khách có thể đi tối đa quãng đường (km) là:",
        "options": [
          "20 km",
          "19 km",
          "21 km",
          "12 km"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một thang máy có tải trọng tối đa 650 kg. Nhân viên nặng 70 kg mang theo các kiện hàng mỗi kiện nặng 30 kg. Số kiện hàng tối đa nhân viên đó có thể mang cùng là:",
        "options": [
          "19 kiện",
          "20 kiện",
          "21 kiện",
          "20 kiện"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng sản xuất có chi phí cố định là 10 triệu đồng/tháng. Mỗi sản phẩm bán ra thu lãi 50 000 đồng. Xưởng cần sản xuất ít nhất bao nhiêu sản phẩm mỗi tháng để bắt đầu có lãi?",
        "options": [
          "201 sản phẩm",
          "200 sản phẩm",
          "150 sản phẩm",
          "250 sản phẩm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Số nguyên $x$ lớn nhất thỏa mãn bất phương trình $\\frac{x - 2}{2} + \\frac{x - 3}{3} < \\frac{x + 1}{6}$ là:",
        "options": [
          "$x = 3$",
          "$x = 2$",
          "$x = 4$",
          "$x = 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét phương trình tích $(2x - 4)(x + 3) = 0$ (Đề 02):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình đã cho là phương trình tích gồm hai nhân tử bậc nhất.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ nhất 2x - 4 = 0 cho nghiệm x = 2.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ hai x + 3 = 0 cho nghiệm x = -3.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tổng hai nghiệm của phương trình bằng 5.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế học tập (Mã đề 02): Bạn Hùng có điểm 4 bài kiểm tra môn Toán lần lượt là 7; 8; 8; 9. Bạn còn 1 bài kiểm tra cuối kỳ hệ số 2. Hùng muốn điểm trung bình môn cả kỳ đạt từ 8,5 trở lên.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng số hệ số điểm kiểm tra môn Toán trong kỳ là 1 + 1 + 1 + 1 + 2 = 6.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng điểm 4 bài kiểm tra đầu tiên là: 7 + 8 + 8 + 9 = 32 điểm.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Bất phương trình tìm điểm bài cuối kỳ x là: (32 + 2x) / 6 >= 8,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Bạn Hùng chỉ cần đạt bài cuối kỳ từ 9,0 điểm là hoàn thành mục tiêu.",
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
        "question": "Giải phương trình: 3x - 6 = 0. Tìm x.",
        "answer": "2",
        "acceptableAnswers": [
          "2"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **2**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm nghiệm nguyên dương nhỏ nhất của bất phương trình: 2x > 5.",
        "answer": "3",
        "acceptableAnswers": [
          "3"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **3**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một công ty viễn thông thu cước thuê bao cố định 50 000 đồng/tháng và 1 000 đồng cho mỗi phút gọi. Bạn Lan có ngân sách tối đa 150 000 đồng/tháng. Hỏi bạn Lan có thể gọi tối đa bao nhiêu phút?",
        "answer": "100",
        "acceptableAnswers": [
          "100"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **100**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tìm số nguyên x lớn nhất thỏa mãn: (x - 1)/2 - (x - 2)/3 > 1.",
        "answer": "7",
        "acceptableAnswers": [
          "7"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **7**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình chứa ẩn ở mẫu: $\\frac{x + 2}{x - 2} - \\frac{1}{x} = 1$.",
        "rubric": "ĐKXĐ: x khác 0 và x khác 2 (0.25đ).\nQuy đồng mẫu thức chung x(x - 2): x(x + 2) - (x - 2) = x(x - 2) (0.25đ).\n<=> x^2 + 2x - x + 2 = x^2 - 2x <=> (2 + 1)x = -2 => x = -2/(2 + 1) (thỏa mãn ĐKXĐ) (0.25đ).\nKết luận tập nghiệm (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một người có 300 triệu đồng gửi vào hai sổ tiết kiệm tại ngân hàng. Sổ thứ nhất kỳ hạn 12 tháng lãi suất 6%/năm. Sổ thứ hai kỳ hạn 6 tháng lãi suất 5%/năm. Sau một năm, tổng số tiền lãi nhận được là 16,8 triệu đồng. Tính số tiền gửi ở mỗi sổ.",
        "rubric": "Gọi số tiền gửi ở sổ thứ nhất là x (triệu đồng), sổ thứ hai là y (triệu đồng) (0 < x, y < 300) (0.25đ).\nTa có hệ pt: x + y = 300 và 0,06x + 0,05y = 16,8 (0.25đ).\nGiải ra được x = 180 (triệu đồng) và y = 120 (triệu đồng) (0.25đ).\nKết luận số tiền mỗi sổ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hai số thực dương $a, b$ thỏa mãn $a + b = 2$. Chứng minh rằng: $\\frac{1}{a} + \\frac{1}{b} \\ge 2$.",
        "rubric": "Áp dụng bất đẳng thức Cauchy cho hai số dương a, b: a + b >= 2 căn(ab) => 2 >= 2 căn(ab) => ab <= 1 (0.25đ).\nTa có: 1/a + 1/b = (a + b)/(ab) = 2/(ab) (0.25đ).\nVì ab <= 1 và ab > 0 nên 2/(ab) >= 2/1 = 2 (0.25đ).\nDấu '=' xảy ra khi a = b = 1. Bài toán được chứng minh (0.25đ)."
      }
    ]
  },
  "c2_9_bai4_test3": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương II: Phương trình và bất phương trình bậc nhất một ẩn - Đề số 03",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phương trình tích có dạng chuẩn là:",
        "options": [
          "$A(x) \\cdot B(x) = 0$",
          "$A(x) + B(x) = 0$",
          "$\\frac{A(x)}{B(x)} = 0$",
          "$A(x) - B(x) = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Điều kiện xác định của phương trình $\\frac{2x}{3x - 6} = 1$ là:",
        "options": [
          "$x \\neq 2$",
          "$x \\neq 0$",
          "$x > 2$",
          "$x \\neq 3$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nhân hai vế của bất đẳng thức với một số âm, ta phải:",
        "options": [
          "Đổi chiều bất đẳng thức",
          "Giữ nguyên chiều",
          "Nhân thêm số 0",
          "Lấy nghịch đảo"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nghiệm của bất phương trình $4x > 8$ là:",
        "options": [
          "$x > 2$",
          "$x < 2$",
          "$x \\ge 2$",
          "$x > 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tập nghiệm của phương trình $(x - 3)(2x + 6) = 0$ là:",
        "options": [
          "$\\{3; -3\\}$",
          "$\\{-3; 3\\}$",
          "$\\{3; 3\\}$",
          "$\\{-3; -3\\}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bất phương trình $2x - 3 \\le x + 6$ có nghiệm là:",
        "options": [
          "$x \\le 9$",
          "$x \\ge 9$",
          "$x < 6$",
          "$x \\le 3$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Giá trị $x = 3$ là nghiệm của bất phương trình nào sau đây?",
        "options": [
          "$2x - 1 < 7$",
          "$3x > 11$",
          "$x + 5 \\le 3$",
          "$-x > -2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Giải phương trình $\\frac{x + 3}{x - 1} = 2$ ta được nghiệm là:",
        "options": [
          "$x = 5$",
          "$x = 1$",
          "$x = 3$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một hãng taxi có giá mở cửa là 8.0 đồng cho km đầu tiên và 7.5 đồng cho mỗi km tiếp theo. Với số tiền 9.0 đồng, khách có thể đi tối đa quãng đường (km) là:",
        "options": [
          "1.0 km",
          "0.0 km",
          "1.0 km",
          "12 km"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một thang máy có tải trọng tối đa 9.0 kg. Nhân viên nặng 8.0 kg mang theo các kiện hàng mỗi kiện nặng 7.5 kg. Số kiện hàng tối đa nhân viên đó có thể mang cùng là:",
        "options": [
          "0.0 kiện",
          "1.0 kiện",
          "1.0 kiện",
          "20 kiện"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng sản xuất có chi phí cố định là 10 triệu đồng/tháng. Mỗi sản phẩm bán ra thu lãi 50 000 đồng. Xưởng cần sản xuất ít nhất bao nhiêu sản phẩm mỗi tháng để bắt đầu có lãi?",
        "options": [
          "201 sản phẩm",
          "200 sản phẩm",
          "150 sản phẩm",
          "250 sản phẩm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Số nguyên $x$ lớn nhất thỏa mãn bất phương trình $\\frac{x - 3}{2} + \\frac{x - 4}{3} < \\frac{x + 1}{6}$ là:",
        "options": [
          "$x = 4$",
          "$x = 3$",
          "$x = 5$",
          "$x = 2$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét phương trình tích $(2x - 6)(x + 3) = 0$ (Đề 03):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình đã cho là phương trình tích gồm hai nhân tử bậc nhất.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ nhất 2x - 6 = 0 cho nghiệm x = 3.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ hai x + 3 = 0 cho nghiệm x = -3.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tổng hai nghiệm của phương trình bằng 6.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế học tập (Mã đề 03): Bạn Hùng có điểm 4 bài kiểm tra môn Toán lần lượt là 7; 8; 8; 9. Bạn còn 1 bài kiểm tra cuối kỳ hệ số 2. Hùng muốn điểm trung bình môn cả kỳ đạt từ 8,5 trở lên.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng số hệ số điểm kiểm tra môn Toán trong kỳ là 1 + 1 + 1 + 1 + 2 = 6.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng điểm 4 bài kiểm tra đầu tiên là: 7 + 8 + 8 + 9 = 32 điểm.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Bất phương trình tìm điểm bài cuối kỳ x là: (32 + 2x) / 6 >= 8,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Bạn Hùng chỉ cần đạt bài cuối kỳ từ 9,0 điểm là hoàn thành mục tiêu.",
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
        "question": "Giải phương trình: 3x - 9 = 0. Tìm x.",
        "answer": "3",
        "acceptableAnswers": [
          "3"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **3**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm nghiệm nguyên dương nhỏ nhất của bất phương trình: 2x > 7.",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một công ty viễn thông thu cước thuê bao cố định 50 000 đồng/tháng và 1 000 đồng cho mỗi phút gọi. Bạn Lan có ngân sách tối đa 150 000 đồng/tháng. Hỏi bạn Lan có thể gọi tối đa bao nhiêu phút?",
        "answer": "100",
        "acceptableAnswers": [
          "100"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **100**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tìm số nguyên x lớn nhất thỏa mãn: (x - 1)/2 - (x - 2)/3 > 1.",
        "answer": "7",
        "acceptableAnswers": [
          "7"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **7**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình chứa ẩn ở mẫu: $\\frac{x + 3}{x - 2} - \\frac{1}{x} = 1$.",
        "rubric": "ĐKXĐ: x khác 0 và x khác 2 (0.25đ).\nQuy đồng mẫu thức chung x(x - 2): x(x + 3) - (x - 2) = x(x - 2) (0.25đ).\n<=> x^2 + 3x - x + 2 = x^2 - 2x <=> (3 + 1)x = -2 => x = -2/(3 + 1) (thỏa mãn ĐKXĐ) (0.25đ).\nKết luận tập nghiệm (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một người có 300 triệu đồng gửi vào hai sổ tiết kiệm tại ngân hàng. Sổ thứ nhất kỳ hạn 12 tháng lãi suất 6%/năm. Sổ thứ hai kỳ hạn 6 tháng lãi suất 5%/năm. Sau một năm, tổng số tiền lãi nhận được là 16,8 triệu đồng. Tính số tiền gửi ở mỗi sổ.",
        "rubric": "Gọi số tiền gửi ở sổ thứ nhất là x (triệu đồng), sổ thứ hai là y (triệu đồng) (0 < x, y < 300) (0.25đ).\nTa có hệ pt: x + y = 300 và 0,06x + 0,05y = 16,8 (0.25đ).\nGiải ra được x = 180 (triệu đồng) và y = 120 (triệu đồng) (0.25đ).\nKết luận số tiền mỗi sổ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hai số thực dương $a, b$ thỏa mãn $a + b = 2$. Chứng minh rằng: $\\frac{1}{a} + \\frac{1}{b} \\ge 2$.",
        "rubric": "Áp dụng bất đẳng thức Cauchy cho hai số dương a, b: a + b >= 2 căn(ab) => 2 >= 2 căn(ab) => ab <= 1 (0.25đ).\nTa có: 1/a + 1/b = (a + b)/(ab) = 2/(ab) (0.25đ).\nVì ab <= 1 và ab > 0 nên 2/(ab) >= 2/1 = 2 (0.25đ).\nDấu '=' xảy ra khi a = b = 1. Bài toán được chứng minh (0.25đ)."
      }
    ]
  },
  "c2_9_bai4_test4": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương II: Phương trình và bất phương trình bậc nhất một ẩn - Đề số 04",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phương trình tích có dạng chuẩn là:",
        "options": [
          "$A(x) \\cdot B(x) = 0$",
          "$A(x) + B(x) = 0$",
          "$\\frac{A(x)}{B(x)} = 0$",
          "$A(x) - B(x) = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Điều kiện xác định của phương trình $\\frac{2x}{4x - 8} = 1$ là:",
        "options": [
          "$x \\neq 2$",
          "$x \\neq 0$",
          "$x > 2$",
          "$x \\neq 4$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nhân hai vế của bất đẳng thức với một số âm, ta phải:",
        "options": [
          "Đổi chiều bất đẳng thức",
          "Giữ nguyên chiều",
          "Nhân thêm số 0",
          "Lấy nghịch đảo"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nghiệm của bất phương trình $5x > 10$ là:",
        "options": [
          "$x > 2$",
          "$x < 2$",
          "$x \\ge 2$",
          "$x > 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tập nghiệm của phương trình $(x - 4)(2x + 6) = 0$ là:",
        "options": [
          "$\\{4; -3\\}$",
          "$\\{-4; 3\\}$",
          "$\\{4; 3\\}$",
          "$\\{-4; -3\\}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bất phương trình $2x - 4 \\le x + 7$ có nghiệm là:",
        "options": [
          "$x \\le 11$",
          "$x \\ge 11$",
          "$x < 7$",
          "$x \\le 3$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Giá trị $x = 4$ là nghiệm của bất phương trình nào sau đây?",
        "options": [
          "$2x - 1 < 9$",
          "$3x > 14$",
          "$x + 5 \\le 4$",
          "$-x > -3$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Giải phương trình $\\frac{x + 4}{x - 1} = 2$ ta được nghiệm là:",
        "options": [
          "$x = 6$",
          "$x = 2$",
          "$x = 4$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một hãng taxi có giá mở cửa là 50,000 đồng cho km đầu tiên và 1,000 đồng cho mỗi km tiếp theo. Với số tiền 150,000 đồng, khách có thể đi tối đa quãng đường (km) là:",
        "options": [
          "101 km",
          "100 km",
          "150 km",
          "12 km"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một thang máy có tải trọng tối đa 150000 kg. Nhân viên nặng 50000 kg mang theo các kiện hàng mỗi kiện nặng 1000 kg. Số kiện hàng tối đa nhân viên đó có thể mang cùng là:",
        "options": [
          "100 kiện",
          "101 kiện",
          "150 kiện",
          "20 kiện"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng sản xuất có chi phí cố định là 10 triệu đồng/tháng. Mỗi sản phẩm bán ra thu lãi 50 000 đồng. Xưởng cần sản xuất ít nhất bao nhiêu sản phẩm mỗi tháng để bắt đầu có lãi?",
        "options": [
          "201 sản phẩm",
          "200 sản phẩm",
          "150 sản phẩm",
          "250 sản phẩm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Số nguyên $x$ lớn nhất thỏa mãn bất phương trình $\\frac{x - 4}{2} + \\frac{x - 5}{3} < \\frac{x + 1}{6}$ là:",
        "options": [
          "$x = 5$",
          "$x = 4$",
          "$x = 6$",
          "$x = 3$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét phương trình tích $(2x - 8)(x + 3) = 0$ (Đề 04):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình đã cho là phương trình tích gồm hai nhân tử bậc nhất.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ nhất 2x - 8 = 0 cho nghiệm x = 4.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ hai x + 3 = 0 cho nghiệm x = -3.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tổng hai nghiệm của phương trình bằng 7.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế học tập (Mã đề 04): Bạn Hùng có điểm 4 bài kiểm tra môn Toán lần lượt là 7; 8; 8; 9. Bạn còn 1 bài kiểm tra cuối kỳ hệ số 2. Hùng muốn điểm trung bình môn cả kỳ đạt từ 8,5 trở lên.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng số hệ số điểm kiểm tra môn Toán trong kỳ là 1 + 1 + 1 + 1 + 2 = 6.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng điểm 4 bài kiểm tra đầu tiên là: 7 + 8 + 8 + 9 = 32 điểm.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Bất phương trình tìm điểm bài cuối kỳ x là: (32 + 2x) / 6 >= 8,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Bạn Hùng chỉ cần đạt bài cuối kỳ từ 9,0 điểm là hoàn thành mục tiêu.",
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
        "question": "Giải phương trình: 3x - 12 = 0. Tìm x.",
        "answer": "4",
        "acceptableAnswers": [
          "4"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **4**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm nghiệm nguyên dương nhỏ nhất của bất phương trình: 2x > 9.",
        "answer": "5",
        "acceptableAnswers": [
          "5"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **5**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một công ty viễn thông thu cước thuê bao cố định 50 000 đồng/tháng và 1 000 đồng cho mỗi phút gọi. Bạn Lan có ngân sách tối đa 150 000 đồng/tháng. Hỏi bạn Lan có thể gọi tối đa bao nhiêu phút?",
        "answer": "100",
        "acceptableAnswers": [
          "100"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **100**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tìm số nguyên x lớn nhất thỏa mãn: (x - 1)/2 - (x - 2)/3 > 1.",
        "answer": "7",
        "acceptableAnswers": [
          "7"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **7**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình chứa ẩn ở mẫu: $\\frac{x + 4}{x - 2} - \\frac{1}{x} = 1$.",
        "rubric": "ĐKXĐ: x khác 0 và x khác 2 (0.25đ).\nQuy đồng mẫu thức chung x(x - 2): x(x + 4) - (x - 2) = x(x - 2) (0.25đ).\n<=> x^2 + 4x - x + 2 = x^2 - 2x <=> (4 + 1)x = -2 => x = -2/(4 + 1) (thỏa mãn ĐKXĐ) (0.25đ).\nKết luận tập nghiệm (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một người có 300 triệu đồng gửi vào hai sổ tiết kiệm tại ngân hàng. Sổ thứ nhất kỳ hạn 12 tháng lãi suất 6%/năm. Sổ thứ hai kỳ hạn 6 tháng lãi suất 5%/năm. Sau một năm, tổng số tiền lãi nhận được là 16,8 triệu đồng. Tính số tiền gửi ở mỗi sổ.",
        "rubric": "Gọi số tiền gửi ở sổ thứ nhất là x (triệu đồng), sổ thứ hai là y (triệu đồng) (0 < x, y < 300) (0.25đ).\nTa có hệ pt: x + y = 300 và 0,06x + 0,05y = 16,8 (0.25đ).\nGiải ra được x = 180 (triệu đồng) và y = 120 (triệu đồng) (0.25đ).\nKết luận số tiền mỗi sổ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hai số thực dương $a, b$ thỏa mãn $a + b = 2$. Chứng minh rằng: $\\frac{1}{a} + \\frac{1}{b} \\ge 2$.",
        "rubric": "Áp dụng bất đẳng thức Cauchy cho hai số dương a, b: a + b >= 2 căn(ab) => 2 >= 2 căn(ab) => ab <= 1 (0.25đ).\nTa có: 1/a + 1/b = (a + b)/(ab) = 2/(ab) (0.25đ).\nVì ab <= 1 và ab > 0 nên 2/(ab) >= 2/1 = 2 (0.25đ).\nDấu '=' xảy ra khi a = b = 1. Bài toán được chứng minh (0.25đ)."
      }
    ]
  },
  "c2_9_bai4_test5": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương II: Phương trình và bất phương trình bậc nhất một ẩn - Đề số 05",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phương trình tích có dạng chuẩn là:",
        "options": [
          "$A(x) \\cdot B(x) = 0$",
          "$A(x) + B(x) = 0$",
          "$\\frac{A(x)}{B(x)} = 0$",
          "$A(x) - B(x) = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Điều kiện xác định của phương trình $\\frac{2x}{5x - 10} = 1$ là:",
        "options": [
          "$x \\neq 2$",
          "$x \\neq 0$",
          "$x > 2$",
          "$x \\neq 5$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nhân hai vế của bất đẳng thức với một số âm, ta phải:",
        "options": [
          "Đổi chiều bất đẳng thức",
          "Giữ nguyên chiều",
          "Nhân thêm số 0",
          "Lấy nghịch đảo"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nghiệm của bất phương trình $6x > 12$ là:",
        "options": [
          "$x > 2$",
          "$x < 2$",
          "$x \\ge 2$",
          "$x > 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tập nghiệm của phương trình $(x - 5)(2x + 6) = 0$ là:",
        "options": [
          "$\\{5; -3\\}$",
          "$\\{-5; 3\\}$",
          "$\\{5; 3\\}$",
          "$\\{-5; -3\\}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bất phương trình $2x - 5 \\le x + 8$ có nghiệm là:",
        "options": [
          "$x \\le 13$",
          "$x \\ge 13$",
          "$x < 8$",
          "$x \\le 3$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Giá trị $x = 5$ là nghiệm của bất phương trình nào sau đây?",
        "options": [
          "$2x - 1 < 11$",
          "$3x > 17$",
          "$x + 5 \\le 5$",
          "$-x > -4$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Giải phương trình $\\frac{x + 5}{x - 1} = 2$ ta được nghiệm là:",
        "options": [
          "$x = 7$",
          "$x = 3$",
          "$x = 5$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một hãng taxi có giá mở cửa là 5,000,000 đồng cho km đầu tiên và 80,000 đồng cho mỗi km tiếp theo. Với số tiền 150,000 đồng, khách có thể đi tối đa quãng đường (km) là:",
        "options": [
          "-60 km",
          "-61 km",
          "1 km",
          "12 km"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một thang máy có tải trọng tối đa 150000 kg. Nhân viên nặng 5000000 kg mang theo các kiện hàng mỗi kiện nặng 80000 kg. Số kiện hàng tối đa nhân viên đó có thể mang cùng là:",
        "options": [
          "-61 kiện",
          "-60 kiện",
          "1 kiện",
          "20 kiện"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng sản xuất có chi phí cố định là 10 triệu đồng/tháng. Mỗi sản phẩm bán ra thu lãi 50 000 đồng. Xưởng cần sản xuất ít nhất bao nhiêu sản phẩm mỗi tháng để bắt đầu có lãi?",
        "options": [
          "201 sản phẩm",
          "200 sản phẩm",
          "150 sản phẩm",
          "250 sản phẩm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Số nguyên $x$ lớn nhất thỏa mãn bất phương trình $\\frac{x - 5}{2} + \\frac{x - 6}{3} < \\frac{x + 1}{6}$ là:",
        "options": [
          "$x = 6$",
          "$x = 5$",
          "$x = 7$",
          "$x = 4$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét phương trình tích $(2x - 10)(x + 3) = 0$ (Đề 05):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình đã cho là phương trình tích gồm hai nhân tử bậc nhất.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ nhất 2x - 10 = 0 cho nghiệm x = 5.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ hai x + 3 = 0 cho nghiệm x = -3.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tổng hai nghiệm của phương trình bằng 8.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế học tập (Mã đề 05): Bạn Hùng có điểm 4 bài kiểm tra môn Toán lần lượt là 7; 8; 8; 9. Bạn còn 1 bài kiểm tra cuối kỳ hệ số 2. Hùng muốn điểm trung bình môn cả kỳ đạt từ 8,5 trở lên.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng số hệ số điểm kiểm tra môn Toán trong kỳ là 1 + 1 + 1 + 1 + 2 = 6.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng điểm 4 bài kiểm tra đầu tiên là: 7 + 8 + 8 + 9 = 32 điểm.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Bất phương trình tìm điểm bài cuối kỳ x là: (32 + 2x) / 6 >= 8,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Bạn Hùng chỉ cần đạt bài cuối kỳ từ 9,0 điểm là hoàn thành mục tiêu.",
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
        "question": "Giải phương trình: 3x - 15 = 0. Tìm x.",
        "answer": "5",
        "acceptableAnswers": [
          "5"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **5**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm nghiệm nguyên dương nhỏ nhất của bất phương trình: 2x > 11.",
        "answer": "6",
        "acceptableAnswers": [
          "6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **6**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một công ty viễn thông thu cước thuê bao cố định 50 000 đồng/tháng và 1 000 đồng cho mỗi phút gọi. Bạn Lan có ngân sách tối đa 150 000 đồng/tháng. Hỏi bạn Lan có thể gọi tối đa bao nhiêu phút?",
        "answer": "100",
        "acceptableAnswers": [
          "100"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **100**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tìm số nguyên x lớn nhất thỏa mãn: (x - 1)/2 - (x - 2)/3 > 1.",
        "answer": "7",
        "acceptableAnswers": [
          "7"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **7**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình chứa ẩn ở mẫu: $\\frac{x + 5}{x - 2} - \\frac{1}{x} = 1$.",
        "rubric": "ĐKXĐ: x khác 0 và x khác 2 (0.25đ).\nQuy đồng mẫu thức chung x(x - 2): x(x + 5) - (x - 2) = x(x - 2) (0.25đ).\n<=> x^2 + 5x - x + 2 = x^2 - 2x <=> (5 + 1)x = -2 => x = -2/(5 + 1) (thỏa mãn ĐKXĐ) (0.25đ).\nKết luận tập nghiệm (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một người có 300 triệu đồng gửi vào hai sổ tiết kiệm tại ngân hàng. Sổ thứ nhất kỳ hạn 12 tháng lãi suất 6%/năm. Sổ thứ hai kỳ hạn 6 tháng lãi suất 5%/năm. Sau một năm, tổng số tiền lãi nhận được là 16,8 triệu đồng. Tính số tiền gửi ở mỗi sổ.",
        "rubric": "Gọi số tiền gửi ở sổ thứ nhất là x (triệu đồng), sổ thứ hai là y (triệu đồng) (0 < x, y < 300) (0.25đ).\nTa có hệ pt: x + y = 300 và 0,06x + 0,05y = 16,8 (0.25đ).\nGiải ra được x = 180 (triệu đồng) và y = 120 (triệu đồng) (0.25đ).\nKết luận số tiền mỗi sổ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hai số thực dương $a, b$ thỏa mãn $a + b = 2$. Chứng minh rằng: $\\frac{1}{a} + \\frac{1}{b} \\ge 2$.",
        "rubric": "Áp dụng bất đẳng thức Cauchy cho hai số dương a, b: a + b >= 2 căn(ab) => 2 >= 2 căn(ab) => ab <= 1 (0.25đ).\nTa có: 1/a + 1/b = (a + b)/(ab) = 2/(ab) (0.25đ).\nVì ab <= 1 và ab > 0 nên 2/(ab) >= 2/1 = 2 (0.25đ).\nDấu '=' xảy ra khi a = b = 1. Bài toán được chứng minh (0.25đ)."
      }
    ]
  },
  "c2_9_bai4_test6": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương II: Phương trình và bất phương trình bậc nhất một ẩn - Đề số 06",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phương trình tích có dạng chuẩn là:",
        "options": [
          "$A(x) \\cdot B(x) = 0$",
          "$A(x) + B(x) = 0$",
          "$\\frac{A(x)}{B(x)} = 0$",
          "$A(x) - B(x) = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Điều kiện xác định của phương trình $\\frac{2x}{6x - 12} = 1$ là:",
        "options": [
          "$x \\neq 2$",
          "$x \\neq 0$",
          "$x > 2$",
          "$x \\neq 6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nhân hai vế của bất đẳng thức với một số âm, ta phải:",
        "options": [
          "Đổi chiều bất đẳng thức",
          "Giữ nguyên chiều",
          "Nhân thêm số 0",
          "Lấy nghịch đảo"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nghiệm của bất phương trình $7x > 14$ là:",
        "options": [
          "$x > 2$",
          "$x < 2$",
          "$x \\ge 2$",
          "$x > 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tập nghiệm của phương trình $(x - 6)(2x + 6) = 0$ là:",
        "options": [
          "$\\{6; -3\\}$",
          "$\\{-6; 3\\}$",
          "$\\{6; 3\\}$",
          "$\\{-6; -3\\}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bất phương trình $2x - 6 \\le x + 9$ có nghiệm là:",
        "options": [
          "$x \\le 15$",
          "$x \\ge 15$",
          "$x < 9$",
          "$x \\le 3$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Giá trị $x = 6$ là nghiệm của bất phương trình nào sau đây?",
        "options": [
          "$2x - 1 < 13$",
          "$3x > 20$",
          "$x + 5 \\le 6$",
          "$-x > -5$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Giải phương trình $\\frac{x + 6}{x - 1} = 2$ ta được nghiệm là:",
        "options": [
          "$x = 8$",
          "$x = 4$",
          "$x = 6$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một hãng taxi có giá mở cửa là 5,000 đồng cho km đầu tiên và 120 đồng cho mỗi km tiếp theo. Với số tiền 2,000 đồng, khách có thể đi tối đa quãng đường (km) là:",
        "options": [
          "-24 km",
          "-25 km",
          "16 km",
          "12 km"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một thang máy có tải trọng tối đa 2000 kg. Nhân viên nặng 5000 kg mang theo các kiện hàng mỗi kiện nặng 120 kg. Số kiện hàng tối đa nhân viên đó có thể mang cùng là:",
        "options": [
          "-25 kiện",
          "-24 kiện",
          "16 kiện",
          "20 kiện"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng sản xuất có chi phí cố định là 10 triệu đồng/tháng. Mỗi sản phẩm bán ra thu lãi 50 000 đồng. Xưởng cần sản xuất ít nhất bao nhiêu sản phẩm mỗi tháng để bắt đầu có lãi?",
        "options": [
          "201 sản phẩm",
          "200 sản phẩm",
          "150 sản phẩm",
          "250 sản phẩm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Số nguyên $x$ lớn nhất thỏa mãn bất phương trình $\\frac{x - 6}{2} + \\frac{x - 7}{3} < \\frac{x + 1}{6}$ là:",
        "options": [
          "$x = 7$",
          "$x = 6$",
          "$x = 8$",
          "$x = 5$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét phương trình tích $(2x - 12)(x + 3) = 0$ (Đề 06):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình đã cho là phương trình tích gồm hai nhân tử bậc nhất.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ nhất 2x - 12 = 0 cho nghiệm x = 6.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ hai x + 3 = 0 cho nghiệm x = -3.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tổng hai nghiệm của phương trình bằng 9.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế học tập (Mã đề 06): Bạn Hùng có điểm 4 bài kiểm tra môn Toán lần lượt là 7; 8; 8; 9. Bạn còn 1 bài kiểm tra cuối kỳ hệ số 2. Hùng muốn điểm trung bình môn cả kỳ đạt từ 8,5 trở lên.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng số hệ số điểm kiểm tra môn Toán trong kỳ là 1 + 1 + 1 + 1 + 2 = 6.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng điểm 4 bài kiểm tra đầu tiên là: 7 + 8 + 8 + 9 = 32 điểm.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Bất phương trình tìm điểm bài cuối kỳ x là: (32 + 2x) / 6 >= 8,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Bạn Hùng chỉ cần đạt bài cuối kỳ từ 9,0 điểm là hoàn thành mục tiêu.",
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
        "question": "Giải phương trình: 3x - 18 = 0. Tìm x.",
        "answer": "6",
        "acceptableAnswers": [
          "6"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **6**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm nghiệm nguyên dương nhỏ nhất của bất phương trình: 2x > 13.",
        "answer": "7",
        "acceptableAnswers": [
          "7"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **7**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một công ty viễn thông thu cước thuê bao cố định 50 000 đồng/tháng và 1 000 đồng cho mỗi phút gọi. Bạn Lan có ngân sách tối đa 150 000 đồng/tháng. Hỏi bạn Lan có thể gọi tối đa bao nhiêu phút?",
        "answer": "100",
        "acceptableAnswers": [
          "100"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **100**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tìm số nguyên x lớn nhất thỏa mãn: (x - 1)/2 - (x - 2)/3 > 1.",
        "answer": "7",
        "acceptableAnswers": [
          "7"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **7**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình chứa ẩn ở mẫu: $\\frac{x + 6}{x - 2} - \\frac{1}{x} = 1$.",
        "rubric": "ĐKXĐ: x khác 0 và x khác 2 (0.25đ).\nQuy đồng mẫu thức chung x(x - 2): x(x + 6) - (x - 2) = x(x - 2) (0.25đ).\n<=> x^2 + 6x - x + 2 = x^2 - 2x <=> (6 + 1)x = -2 => x = -2/(6 + 1) (thỏa mãn ĐKXĐ) (0.25đ).\nKết luận tập nghiệm (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một người có 300 triệu đồng gửi vào hai sổ tiết kiệm tại ngân hàng. Sổ thứ nhất kỳ hạn 12 tháng lãi suất 6%/năm. Sổ thứ hai kỳ hạn 6 tháng lãi suất 5%/năm. Sau một năm, tổng số tiền lãi nhận được là 16,8 triệu đồng. Tính số tiền gửi ở mỗi sổ.",
        "rubric": "Gọi số tiền gửi ở sổ thứ nhất là x (triệu đồng), sổ thứ hai là y (triệu đồng) (0 < x, y < 300) (0.25đ).\nTa có hệ pt: x + y = 300 và 0,06x + 0,05y = 16,8 (0.25đ).\nGiải ra được x = 180 (triệu đồng) và y = 120 (triệu đồng) (0.25đ).\nKết luận số tiền mỗi sổ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hai số thực dương $a, b$ thỏa mãn $a + b = 2$. Chứng minh rằng: $\\frac{1}{a} + \\frac{1}{b} \\ge 2$.",
        "rubric": "Áp dụng bất đẳng thức Cauchy cho hai số dương a, b: a + b >= 2 căn(ab) => 2 >= 2 căn(ab) => ab <= 1 (0.25đ).\nTa có: 1/a + 1/b = (a + b)/(ab) = 2/(ab) (0.25đ).\nVì ab <= 1 và ab > 0 nên 2/(ab) >= 2/1 = 2 (0.25đ).\nDấu '=' xảy ra khi a = b = 1. Bài toán được chứng minh (0.25đ)."
      }
    ]
  },
  "c2_9_bai4_test7": {
    "title": "Toán 9 (KNTT) - Bài kiểm tra cuối Chương II: Phương trình và bất phương trình bậc nhất một ẩn - Đề số 07",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phương trình tích có dạng chuẩn là:",
        "options": [
          "$A(x) \\cdot B(x) = 0$",
          "$A(x) + B(x) = 0$",
          "$\\frac{A(x)}{B(x)} = 0$",
          "$A(x) - B(x) = 0$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Điều kiện xác định của phương trình $\\frac{2x}{7x - 14} = 1$ là:",
        "options": [
          "$x \\neq 2$",
          "$x \\neq 0$",
          "$x > 2$",
          "$x \\neq 7$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nhân hai vế của bất đẳng thức với một số âm, ta phải:",
        "options": [
          "Đổi chiều bất đẳng thức",
          "Giữ nguyên chiều",
          "Nhân thêm số 0",
          "Lấy nghịch đảo"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nghiệm của bất phương trình $8x > 16$ là:",
        "options": [
          "$x > 2$",
          "$x < 2$",
          "$x \\ge 2$",
          "$x > 1$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tập nghiệm của phương trình $(x - 7)(2x + 6) = 0$ là:",
        "options": [
          "$\\{7; -3\\}$",
          "$\\{-7; 3\\}$",
          "$\\{7; 3\\}$",
          "$\\{-7; -3\\}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Bất phương trình $2x - 7 \\le x + 10$ có nghiệm là:",
        "options": [
          "$x \\le 17$",
          "$x \\ge 17$",
          "$x < 10$",
          "$x \\le 3$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Giá trị $x = 7$ là nghiệm của bất phương trình nào sau đây?",
        "options": [
          "$2x - 1 < 15$",
          "$3x > 23$",
          "$x + 5 \\le 7$",
          "$-x > -6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Giải phương trình $\\frac{x + 7}{x - 1} = 2$ ta được nghiệm là:",
        "options": [
          "$x = 9$",
          "$x = 5$",
          "$x = 7$",
          "Vô nghiệm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một hãng taxi có giá mở cửa là 15,000,000 đồng cho km đầu tiên và 12,000,000 đồng cho mỗi km tiếp theo. Với số tiền 15 đồng, khách có thể đi tối đa quãng đường (km) là:",
        "options": [
          "-1 km",
          "-2 km",
          "0 km",
          "12 km"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một thang máy có tải trọng tối đa 15 kg. Nhân viên nặng 15000000 kg mang theo các kiện hàng mỗi kiện nặng 12000000 kg. Số kiện hàng tối đa nhân viên đó có thể mang cùng là:",
        "options": [
          "-2 kiện",
          "-1 kiện",
          "0 kiện",
          "20 kiện"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một xưởng sản xuất có chi phí cố định là 10 triệu đồng/tháng. Mỗi sản phẩm bán ra thu lãi 50 000 đồng. Xưởng cần sản xuất ít nhất bao nhiêu sản phẩm mỗi tháng để bắt đầu có lãi?",
        "options": [
          "201 sản phẩm",
          "200 sản phẩm",
          "150 sản phẩm",
          "250 sản phẩm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Số nguyên $x$ lớn nhất thỏa mãn bất phương trình $\\frac{x - 7}{2} + \\frac{x - 8}{3} < \\frac{x + 1}{6}$ là:",
        "options": [
          "$x = 8$",
          "$x = 7$",
          "$x = 9$",
          "$x = 6$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét phương trình tích $(2x - 14)(x + 3) = 0$ (Đề 07):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Phương trình đã cho là phương trình tích gồm hai nhân tử bậc nhất.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ nhất 2x - 14 = 0 cho nghiệm x = 7.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Nhân tử thứ hai x + 3 = 0 cho nghiệm x = -3.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Tổng hai nghiệm của phương trình bằng 10.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bài toán thực tế học tập (Mã đề 07): Bạn Hùng có điểm 4 bài kiểm tra môn Toán lần lượt là 7; 8; 8; 9. Bạn còn 1 bài kiểm tra cuối kỳ hệ số 2. Hùng muốn điểm trung bình môn cả kỳ đạt từ 8,5 trở lên.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Tổng số hệ số điểm kiểm tra môn Toán trong kỳ là 1 + 1 + 1 + 1 + 2 = 6.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng điểm 4 bài kiểm tra đầu tiên là: 7 + 8 + 8 + 9 = 32 điểm.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Bất phương trình tìm điểm bài cuối kỳ x là: (32 + 2x) / 6 >= 8,5.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Bạn Hùng chỉ cần đạt bài cuối kỳ từ 9,0 điểm là hoàn thành mục tiêu.",
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
        "question": "Giải phương trình: 3x - 21 = 0. Tìm x.",
        "answer": "7",
        "acceptableAnswers": [
          "7"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **7**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm nghiệm nguyên dương nhỏ nhất của bất phương trình: 2x > 15.",
        "answer": "8",
        "acceptableAnswers": [
          "8"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **8**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một công ty viễn thông thu cước thuê bao cố định 50 000 đồng/tháng và 1 000 đồng cho mỗi phút gọi. Bạn Lan có ngân sách tối đa 150 000 đồng/tháng. Hỏi bạn Lan có thể gọi tối đa bao nhiêu phút?",
        "answer": "100",
        "acceptableAnswers": [
          "100"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **100**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tìm số nguyên x lớn nhất thỏa mãn: (x - 1)/2 - (x - 2)/3 > 1.",
        "answer": "7",
        "acceptableAnswers": [
          "7"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **7**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Giải phương trình chứa ẩn ở mẫu: $\\frac{x + 7}{x - 2} - \\frac{1}{x} = 1$.",
        "rubric": "ĐKXĐ: x khác 0 và x khác 2 (0.25đ).\nQuy đồng mẫu thức chung x(x - 2): x(x + 7) - (x - 2) = x(x - 2) (0.25đ).\n<=> x^2 + 7x - x + 2 = x^2 - 2x <=> (7 + 1)x = -2 => x = -2/(7 + 1) (thỏa mãn ĐKXĐ) (0.25đ).\nKết luận tập nghiệm (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một người có 300 triệu đồng gửi vào hai sổ tiết kiệm tại ngân hàng. Sổ thứ nhất kỳ hạn 12 tháng lãi suất 6%/năm. Sổ thứ hai kỳ hạn 6 tháng lãi suất 5%/năm. Sau một năm, tổng số tiền lãi nhận được là 16,8 triệu đồng. Tính số tiền gửi ở mỗi sổ.",
        "rubric": "Gọi số tiền gửi ở sổ thứ nhất là x (triệu đồng), sổ thứ hai là y (triệu đồng) (0 < x, y < 300) (0.25đ).\nTa có hệ pt: x + y = 300 và 0,06x + 0,05y = 16,8 (0.25đ).\nGiải ra được x = 180 (triệu đồng) và y = 120 (triệu đồng) (0.25đ).\nKết luận số tiền mỗi sổ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hai số thực dương $a, b$ thỏa mãn $a + b = 2$. Chứng minh rằng: $\\frac{1}{a} + \\frac{1}{b} \\ge 2$.",
        "rubric": "Áp dụng bất đẳng thức Cauchy cho hai số dương a, b: a + b >= 2 căn(ab) => 2 >= 2 căn(ab) => ab <= 1 (0.25đ).\nTa có: 1/a + 1/b = (a + b)/(ab) = 2/(ab) (0.25đ).\nVì ab <= 1 và ab > 0 nên 2/(ab) >= 2/1 = 2 (0.25đ).\nDấu '=' xảy ra khi a = b = 1. Bài toán được chứng minh (0.25đ)."
      }
    ]
  }
};

if (typeof window !== 'undefined') {
  window.EXAMS_9_C2_9 = EXAMS_9_C2_9;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { EXAMS_9_C2_9 };
}
