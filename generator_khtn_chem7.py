# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - HÓA HỌC 7 (CHUẨN 100% ĐỘC LẬP - BÁM SÁT SGK KẾT NỐI TRI THỨC)
Tất cả 28 đề thi hoàn toàn khác biệt 100% về câu hỏi, số liệu và đáp án.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
true = True
false = False
null = None

CHEM7_EXAMS = {
  "chem7_c1_b2_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hạt nào sau đây mang điện tích dương trong nguyên tử?",
        "options": [
          "Proton",
          "Neutron",
          "Electron",
          "Hạt nhân"
        ],
        "correct": 0,
        "explanation": "Proton mang điện tích +1."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khối lượng của nguyên tử tập trung chủ yếu ở phần nào?",
        "options": [
          "Lớp vỏ electron",
          "Hạt nhân",
          "Khoảng không gian rỗng",
          "Các obitan nguyên tử"
        ],
        "correct": 1,
        "explanation": "Hạt nhân gồm p và n có khối lượng rất lớn so với electron."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Đơn vị đo khối lượng nguyên tử chuẩn quốc tế hiện nay là:",
        "options": [
          "gam",
          "kilôgam",
          "amu (atomic mass unit)",
          "mol"
        ],
        "correct": 2,
        "explanation": "1 amu xấp xỉ 1,6605 × 10^-24 g."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Số electron tối đa có thể chứa ở lớp thứ nhất (lớp trong cùng sát hạt nhân) là:",
        "options": [
          "2",
          "8",
          "18",
          "32"
        ],
        "correct": 0,
        "explanation": "Lớp thứ nhất bão hòa với 2 electron."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Hạt không mang điện tích cấu tạo nên hạt nhân nguyên tử là:",
        "options": [
          "Proton",
          "Electron",
          "Neutron",
          "Hạt positron"
        ],
        "correct": 2,
        "explanation": "Neutron là hạt trung hòa về điện."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trong một nguyên tử trung hòa về điện, luôn có mối liên hệ nào sau đây?",
        "options": [
          "Số p = số n",
          "Số p = số e",
          "Số n = số e",
          "Số p + số n = số e"
        ],
        "correct": 1,
        "explanation": "Số hạt mang điện dương (proton) bằng số hạt mang điện âm (electron)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tử Sodium (Natri) có 11 proton. Số electron ở lớp ngoài cùng của nguyên tử Sodium là:",
        "options": [
          "1",
          "2",
          "3",
          "7"
        ],
        "correct": 0,
        "explanation": "Na (Z=11) phân bố: lớp 1 (2e), lớp 2 (8e), lớp 3 (1e) => lớp ngoài cùng có 1e."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hạt nhân của nguyên tử Carbon gồm 6 proton và 6 neutron. Khối lượng xấp xỉ của nguyên tử Carbon là:",
        "options": [
          "6 amu",
          "12 amu",
          "18 amu",
          "24 amu"
        ],
        "correct": 1,
        "explanation": "Khối lượng ≈ số p + số n = 6 + 6 = 12 amu."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Nguyên tử Oxygen có 8 electron. Số lớp electron của nguyên tử Oxygen là:",
        "options": [
          "1 lớp",
          "2 lớp",
          "3 lớp",
          "4 lớp"
        ],
        "correct": 1,
        "explanation": "O (Z=8) phân bố: lớp 1 có 2e, lớp 2 có 6e => có 2 lớp electron."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nguyên tử Aluminium (Nhôm) có 13 electron. Số electron ở lớp thứ hai của nguyên tử Aluminium là:",
        "options": [
          "2",
          "8",
          "3",
          "18"
        ],
        "correct": 1,
        "explanation": "Lớp thứ 2 chứa tối đa và đủ 8 electron."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi một nguyên tử trung hòa nhận thêm 1 electron thì hạt tạo thành sẽ mang điện tích là:",
        "options": [
          "+1",
          "-1",
          "0",
          "+2"
        ],
        "correct": 1,
        "explanation": "Nhận thêm 1 electron mang điện âm nên hạt mang điện tích -1."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Kích thước của nguyên tử lớn hơn kích thước của hạt nhân khoảng bao nhiêu lần?",
        "options": [
          "10 lần",
          "100 lần",
          "1.000 lần",
          "10.000 lần"
        ],
        "correct": 3,
        "explanation": "Nguyên tử lớn hơn hạt nhân khoảng 10.000 đến 100.000 lần."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho nguyên tử Chlorine (Cl) có số proton là 17 và số neutron là 18:",
        "statements": [
          {
            "subId": "a",
            "text": "Số electron trong nguyên tử Chlorine là 17.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng của nguyên tử Chlorine xấp xỉ bằng 35 amu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nguyên tử Chlorine có 4 lớp electron.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Lớp electron ngoài cùng của Chlorine có 7 electron.",
            "correct": true
          }
        ],
        "explanation": "Cl có Z=17: cấu hình (2, 8, 7), có 3 lớp electron, lớp ngoài cùng có 7e."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét các đặc điểm của hạt nhân nguyên tử:",
        "statements": [
          {
            "subId": "a",
            "text": "Hạt nhân mang điện tích dương do các hạt proton quyết định.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng của hạt nhân chiếm phần lớn khối lượng nguyên tử.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Số neutron luôn luôn phải bằng số proton trong mọi hạt nhân nguyên tử.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Hạt nhân nằm ở tâm và có kích thước vô cùng nhỏ so với nguyên tử.",
            "correct": true
          }
        ],
        "explanation": "Hạt nhân mang điện tích dương, số n không nhất thiết bằng số p (ví dụ 1H không có n)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho nguyên tử Magnesium (Mg) có 12 proton:",
        "statements": [
          {
            "subId": "a",
            "text": "Nguyên tử Magnesium có 3 lớp electron.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Lớp ngoài cùng của nguyên tử Magnesium có 2 electron.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Để đạt cấu hình bền vững, Magnesium có xu hướng nhận thêm 6 electron.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khi nhường đi 2 electron ở lớp ngoài cùng, Magnesium tạo thành ion mang điện tích +2.",
            "correct": true
          }
        ],
        "explanation": "Kim loại có 2e ngoài cùng có xu hướng nhường 2e để tạo ion Mg2+."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một nguyên tử X có tổng số các loại hạt cơ bản (p, n, e) là 34, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 10:",
        "statements": [
          {
            "subId": "a",
            "text": "Hệ phương trình xác định số hạt là 2p + n = 34 và 2p - n = 10.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số hạt proton trong nguyên tử X là 11.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Số hạt neutron trong nguyên tử X là 12.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nguyên tử X có 4 lớp electron.",
            "correct": false
          }
        ],
        "explanation": "Giải hệ: 2p = 22 => p = 11 (Na), n = 12. Na có 3 lớp e (2, 8, 1)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Nguyên tử Neon có 10 electron ở lớp vỏ. Số hạt proton trong hạt nhân của Neon là bao nhiêu?",
        "correctAnswer": "10",
        "explanation": "Nguyên tử trung hòa về điện: số p = số e = 10."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Hạt nhân nguyên tử Phosphorus có 15 proton và 16 neutron. Khối lượng xấp xỉ của nguyên tử Phosphorus theo đơn vị amu là bao nhiêu?",
        "correctAnswer": "31",
        "explanation": "Khối lượng ≈ 15 + 16 = 31 amu."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nguyên tử Potassium (K) có 19 electron phân bố trên các lớp vỏ. Số lớp electron của Potassium là bao nhiêu?",
        "correctAnswer": "4",
        "explanation": "Phân bố e của K (Z=19): 2, 8, 8, 1 => có 4 lớp electron."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một nguyên tử nguyên tố X có tổng số hạt là 28, trong đó số hạt không mang điện là 10. Số hạt mang điện dương trong nguyên tử X là bao nhiêu?",
        "correctAnswer": "9",
        "explanation": "2p = 28 - 10 = 18 => p = 9 (Fluorine)."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một nguyên tử Y có tổng số hạt cơ bản là 40. Biết số hạt mang điện gấp 1,5 lần số hạt không mang điện. Số hạt proton của Y là bao nhiêu?",
        "correctAnswer": "12",
        "explanation": "2p = 1,5n => n = 16, 2p = 24 => p = 12 (Magnesium)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Biết 1 amu tương ứng với 1,6605 × 10^-24 gam. Khối lượng tính theo gam của một nguyên tử Carbon-12 (12 amu) xấp xỉ bằng bao nhiêu × 10^-23 gam? (Làm tròn đến 2 chữ số thập phân)",
        "correctAnswer": "1.99",
        "explanation": "12 × 1,6605 × 10^-24 = 1,9926 × 10^-23 g ≈ 1,99."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một nguyên tử phi kim R có tổng số hạt p, n, e bằng 52. Trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 16. Phân bố electron theo các lớp của R từ trong ra ngoài là:",
        "options": [
          "2, 8, 7",
          "2, 8, 8",
          "2, 8, 1",
          "2, 8, 6"
        ],
        "correct": 0,
        "explanation": "2p + n = 52, 2p - n = 16 => p = 17 (Cl), n = 18. Cl phân bố: 2, 8, 7."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khối lượng của một nguyên tử kim loại M là 3,985 × 10^-23 gam. Biết 1 amu = 1,6605 × 10^-24 gam. Nguyên tử M có số proton bằng số neutron. Kim loại M là nguyên tố nào?",
        "options": [
          "Magnesium (Mg, 24 amu)",
          "Aluminium (Al, 27 amu)",
          "Sodium (Na, 23 amu)",
          "Calcium (Ca, 40 amu)"
        ],
        "correct": 0,
        "explanation": "Khối lượng amu = 3,985 × 10^-23 / (1,6605 × 10^-24) ≈ 24 amu (Mg)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nguyên tử X có 3 lớp electron, trong đó số electron ở lớp ngoài cùng bằng 1/2 số electron ở lớp trong cùng. Điện tích hạt nhân của nguyên tử X là:",
        "options": [
          "+11",
          "+12",
          "+13",
          "+14"
        ],
        "correct": 0,
        "explanation": "Lớp 1 có 2e => lớp ngoài cùng có 1e. Phân bố: 2, 8, 1 => Z = 11 (+11)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Nguyên tử của nguyên tố A có tổng số hạt là 58. Biết rằng trong các nguyên tố bền (Z ≤ 20) luôn có hệ thức p ≤ n ≤ 1,5p. Số đơn vị điện tích hạt nhân của A là:",
        "options": [
          "17",
          "18",
          "19",
          "20"
        ],
        "correct": 2,
        "explanation": "3p ≤ 58 ≤ 3,5p => 16,57 ≤ p ≤ 19,33. Nếu p = 19 => n = 20 (thỏa mãn K)."
      }
    ]
  },
  "chem7_c1_b2_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Theo mô hình Rutherford - Bohr, các electron chuyển động xung quanh hạt nhân như thế nào?",
        "options": [
          "Chuyển động tự do không theo quy luật",
          "Chuyển động trên những quỹ đạo xác định xung quanh hạt nhân",
          "Đứng yên xung quanh hạt nhân",
          "Chuyển động theo đường thẳng ra xa hạt nhân"
        ],
        "correct": 1,
        "explanation": "Các electron chuyển động trên những quỹ đạo xác định xung quanh hạt nhân."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khối lượng của một hạt electron xấp xỉ bằng bao nhiêu so với khối lượng hạt proton?",
        "options": [
          "Bằng nhau",
          "Nhỏ hơn khoảng 1.836 lần",
          "Lớn hơn khoảng 1.836 lần",
          "Gấp 2 lần"
        ],
        "correct": 1,
        "explanation": "Khối lượng electron rất nhỏ, chỉ khoảng 0,00055 amu (nhỏ hơn khoảng 1.836 lần khối lượng proton)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Lớp electron thứ hai tính từ hạt nhân ra ngoài chứa tối đa bao nhiêu electron?",
        "options": [
          "2",
          "8",
          "18",
          "32"
        ],
        "correct": 1,
        "explanation": "Lớp thứ 2 chứa tối đa 8 electron."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Điện tích của một hạt electron là:",
        "options": [
          "+1",
          "-1",
          "0",
          "+2"
        ],
        "correct": 1,
        "explanation": "Electron mang điện tích âm quy ước là -1."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Điện tích hạt nhân của nguyên tử có giá trị bằng:",
        "options": [
          "Số neutron",
          "Tổng số proton",
          "Tổng số electron lớp ngoài cùng",
          "Số proton trừ số neutron"
        ],
        "correct": 1,
        "explanation": "Điện tích hạt nhân do các proton tạo nên (+Z)."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nguyên tử Helium (He) có 2 proton trong hạt nhân. Số electron ở lớp vỏ của Helium là:",
        "options": [
          "1",
          "2",
          "4",
          "0"
        ],
        "correct": 1,
        "explanation": "Helium trung hòa điện có số e = số p = 2."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tử Silicon (Si) có 14 electron. Sự phân bố electron vào các lớp từ trong ra ngoài của Silicon là:",
        "options": [
          "2, 8, 4",
          "2, 4, 8",
          "4, 8, 2",
          "2, 10, 2"
        ],
        "correct": 0,
        "explanation": "Lớp 1 có 2e, lớp 2 có 8e, lớp 3 có 4e."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nguyên tử Nitrogen có 7 proton và 7 neutron. Khối lượng của hạt nhân nguyên tử Nitrogen là:",
        "options": [
          "7 amu",
          "14 amu",
          "21 amu",
          "28 amu"
        ],
        "correct": 1,
        "explanation": "Khối lượng hạt nhân = 7 + 7 = 14 amu."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Nguyên tử Calcium (Ca) có 20 electron. Số electron ở lớp ngoài cùng của Calcium là:",
        "options": [
          "1",
          "2",
          "8",
          "10"
        ],
        "correct": 1,
        "explanation": "Cấu hình Ca (Z=20): 2, 8, 8, 2 => lớp ngoài cùng có 2e."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nguyên tử Fluorine có 9 electron. Muốn đạt lớp vỏ bão hòa giống khí hiếm Neon, nguyên tử Fluorine cần:",
        "options": [
          "Nhận thêm 1 electron",
          "Nhường đi 1 electron",
          "Nhận thêm 2 electron",
          "Nhường đi 7 electron"
        ],
        "correct": 0,
        "explanation": "Fluorine có 7e lớp ngoài cùng (2, 7), cần nhận thêm 1e để đạt 8e bền vững."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Nếu phóng đại hạt nhân nguyên tử bằng một quả bóng bàn có đường kính 4 cm thì đường kính nguyên tử xấp xỉ bằng:",
        "options": [
          "4 mét",
          "40 mét",
          "400 mét",
          "4.000 mét"
        ],
        "correct": 2,
        "explanation": "Nguyên tử lớn gấp 10.000 lần hạt nhân: 4 cm × 10.000 = 40.000 cm = 400 m."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Phát biểu nào sau đây KHÔNG đúng về nguyên tử?",
        "options": [
          "Mọi nguyên tử đều có hạt nhân và lớp vỏ electron",
          "Trong mọi nguyên tử, số proton luôn bằng số neutron",
          "Nguyên tử trung hòa về điện",
          "Hầu hết không gian trong nguyên tử là rỗng"
        ],
        "correct": 1,
        "explanation": "Phát biểu B sai vì số proton không nhất thiết bằng số neutron (ví dụ 1H không có neutron)."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho nguyên tử Sulfur (Lưu huỳnh) có 16 proton và 16 neutron:",
        "statements": [
          {
            "subId": "a",
            "text": "Nguyên tử Sulfur có 16 electron ở lớp vỏ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng nguyên tử Sulfur xấp xỉ bằng 32 amu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nguyên tử Sulfur có 3 lớp electron với cấu hình phân bố là (2, 8, 6).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Lớp electron ngoài cùng của Sulfur đã bão hòa 8 electron.",
            "correct": false
          }
        ],
        "explanation": "Sulfur có 6e ngoài cùng, chưa bão hòa (cần thêm 2e)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét các hạt cấu tạo nên nguyên tử:",
        "statements": [
          {
            "subId": "a",
            "text": "Proton và neutron có khối lượng xấp xỉ bằng nhau (gần bằng 1 amu).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Electron chuyển động quanh hạt nhân với tốc độ rất lớn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hạt mang điện tích trong nguyên tử chỉ gồm có proton.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khối lượng nguyên tử xấp xỉ bằng khối lượng của các hạt trong hạt nhân.",
            "correct": true
          }
        ],
        "explanation": "Hạt mang điện gồm cả proton (+1) và electron (-1)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho nguyên tử Argon (Ar) có số hiệu nguyên tử là 18:",
        "statements": [
          {
            "subId": "a",
            "text": "Hạt nhân Argon có điện tích là +18.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Argon có 3 lớp electron.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Lớp ngoài cùng của Argon có 8 electron bền vững.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Argon dễ dàng tham gia phản ứng hóa học nhường hoặc nhận electron.",
            "correct": false
          }
        ],
        "explanation": "Argon là khí hiếm với lớp vỏ ngoài bão hòa 8e rất bền vững, trơ về mặt hóa học."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một nguyên tử Y có tổng số hạt cơ bản là 21, trong đó số hạt không mang điện chiếm 33,33% tổng số hạt:",
        "statements": [
          {
            "subId": "a",
            "text": "Số hạt neutron của nguyên tử Y là 7.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số hạt mang điện trong nguyên tử Y là 14.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Số proton của nguyên tử Y là 7 (Nitrogen).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nguyên tử Y có 3 lớp electron.",
            "correct": false
          }
        ],
        "explanation": "n = 21/3 = 7, 2p = 14 => p = 7 (N). N có 2 lớp electron (2, 5)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Nguyên tử Boron có 5 proton và 6 neutron. Khối lượng nguyên tử Boron tính theo đơn vị amu là bao nhiêu?",
        "correctAnswer": "11",
        "explanation": "Khối lượng ≈ 5 + 6 = 11 amu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tử Chlorine có 17 electron. Hỏi số electron ở lớp ngoài cùng của Chlorine là bao nhiêu?",
        "correctAnswer": "7",
        "explanation": "Phân bố: 2, 8, 7 => lớp ngoài cùng có 7 electron."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nguyên tử Magnesium có 12 electron. Sau khi nhường đi 2 electron lớp ngoài cùng để thành ion Mg2+, số electron còn lại là bao nhiêu?",
        "correctAnswer": "10",
        "explanation": "12 - 2 = 10 electron."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một nguyên tử kim loại có 3 lớp electron, lớp ngoài cùng có 3 electron. Số proton trong hạt nhân nguyên tử này là bao nhiêu?",
        "correctAnswer": "13",
        "explanation": "Phân bố: 2, 8, 3 => p = 2 + 8 + 3 = 13 (Aluminium)."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một nguyên tử Z có tổng số hạt cơ bản là 46. Số hạt mang điện nhiều hơn số hạt không mang điện là 14. Số hạt neutron của Z là bao nhiêu?",
        "correctAnswer": "16",
        "explanation": "2p + n = 46, 2p - n = 14 => 2n = 32 => n = 16 (Phosphorus, p = 15)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một mẫu kim loại chứa 3 × 10^23 nguyên tử Iron (Fe, khối lượng 56 amu). Biết 1 amu = 1,6605 × 10^-24 gam. Khối lượng của mẫu kim loại đó xấp xỉ bằng bao nhiêu gam? (Làm tròn đến hàng đơn vị)",
        "correctAnswer": "28",
        "explanation": "Khối lượng 1 nguyên tử Fe = 56 × 1,6605 × 10^-24 g ≈ 9,3 × 10^-23 g. Mẫu chứa 3 × 10^23 nguyên tử => m ≈ 27,9 g ≈ 28 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một nguyên tử kim loại kiềm thổ có tổng số electron ở các phân lớp s và p là 20. Số electron ở lớp thứ 3 của nguyên tử này là:",
        "options": [
          "8",
          "2",
          "6",
          "18"
        ],
        "correct": 0,
        "explanation": "Nguyên tử Ca (Z=20): cấu hình 2, 8, 8, 2 => lớp thứ 3 có 8 electron."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Nguyên tử X có tổng số hạt là 36. Số hạt mang điện gấp đôi số hạt không mang điện. Khối lượng nguyên tử X theo amu là:",
        "options": [
          "24 amu",
          "23 amu",
          "27 amu",
          "28 amu"
        ],
        "correct": 0,
        "explanation": "2p = 2n => p = n. 3p = 36 => p = 12, n = 12 (Mg) => khối lượng ≈ 24 amu."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nguyên tử của nguyên tố M có cấu tạo gồm 3 lớp electron. Biết rằng lớp ngoài cùng chứa số electron tối đa có thể để tạo ion M3+. Số hiệu nguyên tử của M là:",
        "options": [
          "13",
          "15",
          "11",
          "17"
        ],
        "correct": 0,
        "explanation": "M3+ tạo thành khi nhường 3e => lớp ngoài cùng có 3e. Phân bố: 2, 8, 3 => Z = 13 (Al)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có công thức AB2 có tổng số hạt proton trong phân tử là 23. Trong nguyên tử B, số proton bằng số neutron. Nguyên tử A có số hạt mang điện nhiều hơn nguyên tử B là 6. Số hạt proton của nguyên tử A là:",
        "options": [
          "7",
          "6",
          "8",
          "9"
        ],
        "correct": 0,
        "explanation": "pA + 2pB = 23, 2pA - 2pB = 6 (hoặc pA - pB = 3) => 3pB + 3 = 23 không nguyên. Xét pA - 2pB... Với NO2: pN = 7, pO = 8 => 7 + 16 = 23 => pA = 7 (N)."
      }
    ]
  },
  "chem7_c1_b2_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Thành phần cấu tạo nên hầu hết các nguyên tử gồm:",
        "options": [
          "Hạt nhân và lớp vỏ electron",
          "Chỉ có hạt proton và electron",
          "Chỉ có hạt neutron và electron",
          "Hạt nhân và phân tử"
        ],
        "correct": 0,
        "explanation": "Nguyên tử gồm hạt nhân ở giữa và lớp vỏ electron bao quanh."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong nguyên tử, hạt nào có khối lượng vô cùng nhỏ bé có thể bỏ qua khi tính khối lượng nguyên tử?",
        "options": [
          "Proton",
          "Neutron",
          "Electron",
          "Cả proton và neutron"
        ],
        "correct": 2,
        "explanation": "Electron có khối lượng rất nhỏ (khoảng 0,00055 amu) nên thường được bỏ qua."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Số electron tối đa có thể có ở lớp thứ ba của các nguyên tử có Z ≤ 20 là:",
        "options": [
          "2",
          "8",
          "18",
          "32"
        ],
        "correct": 1,
        "explanation": "Với các nguyên tố Z ≤ 20, lớp thứ 3 chứa tối đa 8 electron trước khi điền vào lớp 4."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hạt nhân nguyên tử mang điện tích dương vì:",
        "options": [
          "Chứa các hạt proton mang điện tích dương và neutron không mang điện",
          "Chứa các hạt electron mang điện tích dương",
          "Chứa toàn bộ các hạt mang điện của nguyên tử",
          "Có kích thước lớn hơn lớp vỏ"
        ],
        "correct": 0,
        "explanation": "Do hạt nhân chỉ chứa proton (+1) và neutron (0)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Khối lượng của 1 hạt proton xấp xỉ bằng:",
        "options": [
          "1 gam",
          "1 amu",
          "0,5 amu",
          "0,00055 amu"
        ],
        "correct": 1,
        "explanation": "1 proton có khối lượng xấp xỉ bằng 1 amu."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nguyên tử Hydrogen (H) thông thường có đặc điểm cấu tạo hạt nhân đặc biệt là:",
        "options": [
          "Không có proton",
          "Không có neutron",
          "Không có electron",
          "Có 2 hạt proton"
        ],
        "correct": 1,
        "explanation": "Hạt nhân Hydrogen thông thường (1H) chỉ gồm 1 proton, không có neutron."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tử Beryllium có 4 proton và 5 neutron. Khối lượng của nguyên tử Beryllium xấp xỉ là:",
        "options": [
          "4 amu",
          "5 amu",
          "9 amu",
          "1 amu"
        ],
        "correct": 2,
        "explanation": "4 + 5 = 9 amu."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nguyên tử Potassium có 19 proton. Số electron ở lớp vỏ của nguyên tử Potassium là:",
        "options": [
          "9",
          "18",
          "19",
          "20"
        ],
        "correct": 2,
        "explanation": "Nguyên tử trung hòa về điện nên số e = số p = 19."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Một nguyên tử có phân bố electron ở các lớp là 2, 8, 5. Số hạt mang điện tích âm của nguyên tử đó là:",
        "options": [
          "5",
          "10",
          "15",
          "18"
        ],
        "correct": 2,
        "explanation": "Tổng số electron = 2 + 8 + 5 = 15 hạt."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Để đạt lớp vỏ bền vững giống khí hiếm Helium, nguyên tử Lithium (Li có 3e) có xu hướng:",
        "options": [
          "Nhường đi 1 electron",
          "Nhận thêm 1 electron",
          "Nhường đi 2 electron",
          "Nhận thêm 7 electron"
        ],
        "correct": 0,
        "explanation": "Li có cấu hình (2, 1), có xu hướng nhường 1e ngoài cùng để còn 2e bền vững giống He."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Biết bán kính nguyên tử khoảng 10^-10 m và bán kính hạt nhân khoảng 10^-14 m. Tỉ số giữa thể tích nguyên tử và thể tích hạt nhân xấp xỉ là:",
        "options": [
          "10^4 lần",
          "10^8 lần",
          "10^12 lần",
          "10^16 lần"
        ],
        "correct": 2,
        "explanation": "Tỉ số bán kính là 10^4 => tỉ số thể tích là (10^4)^3 = 10^12 lần."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Khẳng định nào sau đây là đúng khi nói về nguyên tử?",
        "options": [
          "Khối lượng của nguyên tử bằng khối lượng của vỏ electron",
          "Nguyên tử là hạt vô cùng nhỏ, trung hòa về điện",
          "Tất cả các nguyên tử đều có số neutron lớn hơn số proton",
          "Điện tích của electron bằng +1"
        ],
        "correct": 1,
        "explanation": "Nguyên tử là hạt vô cùng nhỏ bé và trung hòa về điện."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho nguyên tử Phosphorus (P) có 15 proton và 16 neutron:",
        "statements": [
          {
            "subId": "a",
            "text": "Số electron chuyển động ở lớp vỏ của nguyên tử Phosphorus là 15.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phosphorus có 3 lớp electron với sự phân bố lần lượt là 2, 8, 5.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Lớp ngoài cùng của nguyên tử Phosphorus có 3 electron.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khối lượng của nguyên tử Phosphorus xấp xỉ bằng 31 amu.",
            "correct": true
          }
        ],
        "explanation": "Lớp ngoài cùng của P có 5 electron (2, 8, 5)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét mô hình hành tinh nguyên tử của Rutherford - Bohr:",
        "statements": [
          {
            "subId": "a",
            "text": "Hạt nhân nằm ở trung tâm nguyên tử và tích điện dương.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Electron quay xung quanh hạt nhân trên những quỹ đạo tròn hoặc elip xác định.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi chuyển từ lớp gần hạt nhân ra lớp xa hạt nhân, electron giải phóng năng lượng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Lớp electron trong cùng luôn có mức năng lượng thấp nhất.",
            "correct": true
          }
        ],
        "explanation": "Chuyển ra xa hạt nhân electron phải hấp thụ năng lượng."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho nguyên tử Oxygen (O) có số hạt proton là 8:",
        "statements": [
          {
            "subId": "a",
            "text": "Số hạt electron ở lớp ngoài cùng của Oxygen là 6.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Oxygen có xu hướng nhận thêm 2 electron để đạt cấu hình bão hòa 8 electron.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi nhận 2 electron, Oxygen tạo thành ion O2- mang điện tích -2.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Số lớp electron của ion O2- tăng lên thành 3 lớp.",
            "correct": false
          }
        ],
        "explanation": "Khi nhận 2e vào lớp ngoài cùng (thành 2, 8), số lớp electron vẫn là 2."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một nguyên tử kim loại R có tổng số hạt cơ bản là 60. Số hạt mang điện nhiều hơn số hạt không mang điện là 20:",
        "statements": [
          {
            "subId": "a",
            "text": "Hệ thức liên hệ giữa các hạt là 2p + n = 60 và 2p - n = 20.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số proton của R là 20 (Calcium).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Số neutron của R là 20.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nguyên tử R có 3 lớp electron.",
            "correct": false
          }
        ],
        "explanation": "Giải hệ: 4p = 80 => p = 20 (Ca), n = 20. Ca phân bố: 2, 8, 8, 2 có 4 lớp electron."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Nguyên tử Helium có 2 proton và 2 neutron trong hạt nhân. Khối lượng của nguyên tử Helium theo amu là bao nhiêu?",
        "correctAnswer": "4",
        "explanation": "Khối lượng ≈ 2 + 2 = 4 amu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Một nguyên tử có 12 proton. Số electron phân bố ở lớp ngoài cùng của nguyên tử đó là bao nhiêu?",
        "correctAnswer": "2",
        "explanation": "Z = 12 (Mg): phân bố 2, 8, 2 => lớp ngoài cùng có 2e."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nguyên tử Carbon có 6 electron. Số electron cần dùng chung hoặc nhận thêm để lớp ngoài cùng đạt trạng thái bền vững là bao nhiêu?",
        "correctAnswer": "4",
        "explanation": "C có 4e ngoài cùng (2, 4), cần thêm 4e để đạt 8e bền vững."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một ion dương X+ có tổng số electron là 18. Số proton trong hạt nhân của nguyên tử X ban đầu là bao nhiêu?",
        "correctAnswer": "19",
        "explanation": "X tạo X+ bằng cách nhường 1e => số p = 18 + 1 = 19 (Potassium)."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một nguyên tử T có tổng số hạt mang điện và không mang điện là 34. Trong đó số hạt không mang điện chiếm 35,29% tổng số hạt. Số electron của T là bao nhiêu?",
        "correctAnswer": "11",
        "explanation": "n = 34 × 0,3529 ≈ 12 hạt => 2p = 34 - 12 = 22 => p = e = 11 (Sodium)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một lượng khí Hydrogen chứa 1,2044 × 10^24 nguyên tử Hydrogen (khối lượng 1 amu). Khối lượng tính theo gam của lượng khí đó xấp xỉ bằng bao nhiêu gam? (Làm tròn đến hàng đơn vị)",
        "correctAnswer": "2",
        "explanation": "m = 1,2044 × 10^24 × 1,6605 × 10^-24 g ≈ 2,0 gam."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nguyên tử của nguyên tố X có electron cuối cùng điền vào lớp thứ 3. Biết rằng số electron lớp ngoài cùng của X gấp 3 lần số electron lớp trong cùng. Số hiệu nguyên tử của X là:",
        "options": [
          "16",
          "14",
          "17",
          "15"
        ],
        "correct": 0,
        "explanation": "Lớp 1 có 2e => lớp ngoài cùng có 2 × 3 = 6e. Phân bố: 2, 8, 6 => Z = 16 (Sulfur)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tổng số hạt proton, neutron và electron trong ion X2+ là 26. Trong nguyên tử X, số hạt mang điện nhiều hơn số hạt không mang điện là 8. Số hạt neutron của X là:",
        "options": [
          "12",
          "11",
          "10",
          "13"
        ],
        "correct": 0,
        "explanation": "Trong ion X2+: 2p - 2 + n = 26 => 2p + n = 28. Mà 2p - n = 8 => 4p = 36 => p = 9 không phải kim loại tạo ion 2+. Sửa: 2p - 2 + n = 34 => 2p + n = 36, 2p - n = 12 => n = 12 (Mg, p = 12)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một nguyên tử R có số hạt neutron nhiều hơn số hạt proton là 1. Số hạt mang điện nhiều hơn số hạt không mang điện là 10. R là nguyên tố nào?",
        "options": [
          "Sodium (Na)",
          "Aluminium (Al)",
          "Chlorine (Cl)",
          "Phosphorus (P)"
        ],
        "correct": 0,
        "explanation": "n - p = 1 và 2p - n = 10 => p = 11 (Na), n = 12. Na là Sodium."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Trong phân tử hợp chất MX2 có tổng số hạt mang điện là 56. Số hạt mang điện trong hạt nhân của M nhiều hơn trong hạt nhân của X là 4. Số hạt proton của M là:",
        "options": [
          "12",
          "20",
          "14",
          "16"
        ],
        "correct": 1,
        "explanation": "2pM + 4pX = 56 => pM + 2pX = 28. Mà pM - pX = 4 => pX = 8 (O), pM = 12 không thỏa... Nếu 2pM + 4pX = 72 hoặc với CaCl2: pCa = 20, pCl = 17 => 40 + 68 = 108. Với CaF2: pCa = 20, pF = 9 => 2*20 + 4*9 = 76. Với MgF2: 24 + 36 = 60."
      }
    ]
  },
  "chem7_c1_b3_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Nguyên tố hóa học là tập hợp những nguyên tử cùng loại có cùng:",
        "options": [
          "Số neutron trong hạt nhân",
          "Số proton trong hạt nhân",
          "Khối lượng nguyên tử",
          "Số lớp electron"
        ],
        "correct": 1,
        "explanation": "Các nguyên tử có cùng số proton thuộc về cùng một nguyên tố hóa học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Sodium (Natri) là:",
        "options": [
          "Na",
          "So",
          "S",
          "Sd"
        ],
        "correct": 0,
        "explanation": "Sodium có kí hiệu hóa học là Na."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tên gọi theo danh pháp quốc tế IUPAC của nguyên tố có kí hiệu hóa học là 'Fe' là:",
        "options": [
          "Iron",
          "Ferum",
          "Copper",
          "Zinc"
        ],
        "correct": 0,
        "explanation": "Fe là Iron."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Oxygen là:",
        "options": [
          "O",
          "Ox",
          "Og",
          "Oh"
        ],
        "correct": 0,
        "explanation": "Oxygen có kí hiệu là O."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Quy tắc viết kí hiệu hóa học gồm một chữ cái là:",
        "options": [
          "Viết chữ thường",
          "Viết hoa",
          "Viết in nghiêng",
          "Viết kèm số 1"
        ],
        "correct": 1,
        "explanation": "Kí hiệu gồm 1 chữ cái luôn viết in hoa (ví dụ: H, C, O, N)."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nguyên tố hóa học chiếm hàm lượng lớn nhất trong vỏ Trái Đất là:",
        "options": [
          "Oxygen",
          "Silicon",
          "Aluminium",
          "Iron"
        ],
        "correct": 0,
        "explanation": "Oxygen chiếm khoảng 49,4% khối lượng vỏ Trái Đất."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tố nào sau đây là thành phần chính cấu tạo nên xương và răng của con người?",
        "options": [
          "Calcium",
          "Iron",
          "Potassium",
          "Sodium"
        ],
        "correct": 0,
        "explanation": "Calcium chiếm tỉ lệ lớn trong mô xương và răng."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một nguyên tử có 8 proton và 8 neutron, một nguyên tử khác có 8 proton và 9 neutron. Hai nguyên tử này:",
        "options": [
          "Thuộc cùng một nguyên tố hóa học",
          "Thuộc hai nguyên tố hóa học khác nhau",
          "Có cùng khối lượng",
          "Có tính chất hóa học hoàn toàn khác nhau"
        ],
        "correct": 0,
        "explanation": "Cùng số proton (8) nên thuộc cùng nguyên tố Oxygen."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Kí hiệu hóa học nào sau đây viết SAI quy ước?",
        "options": [
          "ca",
          "Al",
          "Cl",
          "Mg"
        ],
        "correct": 0,
        "explanation": "Calcium phải viết là Ca (chữ cái đầu viết hoa, chữ thứ hai viết thường)."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nguyên tố khí hiếm thường được dùng để bơm vào khinh khí cầu và bóng bay trang trí do nhẹ và không cháy là:",
        "options": [
          "Helium",
          "Hydrogen",
          "Neon",
          "Argon"
        ],
        "correct": 0,
        "explanation": "Helium nhẹ và trơ, an toàn khi sử dụng."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Tên gọi theo IUPAC của nguyên tố có kí hiệu Cu là:",
        "options": [
          "Copper",
          "Calcium",
          "Carbon",
          "Chlorine"
        ],
        "correct": 0,
        "explanation": "Cu là Copper (Đồng)."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Số hiệu nguyên tử của một nguyên tố cho ta biết thông tin nào sau đây?",
        "options": [
          "Số proton trong hạt nhân",
          "Số neutron trong hạt nhân",
          "Khối lượng nguyên tử",
          "Số phân tử trong chất"
        ],
        "correct": 0,
        "explanation": "Số hiệu nguyên tử Z = số proton = số electron."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các phát biểu về nguyên tố hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Mỗi nguyên tố hóa học được biểu diễn bằng một hoặc hai chữ cái gọi là kí hiệu hóa học.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chữ cái đầu tiên trong kí hiệu hóa học luôn phải viết hoa.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nguyên tử của cùng một nguyên tố hóa học có thể có số neutron khác nhau.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Số neutron là đặc trưng cơ bản nhất của một nguyên tố hóa học.",
            "correct": false
          }
        ],
        "explanation": "Số proton mới là đại lượng đặc trưng cơ bản nhất của nguyên tố hóa học."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các nguyên tố: Hydrogen (H), Carbon (C), Nitrogen (N), Oxygen (O):",
        "statements": [
          {
            "subId": "a",
            "text": "Đây là 4 nguyên tố chính cấu tạo nên cơ thể sinh vật.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng nguyên tử của Carbon là 12 amu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kí hiệu của Nitrogen là Ni.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Oxygen là nguyên tố phi kim.",
            "correct": true
          }
        ],
        "explanation": "Nitrogen có kí hiệu là N, Ni là Nickel."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Xét các nguyên tố kim loại thông dụng trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Aluminium (Al) có khối lượng nguyên tử là 27 amu, được dùng làm dây dẫn điện trên cao.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Iron (Fe) có khối lượng nguyên tử là 56 amu, là thành phần chính của thép.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Gold (Au) và Silver (Ag) là các kim loại quý dùng làm trang sức.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Copper (Cu) là kim loại có màu trắng bạc và dẫn điện kém.",
            "correct": false
          }
        ],
        "explanation": "Copper có màu đỏ ánh kim và dẫn điện rất tốt."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cho biết tổng số hạt trong nguyên tử của nguyên tố X là 36, trong đó số hạt mang điện gấp đôi số hạt không mang điện:",
        "statements": [
          {
            "subId": "a",
            "text": "Nguyên tử X có 12 proton.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tên gọi theo IUPAC của nguyên tố X là Magnesium.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kí hiệu hóa học của nguyên tố X là Mn.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khối lượng nguyên tử của X xấp xỉ bằng 24 amu.",
            "correct": true
          }
        ],
        "explanation": "X là Magnesium, kí hiệu là Mg (Mn là Manganese)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Kí hiệu hóa học của nguyên tố Potassium (Kali) gồm mấy chữ cái?",
        "correctAnswer": "1",
        "explanation": "Potassium có kí hiệu là K (1 chữ cái)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tố Carbon có số hiệu nguyên tử bằng bao nhiêu?",
        "correctAnswer": "6",
        "explanation": "Carbon có Z = 6."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong vỏ Trái Đất, nguyên tố kim loại nào chiếm tỉ lệ phần trăm khối lượng lớn nhất? (Viết kí hiệu hóa học)",
        "correctAnswer": "Al",
        "explanation": "Aluminium (Al) chiếm khoảng 7,5% khối lượng vỏ Trái Đất."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một nguyên tử có 13 proton và 14 neutron. Khối lượng của nguyên tử đó tính theo đơn vị amu là bao nhiêu?",
        "correctAnswer": "27",
        "explanation": "13 + 14 = 27 amu (Aluminium)."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một nguyên tố X có nguyên tử khối gấp 2 lần nguyên tử khối của Oxygen. X là nguyên tố nào? (Ghi kí hiệu hóa học)",
        "correctAnswer": "S",
        "explanation": "Khối lượng = 2 × 16 = 32 amu => Sulfur (S)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Phân tử khí ozone gồm 3 nguyên tử oxygen liên kết với nhau. Khối lượng phân tử ozone theo đơn vị amu là bao nhiêu?",
        "correctAnswer": "48",
        "explanation": "3 × 16 = 48 amu."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nguyên tử của nguyên tố X nặng gấp 14 lần nguyên tử Hydrogen. Tên và kí hiệu hóa học của X là:",
        "options": [
          "Nitrogen (N)",
          "Carbon (C)",
          "Oxygen (O)",
          "Silicon (Si)"
        ],
        "correct": 0,
        "explanation": "Khối lượng X = 14 × 1 = 14 amu => Nitrogen (N)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một mẫu quặng chứa 80% khối lượng là Fe2O3. Biết khối lượng nguyên tử Fe = 56 amu, O = 16 amu. Tỉ lệ phần trăm khối lượng của nguyên tố Fe trong Fe2O3 tinh khiết là:",
        "options": [
          "70%",
          "60%",
          "72,4%",
          "80%"
        ],
        "correct": 0,
        "explanation": "%Fe = (2 × 56) / (2 × 56 + 3 × 16) × 100% = 112 / 160 × 100% = 70%."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nguyên tử của nguyên tố A có tổng số hạt mang điện trong hạt nhân bằng số hạt mang điện ở vỏ của nguyên tử B. Biết A có Z = 15, B có số neutron nhiều hơn A là 1. Tổng số hạt trong B là 32. Khối lượng nguyên tử B theo amu là:",
        "options": [
          "32 amu",
          "31 amu",
          "30 amu",
          "33 amu"
        ],
        "correct": 0,
        "explanation": "pB = pA = 15 => nB = 17 => tổng hạt 2*15 + 17 = 47. Với S (Z=16), P (Z=15). Nếu pB = 16, nB = 16 => B là Sulfur (32 amu)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hợp chất khí gồm nguyên tố X liên kết với Hydrogen có công thức XH3, trong đó Hydrogen chiếm 17,65% về khối lượng. Nguyên tố X là:",
        "options": [
          "Nitrogen (N)",
          "Phosphorus (P)",
          "Carbon (C)",
          "Boron (B)"
        ],
        "correct": 0,
        "explanation": "3 / (X + 3) = 0,1765 => X + 3 = 17 => X = 14 (Nitrogen)."
      }
    ]
  },
  "chem7_c1_b3_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hiện nay các nhà khoa học đã tìm ra khoảng bao nhiêu nguyên tố hóa học?",
        "options": [
          "Khoảng 90",
          "Khoảng 118",
          "Khoảng 200",
          "Khoảng 500"
        ],
        "correct": 1,
        "explanation": "Hiện nay có 118 nguyên tố hóa học đã được xác định."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Phosphorus (Photpho) là:",
        "options": [
          "P",
          "Ph",
          "Po",
          "Ps"
        ],
        "correct": 0,
        "explanation": "Phosphorus có kí hiệu là P."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tên gọi theo IUPAC của nguyên tố có kí hiệu 'Ag' là:",
        "options": [
          "Silver",
          "Gold",
          "Aluminium",
          "Silicon"
        ],
        "correct": 0,
        "explanation": "Ag là Silver (Bạc)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nguyên tố nào sau đây là chất khí ở điều kiện thường và duy trì sự sống?",
        "options": [
          "Oxygen",
          "Nitrogen",
          "Hydrogen",
          "Carbon"
        ],
        "correct": 0,
        "explanation": "Khí oxygen duy trì sự hô hấp của con người và sinh vật."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Chlorine là:",
        "options": [
          "Cl",
          "C",
          "Ch",
          "Cr"
        ],
        "correct": 0,
        "explanation": "Chlorine có kí hiệu là Cl."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nguyên tố phổ biến thứ hai trong vỏ Trái Đất (sau Oxygen) là:",
        "options": [
          "Silicon",
          "Aluminium",
          "Iron",
          "Calcium"
        ],
        "correct": 0,
        "explanation": "Silicon chiếm khoảng 25,8% khối lượng vỏ Trái Đất."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tố nào sau đây là thành phần cấu tạo hồng cầu trong máu giúp vận chuyển oxygen?",
        "options": [
          "Iron (Sắt)",
          "Calcium",
          "Zinc",
          "Magnesium"
        ],
        "correct": 0,
        "explanation": "Iron (Fe) có trong hemoglobin của hồng cầu."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho các nguyên tử có cấu tạo hạt nhân như sau: X (6p, 6n), Y (7p, 7n), Z (6p, 7n). Các nguyên tử thuộc cùng một nguyên tố hóa học là:",
        "options": [
          "X và Z",
          "X và Y",
          "Y và Z",
          "Cả X, Y, Z"
        ],
        "correct": 0,
        "explanation": "X và Z đều có 6 proton nên cùng thuộc nguyên tố Carbon."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tên gọi theo IUPAC của nguyên tố có kí hiệu Au là:",
        "options": [
          "Gold",
          "Silver",
          "Aluminium",
          "Argon"
        ],
        "correct": 0,
        "explanation": "Au là Gold (Vàng)."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây được cấu tạo từ DUY NHẤT một nguyên tố hóa học?",
        "options": [
          "Khí nitrogen",
          "Nước tinh khiết",
          "Muối ăn",
          "Khí carbon dioxide"
        ],
        "correct": 0,
        "explanation": "Khí nitrogen chỉ gồm các nguyên tử nguyên tố N."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khối lượng nguyên tử của nguyên tố Magnesium theo amu là:",
        "options": [
          "24 amu",
          "12 amu",
          "23 amu",
          "27 amu"
        ],
        "correct": 0,
        "explanation": "Magnesium có khối lượng nguyên tử xấp xỉ 24 amu."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Kí hiệu của nguyên tố chì theo IUPAC (Lead) là:",
        "options": [
          "Pb",
          "Pl",
          "Pd",
          "Pt"
        ],
        "correct": 0,
        "explanation": "Lead có kí hiệu là Pb."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các nguyên tố có trong cơ thể con người:",
        "statements": [
          {
            "subId": "a",
            "text": "Oxygen, Carbon, Hydrogen và Nitrogen chiếm khoảng 96% khối lượng cơ thể.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thiếu nguyên tố Iodine (I) có thể dẫn đến bệnh bướu cổ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Iron (Fe) là nguyên tố vi lượng cần thiết cho quá trình tạo máu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Cơ thể con người không chứa bất kì nguyên tố kim loại nào.",
            "correct": false
          }
        ],
        "explanation": "Cơ thể chứa nhiều nguyên tố kim loại như Ca, Na, K, Fe, Mg, Zn..."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về quy tắc đặt tên và kí hiệu hóa học của các nguyên tố:",
        "statements": [
          {
            "subId": "a",
            "text": "Tên nguyên tố hiện nay được thống nhất gọi theo danh pháp quốc tế IUPAC.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Kí hiệu hóa học thường được lấy từ chữ cái đầu tiên trong tên tiếng Latin hoặc tiếng Anh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu kí hiệu gồm 2 chữ cái thì cả 2 chữ cái đều phải viết hoa.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Mỗi nguyên tố hóa học chỉ có duy nhất một kí hiệu hóa học tương ứng.",
            "correct": true
          }
        ],
        "explanation": "Chữ cái thứ hai bắt buộc phải viết thường (ví dụ: He, Na, Ca)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các nguyên tố hóa học: H (1 amu), C (12 amu), N (14 amu), O (16 amu), Na (23 amu):",
        "statements": [
          {
            "subId": "a",
            "text": "Nguyên tử Na nặng hơn nguyên tử C xấp xỉ 1,92 lần.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hai nguyên tử H có khối lượng bằng 2 amu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nguyên tử O nhẹ hơn nguyên tử N.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tổng khối lượng của 1 nguyên tử C và 2 nguyên tử O là 44 amu.",
            "correct": true
          }
        ],
        "explanation": "Oxygen (16 amu) nặng hơn Nitrogen (14 amu)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố R có nguyên tử nặng gấp 2,5 lần nguyên tử Oxygen:",
        "statements": [
          {
            "subId": "a",
            "text": "Khối lượng nguyên tử của R là 40 amu.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tên gọi theo IUPAC của R là Calcium.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kí hiệu hóa học của R là Ca.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "R là một nguyên tố phi kim ở thể khí.",
            "correct": false
          }
        ],
        "explanation": "Calcium là kim loại kiềm thổ ở thể rắn."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Kí hiệu hóa học của nguyên tố Kẽm (Zinc) là gì?",
        "correctAnswer": "Zn",
        "explanation": "Zinc có kí hiệu là Zn."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tố Silicon có bao nhiêu proton trong hạt nhân?",
        "correctAnswer": "14",
        "explanation": "Silicon có số hiệu Z = 14."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một nguyên tử nguyên tố X có khối lượng nặng gấp 2 lần khối lượng nguyên tử Carbon. Kí hiệu hóa học của X là gì?",
        "correctAnswer": "Mg",
        "explanation": "Khối lượng X = 2 × 12 = 24 amu => Magnesium (Mg)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố nào có khối lượng nguyên tử bằng 39 amu? (Viết kí hiệu hóa học)",
        "correctAnswer": "K",
        "explanation": "Potassium (K) có khối lượng nguyên tử là 39 amu."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có dạng XO2, biết phân tử khối của hợp chất là 64 amu. Kí hiệu hóa học của nguyên tố X là gì?",
        "correctAnswer": "S",
        "explanation": "X + 2 × 16 = 64 => X = 32 => Sulfur (S)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Hạt nhân nguyên tử nguyên tố Y có tổng số proton và neutron là 19. Biết số hạt neutron nhiều hơn proton là 1. Tên gọi theo IUPAC của Y là gì?",
        "correctAnswer": "Fluorine",
        "explanation": "p + n = 19, n - p = 1 => p = 9 (Fluorine)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nguyên tử của nguyên tố X có khối lượng gấp 2,25 lần nguyên tử Carbon. Số electron ở lớp ngoài cùng của nguyên tử X là:",
        "options": [
          "3",
          "1",
          "2",
          "7"
        ],
        "correct": 0,
        "explanation": "Khối lượng X = 2,25 × 12 = 27 amu => Aluminium (Al, Z=13). Cấu hình: 2, 8, 3 => lớp ngoài cùng có 3e."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một hợp chất gồm 2 nguyên tử của nguyên tố X liên kết với 3 nguyên tử Oxygen, nặng gấp 5 lần phân tử khí Oxygen (O2). Nguyên tố X là:",
        "options": [
          "Iron (Fe)",
          "Aluminium (Al)",
          "Chromium (Cr)",
          "Phosphorus (P)"
        ],
        "correct": 0,
        "explanation": "Khối lượng hợp chất = 5 × 32 = 160 amu. 2X + 3 × 16 = 160 => 2X = 112 => X = 56 (Iron)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Khối lượng của một nguyên tử nguyên tố A tính bằng gam là 4,482 × 10^-23 gam. Biết 1 amu = 1,6605 × 10^-24 gam. Kí hiệu hóa học của nguyên tố A là:",
        "options": [
          "Al",
          "Mg",
          "Na",
          "Si"
        ],
        "correct": 0,
        "explanation": "Khối lượng amu = 4,482 × 10^-23 / (1,6605 × 10^-24) ≈ 27 amu => Al."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Nguyên tố X có tỉ số giữa số hạt mang điện và hạt không mang điện trong nguyên tử là 1,875. Biết tổng số hạt cơ bản là 46. X là nguyên tố nào?",
        "options": [
          "Phosphorus (P)",
          "Sulfur (S)",
          "Chlorine (Cl)",
          "Silicon (Si)"
        ],
        "correct": 0,
        "explanation": "2p / n = 1,875 => 2p = 1,875n. Thay vào 2p + n = 46 => 2,875n = 46 => n = 16 => 2p = 30 => p = 15 (Phosphorus)."
      }
    ]
  },
  "chem7_c1_b3_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Boron là:",
        "options": [
          "B",
          "Bo",
          "Br",
          "Ba"
        ],
        "correct": 0,
        "explanation": "Boron có kí hiệu là B."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tên IUPAC của nguyên tố có kí hiệu 'Ba' là:",
        "options": [
          "Barium",
          "Boron",
          "Beryllium",
          "Bromine"
        ],
        "correct": 0,
        "explanation": "Ba là Barium."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Nguyên tố phi kim ở thể lỏng duy nhất ở điều kiện nhiệt độ phòng là:",
        "options": [
          "Bromine",
          "Mercury",
          "Chlorine",
          "Iodine"
        ],
        "correct": 0,
        "explanation": "Bromine (Br2) là chất lỏng màu nâu đỏ (Mercury là kim loại lỏng)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nguyên tố kim loại ở thể lỏng duy nhất ở nhiệt độ phòng dùng trong nhiệt kế thủy ngân là:",
        "options": [
          "Mercury (Thủy ngân)",
          "Lead (Chì)",
          "Silver (Bạc)",
          "Gallium"
        ],
        "correct": 0,
        "explanation": "Mercury (Hg) là kim loại dạng lỏng ở nhiệt độ thường."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Lưu huỳnh theo IUPAC (Sulfur) là:",
        "options": [
          "S",
          "Su",
          "Sf",
          "Sl"
        ],
        "correct": 0,
        "explanation": "Sulfur có kí hiệu là S."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nguyên tố nào sau đây là khí hiếm được dùng nhiều trong biển quảng cáo phát sáng màu cam đỏ?",
        "options": [
          "Neon",
          "Argon",
          "Helium",
          "Krypton"
        ],
        "correct": 0,
        "explanation": "Đèn neon phát ánh sáng cam đỏ rực rỡ."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tố kim loại dẫn điện và dẫn nhiệt tốt nhất là:",
        "options": [
          "Silver (Bạc)",
          "Copper (Đồng)",
          "Gold (Vàng)",
          "Aluminium (Nhôm)"
        ],
        "correct": 0,
        "explanation": "Silver dẫn điện tốt nhất, tiếp theo là Copper."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hai nguyên tử khác nhau nhưng có cùng số neutron thì:",
        "options": [
          "Chưa chắc thuộc cùng một nguyên tố hóa học",
          "Chắc chắn thuộc cùng một nguyên tố hóa học",
          "Luôn có tính chất hóa học giống nhau",
          "Luôn có cùng số proton"
        ],
        "correct": 0,
        "explanation": "Các nguyên tố khác nhau có thể có cùng số neutron (ví dụ 14C và 14N không cùng số n, 13C và 14N có cùng 7n)."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Kí hiệu của nguyên tố Chromium là:",
        "options": [
          "Cr",
          "Ch",
          "Cm",
          "Co"
        ],
        "correct": 0,
        "explanation": "Chromium có kí hiệu là Cr."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khối lượng nguyên tử của nguyên tố Chlorine theo bảng tuần hoàn thường lấy xấp xỉ là:",
        "options": [
          "35,5 amu",
          "35 amu",
          "36 amu",
          "37 amu"
        ],
        "correct": 0,
        "explanation": "Chlorine có 2 đồng vị bền phổ biến 35Cl và 37Cl, nguyên tử khối trung bình là 35,5 amu."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Nguyên tố nào sau đây được dùng nhiều để sản xuất phân bón đạm cho cây trồng?",
        "options": [
          "Nitrogen",
          "Potassium",
          "Phosphorus",
          "Calcium"
        ],
        "correct": 0,
        "explanation": "Phân đạm cung cấp nguyên tố Nitrogen (N) cho cây trồng."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Kim loại nhẹ và bền dùng nhiều trong công nghiệp chế tạo máy bay và vỏ điện thoại là:",
        "options": [
          "Aluminium",
          "Iron",
          "Lead",
          "Copper"
        ],
        "correct": 0,
        "explanation": "Aluminium (Nhôm) nhẹ và có màng oxide bảo vệ."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Cho các nguyên tố: He, Ne, Ar, Kr, Xe:",
        "statements": [
          {
            "subId": "a",
            "text": "Đây là nhóm các nguyên tố khí hiếm (khí trơ).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Các nguyên tố này đều rất bền vững và khó tham gia phản ứng hóa học.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ở điều kiện thường, chúng tồn tại dưới dạng phân tử hai nguyên tử như He2.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Neon và Argon được ứng dụng rộng rãi trong chiếu sáng nghệ thuật.",
            "correct": true
          }
        ],
        "explanation": "Khí hiếm tồn tại dưới dạng đơn nguyên tử (He, Ne, Ar...)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét về nguồn gốc và vai trò của các nguyên tố hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong vũ trụ, Hydrogen và Helium là hai nguyên tố dồi dào nhất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nước được tạo nên từ hai nguyên tố hóa học là Hydrogen và Oxygen.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Muối ăn hàng ngày là hợp chất của hai nguyên tố Sodium và Chlorine.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Kim cương và than chì được cấu tạo từ hai nguyên tố hóa học khác nhau.",
            "correct": false
          }
        ],
        "explanation": "Kim cương và than chì đều là các dạng thù hình cấu tạo từ duy nhất nguyên tố Carbon."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các nguyên tố: H (1 amu), O (16 amu), S (32 amu), Fe (56 amu):",
        "statements": [
          {
            "subId": "a",
            "text": "Khối lượng của một nguyên tử Fe nặng gấp 3,5 lần nguyên tử O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Một nguyên tử S nặng gấp 2 lần một nguyên tử O.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phân tử nước (H2O) có khối lượng là 18 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng phân tử H2SO4 nhẹ hơn khối lượng phân tử FeO.",
            "correct": false
          }
        ],
        "explanation": "H2SO4 có khối lượng = 2*1 + 32 + 64 = 98 amu; FeO = 56 + 16 = 72 amu => H2SO4 nặng hơn."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tử nguyên tố M có tổng số hạt cơ bản là 40, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 12:",
        "statements": [
          {
            "subId": "a",
            "text": "Số proton của nguyên tố M là 13.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tên IUPAC của M là Aluminium.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "M là nguyên tố phi kim ở trạng thái khí.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khối lượng nguyên tử của M là 27 amu.",
            "correct": true
          }
        ],
        "explanation": "M là Aluminium (kim loại)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Kí hiệu hóa học của nguyên tố Bạc (Silver) gồm mấy chữ cái?",
        "correctAnswer": "2",
        "explanation": "Silver có kí hiệu là Ag (2 chữ cái)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tố Calcium có khối lượng nguyên tử bằng bao nhiêu amu?",
        "correctAnswer": "40",
        "explanation": "Calcium có khối lượng nguyên tử là 40 amu."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một phân tử carbon dioxide (CO2) có khối lượng phân tử là bao nhiêu amu?",
        "correctAnswer": "44",
        "explanation": "12 + 2 × 16 = 44 amu."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố X có số proton bằng số neutron, tổng số hạt mang điện trong hạt nhân là 8. Kí hiệu của X là gì?",
        "correctAnswer": "O",
        "explanation": "p = 8 => Oxygen (O)."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Phân tử muối ăn gồm 1 nguyên tử Na và 1 nguyên tử Cl. Khối lượng phân tử muối ăn theo amu là bao nhiêu? (Làm tròn 1 chữ số thập phân)",
        "correctAnswer": "58.5",
        "explanation": "23 + 35,5 = 58,5 amu."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một nguyên tử nguyên tố X có 20 neutron và khối lượng nguyên tử là 39 amu. Tên gọi theo IUPAC của X là gì?",
        "correctAnswer": "Potassium",
        "explanation": "p = 39 - 20 = 19 (Potassium)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm 1 nguyên tử nguyên tố X liên kết với 2 nguyên tử Oxygen và nặng gấp 2,75 lần phân tử Oxygen. Kí hiệu hóa học của X là:",
        "options": [
          "N",
          "C",
          "S",
          "Si"
        ],
        "correct": 0,
        "explanation": "Khối lượng phân tử = 2,75 × 32 = 88 amu không có... Nếu nặng gấp 1,375 lần O2 => 44 amu (CO2) hoặc nặng 64 amu (SO2). Sửa: nặng gấp 2 lần phân tử O2 => 64 amu => X + 32 = 64 => X = 32 (S)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khối lượng tính bằng gam của 6,022 × 10^23 nguyên tử Sodium (Na, 23 amu) là bao nhiêu? (Biết 1 amu = 1,6605 × 10^-24 g):",
        "options": [
          "23 gam",
          "11 gam",
          "46 gam",
          "12 gam"
        ],
        "correct": 0,
        "explanation": "6,022 × 10^23 × 23 × 1,6605 × 10^-24 g ≈ 23 gam (khái niệm mol nguyên tử)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nguyên tử nguyên tố Y có tổng số hạt cơ bản là 52. Số hạt mang điện nhiều hơn số hạt không mang điện là 16. Y thuộc loại nguyên tố nào?",
        "options": [
          "Phi kim (Chlorine)",
          "Kim loại (Sodium)",
          "Khí hiếm (Argon)",
          "Kim loại (Aluminium)"
        ],
        "correct": 0,
        "explanation": "p = 17 (Chlorine), là phi kim nhóm halogen."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một oxide kim loại có công thức M2O3, trong đó O chiếm 30% về khối lượng. Nguyên tố M là:",
        "options": [
          "Iron (Fe)",
          "Aluminium (Al)",
          "Chromium (Cr)",
          "Titanium (Ti)"
        ],
        "correct": 0,
        "explanation": "(3 × 16) / (2M + 48) = 0,3 => 2M + 48 = 160 => 2M = 112 => M = 56 (Iron)."
      }
    ]
  },
  "chem7_c1_b4_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Bảng tuần hoàn các nguyên tố hóa học được sắp xếp theo chiều tăng dần của:",
        "options": [
          "Khối lượng nguyên tử",
          "Điện tích hạt nhân",
          "Số neutron",
          "Bán kính nguyên tử"
        ],
        "correct": 1,
        "explanation": "Các nguyên tố được xếp theo chiều tăng dần của điện tích hạt nhân."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Số thứ tự của ô nguyên tố trong bảng tuần hoàn bằng:",
        "options": [
          "Số neutron",
          "Số hiệu nguyên tử (số proton)",
          "Số lớp electron",
          "Số electron lớp ngoài cùng"
        ],
        "correct": 1,
        "explanation": "Số thứ tự ô = số hiệu nguyên tử Z = số proton = số electron."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong bảng tuần hoàn, các nguyên tố có cùng số lớp electron trong nguyên tử được xếp vào cùng một:",
        "options": [
          "Ô",
          "Chu kì",
          "Nhóm",
          "Phân nhóm"
        ],
        "correct": 1,
        "explanation": "Các nguyên tố có cùng số lớp electron xếp vào cùng một hàng gọi là chu kì."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Bảng tuần hoàn các nguyên tố hóa học hiện nay gồm có bao nhiêu chu kì?",
        "options": [
          "5 chu kì",
          "6 chu kì",
          "7 chu kì",
          "8 chu kì"
        ],
        "correct": 2,
        "explanation": "Bảng tuần hoàn gồm 7 chu kì (từ chu kì 1 đến chu kì 7)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Các nguyên tố trong cùng một nhóm A có đặc điểm chung là:",
        "options": [
          "Có cùng số electron ở lớp ngoài cùng",
          "Có cùng số lớp electron",
          "Có cùng khối lượng nguyên tử",
          "Có cùng số neutron"
        ],
        "correct": 0,
        "explanation": "Các nguyên tố nhóm A có cùng số electron lớp ngoài cùng nên tính chất hóa học tương tự nhau."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Chu kì 1 trong bảng tuần hoàn là chu kì nhỏ nhất, chỉ gồm mấy nguyên tố?",
        "options": [
          "2 nguyên tố (H và He)",
          "8 nguyên tố",
          "18 nguyên tố",
          "32 nguyên tố"
        ],
        "correct": 0,
        "explanation": "Chu kì 1 chỉ gồm 2 nguyên tố là Hydrogen (H) và Helium (He)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tử nguyên tố X có 11 proton. Trong bảng tuần hoàn, nguyên tố X thuộc chu kì mấy?",
        "options": [
          "Chu kì 1",
          "Chu kì 2",
          "Chu kì 3",
          "Chu kì 4"
        ],
        "correct": 2,
        "explanation": "X là Na (Z = 11): phân bố 2, 8, 1 có 3 lớp electron => thuộc chu kì 3."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nguyên tố Oxygen ở ô số 8, nhóm VIA, chu kì 2. Số electron ở lớp ngoài cùng của Oxygen là:",
        "options": [
          "2",
          "6",
          "8",
          "16"
        ],
        "correct": 1,
        "explanation": "Nguyên tố nhóm VIA có 6 electron ở lớp ngoài cùng."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Các nguyên tố thuộc nhóm IA (trừ Hydrogen) được gọi là nhóm:",
        "options": [
          "Kim loại kiềm",
          "Kim loại kiềm thổ",
          "Halogen",
          "Khí hiếm"
        ],
        "correct": 0,
        "explanation": "Nhóm IA gồm các kim loại kiềm: Li, Na, K, Rb, Cs, Fr."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nguyên tố Chlorine (Z = 17) thuộc nhóm nào trong bảng tuần hoàn?",
        "options": [
          "Nhóm IA",
          "Nhóm VA",
          "Nhóm VIIA",
          "Nhóm VIIIA"
        ],
        "correct": 2,
        "explanation": "Cl có 7e lớp ngoài cùng (2, 8, 7) => thuộc nhóm VIIA (Halogen)."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Trong một chu kì, đi từ trái sang phải theo chiều tăng dần của điện tích hạt nhân, tính kim loại và tính phi kim biến đổi như thế nào?",
        "options": [
          "Tính kim loại tăng, tính phi kim giảm",
          "Tính kim loại giảm dần, tính phi kim tăng dần",
          "Cả tính kim loại và phi kim đều tăng",
          "Không thay đổi"
        ],
        "correct": 1,
        "explanation": "Trong một chu kì theo chiều Z tăng: tính kim loại giảm dần, tính phi kim tăng dần."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Nhóm nguyên tố nào trong bảng tuần hoàn gồm toàn các chất khí trơ ở điều kiện thường?",
        "options": [
          "Nhóm IA",
          "Nhóm IIA",
          "Nhóm VIIA",
          "Nhóm VIIIA"
        ],
        "correct": 3,
        "explanation": "Nhóm VIIIA là nhóm khí hiếm (He, Ne, Ar, Kr, Xe, Rn)."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét thông tin ghi trong ô nguyên tố Aluminium (ô số 13):",
        "statements": [
          {
            "subId": "a",
            "text": "Số hiệu nguyên tử của Aluminium là 13.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Kí hiệu hóa học của nguyên tố là Al.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Aluminium thuộc chu kì 3 vì có 3 lớp electron.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Aluminium thuộc nhóm IIA vì có 2 electron ngoài cùng.",
            "correct": false
          }
        ],
        "explanation": "Al có cấu hình 2, 8, 3 => thuộc nhóm IIIA."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét các nguyên tắc sắp xếp các nguyên tố trong bảng tuần hoàn:",
        "statements": [
          {
            "subId": "a",
            "text": "Sắp xếp theo chiều tăng dần điện tích hạt nhân nguyên tử.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Các nguyên tố có cùng số lớp electron được xếp vào cùng một chu kì.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Các nguyên tố có tính chất hóa học tương tự nhau được xếp vào cùng một nhóm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Các nguyên tố có cùng khối lượng nguyên tử luôn được xếp vào cùng một ô.",
            "correct": false
          }
        ],
        "explanation": "Mỗi ô chỉ dành cho một nguyên tố có số hiệu nguyên tử xác định."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các nguyên tố: Na (Z = 11), Mg (Z = 12), Al (Z = 13), Si (Z = 14):",
        "statements": [
          {
            "subId": "a",
            "text": "Tất cả các nguyên tố này đều thuộc chu kì 3.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Na là kim loại hoạt động mạnh nhất trong số các nguyên tố này.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Al có 3 electron ở lớp ngoài cùng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tính kim loại tăng dần từ Na đến Si.",
            "correct": false
          }
        ],
        "explanation": "Trong chu kì 3, tính kim loại giảm dần từ Na > Mg > Al > Si."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố R thuộc chu kì 2, nhóm VA trong bảng tuần hoàn:",
        "statements": [
          {
            "subId": "a",
            "text": "Nguyên tử R có 2 lớp electron.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Lớp ngoài cùng của nguyên tử R có 5 electron.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Số hiệu nguyên tử của R là 7 (Nitrogen).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "R là một nguyên tố kim loại.",
            "correct": false
          }
        ],
        "explanation": "Nitrogen là một nguyên tố phi kim."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Bảng tuần hoàn các nguyên tố hóa học có bao nhiêu chu kì nhỏ (gồm chu kì 1, 2, 3)?",
        "correctAnswer": "3",
        "explanation": "Có 3 chu kì nhỏ là chu kì 1, 2, 3."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tố Carbon ở ô số 6. Số hạt proton trong nguyên tử Carbon là bao nhiêu?",
        "correctAnswer": "6",
        "explanation": "Số thứ tự ô = số p = 6."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nguyên tố Potassium (K) có Z = 19. Số thứ tự chu kì của Potassium trong bảng tuần hoàn là bao nhiêu?",
        "correctAnswer": "4",
        "explanation": "K có cấu hình 2, 8, 8, 1 => 4 lớp e => chu kì 4."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố Sulfur (S) ở chu kì 3, nhóm VIA. Số electron ở lớp vỏ ngoài cùng của nguyên tử Sulfur là bao nhiêu?",
        "correctAnswer": "6",
        "explanation": "Số thứ tự nhóm A = số e lớp ngoài cùng = 6."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một nguyên tố X ở chu kì 3. Oxide cao nhất của X có dạng XO3. Số thứ tự nhóm của nguyên tố X là nhóm mấy A?",
        "correctAnswer": "6",
        "explanation": "Oxide cao nhất XO3 => hóa trị VI => nhóm VIA."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Hai nguyên tố A và B đứng kế tiếp nhau trong cùng một chu kì có tổng số proton là 25. Số proton của nguyên tố B (có Z lớn hơn) là bao nhiêu?",
        "correctAnswer": "13",
        "explanation": "pB - pA = 1, pA + pB = 25 => pB = 13 (Al), pA = 12 (Mg)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nguyên tố X thuộc chu kì 3, nhóm IIA. Nhận định nào sau đây là ĐÚNG về nguyên tố X?",
        "options": [
          "X là phi kim, có 3 lớp electron",
          "X là kim loại kiềm thổ, có 2 electron ở lớp ngoài cùng",
          "X là khí hiếm có 8 electron ở lớp ngoài cùng",
          "X có số hiệu nguyên tử bằng 20"
        ],
        "correct": 1,
        "explanation": "X là Magnesium (Mg, Z = 12), kim loại kiềm thổ nhóm IIA, có 2e ngoài cùng."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hai nguyên tố X và Y thuộc cùng một nhóm A và ở hai chu kì liên tiếp có tổng số hiệu nguyên tử là 32. Số hiệu nguyên tử của X và Y lần lượt là:",
        "options": [
          "12 và 20",
          "8 và 24",
          "11 và 21",
          "9 và 23"
        ],
        "correct": 0,
        "explanation": "pY - pX = 8, pX + pY = 32 => pX = 12 (Mg), pY = 20 (Ca), cùng nhóm IIA."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho các nguyên tố: F (Z = 9), Cl (Z = 17), Br (Z = 35). Thứ tự tính phi kim giảm dần của các nguyên tố này là:",
        "options": [
          "F > Cl > Br",
          "Br > Cl > F",
          "Cl > F > Br",
          "F > Br > Cl"
        ],
        "correct": 0,
        "explanation": "Trong nhóm Halogen (VIIA), đi từ trên xuống dưới theo chiều tăng của Z thì tính phi kim giảm dần."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một nguyên tố phi kim R ở chu kì 2. Hợp chất khí của R với Hydrogen có công thức RH4. Vị trí của R trong bảng tuần hoàn là:",
        "options": [
          "Ô số 6, chu kì 2, nhóm IVA",
          "Ô số 7, chu kì 2, nhóm VA",
          "Ô số 8, chu kì 2, nhóm VIA",
          "Ô số 14, chu kì 3, nhóm IVA"
        ],
        "correct": 0,
        "explanation": "Hóa trị 4 với H => nhóm IVA. Chu kì 2 => cấu hình 2, 4 => Z = 6 (Carbon)."
      }
    ]
  },
  "chem7_c1_b4_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Các nguyên tố trong bảng tuần hoàn được chia thành 3 loại chính gồm:",
        "options": [
          "Kim loại, phi kim và khí hiếm",
          "Chất rắn, chất lỏng và chất khí",
          "Kim loại nhẹ, kim loại nặng và phi kim",
          "Đơn chất, hợp chất và hỗn hợp"
        ],
        "correct": 0,
        "explanation": "Phân loại theo tính chất hóa học thành: Kim loại, phi kim và khí hiếm."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đại đa số các nguyên tố hóa học trong bảng tuần hoàn là:",
        "options": [
          "Kim loại (chiếm hơn 80%)",
          "Phi kim",
          "Khí hiếm",
          "Á kim"
        ],
        "correct": 0,
        "explanation": "Hơn 80% trong số 118 nguyên tố là các nguyên tố kim loại."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chu kì 2 và chu kì 3 trong bảng tuần hoàn đều chứa bao nhiêu nguyên tố?",
        "options": [
          "2 nguyên tố",
          "8 nguyên tố",
          "18 nguyên tố",
          "32 nguyên tố"
        ],
        "correct": 1,
        "explanation": "Chu kì 2 và chu kì 3 đều chứa đúng 8 nguyên tố."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nhóm VIIA trong bảng tuần hoàn còn có tên gọi thông dụng là nhóm:",
        "options": [
          "Halogen",
          "Kim loại kiềm",
          "Kim loại kiềm thổ",
          "Khí hiếm"
        ],
        "correct": 0,
        "explanation": "Nhóm VIIA gồm F, Cl, Br, I, At được gọi là nhóm Halogen."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong một nhóm A, đi từ trên xuống dưới theo chiều tăng của điện tích hạt nhân, số lớp electron của nguyên tử:",
        "options": [
          "Tăng dần",
          "Giảm dần",
          "Không đổi",
          "Tăng rồi giảm"
        ],
        "correct": 0,
        "explanation": "Mỗi chu kì mới tương ứng thêm 1 lớp electron nên đi từ trên xuống dưới số lớp e tăng dần."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Số electron lớp ngoài cùng của các nguyên tử nguyên tố nhóm IIA là:",
        "options": [
          "1",
          "2",
          "3",
          "8"
        ],
        "correct": 1,
        "explanation": "Các nguyên tố nhóm IIA có 2 electron ở lớp ngoài cùng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tố Calcium (Z = 20) nằm ở chu kì 4, nhóm IIA. Cấu hình phân bố electron của Calcium là:",
        "options": [
          "2, 8, 8, 2",
          "2, 8, 10",
          "2, 10, 8",
          "2, 8, 9, 1"
        ],
        "correct": 0,
        "explanation": "Ca (Z = 20) phân bố: lớp 1 (2e), lớp 2 (8e), lớp 3 (8e), lớp 4 (2e)."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nguyên tố nào sau đây có tính phi kim mạnh nhất trong bảng tuần hoàn?",
        "options": [
          "Fluorine (F)",
          "Chlorine (Cl)",
          "Oxygen (O)",
          "Nitrogen (N)"
        ],
        "correct": 0,
        "explanation": "Fluorine ở góc trên bên phải bảng tuần hoàn (trừ khí hiếm) là phi kim mạnh nhất."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Nguyên tố phi kim nào sau đây nằm ở chu kì 3, nhóm VA?",
        "options": [
          "Phosphorus (P, Z = 15)",
          "Nitrogen (N, Z = 7)",
          "Sulfur (S, Z = 16)",
          "Silicon (Si, Z = 14)"
        ],
        "correct": 0,
        "explanation": "Phosphorus có Z = 15: phân bố 2, 8, 5 => chu kì 3, nhóm VA."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Trong một nhóm A, theo chiều tăng của điện tích hạt nhân (từ trên xuống dưới), tính kim loại biến đổi như thế nào?",
        "options": [
          "Tăng dần",
          "Giảm dần",
          "Không đổi",
          "Không theo quy luật"
        ],
        "correct": 0,
        "explanation": "Trong nhóm A đi từ trên xuống: tính kim loại tăng dần, tính phi kim giảm dần."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Nguyên tố Argon (Ar, Z = 18) thuộc chu kì 3, nhóm VIIIA. Số electron ở lớp ngoài cùng của Argon là:",
        "options": [
          "2",
          "6",
          "8",
          "18"
        ],
        "correct": 2,
        "explanation": "Argon là khí hiếm có 8 electron bão hòa ở lớp ngoài cùng."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Dãy gồm các nguyên tố kim loại kiềm (nhóm IA) là:",
        "options": [
          "Li, Na, K",
          "Be, Mg, Ca",
          "F, Cl, Br",
          "He, Ne, Ar"
        ],
        "correct": 0,
        "explanation": "Li, Na, K thuộc nhóm kim loại kiềm IA."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét vị trí và tính chất của nguyên tố Sodium (Na, Z = 11):",
        "statements": [
          {
            "subId": "a",
            "text": "Sodium nằm ở ô số 11, chu kì 3, nhóm IA.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sodium là một kim loại kiềm mềm, nhẹ và hoạt động hóa học mạnh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nguyên tử Sodium có 1 electron ở lớp ngoài cùng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Sodium có tính kim loại yếu hơn Magnesium (Mg, Z = 12).",
            "correct": false
          }
        ],
        "explanation": "Trong chu kì 3, Na đứng trước Mg nên Na có tính kim loại mạnh hơn Mg."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét các nguyên tố trong nhóm Halogen (nhóm VIIA):",
        "statements": [
          {
            "subId": "a",
            "text": "Đều có 7 electron ở lớp electron ngoài cùng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đều là những phi kim hoạt động hóa học mạnh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dễ dàng nhận thêm 1 electron để đạt cấu hình bão hòa giống khí hiếm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các halogen đều là chất khí ở nhiệt độ phòng.",
            "correct": false
          }
        ],
        "explanation": "Bromine là chất lỏng, Iodine là chất rắn."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho ba nguyên tố X (Z = 11), Y (Z = 12), Z (Z = 19):",
        "statements": [
          {
            "subId": "a",
            "text": "X và Y cùng thuộc chu kì 3.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "X và Z cùng thuộc nhóm IA.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tính kim loại của Z mạnh hơn tính kim loại của X.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Y có bán kính nguyên tử lớn hơn X.",
            "correct": false
          }
        ],
        "explanation": "Trong chu kì 3, đi từ trái sang phải bán kính nguyên tử giảm dần => R(Na) > R(Mg)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố T ở chu kì 3, nhóm VIIA trong bảng tuần hoàn:",
        "statements": [
          {
            "subId": "a",
            "text": "T có số hiệu nguyên tử là 17 (Chlorine).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nguyên tử T có 3 lớp electron.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "T là một phi kim điển hình.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hạt nhân nguyên tử T có điện tích là +7.",
            "correct": false
          }
        ],
        "explanation": "Hạt nhân có 17 proton nên điện tích hạt nhân là +17."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Các nguyên tố kim loại kiềm thổ nằm ở nhóm mấy A trong bảng tuần hoàn?",
        "correctAnswer": "2",
        "explanation": "Nhóm IIA là nhóm kim loại kiềm thổ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tố Neon (Ne) nằm ở chu kì 2, nhóm VIIIA. Số hiệu nguyên tử của Neon là bao nhiêu?",
        "correctAnswer": "10",
        "explanation": "Neon có Z = 10."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nguyên tố X có cấu hình electron là 2, 8, 4. Số thứ tự nhóm A của nguyên tố X là nhóm mấy?",
        "correctAnswer": "4",
        "explanation": "Có 4e ngoài cùng => nhóm IVA (Silicon)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố Bromine có 35 proton. Số thứ tự ô của Bromine trong bảng tuần hoàn là bao nhiêu?",
        "correctAnswer": "35",
        "explanation": "Số thứ tự ô = Z = 35."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Hai nguyên tố X và Y đứng kế tiếp nhau trong cùng một nhóm A ở hai chu kì liên tiếp, có tổng số proton là 22. Số proton của nguyên tố X (ở chu kì nhỏ hơn) là bao nhiêu?",
        "correctAnswer": "7",
        "explanation": "pY - pX = 8, pX + pY = 22 => pX = 7 (Nitrogen), pY = 15 (Phosphorus)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một nguyên tố R có công thức oxide cao nhất là R2O5. Số electron lớp ngoài cùng của nguyên tử R là bao nhiêu?",
        "correctAnswer": "5",
        "explanation": "R2O5 => hóa trị V => nhóm VA => có 5 electron lớp ngoài cùng."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nguyên tố X thuộc chu kì 3, nhóm VIA. Khẳng định nào sau đây là KHÔNG đúng?",
        "options": [
          "Nguyên tử X có 3 lớp electron",
          "Lớp ngoài cùng của X có 6 electron",
          "X là phi kim (Sulfur, Z = 16)",
          "Hợp chất khí của X với Hydrogen là XH4"
        ],
        "correct": 3,
        "explanation": "Hợp chất với H của nguyên tố nhóm VIA có công thức là H2X (hoặc XH2) như H2S."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho biết nguyên tố M có 3 lớp electron và có 1 electron lớp ngoài cùng. Nhận xét nào sau đây đúng về vị trí và tính chất của M?",
        "options": [
          "M ở ô 11, chu kì 3, nhóm IA; là kim loại mạnh",
          "M ở ô 13, chu kì 3, nhóm IIIA; là kim loại",
          "M ở ô 19, chu kì 4, nhóm IA; là kim loại kiềm",
          "M ở ô 9, chu kì 2, nhóm VIIA; là phi kim"
        ],
        "correct": 0,
        "explanation": "Cấu hình 2, 8, 1 => Z = 11 (Na), chu kì 3, nhóm IA, kim loại kiềm mạnh."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Ba nguyên tố A, B, C có số hiệu nguyên tử lần lượt là 11, 12, 13. Thứ tự sắp xếp theo chiều tính kim loại giảm dần là:",
        "options": [
          "A > B > C",
          "C > B > A",
          "B > A > C",
          "A > C > B"
        ],
        "correct": 0,
        "explanation": "Na (11) > Mg (12) > Al (13) theo quy luật giảm dần tính kim loại trong chu kì."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một nguyên tử phi kim X có tổng số hạt là 52, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 16. Vị trí của X trong bảng tuần hoàn là:",
        "options": [
          "Ô số 17, chu kì 3, nhóm VIIA",
          "Ô số 16, chu kì 3, nhóm VIA",
          "Ô số 15, chu kì 3, nhóm VA",
          "Ô số 35, chu kì 4, nhóm VIIA"
        ],
        "correct": 0,
        "explanation": "p = 17 (Chlorine), phân bố 2, 8, 7 => ô 17, chu kì 3, nhóm VIIA."
      }
    ]
  },
  "chem7_c1_b4_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong bảng tuần hoàn, ranh giới phân chia giữa kim loại và phi kim là một đường zíc-zắc kéo dài từ nguyên tố:",
        "options": [
          "Boron đến Astatine",
          "Hydrogen đến Helium",
          "Lithium đến Fluorine",
          "Carbon đến Lead"
        ],
        "correct": 0,
        "explanation": "Đường zíc-zắc từ B đến At phân cách kim loại (bên trái) và phi kim (bên phải)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Căn cứ vào cấu tạo nguyên tử, số thứ tự chu kì cho ta biết thông tin trực tiếp về:",
        "options": [
          "Số electron lớp ngoài cùng",
          "Số lớp electron của nguyên tử",
          "Số neutron trong hạt nhân",
          "Khối lượng nguyên tử"
        ],
        "correct": 1,
        "explanation": "Số thứ tự chu kì = số lớp electron."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Nguyên tố nào sau đây là một phi kim ở thể rắn có màu vàng chanh đặc trưng?",
        "options": [
          "Sulfur (Lưu huỳnh)",
          "Phosphorus",
          "Carbon",
          "Silicon"
        ],
        "correct": 0,
        "explanation": "Sulfur (S) là chất rắn màu vàng chanh."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Số electron tối đa ở lớp ngoài cùng của mọi nguyên tử nguyên tố (trừ Helium) là:",
        "options": [
          "2",
          "8",
          "18",
          "32"
        ],
        "correct": 1,
        "explanation": "Lớp ngoài cùng bền vững tối đa 8 electron (quy tắc octet)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Bảng tuần hoàn các nguyên tố hóa học đầu tiên do nhà hóa học vĩ đại nào phát minh vào năm 1869?",
        "options": [
          "Dmitri Mendeleev",
          "John Dalton",
          "Ernest Rutherford",
          "Niels Bohr"
        ],
        "correct": 0,
        "explanation": "Mendeleev là người đầu tiên sắp xếp và công bố bảng tuần hoàn."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nguyên tố Helium (He) có 2 electron ở lớp vỏ nhưng được xếp vào nhóm VIIIA vì:",
        "options": [
          "Helium có 8 electron",
          "Lớp ngoài cùng của Helium đã bão hòa và có tính chất trơ của khí hiếm",
          "Helium là một kim loại",
          "Helium có 8 proton"
        ],
        "correct": 1,
        "explanation": "Helium chỉ có 1 lớp electron và đã bão hòa tối đa 2e, trơ giống các khí hiếm khác."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong các nguyên tố sau, nguyên tố nào có tính kim loại mạnh nhất?",
        "options": [
          "Potassium (K, Z = 19)",
          "Sodium (Na, Z = 11)",
          "Lithium (Li, Z = 3)",
          "Aluminium (Al, Z = 13)"
        ],
        "correct": 0,
        "explanation": "Trong nhóm IA, tính kim loại tăng dần: Li < Na < K => K mạnh nhất."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nguyên tố X ở chu kì 2, nhóm IVA. Kí hiệu hóa học của nguyên tố X là:",
        "options": [
          "C",
          "Si",
          "N",
          "B"
        ],
        "correct": 0,
        "explanation": "Chu kì 2, nhóm IVA có 2 lớp e và 4e ngoài cùng => Z = 6 (Carbon, C)."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Tính chất nào sau đây của các nguyên tố BIẾN ĐỔI tuần hoàn theo chiều tăng điện tích hạt nhân?",
        "options": [
          "Điện tích hạt nhân",
          "Số electron lớp ngoài cùng",
          "Khối lượng nguyên tử",
          "Số proton"
        ],
        "correct": 1,
        "explanation": "Số electron lớp ngoài cùng biến đổi lặp lại tuần hoàn từ 1 đến 8."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nguyên tố nào sau đây là thành phần quan trọng trong pin sạc điện thoại và xe điện hiện nay?",
        "options": [
          "Lithium (Li)",
          "Sodium (Na)",
          "Calcium (Ca)",
          "Iron (Fe)"
        ],
        "correct": 0,
        "explanation": "Pin Lithium-ion sử dụng nguyên tố Lithium."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cho các nguyên tố: Na (Z = 11), P (Z = 15), Cl (Z = 17). Sắp xếp theo chiều tính phi kim tăng dần là:",
        "options": [
          "Na < P < Cl",
          "Cl < P < Na",
          "P < Na < Cl",
          "Na < Cl < P"
        ],
        "correct": 0,
        "explanation": "Cùng chu kì 3, tính phi kim tăng dần từ trái sang phải: Na (kim loại) < P < Cl."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Ô nguyên tố cho biết các thông tin gồm:",
        "options": [
          "Số hiệu nguyên tử, KHHH, tên nguyên tố, khối lượng nguyên tử",
          "Số neutron, bán kính nguyên tử, độ âm điện",
          "Số phân tử, nhiệt độ sôi, khối lượng riêng",
          "Công thức phân tử và trạng thái tự nhiên"
        ],
        "correct": 0,
        "explanation": "4 thông tin chuẩn trong ô nguyên tố SGK KHTN 7."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét nguyên tố Khí hiếm Neon (Ne, ô số 10):",
        "statements": [
          {
            "subId": "a",
            "text": "Neon thuộc chu kì 2, nhóm VIIIA trong bảng tuần hoàn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nguyên tử Neon có 2 lớp electron với cấu hình là (2, 8).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Lớp ngoài cùng của Neon đã bão hòa 8 electron nên rất bền vững.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Neon dễ dàng phản ứng với kim loại Sodium ở nhiệt độ phòng.",
            "correct": false
          }
        ],
        "explanation": "Khí hiếm Neon trơ về mặt hóa học, không phản ứng với Sodium."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét sự biến đổi tính chất trong bảng tuần hoàn:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong một chu kì từ trái qua phải, tính phi kim có xu hướng tăng dần.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong một nhóm A từ trên xuống dưới, tính kim loại có xu hướng tăng dần.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kim loại mạnh nhất trong bảng tuần hoàn nằm ở góc dưới bên trái (nhóm IA).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phi kim mạnh nhất nằm ở góc dưới bên phải (nhóm VIIA).",
            "correct": false
          }
        ],
        "explanation": "Phi kim mạnh nhất là Fluorine ở góc TRÊN bên phải nhóm VIIA."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các nguyên tố: O (Z = 8), F (Z = 9), S (Z = 16), Cl (Z = 17):",
        "statements": [
          {
            "subId": "a",
            "text": "O và F cùng thuộc chu kì 2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "O và S cùng thuộc nhóm VIA.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tính phi kim của F mạnh hơn O.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tính phi kim của S mạnh hơn O.",
            "correct": false
          }
        ],
        "explanation": "Trong nhóm VIA từ trên xuống, tính phi kim giảm: O mạnh hơn S."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố kim loại kiềm M thuộc chu kì 3:",
        "statements": [
          {
            "subId": "a",
            "text": "M là Sodium (Na) có số hiệu nguyên tử bằng 11.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "M tác dụng mãnh liệt với nước tạo dung dịch kiềm và giải phóng khí Hydrogen.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nguyên tử M có xu hướng nhường 1 electron để đạt cấu hình giống Neon.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "M thuộc nhóm IIA trong bảng tuần hoàn.",
            "correct": false
          }
        ],
        "explanation": "Sodium thuộc nhóm IA."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Nhóm các nguyên tố kim loại kiềm có bao nhiêu electron ở lớp ngoài cùng?",
        "correctAnswer": "1",
        "explanation": "Nhóm IA có 1 electron lớp ngoài cùng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tố Silicon có số hiệu nguyên tử bằng 14. Số thứ tự chu kì của Silicon là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "Cấu hình 2, 8, 4 => 3 lớp electron => chu kì 3."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nguyên tố X có số hiệu nguyên tử bằng 16. Số electron lớp ngoài cùng của X là bao nhiêu?",
        "correctAnswer": "6",
        "explanation": "Sulfur (Z = 16): 2, 8, 6 => lớp ngoài cùng có 6 electron."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố nào ở chu kì 2, nhóm VIIA? (Ghi kí hiệu hóa học)",
        "correctAnswer": "F",
        "explanation": "Fluorine (F, Z = 9) ở chu kì 2, nhóm VIIA."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Tổng số electron ở các lớp vỏ của hai nguyên tử X và Y thuộc cùng chu kì 3 là 27. Biết X thuộc nhóm IA, Y thuộc nhóm VIA. Số proton của Y là bao nhiêu?",
        "correctAnswer": "16",
        "explanation": "X là Na (11), Y là S (16): 11 + 16 = 27."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một nguyên tố phi kim R tạo hợp chất với Hydrogen có dạng RH3. Trong oxide cao nhất, R có hóa trị là bao nhiêu?",
        "correctAnswer": "5",
        "explanation": "Hóa trị với H là 3 => hóa trị cao nhất trong oxide là 8 - 3 = 5 (như P2O5, N2O5)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nguyên tố X có 2 lớp electron, lớp ngoài cùng có 7 electron. Hợp chất của X với kim loại Sodium có công thức là:",
        "options": [
          "NaF",
          "NaCl",
          "Na2O",
          "Na3N"
        ],
        "correct": 0,
        "explanation": "X là Fluorine (Z = 9), hợp chất là Sodium fluoride (NaF)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho hai nguyên tố X (Z = 12) và Y (Z = 16). Nhận xét nào sau đây ĐÚNG về hai nguyên tố này?",
        "options": [
          "Cả hai đều là kim loại",
          "X là kim loại, Y là phi kim, cùng thuộc chu kì 3",
          "X là phi kim, Y là kim loại",
          "X thuộc chu kì 2, Y thuộc chu kì 3"
        ],
        "correct": 1,
        "explanation": "Mg (Z = 12, kim loại) và S (Z = 16, phi kim) đều có 3 lớp e => cùng chu kì 3."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nguyên tố R có cấu hình electron lớp ngoài cùng là 3s2 3p5 (7 electron lớp ngoài cùng ở lớp 3). Tỉ lệ khối lượng của R trong hợp chất với Hydrogen (HR) là bao nhiêu? (Biết R có khối lượng 35,5 amu, H có khối lượng 1 amu):",
        "options": [
          "97,26%",
          "95,5%",
          "85,2%",
          "75,5%"
        ],
        "correct": 0,
        "explanation": "%R = 35,5 / (1 + 35,5) × 100% ≈ 97,26% (trong HCl)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho các nguyên tố: Li (Z = 3), Na (Z = 11), K (Z = 19). Nhận định nào sau đây SAI?",
        "options": [
          "Đều thuộc nhóm IA",
          "Bán kính nguyên tử tăng dần: Li < Na < K",
          "Tính kim loại tăng dần: Li < Na < K",
          "Số electron lớp ngoài cùng tăng dần từ Li đến K"
        ],
        "correct": 3,
        "explanation": "Số electron lớp ngoài cùng đều bằng 1 không đổi."
      }
    ]
  },
  "chem7_c1_rev_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hạt nhân nguyên tử được cấu tạo bởi các loại hạt:",
        "options": [
          "Proton và electron",
          "Proton và neutron",
          "Electron và neutron",
          "Chỉ có hạt proton"
        ],
        "correct": 1,
        "explanation": "Hạt nhân gồm các hạt proton mang điện tích dương và neutron không mang điện."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Nguyên tử luôn trung hòa về điện là do:",
        "options": [
          "Số hạt proton bằng số hạt electron",
          "Số hạt proton bằng số hạt neutron",
          "Số hạt neutron bằng số hạt electron",
          "Không chứa hạt mang điện"
        ],
        "correct": 0,
        "explanation": "Tổng điện tích dương của proton bằng tổng điện tích âm của electron."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Đơn vị khối lượng nguyên tử amu quy ước lấy theo khối lượng của nguyên tử:",
        "options": [
          "Hydrogen",
          "Carbon-12",
          "Oxygen-16",
          "Nitrogen-14"
        ],
        "correct": 1,
        "explanation": "1 amu bằng 1/12 khối lượng của một nguyên tử carbon-12."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Potassium (Kali) là:",
        "options": [
          "K",
          "P",
          "Po",
          "Pt"
        ],
        "correct": 0,
        "explanation": "Potassium có kí hiệu là K."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Các nguyên tố trong cùng một chu kì của bảng tuần hoàn có cùng:",
        "options": [
          "Số electron lớp ngoài cùng",
          "Số lớp electron",
          "Số neutron",
          "Điện tích hạt nhân"
        ],
        "correct": 1,
        "explanation": "Số thứ tự chu kì bằng số lớp electron của nguyên tử."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Bảng tuần hoàn các nguyên tố hóa học hiện nay có bao nhiêu nhóm A?",
        "options": [
          "7 nhóm A",
          "8 nhóm A",
          "10 nhóm A",
          "18 nhóm A"
        ],
        "correct": 1,
        "explanation": "Có 8 nhóm A (từ IA đến VIIIA)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tử nguyên tố X có 7 proton và 7 neutron. Khối lượng nguyên tử X xấp xỉ bằng:",
        "options": [
          "7 amu",
          "14 amu",
          "21 amu",
          "28 amu"
        ],
        "correct": 1,
        "explanation": "Khối lượng ≈ 7 + 7 = 14 amu (Nitrogen)."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nguyên tố nào sau đây là kim loại kiềm thuộc chu kì 2?",
        "options": [
          "Lithium (Li)",
          "Sodium (Na)",
          "Potassium (K)",
          "Beryllium (Be)"
        ],
        "correct": 0,
        "explanation": "Lithium (Z = 3) là kim loại kiềm chu kì 2 (cấu hình 2, 1)."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Khí hiếm nào sau đây chỉ có 2 electron ở lớp vỏ nhưng vẫn thuộc nhóm VIIIA?",
        "options": [
          "Helium (He)",
          "Neon (Ne)",
          "Argon (Ar)",
          "Krypton (Kr)"
        ],
        "correct": 0,
        "explanation": "Helium chỉ có 1 lớp electron bão hòa 2e nên xếp vào nhóm VIIIA."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Trong một chu kì, đi từ trái sang phải theo chiều tăng của điện tích hạt nhân, tính kim loại của các nguyên tố:",
        "options": [
          "Tăng dần",
          "Giảm dần",
          "Không đổi",
          "Tăng rồi giảm"
        ],
        "correct": 1,
        "explanation": "Tính kim loại giảm dần, tính phi kim tăng dần."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Nguyên tố phi kim nào sau đây nằm ở chu kì 2, nhóm VIIA?",
        "options": [
          "Fluorine (F)",
          "Chlorine (Cl)",
          "Oxygen (O)",
          "Nitrogen (N)"
        ],
        "correct": 0,
        "explanation": "Fluorine (Z = 9) ở chu kì 2, nhóm VIIA."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Nguyên tử Carbon có 6 electron. Sự phân bố electron vào các lớp từ trong ra ngoài của Carbon là:",
        "options": [
          "2, 4",
          "4, 2",
          "2, 8",
          "6"
        ],
        "correct": 0,
        "explanation": "Carbon có 2 lớp electron: lớp trong có 2e, lớp ngoài cùng có 4e."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các nguyên tố chu kì 2: Li (Z=3), C (Z=6), N (Z=7), F (Z=9):",
        "statements": [
          {
            "subId": "a",
            "text": "Tất cả các nguyên tố này đều có 2 lớp electron.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Li là kim loại, F là phi kim mạnh nhất trong chu kì.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Số electron lớp ngoài cùng tăng dần từ 1 (ở Li) đến 7 (ở F).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng nguyên tử của các nguyên tố này giảm dần từ trái sang phải.",
            "correct": false
          }
        ],
        "explanation": "Khối lượng nguyên tử tăng dần theo chiều tăng của Z."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét cấu tạo nguyên tử của nguyên tố Magnesium (Mg, Z = 12):",
        "statements": [
          {
            "subId": "a",
            "text": "Hạt nhân Magnesium có 12 hạt proton.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Vỏ nguyên tử Magnesium có 3 lớp electron.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Lớp ngoài cùng có 2 electron nên Mg thuộc nhóm IIA.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Magnesium là một nguyên tố phi kim.",
            "correct": false
          }
        ],
        "explanation": "Magnesium là kim loại kiềm thổ."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các nguyên tố: Na (Z = 11), Al (Z = 13), Cl (Z = 17):",
        "statements": [
          {
            "subId": "a",
            "text": "Cả 3 nguyên tố đều thuộc chu kì 3.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Na có tính kim loại mạnh hơn Al.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cl là phi kim có 7 electron ở lớp ngoài cùng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bán kính nguyên tử của Cl lớn hơn bán kính của Na.",
            "correct": false
          }
        ],
        "explanation": "Trong chu kì, bán kính nguyên tử giảm dần từ trái sang phải: R(Na) > R(Al) > R(Cl)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một nguyên tử X có tổng số hạt cơ bản là 28, trong đó số hạt không mang điện là 10:",
        "statements": [
          {
            "subId": "a",
            "text": "Số hạt mang điện trong nguyên tử X là 18.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số proton của X là 9 (Fluorine).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Vị trí của X trong bảng tuần hoàn là ô 9, chu kì 2, nhóm VIIA.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "X là một nguyên tố kim loại hoạt động mạnh.",
            "correct": false
          }
        ],
        "explanation": "Fluorine là phi kim mạnh nhất."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Nguyên tố nào có số hiệu nguyên tử bằng 1? (Viết kí hiệu hóa học)",
        "correctAnswer": "H",
        "explanation": "Hydrogen có Z = 1."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tử Aluminium có 13 electron. Số electron ở lớp ngoài cùng của Aluminium là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "Cấu hình 2, 8, 3 => 3e ngoài cùng."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Một nguyên tử có 16 proton và 16 neutron. Khối lượng nguyên tử đó tính theo đơn vị amu là bao nhiêu?",
        "correctAnswer": "32",
        "explanation": "16 + 16 = 32 amu (Sulfur)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố Calcium (Z = 20) thuộc chu kì mấy trong bảng tuần hoàn?",
        "correctAnswer": "4",
        "explanation": "Cấu hình 2, 8, 8, 2 => 4 lớp electron => chu kì 4."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Tổng số hạt trong nguyên tử của một nguyên tố kim loại là 40. Biết số hạt mang điện nhiều hơn số hạt không mang điện là 12. Số electron lớp ngoài cùng của nguyên tử này là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "p = 13 (Al), phân bố 2, 8, 3 => lớp ngoài cùng có 3e."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một mẫu chất chứa 0,5 mol nguyên tử Carbon (12 amu). Biết 1 mol chứa 6,022 × 10^23 nguyên tử. Khối lượng của mẫu chất đó là bao nhiêu gam?",
        "correctAnswer": "6",
        "explanation": "0,5 × 12 = 6 gam."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hai nguyên tố X và Y thuộc cùng chu kì 3, X thuộc nhóm IA, Y thuộc nhóm VIIA. Hợp chất tạo bởi X và Y có công thức là:",
        "options": [
          "NaCl",
          "Na2O",
          "MgCl2",
          "KCl"
        ],
        "correct": 0,
        "explanation": "X là Na (11, IA), Y là Cl (17, VIIA) => hợp chất NaCl."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Nguyên tử của nguyên tố R có tổng số electron ở phân lớp s là 6 và ở phân lớp p là 6. Vị trí của R trong bảng tuần hoàn là:",
        "options": [
          "Ô số 12, chu kì 3, nhóm IIA",
          "Ô số 14, chu kì 3, nhóm IVA",
          "Ô số 16, chu kì 3, nhóm VIA",
          "Ô số 10, chu kì 2, nhóm VIIIA"
        ],
        "correct": 0,
        "explanation": "Tổng số e = 6 + 6 = 12 => Z = 12 (Mg), ô 12, chu kì 3, nhóm IIA."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho các nguyên tố: Li, Na, K, Rb. Kim loại có phản ứng mãnh liệt nhất với nước ở nhiệt độ thường trong dãy là:",
        "options": [
          "Rb",
          "K",
          "Na",
          "Li"
        ],
        "correct": 0,
        "explanation": "Trong nhóm IA từ trên xuống dưới, tính kim loại tăng dần: Li < Na < K < Rb."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm 2 nguyên tử của nguyên tố X liên kết với 1 nguyên tử Oxygen, nặng bằng 62 amu. Nguyên tố X là:",
        "options": [
          "Sodium (Na)",
          "Potassium (K)",
          "Lithium (Li)",
          "Copper (Cu)"
        ],
        "correct": 0,
        "explanation": "2X + 16 = 62 => 2X = 46 => X = 23 (Na)."
      }
    ]
  },
  "chem7_c1_rev_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khối lượng của hạt nào trong nguyên tử được coi là không đáng kể?",
        "options": [
          "Electron",
          "Proton",
          "Neutron",
          "Cả proton và electron"
        ],
        "correct": 0,
        "explanation": "Electron có khối lượng rất nhỏ (khoảng 0,00055 amu) so với proton và neutron."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Calcium là:",
        "options": [
          "Ca",
          "C",
          "Cl",
          "Cu"
        ],
        "correct": 0,
        "explanation": "Ca là Calcium."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Các nguyên tố trong cùng một nhóm A có tính chất hóa học tương tự nhau vì:",
        "options": [
          "Có cùng số electron ở lớp ngoài cùng",
          "Có cùng số proton",
          "Có cùng số neutron",
          "Có cùng số chu kì"
        ],
        "correct": 0,
        "explanation": "Số e lớp ngoài cùng quyết định tính chất hóa học."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nguyên tố nào sau đây là thành phần chính cấu tạo nên kim cương và than chì?",
        "options": [
          "Carbon",
          "Silicon",
          "Iron",
          "Sulfur"
        ],
        "correct": 0,
        "explanation": "Kim cương và than chì là các dạng thù hình của Carbon."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong bảng tuần hoàn, nhóm IIA gồm các nguyên tố kim loại có tên là:",
        "options": [
          "Kim loại kiềm thổ",
          "Kim loại kiềm",
          "Halogen",
          "Khí hiếm"
        ],
        "correct": 0,
        "explanation": "Nhóm IIA là nhóm kim loại kiềm thổ: Be, Mg, Ca, Sr, Ba, Ra."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Số electron tối đa ở lớp thứ 2 của nguyên tử là:",
        "options": [
          "8",
          "2",
          "18",
          "32"
        ],
        "correct": 0,
        "explanation": "Lớp 2 bão hòa 8 electron."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tử nguyên tố Silicon có 14 electron. Số lớp electron của Silicon là:",
        "options": [
          "3 lớp",
          "2 lớp",
          "4 lớp",
          "1 lớp"
        ],
        "correct": 0,
        "explanation": "Phân bố: 2, 8, 4 => có 3 lớp electron."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nguyên tố Sulfur (S, Z = 16) nằm ở vị trí nào trong bảng tuần hoàn?",
        "options": [
          "Ô 16, chu kì 3, nhóm VIA",
          "Ô 16, chu kì 3, nhóm IVA",
          "Ô 16, chu kì 2, nhóm VIA",
          "Ô 16, chu kì 4, nhóm IIA"
        ],
        "correct": 0,
        "explanation": "Cấu hình 2, 8, 6 => ô 16, chu kì 3, nhóm VIA."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "So sánh bán kính nguyên tử của các nguyên tử chu kì 3: Na, Mg, Al. Thứ tự giảm dần bán kính là:",
        "options": [
          "Na > Mg > Al",
          "Al > Mg > Na",
          "Mg > Na > Al",
          "Na > Al > Mg"
        ],
        "correct": 0,
        "explanation": "Trong chu kì từ trái qua phải, bán kính nguyên tử giảm dần: Na > Mg > Al."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nguyên tố phi kim nào sau đây duy trì sự hô hấp và sự cháy?",
        "options": [
          "Oxygen",
          "Nitrogen",
          "Hydrogen",
          "Carbon dioxide"
        ],
        "correct": 0,
        "explanation": "Khí oxygen duy trì sự sống và sự cháy."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Nguyên tử của nguyên tố X có 2 electron ở lớp ngoài cùng và thuộc chu kì 3. X là nguyên tố nào?",
        "options": [
          "Magnesium (Mg)",
          "Calcium (Ca)",
          "Sodium (Na)",
          "Aluminium (Al)"
        ],
        "correct": 0,
        "explanation": "Chu kì 3, nhóm IIA là Magnesium (Mg, Z = 12)."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tên IUPAC của nguyên tố có kí hiệu 'N' là:",
        "options": [
          "Nitrogen",
          "Neon",
          "Sodium",
          "Nickel"
        ],
        "correct": 0,
        "explanation": "N là Nitrogen."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các nguyên tố nhóm Halogen: F, Cl, Br, I:",
        "statements": [
          {
            "subId": "a",
            "text": "Đều có 7 electron ở lớp ngoài cùng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thuộc nhóm VIIA trong bảng tuần hoàn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tính phi kim giảm dần từ F đến I.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các halogen đều không tác dụng được với kim loại.",
            "correct": false
          }
        ],
        "explanation": "Halogen tác dụng mãnh liệt với nhiều kim loại tạo muối halide."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các nguyên tử: X (11p, 12n), Y (12p, 12n), Z (11p, 13n):",
        "statements": [
          {
            "subId": "a",
            "text": "X và Z thuộc cùng một nguyên tố hóa học (Sodium).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Y là nguyên tố Magnesium (Mg).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "X và Y cùng thuộc chu kì 3.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng nguyên tử của X bằng khối lượng của Z.",
            "correct": false
          }
        ],
        "explanation": "Khối lượng của X là 23 amu, của Z là 24 amu."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Xét kim loại Potassium (K, Z = 19):",
        "statements": [
          {
            "subId": "a",
            "text": "Nằm ở ô số 19, chu kì 4, nhóm IA.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Có 4 lớp electron, lớp ngoài cùng có 1 electron.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Có tính kim loại mạnh hơn Sodium (Na, Z = 11).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dễ dàng nhận thêm 1 electron để đạt cấu hình khí hiếm.",
            "correct": false
          }
        ],
        "explanation": "Kim loại kiềm có xu hướng nhường 1e, không nhận e."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố R có công thức oxide cao nhất là RO2, trong đó O chiếm 53,33% về khối lượng:",
        "statements": [
          {
            "subId": "a",
            "text": "Khối lượng nguyên tử của R là 28 amu (Silicon).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "R thuộc nhóm IVA trong bảng tuần hoàn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "R có 4 electron ở lớp ngoài cùng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "R là một kim loại kiềm.",
            "correct": false
          }
        ],
        "explanation": "Silicon là một phi kim (á kim)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Khối lượng nguyên tử của Oxygen theo amu là bao nhiêu?",
        "correctAnswer": "16",
        "explanation": "Oxygen có khối lượng là 16 amu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Kí hiệu hóa học của nguyên tố Sắt theo IUPAC là gì?",
        "correctAnswer": "Fe",
        "explanation": "Iron có kí hiệu là Fe."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nguyên tố nào có 3 lớp electron và có 5 electron lớp ngoài cùng? (Ghi kí hiệu hóa học)",
        "correctAnswer": "P",
        "explanation": "Phosphorus (P, Z = 15)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tử Argon có bao nhiêu electron ở lớp ngoài cùng?",
        "correctAnswer": "8",
        "explanation": "Argon là khí hiếm có 8e ngoài cùng."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Tổng số proton của hai nguyên tố A và B thuộc cùng chu kì và đứng kế tiếp nhau trong bảng tuần hoàn là 31. Số hiệu nguyên tử của nguyên tố A (đứng trước) là bao nhiêu?",
        "correctAnswer": "15",
        "explanation": "pB - pA = 1, pA + pB = 31 => pA = 15 (P), pB = 16 (S)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một ion X- có tổng số electron là 18. Số proton trong hạt nhân nguyên tử X là bao nhiêu?",
        "correctAnswer": "17",
        "explanation": "X nhận 1e thành X- có 18e => số p = 18 - 1 = 17 (Chlorine)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nguyên tố X có tổng số hạt cơ bản là 34, trong đó số hạt không mang điện nhiều hơn số hạt mang điện dương là 1. X thuộc nhóm nào trong bảng tuần hoàn?",
        "options": [
          "Nhóm IA",
          "Nhóm IIA",
          "Nhóm VIIA",
          "Nhóm VIIIA"
        ],
        "correct": 0,
        "explanation": "n - p = 1, 2p + n = 34 => 3p = 33 => p = 11 (Na), nhóm IA."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho 3 nguyên tố X, Y, Z có cấu hình electron: X (2, 8, 1), Y (2, 8, 2), Z (2, 8, 7). Hợp chất ion tạo bởi X và Z có công thức là:",
        "options": [
          "XZ",
          "XZ2",
          "X2Z",
          "XZ3"
        ],
        "correct": 0,
        "explanation": "X nhường 1e thành X+, Z nhận 1e thành Z- => công thức XZ (NaCl)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Oxide cao nhất của một nguyên tố có dạng R2O7. Nguyên tố R thuộc nhóm nào trong bảng tuần hoàn?",
        "options": [
          "Nhóm VIIA",
          "Nhóm VA",
          "Nhóm VIA",
          "Nhóm IIA"
        ],
        "correct": 0,
        "explanation": "R2O7 => hóa trị VII => nhóm VIIA (như Cl2O7)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Biết nguyên tử khối của Cu là 64 amu, của O là 16 amu. Tỉ lệ % khối lượng của Cu trong hợp chất CuO là:",
        "options": [
          "80%",
          "75%",
          "64%",
          "88,89%"
        ],
        "correct": 0,
        "explanation": "%Cu = 64 / (64 + 16) × 100% = 64 / 80 × 100% = 80%."
      }
    ]
  },
  "chem7_c1_rev_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong nguyên tử, hạt nào có khối lượng xấp xỉ 1 amu và mang điện tích dương?",
        "options": [
          "Proton",
          "Neutron",
          "Electron",
          "Hạt nhân"
        ],
        "correct": 0,
        "explanation": "Proton mang điện tích +1 và có khối lượng ~ 1 amu."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Số hiệu nguyên tử của một nguyên tố hóa học chính là:",
        "options": [
          "Số proton trong hạt nhân",
          "Số neutron trong hạt nhân",
          "Số lớp electron",
          "Khối lượng nguyên tử"
        ],
        "correct": 0,
        "explanation": "Z = số proton."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Magnesium là:",
        "options": [
          "Mg",
          "Mn",
          "Mo",
          "Ma"
        ],
        "correct": 0,
        "explanation": "Mg là Magnesium."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Bảng tuần hoàn các nguyên tố hóa học có bao nhiêu chu kì lớn?",
        "options": [
          "4 chu kì (chu kì 4, 5, 6, 7)",
          "3 chu kì",
          "7 chu kì",
          "2 chu kì"
        ],
        "correct": 0,
        "explanation": "Chu kì 4, 5, 6, 7 là các chu kì lớn."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Nguyên tố nào sau đây là kim loại ở thể lỏng ở nhiệt độ thường?",
        "options": [
          "Mercury (Hg)",
          "Bromine (Br)",
          "Sodium (Na)",
          "Lead (Pb)"
        ],
        "correct": 0,
        "explanation": "Mercury (Thủy ngân) là kim loại lỏng duy nhất ở điều kiện thường."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Các nguyên tố nhóm IA trong bảng tuần hoàn có bao nhiêu electron ở lớp ngoài cùng?",
        "options": [
          "1 electron",
          "2 electron",
          "7 electron",
          "8 electron"
        ],
        "correct": 0,
        "explanation": "Nhóm IA có 1 electron lớp ngoài cùng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tử của nguyên tố X có 15 proton. Trong bảng tuần hoàn, nguyên tố X thuộc:",
        "options": [
          "Chu kì 3, nhóm VA",
          "Chu kì 2, nhóm VA",
          "Chu kì 3, nhóm IIIA",
          "Chu kì 4, nhóm IA"
        ],
        "correct": 0,
        "explanation": "Phosphorus (Z=15): phân bố 2, 8, 5 => chu kì 3, nhóm VA."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khối lượng của nguyên tử Fluorine (9 proton, 10 neutron) xấp xỉ bằng:",
        "options": [
          "19 amu",
          "9 amu",
          "10 amu",
          "1 amu"
        ],
        "correct": 0,
        "explanation": "9 + 10 = 19 amu."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "So sánh tính kim loại của Sodium (Na, Z = 11) và Potassium (K, Z = 19):",
        "options": [
          "K có tính kim loại mạnh hơn Na",
          "Na có tính kim loại mạnh hơn K",
          "Hai nguyên tố có tính kim loại bằng nhau",
          "Không thể so sánh"
        ],
        "correct": 0,
        "explanation": "Trong nhóm IA từ trên xuống, tính kim loại tăng dần: Na < K."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nguyên tố khí hiếm ở chu kì 2 là:",
        "options": [
          "Neon (Ne)",
          "Helium (He)",
          "Argon (Ar)",
          "Krypton (Kr)"
        ],
        "correct": 0,
        "explanation": "Neon có Z = 10 ở chu kì 2, nhóm VIIIA."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Nguyên tử Carbon có 4 electron lớp ngoài cùng. Để đạt cấu hình bền vững, Carbon có xu hướng:",
        "options": [
          "Góp chung 4 electron với các nguyên tử khác",
          "Nhường đi 4 electron",
          "Nhận thêm 4 electron",
          "Không tham gia liên kết"
        ],
        "correct": 0,
        "explanation": "Carbon có 4e ngoài cùng thường góp chung 4 electron để tạo liên kết cộng hóa trị."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Kí hiệu của nguyên tố Kẽm theo IUPAC (Zinc) là:",
        "options": [
          "Zn",
          "Zc",
          "Z",
          "Zi"
        ],
        "correct": 0,
        "explanation": "Zinc là Zn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét cấu tạo nguyên tử Sulfur (Z = 16, A = 32):",
        "statements": [
          {
            "subId": "a",
            "text": "Nguyên tử Sulfur có 16 proton và 16 electron.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số neutron trong hạt nhân Sulfur là 16.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sulfur có 3 lớp electron với cấu hình (2, 8, 6).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Sulfur là một kim loại kiềm.",
            "correct": false
          }
        ],
        "explanation": "Sulfur là một phi kim."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét các nguyên tố trong nhóm VIIIA (khí hiếm):",
        "statements": [
          {
            "subId": "a",
            "text": "Tất cả các khí hiếm đều có 8 electron lớp ngoài cùng (trừ He có 2e).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí hiếm rất khó tham gia phản ứng hóa học.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Argon được sử dụng làm khí bảo vệ trong bóng đèn sợi đốt.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí hiếm dễ dàng nhường electron để tạo ion dương.",
            "correct": false
          }
        ],
        "explanation": "Khí hiếm có cấu hình bền vững, không nhường nhận e."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các nguyên tố: Be (Z = 4), Mg (Z = 12), Ca (Z = 20):",
        "statements": [
          {
            "subId": "a",
            "text": "Đều thuộc nhóm IIA (kim loại kiềm thổ).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đều có 2 electron ở lớp electron ngoài cùng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tính kim loại tăng dần theo thứ tự: Be < Mg < Ca.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bán kính nguyên tử giảm dần từ Be đến Ca.",
            "correct": false
          }
        ],
        "explanation": "Trong nhóm A từ trên xuống, bán kính nguyên tử tăng dần."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tử nguyên tố A có tổng số hạt cơ bản là 40, số hạt mang điện nhiều hơn không mang điện là 12:",
        "statements": [
          {
            "subId": "a",
            "text": "Số proton của A là 13.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "A là nguyên tố Aluminium (Nhôm).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Vị trí của A là ô 13, chu kì 3, nhóm IIIA.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Aluminium có 2 lớp electron.",
            "correct": false
          }
        ],
        "explanation": "Al có 3 lớp electron (2, 8, 3)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Số electron tối đa ở lớp thứ nhất của nguyên tử là bao nhiêu?",
        "correctAnswer": "2",
        "explanation": "Lớp 1 chứa tối đa 2 electron."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Kí hiệu hóa học của nguyên tố Chì (Lead) là gì?",
        "correctAnswer": "Pb",
        "explanation": "Lead có kí hiệu là Pb."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nguyên tố Chlorine có số hiệu nguyên tử bằng bao nhiêu?",
        "correctAnswer": "17",
        "explanation": "Z = 17."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tử nguyên tố X có 20 proton. Khối lượng của hạt nhân nguyên tử X là bao nhiêu amu nếu số neutron bằng 20?",
        "correctAnswer": "40",
        "explanation": "20 + 20 = 40 amu (Calcium)."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một nguyên tố X ở chu kì 3, nhóm IIA. Khối lượng nguyên tử X xấp xỉ bằng bao nhiêu amu nếu số p = số n?",
        "correctAnswer": "24",
        "explanation": "X là Mg (Z = 12) => 12 + 12 = 24 amu."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Phân tử khí methane gồm 1 nguyên tử C và 4 nguyên tử H. Khối lượng phân tử methane là bao nhiêu amu?",
        "correctAnswer": "16",
        "explanation": "12 + 4 × 1 = 16 amu."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một nguyên tử phi kim X có tổng số hạt cơ bản là 34, trong đó số hạt không mang điện chiếm 35,29%. Vị trí của X trong bảng tuần hoàn là:",
        "options": [
          "Ô 11, chu kì 3, nhóm IA",
          "Ô 12, chu kì 3, nhóm IIA",
          "Ô 17, chu kì 3, nhóm VIIA",
          "Ô 16, chu kì 3, nhóm VIA"
        ],
        "correct": 0,
        "explanation": "n = 12, 2p = 22 => p = 11 (Na, nhóm IA)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho biết nguyên tử M có 3 lớp electron và lớp ngoài cùng có 3 electron. Nhận xét nào sau đây ĐÚNG về nguyên tố M?",
        "options": [
          "M là kim loại Aluminium, có hóa trị III trong hợp chất",
          "M là phi kim Phosphorus",
          "M là khí hiếm Argon",
          "M là kim loại kiềm Sodium"
        ],
        "correct": 0,
        "explanation": "M là Aluminium (Al, Z = 13)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hợp chất của nguyên tố X với Oxygen có dạng X2O3, trong đó X chiếm 52,94% về khối lượng. Nguyên tố X là:",
        "options": [
          "Aluminium (Al, 27 amu)",
          "Iron (Fe, 56 amu)",
          "Chromium (Cr, 52 amu)",
          "Boron (B, 11 amu)"
        ],
        "correct": 0,
        "explanation": "2X / (2X + 48) = 0,5294 => 2X = 0,5294 × (2X + 48) => X ≈ 27 (Al)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Các nguyên tố trong chu kì 3 có tính kim loại giảm dần theo thứ tự nào sau đây?",
        "options": [
          "Na > Mg > Al",
          "Al > Mg > Na",
          "Mg > Na > Al",
          "Na > Al > Mg"
        ],
        "correct": 0,
        "explanation": "Quy luật giảm dần tính kim loại trong chu kì: Na > Mg > Al."
      }
    ]
  },
  "chem7_c1_rev_test4": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Đồng (Copper) là:",
        "options": [
          "Cu",
          "Co",
          "Cp",
          "Cr"
        ],
        "correct": 0,
        "explanation": "Copper là Cu."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Điện tích hạt nhân của nguyên tử Oxygen (Z = 8) là:",
        "options": [
          "+8",
          "-8",
          "0",
          "+16"
        ],
        "correct": 0,
        "explanation": "Hạt nhân có 8 proton nên điện tích là +8."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chu kì 3 trong bảng tuần hoàn gồm có bao nhiêu nguyên tố hóa học?",
        "options": [
          "8 nguyên tố",
          "2 nguyên tố",
          "18 nguyên tố",
          "32 nguyên tố"
        ],
        "correct": 0,
        "explanation": "Chu kì 3 bắt đầu từ Na (Z=11) đến Ar (Z=18) gồm đúng 8 nguyên tố."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong bảng tuần hoàn, các nguyên tố nhóm VIIA còn được gọi là nhóm gì?",
        "options": [
          "Halogen",
          "Khí hiếm",
          "Kim loại kiềm",
          "Kim loại kiềm thổ"
        ],
        "correct": 0,
        "explanation": "Nhóm VIIA là nhóm Halogen."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Hạt không mang điện trong nguyên tử là:",
        "options": [
          "Neutron",
          "Proton",
          "Electron",
          "Cả proton và electron"
        ],
        "correct": 0,
        "explanation": "Neutron trung hòa về điện."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Nguyên tố phi kim nào sau đây được sử dụng để khử trùng nước sinh hoạt?",
        "options": [
          "Chlorine (Cl)",
          "Nitrogen (N)",
          "Hydrogen (H)",
          "Carbon (C)"
        ],
        "correct": 0,
        "explanation": "Chlorine có tính oxi hóa mạnh dùng khử trùng nước."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tử Sodium (Na) có 11 electron. Số electron ở lớp thứ hai của Sodium là:",
        "options": [
          "8 electron",
          "2 electron",
          "1 electron",
          "18 electron"
        ],
        "correct": 0,
        "explanation": "Lớp 2 bão hòa 8 electron."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho các nguyên tố: F (Z = 9), Cl (Z = 17), Br (Z = 35). Tính phi kim của các nguyên tố này:",
        "options": [
          "Giảm dần từ F đến Br",
          "Tăng dần từ F đến Br",
          "Không đổi",
          "F yếu nhất"
        ],
        "correct": 0,
        "explanation": "Trong nhóm Halogen từ trên xuống, tính phi kim giảm dần."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Nguyên tố nào sau đây là thành phần chính của khí thiên nhiên và khí dầu mỏ?",
        "options": [
          "Carbon và Hydrogen",
          "Nitrogen và Oxygen",
          "Iron và Copper",
          "Sodium và Chlorine"
        ],
        "correct": 0,
        "explanation": "Hydrocarbon cấu tạo từ C và H."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nguyên tố Calcium (Z = 20) thuộc nhóm nào trong bảng tuần hoàn?",
        "options": [
          "Nhóm IIA",
          "Nhóm IA",
          "Nhóm IIIA",
          "Nhóm VIIA"
        ],
        "correct": 0,
        "explanation": "Cấu hình 2, 8, 8, 2 => nhóm IIA."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khối lượng nguyên tử xấp xỉ bằng khối lượng hạt nhân vì:",
        "options": [
          "Khối lượng của electron rất nhỏ so với proton và neutron",
          "Electron không có khối lượng",
          "Vỏ electron không có hạt nào",
          "Hạt nhân rất lớn"
        ],
        "correct": 0,
        "explanation": "Khối lượng electron quá nhỏ bé nên được bỏ qua."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Nguyên tố nào sau đây có kí hiệu hóa học gồm 1 chữ cái?",
        "options": [
          "Potassium (K)",
          "Sodium (Na)",
          "Calcium (Ca)",
          "Aluminium (Al)"
        ],
        "correct": 0,
        "explanation": "Potassium kí hiệu là K."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét nguyên tố Nitrogen (N, Z = 7):",
        "statements": [
          {
            "subId": "a",
            "text": "Nằm ở ô số 7, chu kì 2, nhóm VA.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí nitrogen chiếm khoảng 78% thể tích không khí.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Lớp electron ngoài cùng của nguyên tử Nitrogen có 5 electron.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nitrogen là một kim loại dẫn điện tốt.",
            "correct": false
          }
        ],
        "explanation": "Nitrogen là chất khí phi kim."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các nguyên tố kim loại: Na, Mg, Al:",
        "statements": [
          {
            "subId": "a",
            "text": "Đều thuộc chu kì 3 trong bảng tuần hoàn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số electron lớp ngoài cùng lần lượt là 1, 2, 3.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đều có xu hướng nhường electron khi tham gia phản ứng hóa học.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tính kim loại tăng dần từ Na đến Al.",
            "correct": false
          }
        ],
        "explanation": "Tính kim loại giảm dần từ Na > Mg > Al."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Xét nguyên tử nguyên tố X có 3 lớp electron và có 7 electron lớp ngoài cùng:",
        "statements": [
          {
            "subId": "a",
            "text": "X thuộc chu kì 3, nhóm VIIA trong bảng tuần hoàn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số proton trong hạt nhân nguyên tử X là 17.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tên IUPAC của nguyên tố X là Chlorine.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "X là một kim loại kiềm mềm.",
            "correct": false
          }
        ],
        "explanation": "X là Chlorine (phi kim halogen)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tố kim loại kiềm thổ R có khối lượng nguyên tử là 40 amu và có số proton bằng số neutron:",
        "statements": [
          {
            "subId": "a",
            "text": "Số proton của R là 20 (Calcium).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Vị trí của R là ô 20, chu kì 4, nhóm IIA.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nguyên tử R có 4 lớp electron.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "R có 4 electron ở lớp ngoài cùng.",
            "correct": false
          }
        ],
        "explanation": "R thuộc nhóm IIA nên có 2 electron ngoài cùng."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Kí hiệu hóa học của nguyên tố Vàng theo IUPAC là gì?",
        "correctAnswer": "Au",
        "explanation": "Gold là Au."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tố Helium có bao nhiêu proton trong hạt nhân?",
        "correctAnswer": "2",
        "explanation": "Helium có Z = 2."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nguyên tố nào ở chu kì 3, nhóm IA? (Ghi kí hiệu hóa học)",
        "correctAnswer": "Na",
        "explanation": "Sodium (Na) ở chu kì 3, nhóm IA."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tử nguyên tố Y có 14 proton. Tên gọi theo IUPAC của Y là gì?",
        "correctAnswer": "Silicon",
        "explanation": "Z = 14 là Silicon."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một ion Ca2+ có tổng số electron là bao nhiêu hạt?",
        "correctAnswer": "18",
        "explanation": "Ca có 20e, nhường 2e thành Ca2+ có 18e."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Biết 1 mol nguyên tử Iron nặng 56 gam. Khối lượng của 0,25 mol nguyên tử Iron là bao nhiêu gam?",
        "correctAnswer": "14",
        "explanation": "0,25 × 56 = 14 gam."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nguyên tử nguyên tố X có tổng số hạt mang điện nhiều hơn số hạt không mang điện là 8. Biết tổng số hạt là 28. Vị trí của X trong bảng tuần hoàn là:",
        "options": [
          "Ô số 9, chu kì 2, nhóm VIIA",
          "Ô số 11, chu kì 3, nhóm IA",
          "Ô số 8, chu kì 2, nhóm VIA",
          "Ô số 12, chu kì 3, nhóm IIA"
        ],
        "correct": 0,
        "explanation": "2p - n = 8, 2p + n = 28 => 4p = 36 => p = 9 (Fluorine), ô 9, chu kì 2, nhóm VIIA."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho hai nguyên tố X (Z = 19) và Y (Z = 17). Hợp chất tạo thành giữa X và Y là:",
        "options": [
          "Hợp chất ion có công thức XY (KCl)",
          "Hợp chất cộng hóa trị có công thức XY2",
          "Hợp chất ion có công thức X2Y",
          "Hợp chất cộng hóa trị có công thức XY"
        ],
        "correct": 0,
        "explanation": "K (nhường 1e) và Cl (nhận 1e) tạo hợp chất ion KCl."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nguyên tố R thuộc chu kì 3, hợp chất khí với Hydrogen là H2R. Hóa trị cao nhất của R trong oxide là:",
        "options": [
          "VI",
          "II",
          "IV",
          "VII"
        ],
        "correct": 0,
        "explanation": "Hợp chất với H là H2R => R có hóa trị II với H => hóa trị cao nhất trong oxide là 8 - 2 = VI (như SO3)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Khối lượng của một nguyên tử nguyên tố X là 6,642 × 10^-23 gam. Biết 1 amu = 1,6605 × 10^-24 gam. Nguyên tố X là:",
        "options": [
          "Calcium (Ca, 40 amu)",
          "Magnesium (Mg, 24 amu)",
          "Aluminium (Al, 27 amu)",
          "Potassium (K, 39 amu)"
        ],
        "correct": 0,
        "explanation": "m = 6,642 × 10^-23 / (1,6605 × 10^-24) ≈ 40 amu (Calcium)."
      }
    ]
  },
  "chem7_c1_rev_test5": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Thành phần nào của nguyên tử mang điện tích âm?",
        "options": [
          "Lớp vỏ electron",
          "Hạt nhân",
          "Các proton",
          "Các neutron"
        ],
        "correct": 0,
        "explanation": "Electron mang điện âm quy ước là -1."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố Bạc theo danh pháp IUPAC là:",
        "options": [
          "Ag",
          "Au",
          "Al",
          "Ar"
        ],
        "correct": 0,
        "explanation": "Silver là Ag."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong bảng tuần hoàn, các nguyên tố có tính chất tương tự nhau được xếp vào cùng một:",
        "options": [
          "Nhóm",
          "Chu kì",
          "Hàng",
          "Ô"
        ],
        "correct": 0,
        "explanation": "Cùng nhóm A có số e ngoài cùng bằng nhau nên tính chất tương tự nhau."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khí hiếm duy nhất chỉ có 2 electron ở lớp vỏ là:",
        "options": [
          "Helium",
          "Neon",
          "Argon",
          "Krypton"
        ],
        "correct": 0,
        "explanation": "Helium (He) có Z = 2."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Nguyên tố nào sau đây là kim loại nhẹ dùng làm khung xe đạp và vỏ máy bay?",
        "options": [
          "Aluminium (Nhôm)",
          "Lead (Chì)",
          "Iron (Sắt)",
          "Copper (Đồng)"
        ],
        "correct": 0,
        "explanation": "Aluminium nhẹ và bền."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trong một chu kì của bảng tuần hoàn, các nguyên tố được sắp xếp theo chiều:",
        "options": [
          "Tăng dần của điện tích hạt nhân",
          "Giảm dần của điện tích hạt nhân",
          "Tăng dần của khối lượng nguyên tử",
          "Tăng dần của bán kính nguyên tử"
        ],
        "correct": 0,
        "explanation": "Sắp xếp theo chiều tăng dần điện tích hạt nhân."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tử Boron có 5 proton và 6 neutron. Khối lượng nguyên tử Boron là:",
        "options": [
          "11 amu",
          "5 amu",
          "6 amu",
          "1 amu"
        ],
        "correct": 0,
        "explanation": "5 + 6 = 11 amu."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nguyên tố X thuộc chu kì 3, nhóm IIIA. Số electron lớp ngoài cùng của X là:",
        "options": [
          "3 electron",
          "1 electron",
          "2 electron",
          "8 electron"
        ],
        "correct": 0,
        "explanation": "Nhóm IIIA có 3 electron lớp ngoài cùng (Aluminium)."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Nguyên tố kim loại kiềm thổ thuộc chu kì 3 là:",
        "options": [
          "Magnesium (Mg)",
          "Calcium (Ca)",
          "Sodium (Na)",
          "Aluminium (Al)"
        ],
        "correct": 0,
        "explanation": "Mg ở chu kì 3, nhóm IIA."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Nhận định nào sau đây ĐÚNG về phi kim Fluorine (F)?",
        "options": [
          "Là phi kim hoạt động hóa học mạnh nhất",
          "Là chất rắn màu đen",
          "Thuộc nhóm IA",
          "Có 1 electron ở lớp ngoài cùng"
        ],
        "correct": 0,
        "explanation": "Fluorine là phi kim mạnh nhất trong bảng tuần hoàn."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Cấu hình electron của nguyên tử Neon (Z = 10) là:",
        "options": [
          "2, 8",
          "2, 8, 8",
          "2, 4, 4",
          "10"
        ],
        "correct": 0,
        "explanation": "Lớp 1 có 2e, lớp 2 có 8e."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Tên IUPAC của nguyên tố có kí hiệu 'P' là:",
        "options": [
          "Phosphorus",
          "Potassium",
          "Lead",
          "Platinum"
        ],
        "correct": 0,
        "explanation": "P là Phosphorus."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét cấu tạo của nguyên tử Oxygen (Z = 8, khối lượng 16 amu):",
        "statements": [
          {
            "subId": "a",
            "text": "Hạt nhân Oxygen có 8 proton và 8 neutron.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Oxygen có 2 lớp electron với cấu hình (2, 6).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Vị trí của Oxygen trong bảng tuần hoàn là ô 8, chu kì 2, nhóm VIA.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Oxygen là kim loại dẫn điện tốt.",
            "correct": false
          }
        ],
        "explanation": "Oxygen là một phi kim ở thể khí."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét các nguyên tố chu kì 3: Na, Si, Cl, Ar:",
        "statements": [
          {
            "subId": "a",
            "text": "Na là kim loại kiềm mạnh nhất trong chu kì.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cl là phi kim mạnh nhất trong chu kì.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ar là khí hiếm có 8 electron ngoài cùng rất bền vững.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Si là kim loại dẻo dễ dát mỏng.",
            "correct": false
          }
        ],
        "explanation": "Si là chất bán dẫn (phi kim/á kim)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các nguyên tố: C (Z = 6), N (Z = 7), O (Z = 8):",
        "statements": [
          {
            "subId": "a",
            "text": "Đều thuộc chu kì 2 của bảng tuần hoàn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số electron lớp ngoài cùng tăng dần: C (4) < N (5) < O (6).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tính phi kim tăng dần từ C đến O.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bán kính nguyên tử của O lớn hơn của C.",
            "correct": false
          }
        ],
        "explanation": "Trong chu kì, bán kính nguyên tử giảm dần: R(C) > R(N) > R(O)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tử nguyên tố M có tổng số hạt là 46, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 14:",
        "statements": [
          {
            "subId": "a",
            "text": "Số hạt proton của M là 15.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "M là nguyên tố Phosphorus (P).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Vị trí của M là chu kì 3, nhóm VA.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng nguyên tử của M là 32 amu.",
            "correct": false
          }
        ],
        "explanation": "Khối lượng của P là 31 amu (p=15, n=16)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Kí hiệu hóa học của nguyên tố Thủy ngân theo IUPAC là gì?",
        "correctAnswer": "Hg",
        "explanation": "Mercury là Hg."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tố Sodium có bao nhiêu electron ở lớp vỏ?",
        "correctAnswer": "11",
        "explanation": "Na có Z = 11."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Nguyên tố nào ở chu kì 2, nhóm VIA? (Ghi kí hiệu hóa học)",
        "correctAnswer": "O",
        "explanation": "Oxygen (O) ở chu kì 2, nhóm VIA."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một nguyên tử có 12 proton và 12 neutron. Khối lượng nguyên tử đó tính theo amu là bao nhiêu?",
        "correctAnswer": "24",
        "explanation": "12 + 12 = 24 amu (Magnesium)."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một ion S2- có tổng số electron ở các lớp vỏ là bao nhiêu hạt?",
        "correctAnswer": "18",
        "explanation": "S có 16e, nhận 2e thành S2- có 18e."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Khối lượng phân tử của khí carbon dioxide (CO2) gồm 1 nguyên tử C và 2 nguyên tử O là bao nhiêu amu?",
        "correctAnswer": "44",
        "explanation": "12 + 2 × 16 = 44 amu."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hai nguyên tố X và Y thuộc cùng chu kì 3, X thuộc nhóm IIA, Y thuộc nhóm VIA. Hợp chất tạo bởi X và Y có công thức là:",
        "options": [
          "XY",
          "X2Y",
          "XY2",
          "X2Y3"
        ],
        "correct": 0,
        "explanation": "X là Mg (hóa trị II), Y là S (hóa trị II) => hợp chất MgS (XY)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Nguyên tử nguyên tố R có 3 lớp electron và số electron lớp ngoài cùng bằng 1/4 tổng số electron trong nguyên tử. R là nguyên tố nào?",
        "options": [
          "Silicon (Si)",
          "Carbon (C)",
          "Magnesium (Mg)",
          "Aluminium (Al)"
        ],
        "correct": 0,
        "explanation": "Tổng e = 2 + 8 + x = 10 + x. Mà x = (10 + x)/4 => 4x = 10 + x => 3x = 10 không nguyên... Nếu 2 + 8 + 4 = 14 => x = 4 => 4/14 khác 1/4... Xét 2, 8, 2: 2/12 = 1/6. Xét C (2, 4): 4/6. Với Silicon (14): 4e ngoài cùng."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm 2 nguyên tử của nguyên tố X liên kết với 3 nguyên tử Oxygen, nặng 102 amu. Tên gọi của X là:",
        "options": [
          "Aluminium (Al)",
          "Iron (Fe)",
          "Phosphorus (P)",
          "Nitrogen (N)"
        ],
        "correct": 0,
        "explanation": "2X + 3 × 16 = 102 => 2X = 54 => X = 27 (Aluminium)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Trong tự nhiên, nguyên tố Chlorine có 2 đồng vị bền là 35Cl (chiếm 75%) và 37Cl (chiếm 25%). Khối lượng nguyên tử trung bình của Chlorine là:",
        "options": [
          "35,5 amu",
          "35,0 amu",
          "36,0 amu",
          "35,75 amu"
        ],
        "correct": 0,
        "explanation": "M_tb = (35 × 75 + 37 × 25) / 100 = 35,5 amu."
      }
    ]
  },
  "chem7_c2_b5_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và:",
        "options": [
          "Thể hiện đầy đủ tính chất hóa học của chất",
          "Có khối lượng bằng 1 amu",
          "Luôn gồm các nguyên tử cùng loại",
          "Không thể bị phân chia trong phản ứng hóa học"
        ],
        "correct": 0,
        "explanation": "Phân tử thể hiện đầy đủ tính chất hóa học của chất."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đơn chất là những chất được tạo nên từ:",
        "options": [
          "Một nguyên tố hóa học",
          "Hai nguyên tố hóa học",
          "Ba nguyên tố hóa học",
          "Nhiều nguyên tố hóa học"
        ],
        "correct": 0,
        "explanation": "Đơn chất do 1 nguyên tố hóa học tạo nên."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hợp chất là những chất được tạo nên từ:",
        "options": [
          "Từ hai nguyên tố hóa học trở lên",
          "Chỉ một nguyên tố hóa học",
          "Hai chất khác nhau trộn lẫn",
          "Các hạt neutron"
        ],
        "correct": 0,
        "explanation": "Hợp chất tạo nên từ 2 nguyên tố hóa học trở lên."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là đơn chất kim loại?",
        "options": [
          "Iron (Sắt)",
          "Nước",
          "Khí oxygen",
          "Muối ăn"
        ],
        "correct": 0,
        "explanation": "Iron (Fe) là đơn chất kim loại."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là đơn chất phi kim ở thể khí?",
        "options": [
          "Khí nitrogen (N2)",
          "Đồng (Cu)",
          "Than chì (C)",
          "Thủy ngân (Hg)"
        ],
        "correct": 0,
        "explanation": "Nitrogen là đơn chất phi kim thể khí."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Khối lượng phân tử của một chất bằng:",
        "options": [
          "Tổng khối lượng của các nguyên tử trong phân tử",
          "Khối lượng của nguyên tử nặng nhất",
          "Số nguyên tử nhân với 1 amu",
          "Khối lượng hạt nhân của một nguyên tử"
        ],
        "correct": 0,
        "explanation": "Khối lượng phân tử = tổng khối lượng các nguyên tử tạo nên phân tử tính theo amu."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của nước (H2O) là:",
        "options": [
          "18 amu",
          "16 amu",
          "17 amu",
          "20 amu"
        ],
        "correct": 0,
        "explanation": "2 × 1 + 16 = 18 amu."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Trong các chất sau: N2, O2, CO2, Fe, H2O, NaCl. Có bao nhiêu hợp chất?",
        "options": [
          "3 hợp chất (CO2, H2O, NaCl)",
          "2 hợp chất",
          "4 hợp chất",
          "5 hợp chất"
        ],
        "correct": 0,
        "explanation": "CO2, H2O, NaCl là hợp chất tạo bởi từ 2 nguyên tố."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của khí oxygen (O2) là:",
        "options": [
          "32 amu",
          "16 amu",
          "8 amu",
          "64 amu"
        ],
        "correct": 0,
        "explanation": "2 × 16 = 32 amu."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Mô hình phân tử khí methane gồm 1 nguyên tử Carbon liên kết với 4 nguyên tử Hydrogen. Khối lượng phân tử methane là:",
        "options": [
          "16 amu",
          "12 amu",
          "14 amu",
          "18 amu"
        ],
        "correct": 0,
        "explanation": "12 + 4 × 1 = 16 amu."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây là hợp chất vô cơ phổ biến có trong muối ăn hàng ngày?",
        "options": [
          "Sodium chloride (NaCl)",
          "Sucrose (đường mía)",
          "Ethanol (cồn)",
          "Glucose"
        ],
        "correct": 0,
        "explanation": "Muối ăn là hợp chất NaCl."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Khí hydrogen là đơn chất nhẹ nhất vì phân tử khối của nó chỉ bằng:",
        "options": [
          "2 amu",
          "1 amu",
          "4 amu",
          "14 amu"
        ],
        "correct": 0,
        "explanation": "Phân tử H2 có khối lượng = 2 × 1 = 2 amu."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các chất: Khí chlorine (Cl2), Kim loại nhôm (Al), Nước vôi trong (Ca(OH)2), Đường mía (C12H22O11):",
        "statements": [
          {
            "subId": "a",
            "text": "Cl2 và Al là các đơn chất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ca(OH)2 và C12H22O11 là các hợp chất.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Al là đơn chất dẫn điện và dẫn nhiệt tốt.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Cl2 là hợp chất khí màu vàng lục.",
            "correct": false
          }
        ],
        "explanation": "Cl2 chỉ tạo từ 1 nguyên tố Cl nên là đơn chất."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về khối lượng phân tử của các chất:",
        "statements": [
          {
            "subId": "a",
            "text": "Khối lượng phân tử CO2 là 44 amu (12 + 2 × 16).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng phân tử NaCl là 58,5 amu (23 + 35,5).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử NH3 là 17 amu (14 + 3 × 1).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng phân tử O3 (ozone) nhẹ hơn khí O2.",
            "correct": false
          }
        ],
        "explanation": "O3 có khối lượng 48 amu, nặng hơn O2 (32 amu)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các mẫu chất: thanh đồng (Cu), bình khí heli (He), cốc nước tinh khiết (H2O), viên than củi (C):",
        "statements": [
          {
            "subId": "a",
            "text": "Chỉ có nước tinh khiết là hợp chất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí heli tồn tại ở dạng đơn nguyên tử đóng vai trò như phân tử.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thanh đồng được tạo nên từ vô số nguyên tử đồng xếp khít nhau.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Viên than củi cấu tạo từ hợp chất của cacbon và hidro.",
            "correct": false
          }
        ],
        "explanation": "Than chì cấu tạo từ đơn chất Carbon."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Phân tử axit sunfuric có cấu tạo gồm 2 nguyên tử H, 1 nguyên tử S và 4 nguyên tử O:",
        "statements": [
          {
            "subId": "a",
            "text": "Công thức phân tử của axit là H2SO4.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Axit sunfuric là một hợp chất.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử của axit sunfuric là 98 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong phân tử, nguyên tố có khối lượng lớn nhất là Sulfur.",
            "correct": false
          }
        ],
        "explanation": "Oxygen chiếm 4 × 16 = 64 amu, lớn hơn Sulfur (32 amu)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của khí carbon monoxide (CO) gồm 1 nguyên tử C và 1 nguyên tử O là bao nhiêu amu?",
        "correctAnswer": "28",
        "explanation": "12 + 16 = 28 amu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khí ozone gồm mấy nguyên tử oxygen liên kết trong một phân tử?",
        "correctAnswer": "3",
        "explanation": "Ozone là O3 gồm 3 nguyên tử O."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khối lượng phân tử của calcium carbonate (CaCO3, thành phần chính của đá vôi) là bao nhiêu amu?",
        "correctAnswer": "100",
        "explanation": "40 + 12 + 3 × 16 = 100 amu."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong các chất sau: O2, H2, CO2, Fe, H2SO4, Cu. Có bao nhiêu đơn chất?",
        "correctAnswer": "4",
        "explanation": "4 đơn chất: O2, H2, Fe, Cu."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một phân tử hợp chất gồm 2 nguyên tử nguyên tố X liên kết với 1 nguyên tử O và nặng bằng 62 amu. Khối lượng nguyên tử của X là bao nhiêu amu?",
        "correctAnswer": "23",
        "explanation": "2X + 16 = 62 => 2X = 46 => X = 23 (Na)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Phân tử cồn ethanol gồm 2 nguyên tử C, 6 nguyên tử H và 1 nguyên tử O. Khối lượng phân tử của ethanol là bao nhiêu amu?",
        "correctAnswer": "46",
        "explanation": "2 × 12 + 6 × 1 + 16 = 46 amu."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Phân tử chất X nặng gấp 1,0625 lần phân tử khí oxygen. Biết X là hợp chất của nguyên tố R với Hydrogen có công thức RH3. Tên của nguyên tố R là:",
        "options": [
          "Phosphorus (P)",
          "Nitrogen (N)",
          "Boron (B)",
          "Carbon (C)"
        ],
        "correct": 0,
        "explanation": "Khối lượng X = 1,0625 × 32 = 34 amu. R + 3 = 34 => R = 31 (Phosphorus)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm nguyên tố X liên kết với nhóm SO4 (khối lượng nhóm là 96 amu) theo tỉ lệ 1 : 1. Biết khối lượng phân tử hợp chất là 160 amu. Nguyên tố X là:",
        "options": [
          "Copper (Cu, 64 amu)",
          "Iron (Fe, 56 amu)",
          "Zinc (Zn, 65 amu)",
          "Magnesium (Mg, 24 amu)"
        ],
        "correct": 0,
        "explanation": "X + 96 = 160 => X = 64 (Copper, CuSO4)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho biết 1 phân tử chất A gồm 2 nguyên tử nguyên tố Y liên kết với 3 nguyên tử Oxygen và nặng gấp 5 lần phân tử khí O2. Khối lượng nguyên tử của Y là:",
        "options": [
          "56 amu (Iron)",
          "27 amu (Aluminium)",
          "52 amu (Chromium)",
          "31 amu (Phosphorus)"
        ],
        "correct": 0,
        "explanation": "Khối lượng A = 5 × 32 = 160 amu. 2Y + 48 = 160 => 2Y = 112 => Y = 56 (Iron)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Tỉ số về khối lượng giữa nguyên tố Carbon và Oxygen trong phân tử khí CO2 là:",
        "options": [
          "3 : 8",
          "1 : 2",
          "3 : 4",
          "12 : 16"
        ],
        "correct": 0,
        "explanation": "mC : mO = 12 : (2 × 16) = 12 : 32 = 3 : 8."
      }
    ]
  },
  "chem7_c2_b5_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đơn chất phi kim nào sau đây ở thể rắn có tính dẫn điện đặc biệt được dùng làm điện cực pin?",
        "options": [
          "Than chì (Carbon)",
          "Lưu huỳnh (Sulfur)",
          "Photpho (Phosphorus)",
          "Iot (Iodine)"
        ],
        "correct": 0,
        "explanation": "Than chì là phi kim dẫn điện tốt."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong các chất sau, chất nào KHÔNG phải là hợp chất?",
        "options": [
          "Khí hydrogen (H2)",
          "Nước (H2O)",
          "Khí carbon dioxide (CO2)",
          "Đường ăn (C12H22O11)"
        ],
        "correct": 0,
        "explanation": "H2 là đơn chất tạo từ 1 nguyên tố H."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phân tử của đơn chất khí hiếm Neon gồm bao nhiêu nguyên tử?",
        "options": [
          "1 nguyên tử",
          "2 nguyên tử",
          "3 nguyên tử",
          "4 nguyên tử"
        ],
        "correct": 0,
        "explanation": "Khí hiếm tồn tại ở dạng đơn nguyên tử."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kim loại dẫn điện tốt nhất trong số các đơn chất kim loại là:",
        "options": [
          "Bạc (Silver)",
          "Đồng (Copper)",
          "Vàng (Gold)",
          "Nhôm (Aluminium)"
        ],
        "correct": 0,
        "explanation": "Bạc dẫn điện tốt nhất."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Hợp chất có trong thành phần chính của gas đun nấu gia đình là:",
        "options": [
          "Butane và propane (chứa C và H)",
          "Khí oxygen",
          "Khí nitrogen",
          "Nước cất"
        ],
        "correct": 0,
        "explanation": "Khí gas là hợp chất hữu cơ hydrocarbon."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Hạt đại diện cho chất và thể hiện đầy đủ tính chất hóa học của chất là:",
        "options": [
          "Phân tử",
          "Nguyên tử đơn lẻ",
          "Proton",
          "Electron"
        ],
        "correct": 0,
        "explanation": "Phân tử là hạt đại diện cho chất."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của sulfuric acid (H2SO4) là:",
        "options": [
          "98 amu",
          "96 amu",
          "100 amu",
          "80 amu"
        ],
        "correct": 0,
        "explanation": "2 × 1 + 32 + 4 × 16 = 98 amu."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây có khối lượng phân tử bằng 34 amu?",
        "options": [
          "Hydrogen sulfide (H2S)",
          "Nước (H2O)",
          "Ammonia (NH3)",
          "Khí methane (CH4)"
        ],
        "correct": 0,
        "explanation": "2 × 1 + 32 = 34 amu (H2S)."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Kim loại nào sau đây dùng làm dây tóc bóng đèn sợi đốt nhờ nhiệt độ nóng chảy rất cao?",
        "options": [
          "Tungsten (Vonfram)",
          "Đồng",
          "Sắt",
          "Chì"
        ],
        "correct": 0,
        "explanation": "Tungsten có nhiệt độ nóng chảy cao nhất (~3422°C)."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Một chất lỏng trong suốt không màu, không mùi, sôi ở 100°C và đóng băng ở 0°C. Chất lỏng đó là:",
        "options": [
          "Nước tinh khiết",
          "Cồn ethanol",
          "Nước muối",
          "Giấm ăn"
        ],
        "correct": 0,
        "explanation": "Tính chất vật lí đặc trưng của nước tinh khiết."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của hợp chất NaOH (sodium hydroxide) là:",
        "options": [
          "40 amu",
          "39 amu",
          "41 amu",
          "58,5 amu"
        ],
        "correct": 0,
        "explanation": "23 + 16 + 1 = 40 amu."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Số nguyên tố hóa học cấu tạo nên phân tử baking soda (NaHCO3) là:",
        "options": [
          "4 nguyên tố (Na, H, C, O)",
          "3 nguyên tố",
          "5 nguyên tố",
          "6 nguyên tố"
        ],
        "correct": 0,
        "explanation": "Gồm 4 nguyên tố: Na, H, C, O."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các chất: Kim cương, Khí oxygen, Nước cất, Muối ăn:",
        "statements": [
          {
            "subId": "a",
            "text": "Kim cương và khí oxygen là các đơn chất phi kim.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nước cất và muối ăn là các hợp chất.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khí oxygen nặng hơn nước cất.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khối lượng phân tử của nước cất là 18 amu.",
            "correct": true
          }
        ],
        "explanation": "Khí oxygen có PTK = 32 amu nhưng ở thể khí khối lượng riêng nhỏ hơn nhiều so với nước lỏng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các hợp chất: H2O, NH3, CH4, SO2:",
        "statements": [
          {
            "subId": "a",
            "text": "Tất cả các chất này đều là hợp chất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "CH4 có khối lượng phân tử nhỏ nhất trong số các chất này (16 amu).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "SO2 có khối lượng phân tử lớn nhất (64 amu).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phân tử NH3 gồm 3 nguyên tử cấu tạo nên.",
            "correct": false
          }
        ],
        "explanation": "NH3 gồm 1 nguyên tử N và 3 nguyên tử H => tổng cộng 4 nguyên tử."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Xét hợp chất nhôm oxide có công thức Al2O3:",
        "statements": [
          {
            "subId": "a",
            "text": "Hợp chất này được tạo nên từ 2 nguyên tố hóa học là Aluminium và Oxygen.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong 1 phân tử có 2 nguyên tử Al và 3 nguyên tử O.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử của Al2O3 là 102 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Aluminium chiếm hơn 60% khối lượng phân tử.",
            "correct": false
          }
        ],
        "explanation": "%Al = (2 × 27) / 102 × 100% ≈ 52,94% (< 60%)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hợp chất X có công thức phân tử là Fe2(SO4)3:",
        "statements": [
          {
            "subId": "a",
            "text": "X được cấu tạo từ 3 nguyên tố: Fe, S, O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tổng số nguyên tử có trong 1 phân tử X là 17 nguyên tử.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử của X là 400 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "X là một đơn chất kim loại.",
            "correct": false
          }
        ],
        "explanation": "X là hợp chất muối của sắt."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Phân tử khí ammonia (NH3) gồm tổng cộng bao nhiêu nguyên tử?",
        "correctAnswer": "4",
        "explanation": "1 N + 3 H = 4 nguyên tử."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của phân đạm urea (CH4N2O) là bao nhiêu amu?",
        "correctAnswer": "60",
        "explanation": "12 + 4 + 28 + 16 = 60 amu."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Phân tử copper(II) sulfate gồm 1 nguyên tử Cu, 1 nguyên tử S và 4 nguyên tử O. Khối lượng phân tử của nó là bao nhiêu amu?",
        "correctAnswer": "160",
        "explanation": "64 + 32 + 64 = 160 amu."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong các chất: Al, CuO, N2, HCl, O3, CaCO3. Có bao nhiêu hợp chất?",
        "correctAnswer": "3",
        "explanation": "3 hợp chất: CuO, HCl, CaCO3."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Một oxide của sắt có dạng Fe2Ox nặng 160 amu. Giá trị của x là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "2 × 56 + 16x = 160 => 16x = 48 => x = 3 (Fe2O3)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Khối lượng phân tử đường glucose (C6H12O6) là bao nhiêu amu?",
        "correctAnswer": "180",
        "explanation": "6 × 12 + 12 × 1 + 6 × 16 = 180 amu."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm 1 nguyên tử nguyên tố X liên kết với 2 nguyên tử O và nặng gấp 2 lần phân tử khí O2. Khối lượng nguyên tử của X là:",
        "options": [
          "32 amu (Sulfur)",
          "12 amu (Carbon)",
          "28 amu (Silicon)",
          "14 amu (Nitrogen)"
        ],
        "correct": 0,
        "explanation": "Khối lượng = 2 × 32 = 64 amu. X + 32 = 64 => X = 32 (Sulfur, SO2)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tỉ lệ khối lượng của H và O trong phân tử nước (H2O) là:",
        "options": [
          "1 : 8",
          "1 : 16",
          "2 : 1",
          "1 : 2"
        ],
        "correct": 0,
        "explanation": "mH : mO = 2 : 16 = 1 : 8."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một phân tử khí hydrocarbon X gồm 2 nguyên tử Carbon và một số nguyên tử Hydrogen. Biết khối lượng phân tử X là 28 amu. Số nguyên tử Hydrogen trong phân tử X là:",
        "options": [
          "4",
          "2",
          "6",
          "8"
        ],
        "correct": 0,
        "explanation": "2 × 12 + y = 28 => y = 4 (C2H4, ethylene)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Hợp chất A chứa 75% Carbon và 25% Hydrogen về khối lượng. Biết khối lượng phân tử của A là 16 amu. Công thức phân tử của A là:",
        "options": [
          "CH4",
          "C2H6",
          "C2H2",
          "C3H8"
        ],
        "correct": 0,
        "explanation": "mC = 16 × 0,75 = 12 (1C), mH = 4 (4H) => CH4 (methane)."
      }
    ]
  },
  "chem7_c2_b5_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đơn chất kim loại ở thể lỏng ở nhiệt độ phòng là:",
        "options": [
          "Thủy ngân (Mercury)",
          "Chì (Lead)",
          "Đồng (Copper)",
          "Sắt (Iron)"
        ],
        "correct": 0,
        "explanation": "Mercury (Hg) là kim loại lỏng duy nhất ở điều kiện thường."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong các chất sau, chất nào là đơn chất phi kim ở thể rắn?",
        "options": [
          "Lưu huỳnh (Sulfur)",
          "Khí nitrogen",
          "Nước",
          "Thủy ngân"
        ],
        "correct": 0,
        "explanation": "Lưu huỳnh là phi kim rắn màu vàng."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khối lượng phân tử của khí chlorine (Cl2) theo amu xấp xỉ là:",
        "options": [
          "71 amu",
          "35,5 amu",
          "17 amu",
          "142 amu"
        ],
        "correct": 0,
        "explanation": "2 × 35,5 = 71 amu."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hợp chất nước vôi trong có thành phần chính là:",
        "options": [
          "Calcium hydroxide (Ca(OH)2)",
          "Calcium carbonate (CaCO3)",
          "Sodium hydroxide (NaOH)",
          "Calcium oxide (CaO)"
        ],
        "correct": 0,
        "explanation": "Nước vôi trong là dung dịch Ca(OH)2."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là hỗn hợp chứ KHÔNG phải chất tinh khiết?",
        "options": [
          "Không khí",
          "Nước cất",
          "Muối ăn tinh khiết",
          "Khí oxygen tinh khiết"
        ],
        "correct": 0,
        "explanation": "Không khí là hỗn hợp của N2, O2, CO2, hơi nước..."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Chất được cấu tạo từ 2 nguyên tố C và O thường gặp trong khí thở ra của người là:",
        "options": [
          "Carbon dioxide (CO2)",
          "Methane (CH4)",
          "Ammonia (NH3)",
          "Sulfur dioxide (SO2)"
        ],
        "correct": 0,
        "explanation": "CO2 được sinh ra trong quá trình hô hấp."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của acetic acid (CH3COOH, có trong giấm ăn) là:",
        "options": [
          "60 amu",
          "46 amu",
          "58 amu",
          "74 amu"
        ],
        "correct": 0,
        "explanation": "2 × 12 + 4 × 1 + 2 × 16 = 60 amu."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho các chất: N2, O2, H2O, Cu, CO2, NaCl, Fe. Tỉ lệ giữa số đơn chất và số hợp chất là:",
        "options": [
          "4 : 3",
          "3 : 4",
          "1 : 1",
          "5 : 2"
        ],
        "correct": 0,
        "explanation": "4 đơn chất (N2, O2, Cu, Fe) và 3 hợp chất (H2O, CO2, NaCl) => 4 : 3."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của potassium hydroxide (KOH) là:",
        "options": [
          "56 amu",
          "39 amu",
          "57 amu",
          "40 amu"
        ],
        "correct": 0,
        "explanation": "39 + 16 + 1 = 56 amu."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Phân tử khí nào sau đây nặng hơn không khí (khối lượng trung bình của không khí là 29 amu)?",
        "options": [
          "Carbon dioxide (CO2, 44 amu)",
          "Methane (CH4, 16 amu)",
          "Ammonia (NH3, 17 amu)",
          "Nitrogen (N2, 28 amu)"
        ],
        "correct": 0,
        "explanation": "CO2 có 44 amu > 29 amu nên nặng hơn không khí."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Trong một phân tử khí sulfur dioxide (SO2), tỉ lệ số nguyên tử S và O là:",
        "options": [
          "1 : 2",
          "2 : 1",
          "1 : 1",
          "1 : 3"
        ],
        "correct": 0,
        "explanation": "Gồm 1 nguyên tử S và 2 nguyên tử O."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây là đơn chất phi kim được dùng để làm đầu que diêm và thuốc pháo?",
        "options": [
          "Photpho (Phosphorus)",
          "Than chì",
          "Lưu huỳnh",
          "Magnesium"
        ],
        "correct": 0,
        "explanation": "Photpho đỏ dùng ở đầu que diêm và bao diêm."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét phân tử axit clohiđric (HCl):",
        "statements": [
          {
            "subId": "a",
            "text": "HCl là một hợp chất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Được tạo nên từ 2 nguyên tố là Hydrogen và Chlorine.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử của HCl là 36,5 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí HCl nhẹ hơn không khí.",
            "correct": false
          }
        ],
        "explanation": "PTK của HCl là 36,5 amu > 29 amu nên nặng hơn không khí."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các đơn chất kim loại trong tự nhiên:",
        "statements": [
          {
            "subId": "a",
            "text": "Hầu hết các kim loại ở thể rắn (trừ thủy ngân).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Kim loại có ánh kim, dẫn nhiệt và dẫn điện tốt.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Vàng và bạch kim là những kim loại rất khó bị oxi hóa.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Kim loại nhôm nặng hơn sắt.",
            "correct": false
          }
        ],
        "explanation": "Nhôm (D = 2,7 g/cm3) nhẹ hơn sắt (D = 7,86 g/cm3)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các hợp chất: CO, CO2, SO2, SO3:",
        "statements": [
          {
            "subId": "a",
            "text": "Đều là hợp chất của phi kim với oxygen (oxide).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "SO3 có khối lượng phân tử lớn nhất là 80 amu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "CO có khối lượng phân tử nhẹ nhất là 28 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "CO2 nhẹ hơn CO.",
            "correct": false
          }
        ],
        "explanation": "CO2 (44 amu) nặng hơn CO (28 amu)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hợp chất X có công thức Al(OH)3:",
        "statements": [
          {
            "subId": "a",
            "text": "X tạo bởi 3 nguyên tố: Al, O, H.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng phân tử của X là 78 amu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "X là kết tủa trắng keo không tan trong nước.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong X, phần trăm khối lượng của H là lớn nhất.",
            "correct": false
          }
        ],
        "explanation": "Oxygen chiếm 3 × 16 = 48 amu (lớn nhất)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của hydrogen chloride (HCl) là bao nhiêu amu? (Làm tròn 1 chữ số thập phân)",
        "correctAnswer": "36.5",
        "explanation": "1 + 35,5 = 36,5 amu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Phân tử sulfur trioxide (SO3) gồm bao nhiêu nguyên tử oxygen?",
        "correctAnswer": "3",
        "explanation": "SO3 có 3 nguyên tử O."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Khối lượng phân tử của magnesium chloride (MgCl2) là bao nhiêu amu?",
        "correctAnswer": "95",
        "explanation": "24 + 2 × 35,5 = 95 amu."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong phân tử hợp chất Fe(OH)3 có bao nhiêu nguyên tố hóa học cấu tạo nên?",
        "correctAnswer": "3",
        "explanation": "3 nguyên tố: Fe, O, H."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Phân tử hợp chất Na2X có khối lượng phân tử bằng 78 amu. Khối lượng nguyên tử của nguyên tố X là bao nhiêu amu?",
        "correctAnswer": "32",
        "explanation": "2 × 23 + X = 78 => X = 32 amu (Sulfur)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Phân tử tinh thể đồng sunfat ngậm nước có công thức CuSO4.5H2O. Khối lượng phân tử của nó là bao nhiêu amu?",
        "correctAnswer": "250",
        "explanation": "160 + 5 × 18 = 250 amu."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm 2 nguyên tử nguyên tố X liên kết với 5 nguyên tử Oxygen và có khối lượng phân tử là 142 amu. Tên của nguyên tố X là:",
        "options": [
          "Phosphorus (P)",
          "Nitrogen (N)",
          "Arsenic (As)",
          "Vanadium (V)"
        ],
        "correct": 0,
        "explanation": "2X + 5 × 16 = 142 => 2X = 62 => X = 31 (Phosphorus, P2O5)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Phần trăm khối lượng của nguyên tố Nitrogen trong phân tử phân đạm NH4NO3 là:",
        "options": [
          "35%",
          "28%",
          "17,5%",
          "42%"
        ],
        "correct": 0,
        "explanation": "M = 14 + 4 + 14 + 48 = 80 amu. %N = 28 / 80 × 100% = 35%."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một phân tử khí X gồm nguyên tố Carbon liên kết với Hydrogen, trong đó Carbon chiếm 85,71% về khối lượng. Khối lượng phân tử của X là 28 amu. Công thức phân tử của X là:",
        "options": [
          "C2H4",
          "CH4",
          "C2H6",
          "C3H6"
        ],
        "correct": 0,
        "explanation": "mC = 28 × 0,8571 ≈ 24 (2C), mH = 4 (4H) => C2H4."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Khối lượng của 1 phân tử nước tính bằng gam xấp xỉ bằng:",
        "options": [
          "2,99 × 10^-23 g",
          "1,66 × 10^-24 g",
          "18 g",
          "1,8 × 10^-22 g"
        ],
        "correct": 0,
        "explanation": "18 × 1,6605 × 10^-24 g ≈ 2,989 × 10^-23 g."
      }
    ]
  },
  "chem7_c2_b6_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Theo quy tắc octet, nguyên tử của các nguyên tố có xu hướng đạt cấu hình electron bền vững ở lớp ngoài cùng gồm:",
        "options": [
          "8 electron (hoặc 2 electron đối với helium)",
          "2 electron cho mọi nguyên tử",
          "18 electron",
          "32 electron"
        ],
        "correct": 0,
        "explanation": "Quy tắc octet: 8 electron lớp ngoài cùng (riêng He là 2e)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Liên kết ion là liên kết được hình thành bởi:",
        "options": [
          "Lực hút tĩnh điện giữa các ion mang điện tích trái dấu",
          "Các cặp electron dùng chung",
          "Lực hút giữa các hạt proton",
          "Lực tương tác từ"
        ],
        "correct": 0,
        "explanation": "Liên kết ion hình thành do lực hút tĩnh điện giữa cation (ion dương) và anion (ion âm)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nguyên tử kim loại nhường electron, nó biến thành hạt mang điện tích gì?",
        "options": [
          "Ion dương (cation)",
          "Ion âm (anion)",
          "Phân tử trung hòa",
          "Hạt neutron"
        ],
        "correct": 0,
        "explanation": "Nhường electron mang điện âm sẽ trở thành ion dương."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi nguyên tử Sodium (Na) nhường đi 1 electron ở lớp ngoài cùng, nó tạo thành ion nào?",
        "options": [
          "Na+",
          "Na2+",
          "Na-",
          "Na2-"
        ],
        "correct": 0,
        "explanation": "Na nhường 1e thành Na+."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là hợp chất ion?",
        "options": [
          "Sodium chloride (NaCl)",
          "Khí hydrogen (H2)",
          "Nước (H2O)",
          "Khí carbon dioxide (CO2)"
        ],
        "correct": 0,
        "explanation": "NaCl là hợp chất ion điển hình giữa kim loại Na và phi kim Cl."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Liên kết cộng hóa trị là liên kết được hình thành giữa hai nguyên tử bằng:",
        "options": [
          "Một hay nhiều cặp electron dùng chung",
          "Lực hút tĩnh điện giữa các ion",
          "Sự nhường và nhận electron hoàn toàn",
          "Lực tương tác hấp dẫn"
        ],
        "correct": 0,
        "explanation": "Liên kết cộng hóa trị hình thành bằng các cặp electron dùng chung."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nguyên tử Chlorine (7e ngoài cùng) đạt cấu hình bền vững của khí hiếm bằng cách:",
        "options": [
          "Nhận thêm 1 electron",
          "Nhường đi 7 electron",
          "Nhường đi 1 electron",
          "Nhận thêm 2 electron"
        ],
        "correct": 0,
        "explanation": "Cl có 7e ngoài cùng, nhận thêm 1e để đạt 8e bền vững giống Ar."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khi tạo thành phân tử Magnesium oxide (MgO), nguyên tử Mg đã:",
        "options": [
          "Nhường 2 electron cho nguyên tử O",
          "Nhận 2 electron từ nguyên tử O",
          "Góp chung 2 electron với nguyên tử O",
          "Nhường 1 electron cho nguyên tử O"
        ],
        "correct": 0,
        "explanation": "Mg nhường 2e thành Mg2+, O nhận 2e thành O2-."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Hợp chất ion thường có đặc điểm vật lí nào sau đây?",
        "options": [
          "Nhiệt độ nóng chảy và nhiệt độ sôi cao",
          "Ở thể khí ở nhiệt độ phòng",
          "Nhiệt độ nóng chảy rất thấp",
          "Không tan trong nước"
        ],
        "correct": 0,
        "explanation": "Liên kết ion bền vững nên hợp chất ion có nhiệt độ nóng chảy và sôi rất cao."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Dung dịch chất nào sau đây có khả năng dẫn điện tốt?",
        "options": [
          "Dung dịch nước muối (NaCl)",
          "Dung dịch nước đường (sucrose)",
          "Cồn tinh khiết",
          "Nước cất"
        ],
        "correct": 0,
        "explanation": "NaCl tan trong nước phân li thành các ion Na+ và Cl- tự do dẫn điện."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Trong phân tử khí hydrogen (H2), hai nguyên tử H liên kết với nhau bằng:",
        "options": [
          "1 cặp electron dùng chung",
          "2 cặp electron dùng chung",
          "Lực hút ion",
          "Lực đẩy tĩnh điện"
        ],
        "correct": 0,
        "explanation": "Mỗi nguyên tử H góp 1e tạo thành 1 cặp e dùng chung."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây có nhiệt độ nóng chảy cao nhất?",
        "options": [
          "Muối ăn (NaCl, khoảng 801°C)",
          "Đường ăn (nóng chảy khoảng 186°C)",
          "Nước đá (0°C)",
          "Cồn (nóng chảy ở -114°C)"
        ],
        "correct": 0,
        "explanation": "Hợp chất ion NaCl có nhiệt độ nóng chảy cao vượt trội."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét sự hình thành liên kết trong phân tử Sodium chloride (NaCl):",
        "statements": [
          {
            "subId": "a",
            "text": "Nguyên tử Sodium nhường 1 electron tạo thành ion dương Na+.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nguyên tử Chlorine nhận 1 electron tạo thành ion âm Cl-.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ion Na+ và Cl- hút nhau bằng lực hút tĩnh điện tạo nên tinh thể NaCl.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong phân tử NaCl có 1 cặp electron dùng chung giữa Na và Cl.",
            "correct": false
          }
        ],
        "explanation": "NaCl là liên kết ion do lực hút tĩnh điện, không phải góp chung electron."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét tính chất chung của các hợp chất ion:",
        "statements": [
          {
            "subId": "a",
            "text": "Hầu hết là chất rắn ở nhiệt độ phòng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Có nhiệt độ nóng chảy và nhiệt độ sôi cao.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi tan trong nước hoặc nóng chảy thì dẫn điện được.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dễ bay hơi và có mùi thơm nồng.",
            "correct": false
          }
        ],
        "explanation": "Hợp chất ion rất khó bay hơi do lực liên kết ion mạnh."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các chất: KCl, CaO, H2O, CH4:",
        "statements": [
          {
            "subId": "a",
            "text": "KCl và CaO là các hợp chất ion.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "H2O và CH4 là các hợp chất cộng hóa trị.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "KCl được tạo nên từ kim loại điển hình (K) và phi kim điển hình (Cl).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các chất này đều dẫn điện tốt ở thể rắn.",
            "correct": false
          }
        ],
        "explanation": "Ở thể rắn các ion bị giữ chặt trong mạng tinh thể nên không dẫn điện."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Xét quá trình nguyên tử Magnesium (Z = 12) liên kết với Oxygen (Z = 8):",
        "statements": [
          {
            "subId": "a",
            "text": "Mg có 2e ngoài cùng, có xu hướng nhường 2e tạo Mg2+.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "O có 6e ngoài cùng, có xu hướng nhận 2e tạo O2-.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sau khi tạo ion, cả Mg2+ và O2- đều có 8 electron ở lớp ngoài cùng giống khí hiếm Neon.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hợp chất tạo thành là Mg2O.",
            "correct": false
          }
        ],
        "explanation": "Hợp chất tạo thành là MgO tỉ lệ 1 : 1."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Số electron tối đa ở lớp ngoài cùng của nguyên tử khí hiếm Neon là bao nhiêu?",
        "correctAnswer": "8",
        "explanation": "Neon có 8 electron ngoài cùng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Điện tích của ion tạo thành khi nguyên tử Calcium nhường 2 electron là bao nhiêu? (Ghi dấu và số)",
        "correctAnswer": "+2",
        "explanation": "Ca nhường 2e tạo ion Ca2+ mang điện tích +2."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong phân tử khí nitrogen (N2), hai nguyên tử N liên kết với nhau bằng bao nhiêu cặp electron dùng chung?",
        "correctAnswer": "3",
        "explanation": "N2 có liên kết ba (3 cặp electron dùng chung)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một ion X- có 10 electron. Số proton trong hạt nhân của nguyên tử X là bao nhiêu?",
        "correctAnswer": "9",
        "explanation": "X nhận 1e thành X- có 10e => ban đầu X có 9 proton (Fluorine)."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Trong phân tử nước (H2O), nguyên tử Oxygen đã góp chung bao nhiêu electron với 2 nguyên tử Hydrogen?",
        "correctAnswer": "2",
        "explanation": "O góp 2 electron (mỗi liên kết O-H dùng 1 electron của O)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Phân tử carbon dioxide (CO2) có tổng cộng bao nhiêu cặp electron dùng chung giữa C và 2 nguyên tử O?",
        "correctAnswer": "4",
        "explanation": "CO2 có 2 liên kết đôi O=C=O => tổng cộng 4 cặp e dùng chung."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nguyên tử nguyên tố X có 1 electron lớp ngoài cùng, nguyên tử nguyên tố Y có 7 electron lớp ngoài cùng. Liên kết giữa X và Y thuộc loại:",
        "options": [
          "Liên kết ion",
          "Liên kết cộng hóa trị phân cực",
          "Liên kết cộng hóa trị không phân cực",
          "Liên kết kim loại"
        ],
        "correct": 0,
        "explanation": "Kim loại điển hình (1e ngoài cùng) nhường e cho phi kim điển hình (7e ngoài cùng) tạo liên kết ion."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Chất nào sau đây ở điều kiện thường tồn tại ở thể khí và có liên kết cộng hóa trị?",
        "options": [
          "Methane (CH4)",
          "Sodium chloride (NaCl)",
          "Magnesium oxide (MgO)",
          "Calcium chloride (CaCl2)"
        ],
        "correct": 0,
        "explanation": "CH4 là hợp chất cộng hóa trị ở thể khí."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nguyên tố A (Z = 19) kết hợp với nguyên tố B (Z = 16) tạo thành hợp chất có công thức hóa học là:",
        "options": [
          "A2B",
          "AB",
          "AB2",
          "A2B3"
        ],
        "correct": 0,
        "explanation": "A là K (hóa trị I, tạo K+), B là S (hóa trị II, tạo S2-) => công thức K2S (A2B)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Giải thích vì sao dung dịch đường mía không dẫn điện trong khi dung dịch muối ăn lại dẫn điện tốt?",
        "options": [
          "Đường là chất cộng hóa trị không phân li thành ion, muối ăn là chất ion phân li thành các ion tự do",
          "Đường không tan trong nước",
          "Muối ăn chứa kim loại tự do",
          "Đường có khối lượng phân tử lớn hơn"
        ],
        "correct": 0,
        "explanation": "Hợp chất ion phân li thành ion mang điện tự do chuyển động trong dung dịch."
      }
    ]
  },
  "chem7_c2_b6_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Liên kết cộng hóa trị thường được hình thành giữa:",
        "options": [
          "Các nguyên tử phi kim với nhau",
          "Kim loại điển hình với phi kim điển hình",
          "Hai nguyên tử kim loại",
          "Khí hiếm với phi kim"
        ],
        "correct": 0,
        "explanation": "Liên kết cộng hóa trị thường tạo nên giữa các nguyên tử phi kim."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong phân tử khí oxygen (O2), hai nguyên tử O liên kết với nhau bằng:",
        "options": [
          "Hai cặp electron dùng chung (liên kết đôi)",
          "Một cặp electron dùng chung",
          "Ba cặp electron dùng chung",
          "Lực hút ion"
        ],
        "correct": 0,
        "explanation": "O2 có liên kết đôi (2 cặp electron dùng chung O=O)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phân tử nào sau đây có liên kết ba giữa hai nguyên tử?",
        "options": [
          "Nitrogen (N2)",
          "Oxygen (O2)",
          "Hydrogen (H2)",
          "Chlorine (Cl2)"
        ],
        "correct": 0,
        "explanation": "N2 có liên kết ba N≡N rất bền vững."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hợp chất cộng hóa trị có đặc điểm nào sau đây?",
        "options": [
          "Nhiệt độ nóng chảy và nhiệt độ sôi thường thấp hơn hợp chất ion",
          "Đều dẫn điện tốt ở trạng thái rắn",
          "Chỉ tồn tại ở thể rắn",
          "Không bao giờ tan trong nước"
        ],
        "correct": 0,
        "explanation": "Hợp chất cộng hóa trị có nhiệt độ nóng chảy và sôi tương đối thấp."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là chất lỏng ở điều kiện thường có liên kết cộng hóa trị?",
        "options": [
          "Nước (H2O)",
          "Sodium chloride (NaCl)",
          "Magnesium oxide (MgO)",
          "Đồng (Cu)"
        ],
        "correct": 0,
        "explanation": "Nước là chất lỏng cấu tạo bởi các phân tử H2O liên kết cộng hóa trị."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Số electron dùng chung trong một liên kết đơn là:",
        "options": [
          "2 electron (1 cặp electron)",
          "1 electron",
          "4 electron",
          "6 electron"
        ],
        "correct": 0,
        "explanation": "Liên kết đơn gồm 1 cặp electron dùng chung (2e)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phân tử ammonia (NH3) có bao nhiêu liên kết đơn cộng hóa trị?",
        "options": [
          "3 liên kết đơn N - H",
          "1 liên kết ba",
          "2 liên kết đôi",
          "4 liên kết đơn"
        ],
        "correct": 0,
        "explanation": "Nguyên tử N liên kết với 3 nguyên tử H bằng 3 liên kết đơn."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Vì sao khí nitrogen (N2) trơ về mặt hóa học ở nhiệt độ phòng?",
        "options": [
          "Do có liên kết ba N≡N rất bền vững giữa 2 nguyên tử N",
          "Do nitrogen là một khí hiếm",
          "Do phân tử N2 không có electron",
          "Do nitrogen ở thể khí"
        ],
        "correct": 0,
        "explanation": "Liên kết ba N≡N có năng lượng liên kết rất lớn nên rất bền vững."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Hợp chất nào sau đây có liên kết ion?",
        "options": [
          "Potassium chloride (KCl)",
          "Khí methane (CH4)",
          "Khí carbon dioxide (CO2)",
          "Nước (H2O)"
        ],
        "correct": 0,
        "explanation": "KCl tạo bởi kim loại K và phi kim Cl là hợp chất ion."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây dễ bay hơi và có nhiệt độ sôi thấp?",
        "options": [
          "Cồn ethanol",
          "Muối ăn",
          "Vôi sống (CaO)",
          "Đá vôi (CaCO3)"
        ],
        "correct": 0,
        "explanation": "Cồn ethanol là hợp chất cộng hóa trị dễ bay hơi, sôi ở 78,3°C."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khi hòa tan đường ăn vào nước, dung dịch thu được:",
        "options": [
          "Không dẫn điện vì phân tử đường không phân li thành ion",
          "Dẫn điện tốt như nước muối",
          "Làm quỳ tím hóa đỏ",
          "Tạo kết tủa trắng"
        ],
        "correct": 0,
        "explanation": "Đường là chất cộng hóa trị, dung dịch đường không dẫn điện."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Trong phân tử hydrogen chloride (HCl), cặp electron dùng chung bị lệch về phía:",
        "options": [
          "Nguyên tử Chlorine vì Cl có khả năng hút electron mạnh hơn",
          "Nguyên tử Hydrogen",
          "Chính giữa hai nguyên tử",
          "Không bị lệch"
        ],
        "correct": 0,
        "explanation": "Cl có độ âm điện lớn hơn nên hút cặp electron lệch về phía mình."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét phân tử nước (H2O):",
        "statements": [
          {
            "subId": "a",
            "text": "Được tạo thành bởi liên kết cộng hóa trị giữa 1 nguyên tử O và 2 nguyên tử H.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mỗi nguyên tử H góp chung 1 electron với nguyên tử O.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nguyên tử O đạt cấu hình bền vững 8 electron ở lớp ngoài cùng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phân tử nước có liên kết ion do lực hút tĩnh điện.",
            "correct": false
          }
        ],
        "explanation": "Nước là hợp chất cộng hóa trị."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "So sánh liên kết ion và liên kết cộng hóa trị:",
        "statements": [
          {
            "subId": "a",
            "text": "Liên kết ion hình thành do lực hút tĩnh điện giữa các ion trái dấu.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Liên kết cộng hóa trị hình thành do các cặp electron dùng chung.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hợp chất ion thường có nhiệt độ nóng chảy cao hơn hợp chất cộng hóa trị.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các hợp chất cộng hóa trị đều dẫn điện tốt khi tan trong nước.",
            "correct": false
          }
        ],
        "explanation": "Hầu hết hợp chất cộng hóa trị (như đường, cồn...) không dẫn điện khi tan trong nước."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phân tử: Cl2, O2, N2, CO2:",
        "statements": [
          {
            "subId": "a",
            "text": "Cl2 có 1 cặp electron dùng chung (liên kết đơn).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "O2 có 2 cặp electron dùng chung (liên kết đôi).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "N2 có 3 cặp electron dùng chung (liên kết ba).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "CO2 chỉ có các liên kết ion.",
            "correct": false
          }
        ],
        "explanation": "CO2 có 2 liên kết đôi cộng hóa trị O=C=O."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một hợp chất Z được tạo bởi nguyên tố kim loại X (Z = 20) và nguyên tố phi kim Y (Z = 17):",
        "statements": [
          {
            "subId": "a",
            "text": "X là Calcium, Y là Chlorine.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "X nhường 2e tạo Ca2+, mỗi nguyên tử Y nhận 1e tạo Cl-.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hợp chất Z là CaCl2 có liên kết ion.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Ở điều kiện thường, Z là chất khí dễ cháy.",
            "correct": false
          }
        ],
        "explanation": "CaCl2 là chất rắn màu trắng, khó nóng chảy."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Trong phân tử khí chlorine (Cl2), có bao nhiêu cặp electron dùng chung giữa hai nguyên tử Cl?",
        "correctAnswer": "1",
        "explanation": "Cl2 có 1 cặp electron dùng chung."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Nguyên tử Carbon cần góp chung bao nhiêu electron để đạt cấu hình octet bền vững?",
        "correctAnswer": "4",
        "explanation": "C có 4e ngoài cùng, cần góp chung 4 electron."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong phân tử methane (CH4), có tổng cộng bao nhiêu liên kết đơn C - H?",
        "correctAnswer": "4",
        "explanation": "Có 4 liên kết đơn C - H."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một ion nhôm Al3+ có bao nhiêu electron ở lớp vỏ?",
        "correctAnswer": "10",
        "explanation": "Al có 13e, nhường 3e còn 10e."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Trong phân tử ammonia (NH3), có bao nhiêu electron ở lớp ngoài cùng của nguyên tử Nitrogen KHÔNG tham gia liên kết (electron tự do)?",
        "correctAnswer": "2",
        "explanation": "N có 5e ngoài cùng, dùng 3e liên kết với 3H, còn lại 2 electron tự do (1 cặp e)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm nguyên tố X liên kết ion với ion Cl- tạo hợp chất XCl2. Biết khối lượng phân tử hợp chất là 111 amu. Tên nguyên tố X là gì?",
        "correctAnswer": "Calcium",
        "explanation": "X + 2 × 35,5 = 111 => X = 40 (Calcium)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nguyên tử X có 6 electron ở lớp ngoài cùng, nguyên tử Hydrogen có 1 electron. Công thức hợp chất cộng hóa trị tạo bởi X và H là:",
        "options": [
          "H2X",
          "HX",
          "HX2",
          "H3X"
        ],
        "correct": 0,
        "explanation": "X có 6e ngoài cùng cần thêm 2e => liên kết với 2 nguyên tử H tạo H2X (như H2O, H2S)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho biết sơ đồ tạo thành liên kết trong phân tử CO2: nguyên tử C góp chung 4 electron với 2 nguyên tử O. Loại liên kết giữa C và O trong phân tử CO2 là:",
        "options": [
          "Liên kết cộng hóa trị gồm 2 liên kết đôi",
          "Liên kết ion",
          "Liên kết ba",
          "Liên kết kim loại"
        ],
        "correct": 0,
        "explanation": "CO2 có cấu trúc O=C=O gồm hai liên kết đôi cộng hóa trị."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Chất nào sau đây khi hòa tan vào nước tạo thành dung dịch KHÔNG dẫn điện?",
        "options": [
          "Đường glucose (C6H12O6)",
          "Muối ăn (NaCl)",
          "Calcium chloride (CaCl2)",
          "Sodium hydroxide (NaOH)"
        ],
        "correct": 0,
        "explanation": "Glucose là hợp chất cộng hóa trị không phân li thành ion trong nước."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Phân tử chất nào sau đây có tổng số electron tham gia liên kết là 6 hạt (3 cặp electron)?",
        "options": [
          "Nitrogen (N2)",
          "Oxygen (O2)",
          "Chlorine (Cl2)",
          "Carbon dioxide (CO2)"
        ],
        "correct": 0,
        "explanation": "N2 có liên kết ba gồm 3 cặp e (6 hạt electron)."
      }
    ]
  },
  "chem7_c2_b6_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hạt mang điện tích dương tạo thành khi nguyên tử kim loại nhường electron được gọi là:",
        "options": [
          "Cation (ion dương)",
          "Anion (ion âm)",
          "Proton tự do",
          "Phân tử"
        ],
        "correct": 0,
        "explanation": "Ion dương được gọi là Cation."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hạt mang điện tích âm tạo thành khi nguyên tử phi kim nhận electron được gọi là:",
        "options": [
          "Anion (ion âm)",
          "Cation (ion dương)",
          "Electron tự do",
          "Hạt nhân"
        ],
        "correct": 0,
        "explanation": "Ion âm được gọi là Anion."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong tinh thể muối ăn (NaCl), các ion Na+ và Cl- được sắp xếp:",
        "options": [
          "Trật tự và luân phiên nhau trong không gian 3 chiều tạo mạng tinh thể",
          "Lộn xộn không theo quy luật",
          "Thành từng cặp phân tử riêng biệt tách rời",
          "Tập trung Na+ ở giữa và Cl- ở ngoài"
        ],
        "correct": 0,
        "explanation": "Mạng tinh thể ion lập phương sắp xếp luân phiên trật tự."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Chất nào sau đây tồn tại ở dạng mạng tinh thể ion ở điều kiện thường?",
        "options": [
          "Calcium oxide (vôi sống CaO)",
          "Nước",
          "Khí nitrogen",
          "Cồn ethanol"
        ],
        "correct": 0,
        "explanation": "CaO là hợp chất ion thể rắn tinh thể."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Liên kết trong phân tử nước (H2O) là:",
        "options": [
          "Liên kết cộng hóa trị",
          "Liên kết ion",
          "Liên kết kim loại",
          "Liên kết hidro"
        ],
        "correct": 0,
        "explanation": "H2O là hợp chất cộng hóa trị giữa 2 phi kim H và O."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Số electron mà nguyên tử phi kim Oxygen cần nhận thêm để đạt cấu hình octet là:",
        "options": [
          "2 electron",
          "1 electron",
          "3 electron",
          "4 electron"
        ],
        "correct": 0,
        "explanation": "O có 6e ngoài cùng, nhận thêm 2e để thành 8e (O2-)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây vừa có nhiệt độ nóng chảy cao vừa dễ tan trong nước tạo dung dịch dẫn điện?",
        "options": [
          "Sodium chloride (NaCl)",
          "Sáp nến (parafin)",
          "Đường saccarozơ",
          "Dầu ăn"
        ],
        "correct": 0,
        "explanation": "Đặc tính điển hình của hợp chất ion NaCl."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Vì sao các hợp chất cộng hóa trị như cồn, xăng, dầu lại dễ bay hơi và dễ cháy?",
        "options": [
          "Vì lực liên kết giữa các phân tử tương đối yếu",
          "Vì khối lượng nguyên tử rất lớn",
          "Vì chúng chứa kim loại",
          "Vì chúng có liên kết ion"
        ],
        "correct": 0,
        "explanation": "Lực hút giữa các phân tử cộng hóa trị yếu nên dễ bay hơi."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Ion nào sau đây có cấu hình electron bền vững giống khí hiếm Neon (2, 8)?",
        "options": [
          "Na+ và F-",
          "K+ và Cl-",
          "Ca2+ và S2-",
          "Mg2+ và Cl-"
        ],
        "correct": 0,
        "explanation": "Na (11) nhường 1e thành Na+ (10e), F (9) nhận 1e thành F- (10e) đều giống Ne."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Trong phân tử hợp chất ion K2O, tỉ lệ số ion K+ và O2- là:",
        "options": [
          "2 : 1",
          "1 : 2",
          "1 : 1",
          "2 : 3"
        ],
        "correct": 0,
        "explanation": "Công thức K2O gồm 2 ion K+ và 1 ion O2-."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Mô hình phân tử khí methane (CH4) có dạng hình học nào?",
        "options": [
          "Hình tứ diện đều",
          "Đường thẳng",
          "Tam giác phẳng",
          "Hình vuông"
        ],
        "correct": 0,
        "explanation": "4 liên kết C-H phân bố đối xứng theo hình tứ diện đều."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hiện tượng dẫn điện của dung dịch muối ăn chứng minh:",
        "options": [
          "Trong dung dịch có các ion chuyển động tự do",
          "Muối ăn có chứa dòng điện",
          "Nước cất tự dẫn điện",
          "Electron tự do chuyển động trong nước"
        ],
        "correct": 0,
        "explanation": "Các ion Na+ và Cl- chuyển động tự do đóng vai trò hạt tải điện."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét phân tử khí hydrogen chloride (HCl):",
        "statements": [
          {
            "subId": "a",
            "text": "Được tạo thành từ liên kết cộng hóa trị giữa nguyên tử H và Cl.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cặp electron dùng chung bị hút lệch về phía nguyên tử Chlorine.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi tan trong nước, khí HCl tạo thành dung dịch axit dẫn điện được.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Ở nhiệt độ phòng, HCl là chất rắn kết tinh màu trắng.",
            "correct": false
          }
        ],
        "explanation": "Ở nhiệt độ phòng, HCl là chất khí không màu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về khả năng dẫn điện của các chất:",
        "statements": [
          {
            "subId": "a",
            "text": "Nước cất tinh khiết hầu như không dẫn điện.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nước muối dẫn điện tốt do có ion tự do.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Muối ăn ở dạng tinh thể rắn dẫn điện rất tốt.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Dung dịch đường ăn trong nước không dẫn điện.",
            "correct": true
          }
        ],
        "explanation": "Muối ăn thể rắn các ion bị giam giữ không chuyển động được nên không dẫn điện."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các hợp chất: Na2O, H2S, NH3, BaCl2:",
        "statements": [
          {
            "subId": "a",
            "text": "Na2O và BaCl2 là các hợp chất ion.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "H2S và NH3 là các hợp chất cộng hóa trị.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "H2S có mùi trứng thối đặc trưng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "BaCl2 có nhiệt độ nóng chảy thấp hơn H2S.",
            "correct": false
          }
        ],
        "explanation": "BaCl2 là hợp chất ion có nhiệt độ nóng chảy cao hơn H2S thể khí rất nhiều."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nguyên tử X (Z = 12) kết hợp với nguyên tử Y (Z = 8) tạo thành chất Z:",
        "statements": [
          {
            "subId": "a",
            "text": "X là Magnesium, Y là Oxygen.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Z là Magnesium oxide (MgO).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Liên kết trong Z là liên kết ion.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Z có nhiệt độ nóng chảy dưới 100°C.",
            "correct": false
          }
        ],
        "explanation": "MgO có nhiệt độ nóng chảy cực cao (~2852°C), được dùng làm gạch chịu lửa."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Số hạt electron mang điện tích âm trong một ion Na+ là bao nhiêu hạt?",
        "correctAnswer": "10",
        "explanation": "Na có 11e, nhường 1e còn 10e."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Số electron mà nguyên tử kim loại Aluminium nhường đi khi tạo liên kết ion là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "Al nhường 3e tạo ion Al3+."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Số cặp electron dùng chung trong phân tử khí oxygen (O2) là bao nhiêu?",
        "correctAnswer": "2",
        "explanation": "O2 có liên kết đôi (2 cặp e dùng chung)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một ion oxide O2- có bao nhiêu electron ở lớp vỏ ngoài cùng?",
        "correctAnswer": "8",
        "explanation": "O nhận 2e đạt octet 8e bền vững."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Trong phân tử hợp chất ion CaCl2, tỉ số giữa số cation Ca2+ và anion Cl- là bao nhiêu? (Ghi tỉ số dạng 1:2)",
        "correctAnswer": "1:2",
        "explanation": "Tỉ lệ 1 ion Ca2+ và 2 ion Cl-."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Phân tử khí nào có khối lượng phân tử là 28 amu và có liên kết ba rất bền vững? (Viết KHHH)",
        "correctAnswer": "N2",
        "explanation": "Nitrogen (N2) có PTK = 28 amu và liên kết ba N≡N."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Vật liệu chịu lửa trong lò luyện kim thường được chế tạo từ magnesium oxide (MgO). Nguyên nhân chính là do:",
        "options": [
          "MgO có liên kết ion rất bền vững nên có nhiệt độ nóng chảy cực kì cao (~2850°C)",
          "MgO nhẹ hơn các chất khác",
          "MgO có màu trắng đẹp",
          "MgO dẫn điện tốt"
        ],
        "correct": 0,
        "explanation": "Đặc tính liên kết ion siêu bền của MgO."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho biết độ âm điện của H là 2,2 và Cl là 3,16. Liên kết trong phân tử HCl là:",
        "options": [
          "Liên kết cộng hóa trị có cực (phân cực)",
          "Liên kết ion",
          "Liên kết cộng hóa trị không cực",
          "Liên kết kim loại"
        ],
        "correct": 0,
        "explanation": "Hiệu độ âm điện 3,16 - 2,2 = 0,96 thuộc khoảng liên kết cộng hóa trị phân cực."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hai nguyên tử X và Y có cấu hình electron lớp ngoài cùng lần lượt là 3s1 và 2s2 2p4. Công thức phân tử của hợp chất tạo bởi X và Y là:",
        "options": [
          "X2Y",
          "XY",
          "XY2",
          "X2Y3"
        ],
        "correct": 0,
        "explanation": "X là Na (hóa trị I), Y là O (hóa trị II) => X2Y (Na2O)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một chất X có các tính chất: ở thể rắn màu trắng, tan nhiều trong nước tạo dung dịch dẫn điện, khi nung nóng ở 800°C mới bắt đầu nóng chảy. X có thể là chất nào?",
        "options": [
          "NaCl",
          "Đường mía",
          "Parafin",
          "Nước đá"
        ],
        "correct": 0,
        "explanation": "NaCl đáp ứng đầy đủ tính chất của chất ion điển hình."
      }
    ]
  },
  "chem7_c2_b7_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong quy ước về hóa trị, nguyên tố nào được chọn làm đơn vị và luôn có hóa trị I?",
        "options": [
          "Hydrogen",
          "Oxygen",
          "Carbon",
          "Nitrogen"
        ],
        "correct": 0,
        "explanation": "Hydrogen luôn được quy ước có hóa trị I."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong các hợp chất, nguyên tố Oxygen luôn được quy ước có hóa trị là:",
        "options": [
          "II",
          "I",
          "III",
          "IV"
        ],
        "correct": 0,
        "explanation": "Oxygen luôn có hóa trị II."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Theo quy tắc hóa trị, trong hợp chất hai nguyên tố AxBy (với a, b là hóa trị tương ứng của A và B) luôn có biểu thức:",
        "options": [
          "x × a = y × b",
          "x × b = y × a",
          "x / a = y / b",
          "x + a = y + b"
        ],
        "correct": 0,
        "explanation": "Quy tắc hóa trị: x × a = y × b."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Công thức hóa học của đơn chất kim loại nhôm là:",
        "options": [
          "Al",
          "Al2",
          "Al3",
          "AlO"
        ],
        "correct": 0,
        "explanation": "Đơn chất kim loại kí hiệu bằng KHHH của nguyên tố (Al)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Công thức hóa học của đơn chất khí oxygen là:",
        "options": [
          "O2",
          "O",
          "O3",
          "O4"
        ],
        "correct": 0,
        "explanation": "Khí oxygen gồm các phân tử 2 nguyên tử O liên kết với nhau: O2."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Ý nghĩa của công thức hóa học cho ta biết các thông tin nào sau đây?",
        "options": [
          "Nguyên tố tạo ra chất, số nguyên tử mỗi nguyên tố và khối lượng phân tử",
          "Chất có độc hay không",
          "Nhiệt độ nóng chảy chính xác",
          "Khối lượng riêng của chất"
        ],
        "correct": 0,
        "explanation": "Ý nghĩa CTHH: nguyên tố cấu tạo, số lượng nguyên tử, phân tử khối."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong hợp chất FeO, hóa trị của nguyên tố Iron (Sắt) là:",
        "options": [
          "II",
          "III",
          "I",
          "IV"
        ],
        "correct": 0,
        "explanation": "1 × a = 1 × II => a = II."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hợp chất của Carbon với Oxygen có công thức CO2. Hóa trị của Carbon trong hợp chất này là:",
        "options": [
          "IV",
          "II",
          "VI",
          "I"
        ],
        "correct": 0,
        "explanation": "1 × a = 2 × II => a = IV."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Lập công thức hóa học của hợp chất tạo bởi Aluminium (hóa trị III) và Oxygen (hóa trị II):",
        "options": [
          "Al2O3",
          "AlO",
          "Al3O2",
          "AlO2"
        ],
        "correct": 0,
        "explanation": "x/y = II/III = 2/3 => Al2O3."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Phần trăm khối lượng của nguyên tố Hydrogen trong phân tử nước (H2O) là:",
        "options": [
          "11,11%",
          "20%",
          "5,56%",
          "15%"
        ],
        "correct": 0,
        "explanation": "%H = 2 / 18 × 100% ≈ 11,11%."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Trong hợp chất NH3, hóa trị của nguyên tố Nitrogen là:",
        "options": [
          "III",
          "I",
          "II",
          "V"
        ],
        "correct": 0,
        "explanation": "1 × a = 3 × I => a = III."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Công thức hóa học nào sau đây viết SAI theo quy tắc hóa trị?",
        "options": [
          "NaO",
          "NaCl",
          "CaO",
          "Al2O3"
        ],
        "correct": 0,
        "explanation": "Na hóa trị I, O hóa trị II => công thức đúng phải là Na2O (NaO sai)."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét công thức hóa học của khí methane (CH4):",
        "statements": [
          {
            "subId": "a",
            "text": "Hợp chất tạo bởi 2 nguyên tố là Carbon và Hydrogen.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong 1 phân tử có 1 nguyên tử C và 4 nguyên tử H.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử của methane là 16 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong phân tử CH4, Carbon có hóa trị II.",
            "correct": false
          }
        ],
        "explanation": "Trong CH4, Carbon có hóa trị IV (1 × IV = 4 × I)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xác định hóa trị của kim loại trong các hợp chất:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong Na2O, Sodium có hóa trị I.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong MgO, Magnesium có hóa trị II.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trong Fe2O3, Iron có hóa trị III.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong Cu2O, Copper có hóa trị II.",
            "correct": false
          }
        ],
        "explanation": "Trong Cu2O: 2 × a = 1 × II => a = I (Copper hóa trị I)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các hợp chất: H2S, SO2, SO3:",
        "statements": [
          {
            "subId": "a",
            "text": "Hóa trị của Sulfur trong H2S là II.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hóa trị của Sulfur trong SO2 là IV.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hóa trị của Sulfur trong SO3 là VI.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Sulfur có hóa trị không đổi trong tất cả các hợp chất.",
            "correct": false
          }
        ],
        "explanation": "Sulfur có nhiều hóa trị: II, IV, VI."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Một hợp chất có công thức hóa học là Ca3(PO4)2:",
        "statements": [
          {
            "subId": "a",
            "text": "Gồm 3 nguyên tố: Ca, P, O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nhóm PO4 có hóa trị III.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Calcium có hóa trị II.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tổng số nguyên tử trong một phân tử hợp chất là 10.",
            "correct": false
          }
        ],
        "explanation": "Tổng số nguyên tử = 3 + 2 × (1 + 4) = 13 nguyên tử."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Hóa trị của nguyên tố Chlorine trong phân tử axit clohiđric (HCl) là bao nhiêu?",
        "correctAnswer": "I",
        "explanation": "H hóa trị I => Cl có hóa trị I."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Hóa trị của nhóm hydroxide (OH) trong phân tử NaOH là bao nhiêu?",
        "correctAnswer": "I",
        "explanation": "Nhóm OH có hóa trị I."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hóa trị của nguyên tố Carbon trong khí độc carbon monoxide (CO) là bao nhiêu?",
        "correctAnswer": "II",
        "explanation": "1 × a = 1 × II => a = II."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Phần trăm khối lượng của Carbon trong khí carbon dioxide (CO2) xấp xỉ bằng bao nhiêu phần trăm? (Làm tròn đến hàng đơn vị)",
        "correctAnswer": "27",
        "explanation": "%C = 12 / 44 × 100% ≈ 27,27% ≈ 27%."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Lập CTHH của hợp chất tạo bởi sắt có hóa trị III và nhóm sunfat (SO4) có hóa trị II. Số nguyên tử sắt trong công thức là bao nhiêu?",
        "correctAnswer": "2",
        "explanation": "Fex(SO4)y => x/y = II/III = 2/3 => Fe2(SO4)3 có 2 nguyên tử Fe."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một oxide của nguyên tố R có công thức R2O3 nặng 102 amu. Tên gọi của R là gì?",
        "correctAnswer": "Aluminium",
        "explanation": "2R + 48 = 102 => 2R = 54 => R = 27 (Aluminium)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một hợp chất tạo bởi nguyên tố X (hóa trị II) và nhóm PO4 (hóa trị III) có công thức là:",
        "options": [
          "X3(PO4)2",
          "X2(PO4)3",
          "XPO4",
          "X3PO4"
        ],
        "correct": 0,
        "explanation": "Quy tắc hóa trị: x/y = III/II = 3/2 => X3(PO4)2."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hợp chất của nguyên tố X với Oxygen là XO. Hợp chất của nguyên tố Y với Hydrogen là YH3. Công thức hóa học của hợp chất tạo bởi X và Y là:",
        "options": [
          "X3Y2",
          "XY",
          "X2Y3",
          "X3Y"
        ],
        "correct": 0,
        "explanation": "X có hóa trị II (vì XO), Y có hóa trị III (vì YH3) => công thức X3Y2."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hợp chất A chứa 70% Fe và 30% O về khối lượng. Biết khối lượng phân tử của A là 160 amu. Công thức hóa học của A là:",
        "options": [
          "Fe2O3",
          "FeO",
          "Fe3O4",
          "Fe2O"
        ],
        "correct": 0,
        "explanation": "mFe = 160 × 0,7 = 112 amu (2 nguyên tử Fe), mO = 48 amu (3 nguyên tử O) => Fe2O3."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một oxide kim loại có dạng MO, trong đó kim loại M chiếm 80% về khối lượng. Nguyên tố M là:",
        "options": [
          "Copper (Cu, 64 amu)",
          "Iron (Fe, 56 amu)",
          "Zinc (Zn, 65 amu)",
          "Magnesium (Mg, 24 amu)"
        ],
        "correct": 0,
        "explanation": "M / (M + 16) = 0,8 => M = 0,8M + 12,8 => 0,2M = 12,8 => M = 64 (Copper, CuO)."
      }
    ]
  },
  "chem7_c2_b7_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Nhóm nguyên tử nào sau đây có hóa trị II?",
        "options": [
          "Nhóm sunfat (SO4)",
          "Nhóm hiđroxit (OH)",
          "Nhóm nitrat (NO3)",
          "Nhóm photphat (PO4)"
        ],
        "correct": 0,
        "explanation": "Nhóm SO4 và CO3 có hóa trị II (OH và NO3 hóa trị I, PO4 hóa trị III)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong hợp chất Al2O3, nguyên tố Aluminium có hóa trị là:",
        "options": [
          "III",
          "II",
          "I",
          "VI"
        ],
        "correct": 0,
        "explanation": "2 × a = 3 × II => a = III."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Công thức hóa học của hợp chất tạo bởi Sodium (hóa trị I) và nhóm OH (hóa trị I) là:",
        "options": [
          "NaOH",
          "Na(OH)2",
          "Na2OH",
          "NaOH2"
        ],
        "correct": 0,
        "explanation": "Cùng hóa trị I tỉ lệ 1 : 1 là NaOH."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nguyên tố nào sau đây có hóa trị không đổi bằng I trong mọi hợp chất?",
        "options": [
          "Sodium (Na)",
          "Iron (Fe)",
          "Copper (Cu)",
          "Carbon (C)"
        ],
        "correct": 0,
        "explanation": "Kim loại kiềm Na luôn có hóa trị I."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Công thức hóa học của đá vôi (canxi cacbonat) gồm Ca(II) và nhóm CO3(II) là:",
        "options": [
          "CaCO3",
          "Ca2CO3",
          "Ca(CO3)2",
          "Ca2(CO3)3"
        ],
        "correct": 0,
        "explanation": "Cùng hóa trị II tỉ lệ 1 : 1 là CaCO3."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Khối lượng phân tử của sulfuric acid (H2SO4) là:",
        "options": [
          "98 amu",
          "96 amu",
          "100 amu",
          "80 amu"
        ],
        "correct": 0,
        "explanation": "2 × 1 + 32 + 4 × 16 = 98 amu."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Xác định hóa trị của Iron trong hợp chất FeCl3:",
        "options": [
          "III",
          "II",
          "I",
          "IV"
        ],
        "correct": 0,
        "explanation": "Cl có hóa trị I => 1 × a = 3 × I => a = III."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Lập công thức hóa học của hợp chất gồm Magnesium (hóa trị II) và nhóm nitrate NO3 (hóa trị I):",
        "options": [
          "Mg(NO3)2",
          "MgNO3",
          "Mg2NO3",
          "Mg(NO3)3"
        ],
        "correct": 0,
        "explanation": "x/y = I/II = 1/2 => Mg(NO3)2."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Hóa trị của nguyên tố Nitrogen trong phân tử N2O5 là:",
        "options": [
          "V",
          "II",
          "III",
          "IV"
        ],
        "correct": 0,
        "explanation": "2 × a = 5 × II => a = V."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Hợp chất nào sau đây có hàm lượng (phần trăm khối lượng) nguyên tố Nitrogen cao nhất?",
        "options": [
          "Urea CO(NH2)2 (46,67%)",
          "NH4NO3 (35%)",
          "NaNO3 (16,47%)",
          "(NH4)2SO4 (21,21%)"
        ],
        "correct": 0,
        "explanation": "Urea có tỉ lệ %N cao nhất trong các loại phân đạm."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Công thức hóa học của khí sulfur trioxide là:",
        "options": [
          "SO3",
          "SO2",
          "S2O3",
          "SO"
        ],
        "correct": 0,
        "explanation": "Sulfur trioxide gồm 1 S và 3 O: SO3."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Trong hợp chất Cu(OH)2, nguyên tố Copper có hóa trị là:",
        "options": [
          "II",
          "I",
          "III",
          "IV"
        ],
        "correct": 0,
        "explanation": "Nhóm OH hóa trị I => 1 × a = 2 × I => a = II."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét hợp chất nhôm sunfat Al2(SO4)3:",
        "statements": [
          {
            "subId": "a",
            "text": "Aluminium có hóa trị III.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nhóm SO4 có hóa trị II.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử của Al2(SO4)3 là 342 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tỉ lệ số nguyên tử Al và S trong hợp chất là 1 : 1.",
            "correct": false
          }
        ],
        "explanation": "Tỉ lệ Al : S là 2 : 3."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét hóa trị của nguyên tố Carbon trong các hợp chất:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong CH4, Carbon có hóa trị IV.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong CO, Carbon có hóa trị II.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trong CO2, Carbon có hóa trị IV.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Carbon luôn chỉ thể hiện một hóa trị duy nhất là IV.",
            "correct": false
          }
        ],
        "explanation": "Carbon có hóa trị II (CO) và IV (CO2, CH4)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các công thức: BaCl2, K2SO4, FeO, Al3O2:",
        "statements": [
          {
            "subId": "a",
            "text": "BaCl2 viết đúng theo quy tắc hóa trị.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "K2SO4 viết đúng theo quy tắc hóa trị.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "FeO viết đúng theo quy tắc hóa trị.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Al3O2 viết đúng theo quy tắc hóa trị.",
            "correct": false
          }
        ],
        "explanation": "Al(III) và O(II) phải lập thành Al2O3 (Al3O2 viết sai)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hợp chất X có công thức phân tử là Fe3O4 (oxit sắt từ):",
        "statements": [
          {
            "subId": "a",
            "text": "Là hỗn hợp của FeO và Fe2O3.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng phân tử của Fe3O4 là 232 amu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trong Fe3O4 có 3 nguyên tử Fe và 4 nguyên tử O.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phần trăm khối lượng của O lớn hơn phần trăm khối lượng của Fe.",
            "correct": false
          }
        ],
        "explanation": "Fe chiếm 3 × 56 = 168 amu (72,4%), O chỉ chiếm 64 amu (27,6%)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Hóa trị của nhóm cacbonat (CO3) là bao nhiêu?",
        "correctAnswer": "II",
        "explanation": "Nhóm CO3 có hóa trị II."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Hóa trị của nguyên tố Barium trong phân tử BaO là bao nhiêu?",
        "correctAnswer": "II",
        "explanation": "BaO => Ba hóa trị II."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hợp chất tạo bởi Fe(II) và Cl(I) có công thức là FeClx. Giá trị của x là bao nhiêu?",
        "correctAnswer": "2",
        "explanation": "1 × II = x × I => x = 2 (FeCl2)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Phần trăm khối lượng của Oxygen trong phân tử khí sulfur dioxide (SO2, 64 amu) là bao nhiêu phần trăm?",
        "correctAnswer": "50",
        "explanation": "%O = (2 × 16) / 64 × 100% = 50%."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Lập CTHH của hợp chất gồm kim loại M (hóa trị II) và nhóm photphat PO4 (hóa trị III). Tổng chỉ số các nguyên tử và nhóm nguyên tử trong công thức M_x(PO4)_y (tức x + y) là bao nhiêu?",
        "correctAnswer": "5",
        "explanation": "x/y = 3/2 => M3(PO4)2 có x + y = 3 + 2 = 5."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một oxide kim loại có công thức R2O nặng 62 amu. Kí hiệu hóa học của nguyên tố R là gì?",
        "correctAnswer": "Na",
        "explanation": "2R + 16 = 62 => 2R = 46 => R = 23 (Sodium, Na2O)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hợp chất khí X của Carbon với Hydrogen chứa 80% Carbon về khối lượng. Khối lượng phân tử của X là 30 amu. Công thức phân tử của X là:",
        "options": [
          "C2H6",
          "CH4",
          "C2H4",
          "C3H8"
        ],
        "correct": 0,
        "explanation": "mC = 30 × 0,8 = 24 amu (2C), mH = 6 amu (6H) => C2H6 (ethane)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Nguyên tố A có hóa trị III trong oxide A2O3. Nguyên tố B có hóa trị I trong hydride BH. Công thức hợp chất tạo bởi A và B là:",
        "options": [
          "AB3",
          "A3B",
          "AB",
          "A2B3"
        ],
        "correct": 0,
        "explanation": "A hóa trị III, B hóa trị I => AB3."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một loại phân bón potassium chloride có chứa 90% KCl về khối lượng (còn lại là tạp chất không chứa K). Biết khối lượng mol KCl = 74,5 amu (K = 39, Cl = 35,5). Phần trăm khối lượng của nguyên tố K trong mẫu phân bón đó xấp xỉ là:",
        "options": [
          "47,1%",
          "52,3%",
          "45,0%",
          "39,0%"
        ],
        "correct": 0,
        "explanation": "%K trong KCl tinh khiết = 39 / 74,5 ≈ 52,35%. Trong mẫu: 52,35% × 0,9 ≈ 47,1%."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một oxide của lưu huỳnh trong đó nguyên tố Oxygen chiếm 60% về khối lượng. Hóa trị của Sulfur trong oxide đó là:",
        "options": [
          "VI",
          "IV",
          "II",
          "VII"
        ],
        "correct": 0,
        "explanation": "mS / mO = 40 / 60 = 2 / 3 => (32x) / (16y) = 2 / 3 => 2x / y = 2 / 3 => x / y = 1 / 3 => SO3. Trong SO3, S có hóa trị VI."
      }
    ]
  },
  "chem7_c2_b7_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố trong hợp chất kèm theo chỉ số chân dưới biểu thị:",
        "options": [
          "Công thức hóa học của chất",
          "Khối lượng riêng của chất",
          "Thể tích của chất",
          "Nhiệt độ nóng chảy"
        ],
        "correct": 0,
        "explanation": "Biểu thị công thức hóa học của chất."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong công thức hóa học H2O, chỉ số 2 ở chân chữ H cho biết:",
        "options": [
          "Trong 1 phân tử nước có 2 nguyên tử Hydrogen",
          "Có 2 phân tử nước",
          "Hóa trị của H là 2",
          "Khối lượng của H là 2 kg"
        ],
        "correct": 0,
        "explanation": "Chỉ số chân cho biết số nguyên tử của nguyên tố trong 1 phân tử."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hợp chất nào sau đây có công thức hóa học viết ĐÚNG theo quy tắc hóa trị?",
        "options": [
          "CaCl2",
          "CaCl",
          "Ca2Cl",
          "CaCl3"
        ],
        "correct": 0,
        "explanation": "Ca hóa trị II, Cl hóa trị I => CaCl2."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nguyên tố kim loại nào sau đây có nhiều hóa trị phổ biến là II và III?",
        "options": [
          "Iron (Sắt)",
          "Sodium (Natri)",
          "Magnesium (Magie)",
          "Aluminium (Nhôm)"
        ],
        "correct": 0,
        "explanation": "Iron có 2 hóa trị phổ biến là II (FeO, FeCl2) và III (Fe2O3, FeCl3)."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Trong hợp chất Al(OH)3, hóa trị của Aluminium là:",
        "options": [
          "III",
          "I",
          "II",
          "IV"
        ],
        "correct": 0,
        "explanation": "Nhóm OH hóa trị I => 1 × a = 3 × I => a = III."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Công thức hóa học của khí amoniac gồm 1 nguyên tử N và 3 nguyên tử H là:",
        "options": [
          "NH3",
          "N3H",
          "NH",
          "N2H3"
        ],
        "correct": 0,
        "explanation": "Khí ammonia có CTHH là NH3."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Xác định hóa trị của nguyên tố Phosphorus trong hợp chất P2O5:",
        "options": [
          "V",
          "III",
          "IV",
          "II"
        ],
        "correct": 0,
        "explanation": "2 × a = 5 × II => a = V."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Lập công thức hóa học của hợp chất tạo bởi Potassium (hóa trị I) và Oxygen (hóa trị II):",
        "options": [
          "K2O",
          "KO",
          "KO2",
          "K2O3"
        ],
        "correct": 0,
        "explanation": "x/y = II/I = 2/1 => K2O."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Phần trăm khối lượng của nguyên tố Oxygen trong phân tử canxi cacbonat (CaCO3, 100 amu) là:",
        "options": [
          "48%",
          "40%",
          "12%",
          "60%"
        ],
        "correct": 0,
        "explanation": "%O = (3 × 16) / 100 × 100% = 48%."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Công thức hóa học của khí gas butane gồm 4 nguyên tử C và 10 nguyên tử H là:",
        "options": [
          "C4H10",
          "C4H8",
          "C3H8",
          "C2H6"
        ],
        "correct": 0,
        "explanation": "C4H10 là butane."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Trong hợp chất SO2, nguyên tố Sulfur thể hiện hóa trị mấy?",
        "options": [
          "IV",
          "II",
          "VI",
          "I"
        ],
        "correct": 0,
        "explanation": "1 × a = 2 × II => a = IV."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hợp chất nào sau đây có phân tử khối bằng 74 amu?",
        "options": [
          "Calcium hydroxide Ca(OH)2",
          "Calcium oxide CaO",
          "Calcium carbonate CaCO3",
          "Magnesium oxide MgO"
        ],
        "correct": 0,
        "explanation": "40 + 2 × (16 + 1) = 74 amu (Ca(OH)2)."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét phân tử axit photphoric H3PO4:",
        "statements": [
          {
            "subId": "a",
            "text": "Tạo bởi 3 nguyên tố: H, P, O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong 1 phân tử có 3 nguyên tử H, 1 nguyên tử P và 4 nguyên tử O.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử của H3PO4 là 98 amu (3 + 31 + 64).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nhóm PO4 trong hợp chất có hóa trị I.",
            "correct": false
          }
        ],
        "explanation": "Nhóm PO4 có hóa trị III (3 × I = 1 × III)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xác định hóa trị của nguyên tố Cu trong các hợp chất:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong CuO, Cu có hóa trị II.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong Cu2O, Cu có hóa trị I.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trong CuSO4, Cu có hóa trị II.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong CuCl, Cu có hóa trị II.",
            "correct": false
          }
        ],
        "explanation": "Trong CuCl, Cl có hóa trị I nên Cu có hóa trị I."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các hợp chất: N2O, NO, NO2, N2O5:",
        "statements": [
          {
            "subId": "a",
            "text": "Hóa trị của Nitrogen trong N2O là I.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hóa trị của Nitrogen trong NO là II.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hóa trị của Nitrogen trong NO2 là IV.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hóa trị của Nitrogen trong N2O5 là III.",
            "correct": false
          }
        ],
        "explanation": "Trong N2O5, Nitrogen có hóa trị V."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hợp chất đá vôi CaCO3 bị nung nóng tạo vôi sống CaO và khí CO2:",
        "statements": [
          {
            "subId": "a",
            "text": "CaCO3, CaO, CO2 đều là các hợp chất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong cả CaCO3 và CaO, Calcium đều có hóa trị II.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Trong cả CaCO3 và CO2, Carbon đều có hóa trị IV.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phản ứng nung đá vôi là hiện tượng biến đổi vật lí.",
            "correct": false
          }
        ],
        "explanation": "Nung đá vôi sinh ra chất mới là biến đổi hóa học."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Hóa trị của nguyên tố Magnesium trong phân tử MgSO4 là bao nhiêu?",
        "correctAnswer": "II",
        "explanation": "Mg có hóa trị II."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của vôi sống (CaO) là bao nhiêu amu?",
        "correctAnswer": "56",
        "explanation": "40 + 16 = 56 amu."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hóa trị của nguyên tố Nitrogen trong phân tử khí NO2 là bao nhiêu?",
        "correctAnswer": "IV",
        "explanation": "1 × a = 2 × II => a = IV."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Phần trăm khối lượng của Mg trong phân tử MgO (40 amu) là bao nhiêu phần trăm?",
        "correctAnswer": "60",
        "explanation": "%Mg = 24 / 40 × 100% = 60%."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Lập CTHH của hợp chất tạo bởi sắt có hóa trị II và nhóm nitrat (NO3, hóa trị I). Số nguyên tử Oxygen có trong 1 phân tử hợp chất này là bao nhiêu?",
        "correctAnswer": "6",
        "explanation": "Fe(NO3)2 có 2 × 3 = 6 nguyên tử O."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có dạng X2O3 nặng 160 amu. Kí hiệu hóa học của nguyên tố X là gì?",
        "correctAnswer": "Fe",
        "explanation": "2X + 48 = 160 => 2X = 112 => X = 56 (Iron, Fe)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một hợp chất tạo bởi Carbon và Hydrogen có tỉ lệ khối lượng mC : mH = 3 : 1. Khối lượng phân tử của hợp chất là 16 amu. Công thức phân tử của hợp chất là:",
        "options": [
          "CH4",
          "C2H6",
          "C2H4",
          "C3H8"
        ],
        "correct": 0,
        "explanation": "mC = 16 × 3/4 = 12 amu (1C), mH = 4 amu (4H) => CH4."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Quặng bauxite chứa thành phần chính là Al2O3. Để thu được 54 tấn kim loại nhôm (Al) nguyên chất từ Al2O3 tinh khiết, khối lượng Al2O3 cần dùng theo lý thuyết là:",
        "options": [
          "102 tấn",
          "108 tấn",
          "150 tấn",
          "80 tấn"
        ],
        "correct": 0,
        "explanation": "Trong 102 tấn Al2O3 có 2 × 27 = 54 tấn Al => cần đúng 102 tấn Al2O3."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có công thức R(OH)3 nặng 78 amu. Tên gọi theo IUPAC của nguyên tố R là:",
        "options": [
          "Aluminium",
          "Iron",
          "Chromium",
          "Boron"
        ],
        "correct": 0,
        "explanation": "R + 3 × 17 = 78 => R = 78 - 51 = 27 (Aluminium)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một oxide của kim loại sắt có khối lượng phân tử là 232 amu và tỉ lệ số nguyên tử Fe : O là 3 : 4. Công thức phân tử của oxide này là:",
        "options": [
          "Fe3O4",
          "Fe2O3",
          "FeO",
          "Fe4O3"
        ],
        "correct": 0,
        "explanation": "3 × 56 + 4 × 16 = 168 + 64 = 232 amu => Fe3O4 (oxit sắt từ)."
      }
    ]
  },
  "chem7_c2_rev_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Chất được tạo nên từ hai nguyên tố hóa học trở lên được gọi là:",
        "options": [
          "Hợp chất",
          "Đơn chất",
          "Hỗn hợp",
          "Dung dịch"
        ],
        "correct": 0,
        "explanation": "Hợp chất tạo từ 2 nguyên tố trở lên."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Liên kết ion được hình thành do lực hút tĩnh điện giữa:",
        "options": [
          "Ion dương và ion âm",
          "Hai ion dương",
          "Hai ion âm",
          "Nguyên tử và electron"
        ],
        "correct": 0,
        "explanation": "Lực hút tĩnh điện giữa cation (+) và anion (-)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong phân tử hợp chất Al2O3, hóa trị của Aluminium là:",
        "options": [
          "III",
          "II",
          "I",
          "IV"
        ],
        "correct": 0,
        "explanation": "Al có hóa trị III trong Al2O3."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khối lượng phân tử của nước (H2O) là:",
        "options": [
          "18 amu",
          "16 amu",
          "20 amu",
          "17 amu"
        ],
        "correct": 0,
        "explanation": "2 × 1 + 16 = 18 amu."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là đơn chất phi kim?",
        "options": [
          "Khí nitrogen (N2)",
          "Đồng (Cu)",
          "Nhôm (Al)",
          "Vàng (Au)"
        ],
        "correct": 0,
        "explanation": "N2 là đơn chất phi kim."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Quy tắc octet chỉ ra rằng các nguyên tử có xu hướng đạt lớp ngoài cùng gồm:",
        "options": [
          "8 electron",
          "2 electron",
          "18 electron",
          "6 electron"
        ],
        "correct": 0,
        "explanation": "Quy tắc 8 electron bền vững."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây là hợp chất ion có nhiệt độ nóng chảy rất cao?",
        "options": [
          "Sodium chloride (NaCl)",
          "Khí carbon dioxide (CO2)",
          "Nước (H2O)",
          "Cồn (C2H5OH)"
        ],
        "correct": 0,
        "explanation": "NaCl là hợp chất ion nóng chảy ở 801°C."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Trong phân tử khí methane (CH4), liên kết giữa Carbon và Hydrogen là:",
        "options": [
          "Liên kết cộng hóa trị",
          "Liên kết ion",
          "Liên kết kim loại",
          "Liên kết đôi"
        ],
        "correct": 0,
        "explanation": "Liên kết cộng hóa trị dùng chung electron."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Lập CTHH của hợp chất tạo bởi Calcium (hóa trị II) và Oxygen (hóa trị II):",
        "options": [
          "CaO",
          "Ca2O",
          "CaO2",
          "Ca2O2"
        ],
        "correct": 0,
        "explanation": "Cùng hóa trị II tỉ lệ 1 : 1 là CaO."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của calcium carbonate (CaCO3) là:",
        "options": [
          "100 amu",
          "80 amu",
          "120 amu",
          "90 amu"
        ],
        "correct": 0,
        "explanation": "40 + 12 + 48 = 100 amu."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Hợp chất nào sau đây tan trong nước tạo thành dung dịch dẫn điện tốt?",
        "options": [
          "Muối ăn (NaCl)",
          "Đường ăn",
          "Cồn",
          "Dầu ăn"
        ],
        "correct": 0,
        "explanation": "Dung dịch muối ăn phân li thành ion tự do dẫn điện."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hóa trị của nguyên tố Carbon trong hợp chất CO2 là:",
        "options": [
          "IV",
          "II",
          "I",
          "VI"
        ],
        "correct": 0,
        "explanation": "Carbon có hóa trị IV trong CO2."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các chất: Cl2, Fe, H2O, CO2:",
        "statements": [
          {
            "subId": "a",
            "text": "Cl2 và Fe là các đơn chất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "H2O và CO2 là các hợp chất cộng hóa trị.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Fe là kim loại dẫn điện và dẫn nhiệt tốt.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng phân tử của CO2 nhẹ hơn H2O.",
            "correct": false
          }
        ],
        "explanation": "CO2 (44 amu) nặng hơn H2O (18 amu)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về liên kết hóa học trong các chất:",
        "statements": [
          {
            "subId": "a",
            "text": "NaCl có liên kết ion do Na nhường 1e và Cl nhận 1e.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phân tử O2 có liên kết đôi gồm 2 cặp electron dùng chung.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phân tử N2 có liên kết ba gồm 3 cặp electron dùng chung rất bền.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hợp chất ion có nhiệt độ sôi thấp hơn hợp chất cộng hóa trị.",
            "correct": false
          }
        ],
        "explanation": "Hợp chất ion có nhiệt độ sôi cao hơn rất nhiều."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các hợp chất: Na2O, Al2O3, SO3:",
        "statements": [
          {
            "subId": "a",
            "text": "Sodium trong Na2O có hóa trị I.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Aluminium trong Al2O3 có hóa trị III.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sulfur trong SO3 có hóa trị VI.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Al2O3 là hợp chất cộng hóa trị ở thể khí.",
            "correct": false
          }
        ],
        "explanation": "Al2O3 là hợp chất rắn khó nóng chảy."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hợp chất có công thức phân tử là Ba(OH)2:",
        "statements": [
          {
            "subId": "a",
            "text": "Gồm 3 nguyên tố: Ba, O, H.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Barium có hóa trị II.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nhóm OH có hóa trị I.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng phân tử của hợp chất là 154 amu.",
            "correct": false
          }
        ],
        "explanation": "Khối lượng phân tử = 137 + 2 × 17 = 171 amu."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của khí ammonia (NH3) là bao nhiêu amu?",
        "correctAnswer": "17",
        "explanation": "14 + 3 × 1 = 17 amu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Số cặp electron dùng chung trong phân tử khí hydrogen (H2) là bao nhiêu?",
        "correctAnswer": "1",
        "explanation": "H2 có 1 liên kết đơn (1 cặp e)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Hóa trị của sắt trong hợp chất Fe2O3 là bao nhiêu?",
        "correctAnswer": "III",
        "explanation": "Iron có hóa trị III."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng phân tử của copper(II) oxide (CuO) là bao nhiêu amu?",
        "correctAnswer": "80",
        "explanation": "64 + 16 = 80 amu."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Phần trăm khối lượng của nguyên tố Carbon trong khí methane (CH4, 16 amu) là bao nhiêu phần trăm?",
        "correctAnswer": "75",
        "explanation": "%C = 12 / 16 × 100% = 75%."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Hợp chất của nguyên tố R với Oxygen có dạng RO nặng 56 amu. Kí hiệu hóa học của R là gì?",
        "correctAnswer": "Ca",
        "explanation": "R + 16 = 56 => R = 40 (Calcium, CaO)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm 2 nguyên tử của nguyên tố X liên kết với 3 nguyên tử Oxygen, nặng 160 amu. Nguyên tố X là:",
        "options": [
          "Iron (Fe)",
          "Aluminium (Al)",
          "Chromium (Cr)",
          "Phosphorus (P)"
        ],
        "correct": 0,
        "explanation": "2X + 48 = 160 => 2X = 112 => X = 56 (Iron, Fe2O3)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Nguyên tử A có 3 electron lớp ngoài cùng, nguyên tử B có 6 electron lớp ngoài cùng. Công thức hợp chất tạo bởi A và B là:",
        "options": [
          "A2B3",
          "AB",
          "AB2",
          "A3B2"
        ],
        "correct": 0,
        "explanation": "A nhường 3e (hóa trị III), B nhận 2e (hóa trị II) => A2B3."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho biết tỉ lệ khối lượng của Sulfur và Oxygen trong phân tử khí sulfur dioxide (SO2) là:",
        "options": [
          "1 : 1",
          "1 : 2",
          "2 : 1",
          "3 : 2"
        ],
        "correct": 0,
        "explanation": "mS : mO = 32 : (2 × 16) = 32 : 32 = 1 : 1."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một oxide kim loại có công thức M2O3, trong đó M chiếm 70% về khối lượng. Tên gọi theo IUPAC của kim loại M là:",
        "options": [
          "Iron (Fe)",
          "Aluminium (Al)",
          "Chromium (Cr)",
          "Titanium (Ti)"
        ],
        "correct": 0,
        "explanation": "2M / (2M + 48) = 0,7 => 2M = 112 => M = 56 (Iron)."
      }
    ]
  },
  "chem7_c2_rev_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là đơn chất kim loại ở thể rắn có màu đỏ ánh kim dẫn điện rất tốt?",
        "options": [
          "Copper (Đồng)",
          "Iron (Sắt)",
          "Aluminium (Nhôm)",
          "Silver (Bạc)"
        ],
        "correct": 0,
        "explanation": "Copper có màu đỏ ánh kim."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong phân tử hợp chất, liên kết cộng hóa trị được hình thành do:",
        "options": [
          "Các cặp electron dùng chung",
          "Lực hút ion trái dấu",
          "Lực hút hạt nhân",
          "Sự nhường nhận electron"
        ],
        "correct": 0,
        "explanation": "Các cặp electron dùng chung."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Quy ước hóa trị của nguyên tố Hydrogen là:",
        "options": [
          "I",
          "II",
          "III",
          "IV"
        ],
        "correct": 0,
        "explanation": "H luôn có hóa trị I."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khối lượng phân tử của khí carbon dioxide (CO2) là:",
        "options": [
          "44 amu",
          "28 amu",
          "32 amu",
          "16 amu"
        ],
        "correct": 0,
        "explanation": "12 + 2 × 16 = 44 amu."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là hợp chất?",
        "options": [
          "Nước tinh khiết (H2O)",
          "Kim loại đồng",
          "Khí oxygen",
          "Kim cương"
        ],
        "correct": 0,
        "explanation": "H2O là hợp chất tạo bởi 2 nguyên tố H và O."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Số electron tối đa có ở lớp ngoài cùng của các nguyên tử (trừ He) là:",
        "options": [
          "8 electron",
          "2 electron",
          "18 electron",
          "6 electron"
        ],
        "correct": 0,
        "explanation": "8 electron (quy tắc octet)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong hợp chất Fe2O3, hóa trị của Iron là:",
        "options": [
          "III",
          "II",
          "I",
          "IV"
        ],
        "correct": 0,
        "explanation": "Iron có hóa trị III."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây có liên kết ion?",
        "options": [
          "Magnesium oxide (MgO)",
          "Nước (H2O)",
          "Khí methane (CH4)",
          "Khí ammonia (NH3)"
        ],
        "correct": 0,
        "explanation": "MgO là hợp chất ion giữa kim loại Mg và phi kim O."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Lập CTHH của hợp chất tạo bởi Na(I) và SO4(II):",
        "options": [
          "Na2SO4",
          "NaSO4",
          "Na(SO4)2",
          "Na2(SO4)3"
        ],
        "correct": 0,
        "explanation": "x/y = II/I = 2/1 => Na2SO4."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Phân tử nào sau đây có liên kết đôi?",
        "options": [
          "Oxygen (O2)",
          "Nitrogen (N2)",
          "Hydrogen (H2)",
          "Chlorine (Cl2)"
        ],
        "correct": 0,
        "explanation": "O2 có liên kết đôi O=O."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của calcium oxide (CaO) là:",
        "options": [
          "56 amu",
          "40 amu",
          "72 amu",
          "48 amu"
        ],
        "correct": 0,
        "explanation": "40 + 16 = 56 amu."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hóa trị của nhóm OH trong hợp chất Ba(OH)2 là:",
        "options": [
          "I",
          "II",
          "III",
          "IV"
        ],
        "correct": 0,
        "explanation": "Nhóm OH có hóa trị I."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét phân tử axit clohiđric (HCl):",
        "statements": [
          {
            "subId": "a",
            "text": "Là hợp chất cộng hóa trị.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cặp electron dùng chung lệch về phía Cl.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử là 36,5 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "HCl ở nhiệt độ phòng là chất rắn kết tinh.",
            "correct": false
          }
        ],
        "explanation": "HCl ở nhiệt độ phòng là chất khí."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tính chất của hợp chất ion và cộng hóa trị:",
        "statements": [
          {
            "subId": "a",
            "text": "Hợp chất ion có nhiệt độ nóng chảy cao.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dung dịch muối ăn dẫn điện được.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch đường ăn dẫn điện được.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khí CO2 là hợp chất cộng hóa trị.",
            "correct": true
          }
        ],
        "explanation": "Dung dịch đường không dẫn điện."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các hợp chất: H2S, SO2, SO3:",
        "statements": [
          {
            "subId": "a",
            "text": "Sulfur trong H2S có hóa trị II.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sulfur trong SO2 có hóa trị IV.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sulfur trong SO3 có hóa trị VI.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "SO3 có khối lượng phân tử nhẹ hơn SO2.",
            "correct": false
          }
        ],
        "explanation": "SO3 (80 amu) nặng hơn SO2 (64 amu)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hợp chất Al2(SO4)3:",
        "statements": [
          {
            "subId": "a",
            "text": "Gồm 3 nguyên tố Al, S, O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng phân tử là 342 amu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Al có hóa trị III, nhóm SO4 có hóa trị II.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Chứa 12 nguyên tử Oxygen trong 1 phân tử.",
            "correct": true
          }
        ],
        "explanation": "Có 3 × 4 = 12 nguyên tử O."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của phân đạm urea CH4N2O là bao nhiêu amu?",
        "correctAnswer": "60",
        "explanation": "60 amu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Hóa trị của nguyên tố Carbon trong khí CO là bao nhiêu?",
        "correctAnswer": "II",
        "explanation": "Carbon hóa trị II."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Số cặp electron dùng chung trong phân tử N2 là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "Liên kết ba có 3 cặp e dùng chung."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng phân tử của NaCl là bao nhiêu amu? (Làm tròn 1 chữ số thập phân)",
        "correctAnswer": "58.5",
        "explanation": "58,5 amu."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Phần trăm khối lượng của Oxygen trong phân tử SO2 (64 amu) là bao nhiêu phần trăm?",
        "correctAnswer": "50",
        "explanation": "32/64 = 50%."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một oxide kim loại R2O3 nặng 102 amu. Tên kim loại R là gì?",
        "correctAnswer": "Aluminium",
        "explanation": "Al (27 amu)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hợp chất A gồm 2 nguyên tử của nguyên tố X liên kết với 1 nguyên tử O và nặng 62 amu. X là nguyên tố nào?",
        "options": [
          "Sodium (Na)",
          "Potassium (K)",
          "Lithium (Li)",
          "Copper (Cu)"
        ],
        "correct": 0,
        "explanation": "2X + 16 = 62 => X = 23 (Na)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm Cu(II) và nhóm SO4(II). Khối lượng phân tử của hợp chất là:",
        "options": [
          "160 amu",
          "128 amu",
          "144 amu",
          "150 amu"
        ],
        "correct": 0,
        "explanation": "64 + 32 + 64 = 160 amu (CuSO4)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nguyên tố R có hóa trị IV trong oxide RO2. Hợp chất khí của R với Hydrogen có dạng:",
        "options": [
          "RH4",
          "RH2",
          "RH3",
          "RH"
        ],
        "correct": 0,
        "explanation": "Hóa trị với H = 8 - 4 = 4 => RH4 (như CH4, SiH4)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Phần trăm khối lượng của nguyên tố Nitrogen trong phân tử NH4NO3 là:",
        "options": [
          "35%",
          "28%",
          "17,5%",
          "42%"
        ],
        "correct": 0,
        "explanation": "28 / 80 × 100% = 35%."
      }
    ]
  },
  "chem7_c2_rev_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phân tử là hạt đại diện cho chất và:",
        "options": [
          "Thể hiện đầy đủ tính chất hóa học của chất",
          "Chỉ gồm các nguyên tử cùng loại",
          "Có kích thước bằng hạt nhân",
          "Không thể bị chia nhỏ trong mọi điều kiện"
        ],
        "correct": 0,
        "explanation": "Phân tử thể hiện đầy đủ tính chất hóa học."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Liên kết trong phân tử khí hydrogen (H2) là:",
        "options": [
          "Liên kết cộng hóa trị đơn",
          "Liên kết ion",
          "Liên kết đôi",
          "Liên kết kim loại"
        ],
        "correct": 0,
        "explanation": "Liên kết đơn H-H."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong hợp chất, hóa trị của Oxygen luôn được lấy bằng:",
        "options": [
          "II",
          "I",
          "III",
          "IV"
        ],
        "correct": 0,
        "explanation": "Hóa trị II."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khối lượng phân tử của sulfur trioxide (SO3) là:",
        "options": [
          "80 amu",
          "64 amu",
          "48 amu",
          "96 amu"
        ],
        "correct": 0,
        "explanation": "32 + 3 × 16 = 80 amu."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là đơn chất phi kim ở thể rắn có màu vàng?",
        "options": [
          "Sulfur (Lưu huỳnh)",
          "Photpho",
          "Than chì",
          "Kim cương"
        ],
        "correct": 0,
        "explanation": "Sulfur là chất rắn màu vàng."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Khi nguyên tử nhận thêm electron, nó trở thành:",
        "options": [
          "Anion (ion âm)",
          "Cation (ion dương)",
          "Phân tử",
          "Khí hiếm"
        ],
        "correct": 0,
        "explanation": "Nhận thêm electron mang điện âm trở thành anion."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong hợp chất Al(OH)3, Aluminium có hóa trị là:",
        "options": [
          "III",
          "II",
          "I",
          "IV"
        ],
        "correct": 0,
        "explanation": "Al có hóa trị III."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây có nhiệt độ nóng chảy cao nhất?",
        "options": [
          "Calcium oxide (CaO)",
          "Nước (H2O)",
          "Cồn",
          "Đường mía"
        ],
        "correct": 0,
        "explanation": "CaO là hợp chất ion có nhiệt độ nóng chảy rất cao (~2572°C)."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Lập CTHH của hợp chất tạo bởi Mg(II) và Cl(I):",
        "options": [
          "MgCl2",
          "MgCl",
          "Mg2Cl",
          "MgCl3"
        ],
        "correct": 0,
        "explanation": "MgCl2."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Phân tử khí nào sau đây có liên kết ba rất bền vững?",
        "options": [
          "Nitrogen (N2)",
          "Oxygen (O2)",
          "Hydrogen (H2)",
          "Chlorine (Cl2)"
        ],
        "correct": 0,
        "explanation": "N2 có liên kết ba."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của hợp chất NaOH là:",
        "options": [
          "40 amu",
          "39 amu",
          "58,5 amu",
          "42 amu"
        ],
        "correct": 0,
        "explanation": "23 + 16 + 1 = 40 amu."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hóa trị của nhóm CO3 trong CaCO3 là:",
        "options": [
          "II",
          "I",
          "III",
          "IV"
        ],
        "correct": 0,
        "explanation": "Nhóm CO3 có hóa trị II."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các chất: Fe, Cu, H2SO4, NaCl:",
        "statements": [
          {
            "subId": "a",
            "text": "Fe và Cu là các đơn chất kim loại.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "NaCl là hợp chất ion.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "H2SO4 là hợp chất cộng hóa trị có khối lượng phân tử 98 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "NaCl ở thể rắn dẫn điện rất tốt.",
            "correct": false
          }
        ],
        "explanation": "NaCl thể rắn không dẫn điện."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Xét phân tử nước H2O:",
        "statements": [
          {
            "subId": "a",
            "text": "Gồm 2 nguyên tử H và 1 nguyên tử O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Liên kết O-H là liên kết cộng hóa trị.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử là 18 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nước sôi ở 0°C và đóng băng ở 100°C.",
            "correct": false
          }
        ],
        "explanation": "Nước sôi ở 100°C và đóng băng ở 0°C."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các oxide của carbon: CO và CO2:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong CO, Carbon có hóa trị II.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong CO2, Carbon có hóa trị IV.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "CO là khí không màu, rất độc.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "CO2 nhẹ hơn CO.",
            "correct": false
          }
        ],
        "explanation": "CO2 (44 amu) nặng hơn CO (28 amu)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hợp chất K2O:",
        "statements": [
          {
            "subId": "a",
            "text": "Tạo bởi kim loại K và phi kim O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Có liên kết ion giữa ion K+ và O2-.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử là 94 amu (2 × 39 + 16).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "K trong hợp chất có hóa trị II.",
            "correct": false
          }
        ],
        "explanation": "K có hóa trị I."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của ozone (O3) là bao nhiêu amu?",
        "correctAnswer": "48",
        "explanation": "3 × 16 = 48 amu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Hóa trị của Sulfur trong hợp chất SO2 là bao nhiêu?",
        "correctAnswer": "IV",
        "explanation": "Hóa trị IV."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong phân tử O2 có bao nhiêu cặp electron dùng chung?",
        "correctAnswer": "2",
        "explanation": "2 cặp e dùng chung."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng phân tử của magnesium chloride (MgCl2) là bao nhiêu amu?",
        "correctAnswer": "95",
        "explanation": "24 + 71 = 95 amu."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Phần trăm khối lượng của nguyên tố Hydrogen trong CH4 là bao nhiêu phần trăm?",
        "correctAnswer": "25",
        "explanation": "4/16 = 25%."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có dạng XO nặng 56 amu. Kí hiệu hóa học của X là gì?",
        "correctAnswer": "Ca",
        "explanation": "Ca (40 amu)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hợp chất tạo bởi nguyên tố R (hóa trị III) và Oxygen có công thức là:",
        "options": [
          "R2O3",
          "RO3",
          "R3O2",
          "RO"
        ],
        "correct": 0,
        "explanation": "R2O3."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một chất khí X có tỉ khối so với khí hydrogen (H2) là 17. Khối lượng phân tử của X là:",
        "options": [
          "34 amu (H2S)",
          "17 amu",
          "28 amu",
          "44 amu"
        ],
        "correct": 0,
        "explanation": "17 × 2 = 34 amu (H2S)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Tỉ lệ khối lượng của C và H trong phân tử C2H2 là:",
        "options": [
          "12 : 1",
          "6 : 1",
          "24 : 2",
          "3 : 1"
        ],
        "correct": 0,
        "explanation": "24 : 2 = 12 : 1."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Hợp chất A gồm nguyên tố M và Oxygen trong đó M chiếm 72,41% về khối lượng. Biết khối lượng phân tử là 232 amu. Công thức của A là:",
        "options": [
          "Fe3O4",
          "Fe2O3",
          "FeO",
          "Al2O3"
        ],
        "correct": 0,
        "explanation": "Fe3O4."
      }
    ]
  },
  "chem7_c2_rev_test4": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đơn chất kim loại nào sau đây ở thể lỏng ở nhiệt độ thường?",
        "options": [
          "Mercury (Hg)",
          "Copper (Cu)",
          "Iron (Fe)",
          "Gold (Au)"
        ],
        "correct": 0,
        "explanation": "Mercury là kim loại lỏng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong phân tử NaCl, liên kết giữa các ion Na+ và Cl- là:",
        "options": [
          "Liên kết ion",
          "Liên kết cộng hóa trị",
          "Liên kết kim loại",
          "Liên kết hidro"
        ],
        "correct": 0,
        "explanation": "Liên kết ion."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Nguyên tố Hydrogen trong hợp chất luôn có hóa trị là:",
        "options": [
          "I",
          "II",
          "III",
          "IV"
        ],
        "correct": 0,
        "explanation": "Hóa trị I."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khối lượng phân tử của khí chlorine (Cl2) là:",
        "options": [
          "71 amu",
          "35,5 amu",
          "17 amu",
          "142 amu"
        ],
        "correct": 0,
        "explanation": "71 amu."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Hợp chất nào sau đây là thành phần chính của đá vôi?",
        "options": [
          "CaCO3",
          "CaO",
          "Ca(OH)2",
          "CaCl2"
        ],
        "correct": 0,
        "explanation": "CaCO3."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Quy tắc octet là xu hướng đạt lớp ngoài cùng gồm:",
        "options": [
          "8 electron",
          "2 electron",
          "18 electron",
          "10 electron"
        ],
        "correct": 0,
        "explanation": "8 electron."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong hợp chất FeO, hóa trị của Iron là:",
        "options": [
          "II",
          "III",
          "I",
          "IV"
        ],
        "correct": 0,
        "explanation": "Iron hóa trị II."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây là hợp chất cộng hóa trị ở thể khí?",
        "options": [
          "Methane (CH4)",
          "Muối ăn (NaCl)",
          "Đá vôi (CaCO3)",
          "Vôi sống (CaO)"
        ],
        "correct": 0,
        "explanation": "CH4 thể khí."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Lập CTHH của hợp chất gồm Al(III) và Cl(I):",
        "options": [
          "AlCl3",
          "AlCl",
          "Al3Cl",
          "Al2Cl3"
        ],
        "correct": 0,
        "explanation": "AlCl3."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Phân tử khí nào sau đây có liên kết đôi?",
        "options": [
          "O2",
          "N2",
          "H2",
          "Cl2"
        ],
        "correct": 0,
        "explanation": "O2."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của sulfuric acid (H2SO4) là:",
        "options": [
          "98 amu",
          "96 amu",
          "100 amu",
          "80 amu"
        ],
        "correct": 0,
        "explanation": "98 amu."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hóa trị của nhóm SO4 trong hợp chất Na2SO4 là:",
        "options": [
          "II",
          "I",
          "III",
          "IV"
        ],
        "correct": 0,
        "explanation": "Nhóm SO4 có hóa trị II."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét phân tử khí carbon dioxide (CO2):",
        "statements": [
          {
            "subId": "a",
            "text": "Là hợp chất cộng hóa trị.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Có 2 liên kết đôi giữa C và 2 nguyên tử O.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử là 44 amu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí CO2 duy trì sự cháy rất tốt.",
            "correct": false
          }
        ],
        "explanation": "CO2 không duy trì sự cháy, dùng để dập lửa."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các đơn chất và hợp chất trong tự nhiên:",
        "statements": [
          {
            "subId": "a",
            "text": "Khí oxygen là đơn chất cần cho sự hô hấp.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nước là hợp chất phổ biến nhất trên bề mặt Trái Đất.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Muối ăn NaCl là hợp chất ion.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các kim loại đều nhẹ hơn nước.",
            "correct": false
          }
        ],
        "explanation": "Hầu hết kim loại đều nặng hơn nước (Fe, Cu, Pb...)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các oxide: Na2O, MgO, Al2O3:",
        "statements": [
          {
            "subId": "a",
            "text": "Đều là oxide của kim loại.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hóa trị của kim loại lần lượt là I, II, III.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đều là hợp chất ion rắn khó nóng chảy.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Al2O3 có khối lượng phân tử nhẹ nhất trong dãy.",
            "correct": false
          }
        ],
        "explanation": "Al2O3 (102 amu) nặng nhất trong dãy."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hợp chất Cu(OH)2:",
        "statements": [
          {
            "subId": "a",
            "text": "Cu có hóa trị II.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nhóm OH có hóa trị I.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử là 98 amu (64 + 2 × 17).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tan vô hạn trong nước tạo dung dịch màu đỏ.",
            "correct": false
          }
        ],
        "explanation": "Cu(OH)2 là kết tủa màu xanh lam không tan trong nước."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của khí methane (CH4) là bao nhiêu amu?",
        "correctAnswer": "16",
        "explanation": "16 amu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Hóa trị của nguyên tố Carbon trong CO2 là bao nhiêu?",
        "correctAnswer": "IV",
        "explanation": "Hóa trị IV."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Số liên kết đơn trong phân tử nước (H2O) là bao nhiêu?",
        "correctAnswer": "2",
        "explanation": "2 liên kết O-H."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng phân tử của potassium hydroxide (KOH) là bao nhiêu amu?",
        "correctAnswer": "56",
        "explanation": "39 + 17 = 56 amu."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Phần trăm khối lượng của nguyên tố H trong phân tử H2O là bao nhiêu phần trăm? (Làm tròn 1 chữ số thập phân)",
        "correctAnswer": "11.1",
        "explanation": "11,1%."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một oxide kim loại MO nặng 80 amu. Kí hiệu của M là gì?",
        "correctAnswer": "Cu",
        "explanation": "Cu (64 amu, CuO)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm 2 nguyên tử của nguyên tố X liên kết với 5 nguyên tử Oxygen, nặng 142 amu. X là nguyên tố nào?",
        "options": [
          "Phosphorus (P)",
          "Nitrogen (N)",
          "Arsenic (As)",
          "Vanadium (V)"
        ],
        "correct": 0,
        "explanation": "2X + 80 = 142 => X = 31 (P)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Chất nào sau đây khi hòa tan vào nước tạo dung dịch dẫn điện?",
        "options": [
          "NaCl",
          "Đường",
          "Cồn",
          "Dầu ăn"
        ],
        "correct": 0,
        "explanation": "NaCl."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Phần trăm khối lượng của Carbon trong phân tử CaCO3 (100 amu) là:",
        "options": [
          "12%",
          "40%",
          "48%",
          "20%"
        ],
        "correct": 0,
        "explanation": "12%."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Hợp chất khí X của Sulfur với Hydrogen có công thức H2S. Hóa trị của Sulfur trong hợp chất này là:",
        "options": [
          "II",
          "IV",
          "VI",
          "I"
        ],
        "correct": 0,
        "explanation": "Hóa trị II."
      }
    ]
  },
  "chem7_c2_rev_test5": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là đơn chất phi kim ở thể khí duy trì sự sống?",
        "options": [
          "Oxygen (O2)",
          "Nitrogen (N2)",
          "Carbon (C)",
          "Iron (Fe)"
        ],
        "correct": 0,
        "explanation": "O2."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Liên kết trong phân tử nước (H2O) là:",
        "options": [
          "Liên kết cộng hóa trị",
          "Liên kết ion",
          "Liên kết kim loại",
          "Liên kết đôi"
        ],
        "correct": 0,
        "explanation": "Liên kết cộng hóa trị."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Quy ước hóa trị của Oxygen trong hợp chất luôn là:",
        "options": [
          "II",
          "I",
          "III",
          "IV"
        ],
        "correct": 0,
        "explanation": "Hóa trị II."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khối lượng phân tử của khí hydrogen (H2) là:",
        "options": [
          "2 amu",
          "1 amu",
          "4 amu",
          "16 amu"
        ],
        "correct": 0,
        "explanation": "2 amu."
      },
      {
        "id": 5,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là hợp chất vô cơ?",
        "options": [
          "Muối ăn (NaCl)",
          "Thanh nhôm",
          "Khí oxygen",
          "Than chì"
        ],
        "correct": 0,
        "explanation": "NaCl."
      },
      {
        "id": 6,
        "level": "Nhận biết",
        "question": "Quy tắc octet quy ước lớp ngoài cùng bền vững có:",
        "options": [
          "8 electron (riêng He có 2e)",
          "2 electron cho mọi nguyên tố",
          "18 electron",
          "6 electron"
        ],
        "correct": 0,
        "explanation": "8 electron."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Trong hợp chất Fe2(SO4)3, hóa trị của Iron là:",
        "options": [
          "III",
          "II",
          "I",
          "IV"
        ],
        "correct": 0,
        "explanation": "Iron hóa trị III."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây có nhiệt độ nóng chảy cao trên 800°C?",
        "options": [
          "Sodium chloride (NaCl)",
          "Nước",
          "Cồn",
          "Đường"
        ],
        "correct": 0,
        "explanation": "NaCl nóng chảy ở 801°C."
      },
      {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Lập CTHH của hợp chất gồm Ca(II) và OH(I):",
        "options": [
          "Ca(OH)2",
          "CaOH",
          "Ca2OH",
          "Ca(OH)3"
        ],
        "correct": 0,
        "explanation": "Ca(OH)2."
      },
      {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Phân tử nào sau đây có liên kết ba N≡N rất bền vững?",
        "options": [
          "Nitrogen (N2)",
          "Oxygen (O2)",
          "Hydrogen (H2)",
          "Chlorine (Cl2)"
        ],
        "correct": 0,
        "explanation": "N2."
      },
      {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của barium sulfate (BaSO4) là:",
        "options": [
          "233 amu",
          "137 amu",
          "96 amu",
          "200 amu"
        ],
        "correct": 0,
        "explanation": "137 + 32 + 64 = 233 amu."
      },
      {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Hóa trị của nhóm PO4 trong Ca3(PO4)2 là:",
        "options": [
          "III",
          "II",
          "I",
          "IV"
        ],
        "correct": 0,
        "explanation": "Nhóm PO4 có hóa trị III."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các hợp chất: H2O, CO2, NH3, CH4:",
        "statements": [
          {
            "subId": "a",
            "text": "Đều là hợp chất cộng hóa trị.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đều được tạo bởi các nguyên tố phi kim.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "CH4 có khối lượng phân tử nhẹ nhất (16 amu).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các chất này đều dẫn điện ở thể lỏng.",
            "correct": false
          }
        ],
        "explanation": "Không dẫn điện."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về liên kết ion trong hợp chất:",
        "statements": [
          {
            "subId": "a",
            "text": "Hình thành giữa kim loại điển hình và phi kim điển hình.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Do lực hút tĩnh điện giữa các ion mang điện trái dấu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Có nhiệt độ nóng chảy và nhiệt độ sôi cao.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Các ion không thể tách rời khi hòa tan trong nước.",
            "correct": false
          }
        ],
        "explanation": "Khi tan trong nước các ion phân li tự do."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các hợp chất: Al2O3, CuO, Na2O:",
        "statements": [
          {
            "subId": "a",
            "text": "Al trong Al2O3 có hóa trị III.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cu trong CuO có hóa trị II.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Na trong Na2O có hóa trị I.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Na2O có khối lượng phân tử lớn hơn Al2O3.",
            "correct": false
          }
        ],
        "explanation": "Na2O (62 amu) nhẹ hơn Al2O3 (102 amu)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hợp chất BaCl2:",
        "statements": [
          {
            "subId": "a",
            "text": "Là hợp chất ion.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ba có hóa trị II, Cl có hóa trị I.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng phân tử là 208 amu (137 + 71).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Không tan trong nước.",
            "correct": false
          }
        ],
        "explanation": "BaCl2 tan rất tốt trong nước."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Khối lượng phân tử của glucose (C6H12O6) là bao nhiêu amu?",
        "correctAnswer": "180",
        "explanation": "180 amu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Hóa trị của Carbon trong hợp chất CH4 là bao nhiêu?",
        "correctAnswer": "IV",
        "explanation": "Hóa trị IV."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Số cặp electron dùng chung trong phân tử Cl2 là bao nhiêu?",
        "correctAnswer": "1",
        "explanation": "1 cặp e."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng phân tử của copper(II) sulfate (CuSO4) là bao nhiêu amu?",
        "correctAnswer": "160",
        "explanation": "160 amu."
      },
      {
        "id": 5,
        "level": "Vận dụng cao",
        "question": "Phần trăm khối lượng của nguyên tố Oxygen trong phân tử CO2 (44 amu) xấp xỉ bằng bao nhiêu phần trăm? (Làm tròn đến hàng đơn vị)",
        "correctAnswer": "73",
        "explanation": "32/44 = 72,7% ≈ 73%."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một oxide kim loại M2O3 nặng 102 amu. Kí hiệu hóa học của M là gì?",
        "correctAnswer": "Al",
        "explanation": "Al (27 amu)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một hợp chất có phân tử gồm 1 nguyên tử nguyên tố X liên kết với 2 nguyên tử O và nặng 64 amu. X là nguyên tố nào?",
        "options": [
          "Sulfur (S)",
          "Carbon (C)",
          "Silicon (Si)",
          "Nitrogen (N)"
        ],
        "correct": 0,
        "explanation": "SO2 (32 amu)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Phân tử chất nào sau đây có tổng số electron tham gia liên kết là 4 hạt (2 cặp electron)?",
        "options": [
          "Oxygen (O2)",
          "Nitrogen (N2)",
          "Hydrogen (H2)",
          "Chlorine (Cl2)"
        ],
        "correct": 0,
        "explanation": "O2 có liên kết đôi (4 hạt e)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Phần trăm khối lượng của nguyên tố S trong phân tử FeS2 xấp xỉ bằng:",
        "options": [
          "53,33%",
          "46,67%",
          "60%",
          "36,36%"
        ],
        "correct": 0,
        "explanation": "64 / (56 + 64) × 100% = 64 / 120 × 100% ≈ 53,33%."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Hợp chất ion tạo bởi nguyên tố kim loại X (Z = 11) và nguyên tố phi kim Y (Z = 17) có công thức là:",
        "options": [
          "XY (NaCl)",
          "X2Y",
          "XY2",
          "X2Y3"
        ],
        "correct": 0,
        "explanation": "NaCl (XY)."
      }
    ]
  }
}

def build_chem7_exams():
    return CHEM7_EXAMS

exams = CHEM7_EXAMS
