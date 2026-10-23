// ==============================================================================
// NGÂN HÀNG ĐỀ THI TOÁN 8 (KNTT) - Bài 11: Hình thang cân
// Bao gồm 3 đề phân hóa: Đề 1 (Cơ bản) < Đề 2 (Khá) < Đề 3 (Nâng cao)
// Chuẩn ma trận 10 điểm: 12 TN + 2 Đ/S + 4 TLN + 3 Tự luận
// ==============================================================================

const BAI_2_TOAN8_EXAMS = {
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
  }
};

if (typeof window !== 'undefined') {
  window.CHAPTER3_TOAN8_EXAMS = window.CHAPTER3_TOAN8_EXAMS || {};
  Object.assign(window.CHAPTER3_TOAN8_EXAMS, BAI_2_TOAN8_EXAMS);
  window.EXAMS_8_C3_8 = window.CHAPTER3_TOAN8_EXAMS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BAI_2_TOAN8_EXAMS;
}
