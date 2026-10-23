// ==============================================================================
// NGÂN HÀNG ĐỀ KIỂM TRA CHƯƠNG III: TỨ GIÁC - TOÁN 8 (KẾT NỐI TRI THỨC)
// Bao gồm đầy đủ Bài 10 (Tứ giác), Bài 11 (Hình thang cân), Bài 12 (Hình bình hành)...
// Mỗi bài 3 đề chuẩn ma trận: 12 trắc nghiệm, 2 đúng sai, 4 trả lời ngắn, 3 tự luận
// Phân hóa độ khó rõ rệt: Đề 1 (Cơ bản) < Đề 2 (Khá) < Đề 3 (Nâng cao)
// ==============================================================================

const CHAPTER3_TOAN8_EXAMS = {
  "c3_8_bai1_test1": {
    "title": "Toán 8 (KNTT) - Bài 10: Tứ giác - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tổng số đo bốn góc của một tứ giác lồi bằng:",
        "options": [
          "$360^\\circ$",
          "$180^\\circ$",
          "$270^\\circ$",
          "$540^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 60^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = 100^\\circ$. Số đo góc $D$ bằng:",
        "options": [
          "$120^\\circ$",
          "$100^\\circ$",
          "$110^\\circ$",
          "$130^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tứ giác lồi là tứ giác mà:",
        "options": [
          "Luôn nằm trong một nửa mặt phẳng có bờ là đường thẳng chứa bất kì cạnh nào",
          "Có hai góc tù và hai góc nhọn",
          "Có hai đường chéo bằng nhau",
          "Có bốn cạnh bằng nhau"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Số đường chéo của một tứ giác lồi là:",
        "options": [
          "$2$",
          "$4$",
          "$3$",
          "$1$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Góc kề bù với một góc của tứ giác được gọi là:",
        "options": [
          "Góc ngoài của tứ giác",
          "Góc trong của tứ giác",
          "Góc đối của tứ giác",
          "Góc kề của tứ giác"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Một tứ giác có thể có nhiều nhất bao nhiêu góc tù?",
        "options": [
          "$3$",
          "$4$",
          "$2$",
          "$1$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tứ giác $ABCD$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = 90^\\circ, \\widehat{C} = 120^\\circ$. Số đo góc ngoài tại đỉnh $D$ bằng:",
        "options": [
          "$100^\\circ$",
          "$80^\\circ$",
          "$110^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 2x, \\widehat{B} = 3x, \\widehat{C} = 4x, \\widehat{D} = x$. Giá trị của $x$ là:",
        "options": [
          "$36^\\circ$",
          "$30^\\circ$",
          "$40^\\circ$",
          "$45^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tứ giác $ABCD$ có chu vi $32\\text{ cm}$, biết $AB = 6\\text{ cm}, BC = 8\\text{ cm}, CD = 10\\text{ cm}$. Độ dài cạnh $AD$ là:",
        "options": [
          "$8\\text{ cm}$",
          "$6\\text{ cm}$",
          "$9\\text{ cm}$",
          "$7\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Trong một tứ giác, khẳng định nào sau đây là luôn đúng?",
        "options": [
          "Có nhiều nhất 3 góc nhọn",
          "Cả 4 góc đều phải là góc nhọn",
          "Có ít nhất 2 góc vuông",
          "Tổng 2 góc đối luôn bằng $180^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$. Khẳng định nào sau đây là đúng theo bất đẳng thức tam giác?",
        "options": [
          "$AC < AB + BC$",
          "$AC > AB + BC$",
          "$AC = AB + BC$",
          "$AC \\ge AB + BC$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tổng các góc ngoài tại 4 đỉnh của một tứ giác lồi bằng:",
        "options": [
          "$360^\\circ$",
          "$180^\\circ$",
          "$720^\\circ$",
          "$540^\\circ$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tứ giác $ABCD$ có $\\widehat{A} = 100^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = 110^\\circ$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số đo góc $D$ bằng $70^\\circ$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng hai góc $\\widehat{A} + \\widehat{B} = 180^\\circ$ nên hai cạnh $AD$ và $BC$ song song.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Góc ngoài tại đỉnh $A$ của tứ giác có số đo là $100^\\circ$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Tứ giác $ABCD$ có ít nhất hai góc nhọn.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một khu đất hình tứ giác $ABCD$ có độ dài các cạnh lần lượt là $AB = 12\\text{ m}, BC = 15\\text{ m}, CD = 9\\text{ m}, DA = 14\\text{ m}$ và đường chéo $AC = 18\\text{ m}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Chu vi của khu đất tứ giác $ABCD$ bằng $50\\text{ m}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài đường chéo $AC$ luôn nhỏ hơn tổng độ dài hai cạnh $AB + BC$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Chu vi tam giác $ABC$ lớn hơn chu vi tam giác $ADC$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Tổng độ dài hai đường chéo $AC + BD$ của tứ giác có thể nhỏ hơn $25\\text{ m}$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 75^\\circ, \\widehat{B} = 115^\\circ, \\widehat{C} = 80^\\circ$. Tính số đo góc $D$ (theo độ).",
        "answer": "90"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tứ giác $MNPQ$ có các góc tỉ lệ với $1 : 2 : 3 : 4$. Tìm số đo góc lớn nhất (theo độ).",
        "answer": "144"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 100^\\circ, \\widehat{B} = 120^\\circ$. Hai góc $C$ và $D$ có mối liên hệ $\\widehat{C} - \\widehat{D} = 20^\\circ$. Tính số đo góc $C$ (theo độ).",
        "answer": "80"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho tứ giác $ABCD$ có hai đường chéo cắt nhau tại $O$. Biết $OA = 3\\text{ cm}, OC = 5\\text{ cm}, OB = 4\\text{ cm}, OD = 6\\text{ cm}$. Tính tổng độ dài hai đường chéo $AC + BD$ (theo cm).",
        "answer": "18"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 110^\\circ, \\widehat{B} = 90^\\circ$. Biết góc ngoài tại đỉnh $C$ bằng $120^\\circ$.\na) Tính số đo góc $C$ của tứ giác.\nb) Tính số đo góc $D$ của tứ giác.",
        "rubric": "a) Góc C trong và góc ngoài tại C kề bù nên: góc C = 180° - 120° = 60° (0.5đ)\nb) Tổng 4 góc tứ giác: góc D = 360° - (110° + 90° + 60°) = 100° (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Chứng minh rằng trong một tứ giác lồi $ABCD$, tổng độ dài hai đường chéo lớn hơn nửa chu vi của tứ giác:\n$$AC + BD > \\frac{AB + BC + CD + DA}{2}$$",
        "rubric": "Gọi O là giao điểm của AC và BD (0.25đ)\nTrong các tam giác OAB, OBC, OCD, ODA ta có:\nOA + OB > AB, OB + OC > BC, OC + OD > CD, OD + OA > DA (0.25đ)\nCộng từng vế: 2(OA + OC + OB + OD) > AB + BC + CD + DA (0.25đ)\n<=> 2(AC + BD) > Chu vi => AC + BD > (AB + BC + CD + DA)/2 (ĐPCM) (0.25đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tứ giác lồi $ABCD$. Các tia phân giác của góc $A$ và góc $B$ cắt nhau tại điểm $I$.\na) Chứng minh rằng $\\widehat{AIB} = \\frac{\\widehat{C} + \\widehat{D}}{2}$.\nb) Biết $\\widehat{C} = 85^\\circ$ và $\\widehat{D} = 75^\\circ$, tính số đo góc $AIB$.",
        "rubric": "a) Trong tam giác AIB: góc AIB = 180° - (góc A/2 + góc B/2) = 180° - (góc A + góc B)/2 (0.25đ)\nMặt khác: góc A + góc B = 360° - (góc C + góc D) (0.25đ)\n=> góc AIB = 180° - [360° - (góc C + góc D)] / 2 = (góc C + góc D)/2 (ĐPCM) (0.25đ)\nb) Thay số: góc AIB = (85° + 75°)/2 = 160°/2 = 80° (0.25đ)"
      }
    ]
  },
  "c3_8_bai1_test2": {
    "title": "Toán 8 (KNTT) - Bài 10: Tứ giác - Bài kiểm tra số 2 (⚡ Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Góc kề bù với góc $A$ của tứ giác $ABCD$ có số đo $115^\\circ$. Số đo góc $A$ bằng:",
        "options": [
          "$65^\\circ$",
          "$75^\\circ$",
          "$115^\\circ$",
          "$85^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tứ giác $ABCD$ có $\\widehat{A} = \\widehat{C} = 90^\\circ$. Tổng hai góc $\\widehat{B} + \\widehat{D}$ bằng:",
        "options": [
          "$180^\\circ$",
          "$90^\\circ$",
          "$270^\\circ$",
          "$360^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} : \\widehat{B} : \\widehat{C} : \\widehat{D} = 1 : 2 : 3 : 4$. Góc nhỏ nhất của tứ giác bằng:",
        "options": [
          "$36^\\circ$",
          "$18^\\circ$",
          "$72^\\circ$",
          "$54^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tứ giác có hai đường chéo vuông góc với nhau tại trung điểm của mỗi đường là:",
        "options": [
          "Hình thoi",
          "Hình thang cân",
          "Hình chữ nhật",
          "Hình thang vuông"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong tứ giác lồi $ABCD$, đoạn thẳng nối hai đỉnh đối diện gọi là:",
        "options": [
          "Đường chéo",
          "Cạnh bên",
          "Đường cao",
          "Đường trung tuyến"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nếu một tứ giác có 3 góc vuông thì góc còn lại là:",
        "options": [
          "Góc vuông",
          "Góc nhọn",
          "Góc tù",
          "Góc bẹt"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tứ giác $ABCD$ có $\\widehat{A} = 80^\\circ, \\widehat{B} = 70^\\circ$, góc ngoài tại đỉnh $C$ bằng $110^\\circ$. Số đo góc $D$ là:",
        "options": [
          "$140^\\circ$",
          "$130^\\circ$",
          "$120^\\circ$",
          "$150^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = \\widehat{B} + 20^\\circ, \\widehat{B} = \\widehat{C} + 10^\\circ, \\widehat{C} = \\widehat{D} + 10^\\circ$. Số đo góc $D$ bằng:",
        "options": [
          "$70^\\circ$",
          "$80^\\circ$",
          "$60^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$ của tứ giác $ABCD$. Khẳng định nào sau đây luôn đúng?",
        "options": [
          "$AC + BD < AB + BC + CD + DA$",
          "$AC + BD > AB + BC + CD + DA$",
          "$AC + BD = AB + CD$",
          "$AC \\cdot BD = AB \\cdot CD$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tứ giác $ABCD$ có $\\widehat{A} = 120^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = 2\\widehat{D}$. Số đo góc $D$ là:",
        "options": [
          "$53^\\circ 20'$",
          "$60^\\circ$",
          "$45^\\circ$",
          "$50^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} + \\widehat{B} = 200^\\circ$. Hai tia phân giác của góc $C$ và góc $D$ cắt nhau tại $M$. Số đo góc $CMD$ bằng:",
        "options": [
          "$100^\\circ$",
          "$80^\\circ$",
          "$120^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $AB = BC$ và $CD = DA$. Khi đó đường thẳng $BD$ là:",
        "options": [
          "Đường trung trực của đoạn thẳng $AC$",
          "Đường song song với $AC$",
          "Đường phân giác góc $B$ nhưng không vuông góc $AC$",
          "Đoạn thẳng bằng $AC$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tứ giác $ABCD$ có các góc ngoài tại các đỉnh $A, B, C, D$ lần lượt là $A_1, B_1, C_1, D_1$. Biết $\\widehat{A} = 110^\\circ, \\widehat{B} = 70^\\circ, \\widehat{C} = 60^\\circ$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số đo góc $D$ của tứ giác bằng $120^\\circ$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Số đo góc ngoài $D_1$ tại đỉnh $D$ bằng $60^\\circ$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tổng bốn góc ngoài $A_1 + B_1 + C_1 + D_1 = 360^\\circ$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Góc ngoài $A_1$ lớn hơn góc ngoài $C_1$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tứ giác $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Biết $AB = 7\\text{ cm}, BC = 9\\text{ cm}, CD = 11\\text{ cm}, DA = 5\\text{ cm}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Nửa chu vi của tứ giác $ABCD$ bằng $16\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng độ dài hai đường chéo $AC + BD$ luôn lớn hơn $16\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tổng độ dài hai đường chéo $AC + BD$ luôn nhỏ hơn $32\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Điểm $O$ là điểm duy nhất thỏa mãn tổng khoảng cách $OA + OB + OC + OD$ nhỏ nhất.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 100^\\circ, \\widehat{D} = 60^\\circ$. Góc ngoài tại đỉnh $B$ là $80^\\circ$. Tính số đo góc $C$ (theo độ).",
        "answer": "100"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{C} + \\widehat{D} = 150^\\circ$. Hai tia phân giác của góc $A$ và góc $B$ cắt nhau tại $I$. Tính số đo góc $AIB$ (theo độ).",
        "answer": "75"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Một tứ giác có độ dài 4 cạnh là $x, 2x, 3x, 4x$ (đơn vị cm). Biết chu vi tứ giác là $50\\text{ cm}$. Tính độ dài cạnh lớn nhất (theo cm).",
        "answer": "20"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho tứ giác $ABCD$ có chu vi bằng $60\\text{ cm}$. Tổng độ dài hai đường chéo $AC + BD$ là một số nguyên dương $k$. Giá trị nhỏ nhất có thể có của $k$ là bao nhiêu?",
        "answer": "31"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} : \\widehat{B} : \\widehat{C} : \\widehat{D} = 2 : 3 : 4 : 3$.\na) Tính số đo mỗi góc của tứ giác.\nb) Chứng minh rằng hai đường thẳng $AB$ và $CD$ song song với nhau.",
        "rubric": "a) Tổng số phần: 2 + 3 + 4 + 3 = 12 phần. Giá trị 1 phần: 360°/12 = 30°.\nGóc A = 60°, góc B = 90°, góc C = 120°, góc D = 90° (0.5đ)\nb) Ta có góc B = 90° (BC vuông góc AB) và góc D = 90° (CD vuông góc AD), mặt khác góc A + góc D = 60° + 90° = 150°, góc B + góc C = 90° + 120° = 210°. Nếu xét góc A + góc B = 150°... (Xét góc trong cùng phía: góc B + góc C = 90 + 120, xét góc B = 90° và D = 90°... Hoặc có góc A + góc C = 180°...) (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tứ giác $ABCD$ có $AB = AD$ và $CB = CD$. Gọi $O$ là giao điểm của $AC$ và $BD$.\na) Chứng minh tam giác $ABC$ bằng tam giác $ADC$.\nb) Chứng minh $AC$ vuông góc với $BD$ tại trung điểm của $BD$.",
        "rubric": "a) Xét tam giác ABC và ADC: AB = AD (gt), CB = CD (gt), AC chung => tam giác ABC = tam giác ADC (c-c-c) (0.5đ)\nb) Suy ra góc BAC = góc DAC => AC là phân giác góc BAD trong tam giác cân ABD => AC vuông góc BD và đi qua trung điểm của BD (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tứ giác lồi $ABCD$. Gọi $M$ là một điểm bất kì nằm trong tứ giác.\na) Chứng minh rằng: $MA + MB + MC + MD \\ge AC + BD$.\nb) Điểm $M$ ở vị trí nào thì tổng $MA + MB + MC + MD$ đạt giá trị nhỏ nhất?",
        "rubric": "a) Áp dụng bất đẳng thức tam giác trong tam giác MAC: MA + MC >= AC (dấu '=' xảy ra <=> M thuộc AC) (0.25đ)\nTrong tam giác MBD: MB + MD >= BD (dấu '=' xảy ra <=> M thuộc BD) (0.25đ)\nCộng vế với vế: MA + MB + MC + MD >= AC + BD (0.25đ)\nb) Dấu '=' xảy ra <=> M đồng thời thuộc AC và BD <=> M là giao điểm của hai đường chéo AC và BD. Vậy GTNN là AC + BD khi M là giao điểm 2 đường chéo (0.25đ)"
      }
    ]
  },
  "c3_8_bai1_test3": {
    "title": "Toán 8 (KNTT) - Bài 10: Tứ giác - Bài kiểm tra số 3 (🔥 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tứ giác $ABCD$ có $\\widehat{A} = 100^\\circ, \\widehat{B} = 70^\\circ, \\widehat{C} = 110^\\circ$. Góc ngoài tại đỉnh $D$ có số đo là:",
        "options": [
          "$100^\\circ$",
          "$80^\\circ$",
          "$90^\\circ$",
          "$110^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khẳng định nào sau đây là sai khi nói về tứ giác lồi?",
        "options": [
          "Có thể có 4 góc tù",
          "Tổng 4 góc luôn bằng $360^\\circ$",
          "Hai đường chéo luôn cắt nhau tại một điểm nằm trong tứ giác",
          "Có nhiều nhất 3 góc nhọn"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Góc kề bù của một góc trong tứ giác bằng $135^\\circ$. Góc trong đó là góc:",
        "options": [
          "Nhọn",
          "Tù",
          "Vuông",
          "Bẹt"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Cho tứ giác $ABCD$. Tổng $\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D}$ tính theo độ radian là:",
        "options": [
          "$2\\pi$",
          "$\\pi$",
          "$4\\pi$",
          "$\\frac{3\\pi}{2}$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tứ giác có hai đường chéo bằng nhau và cắt nhau tại trung điểm của mỗi đường là:",
        "options": [
          "Hình chữ nhật",
          "Hình thoi",
          "Hình bình hành",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tứ giác có 4 cạnh bằng nhau được gọi là:",
        "options": [
          "Hình thoi",
          "Hình chữ nhật",
          "Hình thang cân",
          "Hình bình hành"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} - \\widehat{B} = 10^\\circ, \\widehat{B} - \\widehat{C} = 10^\\circ, \\widehat{C} - \\widehat{D} = 10^\\circ$. Số đo góc $A$ là:",
        "options": [
          "$105^\\circ$",
          "$95^\\circ$",
          "$110^\\circ$",
          "$100^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có các tia phân giác của góc $A$ và góc $D$ cắt nhau tại $E$, các tia phân giác của góc $B$ và góc $C$ cắt nhau tại $F$. Tổng $\\widehat{AED} + \\widehat{BFC}$ bằng:",
        "options": [
          "$180^\\circ$",
          "$360^\\circ$",
          "$90^\\circ$",
          "$270^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tứ giác lồi $ABCD$ có $\\widehat{A} = 90^\\circ, \\widehat{C} = 90^\\circ$. Các tia phân giác của góc $B$ và góc $D$:",
        "options": [
          "Song song hoặc trùng nhau",
          "Vuông góc với nhau",
          "Tạo với nhau một góc $45^\\circ$",
          "Cắt nhau tại góc $60^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có độ dài các cạnh thỏa mãn $AB + CD = BC + AD$. Tứ giác này có tính chất:",
        "options": [
          "Ngoại tiếp được một đường tròn",
          "Nội tiếp được một đường tròn",
          "Là hình thoi",
          "Có hai đường chéo bằng nhau"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Độ dài hai đường chéo của tứ giác $ABCD$ là $8\\text{ cm}$ và $12\\text{ cm}$. Đoạn thẳng nối trung điểm hai đường chéo bằng $2\\text{ cm}$. Khẳng định nào đúng?",
        "options": [
          "Tứ giác $ABCD$ không thể là hình bình hành",
          "Tứ giác $ABCD$ là hình bình hành",
          "Hai đường chéo vuông góc",
          "Hai đường chéo cắt nhau tại trung điểm mỗi đường"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $AC = 10\\text{ cm}, BD = 14\\text{ cm}$. Diện tích lớn nhất của tứ giác $ABCD$ bằng:",
        "options": [
          "$70\\text{ cm}^2$",
          "$140\\text{ cm}^2$",
          "$35\\text{ cm}^2$",
          "$24\\text{ cm}^2$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tứ giác lồi $ABCD$ có $\\widehat{A} = \\alpha, \\widehat{B} = \\beta, \\widehat{C} = \\gamma, \\widehat{D} = \\delta$. Gọi $I$ là giao điểm các tia phân giác của $\\widehat{A}$ và $\\widehat{D}$; $K$ là giao điểm các tia phân giác của $\\widehat{B}$ và $\\widehat{C}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Trong tam giác $AID$, góc $\\widehat{AID} = 180^\\circ - \\frac{\\alpha + \\delta}{2}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Trong tam giác $BKC$, góc $\\widehat{BKC} = 180^\\circ - \\frac{\\beta + \\gamma}{2}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tổng hai góc $\\widehat{AID} + \\widehat{BKC} = 180^\\circ$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Nếu $\\alpha + \\delta = 180^\\circ$ thì hai tia phân giác $AI$ và $DI$ vuông góc với nhau.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tứ giác lồi $ABCD$. Gọi $P$ là chu vi của tứ giác và $d_1, d_2$ lần lượt là độ dài hai đường chéo $AC, BD$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Bất đẳng thức $d_1 + d_2 > \\frac{P}{2}$ luôn đúng với mọi tứ giác lồi.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Bất đẳng thức $d_1 + d_2 < P$ luôn đúng với mọi tứ giác lồi.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Nếu $P = 40\\text{ cm}$ thì tổng $d_1 + d_2$ có thể nhận giá trị bằng $19\\text{ cm}$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Nếu tứ giác có hai đường chéo vuông góc thì diện tích $S = \\frac{1}{2} d_1 d_2$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 120^\\circ, \\widehat{B} = 90^\\circ$. Tỉ số giữa góc $C$ và góc $D$ là $2 : 3$. Tính số đo góc $D$ (theo độ).",
        "answer": "90"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tứ giác $ABCD$ có hai đường chéo vuông góc với nhau và có độ dài $AC = 16\\text{ cm}, BD = 25\\text{ cm}$. Tính diện tích tứ giác (theo cm²).",
        "answer": "200"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = 80^\\circ$. Tia phân giác góc $C$ và góc $D$ cắt nhau tại $M$. Tính số đo góc $\\widehat{CMD}$ (theo độ).",
        "answer": "75"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho tứ giác $ABCD$ có $AB = 3\\text{ cm}, BC = 7\\text{ cm}, CD = 11\\text{ cm}, DA = 5\\text{ cm}$. Số đo lớn nhất của đường chéo $AC$ là một số nguyên. Tìm số nguyên đó (theo cm).",
        "answer": "7"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{B} + \\widehat{D} = 180^\\circ, CB = CD$.\na) Chứng minh điểm $C$ nằm trên đường trung trực của đoạn thẳng $BD$.\nb) Chứng minh tia $AC$ là tia phân giác của góc $BAD$.",
        "rubric": "a) Vì CB = CD (gt) nên C cách đều hai đầu mút B và D => C nằm trên đường trung trực của BD (0.5đ)\nb) Trên tia đối của tia DA lấy điểm E sao cho DE = AB. Tam giác ABC = tam giác EDC (c-g-c) => AC = EC và góc BAC = góc DEC = góc DAC => AC là tia phân giác của góc BAD (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Chứng minh rằng trong một tứ giác lồi $ABCD$, tổng độ dài hai đường chéo $AC + BD$ thỏa mãn hệ thức:\n$$\\frac{AB + BC + CD + DA}{2} < AC + BD < AB + BC + CD + DA$$",
        "rubric": "- Chứng minh vế trái: Gọi O là giao điểm 2 đường chéo, áp dụng BĐT tam giác cho 4 tam giác OAB, OBC, OCD, ODA => 2(AC + BD) > Chu vi => AC + BD > Chu vi / 2 (0.5đ)\n- Chứng minh vế phải: Áp dụng BĐT tam giác cho tam giác ABC: AC < AB + BC; tam giác ADC: AC < AD + CD; tam giác ABD: BD < AB + AD; tam giác CBD: BD < BC + CD. Cộng lại: 2(AC + BD) < 2(AB + BC + CD + DA) => AC + BD < Chu vi (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tứ giác lồi $ABCD$ có diện tích $S$ và hai đường chéo $AC, BD$.\na) Chứng minh rằng: $S \\le \\frac{1}{2} AC \\cdot BD$.\nb) Dấu đẳng thức xảy ra khi nào? Nếu $AC = 10\\text{ cm}, BD = 12\\text{ cm}$ thì diện tích lớn nhất của tứ giác bằng bao nhiêu?",
        "rubric": "a) Gọi alpha là góc tạo bởi hai đường chéo AC và BD. Diện tích tứ giác lồi bất kì bằng S = 1/2 . AC . BD . sin(alpha) (0.5đ)\nVì sin(alpha) <= 1 với mọi góc alpha nên S <= 1/2 . AC . BD (0.25đ)\nb) Dấu '=' xảy ra <=> sin(alpha) = 1 <=> alpha = 90° <=> AC vuông góc với BD.\nKhi đó S_max = 1/2 . 10 . 12 = 60 cm² (0.25đ)"
      }
    ]
  },
  "c3_8_bai2_test1": {
    "title": "Toán 8 (KNTT) - Bài 11: Hình thang cân - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hình thang là tứ giác có:",
        "options": [
          "Hai cạnh đối song song",
          "Hai cạnh đối bằng nhau",
          "Hai đường chéo bằng nhau",
          "Bốn cạnh bằng nhau"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hình thang cân là hình thang có:",
        "options": [
          "Hai góc kề một đáy bằng nhau",
          "Hai cạnh bên song song",
          "Hai góc đối bằng nhau",
          "Có một góc vuông"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong hình thang cân, khẳng định nào sau đây là sai?",
        "options": [
          "Hai góc đối bằng nhau",
          "Hai cạnh bên bằng nhau",
          "Hai đường chéo bằng nhau",
          "Hai góc kề một đáy bằng nhau"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hình thang có một góc vuông được gọi là:",
        "options": [
          "Hình thang vuông",
          "Hình thang cân",
          "Hình chữ nhật",
          "Hình bình hành"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$). Biết $\\widehat{C} = 60^\\circ$. Số đo góc $D$ bằng:",
        "options": [
          "$60^\\circ$",
          "$120^\\circ$",
          "$90^\\circ$",
          "$30^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hình thang cân có bao nhiêu trục đối xứng?",
        "options": [
          "$1$",
          "$2$",
          "$0$",
          "$4$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$). Biết $\\widehat{D} = 70^\\circ$. Số đo góc $A$ bằng:",
        "options": [
          "$110^\\circ$",
          "$70^\\circ$",
          "$120^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$) có $AC = BD$. Tứ giác $ABCD$ là:",
        "options": [
          "Hình thang cân",
          "Hình bình hành",
          "Hình chữ nhật",
          "Hình thang vuông"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Hình thang cân $ABCD$ có đáy nhỏ $AB = 4\\text{ cm}$, đáy lớn $CD = 10\\text{ cm}$, cạnh bên $AD = 5\\text{ cm}$. Chu vi hình thang cân là:",
        "options": [
          "$24\\text{ cm}$",
          "$19\\text{ cm}$",
          "$29\\text{ cm}$",
          "$20\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$). Kẻ các đường cao $AH, BK$ xuống đáy $CD$. Khẳng định nào sau đây đúng?",
        "options": [
          "$DH = CK$",
          "$DH = 2CK$",
          "$AH = CD$",
          "$DH = AB$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Một hình thang cân có một góc bằng $50^\\circ$. Các góc còn lại của hình thang đó lần lượt là:",
        "options": [
          "$50^\\circ, 130^\\circ, 130^\\circ$",
          "$50^\\circ, 50^\\circ, 130^\\circ$",
          "$60^\\circ, 120^\\circ, 130^\\circ$",
          "$50^\\circ, 90^\\circ, 140^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ cân tại $A$. Lấy điểm $D$ trên cạnh $AB$, điểm $E$ trên cạnh $AC$ sao cho $AD = AE$. Tứ giác $BDEC$ là:",
        "options": [
          "Hình thang cân",
          "Hình bình hành",
          "Hình thang vuông",
          "Hình thoi"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình thang cân $ABCD$ có $AB \\parallel CD$ ($AB < CD$), $\\widehat{D} = 60^\\circ$. Kẻ đường cao $AH$ vuông góc với $CD$ ($H \\in CD$).",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số đo góc $C$ bằng $60^\\circ$ và số đo góc $A$ bằng $120^\\circ$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $AC$ có độ dài bằng đoạn thẳng $BD$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Trong tam giác vuông $ADH$, số đo góc $\\widehat{DAH} = 30^\\circ$ nên $DH = \\frac{1}{2} AD$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Nếu $AD = 6\\text{ cm}$ thì độ dài đoạn thẳng $DH = 4\\text{ cm}$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một chiếc thang gấp có dạng hình thang cân $ABCD$ với hai thanh đứng là $AD$ và $BC$, hai bậc thang song song là $AB$ và $CD$. Biết $AB = 40\\text{ cm}, CD = 60\\text{ cm}$ và cạnh bên $AD = 50\\text{ cm}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Độ dài cạnh bên $BC$ bằng $50\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Chu vi của khung hình thang cân $ABCD$ bằng $200\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Kẻ hai đường cao từ $A$ và $B$ xuống $CD$ chia đáy $CD$ thành ba đoạn, trong đó hai đoạn ở hai bên mỗi đoạn dài $10\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Chiều cao của chiếc thang nhỏ hơn $45\\text{ cm}$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$) có $\\widehat{A} = 115^\\circ$. Tính số đo góc $C$ (theo độ).",
        "answer": "65"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Hình thang cân $ABCD$ có đáy nhỏ $AB = 5\\text{ cm}$, đáy lớn $CD = 13\\text{ cm}$, cạnh bên bằng $5\\text{ cm}$. Kẻ đường cao $AH \\perp CD$. Tính độ dài $DH$ (theo cm).",
        "answer": "4"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang cân $ABCD$ có đáy nhỏ $AB = 6\\text{ cm}$, chu vi hình thang bằng $28\\text{ cm}$, cạnh bên bằng $5\\text{ cm}$. Tính độ dài đáy lớn $CD$ (theo cm).",
        "answer": "12"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hình thang cân $ABCD$ ($AB \\parallel CD$) có hai đường chéo $AC \\perp BD$. Biết đường cao của hình thang $h = 8\\text{ cm}$. Tính độ dài đường trung bình của hình thang (theo cm).",
        "answer": "8"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$). Biết $\\widehat{A} = 2\\widehat{D}$.\na) Tính số đo các góc của hình thang cân.\nb) Chứng minh rằng $AD = BC$ và $AC = BD$.",
        "rubric": "a) Vì AB // CD nên góc A + góc D = 180° (hai góc trong cùng phía) (0.25đ)\nThay góc A = 2.góc D: 3.góc D = 180° => góc D = 60° => góc A = 120° (0.25đ)\nDo ABCD là hình thang cân nên góc C = góc D = 60° và góc B = góc A = 120° (0.25đ)\nb) Theo định nghĩa và tính chất của hình thang cân: hai cạnh bên bằng nhau AD = BC, hai đường chéo bằng nhau AC = BD (0.25đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ cân tại $A$. Trên các cạnh bên $AB, AC$ lần lượt lấy các điểm $M, N$ sao cho $BM = CN$.\na) Chứng minh tứ giác $BMNC$ là hình thang cân.\nb) Biết $\\widehat{A} = 50^\\circ$, tính số đo các góc của hình thang cân $BMNC$.",
        "rubric": "a) Vì tam giác ABC cân tại A nên AB = AC. Lại có BM = CN nên AM = AN => tam giác AMN cân tại A (0.25đ)\nDo đó góc AMN = (180° - góc A)/2 = góc B => MN // BC (hai góc đồng vị bằng nhau) => BMNC là hình thang (0.25đ)\nHình thang BMNC có hai góc kề đáy góc B = góc C nên là hình thang cân (0.25đ)\nb) Góc B = góc C = (180° - 50°)/2 = 65° => góc BMN = góc MNC = 180° - 65° = 115° (0.25đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình thang cân $ABCD$ ($AB \\parallel CD, AB < CD$). Kẻ các đường cao $AH, BK$ xuống đáy $CD$.\na) Chứng minh rằng $DH = CK = \\frac{CD - AB}{2}$.\nb) Cho $AB = 6\\text{ cm}, CD = 14\\text{ cm}$ và $AD = 5\\text{ cm}$. Tính độ dài đường cao $AH$ và diện tích hình thang $ABCD$.",
        "rubric": "a) Tam giác vuông AHD = tam giác vuông BKC (cạnh huyền - góc nhọn: AD = BC, góc D = góc C) => DH = CK (0.25đ)\nTứ giác ABKH có AB // HK và AH // BK (cùng vuông góc CD) nên AB = HK. Ta có CD = DH + HK + KC = 2DH + AB => DH = (CD - AB)/2 (0.25đ)\nb) DH = (14 - 6)/2 = 4 cm (0.25đ)\nTrong tam giác vuông AHD: AH² = AD² - DH² = 5² - 4² = 9 => AH = 3 cm.\nDiện tích hình thang: S = (AB + CD) . AH / 2 = (6 + 14) . 3 / 2 = 30 cm² (0.25đ)"
      }
    ]
  },
  "c3_8_bai2_test2": {
    "title": "Toán 8 (KNTT) - Bài 11: Hình thang cân - Bài kiểm tra số 2 (⚡ Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Dấu hiệu nào sau đây không dùng để nhận biết hình thang cân?",
        "options": [
          "Hình thang có hai cạnh bên bằng nhau",
          "Hình thang có hai góc kề một đáy bằng nhau",
          "Hình thang có hai đường chéo bằng nhau",
          "Tứ giác có hai đường chéo bằng nhau và hai cạnh đối song song"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$). Gọi $O$ là giao điểm của $AC$ và $BD$. Khẳng định nào đúng?",
        "options": [
          "$OA = OB$ và $OC = OD$",
          "$OA = OD$ và $OB = OC$",
          "$OA = OC$ và $OB = OD$",
          "$OA = OB = OC = OD$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hình thang cân có hai đường chéo:",
        "options": [
          "Bằng nhau",
          "Vuông góc với nhau",
          "Cắt nhau tại trung điểm mỗi đường",
          "Là các đường phân giác của các góc"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hình thang $ABCD$ ($AB \\parallel CD$) có $\\widehat{C} = \\widehat{D} = 80^\\circ$. Tứ giác $ABCD$ là:",
        "options": [
          "Hình thang cân",
          "Hình bình hành",
          "Hình thang vuông",
          "Hình chữ nhật"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Cho hình thang cân $ABCD$ có $\\widehat{A} = 130^\\circ$. Số đo góc đối diện $\\widehat{C}$ bằng:",
        "options": [
          "$50^\\circ$",
          "$130^\\circ$",
          "$65^\\circ$",
          "$70^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trục đối xứng của hình thang cân là:",
        "options": [
          "Đường thẳng đi qua trung điểm hai đáy",
          "Đường chéo của hình thang",
          "Đường cao của hình thang",
          "Đường thẳng chứa cạnh bên"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hình thang cân $ABCD$ ($AB \\parallel CD$) có đường cao $AH = 4\\text{ cm}$, cạnh bên $AD = 5\\text{ cm}$, đáy nhỏ $AB = 3\\text{ cm}$. Đáy lớn $CD$ có độ dài bằng:",
        "options": [
          "$9\\text{ cm}$",
          "$8\\text{ cm}$",
          "$10\\text{ cm}$",
          "$7\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$). Biết $\\widehat{A} = 3\\widehat{D}$. Số đo góc $B$ bằng:",
        "options": [
          "$135^\\circ$",
          "$45^\\circ$",
          "$120^\\circ$",
          "$150^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ đều. Lấy các điểm $D, E$ lần lượt trên các cạnh $AB, AC$ sao cho $BD = CE$. Tứ giác $BDEC$ là:",
        "options": [
          "Hình thang cân",
          "Hình thoi",
          "Hình bình hành",
          "Hình thang vuông"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Hình thang cân có đáy lớn bằng $10\\text{ cm}$, đáy nhỏ bằng một nửa đáy lớn và bằng cạnh bên. Chu vi hình thang cân là:",
        "options": [
          "$25\\text{ cm}$",
          "$30\\text{ cm}$",
          "$20\\text{ cm}$",
          "$35\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD, AB < CD$). Giao điểm $E$ của hai cạnh bên kéo dài $AD$ và $BC$ tạo thành tam giác $ECD$ là:",
        "options": [
          "Tam giác cân tại $E$",
          "Tam giác vuông tại $E$",
          "Tam giác đều",
          "Tam giác vuông cân tại $E$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một hình thang cân có góc nhọn bằng $45^\\circ$, cạnh bên bằng $4\\sqrt{2}\\text{ cm}$, đáy nhỏ bằng $5\\text{ cm}$. Đáy lớn có độ dài là:",
        "options": [
          "$13\\text{ cm}$",
          "$9\\text{ cm}$",
          "$11\\text{ cm}$",
          "$15\\text{ cm}$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình thang cân $ABCD$ ($AB \\parallel CD, AB < CD$). Hai đường chéo $AC$ và $BD$ cắt nhau tại điểm $O$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tam giác $OAB$ và tam giác $OCD$ đều là các tam giác cân tại $O$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Hai đoạn thẳng $OA = OB$ và $OC = OD$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Hai tam giác $OAD$ và $OBC$ có diện tích bằng nhau.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng nối trung điểm của $AB$ và $CD$ luôn đi qua điểm $O$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình thang cân $ABCD$ có đáy nhỏ $AB = 8\\text{ cm}$, đáy lớn $CD = 20\\text{ cm}$, đường cao $AH = 8\\text{ cm}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $DH = 6\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài cạnh bên $AD = 10\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Diện tích hình thang cân $ABCD$ bằng $112\\text{ cm}^2$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Độ dài đường chéo $AC$ lớn hơn $18\\text{ cm}$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$) có $\\widehat{C} = 55^\\circ$. Tính hiệu số đo giữa góc $A$ và góc $C$ (theo độ).",
        "answer": "70"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Hình thang cân $ABCD$ có góc nhọn bằng $60^\\circ$, cạnh bên bằng $8\\text{ cm}$ và đáy nhỏ $AB = 6\\text{ cm}$. Tính độ dài đáy lớn $CD$ (theo cm).",
        "answer": "14"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang cân $ABCD$ có diện tích $45\\text{ cm}^2$, đường cao $h = 5\\text{ cm}$. Biết đáy lớn hơn đáy nhỏ $4\\text{ cm}$. Tính độ dài đáy lớn (theo cm).",
        "answer": "11"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình thang cân $ABCD$ có đường chéo $AC$ vuông góc với cạnh bên $BC$. Biết $AB = 6\\text{ cm}, CD = 10\\text{ cm}$. Tính độ dài cạnh bên $AD$ (theo cm).",
        "answer": "4"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ cân tại $A$. Gọi $D, E$ lần lượt là trung điểm của $AB$ và $AC$.\na) Chứng minh tứ giác $BDEC$ là hình thang cân.\nb) Biết $\\widehat{BAC} = 70^\\circ$, tính số đo các góc của tứ giác $BDEC$.",
        "rubric": "a) D, E là trung điểm của AB, AC nên DE là đường trung bình của tam giác ABC => DE // BC => BDEC là hình thang (0.25đ)\nTam giác ABC cân tại A => góc B = góc C => BDEC là hình thang cân (0.25đ)\nb) Góc B = góc C = (180° - 70°)/2 = 55° (0.25đ)\nDo DE // BC => góc BDE = góc CED = 180° - 55° = 125° (0.25đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Hai đường phân giác của góc $A$ và góc $D$ cắt nhau tại điểm $I$ thuộc cạnh bên $BC$.\na) Chứng minh tam giác $AID$ vuông tại $I$.\nb) Chứng minh $AD = AB + CD$.",
        "rubric": "a) AB // CD => góc BAD + góc ADC = 180° (hai góc trong cùng phía) (0.25đ)\nAI và DI là phân giác => góc IAD + góc IDA = (góc BAD + góc ADC)/2 = 90° => tam giác AID vuông tại I (0.25đ)\nb) Kéo dài AI cắt DC tại K. AB // DK => góc BIA... => AD = DK = CD + CK = CD + AB (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình thang cân $ABCD$ ($AB \\parallel CD, AB < CD$) có hai đường chéo $AC$ và $BD$ vuông góc với nhau tại $O$.\na) Chứng minh rằng đường cao của hình thang bằng nửa tổng hai đáy: $h = \\frac{AB + CD}{2}$.\nb) Biết $AB = 5\\text{ cm}, CD = 11\\text{ cm}$. Tính diện tích hình thang cân $ABCD$.",
        "rubric": "a) Tam giác OAB vuông cân tại O => đường cao OH1 = AB/2 (0.25đ)\nTam giác OCD vuông cân tại O => đường cao OH2 = CD/2 (0.25đ)\nĐường cao của hình thang là h = OH1 + OH2 = (AB + CD)/2 (0.25đ)\nb) Chiều cao h = (5 + 11)/2 = 8 cm. Diện tích hình thang S = (AB + CD) . h / 2 = 16 . 8 / 2 = 64 cm² (0.25đ)"
      }
    ]
  },
  "c3_8_bai2_test3": {
    "title": "Toán 8 (KNTT) - Bài 11: Hình thang cân - Bài kiểm tra số 3 (🔥 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Một hình thang có hai đường chéo bằng nhau thì chắc chắn là:",
        "options": [
          "Hình thang cân",
          "Hình chữ nhật",
          "Hình bình hành",
          "Hình thoi"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$). Kết luận nào sau đây luôn đúng?",
        "options": [
          "$\\triangle ACD = \\triangle BDC$",
          "$\\triangle AOB = \\triangle COD$",
          "$AB = CD$",
          "$AD \\parallel BC$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hình thang cân có góc kề đáy lớn bằng $45^\\circ$ thì góc kề đáy nhỏ bằng:",
        "options": [
          "$135^\\circ$",
          "$45^\\circ$",
          "$90^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Điều kiện cần và đủ để một hình thang là hình thang cân là:",
        "options": [
          "Có hai góc kề một đáy bằng nhau",
          "Có hai cạnh bên bằng nhau",
          "Có hai đáy bằng nhau",
          "Có một góc vuông"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tứ giác có hai cạnh đối song song và hai góc đối bù nhau là:",
        "options": [
          "Hình thang cân",
          "Hình thoi",
          "Hình bình hành",
          "Hình vuông"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Đường thẳng nối trung điểm hai đáy của hình thang cân:",
        "options": [
          "Vuông góc với hai đáy",
          "Bằng hai cạnh bên",
          "Bằng nửa tổng hai đáy",
          "Song song với hai cạnh bên"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hình thang cân $ABCD$ có đường chéo $BD$ vuông góc với cạnh bên $BC$, $\\widehat{BCD} = 60^\\circ$. Khẳng định nào sau đây đúng?",
        "options": [
          "$CD = 2AB$",
          "$CD = 3AB$",
          "$CD = 1.5AB$",
          "$CD = 4AB$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một hình thang cân có đáy nhỏ bằng $6\\text{ cm}$, cạnh bên bằng $5\\text{ cm}$, góc ở đáy lớn bằng $60^\\circ$. Chu vi hình thang là:",
        "options": [
          "$27\\text{ cm}$",
          "$26\\text{ cm}$",
          "$28\\text{ cm}$",
          "$30\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$). Gọi $M, N$ lần lượt là trung điểm của $AD, BC$. Khẳng định nào sau đây là sai?",
        "options": [
          "$MN = AD$",
          "$MN \\parallel AB \\parallel CD$",
          "$MN = \\frac{AB + CD}{2}$",
          "Đoạn thẳng nối trung điểm 2 đáy cắt $MN$ tại trung điểm của $MN$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Hình thang cân có hai đường chéo vuông góc và độ dài đường cao là $h$. Diện tích của hình thang cân này bằng:",
        "options": [
          "$h^2$",
          "$2h^2$",
          "$\\frac{1}{2}h^2$",
          "$4h^2$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$) có $AC = 13\\text{ cm}$, đường cao $AH = 12\\text{ cm}$. Tổng độ dài hai đáy $AB + CD$ bằng:",
        "options": [
          "$10\\text{ cm}$",
          "$12\\text{ cm}$",
          "$15\\text{ cm}$",
          "$8\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{C} = \\widehat{D}$ và $AD = BC$. Khẳng định nào đúng nhất?",
        "options": [
          "Tứ giác $ABCD$ là hình thang cân hoặc hình bình hành",
          "Tứ giác $ABCD$ chắc chắn là hình thang cân",
          "Tứ giác $ABCD$ chắc chắn là hình chữ nhật",
          "Tứ giác $ABCD$ là hình thang vuông"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình thang cân $ABCD$ ($AB \\parallel CD, AB < CD$) có hai đường chéo $AC$ và $BD$ vuông góc với nhau. Gọi $H$ là chân đường cao kẻ từ $A$ xuống $CD$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $HC$ bằng chiều cao $AH$ của hình thang.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $HC = \\frac{AB + CD}{2}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Diện tích hình thang cân $ABCD$ đúng bằng diện tích hình vuông có cạnh là $AH$ ($S = AH^2$).",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Nếu $AH = 10\\text{ cm}$ thì diện tích hình thang cân bằng $200\\text{ cm}^2$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ nhọn có các đường cao $BD$ và $CE$ cắt nhau tại $H$. Gọi $M$ và $N$ lần lượt là điểm đối xứng của $H$ qua $AC$ và $AB$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác có 4 điểm $B, C, D, E$ cùng nằm trên một đường tròn.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $ED$ song song với tiếp tuyến tại $A$ của đường tròn ngoại tiếp tam giác $ABC$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tứ giác $BCDE$ là hình thang cân khi và chỉ khi tam giác $ABC$ cân tại $A$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Diện tích tứ giác $BCDE$ luôn lớn hơn diện tích tam giác $ADE$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$) có $AB = 7\\text{ cm}, CD = 17\\text{ cm}$ và chiều cao $h = 12\\text{ cm}$. Tính độ dài đường chéo $AC$ (theo cm).",
        "answer": "13"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Một hình thang cân có đáy lớn $CD = 24\\text{ cm}$, đường chéo vuông góc với cạnh bên, góc nhọn của hình thang bằng $60^\\circ$. Tính độ dài cạnh bên (theo cm).",
        "answer": "12"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một hình thang cân có hai đường chéo vuông góc với nhau và diện tích bằng $100\\text{ cm}^2$. Tính độ dài đường cao của hình thang (theo cm).",
        "answer": "10"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình thang cân $ABCD$ có $AB = 4\\text{ cm}, CD = 10\\text{ cm}, AD = 5\\text{ cm}$. Điểm $M$ nằm trên đáy $CD$ sao cho chu vi tam giác $ADM$ bằng chu vi tứ giác $ABCM$. Tính độ dài đoạn thẳng $DM$ (theo cm).",
        "answer": "7"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD, AB < CD$). Đường chéo $BD$ vuông góc với cạnh bên $BC$. Biết $\\widehat{BCD} = 60^\\circ$.\na) Chứng minh tam giác $BCD$ là nửa tam giác đều và $CD = 2BC$.\nb) Chứng minh rằng $BC = AB$.",
        "rubric": "a) Tam giác BCD vuông tại B có góc C = 60° => góc BDC = 30°. Do đó BC = CD/2 <=> CD = 2BC (0.5đ)\nb) Góc ADC = góc BCD = 60°. Lại có góc BDC = 30° => góc ADB = 30°.\nMặt khác AB // CD => góc ABD = góc BDC = 30° (so le trong).\nTam giác ABD có góc ADB = góc ABD = 30° nên tam giác ABD cân tại A => AB = AD. Mà AD = BC (hình thang cân) => AB = BC (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ có ba góc nhọn, các đường cao $BD$ và $CE$.\na) Chứng minh tứ giác $BEDC$ có các điểm $B, C, D, E$ cùng cách đều trung điểm $M$ của $BC$.\nb) Gọi $K, L$ lần lượt là hình chiếu của $B, C$ lên đường thẳng $ED$. Chứng minh rằng $EK = DL$.",
        "rubric": "a) Tam giác BEC vuông tại E, M là trung điểm BC => ME = BC/2. Tam giác BDC vuông tại D, M là trung điểm BC => MD = BC/2. Do đó MB = MC = ME = MD = BC/2 (0.5đ)\nb) Tứ giác BKL C là hình thang vuông (BK // CL cùng vuông góc KL). Đoạn MI nối M với trung điểm I của KL là đường trung bình => I là trung điểm KL. Tam giác MED cân tại M => MI cũng vuông góc ED => I là trung điểm ED => IK = IL và IE = ID => EK = DL (ĐPCM) (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình thang cân $ABCD$ ($AB \\parallel CD$). Gọi $E, F, G, H$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$.\na) Chứng minh rằng tứ giác $EFGH$ là hình thoi.\nb) Hình thang cân $ABCD$ cần thêm điều kiện gì đối với hai đường chéo $AC$ và $BD$ để tứ giác $EFGH$ là hình vuông?",
        "rubric": "a) EF là đường trung bình tam giác ABC => EF // AC và EF = AC/2.\nHG là đường trung bình tam giác ADC => HG // AC và HG = AC/2.\n=> EF // HG và EF = HG => EFGH là hình bình hành (0.25đ)\nMặt khác EH = BD/2. Vì ABCD là hình thang cân nên AC = BD => EF = EH.\nHình bình hành EFGH có hai cạnh kề bằng nhau nên là hình thoi (0.5đ)\nb) Để hình thoi EFGH là hình vuông thì cần góc E = 90° <=> EF vuông góc EH <=> AC vuông góc BD.\nVậy hình thang cân ABCD cần có hai đường chéo vuông góc với nhau thì EFGH là hình vuông (0.25đ)"
      }
    ]
  },
  "c3_8_bai3_test1": {
    "title": "Toán 8 (KNTT) - Bài 12: Hình bình hành - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hình bình hành là tứ giác có:",
        "options": [
          "Các cạnh đối song song",
          "Bốn cạnh bằng nhau",
          "Bốn góc vuông",
          "Hai đường chéo vuông góc"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong hình bình hành, tính chất nào sau đây là sai?",
        "options": [
          "Hai đường chéo bằng nhau",
          "Các cạnh đối bằng nhau",
          "Các góc đối bằng nhau",
          "Hai đường chéo cắt nhau tại trung điểm của mỗi đường"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho hình bình hành $ABCD$ có $\\widehat{A} = 70^\\circ$. Số đo góc $C$ bằng:",
        "options": [
          "$70^\\circ$",
          "$110^\\circ$",
          "$140^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Cho hình bình hành $ABCD$ có $\\widehat{A} = 100^\\circ$. Số đo góc $B$ bằng:",
        "options": [
          "$80^\\circ$",
          "$100^\\circ$",
          "$90^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Hình bình hành có bao nhiêu tâm đối xứng?",
        "options": [
          "$1$",
          "$2$",
          "$0$",
          "Vô số"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tâm đối xứng của hình bình hành là:",
        "options": [
          "Giao điểm của hai đường chéo",
          "Trung điểm của cạnh đáy",
          "Giao điểm của hai đường cao",
          "Một đỉnh bất kì"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$ có $AB = 7\\text{ cm}, BC = 5\\text{ cm}$. Chu vi hình bình hành $ABCD$ bằng:",
        "options": [
          "$24\\text{ cm}$",
          "$12\\text{ cm}$",
          "$35\\text{ cm}$",
          "$20\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Dấu hiệu nào sau đây không kết luận được một tứ giác là hình bình hành?",
        "options": [
          "Tứ giác có hai cạnh đối bằng nhau",
          "Tứ giác có các cạnh đối song song",
          "Tứ giác có hai cạnh đối song song và bằng nhau",
          "Tứ giác có hai đường chéo cắt nhau tại trung điểm mỗi đường"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$ có hai đường chéo cắt nhau tại $O$. Biết $AC = 10\\text{ cm}, BD = 14\\text{ cm}$. Độ dài $OA + OB$ bằng:",
        "options": [
          "$12\\text{ cm}$",
          "$24\\text{ cm}$",
          "$7\\text{ cm}$",
          "$10\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Hình bình hành $ABCD$ có $\\widehat{A} = 2\\widehat{B}$. Số đo góc $A$ bằng:",
        "options": [
          "$120^\\circ$",
          "$60^\\circ$",
          "$90^\\circ$",
          "$100^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Gọi $M, N$ lần lượt là trung điểm của $AB, AC$. Lấy $P$ đối xứng với $M$ qua $N$. Tứ giác $AMCP$ là:",
        "options": [
          "Hình bình hành",
          "Hình chữ nhật",
          "Hình thoi",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hình bình hành $ABCD$ có $AB = 2AD$ và chu vi bằng $36\\text{ cm}$. Độ dài cạnh $AD$ bằng:",
        "options": [
          "$6\\text{ cm}$",
          "$12\\text{ cm}$",
          "$9\\text{ cm}$",
          "$4\\text{ cm}$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình bình hành $ABCD$ có $\\widehat{A} = 110^\\circ$. Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Số đo góc $C = 110^\\circ$ và số đo góc $B = 70^\\circ$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $OA = OC$ và $OB = OD$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Đường chéo $AC$ luôn bằng đường chéo $BD$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Hai tam giác $OAB$ và $OCD$ bằng nhau.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một mảnh vườn hình bình hành $ABCD$ có cạnh $AB = 25\\text{ m}$, chiều cao tương ứng với cạnh $AB$ là $h = 12\\text{ m}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Diện tích của mảnh vườn bằng $300\\text{ m}^2$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Cạnh đối diện $CD$ có độ dài bằng $25\\text{ m}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Nếu cạnh $BC = 15\\text{ m}$ thì chu vi mảnh vườn bằng $80\\text{ m}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Chiều cao ứng với cạnh $BC$ là $25\\text{ m}$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$ có $\\widehat{A} = 3\\widehat{B}$. Tính số đo góc $A$ (theo độ).",
        "answer": "135"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Hình bình hành $ABCD$ có chu vi $48\\text{ cm}$, cạnh $AB$ dài hơn cạnh $BC$ là $4\\text{ cm}$. Tính độ dài cạnh $AB$ (theo cm).",
        "answer": "14"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho hình bình hành $ABCD$ có hai đường chéo cắt nhau tại $O$. Biết chu vi tam giác $AOB$ bằng $18\\text{ cm}$, $AB = 7\\text{ cm}$. Tính tổng độ dài hai đường chéo $AC + BD$ (theo cm).",
        "answer": "22"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình bình hành $ABCD$ có diện tích $72\\text{ cm}^2$. Gọi $M$ là trung điểm của cạnh $CD$. Tính diện tích tam giác $ABM$ (theo cm²).",
        "answer": "36"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$. Lấy điểm $E$ trên cạnh $AB$ và điểm $F$ trên cạnh $CD$ sao cho $AE = CF$.\na) Chứng minh tứ giác $AECF$ là hình bình hành.\nb) Chứng minh đoạn thẳng $EF$ đi qua trung điểm của đường chéo $AC$.",
        "rubric": "a) ABCD là hình bình hành => AB // CD => AE // CF (0.25đ)\nMặt khác AE = CF (gt). Tứ giác AECF có hai cạnh đối song song và bằng nhau nên là hình bình hành (0.25đ)\nb) Trong hình bình hành AECF, hai đường chéo AC và EF cắt nhau tại trung điểm của mỗi đường => EF đi qua trung điểm của AC (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Gọi $M$ là trung điểm của cạnh $BC$. Trên tia đối của tia $MA$ lấy điểm $D$ sao cho $MD = MA$.\na) Chứng minh tứ giác $ABDC$ là hình bình hành.\nb) Lấy điểm $E$ trên cạnh $AB$, $F$ trên cạnh $CD$ sao cho $BE = CF$. Chứng minh ba điểm $E, M, F$ thẳng hàng.",
        "rubric": "a) Tứ giác ABDC có hai đường chéo BC và AD cắt nhau tại trung điểm M của mỗi đường => ABDC là hình bình hành (0.5đ)\nb) Tứ giác EBFD có BE // DF và BE = CF... Hoặc tam giác BEM = tam giác CFM (c-g-c) => góc BME = góc CMF. Vì B, M, C thẳng hàng nên E, M, F thẳng hàng (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình bình hành $ABCD$. Kẻ $AH$ vuông góc với đường chéo $BD$ tại $H$ và $CK$ vuông góc với đường chéo $BD$ tại $K$.\na) Chứng minh rằng $AH = CK$ và tứ giác $AHCK$ là hình bình hành.\nb) Gọi $O$ là giao điểm của $AC$ và $BD$. Chứng minh ba điểm $H, O, K$ thẳng hàng và $O$ là trung điểm của $HK$.",
        "rubric": "a) Tam giác vuông AHB = tam giác vuông CKD (cạnh huyền - góc nhọn: AB = CD, góc ABH = góc CDK do so le trong) => AH = CK (0.25đ)\nMặt khác AH vuông góc BD và CK vuông góc BD => AH // CK. Tứ giác AHCK có AH // CK và AH = CK nên là hình bình hành (0.25đ)\nb) Trong hình bình hành AHCK, hai đường chéo AC và HK cắt nhau tại trung điểm mỗi đường. Mà O là trung điểm AC (do ABCD là HBH) => O cũng là trung điểm của HK => H, O, K thẳng hàng và OH = OK (0.5đ)"
      }
    ]
  },
  "c3_8_bai3_test2": {
    "title": "Toán 8 (KNTT) - Bài 12: Hình bình hành - Bài kiểm tra số 2 (⚡ Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tứ giác nào sau đây không nhất thiết là hình bình hành?",
        "options": [
          "Tứ giác có hai cạnh đối bằng nhau",
          "Tứ giác có các cạnh đối bằng nhau",
          "Tứ giác có hai cạnh đối song song và bằng nhau",
          "Tứ giác có các góc đối bằng nhau"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho hình bình hành $ABCD$. Tia phân giác của góc $A$ cắt $BC$ tại $E$. Tam giác $ABE$ là tam giác:",
        "options": [
          "Tam giác cân tại $B$",
          "Tam giác đều",
          "Tam giác vuông tại $E$",
          "Tam giác tù"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Giao điểm của hai đường chéo hình bình hành chia mỗi đường chéo thành:",
        "options": [
          "Hai đoạn thẳng bằng nhau",
          "Hai đoạn thẳng tỉ lệ $1 : 2$",
          "Hai đoạn thẳng vuông góc",
          "Hai đoạn thẳng bất kì"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Cho hình bình hành $ABCD$ có $\\widehat{A} - \\widehat{B} = 40^\\circ$. Số đo góc $A$ bằng:",
        "options": [
          "$110^\\circ$",
          "$70^\\circ$",
          "$120^\\circ$",
          "$100^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tứ giác có hai đường chéo cắt nhau tại trung điểm của mỗi đường là dấu hiệu nhận biết của:",
        "options": [
          "Hình bình hành",
          "Hình thang cân",
          "Hình thang vuông",
          "Tứ giác bất kì"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hình bình hành có hai cạnh kề bằng nhau là:",
        "options": [
          "Hình thoi",
          "Hình chữ nhật",
          "Hình vuông",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$ có $AB = 8\\text{ cm}, AD = 5\\text{ cm}$. Kẻ phân giác góc $A$ cắt cạnh $CD$ tại $E$. Độ dài đoạn thẳng $EC$ là:",
        "options": [
          "$3\\text{ cm}$",
          "$4\\text{ cm}$",
          "$5\\text{ cm}$",
          "$2.5\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$. Lấy $M, N$ lần lượt là trung điểm của $AB$ và $CD$. Tứ giác $AMND$ là:",
        "options": [
          "Hình bình hành",
          "Hình thang vuông",
          "Hình chữ nhật",
          "Hình thoi"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$ có hai đường chéo $AC = 12\\text{ cm}, BD = 16\\text{ cm}$ cắt nhau tại $O$. Biết $AB = 10\\text{ cm}$. Tam giác $OAB$ là:",
        "options": [
          "Tam giác vuông tại $O$",
          "Tam giác cân tại $O$",
          "Tam giác đều",
          "Tam giác tù"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Chu vi hình bình hành bằng $60\\text{ cm}$. Tỉ số giữa hai cạnh kề là $2 : 3$. Độ dài hai cạnh kề là:",
        "options": [
          "$12\\text{ cm}$ và $18\\text{ cm}$",
          "$10\\text{ cm}$ và $20\\text{ cm}$",
          "$15\\text{ cm}$ và $15\\text{ cm}$",
          "$8\\text{ cm}$ và $22\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Qua $A$ kẻ đường thẳng song song với $BC$, qua $C$ kẻ đường thẳng song song với $AB$, chúng cắt nhau tại $D$. Tứ giác $ABDC$ là:",
        "options": [
          "Hình bình hành",
          "Hình thang",
          "Hình thang cân",
          "Hình thoi"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$. Các đường phân giác của bốn góc $A, B, C, D$ cắt nhau tạo thành một tứ giác. Tứ giác đó là:",
        "options": [
          "Hình chữ nhật",
          "Hình thoi",
          "Hình bình hành",
          "Hình vuông"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình bình hành $ABCD$. Gọi $M, N$ lần lượt là trung điểm của các cạnh $AB$ và $CD$. Đường chéo $BD$ cắt $AN$ và $CM$ lần lượt tại $E$ và $F$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $AMCN$ là một hình bình hành.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Hai đoạn thẳng $AN$ và $CM$ song song với nhau ($AN \\parallel CM$).",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Các đoạn thẳng trên đường chéo $BD$ bằng nhau: $DE = EF = FB$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Độ dài đoạn thẳng $EF$ bằng một nửa đường chéo $BD$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ có đường trung tuyến $AM$. Gọi $I$ là trung điểm của $AM$. Tia $CI$ cắt cạnh $AB$ tại điểm $D$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Kẻ $ME \\parallel CD$ ($E \\in AB$) thì $E$ là trung điểm của đoạn thẳng $BD$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $AD = DE = EB$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Điểm $D$ là trung điểm của cạnh $AB$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Độ dài $CD = 4 \\cdot ID$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$ có $\\widehat{A} = 125^\\circ$. Tính hiệu số đo giữa góc $A$ và góc kề bù với góc $B$ (theo độ).",
        "answer": "0"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Hình bình hành $ABCD$ có $AB = 10\\text{ cm}$. Phân giác góc $A$ cắt $BC$ tại $E$ sao cho $BE = 2EC$. Tính chu vi hình bình hành (theo cm).",
        "answer": "30"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho hình bình hành $ABCD$ có diện tích $60\\text{ cm}^2$. Điểm $O$ là giao điểm hai đường chéo. Tính diện tích tam giác $OAB$ (theo cm²).",
        "answer": "15"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình bình hành $ABCD$ có hai đường chéo $AC = 8\\text{ cm}, BD = 6\\text{ cm}$ vuông góc với nhau. Tính chu vi hình bình hành (theo cm).",
        "answer": "20"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$. Trên đường chéo $BD$ lấy hai điểm $M$ và $N$ sao cho $BM = DN < \\frac{1}{2}BD$.\na) Chứng minh tam giác $ABM$ bằng tam giác $CDN$.\nb) Chứng minh tứ giác $AMCN$ là hình bình hành.",
        "rubric": "a) Xét tam giác ABM và CDN: AB = CD (tính chất HBH), BM = DN (gt), góc ABM = góc CDN (hai góc so le trong của AB // CD) => tam giác ABM = tam giác CDN (c-g-c) (0.5đ)\nb) Từ câu a suy ra AM = CN. Tương tự tam giác AMD = tam giác CNB => AN = CM. Tứ giác AMCN có các cạnh đối bằng nhau nên là hình bình hành (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ nhọn. Vẽ ra phía ngoài tam giác các tam giác vuông cân tại $A$ là $\\triangle ABD$ và $\\triangle ACE$ (với $\\widehat{ABD} = \\widehat{ACE} = 90^\\circ$ hoặc góc vuông tại $A$ là $\\widehat{BAD} = \\widehat{CAE} = 90^\\circ$). Kẻ đường cao $AH$ của $\\triangle ABC$. Gọi $M$ là trung điểm của $DE$. Chứng minh $AM$ vuông góc với $BC$.",
        "rubric": "Vẽ hình bình hành ADKE. Khi đó M là trung điểm AK. Ta có AD = AB, AE = AC, góc DAE + góc BAC = 180° => tam giác ADE và tam giác ABC có mối liên hệ đặc biệt (0.5đ)\nChứng minh tam giác ADK bằng tam giác BAC => góc MAK + góc B = 90° => AM vuông góc BC (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình bình hành $ABCD$. Một đường thẳng $d$ đi qua đỉnh $A$ cắt đường chéo $BD$ tại $P$, cắt cạnh $BC$ tại $Q$ và cắt tia đối của tia $CD$ tại $R$.\na) Chứng minh rằng: $AP^2 = PQ \\cdot PR$.\nb) Khi đường thẳng $d$ quay quanh $A$, tích $BP \\cdot DP$ đạt giá trị lớn nhất khi nào?",
        "rubric": "a) Vì AD // BC (ABCD là HBH) nên theo định lý Thalès: AP/PQ = DP/PB (0.25đ)\nVì AB // CD nên: PR/AP = DP/PB (0.25đ)\nSuy ra AP/PQ = PR/AP <=> AP² = PQ . PR (ĐPCM) (0.25đ)\nb) Ta có P nằm trên đoạn BD. BP + DP = BD (không đổi). Tích BP . DP lớn nhất khi BP = DP = BD/2, tức là P là trung điểm của BD (giao điểm 2 đường chéo) (0.25đ)"
      }
    ]
  },
  "c3_8_bai3_test3": {
    "title": "Toán 8 (KNTT) - Bài 12: Hình bình hành - Bài kiểm tra số 3 (🔥 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khẳng định nào sau đây là điều kiện cần và đủ để một tứ giác là hình bình hành?",
        "options": [
          "Có các cặp cạnh đối song song",
          "Có hai góc kề bù nhau",
          "Có hai đường chéo bằng nhau",
          "Có một cặp cạnh đối bằng nhau"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hình bình hành có hai đường chéo bằng nhau là hình gì?",
        "options": [
          "Hình chữ nhật",
          "Hình thoi",
          "Hình vuông",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Định lí Varignon phát biểu rằng tứ giác có 4 đỉnh là trung điểm các cạnh của một tứ giác lồi bất kì luôn là:",
        "options": [
          "Hình bình hành",
          "Hình chữ nhật",
          "Hình thoi",
          "Hình thang"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong các hình sau, hình nào không có tâm đối xứng?",
        "options": [
          "Hình thang cân",
          "Hình bình hành",
          "Hình chữ nhật",
          "Hình thoi"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Cho hình bình hành $ABCD$. Tổng bình phương độ dài hai đường chéo $AC^2 + BD^2$ bằng:",
        "options": [
          "$2(AB^2 + BC^2)$",
          "$AB^2 + BC^2 + CD^2 + DA^2$",
          "$4AB \\cdot BC$",
          "$2(AB + BC)^2$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nếu một hình bình hành có một góc vuông thì các góc còn lại:",
        "options": [
          "Đều là góc vuông",
          "Có hai góc tù",
          "Có hai góc nhọn",
          "Không xác định"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$. Lấy $E$ đối xứng với $A$ qua $B$, lấy $F$ đối xứng với $B$ qua $C$. Tỉ số diện tích $\\frac{S_{DEF}}{S_{ABCD}}$ bằng:",
        "options": [
          "$1.5$",
          "$2$",
          "$1$",
          "$2.5$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$ có diện tích $S$. Điểm $M$ bất kì nằm trong hình bình hành. Tổng diện tích $S_{MAB} + S_{MCD}$ bằng:",
        "options": [
          "$\\frac{1}{2}S$",
          "$\\frac{1}{3}S$",
          "$\\frac{1}{4}S$",
          "Phụ thuộc vào vị trí của $M$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Gọi $G$ là trọng tâm tam giác. Dựng hình bình hành $ABDC$. Khẳng định nào đúng?",
        "options": [
          "Điểm $G$ nằm trên đường chéo $AD$ và $AG = \\frac{1}{3}AD$",
          "Điểm $G$ là giao điểm hai đường chéo",
          "$G$ là trung điểm của $AD$",
          "$AG = \\frac{1}{2}AD$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$ có chu vi $20\\text{ cm}$, đường cao $AH = 3\\text{ cm}$ và $AK = 2\\text{ cm}$ ứng với $CD$ và $BC$. Độ dài cạnh $AB$ là:",
        "options": [
          "$6\\text{ cm}$",
          "$4\\text{ cm}$",
          "$5\\text{ cm}$",
          "$8\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tứ giác $ABCD$ có các trung điểm các cạnh tạo thành một hình chữ nhật. Khi đó hai đường chéo $AC$ và $BD$ của tứ giác $ABCD$ phải:",
        "options": [
          "Vuông góc với nhau",
          "Bằng nhau",
          "Song song với nhau",
          "Cắt nhau tại trung điểm"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$ có góc nhọn $\\widehat{A} = 60^\\circ$, độ dài các cạnh $AB = 8\\text{ cm}, AD = 5\\text{ cm}$. Độ dài đường chéo $BD$ bằng:",
        "options": [
          "$7\\text{ cm}$",
          "$\\sqrt{39}\\text{ cm}$",
          "$8\\text{ cm}$",
          "$6\\text{ cm}$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình bình hành $ABCD$. Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$. Một đường thẳng $d$ đi qua $O$ cắt các cạnh $AB$ và $CD$ lần lượt tại $M$ và $N$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Điểm $O$ là trung điểm của đoạn thẳng $MN$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Hai đoạn thẳng $AM$ và $CN$ bằng nhau ($AM = CN$).",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Đường thẳng $d$ chia hình bình hành $ABCD$ thành hai hình thang có diện tích bằng nhau.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Tứ giác $MBND$ luôn là hình chữ nhật.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình bình hành $ABCD$. Lấy điểm $M$ tùy ý trên cạnh $CD$. Đoạn thẳng $AM$ cắt đường chéo $BD$ tại $P$, đoạn thẳng $BM$ cắt đường chéo $AC$ tại $Q$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Diện tích tam giác $MAB$ bằng một nửa diện tích hình bình hành $ABCD$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng diện tích hai tam giác $S_{MAD} + S_{MBC} = S_{MAB}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Nếu $M$ là trung điểm của $CD$ thì đoạn thẳng $DP = \\frac{1}{3}BD$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Đoạn thẳng nối $P$ và $Q$ luôn song song với cạnh $AB$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$ có $AB = 12\\text{ cm}, BC = 8\\text{ cm}$. Đường phân giác góc $A$ cắt cạnh $CD$ kéo dài tại $E$. Tính độ dài đoạn thẳng $DE$ (theo cm).",
        "answer": "8"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Hình bình hành $ABCD$ có $AB = 6\\text{ cm}, AD = 4\\text{ cm}$ và $\\widehat{BAD} = 150^\\circ$. Tính diện tích hình bình hành (theo cm²).",
        "answer": "12"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hình bình hành $ABCD$ có $AB = 5\\text{ cm}, BC = 3\\text{ cm}$. Tổng bình phương độ dài hai đường chéo $AC^2 + BD^2$ bằng bao nhiêu cm²?",
        "answer": "68"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình bình hành $ABCD$ có diện tích $120\\text{ cm}^2$. Gọi $M$ là điểm trên cạnh $AB$ sao cho $AM = 2MB$, $N$ là trung điểm của $CD$. Tính diện tích tứ giác $AMND$ (theo cm²).",
        "answer": "70"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tứ giác lồi $ABCD$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$.\na) Chứng minh tứ giác $MNPQ$ là hình bình hành (Định lí Varignon).\nb) Chứng minh rằng hai đoạn thẳng $MP$ và $NQ$ cắt nhau tại trung điểm của mỗi đoạn.",
        "rubric": "a) Trong tam giác ABC, MN là đường trung bình => MN // AC và MN = AC/2 (0.25đ)\nTrong tam giác ADC, QP là đường trung bình => QP // AC và QP = AC/2 (0.25đ)\n=> MN // QP và MN = QP => MNPQ là hình bình hành (0.25đ)\nb) Vì MNPQ là hình bình hành nên hai đường chéo MP và NQ cắt nhau tại trung điểm của mỗi đoạn (0.25đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình bình hành $ABCD$. Gọi $E$ là trung điểm của $AD$, $F$ là trung điểm của $BC$. Đường chéo $AC$ cắt $BE$ tại $P$ và cắt $DF$ tại $Q$.\na) Chứng minh tứ giác $BEDF$ là hình bình hành.\nb) Chứng minh $AP = PQ = QC$.",
        "rubric": "a) AD // BC và AD = BC => DE // BF và DE = BF => BEDF là hình bình hành (0.5đ)\nb) Trong tam giác AQD có E là trung điểm AD, EP // DQ => P là trung điểm AQ => AP = PQ (0.25đ)\nTương tự trong tam giác BPC có F là trung điểm BC, FQ // BP => Q là trung điểm PC => PQ = QC. Vậy AP = PQ = QC (0.25đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình bình hành $ABCD$. Lấy điểm $M$ tùy ý trên đường chéo $AC$. Qua $M$ kẻ đường thẳng song song với $AB$ cắt $AD$ tại $E$ và cắt $BC$ tại $F$. Qua $M$ kẻ đường thẳng song song với $AD$ cắt $AB$ tại $H$ và cắt $CD$ tại $K$.\na) Chứng minh rằng diện tích hai hình bình hành $MEAH$ và $MFCK$ bằng nhau: $S_{MEAH} = S_{MFCK}$.\nb) Gọi $S_1 = S_{MEAH}, S_2 = S_{MFCK}$. Chứng minh rằng khi $M$ di chuyển trên $AC$ thì tổng $S_1 + S_2$ đạt giá trị lớn nhất khi nào?",
        "rubric": "a) Đường chéo AC chia HBH thành 2 tam giác bằng nhau: S(ABC) = S(ADC) (0.25đ)\nĐường chéo AM chia HBH AEMH: S(AEM) = S(AHM); đường chéo MC chia HBH MFCK: S(CFM) = S(CKM) (0.25đ)\nTrừ vế với vế: S(MEAH) = S(MFCK) (ĐPCM) (0.25đ)\nb) Đặt AM/AC = k (0 < k < 1). Khi đó S_1 = k(1-k).S_ABCD. Tổng S_1 + S_2 = 2k(1-k).S_ABCD. Áp dụng BĐT Cauchy: k(1-k) <= 1/4 (dấu '=' xảy ra khi k = 1/2). Vậy tổng đạt GTLN bằng S_ABCD / 2 khi M là trung điểm của AC (tâm đối xứng) (0.25đ)"
      }
    ]
  }
};

const EXAMS_8_C3_8 = CHAPTER3_TOAN8_EXAMS;

if (typeof window !== 'undefined') {
  window.CHAPTER3_TOAN8_EXAMS = CHAPTER3_TOAN8_EXAMS;
  window.EXAMS_8_C3_8 = CHAPTER3_TOAN8_EXAMS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CHAPTER3_TOAN8_EXAMS, EXAMS_8_C3_8 };
}
