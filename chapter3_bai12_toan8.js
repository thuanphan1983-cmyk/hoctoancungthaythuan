// ==============================================================================
// NGÂN HÀNG ĐỀ THI TOÁN 8 (KNTT) - Bài 12: Hình bình hành
// Bao gồm 3 đề phân hóa: Đề 1 (Cơ bản) < Đề 2 (Khá) < Đề 3 (Nâng cao)
// Chuẩn ma trận 10 điểm: 12 TN + 2 Đ/S + 4 TLN + 3 Tự luận
// ==============================================================================

const BAI_3_TOAN8_EXAMS = {
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

if (typeof window !== 'undefined') {
  window.CHAPTER3_TOAN8_EXAMS = window.CHAPTER3_TOAN8_EXAMS || {};
  Object.assign(window.CHAPTER3_TOAN8_EXAMS, BAI_3_TOAN8_EXAMS);
  window.EXAMS_8_C3_8 = window.CHAPTER3_TOAN8_EXAMS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BAI_3_TOAN8_EXAMS;
}
