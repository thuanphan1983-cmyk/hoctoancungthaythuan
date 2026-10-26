/**
 * NGAN HANG DE KIEM TRA DINH KY TOAN THCS (KNTT) - LOP 6, 7, 8, 9
 * Chuan ma tran GDPT moi: 12 Trac nghiem (3.0d) + 2 Dung/Sai (2.0d) + 4 Tra loi ngan (2.0d) + 4 Tu luan (3.0d)
 * Ty le muc do: 40% Nhan biet (4.0d), 30% Thong hieu (3.0d), 20% Van dung (2.0d), 10% Van dung cao (1.0d)
 */
window.PERIODIC_EXAM_BANK = {
  "6": {
    "mid1": [
      {
        "id": "p_g6_mid1_01",
        "testNum": 1,
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - MÔN TOÁN LỚP 6",
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
              "$3 \\in M$",
              "$8 \\in M$",
              "$9 \\in M$",
              "$4 \\notin M$"
            ],
            "correct": 1,
            "explanation": "Ta có $M = \\{4; 5; 6; 7; 8\\}$. Số $8 \\in M$ là khẳng định đúng."
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Số tự nhiên nào sau đây là số nguyên tố?",
            "options": [
              "$9$",
              "$15$",
              "$17$",
              "$21$"
            ],
            "correct": 2,
            "explanation": "Số $17$ chỉ có hai ước tự nhiên là $1$ và $17$ nên $17$ là số nguyên tố."
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Kết quả của phép nhân hai lũy thừa cùng cơ số $3^4 \\cdot 3^2$ là:",
            "options": [
              "$3^8$",
              "$3^6$",
              "$9^6$",
              "$3^2$"
            ],
            "correct": 1,
            "explanation": "$3^4 \\cdot 3^2 = 3^{4+2} = 3^6$."
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Thứ tự thực hiện phép tính đối với biểu thức có các dấu ngoặc là:",
            "options": [
              "$[\\ ] \\rightarrow (\\ ) \\rightarrow \\{\\ \\}$",
              "$(\\ ) \\rightarrow [\\ ] \\rightarrow \\{\\ \\}$",
              "$\\{\\ \\} \\rightarrow [\\ ] \\rightarrow (\\ )$",
              "$(\\ ) \\rightarrow \\{\\ \\} \\rightarrow [\\ ]$"
            ],
            "correct": 1,
            "explanation": "Thứ tự ưu tiên đúng: ngoặc tròn $(\\ )$, rồi ngoặc vuông $[\\ ]$, cuối cùng là ngoặc nhọn $\\{\\ \\}$."
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Số nào sau đây chia hết cho cả $2$ và $5$?",
            "options": [
              "$124$",
              "$235$",
              "$350$",
              "$418$"
            ],
            "correct": 2,
            "explanation": "Số có chữ số tận cùng là $0$ thì chia hết cho cả $2$ và $5$. Do đó số $350$ chia hết cho cả $2$ và $5$."
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Trong các số sau, số nào chia hết cho $9$?",
            "options": [
              "$135$",
              "$241$",
              "$502$",
              "$671$"
            ],
            "correct": 0,
            "explanation": "Số $135$ có tổng các chữ số là $1 + 3 + 5 = 9 \\ \\vdots \\ 9$ nên $135$ chia hết cho $9$."
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Hình tam giác đều có đặc điểm nào sau đây?",
            "options": [
              "Có hai cạnh bằng nhau",
              "Có 3 cạnh bằng nhau và 3 góc bằng nhau",
              "Có một góc vuông",
              "Có hai đường chéo bằng nhau"
            ],
            "correct": 1,
            "explanation": "Tam giác đều có 3 cạnh bằng nhau và 3 góc bằng nhau (mỗi góc bằng $60^\\circ$)."
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Hình thoi có độ dài hai đường chéo là $6\\text{ cm}$ và $8\\text{ cm}$. Diện tích của hình thoi là:",
            "options": [
              "$48\\text{ cm}^2$",
              "$24\\text{ cm}^2$",
              "$14\\text{ cm}^2$",
              "$28\\text{ cm}^2$"
            ],
            "correct": 1,
            "explanation": "Diện tích hình thoi: $S = \\frac{1}{2} \\cdot 6 \\cdot 8 = 24\\text{ cm}^2$."
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
            "explanation": "$18 : 3^2 + 5 \\cdot 2 = 18 : 9 + 10 = 2 + 10 = 12$."
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Biết số tự nhiên $\\overline{1x5}$ chia hết cho $3$. Chữ số $x$ có thể nhận giá trị nào sau đây?",
            "options": [
              "$1$",
              "$2$",
              "$3$",
              "$4$"
            ],
            "correct": 2,
            "explanation": "Tổng các chữ số: $1 + x + 5 = 6 + x \\ \\vdots \\ 3$. Với $x = 3$ thì $6 + 3 = 9 \\ \\vdots \\ 3$."
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Ước chung lớn nhất của $24$ và $36$ là:",
            "options": [
              "$6$",
              "$12$",
              "$72$",
              "$18$"
            ],
            "correct": 1,
            "explanation": "Ta có $24 = 2^3 \\cdot 3$ và $36 = 2^2 \\cdot 3^2 \\Rightarrow \\text{ƯCLN}(24, 36) = 2^2 \\cdot 3 = 12$."
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Một mảnh sân hình chữ nhật có chiều dài $12\\text{ m}$ và chiều rộng $5\\text{ m}$. Chu vi của mảnh sân đó là:",
            "options": [
              "$60\\text{ m}$",
              "$34\\text{ m}$",
              "$17\\text{ m}$",
              "$70\\text{ m}$"
            ],
            "correct": 1,
            "explanation": "Chu vi hình chữ nhật: $C = 2 \\cdot (12 + 5) = 2 \\cdot 17 = 34\\text{ m}$."
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "intro": "Cho hai số tự nhiên $A = 2^3 \\cdot 3 \\cdot 5^2$ và $B = 2^2 \\cdot 3^2 \\cdot 7$.",
            "statements": [
              {
                "key": "a",
                "text": "Số $A$ chia hết cho $10$.",
                "correct": true,
                "explanation": "Vì $A$ chứa cả thừa số $2$ và $5$ nên $A \\ \\vdots \\ (2 \\cdot 5) = 10$."
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
                "explanation": "Tập hợp các ước tự nhiên của $12$ là $\\{1; 2; 3; 4; 6; 12\\}$ gồm $6$ phần tử."
              },
              {
                "key": "d",
                "text": "Bội chung nhỏ nhất của $A$ và $B$ là $\\text{BCNN}(A, B) = 12\\ 600$.",
                "correct": true,
                "explanation": "$\\text{BCNN}(A, B) = 2^3 \\cdot 3^2 \\cdot 5^2 \\cdot 7 = 8 \\cdot 9 \\cdot 25 \\cdot 7 = 12\\ 600$."
              }
            ]
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
            ]
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức: $P = 75 - (3 \\cdot 5^2 - 4 \\cdot 2^3)$",
            "answer": "32",
            "explanation": "$3 \\cdot 25 - 4 \\cdot 8 = 75 - 32 = 43$. Khi đó $P = 75 - 43 = 32$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số tự nhiên $x$ thỏa mãn: $3 \\cdot (x - 4) = 27$",
            "answer": "13",
            "explanation": "$x - 4 = 27 : 3 = 9 \\Rightarrow x = 9 + 4 = 13$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Một đội tình nguyện viên có $36$ nam và $48$ nữ được chia đều vào các tổ sao cho số nam và nữ ở mỗi tổ đều bằng nhau. Hỏi có thể chia được nhiều nhất thành bao nhiêu tổ?",
            "answer": "12",
            "explanation": "Số tổ nhiều nhất là $\\text{ƯCLN}(36, 48) = 12$ tổ."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm chữ số $a$ để số tự nhiên $\\overline{4a10}$ chia hết cho $9$:",
            "answer": "4",
            "explanation": "Tổng các chữ số: $4 + a + 1 + 0 = 5 + a$. Để số chia hết cho $9$ thì $5 + a \\ \\vdots \\ 9 \\Rightarrow a = 4$."
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết - Thông hiểu",
            "points": 1.0,
            "question": "Thực hiện phép tính một cách hợp lý:\na) $28 \\cdot 76 + 28 \\cdot 24 - 800$\nb) $120 : [54 - (5 - 1)^2 \\cdot 2]$",
            "rubric": "a) Tính nhanh bằng tính chất phân phối: $28(76 + 24) - 800 = 28 \\cdot 100 - 800 = 2800 - 800 = 2000$ (0.5đ).\nb) Tính lũy thừa và trong ngoặc: $(5 - 1)^2 \\cdot 2 = 16 \\cdot 2 = 32$. $54 - 32 = 22$. Kết quả $120 : 22 = \\frac{60}{11}$ (0.5đ).",
            "modelSolution": "a) $28 \\cdot 76 + 28 \\cdot 24 - 800 = 28 \\cdot (76 + 24) - 800 = 28 \\cdot 100 - 800 = 2800 - 800 = 2000$.\nb) Ta có: $(5 - 1)^2 \\cdot 2 = 4^2 \\cdot 2 = 16 \\cdot 2 = 32$.\n$54 - 32 = 22$. Do đó biểu thức bằng: $120 : 22 = \\frac{60}{11}$."
          },
          {
            "id": 2,
            "level": "Thông hiểu - Vận dụng",
            "points": 0.75,
            "question": "Tìm số tự nhiên $x$, biết:\na) $2x + 15 = 45$\nb) $5^{x+1} - 5^x = 500$",
            "rubric": "a) $2x = 30 \\Rightarrow x = 15$ (0.35đ).\nb) $5^x(5 - 1) = 500 \\Leftrightarrow 4 \\cdot 5^x = 500 \\Leftrightarrow 5^x = 125 = 5^3 \\Rightarrow x = 3$ (0.4đ).",
            "modelSolution": "a) $2x + 15 = 45 \\Leftrightarrow 2x = 45 - 15 = 30 \\Leftrightarrow x = 15$.\nb) $5^{x+1} - 5^x = 500 \\Leftrightarrow 5^x \\cdot 5 - 5^x = 500 \\Leftrightarrow 5^x \\cdot (5 - 1) = 500 \\Leftrightarrow 5^x \\cdot 4 = 500 \\Leftrightarrow 5^x = 125 \\Leftrightarrow 5^x = 5^3 \\Rightarrow x = 3$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Bác Ba có một khu đất hình chữ nhật dài $24\\text{ m}$, rộng $18\\text{ m}$. Bác muốn lát kín khu đất bằng các viên gạch men hình vuông có độ dài cạnh lớn nhất sao cho các viên gạch được lát liền nhau không phải cắt viên nào.\na) Hỏi độ dài cạnh viên gạch men hình vuông lớn nhất là bao nhiêu mét?\nb) Bác Ba cần dùng tất cả bao nhiêu viên gạch như thế?",
            "rubric": "a) Cạnh viên gạch là ước chung của $24$ và $18$. Cạnh lớn nhất nên bằng $\\text{ƯCLN}(24, 18) = 6\\text{ m}$ (0.4đ).\nb) Số viên gạch cần dùng: $(24 : 6) \\times (18 : 6) = 4 \\times 3 = 12$ viên (0.35đ).",
            "modelSolution": "a) Để lát kín khu đất mà không phải cắt gạch thì độ dài cạnh viên gạch hình vuông phải là ước chung của chiều dài và chiều rộng. Do độ dài cạnh viên gạch là lớn nhất nên độ dài đó bằng $\\text{ƯCLN}(24, 18)$.\nTa có: $24 = 2^3 \\cdot 3$ và $18 = 2 \\cdot 3^2 \\Rightarrow \\text{ƯCLN}(24, 18) = 2 \\cdot 3 = 6\\text{ (m)}$.\nVậy độ dài cạnh viên gạch hình vuông lớn nhất là $6\\text{ m}$.\nb) Chiều dài cần lát: $24 : 6 = 4$ viên.\nChiều rộng cần lát: $18 : 6 = 3$ viên.\nTổng số viên gạch cần dùng để lát kín khu đất là: $4 \\times 3 = 12$ viên."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Cho tổng $S = 1 + 3 + 3^2 + 3^3 + \\dots + 3^{59}$. Chứng minh rằng $S$ chia hết cho $13$.",
            "rubric": "Nhóm mỗi 3 số hạng liên tiếp: $S$ có 60 số hạng chia thành 20 nhóm. Mỗi nhóm chứa nhân tử chung $(1 + 3 + 9) = 13 \\Rightarrow S \\ \\vdots \\ 13$ (0.5đ).",
            "modelSolution": "Tổng $S$ có $60$ số hạng. Ta nhóm $3$ số hạng liên tiếp thành một nhóm:\n$$S = (1 + 3 + 3^2) + (3^3 + 3^4 + 3^5) + \\dots + (3^{57} + 3^{58} + 3^{59})$$\n$$S = (1 + 3 + 9) + 3^3(1 + 3 + 9) + \\dots + 3^{57}(1 + 3 + 9)$$\n$$S = 13 + 3^3 \\cdot 13 + \\dots + 3^{57} \\cdot 13 = 13 \\cdot (1 + 3^3 + \\dots + 3^{57})$$\nVì $13 \\ \\vdots \\ 13$ nên $S \\ \\vdots \\ 13$ (điều phải chứng minh)."
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
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - MÔN TOÁN LỚP 7",
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
              "$\\frac{-3}{4} \\in \\mathbb{Q}$",
              "$0 \\notin \\mathbb{Q}$",
              "$5 \\notin \\mathbb{Q}$",
              "$\\sqrt{2} \\in \\mathbb{Q}$"
            ],
            "correct": 0,
            "explanation": "Số $\\frac{-3}{4}$ viết được dưới dạng phân số $\\frac{a}{b}$ với $a, b \\in \\mathbb{Z}, b \\ne 0$ nên $\\frac{-3}{4} \\in \\mathbb{Q}$."
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Số đối của số hữu tỉ $\\frac{-5}{7}$ là:",
            "options": [
              "$\\frac{5}{7}$",
              "$\\frac{-7}{5}$",
              "$\\frac{7}{5}$",
              "$\\frac{-5}{-7}$"
            ],
            "correct": 0,
            "explanation": "Số đối của số hữu tỉ $x$ là $-x$. Do đó số đối của $\\frac{-5}{7}$ là $-\\left(\\frac{-5}{7}\\right) = \\frac{5}{7}$."
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Trong các số hữu tỉ sau, số nào là số hữu tỉ dương?",
            "options": [
              "$-\\frac{2}{3}$",
              "$\\frac{-4}{-5}$",
              "$\\frac{0}{7}$",
              "$\\frac{-1}{9}$"
            ],
            "correct": 1,
            "explanation": "Ta có $\\frac{-4}{-5} = \\frac{4}{5} > 0$ là số hữu tỉ dương."
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Kết quả của phép tính $\\left(-\\frac{2}{3}\\right)^3$ là:",
            "options": [
              "$-\\frac{6}{9}$",
              "$-\\frac{8}{27}$",
              "$\\frac{8}{27}$",
              "$-\\frac{8}{9}$"
            ],
            "correct": 1,
            "explanation": "$\\left(-\\frac{2}{3}\\right)^3 = \\frac{(-2)^3}{3^3} = -\\frac{8}{27}$."
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Với mọi $x \\in \\mathbb{Q}, x \\ne 0$ và $m, n \\in \\mathbb{N}$, công thức nhân hai lũy thừa cùng cơ số là:",
            "options": [
              "$x^m \\cdot x^n = x^{m \\cdot n}$",
              "$x^m \\cdot x^n = x^{m + n}$",
              "$(x^m)^n = x^{m + n}$",
              "$x^m : x^n = x^{m : n}$"
            ],
            "correct": 1,
            "explanation": "Quy tắc: Khi nhân hai lũy thừa cùng cơ số, ta giữ nguyên cơ số và cộng các số mũ: $x^m \\cdot x^n = x^{m + n}$."
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Cho $x + \\frac{1}{3} = \\frac{4}{5}$. Theo quy tắc chuyển vế, ta suy ra:",
            "options": [
              "$x = \\frac{4}{5} + \\frac{1}{3}$",
              "$x = \\frac{4}{5} - \\frac{1}{3}$",
              "$x = -\\frac{4}{5} - \\frac{1}{3}$",
              "$x = \\frac{1}{3} - \\frac{4}{5}$"
            ],
            "correct": 1,
            "explanation": "Quy tắc chuyển vế: Khi chuyển một số hạng từ vế này sang vế kia của một đẳng thức, ta phải đổi dấu số hạng đó: $x = \\frac{4}{5} - \\frac{1}{3}$."
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Khẳng định nào sau đây về hai góc đối đỉnh là **đúng**?",
            "options": [
              "Hai góc đối đỉnh thì có tổng số đo bằng $180^\\circ$",
              "Hai góc bằng nhau thì đối đỉnh",
              "Hai góc đối đỉnh thì bằng nhau",
              "Hai góc đối đỉnh là hai góc kề bù"
            ],
            "correct": 2,
            "explanation": "Định lí: Hai góc đối đỉnh thì bằng nhau."
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Cho $\\widehat{xOy} = 70^\\circ$. Góc đối đỉnh với $\\widehat{xOy}$ có số đo là:",
            "options": [
              "$110^\\circ$",
              "$70^\\circ$",
              "$20^\\circ$",
              "$90^\\circ$"
            ],
            "correct": 1,
            "explanation": "Hai góc đối đỉnh có số đo bằng nhau nên góc đối đỉnh với $\\widehat{xOy}$ cũng bằng $70^\\circ$."
          },
          {
            "id": 9,
            "level": "Thông hiểu",
            "question": "Kết quả của phép tính $\\frac{3}{4} - \\frac{1}{2} : \\frac{2}{3}$ là:",
            "options": [
              "$0$",
              "$\\frac{1}{4}$",
              "$\\frac{3}{8}$",
              "$1$"
            ],
            "correct": 0,
            "explanation": "$\\frac{3}{4} - \\frac{1}{2} : \\frac{2}{3} = \\frac{3}{4} - \\frac{1}{2} \\cdot \\frac{3}{2} = \\frac{3}{4} - \\frac{3}{4} = 0$."
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Cho biết tia $Oz$ là tia phân giác của $\\widehat{xOy}$ và $\\widehat{xOy} = 80^\\circ$. Số đo của góc $\\widehat{xOz}$ là:",
            "options": [
              "$160^\\circ$",
              "$40^\\circ$",
              "$80^\\circ$",
              "$50^\\circ$"
            ],
            "correct": 1,
            "explanation": "Vì $Oz$ là tia phân giác nên $\\widehat{xOz} = \\frac{\\widehat{xOy}}{2} = \\frac{80^\\circ}{2} = 40^\\circ$."
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Cho hai đường thẳng $a \\parallel b$. Một đường thẳng $c$ cắt $a, b$ lần lượt tại $A$ và $B$. Biết một góc so le trong có số đo bằng $65^\\circ$. Số đo của góc so le trong còn lại là:",
            "options": [
              "$115^\\circ$",
              "$65^\\circ$",
              "$25^\\circ$",
              "$90^\\circ$"
            ],
            "correct": 1,
            "explanation": "Nếu hai đường thẳng song song bị cắt bởi một đường thẳng thứ ba thì hai góc so le trong bằng nhau, nên góc đó có số đo là $65^\\circ$."
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Tìm $x$, biết $x^2 = \\frac{16}{25}$:",
            "options": [
              "$x = \\frac{4}{5}$",
              "$x = -\\frac{4}{5}$",
              "$x = \\frac{4}{5}$ hoặc $x = -\\frac{4}{5}$",
              "$x = \\frac{16}{50}$"
            ],
            "correct": 2,
            "explanation": "Vì $\\left(\\frac{4}{5}\\right)^2 = \\frac{16}{25}$ và $\\left(-\\frac{4}{5}\\right)^2 = \\frac{16}{25}$ nên $x = \\pm \\frac{4}{5}$."
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "intro": "Cho hai biểu thức số hữu tỉ: $A = \\left(-\\frac{1}{2}\\right)^3 : \\frac{1}{4} + \\frac{3}{2}$ và $B = \\frac{5}{7} \\cdot \\frac{13}{19} + \\frac{5}{7} \\cdot \\frac{6}{19}$.",
            "statements": [
              {
                "key": "a",
                "text": "Biểu thức $A$ có chứa lũy thừa với số mũ lẻ nên $\\left(-\\frac{1}{2}\\right)^3 = -\\frac{1}{8}$.",
                "correct": true,
                "explanation": "$\\left(-\\frac{1}{2}\\right)^3 = -\\frac{1}{8}$ (số mũ lẻ của số âm cho kết quả âm)."
              },
              {
                "key": "b",
                "text": "Giá trị của biểu thức $A$ bằng $1$.",
                "correct": true,
                "explanation": "$A = -\\frac{1}{8} \\cdot 4 + \\frac{3}{2} = -\\frac{1}{2} + \\frac{3}{2} = 1$."
              },
              {
                "key": "c",
                "text": "Áp dụng tính chất phân phối, ta có $B = \\frac{5}{7} \\cdot \\left(\\frac{13}{19} + \\frac{6}{19}\\right)$.",
                "correct": true,
                "explanation": "Đúng theo tính chất phân phối của phép nhân đối với phép cộng."
              },
              {
                "key": "d",
                "text": "Giá trị của biểu thức $B$ là một số nguyên.",
                "correct": false,
                "explanation": "$B = \\frac{5}{7} \\cdot 1 = \\frac{5}{7} \\notin \\mathbb{Z}$ (không phải là số nguyên)."
              }
            ]
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "intro": "Cho hai đường thẳng phân biệt $a$ và $b$ cùng vuông góc với đường thẳng $c$ ($a \\perp c$ và $b \\perp c$). Một đường thẳng $d$ cắt $a$ tại $C$ và cắt $b$ tại $D$ sao cho góc $\\widehat{ACD} = 120^\\circ$.",
            "statements": [
              {
                "key": "a",
                "text": "Hai đường thẳng $a$ và $b$ song song với nhau ($a \\parallel b$).",
                "correct": true,
                "explanation": "Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau."
              },
              {
                "key": "b",
                "text": "Hai góc $\\widehat{ACD}$ và $\\widehat{CDB}$ là hai góc so le trong.",
                "correct": false,
                "explanation": "Hai góc $\\widehat{ACD}$ và $\\widehat{CDB}$ nằm cùng một phía đối với cát tuyến $d$ nên là hai góc trong cùng phía."
              },
              {
                "key": "c",
                "text": "Số đo của góc $\\widehat{CDB}$ bằng $60^\\circ$.",
                "correct": true,
                "explanation": "Vì $a \\parallel b$ nên hai góc trong cùng phía bù nhau: $\\widehat{CDB} = 180^\\circ - 120^\\circ = 60^\\circ$."
              },
              {
                "key": "d",
                "text": "Tia phân giác của góc $\\widehat{CDB}$ tạo với đường thẳng $b$ một góc $30^\\circ$.",
                "correct": true,
                "explanation": "Tia phân giác chia đôi góc $60^\\circ$ thành hai góc bằng nhau: $60^\\circ : 2 = 30^\\circ$."
              }
            ]
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức $M = \\frac{2}{3} + \\left(-\\frac{1}{6}\\right) \\cdot 2$ (viết kết quả dưới dạng phân số tối giản a/b):",
            "answer": "1/3",
            "explanation": "$M = \\frac{2}{3} + \\left(-\\frac{1}{3}\\right) = \\frac{1}{3}$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm số hữu tỉ $x > 0$, biết rằng: $\\left(x - \\frac{1}{3}\\right)^2 = \\frac{4}{9}$",
            "answer": "1",
            "explanation": "$x - \\frac{1}{3} = \\frac{2}{3} \\Rightarrow x = \\frac{2}{3} + \\frac{1}{3} = 1$ (do $x > 0$)."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho hình vẽ có hai đường thẳng song song $xx' \\parallel yy'$. Một cát tuyến cắt $xx'$ tại $A$ và cắt $yy'$ tại $B$. Biết góc $\\widehat{xAB} = 75^\\circ$. Tính số đo của góc so le trong $\\widehat{ABy'}$ (đơn vị: độ):",
            "answer": "75",
            "explanation": "Vì $xx' \\parallel yy'$ nên hai góc so le trong bằng nhau: $\\widehat{ABy'} = \\widehat{xAB} = 75^\\circ$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của biểu thức: $A = \\left|x - \\frac{3}{5}\\right| + 2026$",
            "answer": "2026",
            "explanation": "Vì $\\left|x - \\frac{3}{5}\\right| \\ge 0$ với mọi $x \\in \\mathbb{Q}$ nên $A \\ge 2026$. Dấu \"=\" xảy ra khi $x = \\frac{3}{5}$."
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết - Thông hiểu",
            "points": 1.0,
            "question": "Tính giá trị của các biểu thức sau một cách hợp lý:\na) $A = \\frac{11}{24} - \\frac{5}{41} + \\frac{13}{24} + 0,5 - \\frac{36}{41}$\nb) $B = \\left(-\\frac{3}{4}\\right)^2 : \\frac{9}{8} - \\frac{2}{3} \\cdot \\left(\\frac{3}{4} - \\frac{1}{2}\\right)$",
            "rubric": "a) Nhóm phân số cùng mẫu: $(\\frac{11}{24} + \\frac{13}{24}) - (\\frac{5}{41} + \\frac{36}{41}) + 0.5 = 1 - 1 + 0.5 = 0.5$ (0.5đ).\nb) $\\frac{9}{16} \\cdot \\frac{8}{9} - \\frac{2}{3} \\cdot \\frac{1}{4} = \\frac{1}{2} - \\frac{1}{6} = \\frac{2}{6} = \\frac{1}{3}$ (0.5đ).",
            "modelSolution": "a) $A = \\left(\\frac{11}{24} + \\frac{13}{24}\\right) - \\left(\\frac{5}{41} + \\frac{36}{41}\\right) + 0,5 = \\frac{24}{24} - \\frac{41}{41} + 0,5 = 1 - 1 + 0,5 = 0,5$.\nb) $B = \\frac{9}{16} \\cdot \\frac{8}{9} - \\frac{2}{3} \\cdot \\frac{1}{4} = \\frac{1}{2} - \\frac{1}{6} = \\frac{3 - 1}{6} = \\frac{2}{6} = \\frac{1}{3}$."
          },
          {
            "id": 2,
            "level": "Thông hiểu - Vận dụng",
            "points": 0.75,
            "question": "Tìm số hữu tỉ $x$, biết:\na) $\\frac{3}{4} + \\frac{1}{4}x = -\\frac{1}{2}$\nb) $(2x - 1)^3 = -\\frac{8}{27}$",
            "rubric": "a) $\\frac{1}{4}x = -\\frac{1}{2} - \\frac{3}{4} = -\\frac{5}{4} \\Rightarrow x = -5$ (0.35đ).\nb) $2x - 1 = -\\frac{2}{3} \\Rightarrow 2x = \\frac{1}{3} \\Rightarrow x = \\frac{1}{6}$ (0.4đ).",
            "modelSolution": "a) $\\frac{1}{4}x = -\\frac{1}{2} - \\frac{3}{4} \\Leftrightarrow \\frac{1}{4}x = -\\frac{5}{4} \\Leftrightarrow x = -\\frac{5}{4} : \\frac{1}{4} = -5$.\nb) $(2x - 1)^3 = \\left(-\\frac{2}{3}\\right)^3 \\Leftrightarrow 2x - 1 = -\\frac{2}{3} \\Leftrightarrow 2x = 1 - \\frac{2}{3} = \\frac{1}{3} \\Leftrightarrow x = \\frac{1}{6}$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho góc nhọn $\\widehat{xOy} = 60^\\circ$. Trên tia $Ox$ lấy điểm $A$, qua $A$ kẻ đường thẳng $d$ song song với $Oy$.\na) Tính số đo góc $\\widehat{xAd}$ (góc đồng vị với $\\widehat{xOy}$).\nb) Kẻ tia phân giác $Oz$ của $\\widehat{xOy}$ và tia phân giác $At$ của $\\widehat{xAd}$. Chứng minh rằng $At \\parallel Oz$.",
            "rubric": "a) Vì $d \\parallel Oy$ nên hai góc đồng vị bằng nhau: $\\widehat{xAd} = \\widehat{xOy} = 60^\\circ$ (0.35đ).\nb) Chứng minh góc $\\widehat{xOz} = 30^\\circ$ và $\\widehat{xAt} = 30^\\circ$. Hai góc này ở vị trí đồng vị nên $At \\parallel Oz$ (0.4đ).",
            "modelSolution": "a) Vì $d \\parallel Oy$ nên góc $\\widehat{xAd}$ và $\\widehat{xOy}$ là hai góc đồng vị bằng nhau. Do đó: $\\widehat{xAd} = \\widehat{xOy} = 60^\\circ$.\nb) Vì $Oz$ là tia phân giác của $\\widehat{xOy}$ nên $\\widehat{xOz} = \\frac{\\widehat{xOy}}{2} = \\frac{60^\\circ}{2} = 30^\\circ$.\nVì $At$ là tia phân giác của $\\widehat{xAd}$ nên $\\widehat{xAt} = \\frac{\\widehat{xAd}}{2} = \\frac{60^\\circ}{2} = 30^\\circ$.\nSuy ra $\\widehat{xAt} = \\widehat{xOz} = 30^\\circ$. Mà hai góc này ở vị trí đồng vị đối với hai đường thẳng $At$ và $Oz$ bị cắt bởi đường thẳng $Ox$, do đó $At \\parallel Oz$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "So sánh hai lũy thừa sau: $A = 2^{300}$ và $B = 3^{200}$.",
            "rubric": "Đưa về cùng số mũ $100$: $2^{300} = (2^3)^{100} = 8^{100}$; $3^{200} = (3^2)^{100} = 9^{100}$. Vì $8 < 9$ nên $2^{300} < 3^{200}$ (0.5đ).",
            "modelSolution": "Ta có:\n$$A = 2^{300} = 2^{3 \\cdot 100} = (2^3)^{100} = 8^{100}$$\n$$B = 3^{200} = 3^{2 \\cdot 100} = (3^2)^{100} = 9^{100}$$\nVì $8 < 9$ và $100 > 0$ nên $8^{100} < 9^{100}$.\nVậy $2^{300} < 3^{200}$."
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
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - MÔN TOÁN LỚP 8",
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
              "$2x + y$",
              "$3x^2 y z^3$",
              "$\\frac{x}{y}$",
              "$x^2 - 4$"
            ],
            "correct": 1,
            "explanation": "Đơn thức là biểu thức đại số chỉ gồm một số, hoặc một biến, hoặc một tích giữa các số và các biến. Do đó $3x^2 y z^3$ là đơn thức."
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Bậc của đơn thức $5x^3 y^2 z$ là:",
            "options": [
              "$3$",
              "$5$",
              "$6$",
              "$7$"
            ],
            "correct": 2,
            "explanation": "Bậc của đơn thức là tổng số mũ của tất cả các biến: $3 + 2 + 1 = 6$."
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Đơn thức nào sau đây đồng dạng với đơn thức $-4x^2 y$?",
            "options": [
              "$3xy^2$",
              "$\\frac{1}{2}x^2 y$",
              "$-4x^2 y^2$",
              "$2x^3 y$"
            ],
            "correct": 1,
            "explanation": "Hai đơn thức đồng dạng là hai đơn thức có hệ số khác $0$ và có cùng phần biến. $\\frac{1}{2}x^2 y$ có cùng phần biến $x^2 y$."
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Bậc của đa thức $P = 4x^4 y - 3x^2 y^3 - 4x^4 y + 7$ sau khi thu gọn là:",
            "options": [
              "$5$",
              "$4$",
              "$6$",
              "$0$"
            ],
            "correct": 0,
            "explanation": "Thu gọn $P = -3x^2 y^3 + 7$. Hạng tử có bậc cao nhất là $-3x^2 y^3$ có bậc là $2 + 3 = 5$."
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Khai triển hằng đẳng thức $(x + 3)^2$ ta được kết quả là:",
            "options": [
              "$x^2 + 9$",
              "$x^2 + 6x + 9$",
              "$x^2 + 3x + 9$",
              "$x^2 + 6x + 6$"
            ],
            "correct": 1,
            "explanation": "$(x + 3)^2 = x^2 + 2 \\cdot x \\cdot 3 + 3^2 = x^2 + 6x + 9$."
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Viết biểu thức $x^2 - 16$ dưới dạng tích ta được:",
            "options": [
              "$(x - 4)(x + 4)$",
              "$(x - 16)(x + 16)$",
              "$(x - 4)^2$",
              "$(x + 4)^2$"
            ],
            "correct": 0,
            "explanation": "Áp dụng hằng đẳng thức hiệu hai bình phương: $x^2 - 16 = x^2 - 4^2 = (x - 4)(x + 4)$."
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Kết quả của phép nhân đơn thức với đa thức $2x(x^2 - 5)$ là:",
            "options": [
              "$2x^3 - 5$",
              "$2x^3 - 10x$",
              "$2x^3 + 10x$",
              "$3x^3 - 10x$"
            ],
            "correct": 1,
            "explanation": "$2x \\cdot (x^2 - 5) = 2x \\cdot x^2 - 2x \\cdot 5 = 2x^3 - 10x$."
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Kết quả của phép chia đơn thức $15x^4 y^3 : 3x^2 y$ là:",
            "options": [
              "$5x^2 y^2$",
              "$5x^6 y^4$",
              "$12x^2 y^2$",
              "$5x^2 y^3$"
            ],
            "correct": 0,
            "explanation": "$15x^4 y^3 : 3x^2 y = (15 : 3) \\cdot (x^4 : x^2) \\cdot (y^3 : y) = 5x^2 y^2$."
          },
          {
            "id": 9,
            "level": "Nhận biết",
            "question": "Tổng số đo bốn góc trong một tứ giác lồi luôn bằng:",
            "options": [
              "$180^\\circ$",
              "$360^\\circ$",
              "$90^\\circ$",
              "$270^\\circ$"
            ],
            "correct": 1,
            "explanation": "Định lí: Tổng các góc của một tứ giác bằng $360^\\circ$."
          },
          {
            "id": 10,
            "level": "Nhận biết",
            "question": "Khẳng định nào sau đây về tính chất của hình thang cân là **sai**?",
            "options": [
              "Hai cạnh bên bằng nhau",
              "Hai góc kề một đáy bằng nhau",
              "Hai đường chéo vuông góc với nhau",
              "Hai đường chéo bằng nhau"
            ],
            "correct": 2,
            "explanation": "Hình thang cân có hai đường chéo bằng nhau chứ không nhất thiết vuông góc với nhau."
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Phân tích đa thức $x^2 - 4x + 4 - y^2$ thành nhân tử ta được:",
            "options": [
              "$(x - 2 - y)(x - 2 + y)$",
              "$(x - 2)^2 - y^2$",
              "$(x + 2 - y)(x + 2 + y)$",
              "$(x - y - 4)(x + y + 4)$"
            ],
            "correct": 0,
            "explanation": "$(x^2 - 4x + 4) - y^2 = (x - 2)^2 - y^2 = (x - 2 - y)(x - 2 + y)$."
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Cho tứ giác $ABCD$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = 100^\\circ$. Số đo của góc $\\widehat{D}$ là:",
            "options": [
              "$110^\\circ$",
              "$120^\\circ$",
              "$90^\\circ$",
              "$100^\\circ$"
            ],
            "correct": 0,
            "explanation": "$\\widehat{D} = 360^\\circ - (70^\\circ + 80^\\circ + 100^\\circ) = 360^\\circ - 250^\\circ = 110^\\circ$."
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "intro": "Cho hai đa thức $M = 3x^2 y - 2xy^2 + 5$ và $N = x^2 y + 2xy^2 - 3$.",
            "statements": [
              {
                "key": "a",
                "text": "Đa thức $M + N$ sau khi thu gọn bằng $4x^2 y + 2$.",
                "correct": true,
                "explanation": "$M + N = (3+1)x^2 y + (-2+2)xy^2 + (5-3) = 4x^2 y + 2$."
              },
              {
                "key": "b",
                "text": "Đa thức $M - N$ có chứa hạng tử có bậc 3 đối với biến $y$.",
                "correct": false,
                "explanation": "$M - N = 2x^2 y - 4xy^2 + 8$, biến $y$ có số mũ lớn nhất là $2$."
              },
              {
                "key": "c",
                "text": "Tại $x = 1, y = -1$, giá trị của đa thức $M + N$ bằng $-2$.",
                "correct": true,
                "explanation": "Thay $x = 1, y = -1$: $4(1)^2(-1) + 2 = -4 + 2 = -2$."
              },
              {
                "key": "d",
                "text": "Rút gọn biểu thức $(x + y)^2 - (x - y)^2$ ta được kết quả là $4xy$.",
                "correct": true,
                "explanation": "$(x^2 + 2xy + y^2) - (x^2 - 2xy + y^2) = 4xy$."
              }
            ]
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
                "explanation": "Đoạn thẳng nối trung điểm hai cạnh của tam giác là đường trung bình."
              },
              {
                "key": "b",
                "text": "Tứ giác $BDEC$ là hình thang cân.",
                "correct": true,
                "explanation": "Vì $DE \\parallel BC$ và $\\widehat{B} = \\widehat{C}$ (do $\\Delta ABC$ cân tại $A$) nên $BDEC$ là hình thang cân."
              },
              {
                "key": "c",
                "text": "Nếu $BC = 10\\text{ cm}$ thì độ dài đoạn thẳng $DE = 5\\text{ cm}$.",
                "correct": true,
                "explanation": "Theo tính chất đường trung bình: $DE = \\frac{1}{2} BC = 5\\text{ cm}$."
              },
              {
                "key": "d",
                "text": "Gọi $O$ là giao điểm của hai đường chéo $BE$ và $CD$. Khi đó đoạn thẳng $OB = OD$.",
                "correct": false,
                "explanation": "Trong hình thang cân $BDEC$, ta có $OB = OC$ và $OD = OE$, đoạn $OB \\ne OD$."
              }
            ]
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức $A = x^3 - 3x^2 + 3x - 1$ tại $x = 101$:",
            "answer": "1000000",
            "explanation": "$A = (x - 1)^3 = (101 - 1)^3 = 100^3 = 1\\ 000\\ 000$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tìm giá trị của $x$, biết: $(x - 3)(x + 3) - x(x - 2) = 11$",
            "answer": "10",
            "explanation": "$x^2 - 9 - x^2 + 2x = 11 \\Leftrightarrow 2x - 9 = 11 \\Leftrightarrow 2x = 20 \\Leftrightarrow x = 10$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho hình thang cân $ABCD$ ($AB \\parallel CD$) có $\\widehat{C} = 65^\\circ$. Tính số đo của góc $\\widehat{A}$ (đơn vị: độ):",
            "answer": "115",
            "explanation": "Hai góc kề một cạnh bên bù nhau: $\\widehat{A} = 180^\\circ - \\widehat{D} = 180^\\circ - 65^\\circ = 115^\\circ$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Tìm giá trị nhỏ nhất của biểu thức: $M = x^2 - 6x + y^2 + 4y + 2039$",
            "answer": "2026",
            "explanation": "$M = (x - 3)^2 + (y + 2)^2 - 9 - 4 + 2039 = (x - 3)^2 + (y + 2)^2 + 2026 \\ge 2026$. Dấu \"=\" xảy ra khi $x = 3, y = -2$."
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết - Thông hiểu",
            "points": 1.0,
            "question": "a) Thu gọn đa thức: $A = 5x^2 y - 3xy^2 + 2x^2 y + 4xy^2 - 7$.\nb) Thực hiện phép chia: $(12x^3 y^2 - 9x^2 y^3 + 6x^2 y^2) : (3x^2 y^2)$.",
            "rubric": "a) $A = (5+2)x^2 y + (-3+4)xy^2 - 7 = 7x^2 y + xy^2 - 7$ (0.5đ).\nb) Chia từng hạng tử: $4x - 3y + 2$ (0.5đ).",
            "modelSolution": "a) $A = (5x^2 y + 2x^2 y) + (-3xy^2 + 4xy^2) - 7 = 7x^2 y + xy^2 - 7$.\nb) $(12x^3 y^2 - 9x^2 y^3 + 6x^2 y^2) : (3x^2 y^2) = (12x^3 y^2 : 3x^2 y^2) - (9x^2 y^3 : 3x^2 y^2) + (6x^2 y^2 : 3x^2 y^2) = 4x - 3y + 2$."
          },
          {
            "id": 2,
            "level": "Thông hiểu - Vận dụng",
            "points": 0.75,
            "question": "Phân tích các đa thức sau thành nhân tử:\na) $3x^2 - 6x$\nb) $x^2 - 2xy + y^2 - 25$",
            "rubric": "a) Đặt nhân tử chung: $3x(x - 2)$ (0.35đ).\nb) Nhóm 3 số đầu hằng đẳng thức rồi dùng hiệu hai bình phương: $(x - y)^2 - 5^2 = (x - y - 5)(x - y + 5)$ (0.4đ).",
            "modelSolution": "a) $3x^2 - 6x = 3x(x - 2)$.\nb) $x^2 - 2xy + y^2 - 25 = (x^2 - 2xy + y^2) - 5^2 = (x - y)^2 - 5^2 = (x - y - 5)(x - y + 5)$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Cho hình bình hành $ABCD$. Gọi $E$ và $F$ lần lượt là trung điểm của hai cạnh $AB$ và $CD$.\na) Chứng minh tứ giác $AECF$ là hình bình hành.\nb) Gọi $O$ là giao điểm của hai đường chéo $AC$ và $BD$. Chứng minh ba điểm $E, O, F$ thẳng hàng.",
            "rubric": "a) Chứng minh $AE \\parallel CF$ và $AE = CF = \\frac{1}{2}AB \\Rightarrow AECF$ là hình bình hành (0.4đ).\nb) Do $O$ là trung điểm $AC$ mà $AECF$ là hình bình hành nên $O$ cũng là trung điểm $EF \\Rightarrow E, O, F$ thẳng hàng (0.35đ).",
            "modelSolution": "a) Vì $ABCD$ là hình bình hành nên $AB \\parallel CD$ và $AB = CD$.\nDo $E$ là trung điểm $AB$ nên $AE = \\frac{1}{2} AB$.\nDo $F$ là trung điểm $CD$ nên $CF = \\frac{1}{2} CD$.\nSuy ra $AE = CF$ và $AE \\parallel CF$ (do $AB \\parallel CD$).\nTứ giác $AECF$ có một cặp cạnh đối song song và bằng nhau nên $AECF$ là hình bình hành.\nb) Vì $ABCD$ là hình bình hành nên hai đường chéo $AC$ và $BD$ cắt nhau tại trung điểm của mỗi đường, suy ra $O$ là trung điểm của $AC$.\nLại có $AECF$ là hình bình hành có hai đường chéo là $AC$ và $EF$, nên hai đường chéo này cắt nhau tại trung điểm của mỗi đường. Do $O$ là trung điểm của $AC$ nên $O$ cũng là trung điểm của $EF$.\nVậy ba điểm $E, O, F$ thẳng hàng."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Cho các số thực $x, y$ thỏa mãn: $x^2 + 2y^2 + 2xy - 2x - 4y + 2 = 0$. Tính giá trị của biểu thức $Q = (x - 1)^{2025} + (y - 1)^{2026}$.",
            "rubric": "Biến đổi thành tổng bình phương: $(x + y - 1)^2 + (y - 1)^2 = 0 \\Rightarrow y = 1, x = 0 \\Rightarrow Q = (-1)^{2025} + 0^{2026} = -1$ (0.5đ).",
            "modelSolution": "Ta biến đổi phương trình đã cho như sau:\n$$x^2 + 2y^2 + 2xy - 2x - 4y + 2 = 0$$\n$$(x^2 + 2xy + y^2) - 2(x + y) + 1 + (y^2 - 2y + 1) = 0$$\n$$[(x + y)^2 - 2(x + y) + 1] + (y - 1)^2 = 0$$\n$$(x + y - 1)^2 + (y - 1)^2 = 0$$\nVì $(x + y - 1)^2 \\ge 0$ và $(y - 1)^2 \\ge 0$ với mọi $x, y$ nên đẳng thức xảy ra khi và chỉ khi:\n$$\\begin{cases} x + y - 1 = 0 \\\\ y - 1 = 0 \\end{cases} \\Leftrightarrow \\begin{cases} y = 1 \\\\ x = 0 \\end{cases}$$\nThay $x = 0$ và $y = 1$ vào biểu thức $Q$, ta được:\n$$Q = (0 - 1)^{2025} + (1 - 1)^{2026} = (-1)^{2025} + 0^{2026} = -1 + 0 = -1$$\nVậy $Q = -1$."
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
        "title": "ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ 1 - MÔN TOÁN LỚP 9",
        "topic": "Hệ hai phương trình bậc nhất hai ẩn, Phương trình quy về bậc nhất, Căn bậc hai & Hệ thức lượng trong tam giác vuông",
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
              "$(1; 1)$",
              "$(2; 1)$",
              "$(1; -2)$",
              "$(0; 3)$"
            ],
            "correct": 1,
            "explanation": "Thay $(x; y) = (2; 1)$ vào phương trình: $2(2) - 1 = 4 - 1 = 3$ (thỏa mãn)."
          },
          {
            "id": 2,
            "level": "Nhận biết",
            "question": "Nghiệm của hệ phương trình $\\begin{cases} x + y = 5 \\\\ x - y = 1 \\end{cases}$ là:",
            "options": [
              "$(2; 3)$",
              "$(3; 2)$",
              "$(4; 1)$",
              "$(1; 4)$"
            ],
            "correct": 1,
            "explanation": "Cộng hai phương trình: $2x = 6 \\Rightarrow x = 3$. Thay vào: $y = 5 - 3 = 2$."
          },
          {
            "id": 3,
            "level": "Nhận biết",
            "question": "Tập nghiệm của phương trình tích $(x - 5)(2x + 6) = 0$ là:",
            "options": [
              "$S = \\{5; -3\\}$",
              "$S = \\{-5; 3\\}$",
              "$S = \\{5; 3\\}$",
              "$S = \\{-5; -3\\}$"
            ],
            "correct": 0,
            "explanation": "$x - 5 = 0 \\Rightarrow x = 5$ hoặc $2x + 6 = 0 \\Rightarrow x = -3$."
          },
          {
            "id": 4,
            "level": "Nhận biết",
            "question": "Điều kiện xác định của biểu thức căn bậc hai $\\sqrt{3x - 6}$ là:",
            "options": [
              "$x > 2$",
              "$x \\ge 2$",
              "$x \\le 2$",
              "$x \\ge -2$"
            ],
            "correct": 1,
            "explanation": "Biểu thức dưới dấu căn không âm: $3x - 6 \\ge 0 \\Leftrightarrow 3x \\ge 6 \\Leftrightarrow x \\ge 2$."
          },
          {
            "id": 5,
            "level": "Nhận biết",
            "question": "Giá trị của biểu thức $\\sqrt{(-7)^2}$ là:",
            "options": [
              "$-7$",
              "$7$",
              "$\\pm 7$",
              "$49$"
            ],
            "correct": 1,
            "explanation": "Theo hằng đẳng thức căn bậc hai: $\\sqrt{(-7)^2} = |-7| = 7$."
          },
          {
            "id": 6,
            "level": "Nhận biết",
            "question": "Khai phương một tích $\\sqrt{25 \\cdot 36}$ ta được kết quả là:",
            "options": [
              "$60$",
              "$30$",
              "$900$",
              "$11$"
            ],
            "correct": 1,
            "explanation": "$\\sqrt{25 \\cdot 36} = \\sqrt{25} \\cdot \\sqrt{36} = 5 \\cdot 6 = 30$."
          },
          {
            "id": 7,
            "level": "Nhận biết",
            "question": "Trục căn thức ở mẫu của biểu thức $\\frac{6}{\\sqrt{3}}$ ta được:",
            "options": [
              "$2\\sqrt{3}$",
              "$3\\sqrt{3}$",
              "$6\\sqrt{3}$",
              "$2$"
            ],
            "correct": 0,
            "explanation": "$\\frac{6}{\\sqrt{3}} = \\frac{6\\sqrt{3}}{3} = 2\\sqrt{3}$."
          },
          {
            "id": 8,
            "level": "Nhận biết",
            "question": "Cho tam giác $ABC$ vuông tại $A$. Tỉ số lượng giác $\\sin B$ bằng:",
            "options": [
              "$\\frac{AC}{BC}$",
              "$\\frac{AB}{BC}$",
              "$\\frac{AC}{AB}$",
              "$\\frac{AB}{AC}$"
            ],
            "correct": 0,
            "explanation": "Trong tam giác vuông, $\\sin = \\frac{\\text{cạnh đối}}{\\text{cạnh huyền}} = \\frac{AC}{BC}$."
          },
          {
            "id": 9,
            "level": "Nhận biết",
            "question": "Với góc nhọn $\\alpha$ bất kỳ, khẳng định nào sau đây là **sai**?",
            "options": [
              "$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$",
              "$\\tan \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha}$",
              "$\\sin(90^\\circ - \\alpha) = \\cos \\alpha$",
              "$\\sin \\alpha > 1$"
            ],
            "correct": 3,
            "explanation": "Với mọi góc nhọn $\\alpha$, ta luôn có $0 < \\sin \\alpha < 1$. Khẳng định $\\sin \\alpha > 1$ là sai."
          },
          {
            "id": 10,
            "level": "Thông hiểu",
            "question": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 3\\text{ cm}, AC = 4\\text{ cm}$. Giá trị của $\\tan B$ bằng:",
            "options": [
              "$\\frac{3}{4}$",
              "$\\frac{4}{3}$",
              "$\\frac{4}{5}$",
              "$\\frac{3}{5}$"
            ],
            "correct": 1,
            "explanation": "$\\tan B = \\frac{AC}{AB} = \\frac{4}{3}$."
          },
          {
            "id": 11,
            "level": "Thông hiểu",
            "question": "Rút gọn biểu thức $P = \\sqrt{48} - \\sqrt{27} + \\sqrt{12}$ ta được kết quả là:",
            "options": [
              "$3\\sqrt{3}$",
              "$5\\sqrt{3}$",
              "$9\\sqrt{3}$",
              "$2\\sqrt{3}$"
            ],
            "correct": 0,
            "explanation": "$P = 4\\sqrt{3} - 3\\sqrt{3} + 2\\sqrt{3} = (4 - 3 + 2)\\sqrt{3} = 3\\sqrt{3}$."
          },
          {
            "id": 12,
            "level": "Thông hiểu",
            "question": "Một cột cờ có bóng trên mặt đất dài $10\\text{ m}$. Biết góc tạo bởi tia nắng mặt trời với mặt đất là $60^\\circ$. Chiều cao cột cờ (làm tròn đến hàng phần mười) là:",
            "options": [
              "$17,3\\text{ m}$",
              "$5,8\\text{ m}$",
              "$20,0\\text{ m}$",
              "$14,1\\text{ m}$"
            ],
            "correct": 0,
            "explanation": "$h = 10 \\cdot \\tan 60^\\circ = 10\\sqrt{3} \\approx 17,3\\text{ m}$."
          }
        ],
        "part2": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "intro": "Cho hệ phương trình bậc nhất hai ẩn $\\begin{cases} 2x + y = 7 \\\\ 3x - 2y = 7 \\end{cases}$ và phương trình chứa ẩn ở mẫu $\\frac{x + 1}{x - 2} - \\frac{1}{x} = 1$.",
            "statements": [
              {
                "key": "a",
                "text": "Cặp số $(x; y) = (3; 1)$ là nghiệm duy nhất của hệ phương trình.",
                "correct": true,
                "explanation": "Thay $x = 3, y = 1$: $2(3) + 1 = 7$ và $3(3) - 2(1) = 7$ (thỏa mãn cả 2 phương trình)."
              },
              {
                "key": "b",
                "text": "Điều kiện xác định của phương trình chứa ẩn ở mẫu là $x \\ne 2$ và $x \\ne 0$.",
                "correct": true,
                "explanation": "Mẫu số khác 0: $x - 2 \\ne 0 \\Leftrightarrow x \\ne 2$ và $x \\ne 0$."
              },
              {
                "key": "c",
                "text": "Nhân phương trình đầu với $2$ rồi cộng vế theo vế với phương trình thứ hai ta thu được phương trình một ẩn $7x = 21$.",
                "correct": true,
                "explanation": "$4x + 2y = 14$ cộng $3x - 2y = 7$ cho $7x = 21$."
              },
              {
                "key": "d",
                "text": "Phương trình chứa ẩn ở mẫu có hai nghiệm phân biệt.",
                "correct": false,
                "explanation": "Quy đồng: $x(x+1) - (x-2) = x(x-2) \\Leftrightarrow x^2 + 2 = x^2 - 2x \\Leftrightarrow -2x = 2 \\Leftrightarrow x = -1$ (chỉ có duy nhất 1 nghiệm)."
              }
            ]
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
                "explanation": "$BC = BH + CH = 4 + 9 = 13\\text{ cm}$."
              },
              {
                "key": "b",
                "text": "Độ dài đường cao $AH$ bằng $6\\text{ cm}$.",
                "correct": true,
                "explanation": "Theo hệ thức lượng: $AH^2 = BH \\cdot CH = 4 \\cdot 9 = 36 \\Rightarrow AH = 6\\text{ cm}$."
              },
              {
                "key": "c",
                "text": "Độ dài cạnh góc vuông $AB = 2\\sqrt{13}\\text{ cm}$.",
                "correct": true,
                "explanation": "$AB^2 = BH \\cdot BC = 4 \\cdot 13 = 52 \\Rightarrow AB = \\sqrt{52} = 2\\sqrt{13}\\text{ cm}$."
              },
              {
                "key": "d",
                "text": "Giá trị của $\\sin B$ bằng $\\frac{9}{13}$.",
                "correct": false,
                "explanation": "$\\sin B = \\frac{AC}{BC} = \\frac{\\sqrt{9 \\cdot 13}}{13} = \\frac{3\\sqrt{13}}{13} \\ne \\frac{9}{13}$."
              }
            ]
          }
        ],
        "part3": [
          {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Tìm giá trị của tổng $x_0 + y_0$, biết $(x_0; y_0)$ là nghiệm của hệ phương trình: $\\begin{cases} 3x - y = 5 \\\\ 2x + 3y = 7 \\end{cases}$",
            "answer": "3",
            "explanation": "Nhân pt 1 với 3: $9x - 3y = 15$. Cộng pt 2: $11x = 22 \\Rightarrow x_0 = 2$. $y_0 = 3(2) - 5 = 1$. Tổng $x_0 + y_0 = 3$."
          },
          {
            "id": 2,
            "level": "Thông hiểu",
            "question": "Tính giá trị của biểu thức: $A = \\sqrt{(\\sqrt{3} - 2)^2} + \\sqrt{3}$",
            "answer": "2",
            "explanation": "$A = |\\sqrt{3} - 2| + \\sqrt{3} = 2 - \\sqrt{3} + \\sqrt{3} = 2$."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "question": "Cho tam giác $ABC$ vuông tại $A$, có đường cao $AH$. Biết $AB = 9\\text{ cm}, AC = 12\\text{ cm}$. Tính độ dài đường cao $AH$ (đơn vị: cm, viết dưới dạng số thập phân):",
            "answer": "7.2",
            "explanation": "$BC = \\sqrt{9^2 + 12^2} = 15\\text{ cm}$. $AH = \\frac{AB \\cdot AC}{BC} = \\frac{9 \\cdot 12}{15} = 7,2\\text{ cm}$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "question": "Một chiếc máy bay cất cánh tạo với mặt đất góc $24^\\circ$. Sau $1$ phút, máy bay đạt độ cao $1200\\text{ m}$. Hỏi vận tốc trung bình của máy bay là bao nhiêu km/h? (Làm tròn đến hàng đơn vị; $\\sin 24^\\circ \\approx 0,4067$):",
            "answer": "177",
            "explanation": "Quãng đường $s = 1200 / \\sin 24^\\circ \\approx 2950,6\\text{ m} \\approx 2,95\\text{ km}$. Thời gian $1/60\\text{ h}$. Vận tốc $v \\approx 2,95 \\times 60 \\approx 177\\text{ km/h}$."
          }
        ],
        "part4": [
          {
            "id": 1,
            "level": "Nhận biết - Thông hiểu",
            "points": 1.0,
            "question": "a) Trục căn thức ở mẫu và rút gọn: $A = \\frac{3}{\\sqrt{5} - \\sqrt{2}} - \\frac{3}{\\sqrt{5} + \\sqrt{2}}$.\nb) Cho biểu thức $P = \\frac{\\sqrt{x}}{\\sqrt{x} - 2} - \\frac{4}{x - 2\\sqrt{x}}$ với $x > 0, x \\ne 4$. Rút gọn biểu thức $P$.",
            "rubric": "a) Quy đồng / trục căn thức: $\\frac{3(\\sqrt{5}+\\sqrt{2})}{3} - \\frac{3(\\sqrt{5}-\\sqrt{2})}{3} = 2\\sqrt{2}$ (0.5đ).\nb) Quy đồng mẫu chung $\\sqrt{x}(\\sqrt{x}-2)$: $P = \\frac{x - 4}{\\sqrt{x}(\\sqrt{x}-2)} = \\frac{(\\sqrt{x}-2)(\\sqrt{x}+2)}{\\sqrt{x}(\\sqrt{x}-2)} = \\frac{\\sqrt{x}+2}{\\sqrt{x}}$ (0.5đ).",
            "modelSolution": "a) $A = \\frac{3(\\sqrt{5} + \\sqrt{2})}{(\\sqrt{5} - \\sqrt{2})(\\sqrt{5} + \\sqrt{2})} - \\frac{3(\\sqrt{5} - \\sqrt{2})}{(\\sqrt{5} + \\sqrt{2})(\\sqrt{5} - \\sqrt{2})} = \\frac{3(\\sqrt{5} + \\sqrt{2})}{5 - 2} - \\frac{3(\\sqrt{5} - \\sqrt{2})}{5 - 2} = (\\sqrt{5} + \\sqrt{2}) - (\\sqrt{5} - \\sqrt{2}) = 2\\sqrt{2}$.\nb) Với $x > 0, x \\ne 4$, ta có:\n$$P = \\frac{\\sqrt{x}}{\\sqrt{x} - 2} - \\frac{4}{\\sqrt{x}(\\sqrt{x} - 2)} = \\frac{\\sqrt{x} \\cdot \\sqrt{x} - 4}{\\sqrt{x}(\\sqrt{x} - 2)} = \\frac{x - 4}{\\sqrt{x}(\\sqrt{x} - 2)} = \\frac{(\\sqrt{x} - 2)(\\sqrt{x} + 2)}{\\sqrt{x}(\\sqrt{x} - 2)} = \\frac{\\sqrt{x} + 2}{\\sqrt{x}}$$"
          },
          {
            "id": 2,
            "level": "Thông hiểu - Vận dụng",
            "points": 0.75,
            "question": "Giải bài toán bằng cách lập hệ phương trình:\nHai xí nghiệp theo kế hoạch phải làm tổng cộng $700$ sản phẩm. Do áp dụng kĩ thuật mới, xí nghiệp I đã vượt mức kế hoạch $15\\%$, xí nghiệp II vượt mức kế hoạch $20\\%$, do đó cả hai xí nghiệp đã làm được $820$ sản phẩm. Hỏi theo kế hoạch mỗi xí nghiệp phải làm bao nhiêu sản phẩm?",
            "rubric": "Gọi số sp theo KH của xí nghiệp I và II lần lượt là $x, y$ ($x, y \\in \\mathbb{N}^*, x, y < 700$).\nLập hệ: $\\begin{cases} x + y = 700 \\\\ 1,15x + 1,20y = 820 \\end{cases}$ (0.35đ).\nGiải ra $x = 400, y = 300$ và kết luận (0.4đ).",
            "modelSolution": "Gọi số sản phẩm xí nghiệp I và xí nghiệp II phải làm theo kế hoạch lần lượt là $x$ và $y$ ($x, y \\in \\mathbb{N}^*; x, y < 700$).\nTheo kế hoạch hai xí nghiệp phải làm $700$ sản phẩm nên ta có phương trình:\n$$x + y = 700 \\quad (1)$$\nThực tế, xí nghiệp I vượt mức $15\\%$ nên làm được $1,15x$ sản phẩm;\nxí nghiệp II vượt mức $20\\%$ nên làm được $1,20y$ sản phẩm.\nCả hai xí nghiệp đã làm được $820$ sản phẩm nên ta có phương trình:\n$$1,15x + 1,20y = 820 \\quad (2)$$\nTừ $(1)$ và $(2)$ ta có hệ phương trình:\n$$\\begin{cases} x + y = 700 \\\\ 1,15x + 1,20y = 820 \\end{cases} \\Leftrightarrow \\begin{cases} 1,15x + 1,15y = 805 \\\\ 1,15x + 1,20y = 820 \\end{cases} \\Leftrightarrow \\begin{cases} 0,05y = 15 \\\\ x + y = 700 \\end{cases} \\Leftrightarrow \\begin{cases} y = 300 \\\\ x = 400 \\end{cases} \\text{ (thỏa mãn)}$$\nVậy theo kế hoạch, xí nghiệp I phải làm $400$ sản phẩm, xí nghiệp II phải làm $300$ sản phẩm."
          },
          {
            "id": 3,
            "level": "Vận dụng",
            "points": 0.75,
            "question": "Một người quan sát đứng tại vị trí $A$ trên bờ hồ nhìn thấy đỉnh của một ngọn tháp ở bờ đối diện với góc nâng $35^\\circ$. Người đó lùi xa ra phía sau thêm $25\\text{ m}$ đến vị trí $B$ (ba điểm $B, A$ và chân tháp $C$ thẳng hàng) thì nhìn thấy đỉnh tháp với góc nâng $22^\\circ$.\na) Hãy tính chiều cao của ngọn tháp (làm tròn đến mét).\nb) Tính khoảng cách từ vị trí quan sát ban đầu $A$ đến chân ngọn tháp $C$.",
            "rubric": "Gọi chiều cao ngọn tháp là $h = CD$. $AC = h / \\tan 35^\\circ$, $BC = h / \\tan 22^\\circ$. $BC - AC = 25 \\Rightarrow h(\\frac{1}{\\tan 22^\\circ} - \\frac{1}{\\tan 35^\\circ}) = 25 \\Rightarrow h \\approx 24\\text{ m}$ (0.4đ).\n$AC = 24 / \\tan 35^\\circ \\approx 34\\text{ m}$ (0.35đ).",
            "modelSolution": "Gọi ngọn tháp là $CD$ vuông góc với mặt đất tại chân tháp $C$, chiều cao ngọn tháp là $h = CD$ (m).\nTrong tam giác vuông $ACD$, ta có: $AC = \\frac{h}{\\tan 35^\\circ}$.\nTrong tam giác vuông $BCD$, ta có: $BC = \\frac{h}{\\tan 22^\\circ}$.\nTheo đề bài, khoảng cách giữa hai vị trí quan sát là $AB = BC - AC = 25\\text{ m}$.\nDo đó: $h \\cdot \\left(\\frac{1}{\\tan 22^\\circ} - \\frac{1}{\\tan 35^\\circ}\\right) = 25$\n$$h \\cdot (2,4751 - 1,4281) = 25 \\Leftrightarrow h \\cdot 1,0470 \\approx 25 \\Rightarrow h \\approx \\frac{25}{1,0470} \\approx 23,88 \\approx 24\\text{ (m)}$$\nKhoảng cách từ vị trí ban đầu $A$ đến chân tháp $C$ là:\n$$AC = \\frac{23,88}{\\tan 35^\\circ} \\approx \\frac{23,88}{0,7002} \\approx 34,1 \\approx 34\\text{ (m)}$$\nVậy ngọn tháp cao khoảng $24\\text{ m}$ và khoảng cách từ $A$ đến chân tháp khoảng $34\\text{ m}$."
          },
          {
            "id": 4,
            "level": "Vận dụng cao",
            "points": 0.5,
            "question": "Cho hai số thực dương $x, y$ thỏa mãn $x + y = 2$. Tìm giá trị nhỏ nhất của biểu thức:\n$$M = \\frac{1}{x} + \\frac{1}{y} + \\frac{4}{x^2 + y^2}$$",
            "rubric": "Biến đổi $\\frac{1}{x} + \\frac{1}{y} = \\frac{x+y}{xy} = \\frac{2}{xy} = \\frac{1}{2xy} + \\frac{3}{2xy}$.\nÁp dụng BĐT Cauchy-Schwarz: $\\frac{1}{2xy} + \\frac{4}{x^2+y^2} \\ge \\frac{(1+2)^2}{x^2+2xy+y^2} = \\frac{9}{(x+y)^2} = \\frac{9}{4}$.\nVà $\\frac{3}{2xy} \\ge \\frac{3}{2 \\cdot \\frac{(x+y)^2}{4}} = \\frac{6}{4}$. Tổng $\\text{Min} = \\frac{15}{4} = 3,75$ khi $x = y = 1$ (0.5đ).",
            "modelSolution": "Vì $x, y > 0$ và $x + y = 2$, ta có:\n$$\\frac{1}{x} + \\frac{1}{y} = \\frac{x + y}{xy} = \\frac{2}{xy} = \\frac{1}{2xy} + \\frac{3}{2xy}$$\nKhi đó biểu thức $M$ được viết lại thành:\n$$M = \\left(\\frac{1}{2xy} + \\frac{4}{x^2 + y^2}\\right) + \\frac{3}{2xy}$$\nÁp dụng bất đẳng thức Cauchy-Schwarz dạng Engel:\n$$\\frac{1}{2xy} + \\frac{4}{x^2 + y^2} = \\frac{1^2}{2xy} + \\frac{2^2}{x^2 + y^2} \\ge \\frac{(1 + 2)^2}{2xy + x^2 + y^2} = \\frac{9}{(x + y)^2} = \\frac{9}{2^2} = \\frac{9}{4}$$\nMặt khác, theo bất đẳng thức $xy \\le \\frac{(x + y)^2}{4} = \\frac{4}{4} = 1$, ta có:\n$$\\frac{3}{2xy} \\ge \\frac{3}{2 \\cdot 1} = \\frac{3}{2} = \\frac{6}{4}$$\nCộng hai bất đẳng thức trên lại, ta được:\n$$M \\ge \\frac{9}{4} + \\frac{6}{4} = \\frac{15}{4}$$\nDấu \"=\" xảy ra khi và chỉ khi $\\begin{cases} 2xy = \\frac{x^2 + y^2}{2} \\\\ x = y \\\\ x + y = 2 \\end{cases} \\Leftrightarrow x = y = 1$.\nVậy giá trị nhỏ nhất của $M$ là $\\frac{15}{4}$ (tức $3,75$) đạt được khi $x = y = 1$."
          }
        ]
      }
    ]
  }
};
