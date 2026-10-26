// ==============================================================================
// NGÂN HÀNG ĐỀ THI TOÁN 8 (KNTT) - Bài 13: Hình chữ nhật
// Bao gồm 3 đề phân hóa: Đề 1 (Cơ bản) < Đề 2 (Khá) < Đề 3 (Nâng cao)
// Chuẩn ma trận 10 điểm: 12 TN + 2 Đ/S + 4 TLN + 3 Tự luận
// ==============================================================================

const BAI_4_TOAN8_EXAMS = {
  "c3_8_bai4_test1": {
    "title": "Toán 8 (KNTT) - Bài 13: Hình chữ nhật - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hình chữ nhật là tứ giác có:",
        "options": [
          "Hai cạnh kề bằng nhau",
          "Hai đường chéo vuông góc",
          "Bốn góc vuông",
          "Bốn cạnh bằng nhau"
        ],
        "correct": 2
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong hình chữ nhật, khẳng định nào sau đây là sai?",
        "options": [
          "Giao điểm hai đường chéo cách đều bốn đỉnh",
          "Hai đường chéo bằng nhau",
          "Hai đường chéo vuông góc với nhau",
          "Các cạnh đối song song và bằng nhau"
        ],
        "correct": 2
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong một tam giác vuông, đường trung tuyến ứng với cạnh huyền có độ dài bằng:",
        "options": [
          "Cạnh góc vuông",
          "Gấp đôi cạnh huyền",
          "Nửa độ dài cạnh huyền",
          "Cạnh huyền"
        ],
        "correct": 2
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hình chữ nhật có bao nhiêu trục đối xứng?",
        "options": [
          "$1$",
          "$0$",
          "$4$",
          "$2$"
        ],
        "correct": 3
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Hình bình hành có thêm điều kiện nào sau đây thì trở thành hình chữ nhật?",
        "options": [
          "Có một góc vuông",
          "Có hai đường chéo vuông góc",
          "Có hai cạnh kề bằng nhau",
          "Có một đường chéo là phân giác một góc"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Cho tam giác $ABC$ vuông tại $A$ có $BC = 12\\text{ cm}$. Độ dài đường trung tuyến $AM$ bằng:",
        "options": [
          "$24\\text{ cm}$",
          "$6\\text{ cm}$",
          "$8\\text{ cm}$",
          "$12\\text{ cm}$"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hình chữ nhật $ABCD$ có chiều dài $AB = 8\\text{ cm}$, chiều rộng $BC = 6\\text{ cm}$. Độ dài đường chéo $AC$ bằng:",
        "options": [
          "$12\\text{ cm}$",
          "$48\\text{ cm}$",
          "$14\\text{ cm}$",
          "$10\\text{ cm}$"
        ],
        "correct": 3
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hình thang cân có thêm điều kiện nào sau đây thì trở thành hình chữ nhật?",
        "options": [
          "Có hai đường chéo bằng nhau",
          "Có hai cạnh bên song song",
          "Có hai góc kề đáy bằng nhau",
          "Có một góc vuông"
        ],
        "correct": 3
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$ có hai đường chéo cắt nhau tại $O$. Biết $OA = 5\\text{ cm}, AB = 8\\text{ cm}$. Độ dài cạnh $BC$ là:",
        "options": [
          "$10\\text{ cm}$",
          "$6\\text{ cm}$",
          "$8\\text{ cm}$",
          "$5\\text{ cm}$"
        ],
        "correct": 1
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Chu vi của một hình chữ nhật là $28\\text{ cm}$, biết chiều dài hơn chiều rộng $4\\text{ cm}$. Diện tích của hình chữ nhật đó bằng:",
        "options": [
          "$45\\text{ cm}^2$",
          "$40\\text{ cm}^2$",
          "$48\\text{ cm}^2$",
          "$50\\text{ cm}^2$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có đường trung tuyến $AM = 5\\text{ cm}$ và $BC = 10\\text{ cm}$. Khẳng định nào sau đây là đúng?",
        "options": [
          "Tam giác $ABC$ đều",
          "Tam giác $ABC$ vuông tại $A$",
          "Tam giác $ABC$ vuông tại $B$",
          "Tam giác $ABC$ cân tại $A$"
        ],
        "correct": 1
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$. Tứ giác $MNPQ$ là:",
        "options": [
          "Hình thoi",
          "Hình thang cân",
          "Hình chữ nhật",
          "Hình vuông"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của cạnh huyền $BC$. Trên tia đối của tia $MA$ lấy điểm $D$ sao cho $MD = MA$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $ABDC$ là một hình bình hành vì có hai đường chéo cắt nhau tại trung điểm mỗi đường.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Vì $\\widehat{BAC} = 90^\\circ$ nên hình bình hành $ABDC$ là hình chữ nhật.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Độ dài đường chéo $AD$ gấp đôi cạnh huyền $BC$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng $AM = \\frac{1}{2} BC$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Một sân bóng rổ mini hình chữ nhật $ABCD$ có chiều dài $AB = 16\\text{ m}$ và chiều rộng $BC = 12\\text{ m}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Chu vi của sân bóng rổ bằng $56\\text{ m}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Diện tích của sân bóng rổ bằng $192\\text{ m}^2$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Độ dài đường chéo $AC$ của sân bằng $20\\text{ m}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Khoảng cách từ tâm đối xứng $O$ đến mỗi đỉnh của sân là $15\\text{ m}$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$ có $AC = 13\\text{ cm}, AB = 12\\text{ cm}$. Tính độ dài cạnh $AD$ (theo cm).",
        "answer": "5"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tam giác $ABC$ vuông tại $A$ có $AB = 9\\text{ cm}, AC = 12\\text{ cm}$. Gọi $M$ là trung điểm của $BC$. Tính độ dài $AM$ (theo cm).",
        "answer": "7.5"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho hình chữ nhật $ABCD$ có hai đường chéo cắt nhau tại $O$. Biết $\\widehat{AOB} = 60^\\circ$ và $AC = 12\\text{ cm}$. Tính độ dài cạnh $BC$ (theo cm).",
        "answer": "6"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hình chữ nhật có chu vi bằng $34\\text{ cm}$ và độ dài đường chéo bằng $13\\text{ cm}$. Tính diện tích hình chữ nhật (theo cm²).",
        "answer": "60"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$. Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$.\na) Chứng minh rằng $OA = OB = OC = OD$.\nb) Biết $\\widehat{AOD} = 120^\\circ$ và $AC = 10\\text{ cm}$, tính số đo góc $\\widehat{ACD}$ và độ dài cạnh $AB$.",
        "rubric": "a) Trong hình chữ nhật ABCD, hai đường chéo AC = BD và cắt nhau tại trung điểm O của mỗi đường => OA = OC = AC/2, OB = OD = BD/2 => OA = OB = OC = OD (0.5đ)\nb) Góc AOB kề bù với góc AOD => góc AOB = 180° - 120° = 60°. Tam giác OAB cân tại O có góc AOB = 60° nên là tam giác đều => AB = OA = AC/2 = 5 cm. Góc ACD: tam giác ODC đều => góc OCD = 60° => góc ACD = 60° (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$), đường cao $AH$. Kẻ $HM \\perp AB$ tại $M$ và $HN \\perp AC$ tại $N$.\na) Chứng minh tứ giác $AMHN$ là hình chữ nhật.\nb) Chứng minh $MN = AH$ và $MN \\perp OA$ (với $O$ là trung điểm của $BC$).",
        "rubric": "a) Tứ giác AMHN có góc A = 90°, góc AMH = 90°, góc ANH = 90° => Tứ giác có 3 góc vuông nên AMHN là hình chữ nhật (0.5đ)\nb) AMHN là hình chữ nhật => hai đường chéo AH = MN (0.25đ). Gọi I là giao điểm AH và MN. Tam giác vuông ABC có AO là trung tuyến => góc OAC = góc OCA; tam giác vuông AMHN có góc INA = góc IAN... Suy ra AO vuông góc MN (0.25đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình chữ nhật $ABCD$. Kẻ $BH \\perp AC$ tại $H$. Gọi $M, N$ lần lượt là trung điểm của $AH$ và $CD$.\na) Chứng minh tứ giác $BCNM$ hoặc tam giác $BMN$ có tính chất vuông góc ($BM \\perp MN$).\nb) Kẻ $CK \\perp BD$ tại $K$. Chứng minh rằng bốn điểm $B, H, K, C$ cùng thuộc một đường tròn.",
        "rubric": "a) Gọi K là trung điểm BH => MK là đường trung bình tam giác ABH => MK // AB // CD và MK = AB/2 = CD/2 = CN => MKNC là HBH => MN // KC. Trong tam giác BMC, K là trực tâm => CK vuông góc BM => MN vuông góc BM (0.5đ)\nb) BH vuông góc AC tại H => góc BHC = 90°; BK vuông góc CD... Xét các góc cùng nhìn một đoạn thẳng dưới góc 90° => 4 điểm B, H, K, C cùng nằm trên đường tròn đường kính BC (0.5đ)"
      }
    ]
  },
  "c3_8_bai4_test2": {
    "title": "Toán 8 (KNTT) - Bài 13: Hình chữ nhật - Bài kiểm tra số 2 (⚡ Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tứ giác có hai đường chéo bằng nhau và cắt nhau tại trung điểm mỗi đường là:",
        "options": [
          "Hình thang cân",
          "Hình thoi",
          "Hình bình hành",
          "Hình chữ nhật"
        ],
        "correct": 3
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hình bình hành $ABCD$ có hai đường chéo $AC = BD$. Tứ giác $ABCD$ là:",
        "options": [
          "Hình thoi",
          "Hình chữ nhật",
          "Hình thang vuông",
          "Hình vuông"
        ],
        "correct": 1
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho tam giác $ABC$ có $AM$ là trung tuyến và $AM = \\frac{1}{2}BC$. Tam giác $ABC$ là:",
        "options": [
          "Tam giác cân tại $A$",
          "Tam giác vuông tại $A$",
          "Tam giác vuông cân tại $A$",
          "Tam giác đều"
        ],
        "correct": 1
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Cho hình chữ nhật $ABCD$. Góc giữa hai đường chéo bằng $90^\\circ$ thì hình chữ nhật $ABCD$ là:",
        "options": [
          "Hình bình hành",
          "Hình thang",
          "Hình vuông",
          "Hình thoi"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Tâm đối xứng của hình chữ nhật là:",
        "options": [
          "Giao điểm của hai đường chéo",
          "Trung điểm của cạnh dài",
          "Giao điểm của hai cạnh kề",
          "Không có tâm đối xứng"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trong hình chữ nhật, khoảng cách từ giao điểm hai đường chéo tới mỗi đỉnh:",
        "options": [
          "Khác nhau",
          "Bằng nửa chiều dài",
          "Bằng nửa chiều rộng",
          "Bằng nhau"
        ],
        "correct": 3
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hình chữ nhật $ABCD$ có chu vi $36\\text{ cm}$, tỉ số hai cạnh là $\\frac{AB}{BC} = \\frac{4}{5}$. Diện tích hình chữ nhật là:",
        "options": [
          "$160\\text{ cm}^2$",
          "$90\\text{ cm}^2$",
          "$72\\text{ cm}^2$",
          "$80\\text{ cm}^2$"
        ],
        "correct": 3
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Điểm $M$ là trung điểm $BC$, điểm $D$ đối xứng với $A$ qua $M$. Tứ giác $ABDC$ có diện tích bằng:",
        "options": [
          "$24\\text{ cm}^2$",
          "$48\\text{ cm}^2$",
          "$36\\text{ cm}^2$",
          "$50\\text{ cm}^2$"
        ],
        "correct": 1
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$ có đường chéo $AC = 10\\text{ cm}$, góc tạo bởi $AC$ và $AB$ là $30^\\circ$. Diện tích hình chữ nhật $ABCD$ là:",
        "options": [
          "$25\\text{ cm}^2$",
          "$50\\text{ cm}^2$",
          "$25\\sqrt{3}\\text{ cm}^2$",
          "$50\\sqrt{3}\\text{ cm}^2$"
        ],
        "correct": 2
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Hình thang cân $ABCD$ ($AB \\parallel CD$) có $AD \\parallel BC$. Khi đó hình thang cân $ABCD$ là:",
        "options": [
          "Hình chữ nhật",
          "Hình vuông",
          "Chỉ là hình bình hành",
          "Hình thoi"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Các đường phân giác của bốn góc của một hình bình hành cắt nhau tạo thành một:",
        "options": [
          "Hình chữ nhật",
          "Hình vuông",
          "Hình thoi",
          "Hình bình hành"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$ có $AB = 4\\text{ cm}, BC = 3\\text{ cm}$. Khoảng cách từ điểm $B$ đến đường chéo $AC$ bằng:",
        "options": [
          "$2.5\\text{ cm}$",
          "$2\\text{ cm}$",
          "$2.4\\text{ cm}$",
          "$3\\text{ cm}$"
        ],
        "correct": 2
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ cân tại $A$, đường cao $AH$. Gọi $M$ là trung điểm của $AC$. Lấy $D$ đối xứng với $H$ qua $M$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $AHCD$ là một hình bình hành vì có hai đường chéo $AC$ và $HD$ cắt nhau tại trung điểm $M$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Vì $AH \\perp BC$ nên góc $\\widehat{AHC} = 90^\\circ$, suy ra $AHCD$ là hình chữ nhật.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng $AD$ song song và bằng đoạn thẳng $HC$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Tứ giác $ABHD$ là một hình thang vuông.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình chữ nhật $ABCD$ có diện tích $48\\text{ cm}^2$ và đường chéo $AC = 10\\text{ cm}$. Đặt độ dài hai cạnh là $a$ và $b$ ($a > b$).",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Hệ thức $a^2 + b^2 = 100$ và $a \\cdot b = 48$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài $(a + b)^2 = a^2 + b^2 + 2ab = 196$, suy ra nửa chu vi $a + b = 14\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Độ dài các cạnh của hình chữ nhật là $a = 8\\text{ cm}$ và $b = 6\\text{ cm}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Khoảng cách từ đỉnh $A$ đến đường chéo $BD$ bằng $5\\text{ cm}$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$ có chu vi $40\\text{ cm}$. Biết $AB = 3BC$. Tính độ dài đường chéo $AC$ (theo cm, làm tròn kết quả dạng căn thức: viết giá trị $AC^2$).",
        "answer": "250"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Tam giác $ABC$ vuông tại $A$ có $AB = 12\\text{ cm}, AC = 16\\text{ cm}$. Kẻ đường cao $AH$. Tính khoảng cách giữa hai trung điểm của $AH$ và $BC$ (theo cm).",
        "answer": "5"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Hình chữ nhật $ABCD$ có $AB = 8\\text{ cm}, BC = 6\\text{ cm}$. Kẻ $BH \\perp AC$. Tính độ dài đoạn thẳng $AH$ (theo cm).",
        "answer": "6.4"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình chữ nhật $ABCD$ và một điểm $M$ bất kì. Biết $MA = 3\\text{ cm}, MB = 5\\text{ cm}, MC = 6\\text{ cm}$. Tính độ dài đoạn thẳng $MD$ (theo cm, viết giá trị $MD^2$).",
        "answer": "20"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông tại $A$. Gọi $D, E, F$ lần lượt là trung điểm của các cạnh $AB, BC, CA$.\na) Chứng minh tứ giác $ADFE$ là hình chữ nhật.\nb) Biết $AB = 6\\text{ cm}, AC = 8\\text{ cm}$, tính độ dài đường chéo $DE$ của tứ giác.",
        "rubric": "a) D là trung điểm AB, E là trung điểm BC => DE là đường trung bình => DE // AC hay DE // AF. Tương tự EF // AB hay EF // AD => ADFE là hình bình hành. Lại có góc A = 90° => ADFE là hình chữ nhật (0.5đ)\nb) BC = căn(6² + 8²) = 10 cm. Trong tam giác vuông ABC, AE là trung tuyến ứng với cạnh huyền BC nên AE = BC/2 = 5 cm. Vì ADFE là hình chữ nhật nên DE = AE = 5 cm (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình chữ nhật $ABCD$. Kẻ $AK \\perp BD$ tại $K$ và $CP \\perp BD$ tại $P$.\na) Chứng minh tứ giác $AKCP$ là hình bình hành.\nb) Gọi $M$ là trung điểm của $BC$. Tia $AK$ cắt $BC$ tại $E$. Chứng minh $AE \\cdot AK = AB^2$ và tam giác $ABE$ đồng dạng với tam giác $KBA$.",
        "rubric": "a) AK vuông góc BD và CP vuông góc BD => AK // CP. Tam giác vuông AKD = tam giác vuông CPB (cạnh huyền - góc nhọn: AD = BC, góc ADK = góc PBC) => AK = CP. Tứ giác AKCP có AK // CP và AK = CP nên là hình bình hành (0.5đ)\nb) Tam giác ABE vuông tại B có đường cao BK... Chứng minh tam giác ABE đồng dạng tam giác KBA (g-g) => AB/AK = AE/AB => AE . AK = AB² (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình chữ nhật $ABCD$ và điểm $M$ tùy ý nằm trong hình chữ nhật.\na) Chứng minh hệ thức: $MA^2 + MC^2 = MB^2 + MD^2$.\nb) Ứng dụng: Cho $ABCD$ là mảnh vườn hình chữ nhật, cột đèn chiếu sáng đặt tại $M$ thỏa mãn khoảng cách $MA = 4\\text{ m}, MB = 5\\text{ m}, MC = 7\\text{ m}$. Tính khoảng cách từ cột đèn đến góc vườn $D$.",
        "rubric": "a) Qua M kẻ đường thẳng EF // AB (E thuộc AD, F thuộc BC) và GH // AD (G thuộc AB, H thuộc CD). Ta có AE = BF, ED = FC, AG = DH, GB = HC (0.25đ)\nÁp dụng định lí Pythagore:\nMA² + MC² = (AE² + AG²) + (ED² + HC²) (0.25đ)\nMB² + MD² = (BF² + GB²) + (ED² + DH²)\nDo các đoạn tương ứng bằng nhau nên MA² + MC² = MB² + MD² (ĐPCM) (0.25đ)\nb) Thay số: 4² + 7² = 5² + MD² <=> 16 + 49 = 25 + MD² <=> 65 = 25 + MD² => MD² = 40 => MD = căn(40) = 2.căn(10) m (khoảng 6.32 m) (0.25đ)"
      }
    ]
  },
  "c3_8_bai4_test3": {
    "title": "Toán 8 (KNTT) - Bài 13: Hình chữ nhật - Bài kiểm tra số 3 (🔥 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Giao điểm các đường phân giác của một tứ giác lồi tạo thành một hình chữ nhật khi và chỉ khi tứ giác đó là:",
        "options": [
          "Hình vuông",
          "Hình thoi",
          "Hình thang cân",
          "Hình bình hành"
        ],
        "correct": 3
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho hình chữ nhật $ABCD$ có chu vi $P$ và diện tích $S$. Hệ thức nào sau đây luôn đúng?",
        "options": [
          "$P^2 \\ge 16S$",
          "$P^2 = 8S$",
          "$P \\ge 4S$",
          "$P^2 \\le 16S$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hình chữ nhật có chu vi không đổi thì diện tích lớn nhất khi hình chữ nhật đó là:",
        "options": [
          "Hình bình hành",
          "Hình thoi",
          "Tam giác đều",
          "Hình vuông"
        ],
        "correct": 3
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tứ giác có hai trục đối xứng vuông góc với nhau và có một tâm đối xứng là:",
        "options": [
          "Chỉ có hình bình hành",
          "Chỉ có hình vuông",
          "Hình chữ nhật hoặc hình thoi",
          "Chỉ có hình chữ nhật"
        ],
        "correct": 2
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong hình chữ nhật $ABCD$, khoảng cách từ $A$ và $C$ đến đường chéo $BD$:",
        "options": [
          "$A$ gần hơn $C$",
          "Khác nhau",
          "$C$ gần hơn $A$",
          "Bằng nhau"
        ],
        "correct": 3
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Tam giác vuông có độ dài hai cạnh góc vuông là $a, b$. Bán kính đường tròn ngoại tiếp tam giác đó bằng:",
        "options": [
          "$\\frac{a + b}{2}$",
          "$\\frac{\\sqrt{a^2 + b^2}}{2}$",
          "$\\sqrt{a^2 + b^2}$",
          "$\\frac{ab}{2}$"
        ],
        "correct": 1
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$ có $AB = 2AD$. Gọi $E, F$ lần lượt là trung điểm của $AB, CD$. Tứ giác $AEFD$ là:",
        "options": [
          "Hình vuông",
          "Hình bình hành không vuông",
          "Hình chữ nhật",
          "Hình thoi"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$. Gọi $H$ là chân đường vuông góc kẻ từ $B$ đến $AC$. Biết $AH = 3\\text{ cm}, HC = 12\\text{ cm}$. Độ dài đường cao $BH$ bằng:",
        "options": [
          "$7.5\\text{ cm}$",
          "$4\\text{ cm}$",
          "$6\\text{ cm}$",
          "$9\\text{ cm}$"
        ],
        "correct": 2
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông cân tại $A$. Điểm $M$ thuộc cạnh huyền $BC$. Kẻ $MD \\perp AB, ME \\perp AC$. Chu vi tứ giác $ADME$ bằng:",
        "options": [
          "$2AB$",
          "$AB + AC$",
          "$4AB$",
          "$BC$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$ có $AC = 10\\text{ cm}$. Điểm $P$ tùy ý trên mặt phẳng. Giá trị nhỏ nhất của tổng $PA^2 + PC^2$ bằng:",
        "options": [
          "$25$",
          "$100$",
          "$50$",
          "$200$"
        ],
        "correct": 2
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$ có $AB = 8\\text{ cm}, BC = 6\\text{ cm}$. Điểm $E$ thuộc cạnh $CD$ sao cho diện tích tam giác $ADE$ bằng $\\frac{1}{4}$ diện tích hình chữ nhật. Độ dài $DE$ là:",
        "options": [
          "$2\\text{ cm}$",
          "$4\\text{ cm}$",
          "$6\\text{ cm}$",
          "$3\\text{ cm}$"
        ],
        "correct": 1
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$. Để tứ giác có các đỉnh là tâm đối xứng của các hình vuông dựng ra phía ngoài các cạnh của $ABCD$ là một hình vuông thì $ABCD$ cần là:",
        "options": [
          "Hình chữ nhật",
          "Hình bình hành bất kì",
          "Hình thang",
          "Hình thoi"
        ],
        "correct": 1
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ nhọn có ba đường cao $AD, BE, CF$ cắt nhau tại trực tâm $H$. Gọi $M$ là trung điểm của $BC$ và $K$ là điểm đối xứng của $H$ qua $M$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $BHCK$ là một hình bình hành vì có hai đường chéo cắt nhau tại trung điểm $M$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $BK$ vuông góc với $AB$ và $CK$ vuông góc với $AC$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Điểm $K$ nằm trên đường tròn ngoại tiếp tam giác $ABC$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Nếu $\\widehat{BAC} = 60^\\circ$ thì độ dài $AH = 2 \\cdot OM$ (với $O$ là tâm đường tròn ngoại tiếp $\\triangle ABC$).",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình chữ nhật $ABCD$. Trên cạnh $AB$ lấy điểm $E$, trên cạnh $CD$ lấy điểm $F$ sao cho $AE = CF$. Gọi $I$ là giao điểm của $EF$ và $AC$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $AECF$ là hình bình hành.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Điểm $I$ chính là tâm đối xứng của hình chữ nhật $ABCD$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Đường thẳng $EF$ luôn đi qua giao điểm của hai đường chéo $AC$ và $BD$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Độ dài đoạn thẳng $EF$ nhỏ nhất khi $E$ trùng với trung điểm của cạnh $AB$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình chữ nhật $ABCD$ có $AB = 8\\text{ cm}, BC = 6\\text{ cm}$. Phân giác góc $A$ cắt cạnh $CD$ tại điểm $E$. Tính diện tích tam giác $ADE$ (theo cm²).",
        "answer": "18"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH = 6\\text{ cm}$ và $HC = 9\\text{ cm}$. Tính độ dài đường trung tuyến $AM$ (theo cm).",
        "answer": "6.5"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hình chữ nhật $ABCD$ có diện tích $36\\text{ cm}^2$. Điểm $M$ nằm trên cạnh $AB$. Gọi $E, F$ lần lượt là hình chiếu của $M$ lên $AC$ và $BD$. Biết $AC = 10\\text{ cm}$. Tính giá trị của biểu thức $AC \\cdot (ME + MF)$ (theo cm²).",
        "answer": "36"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hình chữ nhật $ABCD$ có $AB = 4\\text{ cm}, BC = 3\\text{ cm}$. Điểm $M$ di động trên đường chéo $BD$. Tìm giá trị nhỏ nhất của tổng khoảng cách từ $M$ đến hai cạnh $AB$ và $AD$ (theo cm).",
        "answer": "2.4"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông cân tại $A$. Trên cạnh huyền $BC$ lấy điểm $M$ tùy ý. Kẻ $MD \\perp AB$ tại $D$ và $ME \\perp AC$ tại $E$.\na) Chứng minh tứ giác $ADME$ là hình chữ nhật.\nb) Chứng minh rằng khi $M$ thay đổi trên cạnh $BC$, chu vi tứ giác $ADME$ không đổi.",
        "rubric": "a) Tứ giác ADME có góc A = 90°, góc ADM = 90°, góc AEM = 90° nên là hình chữ nhật (0.5đ)\nb) Tam giác DBM vuông tại D có góc B = 45° nên là tam giác vuông cân => BD = DM. Do ADME là HCH nên DM = AE. Chu vi ADME = 2(AD + AE) = 2(AD + BD) = 2AB (không đổi) (0.5đ)"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình chữ nhật $ABCD$. Kẻ $BH \\perp AC$ tại $H$. Gọi $I, K$ lần lượt là trung điểm của $AH$ và $CD$.\na) Chứng minh $CI \\perp BI$.\nb) Chứng minh góc $\\widehat{BIK} = 90^\\circ$.",
        "rubric": "a) Gọi M là trung điểm BH => IM là đường trung bình tam giác ABH => IM // AB // CD và IM = AB/2 = KC => IMKC là HBH => IK // MC (0.5đ)\nb) Trong tam giác IBC, M là trực tâm => CM vuông góc IB. Mà IK // CM nên IK vuông góc IB => góc BIK = 90° (ĐPCM) (0.5đ)"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình chữ nhật $ABCD$ có diện tích $S$. Điểm $M$ nằm trong hình chữ nhật.\na) Chứng minh rằng: $S_{MAB} + S_{MCD} = \\frac{1}{2}S$.\nb) Tìm tập hợp các điểm $M$ nằm trong hình chữ nhật sao cho $S_{MAB} = S_{MCD}$.",
        "rubric": "a) Kẻ đường thẳng qua M vuông góc với AB tại E và CD tại F => EF là đường cao hình chữ nhật: EF = BC. S(MAB) + S(MCD) = 1/2 AB . ME + 1/2 CD . MF = 1/2 AB(ME + MF) = 1/2 AB . EF = 1/2 S (0.5đ)\nb) Để S(MAB) = S(MCD) <=> 1/2 AB . ME = 1/2 CD . MF <=> ME = MF (vì AB = CD). Vậy điểm M cách đều hai cạnh AB và CD, tức là M nằm trên đường trung bình nối trung điểm hai cạnh AD và BC của hình chữ nhật (0.5đ)"
      }
    ]
  }
};

if (typeof window !== 'undefined') {
  window.CHAPTER3_TOAN8_EXAMS = window.CHAPTER3_TOAN8_EXAMS || {};
  Object.assign(window.CHAPTER3_TOAN8_EXAMS, BAI_4_TOAN8_EXAMS);
  window.EXAMS_8_C3_8 = window.CHAPTER3_TOAN8_EXAMS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BAI_4_TOAN8_EXAMS;
}
