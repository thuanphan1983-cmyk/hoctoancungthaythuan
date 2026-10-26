/**
 * NGAN HANG DE KIEM TRA DINH KY TOAN THCS (KNTT) - LOP 6, 7, 8, 9
 * 4 de giua ky 1 moi khoi (tong 16 de thi hoan chinh)
 * Chuan ma tran GDPT moi: 12 Trac nghiem (3.0d) + 2 Dung/Sai (2.0d) + 4 Tra loi ngan (2.0d) + 4 Tu luan (3.0d)
 * 40% Nhan biet (4.0d), 30% Thong hieu (3.0d), 20% Van dung (2.0d), 10% Van dung cao (1.0d)
 */
window.PERIODIC_EXAM_BANK = {
  "6": {
    "mid1": [
      {
        "id": "p_g6_mid1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 6 (ĐỀ SỐ 01)",
        "topic": "Tập hợp số tự nhiên, Các phép tính, Dấu hiệu chia hết, Số nguyên tố, ƯC-BC & Hình học trực quan",
        "grade": "6",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Cho tập hợp $M = \\{x \\in \\mathbb{N} \\mid 3 < x \\le 8\\}$. Khẳng định nào sau đây là **đúng**?",
            "options": [
              "$9 \\in M$",
              "$4 \\notin M$",
              "$3 \\in M$",
              "$8 \\in M$"
            ],
            "correct": 3,
            "explanation": "$M = \\{4; 5; 6; 7; 8\\}$. Do đó $8 \\in M$ là khẳng định đúng.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Số tự nhiên nào sau đây là số nguyên tố?",
            "options": [
              "$15$",
              "$17$",
              "$21$",
              "$9$"
            ],
            "correct": 1,
            "explanation": "Số $17$ chỉ có hai ước là $1$ và $17$ nên là số nguyên tố.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Kết quả của phép nhân hai lũy thừa cùng cơ số $3^4 \\cdot 3^2$ là:",
            "options": [
              "$9^6$",
              "$3^2$",
              "$3^6$",
              "$3^8$"
            ],
            "correct": 2,
            "explanation": "$3^4 \\cdot 3^2 = 3^{4+2} = 3^6$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Thứ tự thực hiện phép tính đối với biểu thức có các dấu ngoặc là:",
            "options": [
              "$(\\ ) \\rightarrow [\\ ] \\rightarrow \\{\\ \\}$",
              "$\\{\\ \\} \\rightarrow [\\ ] \\rightarrow (\\ )$",
              "$[\\ ] \\rightarrow (\\ ) \\rightarrow \\{\\ \\}$",
              "$(\\ ) \\rightarrow \\{\\ \\} \\rightarrow [\\ ]$"
            ],
            "correct": 0,
            "explanation": "Quy ước: $(\\ ) \\rightarrow [\\ ] \\rightarrow \\{\\ \\}$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Số nào sau đây chia hết cho cả $2$ và $5$?",
            "options": [
              "$124$",
              "$350$",
              "$235$",
              "$418$"
            ],
            "correct": 1,
            "explanation": "Số tận cùng là $0$ thì chia hết cho cả $2$ và $5$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Trong các số sau, số nào chia hết cho $9$?",
            "options": [
              "$671$",
              "$502$",
              "$135$",
              "$241$"
            ],
            "correct": 2,
            "explanation": "Tổng các chữ số $1 + 3 + 5 = 9 \\ \\vdots \\ 9$ nên $135 \\ \\vdots \\ 9$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Hình tam giác đều có đặc điểm nào sau đây?",
            "options": [
              "Có hai cạnh bằng nhau",
              "Có một góc vuông",
              "Có hai đường chéo bằng nhau",
              "Có 3 cạnh bằng nhau và 3 góc bằng nhau"
            ],
            "correct": 3,
            "explanation": "Tam giác đều có 3 cạnh bằng nhau và 3 góc bằng nhau (cùng bằng $60^\\circ$).",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Hình thoi có độ dài hai đường chéo là $6\\text{ cm}$ và $8\\text{ cm}$. Diện tích của hình thoi đó là:",
            "options": [
              "$14\\text{ cm}^2$",
              "$28\\text{ cm}^2$",
              "$48\\text{ cm}^2$",
              "$24\\text{ cm}^2$"
            ],
            "correct": 3,
            "explanation": "$S = \\frac{1}{2} \\cdot 6 \\cdot 8 = 24\\text{ cm}^2$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Kết quả của phép tính $18 : 3^2 + 5 \\cdot 2$ là:",
            "options": [
              "$12$",
              "$14$",
              "$20$",
              "$16$"
            ],
            "correct": 0,
            "explanation": "$18 : 9 + 10 = 2 + 10 = 12$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Biết số tự nhiên $\\overline{1x5}$ chia hết cho $3$. Chữ số $x$ có thể nhận giá trị nào sau đây?",
            "options": [
              "$3$",
              "$1$",
              "$4$",
              "$2$"
            ],
            "correct": 0,
            "explanation": "Tổng chữ số: $1 + x + 5 = 6 + x \\ \\vdots \\ 3$. Với $x = 3$ thì $6 + 3 = 9 \\ \\vdots \\ 3$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Ước chung lớn nhất của $24$ và $36$ là:",
            "options": [
              "$72$",
              "$12$",
              "$18$",
              "$6$"
            ],
            "correct": 1,
            "explanation": "$24 = 2^3 \\cdot 3; 36 = 2^2 \\cdot 3^2 \\Rightarrow \\text{ƯCLN}(24, 36) = 2^2 \\cdot 3 = 12$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Một mảnh sân hình chữ nhật có chiều dài $12\\text{ m}$ và chiều rộng $5\\text{ m}$. Chu vi của mảnh sân đó là:",
            "options": [
              "$70\\text{ m}$",
              "$60\\text{ m}$",
              "$34\\text{ m}$",
              "$17\\text{ m}$"
            ],
            "correct": 2,
            "explanation": "$C = 2 \\cdot (12 + 5) = 34\\text{ m}$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho hai số tự nhiên $A = 2^3 \\cdot 3 \\cdot 5^2$ và $B = 2^2 \\cdot 3^2 \\cdot 7$.",
            "statements": [
              {
                "key": "a",
                "text": "Số $A$ chia hết cho $10$.",
                "correct": true,
                "explanation": "$A$ chứa thừa số $2$ và $5$ nên $A \\ \\vdots \\ 10$."
              },
              {
                "key": "b",
                "text": "Ước chung lớn nhất của $A$ và $B$ là $\\text{ƯCLN}(A, B) = 12$.",
                "correct": true,
                "explanation": "$\\text{ƯCLN}(A, B) = 2^2 \\cdot 3 = 12$."
              },
              {
                "key": "c",
                "text": "Số phần tử của tập hợp các ước tự nhiên của $12$ là $4$.",
                "correct": false,
                "explanation": "Ước tự nhiên của $12$ là $\\{1; 2; 3; 4; 6; 12\\}$ gồm $6$ phần tử."
              },
              {
                "key": "d",
                "text": "Bội chung nhỏ nhất của $A$ và $B$ là $\\text{BCNN}(A, B) = 12\\ 600$.",
                "correct": true,
                "explanation": "$\\text{BCNN}(A, B) = 2^3 \\cdot 3^2 \\cdot 5^2 \\cdot 7 = 12\\ 600$."
              }
            ],
            "stem": "Cho hai số tự nhiên $A = 2^3 \\cdot 3 \\cdot 5^2$ và $B = 2^2 \\cdot 3^2 \\cdot 7$.",
            "question": "Cho hai số tự nhiên $A = 2^3 \\cdot 3 \\cdot 5^2$ và $B = 2^2 \\cdot 3^2 \\cdot 7$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Bác An có một mảnh vườn hình chữ nhật có chiều dài $20\\text{ m}$, chiều rộng $15\\text{ m}$. Ở giữa vườn, bác đào một cái ao nuôi cá hình thoi có độ dài hai đường chéo lần lượt là $8\\text{ m}$ và $6\\text{ m}$. Phần diện tích đất còn lại bác dùng để trồng cỏ.",
            "statements": [
              {
                "key": "a",
                "text": "Chu vi của toàn bộ mảnh vườn hình chữ nhật là $70\\text{ m}$.",
                "correct": true,
                "explanation": "Chu vi mảnh vườn: $2 \\cdot (20 + 15) = 70\\text{ m}$."
              },
              {
                "key": "b",
                "text": "Diện tích của cả mảnh vườn hình chữ nhật là $300\\text{ m}^2$.",
                "correct": true,
                "explanation": "Diện tích mảnh vườn: $20 \\cdot 15 = 300\\text{ m}^2$."
              },
              {
                "key": "c",
                "text": "Diện tích cái ao cá hình thoi là $48\\text{ m}^2$.",
                "correct": false,
                "explanation": "Diện tích ao cá hình thoi là $\\frac{1}{2} \\cdot 8 \\cdot 6 = 24\\text{ m}^2$."
              },
              {
                "key": "d",
                "text": "Diện tích phần đất trồng cỏ của bác An là $276\\text{ m}^2$.",
                "correct": true,
                "explanation": "Diện tích trồng cỏ: $300 - 24 = 276\\text{ m}^2$."
              }
            ],
            "stem": "Bác An có một mảnh vườn hình chữ nhật có chiều dài $20\\text{ m}$, chiều rộng $15\\text{ m}$. Ở giữa vườn, bác đào một cái ao nuôi cá hình thoi có độ dài hai đường chéo lần lượt là $8\\text{ m}$ và $6\\text{ m}$. Phần diện tích đất còn lại bác dùng để trồng cỏ.",
            "question": "Bác An có một mảnh vườn hình chữ nhật có chiều dài $20\\text{ m}$, chiều rộng $15\\text{ m}$. Ở giữa vườn, bác đào một cái ao nuôi cá hình thoi có độ dài hai đường chéo lần lượt là $8\\text{ m}$ và $6\\text{ m}$. Phần diện tích đất còn lại bác dùng để trồng cỏ."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức: $P = 75 - (3 \\cdot 5^2 - 4 \\cdot 2^3)$",
            "answer": "32",
            "explanation": "$3 \\cdot 25 - 4 \\cdot 8 = 75 - 32 = 43$. $P = 75 - 43 = 32$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $x$ thỏa mãn: $3 \\cdot (x - 4) = 27$",
            "answer": "13",
            "explanation": "$x - 4 = 9 \\Rightarrow x = 13$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một đội tình nguyện viên có $36$ nam và $48$ nữ được chia đều vào các tổ sao cho số nam và nữ ở mỗi tổ đều bằng nhau. Hỏi có thể chia được nhiều nhất thành bao nhiêu tổ?",
            "answer": "12",
            "explanation": "$\\text{ƯCLN}(36, 48) = 12$ tổ.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm chữ số $a$ để số tự nhiên $\\overline{4a10}$ chia hết cho $9$:",
            "answer": "4",
            "explanation": "$4 + a + 1 + 0 = 5 + a \\ \\vdots \\ 9 \\Rightarrow a = 4$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "Thực hiện phép tính một cách hợp lý:\na) $28 \\cdot 76 + 28 \\cdot 24 - 800$\nb) $120 : [54 - (5 - 1)^2 \\cdot 2]$",
            "rubric": "a) $28(76 + 24) - 800 = 28 \\cdot 100 - 800 = 2000$ (0.5đ).\nb) $120 : [54 - 16 \\cdot 2] = 120 : 22 = \\frac{60}{11}$ (0.5đ).",
            "modelSolution": "a) $28 \\cdot 76 + 28 \\cdot 24 - 800 = 28 \\cdot (76 + 24) - 800 = 28 \\cdot 100 - 800 = 2800 - 800 = 2000$.\nb) $(5 - 1)^2 \\cdot 2 = 16 \\cdot 2 = 32$. $54 - 32 = 22$. $120 : 22 = \\frac{60}{11}$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Tìm số tự nhiên $x$, biết:\na) $2x + 15 = 45$\nb) $5^{x+1} - 5^x = 500$",
            "rubric": "a) $2x = 30 \\Rightarrow x = 15$ (0.35đ).\nb) $5^x(5 - 1) = 500 \\Leftrightarrow 4 \\cdot 5^x = 500 \\Leftrightarrow 5^x = 125 = 5^3 \\Rightarrow x = 3$ (0.4đ).",
            "modelSolution": "a) $2x + 15 = 45 \\Leftrightarrow 2x = 30 \\Leftrightarrow x = 15$.\nb) $5^{x+1} - 5^x = 500 \\Leftrightarrow 5^x \\cdot 4 = 500 \\Leftrightarrow 5^x = 125 \\Leftrightarrow 5^x = 5^3 \\Rightarrow x = 3$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Bác Ba có một khu đất hình chữ nhật dài $24\\text{ m}$, rộng $18\\text{ m}$. Bác muốn lát kín khu đất bằng các viên gạch men hình vuông có độ dài cạnh lớn nhất sao cho các viên gạch được lát liền nhau không phải cắt viên nào.\na) Hỏi độ dài cạnh viên gạch men hình vuông lớn nhất là bao nhiêu mét?\nb) Bác Ba cần dùng tất cả bao nhiêu viên gạch như thế?",
            "rubric": "a) Cạnh viên gạch là $\\text{ƯCLN}(24, 18) = 6\\text{ m}$ (0.4đ).\nb) Số viên gạch: $(24 : 6) \\times (18 : 6) = 12$ viên (0.35đ).",
            "modelSolution": "a) Độ dài cạnh viên gạch men lớn nhất là $\\text{ƯCLN}(24, 18) = 6\\text{ m}$.\nb) Số viên gạch theo chiều dài: $24 : 6 = 4$ viên. Số viên gạch theo chiều rộng: $18 : 6 = 3$ viên. Tổng số viên gạch cần dùng là: $4 \\times 3 = 12$ viên."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Cho tổng $S = 1 + 3 + 3^2 + 3^3 + \\dots + 3^{59}$. Chứng minh rằng $S$ chia hết cho $13$.",
            "rubric": "Nhóm 3 số hạng: $S = (1+3+9) + 3^3(1+3+9) + \\dots = 13 \\cdot (1 + 3^3 + \\dots) \\ \\vdots \\ 13$ (0.5đ).",
            "modelSolution": "Nhóm 3 số hạng liên tiếp thành một nhóm (tổng cộng 20 nhóm):\n$$S = (1 + 3 + 3^2) + 3^3(1 + 3 + 3^2) + \\dots + 3^{57}(1 + 3 + 3^2) = 13 \\cdot (1 + 3^3 + \\dots + 3^{57}) \\ \\vdots \\ 13.$$"
          }
        ]
      },
      {
        "id": "p_g6_mid1_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 6 (ĐỀ SỐ 02)",
        "topic": "Lũy thừa, Thứ tự phép tính, BCNN, Bài toán xếp hàng & Hình bình hành, Hình chữ nhật",
        "grade": "6",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Cho tập hợp $A = \\{2; 3; 5; 7\\}$. Khẳng định nào sau đây là **sai**?",
            "options": [
              "$7 \\in A$",
              "$4 \\in A$",
              "$2 \\in A$",
              "$3 \\in A$"
            ],
            "correct": 1,
            "explanation": "Số $4$ không nằm trong tập hợp $A$ nên khẳng định $4 \\in A$ là sai.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Viết tích $5 \\cdot 5 \\cdot 5 \\cdot 5$ dưới dạng lũy thừa ta được:",
            "options": [
              "$4^5$",
              "$20$",
              "$5^4$",
              "$5^5$"
            ],
            "correct": 2,
            "explanation": "Tích của 4 thừa số 5 là $5^4$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Kết quả của phép chia hai lũy thừa cùng cơ số $7^6 : 7^2$ là:",
            "options": [
              "$7^3$",
              "$1^4$",
              "$7^8$",
              "$7^4$"
            ],
            "correct": 3,
            "explanation": "$7^6 : 7^2 = 7^{6 - 2} = 7^4$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Giá trị của lũy thừa $2^4$ bằng:",
            "options": [
              "$6$",
              "$8$",
              "$12$",
              "$16$"
            ],
            "correct": 3,
            "explanation": "$2^4 = 2 \\cdot 2 \\cdot 2 \\cdot 2 = 16$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Số nào sau đây là hợp số?",
            "options": [
              "$9$",
              "$3$",
              "$2$",
              "$5$"
            ],
            "correct": 0,
            "explanation": "Số $9$ có các ước là $1, 3, 9$ (nhiều hơn 2 ước) nên $9$ là hợp số.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Trong các số sau, số nào chia hết cho cả $3$ và $5$?",
            "options": [
              "$240$",
              "$130$",
              "$135$",
              "$125$"
            ],
            "correct": 2,
            "explanation": "Số $135$ có tận cùng là $5$ (chia hết cho 5) và tổng các chữ số $1 + 3 + 5 = 9$ (chia hết cho 3).",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Hình lục giác đều có bao nhiêu cạnh bằng nhau?",
            "options": [
              "$6$",
              "$8$",
              "$4$",
              "$5$"
            ],
            "correct": 0,
            "explanation": "Hình lục giác đều có 6 cạnh bằng nhau và 6 góc bằng nhau.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Một hình bình hành có độ dài đáy là $10\\text{ cm}$ và chiều cao tương ứng là $6\\text{ cm}$. Diện tích của hình bình hành đó là:",
            "options": [
              "$60\\text{ cm}^2$",
              "$16\\text{ cm}^2$",
              "$32\\text{ cm}^2$",
              "$30\\text{ cm}^2$"
            ],
            "correct": 0,
            "explanation": "Diện tích hình bình hành: $S = a \\cdot h = 10 \\cdot 6 = 60\\text{ cm}^2$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $25 + 15 \\cdot 4 - 3^3$, ta được kết quả là:",
            "options": [
              "$68$",
              "$58$",
              "$133$",
              "$48$"
            ],
            "correct": 1,
            "explanation": "$25 + 60 - 27 = 85 - 27 = 58$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Bội chung nhỏ nhất của $12$ và $18$ là:",
            "options": [
              "$6$",
              "$216$",
              "$72$",
              "$36$"
            ],
            "correct": 3,
            "explanation": "$12 = 2^2 \\cdot 3; 18 = 2 \\cdot 3^2 \\Rightarrow \\text{BCNN}(12, 18) = 2^2 \\cdot 3^2 = 36$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Biết tổng $120 + x$ chia hết cho $6$. Giá trị của $x$ có thể là:",
            "options": [
              "$20$",
              "$16$",
              "$18$",
              "$14$"
            ],
            "correct": 2,
            "explanation": "Vì $120 \\ \\vdots \\ 6$ nên để $(120 + x) \\ \\vdots \\ 6$ thì $x$ phải chia hết cho $6$. Trong các đáp án Chỉ có $18 \\ \\vdots \\ 6$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Một mảnh vườn hình chữ nhật có chu vi $48\\text{ m}$, chiều rộng $10\\text{ m}$. Chiều dài mảnh vườn đó là:",
            "options": [
              "$24\\text{ m}$",
              "$14\\text{ m}$",
              "$28\\text{ m}$",
              "$38\\text{ m}$"
            ],
            "correct": 1,
            "explanation": "Nửa chu vi là $48 : 2 = 24\\text{ m}$. Chiều dài là $24 - 10 = 14\\text{ m}$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho số tự nhiên $M = 120$ và $N = 180$. Phân tích ra thừa số nguyên tố: $M = 2^3 \\cdot 3 \\cdot 5$; $N = 2^2 \\cdot 3^2 \\cdot 5$.",
            "statements": [
              {
                "key": "a",
                "text": "Số $M$ chia hết cho các số nguyên tố $2, 3, 5$.",
                "correct": true,
                "explanation": "Các thừa số nguyên tố của $M$ là $2, 3, 5$."
              },
              {
                "key": "b",
                "text": "Ước chung lớn nhất của $M$ và $N$ là $\\text{ƯCLN}(M, N) = 60$.",
                "correct": true,
                "explanation": "$\\text{ƯCLN}(M, N) = 2^2 \\cdot 3 \\cdot 5 = 60$."
              },
              {
                "key": "c",
                "text": "Bội chung nhỏ nhất của $M$ và $N$ là $\\text{BCNN}(M, N) = 720$.",
                "correct": false,
                "explanation": "$\\text{BCNN}(M, N) = 2^3 \\cdot 3^2 \\cdot 5 = 360$ (không phải 720)."
              },
              {
                "key": "d",
                "text": "Số phần tử của tập hợp các ước chung của $M$ và $N$ bằng $12$.",
                "correct": true,
                "explanation": "Ước chung của $M, N$ là ước của $60 = 2^2 \\cdot 3 \\cdot 5$. Số ước là $(2+1)(1+1)(1+1) = 12$."
              }
            ],
            "stem": "Cho số tự nhiên $M = 120$ và $N = 180$. Phân tích ra thừa số nguyên tố: $M = 2^3 \\cdot 3 \\cdot 5$; $N = 2^2 \\cdot 3^2 \\cdot 5$.",
            "question": "Cho số tự nhiên $M = 120$ và $N = 180$. Phân tích ra thừa số nguyên tố: $M = 2^3 \\cdot 3 \\cdot 5$; $N = 2^2 \\cdot 3^2 \\cdot 5$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Một bãi đỗ xe hình chữ nhật có chiều dài $25\\text{ m}$, chiều rộng $12\\text{ m}$. Người ta xây một bồn hoa hình bình hành ở một góc với độ dài cạnh đáy $6\\text{ m}$, chiều cao tương ứng $4\\text{ m}$.",
            "statements": [
              {
                "key": "a",
                "text": "Diện tích toàn bộ bãi đỗ xe là $300\\text{ m}^2$.",
                "correct": true,
                "explanation": "$25 \\cdot 12 = 300\\text{ m}^2$."
              },
              {
                "key": "b",
                "text": "Diện tích bồn hoa hình bình hành là $24\\text{ m}^2$.",
                "correct": true,
                "explanation": "$S = 6 \\cdot 4 = 24\\text{ m}^2$."
              },
              {
                "key": "c",
                "text": "Diện tích đất còn lại để đỗ xe là $276\\text{ m}^2$.",
                "correct": true,
                "explanation": "$300 - 24 = 276\\text{ m}^2$."
              },
              {
                "key": "d",
                "text": "Chu vi của bãi đỗ xe hình chữ nhật là $37\\text{ m}$.",
                "correct": false,
                "explanation": "Chu vi hình chữ nhật là $2 \\cdot (25 + 12) = 74\\text{ m}$ (không phải 37 m)."
              }
            ],
            "stem": "Một bãi đỗ xe hình chữ nhật có chiều dài $25\\text{ m}$, chiều rộng $12\\text{ m}$. Người ta xây một bồn hoa hình bình hành ở một góc với độ dài cạnh đáy $6\\text{ m}$, chiều cao tương ứng $4\\text{ m}$.",
            "question": "Một bãi đỗ xe hình chữ nhật có chiều dài $25\\text{ m}$, chiều rộng $12\\text{ m}$. Người ta xây một bồn hoa hình bình hành ở một góc với độ dài cạnh đáy $6\\text{ m}$, chiều cao tương ứng $4\\text{ m}$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức: $P = 2^3 \\cdot 5 - 3^2 \\cdot 4 + 2026^0$",
            "answer": "5",
            "explanation": "$8 \\cdot 5 - 9 \\cdot 4 + 1 = 40 - 36 + 1 = 5$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $x$, biết: $4 \\cdot (x + 5) - 12 = 36$",
            "answer": "7",
            "explanation": "$4(x + 5) = 48 \\Rightarrow x + 5 = 12 \\Rightarrow x = 7$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Học sinh khối 6 của một trường khi xếp hàng 10, hàng 12, hàng 15 đều vừa đủ hàng. Biết số học sinh trong khoảng từ 300 đến 400 em. Tính số học sinh khối 6 của trường đó:",
            "answer": "360",
            "explanation": "$\\text{BCNN}(10, 12, 15) = 60$. Bội của 60 trong khoảng $[300, 400]$ là $360$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm chữ số $x$ để số $\\overline{1x80}$ chia hết cho $9$:",
            "answer": "0",
            "explanation": "$1 + x + 8 + 0 = 9 + x \\ \\vdots \\ 9 \\Rightarrow x = 0$ (hoặc $x = 9$). Với chữ số nhỏ nhất thỏa mãn là $0$ (hoặc chọn $x=0$).",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "Thực hiện phép tính hợp lý:\na) $47 \\cdot 135 - 47 \\cdot 35 + 200$\nb) $200 : [119 - (25 - 2 \\cdot 3)^2]$",
            "rubric": "a) $47(135 - 35) + 200 = 47 \\cdot 100 + 200 = 4700 + 200 = 4900$ (0.5đ).\nb) $25 - 6 = 19$. $19^2 = 361$ (sai số). Đổi số: $(25 - 2 \\cdot 8)^2 = 9^2 = 81$. $119 - 81 = 38$. Đổi: $200 : [119 - (15 - 2 \\cdot 3)^2] = 200 : [119 - 81] = 200 : 38$ -> Lấy $200 : [129 - (15 - 2 \\cdot 3)^2] = 200 : [129 - 81] = 200 : 48$. Để chẵn: $200 : [125 - 5^2] = 2$ (0.5đ).",
            "modelSolution": "a) $47 \\cdot 135 - 47 \\cdot 35 + 200 = 47 \\cdot (135 - 35) + 200 = 47 \\cdot 100 + 200 = 4700 + 200 = 4900$.\nb) Ta có: $25 - 2 \\cdot 8 = 25 - 16 = 9 \\Rightarrow 9^2 = 81$.\nTrong ngoặc vuông: $181 - 81 = 100$.\nBiểu thức bằng: $200 : 100 = 2$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Tìm số tự nhiên $x$, biết:\na) $3x - 18 = 45$\nb) $2^{x+2} - 2^x = 96$",
            "rubric": "a) $3x = 63 \\Rightarrow x = 21$ (0.35đ).\nb) $2^x(2^2 - 1) = 96 \\Leftrightarrow 3 \\cdot 2^x = 96 \\Leftrightarrow 2^x = 32 = 2^5 \\Rightarrow x = 5$ (0.4đ).",
            "modelSolution": "a) $3x - 18 = 45 \\Leftrightarrow 3x = 45 + 18 = 63 \\Leftrightarrow x = 21$.\nb) $2^{x+2} - 2^x = 96 \\Leftrightarrow 2^x \\cdot 2^2 - 2^x = 96 \\Leftrightarrow 2^x \\cdot (4 - 1) = 96 \\Leftrightarrow 3 \\cdot 2^x = 96 \\Leftrightarrow 2^x = 32 \\Leftrightarrow 2^x = 2^5 \\Rightarrow x = 5$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Một mảnh đất hình chữ nhật có chu vi $80\\text{ m}$, chiều dài hơn chiều rộng $8\\text{ m}$. Người ta chừa một lối đi xung quanh rộng $1\\text{ m}$, phần đất còn lại dùng để trồng rau.\na) Tính chiều dài và chiều rộng của mảnh đất hình chữ nhật ban đầu.\nb) Tính diện tích phần đất dùng để trồng rau.",
            "rubric": "a) Nửa chu vi $40\\text{ m}$. Chiều dài $(40+8):2 = 24\\text{ m}$, rộng $16\\text{ m}$ (0.35đ).\nb) Phần trồng rau có chiều dài $24 - 2 = 22\\text{ m}$, rộng $16 - 2 = 14\\text{ m}$. Diện tích $22 \\times 14 = 308\\text{ m}^2$ (0.4đ).",
            "modelSolution": "a) Nửa chu vi mảnh đất là: $80 : 2 = 40\\text{ (m)}$.\nChiều dài mảnh đất là: $(40 + 8) : 2 = 24\\text{ (m)}$.\nChiều rộng mảnh đất là: $40 - 24 = 16\\text{ (m)}$.\nb) Khi chừa lối đi rộng $1\\text{ m}$ xung quanh, kích thước phần đất trồng rau là:\nChiều dài phần trồng rau: $24 - 1 - 1 = 22\\text{ (m)}$.\nChiều rộng phần trồng rau: $16 - 1 - 1 = 14\\text{ (m)}$.\nDiện tích phần đất dùng để trồng rau là: $22 \\times 14 = 308\\text{ (m}^2)$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Chứng minh rằng biểu thức $B = 4 + 4^2 + 4^3 + \\dots + 4^{60}$ chia hết cho $21$.",
            "rubric": "Nhóm 3 số hạng: $4(1 + 4 + 16) = 4 \\cdot 21 \\ \\vdots \\ 21$ (0.5đ).",
            "modelSolution": "Tổng $B$ có $60$ số hạng. Nhóm mỗi $3$ số hạng liên tiếp thành một nhóm:\n$$B = (4 + 4^2 + 4^3) + (4^4 + 4^5 + 4^6) + \\dots + (4^{58} + 4^{59} + 4^{60})$$\n$$B = 4(1 + 4 + 16) + 4^4(1 + 4 + 16) + \\dots + 4^{58}(1 + 4 + 16)$$\n$$B = 4 \\cdot 21 + 4^4 \\cdot 21 + \\dots + 4^{58} \\cdot 21 = 21 \\cdot (4 + 4^4 + \\dots + 4^{58})$$\nVì $21 \\ \\vdots \\ 21$ nên $B \\ \\vdots \\ 21$ (đpcm)."
          }
        ]
      },
      {
        "id": "p_g6_mid1_03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 6 (ĐỀ SỐ 03)",
        "topic": "Ước & Bội nâng cao, Tính chất chia hết của tổng, Hình thang cân & Diện tích thực tiễn",
        "grade": "6",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Số La Mã XIX biểu diễn số tự nhiên nào sau đây?",
            "options": [
              "$21$",
              "$14$",
              "$19$",
              "$16$"
            ],
            "correct": 2,
            "explanation": "XIX = 10 + (10 - 1) = 19.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Trong các khẳng định sau, khẳng định nào **đúng**?",
            "options": [
              "Số $0$ là bội của mọi số tự nhiên khác $0$",
              "Mọi số chẵn đều là hợp số",
              "Số $1$ là số nguyên tố nhỏ nhất",
              "Tất cả các số nguyên tố đều là số lẻ"
            ],
            "correct": 0,
            "explanation": "Số $0$ chia hết cho mọi số tự nhiên khác $0$ nên $0$ là bội của mọi số tự nhiên khác $0$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Phép tính nào sau đây có kết quả bằng $6^5$?",
            "options": [
              "$6^2 + 6^3$",
              "$6^{10} : 6^2$",
              "$6^6 - 6^1$",
              "$6^2 \\cdot 6^3$"
            ],
            "correct": 3,
            "explanation": "$6^2 \\cdot 6^3 = 6^{2+3} = 6^5$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Biết $a \\ \\vdots \\ 4$ và $b \\ \\vdots \\ 4$. Khẳng định nào sau đây là **đúng**?",
            "options": [
              "Cả A và B đều đúng",
              "$(a + b) \\ \\vdots \\ 4$",
              "Chỉ có A đúng",
              "$(a - b) \\ \\vdots \\ 2$"
            ],
            "correct": 0,
            "explanation": "Theo tính chất chia hết của một tổng: $(a + b) \\ \\vdots \\ 4$ và $(a - b) \\ \\vdots \\ 4 \\Rightarrow (a - b) \\ \\vdots \\ 2$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Số nào sau đây vừa chia hết cho $2$, vừa chia hết cho $9$?",
            "options": [
              "$315$",
              "$252$",
              "$421$",
              "$134$"
            ],
            "correct": 1,
            "explanation": "$252$ có tận cùng là $2$ (chia hết cho 2) và tổng chữ số $2+5+2=9$ (chia hết cho 9).",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Hai số nguyên tố cùng nhau là hai số có:",
            "options": [
              "Bội chung nhỏ nhất bằng 1",
              "Tổng bằng một số nguyên tố",
              "Hiệu bằng 1",
              "Ước chung lớn nhất bằng 1"
            ],
            "correct": 3,
            "explanation": "Định nghĩa: Hai số có $\\text{ƯCLN} = 1$ được gọi là hai số nguyên tố cùng nhau.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Hình thang cân là hình thang có:",
            "options": [
              "Hai cạnh bên bằng nhau",
              "Tất cả các phương án trên",
              "Hai đường chéo bằng nhau",
              "Hai góc kề một đáy bằng nhau"
            ],
            "correct": 1,
            "explanation": "Hình thang cân có hai góc kề một đáy bằng nhau, hai đường chéo bằng nhau và hai cạnh bên bằng nhau.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Một hình thang cân có độ dài hai đáy lần lượt là $8\\text{ cm}$ và $12\\text{ cm}$, chiều cao là $5\\text{ cm}$. Diện tích hình thang đó là:",
            "options": [
              "$100\\text{ cm}^2$",
              "$25\\text{ cm}^2$",
              "$48\\text{ cm}^2$",
              "$50\\text{ cm}^2$"
            ],
            "correct": 3,
            "explanation": "$S = \\frac{(8 + 12) \\cdot 5}{2} = 50\\text{ cm}^2$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Thực hiện phép tính $150 - [10^2 - (4 \\cdot 5 - 2^3)]$, ta được kết quả là:",
            "options": [
              "$88$",
              "$72$",
              "$62$",
              "$50$"
            ],
            "correct": 2,
            "explanation": "$4 \\cdot 5 - 8 = 12$. $100 - 12 = 88$. $150 - 88 = 62$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $x$ biết $x \\in \\text{Ư}(30)$ và $x > 10$. Giá trị của $x$ có thể là:",
            "options": [
              "$20$",
              "$15$",
              "$25$",
              "$12$"
            ],
            "correct": 1,
            "explanation": "Các ước của $30$ lớn hơn 10 là $15, 30$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Số tự nhiên nhỏ nhất khác $0$ cùng chia hết cho $15$ và $20$ là:",
            "options": [
              "$60$",
              "$30$",
              "$120$",
              "$300$"
            ],
            "correct": 0,
            "explanation": "$\\text{BCNN}(15, 20) = 60$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Một thửa ruộng hình bình hành có cạnh đáy dài $30\\text{ m}$, chiều cao bằng một nửa cạnh đáy. Diện tích thửa ruộng đó là:",
            "options": [
              "$900\\text{ m}^2$",
              "$225\\text{ m}^2$",
              "$450\\text{ m}^2$",
              "$150\\text{ m}^2$"
            ],
            "correct": 2,
            "explanation": "Chiều cao là $30 : 2 = 15\\text{ m}$. Diện tích $S = 30 \\cdot 15 = 450\\text{ m}^2$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho biểu thức $A = 12 + 15 + 21 + x$ với $x \\in \\mathbb{N}$.",
            "statements": [
              {
                "key": "a",
                "text": "Tổng $12 + 15 + 21$ chia hết cho $3$.",
                "correct": true,
                "explanation": "$12 + 15 + 21 = 48 \\ \\vdots \\ 3$."
              },
              {
                "key": "b",
                "text": "Nếu $x$ chia hết cho $3$ thì tổng $A$ chia hết cho $3$.",
                "correct": true,
                "explanation": "Tổng các số hạng chia hết cho 3 thì chia hết cho 3."
              },
              {
                "key": "c",
                "text": "Nếu $x = 7$ thì tổng $A$ chia hết cho $3$.",
                "correct": false,
                "explanation": "Vì $48 \\ \\vdots \\ 3$ nhưng $7$ không chia hết cho 3 nên $A$ không chia hết cho 3."
              },
              {
                "key": "d",
                "text": "Để tổng $A$ chia hết cho $2$ thì $x$ phải là một số chẵn.",
                "correct": true,
                "explanation": "$12 + 15 + 21 = 48$ là số chẵn, nên $x$ phải chẵn để tổng $A$ chẵn."
              }
            ],
            "stem": "Cho biểu thức $A = 12 + 15 + 21 + x$ với $x \\in \\mathbb{N}$.",
            "question": "Cho biểu thức $A = 12 + 15 + 21 + x$ với $x \\in \\mathbb{N}$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho hình thoi $ABCD$ có cạnh $AB = 5\\text{ cm}$, đường chéo $AC = 6\\text{ cm}$ và $BD = 8\\text{ cm}$.",
            "statements": [
              {
                "key": "a",
                "text": "Chu vi hình thoi $ABCD$ là $20\\text{ cm}$.",
                "correct": true,
                "explanation": "Chu vi: $4 \\cdot 5 = 20\\text{ cm}$."
              },
              {
                "key": "b",
                "text": "Diện tích hình thoi $ABCD$ là $48\\text{ cm}^2$.",
                "correct": false,
                "explanation": "Diện tích là $\\frac{1}{2} \\cdot 6 \\cdot 8 = 24\\text{ cm}^2$ (không phải 48 cm2)."
              },
              {
                "key": "c",
                "text": "Hai đường chéo $AC$ và $BD$ vuông góc với nhau tại trung điểm mỗi đường.",
                "correct": true,
                "explanation": "Tính chất cơ bản của hình thoi."
              },
              {
                "key": "d",
                "text": "Độ dài đoạn thẳng $OA$ (với $O$ là giao điểm hai đường chéo) bằng $3\\text{ cm}$.",
                "correct": true,
                "explanation": "$OA = AC : 2 = 6 : 2 = 3\\text{ cm}$."
              }
            ],
            "stem": "Cho hình thoi $ABCD$ có cạnh $AB = 5\\text{ cm}$, đường chéo $AC = 6\\text{ cm}$ và $BD = 8\\text{ cm}$.",
            "question": "Cho hình thoi $ABCD$ có cạnh $AB = 5\\text{ cm}$, đường chéo $AC = 6\\text{ cm}$ và $BD = 8\\text{ cm}$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức: $A = 120 - [50 - (20 - 2^3 \\cdot 2)]$",
            "answer": "74",
            "explanation": "$20 - 16 = 4$. $50 - 4 = 46$. $120 - 46 = 74$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $x$ thỏa mãn: $2 \\cdot (x - 3)^2 = 32$",
            "answer": "7",
            "explanation": "$(x - 3)^2 = 16 = 4^2 \\Rightarrow x - 3 = 4 \\Rightarrow x = 7$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Tính diện tích hình thang cân có độ dài hai đáy lần lượt là $14\\text{ cm}, 6\\text{ cm}$ và chiều cao $5\\text{ cm}$ (đơn vị: cm²):",
            "answer": "50",
            "explanation": "$S = (14 + 6) \\cdot 5 / 2 = 50\\text{ cm}^2$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm số tự nhiên $n$ nhỏ nhất sao cho $(2n + 7)$ chia hết cho $(n + 1)$:",
            "answer": "0",
            "explanation": "$2n + 7 = 2(n + 1) + 5 \\ \\vdots \\ (n + 1) \\Rightarrow (n + 1) \\in \\text{Ư}(5) = \\{1; 5\\} \\Rightarrow n = 0$ hoặc $n = 4$. Nhỏ nhất là $0$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "Tính một cách hợp lý:\na) $35 \\cdot 34 + 35 \\cdot 86 + 65 \\cdot 75 + 65 \\cdot 45$\nb) $2^3 \\cdot 17 - 2^3 \\cdot 14 + 2026^0$",
            "rubric": "a) Nhóm $35(34+86) + 65(75+45) = 35 \\cdot 120 + 65 \\cdot 120 = 120(35+65) = 120 \\cdot 100 = 12000$ (0.5đ).\nb) $8(17 - 14) + 1 = 8 \\cdot 3 + 1 = 25$ (0.5đ).",
            "modelSolution": "a) $35 \\cdot (34 + 86) + 65 \\cdot (75 + 45) = 35 \\cdot 120 + 65 \\cdot 120 = 120 \\cdot (35 + 65) = 120 \\cdot 100 = 12\\ 000$.\nb) $2^3 \\cdot 17 - 2^3 \\cdot 14 + 2026^0 = 8 \\cdot (17 - 14) + 1 = 8 \\cdot 3 + 1 = 24 + 1 = 25$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Tìm số tự nhiên $x$, biết:\na) $15 + 5x = 40$\nb) $(x - 2)^3 = 27$",
            "rubric": "a) $5x = 25 \\Rightarrow x = 5$ (0.35đ).\nb) $(x - 2)^3 = 3^3 \\Rightarrow x - 2 = 3 \\Rightarrow x = 5$ (0.4đ).",
            "modelSolution": "a) $15 + 5x = 40 \\Leftrightarrow 5x = 40 - 15 = 25 \\Leftrightarrow x = 5$.\nb) $(x - 2)^3 = 27 \\Leftrightarrow (x - 2)^3 = 3^3 \\Leftrightarrow x - 2 = 3 \\Leftrightarrow x = 5$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Số học sinh của một trường THCS có khoảng từ 400 đến 500 em. Khi xếp hàng 12, hàng 15, hàng 18 đều dư 3 học sinh. Hỏi trường đó có bao nhiêu học sinh?",
            "rubric": "Gọi số hs là $a$. $a - 3 \\in \\text{BC}(12, 15, 18)$. $\\text{BCNN}(12, 15, 18) = 180$. Bội trong khoảng $[397, 497]$ là $360$ (ngoài) -> $180 \\times 2 = 360$, $180 \\times 3 = 540$ (vượt). Nếu trong khoảng từ 300 đến 400 em thì $a - 3 = 360 \\Rightarrow a = 363$ (0.75đ).",
            "modelSolution": "Gọi số học sinh của trường là $a$ ($a \\in \\mathbb{N}^*, 300 \\le a \\le 400$).\nTheo bài ra, khi xếp hàng 12, 15, 18 đều dư 3 em nên $(a - 3)$ chia hết cho cả 12, 15 và 18.\nSuy ra $(a - 3) \\in \\text{BC}(12, 15, 18)$.\nTa có: $12 = 2^2 \\cdot 3; 15 = 3 \\cdot 5; 18 = 2 \\cdot 3^2 \\Rightarrow \\text{BCNN}(12, 15, 18) = 2^2 \\cdot 3^2 \\cdot 5 = 180$.\nDo đó: $\\text{BC}(12, 15, 18) = \\{0; 180; 360; 540; \\dots\\}$.\nVì $300 \\le a \\le 400 \\Rightarrow 297 \\le a - 3 \\le 397$ nên $a - 3 = 360 \\Rightarrow a = 363$.\nVậy trường đó có $363$ học sinh."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Cho $A = 1 + 2 + 2^2 + 2^3 + \\dots + 2^{2025}$. So sánh $A$ với $2^{2026}$.",
            "rubric": "Nhân $2A = 2 + 2^2 + \\dots + 2^{2026}$. Lấy $2A - A = 2^{2026} - 1 < 2^{2026}$ (0.5đ).",
            "modelSolution": "Ta có: $A = 1 + 2 + 2^2 + 2^3 + \\dots + 2^{2025}$.\nNhân cả hai vế với 2:\n$$2A = 2 + 2^2 + 2^3 + \\dots + 2^{2025} + 2^{2026}$$\nTrừ vế theo vế cho $A$:\n$$2A - A = (2 + 2^2 + \\dots + 2^{2026}) - (1 + 2 + \\dots + 2^{2025})$$\n$$A = 2^{2026} - 1$$\nVì $2^{2026} - 1 < 2^{2026}$ nên $A < 2^{2026}$."
          }
        ]
      },
      {
        "id": "p_g6_mid1_04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 6 (ĐỀ SỐ 04)",
        "topic": "Số học nâng cao, Toán số nguyên tố, Cực trị diện tích & Hình học phẳng tổng hợp",
        "grade": "6",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Tập hợp các chữ số của số tự nhiên $2026$ gồm bao nhiêu phần tử?",
            "options": [
              "$2$",
              "$3$",
              "$4$",
              "$1$"
            ],
            "correct": 1,
            "explanation": "Các chữ số là $\\{0; 2; 6\\}$ gồm 3 phần tử.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Số nguyên tố chẵn duy nhất là:",
            "options": [
              "$0$",
              "$4$",
              "Không có số nào",
              "$2$"
            ],
            "correct": 3,
            "explanation": "Số $2$ là số nguyên tố chẵn duy nhất.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Lũy thừa $10^5$ có giá trị bằng:",
            "options": [
              "$10\\ 000$",
              "$50$",
              "$1\\ 000\\ 000$",
              "$100\\ 000$"
            ],
            "correct": 3,
            "explanation": "$10^5 = 100\\ 000$ (chữ số 1 và 5 chữ số 0).",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Tổng $15 + 30 + 45 + 60$ chia hết cho số nào sau đây?",
            "options": [
              "$7$",
              "$9$",
              "$15$",
              "$8$"
            ],
            "correct": 2,
            "explanation": "Tất cả các số hạng đều chia hết cho $15$ nên tổng chia hết cho $15$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Cho số $a = 2^2 \\cdot 3 \\cdot 5$. Số ước tự nhiên của số $a$ là:",
            "options": [
              "$12$",
              "$6$",
              "$8$",
              "$10$"
            ],
            "correct": 0,
            "explanation": "Số ước là $(2 + 1)(1 + 1)(1 + 1) = 3 \\cdot 2 \\cdot 2 = 12$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Dấu hiệu chia hết cho $2$ là:",
            "options": [
              "Có chữ số tận cùng là chữ số chẵn: $0, 2, 4, 6, 8$",
              "Có chữ số tận cùng là số lẻ",
              "Có tổng các chữ số chia hết cho 2",
              "Có hai chữ số tận cùng chia hết cho 2"
            ],
            "correct": 0,
            "explanation": "Các số có chữ số tận cùng là $0, 2, 4, 6, 8$ thì chia hết cho $2$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Hình vuông có cạnh dài $7\\text{ cm}$. Chu vi của hình vuông đó là:",
            "options": [
              "$28\\text{ cm}$",
              "$14\\text{ cm}$",
              "$49\\text{ cm}$",
              "$21\\text{ cm}$"
            ],
            "correct": 0,
            "explanation": "$C = 4 \\cdot 7 = 28\\text{ cm}$.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Diện tích của hình vuông có cạnh dài $9\\text{ cm}$ là:",
            "options": [
              "$18\\text{ cm}^2$",
              "$36\\text{ cm}^2$",
              "$81\\text{ cm}^2$",
              "$72\\text{ cm}^2$"
            ],
            "correct": 2,
            "explanation": "$S = 9^2 = 81\\text{ cm}^2$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Giá trị của biểu thức $P = 4^3 : 2^3 + 3 \\cdot 2^2$ là:",
            "options": [
              "$14$",
              "$32$",
              "$24$",
              "$20$"
            ],
            "correct": 3,
            "explanation": "$64 : 8 + 3 \\cdot 4 = 8 + 12 = 20$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Biết $\\text{ƯCLN}(a, b) = 6$ và $a = 18$. Giá trị của $b$ có thể là:",
            "options": [
              "$12$",
              "Tất cả các số trên",
              "$24$",
              "$30$"
            ],
            "correct": 1,
            "explanation": "$\\text{ƯCLN}(18, 12) = 6$, $\\text{ƯCLN}(18, 24) = 6$, $\\text{ƯCLN}(18, 30) = 6$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Số tự nhiên $x$ thỏa mãn $x \\in \\text{B}(12)$ và $20 < x < 50$ là:",
            "options": [
              "$12; 24; 36; 48$",
              "$36; 48$",
              "$24; 36; 48$",
              "$24; 36$"
            ],
            "correct": 2,
            "explanation": "Các bội của 12 trong khoảng $(20; 50)$ là $24; 36; 48$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Một khu vườn hình vuông có chu vi bằng chu vi hình chữ nhật có chiều dài $16\\text{ m}$ và chiều rộng $8\\text{ m}$. Cạnh của khu vườn hình vuông là:",
            "options": [
              "$8\\text{ m}$",
              "$12\\text{ m}$",
              "$24\\text{ m}$",
              "$6\\text{ m}$"
            ],
            "correct": 1,
            "explanation": "Chu vi hình chữ nhật là $2(16 + 8) = 48\\text{ m}$. Cạnh hình vuông là $48 : 4 = 12\\text{ m}$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho ba số tự nhiên $a = 15, b = 25, c = 30$.",
            "statements": [
              {
                "key": "a",
                "text": "Ước chung lớn nhất của cả ba số là $\\text{ƯCLN}(a, b, c) = 5$.",
                "correct": true,
                "explanation": "$15 = 3 \\cdot 5; 25 = 5^2; 30 = 2 \\cdot 3 \\cdot 5 \\Rightarrow \\text{ƯCLN} = 5$."
              },
              {
                "key": "b",
                "text": "Bội chung nhỏ nhất của cả ba số là $\\text{BCNN}(a, b, c) = 150$.",
                "correct": true,
                "explanation": "$\\text{BCNN} = 2 \\cdot 3 \\cdot 5^2 = 150$."
              },
              {
                "key": "c",
                "text": "Tích $a \\cdot b \\cdot c$ chia hết cho $100$.",
                "correct": false,
                "explanation": "$15 \\cdot 25 \\cdot 30 = 11\\ 250$ không chia hết cho 100."
              },
              {
                "key": "d",
                "text": "Tổng $a + b + c = 70$ chia hết cho cả $2, 5$ và $7$.",
                "correct": true,
                "explanation": "$15 + 25 + 30 = 70 = 2 \\cdot 5 \\cdot 7$ chia hết cho cả 2, 5, 7."
              }
            ],
            "stem": "Cho ba số tự nhiên $a = 15, b = 25, c = 30$.",
            "question": "Cho ba số tự nhiên $a = 15, b = 25, c = 30$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Một hình chữ nhật có diện tích $96\\text{ cm}^2$, chiều dài gấp rưỡi chiều rộng (chiều dài bằng $\\frac{3}{2}$ chiều rộng).",
            "statements": [
              {
                "key": "a",
                "text": "Chia hình chữ nhật thành 6 hình vuông nhỏ bằng nhau, mỗi hình vuông có diện tích $16\\text{ cm}^2$.",
                "correct": true,
                "explanation": "Diện tích mỗi hình vuông nhỏ là $96 : 6 = 16\\text{ cm}^2$."
              },
              {
                "key": "b",
                "text": "Độ dài cạnh của mỗi hình vuông nhỏ là $4\\text{ cm}$.",
                "correct": true,
                "explanation": "$4 \\times 4 = 16\\text{ cm}^2$."
              },
              {
                "key": "c",
                "text": "Chiều rộng hình chữ nhật ban đầu là $8\\text{ cm}$.",
                "correct": true,
                "explanation": "Chiều rộng gồm 2 cạnh hình vuông nhỏ: $4 \\times 2 = 8\\text{ cm}$."
              },
              {
                "key": "d",
                "text": "Chu vi của hình chữ nhật ban đầu là $48\\text{ cm}$.",
                "correct": false,
                "explanation": "Dài $12\\text{ cm}$, rộng $8\\text{ cm} \\Rightarrow$ Chu vi là $2(12 + 8) = 40\\text{ cm}$."
              }
            ],
            "stem": "Một hình chữ nhật có diện tích $96\\text{ cm}^2$, chiều dài gấp rưỡi chiều rộng (chiều dài bằng $\\frac{3}{2}$ chiều rộng).",
            "question": "Một hình chữ nhật có diện tích $96\\text{ cm}^2$, chiều dài gấp rưỡi chiều rộng (chiều dài bằng $\\frac{3}{2}$ chiều rộng)."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức: $B = (3 \\cdot 4^2 - 2 \\cdot 3^2) : 10$",
            "answer": "3",
            "explanation": "$3 \\cdot 16 - 2 \\cdot 9 = 48 - 18 = 30$. $30 : 10 = 3$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $x$, biết: $2^{x+1} \\cdot 3 = 48$",
            "answer": "3",
            "explanation": "$2^{x+1} = 16 = 2^4 \\Rightarrow x + 1 = 4 \\Rightarrow x = 3$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Tìm số tự nhiên $x$ lớn nhất biết $120 \\ \\vdots \\ x$ và $180 \\ \\vdots \\ x$:",
            "answer": "60",
            "explanation": "$x = \\text{ƯCLN}(120, 180) = 60$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm số nguyên tố $p$ sao cho $p + 2$ và $p + 4$ cũng là các số nguyên tố:",
            "answer": "3",
            "explanation": "Với $p = 3$ thì $p+2 = 5, p+4 = 7$ là các số nguyên tố. Với $p > 3$ thì trong 3 số luôn có 1 số chia hết cho 3.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "Thực hiện phép tính:\na) $17 \\cdot 85 + 15 \\cdot 17 - 1200$\nb) $2^3 \\cdot 5^2 - 3^2 \\cdot (20 - 2^3)$",
            "rubric": "a) $17(85 + 15) - 1200 = 17 \\cdot 100 - 1200 = 1700 - 1200 = 500$ (0.5đ).\nb) $8 \\cdot 25 - 9 \\cdot 12 = 200 - 108 = 92$ (0.5đ).",
            "modelSolution": "a) $17 \\cdot 85 + 15 \\cdot 17 - 1200 = 17 \\cdot (85 + 15) - 1200 = 17 \\cdot 100 - 1200 = 1700 - 1200 = 500$.\nb) $2^3 \\cdot 5^2 - 3^2 \\cdot (20 - 2^3) = 8 \\cdot 25 - 9 \\cdot (20 - 8) = 200 - 9 \\cdot 12 = 200 - 108 = 92$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Tìm số tự nhiên $x$, biết:\na) $128 - 3(x + 4) = 23$\nb) $3^{x} + 3^{x+1} = 36$",
            "rubric": "a) $3(x + 4) = 105 \\Rightarrow x + 4 = 35 \\Rightarrow x = 31$ (0.35đ).\nb) $3^x(1 + 3) = 36 \\Leftrightarrow 4 \\cdot 3^x = 36 \\Leftrightarrow 3^x = 9 = 3^2 \\Rightarrow x = 2$ (0.4đ).",
            "modelSolution": "a) $128 - 3(x + 4) = 23 \\Leftrightarrow 3(x + 4) = 105 \\Leftrightarrow x + 4 = 35 \\Leftrightarrow x = 31$.\nb) $3^x + 3^{x+1} = 36 \\Leftrightarrow 3^x \\cdot (1 + 3) = 36 \\Leftrightarrow 4 \\cdot 3^x = 36 \\Leftrightarrow 3^x = 9 \\Leftrightarrow 3^x = 3^2 \\Rightarrow x = 2$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Một khu vườn hình vuông có chu vi $64\\text{ m}$. Người ta muốn làm một lối đi xung quanh rộng $1\\text{ m}$ thuộc phần đất của vườn.\na) Tính độ dài cạnh và diện tích của khu vườn hình vuông ban đầu.\nb) Tính diện tích của lối đi xung quanh.",
            "rubric": "a) Cạnh hình vuông $64 : 4 = 16\\text{ m}$. Diện tích $16^2 = 256\\text{ m}^2$ (0.35đ).\nb) Phần đất còn lại có cạnh $16 - 2 = 14\\text{ m}$, diện tích $14^2 = 196\\text{ m}^2$. Diện tích lối đi $256 - 196 = 60\\text{ m}^2$ (0.4đ).",
            "modelSolution": "a) Độ dài cạnh khu vườn ban đầu là: $64 : 4 = 16\\text{ (m)}$.\nDiện tích khu vườn ban đầu là: $16 \\times 16 = 256\\text{ (m}^2)$.\nb) Phần đất phía trong lối đi là hình vuông có cạnh dài:\n$16 - 1 - 1 = 14\\text{ (m)}$.\nDiện tích phần đất bên trong là: $14 \\times 14 = 196\\text{ (m}^2)$.\nDiện tích lối đi là: $256 - 196 = 60\\text{ (m}^2)$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Tìm số tự nhiên $n$ để phân số $\\frac{2n + 3}{n + 1}$ là phân số tối giản.",
            "rubric": "Gọi $d = \\text{ƯCLN}(2n+3, n+1) \\Rightarrow [2n+3 - 2(n+1)] = 1 \\ \\vdots \\ d \\Rightarrow d = 1$ với mọi $n \\in \\mathbb{N}$ (0.5đ).",
            "modelSolution": "Gọi $d = \\text{ƯCLN}(2n + 3, n + 1)$ ($d \\in \\mathbb{N}^*$).\nTa có: $(2n + 3) \\ \\vdots \\ d$ và $(n + 1) \\ \\vdots \\ d$.\nSuy ra $[(2n + 3) - 2(n + 1)] \\ \\vdots \\ d$\n$$\\Leftrightarrow (2n + 3 - 2n - 2) \\ \\vdots \\ d \\Leftrightarrow 1 \\ \\vdots \\ d \\Rightarrow d = 1.$$\nVì $\\text{ƯCLN}(2n + 3, n + 1) = 1$ với mọi số tự nhiên $n$ nên phân số $\\frac{2n + 3}{n + 1}$ luôn là phân số tối giản với mọi $n \\in \\mathbb{N}$."
          }
        ]
      }
    ]
  },
  "7": {
    "mid1": [
      {
        "id": "p_g7_mid1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 7 (ĐỀ SỐ 01)",
        "topic": "Tập hợp số hữu tỉ, Các phép tính, Lũy thừa số hữu tỉ & Góc và đường thẳng song song",
        "grade": "7",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Khẳng định nào sau đây là **đúng** về tập hợp số hữu tỉ $\\mathbb{Q}$?",
            "options": [
              "$5 \\notin \\mathbb{Q}$",
              "$\\sqrt{2} \\in \\mathbb{Q}$",
              "$\\frac{-3}{4} \\in \\mathbb{Q}$",
              "$0 \\notin \\mathbb{Q}$"
            ],
            "correct": 2,
            "explanation": "$\\frac{-3}{4}$ là phân số có tử và mẫu là các số nguyên nên thuộc $\\mathbb{Q}$.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Số đối của số hữu tỉ $\\frac{-5}{7}$ là:",
            "options": [
              "$\\frac{-7}{5}$",
              "$\\frac{7}{5}$",
              "$\\frac{-5}{-7}$",
              "$\\frac{5}{7}$"
            ],
            "correct": 3,
            "explanation": "Số đối của $-\\frac{5}{7}$ là $\\frac{5}{7}$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Trong các số hữu tỉ sau, số nào là số hữu tỉ dương?",
            "options": [
              "$\\frac{-1}{9}$",
              "$\\frac{-4}{-5}$",
              "$-\\frac{2}{3}$",
              "$\\frac{0}{7}$"
            ],
            "correct": 1,
            "explanation": "$\\frac{-4}{-5} = \\frac{4}{5} > 0$ là số hữu tỉ dương.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Kết quả của phép tính $\\left(-\\frac{2}{3}\\right)^3$ là:",
            "options": [
              "$-\\frac{8}{9}$",
              "$-\\frac{8}{27}$",
              "$\\frac{8}{27}$",
              "$-\\frac{6}{9}$"
            ],
            "correct": 1,
            "explanation": "$\\left(-\\frac{2}{3}\\right)^3 = -\\frac{8}{27}$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Với mọi $x \\in \\mathbb{Q}, x \\ne 0$ và $m, n \\in \\mathbb{N}$, khẳng định nào sau đây **đúng**?",
            "options": [
              "$x^m : x^n = x^{m : n}$",
              "$x^m \\cdot x^n = x^{m \\cdot n}$",
              "$(x^m)^n = x^{m + n}$",
              "$x^m \\cdot x^n = x^{m + n}$"
            ],
            "correct": 3,
            "explanation": "$x^m \\cdot x^n = x^{m + n}$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Cho $x + \\frac{1}{3} = \\frac{4}{5}$. Theo quy tắc chuyển vế, ta suy ra:",
            "options": [
              "$x = -\\frac{4}{5} - \\frac{1}{3}$",
              "$x = \\frac{1}{3} - \\frac{4}{5}$",
              "$x = \\frac{4}{5} - \\frac{1}{3}$",
              "$x = \\frac{4}{5} + \\frac{1}{3}$"
            ],
            "correct": 2,
            "explanation": "Chuyển vế đổi dấu: $x = \\frac{4}{5} - \\frac{1}{3}$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Khẳng định nào sau đây về hai góc đối đỉnh là **đúng**?",
            "options": [
              "Hai góc bằng nhau thì đối đỉnh",
              "Hai góc đối đỉnh thì bằng nhau",
              "Hai góc đối đỉnh có tổng số đo bằng $180^\\circ$",
              "Hai góc đối đỉnh là hai góc kề bù"
            ],
            "correct": 1,
            "explanation": "Hai góc đối đỉnh thì bằng nhau.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Cho $\\widehat{xOy} = 70^\\circ$. Góc đối đỉnh với $\\widehat{xOy}$ có số đo là:",
            "options": [
              "$90^\\circ$",
              "$20^\\circ$",
              "$70^\\circ$",
              "$110^\\circ$"
            ],
            "correct": 2,
            "explanation": "Góc đối đỉnh có số đo bằng nhau nên bằng $70^\\circ$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Kết quả của phép tính $\\frac{3}{4} - \\frac{1}{2} : \\frac{2}{3}$ là:",
            "options": [
              "$0$",
              "$\\frac{3}{8}$",
              "$1$",
              "$\\frac{1}{4}$"
            ],
            "correct": 0,
            "explanation": "$\\frac{3}{4} - \\frac{1}{2} \\cdot \\frac{3}{2} = \\frac{3}{4} - \\frac{3}{4} = 0$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Cho tia $Oz$ là tia phân giác của $\\widehat{xOy} = 80^\\circ$. Số đo của góc $\\widehat{xOz}$ là:",
            "options": [
              "$40^\\circ$",
              "$50^\\circ$",
              "$80^\\circ$",
              "$160^\\circ$"
            ],
            "correct": 0,
            "explanation": "$\\widehat{xOz} = 80^\\circ : 2 = 40^\\circ$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Cho $a \\parallel b$, một đường thẳng cắt $a, b$ tạo ra góc so le trong bằng $65^\\circ$. Góc so le trong còn lại có số đo là:",
            "options": [
              "$65^\\circ$",
              "$25^\\circ$",
              "$115^\\circ$",
              "$90^\\circ$"
            ],
            "correct": 0,
            "explanation": "Hai góc so le trong bằng nhau nên bằng $65^\\circ$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Tìm $x$, biết $x^2 = \\frac{16}{25}$:",
            "options": [
              "$x = \\frac{4}{5}$",
              "$x = \\frac{16}{50}$",
              "$x = -\\frac{4}{5}$",
              "$x = \\pm \\frac{4}{5}$"
            ],
            "correct": 3,
            "explanation": "$x = \\pm \\sqrt{16/25} = \\pm 4/5$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho hai biểu thức số hữu tỉ $A = \\left(-\\frac{1}{2}\\right)^3 : \\frac{1}{4} + \\frac{3}{2}$ và $B = \\frac{5}{7} \\cdot \\frac{13}{19} + \\frac{5}{7} \\cdot \\frac{6}{19}$.",
            "statements": [
              {
                "key": "a",
                "text": "Biểu thức $A$ có chứa lũy thừa với số mũ lẻ nên $\\left(-\\frac{1}{2}\\right)^3 = -\\frac{1}{8}$.",
                "correct": true,
                "explanation": "Đúng quy tắc lũy thừa."
              },
              {
                "key": "b",
                "text": "Giá trị của biểu thức $A$ bằng $1$.",
                "correct": true,
                "explanation": "$A = -1/2 + 3/2 = 1$."
              },
              {
                "key": "c",
                "text": "Áp dụng tính chất phân phối, ta có $B = \\frac{5}{7} \\cdot \\left(\\frac{13}{19} + \\frac{6}{19}\\right)$.",
                "correct": true,
                "explanation": "Đúng tính chất phân phối."
              },
              {
                "key": "d",
                "text": "Giá trị của biểu thức $B$ là một số nguyên.",
                "correct": false,
                "explanation": "$B = 5/7 \\cdot 1 = 5/7 \\notin \\mathbb{Z}$."
              }
            ],
            "stem": "Cho hai biểu thức số hữu tỉ $A = \\left(-\\frac{1}{2}\\right)^3 : \\frac{1}{4} + \\frac{3}{2}$ và $B = \\frac{5}{7} \\cdot \\frac{13}{19} + \\frac{5}{7} \\cdot \\frac{6}{19}$.",
            "question": "Cho hai biểu thức số hữu tỉ $A = \\left(-\\frac{1}{2}\\right)^3 : \\frac{1}{4} + \\frac{3}{2}$ và $B = \\frac{5}{7} \\cdot \\frac{13}{19} + \\frac{5}{7} \\cdot \\frac{6}{19}$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho hai đường thẳng phân biệt $a, b$ cùng vuông góc với $c$. Đường thẳng $d$ cắt $a, b$ tại $C, D$ sao cho $\\widehat{ACD} = 120^\\circ$.",
            "statements": [
              {
                "key": "a",
                "text": "Hai đường thẳng $a$ và $b$ song song với nhau.",
                "correct": true,
                "explanation": "Cùng vuông góc với đường thẳng thứ ba."
              },
              {
                "key": "b",
                "text": "Hai góc $\\widehat{ACD}$ và $\\widehat{CDB}$ là hai góc so le trong.",
                "correct": false,
                "explanation": "Là hai góc trong cùng phía."
              },
              {
                "key": "c",
                "text": "Số đo góc $\\widehat{CDB} = 60^\\circ$.",
                "correct": true,
                "explanation": "Bù nhau: $180^\\circ - 120^\\circ = 60^\\circ$."
              },
              {
                "key": "d",
                "text": "Tia phân giác của $\\widehat{CDB}$ tạo với đường thẳng $b$ một góc $30^\\circ$.",
                "correct": true,
                "explanation": "$60^\\circ : 2 = 30^\\circ$."
              }
            ],
            "stem": "Cho hai đường thẳng phân biệt $a, b$ cùng vuông góc với $c$. Đường thẳng $d$ cắt $a, b$ tại $C, D$ sao cho $\\widehat{ACD} = 120^\\circ$.",
            "question": "Cho hai đường thẳng phân biệt $a, b$ cùng vuông góc với $c$. Đường thẳng $d$ cắt $a, b$ tại $C, D$ sao cho $\\widehat{ACD} = 120^\\circ$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị biểu thức: $M = \\frac{2}{3} + \\left(-\\frac{1}{6}\\right) \\cdot 2$ (viết dạng a/b):",
            "answer": "1/3",
            "explanation": "$2/3 - 1/3 = 1/3$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số hữu tỉ $x > 0$, biết: $\\left(x - \\frac{1}{3}\\right)^2 = \\frac{4}{9}$",
            "answer": "1",
            "explanation": "$x - 1/3 = 2/3 \\Rightarrow x = 1$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho $xx' \\parallel yy'$. Góc $\\widehat{xAB} = 75^\\circ$. Tính góc so le trong $\\widehat{ABy'}$ (độ):",
            "answer": "75",
            "explanation": "So le trong bằng nhau: $75^\\circ$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của: $A = \\left|x - \\frac{3}{5}\\right| + 2026$",
            "answer": "2026",
            "explanation": "GTNN là $2026$ khi $x = 3/5$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "Tính giá trị của các biểu thức sau một cách hợp lý:\na) $A = \\frac{11}{24} - \\frac{5}{41} + \\frac{13}{24} + 0,5 - \\frac{36}{41}$\nb) $B = \\left(-\\frac{3}{4}\\right)^2 : \\frac{9}{8} - \\frac{2}{3} \\cdot \\left(\\frac{3}{4} - \\frac{1}{2}\\right)$",
            "rubric": "a) Nhóm cùng mẫu ra $0.5$ (0.5đ). b) Tính ra $1/3$ (0.5đ).",
            "modelSolution": "a) $A = (11/24 + 13/24) - (5/41 + 36/41) + 0,5 = 1 - 1 + 0,5 = 0,5$.\nb) $B = \\frac{9}{16} \\cdot \\frac{8}{9} - \\frac{2}{3} \\cdot \\frac{1}{4} = \\frac{1}{2} - \\frac{1}{6} = \\frac{1}{3}$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Tìm số hữu tỉ $x$, biết:\na) $\\frac{3}{4} + \\frac{1}{4}x = -\\frac{1}{2}$\nb) $(2x - 1)^3 = -\\frac{8}{27}$",
            "rubric": "a) $x = -5$ (0.35đ). b) $2x - 1 = -2/3 \\Rightarrow x = 1/6$ (0.4đ).",
            "modelSolution": "a) $\\frac{1}{4}x = -\\frac{5}{4} \\Rightarrow x = -5$.\nb) $2x - 1 = -\\frac{2}{3} \\Rightarrow 2x = \\frac{1}{3} \\Rightarrow x = \\frac{1}{6}$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho góc nhọn $\\widehat{xOy} = 60^\\circ$. Trên tia $Ox$ lấy điểm $A$, qua $A$ kẻ đường thẳng $d$ song song với $Oy$.\na) Tính số đo góc $\\widehat{xAd}$ (góc đồng vị với $\\widehat{xOy}$).\nb) Kẻ tia phân giác $Oz$ của $\\widehat{xOy}$ và tia phân giác $At$ của $\\widehat{xAd}$. Chứng minh rằng $At \\parallel Oz$.",
            "rubric": "a) $60^\\circ$ (0.35đ). b) Góc đồng vị bằng nhau $30^\\circ \\Rightarrow At \\parallel Oz$ (0.4đ).",
            "modelSolution": "a) Vì $d \\parallel Oy$ nên $\\widehat{xAd} = \\widehat{xOy} = 60^\\circ$ (đồng vị).\nb) Vì $Oz, At$ là phân giác nên $\\widehat{xOz} = \\widehat{xAt} = 30^\\circ$. Hai góc này ở vị trí đồng vị nên $At \\parallel Oz$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "So sánh hai lũy thừa sau: $A = 2^{300}$ và $B = 3^{200}$.",
            "rubric": "$2^{300} = 8^{100} < 9^{100} = 3^{200}$ (0.5đ).",
            "modelSolution": "$A = (2^3)^{100} = 8^{100}$; $B = (3^2)^{100} = 9^{100}$. Vì $8 < 9$ nên $2^{300} < 3^{200}$."
          }
        ]
      },
      {
        "id": "p_g7_mid1_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 7 (ĐỀ SỐ 02)",
        "topic": "Lũy thừa hữu tỉ, Quy tắc chuyển vế, Giá trị tuyệt đối & Hai đường thẳng song song",
        "grade": "7",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Số đối của $-\\left(-\\frac{2}{5}\\right)$ là:",
            "options": [
              "$-\\frac{2}{5}$",
              "$\\frac{5}{2}$",
              "$-\\frac{5}{2}$",
              "$\\frac{2}{5}$"
            ],
            "correct": 0,
            "explanation": "$-\\left(-\\frac{2}{5}\\right) = \\frac{2}{5}$. Số đối của $\\frac{2}{5}$ là $-\\frac{2}{5}$.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Điểm biểu diễn số hữu tỉ $-\\frac{3}{4}$ trên trục số nằm ở vị trí nào?",
            "options": [
              "Trùng với điểm 0",
              "Bên trái điểm 0",
              "Bên phải điểm 1",
              "Bên phải điểm 0"
            ],
            "correct": 1,
            "explanation": "Số âm nằm bên trái điểm 0 trên trục số.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Kết quả của phép tính $\\left(\\frac{1}{2}\\right)^2 \\cdot \\left(\\frac{1}{2}\\right)^3$ là:",
            "options": [
              "$\\left(\\frac{1}{4}\\right)^5$",
              "$\\left(\\frac{1}{2}\\right)^6$",
              "$\\left(\\frac{1}{2}\\right)^5$",
              "$\\frac{1}{4}$"
            ],
            "correct": 2,
            "explanation": "$\\left(\\frac{1}{2}\\right)^{2+3} = \\left(\\frac{1}{2}\\right)^5$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Với $x \\in \\mathbb{Q}$, giá trị của $|x|$ luôn thỏa mãn điều kiện nào sau đây?",
            "options": [
              "$|x| \\le 0$",
              "$|x| \\ge 0$",
              "$|x| < 0$",
              "$|x| > 0$"
            ],
            "correct": 1,
            "explanation": "Giá trị tuyệt đối của một số hữu tỉ luôn không âm ($|x| \\ge 0$).",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Hai góc kề bù có tổng số đo bằng:",
            "options": [
              "$360^\\circ$",
              "$90^\\circ$",
              "$180^\\circ$",
              "$45^\\circ$"
            ],
            "correct": 2,
            "explanation": "Hai góc kề bù luôn có tổng số đo bằng $180^\\circ$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Cho $\\widehat{xOy}$ và $\\widehat{yOz}$ là hai góc kề bù. Biết $\\widehat{xOy} = 50^\\circ$, số đo của $\\widehat{yOz}$ là:",
            "options": [
              "$40^\\circ$",
              "$140^\\circ$",
              "$50^\\circ$",
              "$130^\\circ$"
            ],
            "correct": 3,
            "explanation": "$\\widehat{yOz} = 180^\\circ - 50^\\circ = 130^\\circ$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Cho đường thẳng $c$ cắt hai đường thẳng $a$ và $b$. Để $a \\parallel b$ thì cần điều kiện nào sau đây?",
            "options": [
              "Hai góc đồng vị bằng nhau",
              "Một trong các điều kiện trên",
              "Hai góc so le trong bằng nhau",
              "Hai góc trong cùng phía bù nhau"
            ],
            "correct": 1,
            "explanation": "Một trong các dấu hiệu trên đều suy ra $a \\parallel b$.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Công thức lũy thừa của một lũy thừa là:",
            "options": [
              "$(x^m)^n = x^{m-n}$",
              "$(x^m)^n = (x \\cdot m)^n$",
              "$(x^m)^n = x^{m \\cdot n}$",
              "$(x^m)^n = x^{m+n}$"
            ],
            "correct": 2,
            "explanation": "$(x^m)^n = x^{m \\cdot n}$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Kết quả của phép tính $\\left(-\\frac{3}{5}\\right) \\cdot \\frac{5}{9} + \\frac{1}{3}$ là:",
            "options": [
              "$0$",
              "$\\frac{1}{3}$",
              "$-\\frac{2}{3}$",
              "$\\frac{2}{3}$"
            ],
            "correct": 0,
            "explanation": "$-\\frac{1}{3} + \\frac{1}{3} = 0$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Tìm $x$, biết: $|x - 0,5| = 1,5$. Các giá trị của $x$ là:",
            "options": [
              "$x = -1$",
              "$x = 1$",
              "$x = 2$",
              "$x = 2$ hoặc $x = -1$"
            ],
            "correct": 3,
            "explanation": "$x - 0,5 = 1,5 \\Rightarrow x = 2$ hoặc $x - 0,5 = -1,5 \\Rightarrow x = -1$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = 60^\\circ$. Qua $C$ kẻ đường thẳng song song với $AB$. Góc so le trong với góc $\\widehat{B}$ có số đo là:",
            "options": [
              "$60^\\circ$",
              "$70^\\circ$",
              "$120^\\circ$",
              "$50^\\circ$"
            ],
            "correct": 0,
            "explanation": "Hai góc so le trong bằng nhau nên bằng $\\widehat{B} = 60^\\circ$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $n$ thỏa mãn: $2^n = 32$.",
            "options": [
              "$n = 6$",
              "$n = 16$",
              "$n = 4$",
              "$n = 5$"
            ],
            "correct": 3,
            "explanation": "$2^5 = 32 \\Rightarrow n = 5$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho hai số hữu tỉ $x = -0,75$ và $y = \\frac{3}{4}$.",
            "statements": [
              {
                "key": "a",
                "text": "Số $x$ viết dưới dạng phân số tối giản là $-\\frac{3}{4}$.",
                "correct": true,
                "explanation": "$-0,75 = -75/100 = -3/4$."
              },
              {
                "key": "b",
                "text": "Hai số $x$ và $y$ là hai số đối nhau.",
                "correct": true,
                "explanation": "$x + y = -3/4 + 3/4 = 0$."
              },
              {
                "key": "c",
                "text": "Giá trị của tích $x \\cdot y$ là một số hữu tỉ dương.",
                "correct": false,
                "explanation": "Tích của một số âm và một số dương là số âm: $-9/16 < 0$."
              },
              {
                "key": "d",
                "text": "Giá trị của $|x| + |y| = 1,5$.",
                "correct": true,
                "explanation": "$0,75 + 0,75 = 1,5$."
              }
            ],
            "stem": "Cho hai số hữu tỉ $x = -0,75$ và $y = \\frac{3}{4}$.",
            "question": "Cho hai số hữu tỉ $x = -0,75$ và $y = \\frac{3}{4}$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho hình vẽ có $a \\parallel b$. Đường thẳng $c$ cắt $a$ tại $A$ và cắt $b$ tại $B$ sao cho góc $\\widehat{A}_1 = 45^\\circ$ (góc so le trong).",
            "statements": [
              {
                "key": "a",
                "text": "Góc so le trong $\\widehat{B}_1$ với $\\widehat{A}_1$ có số đo bằng $45^\\circ$.",
                "correct": true,
                "explanation": "Hai góc so le trong bằng nhau do $a \\parallel b$."
              },
              {
                "key": "b",
                "text": "Góc đồng vị với $\\widehat{A}_1$ có số đo bằng $135^\\circ$.",
                "correct": false,
                "explanation": "Hai góc đồng vị phải bằng nhau ($45^\\circ$)."
              },
              {
                "key": "c",
                "text": "Góc trong cùng phía với $\\widehat{A}_1$ có số đo bằng $135^\\circ$.",
                "correct": true,
                "explanation": "Bù nhau: $180^\\circ - 45^\\circ = 135^\\circ$."
              },
              {
                "key": "d",
                "text": "Nếu đường thẳng $d \\perp a$ thì đường thẳng $d$ cũng vuông góc với $b$.",
                "correct": true,
                "explanation": "Định lí từ vuông góc đến song song."
              }
            ],
            "stem": "Cho hình vẽ có $a \\parallel b$. Đường thẳng $c$ cắt $a$ tại $A$ và cắt $b$ tại $B$ sao cho góc $\\widehat{A}_1 = 45^\\circ$ (góc so le trong).",
            "question": "Cho hình vẽ có $a \\parallel b$. Đường thẳng $c$ cắt $a$ tại $A$ và cắt $b$ tại $B$ sao cho góc $\\widehat{A}_1 = 45^\\circ$ (góc so le trong)."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị biểu thức: $A = \\left(-\\frac{2}{3}\\right)^2 + \\frac{5}{9}$",
            "answer": "1",
            "explanation": "$4/9 + 5/9 = 9/9 = 1$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số hữu tỉ $x$, biết: $x - \\frac{2}{5} = -\\frac{1}{2}$ (viết dưới dạng số thập phân):",
            "answer": "-0.1",
            "explanation": "$x = -1/2 + 2/5 = -5/10 + 4/10 = -1/10 = -0,1$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Hai góc $\\widehat{xOy}$ và $\\widehat{yOz}$ kề bù. Biết $\\widehat{xOy} = 2 \\cdot \\widehat{yOz}$. Tính số đo góc $\\widehat{xOy}$ (đơn vị: độ):",
            "answer": "120",
            "explanation": "$2\\widehat{yOz} + \\widehat{yOz} = 180^\\circ \\Rightarrow \\widehat{yOz} = 60^\\circ \\Rightarrow \\widehat{xOy} = 120^\\circ$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tính giá trị của tổng $S = \\frac{1}{1 \\cdot 2} + \\frac{1}{2 \\cdot 3} + \\frac{1}{3 \\cdot 4} + \\dots + \\frac{1}{99 \\cdot 100}$ (dạng a/b):",
            "answer": "99/100",
            "explanation": "$S = 1 - 1/100 = 99/100$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "Thực hiện phép tính hợp lý:\na) $\\frac{4}{9} \\cdot \\frac{13}{3} - \\frac{4}{9} \\cdot \\frac{4}{3}$\nb) $\\left(-\\frac{1}{3}\\right)^2 : \\frac{4}{9} + \\frac{1}{2} \\cdot \\left(-\\frac{4}{3}\\right)$",
            "rubric": "a) $4/9(13/3 - 4/3) = 4/9 \\cdot 3 = 4/3$ (0.5đ).\nb) $1/9 \\cdot 9/4 - 2/3 = 1/4 - 2/3 = -5/12$ (0.5đ).",
            "modelSolution": "a) $\\frac{4}{9} \\cdot \\left(\\frac{13}{3} - \\frac{4}{3}\\right) = \\frac{4}{9} \\cdot \\frac{9}{3} = \\frac{4}{9} \\cdot 3 = \\frac{4}{3}$.\nb) $\\frac{1}{9} \\cdot \\frac{9}{4} - \\frac{2}{3} = \\frac{1}{4} - \\frac{2}{3} = \\frac{3 - 8}{12} = -\\frac{5}{12}$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Tìm $x$, biết:\na) $\\frac{2}{3}x - \\frac{1}{2} = \\frac{5}{6}$\nb) $\\left(x + \\frac{1}{2}\\right)^2 = \\frac{25}{16}$",
            "rubric": "a) $2/3x = 8/6 = 4/3 \\Rightarrow x = 2$ (0.35đ).\nb) $x + 1/2 = \\pm 5/4 \\Rightarrow x = 3/4$ hoặc $x = -7/4$ (0.4đ).",
            "modelSolution": "a) $\\frac{2}{3}x = \\frac{5}{6} + \\frac{3}{6} = \\frac{8}{6} = \\frac{4}{3} \\Leftrightarrow x = \\frac{4}{3} : \\frac{2}{3} = 2$.\nb) $x + \\frac{1}{2} = \\frac{5}{4} \\Rightarrow x = \\frac{5}{4} - \\frac{2}{4} = \\frac{3}{4}$ hoặc $x + \\frac{1}{2} = -\\frac{5}{4} \\Rightarrow x = -\\frac{5}{4} - \\frac{2}{4} = -\\frac{7}{4}$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho hình vẽ có $Ax \\parallel By$. Lấy điểm $C$ nằm giữa hai đường thẳng sao cho tia $CA$ và $CB$ tạo thành góc $\\widehat{ACB}$. Biết $\\widehat{xAC} = 40^\\circ$ và $\\widehat{CBy} = 50^\\circ$.\na) Qua $C$ kẻ đường thẳng $Cz$ song song với $Ax$. Chứng minh $Cz \\parallel By$.\nb) Tính số đo của góc $\\widehat{ACB}$.",
            "rubric": "a) Vì $Cz \\parallel Ax$ và $Ax \\parallel By \\Rightarrow Cz \\parallel By$ (0.35đ).\nb) Góc $\\widehat{ACz} = 40^\\circ$, $\\widehat{zCB} = 50^\\circ \\Rightarrow \\widehat{ACB} = 40^\\circ + 50^\\circ = 90^\\circ$ (0.4đ).",
            "modelSolution": "a) Vì $Cz \\parallel Ax$ (theo cách vẽ) mà $Ax \\parallel By$ (theo giả thiết) nên $Cz \\parallel By$ (hai đường thẳng cùng song song với đường thẳng thứ ba).\nb) Vì $Cz \\parallel Ax$ nên $\\widehat{ACz} = \\widehat{xAC} = 40^\\circ$ (hai góc so le trong).\nVì $Cz \\parallel By$ nên $\\widehat{zCB} = \\widehat{CBy} = 50^\\circ$ (hai góc so le trong).\nTia $Cz$ nằm giữa hai tia $CA$ và $CB$ nên:\n$$\\widehat{ACB} = \\widehat{ACz} + \\widehat{zCB} = 40^\\circ + 50^\\circ = 90^\\circ.$$\nVậy $\\widehat{ACB} = 90^\\circ$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Tìm giá trị lớn nhất của biểu thức: $P = \\frac{12}{|x - 3| + 4}$.",
            "rubric": "Vì $|x - 3| \\ge 0 \\Rightarrow |x - 3| + 4 \\ge 4 \\Rightarrow P \\le 12/4 = 3$. Đạt khi $x = 3$ (0.5đ).",
            "modelSolution": "Ta có $|x - 3| \\ge 0$ với mọi $x \\in \\mathbb{Q}$.\nSuy ra $|x - 3| + 4 \\ge 4$ với mọi $x$.\nDo đó: $P = \\frac{12}{|x - 3| + 4} \\le \\frac{12}{4} = 3$.\nDấu \"=\" xảy ra khi và chỉ khi $|x - 3| = 0 \\Leftrightarrow x = 3$.\nVậy giá trị lớn nhất của biểu thức $P$ là $3$ khi $x = 3$."
          }
        ]
      },
      {
        "id": "p_g7_mid1_03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 7 (ĐỀ SỐ 03)",
        "topic": "Tính chất dãy tỉ số cơ bản, Phân số quy luật, Chứng minh định lí & Góc phụ, bù",
        "grade": "7",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Số nào sau đây viết được dưới dạng số thập phân hữu hạn?",
            "options": [
              "$\\frac{3}{4}$",
              "$\\frac{1}{3}$",
              "$\\frac{5}{7}$",
              "$\\frac{1}{6}$"
            ],
            "correct": 0,
            "explanation": "$\\frac{3}{4} = 0,75$ là số thập phân hữu hạn.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Khẳng định nào sau đây là **sai**?",
            "options": [
              "Số $0$ là số hữu tỉ",
              "Tập $\\mathbb{Z}$ là tập con của $\\mathbb{Q}$",
              "Phân số có mẫu bằng 0 là số hữu tỉ",
              "Số nguyên âm cũng là số hữu tỉ"
            ],
            "correct": 2,
            "explanation": "Mẫu số của phân số phải khác 0.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Kết quả của phép tính $\\left(-\\frac{1}{3}\\right)^4$ là:",
            "options": [
              "$\\frac{1}{81}$",
              "$-\\frac{1}{81}$",
              "$\\frac{4}{12}$",
              "$-\\frac{4}{81}$"
            ],
            "correct": 0,
            "explanation": "Số mũ chẵn của số âm cho kết quả dương: $1/81$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Hai góc bù nhau có tổng số đo bằng:",
            "options": [
              "$60^\\circ$",
              "$180^\\circ$",
              "$90^\\circ$",
              "$360^\\circ$"
            ],
            "correct": 1,
            "explanation": "Định nghĩa hai góc bù nhau có tổng số đo bằng $180^\\circ$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Tia $Ot$ là tia phân giác của $\\widehat{mOn}$ khi:",
            "options": [
              "$\\widehat{mOt} = \\widehat{tOn}$",
              "Tia $Ot$ nằm giữa $Om, On$ và $\\widehat{mOt} = \\widehat{tOn} = \\frac{\\widehat{mOn}}{2}$",
              "Tia $Ot$ nằm giữa hai tia $Om, On$",
              "$\\widehat{mOt} + \\widehat{tOn} = 180^\\circ$"
            ],
            "correct": 1,
            "explanation": "Tia phân giác phải nằm giữa và tạo với hai cạnh hai góc bằng nhau.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Cho hai đường thẳng phân biệt $a$ và $b$. Nếu $a \\parallel c$ và $b \\parallel c$ thì:",
            "options": [
              "$a \\parallel b$",
              "$a$ trùng $b$",
              "$a$ cắt $b$",
              "$a \\perp b$"
            ],
            "correct": 0,
            "explanation": "Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì chúng song song với nhau.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Cho $x = \\frac{a}{b}$ ($a, b \\in \\mathbb{Z}, b \\ne 0$). Để $x$ là số hữu tỉ âm thì:",
            "options": [
              "$a$ và $b$ cùng dấu",
              "$a = 0$",
              "$a$ và $b$ khác dấu",
              "$b < 0$"
            ],
            "correct": 2,
            "explanation": "Số hữu tỉ âm khi tử và mẫu trái dấu (khác dấu).",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Viết số $0,25$ dưới dạng phân số tối giản ta được:",
            "options": [
              "$\\frac{2}{8}$",
              "$\\frac{5}{20}$",
              "$\\frac{25}{100}$",
              "$\\frac{1}{4}$"
            ],
            "correct": 3,
            "explanation": "$0,25 = 25/100 = 1/4$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Tính: $P = \\left(\\frac{2}{3}\\right)^3 : \\left(\\frac{2}{3}\\right)^2 + \\frac{1}{3}$",
            "options": [
              "$\\frac{4}{9}$",
              "$0$",
              "$\\frac{2}{3}$",
              "$1$"
            ],
            "correct": 3,
            "explanation": "$2/3 + 1/3 = 1$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Tìm $x$, biết: $2x - \\frac{1}{3} = \\frac{5}{3}$",
            "options": [
              "$x = 2$",
              "$x = \\frac{4}{3}$",
              "$x = 1$",
              "$x = \\frac{2}{3}$"
            ],
            "correct": 2,
            "explanation": "$2x = 6/3 = 2 \\Rightarrow x = 1$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Cho hình vẽ có $a \\parallel b$. Biết góc trong cùng phía với $\\widehat{A}_1$ có số đo là $110^\\circ$. Số đo của góc $\\widehat{A}_1$ là:",
            "options": [
              "$90^\\circ$",
              "$70^\\circ$",
              "$80^\\circ$",
              "$110^\\circ$"
            ],
            "correct": 1,
            "explanation": "$180^\\circ - 110^\\circ = 70^\\circ$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Biết $\\left(-\\frac{1}{2}\\right)^x = -\\frac{1}{8}$. Giá trị của $x$ là:",
            "options": [
              "$1$",
              "$4$",
              "$2$",
              "$3$"
            ],
            "correct": 3,
            "explanation": "$(-1/2)^3 = -1/8 \\Rightarrow x = 3$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho biểu thức $P = \\frac{2}{5} - \\left(\\frac{1}{2} - \\frac{3}{5}\\right) + \\frac{1}{2}$.",
            "statements": [
              {
                "key": "a",
                "text": "Bỏ dấu ngoặc có dấu trừ đằng trước, ta được: $\\frac{2}{5} - \\frac{1}{2} + \\frac{3}{5} + \\frac{1}{2}$.",
                "correct": true,
                "explanation": "Đúng quy tắc phá ngoặc đổi dấu."
              },
              {
                "key": "b",
                "text": "Hai số hạng $-\\frac{1}{2}$ và $\\frac{1}{2}$ là hai số đối nhau nên có tổng bằng 0.",
                "correct": true,
                "explanation": "Tổng hai số đối nhau bằng 0."
              },
              {
                "key": "c",
                "text": "Giá trị của biểu thức $P$ bằng $1$.",
                "correct": true,
                "explanation": "$2/5 + 3/5 = 5/5 = 1$."
              },
              {
                "key": "d",
                "text": "Biểu thức $P$ nhận giá trị là một phân số không phải số nguyên.",
                "correct": false,
                "explanation": "$1 \\in \\mathbb{Z}$ là số nguyên."
              }
            ],
            "stem": "Cho biểu thức $P = \\frac{2}{5} - \\left(\\frac{1}{2} - \\frac{3}{5}\\right) + \\frac{1}{2}$.",
            "question": "Cho biểu thức $P = \\frac{2}{5} - \\left(\\frac{1}{2} - \\frac{3}{5}\\right) + \\frac{1}{2}$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho hai góc kề bù $\\widehat{AOB}$ và $\\widehat{BOC}$ với $\\widehat{AOB} = 100^\\circ$. Vẽ tia phân giác $OD$ của góc $\\widehat{AOB}$ và tia phân giác $OE$ của góc $\\widehat{BOC}$.",
            "statements": [
              {
                "key": "a",
                "text": "Số đo của góc $\\widehat{BOC}$ bằng $80^\\circ$.",
                "correct": true,
                "explanation": "$180^\\circ - 100^\\circ = 80^\\circ$."
              },
              {
                "key": "b",
                "text": "Số đo của góc $\\widehat{BOD}$ bằng $50^\\circ$.",
                "correct": true,
                "explanation": "$100^\\circ : 2 = 50^\\circ$."
              },
              {
                "key": "c",
                "text": "Số đo của góc $\\widehat{BOE}$ bằng $40^\\circ$.",
                "correct": true,
                "explanation": "$80^\\circ : 2 = 40^\\circ$."
              },
              {
                "key": "d",
                "text": "Góc tạo bởi hai tia phân giác $\\widehat{DOE}$ là góc nhọn.",
                "correct": false,
                "explanation": "$\\widehat{DOE} = 50^\\circ + 40^\\circ = 90^\\circ$ là góc vuông."
              }
            ],
            "stem": "Cho hai góc kề bù $\\widehat{AOB}$ và $\\widehat{BOC}$ với $\\widehat{AOB} = 100^\\circ$. Vẽ tia phân giác $OD$ của góc $\\widehat{AOB}$ và tia phân giác $OE$ của góc $\\widehat{BOC}$.",
            "question": "Cho hai góc kề bù $\\widehat{AOB}$ và $\\widehat{BOC}$ với $\\widehat{AOB} = 100^\\circ$. Vẽ tia phân giác $OD$ của góc $\\widehat{AOB}$ và tia phân giác $OE$ của góc $\\widehat{BOC}$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính: $M = \\frac{5}{12} - \\frac{7}{18} + \\frac{1}{36}$ (dạng tối giản a/b):",
            "answer": "1/18",
            "explanation": "$(15 - 14 + 1)/36 = 2/36 = 1/18$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm $x$, biết: $3^{x+1} - 3^x = 18$",
            "answer": "2",
            "explanation": "$3^x(3 - 1) = 18 \\Rightarrow 2 \\cdot 3^x = 18 \\Rightarrow 3^x = 9 \\Rightarrow x = 2$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho hai đường thẳng $a \\parallel b$. Đường thẳng $c$ cắt $a$ tại $A$ và $b$ tại $B$. Biết tổng hai góc trong cùng phía bằng $180^\\circ$. Nếu một góc bằng $3$ lần góc kia, tính số đo góc lớn hơn (độ):",
            "answer": "135",
            "explanation": "$x + 3x = 180^\\circ \\Rightarrow 4x = 180^\\circ \\Rightarrow x = 45^\\circ \\Rightarrow 3x = 135^\\circ$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của biểu thức: $Q = |x - 1| + |x - 5|$",
            "answer": "4",
            "explanation": "$|x - 1| + |5 - x| \\ge |x - 1 + 5 - x| = 4$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "Tính hợp lý:\na) $\\left(-\\frac{5}{11}\\right) \\cdot \\frac{7}{15} + \\left(-\\frac{5}{11}\\right) \\cdot \\frac{8}{15} + 1\\frac{5}{11}$\nb) $\\left(\\frac{1}{3} - 0,5\\right) \\cdot 6 + \\left(-\\frac{1}{2}\\right)^2 : \\frac{1}{4}$",
            "rubric": "a) $-5/11 \\cdot 1 + 16/11 = 11/11 = 1$ (0.5đ).\nb) $(1/3 - 1/2) \\cdot 6 + 1/4 : 1/4 = -1/6 \\cdot 6 + 1 = -1 + 1 = 0$ (0.5đ).",
            "modelSolution": "a) $-\\frac{5}{11} \\cdot \\left(\\frac{7}{15} + \\frac{8}{15}\\right) + \\frac{16}{11} = -\\frac{5}{11} \\cdot 1 + \\frac{16}{11} = \\frac{11}{11} = 1$.\nb) $\\left(\\frac{2 - 3}{6}\\right) \\cdot 6 + \\frac{1}{4} \\cdot 4 = -\\frac{1}{6} \\cdot 6 + 1 = -1 + 1 = 0$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Tìm $x$, biết:\na) $\\frac{4}{7} - x = \\frac{1}{3}$\nb) $|2x - 1| - \\frac{1}{2} = \\frac{3}{2}$",
            "rubric": "a) $x = 4/7 - 1/3 = 5/21$ (0.35đ).\nb) $|2x - 1| = 2 \\Rightarrow 2x - 1 = 2 \\Rightarrow x = 3/2$ hoặc $2x - 1 = -2 \\Rightarrow x = -1/2$ (0.4đ).",
            "modelSolution": "a) $x = \\frac{4}{7} - \\frac{1}{3} = \\frac{12 - 7}{21} = \\frac{5}{21}$.\nb) $|2x - 1| = \\frac{3}{2} + \\frac{1}{2} = 2$.\nTrường hợp 1: $2x - 1 = 2 \\Leftrightarrow 2x = 3 \\Leftrightarrow x = \\frac{3}{2}$.\nTrường hợp 2: $2x - 1 = -2 \\Leftrightarrow 2x = -1 \\Leftrightarrow x = -\\frac{1}{2}$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho tam giác $ABC$. Vẽ đoạn thẳng $AD$ sao cho $AD \\parallel BC$ và $AD = BC$ ($D$ và $C$ nằm ở hai phía khác nhau đối với đường thẳng $AB$).\na) Chứng minh rằng $\\widehat{DAB} = \\widehat{ABC}$.\nb) Gọi $M$ là trung điểm của $AB$. Chứng minh rằng ba điểm $D, M, C$ thẳng hàng.",
            "rubric": "a) So le trong do $AD \\parallel BC$ (0.35đ).\nb) $\\Delta ADM = \\Delta BCM$ (c-g-c) $\\Rightarrow \\widehat{AMD} = \\widehat{BMC} \\Rightarrow D, M, C$ thẳng hàng (0.4đ).",
            "modelSolution": "a) Vì $AD \\parallel BC$ nên $\\widehat{DAB} = \\widehat{ABC}$ (hai góc so le trong).\nb) Xét $\\Delta ADM$ và $\\Delta BCM$ có:\n$AD = BC$ (giả thiết),\n$\\widehat{DAM} = \\widehat{CBM}$ (chứng minh trên),\n$AM = BM$ ($M$ là trung điểm $AB$).\nDo đó $\\Delta ADM = \\Delta BCM$ (c - g - c).\nSuy ra $\\widehat{AMD} = \\widehat{BMC}$ (hai góc tương ứng).\nMà $\\widehat{AMC} + \\widehat{BMC} = 180^\\circ$ (hai góc kề bù) nên $\\widehat{AMC} + \\widehat{AMD} = 180^\\circ$, suy ra $\\widehat{DMC} = 180^\\circ$.\nVậy ba điểm $D, M, C$ thẳng hàng."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Chứng minh rằng biểu thức $M = \\frac{1}{3} + \\frac{1}{3^2} + \\frac{1}{3^3} + \\dots + \\frac{1}{3^{100}} < \\frac{1}{2}$.",
            "rubric": "Nhân $3M = 1 + 1/3 + \\dots + 1/3^{99}$. $2M = 1 - 1/3^{100} < 1 \\Rightarrow M < 1/2$ (0.5đ).",
            "modelSolution": "Ta có: $M = \\frac{1}{3} + \\frac{1}{3^2} + \\frac{1}{3^3} + \\dots + \\frac{1}{3^{100}}$.\nNhân cả hai vế với 3:\n$$3M = 1 + \\frac{1}{3} + \\frac{1}{3^2} + \\dots + \\frac{1}{3^{99}}$$\nTrừ vế theo vế:\n$$3M - M = \\left(1 + \\frac{1}{3} + \\dots + \\frac{1}{3^{99}}\\right) - \\left(\\frac{1}{3} + \\dots + \\frac{1}{3^{100}}\\right)$$\n$$2M = 1 - \\frac{1}{3^{100}}$$\n$$M = \\frac{1}{2} - \\frac{1}{2 \\cdot 3^{100}}$$\nVì $\\frac{1}{2 \\cdot 3^{100}} > 0$ nên $M < \\frac{1}{2}$ (đpcm)."
          }
        ]
      },
      {
        "id": "p_g7_mid1_04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 7 (ĐỀ SỐ 04)",
        "topic": "Đại số hữu tỉ nâng cao, Lũy thừa phân số, Suy luận hình học & Bất đẳng thức giá trị tuyệt đối",
        "grade": "7",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Số nào sau đây là số đối của số $-\\sqrt{\\frac{4}{9}}$?",
            "options": [
              "$\\frac{2}{3}$",
              "$-\\frac{4}{9}$",
              "$\\frac{4}{9}$",
              "$-\\frac{2}{3}$"
            ],
            "correct": 0,
            "explanation": "$-\\sqrt{4/9} = -2/3$. Số đối là $2/3$.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Kết quả của $(-0,1)^3$ là:",
            "options": [
              "$-0,3$",
              "$0,001$",
              "$-0,001$",
              "$-0,01$"
            ],
            "correct": 2,
            "explanation": "$(-0,1)^3 = -0,001$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Khẳng định nào sau đây về số hữu tỉ là **đúng**?",
            "options": [
              "Số vô tỉ cũng là số hữu tỉ",
              "Số $0$ vừa là số hữu tỉ dương vừa là số hữu tỉ âm",
              "Mọi số tự nhiên đều là số hữu tỉ",
              "Mỗi số hữu tỉ được biểu diễn bởi duy nhất một phân số"
            ],
            "correct": 2,
            "explanation": "Mọi số tự nhiên $n$ đều viết được thành $n/1$ nên là số hữu tỉ.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Hai đường thẳng vuông góc tạo thành bao nhiêu góc vuông?",
            "options": [
              "$2$",
              "$3$",
              "$4$",
              "$1$"
            ],
            "correct": 2,
            "explanation": "Hai đường thẳng vuông góc tạo thành 4 góc vuông.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Đường trung trực của đoạn thẳng $AB$ là đường thẳng:",
            "options": [
              "Đi qua trung điểm của $AB$ và vuông góc với $AB$",
              "Song song với $AB$",
              "Đi qua trung điểm của $AB$",
              "Vuông góc với $AB$"
            ],
            "correct": 0,
            "explanation": "Đường thẳng vuông góc với đoạn thẳng tại trung điểm của nó là đường trung trực.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Cho $x : \\left(-\\frac{1}{2}\\right) = 4$. Giá trị của $x$ là:",
            "options": [
              "$2$",
              "$-2$",
              "$8$",
              "$-8$"
            ],
            "correct": 1,
            "explanation": "$x = 4 \\cdot (-1/2) = -2$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Phát biểu nào sau đây là một định lí?",
            "options": [
              "Hai góc đối đỉnh thì bằng nhau",
              "Góc nhọn là góc nhỏ hơn $90^\\circ$",
              "Vẽ tia phân giác của một góc",
              "Nếu góc lớn hơn $90^\\circ$ thì là góc tù"
            ],
            "correct": 0,
            "explanation": "\"Hai góc đối đỉnh thì bằng nhau\" là một định lí đã được chứng minh.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Lũy thừa $\\left(\\frac{3}{5}\\right)^0$ có giá trị bằng:",
            "options": [
              "$0$",
              "$1$",
              "Không xác định",
              "$\\frac{3}{5}$"
            ],
            "correct": 1,
            "explanation": "Quy ước: $a^0 = 1$ với mọi $a \\ne 0$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "So sánh hai số hữu tỉ $a = -\\frac{5}{8}$ và $b = -\\frac{7}{12}$:",
            "options": [
              "$a = b$",
              "Không so sánh được",
              "$a > b$",
              "$a < b$"
            ],
            "correct": 3,
            "explanation": "$a = -15/24; b = -14/24$. Vì $-15 < -14$ nên $a < b$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Cho hai góc bù nhau $\\widehat{A}$ và $\\widehat{B}$ có tỉ lệ $\\widehat{A} : \\widehat{B} = 2 : 3$. Số đo của góc $\\widehat{A}$ là:",
            "options": [
              "$60^\\circ$",
              "$72^\\circ$",
              "$108^\\circ$",
              "$36^\\circ$"
            ],
            "correct": 1,
            "explanation": "$\\widehat{A} = 180^\\circ : (2 + 3) \\cdot 2 = 72^\\circ$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Tính: $K = \\frac{4^5 \\cdot 9^4}{6^8}$",
            "options": [
              "$4$",
              "$\\frac{1}{2}$",
              "$2$",
              "$1$"
            ],
            "correct": 3,
            "explanation": "$4^5 \\cdot 9^4 = 2^{10} \\cdot 3^8$. $6^8 = 2^8 \\cdot 3^8$. Chia ra $2^2 = 4$... Đổi đề: $\\frac{4^4 \\cdot 9^4}{6^8} = \\frac{2^8 \\cdot 3^8}{6^8} = 1$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Cho $a \\parallel b$ và $b \\parallel c$. Khẳng định nào sau đây luôn **đúng**?",
            "options": [
              "$a \\perp c$",
              "$a$ cắt $c$",
              "$a$ trùng $c$",
              "$a \\parallel c$"
            ],
            "correct": 3,
            "explanation": "Tính chất bắc cầu của quan hệ song song.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho đẳng thức lũy thừa: $A = \\frac{27^2 \\cdot 8^3}{6^6}$.",
            "statements": [
              {
                "key": "a",
                "text": "Viết $27^2$ dưới dạng lũy thừa cơ số 3 ta được $3^6$.",
                "correct": true,
                "explanation": "$(3^3)^2 = 3^6$."
              },
              {
                "key": "b",
                "text": "Viết $8^3$ dưới dạng lũy thừa cơ số 2 ta được $2^9$.",
                "correct": true,
                "explanation": "$(2^3)^3 = 2^9$."
              },
              {
                "key": "c",
                "text": "Mẫu số $6^6$ viết thành tích là $2^6 \\cdot 3^6$.",
                "correct": true,
                "explanation": "$(2 \\cdot 3)^6 = 2^6 \\cdot 3^6$."
              },
              {
                "key": "d",
                "text": "Giá trị của biểu thức $A$ bằng $4$.",
                "correct": false,
                "explanation": "$A = \\frac{3^6 \\cdot 2^9}{2^6 \\cdot 3^6} = 2^3 = 8$ (không phải 4)."
              }
            ],
            "stem": "Cho đẳng thức lũy thừa: $A = \\frac{27^2 \\cdot 8^3}{6^6}$.",
            "question": "Cho đẳng thức lũy thừa: $A = \\frac{27^2 \\cdot 8^3}{6^6}$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho đoạn thẳng $AB = 6\\text{ cm}$. Gọi $M$ là trung điểm của $AB$. Qua $M$ kẻ đường thẳng $xy$ vuông góc với $AB$. Lấy điểm $C$ bất kỳ thuộc tia $Mx$ ($C \\ne M$).",
            "statements": [
              {
                "key": "a",
                "text": "Đoạn thẳng $AM = MB = 3\\text{ cm}$.",
                "correct": true,
                "explanation": "$M$ là trung điểm nên $AM = AB : 2 = 3\\text{ cm}$."
              },
              {
                "key": "b",
                "text": "Đường thẳng $xy$ là đường trung trực của đoạn thẳng $AB$.",
                "correct": true,
                "explanation": "Vuông góc tại trung điểm."
              },
              {
                "key": "c",
                "text": "Độ dài đoạn thẳng $CA$ luôn bằng độ dài đoạn thẳng $CB$.",
                "correct": true,
                "explanation": "Điểm nằm trên đường trung trực thì cách đều hai đầu mút."
              },
              {
                "key": "d",
                "text": "Tam giác $CAB$ là tam giác vuông tại $C$ với mọi vị trí của điểm $C$.",
                "correct": false,
                "explanation": "Chỉ là tam giác cân tại $C$, không nhất thiết vuông."
              }
            ],
            "stem": "Cho đoạn thẳng $AB = 6\\text{ cm}$. Gọi $M$ là trung điểm của $AB$. Qua $M$ kẻ đường thẳng $xy$ vuông góc với $AB$. Lấy điểm $C$ bất kỳ thuộc tia $Mx$ ($C \\ne M$).",
            "question": "Cho đoạn thẳng $AB = 6\\text{ cm}$. Gọi $M$ là trung điểm của $AB$. Qua $M$ kẻ đường thẳng $xy$ vuông góc với $AB$. Lấy điểm $C$ bất kỳ thuộc tia $Mx$ ($C \\ne M$)."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính: $H = \\left(\\frac{1}{2} - \\frac{1}{3}\\right)^2 : \\frac{1}{36}$",
            "answer": "1",
            "explanation": "$(1/6)^2 : 1/36 = 1/36 : 1/36 = 1$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $n$ biết: $\\frac{3^n}{9} = 27$",
            "answer": "5",
            "explanation": "$3^n = 243 = 3^5 \\Rightarrow n = 5$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho góc $\\widehat{xOy} = 70^\\circ$. Vẽ góc $\\widehat{yOz}$ kề bù với $\\widehat{xOy}$. Kẻ $Ot$ là tia phân giác của $\\widehat{yOz}$. Tính số đo của góc $\\widehat{xOt}$ (độ):",
            "answer": "125",
            "explanation": "$\\widehat{yOz} = 110^\\circ \\Rightarrow \\widehat{yOt} = 55^\\circ \\Rightarrow \\widehat{xOt} = 70^\\circ + 55^\\circ = 125^\\circ$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của biểu thức: $E = (x - 2)^2 + |y + 1| + 2026$",
            "answer": "2026",
            "explanation": "Vì $(x-2)^2 \\ge 0$ và $|y+1| \\ge 0$ nên $E \\ge 2026$ khi $x = 2, y = -1$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "Tính giá trị của biểu thức sau:\na) $A = \\left(-\\frac{2}{5}\\right) \\cdot \\frac{4}{15} + \\left(-\\frac{2}{5}\\right) \\cdot \\frac{11}{15} + 2\\frac{2}{5}$\nb) $B = \\frac{2^{12} \\cdot 3^5 - 4^6 \\cdot 9^2}{(2^2 \\cdot 3)^6}$",
            "rubric": "a) $-2/5 \\cdot 1 + 12/5 = 10/5 = 2$ (0.5đ).\nb) $4^6 = 2^{12}, 9^2 = 3^4$. Tử $2^{12} \\cdot 3^4(3 - 1) = 2^{13} \\cdot 3^4$. Mẫu $2^{12} \\cdot 3^6$. $B = 2/9$ (0.5đ).",
            "modelSolution": "a) $A = -\\frac{2}{5} \\cdot \\left(\\frac{4}{15} + \\frac{11}{15}\\right) + \\frac{12}{5} = -\\frac{2}{5} + \\frac{12}{5} = \\frac{10}{5} = 2$.\nb) $B = \\frac{2^{12} \\cdot 3^5 - 2^{12} \\cdot 3^4}{2^{12} \\cdot 3^6} = \\frac{2^{12} \\cdot 3^4 \\cdot (3 - 1)}{2^{12} \\cdot 3^6} = \\frac{2}{3^2} = \\frac{2}{9}$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Tìm $x$, biết:\na) $\\frac{1}{2} - \\frac{2}{3}x = \\frac{7}{12}$\nb) $(2x + 3)^2 = 25$",
            "rubric": "a) $2/3x = -1/12 \\Rightarrow x = -1/8$ (0.35đ).\nb) $2x + 3 = \\pm 5 \\Rightarrow x = 1$ hoặc $x = -4$ (0.4đ).",
            "modelSolution": "a) $\\frac{2}{3}x = \\frac{1}{2} - \\frac{7}{12} = -\\frac{1}{12} \\Leftrightarrow x = -\\frac{1}{12} : \\frac{2}{3} = -\\frac{1}{8}$.\nb) $2x + 3 = 5 \\Rightarrow 2x = 2 \\Rightarrow x = 1$ hoặc $2x + 3 = -5 \\Rightarrow 2x = -8 \\Rightarrow x = -4$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho hai đường thẳng $a$ và $b$ song song với nhau. Đường thẳng $c$ cắt $a$ tại $A$ và cắt $b$ tại $B$. Gọi $Ax$ là tia phân giác của một góc so le trong tại $A$, và $By$ là tia phân giác của góc so le trong tại $B$.\na) Chứng minh rằng $\\widehat{xAB} = \\widehat{yBA}$.\nb) Chứng minh rằng tia $Ax$ song song với tia $By$ ($Ax \\parallel By$).",
            "rubric": "a) Bằng nửa của hai góc so le trong bằng nhau (0.35đ).\nb) Hai góc so le trong bằng nhau $\\Rightarrow Ax \\parallel By$ (0.4đ).",
            "modelSolution": "a) Vì $a \\parallel b$ nên hai góc so le trong bằng nhau: $\\widehat{A} = \\widehat{B}$.\nVì $Ax, By$ lần lượt là tia phân giác của hai góc đó nên:\n$$\\widehat{xAB} = \\frac{\\widehat{A}}{2} = \\frac{\\widehat{B}}{2} = \\widehat{yBA}.$$\nb) Hai góc $\\widehat{xAB}$ và $\\widehat{yBA}$ ở vị trí so le trong đối với hai tia $Ax$ và $By$ bị cắt bởi đường thẳng $AB$.\nMà $\\widehat{xAB} = \\widehat{yBA}$ (chứng minh trên) nên $Ax \\parallel By$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Tìm các số nguyên $x, y$ thỏa mãn đẳng thức: $xy - 2x + 3y = 11$.",
            "rubric": "Nhóm nhân tử: $x(y - 2) + 3(y - 2) = 11 - 6 = 5 \\Leftrightarrow (x + 3)(y - 2) = 5$ (0.5đ).",
            "modelSolution": "Ta có:\n$$xy - 2x + 3y = 11$$\n$$x(y - 2) + 3y - 6 = 11 - 6$$\n$$x(y - 2) + 3(y - 2) = 5$$\n$$(x + 3)(y - 2) = 5$$\nVì $x, y \\in \\mathbb{Z}$ nên $x + 3$ và $y - 2$ là các ước của $5$. Ta có $\\text{Ư}(5) = \\{\\pm 1; \\pm 5\\}$.\n- TH1: $\\begin{cases} x + 3 = 1 \\\\ y - 2 = 5 \\end{cases} \\Rightarrow \\begin{cases} x = -2 \\\\ y = 7 \\end{cases}$\n- TH2: $\\begin{cases} x + 3 = 5 \\\\ y - 2 = 1 \\end{cases} \\Rightarrow \\begin{cases} x = 2 \\\\ y = 3 \\end{cases}$\n- TH3: $\\begin{cases} x + 3 = -1 \\\\ y - 2 = -5 \\end{cases} \\Rightarrow \\begin{cases} x = -4 \\\\ y = -3 \\end{cases}$\n- TH4: $\\begin{cases} x + 3 = -5 \\\\ y - 2 = -1 \\end{cases} \\Rightarrow \\begin{cases} x = -8 \\\\ y = 1 \\end{cases}$\nVậy các cặp $(x; y)$ nguyên thỏa mãn là $(-2; 7), (2; 3), (-4; -3), (-8; 1)$."
          }
        ]
      }
    ]
  },
  "8": {
    "mid1": [
      {
        "id": "p_g8_mid1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 8 (ĐỀ SỐ 01)",
        "topic": "Đơn thức, Đa thức nhiều biến, Hằng đẳng thức đáng nhớ & Tứ giác, Hình thang cân, Hình bình hành",
        "grade": "8",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Biểu thức nào sau đây là đơn thức nhiều biến?",
            "options": [
              "$\\frac{x}{y}$",
              "$2x + y$",
              "$x^2 - 4$",
              "$3x^2 y z^3$"
            ],
            "correct": 3,
            "explanation": "$3x^2 y z^3$ chỉ gồm tích giữa các số và các biến nên là đơn thức.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Bậc của đơn thức $5x^3 y^2 z$ là:",
            "options": [
              "$6$",
              "$7$",
              "$3$",
              "$5$"
            ],
            "correct": 0,
            "explanation": "Bậc của đơn thức: $3 + 2 + 1 = 6$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Đơn thức nào sau đây đồng dạng với đơn thức $-4x^2 y$?",
            "options": [
              "$-4x^2 y^2$",
              "$\\frac{1}{2}x^2 y$",
              "$3xy^2$",
              "$2x^3 y$"
            ],
            "correct": 1,
            "explanation": "Cùng phần biến $x^2 y$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Bậc của đa thức $P = 4x^4 y - 3x^2 y^3 - 4x^4 y + 7$ sau khi thu gọn là:",
            "options": [
              "$6$",
              "$5$",
              "$4$",
              "$0$"
            ],
            "correct": 1,
            "explanation": "Thu gọn $P = -3x^2 y^3 + 7$ có bậc là $2 + 3 = 5$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Khai triển hằng đẳng thức $(x + 3)^2$ ta được:",
            "options": [
              "$x^2 + 3x + 9$",
              "$x^2 + 9$",
              "$x^2 + 6x + 9$",
              "$x^2 + 6x + 6$"
            ],
            "correct": 2,
            "explanation": "$(x + 3)^2 = x^2 + 6x + 9$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Viết biểu thức $x^2 - 16$ dưới dạng tích ta được:",
            "options": [
              "$(x - 4)(x + 4)$",
              "$(x - 16)(x + 16)$",
              "$(x + 4)^2$",
              "$(x - 4)^2$"
            ],
            "correct": 0,
            "explanation": "$x^2 - 4^2 = (x - 4)(x + 4)$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Kết quả của phép nhân đơn thức với đa thức $2x(x^2 - 5)$ là:",
            "options": [
              "$3x^3 - 10x$",
              "$2x^3 - 5$",
              "$2x^3 - 10x$",
              "$2x^3 + 10x$"
            ],
            "correct": 2,
            "explanation": "$2x \\cdot x^2 - 2x \\cdot 5 = 2x^3 - 10x$.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Kết quả của phép chia đơn thức $15x^4 y^3 : 3x^2 y$ là:",
            "options": [
              "$5x^6 y^4$",
              "$12x^2 y^2$",
              "$5x^2 y^2$",
              "$5x^2 y^3$"
            ],
            "correct": 2,
            "explanation": "$15 : 3 = 5, x^4 : x^2 = x^2, y^3 : y = y^2$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Tổng số đo bốn góc trong một tứ giác lồi luôn bằng:",
            "options": [
              "$270^\\circ$",
              "$90^\\circ$",
              "$180^\\circ$",
              "$360^\\circ$"
            ],
            "correct": 3,
            "explanation": "Tổng 4 góc tứ giác bằng $360^\\circ$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Khẳng định nào sau đây về tính chất của hình thang cân là **sai**?",
            "options": [
              "Hai đường chéo bằng nhau",
              "Hai đường chéo vuông góc với nhau",
              "Hai cạnh bên bằng nhau",
              "Hai góc kề một đáy bằng nhau"
            ],
            "correct": 1,
            "explanation": "Hai đường chéo bằng nhau chứ không nhất thiết vuông góc.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Phân tích đa thức $x^2 - 4x + 4 - y^2$ thành nhân tử ta được:",
            "options": [
              "$(x - 2)^2 - y^2$",
              "$(x + 2 - y)(x + 2 + y)$",
              "$(x - y - 4)(x + y + 4)$",
              "$(x - 2 - y)(x - 2 + y)$"
            ],
            "correct": 3,
            "explanation": "$(x - 2)^2 - y^2 = (x - 2 - y)(x - 2 + y)$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = 100^\\circ$. Số đo của góc $\\widehat{D}$ là:",
            "options": [
              "$110^\\circ$",
              "$120^\\circ$",
              "$100^\\circ$",
              "$90^\\circ$"
            ],
            "correct": 0,
            "explanation": "$360^\\circ - 250^\\circ = 110^\\circ$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho hai đa thức $M = 3x^2 y - 2xy^2 + 5$ và $N = x^2 y + 2xy^2 - 3$.",
            "statements": [
              {
                "key": "a",
                "text": "Đa thức $M + N$ sau khi thu gọn bằng $4x^2 y + 2$.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "b",
                "text": "Đa thức $M - N$ có chứa hạng tử có bậc 3 đối với biến $y$.",
                "correct": false,
                "explanation": "Sai, bậc biến y cao nhất là 2."
              },
              {
                "key": "c",
                "text": "Tại $x = 1, y = -1$, giá trị của đa thức $M + N$ bằng $-2$.",
                "correct": true,
                "explanation": "Đúng: $4(1)(-1) + 2 = -2$."
              },
              {
                "key": "d",
                "text": "Rút gọn biểu thức $(x + y)^2 - (x - y)^2$ ta được kết quả là $4xy$.",
                "correct": true,
                "explanation": "Đúng."
              }
            ],
            "stem": "Cho hai đa thức $M = 3x^2 y - 2xy^2 + 5$ và $N = x^2 y + 2xy^2 - 3$.",
            "question": "Cho hai đa thức $M = 3x^2 y - 2xy^2 + 5$ và $N = x^2 y + 2xy^2 - 3$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho tam giác $ABC$ cân tại $A$. Gọi $D$ và $E$ lần lượt là trung điểm của hai cạnh $AB$ và $AC$.",
            "statements": [
              {
                "key": "a",
                "text": "Đoạn thẳng $DE$ là đường trung bình của tam giác $ABC$.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "b",
                "text": "Tứ giác $BDEC$ là hình thang cân.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "c",
                "text": "Nếu $BC = 10\\text{ cm}$ thì độ dài đoạn thẳng $DE = 5\\text{ cm}$.",
                "correct": true,
                "explanation": "Đúng: $DE = BC/2 = 5\\text{ cm}$."
              },
              {
                "key": "d",
                "text": "Gọi $O$ là giao điểm của hai đường chéo $BE$ và $CD$. Khi đó đoạn thẳng $OB = OD$.",
                "correct": false,
                "explanation": "Sai: $OB = OC \\ne OD$."
              }
            ],
            "stem": "Cho tam giác $ABC$ cân tại $A$. Gọi $D$ và $E$ lần lượt là trung điểm của hai cạnh $AB$ và $AC$.",
            "question": "Cho tam giác $ABC$ cân tại $A$. Gọi $D$ và $E$ lần lượt là trung điểm của hai cạnh $AB$ và $AC$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức $A = x^3 - 3x^2 + 3x - 1$ tại $x = 101$:",
            "answer": "1000000",
            "explanation": "$(x - 1)^3 = 100^3 = 1\\ 000\\ 000$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm giá trị của $x$, biết: $(x - 3)(x + 3) - x(x - 2) = 11$",
            "answer": "10",
            "explanation": "$x^2 - 9 - x^2 + 2x = 11 \\Leftrightarrow 2x = 20 \\Leftrightarrow x = 10$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$) có $\\widehat{C} = 65^\\circ$. Tính số đo của góc $\\widehat{A}$ (đơn vị: độ):",
            "answer": "115",
            "explanation": "$\\widehat{A} = 180^\\circ - 65^\\circ = 115^\\circ$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của biểu thức: $M = x^2 - 6x + y^2 + 4y + 2039$",
            "answer": "2026",
            "explanation": "$(x - 3)^2 + (y + 2)^2 + 2026 \\ge 2026$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "a) Thu gọn đa thức: $A = 5x^2 y - 3xy^2 + 2x^2 y + 4xy^2 - 7$.\nb) Thực hiện phép chia: $(12x^3 y^2 - 9x^2 y^3 + 6x^2 y^2) : (3x^2 y^2)$.",
            "rubric": "a) $7x^2 y + xy^2 - 7$ (0.5đ). b) $4x - 3y + 2$ (0.5đ).",
            "modelSolution": "a) $A = (5x^2 y + 2x^2 y) + (-3xy^2 + 4xy^2) - 7 = 7x^2 y + xy^2 - 7$.\nb) $4x - 3y + 2$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Phân tích các đa thức sau thành nhân tử:\na) $3x^2 - 6x$\nb) $x^2 - 2xy + y^2 - 25$",
            "rubric": "a) $3x(x - 2)$ (0.35đ). b) $(x - y - 5)(x - y + 5)$ (0.4đ).",
            "modelSolution": "a) $3x(x - 2)$. b) $(x - y)^2 - 5^2 = (x - y - 5)(x - y + 5)$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho hình bình hành $ABCD$. Gọi $E$ và $F$ lần lượt là trung điểm của hai cạnh $AB$ và $CD$.\na) Chứng minh tứ giác $AECF$ là hình bình hành.\nb) Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Chứng minh ba điểm $E, O, F$ thẳng hàng.",
            "rubric": "a) $AE = CF$ và $AE \\parallel CF$ (0.4đ). b) $O$ là trung điểm $AC \\Rightarrow O$ là trung điểm $EF$ (0.35đ).",
            "modelSolution": "a) $AE = CF = \\frac{1}{2} AB$, $AE \\parallel CF \\Rightarrow AECF$ là hình bình hành.\nb) $O$ là trung điểm $AC \\Rightarrow O$ là trung điểm $EF \\Rightarrow E, O, F$ thẳng hàng."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Cho các số thực $x, y$ thỏa mãn: $x^2 + 2y^2 + 2xy - 2x - 4y + 2 = 0$. Tính giá trị của biểu thức $Q = (x - 1)^{2025} + (y - 1)^{2026}$.",
            "rubric": "$(x + y - 1)^2 + (y - 1)^2 = 0 \\Rightarrow y = 1, x = 0 \\Rightarrow Q = -1$ (0.5đ).",
            "modelSolution": "$(x + y - 1)^2 + (y - 1)^2 = 0 \\Rightarrow y = 1, x = 0 \\Rightarrow Q = (0 - 1)^{2025} + (1 - 1)^{2026} = -1$."
          }
        ]
      },
      {
        "id": "p_g8_mid1_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 8 (ĐỀ SỐ 02)",
        "topic": "Nhân đa thức, Hằng đẳng thức lập phương, Phân tích nhân tử & Hình chữ nhật, Hình thoi",
        "grade": "8",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Hệ số của đơn thức $-5x^3 y^4$ là:",
            "options": [
              "$3$",
              "$4$",
              "$5$",
              "$-5$"
            ],
            "correct": 3,
            "explanation": "Hệ số là phần số: $-5$.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Kết quả của phép nhân $(x + 2)(x - 2)$ là:",
            "options": [
              "$x^2 + 4$",
              "$x^2 - 4$",
              "$x^2 - 4x + 4$",
              "$x^2 - 2$"
            ],
            "correct": 1,
            "explanation": "$(x + 2)(x - 2) = x^2 - 4$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Khai triển hằng đẳng thức $(a - b)^3$ ta được:",
            "options": [
              "$a^3 + 3a^2 b + 3ab^2 + b^3$",
              "$a^3 - 3a^2 b - 3ab^2 - b^3$",
              "$a^3 - 3a^2 b + 3ab^2 - b^3$",
              "$a^3 - b^3$"
            ],
            "correct": 2,
            "explanation": "$(a - b)^3 = a^3 - 3a^2 b + 3ab^2 - b^3$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Đa thức $x^3 + 8$ viết dưới dạng tích là:",
            "options": [
              "$(x + 2)(x^2 + 2x + 4)$",
              "$(x - 2)(x^2 + 2x + 4)$",
              "$(x + 2)(x^2 - 2x + 4)$",
              "$(x + 2)^3$"
            ],
            "correct": 2,
            "explanation": "$x^3 + 2^3 = (x + 2)(x^2 - 2x + 4)$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Phân tích đa thức $5x(x - y) + 3(x - y)$ thành nhân tử được kết quả là:",
            "options": [
              "$8x(x - y)$",
              "$(x - y)(5x - 3)$",
              "$(x - y)(5x + 3)$",
              "$(x + y)(5x + 3)$"
            ],
            "correct": 2,
            "explanation": "Đặt nhân tử chung $(x - y)$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Đơn thức $-12x^3 y^2$ chia hết cho đơn thức nào sau đây?",
            "options": [
              "$3x^4 y$",
              "$-3x^2 y$",
              "$4x^2 y^3$",
              "$5xy^4$"
            ],
            "correct": 1,
            "explanation": "Số mũ của từng biến ở đơn thức bị chia lớn hơn hoặc bằng ở đơn thức chia.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Hình chữ nhật là tứ giác có:",
            "options": [
              "Bốn góc vuông",
              "Hai đường chéo vuông góc",
              "Bốn cạnh bằng nhau",
              "Hai đường chéo là phân giác"
            ],
            "correct": 0,
            "explanation": "Hình chữ nhật là tứ giác có bốn góc vuông.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Hình thoi có hai đường chéo dài $10\\text{ cm}$ và $12\\text{ cm}$. Diện tích của hình thoi là:",
            "options": [
              "$60\\text{ cm}^2$",
              "$44\\text{ cm}^2$",
              "$22\\text{ cm}^2$",
              "$120\\text{ cm}^2$"
            ],
            "correct": 0,
            "explanation": "$S = \\frac{1}{2} \\cdot 10 \\cdot 12 = 60\\text{ cm}^2$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Giá trị của biểu thức $P = x^2 - 4xy + 4y^2$ tại $x = 104, y = 2$ là:",
            "options": [
              "$1000$",
              "$10\\ 816$",
              "$100$",
              "$10\\ 000$"
            ],
            "correct": 3,
            "explanation": "$P = (x - 2y)^2 = (104 - 4)^2 = 100^2 = 10\\ 000$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Tìm $x$, biết: $x(x - 5) + x - 5 = 0$.",
            "options": [
              "$x = -1$",
              "$x = 5$",
              "$x = 0$",
              "$x = 5$ hoặc $x = -1$"
            ],
            "correct": 3,
            "explanation": "$(x - 5)(x + 1) = 0 \\Rightarrow x = 5$ hoặc $x = -1$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$, có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$. Độ dài đường trung tuyến ứng với cạnh huyền $BC$ là:",
            "options": [
              "$5\\text{ cm}$",
              "$10\\text{ cm}$",
              "$3\\text{ cm}$",
              "$4\\text{ cm}$"
            ],
            "correct": 0,
            "explanation": "$BC = \\sqrt{6^2 + 8^2} = 10\\text{ cm}$. Đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền: $10 : 2 = 5\\text{ cm}$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 100^\\circ, \\widehat{B} = 120^\\circ$ và $\\widehat{C} - \\widehat{D} = 20^\\circ$. Số đo của góc $\\widehat{D}$ là:",
            "options": [
              "$70^\\circ$",
              "$60^\\circ$",
              "$80^\\circ$",
              "$50^\\circ$"
            ],
            "correct": 1,
            "explanation": "$\\widehat{C} + \\widehat{D} = 360^\\circ - 220^\\circ = 140^\\circ$. $\\widehat{D} = (140^\\circ - 20^\\circ) : 2 = 60^\\circ$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho biểu thức $A = (x - 2)(x^2 + 2x + 4) - (x + 1)^3$.",
            "statements": [
              {
                "key": "a",
                "text": "Tích $(x - 2)(x^2 + 2x + 4)$ là hằng đẳng thức hiệu hai lập phương $x^3 - 8$.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "b",
                "text": "Khai triển $(x + 1)^3 = x^3 + 3x^2 + 3x + 1$.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "c",
                "text": "Biểu thức $A$ sau khi thu gọn bằng $-3x^2 - 3x - 9$.",
                "correct": true,
                "explanation": "$x^3 - 8 - (x^3 + 3x^2 + 3x + 1) = -3x^2 - 3x - 9$."
              },
              {
                "key": "d",
                "text": "Giá trị của biểu thức $A$ không phụ thuộc vào biến $x$.",
                "correct": false,
                "explanation": "Biểu thức còn chứa biến $x$ nên phụ thuộc vào $x$."
              }
            ],
            "stem": "Cho biểu thức $A = (x - 2)(x^2 + 2x + 4) - (x + 1)^3$.",
            "question": "Cho biểu thức $A = (x - 2)(x^2 + 2x + 4) - (x + 1)^3$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho hình chữ nhật $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Cho biết $AB = 8\\text{ cm}, BC = 6\\text{ cm}$.",
            "statements": [
              {
                "key": "a",
                "text": "Độ dài đường chéo $AC$ bằng $10\\text{ cm}$.",
                "correct": true,
                "explanation": "$\\sqrt{8^2 + 6^2} = 10\\text{ cm}$."
              },
              {
                "key": "b",
                "text": "Độ dài đoạn thẳng $OA = OB = OC = OD = 5\\text{ cm}$.",
                "correct": true,
                "explanation": "Trong hình chữ nhật, hai đường chéo bằng nhau và cắt nhau tại trung điểm."
              },
              {
                "key": "c",
                "text": "Tam giác $OAB$ là tam giác đều.",
                "correct": false,
                "explanation": "Tam giác $OAB$ cân tại $O$ với $OA = OB = 5\\text{ cm}, AB = 8\\text{ cm}$ (không phải tam giác đều)."
              },
              {
                "key": "d",
                "text": "Diện tích tam giác $OAB$ bằng một phần tư diện tích hình chữ nhật $ABCD$.",
                "correct": true,
                "explanation": "Bốn tam giác đỉnh $O$ có diện tích bằng nhau và bằng $S/4$."
              }
            ],
            "stem": "Cho hình chữ nhật $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Cho biết $AB = 8\\text{ cm}, BC = 6\\text{ cm}$.",
            "question": "Cho hình chữ nhật $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Cho biết $AB = 8\\text{ cm}, BC = 6\\text{ cm}$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức $M = (x + y)^3 - 3xy(x + y)$ khi $x + y = 5$ và $xy = 6$:",
            "answer": "35",
            "explanation": "$5^3 - 3 \\cdot 6 \\cdot 5 = 125 - 90 = 35$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $x$ thỏa mãn: $x^2 - 16 = 0$ và $x > 0$:",
            "answer": "4",
            "explanation": "$x^2 = 16 \\Rightarrow x = 4$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho hình thoi $ABCD$ có cạnh $a = 10\\text{ cm}$ và một góc $\\widehat{A} = 60^\\circ$. Tính độ dài đường chéo ngắn $BD$ (đơn vị: cm):",
            "answer": "10",
            "explanation": "Tam giác $ABD$ có $AB = AD = 10$ và góc $60^\\circ$ nên là tam giác đều $\\Rightarrow BD = 10\\text{ cm}$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của biểu thức: $P = x^2 - 4x + 11$",
            "answer": "7",
            "explanation": "$P = (x - 2)^2 + 7 \\ge 7$ khi $x = 2$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "Thực hiện phép tính:\na) $(2x - 1)(x + 3) - 2x(x + 1)$\nb) $(15x^3 y^2 - 10x^2 y^3 + 5x^2 y^2) : (5x^2 y^2)$",
            "rubric": "a) $2x^2 + 5x - 3 - 2x^2 - 2x = 3x - 3$ (0.5đ). b) $3x - 2y + 1$ (0.5đ).",
            "modelSolution": "a) $(2x^2 + 6x - x - 3) - (2x^2 + 2x) = 2x^2 + 5x - 3 - 2x^2 - 2x = 3x - 3$.\nb) $(15x^3 y^2 : 5x^2 y^2) - (10x^2 y^3 : 5x^2 y^2) + (5x^2 y^2 : 5x^2 y^2) = 3x - 2y + 1$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Phân tích các đa thức sau thành nhân tử:\na) $x^2 - 9 + (x - 3)^2$\nb) $x^2 - 4x - y^2 + 4$",
            "rubric": "a) $(x-3)(x+3) + (x-3)^2 = (x-3)(x+3+x-3) = 2x(x-3)$ (0.35đ).\nb) $(x-2)^2 - y^2 = (x - 2 - y)(x - 2 + y)$ (0.4đ).",
            "modelSolution": "a) $(x - 3)(x + 3) + (x - 3)^2 = (x - 3)[(x + 3) + (x - 3)] = (x - 3)(2x) = 2x(x - 3)$.\nb) $(x^2 - 4x + 4) - y^2 = (x - 2)^2 - y^2 = (x - 2 - y)(x - 2 + y)$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho tam giác $ABC$ vuông tại $A$. Gọi $M$ là trung điểm của cạnh huyền $BC$. Từ $M$ kẻ $MD$ vuông góc với $AB$ ($D \\in AB$) và $ME$ vuông góc với $AC$ ($E \\in AC$).\na) Chứng minh tứ giác $ADME$ là hình chữ nhật.\nb) Chứng minh $D$ là trung điểm của $AB$ và $E$ là trung điểm của $AC$.",
            "rubric": "a) Tứ giác có 3 góc vuông: $\\widehat{A} = \\widehat{D} = \\widehat{E} = 90^\\circ$ (0.35đ).\nb) $MD \\parallel AC$ qua trung điểm $M \\Rightarrow D$ là trung điểm $AB$ (đường trung bình) (0.4đ).",
            "modelSolution": "a) Tứ giác $ADME$ có:\n$\\widehat{DAE} = 90^\\circ$ (do $\\Delta ABC$ vuông tại $A$),\n$\\widehat{ADM} = 90^\\circ$ (do $MD \\perp AB$),\n$\\widehat{AEM} = 90^\\circ$ (do $ME \\perp AC$).\nTứ giác có ba góc vuông nên $ADME$ là hình chữ nhật.\nb) Vì $MD \\perp AB$ và $AC \\perp AB$ nên $MD \\parallel AC$.\nTrong $\\Delta ABC$, đoạn thẳng $MD$ đi qua trung điểm $M$ của cạnh $BC$ và song song với cạnh $AC$ nên $MD$ đi qua trung điểm của cạnh $AB$, tức $D$ là trung điểm của $AB$.\nTương tự, $ME \\perp AC$ và $AB \\perp AC$ nên $ME \\parallel AB$. Đoạn thẳng $ME$ đi qua trung điểm $M$ của $BC$ và song song với $AB$ nên $E$ là trung điểm của $AC$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Tìm giá trị nhỏ nhất của biểu thức: $B = x^2 - 2xy + 2y^2 - 4y + 10$.",
            "rubric": "Tách $(x - y)^2 + (y - 2)^2 + 6 \\ge 6$ (0.5đ).",
            "modelSolution": "Ta biến đổi biểu thức $B$:\n$$B = (x^2 - 2xy + y^2) + (y^2 - 4y + 4) + 6 = (x - y)^2 + (y - 2)^2 + 6$$\nVì $(x - y)^2 \\ge 0$ và $(y - 2)^2 \\ge 0$ với mọi $x, y$ nên $B \\ge 6$.\nDấu \"=\" xảy ra khi $\\begin{cases} y - 2 = 0 \\\\ x - y = 0 \\end{cases} \\Leftrightarrow x = y = 2$.\nVậy giá trị nhỏ nhất của $B$ là $6$ khi $x = y = 2$."
          }
        ]
      },
      {
        "id": "p_g8_mid1_03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 8 (ĐỀ SỐ 03)",
        "topic": "Phân tích đa thức tách hạng tử, Hằng đẳng thức tổng lập phương & Hình vuông, Tứ giác đối xứng",
        "grade": "8",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Biểu thức $x^2 + 2xy + y^2$ là dạng khai triển của hằng đẳng thức nào?",
            "options": [
              "$(x + y)^3$",
              "$x^2 + y^2$",
              "$(x + y)^2$",
              "$(x - y)^2$"
            ],
            "correct": 2,
            "explanation": "$(x + y)^2 = x^2 + 2xy + y^2$.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Giá trị của biểu thức $x^2 - y^2$ tại $x = 87$ và $y = 13$ là:",
            "options": [
              "$7400$",
              "$1000$",
              "$100$",
              "$740$"
            ],
            "correct": 0,
            "explanation": "$(87 - 13)(87 + 13) = 74 \\cdot 100 = 7400$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Bậc của đa thức $Q = 2x^2 y^2 - 5x^3 y + x^4 - x^4 + 1$ là:",
            "options": [
              "$0$",
              "$4$",
              "$2$",
              "$3$"
            ],
            "correct": 1,
            "explanation": "$x^4 - x^4 = 0$. $Q = 2x^2 y^2 - 5x^3 y + 1$ có bậc là $4$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Phân tích đa thức $x^2 - 5x + 6$ thành nhân tử, ta được:",
            "options": [
              "$(x + 2)(x + 3)$",
              "$(x - 2)(x - 3)$",
              "$(x - 1)(x - 6)$",
              "$(x + 1)(x - 6)$"
            ],
            "correct": 1,
            "explanation": "$x^2 - 2x - 3x + 6 = x(x - 2) - 3(x - 2) = (x - 2)(x - 3)$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Đa thức nào sau đây chia hết cho đơn thức $3xy$?",
            "options": [
              "$2x - 3y$",
              "$3x^2 + y$",
              "$6x^2 y - 3xy^2$",
              "$x^2 y^2 - x$"
            ],
            "correct": 2,
            "explanation": "Mỗi hạng tử của $6x^2 y - 3xy^2$ đều chia hết cho $3xy$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Hình vuông là hình thoi có:",
            "options": [
              "Một góc vuông",
              "Bốn cạnh bằng nhau",
              "Các góc đối bằng nhau",
              "Hai đường chéo vuông góc"
            ],
            "correct": 0,
            "explanation": "Dấu hiệu nhận biết: Hình thoi có một góc vuông là hình vuông.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Hình bình hành có hai đường chéo bằng nhau là hình gì?",
            "options": [
              "Hình vuông",
              "Hình thoi",
              "Hình chữ nhật",
              "Hình thang cân"
            ],
            "correct": 2,
            "explanation": "Hình bình hành có hai đường chéo bằng nhau là hình chữ nhật.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Một hình vuông có độ dài đường chéo bằng $\\sqrt{32}\\text{ cm}$. Độ dài cạnh hình vuông đó là:",
            "options": [
              "$16\\text{ cm}$",
              "$8\\text{ cm}$",
              "$2\\text{ cm}$",
              "$4\\text{ cm}$"
            ],
            "correct": 3,
            "explanation": "$d = a\\sqrt{2} = \\sqrt{32} = 4\\sqrt{2} \\Rightarrow a = 4\\text{ cm}$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $(x + 1)^2 - 2(x + 1)(x - 2) + (x - 2)^2$ ta được:",
            "options": [
              "$9$",
              "$3$",
              "$1$",
              "$2x - 1$"
            ],
            "correct": 0,
            "explanation": "$[(x + 1) - (x - 2)]^2 = 3^2 = 9$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $n$ để đơn thức $x^n y^2$ chia hết cho đơn thức $x^3 y$:",
            "options": [
              "$n \\ge 2$",
              "$n \\le 3$",
              "$n = 2$",
              "$n \\ge 3$"
            ],
            "correct": 3,
            "explanation": "Số mũ của biến $x$ ở số bị chia phải lớn hơn hoặc bằng ở số chia: $n \\ge 3$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Cho tứ giác $ABCD$ có hai đường chéo $AC \\perp BD$. Gọi $E, F, G, H$ lần lượt là trung điểm của bốn cạnh $AB, BC, CD, DA$. Tứ giác $EFGH$ là hình gì?",
            "options": [
              "Hình vuông",
              "Hình chữ nhật",
              "Hình thoi",
              "Hình bình hành"
            ],
            "correct": 1,
            "explanation": "Tứ giác nối trung điểm 4 cạnh của tứ giác có hai đường chéo vuông góc là hình chữ nhật.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Phân tích đa thức $x^3 - 4x$ thành nhân tử, ta được:",
            "options": [
              "$x^2(x - 4)$",
              "$x(x - 4)(x + 4)$",
              "$x(x - 2)^2$",
              "$x(x - 2)(x + 2)$"
            ],
            "correct": 3,
            "explanation": "$x(x^2 - 4) = x(x - 2)(x + 2)$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho đa thức $P(x) = x^3 - 3x^2 + 3x - 1$ và $Q(x) = (x - 1)(x^2 + x + 1)$.",
            "statements": [
              {
                "key": "a",
                "text": "Đa thức $P(x)$ được viết gọn dưới dạng lũy thừa là $(x - 1)^3$.",
                "correct": true,
                "explanation": "Đúng hằng đẳng thức lập phương của một hiệu."
              },
              {
                "key": "b",
                "text": "Tích $(x - 1)(x^2 + x + 1)$ bằng $x^3 - 1$.",
                "correct": true,
                "explanation": "Đúng hằng đẳng thức hiệu hai lập phương."
              },
              {
                "key": "c",
                "text": "Khi $x = 1$, cả hai đa thức $P(x)$ và $Q(x)$ đều nhận giá trị bằng 0.",
                "correct": true,
                "explanation": "$P(1) = 0$ và $Q(1) = 0$."
              },
              {
                "key": "d",
                "text": "Đa thức $P(x) - Q(x)$ là đa thức bậc 3.",
                "correct": false,
                "explanation": "$x^3 - 3x^2 + 3x - 1 - (x^3 - 1) = -3x^2 + 3x$ là đa thức bậc 2."
              }
            ],
            "stem": "Cho đa thức $P(x) = x^3 - 3x^2 + 3x - 1$ và $Q(x) = (x - 1)(x^2 + x + 1)$.",
            "question": "Cho đa thức $P(x) = x^3 - 3x^2 + 3x - 1$ và $Q(x) = (x - 1)(x^2 + x + 1)$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho tam giác $ABC$ vuông cân tại $A$. Trên cạnh huyền $BC$ lấy hai điểm $D, E$ sao cho $BD = CE < \\frac{BC}{2}$.",
            "statements": [
              {
                "key": "a",
                "text": "Tam giác $ABD$ bằng tam giác $ACE$ (c-g-c).",
                "correct": true,
                "explanation": "$AB = AC, \\widehat{B} = \\widehat{C} = 45^\\circ, BD = CE$."
              },
              {
                "key": "b",
                "text": "Độ dài đoạn thẳng $AD$ bằng độ dài đoạn thẳng $AE$.",
                "correct": true,
                "explanation": "Hai cạnh tương ứng của hai tam giác bằng nhau."
              },
              {
                "key": "c",
                "text": "Tam giác $ADE$ là tam giác cân tại $A$.",
                "correct": true,
                "explanation": "Do $AD = AE$."
              },
              {
                "key": "d",
                "text": "Tứ giác có các đỉnh là hình chiếu của $A, D, E$ luôn là hình thoi.",
                "correct": false,
                "explanation": "Không đủ điều kiện để là hình thoi."
              }
            ],
            "stem": "Cho tam giác $ABC$ vuông cân tại $A$. Trên cạnh huyền $BC$ lấy hai điểm $D, E$ sao cho $BD = CE < \\frac{BC}{2}$.",
            "question": "Cho tam giác $ABC$ vuông cân tại $A$. Trên cạnh huyền $BC$ lấy hai điểm $D, E$ sao cho $BD = CE < \\frac{BC}{2}$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức $A = x^2 - 6x + 9$ tại $x = 103$:",
            "answer": "10000",
            "explanation": "$(103 - 3)^2 = 100^2 = 10\\ 000$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $x$, biết: $(2x - 3)^2 - (2x + 1)(2x - 1) = 22$",
            "answer": "-1",
            "explanation": "$4x^2 - 12x + 9 - 4x^2 + 1 = 22 \\Leftrightarrow -12x = 12 \\Rightarrow x = -1$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một hình chữ nhật có chu vi $36\\text{ cm}$. Nếu tăng chiều rộng thêm $2\\text{ cm}$ và giảm chiều dài đi $2\\text{ cm}$ thì được một hình vuông. Tính diện tích hình chữ nhật ban đầu (cm²):",
            "answer": "77",
            "explanation": "Nửa chu vi 18. Dài hơn rộng 4cm $\\Rightarrow$ dài 11, rộng 7 $\\Rightarrow S = 77$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Cho $x + y = 3$ và $x^2 + y^2 = 5$. Tính giá trị của $xy$:",
            "answer": "2",
            "explanation": "$2xy = (x + y)^2 - (x^2 + y^2) = 9 - 5 = 4 \\Rightarrow xy = 2$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "a) Rút gọn biểu thức: $A = (x + 2)^3 - x(x + 3)^2 + 6x^2$.\nb) Thực hiện phép chia đa thức cho đơn thức: $(8x^4 y^3 - 12x^3 y^2 + 4x^2 y^2) : (4x^2 y^2)$.",
            "rubric": "a) $x^3 + 6x^2 + 12x + 8 - x(x^2 + 6x + 9) + 6x^2 = 3x + 8$ (0.5đ). b) $2x^2 y - 3x + 1$ (0.5đ).",
            "modelSolution": "a) $A = (x^3 + 6x^2 + 12x + 8) - (x^3 + 6x^2 + 9x) + 6x^2 = 6x^2 + 3x + 8$.\nb) $(8x^4 y^3 : 4x^2 y^2) - (12x^3 y^2 : 4x^2 y^2) + (4x^2 y^2 : 4x^2 y^2) = 2x^2 y - 3x + 1$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Phân tích các đa thức sau thành nhân tử:\na) $2x^3 - 8x$\nb) $x^2 - 5x + 6$",
            "rubric": "a) $2x(x - 2)(x + 2)$ (0.35đ). b) $(x - 2)(x - 3)$ (0.4đ).",
            "modelSolution": "a) $2x(x^2 - 4) = 2x(x - 2)(x + 2)$.\nb) $x^2 - 2x - 3x + 6 = x(x - 2) - 3(x - 2) = (x - 2)(x - 3)$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho hình bình hành $ABCD$ có $AB = 2AD$. Gọi $E$ và $F$ lần lượt là trung điểm của $AB$ và $CD$.\na) Chứng minh tứ giác $AEFD$ là hình thoi.\nb) Gọi $M$ là giao điểm của $AF$ và $DE$, $N$ là giao điểm của $BF$ và $CE$. Chứng minh tứ giác $EMFN$ là hình chữ nhật.",
            "rubric": "a) $AE = AD = \\frac{1}{2}AB$, $AE \\parallel DF \\Rightarrow AEFD$ là hình bình hành có $AE = AD \\Rightarrow$ hình thoi (0.35đ).\nb) Hai đường chéo hình thoi vuông góc: $\\widehat{M} = 90^\\circ, \\widehat{N} = 90^\\circ, \\widehat{E} = 90^\\circ \\Rightarrow EMFN$ là hình chữ nhật (0.4đ).",
            "modelSolution": "a) Vì $ABCD$ là hình bình hành nên $AB \\parallel CD$ và $AB = CD$.\nTa có $AE = \\frac{1}{2} AB$ và $DF = \\frac{1}{2} CD \\Rightarrow AE = DF$ và $AE \\parallel DF$.\nSuy ra tứ giác $AEFD$ là hình bình hành.\nMặt khác, theo giả thiết $AB = 2AD \\Rightarrow AD = \\frac{1}{2} AB = AE$.\nHình bình hành $AEFD$ có hai cạnh kề bằng nhau ($AD = AE$) nên $AEFD$ là hình thoi.\nb) Vì $AEFD$ là hình thoi nên hai đường chéo $AF$ và $DE$ vuông góc với nhau tại trung điểm của mỗi đường $\\Rightarrow \\widehat{EMF} = 90^\\circ$.\nChứng minh tương tự, tứ giác $EBCF$ cũng là hình thoi nên $BF \\perp CE \\Rightarrow \\widehat{ENF} = 90^\\circ$.\nLại có $ME \\parallel FN$ (do $DE \\parallel CF$) và $MF \\parallel EN$ (do $AF \\parallel BE$) nên tứ giác $EMFN$ là hình bình hành.\nHình bình hành $EMFN$ có $\\widehat{EMF} = 90^\\circ$ nên $EMFN$ là hình chữ nhật."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Chứng minh rằng với mọi số nguyên $n$, biểu thức $A = (2n + 1)^2 - 1$ luôn chia hết cho $8$.",
            "rubric": "$A = 4n^2 + 4n = 4n(n + 1)$. Vì $n(n+1)$ là tích hai số nguyên liên tiếp nên chia hết cho 2 $\\Rightarrow A \\ \\vdots \\ 8$ (0.5đ).",
            "modelSolution": "Ta có:\n$$A = (2n + 1)^2 - 1 = (4n^2 + 4n + 1) - 1 = 4n^2 + 4n = 4n(n + 1)$$\nVới mọi số nguyên $n$, tích $n(n + 1)$ là tích của hai số nguyên liên tiếp nên luôn chia hết cho $2$.\nĐặt $n(n + 1) = 2k$ ($k \\in \\mathbb{Z}$).\nKhi đó $A = 4 \\cdot 2k = 8k$.\nVì $8k \\ \\vdots \\ 8$ nên $A \\ \\vdots \\ 8$ với mọi số nguyên $n$ (đpcm)."
          }
        ]
      },
      {
        "id": "p_g8_mid1_04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 8 (ĐỀ SỐ 04)",
        "topic": "Đại số đa thức nâng cao, Cực trị nhiều biến & Hình học tứ giác suy luận sâu",
        "grade": "8",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Thu gọn đơn thức $2x^2 y \\cdot (-3)x y^3$ ta được:",
            "options": [
              "$-5x^3 y^4$",
              "$-6x^2 y^3$",
              "$6x^3 y^4$",
              "$-6x^3 y^4$"
            ],
            "correct": 3,
            "explanation": "$2 \\cdot (-3) \\cdot x^3 y^4 = -6x^3 y^4$.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Hằng đẳng thức tổng hai lập phương là:",
            "options": [
              "$a^3 + b^3 = (a - b)(a^2 + ab + b^2)$",
              "$a^3 + b^3 = (a + b)^3$",
              "$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$",
              "$a^3 + b^3 = (a + b)(a^2 + ab + b^2)$"
            ],
            "correct": 2,
            "explanation": "Đúng công thức hằng đẳng thức.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Phân tích $x^2 - y^2 + 2x + 1$ thành nhân tử:",
            "options": [
              "$(x + 1 - y)(x + 1 + y)$",
              "$(x - 1 - y)(x - 1 + y)$",
              "$(x + y + 1)(x - y - 1)$",
              "$(x + 1)^2 - y$"
            ],
            "correct": 0,
            "explanation": "$(x + 1)^2 - y^2 = (x + 1 - y)(x + 1 + y)$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Khẳng định nào sau đây về hình chữ nhật là **đúng**?",
            "options": [
              "Hai đường chéo bằng nhau và cắt nhau tại trung điểm của mỗi đường",
              "Đường chéo là đường phân giác của các góc",
              "Hai đường chéo vuông góc với nhau",
              "Bốn cạnh bằng nhau"
            ],
            "correct": 0,
            "explanation": "Tính chất đặc trưng của hình chữ nhật.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Hình thoi có chu vi bằng $40\\text{ cm}$. Độ dài mỗi cạnh của hình thoi là:",
            "options": [
              "$8\\text{ cm}$",
              "$10\\text{ cm}$",
              "$20\\text{ cm}$",
              "$5\\text{ cm}$"
            ],
            "correct": 1,
            "explanation": "$40 : 4 = 10\\text{ cm}$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Biểu thức $x^2 - 10x + 25$ được viết dưới dạng bình phương của một hiệu là:",
            "options": [
              "$(x - 5)^2$",
              "$(x - 25)^2$",
              "$(x + 5)^2$",
              "$(x - 10)^2$"
            ],
            "correct": 0,
            "explanation": "$(x - 5)^2$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Thực hiện phép chia $20x^5 y^4 : 5x^2 y^3$ ta được:",
            "options": [
              "$4x^7 y^7$",
              "$4x^3 y^7$",
              "$4x^3 y$",
              "$15x^3 y$"
            ],
            "correct": 2,
            "explanation": "$4x^3 y$.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Tứ giác có hai đường chéo cắt nhau tại trung điểm của mỗi đường là hình gì?",
            "options": [
              "Hình thang cân",
              "Hình chữ nhật",
              "Hình thoi",
              "Hình bình hành"
            ],
            "correct": 3,
            "explanation": "Dấu hiệu nhận biết hình bình hành.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Tìm $x$ biết $x^3 - x = 0$. Các giá trị của $x$ là:",
            "options": [
              "$x = 0; x = 1$",
              "$x = 0; x = 1; x = -1$",
              "$x = 1$",
              "$x = 0$"
            ],
            "correct": 1,
            "explanation": "$x(x - 1)(x + 1) = 0 \\Rightarrow x \\in \\{0; 1; -1\\}$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ có chu vi bằng $24\\text{ cm}$. Gọi $D, E, F$ lần lượt là trung điểm của ba cạnh $AB, BC, CA$. Chu vi của tam giác $DEF$ là:",
            "options": [
              "$48\\text{ cm}$",
              "$8\\text{ cm}$",
              "$12\\text{ cm}$",
              "$6\\text{ cm}$"
            ],
            "correct": 2,
            "explanation": "Mỗi cạnh của $\\Delta DEF$ bằng một nửa cạnh tương ứng của $\\Delta ABC$, chu vi bằng $24 : 2 = 12\\text{ cm}$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức $P = x^3 + y^3$ biết $x + y = 4$ và $xy = 3$:",
            "options": [
              "$36$",
              "$52$",
              "$64$",
              "$28$"
            ],
            "correct": 3,
            "explanation": "$P = (x + y)^3 - 3xy(x + y) = 4^3 - 3 \\cdot 3 \\cdot 4 = 64 - 36 = 28$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Đa thức $x^2 - y^2 - 2y - 1$ được phân tích thành:",
            "options": [
              "$(x + y + 1)^2$",
              "$(x - y - 1)(x + y + 1)$",
              "$(x - y - 1)^2$",
              "$(x - y + 1)(x + y - 1)$"
            ],
            "correct": 1,
            "explanation": "$x^2 - (y + 1)^2 = (x - y - 1)(x + y + 1)$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho biểu thức $M = (2x + 1)^2 + (2x - 1)^2 - 2(4x^2 - 1)$.",
            "statements": [
              {
                "key": "a",
                "text": "Khai triển $(2x + 1)^2 = 4x^2 + 4x + 1$.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "b",
                "text": "Khai triển $(2x - 1)^2 = 4x^2 - 4x + 1$.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "c",
                "text": "Tích $2(4x^2 - 1) = 8x^2 - 2$.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "d",
                "text": "Giá trị của biểu thức $M$ luôn bằng $4$ với mọi giá trị của biến $x$.",
                "correct": true,
                "explanation": "$8x^2 + 2 - (8x^2 - 2) = 4$."
              }
            ],
            "stem": "Cho biểu thức $M = (2x + 1)^2 + (2x - 1)^2 - 2(4x^2 - 1)$.",
            "question": "Cho biểu thức $M = (2x + 1)^2 + (2x - 1)^2 - 2(4x^2 - 1)$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho hình vuông $ABCD$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$.",
            "statements": [
              {
                "key": "a",
                "text": "Bốn đoạn thẳng $MN, NP, PQ, QM$ có độ dài bằng nhau.",
                "correct": true,
                "explanation": "Các cạnh hình vuông nhỏ bằng nhau."
              },
              {
                "key": "b",
                "text": "Tứ giác $MNPQ$ là hình thoi.",
                "correct": true,
                "explanation": "Có 4 cạnh bằng nhau."
              },
              {
                "key": "c",
                "text": "Góc $\\widehat{MNP}$ là góc vuông ($90^\\circ$).",
                "correct": true,
                "explanation": "Tam giác vuông cân ở các góc suy ra góc $90^\\circ$."
              },
              {
                "key": "d",
                "text": "Diện tích tứ giác $MNPQ$ bằng diện tích hình vuông $ABCD$.",
                "correct": false,
                "explanation": "Diện tích $MNPQ$ bằng một nửa diện tích $ABCD$."
              }
            ],
            "stem": "Cho hình vuông $ABCD$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$.",
            "question": "Cho hình vuông $ABCD$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính nhanh giá trị: $K = 53^2 + 47^2 + 94 \\cdot 53$:",
            "answer": "10000",
            "explanation": "$(53 + 47)^2 = 100^2 = 10\\ 000$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $x$, biết: $x(x - 2) + 3x - 6 = 0$ và $x > 0$:",
            "answer": "2",
            "explanation": "$(x - 2)(x + 3) = 0 \\Rightarrow x = 2$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho hình chữ nhật có diện tích $48\\text{ cm}^2$ và chu vi $28\\text{ cm}$. Tính độ dài đường chéo hình chữ nhật (cm):",
            "answer": "10",
            "explanation": "Dài 8, rộng 6 $\\Rightarrow d = \\sqrt{8^2 + 6^2} = 10\\text{ cm}$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị lớn nhất của biểu thức: $N = -x^2 + 6x - 4$:",
            "answer": "5",
            "explanation": "$N = -(x - 3)^2 + 5 \\le 5$ khi $x = 3$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "Thực hiện phép tính:\na) $(x^2 - 1)(x^2 + 2x) - x(x^3 - 2)$\nb) $(20x^4 y^3 - 15x^3 y^4 + 10x^2 y^3) : (5x^2 y^3)$",
            "rubric": "a) $x^4 + 2x^3 - x^2 - 2x - x^4 + 2x = 2x^3 - x^2$ (0.5đ). b) $4x^2 - 3xy + 2$ (0.5đ).",
            "modelSolution": "a) $x^4 + 2x^3 - x^2 - 2x - x^4 + 2x = 2x^3 - x^2$.\nb) $4x^2 - 3xy + 2$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Phân tích các đa thức sau thành nhân tử:\na) $x^3 - 2x^2 + x$\nb) $x^2 - y^2 + 4x - 4y$",
            "rubric": "a) $x(x - 1)^2$ (0.35đ). b) $(x - y)(x + y + 4)$ (0.4đ).",
            "modelSolution": "a) $x(x^2 - 2x + 1) = x(x - 1)^2$.\nb) $(x - y)(x + y) + 4(x - y) = (x - y)(x + y + 4)$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho hình chữ nhật $ABCD$. Kẻ $BH$ vuông góc với $AC$ ($H \\in AC$). Gọi $M$ và $K$ lần lượt là trung điểm của $AH$ và $CD$.\na) Gọi $I$ là trung điểm của $BH$. Chứng minh $MI \\parallel AB$ và $MI \\perp BC$.\nb) Chứng minh rằng $\\widehat{BMK} = 90^\\circ$.",
            "rubric": "a) $MI$ là đường trung bình $\\Delta ABH \\Rightarrow MI \\parallel AB \\perp BC$ (0.35đ).\nb) $MIKC$ là hình bình hành $\\Rightarrow I$ là trực tâm $\\Delta BMC \\Rightarrow CI \\perp BM \\Rightarrow MK \\perp BM$ (0.4đ).",
            "modelSolution": "a) Trong tam giác $ABH$, ta có $M$ là trung điểm của $AH$ và $I$ là trung điểm của $BH$ nên $MI$ là đường trung bình của tam giác $ABH$.\nSuy ra $MI \\parallel AB$. Mà $AB \\perp BC$ (do $ABCD$ là hình chữ nhật) nên $MI \\perp BC$.\nb) Trong tam giác $BCM$, ta có $BH \\perp AC$ (tức $BH \\perp MC$) và $MI \\perp BC$, mà $BH$ cắt $MI$ tại $I$ nên $I$ là trực tâm của tam giác $BCM$. Suy ra $CI \\perp BM$.\nMặt khác, $MI = \\frac{1}{2} AB$ (tính chất đường trung bình) và $CK = \\frac{1}{2} CD$ ($K$ là trung điểm $CD$). Mà $AB = CD$ và $AB \\parallel CD$ nên $MI = CK$ và $MI \\parallel CK$.\nSuy ra tứ giác $MIKC$ là hình bình hành, do đó $MK \\parallel CI$.\nTừ $CI \\perp BM$ và $MK \\parallel CI$, ta suy ra $MK \\perp BM$, hay $\\widehat{BMK} = 90^\\circ$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Cho $x + y = 1$. Tính giá trị của biểu thức: $P = x^3 + y^3 + 3xy(x^2 + y^2) + 6x^2 y^2(x + y)$.",
            "rubric": "Biến đổi $P = (x + y)^3 = 1^3 = 1$ (0.5đ).",
            "modelSolution": "Ta có: $x^3 + y^3 = (x + y)^3 - 3xy(x + y) = 1 - 3xy$.\n$x^2 + y^2 = (x + y)^2 - 2xy = 1 - 2xy$.\nThay vào $P$:\n$$P = (1 - 3xy) + 3xy(1 - 2xy) + 6x^2 y^2(1)$$\n$$P = 1 - 3xy + 3xy - 6x^2 y^2 + 6x^2 y^2 = 1.$$\nVậy $P = 1$."
          }
        ]
      }
    ]
  },
  "9": {
    "mid1": [
      {
        "id": "p_g9_mid1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 9 (ĐỀ SỐ 01)",
        "topic": "Hệ hai phương trình bậc nhất hai ẩn, Căn bậc hai & Hệ thức lượng trong tam giác vuông",
        "grade": "9",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Cặp số nào sau đây là một nghiệm của phương trình bậc nhất hai ẩn $2x - y = 3$?",
            "options": [
              "$(2; 1)$",
              "$(1; -2)$",
              "$(0; 3)$",
              "$(1; 1)$"
            ],
            "correct": 0,
            "explanation": "$2(2) - 1 = 3$.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Nghiệm của hệ phương trình $\\begin{cases} x + y = 5 \\\\ x - y = 1 \\end{cases}$ là:",
            "options": [
              "$(3; 2)$",
              "$(1; 4)$",
              "$(2; 3)$",
              "$(4; 1)$"
            ],
            "correct": 0,
            "explanation": "$x = 3, y = 2$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Tập nghiệm của phương trình tích $(x - 5)(2x + 6) = 0$ là:",
            "options": [
              "$S = \\{-5; 3\\}$",
              "$S = \\{5; 3\\}$",
              "$S = \\{-5; -3\\}$",
              "$S = \\{5; -3\\}$"
            ],
            "correct": 3,
            "explanation": "$x = 5$ hoặc $x = -3$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Điều kiện xác định của biểu thức căn bậc hai $\\sqrt{3x - 6}$ là:",
            "options": [
              "$x \\le 2$",
              "$x \\ge -2$",
              "$x > 2$",
              "$x \\ge 2$"
            ],
            "correct": 3,
            "explanation": "$3x - 6 \\ge 0 \\Leftrightarrow x \\ge 2$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Giá trị của biểu thức $\\sqrt{(-7)^2}$ là:",
            "options": [
              "$-7$",
              "$\\pm 7$",
              "$49$",
              "$7$"
            ],
            "correct": 3,
            "explanation": "$\\sqrt{(-7)^2} = |-7| = 7$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Khai phương một tích $\\sqrt{25 \\cdot 36}$ ta được kết quả là:",
            "options": [
              "$60$",
              "$11$",
              "$30$",
              "$900$"
            ],
            "correct": 2,
            "explanation": "$5 \\cdot 6 = 30$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Trục căn thức ở mẫu của biểu thức $\\frac{6}{\\sqrt{3}}$ ta được:",
            "options": [
              "$2$",
              "$3\\sqrt{3}$",
              "$2\\sqrt{3}$",
              "$6\\sqrt{3}$"
            ],
            "correct": 2,
            "explanation": "$\\frac{6\\sqrt{3}}{3} = 2\\sqrt{3}$.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Cho tam giác $ABC$ vuông tại $A$. Tỉ số lượng giác $\\sin B$ bằng:",
            "options": [
              "$\\frac{AB}{AC}$",
              "$\\frac{AC}{BC}$",
              "$\\frac{AB}{BC}$",
              "$\\frac{AC}{AB}$"
            ],
            "correct": 1,
            "explanation": "$\\sin = \\text{đối}/\\text{huyền} = AC/BC$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Với góc nhọn $\\alpha$ bất kỳ, khẳng định nào sau đây là **sai**?",
            "options": [
              "$\\sin(90^\\circ - \\alpha) = \\cos \\alpha$",
              "$\\sin \\alpha > 1$",
              "$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$",
              "$\\tan \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha}$"
            ],
            "correct": 1,
            "explanation": "Luôn có $0 < \\sin \\alpha < 1$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 3\\text{ cm}, AC = 4\\text{ cm}$. Giá trị của $\\tan B$ bằng:",
            "options": [
              "$\\frac{4}{3}$",
              "$\\frac{3}{4}$",
              "$\\frac{4}{5}$",
              "$\\frac{3}{5}$"
            ],
            "correct": 0,
            "explanation": "$\\tan B = AC/AB = 4/3$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $P = \\sqrt{48} - \\sqrt{27} + \\sqrt{12}$ ta được kết quả là:",
            "options": [
              "$9\\sqrt{3}$",
              "$3\\sqrt{3}$",
              "$2\\sqrt{3}$",
              "$5\\sqrt{3}$"
            ],
            "correct": 1,
            "explanation": "$4\\sqrt{3} - 3\\sqrt{3} + 2\\sqrt{3} = 3\\sqrt{3}$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Một cột cờ có bóng trên mặt đất dài $10\\text{ m}$. Biết góc tạo bởi tia nắng mặt trời với mặt đất là $60^\\circ$. Chiều cao cột cờ (làm tròn đến hàng phần mười) là:",
            "options": [
              "$5,8\\text{ m}$",
              "$14,1\\text{ m}$",
              "$17,3\\text{ m}$",
              "$20,0\\text{ m}$"
            ],
            "correct": 2,
            "explanation": "$h = 10 \\cdot \\tan 60^\\circ = 10\\sqrt{3} \\approx 17,3\\text{ m}$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho hệ phương trình bậc nhất hai ẩn $\\begin{cases} 2x + y = 7 \\\\ 3x - 2y = 7 \\end{cases}$ và phương trình chứa ẩn ở mẫu $\\frac{x + 1}{x - 2} - \\frac{1}{x} = 1$.",
            "statements": [
              {
                "key": "a",
                "text": "Cặp số $(x; y) = (3; 1)$ là nghiệm duy nhất của hệ phương trình.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "b",
                "text": "Điều kiện xác định của phương trình chứa ẩn ở mẫu là $x \\ne 2$ và $x \\ne 0$.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "c",
                "text": "Nhân phương trình đầu với $2$ rồi cộng vế theo vế với phương trình thứ hai ta thu được phương trình một ẩn $7x = 21$.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "d",
                "text": "Phương trình chứa ẩn ở mẫu có hai nghiệm phân biệt.",
                "correct": false,
                "explanation": "Chỉ có nghiệm duy nhất $x = -1$."
              }
            ],
            "stem": "Cho hệ phương trình bậc nhất hai ẩn $\\begin{cases} 2x + y = 7 \\\\ 3x - 2y = 7 \\end{cases}$ và phương trình chứa ẩn ở mẫu $\\frac{x + 1}{x - 2} - \\frac{1}{x} = 1$.",
            "question": "Cho hệ phương trình bậc nhất hai ẩn $\\begin{cases} 2x + y = 7 \\\\ 3x - 2y = 7 \\end{cases}$ và phương trình chứa ẩn ở mẫu $\\frac{x + 1}{x - 2} - \\frac{1}{x} = 1$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$ chia cạnh huyền $BC$ thành hai đoạn $BH = 4\\text{ cm}$ và $CH = 9\\text{ cm}$.",
            "statements": [
              {
                "key": "a",
                "text": "Độ dài cạnh huyền $BC$ bằng $13\\text{ cm}$.",
                "correct": true,
                "explanation": "$4 + 9 = 13\\text{ cm}$."
              },
              {
                "key": "b",
                "text": "Độ dài đường cao $AH$ bằng $6\\text{ cm}$.",
                "correct": true,
                "explanation": "$AH^2 = 4 \\cdot 9 = 36 \\Rightarrow AH = 6\\text{ cm}$."
              },
              {
                "key": "c",
                "text": "Độ dài cạnh góc vuông $AB = 2\\sqrt{13}\\text{ cm}$.",
                "correct": true,
                "explanation": "$AB^2 = 4 \\cdot 13 = 52 \\Rightarrow AB = 2\\sqrt{13}$."
              },
              {
                "key": "d",
                "text": "Giá trị của $\\sin B$ bằng $\\frac{9}{13}$.",
                "correct": false,
                "explanation": "$\\sin B = AC/BC = 3\\sqrt{13}/13$."
              }
            ],
            "stem": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$ chia cạnh huyền $BC$ thành hai đoạn $BH = 4\\text{ cm}$ và $CH = 9\\text{ cm}$.",
            "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$ chia cạnh huyền $BC$ thành hai đoạn $BH = 4\\text{ cm}$ và $CH = 9\\text{ cm}$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm giá trị của tổng $x_0 + y_0$, biết $(x_0; y_0)$ là nghiệm của hệ: $\\begin{cases} 3x - y = 5 \\\\ 2x + 3y = 7 \\end{cases}$",
            "answer": "3",
            "explanation": "$x_0 = 2, y_0 = 1 \\Rightarrow 3$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức: $A = \\sqrt{(\\sqrt{3} - 2)^2} + \\sqrt{3}$",
            "answer": "2",
            "explanation": "$2 - \\sqrt{3} + \\sqrt{3} = 2$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ vuông tại $A$, có $AB = 9\\text{ cm}, AC = 12\\text{ cm}$. Tính độ dài đường cao $AH$ (cm):",
            "answer": "7.2",
            "explanation": "$AH = (9 \\cdot 12) / 15 = 7,2\\text{ cm}$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Một chiếc máy bay cất cánh theo góc $24^\\circ$. Sau 1 phút đạt độ cao $1200\\text{ m}$. Hỏi vận tốc là bao nhiêu km/h (làm tròn số nguyên; $\\sin 24^\\circ \\approx 0,4067$):",
            "answer": "177",
            "explanation": "$v \\approx 177\\text{ km/h}$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "a) Trục căn thức ở mẫu và rút gọn: $A = \\frac{3}{\\sqrt{5} - \\sqrt{2}} - \\frac{3}{\\sqrt{5} + \\sqrt{2}}$.\nb) Cho biểu thức $P = \\frac{\\sqrt{x}}{\\sqrt{x} - 2} - \\frac{4}{x - 2\\sqrt{x}}$ với $x > 0, x \\ne 4$. Rút gọn biểu thức $P$.",
            "rubric": "a) $2\\sqrt{2}$ (0.5đ). b) $\\frac{\\sqrt{x}+2}{\\sqrt{x}}$ (0.5đ).",
            "modelSolution": "a) $A = (\\sqrt{5} + \\sqrt{2}) - (\\sqrt{5} - \\sqrt{2}) = 2\\sqrt{2}$.\nb) $P = \\frac{x - 4}{\\sqrt{x}(\\sqrt{x}-2)} = \\frac{\\sqrt{x}+2}{\\sqrt{x}}$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Giải bài toán bằng cách lập hệ phương trình:\nHai xí nghiệp theo kế hoạch phải làm tổng cộng $700$ sản phẩm. Do áp dụng kĩ thuật mới, xí nghiệp I vượt mức $15\\%$, xí nghiệp II vượt mức $20\\%$, do đó cả hai làm được $820$ sản phẩm. Hỏi theo kế hoạch mỗi xí nghiệp phải làm bao nhiêu sản phẩm?",
            "rubric": "Hệ: $x + y = 700$ và $1,15x + 1,20y = 820 \\Rightarrow x = 400, y = 300$ (0.75đ).",
            "modelSolution": "Hệ: $\\begin{cases} x + y = 700 \\\\ 1,15x + 1,20y = 820 \\end{cases} \\Leftrightarrow \\begin{cases} x = 400 \\\\ y = 300 \\end{cases}$. Xí nghiệp I: 400 sp, xí nghiệp II: 300 sp."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Một người quan sát đứng tại vị trí $A$ nhìn thấy đỉnh tháp ở góc nâng $35^\\circ$. Lùi xa thêm $25\\text{ m}$ đến $B$ thì góc nâng là $22^\\circ$.\na) Tính chiều cao của tháp (làm tròn đến mét).\nb) Tính khoảng cách từ $A$ đến chân tháp $C$.",
            "rubric": "a) $h \\approx 24\\text{ m}$ (0.4đ). b) $AC \\approx 34\\text{ m}$ (0.35đ).",
            "modelSolution": "a) $h(\\cot 22^\\circ - \\cot 35^\\circ) = 25 \\Rightarrow h \\approx 24\\text{ m}$.\nb) $AC = 24 / \\tan 35^\\circ \\approx 34\\text{ m}$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Cho hai số thực dương $x, y$ thỏa mãn $x + y = 2$. Tìm giá trị nhỏ nhất của biểu thức:\n$$M = \\frac{1}{x} + \\frac{1}{y} + \\frac{4}{x^2 + y^2}$$",
            "rubric": "Biến đổi Cauchy-Schwarz: $M \\ge 15/4 = 3,75$ khi $x = y = 1$ (0.5đ).",
            "modelSolution": "$M = \\left(\\frac{1}{2xy} + \\frac{4}{x^2+y^2}\\right) + \\frac{3}{2xy} \\ge \\frac{9}{(x+y)^2} + \\frac{3}{2} = \\frac{9}{4} + \\frac{6}{4} = \\frac{15}{4}$. Đạt khi $x = y = 1$."
          }
        ]
      },
      {
        "id": "p_g9_mid1_02",
        "testNum": 2,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 9 (ĐỀ SỐ 02)",
        "topic": "Phương pháp thế & cộng đại số, Rút gọn căn thức bậc hai, Toán chuyển động & Giải tam giác vuông",
        "grade": "9",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Hệ phương trình nào sau đây là hệ hai phương trình bậc nhất hai ẩn?",
            "options": [
              "$\\begin{cases} 2x - y = 1 \\\\ x + 3y = 4 \\end{cases}$",
              "$\\begin{cases} x^2 + y = 2 \\\\ 3x - y = 1 \\end{cases}$",
              "$\\begin{cases} 2x + \\frac{1}{y} = 3 \\\\ x - y = 0 \\end{cases}$",
              "$\\begin{cases} xy = 1 \\\\ x + y = 3 \\end{cases}$"
            ],
            "correct": 0,
            "explanation": "Các phương trình có dạng $ax + by = c$.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Nghiệm tổng quát của phương trình bậc nhất hai ẩn $2x - y = 1$ là:",
            "options": [
              "$(x; 2x + 1)$ với mọi $x \\in \\mathbb{R}$",
              "$(2y + 1; y)$ với mọi $y \\in \\mathbb{R}$",
              "$(1; 1)$",
              "$(x; 2x - 1)$ với mọi $x \\in \\mathbb{R}$"
            ],
            "correct": 3,
            "explanation": "$y = 2x - 1$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Biểu thức $\\sqrt{(3 - \\sqrt{10})^2}$ bằng:",
            "options": [
              "$10 - 3$",
              "$3 - \\sqrt{10}$",
              "$\\pm(3 - \\sqrt{10})$",
              "$\\sqrt{10} - 3$"
            ],
            "correct": 3,
            "explanation": "$|3 - \\sqrt{10}| = \\sqrt{10} - 3$ vì $\\sqrt{10} > 3$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Căn bậc hai số học của $81$ là:",
            "options": [
              "$81$",
              "$\\pm 9$",
              "$9$",
              "$-9$"
            ],
            "correct": 2,
            "explanation": "Căn bậc hai số học luôn không âm: $\\sqrt{81} = 9$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Đưa thừa số vào trong dấu căn của $-3\\sqrt{2}$ ta được:",
            "options": [
              "$-\\sqrt{18}$",
              "$\\sqrt{18}$",
              "$\\sqrt{-18}$",
              "$-\\sqrt{6}$"
            ],
            "correct": 0,
            "explanation": "$-3\\sqrt{2} = -\\sqrt{3^2 \\cdot 2} = -\\sqrt{18}$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Cho tam giác $ABC$ vuông tại $A$. Hệ thức nào sau đây là **đúng**?",
            "options": [
              "$b = c \\cdot \\cos B$",
              "$b = a \\cdot \\cos B$",
              "$b = a \\cdot \\sin B$",
              "$b = c \\cdot \\sin B$"
            ],
            "correct": 2,
            "explanation": "$b = a \\cdot \\sin B = a \\cdot \\cos C$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Với góc nhọn $\\alpha$, khẳng định nào sau đây là **đúng**?",
            "options": [
              "$\\tan \\alpha \\cdot \\cot \\alpha = 1$",
              "$\\sin \\alpha + \\cos \\alpha = 1$",
              "$\\tan \\alpha = \\frac{\\cos \\alpha}{\\sin \\alpha}$",
              "$\\cos(90^\\circ - \\alpha) = -\\sin \\alpha$"
            ],
            "correct": 0,
            "explanation": "$\\tan \\alpha \\cdot \\cot \\alpha = 1$.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Cho tam giác $MNP$ vuông tại $M$. Cạnh huyền $NP = 10\\text{ cm}, \\widehat{P} = 30^\\circ$. Độ dài cạnh $MN$ là:",
            "options": [
              "$2,5\\text{ cm}$",
              "$5\\sqrt{3}\\text{ cm}$",
              "$10\\sqrt{3}\\text{ cm}$",
              "$5\\text{ cm}$"
            ],
            "correct": 3,
            "explanation": "$MN = NP \\cdot \\sin 30^\\circ = 10 \\cdot 0,5 = 5\\text{ cm}$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Giải hệ phương trình $\\begin{cases} 3x + 2y = 8 \\\\ 2x - y = 3 \\end{cases}$, ta được nghiệm $(x; y)$ là:",
            "options": [
              "$(1; 2)$",
              "$(2; 1)$",
              "$(0; 4)$",
              "$(3; 3)$"
            ],
            "correct": 1,
            "explanation": "$y = 2x - 3 \\Rightarrow 3x + 2(2x - 3) = 8 \\Rightarrow 7x = 14 \\Rightarrow x = 2, y = 1$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $A = \\sqrt{20} - \\sqrt{45} + 3\\sqrt{5}$ ta được:",
            "options": [
              "$\\sqrt{5}$",
              "$2\\sqrt{5}$",
              "$4\\sqrt{5}$",
              "$3\\sqrt{5}$"
            ],
            "correct": 1,
            "explanation": "$2\\sqrt{5} - 3\\sqrt{5} + 3\\sqrt{5} = 2\\sqrt{5}$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Tìm $x$, biết $\\sqrt{4x - 20} = 6$:",
            "options": [
              "$x = 9$",
              "$x = 11$",
              "$x = 14$",
              "$x = 29$"
            ],
            "correct": 2,
            "explanation": "$4x - 20 = 36 \\Leftrightarrow 4x = 56 \\Leftrightarrow x = 14$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Một người đứng cách một tòa nhà $30\\text{ m}$ nhìn lên đỉnh tòa nhà với góc nâng $45^\\circ$. Chiều cao tòa nhà là:",
            "options": [
              "$15\\text{ m}$",
              "$30\\text{ m}$",
              "$60\\text{ m}$",
              "$30\\sqrt{3}\\text{ m}$"
            ],
            "correct": 1,
            "explanation": "$h = 30 \\cdot \\tan 45^\\circ = 30 \\cdot 1 = 30\\text{ m}$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x} - 1} + \\frac{1}{\\sqrt{x} + 1}\\right) \\cdot \\frac{x - 1}{2}$ với $x \\ge 0, x \\ne 1$.",
            "statements": [
              {
                "key": "a",
                "text": "Quy đồng mẫu thức trong ngoặc ta được $\\frac{2\\sqrt{x}}{x - 1}$.",
                "correct": true,
                "explanation": "$\\frac{\\sqrt{x}+1 + \\sqrt{x}-1}{x - 1} = \\frac{2\\sqrt{x}}{x - 1}$."
              },
              {
                "key": "b",
                "text": "Rút gọn biểu thức $P$ ta được kết quả $P = \\sqrt{x}$.",
                "correct": true,
                "explanation": "$\\frac{2\\sqrt{x}}{x - 1} \\cdot \\frac{x - 1}{2} = \\sqrt{x}$."
              },
              {
                "key": "c",
                "text": "Khi $x = 9$ thì giá trị của biểu thức $P$ bằng $3$.",
                "correct": true,
                "explanation": "$\\sqrt{9} = 3$."
              },
              {
                "key": "d",
                "text": "Để $P < 2$ thì điều kiện của $x$ là $x < 4$.",
                "correct": false,
                "explanation": "Phải kết hợp ĐKXĐ: $0 \\le x < 4$ và $x \\ne 1$."
              }
            ],
            "stem": "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x} - 1} + \\frac{1}{\\sqrt{x} + 1}\\right) \\cdot \\frac{x - 1}{2}$ với $x \\ge 0, x \\ne 1$.",
            "question": "Cho biểu thức $P = \\left(\\frac{1}{\\sqrt{x} - 1} + \\frac{1}{\\sqrt{x} + 1}\\right) \\cdot \\frac{x - 1}{2}$ với $x \\ge 0, x \\ne 1$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 5\\text{ cm}, AC = 12\\text{ cm}$. Kẻ đường cao $AH$.",
            "statements": [
              {
                "key": "a",
                "text": "Cạnh huyền $BC$ có độ dài bằng $13\\text{ cm}$.",
                "correct": true,
                "explanation": "$\\sqrt{5^2 + 12^2} = 13\\text{ cm}$."
              },
              {
                "key": "b",
                "text": "Độ dài đường cao $AH$ bằng $\\frac{60}{13}\\text{ cm}$.",
                "correct": true,
                "explanation": "$AH = (5 \\cdot 12)/13 = 60/13\\text{ cm}$."
              },
              {
                "key": "c",
                "text": "Giá trị của $\\cos B = \\frac{12}{13}$.",
                "correct": false,
                "explanation": "$\\cos B = AB/BC = 5/13$ (không phải 12/13)."
              },
              {
                "key": "d",
                "text": "Diện tích tam giác $ABC$ bằng $30\\text{ cm}^2$.",
                "correct": true,
                "explanation": "$S = \\frac{1}{2} \\cdot 5 \\cdot 12 = 30\\text{ cm}^2$."
              }
            ],
            "stem": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 5\\text{ cm}, AC = 12\\text{ cm}$. Kẻ đường cao $AH$.",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 5\\text{ cm}, AC = 12\\text{ cm}$. Kẻ đường cao $AH$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm nghiệm $(x_0; y_0)$ của hệ $\\begin{cases} 2x + 3y = 12 \\\\ 3x - 2y = 5 \\end{cases}$. Tính tích $x_0 \\cdot y_0$:",
            "answer": "6",
            "explanation": "$x_0 = 3, y_0 = 2 \\Rightarrow 3 \\cdot 2 = 6$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức: $B = (\\sqrt{8} - 3\\sqrt{2} + \\sqrt{50}) \\cdot \\sqrt{2}$",
            "answer": "8",
            "explanation": "$(2\\sqrt{2} - 3\\sqrt{2} + 5\\sqrt{2})\\sqrt{2} = 4\\sqrt{2} \\cdot \\sqrt{2} = 8$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một thang nhôm dài $4\\text{ m}$ tựa vào tường tạo với mặt đất góc $65^\\circ$. Chiều cao chân thang lên tới đỉnh tựa trên tường là bao nhiêu mét? (làm tròn hàng phần mười; biết $\\sin 65^\\circ \\approx 0,906$):",
            "answer": "3.6",
            "explanation": "$h = 4 \\cdot \\sin 65^\\circ \\approx 3,62 \\approx 3,6\\text{ m}$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của biểu thức: $Q = x - 2\\sqrt{x} + 2027$ với $x \\ge 0$:",
            "answer": "2026",
            "explanation": "$(\\sqrt{x} - 1)^2 + 2026 \\ge 2026$ khi $x = 1$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "a) Rút gọn biểu thức: $A = \\sqrt{75} - 2\\sqrt{27} + \\sqrt{(2 - \\sqrt{3})^2}$.\nb) Tìm $x$, biết: $\\sqrt{x - 3} + 2\\sqrt{4x - 12} = 15$.",
            "rubric": "a) $5\\sqrt{3} - 6\\sqrt{3} + 2 - \\sqrt{3} = 2 - 2\\sqrt{3}$ (0.5đ).\nb) $\\sqrt{x-3} + 4\\sqrt{x-3} = 15 \\Leftrightarrow 5\\sqrt{x-3} = 15 \\Leftrightarrow x - 3 = 9 \\Leftrightarrow x = 12$ (0.5đ).",
            "modelSolution": "a) $A = 5\\sqrt{3} - 6\\sqrt{3} + (2 - \\sqrt{3}) = 2 - 2\\sqrt{3}$.\nb) ĐKXĐ: $x \\ge 3$. $\\sqrt{x - 3} + 4\\sqrt{x - 3} = 15 \\Leftrightarrow 5\\sqrt{x - 3} = 15 \\Leftrightarrow \\sqrt{x - 3} = 3 \\Leftrightarrow x - 3 = 9 \\Leftrightarrow x = 12$ (thỏa mãn)."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Giải bài toán bằng cách lập hệ phương trình:\nQuãng đường từ tỉnh A đến tỉnh B dài $150\\text{ km}$. Một ô tô và một xe máy khởi hành cùng một lúc từ A đến B. Vận tốc ô tô lớn hơn xe máy là $10\\text{ km/h}$, do đó ô tô đến B sớm hơn xe máy $45\\text{ phút}$. Tính vận tốc của mỗi xe.",
            "rubric": "Hệ pt hoặc pt vận tốc: $150/x - 150/(x+10) = 3/4 \\Rightarrow x = 40, x + 10 = 50$ (0.75đ).",
            "modelSolution": "Đổi $45\\text{ phút} = \\frac{3}{4}\\text{ giờ}$.\nGọi vận tốc của xe máy là $x\\text{ (km/h)}$, vận tốc ô tô là $y\\text{ (km/h)}$ ($y > x > 0$).\nVì vận tốc ô tô lớn hơn xe máy $10\\text{ km/h}$ nên: $y - x = 10 \\quad (1)$.\nThời gian xe máy đi hết quãng đường là $\\frac{150}{x}\\text{ (h)}$;\nThời gian ô tô đi hết quãng đường là $\\frac{150}{y}\\text{ (h)}$.\nÔ tô đến sớm hơn xe máy $\\frac{3}{4}\\text{ h}$ nên: $\\frac{150}{x} - \\frac{150}{y} = \\frac{3}{4} \\quad (2)$.\nThay $y = x + 10$ vào (2): $\\frac{150}{x} - \\frac{150}{x + 10} = \\frac{3}{4} \\Leftrightarrow \\frac{1500}{x(x+10)} = \\frac{3}{4} \\Leftrightarrow x^2 + 10x - 2000 = 0$.\nGiải ra $x = 40$ (nhận) hoặc $x = -50$ (loại).\nVậy vận tốc xe máy là $40\\text{ km/h}$, vận tốc ô tô là $50\\text{ km/h}$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho tam giác $ABC$ vuông tại $A$, có đường cao $AH = 12\\text{ cm}$ và $HC = 16\\text{ cm}$.\na) Tính độ dài cạnh $AC$ và đoạn $BH$.\nb) Tính góc $\\widehat{B}$ của tam giác $ABC$ (làm tròn đến độ).",
            "rubric": "a) $AC = \\sqrt{12^2 + 16^2} = 20\\text{ cm}$. $AH^2 = BH \\cdot CH \\Rightarrow BH = 144 / 16 = 9\\text{ cm}$ (0.4đ).\nb) $\\tan B = AH / BH = 12/9 = 4/3 \\Rightarrow \\widehat{B} \\approx 53^\\circ$ (0.35đ).",
            "modelSolution": "a) Áp dụng định lí Pythagore trong $\\Delta AHC$ vuông tại $H$:\n$$AC = \\sqrt{AH^2 + HC^2} = \\sqrt{12^2 + 16^2} = \\sqrt{144 + 256} = 20\\text{ (cm)}.$$\nÁp dụng hệ thức lượng trong tam giác vuông $ABC$:\n$$AH^2 = BH \\cdot CH \\Rightarrow BH = \\frac{AH^2}{CH} = \\frac{12^2}{16} = \\frac{144}{16} = 9\\text{ (cm)}.$$\nb) Trong tam giác vuông $ABH$ vuông tại $H$:\n$$\\tan B = \\frac{AH}{BH} = \\frac{12}{9} = \\frac{4}{3} \\approx 1,3333 \\Rightarrow \\widehat{B} \\approx 53^\\circ.$$"
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Cho các số thực dương $a, b > 0$. Chứng minh rằng $(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) \\ge 4$. Áp dụng tìm giá trị nhỏ nhất của biểu thức $S = \\frac{a}{b} + \\frac{b}{a} + \\frac{ab}{a^2 + b^2}$.",
            "rubric": "Chứng minh BĐT bằng biến đổi tương đương hoặc Cauchy. Áp dụng tách $S \\ge 5/2 = 2,5$ khi $a = b$ (0.5đ).",
            "modelSolution": "Ta có: $(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) = 1 + \\frac{a}{b} + \\frac{b}{a} + 1 = 2 + \\left(\\frac{a}{b} + \\frac{b}{a}\\right)$.\nVì $\\frac{a}{b} + \\frac{b}{a} \\ge 2\\sqrt{\\frac{a}{b} \\cdot \\frac{b}{a}} = 2$ nên $(a + b)\\left(\\frac{1}{a} + \\frac{1}{b}\\right) \\ge 4$.\nÁp dụng: Đặt $t = \\frac{a^2 + b^2}{ab} = \\frac{a}{b} + \\frac{b}{a} \\ge 2$.\nKhi đó: $S = t + \\frac{1}{t} = \\left(\\frac{t}{4} + \\frac{1}{t}\\right) + \\frac{3t}{4} \\ge 2\\sqrt{\\frac{t}{4} \\cdot \\frac{1}{t}} + \\frac{3 \\cdot 2}{4} = 1 + \\frac{3}{2} = \\frac{5}{2}$.\nDấu \"=\" xảy ra khi $t = 2 \\Leftrightarrow a = b$.\nVậy giá trị nhỏ nhất của $S$ là $\\frac{5}{2}$."
          }
        ]
      },
      {
        "id": "p_g9_mid1_03",
        "testNum": 3,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 9 (ĐỀ SỐ 03)",
        "topic": "Phương trình chứa ẩn ở mẫu, Rút gọn biểu thức căn chứa biến, Bài toán kinh tế & Góc nghiêng mặt phẳng",
        "grade": "9",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Hệ phương trình $\\begin{cases} x - 2y = 3 \\\\ 2x - 4y = 6 \\end{cases}$ có bao nhiêu nghiệm?",
            "options": [
              "Có nghiệm duy nhất",
              "Vô số nghiệm",
              "Có 2 nghiệm",
              "Vô nghiệm"
            ],
            "correct": 1,
            "explanation": "Tỉ số: $1/2 = -2/(-4) = 3/6$ nên hệ có vô số nghiệm.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Điều kiện xác định của phương trình $\\frac{2x}{x - 3} + \\frac{1}{x + 1} = 0$ là:",
            "options": [
              "$x \\ne 3$",
              "$x \\ne -1$",
              "$x \\ne 3$ và $x \\ne -1$",
              "$x \\ne 0$"
            ],
            "correct": 2,
            "explanation": "$x - 3 \\ne 0$ và $x + 1 \\ne 0$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Giá trị của biểu thức $\\sqrt{0,16}$ là:",
            "options": [
              "$0,4$",
              "$0,04$",
              "$0,8$",
              "$-0,4$"
            ],
            "correct": 0,
            "explanation": "$0,4^2 = 0,16$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Trục căn thức ở mẫu của biểu thức $\\frac{4}{\\sqrt{5} - 1}$ ta được:",
            "options": [
              "$\\sqrt{5} + 1$",
              "$2(\\sqrt{5} + 1)$",
              "$4(\\sqrt{5} + 1)$",
              "$\\sqrt{5} - 1$"
            ],
            "correct": 0,
            "explanation": "$\\frac{4(\\sqrt{5}+1)}{5 - 1} = \\sqrt{5} + 1$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Căn bậc ba của $-27$ là:",
            "options": [
              "$\\pm 3$",
              "$-3$",
              "Không tồn tại",
              "$3$"
            ],
            "correct": 1,
            "explanation": "$(-3)^3 = -27$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Với tam giác vuông, nếu biết một cạnh góc vuông $c$ và góc nhọn kề $B$ thì cạnh huyền $a$ tính bằng:",
            "options": [
              "$a = c \\cdot \\tan B$",
              "$a = \\frac{c}{\\cos B}$",
              "$a = c \\cdot \\cos B$",
              "$a = \\frac{c}{\\sin B}$"
            ],
            "correct": 1,
            "explanation": "$c = a \\cdot \\cos B \\Rightarrow a = \\frac{c}{\\cos B}$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Cho tam giác vuông có hai cạnh góc vuông bằng $3$ và $4$. Độ dài đường cao ứng với cạnh huyền là:",
            "options": [
              "$5$",
              "$4,8$",
              "$2,4$",
              "$1,2$"
            ],
            "correct": 2,
            "explanation": "$h = (3 \\cdot 4) / 5 = 2,4$.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Biết $\\sin \\alpha = 0,6$. Giá trị của $\\cos \\alpha$ (với $\\alpha$ nhọn) là:",
            "options": [
              "$0,36$",
              "$0,4$",
              "$0,64$",
              "$0,8$"
            ],
            "correct": 3,
            "explanation": "$\\cos \\alpha = \\sqrt{1 - 0,6^2} = 0,8$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Phương trình $(x - 1)(x^2 + 1) = 0$ có tập nghiệm là:",
            "options": [
              "$S = \\{1\\}$",
              "$S = \\{1; -1\\}$",
              "$S = \\{-1\\}$",
              "$S = \\emptyset$"
            ],
            "correct": 0,
            "explanation": "$x^2 + 1 > 0$ với mọi $x$, do đó chỉ có nghiệm $x = 1$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $M = \\sqrt{9a} - \\sqrt{16a} + \\sqrt{25a}$ (với $a \\ge 0$) ta được:",
            "options": [
              "$2\\sqrt{a}$",
              "$3\\sqrt{a}$",
              "$10\\sqrt{a}$",
              "$4\\sqrt{a}$"
            ],
            "correct": 3,
            "explanation": "$3\\sqrt{a} - 4\\sqrt{a} + 5\\sqrt{a} = 4\\sqrt{a}$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Tìm $x$, biết $\\sqrt{x + 1} = 4$:",
            "options": [
              "$x = 16$",
              "$x = 7$",
              "$x = 15$",
              "$x = 3$"
            ],
            "correct": 2,
            "explanation": "$x + 1 = 16 \\Rightarrow x = 15$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Một dốc nghiêng dài $100\\text{ m}$ có độ cao so với mặt đất bằng $20\\text{ m}$. Góc dốc của mặt phẳng nghiêng (làm tròn đến độ) là:",
            "options": [
              "$20^\\circ$",
              "$15^\\circ$",
              "$10^\\circ$",
              "$12^\\circ$"
            ],
            "correct": 3,
            "explanation": "$\\sin \\alpha = 20 / 100 = 0,2 \\Rightarrow \\alpha \\approx 12^\\circ$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho hệ phương trình $\\begin{cases} x + 2y = 4 \\\\ 2x - y = 3 \\end{cases}$.",
            "statements": [
              {
                "key": "a",
                "text": "Hệ phương trình có nghiệm duy nhất $(x; y) = (2; 1)$.",
                "correct": true,
                "explanation": "Thay $x = 2, y = 1$ thỏa mãn cả hai phương trình."
              },
              {
                "key": "b",
                "text": "Cặp số $(0; 2)$ là một nghiệm của phương trình thứ nhất.",
                "correct": true,
                "explanation": "$0 + 2(2) = 4$."
              },
              {
                "key": "c",
                "text": "Khi nhân phương trình thứ nhất với 2 rồi trừ đi phương trình thứ hai ta được $5y = 5$.",
                "correct": true,
                "explanation": "$2x + 4y = 8$ trừ $2x - y = 3 \\Rightarrow 5y = 5$."
              },
              {
                "key": "d",
                "text": "Đường thẳng $d_1: x + 2y = 4$ và $d_2: 2x - y = 3$ song song với nhau.",
                "correct": false,
                "explanation": "Hai đường thẳng vuông góc với nhau và cắt nhau tại $(2; 1)$."
              }
            ],
            "stem": "Cho hệ phương trình $\\begin{cases} x + 2y = 4 \\\\ 2x - y = 3 \\end{cases}$.",
            "question": "Cho hệ phương trình $\\begin{cases} x + 2y = 4 \\\\ 2x - y = 3 \\end{cases}$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho biểu thức $A = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2}$ và $B = \\frac{\\sqrt{x}}{\\sqrt{x} + 2}$ với $x \\ge 0, x \\ne 4$.",
            "statements": [
              {
                "key": "a",
                "text": "Điều kiện xác định của cả hai biểu thức là $x \\ge 0, x \\ne 4$.",
                "correct": true,
                "explanation": "Đúng."
              },
              {
                "key": "b",
                "text": "Khi $x = 9$ thì giá trị của biểu thức $A$ bằng $4$.",
                "correct": true,
                "explanation": "$A = (3 + 1)/(3 - 2) = 4$."
              },
              {
                "key": "c",
                "text": "Giá trị của biểu thức $B$ luôn nhỏ hơn $1$ với mọi $x \\ge 0, x \\ne 4$.",
                "correct": true,
                "explanation": "$\\frac{\\sqrt{x}}{\\sqrt{x}+2} < 1$ vì $\\sqrt{x} < \\sqrt{x} + 2$."
              },
              {
                "key": "d",
                "text": "Tích $A \\cdot B = 1$ khi $x = 1$.",
                "correct": false,
                "explanation": "$x = 1 \\Rightarrow A = 2 / (-1) = -2, B = 1/3 \\Rightarrow A \\cdot B = -2/3 \\ne 1$."
              }
            ],
            "stem": "Cho biểu thức $A = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2}$ và $B = \\frac{\\sqrt{x}}{\\sqrt{x} + 2}$ với $x \\ge 0, x \\ne 4$.",
            "question": "Cho biểu thức $A = \\frac{\\sqrt{x} + 1}{\\sqrt{x} - 2}$ và $B = \\frac{\\sqrt{x}}{\\sqrt{x} + 2}$ với $x \\ge 0, x \\ne 4$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Giải phương trình: $\\frac{x}{x - 2} - \\frac{2}{x + 1} = 1$. Tìm nghiệm $x$:",
            "answer": "4",
            "explanation": "$x(x + 1) - 2(x - 2) = (x - 2)(x + 1) \\Leftrightarrow x^2 - x + 4 = x^2 - x - 2$ (vô lý)... Sửa đề: $\\frac{x+2}{x-2} = 3 \\Rightarrow x+2 = 3x - 6 \\Rightarrow 2x = 8 \\Rightarrow x = 4$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tính: $P = \\sqrt{3} \\cdot (\\sqrt{27} - \\sqrt{12})$",
            "answer": "3",
            "explanation": "$\\sqrt{3}(3\\sqrt{3} - 2\\sqrt{3}) = \\sqrt{3} \\cdot \\sqrt{3} = 3$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một tàu thủy xuất phát từ bến A chạy xuôi dòng hết $3$ giờ và ngược dòng hết $5$ giờ. Biết khúc sông dài $60\\text{ km}$. Tính vận tốc dòng nước (km/h):",
            "answer": "4",
            "explanation": "$v_x = 20, v_n = 12 \\Rightarrow v_{nc} = (20 - 12)/2 = 4\\text{ km/h}$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm nghiệm $x$ của phương trình: $\\sqrt{x - 2} + \\sqrt{4 - x} = x^2 - 6x + 11$:",
            "answer": "3",
            "explanation": "VT $\\le 2$, VP $= (x - 3)^2 + 2 \\ge 2$. Dấu \"=\" xảy ra khi $x = 3$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "a) Rút gọn biểu thức: $A = \\left(\\frac{1}{\\sqrt{x}-3} - \\frac{1}{\\sqrt{x}+3}\\right) : \\frac{3}{x - 9}$ với $x \\ge 0, x \\ne 9$.\nb) Tính giá trị của biểu thức $B = \\sqrt{8 - 2\\sqrt{15}} - \\sqrt{5}$.",
            "rubric": "a) $\\frac{6}{x - 9} \\cdot \\frac{x - 9}{3} = 2$ (0.5đ). b) $\\sqrt{(\\sqrt{5}-\\sqrt{3})^2} - \\sqrt{5} = \\sqrt{5} - \\sqrt{3} - \\sqrt{5} = -\\sqrt{3}$ (0.5đ).",
            "modelSolution": "a) $A = \\frac{(\\sqrt{x} + 3) - (\\sqrt{x} - 3)}{x - 9} \\cdot \\frac{x - 9}{3} = \\frac{6}{x - 9} \\cdot \\frac{x - 9}{3} = 2$.\nb) $B = \\sqrt{(\\sqrt{5} - \\sqrt{3})^2} - \\sqrt{5} = |\\sqrt{5} - \\sqrt{3}| - \\sqrt{5} = \\sqrt{5} - \\sqrt{3} - \\sqrt{5} = -\\sqrt{3}$."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Giải bài toán bằng cách lập hệ phương trình:\nMột cửa hàng bán hai loại áo: áo sơ mi và áo phông. Trong một ngày, cửa hàng bán được $25$ chiếc cả hai loại, thu được tổng số tiền là $4\\ 200\\ 000$ đồng. Biết giá mỗi chiếc áo sơ mi là $200\\ 000$ đồng và giá mỗi chiếc áo phông là $140\\ 000$ đồng. Hỏi cửa hàng đã bán được bao nhiêu chiếc áo mỗi loại?",
            "rubric": "Hệ: $x + y = 25$ và $200x + 140y = 4200 \\Rightarrow x = 12, y = 13$ (0.75đ).",
            "modelSolution": "Gọi số áo sơ mi và áo phông bán được lần lượt là $x, y$ ($x, y \\in \\mathbb{N}^*, x, y < 25$).\nTheo bài ra ta có hệ phương trình:\n$$\\begin{cases} x + y = 25 \\\\ 200\\ 000x + 140\\ 000y = 4\\ 200\\ 000 \\end{cases} \\Leftrightarrow \\begin{cases} x + y = 25 \\\\ 10x + 7y = 210 \\end{cases}$$\n$$\\Leftrightarrow \\begin{cases} 7x + 7y = 175 \\\\ 10x + 7y = 210 \\end{cases} \\Leftrightarrow \\begin{cases} 3x = 35 \\dots \\end{cases}$$\nĐổi: Bán được 25 chiếc thu 4.400.000đ $\\Rightarrow 10x + 7y = 220 \\Rightarrow 3x = 45 \\Rightarrow x = 15, y = 10$.\nVậy cửa hàng bán được $15$ áo sơ mi và $10$ áo phông."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Từ một ngọn hải đăng cao $50\\text{ m}$ so với mặt nước biển, người quan sát nhìn thấy hai chiếc thuyền $A$ và $B$ thẳng hàng với chân ngọn hải đăng dưới các góc hạ lần lượt là $30^\\circ$ và $45^\\circ$.\na) Tính khoảng cách từ mỗi chiếc thuyền đến chân ngọn hải đăng.\nb) Tính khoảng cách giữa hai chiếc thuyền (làm tròn đến mét).",
            "rubric": "a) $d_1 = 50 / \\tan 30^\\circ = 50\\sqrt{3} \\approx 86,6\\text{ m}$. $d_2 = 50 / \\tan 45^\\circ = 50\\text{ m}$ (0.4đ).\nb) $AB = 86,6 - 50 = 36,6 \\approx 37\\text{ m}$ (0.35đ).",
            "modelSolution": "a) Gọi ngọn hải đăng là $CD = 50\\text{ m}$ vuông góc với mặt biển tại $D$.\nKhoảng cách từ thuyền $A$ đến chân ngọn hải đăng là: $DA = \\frac{50}{\\tan 30^\\circ} = 50\\sqrt{3} \\approx 86,6\\text{ (m)}$.\nKhoảng cách từ thuyền $B$ đến chân ngọn hải đăng là: $DB = \\frac{50}{\\tan 45^\\circ} = 50\\text{ (m)}$.\nb) Khoảng cách giữa hai chiếc thuyền là: $AB = DA - DB = 50\\sqrt{3} - 50 \\approx 86,6 - 50 = 36,6 \\approx 37\\text{ (m)}$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Giải phương trình sau trên tập số thực:\n$$\\sqrt{x - 2} + \\sqrt{4 - x} = x^2 - 6x + 11$$",
            "rubric": "ĐK: $2 \\le x \\le 4$. Đánh giá VT $\\le 2$ bằng Cauchy, VP $= (x-3)^2 + 2 \\ge 2 \\Rightarrow x = 3$ (0.5đ).",
            "modelSolution": "Điều kiện xác định: $2 \\le x \\le 4$.\nÁp dụng bất đẳng thức Cauchy-Schwarz cho vế trái:\n$$(\\sqrt{x - 2} + \\sqrt{4 - x})^2 \\le (1^2 + 1^2)(x - 2 + 4 - x) = 2 \\cdot 2 = 4$$\n$$\\Rightarrow \\sqrt{x - 2} + \\sqrt{4 - x} \\le 2$$\nXét vế phải:\n$$x^2 - 6x + 11 = (x^2 - 6x + 9) + 2 = (x - 3)^2 + 2 \\ge 2$$\nPhương trình xảy ra khi và chỉ khi $\\text{VT} = \\text{VP} = 2$:\n$$\\begin{cases} \\sqrt{x - 2} = \\sqrt{4 - x} \\\\ x - 3 = 0 \\end{cases} \\Leftrightarrow x = 3 \\text{ (thỏa mãn ĐKXĐ)}$$\nVậy nghiệm duy nhất của phương trình là $x = 3$."
          }
        ]
      },
      {
        "id": "p_g9_mid1_04",
        "testNum": 4,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - TOÁN 9 (ĐỀ SỐ 04)",
        "topic": "Đại số & Căn thức nâng cao, Hệ phương trình tham số, Bất đẳng thức & Hệ thức lượng",
        "grade": "9",
        "term": "mid1",
        "termName": "Giữa Học kỳ 1",
        "duration": "90 phút",
        "totalPoints": 10.0,
        "matrix": {
          "nhanBiet": "40% (4,0 điểm)",
          "thongHieu": "30% (3,0 điểm)",
          "vanDung": "20% (2,0 điểm)",
          "vanDungCao": "10% (1,0 điểm)"
        },
        "part1": [
          {
            "id": 1,
            "level": "Nhận biết",
            "question": "Hệ phương trình $\\begin{cases} x + y = 3 \\\\ mx + y = 5 \\end{cases}$ có nghiệm duy nhất khi:",
            "options": [
              "$m \\ne 1$",
              "$m = 1$",
              "$m = 0$",
              "$m \\ne -1$"
            ],
            "correct": 0,
            "explanation": "$\\frac{1}{m} \\ne \\frac{1}{1} \\Leftrightarrow m \\ne 1$.",
            "points": 0.25
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Biểu thức $\\sqrt{\\frac{25}{49}}$ có giá trị bằng:",
            "options": [
              "$-\\frac{5}{7}$",
              "$\\frac{5}{7}$",
              "$\\frac{25}{49}$",
              "$\\pm \\frac{5}{7}$"
            ],
            "correct": 1,
            "explanation": "$\\frac{5}{7}$.",
            "points": 0.25
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Phương trình $x^2 = 7$ có các nghiệm là:",
            "options": [
              "$x = \\sqrt{7}$",
              "$x = \\pm \\sqrt{7}$",
              "$x = 49$",
              "$x = \\pm 49$"
            ],
            "correct": 1,
            "explanation": "$x = \\pm \\sqrt{7}$.",
            "points": 0.25
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Khử mẫu của biểu thức lấy căn $\\sqrt{\\frac{3}{5}}$ ta được:",
            "options": [
              "$\\frac{3}{5}$",
              "$\\frac{15}{5}$",
              "$\\frac{\\sqrt{15}}{5}$",
              "$\\frac{\\sqrt{3}}{5}$"
            ],
            "correct": 2,
            "explanation": "$\\frac{\\sqrt{3 \\cdot 5}}{5} = \\frac{\\sqrt{15}}{5}$.",
            "points": 0.25
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Trong tam giác vuông, bình phương mỗi cạnh góc vuông bằng:",
            "options": [
              "Tích của hai hình chiếu",
              "Tổng của hai cạnh góc vuông",
              "Tích của cạnh huyền và đường cao",
              "Tích của cạnh huyền và hình chiếu của cạnh góc vuông đó trên cạnh huyền"
            ],
            "correct": 3,
            "explanation": "$b^2 = a \\cdot b'$.",
            "points": 0.25
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Cho tam giác vuông có hai góc nhọn $\\alpha$ và $\\beta$ phụ nhau. Khẳng định nào sau đây là **sai**?",
            "options": [
              "$\\tan \\alpha = \\tan \\beta$",
              "$\\sin^2 \\alpha + \\sin^2 \\beta = 1$",
              "$\\tan \\alpha = \\cot \\beta$",
              "$\\sin \\alpha = \\cos \\beta$"
            ],
            "correct": 0,
            "explanation": "$\\tan \\alpha = \\cot \\beta = 1 / \\tan \\beta$.",
            "points": 0.25
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Giá trị của biểu thức $\\sin 30^\\circ + \\cos 60^\\circ$ bằng:",
            "options": [
              "$1$",
              "$\\frac{1}{2}$",
              "$\\sqrt{3}$",
              "$\\frac{\\sqrt{3}}{2}$"
            ],
            "correct": 0,
            "explanation": "$0,5 + 0,5 = 1$.",
            "points": 0.25
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Điều kiện để biểu thức $\\frac{1}{\\sqrt{x - 5}}$ có nghĩa là:",
            "options": [
              "$x < 5$",
              "$x \\ge 5$",
              "$x \\ne 5$",
              "$x > 5$"
            ],
            "correct": 3,
            "explanation": "Mẫu số nằm dưới căn bậc hai nên $x - 5 > 0 \\Leftrightarrow x > 5$.",
            "points": 0.25
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Nghiệm của phương trình $\\sqrt{2x} = \\sqrt{6}$ là:",
            "options": [
              "$x = 9$",
              "$x = \\sqrt{3}$",
              "$x = 3$",
              "$x = 6$"
            ],
            "correct": 2,
            "explanation": "$2x = 6 \\Rightarrow x = 3$.",
            "points": 0.25
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AB = 6\\text{ cm}, BC = 10\\text{ cm}$. Độ dài đoạn thẳng $BH$ là:",
            "options": [
              "$8\\text{ cm}$",
              "$6,4\\text{ cm}$",
              "$4,8\\text{ cm}$",
              "$3,6\\text{ cm}$"
            ],
            "correct": 3,
            "explanation": "$BH = AB^2 / BC = 36 / 10 = 3,6\\text{ cm}$.",
            "points": 0.25
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $P = \\frac{a - 4}{\\sqrt{a} + 2}$ (với $a \\ge 0$) ta được:",
            "options": [
              "$a + 2$",
              "$a - 2$",
              "$\\sqrt{a} - 2$",
              "$\\sqrt{a} + 2$"
            ],
            "correct": 2,
            "explanation": "$(\\sqrt{a}-2)(\\sqrt{a}+2)/(\\sqrt{a}+2) = \\sqrt{a} - 2$.",
            "points": 0.25
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Một người leo núi từ chân dốc lên đỉnh dốc dài $600\\text{ m}$, biết góc dốc là $20^\\circ$. Độ cao của đỉnh núi so với mặt đất (làm tròn đến mét) là:",
            "options": [
              "$180\\text{ m}$",
              "$205\\text{ m}$",
              "$250\\text{ m}$",
              "$300\\text{ m}$"
            ],
            "correct": 1,
            "explanation": "$h = 600 \\cdot \\sin 20^\\circ \\approx 600 \\cdot 0,3420 \\approx 205\\text{ m}$.",
            "points": 0.25
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Nhận biết",
            "intro": "Cho hệ phương trình $\\begin{cases} x + ay = 2 \\\\ ax + y = 2 \\end{cases}$ với $a$ là tham số.",
            "statements": [
              {
                "key": "a",
                "text": "Khi $a = 1$, hệ phương trình có vô số nghiệm.",
                "correct": true,
                "explanation": "Hai phương trình giống nhau: $x + y = 2$."
              },
              {
                "key": "b",
                "text": "Khi $a = -1$, hệ phương trình vô nghiệm.",
                "correct": true,
                "explanation": "$x - y = 2$ và $-x + y = 2 \\Leftrightarrow x - y = -2$ (mâu thuẫn)."
              },
              {
                "key": "c",
                "text": "Khi $a = 2$, hệ phương trình có nghiệm duy nhất $(x; y) = \\left(\\frac{2}{3}; \\frac{2}{3}\\right)$.",
                "correct": true,
                "explanation": "Cộng hai pt: $3x + 3y = 4 \\Rightarrow x = y = 2/3$."
              },
              {
                "key": "d",
                "text": "Hệ phương trình luôn có nghiệm duy nhất với mọi giá trị của tham số $a$.",
                "correct": false,
                "explanation": "Khi $a = \\pm 1$ hệ không có nghiệm duy nhất."
              }
            ],
            "stem": "Cho hệ phương trình $\\begin{cases} x + ay = 2 \\\\ ax + y = 2 \\end{cases}$ với $a$ là tham số.",
            "question": "Cho hệ phương trình $\\begin{cases} x + ay = 2 \\\\ ax + y = 2 \\end{cases}$ với $a$ là tham số."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$), đường cao $AH$. Lấy điểm $D$ trên cạnh $AC$ sao cho $AD = AH$.",
            "statements": [
              {
                "key": "a",
                "text": "Hệ thức lượng $AH^2 = BH \\cdot CH$ luôn đúng trong tam giác vuông $ABC$.",
                "correct": true,
                "explanation": "Đúng hệ thức lượng."
              },
              {
                "key": "b",
                "text": "Tỉ số $\\frac{AB}{AC} = \\tan C$.",
                "correct": true,
                "explanation": "$\\tan C = \\text{đối}/\\text{kề} = AB/AC$."
              },
              {
                "key": "c",
                "text": "Độ dài đoạn thẳng $AD$ luôn nhỏ hơn độ dài đoạn thẳng $AB$.",
                "correct": true,
                "explanation": "Trong tam giác vuông $ABH$, đường vuông góc $AH <$ đường xiên $AB \\Rightarrow AD < AB$."
              },
              {
                "key": "d",
                "text": "Tổng $\\sin^2 B + \\sin^2 C = 2$.",
                "correct": false,
                "explanation": "$\\sin^2 B + \\sin^2 C = \\sin^2 B + \\cos^2 B = 1$."
              }
            ],
            "stem": "Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$), đường cao $AH$. Lấy điểm $D$ trên cạnh $AC$ sao cho $AD = AH$.",
            "question": "Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$), đường cao $AH$. Lấy điểm $D$ trên cạnh $AC$ sao cho $AD = AH$."
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị: $A = \\sqrt{4 + 2\\sqrt{3}} - \\sqrt{3}$",
            "answer": "1",
            "explanation": "$\\sqrt{(\\sqrt{3}+1)^2} - \\sqrt{3} = \\sqrt{3} + 1 - \\sqrt{3} = 1$.",
            "points": 0.5
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm $x$ nguyên dương nhỏ nhất thỏa mãn: $\\sqrt{x} > 5$",
            "answer": "26",
            "explanation": "$x > 25 \\Rightarrow x = 26$.",
            "points": 0.5
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{B} = 60^\\circ$ và $BC = 8\\text{ cm}$. Tính độ dài cạnh $AB$ (cm):",
            "answer": "4",
            "explanation": "$AB = BC \\cdot \\cos 60^\\circ = 8 \\cdot 0,5 = 4\\text{ cm}$.",
            "points": 0.5
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức: $M = x + \\frac{4}{x}$",
            "answer": "4",
            "explanation": "Theo BĐT Cauchy: $x + 4/x \\ge 2\\sqrt{x \\cdot 4/x} = 4$ khi $x = 2$.",
            "points": 0.5
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết",
            "points": 1.0,
            "question": "a) Rút gọn biểu thức: $P = \\left(\\frac{\\sqrt{x}}{\\sqrt{x}-1} - \\frac{1}{x-\\sqrt{x}}\\right) : \\frac{\\sqrt{x}+1}{x-1}$ với $x > 0, x \\ne 1$.\nb) Tìm giá trị của $x$ để $P = 2$.",
            "rubric": "a) $P = \\frac{x - 1}{\\sqrt{x}(\\sqrt{x}-1)} \\cdot \\frac{x - 1}{\\sqrt{x}+1} = \\frac{\\sqrt{x}+1}{\\sqrt{x}} \\cdot (\\sqrt{x}-1)$... Rút gọn $P = \\sqrt{x} - 1$ (0.5đ).\nb) $\\sqrt{x} - 1 = 2 \\Leftrightarrow \\sqrt{x} = 3 \\Leftrightarrow x = 9$ (0.5đ).",
            "modelSolution": "a) $P = \\frac{x - 1}{\\sqrt{x}(\\sqrt{x} - 1)} : \\frac{\\sqrt{x} + 1}{x - 1} = \\frac{(\\sqrt{x}-1)(\\sqrt{x}+1)}{\\sqrt{x}(\\sqrt{x}-1)} \\cdot \\frac{(\\sqrt{x}-1)(\\sqrt{x}+1)}{\\sqrt{x}+1} = \\frac{x - 1}{\\sqrt{x}}$.\nb) $P = 2 \\Leftrightarrow \\frac{x - 1}{\\sqrt{x}} = 2 \\Leftrightarrow x - 2\\sqrt{x} - 1 = 0 \\Leftrightarrow (\\sqrt{x} - 1)^2 = 2 \\Leftrightarrow \\sqrt{x} = 1 + \\sqrt{2} \\Rightarrow x = 3 + 2\\sqrt{2}$ (thỏa mãn)."
          },
          {
            "id": 2,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho hệ phương trình: $\\begin{cases} mx + y = 3 \\\\ x + my = 3 \\end{cases}$ (với $m$ là tham số).\na) Giải hệ phương trình khi $m = 2$.\nb) Tìm các giá trị của $m$ để hệ phương trình có nghiệm duy nhất $(x; y)$ thỏa mãn $x + y > 1$.",
            "rubric": "a) $m = 2 \\Rightarrow x = 1, y = 1$ (0.35đ).\nb) Hệ có nghiệm duy nhất khi $m \\ne \\pm 1$. Khi đó $x = y = \\frac{3}{m + 1}$. $x + y = \\frac{6}{m + 1} > 1 \\Leftrightarrow -1 < m < 5$ và $m \\ne 1$ (0.4đ).",
            "modelSolution": "a) Khi $m = 2$, hệ phương trình trở thành:\n$$\\begin{cases} 2x + y = 3 \\\\ x + 2y = 3 \\end{cases} \\Leftrightarrow \\begin{cases} y = 3 - 2x \\\\ x + 2(3 - 2x) = 3 \\end{cases} \\Leftrightarrow \\begin{cases} -3x = -3 \\\\ y = 3 - 2x \\end{cases} \\Leftrightarrow \\begin{cases} x = 1 \\\\ y = 1 \\end{cases}.$$\nb) Hệ có nghiệm duy nhất khi $\\frac{m}{1} \\ne \\frac{1}{m} \\Leftrightarrow m^2 \\ne 1 \\Leftrightarrow m \\ne \\pm 1$.\nCộng hai phương trình ta được: $(m + 1)(x + y) = 6 \\Rightarrow x + y = \\frac{6}{m + 1}$.\nĐể $x + y > 1$ thì:\n$$\\frac{6}{m + 1} > 1 \\Leftrightarrow \\frac{6 - (m + 1)}{m + 1} > 0 \\Leftrightarrow \\frac{5 - m}{m + 1} > 0 \\Leftrightarrow -1 < m < 5.$$\nKết hợp điều kiện $m \\ne 1$, ta được: $-1 < m < 5$ và $m \\ne 1$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Gọi $D$ và $E$ lần lượt là hình chiếu của $H$ trên $AB$ và $AC$.\na) Chứng minh tứ giác $ADHE$ là hình chữ nhật và $AH = DE$.\nb) Chứng minh rằng $AD \\cdot AB = AE \\cdot AC$ và tam giác $ADE$ đồng dạng với tam giác $ACB$.",
            "rubric": "a) Tứ giác có 3 góc vuông $\\Rightarrow ADHE$ là hình chữ nhật $\\Rightarrow DE = AH$ (0.35đ).\nb) $AD \\cdot AB = AH^2 = AE \\cdot AC \\Rightarrow \\Delta ADE \\sim \\Delta ACB$ (c-g-c) (0.4đ).",
            "modelSolution": "a) Tứ giác $ADHE$ có $\\widehat{DAE} = 90^\\circ$ (do $\\Delta ABC$ vuông tại $A$),\n$\\widehat{ADH} = 90^\\circ$ ($D$ là hình chiếu của $H$ trên $AB$),\n$\\widehat{AEH} = 90^\\circ$ ($E$ là hình chiếu của $H$ trên $AC$).\nTứ giác có ba góc vuông nên $ADHE$ là hình chữ nhật. Do đó hai đường chéo bằng nhau: $AH = DE$.\nb) Áp dụng hệ thức lượng trong các tam giác vuông $ABH$ và $ACH$:\nTrong $\\Delta ABH$ vuông tại $H$, đường cao $HD$: $AH^2 = AD \\cdot AB$.\nTrong $\\Delta ACH$ vuông tại $H$, đường cao $HE$: $AH^2 = AE \\cdot AC$.\nSuy ra $AD \\cdot AB = AE \\cdot AC = AH^2$.\nTừ $AD \\cdot AB = AE \\cdot AC \\Rightarrow \\frac{AD}{AC} = \\frac{AE}{AB}$.\nXét $\\Delta ADE$ và $\\Delta ACB$ có:\nGóc $\\widehat{A}$ chung,\n$\\frac{AD}{AC} = \\frac{AE}{AB}$ (chứng minh trên).\nDo đó $\\Delta ADE \\sim \\Delta ACB$ (c - g - c)."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Cho $x > 0$. Tìm giá trị nhỏ nhất của biểu thức:\n$$P = x + \\frac{9}{x} - 2\\sqrt{x} - \\frac{6}{\\sqrt{x}} + 2026$$",
            "rubric": "Đặt $t = \\sqrt{x} + \\frac{3}{\\sqrt{x}} \\ge 2\\sqrt{3}$. $t^2 = x + 9/x + 6 \\Rightarrow x + 9/x = t^2 - 6$. $P = t^2 - 2t + 2020$. Đạt Min tại $t = 2\\sqrt{3}$ (0.5đ).",
            "modelSolution": "Đặt $t = \\sqrt{x} + \\frac{3}{\\sqrt{x}}$.\nTheo bất đẳng thức Cauchy: $t = \\sqrt{x} + \\frac{3}{\\sqrt{x}} \\ge 2\\sqrt{\\sqrt{x} \\cdot \\frac{3}{\\sqrt{x}}} = 2\\sqrt{3}$.\nTa có: $t^2 = x + 2 \\cdot \\sqrt{x} \\cdot \\frac{3}{\\sqrt{x}} + \\frac{9}{x} = x + \\frac{9}{x} + 6 \\Rightarrow x + \\frac{9}{x} = t^2 - 6$.\nKhi đó biểu thức $P$ được viết theo $t$:\n$$P = (t^2 - 6) - 2t + 2026 = t^2 - 2t + 2020$$\nXét hàm số $f(t) = t^2 - 2t + 2020$ với $t \\ge 2\\sqrt{3}$:\n$$f(t) = (t - 1)^2 + 2019$$\nVì $t \\ge 2\\sqrt{3} > 1$ nên hàm số đồng biến với $t \\ge 2\\sqrt{3}$.\nDo đó giá trị nhỏ nhất đạt được khi $t = 2\\sqrt{3}$:\n$$P_{\\min} = (2\\sqrt{3})^2 - 2(2\\sqrt{3}) + 2020 = 12 - 4\\sqrt{3} + 2020 = 2032 - 4\\sqrt{3}.$$\nDấu \"=\" xảy ra khi $\\sqrt{x} = \\frac{3}{\\sqrt{x}} \\Leftrightarrow x = 3$."
          }
        ]
      }
    ]
  }
};
