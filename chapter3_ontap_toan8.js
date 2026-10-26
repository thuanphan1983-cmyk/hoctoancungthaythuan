// ==============================================================================
// NGÂN HÀNG ĐỀ THI TOÁN 8 (KNTT) - Ôn tập cuối Chương III: Tứ giác
// Bao gồm 3 đề phân hóa: Đề 1 (Cơ bản) < Đề 2 (Khá) < Đề 3 (Nâng cao)
// Chuẩn ma trận 10 điểm: 12 TN + 2 Đ/S + 4 TLN + 3 Tự luận
// ==============================================================================

const BAI_6_TOAN8_EXAMS = {
  "c3_8_bai6_test1": {
    "title": "Toán 8 (KNTT) - Bài kiểm tra cuối Chương III: Tứ giác - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tổng bốn góc của một tứ giác lồi luôn bằng:",
        "options": [
          "$270^\\circ$",
          "$180^\\circ$",
          "$540^\\circ$",
          "$360^\\circ$"
        ],
        "correct": 3
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tứ giác có hai cạnh đối song song là:",
        "options": [
          "Hình thoi",
          "Hình thang",
          "Hình chữ nhật",
          "Hình bình hành"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hình thang có hai đường chéo bằng nhau là:",
        "options": [
          "Hình thang cân",
          "Hình chữ nhật",
          "Hình thoi",
          "Hình bình hành"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hình bình hành có hai đường chéo vuông góc với nhau là:",
        "options": [
          "Hình thang cân",
          "Hình chữ nhật",
          "Hình thang vuông",
          "Hình thoi"
        ],
        "correct": 3
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Hình chữ nhật có hai cạnh kề bằng nhau là:",
        "options": [
          "Hình thang cân",
          "Hình bình hành",
          "Hình thoi",
          "Hình vuông"
        ],
        "correct": 3
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tứ giác vừa có 4 góc vuông vừa có 4 cạnh bằng nhau là:",
        "options": [
          "Hình vuông",
          "Hình bình hành",
          "Hình chữ nhật",
          "Hình thoi"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tứ giác $ABCD$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = 100^\\circ$. Số đo góc $D$ bằng:",
        "options": [
          "$100^\\circ$",
          "$110^\\circ$",
          "$120^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hình chữ nhật $ABCD$ có $AB = 8\\text{ cm}, BC = 6\\text{ cm}$. Bán kính đường tròn đi qua bốn đỉnh $A, B, C, D$ là:",
        "options": [
          "$10\\text{ cm}$",
          "$4\\text{ cm}$",
          "$5\\text{ cm}$",
          "$7\\text{ cm}$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho hình thoi có độ dài hai đường chéo là $10\\text{ cm}$ và $24\\text{ cm}$. Chu vi hình thoi đó bằng:",
        "options": [
          "$48\\text{ cm}$",
          "$52\\text{ cm}$",
          "$68\\text{ cm}$",
          "$34\\text{ cm}$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Tứ giác có các đỉnh là trung điểm của bốn cạnh của một tứ giác lồi bất kì luôn là:",
        "options": [
          "Hình bình hành",
          "Hình vuông",
          "Hình chữ nhật",
          "Hình thoi"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Độ dài đường trung tuyến $AM$ bằng:",
        "options": [
          "$10\\text{ cm}$",
          "$4.8\\text{ cm}$",
          "$5\\text{ cm}$",
          "$7\\text{ cm}$"
        ],
        "correct": 2
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Một hình vuông có chu vi bằng $32\\text{ cm}$. Diện tích của hình vuông đó bằng:",
        "options": [
          "$32\\text{ cm}^2$",
          "$128\\text{ cm}^2$",
          "$64\\text{ cm}^2$",
          "$16\\text{ cm}^2$"
        ],
        "correct": 2
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của cạnh huyền $BC$. Kẻ $MD \\perp AB$ tại $D$ và $ME \\perp AC$ tại $E$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $ADME$ có 3 góc vuông nên là hình chữ nhật.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Điểm $D$ là trung điểm của $AB$ và điểm $E$ là trung điểm của $AC$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Độ dài đoạn thẳng $DE$ bằng một nửa độ dài cạnh huyền $BC$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Tứ giác $ADME$ luôn là hình vuông với mọi tam giác vuông $ABC$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình bình hành $ABCD$ có $AB = 2AD$. Gọi $E, F$ lần lượt là trung điểm của $AB$ và $CD$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $AEFD$ là hình thoi vì có 4 cạnh bằng nhau.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tứ giác $EBCF$ cũng là hình thoi.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng $AF$ luôn vuông góc với đoạn thẳng $DE$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Nếu $\\widehat{A} = 90^\\circ$ thì tứ giác $AEFD$ trở thành hình chữ nhật nhưng không phải hình vuông.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 105^\\circ, \\widehat{B} = 85^\\circ, \\widehat{C} = 70^\\circ$. Tính số đo góc $D$ (theo độ).",
        "answer": "100"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Hình thang cân $ABCD$ ($AB \\parallel CD$) có $AB = 4\\text{ cm}, CD = 10\\text{ cm}$, cạnh bên bằng $5\\text{ cm}$. Tính diện tích hình thang cân (theo cm²).",
        "answer": "28"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Một hình thoi có diện tích bằng $48\\text{ cm}^2$ và một đường chéo dài $8\\text{ cm}$. Tính độ dài cạnh của hình thoi (theo cm, làm tròn số nguyên).",
        "answer": "7"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hình vuông có độ dài đường chéo bằng $14\\text{ cm}$. Tính diện tích của hình vuông đó (theo cm²).",
        "answer": "98"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ cân tại $A$. Gọi $D, E$ lần lượt là trung điểm của $AB, AC$.\na) Chứng minh tứ giác $BDEC$ là hình thang cân.\nb) Biết $\\widehat{A} = 80^\\circ$, tính số đo các góc của hình thang cân $BDEC$.",
        "rubric": "a) DE là đường trung bình tam giác ABC => DE // BC => BDEC là hình thang. Lại có góc B = góc C (do tam giác ABC cân tại A) => BDEC là hình thang cân (0.5đ)\nb) Góc B = góc C = (180° - 80°)/2 = 50°. Góc BDE = góc CED = 180° - 50° = 130° (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của $BC$. Lấy điểm $D$ đối xứng với $A$ qua $M$.\na) Chứng minh tứ giác $ABDC$ là hình chữ nhật.\nb) Kẻ $AH \\perp BC$ tại $H$. Gọi $I$ là trung điểm của $AH$. Chứng minh rằng nếu tam giác $ABC$ vuông cân thì tứ giác $ABDC$ là hình vuông.",
        "rubric": "a) M là trung điểm của AD và BC => ABDC là hình bình hành. Có góc BAC = 90° => ABDC là hình chữ nhật (0.5đ)\nb) Nếu tam giác ABC vuông cân tại A thì AB = AC. Hình chữ nhật ABDC có hai cạnh kề AB = AC nên là hình vuông (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình vuông $ABCD$. Lấy điểm $E$ trên cạnh $CD$ và điểm $F$ trên cạnh $BC$ sao cho $\\widehat{EAF} = 45^\\circ$. Kẻ $AH \\perp EF$ tại $H$.\na) Chứng minh rằng $AH = AB$.\nb) Chứng minh chu vi tam giác $CEF$ bằng nửa chu vi hình vuông $ABCD$.",
        "rubric": "a) Trên tia đối tia DC lấy điểm K sao cho DK = BF. Tam giác ABF = tam giác ADK (c-g-c) => AF = AK và góc BAF = góc DAK. Khi đó góc KAE = góc DAK + góc DAE = góc BAF + góc DAE = 90° - 45° = 45° = góc FAE. Tam giác AKE = tam giác AFE (c-g-c) => AH = AD = AB (0.5đ)\nb) Chu vi tam giác CEF = CE + EF + FC = CE + KE + FC = CE + KD + DE + FC = CE + BF + DE + FC = (CE + DE) + (BF + FC) = CD + BC = 2a = Nửa chu vi hình vuông (ĐPCM) (0.5đ)"
      }
    ]
  },
  "c3_8_bai6_test2": {
    "title": "Toán 8 (KNTT) - Bài kiểm tra cuối Chương III: Tứ giác - Bài kiểm tra số 2 (⚡ Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khẳng định nào sau đây là đúng về mối quan hệ giữa các hình?",
        "options": [
          "Hình thoi có một góc vuông là hình chữ nhật nhưng không phải hình vuông",
          "Hình vuông vừa là hình chữ nhật vừa là hình thoi",
          "Hình thang cân là hình bình hành",
          "Hình bình hành có hai đường chéo bằng nhau là hình thoi"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tứ giác có hai đường chéo vuông góc với nhau tại trung điểm của mỗi đường là:",
        "options": [
          "Hình thang cân",
          "Hình bình hành không thoi",
          "Hình chữ nhật",
          "Hình thoi"
        ],
        "correct": 3
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tứ giác có hai đường chéo bằng nhau và cắt nhau tại trung điểm của mỗi đường là:",
        "options": [
          "Hình thang cân",
          "Hình bình hành",
          "Hình thoi",
          "Hình chữ nhật"
        ],
        "correct": 3
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hình thoi có bốn góc bằng nhau là:",
        "options": [
          "Hình vuông",
          "Hình thang cân",
          "Hình bình hành",
          "Hình chữ nhật"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Hình nào sau đây có vô số trục đối xứng?",
        "options": [
          "Hình thoi",
          "Hình chữ nhật",
          "Hình tròn",
          "Hình vuông"
        ],
        "correct": 2
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tâm đối xứng của hình vuông là:",
        "options": [
          "Không có tâm đối xứng",
          "Một đỉnh của hình vuông",
          "Giao điểm của hai đường chéo",
          "Trung điểm của một cạnh"
        ],
        "correct": 2
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$). Biết $\\widehat{A} = 3\\widehat{D}$. Hiệu số đo giữa góc $B$ và góc $C$ bằng:",
        "options": [
          "$45^\\circ$",
          "$120^\\circ$",
          "$60^\\circ$",
          "$90^\\circ$"
        ],
        "correct": 3
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có chu vi $24\\text{ cm}$. Gọi $M, N, P$ lần lượt là trung điểm của $AB, BC, CA$. Chu vi tam giác $MNP$ bằng:",
        "options": [
          "$12\\text{ cm}$",
          "$24\\text{ cm}$",
          "$6\\text{ cm}$",
          "$18\\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một hình chữ nhật có độ dài đường chéo bằng $15\\text{ cm}$ và tỉ số hai cạnh là $3 : 4$. Diện tích hình chữ nhật là:",
        "options": [
          "$216\\text{ cm}^2$",
          "$108\\text{ cm}^2$",
          "$144\\text{ cm}^2$",
          "$96\\text{ cm}^2$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có hai đường chéo $AC \\perp BD$. Tứ giác có các đỉnh là trung điểm bốn cạnh của $ABCD$ là:",
        "options": [
          "Hình thoi",
          "Hình bình hành không vuông",
          "Hình chữ nhật",
          "Hình vuông"
        ],
        "correct": 2
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có hai đường chéo $AC = BD$. Tứ giác có các đỉnh là trung điểm bốn cạnh của $ABCD$ là:",
        "options": [
          "Hình vuông",
          "Hình thoi",
          "Hình bình hành không thoi",
          "Hình chữ nhật"
        ],
        "correct": 1
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hình vuông có diện tích bằng $144\\text{ cm}^2$. Bán kính đường tròn ngoại tiếp hình vuông đó bằng:",
        "options": [
          "$6\\sqrt{2}\\text{ cm}$",
          "$12\\sqrt{2}\\text{ cm}$",
          "$12\\text{ cm}$",
          "$6\\text{ cm}$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình bình hành $ABCD$. Lấy $M, N$ lần lượt trên các cạnh $AB, CD$ sao cho $AM = CN$.",
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
            "text": "Đoạn thẳng $MN$ đi qua giao điểm của hai đường chéo $AC$ và $BD$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tứ giác $MBND$ cũng là một hình bình hành.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Nếu $ABCD$ là hình thoi thì $AMCN$ chắc chắn là hình thoi.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ vuông cân tại $A$. Dựng hình vuông $BCDE$ sao cho điểm $A$ nằm ngoài hình vuông.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Góc $\\widehat{ABC} = \\widehat{ACB} = 45^\\circ$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Các góc $\\widehat{ABE} = \\widehat{ACD} = 135^\\circ$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Hai tam giác $ABE$ và $ACD$ bằng nhau.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Đoạn thẳng $AE$ vuông góc với đoạn thẳng $AD$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thang cân $ABCD$ có đường chéo $AC = 15\\text{ cm}$, đường cao $AH = 9\\text{ cm}$. Tính tổng độ dài hai đáy $AB + CD$ (theo cm).",
        "answer": "24"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Hình thoi $ABCD$ có chu vi $40\\text{ cm}$, khoảng cách giữa hai cạnh đối là $9.6\\text{ cm}$. Tính diện tích hình thoi (theo cm²).",
        "answer": "96"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho hình chữ nhật $ABCD$ có diện tích $60\\text{ cm}^2$ và chu vi $34\\text{ cm}$. Tính độ dài đường chéo $AC$ (theo cm).",
        "answer": "13"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình vuông $ABCD$ cạnh $10\\text{ cm}$. Gọi $M$ là trung điểm $AB$. Đoạn thẳng $CM$ cắt $BD$ tại $P$. Tính diện tích tam giác $BPM$ (theo cm², viết dưới dạng phân số tối giản $a/b$).",
        "answer": "25/3"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của $BC$. Kẻ $MD \\perp AB$ tại $D$ và $ME \\perp AC$ tại $E$.\na) Chứng minh tứ giác $ADME$ là hình chữ nhật.\nb) Lấy điểm $P$ đối xứng với $M$ qua $D$. Chứng minh tứ giác $AMBP$ là hình thoi.",
        "rubric": "a) Tứ giác ADME có 3 góc vuông nên là hình chữ nhật (0.5đ)\nb) D là trung điểm PM (gt). MD // AC và M là trung điểm BC => D là trung điểm AB. Tứ giác AMBP có hai đường chéo cắt nhau tại trung điểm D mỗi đường nên là HBH. Lại có AB vuông góc PM => AMBP là hình thoi (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình bình hành $ABCD$ có $AB = 2AD$. Gọi $E, F$ lần lượt là trung điểm của $AB$ và $CD$.\na) Chứng minh tứ giác $AEFD$ là hình thoi.\nb) Gọi $M$ là giao điểm của $AF$ và $DE$, $N$ là giao điểm của $BF$ và $CE$. Chứng minh tứ giác $EMFN$ là hình chữ nhật.",
        "rubric": "a) AEFD có AD // EF, AD = EF = AB/2 = AE => AEFD là hình thoi (0.5đ)\nb) Trong hình thoi AEFD: AF vuông góc DE tại M => góc M = 90°. Tương tự góc N = 90°. ME // NF và MF // NE => EMFN là HBH có góc M = 90° nên là hình chữ nhật (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình vuông $ABCD$. Lấy điểm $M$ trên cạnh $BC$. Kẻ tia $Ax$ vuông góc với $AM$ cắt đường thẳng $CD$ tại $N$. Gọi $I$ là trung điểm của đoạn thẳng $MN$.\na) Chứng minh tam giác $AMN$ vuông cân tại $A$.\nb) Chứng minh rằng khi $M$ di chuyển trên cạnh $BC$, điểm $I$ luôn thuộc một đường thẳng cố định.",
        "rubric": "a) Tam giác vuông ABM = tam giác vuông ADN (cạnh góc vuông - góc nhọn: AB = AD, góc BAM = góc DAN cùng phụ góc DAM) => AM = AN. Tam giác AMN vuông tại A có AM = AN nên là tam giác vuông cân tại A (0.5đ)\nb) I là trung điểm MN, tam giác CMN vuông tại C => CI = MN/2. Lại có AI = MN/2 (tam giác vuông cân AMN) => AI = CI. Do A và C cố định nên I luôn nằm trên đường trung trực của đoạn thẳng AC (chính là đường thẳng chứa đường chéo BD của hình vuông) (0.5đ)"
      }
    ]
  },
  "c3_8_bai6_test3": {
    "title": "Toán 8 (KNTT) - Bài kiểm tra cuối Chương III: Tứ giác - Bài kiểm tra số 3 (🔥 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tứ giác có hai đường chéo bằng nhau và vuông góc với nhau tại trung điểm của mỗi đường là:",
        "options": [
          "Hình vuông",
          "Hình thang cân",
          "Hình thoi",
          "Hình chữ nhật"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Một tứ giác lồi vừa có trục đối xứng vừa có tâm đối xứng không thể là:",
        "options": [
          "Hình thang vuông",
          "Hình vuông",
          "Hình chữ nhật",
          "Hình thoi"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Điều kiện cần và đủ để hình bình hành là hình vuông là:",
        "options": [
          "Có bốn cạnh bằng nhau",
          "Có hai đường chéo bằng nhau",
          "Có hai đường chéo bằng nhau và vuông góc với nhau",
          "Có hai đường chéo vuông góc"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tổng bình phương bốn cạnh của một tứ giác lồi bằng tổng bình phương hai đường chéo khi và chỉ khi tứ giác đó là:",
        "options": [
          "Hình thoi",
          "Hình vuông",
          "Hình bình hành",
          "Hình chữ nhật"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tứ giác có các đỉnh là trung điểm của bốn cạnh của một hình thang cân có hai đường chéo vuông góc là:",
        "options": [
          "Hình thoi",
          "Hình bình hành",
          "Hình chữ nhật",
          "Hình vuông"
        ],
        "correct": 3
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Cho hình vuông có cạnh $a$. Diện tích hình tròn ngoại tiếp hình vuông đó bằng:",
        "options": [
          "$\\pi a^2$",
          "$2\\pi a^2$",
          "$\\frac{\\pi a^2}{2}$",
          "$\\frac{\\pi a^2}{4}$"
        ],
        "correct": 2
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $AC \\perp BD$. Đặt $AB = a, BC = b, CD = c, DA = d$. Hệ thức nào sau đây luôn đúng?",
        "options": [
          "$a + c = b + d$",
          "$a^2 + c^2 = b^2 + d^2$",
          "$a \\cdot c = b \\cdot d$",
          "$a^2 + b^2 = c^2 + d^2$"
        ],
        "correct": 1
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho hình vuông $ABCD$. Gọi $E, F$ lần lượt là trung điểm của $BC, CD$. Đoạn thẳng $AE$ cắt $BF$ tại $I$. Khẳng định nào sau đây là đúng?",
        "options": [
          "$AE \\parallel BF$",
          "$AE \\perp BF$ và $CI = CD$",
          "$AE = 2BF$",
          "Tam giác $AIB$ vuông cân"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Hình thoi $ABCD$ có $\\widehat{A} = 60^\\circ$. Gọi $M, N$ lần lượt là trung điểm của $BC, CD$. Tam giác $AMN$ là:",
        "options": [
          "Tam giác cân có góc đáy $30^\\circ$",
          "Tam giác vuông",
          "Tam giác vuông cân",
          "Tam giác đều"
        ],
        "correct": 3
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$ có $AB = 8\\text{ cm}, BC = 6\\text{ cm}$. Điểm $M$ thuộc đường chéo $BD$. Khoảng cách từ $M$ đến $AB$ là $x$, đến $AD$ là $y$. Giá trị biểu thức $3x + 4y$ bằng:",
        "options": [
          "$36$",
          "$24$",
          "$12$",
          "$48$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho hình vuông $ABCD$. Điểm $M$ thuộc cạnh $BC$. Tia phân giác của góc $\\widehat{DAM}$ cắt cạnh $CD$ tại $P$. Khẳng định nào sau đây luôn đúng?",
        "options": [
          "$AP^2 = BM^2 + DP^2$",
          "$AP = BM - DP$",
          "$AP = 2(BM + DP)$",
          "$AP = BM + DP$"
        ],
        "correct": 3
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có diện tích $S = 32\\text{ cm}^2$ và $AC + BD = 16\\text{ cm}$. Khi đó hai đường chéo $AC$ và $BD$:",
        "options": [
          "Bằng nhau và vuông góc với nhau",
          "Bằng nhau nhưng không vuông góc",
          "Cắt nhau tại trung điểm mỗi đường",
          "Vuông góc nhưng không bằng nhau"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình vuông $ABCD$. Lấy điểm $E$ trên cạnh $BC$, điểm $F$ trên cạnh $CD$ sao cho $\\widehat{EAF} = 45^\\circ$. Kẻ $AH \\perp EF$ tại $H$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $AH$ luôn bằng độ dài cạnh hình vuông $AB$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Chu vi của tam giác $CEF$ luôn bằng nửa chu vi hình vuông $ABCD$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng $EF = BE + DF$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Diện tích tam giác $AEF$ luôn lớn hơn diện tích tam giác $CEF$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình thoi $ABCD$ có cạnh bằng $a$ và góc $\\widehat{A} = 60^\\circ$. Một đường thẳng $d$ bất kì đi qua đỉnh $C$ cắt tia đối của tia $BA$ tại $E$ và cắt tia đối của tia $DA$ tại $F$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tích hai đoạn thẳng $BE \\cdot DF = a^2$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tam giác $ABD$ là một tam giác đều cạnh $a$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Hai tam giác $BDE$ và $FDB$ đồng dạng với nhau.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Số đo góc $\\widehat{EOF}$ (với $O$ là giao điểm $AC$ và $BD$) bằng $90^\\circ$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình vuông $ABCD$ cạnh $12\\text{ cm}$. Gọi $E, F$ là trung điểm của $AB, CD$. Tính bán kính đường tròn đi qua bốn đỉnh của hình chữ nhật $AEFD$ (theo cm, viết dạng $a\\sqrt{5}$ với $a$ là số nguyên).",
        "answer": "3"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình thoi $ABCD$ có $AC = 16\\text{ cm}, BD = 12\\text{ cm}$. Gọi $M, N, P, Q$ là trung điểm bốn cạnh. Tính diện tích hình chữ nhật $MNPQ$ (theo cm²).",
        "answer": "48"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hình vuông $ABCD$ có cạnh bằng $10\\text{ cm}$. Lấy điểm $E$ trên cạnh $BC$ sao cho $BE = 3\\text{ cm}$. Kẻ $AF \\perp AE$ ($F \\in CD$ kéo dài). Tính diện tích tam giác $AEF$ (theo cm²).",
        "answer": "54.5"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình chữ nhật $ABCD$ có $AB = 4\\text{ cm}, BC = 3\\text{ cm}$. Một điểm $M$ di động trong hình chữ nhật. Tìm giá trị nhỏ nhất của tổng $S = MA^2 + MB^2 + MC^2 + MD^2$ (theo cm²).",
        "answer": "25"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình vuông $ABCD$. Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$. Lấy điểm $M$ trên đoạn $OB$ ($M$ khác $O, B$). Kẻ $ME \\perp AB$ tại $E$ và $MF \\perp BC$ tại $F$.\na) Chứng minh tứ giác $BEMF$ là hình vuông.\nb) Chứng minh $DE = CF$ và $DE \\perp CF$.",
        "rubric": "a) Góc B = 90°, ME vuông góc AB, MF vuông góc BC => BEMF là hình chữ nhật. Vì M thuộc BD (phân giác góc B) nên ME = MF => BEMF là hình vuông (0.5đ)\nb) Xét tam giác ADE và tam giác DCF: AD = DC, AE = DF (do AB - BE = BC - MF), góc A = góc D = 90° => tam giác ADE = tam giác DCF (c-g-c) => DE = CF và góc ADE = góc DCF => DE vuông góc CF (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tứ giác lồi $ABCD$. Dựng ra phía ngoài tứ giác các hình vuông có cạnh lần lượt là $AB, BC, CD, DA$. Gọi $O_1, O_2, O_3, O_4$ lần lượt là tâm của bốn hình vuông đó.\na) Chứng minh đoạn thẳng $O_1 O_3$ bằng đoạn thẳng $O_2 O_4$ (Định lí Van Aubel).\nb) Chứng minh rằng $O_1 O_3 \\perp O_2 O_4$.",
        "rubric": "a) Sử dụng phương pháp vectơ hoặc phép quay góc 90° tâm là trung điểm đường chéo: Dựng tam giác bằng nhau chứng minh đoạn thẳng nối hai tâm đối diện bằng nhau O1O3 = O2O4 (0.5đ)\nb) Tương tự từ phép quay 90° suy ra góc giữa hai đoạn thẳng O1O3 và O2O4 bằng 90°, tức là O1O3 vuông góc O2O4 (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình vuông $ABCD$ cạnh $a$. Điểm $M$ nằm trên cạnh $BC$, điểm $N$ nằm trên cạnh $CD$ sao cho chu vi tam giác $CMN$ bằng $2a$.\na) Chứng minh rằng góc $\\widehat{MAN} = 45^\\circ$.\nb) Tìm giá trị lớn nhất và giá trị nhỏ nhất của diện tích tam giác $AMN$ khi $M, N$ thay đổi.",
        "rubric": "a) Chu vi tam giác CMN = CM + MN + NC = 2a = BC + CD = (BM + MC) + (CN + ND) => MN = BM + DN. Trên tia đối tia DC lấy K sao cho DK = BM => NK = ND + DK = DN + BM = MN. Tam giác ABM = tam giác ADK => AM = AK. Tam giác AMN = tam giác AKN (c-c-c) => góc MAN = góc KAN = 1/2 góc BAK = 45° (0.5đ)\nb) Kẻ AH vuông góc MN => AH = AB = a. S(AMN) = 1/2 a . MN. Vì MN = BM + DN và CM + CN + MN = 2a. Áp dụng BĐT: MN nhỏ nhất khi BM = DN <=> MN = 2a(căn 2 - 1). Khi đó S(AMN)_min = a²(căn 2 - 1). S(AMN)_max đạt được khi M trùng B hoặc M trùng C (S = a²/2) (0.5đ)"
      }
    ]
  }
};

if (typeof window !== 'undefined') {
  window.CHAPTER3_TOAN8_EXAMS = window.CHAPTER3_TOAN8_EXAMS || {};
  Object.assign(window.CHAPTER3_TOAN8_EXAMS, BAI_6_TOAN8_EXAMS);
  window.EXAMS_8_C3_8 = window.CHAPTER3_TOAN8_EXAMS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BAI_6_TOAN8_EXAMS;
}
