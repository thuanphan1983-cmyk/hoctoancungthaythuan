// ==============================================================================
// NGÂN HÀNG ĐỀ THI TOÁN 8 (KNTT) - Bài 10: Tứ giác
// Bao gồm 3 đề phân hóa: Đề 1 (Cơ bản) < Đề 2 (Khá) < Đề 3 (Nâng cao)
// Chuẩn ma trận 10 điểm: 12 TN + 2 Đ/S + 4 TLN + 3 Tự luận
// ==============================================================================

const BAI_1_TOAN8_EXAMS = {
  "c3_8_bai1_test1": {
    "title": "Toán 8 (KNTT) - Bài 10: Tứ giác - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tổng số đo bốn góc của một tứ giác lồi bằng:",
        "options": [
          "$360^\\circ$",
          "$270^\\circ$",
          "$180^\\circ$",
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
          "Có hai đường chéo bằng nhau",
          "Luôn nằm trong một nửa mặt phẳng có bờ là đường thẳng chứa bất kì cạnh nào",
          "Có hai góc tù và hai góc nhọn",
          "Có bốn cạnh bằng nhau"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Số đường chéo của một tứ giác lồi là:",
        "options": [
          "$1$",
          "$4$",
          "$2$",
          "$3$"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Góc kề bù với một góc của tứ giác được gọi là:",
        "options": [
          "Góc trong của tứ giác",
          "Góc ngoài của tứ giác",
          "Góc đối của tứ giác",
          "Góc kề của tứ giác"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Một tứ giác có thể có nhiều nhất bao nhiêu góc tù?",
        "options": [
          "$2$",
          "$4$",
          "$1$",
          "$3$"
        ],
        "correct": 3
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tứ giác $ABCD$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = 90^\\circ, \\widehat{C} = 120^\\circ$. Số đo góc ngoài tại đỉnh $D$ bằng:",
        "options": [
          "$100^\\circ$",
          "$80^\\circ$",
          "$90^\\circ$",
          "$110^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 2x, \\widehat{B} = 3x, \\widehat{C} = 4x, \\widehat{D} = x$. Giá trị của $x$ là:",
        "options": [
          "$30^\\circ$",
          "$45^\\circ$",
          "$36^\\circ$",
          "$40^\\circ$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tứ giác $ABCD$ có chu vi $32\\text{ cm}$, biết $AB = 6\\text{ cm}, BC = 8\\text{ cm}, CD = 10\\text{ cm}$. Độ dài cạnh $AD$ là:",
        "options": [
          "$9\\text{ cm}$",
          "$6\\text{ cm}$",
          "$7\\text{ cm}$",
          "$8\\text{ cm}$"
        ],
        "correct": 3
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Trong một tứ giác, khẳng định nào sau đây là luôn đúng?",
        "options": [
          "Tổng 2 góc đối luôn bằng $180^\\circ$",
          "Có nhiều nhất 3 góc nhọn",
          "Cả 4 góc đều phải là góc nhọn",
          "Có ít nhất 2 góc vuông"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$. Khẳng định nào sau đây là đúng theo bất đẳng thức tam giác?",
        "options": [
          "$AC > AB + BC$",
          "$AC \\ge AB + BC$",
          "$AC = AB + BC$",
          "$AC < AB + BC$"
        ],
        "correct": 3
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tổng các góc ngoài tại 4 đỉnh của một tứ giác lồi bằng:",
        "options": [
          "$540^\\circ$",
          "$180^\\circ$",
          "$360^\\circ$",
          "$720^\\circ$"
        ],
        "correct": 2
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
          "$115^\\circ$",
          "$65^\\circ$",
          "$75^\\circ$",
          "$85^\\circ$"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tứ giác $ABCD$ có $\\widehat{A} = \\widehat{C} = 90^\\circ$. Tổng hai góc $\\widehat{B} + \\widehat{D}$ bằng:",
        "options": [
          "$180^\\circ$",
          "$360^\\circ$",
          "$90^\\circ$",
          "$270^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} : \\widehat{B} : \\widehat{C} : \\widehat{D} = 1 : 2 : 3 : 4$. Góc nhỏ nhất của tứ giác bằng:",
        "options": [
          "$54^\\circ$",
          "$72^\\circ$",
          "$36^\\circ$",
          "$18^\\circ$"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tứ giác có hai đường chéo vuông góc với nhau tại trung điểm của mỗi đường là:",
        "options": [
          "Hình chữ nhật",
          "Hình thang vuông",
          "Hình thang cân",
          "Hình thoi"
        ],
        "correct": 3
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong tứ giác lồi $ABCD$, đoạn thẳng nối hai đỉnh đối diện gọi là:",
        "options": [
          "Cạnh bên",
          "Đường chéo",
          "Đường cao",
          "Đường trung tuyến"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nếu một tứ giác có 3 góc vuông thì góc còn lại là:",
        "options": [
          "Góc nhọn",
          "Góc bẹt",
          "Góc tù",
          "Góc vuông"
        ],
        "correct": 3
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tứ giác $ABCD$ có $\\widehat{A} = 80^\\circ, \\widehat{B} = 70^\\circ$, góc ngoài tại đỉnh $C$ bằng $110^\\circ$. Số đo góc $D$ là:",
        "options": [
          "$140^\\circ$",
          "$150^\\circ$",
          "$120^\\circ$",
          "$130^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = \\widehat{B} + 20^\\circ, \\widehat{B} = \\widehat{C} + 10^\\circ, \\widehat{C} = \\widehat{D} + 10^\\circ$. Số đo góc $D$ bằng:",
        "options": [
          "$90^\\circ$",
          "$80^\\circ$",
          "$70^\\circ$",
          "$60^\\circ$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$ của tứ giác $ABCD$. Khẳng định nào sau đây luôn đúng?",
        "options": [
          "$AC + BD = AB + CD$",
          "$AC + BD > AB + BC + CD + DA$",
          "$AC \\cdot BD = AB \\cdot CD$",
          "$AC + BD < AB + BC + CD + DA$"
        ],
        "correct": 3
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tứ giác $ABCD$ có $\\widehat{A} = 120^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = 2\\widehat{D}$. Số đo góc $D$ là:",
        "options": [
          "$60^\\circ$",
          "$50^\\circ$",
          "$53^\\circ 20'$",
          "$45^\\circ$"
        ],
        "correct": 2
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} + \\widehat{B} = 200^\\circ$. Hai tia phân giác của góc $C$ và góc $D$ cắt nhau tại $M$. Số đo góc $CMD$ bằng:",
        "options": [
          "$100^\\circ$",
          "$120^\\circ$",
          "$80^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $AB = BC$ và $CD = DA$. Khi đó đường thẳng $BD$ là:",
        "options": [
          "Đường song song với $AC$",
          "Đường trung trực của đoạn thẳng $AC$",
          "Đoạn thẳng bằng $AC$",
          "Đường phân giác góc $B$ nhưng không vuông góc $AC$"
        ],
        "correct": 1
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
          "$80^\\circ$",
          "$100^\\circ$",
          "$110^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khẳng định nào sau đây là sai khi nói về tứ giác lồi?",
        "options": [
          "Có nhiều nhất 3 góc nhọn",
          "Hai đường chéo luôn cắt nhau tại một điểm nằm trong tứ giác",
          "Tổng 4 góc luôn bằng $360^\\circ$",
          "Có thể có 4 góc tù"
        ],
        "correct": 3
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Góc kề bù của một góc trong tứ giác bằng $135^\\circ$. Góc trong đó là góc:",
        "options": [
          "Bẹt",
          "Vuông",
          "Nhọn",
          "Tù"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Cho tứ giác $ABCD$. Tổng $\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D}$ tính theo độ radian là:",
        "options": [
          "$\\frac{3\\pi}{2}$",
          "$\\pi$",
          "$4\\pi$",
          "$2\\pi$"
        ],
        "correct": 3
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tứ giác có hai đường chéo bằng nhau và cắt nhau tại trung điểm của mỗi đường là:",
        "options": [
          "Hình bình hành",
          "Hình chữ nhật",
          "Hình thoi",
          "Hình thang cân"
        ],
        "correct": 1
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tứ giác có 4 cạnh bằng nhau được gọi là:",
        "options": [
          "Hình thoi",
          "Hình bình hành",
          "Hình thang cân",
          "Hình chữ nhật"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} - \\widehat{B} = 10^\\circ, \\widehat{B} - \\widehat{C} = 10^\\circ, \\widehat{C} - \\widehat{D} = 10^\\circ$. Số đo góc $A$ là:",
        "options": [
          "$95^\\circ$",
          "$110^\\circ$",
          "$105^\\circ$",
          "$100^\\circ$"
        ],
        "correct": 2
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có các tia phân giác của góc $A$ và góc $D$ cắt nhau tại $E$, các tia phân giác của góc $B$ và góc $C$ cắt nhau tại $F$. Tổng $\\widehat{AED} + \\widehat{BFC}$ bằng:",
        "options": [
          "$180^\\circ$",
          "$90^\\circ$",
          "$360^\\circ$",
          "$270^\\circ$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tứ giác lồi $ABCD$ có $\\widehat{A} = 90^\\circ, \\widehat{C} = 90^\\circ$. Các tia phân giác của góc $B$ và góc $D$:",
        "options": [
          "Tạo với nhau một góc $45^\\circ$",
          "Vuông góc với nhau",
          "Song song hoặc trùng nhau",
          "Cắt nhau tại góc $60^\\circ$"
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có độ dài các cạnh thỏa mãn $AB + CD = BC + AD$. Tứ giác này có tính chất:",
        "options": [
          "Là hình thoi",
          "Ngoại tiếp được một đường tròn",
          "Có hai đường chéo bằng nhau",
          "Nội tiếp được một đường tròn"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Độ dài hai đường chéo của tứ giác $ABCD$ là $8\\text{ cm}$ và $12\\text{ cm}$. Đoạn thẳng nối trung điểm hai đường chéo bằng $2\\text{ cm}$. Khẳng định nào đúng?",
        "options": [
          "Hai đường chéo cắt nhau tại trung điểm mỗi đường",
          "Hai đường chéo vuông góc",
          "Tứ giác $ABCD$ là hình bình hành",
          "Tứ giác $ABCD$ không thể là hình bình hành"
        ],
        "correct": 3
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $AC = 10\\text{ cm}, BD = 14\\text{ cm}$. Diện tích lớn nhất của tứ giác $ABCD$ bằng:",
        "options": [
          "$70\\text{ cm}^2$",
          "$24\\text{ cm}^2$",
          "$140\\text{ cm}^2$",
          "$35\\text{ cm}^2$"
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
  }
};

if (typeof window !== 'undefined') {
  window.CHAPTER3_TOAN8_EXAMS = window.CHAPTER3_TOAN8_EXAMS || {};
  Object.assign(window.CHAPTER3_TOAN8_EXAMS, BAI_1_TOAN8_EXAMS);
  window.EXAMS_8_C3_8 = window.CHAPTER3_TOAN8_EXAMS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BAI_1_TOAN8_EXAMS;
}
