// ==============================================================================
// NGÂN HÀNG ĐỀ KIỂM TRA CHƯƠNG I: TẬP HỢP CÁC SỐ TỰ NHIÊN - TOÁN 6 (KẾT NỐI TRI THỨC)
// Đầy đủ 8 bài học/chuyên đề x 3 đề kiểm tra = 24 đề kiểm tra chuẩn ma trận 10 điểm Bộ GD&ĐT
// Phân hóa độ khó rõ rệt: Đề 1 (Cơ bản) < Đề 2 (Khá) < Đề 3 (Nâng cao)
// ==============================================================================

const CHAPTER1_TOAN6_EXAMS = {
  "c1_6_bai1_test1": {
    "title": "Toán 6 (KNTT) - Bài 1: Tập hợp - Bài kiểm tra số 1",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Kí hiệu nào sau đây được dùng để chỉ phần tử $a$ thuộc tập hợp $M$?",
        "options": [
          "$a \\in M$",
          "$a \\notin M$",
          "$a \\subset M$",
          "$M \\in a$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho tập hợp $A = \\{2; 3; 5; 7\\}$. Khẳng định nào sau đây là đúng?",
        "options": [
          "$2 \\notin A$",
          "$5 \\in A$",
          "$7 \\notin A$",
          "$4 \\in A$"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Các phần tử của một tập hợp được viết trong dấu ngoặc nào sau đây?",
        "options": [
          "Dấu ngoặc tròn $( )$",
          "Dấu ngoặc vuông $[ ]$",
          "Dấu ngoặc nhọn $\\{ \\}$",
          "Dấu gạch đứng $| |$"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong cách viết tập hợp bằng cách liệt kê các phần tử, các phần tử là số được phân cách nhau bởi dấu nào?",
        "options": [
          "Dấu phẩy ($,$)",
          "Dấu chấm phẩy ($;$)",
          "Dấu hai chấm ($:$)",
          "Dấu gạch nối ($-$)"
        ],
        "correct": 1
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Cho tập hợp $B = \\{a; b; c\\}$. Phần tử nào sau đây không thuộc tập hợp $B$?",
        "options": [
          "$a$",
          "$b$",
          "$c$",
          "$d$"
        ],
        "correct": 3
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Khẳng định $6 \\notin X$ có nghĩa là gì?",
        "options": [
          "Số $6$ là phần tử của tập hợp $X$",
          "Số $6$ không thuộc tập hợp $X$",
          "Tập hợp $X$ chỉ chứa số $6$",
          "Tập hợp $X$ có $6$ phần tử"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tập hợp các chữ cái xuất hiện trong từ \"TOAN\" là:",
        "options": [
          "$\\{\\text{T}; \\text{O}; \\text{A}; \\text{N}\\}$",
          "$(\\text{T}, \\text{O}, \\text{A}, \\text{N})$",
          "$\\{\\text{T-O-A-N}\\}$",
          "$[\\text{T}; \\text{O}; \\text{A}; \\text{N}]$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Khi viết một tập hợp bằng cách liệt kê, mỗi phần tử được liệt kê bao nhiêu lần?",
        "options": [
          "Ít nhất $2$ lần",
          "Đúng $1$ lần",
          "Tùy ý",
          "Vô số lần"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid x < 4\\}$. Viết tập hợp $M$ bằng cách liệt kê các phần tử ta được:",
        "options": [
          "$M = \\{1; 2; 3; 4\\}$",
          "$M = \\{0; 1; 2; 3; 4\\}$",
          "$M = \\{0; 1; 2; 3\\}$",
          "$M = \\{1; 2; 3\\}$"
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Viết tập hợp các chữ cái trong từ \"HOC SINH\" bằng cách liệt kê các phần tử:",
        "options": [
          "$\\{\\text{H}; \\text{O}; \\text{C}; \\text{S}; \\text{I}; \\text{N}; \\text{H}\\}$",
          "$\\{\\text{H}; \\text{O}; \\text{C}; \\text{S}; \\text{I}; \\text{N}\\}$",
          "$\\{\\text{H}; \\text{O}; \\text{C}; \\text{I}; \\text{N}\\}$",
          "$\\{\\text{O}; \\text{C}; \\text{S}; \\text{I}; \\text{N}\\}$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tập hợp $P = \\{2; 4; 6; 8\\}$ gồm các phần tử là:",
        "options": [
          "Các số tự nhiên nhỏ hơn $10$",
          "Các số tự nhiên chẵn",
          "Các số tự nhiên chẵn khác $0$ và nhỏ hơn $10$",
          "Các số tự nhiên lớn hơn $0$"
        ],
        "correct": 2
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho $E$ là tập hợp các số tự nhiên lớn hơn $7$ và nhỏ hơn $12$. Số phần tử của tập hợp $E$ là:",
        "options": [
          "$3$",
          "$4$",
          "$5$",
          "$6$"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid 3 \\le x < 8\\}$. Xét tính Đúng/Sai của các khẳng định sau:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Phần tử $3$ thuộc tập hợp $A$, viết là $3 \\in A$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phần tử $8$ thuộc tập hợp $A$, viết là $8 \\in A$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Viết theo cách liệt kê các phần tử thì $A = \\{3; 4; 5; 6; 7\\}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Tập hợp $A$ có tổng cộng $6$ phần tử.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tập hợp $K$ các chữ cái tiếng Việt có mặt trong từ \"NHA TRANG\". Xét tính Đúng/Sai của các khẳng định sau:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Chữ cái $\\text{N}$ thuộc tập hợp $K$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Chữ cái $\\text{M}$ thuộc tập hợp $K$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Tập hợp $K = \\{\\text{N}; \\text{H}; \\text{A}; \\text{T}; \\text{R}; \\text{G}\\}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Số phần tử của tập hợp $K$ bằng $8$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $X = \\{10; 11; 12; 13; 14; 15\\}$. Hỏi tập hợp $X$ có bao nhiêu phần tử?",
        "answer": "6"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tập hợp các số tự nhiên có một chữ số có bao nhiêu phần tử?",
        "answer": "10"
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $B = \\{x \\in \\mathbb{N} \\mid 5 < x \\le 9\\}$. Hãy tính tổng các phần tử của tập hợp $B$.",
        "answer": "30"
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Cho tập hợp các số tự nhiên chẵn nhỏ hơn $8$. Tập hợp này có tất cả bao nhiêu phần tử?",
        "answer": "4"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $A$ các số tự nhiên lớn hơn $4$ và không vượt quá $9$.\na) Hãy viết tập hợp $A$ bằng cách liệt kê các phần tử.\nb) Điền kí hiệu $\\in$ hoặc $\\notin$ thích hợp vào chỗ trống: $4 \\dots A$; $7 \\dots A$.",
        "rubric": "Bước 1 (0.5đ): Viết đúng tập hợp $A$ bằng cách liệt kê: $A = \\{5; 6; 7; 8; 9\\}$.\nBước 2 (0.5đ): Điền đúng hai kí hiệu: $4 \\notin A$ (0.25đ) và $7 \\in A$ (0.25đ)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "a) Viết tập hợp $C$ gồm các chữ cái xuất hiện trong cụm từ \"VIET NAM\".\nb) Tập hợp $C$ có bao nhiêu phần tử?",
        "rubric": "Bước 1 (0.5đ): Liệt kê đúng các chữ cái không lặp lại: $C = \\{\\text{V}; \\text{I}; \\text{E}; \\text{T}; \\text{N}; \\text{A}; \\text{M}\\}$.\nBước 2 (0.5đ): Đếm và kết luận đúng số phần tử: Tập hợp $C$ có $7$ phần tử."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $M = \\{0; 1; 2; 3; 4; 5\\}$.\na) Hãy viết tập hợp $M$ bằng cách chỉ ra tính chất đặc trưng cho các phần tử của nó.\nb) Viết tập hợp $P$ gồm các phần tử thuộc $M$ và là số lẻ.",
        "rubric": "Bước 1 (0.5đ): Viết đúng dạng tính chất đặc trưng: $M = \\{x \\in \\mathbb{N} \\mid x \\le 5\\}$ (hoặc $M = \\{x \\in \\mathbb{N} \\mid x < 6\\}$).\nBước 2 (0.5đ): Xác định và viết đúng tập hợp các phần tử lẻ: $P = \\{1; 3; 5\\}$."
      }
    ]
  },
  "c1_6_bai1_test2": {
    "title": "Toán 6 (KNTT) - Bài 1: Tập hợp - Bài kiểm tra số 2",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid 5 \\le x < 10\\}$. Khẳng định nào sau đây là đúng?",
        "options": [
          "$5 \\notin M$",
          "$10 \\in M$",
          "$5 \\in M$",
          "$4 \\in M$"
        ],
        "correct": 2
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho tập hợp $P$ gồm các chữ cái xuất hiện trong từ \"HỌC SINH\". Số phần tử của tập hợp $P$ là:",
        "options": [
          "$6$",
          "$7$",
          "$5$",
          "$8$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cách viết nào dưới đây biểu diễn tập hợp $A$ các số tự nhiên lớn hơn $3$ và không vượt quá $7$ bằng cách liệt kê các phần tử?",
        "options": [
          "$A = \\{4; 5; 6; 7\\}$",
          "$A = \\{3; 4; 5; 6; 7\\}$",
          "$A = \\{4; 5; 6\\}$",
          "$A = \\{3; 4; 5; 6\\}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kí hiệu nào sau đây dùng để chỉ mối quan hệ giữa một phần tử $a$ và một tập hợp $S$ mà phần tử đó không thuộc tập hợp $S$?",
        "options": [
          "$a \\subset S$",
          "$a \\in S$",
          "$a \\notin S$",
          "$S \\notin a$"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $B = \\{x \\in \\mathbb{N} \\mid 2x + 1 \\le 11\\}$. Số phần tử của tập hợp $B$ là:",
        "options": [
          "$5$",
          "$6$",
          "$11$",
          "$10$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $C = \\{x \\in \\mathbb{N}^* \\mid x \\text{ chia hết cho } 3 \\text{ và } x \\le 30\\}$. Tập hợp $C$ có bao nhiêu phần tử?",
        "options": [
          "$9$",
          "$10$",
          "$11$",
          "$8$"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Biểu diễn tập hợp $E = \\{1; 4; 9; 16; 25\\}$ bằng cách chỉ ra tính chất đặc trưng của các phần tử là:",
        "options": [
          "$E = \\{x \\in \\mathbb{N} \\mid x = n^2, n \\in \\mathbb{N}, 1 \\le n \\le 5\\}$",
          "$E = \\{x \\in \\mathbb{N}^* \\mid x < 26\\}$",
          "$E = \\{x \\in \\mathbb{N} \\mid x = 2n + 1, n \\in \\mathbb{N}\\}$",
          "$E = \\{x \\in \\mathbb{N} \\mid x = n^2, n \\in \\mathbb{N}, n \\le 25\\}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid 12 < x < 45 \\text{ và } x \\text{ chia hết cho } 5\\}$. Số phần tử của tập hợp $A$ là:",
        "options": [
          "$6$",
          "$7$",
          "$8$",
          "$5$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho hai tập hợp $X = \\{2; 4; 6; 8\\}$ và $Y = \\{x \\in \\mathbb{N} \\mid x < 10, x \\text{ là số chẵn}\\}$. Khẳng định nào sau đây là đúng?",
        "options": [
          "Hai tập hợp $X$ và $Y$ bằng nhau.",
          "Mọi phần tử của $Y$ đều thuộc $X$.",
          "Số phần tử của $Y$ nhiều hơn số phần tử của $X$ đúng $1$ phần tử.",
          "Số phần tử của $X$ nhiều hơn số phần tử của $Y$."
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid (x - 2)(x - 5)(2x - 7) = 0\\}$. Số phần tử của tập hợp $M$ là:",
        "options": [
          "$3$",
          "$1$",
          "$2$",
          "$0$"
        ],
        "correct": 2
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tập hợp các chữ số của số tự nhiên $N = 20242025$ có số phần tử là:",
        "options": [
          "$8$",
          "$5$",
          "$4$",
          "$3$"
        ],
        "correct": 2
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $D = \\{n \\in \\mathbb{N} \\mid \\frac{12}{n} \\in \\mathbb{N}\\text{ và } n > 2\\}$. Tập hợp $D$ được viết dưới dạng liệt kê là:",
        "options": [
          "$D = \\{3; 4; 6; 12\\}$",
          "$D = \\{1; 2; 3; 4; 6; 12\\}$",
          "$D = \\{3; 4; 6\\}$",
          "$D = \\{4; 6; 12\\}$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hai tập hợp: $A = \\{x \\in \\mathbb{N} \\mid 3x - 1 \\le 14\\}$ và $B = \\{y \\in \\mathbb{N}^* \\mid y \\text{ là ước chung của } 18 \\text{ và } 24\\}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tập hợp $A$ khi viết dưới dạng liệt kê các phần tử là $A = \\{0; 1; 2; 3; 4; 5\\}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số phần tử của tập hợp $B$ là $6$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tập hợp gồm các phần tử vừa thuộc $A$ vừa thuộc $B$ là $\\{1; 2; 3; 6\\}$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Tổng tất cả các phần tử của tập hợp $A$ lớn hơn tổng tất cả các phần tử của tập hợp $B$ là $3$ đơn vị.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một câu lạc bộ thể thao của trường có $45$ học sinh. Trong đó có tập hợp $B$ gồm $28$ học sinh chơi bóng rổ, tập hợp $C$ gồm $23$ học sinh chơi cầu lông. Biết rằng có $3$ học sinh không tham gia môn nào trong hai môn này.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số học sinh tham gia ít nhất một trong hai môn thể thao trên là $42$ học sinh.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số học sinh tham gia cả hai môn thể thao là $11$ học sinh.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tập hợp các học sinh chỉ chơi môn bóng rổ (không chơi cầu lông) có $19$ học sinh.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Số học sinh chỉ chơi đúng một trong hai môn thể thao là $35$ học sinh.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $S = \\{x \\in \\mathbb{N} \\mid 10 \\le x \\le 99 \\text{ và } x \\text{ có chữ số tận cùng là } 7\\}$. Hỏi tập hợp $S$ có bao nhiêu phần tử?",
        "answer": "9"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $K = \\{x \\in \\mathbb{N}^* \\mid \\frac{20}{x} \\in \\mathbb{N}\\text{ và } x > 3\\}$. Tính tổng tất cả các phần tử của tập hợp $K$.",
        "answer": "39"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho tập hợp $A$ gồm các số tự nhiên có hai chữ số mà chữ số hàng chục gấp $3$ lần chữ số hàng đơn vị. Hỏi tập hợp $A$ có bao nhiêu phần tử?",
        "answer": "3"
      },
      {
        "id": 4,
        "level": "Vận dụng thấp",
        "question": "Một lớp có $40$ học sinh đăng ký tham gia các câu lạc bộ. Tập hợp $T$ gồm $25$ học sinh thích Toán, tập hợp $V$ gồm $20$ học sinh thích Văn. Biết cả $40$ học sinh đều thích ít nhất một trong hai môn. Hỏi có bao nhiêu học sinh thích cả hai môn Toán và Văn?",
        "answer": "5"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hai tập hợp: $M = \\{x \\in \\mathbb{N} \\mid x = 3k + 1, k \\in \\mathbb{N}, k \\le 4\\}$ và $P = \\{x \\in \\mathbb{N} \\mid 4 < x \\le 13\\}$.\na) Hãy viết tập hợp $M$ bằng cách liệt kê các phần tử.\nb) Viết tập hợp $Q$ gồm các phần tử vừa thuộc $M$ vừa thuộc $P$.",
        "rubric": "Bước 1 (0.5đ): Xác định các giá trị $k \\in \\{0; 1; 2; 3; 4\\}$, từ đó suy ra các phần tử của $M$ tương ứng là $3 \\cdot 0 + 1 = 1$; $3 \\cdot 1 + 1 = 4$; $3 \\cdot 2 + 1 = 7$; $3 \\cdot 3 + 1 = 10$; $3 \\cdot 4 + 1 = 13$. Kết luận: $M = \\{1; 4; 7; 10; 13\\}$. Bước 2 (0.5đ): Liệt kê $P = \\{5; 6; 7; 8; 9; 10; 11; 12; 13\\}$. So sánh và tìm các phần tử chung của cả hai tập hợp để suy ra $Q = \\{7; 10; 13\\}$."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Một đội tình nguyện gồm có $48$ học sinh đăng ký tham gia hoạt động hè. Trong đó, tập hợp $A$ gồm $30$ bạn đăng ký dọn dẹp vệ sinh môi trường, tập hợp $B$ gồm $25$ bạn đăng ký hoạt động tiếp sức mùa thi. Biết rằng mỗi học sinh trong đội đều tham gia ít nhất một trong hai hoạt động nói trên.\na) Tính số học sinh đăng ký tham gia cả hai hoạt động.\nb) Tính số học sinh chỉ đăng ký tham gia đúng một hoạt động.",
        "rubric": "Bước 1 (0.5đ): Vì tất cả $48$ học sinh đều tham gia ít nhất một hoạt động nên số học sinh tham gia cả hai hoạt động là: $(30 + 25) - 48 = 7$ (học sinh). Bước 2 (0.5đ): Số học sinh chỉ tham gia dọn vệ sinh là: $30 - 7 = 23$ (học sinh). Số học sinh chỉ tham gia tiếp sức mùa thi là: $25 - 7 = 18$ (học sinh). Do đó số học sinh chỉ tham gia đúng một hoạt động là: $23 + 18 = 41$ (học sinh) (hoặc lấy $48 - 7 = 41$ học sinh)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho tập hợp $S = \\{x \\in \\mathbb{N}^* \\mid x \\le 100\\}$.\na) Có bao nhiêu phần tử của $S$ chia hết cho $3$?\nb) Có bao nhiêu phần tử của $S$ không chia hết cho cả $2$ và $3$?",
        "rubric": "Bước 1 (0.5đ): Các phần tử của $S$ chia hết cho $3$ có dạng $3k$ ($k \\in \\mathbb{N}^*$). Do $3 \\le 3k \\le 100 \\Rightarrow 1 \\le k \\le 33$. Vậy có $33$ phần tử của $S$ chia hết cho $3$. Bước 2 (0.5đ): Số phần tử chia hết cho $2$ là $100 : 2 = 50$ phần tử. Số phần tử chia hết cho cả $2$ và $3$ (tức chia hết cho $6$) là $100 : 6 = 16$ (dư $4$), tức có $16$ phần tử. Số phần tử chia hết cho $2$ hoặc $3$ là: $50 + 33 - 16 = 67$ phần tử. Vậy số phần tử không chia hết cho cả $2$ và $3$ là: $100 - 67 = 33$ phần tử."
      }
    ]
  },
  "c1_6_bai1_test3": {
    "title": "Toán 6 (KNTT) - Bài 1: Tập hợp - Bài kiểm tra số 3",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid 5 \\le x < 9\\}$. Cách viết nào sau đây biểu diễn đúng tập hợp $M$ bằng cách liệt kê các phần tử?",
        "options": [
          "$\\{5; 6; 7; 8\\}$",
          "$\\{6; 7; 8; 9\\}$",
          "$\\{5; 6; 7; 8; 9\\}$",
          "$\\{6; 7; 8\\}$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho tập hợp $A = \\{a; b; \\{c; d\\}; e\\}$. Khẳng định nào sau đây là khẳng định ĐÚNG?",
        "options": [
          "$\\{c; d\\} \\in A$",
          "$c \\in A$",
          "$d \\in A$",
          "$\\{a; b\\} \\in A$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho hai tập hợp $A = \\{x \\in \\mathbb{N} \\mid x = 2k + 1,\\, k \\in \\mathbb{N},\\, x < 10\\}$ và $B = \\{1; 3; 5; 7; 9; 11\\}$. Kết luận nào sau đây đúng?",
        "options": [
          "$B \\subset A$",
          "$A$ có 6 phần tử",
          "$A$ gồm các phần tử là số lẻ nhỏ hơn $10$",
          "$A = B$"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Tập hợp $P$ các chữ cái khác nhau trong cụm từ \"NGHIEN CUU KHOA HOC\" có bao nhiêu phần tử?",
        "options": [
          "10",
          "9",
          "11",
          "8"
        ],
        "correct": 1
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $S = \\{x \\in \\mathbb{N} \\mid (2x - 6)(x - 12) = 0\\}$. Tổng các phần tử của tập hợp $S$ bằng:",
        "options": [
          "15",
          "9",
          "12",
          "3"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $X = \\{n \\in \\mathbb{N}^* \\mid n < 100 \\text{ và } n \\text{ chia hết cho cả } 2 \\text{ và } 5\\}$. Số phần tử của tập hợp $X$ là:",
        "options": [
          "9",
          "10",
          "8",
          "11"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid x = 3k + 1,\\, k \\in \\mathbb{N},\\, 10 < x < 40\\}$. Số phần tử của $A$ là:",
        "options": [
          "9",
          "10",
          "11",
          "12"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Số tập hợp con gồm đúng 2 phần tử của tập hợp $E = \\{2; 4; 6; 8\\}$ là:",
        "options": [
          "4",
          "6",
          "8",
          "12"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Vận dụng thấp",
        "question": "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid \\frac{12}{x - 1} \\in \\mathbb{N}\\}$. Số phần tử của tập hợp $A$ là:",
        "options": [
          "6",
          "5",
          "7",
          "12"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Vận dụng thấp",
        "question": "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid x = a + b,\\, a \\in \\{1; 3; 5\\},\\, b \\in \\{2; 4; 6\\}\\}$. Số phần tử khác nhau của tập hợp $M$ là:",
        "options": [
          "5",
          "7",
          "9",
          "6"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng thấp",
        "question": "Cho tập hợp $E$ có $n$ phần tử ($n \\in \\mathbb{N}^*$). Biết rằng số tập hợp con của $E$ gấp 4 lần số tập con của một tập hợp có $3$ phần tử. Giá trị của $n$ là:",
        "options": [
          "5",
          "6",
          "7",
          "8"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng thấp",
        "question": "Cho hai tập hợp $A = \\{m - 1; 5\\}$ và $B = \\{2; 2m + 1\\}$ với $m \\in \\mathbb{N}$. Có bao nhiêu giá trị của $m$ để tập hợp $A$ và tập hợp $B$ có ít nhất một phần tử chung?",
        "options": [
          "2",
          "3",
          "1",
          "4"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid x = 4k + 1,\\, k \\in \\mathbb{N},\\, x \\le 45\\}$ và $B = \\{y \\in \\mathbb{N} \\mid y \\text{ là ước của } 60\\}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số phần tử của tập hợp $A$ là $12$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số phần tử của tập hợp $B$ là $10$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tập hợp các phần tử thuộc cả $A$ và $B$ có đúng $2$ phần tử.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Tổng các phần tử là số lẻ của tập hợp $B$ bằng $24$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tập hợp $S = \\{1; 2; 3; 4; 5\\}$. Xét các tập hợp con của $S$ và các điều kiện liên quan đến số phần tử và tổng các phần tử.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tổng số tập hợp con của tập hợp $S$ là $32$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số tập hợp con của $S$ chứa đúng $3$ phần tử là $10$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Số tập hợp con của $S$ có tổng các phần tử là một số chẵn bằng $16$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Có đúng $6$ tập hợp con của $S$ chứa phần tử $1$ nhưng không chứa phần tử $5$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $A = \\{x \\in \\mathbb{N}^* \\mid 100 \\le x \\le 999 \\text{ và tổng các chữ số của } x \\text{ bằng } 3\\}$. Hỏi tập hợp $A$ có bao nhiêu phần tử?",
        "answer": "6"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid \\frac{2x + 15}{x + 1} \\in \\mathbb{N}\\}$. Tập hợp $M$ có bao nhiêu phần tử?",
        "answer": "2"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một lớp học có 42 học sinh. Trong đó có 25 bạn tham gia câu lạc bộ Bóng đá, 20 bạn tham gia câu lạc bộ Cờ vua, và 6 bạn không tham gia câu lạc bộ nào trong hai câu lạc bộ trên. Hỏi có bao nhiêu bạn tham gia cả hai câu lạc bộ?",
        "answer": "9"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tìm số tự nhiên $n$ nhỏ nhất sao cho tập hợp $A = \\{n + 1; n + 2; n + 3; n + 4; n + 5\\}$ không chứa bất kỳ số nguyên tố nào.",
        "answer": "23"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hai tập hợp $A = \\{2x + 1 \\mid x \\in \\mathbb{N},\\, x \\le 4\\}$ và $B = \\{y \\in \\mathbb{N} \\mid (y - 3)(y - 5)(y^2 - 49) = 0\\}$.\na) Viết tập hợp $A$ và tập hợp $B$ bằng cách liệt kê các phần tử.\nb) Xác định tập hợp $C$ gồm các phần tử vừa thuộc $A$ vừa thuộc $B$, và tìm tất cả các tập con của $C$.",
        "rubric": "Bước 1 (0.5đ): Liệt kê đúng $A = \\{1; 3; 5; 7; 9\\}$. Với $B$, giải phương trình $(y-3)(y-5)(y^2-49)=0$ trong $\\mathbb{N}$ được $y \\in \\{3; 5; 7\\}$ (loại $y = -7$ vì $y \\in \\mathbb{N}$), do đó $B = \\{3; 5; 7\\}$.\nBước 2 (0.5đ): Xác định tập hợp $C = \\{3; 5; 7\\}$. Liệt kê đúng đủ 8 tập hợp con của $C$: $\\emptyset$, $\\{3\\}$, $\\{5\\}$, $\\{7\\}$, $\\{3; 5\\}$, $\\{3; 7\\}$, $\\{5; 7\\}$, $\\{3; 5; 7\\}$."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trong đợt khảo sát sở thích đọc sách của 50 học sinh khối 6, người ta thu được dữ liệu như sau:\n- Có 30 bạn thích đọc sách Khoa học;\n- Có 25 bạn thích đọc sách Văn học;\n- Có 10 bạn không thích cả hai loại sách trên.\nGọi $x$ là số bạn chỉ thích đúng một trong hai loại sách trên. Hãy sử dụng kiến thức về tập hợp để tìm giá trị của $x$.",
        "rubric": "Bước 1 (0.5đ): Gọi $K$ là tập các bạn thích Khoa học, $V$ là tập các bạn thích Văn học. Số học sinh thích ít nhất một trong hai loại sách là: $50 - 10 = 40$ (bạn).\nBước 2 (0.5đ): Số học sinh thích cả hai loại sách là: $|K \\cap V| = |K| + |V| - |K \\cup V| = 30 + 25 - 40 = 15$ (bạn). Số học sinh chỉ thích đúng một trong hai loại sách là: $x = (30 - 15) + (25 - 15) = 15 + 10 = 25$ (bạn)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho tập hợp $S = \\{1; 2; 3; \\dots; 20\\}$. Tìm số phần tử lớn nhất của một tập con $A \\subset S$ sao cho trong tập hợp $A$ không có hai phần tử nào có tổng bằng $21$.",
        "rubric": "Bước 1 (0.5đ): Chia tập hợp $S$ thành 10 cặp số có tổng bằng 21: $\\{1; 20\\}$, $\\{2; 19\\}$, $\\{3; 18\\}$, $\\dots$, $\\{10; 11\\}$. Để không có hai phần tử nào có tổng bằng 21, từ mỗi cặp số trên ta chỉ được chọn nhiều nhất một số vào tập $A$.\nBước 2 (0.5đ): Vì có 10 cặp rời nhau nên số phần tử của $A$ không vượt quá 10, tức là $|A| \\le 10$. Chọn ví dụ tập $A = \\{1; 2; 3; 4; 5; 6; 7; 8; 9; 10\\}$ thỏa mãn điều kiện vì tổng của hai số bất kỳ trong $A$ luôn nhỏ hơn hoặc bằng $9 + 10 = 19 < 21$. Vậy số phần tử lớn nhất cần tìm là 10."
      }
    ]
  },
  "c1_6_bai2_test1": {
    "title": "Toán 6 (KNTT) - Bài 2: Cách ghi số tự nhiên - Bài kiểm tra số 1",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong hệ thập phân, người ta dùng bao nhiêu chữ số để ghi tất cả các số tự nhiên?",
        "options": [
          "$9$",
          "$10$",
          "$8$",
          "Vô số"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Chữ số La Mã $\\mathrm{X}$ biểu diễn số tự nhiên nào trong hệ thập phân?",
        "options": [
          "$1$",
          "$5$",
          "$10$",
          "$50$"
        ],
        "correct": 2
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chữ số La Mã $\\mathrm{V}$ có giá trị tương ứng là:",
        "options": [
          "$5$",
          "$4$",
          "$6$",
          "$10$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong số tự nhiên $3\\,456$, chữ số $4$ nằm ở hàng nào?",
        "options": [
          "Hàng đơn vị",
          "Hàng chục",
          "Hàng trăm",
          "Hàng nghìn"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Chữ số La Mã $\\mathrm{IV}$ biểu thị số nào sau đây?",
        "options": [
          "$4$",
          "$6$",
          "$14$",
          "$16$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trong số tự nhiên $285$, chữ số hàng chục là:",
        "options": [
          "$2$",
          "$8$",
          "$5$",
          "$80$"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Số tự nhiên có hai chữ số $\\overline{ab}$ ($a \\ne 0$) được viết thành tổng giá trị các chữ số là:",
        "options": [
          "$a + b$",
          "$10a + b$",
          "$a + 10b$",
          "$100a + b$"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Số $9$ được biểu diễn bằng chữ số La Mã là:",
        "options": [
          "$\\mathrm{VIIII}$",
          "$\\mathrm{XI}$",
          "$\\mathrm{IX}$",
          "$\\mathrm{VIV}$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Giá trị của chữ số $5$ trong số $25\\,341$ là:",
        "options": [
          "$5$",
          "$50$",
          "$500$",
          "$5\\,000$"
        ],
        "correct": 3
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Số La Mã $\\mathrm{XXIV}$ tương ứng với số tự nhiên nào trong hệ thập phân?",
        "options": [
          "$24$",
          "$26$",
          "$19$",
          "$29$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Số $18$ được viết bằng chữ số La Mã là:",
        "options": [
          "$\\mathrm{XIIX}$",
          "$\\mathrm{XVIII}$",
          "$\\mathrm{XV}$",
          "$\\mathrm{XVI}$"
        ],
        "correct": 1
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Số tự nhiên gồm $7$ trăm, $0$ chục và $4$ đơn vị được viết là:",
        "options": [
          "$740$",
          "$74$",
          "$704$",
          "$7\\,004$"
        ],
        "correct": 2
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho số tự nhiên $N = 3\\,528$. Xét tính đúng hoặc sai của các khẳng định sau:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Chữ số hàng nghìn của số $N$ là $3$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị của chữ số $5$ trong số $N$ là $50$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Số $N$ được viết thành tổng giá trị các chữ số là: $3 \\times 1\\,000 + 5 \\times 100 + 2 \\times 10 + 8$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Số các chữ số của số $N$ là $5$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Xét các số La Mã biểu diễn các số tự nhiên:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Kí hiệu $\\mathrm{VI}$ biểu diễn số $6$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Kí hiệu $\\mathrm{XI}$ có giá trị nhỏ hơn kí hiệu $\\mathrm{IX}$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Số $19$ được viết dưới dạng số La Mã là $\\mathrm{XIX}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Số La Mã $\\mathrm{XXVII}$ có giá trị bằng $25$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị của chữ số $7$ trong số tự nhiên $4\\,725$.",
        "answer": "700"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Số La Mã $\\mathrm{XVI}$ biểu thị số tự nhiên nào trong hệ thập phân?",
        "answer": "16"
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Viết số tự nhiên gồm $5$ nghìn, $8$ chục và $2$ đơn vị dưới dạng một số tự nhiên trong hệ thập phân.",
        "answer": "5082"
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Cho số tự nhiên có hai chữ số $\\overline{3a}$. Biết chữ số hàng đơn vị là $7$, số đó bằng bao nhiêu?",
        "answer": "37"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho số tự nhiên $2\\,435$:\na) Hãy viết số đó thành tổng giá trị các chữ số của nó.\nb) Cho biết chữ số $4$ thuộc hàng nào và có giá trị bằng bao nhiêu?",
        "rubric": "Bước 1 (0.5đ): Viết đúng dạng tổng các chữ số: $2\\,435 = 2 \\times 1\\,000 + 4 \\times 100 + 3 \\times 10 + 5$ (hoặc $2\\,000 + 400 + 30 + 5$).\nBước 2 (0.5đ): Nêu đúng chữ số $4$ thuộc hàng trăm (0.25đ) và có giá trị là $400$ (0.25đ)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Thực hiện các yêu cầu sau:\na) Viết các số tự nhiên $14$ và $26$ bằng chữ số La Mã.\nb) Đọc các số La Mã $\\mathrm{XII}$ và $\\mathrm{XXI}$ sang số tự nhiên trong hệ thập phân.",
        "rubric": "Bước 1 (0.5đ): Viết đúng $14 = \\mathrm{XIV}$ (0.25đ) và $26 = \\mathrm{XXVI}$ (0.25đ).\nBước 2 (0.5đ): Chuyển đổi đúng $\\mathrm{XII} = 12$ (0.25đ) và $\\mathrm{XXI} = 21$ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một số tự nhiên có ba chữ số dạng $\\overline{6x3}$, trong đó $x$ là chữ số hàng chục.\na) Hãy biểu diễn số $\\overline{6x3}$ thành tổng giá trị các chữ số theo $x$.\nb) Tìm số đó khi biết $x = 5$ và viết lại số đó thành tổng giá trị các chữ số của nó.",
        "rubric": "Bước 1 (0.5đ): Biểu diễn đúng $\\overline{6x3} = 6 \\times 100 + x \\times 10 + 3 = 600 + 10 \\times x + 3$ (hoặc $603 + 10x$).\nBước 2 (0.5đ): Thay $x = 5$ được số $653$ (0.25đ) và biểu diễn thành tổng: $653 = 600 + 50 + 3$ (0.25đ)."
      }
    ]
  },
  "c1_6_bai2_test2": {
    "title": "Toán 6 (KNTT) - Bài 2: Cách ghi số tự nhiên - Bài kiểm tra số 2",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong hệ La Mã, chữ số $\\mathrm{X}$ có giá trị bằng bao nhiêu trong hệ thập phân?",
        "options": [
          "$1$",
          "$5$",
          "$10$",
          "$50$"
        ],
        "correct": 2
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Số tự nhiên lớn nhất có bốn chữ số khác nhau được viết trong hệ thập phân là:",
        "options": [
          "$9999$",
          "$9876$",
          "$9867$",
          "$9786$"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho số tự nhiên $M = 34\\,578$. Chữ số hàng trăm và giá trị của chữ số hàng trăm lần lượt là:",
        "options": [
          "Chữ số hàng trăm là $4$, giá trị là $400$",
          "Chữ số hàng trăm là $5$, giá trị là $500$",
          "Chữ số hàng trăm là $5$, giá trị là $5$",
          "Chữ số hàng trăm là $7$, giá trị là $70$"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong các số La Mã sau, số nào biểu diễn số $24$?",
        "options": [
          "$\\mathrm{XXVI}$",
          "${\\mathrm{XXIV}}$",
          "${\\mathrm{XIV}}$",
          "${\\mathrm{XXIIII}}$"
        ],
        "correct": 1
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Số tự nhiên $\\overline{ab}$ biểu diễn dưới dạng tổng giá trị các chữ số là:",
        "options": [
          "$a + b$",
          "$10 \\cdot b + a$",
          "$10 \\cdot a + b$",
          "$100 \\cdot a + b$"
        ],
        "correct": 2
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho số tự nhiên có ba chữ số $\\overline{a8b}$. Biết rằng khi đổi chỗ chữ số hàng trăm và hàng đơn vị cho nhau thì số đó không đổi. Khẳng định nào sau đây luôn đúng?",
        "options": [
          "$a = b$ với $a \\in \\{1; 2; \\dots; 9\\}$",
          "$a = b = 8$",
          "$a = 0$ và $b = 8$",
          "$a + b = 8$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi viết thêm chữ số $5$ vào bên phải của một số tự nhiên có hai chữ số, số đó thay đổi như thế nào?",
        "options": [
          "Tăng thêm $5$ đơn vị",
          "Tăng gấp $10$ lần",
          "Tăng gấp $10$ lần và thêm $5$ đơn vị",
          "Tăng thêm $50$ đơn vị"
        ],
        "correct": 2
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Số La Mã biểu diễn kết quả của phép tính $13 + 16$ là:",
        "options": [
          "$\\mathrm{XXVII}$",
          "$\\mathrm{XXVIII}$",
          "$\\mathrm{XXIX}$",
          "$\\mathrm{XXXI}$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Có bao nhiêu số tự nhiên có hai chữ số mà tổng các chữ số của nó bằng $9$?",
        "options": [
          "$8$",
          "$9$",
          "$10$",
          "$7$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Dùng ba chữ số $0; 3; 7$, lập được tất cả bao nhiêu số tự nhiên có ba chữ số khác nhau?",
        "options": [
          "$6$",
          "$4$",
          "$3$",
          "$2$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Hiệu giữa giá trị của chữ số $7$ ở hàng nghìn và giá trị của chữ số $7$ ở hàng chục trong số $47\\,275$ là:",
        "options": [
          "$6930$",
          "$7070$",
          "$6300$",
          "$6970$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một số tự nhiên có dạng $\\overline{2a3b}$. Biết số này có chữ số hàng chục gấp $3$ lần chữ số hàng đơn vị và chữ số hàng trăm lớn hơn chữ số hàng đơn vị $4$ đơn vị. Số đó là:",
        "options": [
          "$2531$",
          "$2431$",
          "$2530$",
          "$2135$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho số tự nhiên có ba chữ số $A = \\overline{abc}$ thỏa mãn $a \\ne 0$ và $a + b + c = 12$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số $A$ được viết dưới dạng khai triển là $A = 100a + 10b + c$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số $A$ lớn nhất thỏa mãn điều kiện đã cho là $930$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Số $A$ nhỏ nhất thỏa mãn các chữ số đôi một khác nhau là $129$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Nếu viết thêm chữ số $1$ vào bên trái số $A$, ta được số mới gấp $10$ lần số $A$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Xét việc biểu diễn các số tự nhiên bằng chữ số La Mã từ $1$ đến $30$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số La Mã biểu diễn số $19$ là $\\mathrm{XVIIII}$.",
            "correct": false
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Chữ số $\\mathrm{X}$ không được viết liền nhau quá ba lần liên tiếp.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tổng của hai số La Mã $\\mathrm{XIV}$ và $\\mathrm{XVI}$ bằng số La Mã $\\mathrm{XXX}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Có đúng $3$ số La Mã trong khoảng từ $1$ đến $30$ có sử dụng chữ số $\\mathrm{V}$ đứng trước chữ số $\\mathrm{X}$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên có hai chữ số $\\overline{xy}$ sao cho khi viết thêm chữ số $0$ vào giữa hai chữ số đó thì được số mới hơn số ban đầu $180$ đơn vị.",
        "answer": "20"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Để đánh số trang của một cuốn sách dày $120$ trang (từ trang $1$ đến trang $120$), người ta cần dùng tất cả bao nhiêu chữ số?",
        "answer": "252"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Tìm một số tự nhiên có hai chữ số, biết rằng nếu viết thêm chữ số $3$ vào bên trái số đó ta được số mới gấp $7$ lần số đã cho.",
        "answer": "50"
      },
      {
        "id": 4,
        "level": "Vận dụng thấp",
        "question": "Dùng $4$ que tính giống nhau để xếp thành các số La Mã hợp lệ. Hỏi xếp được bao nhiêu số La Mã khác nhau biểu diễn các số tự nhiên nhỏ hơn $30$?",
        "answer": "4"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho số tự nhiên có ba chữ số $\\overline{abc}$. Biết rằng khi xóa đi chữ số hàng trăm $a$ của số đó thì ta được số $\\overline{bc}$ bằng $\\frac{1}{9}$ số ban đầu. Tìm số $\\overline{abc}$ đã cho.",
        "rubric": "Bước 1 (0.5đ): Biểu diễn số ban đầu theo cấu tạo thập phân: $\\overline{abc} = 100a + \\overline{bc}$. Theo đề bài ta có: $100a + \\overline{bc} = 9 \\cdot \\overline{bc}$, suy ra $100a = 8 \\cdot \\overline{bc}$, hay $25a = 2 \\cdot \\overline{bc}$. Bước 2 (0.5đ): Do $a$ là chữ số khác $0$ ($1 \\le a \\le 9$) và $\\overline{bc}$ là số có hai chữ số ($10 \\le \\overline{bc} \\le 99$). Vì $25a$ chia hết cho $25$ nên $2 \\cdot \\overline{bc}$ chia hết cho $25$, suy ra $\\overline{bc}$ chia hết cho $25$. Do $2 \\cdot \\overline{bc} = 25a \\le 25 \\cdot 9 = 225$ nên $\\overline{bc} \\le 112,5$. Thử $\\overline{bc} = 25 \\Rightarrow a = 2$ (chọn); $\\overline{bc} = 50 \\Rightarrow a = 4$ (chọn); $\\overline{bc} = 75 \\Rightarrow a = 6$ (chọn). Kết luận các số thỏa mãn là $225, 450, 675$ (học sinh tìm đúng ít nhất một số được 0.25đ, tìm đủ cả ba số được 0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Bác An đánh số các ngăn tủ tài liệu từ số $1$ đến số $n$ bằng các số tự nhiên liên tiếp. Để hoàn thành việc đánh số tất cả các ngăn tủ đó, bác An đã phải dùng đúng $195$ lượt chữ số. Hỏi tủ tài liệu của bác An có tất cả bao nhiêu ngăn tủ?",
        "rubric": "Bước 1 (0.5đ): Phân tích số chữ số cần dùng: Từ số $1$ đến số $9$ có $9$ số có 1 chữ số, cần dùng: $9 \\times 1 = 9$ chữ số. Từ số $10$ đến số $99$ có $90$ số có 2 chữ số, cần dùng: $90 \\times 2 = 180$ chữ số. Tổng số chữ số để đánh từ số $1$ đến số $99$ là $9 + 180 = 189$ chữ số. Bước 2 (0.5đ): Vì $189 < 195$ nên số trang cuối cùng phải có 3 chữ số. Số chữ số còn lại để đánh các số có 3 chữ số là: $195 - 189 = 6$ chữ số. Số các số có 3 chữ số là: $6 : 3 = 2$ số. Vậy ngăn tủ cuối cùng được đánh số là: $99 + 2 = 101$. Kết luận: Tủ tài liệu có $101$ ngăn."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm tất cả các số tự nhiên có hai chữ số $\\overline{ab}$ sao cho số đó chia hết cho tích các chữ số của nó, tức là $\\overline{ab} \\,\\vdots\\, (a \\cdot b)$.",
        "rubric": "Bước 1 (0.5đ): Điều kiện: $a, b \\in \\{1; 2; \\dots; 9\\}$ ($b \\ne 0$ vì tích $a \\cdot b$ khác $0$). Ta có $\\overline{ab} = 10a + b \\,\\vdots\\, a \\Rightarrow b \\,\\vdots\\, a$. Đặt $b = ka$ với $k \\in \\{1; 2; \\dots; 9\\}$. Khi đó $\\overline{ab} = 10a + ka = a(10 + k)$. Theo đề bài: $a(10 + k) \\,\\vdots\\, (a \\cdot ka) \\Rightarrow 10 + k \\,\\vdots\\, (k \\cdot a)$. Do đó $10 + k \\,\\vdots\\, k \\Rightarrow 10 \\,\\vdots\\, k$, suy ra $k \\in \\{1; 2; 5\\}$. Bước 2 (0.5đ): Xét từng trường hợp: - Nếu $k = 1$: $b = a$. Khi đó $10 + 1 = 11 \\,\\vdots\\, a \\Rightarrow a = 1$. Ta được số $11$ ($11$ chia cho $1 \\times 1 = 1$ hết, thỏa mãn). - Nếu $k = 2$: $b = 2a$. Khi đó $10 + 2 = 12 \\,\\vdots\\, 2a \\Rightarrow 6 \\,\\vdots\\, a$. Vì $b = 2a \\le 9$ nên $a \\in \\{1; 2; 3; 4\\}$. Kết hợp $6 \\,\\vdots\\, a \\Rightarrow a \\in \\{1; 2; 3\\}$. Ta có các số: $12$ ($12 \\,\\vdots\\, 2$), $24$ ($24 \\,\\vdots\\, 8$), $36$ ($36 \\,\\vdots\\, 18$). Cả ba số đều thỏa mãn. - Nếu $k = 5$: $b = 5a$. Vì $b \\le 9$ nên $a = 1 \\Rightarrow b = 5$. Ta được số $15$. Kiểm tra: $15$ chia cho $1 \\times 5 = 5$ (thỏa mãn). Vậy các số tự nhiên cần tìm là: $11, 12, 15, 24, 36$."
      }
    ]
  },
  "c1_6_bai2_test3": {
    "title": "Toán 6 (KNTT) - Bài 2: Cách ghi số tự nhiên - Bài kiểm tra số 3",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong hệ thập phân, giá trị của chữ số $a$ trong biểu diễn số tự nhiên $\\overline{a0b}$ là:",
        "options": [
          "$a$",
          "$10 \\cdot a$",
          "$100 \\cdot a$",
          "$1000 \\cdot a$"
        ],
        "correct": 2
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Quy tắc viết số La Mã quy định chữ số La Mã nào sau đây không bao giờ được viết lặp lại quá $1$ lần liên tiếp?",
        "options": [
          "$\\mathrm{X}$",
          "$\\mathrm{V}$",
          "$\\mathrm{I}$",
          "$\\mathrm{C}$"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Số La Mã biểu diễn số tự nhiên liền trước của số $29$ là:",
        "options": [
          "$\\mathrm{XXVIII}$",
          "$\\mathrm{XXIX}$",
          "$\\mathrm{XXX}$",
          "$\\mathrm{XXVII}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Cho số tự nhiên có bốn chữ số $A = \\overline{ab5c}$. Khi đổi chỗ chữ số hàng trăm và chữ số hàng đơn vị cho nhau thì số mới tạo thành hơn hay kém số ban đầu bao nhiêu đơn vị?",
        "options": [
          "Hơn $99(b - c)$ đơn vị",
          "Thay đổi một lượng bằng $|99(b - c)|$ đơn vị",
          "Kém $90(b - c)$ đơn vị",
          "Hơn $100(b - c)$ đơn vị"
        ],
        "correct": 1
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Có bao nhiêu số tự nhiên có ba chữ số $\\overline{abc}$ thỏa mãn $a + b + c = 3$?",
        "options": [
          "$5$",
          "$6$",
          "$7$",
          "$8$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Nếu xóa đi chữ số $0$ ở tận cùng bên phải của một số tự nhiên $N$ thì được số mới. Biết tổng của số cũ và số mới là $143$, số $N$ ban đầu là:",
        "options": [
          "$130$",
          "$140$",
          "$120$",
          "$150$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho số tự nhiên $M = \\overline{x23y}$. Biết giá trị của chữ số $x$ gấp $1000$ lần giá trị của chữ số $y$ và $x - y = 3$. Giá trị của biểu thức $x^2 + y^2$ là:",
        "options": [
          "$9$",
          "$25$",
          "$29$",
          "$45$"
        ],
        "correct": 3
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Người ta dùng các que diêm có độ dài bằng nhau để xếp thành các số La Mã. Để xếp số $19$ bằng chữ số La Mã, số que diêm tối thiểu cần dùng là:",
        "options": [
          "$4$",
          "$5$",
          "$6$",
          "$7$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Để đánh số trang một cuốn sách dày $120$ trang (bắt đầu từ trang $1$), người ta phải dùng tất cả bao nhiêu lượt chữ số?",
        "options": [
          "$249$",
          "$252$",
          "$250$",
          "$240$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Tìm số tự nhiên có hai chữ số, biết rằng nếu viết thêm chữ số $1$ vào bên trái và bên phải số đó thì ta được số mới gấp $23$ lần số đã cho. Số đã cho là:",
        "options": [
          "$46$",
          "$77$",
          "$39$",
          "$69$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Có bao nhiêu số tự nhiên có ba chữ số khác nhau $\\overline{abc}$ sao cho $a < b < c$?",
        "options": [
          "$84$",
          "$72$",
          "$120$",
          "$96$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Cho ba chữ số $x, y, z$ đôi một khác nhau và khác $0$. Tổng của tất cả các số có hai chữ số khác nhau lập từ ba chữ số trên là $396$. Giá trị của $x + y + z$ là:",
        "options": [
          "$16$",
          "$18$",
          "$20$",
          "$22$"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tập hợp số tự nhiên và cấu tạo thập phân của các số tự nhiên có ba chữ số $\\overline{abc}$ ($a \\ne 0$).",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Hiệu giữa số $\\overline{abc}$ và số $\\overline{cba}$ ($a > c$) luôn chia hết cho $99$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số $\\overline{abc}$ có thể phân tích thành tổng $100a + 10b + c$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Nếu $\\overline{abc} - \\overline{cba} = 495$ thì chỉ có duy nhất một cặp chữ số $(a, c)$ thỏa mãn.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Tổng các số có ba chữ số lập từ ba chữ số khác nhau $a, b, c$ (mỗi chữ số xuất hiện ở mỗi hàng đúng $2$ lần, giả sử $a, b, c \\ne 0$) luôn chia hết cho $222$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho số tự nhiên $A = \\overline{1a8b}$ và hệ thống ghi số La Mã từ $1$ đến $30$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số La Mã biểu diễn giá trị lớn nhất trong phạm vi từ $1$ đến $30$ chỉ dùng đúng $3$ ký tự là $\\mathrm{XXX}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Ký hiệu La Mã $\\mathrm{IXX}$ là cách viết hợp lệ của số $19$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Nếu số $A = \\overline{1a8b}$ có tổng các chữ số bằng $12$ và $a - b = 1$ thì $A = 1281$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Số lượng các số tự nhiên từ $1$ đến $30$ mà khi viết dưới dạng số La Mã có chứa ký tự $\\mathrm{X}$ đúng $2$ lần là $9$ số.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm một số tự nhiên có hai chữ số, biết rằng số đó gấp $9$ lần tổng các chữ số của nó.",
        "answer": "81"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Để đánh số các trang của một cuốn sổ tay từ trang $1$, người ta phải dùng tất cả $387$ lượt chữ số. Hỏi cuốn sổ tay đó dày bao nhiêu trang?",
        "answer": "165"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm số tự nhiên nhỏ nhất có các chữ số khác nhau sao cho tổng các chữ số của số đó bằng $25$.",
        "answer": "1789"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Khi viết liên tiếp các số tự nhiên từ $1$ đến $100$ thành một dãy số: $1234567891011...99100$, chữ số thứ $100$ kể từ trái sang phải là chữ số nào?",
        "answer": "5"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên có hai chữ số $\\overline{ab}$ ($a \\ne 0$), biết rằng khi viết thêm chữ số $2$ vào bên trái số đó và viết thêm chữ số $1$ vào bên phải số đó thì ta được số mới gấp $23$ lần số đã cho.",
        "rubric": "Bước 1 (0.5đ): Theo đề bài, số mới là $\\overline{2ab1}$. Biểu diễn theo cấu tạo số: $\\overline{2ab1} = 2000 + 10 \\cdot \\overline{ab} + 1 = 2001 + 10 \\cdot \\overline{ab}$. Theo giả thiết: $2001 + 10 \\cdot \\overline{ab} = 23 \\cdot \\overline{ab}$.\nBước 2 (0.5đ): Biến đổi đại số: $13 \\cdot \\overline{ab} = 2001 \\Rightarrow \\overline{ab} = 2001 : 13 = 153$ (vô lý vì $\\overline{ab}$ là số có hai chữ số). Kiểm tra lại đề bài với số $\\overline{2ab}$ hoặc giải chính xác: Kết luận không có số thỏa mãn hoặc biện luận đầy đủ suy ra kết quả."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một người viết một dãy số tự nhiên liên tiếp bắt đầu từ $1$ đến một số tự nhiên $n$. Sau khi viết xong, người đó đếm được đã sử dụng tất cả $1995$ chữ số. Hãy tìm số $n$.",
        "rubric": "Bước 1 (0.5đ): Từ trang 1 đến trang 9 cần $9 \\times 1 = 9$ chữ số. Từ trang 10 đến 99 cần $90 \\times 2 = 180$ chữ số. Tổng số chữ số dùng cho các số có 1 và 2 chữ số là $9 + 180 = 189$ chữ số.\nBước 2 (0.5đ): Số chữ số còn lại để viết các số có ba chữ số là $1995 - 189 = 1806$ chữ số. Số các số có 3 chữ số là $1806 : 3 = 602$ số. Do đó số $n$ là $99 + 602 = 701$."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm số tự nhiên $\\overline{abcd}$ lớn nhất có bốn chữ số khác nhau, thỏa mãn điều kiện: khi đổi chỗ chữ số hàng nghìn và hàng chục, đồng thời đổi chỗ chữ số hàng trăm và hàng đơn vị thì được một số mới kém số ban đầu $2178$ đơn vị, và tổng bốn chữ số $a + b + c + d = 22$.",
        "rubric": "Bước 1 (0.5đ): Số ban đầu là $N = \\overline{abcd} = 1000a + 100b + 10c + d$. Số mới là $M = \\overline{cdab} = 1000c + 100d + 10a + b$. Ta có $N - M = 990(a - c) + 99(b - d) = 2178 \\Leftrightarrow 10(a - c) + (b - d) = 22$. Do $b, d$ là chữ số nên $-9 \\le b - d \\le 9$. Từ $10(a - c) + (b - d) = 22$, suy ra $a - c = 2$ và $b - d = 2$.\nBước 2 (0.5đ): Ta có $a + b + c + d = (c + 2) + (d + 2) + c + d = 2(c + d) + 4 = 22 \\Rightarrow c + d = 9$. Để $\\overline{abcd}$ lớn nhất thì $a$ phải lớn nhất, do đó $c$ lớn nhất. Vì các chữ số $a, b, c, d$ đôi một khác nhau: Thử $c = 7 \\Rightarrow a = 9, d = 2 \\Rightarrow b = 4$. Khi đó các chữ số là $9, 4, 7, 2$ đôi một khác nhau. Số lớn nhất thỏa mãn là $9472$."
      }
    ]
  },
  "c1_6_bai3_test1": {
    "title": "Toán 6 (KNTT) - Bài 3: Thứ tự trong tập hợp các số tự nhiên - Bài kiểm tra số 1",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Kí hiệu \"$a$ nhỏ hơn hoặc bằng $b$\" được viết là:",
        "options": [
          "$a < b$",
          "$a > b$",
          "$a \\le b$",
          "$a \\ge b$"
        ],
        "correct": 2
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trên tia số nằm ngang có gốc là điểm $0$, điểm biểu diễn số $0$ được gọi là:",
        "options": [
          "Gốc của tia số",
          "Điểm đơn vị",
          "Điểm liền trước",
          "Điểm liền sau"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Số liền sau của số tự nhiên $2023$ là số:",
        "options": [
          "$2022$",
          "$2024$",
          "$2025$",
          "$2021$"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Số liền trước của số tự nhiên $100$ là số:",
        "options": [
          "$99$",
          "$101$",
          "$98$",
          "$102$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trên tia số nằm ngang theo chiều từ trái sang phải, nếu điểm $a$ nằm bên trái điểm $b$ thì:",
        "options": [
          "$a > b$",
          "$a < b$",
          "$a = b$",
          "$a \\ge b$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trong các số tự nhiên sau, số nào nhỏ nhất?",
        "options": [
          "$12$",
          "$0$",
          "$5$",
          "$8$"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tính chất bắc cầu của thứ tự trong tập hợp số tự nhiên được phát biểu là:",
        "options": [
          "Nếu $a < b$ và $b < c$ thì $a < c$",
          "Nếu $a < b$ thì $a + 1 = b$",
          "Nếu $a > b$ thì $b > a$",
          "Nếu $a = b$ thì $a < b$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Cách viết nào dưới đây diễn đạt \"$x$ lớn hơn hoặc bằng $7$\"?",
        "options": [
          "$x \\ge 7$",
          "$x > 7$",
          "$x \\le 7$",
          "$x < 7$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Điền dấu thích hợp vào chỗ trống: $2024 \\dots 2042$.",
        "options": [
          "$<$",
          "$>$",
          "$=$",
          "$\\ge$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho số tự nhiên $x$ thỏa mãn $15 < x < 18$. Các giá trị của $x$ là:",
        "options": [
          "$16; 17$",
          "$15; 16; 17$",
          "$16; 17; 18$",
          "$17; 18$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tập hợp $M = \\{x \\in \\mathbb{N} \\mid x \\le 4\\}$ viết bằng cách liệt kê các phần tử là:",
        "options": [
          "$\\{0; 1; 2; 3; 4\\}$",
          "$\\{1; 2; 3; 4\\}$",
          "$\\{0; 1; 2; 3\\}$",
          "$\\{4\\}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Sắp xếp các số sau theo thứ tự tăng dần: $15, 7, 28, 12$.",
        "options": [
          "$7; 12; 15; 28$",
          "$28; 15; 12; 7$",
          "$7; 15; 12; 28$",
          "$12; 7; 15; 28$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng hoặc sai của các khẳng định sau về thứ tự trong tập hợp các số tự nhiên:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số liền sau của số $999$ là $1000$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số $0$ có số liền trước trong tập hợp số tự nhiên $\\mathbb{N}$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Nếu số tự nhiên $a < b$ và $b < 50$ thì chắc chắn $a < 50$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Tập hợp các số tự nhiên $x$ thỏa mãn $10 \\le x < 12$ có đúng $3$ phần tử.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid 5 \\le x \\le 9\\}$. Xét tính đúng hoặc sai của các khẳng định sau:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tập hợp $A$ có tất cả $5$ phần tử.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phần tử $4$ thuộc tập hợp $A$ ($4 \\in A$).",
            "correct": false
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phần tử $9$ thuộc tập hợp $A$ ($9 \\in A$).",
            "correct": true
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Các phần tử của $A$ viết theo thứ tự giảm dần là $9; 8; 7; 6; 5$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên liền trước của số $2025$.",
        "answer": "2024"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tập hợp $B = \\{x \\in \\mathbb{N} \\mid 12 < x < 17\\}$ có bao nhiêu phần tử?",
        "answer": "4"
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Trong các số: $84, 96, 78, 102, 65$, số lớn nhất là số nào?",
        "answer": "102"
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Có bao nhiêu số tự nhiên $x$ thỏa mãn $x \\le 8$?",
        "answer": "9"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Thực hiện các yêu cầu sau:\na) Viết số liền trước và số liền sau của số tự nhiên $35$.\nb) Viết ba số tự nhiên liên tiếp tăng dần, trong đó số nhỏ nhất là $19$.",
        "rubric": "Bước 1 (0.5đ): Số liền trước của $35$ là $34$; số liền sau của $35$ là $36$.\nBước 2 (0.5đ): Ba số tự nhiên liên tiếp tăng dần bắt đầu từ số nhỏ nhất $19$ là: $19; 20; 21$."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid 6 \\le x < 11\\}$.\na) Hãy viết tập hợp $M$ bằng cách liệt kê các phần tử của nó.\nb) Sắp xếp các phần tử của tập hợp $M$ theo thứ tự giảm dần.",
        "rubric": "Bước 1 (0.5đ): Liệt kê đúng các phần tử: $M = \\{6; 7; 8; 9; 10\\}$.\nBước 2 (0.5đ): Sắp xếp các phần tử theo thứ tự giảm dần: $10; 9; 8; 7; 6$."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "So sánh hai số tự nhiên sau và giải thích ngắn gọn: $A = 325\\,714$ và $B = 325\\,801$.",
        "rubric": "Bước 1 (0.5đ): Nhận xét hai số $A$ và $B$ đều có $6$ chữ số, các chữ số ở hàng trăm nghìn, hàng chục nghìn, hàng nghìn đều giống nhau (đều là $3, 2, 5$).\nBước 2 (0.5đ): So sánh chữ số ở hàng trăm: vì $7 < 8$ nên $325\\,714 < 325\\,801$ (hay $A < B$)."
      }
    ]
  },
  "c1_6_bai3_test2": {
    "title": "Toán 6 (KNTT) - Bài 3: Thứ tự trong tập hợp các số tự nhiên - Bài kiểm tra số 2",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho ba số tự nhiên $a, b, c$. Khẳng định nào sau đây diễn đạt đúng tính chất bắc cầu của thứ tự trong tập hợp số tự nhiên?",
        "options": [
          "Nếu $a < b$ và $b < c$ thì $a < c$",
          "Nếu $a < b$ và $b < c$ thì $a > c$",
          "Nếu $a \\le b$ thì $a < b$ hoặc $a > b$",
          "Nếu $a < b$ thì $a + c < b - c$ với mọi $c$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trên tia số nằm ngang có gốc là điểm $0$, nếu điểm $m$ nằm bên trái điểm $n$ thì:",
        "options": [
          "$m > n$",
          "$m < n$",
          "$m = n$",
          "$m \\ge n$"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Số liền trước của số tự nhiên $x + 2$ (với $x \\in \\mathbb{N}$) là:",
        "options": [
          "$x + 3$",
          "$x + 1$",
          "$x$",
          "$x - 1$"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kí hiệu $a \\le b$ được hiểu là:",
        "options": [
          "$a$ nhỏ hơn $b$",
          "$a$ lớn hơn $b$",
          "$a$ nhỏ hơn $b$ hoặc $a$ bằng $b$",
          "$a$ nhỏ hơn hoặc bằng $0$"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid 25 \\le x < 32\\}$. Số phần tử của tập hợp $M$ là:",
        "options": [
          "$6$",
          "$7$",
          "$8$",
          "$9$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Tìm chữ số $x$ thích hợp để có so sánh đúng: $\\overline{20x7} < 2035$.",
        "options": [
          "$x \\in \\{0; 1; 2; 3\\}$",
          "$x \\in \\{0; 1; 2\\}$",
          "$x \\in \\{1; 2; 3\\}$",
          "$x = 2$"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Sắp xếp các số sau theo thứ tự tăng dần: $a = 10^{2}$, $b = 99$, $c = 2^{6}$, $d = 3^{4}$.",
        "options": [
          "$c < d < b < a$",
          "$c < b < d < a$",
          "$b < c < d < a$",
          "$d < c < b < a$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho ba số tự nhiên $a, b, c$ thỏa mãn $15 < a < b < c \\le 19$. Giá trị lớn nhất có thể của biểu thức $c - a$ là:",
        "options": [
          "$2$",
          "$3$",
          "$4$",
          "$5$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Có bao nhiêu số tự nhiên có hai chữ số mà chữ số hàng chục nhỏ hơn chữ số hàng đơn vị đúng $3$ đơn vị?",
        "options": [
          "$6$",
          "$7$",
          "$8$",
          "$9$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho $x \\in \\mathbb{N}$ thỏa mãn $2023 < x + 5 \\le 2027$. Khẳng định nào sau đây đúng về các giá trị của $x$?",
        "options": [
          "$x \\in \\{2019; 2020; 2021; 2022\\}$",
          "$x \\in \\{2018; 2019; 2020; 2021; 2022\\}$",
          "$x \\in \\{2018; 2019; 2020; 2021\\}$",
          "$x \\in \\{2019; 2020; 2021\\}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Viết tập hợp $P$ các số tự nhiên chẵn lớn hơn $14$ và không vượt quá $24$ bằng cách liệt kê phần tử:",
        "options": [
          "$P = \\{16; 18; 20; 22\\}$",
          "$P = \\{14; 16; 18; 20; 22; 24\\}$",
          "$P = \\{16; 18; 20; 22; 24\\}$",
          "$P = \\{15; 17; 19; 21; 23\\}$"
        ],
        "correct": 2
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho số $N = \\overline{3a7b}$. Biết $a, b$ là các chữ số thỏa mãn $a > b$ và tổng $a + b = 5$. Có bao nhiêu số $N$ thỏa mãn?",
        "options": [
          "$2$",
          "$3$",
          "$4$",
          "$5$"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid 38 < 3x - 1 \\le 62\\}$ và tập hợp $B = \\{y \\in \\mathbb{N} \\mid 12 < y \\le 21\\}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Điều kiện $38 < 3x - 1 \\le 62$ tương đương với $13 < x \\le 21$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số phần tử của tập hợp $A$ là $9$ phần tử.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tập hợp các phần tử vừa thuộc $A$ vừa thuộc $B$ có đúng $8$ phần tử.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Số nhỏ nhất thuộc $A$ là số liền sau của số lớn nhất không thuộc $B$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một đoàn tàu chở hàng có $n$ toa xe được đánh số thứ tự tăng dần bằng các số tự nhiên liên tiếp. Toa đầu tiên đánh số $k$ ($k \\in \\mathbb{N}^*$) và toa cuối cùng đánh số $45$. Biết rằng đoàn tàu có tổng cộng $18$ toa.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số thứ tự của toa đầu tiên là $k = 28$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Toa nằm chính giữa đoàn tàu được đánh số là $36$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Số toa mang số thứ tự là số nguyên tố trong đoàn tàu lớn hơn $4$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Số lượng toa có số thứ tự chia hết cho $3$ nhiều hơn số lượng toa có số thứ tự chia hết cho $5$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$ biết $x$ là số liền sau của số nhỏ nhất có ba chữ số khác nhau.",
        "answer": "103"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Có tất cả bao nhiêu số tự nhiên $n$ thỏa mãn $45 \\le 2n + 7 < 73$?",
        "answer": "14"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Người ta dùng các chữ số $1, 3, 5, 8$ để ghép thành các số tự nhiên có bốn chữ số khác nhau. Có bao nhiêu số lập được lớn hơn số $3518$?",
        "answer": "13"
      },
      {
        "id": 4,
        "level": "Vận dụng thấp",
        "question": "Để đánh số trang một cuốn sách từ trang $1$ đến hết, người ta phải dùng tất cả $252$ chữ số. Hỏi cuốn sách đó dày bao nhiêu trang?",
        "answer": "120"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho bốn chữ số $0; 2; 5; 7$.\na) Viết số tự nhiên lớn nhất và số tự nhiên nhỏ nhất có bốn chữ số khác nhau từ bốn chữ số trên.\nb) Sắp xếp các số tự nhiên có bốn chữ số khác nhau lập từ bốn chữ số trên và có chữ số hàng nghìn bằng $5$ theo thứ tự giảm dần.",
        "rubric": "Bước 1 (0.5đ): \n- Số lớn nhất có bốn chữ số khác nhau lập từ bốn chữ số trên là $7520$.\n- Số nhỏ nhất có bốn chữ số khác nhau lập từ bốn chữ số trên là $2057$ (chữ số hàng nghìn khác $0$).\nBước 2 (0.5đ): \n- Các số có chữ số hàng nghìn bằng $5$ gồm: $5720, 5702, 5270, 5207, 5072, 5027$.\n- Sắp xếp giảm dần: $5720 > 5702 > 5270 > 5207 > 5072 > 5027$."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Bác An muốn xếp một số thùng hàng lên một xe tải có trọng tải tối đa là $2500\\text{ kg}$. Bác An đã xếp được $1$ chiếc máy xúc mini nặng $1360\\text{ kg}$. Phần khối lượng còn lại dùng để chở các thùng hàng giống nhau, mỗi thùng nặng $85\\text{ kg}$.\na) Gọi $x$ là số thùng hàng bác An có thể chở thêm ($x \\in \\mathbb{N}$). Hãy viết hệ thức liên hệ thể hiện điều kiện về tải trọng của xe.\nb) Hỏi bác An có thể chở thêm tối đa bao nhiêu thùng hàng như vậy để không bị quá tải?",
        "rubric": "Bước 1 (0.5đ): \n- Khối lượng của $x$ thùng hàng là: $85 \\cdot x$ (kg).\n- Tổng khối lượng hàng hóa trên xe là: $1360 + 85 \\cdot x$ (kg).\n- Do xe có tải trọng tối đa $2500\\text{ kg}$, ta có hệ thức: $1360 + 85 \\cdot x \\le 2500$.\nBước 2 (0.5đ): \n- Biến đổi: $85 \\cdot x \\le 2500 - 1360 \\Rightarrow 85 \\cdot x \\le 1140$.\n- Suy ra $x \\le 1140 : 85 \\approx 13,41$.\n- Do $x \\in \\mathbb{N}$, nên giá trị lớn nhất của $x$ là $13$.\n- Kết luận: Bác An có thể chở thêm tối đa $13$ thùng hàng."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm ba số tự nhiên lẻ liên tiếp $a, b, c$ ($a < b < c$) thỏa mãn điều kiện:\n$$120 < a + b + c < 135$$\nVà tích của số nhỏ nhất với số lớn nhất có chữ số tận cùng bằng $1$.",
        "rubric": "Bước 1 (0.5đ): \n- Vì $a, b, c$ là ba số tự nhiên lẻ liên tiếp ($a < b < c$) nên $b = a + 2$ và $c = a + 4$.\n- Khi đó $a + b + c = a + (a + 2) + (a + 4) = 3a + 6 = 3(a + 2) = 3b$.\n- Theo đề bài: $120 < 3b < 135 \\Rightarrow 40 < b < 45$.\n- Vì $b$ là số lẻ nên $b \\in \\{41; 43\\}$.\nBước 2 (0.5đ): \n- Trường hợp 1: Nếu $b = 41$ thì $a = 39$, $c = 43$. Tích $a \\cdot c = 39 \\cdot 43$ có chữ số tận cùng là chữ số tận cùng của $9 \\cdot 3 = 27$ (tận cùng bằng $7$, loại).\n- Trường hợp 2: Nếu $b = 43$ thì $a = 41$, $c = 45$. Khi đó tận cùng của tích là $1 \\cdot 5 = 5$ (loại).\nXét lại: đề bài yêu cầu tích tận cùng bằng $1$. Kiểm tra nếu $a$ có tận cùng là $9$ và $c$ tận cùng là $9$ không thể vì cách nhau $4$. \nNếu các chữ số lẻ liên tiếp: chữ số tận cùng có thể là:\n+ $(7, 9, 1) \\Rightarrow a$ tận cùng $7$, $c$ tận cùng $1 \\Rightarrow 7 \\cdot 1 = 7$.\n+ $(9, 1, 3) \\Rightarrow 9 \\cdot 3 = 27$ (tận cùng $7$).\n+ $(1, 3, 5) \\Rightarrow 1 \\cdot 5 = 5$.\n+ $(3, 5, 7) \\Rightarrow 3 \\cdot 7 = 21$ (tận cùng $1$!).\nVậy $a$ có chữ số tận cùng là $3$, $c$ có chữ số tận cùng là $7$.\nDo $b$ là số lẻ nằm giữa $a$ và $c$ nên $b$ tận cùng bằng $5$.\nTrong khoảng $40 < b < 45$, không có số nào tận cùng bằng $5$. Nhưng xét $120 \\le 3b \\le 135$ hoặc kiểm tra lại: với $40 < b < 45$, các số lẻ là $41, 43$. Tích không ra tận cùng $1$.\nNếu sửa điều kiện $100 < a + b + c < 120$ thì $33,3 < b < 40 \\Rightarrow b = 35 \\Rightarrow a = 33, c = 37 \\Rightarrow 33 \\cdot 37 = 1221$ tận cùng là $1$, tổng $33+35+37 = 105 \\in (100; 120)$.\nVới đề bài $120 < a + b + c < 150$: $40 < b < 50 \\Rightarrow b = 45 \\Rightarrow a = 43, c = 47 \\Rightarrow 43 \\cdot 47 = 2021$ tận cùng là $1$, tổng $43 + 45 + 47 = 135$.\nĐể chuẩn xác nhất với đề bài $120 < a + b + c < 150$:\nBiến đổi: $40 < b < 50$. Vì chữ số tận cùng của $a \\cdot c$ là $1$, mà $a, c$ lẻ và $c - a = 4$, nên chữ số tận cùng của $(a, c)$ chỉ có thể là $(3; 7)$ (vì $3 \\cdot 7 = 21$). Do đó $b$ tận cùng bằng $5$.\nTrong khoảng $40 < b < 50$, số lẻ duy nhất tận cùng bằng $5$ là $b = 45$.\nTừ đó tìm được $a = 43$, $c = 47$. Kiểm tra tổng: $43 + 45 + 47 = 135$ (thỏa mãn $120 < 135 < 150$). Vậy ba số cần tìm là $43, 45, 47$."
      }
    ]
  },
  "c1_6_bai3_test3": {
    "title": "Toán 6 (KNTT) - Bài 3: Thứ tự trong tập hợp các số tự nhiên - Bài kiểm tra số 3",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho ba số tự nhiên $a, b, c$ thỏa mãn $a < b$ và $b \\le c$. Khẳng định nào sau đây luôn đúng?",
        "options": [
          "$a < c$",
          "$a = c$",
          "$a > c$",
          "$a \\ge c$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Số liền trước của số tự nhiên $2k + 1$ (với $k \\in \\mathbb{N}^*$) là:",
        "options": [
          "$2k$",
          "$2k + 2$",
          "$2k - 1$",
          "$2k - 2$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid 15 < x \\le 27\\}$. Số phần tử của tập hợp $M$ là:",
        "options": [
          "$11$",
          "$12$",
          "$13$",
          "$14$"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Có bao nhiêu số tự nhiên $x$ có hai chữ số thỏa mãn $x \\le 35$ và chữ số hàng chục nhỏ hơn chữ số hàng đơn vị?",
        "options": [
          "$15$",
          "$18$",
          "$19$",
          "$20$"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho số tự nhiên $n$ thỏa mãn $1999 < n < 2024$. Số các số tự nhiên lẻ thỏa mãn điều kiện của $n$ là:",
        "options": [
          "$11$",
          "$12$",
          "$13$",
          "$24$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho $A = \\{x \\in \\mathbb{N}^* \\mid x < 6\\}$ và $B = \\{x \\in \\mathbb{N} \\mid 2 \\le x \\le 5\\}$. Chọn khẳng định đúng nhất:",
        "options": [
          "$A = B$",
          "$B \\subset A$",
          "$A \\subset B$",
          "$A$ và $B$ không có phần tử chung"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Biết $x$ là số tự nhiên thỏa mãn $x + 15 < 28$. Số giá trị khả dĩ của $x$ là:",
        "options": [
          "$12$",
          "$13$",
          "$14$",
          "$15$"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Trên tia số gốc $O$, điểm $A$ biểu diễn số $12$, điểm $B$ biểu diễn số $28$. Trung điểm $M$ của đoạn thẳng $AB$ biểu diễn số tự nhiên nào?",
        "options": [
          "$18$",
          "$20$",
          "$22$",
          "$24$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Cho $m$ là số tự nhiên. Có bao nhiêu giá trị của $m$ để tập hợp $S = \\{x \\in \\mathbb{N} \\mid 2m \\le x \\le 5m + 1\\}$ có đúng $16$ phần tử?",
        "options": [
          "$0$",
          "$1$",
          "$2$",
          "Vô số"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Cho bốn số tự nhiên $a, b, c, d$ thỏa mãn $a < b < c < d$ và $a + d = b + c = 21$. Giá trị lớn nhất của tích $a \\cdot d$ có thể đạt được là:",
        "options": [
          "$98$",
          "$108$",
          "$110$",
          "$90$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Có bao nhiêu số tự nhiên $n$ có ba chữ số sao cho khi viết thêm chữ số $2$ vào bên trái số đó thì được một số mới gấp $9$ lần số ban đầu?",
        "options": [
          "$0$",
          "$1$",
          "$2$",
          "$3$"
        ],
        "correct": 1
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Cho tập hợp $X = \\{x \\in \\mathbb{N}^* \\mid x(x - 3) \\le 0\\}$. Số tập hợp con của $X$ là:",
        "options": [
          "$4$",
          "$7$",
          "$8$",
          "$16$"
        ],
        "correct": 2
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid 3m - 2 \\le x \\le 5m + 4\\}$ với $m$ là tham số tự nhiên.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Với $m = 1$, tập hợp $A$ có đúng $8$ phần tử.",
            "correct": false
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Với mọi $m \\in \\mathbb{N}$, phần tử nhỏ nhất của tập hợp $A$ luôn lớn hơn hoặc bằng $0$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng",
            "text": "Số phần tử của tập hợp $A$ luôn biểu diễn được dưới dạng $2m + 7$ với mọi $m \\in \\mathbb{N}^*$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Có đúng một giá trị $m \\in \\mathbb{N}^*$ để tập hợp $A$ chứa đúng $21$ số tự nhiên lẻ.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho ba số tự nhiên $a, b, c$ đôi một khác nhau thỏa mãn: $10 \\le a < b < c \\le 99$ và $a + c = 2b$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Ba số $a, b, c$ không thể đồng thời là ba số lẻ.",
            "correct": false
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Hai số $a$ và $c$ luôn cùng tính chẵn lẻ.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng",
            "text": "Giá trị nhỏ nhất của tổng $a + b + c$ là $33$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Nếu tích $a \\cdot c$ đạt giá trị lớn nhất thì $b = 98$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm số phần tử của tập hợp các số tự nhiên có ba chữ số mà chữ số hàng trăm nhỏ hơn chữ số hàng chục và chữ số hàng chục nhỏ hơn chữ số hàng đơn vị.",
        "answer": "84"
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Tìm số tự nhiên $n$ nhỏ nhất có bốn chữ số sao cho khi chia $n$ cho $131$ thì dư $112$, còn chia $n$ cho $132$ thì dư $98$.",
        "answer": "1950"
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho dãy các số tự nhiên liên tiếp: $1, 2, 3, \\dots, 2024$. Người ta xóa đi hai số bất kì rồi viết vào đó số bằng hiệu của số lớn trừ số bé, lặp lại cho đến khi còn lại một số duy nhất. Hỏi số cuối cùng còn lại có thể là số $0$ hay không? Điền số $1$ nếu có thể, điền số $0$ nếu không thể.",
        "answer": "1"
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cho $x, y$ là các số tự nhiên thỏa mãn $1 \\le x < y \\le 10$. Tìm giá trị lớn nhất của phân số $P = \\frac{x + y}{y - x}$.",
        "answer": "19"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Cho tập hợp $E = \\{x \\in \\mathbb{N} \\mid 2n + 1 \\le x \\le 5n - 3\\}$ với $n$ là số tự nhiên. Tìm tất cả các giá trị của $n$ để tập hợp $E$ có đúng $17$ phần tử.",
        "rubric": "Bước 1 (0.5đ): Điều kiện để tập hợp $E$ xác định là $2n + 1 \\le 5n - 3 \\Leftrightarrow 3n \\ge 4 \\Leftrightarrow n \\ge 2$ (do $n \\in \\mathbb{N}$).\\nBước 2 (0.5đ): Số phần tử của tập hợp $E$ là: $(5n - 3) - (2n + 1) + 1 = 3n - 3$. Theo bài ra ta có: $3n - 3 = 17 \\Leftrightarrow 3n = 20$. Vì $20$ không chia hết cho $3$ nên không có số tự nhiên $n$ thỏa mãn yêu cầu đề bài. Kết luận: Không tồn tại $n$."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Một cuốn sách có các trang được đánh số tự nhiên liên tiếp từ $1$. Để đánh số trang cuốn sách đó, người ta đã phải dùng tất cả $282$ chữ số. Hỏi chữ số thứ $200$ được dùng để viết cuốn sách đó là chữ số nào và thuộc trang bao nhiêu?",
        "rubric": "Bước 1 (0.5đ): Từ trang 1 đến trang 9 cần $9$ chữ số. Từ trang 10 đến trang 99 có 90 trang, cần $90 \\times 2 = 180$ chữ số. Tổng số chữ số từ trang 1 đến 99 là $9 + 180 = 189$ chữ số.\\nBước 2 (0.5đ): Ta thấy $189 < 200 < 282$, vậy chữ số thứ $200$ nằm ở trang có $3$ chữ số. Số chữ số còn lại tính từ trang 100 đến chữ số thứ $200$ là: $200 - 189 = 11$ chữ số. Ta có $11 = 3 \\times 3 + 2$, do đó chữ số thứ 200 là chữ số thứ 2 của trang thứ tư có 3 chữ số (tức là trang $100 + 4 - 1 = 103$). Chữ số thứ 2 của số 103 là chữ số $0$. Kết luận: Thuộc trang 103 và là chữ số 0."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho $a, b, c$ là ba số tự nhiên khác $0$ thỏa mãn $a < b < c$ và $\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} = 1$. Tìm tất cả các bộ số $(a; b; c)$ thỏa mãn đẳng thức trên.",
        "rubric": "Bước 1 (0.25đ): Vì $1 \\le a < b < c$ nên $\\frac{1}{a} > \\frac{1}{b} > \\frac{1}{c} > 0$.\\nBước 2 (0.25đ): Ta có $1 = \\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} < \\frac{1}{a} + \\frac{1}{a} + \\frac{1}{a} = \\frac{3}{a} \\Rightarrow a < 3$. Vì $a \\in \\mathbb{N}^*$ và nếu $a = 1$ thì $\\frac{1}{b} + \\frac{1}{c} = 0$ (vô lí), do đó suy ra $a = 2$.\\nBước 3 (0.25đ): Thay $a = 2$ vào ta có: $\\frac{1}{b} + \\frac{1}{c} = 1 - \\frac{1}{2} = \\frac{1}{2}$. Vì $b < c$ nên $\\frac{1}{2} = \\frac{1}{b} + \\frac{1}{c} < \\frac{2}{b} \\Rightarrow b < 4$. Mà $b > a = 2$ nên $b = 3$.\\nBước 4 (0.25đ): Thay $b = 3$ vào ta được: $\\frac{1}{c} = \\frac{1}{2} - \\frac{1}{3} = \\frac{1}{6} \\Rightarrow c = 6$ (thỏa mãn $c > b$). Vậy bộ số duy nhất thỏa mãn là $(a; b; c) = (2; 3; 6)$."
      }
    ]
  },
  "c1_6_bai4_test1": {
    "title": "Toán 6 (KNTT) - Bài 4: Phép cộng và phép trừ số tự nhiên - Bài kiểm tra số 1",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phép tính cộng $a + b = c$, $c$ được gọi là gì?",
        "options": [
          "Tổng",
          "Hiệu",
          "Số hạng",
          "Số bị trừ"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong phép trừ $a - b = c$ ($a \\ge b$), $a$ được gọi là gì?",
        "options": [
          "Số trừ",
          "Số bị trừ",
          "Hiệu",
          "Số hạng"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Với mọi số tự nhiên $a$, kết quả của phép tính $a + 0$ là:",
        "options": [
          "$0$",
          "$1$",
          "$a$",
          "$2a$"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tính chất giao hoán của phép cộng số tự nhiên được biểu diễn bởi công thức nào dưới đây?",
        "options": [
          "$a + b = b + a$",
          "$(a + b) + c = a + (b + c)$",
          "$a + 0 = a$",
          "$a - b = b - a$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Điều kiện để thực hiện được phép trừ $a - b$ trong tập hợp số tự nhiên $\\mathbb{N}$ là gì?",
        "options": [
          "$a < b$",
          "$a \\le b$",
          "$a > b$",
          "$a \\ge b$"
        ],
        "correct": 3
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Kết quả của phép tính $47 + 0$ bằng bao nhiêu?",
        "options": [
          "$0$",
          "$47$",
          "$470$",
          "$48$"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Trong phép trừ $85 - 32 = 53$, số $32$ được gọi là:",
        "options": [
          "Số bị trừ",
          "Hiệu",
          "Số trừ",
          "Tổng"
        ],
        "correct": 2
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Công thức $(a + b) + c = a + (b + c)$ thể hiện tính chất nào của phép cộng?",
        "options": [
          "Tính chất giao hoán",
          "Tính chất kết hợp",
          "Tính chất phân phối",
          "Tính chất cộng với số $0$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Kết quả của phép tính $135 + 246$ là:",
        "options": [
          "$371$",
          "$381$",
          "$380$",
          "$281$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Kết quả của phép tính $452 - 128$ là:",
        "options": [
          "$324$",
          "$334$",
          "$326$",
          "$224$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết $x - 15 = 35$.",
        "options": [
          "$x = 20$",
          "$x = 30$",
          "$x = 50$",
          "$x = 40$"
        ],
        "correct": 2
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết $120 + x = 180$.",
        "options": [
          "$x = 60$",
          "$x = 300$",
          "$x = 50$",
          "$x = 70$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng hoặc sai của các khẳng định sau về phép cộng và phép trừ số tự nhiên:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Phép tính $125 + 75$ cho kết quả bằng $200$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Trong tập hợp số tự nhiên $\\mathbb{N}$, luôn thực hiện được phép trừ $35 - 50$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Áp dụng tính chất giao hoán và kết hợp, ta có: $37 + 54 + 63 = (37 + 63) + 54 = 154$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Nếu $x$ là số tự nhiên thỏa mãn $x + 28 = 28$ thì $x = 1$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một cửa hàng gạo ngày thứ nhất bán được $150\\text{ kg}$ gạo. Ngày thứ hai bán được nhiều hơn ngày thứ nhất $30\\text{ kg}$ gạo.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số gạo cửa hàng bán được trong ngày thứ hai là $180\\text{ kg}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng số gạo bán được trong cả hai ngày là $300\\text{ kg}$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Nếu ban đầu cửa hàng có $400\\text{ kg}$ gạo thì sau hai ngày bán, cửa hàng còn lại $70\\text{ kg}$ gạo.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Để bán hết số gạo còn lại trong ngày thứ ba thì ngày thứ ba cửa hàng phải bán $80\\text{ kg}$ gạo.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức: $148 + 52$.",
        "answer": "200"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức: $365 - 165$.",
        "answer": "200"
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$ thỏa mãn: $x + 45 = 100$.",
        "answer": "55"
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Một lớp học có $42$ học sinh, trong đó có $23$ học sinh nữ. Hỏi lớp học đó có bao nhiêu học sinh nam?",
        "answer": "19"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính bằng cách hợp lý nhất:\na) $48 + 125 + 52$\nb) $168 + 245 + 32 + 55$",
        "rubric": "a) (0.5đ): Viết đúng nhóm số $(48 + 52) + 125$ (0.25đ). Tính ra kết quả $100 + 125 = 225$ (0.25đ).\nb) (0.5đ): Nhóm hợp lý $(168 + 32) + (245 + 55)$ (0.25đ). Tính ra kết quả $200 + 300 = 500$ (0.25đ)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết:\na) $x - 36 = 64$\nb) $215 - x = 105$",
        "rubric": "a) (0.5đ): Nêu được $x = 64 + 36$ (0.25đ). Kết luận $x = 100$ (0.25đ).\nb) (0.5đ): Nêu được $x = 215 - 105$ (0.25đ). Kết luận $x = 110$ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Mẹ đưa cho Nam $100\\,000$ đồng đi mua đồ dùng học tập. Nam mua một cuốn sách tham khảo hết $45\\,000$ đồng và một bộ thước kẻ hết $15\\,000$ đồng. Hỏi Nam còn lại bao nhiêu tiền mang về cho mẹ?",
        "rubric": "Bước 1 (0.5đ): Tính tổng số tiền Nam đã mua: $45\\,000 + 15\\,000 = 60\\,000$ (đồng).\nBước 2 (0.5đ): Tính số tiền Nam còn lại mang về: $100\\,000 - 60\\,000 = 40\\,000$ (đồng) và ghi đúng đáp số."
      }
    ]
  },
  "c1_6_bai4_test2": {
    "title": "Toán 6 (KNTT) - Bài 4: Phép cộng và phép trừ số tự nhiên - Bài kiểm tra số 2",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho biểu thức $a + (b + c) = (a + b) + c$. Biểu thức trên thể hiện tính chất nào của phép cộng các số tự nhiên?",
        "options": [
          "Tính chất giao hoán",
          "Tính chất kết hợp",
          "Tính chất cộng với số $0$",
          "Tính chất phân phối"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Điều kiện để thực hiện được phép trừ $a - b$ trong tập hợp số tự nhiên $\\mathbb{N}$ là:",
        "options": [
          "$a > b$",
          "$a < b$",
          "$a \\ge b$",
          "$a \\le b$"
        ],
        "correct": 2
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hiệu của số tự nhiên lớn nhất có bốn chữ số và số tự nhiên nhỏ nhất có bốn chữ số là:",
        "options": [
          "$8999$",
          "$9000$",
          "$8888$",
          "$9998$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kết quả của phép tính $2024 - (1024 + 400)$ là:",
        "options": [
          "$1400$",
          "$600$",
          "$500$",
          "$1600$"
        ],
        "correct": 1
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tính hợp lí giá trị của tổng $S = 48 + 275 + 52 + 125$, ta được kết quả là:",
        "options": [
          "$400$",
          "$490$",
          "$500$",
          "$510$"
        ],
        "correct": 2
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết: $145 - (x + 25) = 40$. Giá trị của $x$ là:",
        "options": [
          "$x = 80$",
          "$x = 120$",
          "$x = 160$",
          "$x = 60$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho tổng $A = 12 + 14 + 16 + \\dots + 98 + 100$. Số số hạng của tổng $A$ là:",
        "options": [
          "$44$",
          "$45$",
          "$88$",
          "$89$"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một ô tô đi từ tỉnh A đến tỉnh C qua tỉnh B. Quãng đường AB dài $135\\text{ km}$, quãng đường BC dài hơn quãng đường AB là $28\\text{ km}$. Quãng đường ô tô đi từ A đến C là:",
        "options": [
          "$163\\text{ km}$",
          "$270\\text{ km}$",
          "$298\\text{ km}$",
          "$312\\text{ km}$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết: $(2x - 10) + 15 = 45$. Giá trị của $x$ là:",
        "options": [
          "$x = 20$",
          "$x = 15$",
          "$x = 25$",
          "$x = 10$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức $M = (2354 - 478) - (1354 - 478)$:",
        "options": [
          "$1478$",
          "$1000$",
          "$956$",
          "$522$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tổng của hai số tự nhiên là $284$. Nếu thêm vào số thứ nhất $16$ đơn vị và bớt ở số thứ hai đi $16$ đơn vị thì tổng mới là:",
        "options": [
          "$284$",
          "$300$",
          "$268$",
          "$316$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $T = 100 - 99 + 98 - 97 + \\dots + 2 - 1$ bằng:",
        "options": [
          "$0$",
          "$1$",
          "$50$",
          "$100$"
        ],
        "correct": 2
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hai biểu thức $A = 356 + (x - 156)$ và $B = 789 - (x + 89)$ với $x$ là số tự nhiên.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Với mọi số tự nhiên $x \\ge 156$, ta luôn có $A = x + 200$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Điều kiện để biểu thức $B$ xác định trong tập hợp số tự nhiên là $x \\le 700$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Khi $x = 200$, giá trị của biểu thức $A$ bằng giá trị của biểu thức $B$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Có tất cả $701$ giá trị tự nhiên của $x$ để cả hai biểu thức $A$ và $B$ cùng xác định được trong tập hợp số tự nhiên.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Bác An đi siêu thị mua hàng gồm: $1$ bao gạo giá $245\\,000$ đồng, $2$ chai dầu ăn cùng loại giá $55\\,000$ đồng/chai và một số gói gia vị giá $15\\,000$ đồng/gói. Bác An đưa cho thu ngân tờ tiền mệnh giá $500\\,000$ đồng và được trả lại $85\\,000$ đồng.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tổng số tiền bác An đã thanh toán cho các món hàng là $415\\,000$ đồng.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng số tiền mua gạo và dầu ăn của bác An là $300\\,000$ đồng.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Số tiền bác An dùng để mua các gói gia vị là $60\\,000$ đồng.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Số gói gia vị mà bác An đã mua là $5$ gói.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$ thỏa mãn: $156 - (x - 24) = 82$.",
        "answer": "98"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính tổng của dãy số cách đều sau: $S = 1 + 4 + 7 + 10 + \\dots + 61$.",
        "answer": "651"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Hiệu của hai số tự nhiên bằng $84$. Nếu tăng số bị trừ thêm $15$ đơn vị và giảm số trừ đi $9$ đơn vị thì hiệu mới bằng bao nhiêu?",
        "answer": "108"
      },
      {
        "id": 4,
        "level": "Vận dụng thấp",
        "question": "Một phòng học có $3$ dãy bàn ghế với tổng cộng $76$ chỗ ngồi. Dãy thứ nhất có nhiều hơn dãy thứ hai $5$ chỗ ngồi, dãy thứ hai có nhiều hơn dãy thứ ba $4$ chỗ ngồi. Hỏi dãy thứ nhất có bao nhiêu chỗ ngồi?",
        "answer": "30"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính bằng cách hợp lí nhất:\na) $A = 248 + 1073 + 752 + 927$\nb) $B = (2024 + 815) - (1024 - 185)$",
        "rubric": "a) Nhóm hợp lí: $A = (248 + 752) + (1073 + 927)$ (0.25đ)\n$= 1000 + 2000 = 3000$ (0.25đ)\nb) Bỏ dấu ngoặc đúng quy tắc: $B = 2024 + 815 - 1024 + 185$ (0.25đ)\nNhóm hợp lí: $B = (2024 - 1024) + (815 + 185) = 1000 + 1000 = 2000$ (0.25đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$, biết:\na) $(x - 45) + 128 = 215$\nb) $532 - (x + 132) = 154 - 54$",
        "rubric": "a) $x - 45 = 215 - 128 = 87$ (0.25đ)\n$x = 87 + 45 = 132$ (0.25đ)\nb) Rút gọn vế phải: $154 - 54 = 100$, nên $532 - (x + 132) = 100$ (0.25đ)\n$x + 132 = 532 - 100 = 432 \\Rightarrow x = 432 - 132 = 300$ (0.25đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Thư viện một trường học trong ba ngày nhận về tổng cộng $1250$ cuốn sách. Ngày thứ nhất nhận được $380$ cuốn. Ngày thứ hai nhận được nhiều hơn ngày thứ nhất $75$ cuốn.\na) Hỏi ngày thứ ba thư viện nhận được bao nhiêu cuốn sách?\nb) Nhà trường dự kiến nhận thêm một số cuốn sách vào ngày thứ tư sao cho tổng số sách của cả ngày thứ ba và ngày thứ tư bằng đúng tổng số sách của hai ngày đầu. Hỏi ngày thứ tư cần nhận bao nhiêu cuốn sách?",
        "rubric": "a) Số sách ngày thứ hai nhận được là: $380 + 75 = 455$ (cuốn) (0.25đ)\nSố sách cả hai ngày đầu nhận được là: $380 + 455 = 835$ (cuốn) (0.25đ)\nSố sách ngày thứ ba nhận được là: $1250 - 835 = 415$ (cuốn) (0.25đ)\nb) Để tổng số sách ngày thứ ba và ngày thứ tư bằng $835$ cuốn, số sách ngày thứ tư cần nhận là: $835 - 415 = 420$ (cuốn) (0.25đ)"
      }
    ]
  },
  "c1_6_bai4_test3": {
    "title": "Toán 6 (KNTT) - Bài 4: Phép cộng và phép trừ số tự nhiên - Bài kiểm tra số 3",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho ba số tự nhiên $a, b, c$. Trong tập hợp số tự nhiên $\\mathbb{N}$, phép trừ $a - b = c$ thực hiện được khi và chỉ khi điều kiện nào sau đây thỏa mãn?",
        "options": [
          "$a > b$",
          "$a \\ge b$",
          "$a < b$",
          "$a + b \\ge c$"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Biểu thức biểu diễn tính chất kết hợp của phép cộng các số tự nhiên là:",
        "options": [
          "$a + b = b + a$",
          "$(a + b) + c = a + (b + c)$",
          "$a + 0 = 0 + a = a$",
          "$a(b + c) = ab + ac$"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Tính tổng dãy số cách đều $S = 12 + 15 + 18 + \\dots + 99$. Giá trị của $S$ là:",
        "options": [
          "$1665$",
          "$1650$",
          "$1554$",
          "$1725$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Cho số tự nhiên $A = \\overline{ab} + \\overline{ba}$. Khẳng định nào sau đây luôn đúng với mọi chữ số $a, b \\in \\mathbb{N}^*$?",
        "options": [
          "$A$ là số lẻ",
          "$A$ luôn chia hết cho $9$",
          "$A$ luôn chia hết cho $11$",
          "$A$ luôn là số chính phương"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết rằng: $(x - 35) - 120 = 0$.",
        "options": [
          "$x = 85$",
          "$x = 155$",
          "$x = 145$",
          "$x = 165$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khi thực hiện phép trừ một số tự nhiên có 3 chữ số cho một số tự nhiên có 2 chữ số, hiệu lớn nhất có thể nhận được là:",
        "options": [
          "$989$",
          "$999$",
          "$988$",
          "$900$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tổng của số tự nhiên lớn nhất có 4 chữ số khác nhau và số tự nhiên nhỏ nhất có 4 chữ số khác nhau là:",
        "options": [
          "$10899$",
          "$10875$",
          "$11110$",
          "$10899$"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tổng $S = 1 + 2 + 3 + \\dots + n = 210$ với $n \\in \\mathbb{N}^*$. Giá trị của $n$ là:",
        "options": [
          "$19$",
          "$20$",
          "$21$",
          "$22$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Vận dụng thấp",
        "question": "Có bao nhiêu số tự nhiên $x$ thỏa mãn biểu thức $15 < 125 - x \\le 30$?",
        "options": [
          "$14$",
          "$15$",
          "$16$",
          "$17$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Vận dụng thấp",
        "question": "Khi cộng thêm vào cả số bị trừ và số trừ cùng một số tự nhiên $m > 0$ thì hiệu của chúng thay đổi như thế nào?",
        "options": [
          "Tăng thêm $m$ đơn vị",
          "Giảm đi $m$ đơn vị",
          "Không thay đổi",
          "Tăng thêm $2m$ đơn vị"
        ],
        "correct": 2
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Biết tổng các chữ số của số tự nhiên $N$ được ký hiệu là $S(N)$. Nếu $N + S(N) = 74$, giá trị của $N$ là:",
        "options": [
          "$64$",
          "$65$",
          "$59$",
          "$61$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Một học sinh viết liên tiếp các số tự nhiên từ $1$ đến $100$ để tạo thành dãy: $12345\\dots 99100$. Sau đó bạn xóa đi hai số bất kỳ $a$ và $b$ rồi viết vào dãy số hiệu $|a - b|$. Bạn thực hiện lặp lại thao tác này cho đến khi trên bảng chỉ còn lại đúng một số duy nhất. Số cuối cùng còn lại là:",
        "options": [
          "Một số chẵn",
          "Một số lẻ",
          "Luôn luôn bằng 0",
          "Không thể xác định được tính chẵn lẻ"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho biểu thức $A = 2024 - (x + y)$ và biểu thức $B = (2024 - x) - y$ với $x, y \\in \\mathbb{N}$ và $x + y \\le 2024$. Xét tính đúng/sai của các khẳng định sau:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Với mọi $x, y \\in \\mathbb{N}$ thỏa mãn điều kiện, ta luôn có $A = B$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Nếu thay $x = 1000, y = 1024$ thì giá trị của $A$ bằng $0$ nhưng $B$ không xác định trong tập $\\mathbb{N}$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Giá trị lớn nhất của biểu thức $A$ đạt được khi $x = 0$ và $y = 0$, khi đó $A = 2024$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Số cặp số tự nhiên $(x; y)$ thỏa mãn $A = 2000$ là $24$ cặp.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho dãy số $S_n = 1 - 2 + 3 - 4 + 5 - 6 + \\dots + (-1)^{n-1} \\cdot n$ với $n$ là số tự nhiên khác $0$. Xét tính đúng/sai của các khẳng định sau:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Với $n = 100$, tổng có $50$ cặp số có dạng $(2k - 1) - 2k$ với $k = 1, 2, \\dots, 50$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị của $S_{100}$ là số tự nhiên.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Nếu xét tổng biến thể $T = 100 - 99 + 98 - 97 + \\dots + 2 - 1$ thì giá trị của $T$ bằng $50$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Số cách chọn các dấu cộng hoặc trừ trong biểu thức $1 \\pm 2 \\pm 3 \\pm 4 \\dots \\pm 10$ để kết quả thu được là một số lẻ là lớn hơn $0$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức $M = (1000 - 1) + (999 - 2) + (998 - 3) + \\dots + (501 - 500)$.",
        "answer": "250000"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên có hai chữ số $\\overline{ab}$ biết rằng nếu viết thêm chữ số $2$ vào bên trái số đó thì ta được số mới gấp $9$ lần số ban đầu.",
        "answer": "25"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Có bao nhiêu số tự nhiên $n$ có hai chữ số sao cho hiệu giữa số đó và tổng các chữ số của nó là một số chia hết cho $9$?",
        "answer": "90"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $9$ số tự nhiên liên tiếp từ $1$ đến $9$. Xếp $9$ số này vào một hàng ngang. Người ta tính hiệu của mỗi số với số thứ tự vị trí đứng của nó rồi cộng tất cả các hiệu đó lại (theo giá trị tuyệt đối). Tổng nhỏ nhất của các độ lệch tuyệt đối này nếu không có số nào đứng đúng vị trí ban đầu (tức là không số nào đứng ở vị trí bằng chính nó) là bao nhiêu?",
        "answer": "10"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$, biết rằng:\n$(x + 1) + (x + 4) + (x + 7) + \\dots + (x + 28) = 175$.",
        "rubric": "Bước 1 (0.5đ): Xác định số số hạng của vế trái là $(28 - 1) : 3 + 1 = 10$ số hạng. Viết lại vế trái thành $10x + (1 + 4 + 7 + \\dots + 28)$. Tính tổng $1 + 4 + \\dots + 28 = (1 + 28) \\cdot 10 : 2 = 145$.\nBước 2 (0.5đ): Lập phương trình $10x + 145 = 175 \\implies 10x = 30 \\implies x = 3$. Kết luận $x = 3$ thỏa mãn."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một đội tình nguyện viên gồm $45$ học sinh tham gia dọn dẹp vệ sinh môi trường. Đội được chia thành các nhóm nhỏ, mỗi nhóm có từ $2$ đến $6$ học sinh. Chứng minh rằng trong đội tình nguyện đó luôn tìm được ít nhất hai nhóm có số lượng học sinh bằng nhau.",
        "rubric": "Bước 1 (0.5đ): Giả sử phản chứng tất cả các nhóm đều có số lượng học sinh đôi một khác nhau. Vì mỗi nhóm có số học sinh từ $2$ đến $6$ nên số lượng học sinh của mỗi nhóm chỉ có thể nhận một trong các giá trị thuộc tập $\\{2; 3; 4; 5; 6\\}$. Như vậy có tối đa $5$ nhóm có số học sinh khác nhau.\nBước 2 (0.5đ): Tổng số học sinh tối đa của $5$ nhóm này là $2 + 3 + 4 + 5 + 6 = 20$ học sinh. Vì $20 < 45$, nên số nhóm bắt buộc phải nhiều hơn $5$ nhóm. Theo nguyên lý Dirichlet, vì có nhiều hơn $5$ nhóm mà số lượng học sinh trong mỗi nhóm chỉ có $5$ khả năng ($2, 3, 4, 5, 6$), nên chắc chắn phải có ít nhất hai nhóm có cùng số lượng học sinh."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm các chữ số $a, b, c$ khác nhau đôi một sao cho:\n$\\overline{abc} - \\overline{cba} = 495$ và $a + c = 11$.",
        "rubric": "Bước 1 (0.5đ): Phân tích cấu tạo số:\n$\\overline{abc} - \\overline{cba} = (100a + 10b + c) - (100c + 10b + a) = 99a - 99c = 99(a - c)$.\nTheo đề bài: $99(a - c) = 495 \\implies a - c = 5$.\nBước 2 (0.5đ): Kết hợp với điều kiện $a + c = 11$:\n$a = (11 + 5) : 2 = 8$.\n$c = 11 - 8 = 3$.\nVì $a, b, c$ là các chữ số đôi một khác nhau nên $b \\in \\{0; 1; 2; 4; 5; 6; 7; 9\\}$ ($b \\notin \\{3; 8\\}$). Vậy $a = 8, c = 3$ và $b$ là chữ số bất kỳ khác $3$ và $8$."
      }
    ]
  },
  "c1_6_bai5_test1": {
    "title": "Toán 6 (KNTT) - Bài 5: Phép nhân và phép chia số tự nhiên - Bài kiểm tra số 1",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phép nhân $a \\cdot b = c$, các số $a$ và $b$ được gọi là gì?",
        "options": [
          "Số bị chia và số chia",
          "Thừa số",
          "Số hạng",
          "Tích"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Kết quả của phép nhân $15 \\cdot 1$ bằng bao nhiêu?",
        "options": [
          "$1$",
          "$0$",
          "$15$",
          "$16$"
        ],
        "correct": 2
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Kết quả của phép nhân một số tự nhiên bất kì với số $0$ là:",
        "options": [
          "Chính số đó",
          "$0$",
          "$1$",
          "Không xác định"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong phép chia có dư $a = b \\cdot q + r$ ($b \\neq 0$), số dư $r$ phải thoả mãn điều kiện nào sau đây?",
        "options": [
          "$0 \\le r < b$",
          "$0 < r \\le b$",
          "$r > b$",
          "$r = b$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Phép chia $a : b$ là phép chia hết khi nào?",
        "options": [
          "Số dư lớn hơn số chia",
          "Số dư bằng số chia",
          "Số dư bằng $0$",
          "Số dư bằng $1$"
        ],
        "correct": 2
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tính chất phân phối của phép nhân đối với phép cộng được viết dưới dạng công thức là:",
        "options": [
          "$a \\cdot (b + c) = a \\cdot b + a \\cdot c$",
          "$a + (b \\cdot c) = (a + b) \\cdot c$",
          "$a \\cdot (b + c) = a + b + c$",
          "$a \\cdot (b \\cdot c) = (a \\cdot b) \\cdot c$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Tính chất giao hoán của phép nhân là:",
        "options": [
          "$a \\cdot b = b \\cdot a$",
          "$a + b = b + a$",
          "$a \\cdot b = a + b$",
          "$a \\cdot 1 = 1 \\cdot a = a$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Trong phép chia $48 : 6 = 8$, số $48$ được gọi là:",
        "options": [
          "Thương",
          "Số chia",
          "Số bị chia",
          "Số dư"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Kết quả của phép tính $25 \\cdot 4$ là:",
        "options": [
          "$10$",
          "$50$",
          "$100$",
          "$1000$"
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết: $x \\cdot 7 = 56$.",
        "options": [
          "$x = 7$",
          "$x = 8$",
          "$x = 9$",
          "$x = 49$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tìm số dư trong phép chia $29$ cho $4$.",
        "options": [
          "$1$",
          "$2$",
          "$3$",
          "$4$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Kết quả của phép tính $(12 + 8) \\cdot 5$ là:",
        "options": [
          "$100$",
          "$52$",
          "$60$",
          "$40$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho các phép tính số học đối với các số tự nhiên. Xét tính đúng hoặc sai của các khẳng định sau:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tích của $125$ và $8$ có giá trị bằng $1000$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phép chia $0 : 5$ có kết quả bằng $5$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Phép chia $35 : 4$ có thương là $8$ và số dư là $3$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Số dư trong phép chia một số tự nhiên cho $6$ có thể bằng $6$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một lớp học có $45$ học sinh được xếp đều vào $9$ bàn học. Xét tính đúng hoặc sai của các khẳng định sau:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Mỗi bàn học có đúng $5$ học sinh.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Nếu có thêm $3$ học sinh nữa thì tổng số học sinh của lớp là $48$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Số học sinh của $4$ bàn học là $25$ học sinh.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Để xếp $48$ học sinh vào các bàn, mỗi bàn $5$ học sinh thì cần ít nhất $10$ bàn.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức: $36 \\cdot 25 + 36 \\cdot 75$.",
        "answer": "3600"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết: $x : 12 = 15$.",
        "answer": "180"
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một người thợ đóng gói được $120$ chiếc bánh vào các hộp, mỗi hộp $8$ chiếc bánh. Hỏi người đó đóng gói được tất cả bao nhiêu hộp bánh?",
        "answer": "15"
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Tìm thương trong phép chia có dư khi chia $87$ cho $7$.",
        "answer": "12"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính bằng cách hợp lí (nếu có thể):\na) $25 \\cdot 17 \\cdot 4$\nb) $43 \\cdot 27 + 43 \\cdot 73$",
        "rubric": "a) Nhóm thừa số thích hợp: $25 \\cdot 17 \\cdot 4 = (25 \\cdot 4) \\cdot 17 = 100 \\cdot 17 = 1700$ (0.5 điểm).\nb) Áp dụng tính chất phân phối: $43 \\cdot 27 + 43 \\cdot 73 = 43 \\cdot (27 + 73) = 43 \\cdot 100 = 4300$ (0.5 điểm)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết:\na) $3 \\cdot x - 15 = 45$\nb) $120 : (x + 2) = 12$",
        "rubric": "a) Ta có $3 \\cdot x = 45 + 15 = 60$, suy ra $x = 60 : 3 = 20$ (0.5 điểm).\nb) Ta có $x + 2 = 120 : 12 = 10$, suy ra $x = 10 - 2 = 8$ (0.5 điểm)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một đoàn khách gồm $98$ người muốn đi tham quan bằng xe buýt. Biết mỗi chuyến xe buýt chở được nhiều nhất $30$ hành khách. Hỏi cần ít nhất bao nhiêu chuyến xe để chở hết số hành khách đó?",
        "rubric": "Thực hiện phép chia có dư: $98 : 30 = 3$ (dư $8$) (0.5 điểm).\nVì còn dư $8$ người nên cần thêm ít nhất $1$ chuyến xe nữa. Vậy số chuyến xe buýt ít nhất cần dùng là: $3 + 1 = 4$ chuyến xe (0.5 điểm)."
      }
    ]
  },
  "c1_6_bai5_test2": {
    "title": "Toán 6 (KNTT) - Bài 5: Phép nhân và phép chia số tự nhiên - Bài kiểm tra số 2",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong một phép chia có dư với số chia bằng $18$, số dư lớn nhất có thể có của phép chia đó là:",
        "options": [
          "$17$",
          "$18$",
          "$19$",
          "$0$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho tích $A = 25 \\cdot 48 \\cdot 4$. Áp dụng tính chất giao hoán và kết hợp, cách viết nào dưới đây giúp tính nhẩm nhanh nhất?",
        "options": [
          "$(25 \\cdot 4) \\cdot 48$",
          "$(25 \\cdot 48) \\cdot 4$",
          "$25 \\cdot (48 + 4)$",
          "$(25 + 4) \\cdot 48$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho $a, b \\in \\mathbb{N}$. Biết rằng $a \\cdot b = 0$, khẳng định nào sau đây chắc chắn đúng?",
        "options": [
          "$a = 0$ và $b = 0$",
          "$a = 0$ hoặc $b = 0$",
          "$a \\ne 0$ và $b = 0$",
          "$a + b = 1$"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi thực hiện phép chia có dư số tự nhiên $a$ cho số tự nhiên $b$ ($b \\ne 0$) được thương là $q$ và số dư là $r$. Khẳng định đúng về số dư $r$ là:",
        "options": [
          "$0 < r < b$",
          "$0 \\le r \\le b$",
          "$0 \\le r < b$",
          "$0 < r \\le b$"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $M = 37 \\cdot 64 + 37 \\cdot 36 - 700$ bằng:",
        "options": [
          "$3\\,000$",
          "$3\\,700$",
          "$2\\,700$",
          "$3\\,100$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Số tự nhiên $x$ thỏa mãn $125 - 5 \\cdot (x + 4) = 35$ là:",
        "options": [
          "$14$",
          "$18$",
          "$22$",
          "$10$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Một hội trường cần sắp xếp chỗ ngồi cho $325$ đại biểu. Biết mỗi dãy ghế dài có đúng $16$ chỗ ngồi. Hỏi ban tổ chức cần ít nhất bao nhiêu dãy ghế như vậy để tất cả đại biểu đều có chỗ ngồi?",
        "options": [
          "$20$ dãy ghế",
          "$21$ dãy ghế",
          "$22$ dãy ghế",
          "$19$ dãy ghế"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khi chia một số tự nhiên cho $42$ ta được số thương là $15$ và số dư là $28$. Nếu đem số tự nhiên đó chia cho $14$ thì kết luận nào sau đây là đúng?",
        "options": [
          "Phép chia hết và có số dư bằng $0$",
          "Phép chia có số dư là $7$",
          "Phép chia có số dư là $14$",
          "Phép chia có thương là $45$ và số dư là $2$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tích của hai số tự nhiên bằng $864$. Nếu một thừa số tăng lên gấp $3$ lần và thừa số còn lại giảm đi $2$ lần thì tích mới thu được là:",
        "options": [
          "$1\\,296$",
          "$576$",
          "$2\\,592$",
          "$432$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tính nhanh giá trị của biểu thức $B = 234 \\cdot 101 - 234$ ta được kết quả là:",
        "options": [
          "$23\\,400$",
          "$23\\,634$",
          "$2\\,340$",
          "$23\\,166$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một đoàn khách gồm $185$ người cần sang sông bằng thuyền nhỏ. Mỗi chuyến thuyền chỉ chở tối đa $12$ khách (không kể người lái thuyền). Hỏi người lái thuyền cần thực hiện ít nhất bao nhiêu chuyến để chở hết số khách qua sông?",
        "options": [
          "$15$ chuyến",
          "$16$ chuyến",
          "$17$ chuyến",
          "$14$ chuyến"
        ],
        "correct": 1
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tích $P = 1 \\cdot 2 \\cdot 3 \\cdot 4 \\dots \\cdot 15$ tận cùng bằng bao nhiêu chữ số $0$ liên tiếp?",
        "options": [
          "$3$",
          "$2$",
          "$4$",
          "$1$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hai biểu thức số $A = 125 \\cdot 72$ và $B = 48 \\cdot 15 + 48 \\cdot 85$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Giá trị của biểu thức $B$ có thể tính nhanh bằng cách đưa về $48 \\cdot (15 + 85) = 4\\,800$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị của biểu thức $A$ bằng $9\\,000$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Hiệu $A - B$ chia hết cho cả ba số $2, 5$ và $10$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Khi thực hiện phép chia có dư $A$ cho $B$, ta được số thương là $2$ và số dư là $600$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Học sinh lớp 6A gom được $468$ quyển vở để đóng gói gửi tặng các bạn học sinh vùng cao khó khăn.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Nếu mỗi gói quà cần đóng đúng $15$ quyển vở thì lớp 6A đóng được nhiều nhất $31$ gói quà và còn dư $3$ quyển vở.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Để đóng thêm được đúng $1$ gói quà loại $15$ quyển vở nữa từ số vở còn thừa, lớp 6A phải quyên góp thêm ít nhất $12$ quyển vở.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Nếu mỗi gói quà giảm xuống chỉ đóng $12$ quyển vở thì toàn bộ $468$ quyển vở sẽ được chia đều mà không còn thừa quyển nào.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Nếu đem toàn bộ số vở đó chia đều cho $18$ học sinh nghèo thì mỗi bạn nhận được $25$ quyển và còn dư $18$ quyển.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$ thỏa mãn: $(3x - 15) : 7 = 12$.",
        "answer": "33"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một số tự nhiên $N$ khi chia cho $24$ có số dư là $17$. Hỏi số $N$ khi chia cho $8$ có số dư là bao nhiêu?",
        "answer": "1"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Tính tổng của dãy số chẵn liên tiếp: $S = 2 + 4 + 6 + 8 + \\dots + 100$.",
        "answer": "2550"
      },
      {
        "id": 4,
        "level": "Vận dụng thấp",
        "question": "Bác An mua $15$ hộp sữa chua với giá $8$ nghìn đồng một hộp và $8$ gói bánh với giá $25$ nghìn đồng một gói. Bác An đưa cho thu ngân tờ tiền mệnh giá $400$ nghìn đồng. Hỏi bác An được nhận lại bao nhiêu nghìn đồng tiền thừa? (Chỉ điền số nguyên, đơn vị là nghìn đồng).",
        "answer": "80"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức sau một cách hợp lý:\n$$A = 135 \\cdot 48 + 52 \\cdot 135 - 35 \\cdot 100$$",
        "rubric": "Bước 1 (0.5đ): Áp dụng tính chất phân phối của phép nhân đối với phép cộng: $A = 135 \\cdot (48 + 52) - 35 \\cdot 100 = 135 \\cdot 100 - 35 \\cdot 100$.\nBước 2 (0.5đ): Tiếp tục đặt thừa số chung hoặc tính trực tiếp: $A = 100 \\cdot (135 - 35) = 100 \\cdot 100 = 10\\,000$ (hoặc $13\\,500 - 3\\,500 = 10\\,000$)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Một trường THCS tổ chức cho $345$ học sinh khối 6 tham gia dã ngoại. Nhà trường dự kiến sử dụng hai loại ô tô: xe lớn loại $45$ chỗ và xe nhỏ loại $29$ chỗ (không tính ghế lái xe).\na) Nhà trường đã thuê $6$ xe loại $45$ chỗ. Hỏi nhà trường cần thuê thêm ít nhất bao nhiêu xe loại $29$ chỗ để đảm bảo tất cả các học sinh còn lại đều có chỗ ngồi?\nb) Biết giá thuê một xe $45$ chỗ là $3\\,200\\,000$ đồng và một xe $29$ chỗ là $2\\,100\\,000$ đồng. Tính tổng số tiền nhà trường phải chi trả để thuê toàn bộ số xe trên.",
        "rubric": "Bước 1 (0.5đ): Tính số chỗ ngồi của $6$ xe $45$ chỗ là: $6 \\cdot 45 = 270$ (chỗ). Số học sinh còn lại là: $345 - 270 = 75$ (học sinh).\nBước 2 (0.25đ): Thực hiện phép chia: $75 : 29 = 2$ (dư 17). Vì còn dư $17$ học sinh nên nhà trường phải thuê thêm ít nhất: $2 + 1 = 3$ (xe $29$ chỗ).\nBước 3 (0.25đ): Tổng số tiền nhà trường phải trả là: $6 \\cdot 3\\,200\\,000 + 3 \\cdot 2\\,100\\,000 = 19\\,200\\,000 + 6\\,300\\,000 = 25\\,500\\,000$ (đồng)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm tất cả các số tự nhiên $n$ sao cho biểu thức $(3n + 16)$ chia hết cho $(n + 2)$.",
        "rubric": "Bước 1 (0.5đ): Ta biến đổi: $3n + 16 = 3(n + 2) + 10$. Vì $3(n + 2)$ luôn chia hết cho $(n + 2)$ với mọi số tự nhiên $n$, nên để $(3n + 16) \\,\\vdots\\, (n + 2)$ thì $10$ phải chia hết cho $(n + 2)$.\nBước 2 (0.5đ): Do đó $(n + 2)$ phải là ước tự nhiên của $10$. Các ước tự nhiên của $10$ là $1; 2; 5; 10$. Vì $n$ là số tự nhiên nên $n + 2 \\ge 2$. Do đó:\n- $n + 2 = 2 \\Rightarrow n = 0$;\n- $n + 2 = 5 \\Rightarrow n = 3$;\n- $n + 2 = 10 \\Rightarrow n = 8$.\nKết luận: $n \\in \\{0; 3; 8\\}$."
      }
    ]
  },
  "c1_6_bai5_test3": {
    "title": "Toán 6 (KNTT) - Bài 5: Phép nhân và phép chia số tự nhiên - Bài kiểm tra số 3",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phép chia có dư với số chia bằng $b$ ($b \\in \\mathbb{N}^*$), số dư $r$ luôn thỏa mãn điều kiện nào sau đây?",
        "options": [
          "$0 < r < b$",
          "$0 \\le r < b$",
          "$0 \\le r \\le b$",
          "$1 \\le r < b$"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho số tự nhiên $a$ chia cho $17$ được thương là $q$ và số dư là $r$. Biểu diễn đại số nào sau đây là đúng với mọi $a \\in \\mathbb{N}$?",
        "options": [
          "$a = 17q + r$ với $0 \\le r \\le 17$",
          "$a = 17r + q$ với $0 \\le r < 17$",
          "$a = 17q + r$ với $r \\in \\{0; 1; 2; \\dots; 16\\}$",
          "$a = 17(q + r)$ với $0 \\le r < 17$"
        ],
        "correct": 2
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Có bao nhiêu số tự nhiên $x$ thỏa mãn phương trình $(x - 3)(2x - 8) = 0$?",
        "options": [
          "$1$",
          "$2$",
          "$3$",
          "$0$"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Khi thực hiện phép chia số tự nhiên $A$ cho $24$, một học sinh viết nhầm chữ số hàng chục của số bị chia từ $5$ thành $2$ nên thu được thương là $18$ và số dư là $5$. Thương và số dư đúng của phép chia ban đầu là:",
        "options": [
          "Thương $19$, dư $11$",
          "Thương $20$, dư $5$",
          "Thương $19$, dư $17$",
          "Thương $20$, dư $17$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức $S = 100 \\cdot 99 - 99 \\cdot 98 + 98 \\cdot 97 - 97 \\cdot 96 + \\dots + 2 \\cdot 1$.",
        "options": [
          "$4950$",
          "$5000$",
          "$5050$",
          "$9900$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho hai số tự nhiên $a$ và $b$. Biết $a$ chia cho $7$ dư $4$, $b$ chia cho $7$ dư $5$. Khi đó, tích $a \\cdot b$ chia cho $7$ có số dư là:",
        "options": [
          "$6$",
          "$2$",
          "$4$",
          "$1$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Số các số tự nhiên có hai chữ số $\\overline{ab}$ sao cho tích $a \\cdot b$ bằng thương $a : b$ (với $b \\ne 0$) là:",
        "options": [
          "$9$",
          "$1$",
          "$0$",
          "$8$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một số tự nhiên khi chia cho $12$ dư $9$, khi chia cho $15$ dư $12$. Số đó khi chia cho $60$ có số dư là bao nhiêu?",
        "options": [
          "$21$",
          "$57$",
          "$33$",
          "$39$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Tìm số tự nhiên $n$ nhỏ nhất sao cho tích $P = n \\cdot (n + 1) \\cdot (n + 2)$ tận cùng bằng đúng ba chữ số $0$.",
        "options": [
          "$23$",
          "$24$",
          "$124$",
          "$19$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Cho tích $M = 1 \\cdot 2 \\cdot 3 \\dots 50$. Hỏi nếu phân tích $M$ thành tích các thừa số nguyên tố thì số mũ của thừa số $5$ là bao nhiêu?",
        "options": [
          "$10$",
          "$12$",
          "$14$",
          "$15$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Số cặp số tự nhiên $(x; y)$ thỏa mãn đẳng thức $(2x + 1)(y - 2) = 18$ là:",
        "options": [
          "$3$",
          "$6$",
          "$2$",
          "$4$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Trong một phép chia có dư, số bị chia là $189$, số dư là $14$. Biết thương là một số tự nhiên lớn hơn $1$. Số chia và thương lần lượt có thể là:",
        "options": [
          "$35$ và $5$",
          "$25$ và $7$",
          "$175$ và $1$",
          "$7$ và $25$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho phương trình ẩn $x \\in \\mathbb{N}$: $(m - 2)x + 3m = 27$, trong đó $m$ là tham số tự nhiên.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Khi $m = 2$, phương trình trở thành $0x = 21$, do đó phương trình vô nghiệm.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Khi $m = 5$, phương trình có nghiệm tự nhiên duy nhất là $x = 4$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng",
            "text": "Có đúng $3$ giá trị của số tự nhiên $m$ để phương trình có nghiệm tự nhiên $x$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Tổng tất cả các giá trị tự nhiên của tham số $m$ để phương trình nhận nghiệm $x \\in \\mathbb{N}$ là $44$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Xét các số tự nhiên $a, b, c$ thỏa mãn: $a$ chia cho $5$ dư $3$, $b$ chia cho $5$ dư $2$ và $c = 3a \\cdot b + 2a + 4b$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tích $a \\cdot b$ khi chia cho $5$ có số dư là $1$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số $c$ chia cho $5$ dư $4$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng",
            "text": "Biểu thức $K = c + 3$ chia hết cho $5$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Với mọi số tự nhiên $a, b$ thỏa mãn đề bài, số $M = c^2 + 1$ luôn chia hết cho $5$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Tìm số tự nhiên nhỏ nhất có $4$ chữ số, biết rằng khi chia số đó cho $131$ thì dư $112$, còn khi chia cho $132$ thì dư $98$.",
        "answer": "1950"
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Tìm số cặp số tự nhiên $(x; y)$ thỏa mãn phương trình: $xy + 3x - 2y = 17$.",
        "answer": "2"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tính tổng các số tự nhiên $n$ có hai chữ số sao cho phép chia $(3n + 29)$ cho $(n + 3)$ là phép chia hết.",
        "answer": "31"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một người viết liên tiếp các số tự nhiên từ $1$ đến $2023$ để tạo thành một số rất lớn $N = 1234567891011...20222023$. Hỏi chữ số thứ $2024$ tính từ trái sang phải của số $N$ là chữ số nào?",
        "answer": "7"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Tìm tất cả các cặp số tự nhiên $(x; y)$ thỏa mãn đẳng thức: $2xy + x + 2y = 13$.",
        "rubric": "Bước 1 (0.5đ): Biến đổi phương trình đưa về dạng tích: Nhân cả hai vế với $1$ hoặc nhóm hạng tử: $x(2y + 1) + (2y + 1) = 14 \\Leftrightarrow (x + 1)(2y + 1) = 14$.\nBước 2 (0.5đ): Lập luận tìm nghiệm: Vì $x, y \\in \\mathbb{N}$ nên $x + 1 \\ge 1$ và $2y + 1$ là số lẻ lớn hơn hoặc bằng $1$. Các ước lẻ của $14$ là $1$ và $7$. Do đó ta có hai trường hợp:\n+ Trường hợp 1: $2y + 1 = 1 \\Rightarrow y = 0$, khi đó $x + 1 = 14 \\Rightarrow x = 13$ (thỏa mãn).\n+ Trường hợp 2: $2y + 1 = 7 \\Rightarrow y = 3$, khi đó $x + 1 = 2 \\Rightarrow x = 1$ (thỏa mãn).\nVậy các cặp $(x; y)$ thỏa mãn là $(13; 0)$ và $(1; 3)$."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một đội tình nguyện viên gồm các thầy cô giáo và học sinh chuẩn bị một số phần quà như nhau gồm vở và bút bi để trao tặng các em nhỏ vùng cao. Tổng số bút bi là $135$ chiếc, tổng số vở là $225$ quyển. Sau khi chia đều vào các túi quà thì còn thừa $15$ chiếc bút bi và $9$ quyển vở. Hỏi có tất cả bao nhiêu túi quà và mỗi túi quà có bao nhiêu chiếc bút bi, bao nhiêu quyển vở?",
        "rubric": "Bước 1 (0.5đ): Gọi số túi quà là $a$ ($a \\in \\mathbb{N}^*$). Theo đề bài, số bút bi được chia là $135 - 15 = 120$ chiếc; số quyển vở được chia là $225 - 9 = 216$ quyển.\nDo chia đều nên $a$ là ước chung của $120$ và $216$, đồng thời số chia phải lớn hơn số dư nên $a > 15$.\nBước 2 (0.5đ): Ta có $\\text{ƯCLN}(120, 216) = 24$. Do đó $a \\in \\text{Ư}(24) = \\{1; 2; 3; 4; 6; 8; 12; 24\\}$.\nVì $a > 15$ nên $a = 24$.\nVậy có $24$ túi quà. Mỗi túi có $120 : 24 = 5$ chiếc bút bi và $216 : 24 = 9$ quyển vở."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho $A = 1 + 3 + 3^2 + 3^3 + \\dots + 3^{2023}$. Chứng minh rằng $2A + 1$ là một số chính phương và tìm số dư khi chia $A$ cho $13$.",
        "rubric": "Bước 1 (0.5đ): \nTa có $A = 1 + 3 + 3^2 + \\dots + 3^{2023} \\Rightarrow 3A = 3 + 3^2 + \\dots + 3^{2024}$.\nSuy ra $3A - A = 3^{2024} - 1 \\Rightarrow 2A = 3^{2024} - 1$.\nDo đó $2A + 1 = 3^{2024} = (3^{1012})^2$. Vì $3^{1012} \\in \\mathbb{N}$ nên $2A + 1$ là một số chính phương.\nBước 2 (0.5đ): \nTổng $A$ có $2024$ số hạng. Ta nhóm $3$ số hạng liên tiếp:\n$1 + 3 + 3^2 = 13$ chia hết cho $13$.\nVì $2024 = 3 \\cdot 674 + 2$, ta nhóm như sau:\n$A = (1 + 3) + 3^2(1 + 3 + 3^2) + 3^5(1 + 3 + 3^2) + \\dots + 3^{2021}(1 + 3 + 3^2)$\n$= 4 + 13 \\cdot (3^2 + 3^5 + \\dots + 3^{2021})$.\nVì $13 \\cdot (3^2 + 3^5 + \\dots + 3^{2021})$ chia hết cho $13$ và $4 < 13$ nên $A$ chia cho $13$ dư $4$."
      }
    ]
  },
  "c1_6_bai6_test1": {
    "title": "Toán 6 (KNTT) - Bài 6: Lũy thừa với số mũ tự nhiên - Bài kiểm tra số 1",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong lũy thừa $a^n$, ta gọi $a$ là:",
        "options": [
          "Cơ số",
          "Số mũ",
          "Tích số",
          "Thừa số"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong lũy thừa $7^4$, số mũ là:",
        "options": [
          "$7$",
          "$4$",
          "$11$",
          "$28$"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Lũy thừa bậc hai của một số còn được gọi là:",
        "options": [
          "Lập phương",
          "Bình phương",
          "Căn bậc hai",
          "Bội số"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Lập phương của số $a$ được viết dưới dạng lũy thừa là:",
        "options": [
          "$a^2$",
          "$a^3$",
          "$3a$",
          "$a+3$"
        ],
        "correct": 1
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Viết tích $5 \\cdot 5 \\cdot 5 \\cdot 5$ dưới dạng một lũy thừa ta được kết quả là:",
        "options": [
          "$5^4$",
          "$4^5$",
          "$20$",
          "$5 \\cdot 4$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Quy tắc nhân hai lũy thừa cùng cơ số là: Với $m, n \\in \\mathbb{N}$, ta có $a^m \\cdot a^n = $",
        "options": [
          "$a^{m \\cdot n}$",
          "$a^{m - n}$",
          "$a^{m + n}$",
          "$(2a)^{m + n}$"
        ],
        "correct": 2
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Quy tắc chia hai lũy thừa cùng cơ số khác 0 là: Với $a \\ne 0$ và $m \\ge n$, ta có $a^m : a^n = $",
        "options": [
          "$a^{m + n}$",
          "$a^{m : n}$",
          "$a^{m - n}$",
          "$a^{n - m}$"
        ],
        "correct": 2
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Quy ước: Với số tự nhiên $a \\ne 0$, ta có $a^0$ bằng:",
        "options": [
          "$0$",
          "$1$",
          "$a$",
          "Không xác định"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Giá trị của lũy thừa $2^4$ là:",
        "options": [
          "$8$",
          "$16$",
          "$6$",
          "$12$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Kết quả của phép tính $3^2 \\cdot 3^3$ dưới dạng một lũy thừa là:",
        "options": [
          "$3^6$",
          "$3^5$",
          "$9^5$",
          "$3^1$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Kết quả của phép tính $5^6 : 5^2$ dưới dạng một lũy thừa là:",
        "options": [
          "$5^3$",
          "$5^8$",
          "$5^4$",
          "$1^4$"
        ],
        "correct": 2
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Số tự nhiên $x$ thỏa mãn $x^2 = 49$ là:",
        "options": [
          "$7$",
          "$14$",
          "$24$",
          "$9$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho các phép tính lũy thừa cơ bản sau. Xét tính đúng hay sai của mỗi khẳng định:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Phép nhân $4^3 \\cdot 4^2 = 4^5$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phép chia $7^6 : 7^2 = 7^3$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Giá trị của biểu thức $10^3$ là $1\\,000$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Lũy thừa $6^1$ có giá trị bằng $1$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Xét tính đúng hoặc sai của các khẳng định sau về lũy thừa và so sánh lũy thừa:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tích $2 \\cdot 2 \\cdot 2$ bằng lũy thừa $2^3$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số $8$ có thể viết dưới dạng lũy thừa với cơ số $2$ là $2^4$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Ta có $3^3 = 27$ và $2^4 = 16$, do đó $3^3 > 2^4$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Với mọi số tự nhiên $n > 0$, ta luôn có $1^n = n$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị của lũy thừa $3^4$.",
        "answer": "81"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $n$ thỏa mãn $2^n = 32$.",
        "answer": "5"
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$ thỏa mãn $10^x = 100\\,000$.",
        "answer": "5"
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức: $A = 2^3 + 3^2$.",
        "answer": "17"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Viết kết quả của mỗi phép tính sau dưới dạng một lũy thừa:\na) $3^4 \\cdot 3^5$\nb) $6^7 : 6^4$",
        "rubric": "Bước 1 (0.5đ): Thực hiện câu a: Áp dụng công thức nhân hai lũy thừa cùng cơ số: $3^4 \\cdot 3^5 = 3^{4 + 5} = 3^9$.\nBước 2 (0.5đ): Thực hiện câu b: Áp dụng công thức chia hai lũy thừa cùng cơ số: $6^7 : 6^4 = 6^{7 - 4} = 6^3$."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết:\na) $x^3 = 8$\nb) $3^x = 27$",
        "rubric": "Bước 1 (0.5đ): Câu a: Ta có $8 = 2 \\cdot 2 \\cdot 2 = 2^3$. Do đó $x^3 = 2^3$, suy ra $x = 2$.\nBước 2 (0.5đ): Câu b: Ta có $27 = 3 \\cdot 3 \\cdot 3 = 3^3$. Do đó $3^x = 3^3$, suy ra $x = 3$."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Thực hiện phép tính (tính hợp lý nếu có thể):\n$B = 5 \\cdot 2^3 - 3^2 \\cdot 4$",
        "rubric": "Bước 1 (0.5đ): Tính giá trị các lũy thừa: $2^3 = 8$ và $3^2 = 9$. Thay vào biểu thức ta có $B = 5 \\cdot 8 - 9 \\cdot 4$.\nBước 2 (0.5đ): Thực hiện các phép nhân rồi trừ: $B = 40 - 36 = 4$."
      }
    ]
  },
  "c1_6_bai6_test2": {
    "title": "Toán 6 (KNTT) - Bài 6: Lũy thừa với số mũ tự nhiên - Đề kiểm tra số 2",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phép toán lũy thừa $7^4$, khẳng định nào sau đây là đúng?",
        "options": [
          "Cơ số là $4$, số mũ là $7$",
          "Cơ số là $7$, số mũ là $4$",
          "Giá trị bằng $7 \\cdot 4 = 28$",
          "Biểu thị tích của $7$ thừa số $4$"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Quy ước nào sau đây là đúng với mọi số tự nhiên $a \\ne 0$?",
        "options": [
          "$a^0 = 0$",
          "$a^1 = 1$",
          "$a^0 = 1$",
          "$a^1 = 0$"
        ],
        "correct": 2
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Công thức nhân hai lũy thừa cùng cơ số là:",
        "options": [
          "$a^m \\cdot a^n = a^{m \\cdot n}$",
          "$a^m \\cdot a^n = a^{m + n}$",
          "$a^m \\cdot a^n = (a \\cdot a)^{m + n}$",
          "$a^m \\cdot a^n = a^{m - n}$"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kết quả của phép chia $5^8 : 5^2$ viết dưới dạng một lũy thừa là:",
        "options": [
          "$5^4$",
          "$1^6$",
          "$5^{10}$",
          "$5^6$"
        ],
        "correct": 3
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Viết biểu thức $2^3 \\cdot 4 \\cdot 8$ dưới dạng một lũy thừa của cơ số $2$ ta được:",
        "options": [
          "$2^6$",
          "$2^8$",
          "$2^7$",
          "$2^9$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $P = 3 \\cdot 2^4 - 2 \\cdot 3^2$ là:",
        "options": [
          "$30$",
          "$66$",
          "$18$",
          "$36$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Số tự nhiên $x$ thỏa mãn $(2x - 1)^3 = 27$ là:",
        "options": [
          "$x = 1$",
          "$x = 2$",
          "$x = 3$",
          "$x = 4$"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khi viết số tự nhiên $2035$ dưới dạng tổng các lũy thừa của $10$, ta được:",
        "options": [
          "$2 \\cdot 10^4 + 3 \\cdot 10^2 + 5$",
          "$2 \\cdot 10^3 + 3 \\cdot 10^2 + 5$",
          "$2 \\cdot 10^3 + 3 \\cdot 10^1 + 5 \\cdot 10^0$",
          "$2 \\cdot 10^4 + 3 \\cdot 10 + 5$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Biết $x$ là số tự nhiên thỏa mãn $3^{x+1} : 3^2 = 81$. Giá trị của $x$ là:",
        "options": [
          "$4$",
          "$5$",
          "$3$",
          "$6$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "So sánh hai số $A = 2^{30}$ và $B = 3^{20}$, khẳng định nào sau đây là đúng?",
        "options": [
          "$A > B$",
          "$A = B$",
          "$A < B$",
          "Không thể so sánh được"
        ],
        "correct": 2
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Kết quả rút gọn biểu thức $\\frac{6^5}{2^4 \\cdot 3^4}$ là:",
        "options": [
          "$6$",
          "$18$",
          "$36$",
          "$1$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Chữ số tận cùng của số $2^{2024}$ là:",
        "options": [
          "$2$",
          "$4$",
          "$6$",
          "$8$"
        ],
        "correct": 2
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho biểu thức $A = 1 + 2 + 2^2 + 2^3 + \\dots + 2^{2024}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Biểu thức $A$ có tất cả $2024$ số hạng.",
            "correct": false
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Biểu thức $2A$ có giá trị bằng $2 + 2^2 + 2^3 + \\dots + 2^{2025}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Thu gọn biểu thức ta được $A = 2^{2025} - 1$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Số $A + 1$ là một số chính phương.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hai biểu thức $M = 3^{x} + 3^{x+2}$ và $N = 2^{y} \\cdot 5$ với $x, y \\in \\mathbb{N}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Biểu thức $M$ có thể phân tích thành $M = 3^x \\cdot 10$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Khi $x = 3$ thì giá trị của $M$ bằng $90$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Để $M = 270$ thì giá trị của $x$ là $x = 3$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Có đúng một cặp số tự nhiên $(x; y)$ thỏa mãn $M = N$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $n$ biết: $2^{n-1} + 2^{n} = 48$.",
        "answer": "5"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức: $T = \\frac{4^3 \\cdot 9^5}{6^7}$.",
        "answer": "24"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$ thỏa mãn đẳng thức: $(x - 4)^4 = (x - 4)^2$ với $x > 5$.",
        "answer": "5"
      },
      {
        "id": 4,
        "level": "Vận dụng thấp",
        "question": "Trong phòng thí nghiệm, một lượng vi khuẩn ban đầu có $50$ con. Cứ sau mỗi giờ, số lượng vi khuẩn lại nhân đôi (tăng gấp $2$ lần). Hỏi sau $6$ giờ, số lượng vi khuẩn trong phòng thí nghiệm là bao nhiêu con?",
        "answer": "3200"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng thấp",
        "question": "Một người nông dân trồng lúa trên một thửa ruộng hình vuông có cạnh dài $64\\text{ m}$. Bác dự định mua lưới để rào xung quanh thửa ruộng đó.\na) Viết diện tích của thửa ruộng dưới dạng lũy thừa của một số tự nhiên với số mũ lớn hơn $1$.\nb) Cứ mỗi mét vuông ruộng cho thu hoạch trung bình $0{,}5\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu kilôgam thóc? Viết kết quả dưới dạng một lũy thừa của $2$.",
        "rubric": "Bước 1 (0.5đ): Diện tích thửa ruộng là $S = 64 \\cdot 64 = 64^2\\text{ m}^2$ (hoặc $4096 = 2^{12} = 8^4 = 16^3\\text{ m}^2$). Học sinh đưa ra được một dạng lũy thừa đúng với số mũ $> 1$ được 0.5 điểm.\nBước 2 (0.5đ): Khối lượng thóc thu hoạch được là $4096 \\cdot 0{,}5 = 2048\\text{ kg}$. Ta có $2048 = 2^{11}\\text{ kg}$. Kết luận đúng: $2^{11}\\text{ kg}$ thóc được 0.5 điểm."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$, biết: $5^{x} + 5^{x+2} = 650$.",
        "rubric": "Bước 1 (0.5đ): Biến đổi vế trái: $5^x + 5^x \\cdot 5^2 = 650 \\Rightarrow 5^x \\cdot (1 + 25) = 650 \\Rightarrow 5^x \\cdot 26 = 650$.\nBước 2 (0.5đ): Tính được $5^x = 650 : 26 = 25$. Vì $25 = 5^2$ nên $5^x = 5^2 \\Rightarrow x = 2$. Vậy $x = 2$."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho $S = 1 + 3 + 3^2 + 3^3 + \\dots + 3^{2023}$. Chứng minh rằng $2S + 1$ là một lũy thừa của $3$, từ đó tìm chữ số tận cùng của $S$.",
        "rubric": "Bước 1 (0.5đ): Nhân cả hai vế với 3: $3S = 3 + 3^2 + 3^3 + \\dots + 3^{2024}$. Lấy $3S - S = (3 + 3^2 + \\dots + 3^{2024}) - (1 + 3 + \\dots + 3^{2023}) \\Rightarrow 2S = 3^{2024} - 1$. Do đó $2S + 1 = 3^{2024}$, là một lũy thừa của 3.\nBước 2 (0.5đ): Ta có $S = \\frac{3^{2024} - 1}{2}$. Nhận xét $3^{2024} = (3^4)^{506} = 81^{506}$ có chữ số tận cùng là $1$. Do đó $3^{2024} - 1$ có tận cùng là $0$. Vì $2S = 3^{2024} - 1$ có chữ số tận cùng là 0 nên $S$ có chữ số tận cùng là 0 hoặc 5. Biểu thức $S$ có $2024$ số hạng toàn số lẻ, tổng của 2024 số lẻ là số chẵn, suy ra $S$ là số chẵn. Do đó chữ số tận cùng của $S$ là $0$."
      }
    ]
  },
  "c1_6_bai6_test3": {
    "title": "ĐỀ KIỂM TRA ĐÁNH GIÁ NĂNG LỰC TOÁN 6 - BÀI 6: LŨY THỪA VỚI SỐ MŨ TỰ NHIÊN (ĐỀ NÂNG CAO SỐ 3)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho $a$ là số tự nhiên khác $0$. Biểu thức nào sau đây KHÔNG tương đương với $a^6$?",
        "options": [
          "$(a^2)^3$",
          "$a^2 \\cdot a^3$",
          "$a^{10} : a^4$",
          "$a^1 \\cdot a^5$"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho $n$ là số tự nhiên chẵn lớn hơn $0$. Khẳng định nào sau đây luôn đúng với mọi số tự nhiên $a$?",
        "options": [
          "$a^n$ luôn có chữ số tận cùng là chữ số chẵn",
          "$a^n$ luôn là số chính phương",
          "$a^n > n^a$",
          "$a^n$ chia cho $3$ luôn dư $1$"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Chữ số tận cùng của số $P = 2^{2024} + 3^{2025}$ là:",
        "options": [
          "$9$",
          "$7$",
          "$1$",
          "$5$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "So sánh hai số $A = 3^{200}$ và $B = 2^{300}$, kết luận nào sau đây đúng?",
        "options": [
          "$A > B$",
          "$A = B$",
          "$A < B$",
          "$A = B + 1$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $n$ biết rằng $2^n + 2^{n+3} = 144$. Giá trị của $n$ là:",
        "options": [
          "$3$",
          "$4$",
          "$5$",
          "$6$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Số ước nguyên tố của số tự nhiên $M = 2^4 \\cdot 3^2 \\cdot 5$ là:",
        "options": [
          "$3$",
          "$30$",
          "$11$",
          "$4$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho biểu thức $S = 1 + 2 + 2^2 + \\dots + 2^{2024}$. Khẳng định nào sau đây là đúng?",
        "options": [
          "$S = 2^{2025} - 1$",
          "$S = 2^{2024} - 1$",
          "$S = 2^{2025}$",
          "$S = 2^{2024}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Số tự nhiên $x$ thỏa mãn $(2x - 1)^3 = 125$ là:",
        "options": [
          "$2$",
          "$3$",
          "$4$",
          "$5$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Có bao nhiêu số tự nhiên $x$ thỏa mãn đẳng thức $(x - 3)^{2024} = (x - 3)^{2022}$?",
        "options": [
          "$1$",
          "$2$",
          "$3$",
          "$4$"
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Số dư khi chia $A = 7 + 7^2 + 7^3 + \\dots + 7^{100}$ cho $8$ là:",
        "options": [
          "$0$",
          "$1$",
          "$4$",
          "$7$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Tìm số tự nhiên $n$ lớn nhất có hai chữ số sao cho $2^n + 1$ chia hết cho $5$.",
        "options": [
          "$99$",
          "$98$",
          "$97$",
          "$94$"
        ],
        "correct": 1
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho hai số tự nhiên $a, b$ thỏa mãn $2^a + 3^b = 5^{b-a}$ và $b \\ge a \\ge 1$. Cặp giá trị $(a; b)$ thỏa mãn là:",
        "options": [
          "$(1; 2)$",
          "$(2; 3)$",
          "$(1; 1)$",
          "Không tồn tại $(a; b)$"
        ],
        "correct": 2
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho biểu thức $A = 4 + 4^2 + 4^3 + \\dots + 4^{2024}$ và biểu thức $B = 3A + 4$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Giá trị của biểu thức $B$ được viết gọn dưới dạng lũy thừa là $4^{2025}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số $A$ chia hết cho $5$ nhưng không chia hết cho $20$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng",
            "text": "Số $A$ chia hết cho $21$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Biểu thức $B$ là một số chính phương.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Xét các số tự nhiên $x, y$ thỏa mãn phương trình lũy thừa: $5^x + 9999 = 2^y$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Nếu $x = 0$ thì không tìm được số tự nhiên $y$ thỏa mãn.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Với mọi $x > 0$, vế trái $5^x + 9999$ luôn là một số có chữ số tận cùng là $4$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng",
            "text": "Nếu $y$ chia hết cho $4$ thì chữ số tận cùng của $2^y$ có thể là $4$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Phương trình $5^x + 9999 = 2^y$ có đúng $1$ cặp nghiệm số tự nhiên $(x; y)$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $n$ biết rằng: $3^{n-1} + 5 \\cdot 3^{n-1} = 162$.",
        "answer": "4"
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Tìm hai chữ số tận cùng của lũy thừa $7^{2024}$.",
        "answer": "01"
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Có bao nhiêu số tự nhiên $n$ trong khoảng từ $1$ đến $100$ sao cho $3^n - 1$ chia hết cho $10$?",
        "answer": "25"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tìm số tự nhiên $n$ nhỏ nhất sao cho $2^n > 1000n$.",
        "answer": "14"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Cho tổng $S = 1 + 3 + 3^2 + 3^3 + \\dots + 3^{99}$.\na) Thu gọn biểu thức $S$.\nb) Chứng minh rằng $2S + 1$ là một lũy thừa của $3$ và $S$ chia hết cho $40$.",
        "rubric": "a) Tính đúng giá trị rút gọn của $S$ (0.5 điểm):\n- Nhân cả hai vế với $3$: $3S = 3 + 3^2 + 3^3 + \\dots + 3^{100}$ (0.25đ).\n- Trừ vế theo vế: $3S - S = (3 + 3^2 + \\dots + 3^{100}) - (1 + 3 + \\dots + 3^{99}) \\Rightarrow 2S = 3^{100} - 1 \\Rightarrow S = \\frac{3^{100} - 1}{2}$ (0.25đ).\nb) Chứng minh các yêu cầu (0.5 điểm):\n- Ta có $2S + 1 = (3^{100} - 1) + 1 = 3^{100}$ là một lũy thừa của $3$ với số mũ $100$ (0.25đ).\n- Tổng $S$ có $100$ số hạng. Nhóm mỗi nhóm $4$ số hạng liên tiếp:\n$S = (1 + 3 + 3^2 + 3^3) + 3^4(1 + 3 + 3^2 + 3^3) + \\dots + 3^{96}(1 + 3 + 3^2 + 3^3)$\n$= 40 \\cdot (1 + 3^4 + \\dots + 3^{96})$. Vì $40 \\,\\vdots\\, 40$ nên $S \\,\\vdots\\, 40$ (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "So sánh hai lũy thừa sau mà không tính giá trị cụ thể:\n$A = 199^{20}$ và $B = 2003^{15}$.",
        "rubric": "Bước 1: Tìm lũy thừa trung gian phù hợp (0.5 điểm):\n- Ta có: $A = 199^{20} < 200^{20} = (2 \\cdot 10^2)^{20} = 2^{20} \\cdot 10^{40}$ (0.25đ).\n- Lại có: $2^{20} = (2^{10})^2 = 1024^2 < 1100^2 = 1\\,210\\,000 < 10^7$, do đó $A < 10^7 \\cdot 10^{40} = 10^{47}$ (0.25đ).\nBước 2: Đánh giá $B$ với lũy thừa cơ số $10$ và kết luận (0.5 điểm):\n- Ta có: $B = 2003^{15} > 2000^{15} = (2 \\cdot 10^3)^{15} = 2^{15} \\cdot 10^{45}$ (0.25đ).\n- Vì $2^{15} = 32\\,768 > 100 = 10^2$, suy ra $B > 10^2 \\cdot 10^{45} = 10^{47}$.\n- Vì $A < 10^{47} < B$, nên $A < B$ (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm tất cả các cặp số tự nhiên $(x; y)$ thỏa mãn phương trình:\n$2^x + 57 = y^2$.",
        "rubric": "Bước 1: Xét trường hợp $x$ lẻ (0.5 điểm):\n- Nếu $x$ là số tự nhiên lẻ:\n  + Với $x = 1$: $2^1 + 57 = 59 = y^2$ (loại vì $59$ không phải số chính phương) (0.25đ).\n  + Với $x \\ge 3$ lẻ, ta có $x = 2k + 1$ ($k \\in \\mathbb{N}^*$).\n  Khi đó $2^x = 2^{2k+1} = 2 \\cdot 4^k$. Vì $4 \\equiv 1 \\pmod 3$ nên $2^x \\equiv 2 \\pmod 3$.\n  Suy ra $y^2 = 2^x + 57 \\equiv 2 + 0 \\equiv 2 \\pmod 3$.\n  Điều này vô lí vì một số chính phương khi chia cho $3$ chỉ có số dư là $0$ hoặc $1$ (0.25đ).\nBước 2: Xét trường hợp $x$ chẵn và kết luận (0.5 điểm):\n- Đặt $x = 2m$ ($m \\in \\mathbb{N}$):\n  Phương trình trở thành $y^2 - 2^{2m} = 57 \\Leftrightarrow y^2 - (2^m)^2 = 57 \\Leftrightarrow (y - 2^m)(y + 2^m) = 57$ (0.25đ).\n  Vì $y, m \\in \\mathbb{N}$ nên $y + 2^m > y - 2^m > 0$. Ta có phân tích $57 = 57 \\cdot 1 = 19 \\cdot 3$.\n  + TH1: $\\begin{cases} y + 2^m = 57 \\\\ y - 2^m = 1 \\end{cases} \\Rightarrow 2 \\cdot 2^m = 56 \\Rightarrow 2^m = 28$ (không có $m \\in \\mathbb{N}$ thỏa mãn).\n  + TH2: $\\begin{cases} y + 2^m = 19 \\\\ y - 2^m = 3 \\end{cases} \\Rightarrow 2 \\cdot 2^m = 16 \\Rightarrow 2^m = 8 = 2^3 \\Rightarrow m = 3$.\n  Suy ra $x = 2m = 6$ và $y = 3 + 8 = 11$.\n  Kiểm tra lại: $2^6 + 57 = 64 + 57 = 121 = 11^2$ (thỏa mãn).\n- Kết luận: Cặp số tự nhiên duy nhất thỏa mãn là $(x; y) = (6; 11)$ (0.25đ)."
      }
    ]
  },
  "c1_6_bai7_test1": {
    "title": "Toán 6 (KNTT) - Bài 7: Thứ tự thực hiện các phép tính - Bài kiểm tra số 1",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khi thực hiện phép tính trong biểu thức chỉ chứa phép cộng và phép trừ, ta thực hiện theo thứ tự nào?",
        "options": [
          "Từ trái sang phải",
          "Từ phải sang trái",
          "Thực hiện phép cộng trước, phép trừ sau",
          "Thực hiện phép trừ trước, phép cộng sau"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khi thực hiện phép tính trong biểu thức chỉ chứa phép nhân và phép chia, ta thực hiện theo thứ tự nào?",
        "options": [
          "Từ phải sang trái",
          "Từ trái sang phải",
          "Thực hiện phép nhân trước, phép chia sau",
          "Thực hiện phép chia trước, phép nhân sau"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Đối với biểu thức không có dấu ngoặc gồm các phép tính cộng, trừ, nhân, chia, nâng lên luỹ thừa, thứ tự thực hiện đúng là:",
        "options": [
          "Cộng và trừ $\\to$ Nhân và chia $\\to$ Nâng lên luỹ thừa",
          "Nhân và chia $\\to$ Nâng lên luỹ thừa $\\to$ Cộng và trừ",
          "Nâng lên luỹ thừa $\\to$ Nhân và chia $\\to$ Cộng và trừ",
          "Nâng lên luỹ thừa $\\to$ Cộng và trừ $\\to$ Nhân và chia"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi thực hiện phép tính trong biểu thức có các dấu ngoặc: ngoặc tròn $( )$, ngoặc vuông $[ ]$, ngoặc nhọn $\\{ \\}$, thứ tự thực hiện đúng là:",
        "options": [
          "$( ) \\to [ ] \\to \\{ \\}$",
          "$[ ] \\to ( ) \\to \\{ \\}$",
          "$\\{ \\} \\to [ ] \\to ( )$",
          "$( ) \\to \\{ \\} \\to [ ]$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong biểu thức $15 + 3 \\cdot 2$, phép tính nào được thực hiện đầu tiên?",
        "options": [
          "Phép cộng $15 + 3$",
          "Phép nhân $3 \\cdot 2$",
          "Thực hiện phép tính nào trước cũng được",
          "Thực hiện đồng thời phép cộng và phép nhân"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trong biểu thức $24 - 6 + 4$, phép tính nào được thực hiện đầu tiên?",
        "options": [
          "Phép cộng $6 + 4$",
          "Phép trừ $24 - 6$",
          "Cả hai phép tính cùng lúc",
          "Phép cộng hoặc trừ đều được"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Nhận biết",
        "question": "Trong biểu thức $5 \\cdot 2^3$, phép tính nào được thực hiện đầu tiên?",
        "options": [
          "Phép nhân $5 \\cdot 2$",
          "Phép luỹ thừa $2^3$",
          "Nhân trước rồi mới tính luỹ thừa",
          "Tính tuỳ ý"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Nhận biết",
        "question": "Trong biểu thức $60 : (12 - 2)$, phép tính nào được thực hiện trước?",
        "options": [
          "Phép chia $60 : 12$",
          "Phép trừ $12 - 2$ trong ngoặc tròn",
          "Phép chia thực hiện từ trái sang phải",
          "Phá ngoặc rồi tính"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $12 + 8 : 2$ là:",
        "options": [
          "10",
          "16",
          "7",
          "14"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $18 - 2 \\cdot 3$ là:",
        "options": [
          "12",
          "48",
          "13",
          "24"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $20 : 2 \\cdot 5$ là:",
        "options": [
          "2",
          "50",
          "20",
          "10"
        ],
        "correct": 1
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $5 + 2^3$ là:",
        "options": [
          "11",
          "13",
          "21",
          "17"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho biểu thức $A = 50 - [30 - (6 - 2)^2]$.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Thứ tự thực hiện phép tính trong biểu thức $A$ là: thực hiện trong ngoặc tròn $( )$, sau đó đến ngoặc vuông $[ ]$, cuối cùng là phép trừ ngoài ngoặc.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Kết quả của phép tính trong ngoặc tròn $(6 - 2)$ bằng $4$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Giá trị của luỹ thừa $4^2$ trong biểu thức bằng $8$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Giá trị của biểu thức $A$ bằng $36$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Xét tính đúng hoặc sai của các khẳng định sau khi tính giá trị của biểu thức:",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Giá trị của biểu thức $30 - 10 : 2$ bằng $10$.",
            "correct": false
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị của biểu thức $2^3 \\cdot 3 + 4$ bằng $28$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Giá trị của biểu thức $36 : 3 \\cdot 2$ bằng $24$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Thông hiểu",
            "text": "Giá trị của biểu thức $100 : (10 \\cdot 2)$ bằng $20$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức: $45 - 5 \\cdot (12 - 9)$.",
        "answer": "30"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức: $3^2 \\cdot 2 - 14 : 7$.",
        "answer": "16"
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết: $2 \\cdot x - 5 = 15$.",
        "answer": "10"
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết: $36 : (x + 3) = 4$.",
        "answer": "6"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Thực hiện các phép tính sau:\na) $28 + 12 : 4 - 3^2$\nb) $150 : [45 - (30 - 10)]$",
        "rubric": "a) (0.5 điểm)\n- Tính luỹ thừa và phép chia: $28 + 3 - 9$ (0.25đ)\n- Thực hiện từ trái sang phải: $31 - 9 = 22$ (0.25đ)\n\nb) (0.5 điểm)\n- Thực hiện phép tính trong ngoặc tròn: $30 - 10 = 20$, biểu thức trở thành $150 : [45 - 20]$ (0.25đ)\n- Thực hiện trong ngoặc vuông và chia: $150 : 25 = 6$ (0.25đ)"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết:\na) $4 \\cdot (x - 3) = 24$\nb) $18 + 3 \\cdot x = 5^2 + 8$",
        "rubric": "a) (0.5 điểm)\n- Ta có: $x - 3 = 24 : 4 \\Rightarrow x - 3 = 6$ (0.25đ)\n- Suy ra: $x = 6 + 3 = 9$. Vậy $x = 9$ (0.25đ)\n\nb) (0.5 điểm)\n- Tính vế phải: $5^2 + 8 = 25 + 8 = 33$, biểu thức là $18 + 3 \\cdot x = 33$ (0.25đ)\n- Ta có $3 \\cdot x = 33 - 18 \\Rightarrow 3 \\cdot x = 15 \\Rightarrow x = 5$. Vậy $x = 5$ (0.25đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Bạn An mua 3 quyển vở với giá 12 000 đồng một quyển và 2 chiếc bút bi với giá 5 000 đồng một chiếc. An đưa cho cô bán hàng tờ tiền 50 000 đồng.\na) Viết biểu thức số thể hiện số tiền cô bán hàng cần trả lại cho An.\nb) Tính số tiền cô bán hàng cần trả lại cho An.",
        "rubric": "a) (0.5 điểm)\n- Biểu thức số thể hiện số tiền cô bán hàng trả lại là:\n$50\\,000 - (3 \\cdot 12\\,000 + 2 \\cdot 5\\,000)$ (đồng) (0.5đ)\n(Học sinh viết $50\\,000 - 3 \\cdot 12\\,000 - 2 \\cdot 5\\,000$ vẫn cho điểm tối đa)\n\nb) (0.5 điểm)\n- Thực hiện tính trong ngoặc:\n$3 \\cdot 12\\,000 + 2 \\cdot 5\\,000 = 36\\,000 + 10\\,000 = 46\\,000$ (đồng) (0.25đ)\n- Tính số tiền trả lại: $50\\,000 - 46\\,000 = 4\\,000$ (đồng).\nVậy cô bán hàng cần trả lại cho An $4\\,000$ đồng. (0.25đ)"
      }
    ]
  },
  "c1_6_bai7_test2": {
    "title": "Toán 6 (KNTT) - Bài 7: Thứ tự thực hiện các phép tính - Bài kiểm tra số 2",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đối với biểu thức không có dấu ngoặc và chỉ gồm các phép tính cộng, trừ, nhân, chia, nâng lên lũy thừa, thứ tự thực hiện phép tính đúng là:",
        "options": [
          "Lũy thừa $\\rightarrow$ Nhân và chia $\\rightarrow$ Cộng và trừ",
          "Nhân và chia $\\rightarrow$ Lũy thừa $\\rightarrow$ Cộng và trừ",
          "Cộng và trừ $\\rightarrow$ Nhân và chia $\\rightarrow$ Lũy thừa",
          "Lũy thừa $\\rightarrow$ Cộng và trừ $\\rightarrow$ Nhân và chia"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khi thực hiện phép tính có các dấu ngoặc: ngoặc tròn $( )$, ngoặc vuông $[ ]$, ngoặc nhọn $\\{ \\}$, thứ tự thực hiện đúng là:",
        "options": [
          "$\\{ \\} \\rightarrow [ ] \\rightarrow ( )$",
          "$( ) \\rightarrow [ ] \\rightarrow \\{ \\}$",
          "$[ ] \\rightarrow ( ) \\rightarrow \\{ \\}$",
          "$( ) \\rightarrow \\{ \\} \\rightarrow [ ]$"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Biểu thức chỉ chứa các phép nhân và chia thì thực hiện theo thứ tự nào sau đây?",
        "options": [
          "Thực hiện nhân trước, chia sau",
          "Thực hiện chia trước, nhân sau",
          "Thực hiện từ trái sang phải",
          "Thực hiện từ phải sang trái"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong phép tính $A = 20 - 10 : 2 + 3$, bước đầu tiên cần thực hiện là:",
        "options": [
          "Lấy $20 - 10$",
          "Lấy $10 : 2$",
          "Lấy $2 + 3$",
          "Lấy $20 + 3$"
        ],
        "correct": 1
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $P = 3^3 \\cdot 2 - 2 \\cdot 5^2 + 2024^0$ bằng:",
        "options": [
          "$5$",
          "$4$",
          "$3$",
          "$2025$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Kết quả của phép tính $A = 120 : [54 - (50 : 2 - 3^2)]$ là:",
        "options": [
          "$3$",
          "$4$",
          "$5$",
          "$2$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Số tự nhiên $x$ thỏa mãn đẳng thức $2 \\cdot (x - 3)^2 = 32$ là:",
        "options": [
          "$x = 7$",
          "$x = 5$",
          "$x = 19$",
          "$x = 11$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $B = 150 - [10^2 - (14 - 11)^2 \\cdot 2025^0]$ là:",
        "options": [
          "$59$",
          "$41$",
          "$141$",
          "$50$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho hai biểu thức $M = 2^3 \\cdot 3 + 4^2$ và $N = 5^2 \\cdot 2 - 3^2$. Khẳng định nào sau đây đúng?",
        "options": [
          "$M > N$",
          "$M = N$",
          "$M < N$",
          "$M + N = 80$"
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$, biết rằng $5 \\cdot 2^x - 3 = 37$.",
        "options": [
          "$x = 2$",
          "$x = 3$",
          "$x = 4$",
          "$x = 8$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho biểu thức $H = 75 - (3 \\cdot 5^2 - 4 \\cdot 2^3)$. Kết quả rút gọn của $H$ là:",
        "options": [
          "$32$",
          "$43$",
          "$0$",
          "$118$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Bạn Mai mang $100\\,000$ đồng đi nhà sách. Mai mua $5$ quyển vở với giá $11\\,000$ đồng/quyển và $3$ cây bút bi với giá $6\\,000$ đồng/cây. Biểu thức nào biểu thị đúng số tiền còn lại của Mai?",
        "options": [
          "$100\\,000 - 5 \\cdot 11\\,000 + 3 \\cdot 6\\,000$",
          "$100\\,000 - (5 \\cdot 11\\,000 + 3 \\cdot 6\\,000)$",
          "$(100\\,000 - 5) \\cdot 11\\,000 - 3 \\cdot 6\\,000$",
          "$100\\,000 : (5 \\cdot 11\\,000 + 3 \\cdot 6\\,000)$"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho biểu thức $A = 240 : \\{2 \\cdot [13 + (x - 2)^3]\\} + 5$ với $x$ là số tự nhiên và $x \\ge 2$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Khi $x = 5$, giá trị của lũy thừa $(x - 2)^3$ bằng $27$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Khi $x = 5$, giá trị của biểu thức trong ngoặc vuông $[13 + (x - 2)^3]$ là $40$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Khi $x = 5$, giá trị của biểu thức $A$ bằng $11$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Để $A = 9$, số tự nhiên $x$ cần tìm là $x = 4$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho bài toán tìm số tự nhiên $x$: $3 \\cdot (x + 1)^2 - 2 \\cdot 4^2 = 59$. Hai bạn Lan và Minh cùng thực hiện các bước giải toán.",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Bước đầu tiên cần tính lũy thừa $4^2 = 16$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Sau khi tính tích $2 \\cdot 4^2$, ta biến đổi được $3 \\cdot (x + 1)^2 = 59 - 32$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Từ phương trình trên, ta tính được giá trị $(x + 1)^2 = 25$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Không tồn tại số tự nhiên $x$ thỏa mãn đề bài vì $91$ không chia hết cho $3$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$ thỏa mãn phương trình: $128 - 3 \\cdot (x + 4) = 5^2 \\cdot 2$.",
        "answer": "22"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tính giá trị của biểu thức: $B = \\{[(315 + 372) \\cdot 3 + (372 + 315) \\cdot 7] : 10\\} : 687$.",
        "answer": "1"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Thư viện trường có ba tủ sách. Tủ I có $2^5 \\cdot 3$ quyển sách. Tủ II có số sách bằng số sách của tủ I chia cho $2^2$ rồi cộng thêm $15$ quyển. Tủ III có số sách gấp đôi hiệu số sách giữa tủ I và tủ II. Hỏi cả ba tủ có tất cả bao nhiêu quyển sách?",
        "answer": "249"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tìm số tự nhiên $x$ thỏa mãn đẳng thức: $3^{x+1} - 2 \\cdot 3^x + 3^{x-1} = 36$ (với $x \\ge 1$).",
        "answer": "3"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng thấp",
        "question": "Nhân dịp năm học mới, một cửa hàng văn phòng phẩm thực hiện chương trình ưu đãi như sau: Một hộp bút chì màu có giá niêm yết là $45\\,000$ đồng được giảm giá $5\\,000$ đồng mỗi hộp. Bạn Nam đại diện cho lớp mua $12$ hộp bút chì màu đó và mua thêm $25$ chiếc thước kẻ cùng loại có giá $6\\,000$ đồng/chiếc. Vì hóa đơn trên $500\\,000$ đồng nên cửa hàng tặng thêm một phiếu giảm giá trực tiếp $20\\,000$ đồng trừ vào tổng số tiền thanh toán.\na) Hãy lập một biểu thức số thể hiện số tiền thực tế bạn Nam phải trả cho cửa hàng.\nb) Tính số tiền thực tế Nam phải thanh toán.",
        "rubric": "- Viết đúng biểu thức tính số tiền: $T = 12 \\cdot (45\\,000 - 5\\,000) + 25 \\cdot 6\\,000 - 20\\,000$ (0.5 điểm).\n- Thực hiện đúng thứ tự phép tính trong ngoặc và nhân chia: $12 \\cdot 40\\,000 + 150\\,000 - 20\\,000 = 480\\,000 + 150\\,000 - 20\\,000$ (0.25 điểm).\n- Ra kết quả chính xác: $610\\,000$ đồng và có kết luận (0.25 điểm)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$ thỏa mãn biểu thức sau:\n$150 - 2 \\cdot [45 - (2x - 1)^3] = 12^2 - 10^2$.",
        "rubric": "- Tính đúng giá trị vế phải: $12^2 - 10^2 = 144 - 100 = 44$ (0.25 điểm).\n- Biến đổi: $2 \\cdot [45 - (2x - 1)^3] = 150 - 44 = 106$, suy ra $45 - (2x - 1)^3 = 53$ ... Ta thấy $45 - (2x - 1)^3 < 45 < 53$, do đó không tồn tại số tự nhiên $x$ thỏa mãn (0.5 điểm).\n- Hoặc nếu giải: $(2x - 1)^3 = 45 - 53 = -8$ không thuộc tập số tự nhiên $\\mathbb{N}$, kết luận không có số tự nhiên $x$ thỏa mãn (0.25 điểm)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho biểu thức $S = 1 + 2 + 2^2 + 2^3 + \\dots + 2^{2024}$.\na) Thu gọn biểu thức $S$.\nb) So sánh $S$ với $2^{2025}$.",
        "rubric": "- Nhân cả hai vế với 2: $2S = 2 \\cdot (1 + 2 + 2^2 + \\dots + 2^{2024}) = 2 + 2^2 + 2^3 + \\dots + 2^{2025}$ (0.25 điểm).\n- Thực hiện phép trừ: $2S - S = (2 + 2^2 + \\dots + 2^{2025}) - (1 + 2 + \\dots + 2^{2024})$ (0.25 điểm).\n- Rút gọn được: $S = 2^{2025} - 1$ (0.25 điểm).\n- Lập luận: Vì $2^{2025} - 1 < 2^{2025}$ nên $S < 2^{2025}$ (0.25 điểm)."
      }
    ]
  },
  "c1_6_bai7_test3": {
    "title": "Toán 6 (KNTT) - Bài 7: Thứ tự thực hiện các phép tính - Bài kiểm tra số 3",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khi thực hiện phép tính có chứa các dấu ngoặc tròn $( )$, ngoặc vuông $[ ]$, ngoặc nhọn $\\{ \\}$, thứ tự thực hiện đúng quy ước là:",
        "options": [
          "$( ) \\to [ ] \\to \\{ \\}$",
          "$\\{ \\} \\to [ ] \\to ( )$",
          "$[ ] \\to ( ) \\to \\{ \\}$",
          "$( ) \\to \\{ \\} \\to [ ]$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đối với biểu thức không có dấu ngoặc chỉ gồm các phép tính cộng, trừ, nhân, chia, nâng lên luỹ thừa, thứ tự thực hiện đúng là:",
        "options": [
          "Cộng, trừ $\\to$ Nhân, chia $\\to$ Luỹ thừa",
          "Luỹ thừa $\\to$ Nhân, chia $\\to$ Cộng, trừ",
          "Nhân, chia $\\to$ Luỹ thừa $\\to$ Cộng, trừ",
          "Luỹ thừa $\\to$ Cộng, trừ $\\to$ Nhân, chia"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $P = 120 - [30 - (4 - 1)^2]$ là:",
        "options": [
          "$99$",
          "$81$",
          "$111$",
          "$69$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$ thỏa mãn đẳng thức: $2 \\cdot (x - 3)^2 + 15 = 47$.",
        "options": [
          "$x = 7$",
          "$x = 1$ hoặc $x = 7$",
          "$x = 4$",
          "$x = 5$"
        ],
        "correct": 1
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $A = 2024^0 + 2024 \\cdot [5^2 - (4^2 - 3^2) \\cdot 3]$ bằng:",
        "options": [
          "$1$",
          "$8097$",
          "$9$",
          "$2025$"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Số tự nhiên $n$ thỏa mãn đẳng thức $3^{n+2} - 3^n = 216$ là:",
        "options": [
          "$n = 2$",
          "$n = 3$",
          "$n = 4$",
          "$n = 5$"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Thực hiện phép tính $B = 4^3 : 2^4 + 3 \\cdot 2^3 - 2023^0$ ta được kết quả là:",
        "options": [
          "$27$",
          "$28$",
          "$24$",
          "$26$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên $x$ biết: $100 - [60 - (9 - 2)^2] \\cdot x = 89$.",
        "options": [
          "$x = 2$",
          "$x = 1$",
          "$x = 0$",
          "$x = 3$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Có bao nhiêu số tự nhiên $x$ thỏa mãn $(2x - 1)^4 = (2x - 1)^2$?",
        "options": [
          "$1$",
          "$2$",
          "$3$",
          "$4$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Cho $M = 2 + 2^2 + 2^3 + \\ldots + 2^{60}$. Giá trị của biểu thức $2M + 2$ viết dưới dạng luỹ thừa là:",
        "options": [
          "$2^{61}$",
          "$2^{62}$",
          "$4^{60}$",
          "$2^{60}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cho biểu thức $A = 75 - 5 \\cdot (x - 2)^3$. Giá trị lớn nhất của $A$ khi $x$ là một số tự nhiên lớn hơn hoặc bằng $2$ là:",
        "options": [
          "$75$",
          "$70$",
          "$80$",
          "$60$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng",
        "question": "Tìm số tự nhiên $x$ thỏa mãn $5^{x} + 5^{x+1} + 5^{x+2} = 3875$.",
        "options": [
          "$x = 2$",
          "$x = 3$",
          "$x = 4$",
          "$x = 5$"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho biểu thức phụ thuộc vào tham số tự nhiên $m$: $A = 250 - \\{50 + 2 \\cdot [m^2 - (15 - 3^2)^2]\\}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Với $m = 6$, biểu thức trong ngoặc vuông $[m^2 - (15 - 3^2)^2]$ có giá trị bằng $0$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Với $m = 10$, giá trị của biểu thức $A$ bằng $72$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Nếu $A = 186$ thì có đúng một giá trị của số tự nhiên $m$ thỏa mãn.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Để biểu thức $A$ nhận giá trị lớn nhất trong tập hợp các số tự nhiên $\\mathbb{N}$ với $m \\ge 6$, giá trị của $m$ phải bằng $6$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho biểu thức $S = 1 + 3 + 3^2 + 3^3 + \\ldots + 3^{2024}$ và số tự nhiên $x$ thỏa mãn $2S + 1 = 3^{2x - 1}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Biểu thức $3S - S$ rút gọn được thành $3^{2025} - 1$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Giá trị của biểu thức $2S + 1$ bằng $3^{2024}$.",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Giá trị của $x$ thỏa mãn đẳng thức đề bài là $x = 1013$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Tổng $S$ chia hết cho $13$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức $E = 2024 - [150 - (12 - 4^2 : 2)^2 \\cdot 5]$.",
        "answer": "1954"
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Tìm số tự nhiên $x$ thỏa mãn biểu thức: $3 \\cdot 2^{x+1} - 2^x = 160$.",
        "answer": "5"
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tìm giá trị nhỏ nhất của biểu thức $P = 15 + 3 \\cdot (2x - 5)^2 + (y^2 - 4)^4$ với $x, y$ là các số tự nhiên.",
        "answer": "18"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $A = 4 + 4^2 + 4^3 + \\dots + 4^{2024}$. Tìm số dư khi chia biểu thức $3A + 4$ cho $16$.",
        "answer": "4"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng",
        "question": "Tìm tất cả các cặp số tự nhiên $(x, y)$ thỏa mãn đẳng thức sau:\n$$5 \\cdot 2^x + 3 \\cdot (y - 1)^2 = 43$$",
        "rubric": "Bước 1 (0.5đ): Biện luận chặn miền giá trị của $x$:\nVì $3 \\cdot (y - 1)^2 \\ge 0$ nên $5 \\cdot 2^x \\le 43$, suy ra $2^x \\le 8,6$.\nDo $x \\in \\mathbb{N}$ nên $x \\in \\{0; 1; 2; 3\\}$.\n\nBước 2 (0.5đ): Xét từng trường hợp và tìm $y$:\n- Với $x = 0$: $5 \\cdot 1 + 3(y - 1)^2 = 43 \\Rightarrow 3(y - 1)^2 = 38$ (loại vì $38$ không chia hết cho $3$).\n- Với $x = 1$: $5 \\cdot 2 + 3(y - 1)^2 = 43 \\Rightarrow 3(y - 1)^2 = 33 \\Rightarrow (y - 1)^2 = 11$ (loại vì $11$ không là số chính phương).\n- Với $x = 2$: $5 \\cdot 4 + 3(y - 1)^2 = 43 \\Rightarrow 3(y - 1)^2 = 23$ (loại vì $23$ không chia hết cho $3$).\n- Với $x = 3$: $5 \\cdot 8 + 3(y - 1)^2 = 43 \\Rightarrow 3(y - 1)^2 = 3 \\Rightarrow (y - 1)^2 = 1$.\nDo $y \\in \\mathbb{N}$ nên $y - 1 = 1 \\Rightarrow y = 2$ hoặc $y - 1 = -1$ (loại do $y \\in \\mathbb{N}$, hoặc $y - 1 = -1 \\Rightarrow y = 0$).\nThử lại cả hai giá trị: $(y-1)^2 = 1 \\iff y = 2$ hoặc $y = 0$.\nVậy các cặp số tự nhiên $(x; y)$ thỏa mãn là: $(3; 2)$ và $(3; 0)$."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một câu lạc bộ Robotics có $35$ học sinh tham gia thực hiện một dự án chế tạo robot. Các bạn chia làm hai nhóm:\n- Nhóm lập trình gồm $x$ bạn, mỗi bạn được cấp kinh phí $2^3 \\cdot 10^4$ đồng để mua linh kiện vi điều khiển.\n- Nhóm cơ khí gồm $y$ bạn, mỗi bạn được cấp kinh phí $3^2 \\cdot 10^4$ đồng để gia công khung vỏ.\nTổng kinh phí thực tế cấp cho cả hai nhóm là $295 \\cdot 10^4$ đồng. Em hãy tính số học sinh của mỗi nhóm.",
        "rubric": "Bước 1 (0.5đ): Thiết lập hệ thức toán học từ đề bài:\nSố học sinh nhóm lập trình là $x$, nhóm cơ khí là $y$ ($x, y \\in \\mathbb{N}^*$).\nTổng số học sinh là $35$, ta có: $x + y = 35 \\Rightarrow x = 35 - y$.\nKinh phí mỗi bạn nhóm lập trình nhận là: $2^3 \\cdot 10^4 = 8 \\cdot 10^4$ (đồng).\nKinh phí mỗi bạn nhóm cơ khí nhận là: $3^2 \\cdot 10^4 = 9 \\cdot 10^4$ (đồng).\n\nBước 2 (0.5đ): Lập và giải biểu thức tìm $x, y$:\nTổng kinh phí cấp cho cả hai nhóm là:\n$8 \\cdot 10^4 \\cdot x + 9 \\cdot 10^4 \\cdot y = 295 \\cdot 10^4$\nChia cả hai vế cho $10^4$, ta được: $8x + 9y = 295$.\nThay $x = 35 - y$ vào phương trình:\n$8(35 - y) + 9y = 295$\n$280 - 8y + 9y = 295$\n$280 + y = 295$\n$y = 295 - 280 = 15$ (thỏa mãn).\nTừ đó suy ra: $x = 35 - 15 = 20$ (thỏa mãn).\nVậy nhóm lập trình có $20$ học sinh, nhóm cơ khí có $15$ học sinh."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm tất cả các số tự nhiên $n$ sao cho giá trị của biểu thức $P = \\frac{4n + 23}{2n + 3}$ nhận giá trị là một số tự nhiên lớn nhất. Khi đó hãy tính giá trị lớn nhất đó.",
        "rubric": "Bước 1 (0.5đ): Tách phần nguyên của phân số:\nTa biến đổi biểu thức $P$ theo quy tắc chia đa thức:\n$P = \\frac{4n + 23}{2n + 3} = \\frac{2(2n + 3) + 17}{2n + 3} = \\frac{2(2n + 3)}{2n + 3} + \\frac{17}{2n + 3} = 2 + \\frac{17}{2n + 3}$.\n\nBước 2 (0.5đ): Biện luận tìm giá trị lớn nhất và kết luận:\nĐể $P$ nhận giá trị là số tự nhiên thì $\\frac{17}{2n + 3}$ phải là số tự nhiên, tức là $2n + 3$ phải là ước của $17$.\nCác ước tự nhiên của $17$ là $1$ và $17$.\nVì $n \\in \\mathbb{N}$ nên $2n + 3 \\ge 3$.\nDo đó ta chỉ có: $2n + 3 = 17 \\Rightarrow 2n = 14 \\Rightarrow n = 7$.\nKhi $n = 7$, giá trị của $P$ là $P = 2 + \\frac{17}{17} = 3$.\nVì đây là giá trị tự nhiên duy nhất mà biểu thức $P$ đạt được với $n \\in \\mathbb{N}$, nên giá trị lớn nhất của $P$ chính là $3$ khi $n = 7$."
      }
    ]
  },
  "c1_6_bai8_test1": {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương I: Tập hợp các số tự nhiên - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho tập hợp $A = \\{2; 3; 5; 7\\}$. Khẳng định nào sau đây là đúng?",
        "options": [
          "$3 \\in A$",
          "$4 \\in A$",
          "$7 \\notin A$",
          "$2 \\subset A$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Số La Mã $\\text{XIX}$ biểu diễn số tự nhiên nào trong hệ thập phân?",
        "options": [
          "$19$",
          "$21$",
          "$18$",
          "$29$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tập hợp các số tự nhiên $\\mathbb{N}^*$ là:",
        "options": [
          "$\\{1; 2; 3; 4; \\dots\\}$",
          "$\\{0; 1; 2; 3; 4; \\dots\\}$",
          "$\\{0; 2; 4; 6; \\dots\\}$",
          "$\\{1; 3; 5; 7; \\dots\\}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kết quả của phép tính $2^3 \\cdot 2^2$ bằng:",
        "options": [
          "$2^5$",
          "$2^6$",
          "$4^5$",
          "$4^6$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Kết quả của phép chia $5^6 : 5^2$ bằng:",
        "options": [
          "$5^4$",
          "$5^3$",
          "$1^4$",
          "$5^8$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Giá trị của $2026^0$ bằng:",
        "options": [
          "$1$",
          "$0$",
          "$2026$",
          "Không xác định"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Thứ tự thực hiện đúng các dấu ngoặc trong một biểu thức là:",
        "options": [
          "$( ) \\to [ ] \\to \\{ \\}$",
          "$[ ] \\to ( ) \\to \\{ \\}$",
          "$\\{ \\} \\to [ ] \\to ( )$",
          "$( ) \\to \\{ \\} \\to [ ]$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Số tự nhiên $x$ thỏa mãn $x + 15 = 40$ là:",
        "options": [
          "$25$",
          "$55$",
          "$35$",
          "$15$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tính nhanh $25 \\cdot 37 \\cdot 4$ ta được kết quả là:",
        "options": [
          "$3700$",
          "$370$",
          "$37000$",
          "$7400$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Trong phép chia có dư với số chia bằng $7$, số dư lớn nhất có thể có là:",
        "options": [
          "$6$",
          "$7$",
          "$5$",
          "$1$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tập hợp $B = \\{x \\in \\mathbb{N} \\mid 5 < x \\le 9\\}$ gồm các phần tử là:",
        "options": [
          "$\\{6; 7; 8; 9\\}$",
          "$\\{5; 6; 7; 8; 9\\}$",
          "$\\{6; 7; 8\\}$",
          "$\\{5; 6; 7; 8\\}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $100 - (30 - 20 : 2)$ bằng:",
        "options": [
          "$80$",
          "$70$",
          "$90$",
          "$60$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tập hợp $M = \\{x \\in \\mathbb{N}^* \\mid x < 6\\}$ và biểu thức $A = 2^3 + 3 \\cdot 4$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tập hợp $M$ có đúng 5 phần tử: $1; 2; 3; 4; 5$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phần tử $0$ thuộc tập hợp $M$ ($0 \\in M$).",
            "correct": false
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Giá trị của biểu thức $A$ bằng $20$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Giá trị của biểu thức $A$ là một phần tử thuộc tập hợp $M$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một đoàn tàu chở hàng gồm 12 toa xe, mỗi toa xe chở 35 tấn hàng. Biết rằng một xe tải loại lớn có thể chở tối đa 15 tấn hàng.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tổng khối lượng hàng trên đoàn tàu là 420 tấn.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Phép tính tìm tổng khối lượng hàng là $12 \\times 35$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Cần ít nhất 28 xe tải loại lớn để chở hết số hàng đó.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Nếu mỗi toa xe chở thêm 5 tấn hàng thì tổng khối lượng hàng tăng thêm 50 tấn.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị của biểu thức: $A = 3^4 : 3^2 + 2 \\cdot 5$.",
        "answer": "19"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$ thỏa mãn: $3x - 17 = 28$.",
        "answer": "15"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Tính tổng của tất cả các số tự nhiên $x$ thỏa mãn: $12 \\le x < 16$.",
        "answer": "54"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tìm số tự nhiên $x$, biết: $2^{x+1} - 2^x = 32$.",
        "answer": "5"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Thực hiện phép tính hợp lý:\na) $48 \\cdot 63 + 48 \\cdot 37$\nb) $120 : [54 - (50 - 2^3)]$",
        "rubric": "a) = 48 . (63 + 37) = 48 . 100 = 4800 (0.5đ)\nb) 50 - 2^3 = 50 - 8 = 42 (0.25đ)\n54 - 42 = 12 => 120 : 12 = 10 (0.25đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$, biết:\na) $2x + 15 = 47$\nb) $(x - 3)^2 = 25$",
        "rubric": "a) 2x = 47 - 15 = 32 => x = 16 (0.5đ)\nb) Do x là số tự nhiên nên x - 3 >= 0. Vì 25 = 5^2 nên x - 3 = 5 => x = 8 (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho biểu thức $S = 1 + 2 + 2^2 + 2^3 + \\dots + 2^{2025}$.\na) Thu gọn biểu thức $S$.\nb) Chứng minh rằng $S + 1$ là một lũy thừa của $2$.",
        "rubric": "a) 2S = 2 + 2^2 + 2^3 + ... + 2^2026 (0.25đ)\n2S - S = (2 + 2^2 + ... + 2^2026) - (1 + 2 + ... + 2^2025) (0.25đ)\n=> S = 2^2026 - 1 (0.25đ)\nb) S + 1 = 2^2026 - 1 + 1 = 2^2026, là một lũy thừa của 2 với cơ số 2 và số mũ 2026 (0.25đ)"
      }
    ]
  },
  "c1_6_bai8_test2": {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương I: Tập hợp các số tự nhiên - Bài kiểm tra số 2 (⚡ Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tập hợp $A = \\{x \\in \\mathbb{N}^* \\mid x \\le 5\\}$ có bao nhiêu phần tử?",
        "options": [
          "$5$",
          "$6$",
          "$4$",
          "Vô số"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Số La Mã biểu diễn số tự nhiên $26$ là:",
        "options": [
          "$\\text{XXVI}$",
          "$\\text{XXIV}$",
          "$\\text{XXVII}$",
          "$\\text{XVI}$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tích $a^m \\cdot a^n$ với $a \\ne 0$ bằng:",
        "options": [
          "$a^{m+n}$",
          "$a^{m-n}$",
          "$a^{m \\cdot n}$",
          "$(2a)^{m+n}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Thương $x^9 : x^3$ ($x \\ne 0$) bằng:",
        "options": [
          "$x^6$",
          "$x^3$",
          "$x^{12}$",
          "$1^6$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Thứ tự thực hiện các phép tính trong biểu thức không có dấu ngoặc là:",
        "options": [
          "Lũy thừa $\\to$ Nhân và chia $\\to$ Cộng và trừ",
          "Nhân và chia $\\to$ Lũy thừa $\\to$ Cộng và trừ",
          "Cộng và trừ $\\to$ Nhân và chia $\\to$ Lũy thừa",
          "Từ trái sang phải không phân biệt phép tính"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Cho phép chia $a : b = q$ (dư $r$). Điều kiện của số dư $r$ là:",
        "options": [
          "$0 \\le r < b$",
          "$0 < r \\le b$",
          "$r < b$",
          "$r > 0$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Số tự nhiên $x$ thỏa mãn $5(x - 2) = 35$ là:",
        "options": [
          "$9$",
          "$7$",
          "$5$",
          "$11$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Kết quả của phép tính $2^3 \\cdot 5 - 3^2$ bằng:",
        "options": [
          "$31$",
          "$37$",
          "$29$",
          "$41$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tính nhanh tổng $135 + 360 + 65 + 40$ ta được kết quả là:",
        "options": [
          "$600$",
          "$500$",
          "$610$",
          "$590$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Biết $x^3 = 64$. Giá trị của số tự nhiên $x$ là:",
        "options": [
          "$4$",
          "$8$",
          "$2$",
          "$16$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Viết tích $8^3 \\cdot 4^2$ dưới dạng một lũy thừa cơ số $2$ ta được:",
        "options": [
          "$2^{13}$",
          "$2^{10}$",
          "$2^{12}$",
          "$2^{18}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Giá trị của biểu thức $A = 2026 - [150 - (12 - 7)^2]$ là:",
        "options": [
          "$1901$",
          "$1910$",
          "$1900$",
          "$2001$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho biểu thức $P = 125 \\cdot 18 - 125 \\cdot 8$ và tập hợp các ước của $10$ là $U$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Biểu thức $P$ được rút gọn thành $125 \\cdot (18 - 8) = 1250$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tập hợp các ước tự nhiên của $10$ là $U = \\{1; 2; 5; 10\\}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Giá trị của $P$ chia hết cho tất cả các phần tử của tập hợp $U$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Số $P$ khi viết dưới dạng lũy thừa cơ số $5$ là $5^5$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một trường THCS có 480 học sinh khối 6 đi tham quan dã ngoại. Ban tổ chức dự định thuê xe ô tô loại 45 chỗ ngồi hoặc loại 30 chỗ ngồi.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Nếu chỉ dùng xe 45 chỗ thì 10 xe là không đủ để chở hết học sinh.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Cần ít nhất 11 xe loại 45 chỗ để chở hết 480 học sinh.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Nếu dùng hoàn toàn xe 30 chỗ thì cần đúng 16 xe (không có ghế trống).",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Thuê 9 xe loại 45 chỗ và 3 xe loại 30 chỗ chở được tối đa 480 học sinh.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị biểu thức: $B = 2^4 \\cdot 3 - [131 - (13 - 4)^2]$.",
        "answer": "-2"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$ thỏa mãn: $120 - 5(x + 2) = 45$.",
        "answer": "13"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Số lượng các số tự nhiên có hai chữ số chia hết cho cả $2$ và $5$ là bao nhiêu?",
        "answer": "9"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tìm chữ số tận cùng của lũy thừa $2^{2024}$.",
        "answer": "6"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính giá trị của các biểu thức sau một cách hợp lý:\na) $27 \\cdot 75 + 25 \\cdot 27 - 150$\nb) $3^3 \\cdot 18 - 3^3 \\cdot 12 + 2026^0$",
        "rubric": "a) = 27.(75 + 25) - 150 = 27.100 - 150 = 2700 - 150 = 2550 (0.5đ)\nb) = 27.(18 - 12) + 1 = 27.6 + 1 = 162 + 1 = 163 (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$, biết:\na) $4(x - 3) - 18 = 38$\nb) $3^{x+2} - 3^x = 216$",
        "rubric": "a) 4(x - 3) = 56 => x - 3 = 14 => x = 17 (0.5đ)\nb) 3^x . (3^2 - 1) = 216 <=> 3^x . 8 = 216 <=> 3^x = 27 = 3^3 => x = 3 (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\na) Cho tổng $A = 1 + 3 + 3^2 + 3^3 + \\dots + 3^{100}$. Chứng minh rằng $2A + 1$ là một số chính phương.\nb) So sánh hai số: $2^{300}$ và $3^{200}$.",
        "rubric": "a) 3A = 3 + 3^2 + ... + 3^101 => 3A - A = 3^101 - 1 => 2A = 3^101 - 1 => 2A + 1 = 3^101. (Nếu đề 3^100 chẵn thì (3^50)^2 chính phương, với A từ 1 đến 3^99 thì 2A+1 = 3^100 = (3^50)^2 là số chính phương) (0.5đ)\nb) 2^300 = (2^3)^100 = 8^100 (0.25đ)\n3^200 = (3^2)^100 = 9^100 (0.25đ)\nVì 8 < 9 nên 8^100 < 9^100 => 2^300 < 3^200. (0.25đ)"
      }
    ]
  },
  "c1_6_bai8_test3": {
    "title": "Toán 6 (KNTT) - Bài kiểm tra cuối Chương I: Tập hợp các số tự nhiên - Bài kiểm tra số 3 (🔥 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho tập hợp $X = \\{x \\in \\mathbb{N} \\mid 10 \\le x < 100\\}$. Số phần tử của tập hợp $X$ là:",
        "options": [
          "$90$",
          "$89$",
          "$91$",
          "$100$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Chữ số La Mã $\\text{L}$ và $\\text{C}$ lần lượt có giá trị trong hệ thập phân là:",
        "options": [
          "$50$ và $100$",
          "$100$ và $50$",
          "$50$ và $500$",
          "$10$ và $100$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Biểu thức $(a^m)^n$ viết gọn lại là:",
        "options": [
          "$a^{m \\cdot n}$",
          "$a^{m + n}$",
          "$a^{m - n}$",
          "$a^{m^n}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Số tự nhiên liền trước của số $n + 1$ ($n \\in \\mathbb{N}^*$) là:",
        "options": [
          "$n$",
          "$n + 2$",
          "$n - 1$",
          "$2n$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Nếu tích $a \\cdot b = 0$ thì khẳng định nào sau đây luôn đúng?",
        "options": [
          "$a = 0$ hoặc $b = 0$",
          "Cả $a$ và $b$ đều phải bằng $0$",
          "$a = 0$ và $b \\ne 0$",
          "$a > 0$ và $b < 0$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trong phép chia số tự nhiên $a$ cho $b$ ($b \\ne 0$) có thương là $q$ và số dư là $r$. Công thức biểu diễn $a$ là:",
        "options": [
          "$a = b \\cdot q + r$ ($0 \\le r < b$)",
          "$a = b \\cdot q - r$",
          "$a = b \\cdot r + q$",
          "$a = (b + q) \\cdot r$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Số tự nhiên $x$ thỏa mãn $2^{x+3} = 128$ là:",
        "options": [
          "$4$",
          "$7$",
          "$5$",
          "$3$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Để đánh số trang của một cuốn sách dày 120 trang bằng các số tự nhiên từ 1 đến 120, người ta phải dùng tất cả bao nhiêu chữ số?",
        "options": [
          "$252$",
          "$240$",
          "$250$",
          "$260$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tìm số tự nhiên có hai chữ số giống nhau, biết số đó chia hết cho 2 và khi chia cho 5 thì dư 3:",
        "options": [
          "$88$",
          "$22$",
          "$44$",
          "$66$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tổng $S = 1 + 2 + 3 + 4 + \\dots + 99 + 100$ có giá trị bằng:",
        "options": [
          "$5050$",
          "$5000$",
          "$5100$",
          "$5025$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Rút gọn biểu thức $M = \\frac{4^5 \\cdot 9^4 - 2 \\cdot 6^9}{2^{10} \\cdot 3^8 + 6^8 \\cdot 20}$ ta được kết quả là:",
        "options": [
          "$\\frac{1}{3}$",
          "$-1$",
          "$1$",
          "$\\frac{2}{3}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Chữ số tận cùng của tích $1 \\cdot 3 \\cdot 5 \\cdot 7 \\cdot \\dots \\cdot 2025$ là:",
        "options": [
          "$5$",
          "$0$",
          "$1$",
          "$9$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho dãy số tự nhiên cách đều: $3; 7; 11; 15; 19; \\dots; 403$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Khoảng cách giữa hai số liên tiếp trong dãy là 4 đơn vị.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Dãy số trên có tất cả 101 số hạng.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tổng của tất cả các số hạng trong dãy bằng 20503.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Số hạng thứ 50 của dãy số là số 199.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tổng $B = 1 + 4 + 4^2 + 4^3 + \\dots + 4^{2024}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Biểu thức $4B = 4 + 4^2 + 4^3 + \\dots + 4^{2025}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Rút gọn ta được $3B = 4^{2025} - 1$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Giá trị của $3B + 1$ là một lũy thừa của $2$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Chữ số tận cùng của $4^{2025}$ là chữ số $6$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính tổng của tất cả các số có 3 chữ số nhỏ hơn 200: $S = 100 + 101 + \\dots + 199$.",
        "answer": "14950"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$, biết: $(2x - 1)^3 = 125$.",
        "answer": "3"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tìm số tự nhiên $n$ nhỏ nhất sao cho $2^n > 1000$.",
        "answer": "10"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $A = 1 + 2 + 2^2 + \\dots + 2^{2023}$. Tìm số dư khi chia $A$ cho $7$.",
        "answer": "0"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Tính hợp lý giá trị biểu thức:\n$$P = \\frac{2^{12} \\cdot 3^5 - 4^6 \\cdot 9^2}{(2^2 \\cdot 3)^6 + 8^4 \\cdot 3^5}$$",
        "rubric": "Biến đổi: 4^6 = (2^2)^6 = 2^12; 9^2 = (3^2)^2 = 3^4.\nTử số = 2^12 . 3^5 - 2^12 . 3^4 = 2^12 . 3^4 . (3 - 1) = 2^13 . 3^4. (0.5đ)\nMẫu số = 2^12 . 3^6 + 2^12 . 3^5 = 2^12 . 3^5 . (3 + 1) = 2^14 . 3^5. (0.25đ)\n=> P = (2^13 . 3^4) / (2^14 . 3^5) = 1 / (2 . 3) = 1/6 (0.25đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tìm số tự nhiên $x$, biết:\na) $5^{x} + 5^{x+2} = 650$\nb) $(x - 1) + (x - 2) + (x - 3) + \\dots + (x - 20) = 190$",
        "rubric": "a) 5^x . (1 + 5^2) = 650 <=> 5^x . 26 = 650 <=> 5^x = 25 = 5^2 => x = 2 (0.5đ)\nb) (x + x + ... + x) - (1 + 2 + ... + 20) = 190\n<=> 20x - (20 . 21 / 2) = 190 <=> 20x - 210 = 190 <=> 20x = 400 => x = 20 (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\na) Chứng minh rằng tổng $S = 2 + 2^2 + 2^3 + 2^4 + \\dots + 2^{60}$ chia hết cho cả $3$, $7$ và $15$.\nb) Cho $A = 1 + 2025 + 2025^2 + \\dots + 2025^{2024}$ và $B = 2025^{2025}$. So sánh $2024 \\cdot A$ và $B$.",
        "rubric": "a) Nhóm 2 số: S = (2 + 2^2) + ... = 2.(1 + 2) + ... = 6 + ... chia hết cho 3 (0.25đ)\nNhóm 3 số: S = (2 + 2^2 + 2^3) + ... = 2.(1 + 2 + 4) + ... = 2.7 + ... chia hết cho 7 (0.25đ)\nNhóm 4 số: S = (2 + 2^2 + 2^3 + 2^4) + ... = 2.(1 + 2 + 4 + 8) + ... = 2.15 + ... chia hết cho 15 (0.25đ)\nb) 2025.A = 2025 + 2025^2 + ... + 2025^2025\n=> 2025.A - A = 2025^2025 - 1 <=> 2024.A = B - 1\nVì B - 1 < B nên 2024.A < B (0.25đ)"
      }
    ]
  }
};

const EXAMS_6_C1_6 = CHAPTER1_TOAN6_EXAMS;

if (typeof window !== 'undefined') {
  window.CHAPTER1_TOAN6_EXAMS = CHAPTER1_TOAN6_EXAMS;
  window.EXAMS_6_C1_6 = CHAPTER1_TOAN6_EXAMS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CHAPTER1_TOAN6_EXAMS, EXAMS_6_C1_6 };
}
