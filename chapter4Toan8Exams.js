// ==============================================================================
// NGÂN HÀNG ĐỀ KIỂM TRA CHƯƠNG IV: ĐỊNH LÍ THALÈS - TOÁN 8 (KNTT)
// Đầy đủ 4 bài học/chuyên đề x 3 đề kiểm tra = 12 đề kiểm tra chuẩn ma trận 10 điểm Bộ GD&ĐT
// Phân hóa độ khó rõ rệt: Đề 1 (Cơ bản) < Đề 2 (Khá) < Đề 3 (Nâng cao)
// ==============================================================================

const CHAPTER4_TOAN8_EXAMS = {
  "c4_8_bai1_test1": {
    "title": "Toán 8 (KNTT) - Bài 15: Định lí Thalès trong tam giác - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tỉ số của hai đoạn thẳng $AB = 4\text{ cm}$ và $CD = 10\text{ cm}$ bằng:",
        "options": [
          "$\frac{2}{5}$",
          "$\frac{5}{2}$",
          "$\frac{2}{3}$",
          "$\frac{1}{2}$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho bốn đoạn thẳng $AB, CD, A'B', C'D'$. Điều kiện để bốn đoạn thẳng đó tỉ lệ là:",
        "options": [
          "$\frac{AB}{CD} = \frac{A'B'}{C'D'}$",
          "$\frac{AB}{A'B'} = \frac{C'D'}{CD}$",
          "$AB \\cdot CD = A'B' \\cdot C'D'$",
          "$AB + CD = A'B' + C'D'$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho tam giác $ABC$, đường thẳng $d \\parallel BC$ cắt hai cạnh $AB, AC$ lần lượt tại $M, N$. Tỉ số nào sau đây là ĐÚNG theo định lí Thalès?",
        "options": [
          "$\frac{AM}{MB} = \frac{AN}{NC}$",
          "$\frac{AM}{AB} = \frac{NC}{AN}$",
          "$\frac{AM}{AN} = \frac{AB}{NC}$",
          "$\frac{MB}{AB} = \frac{AN}{AC}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Cho hình vẽ với $MN \\parallel BC$. Biết $AM = 3\text{ cm}, MB = 6\text{ cm}, AN = 4\text{ cm}$. Độ dài đoạn thẳng $NC$ là:",
        "options": [
          "$8\text{ cm}$",
          "$6\text{ cm}$",
          "$7\text{ cm}$",
          "$9\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Theo hệ quả của định lí Thalès, nếu đường thẳng song song với một cạnh của tam giác và cắt hai cạnh còn lại thì:",
        "options": [
          "Tạo thành một tam giác mới có ba cạnh tương ứng tỉ lệ với ba cạnh của tam giác đã cho",
          "Tạo thành một tam giác mới bằng tam giác đã cho",
          "Tạo thành một tam giác mới có diện tích bằng tam giác đã cho",
          "Tạo thành một tam giác vuông"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$ có $MN \\parallel BC$ ($M \\in AB, N \\in AC$). Khẳng định nào sau đây là hệ quả của định lí Thalès?",
        "options": [
          "$\frac{AM}{AB} = \frac{AN}{AC} = \frac{MN}{BC}$",
          "$\frac{AM}{MB} = \frac{AN}{NC} = \frac{MN}{BC}$",
          "$\frac{AM}{AB} = \frac{NC}{AC} = \frac{MN}{BC}$",
          "$\frac{MB}{AB} = \frac{AN}{AC} = \frac{MN}{BC}$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $MN \\parallel BC$ ($M \\in AB, N \\in AC$). Biết $AM = 2\text{ cm}, AB = 6\text{ cm}, BC = 9\text{ cm}$. Độ dài đoạn thẳng $MN$ bằng:",
        "options": [
          "$3\text{ cm}$",
          "$4\text{ cm}$",
          "$2.5\text{ cm}$",
          "$4.5\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$. Điểm $M$ thuộc cạnh $AB$, điểm $N$ thuộc cạnh $AC$ sao cho $AM = 2, MB = 4, AN = 3, NC = 6$. Khẳng định nào sau đây đúng?",
        "options": [
          "$MN \\parallel BC$",
          "$MN$ cắt $BC$",
          "$MN \\perp BC$",
          "$MN = BC$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Đo chiều cao của một cột cờ bằng bóng nắng: Một cọc tiêu cao $2\text{ m}$ cắm vuông góc với mặt đất có bóng dài $1.6\text{ m}$. Cùng thời điểm đó, bóng của cột cờ dài $8\text{ m}$. Chiều cao của cột cờ là:",
        "options": [
          "$10\text{ m}$",
          "$12\text{ m}$",
          "$9.6\text{ m}$",
          "$8.5\text{ m}$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $DE \\parallel BC$ ($D \\in AB, E \\in AC$). Biết $AD = 3\text{ cm}, DB = 5\text{ cm}$ và $AC = 16\text{ cm}$. Độ dài $AE$ là:",
        "options": [
          "$6\text{ cm}$",
          "$10\text{ cm}$",
          "$8\text{ cm}$",
          "$9.6\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Một đường thẳng song song với hai đáy cắt hai cạnh bên $AD$ và $BC$ lần lượt tại $M$ và $N$. Hệ thức nào sau đây đúng?",
        "options": [
          "$\frac{AM}{MD} = \frac{BN}{NC}$",
          "$\frac{AM}{AD} = \frac{NC}{BC}$",
          "$\frac{AM}{MB} = \frac{DN}{NC}$",
          "$\frac{MD}{AD} = \frac{BN}{BC}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $MN \\parallel BC$ ($M \\in AB, N \\in AC$). Biết $\frac{AM}{MB} = \frac{1}{2}$. Tỉ số $\frac{MN}{BC}$ bằng:",
        "options": [
          "$\frac{1}{3}$",
          "$\frac{1}{2}$",
          "$\frac{2}{3}$",
          "$\frac{1}{4}$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$, đường thẳng $d$ song song với $BC$ cắt cạnh $AB$ tại $M$ và cắt cạnh $AC$ tại $N$. Biết $AM = 4\text{ cm}, MB = 2\text{ cm}, AN = 6\text{ cm}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $AB = 6\text{ cm}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Theo định lí Thalès, độ dài đoạn thẳng $NC = 3\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tỉ số $\frac{AM}{AB} = \frac{2}{3}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Nếu $BC = 12\text{ cm}$ thì độ dài $MN = 9\text{ cm}$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ có $AB = 10\text{ cm}, AC = 15\text{ cm}$. Trên cạnh $AB$ lấy điểm $D$ sao cho $AD = 4\text{ cm}$, trên cạnh $AC$ lấy điểm $E$ sao cho $AE = 6\text{ cm}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tỉ số $\frac{AD}{AB} = \frac{2}{5}$ và $\frac{AE}{AC} = \frac{2}{5}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $DE$ song song với cạnh $BC$ theo định lí Thalès đảo.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Độ dài đoạn thẳng $DB = 6\text{ cm}$ và $EC = 9\text{ cm}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Tỉ số $\frac{DE}{BC} = \frac{4}{9}$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $MN \\parallel BC$ ($M \\in AB, N \\in AC$). Biết $AM = 6, MB = 4, AN = 9$. Tính độ dài $NC$.",
        "answer": "6"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $DE \\parallel BC$ ($D \\in AB, E \\in AC$). Biết $AD = 3, AB = 12$ và $BC = 20$. Tính độ dài đoạn thẳng $DE$.",
        "answer": "5"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Để đo khoảng cách giữa hai điểm $A$ và $B$ bị ngăn cách bởi hồ nước, người ta chọn điểm $C$ và lấy hai điểm $M, N$ lần lượt trên $CA, CB$ sao cho $MN \\parallel AB$. Biết $CM = 20\text{ m}, CA = 50\text{ m}$ và đo được $MN = 32\text{ m}$. Khoảng cách $AB$ bằng bao nhiêu mét?",
        "answer": "80"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$ có diện tích bằng $45\text{ cm}^2$. Trên cạnh $AB$ lấy điểm $M$ sao cho $AM = \frac{1}{3}AB$. Kẻ $MN \\parallel BC$ ($N \\in AC$). Tính diện tích hình thang $MN C B$ theo đơn vị $\text{cm}^2$.",
        "answer": "40"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Một đường thẳng song song với cạnh $BC$ cắt cạnh $AB$ tại $D$ và cắt cạnh $AC$ tại $E$. Biết $AD = 6\text{ cm}, DB = 9\text{ cm}, AE = 8\text{ cm}$.\na) Tính độ dài đoạn thẳng $EC$ và $AC$.\nb) Biết $BC = 20\text{ cm}$, tính độ dài đoạn thẳng $DE$.",
        "rubric": "a) Áp dụng định lí Thalès: AD/DB = AE/EC <=> 6/9 = 8/EC => EC = (9*8)/6 = 12 cm (0.25đ). Tính AC = AE + EC = 8 + 12 = 20 cm (0.25đ).\nb) Ta có AB = AD + DB = 6 + 9 = 15 cm. Áp dụng hệ quả định lí Thalès: DE/BC = AD/AB <=> DE/20 = 6/15 => DE = (20*6)/15 = 8 cm (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$, $AB < CD$). Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Qua $O$ kẻ đường thẳng song song với $AB$ cắt hai cạnh bên $AD$ và $BC$ lần lượt tại $M$ và $N$.\na) Chứng minh rằng $\frac{AM}{MD} = \frac{BN}{NC}$.\nb) Chứng minh rằng $OM = ON$.",
        "rubric": "a) Xét tam giác ADC có MO // CD => AM/MD = AO/OC (1) (0.25đ). Xét tam giác ABC có ON // AB => BN/NC = AO/OC (2). Từ (1) và (2) suy ra AM/MD = BN/NC (0.25đ).\nb) Xét tam giác ADC có MO // CD => OM/CD = AO/AC (0.25đ). Xét tam giác BDC có ON // CD => ON/CD = BN/BC. Mà BN/BC = AO/AC nên OM/CD = ON/CD => OM = ON (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tam giác $ABC$ có trung tuyến $AM$. Một đường thẳng $d$ bất kì đi qua điểm $M$ cắt cạnh $AB$ tại $D$ và cắt tia đối của tia $CA$ tại $E$.\nChứng minh hệ thức: $\frac{AB}{AD} - \frac{AC}{AE} = 1$.",
        "rubric": "Từ B và C kẻ các đường thẳng song song với d cắt AC lần lượt tại K và H (hoặc kẻ từ B và C các đường song song với AM). Cách ngắn nhất: Kẻ BK // d (K thuộc AC) và CI // d. Vì M là trung điểm BC nên khoảng cách từ B và C đến d bằng nhau (0.5đ). Áp dụng định lí Thalès: AB/AD = AK/AM và AC/AE = ... biến đổi tỉ số: AB/AD = 1 + BD/AD; AC/AE = CE/AE - 1. Dùng tỉ số qua trung điểm M suy ra AB/AD - AC/AE = 1 (0.5đ)."
      }
    ]
  },
  "c4_8_bai1_test2": {
    "title": "Toán 8 (KNTT) - Bài 15: Định lí Thalès trong tam giác - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho đoạn thẳng $AB = 8\text{ cm}$. Điểm $C$ nằm trên đoạn thẳng $AB$ sao cho $\frac{CA}{CB} = \frac{3}{5}$. Độ dài đoạn thẳng $CA$ là:",
        "options": [
          "$3\text{ cm}$",
          "$5\text{ cm}$",
          "$4\text{ cm}$",
          "$4.8\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho tam giác $ABC$ có $MN \\parallel BC$ ($M \\in AB, N \\in AC$). Biết $AM = 2MB$. Tỉ số $\frac{AN}{AC}$ bằng:",
        "options": [
          "$\frac{2}{3}$",
          "$\frac{1}{2}$",
          "$\frac{2}{1}$",
          "$\frac{1}{3}$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Giao điểm hai đường chéo là $O$. Tỉ số nào sau đây luôn đúng?",
        "options": [
          "$\frac{OA}{OC} = \frac{OB}{OD}$",
          "$\frac{OA}{OB} = \frac{OC}{OD}$",
          "$\frac{OA}{OD} = \frac{OB}{OC}$",
          "$\frac{OA}{OC} = \frac{OD}{OB}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $AB = 12\text{ cm}, AC = 18\text{ cm}$. Trên $AB$ lấy $D$ sao cho $BD = 4\text{ cm}$, trên $AC$ lấy $E$ sao cho $CE = 6\text{ cm}$. Kết luận nào sau đây đúng?",
        "options": [
          "$DE \\parallel BC$",
          "$DE$ không song song $BC$",
          "$DE \\perp BC$",
          "$DE = \frac{1}{2}BC$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$) có $AB = 4\text{ cm}, CD = 10\text{ cm}$. Đường thẳng song song với hai đáy cắt hai cạnh bên $AD, BC$ tại $M, N$ sao cho $AM = 2MD$. Độ dài đoạn thẳng $MN$ bằng:",
        "options": [
          "$8\text{ cm}$",
          "$7\text{ cm}$",
          "$6\text{ cm}$",
          "$7.5\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$. Đường thẳng song song với $BC$ cắt $AB$ tại $D$ và $AC$ tại $E$. Biết $AD = x, DB = 2, AE = 3, EC = x - 1$. Giá trị của $x$ là:",
        "options": [
          "$3$",
          "$2$",
          "$4$",
          "$1$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$. Điểm $F$ thuộc cạnh $BC$. Tia $AF$ cắt đường thẳng $CD$ tại $E$. Tỉ số $\frac{AF}{AE}$ bằng tỉ số nào dưới đây?",
        "options": [
          "$\frac{BF}{BC}$",
          "$\frac{CF}{BC}$",
          "$\frac{AB}{CD}$",
          "$\frac{DF}{BC}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $BC = 12\text{ cm}$. Trên cạnh $AB$ lấy hai điểm $M, P$ sao cho $AM = MP = PB$. Kẻ $MN \\parallel BC$ và $PQ \\parallel BC$ ($N, Q \\in AC$). Độ dài đoạn thẳng $MN$ và $PQ$ lần lượt là:",
        "options": [
          "$4\text{ cm}$ và $8\text{ cm}$",
          "$3\text{ cm}$ và $6\text{ cm}$",
          "$4\text{ cm}$ và $6\text{ cm}$",
          "$5\text{ cm}$ và $10\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ vuông tại $A$ có $AB = 6, AC = 8$. Lấy điểm $M$ trên $AB$ sao cho $AM = 3$. Kẻ $MN \\parallel BC$ ($N \\in AC$). Độ dài đoạn thẳng $MN$ bằng:",
        "options": [
          "$5$",
          "$4$",
          "$4.5$",
          "$6$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có trung tuyến $AM$. Đường thẳng song song với $BC$ cắt $AB, AM, AC$ lần lượt tại $D, I, E$. Khẳng định nào sau đây là đúng?",
        "options": [
          "$I$ là trung điểm của $DE$",
          "$ID = 2IE$",
          "$IE = 2ID$",
          "$DE = 2AM$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$. Điểm $D$ trên cạnh $BC$. Đường thẳng qua $D$ song song với $AB$ cắt $AC$ tại $E$, đường thẳng qua $D$ song song với $AC$ cắt $AB$ tại $F$. Giá trị của tổng $\frac{AE}{AC} + \frac{AF}{AB}$ bằng:",
        "options": [
          "$1$",
          "$2$",
          "$\frac{1}{2}$",
          "$\frac{3}{2}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$. Một đường thẳng cắt $AB$ tại $D$ và $AC$ tại $E$. Để $DE \\parallel BC$ thì điều kiện cần và đủ là:",
        "options": [
          "$\frac{AD}{BD} = \frac{AE}{CE}$",
          "$\frac{AD}{AE} = \frac{BD}{BC}$",
          "$\frac{AD}{AB} = \frac{EC}{AC}$",
          "$AD = AE$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho hình bình hành $ABCD$. Qua đỉnh $A$ kẻ đường thẳng cắt đường chéo $BD$ tại $P$, cắt cạnh $BC$ tại $Q$ và cắt tia đối của tia $DC$ tại $R$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Do $AB \\parallel CR$ nên $\frac{AP}{PR} = \frac{BP}{PD}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Do $AD \\parallel BQ$ nên $\frac{PQ}{AP} = \frac{BP}{PD}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Hệ thức $AP^2 = PQ \\cdot PR$ là một hệ thức đúng.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Độ dài $AP$ bằng trung bình cộng của $PQ$ và $PR$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ nhọn. Lấy điểm $D$ trên cạnh $AB$, điểm $E$ trên cạnh $AC$ sao cho $DE \\parallel BC$. Biết $AD = 4\text{ cm}, DB = 6\text{ cm}, BC = 15\text{ cm}$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tỉ số đồng dạng giữa $\triangle ADE$ và $\triangle ABC$ bằng $\frac{2}{5}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $DE = 6\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tỉ số diện tích $\frac{S_{\triangle ADE}}{S_{\triangle ABC}} = \frac{4}{25}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Diện tích tứ giác $BDEC$ chiếm $\frac{21}{25}$ diện tích tam giác $ABC$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $AB = 15\text{ cm}$. Lấy điểm $M$ trên $AB$ sao cho $AM = 5\text{ cm}$. Kẻ $MN \\parallel BC$ ($N \\in AC$). Tỉ số diện tích $\frac{S_{\triangle ABC}}{S_{\triangle AMN}}$ bằng bao nhiêu?",
        "answer": "9"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$) có $AB = 6\text{ cm}, CD = 14\text{ cm}$. Hai đường chéo cắt nhau tại $O$. Qua $O$ kẻ đường thẳng song song với đáy cắt $AD$ tại $M$. Tính độ dài đoạn thẳng $OM$ (kết quả dạng số thập phân, ví dụ 4.2).",
        "answer": "4.2"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho $\triangle ABC$ có $DE \\parallel BC$ ($D \\in AB, E \\in AC$). Biết $AD = x + 1, DB = 3, AE = x + 3, EC = 5$. Tìm giá trị của $x$.",
        "answer": "2"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$ có diện tích bằng $60\text{ cm}^2$. Trên cạnh $BC$ lấy điểm $D$ sao cho $BD = 2DC$. Kẻ $DE \\parallel AB$ ($E \\in AC$) và $DF \\parallel AC$ ($F \\in AB$). Tính diện tích của tứ giác $AEDF$ theo đơn vị $\text{cm}^2$.",
        "answer": "26.67"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$.\na) Chứng minh rằng $OA \\cdot OD = OB \\cdot OC$.\nb) Đường thẳng qua $O$ song song với $AB$ cắt $AD$ tại $M$ và cắt $BC$ tại $N$. Chứng minh rằng $\frac{1}{AB} + \frac{1}{CD} = \frac{2}{MN}$.",
        "rubric": "a) Vì AB // CD nên áp dụng hệ quả Thalès: OA/OC = OB/OD => OA * OD = OB * OC (0.5đ).\nb) Ta có OM/AB = OD/BD và OM/CD = OA/AC = OB/BD. Cộng lại: OM/AB + OM/CD = (OD + OB)/BD = 1 => 1/AB + 1/CD = 1/OM. Vì OM = ON nên MN = 2OM => 1/OM = 2/MN. Vậy 1/AB + 1/CD = 2/MN (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ nhọn. Các đường cao $BD$ và $CE$ cắt nhau tại $H$.\na) Chứng minh rằng $AE \\cdot AB = AD \\cdot AC$.\nb) Qua $D$ kẻ đường thẳng vuông góc với $AC$ cắt $BC$ tại $M$. Qua $E$ kẻ đường thẳng vuông góc với $AB$ cắt $BC$ tại $N$. Chứng minh rằng $MN \\parallel DE$.",
        "rubric": "a) Xét tam giác ADB và tam giác AEC vuông: góc A chung => tam giác ADB đồng dạng tam giác AEC (g-g) => AD/AE = AB/AC => AE * AB = AD * AC (0.5đ).\nb) Dùng định lí Thalès kết hợp hình chiếu vuông góc, tỉ số đoạn thẳng trên BC tương ứng bằng nhau => MN // DE theo định lí Thalès đảo (0.5đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tam giác $ABC$. Lấy điểm $D$ trên cạnh $BC$. Một đường thẳng song song với $AD$ cắt các đường thẳng $AB, AC$ và đường thẳng qua $D$ song song với $AC$ lần lượt tại $E, F$ và $G$.\nChứng minh rằng $AD^2 = EF \\cdot EG$ nếu $D$ là trung điểm của $BC$.",
        "rubric": "Áp dụng định lí Thalès trong các tam giác có các đường thẳng song song: EF/AD = BE/BA và EG/AD = ... Biến đổi các tỉ số kết hợp giả thiết D là trung điểm BC: thiết lập tích các tỉ số bằng 1, suy ra AD^2 = EF * EG (1.0đ)."
      }
    ]
  },
  "c4_8_bai1_test3": {
    "title": "Toán 8 (KNTT) - Bài 15: Định lí Thalès trong tam giác - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$. Một đường thẳng $d$ cắt $AB$ tại $D$, $AC$ tại $E$ và cắt tia đối của $BC$ tại $F$. Đẳng thức nào sau đây biểu diễn định lí Menelaus?",
        "options": [
          "$\frac{DA}{DB} \\cdot \frac{FC}{FB} \\cdot \frac{EB}{EC} = 1$",
          "$\frac{AD}{DB} \\cdot \frac{BF}{FC} \\cdot \frac{CE}{EA} = 1$",
          "$\frac{AD}{AB} \\cdot \frac{BE}{EC} \\cdot \frac{CF}{FA} = 1$",
          "$\frac{AD}{DB} \\cdot \frac{BE}{EC} \\cdot \frac{CF}{FA} = 1$"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có ba trung tuyến $AD, BE, CF$ đồng quy tại trọng tâm $G$. Tỉ số $\frac{GA}{GD} \\cdot \frac{GB}{GE} \\cdot \frac{GC}{GF}$ bằng:",
        "options": [
          "$8$",
          "$6$",
          "$4$",
          "$1$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Các điểm $D, E, F$ lần lượt nằm trên $BC, CA, AB$ sao cho $AD, BE, CF$ đồng quy tại $O$. Theo định lí Ceva:",
        "options": [
          "$\frac{AF}{FB} \\cdot \frac{BD}{DC} \\cdot \frac{CE}{EA} = 1$",
          "$\frac{AF}{FB} \\cdot \frac{BD}{DC} \\cdot \frac{CE}{EA} = -1$",
          "$\frac{AF}{AB} \\cdot \frac{BD}{BC} \\cdot \frac{CE}{CA} = 1$",
          "$\frac{AB}{AF} + \frac{BC}{BD} + \frac{CA}{CE} = 1$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $M$ là trung điểm của $CD$. Giao điểm của $AM$ và $BD$ là $E$, giao điểm của $BM$ và $AC$ là $F$. Kết luận nào sau đây đúng?",
        "options": [
          "$EF \\parallel AB$",
          "$EF \\perp AB$",
          "$EF = AB$",
          "$EF = CD$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Lấy điểm $D$ trên cạnh $AB$ sao cho $AD = 2DB$, điểm $E$ trên $AC$ sao cho $AE = 2EC$. Điểm $M$ bất kì trong tam giác. Diện tích tam giác $ADE$ bằng bao nhiêu phần diện tích $\triangle ABC$?",
        "options": [
          "$\frac{4}{9}$",
          "$\frac{2}{3}$",
          "$\frac{1}{3}$",
          "$\frac{4}{5}$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Vận dụng thấp",
        "question": "Cho tứ giác $ABCD$. Gọi $E, F$ lần lượt là giao điểm của $AB$ và $CD$, của $AD$ và $BC$. Đường thẳng qua $E$ song song với $BC$ cắt $BD$ tại $M$, đường thẳng qua $E$ song song với $AD$ cắt $AC$ tại $N$. Khi đó:",
        "options": [
          "$MN \\parallel CD$",
          "$MN \\perp CD$",
          "$MN = CD$",
          "$MN$ đi qua $F$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Lấy $M$ trên $BC$ sao cho $BM = 3MC$. Lấy $N$ trên $AM$ sao cho $AN = 2NM$. Đường thẳng $BN$ cắt $AC$ tại $P$. Tỉ số $\frac{AP}{PC}$ bằng:",
        "options": [
          "$\frac{2}{3}$",
          "$\frac{1}{2}$",
          "$\frac{3}{2}$",
          "$\frac{3}{4}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Qua $O$ vẽ đường thẳng song song với $AB$ cắt $AD, BC$ tại $E, F$. Biết $AB = a, CD = b$. Độ dài $EF$ bằng:",
        "options": [
          "$\frac{2ab}{a+b}$",
          "$\frac{ab}{a+b}$",
          "$\frac{a+b}{2}$",
          "$\\sqrt{ab}$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ có trọng tâm $G$. Một đường thẳng đi qua $G$ cắt hai cạnh $AB, AC$ lần lượt tại $M, N$. Giá trị của biểu thức $\frac{AB}{AM} + \frac{AC}{AN}$ bằng:",
        "options": [
          "$3$",
          "$2$",
          "$4$",
          "$\frac{3}{2}$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$. Lấy $D$ thuộc cạnh $BC$. Từ $D$ kẻ đường thẳng song song với $AB$ cắt $AC$ tại $E$, kẻ đường thẳng song song với $AC$ cắt $AB$ tại $F$. Giá trị lớn nhất của tích diện tích $S_{\triangle BDF} \\cdot S_{\triangle CDE}$ là:",
        "options": [
          "$\frac{1}{16} S_{\triangle ABC}^2$",
          "$\frac{1}{4} S_{\triangle ABC}^2$",
          "$\frac{1}{8} S_{\triangle ABC}^2$",
          "$\frac{1}{9} S_{\triangle ABC}^2$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Cho hình bình hành $ABCD$. Điểm $M$ thuộc $AB$, $N$ thuộc $BC$ sao cho $AM = CN$. $DM$ cắt $BN$ tại $P$. Tỉ số $\frac{DP}{PM}$ phụ thuộc vào:",
        "options": [
          "Tỉ số $\frac{AM}{AB}$ và kích thước hình bình hành",
          "Chỉ phụ thuộc góc $A$",
          "Không phụ thuộc vào $M, N$",
          "Luôn bằng $1$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho tứ giác lồi $ABCD$. Các đường thẳng $AB$ và $CD$ cắt nhau tại $E$, $AD$ và $BC$ cắt nhau tại $F$. Trung điểm các đoạn thẳng $AC, BD, EF$ cùng nằm trên một đường thẳng. Đường thẳng này được gọi là:",
        "options": [
          "Đường thẳng Gauss (Newton)",
          "Đường thẳng Euler",
          "Đường thẳng Simson",
          "Đường thẳng Steiner"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$. Trên cạnh $AB$ lấy điểm $D$ sao cho $AD = 2DB$. Trên cạnh $AC$ lấy điểm $E$ sao cho $EC = 3AE$. Gọi $K$ là giao điểm của $BE$ và $CD$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tỉ số $\frac{AD}{AB} = \frac{2}{3}$ và $\frac{AE}{AC} = \frac{1}{4}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng $DE$ không song song với cạnh $BC$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng cao",
            "text": "Áp dụng định lí Menelaus cho tam giác $ADC$ với cát tuyến $B - K - E$, ta có $\frac{KB}{KE} = \frac{11}{2}$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Tỉ số diện tích $\frac{S_{\triangle KBC}}{S_{\triangle ABC}} = \frac{6}{11}$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình thang $ABCD$ ($AB \\parallel CD$, $AB < CD$). Hai đường chéo $AC$ và $BD$ cắt nhau tại $O$, hai cạnh bên $AD$ và $BC$ cắt nhau tại $K$. Đường thẳng $KO$ cắt $AB$ tại $M$ và cắt $CD$ tại $N$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Theo hệ quả định lí Thalès, $\frac{KM}{KN} = \frac{AB}{CD}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Vận dụng thấp",
            "text": "Điểm $M$ là trung điểm của đáy $AB$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Điểm $N$ là trung điểm của đáy $CD$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Đường thẳng $MN$ không đi qua trung điểm của đoạn thẳng nối trung điểm hai đường chéo.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có trọng tâm $G$. Đường thẳng $d$ qua $G$ song song với $BC$ cắt $AB, AC$ lần lượt tại $M, N$. Biết $BC = 18\text{ cm}$. Tính độ dài đoạn thẳng $MN$ theo cm.",
        "answer": "12"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho $\triangle ABC$. Lấy $D$ trên cạnh $BC$ sao cho $BD = \frac{1}{3}BC$. Lấy $E$ trên $AD$ sao cho $AE = \frac{1}{2}ED$. Đường thẳng $BE$ cắt $AC$ tại $K$. Tính tỉ số $\frac{AK}{KC}$ (kết quả dạng phân số tối giản a/b, điền a/b).",
        "answer": "1/5"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$) có $AB = 4, CD = 9$. Gọi $O$ là giao điểm hai đường chéo. Qua $O$ kẻ đường thẳng song song với $AB$ cắt $AD, BC$ tại $M, N$. Tính độ dài $MN$ (kết quả dạng số thập phân làm tròn 2 chữ số sau dấu phẩy).",
        "answer": "5.54"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$ có diện tích bằng $72\text{ cm}^2$. Điểm $M$ di động trên cạnh $BC$. Từ $M$ kẻ các đường thẳng song song với $AB$ và $AC$ tạo thành một hình bình hành với hai cạnh nằm trên $AB, AC$. Diện tích lớn nhất của hình bình hành này bằng bao nhiêu $\text{cm}^2$?",
        "answer": "36"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $M, N$ lần lượt là trung điểm của $AB$ và $CD$. Đường thẳng $MN$ cắt đường thẳng $AD$ tại $E$ và cắt $BC$ tại $F$.\nChứng minh rằng $EA \\cdot ED = EB \\cdot EC$ (hoặc $\frac{EA}{ED} = \frac{EB}{EC}$).",
        "rubric": "Áp dụng định lí Thalès cho tam giác EDC có AB // CD: EA/ED = EB/EC = AB/CD (0.5đ). Từ đó suy ra tỉ số đồng dạng và tích đoạn thẳng tương ứng (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Trên tia đối của tia $BA$ lấy điểm $D$ sao cho $BD = BA$. Trên cạnh $BC$ lấy điểm $E$ sao cho $BE = \frac{1}{3}BC$. Gọi $K$ là giao điểm của $AE$ và $CD$.\na) Chứng minh rằng $K$ là trung điểm của $CD$.\nb) Tính tỉ số $\frac{AK}{KE}$.",
        "rubric": "a) Xét tam giác ADC có đường trung tuyến CB. Điểm E chia BC theo tỉ số BE = 1/3 BC nên E là trọng tâm tam giác ADC => AE là đường trung tuyến thứ hai => AE đi qua trung điểm K của CD (0.5đ).\nb) Theo tính chất trọng tâm tam giác ADC: AE = 2/3 AK => AK/KE = 3 (hoặc AE/EK = 2/1) (0.5đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tam giác $ABC$ có ba góc nhọn. Một điểm $P$ nằm trong tam giác. Gọi $D, E, F$ lần lượt là hình chiếu vuông góc của $P$ lên các cạnh $BC, CA, AB$.\nChứng minh rằng $P$ trùng với tâm đường tròn nội tiếp tam giác $ABC$ khi và chỉ khi biểu thức $T = \frac{PD}{h_a} + \frac{PE}{h_b} + \frac{PF}{h_c} = 1$ (với $h_a, h_b, h_c$ là các đường cao tương ứng của $\triangle ABC$).",
        "rubric": "Nhận xét tổng diện tích: S(PBC) + S(PCA) + S(PAB) = S(ABC) (0.25đ). Ta có S(PBC)/S(ABC) = (1/2 a * PD)/(1/2 a * h_a) = PD/h_a. Tương tự PE/h_b = S(PCA)/S, PF/h_c = S(PAB)/S (0.25đ). Do đó tổng PD/h_a + PE/h_b + PF/h_c luôn bằng 1 với MỌI điểm P nằm trong tam giác (0.25đ). Kết hợp điều kiện P là tâm nội tiếp khi và chỉ khi PD = PE = PF = r, suy ra r(1/h_a + 1/h_b + 1/h_c) = 1 (0.25đ)."
      }
    ]
  },
  "c4_8_bai2_test1": {
    "title": "Toán 8 (KNTT) - Bài 16: Đường trung bình của tam giác - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đường trung bình của tam giác là đoạn thẳng:",
        "options": [
          "Nối trung điểm hai cạnh của tam giác",
          "Nối từ đỉnh đến trung điểm cạnh đối diện",
          "Vuông góc từ đỉnh xuống cạnh đối diện",
          "Chia đôi một góc của tam giác"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Một tam giác có bao nhiêu đường trung bình?",
        "options": [
          "$3$",
          "$1$",
          "$2$",
          "$4$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Đường trung bình của tam giác có tính chất nào sau đây?",
        "options": [
          "Song song với cạnh thứ ba và bằng nửa cạnh ấy",
          "Vuông góc với cạnh thứ ba",
          "Bằng một phần ba cạnh thứ ba",
          "Đi qua trọng tâm tam giác"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$ có $M, N$ lần lượt là trung điểm của $AB$ và $AC$. Biết $BC = 12\text{ cm}$. Độ dài đoạn thẳng $MN$ là:",
        "options": [
          "$6\text{ cm}$",
          "$24\text{ cm}$",
          "$4\text{ cm}$",
          "$3\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Cho tam giác $ABC$ có chu vi bằng $24\text{ cm}$. Gọi $D, E, F$ lần lượt là trung điểm của ba cạnh $AB, BC, CA$. Chu vi tam giác $DEF$ bằng:",
        "options": [
          "$12\text{ cm}$",
          "$6\text{ cm}$",
          "$48\text{ cm}$",
          "$8\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Đường thẳng đi qua trung điểm một cạnh của tam giác và song song với cạnh thứ hai thì:",
        "options": [
          "Đi qua trung điểm của cạnh thứ ba",
          "Vuông góc với cạnh thứ ba",
          "Bằng cạnh thứ hai",
          "Trùng với đường cao"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $M$ là trung điểm $AB$. Đường thẳng qua $M$ song song với $BC$ cắt $AC$ tại $N$. Biết $AC = 10\text{ cm}$. Độ dài đoạn thẳng $AN$ là:",
        "options": [
          "$5\text{ cm}$",
          "$2.5\text{ cm}$",
          "$10\text{ cm}$",
          "$7.5\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có các đường trung bình $DE, EF, FD$. Diện tích tam giác $DEF$ bằng bao nhiêu phần diện tích $\triangle ABC$?",
        "options": [
          "$\frac{1}{4}$",
          "$\frac{1}{2}$",
          "$\frac{1}{3}$",
          "$\frac{1}{8}$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ cân tại $A$ có $AB = AC = 10\text{ cm}, BC = 12\text{ cm}$. Gọi $M, N$ lần lượt là trung điểm của $AB, AC$. Tứ giác $BMNC$ là hình gì?",
        "options": [
          "Hình thang cân",
          "Hình bình hành",
          "Hình chữ nhật",
          "Hình thoi"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\text{ cm}, AC = 8\text{ cm}$. Gọi $M, N$ lần lượt là trung điểm của $AB, AC$. Độ dài $MN$ bằng:",
        "options": [
          "$5\text{ cm}$",
          "$10\text{ cm}$",
          "$7\text{ cm}$",
          "$4.5\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tứ giác có bốn đỉnh là bốn trung điểm của các cạnh của một tứ giác bất kì luôn là:",
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
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $M, N$ lần lượt là trung điểm của hai cạnh bên $AD$ và $BC$. Đoạn thẳng $MN$ có độ dài bằng:",
        "options": [
          "$\frac{AB + CD}{2}$",
          "$\frac{CD - AB}{2}$",
          "$\\sqrt{AB \\cdot CD}$",
          "$AB + CD$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ có $AB = 8\text{ cm}, AC = 10\text{ cm}, BC = 12\text{ cm}$. Gọi $D, E, F$ lần lượt là trung điểm của các cạnh $AB, AC, BC$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $DE$ là đường trung bình của tam giác $ABC$ và $DE = 6\text{ cm}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $DF = 5\text{ cm}$ và $EF = 4\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Chu vi tam giác $DEF$ bằng $15\text{ cm}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Tứ giác $BDEF$ là hình chữ nhật.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình chữ nhật $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Gọi $M, N$ lần lượt là trung điểm của $OA$ và $OB$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $MN$ là đường trung bình của tam giác $OAB$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $MN$ song song với cạnh $AB$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Độ dài $MN = \frac{1}{2}AB$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Tứ giác $MNCD$ là hình bình hành.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có chu vi bằng $36\text{ cm}$. Nối trung điểm ba cạnh của $\triangle ABC$ ta được tam giác mới có chu vi bằng bao nhiêu cm?",
        "answer": "18"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $M, N$ lần lượt là trung điểm của $AB, AC$. Biết $MN = 7.5\text{ cm}$. Tính độ dài cạnh $BC$ theo cm.",
        "answer": "15"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho tứ giác $ABCD$ có hai đường chéo $AC = 16\text{ cm}$ và $BD = 12\text{ cm}$ vuông góc với nhau. Nối trung điểm bốn cạnh của tứ giác $ABCD$ ta được một hình chữ nhật có chu vi bằng bao nhiêu cm?",
        "answer": "28"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$ vuông tại $A$, đường cao $AH = 12\text{ cm}, BC = 25\text{ cm}$. Gọi $M, N$ lần lượt là hình chiếu của $H$ lên $AB, AC$. Tính độ dài đoạn thẳng $MN$ theo cm.",
        "answer": "12"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Gọi $M, N, P$ lần lượt là trung điểm của các cạnh $AB, AC, BC$.\na) Chứng minh tứ giác $BMNP$ là hình bình hành.\nb) Tam giác $ABC$ cần thêm điều kiện gì để tứ giác $BMNP$ là hình thoi?",
        "rubric": "a) MN là đường trung bình của tam giác ABC => MN // BC và MN = 1/2 BC = BP. Tứ giác BMNP có một cặp cạnh đối song song và bằng nhau (MN // BP và MN = BP) nên là hình bình hành (0.5đ).\nb) Hình bình hành BMNP là hình thoi <=> BM = BP <=> 1/2 AB = 1/2 BC <=> AB = BC. Vậy tam giác ABC phải cân tại B (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Trên tia đối của tia $BA$ lấy điểm $D$ sao cho $BD = BA$. Trên cạnh $BC$ lấy điểm $E$ sao cho $BE = \frac{1}{2}EC$. Gọi $M$ là giao điểm của $AE$ và $DC$.\na) Chứng minh rằng $E$ là trung điểm của đoạn thẳng nối trung điểm của $AB$ và $DC$.\nb) Chứng minh rằng $M$ là trung điểm của $DC$.",
        "rubric": "a) Lấy K là trung điểm của EC => BE = EK = KC => K là trung điểm của EC và E là trung điểm của BK (0.25đ). Trong tam giác ADC, nối BK và chứng minh các tính chất song song theo đường trung bình (0.25đ).\nb) Áp dụng định lí đường trung bình trong tam giác: chứng minh AE đi qua trung điểm M của DC (0.5đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tứ giác lồi $ABCD$. Gọi $M, N$ lần lượt là trung điểm của hai cạnh đối diện $AD$ và $BC$. Chứng minh rằng $MN \\le \frac{AB + CD}{2}$. Dấu đẳng thức xảy ra khi nào?",
        "rubric": "Lấy điểm K là trung điểm đường chéo AC (0.25đ). Trong tam giác ACD có MK là đường trung bình => MK = CD/2 và MK // CD (0.25đ). Trong tam giác ABC có NK là đường trung bình => NK = AB/2 và NK // AB (0.25đ). Xét 3 điểm M, K, N: theo bất đẳng thức tam giác ta có MN <= MK + KN = CD/2 + AB/2 = (AB + CD)/2. Dấu '=' xảy ra khi M, K, N thẳng hàng <=> MK // KN <=> AB // CD, tức tứ giác ABCD là hình thang có 2 đáy là AB và CD (0.25đ)."
      }
    ]
  },
  "c4_8_bai2_test2": {
    "title": "Toán 8 (KNTT) - Bài 16: Đường trung bình của tam giác - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$. Gọi $M, N$ lần lượt là trung điểm của $AB, AC$. Nếu $MN = 5\text{ cm}$ thì độ dài cạnh $BC$ là:",
        "options": [
          "$10\text{ cm}$",
          "$2.5\text{ cm}$",
          "$5\text{ cm}$",
          "$15\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tứ giác có các đỉnh là trung điểm bốn cạnh của một hình thoi là hình gì?",
        "options": [
          "Hình chữ nhật",
          "Hình thoi",
          "Hình vuông",
          "Hình bình hành không có góc vuông"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có chu vi $30\text{ cm}$. Gọi $M, N, P$ lần lượt là trung điểm $AB, BC, CA$. Chu vi tam giác $MNP$ bằng:",
        "options": [
          "$15\text{ cm}$",
          "$10\text{ cm}$",
          "$7.5\text{ cm}$",
          "$20\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $E, F$ lần lượt là trung điểm của $AD, BC$. Biết $AB = 6\text{ cm}$ và $EF = 9\text{ cm}$. Độ dài đáy $CD$ là:",
        "options": [
          "$12\text{ cm}$",
          "$15\text{ cm}$",
          "$10\text{ cm}$",
          "$8\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông tại $A$, có $BC = 10\text{ cm}$. Gọi $D, E, F$ lần lượt là trung điểm của $AB, BC, CA$. Độ dài đoạn thẳng $DF$ bằng:",
        "options": [
          "$5\text{ cm}$",
          "$2.5\text{ cm}$",
          "$10\text{ cm}$",
          "$6\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Gọi $M$ là trung điểm $BC$. Từ $M$ kẻ $MD \\parallel AC$ ($D \\in AB$) và $ME \\parallel AB$ ($E \\in AC$). Tứ giác $ADME$ là hình gì?",
        "options": [
          "Hình bình hành",
          "Hình chữ nhật",
          "Hình thoi",
          "Hình vuông"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $AB = 6\text{ cm}, AC = 8\text{ cm}, BC = 10\text{ cm}$. Gọi $M, N$ là trung điểm của $AB, BC$. Diện tích tam giác $BMN$ bằng:",
        "options": [
          "$6\text{ cm}^2$",
          "$12\text{ cm}^2$",
          "$24\text{ cm}^2$",
          "$3\text{ cm}^2$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $CD$. Đoạn thẳng $AN$ và $CM$ cắt đường chéo $BD$ lần lượt tại $E$ và $F$. Khẳng định nào sau đây là đúng?",
        "options": [
          "$BE = EF = FD$",
          "$BE = 2EF$",
          "$EF = 2FD$",
          "$BE + FD = EF$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Gọi $M, N$ là trung điểm của $AB, AC$. Trên tia đối của tia $NM$ lấy điểm $P$ sao cho $NP = NM$. Tứ giác $AMCP$ là hình gì?",
        "options": [
          "Hình bình hành",
          "Hình thoi",
          "Hình chữ nhật",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$. Gọi $M, N, P, Q$ lần lượt là trung điểm của $AB, BC, CD, DA$. Để $MNPQ$ là hình chữ nhật thì tứ giác $ABCD$ cần có:",
        "options": [
          "Hai đường chéo vuông góc với nhau",
          "Hai đường chéo bằng nhau",
          "Các cạnh đối bằng nhau",
          "Các góc vuông"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có đường trung tuyến $AM$. Gọi $I$ là trung điểm $AM$. Tia $BI$ cắt $AC$ tại $E$. Tỉ số $\frac{AE}{EC}$ bằng:",
        "options": [
          "$\frac{1}{2}$",
          "$\frac{1}{3}$",
          "$\frac{2}{3}$",
          "$1$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho tam giác đều $ABC$ có cạnh bằng $8\text{ cm}$. Nối trung điểm các cạnh tạo thành tam giác thứ hai, nối trung điểm các cạnh tam giác thứ hai tạo thành tam giác thứ ba. Chu vi tam giác thứ ba bằng:",
        "options": [
          "$6\text{ cm}$",
          "$12\text{ cm}$",
          "$3\text{ cm}$",
          "$8\text{ cm}$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ cân tại $A$. Gọi $D, E$ lần lượt là trung điểm của $AB$ và $AC$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $BDEC$ là hình thang có đáy $DE = \frac{1}{2}BC$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Góc $\\widehat{B}$ bằng góc $\\widehat{C}$ nên $BDEC$ là hình thang cân.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Hai đoạn thẳng $BE$ và $CD$ bằng nhau.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Nếu tam giác $ABC$ đều thì tứ giác $BDEC$ có hai đường chéo vuông góc.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tứ giác $ABCD$. Gọi $M, N, P, Q$ lần lượt là trung điểm của $AB, BC, CD, DA$. Gọi $I, K$ lần lượt là trung điểm của hai đường chéo $AC$ và $BD$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $MNPQ$ luôn là hình bình hành (định lí Varignon).",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $MP$ và $NQ$ cắt nhau tại trung điểm của mỗi đoạn.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Ba đoạn thẳng $MP, NQ, IK$ đồng quy tại một điểm.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Chu vi hình bình hành $MNPQ$ bằng tổng độ dài bốn cạnh của tứ giác $ABCD$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có cạnh $BC = 18\text{ cm}$. Gọi $M, N$ lần lượt là trung điểm của $AB, AC$. Lấy $I$ là trung điểm của $MN$. Đoạn thẳng $MI$ có độ dài bằng bao nhiêu cm?",
        "answer": "4.5"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ có trung tuyến $AM = 9\text{ cm}$. Gọi $G$ là trọng tâm của tam giác $ABC$. Gọi $D$ là trung điểm của $BG$. Tính độ dài đoạn thẳng $DG$ theo cm.",
        "answer": "3"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Đoạn thẳng nối trung điểm hai cạnh bên $AD$ và $BC$ dài $14\text{ cm}$, hiệu độ dài hai đáy là $6\text{ cm}$. Tính độ dài đáy lớn $CD$ theo cm.",
        "answer": "17"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$ có diện tích bằng $48\text{ cm}^2$. Gọi $M, N, P$ lần lượt là trung điểm của $BC, CA, AB$. Gọi $G$ là trọng tâm của tam giác $ABC$. Tính diện tích tam giác $GMN$ theo đơn vị $\text{cm}^2$.",
        "answer": "4"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Các đường trung tuyến $BD$ và $CE$ cắt nhau tại $G$. Gọi $M, N$ lần lượt là trung điểm của $BG$ và $CG$.\na) Chứng minh tứ giác $MNDE$ là hình bình hành.\nb) Tìm điều kiện của tam giác $ABC$ để tứ giác $MNDE$ là hình chữ nhật.",
        "rubric": "a) DE là đường trung bình tam giác ABC => DE // BC và DE = 1/2 BC (0.25đ). MN là đường trung bình tam giác GBC => MN // BC và MN = 1/2 BC (0.25đ). Suy ra DE // MN và DE = MN => MNDE là hình bình hành (0.25đ).\nb) MNDE là hình chữ nhật <=> hai đường chéo vuông góc hoặc có 1 góc vuông <=> ME vuông góc MN <=> BD vuông góc CE (hai đường trung tuyến vuông góc) (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình bình hành $ABCD$. Gọi $M, N$ lần lượt là trung điểm của các cạnh $BC, AD$. Gọi $I$ là giao điểm của $AM$ và $BD$, gọi $K$ là giao điểm của $CN$ và $BD$.\na) Chứng minh tứ giác $AMCN$ là hình bình hành.\nb) Chứng minh rằng $DI = IK = KB$.",
        "rubric": "a) Vì ABCD là hình bình hành nên AD // BC và AD = BC. Do N, M là trung điểm nên AN // MC và AN = MC => AMCN là hình bình hành (0.5đ).\nb) Xét tam giác ABD có I là trọng tâm do là giao điểm của trung tuyến BD/2 và AM => DI = 2/3 đường trung tuyến = 1/3 BD. Tương tự trong tam giác BCD có BK = 1/3 BD. Suy ra DI = IK = KB = 1/3 BD (0.5đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tam giác $ABC$ có đường cao $AH$. Gọi $D, E, F$ lần lượt là trung điểm của $AB, BC, CA$.\nChứng minh rằng tứ giác $DFEH$ là hình thang cân.",
        "rubric": "Vì D, F là trung điểm AB, AC nên DF là đường trung bình tam giác ABC => DF // BC => DFEH là hình thang (0.25đ). Ta cần chứng minh DE = HF. DE là đường trung bình tam giác ABC nên DE = 1/2 AC (0.25đ). Trong tam giác vuông AHC vuông tại H có HF là đường trung tuyến ứng với cạnh huyền AC nên HF = 1/2 AC (0.25đ). Do đó DE = HF. Hình thang DFEH có hai cạnh bên bằng nhau và không song song (hoặc hai đường chéo bằng nhau) => DFEH là hình thang cân (0.25đ)."
      }
    ]
  },
  "c4_8_bai2_test3": {
    "title": "Toán 8 (KNTT) - Bài 16: Đường trung bình của tam giác - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $AB \\perp CD$. Gọi $E, F, G, H$ lần lượt là trung điểm của $BC, BD, AD, AC$. Tứ giác $EFGH$ là hình gì?",
        "options": [
          "Hình chữ nhật",
          "Hình thoi",
          "Hình vuông",
          "Hình bình hành không có góc vuông"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $AC = BD$. Gọi $M, N, P, Q$ lần lượt là trung điểm của $AB, BC, CD, DA$. Tứ giác $MNPQ$ là hình gì?",
        "options": [
          "Hình thoi",
          "Hình chữ nhật",
          "Hình vuông",
          "Hình thang cân"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho tứ giác $ABCD$ có $AC \\perp BD$ và $AC = BD$. Nối trung điểm 4 cạnh của tứ giác được hình gì?",
        "options": [
          "Hình vuông",
          "Hình chữ nhật",
          "Hình thoi",
          "Hình bình hành"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Trên cạnh $AB$ lấy điểm $D$ sao cho $AD = 2DB$. Gọi $M$ là trung điểm của $BC$. Đường thẳng qua $D$ song song với $BC$ cắt $AM$ tại $I$. Tỉ số $\frac{DI}{BC}$ bằng:",
        "options": [
          "$\frac{1}{3}$",
          "$\frac{2}{3}$",
          "$\frac{1}{2}$",
          "$\frac{1}{6}$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $E, F$ lần lượt là trung điểm của $AD, BC$. Đoạn thẳng $EF$ cắt hai đường chéo $BD$ và $AC$ lần lượt tại $M$ và $N$. Độ dài đoạn thẳng $MN$ bằng:",
        "options": [
          "$\frac{|CD - AB|}{2}$",
          "$\frac{CD + AB}{2}$",
          "$\frac{CD - AB}{4}$",
          "$\frac{CD + AB}{4}$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Gọi $H$ là trực tâm của tam giác, $O$ là tâm đường tròn ngoại tiếp, $M$ là trung điểm của $BC$. Mối quan hệ giữa đoạn thẳng $AH$ và $OM$ là:",
        "options": [
          "$AH = 2OM$ và $AH \\parallel OM$",
          "$AH = OM$",
          "$AH = 3OM$",
          "$AH \\perp OM$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ có trung tuyến $AM$. Lấy điểm $D$ trên $AM$ sao cho $AD = 2DM$. Gọi $E$ là giao điểm của $BD$ và $AC$. Tỉ số $\frac{AE}{EC}$ bằng:",
        "options": [
          "$1$",
          "$\frac{1}{2}$",
          "$2$",
          "$\frac{2}{3}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Vận dụng thấp",
        "question": "Cho tứ giác $ABCD$ có $AD = BC$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $CD$. Đường thẳng $MN$ cắt các đường thẳng $AD$ và $BC$ lần lượt tại $P$ và $Q$. Khi đó góc $\\widehat{APD}$ và $\\widehat{BQM}$:",
        "options": [
          "Bằng nhau",
          "Bù nhau",
          "Phụ nhau",
          "Không có mối quan hệ cố định"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$. Gọi $M$ là trung điểm $BC$. Từ $A$ kẻ đường thẳng $d$ vuông góc với $AM$. Các đường phân giác của góc $B$ và góc $C$ cắt $d$ lần lượt tại $E$ và $F$. Kết luận nào sau đây đúng?",
        "options": [
          "$AE = AF$",
          "$AE = 2AF$",
          "$AF = 2AE$",
          "$BE \\parallel CF$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$. Gọi $G$ là trọng tâm, $M, N, P$ lần lượt là trung điểm của $BC, CA, AB$. Gọi $A', B', C'$ lần lượt là điểm đối xứng của $A, B, C$ qua $G$. Khi đó sáu điểm $M, N, P, A', B', C'$:",
        "options": [
          "Cùng nằm trên một đường tròn nếu $\triangle ABC$ đều",
          "Luôn thẳng hàng",
          "Tạo thành một tam giác",
          "Tạo thành hai đường thẳng song song"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Đường trung bình thứ $n$ nối trung điểm của tam giác thứ $n-1$. Biết diện tích tam giác ban đầu là $S_0$. Diện tích của tam giác thứ $n$ là:",
        "options": [
          "$\frac{S_0}{4^n}$",
          "$\frac{S_0}{2^n}$",
          "$\frac{S_0}{3^n}$",
          "$\frac{S_0}{4n}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho tứ giác $ABCD$. Gọi $G$ là trọng tâm tứ giác (giao điểm của hai đoạn thẳng nối trung điểm các cạnh đối). Với mọi điểm $M$ bất kì trong không gian, ta luôn có:",
        "options": [
          "$\u000bec{MA} + \u000bec{MB} + \u000bec{MC} + \u000bec{MD} = 4\u000bec{MG}$",
          "$\u000bec{MA} + \u000bec{MC} = \u000bec{MB} + \u000bec{MD}$",
          "$\u000bec{GA} + \u000bec{GB} + \u000bec{GC} + \u000bec{GD} = \u000bec{AB}$",
          "$MA + MB + MC + MD = 4MG$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ có trực tâm $H$ và tâm đường tròn ngoại tiếp $O$. Gọi $M$ là trung điểm của $BC$, $K$ là điểm đối xứng của $H$ qua $M$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $BHCK$ là hình bình hành do có hai đường chéo cắt nhau tại trung điểm $M$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng $AK$ là đường kính của đường tròn ngoại tiếp tam giác $ABC$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng cao",
            "text": "Đoạn thẳng $OM$ là đường trung bình của tam giác $AHK$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Trọng tâm $G$ của tam giác $ABC$ chia đoạn thẳng $OH$ theo tỉ số $OG = 2GH$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$), đường cao $AH$. Gọi $D, E$ lần lượt là hình chiếu của $H$ trên $AB$ và $AC$. Gọi $I$ là trung điểm của $BC$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $ADHE$ có ba góc vuông nên là hình chữ nhật.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng $DE$ bằng đoạn thẳng $AH$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng cao",
            "text": "Đoạn thẳng $AI$ vuông góc với đoạn thẳng $DE$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Diện tích tứ giác $ADHE$ lớn hơn một nửa diện tích tam giác $ABC$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông tại $A$. Gọi $M, N$ lần lượt là trung điểm của $AB, BC$. Biết $AC = 16\text{ cm}$. Tính độ dài $MN$ theo cm.",
        "answer": "8"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tứ giác $ABCD$ có $AC = 14\text{ cm}, BD = 18\text{ cm}$. Gọi $M, N, P, Q$ lần lượt là trung điểm của $AB, BC, CD, DA$. Chu vi của hình bình hành $MNPQ$ bằng bao nhiêu cm?",
        "answer": "32"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Hai đáy $AB = 6\text{ cm}, CD = 16\text{ cm}$. Đoạn thẳng nối trung điểm hai đường chéo $AC$ và $BD$ có độ dài bằng bao nhiêu cm?",
        "answer": "5"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$ có diện tích bằng $96\text{ cm}^2$. Gọi $D$ là trung điểm của $AB$, $E$ là trung điểm của $CD$. Đường thẳng $AE$ cắt $BC$ tại $F$. Tính diện tích tam giác $ABF$ theo đơn vị $\text{cm}^2$.",
        "answer": "32"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $E$ là trung điểm của $AD$, $F$ là trung điểm của $BC$. Đường thẳng $EF$ cắt $BD$ tại $I$ và cắt $AC$ tại $K$.\na) Chứng minh rằng $I$ là trung điểm của $BD$ và $K$ là trung điểm của $AC$.\nb) Chứng minh rằng $IK = \frac{CD - AB}{2}$.",
        "rubric": "a) Trong tam giác ABD có E là trung điểm AD, EI // AB => I là trung điểm BD (0.25đ). Trong tam giác ADC có E là trung điểm AD, EK // CD => K là trung điểm AC (0.25đ).\nb) Ta có EK = 1/2 CD (đường trung bình tam giác ADC) và EI = 1/2 AB (đường trung bình tam giác ABD) (0.25đ). Suy ra IK = EK - EI = 1/2 CD - 1/2 AB = (CD - AB)/2 (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ nhọn. Vẽ ra phía ngoài tam giác các tam giác vuông cân tại $A$ là $\triangle ABD$ và $\triangle ACE$ (với $\\widehat{ABD} = \\widehat{ACE} = 90^\\circ$ hoặc góc vuông tại $A$). Gọi $M$ là trung điểm của $BC$.\na) Chứng minh rằng $DE = 2AM$.\nb) Chứng minh rằng $AM \\perp DE$.",
        "rubric": "Trên tia đối của tia MA lấy điểm K sao cho MK = MA => ABKC là hình bình hành => CK = AB = AD và góc ACK bù góc BAC (0.25đ). Ta có góc DAE + góc BAC = 180 độ => góc DAE = góc ACK (0.25đ). Xét tam giác ADE và tam giác CKA có: AD = CK, AE = CA, góc DAE = góc ACK => tam giác ADE = tam giác CKA (c-g-c) (0.25đ) => DE = AK = 2AM và góc ADE = góc CKA => AM vuông góc DE (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tam giác $ABC$ có trọng tâm $G$. Lấy điểm $M$ tùy ý trong tam giác. Gọi $A', B', C'$ lần lượt là trọng tâm của các tam giác $MBC, MCA, MAB$.\nChứng minh rằng ba đường thẳng $AA', BB', CC'$ đồng quy tại một điểm và điểm đó là trung điểm của đoạn thẳng $MG$.",
        "rubric": "Gọi P là trung điểm BC. Vì G là trọng tâm tam giác ABC nên G thuộc AP và PG/PA = 1/3 (0.25đ). Vì A' là trọng tâm tam giác MBC nên A' thuộc MP và PA'/PM = 1/3 (0.25đ). Trong tam giác PAM có PG/PA = PA'/PM = 1/3 nên theo định lí Thalès đảo ta có GA' // AM và GA'/AM = 1/3 (0.25đ). Gọi O là giao điểm của AA' và MG. Áp dụng hệ quả Thalès cho tam giác OAM có GA' // AM => OG/OM = GA'/AM = ... biến đổi suy ra O là trung điểm MG. Tương tự BB' và CC' cũng cắt MG tại trung điểm O. Vậy ba đường thẳng đồng quy tại trung điểm của MG (0.25đ)."
      }
    ]
  },
  "c4_8_bai3_test1": {
    "title": "Toán 8 (KNTT) - Bài 17: Tính chất đường phân giác của tam giác - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong một tam giác, đường phân giác của một góc chia cạnh đối diện thành hai đoạn thẳng:",
        "options": [
          "Tỉ lệ với hai cạnh kề hai đoạn ấy",
          "Bằng nhau",
          "Tỉ lệ nghịch với hai cạnh kề",
          "Bằng nửa cạnh đối diện"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$ có tia phân giác của góc $A$ cắt cạnh $BC$ tại $D$. Tỉ số nào sau đây là ĐÚNG?",
        "options": [
          "$\frac{DB}{DC} = \frac{AB}{AC}$",
          "$\frac{DB}{DC} = \frac{AC}{AB}$",
          "$\frac{DB}{AB} = \frac{DC}{BC}$",
          "$\frac{DB}{DC} = \frac{BC}{AC}$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$ có $AD$ là tia phân giác góc $A$ ($D \\in BC$). Biết $AB = 4\text{ cm}, AC = 6\text{ cm}, DB = 2\text{ cm}$. Độ dài đoạn thẳng $DC$ bằng:",
        "options": [
          "$3\text{ cm}$",
          "$4\text{ cm}$",
          "$2\text{ cm}$",
          "$5\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Cho $\triangle MNP$ có $MI$ là phân giác của góc $M$ ($I \\in NP$). Đẳng thức nào sau đây đúng?",
        "options": [
          "$\frac{IN}{IP} = \frac{MN}{MP}$",
          "$\frac{IN}{IP} = \frac{MP}{MN}$",
          "$\frac{IN}{MN} = \frac{IP}{NP}$",
          "$IN \\cdot MP = IP \\cdot NP$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$ có $AB = 6\text{ cm}, AC = 9\text{ cm}$. $AD$ là phân giác góc $A$ ($D \\in BC$). Tỉ số $\frac{DB}{DC}$ bằng:",
        "options": [
          "$\frac{2}{3}$",
          "$\frac{3}{2}$",
          "$\frac{2}{5}$",
          "$\frac{3}{5}$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Định lí về tính chất đường phân giác trong tam giác vẫn đúng đối với:",
        "options": [
          "Tia phân giác của góc ngoài tam giác",
          "Đường trung tuyến của tam giác",
          "Đường cao của tam giác",
          "Đường trung trực của tam giác"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $AD$ là phân giác góc $A$ ($D \\in BC$). Biết $AB = 5\text{ cm}, AC = 8\text{ cm}$ và $BC = 13\text{ cm}$. Độ dài đoạn thẳng $BD$ là:",
        "options": [
          "$5\text{ cm}$",
          "$8\text{ cm}$",
          "$6.5\text{ cm}$",
          "$4\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có phân giác $AD$. Biết $AB = 6, AC = 10$ và $BC = 12$. Độ dài đoạn thẳng $DC$ bằng:",
        "options": [
          "$7.5$",
          "$4.5$",
          "$8$",
          "$6$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $AD$ là phân giác góc $A$ ($D \\in BC$). Tỉ số diện tích $\frac{S_{\triangle ABD}}{S_{\triangle ACD}}$ bằng tỉ số nào dưới đây?",
        "options": [
          "$\frac{AB}{AC}$",
          "$\\left(\frac{AB}{AC}\right)^2$",
          "$\frac{AD}{BC}$",
          "$1$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ cân tại $A$. Đường phân giác của góc $A$ cắt $BC$ tại $D$. Khẳng định nào sau đây là SAI?",
        "options": [
          "$DB = 2DC$",
          "$D$ là trung điểm của $BC$",
          "$AD \\perp BC$",
          "$AD$ là đường trung tuyến của tam giác"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ vuông tại $A$ có $AB = 3\text{ cm}, AC = 4\text{ cm}$. Phân giác góc $A$ cắt $BC$ tại $D$. Độ dài đoạn thẳng $BD$ là:",
        "options": [
          "$\frac{15}{7}\text{ cm}$",
          "$\frac{20}{7}\text{ cm}$",
          "$2\text{ cm}$",
          "$2.5\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$, $AD$ là phân giác góc trong, $AE$ là phân giác góc ngoài tại đỉnh $A$ ($D, E \\in BC$). Góc $\\widehat{DAE}$ bằng:",
        "options": [
          "$90^\\circ$",
          "$60^\\circ$",
          "$45^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ có $AB = 6\text{ cm}, AC = 9\text{ cm}, BC = 10\text{ cm}$. Kẻ đường phân giác $AD$ của góc $A$ ($D \\in BC$).",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tỉ số $\frac{DB}{DC} = \frac{2}{3}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $BD = 4\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $DC = 6\text{ cm}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Tỉ số diện tích giữa $\triangle ABD$ và $\triangle ACD$ bằng $\frac{4}{9}$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\text{ cm}, AC = 8\text{ cm}$. Kẻ phân giác $BD$ của góc $B$ ($D \\in AC$).",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Độ dài cạnh huyền $BC = 10\text{ cm}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Theo tính chất phân giác, $\frac{DA}{DC} = \frac{BA}{BC} = \frac{3}{5}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Độ dài đoạn thẳng $DA = 3\text{ cm}$ và $DC = 5\text{ cm}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Độ dài đường phân giác $BD = \\sqrt{6^2 + 3^2} = 3\\sqrt{5}\text{ cm}$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $AB = 8\text{ cm}, AC = 12\text{ cm}$. Phân giác trong của góc $A$ cắt $BC$ tại $D$. Biết $BD = 6\text{ cm}$. Tính độ dài đoạn thẳng $DC$ theo cm.",
        "answer": "9"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $AB = 10\text{ cm}, AC = 15\text{ cm}, BC = 20\text{ cm}$. Phân giác $AD$ cắt $BC$ tại $D$. Tính độ dài $BD$ theo cm.",
        "answer": "8"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho $\triangle ABC$ vuông tại $A$ có $AB = 9, AC = 12$. Kẻ phân giác $AD$ của góc $A$ ($D \\in BC$). Tính độ dài đoạn thẳng $CD$ (kết quả dạng số thập phân, ví dụ 8.57).",
        "answer": "8.57"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$ có $AB = 4, AC = 6, BC = 5$. Kẻ phân giác trong $AD$ và phân giác ngoài $AE$ ($D, E \\in BC$). Tính độ dài đoạn thẳng $DE$.",
        "answer": "12"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $AB = 12\text{ cm}, AC = 18\text{ cm}, BC = 20\text{ cm}$. Tia phân giác của góc $A$ cắt cạnh $BC$ tại $D$.\na) Tính độ dài các đoạn thẳng $BD$ và $CD$.\nb) Kẻ $DE \\parallel AB$ ($E \\in AC$). Tính độ dài đoạn thẳng $DE$.",
        "rubric": "a) Áp dụng tính chất phân giác: BD/CD = AB/AC = 12/18 = 2/3. Suy ra BD/2 = CD/3 = (BD + CD)/(2 + 3) = 20/5 = 4 (0.25đ). Tính được BD = 8 cm, CD = 12 cm (0.25đ).\nb) Xét tam giác ABC có DE // AB => DE/AB = CD/BC <=> DE/12 = 12/20 => DE = (12*12)/20 = 7.2 cm (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ cân tại $A$. Các đường phân giác $BD$ và $CE$ cắt nhau tại $I$.\na) Chứng minh rằng $AD = AE$.\nb) Chứng minh rằng $ED \\parallel BC$.\nc) Biết $AB = AC = 15\text{ cm}, BC = 10\text{ cm}$. Tính độ dài đoạn thẳng $ED$.",
        "rubric": "a) Vì tam giác ABC cân tại A nên góc B = góc C => phân giác BD và CE bằng nhau và chia các góc bằng nhau. Tam giác ABD = tam giác ACE (g-c-g) => AD = AE (0.25đ).\nb) Vì AD = AE và AB = AC => AD/AB = AE/AC => ED // BC theo định lí Thalès đảo (0.25đ).\nc) Áp dụng tính chất phân giác cho tam giác ABD: DA/DC = BA/BC = 15/10 = 3/2 => DA/3 = DC/2 = AC/5 = 15/5 = 3 => DA = 9 cm (0.25đ). Áp dụng hệ quả Thalès: ED/BC = AD/AC => ED/10 = 9/15 => ED = 6 cm (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tam giác $ABC$ có $AD$ là phân giác của góc $A$ ($D \\in BC$).\nChứng minh công thức tính độ dài đường phân giác: $AD^2 = AB \\cdot AC - DB \\cdot DC$.",
        "rubric": "Vẽ đường tròn ngoại tiếp tam giác ABC. Tia AD cắt đường tròn tại điểm thứ hai E (0.25đ). Chứng minh tam giác ABD đồng dạng tam giác AEC (g-g) vì góc BAD = góc EAC và góc ABD = góc AEC (cùng chắn cung AC) (0.25đ). Suy ra AB/AE = AD/AC => AB * AC = AD * AE = AD * (AD + DE) = AD^2 + AD * DE (0.25đ). Lại có tam giác BDE đồng dạng tam giác ADC (hoặc phương tích điểm D) => AD * DE = DB * DC. Thay vào được: AB * AC = AD^2 + DB * DC => AD^2 = AB * AC - DB * DC (0.25đ)."
      }
    ]
  },
  "c4_8_bai3_test2": {
    "title": "Toán 8 (KNTT) - Bài 17: Tính chất đường phân giác của tam giác - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$ có phân giác trong $AD$ và phân giác ngoài $AK$ tại đỉnh $A$ ($D, K \\in BC$). Hệ thức nào sau đây đúng?",
        "options": [
          "$\frac{KB}{KC} = \frac{DB}{DC} = \frac{AB}{AC}$",
          "$\frac{KB}{KC} = -\frac{DB}{DC}$",
          "$KB \\cdot DB = KC \\cdot DC$",
          "$KD = BC$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $AB = 12\text{ cm}, AC = 16\text{ cm}, BC = 21\text{ cm}$. Phân giác của góc $A$ cắt $BC$ tại $D$. Độ dài đoạn thẳng $BD$ là:",
        "options": [
          "$9\text{ cm}$",
          "$12\text{ cm}$",
          "$10.5\text{ cm}$",
          "$8\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\text{ cm}, AC = 8\text{ cm}$. Phân giác của góc $C$ cắt $AB$ tại $M$. Độ dài đoạn thẳng $AM$ là:",
        "options": [
          "$\frac{8}{3}\text{ cm}$",
          "$3\text{ cm}$",
          "$\frac{10}{3}\text{ cm}$",
          "$2\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có phân giác $AD$. Kẻ $DH \\parallel AB$ ($H \\in AC$). Biết $AB = 6\text{ cm}, AC = 12\text{ cm}$. Độ dài đoạn thẳng $DH$ là:",
        "options": [
          "$4\text{ cm}$",
          "$3\text{ cm}$",
          "$5\text{ cm}$",
          "$4.5\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có phân giác $AD$. Biết diện tích tam giác $ABD$ bằng $18\text{ cm}^2$ và diện tích tam giác $ACD$ bằng $27\text{ cm}^2$. Tỉ số $\frac{AB}{AC}$ bằng:",
        "options": [
          "$\frac{2}{3}$",
          "$\frac{3}{2}$",
          "$\frac{4}{9}$",
          "$\frac{9}{4}$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có ba phân giác $AD, BE, CF$ cắt nhau tại $I$. Tỉ số $\frac{ID}{IA}$ bằng:",
        "options": [
          "$\frac{a}{b + c}$",
          "$\frac{b + c}{a}$",
          "$\frac{b}{a + c}$",
          "$\frac{c}{a + b}$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có phân giác $AD$. Trên cạnh $AB$ lấy điểm $E$ sao cho $AE = AC$. Khẳng định nào sau đây là đúng?",
        "options": [
          "$\triangle ADE = \triangle ADC$",
          "$DE \\parallel BC$",
          "$DE = BC$",
          "$\triangle BDE$ cân tại $D$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho hình thoi $ABCD$. Điểm $M$ thuộc cạnh $BC$. Tia phân giác của góc $\\widehat{BAM}$ cắt $BC$ tại $E$. Tỉ số $\frac{EB}{EM}$ bằng tỉ số nào dưới đây?",
        "options": [
          "$\frac{AB}{AM}$",
          "$\frac{AM}{AB}$",
          "$\frac{BM}{AB}$",
          "$\frac{BC}{AM}$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có phân giác $AD$. Biết $AB = c, AC = b, BC = a$. Công thức tính độ dài đoạn $BD$ theo $a, b, c$ là:",
        "options": [
          "$BD = \frac{ac}{b + c}$",
          "$BD = \frac{ab}{b + c}$",
          "$BD = \frac{bc}{a + b}$",
          "$BD = \frac{a(b+c)}{c}$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có chu vi bằng $36\text{ cm}$. Phân giác $AD$ chia cạnh $BC$ thành hai đoạn $BD = 6\text{ cm}$ và $DC = 9\text{ cm}$. Độ dài cạnh $AB$ bằng:",
        "options": [
          "$\frac{42}{5}\text{ cm}$",
          "$8.4\text{ cm}$",
          "$9\text{ cm}$",
          "$10\text{ cm}$"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$. Đường phân giác của góc $B$ cắt $AC$ tại $E$. Từ $E$ kẻ đường thẳng song song với $AB$ cắt $BC$ tại $F$. Tam giác $BEF$ là tam giác gì?",
        "options": [
          "Tam giác cân tại $F$",
          "Tam giác vuông tại $F$",
          "Tam giác đều",
          "Tam giác vuông cân"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $AB = 8, AC = 12$. Phân giác ngoài tại đỉnh $A$ cắt đường thẳng $BC$ tại $E$. Biết $BC = 5$. Độ dài đoạn thẳng $BE$ là:",
        "options": [
          "$10$",
          "$8$",
          "$12$",
          "$15$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ vuông tại $A$ ($AB = 9\text{ cm}, AC = 12\text{ cm}$). Phân giác của góc $A$ cắt $BC$ tại $D$. Từ $D$ kẻ $DH \\perp AB$ ($H \\in AB$) và $DK \\perp AC$ ($K \\in AC$).",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tứ giác $AHDK$ có 3 góc vuông và $AD$ là phân giác nên là hình vuông.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài cạnh huyền $BC = 15\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tỉ số $\frac{DB}{DC} = \frac{3}{4}$ nên $DB = \frac{45}{7}\text{ cm}$ và $DC = \frac{60}{7}\text{ cm}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Cạnh của hình vuông $AHDK$ có độ dài bằng $5.5\text{ cm}$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ có $AB = c, AC = b, BC = a$. Các đường phân giác $AD, BE, CF$ đồng quy tại điểm $I$ (tâm đường tròn nội tiếp).",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tỉ số $\frac{DB}{DC} = \frac{c}{b}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Vận dụng thấp",
            "text": "Tỉ số $\frac{AI}{ID} = \frac{b + c}{a}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tỉ số $\frac{AF}{FB} \\cdot \frac{BD}{DC} \\cdot \frac{CE}{EA} = 1$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Tổng $\frac{AI}{AD} + \frac{BI}{BE} + \frac{CI}{CF} = 1$.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $AB = 6, AC = 9, BC = 10$. Đường phân giác góc $A$ cắt $BC$ tại $D$. Tính độ dài $BD$.",
        "answer": "4"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho $\triangle ABC$ vuông tại $A$ có $AB = 15\text{ cm}, AC = 20\text{ cm}$. Đường phân giác của góc $A$ cắt $BC$ tại $D$. Từ $D$ kẻ $DH \\perp AB$ ($H \\in AB$). Tính độ dài đoạn thẳng $DH$ (kết quả dạng số thập phân, ví dụ 8.57).",
        "answer": "8.57"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho $\triangle ABC$ có $AB = 12\text{ cm}, AC = 18\text{ cm}$. Phân giác trong $AD$ và phân giác ngoài $AE$ ($D, E \\in BC$). Biết $BC = 15\text{ cm}$. Tính độ dài đoạn thẳng $BE$ theo cm.",
        "answer": "30"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$ có $AB = 6, AC = 8, BC = 7$. Gọi $I$ là giao điểm các đường phân giác của $\triangle ABC$. Kẻ $AD$ là phân giác góc $A$. Tính tỉ số $\frac{AI}{ID}$ (kết quả viết dạng số thập phân làm tròn 1 chữ số sau dấu phẩy).",
        "answer": "2"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $AB = 10\text{ cm}, AC = 15\text{ cm}, BC = 20\text{ cm}$. Đường phân giác góc $A$ cắt $BC$ tại $D$.\na) Tính độ dài các đoạn thẳng $BD$ và $CD$.\nb) Đường thẳng qua $D$ song song với $AB$ cắt $AC$ tại $E$. Chứng minh $\triangle CDE$ đồng dạng $\triangle CBA$ và tính độ dài $DE$.",
        "rubric": "a) Theo tính chất phân giác: BD/CD = AB/AC = 10/15 = 2/3. Suy ra BD = (20*2)/5 = 8 cm, CD = 12 cm (0.5đ).\nb) DE // AB => tam giác CDE đồng dạng tam giác CBA (g-g) (0.25đ). Áp dụng hệ quả Thalès: DE/AB = CD/CB = 12/20 = 3/5 => DE = (10*3)/5 = 6 cm (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ vuông tại $A$. Đường phân giác của góc $B$ cắt $AC$ tại $D$. Kẻ $DH \\perp BC$ ($H \\in BC$).\na) Chứng minh rằng $BA = BH$ và $DA = DH$.\nb) Biết $AB = 6\text{ cm}, BC = 10\text{ cm}$. Tính độ dài các đoạn thẳng $AD$ và $DC$.",
        "rubric": "a) Xét hai tam giác vuông ABD và HBD có cạnh huyền BD chung, góc ABD = góc HBD (phân giác) => tam giác ABD = tam giác HBD (cạnh huyền - góc nhọn). Do đó BA = BH và DA = DH (0.5đ).\nb) Tam giác ABC vuông tại A có AC = sqrt(10^2 - 6^2) = 8 cm (0.25đ). Áp dụng tính chất phân giác: DA/DC = BA/BC = 6/10 = 3/5. Suy ra DA/3 = DC/5 = AC/8 = 8/8 = 1 => DA = 3 cm, DC = 5 cm (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tam giác $ABC$. Gọi $AD, BE, CF$ lần lượt là các đường phân giác trong của tam giác.\nChứng minh rằng: $\frac{S_{\triangle DEF}}{S_{\triangle ABC}} = \frac{2abc}{(a+b)(b+c)(c+a)}$ (với $a, b, c$ là độ dài ba cạnh của $\triangle ABC$).",
        "rubric": "Ta có S(AEF)/S(ABC) = (AE * AF)/(AB * AC) (0.25đ). Theo tính chất phân giác: AE = b*c/(a+c) và AF = b*c/(a+b) => S(AEF)/S = b*c / ((a+b)(a+c)) (0.25đ). Tương tự cho S(BDF)/S và S(CDE)/S (0.25đ). Lấy 1 trừ đi tổng 3 tỉ số diện tích các tam giác ở góc, sau khi quy đồng và rút gọn được S(DEF)/S = 2abc / ((a+b)(b+c)(c+a)) (0.25đ)."
      }
    ]
  },
  "c4_8_bai3_test3": {
    "title": "Toán 8 (KNTT) - Bài 17: Tính chất đường phân giác của tam giác - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có các cạnh thỏa mãn $a^2 = b^2 + bc$. Kẻ phân giác $AD$. Khi đó góc $\\widehat{BAC}$ bằng:",
        "options": [
          "$2\\widehat{B}$",
          "$2\\widehat{C}$",
          "$90^\\circ$",
          "$120^\\circ$"
        ],
        "correct": 1
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có phân giác $AD$. Biết $AB = 6, AC = 8, BC = 7$. Độ dài đoạn phân giác $AD$ bằng:",
        "options": [
          "$\\sqrt{36} = 6$",
          "$\\sqrt{38}$",
          "$5$",
          "$\\sqrt{42}$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có phân giác trong $AD$ và phân giác ngoài $AE$ ($D, E \\in BC$). Khi đó đường tròn đường kính $DE$ được gọi là:",
        "options": [
          "Đường tròn Apollonius",
          "Đường tròn Euler",
          "Đường tròn nội tiếp",
          "Đường tròn ngoại tiếp"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Gọi $I$ là giao điểm ba đường phân giác trong. Một đường thẳng qua $I$ song song với $BC$ cắt $AB, AC$ lần lượt tại $M, N$. Đẳng thức nào sau đây đúng?",
        "options": [
          "$MN = BM + CN$",
          "$MN = BM - CN$",
          "$MN = \frac{BM + CN}{2}$",
          "$MN^2 = BM \\cdot CN$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ vuông cân tại $A$. Đường phân giác của góc $B$ cắt $AC$ tại $D$. Tỉ số $\frac{AD}{DC}$ bằng:",
        "options": [
          "$\frac{\\sqrt{2}}{2}$",
          "$\\sqrt{2} - 1$",
          "$\frac{1}{2}$",
          "$\\sqrt{2}$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Vận dụng thấp",
        "question": "Cho hình bình hành $ABCD$. Tia phân giác của góc $A$ cắt $BC$ tại $E$, tia phân giác của góc $B$ cắt $AD$ tại $F$. Tứ giác $ABEF$ là hình gì?",
        "options": [
          "Hình thoi",
          "Hình chữ nhật",
          "Hình vuông",
          "Hình bình hành"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ có $AB < AC$. Kẻ đường phân giác $AD$ và trung tuyến $AM$. Kết luận nào sau đây đúng về vị trí tương đối của $D$ và $M$ trên cạnh $BC$?",
        "options": [
          "Điểm $D$ nằm giữa hai điểm $B$ và $M$",
          "Điểm $M$ nằm giữa hai điểm $B$ và $D$",
          "Điểm $D$ trùng điểm $M$",
          "Không thể xác định"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Vận dụng thấp",
        "question": "Cho $\triangle ABC$. Kẻ phân giác $AD$. Biết $\frac{AB}{AC} = \frac{2}{3}$. Qua $D$ kẻ $DE \\parallel AB$ ($E \\in AC$). Tỉ số $\frac{AE}{AC}$ bằng:",
        "options": [
          "$\frac{2}{5}$",
          "$\frac{3}{5}$",
          "$\frac{2}{3}$",
          "$\frac{1}{3}$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$ có hai đường phân giác $BD$ và $CE$ bằng nhau ($BD = CE$). Khi đó tam giác $ABC$ là tam giác gì? (Định lí Steiner - Lehmus)",
        "options": [
          "Tam giác cân tại $A$",
          "Tam giác đều",
          "Tam giác vuông tại $A$",
          "Tam giác vuông cân"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$ vuông tại $A$, phân giác $AD$. Kẻ đường cao $AH$. Khẳng định nào sau đây là đúng về tia phân giác của góc $\\widehat{HAC}$?",
        "options": [
          "Trùng với tia đối của tia phân giác góc HAB",
          "Tia phân giác góc BAH và tia phân giác góc HAC vuông góc với nhau",
          "Phân giác góc BAH trùng với phân giác AD",
          "Hai góc BAH và HAC bằng nhau"
        ],
        "correct": 1
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$ có $AB = c, AC = b, BC = a$. Độ dài đường phân giác trong $AD$ thỏa mãn bất đẳng thức nào sau đây?",
        "options": [
          "$AD < \frac{2bc}{b+c}$",
          "$AD > \frac{2bc}{b+c}$",
          "$AD = \frac{b+c}{2}$",
          "$AD = \\sqrt{bc}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$. Điểm $M$ thuộc cạnh $BC$. Gọi $D, E$ lần lượt là hình chiếu của $M$ trên $AB, AC$. Vị trí của điểm $M$ để $MD + ME$ không phụ thuộc vào $M$ khi $M$ di chuyển là khi:",
        "options": [
          "Tam giác $ABC$ cân tại $A$",
          "Tam giác $ABC$ vuông tại $A$",
          "Tam giác $ABC$ có góc $A = 120^\\circ$",
          "Mọi tam giác bất kì"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ có $AB = 4\text{ cm}, AC = 6\text{ cm}, \\widehat{A} = 120^\\circ$. Đường phân giác của góc $A$ cắt cạnh $BC$ tại $D$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tia $AD$ chia góc $A$ thành hai góc $\\widehat{BAD} = \\widehat{CAD} = 60^\\circ$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Vận dụng thấp",
            "text": "Diện tích tam giác $ABC$ bằng tổng diện tích hai tam giác $ABD$ và $ACD$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng cao",
            "text": "Áp dụng công thức diện tích tam giác theo góc: $\frac{1}{AD} = \frac{1}{AB} + \frac{1}{AC}$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Độ dài đoạn phân giác $AD = 2.4\text{ cm}$.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ có ba đường phân giác $AD, BE, CF$ cắt nhau tại $I$. Đặt $BC = a, AC = b, AB = c$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Điểm $I$ cách đều ba cạnh của tam giác $ABC$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Vận dụng thấp",
            "text": "Theo tính chất phân giác, $\frac{AI}{ID} = \frac{b+c}{a}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng cao",
            "text": "Tổng các tỉ số $\frac{AI}{AD} + \frac{BI}{BE} + \frac{CI}{CF} = 2$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Tích ba tỉ số $\frac{ID}{AD} \\cdot \frac{IE}{BE} \\cdot \frac{IF}{CF} \\le \frac{1}{27}$. Dấu bằng xảy ra khi tam giác $ABC$ đều.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $AB = 6\text{ cm}, AC = 12\text{ cm}, \\widehat{A} = 120^\\circ$. Tính độ dài đường phân giác trong $AD$ theo cm.",
        "answer": "4"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho $\triangle ABC$ có $AB = 5, AC = 7, BC = 6$. Kẻ phân giác $AD$. Tính độ dài đoạn thẳng $AD^2$.",
        "answer": "25"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$ có $AB = 12, AC = 16, BC = 14$. Gọi $I$ là tâm đường tròn nội tiếp. Tính tỉ số $\frac{AI}{ID}$ (kết quả là số nguyên).",
        "answer": "2"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$ vuông tại $A$ có $AB = 21, AC = 28$. Phân giác $AD$ cắt $BC$ tại $D$. Gọi $r$ là bán kính đường tròn nội tiếp tam giác $ABC$. Tính giá trị của $r$.",
        "answer": "7"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Đường phân giác của góc $A$ cắt $BC$ tại $D$. Chứng minh rằng nếu $\\widehat{A} = 120^\\circ$ thì $\frac{1}{AD} = \frac{1}{AB} + \frac{1}{AC}$.",
        "rubric": "Ta có S(ABC) = S(ABD) + S(ACD) (0.25đ). Áp dụng công thức tính diện tích qua sin của góc kẹp: 1/2 AB * AC * sin(120) = 1/2 AB * AD * sin(60) + 1/2 AC * AD * sin(60) (0.25đ). Vì sin(120) = sin(60) = sqrt(3)/2 khác 0 nên chia cả hai vế cho 1/2 sin(60): AB * AC = AD * (AB + AC) (0.25đ). Chia cả hai vế cho AB * AC * AD ta được: 1/AD = (AB + AC)/(AB * AC) = 1/AB + 1/AC (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Đường tròn nội tiếp $(I)$ tiếp xúc với các cạnh $BC, CA, AB$ lần lượt tại $D, E, F$. Đặt $BC = a, CA = b, AB = c$, nửa chu vi $p = \frac{a+b+c}{2}$.\na) Tính độ dài đoạn thẳng $AF, BD, CE$ theo $a, b, c, p$.\nb) Chứng minh rằng $AD, BE, CF$ đồng quy (điểm Gergonne).",
        "rubric": "a) Theo tính chất hai tiếp tuyến cắt nhau: AF = AE = x, BD = BF = y, CD = CE = z. Ta có x + y = c, y + z = a, z + x = b => x + y + z = p. Từ đó suy ra AF = AE = p - a; BD = BF = p - b; CD = CE = p - c (0.5đ).\nb) Xét tích: (AF/FB) * (BD/DC) * (CE/EA) = ((p-a)/(p-b)) * ((p-b)/(p-c)) * ((p-c)/(p-a)) = 1 (0.25đ). Theo định lí Ceva đảo, ba đoạn thẳng AD, BE, CF đồng quy tại một điểm (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tam giác $ABC$ có ba góc nhọn. Gọi $AD, BE, CF$ là các đường phân giác trong của tam giác.\nChứng minh rằng: $\frac{AD^2}{AB \\cdot AC} + \frac{BE^2}{BC \\cdot BA} + \frac{CF^2}{CA \\cdot CB} \\le \frac{9}{4}$. Dấu đẳng thức xảy ra khi nào?",
        "rubric": "Theo công thức tính độ dài đường phân giác: AD^2 = AB * AC - DB * DC = bc - (a^2 bc)/(b+c)^2 = bc [1 - a^2/(b+c)^2] = bc * ((b+c)^2 - a^2)/(b+c)^2 (0.25đ). Suy ra AD^2 / (bc) = 1 - a^2 / (b+c)^2. Áp dụng bất đẳng thức Cauchy-Schwarz: (b+c)^2 <= 2(b^2 + c^2) hoặc dùng bất đẳng thức 4bc <= (b+c)^2 => AD <= (b+c)/2 * cos(A/2) (0.25đ). Cộng ba biểu thức lại và áp dụng bất đẳng thức lượng giác: cos^2(A/2) + cos^2(B/2) + cos^2(C/2) <= 9/4 (0.25đ). Dấu đẳng thức xảy ra khi và chỉ khi a = b = c, tức tam giác ABC là tam giác đều (0.25đ)."
      }
    ]
  },
  "c4_8_bai4_test1": {
    "title": "Toán 8 (KNTT) - Bài kiểm tra cuối Chương IV: Định lí Thalès - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho đoạn thẳng $AB = 6\text{ cm}, CD = 9\text{ cm}$. Tỉ số của hai đoạn thẳng $AB$ và $CD$ là:",
        "options": [
          "$\frac{2}{3}$",
          "$\frac{3}{2}$",
          "$\frac{1}{3}$",
          "$\frac{2}{5}$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$, $MN \\parallel BC$ ($M \\in AB, N \\in AC$). Khẳng định nào sau đây là định lí Thalès thuận?",
        "options": [
          "$\frac{AM}{AB} = \frac{AN}{AC}$",
          "$\frac{AM}{MB} = \frac{NC}{AN}$",
          "$\frac{AM}{AN} = \frac{BC}{MN}$",
          "$\frac{MB}{AB} = \frac{AN}{AC}$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$ có $M, N$ lần lượt là trung điểm của $AB, AC$. Đoạn thẳng $MN$ được gọi là:",
        "options": [
          "Đường trung bình của tam giác $ABC$",
          "Đường trung trực của tam giác $ABC$",
          "Đường phân giác của tam giác $ABC$",
          "Đường cao của tam giác $ABC$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Đường trung bình của tam giác có độ dài bằng bao nhiêu so với cạnh song song với nó?",
        "options": [
          "Một nửa",
          "Bằng nhau",
          "Một phần ba",
          "Gấp đôi"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$ có $AD$ là tia phân giác của góc $A$ ($D \\in BC$). Đẳng thức nào sau đây đúng?",
        "options": [
          "$\frac{DB}{DC} = \frac{AB}{AC}$",
          "$\frac{DB}{DC} = \frac{AC}{AB}$",
          "$\frac{DB}{AB} = \frac{DC}{BC}$",
          "$DB \\cdot AB = DC \\cdot AC$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$ có $MN$ là đường trung bình song song với $BC$. Biết $BC = 14\text{ cm}$. Độ dài $MN$ là:",
        "options": [
          "$7\text{ cm}$",
          "$28\text{ cm}$",
          "$4.6\text{ cm}$",
          "$3.5\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $DE \\parallel BC$ ($D \\in AB, E \\in AC$). Biết $AD = 4\text{ cm}, DB = 2\text{ cm}, AE = 6\text{ cm}$. Độ dài đoạn thẳng $EC$ là:",
        "options": [
          "$3\text{ cm}$",
          "$4\text{ cm}$",
          "$2\text{ cm}$",
          "$5\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $AB = 6\text{ cm}, AC = 8\text{ cm}, BC = 10\text{ cm}$. $AD$ là phân giác của góc $A$ ($D \\in BC$). Độ dài đoạn thẳng $BD$ là:",
        "options": [
          "$\frac{30}{7}\text{ cm}$",
          "$4\text{ cm}$",
          "$5\text{ cm}$",
          "$\frac{40}{7}\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ vuông tại $A$ có $AB = 6\text{ cm}, AC = 8\text{ cm}$. Gọi $M$ là trung điểm của $BC$. Độ dài đoạn thẳng $AM$ là:",
        "options": [
          "$5\text{ cm}$",
          "$10\text{ cm}$",
          "$4\text{ cm}$",
          "$4.8\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Một cột đèn có bóng trên mặt đất dài $4\text{ m}$. Cùng lúc đó một cọc thẳng đứng cao $1\text{ m}$ có bóng dài $0.8\text{ m}$. Chiều cao cột đèn là:",
        "options": [
          "$5\text{ m}$",
          "$4.5\text{ m}$",
          "$3.2\text{ m}$",
          "$6\text{ m}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $E, F$ lần lượt là trung điểm của $AD, BC$. Biết $AB = 5\text{ cm}, CD = 11\text{ cm}$. Độ dài đoạn thẳng $EF$ là:",
        "options": [
          "$8\text{ cm}$",
          "$6\text{ cm}$",
          "$16\text{ cm}$",
          "$7\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $D$ là trung điểm $AB$, $E$ là trung điểm $AC$. Tỉ số diện tích $\frac{S_{\triangle ADE}}{S_{\triangle ABC}}$ bằng:",
        "options": [
          "$\frac{1}{4}$",
          "$\frac{1}{2}$",
          "$\frac{1}{3}$",
          "$\frac{1}{8}$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\text{ cm}, AC = 8\text{ cm}$. Gọi $M$ là trung điểm của $BC$. Kẻ $MD \\perp AB$ tại $D$ và $ME \\perp AC$ tại $E$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Độ dài cạnh huyền $BC = 10\text{ cm}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tứ giác $ADME$ có ba góc vuông nên là hình chữ nhật.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Điểm $D$ là trung điểm của $AB$ và điểm $E$ là trung điểm của $AC$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Độ dài đoạn thẳng $DE = 6\text{ cm}$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ có $AB = 8\text{ cm}, AC = 12\text{ cm}, BC = 15\text{ cm}$. Kẻ phân giác $AD$ của góc $A$ ($D \\in BC$). Qua $D$ kẻ đường thẳng song song với $AB$ cắt $AC$ tại $E$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tỉ số $\frac{DB}{DC} = \frac{2}{3}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Độ dài đoạn thẳng $BD = 6\text{ cm}$ và $DC = 9\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tam giác $ADE$ là tam giác cân tại $E$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Độ dài đoạn thẳng $DE = 4.8\text{ cm}$.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $MN \\parallel BC$ ($M \\in AB, N \\in AC$). Biết $AM = 4\text{ cm}, MB = 2\text{ cm}, MN = 6\text{ cm}$. Tính độ dài cạnh $BC$ theo cm.",
        "answer": "9"
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có chu vi bằng $28\text{ cm}$. Gọi $D, E, F$ lần lượt là trung điểm của ba cạnh tam giác. Tính chu vi tam giác $DEF$ theo cm.",
        "answer": "14"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho $\triangle ABC$ có $AB = 6\text{ cm}, AC = 9\text{ cm}$. Phân giác trong $AD$ cắt $BC$ tại $D$. Biết $BC = 10\text{ cm}$. Tính độ dài đoạn thẳng $CD$ theo cm.",
        "answer": "6"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 9, AC = 12$. Gọi $D$ là trung điểm của $AB$, $E$ là trung điểm của $AC$. Gọi $G$ là trọng tâm của tam giác $ABC$. Tính diện tích tứ giác $BDGE$ theo đơn vị $\text{cm}^2$.",
        "answer": "27"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $AB = 9\text{ cm}, AC = 12\text{ cm}, BC = 14\text{ cm}$. Đường phân giác của góc $A$ cắt cạnh $BC$ tại $D$.\na) Tính độ dài các đoạn thẳng $BD$ và $CD$.\nb) Qua $D$ kẻ đường thẳng song song với $AC$ cắt $AB$ tại $M$. Tính độ dài đoạn thẳng $DM$.",
        "rubric": "a) Áp dụng tính chất phân giác: BD/CD = AB/AC = 9/12 = 3/4. Suy ra BD/3 = CD/4 = (BD + CD)/(3 + 4) = 14/7 = 2. Vậy BD = 6 cm, CD = 8 cm (0.5đ).\nb) DM // AC => DM/AC = BD/BC <=> DM/12 = 6/14 = 3/7 => DM = (12*3)/7 = 36/7 cm (xấp xỉ 5.14 cm) (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình bình hành $ABCD$. Gọi $M$ là trung điểm của cạnh $AB$, $N$ là trung điểm của cạnh $CD$. Đoạn thẳng $DN$ cắt $AC$ tại $E$, đoạn thẳng $BM$ cắt $AC$ tại $F$.\na) Chứng minh rằng $AE = EF = FC$.\nb) Chứng minh rằng tứ giác $EMFN$ là hình bình hành.",
        "rubric": "a) Xét tam giác ABC có F là trọng tâm (giao điểm của đường chéo và trung tuyến BM) => CF = 2/3 đường trung tuyến = 1/3 AC. Tương tự trong tam giác ADC có E là trọng tâm => AE = 1/3 AC. Suy ra AE = EF = FC = 1/3 AC (0.5đ).\nb) Do AE = FC và AM = NC, góc MAF = góc NCE => tam giác AMF = tam giác CNE => MF = NE. Tương tự ME = NF => tứ giác EMFN là hình bình hành (0.5đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho hình thang $ABCD$ ($AB \\parallel CD$, $AB < CD$). Hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Đường thẳng qua $O$ song song với $AB$ cắt $AD, BC$ lần lượt tại $M$ và $N$.\na) Chứng minh rằng $OM = ON$.\nb) Biết diện tích tam giác $AOB$ bằng $a^2$ và diện tích tam giác $COD$ bằng $b^2$. Tính diện tích hình thang $ABCD$ theo $a$ và $b$.",
        "rubric": "a) Theo hệ quả Thalès: OM/CD = AO/AC và ON/CD = BN/BC. Mà AO/AC = BN/BC nên OM = ON (0.5đ).\nb) Tam giác AOB đồng dạng tam giác COD với tỉ số k = a/b = AB/CD => OA/OC = OB/OD = a/b. Tính S(AOD) = S(BOC) = a*b. Vậy diện tích hình thang ABCD = S(AOB) + S(COD) + S(AOD) + S(BOC) = a^2 + b^2 + 2ab = (a + b)^2 (0.5đ)."
      }
    ]
  },
  "c4_8_bai4_test2": {
    "title": "Toán 8 (KNTT) - Bài kiểm tra cuối Chương IV: Định lí Thalès - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Cho $\triangle ABC$. Điểm $D \\in AB, E \\in AC$. Điều kiện nào sau đây KHÔNG khẳng định được $DE \\parallel BC$?",
        "options": [
          "$\frac{AD}{AB} = \frac{DE}{BC}$",
          "$\frac{AD}{DB} = \frac{AE}{EC}$",
          "$\frac{AD}{AB} = \frac{AE}{AC}$",
          "$\frac{DB}{AB} = \frac{EC}{AC}$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $AB = 9, AC = 12$. Lấy $M$ trên $AB$ sao cho $AM = 3$. Kẻ $MN \\parallel BC$ ($N \\in AC$). Độ dài đoạn thẳng $AN$ là:",
        "options": [
          "$4$",
          "$3$",
          "$6$",
          "$5$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có chu vi $24\text{ cm}$. Gọi $M, N, P$ lần lượt là trung điểm của ba cạnh. Chu vi tam giác $MNP$ bằng:",
        "options": [
          "$12\text{ cm}$",
          "$6\text{ cm}$",
          "$8\text{ cm}$",
          "$16\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Thông hiểu",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$) có $AB = 4\text{ cm}, CD = 8\text{ cm}$. Giao điểm của hai đường chéo là $O$. Tỉ số $\frac{OA}{OC}$ bằng:",
        "options": [
          "$\frac{1}{2}$",
          "$\frac{1}{3}$",
          "$\frac{2}{3}$",
          "$2$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có phân giác $AD$. Biết $AB = 8, AC = 12$ và $BD = 4$. Độ dài cạnh $BC$ là:",
        "options": [
          "$10$",
          "$6$",
          "$8$",
          "$12$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $AB = 6\text{ cm}, AC = 9\text{ cm}$. Phân giác góc ngoài tại đỉnh $A$ cắt đường thẳng $BC$ tại $E$. Tỉ số $\frac{EB}{EC}$ bằng:",
        "options": [
          "$\frac{2}{3}$",
          "$\frac{3}{2}$",
          "$\frac{1}{3}$",
          "$\frac{2}{5}$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$. Gọi $D, E$ lần lượt là trung điểm của $AB, BC$. Lấy $K$ trên đoạn $DE$ sao cho $DK = 2KE$. Tỉ số $\frac{DK}{AC}$ bằng:",
        "options": [
          "$\frac{1}{3}$",
          "$\frac{1}{4}$",
          "$\frac{1}{6}$",
          "$\frac{2}{3}$"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho hình thoi $ABCD$. Gọi $E, F, G, H$ lần lượt là trung điểm của $AB, BC, CD, DA$. Tứ giác $EFGH$ là hình gì?",
        "options": [
          "Hình chữ nhật",
          "Hình thoi",
          "Hình vuông",
          "Hình bình hành không có góc vuông"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $DE \\parallel BC$ ($D \\in AB, E \\in AC$). Biết diện tích $\triangle ADE$ bằng $\frac{1}{9}$ diện tích $\triangle ABC$. Tỉ số $\frac{AD}{AB}$ bằng:",
        "options": [
          "$\frac{1}{3}$",
          "$\frac{1}{9}$",
          "$\frac{1}{6}$",
          "$\frac{2}{3}$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ vuông tại $A$ có $AB = 12\text{ cm}, AC = 16\text{ cm}$. Đường phân giác góc $A$ cắt $BC$ tại $D$. Khoảng cách từ $D$ đến cạnh $AB$ bằng:",
        "options": [
          "$\frac{48}{7}\text{ cm}$",
          "$6\text{ cm}$",
          "$8\text{ cm}$",
          "$\frac{36}{7}\text{ cm}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có đường trung tuyến $AM$. Gọi $G$ là trọng tâm. Qua $G$ kẻ đường thẳng song song với $BC$ cắt $AB$ tại $D$ và $AC$ tại $E$. Khẳng định nào sau đây là SAI?",
        "options": [
          "$\frac{AD}{AB} = \frac{1}{3}$",
          "$\frac{AD}{AB} = \frac{2}{3}$",
          "$\frac{DE}{BC} = \frac{2}{3}$",
          "$\frac{S_{\triangle ADE}}{S_{\triangle ABC}} = \frac{4}{9}$"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$. Đường phân giác của góc $B$ cắt $AC$ tại $D$. Từ $D$ kẻ đường thẳng song song với $BC$ cắt $AB$ tại $E$. Khẳng định nào sau đây đúng?",
        "options": [
          "$ED = EB$",
          "$ED = EA$",
          "$ED = BC$",
          "$ED = AD$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ vuông tại $A$ ($AB = 6\text{ cm}, AC = 8\text{ cm}$). Kẻ đường cao $AH$. Gọi $D, E$ lần lượt là hình chiếu của $H$ trên $AB$ và $AC$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Độ dài đường cao $AH = 4.8\text{ cm}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tứ giác $ADHE$ là hình chữ nhật và có độ dài $DE = 4.8\text{ cm}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Hệ thức $AD \\cdot AB = AE \\cdot AC$ là một hệ thức đúng.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng $DE$ song song với cạnh huyền $BC$.",
            "correct": false
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $M$ là trung điểm của cạnh đáy $AB$. Giao điểm của $DM$ và $AC$ là $E$, giao điểm của $CM$ và $BD$ là $F$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Theo định lí Thalès, $\frac{ME}{ED} = \frac{AM}{CD}$ và $\frac{MF}{FC} = \frac{MB}{CD}$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Đoạn thẳng $EF$ song song với hai đáy $AB$ và $CD$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng thấp",
            "text": "Tỉ số $\frac{EF}{CD} = \frac{AB}{AB + 2CD}$.",
            "correct": false
          },
          {
            "key": "d",
            "level": "Vận dụng thấp",
            "text": "Đoạn thẳng $EF$ cắt hai cạnh bên $AD$ và $BC$ tại các điểm chia các cạnh bên theo cùng tỉ số.",
            "correct": true
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$ có $AB = 10, AC = 15$. Kẻ phân giác $AD$ ($D \\in BC$). Kẻ $DE \\parallel AB$ ($E \\in AC$). Biết $BC = 20$. Tính độ dài $DE$.",
        "answer": "6"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$) có hai đáy $AB = 8\text{ cm}, CD = 18\text{ cm}$. Hai đường chéo cắt nhau tại $O$. Qua $O$ vẽ đường thẳng song song với hai đáy cắt hai cạnh bên tại $M$ và $N$. Tính độ dài đoạn thẳng $MN$ theo cm (kết quả dạng số thập phân, ví dụ 11.08).",
        "answer": "11.08"
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ có trung tuyến $AM = 12\text{ cm}$. Lấy $D$ trên $AM$ sao cho $AD = 8\text{ cm}$. Đường thẳng qua $D$ song song với $BC$ cắt $AB, AC$ lần lượt tại $E, F$. Tính tỉ số $\frac{EF}{BC}$ (kết quả dạng phân số tối giản a/b, điền a/b).",
        "answer": "2/3"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$ vuông tại $A$ có $AB = 15, AC = 20$. Kẻ đường phân giác trong $AD$ và phân giác ngoài $AE$ ($D, E \\in BC$). Tính độ dài đoạn thẳng $DE$.",
        "answer": "85.71"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ vuông tại $A$. Đường cao $AH$ cắt đường phân giác $BD$ tại $I$.\na) Chứng minh tam giác $AID$ cân tại $A$.\nb) Chứng minh rằng $IH \\cdot CD = IA \\cdot AD$.",
        "rubric": "a) Xét góc AID = góc BIH (đối đỉnh) = 90 - góc HBD. Góc ADI = 90 - góc ABD. Vì BD là phân giác góc B nên góc HBD = góc ABD => góc AID = góc ADI => tam giác AID cân tại A (0.5đ).\nb) Tam giác ABD có đường phân giác BI => IH/IA = BH/BA. Lại có BH/BA = AB/BC = AD/CD => IH/IA = AD/CD => IH * CD = IA * AD (0.5đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Gọi $M$ là trung điểm của $BC$. Phân giác của góc $AMB$ cắt $AB$ tại $D$, phân giác của góc $AMC$ cắt $AC$ tại $E$.\na) Chứng minh rằng $DE \\parallel BC$.\nb) Gọi $I$ là giao điểm của $DE$ và $AM$. Chứng minh rằng $I$ là trung điểm của $DE$.",
        "rubric": "a) Theo tính chất phân giác: DA/DB = MA/MB và EA/EC = MA/MC. Vì MB = MC nên DA/DB = EA/EC => DE // BC theo định lí Thalès đảo (0.5đ).\nb) Áp dụng hệ quả Thalès: trong tam giác ABM có DI // BM => DI/BM = AI/AM. Trong tam giác ACM có IE // MC => IE/MC = AI/AM. Suy ra DI/BM = IE/MC. Mà BM = MC nên DI = IE => I là trung điểm DE (0.5đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tam giác $ABC$. Lấy điểm $O$ nằm trong tam giác. Các tia $AO, BO, CO$ cắt các cạnh $BC, CA, AB$ lần lượt tại $D, E, F$.\nChứng minh rằng: $\frac{OD}{AD} + \frac{OE}{BE} + \frac{OF}{CF} = 1$ và $\frac{AO}{AD} + \frac{BO}{BE} + \frac{CO}{CF} = 2$.",
        "rubric": "Nhận xét diện tích: S(OBC)/S(ABC) = OD/AD (chiều cao tỉ lệ cạnh đối diện) (0.25đ). Tương tự OE/BE = S(OCA)/S(ABC) và OF/CF = S(OAB)/S(ABC) (0.25đ). Do đó: OD/AD + OE/BE + OF/CF = (S(OBC) + S(OCA) + S(OAB))/S(ABC) = 1 (0.25đ). Ta có AO/AD = 1 - OD/AD, BO/BE = 1 - OE/BE, CO/CF = 1 - OF/CF. Cộng lại: AO/AD + BO/BE + CO/CF = 3 - (OD/AD + OE/BE + OF/CF) = 3 - 1 = 2 (0.25đ)."
      }
    ]
  },
  "c4_8_bai4_test3": {
    "title": "Toán 8 (KNTT) - Bài kiểm tra cuối Chương IV: Định lí Thalès - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho $\triangle ABC$. Lấy điểm $M$ trên cạnh $BC$. Kẻ $MD \\parallel AC$ ($D \\in AB$) và $ME \\parallel AB$ ($E \\in AC$). Đẳng thức nào sau đây luôn đúng?",
        "options": [
          "$\frac{MD}{AC} + \frac{ME}{AB} = 1$",
          "$\frac{MD}{AB} + \frac{ME}{AC} = 1$",
          "$\frac{MD}{AC} \\cdot \frac{ME}{AB} = 1$",
          "$MD + ME = BC$"
        ],
        "correct": 0
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho hình bình hành $ABCD$. Một đường thẳng đi qua $D$ cắt cạnh $BC$ tại $P$ và cắt tia đối của tia $AB$ tại $Q$. Hệ thức nào sau đây đúng?",
        "options": [
          "$DP \\cdot DQ = CD \\cdot AD$",
          "$\frac{DP}{DQ} = \frac{CP}{BQ}$",
          "$DP^2 = BP \\cdot CP$",
          "$\frac{1}{DP} + \frac{1}{DQ} = \frac{1}{CD}$"
        ],
        "correct": 0
      },
      {
        "id": 3,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$. Các đường phân giác $AD, BE, CF$ đồng quy tại $I$. Khẳng định nào sau đây thể hiện định lí Ceva cho đường phân giác?",
        "options": [
          "$\frac{DB}{DC} \\cdot \frac{EC}{EA} \\cdot \frac{FA}{FB} = 1$",
          "$\frac{DB}{DC} + \frac{EC}{EA} + \frac{FA}{FB} = 1$",
          "$\frac{DB}{DC} \\cdot \frac{EC}{EA} \\cdot \frac{FA}{FB} = -1$",
          "$DB \\cdot EC \\cdot FA = DC \\cdot EA \\cdot FB = 1$"
        ],
        "correct": 0
      },
      {
        "id": 4,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Phân giác của góc $B$ cắt $AH$ tại $E$ và cắt $AC$ tại $F$. Tỉ số $\frac{EH}{EA}$ bằng tỉ số nào dưới đây?",
        "options": [
          "$\frac{FA}{FC}$",
          "$\frac{FC}{FA}$",
          "$\frac{AB}{BC}$",
          "$\frac{BH}{BA}$"
        ],
        "correct": 0
      },
      {
        "id": 5,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Hai đường chéo cắt nhau tại $O$. Một đường thẳng qua $O$ cắt $AB$ tại $E$ và cắt $CD$ tại $F$. Tỉ số $\frac{OE}{OF}$ bằng:",
        "options": [
          "$\frac{AB}{CD}$",
          "$\frac{CD}{AB}$",
          "$1$",
          "$\\left(\frac{AB}{CD}\right)^2$"
        ],
        "correct": 0
      },
      {
        "id": 6,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ có $AB = 6, AC = 8, BC = 10$. Gọi $I$ là tâm đường tròn nội tiếp tam giác. Khoảng cách từ $I$ đến các cạnh của tam giác bằng:",
        "options": [
          "$2$",
          "$2.5$",
          "$3$",
          "$1.5$"
        ],
        "correct": 0
      },
      {
        "id": 7,
        "level": "Vận dụng thấp",
        "question": "Cho tứ giác $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $AD, BC$. Biết $MN = \frac{AB + CD}{2}$. Khi đó tứ giác $ABCD$ là:",
        "options": [
          "Hình thang có hai đáy $AB$ và $CD$",
          "Hình bình hành",
          "Hình chữ nhật",
          "Tứ giác có hai đường chéo vuông góc"
        ],
        "correct": 0
      },
      {
        "id": 8,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$ nhọn. Các đường cao $AD, BE, CF$ cắt nhau tại $H$. Gọi $M$ là trung điểm của $BC$. Đường thẳng qua $H$ vuông góc với $MH$ cắt $AB, AC$ lần lượt tại $P, Q$. Kết luận nào sau đây đúng?",
        "options": [
          "$HP = HQ$",
          "$HP = 2HQ$",
          "$HQ = 2HP$",
          "$P, Q, M$ thẳng hàng"
        ],
        "correct": 0
      },
      {
        "id": 9,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$. Lấy điểm $D$ trên cạnh $BC$. Gọi $r_1, r_2, r$ lần lượt là bán kính đường tròn nội tiếp của $\triangle ABD, \triangle ACD, \triangle ABC$. Hệ thức nào sau đây luôn đúng?",
        "options": [
          "$r_1 + r_2 > r$",
          "$r_1 + r_2 = r$",
          "$r_1 + r_2 < r$",
          "$r_1 \\cdot r_2 = r^2$"
        ],
        "correct": 0
      },
      {
        "id": 10,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$ có trọng tâm $G$. Một đường thẳng $d$ đi qua $G$ cắt hai cạnh $AB, AC$ tại $M, N$. Gọi $S$ là diện tích tam giác $AMN$ và $S_0$ là diện tích tam giác $ABC$. Giá trị nhỏ nhất của tỉ số $\frac{S}{S_0}$ bằng:",
        "options": [
          "$\frac{4}{9}$",
          "$\frac{1}{2}$",
          "$\frac{1}{3}$",
          "$\frac{2}{3}$"
        ],
        "correct": 0
      },
      {
        "id": 11,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$. Kẻ ba đường phân giác trong $AD, BE, CF$. Đặt $BC = a, CA = b, AB = c$. Biểu thức $\frac{AD^2}{bc} + \frac{BE^2}{ca} + \frac{CF^2}{ab}$ đạt giá trị lớn nhất khi:",
        "options": [
          "Tam giác $ABC$ đều",
          "Tam giác $ABC$ vuông cân",
          "Tam giác $ABC$ cân có góc $120^\\circ$",
          "Mọi tam giác"
        ],
        "correct": 0
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho hình bình hành $ABCD$. Điểm $M$ thuộc đường chéo $AC$. Đường thẳng qua $M$ song song với $AB$ cắt $AD, BC$ tại $E, F$. Đường thẳng qua $M$ song song với $AD$ cắt $AB, CD$ tại $H, K$. Diện tích hai hình bình hành $EMKD$ và $MFBH$:",
        "options": [
          "Luôn bằng nhau",
          "Diện tích $EMKD$ lớn hơn",
          "Diện tích $MFBH$ lớn hơn",
          "Chỉ bằng nhau khi $M$ là trung điểm $AC$"
        ],
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Cho tam giác $ABC$ nhọn ($AB < AC$). Các đường cao $AD, BE, CF$ cắt nhau tại trực tâm $H$. Gọi $M$ là trung điểm của $BC$. Đường thẳng qua $H$ vuông góc với $AM$ cắt các đường thẳng $AB, AC$ lần lượt tại $P$ và $Q$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tam giác $ABD$ đồng dạng với tam giác $CBE$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Vận dụng thấp",
            "text": "Hệ thức $AF \\cdot AB = AE \\cdot AC = AH \\cdot AD$ là đúng.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng cao",
            "text": "Đoạn thẳng $HP$ bằng đoạn thẳng $HQ$ ($H$ là trung điểm $PQ$).",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Bốn điểm $B, C, P, Q$ cùng nằm trên một đường tròn.",
            "correct": true
          }
        ]
      },
      {
        "id": 2,
        "stem": "Cho tam giác $ABC$ có ba góc nhọn. Gọi $I$ là tâm đường tròn nội tiếp tam giác. Đường thẳng qua $I$ vuông góc với $AI$ cắt các cạnh $AB, AC$ lần lượt tại $M$ và $N$.",
        "statements": [
          {
            "key": "a",
            "level": "Thông hiểu",
            "text": "Tam giác $AMN$ là tam giác cân tại $A$ có đường cao $AI$.",
            "correct": true
          },
          {
            "key": "b",
            "level": "Vận dụng thấp",
            "text": "Góc $\\widehat{BMI} = \\widehat{C} + \frac{\\widehat{A}}{2}$.",
            "correct": true
          },
          {
            "key": "c",
            "level": "Vận dụng cao",
            "text": "Tam giác $BMI$ đồng dạng với tam giác $INC$.",
            "correct": true
          },
          {
            "key": "d",
            "level": "Vận dụng cao",
            "text": "Hệ thức $BM \\cdot CN = AI^2$ là một hệ thức đúng.",
            "correct": false
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho tam giác $ABC$ có $AB = 10, AC = 15, BC = 20$. Phân giác $AD$ cắt $BC$ tại $D$. Gọi $I$ là tâm đường tròn nội tiếp. Tính tỉ số $\frac{AI}{ID}$ (kết quả dạng phân số tối giản a/b, điền a/b).",
        "answer": "5/4"
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$) có $AB = 6\text{ cm}, CD = 14\text{ cm}$. Hai đường chéo cắt nhau tại $O$. Qua $O$ kẻ đường thẳng song song với hai đáy cắt hai cạnh bên tại $M$ và $N$. Tính độ dài $MN$ theo cm (kết quả dạng số thập phân làm tròn 1 chữ số sau dấu phẩy).",
        "answer": "8.4"
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\text{ cm}, AC = 8\text{ cm}$. Đường phân giác của góc $A$ cắt cạnh huyền $BC$ tại $D$. Kẻ $DH \\perp AB$. Tính độ dài đoạn thẳng $DH$ (kết quả dạng số thập phân làm tròn 2 chữ số sau dấu phẩy).",
        "answer": "3.43"
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho $\triangle ABC$ có diện tích bằng $90\text{ cm}^2$. Trọng tâm là $G$. Một đường thẳng đi qua $G$ cắt hai cạnh $AB, AC$ tại $M, N$. Diện tích nhỏ nhất của tam giác $AMN$ bằng bao nhiêu $\text{cm}^2$?",
        "answer": "40"
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho hình thang $ABCD$ ($AB \\parallel CD$). Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$.\na) Chứng minh rằng diện tích hai tam giác $AOD$ và $BOC$ bằng nhau.\nb) Biết $AB = 4\text{ cm}, CD = 9\text{ cm}$. Tính tỉ số diện tích $\frac{S_{\triangle AOB}}{S_{\triangle COD}}$ và tính diện tích hình thang $ABCD$ nếu biết $S_{\triangle AOB} = 16\text{ cm}^2$.",
        "rubric": "a) Xét tam giác ACD và BCD có đáy chung CD, chiều cao bằng nhau (khoảng cách giữa hai đáy song song) => S(ACD) = S(BCD). Trừ đi phần diện tích chung S(OCD) ta được: S(AOD) = S(BOC) (0.5đ).\nb) Tam giác AOB đồng dạng tam giác COD theo tỉ số k = AB/CD = 4/9 => S(AOB)/S(COD) = k^2 = 16/81 (0.25đ). Biết S(AOB) = 16 cm^2 => S(COD) = 81 cm^2. Khi đó S(AOD) = S(BOC) = sqrt(16 * 81) = 36 cm^2. Diện tích hình thang ABCD = 16 + 81 + 36 + 36 = 169 cm^2 (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng thấp",
        "question": "Cho tam giác $ABC$ có ba góc nhọn. Các đường cao $AD, BE, CF$ cắt nhau tại $H$.\na) Chứng minh rằng $BH \\cdot BE + CH \\cdot CF = BC^2$.\nb) Chứng minh rằng $H$ là giao điểm các đường phân giác của tam giác $DEF$ (tam giác trực tâm).",
        "rubric": "a) Kẻ hình chiếu hoặc dùng hệ thức lượng: BH * BE = BC * BD và CH * CF = BC * CD (0.25đ). Cộng lại: BH * BE + CH * CF = BC * (BD + CD) = BC * BC = BC^2 (0.25đ).\nb) Chứng minh tứ giác BDHF và CDHE nội tiếp (hoặc các góc tương ứng bằng nhau) => góc HDF = góc HBF = 90 - C = góc HCE = góc HDE => DH là phân giác góc EDF. Tương tự EH, FH là phân giác các góc còn lại của tam giác DEF => H là giao điểm 3 đường phân giác của tam giác DEF (0.5đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "(Câu điểm 10)\nCho tam giác $ABC$ có $BC = a, CA = b, AB = c$. Gọi $I$ là tâm đường tròn nội tiếp tam giác. Đường thẳng vuông góc với $AI$ tại $I$ cắt các cạnh $AB, AC$ lần lượt tại $M, N$.\na) Chứng minh rằng $AM = AN = \frac{2bc}{b+c} \\cdot \\cos^2\frac{A}{2}$ (hoặc tính theo các đoạn tiếp tuyến).\nb) Chứng minh rằng $BM \\cdot CN = IM^2 = IN^2$.",
        "rubric": "a) Xét tam giác AMN có AI là phân giác góc A và AI vuông góc MN nên tam giác AMN cân tại A => AM = AN và AI là đường cao đồng thời là trung trực (0.25đ). Dùng công thức lượng giác hoặc diện tích tính được độ dài AM = AN (0.25đ).\nb) Ta tính góc: góc MIB = góc MBI = góc B/2 + góc A/2 = ... => tam giác BMI đồng dạng tam giác INC (g-g) vì góc MIB = góc NCI và góc BMI = góc NIC (0.25đ). Từ tỉ số đồng dạng suy ra BM/IN = MI/CN => BM * CN = MI * IN = IM^2 (do IM = IN). Ta có điều phải chứng minh (0.25đ)."
      }
    ]
  }
};

const EXAMS_8_C4_8 = CHAPTER4_TOAN8_EXAMS;

if (typeof window !== 'undefined') {
  window.CHAPTER4_TOAN8_EXAMS = CHAPTER4_TOAN8_EXAMS;
  window.EXAMS_8_C4_8 = CHAPTER4_TOAN8_EXAMS;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CHAPTER4_TOAN8_EXAMS, EXAMS_8_C4_8 };
}
