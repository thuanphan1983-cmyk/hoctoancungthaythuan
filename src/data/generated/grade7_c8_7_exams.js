// ==============================================================================
// NGÂN HÀNG ĐỀ KIỂM TRA CHƯƠNG VIII: LÀM QUEN VỚI BIẾN CỐ VÀ XÁC SUẤT CỦA BIẾN CỐ - TOÁN 7 (KNTT)
// Chuẩn ma trận khảo thí 2025: Đề 1 & 2 (Khá 40/30/20/10), Đề 3 (Khá Giỏi 20/30/30/20)
// Cập nhật lúc: 2026-11-02 07:40:53
// ==============================================================================

const EXAMS_7_C8_7 = {
  "c8_7_bai1_test1": {
    "title": "Toán 7 - Bài 29: Làm quen với biến cố - Đề 1 (Cơ bản)",
    "time": 45,
    "totalPoints": 10.0,
    "part1": [
      {
        "id": 1,
        "question": "Biến cố nào sau đây là biến cố chắc chắn?",
        "options": [
          "B. Gieo một con xúc xắc 6 mặt thì số chấm xuất hiện nhỏ hơn 7",
          "D. Tháng Hai của một năm có 32 ngày",
          "A. Ngày mai mặt trời mọc ở hướng Tây",
          "C. Gieo một đồng xu thì xuất hiện mặt sấp"
        ],
        "answer": "B",
        "explanation": "Con xúc xắc có các mặt từ 1 đến 6 chấm nên số chấm xuất hiện luôn nhỏ hơn 7, đây là biến cố chắc chắn.",
        "correct": 2
      },
      {
        "id": 2,
        "question": "Biến cố nào sau đây là biến cố không thể?",
        "options": [
          "B. Tung đồng xu xuất hiện mặt ngửa",
          "C. Gieo một con xúc xắc xuất hiện mặt 8 chấm",
          "D. Ngày mai trời có mưa",
          "A. Gieo xúc xắc xuất hiện mặt 6 chấm"
        ],
        "answer": "C",
        "explanation": "Con xúc xắc 6 mặt chỉ có từ 1 đến 6 chấm nên không thể xuất hiện mặt 8 chấm.",
        "correct": 3
      },
      {
        "id": 3,
        "question": "Biến cố nào sau đây là biến cố ngẫu nhiên?",
        "options": [
          "C. Trong hình vuông có 5 góc vuông",
          "B. Chọn ngẫu nhiên một bạn trong lớp và bạn đó là nữ",
          "A. Nước sôi ở 100 độ C trong điều kiện áp suất tiêu chuẩn",
          "D. Gieo xúc xắc được số chấm lớn hơn 0"
        ],
        "answer": "B",
        "explanation": "Biến cố chọn được một bạn nữ không thể biết trước chắc chắn xảy ra hay không xảy ra nên là biến cố ngẫu nhiên.",
        "correct": 2
      },
      {
        "id": 4,
        "question": "Tung một đồng xu 1 lần. Biến cố 'Mặt xuất hiện là mặt ngửa' là:",
        "options": [
          "D. Không phải là biến cố",
          "C. Biến cố ngẫu nhiên",
          "B. Biến cố không thể",
          "A. Biến cố chắc chắn"
        ],
        "answer": "C",
        "explanation": "Đồng xu có 2 mặt sấp hoặc ngửa, ta không thể biết trước mặt nào sẽ xuất hiện nên đây là biến cố ngẫu nhiên.",
        "correct": 3
      },
      {
        "id": 5,
        "question": "Trong hộp có 5 viên bi xanh và 3 viên bi đỏ. Lấy ngẫu nhiên 1 viên bi. Biến cố 'Lấy được viên bi màu vàng' là:",
        "options": [
          "D. Biến cố đồng khả năng",
          "B. Biến cố không thể",
          "C. Biến cố ngẫu nhiên",
          "A. Biến cố chắc chắn"
        ],
        "answer": "B",
        "explanation": "Trong hộp không có bi vàng nên không thể lấy được bi vàng.",
        "correct": 3
      },
      {
        "id": 6,
        "question": "Trong hộp chỉ có 10 viên bi đỏ. Lấy ngẫu nhiên 1 viên bi. Biến cố 'Lấy được viên bi đỏ' là:",
        "options": [
          "A. Biến cố chắc chắn",
          "D. Biến cố có xác suất bằng 0",
          "C. Biến cố ngẫu nhiên",
          "B. Biến cố không thể"
        ],
        "answer": "A",
        "explanation": "Tất cả các viên bi trong hộp đều màu đỏ nên chắc chắn lấy được viên bi màu đỏ.",
        "correct": 0
      },
      {
        "id": 7,
        "question": "Gieo một con xúc xắc 6 mặt cân đối. Biến cố nào là biến cố ngẫu nhiên?",
        "options": [
          "C. Số chấm xuất hiện lớn hơn 0",
          "A. Số chấm xuất hiện là số chia hết cho 7",
          "D. Số chấm xuất hiện nhỏ hơn hoặc bằng 6",
          "B. Số chấm xuất hiện là số lẻ"
        ],
        "answer": "B",
        "explanation": "Số chấm là số lẻ (1, 3, 5) có thể xảy ra hoặc không xảy ra nên là biến cố ngẫu nhiên.",
        "correct": 1
      },
      {
        "id": 8,
        "question": "Có 4 tấm thẻ ghi các số 2, 4, 6, 8. Rút ngẫu nhiên 1 tấm thẻ. Biến cố 'Số trên thẻ rút ra là số chẵn' là:",
        "options": [
          "D. Cả A và B đều đúng",
          "B. Biến cố ngẫu nhiên",
          "A. Biến cố không thể",
          "C. Biến cố chắc chắn"
        ],
        "answer": "C",
        "explanation": "Tất cả các thẻ đều ghi số chẵn nên biến cố rút được số chẵn là biến cố chắc chắn.",
        "correct": 2
      },
      {
        "id": 9,
        "question": "Chọn một ngày bất kì trong tuần. Biến cố 'Ngày được chọn có tên bắt đầu bằng chữ Thứ' là:",
        "options": [
          "D. Biến cố có khả năng 50%",
          "A. Biến cố không thể",
          "C. Biến cố chắc chắn",
          "B. Biến cố ngẫu nhiên"
        ],
        "answer": "B",
        "explanation": "Chủ nhật không bắt đầu bằng chữ Thứ, còn Thứ Hai đến Thứ Bảy thì có, nên là biến cố ngẫu nhiên.",
        "correct": 1
      },
      {
        "id": 10,
        "question": "Gieo hai con xúc xắc cân đối. Biến cố 'Tổng số chấm trên hai con xúc xắc bằng 1' là:",
        "options": [
          "A. Biến cố chắc chắn",
          "D. Biến cố đồng thời",
          "B. Biến cố ngẫu nhiên",
          "C. Biến cố không thể"
        ],
        "answer": "C",
        "explanation": "Mỗi con xúc xắc có ít nhất 1 chấm nên tổng số chấm nhỏ nhất là 1 + 1 = 2, không thể bằng 1.",
        "correct": 0
      },
      {
        "id": 11,
        "question": "Một năm dương lịch có 365 ngày hoặc 366 ngày. Biến cố 'Năm tiếp theo có 367 ngày' là:",
        "options": [
          "D. Biến cố có điều kiện",
          "A. Biến cố chắc chắn",
          "C. Biến cố ngẫu nhiên",
          "B. Biến cố không thể"
        ],
        "answer": "B",
        "explanation": "Năm dương lịch nhiều nhất chỉ có 366 ngày, không thể có 367 ngày.",
        "correct": 1
      },
      {
        "id": 12,
        "question": "Lấy ngẫu nhiên một chữ cái trong từ 'TOAN'. Biến cố 'Chữ cái lấy ra là chữ T' là:",
        "options": [
          "A. Biến cố chắc chắn",
          "C. Biến cố ngẫu nhiên",
          "B. Biến cố không thể",
          "D. Biến cố tuyệt đối"
        ],
        "answer": "C",
        "explanation": "Các chữ cái là T, O, A, N. Ta có thể lấy được T hoặc không, nên là biến cố ngẫu nhiên.",
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 13,
        "stem": "Một hộp chứa 6 quả bóng có kích thước và khối lượng như nhau, ghi các số 1, 2, 3, 4, 5, 6. Lấy ngẫu nhiên một quả bóng.",
        "statements": [
          {
            "id": "a",
            "statement": "Biến cố 'Quả bóng lấy ra ghi số chia hết cho 7' là biến cố không thể.",
            "answer": true,
            "explanation": "Các số từ 1 đến 6 không có số nào chia hết cho 7."
          },
          {
            "id": "b",
            "statement": "Biến cố 'Quả bóng lấy ra ghi số lớn hơn 0' là biến cố chắc chắn.",
            "answer": true,
            "explanation": "Tất cả các số 1, 2, 3, 4, 5, 6 đều lớn hơn 0."
          },
          {
            "id": "c",
            "statement": "Biến cố 'Quả bóng lấy ra ghi số nguyên tố' là biến cố chắc chắn.",
            "answer": false,
            "explanation": "Số 1, 4, 6 không phải là số nguyên tố nên đây là biến cố ngẫu nhiên."
          },
          {
            "id": "d",
            "statement": "Có tất cả 3 kết quả thuận lợi cho biến cố 'Quả bóng lấy ra ghi số chẵn'.",
            "answer": true,
            "explanation": "Các kết quả thuận lợi là 2, 4, 6 (gồm 3 kết quả)."
          }
        ]
      },
      {
        "id": 14,
        "stem": "Gieo đồng thời hai đồng xu cân đối và đồng chất.",
        "statements": [
          {
            "id": "a",
            "statement": "Biến cố 'Có ít nhất một đồng xu xuất hiện mặt sấp' là biến cố ngẫu nhiên.",
            "answer": true,
            "explanation": "Có thể xảy ra (SS, SN, NS) hoặc không xảy ra (NN)."
          },
          {
            "id": "b",
            "statement": "Biến cố 'Cả hai đồng xu đều xuất hiện mặt ngửa' là biến cố chắc chắn.",
            "answer": false,
            "explanation": "Đây là biến cố ngẫu nhiên."
          },
          {
            "id": "c",
            "statement": "Biến cố 'Xuất hiện ba mặt sấp' là biến cố không thể.",
            "answer": true,
            "explanation": "Chỉ có hai đồng xu nên không thể có 3 mặt sấp."
          },
          {
            "id": "d",
            "statement": "Tất cả các kết quả có thể xảy ra của phép thử là 4 kết quả.",
            "answer": true,
            "explanation": "Các kết quả là (S, S), (S, N), (N, S), (N, N)."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 15,
        "question": "Gieo một con xúc xắc 6 mặt cân đối. Có bao nhiêu kết quả thuận lợi cho biến cố 'Số chấm xuất hiện là số lẻ'?",
        "answer": "3",
        "explanation": "Các số chấm lẻ là 1, 3, 5 nên có 3 kết quả thuận lợi."
      },
      {
        "id": 16,
        "question": "Một tổ có 4 học sinh nam và 5 học sinh nữ. Chọn ngẫu nhiên một bạn làm tổ trưởng. Hỏi có bao nhiêu kết quả có thể xảy ra đối với bạn được chọn?",
        "answer": "9",
        "explanation": "Tổ có 4 + 5 = 9 học sinh nên có 9 kết quả có thể xảy ra."
      },
      {
        "id": 17,
        "question": "Có 10 tấm thẻ cùng loại được đánh số từ 1 đến 10. Rút ngẫu nhiên một thẻ. Có bao nhiêu kết quả thuận lợi cho biến cố 'Số ghi trên thẻ là số chia hết cho 3'?",
        "answer": "3",
        "explanation": "Các số từ 1 đến 10 chia hết cho 3 là 3, 6, 9 (gồm 3 số)."
      },
      {
        "id": 18,
        "question": "Tung một con xúc xắc 6 mặt cân đối. Có bao nhiêu kết quả thuận lợi cho biến cố 'Số chấm xuất hiện lớn hơn 4'?",
        "answer": "2",
        "explanation": "Các số chấm lớn hơn 4 là 5 và 6 (gồm 2 kết quả)."
      }
    ],
    "part4": [
      {
        "id": 19,
        "question": "Trong một hộp có 4 chiếc bút bi xanh, 3 chiếc bút bi đỏ và 2 chiếc bút bi đen (cùng loại). Bạn An lấy ngẫu nhiên một chiếc bút ra khỏi hộp. Trong các biến cố sau, biến cố nào là biến cố chắc chắn, biến cố không thể, biến cố ngẫu nhiên?\na) Biến cố A: 'An lấy được chiếc bút bi màu tím'.\nb) Biến cố B: 'An lấy được chiếc bút bi màu xanh hoặc đỏ hoặc đen'.\nc) Biến cố C: 'An lấy được chiếc bút bi màu xanh'.",
        "rubric": [
          {
            "step": "Xét biến cố A: Trong hộp chỉ có bút xanh, đỏ, đen nên không thể lấy được bút tím. Vậy A là biến cố không thể.",
            "points": 0.35
          },
          {
            "step": "Xét biến cố B: Vì tất cả các bút trong hộp chỉ có màu xanh, đỏ, đen nên lấy ra chắc chắn được một trong ba màu đó. Vậy B là biến cố chắc chắn.",
            "points": 0.35
          },
          {
            "step": "Xét biến cố C: Trong hộp có bút xanh và cả các màu khác nên có thể lấy được hoặc không lấy được bút xanh. Vậy C là biến cố ngẫu nhiên.",
            "points": 0.3
          }
        ],
        "solution": "a) Biến cố A là biến cố không thể vì trong hộp không có bút màu tím.\nb) Biến cố B là biến cố chắc chắn vì tất cả bút trong hộp đều thuộc một trong ba màu xanh, đỏ, đen.\nc) Biến cố C là biến cố ngẫu nhiên vì việc lấy được bút bi xanh có thể xảy ra hoặc không xảy ra."
      },
      {
        "id": 20,
        "question": "Gieo một con xúc xắc 6 mặt cân đối một lần. Nêu tất cả các kết quả thuận lợi cho mỗi biến cố sau:\na) Biến cố M: 'Số chấm xuất hiện là ước của 6'.\nb) Biến cố N: 'Số chấm xuất hiện là số chia cho 3 dư 1'.",
        "rubric": [
          {
            "step": "Xác định tập hợp kết quả của phép thử là {1, 2, 3, 4, 5, 6}.",
            "points": 0.25
          },
          {
            "step": "Với biến cố M: các ước của 6 trong tập hợp trên là 1, 2, 3, 6. Có 4 kết quả thuận lợi.",
            "points": 0.4
          },
          {
            "step": "Với biến cố N: các số chia cho 3 dư 1 là 1, 4. Có 2 kết quả thuận lợi.",
            "points": 0.35
          }
        ],
        "solution": "Tập hợp các kết quả có thể xảy ra khi gieo xúc xắc là {1; 2; 3; 4; 5; 6}.\na) Các kết quả thuận lợi cho biến cố M là: 1, 2, 3, 6 (gồm 4 kết quả).\nb) Các kết quả thuận lợi cho biến cố N là: 1, 4 (gồm 2 kết quả)."
      },
      {
        "id": 21,
        "question": "Một túi đựng 5 tấm thẻ đánh số từ 11 đến 15. Rút ngẫu nhiên một tấm thẻ.\na) Viết tập hợp các kết quả có thể xảy ra đối với số trên thẻ rút được.\nb) Trong các biến cố sau, biến cố nào là biến cố chắc chắn, không thể, ngẫu nhiên:\n- Biến cố E: 'Số ghi trên thẻ là số có hai chữ số'.\n- Biến cố F: 'Số ghi trên thẻ là số chia hết cho 10'.\n- Biến cố G: 'Số ghi trên thẻ là số nguyên tố'.",
        "rubric": [
          {
            "step": "Liệt kê tập hợp các kết quả có thể xảy ra: S = {11, 12, 13, 14, 15}.",
            "points": 0.3
          },
          {
            "step": "Biến cố E là biến cố chắc chắn vì tất cả các số 11, 12, 13, 14, 15 đều có hai chữ số.",
            "points": 0.25
          },
          {
            "step": "Biến cố F là biến cố không thể vì không có số nào trong tập hợp chia hết cho 10.",
            "points": 0.25
          },
          {
            "step": "Biến cố G là biến cố ngẫu nhiên vì trong tập hợp có số nguyên tố (11, 13) và hợp số (12, 14, 15).",
            "points": 0.2
          }
        ],
        "solution": "a) Tập hợp các kết quả có thể xảy ra là: S = {11; 12; 13; 14; 15}.\nb)\n- Biến cố E là biến cố chắc chắn vì mọi số từ 11 đến 15 đều có hai chữ số.\n- Biến cố F là biến cố không thể vì trong tập hợp không có số nào tận cùng bằng 0 nên không chia hết cho 10.\n- Biến cố G là biến cố ngẫu nhiên vì có thể rút được số nguyên tố (11 hoặc 13) hoặc hợp số (12, 14, 15)."
      }
    ]
  },
  "c8_7_bai1_test2": {
    "title": "Toán 7 - Bài 29: Làm quen với biến cố - Đề 2 (Khá)",
    "time": 45,
    "totalPoints": 10.0,
    "part1": [
      {
        "id": 1,
        "question": "Gieo hai con xúc xắc cân đối. Biến cố nào sau đây là biến cố chắc chắn?",
        "options": [
          "B. Tích số chấm bằng 36",
          "D. Hai con xúc xắc có số chấm bằng nhau",
          "A. Tổng số chấm lớn hơn 1",
          "C. Tổng số chấm là số chẵn"
        ],
        "answer": "A",
        "explanation": "Số chấm trên mỗi con xúc xắc từ 1 đến 6 nên tổng số chấm nhỏ nhất là 1 + 1 = 2 > 1. Do đó tổng luôn lớn hơn 1.",
        "correct": 2
      },
      {
        "id": 2,
        "question": "Gieo hai con xúc xắc cân đối. Biến cố nào sau đây là biến cố không thể?",
        "options": [
          "A. Hiệu số chấm bằng 0",
          "C. Tích số chấm là số lẻ",
          "B. Tổng số chấm bằng 13",
          "D. Tổng số chấm chia hết cho 5"
        ],
        "answer": "B",
        "explanation": "Số chấm lớn nhất trên mỗi con là 6 nên tổng lớn nhất là 6 + 6 = 12. Tổng số chấm không thể bằng 13.",
        "correct": 0
      },
      {
        "id": 3,
        "question": "Một hộp có 8 tấm thẻ ghi các số từ 1 đến 8. Rút ngẫu nhiên một thẻ. Biến cố 'Số ghi trên thẻ là số chính phương' có bao nhiêu kết quả thuận lợi?",
        "options": [
          "B. 2",
          "C. 3",
          "D. 4",
          "A. 1"
        ],
        "answer": "B",
        "explanation": "Các số chính phương từ 1 đến 8 là $1^2 = 1$ và $2^2 = 4$. Có 2 kết quả thuận lợi.",
        "correct": 3
      },
      {
        "id": 4,
        "question": "Gieo một con xúc xắc. Biến cố nào sau đây có 3 kết quả thuận lợi?",
        "options": [
          "B. Mặt xuất hiện có số chấm lớn hơn 4",
          "A. Mặt xuất hiện có số chấm chia hết cho 2",
          "D. Mặt xuất hiện có số chấm chia hết cho 3",
          "C. Mặt xuất hiện có số chấm là ước của 5"
        ],
        "answer": "A",
        "explanation": "Số chấm chia hết cho 2 là {2, 4, 6} (gồm 3 kết quả thuận lợi).",
        "correct": 1
      },
      {
        "id": 5,
        "question": "Chọn ngẫu nhiên một số tự nhiên có hai chữ số. Biến cố nào sau đây là biến cố ngẫu nhiên?",
        "options": [
          "A. Số được chọn lớn hơn 9",
          "C. Số được chọn có tổng hai chữ số bằng 18",
          "D. Số được chọn là số có ba chữ số",
          "B. Số được chọn nhỏ hơn 100"
        ],
        "answer": "C",
        "explanation": "Số có tổng các chữ số bằng 18 là 99 (có thể xảy ra hoặc không xảy ra). Các phương án A, B là chắc chắn, D là không thể.",
        "correct": 0
      },
      {
        "id": 6,
        "question": "Một xạ thủ bắn một viên đạn vào bia. Gọi biến cố A là 'Viên đạn trúng hồng tâm'. Biến cố phủ định của A là:",
        "options": [
          "D. Viên đạn bắn trượt hoàn toàn",
          "C. Viên đạn trúng vòng 9",
          "A. Viên đạn trúng bia",
          "B. Viên đạn không trúng hồng tâm"
        ],
        "answer": "B",
        "explanation": "Phủ định của 'trúng hồng tâm' là 'không trúng hồng tâm'.",
        "correct": 2
      },
      {
        "id": 7,
        "question": "Gieo hai con xúc xắc 6 mặt. Số kết quả thuận lợi cho biến cố 'Tổng số chấm bằng 4' là:",
        "options": [
          "B. 3",
          "A. 2",
          "D. 5",
          "C. 4"
        ],
        "answer": "B",
        "explanation": "Các cặp số chấm có tổng bằng 4 là (1, 3), (2, 2), (3, 1). Có 3 kết quả thuận lợi.",
        "correct": 1
      },
      {
        "id": 8,
        "question": "Tung 3 đồng xu cân đối đồng thời. Số kết quả có thể xảy ra của phép thử là:",
        "options": [
          "D. 9",
          "B. 6",
          "A. 3",
          "C. 8"
        ],
        "answer": "C",
        "explanation": "Mỗi đồng xu có 2 kết quả nên 3 đồng xu có $2 \\times 2 \\times 2 = 8$ kết quả.",
        "correct": 2
      },
      {
        "id": 9,
        "question": "Một hộp có chứa 3 quả cầu đỏ, 4 quả cầu xanh, 5 quả cầu vàng. Lấy ngẫu nhiên 3 quả cầu. Biến cố nào là biến cố chắc chắn?",
        "options": [
          "D. Ba quả lấy ra có đủ 3 màu",
          "B. Có ít nhất một quả cầu màu vàng",
          "C. Số quả cầu lấy ra không vượt quá 3",
          "A. Cả 3 quả đều màu đỏ"
        ],
        "answer": "C",
        "explanation": "Theo quy tắc ta lấy 3 quả cầu nên số quả lấy ra chắc chắn đúng bằng 3, tức không vượt quá 3.",
        "correct": 3
      },
      {
        "id": 10,
        "question": "Quay một vòng quay may mắn chia đều thành 8 phần ghi số từ 1 đến 8. Biến cố 'Mũi tên dừng lại ở ô ghi số là bội của 3' có các kết quả thuận lợi là:",
        "options": [
          "B. {3; 6; 9}",
          "C. {1; 3; 6}",
          "D. {3}",
          "A. {3; 6}"
        ],
        "answer": "A",
        "explanation": "Các số từ 1 đến 8 là bội của 3 gồm 3 và 6.",
        "correct": 3
      },
      {
        "id": 11,
        "question": "Lớp 7A có 40 học sinh, trong đó có 22 bạn nữ và 18 bạn nam. Chọn ngẫu nhiên 1 bạn đi dự đại hội. Biến cố 'Bạn được chọn là học sinh giỏi' là:",
        "options": [
          "B. Biến cố chắc chắn",
          "A. Biến cố ngẫu nhiên",
          "C. Biến cố không thể",
          "D. Chưa đủ dữ liệu để xác định"
        ],
        "answer": "A",
        "explanation": "Trong lớp có thể có bạn giỏi hoặc không giỏi, việc chọn ngẫu nhiên 1 bạn là học sinh giỏi là biến cố ngẫu nhiên.",
        "correct": 1
      },
      {
        "id": 12,
        "question": "Gieo một con xúc xắc 6 mặt. Biến cố 'Số chấm xuất hiện không phải là số 5' có bao nhiêu kết quả thuận lợi?",
        "options": [
          "A. 1",
          "D. 6",
          "B. 4",
          "C. 5"
        ],
        "answer": "C",
        "explanation": "Các kết quả thuận lợi là 1, 2, 3, 4, 6 (gồm 5 kết quả).",
        "correct": 0
      }
    ],
    "part2": [
      {
        "id": 13,
        "stem": "Gieo hai con xúc xắc cân đối cùng lúc. Kí hiệu $(a, b)$ là số chấm xuất hiện trên hai con xúc xắc.",
        "statements": [
          {
            "id": "a",
            "statement": "Biến cố 'Tích $a \\cdot b = 37$' là biến cố không thể.",
            "answer": true,
            "explanation": "Tích lớn nhất là $6 \\times 6 = 36 < 37$, nên không thể bằng 37."
          },
          {
            "id": "b",
            "statement": "Có đúng 6 kết quả làm cho hai con xúc xắc xuất hiện số chấm giống nhau ($a = b$).",
            "answer": true,
            "explanation": "Đó là các cặp (1,1), (2,2), (3,3), (4,4), (5,5), (6,6)."
          },
          {
            "id": "c",
            "statement": "Biến cố 'Tổng số chấm $a + b \\ge 2$' là biến cố chắc chắn.",
            "answer": true,
            "explanation": "Vì $a \\ge 1, b \\ge 1$ nên $a + b \\ge 2$ luôn luôn xảy ra."
          },
          {
            "id": "d",
            "statement": "Có tất cả 5 kết quả thuận lợi cho biến cố 'Tổng số chấm $a + b = 6$'.",
            "answer": true,
            "explanation": "Các cặp có tổng bằng 6 là (1,5), (2,4), (3,3), (4,2), (5,1) gồm đúng 5 kết quả."
          }
        ]
      },
      {
        "id": 14,
        "stem": "Một túi chứa 20 chiếc kẹo cùng loại gồm 8 kẹo dâu, 7 kẹo cam và 5 kẹo nho. Lấy ngẫu nhiên đồng thời 2 chiếc kẹo.",
        "statements": [
          {
            "id": "a",
            "statement": "Biến cố 'Lấy được ít nhất 1 chiếc kẹo bạc hà' là biến cố không thể.",
            "answer": true,
            "explanation": "Trong túi không có kẹo bạc hà."
          },
          {
            "id": "b",
            "statement": "Biến cố 'Lấy được 2 chiếc kẹo cùng vị dâu' là biến cố ngẫu nhiên.",
            "answer": true,
            "explanation": "Có thể lấy được 2 kẹo dâu hoặc không."
          },
          {
            "id": "c",
            "statement": "Biến cố 'Lấy được 2 chiếc kẹo có tổng khối lượng lớn hơn 0' là biến cố ngẫu nhiên.",
            "answer": false,
            "explanation": "Mỗi chiếc kẹo đều có khối lượng dương nên biến cố này là chắc chắn."
          },
          {
            "id": "d",
            "statement": "Nếu lấy liên tiếp 16 chiếc kẹo thì biến cố 'Có ít nhất một chiếc kẹo dâu' là biến cố chắc chắn.",
            "answer": true,
            "explanation": "Số kẹo không phải dâu là 7 + 5 = 12 chiếc. Khi lấy 16 chiếc thì chắc chắn phải có ít nhất 16 - 12 = 4 chiếc kẹo dâu."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 15,
        "question": "Gieo hai con xúc xắc cân đối. Có bao nhiêu kết quả thuận lợi cho biến cố 'Tổng số chấm xuất hiện trên hai con xúc xắc bằng 7'?",
        "answer": "6",
        "explanation": "Các cặp có tổng bằng 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) -> Có 6 kết quả."
      },
      {
        "id": 16,
        "question": "Từ các chữ số 1, 2, 3, viết ngẫu nhiên một số tự nhiên có hai chữ số khác nhau. Có bao nhiêu kết quả có thể xảy ra?",
        "answer": "6",
        "explanation": "Các số viết được là 12, 13, 21, 23, 31, 32. Có 6 kết quả."
      },
      {
        "id": 17,
        "question": "Một hộp chứa các thẻ đánh số từ 1 đến 25. Rút ngẫu nhiên một thẻ. Có bao nhiêu kết quả thuận lợi cho biến cố 'Số ghi trên thẻ là số chia hết cho cả 2 và 3'?",
        "answer": "4",
        "explanation": "Số chia hết cho cả 2 và 3 là bội của 6: 6, 12, 18, 24 -> Có 4 kết quả."
      },
      {
        "id": 18,
        "question": "Tung 3 đồng xu cân đối cùng lúc. Có bao nhiêu kết quả thuận lợi cho biến cố 'Có đúng hai đồng xu xuất hiện mặt sấp'?",
        "answer": "3",
        "explanation": "Các kết quả thỏa mãn là (S, S, N), (S, N, S), (N, S, S) -> Có 3 kết quả."
      }
    ],
    "part4": [
      {
        "id": 19,
        "question": "Một hộp kín chứa 12 tấm thẻ ghi các số từ 1 đến 12. Rút ngẫu nhiên một tấm thẻ.\na) Liệt kê các kết quả thuận lợi cho biến cố A: 'Số ghi trên thẻ là số chia hết cho 4'.\nb) Liệt kê các kết quả thuận lợi cho biến cố B: 'Số ghi trên thẻ là số nguyên tố'.\nc) Có bao nhiêu kết quả thuận lợi cho biến cố C: 'Số ghi trên thẻ vừa chia hết cho 2 vừa chia hết cho 3'?",
        "rubric": [
          {
            "step": "Biến cố A: Các số chia hết cho 4 từ 1 đến 12 là {4, 8, 12}.",
            "points": 0.35
          },
          {
            "step": "Biến cố B: Các số nguyên tố từ 1 đến 12 là {2, 3, 5, 7, 11}.",
            "points": 0.35
          },
          {
            "step": "Biến cố C: Các số chia hết cho 6 là {6, 12}. Kết luận có 2 kết quả thuận lợi.",
            "points": 0.3
          }
        ],
        "solution": "a) Các kết quả thuận lợi cho biến cố A là: 4; 8; 12.\nb) Các kết quả thuận lợi cho biến cố B là: 2; 3; 5; 7; 11.\nc) Số vừa chia hết cho 2 vừa chia hết cho 3 là số chia hết cho 6. Các kết quả thuận lợi cho biến cố C là 6 và 12. Vậy có 2 kết quả thuận lợi."
      },
      {
        "id": 20,
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Hãy cho biết mỗi biến cố sau là biến cố loại nào (chắc chắn, không thể, ngẫu nhiên) và giải thích ngắn gọn:\na) Biến cố K: 'Hiệu số chấm trên hai con xúc xắc bằng 6'.\nb) Biến cố L: 'Tổng số chấm trên hai con xúc xắc nhỏ hơn 13'.\nc) Biến cố M: 'Tích số chấm trên hai con xúc xắc là số lẻ'.",
        "rubric": [
          {
            "step": "K là biến cố không thể vì hiệu lớn nhất chỉ là 6 - 1 = 5 < 6.",
            "points": 0.35
          },
          {
            "step": "L là biến cố chắc chắn vì tổng lớn nhất chỉ là 6 + 6 = 12 < 13.",
            "points": 0.35
          },
          {
            "step": "M là biến cố ngẫu nhiên vì tích có thể lẻ (khi cả 2 cùng lẻ) hoặc chẵn (khi có ít nhất 1 số chẵn).",
            "points": 0.3
          }
        ],
        "solution": "a) Biến cố K là biến cố không thể vì số chấm mỗi con lớn nhất là 6, nhỏ nhất là 1 nên hiệu lớn nhất là $6 - 1 = 5 < 6$.\nb) Biến cố L là biến cố chắc chắn vì tổng số chấm lớn nhất là $6 + 6 = 12 < 13$.\nc) Biến cố M là biến cố ngẫu nhiên vì nếu gieo được (1, 3) thì tích bằng 3 (lẻ), nếu gieo được (2, 3) thì tích bằng 6 (chẵn)."
      },
      {
        "id": 21,
        "question": "Trong bình có 15 viên bi gồm 6 viên bi trắng, 5 viên bi đen và 4 viên bi vàng. Cần lấy ra ngẫu nhiên ít nhất bao nhiêu viên bi để biến cố 'Trong các viên bi lấy ra chắc chắn có đủ cả 3 màu' là biến cố chắc chắn? Giải thích chi tiết.",
        "rubric": [
          {
            "step": "Phân tích trường hợp xấu nhất: lấy nhiều bi nhất mà vẫn chưa đủ 3 màu.",
            "points": 0.3
          },
          {
            "step": "Trường hợp xấu nhất là lấy hết hai loại màu có số lượng nhiều nhất: toàn bộ 6 bi trắng và 5 bi đen, tổng cộng 6 + 5 = 11 viên bi.",
            "points": 0.4
          },
          {
            "step": "Khi lấy thêm 1 viên nữa (viên thứ 12), viên này chắc chắn là màu vàng. Vậy cần lấy ít nhất 12 viên bi.",
            "points": 0.3
          }
        ],
        "solution": "Để biến cố 'chắc chắn có đủ cả 3 màu' xảy ra, ta xét tình huống xấu nhất (rủi ro nhất):\n- Tình huống lấy ra nhiều bi nhất mà vẫn chưa đủ 3 màu là khi ta đã lấy hết toàn bộ số bi của hai màu có số lượng nhiều nhất, tức là lấy được 6 bi trắng và 5 bi đen. Khi đó ta đã lấy: $6 + 5 = 11$ (viên bi) mà vẫn chỉ có 2 màu.\n- Do đó, khi ta lấy thêm 1 viên nữa (tức $11 + 1 = 12$ viên bi), viên bi còn lại bắt buộc phải là bi màu vàng.\nVậy cần lấy ngẫu nhiên ít nhất 12 viên bi để chắc chắn lấy được đủ cả 3 màu."
      }
    ]
  },
  "c8_7_bai1_test3": {
    "title": "Toán 7 - Bài 29: Làm quen với biến cố - Đề 3 (Nâng cao)",
    "time": 45,
    "totalPoints": 10.0,
    "part1": [
      {
        "id": 1,
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Có bao nhiêu kết quả thuận lợi cho biến cố 'Tổng số chấm xuất hiện là số nguyên tố'?",
        "options": [
          "B. 14",
          "C. 15",
          "D. 16",
          "A. 13"
        ],
        "answer": "C",
        "explanation": "Tổng số chấm có thể nhận các giá trị nguyên tố là 2, 3, 5, 7, 11. Số cặp tương ứng: tổng=2 (1), tổng=3 (2), tổng=5 (4), tổng=7 (6), tổng=11 (2). Tổng cộng: 1 + 2 + 4 + 6 + 2 = 15 cặp.",
        "correct": 3
      },
      {
        "id": 2,
        "question": "Chọn ngẫu nhiên một số tự nhiên có 3 chữ số. Biến cố nào sau đây là biến cố chắc chắn?",
        "options": [
          "B. Số được chọn lớn hơn 99 và nhỏ hơn 1000",
          "A. Số được chọn chia hết cho 5",
          "C. Số được chọn có các chữ số khác nhau",
          "D. Số được chọn có tổng các chữ số là số chẵn"
        ],
        "answer": "B",
        "explanation": "Các số tự nhiên có 3 chữ số là từ 100 đến 999, tức lớn hơn 99 và nhỏ hơn 1000.",
        "correct": 1
      },
      {
        "id": 3,
        "question": "Gieo hai con xúc xắc. Biến cố 'Tích số chấm xuất hiện chia hết cho 6' có bao nhiêu kết quả thuận lợi?",
        "options": [
          "B. 18",
          "D. 25",
          "A. 15",
          "C. 21"
        ],
        "answer": "D",
        "explanation": "Tích không chia hết cho 6 khi không có thừa số 6, tức: (không chia hết cho 2) hoặc (không chia hết cho 3). Số cặp có tích lẻ là 3x3=9. Số cặp có tích không chia hết cho 3 (chỉ gồm 1,2,4,5) là 4x4=16. Số cặp vừa lẻ vừa không chia hết cho 3 (chỉ 1,5) là 2x2=4. Số cặp không chia hết cho 6 là 9 + 16 - 4 = 21. Vậy số cặp chia hết cho 6 là 36 - 21 = 15... Không: nếu có số 6 thì chia hết cho 6. Các cặp có ít nhất 1 mặt 6: 11 cặp. Các cặp không có 6 nhưng tích chia hết cho 6: gồm 2 hoặc 4 ghép với 3: (2,3), (3,2), (4,3), (3,4) -> 4 cặp. Tổng cộng 11 + 4 = 15 kết quả thuận lợi. Tuy nhiên lưu ý (3,2),(3,4),(2,3),(4,3) và (6,...): số kết quả = 15.",
        "correct": 2
      },
      {
        "id": 4,
        "question": "Trong một hộp có 30 tấm thẻ ghi số từ 1 đến 30. Rút ngẫu nhiên một thẻ. Biến cố 'Số trên thẻ là bội của 3 hoặc bội của 5' có bao nhiêu kết quả thuận lợi?",
        "options": [
          "B. 16",
          "A. 14",
          "D. 12",
          "C. 15"
        ],
        "answer": "A",
        "explanation": "Số bội của 3 là 10. Số bội của 5 là 6. Bội chung của 3 và 5 (bội của 15) là 2 (15, 30). Số kết quả thuận lợi là 10 + 6 - 2 = 14.",
        "correct": 1
      },
      {
        "id": 5,
        "question": "Tung 4 đồng xu cân đối đồng thời. Số kết quả thuận lợi cho biến cố 'Số mặt sấp bằng số mặt ngửa' là:",
        "options": [
          "D. 10",
          "C. 8",
          "B. 6",
          "A. 4"
        ],
        "answer": "B",
        "explanation": "Bằng nhau tức là có 2 sấp và 2 ngửa. Số cách chọn vị trí cho 2 sấp trong 4 vị trí là $C_4^2 = 6$ kết quả: SSNN, SNSN, SNNS, NSSN, NSNS, NNSS.",
        "correct": 3
      },
      {
        "id": 6,
        "question": "Một tổ gồm 6 học sinh giỏi Toán và 4 học sinh giỏi Văn. Cần chọn ngẫu nhiên một ban đại diện 3 người. Biến cố 'Trong ban đại diện có cả bạn giỏi Toán và bạn giỏi Văn' là:",
        "options": [
          "A. Biến cố chắc chắn",
          "C. Biến cố ngẫu nhiên",
          "D. Biến cố đồng khả năng",
          "B. Biến cố không thể"
        ],
        "answer": "C",
        "explanation": "Có thể chọn được 3 bạn toàn giỏi Toán hoặc cả hai môn, nên là biến cố ngẫu nhiên.",
        "correct": 0
      },
      {
        "id": 7,
        "question": "Gieo hai con xúc xắc. Biến cố 'Hiệu số chấm bằng 2' có bao nhiêu kết quả thuận lợi?",
        "options": [
          "C. 8",
          "B. 6",
          "A. 4",
          "D. 10"
        ],
        "answer": "C",
        "explanation": "Các cặp có hiệu bằng 2: (1,3), (2,4), (3,5), (4,6) và ngược lại (3,1), (4,2), (5,3), (6,4). Tổng cộng có 8 kết quả.",
        "correct": 2
      },
      {
        "id": 8,
        "question": "Cho đa thức $P(x) = x^2 - 4x + 3$. Chọn ngẫu nhiên một số $a \\in \\{1, 2, 3, 4, 5\\}$. Biến cố '$a$ là nghiệm của $P(x)$' có bao nhiêu kết quả thuận lợi?",
        "options": [
          "C. 3",
          "D. 4",
          "B. 2",
          "A. 1"
        ],
        "answer": "B",
        "explanation": "$x^2 - 4x + 3 = 0 \\Leftrightarrow x = 1$ hoặc $x = 3$. Cả 1 và 3 đều thuộc tập hợp nên có 2 kết quả thuận lợi.",
        "correct": 3
      },
      {
        "id": 9,
        "question": "Một mật mã két sắt gồm 3 chữ số từ 0 đến 9. Biến cố 'Bấm ngẫu nhiên 3 chữ số mà trúng ngay mật mã' là:",
        "options": [
          "D. Biến cố đồng khả năng",
          "A. Biến cố chắc chắn",
          "B. Biến cố không thể",
          "C. Biến cố ngẫu nhiên"
        ],
        "answer": "C",
        "explanation": "Khả năng xảy ra rất nhỏ nhưng hoàn toàn có thể xảy ra hoặc không xảy ra, nên là biến cố ngẫu nhiên.",
        "correct": 1
      },
      {
        "id": 10,
        "question": "Gieo hai con xúc xắc cân đối. Biến cố nào sau đây có ít kết quả thuận lợi nhất?",
        "options": [
          "A. Tổng số chấm bằng 2",
          "B. Tổng số chấm bằng 7",
          "D. Tổng số chấm bằng 6",
          "C. Tổng số chấm bằng 10"
        ],
        "answer": "A",
        "explanation": "Tổng bằng 2 chỉ có duy nhất 1 kết quả là (1, 1).",
        "correct": 0
      },
      {
        "id": 11,
        "question": "Trong túi có 7 viên bi đỏ, 5 viên bi xanh và 4 viên bi vàng. Lấy ngẫu nhiên $k$ viên bi. Giá trị nhỏ nhất của $k$ để chắc chắn có ít nhất 1 viên bi màu vàng là:",
        "options": [
          "A. 11",
          "B. 12",
          "D. 14",
          "C. 13"
        ],
        "answer": "C",
        "explanation": "Số bi không phải màu vàng là 7 + 5 = 12. Trường hợp xấu nhất lấy 12 viên toàn đỏ và xanh. Lấy thêm 1 viên nữa (viên thứ 13) chắc chắn có bi vàng. Vậy $k = 13$.",
        "correct": 0
      },
      {
        "id": 12,
        "question": "Cho tập hợp $A = \\{n \\in \\mathbb{N} \\mid 10 \\le n \\le 99\\}$. Chọn ngẫu nhiên một phần tử của $A$. Biến cố 'Phần tử được chọn có tích hai chữ số bằng 12' có bao nhiêu kết quả thuận lợi?",
        "options": [
          "B. 4",
          "D. 8",
          "A. 2",
          "C. 6"
        ],
        "answer": "B",
        "explanation": "Các cặp chữ số có tích bằng 12 là (2,6), (6,2), (3,4), (4,3). Các số tương ứng là 26, 62, 34, 43. Có 4 kết quả thuận lợi.",
        "correct": 2
      }
    ],
    "part2": [
      {
        "id": 13,
        "stem": "Một hộp kín chứa 50 tấm thẻ cùng loại được đánh số từ 1 đến 50. Rút ngẫu nhiên một tấm thẻ.",
        "statements": [
          {
            "id": "a",
            "statement": "Biến cố 'Số trên thẻ là số chính phương' có 7 kết quả thuận lợi.",
            "answer": true,
            "explanation": "Các số chính phương là $1^2, 2^2, 3^2, 4^2, 5^2, 6^2, 7^2$ (từ 1 đến 49) gồm 7 số."
          },
          {
            "id": "b",
            "statement": "Biến cố 'Số trên thẻ chia hết cho 11' có 5 kết quả thuận lợi.",
            "answer": false,
            "explanation": "Các số chia hết cho 11 là 11, 22, 33, 44 -> chỉ có 4 kết quả thuận lợi."
          },
          {
            "id": "c",
            "statement": "Biến cố 'Số trên thẻ là số có hai chữ số giống nhau' có 4 kết quả thuận lợi.",
            "answer": true,
            "explanation": "Đó là các số 11, 22, 33, 44 (gồm 4 kết quả)."
          },
          {
            "id": "d",
            "statement": "Biến cố 'Số trên thẻ là ước của 60' có 12 kết quả thuận lợi.",
            "answer": false,
            "explanation": "Các ước dương của 60 là 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60. Trong khoảng 1 đến 50 có tất cả các ước trừ 60, tức có 12 - 1 = 11 kết quả. Do đó mệnh đề có 12 kết quả là sai. (Đính chính: ước của 60 gồm 1,2,3,4,5,6,10,12,15,20,30 là 11 số)."
          }
        ]
      },
      {
        "id": 14,
        "stem": "Xét bài toán gieo 3 đồng xu cân đối đồng chất.",
        "statements": [
          {
            "id": "a",
            "statement": "Tổng số kết quả có thể xảy ra của phép thử là 8 kết quả.",
            "answer": true,
            "explanation": "$2^3 = 8$."
          },
          {
            "id": "b",
            "statement": "Biến cố 'Có ít nhất một mặt ngửa' có 7 kết quả thuận lợi.",
            "answer": true,
            "explanation": "Chỉ có 1 kết quả không có mặt ngửa nào (SSS), nên $8 - 1 = 7$."
          },
          {
            "id": "c",
            "statement": "Biến cố 'Số mặt ngửa nhiều hơn số mặt sấp' có 4 kết quả thuận lợi.",
            "answer": true,
            "explanation": "Số mặt ngửa > số sấp tức có 2 hoặc 3 mặt ngửa: NNS, NSN, SNN, NNN (gồm 4 kết quả)."
          },
          {
            "id": "d",
            "statement": "Biến cố 'Cả ba đồng xu xuất hiện cùng một mặt' là biến cố chắc chắn.",
            "answer": false,
            "explanation": "Đây là biến cố ngẫu nhiên (chỉ xảy ra khi SSS hoặc NNN)."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 15,
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Có bao nhiêu kết quả thuận lợi cho biến cố 'Tổng số chấm xuất hiện lớn hơn hoặc bằng 10'?",
        "answer": "6",
        "explanation": "Tổng = 10 có (4,6), (5,5), (6,4) (3 cặp); Tổng = 11 có (5,6), (6,5) (2 cặp); Tổng = 12 có (6,6) (1 cặp). Tổng cộng: 3 + 2 + 1 = 6 kết quả."
      },
      {
        "id": 16,
        "question": "Từ các chữ số 0, 1, 2, 3, lập các số tự nhiên có hai chữ số khác nhau. Có bao nhiêu kết quả thuận lợi cho biến cố 'Số lập được là số chẵn'?",
        "answer": "5",
        "explanation": "Các số chẵn gồm: tận cùng 0 (10, 20, 30: 3 số); tận cùng 2 (12, 32: 2 số). Tổng cộng có 3 + 2 = 5 kết quả."
      },
      {
        "id": 17,
        "question": "Một lớp có 15 học sinh nam và 20 học sinh nữ. Chọn ngẫu nhiên một ban cán sự gồm 2 người. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố 'Ban cán sự gồm 1 nam và 1 nữ'?",
        "answer": "300",
        "explanation": "Số cách chọn 1 nam là 15, chọn 1 nữ là 20. Số kết quả thuận lợi là $15 \\times 20 = 300$."
      },
      {
        "id": 18,
        "question": "Có bao nhiêu số tự nhiên $x \\in \\{1, 2, 3, ..., 100\\}$ là kết quả thuận lợi cho biến cố 'Giá trị biểu thức $x^2 + 1$ có chữ số tận cùng là 0'?",
        "answer": "20",
        "explanation": "$x^2 + 1$ tận cùng 0 khi $x^2$ tận cùng 9. Số $x$ phải có tận cùng là 3 hoặc 7. Từ 1 đến 100 có 10 số tận cùng 3 và 10 số tận cùng 7, tổng cộng có 20 số."
      }
    ],
    "part4": [
      {
        "id": 19,
        "question": "Cho tập hợp $S = \\{1, 2, 3, 4, 5, 6, 7, 8, 9\\}$. Chọn ngẫu nhiên một số thuộc $S$.\na) Xác định số kết quả thuận lợi cho biến cố A: 'Số được chọn thỏa mãn bất phương trình $2x - 5 > 3$'.\nb) Xác định số kết quả thuận lợi cho biến cố B: 'Số được chọn là nghiệm của phương trình $(x - 2)(x^2 - 9) = 0$'.\nc) Viết tập hợp các kết quả thuận lợi cho biến cố C: 'Số được chọn vừa là số lẻ vừa là hợp số'.",
        "rubric": [
          {
            "step": "Giải bất phương trình $2x > 8 \\Rightarrow x > 4$. Các số thuộc S lớn hơn 4 là {5, 6, 7, 8, 9}. Có 5 kết quả thuận lợi.",
            "points": 0.35
          },
          {
            "step": "Phương trình có nghiệm $x = 2$, $x = 3$, $x = -3$. Vì $x \\in S$ nên nhận $x \\in \\{2, 3\\}$. Có 2 kết quả thuận lợi.",
            "points": 0.35
          },
          {
            "step": "Số lẻ trong S: {1, 3, 5, 7, 9}. Số hợp số là số lớn hơn 1 không phải nguyên tố: 9. Vậy C = {9}.",
            "points": 0.3
          }
        ],
        "solution": "a) Ta có $2x - 5 > 3 \\Leftrightarrow 2x > 8 \\Leftrightarrow x > 4$.\nCác số trong S lớn hơn 4 là: 5; 6; 7; 8; 9. Vậy có 5 kết quả thuận lợi cho biến cố A.\nb) Phương trình $(x - 2)(x^2 - 9) = 0 \\Leftrightarrow x = 2$ hoặc $x = 3$ hoặc $x = -3$.\nVì $x \\in S = \\{1; 2; ...; 9\\}$ nên chỉ nhận $x = 2$ và $x = 3$. Vậy có 2 kết quả thuận lợi cho biến cố B.\nc) Các số lẻ trong S là 1, 3, 5, 7, 9. Trong các số này, chỉ có 9 là hợp số (vì $9 = 3^2$, còn 1 không là số nguyên tố cũng không là hợp số, 3, 5, 7 là số nguyên tố). Vậy tập hợp kết quả thuận lợi cho C là $\\{9\\}$."
      },
      {
        "id": 20,
        "question": "Gieo đồng thời hai con xúc xắc cân đối 6 mặt. Gọi $x, y$ lần lượt là số chấm xuất hiện trên con xúc xắc thứ nhất và con xúc xắc thứ hai.\na) Có bao nhiêu kết quả thuận lợi cho biến cố: '$x + y$' chia hết cho 5?\nb) Có bao nhiêu kết quả thuận lợi cho biến cố: '$|x - y| \\le 1$'?",
        "rubric": [
          {
            "step": "Tìm các cặp $(x, y)$ có tổng chia hết cho 5: tổng = 5 gồm 4 cặp: (1,4), (2,3), (3,2), (4,1); tổng = 10 gồm 3 cặp: (4,6), (5,5), (6,4). Tổng cộng có 7 kết quả.",
            "points": 0.5
          },
          {
            "step": "Tìm các cặp $|x - y| \\le 1$: nếu $|x - y| = 0$ có 6 cặp; nếu $|x - y| = 1$ có các cặp (1,2),(2,3),(3,4),(4,5),(5,6) và ngược lại (10 cặp). Tổng cộng $6 + 10 = 16$ kết quả.",
            "points": 0.5
          }
        ],
        "solution": "a) Vì $1 \\le x, y \\le 6$ nên $2 \\le x + y \\le 12$.\nCác giá trị của $x + y$ chia hết cho 5 là 5 và 10.\n- Với $x + y = 5$: có 4 cặp là (1, 4), (2, 3), (3, 2), (4, 1).\n- Với $x + y = 10$: có 3 cặp là (4, 6), (5, 5), (6, 4).\nVậy có tất cả $4 + 3 = 7$ kết quả thuận lợi.\nb) Điều kiện $|x - y| \\le 1$ tương đương $|x - y| = 0$ hoặc $|x - y| = 1$:\n- Khi $|x - y| = 0 \\Rightarrow x = y$: có 6 cặp: (1,1), (2,2), (3,3), (4,4), (5,5), (6,6).\n- Khi $|x - y| = 1$: các cặp là (1,2), (2,3), (3,4), (4,5), (5,6) và (2,1), (3,2), (4,3), (5,4), (6,5) gồm 10 cặp.\nVậy có tất cả $6 + 10 = 16$ kết quả thuận lợi."
      },
      {
        "id": 21,
        "question": "Một nhóm gồm 5 học sinh nam và 4 học sinh nữ. Thầy giáo chọn ngẫu nhiên ra 4 bạn để tham gia đội thi hùng biện tiếng Anh.\na) Biến cố 'Trong 4 bạn được chọn có cả nam và nữ' là biến cố loại nào?\nb) Cần chọn ít nhất bao nhiêu học sinh để chắc chắn luôn có ít nhất 2 học sinh nữ được chọn?",
        "rubric": [
          {
            "step": "a) Biến cố có thể không xảy ra (nếu chọn 4 bạn đều là nam) nên là biến cố ngẫu nhiên.",
            "points": 0.4
          },
          {
            "step": "b) Xét trường hợp xấu nhất: chọn tất cả 5 học sinh nam và chỉ 1 học sinh nữ (tổng cộng 6 học sinh) vẫn chưa đủ 2 nữ.",
            "points": 0.3
          },
          {
            "step": "Do đó cần chọn thêm 1 học sinh nữa (học sinh thứ 7) thì chắc chắn có ít nhất 2 bạn nữ. Kết luận: cần chọn ít nhất 7 học sinh.",
            "points": 0.3
          }
        ],
        "solution": "a) Vì có 5 học sinh nam nên hoàn toàn có khả năng 4 bạn được chọn đều là học sinh nam (không có bạn nữ nào). Do đó biến cố 'Trong 4 bạn có cả nam và nữ' có thể xảy ra hoặc không xảy ra, đây là biến cố ngẫu nhiên.\nb) Để chắc chắn có ít nhất 2 bạn nữ, ta xét trường hợp bất lợi nhất là đã chọn hết toàn bộ 5 bạn nam và 1 bạn nữ (tổng số học sinh đã chọn là $5 + 1 = 6$ bạn) mà vẫn chưa có đủ 2 bạn nữ.\nKhi đó, nếu ta chọn thêm 1 bạn nữa (tức bạn thứ 7), bạn này chắc chắn phải là nữ.\nVậy cần chọn ít nhất 7 học sinh để chắc chắn có ít nhất 2 bạn nữ."
      }
    ]
  },
  "c8_7_bai2_test1": {
    "title": "Toán 7 - Bài 30: Làm quen với xác suất của biến cố - Đề 1 (Cơ bản)",
    "time": 45,
    "totalPoints": 10.0,
    "part1": [
      {
        "id": 1,
        "question": "Xác suất của một biến cố chắc chắn bằng:",
        "options": [
          "A. 0",
          "C. 1",
          "B. 0,5",
          "D. 100"
        ],
        "answer": "C",
        "explanation": "Biến cố chắc chắn luôn luôn xảy ra nên có xác suất bằng 1.",
        "correct": 0
      },
      {
        "id": 2,
        "question": "Xác suất của một biến cố không thể bằng:",
        "options": [
          "B. 0,5",
          "C. 1",
          "D. -1",
          "A. 0"
        ],
        "answer": "A",
        "explanation": "Biến cố không thể không bao giờ xảy ra nên có xác suất bằng 0.",
        "correct": 3
      },
      {
        "id": 3,
        "question": "Tung một đồng xu cân đối đồng chất một lần. Xác suất để xuất hiện mặt sấp là:",
        "options": [
          "A. 1",
          "D. $\\frac{1}{4}$",
          "B. 0",
          "C. $\\frac{1}{2}$"
        ],
        "answer": "C",
        "explanation": "Có 2 kết quả đồng khả năng (S, N). Kết quả thuận lợi cho mặt sấp là 1. Xác suất là $\\frac{1}{2}$.",
        "correct": 0
      },
      {
        "id": 4,
        "question": "Gieo một con xúc xắc 6 mặt cân đối một lần. Xác suất để xuất hiện mặt 3 chấm là:",
        "options": [
          "B. $\\frac{3}{6}$",
          "A. $\\frac{1}{6}$",
          "C. $\\frac{1}{2}$",
          "D. $\\frac{1}{3}$"
        ],
        "answer": "A",
        "explanation": "Tổng số kết quả là 6, có 1 kết quả xuất hiện mặt 3 chấm. Xác suất là $\\frac{1}{6}$.",
        "correct": 1
      },
      {
        "id": 5,
        "question": "Một hộp có 1 quả bóng xanh và 1 quả bóng đỏ có cùng kích thước và khối lượng. Lấy ngẫu nhiên 1 quả bóng. Xác suất lấy được bóng đỏ là:",
        "options": [
          "D. $\\frac{2}{3}$",
          "B. 0",
          "A. 1",
          "C. $\\frac{1}{2}$"
        ],
        "answer": "C",
        "explanation": "Có 2 khả năng như nhau, bóng đỏ chiếm 1 khả năng nên xác suất là $\\frac{1}{2}$.",
        "correct": 2
      },
      {
        "id": 6,
        "question": "Gieo một con xúc xắc 6 mặt cân đối. Xác suất xuất hiện mặt có số chấm là số chẵn là:",
        "options": [
          "D. $\\frac{2}{3}$",
          "A. $\\frac{1}{6}$",
          "B. $\\frac{1}{3}$",
          "C. $\\frac{1}{2}$"
        ],
        "answer": "C",
        "explanation": "Các số chẵn là 2, 4, 6 (gồm 3 kết quả). Xác suất là $\\frac{3}{6} = \\frac{1}{2}$.",
        "correct": 1
      },
      {
        "id": 7,
        "question": "Gieo một con xúc xắc 6 mặt cân đối. Xác suất xuất hiện mặt có số chấm lớn hơn 4 là:",
        "options": [
          "D. $\\frac{2}{3}$",
          "C. $\\frac{1}{2}$",
          "B. $\\frac{1}{3}$",
          "A. $\\frac{1}{6}$"
        ],
        "answer": "B",
        "explanation": "Các số chấm lớn hơn 4 là 5, 6 (gồm 2 kết quả). Xác suất là $\\frac{2}{6} = \\frac{1}{3}$.",
        "correct": 3
      },
      {
        "id": 8,
        "question": "Một túi đựng 4 viên bi xanh và 4 viên bi đỏ có kích thước như nhau. Lấy ngẫu nhiên một viên bi. Khả năng lấy được bi xanh so với bi đỏ là:",
        "options": [
          "B. Nhỏ hơn",
          "C. Bằng nhau",
          "D. Không so sánh được",
          "A. Lớn hơn"
        ],
        "answer": "C",
        "explanation": "Số lượng bi xanh và bi đỏ bằng nhau nên khả năng lấy được là như nhau.",
        "correct": 3
      },
      {
        "id": 9,
        "question": "Một hộp có 5 tấm thẻ đánh số từ 1 đến 5. Rút ngẫu nhiên một tấm thẻ. Xác suất để rút được tấm thẻ ghi số nguyên tố là:",
        "options": [
          "B. $\\frac{2}{5}$",
          "D. $\\frac{4}{5}$",
          "A. $\\frac{1}{5}$",
          "C. $\\frac{3}{5}$"
        ],
        "answer": "C",
        "explanation": "Các số nguyên tố từ 1 đến 5 là 2, 3, 5 (gồm 3 số). Xác suất là $\\frac{3}{5}$.",
        "correct": 2
      },
      {
        "id": 10,
        "question": "Một chiếc vòng quay có 4 phần bằng nhau ghi các màu: Xanh, Đỏ, Tím, Vàng. Quay vòng quay 1 lần. Xác suất mũi tên chỉ vào ô màu Đỏ là:",
        "options": [
          "A. $\\frac{1}{2}$",
          "D. $\\frac{1}{8}$",
          "C. $\\frac{1}{4}$",
          "B. $\\frac{1}{3}$"
        ],
        "answer": "C",
        "explanation": "Có 4 ô bằng nhau, ô màu đỏ chiếm 1 phần nên xác suất là $\\frac{1}{4}$.",
        "correct": 0
      },
      {
        "id": 11,
        "question": "Nếu một biến cố có xác suất bằng 0,8 thì biến cố đó là biến cố:",
        "options": [
          "D. Ngẫu nhiên có khả năng xảy ra thấp",
          "A. Chắc chắn",
          "B. Không thể",
          "C. Ngẫu nhiên có khả năng xảy ra cao"
        ],
        "answer": "C",
        "explanation": "Xác suất 0,8 khá gần 1 nên biến cố có khả năng xảy ra cao.",
        "correct": 1
      },
      {
        "id": 12,
        "question": "Gieo một con xúc xắc 6 mặt cân đối. Biến cố nào sau đây có xác suất bằng $\\frac{1}{6}$?",
        "options": [
          "D. Xuất hiện mặt có số chấm nhỏ hơn 6",
          "B. Xuất hiện mặt 1 chấm",
          "A. Xuất hiện mặt có số chấm là số nguyên tố",
          "C. Xuất hiện mặt có số chấm chia hết cho 2"
        ],
        "answer": "B",
        "explanation": "Mặt 1 chấm chỉ có 1 kết quả thuận lợi nên xác suất là $\\frac{1}{6}$.",
        "correct": 2
      }
    ],
    "part2": [
      {
        "id": 13,
        "stem": "Một hộp kín chứa 10 quả bóng có cùng kích thước và khối lượng, được đánh số từ 1 đến 10. Lấy ngẫu nhiên một quả bóng.",
        "statements": [
          {
            "id": "a",
            "statement": "Số kết quả có thể xảy ra của phép thử là 10.",
            "answer": true,
            "explanation": "Có 10 quả bóng được đánh số từ 1 đến 10."
          },
          {
            "id": "b",
            "statement": "Xác suất lấy được quả bóng ghi số chẵn bằng $\\frac{1}{2}$.",
            "answer": true,
            "explanation": "Các số chẵn là 2, 4, 6, 8, 10 (gồm 5 số). Xác suất là $\\frac{5}{10} = \\frac{1}{2}$."
          },
          {
            "id": "c",
            "statement": "Xác suất lấy được quả bóng ghi số chia hết cho 5 bằng $\\frac{1}{10}$.",
            "answer": false,
            "explanation": "Số chia hết cho 5 là 5 và 10 (gồm 2 số). Xác suất là $\\frac{2}{10} = \\frac{1}{5}$."
          },
          {
            "id": "d",
            "statement": "Xác suất lấy được quả bóng ghi số lớn hơn 7 bằng 0,3.",
            "answer": true,
            "explanation": "Các số lớn hơn 7 là 8, 9, 10 (gồm 3 số). Xác suất là $\\frac{3}{10} = 0,3$."
          }
        ]
      },
      {
        "id": 14,
        "stem": "Gieo một con xúc xắc 6 mặt cân đối đồng chất.",
        "statements": [
          {
            "id": "a",
            "statement": "Khả năng xuất hiện của mỗi mặt từ 1 đến 6 chấm là như nhau.",
            "answer": true,
            "explanation": "Do con xúc xắc cân đối và đồng chất."
          },
          {
            "id": "b",
            "statement": "Xác suất xuất hiện mặt có số chấm nhỏ hơn 3 là $\\frac{1}{3}$.",
            "answer": true,
            "explanation": "Các mặt nhỏ hơn 3 là 1 và 2 (2 kết quả). Xác suất là $\\frac{2}{6} = \\frac{1}{3}$."
          },
          {
            "id": "c",
            "statement": "Xác suất xuất hiện mặt có số chấm là bội của 4 là $\\frac{1}{6}$.",
            "answer": true,
            "explanation": "Bội của 4 từ 1 đến 6 chỉ có số 4 (1 kết quả). Xác suất là $\\frac{1}{6}$."
          },
          {
            "id": "d",
            "statement": "Xác suất xuất hiện mặt có số chấm lớn hơn 6 bằng 1.",
            "answer": false,
            "explanation": "Số chấm lớn nhất là 6 nên đây là biến cố không thể, xác suất bằng 0."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 15,
        "question": "Gieo một con xúc xắc cân đối 6 mặt. Tính xác suất để xuất hiện mặt có số chấm là số chia hết cho 3 (kết quả viết dưới dạng phân số tối giản).",
        "answer": "1/3",
        "explanation": "Số chia hết cho 3 là 3, 6 (gồm 2 kết quả). Xác suất = 2/6 = 1/3."
      },
      {
        "id": 16,
        "question": "Trong một hộp có 8 viên bi xanh, 5 viên bi đỏ và 7 viên bi vàng có kích thước giống nhau. Lấy ngẫu nhiên một viên bi. Tính xác suất để lấy được viên bi màu đỏ (viết dưới dạng phân số tối giản).",
        "answer": "1/4",
        "explanation": "Tổng số bi là 8 + 5 + 7 = 20. Số bi đỏ là 5. Xác suất = 5/20 = 1/4."
      },
      {
        "id": 17,
        "question": "Có 20 tấm thẻ đánh số từ 1 đến 20. Rút ngẫu nhiên một thẻ. Tính xác suất để rút được tấm thẻ có số tận cùng là chữ số 0.",
        "answer": "1/10",
        "explanation": "Các số tận cùng là 0 gồm 10 và 20 (2 thẻ). Xác suất = 2/20 = 1/10."
      },
      {
        "id": 18,
        "question": "Một tổ học sinh có 6 bạn nam và 6 bạn nữ. Chọn ngẫu nhiên một bạn làm lớp phó. Tính xác suất để bạn được chọn là nữ.",
        "answer": "1/2",
        "explanation": "Xác suất chọn bạn nữ là 6 / (6 + 6) = 6/12 = 1/2."
      }
    ],
    "part4": [
      {
        "id": 19,
        "question": "Một chiếc hộp chứa 15 tấm thẻ cùng loại được đánh số từ 1 đến 15. Rút ngẫu nhiên một tấm thẻ. Tính xác suất của các biến cố sau:\na) Biến cố A: 'Số ghi trên thẻ là số chẵn'.\nb) Biến cố B: 'Số ghi trên thẻ là số chia hết cho 5'.\nc) Biến cố C: 'Số ghi trên thẻ là số có một chữ số'.",
        "rubric": [
          {
            "step": "Có 15 kết quả có thể đồng khả năng xảy ra.",
            "points": 0.1
          },
          {
            "step": "Số chẵn từ 1 đến 15 là: 2, 4, 6, 8, 10, 12, 14 (gồm 7 số). Xác suất P(A) = 7/15.",
            "points": 0.3
          },
          {
            "step": "Số chia hết cho 5 là: 5, 10, 15 (gồm 3 số). Xác suất P(B) = 3/15 = 1/5.",
            "points": 0.3
          },
          {
            "step": "Số có một chữ số là: 1 đến 9 (gồm 9 số). Xác suất P(C) = 9/15 = 3/5.",
            "points": 0.3
          }
        ],
        "solution": "Tổng số kết quả có thể xảy ra là 15.\na) Các số chẵn từ 1 đến 15 là 2; 4; 6; 8; 10; 12; 14 gồm 7 kết quả thuận lợi. Vậy $P(A) = \\frac{7}{15}$.\nb) Các số chia hết cho 5 là 5; 10; 15 gồm 3 kết quả thuận lợi. Vậy $P(B) = \\frac{3}{15} = \\frac{1}{5}$.\nc) Các số có một chữ số từ 1 đến 15 là từ 1 đến 9 gồm 9 kết quả thuận lợi. Vậy $P(C) = \\frac{9}{15} = \\frac{3}{5}$."
      },
      {
        "id": 20,
        "question": "Lớp 7B có 36 học sinh gồm 20 học sinh nam và 16 học sinh nữ. Cô giáo gọi ngẫu nhiên một bạn lên bảng chữa bài tập.\na) Tính xác suất để bạn được gọi là bạn nam.\nb) Tính xác suất để bạn được gọi là bạn nữ.\nc) So sánh khả năng được gọi lên bảng của bạn nam và bạn nữ.",
        "rubric": [
          {
            "step": "Xác suất gọi bạn nam: P(nam) = 20/36 = 5/9.",
            "points": 0.35
          },
          {
            "step": "Xác suất gọi bạn nữ: P(nữ) = 16/36 = 4/9.",
            "points": 0.35
          },
          {
            "step": "So sánh 5/9 > 4/9 nên khả năng bạn nam được gọi cao hơn bạn nữ.",
            "points": 0.3
          }
        ],
        "solution": "Tổng số học sinh của lớp là 36.\na) Xác suất bạn được gọi là bạn nam là: $P(nam) = \\frac{20}{36} = \\frac{5}{9}$.\nb) Xác suất bạn được gọi là bạn nữ là: $P(nữ) = \\frac{16}{36} = \\frac{4}{9}$.\nc) Vì $\\frac{5}{9} > \\frac{4}{9}$ nên khả năng bạn nam được gọi lên bảng cao hơn khả năng bạn nữ được gọi."
      },
      {
        "id": 21,
        "question": "Gieo một con xúc xắc 6 mặt cân đối một lần. Tính xác suất của các biến cố sau:\na) Biến cố E: 'Số chấm xuất hiện là số nguyên tố'.\nb) Biến cố F: 'Số chấm xuất hiện không vượt quá 4'.\nc) Biến cố G: 'Số chấm xuất hiện là số lẻ hoặc lớn hơn 4'.",
        "rubric": [
          {
            "step": "Có 6 kết quả đồng khả năng {1, 2, 3, 4, 5, 6}.",
            "points": 0.1
          },
          {
            "step": "Các số nguyên tố là 2, 3, 5 (3 kết quả). P(E) = 3/6 = 1/2.",
            "points": 0.3
          },
          {
            "step": "Số chấm không vượt quá 4 là 1, 2, 3, 4 (4 kết quả). P(F) = 4/6 = 2/3.",
            "points": 0.3
          },
          {
            "step": "Số lẻ gồm {1, 3, 5}; số lớn hơn 4 gồm {5, 6}. Hợp lại là {1, 3, 5, 6} (4 kết quả). P(G) = 4/6 = 2/3.",
            "points": 0.3
          }
        ],
        "solution": "Tổng số kết quả có thể xảy ra khi gieo con xúc xắc là 6.\na) Các kết quả thuận lợi cho E là các số nguyên tố: 2; 3; 5 (gồm 3 kết quả).\nVậy $P(E) = \\frac{3}{6} = \\frac{1}{2}$.\nb) Số chấm không vượt quá 4 nghĩa là nhỏ hơn hoặc bằng 4, gồm: 1; 2; 3; 4 (gồm 4 kết quả).\nVậy $P(F) = \\frac{4}{6} = \\frac{2}{3}$.\nc) Các số lẻ là 1, 3, 5. Các số lớn hơn 4 là 5, 6. Do đó các số là số lẻ hoặc lớn hơn 4 gồm: 1; 3; 5; 6 (gồm 4 kết quả thuận lợi).\nVậy $P(G) = \\frac{4}{6} = \\frac{2}{3}$."
      }
    ]
  },
  "c8_7_bai2_test2": {
    "title": "Toán 7 - Bài 30: Làm quen với xác suất của biến cố - Đề 2 (Khá)",
    "time": 45,
    "totalPoints": 10.0,
    "part1": [
      {
        "id": 1,
        "question": "Một túi đựng các viên kẹo giống nhau gồm 5 kẹo cam, 4 kẹo dâu và 6 kẹo táo. Lấy ngẫu nhiên 1 viên kẹo. Xác suất để lấy được viên kẹo cam hoặc dâu là:",
        "options": [
          "C. $\\frac{4}{15}$",
          "A. $\\frac{1}{3}$",
          "D. $\\frac{2}{5}$",
          "B. $\\frac{3}{5}$"
        ],
        "answer": "B",
        "explanation": "Tổng số kẹo là 5 + 4 + 6 = 15. Số kẹo cam hoặc dâu là 5 + 4 = 9. Xác suất là $\\frac{9}{15} = \\frac{3}{5}$.",
        "correct": 1
      },
      {
        "id": 2,
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm xuất hiện bằng 2 là:",
        "options": [
          "C. $\\frac{1}{12}$",
          "B. $\\frac{1}{18}$",
          "D. $\\frac{1}{6}$",
          "A. $\\frac{1}{36}$"
        ],
        "answer": "A",
        "explanation": "Tổng số kết quả là 36. Cặp (1, 1) là kết quả duy nhất có tổng bằng 2. Xác suất là $\\frac{1}{36}$.",
        "correct": 3
      },
      {
        "id": 3,
        "question": "Tung hai đồng xu cân đối đồng thời. Xác suất để có đúng một đồng xu xuất hiện mặt sấp là:",
        "options": [
          "A. $\\frac{1}{4}$",
          "D. 1",
          "B. $\\frac{1}{2}$",
          "C. $\\frac{3}{4}$"
        ],
        "answer": "B",
        "explanation": "Các kết quả là SS, SN, NS, NN (4 kết quả). Có đúng 1 mặt sấp là SN, NS (2 kết quả). Xác suất là $\\frac{2}{4} = \\frac{1}{2}$.",
        "correct": 0
      },
      {
        "id": 4,
        "question": "Một hộp có 20 thẻ đánh số từ 1 đến 20. Rút ngẫu nhiên một thẻ. Xác suất để số ghi trên thẻ là số chính phương là:",
        "options": [
          "A. $\\frac{1}{5}$",
          "B. $\\frac{1}{4}$",
          "C. $\\frac{3}{20}$",
          "D. $\\frac{1}{10}$"
        ],
        "answer": "A",
        "explanation": "Các số chính phương từ 1 đến 20 là 1, 4, 9, 16 (4 số). Xác suất là $\\frac{4}{20} = \\frac{1}{5}$.",
        "correct": 0
      },
      {
        "id": 5,
        "question": "Gieo hai con xúc xắc cân đối. Xác suất để hai mặt xuất hiện có cùng số chấm là:",
        "options": [
          "C. $\\frac{1}{12}$",
          "B. $\\frac{1}{6}$",
          "D. $\\frac{5}{36}$",
          "A. $\\frac{1}{36}$"
        ],
        "answer": "B",
        "explanation": "Các cặp có số chấm bằng nhau là (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) gồm 6 kết quả. Xác suất là $\\frac{6}{36} = \\frac{1}{6}$.",
        "correct": 3
      },
      {
        "id": 6,
        "question": "Chọn ngẫu nhiên một số tự nhiên có hai chữ số. Xác suất để số được chọn chia hết cho 10 là:",
        "options": [
          "A. $\\frac{1}{10}$",
          "D. $\\frac{9}{100}$",
          "B. $\\frac{1}{9}$",
          "C. $\\frac{1}{11}$"
        ],
        "answer": "A",
        "explanation": "Các số tự nhiên có hai chữ số là từ 10 đến 99 (có 90 số). Các số chia hết cho 10 là 10, 20, ..., 90 (có 9 số). Xác suất là $\\frac{9}{90} = \\frac{1}{10}$.",
        "correct": 0
      },
      {
        "id": 7,
        "question": "Một hộp chứa 10 viên bi, trong đó có $x$ viên bi đỏ và số còn lại là bi xanh. Biết xác suất lấy được bi đỏ là 0,4. Số viên bi xanh trong hộp là:",
        "options": [
          "B. 5",
          "D. 7",
          "A. 4",
          "C. 6"
        ],
        "answer": "C",
        "explanation": "Số bi đỏ là $10 \\times 0,4 = 4$. Số bi xanh là $10 - 4 = 6$.",
        "correct": 2
      },
      {
        "id": 8,
        "question": "Gieo một con xúc xắc 6 mặt cân đối. Xác suất xuất hiện mặt có số chấm là ước của 12 là:",
        "options": [
          "B. $\\frac{2}{3}$",
          "C. $\\frac{1}{2}$",
          "A. $\\frac{5}{6}$",
          "D. 1"
        ],
        "answer": "A",
        "explanation": "Các ước của 12 trong tập {1, 2, 3, 4, 5, 6} là 1, 2, 3, 4, 6 (gồm 5 kết quả). Xác suất là $\\frac{5}{6}$.",
        "correct": 2
      },
      {
        "id": 9,
        "question": "Một tấm bìa hình tròn được chia thành 6 hình quạt bằng nhau đánh số từ 1 đến 6. Quay tấm bìa. Xác suất mũi tên chỉ vào ô ghi số nguyên tố là:",
        "options": [
          "C. $\\frac{1}{2}$",
          "D. $\\frac{2}{3}$",
          "A. $\\frac{1}{6}$",
          "B. $\\frac{1}{3}$"
        ],
        "answer": "C",
        "explanation": "Các số nguyên tố là 2, 3, 5 (3 ô). Xác suất là $\\frac{3}{6} = \\frac{1}{2}$.",
        "correct": 2
      },
      {
        "id": 10,
        "question": "Gieo hai con xúc xắc cân đối. Xác suất để tổng số chấm bằng 7 là:",
        "options": [
          "D. $\\frac{1}{12}$",
          "A. $\\frac{1}{6}$",
          "B. $\\frac{5}{36}$",
          "C. $\\frac{7}{36}$"
        ],
        "answer": "A",
        "explanation": "Có 6 cặp có tổng bằng 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). Xác suất là $\\frac{6}{36} = \\frac{1}{6}$.",
        "correct": 1
      },
      {
        "id": 11,
        "question": "Một túi chứa các thẻ ghi các chữ cái trong từ 'HOC SINH'. Rút ngẫu nhiên một thẻ. Xác suất rút được chữ 'H' là:",
        "options": [
          "B. $\\frac{2}{7}$",
          "A. $\\frac{1}{7}$",
          "D. $\\frac{2}{6}$",
          "C. $\\frac{1}{6}$"
        ],
        "answer": "B",
        "explanation": "Từ 'HOC SINH' có 7 chữ cái (H, O, C, S, I, N, H) trong đó có 2 chữ H. Xác suất là $\\frac{2}{7}$.",
        "correct": 1
      },
      {
        "id": 12,
        "question": "Xác suất để một biến cố không xảy ra bằng 0,35. Xác suất để biến cố đó xảy ra là:",
        "options": [
          "C. 0,65",
          "B. 0,75",
          "D. 0,55",
          "A. 0,35"
        ],
        "answer": "C",
        "explanation": "$1 - 0,35 = 0,65$.",
        "correct": 3
      }
    ],
    "part2": [
      {
        "id": 13,
        "stem": "Gieo đồng thời hai con xúc xắc cân đối và đồng chất.",
        "statements": [
          {
            "id": "a",
            "statement": "Số kết quả có thể xảy ra của phép thử là 36 kết quả.",
            "answer": true,
            "explanation": "$6 \\times 6 = 36$."
          },
          {
            "id": "b",
            "statement": "Xác suất để tích số chấm bằng 12 là $\\frac{1}{9}$.",
            "answer": true,
            "explanation": "Các cặp có tích bằng 12: (2,6), (3,4), (4,3), (6,2) gồm 4 cặp. Xác suất là $\\frac{4}{36} = \\frac{1}{9}$."
          },
          {
            "id": "c",
            "statement": "Xác suất để tổng số chấm lớn hơn 10 là $\\frac{1}{12}$.",
            "answer": true,
            "explanation": "Tổng > 10 gồm tổng 11 có (5,6),(6,5) và tổng 12 có (6,6) -> 3 cặp. Xác suất là $\\frac{3}{36} = \\frac{1}{12}$."
          },
          {
            "id": "d",
            "statement": "Xác suất để hai con xúc xắc có số chấm khác nhau là $\\frac{5}{6}$.",
            "answer": true,
            "explanation": "Xác suất có số chấm giống nhau là $\\frac{6}{36} = \\frac{1}{6}$. Vậy xác suất khác nhau là $1 - \\frac{1}{6} = \\frac{5}{6}$."
          }
        ]
      },
      {
        "id": 14,
        "stem": "Một hộp chứa 30 tấm thẻ cùng loại được ghi số từ 1 đến 30. Rút ngẫu nhiên một tấm thẻ.",
        "statements": [
          {
            "id": "a",
            "statement": "Xác suất rút được thẻ ghi số có hai chữ số là $\\frac{7}{10}$.",
            "answer": true,
            "explanation": "Từ 10 đến 30 có 21 số. Xác suất là $\\frac{21}{30} = \\frac{7}{10}$."
          },
          {
            "id": "b",
            "statement": "Xác suất rút được thẻ ghi số chia hết cho 4 là $\\frac{7}{30}$.",
            "answer": true,
            "explanation": "Các số chia hết cho 4: 4, 8, 12, 16, 20, 24, 28 (7 số). Xác suất là $\\frac{7}{30}$."
          },
          {
            "id": "c",
            "statement": "Xác suất rút được thẻ ghi số vừa chia hết cho 2 vừa chia hết cho 5 là $\\frac{1}{10}$.",
            "answer": true,
            "explanation": "Số chia hết cho cả 2 và 5 là số tận cùng bằng 0: 10, 20, 30 (3 số). Xác suất là $\\frac{3}{30} = \\frac{1}{10}$."
          },
          {
            "id": "d",
            "statement": "Xác suất rút được thẻ ghi số nguyên tố nhỏ hơn 10 là $\\frac{1}{6}$.",
            "answer": false,
            "explanation": "Các số nguyên tố nhỏ hơn 10 là 2, 3, 5, 7 (4 số). Xác suất là $\\frac{4}{30} = \\frac{2}{15} \\neq \\frac{1}{6}$."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 15,
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Tính xác suất để tổng số chấm xuất hiện bằng 8 (kết quả viết dưới dạng phân số tối giản).",
        "answer": "5/36",
        "explanation": "Các cặp có tổng bằng 8 là (2,6), (3,5), (4,4), (5,3), (6,2) gồm 5 cặp. Xác suất là 5/36."
      },
      {
        "id": 16,
        "question": "Tung 3 đồng xu cân đối đồng thời. Tính xác suất để có đúng 2 đồng xu xuất hiện mặt ngửa.",
        "answer": "3/8",
        "explanation": "Có 8 kết quả. Số kết quả có đúng 2 mặt ngửa là (N, N, S), (N, S, N), (S, N, N) (3 kết quả). Xác suất là 3/8."
      },
      {
        "id": 17,
        "question": "Một hộp có 5 viên bi xanh, 7 viên bi đỏ và một số viên bi vàng. Lấy ngẫu nhiên 1 viên bi, biết xác suất lấy được bi vàng là 0,4. Hỏi trong hộp có bao nhiêu viên bi vàng?",
        "answer": "8",
        "explanation": "Tổng số bi xanh và đỏ là 5 + 7 = 12, chiếm 1 - 0,4 = 0,6 tổng số bi. Tổng số bi trong hộp là 12 / 0,6 = 20 viên. Số bi vàng là 20 - 12 = 8 viên."
      },
      {
        "id": 18,
        "question": "Chọn ngẫu nhiên một số tự nhiên có hai chữ số từ 10 đến 99. Tính xác suất để số được chọn có hai chữ số giống nhau (kết quả viết dưới dạng phân số tối giản).",
        "answer": "1/10",
        "explanation": "Có 90 số có hai chữ số. Các số có hai chữ số giống nhau là 11, 22, ..., 99 (9 số). Xác suất = 9/90 = 1/10."
      }
    ],
    "part4": [
      {
        "id": 19,
        "question": "Gieo đồng thời hai con xúc xắc 6 mặt cân đối. Tính xác suất của các biến cố sau:\na) Biến cố A: 'Tổng số chấm xuất hiện bằng 6'.\nb) Biến cố B: 'Tích số chấm xuất hiện bằng 6'.\nc) Biến cố C: 'Hiệu số chấm giữa hai con xúc xắc bằng 0'.",
        "rubric": [
          {
            "step": "Tổng số kết quả có thể xảy ra khi gieo hai con xúc xắc là 36.",
            "points": 0.1
          },
          {
            "step": "Tổng bằng 6: (1,5), (2,4), (3,3), (4,2), (5,1) gồm 5 kết quả. P(A) = 5/36.",
            "points": 0.3
          },
          {
            "step": "Tích bằng 6: (1,6), (2,3), (3,2), (6,1) gồm 4 kết quả. P(B) = 4/36 = 1/9.",
            "points": 0.3
          },
          {
            "step": "Hiệu bằng 0: (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) gồm 6 kết quả. P(C) = 6/36 = 1/6.",
            "points": 0.3
          }
        ],
        "solution": "Số kết quả có thể xảy ra của phép thử là $6 \\times 6 = 36$.\na) Các kết quả thuận lợi cho A: (1, 5), (2, 4), (3, 3), (4, 2), (5, 1) gồm 5 kết quả. Vậy $P(A) = \\frac{5}{36}$.\nb) Các kết quả thuận lợi cho B: (1, 6), (2, 3), (3, 2), (6, 1) gồm 4 kết quả. Vậy $P(B) = \\frac{4}{36} = \\frac{1}{9}$.\nc) Hiệu số chấm bằng 0 tức hai con xúc xắc có số chấm bằng nhau: (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) gồm 6 kết quả. Vậy $P(C) = \\frac{6}{36} = \\frac{1}{6}$."
      },
      {
        "id": 20,
        "question": "Một túi đựng 25 chiếc thẻ được đánh số từ 1 đến 25. Rút ngẫu nhiên một thẻ từ trong túi.\na) Tính xác suất để số ghi trên thẻ là số nguyên tố.\nb) Tính xác suất để số ghi trên thẻ chia hết cho cả 2 và 3.\nc) Tính xác suất để số ghi trên thẻ có chữ số hàng đơn vị là 5.",
        "rubric": [
          {
            "step": "Số kết quả có thể là 25.",
            "points": 0.1
          },
          {
            "step": "Số nguyên tố từ 1 đến 25: 2, 3, 5, 7, 11, 13, 17, 19, 23 (9 số). Xác suất là 9/25.",
            "points": 0.3
          },
          {
            "step": "Số chia hết cho 6: 6, 12, 18, 24 (4 số). Xác suất là 4/25.",
            "points": 0.3
          },
          {
            "step": "Số có chữ số hàng đơn vị là 5: 5, 15, 25 (3 số). Xác suất là 3/25.",
            "points": 0.3
          }
        ],
        "solution": "Tổng số kết quả có thể xảy ra là 25.\na) Các số nguyên tố từ 1 đến 25 là: 2; 3; 5; 7; 11; 13; 17; 19; 23 gồm 9 số.\nXác suất là $P = \\frac{9}{25}$.\nb) Số chia hết cho cả 2 và 3 là bội của 6: 6; 12; 18; 24 gồm 4 số.\nXác suất là $P = \\frac{4}{25}$.\nc) Các số có chữ số hàng đơn vị là 5 gồm: 5; 15; 25 gồm 3 số.\nXác suất là $P = \\frac{3}{25}$."
      },
      {
        "id": 21,
        "question": "Trong một hộp kín có một số quả bóng bàn màu trắng và màu cam cùng kích thước. Bạn Nam lấy ngẫu nhiên một quả bóng, ghi lại màu rồi trả lại hộp. Lặp lại thí nghiệm đó 100 lần, Nam thấy có 35 lần lấy được bóng màu cam.\na) Tính xác suất thực nghiệm của biến cố 'Lấy được bóng màu cam'.\nb) Giả sử trong hộp có tất cả 20 quả bóng. Hãy ước lượng xem trong hộp có khoảng bao nhiêu quả bóng màu trắng.",
        "rubric": [
          {
            "step": "Xác suất thực nghiệm của biến cố lấy được bóng cam là 35/100 = 0,35.",
            "points": 0.4
          },
          {
            "step": "Ước lượng số bóng cam trong hộp: 20 x 0,35 = 7 quả.",
            "points": 0.3
          },
          {
            "step": "Ước lượng số bóng trắng trong hộp: 20 - 7 = 13 quả.",
            "points": 0.3
          }
        ],
        "solution": "a) Xác suất thực nghiệm của biến cố 'Lấy được bóng màu cam' qua 100 lần thử là:\n$P_{tn} = \\frac{35}{100} = 0,35$.\nb) Vì số lần thử khá lớn (100 lần), xác suất thực nghiệm xấp xỉ xác suất lí thuyết.\nSố bóng màu cam trong hộp ước lượng là: $20 \\times 0,35 = 7$ (quả).\nVậy số quả bóng màu trắng trong hộp khoảng: $20 - 7 = 13$ (quả)."
      }
    ]
  },
  "c8_7_bai2_test3": {
    "title": "Toán 7 - Bài 30: Làm quen với xác suất của biến cố - Đề 3 (Nâng cao)",
    "time": 45,
    "totalPoints": 10.0,
    "part1": [
      {
        "id": 1,
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để số chấm xuất hiện trên hai con xúc xắc hơn kém nhau 2 chấm là:",
        "options": [
          "D. $\\frac{1}{4}$",
          "A. $\\frac{1}{6}$",
          "B. $\\frac{2}{9}$",
          "C. $\\frac{5}{18}$"
        ],
        "answer": "B",
        "explanation": "Các cặp có hiệu bằng 2: (1,3), (2,4), (3,5), (4,6) và hoán vị (3,1), (4,2), (5,3), (6,4) -> 8 cặp. Xác suất là $\\frac{8}{36} = \\frac{2}{9}$.",
        "correct": 1
      },
      {
        "id": 2,
        "question": "Chọn ngẫu nhiên một số tự nhiên có 3 chữ số. Xác suất để số được chọn chia hết cho 5 là:",
        "options": [
          "B. $\\frac{1}{4}$",
          "D. $\\frac{2}{9}$",
          "A. $\\frac{1}{5}$",
          "C. $\\frac{1}{10}$"
        ],
        "answer": "A",
        "explanation": "Các số có 3 chữ số từ 100 đến 999 có 900 số. Các số chia hết cho 5 là từ 100 đến 995, có $\\frac{995 - 100}{5} + 1 = 180$ số. Xác suất là $\\frac{180}{900} = \\frac{1}{5}$.",
        "correct": 2
      },
      {
        "id": 3,
        "question": "Tung 4 đồng xu cân đối đồng thời. Xác suất để có ít nhất một mặt ngửa là:",
        "options": [
          "D. $\\frac{3}{4}$",
          "B. $\\frac{15}{16}$",
          "A. $\\frac{1}{16}$",
          "C. $\\frac{7}{8}$"
        ],
        "answer": "B",
        "explanation": "Tổng số kết quả là $2^4 = 16$. Chỉ có duy nhất 1 kết quả không có mặt ngửa nào (SSSS). Xác suất ít nhất 1 ngửa là $1 - \\frac{1}{16} = \\frac{15}{16}$.",
        "correct": 2
      },
      {
        "id": 4,
        "question": "Gieo hai con xúc xắc cân đối. Xác suất để tích số chấm là một số chính phương là:",
        "options": [
          "B. $\\frac{2}{9}$",
          "A. $\\frac{7}{36}$",
          "D. $\\frac{5}{18}$",
          "C. $\\frac{1}{6}$"
        ],
        "answer": "B",
        "explanation": "Tích là chính phương gồm: hai số bằng nhau (1,1),(2,2),(3,3),(4,4),(5,5),(6,6) (6 cặp) và các cặp khác nhau: (1,4), (4,1) (tích 4) -> 2 cặp. Tổng cộng 6 + 2 = 8 cặp. Xác suất là $\\frac{8}{36} = \\frac{2}{9}$.",
        "correct": 1
      },
      {
        "id": 5,
        "question": "Một hộp có 12 tấm thẻ ghi số từ 1 đến 12. Rút ngẫu nhiên đồng thời hai thẻ. Số kết quả có thể xảy ra của phép thử là:",
        "options": [
          "A. 144",
          "C. 132",
          "B. 66",
          "D. 24"
        ],
        "answer": "B",
        "explanation": "Số cách chọn 2 thẻ từ 12 thẻ là $\\frac{12 \\times 11}{2} = 66$.",
        "correct": 0
      },
      {
        "id": 6,
        "question": "Một hộp đựng 4 bi xanh, 5 bi đỏ và 6 bi vàng. Lấy ngẫu nhiên 1 viên bi. Xác suất để viên bi lấy ra không có màu đỏ là:",
        "options": [
          "B. $\\frac{2}{3}$",
          "C. $\\frac{3}{5}$",
          "D. $\\frac{4}{15}$",
          "A. $\\frac{1}{3}$"
        ],
        "answer": "B",
        "explanation": "Tổng số bi là 4 + 5 + 6 = 15. Số bi không phải màu đỏ là 4 + 6 = 10. Xác suất là $\\frac{10}{15} = \\frac{2}{3}$.",
        "correct": 3
      },
      {
        "id": 7,
        "question": "Gieo hai con xúc xắc. Xác suất để tổng số chấm xuất hiện là số chia hết cho 4 là:",
        "options": [
          "D. $\\frac{7}{36}$",
          "C. $\\frac{5}{18}$",
          "B. $\\frac{1}{6}$",
          "A. $\\frac{1}{4}$"
        ],
        "answer": "A",
        "explanation": "Tổng chia hết cho 4 có thể là 4, 8, 12. Tổng = 4 có 3 cặp; Tổng = 8 có 5 cặp; Tổng = 12 có 1 cặp. Tổng cộng 3 + 5 + 1 = 9 cặp. Xác suất là $\\frac{9}{36} = \\frac{1}{4}$.",
        "correct": 3
      },
      {
        "id": 8,
        "question": "Từ các chữ số 1, 2, 3, 4, 5 viết ngẫu nhiên một số tự nhiên có hai chữ số khác nhau. Xác suất để số đó chia hết cho 3 là:",
        "options": [
          "A. $\\frac{2}{5}$",
          "D. $\\frac{1}{5}$",
          "C. $\\frac{3}{10}$",
          "B. $\\frac{1}{2}$"
        ],
        "answer": "A",
        "explanation": "Tổng số các số viết được là $5 \\times 4 = 20$. Các cặp hai chữ số có tổng chia hết cho 3 là (1,2), (1,5), (2,4), (4,5) mỗi cặp cho 2 số. Tổng có $4 \\times 2 = 8$ số. Xác suất là $\\frac{8}{20} = \\frac{2}{5}$.",
        "correct": 0
      },
      {
        "id": 9,
        "question": "Một đa giác đều 12 đỉnh. Chọn ngẫu nhiên một đỉnh. Xác suất để đỉnh đó là một trong các đỉnh thuộc trục đối xứng của đa giác là:",
        "options": [
          "A. Không xác định",
          "C. $\\frac{1}{6}$",
          "B. Phụ thuộc góc quay",
          "D. 1"
        ],
        "answer": "D",
        "explanation": "Mỗi đỉnh của đa giác đều 12 đỉnh đều nằm trên một trục đối xứng (đa giác có số đỉnh chẵn có các trục đối xứng đi qua các cặp đỉnh đối diện). Do đó biến cố này là chắc chắn, xác suất bằng 1.",
        "correct": 0
      },
      {
        "id": 10,
        "question": "Một người gọi điện thoại nhưng quên mất chữ số cuối cùng, chỉ nhớ nó là một chữ số lẻ. Người đó bấm ngẫu nhiên một chữ số lẻ. Xác suất để người đó gọi đúng ngay lần đầu là:",
        "options": [
          "C. $\\frac{1}{2}$",
          "D. $\\frac{1}{9}$",
          "A. $\\frac{1}{10}$",
          "B. $\\frac{1}{5}$"
        ],
        "answer": "B",
        "explanation": "Có 5 chữ số lẻ (1, 3, 5, 7, 9). Chọn ngẫu nhiên 1 chữ số đúng trong 5 chữ số có xác suất $\\frac{1}{5}$.",
        "correct": 2
      },
      {
        "id": 11,
        "question": "Gieo hai con xúc xắc cân đối. Xác suất để có ít nhất một con xúc xắc xuất hiện mặt 6 chấm là:",
        "options": [
          "C. $\\frac{1}{3}$",
          "A. $\\frac{1}{6}$",
          "D. $\\frac{5}{18}$",
          "B. $\\frac{11}{36}$"
        ],
        "answer": "B",
        "explanation": "Số kết quả không có mặt 6 nào là $5 \\times 5 = 25$. Số kết quả có ít nhất 1 mặt 6 là $36 - 25 = 11$. Xác suất là $\\frac{11}{36}$.",
        "correct": 1
      },
      {
        "id": 12,
        "question": "Một hộp có 100 chiếc thẻ đánh số từ 1 đến 100. Rút ngẫu nhiên 1 thẻ. Xác suất để số trên thẻ chia hết cho cả 3 và 4 là:",
        "options": [
          "C. $\\frac{1}{10}$",
          "B. $\\frac{1}{12}$",
          "D. $\\frac{7}{100}$",
          "A. $\\frac{2}{25}$"
        ],
        "answer": "A",
        "explanation": "Chia hết cho cả 3 và 4 tức chia hết cho 12. Từ 1 đến 100 có các số 12, 24, 36, 48, 60, 72, 84, 96 (8 số). Xác suất là $\\frac{8}{100} = \\frac{2}{25}$.",
        "correct": 3
      }
    ],
    "part2": [
      {
        "id": 13,
        "stem": "Gieo đồng thời hai con xúc xắc cân đối 6 mặt. Kí hiệu $(x, y)$ là số chấm xuất hiện trên hai con xúc xắc.",
        "statements": [
          {
            "id": "a",
            "statement": "Xác suất để $x + y = 9$ bằng $\\frac{1}{9}$.",
            "answer": true,
            "explanation": "Các cặp có tổng bằng 9: (3,6), (4,5), (5,4), (6,3) có 4 cặp. Xác suất là $\\frac{4}{36} = \\frac{1}{9}$."
          },
          {
            "id": "b",
            "statement": "Xác suất để $x > y$ bằng $\\frac{5}{12}$.",
            "answer": true,
            "explanation": "Có 6 cặp $x = y$. Còn lại 30 cặp chia đều cho $x > y$ và $x < y$ nên có 15 cặp $x > y$. Xác suất là $\\frac{15}{36} = \\frac{5}{12}$."
          },
          {
            "id": "c",
            "statement": "Xác suất để $x \\cdot y$ là số lẻ bằng $\\frac{1}{2}$.",
            "answer": false,
            "explanation": "Tích là số lẻ khi cả $x$ và $y$ đều lẻ: $3 \\times 3 = 9$ cặp. Xác suất là $\\frac{9}{36} = \\frac{1}{4} \\neq \\frac{1}{2}$."
          },
          {
            "id": "d",
            "statement": "Xác suất để $x + y \\le 4$ bằng $\\frac{1}{6}$.",
            "answer": true,
            "explanation": "Tổng $\\le 4$ gồm: tổng 2 có 1 cặp; tổng 3 có 2 cặp; tổng 4 có 3 cặp. Tổng cộng 1 + 2 + 3 = 6 cặp. Xác suất $\\frac{6}{36} = \\frac{1}{6}$."
          }
        ]
      },
      {
        "id": 14,
        "stem": "Một hộp chứa 50 chiếc thẻ cùng loại đánh số từ 1 đến 50. Rút ngẫu nhiên một chiếc thẻ.",
        "statements": [
          {
            "id": "a",
            "statement": "Xác suất để rút được thẻ ghi số có chữ số tận cùng là 2 bằng $\\frac{1}{10}$.",
            "answer": true,
            "explanation": "Các số tận cùng là 2 gồm: 2, 12, 22, 32, 42 (5 số). Xác suất là $\\frac{5}{50} = \\frac{1}{10}$."
          },
          {
            "id": "b",
            "statement": "Xác suất để rút được thẻ ghi số chia hết cho cả 3 và 5 bằng $\\frac{3}{50}$.",
            "answer": true,
            "explanation": "Số chia hết cho 15 gồm: 15, 30, 45 (3 số). Xác suất là $\\frac{3}{50}$."
          },
          {
            "id": "c",
            "statement": "Xác suất để số trên thẻ là số chính phương lớn hơn 10 bằng 0,08.",
            "answer": true,
            "explanation": "Các số chính phương lớn hơn 10 và $\\le 50$ là 16, 25, 36, 49 (4 số). Xác suất là $\\frac{4}{50} = 0,08$."
          },
          {
            "id": "d",
            "statement": "Biến cố 'Rút được thẻ ghi số lớn hơn 50' có xác suất bằng 1.",
            "answer": false,
            "explanation": "Các thẻ chỉ đánh số từ 1 đến 50 nên biến cố này là không thể, xác suất bằng 0."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 15,
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Tính xác suất để tích hai số chấm xuất hiện chia hết cho 5 (kết quả viết dưới dạng phân số tối giản).",
        "answer": "11/36",
        "explanation": "Tích chia hết cho 5 khi có ít nhất một con xuất hiện mặt 5 chấm. Số kết quả không có mặt 5 là 5x5=25. Số kết quả có ít nhất 1 mặt 5 là 36 - 25 = 11. Xác suất là 11/36."
      },
      {
        "id": 16,
        "question": "Một bình kín có 12 viên bi đỏ và $n$ viên bi xanh có kích thước giống nhau. Lấy ngẫu nhiên một viên bi, biết xác suất lấy được bi xanh là 0,6. Tìm giá trị của $n$.",
        "answer": "18",
        "explanation": "Xác suất lấy bi đỏ là 1 - 0,6 = 0,4. Tổng số bi là 12 / 0,4 = 30 viên. Vậy số bi xanh n = 30 - 12 = 18 viên."
      },
      {
        "id": 17,
        "question": "Chọn ngẫu nhiên một số tự nhiên có hai chữ số từ 10 đến 99. Tính xác suất để tổng hai chữ số của số đó bằng 9 (kết quả viết dưới dạng phân số tối giản).",
        "answer": "1/10",
        "explanation": "Có 90 số. Các số có tổng 2 chữ số bằng 9 là 18, 27, 36, 45, 54, 63, 72, 81, 90 (9 số). Xác suất là 9/90 = 1/10."
      },
      {
        "id": 18,
        "question": "Tung 3 đồng xu cân đối đồng thời. Tính xác suất để có ít nhất hai đồng xu xuất hiện mặt sấp.",
        "answer": "1/2",
        "explanation": "Có ít nhất 2 sấp gồm 2 sấp (3 kết quả) và 3 sấp (1 kết quả). Tổng cộng 4 kết quả trên 8. Xác suất là 4/8 = 1/2."
      }
    ],
    "part4": [
      {
        "id": 19,
        "question": "Gieo đồng thời hai con xúc xắc 6 mặt cân đối.\na) Tính xác suất để tổng số chấm xuất hiện trên hai con xúc xắc là một số nguyên tố.\nb) Tính xác suất để hiệu số chấm xuất hiện trên hai con xúc xắc bằng 1.\nc) Tính xác suất để số chấm trên con xúc xắc thứ nhất gấp đôi số chấm trên con xúc xắc thứ hai.",
        "rubric": [
          {
            "step": "Tổng số kết quả là 36.",
            "points": 0.1
          },
          {
            "step": "Tổng nguyên tố: 2, 3, 5, 7, 11 gồm 15 cặp. P = 15/36 = 5/12.",
            "points": 0.3
          },
          {
            "step": "Hiệu bằng 1: (1,2), (2,3), (3,4), (4,5), (5,6) và ngược lại (10 cặp). P = 10/36 = 5/18.",
            "points": 0.3
          },
          {
            "step": "Số chấm thứ nhất gấp đôi thứ hai: (2,1), (4,2), (6,3) gồm 3 cặp. P = 3/36 = 1/12.",
            "points": 0.3
          }
        ],
        "solution": "Tổng số kết quả có thể xảy ra của phép thử là $6 \\times 6 = 36$.\na) Các giá trị nguyên tố có thể của tổng hai con xúc xắc là 2, 3, 5, 7, 11:\n- Tổng = 2: (1,1) -> 1 cặp\n- Tổng = 3: (1,2), (2,1) -> 2 cặp\n- Tổng = 5: (1,4), (2,3), (3,2), (4,1) -> 4 cặp\n- Tổng = 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) -> 6 cặp\n- Tổng = 11: (5,6), (6,5) -> 2 cặp\nTổng số kết quả thuận lợi là $1 + 2 + 4 + 6 + 2 = 15$.\nXác suất là $P = \\frac{15}{36} = \\frac{5}{12}$.\nb) Các cặp có hiệu số chấm bằng 1 là: (1,2), (2,3), (3,4), (4,5), (5,6) và (2,1), (3,2), (4,3), (5,4), (6,5) gồm 10 cặp.\nXác suất là $P = \\frac{10}{36} = \\frac{5}{18}$.\nc) Các cặp có số chấm xúc xắc thứ nhất gấp đôi xúc xắc thứ hai là: (2,1), (4,2), (6,3) gồm 3 cặp.\nXác suất là $P = \\frac{3}{36} = \\frac{1}{12}$."
      },
      {
        "id": 20,
        "question": "Một tổ có 5 học sinh nam và 3 học sinh nữ. Thầy giáo gọi ngẫu nhiên lần lượt 2 bạn lên bảng (bạn thứ nhất lên bảng xong không gọi lại nữa).\na) Tính số kết quả có thể xảy ra khi chọn lần lượt 2 bạn.\nb) Tính xác suất để cả 2 bạn được gọi đều là bạn nữ.\nc) Tính xác suất để trong 2 bạn được gọi có ít nhất 1 bạn nam.",
        "rubric": [
          {
            "step": "Số kết quả chọn lần lượt 2 bạn: 8 x 7 = 56 kết quả.",
            "points": 0.35
          },
          {
            "step": "Cả 2 bạn đều nữ: chọn bạn thứ nhất có 3 cách, bạn thứ hai có 2 cách -> 3 x 2 = 6 kết quả. Xác suất là 6/56 = 3/28.",
            "points": 0.35
          },
          {
            "step": "Xác suất có ít nhất 1 bạn nam là biến cố đối của 'cả 2 đều nữ': P = 1 - 3/28 = 25/28.",
            "points": 0.3
          }
        ],
        "solution": "Tổng số học sinh là $5 + 3 = 8$ bạn.\na) Bạn thứ nhất có 8 cách chọn, bạn thứ hai có 7 cách chọn. Số kết quả có thể xảy ra là: $8 \\times 7 = 56$ kết quả.\nb) Để cả 2 bạn đều là nữ: bạn thứ nhất có 3 cách chọn, bạn thứ hai có 2 cách chọn. Số kết quả thuận lợi là $3 \\times 2 = 6$.\nXác suất là $P = \\frac{6}{56} = \\frac{3}{28}$.\nc) Biến cố 'Trong 2 bạn có ít nhất 1 bạn nam' là biến cố đối của biến cố 'Cả 2 bạn đều là nữ'.\nDo đó xác suất cần tìm là: $P = 1 - \\frac{3}{28} = \\frac{25}{28}$."
      },
      {
        "id": 21,
        "question": "Một hộp kín chứa 40 viên bi gồm 3 màu: xanh, đỏ và vàng có kích thước như nhau. Biết số bi đỏ gấp đôi số bi xanh. Lấy ngẫu nhiên 1 viên bi, xác suất lấy được bi vàng là 0,25.\na) Tính số viên bi vàng trong hộp.\nb) Tính số viên bi xanh và số viên bi đỏ trong hộp.\nc) Tính xác suất để lấy được viên bi không phải màu xanh.",
        "rubric": [
          {
            "step": "Số bi vàng: 40 x 0,25 = 10 viên.",
            "points": 0.3
          },
          {
            "step": "Tổng số bi xanh và đỏ: 40 - 10 = 30 viên. Vì bi đỏ gấp đôi bi xanh nên bi xanh là 30 / 3 = 10 viên, bi đỏ là 20 viên.",
            "points": 0.4
          },
          {
            "step": "Số bi không phải màu xanh là 40 - 10 = 30 viên. Xác suất là 30/40 = 3/4 = 0,75.",
            "points": 0.3
          }
        ],
        "solution": "a) Số viên bi vàng trong hộp là:\n$40 \\times 0,25 = 10$ (viên bi).\nb) Tổng số viên bi xanh và bi đỏ là:\n$40 - 10 = 30$ (viên bi).\nTheo đề bài, số bi đỏ gấp đôi số bi xanh, ta coi số bi xanh là 1 phần thì số bi đỏ là 2 phần (tổng 3 phần).\nSố viên bi xanh là: $30 : (1 + 2) \\times 1 = 10$ (viên bi).\nSố viên bi đỏ là: $30 - 10 = 20$ (viên bi).\nc) Số viên bi không phải màu xanh là số bi đỏ và vàng, gồm $20 + 10 = 30$ viên.\nXác suất lấy được viên bi không phải màu xanh là:\n$P = \\frac{30}{40} = \\frac{3}{4} = 0,75$."
      }
    ]
  },
  "c8_7_bai3_test1": {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương VIII: Làm quen với biến cố và xác suất của biến cố - Đề số 01",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Biến cố chắc chắn là biến cố (Đề 01):",
        "options": [
          "Luôn xảy ra trong phép thử",
          "Không bao giờ xảy ra",
          "Có thể xảy ra hoặc không",
          "Có xác suất bằng 0"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Biến cố không thể là biến cố:",
        "options": [
          "Không bao giờ xảy ra trong phép thử",
          "Luôn luôn xảy ra",
          "Xảy ra với xác suất 1",
          "Xảy ra với xác suất 0,5"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Gieo một con xúc xắc 6 mặt cân đối thì biến cố nào sau đây là ngẫu nhiên?",
        "options": [
          "Xuất hiện mặt có số chấm là số chẵn",
          "Xuất hiện mặt 7 chấm",
          "Xuất hiện mặt có số chấm nhỏ hơn 10",
          "Xuất hiện mặt 0 chấm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Xác suất của biến cố chắc chắn bằng:",
        "options": [
          "1",
          "0",
          "0,5",
          "-1"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc cân đối. Xác suất xuất hiện mặt có số chấm chia hết cho 3 là:",
        "options": [
          "$\\frac{1}{3}$",
          "$\\frac{1}{2}$",
          "$\\frac{1}{6}$",
          "$\\frac{2}{3}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Một túi có 6 viên kẹo màu xanh và 5 viên kẹo màu đỏ. Lấy ngẫu nhiên 1 chiếc kẹo. Biến cố lấy được kẹo màu xanh có xác suất là:",
        "options": [
          "$\\frac{6}{11}$",
          "$\\frac{1}{2}$",
          "$\\frac{5}{10}$",
          "$\\frac{1}{5}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Rút ngẫu nhiên một lá bài trong bộ bài có 10 lá đánh số từ 1 đến 10. Xác suất rút được lá bài ghi số nguyên tố là:",
        "options": [
          "0,4",
          "0,5",
          "0,3",
          "0,2"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tung một đồng xu 20 lần thấy có 12 lần xuất hiện mặt Ngửa. Xác suất thực nghiệm xuất hiện mặt Ngửa là:",
        "options": [
          "0,6",
          "0,4",
          "0,5",
          "0,8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hội khỏe Phù Đổng trường có 16 đội bóng chuyền tham gia thi đấu loại trực tiếp bốc thăm ngẫu nhiên. Xác suất để đội lớp 7A gặp đội lớp 7B ngay ở trận đầu tiên là một biến cố:",
        "options": [
          "Ngẫu nhiên",
          "Chắc chắn",
          "Không thể",
          "Đồng khả năng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một hộp có 1 quả bóng xanh, 1 quả bóng đỏ, 1 quả bóng vàng. Bạn An lấy ra 1 quả rồi đặt lại vào hộp, sau đó bạn Bình lấy ra 1 quả. Số kết quả có thể xảy ra là:",
        "options": [
          "9",
          "3",
          "6",
          "8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Trong một hộp có 25 chiếc bút bi, trong đó có 5 chiếc bút màu đỏ, còn lại là màu xanh. Xác suất lấy được chiếc bút màu xanh là:",
        "options": [
          "0.80",
          "0,75",
          "0,5",
          "0,25"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm trên hai con xúc xắc bằng 11 là:",
        "options": [
          "$\\frac{2}{36} = \\frac{1}{18}$",
          "$\\frac{1}{36}$",
          "$\\frac{3}{36}$",
          "$\\frac{4}{36}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về biến cố (Đề 01):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Biến cố ngẫu nhiên là biến cố có thể xảy ra hoặc không xảy ra tùy thuộc vào kết quả của phép thử.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Xác suất của một biến cố là một con số nằm giữa 0 và 1 (kể cả 0 và 1).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Gieo một con xúc xắc 6 mặt thì xác suất ra mặt 1 chấm bằng xác suất ra mặt 6 chấm.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Nếu tung đồng xu 10 lần đều ra mặt Sấp thì chắc chắn lần thứ 11 sẽ ra mặt Ngửa.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Trong một hộp kín có 11 thẻ trắng và 10 thẻ đen có cùng kích thước và khối lượng (Mã đề 01):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hành động rút ngẫu nhiên 1 thẻ là một phép thử ngẫu nhiên.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng số kết quả có thể xảy ra khi rút 1 thẻ là 21.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Xác suất rút được thẻ đen là 10 / (21).",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Khả năng rút được thẻ đen luôn cao hơn rút được thẻ trắng với mọi t >= 1.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc 6 mặt. Tính xác suất xuất hiện mặt có số chấm là số lẻ.",
        "answer": "0.5",
        "acceptableAnswers": [
          "0.5"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.5**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một hộp có 7 bi xanh và 4 bi đỏ. Tính tổng số kết quả có thể xảy ra khi lấy ngẫu nhiên 1 viên bi.",
        "answer": "11",
        "acceptableAnswers": [
          "11"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **11**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tung một đồng xu 40 lần thấy xuất hiện mặt Ngửa 22 lần. Tính xác suất thực nghiệm xuất hiện mặt Sấp.",
        "answer": "0.45",
        "acceptableAnswers": [
          "0.45"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.45**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong hộp có 10 tấm thẻ đánh số từ 1 đến 10. Rút ngẫu nhiên 1 thẻ. Tính xác suất thẻ rút được ghi số lớn hơn 7.",
        "answer": "0.3",
        "acceptableAnswers": [
          "0.3"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.3**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một hộp đựng 6 tấm thẻ ghi số chẵn và 5 tấm thẻ ghi số lẻ. Rút ngẫu nhiên 1 tấm thẻ. Tính xác suất rút được thẻ ghi số chẵn và xác suất rút được thẻ ghi số lẻ.",
        "rubric": "Tổng số tấm thẻ trong hộp: (6) + 5 = 11 thẻ (0.25đ).\nSố kết quả thuận lợi rút thẻ số chẵn là 6 (0.25đ).\nXác suất rút thẻ chẵn: P(Chẵn) = (6) / (11) (0.25đ).\nXác suất rút thẻ lẻ: P(Lẻ) = 5 / (11) (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Trong một đợt kiểm tra chất lượng sản phẩm gồm 110 linh kiện điện tử, người ta phát hiện có 5 linh kiện bị lỗi. Hãy tính xác suất thực nghiệm một linh kiện bị lỗi và ước lượng nếu sản xuất 10 000 linh kiện thì có khoảng bao nhiêu linh kiện bị lỗi.",
        "rubric": "Xác suất thực nghiệm linh kiện bị lỗi: P = 5 / (110) (0.25đ).\nTỉ lệ lỗi thực nghiệm ước tính cho toàn bộ lô hàng (0.25đ).\nSố linh kiện lỗi dự đoán trong 10 000 linh kiện: N = 10 000 . P (0.25đ).\nTính toán và kết luận số linh kiện lỗi ước lượng (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một chiếc hộp có 3 quả bóng xanh và 2 quả bóng đỏ. Bạn Nam lấy ngẫu nhiên 1 quả bóng, xem màu rồi KHÔNG trả lại vào hộp. Sau đó bạn Bình lấy tiếp 1 quả bóng. Tính xác suất để cả hai bạn đều lấy được bóng màu xanh.",
        "rubric": "Xác suất bạn Nam lấy được quả bóng màu xanh lần thứ nhất là: 3/5 (0.25đ).\nSau khi Nam lấy 1 bóng xanh, trong hộp còn lại 4 quả bóng (gồm 2 xanh và 2 đỏ) (0.25đ).\nXác suất bạn Bình lấy được quả bóng màu xanh lần thứ hai là: 2/4 = 1/2 (0.25đ).\nXác suất để cả hai bạn cùng lấy được bóng xanh là: (3/5) . (1/2) = 3/10 = 0,3 (0.25đ)."
      }
    ]
  },
  "c8_7_bai3_test2": {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương VIII: Làm quen với biến cố và xác suất của biến cố - Đề số 02",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Biến cố chắc chắn là biến cố (Đề 02):",
        "options": [
          "Luôn xảy ra trong phép thử",
          "Không bao giờ xảy ra",
          "Có thể xảy ra hoặc không",
          "Có xác suất bằng 0"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Biến cố không thể là biến cố:",
        "options": [
          "Không bao giờ xảy ra trong phép thử",
          "Luôn luôn xảy ra",
          "Xảy ra với xác suất 1",
          "Xảy ra với xác suất 0,5"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Gieo một con xúc xắc 6 mặt cân đối thì biến cố nào sau đây là ngẫu nhiên?",
        "options": [
          "Xuất hiện mặt có số chấm là số chẵn",
          "Xuất hiện mặt 7 chấm",
          "Xuất hiện mặt có số chấm nhỏ hơn 10",
          "Xuất hiện mặt 0 chấm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Xác suất của biến cố chắc chắn bằng:",
        "options": [
          "1",
          "0",
          "0,5",
          "-1"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc cân đối. Xác suất xuất hiện mặt có số chấm chia hết cho 3 là:",
        "options": [
          "$\\frac{1}{3}$",
          "$\\frac{1}{2}$",
          "$\\frac{1}{6}$",
          "$\\frac{2}{3}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Một túi có 7 viên kẹo màu xanh và 5 viên kẹo màu đỏ. Lấy ngẫu nhiên 1 chiếc kẹo. Biến cố lấy được kẹo màu xanh có xác suất là:",
        "options": [
          "$\\frac{7}{12}$",
          "$\\frac{1}{2}$",
          "$\\frac{5}{10}$",
          "$\\frac{1}{5}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Rút ngẫu nhiên một lá bài trong bộ bài có 10 lá đánh số từ 1 đến 10. Xác suất rút được lá bài ghi số nguyên tố là:",
        "options": [
          "0,4",
          "0,5",
          "0,3",
          "0,2"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tung một đồng xu 20 lần thấy có 12 lần xuất hiện mặt Ngửa. Xác suất thực nghiệm xuất hiện mặt Ngửa là:",
        "options": [
          "0,6",
          "0,4",
          "0,5",
          "0,8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hội khỏe Phù Đổng trường có 17 đội bóng chuyền tham gia thi đấu loại trực tiếp bốc thăm ngẫu nhiên. Xác suất để đội lớp 7A gặp đội lớp 7B ngay ở trận đầu tiên là một biến cố:",
        "options": [
          "Ngẫu nhiên",
          "Chắc chắn",
          "Không thể",
          "Đồng khả năng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một hộp có 1 quả bóng xanh, 1 quả bóng đỏ, 1 quả bóng vàng. Bạn An lấy ra 1 quả rồi đặt lại vào hộp, sau đó bạn Bình lấy ra 1 quả. Số kết quả có thể xảy ra là:",
        "options": [
          "9",
          "3",
          "6",
          "8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Trong một hộp có 30 chiếc bút bi, trong đó có 5 chiếc bút màu đỏ, còn lại là màu xanh. Xác suất lấy được chiếc bút màu xanh là:",
        "options": [
          "0.83",
          "0,75",
          "0,5",
          "0,25"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm trên hai con xúc xắc bằng 11 là:",
        "options": [
          "$\\frac{2}{36} = \\frac{1}{18}$",
          "$\\frac{1}{36}$",
          "$\\frac{3}{36}$",
          "$\\frac{4}{36}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về biến cố (Đề 02):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Biến cố ngẫu nhiên là biến cố có thể xảy ra hoặc không xảy ra tùy thuộc vào kết quả của phép thử.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Xác suất của một biến cố là một con số nằm giữa 0 và 1 (kể cả 0 và 1).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Gieo một con xúc xắc 6 mặt thì xác suất ra mặt 1 chấm bằng xác suất ra mặt 6 chấm.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Nếu tung đồng xu 10 lần đều ra mặt Sấp thì chắc chắn lần thứ 11 sẽ ra mặt Ngửa.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Trong một hộp kín có 12 thẻ trắng và 10 thẻ đen có cùng kích thước và khối lượng (Mã đề 02):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hành động rút ngẫu nhiên 1 thẻ là một phép thử ngẫu nhiên.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng số kết quả có thể xảy ra khi rút 1 thẻ là 22.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Xác suất rút được thẻ đen là 10 / (22).",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Khả năng rút được thẻ đen luôn cao hơn rút được thẻ trắng với mọi t >= 1.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc 6 mặt. Tính xác suất xuất hiện mặt có số chấm là số lẻ.",
        "answer": "0.5",
        "acceptableAnswers": [
          "0.5"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.5**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một hộp có 8 bi xanh và 4 bi đỏ. Tính tổng số kết quả có thể xảy ra khi lấy ngẫu nhiên 1 viên bi.",
        "answer": "12",
        "acceptableAnswers": [
          "12"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **12**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tung một đồng xu 40 lần thấy xuất hiện mặt Ngửa 22 lần. Tính xác suất thực nghiệm xuất hiện mặt Sấp.",
        "answer": "0.45",
        "acceptableAnswers": [
          "0.45"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.45**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong hộp có 10 tấm thẻ đánh số từ 1 đến 10. Rút ngẫu nhiên 1 thẻ. Tính xác suất thẻ rút được ghi số lớn hơn 7.",
        "answer": "0.3",
        "acceptableAnswers": [
          "0.3"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.3**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một hộp đựng 7 tấm thẻ ghi số chẵn và 5 tấm thẻ ghi số lẻ. Rút ngẫu nhiên 1 tấm thẻ. Tính xác suất rút được thẻ ghi số chẵn và xác suất rút được thẻ ghi số lẻ.",
        "rubric": "Tổng số tấm thẻ trong hộp: (7) + 5 = 12 thẻ (0.25đ).\nSố kết quả thuận lợi rút thẻ số chẵn là 7 (0.25đ).\nXác suất rút thẻ chẵn: P(Chẵn) = (7) / (12) (0.25đ).\nXác suất rút thẻ lẻ: P(Lẻ) = 5 / (12) (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Trong một đợt kiểm tra chất lượng sản phẩm gồm 120 linh kiện điện tử, người ta phát hiện có 5 linh kiện bị lỗi. Hãy tính xác suất thực nghiệm một linh kiện bị lỗi và ước lượng nếu sản xuất 10 000 linh kiện thì có khoảng bao nhiêu linh kiện bị lỗi.",
        "rubric": "Xác suất thực nghiệm linh kiện bị lỗi: P = 5 / (120) (0.25đ).\nTỉ lệ lỗi thực nghiệm ước tính cho toàn bộ lô hàng (0.25đ).\nSố linh kiện lỗi dự đoán trong 10 000 linh kiện: N = 10 000 . P (0.25đ).\nTính toán và kết luận số linh kiện lỗi ước lượng (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một chiếc hộp có 3 quả bóng xanh và 2 quả bóng đỏ. Bạn Nam lấy ngẫu nhiên 1 quả bóng, xem màu rồi KHÔNG trả lại vào hộp. Sau đó bạn Bình lấy tiếp 1 quả bóng. Tính xác suất để cả hai bạn đều lấy được bóng màu xanh.",
        "rubric": "Xác suất bạn Nam lấy được quả bóng màu xanh lần thứ nhất là: 3/5 (0.25đ).\nSau khi Nam lấy 1 bóng xanh, trong hộp còn lại 4 quả bóng (gồm 2 xanh và 2 đỏ) (0.25đ).\nXác suất bạn Bình lấy được quả bóng màu xanh lần thứ hai là: 2/4 = 1/2 (0.25đ).\nXác suất để cả hai bạn cùng lấy được bóng xanh là: (3/5) . (1/2) = 3/10 = 0,3 (0.25đ)."
      }
    ]
  },
  "c8_7_bai3_test3": {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương VIII: Làm quen với biến cố và xác suất của biến cố - Đề số 03",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Biến cố chắc chắn là biến cố (Đề 03):",
        "options": [
          "Luôn xảy ra trong phép thử",
          "Không bao giờ xảy ra",
          "Có thể xảy ra hoặc không",
          "Có xác suất bằng 0"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Biến cố không thể là biến cố:",
        "options": [
          "Không bao giờ xảy ra trong phép thử",
          "Luôn luôn xảy ra",
          "Xảy ra với xác suất 1",
          "Xảy ra với xác suất 0,5"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Gieo một con xúc xắc 6 mặt cân đối thì biến cố nào sau đây là ngẫu nhiên?",
        "options": [
          "Xuất hiện mặt có số chấm là số chẵn",
          "Xuất hiện mặt 7 chấm",
          "Xuất hiện mặt có số chấm nhỏ hơn 10",
          "Xuất hiện mặt 0 chấm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Xác suất của biến cố chắc chắn bằng:",
        "options": [
          "1",
          "0",
          "0,5",
          "-1"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc cân đối. Xác suất xuất hiện mặt có số chấm chia hết cho 3 là:",
        "options": [
          "$\\frac{1}{3}$",
          "$\\frac{1}{2}$",
          "$\\frac{1}{6}$",
          "$\\frac{2}{3}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Một túi có 8 viên kẹo màu xanh và 5 viên kẹo màu đỏ. Lấy ngẫu nhiên 1 chiếc kẹo. Biến cố lấy được kẹo màu xanh có xác suất là:",
        "options": [
          "$\\frac{8}{13}$",
          "$\\frac{1}{2}$",
          "$\\frac{5}{10}$",
          "$\\frac{1}{5}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Rút ngẫu nhiên một lá bài trong bộ bài có 10 lá đánh số từ 1 đến 10. Xác suất rút được lá bài ghi số nguyên tố là:",
        "options": [
          "0,4",
          "0,5",
          "0,3",
          "0,2"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tung một đồng xu 20 lần thấy có 12 lần xuất hiện mặt Ngửa. Xác suất thực nghiệm xuất hiện mặt Ngửa là:",
        "options": [
          "0,6",
          "0,4",
          "0,5",
          "0,8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hội khỏe Phù Đổng trường có 18 đội bóng chuyền tham gia thi đấu loại trực tiếp bốc thăm ngẫu nhiên. Xác suất để đội lớp 7A gặp đội lớp 7B ngay ở trận đầu tiên là một biến cố:",
        "options": [
          "Ngẫu nhiên",
          "Chắc chắn",
          "Không thể",
          "Đồng khả năng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một hộp có 1 quả bóng xanh, 1 quả bóng đỏ, 1 quả bóng vàng. Bạn An lấy ra 1 quả rồi đặt lại vào hộp, sau đó bạn Bình lấy ra 1 quả. Số kết quả có thể xảy ra là:",
        "options": [
          "9",
          "3",
          "6",
          "8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Trong một hộp có 35 chiếc bút bi, trong đó có 5 chiếc bút màu đỏ, còn lại là màu xanh. Xác suất lấy được chiếc bút màu xanh là:",
        "options": [
          "0.86",
          "0,75",
          "0,5",
          "0,25"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm trên hai con xúc xắc bằng 11 là:",
        "options": [
          "$\\frac{2}{36} = \\frac{1}{18}$",
          "$\\frac{1}{36}$",
          "$\\frac{3}{36}$",
          "$\\frac{4}{36}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về biến cố (Đề 03):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Biến cố ngẫu nhiên là biến cố có thể xảy ra hoặc không xảy ra tùy thuộc vào kết quả của phép thử.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Xác suất của một biến cố là một con số nằm giữa 0 và 1 (kể cả 0 và 1).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Gieo một con xúc xắc 6 mặt thì xác suất ra mặt 1 chấm bằng xác suất ra mặt 6 chấm.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Nếu tung đồng xu 10 lần đều ra mặt Sấp thì chắc chắn lần thứ 11 sẽ ra mặt Ngửa.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Trong một hộp kín có 13 thẻ trắng và 10 thẻ đen có cùng kích thước và khối lượng (Mã đề 03):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hành động rút ngẫu nhiên 1 thẻ là một phép thử ngẫu nhiên.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng số kết quả có thể xảy ra khi rút 1 thẻ là 23.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Xác suất rút được thẻ đen là 10 / (23).",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Khả năng rút được thẻ đen luôn cao hơn rút được thẻ trắng với mọi t >= 1.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc 6 mặt. Tính xác suất xuất hiện mặt có số chấm là số lẻ.",
        "answer": "0.5",
        "acceptableAnswers": [
          "0.5"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.5**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một hộp có 9 bi xanh và 4 bi đỏ. Tính tổng số kết quả có thể xảy ra khi lấy ngẫu nhiên 1 viên bi.",
        "answer": "13",
        "acceptableAnswers": [
          "13"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **13**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tung một đồng xu 40 lần thấy xuất hiện mặt Ngửa 22 lần. Tính xác suất thực nghiệm xuất hiện mặt Sấp.",
        "answer": "0.45",
        "acceptableAnswers": [
          "0.45"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.45**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong hộp có 10 tấm thẻ đánh số từ 1 đến 10. Rút ngẫu nhiên 1 thẻ. Tính xác suất thẻ rút được ghi số lớn hơn 7.",
        "answer": "0.3",
        "acceptableAnswers": [
          "0.3"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.3**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một hộp đựng 8 tấm thẻ ghi số chẵn và 5 tấm thẻ ghi số lẻ. Rút ngẫu nhiên 1 tấm thẻ. Tính xác suất rút được thẻ ghi số chẵn và xác suất rút được thẻ ghi số lẻ.",
        "rubric": "Tổng số tấm thẻ trong hộp: (8) + 5 = 13 thẻ (0.25đ).\nSố kết quả thuận lợi rút thẻ số chẵn là 8 (0.25đ).\nXác suất rút thẻ chẵn: P(Chẵn) = (8) / (13) (0.25đ).\nXác suất rút thẻ lẻ: P(Lẻ) = 5 / (13) (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Trong một đợt kiểm tra chất lượng sản phẩm gồm 130 linh kiện điện tử, người ta phát hiện có 5 linh kiện bị lỗi. Hãy tính xác suất thực nghiệm một linh kiện bị lỗi và ước lượng nếu sản xuất 10 000 linh kiện thì có khoảng bao nhiêu linh kiện bị lỗi.",
        "rubric": "Xác suất thực nghiệm linh kiện bị lỗi: P = 5 / (130) (0.25đ).\nTỉ lệ lỗi thực nghiệm ước tính cho toàn bộ lô hàng (0.25đ).\nSố linh kiện lỗi dự đoán trong 10 000 linh kiện: N = 10 000 . P (0.25đ).\nTính toán và kết luận số linh kiện lỗi ước lượng (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một chiếc hộp có 3 quả bóng xanh và 2 quả bóng đỏ. Bạn Nam lấy ngẫu nhiên 1 quả bóng, xem màu rồi KHÔNG trả lại vào hộp. Sau đó bạn Bình lấy tiếp 1 quả bóng. Tính xác suất để cả hai bạn đều lấy được bóng màu xanh.",
        "rubric": "Xác suất bạn Nam lấy được quả bóng màu xanh lần thứ nhất là: 3/5 (0.25đ).\nSau khi Nam lấy 1 bóng xanh, trong hộp còn lại 4 quả bóng (gồm 2 xanh và 2 đỏ) (0.25đ).\nXác suất bạn Bình lấy được quả bóng màu xanh lần thứ hai là: 2/4 = 1/2 (0.25đ).\nXác suất để cả hai bạn cùng lấy được bóng xanh là: (3/5) . (1/2) = 3/10 = 0,3 (0.25đ)."
      }
    ]
  },
  "c8_7_bai3_test4": {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương VIII: Làm quen với biến cố và xác suất của biến cố - Đề số 04",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Biến cố chắc chắn là biến cố (Đề 04):",
        "options": [
          "Luôn xảy ra trong phép thử",
          "Không bao giờ xảy ra",
          "Có thể xảy ra hoặc không",
          "Có xác suất bằng 0"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Biến cố không thể là biến cố:",
        "options": [
          "Không bao giờ xảy ra trong phép thử",
          "Luôn luôn xảy ra",
          "Xảy ra với xác suất 1",
          "Xảy ra với xác suất 0,5"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Gieo một con xúc xắc 6 mặt cân đối thì biến cố nào sau đây là ngẫu nhiên?",
        "options": [
          "Xuất hiện mặt có số chấm là số chẵn",
          "Xuất hiện mặt 7 chấm",
          "Xuất hiện mặt có số chấm nhỏ hơn 10",
          "Xuất hiện mặt 0 chấm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Xác suất của biến cố chắc chắn bằng:",
        "options": [
          "1",
          "0",
          "0,5",
          "-1"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc cân đối. Xác suất xuất hiện mặt có số chấm chia hết cho 3 là:",
        "options": [
          "$\\frac{1}{3}$",
          "$\\frac{1}{2}$",
          "$\\frac{1}{6}$",
          "$\\frac{2}{3}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Một túi có 9 viên kẹo màu xanh và 5 viên kẹo màu đỏ. Lấy ngẫu nhiên 1 chiếc kẹo. Biến cố lấy được kẹo màu xanh có xác suất là:",
        "options": [
          "$\\frac{9}{14}$",
          "$\\frac{1}{2}$",
          "$\\frac{5}{10}$",
          "$\\frac{1}{5}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Rút ngẫu nhiên một lá bài trong bộ bài có 10 lá đánh số từ 1 đến 10. Xác suất rút được lá bài ghi số nguyên tố là:",
        "options": [
          "0,4",
          "0,5",
          "0,3",
          "0,2"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tung một đồng xu 20 lần thấy có 12 lần xuất hiện mặt Ngửa. Xác suất thực nghiệm xuất hiện mặt Ngửa là:",
        "options": [
          "0,6",
          "0,4",
          "0,5",
          "0,8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hội khỏe Phù Đổng trường có 19 đội bóng chuyền tham gia thi đấu loại trực tiếp bốc thăm ngẫu nhiên. Xác suất để đội lớp 7A gặp đội lớp 7B ngay ở trận đầu tiên là một biến cố:",
        "options": [
          "Ngẫu nhiên",
          "Chắc chắn",
          "Không thể",
          "Đồng khả năng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một hộp có 1 quả bóng xanh, 1 quả bóng đỏ, 1 quả bóng vàng. Bạn An lấy ra 1 quả rồi đặt lại vào hộp, sau đó bạn Bình lấy ra 1 quả. Số kết quả có thể xảy ra là:",
        "options": [
          "9",
          "3",
          "6",
          "8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Trong một hộp có 40 chiếc bút bi, trong đó có 5 chiếc bút màu đỏ, còn lại là màu xanh. Xác suất lấy được chiếc bút màu xanh là:",
        "options": [
          "0.88",
          "0,75",
          "0,5",
          "0,25"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm trên hai con xúc xắc bằng 11 là:",
        "options": [
          "$\\frac{2}{36} = \\frac{1}{18}$",
          "$\\frac{1}{36}$",
          "$\\frac{3}{36}$",
          "$\\frac{4}{36}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về biến cố (Đề 04):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Biến cố ngẫu nhiên là biến cố có thể xảy ra hoặc không xảy ra tùy thuộc vào kết quả của phép thử.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Xác suất của một biến cố là một con số nằm giữa 0 và 1 (kể cả 0 và 1).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Gieo một con xúc xắc 6 mặt thì xác suất ra mặt 1 chấm bằng xác suất ra mặt 6 chấm.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Nếu tung đồng xu 10 lần đều ra mặt Sấp thì chắc chắn lần thứ 11 sẽ ra mặt Ngửa.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Trong một hộp kín có 14 thẻ trắng và 10 thẻ đen có cùng kích thước và khối lượng (Mã đề 04):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hành động rút ngẫu nhiên 1 thẻ là một phép thử ngẫu nhiên.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng số kết quả có thể xảy ra khi rút 1 thẻ là 24.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Xác suất rút được thẻ đen là 10 / (24).",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Khả năng rút được thẻ đen luôn cao hơn rút được thẻ trắng với mọi t >= 1.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc 6 mặt. Tính xác suất xuất hiện mặt có số chấm là số lẻ.",
        "answer": "0.5",
        "acceptableAnswers": [
          "0.5"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.5**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một hộp có 10 bi xanh và 4 bi đỏ. Tính tổng số kết quả có thể xảy ra khi lấy ngẫu nhiên 1 viên bi.",
        "answer": "14",
        "acceptableAnswers": [
          "14"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **14**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tung một đồng xu 40 lần thấy xuất hiện mặt Ngửa 22 lần. Tính xác suất thực nghiệm xuất hiện mặt Sấp.",
        "answer": "0.45",
        "acceptableAnswers": [
          "0.45"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.45**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong hộp có 10 tấm thẻ đánh số từ 1 đến 10. Rút ngẫu nhiên 1 thẻ. Tính xác suất thẻ rút được ghi số lớn hơn 7.",
        "answer": "0.3",
        "acceptableAnswers": [
          "0.3"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.3**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một hộp đựng 9 tấm thẻ ghi số chẵn và 5 tấm thẻ ghi số lẻ. Rút ngẫu nhiên 1 tấm thẻ. Tính xác suất rút được thẻ ghi số chẵn và xác suất rút được thẻ ghi số lẻ.",
        "rubric": "Tổng số tấm thẻ trong hộp: (9) + 5 = 14 thẻ (0.25đ).\nSố kết quả thuận lợi rút thẻ số chẵn là 9 (0.25đ).\nXác suất rút thẻ chẵn: P(Chẵn) = (9) / (14) (0.25đ).\nXác suất rút thẻ lẻ: P(Lẻ) = 5 / (14) (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Trong một đợt kiểm tra chất lượng sản phẩm gồm 140 linh kiện điện tử, người ta phát hiện có 5 linh kiện bị lỗi. Hãy tính xác suất thực nghiệm một linh kiện bị lỗi và ước lượng nếu sản xuất 10 000 linh kiện thì có khoảng bao nhiêu linh kiện bị lỗi.",
        "rubric": "Xác suất thực nghiệm linh kiện bị lỗi: P = 5 / (140) (0.25đ).\nTỉ lệ lỗi thực nghiệm ước tính cho toàn bộ lô hàng (0.25đ).\nSố linh kiện lỗi dự đoán trong 10 000 linh kiện: N = 10 000 . P (0.25đ).\nTính toán và kết luận số linh kiện lỗi ước lượng (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một chiếc hộp có 3 quả bóng xanh và 2 quả bóng đỏ. Bạn Nam lấy ngẫu nhiên 1 quả bóng, xem màu rồi KHÔNG trả lại vào hộp. Sau đó bạn Bình lấy tiếp 1 quả bóng. Tính xác suất để cả hai bạn đều lấy được bóng màu xanh.",
        "rubric": "Xác suất bạn Nam lấy được quả bóng màu xanh lần thứ nhất là: 3/5 (0.25đ).\nSau khi Nam lấy 1 bóng xanh, trong hộp còn lại 4 quả bóng (gồm 2 xanh và 2 đỏ) (0.25đ).\nXác suất bạn Bình lấy được quả bóng màu xanh lần thứ hai là: 2/4 = 1/2 (0.25đ).\nXác suất để cả hai bạn cùng lấy được bóng xanh là: (3/5) . (1/2) = 3/10 = 0,3 (0.25đ)."
      }
    ]
  },
  "c8_7_bai3_test5": {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương VIII: Làm quen với biến cố và xác suất của biến cố - Đề số 05",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Biến cố chắc chắn là biến cố (Đề 05):",
        "options": [
          "Luôn xảy ra trong phép thử",
          "Không bao giờ xảy ra",
          "Có thể xảy ra hoặc không",
          "Có xác suất bằng 0"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Biến cố không thể là biến cố:",
        "options": [
          "Không bao giờ xảy ra trong phép thử",
          "Luôn luôn xảy ra",
          "Xảy ra với xác suất 1",
          "Xảy ra với xác suất 0,5"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Gieo một con xúc xắc 6 mặt cân đối thì biến cố nào sau đây là ngẫu nhiên?",
        "options": [
          "Xuất hiện mặt có số chấm là số chẵn",
          "Xuất hiện mặt 7 chấm",
          "Xuất hiện mặt có số chấm nhỏ hơn 10",
          "Xuất hiện mặt 0 chấm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Xác suất của biến cố chắc chắn bằng:",
        "options": [
          "1",
          "0",
          "0,5",
          "-1"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc cân đối. Xác suất xuất hiện mặt có số chấm chia hết cho 3 là:",
        "options": [
          "$\\frac{1}{3}$",
          "$\\frac{1}{2}$",
          "$\\frac{1}{6}$",
          "$\\frac{2}{3}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Một túi có 10 viên kẹo màu xanh và 5 viên kẹo màu đỏ. Lấy ngẫu nhiên 1 chiếc kẹo. Biến cố lấy được kẹo màu xanh có xác suất là:",
        "options": [
          "$\\frac{10}{15}$",
          "$\\frac{1}{2}$",
          "$\\frac{5}{10}$",
          "$\\frac{1}{5}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Rút ngẫu nhiên một lá bài trong bộ bài có 10 lá đánh số từ 1 đến 10. Xác suất rút được lá bài ghi số nguyên tố là:",
        "options": [
          "0,4",
          "0,5",
          "0,3",
          "0,2"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tung một đồng xu 20 lần thấy có 12 lần xuất hiện mặt Ngửa. Xác suất thực nghiệm xuất hiện mặt Ngửa là:",
        "options": [
          "0,6",
          "0,4",
          "0,5",
          "0,8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hội khỏe Phù Đổng trường có 20 đội bóng chuyền tham gia thi đấu loại trực tiếp bốc thăm ngẫu nhiên. Xác suất để đội lớp 7A gặp đội lớp 7B ngay ở trận đầu tiên là một biến cố:",
        "options": [
          "Ngẫu nhiên",
          "Chắc chắn",
          "Không thể",
          "Đồng khả năng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một hộp có 1 quả bóng xanh, 1 quả bóng đỏ, 1 quả bóng vàng. Bạn An lấy ra 1 quả rồi đặt lại vào hộp, sau đó bạn Bình lấy ra 1 quả. Số kết quả có thể xảy ra là:",
        "options": [
          "9",
          "3",
          "6",
          "8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Trong một hộp có 45 chiếc bút bi, trong đó có 5 chiếc bút màu đỏ, còn lại là màu xanh. Xác suất lấy được chiếc bút màu xanh là:",
        "options": [
          "0.89",
          "0,75",
          "0,5",
          "0,25"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm trên hai con xúc xắc bằng 11 là:",
        "options": [
          "$\\frac{2}{36} = \\frac{1}{18}$",
          "$\\frac{1}{36}$",
          "$\\frac{3}{36}$",
          "$\\frac{4}{36}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về biến cố (Đề 05):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Biến cố ngẫu nhiên là biến cố có thể xảy ra hoặc không xảy ra tùy thuộc vào kết quả của phép thử.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Xác suất của một biến cố là một con số nằm giữa 0 và 1 (kể cả 0 và 1).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Gieo một con xúc xắc 6 mặt thì xác suất ra mặt 1 chấm bằng xác suất ra mặt 6 chấm.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Nếu tung đồng xu 10 lần đều ra mặt Sấp thì chắc chắn lần thứ 11 sẽ ra mặt Ngửa.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Trong một hộp kín có 15 thẻ trắng và 10 thẻ đen có cùng kích thước và khối lượng (Mã đề 05):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hành động rút ngẫu nhiên 1 thẻ là một phép thử ngẫu nhiên.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng số kết quả có thể xảy ra khi rút 1 thẻ là 25.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Xác suất rút được thẻ đen là 10 / (25).",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Khả năng rút được thẻ đen luôn cao hơn rút được thẻ trắng với mọi t >= 1.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc 6 mặt. Tính xác suất xuất hiện mặt có số chấm là số lẻ.",
        "answer": "0.5",
        "acceptableAnswers": [
          "0.5"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.5**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một hộp có 11 bi xanh và 4 bi đỏ. Tính tổng số kết quả có thể xảy ra khi lấy ngẫu nhiên 1 viên bi.",
        "answer": "15",
        "acceptableAnswers": [
          "15"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **15**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tung một đồng xu 40 lần thấy xuất hiện mặt Ngửa 22 lần. Tính xác suất thực nghiệm xuất hiện mặt Sấp.",
        "answer": "0.45",
        "acceptableAnswers": [
          "0.45"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.45**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong hộp có 10 tấm thẻ đánh số từ 1 đến 10. Rút ngẫu nhiên 1 thẻ. Tính xác suất thẻ rút được ghi số lớn hơn 7.",
        "answer": "0.3",
        "acceptableAnswers": [
          "0.3"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.3**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một hộp đựng 10 tấm thẻ ghi số chẵn và 5 tấm thẻ ghi số lẻ. Rút ngẫu nhiên 1 tấm thẻ. Tính xác suất rút được thẻ ghi số chẵn và xác suất rút được thẻ ghi số lẻ.",
        "rubric": "Tổng số tấm thẻ trong hộp: (10) + 5 = 15 thẻ (0.25đ).\nSố kết quả thuận lợi rút thẻ số chẵn là 10 (0.25đ).\nXác suất rút thẻ chẵn: P(Chẵn) = (10) / (15) (0.25đ).\nXác suất rút thẻ lẻ: P(Lẻ) = 5 / (15) (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Trong một đợt kiểm tra chất lượng sản phẩm gồm 150 linh kiện điện tử, người ta phát hiện có 5 linh kiện bị lỗi. Hãy tính xác suất thực nghiệm một linh kiện bị lỗi và ước lượng nếu sản xuất 10 000 linh kiện thì có khoảng bao nhiêu linh kiện bị lỗi.",
        "rubric": "Xác suất thực nghiệm linh kiện bị lỗi: P = 5 / (150) (0.25đ).\nTỉ lệ lỗi thực nghiệm ước tính cho toàn bộ lô hàng (0.25đ).\nSố linh kiện lỗi dự đoán trong 10 000 linh kiện: N = 10 000 . P (0.25đ).\nTính toán và kết luận số linh kiện lỗi ước lượng (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một chiếc hộp có 3 quả bóng xanh và 2 quả bóng đỏ. Bạn Nam lấy ngẫu nhiên 1 quả bóng, xem màu rồi KHÔNG trả lại vào hộp. Sau đó bạn Bình lấy tiếp 1 quả bóng. Tính xác suất để cả hai bạn đều lấy được bóng màu xanh.",
        "rubric": "Xác suất bạn Nam lấy được quả bóng màu xanh lần thứ nhất là: 3/5 (0.25đ).\nSau khi Nam lấy 1 bóng xanh, trong hộp còn lại 4 quả bóng (gồm 2 xanh và 2 đỏ) (0.25đ).\nXác suất bạn Bình lấy được quả bóng màu xanh lần thứ hai là: 2/4 = 1/2 (0.25đ).\nXác suất để cả hai bạn cùng lấy được bóng xanh là: (3/5) . (1/2) = 3/10 = 0,3 (0.25đ)."
      }
    ]
  },
  "c8_7_bai3_test6": {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương VIII: Làm quen với biến cố và xác suất của biến cố - Đề số 06",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Biến cố chắc chắn là biến cố (Đề 06):",
        "options": [
          "Luôn xảy ra trong phép thử",
          "Không bao giờ xảy ra",
          "Có thể xảy ra hoặc không",
          "Có xác suất bằng 0"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Biến cố không thể là biến cố:",
        "options": [
          "Không bao giờ xảy ra trong phép thử",
          "Luôn luôn xảy ra",
          "Xảy ra với xác suất 1",
          "Xảy ra với xác suất 0,5"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Gieo một con xúc xắc 6 mặt cân đối thì biến cố nào sau đây là ngẫu nhiên?",
        "options": [
          "Xuất hiện mặt có số chấm là số chẵn",
          "Xuất hiện mặt 7 chấm",
          "Xuất hiện mặt có số chấm nhỏ hơn 10",
          "Xuất hiện mặt 0 chấm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Xác suất của biến cố chắc chắn bằng:",
        "options": [
          "1",
          "0",
          "0,5",
          "-1"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc cân đối. Xác suất xuất hiện mặt có số chấm chia hết cho 3 là:",
        "options": [
          "$\\frac{1}{3}$",
          "$\\frac{1}{2}$",
          "$\\frac{1}{6}$",
          "$\\frac{2}{3}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Một túi có 11 viên kẹo màu xanh và 5 viên kẹo màu đỏ. Lấy ngẫu nhiên 1 chiếc kẹo. Biến cố lấy được kẹo màu xanh có xác suất là:",
        "options": [
          "$\\frac{11}{16}$",
          "$\\frac{1}{2}$",
          "$\\frac{5}{10}$",
          "$\\frac{1}{5}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Rút ngẫu nhiên một lá bài trong bộ bài có 10 lá đánh số từ 1 đến 10. Xác suất rút được lá bài ghi số nguyên tố là:",
        "options": [
          "0,4",
          "0,5",
          "0,3",
          "0,2"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tung một đồng xu 20 lần thấy có 12 lần xuất hiện mặt Ngửa. Xác suất thực nghiệm xuất hiện mặt Ngửa là:",
        "options": [
          "0,6",
          "0,4",
          "0,5",
          "0,8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hội khỏe Phù Đổng trường có 21 đội bóng chuyền tham gia thi đấu loại trực tiếp bốc thăm ngẫu nhiên. Xác suất để đội lớp 7A gặp đội lớp 7B ngay ở trận đầu tiên là một biến cố:",
        "options": [
          "Ngẫu nhiên",
          "Chắc chắn",
          "Không thể",
          "Đồng khả năng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một hộp có 1 quả bóng xanh, 1 quả bóng đỏ, 1 quả bóng vàng. Bạn An lấy ra 1 quả rồi đặt lại vào hộp, sau đó bạn Bình lấy ra 1 quả. Số kết quả có thể xảy ra là:",
        "options": [
          "9",
          "3",
          "6",
          "8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Trong một hộp có 50 chiếc bút bi, trong đó có 5 chiếc bút màu đỏ, còn lại là màu xanh. Xác suất lấy được chiếc bút màu xanh là:",
        "options": [
          "0.90",
          "0,75",
          "0,5",
          "0,25"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm trên hai con xúc xắc bằng 11 là:",
        "options": [
          "$\\frac{2}{36} = \\frac{1}{18}$",
          "$\\frac{1}{36}$",
          "$\\frac{3}{36}$",
          "$\\frac{4}{36}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về biến cố (Đề 06):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Biến cố ngẫu nhiên là biến cố có thể xảy ra hoặc không xảy ra tùy thuộc vào kết quả của phép thử.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Xác suất của một biến cố là một con số nằm giữa 0 và 1 (kể cả 0 và 1).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Gieo một con xúc xắc 6 mặt thì xác suất ra mặt 1 chấm bằng xác suất ra mặt 6 chấm.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Nếu tung đồng xu 10 lần đều ra mặt Sấp thì chắc chắn lần thứ 11 sẽ ra mặt Ngửa.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Trong một hộp kín có 16 thẻ trắng và 10 thẻ đen có cùng kích thước và khối lượng (Mã đề 06):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hành động rút ngẫu nhiên 1 thẻ là một phép thử ngẫu nhiên.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng số kết quả có thể xảy ra khi rút 1 thẻ là 26.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Xác suất rút được thẻ đen là 10 / (26).",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Khả năng rút được thẻ đen luôn cao hơn rút được thẻ trắng với mọi t >= 1.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc 6 mặt. Tính xác suất xuất hiện mặt có số chấm là số lẻ.",
        "answer": "0.5",
        "acceptableAnswers": [
          "0.5"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.5**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một hộp có 12 bi xanh và 4 bi đỏ. Tính tổng số kết quả có thể xảy ra khi lấy ngẫu nhiên 1 viên bi.",
        "answer": "16",
        "acceptableAnswers": [
          "16"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **16**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tung một đồng xu 40 lần thấy xuất hiện mặt Ngửa 22 lần. Tính xác suất thực nghiệm xuất hiện mặt Sấp.",
        "answer": "0.45",
        "acceptableAnswers": [
          "0.45"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.45**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong hộp có 10 tấm thẻ đánh số từ 1 đến 10. Rút ngẫu nhiên 1 thẻ. Tính xác suất thẻ rút được ghi số lớn hơn 7.",
        "answer": "0.3",
        "acceptableAnswers": [
          "0.3"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.3**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một hộp đựng 11 tấm thẻ ghi số chẵn và 5 tấm thẻ ghi số lẻ. Rút ngẫu nhiên 1 tấm thẻ. Tính xác suất rút được thẻ ghi số chẵn và xác suất rút được thẻ ghi số lẻ.",
        "rubric": "Tổng số tấm thẻ trong hộp: (11) + 5 = 16 thẻ (0.25đ).\nSố kết quả thuận lợi rút thẻ số chẵn là 11 (0.25đ).\nXác suất rút thẻ chẵn: P(Chẵn) = (11) / (16) (0.25đ).\nXác suất rút thẻ lẻ: P(Lẻ) = 5 / (16) (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Trong một đợt kiểm tra chất lượng sản phẩm gồm 160 linh kiện điện tử, người ta phát hiện có 5 linh kiện bị lỗi. Hãy tính xác suất thực nghiệm một linh kiện bị lỗi và ước lượng nếu sản xuất 10 000 linh kiện thì có khoảng bao nhiêu linh kiện bị lỗi.",
        "rubric": "Xác suất thực nghiệm linh kiện bị lỗi: P = 5 / (160) (0.25đ).\nTỉ lệ lỗi thực nghiệm ước tính cho toàn bộ lô hàng (0.25đ).\nSố linh kiện lỗi dự đoán trong 10 000 linh kiện: N = 10 000 . P (0.25đ).\nTính toán và kết luận số linh kiện lỗi ước lượng (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một chiếc hộp có 3 quả bóng xanh và 2 quả bóng đỏ. Bạn Nam lấy ngẫu nhiên 1 quả bóng, xem màu rồi KHÔNG trả lại vào hộp. Sau đó bạn Bình lấy tiếp 1 quả bóng. Tính xác suất để cả hai bạn đều lấy được bóng màu xanh.",
        "rubric": "Xác suất bạn Nam lấy được quả bóng màu xanh lần thứ nhất là: 3/5 (0.25đ).\nSau khi Nam lấy 1 bóng xanh, trong hộp còn lại 4 quả bóng (gồm 2 xanh và 2 đỏ) (0.25đ).\nXác suất bạn Bình lấy được quả bóng màu xanh lần thứ hai là: 2/4 = 1/2 (0.25đ).\nXác suất để cả hai bạn cùng lấy được bóng xanh là: (3/5) . (1/2) = 3/10 = 0,3 (0.25đ)."
      }
    ]
  },
  "c8_7_bai3_test7": {
    "title": "Toán 7 (KNTT) - Bài kiểm tra cuối Chương VIII: Làm quen với biến cố và xác suất của biến cố - Đề số 07",
    "duration": "90 phút",
    "totalScore": 10.0,
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Biến cố chắc chắn là biến cố (Đề 07):",
        "options": [
          "Luôn xảy ra trong phép thử",
          "Không bao giờ xảy ra",
          "Có thể xảy ra hoặc không",
          "Có xác suất bằng 0"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Biến cố không thể là biến cố:",
        "options": [
          "Không bao giờ xảy ra trong phép thử",
          "Luôn luôn xảy ra",
          "Xảy ra với xác suất 1",
          "Xảy ra với xác suất 0,5"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Gieo một con xúc xắc 6 mặt cân đối thì biến cố nào sau đây là ngẫu nhiên?",
        "options": [
          "Xuất hiện mặt có số chấm là số chẵn",
          "Xuất hiện mặt 7 chấm",
          "Xuất hiện mặt có số chấm nhỏ hơn 10",
          "Xuất hiện mặt 0 chấm"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Xác suất của biến cố chắc chắn bằng:",
        "options": [
          "1",
          "0",
          "0,5",
          "-1"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc cân đối. Xác suất xuất hiện mặt có số chấm chia hết cho 3 là:",
        "options": [
          "$\\frac{1}{3}$",
          "$\\frac{1}{2}$",
          "$\\frac{1}{6}$",
          "$\\frac{2}{3}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Một túi có 12 viên kẹo màu xanh và 5 viên kẹo màu đỏ. Lấy ngẫu nhiên 1 chiếc kẹo. Biến cố lấy được kẹo màu xanh có xác suất là:",
        "options": [
          "$\\frac{12}{17}$",
          "$\\frac{1}{2}$",
          "$\\frac{5}{10}$",
          "$\\frac{1}{5}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Rút ngẫu nhiên một lá bài trong bộ bài có 10 lá đánh số từ 1 đến 10. Xác suất rút được lá bài ghi số nguyên tố là:",
        "options": [
          "0,4",
          "0,5",
          "0,3",
          "0,2"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tung một đồng xu 20 lần thấy có 12 lần xuất hiện mặt Ngửa. Xác suất thực nghiệm xuất hiện mặt Ngửa là:",
        "options": [
          "0,6",
          "0,4",
          "0,5",
          "0,8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hội khỏe Phù Đổng trường có 22 đội bóng chuyền tham gia thi đấu loại trực tiếp bốc thăm ngẫu nhiên. Xác suất để đội lớp 7A gặp đội lớp 7B ngay ở trận đầu tiên là một biến cố:",
        "options": [
          "Ngẫu nhiên",
          "Chắc chắn",
          "Không thể",
          "Đồng khả năng"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một hộp có 1 quả bóng xanh, 1 quả bóng đỏ, 1 quả bóng vàng. Bạn An lấy ra 1 quả rồi đặt lại vào hộp, sau đó bạn Bình lấy ra 1 quả. Số kết quả có thể xảy ra là:",
        "options": [
          "9",
          "3",
          "6",
          "8"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Trong một hộp có 55 chiếc bút bi, trong đó có 5 chiếc bút màu đỏ, còn lại là màu xanh. Xác suất lấy được chiếc bút màu xanh là:",
        "options": [
          "0.91",
          "0,75",
          "0,5",
          "0,25"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Gieo đồng thời hai con xúc xắc cân đối. Xác suất để tổng số chấm trên hai con xúc xắc bằng 11 là:",
        "options": [
          "$\\frac{2}{36} = \\frac{1}{18}$",
          "$\\frac{1}{36}$",
          "$\\frac{3}{36}$",
          "$\\frac{4}{36}$"
        ],
        "correct": 0,
        "explanation": "Phương án đúng là **A**. Căn cứ vào định nghĩa và tính chất của bài học."
      }
    ],
    "part2": [
      {
        "id": 1,
        "stem": "Xét tính đúng sai về biến cố (Đề 07):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Biến cố ngẫu nhiên là biến cố có thể xảy ra hoặc không xảy ra tùy thuộc vào kết quả của phép thử.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Xác suất của một biến cố là một con số nằm giữa 0 và 1 (kể cả 0 và 1).",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Gieo một con xúc xắc 6 mặt thì xác suất ra mặt 1 chấm bằng xác suất ra mặt 6 chấm.",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Nếu tung đồng xu 10 lần đều ra mặt Sấp thì chắc chắn lần thứ 11 sẽ ra mặt Ngửa.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      },
      {
        "id": 2,
        "stem": "Trong một hộp kín có 17 thẻ trắng và 10 thẻ đen có cùng kích thước và khối lượng (Mã đề 07):",
        "statements": [
          {
            "key": "a",
            "level": "Nhận biết",
            "text": "Hành động rút ngẫu nhiên 1 thẻ là một phép thử ngẫu nhiên.",
            "correct": true,
            "explanation": "Ý A là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "b",
            "level": "Thông hiểu",
            "text": "Tổng số kết quả có thể xảy ra khi rút 1 thẻ là 27.",
            "correct": true,
            "explanation": "Ý B là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "c",
            "level": "Thông hiểu",
            "text": "Xác suất rút được thẻ đen là 10 / (27).",
            "correct": true,
            "explanation": "Ý C là **Đúng** theo quy tắc và tính chất bài học."
          },
          {
            "key": "d",
            "level": "Vận dụng",
            "text": "Khả năng rút được thẻ đen luôn cao hơn rút được thẻ trắng với mọi t >= 1.",
            "correct": false,
            "explanation": "Ý D là **Sai** theo quy tắc và tính chất bài học."
          }
        ]
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Gieo một con xúc xắc 6 mặt. Tính xác suất xuất hiện mặt có số chấm là số lẻ.",
        "answer": "0.5",
        "acceptableAnswers": [
          "0.5"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.5**."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một hộp có 13 bi xanh và 4 bi đỏ. Tính tổng số kết quả có thể xảy ra khi lấy ngẫu nhiên 1 viên bi.",
        "answer": "17",
        "acceptableAnswers": [
          "17"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **17**."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Tung một đồng xu 40 lần thấy xuất hiện mặt Ngửa 22 lần. Tính xác suất thực nghiệm xuất hiện mặt Sấp.",
        "answer": "0.45",
        "acceptableAnswers": [
          "0.45"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.45**."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong hộp có 10 tấm thẻ đánh số từ 1 đến 10. Rút ngẫu nhiên 1 thẻ. Tính xác suất thẻ rút được ghi số lớn hơn 7.",
        "answer": "0.3",
        "acceptableAnswers": [
          "0.3"
        ],
        "explanation": "Các bước giải chi tiết dẫn đến kết quả: **0.3**."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Một hộp đựng 12 tấm thẻ ghi số chẵn và 5 tấm thẻ ghi số lẻ. Rút ngẫu nhiên 1 tấm thẻ. Tính xác suất rút được thẻ ghi số chẵn và xác suất rút được thẻ ghi số lẻ.",
        "rubric": "Tổng số tấm thẻ trong hộp: (12) + 5 = 17 thẻ (0.25đ).\nSố kết quả thuận lợi rút thẻ số chẵn là 12 (0.25đ).\nXác suất rút thẻ chẵn: P(Chẵn) = (12) / (17) (0.25đ).\nXác suất rút thẻ lẻ: P(Lẻ) = 5 / (17) (0.25đ)."
      },
      {
        "id": 2,
        "level": "Vận dụng",
        "question": "Trong một đợt kiểm tra chất lượng sản phẩm gồm 170 linh kiện điện tử, người ta phát hiện có 5 linh kiện bị lỗi. Hãy tính xác suất thực nghiệm một linh kiện bị lỗi và ước lượng nếu sản xuất 10 000 linh kiện thì có khoảng bao nhiêu linh kiện bị lỗi.",
        "rubric": "Xác suất thực nghiệm linh kiện bị lỗi: P = 5 / (170) (0.25đ).\nTỉ lệ lỗi thực nghiệm ước tính cho toàn bộ lô hàng (0.25đ).\nSố linh kiện lỗi dự đoán trong 10 000 linh kiện: N = 10 000 . P (0.25đ).\nTính toán và kết luận số linh kiện lỗi ước lượng (0.25đ)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một chiếc hộp có 3 quả bóng xanh và 2 quả bóng đỏ. Bạn Nam lấy ngẫu nhiên 1 quả bóng, xem màu rồi KHÔNG trả lại vào hộp. Sau đó bạn Bình lấy tiếp 1 quả bóng. Tính xác suất để cả hai bạn đều lấy được bóng màu xanh.",
        "rubric": "Xác suất bạn Nam lấy được quả bóng màu xanh lần thứ nhất là: 3/5 (0.25đ).\nSau khi Nam lấy 1 bóng xanh, trong hộp còn lại 4 quả bóng (gồm 2 xanh và 2 đỏ) (0.25đ).\nXác suất bạn Bình lấy được quả bóng màu xanh lần thứ hai là: 2/4 = 1/2 (0.25đ).\nXác suất để cả hai bạn cùng lấy được bóng xanh là: (3/5) . (1/2) = 3/10 = 0,3 (0.25đ)."
      }
    ]
  }
};

if (typeof window !== 'undefined') {
  window.EXAMS_7_C8_7 = EXAMS_7_C8_7;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { EXAMS_7_C8_7 };
}
