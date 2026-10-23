// ==============================================================================
// NGÂN HÀNG ĐỀ THI TOÁN 8 (KNTT) - Bài 14: Hình thoi và hình vuông
// Bao gồm 3 đề phân hóa: Đề 1 (Cơ bản) < Đề 2 (Khá) < Đề 3 (Nâng cao)
// Chuẩn ma trận 10 điểm: 12 TN + 2 Đ/S + 4 TLN + 3 Tự luận
// ==============================================================================

const BAI_5_TOAN8_EXAMS = {
  "c3_8_bai5_test1": {
    "title": "Toán 8 (KNTT) - Bài 14: Hình thoi và hình vuông - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hình thoi là tứ giác có:",
        "options": [
          "Bốn cạnh bằng nhau",
          "Bốn góc vuông",
          "Hai đường chéo bằng nhau",
          "Hai cạnh kề vuông góc"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong hình thoi, khẳng định nào sau đây là sai?",
        "options": [
          "Hai đường chéo luôn bằng nhau",
          "Hai đường chéo vuông góc với nhau",
          "Hai đường chéo là các đường phân giác của các góc",
          "Bốn cạnh bằng nhau"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hình vuông là tứ giác có:",
        "options": [
          "Bốn góc vuông và bốn cạnh bằng nhau",
          "Bốn góc vuông",
          "Bốn cạnh bằng nhau",
          "Hai đường chéo vuông góc"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Diện tích của hình thoi có độ dài hai đường chéo $d_1$ và $d_2$ được tính theo công thức:",
        "options": [
          "$S = \\frac{1}{2} d_1 d_2$",
          "$S = d_1 d_2$",
          "$S = 2 d_1 d_2$",
          "$S = \\frac{1}{4} d_1 d_2$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Hình chữ nhật có thêm điều kiện nào sau đây thì trở thành hình vuông?",
        "options": [
          "Hai đường chéo vuông góc với nhau",
          "Hai đường chéo bằng nhau",
          "Có hai cạnh đối bằng nhau",
          "Có một góc vuông"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hình thoi có thêm điều kiện nào sau đây thì trở thành hình vuông?",
        "options": [
          "Có một góc vuông",
          "Hai đường chéo vuông góc",
          "Bốn cạnh bằng nhau",
          "Các góc đối bằng nhau"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho hình thoi $ABCD$ có $\\widehat{A} = 50^\\circ$. Số đo góc $B$ bằng:",
        "options": [
          "$130^\\circ$",
          "$50^\\circ$",
          "$90^\\circ$",
          "$100^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một hình thoi có độ dài hai đường chéo lần lượt là $6\\text{ cm}$ và $8\\text{ cm}$. Diện tích của hình thoi là:",
        "options": [
          "$24\\text{ cm}^2$",
          "$48\\text{ cm}^2$",
          "$14\\text{ cm}^2$",
          "$28\\text{ cm}^2$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một hình thoi có độ dài hai đường chéo là $6\\text{ cm}$ và $8\\text{ cm}$. Chu vi của hình thoi đó bằng:",
        "options": [
          "$20\\text{ cm}$",
          "$24\\text{ cm}$",
          "$28\\text{ cm}$",
          "$16\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Hình vuông $ABCD$ có cạnh bằng $5\\text{ cm}$. Độ dài đường chéo $AC$ bằng:",
        "options": [
          "$5\\sqrt{2}\\text{ cm}$",
          "$10\\text{ cm}$",
          "$25\\text{ cm}$",
          "$7\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ cân tại $A$. Gọi $M$ là trung điểm $BC$. Lấy $D$ đối xứng với $A$ qua $M$. Tứ giác $ABDC$ là:",
        "options": [
          "Hình thoi",
          "Hình vuông",
          "Hình chữ nhật",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hình vuông có bao nhiêu trục đối xứng?",
        "options": [
          "$4$",
          "$2$",
          "$1$",
          "$8$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình thoi $ABCD$ có hai đường chéo cắt nhau tại $O$. Biết $AC = 12\\text{ cm}, BD = 16\\text{ cm}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Hai đường chéo $AC$ và $BD$ vuông góc với nhau tại trung điểm $O$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $OA = 6\\text{ cm}$ và $OB = 8\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Độ dài cạnh của hình thoi $AB = 10\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Diện tích của hình thoi bằng $192\\text{ cm}^2$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một mảnh gạch men trang trí có dạng hình vuông $ABCD$ với chu vi bằng $40\\text{ cm}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Độ dài mỗi cạnh của viên gạch bằng $10\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Diện tích của viên gạch men bằng $100\\text{ cm}^2$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Độ dài đường chéo của viên gạch là $10\\sqrt{2}\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Đường chéo chia hình vuông thành hai tam giác đều.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thoi $ABCD$ có $\\widehat{A} = 60^\\circ$ và $AB = 7\\text{ cm}$. Tính độ dài đường chéo $BD$ (theo cm).",
        "answer": "7"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Hình thoi $ABCD$ có chu vi $52\\text{ cm}$ và đường chéo $AC = 24\\text{ cm}$. Tính độ dài đường chéo $BD$ (theo cm).",
        "answer": "10"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Hình vuông có diện tích bằng $72\\text{ cm}^2$. Tính độ dài đường chéo của hình vuông đó (theo cm).",
        "answer": "12"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình thoi $ABCD$ có hai đường chéo $AC = 10\\text{ cm}, BD = 24\\text{ cm}$. Tính khoảng cách giữa hai cạnh đối $AB$ và $CD$ (theo cm, viết dưới dạng phân số tối giản $a/b$).",
        "answer": "120/13"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thoi $ABCD$. Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$.\na) Chứng minh rằng $AC \\perp BD$ và $AC$ là phân giác của góc $\\widehat{BAD}$.\nb) Biết $\\widehat{B} = 120^\\circ$ và $BD = 6\\text{ cm}$, tính độ dài cạnh $AB$ và độ dài đường chéo $AC$.",
        "rubric": "a) Theo tính chất hình thoi, hai đường chéo vuông góc với nhau và là các đường phân giác của các góc (0.5đ)\nb) Góc B = 120° => góc A = 60°. Tam giác ABD cân tại A có góc A = 60° nên là tam giác đều => AB = BD = 6 cm. OA = AB . căn(3)/2 = 3.căn(3) cm => AC = 2OA = 6.căn(3) cm (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ vuông cân tại $A$. Điểm $M$ thuộc cạnh huyền $BC$. Kẻ $MD \\perp AB$ tại $D$ và $ME \\perp AC$ tại $E$.\na) Tứ giác $ADME$ là hình gì?\nb) Điểm $M$ ở vị trí nào trên cạnh $BC$ thì tứ giác $ADME$ là hình vuông?",
        "rubric": "a) Tứ giác ADME có 3 góc vuông nên là hình chữ nhật (0.5đ)\nb) Hình chữ nhật ADME là hình vuông <=> hai cạnh kề bằng nhau AD = AE <=> tam giác ADM = tam giác AEM <=> AM là phân giác góc A. Trong tam giác vuông cân ABC, phân giác góc A đồng thời là đường cao, trung tuyến => M là trung điểm của BC (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình vuông $ABCD$. Trên các cạnh $AB, BC, CD, DA$ lần lượt lấy các điểm $M, N, P, Q$ sao cho $AM = BN = CP = DQ$.\na) Chứng minh tứ giác $MNPQ$ là hình vuông.\nb) Cho $AB = 8\\text{ cm}$. Tìm vị trí của $M$ trên $AB$ để diện tích tứ giác $MNPQ$ đạt giá trị nhỏ nhất.",
        "rubric": "a) Tam giác AQM = tam giác BMN = tam giác CPN = tam giác DQP (c-g-c) => MN = NP = PQ = QM => MNPQ là hình thoi. Lại có góc AMQ + góc BMN = 90° => góc NMQ = 90° => MNPQ là hình vuông (0.5đ)\nb) Đặt AM = x (0 <= x <= 8). MB = 8 - x. MN² = x² + (8 - x)² = 2x² - 16x + 64 = 2(x - 4)² + 32 >= 32. Dấu '=' xảy ra khi x = 4. Vậy khi M là trung điểm AB thì diện tích MNPQ nhỏ nhất bằng 32 cm² (0.5đ)"
      }
    ]
  },
  "c3_8_bai5_test2": {
    "title": "Toán 8 (KNTT) - Bài 14: Hình thoi và hình vuông - Bài kiểm tra số 2 (⚡ Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hình bình hành có hai đường chéo vuông góc với nhau là:",
        "options": [
          "Hình thoi",
          "Hình chữ nhật",
          "Hình thang cân",
          "Hình vuông"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hình chữ nhật có hai đường chéo vuông góc với nhau là:",
        "options": [
          "Hình vuông",
          "Hình thoi",
          "Hình bình hành",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hình thoi có hai đường chéo bằng nhau là:",
        "options": [
          "Hình vuông",
          "Hình chữ nhật",
          "Hình bình hành",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tứ giác có các đỉnh là trung điểm bốn cạnh của một hình chữ nhật là:",
        "options": [
          "Hình thoi",
          "Hình vuông",
          "Hình chữ nhật",
          "Hình bình hành không vuông"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tứ giác có các đỉnh là trung điểm bốn cạnh của một hình thoi là:",
        "options": [
          "Hình chữ nhật",
          "Hình vuông",
          "Hình thoi",
          "Hình thang"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Đường chéo của hình vuông tạo với các cạnh một góc bằng:",
        "options": [
          "$45^\\circ$",
          "$30^\\circ$",
          "$60^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho hình thoi $ABCD$ có cạnh bằng $10\\text{ cm}$ và một đường chéo dài $12\\text{ cm}$. Độ dài đường chéo còn lại là:",
        "options": [
          "$16\\text{ cm}$",
          "$8\\text{ cm}$",
          "$14\\text{ cm}$",
          "$20\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hình vuông có đường chéo dài $10\\text{ cm}$. Diện tích của hình vuông đó bằng:",
        "options": [
          "$50\\text{ cm}^2$",
          "$100\\text{ cm}^2$",
          "$25\\text{ cm}^2$",
          "$75\\text{ cm}^2$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông cân tại $A$. Dựng ra phía ngoài tam giác các hình vuông $ABDE$ và $ACFG$. Tứ giác $BDEC$ có quan hệ gì với $BCGF$?",
        "options": [
          "Có diện tích bằng nhau",
          "Có chu vi bằng nhau",
          "Là các hình vuông bằng nhau",
          "Cả 3 khẳng định trên"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Hình thoi $ABCD$ có góc $\\widehat{A} = 120^\\circ$ và cạnh $a = 4\\text{ cm}$. Diện tích hình thoi bằng:",
        "options": [
          "$8\\sqrt{3}\\text{ cm}^2$",
          "$16\\sqrt{3}\\text{ cm}^2$",
          "$8\\text{ cm}^2$",
          "$16\\text{ cm}^2$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$. Tia phân giác góc $A$ cắt $BC$ tại $E$, tia phân giác góc $B$ cắt $AD$ tại $F$. Tứ giác $ABEF$ là:",
        "options": [
          "Hình thoi",
          "Hình vuông",
          "Hình chữ nhật",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một hình vuông có cạnh $a$. Nối trung điểm các cạnh liên tiếp của nó ta được hình vuông mới. Tỉ số diện tích của hình vuông mới so với hình vuông ban đầu là:",
        "options": [
          "$\\frac{1}{2}$",
          "$\\frac{1}{4}$",
          "$\\frac{1}{3}$",
          "$\\frac{2}{3}$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ cân tại $A$. Gọi $M$ là trung điểm cạnh đáy $BC$. Qua $M$ kẻ đường thẳng song song với $AC$ cắt $AB$ tại $E$, kẻ đường thẳng song song với $AB$ cắt $AC$ tại $F$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $AEMF$ là một hình bình hành vì có các cạnh đối song song.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $AM$ là tia phân giác của góc $\\widehat{EAF}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Hình bình hành $AEMF$ là hình thoi vì có đường chéo $AM$ là tia phân giác.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Để $AEMF$ là hình vuông thì tam giác $ABC$ phải là tam giác đều.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình vuông $ABCD$ có cạnh bằng $6\\text{ cm}$. Gọi $E, F$ lần lượt là trung điểm của $AB$ và $BC$. Đoạn thẳng $CE$ cắt $DF$ tại $M$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Hai tam giác vuông $CBE$ và $DCF$ bằng nhau.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Hai đường thẳng $CE$ và $DF$ vuông góc với nhau tại $M$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tam giác $AMD$ là tam giác cân tại $M$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Độ dài đoạn thẳng $CE = 3\\sqrt{5}\\text{ cm}$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thoi $ABCD$ có chu vi bằng $40\\text{ cm}$ và một góc bằng $60^\\circ$. Tính độ dài đường chéo lớn của hình thoi (theo cm, viết dạng $a\\sqrt{3}$ với $a$ là số nguyên).",
        "answer": "10"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Một hình vuông có diện tích bằng $98\\text{ cm}^2$. Tính độ dài cạnh của hình vuông (theo cm, viết giá trị $a^2$).",
        "answer": "98"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho hình thoi $ABCD$ có độ dài hai đường chéo $AC = 16\\text{ cm}, BD = 12\\text{ cm}$. Tính độ dài đường cao của hình thoi (theo cm).",
        "answer": "9.6"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình vuông $ABCD$ có cạnh $8\\text{ cm}$. Lấy điểm $E$ trên cạnh $BC$ sao cho $BE = 2\\text{ cm}$. Đường thẳng qua $A$ vuông góc với $AE$ cắt đường thẳng $CD$ tại $F$. Tính độ dài đoạn thẳng $AF$ (theo cm, viết giá trị $AF^2$).",
        "answer": "68"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có ba góc nhọn. Vẽ ra phía ngoài tam giác các hình vuông $ABDE$ và $ACFG$.\na) Chứng minh $CD = BF$.\nb) Chứng minh $CD \\perp BF$.",
        "rubric": "a) Xét tam giác ADC và tam giác ABF: AD = AB, AC = AF, góc DAC = 90° + góc A = góc BAF => tam giác ADC = tam giác ABF (c-g-c) => CD = BF (0.5đ)\nb) Gọi giao điểm của CD và BF là I, CD và AB là K. Tam giác AKD vuông tại A... Suy ra góc KIB = 90° => CD vuông góc BF (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình vuông $ABCD$. Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$. Một góc vuông $xOy$ quay quanh đỉnh $O$, các tia $Ox, Oy$ lần lượt cắt các cạnh $AB$ và $BC$ tại $M$ và $N$.\na) Chứng minh tam giác $OAM$ bằng tam giác $OBN$.\nb) Chứng minh diện tích tứ giác $OMBN$ không đổi khi góc $xOy$ quay quanh $O$.",
        "rubric": "a) Ta có OA = OB (tính chất hình vuông), góc OAM = góc OBN = 45°. Góc AOM = 90° - góc MOB = góc BON => tam giác OAM = tam giác OBN (g-c-g) (0.5đ)\nb) S(OMBN) = S(OBM) + S(OBN) = S(OBM) + S(OAM) = S(OAB) = 1/4 S(ABCD) (không đổi) (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình vuông $ABCD$ cạnh $a$. Lấy điểm $E$ tùy ý trên cạnh $BC$ ($E$ khác $B, C$). Tia $AE$ cắt đường thẳng $CD$ tại $F$. Kẻ đường thẳng qua $A$ vuông góc với $AE$ cắt đường thẳng $CD$ tại $K$.\na) Chứng minh tam giác $AKF$ vuông tại $A$ và $AK = AE$.\nb) Chứng minh rằng biểu thức $\\frac{1}{AE^2} + \\frac{1}{AF^2}$ không đổi khi điểm $E$ di chuyển trên cạnh $BC$.",
        "rubric": "a) Tam giác vuông ABE = tam giác vuông ADK (cạnh góc vuông - góc nhọn: AB = AD, góc BAE = góc DAK cùng phụ góc DAE) => AE = AK (0.25đ)\nTam giác AKF vuông tại A có đường cao AD = a (0.25đ)\nb) Trong tam giác vuông AKF có AD là đường cao: 1/AD² = 1/AK² + 1/AF² (0.25đ)\nMà AK = AE nên: 1/AE² + 1/AF² = 1/AD² = 1/a² (không đổi) (0.25đ)"
      }
    ]
  },
  "c3_8_bai5_test3": {
    "title": "Toán 8 (KNTT) - Bài 14: Hình thoi và hình vuông - Bài kiểm tra số 3 (🔥 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tứ giác có 4 trục đối xứng là:",
        "options": [
          "Hình vuông",
          "Hình chữ nhật",
          "Hình thoi",
          "Hình bình hành"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khẳng định nào sau đây là sai khi nói về hình vuông?",
        "options": [
          "Có hai đường chéo không bằng nhau",
          "Vừa là hình chữ nhật vừa là hình thoi",
          "Có tâm đối xứng là giao điểm hai đường chéo",
          "Hai đường chéo vuông góc tại trung điểm mỗi đường"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tứ giác có các đỉnh là trung điểm của bốn cạnh của một hình thoi là:",
        "options": [
          "Hình chữ nhật",
          "Hình vuông",
          "Hình thoi",
          "Hình bình hành không vuông"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tứ giác có các đỉnh là trung điểm của bốn cạnh của một hình vuông là:",
        "options": [
          "Hình vuông",
          "Hình thoi",
          "Hình chữ nhật",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Một hình thoi có cạnh bằng $a$ và một góc bằng $60^\\circ$. Diện tích của hình thoi bằng:",
        "options": [
          "$\\frac{a^2\\sqrt{3}}{2}$",
          "$a^2\\sqrt{3}$",
          "$\\frac{a^2}{2}$",
          "$\\frac{a^2\\sqrt{3}}{4}$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hình vuông có cạnh bằng $a$. Bán kính đường tròn nội tiếp hình vuông bằng:",
        "options": [
          "$\\frac{a}{2}$",
          "$\\frac{a\\sqrt{2}}{2}$",
          "$a$",
          "$\\frac{a}{4}$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho hình vuông $ABCD$. Điểm $M$ nằm trong hình vuông sao cho tam giác $MCD$ đều. Khi đó số đo góc $\\widehat{MAB}$ bằng:",
        "options": [
          "$15^\\circ$",
          "$30^\\circ$",
          "$45^\\circ$",
          "$20^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho hình thoi $ABCD$ có đường chéo $AC = a, BD = b$. Tỉ số $\\frac{a}{b} = \\frac{3}{4}$ và chu vi bằng $40\\text{ cm}$. Tích hai đường chéo $a \\cdot b$ bằng:",
        "options": [
          "$192\\text{ cm}^2$",
          "$96\\text{ cm}^2$",
          "$384\\text{ cm}^2$",
          "$200\\text{ cm}^2$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = c, AC = b$. Dựng hình vuông $ADEF$ nội tiếp tam giác ($D \\in AB, E \\in BC, F \\in AC$). Độ dài cạnh của hình vuông đó bằng:",
        "options": [
          "$\\frac{bc}{b + c}$",
          "$\\frac{bc}{2(b + c)}$",
          "$\\frac{b + c}{2}$",
          "$\\sqrt{bc}$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho hình vuông $ABCD$ cạnh $6\\text{ cm}$. Lấy $E, F$ lần lượt trên $BC, CD$ sao cho $BE = 2\\text{ cm}, DF = 3\\text{ cm}$. Diện tích tam giác $AEF$ bằng:",
        "options": [
          "$11\\text{ cm}^2$",
          "$12\\text{ cm}^2$",
          "$13\\text{ cm}^2$",
          "$15\\text{ cm}^2$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho hình vuông $ABCD$. Điểm $P$ thuộc miền trong hình vuông thỏa mãn $PA : PB : PC = 1 : 2 : 3$. Khi đó số đo góc $\\widehat{APB}$ bằng:",
        "options": [
          "$135^\\circ$",
          "$120^\\circ$",
          "$150^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một hình chữ nhật và một hình vuông có cùng chu vi. Khẳng định nào sau đây luôn đúng?",
        "options": [
          "Diện tích hình vuông lớn hơn diện tích hình chữ nhật",
          "Diện tích hình chữ nhật lớn hơn diện tích hình vuông",
          "Hai hình có diện tích bằng nhau",
          "Đường chéo hai hình bằng nhau"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình vuông $ABCD$. Gọi $M$ là trung điểm của cạnh $CD$. Lấy điểm $N$ trên cạnh $BC$ sao cho $NC = 2NB$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Nếu cạnh hình vuông là $a$ thì $DM = MC = \\frac{a}{2}$ và $BN = \\frac{a}{3}, NC = \\frac{2a}{3}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $AM^2 = a^2 + \\frac{a^2}{4} = \\frac{5a^2}{4}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng $AN$ vuông góc với đoạn thẳng $BM$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Tam giác $AMN$ là tam giác vuông tại $M$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình vuông $ABCD$ có cạnh bằng $a$. Lấy điểm $E$ bất kì trên đường chéo $BD$. Kẻ $EM \\perp AB$ tại $M$ và $EN \\perp AD$ tại $N$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $AMEN$ là một hình chữ nhật.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tam giác $BME$ và tam giác $DNE$ đều là các tam giác vuông cân.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Chu vi hình chữ nhật $AMEN$ luôn bằng $2a$ (không phụ thuộc vị trí của $E$).",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Đoạn thẳng $MN$ vuông góc với đoạn thẳng $CE$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình vuông $ABCD$ cạnh $10\\text{ cm}$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $CD$. Tính diện tích tứ giác $AMCN$ (theo cm²).",
        "answer": "50"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Hình thoi $ABCD$ có chu vi $40\\text{ cm}$, một đường chéo dài $12\\text{ cm}$. Tính diện tích hình thoi (theo cm²).",
        "answer": "96"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hình vuông $ABCD$ cạnh $12\\text{ cm}$. Điểm $E$ thuộc cạnh $BC$ sao cho $BE = 5\\text{ cm}$. Đường phân giác góc $\\widehat{DAE}$ cắt cạnh $CD$ tại $F$. Tính độ dài đoạn thẳng $CF$ (theo cm).",
        "answer": "7"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình vuông $ABCD$ cạnh $a = 6\\text{ cm}$. Một góc vuông $xAy$ quay quanh đỉnh $A$, cắt các cạnh $BC$ và $CD$ lần lượt tại $E$ và $F$. Khi $BE = 2\\text{ cm}$, tính diện tích tam giác $AEF$ (theo cm²).",
        "answer": "22.5"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình vuông $ABCD$. Lấy điểm $E$ trên tia đối của tia $CD$ và điểm $F$ trên tia đối của tia $BC$ sao cho $CE = CF$.\na) Chứng minh tam giác $ACE$ bằng tam giác $ACF$.\nb) Gọi $M$ là trung điểm của $EF$. Chứng minh tam giác $AMC$ vuông cân tại $M$.",
        "rubric": "a) Xét tam giác ACE và ACF: AC chung, CE = CF, góc ACE = góc ACF = 135° => tam giác ACE = tam giác ACF (c-g-c) (0.5đ)\nb) Tam giác CEF vuông cân tại C, M là trung điểm EF => CM vuông góc EF và CM = ME = MF. Chứng minh tam giác AMC vuông cân tại M (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình vuông $ABCD$. Gọi $M$ là trung điểm của $BC$, $N$ là điểm trên cạnh $CD$ sao cho $CN = \\frac{1}{4}CD$. Chứng minh rằng tam giác $AMN$ là tam giác vuông tại $M$.",
        "rubric": "Đặt cạnh hình vuông là a. BM = MC = a/2; CN = a/4; DN = 3a/4.\nAM² = AB² + BM² = a² + a²/4 = 5a²/4 (0.25đ)\nMN² = MC² + CN² = a²/4 + a²/16 = 5a²/16 (0.25đ)\nAN² = AD² + DN² = a² + 9a²/16 = 25a²/16 (0.25đ)\nNhận thấy AM² + MN² = 5a²/4 + 5a²/16 = 25a²/16 = AN². Theo định lí Pythagore đảo => tam giác AMN vuông tại M (ĐPCM) (0.25đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình vuông $ABCD$ có cạnh bằng $a$. Một đường thẳng $d$ đi qua đỉnh $A$ cắt cạnh $BC$ tại $E$ và cắt đường thẳng $CD$ tại $F$.\na) Chứng minh rằng: $\\frac{1}{AE^2} + \\frac{1}{AF^2} = \\frac{1}{a^2}$.\nb) Tìm vị trí của điểm $E$ trên cạnh $BC$ sao cho tổng khoảng cách $AE + AF$ đạt giá trị nhỏ nhất.",
        "rubric": "a) Kẻ AG vuông góc AE (G thuộc đường thẳng CD). Tam giác ABE = tam giác ADG (c-g-c) => AE = AG. Trong tam giác vuông AGF có đường cao AD = a: 1/AD² = 1/AG² + 1/AF² <=> 1/a² = 1/AE² + 1/AF² (0.5đ)\nb) Áp dụng BĐT Cauchy-Schwarz: (AE + AF)² <= 2(AE² + AF²)... Tổng AE + AF nhỏ nhất khi E trùng với đỉnh B hoặc vị trí đối xứng. Hoặc khảo sát hàm lượng giác: AE = a/cos(alpha), AF = a/sin(alpha) => min khi alpha = 45° (E trùng C)... (0.5đ)"
      }
    ]
  }
};

if (typeof window !== 'undefined') {
  window.CHAPTER3_TOAN8_EXAMS = window.CHAPTER3_TOAN8_EXAMS || {};
  Object.assign(window.CHAPTER3_TOAN8_EXAMS, BAI_5_TOAN8_EXAMS);
  window.EXAMS_8_C3_8 = window.CHAPTER3_TOAN8_EXAMS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BAI_5_TOAN8_EXAMS;
}
