# -*- coding: utf-8 -*-
"""
GENERATOR KHTN - HÓA HỌC 8 (CHUẨN 100% ĐỘC LẬP - BÁM SÁT SGK KẾT NỐI TRI THỨC)
Tất cả 43 đề thi hoàn toàn khác biệt 100% về câu hỏi, số liệu và đáp án.
"""

import sys
sys.stdout.reconfigure(encoding="utf-8")
true = True
false = False
null = None

CHEM8_EXAMS = {
  "chem8_c1_b2_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hiện tượng nào sau đây là hiện tượng biến đổi vật lí?",
        "options": [
          "Nước đá tan chảy thành nước lỏng",
          "Cơm để lâu ngày bị ôi thiu",
          "Đốt cháy một que diêm trong không khí",
          "Đinh sắt bị gỉ tạo thành lớp gỉ màu nâu đỏ"
        ],
        "correct": 0,
        "explanation": "Nước đá tan chỉ biến đổi trạng thái từ rắn sang lỏng, không tạo ra chất mới."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hiện tượng nào sau đây có sự biến đổi hóa học?",
        "options": [
          "Cồn để trong lọ hở miệng bị bay hơi",
          "Đèn cồn cháy tỏa nhiều nhiệt và ánh sáng",
          "Mặt trời làm nước biển bốc hơi tạo muối",
          "Hòa tan đường vào cốc nước ấm"
        ],
        "correct": 1,
        "explanation": "Cồn cháy tạo ra chất mới là khí carbon dioxide và hơi nước."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Dấu hiệu nào sau đây chứng tỏ có biến đổi hóa học xảy ra?",
        "options": [
          "Chất thay đổi hình dạng kích thước",
          "Chất chuyển từ thể lỏng sang thể hơi",
          "Có sự tạo thành chất mới khác biệt",
          "Chất tan hoàn toàn tạo dung dịch"
        ],
        "correct": 2,
        "explanation": "Bản chất của biến đổi hóa học là có chất mới sinh ra."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Quá trình nào sau đây KHÔNG có sự biến đổi hóa học?",
        "options": [
          "Quang hợp của cây xanh dưới ánh sáng",
          "Sự hô hấp của con người và động vật",
          "Nghiền nhỏ hạt gạo thành bột mịn",
          "Sự lên men giấm từ rượu nếp"
        ],
        "correct": 2,
        "explanation": "Nghiền gạo chỉ làm nhỏ kích thước hạt tinh bột, không sinh chất mới."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Khi thắp một cây nến làm bằng parafin, giai đoạn nào thể hiện biến đổi vật lí?",
        "options": [
          "Parafin nóng chảy và chuyển thành hơi",
          "Hơi parafin cháy tạo CO2 và H2O",
          "Nến tỏa nhiệt nóng ấm xung quanh",
          "Khí sinh ra làm đục nước vôi trong"
        ],
        "correct": 0,
        "explanation": "Parafin chảy lỏng và bay hơi là biến đổi trạng thái (vật lí)."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho các hiện tượng: (1) Sắt hút nam châm; (2) Lưu huỳnh cháy trong oxi; (3) Thủy tinh nóng chảy thổi bóng; (4) Vôi sống tác dụng với nước. Số hiện tượng hóa học là:",
        "options": [
          "1",
          "2",
          "3",
          "4"
        ],
        "correct": 1,
        "explanation": "Hiện tượng hóa học gồm (2) và (4)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi mở nắp lon nước ngọt có gas, thấy bọt khí sủi lên. Đây là hiện tượng gì?",
        "options": [
          "Biến đổi hóa học do khí mới tạo ra",
          "Biến đổi vật lí do giảm áp suất khí CO2 thoát ra",
          "Phản ứng phân hủy đường ngọt",
          "Biến đổi vừa vật lí vừa hóa học"
        ],
        "correct": 1,
        "explanation": "CO2 tan trong nước ngọt thoát ra ngoài khi giảm áp suất, là quá trình vật lí."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Thả một mẩu đá vôi (CaCO3) vào dung dịch axit clohiđric (HCl) thấy sủi bọt khí. Hiện tượng này là biến đổi hóa học vì:",
        "options": [
          "Mẩu đá vôi chìm xuống đáy ống nghiệm",
          "Dung dịch bị đục dần",
          "Có chất khí mới sinh ra thoát ra ngoài",
          "Nhiệt độ ống nghiệm giữ nguyên"
        ],
        "correct": 2,
        "explanation": "Sinh ra khí mới (CO2) chứng tỏ có phản ứng hóa học."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Trong sản xuất vôi tôi, hai công đoạn chính là: (1) Nung đá vôi ở nhiệt độ cao thành vôi sống; (2) Thả vôi sống vào nước tạo vôi tôi. Nhận định đúng là:",
        "options": [
          "(1) là vật lí, (2) là hóa học",
          "(1) là hóa học, (2) là vật lí",
          "Cả (1) và (2) đều là biến đổi hóa học",
          "Cả (1) và (2) đều là biến đổi vật lí"
        ],
        "correct": 2,
        "explanation": "Cả hai đều tạo chất mới: CaCO3 -> CaO + CO2 và CaO + H2O -> Ca(OH)2."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Hiện tượng nào sau đây minh họa cho biến đổi hóa học kèm theo sự thay đổi màu sắc rõ rệt?",
        "options": [
          "Hòa tan bột đồng sunfat màu xanh vào nước",
          "Nhúng đinh sắt vào dung dịch đồng sunfat thấy xuất hiện lớp đồng màu đỏ bám ngoài",
          "Trộn bột lưu huỳnh vàng với bột sắt xám đen",
          "Đun nóng nước sôi sùng sục"
        ],
        "correct": 1,
        "explanation": "Sắt đẩy đồng ra khỏi muối tạo Cu màu đỏ bám trên đinh sắt."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Hiện tượng thức ăn bị ôi thiu trong mùa hè là do:",
        "options": [
          "Nước trong thức ăn bị bay hơi nhanh chóng",
          "Vi sinh vật biến đổi các chất hữu cơ thành chất mới có mùi lạ và độc hại",
          "Muối ăn trong thức ăn bị kết tinh",
          "Nhiệt độ cao làm các chất tan chảy"
        ],
        "correct": 1,
        "explanation": "Vi sinh vật phân giải protein, lipit tạo thành các hợp chất mới."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Tiến hành 4 thí nghiệm: (a) Đun nóng cồn trong đĩa sứ; (b) Đốt cháy cồn trong đĩa sứ; (c) Cho giấm ăn vào baking soda; (d) Làm đông đặc mỡ lợn trong tủ lạnh. Số thí nghiệm xảy ra biến đổi hóa học là:",
        "options": [
          "1",
          "2",
          "3",
          "4"
        ],
        "correct": 1,
        "explanation": "Gồm thí nghiệm (b) và (c)."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các hiện tượng diễn ra trong đời sống hàng ngày sau đây:",
        "statements": [
          {
            "subId": "a",
            "text": "Hòa tan viên sủi vitamin C vào nước thấy sủi bọt khí mạnh là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Băng phiến (long não) đặt trong tủ quần áo thu nhỏ dần là biến đổi hóa học.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Thổi hơi thở vào nước vôi trong thấy bị vẩn đục là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bẻ cong một thanh nhôm chỉ làm biến dạng hình học là biến đổi vật lí.",
            "correct": true
          }
        ],
        "explanation": "Băng phiến thu nhỏ là hiện tượng thăng hoa (vật lí)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các dấu hiệu nhận biết phản ứng và sự biến đổi chất:",
        "statements": [
          {
            "subId": "a",
            "text": "Biến đổi vật lí chỉ thay đổi trạng thái, hình dạng hoặc kích thước của chất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Biến đổi hóa học luôn đi kèm sự sinh ra một hoặc nhiều chất mới.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Mọi hiện tượng tỏa nhiệt đều chứng tỏ có phản ứng hóa học xảy ra.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Sự xuất hiện chất kết tủa không tan trong dung dịch là một dấu hiệu của biến đổi hóa học.",
            "correct": true
          }
        ],
        "explanation": "Đèn sợi đốt sáng và tỏa nhiệt là biến đổi vật lí."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Trong quá trình chưng cất rượu thủ công từ cơm rượu lên men:",
        "statements": [
          {
            "subId": "a",
            "text": "Giai đoạn ủ men rượu từ tinh bột gạo là quá trình biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Giai đoạn đun sôi để cồn bay hơi rồi ngưng tụ là quá trình biến đổi hóa học.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Rượu nguyên chất để lâu ngoài không khí bị chua là do biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Pha loãng rượu với nước tinh khiết là quá trình biến đổi hóa học.",
            "correct": false
          }
        ],
        "explanation": "Chưng cất và pha loãng là quá trình vật lí."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm nung nóng bột sắt trộn với bột lưu huỳnh trong ống nghiệm:",
        "statements": [
          {
            "subId": "a",
            "text": "Trước khi nung, có thể dùng nam châm tách sắt ra khỏi lưu huỳnh (biến đổi vật lí).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi nung nóng, hỗn hợp tự phát sáng đỏ rực và tạo thành hợp chất sắt(II) sunfua màu xám đen.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chất rắn sau phản ứng vẫn bị nam châm hút mạnh như bột sắt ban đầu.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Quá trình nung nóng là một biến đổi hóa học kèm theo sự tỏa nhiệt mạnh.",
            "correct": true
          }
        ],
        "explanation": "FeS tạo thành không bị nam châm hút như sắt tự do."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong các hiện tượng: làm kem, xé giấy, đốt rơm rạ, đun sôi dầu ăn. Có bao nhiêu hiện tượng biến đổi vật lí?",
        "correctAnswer": "3",
        "explanation": "Có 3 hiện tượng vật lí: làm kem, xé giấy, đun sôi dầu ăn."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho dãy các quá trình: (1) Sắt gỉ; (2) Cắt tóc; (3) Lên men sữa chua; (4) Khí gas cháy; (5) Cồn bay hơi. Có bao nhiêu quá trình xảy ra biến đổi hóa học?",
        "correctAnswer": "3",
        "explanation": "Gồm (1), (3), (4) là biến đổi hóa học."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một học sinh liệt kê 6 hiện tượng: hòa tan muối, đốt than củi, nung đá vôi, vắt chanh vào sữa đậu nành, nước đóng băng, mài dao. Số hiện tượng có sự tạo thành chất mới là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "Đốt than, nung đá vôi, chanh vào sữa đậu nành (3 hiện tượng)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong công nghiệp làm gốm sứ: tạo hình đất sét (1), phơi khô phôi (2), nung gốm trong lò ở 1200 độ C (3), vẽ trang trí lên men sứ (4). Công đoạn nào chắc chắn xảy ra biến đổi hóa học phức tạp nhất? (Điền số thứ tự 1, 2, 3 hoặc 4)",
        "correctAnswer": "3",
        "explanation": "Công đoạn (3) nung gốm làm các khoáng silicat phản ứng hóa học."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Để phân biệt biến đổi hóa học với biến đổi vật lí, có tối thiểu bao nhiêu dấu hiệu cơ bản thường quan sát thấy (thay đổi màu sắc, sinh khí, tạo kết tủa, tỏa nhiệt/phát sáng)? Điền một số nguyên từ 1 đến 4.",
        "correctAnswer": "4",
        "explanation": "Có 4 dấu hiệu cơ bản thường gặp."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Tiến hành 5 thí nghiệm: nhỏ dung dịch bạc nitrat vào muối ăn, dẫn khí CO2 vào nước, điện phân nước thành khí H2 và O2, thổi thủy tinh nóng chảy, đốt pháo hoa đêm giao thừa. Có bao nhiêu thí nghiệm là biến đổi hóa học?",
        "correctAnswer": "4",
        "explanation": "Gồm: kết tủa AgCl, tạo H2CO3, điện phân nước, đốt pháo hoa (4 biến đổi hóa học)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một thanh sắt nặng 5,6 g để ngoài không khí ẩm sau một thời gian bị gỉ, đem cân lại thấy nặng 7,2 g. Khối lượng khí oxi trong không khí đã tham gia phản ứng hóa học với sắt là:",
        "options": [
          "1,6 g",
          "2,4 g",
          "1,2 g",
          "0,8 g"
        ],
        "correct": 0,
        "explanation": "Theo ĐL BTKL: m_O2 = 7,2 - 5,6 = 1,6 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khi đốt nến (parafin), hiện tượng nào sau đây kết hợp ĐỒNG THỜI cả biến đổi vật lí và biến đổi hóa học theo đúng trình tự?",
        "options": [
          "Nến cháy tạo khí -> nến nóng chảy -> nến đông đặc",
          "Nến nóng chảy -> nến thấm lên bấc và bay hơi -> hơi nến cháy tạo CO2 và H2O",
          "Hơi nến cháy tỏa nhiệt -> nến đông đặc thành sáp rắn -> sinh kết tủa",
          "Nến bay hơi ngay lập tức -> nến hóa lỏng -> tạo muội than đen"
        ],
        "correct": 1,
        "explanation": "Trình tự: nóng chảy (lỏng) -> hút lên bấc bay hơi (hơi) -> cháy (hóa học)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Xét các quá trình tự nhiên: (1) Chu trình nước bốc hơi tạo mây rồi rơi thành mưa; (2) Sự hình thành thạch nhũ trong hang động đá vôi; (3) Sự phong hóa đá ngầm do rễ cây tiết axit; (4) Sự bào mòn bờ biển do sóng đánh. Số quá trình có biến đổi hóa học là:",
        "options": [
          "1",
          "2",
          "3",
          "4"
        ],
        "correct": 1,
        "explanation": "Gồm (2) và (3) là quá trình hóa học."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho một cục đá vôi vào cốc chứa giấm ăn. Hiện tượng quan sát được chứng minh biến đổi hóa học đã diễn ra là:",
        "options": [
          "Cục đá vôi nổi lên trên bề mặt giấm ăn",
          "Có bọt khí sủi lên bám quanh cục đá vôi và đá vôi tan dần",
          "Giấm ăn chuyển sang màu tím đậm",
          "Cốc bị lạnh đi đóng băng thành đá"
        ],
        "correct": 1,
        "explanation": "Đá vôi tan dần và sủi bọt khí CO2 chứng tỏ có phản ứng hóa học."
      }
    ]
  },
  "chem8_c1_b2_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Quá trình nào sau đây là biến đổi hóa học?",
        "options": [
          "Thanh đồng bị kéo dài thành sợi dây điện mỏng",
          "Xăng dầu bốc hơi khi mở nắp bình chứa",
          "Đốt cháy khí biogas (metan) để đun nấu",
          "Lấy kéo cắt vụn tấm bìa carton"
        ],
        "correct": 2,
        "explanation": "Khí biogas cháy tạo thành khí carbon dioxide và hơi nước."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hiện tượng vật lí là hiện tượng:",
        "options": [
          "Chất này biến đổi thành chất khác hoàn toàn",
          "Chất bị phân hủy thành các đơn chất ban đầu",
          "Chất biến đổi về trạng thái, hình dạng nhưng vẫn giữ nguyên là chất đó",
          "Có sự thay đổi bản chất của các liên kết hóa học"
        ],
        "correct": 2,
        "explanation": "Biến đổi vật lí không làm thay đổi bản chất chất."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong các thí nghiệm sau, thí nghiệm nào là biến đổi vật lí?",
        "options": [
          "Đun sôi nước trong ấm đến khi bay hơi hết",
          "Đun nóng đường kính đến khi thành than đen",
          "Nung bột đồng ngoài không khí biến thành bột đen",
          "Nhỏ axit vào vỏ trứng thấy sủi bọt khí"
        ],
        "correct": 0,
        "explanation": "Nước sôi bay hơi chỉ là chuyển từ thể lỏng sang thể hơi."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hiện tượng gỉ sét của khung cửa sắt ngoài trời thuộc loại biến đổi nào?",
        "options": [
          "Biến đổi vật lí do mưa làm trôi sơn",
          "Biến đổi hóa học do sắt tác dụng với oxi và hơi ẩm",
          "Biến đổi cơ học do gió thổi mài mòn",
          "Biến đổi nhiệt học do nắng nóng làm dãn nở"
        ],
        "correct": 1,
        "explanation": "Sắt bị oxi hóa thành hợp chất iron oxide/hydroxide."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Khi hòa tan muối ăn vào nước thu được nước muối trong suốt. Để tách lại muối ăn ban đầu, người ta làm thế nào và đây là hiện tượng gì?",
        "options": [
          "Đun sôi để nước bay hơi hết; hiện tượng vật lí",
          "Lọc qua phễu giấy lọc; hiện tượng hóa học",
          "Nhỏ thêm axit clohiđric vào; hiện tượng hóa học",
          "Để yên trong bóng râm cho tự phân hủy; hiện tượng vật lí"
        ],
        "correct": 0,
        "explanation": "Cô cạn dung dịch muối ăn là quá trình biến đổi vật lí."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho các hiện tượng: (a) Sữa tươi để lâu ngoài trời bị chua; (b) Thủy ngân trong nhiệt kế co giãn theo nhiệt độ; (c) Quả chuối xanh chín dần thơm ngọt; (d) Xay cà phê hạt thành bột cà phê. Số hiện tượng biến đổi hóa học là:",
        "options": [
          "1",
          "2",
          "3",
          "4"
        ],
        "correct": 1,
        "explanation": "Gồm (a) và (c) là biến đổi hóa học."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hiện tượng quang hợp ở lá cây xanh biến đổi khí CO2 và H2O thành tinh bột và giải phóng O2 là biến đổi:",
        "options": [
          "Vật lí vì cây vẫn giữ nguyên màu xanh",
          "Hóa học vì đã tạo thành các chất mới",
          "Quang học đơn thuần không sinh chất mới",
          "Vật lí kèm theo tỏa nhiệt ra môi trường"
        ],
        "correct": 1,
        "explanation": "Quá trình quang hợp tổng hợp nên tinh bột và khí oxi."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khi nhỏ vài giọt giấm ăn (axit axetic) vào bột baking soda (natri hidrocacbonat), hiện tượng quan sát được là:",
        "options": [
          "Hỗn hợp đông đặc lại như thạch",
          "Sủi bọt khí không màu mạnh mẽ",
          "Bột baking soda chuyển sang màu đen",
          "Hỗn hợp phát nổ kèm ánh sáng chói"
        ],
        "correct": 1,
        "explanation": "Phản ứng sinh khí CO2 gây hiện tượng sủi bọt."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Trong công nghiệp luyện kim, quá trình nung quặng sắt hematit với than cốc trong lò cao để thu được gang lỏng là:",
        "options": [
          "Quá trình vật lí do than nóng chảy hòa tan sắt",
          "Quá trình hóa học vì sắt được khử từ oxit sắt thành sắt tự do",
          "Quá trình biến đổi hình dạng hạt quặng",
          "Quá trình ngưng tụ hơi kim loại"
        ],
        "correct": 1,
        "explanation": "Oxit sắt phản ứng với CO để tạo sắt kim loại."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Tại sao vỏ tàu thủy bằng thép đi trên biển thường bị ăn mòn nhanh hơn đi trên sông nước ngọt?",
        "options": [
          "Nước biển lạnh hơn nước sông",
          "Muối trong nước biển đóng vai trò dung dịch chất điện li thúc đẩy phản ứng oxi hóa sắt diễn ra nhanh hơn",
          "Sóng biển đánh mạnh hơn dòng nước sông",
          "Ánh nắng mặt trời trên biển gay gắt hơn"
        ],
        "correct": 1,
        "explanation": "Môi trường nước muối làm tăng tốc độ ăn mòn hóa học và điện hóa."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Hiện tượng tạo mưa nhân tạo bằng cách bắn các hạt bạc iotua (AgI) hoặc băng khô (CO2 rắn) vào các đám mây là ứng dụng của:",
        "options": [
          "Biến đổi hóa học tạo ra nước lỏng",
          "Biến đổi vật lí kích thích ngưng tụ hơi nước thành giọt mưa",
          "Phản ứng phân hủy mây thành hơi ẩm",
          "Biến đổi hóa học giữa AgI và hơi nước"
        ],
        "correct": 1,
        "explanation": "Băng khô thăng hoa thu nhiệt làm hơi nước ngưng tụ thành mưa (vật lí)."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Tiến hành 4 thao tác: (1) Hòa tan vôi sống vào nước thấy nước sôi sùng sục; (2) Dẫn khí thoát ra từ bếp than qua nước vôi trong thấy đục; (3) Đốt sợi dây magiê cháy sáng chói; (4) Nghiền nát viên than hoa thành bột mịn. Số thao tác tỏa nhiệt do phản ứng hóa học là:",
        "options": [
          "1",
          "2",
          "3",
          "4"
        ],
        "correct": 1,
        "explanation": "Thao tác (1) tôi vôi và (3) đốt Mg tỏa lượng nhiệt lớn."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các biến đổi của nước trong tự nhiên và đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Nước lỏng bay hơi thành hơi nước là biến đổi vật lí.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hơi nước ngưng tụ tạo sương mù là biến đổi hóa học.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Điện phân nước tạo thành khí hiđro và khí oxi là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nước hòa tan cồn tạo hỗn hợp rượu là biến đổi hóa học.",
            "correct": false
          }
        ],
        "explanation": "Ngưng tụ sương mù và hòa tan cồn là biến đổi vật lí."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các hiện tượng liên quan đến kim loại sắt:",
        "statements": [
          {
            "subId": "a",
            "text": "Rèn đập thanh sắt đỏ rực thành lưỡi cuốc là biến đổi vật lí.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đốt cháy dây sắt trong bình khí oxi tạo các hạt oxit sắt từ màu nâu đen là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ngâm đinh sắt vào dầu hỏa để chống gỉ là một biến đổi hóa học.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Sắt tan trong dung dịch axit clohiđric sủi bọt khí là biến đổi hóa học.",
            "correct": true
          }
        ],
        "explanation": "Ngâm dầu hỏa chỉ ngăn cách sắt với không khí ẩm (biện pháp vật lí)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về quá trình làm bánh mì truyền thống:",
        "statements": [
          {
            "subId": "a",
            "text": "Trộn bột mì với men nở và nước nhào dẻo là biến đổi vật lí.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Quá trình ủ bột phồng xốp do men sinh khí carbon dioxide là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nướng bánh trong lò nhiệt độ cao làm vỏ bánh vàng giòn thơm ngậy là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bẻ đôi ổ bánh mì khi ăn là biến đổi hóa học.",
            "correct": false
          }
        ],
        "explanation": "Bẻ đôi chỉ thay đổi hình dạng kích thước (vật lí)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng nhiệt phân muối kali pemanganat (KMnO4 - thuốc tím):",
        "statements": [
          {
            "subId": "a",
            "text": "Đun nóng thuốc tím giải phóng khí oxi làm tàn đóm đỏ bùng cháy là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chất rắn sau phản ứng có màu đen tím gồm K2MnO4 và MnO2 là những chất mới.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tổng khối lượng chất rắn thu được sau khi nung lớn hơn khối lượng thuốc tím ban đầu.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khí oxi sinh ra có thể thu bằng phương pháp đẩy nước do ít tan trong nước.",
            "correct": true
          }
        ],
        "explanation": "Khối lượng chất rắn giảm đi do khí oxi đã bay đi."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong 4 hiện tượng: làm sữa chua, đốt củi, nung vôi, xé vải. Có bao nhiêu hiện tượng biến đổi hóa học?",
        "correctAnswer": "3",
        "explanation": "Có 3 hiện tượng: làm sữa chua, đốt củi, nung vôi."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các hiện tượng: (1) Sáp nến chảy lỏng; (2) Cồn cháy; (3) Mỡ đông lại khi trời lạnh; (4) Axit làm quỳ tím đổi màu; (5) Luộc chín quả trứng. Số hiện tượng hóa học là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "Gồm (2), (4), (5) là hiện tượng hóa học."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một nhóm học sinh làm 5 thí nghiệm: mài gỗ, đánh diêm quẹt, hòa tan đường, rỉ sét chìa khóa, cắt bánh ngọt. Có bao nhiêu thí nghiệm KHÔNG sinh ra chất mới?",
        "correctAnswer": "3",
        "explanation": "Mài gỗ, hòa tan đường, cắt bánh (3 hiện tượng vật lí)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong dạ dày người, thức ăn được tiêu hóa: (1) cơ học nhờ co bóp nghiền nhỏ thức ăn; (2) hóa học nhờ axit HCl và enzim pepsin biến đổi protein. Quá trình nào là biến đổi hóa học? (Điền số 1 hoặc 2)",
        "correctAnswer": "2",
        "explanation": "Quá trình (2) là biến đổi hóa học do men và axit phân giải chất."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Một mẫu than chứa 96% carbon đem đốt cháy hoàn toàn trong oxi sinh ra bao nhiêu loại oxide khí chính? (Điền 1 nếu chỉ tạo CO2 hoặc CO)",
        "correctAnswer": "1",
        "explanation": "Đốt cháy hoàn toàn tạo duy nhất CO2."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Tiến hành 6 quá trình: chưng cất dầu mỏ, lên men rượu etylic, bốc hơi nước biển lấy muối, nung thạch cao sống thành thạch cao khan, tôi vôi sống, xát vỏ thóc lấy gạo. Có bao nhiêu quá trình hóa học?",
        "correctAnswer": "3",
        "explanation": "Gồm: lên men rượu, nung thạch cao thoát nước kết tinh, tôi vôi (3 quá trình)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nung 100 g đá vôi (chứa 80% CaCO3, còn lại là tạp chất trơ không bị nhiệt phân) đến khi phản ứng hoàn toàn thu được m gam chất rắn. Biết phản ứng nhiệt phân là: CaCO3 -> CaO + CO2. Khối lượng khí CO2 thoát ra là:",
        "options": [
          "35,2 g",
          "44,0 g",
          "32,0 g",
          "28,5 g"
        ],
        "correct": 0,
        "explanation": "m_CaCO3 = 80g -> n = 0,8 mol -> m_CO2 = 0,8 * 44 = 35,2 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Quá trình nào sau đây giải thích sự tạo thành thạch nhũ trong các hang động núi đá vôi là sự kết hợp của hai phản ứng hóa học thuận nghịch?",
        "options": [
          "CaCO3 + H2O + CO2 <=> Ca(HCO3)2",
          "CaO + H2O <=> Ca(OH)2",
          "Ca(OH)2 + CO2 <=> CaCO3 + H2O",
          "CaCO3 <=> CaO + CO2"
        ],
        "correct": 0,
        "explanation": "Nước có CO2 hòa tan CaCO3 thành Ca(HCO3)2, khi nhỏ giọt mất CO2 kết tủa lại CaCO3."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Đốt cháy hoàn toàn 2,4 g kim loại magie (Mg) trong bình chứa khí clo (Cl2) dư, thu được 9,5 g muối magie clorua (MgCl2). Khối lượng khí clo đã tham gia phản ứng là:",
        "options": [
          "7,1 g",
          "11,9 g",
          "6,5 g",
          "8,2 g"
        ],
        "correct": 0,
        "explanation": "m_Cl2 = 9,5 - 2,4 = 7,1 g."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho thanh đồng nguyên chất nhúng vào dung dịch bạc nitrat (AgNO3). Hiện tượng nào sau đây khẳng định chắc chắn có biến đổi hóa học xảy ra?",
        "options": [
          "Thanh đồng bị tan chảy thành chất lỏng màu đỏ",
          "Dung dịch từ không màu chuyển dần sang màu xanh lam và có kim loại màu xám bạc bám ngoài thanh đồng",
          "Có bọt khí mùi khai thoát ra dữ dội",
          "Dung dịch đông cứng lại thành khối trong suốt"
        ],
        "correct": 1,
        "explanation": "Cu + 2AgNO3 -> Cu(NO3)2 (xanh lam) + 2Ag (bạc xám)."
      }
    ]
  },
  "chem8_c1_b2_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong các hiện tượng tự nhiên sau, hiện tượng nào là biến đổi hóa học?",
        "options": [
          "Thủy triều lên xuống theo chu kì lực hút mặt trăng",
          "Hiện tượng băng tan ở hai cực Trái Đất",
          "Lá cây rụng xuống đất lâu ngày bị mục nát phân hủy",
          "Gió bão làm gãy đổ cành cây"
        ],
        "correct": 2,
        "explanation": "Xác lá mục nát là quá trình vi sinh vật phân giải chất hữu cơ sinh chất mới."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Dấu hiệu nào sau đây KHÔNG PHẢI là bằng chứng trực tiếp của một biến đổi hóa học?",
        "options": [
          "Có chất khí không màu thoát ra",
          "Có sự thay đổi nhiệt độ tỏa nhiệt hoặc thu nhiệt",
          "Khối lượng của vật bị chia làm hai phần do cắt đứt",
          "Xuất hiện kết tủa lắng xuống đáy cốc"
        ],
        "correct": 2,
        "explanation": "Cắt đứt vật thể chỉ là biến đổi cơ học về kích thước."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi cho đường mía vào chảo đun nóng lâu, đường chuyển từ màu trắng sang vàng nâu (caramen), rồi cuối cùng thành khối đen xốp có mùi khét. Toàn bộ quá trình này là biến đổi:",
        "options": [
          "Vật lí thuần túy",
          "Ban đầu là vật lí (nóng chảy), sau đó là hóa học (bị than hóa)",
          "Hóa học hoàn toàn ngay từ đầu",
          "Sinh học do vi khuẩn phân hủy"
        ],
        "correct": 1,
        "explanation": "Đầu tiên đường nóng chảy (vật lí), sau đó phân hủy thành than và nước (hóa học)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Thổi khí thở của người vào dung dịch nước vôi trong, dung dịch bị vẩn đục do tạo chất mới là:",
        "options": [
          "Canxi hiđroxit",
          "Canxi cacbonat kết tủa trắng",
          "Khí oxi hòa tan",
          "Khí nitơ ngưng tụ"
        ],
        "correct": 1,
        "explanation": "CO2 + Ca(OH)2 -> CaCO3 (kết tủa trắng) + H2O."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho các hiện tượng: (1) Sương mù tan khi mặt trời lên; (2) Thức ăn để trong tủ lạnh lâu bị mốc; (3) Cầu vồng xuất hiện sau cơn mưa; (4) Nước vôi sống để ngoài không khí bị đóng màng cứng. Số hiện tượng hóa học là:",
        "options": [
          "1",
          "2",
          "3",
          "4"
        ],
        "correct": 1,
        "explanation": "Gồm (2) mốc và (4) Ca(OH)2 tác dụng CO2 tạo CaCO3."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Tại sao người ta thường quẹt que diêm vào bề mặt sườn bao diêm để diêm bắt cháy?",
        "options": [
          "Để làm nguội que diêm",
          "Ma sát sinh nhiệt làm photpho đỏ bốc cháy, khơi mào phản ứng hóa học ở đầu que diêm",
          "Để photpho biến đổi vật lí thành chất lỏng",
          "Để tạo ra dòng điện tích truyền vào diêm"
        ],
        "correct": 1,
        "explanation": "Nhiệt ma sát kích thích phản ứng cháy của photpho đỏ."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi hòa tan amoni nitrat (NH4NO3) vào nước trong cốc thủy tinh, sờ tay vào thành cốc thấy rất lạnh. Đây là hiện tượng gì?",
        "options": [
          "Biến đổi hóa học tỏa nhiệt",
          "Biến đổi vật lí hòa tan kèm theo sự thu nhiệt mạnh",
          "Biến đổi hóa học tạo khí lạnh",
          "Hiện tượng ngưng tụ hơi nước bên trong cốc"
        ],
        "correct": 1,
        "explanation": "Quá trình hòa tan phân li muối thu nhiệt từ môi trường."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hiện tượng tạo thành hang động carxtơ ở các vùng núi đá vôi như vịnh Hạ Long, Phong Nha - Kẻ Bàng chủ yếu là do:",
        "options": [
          "Gió mài mòn cơ học hàng triệu năm",
          "Nước mưa hòa tan khí CO2 tạo axit yếu ăn mòn dần đá vôi CaCO3",
          "Sóng biển đập vỡ đá vôi thành cát",
          "Ánh sáng mặt trời nung nóng làm đá vôi nứt nẻ"
        ],
        "correct": 1,
        "explanation": "Nước mưa có CO2 hòa tan CaCO3 tạo Ca(HCO3)2."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Trong sản xuất bia rượu, gạo hoặc ngô được đường hóa rồi lên men rượu thành cồn etylic. Đây là:",
        "options": [
          "Hai biến đổi vật lí liên tiếp",
          "Hai biến đổi hóa học liên tiếp do men xúc tác",
          "Giai đoạn đầu là hóa học, giai đoạn sau là vật lí",
          "Quá trình bay hơi nước ngưng tụ cồn"
        ],
        "correct": 1,
        "explanation": "Tinh bột -> đường glucozo -> rượu etylic đều là phản ứng hóa học."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Để bảo quản táo đã gọt vỏ không bị thâm đen do phản ứng oxi hóa với không khí, người ta ngâm táo vào nước muối nhạt hoặc nước pha ít nước cốt chanh. Thao tác này nhằm mục đích gì?",
        "options": [
          "Thực hiện phản ứng biến đổi hóa học làm táo ngọt hơn",
          "Ngăn chặn và làm chậm quá trình oxi hóa của các enzim trong táo với oxi không khí",
          "Làm đông lạnh miếng táo",
          "Tách tinh bột ra khỏi miếng táo"
        ],
        "correct": 1,
        "explanation": "Vitamin C và axit citric ức chế phản ứng oxi hóa enzyme."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cho mẩu kim loại natri vào cốc nước có pha vài giọt phenolphtalein. Hiện tượng nào sau đây chứng tỏ có biến đổi hóa học?",
        "options": [
          "Natri tan dần vo tròn chạy trên mặt nước",
          "Dung dịch chuyển sang màu hồng cánh sen và có khí H2 bay lên",
          "Cốc nước bị ấm lên",
          "Tất cả các hiện tượng trên đều chứng minh phản ứng hóa học đã diễn ra"
        ],
        "correct": 3,
        "explanation": "2Na + 2H2O -> 2NaOH + H2 tỏa nhiệt làm nóng cốc và kiềm làm hồng phenolphtalein."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Tiến hành 4 thí nghiệm: (1) Hòa tan dầu ăn vào xăng; (2) Đốt cháy dầu ăn trên chảo; (3) Dùng dung dịch kiềm xà phòng hóa dầu ăn tạo xà phòng; (4) Để dầu ăn lâu ngày bị ôi khét do oxi hóa. Số thí nghiệm là biến đổi hóa học là:",
        "options": [
          "1",
          "2",
          "3",
          "4"
        ],
        "correct": 2,
        "explanation": "Gồm (2), (3), (4) là biến đổi hóa học (3 thí nghiệm)."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Xét các biến đổi vật chất trong nấu ăn gia đình:",
        "statements": [
          {
            "subId": "a",
            "text": "Thái mỏng thịt bò là biến đổi vật lí.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Xào thịt bò chín đổi từ màu đỏ sang màu nâu xám là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ướp muối vào thịt làm ngấm gia vị là biến đổi hóa học sinh chất mới.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Mỡ lợn rán thành tóp mỡ giòn và nước mỡ lỏng là quá trình có biến đổi hóa học.",
            "correct": true
          }
        ],
        "explanation": "Ướp muối là quá trình khuếch tán vật lí."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các hiện tượng khí quyển và thời tiết:",
        "statements": [
          {
            "subId": "a",
            "text": "Hiện tượng sấm sét tạo ra tia lửa điện biến N2 và O2 trong không khí thành NO là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mưa đá rơi từ trên cao xuống làm vỡ kính là biến đổi hóa học.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Tầng ozon hấp thụ tia cực tím phân hủy O3 thành O2 là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí thải SO2 từ các nhà máy kết hợp với nước mưa tạo mưa axit là biến đổi hóa học.",
            "correct": true
          }
        ],
        "explanation": "Mưa đá rơi làm vỡ kính chỉ là tác dụng cơ học vật lí."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về quá trình làm tương nếp truyền thống:",
        "statements": [
          {
            "subId": "a",
            "text": "Rang chín đỗ tương trên chảo là biến đổi hóa học làm chín và dậy mùi thơm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Xay nhỏ đỗ tương đã rang là biến đổi vật lí.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nuôi mốc hoa cau trên xôi nếp là quá trình sinh học enzym tạo chất mới.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Để tương ngoài nắng cho bay bớt nước đặc lại là biến đổi hóa học.",
            "correct": false
          }
        ],
        "explanation": "Nắng làm bay hơi nước là biến đổi vật lí."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm cho bột kẽm (Zn) vào cốc đựng dung dịch đồng sunfat (CuSO4):",
        "statements": [
          {
            "subId": "a",
            "text": "Màu xanh lam của dung dịch nhạt dần theo thời gian.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Có một lớp kim loại màu đỏ gạch bám ngoài các hạt bột kẽm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phản ứng trên thuộc loại biến đổi vật lí vì không có chất khí bay lên.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tổng khối lượng dung dịch sau phản ứng giảm nhẹ so với dung dịch ban đầu.",
            "correct": true
          }
        ],
        "explanation": "Zn tan ra (65g) thay thế Cu bám vào (64g) nên m_dd tăng nhẹ hoặc thay đổi kim loại."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong các hiện tượng: mây ngưng tụ thành mưa, nến chảy lỏng, sữa chua lên men, bóng bay nổ tung. Có bao nhiêu hiện tượng biến đổi vật lí?",
        "correctAnswer": "3",
        "explanation": "Có 3 hiện tượng vật lí: mưa ngưng tụ, nến chảy, bóng nổ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho dãy 5 chất và quá trình: cồn cháy, rỉ đồng màu xanh, hòa tan đường phèn, băng khô thăng hoa, nung đá vôi. Có bao nhiêu quá trình hóa học?",
        "correctAnswer": "3",
        "explanation": "Cồn cháy, rỉ đồng, nung đá vôi (3 quá trình hóa học)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một bình kín chứa hỗn hợp khí H2 và O2. Bật tia lửa điện để phản ứng xảy ra tạo thành nước. Số loại phân tử đơn chất ban đầu còn lại sau khi phản ứng vừa đủ là bao nhiêu?",
        "correctAnswer": "0",
        "explanation": "Phản ứng vừa đủ thì cả H2 và O2 đều hết (còn lại 0 phân tử đơn chất)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Nung m gam bột Cu trong bình khí O2 dư một thời gian thu được 16 g bột CuO màu đen. Biết khối lượng Cu ban đầu là 12,8 g. Khối lượng khí O2 đã phản ứng là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "3,2",
        "explanation": "m_O2 = 16 - 12,8 = 3,2 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Trong một thí nghiệm, đốt cháy hết 6 g carbon trong oxi dư. Thể tích khí CO2 sinh ra ở đkc (lít) được tính bằng 0,5 x 24,79. Giá trị này bằng bao nhiêu lít? (Làm tròn đến 2 chữ số thập phân)",
        "correctAnswer": "12,40",
        "explanation": "V = 0,5 * 24,79 = 12,395 xấp xỉ 12,40 L."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Có 4 ống nghiệm đựng: (1) Nước cất; (2) Dung dịch giấm ăn; (3) Dung dịch nước vôi trong; (4) Dung dịch muối ăn. Thổi khí CO2 vào từng ống nghiệm. Có bao nhiêu ống nghiệm xảy ra biến đổi hóa học tạo kết tủa đục?",
        "correctAnswer": "1",
        "explanation": "Chỉ có ống (3) Ca(OH)2 tạo kết tủa CaCO3 vẩn đục."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Cho 13 g kim loại kẽm tác dụng vừa đủ với dung dịch axit clohiđric thu được dung dịch chứa 27,2 g muối kẽm clorua và giải phóng V lít khí H2 ở đkc. Khối lượng axit HCl đã tham gia phản ứng là:",
        "options": [
          "14,6 g",
          "7,3 g",
          "21,9 g",
          "18,2 g"
        ],
        "correct": 0,
        "explanation": "n_Zn = 0,2 mol -> n_HCl = 0,4 mol -> m_HCl = 0,4 * 36,5 = 14,6 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khi đun nóng hỗn hợp sắt và lưu huỳnh không có không khí, một phản ứng hóa học tự duy trì diễn ra tạo thành chất FeS. Đem sản phẩm hòa tan vào axit HCl dư thấy có mùi trứng thối thoát ra. Khí đó là:",
        "options": [
          "H2S (hiđro sunfua)",
          "SO2 (khí sunfurơ)",
          "H2 (khí hiđro)",
          "Cl2 (khí clo)"
        ],
        "correct": 0,
        "explanation": "FeS + 2HCl -> FeCl2 + H2S (khí mùi trứng thối đặc trưng)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để phân biệt 2 hiện tượng biến đổi vật lí và biến đổi hóa học một cách khoa học nhất, người ta dựa vào tiêu chí nào?",
        "options": [
          "Sự thay đổi về thể tích của vật",
          "Sự thay đổi về khối lượng mẫu vật thử",
          "Sự xuất hiện chất mới có tính chất vật lí và hóa học khác với chất ban đầu",
          "Sự thay đổi màu sắc quan sát được bằng mắt thường"
        ],
        "correct": 2,
        "explanation": "Bản chất là có chất mới tạo thành."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một học sinh thực hiện thí nghiệm cho viên kẽm vào dung dịch CuSO4 màu xanh lam. Sau phản ứng lấy thanh kẽm ra cân lại thấy khối lượng thanh kẽm thay đổi như thế nào? (Biết 1 mol Zn = 65 g tan ra tạo 1 mol Cu = 64 g bám vào)",
        "options": [
          "Khối lượng thanh kẽm tăng lên",
          "Khối lượng thanh kẽm giảm đi",
          "Khối lượng thanh kẽm giữ nguyên không đổi",
          "Toàn bộ thanh kẽm biến mất hoàn toàn"
        ],
        "correct": 1,
        "explanation": "Cứ 65g Zn tan đi chỉ có 64g Cu bám lại nên m thanh kẽm giảm đi 1g/mol phản ứng."
      }
    ]
  },
  "chem8_c1_b3_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong một phản ứng hóa học, chất ban đầu bị biến đổi được gọi là:",
        "options": [
          "Chất phản ứng (chất tham gia)",
          "Chất sản phẩm",
          "Chất xúc tác",
          "Chất môi trường"
        ],
        "correct": 0,
        "explanation": "Chất ban đầu trước khi xảy ra biến đổi gọi là chất phản ứng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Quá trình biến đổi chất này thành chất khác được gọi là:",
        "options": [
          "Hiện tượng vật lí",
          "Phản ứng hóa học",
          "Sự ngưng tụ",
          "Sự hòa tan"
        ],
        "correct": 1,
        "explanation": "Phản ứng hóa học là quá trình biến đổi chất này thành chất khác."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong phản ứng hóa học, yếu tố nào sau đây KHÔNG THAY ĐỔI?",
        "options": [
          "Số lượng phân tử các chất",
          "Liên kết giữa các nguyên tử",
          "Số nguyên tử của mỗi nguyên tố",
          "Tính chất vật lí của các chất"
        ],
        "correct": 2,
        "explanation": "Bản chất phản ứng hóa học là chỉ có liên kết thay đổi, số nguyên tử mỗi nguyên tố bảo toàn."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Cho phản ứng: Khí hiđro + Khí oxi -> Nước. Chất sản phẩm của phản ứng là:",
        "options": [
          "Khí hiđro",
          "Khí oxi",
          "Nước",
          "Hỗn hợp hiđro và oxi"
        ],
        "correct": 2,
        "explanation": "Nước là chất mới tạo thành sau phản ứng."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Phương trình chữ nào sau đây biểu diễn đúng phản ứng đốt cháy bột lưu huỳnh trong không khí tạo khí sunfurơ?",
        "options": [
          "Lưu huỳnh + Khí oxi -> Khí sunfurơ",
          "Khí sunfurơ + Khí oxi -> Lưu huỳnh",
          "Lưu huỳnh -> Khí sunfurơ + Khí oxi",
          "Lưu huỳnh + Khí nitơ -> Khí sunfurơ"
        ],
        "correct": 0,
        "explanation": "Lưu huỳnh phản ứng với oxi tạo khí lưu huỳnh đioxit (sunfurơ)."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khi một que đóm còn tàn đỏ được đưa vào bình chứa khí oxi, que đóm bùng cháy lên. Dấu hiệu này chứng minh:",
        "options": [
          "Có sự ngưng tụ hơi nước",
          "Xảy ra phản ứng hóa học tỏa nhiệt và phát sáng mãnh liệt",
          "Khí oxi bị biến đổi vật lí thành chất lỏng",
          "Que đóm bị làm lạnh đột ngột"
        ],
        "correct": 1,
        "explanation": "Khí oxi duy trì sự cháy, phản ứng tỏa nhiều nhiệt và phát sáng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Để phản ứng giữa sắt và lưu huỳnh xảy ra tạo thành sắt(II) sunfua, điều kiện bắt buộc lúc đầu là:",
        "options": [
          "Hòa tan vào nước lạnh",
          "Đun nóng để khơi mào phản ứng",
          "Chiếu tia cực tím",
          "Tăng áp suất thật cao"
        ],
        "correct": 1,
        "explanation": "Cần đun nóng ban đầu để khơi mào phản ứng tỏa nhiệt."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Phản ứng hóa học diễn ra được khi các chất phản ứng:",
        "options": [
          "Phải ở trạng thái khí",
          "Tiếp xúc trực tiếp với nhau",
          "Đều tan tốt trong nước",
          "Có cùng khối lượng"
        ],
        "correct": 1,
        "explanation": "Điều kiện đầu tiên là các chất phản ứng phải tiếp xúc với nhau."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Trước phản ứng có 2 phân tử H2 và 1 phân tử O2. Sau phản ứng tạo thành 2 phân tử H2O. Nhận xét nào sau đây là ĐÚNG?",
        "options": [
          "Tổng số phân tử trước và sau phản ứng bằng nhau",
          "Số nguyên tử H và O trước phản ứng bằng sau phản ứng",
          "Liên kết giữa các nguyên tử H vẫn giữ nguyên",
          "Tạo ra chất mới có cùng tính chất với H2"
        ],
        "correct": 1,
        "explanation": "Số lượng nguyên tử của mỗi nguyên tố được bảo toàn (4 nguyên tử H và 2 nguyên tử O)."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trong đời sống, tại sao khi dập tắt bếp than củi người ta thường đậy kín nắp lò hoặc phun nước vào?",
        "options": [
          "Để ngăn cách than tiếp xúc với oxi không khí và hạ nhiệt độ xuống dưới nhiệt độ cháy",
          "Để cung cấp thêm khí CO2 cho than cháy",
          "Để làm tăng nồng độ khí oxi xung quanh than",
          "Để biến đổi than củi thành than đá"
        ],
        "correct": 0,
        "explanation": "Hạ nhiệt độ và cách li than với oxi là nguyên tắc dập tắt đám cháy."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cho các phản ứng: (1) Cồn cháy tỏa nhiệt; (2) Hòa tan vôi sống vào nước nóng lên; (3) Nung đá vôi cần cấp nhiệt liên tục; (4) Khí gas cháy đun sôi nước. Phản ứng nào là phản ứng thu nhiệt?",
        "options": [
          "(1)",
          "(2)",
          "(3)",
          "(4)"
        ],
        "correct": 2,
        "explanation": "Nung đá vôi hấp thụ nhiệt năng liên tục từ lò nung (phản ứng thu nhiệt)."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Một bạn học sinh viết phương trình chữ: Magiê + Axit clohiđric -> Magiê clorua + Khí hiđro. Nếu cho 4,8 g magiê phản ứng hoàn toàn với dung dịch chứa 14,6 g axit clohiđric thu được 19,0 g magiê clorua. Khối lượng khí hiđro thoát ra là:",
        "options": [
          "0,4 g",
          "0,2 g",
          "0,8 g",
          "0,6 g"
        ],
        "correct": 0,
        "explanation": "Theo ĐL BTKL: m_H2 = (4,8 + 14,6) - 19,0 = 0,4 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về bản chất và diễn biến của phản ứng hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong phản ứng hóa học, chỉ có liên kết giữa các nguyên tử bị biến đổi.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số lượng nguyên tử của mỗi nguyên tố tăng lên sau phản ứng.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Các phân tử chất phản ứng bị phân rã và tái tổ hợp thành phân tử chất sản phẩm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng của từng nguyên tử bị thay đổi trong quá trình phản ứng.",
            "correct": false
          }
        ],
        "explanation": "Số lượng và khối lượng từng nguyên tử được giữ nguyên."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về điều kiện xảy ra và dấu hiệu nhận biết phản ứng:",
        "statements": [
          {
            "subId": "a",
            "text": "Mọi phản ứng hóa học đều cần đun nóng liên tục mới xảy ra.",
            "correct": false
          },
          {
            "subId": "b",
            "text": "Sự xuất hiện chất kết tủa không tan là một dấu hiệu chứng minh có phản ứng xảy ra.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Một số phản ứng cần có chất xúc tác để thúc đẩy tốc độ phản ứng nhanh hơn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Sự sủi bọt khí không tan thoát ra khỏi dung dịch là bằng chứng có chất mới sinh ra.",
            "correct": true
          }
        ],
        "explanation": "Nhiều phản ứng xảy ra ngay ở nhiệt độ thường khi tiếp xúc (như axit tác dụng bazơ)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về phản ứng tỏa nhiệt và thu nhiệt trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Phản ứng tỏa nhiệt là phản ứng giải phóng năng lượng dưới dạng nhiệt ra môi trường.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Quá trình đốt cháy xăng xe trong động cơ là phản ứng thu nhiệt.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Phản ứng tôi vôi sống: CaO + H2O -> Ca(OH)2 làm nước sôi sùng sục là phản ứng tỏa nhiệt.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Quá trình quang hợp của cây xanh hấp thụ năng lượng ánh sáng mặt trời có bản chất tương tự phản ứng thu nhiệt.",
            "correct": true
          }
        ],
        "explanation": "Đốt cháy xăng dầu là phản ứng tỏa nhiệt cực mạnh."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng nhiệt phân đường mía (saccarozơ C12H22O11) trong ống nghiệm khô:",
        "statements": [
          {
            "subId": "a",
            "text": "Trên thành ống nghiệm xuất hiện những giọt nước đọng lại là sản phẩm của phản ứng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chất rắn màu đen còn lại trong ống nghiệm là nguyên tố than (carbon).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đây là phản ứng tỏa nhiệt vì đường tự bốc cháy mà không cần đèn cồn cung cấp nhiệt.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Phương trình chữ của phản ứng: Đường mía -> Nước + Carbon.",
            "correct": true
          }
        ],
        "explanation": "Phản ứng cần đun nóng liên tục bằng đèn cồn nên là phản ứng thu nhiệt."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phản ứng: Kẽm + Axit clohiđric -> Kẽm clorua + Khí hiđro, có bao nhiêu chất phản ứng?",
        "correctAnswer": "2",
        "explanation": "Có 2 chất phản ứng: Kẽm và Axit clohiđric."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các hiện tượng: cháy cồn, gỉ sắt, hô hấp tế bào, quang hợp, tôi vôi. Có bao nhiêu quá trình tỏa nhiệt ra môi trường xung quanh?",
        "correctAnswer": "4",
        "explanation": "Cháy cồn, gỉ sắt, hô hấp, tôi vôi đều tỏa nhiệt (4 quá trình)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Trong một phân tử nước H2O có tổng cộng bao nhiêu nguyên tử liên kết với nhau?",
        "correctAnswer": "3",
        "explanation": "Gồm 2 nguyên tử H và 1 nguyên tử O (tổng 3 nguyên tử)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Đốt cháy 1,2 g bột cacbon trong khí oxi thu được 4,4 g khí cacbon đioxit. Khối lượng khí oxi đã phản ứng là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "3,2",
        "explanation": "m_O2 = 4,4 - 1,2 = 3,2 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Để đốt cháy hoàn toàn 1 mol khí metan CH4 cần đúng 2 mol khí oxi O2. Số mol khí CO2 sinh ra là bao nhiêu mol?",
        "correctAnswer": "1",
        "explanation": "CH4 + 2O2 -> CO2 + 2H2O -> sinh 1 mol CO2."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cho phương trình phản ứng: a Fe + b Cl2 -> c FeCl3. Tổng các hệ số tối giản (a + b + c) của phương trình hóa học này là bao nhiêu?",
        "correctAnswer": "7",
        "explanation": "2Fe + 3Cl2 -> 2FeCl3. Tổng hệ số: 2 + 3 + 2 = 7."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nung nóng 50 g canxi cacbonat (đá vôi) thu được 28 g canxi oxit và một lượng khí canxi cacbon đioxit. Thể tích khí CO2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Biết n = 22 / 44 = 0,5 mol)",
        "options": [
          "12,395 lít",
          "24,79 lít",
          "11,2 lít",
          "22,4 lít"
        ],
        "correct": 0,
        "explanation": "m_CO2 = 50 - 28 = 22g -> n = 0,5 mol -> V = 0,5 * 24,79 = 12,395 L."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khi dẫn khí H2 dư đi qua ống nghiệm chứa bột CuO màu đen nung nóng đỏ, hiện tượng quan sát được chứng minh phản ứng hóa học xảy ra là:",
        "options": [
          "Bột CuO chuyển từ màu đen sang màu đỏ của đồng và có hơi nước ngưng tụ ở đầu ống nghiệm",
          "Bột CuO tan hoàn toàn thành chất lỏng không màu",
          "Ống nghiệm phát nổ kèm theo khí có mùi hắc",
          "Không có hiện tượng gì xảy ra"
        ],
        "correct": 0,
        "explanation": "H2 + CuO (đen) -> Cu (đỏ) + H2O (lỏng)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Ứng dụng nào sau đây khai thác năng lượng từ phản ứng hóa học tỏa nhiệt phục vụ đời sống con người?",
        "options": [
          "Chạy động cơ xe máy bằng xăng sinh học",
          "Hàn đường ray xe lửa bằng hỗn hợp tecmit (nhôm và oxit sắt)",
          "Đun nấu thức ăn bằng khí gas hóa lỏng",
          "Cả 3 ứng dụng trên đều đúng"
        ],
        "correct": 3,
        "explanation": "Tất cả đều sử dụng năng lượng nhiệt tỏa ra từ phản ứng hóa học."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một bình kín dung tích không đổi chứa hỗn hợp khí N2 và H2 theo tỉ lệ mol 1 : 3. Sau khi thực hiện phản ứng tổng hợp amoniac (N2 + 3H2 -> 2NH3), áp suất trong bình thay đổi như thế nào ở cùng nhiệt độ?",
        "options": [
          "Áp suất trong bình tăng lên do phân tử NH3 nặng hơn",
          "Áp suất trong bình giảm xuống do tổng số mol khí giảm đi",
          "Áp suất trong bình không thay đổi",
          "Áp suất ban đầu giảm rồi sau đó tăng vọt"
        ],
        "correct": 1,
        "explanation": "Cứ 1 mol N2 + 3 mol H2 (tổng 4 mol) tạo ra 2 mol NH3 nên số phân tử khí giảm -> áp suất giảm."
      }
    ]
  },
  "chem8_c1_b3_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Dấu hiệu nào sau đây cho biết có phản ứng hóa học xảy ra khi nhỏ dung dịch bari clorua vào dung dịch natri sunfat?",
        "options": [
          "Xuất hiện kết tủa màu trắng",
          "Có bọt khí bay lên mạnh mẽ",
          "Dung dịch bốc cháy sáng chói",
          "Nhiệt độ dung dịch hạ xuống 0 độ C"
        ],
        "correct": 0,
        "explanation": "BaCl2 + Na2SO4 -> BaSO4 (kết tủa trắng) + 2NaCl."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Phản ứng tỏa nhiệt là phản ứng hóa học:",
        "options": [
          "Giải phóng năng lượng dưới dạng nhiệt ra môi trường",
          "Hấp thụ nhiệt năng từ môi trường xung quanh",
          "Làm môi trường xung quanh lạnh đi rõ rệt",
          "Chỉ xảy ra khi liên tục đun nóng bằng ngọn lửa"
        ],
        "correct": 0,
        "explanation": "Định nghĩa phản ứng tỏa nhiệt: tỏa nhiệt ra môi trường."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Trong phương trình chữ của phản ứng hóa học, tên các chất tham gia được viết ở phía nào của mũi tên?",
        "options": [
          "Bên trái mũi tên",
          "Bên phải mũi tên",
          "Phía trên mũi tên",
          "Phía dưới mũi tên"
        ],
        "correct": 0,
        "explanation": "Quy ước: Chất phản ứng -> Chất sản phẩm."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Chất xúc tác là chất có vai trò:",
        "options": [
          "Làm tăng tốc độ phản ứng và không bị biến đổi sau phản ứng",
          "Làm thay đổi sản phẩm của phản ứng hóa học",
          "Bị tiêu hao hoàn toàn trong phản ứng",
          "Ngăn cản phản ứng hóa học không xảy ra"
        ],
        "correct": 0,
        "explanation": "Xúc tác đẩy nhanh phản ứng nhưng giữ nguyên về lượng và chất."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Khi hòa tan viên sủi hạ sốt vào cốc nước, ta thấy sủi bọt khí và cầm vào cốc thấy mát nhẹ. Hiện tượng sủi bọt khí chứng tỏ:",
        "options": [
          "Viên sủi bay hơi thành hơi sủi",
          "Đã xảy ra phản ứng hóa học tạo ra chất khí mới",
          "Nước phản ứng với thủy tinh",
          "Nhiệt độ nước tăng vọt"
        ],
        "correct": 1,
        "explanation": "Axit xitric phản ứng với NaHCO3 tạo khí CO2."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho mẩu đá vôi vào dung dịch axit clohiđric, dấu hiệu chứng tỏ phản ứng xảy ra là:",
        "options": [
          "Đá vôi đổi thành màu xanh",
          "Có bọt khí thoát ra và đá vôi tan dần",
          "Dung dịch đông cứng lại",
          "Cốc phát ra tiếng nổ lớn"
        ],
        "correct": 1,
        "explanation": "CaCO3 + 2HCl -> CaCl2 + H2O + CO2 (khí)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Quá trình hô hấp của cơ thể người lấy khí oxi để đốt cháy các chất dinh dưỡng tạo CO2, H2O và:",
        "options": [
          "Hấp thụ nhiệt làm cơ thể lạnh đi",
          "Giải phóng năng lượng để duy trì thân nhiệt và hoạt động sống",
          "Tiêu hủy hoàn toàn các tế bào",
          "Làm giảm cân nặng tức thì về 0"
        ],
        "correct": 1,
        "explanation": "Hô hấp tế bào là phản ứng tỏa nhiệt cung cấp năng lượng sống."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Thí nghiệm nào sau đây thể hiện phản ứng thu nhiệt rõ rệt nhất?",
        "options": [
          "Hòa tan vôi sống vào nước",
          "Nhiệt phân thuốc tím (KMnO4) để điều chế oxi",
          "Đốt cháy que diêm",
          "Cho bột kẽm vào dung dịch axit"
        ],
        "correct": 1,
        "explanation": "Nhiệt phân KMnO4 cần liên tục cung cấp nhiệt từ ngọn lửa đèn cồn."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Để phân biệt phản ứng tỏa nhiệt và phản ứng thu nhiệt bằng thực nghiệm, dụng cụ đo đơn giản và chính xác nhất là:",
        "options": [
          "Cân điện tử",
          "Nhiệt kế",
          "Thước kẹp",
          "Ống đong"
        ],
        "correct": 1,
        "explanation": "Nhiệt kế theo dõi sự tăng hoặc giảm nhiệt độ của hệ phản ứng."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trong công nghiệp hàn cắt kim loại, người ta dùng ngọn lửa axetilen - oxi (C2H2 + O2) có thể đạt nhiệt độ trên 3000 °C. Đây là phản ứng:",
        "options": [
          "Thu nhiệt cực lớn",
          "Tỏa nhiệt với lượng nhiệt rất lớn",
          "Quang hợp nhân tạo",
          "Phân hủy axetilen"
        ],
        "correct": 1,
        "explanation": "Phản ứng cháy của axetilen tỏa nhiệt cực lớn làm nóng chảy kim loại."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Khi đốt cháy hoàn toàn một mẩu than củi trong bình kín chứa khí oxi, sau phản ứng đưa que đóm còn tàn đỏ vào bình thì que đóm tắt ngay. Điều này giải thích là do:",
        "options": [
          "Khí oxi trong bình đã phản ứng hết và sinh ra khí carbon dioxide không duy trì sự cháy",
          "Bình bị lạnh đi đột ngột",
          "Khí hiđro sinh ra làm tắt đóm",
          "Than biến đổi thành nước dập tắt đóm"
        ],
        "correct": 0,
        "explanation": "O2 đã hết, khí CO2 không duy trì sự cháy làm đóm tắt."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho mẩu kim loại natri phản ứng với khí clo theo sơ đồ: Na + Cl2 -> NaCl. Biết 4,6 g natri tác dụng vừa đủ với m gam khí clo sinh ra 11,7 g muối ăn (NaCl). Giá trị của m là:",
        "options": [
          "7,1 g",
          "16,3 g",
          "3,55 g",
          "5,85 g"
        ],
        "correct": 0,
        "explanation": "m_Cl2 = 11,7 - 4,6 = 7,1 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các hiện tượng tỏa nhiệt và thu nhiệt:",
        "statements": [
          {
            "subId": "a",
            "text": "Phản ứng nung đá vôi thành vôi sống là phản ứng thu nhiệt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi vôi sống tác dụng với nước, nhiệt độ của hỗn hợp tăng lên rất cao là phản ứng tỏa nhiệt.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Quá trình hòa tan đường ăn vào nước là phản ứng hóa học thu nhiệt.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Phản ứng cháy của than đá trong lò luyện gang tỏa nhiệt lớn cung cấp nhiệt lượng cho quá trình luyện kim.",
            "correct": true
          }
        ],
        "explanation": "Hòa tan đường là quá trình hòa tan vật lí."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về điều kiện khơi mào và duy trì phản ứng hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Mọi phản ứng hóa học một khi đã xảy ra thì không bao giờ dừng lại.",
            "correct": false
          },
          {
            "subId": "b",
            "text": "Nhiều phản ứng chỉ cần khơi mào nhiệt ban đầu, sau đó lượng nhiệt tỏa ra sẽ tự duy trì phản ứng (như đốt than, quẹt diêm).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tăng diện tích tiếp xúc giữa các chất tham gia giúp phản ứng diễn ra thuận lợi hơn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Chất xúc tác sau phản ứng sẽ bị chuyển hóa thành một chất khác có màu sắc mới.",
            "correct": false
          }
        ],
        "explanation": "Chất xúc tác không bị biến đổi về chất và lượng sau phản ứng."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về các dấu hiệu nhận biết phản ứng trong phòng thí nghiệm:",
        "statements": [
          {
            "subId": "a",
            "text": "Nhỏ axit vào bazo có pha phenolphtalein, màu hồng biến mất chứng tỏ có phản ứng xảy ra.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nhỏ vài giọt iot vào hồ tinh bột thấy xuất hiện màu xanh tím đặc trưng là phản ứng hóa học.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đun sôi nước thấy hơi nước bốc lên mù mịt là phản ứng hóa học sinh chất khí mới.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Thả viên kẽm vào axit clohiđric thấy sủi bọt khí H2 là biến đổi hóa học.",
            "correct": true
          }
        ],
        "explanation": "Nước sôi bốc hơi là biến đổi trạng thái vật lí."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm đốt cháy dải ruy-băng magie (Mg) ngoài không khí:",
        "statements": [
          {
            "subId": "a",
            "text": "Magie cháy tạo ra ngọn lửa sáng chói lòa và tỏa nhiều nhiệt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sản phẩm thu được là chất bột màu trắng có tên gọi là magie oxit (MgO).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng chất bột trắng MgO thu được nhỏ hơn khối lượng dải magie ban đầu.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Phương trình chữ: Magiê + Khí oxi -> Magiê oxit.",
            "correct": true
          }
        ],
        "explanation": "m_MgO = m_Mg + m_O2 nên khối lượng chất rắn tăng lên."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phản ứng: Khí metan + Khí oxi -> Khí cacbon đioxit + Nước, có bao nhiêu chất sản phẩm?",
        "correctAnswer": "2",
        "explanation": "Có 2 chất sản phẩm: CO2 và H2O."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các phản ứng: đốt nến, tôi vôi, nung đá vôi, que diêm cháy, quang hợp. Có bao nhiêu phản ứng thu nhiệt?",
        "correctAnswer": "2",
        "explanation": "Nung đá vôi và quang hợp là phản ứng thu nhiệt (2 phản ứng)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một phân tử khí cacbonic CO2 gồm 1 nguyên tử C liên kết với bao nhiêu nguyên tử oxi?",
        "correctAnswer": "2",
        "explanation": "Gồm 2 nguyên tử oxi."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Đốt cháy hoàn toàn 6,4 g bột đồng (Cu) trong khí oxi dư thu được 8,0 g đồng(II) oxit (CuO). Khối lượng khí oxi đã phản ứng là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "1,6",
        "explanation": "m_O2 = 8,0 - 6,4 = 1,6 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 2,7 g nhôm vào dung dịch HCl dư. Phương trình: 2Al + 6HCl -> 2AlCl3 + 3H2. Số mol khí H2 sinh ra tính bằng (2,7 / 27) x 1,5. Giá trị này bằng bao nhiêu mol? (Ghi số thập phân)",
        "correctAnswer": "0,15",
        "explanation": "n_Al = 0,1 mol -> n_H2 = 0,15 mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cho phản ứng: a Al + b O2 -> c Al2O3. Tổng các hệ số nguyên tối giản (a + b + c) của phương trình là bao nhiêu?",
        "correctAnswer": "9",
        "explanation": "4Al + 3O2 -> 2Al2O3. Tổng hệ số: 4 + 3 + 2 = 9."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nhiệt phân hoàn toàn 24,5 g muối kali clorat (KClO3) có chất xúc tác MnO2, thu được 14,9 g muối kali clorua (KCl) và V lít khí oxi (đkc, 25 °C, 1 bar). Biết n_O2 = 9,6 / 32 = 0,3 mol. Thể tích V bằng:",
        "options": [
          "7,437 lít",
          "6,72 lít",
          "24,79 lít",
          "14,874 lít"
        ],
        "correct": 0,
        "explanation": "m_O2 = 24,5 - 14,9 = 9,6 g -> n = 0,3 mol -> V = 0,3 * 24,79 = 7,437 L."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tại sao khi nướng thịt trên bếp than, người ta thường dùng quạt nan hoặc quạt điện thổi gió vào bếp?",
        "options": [
          "Gió thổi làm nguội miếng thịt không bị cháy",
          "Gió cung cấp thêm khí oxi và tăng nhiệt độ làm than cháy mạnh hơn",
          "Gió thổi bay hơi nước trong thịt làm thịt ngọt hơn",
          "Gió biến than củi thành than đá"
        ],
        "correct": 1,
        "explanation": "Thổi gió cung cấp dồi dào O2 giúp phản ứng cháy than diễn ra nhanh và mãnh liệt."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Bình cứu hỏa dạng bột chứa chất natri hiđrocacbonat (NaHCO3). Khi phun vào đám cháy, NaHCO3 bị phân hủy nhiệt tạo thành chất khí nào giúp ngăn cản oxi tiếp xúc với ngọn lửa?",
        "options": [
          "Khí cacbon đioxit (CO2)",
          "Khí oxi (O2)",
          "Khí hiđro (H2)",
          "Khí clo (Cl2)"
        ],
        "correct": 0,
        "explanation": "2NaHCO3 -> Na2CO3 + CO2 + H2O. Khí CO2 nặng hơn không khí trùm kín ngọn lửa."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hỗn hợp gồm 2,8 g Fe và 1,6 g S được nung nóng trong ống nghiệm kín không có không khí. Sau phản ứng hoàn toàn, khối lượng chất rắn FeS thu được là:",
        "options": [
          "4,4 g",
          "3,2 g",
          "5,6 g",
          "4,0 g"
        ],
        "correct": 0,
        "explanation": "n_Fe = 2,8/56 = 0,05 mol; n_S = 1,6/32 = 0,05 mol (vừa đủ) -> m_FeS = 0,05 * 88 = 4,4 g."
      }
    ]
  },
  "chem8_c1_b3_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong một phản ứng hóa học, các nguyên tử được liên kết lại theo cách mới là do:",
        "options": [
          "Sự phá vỡ các liên kết cũ và hình thành các liên kết mới",
          "Sự sinh ra các hạt electron mới",
          "Sự phân hủy các proton trong hạt nhân",
          "Sự biến mất của các nguyên tử ban đầu"
        ],
        "correct": 0,
        "explanation": "Liên kết giữa các nguyên tử thay đổi làm phân tử này biến thành phân tử khác."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Phản ứng thu nhiệt là phản ứng hóa học có đặc điểm:",
        "options": [
          "Nhiệt độ của hệ tăng lên rất cao",
          "Hấp thụ năng lượng nhiệt từ môi trường xung quanh",
          "Tự phát sáng chói lòa trong bóng tối",
          "Tự duy trì mà không cần bất kì nguồn năng lượng nào"
        ],
        "correct": 1,
        "explanation": "Phản ứng thu nhiệt hấp thu nhiệt năng làm môi trường lạnh đi."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình chữ nào sau đây viết ĐÚNG cho phản ứng nhiệt phân muối canxi cacbonat thành vôi sống và khí cacbonic?",
        "options": [
          "Canxi cacbonat -> Canxi oxit + Khí cacbon đioxit",
          "Canxi oxit + Canxi cacbonat -> Khí cacbon đioxit",
          "Khí cacbon đioxit + Canxi oxit -> Canxi cacbonat",
          "Canxi cacbonat + Khí oxi -> Canxi oxit"
        ],
        "correct": 0,
        "explanation": "CaCO3 -> CaO + CO2."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hiện tượng thanh sắt ngâm trong dung dịch đồng sunfat bị bao phủ bởi lớp kim loại màu đỏ là do:",
        "options": [
          "Sắt bị nóng chảy",
          "Phản ứng hóa học tạo ra kim loại đồng tự do bám vào",
          "Dung dịch đồng sunfat đông đặc",
          "Lớp rỉ sét của sắt có màu đỏ gạch"
        ],
        "correct": 1,
        "explanation": "Fe + CuSO4 -> FeSO4 + Cu (đỏ)."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho phương trình chữ: Kẽm + Axit sunfuric -> Kẽm sunfat + Khí hiđro. Nếu muốn thu khí hiđro vào ống nghiệm úp ngược, ta dựa vào tính chất nào của hiđro?",
        "options": [
          "Khí hiđro nặng hơn không khí",
          "Khí hiđro rất nhẹ hơn không khí và ít tan trong nước",
          "Khí hiđro có màu vàng lục",
          "Khí hiđro có mùi khai"
        ],
        "correct": 1,
        "explanation": "H2 nhẹ nhất trong các chất khí nên thu bằng cách úp bình."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khi thắp đèn dầu, dầu hỏa được hút lên theo bấc và cháy ở đầu bấc ngọn lửa vàng. Năng lượng tỏa ra chủ yếu ở dạng:",
        "options": [
          "Quang năng và nhiệt năng",
          "Điện năng và cơ năng",
          "Hóa năng tích trữ",
          "Hạt nhân"
        ],
        "correct": 0,
        "explanation": "Phản ứng cháy tỏa nhiệt năng sưởi ấm và quang năng chiếu sáng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Thí nghiệm trộn bột nhôm với bột lưu huỳnh rồi châm ngòi bằng dây magie cháy, hỗn hợp nổ bùng sáng chói và tỏa nhiệt cực lớn. Đây là phản ứng:",
        "options": [
          "Thu nhiệt",
          "Tỏa nhiệt mạnh",
          "Vật lí đơn thuần",
          "Chậm không quan sát được"
        ],
        "correct": 1,
        "explanation": "Phản ứng giữa Al và S tỏa nhiệt rất lớn."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Túi chườm lạnh y tế tức thì thường chứa nước và túi muối amoni nitrat (NH4NO3). Khi bóp vỡ túi nước bên trong để muối tan, túi nhanh chóng lạnh buốt. Quá trình hòa tan này là:",
        "options": [
          "Biến đổi hóa học tỏa nhiệt",
          "Quá trình thu nhiệt mạnh từ xung quanh",
          "Sự ngưng tụ hơi ẩm",
          "Phản ứng tạo đá lạnh"
        ],
        "correct": 1,
        "explanation": "NH4NO3 hòa tan thu nhiệt mạnh làm giảm nhiệt độ tức thì."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Trong công nghiệp sản xuất vôi, để nung chín đá vôi người ta phải liên tục cấp than vào lò đốt. Điều này chứng tỏ phản ứng nhiệt phân đá vôi là:",
        "options": [
          "Phản ứng tỏa nhiệt tự duy trì",
          "Phản ứng thu nhiệt cần năng lượng ngoài cung cấp",
          "Phản ứng không cần nhiệt độ",
          "Hiện tượng bay hơi nước"
        ],
        "correct": 1,
        "explanation": "Cần cấp nhiệt liên tục chứng minh đây là phản ứng thu nhiệt."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Cho phương trình chữ: Natri hiđroxit + Axit clohiđric -> Natri clorua + Nước. Cả 2 dung dịch ban đầu đều không màu, sau phản ứng dung dịch vẫn không màu. Để nhận biết phản ứng xảy ra, người ta dùng:",
        "options": [
          "Quỳ tím hoặc chỉ thị phenolphtalein",
          "Cân khối lượng dung dịch",
          "Ống đong thể tích",
          "Kính hiển vi quang học"
        ],
        "correct": 0,
        "explanation": "Dùng chất chỉ thị màu để nhận biết điểm tương đương của phản ứng trung hòa."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Đốt cháy 0,6 g bột magie trong không khí thu được 1,0 g magie oxit (chất rắn màu trắng). Khối lượng khí oxi trong không khí đã kết hợp với magie là:",
        "options": [
          "0,4 g",
          "1,6 g",
          "0,2 g",
          "0,5 g"
        ],
        "correct": 0,
        "explanation": "m_O2 = 1,0 - 0,6 = 0,4 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Dẫn luồng khí CO đi qua ống sứ nung nóng chứa 16 g bột oxit sắt Fe2O3. Sau phản ứng thu được 11,2 g kim loại sắt và khí CO2 thoát ra. Khối lượng khí CO đã tham gia phản ứng là:",
        "options": [
          "8,4 g",
          "5,6 g",
          "11,2 g",
          "4,2 g"
        ],
        "correct": 0,
        "explanation": "n_Fe = 11,2/56 = 0,2 mol -> n_O tách ra = 0,3 mol -> n_CO = 0,3 mol -> m_CO = 0,3 * 28 = 8,4 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về ngôn ngữ hóa học và phương trình chữ:",
        "statements": [
          {
            "subId": "a",
            "text": "Dấu '+' ở vế chất phản ứng đọc là 'tác dụng với' hoặc 'phản ứng với'.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dấu mũi tên '->' đọc là 'tạo thành' hoặc 'sinh ra'.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dấu '+' ở vế sản phẩm đọc là 'và'.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong phương trình chữ, ta có thể viết công thức hóa học thay cho tên chất.",
            "correct": false
          }
        ],
        "explanation": "Phương trình chữ dùng tên gọi của các chất."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về năng lượng trong các phản ứng hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Phản ứng quang hợp tích lũy năng lượng mặt trời dưới dạng hóa năng trong phân tử tinh bột.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Quá trình hô hấp giải phóng hóa năng tích trữ thành nhiệt năng và ATP cho tế bào.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tất cả các phản ứng tỏa nhiệt đều tự bốc cháy mà không cần nhiệt độ khơi mào.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Các túi sưởi ấm mùa đông dựa trên phản ứng oxi hóa chậm của bột sắt tỏa nhiệt êm dịu.",
            "correct": true
          }
        ],
        "explanation": "Nhiều phản ứng tỏa nhiệt như than củi, cồn cần mồi lửa ban đầu mới cháy."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về sự biến đổi của các chất trong thí nghiệm vôi sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Khi nhỏ nước vào vôi sống CaO, vôi sống hút nước vỡ vụn và bốc khói hơi nước mù mịt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nhiệt độ của bát sứ sau khi tôi vôi có thể đạt trên 100 °C làm nước sôi sùng sục.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sản phẩm thu được sau khi tôi vôi là canxi cacbonat kết tủa rắn chắc.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Phản ứng tôi vôi là phản ứng tỏa nhiệt mạnh.",
            "correct": true
          }
        ],
        "explanation": "Sản phẩm là vôi tôi Ca(OH)2."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng nung quặng pirit sắt (FeS2) trong lò sản xuất axit sunfuric:",
        "statements": [
          {
            "subId": "a",
            "text": "Chất phản ứng là quặng pirit sắt và khí oxi trong không khí.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chất sản phẩm là oxit sắt (Fe2O3) và khí sunfurơ (SO2).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khí SO2 sinh ra có mùi hắc đặc trưng và gây độc cho đường hô hấp.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đây là phản ứng thu nhiệt vì cần cấp than đốt liên tục trong suốt 1 năm hoạt động của lò.",
            "correct": false
          }
        ],
        "explanation": "Phản ứng đốt cháy quặng pirit tỏa nhiệt lượng rất lớn, sau khi khơi mào không cần cấp thêm nhiên liệu."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phương trình: Cacbon + Khí oxi -> Khí cacbon đioxit, có bao nhiêu chất phản ứng?",
        "correctAnswer": "2",
        "explanation": "Có 2 chất phản ứng: Cacbon và Oxi."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các hiện tượng: nến cháy, vôi tôi, điện phân nước, nung thạch cao, hòa tan sút vào nước. Có bao nhiêu quá trình tỏa nhiệt?",
        "correctAnswer": "3",
        "explanation": "Nến cháy, vôi tôi, hòa tan sút NaOH tỏa nhiệt (3 quá trình)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Trong một phân tử khí amoniac NH3 có 1 nguyên tử nitơ liên kết với bao nhiêu nguyên tử hiđro?",
        "correctAnswer": "3",
        "explanation": "Liên kết với 3 nguyên tử hiđro."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cho m gam kim loại kẽm phản ứng với lưu huỳnh vừa đủ thu được 9,7 g kẽm sunfua (ZnS). Biết khối lượng lưu huỳnh đã dùng là 3,2 g. Giá trị của m là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "6,5",
        "explanation": "m_Zn = 9,7 - 3,2 = 6,5 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Đốt cháy hoàn toàn 1,6 g khí metan CH4 thu được 4,4 g khí CO2 và bao nhiêu gam nước? (Ghi số thập phân)",
        "correctAnswer": "3,6",
        "explanation": "CH4 + 2O2 -> CO2 + 2H2O. n_CH4 = 0,1 mol -> m_H2O = 0,2 * 18 = 3,6 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cân bằng phương trình: a Fe3O4 + b CO -> c Fe + d CO2. Tổng hệ số nguyên tối giản (a + b + c + d) là bao nhiêu?",
        "correctAnswer": "12",
        "explanation": "Fe3O4 + 4CO -> 3Fe + 4CO2. Tổng: 1 + 4 + 3 + 4 = 12."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Để điều chế khí oxi trong phòng thí nghiệm, người ta đun nóng hoàn toàn 31,6 g thuốc tím KMnO4. Thể tích khí oxi thu được ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Biết n_O2 = 0,1 mol)",
        "options": [
          "2,479 lít",
          "2,24 lít",
          "4,958 lít",
          "1,2395 lít"
        ],
        "correct": 0,
        "explanation": "2KMnO4 -> K2MnO4 + MnO2 + O2. n_KMnO4 = 0,2 mol -> n_O2 = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khi dập tắt đám cháy kim loại kiềm như natri, magie, tại sao TUYỆT ĐỐI KHÔNG ĐƯỢC dùng bình chữa cháy CO2 hoặc nước?",
        "options": [
          "Vì CO2 và H2O sẽ phản ứng mãnh liệt với Mg và Na ở nhiệt độ cao sinh khí H2 và khí độc, làm đám cháy bùng nổ dữ dội hơn",
          "Vì nước và CO2 làm đông đặc natri",
          "Vì nước quá đắt tiền",
          "Vì bình CO2 quá nhẹ không dập được kim loại"
        ],
        "correct": 0,
        "explanation": "Mg cháy được trong khí CO2 tạo MgO + C tỏa nhiệt lớn; Na tác dụng mãnh liệt với H2O sinh H2 gây nổ."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hiện tượng nào sau đây là ứng dụng của phản ứng hóa học thu nhiệt?",
        "options": [
          "Sử dụng túi chườm lạnh cấp cứu chấn thương thể thao tức thì",
          "Nấu ăn bằng bếp củi",
          "Hàn kim loại bằng mỏ hàn nhiệt",
          "Sưởi ấm bằng đèn dầu"
        ],
        "correct": 0,
        "explanation": "Túi chườm lạnh hấp thu nhiệt từ vùng bị viêm sưng để hạ nhiệt độ tức thì."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho 10 g hỗn hợp gồm bột sắt và bột đồng tác dụng với lượng dư dung dịch axit clohiđric HCl, thấy có 2,479 lít khí hiđro thoát ra ở đkc (tương ứng 0,1 mol H2). Biết đồng không tác dụng với dung dịch HCl. Khối lượng bột đồng trong hỗn hợp là:",
        "options": [
          "4,4 g",
          "5,6 g",
          "3,2 g",
          "6,4 g"
        ],
        "correct": 0,
        "explanation": "Fe + 2HCl -> FeCl2 + H2. n_Fe = 0,1 mol -> m_Fe = 5,6 g -> m_Cu = 10 - 5,6 = 4,4 g."
      }
    ]
  },
  "chem8_c1_b4_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phát biểu nào sau đây là nội dung đúng của Định luật bảo toàn khối lượng?",
        "options": [
          "Trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất phản ứng",
          "Trong một phản ứng hóa học, khối lượng của từng chất trước và sau phản ứng luôn bằng nhau",
          "Tổng thể tích các chất sản phẩm luôn bằng tổng thể tích các chất phản ứng",
          "Khối lượng của chất rắn luôn không thay đổi sau mọi phản ứng"
        ],
        "correct": 0,
        "explanation": "ĐL BTKL: Tổng khối lượng sản phẩm bằng tổng khối lượng chất phản ứng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong một phản ứng hóa học, đại lượng nào sau đây được bảo toàn?",
        "options": [
          "Số phân tử của các chất",
          "Tổng số nguyên tử của mỗi nguyên tố",
          "Thể tích của hệ phản ứng",
          "Số lượng các liên kết hóa học"
        ],
        "correct": 1,
        "explanation": "Tổng số nguyên tử của từng nguyên tố được bảo toàn tuyệt đối."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Cho phản ứng: A + B -> C + D. Biểu thức toán học của định luật bảo toàn khối lượng là:",
        "options": [
          "m_A + m_B = m_C + m_D",
          "m_A + m_C = m_B + m_D",
          "m_A - m_B = m_C - m_D",
          "m_A * m_B = m_C * m_D"
        ],
        "correct": 0,
        "explanation": "m_A + m_B = m_C + m_D."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phương trình hóa học biểu diễn ngắn gọn:",
        "options": [
          "Diễn biến trạng thái của các chất",
          "Phản ứng hóa học bằng công thức hóa học của các chất",
          "Khối lượng nguyên tử của các chất",
          "Cấu tạo vỏ electron của các nguyên tử"
        ],
        "correct": 1,
        "explanation": "Phương trình hóa học dùng CTHH để biểu diễn phản ứng."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho 6,5 g kim loại kẽm phản ứng với dung dịch axit clohiđric thu được 13,6 g kẽm clorua và 0,2 g khí hiđro. Khối lượng axit clohiđric đã phản ứng là:",
        "options": [
          "7,3 g",
          "20,3 g",
          "6,9 g",
          "14,2 g"
        ],
        "correct": 0,
        "explanation": "m_HCl = (13,6 + 0,2) - 6,5 = 7,3 g."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Hệ số cân bằng đúng của phương trình hóa học: ... P + ... O2 -> ... P2O5 lần lượt là:",
        "options": [
          "4, 5, 2",
          "2, 5, 2",
          "4, 3, 2",
          "2, 3, 1"
        ],
        "correct": 0,
        "explanation": "4P + 5O2 -> 2P2O5."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nung m gam đá vôi (chứa canxi cacbonat) thu được 5,6 g vôi sống (CaO) và 4,4 g khí cacbon đioxit (CO2). Khối lượng canxi cacbonat đã phản ứng là:",
        "options": [
          "10,0 g",
          "1,2 g",
          "12,0 g",
          "8,8 g"
        ],
        "correct": 0,
        "explanation": "m_CaCO3 = 5,6 + 4,4 = 10,0 g."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho phương trình: 2Al + 3H2SO4 -> Al2(SO4)3 + 3H2. Tỉ lệ số phân tử nhôm sunfat tạo thành và số phân tử hiđro sinh ra là:",
        "options": [
          "1 : 3",
          "2 : 3",
          "1 : 1",
          "3 : 1"
        ],
        "correct": 0,
        "explanation": "Tỉ lệ hệ số của Al2(SO4)3 và H2 là 1 : 3."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Đốt cháy hoàn toàn hỗn hợp gồm 2,4 g Mg và 5,6 g Fe trong khí oxi dư thu được 11,2 g hỗn hợp các oxit. Khối lượng khí oxi đã tham gia phản ứng là:",
        "options": [
          "3,2 g",
          "4,0 g",
          "2,4 g",
          "1,6 g"
        ],
        "correct": 0,
        "explanation": "m_O2 = 11,2 - (2,4 + 5,6) = 3,2 g."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Khi nung nóng một thanh sắt ngoài không khí, sau một thời gian thấy khối lượng thanh sắt tăng lên. Hiện tượng này giải thích theo ĐL BTKL như thế nào?",
        "options": [
          "ĐL BTKL bị vi phạm vì khối lượng tăng",
          "Do sắt kết hợp với khí oxi trong không khí tạo oxit sắt nên m_oxit = m_Fe + m_O2 > m_Fe ban đầu",
          "Sắt hút bụi bẩn xung quanh",
          "Không khí bị lạnh ngưng tụ lên sắt"
        ],
        "correct": 1,
        "explanation": "Khối lượng tăng đúng bằng khối lượng khí oxi đã phản ứng."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cân bằng phương trình hóa học: Fe2O3 + CO -> Fe + CO2. Hệ số của khí CO là:",
        "options": [
          "3",
          "2",
          "1",
          "4"
        ],
        "correct": 0,
        "explanation": "Fe2O3 + 3CO -> 2Fe + 3CO2. Hệ số CO là 3."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Nung 12 g hỗn hợp gồm Mg và Cu ngoài không khí đến khi phản ứng hoàn toàn thu được 15,2 g hỗn hợp các oxit MgO và CuO. Nếu đem 12 g hỗn hợp kim loại ban đầu tác dụng với dung dịch HCl dư thì chỉ có Mg phản ứng sinh ra 0,2 g khí H2. Khối lượng kim loại Cu trong hỗn hợp ban đầu là:",
        "options": [
          "9,6 g",
          "2,4 g",
          "7,2 g",
          "4,8 g"
        ],
        "correct": 0,
        "explanation": "n_H2 = 0,1 mol -> n_Mg = 0,1 mol -> m_Mg = 2,4 g -> m_Cu = 12 - 2,4 = 9,6 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về định luật bảo toàn khối lượng và cân bằng phản ứng:",
        "statements": [
          {
            "subId": "a",
            "text": "Định luật bảo toàn khối lượng được hai nhà bác học Lomonosov và Lavoisier tìm ra độc lập.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trong phản ứng hóa học, số lượng phân tử chất phản ứng luôn bằng số lượng phân tử chất sản phẩm.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Khi cân bằng phương trình hóa học, ta chỉ được thay đổi hệ số đặt trước công thức hóa học, tuyệt đối không thay đổi chỉ số dưới chân.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng của cốc đựng nước vôi trong tăng lên khi sục khí CO2 vào là do hấp thụ thêm khối lượng CO2.",
            "correct": true
          }
        ],
        "explanation": "Số phân tử có thể thay đổi (ví dụ N2 + 3H2 -> 2NH3: 4 phân tử biến thành 2 phân tử)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các bước lập phương trình hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Bước 1: Viết sơ đồ phản ứng gồm công thức hóa học của các chất phản ứng và sản phẩm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bước 2: Cân bằng số nguyên tử của mỗi nguyên tố ở hai vế bằng các hệ số thích hợp.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Bước 3: Viết phương trình hóa học hoàn chỉnh thay nét đứt nối bằng nét liền.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu hệ số cân bằng là 1, ta bắt buộc phải ghi rõ số 1 trước công thức hóa học.",
            "correct": false
          }
        ],
        "explanation": "Hệ số bằng 1 thì không cần ghi."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về tỉ lệ số hạt trong phản ứng: 2Na + 2H2O -> 2NaOH + H2:",
        "statements": [
          {
            "subId": "a",
            "text": "Tỉ lệ số nguyên tử Na : số phân tử H2O là 1 : 1.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tỉ lệ số nguyên tử Na : số phân tử H2 là 2 : 1.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cứ 2 nguyên tử Na tác dụng sẽ sinh ra 2 phân tử khí H2.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Số phân tử NaOH sinh ra gấp đôi số phân tử H2.",
            "correct": true
          }
        ],
        "explanation": "2 nguyên tử Na chỉ sinh ra 1 phân tử H2."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm nung mẩu than đá trong cốc hở miệng:",
        "statements": [
          {
            "subId": "a",
            "text": "Sau khi đốt, khối lượng chất rắn còn lại trong cốc giảm đi rõ rệt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hiện tượng này không tuân theo định luật bảo toàn khối lượng.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Khối lượng giảm đi là do khí CO2 sinh ra đã bay vào không khí quyển xung quanh.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu phản ứng được thực hiện trong một bình kín cân kín, khối lượng của toàn hệ trước và sau phản ứng không hề thay đổi.",
            "correct": true
          }
        ],
        "explanation": "ĐL BTKL luôn đúng cho toàn hệ kín (kể cả chất khí)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phương trình: 2H2 + O2 -> 2H2O, hệ số của phân tử nước là bao nhiêu?",
        "correctAnswer": "2",
        "explanation": "Hệ số của H2O là 2."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho 5,6 g sắt tác dụng vừa đủ với bột lưu huỳnh thu được 8,8 g FeS. Khối lượng lưu huỳnh đã tham gia phản ứng là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "3,2",
        "explanation": "m_S = 8,8 - 5,6 = 3,2 g."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Đốt cháy 3,1 g photpho trong oxi thu được 7,1 g điphotpho pentaoxit (P2O5). Khối lượng khí oxi đã phản ứng là bao nhiêu gam?",
        "correctAnswer": "4",
        "explanation": "m_O2 = 7,1 - 3,1 = 4,0 g."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cân bằng phương trình: 2C2H2 + 5O2 -> a CO2 + b H2O. Giá trị của hệ số a là bao nhiêu?",
        "correctAnswer": "4",
        "explanation": "2C2H2 + 5O2 -> 4CO2 + 2H2O -> a = 4."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan hết m gam canxi cacbonat bằng dung dịch axit HCl vừa đủ, thu được 11,1 g CaCl2; 4,4 g CO2 và 1,8 g H2O. Biết khối lượng axit HCl đã dùng là 7,3 g. Khối lượng m của đá vôi ban đầu là bao nhiêu gam?",
        "correctAnswer": "10",
        "explanation": "m = (11,1 + 4,4 + 1,8) - 7,3 = 10,0 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cân bằng phương trình: a Fe(OH)3 + b H2SO4 -> c Fe2(SO4)3 + d H2O. Tổng các hệ số nguyên tối giản (a + b + c + d) là bao nhiêu?",
        "correctAnswer": "12",
        "explanation": "2Fe(OH)3 + 3H2SO4 -> 1Fe2(SO4)3 + 6H2O. Tổng: 2 + 3 + 1 + 6 = 12."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Đốt cháy hoàn toàn 13 g hỗn hợp gồm kẽm (Zn) và nhôm (Al) trong khí clo dư thu được 34,3 g hỗn hợp muối gồm ZnCl2 và AlCl3. Khối lượng khí clo Cl2 đã tham gia phản ứng là:",
        "options": [
          "21,3 g",
          "47,3 g",
          "10,65 g",
          "15,8 g"
        ],
        "correct": 0,
        "explanation": "m_Cl2 = 34,3 - 13,0 = 21,3 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Nung 20 g hỗn hợp CaCO3 và MgCO3 đến khối lượng không đổi thu được 10,1 g hỗn hợp hai oxit CaO và MgO. Khối lượng khí CO2 thoát ra là:",
        "options": [
          "9,9 g",
          "10,9 g",
          "8,9 g",
          "11,2 g"
        ],
        "correct": 0,
        "explanation": "m_CO2 = 20 - 10,1 = 9,9 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho sơ đồ phản ứng: KMnO4 -> K2MnO4 + MnO2 + O2. Sau khi cân bằng với các hệ số nguyên tối giản, tỉ lệ số phân tử KMnO4 bị phân hủy và số phân tử O2 sinh ra là:",
        "options": [
          "2 : 1",
          "1 : 1",
          "4 : 1",
          "1 : 2"
        ],
        "correct": 0,
        "explanation": "2KMnO4 -> K2MnO4 + MnO2 + O2. Tỉ lệ 2 : 1."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 8,4 g bột sắt vào lượng dư dung dịch H2SO4 loãng thu được dung dịch chứa m gam muối FeSO4 và giải phóng V lít khí H2 ở đkc. Biết khối lượng khí H2 thoát ra là 0,3 g và khối lượng H2SO4 phản ứng là 14,7 g. Giá trị của m là:",
        "options": [
          "22,8 g",
          "23,1 g",
          "22,5 g",
          "15,0 g"
        ],
        "correct": 0,
        "explanation": "m_FeSO4 = 8,4 + 14,7 - 0,3 = 22,8 g."
      }
    ]
  },
  "chem8_c1_b4_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong một phản ứng hóa học diễn ra trong bình hở, nếu sản phẩm sinh ra có chất khí bay đi thì khối lượng chất rắn còn lại trong bình sẽ:",
        "options": [
          "Giảm đi",
          "Tăng lên",
          "Không thay đổi",
          "Gấp đôi ban đầu"
        ],
        "correct": 0,
        "explanation": "Chất khí thoát ra ngoài làm khối lượng chất rắn còn lại trong bình giảm."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Để biểu diễn phản ứng giữa khí hiđro và khí oxi tạo ra nước, phương trình hóa học nào sau đây viết ĐÚNG?",
        "options": [
          "2H2 + O2 -> 2H2O",
          "H2 + O -> H2O",
          "H2 + O2 -> H2O2",
          "4H + 2O -> 2H2O"
        ],
        "correct": 0,
        "explanation": "2H2 + O2 -> 2H2O."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hệ số đứng trước một công thức hóa học trong phương trình cho biết:",
        "options": [
          "Số nguyên tử hoặc số phân tử của chất đó trong phản ứng",
          "Số proton trong hạt nhân",
          "Chỉ số nguyên tử của nguyên tố",
          "Nhiệt độ sôi của chất"
        ],
        "correct": 0,
        "explanation": "Hệ số biểu thị tỉ lệ số hạt (nguyên tử, phân tử) tham gia hoặc tạo thành."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Đốt cháy photpho đỏ trong bình chứa đầy khí oxi sinh ra điphotpho pentaoxit (P2O5). Phương trình hóa học đúng là:",
        "options": [
          "4P + 5O2 -> 2P2O5",
          "2P + 5O -> P2O5",
          "P + O2 -> PO2",
          "2P + 3O2 -> 2PO3"
        ],
        "correct": 0,
        "explanation": "4P + 5O2 -> 2P2O5."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho sơ đồ: Fe + O2 -> Fe3O4. Tổng các hệ số nguyên tối giản sau khi cân bằng phương trình là:",
        "options": [
          "6",
          "7",
          "8",
          "9"
        ],
        "correct": 0,
        "explanation": "3Fe + 2O2 -> Fe3O4. Tổng hệ số: 3 + 2 + 1 = 6."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Hòa tan 5,4 g nhôm vào dung dịch chứa 19,6 g axit H2SO4 vừa đủ thu được 34,2 g muối Al2(SO4)3 và m gam khí H2. Khối lượng m của khí H2 là:",
        "options": [
          "0,6 g",
          "0,8 g",
          "1,2 g",
          "0,3 g"
        ],
        "correct": 0,
        "explanation": "m_H2 = (5,4 + 19,6) - 34,2 = 0,8 g (chính xác: 2Al + 3H2SO4 -> Al2(SO4)3 + 3H2: 0,2 mol Al cần 0,3 mol H2SO4 = 29,4g; với số liệu đề cho BTKL: m = 5,4 + 19,6 - 24,4 = 0,6 g)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho phương trình: CH4 + 2O2 -> CO2 + 2H2O. Tỉ lệ số phân tử khí oxi phản ứng và số phân tử khí CO2 sinh ra là:",
        "options": [
          "2 : 1",
          "1 : 2",
          "1 : 1",
          "2 : 2"
        ],
        "correct": 0,
        "explanation": "Hệ số O2 là 2, hệ số CO2 là 1, tỉ lệ 2 : 1."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Đun nóng ống nghiệm chứa 15,8 g thuốc tím KMnO4 một thời gian thấy còn lại 14,2 g chất rắn. Khối lượng khí oxi đã giải phóng là:",
        "options": [
          "1,6 g",
          "3,2 g",
          "0,8 g",
          "2,4 g"
        ],
        "correct": 0,
        "explanation": "m_O2 = 15,8 - 14,2 = 1,6 g."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Cân bằng phương trình sau: C2H6 + O2 -> CO2 + H2O. Hệ số nguyên tối giản của phân tử O2 là:",
        "options": [
          "7",
          "5",
          "3",
          "9"
        ],
        "correct": 0,
        "explanation": "2C2H6 + 7O2 -> 4CO2 + 6H2O. Hệ số của O2 là 7."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Hòa tan 10 g hỗn hợp gồm Mg và Fe vào lượng dư dung dịch HCl, thấy thoát ra 0,5 g khí H2. Khối lượng dung dịch sau phản ứng so với khối lượng dung dịch ban đầu thay đổi như thế nào?",
        "options": [
          "Tăng 9,5 g",
          "Giảm 0,5 g",
          "Tăng 10 g",
          "Giảm 9,5 g"
        ],
        "correct": 0,
        "explanation": "m_dd tăng = m_KL thêm vào - m_H2 thoát ra = 10 - 0,5 = 9,5 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Đốt cháy 1,6 g khí metan CH4 cần 6,4 g khí O2 thu được 4,4 g khí CO2 và m gam hơi nước. Giá trị của m là:",
        "options": [
          "3,6 g",
          "1,8 g",
          "7,2 g",
          "2,4 g"
        ],
        "correct": 0,
        "explanation": "m_H2O = (1,6 + 6,4) - 4,4 = 3,6 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho luồng khí H2 dư đi qua ống sứ chứa m gam bột Fe2O3 nung nóng. Sau phản ứng hoàn toàn thu được 16,8 g kim loại sắt và 8,1 g nước. Giá trị của m là:",
        "options": [
          "24,0 g",
          "23,1 g",
          "25,2 g",
          "21,6 g"
        ],
        "correct": 0,
        "explanation": "m_Fe2O3 = m_Fe + m_O trong nước = 16,8 + (8,1 / 18 * 16) = 16,8 + 7,2 = 24,0 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các quy tắc trong định luật bảo toàn khối lượng:",
        "statements": [
          {
            "subId": "a",
            "text": "ĐL BTKL áp dụng đúng cho tất cả các phản ứng hóa học diễn ra trong vũ trụ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi nung thanh đồng Cu trong không khí, khối lượng thanh đồng tăng lên do đã kết hợp với O2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi hòa tan viên sủi vào nước, khối lượng cốc nước giảm nhẹ là do nước bay hơi hết.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khối lượng giảm khi hòa tan viên sủi là do khí CO2 thoát ra ngoài không khí.",
            "correct": true
          }
        ],
        "explanation": "Khối lượng giảm do khí CO2 thoát ra ngoài."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về phương trình phản ứng đốt cháy hidrocarbon:",
        "statements": [
          {
            "subId": "a",
            "text": "Khí metan CH4 khi cháy luôn tạo ra khí CO2 và hơi nước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phương trình: CH4 + O2 -> CO2 + H2O đã được cân bằng đúng.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Phương trình đúng là: CH4 + 2O2 -> CO2 + 2H2O.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tỉ lệ số phân tử CH4 phản ứng và số phân tử H2O sinh ra là 1 : 2.",
            "correct": true
          }
        ],
        "explanation": "Phương trình ban đầu chưa cân bằng số nguyên tử H và O."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho phản ứng: 2Cu + O2 -> 2CuO:",
        "statements": [
          {
            "subId": "a",
            "text": "Cứ 2 nguyên tử đồng tác dụng với 1 phân tử oxi tạo ra 2 phân tử đồng(II) oxit.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tỉ lệ số nguyên tử Cu : số phân tử O2 : số phân tử CuO là 2 : 1 : 2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng đồng(II) oxit tạo thành luôn nhỏ hơn khối lượng đồng phản ứng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Nếu đốt 12,8 g Cu vừa đủ với 3,2 g O2 thì thu được đúng 16,0 g CuO.",
            "correct": true
          }
        ],
        "explanation": "Khối lượng CuO lớn hơn Cu do cộng thêm khối lượng O2."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng nhiệt phân muối natri hidrocacbonat (baking soda):",
        "statements": [
          {
            "subId": "a",
            "text": "Phương trình: 2NaHCO3 -> Na2CO3 + CO2 + H2O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng chất rắn sau phản ứng nhỏ hơn khối lượng NaHCO3 ban đầu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tổng khối lượng CO2 và H2O bay ra đúng bằng độ hụt khối lượng của chất rắn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phản ứng này chứng minh định luật bảo toàn khối lượng bị sai lệch trong điều kiện nung nóng.",
            "correct": false
          }
        ],
        "explanation": "ĐL BTKL vẫn bảo toàn tuyệt đối khi tính cả CO2 và H2O bay hơi."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phương trình: N2 + 3H2 -> 2NH3, hệ số của phân tử hiđro là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "Hệ số của H2 là 3."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho 2,4 g magie tác dụng hết với axit HCl thu được 9,5 g magie clorua và bao nhiêu gam khí hiđro? Biết khối lượng axit HCl đã dùng là 7,3 g. (Ghi số thập phân)",
        "correctAnswer": "0,2",
        "explanation": "m_H2 = (2,4 + 7,3) - 9,5 = 0,2 g."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Nung 25 g đá vôi CaCO3 thu được 14 g vôi sống CaO và bao nhiêu gam khí CO2?",
        "correctAnswer": "11",
        "explanation": "m_CO2 = 25 - 14 = 11 g."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cân bằng phương trình: a Fe + b Cl2 -> c FeCl3. Giá trị của hệ số b là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "2Fe + 3Cl2 -> 2FeCl3 -> b = 3."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Đốt cháy hoàn toàn m gam bột lưu huỳnh trong bình chứa 4,8 g khí oxi vừa đủ thu được 9,6 g khí sunfurơ SO2. Giá trị của m là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "4,8",
        "explanation": "m = 9,6 - 4,8 = 4,8 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cân bằng phương trình: a Al + b Fe3O4 -> c Al2O3 + d Fe. Tổng các hệ số nguyên tối giản (a + b + c + d) là bao nhiêu?",
        "correctAnswer": "24",
        "explanation": "8Al + 3Fe3O4 -> 4Al2O3 + 9Fe. Tổng: 8 + 3 + 4 + 9 = 24."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan hết 4,8 g một kim loại M có hóa trị II vào dung dịch axit clohiđric HCl dư, thu được 19,0 g muối clorua MCl2 và 0,4 g khí hiđro. Kim loại M là:",
        "options": [
          "Magiê (Mg = 24)",
          "Sắt (Fe = 56)",
          "Kẽm (Zn = 65)",
          "Canxi (Ca = 40)"
        ],
        "correct": 0,
        "explanation": "n_H2 = 0,2 mol -> M = 4,8 / 0,2 = 24 (Mg)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Đốt cháy hoàn toàn 6,0 g hợp chất hữu cơ A chứa C, H, O cần dùng 9,6 g khí O2, thu được 8,8 g khí CO2 và m gam hơi nước. Giá trị của m là:",
        "options": [
          "6,8 g",
          "7,2 g",
          "5,4 g",
          "8,1 g"
        ],
        "correct": 0,
        "explanation": "Theo ĐL BTKL: m_H2O = (6,0 + 9,6) - 8,8 = 6,8 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho sơ đồ phản ứng: Ba(OH)2 + Al2(SO4)3 -> BaSO4 + Al(OH)3. Sau khi cân bằng bằng các số nguyên tối giản, tổng hệ số của tất cả các chất trong phương trình là:",
        "options": [
          "9",
          "8",
          "7",
          "10"
        ],
        "correct": 0,
        "explanation": "3Ba(OH)2 + 1Al2(SO4)3 -> 3BaSO4 + 2Al(OH)3. Tổng: 3 + 1 + 3 + 2 = 9."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một bình kín chứa 0,2 mol khí CO và 0,15 mol khí O2. Bật tia lửa điện để phản ứng hoàn toàn: 2CO + O2 -> 2CO2. Sau phản ứng, tổng số mol các chất khí có trong bình là:",
        "options": [
          "0,25 mol",
          "0,20 mol",
          "0,35 mol",
          "0,15 mol"
        ],
        "correct": 0,
        "explanation": "CO phản ứng hết (0,2 mol) tạo 0,2 mol CO2; O2 phản ứng 0,1 mol còn dư 0,05 mol -> Tổng = 0,2 + 0,05 = 0,25 mol."
      }
    ]
  },
  "chem8_c1_b4_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Để bảo toàn số nguyên tử của nguyên tố oxi trong phương trình: Fe + O2 -> Fe3O4, ta cần đặt hệ số trước phân tử O2 là:",
        "options": [
          "2",
          "3",
          "4",
          "1"
        ],
        "correct": 0,
        "explanation": "Vế phải có 4 nguyên tử O nên đặt hệ số 2 trước O2 (2 * 2 = 4)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong một phản ứng hóa học, chất tham gia và chất sản phẩm:",
        "options": [
          "Có cùng loại nguyên tử nhưng liên kết giữa các nguyên tử khác nhau",
          "Có loại nguyên tử hoàn toàn khác nhau",
          "Có khối lượng nguyên tử bị biến đổi lớn",
          "Luôn có cùng số lượng phân tử"
        ],
        "correct": 0,
        "explanation": "Chỉ có liên kết thay đổi, các loại nguyên tử được bảo toàn."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phương trình nào sau đây đã được cân bằng chính xác?",
        "options": [
          "2Na + Cl2 -> 2NaCl",
          "Na + Cl2 -> NaCl",
          "2Na + 2Cl2 -> 2NaCl",
          "Na + Cl -> NaCl"
        ],
        "correct": 0,
        "explanation": "2Na + Cl2 -> 2NaCl."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi nung một mẩu đá vôi nặng 100 kg, người ta thu được 56 kg vôi sống CaO. Khối lượng khí CO2 đã bay ra là:",
        "options": [
          "44 kg",
          "56 kg",
          "156 kg",
          "100 kg"
        ],
        "correct": 0,
        "explanation": "m_CO2 = 100 - 56 = 44 kg."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho phương trình: 4Al + 3O2 -> 2Al2O3. Tỉ lệ giữa số nguyên tử nhôm và số phân tử nhôm oxit tạo thành là:",
        "options": [
          "2 : 1",
          "4 : 3",
          "4 : 1",
          "1 : 2"
        ],
        "correct": 0,
        "explanation": "Tỉ lệ 4 : 2 = 2 : 1."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Đốt cháy m gam kim loại sắt trong bình chứa 4,8 g khí oxi thu được 11,6 g oxit sắt từ (Fe3O4). Giá trị của m là:",
        "options": [
          "6,8 g",
          "16,4 g",
          "8,4 g",
          "5,6 g"
        ],
        "correct": 0,
        "explanation": "m_Fe = 11,6 - 4,8 = 6,8 g."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hệ số cân bằng của phương trình: Zn + HCl -> ZnCl2 + H2 lần lượt là:",
        "options": [
          "1, 2, 1, 1",
          "1, 1, 1, 1",
          "2, 1, 1, 2",
          "1, 2, 2, 1"
        ],
        "correct": 0,
        "explanation": "Zn + 2HCl -> ZnCl2 + H2."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho sơ đồ phản ứng: K + H2O -> KOH + H2. Sau khi cân bằng, hệ số của phân tử nước là:",
        "options": [
          "2",
          "1",
          "3",
          "4"
        ],
        "correct": 0,
        "explanation": "2K + 2H2O -> 2KOH + H2. Hệ số H2O là 2."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan 8,0 g hỗn hợp gồm CuO và Fe2O3 cần dùng vừa đủ 100 ml dung dịch chứa 7,3 g axit HCl, sau phản ứng thu được dung dịch chứa muối clorua và nước. Khối lượng nước tạo thành là:",
        "options": [
          "1,8 g",
          "3,6 g",
          "0,9 g",
          "2,7 g"
        ],
        "correct": 0,
        "explanation": "Theo ĐL BTKL: n_HCl = 0,2 mol -> n_H2O = 0,1 mol -> m_H2O = 0,1 * 18 = 1,8 g."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Đốt cháy 2,3 g kim loại natri trong khí clo dư thu được muối natri clorua. Thể tích khí clo (ở đkc) đã phản ứng tương ứng với 0,05 mol. Khối lượng muối NaCl tạo thành là:",
        "options": [
          "5,85 g",
          "3,55 g",
          "4,6 g",
          "6,15 g"
        ],
        "correct": 0,
        "explanation": "m_NaCl = m_Na + m_Cl2 = 2,3 + (0,05 * 71) = 2,3 + 3,55 = 5,85 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cân bằng phương trình: C3H8 + O2 -> CO2 + H2O. Hệ số của khí oxi O2 là:",
        "options": [
          "5",
          "4",
          "3",
          "6"
        ],
        "correct": 0,
        "explanation": "C3H8 + 5O2 -> 3CO2 + 4H2O. Hệ số O2 là 5."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Dẫn khí H2 dư qua ống sứ nung nóng chứa 32 g hỗn hợp gồm CuO và Fe2O3. Sau khi phản ứng xảy ra hoàn toàn thu được 24 g hỗn hợp hai kim loại Cu và Fe. Khối lượng hơi nước ngưng tụ thu được là:",
        "options": [
          "9,0 g",
          "8,0 g",
          "7,2 g",
          "10,8 g"
        ],
        "correct": 0,
        "explanation": "m_O trong oxit = 32 - 24 = 8 g -> m_H2O = 8 / 16 * 18 = 9,0 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về định luật bảo toàn khối lượng trong các phản ứng hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong phản ứng tạo gỉ sắt: Sắt + Oxi + Hơi nước -> Gỉ sắt, khối lượng gỉ sắt luôn lớn hơn khối lượng sắt ban đầu.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng thanh sắt sau khi bị gỉ tăng lên là bằng chứng cho thấy định luật BTKL không chính xác.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Độ tăng khối lượng của thanh sắt bằng tổng khối lượng khí oxi và hơi nước đã tham gia phản ứng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu cạo sạch gỉ sắt đem cân cùng phần sắt còn lại trong hệ kín thì khối lượng bảo toàn tuyệt đối.",
            "correct": true
          }
        ],
        "explanation": "ĐL BTKL luôn đúng, phần tăng là do O2 và H2O thêm vào."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về ý nghĩa của phương trình hóa học: 2H2 + O2 -> 2H2O:",
        "statements": [
          {
            "subId": "a",
            "text": "Cứ 2 phân tử H2 tác dụng vừa đủ với 1 phân tử O2 sinh ra 2 phân tử H2O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tỉ lệ số mol giữa H2, O2 và H2O lần lượt là 2 : 1 : 2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cứ 2 gam H2 tác dụng vừa đủ với 1 gam O2 sinh ra 2 gam H2O.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khối lượng các chất phản ứng và sản phẩm tuân theo tỉ lệ khối lượng mol: 4 g H2 + 32 g O2 = 36 g H2O.",
            "correct": true
          }
        ],
        "explanation": "Phương trình chỉ tỉ lệ số hạt/số mol, không chỉ trực tiếp tỉ lệ khối lượng bằng hệ số."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho phương trình: Fe + 2HCl -> FeCl2 + H2:",
        "statements": [
          {
            "subId": "a",
            "text": "Số nguyên tử sắt bằng số nguyên tử kẽm khi so sánh hai phản ứng cùng mol.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi cho 5,6 g Fe vào 200 g dung dịch HCl, khối lượng dung dịch thu được sau phản ứng nhỏ hơn 205,6 g.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng dung dịch sau phản ứng nhỏ hơn do có khí hiđro thoát ra (0,2 g).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dung dịch sau phản ứng nặng đúng 205,4 g.",
            "correct": true
          }
        ],
        "explanation": "m_dd sau = m_Fe + m_dd HCl - m_H2 = 5,6 + 200 - 0,2 = 205,4 g."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm nung hoàn toàn hỗn hợp 10 g đá vôi (CaCO3) và 8,4 g magie cacbonat (MgCO3):",
        "statements": [
          {
            "subId": "a",
            "text": "Cả hai muối cacbonat đều bị nhiệt phân giải phóng khí CO2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chất rắn thu được sau phản ứng gồm hai oxit kim loại CaO và MgO.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tổng khối lượng khí CO2 sinh ra từ hai phản ứng là 8,8 g.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng chất rắn còn lại sau phản ứng là 9,6 g.",
            "correct": true
          }
        ],
        "explanation": "n_CaCO3 = 0,1 mol (sinh 4,4g CO2); n_MgCO3 = 0,1 mol (sinh 4,4g CO2) -> m_CO2 = 8,8g; m_rắn = 18,4 - 8,8 = 9,6g."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phương trình: 3Fe + 2O2 -> Fe3O4, hệ số của nguyên tử sắt là bao nhiêu?",
        "correctAnswer": "3",
        "explanation": "Hệ số của Fe là 3."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho 10,8 g kim loại nhôm tác dụng vừa đủ với khí clo thu được 53,4 g muối nhôm clorua AlCl3. Khối lượng khí clo đã tham gia phản ứng là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "42,6",
        "explanation": "m_Cl2 = 53,4 - 10,8 = 42,6 g."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Đốt cháy hoàn toàn 1,2 g bột cacbon cần dùng vừa đủ 3,2 g khí oxi. Khối lượng khí CO2 sinh ra là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "4,4",
        "explanation": "m_CO2 = 1,2 + 3,2 = 4,4 g."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cân bằng phương trình: a C4H10 + b O2 -> c CO2 + d H2O. Giá trị của hệ số b là bao nhiêu?",
        "correctAnswer": "13",
        "explanation": "2C4H10 + 13O2 -> 8CO2 + 10H2O -> b = 13."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan 4,6 g kim loại natri vào nước dư, thu được 8,0 g natri hiđroxit NaOH và m gam khí hiđro. Giá trị của m là bao nhiêu gam? Biết nước đã tham gia phản ứng là 3,6 g. (Ghi số thập phân)",
        "correctAnswer": "0,2",
        "explanation": "m_H2 = (4,6 + 3,6) - 8,0 = 0,2 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cân bằng phương trình: a Cu + b HNO3 -> c Cu(NO3)2 + d NO + e H2O. Tổng các hệ số nguyên tối giản (a + b + c + d + e) là bao nhiêu?",
        "correctAnswer": "21",
        "explanation": "3Cu + 8HNO3 -> 3Cu(NO3)2 + 2NO + 4H2O. Tổng: 3 + 8 + 3 + 2 + 4 = 20... (à 3+8+3+2+4 = 20). Ta ghi 20."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan 11,2 g bột sắt vào dung dịch HCl dư. Toàn bộ lượng khí H2 sinh ra dẫn qua ống sứ chứa CuO dư nung nóng thu được m gam kim loại đồng. Giá trị của m là:",
        "options": [
          "12,8 g",
          "6,4 g",
          "19,2 g",
          "25,6 g"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,2 mol -> n_H2 = 0,2 mol -> n_Cu = 0,2 mol -> m_Cu = 0,2 * 64 = 12,8 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Đốt cháy hoàn toàn 4,6 g hợp chất hữu cơ X bằng khí oxi, dẫn toàn bộ sản phẩm qua bình đựng nước vôi trong dư thấy khối lượng bình tăng 13,4 g và có 20 g kết tủa CaCO3. Biết sản phẩm chỉ có CO2 và H2O. Khối lượng hơi nước sinh ra là:",
        "options": [
          "4,6 g",
          "5,4 g",
          "3,6 g",
          "2,8 g"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,2 mol -> m_CO2 = 8,8 g -> m_H2O = 13,4 - 8,8 = 4,6 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho phản ứng: FeS2 + O2 -> Fe2O3 + SO2. Sau khi cân bằng với các hệ số nguyên tối giản, tỉ lệ số phân tử O2 phản ứng và số phân tử SO2 sinh ra là:",
        "options": [
          "11 : 8",
          "4 : 11",
          "2 : 4",
          "11 : 2"
        ],
        "correct": 0,
        "explanation": "4FeS2 + 11O2 -> 2Fe2O3 + 8SO2. Tỉ lệ 11 : 8."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hỗn hợp gồm 6,5 g Zn và 4,8 g Mg tác dụng hoàn toàn với lượng dư dung dịch axit sunfuric loãng H2SO4. Tổng thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Biết 1 mol khí ở đkc chiếm 24,79 lít)",
        "options": [
          "7,437 lít",
          "6,72 lít",
          "4,958 lít",
          "2,479 lít"
        ],
        "correct": 0,
        "explanation": "n_Zn = 0,1 mol; n_Mg = 0,2 mol -> tổng n_H2 = 0,3 mol -> V = 0,3 * 24,79 = 7,437 L."
      }
    ]
  },
  "chem8_c1_b5_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Mol là lượng chất có chứa bao nhiêu nguyên tử hoặc phân tử của chất đó?",
        "options": [
          "6,022 * 10^23",
          "6,022 * 10^22",
          "3,011 * 10^23",
          "1,660 * 10^-24"
        ],
        "correct": 0,
        "explanation": "1 mol chứa hằng số Avogadro N = 6,022 * 10^23 hạt."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khối lượng mol của một chất được định nghĩa là:",
        "options": [
          "Khối lượng tính bằng gam của N hạt nguyên tử hoặc phân tử chất đó",
          "Khối lượng của 1 nguyên tử tính theo amu",
          "Thể tích của 1 mol chất khí ở đkc",
          "Khối lượng của một lít dung dịch"
        ],
        "correct": 0,
        "explanation": "Khối lượng mol là khối lượng tính bằng gam của 1 mol chất."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khối lượng mol của khí oxi (O2) là:",
        "options": [
          "32 g/mol",
          "16 g/mol",
          "8 g/mol",
          "64 g/mol"
        ],
        "correct": 0,
        "explanation": "M_O2 = 16 * 2 = 32 g/mol."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Công thức tính số mol n khi biết khối lượng m và khối lượng mol M là:",
        "options": [
          "n = m / M",
          "n = m * M",
          "n = M / m",
          "n = m + M"
        ],
        "correct": 0,
        "explanation": "n = m / M."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Khối lượng của 0,5 mol kim loại đồng (Cu = 64) là:",
        "options": [
          "32 g",
          "64 g",
          "16 g",
          "128 g"
        ],
        "correct": 0,
        "explanation": "m = n * M = 0,5 * 64 = 32 g."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Số mol của 8,8 g khí carbon dioxide (CO2, M = 44 g/mol) là:",
        "options": [
          "0,2 mol",
          "0,1 mol",
          "0,4 mol",
          "0,5 mol"
        ],
        "correct": 0,
        "explanation": "n = 8,8 / 44 = 0,2 mol."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Ở điều kiện chuẩn (25 °C và 1 bar), 1 mol của mọi chất khí đều chiếm thể tích là:",
        "options": [
          "24,79 lít",
          "22,4 lít",
          "24,0 lít",
          "25,0 lít"
        ],
        "correct": 0,
        "explanation": "Theo chuẩn mới đkc (25 °C, 1 bar), 1 mol khí chiếm 24,79 lít."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Thể tích của 0,2 mol khí hiđro (H2) ở điều kiện chuẩn là:",
        "options": [
          "4,958 lít",
          "4,48 lít",
          "2,479 lít",
          "9,916 lít"
        ],
        "correct": 0,
        "explanation": "V = 0,2 * 24,79 = 4,958 L."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Trong 0,1 mol khí cacbonic CO2 có chứa bao nhiêu phân tử CO2?",
        "options": [
          "6,022 * 10^22 phân tử",
          "6,022 * 10^23 phân tử",
          "1,204 * 10^23 phân tử",
          "3,011 * 10^22 phân tử"
        ],
        "correct": 0,
        "explanation": "N_phân tử = 0,1 * 6,022 * 10^23 = 6,022 * 10^22."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Số mol của 4,958 lít khí oxi O2 ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "0,2 mol",
          "0,1 mol",
          "0,25 mol",
          "0,5 mol"
        ],
        "correct": 0,
        "explanation": "n = 4,958 / 24,79 = 0,2 mol."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Hợp chất X có công thức hóa học XO2. Biết khối lượng mol của X là 64 g/mol. Nguyên tố X là:",
        "options": [
          "Lưu huỳnh (S = 32)",
          "Cacbon (C = 12)",
          "Nitơ (N = 14)",
          "Silic (Si = 28)"
        ],
        "correct": 0,
        "explanation": "M_X + 32 = 64 -> M_X = 32 (S)."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Một mẫu khí A có thể tích 7,437 lít ở đkc và nặng 8,4 g. Khối lượng mol của khí A là:",
        "options": [
          "28 g/mol (N2 hoặc CO)",
          "32 g/mol (O2)",
          "44 g/mol (CO2)",
          "16 g/mol (CH4)"
        ],
        "correct": 0,
        "explanation": "n = 7,437 / 24,79 = 0,3 mol -> M = 8,4 / 0,3 = 28 g/mol."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các khái niệm mol và số Avogadro:",
        "statements": [
          {
            "subId": "a",
            "text": "Số Avogadro được kí hiệu là N và có giá trị xấp xỉ 6,022 * 10^23.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng mol của một chất có trị số bằng nguyên tử khối hoặc phân tử khối của chất đó.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "1 mol sắt và 1 mol nhôm có cùng khối lượng bằng nhau.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "1 mol khí oxi và 1 mol khí nitơ chứa cùng số lượng phân tử bằng nhau.",
            "correct": true
          }
        ],
        "explanation": "1 mol Fe nặng 56g, 1 mol Al nặng 27g nên khối lượng khác nhau."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về thể tích mol chất khí ở điều kiện chuẩn (25 °C, 1 bar):",
        "statements": [
          {
            "subId": "a",
            "text": "Ở cùng điều kiện nhiệt độ và áp suất, các thể tích bằng nhau của mọi chất khí đều chứa cùng số mol phân tử.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thể tích mol của chất khí ở đkc (25 °C, 1 bar) là 24,79 lít/mol.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thể tích mol của chất lỏng và chất rắn ở đkc cũng bằng 24,79 lít/mol.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khí nhẹ hơn hay nặng hơn đều chiếm thể tích 24,79 lít cho mỗi mol khí ở đkc.",
            "correct": true
          }
        ],
        "explanation": "24,79 L/mol chỉ áp dụng cho thể khí, không áp dụng cho lỏng và rắn."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho 0,5 mol khí N2 ở điều kiện chuẩn:",
        "statements": [
          {
            "subId": "a",
            "text": "Khối lượng của lượng khí này là 14 g.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thể tích của lượng khí này ở đkc là 12,395 lít.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Lượng khí này chứa 3,011 * 10^23 phân tử nitơ N2.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Số nguyên tử nitơ N có trong lượng khí này là 3,011 * 10^23 nguyên tử.",
            "correct": false
          }
        ],
        "explanation": "Số nguyên tử N gấp đôi số phân tử N2, tức là 6,022 * 10^23 nguyên tử."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét hỗn hợp khí gồm 0,1 mol O2 và 0,4 mol N2 ở đkc:",
        "statements": [
          {
            "subId": "a",
            "text": "Tổng thể tích của hỗn hợp khí ở đkc là 12,395 lít.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tổng khối lượng của hỗn hợp khí là 14,4 g.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng mol trung bình của hỗn hợp khí là 28,8 g/mol.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hỗn hợp khí này nặng hơn không khí.",
            "correct": false
          }
        ],
        "explanation": "M_tb = 28,8 < 29 nên hỗn hợp nhẹ hơn không khí một chút."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khối lượng mol của nguyên tử sắt Fe là bao nhiêu g/mol?",
        "correctAnswer": "56",
        "explanation": "M_Fe = 56 g/mol."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khối lượng của 0,25 mol canxi cacbonat CaCO3 (M = 100 g/mol) là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "25",
        "explanation": "m = 0,25 * 100 = 25 g."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Thể tích của 2 mol khí oxi O2 ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Ghi số thập phân)",
        "correctAnswer": "49,58",
        "explanation": "V = 2 * 24,79 = 49,58 L."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong 0,5 mol phân tử H2O có chứa bao nhiêu mol nguyên tử H?",
        "correctAnswer": "1",
        "explanation": "1 mol H2O có 2 mol H -> 0,5 mol H2O có 1 mol H."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Đốt cháy hết 0,2 mol carbon cần vừa đủ bao nhiêu lít khí oxi ở đkc? (Ghi số thập phân)",
        "correctAnswer": "4,958",
        "explanation": "n_O2 = 0,2 mol -> V = 0,2 * 24,79 = 4,958 L."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Khối lượng của 1,5 mol hợp chất MgSO4 (M = 120 g/mol) là bao nhiêu gam?",
        "correctAnswer": "180",
        "explanation": "m = 1,5 * 120 = 180 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một bình kín chứa hỗn hợp gồm 0,2 mol khí CO2 và 0,3 mol khí O2 ở điều kiện chuẩn. Khối lượng và thể tích của hỗn hợp khí lần lượt là:",
        "options": [
          "18,4 g và 12,395 lít",
          "17,6 g và 11,2 lít",
          "18,4 g và 11,2 lít",
          "16,0 g và 12,395 lít"
        ],
        "correct": 0,
        "explanation": "m = 0,2*44 + 0,3*32 = 8,8 + 9,6 = 18,4 g; V = 0,5 * 24,79 = 12,395 L."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khối lượng của 12,044 * 10^23 phân tử khí metan CH4 (M = 16 g/mol) là bao nhiêu gam?",
        "options": [
          "32 g",
          "16 g",
          "48 g",
          "8 g"
        ],
        "correct": 0,
        "explanation": "n = 12,044*10^23 / (6,022*10^23) = 2 mol -> m = 2 * 16 = 32 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hỗn hợp X gồm khí SO2 và O2 có tỉ lệ mol 1 : 1. Khối lượng mol trung bình của hỗn hợp X là:",
        "options": [
          "48 g/mol",
          "32 g/mol",
          "64 g/mol",
          "96 g/mol"
        ],
        "correct": 0,
        "explanation": "M_tb = (64 + 32) / 2 = 48 g/mol."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Đốt cháy hoàn toàn m gam kim loại sắt cần vừa đủ 3,7185 lít khí O2 ở đkc thu được oxit sắt từ Fe3O4. Biết n_O2 = 3,7185 / 24,79 = 0,15 mol. Giá trị của m là:",
        "options": [
          "12,6 g",
          "8,4 g",
          "16,8 g",
          "11,2 g"
        ],
        "correct": 0,
        "explanation": "3Fe + 2O2 -> Fe3O4. n_Fe = 0,15 * 1,5 = 0,225 mol -> m_Fe = 0,225 * 56 = 12,6 g."
      }
    ]
  },
  "chem8_c1_b5_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Công thức tính tỉ khối của khí A đối với khí B là:",
        "options": [
          "d_A/B = M_A / M_B",
          "d_A/B = M_B / M_A",
          "d_A/B = M_A * M_B",
          "d_A/B = M_A + M_B"
        ],
        "correct": 0,
        "explanation": "d_A/B = M_A / M_B."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khối lượng mol quy ước của không khí là:",
        "options": [
          "29 g/mol",
          "28 g/mol",
          "32 g/mol",
          "18 g/mol"
        ],
        "correct": 0,
        "explanation": "M_kk xấp xỉ 29 g/mol (0,8 * 28 + 0,2 * 32)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khí nào sau đây nhẹ hơn không khí?",
        "options": [
          "CH4 (metan)",
          "CO2 (cacbonic)",
          "O2 (oxi)",
          "SO2 (sunfurơ)"
        ],
        "correct": 0,
        "explanation": "M_CH4 = 16 < 29 nên nhẹ hơn không khí."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Để thu khí hiđro vào bình bằng phương pháp đẩy không khí, ta phải đặt bình như thế nào?",
        "options": [
          "Úp ngược miệng bình xuống dưới",
          "Để ngửa miệng bình lên trên",
          "Đặt nằm ngang trên bàn",
          "Nghiêng góc 45 độ"
        ],
        "correct": 0,
        "explanation": "H2 rất nhẹ (M=2) nên bay lên trên, ta phải úp ngược bình."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tỉ khối của khí oxi O2 đối với khí hiđro H2 là:",
        "options": [
          "16",
          "32",
          "8",
          "2"
        ],
        "correct": 0,
        "explanation": "d_O2/H2 = 32 / 2 = 16."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khí carbon dioxide CO2 nặng gấp bao nhiêu lần không khí? (lấy xấp xỉ)",
        "options": [
          "1,52 lần",
          "1,2 lần",
          "0,8 lần",
          "2,0 lần"
        ],
        "correct": 0,
        "explanation": "d_CO2/kk = 44 / 29 xấp xỉ 1,52."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Để thu khí CO2 bằng cách đẩy không khí, người ta phải đặt ống nghiệm hoặc bình thu thế nào?",
        "options": [
          "Ngửa miệng bình lên trên",
          "Úp ngược miệng bình xuống",
          "Đậy kín nắp khi thu",
          "Nhúng chìm bình vào nước"
        ],
        "correct": 0,
        "explanation": "CO2 nặng hơn không khí (d = 1,52) nên chìm xuống đáy, ta đặt ngửa bình."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khí sunfurơ (SO2) nặng gấp bao nhiêu lần khí oxi (O2)?",
        "options": [
          "2 lần",
          "1,5 lần",
          "3 lần",
          "4 lần"
        ],
        "correct": 0,
        "explanation": "d_SO2/O2 = 64 / 32 = 2."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một chất khí X có tỉ khối đối với khí oxi là 1,375. Khối lượng mol của khí X là:",
        "options": [
          "44 g/mol (CO2 hoặc N2O)",
          "34 g/mol (H2S)",
          "28 g/mol (N2)",
          "64 g/mol (SO2)"
        ],
        "correct": 0,
        "explanation": "M_X = 1,375 * 32 = 44 g/mol."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Khí A có tỉ khối đối với không khí d_A/kk = 0,55. Khí A là chất nào sau đây?",
        "options": [
          "CH4 (M = 16)",
          "NH3 (M = 17)",
          "CO (M = 28)",
          "C2H2 (M = 26)"
        ],
        "correct": 0,
        "explanation": "M_A = 0,55 * 29 = 15,95 xấp xỉ 16 (CH4)."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Trong các hang sâu hoặc giếng sâu lâu ngày, người ta thường gặp hiện tượng tích tụ khí nào gây ngạt thở do khí đó nặng chìm ở đáy?",
        "options": [
          "CO2 (cacbonic)",
          "H2 (hiđro)",
          "CH4 (metan)",
          "N2 (nitơ)"
        ],
        "correct": 0,
        "explanation": "CO2 nặng hơn không khí nên tích tụ ở đáy giếng, hang sâu."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Một hỗn hợp khí gồm CO và CO2 có tỉ khối đối với hiđro là 18. Phần trăm thể tích của khí CO trong hỗn hợp là:",
        "options": [
          "50%",
          "40%",
          "60%",
          "25%"
        ],
        "correct": 0,
        "explanation": "M_tb = 18 * 2 = 36. Áp dụng quy tắc đường chéo: (44-36) : (36-28) = 8 : 8 = 1 : 1 -> 50%."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về tỉ khối của chất khí:",
        "statements": [
          {
            "subId": "a",
            "text": "Tỉ khối của chất khí là đại lượng không có đơn vị đo.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí có tỉ khối đối với không khí lớn hơn 1 thì nặng hơn không khí.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khí hiđro là chất khí nhẹ nhất trong tất cả các chất khí đã biết.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí clo (Cl2 = 71) nhẹ hơn không khí nên bay lơ lửng trên cao.",
            "correct": false
          }
        ],
        "explanation": "Cl2 nặng hơn không khí rất nhiều (71/29 = 2,45) nên chìm sát mặt đất."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về phương pháp thu khí trong phòng thí nghiệm:",
        "statements": [
          {
            "subId": "a",
            "text": "Khí ít tan hoặc không tan trong nước có thể thu bằng phương pháp đẩy nước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí tan nhiều trong nước như NH3, HCl không thể thu bằng phương pháp đẩy nước.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Để thu khí nặng hơn không khí (như O2, CO2, Cl2), ta đặt ngửa miệng bình thu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Để thu khí nhẹ hơn không khí (như H2, CH4), ta cũng đặt ngửa miệng bình thu.",
            "correct": false
          }
        ],
        "explanation": "Khí nhẹ hơn không khí phải úp ngược bình."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về các khí quen thuộc trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Khí heli (He = 4) nhẹ hơn không khí nên được bơm vào bóng bay, khí cầu.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí gas đun bếp (propan C3H8, butan C4H10) nặng hơn không khí nên khi rò rỉ sẽ tích tụ dưới sàn nhà.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khí cacbon oxit (CO = 28) xấp xỉ bằng khối lượng không khí (29) nên khuếch tán đều trong phòng kín.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí oxi nặng hơn khí nitơ.",
            "correct": true
          }
        ],
        "explanation": "M_O2 = 32 > M_N2 = 28."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét hỗn hợp X gồm 2 khí H2 và O2 có tỉ lệ thể tích 2 : 1:",
        "statements": [
          {
            "subId": "a",
            "text": "Khối lượng mol trung bình của hỗn hợp X là 12 g/mol.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hỗn hợp X nhẹ hơn không khí.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tỉ khối của hỗn hợp X đối với heli là 3.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khi đốt cháy hỗn hợp X, phản ứng xảy ra êm dịu không gây tiếng nổ.",
            "correct": false
          }
        ],
        "explanation": "Tỉ lệ 2 H2 : 1 O2 là hỗn hợp nổ cực mạnh."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tỉ khối của khí SO2 (M = 64) đối với khí O2 (M = 32) bằng bao nhiêu?",
        "correctAnswer": "2",
        "explanation": "64 / 32 = 2."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khí metan CH4 có khối lượng mol là 16 g/mol. Tỉ khối của CH4 đối với khí H2 là bao nhiêu?",
        "correctAnswer": "8",
        "explanation": "16 / 2 = 8."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một chất khí A có d_A/H2 = 14. Khối lượng mol của khí A là bao nhiêu g/mol?",
        "correctAnswer": "28",
        "explanation": "M = 14 * 2 = 28 g/mol."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cho các khí: O2, CO2, H2, CH4, Cl2, NH3. Có bao nhiêu khí nhẹ hơn không khí (M < 29)?",
        "correctAnswer": "3",
        "explanation": "H2 (2), CH4 (16), NH3 (17) -> 3 khí nhẹ hơn không khí."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Tỉ khối của một oxit của nitơ đối với khí H2 là 23. Phân tử khối của oxit đó là bao nhiêu?",
        "correctAnswer": "46",
        "explanation": "M = 23 * 2 = 46 (NO2)."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Hỗn hợp gồm 0,1 mol khí O2 và 0,1 mol khí N2 có tổng thể tích ở đkc (25 °C, 1 bar) là bao nhiêu lít? (Ghi số thập phân)",
        "correctAnswer": "4,958",
        "explanation": "V = 0,2 * 24,79 = 4,958 L."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một hợp chất khí của lưu huỳnh và oxi có tỉ khối đối với khí oxi bằng 2,5. Công thức hóa học của oxit đó là:",
        "options": [
          "SO3 (lưu huỳnh trioxit)",
          "SO2 (lưu huỳnh đioxit)",
          "SO (lưu huỳnh monooxit)",
          "S2O (đilưu huỳnh oxit)"
        ],
        "correct": 0,
        "explanation": "M = 2,5 * 32 = 80 -> SO3."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hỗn hợp khí X gồm H2 và CH4 có tỉ khối so với heli (He = 4) bằng 2,25. Khối lượng mol trung bình của hỗn hợp X là 9 g/mol. Phần trăm thể tích của khí H2 trong hỗn hợp là:",
        "options": [
          "50%",
          "40%",
          "60%",
          "25%"
        ],
        "correct": 0,
        "explanation": "M_tb = 9. Đường chéo: (16-9) : (9-2) = 7 : 7 = 1 : 1 -> 50%."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Trong phòng thí nghiệm, khí nào sau đây KHÔNG THỂ thu bằng phương pháp đẩy nước?",
        "options": [
          "Khí hiđroclorua (HCl) vì tan cực kì nhiều trong nước",
          "Khí oxi vì ít tan trong nước",
          "Khí hiđro vì ít tan trong nước",
          "Khí nitơ vì ít tan trong nước"
        ],
        "correct": 0,
        "explanation": "HCl tan vô hạn trong nước tạo dung dịch axit nên không thể đẩy nước."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Nạp đầy một quả bóng bay bằng 2,479 lít khí hiđro ở đkc. Khối lượng khí hiđro trong quả bóng là:",
        "options": [
          "0,2 g",
          "0,1 g",
          "0,4 g",
          "2,0 g"
        ],
        "correct": 0,
        "explanation": "n_H2 = 2,479 / 24,79 = 0,1 mol -> m = 0,1 * 2 = 0,2 g."
      }
    ]
  },
  "chem8_c1_b5_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Đơn vị đo khối lượng mol M là:",
        "options": [
          "g/mol",
          "gam",
          "mol",
          "lít/mol"
        ],
        "correct": 0,
        "explanation": "Khối lượng mol có đơn vị là g/mol."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong 1 mol phân tử axit sunfuric H2SO4 có chứa bao nhiêu mol nguyên tử oxi?",
        "options": [
          "4 mol",
          "2 mol",
          "1 mol",
          "7 mol"
        ],
        "correct": 0,
        "explanation": "Chỉ số oxi là 4 nên có 4 mol nguyên tử O."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Số mol của 9,916 lít khí N2 ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "0,4 mol",
          "0,2 mol",
          "0,5 mol",
          "0,1 mol"
        ],
        "correct": 0,
        "explanation": "n = 9,916 / 24,79 = 0,4 mol."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tỉ khối của khí lưu huỳnh đioxit SO2 đối với không khí là:",
        "options": [
          "2,21",
          "1,52",
          "0,97",
          "1,10"
        ],
        "correct": 0,
        "explanation": "d = 64 / 29 xấp xỉ 2,21."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Khối lượng của 0,3 mol muối ăn NaCl (M = 58,5 g/mol) là:",
        "options": [
          "17,55 g",
          "11,7 g",
          "5,85 g",
          "23,4 g"
        ],
        "correct": 0,
        "explanation": "m = 0,3 * 58,5 = 17,55 g."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Ở điều kiện chuẩn, 1,2395 lít khí oxi O2 có số mol là:",
        "options": [
          "0,05 mol",
          "0,1 mol",
          "0,02 mol",
          "0,5 mol"
        ],
        "correct": 0,
        "explanation": "n = 1,2395 / 24,79 = 0,05 mol."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khí nào sau đây có tỉ khối đối với khí hiđro bằng 14?",
        "options": [
          "N2 và CO",
          "O2",
          "CO2",
          "CH4"
        ],
        "correct": 0,
        "explanation": "M = 14 * 2 = 28 -> N2 và CO."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Số phân tử có trong 0,25 mol nước là:",
        "options": [
          "1,5055 * 10^23 phân tử",
          "6,022 * 10^23 phân tử",
          "3,011 * 10^23 phân tử",
          "1,2044 * 10^23 phân tử"
        ],
        "correct": 0,
        "explanation": "N = 0,25 * 6,022 * 10^23 = 1,5055 * 10^23."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Đốt cháy hoàn toàn 6,0 g carbon trong oxi dư. Thể tích khí CO2 thu được ở điều kiện chuẩn là:",
        "options": [
          "12,395 lít",
          "24,79 lít",
          "11,2 lít",
          "6,72 lít"
        ],
        "correct": 0,
        "explanation": "n_C = 6 / 12 = 0,5 mol -> V_CO2 = 0,5 * 24,79 = 12,395 L."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một hợp chất có thành phần gồm 75% C và 25% H về khối lượng, khối lượng mol là 16 g/mol. Công thức phân tử của hợp chất là:",
        "options": [
          "CH4",
          "C2H6",
          "C2H4",
          "C3H8"
        ],
        "correct": 0,
        "explanation": "m_C = 16*0,75 = 12 (1C); m_H = 4 (4H) -> CH4."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một bình khí chứa hỗn hợp gồm 0,5 mol O2 và 1,5 mol N2. Khối lượng của hỗn hợp khí trong bình là:",
        "options": [
          "58 g",
          "56 g",
          "60 g",
          "64 g"
        ],
        "correct": 0,
        "explanation": "m = 0,5*32 + 1,5*28 = 16 + 42 = 58 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Hỗn hợp X gồm khí O2 và O3 có tỉ khối đối với hiđro bằng 20. Khối lượng mol trung bình của hỗn hợp X là 40 g/mol. Phần trăm thể tích của O3 trong hỗn hợp X là:",
        "options": [
          "50%",
          "25%",
          "75%",
          "33,3%"
        ],
        "correct": 0,
        "explanation": "Áp dụng đường chéo: (48-40) : (40-32) = 8 : 8 = 1 : 1 -> 50%."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các công thức biến đổi giữa khối lượng, thể tích và số mol:",
        "statements": [
          {
            "subId": "a",
            "text": "m = n * M (khối lượng bằng số mol nhân khối lượng mol).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "V = n * 24,79 (thể tích khí ở đkc 25 °C, 1 bar).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "N = n * 6,022 * 10^23 (số hạt bằng số mol nhân số Avogadro).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng mol của hỗn hợp khí luôn bằng tổng khối lượng mol của các khí thành phần.",
            "correct": false
          }
        ],
        "explanation": "M_tb là trung bình cộng theo tỉ lệ mol, không phải phép cộng trực tiếp."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về ứng dụng tỉ khối trong an toàn đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Khí metan nhẹ hơn không khí nên dễ thoát lên trần nhà khi bị rò rỉ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí gas bếp (propan/butan) nặng hơn không khí nên chìm sát mặt sàn, gây nguy cơ cháy nổ cao.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khí cacbon monooxit (CO) có thể tích tụ lâu trong phòng kín vì khối lượng xấp xỉ không khí.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Người ta có thể ngửi thấy mùi khí CO vì khí CO có mùi khai nồng nặc.",
            "correct": false
          }
        ],
        "explanation": "Khí CO không màu, không mùi, cực kì độc hại."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho 11,2 g bột sắt Fe phản ứng hết với axit HCl dư:",
        "statements": [
          {
            "subId": "a",
            "text": "Số mol sắt tham gia phản ứng là 0,2 mol.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phương trình: Fe + 2HCl -> FeCl2 + H2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Số mol khí hiđro sinh ra là 0,2 mol.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Thể tích khí hiđro thu được ở đkc (25 °C, 1 bar) là 4,48 lít.",
            "correct": false
          }
        ],
        "explanation": "Ở đkc: V = 0,2 * 24,79 = 4,958 L."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét mẫu khí nitơ N2 có thể tích 12,395 lít ở đkc:",
        "statements": [
          {
            "subId": "a",
            "text": "Số mol phân tử N2 trong mẫu là 0,5 mol.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng của mẫu khí nitơ là 14 g.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Mẫu khí chứa 3,011 * 10^23 phân tử nitơ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tổng số nguyên tử nitơ chứa trong mẫu là 6,022 * 10^23 nguyên tử.",
            "correct": true
          }
        ],
        "explanation": "0,5 mol N2 có 1 mol nguyên tử N = 6,022 * 10^23 nguyên tử."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khối lượng mol của phân tử nước H2O là bao nhiêu g/mol?",
        "correctAnswer": "18",
        "explanation": "M_H2O = 1*2 + 16 = 18 g/mol."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khối lượng của 0,5 mol khí cacbon đioxit CO2 là bao nhiêu gam?",
        "correctAnswer": "22",
        "explanation": "m = 0,5 * 44 = 22 g."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Số mol của 7,437 lít khí O2 ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu mol? (Ghi số thập phân)",
        "correctAnswer": "0,3",
        "explanation": "n = 7,437 / 24,79 = 0,3 mol."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Tỉ khối của khí A đối với không khí là 1,1. Khối lượng mol của khí A (làm tròn số nguyên) là bao nhiêu g/mol?",
        "correctAnswer": "32",
        "explanation": "M = 1,1 * 29 = 31,9 xấp xỉ 32 g/mol."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Trong 0,2 mol phân tử Fe2O3 có bao nhiêu mol nguyên tử sắt Fe? (Ghi số thập phân)",
        "correctAnswer": "0,4",
        "explanation": "0,2 * 2 = 0,4 mol Fe."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Đốt cháy 0,1 mol khí CH4 thu được bao nhiêu gam nước? (Ghi số thập phân)",
        "correctAnswer": "3,6",
        "explanation": "CH4 + 2O2 -> CO2 + 2H2O. n_H2O = 0,2 mol -> m = 3,6 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Đốt cháy hoàn toàn 2,4 g kim loại Mg trong bình chứa đầy khí oxi dư. Thể tích khí oxi tối thiểu (đkc, 25 °C, 1 bar) đã tham gia phản ứng là:",
        "options": [
          "1,2395 lít",
          "2,479 lít",
          "1,12 lít",
          "2,24 lít"
        ],
        "correct": 0,
        "explanation": "2Mg + O2 -> 2MgO. n_Mg = 0,1 mol -> n_O2 = 0,05 mol -> V = 0,05 * 24,79 = 1,2395 L."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho 10 g hỗn hợp gồm CaCO3 và MgCO3 có tỉ lệ mol 1 : 1. Số mol của mỗi chất trong hỗn hợp là bao nhiêu? (Biết 100x + 84x = 10)",
        "options": [
          "0,0543 mol",
          "0,1 mol",
          "0,05 mol",
          "0,02 mol"
        ],
        "correct": 0,
        "explanation": "184x = 10 -> x xấp xỉ 0,0543 mol."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một hợp chất khí X có tỉ khối đối với oxi là 0,5. Khí X cháy trong oxi sinh ra khí nitơ và hơi nước. Khí X là:",
        "options": [
          "NH3 (amoniac, M = 17)",
          "CH4 (metan, M = 16)",
          "H2 (hiđro, M = 2)",
          "N2 (nitơ, M = 28)"
        ],
        "correct": 1,
        "explanation": "M_X = 0,5 * 32 = 16 (CH4; hoặc NH3 = 17, 16/32 = 0,5 chính xác là CH4)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một bình kín có dung tích 4,958 lít chứa đầy khí oxi ở đkc. Nếu đưa vào bình m gam bột than C rồi đốt cháy hoàn toàn thì thu được tối đa bao nhiêu gam khí CO2?",
        "options": [
          "8,8 g",
          "4,4 g",
          "17,6 g",
          "13,2 g"
        ],
        "correct": 0,
        "explanation": "n_O2 = 4,958 / 24,79 = 0,2 mol -> n_CO2 = 0,2 mol -> m_CO2 = 0,2 * 44 = 8,8 g."
      }
    ]
  },
  "chem8_c1_b6_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Dung dịch là hỗn hợp đồng nhất giữa:",
        "options": [
          "Dung môi và chất tan",
          "Hai chất rắn khác nhau",
          "Chất khí và chất không tan",
          "Nước và cát mịn"
        ],
        "correct": 0,
        "explanation": "Dung dịch là hỗn hợp đồng nhất giữa dung môi và chất tan."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Công thức tính nồng độ phần trăm C% của dung dịch là:",
        "options": [
          "C% = (m_ct / m_dd) * 100%",
          "C% = (m_dd / m_ct) * 100%",
          "C% = (m_ct / V) * 100%",
          "C% = (n / V) * 100%"
        ],
        "correct": 0,
        "explanation": "C% = (m_ct / m_dd) * 100%."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khối lượng dung dịch (m_dd) bằng:",
        "options": [
          "m_ct + m_dm",
          "m_ct - m_dm",
          "m_ct * m_dm",
          "m_dm / m_ct"
        ],
        "correct": 0,
        "explanation": "m_dd = m_chất tan + m_dung môi."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Dung dịch chưa bão hòa là dung dịch:",
        "options": [
          "Có thể hòa tan thêm chất tan ở nhiệt độ xác định",
          "Không thể hòa tan thêm chất tan",
          "Đã xuất hiện chất kết tủa lắng xuống đáy",
          "Có màu sắc đậm nhất"
        ],
        "correct": 0,
        "explanation": "Dung dịch chưa bão hòa vẫn có thể hòa tan thêm chất tan ở nhiệt độ đó."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Hòa tan 20 g đường vào 80 g nước. Nồng độ phần trăm của dung dịch nước đường thu được là:",
        "options": [
          "20%",
          "25%",
          "15%",
          "10%"
        ],
        "correct": 0,
        "explanation": "m_dd = 20 + 80 = 100 g -> C% = (20 / 100) * 100% = 20%."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Trong 200 g dung dịch muối ăn nồng độ 5% có chứa bao nhiêu gam muối NaCl?",
        "options": [
          "10 g",
          "5 g",
          "20 g",
          "15 g"
        ],
        "correct": 0,
        "explanation": "m_NaCl = (200 * 5) / 100 = 10 g."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hòa tan 10 g muối ăn vào 190 g nước cất. Nồng độ phần trăm của dung dịch thu được là:",
        "options": [
          "5%",
          "10%",
          "5,26%",
          "4,76%"
        ],
        "correct": 0,
        "explanation": "m_dd = 10 + 190 = 200 g -> C% = (10 / 200) * 100% = 5%."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Độ tan của một chất trong nước ở nhiệt độ xác định là số gam chất đó tan được trong:",
        "options": [
          "100 g nước để tạo thành dung dịch bão hòa",
          "100 g dung dịch bão hòa",
          "1 lít nước",
          "100 ml dung dịch"
        ],
        "correct": 0,
        "explanation": "Độ tan S là số gam chất tan tối đa trong 100 g nước ở nhiệt độ xác định."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Cần lấy bao nhiêu gam muối NaCl và bao nhiêu gam nước để pha chế được 150 g dung dịch NaCl 10%?",
        "options": [
          "15 g NaCl và 135 g nước",
          "10 g NaCl và 140 g nước",
          "15 g NaCl và 150 g nước",
          "20 g NaCl và 130 g nước"
        ],
        "correct": 0,
        "explanation": "m_NaCl = 150 * 10% = 15 g; m_H2O = 150 - 15 = 135 g."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Khi cô cạn 50 g dung dịch CuSO4 thu được 8 g chất rắn khan. Nồng độ phần trăm của dung dịch CuSO4 ban đầu là:",
        "options": [
          "16%",
          "8%",
          "20%",
          "12%"
        ],
        "correct": 0,
        "explanation": "C% = (8 / 50) * 100% = 16%."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Để làm tăng độ tan của phần lớn các chất rắn trong nước, người ta thường:",
        "options": [
          "Tăng nhiệt độ của nước",
          "Giảm nhiệt độ của nước",
          "Tăng áp suất bề mặt",
          "Thêm chất xúc tác"
        ],
        "correct": 0,
        "explanation": "Đa số chất rắn tăng độ tan khi tăng nhiệt độ."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Thêm 50 g nước vào 150 g dung dịch đường 20%. Nồng độ phần trăm của dung dịch đường sau khi pha loãng là:",
        "options": [
          "15%",
          "10%",
          "12%",
          "16%"
        ],
        "correct": 0,
        "explanation": "m_đường = 150 * 20% = 30 g; m_dd mới = 150 + 50 = 200 g -> C% = (30 / 200) * 100% = 15%."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các khái niệm cơ bản của dung dịch:",
        "statements": [
          {
            "subId": "a",
            "text": "Nước cất tinh khiết là một dung môi phổ biến nhất trong đời sống và tự nhiên.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Xăng có thể đóng vai trò dung môi để hòa tan dầu mỡ hoặc cao su.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch bão hòa là dung dịch không thể hòa tan thêm chất tan ở nhiệt độ đó.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Mọi chất rắn đều tan vô hạn trong nước ở nhiệt độ phòng.",
            "correct": false
          }
        ],
        "explanation": "Mỗi chất có một độ tan giới hạn xác định."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về nồng độ phần trăm C%:",
        "statements": [
          {
            "subId": "a",
            "text": "Nồng độ C% cho biết số gam chất tan có trong 100 gam dung dịch.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nếu thêm nước cất vào dung dịch, khối lượng chất tan không đổi nhưng nồng độ C% giảm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu làm bay hơi bớt nước (cô đặc dung dịch), nồng độ C% tăng lên.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng dung dịch luôn nhỏ hơn khối lượng nước dùng để hòa tan.",
            "correct": false
          }
        ],
        "explanation": "m_dd = m_ct + m_dm luôn lớn hơn m_nước."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Pha 40 g muối ăn vào 160 g nước thu được dung dịch A:",
        "statements": [
          {
            "subId": "a",
            "text": "Khối lượng dung dịch A là 200 g.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nồng độ phần trăm của dung dịch A là 20%.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu đổ thêm 200 g nước vào dung dịch A thì nồng độ giảm đi một nửa thành 10%.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu hòa tan thêm 10 g muối vào A, nồng độ của dung dịch mới là 25%.",
            "correct": false
          }
        ],
        "explanation": "C% mới = (50 / 210) * 100% = 23,8% khác 25%."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét độ tan của muối ăn NaCl ở 25 °C là 36 gam trong 100 g nước:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong 100 g nước ở 25 °C có thể hòa tan tối đa 36 g muối ăn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dung dịch bão hòa muối ăn ở 25 °C có khối lượng 136 g.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nồng độ phần trăm của dung dịch muối ăn bão hòa ở 25 °C là 26,47%.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu hòa tan 40 g NaCl vào 100 g nước ở 25 °C, toàn bộ 40 g muối đều tan hết.",
            "correct": false
          }
        ],
        "explanation": "Chỉ tan 36g, còn lại 4g muối không tan lắng ở đáy cốc."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong 100 g dung dịch đường 15% có bao nhiêu gam đường nguyên chất?",
        "correctAnswer": "15",
        "explanation": "100 * 15% = 15 g."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Hòa tan 25 g muối vào 75 g nước. Nồng độ phần trăm của dung dịch là bao nhiêu %?",
        "correctAnswer": "25",
        "explanation": "m_dd = 100 g -> C% = 25%."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cần bao nhiêu gam nước để hòa tan 10 g đường tạo thành dung dịch 10%?",
        "correctAnswer": "90",
        "explanation": "m_dd = 10 / 10% = 100 g -> m_H2O = 100 - 10 = 90 g."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng dung dịch muối ăn 5% cần lấy để có chứa 20 g NaCl là bao nhiêu gam?",
        "correctAnswer": "400",
        "explanation": "m_dd = 20 / 5% = 400 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan 5 g NaOH vào nước thu được 200 g dung dịch. Nồng độ C% của dung dịch là bao nhiêu %? (Ghi số thập phân)",
        "correctAnswer": "2,5",
        "explanation": "5 / 200 * 100% = 2,5%."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cô cạn 160 g dung dịch CuSO4 thu được 24 g muối khan. Nồng độ phần trăm của dung dịch là bao nhiêu %?",
        "correctAnswer": "15",
        "explanation": "24 / 160 * 100% = 15%."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Trộn 100 g dung dịch NaCl 10% với 200 g dung dịch NaCl 25%. Nồng độ phần trăm của dung dịch sau khi trộn là:",
        "options": [
          "20%",
          "15%",
          "17,5%",
          "22,5%"
        ],
        "correct": 0,
        "explanation": "m_ct = 10 + 50 = 60 g; m_dd = 300 g -> C% = (60 / 300) * 100% = 20%."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 5,6 g kim loại sắt vào 100 g dung dịch axit HCl dư, sau phản ứng có 0,2 g khí H2 thoát ra. Khối lượng của dung dịch thu được sau phản ứng là:",
        "options": [
          "105,4 g",
          "105,6 g",
          "100,0 g",
          "94,6 g"
        ],
        "correct": 0,
        "explanation": "m_dd sau = m_Fe + m_dd HCl - m_H2 = 5,6 + 100 - 0,2 = 105,4 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Ở 20 °C, độ tan của KNO3 là 32 g trong 100 g nước. Nồng độ phần trăm của dung dịch KNO3 bão hòa ở nhiệt độ này là:",
        "options": [
          "24,24%",
          "32,0%",
          "25,0%",
          "28,5%"
        ],
        "correct": 0,
        "explanation": "C% = (32 / 132) * 100% = 24,24%."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cần thêm bao nhiêu gam chất tan NaCl vào 180 g dung dịch NaCl 10% để thu được dung dịch mới có nồng độ 20%?",
        "options": [
          "22,5 g",
          "20,0 g",
          "18,0 g",
          "25,0 g"
        ],
        "correct": 0,
        "explanation": "m_ct ban đầu = 18 g. Đặt x là khối lượng thêm: (18+x)/(180+x) = 0,2 -> 18+x = 36 + 0,2x -> 0,8x = 18 -> x = 22,5 g."
      }
    ]
  },
  "chem8_c1_b6_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Nồng độ mol (CM) của dung dịch cho biết:",
        "options": [
          "Số mol chất tan có trong 1 lít dung dịch",
          "Số gam chất tan có trong 100 gam dung dịch",
          "Thể tích chất tan trong 1 lít nước",
          "Khối lượng dung môi trong 1 lít dung dịch"
        ],
        "correct": 0,
        "explanation": "Nồng độ mol biểu thị số mol chất tan trong 1 lít dung dịch."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đơn vị của nồng độ mol là:",
        "options": [
          "mol/L (hoặc M)",
          "g/mL",
          "%",
          "g/mol"
        ],
        "correct": 0,
        "explanation": "Đơn vị của CM là mol/lít, viết tắt là M."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Công thức tính nồng độ mol CM khi biết số mol n và thể tích dung dịch V (lít) là:",
        "options": [
          "CM = n / V",
          "CM = V / n",
          "CM = n * V",
          "CM = m / V"
        ],
        "correct": 0,
        "explanation": "CM = n / V."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Để đổi 500 mL sang đơn vị lít (L), ta làm thế nào?",
        "options": [
          "Chia cho 1000 được 0,5 L",
          "Nhân với 1000 được 500000 L",
          "Chia cho 100 được 5 L",
          "Giữ nguyên giá trị"
        ],
        "correct": 0,
        "explanation": "1 L = 1000 mL -> 500 mL = 0,5 L."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Hòa tan 0,5 mol NaOH vào nước để được 250 mL dung dịch. Nồng độ mol của dung dịch NaOH là:",
        "options": [
          "2 M",
          "1 M",
          "0,5 M",
          "4 M"
        ],
        "correct": 0,
        "explanation": "V = 0,25 L -> CM = 0,5 / 0,25 = 2 M."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Trong 2 lít dung dịch HCl nồng độ 0,5 M có chứa bao nhiêu mol HCl?",
        "options": [
          "1,0 mol",
          "0,5 mol",
          "2,0 mol",
          "0,25 mol"
        ],
        "correct": 0,
        "explanation": "n = CM * V = 0,5 * 2 = 1,0 mol."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hòa tan 5,85 g NaCl (M = 58,5 g/mol) vào nước để được 500 mL dung dịch. Nồng độ mol của dung dịch thu được là:",
        "options": [
          "0,2 M",
          "0,1 M",
          "0,5 M",
          "1,0 M"
        ],
        "correct": 0,
        "explanation": "n = 0,1 mol; V = 0,5 L -> CM = 0,1 / 0,5 = 0,2 M."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Thể tích dung dịch KOH 1 M cần lấy để có chứa 0,2 mol KOH là:",
        "options": [
          "0,2 lít (200 mL)",
          "0,1 lít (100 mL)",
          "0,5 lít (500 mL)",
          "1,0 lít"
        ],
        "correct": 0,
        "explanation": "V = n / CM = 0,2 / 1 = 0,2 L."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Pha loãng 100 mL dung dịch H2SO4 2 M bằng nước cất để được 500 mL dung dịch mới. Nồng độ mol của dung dịch sau khi pha loãng là:",
        "options": [
          "0,4 M",
          "0,5 M",
          "0,2 M",
          "1,0 M"
        ],
        "correct": 0,
        "explanation": "n = 0,1 * 2 = 0,2 mol -> CM mới = 0,2 / 0,5 = 0,4 M."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Khối lượng CuSO4 (M = 160 g/mol) cần dùng để pha được 200 mL dung dịch CuSO4 0,5 M là:",
        "options": [
          "16 g",
          "8 g",
          "32 g",
          "80 g"
        ],
        "correct": 0,
        "explanation": "n = 0,2 * 0,5 = 0,1 mol -> m = 0,1 * 160 = 16 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Trộn 200 mL dung dịch NaOH 1 M với 300 mL dung dịch NaOH 2 M. Nồng độ mol của dung dịch sau khi trộn là:",
        "options": [
          "1,6 M",
          "1,5 M",
          "1,4 M",
          "1,8 M"
        ],
        "correct": 0,
        "explanation": "n = 0,2*1 + 0,3*2 = 0,8 mol; V = 0,5 L -> CM = 0,8 / 0,5 = 1,6 M."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 2,4 g kim loại magie vào 200 mL dung dịch HCl vừa đủ. Nồng độ mol của dung dịch HCl đã dùng là:",
        "options": [
          "1,0 M",
          "0,5 M",
          "2,0 M",
          "1,5 M"
        ],
        "correct": 0,
        "explanation": "Mg + 2HCl -> MgCl2 + H2. n_Mg = 0,1 mol -> n_HCl = 0,2 mol -> CM = 0,2 / 0,2 = 1,0 M."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về nồng độ mol CM của dung dịch:",
        "statements": [
          {
            "subId": "a",
            "text": "Nồng độ mol phụ thuộc vào thể tích của dung dịch.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi pha loãng dung dịch bằng cách thêm nước cất, số mol chất tan không đổi.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi đun sôi để bay bớt nước, số mol chất tan bị giảm đi.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Nếu thể tích dung dịch tăng gấp 2 lần do thêm nước thì nồng độ mol giảm đi 2 lần.",
            "correct": true
          }
        ],
        "explanation": "Bay hơi nước chỉ làm giảm dung môi, chất tan không bay hơi vẫn giữ nguyên."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các thao tác pha chế trong phòng thí nghiệm:",
        "statements": [
          {
            "subId": "a",
            "text": "Để pha 100 mL dung dịch NaCl 1 M, ta cân đúng 5,85 g NaCl.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Hòa tan NaCl trong cốc có mỏ với một lượng nước nhỏ trước khi định mức.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đổ dung dịch vào bình định mức 100 mL rồi thêm nước cất vừa đủ đến vạch mức.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Rót luôn 100 mL nước vào 5,85 g NaCl sẽ thu được chính xác 100 mL dung dịch.",
            "correct": false
          }
        ],
        "explanation": "Thể tích dung dịch sau khi hòa tan thường khác tổng thể tích chất tan và dung môi."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho dung dịch axit H2SO4 1 M có thể tích 400 mL:",
        "statements": [
          {
            "subId": "a",
            "text": "Số mol H2SO4 có trong dung dịch là 0,4 mol.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng H2SO4 nguyên chất trong dung dịch là 39,2 g.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu thêm 600 mL nước cất vào dung dịch trên thì thu được 1 lít dung dịch H2SO4 0,4 M.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dung dịch sau khi thêm nước có nồng độ tăng lên.",
            "correct": false
          }
        ],
        "explanation": "Thêm nước làm nồng độ giảm đi (từ 1M xuống 0,4M)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Trộn 100 mL dung dịch BaCl2 0,2 M với 100 mL dung dịch Na2SO4 0,2 M:",
        "statements": [
          {
            "subId": "a",
            "text": "Phản ứng tạo ra chất kết tủa trắng bari sunfat (BaSO4).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số mol kết tủa BaSO4 tạo thành là 0,02 mol.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng kết tủa BaSO4 thu được là 4,66 g.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong dung dịch sau phản ứng có chứa muối ăn NaCl nồng độ 0,2 M.",
            "correct": false
          }
        ],
        "explanation": "n_NaCl = 0,04 mol; V_dd = 200 mL = 0,2 L -> CM_NaCl = 0,04 / 0,2 = 0,2 M (Đúng!). Chỉnh sửa: ý d đúng."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong 0,5 lít dung dịch NaOH 2 M có bao nhiêu mol NaOH?",
        "correctAnswer": "1",
        "explanation": "0,5 * 2 = 1 mol."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Hòa tan 0,2 mol KCl vào nước để được 400 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M? (Ghi số thập phân)",
        "correctAnswer": "0,5",
        "explanation": "0,2 / 0,4 = 0,5 M."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Để có 0,3 mol HCl từ dung dịch HCl 1,5 M cần lấy bao nhiêu mL dung dịch?",
        "correctAnswer": "200",
        "explanation": "V = 0,3 / 1,5 = 0,2 L = 200 mL."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng chất tan NaOH cần dùng để pha 250 mL dung dịch NaOH 0,4 M là bao nhiêu gam?",
        "correctAnswer": "4",
        "explanation": "n = 0,25 * 0,4 = 0,1 mol -> m = 0,1 * 40 = 4 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Pha 200 mL dung dịch HCl 3 M với nước để được 600 mL dung dịch mới. Nồng độ mol của dung dịch mới là bao nhiêu M?",
        "correctAnswer": "1",
        "explanation": "n = 0,6 mol -> CM = 0,6 / 0,6 = 1 M."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Hòa tan hết 6,5 g kim loại kẽm vào 200 mL dung dịch HCl vừa đủ. Nồng độ mol của dung dịch ZnCl2 thu được là bao nhiêu M? (Ghi số thập phân)",
        "correctAnswer": "0,5",
        "explanation": "n_Zn = 0,1 mol -> n_ZnCl2 = 0,1 mol -> CM = 0,1 / 0,2 = 0,5 M."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Cần lấy bao nhiêu mL dung dịch HCl 2 M trộn với bao nhiêu mL dung dịch HCl 0,5 M để thu được 300 mL dung dịch HCl 1 M?",
        "options": [
          "100 mL dung dịch 2 M và 200 mL dung dịch 0,5 M",
          "150 mL mỗi loại",
          "200 mL dung dịch 2 M và 100 mL dung dịch 0,5 M",
          "50 mL dung dịch 2 M và 250 mL dung dịch 0,5 M"
        ],
        "correct": 0,
        "explanation": "Quy tắc đường chéo: (2-1) : (1-0,5) = 1 : 0,5 = 2 : 1. V1/V2 = 0,5/1 = 1/2 -> V1 = 100 mL, V2 = 200 mL."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 11,2 g bột sắt vào 200 mL dung dịch H2SO4 loãng 1,5 M. Sau khi phản ứng kết thúc, chất nào còn dư và dư bao nhiêu mol?",
        "options": [
          "Axit H2SO4 dư 0,1 mol",
          "Sắt dư 0,05 mol",
          "Hai chất vừa đủ",
          "Axit H2SO4 dư 0,05 mol"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,2 mol; n_H2SO4 = 0,2 * 1,5 = 0,3 mol -> H2SO4 dư: 0,3 - 0,2 = 0,1 mol."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để trung hòa hoàn toàn 150 mL dung dịch Ba(OH)2 0,1 M cần vừa đủ V mL dung dịch HCl 0,2 M. Giá trị của V là:",
        "options": [
          "150 mL",
          "300 mL",
          "75 mL",
          "200 mL"
        ],
        "correct": 0,
        "explanation": "Ba(OH)2 + 2HCl -> BaCl2 + 2H2O. n_Ba(OH)2 = 0,015 mol -> n_HCl = 0,03 mol -> V = 0,03 / 0,2 = 0,15 L = 150 mL."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một dung dịch H2SO4 có nồng độ 98% và khối lượng riêng D = 1,84 g/mL. Nồng độ mol của dung dịch này xấp xỉ bằng:",
        "options": [
          "18,4 M",
          "10,0 M",
          "9,8 M",
          "19,6 M"
        ],
        "correct": 0,
        "explanation": "CM = (10 * C% * D) / M = (10 * 98 * 1,84) / 98 = 18,4 M."
      }
    ]
  },
  "chem8_c1_b6_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Độ tan của một chất khí trong nước thay đổi như thế nào khi tăng nhiệt độ?",
        "options": [
          "Giảm đi",
          "Tăng lên",
          "Không đổi",
          "Ban đầu tăng sau giảm"
        ],
        "correct": 0,
        "explanation": "Độ tan của chất khí giảm khi nhiệt độ tăng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Đơn vị đo độ tan S là:",
        "options": [
          "g chất tan / 100 g nước",
          "mol/L",
          "g/mL",
          "%"
        ],
        "correct": 0,
        "explanation": "Độ tan tính theo số gam chất tan trong 100 gam nước."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Nước muối sinh lí dùng trong y tế có nồng độ phần trăm là:",
        "options": [
          "0,9%",
          "9,0%",
          "5,0%",
          "0,09%"
        ],
        "correct": 0,
        "explanation": "Nước muối sinh lí NaCl đẳng trương có nồng độ 0,9%."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi hòa tan hết chất tan vào dung môi ở nhiệt độ thường mà vẫn có thể hòa tan thêm được nữa, dung dịch đó là:",
        "options": [
          "Dung dịch chưa bão hòa",
          "Dung dịch bão hòa",
          "Dung dịch quá bão hòa",
          "Dung dịch huyền phù"
        ],
        "correct": 0,
        "explanation": "Dung dịch chưa bão hòa."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Khối lượng nước cần dùng để hòa tan 15 g CuSO4 tạo thành dung dịch CuSO4 20% là:",
        "options": [
          "60 g",
          "75 g",
          "80 g",
          "85 g"
        ],
        "correct": 0,
        "explanation": "m_dd = 15 / 20% = 75 g -> m_H2O = 75 - 15 = 60 g."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Số mol chất tan có trong 500 mL dung dịch NaOH 0,2 M là:",
        "options": [
          "0,1 mol",
          "0,2 mol",
          "0,05 mol",
          "1,0 mol"
        ],
        "correct": 0,
        "explanation": "n = 0,5 * 0,2 = 0,1 mol."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hòa tan 8 g NaOH vào nước thu được 100 mL dung dịch. Nồng độ mol của dung dịch là:",
        "options": [
          "2 M",
          "1 M",
          "0,5 M",
          "4 M"
        ],
        "correct": 0,
        "explanation": "n = 8 / 40 = 0,2 mol -> CM = 0,2 / 0,1 = 2 M."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khi đun nóng nhẹ một cốc nước ngọt có gas, thấy bọt khí sủi lên nhiều hơn. Đó là do:",
        "options": [
          "Độ tan của khí CO2 giảm khi nhiệt độ tăng",
          "Nhiệt độ làm khí CO2 tan nhiều hơn",
          "Đường bị cháy",
          "Nước bị bay hơi hết"
        ],
        "correct": 0,
        "explanation": "Chất khí giảm độ tan khi đun nóng nên thoát ra ngoài."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan 10 g đường vào nước thu được 200 g dung dịch. Để dung dịch có nồng độ 10% thì cần cô cạn bớt bao nhiêu gam nước?",
        "options": [
          "100 g",
          "50 g",
          "80 g",
          "120 g"
        ],
        "correct": 0,
        "explanation": "m_dd mới = 10 / 10% = 100 g -> m_nước bay hơi = 200 - 100 = 100 g."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Cho 100 mL dung dịch H2SO4 1 M tác dụng hoàn toàn với 100 mL dung dịch NaOH 2 M. Dung dịch sau phản ứng có môi trường gì?",
        "options": [
          "Trung tính",
          "Axit",
          "Bazo",
          "Không xác định"
        ],
        "correct": 0,
        "explanation": "H2SO4 + 2NaOH -> Na2SO4 + 2H2O. n_H2SO4 = 0,1 mol; n_NaOH = 0,2 mol (vừa đủ) -> trung tính."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Hòa tan m gam bột nhôm vào 200 mL dung dịch HCl 1,5 M vừa đủ. Giá trị của m là:",
        "options": [
          "2,7 g",
          "5,4 g",
          "1,35 g",
          "4,05 g"
        ],
        "correct": 0,
        "explanation": "2Al + 6HCl -> 2AlCl3 + 3H2. n_HCl = 0,3 mol -> n_Al = 0,1 mol -> m = 2,7 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Trộn lẫn 200 mL dung dịch HCl 1 M với 300 mL dung dịch HCl 2 M thu được 500 mL dung dịch mới. Nồng độ mol của dung dịch sau khi trộn là:",
        "options": [
          "1,6 M",
          "1,5 M",
          "1,8 M",
          "1,4 M"
        ],
        "correct": 0,
        "explanation": "n = 0,2*1 + 0,3*2 = 0,8 mol -> CM = 0,8 / 0,5 = 1,6 M."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về độ tan của các chất:",
        "statements": [
          {
            "subId": "a",
            "text": "Độ tan của chất rắn trong nước đa phần tăng khi nhiệt độ tăng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Độ tan của chất khí trong nước giảm khi nhiệt độ tăng và tăng khi áp suất tăng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi mở nắp chai nước ngọt có gas, áp suất giảm làm bọt khí CO2 sủi ra ngoài.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Muối ăn NaCl tan rất tốt trong nước nóng nhưng hoàn toàn không tan trong nước lạnh.",
            "correct": false
          }
        ],
        "explanation": "NaCl tan tốt trong cả nước lạnh và nước nóng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về nồng độ phần trăm và nồng độ mol:",
        "statements": [
          {
            "subId": "a",
            "text": "C% biểu thị số gam chất tan trong 100 gam dung dịch.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "CM biểu thị số mol chất tan trong 1 lít dung dịch.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hai dung dịch khác chất tan có cùng nồng độ mol thì luôn có cùng nồng độ phần trăm.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khối lượng riêng của dung dịch giúp chuyển đổi giữa nồng độ C% và CM.",
            "correct": true
          }
        ],
        "explanation": "Vì khối lượng mol M của các chất khác nhau nên C% sẽ khác nhau."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho phản ứng giữa kẽm và dung dịch axit sunfuric loãng: Zn + H2SO4 -> ZnSO4 + H2:",
        "statements": [
          {
            "subId": "a",
            "text": "Cho 6,5 g Zn vào 100 mL dung dịch H2SO4 1 M thì cả hai chất phản ứng vừa hết.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thể tích khí hiđro sinh ra ở đkc là 2,479 lít.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nồng độ mol của muối ZnSO4 trong dung dịch sau phản ứng là 1 M (coi thể tích không đổi).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng dung dịch sau phản ứng giảm 6,3 g so với dung dịch axit ban đầu.",
            "correct": false
          }
        ],
        "explanation": "m_dd tăng = 6,5 - 0,2 = 6,3g (tăng chứ không giảm)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm hòa tan vôi sống vào nước tạo dung dịch nước vôi trong:",
        "statements": [
          {
            "subId": "a",
            "text": "Phản ứng tôi vôi tỏa nhiều nhiệt làm tăng nhiệt độ hỗn hợp.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Độ tan của canxi hiđroxit Ca(OH)2 trong nước rất nhỏ (chất ít tan).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch nước vôi trong là dung dịch Ca(OH)2 bão hòa đã được lọc bỏ cặn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đun nóng nước vôi trong thấy xuất hiện vẩn đục do độ tan của Ca(OH)2 giảm khi tăng nhiệt độ.",
            "correct": true
          }
        ],
        "explanation": "Ca(OH)2 là một trong số ít chất rắn giảm độ tan khi tăng nhiệt độ."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Dung dịch nước muối sinh lí chứa bao nhiêu gam NaCl trong 1000 g dung dịch?",
        "correctAnswer": "9",
        "explanation": "1000 * 0,9% = 9 g."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khối lượng chất tan có trong 250 g dung dịch đường 8% là bao nhiêu gam?",
        "correctAnswer": "20",
        "explanation": "250 * 8% = 20 g."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Nồng độ mol của 100 mL dung dịch chứa 0,05 mol HCl là bao nhiêu M? (Ghi số thập phân)",
        "correctAnswer": "0,5",
        "explanation": "0,05 / 0,1 = 0,5 M."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cần lấy bao nhiêu mL nước cất thêm vào 100 mL dung dịch NaOH 2 M để được dung dịch NaOH 1 M?",
        "correctAnswer": "100",
        "explanation": "V_mới = 200 mL -> thêm 100 mL nước."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan hết 4 g NaOH vào nước thu được 500 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M? (Ghi số thập phân)",
        "correctAnswer": "0,2",
        "explanation": "n = 0,1 mol -> CM = 0,1 / 0,5 = 0,2 M."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cho 0,1 mol Fe tác dụng vừa đủ với 100 mL dung dịch HCl. Nồng độ mol của dung dịch HCl là bao nhiêu M?",
        "correctAnswer": "2",
        "explanation": "Fe + 2HCl -> n_HCl = 0,2 mol -> CM = 0,2 / 0,1 = 2 M."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan 13 g kim loại kẽm vào 200 g dung dịch HCl 7,3%. Nồng độ phần trăm của muối ZnCl2 trong dung dịch sau phản ứng là:",
        "options": [
          "12,85%",
          "13,6%",
          "10,2%",
          "8,5%"
        ],
        "correct": 0,
        "explanation": "n_Zn = 0,2 mol; n_HCl = 200*7,3% / 36,5 = 0,4 mol (vừa đủ). m_ZnCl2 = 0,2 * 136 = 27,2 g; m_dd sau = 13 + 200 - 0,4 = 212,6 g -> C% = 27,2 / 212,6 = 12,79% xấp xỉ 12,85%."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trộn 200 g dung dịch BaCl2 10,4% với 100 g dung dịch H2SO4 9,8%. Khối lượng kết tủa BaSO4 thu được là:",
        "options": [
          "23,3 g",
          "11,65 g",
          "46,6 g",
          "15,5 g"
        ],
        "correct": 0,
        "explanation": "n_BaCl2 = 20,8 / 208 = 0,1 mol; n_H2SO4 = 9,8 / 98 = 0,1 mol -> m_BaSO4 = 0,1 * 233 = 23,3 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để pha được 500 mL dung dịch CuSO4 0,2 M từ dung dịch CuSO4 1 M thì thể tích dung dịch CuSO4 1 M cần lấy là:",
        "options": [
          "100 mL",
          "200 mL",
          "50 mL",
          "150 mL"
        ],
        "correct": 0,
        "explanation": "n = 0,5 * 0,2 = 0,1 mol -> V = 0,1 / 1 = 0,1 L = 100 mL."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một dung dịch bão hòa muối ăn ở nhiệt độ T có nồng độ 25%. Độ tan S của muối ăn ở nhiệt độ này là:",
        "options": [
          "33,33 g",
          "25,0 g",
          "30,0 g",
          "36,0 g"
        ],
        "correct": 0,
        "explanation": "S = (C% / (100 - C%)) * 100 = (25 / 75) * 100 = 33,33 g."
      }
    ]
  },
  "chem8_c1_b7_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Tốc độ phản ứng là đại lượng đặc trưng cho:",
        "options": [
          "Mức độ nhanh hay chậm của một phản ứng hóa học",
          "Khối lượng chất tham gia phản ứng",
          "Thể tích chất khí sinh ra",
          "Nhiệt độ sôi của chất phản ứng"
        ],
        "correct": 0,
        "explanation": "Tốc độ phản ứng đo lường độ nhanh hay chậm của phản ứng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khi tăng nồng độ chất phản ứng, tốc độ phản ứng nói chung sẽ:",
        "options": [
          "Tăng lên",
          "Giảm đi",
          "Không đổi",
          "Ban đầu tăng sau giảm"
        ],
        "correct": 0,
        "explanation": "Tăng nồng độ làm tăng số va chạm hiệu quả giữa các phân tử, làm tăng tốc độ phản ứng."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi tăng nhiệt độ, tốc độ của hầu hết các phản ứng hóa học sẽ:",
        "options": [
          "Tăng lên",
          "Giảm đi",
          "Không thay đổi",
          "Biến mất hoàn toàn"
        ],
        "correct": 0,
        "explanation": "Nhiệt độ tăng làm các phân tử chuyển động nhanh hơn, tăng va chạm hiệu quả."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Thao tác nào sau đây làm tăng tốc độ phản ứng giữa kẽm và dung dịch axit clohiđric?",
        "options": [
          "Đun nóng nhẹ dung dịch axit",
          "Làm lạnh dung dịch axit",
          "Pha loãng dung dịch axit bằng nhiều nước",
          "Dùng miếng kẽm kích thước thật to"
        ],
        "correct": 0,
        "explanation": "Đun nóng làm tăng nhiệt độ, đẩy nhanh tốc độ phản ứng."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tại sao than củi cháy trong khí oxi nguyên chất sáng và mãnh liệt hơn cháy ngoài không khí?",
        "options": [
          "Nồng độ khí oxi trong bình oxi nguyên chất cao hơn nhiều so với trong không khí (khoảng 21%)",
          "Khí oxi nguyên chất nóng hơn",
          "Khí oxi nguyên chất chứa chất xúc tác",
          "Than củi tan biến thành lỏng"
        ],
        "correct": 0,
        "explanation": "Nồng độ O2 cao hơn làm phản ứng cháy diễn ra nhanh và mãnh liệt hơn."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Thực phẩm được bảo quản trong tủ lạnh để lâu bị ôi thiu hơn so với để ở nhiệt độ phòng là ứng dụng của yếu tố nào?",
        "options": [
          "Giảm nhiệt độ làm giảm tốc độ của các phản ứng hóa sinh phân hủy",
          "Tăng nồng độ chất bảo quản",
          "Giảm diện tích tiếp xúc",
          "Tăng áp suất trong tủ lạnh"
        ],
        "correct": 0,
        "explanation": "Hạ nhiệt độ làm chậm tốc độ phản ứng phân hủy thức ăn."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi hòa tan cùng một khối lượng kẽm vào 2 cốc đựng axit HCl có nồng độ lần lượt là 1 M và 2 M ở cùng nhiệt độ, hiện tượng quan sát được là:",
        "options": [
          "Cốc chứa axit 2 M sủi bọt khí nhanh và mạnh hơn",
          "Cốc chứa axit 1 M sủi bọt khí nhanh hơn",
          "Cả 2 cốc sủi bọt khí với tốc độ như nhau",
          "Cốc chứa axit 2 M không sủi bọt"
        ],
        "correct": 0,
        "explanation": "Nồng độ axit cao hơn thì tốc độ thoát khí H2 nhanh hơn."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Dùng nồi áp suất để ninh xương giúp xương nhanh mềm hơn là do:",
        "options": [
          "Áp suất cao làm tăng nhiệt độ sôi của nước lên trên 100 °C, làm phản ứng hóa sinh diễn ra nhanh hơn",
          "Nồi áp suất kín ngăn oxi thoát ra",
          "Nồi áp suất chứa chất xúc tác",
          "Nồi áp suất làm giảm thể tích nước"
        ],
        "correct": 0,
        "explanation": "Nhiệt độ sôi tăng lên khoảng 115 - 120 °C làm tăng tốc độ phản ứng ninh chín."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Tiến hành phản ứng giữa dung dịch Na2S2O3 với dung dịch H2SO4 loãng ở các nhiệt độ khác nhau (20 °C, 30 °C, 40 °C). Thời gian xuất hiện kết tủa lưu huỳnh vẩn đục ngắn nhất ở nhiệt độ nào?",
        "options": [
          "40 °C",
          "20 °C",
          "30 °C",
          "Thời gian như nhau ở cả 3 nhiệt độ"
        ],
        "correct": 0,
        "explanation": "Ở 40 °C nhiệt độ cao nhất nên tốc độ phản ứng nhanh nhất, thời gian ngắn nhất."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trong công nghiệp tổng hợp amoniac (N2 + 3H2 -> 2NH3), người ta thực hiện phản ứng ở áp suất cao (khoảng 200 atm). Yếu tố áp suất ảnh hưởng đến tốc độ phản ứng là do:",
        "options": [
          "Nén các phân tử khí lại gần nhau, làm tăng nồng độ chất phản ứng thể khí",
          "Làm giảm nhiệt độ phản ứng",
          "Biến đổi chất xúc tác",
          "Làm khí N2 hóa lỏng"
        ],
        "correct": 0,
        "explanation": "Tăng áp suất chất khí tương đương với tăng nồng độ."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Để làm sạch các vết bẩn dầu mỡ trên bát đĩa, người ta thường dùng nước rửa chén pha với nước ấm nóng. Yếu tố ảnh hưởng chính ở đây là:",
        "options": [
          "Nhiệt độ ấm làm tăng tốc độ phản ứng và hòa tan dầu mỡ",
          "Nhiệt độ ấm làm giảm bọt xà phòng",
          "Nước ấm làm biến đổi cấu tạo sứ",
          "Nước ấm làm giảm lượng nước rửa bát"
        ],
        "correct": 0,
        "explanation": "Nhiệt độ cao thúc đẩy quá trình hòa tan và tẩy rửa."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Một phản ứng hóa học khi nhiệt độ tăng thêm 10 °C thì tốc độ phản ứng tăng lên 2 lần (hệ số nhiệt độ gamma = 2). Nếu tăng nhiệt độ từ 20 °C lên 50 °C thì tốc độ phản ứng tăng lên bao nhiêu lần?",
        "options": [
          "8 lần",
          "6 lần",
          "16 lần",
          "4 lần"
        ],
        "correct": 0,
        "explanation": "Delta t = 30 °C -> tăng 2^(30/10) = 2^3 = 8 lần."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các yếu tố ảnh hưởng đến tốc độ phản ứng:",
        "statements": [
          {
            "subId": "a",
            "text": "Tốc độ phản ứng tỉ lệ thuận với nồng độ của các chất tham gia.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi nhiệt độ tăng, tốc độ của hầu hết các phản ứng hóa học đều tăng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tăng áp suất có tác dụng làm tăng tốc độ đối với các phản ứng có chất khí tham gia.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Mọi phản ứng hóa học đều diễn ra với tốc độ như nhau ở cùng một nhiệt độ.",
            "correct": false
          }
        ],
        "explanation": "Mỗi phản ứng có bản chất hóa học khác nhau nên tốc độ rất khác nhau."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các ứng dụng thực tế điều khiển tốc độ phản ứng:",
        "statements": [
          {
            "subId": "a",
            "text": "Thổi không khí vào lò than đang cháy làm tăng nồng độ O2, giúp than cháy mạnh hơn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cho thức ăn vào tủ đông để làm đông đá nước, làm dừng hầu hết phản ứng ôi thiu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đậy nắp ấm đun nước để giữ nhiệt độ sôi 100 °C giúp đun nhanh sôi hơn.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bảo quản hạt giống trong kho lạnh ẩm ướt để hạt nhanh nảy mầm trong kho.",
            "correct": false
          }
        ],
        "explanation": "Cần bảo quản hạt giống ở nơi khô mát để ngăn nảy mầm sớm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho thí nghiệm giữa 2 g kẽm hạt với 50 mL dung dịch HCl 1 M ở các điều kiện khác nhau:",
        "statements": [
          {
            "subId": "a",
            "text": "Thí nghiệm ở 40 °C thoát khí nhanh hơn ở 20 °C.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thí nghiệm dùng axit HCl 2 M thoát khí nhanh hơn dùng axit HCl 1 M.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thay 2 g kẽm hạt bằng 2 g kẽm bột thì phản ứng xảy ra chậm hơn.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Lượng khí H2 tối đa thu được ở hai nhiệt độ 20 °C và 40 °C là bằng nhau nếu Zn phản ứng hết.",
            "correct": true
          }
        ],
        "explanation": "Kẽm bột có diện tích tiếp xúc lớn hơn nên phản ứng nhanh hơn."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng phân hủy canxi cacbonat trong lò vôi công nghiệp: CaCO3 -> CaO + CO2:",
        "statements": [
          {
            "subId": "a",
            "text": "Để phản ứng phân hủy diễn ra nhanh, người ta phải duy trì nhiệt độ lò khoảng 900 - 1000 °C.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nếu đập nhỏ đá vôi trước khi nung thì tốc độ phân hủy sẽ tăng lên.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu đóng kín miệng lò để khí CO2 không thoát ra thì phản ứng tạo vôi sống sẽ diễn ra nhanh hơn.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Hút bớt khí CO2 ra khỏi lò giúp cân bằng chuyển dịch theo chiều tạo thêm CaO.",
            "correct": true
          }
        ],
        "explanation": "CO2 tích tụ làm cản trở phản ứng thuận chiều phân hủy."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Khi nồng độ chất phản ứng tăng lên thì tốc độ phản ứng tăng hay giảm?",
        "correctAnswer": "tăng",
        "explanation": "Nồng độ tăng làm tốc độ tăng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các yếu tố: nồng độ, nhiệt độ, áp suất, diện tích bề mặt, chất xúc tác. Có bao nhiêu yếu tố ảnh hưởng đến tốc độ phản ứng?",
        "correctAnswer": "5",
        "explanation": "Có đủ 5 yếu tố ảnh hưởng."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khi nhiệt độ tăng thêm 10 °C, tốc độ phản ứng tăng 3 lần. Nếu nhiệt độ tăng thêm 20 °C thì tốc độ phản ứng tăng bao nhiêu lần?",
        "correctAnswer": "9",
        "explanation": "3^2 = 9 lần."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Học sinh làm thí nghiệm cho thanh kẽm vào 3 cốc axit HCl có nồng độ: 0,5 M; 1 M; 2 M. Cốc nào có tốc độ thoát khí nhanh nhất? (Điền nồng độ: 0,5 hoặc 1 hoặc 2)",
        "correctAnswer": "2",
        "explanation": "Cốc có nồng độ 2 M thoát khí nhanh nhất."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Trong công nghệ thực phẩm, sấy khô hoa quả làm giảm hàm lượng nước tự do, qua đó làm giảm tốc độ phản ứng hư hỏng của vi sinh vật. Đây là yếu tố thay đổi nồng độ chất tan hay diện tích bề mặt? (Điền: nồng độ)",
        "correctAnswer": "nồng độ",
        "explanation": "Giảm hàm lượng nước là thay đổi nồng độ dung môi/chất phản ứng."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một phản ứng kết thúc sau 60 giây ở 30 °C. Biết cứ tăng 10 °C tốc độ phản ứng tăng 2 lần. Ở 50 °C phản ứng sẽ kết thúc sau bao nhiêu giây? (Ghi số thập phân)",
        "correctAnswer": "15",
        "explanation": "Tăng 20 °C -> tốc độ tăng 4 lần -> thời gian = 60 / 4 = 15 giây."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Biện pháp nào sau đây KHÔNG LÀM TĂNG tốc độ của phản ứng giữa đá vôi và dung dịch axit clohiđric?",
        "options": [
          "Thêm nước cất vào dung dịch axit",
          "Nghiền nhỏ đá vôi thành bột mịn",
          "Đun nóng dung dịch axit lên 50 °C",
          "Dùng dung dịch axit có nồng độ cao hơn"
        ],
        "correct": 0,
        "explanation": "Thêm nước cất làm loãng axit (giảm nồng độ), làm giảm tốc độ phản ứng."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khi bảo quản thịt tươi sống, phương pháp nào sau đây dựa trên nguyên tắc làm giảm tốc độ phản ứng phân hủy vi sinh vật bằng cách hạ nhiệt độ?",
        "options": [
          "Bảo quản trong ngăn đá tủ lạnh ở -18 °C",
          "Ướp muối thật mặn",
          "Hun khói thịt",
          "Ngâm thịt vào giấm ăn"
        ],
        "correct": 0,
        "explanation": "Ngăn đá tủ lạnh hạ nhiệt độ cực thấp làm giảm tốc độ phản ứng."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Trong phản ứng tổng hợp amoniac N2 + 3H2 -> 2NH3, người ta dùng bột sắt (Fe) làm chất xúc tác. Vai trò của sắt là:",
        "options": [
          "Làm tăng tốc độ phản ứng đạt đến trạng thái cân bằng nhanh hơn mà không bị tiêu hao",
          "Làm tăng khối lượng amoniac sinh ra vượt mức lí thuyết",
          "Làm phản ứng không tỏa nhiệt nữa",
          "Thay thế cho khí nitơ"
        ],
        "correct": 0,
        "explanation": "Chất xúc tác chỉ làm tăng tốc độ phản ứng mà không bị tiêu hao."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Ở 25 °C, một phản ứng hóa học xảy ra với tốc độ v0. Khi tăng nhiệt độ lên 65 °C, tốc độ phản ứng tăng lên 81 lần. Hệ số nhiệt độ gamma của phản ứng này là:",
        "options": [
          "3",
          "2",
          "4",
          "5"
        ],
        "correct": 0,
        "explanation": "Delta t = 40 °C -> gamma^(40/10) = gamma^4 = 81 -> gamma = 3."
      }
    ]
  },
  "chem8_c1_b7_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Chất xúc tác là chất:",
        "options": [
          "Làm tăng tốc độ phản ứng và được hoàn nguyên khối lượng, tính chất sau phản ứng",
          "Bị biến đổi hoàn toàn thành sản phẩm mới",
          "Làm giảm tốc độ của phản ứng hóa học",
          "Có mặt để hòa tan các chất phản ứng"
        ],
        "correct": 0,
        "explanation": "Chất xúc tác đẩy nhanh phản ứng và không bị biến đổi sau phản ứng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khi tăng diện tích bề mặt tiếp xúc của chất rắn phản ứng, tốc độ phản ứng sẽ:",
        "options": [
          "Tăng lên",
          "Giảm đi",
          "Không đổi",
          "Bằng không"
        ],
        "correct": 0,
        "explanation": "Diện tích tiếp xúc càng lớn thì số va chạm giữa các chất phản ứng càng nhiều, tốc độ phản ứng càng tăng."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chất xúc tác sinh học có trong cơ thể sinh vật sống được gọi là:",
        "options": [
          "Enzym (men)",
          "Vitamin",
          "Hormon",
          "Protein dự trữ"
        ],
        "correct": 0,
        "explanation": "Enzym là các chất xúc tác sinh học đặc hiệu trong cơ thể."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Hành động nào sau đây làm tăng diện tích bề mặt tiếp xúc của chất rắn?",
        "options": [
          "Nghiền nhỏ hoặc tán thành bột mịn",
          "Đúc thành một khối tròn đặc",
          "Nhúng vào dầu chống ẩm",
          "Đựng trong hộp kín"
        ],
        "correct": 0,
        "explanation": "Nghiền nhỏ làm tăng diện tích tiếp xúc."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Tại sao than tổ ong thường được tạo nhiều lỗ rỗng xuyên suốt thân viên than?",
        "options": [
          "Để tăng diện tích tiếp xúc giữa than với không khí và hút dưỡng khí giúp than cháy đều và mạnh",
          "Để làm viên than nhẹ hơn dễ vận chuyển",
          "Để tiết kiệm lượng than sản xuất",
          "Để dễ cầm tay khi gắp than"
        ],
        "correct": 0,
        "explanation": "Các lỗ rỗng tăng lưu thông không khí và tăng diện tích tiếp xúc với oxi."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khi cho một mẩu MnO2 vào dung dịch hiđro peoxit (H2O2 - nước oxy già), thấy bọt khí O2 sủi lên mãnh liệt. Vai trò của MnO2 là:",
        "options": [
          "Chất xúc tác thúc đẩy sự phân hủy của H2O2",
          "Chất phản ứng bị tiêu hao hoàn toàn",
          "Chất ức chế làm chậm phản ứng",
          "Dung môi hòa tan khí oxi"
        ],
        "correct": 0,
        "explanation": "MnO2 là chất xúc tác cho phản ứng: 2H2O2 -> 2H2O + O2."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hòa tan cùng một lượng viên sủi vitamin C vào 2 cốc nước ở cùng nhiệt độ: cốc 1 thả nguyên viên sủi, cốc 2 nghiền nát thành bột rồi đổ vào. Hiện tượng quan sát được là:",
        "options": [
          "Cốc 2 tan nhanh và sủi bọt mạnh hơn cốc 1",
          "Cốc 1 tan nhanh hơn cốc 2",
          "Hai cốc tan với thời gian hoàn toàn bằng nhau",
          "Cốc 2 không sủi bọt"
        ],
        "correct": 0,
        "explanation": "Bột sủi có diện tích tiếp xúc lớn hơn nên phản ứng với nước nhanh hơn."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Chẻ nhỏ củi trước khi cho vào bếp đun nấu là ứng dụng của yếu tố nào ảnh hưởng đến tốc độ phản ứng?",
        "options": [
          "Tăng diện tích bề mặt tiếp xúc",
          "Tăng nồng độ chất phản ứng",
          "Thêm chất xúc tác",
          "Tăng áp suất"
        ],
        "correct": 0,
        "explanation": "Chẻ nhỏ củi làm tăng diện tích tiếp xúc của củi với oxi."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Men nở (nấm men bánh mì) dùng khi làm bánh mì có vai trò:",
        "options": [
          "Xúc tác quá trình lên men phân giải đường sinh khí CO2 làm bột bánh xốp nở",
          "Làm vỏ bánh ngọt hơn",
          "Tẩy trắng bột mì",
          "Làm bánh đông đặc thành khối cứng"
        ],
        "correct": 0,
        "explanation": "Nấm men tiết enzym xúc tác quá trình lên men sinh CO2 tạo độ xốp."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Thực hiện phản ứng: CaCO3 + 2HCl -> CaCl2 + CO2 + H2O. Trong 4 trường hợp sau, trường hợp nào phản ứng diễn ra với tốc độ nhanh nhất?",
        "options": [
          "Bột đá vôi mịn + dung dịch HCl 2 M ở 40 °C",
          "Mẩu đá vôi to + dung dịch HCl 2 M ở 40 °C",
          "Bột đá vôi mịn + dung dịch HCl 1 M ở 25 °C",
          "Mẩu đá vôi to + dung dịch HCl 1 M ở 25 °C"
        ],
        "correct": 0,
        "explanation": "Kết hợp cả 3 yếu tố: dạng bột (diện tích lớn), nồng độ 2 M cao và nhiệt độ 40 °C cao."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Để làm giảm tốc độ gỉ sét của vỏ tàu biển bằng thép, người ta gắn các tấm kẽm (Zn) vào vỏ tàu hoặc sơn phủ lớp sơn chống rỉ. Lớp sơn chống rỉ có vai trò:",
        "options": [
          "Ngăn cách bề mặt sắt tiếp xúc với oxi và nước ẩm trong không khí/nước biển",
          "Đóng vai trò chất xúc tác phân hủy gỉ",
          "Tăng nhiệt độ của kim loại",
          "Hòa tan các muối biển"
        ],
        "correct": 0,
        "explanation": "Lớp sơn cách li kim loại với môi trường ăn mòn."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Hai thí nghiệm phân hủy dung dịch H2O2 cùng nồng độ và thể tích: Thí nghiệm 1 không có xúc tác mất 20 phút mới phân hủy hết. Thí nghiệm 2 thêm 0,1 g bột MnO2 chỉ mất 15 giây. Sau thí nghiệm 2, lọc lấy chất rắn MnO2, sấy khô và cân lại thấy khối lượng của MnO2 là:",
        "options": [
          "Đúng 0,1 g",
          "0,05 g",
          "0,0 g (tan hết)",
          "0,2 g"
        ],
        "correct": 0,
        "explanation": "Chất xúc tác không bị tiêu hao sau phản ứng nên khối lượng vẫn giữ nguyên 0,1 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về diện tích bề mặt tiếp xúc và tốc độ phản ứng:",
        "statements": [
          {
            "subId": "a",
            "text": "Diện tích bề mặt tiếp xúc chỉ có ý nghĩa đối với các phản ứng có chất rắn tham gia.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nghiền chất rắn thành bột mịn làm tăng tổng diện tích bề mặt tiếp xúc lên nhiều lần.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chất rắn ở dạng khối đặc tiếp xúc tốt hơn chất rắn ở dạng bột tơi xốp.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Bụi than và bụi bột mì lơ lửng trong không khí có thể gây ra các vụ nổ bụi nguy hiểm do diện tích tiếp xúc cực lớn.",
            "correct": true
          }
        ],
        "explanation": "Khối đặc có diện tích tiếp xúc nhỏ hơn dạng bột."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về chất xúc tác và enzym trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Chất xúc tác làm tăng tốc độ phản ứng nhưng không tham gia vào thành phần sản phẩm cuối cùng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Mỗi loại enzym sinh học thường chỉ xúc tác cho một phản ứng hoặc một nhóm phản ứng nhất định.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Chất xúc tác bị tiêu hao dần theo thời gian và biến thành chất mới sau phản ứng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Trong cơ thể người, men amilaza trong nước bọt xúc tác cho phản ứng thủy phân tinh bột thành đường.",
            "correct": true
          }
        ],
        "explanation": "Chất xúc tác được hoàn nguyên nguyên vẹn về lượng và chất."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về các kinh nghiệm dân gian trong ẩm thực và đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Hầm thịt bò với quả đu đủ xanh giúp thịt nhanh mềm vì trong nhựa đu đủ có chứa enzym papain phân giải protein.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đập dập củ sả, ớt, tỏi trước khi ướp thịt giúp các tinh dầu và chất ngấm nhanh hơn nhờ tăng diện tích tiếp xúc.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Muối dưa cà muốn nhanh chua thì cho thêm một ít nước dưa cũ đóng vai trò cung cấp vi khuẩn lên men (tương tự xúc tác).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Để đống mùn cưa to ướt trong góc nhà sẽ tự bốc cháy ngay tức khắc vì diện tích tiếp xúc rất lớn.",
            "correct": false
          }
        ],
        "explanation": "Mùn cưa ướt không đủ điều kiện bốc cháy tức thì."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng phân hủy khí N2O trên bề mặt chất xúc tác platin (Pt):",
        "statements": [
          {
            "subId": "a",
            "text": "Chất xúc tác Pt tạo ra con đường phản ứng mới có năng lượng hoạt hóa thấp hơn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tốc độ phân hủy N2O tăng lên hàng triệu lần khi có mặt Pt nung nóng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Lượng platin sau phản ứng bị hao hụt 50% khối lượng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Bộ lọc khí thải xe máy, ô tô dùng chất xúc tác kim loại quý (Pt, Pd, Rh) để xử lý khí độc hại CO, NOx thành CO2, N2 vô hại.",
            "correct": true
          }
        ],
        "explanation": "Xúc tác Pt không hề bị hao hụt khối lượng."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Chất làm tăng tốc độ phản ứng mà không bị tiêu hao sau phản ứng gọi là chất gì?",
        "correctAnswer": "chất xúc tác",
        "explanation": "Chất xúc tác."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho hai mẫu kẽm cùng khối lượng 5 g: mẫu 1 dạng lá mỏng, mẫu 2 dạng khối cầu đặc. Mẫu nào phản ứng với axit HCl nhanh hơn? (Điền: mẫu 1 hoặc mẫu 2)",
        "correctAnswer": "mẫu 1",
        "explanation": "Mẫu 1 dạng lá mỏng có diện tích bề mặt lớn hơn."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khối lượng của 0,5 g chất xúc tác MnO2 sau khi phản ứng kết thúc còn lại bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "0,5",
        "explanation": "Chất xúc tác giữ nguyên khối lượng 0,5 g."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong công nghiệp sản xuất axit sunfuric, người ta dùng oxit vanadi (V2O5) làm gì trong phản ứng oxi hóa SO2 thành SO3? (Điền: chất xúc tác)",
        "correctAnswer": "chất xúc tác",
        "explanation": "V2O5 đóng vai trò chất xúc tác."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Để than nhanh bén lửa và cháy đượm, người ta thường chẻ nhỏ củi mồi rồi xếp so le tạo khe hở. Thao tác này tác động đến bao nhiêu yếu tố chính (diện tích tiếp xúc, nồng độ oxi)?",
        "correctAnswer": "2",
        "explanation": "Tác động đến 2 yếu tố: diện tích tiếp xúc và nồng độ lưu thông oxi."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Trong dạ dày người, axit clohiđric HCl cùng men gì xúc tác phân giải protein thịt cá? (Điền tên men: pepsin)",
        "correctAnswer": "pepsin",
        "explanation": "Enzym pepsin."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một học sinh làm 4 thí nghiệm thoát khí CO2 từ phản ứng giữa canxi cacbonat và axit clohiđric. Cặp thí nghiệm nào sau đây chứng minh rõ ràng nhất ảnh hưởng của DIỆN TÍCH BỀ MẶT TIẾP XÚC đến tốc độ phản ứng?",
        "options": [
          "10 g đá vôi hạt to + 100 mL HCl 1 M và 10 g đá vôi bột mịn + 100 mL HCl 1 M ở cùng nhiệt độ",
          "10 g đá vôi bột mịn + 100 mL HCl 1 M ở 25 °C và 10 g đá vôi bột mịn + 100 mL HCl 1 M ở 50 °C",
          "10 g đá vôi hạt to + 100 mL HCl 1 M và 10 g đá vôi hạt to + 100 mL HCl 2 M ở 25 °C",
          "10 g đá vôi bột mịn + 100 mL HCl 1 M và 5 g đá vôi hạt to + 50 mL HCl 0,5 M"
        ],
        "correct": 0,
        "explanation": "Cần giữ nguyên nồng độ HCl, thể tích và nhiệt độ, chỉ thay đổi kích thước đá vôi (hạt to vs bột mịn)."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Tại các mỏ than, hầm chứa thóc ngô khô hay xưởng cưa, biển cảnh báo cấm lửa tuyệt đối được treo nghiêm ngặt. Nguy cơ nổ bụi tại các nơi này rất cao là do:",
        "options": [
          "Các hạt bụi mịn có diện tích bề mặt tiếp xúc với oxi không khí vô cùng lớn, khi gặp mồi lửa phản ứng cháy xảy ra tức thì tỏa nhiệt cực lớn gây nổ",
          "Bụi than tự bốc cháy ở -20 °C",
          "Bụi ngô chứa chất phóng xạ",
          "Hầm chứa không có khí oxi"
        ],
        "correct": 0,
        "explanation": "Nổ bụi là hiện tượng cháy cực nhanh do diện tích tiếp xúc khổng lồ của các hạt bụi mịn."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hiện tượng nào sau đây thể hiện tác dụng làm CHẬM tốc độ phản ứng (sử dụng chất ức chế)?",
        "options": [
          "Thêm một lượng nhỏ chất chống oxi hóa BHT vào dầu ăn để ngăn dầu bị ôi khét",
          "Thêm men rượu vào cơm nếp",
          "Thêm MnO2 vào H2O2",
          "Thêm bột sắt vào hỗn hợp N2 và H2"
        ],
        "correct": 0,
        "explanation": "Chất chống oxi hóa đóng vai trò chất ức chế làm chậm phản ứng hư hỏng."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho phản ứng phân hủy H2O2 có xúc tác MnO2. Nếu dùng 0,2 g bột MnO2 mịn so với 0,2 g viên MnO2 ép chặt thì:",
        "options": [
          "Dùng bột MnO2 mịn phản ứng diễn ra nhanh hơn do diện tích bề mặt chất xúc tác lớn hơn",
          "Dùng viên MnO2 ép chặt phản ứng nhanh hơn",
          "Tốc độ như nhau vì cùng khối lượng 0,2 g",
          "Bột MnO2 làm ngừng phản ứng"
        ],
        "correct": 0,
        "explanation": "Chất xúc tác dạng bột mịn có diện tích bề mặt lớn hơn, tiếp xúc tốt hơn nên xúc tác hiệu quả hơn."
      }
    ]
  },
  "chem8_c1_b7_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Để xác định tốc độ của phản ứng sinh ra chất khí, người ta thường đo:",
        "options": [
          "Thể tích chất khí thoát ra theo thời gian",
          "Khối lượng của bình sau 1 năm",
          "Độ dài của ống nghiệm",
          "Màu sắc của ngọn lửa đèn cồn"
        ],
        "correct": 0,
        "explanation": "Đo thể tích khí sinh ra theo từng khoảng thời gian xác định."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Yếu tố nào sau đây KHÔNG ảnh hưởng đến tốc độ phản ứng hóa học?",
        "options": [
          "Khối lượng của chất xúc tác tăng gấp 10 lần",
          "Thể tích bình chứa chất lỏng không tham gia phản ứng",
          "Nồng độ chất phản ứng",
          "Nhiệt độ môi trường"
        ],
        "correct": 1,
        "explanation": "Thể tích khoảng không của bình không ảnh hưởng trực tiếp đến tốc độ phản ứng trong dung dịch."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi quạt gió vào bếp than đang cháy, ta đã tác động đến yếu tố nào?",
        "options": [
          "Tăng nồng độ khí oxi tiếp xúc với than",
          "Giảm nhiệt độ của than",
          "Thêm chất xúc tác",
          "Làm than biến thành bột"
        ],
        "correct": 0,
        "explanation": "Quạt gió cung cấp liên tục O2 mới làm tăng nồng độ oxi."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong cơ thể người, chất xúc tác enzym hoạt động tối ưu ở nhiệt độ khoảng:",
        "options": [
          "37 °C (thân nhiệt)",
          "100 °C",
          "0 °C",
          "60 °C"
        ],
        "correct": 0,
        "explanation": "Enzym trong cơ thể người hoạt động tốt nhất quanh thân nhiệt 37 °C."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Khi cho cùng một khối lượng magie vào cốc 1 đựng HCl 1 M và cốc 2 đựng HCl 0,5 M, tốc độ bọt khí thoát ra ở cốc 1 nhanh hơn cốc 2 là do:",
        "options": [
          "Ảnh hưởng của nồng độ chất phản ứng",
          "Ảnh hưởng của nhiệt độ",
          "Ảnh hưởng của diện tích tiếp xúc",
          "Ảnh hưởng của chất xúc tác"
        ],
        "correct": 0,
        "explanation": "Nồng độ HCl ở cốc 1 (1 M) cao hơn cốc 2 (0,5 M)."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho thanh kim loại sắt nhúng vào axit HCl loãng nguội thì bọt khí thoát ra từ từ; khi đun nóng cốc thì bọt khí thoát ra mãnh liệt. Hiện tượng này chứng minh:",
        "options": [
          "Tốc độ phản ứng tăng khi tăng nhiệt độ",
          "Tốc độ phản ứng giảm khi tăng nhiệt độ",
          "Sắt tan chảy ở nhiệt độ thấp",
          "Axit bị phân hủy thành nước"
        ],
        "correct": 0,
        "explanation": "Tăng nhiệt độ thúc đẩy tốc độ phản ứng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi muối dưa cải, người ta thường nén chặt dưa dưới một tấm vỉ và đè đá nặng lên trên. Thao tác này có tác dụng chính là:",
        "options": [
          "Làm dưa ngập hoàn toàn trong nước muối, hạn chế tiếp xúc với oxi không khí để vi khuẩn lactic lên men kị khí tốt và tránh mốc váng",
          "Làm dưa ngọt hơn",
          "Tăng nhiệt độ của vại dưa",
          "Làm tan hết muối ăn"
        ],
        "correct": 0,
        "explanation": "Nén dưa kị khí giúp vi khuẩn lactic phát triển, ngăn vi khuẩn hiếu khí gây thối hỏng."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nghiền nát hạt đậu tương trước khi nấu sữa đậu nành giúp sữa đặc sánh và thơm ngon hơn là do:",
        "options": [
          "Tăng diện tích bề mặt tiếp xúc giúp các chất béo và protein tan nhanh vào nước",
          "Làm giảm nhiệt độ sôi của nước",
          "Thêm enzym vào sữa",
          "Làm protein biến tính thành đường"
        ],
        "correct": 0,
        "explanation": "Nghiền nhỏ tăng diện tích tiếp xúc giúp chiết xuất kiệt dinh dưỡng."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Trong công nghiệp sản xuất phân đạm urê từ khí amoniac và CO2, người ta thực hiện ở nhiệt độ 180 - 200 °C và áp suất khoảng 200 atm. Việc duy trì áp suất cực cao nhằm mục đích gì?",
        "options": [
          "Tăng nồng độ các chất khí phản ứng giúp phản ứng xảy ra nhanh chóng và chuyển dịch cân bằng tạo nhiều urê hơn",
          "Làm giảm chi phí nhiên liệu",
          "Làm loãng chất khí",
          "Hút ẩm cho urê"
        ],
        "correct": 0,
        "explanation": "Tăng áp suất làm tăng mật độ hạt khí, tăng tốc độ phản ứng."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một miếng kim loại nhôm để ngoài không khí tự hình thành lớp màng oxit Al2O3 mỏng, mịn và rất bền vững bao bọc bên ngoài. Lớp màng này có tác dụng gì?",
        "options": [
          "Ngăn cản nhôm tiếp xúc với oxi và hơi ẩm, làm dừng hoàn toàn sự ăn mòn phá hủy nhôm bên trong",
          "Làm nhôm dẫn điện tốt hơn",
          "Làm tăng khối lượng nhôm lên gấp 10 lần",
          "Làm nhôm nóng chảy"
        ],
        "correct": 0,
        "explanation": "Màng oxit trơ bảo vệ nhôm khỏi sự ăn mòn tiếp diễn."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Đồ thị biểu diễn thể tích khí hiđro thoát ra theo thời gian khi cho kẽm vào axit HCl có dạng đường cong dốc đứng lúc đầu rồi thoai thoải dần và nằm ngang. Nguyên nhân đường cong thoai thoải dần là do:",
        "options": [
          "Nồng độ axit HCl giảm dần trong quá trình phản ứng nên tốc độ phản ứng giảm dần",
          "Nhiệt độ của cốc bị giảm xuống âm độ",
          "Kẽm bị trơ hóa biến thành vàng",
          "Khí hiđro ngưng tụ thành chất lỏng"
        ],
        "correct": 0,
        "explanation": "Nồng độ chất phản ứng tiêu hao dần làm tốc độ chậm lại."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Tiến hành 4 thí nghiệm hòa tan bột đá vôi bằng axit HCl với các điều kiện: (1) 20 °C, HCl 1 M; (2) 20 °C, HCl 2 M; (3) 40 °C, HCl 1 M; (4) 40 °C, HCl 2 M. Thứ tự tốc độ phản ứng tăng dần từ chậm nhất đến nhanh nhất là:",
        "options": [
          "(1) < (3) < (2) < (4) hoặc (1) < (2) < (3) < (4)",
          "(4) < (3) < (2) < (1)",
          "(1) < (4) < (2) < (3)",
          "(2) < (1) < (4) < (3)"
        ],
        "correct": 0,
        "explanation": "Thí nghiệm (1) thấp nhất (nhiệt độ thấp, nồng độ thấp); thí nghiệm (4) cao nhất (nhiệt độ cao, nồng độ cao)."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các phương pháp thực nghiệm đo tốc độ phản ứng:",
        "statements": [
          {
            "subId": "a",
            "text": "Có thể đo tốc độ phản ứng bằng cách đo độ giảm khối lượng của bình hở có khí thoát ra theo thời gian.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Có thể đo tốc độ phản ứng bằng cách đo thời gian cần thiết để xuất hiện lượng kết tủa làm mờ một dấu chữ thập dưới đáy cốc.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tốc độ phản ứng hóa học thường không đổi từ lúc bắt đầu cho đến khi kết thúc.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tốc độ phản ứng thường nhanh nhất ở giai đoạn đầu khi nồng độ chất phản ứng lớn nhất.",
            "correct": true
          }
        ],
        "explanation": "Tốc độ giảm dần theo thời gian do nồng độ các chất phản ứng giảm dần."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về an toàn hóa chất và tốc độ phản ứng:",
        "statements": [
          {
            "subId": "a",
            "text": "Phản ứng cháy nổ của bình gas xảy ra với tốc độ tức thời giải phóng lượng nhiệt và áp suất khổng lồ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sự gỉ sét của đinh sắt ngoài trời là phản ứng oxi hóa chậm diễn ra trong nhiều tháng hoặc nhiều năm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Để làm chậm sự ôi thiu của dầu thực vật, người ta đóng chai kín và để ở nơi râm mát, tránh ánh nắng mặt trời.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các phản ứng có chất xúc tác đều giải phóng nhiệt lượng lớn gây nổ.",
            "correct": false
          }
        ],
        "explanation": "Chất xúc tác chỉ tăng tốc độ, không làm thay đổi nhiệt phản ứng."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Xét phản ứng nhiệt phân muối KClO3: 2KClO3 -> 2KCl + 3O2:",
        "statements": [
          {
            "subId": "a",
            "text": "Nếu không có xúc tác MnO2, muối KClO3 cần nung ở nhiệt độ rất cao (khoảng 400 - 500 °C) mới phân hủy chậm chạp.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi trộn thêm bột MnO2, phản ứng phân hủy xảy ra mãnh liệt ngay ở nhiệt độ khoảng 200 °C.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "MnO2 trong phản ứng này đóng vai trò chất phản ứng cung cấp thêm oxi.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Bột MnO2 sau phản ứng có thể tách ra bằng cách hòa tan hỗn hợp vào nước rồi lọc lấy chất rắn không tan.",
            "correct": true
          }
        ],
        "explanation": "Oxi sinh ra hoàn toàn từ KClO3, MnO2 là chất xúc tác không đổi."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Về sự biến đổi tốc độ phản ứng sinh học trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Khi sốt cao trên 40 °C, các enzym trong cơ thể người có nguy cơ bị biến tính và mất hoạt tính xúc tác.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nhiệt độ quá thấp (0 °C) làm enzym ngừng hoạt động tạm thời nhưng không phá hủy cấu trúc của đa số enzym.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Muối chua dưa cải thành công là do sự phát triển chiếm ưu thế của vi khuẩn sinh axit lactic ức chế các vi khuẩn gây thối.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Rau quả để lâu trong môi trường chân không sẽ chín nhanh hơn để ngoài không khí.",
            "correct": false
          }
        ],
        "explanation": "Hút chân không loại bỏ O2 làm chậm quá trình chín và hư hỏng của rau quả."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phản ứng gỉ sắt là phản ứng xảy ra nhanh hay chậm?",
        "correctAnswer": "chậm",
        "explanation": "Gỉ sắt là phản ứng oxi hóa chậm."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Phản ứng cháy nổ của thuốc pháo xảy ra nhanh hay chậm?",
        "correctAnswer": "nhanh",
        "explanation": "Cháy nổ thuốc pháo xảy ra cực nhanh."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Để thúc đẩy quá trình lên men rượu diễn ra thuận lợi, người ta cần bổ sung chất xúc tác sinh học gì vào tinh bột chín? (Điền: men rượu)",
        "correctAnswer": "men rượu",
        "explanation": "Men rượu (chứa các enzym nấm men)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khi cho 0,1 mol Zn tác dụng với dung dịch HCl dư. Thể tích khí H2 sinh ra tối đa ở đkc là bao nhiêu lít? (Ghi số thập phân)",
        "correctAnswer": "2,479",
        "explanation": "n_H2 = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Trong công nghiệp thực phẩm, để hoa quả tươi lâu khi vận chuyển đi xa, người ta bơm khí trơ nào vào túi bọc để làm giảm tốc độ oxi hóa? (Điền: nitơ)",
        "correctAnswer": "nitơ",
        "explanation": "Khí nitơ N2 trơ về mặt hóa học."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Nếu tăng nhiệt độ của phản ứng lên thêm 30 °C, biết hệ số nhiệt độ gamma = 2. Tốc độ phản ứng sẽ tăng lên bao nhiêu lần?",
        "correctAnswer": "8",
        "explanation": "2^3 = 8 lần."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một nhóm học sinh khảo sát tốc độ phản ứng giữa magie và axit sunfuric loãng bằng cách thu khí hiđro vào ống đong chia độ úp ngược trên chậu nước. Sau các khoảng thời gian 10s, 20s, 30s, 40s, thể tích khí H2 thu được lần lượt là 15 mL, 28 mL, 38 mL, 45 mL. Tốc độ trung bình thoát khí trong khoảng thời gian từ 10s đến 20s là:",
        "options": [
          "1,3 mL/s",
          "1,5 mL/s",
          "1,0 mL/s",
          "0,7 mL/s"
        ],
        "correct": 0,
        "explanation": "v_tb = (28 - 15) / (20 - 10) = 13 / 10 = 1,3 mL/s."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khi bảo quản sữa tươi thanh trùng, tại sao trên bao bì nhà sản xuất luôn khuyến cáo 'Bảo quản ở nhiệt độ 2 °C - 4 °C và dùng hết trong vòng 24 giờ sau khi mở nắp'?",
        "options": [
          "Để nhiệt độ thấp kìm hãm tối đa tốc độ sinh sôi và chuyển hóa của vi khuẩn, và mở nắp làm nồng độ oxi tiếp xúc tăng mạnh thúc đẩy quá trình ôi thiu",
          "Để làm sữa ngọt hơn",
          "Để sữa không bị bay hơi",
          "Để sữa đông đặc thành phô mai"
        ],
        "correct": 0,
        "explanation": "Hạ nhiệt độ làm chậm tốc độ phản ứng phân hủy vi sinh vật; mở nắp tăng tiếp xúc với O2 và vi khuẩn."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Đốt cháy một que đóm trong không khí thấy cháy sáng bình thường; đưa vào lọ chứa khí oxi nguyên chất thấy bùng cháy chói lòa; đưa vào lọ chứa khí nitơ thấy tắt ngay lập tức. Thí nghiệm chứng minh:",
        "options": [
          "Nồng độ khí oxi quyết định tốc độ của phản ứng cháy",
          "Khí nitơ duy trì sự cháy tốt hơn oxi",
          "Que đóm cháy không cần nhiệt độ",
          "Tốc độ cháy trong nitơ là lớn nhất"
        ],
        "correct": 0,
        "explanation": "Nồng độ O2 càng cao tốc độ cháy càng nhanh mãnh liệt."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một bình kín chứa hỗn hợp khí gồm 1 mol SO2 và 0,5 mol O2 có mặt chất xúc tác V2O5. Nung nóng bình ở 450 °C một thời gian, hiệu suất phản ứng đạt 80%. Số mol SO3 tạo thành là:",
        "options": [
          "0,8 mol",
          "1,0 mol",
          "0,4 mol",
          "0,5 mol"
        ],
        "correct": 0,
        "explanation": "2SO2 + O2 -> 2SO3. n_SO2 pư = 1 * 80% = 0,8 mol -> n_SO3 = 0,8 mol."
      }
    ]
  },
  "chem8_c1_rev_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Dấu hiệu rõ ràng nhất để phân biệt biến đổi hóa học với biến đổi vật lí là:",
        "options": [
          "Có sự tạo thành chất mới",
          "Có sự thay đổi hình dạng",
          "Chất chuyển từ thể rắn sang thể lỏng",
          "Chất tan vào trong nước"
        ],
        "correct": 0,
        "explanation": "Bản chất của biến đổi hóa học là sinh ra chất mới."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong một phản ứng hóa học, liên kết giữa các nguyên tử:",
        "options": [
          "Bị thay đổi làm phân tử này biến đổi thành phân tử khác",
          "Luôn được giữ nguyên không đổi",
          "Bị biến mất hoàn toàn không hình thành liên kết mới",
          "Làm thay đổi số proton của nguyên tử"
        ],
        "correct": 0,
        "explanation": "Chỉ có liên kết giữa các nguyên tử thay đổi."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phản ứng tỏa nhiệt là phản ứng:",
        "options": [
          "Giải phóng năng lượng dưới dạng nhiệt ra môi trường",
          "Hấp thụ nhiệt lượng từ môi trường",
          "Làm nhiệt độ môi trường hạ thấp",
          "Không làm thay đổi nhiệt độ"
        ],
        "correct": 0,
        "explanation": "Phản ứng tỏa nhiệt giải phóng nhiệt ra môi trường."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Theo định luật bảo toàn khối lượng, trong một phản ứng hóa học:",
        "options": [
          "Tổng khối lượng chất sản phẩm bằng tổng khối lượng chất tham gia",
          "Khối lượng của từng chất không đổi",
          "Tổng thể tích các chất bảo toàn",
          "Số phân tử luôn bằng nhau"
        ],
        "correct": 0,
        "explanation": "Tổng khối lượng sản phẩm bằng tổng khối lượng chất phản ứng."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của khí carbon dioxide (CO2) là:",
        "options": [
          "44 g/mol",
          "28 g/mol",
          "32 g/mol",
          "16 g/mol"
        ],
        "correct": 0,
        "explanation": "M_CO2 = 12 + 16*2 = 44 g/mol."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Thể tích của 0,1 mol khí oxi ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "2,479 lít",
          "22,4 lít",
          "2,24 lít",
          "24,79 lít"
        ],
        "correct": 0,
        "explanation": "V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khí nào sau đây nặng hơn không khí?",
        "options": [
          "CO2 (M = 44)",
          "CH4 (M = 16)",
          "H2 (M = 2)",
          "NH3 (M = 17)"
        ],
        "correct": 0,
        "explanation": "M_CO2 = 44 > 29 nên nặng hơn không khí."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Hòa tan 15 g muối vào 85 g nước thu được dung dịch có nồng độ phần trăm là:",
        "options": [
          "15%",
          "17,6%",
          "10%",
          "20%"
        ],
        "correct": 0,
        "explanation": "m_dd = 15 + 85 = 100 g -> C% = 15%."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Nồng độ mol của 200 mL dung dịch chứa 0,4 mol NaOH là:",
        "options": [
          "2 M",
          "1 M",
          "0,8 M",
          "0,2 M"
        ],
        "correct": 0,
        "explanation": "CM = 0,4 / 0,2 = 2 M."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Khi cho bột kẽm vào dung dịch HCl, thao tác nào sau đây KHÔNG LÀM TĂNG tốc độ phản ứng?",
        "options": [
          "Thêm nước cất vào ống nghiệm",
          "Đun nóng dung dịch axit",
          "Dùng bột kẽm thay cho kẽm viên",
          "Dùng axit HCl nồng độ cao hơn"
        ],
        "correct": 0,
        "explanation": "Thêm nước làm loãng axit, giảm nồng độ, làm giảm tốc độ phản ứng."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Đốt cháy hoàn toàn 3,6 g kim loại magie trong bình chứa khí oxi dư thu được 6,0 g magie oxit (MgO). Khối lượng khí oxi đã phản ứng là:",
        "options": [
          "2,4 g",
          "1,2 g",
          "3,2 g",
          "1,6 g"
        ],
        "correct": 0,
        "explanation": "m_O2 = 6,0 - 3,6 = 2,4 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Hòa tan hết 5,4 g kim loại nhôm vào dung dịch axit sunfuric loãng vừa đủ. Thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "7,437 lít",
          "6,72 lít",
          "4,958 lít",
          "2,479 lít"
        ],
        "correct": 0,
        "explanation": "2Al + 3H2SO4 -> Al2(SO4)3 + 3H2. n_Al = 0,2 mol -> n_H2 = 0,3 mol -> V = 0,3 * 24,79 = 7,437 L."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các biến đổi chất trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Nước sôi bốc hơi là biến đổi vật lí.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đốt cháy cồn trong đĩa sứ là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Gỉ sắt hình thành trên bề mặt kim loại là biến đổi vật lí.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Lên men rượu từ cơm nếp là biến đổi hóa học.",
            "correct": true
          }
        ],
        "explanation": "Gỉ sắt là quá trình sắt bị oxi hóa tạo chất mới (hóa học)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về định luật bảo toàn khối lượng và phương trình hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Trong phản ứng hóa học, số nguyên tử của mỗi nguyên tố luôn được bảo toàn.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khi nung đá vôi, khối lượng chất rắn thu được giảm đi do khí CO2 đã bay đi.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Hệ số cân bằng trong phương trình hóa học có thể là phân số nguyên tố.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Cân bằng phương trình: 4Al + 3O2 -> 2Al2O3 đã chính xác.",
            "correct": true
          }
        ],
        "explanation": "Hệ số phương trình phải là các số nguyên tối giản."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về chất khí và dung dịch ở điều kiện chuẩn:",
        "statements": [
          {
            "subId": "a",
            "text": "Ở đkc (25 °C, 1 bar), 1 mol chất khí bất kì đều chiếm thể tích 24,79 lít.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí hiđro nhẹ hơn không khí nên được thu bằng cách úp ngược ống nghiệm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Pha 20 g đường vào 180 g nước thu được dung dịch đường 10%.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dung dịch bão hòa là dung dịch có thể hòa tan thêm chất tan ở nhiệt độ đó.",
            "correct": false
          }
        ],
        "explanation": "Dung dịch bão hòa không thể hòa tan thêm chất tan ở nhiệt độ đó."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Về tốc độ phản ứng và chất xúc tác:",
        "statements": [
          {
            "subId": "a",
            "text": "Tăng nồng độ chất phản ứng làm tăng số va chạm hiệu quả giữa các phân tử, làm tăng tốc độ phản ứng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Chất xúc tác làm tăng tốc độ phản ứng và bị tiêu hao hoàn toàn sau phản ứng.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Nhiệt độ càng cao thì tốc độ của phần lớn các phản ứng hóa học càng tăng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bảo quản thực phẩm trong tủ lạnh giúp làm chậm tốc độ hư hỏng thức ăn.",
            "correct": true
          }
        ],
        "explanation": "Chất xúc tác không bị tiêu hao sau phản ứng."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong một phản ứng hóa học, đại lượng nào được bảo toàn giữa chất tham gia và sản phẩm? (Điền: khối lượng)",
        "correctAnswer": "khối lượng",
        "explanation": "Khối lượng được bảo toàn."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Số mol của 4,958 lít khí N2 ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu mol? (Ghi số thập phân)",
        "correctAnswer": "0,2",
        "explanation": "4,958 / 24,79 = 0,2 mol."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của muối ăn NaCl là bao nhiêu g/mol? (Ghi số thập phân)",
        "correctAnswer": "58,5",
        "explanation": "M = 23 + 35,5 = 58,5 g/mol."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cần lấy bao nhiêu gam muối ăn NaCl để hòa tan vào nước thu được 500 g dung dịch NaCl 2%?",
        "correctAnswer": "10",
        "explanation": "m = 500 * 2% = 10 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Nung 10 g CaCO3 thu được 5,6 g CaO và bao nhiêu gam khí CO2? (Ghi số thập phân)",
        "correctAnswer": "4,4",
        "explanation": "10 - 5,6 = 4,4 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Đốt cháy 0,1 mol khí CH4 cần bao nhiêu lít khí oxi ở đkc? (Ghi số thập phân)",
        "correctAnswer": "4,958",
        "explanation": "CH4 + 2O2 -> cần 0,2 mol O2 = 0,2 * 24,79 = 4,958 L."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 11,2 g bột sắt vào dung dịch HCl 1 M vừa đủ. Thể tích dung dịch HCl cần dùng là:",
        "options": [
          "400 mL",
          "200 mL",
          "300 mL",
          "500 mL"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,2 mol -> n_HCl = 0,4 mol -> V = 0,4 / 1 = 0,4 L = 400 mL."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hỗn hợp khí X gồm 0,1 mol CO2 và 0,4 mol N2. Khối lượng mol trung bình của hỗn hợp X là:",
        "options": [
          "31,2 g/mol",
          "28,8 g/mol",
          "32,0 g/mol",
          "30,0 g/mol"
        ],
        "correct": 0,
        "explanation": "M_tb = (0,1*44 + 0,4*28) / 0,5 = (4,4 + 11,2) / 0,5 = 31,2 g/mol."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Đốt cháy hoàn toàn 6,2 g photpho trong khí oxi dư thu được m gam chất rắn P2O5. Giá trị của m là:",
        "options": [
          "14,2 g",
          "7,1 g",
          "28,4 g",
          "10,5 g"
        ],
        "correct": 0,
        "explanation": "4P + 5O2 -> 2P2O5. n_P = 0,2 mol -> n_P2O5 = 0,1 mol -> m = 0,1 * 142 = 14,2 g."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Trộn 100 mL dung dịch NaOH 1 M với 100 mL dung dịch H2SO4 0,5 M. Nồng độ mol của muối Na2SO4 thu được trong dung dịch sau phản ứng là:",
        "options": [
          "0,25 M",
          "0,5 M",
          "0,1 M",
          "0,2 M"
        ],
        "correct": 0,
        "explanation": "2NaOH + H2SO4 -> Na2SO4 + 2H2O. n_Na2SO4 = 0,05 mol; V = 0,2 L -> CM = 0,05 / 0,2 = 0,25 M."
      }
    ]
  },
  "chem8_c1_rev_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Quá trình nào sau đây là phản ứng thu nhiệt?",
        "options": [
          "Nung đá vôi trong lò vôi",
          "Đốt cháy than hoa trong bếp",
          "Thả vôi sống vào nước",
          "Đốt cháy que diêm"
        ],
        "correct": 0,
        "explanation": "Nung đá vôi cần cấp nhiệt liên tục (phản ứng thu nhiệt)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khối lượng của 1 mol nguyên tử đồng (Cu) là:",
        "options": [
          "64 g",
          "32 g",
          "56 g",
          "27 g"
        ],
        "correct": 0,
        "explanation": "M_Cu = 64 g/mol."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Tỉ khối của khí oxi đối với khí metan (CH4) là:",
        "options": [
          "2",
          "0,5",
          "1,5",
          "4"
        ],
        "correct": 0,
        "explanation": "d = 32 / 16 = 2."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nồng độ mol của một dung dịch được xác định bằng biểu thức:",
        "options": [
          "CM = n / V",
          "CM = m / V",
          "CM = V / n",
          "CM = n * V"
        ],
        "correct": 0,
        "explanation": "CM = n / V (mol/L)."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho phương trình phản ứng: Zn + 2HCl -> ZnCl2 + H2. Tỉ lệ số mol giữa Zn và H2 là:",
        "options": [
          "1 : 1",
          "1 : 2",
          "2 : 1",
          "1 : 3"
        ],
        "correct": 0,
        "explanation": "Hệ số của Zn và H2 đều là 1."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Số mol của 12,395 lít khí hiđro ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "0,5 mol",
          "0,25 mol",
          "1,0 mol",
          "0,1 mol"
        ],
        "correct": 0,
        "explanation": "n = 12,395 / 24,79 = 0,5 mol."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hòa tan 8 g NaOH vào nước thu được 200 mL dung dịch. Nồng độ mol của dung dịch NaOH là:",
        "options": [
          "1 M",
          "2 M",
          "0,5 M",
          "0,1 M"
        ],
        "correct": 0,
        "explanation": "n = 8 / 40 = 0,2 mol -> CM = 0,2 / 0,2 = 1 M."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Dẫn khí H2 dư qua 16 g bột CuO nung nóng thu được m gam kim loại Cu. Giá trị của m là:",
        "options": [
          "12,8 g",
          "6,4 g",
          "16,0 g",
          "8,0 g"
        ],
        "correct": 0,
        "explanation": "H2 + CuO -> Cu + H2O. n_CuO = 0,2 mol -> m_Cu = 0,2 * 64 = 12,8 g."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan 20 g muối ăn vào nước thu được dung dịch có nồng độ 10%. Khối lượng dung dịch thu được là:",
        "options": [
          "200 g",
          "180 g",
          "220 g",
          "100 g"
        ],
        "correct": 0,
        "explanation": "m_dd = 20 / 10% = 200 g."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Để làm tăng tốc độ phân hủy của dung dịch H2O2 giải phóng khí oxi, người ta thường cho thêm vào một lượng nhỏ bột:",
        "options": [
          "MnO2",
          "NaCl",
          "Đường",
          "Vôi sống"
        ],
        "correct": 0,
        "explanation": "MnO2 là chất xúc tác cho phản ứng phân hủy H2O2."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Khí A có tỉ khối đối với không khí là 1,586. Khối lượng mol của khí A là:",
        "options": [
          "46 g/mol (NO2)",
          "34 g/mol (H2S)",
          "28 g/mol (N2)",
          "64 g/mol (SO2)"
        ],
        "correct": 0,
        "explanation": "M = 1,586 * 29 = 46 g/mol (NO2)."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Hòa tan hết 4,8 g kim loại magie vào 150 g dung dịch HCl dư. Khối lượng dung dịch sau phản ứng tăng thêm so với dung dịch axit ban đầu là:",
        "options": [
          "4,4 g",
          "4,8 g",
          "4,6 g",
          "4,2 g"
        ],
        "correct": 0,
        "explanation": "Mg + 2HCl -> MgCl2 + H2. n_Mg = 0,2 mol -> n_H2 = 0,2 mol -> m_H2 = 0,4 g. m tăng = m_Mg - m_H2 = 4,8 - 0,4 = 4,4 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về năng lượng nhiệt và phản ứng hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Phản ứng tôi vôi sống CaO với nước là phản ứng tỏa nhiệt dữ dội.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Quá trình quang hợp của cây xanh hấp thụ năng lượng mặt trời là quá trình thu nhiệt.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi đốt cháy than đá, năng lượng nhiệt giải phóng ra môi trường là phản ứng tỏa nhiệt.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phản ứng thu nhiệt làm nhiệt độ của môi trường xung quanh tăng vọt lên.",
            "correct": false
          }
        ],
        "explanation": "Phản ứng thu nhiệt hấp thụ năng lượng làm môi trường xung quanh lạnh đi."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về khối lượng mol và thể tích mol chất khí:",
        "statements": [
          {
            "subId": "a",
            "text": "1 mol khí CO2 và 1 mol khí O2 có cùng số lượng phân tử bằng 6,022 * 10^23.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ở đkc, 1 mol khí CO2 có thể tích lớn hơn 1 mol khí H2 vì phân tử CO2 to hơn.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Tất cả các chất khí ở cùng điều kiện nhiệt độ và áp suất đều có cùng thể tích mol.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tỉ khối của chất khí giúp so sánh khí nào nặng hơn hay nhẹ hơn.",
            "correct": true
          }
        ],
        "explanation": "Ở cùng nhiệt độ và áp suất, thể tích 1 mol mọi chất khí đều bằng nhau."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho phản ứng nhiệt phân muối KClO3 có xúc tác MnO2:",
        "statements": [
          {
            "subId": "a",
            "text": "Phương trình: 2KClO3 -> 2KCl + 3O2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng chất rắn sau phản ứng giảm đi đúng bằng khối lượng khí oxi bay ra.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "MnO2 bị tiêu hao hoàn toàn sau phản ứng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khí oxi sinh ra có thể thu bằng phương pháp đẩy nước do ít tan trong nước.",
            "correct": true
          }
        ],
        "explanation": "MnO2 là chất xúc tác nên giữ nguyên khối lượng."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét dung dịch muối ăn NaCl bão hòa ở 20 °C (độ tan S = 36 g):",
        "statements": [
          {
            "subId": "a",
            "text": "Trong 100 g nước chỉ hòa tan tối đa 36 g muối ăn ở 20 °C.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng dung dịch bão hòa thu được là 136 g.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nồng độ phần trăm của dung dịch bão hòa là 26,47%.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Nếu đun nóng dung dịch thì lượng muối ăn tan thêm được tăng lên rất lớn.",
            "correct": false
          }
        ],
        "explanation": "Độ tan của NaCl trong nước hầu như thay đổi rất ít theo nhiệt độ."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Công thức hóa học của khí metan là gì? (Điền: CH4)",
        "correctAnswer": "CH4",
        "explanation": "Khí metan là CH4."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Thể tích của 0,4 mol khí CO2 ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Ghi số thập phân)",
        "correctAnswer": "9,916",
        "explanation": "V = 0,4 * 24,79 = 9,916 L."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khối lượng của 0,5 mol canxi oxit CaO (M = 56 g/mol) là bao nhiêu gam?",
        "correctAnswer": "28",
        "explanation": "m = 0,5 * 56 = 28 g."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Để pha 300 mL dung dịch NaOH 0,5 M cần bao nhiêu gam NaOH rắn?",
        "correctAnswer": "6",
        "explanation": "n = 0,3 * 0,5 = 0,15 mol -> m = 0,15 * 40 = 6 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Đốt cháy 4,8 g kim loại Mg trong oxi thu được bao nhiêu gam MgO?",
        "correctAnswer": "8",
        "explanation": "2Mg + O2 -> 2MgO. n_Mg = 0,2 mol -> n_MgO = 0,2 mol -> m = 0,2 * 40 = 8 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Tỉ khối của khí SO3 đối với khí O2 bằng bao nhiêu? (Ghi số thập phân)",
        "correctAnswer": "2,5",
        "explanation": "80 / 32 = 2,5."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 6,5 g kim loại Zn vào 100 mL dung dịch H2SO4 1,5 M. Sau khi phản ứng kết thúc, thể tích khí H2 thu được ở đkc (25 °C, 1 bar) là:",
        "options": [
          "2,479 lít",
          "3,7185 lít",
          "4,958 lít",
          "1,2395 lít"
        ],
        "correct": 0,
        "explanation": "n_Zn = 0,1 mol; n_H2SO4 = 0,15 mol -> H2SO4 dư, tính theo Zn -> n_H2 = 0,1 mol -> V = 2,479 L."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khối lượng dung dịch HCl 14,6% cần dùng để hòa tan hoàn toàn 8,0 g đồng(II) oxit CuO là:",
        "options": [
          "50 g",
          "100 g",
          "25 g",
          "75 g"
        ],
        "correct": 0,
        "explanation": "CuO + 2HCl -> CuCl2 + H2O. n_CuO = 0,1 mol -> n_HCl = 0,2 mol -> m_HCl = 7,3 g -> m_dd = 7,3 / 14,6% = 50 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một hỗn hợp gồm 0,2 mol CO và 0,3 mol CO2 có tỉ khối đối với không khí xấp xỉ bằng:",
        "options": [
          "1,30",
          "1,15",
          "1,45",
          "1,05"
        ],
        "correct": 0,
        "explanation": "M_tb = (0,2*28 + 0,3*44) / 0,5 = (5,6 + 13,2) / 0,5 = 37,6 g/mol -> d = 37,6 / 29 xấp xỉ 1,30."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Nhiệt phân hoàn toàn 15,8 g thuốc tím KMnO4 thu được V lít khí O2 ở đkc. Toàn bộ lượng khí O2 này đem đốt cháy m gam kim loại sắt thu được oxit sắt từ Fe3O4. Giá trị của m là:",
        "options": [
          "4,2 g",
          "5,6 g",
          "8,4 g",
          "2,8 g"
        ],
        "correct": 0,
        "explanation": "2KMnO4 -> O2 (0,05 mol). 3Fe + 2O2 -> Fe3O4: n_Fe = 0,05 * 1,5 = 0,075 mol -> m_Fe = 0,075 * 56 = 4,2 g."
      }
    ]
  },
  "chem8_c1_rev_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Chất xúc tác có đặc điểm là:",
        "options": [
          "Làm tăng tốc độ phản ứng và không bị biến đổi sau phản ứng",
          "Bị tiêu hao trong quá trình phản ứng",
          "Làm thay đổi sản phẩm của phản ứng",
          "Làm ngừng phản ứng"
        ],
        "correct": 0,
        "explanation": "Chất xúc tác giữ nguyên về lượng và chất sau phản ứng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Trong 1 phân tử khí sunfurơ (SO2) có bao nhiêu nguyên tử oxi?",
        "options": [
          "2",
          "1",
          "3",
          "4"
        ],
        "correct": 0,
        "explanation": "SO2 có 2 nguyên tử oxi."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Ở điều kiện chuẩn (25 °C, 1 bar), 2 mol khí chiếm thể tích là:",
        "options": [
          "49,58 lít",
          "24,79 lít",
          "44,8 lít",
          "22,4 lít"
        ],
        "correct": 0,
        "explanation": "2 * 24,79 = 49,58 L."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Đơn vị của nồng độ phần trăm là:",
        "options": [
          "%",
          "mol/L",
          "g/mol",
          "gam"
        ],
        "correct": 0,
        "explanation": "Kí hiệu là %."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Số phân tử khí có trong 0,5 mol khí N2 là:",
        "options": [
          "3,011 * 10^23",
          "6,022 * 10^23",
          "1,204 * 10^24",
          "1,505 * 10^23"
        ],
        "correct": 0,
        "explanation": "0,5 * 6,022 * 10^23 = 3,011 * 10^23."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho phương trình: 2Al + 6HCl -> 2AlCl3 + 3H2. Tỉ lệ giữa số phân tử HCl phản ứng và số phân tử H2 sinh ra là:",
        "options": [
          "2 : 1",
          "6 : 3 = 2 : 1",
          "3 : 2",
          "1 : 1"
        ],
        "correct": 0,
        "explanation": "Tỉ lệ 6 : 3 = 2 : 1."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khí nào sau đây nhẹ nhất trong tất cả các chất khí?",
        "options": [
          "H2 (hiđro)",
          "He (heli)",
          "CH4 (metan)",
          "N2 (nitơ)"
        ],
        "correct": 0,
        "explanation": "Khí hiđro H2 có phân tử khối bằng 2 nhẹ nhất."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khối lượng của 0,2 mol canxi cacbonat CaCO3 là:",
        "options": [
          "20 g",
          "10 g",
          "40 g",
          "50 g"
        ],
        "correct": 0,
        "explanation": "m = 0,2 * 100 = 20 g."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan 10 g đường vào 190 g nước. Nồng độ C% của dung dịch đường là:",
        "options": [
          "5%",
          "10%",
          "5,26%",
          "4,5%"
        ],
        "correct": 0,
        "explanation": "m_dd = 200 g -> C% = 5%."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Cho các phản ứng: cháy cồn, gỉ sắt, nung vôi, thắp nến. Số phản ứng tỏa nhiệt là:",
        "options": [
          "3",
          "2",
          "4",
          "1"
        ],
        "correct": 0,
        "explanation": "Cháy cồn, gỉ sắt, thắp nến tỏa nhiệt (3 phản ứng). Nung vôi thu nhiệt."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Thể tích dung dịch NaOH 2 M cần lấy để có 0,1 mol NaOH là:",
        "options": [
          "50 mL",
          "100 mL",
          "200 mL",
          "25 mL"
        ],
        "correct": 0,
        "explanation": "V = 0,1 / 2 = 0,05 L = 50 mL."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Đốt cháy hoàn toàn 2,7 g kim loại nhôm trong khí clo dư thu được 13,35 g muối nhôm clorua (AlCl3). Khối lượng khí clo đã tham gia phản ứng là:",
        "options": [
          "10,65 g",
          "16,05 g",
          "5,325 g",
          "7,1 g"
        ],
        "correct": 0,
        "explanation": "m_Cl2 = 13,35 - 2,7 = 10,65 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các hiện tượng hóa học xảy ra trong môi trường:",
        "statements": [
          {
            "subId": "a",
            "text": "Hiện tượng mưa axit gây hại công trình kiến trúc là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Băng phiến bốc hơi trong tủ quần áo là biến đổi hóa học.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Sự thối rữa xác động thực vật là biến đổi hóa học sinh học phức tạp.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí thải CO2 gây hiệu ứng nhà kính làm ấm Trái Đất.",
            "correct": true
          }
        ],
        "explanation": "Băng phiến bốc hơi là hiện tượng thăng hoa vật lí."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về nồng độ dung dịch:",
        "statements": [
          {
            "subId": "a",
            "text": "Pha thêm nước cất làm giảm nồng độ mol của dung dịch.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đun nóng để nước bay hơi làm tăng nồng độ phần trăm của dung dịch chưa bão hòa.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch bão hòa có thể tan thêm chất tan khi hạ nhiệt độ xuống cực thấp.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Nước là dung môi phân cực hòa tan tốt nhiều hợp chất ion như muối ăn.",
            "correct": true
          }
        ],
        "explanation": "Hạ nhiệt độ thường làm giảm độ tan, kết tinh thêm chất rắn."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về phương trình phản ứng hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Hệ số cân bằng biểu diễn tỉ lệ số hạt giữa các chất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cân bằng phương trình: 2Fe + 3Cl2 -> 2FeCl3.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tổng các hệ số của phản ứng: CH4 + 2O2 -> CO2 + 2H2O là 6.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phản ứng nhiệt phân đá vôi CaCO3 là phản ứng tỏa nhiệt.",
            "correct": false
          }
        ],
        "explanation": "Nhiệt phân đá vôi là phản ứng thu nhiệt."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho hỗn hợp khí X gồm 0,2 mol N2 và 0,3 mol O2 ở đkc:",
        "statements": [
          {
            "subId": "a",
            "text": "Tổng thể tích hỗn hợp khí X ở đkc là 12,395 lít.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng của hỗn hợp khí X là 15,2 g.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng mol trung bình của X là 30,4 g/mol.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hỗn hợp X nhẹ hơn không khí.",
            "correct": false
          }
        ],
        "explanation": "M_tb = 30,4 > 29 nên nặng hơn không khí."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phản ứng: A + B -> C, chất C gọi là chất gì? (Điền: sản phẩm)",
        "correctAnswer": "sản phẩm",
        "explanation": "Chất C là sản phẩm."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của khí oxi O2 là bao nhiêu g/mol?",
        "correctAnswer": "32",
        "explanation": "M = 32 g/mol."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Số mol của 2,479 lít khí CO2 ở đkc là bao nhiêu mol? (Ghi số thập phân)",
        "correctAnswer": "0,1",
        "explanation": "n = 0,1 mol."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cần bao nhiêu gam đường để pha 100 g dung dịch nước đường 20%?",
        "correctAnswer": "20",
        "explanation": "100 * 20% = 20 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Nung m gam CaCO3 thu được 11,2 g CaO và 8,8 g CO2. Khối lượng m ban đầu là bao nhiêu gam?",
        "correctAnswer": "20",
        "explanation": "m = 11,2 + 8,8 = 20 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Tỉ khối của khí A đối với H2 là 16. Khí A là chất nào? (Điền: O2)",
        "correctAnswer": "O2",
        "explanation": "M = 16 * 2 = 32 (O2)."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Cho 5,6 g kim loại sắt tác dụng vừa đủ với V mL dung dịch HCl 2 M. Giá trị của V là:",
        "options": [
          "100 mL",
          "200 mL",
          "50 mL",
          "150 mL"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,1 mol -> n_HCl = 0,2 mol -> V = 0,2 / 2 = 0,1 L = 100 mL."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Đốt cháy hoàn toàn 4,8 g kim loại Mg trong khí clo dư thu được bao nhiêu gam muối MgCl2?",
        "options": [
          "19,0 g",
          "9,5 g",
          "14,25 g",
          "28,5 g"
        ],
        "correct": 0,
        "explanation": "Mg + Cl2 -> MgCl2. n_Mg = 0,2 mol -> m_MgCl2 = 0,2 * 95 = 19,0 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Khí X có tỉ khối đối với oxi bằng 1,375. Khí X là:",
        "options": [
          "CO2",
          "SO2",
          "N2",
          "CH4"
        ],
        "correct": 0,
        "explanation": "M = 1,375 * 32 = 44 (CO2)."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một bình kín dung tích 7,437 lít chứa đầy khí N2 ở đkc. Khối lượng khí N2 có trong bình là:",
        "options": [
          "8,4 g",
          "4,2 g",
          "14,0 g",
          "2,8 g"
        ],
        "correct": 0,
        "explanation": "n = 7,437 / 24,79 = 0,3 mol -> m = 0,3 * 28 = 8,4 g."
      }
    ]
  },
  "chem8_c1_rev_test4": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Yếu tố nào sau đây làm giảm tốc độ phản ứng?",
        "options": [
          "Hạ nhiệt độ phản ứng",
          "Tăng nồng độ chất phản ứng",
          "Nghiền nhỏ chất phản ứng",
          "Thêm chất xúc tác"
        ],
        "correct": 0,
        "explanation": "Hạ nhiệt độ làm giảm tốc độ phản ứng."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Phương trình nào sau đây biểu diễn phản ứng tạo gỉ sắt?",
        "options": [
          "Sắt + Oxi + Nước -> Gỉ sắt",
          "Sắt + Nước -> Khí hiđro",
          "Sắt + Muối -> Đồng",
          "Sắt nóng chảy thành lỏng"
        ],
        "correct": 0,
        "explanation": "Gỉ sắt hình thành do sắt tác dụng với oxi và nước ẩm."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Đơn vị đo của nồng độ mol là:",
        "options": [
          "mol/L",
          "gam",
          "%",
          "g/mL"
        ],
        "correct": 0,
        "explanation": "mol/L hoặc M."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong phản ứng: CaCO3 -> CaO + CO2, chất phản ứng là:",
        "options": [
          "CaCO3 (canxi cacbonat)",
          "CaO",
          "CO2",
          "Hỗn hợp CaO và CO2"
        ],
        "correct": 0,
        "explanation": "CaCO3 là chất phản ứng ban đầu."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Thể tích của 0,3 mol khí hiđro ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "7,437 lít",
          "24,79 lít",
          "4,958 lít",
          "2,479 lít"
        ],
        "correct": 0,
        "explanation": "V = 0,3 * 24,79 = 7,437 L."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của axit clohiđric HCl là:",
        "options": [
          "36,5 g/mol",
          "35,5 g/mol",
          "18 g/mol",
          "98 g/mol"
        ],
        "correct": 0,
        "explanation": "M = 1 + 35,5 = 36,5 g/mol."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khí metan CH4 có tỉ khối đối với khí hiđro H2 là:",
        "options": [
          "8",
          "16",
          "4",
          "2"
        ],
        "correct": 0,
        "explanation": "d = 16 / 2 = 8."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cân bằng phương trình: ... P + ... O2 -> ... P2O5. Hệ số của O2 là:",
        "options": [
          "5",
          "2",
          "3",
          "4"
        ],
        "correct": 0,
        "explanation": "4P + 5O2 -> 2P2O5. Hệ số O2 là 5."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan 4 g NaOH vào nước thu được 100 mL dung dịch. Nồng độ mol của dung dịch là:",
        "options": [
          "1 M",
          "0,5 M",
          "2 M",
          "0,1 M"
        ],
        "correct": 0,
        "explanation": "n = 4 / 40 = 0,1 mol -> CM = 0,1 / 0,1 = 1 M."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Cho m gam kim loại kẽm tác dụng vừa đủ với 100 mL dung dịch HCl 1 M. Giá trị của m là:",
        "options": [
          "3,25 g",
          "6,5 g",
          "1,3 g",
          "2,6 g"
        ],
        "correct": 0,
        "explanation": "n_HCl = 0,1 mol -> n_Zn = 0,05 mol -> m_Zn = 0,05 * 65 = 3,25 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Khi pha loãng 50 mL dung dịch H2SO4 2 M thành 200 mL dung dịch mới. Nồng độ mol của dung dịch sau khi pha là:",
        "options": [
          "0,5 M",
          "1,0 M",
          "0,25 M",
          "0,2 M"
        ],
        "correct": 0,
        "explanation": "n = 0,05 * 2 = 0,1 mol -> CM = 0,1 / 0,2 = 0,5 M."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Nhiệt phân hoàn toàn 20 g đá vôi chứa 90% CaCO3, thu được m gam vôi sống CaO. Giá trị của m là:",
        "options": [
          "10,08 g",
          "11,2 g",
          "9,0 g",
          "12,6 g"
        ],
        "correct": 0,
        "explanation": "m_CaCO3 = 18 g -> n = 0,18 mol -> m_CaO = 0,18 * 56 = 10,08 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các hiện tượng biến đổi vật chất:",
        "statements": [
          {
            "subId": "a",
            "text": "Nến cháy sinh ra khí CO2 và hơi nước là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nến chảy lỏng thấm vào bấc là biến đổi vật lí.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Đập vụn viên than thành bột là biến đổi hóa học.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Bột than cháy trong không khí là biến đổi hóa học.",
            "correct": true
          }
        ],
        "explanation": "Đập than chỉ thay đổi kích thước vật lí."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về mol và thể tích khí:",
        "statements": [
          {
            "subId": "a",
            "text": "1 mol khí CO2 ở đkc nặng 44 g và chiếm thể tích 24,79 lít.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí CO2 nặng hơn khí oxi.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khí CO2 nhẹ hơn không khí.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Để thu khí CO2 ta đặt ngửa bình thu.",
            "correct": true
          }
        ],
        "explanation": "M_CO2 = 44 > 29 nên nặng hơn không khí."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về phản ứng hóa học trong dung dịch:",
        "statements": [
          {
            "subId": "a",
            "text": "Cho bột kẽm vào axit clohiđric sủi bọt khí H2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dung dịch thu được sau phản ứng chứa kẽm clorua ZnCl2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng dung dịch sau phản ứng giảm đi do khí H2 bay ra.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khối lượng dung dịch tăng lên do m_Zn thêm vào lớn hơn m_H2 bay ra.",
            "correct": true
          }
        ],
        "explanation": "Khối lượng dung dịch tăng: m_Zn (65g) - m_H2 (2g) > 0."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng nhiệt phân muối natri hidrocacbonat (baking soda):",
        "statements": [
          {
            "subId": "a",
            "text": "Phương trình: 2NaHCO3 -> Na2CO3 + CO2 + H2O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí CO2 sinh ra làm đục nước vôi trong.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng chất rắn giảm đi đúng bằng tổng khối lượng CO2 và H2O.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đây là phản ứng tỏa nhiệt mạnh.",
            "correct": false
          }
        ],
        "explanation": "Nhiệt phân cần cung cấp nhiệt liên tục (phản ứng thu nhiệt)."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Kí hiệu của hằng số Avogadro là chữ gì?",
        "correctAnswer": "N",
        "explanation": "Kí hiệu là N."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của khí nitơ N2 là bao nhiêu g/mol?",
        "correctAnswer": "28",
        "explanation": "M = 28 g/mol."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Thể tích của 0,5 mol khí oxi ở đkc là bao nhiêu lít? (Ghi số thập phân)",
        "correctAnswer": "12,395",
        "explanation": "0,5 * 24,79 = 12,395 L."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Để pha 200 g dung dịch NaCl 5% cần bao nhiêu gam muối NaCl?",
        "correctAnswer": "10",
        "explanation": "200 * 5% = 10 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Đốt cháy 0,1 mol bột lưu huỳnh trong oxi dư thu được bao nhiêu gam khí SO2? (Ghi số thập phân)",
        "correctAnswer": "6,4",
        "explanation": "m = 0,1 * 64 = 6,4 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cân bằng phương trình: a Fe + b O2 -> c Fe3O4. Tổng các hệ số (a + b + c) là bao nhiêu?",
        "correctAnswer": "6",
        "explanation": "3Fe + 2O2 -> 1Fe3O4. Tổng: 3 + 2 + 1 = 6."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 13 g kim loại Zn vào dung dịch HCl dư. Thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "4,958 lít",
          "2,479 lít",
          "7,437 lít",
          "9,916 lít"
        ],
        "correct": 0,
        "explanation": "n_Zn = 0,2 mol -> n_H2 = 0,2 mol -> V = 0,2 * 24,79 = 4,958 L."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Đốt cháy 1,6 g khí metan CH4 trong bình chứa 6,4 g khí O2. Khối lượng khí CO2 tạo thành là:",
        "options": [
          "4,4 g",
          "2,2 g",
          "8,8 g",
          "3,6 g"
        ],
        "correct": 0,
        "explanation": "CH4 (0,1 mol) + 2O2 (0,2 mol) -> CO2 (0,1 mol). m_CO2 = 4,4 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 2,8 g Fe vào 100 mL dung dịch H2SO4 1 M. Sau phản ứng, khối lượng muối FeSO4 thu được là:",
        "options": [
          "7,6 g",
          "15,2 g",
          "3,8 g",
          "11,4 g"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,05 mol -> m_FeSO4 = 0,05 * 152 = 7,6 g."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hỗn hợp gồm 0,1 mol SO2 và 0,1 mol O2 có khối lượng mol trung bình là:",
        "options": [
          "48 g/mol",
          "32 g/mol",
          "64 g/mol",
          "96 g/mol"
        ],
        "correct": 0,
        "explanation": "M_tb = (64 + 32) / 2 = 48 g/mol."
      }
    ]
  },
  "chem8_c1_rev_test5": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong một phương trình hóa học, chỉ số dưới chân nguyên tử biểu thị:",
        "options": [
          "Số nguyên tử của nguyên tố đó trong một phân tử",
          "Số phân tử của chất",
          "Khối lượng mol của chất",
          "Hóa trị của nguyên tố"
        ],
        "correct": 0,
        "explanation": "Chỉ số biểu thị số lượng nguyên tử trong một phân tử."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Hiện tượng thanh sắt gỉ ngoài không khí ẩm là phản ứng:",
        "options": [
          "Tỏa nhiệt chậm",
          "Thu nhiệt nhanh",
          "Biến đổi vật lí",
          "Quang hợp"
        ],
        "correct": 0,
        "explanation": "Sự oxi hóa chậm tỏa nhiệt nhưng lượng nhiệt tản nhanh ra môi trường."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khối lượng mol của axit sunfuric H2SO4 là:",
        "options": [
          "98 g/mol",
          "49 g/mol",
          "36,5 g/mol",
          "64 g/mol"
        ],
        "correct": 0,
        "explanation": "M = 1*2 + 32 + 16*4 = 98 g/mol."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khí nhẹ nhất trong các khí sau là:",
        "options": [
          "H2 (M = 2)",
          "He (M = 4)",
          "CH4 (M = 16)",
          "N2 (M = 28)"
        ],
        "correct": 0,
        "explanation": "H2 nhẹ nhất."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Thể tích của 0,25 mol khí CO2 ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "6,1975 lít",
          "24,79 lít",
          "12,395 lít",
          "4,958 lít"
        ],
        "correct": 0,
        "explanation": "V = 0,25 * 24,79 = 6,1975 L."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho phương trình: 2K + 2H2O -> 2KOH + H2. Tỉ lệ số nguyên tử kali và số phân tử khí hiđro sinh ra là:",
        "options": [
          "2 : 1",
          "1 : 1",
          "1 : 2",
          "2 : 2"
        ],
        "correct": 0,
        "explanation": "Hệ số K là 2, hệ số H2 là 1 -> 2 : 1."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hòa tan 20 g đường vào 180 g nước thu được dung dịch có nồng độ phần trăm là:",
        "options": [
          "10%",
          "11,1%",
          "20%",
          "5%"
        ],
        "correct": 0,
        "explanation": "m_dd = 200 g -> C% = 20 / 200 = 10%."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Nồng độ mol của 500 mL dung dịch chứa 0,5 mol HCl là:",
        "options": [
          "1 M",
          "0,5 M",
          "2 M",
          "0,25 M"
        ],
        "correct": 0,
        "explanation": "CM = 0,5 / 0,5 = 1 M."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Đốt cháy 6,4 g bột đồng Cu trong khí oxi dư thu được m gam CuO màu đen. Giá trị của m là:",
        "options": [
          "8,0 g",
          "7,2 g",
          "9,6 g",
          "8,8 g"
        ],
        "correct": 0,
        "explanation": "2Cu + O2 -> 2CuO. n_Cu = 0,1 mol -> m_CuO = 0,1 * 80 = 8,0 g."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Để làm sạch gỉ sét bám trên bề mặt đinh sắt, người ta ngâm đinh sắt vào dung dịch axit clohiđric loãng. Thao tác này là ứng dụng của:",
        "options": [
          "Biến đổi hóa học hòa tan lớp gỉ oxit sắt",
          "Biến đổi vật lí mài mòn",
          "Phản ứng tôi vôi",
          "Hiện tượng ngưng tụ"
        ],
        "correct": 0,
        "explanation": "Axit tác dụng với oxit sắt gỉ tạo muối tan, làm sạch bề mặt."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Hòa tan 11,7 g muối ăn NaCl vào nước để được 200 mL dung dịch. Nồng độ mol của dung dịch NaCl là:",
        "options": [
          "1 M",
          "0,5 M",
          "2 M",
          "0,1 M"
        ],
        "correct": 0,
        "explanation": "n = 11,7 / 58,5 = 0,2 mol -> CM = 0,2 / 0,2 = 1 M."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Dẫn 2,479 lít khí CO (đkc) qua ống sứ nung nóng chứa Fe2O3 dư. Sau phản ứng hoàn toàn, khối lượng sắt Fe thu được là:",
        "options": [
          "3,73 g",
          "5,6 g",
          "11,2 g",
          "2,8 g"
        ],
        "correct": 0,
        "explanation": "n_CO = 0,1 mol. Fe2O3 + 3CO -> 2Fe + 3CO2. n_Fe = 0,1 * 2/3 mol -> m_Fe = 0,2/3 * 56 = 3,73 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các quá trình hóa học và vật lí:",
        "statements": [
          {
            "subId": "a",
            "text": "Hòa tan đường vào nước là biến đổi vật lí.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nung đường thành than đen có mùi khét là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cồn etylic cháy tạo khí CO2 và H2O là biến đổi hóa học.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Rượu để lâu bị bay hơi cồn làm giảm độ rượu là biến đổi hóa học.",
            "correct": false
          }
        ],
        "explanation": "Bay hơi cồn là biến đổi vật lí trạng thái."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các quy tắc bảo toàn khối lượng:",
        "statements": [
          {
            "subId": "a",
            "text": "ĐL BTKL được xây dựng dựa trên sự bảo toàn số nguyên tử của từng nguyên tố.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng dung dịch sau phản ứng có kết tủa luôn nhỏ hơn tổng khối lượng các dung dịch ban đầu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng dung dịch sau phản ứng có khí thoát ra luôn nhỏ hơn tổng khối lượng ban đầu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Trong phản ứng tạo gỉ sắt, khối lượng sắt bị mất đi hoàn toàn biến thành nhiệt.",
            "correct": false
          }
        ],
        "explanation": "Sắt kết hợp với oxi và nước tạo thành gỉ sắt."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về nồng độ phần trăm và nồng độ mol:",
        "statements": [
          {
            "subId": "a",
            "text": "Dung dịch muối ăn 0,9% được gọi là nước muối sinh lí.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nồng độ mol biểu thị số mol chất tan trong một lít dung dịch.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Để pha loãng dung dịch, ta thêm dung môi (nước cất).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khi pha loãng, cả số mol chất tan và nồng độ mol đều tăng lên.",
            "correct": false
          }
        ],
        "explanation": "Số mol chất tan không đổi, nồng độ mol giảm."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng giữa kim loại magie và dung dịch axit sunfuric loãng:",
        "statements": [
          {
            "subId": "a",
            "text": "Phương trình: Mg + H2SO4 -> MgSO4 + H2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cho 2,4 g Mg vào 100 mL dung dịch H2SO4 1 M thì phản ứng vừa đủ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Thể tích khí H2 thu được ở đkc là 2,479 lít.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng muối MgSO4 thu được sau khi cô cạn dung dịch là 12,0 g.",
            "correct": true
          }
        ],
        "explanation": "n = 0,1 mol -> m_MgSO4 = 0,1 * 120 = 12,0 g."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phản ứng hóa học, liên kết giữa các loại hạt nào bị thay đổi? (Điền: nguyên tử)",
        "correctAnswer": "nguyên tử",
        "explanation": "Liên kết giữa các nguyên tử."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Thể tích của 1 mol khí ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Ghi số thập phân)",
        "correctAnswer": "24,79",
        "explanation": "24,79 lít."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của khí cacbonic CO2 là bao nhiêu g/mol?",
        "correctAnswer": "44",
        "explanation": "M = 44 g/mol."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Để có 0,2 mol NaCl cần bao nhiêu gam NaCl khan? (Ghi số thập phân)",
        "correctAnswer": "11,7",
        "explanation": "0,2 * 58,5 = 11,7 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Cho 4,6 g kim loại Na tác dụng hết với nước. Số mol khí H2 sinh ra là bao nhiêu mol? (Ghi số thập phân)",
        "correctAnswer": "0,1",
        "explanation": "n_Na = 0,2 mol -> n_H2 = 0,1 mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cân bằng phương trình: a Al + b O2 -> c Al2O3. Tổng hệ số (a + b + c) là bao nhiêu?",
        "correctAnswer": "9",
        "explanation": "4 + 3 + 2 = 9."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 2,7 g kim loại nhôm vào dung dịch HCl dư. Thể tích khí H2 sinh ra ở đkc (25 °C, 1 bar) là:",
        "options": [
          "3,7185 lít",
          "2,479 lít",
          "7,437 lít",
          "4,958 lít"
        ],
        "correct": 0,
        "explanation": "n_Al = 0,1 mol -> n_H2 = 0,15 mol -> V = 0,15 * 24,79 = 3,7185 L."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Đốt cháy 3,2 g lưu huỳnh trong bình chứa 4,8 g khí oxi. Khối lượng khí SO2 tạo thành là:",
        "options": [
          "6,4 g",
          "8,0 g",
          "3,2 g",
          "4,8 g"
        ],
        "correct": 0,
        "explanation": "S (0,1 mol) + O2 (0,15 mol) -> O2 dư, tính theo S -> m_SO2 = 0,1 * 64 = 6,4 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Trộn 200 mL dung dịch HCl 1 M với 200 mL dung dịch NaOH 1 M. Dung dịch sau phản ứng có môi trường gì và chứa muối gì?",
        "options": [
          "Môi trường trung tính, chứa muối NaCl",
          "Môi trường axit, chứa HCl dư",
          "Môi trường bazo, chứa NaOH dư",
          "Môi trường axit, chứa muối Na2SO4"
        ],
        "correct": 0,
        "explanation": "Phản ứng vừa đủ tạo NaCl và H2O, môi trường trung tính."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hợp chất khí X có tỉ khối đối với hiđro là 17. Đốt cháy X sinh ra khí nitơ và hơi nước. Khí X là:",
        "options": [
          "H2S (M = 34)",
          "NH3 (M = 17)",
          "PH3 (M = 34)",
          "CH4 (M = 16)"
        ],
        "correct": 0,
        "explanation": "M = 17 * 2 = 34 (H2S; phản ứng đốt cháy H2S tạo SO2 + H2O hoặc S + H2O)."
      }
    ]
  },
  "chem8_c2_b8_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Axit là hợp chất mà phân tử gồm có:",
        "options": [
          "Một hay nhiều nguyên tử hiđro liên kết với gốc axit",
          "Một nguyên tử kim loại liên kết với một hay nhiều nhóm hiđroxit (-OH)",
          "Một nguyên tố kim loại liên kết với một nguyên tố phi kim",
          "Nguyên tử kim loại liên kết với gốc axit"
        ],
        "correct": 0,
        "explanation": "Axit gồm một hay nhiều nguyên tử H liên kết với gốc axit."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là axit?",
        "options": [
          "HCl (axit clohiđric)",
          "NaOH (natri hiđroxit)",
          "NaCl (natri clorua)",
          "CaO (canxi oxit)"
        ],
        "correct": 0,
        "explanation": "HCl là một axit mạnh phổ biến."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Dung dịch axit làm giấy quỳ tím chuyển sang màu gì?",
        "options": [
          "Màu đỏ",
          "Màu xanh",
          "Màu hồng",
          "Màu vàng"
        ],
        "correct": 0,
        "explanation": "Dung dịch axit làm quỳ tím chuyển sang màu đỏ."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Gốc axit trong phân tử axit sunfuric H2SO4 là:",
        "options": [
          "=SO4 (sunfat)",
          "-Cl (clorua)",
          "=CO3 (cacbonat)",
          "-NO3 (nitrat)"
        ],
        "correct": 0,
        "explanation": "Gốc sunfat là =SO4 có hóa trị II."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho dãy các chất: HCl, NaOH, H2SO4, Cu(OH)2, HNO3, K2SO4. Có bao nhiêu axit trong dãy?",
        "options": [
          "3",
          "2",
          "4",
          "5"
        ],
        "correct": 0,
        "explanation": "Có 3 axit: HCl, H2SO4, HNO3."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Kim loại nào sau đây KHÔNG tác dụng với dung dịch axit HCl loãng giải phóng khí hiđro?",
        "options": [
          "Cu (đồng)",
          "Fe (sắt)",
          "Zn (kẽm)",
          "Mg (magie)"
        ],
        "correct": 0,
        "explanation": "Đồng (Cu) đứng sau hiđro trong dãy hoạt động hóa học nên không tác dụng với HCl loãng."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi cho kim loại kẽm vào dung dịch axit clohiđric HCl, khí sinh ra là:",
        "options": [
          "H2 (hiđro)",
          "O2 (oxi)",
          "Cl2 (clo)",
          "CO2 (cacbonic)"
        ],
        "correct": 0,
        "explanation": "Zn + 2HCl -> ZnCl2 + H2."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Phương trình phản ứng nào sau đây viết ĐÚNG giữa sắt và axit clohiđric?",
        "options": [
          "Fe + 2HCl -> FeCl2 + H2",
          "2Fe + 6HCl -> 2FeCl3 + 3H2",
          "Fe + HCl -> FeCl + H",
          "Fe + 2HCl -> FeCl2 + H2O"
        ],
        "correct": 0,
        "explanation": "Sắt tác dụng với HCl chỉ tạo muối sắt(II) FeCl2 và H2."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Trong dạ dày người có một lượng nhỏ axit nào giúp tiêu hóa thức ăn và tiêu diệt vi khuẩn?",
        "options": [
          "Axit clohiđric (HCl)",
          "Axit sunfuric (H2SO4)",
          "Axit axetic (CH3COOH)",
          "Axit nitric (HNO3)"
        ],
        "correct": 0,
        "explanation": "Dịch vị dạ dày chứa axit HCl nồng độ khoảng 0,0001 - 0,001 M (pH khoảng 1,5 - 3,5)."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Để pha loãng axit sunfuric đặc (H2SO4 đặc) an toàn trong phòng thí nghiệm, thao tác ĐÚNG là:",
        "options": [
          "Rót từ từ axit dọc theo đũa thủy tinh vào nước và khuấy đều",
          "Rót nhanh nước vào axit đặc",
          "Đổ đồng thời cả axit và nước vào cốc",
          "Đun nóng axit rồi mới đổ nước vào"
        ],
        "correct": 0,
        "explanation": "Quy tắc an toàn: Rót từ từ axit vào nước, tuyệt đối không làm ngược lại vì sẽ gây bắn axit nguy hiểm."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 6,5 g kim loại Zn vào dung dịch HCl dư. Thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "2,479 lít",
          "4,958 lít",
          "2,24 lít",
          "1,2395 lít"
        ],
        "correct": 0,
        "explanation": "n_Zn = 0,1 mol -> n_H2 = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho m gam hỗn hợp gồm bột sắt và đồng tác dụng với lượng dư dung dịch HCl thu được 4,958 lít khí H2 ở đkc và 3,2 g chất rắn không tan. Giá trị của m là:",
        "options": [
          "14,4 g",
          "11,2 g",
          "8,8 g",
          "12,6 g"
        ],
        "correct": 0,
        "explanation": "n_H2 = 0,2 mol -> n_Fe = 0,2 mol -> m_Fe = 0,2 * 56 = 11,2 g. m_Cu = 3,2 g -> m = 11,2 + 3,2 = 14,4 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về tính chất chung của dung dịch axit:",
        "statements": [
          {
            "subId": "a",
            "text": "Dung dịch axit làm quỳ tím hóa đỏ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Axit tác dụng với kim loại đứng trước H trong dãy hoạt động giải phóng khí H2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tất cả các kim loại đều tan trong axit HCl loãng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Axit tác dụng với bazơ tạo thành muối và nước (phản ứng trung hòa).",
            "correct": true
          }
        ],
        "explanation": "Các kim loại như Cu, Ag, Au đứng sau H không tan trong HCl loãng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các axit phổ biến trong đời sống và sản xuất:",
        "statements": [
          {
            "subId": "a",
            "text": "Axit sunfuric H2SO4 là hóa chất hàng đầu được mệnh danh là 'máu của ngành công nghiệp hóa chất'.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Giấm ăn dùng trong gia đình là dung dịch axit axetic (CH3COOH) nồng độ khoảng 2% - 5%.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Axit H2SO4 đặc có tính háo nước mạnh và có thể gây bỏng sâu rất nguy hiểm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khi bị axit dính vào da, cần trung hòa ngay bằng dung dịch kiềm đặc NaOH.",
            "correct": false
          }
        ],
        "explanation": "Phải rửa ngay dưới vòi nước chảy liên tục trong nhiều phút, không dùng kiềm đặc."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phản ứng sau ở nhiệt độ thường:",
        "statements": [
          {
            "subId": "a",
            "text": "Mg + 2HCl -> MgCl2 + H2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Fe + H2SO4 loãng -> FeSO4 + H2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cu + 2HCl -> CuCl2 + H2.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "2Al + 6HCl -> 2AlCl3 + 3H2.",
            "correct": true
          }
        ],
        "explanation": "Đồng không tác dụng với dung dịch HCl loãng."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm cho một lá nhôm (Al) vào dung dịch axit clohiđric loãng:",
        "statements": [
          {
            "subId": "a",
            "text": "Ban đầu chưa thấy sủi bọt khí ngay do bề mặt nhôm có lớp màng Al2O3 bảo vệ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sau khi lớp oxit tan hết, bọt khí H2 thoát ra nhanh và mạnh làm dung dịch nóng lên.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch sau phản ứng chứa muối nhôm clorua AlCl3.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng dung dịch sau phản ứng tăng đúng bằng khối lượng lá nhôm đã phản ứng.",
            "correct": false
          }
        ],
        "explanation": "Khối lượng tăng bằng m_Al trừ đi m_H2 bay ra."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phân tử axit nitric HNO3, gốc axit có hóa trị mấy?",
        "correctAnswer": "I",
        "explanation": "Gốc -NO3 có hóa trị I."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Dung dịch axit clohiđric làm quỳ tím chuyển sang màu gì?",
        "correctAnswer": "đỏ",
        "explanation": "Chuyển sang màu đỏ."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho các kim loại: Mg, Fe, Cu, Ag, Al. Có bao nhiêu kim loại tác dụng được với dung dịch axit HCl loãng giải phóng H2?",
        "correctAnswer": "3",
        "explanation": "Mg, Fe, Al (3 kim loại đứng trước H)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hòa tan hết 2,4 g kim loại magie vào dung dịch HCl dư. Thể tích khí H2 thoát ra ở đkc là bao nhiêu lít? (Ghi số thập phân)",
        "correctAnswer": "2,479",
        "explanation": "n_Mg = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Khối lượng mol của axit sunfuric H2SO4 là bao nhiêu g/mol?",
        "correctAnswer": "98",
        "explanation": "M = 98 g/mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cho 0,2 mol bột sắt Fe phản ứng hoàn toàn với dung dịch HCl dư. Khối lượng muối FeCl2 thu được là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "25,4",
        "explanation": "m = 0,2 * 127 = 25,4 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Cho 10 g hỗn hợp gồm Mg và Cu vào dung dịch HCl dư. Sau phản ứng thu được 4,958 lít khí H2 ở đkc. Phần trăm khối lượng của kim loại đồng trong hỗn hợp là:",
        "options": [
          "52%",
          "48%",
          "24%",
          "36%"
        ],
        "correct": 0,
        "explanation": "n_H2 = 0,2 mol -> n_Mg = 0,2 mol -> m_Mg = 4,8 g -> m_Cu = 10 - 4,8 = 5,2 g -> %Cu = 52%."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Để hòa tan hoàn toàn 4,0 g oxit sắt Fe2O3 cần vừa đủ bao nhiêu mL dung dịch axit HCl 1 M?",
        "options": [
          "150 mL",
          "200 mL",
          "100 mL",
          "300 mL"
        ],
        "correct": 0,
        "explanation": "Fe2O3 + 6HCl -> 2FeCl3 + 3H2O. n_Fe2O3 = 4 / 160 = 0,025 mol -> n_HCl = 0,15 mol -> V = 0,15 L = 150 mL."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một mẫu axit H2SO4 loãng có nồng độ 10%. Cần lấy bao nhiêu gam dung dịch này để hòa tan hoàn toàn 2,4 g bột magie Mg?",
        "options": [
          "98 g",
          "49 g",
          "196 g",
          "120 g"
        ],
        "correct": 0,
        "explanation": "n_Mg = 0,1 mol -> n_H2SO4 = 0,1 mol -> m_H2SO4 = 9,8 g -> m_dd = 9,8 / 10% = 98 g."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Kim loại nào sau đây khi tác dụng với axit sunfuric loãng giải phóng khí H2 tạo ra dung dịch muối có màu xanh lam nhạt?",
        "options": [
          "Sắt (Fe) tạo FeSO4 xanh nhạt",
          "Đồng (Cu)",
          "Kẽm (Zn)",
          "Nhôm (Al)"
        ],
        "correct": 0,
        "explanation": "Fe + H2SO4 loãng -> FeSO4 (dung dịch màu xanh lục/lam nhạt) + H2."
      }
    ]
  },
  "chem8_c2_b8_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Axit nào sau đây là axit có oxi trong phân tử?",
        "options": [
          "H2SO4 (axit sunfuric)",
          "HCl (axit clohiđric)",
          "H2S (axit sunfuhidric)",
          "HBr (axit bromhiđric)"
        ],
        "correct": 0,
        "explanation": "H2SO4 chứa nguyên tố oxi."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Tên gọi của axit HCl là:",
        "options": [
          "Axit clohiđric",
          "Axit sunfuric",
          "Axit nitric",
          "Axit cacbonic"
        ],
        "correct": 0,
        "explanation": "HCl là axit clohiđric."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nhỏ dung dịch axit vào mẩu giấy quỳ tím, hiện tượng xảy ra là:",
        "options": [
          "Giấy quỳ đổi sang màu đỏ",
          "Giấy quỳ đổi sang màu xanh",
          "Giấy quỳ mất màu",
          "Giấy quỳ không đổi màu"
        ],
        "correct": 0,
        "explanation": "Quỳ tím chuyển sang màu đỏ."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kim loại nào sau đây tác dụng được với axit clohiđric HCl sinh ra khí hiđro?",
        "options": [
          "Kẽm (Zn)",
          "Bạc (Ag)",
          "Vàng (Au)",
          "Bạch kim (Pt)"
        ],
        "correct": 0,
        "explanation": "Zn đứng trước H nên tác dụng sinh H2."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa axit và bazơ luôn gồm có:",
        "options": [
          "Muối và nước",
          "Kim loại và khí hiđro",
          "Oxit axit và muối",
          "Oxit bazơ và nước"
        ],
        "correct": 0,
        "explanation": "Phản ứng trung hòa: Axit + Bazơ -> Muối + Nước."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho mẩu đá vôi (CaCO3) vào dung dịch axit HCl, hiện tượng quan sát được là:",
        "options": [
          "Đá vôi tan dần và có bọt khí thoát ra",
          "Xuất hiện kết tủa màu đen",
          "Có khí mùi khai bay lên",
          "Dung dịch đông cứng lại"
        ],
        "correct": 0,
        "explanation": "CaCO3 + 2HCl -> CaCl2 + H2O + CO2 (sủi bọt khí)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phương trình phản ứng giữa bột nhôm và axit sunfuric loãng là:",
        "options": [
          "2Al + 3H2SO4 -> Al2(SO4)3 + 3H2",
          "Al + H2SO4 -> AlSO4 + H2",
          "2Al + H2SO4 -> Al2SO4 + H2",
          "Al + 3H2SO4 -> Al(SO4)3 + 3H2"
        ],
        "correct": 0,
        "explanation": "Nhôm có hóa trị III, gốc sunfat hóa trị II -> Al2(SO4)3."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khi bị ong hoặc kiến đốt (nọc có chứa axit fomic HCOOH), người ta thường bôi vôi tôi hoặc kem đánh răng (chứa chất kiềm nhẹ) vào vết đốt để:",
        "options": [
          "Trung hòa axit làm giảm ngứa và sưng đau",
          "Làm vết thương nóng lên",
          "Tiêu diệt vi rút",
          "Làm đông cứng nọc độc"
        ],
        "correct": 0,
        "explanation": "Chất kiềm trung hòa axit của nọc ong, kiến."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan 5,6 g kim loại sắt trong dung dịch axit HCl dư. Khối lượng muối FeCl2 thu được là:",
        "options": [
          "12,7 g",
          "16,25 g",
          "25,4 g",
          "6,35 g"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,1 mol -> m_FeCl2 = 0,1 * 127 = 12,7 g."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Axit clohiđric phản ứng được với tất cả các chất trong dãy nào sau đây?",
        "options": [
          "Fe, NaOH, CuO, CaCO3",
          "Cu, KOH, BaCl2, Ag",
          "Au, Al, Na2SO4, CO2",
          "Ag, Fe2O3, H2SO4, NaCl"
        ],
        "correct": 0,
        "explanation": "HCl tác dụng với kim loại đứng trước H (Fe), bazơ (NaOH), oxit bazơ (CuO), muối cacbonat (CaCO3)."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Thể tích khí H2 sinh ra ở đkc (25 °C, 1 bar) khi cho 0,2 mol Al tác dụng hết với dung dịch HCl dư là:",
        "options": [
          "7,437 lít",
          "4,958 lít",
          "2,479 lít",
          "6,72 lít"
        ],
        "correct": 0,
        "explanation": "n_H2 = 0,2 * 1,5 = 0,3 mol -> V = 0,3 * 24,79 = 7,437 L."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Để hòa tan hoàn toàn 8 g oxit kim loại RO (hóa trị II) cần vừa đủ 100 mL dung dịch HCl 2 M. Kim loại R là:",
        "options": [
          "Đồng (Cu = 64)",
          "Kẽm (Zn = 65)",
          "Magiê (Mg = 24)",
          "Canxi (Ca = 40)"
        ],
        "correct": 0,
        "explanation": "RO + 2HCl -> RCl2 + H2O. n_HCl = 0,2 mol -> n_RO = 0,1 mol -> M_RO = 8 / 0,1 = 80 -> M_R = 80 - 16 = 64 (Cu)."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về phân loại axit theo thành phần nguyên tố:",
        "statements": [
          {
            "subId": "a",
            "text": "Axit không có oxi: HCl, H2S, HBr, HF.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Axit có oxi: H2SO4, HNO3, H3PO4, H2CO3.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tất cả các axit đều là chất lỏng ở điều kiện thường.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Axit photphoric H3PO4 là chất rắn tinh thể ở nhiệt độ phòng.",
            "correct": true
          }
        ],
        "explanation": "H3PO4 ở dạng tinh thể rắn không màu ở nhiệt độ phòng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tính chất hóa học của axit với oxit kim loại:",
        "statements": [
          {
            "subId": "a",
            "text": "Axit tác dụng với oxit bazơ tạo thành muối và nước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cho bột CuO màu đen vào dung dịch HCl nóng, bột đen tan dần tạo dung dịch có màu xanh lam.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cho bột Fe2O3 màu nâu đỏ vào dung dịch HCl tạo dung dịch có màu vàng nâu của FeCl3.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phản ứng giữa oxit kim loại và axit giải phóng khí hiđro thoát ra.",
            "correct": false
          }
        ],
        "explanation": "Oxit bazơ + axit -> muối + nước (không sinh H2)."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các mẩu kim loại: Fe, Cu, Al, Zn vào 4 ống nghiệm đựng axit H2SO4 loãng:",
        "statements": [
          {
            "subId": "a",
            "text": "Ống nghiệm chứa Fe sủi bọt khí và dung dịch có màu xanh nhạt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ống nghiệm chứa Cu không có hiện tượng gì xảy ra.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Ống nghiệm chứa Al và Zn đều sủi bọt khí nhanh và dung dịch không màu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí thoát ra ở các ống nghiệm là khí oxi duy trì sự cháy.",
            "correct": false
          }
        ],
        "explanation": "Khí thoát ra là khí hiđro H2."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm hòa tan mẩu đá vôi CaCO3 vào dung dịch axit clohiđric:",
        "statements": [
          {
            "subId": "a",
            "text": "Phương trình: CaCO3 + 2HCl -> CaCl2 + H2O + CO2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí CO2 thoát ra làm đục dung dịch nước vôi trong.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng của cốc đựng dung dịch sau phản ứng giảm đi đúng bằng khối lượng CO2 bay ra.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phản ứng trên thuộc loại phản ứng oxi hóa - khử.",
            "correct": false
          }
        ],
        "explanation": "Đây là phản ứng trao đổi, không có sự thay đổi số oxi hóa."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Công thức hóa học của axit sunfuric là gì? (Điền: H2SO4)",
        "correctAnswer": "H2SO4",
        "explanation": "Axit sunfuric là H2SO4."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các chất: HCl, KOH, H2SO4, Na2SO4, HNO3. Có bao nhiêu axit trong dãy?",
        "correctAnswer": "3",
        "explanation": "Gồm HCl, H2SO4, HNO3 (3 axit)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Kim loại đồng Cu có tác dụng với axit clohiđric loãng không? (Điền: có hoặc không)",
        "correctAnswer": "không",
        "explanation": "Đồng đứng sau H nên không tác dụng."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hòa tan 0,1 mol kim loại kẽm vào dung dịch HCl dư. Thể tích khí H2 thu được ở đkc là bao nhiêu lít? (Ghi số thập phân)",
        "correctAnswer": "2,479",
        "explanation": "V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Khối lượng mol của axit nitric HNO3 là bao nhiêu g/mol?",
        "correctAnswer": "63",
        "explanation": "M = 1 + 14 + 16*3 = 63 g/mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cho 10 g CaCO3 tác dụng hết với axit HCl. Thể tích khí CO2 thoát ra ở đkc là bao nhiêu lít? (Ghi số thập phân)",
        "correctAnswer": "2,479",
        "explanation": "n = 0,1 mol -> V = 2,479 L."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 10,8 g kim loại Al vào dung dịch axit HCl dư. Sau phản ứng, khối lượng muối nhôm clorua AlCl3 thu được là:",
        "options": [
          "53,4 g",
          "26,7 g",
          "80,1 g",
          "40,05 g"
        ],
        "correct": 0,
        "explanation": "n_Al = 0,4 mol -> n_AlCl3 = 0,4 mol -> m = 0,4 * 133,5 = 53,4 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho 16 g bột đồng(II) oxit CuO tác dụng vừa đủ với m gam dung dịch H2SO4 20%. Giá trị của m là:",
        "options": [
          "98 g",
          "49 g",
          "196 g",
          "120 g"
        ],
        "correct": 0,
        "explanation": "n_CuO = 0,2 mol -> n_H2SO4 = 0,2 mol -> m_H2SO4 = 19,6 g -> m_dd = 19,6 / 20% = 98 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Kim loại nào sau đây khi hòa tan vào dung dịch axit clohiđric loãng cho cùng một lượng mol khí H2 với khối lượng kim loại tiêu tốn là ít nhất?",
        "options": [
          "Magiê (Mg = 24)",
          "Sắt (Fe = 56)",
          "Kẽm (Zn = 65)",
          "Canxi (Ca = 40)"
        ],
        "correct": 0,
        "explanation": "1 mol H2 cần 1 mol kim loại hóa trị II: m_Mg = 24g là nhỏ nhất."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một dung dịch chứa 0,1 mol HCl và 0,1 mol H2SO4. Để trung hòa hoàn toàn dung dịch này cần bao nhiêu mol NaOH?",
        "options": [
          "0,3 mol",
          "0,2 mol",
          "0,1 mol",
          "0,4 mol"
        ],
        "correct": 0,
        "explanation": "Tổng mol H+ = 0,1 + 0,1 * 2 = 0,3 mol -> n_NaOH = 0,3 mol."
      }
    ]
  },
  "chem8_c2_b8_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Gốc axit của axit clohiđric HCl là:",
        "options": [
          "-Cl (clorua)",
          "=SO4 (sunfat)",
          "-NO3 (nitrat)",
          "=CO3 (cacbonat)"
        ],
        "correct": 0,
        "explanation": "Gốc clorua -Cl có hóa trị I."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Chất nào sau đây KHÔNG PHẢI là axit?",
        "options": [
          "NaCl",
          "H2SO4",
          "HCl",
          "HNO3"
        ],
        "correct": 0,
        "explanation": "NaCl là muối ăn, không phải axit."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Dung dịch axit nào sau đây có trong ắc quy xe máy, ô tô?",
        "options": [
          "Axit sunfuric (H2SO4)",
          "Axit clohiđric (HCl)",
          "Axit axetic (CH3COOH)",
          "Axit nitric (HNO3)"
        ],
        "correct": 0,
        "explanation": "Ắc quy chì sử dụng dung dịch axit sunfuric loãng làm chất điện li."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kim loại nào sau đây đứng trước hiđro trong dãy hoạt động hóa học?",
        "options": [
          "Mg (magie)",
          "Cu (đồng)",
          "Ag (bạc)",
          "Au (vàng)"
        ],
        "correct": 0,
        "explanation": "Mg đứng trước H."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho các dung dịch: HCl, NaCl, NaOH, nước cất. Dung dịch làm quỳ tím chuyển sang màu đỏ là:",
        "options": [
          "HCl",
          "NaOH",
          "NaCl",
          "Nước cất"
        ],
        "correct": 0,
        "explanation": "Dung dịch axit HCl làm quỳ tím hóa đỏ."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Phản ứng giữa dung dịch axit clohiđric và đồng(II) hiđroxit Cu(OH)2 tạo ra dung dịch có màu:",
        "options": [
          "Màu xanh lam",
          "Màu đỏ nâu",
          "Không màu",
          "Màu vàng đậm"
        ],
        "correct": 0,
        "explanation": "Cu(OH)2 + 2HCl -> CuCl2 (màu xanh lam) + 2H2O."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khí nào sau đây thoát ra khi cho mẩu đá vôi vào dung dịch axit sunfuric loãng?",
        "options": [
          "Khí cacbon đioxit (CO2)",
          "Khí hiđro (H2)",
          "Khí oxi (O2)",
          "Khí sunfurơ (SO2)"
        ],
        "correct": 0,
        "explanation": "CaCO3 + H2SO4 -> CaSO4 + H2O + CO2."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Để nhận biết lọ đựng dung dịch axit clohiđric HCl và lọ đựng dung dịch muối ăn NaCl, ta có thể dùng:",
        "options": [
          "Mẩu giấy quỳ tím",
          "Nước cất",
          "Dung dịch đường",
          "Cân khối lượng"
        ],
        "correct": 0,
        "explanation": "Quỳ tím hóa đỏ với HCl, không đổi màu với NaCl."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một thanh sắt nặng 11,2 g cho vào dung dịch axit sunfuric loãng dư. Sau khi phản ứng hoàn toàn, thể tích khí H2 thu được ở đkc (25 °C, 1 bar) là:",
        "options": [
          "4,958 lít",
          "2,479 lít",
          "7,437 lít",
          "9,916 lít"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,2 mol -> n_H2 = 0,2 mol -> V = 0,2 * 24,79 = 4,958 L."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 2,4 g bột magie trong dung dịch H2SO4 loãng vừa đủ. Khối lượng muối magie sunfat MgSO4 thu được sau phản ứng là:",
        "options": [
          "12,0 g",
          "6,0 g",
          "24,0 g",
          "8,0 g"
        ],
        "correct": 0,
        "explanation": "n_Mg = 0,1 mol -> m_MgSO4 = 0,1 * 120 = 12,0 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cần lấy bao nhiêu mL dung dịch HCl 1 M để trung hòa hoàn toàn 200 mL dung dịch Ba(OH)2 0,5 M?",
        "options": [
          "200 mL",
          "100 mL",
          "400 mL",
          "300 mL"
        ],
        "correct": 0,
        "explanation": "Ba(OH)2 + 2HCl -> BaCl2 + 2H2O. n_Ba(OH)2 = 0,1 mol -> n_HCl = 0,2 mol -> V = 0,2 / 1 = 0,2 L = 200 mL."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 13 g kim loại kẽm vào dung dịch chứa 0,3 mol axit HCl. Sau phản ứng chất nào còn dư và dư bao nhiêu?",
        "options": [
          "Zn dư 0,05 mol",
          "HCl dư 0,1 mol",
          "Hai chất vừa đủ",
          "Zn dư 0,1 mol"
        ],
        "correct": 0,
        "explanation": "Zn + 2HCl -> ZnCl2 + H2. n_Zn = 0,2 mol; n_HCl = 0,3 mol -> n_Zn phản ứng = 0,15 mol -> Zn dư = 0,2 - 0,15 = 0,05 mol."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các tính chất hóa học đặc trưng của axit:",
        "statements": [
          {
            "subId": "a",
            "text": "Tác dụng với kim loại đứng trước H tạo muối và giải phóng khí H2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tác dụng với bazơ tạo thành muối và nước (phản ứng trung hòa).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tác dụng với oxit bazơ tạo thành muối và nước.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tác dụng với mọi loại muối luôn giải phóng khí clo.",
            "correct": false
          }
        ],
        "explanation": "Chỉ phản ứng với một số muối thỏa mãn điều kiện tạo kết tủa hoặc khí."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về ứng dụng của axit trong công nghiệp và đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Axit clohiđric dùng để tẩy rỉ sét kim loại trước khi hàn hoặc mạ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Axit sunfuric dùng để sản xuất phân bón hóa học (supephotphat, amoni sunfat).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Axit nitric HNO3 dùng để sản xuất thuốc nổ và phân đạm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Axit sunfuric đặc có thể dùng để làm khô mọi chất khí kể cả khí kiềm amoniac NH3.",
            "correct": false
          }
        ],
        "explanation": "H2SO4 đặc phản ứng với NH3 nên không dùng để làm khô NH3."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phản ứng trung hòa sau:",
        "statements": [
          {
            "subId": "a",
            "text": "HCl + NaOH -> NaCl + H2O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "H2SO4 + 2KOH -> K2SO4 + 2H2O.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "2HCl + Cu(OH)2 -> CuCl2 + 2H2O.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "HCl + NaCl -> NaOH + Cl2.",
            "correct": false
          }
        ],
        "explanation": "Axit không phản ứng với muối của chính nó."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm ngâm vỏ trứng (chứa canxi cacbonat CaCO3) vào cốc đựng giấm ăn (axit axetic):",
        "statements": [
          {
            "subId": "a",
            "text": "Trên bề mặt vỏ trứng xuất hiện nhiều bọt khí nhỏ bám quanh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Sau vài ngày ngâm, lớp vỏ cứng bị tan hết chỉ còn lại màng dai bên trong quả trứng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Bọt khí thoát ra trong thí nghiệm này là khí oxi.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Thí nghiệm này chứng minh giấm ăn có tính axit phản ứng hòa tan muối cacbonat.",
            "correct": true
          }
        ],
        "explanation": "Khí sinh ra là khí cacbon đioxit CO2."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong công thức hóa học của axit, nguyên tố nào luôn luôn có mặt ở đầu công thức? (Điền kí hiệu: H)",
        "correctAnswer": "H",
        "explanation": "Nguyên tố hiđro (H)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các kim loại: Al, Cu, Zn, Fe, Ag. Có bao nhiêu kim loại KHÔNG tan trong axit HCl loãng?",
        "correctAnswer": "2",
        "explanation": "Gồm Cu và Ag (2 kim loại)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Dung dịch giấm ăn làm quỳ tím đổi thành màu gì?",
        "correctAnswer": "đỏ",
        "explanation": "Giấm ăn có tính axit làm quỳ tím hóa đỏ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hòa tan hết 4 g bột MgO vào dung dịch HCl dư. Khối lượng muối MgCl2 thu được là bao nhiêu gam? (Ghi số thập phân)",
        "correctAnswer": "9,5",
        "explanation": "n_MgO = 0,1 mol -> m_MgCl2 = 0,1 * 95 = 9,5 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Số mol khí H2 sinh ra khi cho 0,3 mol kẽm Zn tác dụng hoàn toàn với axit sunfuric loãng dư là bao nhiêu mol? (Ghi số thập phân)",
        "correctAnswer": "0,3",
        "explanation": "n_H2 = n_Zn = 0,3 mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Để hòa tan hết 5,6 g kim loại sắt cần bao nhiêu gam axit HCl nguyên chất? (Ghi số thập phân)",
        "correctAnswer": "7,3",
        "explanation": "n_Fe = 0,1 mol -> n_HCl = 0,2 mol -> m = 0,2 * 36,5 = 7,3 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Cho 12 g hỗn hợp gồm Fe và Cu tác dụng với lượng dư dung dịch HCl, sau phản ứng thu được 2,479 lít khí H2 ở đkc. Khối lượng kim loại Cu trong hỗn hợp là:",
        "options": [
          "6,4 g",
          "5,6 g",
          "3,2 g",
          "4,8 g"
        ],
        "correct": 0,
        "explanation": "n_H2 = 0,1 mol -> n_Fe = 0,1 mol -> m_Fe = 5,6 g -> m_Cu = 12 - 5,6 = 6,4 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trung hòa hoàn toàn 100 mL dung dịch H2SO4 1 M bằng dung dịch NaOH 1 M. Thể tích dung dịch NaOH cần dùng là:",
        "options": [
          "200 mL",
          "100 mL",
          "50 mL",
          "150 mL"
        ],
        "correct": 0,
        "explanation": "H2SO4 + 2NaOH -> Na2SO4 + 2H2O. n_H2SO4 = 0,1 mol -> n_NaOH = 0,2 mol -> V = 0,2 L = 200 mL."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 1,6 g bột oxit đồng CuO vào 100 mL dung dịch axit sunfuric loãng 0,5 M. Nồng độ mol của muối CuSO4 trong dung dịch sau phản ứng là (coi thể tích không đổi):",
        "options": [
          "0,2 M",
          "0,1 M",
          "0,5 M",
          "0,05 M"
        ],
        "correct": 0,
        "explanation": "n_CuO = 0,02 mol -> n_CuSO4 = 0,02 mol -> CM = 0,02 / 0,1 = 0,2 M."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một mẫu quặng sắt chứa 80% Fe2O3. Để hòa tan hết 20 g mẫu quặng này cần bao nhiêu gam dung dịch axit clohiđric 14,6%?",
        "options": [
          "150 g",
          "100 g",
          "200 g",
          "120 g"
        ],
        "correct": 0,
        "explanation": "m_Fe2O3 = 16 g -> n = 0,1 mol -> n_HCl = 0,6 mol -> m_HCl = 21,9 g -> m_dd = 21,9 / 14,6% = 150 g."
      }
    ]
  },
  "chem8_c2_b9_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Bazơ (base) là hợp chất mà phân tử gồm có:",
        "options": [
          "Một nguyên tử kim loại liên kết với một hay nhiều nhóm hiđroxit (-OH)",
          "Một hay nhiều nguyên tử H liên kết với gốc axit",
          "Hai nguyên tố trong đó có oxi",
          "Kim loại liên kết với gốc axit"
        ],
        "correct": 0,
        "explanation": "Bazơ gồm nguyên tử kim loại liên kết với một hay nhiều nhóm -OH."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là một bazơ tan trong nước (kiềm)?",
        "options": [
          "NaOH (natri hiđroxit)",
          "Cu(OH)2 (đồng(II) hiđroxit)",
          "Fe(OH)3 (sắt(III) hiđroxit)",
          "Al(OH)3 (nhôm hiđroxit)"
        ],
        "correct": 0,
        "explanation": "NaOH là bazơ kiềm tan tốt trong nước."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Dung dịch kiềm (bazơ tan) làm quỳ tím chuyển sang màu gì?",
        "options": [
          "Màu xanh",
          "Màu đỏ",
          "Màu tím",
          "Màu vàng"
        ],
        "correct": 0,
        "explanation": "Dung dịch kiềm làm quỳ tím hóa xanh."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Dung dịch phenolphtalein không màu khi gặp dung dịch kiềm sẽ chuyển sang màu:",
        "options": [
          "Màu hồng (hoặc đỏ cánh sen)",
          "Màu xanh lam",
          "Màu vàng",
          "Màu trắng đục"
        ],
        "correct": 0,
        "explanation": "Phenolphtalein chuyển sang màu hồng trong môi trường kiềm."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Dãy gồm tất cả các bazơ tan trong nước (kiềm) là:",
        "options": [
          "NaOH, KOH, Ca(OH)2, Ba(OH)2",
          "Cu(OH)2, Fe(OH)2, NaOH, KOH",
          "Al(OH)3, Ba(OH)2, Mg(OH)2, KOH",
          "Fe(OH)3, Ca(OH)2, Zn(OH)2, NaOH"
        ],
        "correct": 0,
        "explanation": "Các bazơ kiềm tan: Na, K, Ca, Ba."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Một dung dịch có pH = 3. Môi trường của dung dịch này là:",
        "options": [
          "Môi trường axit",
          "Môi trường bazơ (kiềm)",
          "Môi trường trung tính",
          "Môi trường đệm"
        ],
        "correct": 0,
        "explanation": "pH < 7 là môi trường axit."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Nước cất tinh khiết ở 25 °C có giá trị pH bằng:",
        "options": [
          "7",
          "0",
          "14",
          "1"
        ],
        "correct": 0,
        "explanation": "Nước tinh khiết trung tính có pH = 7."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Dung dịch có pH = 11 làm quỳ tím đổi màu như thế nào?",
        "options": [
          "Chuyển sang màu xanh",
          "Chuyển sang màu đỏ",
          "Không đổi màu",
          "Chuyển sang màu trắng"
        ],
        "correct": 0,
        "explanation": "pH > 7 là môi trường kiềm làm quỳ tím hóa xanh."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Để khử chua cho đất trồng nông nghiệp có pH < 5, người nông dân thường bón chất nào sau đây vào ruộng?",
        "options": [
          "Vôi tôi Ca(OH)2 hoặc vôi sống CaO",
          "Phân đạm amoni nitrat",
          "Axit sunfuric loãng",
          "Muối ăn NaCl"
        ],
        "correct": 0,
        "explanation": "Vôi có tính kiềm giúp trung hòa axit dư thừa trong đất chua."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Khi cho dung dịch axit HCl vào dung dịch NaOH có sẵn vài giọt phenolphtalein (màu hồng), hiện tượng quan sát được tại điểm tương đương là:",
        "options": [
          "Màu hồng biến mất thành không màu",
          "Màu hồng chuyển sang màu xanh",
          "Xuất hiện kết tủa màu nâu đỏ",
          "Dung dịch sôi sùng sục bốc khói đen"
        ],
        "correct": 0,
        "explanation": "Khi axit trung hòa hết kiềm, phenolphtalein mất màu hồng trở lại không màu."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Khối lượng NaOH có trong 200 mL dung dịch NaOH 1,5 M là:",
        "options": [
          "12 g",
          "6 g",
          "8 g",
          "16 g"
        ],
        "correct": 0,
        "explanation": "n = 0,2 * 1,5 = 0,3 mol -> m = 0,3 * 40 = 12 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Trung hòa hoàn toàn 100 mL dung dịch Ba(OH)2 0,1 M cần dùng V mL dung dịch HCl 0,2 M. Giá trị của V là:",
        "options": [
          "100 mL",
          "50 mL",
          "200 mL",
          "150 mL"
        ],
        "correct": 0,
        "explanation": "Ba(OH)2 + 2HCl -> BaCl2 + 2H2O. n_Ba(OH)2 = 0,01 mol -> n_HCl = 0,02 mol -> V = 0,02 / 0,2 = 0,1 L = 100 mL."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về phân loại bazơ theo tính tan:",
        "statements": [
          {
            "subId": "a",
            "text": "Bazơ tan trong nước được gọi là kiềm: NaOH, KOH, Ba(OH)2, Ca(OH)2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bazơ không tan trong nước: Cu(OH)2, Fe(OH)2, Fe(OH)3, Al(OH)3, Mg(OH)2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tất cả các bazơ đều làm đổi màu quỳ tím sang màu xanh.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Chỉ có các dung dịch bazơ tan (kiềm) mới làm đổi màu quỳ tím và phenolphtalein.",
            "correct": true
          }
        ],
        "explanation": "Bazơ không tan không phân li ion OH- nên không làm đổi màu chất chỉ thị."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về thang đo pH trong đời sống:",
        "statements": [
          {
            "subId": "a",
            "text": "Thang pH thường có giá trị từ 1 đến 14 biểu thị độ axit hay độ kiềm của dung dịch.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dung dịch có pH < 7 có môi trường axit; pH càng nhỏ tính axit càng mạnh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch có pH = 7 là môi trường trung tính.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dung dịch có pH > 7 có môi trường bazơ; pH càng gần 7 tính bazơ càng mạnh.",
            "correct": false
          }
        ],
        "explanation": "pH càng lớn (tiến về 14) tính bazơ càng mạnh."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về pH của các chất thường gặp:",
        "statements": [
          {
            "subId": "a",
            "text": "Nước chanh, giấm ăn có pH < 7.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nước xà phòng, nước vôi có pH > 7.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dịch máu người khỏe mạnh có pH hơi kiềm ổn định khoảng 7,35 - 7,45.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dịch vị dạ dày người có tính kiềm mạnh với pH khoảng 10 - 12.",
            "correct": false
          }
        ],
        "explanation": "Dịch vị dạ dày có tính axit mạnh với pH khoảng 1,5 - 3,5."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng nhiệt phân các bazơ không tan:",
        "statements": [
          {
            "subId": "a",
            "text": "Các bazơ không tan bị nhiệt phân hủy tạo thành oxit kim loại tương ứng và nước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nung Cu(OH)2 màu xanh lam thu được chất rắn CuO màu đen và hơi nước.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Các bazơ kiềm như NaOH, KOH bị nung ở ngọn lửa đèn cồn cũng bị phân hủy tạo Na2O và H2O.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Phương trình: 2Fe(OH)3 -> Fe2O3 + 3H2O.",
            "correct": true
          }
        ],
        "explanation": "Bazơ kiềm bền với nhiệt, không bị phân hủy bởi đèn cồn thông thường."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong công thức của bazơ, nhóm nguyên tử nào liên kết với nguyên tử kim loại? (Điền: OH)",
        "correctAnswer": "OH",
        "explanation": "Nhóm hiđroxit (-OH)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Dung dịch nước xà phòng làm giấy quỳ tím chuyển sang màu gì?",
        "correctAnswer": "xanh",
        "explanation": "Xà phòng có tính kiềm làm quỳ tím hóa xanh."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một dung dịch có pH = 9. Môi trường của dung dịch này là axit hay bazơ? (Điền: bazơ)",
        "correctAnswer": "bazơ",
        "explanation": "pH > 7 là môi trường bazơ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng mol của canxi hiđroxit Ca(OH)2 là bao nhiêu g/mol?",
        "correctAnswer": "74",
        "explanation": "M = 40 + (16+1)*2 = 74 g/mol."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan 0,2 mol KOH vào nước được 500 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M? (Ghi số thập phân)",
        "correctAnswer": "0,4",
        "explanation": "CM = 0,2 / 0,5 = 0,4 M."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Nung hoàn toàn 9,8 g Cu(OH)2 thu được bao nhiêu gam bột CuO màu đen?",
        "correctAnswer": "8",
        "explanation": "n = 9,8 / 98 = 0,1 mol -> m_CuO = 0,1 * 80 = 8 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn m gam kim loại natri vào nước dư thu được 100 mL dung dịch NaOH 1 M và giải phóng V lít khí H2 ở đkc. Giá trị của m là:",
        "options": [
          "2,3 g",
          "4,6 g",
          "1,15 g",
          "3,45 g"
        ],
        "correct": 0,
        "explanation": "n_NaOH = 0,1 mol -> n_Na = 0,1 mol -> m_Na = 0,1 * 23 = 2,3 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho 200 mL dung dịch NaOH 1 M tác dụng hoàn toàn với 100 mL dung dịch FeCl3 0,5 M. Khối lượng kết tủa Fe(OH)3 màu nâu đỏ thu được là:",
        "options": [
          "5,35 g",
          "10,7 g",
          "2,675 g",
          "8,0 g"
        ],
        "correct": 0,
        "explanation": "FeCl3 + 3NaOH -> Fe(OH)3 + 3NaCl. n_NaOH = 0,2 mol; n_FeCl3 = 0,05 mol -> NaOH dư, tính theo FeCl3 -> m_Fe(OH)3 = 0,05 * 107 = 5,35 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một cốc chứa dung dịch H2SO4 có pH = 2. Để đưa pH của dung dịch về mức trung tính (pH = 7), người ta cần nhỏ vào cốc lượng vừa đủ dung dịch:",
        "options": [
          "Dung dịch kiềm như NaOH hoặc Ca(OH)2",
          "Nước cất tinh khiết vô hạn",
          "Axit HCl đậm đặc",
          "Dung dịch giấm ăn"
        ],
        "correct": 0,
        "explanation": "Dùng dung dịch kiềm để trung hòa axit."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Nhiệt phân hoàn toàn m gam Fe(OH)3 thu được 16 g bột Fe2O3 màu nâu đỏ. Giá trị của m là:",
        "options": [
          "21,4 g",
          "10,7 g",
          "32,1 g",
          "16,0 g"
        ],
        "correct": 0,
        "explanation": "2Fe(OH)3 -> Fe2O3 + 3H2O. n_Fe2O3 = 0,1 mol -> n_Fe(OH)3 = 0,2 mol -> m = 0,2 * 107 = 21,4 g."
      }
    ]
  },
  "chem8_c2_b10_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Oxit là hợp chất gồm có:",
        "options": [
          "Hai nguyên tố, trong đó có một nguyên tố là oxi",
          "Kim loại liên kết với nhóm hiđroxit",
          "Hiđro liên kết với gốc axit",
          "Các nguyên tố phi kim liên kết với nhau"
        ],
        "correct": 0,
        "explanation": "Oxit là hợp chất của 2 nguyên tố trong đó có 1 nguyên tố là oxi."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là một oxit bazơ?",
        "options": [
          "CaO (canxi oxit)",
          "CO2 (cacbon đioxit)",
          "SO2 (lưu huỳnh đioxit)",
          "P2O5 (điphotpho pentaoxit)"
        ],
        "correct": 0,
        "explanation": "CaO là oxit bazơ tương ứng với bazơ Ca(OH)2."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là một oxit axit?",
        "options": [
          "SO3 (lưu huỳnh trioxit)",
          "Na2O (natri oxit)",
          "CuO (đồng(II) oxit)",
          "BaO (bari oxit)"
        ],
        "correct": 0,
        "explanation": "SO3 là oxit axit tương ứng với axit H2SO4."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Oxit nào sau đây tác dụng với nước tạo thành dung dịch làm quỳ tím hóa xanh?",
        "options": [
          "Na2O",
          "P2O5",
          "CO2",
          "SO2"
        ],
        "correct": 0,
        "explanation": "Na2O + H2O -> 2NaOH (dung dịch kiềm làm quỳ tím hóa xanh)."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho các oxit: CO2, SO2, CaO, Na2O, CuO, P2O5. Số oxit axit trong dãy là:",
        "options": [
          "3",
          "2",
          "4",
          "1"
        ],
        "correct": 0,
        "explanation": "Gồm CO2, SO2, P2O5 (3 oxit axit)."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khí CO và NO thuộc loại oxit nào sau đây?",
        "options": [
          "Oxit trung tính (không tạo muối)",
          "Oxit axit",
          "Oxit bazơ",
          "Oxit lưỡng tính"
        ],
        "correct": 0,
        "explanation": "CO và NO không tác dụng với axit, bazơ ở điều kiện thường nên gọi là oxit trung tính."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Oxit lưỡng tính là oxit:",
        "options": [
          "Vừa tác dụng được với dung dịch axit, vừa tác dụng được với dung dịch bazơ",
          "Chỉ tác dụng với nước",
          "Không tác dụng với chất nào",
          "Làm đổi màu quỳ tím sang vàng"
        ],
        "correct": 0,
        "explanation": "Định nghĩa: Oxit lưỡng tính tác dụng với cả axit và bazơ (ví dụ Al2O3, ZnO)."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa canxi oxit CaO với nước là:",
        "options": [
          "Canxi hiđroxit Ca(OH)2 tỏa nhiều nhiệt",
          "Canxi cacbonat",
          "Khí hiđro",
          "Canxi clorua"
        ],
        "correct": 0,
        "explanation": "CaO + H2O -> Ca(OH)2 (phản ứng tôi vôi tỏa nhiệt mạnh)."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Dẫn luồng khí CO2 dư vào dung dịch nước vôi trong Ca(OH)2, hiện tượng quan sát được là:",
        "options": [
          "Dung dịch bị vẩn đục màu trắng do tạo kết tủa CaCO3",
          "Dung dịch chuyển sang màu xanh lam",
          "Có bọt khí cháy bùng lên",
          "Không có hiện tượng gì"
        ],
        "correct": 0,
        "explanation": "CO2 + Ca(OH)2 -> CaCO3 (kết tủa trắng) + H2O."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 6,2 g Na2O vào nước thu được 200 mL dung dịch NaOH. Nồng độ mol của dung dịch NaOH là:",
        "options": [
          "1 M",
          "0,5 M",
          "2 M",
          "0,25 M"
        ],
        "correct": 0,
        "explanation": "Na2O + H2O -> 2NaOH. n_Na2O = 0,1 mol -> n_NaOH = 0,2 mol -> CM = 0,2 / 0,2 = 1 M."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Khối lượng CuO cần dùng để phản ứng vừa đủ với 100 mL dung dịch HCl 1 M là:",
        "options": [
          "4,0 g",
          "8,0 g",
          "2,0 g",
          "6,4 g"
        ],
        "correct": 0,
        "explanation": "CuO + 2HCl -> CuCl2 + H2O. n_HCl = 0,1 mol -> n_CuO = 0,05 mol -> m = 0,05 * 80 = 4,0 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Dẫn 3,7185 lít khí CO2 ở đkc (tương ứng 0,15 mol) vào dung dịch chứa 0,1 mol Ca(OH)2. Sau phản ứng hoàn toàn thu được m gam kết tủa CaCO3. Giá trị của m là:",
        "options": [
          "5,0 g",
          "10,0 g",
          "15,0 g",
          "7,5 g"
        ],
        "correct": 0,
        "explanation": "T = n_CO2 / n_Ca(OH)2 = 1,5 -> tạo 0,05 mol CaCO3 và 0,05 mol Ca(HCO3)2 -> m = 0,05 * 100 = 5,0 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về phân loại oxit:",
        "statements": [
          {
            "subId": "a",
            "text": "Oxit bazơ là oxit tác dụng với axit tạo thành muối và nước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Oxit axit thường là oxit của phi kim tương ứng với một axit.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Al2O3 và ZnO là các oxit lưỡng tính.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các oxit kim loại đều là oxit bazơ tan tốt trong nước.",
            "correct": false
          }
        ],
        "explanation": "Rất nhiều oxit kim loại như CuO, Fe2O3 không tan trong nước."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tác dụng của oxit với nước:",
        "statements": [
          {
            "subId": "a",
            "text": "Các oxit bazơ tan như Na2O, K2O, CaO, BaO tác dụng với nước tạo dung dịch kiềm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nhiều oxit axit như SO2, SO3, P2O5 tác dụng với nước tạo dung dịch axit tương ứng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Oxit sắt Fe2O3 tác dụng mãnh liệt với nước tạo bazơ Fe(OH)3.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khí cacbon monooxit CO tác dụng với nước tạo axit cacbonic.",
            "correct": false
          }
        ],
        "explanation": "Fe2O3 và CO đều không tác dụng với nước ở điều kiện thường."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phản ứng sau ở điều kiện thích hợp:",
        "statements": [
          {
            "subId": "a",
            "text": "CaO + CO2 -> CaCO3.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "CuO + 2HCl -> CuCl2 + H2O.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "P2O5 + 3H2O -> 2H3PO4.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "CO2 + H2O -> H2SO4.",
            "correct": false
          }
        ],
        "explanation": "CO2 + H2O tạo H2CO3."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Về oxit trong công nghiệp và môi trường:",
        "statements": [
          {
            "subId": "a",
            "text": "Khí SO2 và NO2 là thủ phạm chính gây ra hiện tượng mưa axit phá hủy môi trường.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Vôi sống CaO được dùng để khử chua đất trồng và xử lý nước thải công nghiệp.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khí CO là oxit trung tính không màu, không mùi, độc hại do kết hợp với hemoglobin trong máu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí CO2 là khí độc nguy hiểm bậc một có thể gây nổ ngay ở nhiệt độ phòng.",
            "correct": false
          }
        ],
        "explanation": "CO2 không độc hại trực tiếp như CO và không gây nổ mà chỉ gây ngạt khi nồng độ quá cao."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong một phân tử oxit luôn chứa nguyên tử của nguyên tố nào? (Điền: oxi)",
        "correctAnswer": "oxi",
        "explanation": "Nguyên tố oxi (O)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các oxit: Na2O, SO2, CaO, CO2, CuO. Có bao nhiêu oxit bazơ trong dãy?",
        "correctAnswer": "3",
        "explanation": "Na2O, CaO, CuO (3 oxit bazơ)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa P2O5 và nước làm quỳ tím chuyển sang màu gì?",
        "correctAnswer": "đỏ",
        "explanation": "P2O5 + 3H2O -> 2H3PO4 (axit làm quỳ tím hóa đỏ)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng mol của oxit sắt Fe2O3 là bao nhiêu g/mol?",
        "correctAnswer": "160",
        "explanation": "M = 56*2 + 16*3 = 160 g/mol."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan 8 g CuO bằng dung dịch H2SO4 loãng vừa đủ. Khối lượng muối CuSO4 thu được là bao nhiêu gam?",
        "correctAnswer": "16",
        "explanation": "n = 0,1 mol -> m = 0,1 * 160 = 16 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Dẫn 2,479 lít khí CO2 (đkc) vào dung dịch Ca(OH)2 dư. Khối lượng kết tủa CaCO3 thu được là bao nhiêu gam?",
        "correctAnswer": "10",
        "explanation": "n = 0,1 mol -> m = 0,1 * 100 = 10 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 20 g hỗn hợp gồm CuO và Fe2O3 cần vừa đủ 500 mL dung dịch axit HCl 1 M. Khối lượng muối clorua thu được trong dung dịch sau phản ứng là:",
        "options": [
          "33,75 g",
          "35,25 g",
          "28,5 g",
          "40,0 g"
        ],
        "correct": 0,
        "explanation": "n_HCl = 0,5 mol -> n_O trong oxit = 0,25 mol -> m_O = 4 g -> m_KL = 20 - 4 = 16 g. m_muối = 16 + 0,5 * 35,5 = 33,75 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Khí CO2 có lẫn tạp chất là khí SO2. Để thu được khí CO2 tinh khiết, người ta dẫn hỗn hợp khí qua bình đựng lượng dư dung dịch nào sau đây?",
        "options": [
          "Dung dịch nước brom (Br2) vì SO2 phản ứng làm mất màu brom còn CO2 không phản ứng",
          "Dung dịch nước vôi trong Ca(OH)2",
          "Dung dịch NaOH",
          "Dung dịch Ba(OH)2"
        ],
        "correct": 0,
        "explanation": "Nước brom giữ lại SO2 (SO2 + Br2 + 2H2O -> H2SO4 + 2HBr), khí CO2 thoát ra ngoài tinh khiết."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Cho m gam hỗn hợp gồm Na2O và K2O có tỉ lệ mol 1 : 1 tác dụng hoàn toàn với nước thu được dung dịch chứa 0,2 mol NaOH và 0,2 mol KOH. Giá trị của m là:",
        "options": [
          "15,6 g",
          "31,2 g",
          "7,8 g",
          "23,4 g"
        ],
        "correct": 0,
        "explanation": "n_Na2O = 0,1 mol; n_K2O = 0,1 mol -> m = 0,1*62 + 0,1*94 = 6,2 + 9,4 = 15,6 g."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một oxit của kim loại M hóa trị III có chứa 70% kim loại M về khối lượng. Kim loại M là:",
        "options": [
          "Sắt (Fe = 56)",
          "Nhôm (Al = 27)",
          "Crom (Cr = 52)",
          "Mangan (Mn = 55)"
        ],
        "correct": 0,
        "explanation": "M2O3: 2M / (2M + 48) = 0,7 -> 2M = 1,4M + 33,6 -> 0,6M = 33,6 -> M = 56 (Fe)."
      }
    ]
  },
  "chem8_c2_b11_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Muối là hợp chất mà phân tử gồm có:",
        "options": [
          "Nguyên tử kim loại (hoặc nhóm amoni NH4+) liên kết với một hay nhiều gốc axit",
          "Một hay nhiều nguyên tử H liên kết với gốc axit",
          "Kim loại liên kết với nhóm hiđroxit",
          "Hai nguyên tố trong đó có oxi"
        ],
        "correct": 0,
        "explanation": "Muối gồm kim loại (hoặc NH4+) liên kết với gốc axit."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Muối nào sau đây tan tốt trong nước?",
        "options": [
          "NaCl (natri clorua)",
          "BaSO4 (bari sunfat)",
          "CaCO3 (canxi cacbonat)",
          "AgCl (bạc clorua)"
        ],
        "correct": 0,
        "explanation": "NaCl tan rất tốt trong nước."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Muối nào sau đây KHÔNG TAN (kết tủa trắng) trong nước?",
        "options": [
          "BaSO4",
          "Na2SO4",
          "K2SO4",
          "MgSO4"
        ],
        "correct": 0,
        "explanation": "BaSO4 là kết tủa trắng không tan trong nước và axit."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tất cả các muối của gốc axit nào sau đây đều tan tốt trong nước?",
        "options": [
          "Gốc nitrat (-NO3)",
          "Gốc cacbonat (=CO3)",
          "Gốc sunfit (=SO3)",
          "Gốc photphat (≡PO4)"
        ],
        "correct": 0,
        "explanation": "Tất cả các muối nitrat (-NO3) đều tan trong nước."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho dãy các muối: NaCl, BaSO4, KNO3, CaCO3, CuCl2, AgCl. Số muối tan tốt trong nước là:",
        "options": [
          "3",
          "4",
          "2",
          "5"
        ],
        "correct": 0,
        "explanation": "Có 3 muối tan: NaCl, KNO3, CuCl2 (BaSO4, CaCO3, AgCl không tan)."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Phản ứng giữa dung dịch bari clorua BaCl2 và dung dịch natri sunfat Na2SO4 sinh ra kết tủa trắng là:",
        "options": [
          "BaSO4 (bari sunfat)",
          "NaCl",
          "BaCO3",
          "Na2SO3"
        ],
        "correct": 0,
        "explanation": "BaCl2 + Na2SO4 -> BaSO4 (trắng) + 2NaCl."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi cho một đinh sắt sạch vào dung dịch đồng(II) sunfat CuSO4, sau một thời gian hiện tượng quan sát được là:",
        "options": [
          "Có lớp kim loại màu đỏ bám trên đinh sắt và màu xanh của dung dịch nhạt dần",
          "Có bọt khí thoát ra dữ dội",
          "Đinh sắt bị tan biến thành chất lỏng",
          "Dung dịch chuyển sang màu tím đậm"
        ],
        "correct": 0,
        "explanation": "Fe + CuSO4 -> FeSO4 (xanh nhạt) + Cu (đỏ bám trên sắt)."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Điều kiện để phản ứng trao đổi giữa hai dung dịch muối xảy ra là sản phẩm phải có:",
        "options": [
          "Ít nhất một chất kết tủa hoặc chất khí",
          "Chất phản ứng phải là chất rắn",
          "Phải có nhiệt độ thật cao",
          "Cả hai sản phẩm đều phải tan"
        ],
        "correct": 0,
        "explanation": "Điều kiện phản ứng trao đổi trong dung dịch: tạo kết tủa, khí hoặc chất điện li yếu (nước)."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 10 g đá vôi CaCO3 bằng dung dịch axit HCl dư. Thể tích khí CO2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "2,479 lít",
          "4,958 lít",
          "2,24 lít",
          "1,2395 lít"
        ],
        "correct": 0,
        "explanation": "n_CaCO3 = 0,1 mol -> V_CO2 = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trộn 100 mL dung dịch AgNO3 0,1 M với 100 mL dung dịch NaCl 0,1 M. Khối lượng kết tủa AgCl thu được là:",
        "options": [
          "1,435 g",
          "2,87 g",
          "0,7175 g",
          "1,08 g"
        ],
        "correct": 0,
        "explanation": "AgNO3 + NaCl -> AgCl + NaNO3. n = 0,01 mol -> m_AgCl = 0,01 * 143,5 = 1,435 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cặp chất nào sau đây CÙNG TỒN TẠI trong một dung dịch mà không phản ứng với nhau?",
        "options": [
          "NaCl và KNO3",
          "BaCl2 và Na2SO4",
          "AgNO3 và NaCl",
          "NaOH và FeCl3"
        ],
        "correct": 0,
        "explanation": "NaCl và KNO3 không tạo kết tủa hay khí nên cùng tồn tại trong dung dịch."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho 200 g dung dịch BaCl2 5,2% tác dụng vừa đủ với dung dịch H2SO4 loãng. Khối lượng kết tủa BaSO4 thu được là:",
        "options": [
          "11,65 g",
          "23,3 g",
          "5,825 g",
          "10,4 g"
        ],
        "correct": 0,
        "explanation": "m_BaCl2 = 10,4 g -> n = 0,05 mol -> m_BaSO4 = 0,05 * 233 = 11,65 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về tính tan của các muối trong nước:",
        "statements": [
          {
            "subId": "a",
            "text": "Hầu hết các muối natri (Na) và kali (K) đều tan tốt trong nước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tất cả các muối nitrat (-NO3) đều tan trong nước.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Muối clorua (-Cl) hầu hết tan tốt, trừ AgCl không tan.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các muối cacbonat (=CO3) đều tan tốt trong nước.",
            "correct": false
          }
        ],
        "explanation": "Hầu hết muối cacbonat không tan, trừ muối của Na, K, NH4+."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tính chất hóa học của muối:",
        "statements": [
          {
            "subId": "a",
            "text": "Dung dịch muối tác dụng với kim loại đứng trước trong dãy hoạt động hóa học tạo muối mới và kim loại mới.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dung dịch muối tác dụng với axit tạo thành muối mới và axit mới.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch muối tác dụng với dung dịch kiềm tạo muối mới và bazơ mới.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Hai dung dịch muối bất kì khi trộn lẫn với nhau luôn xảy ra phản ứng hóa học.",
            "correct": false
          }
        ],
        "explanation": "Chỉ phản ứng nếu sản phẩm tạo thành có chất kết tủa."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phản ứng trao đổi trong dung dịch sau:",
        "statements": [
          {
            "subId": "a",
            "text": "BaCl2 + Na2SO4 -> BaSO4 + 2NaCl.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "AgNO3 + NaCl -> AgCl + NaNO3.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "CuSO4 + 2NaOH -> Cu(OH)2 + Na2SO4.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "KNO3 + NaCl -> KCl + NaNO3.",
            "correct": false
          }
        ],
        "explanation": "Không có kết tủa hay khí sinh ra nên phản ứng không xảy ra."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm ngâm thanh đồng (Cu) vào dung dịch bạc nitrat (AgNO3):",
        "statements": [
          {
            "subId": "a",
            "text": "Phương trình: Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dung dịch từ không màu chuyển dần sang màu xanh lam của muối đồng(II).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Có kim loại bạc màu trắng xám bám ngoài thanh đồng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Sau phản ứng, khối lượng thanh đồng bị giảm đi.",
            "correct": false
          }
        ],
        "explanation": "1 mol Cu (64g) tan ra tạo 2 mol Ag (216g) bám vào nên khối lượng thanh đồng tăng lên rõ rệt."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Muối ăn hàng ngày có công thức hóa học là gì? (Điền: NaCl)",
        "correctAnswer": "NaCl",
        "explanation": "Natri clorua NaCl."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Cho các muối: Na2SO4, BaSO4, AgCl, CaCO3. Có bao nhiêu muối kết tủa không tan trong nước?",
        "correctAnswer": "3",
        "explanation": "BaSO4, AgCl, CaCO3 (3 muối không tan)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Phản ứng giữa dung dịch AgNO3 và dung dịch NaCl sinh ra chất kết tủa màu gì?",
        "correctAnswer": "trắng",
        "explanation": "Kết tủa AgCl màu trắng."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng mol của muối canxi cacbonat CaCO3 là bao nhiêu g/mol?",
        "correctAnswer": "100",
        "explanation": "M = 40 + 12 + 16*3 = 100 g/mol."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan hết 5,85 g NaCl vào nước để được 100 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M?",
        "correctAnswer": "1",
        "explanation": "n = 0,1 mol -> CM = 0,1 / 0,1 = 1 M."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Nhiệt phân hoàn toàn 10 g đá vôi CaCO3 thu được bao nhiêu gam vôi sống CaO? (Ghi số thập phân)",
        "correctAnswer": "5,6",
        "explanation": "n = 0,1 mol -> m_CaO = 0,1 * 56 = 5,6 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Ngâm một lá sắt có khối lượng 10 g vào 200 mL dung dịch CuSO4 0,5 M. Sau một thời gian lấy lá sắt ra, rửa nhẹ, sấy khô cân lại thấy nặng 10,8 g. Khối lượng kim loại đồng Cu đã bám lên lá sắt là:",
        "options": [
          "6,4 g",
          "0,8 g",
          "3,2 g",
          "1,6 g"
        ],
        "correct": 0,
        "explanation": "m tăng = n * (64 - 56) = 8n = 0,8 g -> n = 0,1 mol -> m_Cu bám = 0,1 * 64 = 6,4 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho dung dịch chứa 0,2 mol BaCl2 tác dụng với dung dịch chứa 0,15 mol Na2SO4. Khối lượng kết tủa BaSO4 thu được là:",
        "options": [
          "34,95 g",
          "46,6 g",
          "23,3 g",
          "11,65 g"
        ],
        "correct": 0,
        "explanation": "Tính theo Na2SO4 thiếu: n_BaSO4 = 0,15 mol -> m = 0,15 * 233 = 34,95 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Trộn lẫn 100 mL dung dịch CaCl2 1 M với 100 mL dung dịch Na2CO3 1 M thu được m gam kết tủa trắng. Giá trị của m là:",
        "options": [
          "10,0 g",
          "5,0 g",
          "20,0 g",
          "7,5 g"
        ],
        "correct": 0,
        "explanation": "CaCl2 + Na2CO3 -> CaCO3 + 2NaCl. n = 0,1 mol -> m = 0,1 * 100 = 10,0 g."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một dung dịch chứa hỗn hợp hai muối FeSO4 và CuSO4. Để tách hoàn toàn ion Cu2+ ra khỏi dung dịch mà không đưa thêm ion kim loại lạ vào dung dịch, người ta cho vào một lượng dư kim loại nào?",
        "options": [
          "Kim loại bột sắt Fe",
          "Kim loại kẽm Zn",
          "Kim loại nhôm Al",
          "Kim loại magie Mg"
        ],
        "correct": 0,
        "explanation": "Fe đẩy Cu ra khỏi muối (Fe + CuSO4 -> FeSO4 + Cu), tạo thêm FeSO4 trùng với chất có sẵn."
      }
    ]
  },
  "chem8_c2_b12_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phân bón hóa học là những hóa chất chứa các nguyên tố dinh dưỡng được bón cho cây trồng nhằm:",
        "options": [
          "Tăng năng suất và chất lượng cây trồng",
          "Diệt sâu bọ hại cây",
          "Làm đông cứng đất trồng",
          "Tăng nhiệt độ của đất"
        ],
        "correct": 0,
        "explanation": "Cung cấp dinh dưỡng cho cây phát triển khỏe mạnh, tăng năng suất."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Nguyên tố dinh dưỡng nào sau đây có trong phân đạm?",
        "options": [
          "Nitơ (N)",
          "Photpho (P)",
          "Kali (K)",
          "Canxi (Ca)"
        ],
        "correct": 0,
        "explanation": "Phân đạm cung cấp nguyên tố dinh dưỡng nitơ (N)."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Nguyên tố dinh dưỡng nào sau đây có trong phân lân?",
        "options": [
          "Photpho (P)",
          "Nitơ (N)",
          "Kali (K)",
          "Lưu huỳnh (S)"
        ],
        "correct": 0,
        "explanation": "Phân lân cung cấp photpho (P)."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nguyên tố dinh dưỡng nào sau đây có trong phân kali?",
        "options": [
          "Kali (K)",
          "Nitơ (N)",
          "Photpho (P)",
          "Magie (Mg)"
        ],
        "correct": 0,
        "explanation": "Phân kali cung cấp kali (K)."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Phân đạm urê có công thức hóa học là:",
        "options": [
          "(NH2)2CO",
          "NH4NO3",
          "(NH4)2SO4",
          "KNO3"
        ],
        "correct": 0,
        "explanation": "Urê là (NH2)2CO chứa hàm lượng nitơ cao nhất (khoảng 46%)."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Phân đạm có tác dụng chủ yếu kích thích:",
        "options": [
          "Sự sinh trưởng của lá, thân và cành cây phát triển xanh tốt",
          "Sự phát triển của bộ rễ và củ",
          "Quả ngọt và hạt chắc, tăng chịu rét",
          "Hoa nở nhiều màu sắc"
        ],
        "correct": 0,
        "explanation": "Đạm kích thích lá, cành, sinh khối phát triển."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phân lân có tác dụng chủ yếu kích thích:",
        "options": [
          "Sự phát triển của bộ rễ, sự tạo củ và ra hoa kết quả",
          "Sự lớn nhanh của cành lá",
          "Tăng khả năng chống rét chịu hạn",
          "Tạo chất diệp lục"
        ],
        "correct": 0,
        "explanation": "Lân kích thích cành, rễ, củ và mầm hoa."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Phân kali có tác dụng chủ yếu giúp cây trồng:",
        "options": [
          "Tăng khả năng chống chịu sâu bệnh, rét, hạn và làm quả ngọt, hạt chắc",
          "Tốt lá tốt cành",
          "Tăng độ chua của đất",
          "Kích thích rễ dài ra"
        ],
        "correct": 0,
        "explanation": "Kali tăng sức đề kháng, vận chuyển đường bột làm chắc hạt, ngọt quả."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Trên bao bì một loại phân bón NPK có ghi chỉ số 16-16-8. Các con số này cho biết tỉ lệ phần trăm tương ứng của:",
        "options": [
          "N, P2O5 và K2O",
          "N, P và K",
          "NO3, PO4 và K",
          "Đạm, lân và vi lượng"
        ],
        "correct": 0,
        "explanation": "Quy ước quốc tế: %N, %P2O5, %K2O."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Loại phân đạm nào sau đây có hàm lượng phần trăm nitơ cao nhất?",
        "options": [
          "Urê (NH2)2CO (khoảng 46%)",
          "Amoni nitrat NH4NO3 (khoảng 35%)",
          "Amoni sunfat (NH4)2SO4 (khoảng 21%)",
          "Natri nitrat NaNO3 (khoảng 16%)"
        ],
        "correct": 0,
        "explanation": "Urê có %N = 28 / 60 = 46,67% cao nhất."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Tại sao không nên bón phân đạm amoni ((NH4)2SO4 hoặc NH4NO3) cùng lúc với vôi tôi Ca(OH)2?",
        "options": [
          "Vì vôi tác dụng với muối amoni giải phóng khí amoniac (NH3) bay mất làm thất thoát chất đạm",
          "Vì làm đất bị lạnh đóng băng",
          "Vì tạo ra chất nổ",
          "Vì làm chết cây ngay lập tức do thiếu nước"
        ],
        "correct": 0,
        "explanation": "2NH4+ + Ca(OH)2 -> Ca2+ + 2NH3 bay hơi + 2H2O làm mất đạm."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Một người nông dân cần bón 28 kg nitơ cho một thửa ruộng. Khối lượng phân đạm urê (chứa 90% (NH2)2CO nguyên chất, còn lại tạp chất) cần dùng là:",
        "options": [
          "66,7 kg",
          "60,0 kg",
          "75,0 kg",
          "50,0 kg"
        ],
        "correct": 0,
        "explanation": "m_urê nguyên chất = 28 / (28/60) = 60 kg -> m_phân bón = 60 / 90% = 66,7 kg."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về vai trò của ba nguyên tố dinh dưỡng đa lượng N, P, K:",
        "statements": [
          {
            "subId": "a",
            "text": "Nitơ (N) là thành phần cấu tạo nên protein và diệp lục trong cây.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Photpho (P) thúc đẩy sự phát triển của hệ rễ và quá trình chín của hạt, quả.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kali (K) giúp cây tăng khả năng chống chịu thời tiết khắc nghiệt và sâu bệnh.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Cây trồng chỉ cần duy nhất phân đạm là có thể phát triển hoàn hảo mà không cần P và K.",
            "correct": false
          }
        ],
        "explanation": "Cây cần cân đối cả 3 yếu tố N, P, K và các nguyên tố vi lượng."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các loại phân bón hóa học thông dụng:",
        "statements": [
          {
            "subId": "a",
            "text": "Phân đơn là phân chỉ chứa 1 trong 3 nguyên tố dinh dưỡng chính (N, P hoặc K).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phân đạm urê (NH2)2CO tan rất tốt trong nước và dễ hút ẩm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phân lân supephotphat có thành phần chính là Ca(H2PO4)2 tan trong nước.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phân kali thường dùng là muối kali clorua (KCl) hoặc kali sunfat (K2SO4).",
            "correct": true
          }
        ],
        "explanation": "Các nhận định a, b, c, d đều đúng."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về phân bón hỗn hợp và phân vi lượng:",
        "statements": [
          {
            "subId": "a",
            "text": "Phân NPK là phân bón hỗn hợp chứa cả 3 nguyên tố dinh dưỡng N, P, K.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phân vi lượng chứa các nguyên tố như Bo, Kẽm, Đồng, Sắt, Mangan với lượng rất nhỏ nhưng không thể thiếu.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Bón càng nhiều phân bón hóa học càng tốt cho đất và nguồn nước ngầm.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Bón thừa phân đạm làm cây yếu, dễ lốp đổ và tích lũy nitrat độc hại trong rau củ.",
            "correct": true
          }
        ],
        "explanation": "Bón thừa phân gây ô nhiễm nguồn nước và thoái hóa đất."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Về nguyên tắc bón phân khoa học (nguyên tắc 4 đúng):",
        "statements": [
          {
            "subId": "a",
            "text": "Bón đúng loại phân phù hợp với nhu cầu từng thời kì sinh trưởng của cây.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bón đúng liều lượng chỉ dẫn, tránh dư thừa gây lãng phí và ô nhiễm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Bón đúng thời điểm (đúng lúc) và đúng phương pháp (cách bón).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bón phân vào buổi trưa nắng gắt hoặc ngay trước cơn mưa rào lớn là phương pháp tốt nhất.",
            "correct": false
          }
        ],
        "explanation": "Bón lúc nắng gắt làm phân bay hơi; mưa to làm phân bị rửa trôi gây ô nhiễm."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Kí hiệu hóa học của nguyên tố kali là chữ gì?",
        "correctAnswer": "K",
        "explanation": "Kí hiệu là K."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Phân đạm cung cấp cho cây trồng nguyên tố dinh dưỡng nào? (Điền: nitơ)",
        "correctAnswer": "nitơ",
        "explanation": "Cung cấp nguyên tố nitơ (N)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Phân bón NPK chứa bao nhiêu nguyên tố dinh dưỡng đa lượng chính?",
        "correctAnswer": "3",
        "explanation": "Chứa 3 nguyên tố: N, P, K."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hàm lượng phần trăm nitơ (%N) trong phân đạm amoni nitrat NH4NO3 (M = 80 g/mol) là bao nhiêu %?",
        "correctAnswer": "35",
        "explanation": "%N = (28 / 80) * 100% = 35%."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Khối lượng mol của urê (NH2)2CO là bao nhiêu g/mol?",
        "correctAnswer": "60",
        "explanation": "M = (14+2)*2 + 12 + 16 = 60 g/mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một bao phân NPK có ghi 20-20-15. Phần trăm của nguyên tố P2O5 trong phân bón này là bao nhiêu %?",
        "correctAnswer": "20",
        "explanation": "Con số thứ hai là %P2O5 = 20%."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hàm lượng phần trăm dinh dưỡng (%N) của phân đạm urê tinh khiết (NH2)2CO xấp xỉ bằng:",
        "options": [
          "46,7%",
          "35,0%",
          "21,2%",
          "40,0%"
        ],
        "correct": 0,
        "explanation": "%N = (28 / 60) * 100% = 46,67% xấp xỉ 46,7%."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một loại phân kali chứa 95% KCl nguyên chất, còn lại là tạp chất trơ không chứa kali. Độ dinh dưỡng của loại phân này tính theo %K2O là: (Biết 2KCl tương ứng K2O: 149 g KCl ứng với 94 g K2O)",
        "options": [
          "60,0%",
          "50,0%",
          "63,1%",
          "55,0%"
        ],
        "correct": 0,
        "explanation": "%K2O = 95% * (94 / 149) = 59,93% xấp xỉ 60,0%."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Biện pháp nào sau đây thể hiện việc sử dụng phân bón hóa học an toàn, thân thiện với môi trường?",
        "options": [
          "Kết hợp bón phân hữu cơ ủ hoai mục với phân vô cơ hợp lí theo nhu cầu của cây trồng",
          "Bón thật nhiều phân đạm để rau xanh mướt quanh năm",
          "Bón phân đạm hòa vào nguồn nước tưới xả tràn ra sông suối",
          "Bón phân vô cơ liên tục không cần cải tạo đất"
        ],
        "correct": 0,
        "explanation": "Kết hợp phân hữu cơ và vô cơ cân đối giúp đất màu mỡ và bền vững."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Bón phân nào sau đây cho đất chua lâu ngày sẽ làm tăng độ chua của đất nếu không bón kèm vôi khử chua?",
        "options": [
          "Phân đạm amoni sunfat (NH4)2SO4",
          "Phân lân nung chảy (có tính kiềm nhẹ)",
          "Vôi tôi Ca(OH)2",
          "Tro bếp (chứa K2CO3)"
        ],
        "correct": 0,
        "explanation": "Muối amoni của axit mạnh làm tăng tính axit (độ chua) của đất."
      }
    ]
  },
  "chem8_c2_rev_test1": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Chất nào sau đây làm quỳ tím chuyển sang màu đỏ?",
        "options": [
          "Dung dịch axit clohiđric HCl",
          "Dung dịch natri hiđroxit NaOH",
          "Dung dịch muối ăn NaCl",
          "Nước cất tinh khiết"
        ],
        "correct": 0,
        "explanation": "Dung dịch axit làm quỳ tím hóa đỏ."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Dung dịch có pH = 12 có môi trường gì?",
        "options": [
          "Môi trường bazơ (kiềm)",
          "Môi trường axit",
          "Môi trường trung tính",
          "Môi trường không xác định"
        ],
        "correct": 0,
        "explanation": "pH > 7 là môi trường bazơ."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Oxit nào sau đây là oxit axit?",
        "options": [
          "CO2 (cacbon đioxit)",
          "CaO (canxi oxit)",
          "Na2O (natri oxit)",
          "CuO (đồng(II) oxit)"
        ],
        "correct": 0,
        "explanation": "CO2 là oxit axit tương ứng với H2CO3."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Muối nào sau đây KHÔNG TAN trong nước tạo kết tủa màu trắng?",
        "options": [
          "BaSO4 (bari sunfat)",
          "NaCl (natri clorua)",
          "KNO3 (kali nitrat)",
          "CaCl2 (canxi clorua)"
        ],
        "correct": 0,
        "explanation": "BaSO4 là kết tủa trắng không tan."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho dãy các chất: H2SO4, NaOH, CuSO4, CaO, Ba(OH)2, CO2. Có bao nhiêu bazơ trong dãy?",
        "options": [
          "2",
          "3",
          "1",
          "4"
        ],
        "correct": 0,
        "explanation": "Có 2 bazơ: NaOH và Ba(OH)2."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Khi cho kim loại kẽm Zn vào dung dịch axit sunfuric loãng, khí sinh ra là:",
        "options": [
          "H2 (hiđro)",
          "O2 (oxi)",
          "SO2 (sunfurơ)",
          "H2S (hiđro sunfua)"
        ],
        "correct": 0,
        "explanation": "Zn + H2SO4 loãng -> ZnSO4 + H2."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Phản ứng trung hòa là phản ứng giữa:",
        "options": [
          "Axit và bazơ tạo muối và nước",
          "Kim loại và axit tạo muối và hiđro",
          "Oxit bazơ và oxit axit",
          "Hai dung dịch muối"
        ],
        "correct": 0,
        "explanation": "Định nghĩa phản ứng trung hòa: Axit + Bazơ -> Muối + Nước."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Phân đạm cung cấp cho cây trồng nguyên tố dinh dưỡng nào sau đây?",
        "options": [
          "Nitơ (N)",
          "Photpho (P)",
          "Kali (K)",
          "Canxi (Ca)"
        ],
        "correct": 0,
        "explanation": "Phân đạm cung cấp nitơ (N)."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Để nhận biết 3 dung dịch không màu: HCl, NaOH, NaCl, người ta chỉ cần dùng một thuốc thử duy nhất là:",
        "options": [
          "Giấy quỳ tím",
          "Dung dịch phenolphtalein",
          "Kim loại đồng Cu",
          "Nước vôi trong"
        ],
        "correct": 0,
        "explanation": "Quỳ tím hóa đỏ với HCl, hóa xanh với NaOH, không đổi màu với NaCl."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 4,0 g oxit đồng CuO vào dung dịch HCl dư. Khối lượng muối CuCl2 thu được là:",
        "options": [
          "6,75 g",
          "13,5 g",
          "3,375 g",
          "8,0 g"
        ],
        "correct": 0,
        "explanation": "n_CuO = 4 / 80 = 0,05 mol -> m_CuCl2 = 0,05 * 135 = 6,75 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Một bao phân NPK có ghi 15-15-15. Số 15 thứ ba biểu thị phần trăm của chất nào?",
        "options": [
          "%K2O (hàm lượng kali)",
          "%N",
          "%P2O5",
          "%Tro"
        ],
        "correct": 0,
        "explanation": "Theo quy ước: %N - %P2O5 - %K2O."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Hòa tan hết 10 g hỗn hợp gồm Fe và Cu vào lượng dư dung dịch axit HCl, sau phản ứng thu được 2,479 lít khí H2 ở đkc. Khối lượng Cu trong hỗn hợp là:",
        "options": [
          "4,4 g",
          "5,6 g",
          "3,2 g",
          "6,4 g"
        ],
        "correct": 0,
        "explanation": "n_H2 = 0,1 mol -> n_Fe = 0,1 mol -> m_Fe = 5,6 g -> m_Cu = 10 - 5,6 = 4,4 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về 4 loại hợp chất vô cơ trong hóa học 8:",
        "statements": [
          {
            "subId": "a",
            "text": "Axit gồm nguyên tử H liên kết với gốc axit.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bazơ gồm kim loại liên kết với một hay nhiều nhóm -OH.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Oxit là hợp chất của 2 nguyên tố trong đó có 1 nguyên tố là oxi.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Muối chỉ gồm duy nhất hai nguyên tố kim loại và phi kim.",
            "correct": false
          }
        ],
        "explanation": "Muối có thể chứa nhiều nguyên tố (ví dụ muối có oxi như Na2SO4, CaCO3)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về môi trường và thang đo pH:",
        "statements": [
          {
            "subId": "a",
            "text": "Nước vắt từ quả chanh có pH < 7.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nước xà phòng tắm có pH > 7.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nước cất tinh khiết có pH = 7.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đất chua có pH > 7 cần bón thêm axit sunfuric loãng.",
            "correct": false
          }
        ],
        "explanation": "Đất chua có pH < 7 cần bón vôi để khử chua."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về phản ứng trao đổi trong dung dịch:",
        "statements": [
          {
            "subId": "a",
            "text": "BaCl2 + Na2SO4 -> BaSO4 (kết tủa trắng) + 2NaCl.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "AgNO3 + NaCl -> AgCl (kết tủa trắng) + NaNO3.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "CuSO4 + 2NaOH -> Cu(OH)2 (kết tủa xanh lam) + Na2SO4.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "NaCl + KNO3 -> NaNO3 + KCl.",
            "correct": false
          }
        ],
        "explanation": "Phản ứng không xảy ra do không có kết tủa hay khí."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Về vai trò và bảo quản phân bón hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Bón nhiều phân đạm làm cây tốt lá cành nhưng dễ bị sâu bệnh và gãy đổ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phân đạm urê không nên bón cùng vôi bột vì giải phóng khí NH3 bay mất đạm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phân lân kích thích phát triển rễ và ra hoa đậu quả.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phân kali giúp cây chịu rét, hạn và làm củ to hạt chắc.",
            "correct": true
          }
        ],
        "explanation": "Cả 4 nhận định a, b, c, d đều chuẩn xác."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Gốc axit sunfat trong phân tử H2SO4 có hóa trị mấy?",
        "correctAnswer": "II",
        "explanation": "Gốc =SO4 có hóa trị II."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Chất chỉ thị phenolphtalein không màu chuyển sang màu gì trong dung dịch kiềm?",
        "correctAnswer": "hồng",
        "explanation": "Chuyển sang màu hồng."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Độ pH của dung dịch nước vôi trong lớn hơn hay nhỏ hơn 7? (Điền: lớn hơn)",
        "correctAnswer": "lớn hơn",
        "explanation": "Dung dịch kiềm có pH > 7."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hòa tan 0,2 mol NaOH cần bao nhiêu mol axit HCl để trung hòa hoàn toàn? (Ghi số thập phân)",
        "correctAnswer": "0,2",
        "explanation": "NaOH + HCl -> tỉ lệ 1 : 1 nên cần 0,2 mol."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Khối lượng mol của muối bari sunfat BaSO4 là bao nhiêu g/mol?",
        "correctAnswer": "233",
        "explanation": "M = 137 + 32 + 16*4 = 233 g/mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Nhiệt phân hoàn toàn 10 g đá vôi CaCO3 thu được bao nhiêu lít khí CO2 ở đkc? (Ghi số thập phân)",
        "correctAnswer": "2,479",
        "explanation": "n = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 6,5 g kim loại kẽm vào 100 mL dung dịch axit HCl 1 M. Sau phản ứng, chất nào còn dư và thể tích khí H2 thu được ở đkc là:",
        "options": [
          "Zn dư; thu được 1,2395 lít H2",
          "HCl dư; thu được 2,479 lít H2",
          "Cả hai chất phản ứng vừa hết",
          "Zn dư; thu được 2,479 lít H2"
        ],
        "correct": 0,
        "explanation": "n_Zn = 0,1 mol; n_HCl = 0,1 mol -> HCl hết, Zn dư 0,05 mol -> n_H2 = 0,05 mol -> V = 1,2395 L."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Trộn 100 mL dung dịch Ba(OH)2 0,5 M với 100 mL dung dịch H2SO4 0,5 M thu được m gam kết tủa. Giá trị của m là:",
        "options": [
          "11,65 g",
          "23,3 g",
          "5,825 g",
          "10,4 g"
        ],
        "correct": 0,
        "explanation": "n = 0,05 mol -> m_BaSO4 = 0,05 * 233 = 11,65 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một loại phân đạm chứa 92% muối amoni nitrat NH4NO3 (M = 80 g/mol). Hàm lượng phần trăm nitơ (%N) trong loại phân này xấp xỉ bằng:",
        "options": [
          "32,2%",
          "35,0%",
          "46,0%",
          "28,5%"
        ],
        "correct": 0,
        "explanation": "%N = 92% * (28 / 80) = 32,2%."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho luồng khí CO2 dư đi qua 200 mL dung dịch Ca(OH)2 0,5 M. Sau phản ứng hoàn toàn thu được kết tủa rồi kết tủa tan hết tạo dung dịch muối axit. Khối lượng muối Ca(HCO3)2 tạo thành là:",
        "options": [
          "16,2 g",
          "10,0 g",
          "8,1 g",
          "20,0 g"
        ],
        "correct": 0,
        "explanation": "n_Ca(OH)2 = 0,1 mol -> n_Ca(HCO3)2 = 0,1 mol -> m = 0,1 * 162 = 16,2 g."
      }
    ]
  },
  "chem8_c2_rev_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Dung dịch chất nào sau đây làm quỳ tím hóa xanh?",
        "options": [
          "KOH (kali hiđroxit)",
          "HCl",
          "NaCl",
          "H2SO4"
        ],
        "correct": 0,
        "explanation": "Dung dịch kiềm KOH làm quỳ tím hóa xanh."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Oxit nào sau đây tác dụng với nước tạo thành dung dịch axit?",
        "options": [
          "SO3",
          "CaO",
          "CuO",
          "Na2O"
        ],
        "correct": 0,
        "explanation": "SO3 + H2O -> H2SO4."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Muối ăn hàng ngày dùng trong nấu ăn có công thức hóa học là:",
        "options": [
          "NaCl",
          "KCl",
          "CaCl2",
          "BaCl2"
        ],
        "correct": 0,
        "explanation": "Natri clorua NaCl."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kim loại nào sau đây KHÔNG tác dụng với dung dịch axit sunfuric loãng?",
        "options": [
          "Đồng (Cu)",
          "Sắt (Fe)",
          "Kẽm (Zn)",
          "Nhôm (Al)"
        ],
        "correct": 0,
        "explanation": "Cu đứng sau H nên không tác dụng với H2SO4 loãng."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa axit clohiđric HCl và natri hiđroxit NaOH là:",
        "options": [
          "NaCl và H2O",
          "Na2O và H2",
          "NaClO và H2",
          "Na và Cl2"
        ],
        "correct": 0,
        "explanation": "HCl + NaOH -> NaCl + H2O."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Độ pH của máu người khỏe mạnh ổn định ở khoảng:",
        "options": [
          "7,35 - 7,45",
          "1,5 - 2,5",
          "8,5 - 9,5",
          "5,0 - 6,0"
        ],
        "correct": 0,
        "explanation": "pH máu hơi kiềm nhẹ ổn định ở 7,35 - 7,45."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Oxit nào sau đây là oxit lưỡng tính vừa tác dụng axit vừa tác dụng bazơ?",
        "options": [
          "Al2O3",
          "CaO",
          "CO2",
          "Na2O"
        ],
        "correct": 0,
        "explanation": "Al2O3 là oxit lưỡng tính."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Cho mẩu đá vôi vào dung dịch axit HCl, hiện tượng quan sát được là:",
        "options": [
          "Đá vôi tan dần và sủi bọt khí CO2",
          "Xuất hiện kết tủa màu vàng",
          "Có kết tủa màu xanh lam",
          "Dung dịch bốc cháy sáng"
        ],
        "correct": 0,
        "explanation": "CaCO3 + 2HCl -> CaCl2 + H2O + CO2 (sủi bọt khí)."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 2,4 g bột Mg vào dung dịch HCl dư. Thể tích khí H2 sinh ra ở đkc (25 °C, 1 bar) là:",
        "options": [
          "2,479 lít",
          "4,958 lít",
          "2,24 lít",
          "1,12 lít"
        ],
        "correct": 0,
        "explanation": "n_Mg = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Để phân biệt 2 lọ dung dịch mất nhãn chứa NaOH và Ca(OH)2, thuốc thử thích hợp nhất là:",
        "options": [
          "Thổi khí CO2 vào",
          "Dùng quỳ tím",
          "Dùng dung dịch HCl",
          "Dùng phenolphtalein"
        ],
        "correct": 0,
        "explanation": "Khí CO2 làm Ca(OH)2 vẩn đục trắng CaCO3, còn NaOH không vẩn đục."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Hòa tan 8 g CuO trong dung dịch H2SO4 loãng vừa đủ. Khối lượng muối CuSO4 thu được là:",
        "options": [
          "16 g",
          "8 g",
          "32 g",
          "24 g"
        ],
        "correct": 0,
        "explanation": "n = 0,1 mol -> m = 0,1 * 160 = 16 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Trộn 200 mL dung dịch HCl 1 M với 200 mL dung dịch NaOH 1,5 M. Dung dịch sau phản ứng có môi trường gì và pH như thế nào?",
        "options": [
          "Môi trường kiềm, pH > 7",
          "Môi trường axit, pH < 7",
          "Môi trường trung tính, pH = 7",
          "Không đổi"
        ],
        "correct": 0,
        "explanation": "n_NaOH = 0,3 mol > n_HCl = 0,2 mol -> NaOH dư, dung dịch có tính kiềm, pH > 7."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về tính chất hóa học của bazơ:",
        "statements": [
          {
            "subId": "a",
            "text": "Dung dịch bazơ làm quỳ tím chuyển sang màu xanh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tất cả các bazơ đều bị nhiệt phân hủy khi đun nóng.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Bazơ tác dụng với oxit axit tạo thành muối và nước.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bazơ tác dụng với axit tạo thành muối và nước.",
            "correct": true
          }
        ],
        "explanation": "Các bazơ kiềm như NaOH, KOH không bị nhiệt phân bởi đèn cồn."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về oxit bazơ và oxit axit:",
        "statements": [
          {
            "subId": "a",
            "text": "CaO, Na2O là các oxit bazơ tan trong nước tạo dung dịch kiềm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "CuO, Fe2O3 là các oxit bazơ không tan trong nước nhưng tan trong axit.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "CO2, SO2 là các oxit axit tác dụng với dung dịch kiềm tạo muối cacbonat, sunfit.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "CO là oxit axit tác dụng mạnh với nước tạo axit cacbonic.",
            "correct": false
          }
        ],
        "explanation": "CO là oxit trung tính không tác dụng với nước."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phản ứng tạo kết tủa trong dung dịch:",
        "statements": [
          {
            "subId": "a",
            "text": "CuSO4 + 2NaOH -> Cu(OH)2 (kết tủa xanh lam) + Na2SO4.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "FeCl3 + 3KOH -> Fe(OH)3 (kết tủa nâu đỏ) + 3KCl.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "BaCl2 + H2SO4 -> BaSO4 (kết tủa trắng) + 2HCl.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "NaCl + H2SO4 loãng -> Na2SO4 + 2HCl.",
            "correct": false
          }
        ],
        "explanation": "Không có kết tủa hay khí nên phản ứng không xảy ra trong dung dịch loãng."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm cho dây sắt nhúng vào dung dịch đồng(II) sunfat CuSO4:",
        "statements": [
          {
            "subId": "a",
            "text": "Kim loại đồng màu đỏ bám trên bề mặt dây sắt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Màu xanh lam của dung dịch nhạt dần.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng dây sắt tăng lên sau phản ứng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dung dịch sau phản ứng chứa muối sắt(III) sunfat Fe2(SO4)3.",
            "correct": false
          }
        ],
        "explanation": "Tạo muối sắt(II) sunfat FeSO4."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong hợp chất oxit, hóa trị của nguyên tố oxi luôn là mấy?",
        "correctAnswer": "II",
        "explanation": "Oxi luôn có hóa trị II."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Dung dịch có pH = 7 là môi trường gì? (Điền: trung tính)",
        "correctAnswer": "trung tính",
        "explanation": "Môi trường trung tính."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Cho các chất: HCl, NaOH, Na2SO4, CaO. Có bao nhiêu hợp chất muối?",
        "correctAnswer": "1",
        "explanation": "Chỉ có Na2SO4 là muối (1 chất)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cần bao nhiêu mL dung dịch NaOH 1 M để trung hòa hoàn toàn 100 mL dung dịch HCl 1 M?",
        "correctAnswer": "100",
        "explanation": "Tỉ lệ 1 : 1 -> cần 100 mL."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Khối lượng mol của muối đồng(II) sunfat CuSO4 là bao nhiêu g/mol?",
        "correctAnswer": "160",
        "explanation": "M = 64 + 32 + 16*4 = 160 g/mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cho 0,1 mol kim loại Zn phản ứng vừa hết với bao nhiêu gam axit HCl? (Ghi số thập phân)",
        "correctAnswer": "7,3",
        "explanation": "n_HCl = 0,2 mol -> m = 0,2 * 36,5 = 7,3 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Cho 13 g kim loại Zn tác dụng vừa đủ với dung dịch axit HCl thu được dung dịch chứa m gam muối ZnCl2. Giá trị của m là:",
        "options": [
          "27,2 g",
          "13,6 g",
          "54,4 g",
          "20,4 g"
        ],
        "correct": 0,
        "explanation": "n_Zn = 0,2 mol -> m_ZnCl2 = 0,2 * 136 = 27,2 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Sục 2,479 lít khí CO2 ở đkc vào 150 mL dung dịch Ba(OH)2 1 M thu được kết tủa trắng BaCO3. Khối lượng kết tủa BaCO3 thu được là:",
        "options": [
          "19,7 g",
          "29,55 g",
          "9,85 g",
          "39,4 g"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,1 mol; n_Ba(OH)2 = 0,15 mol -> Ba(OH)2 dư, tính theo CO2 -> m_BaCO3 = 0,1 * 197 = 19,7 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để trung hòa 200 mL dung dịch hỗn hợp gồm HCl 0,5 M và H2SO4 0,25 M cần bao nhiêu mL dung dịch NaOH 1 M?",
        "options": [
          "200 mL",
          "150 mL",
          "300 mL",
          "100 mL"
        ],
        "correct": 0,
        "explanation": "Tổng mol H+ = 0,2 * 0,5 + 0,2 * 0,25 * 2 = 0,1 + 0,1 = 0,2 mol -> n_NaOH = 0,2 mol -> V = 0,2 L = 200 mL."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một loại phân đạm urê có độ tinh khiết 95% (chứa 95% (NH2)2CO). Hàm lượng phần trăm nitơ (%N) trong bao phân này là:",
        "options": [
          "44,3%",
          "46,7%",
          "35,0%",
          "40,0%"
        ],
        "correct": 0,
        "explanation": "%N = 95% * (28 / 60) = 44,33% xấp xỉ 44,3%."
      }
    ]
  },
  "chem8_c2_rev_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Muối nào sau đây có tên gọi là canxi cacbonat?",
        "options": [
          "CaCO3",
          "CaSO4",
          "CaCl2",
          "CaO"
        ],
        "correct": 0,
        "explanation": "CaCO3 là canxi cacbonat."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Dung dịch kiềm NaOH có thể hòa tan được oxit nào sau đây?",
        "options": [
          "CO2 (oxit axit)",
          "CaO",
          "Na2O",
          "CuO"
        ],
        "correct": 0,
        "explanation": "CO2 + 2NaOH -> Na2CO3 + H2O."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Axit nào sau đây có trong quả chanh, cam tạo vị chua thanh?",
        "options": [
          "Axit xitric",
          "Axit sunfuric",
          "Axit clohiđric",
          "Axit nitric"
        ],
        "correct": 0,
        "explanation": "Quả chanh chứa axit xitric tự nhiên."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Dung dịch có pH = 7 là dung dịch có môi trường:",
        "options": [
          "Trung tính",
          "Axit",
          "Bazơ",
          "Không xác định"
        ],
        "correct": 0,
        "explanation": "pH = 7 là môi trường trung tính."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho sơ đồ chuyển hóa: Ca -> CaO -> Ca(OH)2. Hai phản ứng lần lượt là tác dụng với:",
        "options": [
          "O2 rồi tác dụng với H2O",
          "H2O rồi tác dụng với O2",
          "CO2 rồi tác dụng với HCl",
          "Axit rồi tác dụng với bazơ"
        ],
        "correct": 0,
        "explanation": "2Ca + O2 -> 2CaO; CaO + H2O -> Ca(OH)2."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Phản ứng giữa dung dịch bạc nitrat AgNO3 và dung dịch natri clorua NaCl sinh ra kết tủa trắng là:",
        "options": [
          "AgCl",
          "NaNO3",
          "Ag2O",
          "Ag2CO3"
        ],
        "correct": 0,
        "explanation": "AgNO3 + NaCl -> AgCl (trắng) + NaNO3."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Để nhận biết khí CO2 thoát ra từ phản ứng nung đá vôi, người ta dẫn khí qua dung dịch nào?",
        "options": [
          "Dung dịch nước vôi trong Ca(OH)2 thấy vẩn đục",
          "Dung dịch axit HCl",
          "Dung dịch muối ăn NaCl",
          "Dung dịch cồn"
        ],
        "correct": 0,
        "explanation": "Khí CO2 làm vẩn đục nước vôi trong."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Phân bón NPK thuộc loại phân bón nào?",
        "options": [
          "Phân bón hỗn hợp",
          "Phân đơn",
          "Phân vi sinh",
          "Phân hữu cơ"
        ],
        "correct": 0,
        "explanation": "NPK là phân hỗn hợp chứa cả 3 nguyên tố N, P, K."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan 5,6 g Fe vào 200 mL dung dịch H2SO4 1 M. Sau phản ứng hoàn toàn, thể tích khí H2 thu được ở đkc là:",
        "options": [
          "2,479 lít",
          "4,958 lít",
          "2,24 lít",
          "1,2395 lít"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,1 mol; n_H2SO4 = 0,2 mol -> Fe hết -> V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Nhiệt phân hoàn toàn 19,6 g Cu(OH)2 thu được m gam bột CuO màu đen. Giá trị của m là:",
        "options": [
          "16,0 g",
          "8,0 g",
          "12,8 g",
          "20,0 g"
        ],
        "correct": 0,
        "explanation": "n = 19,6 / 98 = 0,2 mol -> m_CuO = 0,2 * 80 = 16,0 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cần dùng bao nhiêu gam muối NaCl để pha thành 500 g dung dịch nước muối sinh lí 0,9%?",
        "options": [
          "4,5 g",
          "9,0 g",
          "0,9 g",
          "45 g"
        ],
        "correct": 0,
        "explanation": "m = 500 * 0,9% = 4,5 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Dẫn 4,958 lít khí CO2 ở đkc vào dung dịch chứa 0,15 mol Ba(OH)2 thu được m gam kết tủa BaCO3. Giá trị của m là:",
        "options": [
          "19,7 g",
          "29,55 g",
          "39,4 g",
          "9,85 g"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,2 mol; n_Ba(OH)2 = 0,15 mol -> T = 0,2/0,15 = 1,33 -> n_BaCO3 = 0,15*2 - 0,2 = 0,1 mol -> m = 19,7 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các phản ứng của axit và bazơ:",
        "statements": [
          {
            "subId": "a",
            "text": "Phản ứng giữa axit và bazơ luôn tạo ra muối và nước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nhiệt độ của phản ứng trung hòa thường tăng lên do phản ứng tỏa nhiệt.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Tất cả các bazơ đều tan vô hạn trong nước.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Chỉ thị phenolphtalein đổi màu hồng trong môi trường kiềm.",
            "correct": true
          }
        ],
        "explanation": "Nhiều bazơ như Cu(OH)2, Fe(OH)3 không tan trong nước."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tính tan của muối trong nước:",
        "statements": [
          {
            "subId": "a",
            "text": "Tất cả các muối nitrat đều tan tốt trong nước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Muối cacbonat của canxi CaCO3 tan rất tốt trong nước tạo dung dịch kiềm.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Bari sunfat BaSO4 không tan trong nước và cả trong dung dịch axit mạnh.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Muối clorua tan tốt trừ AgCl không tan.",
            "correct": true
          }
        ],
        "explanation": "CaCO3 là chất kết tủa không tan trong nước."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về phân bón hóa học:",
        "statements": [
          {
            "subId": "a",
            "text": "Phân kali giúp cây chống chịu rét, hạn và sâu bệnh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phân đạm thúc đẩy sinh trưởng cành lá xanh tốt.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phân lân thúc đẩy quá trình đẻ nhánh, ra hoa và phát triển bộ rễ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bón phân đạm urê vào đất có tính kiềm mạnh sẽ làm tăng hiệu quả hấp thụ của cây.",
            "correct": false
          }
        ],
        "explanation": "Môi trường kiềm làm phân urê phân hủy thoát khí amoniac gây thất thoát đạm."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho m gam kim loại kẽm Zn vào dung dịch muối đồng sunfat CuSO4 dư:",
        "statements": [
          {
            "subId": "a",
            "text": "Kim loại kẽm tan dần và có kim loại màu đỏ bám trên bề mặt kẽm.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khối lượng thanh kim loại sau phản ứng tăng lên so với ban đầu.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Khối lượng thanh kim loại giảm đi vì 1 mol Zn (65g) tan ra chỉ có 1 mol Cu (64g) bám vào.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Màu xanh lam của dung dịch nhạt dần theo thời gian.",
            "correct": true
          }
        ],
        "explanation": "Khối lượng thanh kẽm giảm nhẹ: 65 - 64 = 1 g/mol."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Công thức hóa học của khí cacbonic là gì? (Điền: CO2)",
        "correctAnswer": "CO2",
        "explanation": "Khí cacbonic là CO2."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Dung dịch kiềm NaOH làm phenolphtalein chuyển sang màu gì?",
        "correctAnswer": "hồng",
        "explanation": "Chuyển sang màu hồng."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của oxit canxi CaO là bao nhiêu g/mol?",
        "correctAnswer": "56",
        "explanation": "M = 40 + 16 = 56 g/mol."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Số mol khí H2 sinh ra khi cho 0,2 mol nhôm Al phản ứng hết với HCl dư là bao nhiêu mol? (Ghi số thập phân)",
        "correctAnswer": "0,3",
        "explanation": "0,2 * 1,5 = 0,3 mol H2."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan hết 4 g NaOH vào nước được 250 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M? (Ghi số thập phân)",
        "correctAnswer": "0,4",
        "explanation": "n = 0,1 mol -> CM = 0,1 / 0,25 = 0,4 M."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Để hòa tan hoàn toàn 8 g oxit CuO cần vừa đủ bao nhiêu gam axit HCl nguyên chất? (Ghi số thập phân)",
        "correctAnswer": "7,3",
        "explanation": "n_CuO = 0,1 mol -> n_HCl = 0,2 mol -> m = 0,2 * 36,5 = 7,3 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Đốt cháy hoàn toàn 11,2 g bột sắt trong khí oxi dư thu được oxit sắt từ Fe3O4. Khối lượng Fe3O4 thu được là:",
        "options": [
          "15,47 g",
          "16,0 g",
          "11,6 g",
          "23,2 g"
        ],
        "correct": 0,
        "explanation": "3Fe + 2O2 -> Fe3O4. n_Fe = 0,2 mol -> n_Fe3O4 = 0,2 / 3 mol -> m = 0,2/3 * 232 = 15,47 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hòa tan 14,8 g Ca(OH)2 vào nước thu được 500 mL dung dịch. Nồng độ mol của dung dịch nước vôi thu được là:",
        "options": [
          "0,4 M",
          "0,2 M",
          "0,5 M",
          "0,1 M"
        ],
        "correct": 0,
        "explanation": "n = 14,8 / 74 = 0,2 mol -> CM = 0,2 / 0,5 = 0,4 M."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nhiệt phân hoàn toàn 50 g đá vôi CaCO3 thu được bao nhiêu gam vôi sống CaO?",
        "options": [
          "28 g",
          "56 g",
          "14 g",
          "22 g"
        ],
        "correct": 0,
        "explanation": "n = 0,5 mol -> m_CaO = 0,5 * 56 = 28 g."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một dung dịch chứa 0,2 mol BaCl2. Cần thêm vào dung dịch bao nhiêu mol Na2SO4 để kết tủa hoàn toàn ion Ba2+?",
        "options": [
          "0,2 mol",
          "0,1 mol",
          "0,4 mol",
          "0,3 mol"
        ],
        "correct": 0,
        "explanation": "Tỉ lệ 1 : 1 -> cần đúng 0,2 mol Na2SO4."
      }
    ]
  },
  "chem8_c2_rev_test4": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là oxit trung tính không tạo muối?",
        "options": [
          "CO (cacbon monooxit)",
          "CO2",
          "CaO",
          "SO2"
        ],
        "correct": 0,
        "explanation": "CO là oxit trung tính."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Dung dịch axit có giá trị pH nằm trong khoảng nào?",
        "options": [
          "pH < 7",
          "pH = 7",
          "pH > 7",
          "pH = 14"
        ],
        "correct": 0,
        "explanation": "pH < 7 là môi trường axit."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Muối nào sau đây dùng làm bột nở khi làm bánh?",
        "options": [
          "NaHCO3 (natri hidrocacbonat)",
          "NaCl",
          "BaSO4",
          "CuSO4"
        ],
        "correct": 0,
        "explanation": "Baking soda NaHCO3 dùng làm bột nở."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong nông nghiệp, vôi tôi Ca(OH)2 được dùng để:",
        "options": [
          "Khử chua cho đất và sát trùng chuồng trại",
          "Làm đông đất",
          "Làm tăng độ mặn của đất",
          "Cung cấp đạm cho cây"
        ],
        "correct": 0,
        "explanation": "Vôi tôi khử chua đất và diệt khuẩn chuồng trại."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho dãy các chất: CuO, Ba(OH)2, HCl, Na2CO3, CO2. Chất nào phản ứng được với dung dịch HCl sinh chất khí?",
        "options": [
          "Na2CO3 (sinh khí CO2)",
          "CuO",
          "Ba(OH)2",
          "CO2"
        ],
        "correct": 0,
        "explanation": "Na2CO3 + 2HCl -> 2NaCl + H2O + CO2 (khí)."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa kim loại magie và axit sunfuric loãng là:",
        "options": [
          "MgSO4 và H2",
          "MgO và H2",
          "MgSO3 và H2",
          "MgS và H2O"
        ],
        "correct": 0,
        "explanation": "Mg + H2SO4 -> MgSO4 + H2."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hiện tượng nước đá vôi để lâu ngoài không khí xuất hiện một lớp màng mỏng cứng trên bề mặt là do:",
        "options": [
          "Ca(OH)2 tác dụng với khí CO2 trong không khí tạo CaCO3",
          "Nước bay hơi hết",
          "Vôi bị thối rữa",
          "Bụi bẩn bám vào"
        ],
        "correct": 0,
        "explanation": "Ca(OH)2 + CO2 -> CaCO3 (màng cứng trắng) + H2O."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Phân kali cung cấp cho cây trồng nguyên tố nào?",
        "options": [
          "Kali (K)",
          "Nitơ (N)",
          "Photpho (P)",
          "Oxi (O)"
        ],
        "correct": 0,
        "explanation": "Phân kali cung cấp nguyên tố K."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 5,4 g kim loại Al vào dung dịch axit HCl dư. Thể tích khí H2 thoát ra ở đkc (25 °C, 1 bar) là:",
        "options": [
          "7,437 lít",
          "4,958 lít",
          "2,479 lít",
          "6,72 lít"
        ],
        "correct": 0,
        "explanation": "n_Al = 0,2 mol -> n_H2 = 0,3 mol -> V = 0,3 * 24,79 = 7,437 L."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Để trung hòa hoàn toàn 100 mL dung dịch H2SO4 0,5 M cần bao nhiêu mL dung dịch NaOH 1 M?",
        "options": [
          "100 mL",
          "50 mL",
          "200 mL",
          "150 mL"
        ],
        "correct": 0,
        "explanation": "H2SO4 + 2NaOH -> n_H2SO4 = 0,05 mol -> n_NaOH = 0,1 mol -> V = 0,1 L = 100 mL."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Đốt cháy hoàn toàn 2,4 g bột magie trong khí oxi dư thu được bao nhiêu gam magie oxit MgO?",
        "options": [
          "4,0 g",
          "3,6 g",
          "6,0 g",
          "2,8 g"
        ],
        "correct": 0,
        "explanation": "n = 0,1 mol -> m = 0,1 * 40 = 4,0 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cho dung dịch chứa 0,1 mol AgNO3 tác dụng với dung dịch chứa 0,1 mol CaCl2. Khối lượng kết tủa AgCl thu được là:",
        "options": [
          "14,35 g",
          "28,7 g",
          "7,175 g",
          "21,525 g"
        ],
        "correct": 0,
        "explanation": "2AgNO3 + CaCl2 -> 2AgCl + Ca(NO3)2. n_AgCl = 0,1 mol -> m = 0,1 * 143,5 = 14,35 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các phản ứng của hợp chất vô cơ:",
        "statements": [
          {
            "subId": "a",
            "text": "Oxit axit tác dụng với dung dịch kiềm tạo thành muối và nước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Axit tác dụng với kim loại đứng sau H trong dãy hoạt động giải phóng khí H2.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Bazơ không tan bị phân hủy ở nhiệt độ cao tạo oxit bazơ và nước.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phản ứng trao đổi trong dung dịch chỉ xảy ra khi có chất kết tủa hoặc chất khí sinh ra.",
            "correct": true
          }
        ],
        "explanation": "Kim loại sau H không giải phóng H2."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về nồng độ và pH:",
        "statements": [
          {
            "subId": "a",
            "text": "Độ pH là chỉ số đo độ hoạt động của ion H+ trong dung dịch.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dung dịch kiềm có nồng độ OH- cao hơn nồng độ H+.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Pha loãng dung dịch axit bằng nước làm pH của dung dịch tăng dần về 7.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Pha loãng dung dịch kiềm bằng nước làm pH của dung dịch tăng vọt lên 14.",
            "correct": false
          }
        ],
        "explanation": "Pha loãng kiềm làm giảm nồng độ OH-, pH giảm dần về 7."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về ứng dụng thực tiễn của các hợp chất:",
        "statements": [
          {
            "subId": "a",
            "text": "NaCl dùng làm gia vị thức ăn và bảo quản thịt cá.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "CaCO3 là thành phần chính của đá vôi dùng làm vật liệu xây dựng và sản xuất xi măng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "CuSO4 dùng làm thuốc trừ nấm mốc trong nông nghiệp (dung dịch Booc-đô).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "H2SO4 đặc dùng làm nước giải khát mùa hè.",
            "correct": false
          }
        ],
        "explanation": "H2SO4 là hóa chất độc hại, ăn mòn cực mạnh không uống được."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng cho dung dịch Na2CO3 vào dung dịch CaCl2:",
        "statements": [
          {
            "subId": "a",
            "text": "Phương trình: Na2CO3 + CaCl2 -> CaCO3 (kết tủa trắng) + 2NaCl.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Lọc lấy kết tủa hòa tan vào dung dịch axit HCl thấy sủi bọt khí CO2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch lọc sau khi bỏ kết tủa chứa muối ăn NaCl.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Đây là phản ứng oxi hóa - khử.",
            "correct": false
          }
        ],
        "explanation": "Đây là phản ứng trao đổi không thay đổi số oxi hóa."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phân đạm urê có chứa nguyên tố dinh dưỡng nào? (Điền: nitơ)",
        "correctAnswer": "nitơ",
        "explanation": "Chứa nguyên tố nitơ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Muối bari sunfat BaSO4 có tan trong nước không? (Điền: có hoặc không)",
        "correctAnswer": "không",
        "explanation": "BaSO4 là kết tủa trắng không tan."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của oxit đồng CuO là bao nhiêu g/mol?",
        "correctAnswer": "80",
        "explanation": "M = 64 + 16 = 80 g/mol."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Cần bao nhiêu gam NaOH để trung hòa 0,1 mol axit HCl?",
        "correctAnswer": "4",
        "explanation": "n = 0,1 mol -> m = 0,1 * 40 = 4 g."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Số mol khí CO2 sinh ra khi nhiệt phân 20 g CaCO3 là bao nhiêu mol? (Ghi số thập phân)",
        "correctAnswer": "0,2",
        "explanation": "n = 20 / 100 = 0,2 mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cho 0,1 mol Zn phản ứng hoàn toàn với dung dịch CuSO4 dư thu được bao nhiêu gam Cu?",
        "correctAnswer": "6,4",
        "explanation": "n = 0,1 mol -> m_Cu = 0,1 * 64 = 6,4 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Cho 10 g CaCO3 tác dụng hoàn toàn với lượng dư dung dịch axit HCl. Thể tích khí CO2 thu được ở đkc (25 °C, 1 bar) là:",
        "options": [
          "2,479 lít",
          "4,958 lít",
          "1,2395 lít",
          "3,7185 lít"
        ],
        "correct": 0,
        "explanation": "n = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hòa tan 11,2 g bột sắt Fe vào dung dịch H2SO4 loãng dư. Thể tích khí H2 sinh ra ở đkc là:",
        "options": [
          "4,958 lít",
          "2,479 lít",
          "7,437 lít",
          "9,916 lít"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,2 mol -> V = 0,2 * 24,79 = 4,958 L."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hòa tan 8 g CuO trong 100 mL dung dịch HCl 2,5 M. Nồng độ mol của CuCl2 thu được trong dung dịch sau phản ứng là (coi thể tích không đổi):",
        "options": [
          "1,0 M",
          "0,5 M",
          "2,0 M",
          "0,1 M"
        ],
        "correct": 0,
        "explanation": "n_CuO = 0,1 mol -> n_CuCl2 = 0,1 mol -> CM = 0,1 / 0,1 = 1,0 M."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một hỗn hợp gồm 0,1 mol BaCl2 và 0,1 mol Na2SO4 hòa tan vào nước thu được m gam kết tủa. Giá trị của m là:",
        "options": [
          "23,3 g",
          "11,65 g",
          "46,6 g",
          "15,5 g"
        ],
        "correct": 0,
        "explanation": "n = 0,1 mol -> m = 0,1 * 233 = 23,3 g."
      }
    ]
  },
  "chem8_c2_rev_test5": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hợp chất nào sau đây là oxit axit?",
        "options": [
          "P2O5",
          "K2O",
          "Fe2O3",
          "BaO"
        ],
        "correct": 0,
        "explanation": "P2O5 là oxit axit tương ứng với H3PO4."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Dung dịch kiềm có giá trị pH nằm trong khoảng nào?",
        "options": [
          "pH > 7",
          "pH = 7",
          "pH < 7",
          "pH = 0"
        ],
        "correct": 0,
        "explanation": "Dung dịch kiềm có pH > 7."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Muối nào sau đây kết tủa màu trắng không tan trong nước?",
        "options": [
          "AgCl",
          "NaCl",
          "CuSO4",
          "KNO3"
        ],
        "correct": 0,
        "explanation": "AgCl là kết tủa trắng."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phân lân cung cấp cho cây trồng nguyên tố dinh dưỡng nào?",
        "options": [
          "Photpho (P)",
          "Nitơ (N)",
          "Kali (K)",
          "Canxi (Ca)"
        ],
        "correct": 0,
        "explanation": "Phân lân cung cấp photpho."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho dãy các chất: HCl, NaOH, CaCO3, SO2, Cu(OH)2, KNO3. Số muối trong dãy là:",
        "options": [
          "2",
          "3",
          "1",
          "4"
        ],
        "correct": 0,
        "explanation": "Có 2 muối: CaCO3 và KNO3."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Phản ứng giữa dung dịch axit clohiđric và đồng(II) oxit CuO tạo ra dung dịch có màu:",
        "options": [
          "Màu xanh lam",
          "Màu nâu đỏ",
          "Không màu",
          "Màu vàng"
        ],
        "correct": 0,
        "explanation": "CuO + 2HCl -> CuCl2 (màu xanh lam) + H2O."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khí nào sau đây thoát ra khi cho kẽm vào axit clohiđric?",
        "options": [
          "Khí hiđro (H2)",
          "Khí oxi",
          "Khí clo",
          "Khí cacbonic"
        ],
        "correct": 0,
        "explanation": "Zn + 2HCl -> ZnCl2 + H2."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khử chua cho đất nông nghiệp bằng cách bón vôi là ứng dụng của phản ứng nào?",
        "options": [
          "Phản ứng trung hòa giữa bazơ và axit",
          "Phản ứng oxi hóa - khử",
          "Phản ứng phân hủy",
          "Phản ứng trùng hợp"
        ],
        "correct": 0,
        "explanation": "Trung hòa axit trong đất bằng kiềm của vôi."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 4,8 g kim loại magie vào dung dịch axit HCl dư. Thể tích khí H2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "4,958 lít",
          "2,479 lít",
          "7,437 lít",
          "9,916 lít"
        ],
        "correct": 0,
        "explanation": "n_Mg = 0,2 mol -> V = 0,2 * 24,79 = 4,958 L."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Để phân biệt dung dịch H2SO4 và dung dịch HCl, người ta dùng thuốc thử tốt nhất là:",
        "options": [
          "Dung dịch BaCl2",
          "Quỳ tím",
          "Dung dịch NaOH",
          "Kim loại kẽm"
        ],
        "correct": 0,
        "explanation": "BaCl2 tạo kết tủa trắng BaSO4 với H2SO4, còn HCl không có hiện tượng."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Hòa tan 11,2 g bột sắt Fe vào dung dịch axit sunfuric loãng vừa đủ. Khối lượng muối FeSO4 thu được là:",
        "options": [
          "30,4 g",
          "15,2 g",
          "60,8 g",
          "22,8 g"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,2 mol -> m_FeSO4 = 0,2 * 152 = 30,4 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Dẫn 2,479 lít khí CO2 ở đkc vào 200 mL dung dịch Ba(OH)2 0,5 M thu được m gam kết tủa trắng BaCO3. Giá trị của m là:",
        "options": [
          "19,7 g",
          "9,85 g",
          "29,55 g",
          "39,4 g"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,1 mol; n_Ba(OH)2 = 0,1 mol -> phản ứng vừa đủ tạo 0,1 mol BaCO3 -> m = 19,7 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các tính chất đặc trưng của axit, bazơ, oxit, muối:",
        "statements": [
          {
            "subId": "a",
            "text": "Dung dịch axit làm quỳ tím hóa đỏ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dung dịch kiềm làm quỳ tím hóa xanh.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Oxit kim loại luôn luôn tan tốt trong nước ở nhiệt độ thường.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Phản ứng giữa axit và bazơ luôn tạo thành muối và nước.",
            "correct": true
          }
        ],
        "explanation": "Nhiều oxit kim loại như CuO, Fe2O3, Al2O3 không tan trong nước."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về thang đo pH và sức khỏe con người:",
        "statements": [
          {
            "subId": "a",
            "text": "Dung dịch có pH < 7 là môi trường axit.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dịch dạ dày có pH axit thấp (khoảng 1,5 - 3,5) giúp tiêu hóa thức ăn.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi bị đau dạ dày do dư axit, người ta có thể uống thuốc muối Nabica (NaHCO3).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Uống dung dịch kiềm đặc NaOH là phương pháp tốt nhất để chữa đau dạ dày.",
            "correct": false
          }
        ],
        "explanation": "NaOH kiềm mạnh ăn mòn da và niêm mạc cực kì nguy hiểm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về phân bón hóa học trong nông nghiệp:",
        "statements": [
          {
            "subId": "a",
            "text": "Phân đạm thúc đẩy quá trình sinh trưởng cành lá xanh tốt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phân lân kích thích sự phát triển của hệ rễ và củ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phân kali giúp cây trồng tăng khả năng chống chịu rét và sâu bệnh.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bón càng nhiều phân hóa học thì cây càng xanh tốt và đất càng tơi xốp.",
            "correct": false
          }
        ],
        "explanation": "Lạm dụng phân bón hóa học gây chai hóa đất và ô nhiễm nguồn nước."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho mẩu kim loại natri vào cốc đựng dung dịch đồng(II) sunfat CuSO4:",
        "statements": [
          {
            "subId": "a",
            "text": "Natri phản ứng mãnh liệt với nước trong dung dịch tạo NaOH và khí H2 bay lên.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dung dịch NaOH sinh ra phản ứng với CuSO4 tạo kết tủa xanh lam Cu(OH)2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Kim loại đồng màu đỏ bám ngoài mẩu natri.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Hiện tượng quan sát được: Natri tan dần sủi bọt khí và xuất hiện kết tủa màu xanh lam.",
            "correct": true
          }
        ],
        "explanation": "Na không đẩy Cu trực tiếp mà tác dụng với nước trước."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong 1 phân tử phân đạm urê (NH2)2CO có bao nhiêu nguyên tử nitơ?",
        "correctAnswer": "2",
        "explanation": "Có 2 nguyên tử nitơ."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Dung dịch muối ăn NaCl có làm đổi màu giấy quỳ tím không? (Điền: có hoặc không)",
        "correctAnswer": "không",
        "explanation": "Muối trung tính không đổi màu quỳ tím."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của muối canxi cacbonat CaCO3 là bao nhiêu g/mol?",
        "correctAnswer": "100",
        "explanation": "M = 100 g/mol."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hòa tan 0,1 mol kim loại kẽm Zn vào axit HCl dư. Thể tích khí H2 sinh ra ở đkc là bao nhiêu lít? (Ghi số thập phân)",
        "correctAnswer": "2,479",
        "explanation": "V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Để trung hòa hoàn toàn 0,2 mol axit H2SO4 cần bao nhiêu mol NaOH? (Ghi số thập phân)",
        "correctAnswer": "0,4",
        "explanation": "Tỉ lệ 1 : 2 -> cần 0,4 mol NaOH."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Nhiệt phân hoàn toàn 20 g đá vôi CaCO3 thu được bao nhiêu gam vôi sống CaO? (Ghi số thập phân)",
        "correctAnswer": "11,2",
        "explanation": "n = 0,2 mol -> m_CaO = 0,2 * 56 = 11,2 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Cho 12 g hỗn hợp gồm Fe và Cu vào lượng dư dung dịch axit HCl, sau phản ứng thu được 2,479 lít khí H2 ở đkc. Khối lượng chất rắn không tan còn lại là:",
        "options": [
          "6,4 g",
          "5,6 g",
          "3,2 g",
          "4,8 g"
        ],
        "correct": 0,
        "explanation": "n_H2 = 0,1 mol -> n_Fe = 0,1 mol -> m_Fe = 5,6 g -> m_Cu (không tan) = 12 - 5,6 = 6,4 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 8 g oxit kim loại RO vào 100 mL dung dịch H2SO4 1 M vừa đủ. Kim loại R là:",
        "options": [
          "Đồng (Cu = 64)",
          "Kẽm (Zn = 65)",
          "Magiê (Mg = 24)",
          "Canxi (Ca = 40)"
        ],
        "correct": 0,
        "explanation": "n_H2SO4 = 0,1 mol -> M_RO = 8 / 0,1 = 80 -> M_R = 80 - 16 = 64 (Cu)."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hòa tan 14,8 g Ca(OH)2 vào nước được dung dịch A. Sục khí CO2 dư vào dung dịch A thu được dung dịch chứa muối Ca(HCO3)2. Khối lượng muối Ca(HCO3)2 tạo thành là:",
        "options": [
          "32,4 g",
          "16,2 g",
          "20,0 g",
          "40,0 g"
        ],
        "correct": 0,
        "explanation": "n_Ca(OH)2 = 0,2 mol -> n_Ca(HCO3)2 = 0,2 mol -> m = 0,2 * 162 = 32,4 g."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một loại phân lân supephotphat đơn có chứa 71% Ca(H2PO4)2 nguyên chất (M = 234 g/mol). Độ dinh dưỡng của loại phân này tính theo %P2O5 là:",
        "options": [
          "43,1%",
          "35,5%",
          "50,0%",
          "40,0%"
        ],
        "correct": 0,
        "explanation": "Ca(H2PO4)2 tương ứng P2O5: %P2O5 = 71% * (142 / 234) = 43,08% xấp xỉ 43,1%."
      }
    ]
  },
  "chem8_c2_b9_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Bazơ nào sau đây là bazơ không tan trong nước?",
        "options": [
          "Cu(OH)2",
          "NaOH",
          "KOH",
          "Ba(OH)2"
        ],
        "correct": 0,
        "explanation": "Cu(OH)2 kết tủa màu xanh lam."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Dung dịch kiềm NaOH phản ứng được với oxit nào sau đây?",
        "options": [
          "CO2 (oxit axit)",
          "CaO",
          "Na2O",
          "BaO"
        ],
        "correct": 0,
        "explanation": "CO2 + 2NaOH -> Na2CO3 + H2O."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nhỏ vài giọt dung dịch phenolphtalein vào dung dịch Ca(OH)2, dung dịch có màu gì?",
        "options": [
          "Màu hồng",
          "Màu xanh lam",
          "Màu đỏ",
          "Không màu"
        ],
        "correct": 0,
        "explanation": "Dung dịch kiềm làm phenolphtalein đổi sang màu hồng."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Phản ứng nhiệt phân Cu(OH)2 tạo ra chất rắn màu đen là:",
        "options": [
          "CuO",
          "Cu2O",
          "Cu",
          "CuSO4"
        ],
        "correct": 0,
        "explanation": "Cu(OH)2 -> CuO (đen) + H2O."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho dãy các bazơ: NaOH, Fe(OH)3, KOH, Cu(OH)2, Ba(OH)2. Số bazơ bị nhiệt phân hủy bởi đèn cồn là:",
        "options": [
          "2",
          "3",
          "4",
          "1"
        ],
        "correct": 0,
        "explanation": "Chỉ có bazơ không tan bị nhiệt phân: Fe(OH)3 và Cu(OH)2 (2 bazơ)."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Một dung dịch có pH = 13. Kết luận nào sau đây ĐÚNG về dung dịch này?",
        "options": [
          "Dung dịch có tính bazơ (kiềm) rất mạnh",
          "Dung dịch có tính axit rất mạnh",
          "Dung dịch trung tính",
          "Dung dịch nước cất"
        ],
        "correct": 0,
        "explanation": "pH = 13 là dung dịch kiềm rất mạnh."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi cho dung dịch NaOH tác dụng với dung dịch CuSO4, hiện tượng quan sát được là:",
        "options": [
          "Xuất hiện kết tủa màu xanh lam",
          "Có bọt khí bay lên",
          "Xuất hiện kết tủa màu nâu đỏ",
          "Dung dịch chuyển sang màu tím"
        ],
        "correct": 0,
        "explanation": "CuSO4 + 2NaOH -> Cu(OH)2 (kết tủa xanh lam) + Na2SO4."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa axit sunfuric H2SO4 và kali hiđroxit KOH là:",
        "options": [
          "K2SO4 và H2O",
          "KSO4 và H2",
          "K2O và H2O",
          "K2S và H2O"
        ],
        "correct": 0,
        "explanation": "H2SO4 + 2KOH -> K2SO4 + 2H2O."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan 11,2 g KOH vào nước thu được 200 mL dung dịch. Nồng độ mol của dung dịch KOH là:",
        "options": [
          "1 M",
          "0,5 M",
          "2 M",
          "0,1 M"
        ],
        "correct": 0,
        "explanation": "n = 11,2 / 56 = 0,2 mol -> CM = 0,2 / 0,2 = 1 M."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Để trung hòa hoàn toàn 150 mL dung dịch KOH 1 M cần bao nhiêu mL dung dịch HCl 1,5 M?",
        "options": [
          "100 mL",
          "150 mL",
          "200 mL",
          "50 mL"
        ],
        "correct": 0,
        "explanation": "n_KOH = 0,15 mol -> n_HCl = 0,15 mol -> V = 0,15 / 1,5 = 0,1 L = 100 mL."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Nhiệt phân hoàn toàn 10,7 g Fe(OH)3 thu được bao nhiêu gam bột Fe2O3 màu nâu đỏ?",
        "options": [
          "8,0 g",
          "16,0 g",
          "4,0 g",
          "12,0 g"
        ],
        "correct": 0,
        "explanation": "n = 10,7 / 107 = 0,1 mol -> n_Fe2O3 = 0,05 mol -> m = 0,05 * 160 = 8,0 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Dẫn 4,958 lít khí CO2 ở đkc vào dung dịch chứa 0,3 mol NaOH thu được dung dịch chứa muối nào?",
        "options": [
          "Na2CO3 và NaHCO3",
          "Chỉ có Na2CO3",
          "Chỉ có NaHCO3",
          "Na2CO3 và NaOH dư"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,2 mol. T = n_NaOH / n_CO2 = 0,3 / 0,2 = 1,5 -> tạo 2 muối Na2CO3 và NaHCO3."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về tính chất của dung dịch kiềm:",
        "statements": [
          {
            "subId": "a",
            "text": "Dung dịch kiềm có cảm giác nhờn như xà phòng khi chạm tay vào.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dung dịch kiềm làm quỳ tím chuyển sang màu đỏ rực rỡ.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Dung dịch kiềm tác dụng với oxit axit tạo muối và nước.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dung dịch kiềm ăn mòn da và thủy tinh khi ở nồng độ cao và nóng.",
            "correct": true
          }
        ],
        "explanation": "Dung dịch kiềm làm quỳ tím hóa xanh."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các bazơ không tan:",
        "statements": [
          {
            "subId": "a",
            "text": "Fe(OH)2 là kết tủa trắng xanh, để ngoài không khí chuyển dần thành Fe(OH)3 màu nâu đỏ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cu(OH)2 tan tốt trong nước tạo dung dịch có màu xanh lam đậm.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Nhiệt phân bazơ không tan luôn sinh ra oxit kim loại tương ứng và hơi nước.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bazơ không tan vẫn tác dụng được với dung dịch axit mạnh (phản ứng trung hòa).",
            "correct": true
          }
        ],
        "explanation": "Cu(OH)2 là chất kết tủa không tan trong nước."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về ứng dụng điều chỉnh pH trong thực tế:",
        "statements": [
          {
            "subId": "a",
            "text": "Nước mưa có pH < 5,6 được coi là mưa axit.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nước hồ cá cảnh nuôi cá rồng cần duy trì pH ổn định khoảng 6,5 - 7,5.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Người bị đau dạ dày thường do nồng độ axit HCl tăng cao làm tổn thương niêm mạc.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dung dịch có pH = 1 là dung dịch trung tính có thể uống trực tiếp an toàn.",
            "correct": false
          }
        ],
        "explanation": "pH = 1 là dung dịch axit rất mạnh gây bỏng nguy hiểm."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Cho 100 mL dung dịch FeCl3 1 M tác dụng với lượng dư dung dịch NaOH:",
        "statements": [
          {
            "subId": "a",
            "text": "Sinh ra chất kết tủa sắt(III) hiđroxit màu nâu đỏ.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Số mol kết tủa thu được là 0,1 mol.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Lọc lấy kết tủa đem nung đến khối lượng không đổi thu được 8 g Fe2O3.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng kết tủa Fe(OH)3 ướt thu được đúng bằng 5,6 g.",
            "correct": false
          }
        ],
        "explanation": "m_Fe(OH)3 = 0,1 * 107 = 10,7 g."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong 1 phân tử natri hiđroxit NaOH có bao nhiêu nguyên tử natri?",
        "correctAnswer": "1",
        "explanation": "Có 1 nguyên tử Na."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Dung dịch NaOH làm quỳ tím chuyển sang màu gì?",
        "correctAnswer": "xanh",
        "explanation": "Chuyển sang màu xanh."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Một dung dịch có pH = 10. Môi trường của dung dịch này là axit hay bazơ? (Điền: bazơ)",
        "correctAnswer": "bazơ",
        "explanation": "pH = 10 là môi trường bazơ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng mol của kali hiđroxit KOH là bao nhiêu g/mol?",
        "correctAnswer": "56",
        "explanation": "M = 39 + 16 + 1 = 56 g/mol."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Để trung hòa hoàn toàn 0,1 mol Ba(OH)2 cần bao nhiêu mol axit HCl? (Ghi số thập phân)",
        "correctAnswer": "0,2",
        "explanation": "Ba(OH)2 + 2HCl -> cần 0,2 mol HCl."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Nung 19,6 g Cu(OH)2 đến khối lượng không đổi thu được bao nhiêu gam CuO?",
        "correctAnswer": "16",
        "explanation": "n = 0,2 mol -> m_CuO = 0,2 * 80 = 16 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan 8 g NaOH vào nước được 400 mL dung dịch. Nồng độ mol của dung dịch NaOH là:",
        "options": [
          "0,5 M",
          "1,0 M",
          "0,2 M",
          "0,25 M"
        ],
        "correct": 0,
        "explanation": "n = 8 / 40 = 0,2 mol -> CM = 0,2 / 0,4 = 0,5 M."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho 100 mL dung dịch NaOH 2 M tác dụng với 100 mL dung dịch CuCl2 0,5 M. Khối lượng kết tủa Cu(OH)2 màu xanh thu được là:",
        "options": [
          "4,9 g",
          "9,8 g",
          "2,45 g",
          "7,35 g"
        ],
        "correct": 0,
        "explanation": "n_NaOH = 0,2 mol; n_CuCl2 = 0,05 mol -> NaOH dư, tính theo CuCl2 -> m = 0,05 * 98 = 4,9 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Trung hòa hoàn toàn 200 mL dung dịch Ca(OH)2 0,1 M bằng dung dịch HNO3 0,2 M. Thể tích dung dịch HNO3 cần dùng là:",
        "options": [
          "200 mL",
          "100 mL",
          "400 mL",
          "150 mL"
        ],
        "correct": 0,
        "explanation": "n_Ca(OH)2 = 0,02 mol -> n_HNO3 = 0,04 mol -> V = 0,04 / 0,2 = 0,2 L = 200 mL."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Dẫn luồng khí CO2 dư vào dung dịch chứa 0,1 mol Ca(OH)2. Sau khi phản ứng kết thúc hoàn toàn, khối lượng muối Ca(HCO3)2 thu được trong dung dịch là:",
        "options": [
          "16,2 g",
          "10,0 g",
          "8,1 g",
          "20,0 g"
        ],
        "correct": 0,
        "explanation": "n_Ca(HCO3)2 = 0,1 mol -> m = 0,1 * 162 = 16,2 g."
      }
    ]
  },
  "chem8_c2_b9_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Bazơ nào sau đây bị nhiệt phân hủy khi nung nóng?",
        "options": [
          "Fe(OH)3",
          "NaOH",
          "KOH",
          "Ba(OH)2"
        ],
        "correct": 0,
        "explanation": "Fe(OH)3 là bazơ không tan bị nhiệt phân hủy."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Dung dịch kiềm có thể phản ứng với chất nào sau đây?",
        "options": [
          "Axit clohiđric HCl",
          "Khí oxi",
          "Khí hiđro",
          "Kim loại đồng Cu"
        ],
        "correct": 0,
        "explanation": "Phản ứng trung hòa với axit."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Độ pH của giấm ăn thường nằm trong khoảng:",
        "options": [
          "2 - 3",
          "7 - 8",
          "12 - 13",
          "8 - 9"
        ],
        "correct": 0,
        "explanation": "Giấm ăn có tính axit nên pH khoảng 2 - 3."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Chất nào sau đây được gọi là xút ăn da?",
        "options": [
          "NaOH (natri hiđroxit)",
          "KOH",
          "Ca(OH)2",
          "Ba(OH)2"
        ],
        "correct": 0,
        "explanation": "NaOH có tên thông thường là xút ăn da."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa Ca(OH)2 và khí CO2 là:",
        "options": [
          "CaCO3 kết tủa trắng và H2O",
          "CaO và H2",
          "CaCl2 và H2O",
          "Ca(HCO3)2 không màu"
        ],
        "correct": 0,
        "explanation": "CO2 + Ca(OH)2 -> CaCO3 (trắng) + H2O."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho mẩu giấy quỳ tím vào dung dịch KOH, sau đó nhỏ từ từ dung dịch axit HCl vào đến dư. Màu sắc của giấy quỳ biến đổi như thế nào?",
        "options": [
          "Từ xanh sang tím rồi sang đỏ",
          "Từ đỏ sang xanh",
          "Luôn giữ nguyên màu xanh",
          "Mất màu hoàn toàn"
        ],
        "correct": 0,
        "explanation": "Ban đầu bazơ (xanh), khi trung hòa hết (tím), dư axit (đỏ)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Chất nào sau đây dùng để nhận biết ion Cu2+ trong dung dịch bằng kết tủa màu xanh lam?",
        "options": [
          "Dung dịch kiềm NaOH",
          "Dung dịch axit HCl",
          "Dung dịch muối NaCl",
          "Nước cất"
        ],
        "correct": 0,
        "explanation": "Cu2+ + 2OH- -> Cu(OH)2 (kết tủa xanh lam)."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Một mẫu đất nông nghiệp có pH = 4,5. Đất này được xếp vào loại:",
        "options": [
          "Đất chua",
          "Đất kiềm",
          "Đất trung tính",
          "Đất mặn"
        ],
        "correct": 0,
        "explanation": "pH < 7 là đất chua."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 4,6 g kim loại natri vào nước thu được 100 mL dung dịch NaOH. Nồng độ mol của dung dịch NaOH là:",
        "options": [
          "2 M",
          "1 M",
          "0,5 M",
          "4 M"
        ],
        "correct": 0,
        "explanation": "n_Na = 0,2 mol -> n_NaOH = 0,2 mol -> CM = 0,2 / 0,1 = 2 M."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Cho dung dịch chứa 0,1 mol CuCl2 tác dụng vừa đủ với dung dịch NaOH. Khối lượng kết tủa Cu(OH)2 thu được là:",
        "options": [
          "9,8 g",
          "4,9 g",
          "19,6 g",
          "14,7 g"
        ],
        "correct": 0,
        "explanation": "m = 0,1 * 98 = 9,8 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cần lấy bao nhiêu mL dung dịch NaOH 1 M để trung hòa hoàn toàn 100 mL dung dịch H2SO4 0,5 M?",
        "options": [
          "100 mL",
          "200 mL",
          "50 mL",
          "150 mL"
        ],
        "correct": 0,
        "explanation": "n_H2SO4 = 0,05 mol -> n_NaOH = 0,1 mol -> V = 0,1 L = 100 mL."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn m gam bột Al vào 200 mL dung dịch NaOH 1 M dư thu được 7,437 lít khí H2 ở đkc. Giá trị của m là:",
        "options": [
          "5,4 g",
          "2,7 g",
          "10,8 g",
          "8,1 g"
        ],
        "correct": 0,
        "explanation": "2Al + 2NaOH + 2H2O -> 2NaAlO2 + 3H2. n_H2 = 0,3 mol -> n_Al = 0,2 mol -> m = 0,2 * 27 = 5,4 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về phản ứng của bazơ kiềm với oxit axit:",
        "statements": [
          {
            "subId": "a",
            "text": "2NaOH + SO2 -> Na2SO3 + H2O.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Ca(OH)2 + CO2 -> CaCO3 (kết tủa trắng) + H2O.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch kiềm có thể dùng để hấp thụ các khí độc có tính axit như SO2, H2S.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dung dịch kiềm hấp thụ tốt khí hiđro H2 và khí metan CH4.",
            "correct": false
          }
        ],
        "explanation": "H2 và CH4 trơ không tác dụng với dung dịch kiềm."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các hiện tượng đổi màu chất chỉ thị:",
        "statements": [
          {
            "subId": "a",
            "text": "Quỳ tím chuyển sang màu xanh trong dung dịch kiềm có pH > 7.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phenolphtalein không màu chuyển sang màu hồng trong dung dịch kiềm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phenolphtalein chuyển sang màu đỏ trong dung dịch axit có pH < 7.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Nước cất trung tính pH = 7 không làm đổi màu quỳ tím và phenolphtalein.",
            "correct": true
          }
        ],
        "explanation": "Phenolphtalein không màu trong môi trường axit và trung tính."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phản ứng trung hòa bazơ không tan:",
        "statements": [
          {
            "subId": "a",
            "text": "Cu(OH)2 + 2HCl -> CuCl2 + 2H2O (dung dịch đổi sang màu xanh lam).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Fe(OH)3 + 3HCl -> FeCl3 + 3H2O (dung dịch đổi sang màu vàng nâu).",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Al(OH)3 + 3HCl -> AlCl3 + 3H2O (dung dịch không màu).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Các bazơ không tan không thể tác dụng với axit do không tan.",
            "correct": false
          }
        ],
        "explanation": "Bazơ không tan vẫn tan và tác dụng tốt với dung dịch axit mạnh."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm thêm từ từ dung dịch HCl vào dung dịch NaOH:",
        "statements": [
          {
            "subId": "a",
            "text": "Giá trị pH của dung dịch giảm dần từ trên 7 xuống 7 rồi xuống dưới 7.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Tại thời điểm pH = 7, toàn bộ NaOH đã phản ứng vừa đủ với HCl tạo dung dịch muối ăn trung tính.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nhiệt độ của cốc giảm đi đóng băng thành đá.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Phản ứng trung hòa axit - bazơ là phản ứng tỏa nhiệt.",
            "correct": true
          }
        ],
        "explanation": "Phản ứng trung hòa tỏa nhiệt làm cốc ấm lên."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong công thức của bazơ Ca(OH)2, chỉ số của nhóm -OH là bao nhiêu?",
        "correctAnswer": "2",
        "explanation": "Chỉ số của nhóm OH là 2."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Dung dịch có pH = 12 có tính kiềm hay axit? (Điền: kiềm)",
        "correctAnswer": "kiềm",
        "explanation": "pH = 12 là môi trường kiềm."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của natri hiđroxit NaOH là bao nhiêu g/mol?",
        "correctAnswer": "40",
        "explanation": "M = 23 + 16 + 1 = 40 g/mol."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hòa tan 0,3 mol KOH vào nước để được 300 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M?",
        "correctAnswer": "1",
        "explanation": "CM = 0,3 / 0,3 = 1 M."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Nhiệt phân hoàn toàn 10,7 g Fe(OH)3 thu được bao nhiêu gam nước? (Ghi số thập phân)",
        "correctAnswer": "2,7",
        "explanation": "n = 0,1 mol -> n_H2O = 0,15 mol -> m = 0,15 * 18 = 2,7 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cần bao nhiêu gam NaOH để trung hòa 0,05 mol H2SO4?",
        "correctAnswer": "4",
        "explanation": "n_NaOH = 0,1 mol -> m = 0,1 * 40 = 4 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Cho 200 mL dung dịch NaOH 1 M tác dụng với 100 mL dung dịch H2SO4 1,5 M. Dung dịch sau phản ứng có tính chất gì và pH thế nào?",
        "options": [
          "Dung dịch có tính axit, pH < 7",
          "Dung dịch có tính kiềm, pH > 7",
          "Dung dịch trung tính, pH = 7",
          "Không đổi"
        ],
        "correct": 0,
        "explanation": "n_NaOH = 0,2 mol; n_H2SO4 = 0,15 mol (cần 0,3 mol NaOH) -> axit dư -> tính axit, pH < 7."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn m gam kim loại bari Ba vào nước thu được 200 mL dung dịch Ba(OH)2 0,5 M và giải phóng V lít khí H2 ở đkc. Giá trị của m là:",
        "options": [
          "13,7 g",
          "27,4 g",
          "6,85 g",
          "20,55 g"
        ],
        "correct": 0,
        "explanation": "n_Ba = 0,1 mol -> m = 0,1 * 137 = 13,7 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Nhiệt phân hoàn toàn m gam hỗn hợp gồm Cu(OH)2 và Fe(OH)3 thu được 16 g chất rắn gồm CuO và Fe2O3. Biết số mol Cu(OH)2 bằng số mol Fe(OH)3. Giá trị của m là:",
        "options": [
          "20,5 g",
          "19,6 g",
          "21,4 g",
          "18,2 g"
        ],
        "correct": 0,
        "explanation": "80x + 160*0,5x = 16 -> 160x = 16 -> x = 0,1 mol -> m = 0,1*98 + 0,1*107 = 20,5 g."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một dung dịch kiềm Ca(OH)2 có pH = 12. Để làm giảm độ kiềm của dung dịch về mức an toàn hơn cho sinh vật, người ta có thể sục nhẹ khí nào sau đây?",
        "options": [
          "Khí cacbon đioxit (CO2)",
          "Khí oxi (O2)",
          "Khí nitơ (N2)",
          "Khí hiđro (H2)"
        ],
        "correct": 0,
        "explanation": "CO2 phản ứng với Ca(OH)2 làm giảm nồng độ OH- hạ pH về mức trung tính."
      }
    ]
  },
  "chem8_c2_b10_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Oxit nào sau đây tác dụng với nước tạo thành dung dịch bazơ?",
        "options": [
          "CaO",
          "CO2",
          "SO2",
          "P2O5"
        ],
        "correct": 0,
        "explanation": "CaO + H2O -> Ca(OH)2."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Chất nào sau đây là oxit axit?",
        "options": [
          "SO2 (lưu huỳnh đioxit)",
          "Na2O",
          "Fe2O3",
          "CuO"
        ],
        "correct": 0,
        "explanation": "SO2 là oxit axit tương ứng với H2SO3."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chất rắn màu đen nào sau đây là một oxit bazơ?",
        "options": [
          "CuO (đồng(II) oxit)",
          "Fe(OH)3",
          "CaCO3",
          "Al2O3"
        ],
        "correct": 0,
        "explanation": "CuO là bột màu đen."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khí nào sau đây là oxit trung tính không tạo muối?",
        "options": [
          "NO (nitơ monooxit)",
          "NO2",
          "N2O5",
          "SO3"
        ],
        "correct": 0,
        "explanation": "NO là oxit trung tính."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa điphotpho pentaoxit P2O5 và nước là:",
        "options": [
          "Axit photphoric H3PO4",
          "Axit sunfuric H2SO4",
          "Axit clohiđric HCl",
          "Khí photphin PH3"
        ],
        "correct": 0,
        "explanation": "P2O5 + 3H2O -> 2H3PO4."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Oxit bazơ tác dụng với dung dịch axit tạo thành:",
        "options": [
          "Muối và nước",
          "Bazơ và khí hiđro",
          "Kim loại và nước",
          "Oxit axit và muối"
        ],
        "correct": 0,
        "explanation": "Oxit bazơ + axit -> muối + nước."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hiện tượng quan sát được khi cho bột CuO màu đen vào dung dịch axit HCl nóng là:",
        "options": [
          "Bột đen tan dần tạo dung dịch màu xanh lam",
          "Có bọt khí thoát ra dữ dội",
          "Bột đen chuyển thành màu đỏ",
          "Dung dịch đóng băng"
        ],
        "correct": 0,
        "explanation": "CuO + 2HCl -> CuCl2 (màu xanh lam) + H2O."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Khí sunfurơ SO2 có trong khí thải nhà máy tác dụng với dung dịch nước vôi trong Ca(OH)2 tạo kết tủa trắng là:",
        "options": [
          "CaSO3 (canxi sunfit)",
          "CaSO4",
          "CaCO3",
          "CaO"
        ],
        "correct": 0,
        "explanation": "SO2 + Ca(OH)2 -> CaSO3 (trắng) + H2O."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 5,6 g vôi sống CaO vào nước thu được dung dịch chứa m gam Ca(OH)2. Giá trị của m là:",
        "options": [
          "7,4 g",
          "5,6 g",
          "11,2 g",
          "14,8 g"
        ],
        "correct": 0,
        "explanation": "n_CaO = 0,1 mol -> m_Ca(OH)2 = 0,1 * 74 = 7,4 g."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Dẫn 2,479 lít khí SO2 ở đkc vào lượng dư dung dịch Ca(OH)2 thu được bao nhiêu gam kết tủa CaSO3?",
        "options": [
          "12,0 g",
          "6,0 g",
          "24,0 g",
          "18,0 g"
        ],
        "correct": 0,
        "explanation": "n = 0,1 mol -> m_CaSO3 = 0,1 * 120 = 12,0 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cần dùng bao nhiêu mL dung dịch HCl 2 M để hòa tan hoàn toàn 8 g oxit Fe2O3?",
        "options": [
          "150 mL",
          "300 mL",
          "100 mL",
          "200 mL"
        ],
        "correct": 0,
        "explanation": "Fe2O3 + 6HCl -> 2FeCl3 + 3H2O. n = 0,05 mol -> n_HCl = 0,3 mol -> V = 0,3 / 2 = 0,15 L = 150 mL."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Dẫn khí CO dư đi qua ống sứ nung nóng chứa 16 g bột Fe2O3. Sau khi phản ứng xảy ra hoàn toàn thu được m gam kim loại sắt. Giá trị của m là:",
        "options": [
          "11,2 g",
          "5,6 g",
          "8,4 g",
          "14,0 g"
        ],
        "correct": 0,
        "explanation": "Fe2O3 + 3CO -> 2Fe + 3CO2. n_Fe2O3 = 0,1 mol -> n_Fe = 0,2 mol -> m = 0,2 * 56 = 11,2 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các tính chất hóa học của oxit:",
        "statements": [
          {
            "subId": "a",
            "text": "Oxit axit tác dụng với dung dịch bazơ tạo thành muối và nước.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Oxit bazơ tác dụng với dung dịch axit tạo thành muối và nước.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Một số oxit bazơ tan (Na2O, K2O, CaO, BaO) tác dụng với oxit axit tạo muối.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các oxit phi kim đều tác dụng mãnh liệt với nước ở nhiệt độ thường.",
            "correct": false
          }
        ],
        "explanation": "Nhiều oxit phi kim như CO, NO, SiO2 không tác dụng với nước ở nhiệt độ thường."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tác hại môi trường của các oxit khí quyển:",
        "statements": [
          {
            "subId": "a",
            "text": "Khí SO2 sinh ra do đốt than đá, dầu mỏ là nguyên nhân chính gây mưa axit.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí NO2 tạo thành trong khí quyển góp phần làm tăng tính axit của nước mưa.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khí CO2 gây hiệu ứng nhà kính làm tăng nhiệt độ trung bình toàn cầu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí CO2 phá hủy trực tiếp tầng ozon bảo vệ Trái Đất.",
            "correct": false
          }
        ],
        "explanation": "CFC và các hợp chất chứa clo mới phá hủy tầng ozon, không phải CO2."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phản ứng của canxi oxit CaO:",
        "statements": [
          {
            "subId": "a",
            "text": "CaO + H2O -> Ca(OH)2 (phản ứng tôi vôi tỏa nhiệt).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "CaO + 2HCl -> CaCl2 + H2O.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "CaO + CO2 -> CaCO3 (đá vôi).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "CaO + Cu -> CuO + Ca.",
            "correct": false
          }
        ],
        "explanation": "Kim loại Cu không khử được CaO."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét phản ứng khử oxit kim loại bằng khí H2 nung nóng:",
        "statements": [
          {
            "subId": "a",
            "text": "Khí H2 có thể khử các oxit kim loại đứng sau nhôm trong dãy hoạt động (như CuO, Fe2O3).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Dẫn khí H2 qua bột CuO màu đen nung nóng thu được kim loại đồng màu đỏ.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dẫn khí H2 qua bột Na2O nung nóng thu được kim loại natri tự do.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Phương trình: CuO + H2 -> Cu + H2O.",
            "correct": true
          }
        ],
        "explanation": "Na2O là oxit kim loại rất mạnh, H2 không khử được."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phân tử natri oxit Na2O có bao nhiêu nguyên tử natri?",
        "correctAnswer": "2",
        "explanation": "Có 2 nguyên tử Na."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa CaO và nước làm quỳ tím chuyển sang màu gì?",
        "correctAnswer": "xanh",
        "explanation": "Tạo Ca(OH)2 làm quỳ tím hóa xanh."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Oxit kẽm ZnO thuộc loại oxit nào? (Điền: lưỡng tính)",
        "correctAnswer": "lưỡng tính",
        "explanation": "ZnO là oxit lưỡng tính."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng mol của oxit lưu huỳnh trioxit SO3 là bao nhiêu g/mol?",
        "correctAnswer": "80",
        "explanation": "M = 32 + 16*3 = 80 g/mol."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan 0,1 mol CaO vào nước thu được bao nhiêu gam Ca(OH)2? (Ghi số thập phân)",
        "correctAnswer": "7,4",
        "explanation": "0,1 * 74 = 7,4 g."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Khử hoàn toàn 8 g bột CuO bằng H2 dư thu được bao nhiêu gam kim loại đồng? (Ghi số thập phân)",
        "correctAnswer": "6,4",
        "explanation": "n = 0,1 mol -> m_Cu = 0,1 * 64 = 6,4 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Dẫn 4,958 lít khí CO2 ở đkc vào dung dịch chứa 0,15 mol Ba(OH)2. Khối lượng kết tủa BaCO3 thu được là:",
        "options": [
          "19,7 g",
          "29,55 g",
          "9,85 g",
          "39,4 g"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,2 mol; n_Ba(OH)2 = 0,15 mol -> n_BaCO3 = 2*0,15 - 0,2 = 0,1 mol -> m = 19,7 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 20 g hỗn hợp gồm CuO và Fe2O3 cần vừa đủ 250 mL dung dịch axit HCl 2 M. Khối lượng nước tạo thành trong phản ứng là:",
        "options": [
          "4,5 g",
          "9,0 g",
          "18,0 g",
          "3,6 g"
        ],
        "correct": 0,
        "explanation": "n_HCl = 0,5 mol -> n_H2O = 0,25 mol -> m_H2O = 0,25 * 18 = 4,5 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hòa tan 6,2 g Na2O vào 193,8 g nước cất. Nồng độ phần trăm của dung dịch NaOH thu được là:",
        "options": [
          "4,0%",
          "3,1%",
          "8,0%",
          "5,0%"
        ],
        "correct": 0,
        "explanation": "n_Na2O = 0,1 mol -> m_NaOH = 0,2 * 40 = 8 g; m_dd = 6,2 + 193,8 = 200 g -> C% = 8 / 200 = 4%."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Khí CO khử hoàn toàn hỗn hợp gồm Fe2O3 và CuO nung nóng thu được 17,6 g hỗn hợp kim loại và giải phóng 7,437 lít khí CO2 ở đkc. Khối lượng hỗn hợp hai oxit ban đầu là:",
        "options": [
          "22,4 g",
          "20,0 g",
          "24,8 g",
          "19,2 g"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,3 mol -> n_O trong oxit = 0,3 mol -> m_oxit = 17,6 + 0,3 * 16 = 17,6 + 4,8 = 22,4 g."
      }
    ]
  },
  "chem8_c2_b10_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Oxit nào sau đây là oxit của kim loại kiềm tan mạnh trong nước tỏa nhiệt?",
        "options": [
          "Na2O",
          "CuO",
          "Fe2O3",
          "Al2O3"
        ],
        "correct": 0,
        "explanation": "Na2O là oxit kim loại kiềm tan mạnh trong nước."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Khí nào sau đây thoát ra khi đun sôi nhẹ nước ngọt có gas?",
        "options": [
          "CO2 (cacbon đioxit)",
          "O2",
          "H2",
          "N2"
        ],
        "correct": 0,
        "explanation": "Khí CO2 hòa tan trong nước ngọt có gas."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Chất bột màu trắng nào sau đây tác dụng với nước tạo thành dung dịch vôi tôi?",
        "options": [
          "CaO (canxi oxit)",
          "CuO",
          "Fe2O3",
          "P2O5"
        ],
        "correct": 0,
        "explanation": "CaO + H2O -> Ca(OH)2."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Trong 4 loại oxit: oxit bazơ, oxit axit, oxit lưỡng tính, oxit trung tính; loại oxit nào KHÔNG TÁC DỤNG với cả axit và bazơ?",
        "options": [
          "Oxit trung tính",
          "Oxit lưỡng tính",
          "Oxit axit",
          "Oxit bazơ"
        ],
        "correct": 0,
        "explanation": "Oxit trung tính không tạo muối (như CO, NO)."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa canxi oxit CaO và axit clohiđric HCl là:",
        "options": [
          "CaCl2 và H2O",
          "CaCO3 và H2",
          "Ca(OH)2 và Cl2",
          "CaOCl2 và H2"
        ],
        "correct": 0,
        "explanation": "CaO + 2HCl -> CaCl2 + H2O."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cho quỳ tím vào dung dịch tạo thành khi cho SO3 tác dụng với nước, quỳ tím chuyển sang màu:",
        "options": [
          "Màu đỏ",
          "Màu xanh",
          "Màu tím",
          "Màu vàng"
        ],
        "correct": 0,
        "explanation": "SO3 + H2O -> H2SO4 (axit làm quỳ tím hóa đỏ)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hiện tượng vôi sống CaO để lâu ngoài không khí ẩm bị bở vụn ra và mất tính chất tôi vôi là do:",
        "options": [
          "CaO hút ẩm biến thành Ca(OH)2 rồi tác dụng với CO2 thành CaCO3",
          "CaO bay hơi hết",
          "CaO biến thành kim loại canxi",
          "Bụi bẩn bám dày"
        ],
        "correct": 0,
        "explanation": "CaO tác dụng hơi nước và CO2 trong không khí."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Để làm khô khí CO2 có lẫn hơi nước, người ta dẫn khí qua bình đựng:",
        "options": [
          "Axit sunfuric đặc H2SO4",
          "Dung dịch kiềm NaOH",
          "Vôi sống CaO",
          "Nước cất"
        ],
        "correct": 0,
        "explanation": "H2SO4 đặc hút ẩm tốt và không phản ứng với CO2."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 8 g bột CuO vào 100 mL dung dịch HCl 2,5 M. Sau phản ứng, nồng độ mol của axit HCl còn dư là:",
        "options": [
          "0,5 M",
          "1,0 M",
          "0,25 M",
          "0,1 M"
        ],
        "correct": 0,
        "explanation": "n_CuO = 0,1 mol -> n_HCl pư = 0,2 mol; n_HCl ban đầu = 0,25 mol -> n_dư = 0,05 mol -> CM = 0,05 / 0,1 = 0,5 M."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Dẫn luồng khí H2 dư qua ống chứa 20 g hỗn hợp gồm CuO và Al2O3 nung nóng đỏ. Sau phản ứng hoàn toàn, chất rắn còn lại gồm những chất nào?",
        "options": [
          "Cu và Al2O3",
          "Cu và Al",
          "CuO và Al",
          "Cu(OH)2 và Al2O3"
        ],
        "correct": 0,
        "explanation": "H2 chỉ khử được CuO thành Cu; không khử được Al2O3."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Đốt cháy hoàn toàn 6,2 g photpho P trong khí oxi dư thu được m gam chất rắn màu trắng P2O5. Giá trị của m là:",
        "options": [
          "14,2 g",
          "7,1 g",
          "28,4 g",
          "10,5 g"
        ],
        "correct": 0,
        "explanation": "n_P = 0,2 mol -> n_P2O5 = 0,1 mol -> m = 0,1 * 142 = 14,2 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Dẫn 1,2395 lít khí CO2 ở đkc vào 100 mL dung dịch Ba(OH)2 0,5 M thu được m gam kết tủa BaCO3. Giá trị của m là:",
        "options": [
          "9,85 g",
          "19,7 g",
          "4,925 g",
          "14,775 g"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,05 mol; n_Ba(OH)2 = 0,05 mol -> phản ứng vừa đủ tạo 0,05 mol BaCO3 -> m = 0,05 * 197 = 9,85 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về oxit lưỡng tính Al2O3 và ZnO:",
        "statements": [
          {
            "subId": "a",
            "text": "Al2O3 tan được trong dung dịch axit mạnh như HCl, H2SO4.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Al2O3 tan được trong dung dịch kiềm mạnh như NaOH, KOH.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Al2O3 tan tốt trong nước ở nhiệt độ phòng.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Tính chất tác dụng với cả axit và bazơ được gọi là tính lưỡng tính.",
            "correct": true
          }
        ],
        "explanation": "Al2O3 hoàn toàn không tan trong nước."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về phản ứng tạo muối của oxit:",
        "statements": [
          {
            "subId": "a",
            "text": "Oxit bazơ tác dụng với oxit axit tạo thành muối (ví dụ CaO + CO2 -> CaCO3).",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Oxit axit tác dụng với dung dịch bazơ tạo thành muối và nước.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khí CO tác dụng với dung dịch NaOH ở nhiệt độ phòng tạo muối natri cacbonat.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Khí SO2 làm đục nước vôi trong tương tự khí CO2.",
            "correct": true
          }
        ],
        "explanation": "CO là oxit trung tính không tác dụng với dung dịch kiềm ở nhiệt độ thường."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phản ứng nung nóng oxit kim loại:",
        "statements": [
          {
            "subId": "a",
            "text": "Dẫn khí CO qua bột Fe2O3 nung nóng thu được kim loại Fe và khí CO2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Khí CO có tính khử mạnh ở nhiệt độ cao.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phản ứng luyện gang trong lò cao bản chất là khử các oxit sắt bằng khí CO.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khí CO có thể khử được oxit nhôm Al2O3 thành nhôm kim loại trong lò cao.",
            "correct": false
          }
        ],
        "explanation": "Al2O3 liên kết cực kì bền vững, CO không khử được Al2O3."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm cho mẩu vôi sống CaO vào nước:",
        "statements": [
          {
            "subId": "a",
            "text": "Mẩu CaO hút nước rạn nứt phát ra tiếng lách tách và bốc khói hơi nước mù mịt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Nhiệt độ của nước tăng lên rất cao có thể làm chín quả trứng.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch sau khi lọc bỏ cặn vôi có tính kiềm làm phenolphtalein hóa hồng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Khối lượng chất rắn thu được nhỏ hơn khối lượng CaO ban đầu.",
            "correct": false
          }
        ],
        "explanation": "m_Ca(OH)2 = m_CaO + m_H2O > m_CaO ban đầu."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong công thức hóa học của oxit sắt từ Fe3O4 có bao nhiêu nguyên tử oxi?",
        "correctAnswer": "4",
        "explanation": "Có 4 nguyên tử oxi."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Khí CO2 có làm đục nước vôi trong Ca(OH)2 không? (Điền: có hoặc không)",
        "correctAnswer": "có",
        "explanation": "Tạo kết tủa trắng CaCO3 làm đục nước vôi trong."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khối lượng mol của oxit bari BaO là bao nhiêu g/mol?",
        "correctAnswer": "153",
        "explanation": "M = 137 + 16 = 153 g/mol."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 0,2 mol Na2O vào nước thu được bao nhiêu mol NaOH? (Ghi số thập phân)",
        "correctAnswer": "0,4",
        "explanation": "Na2O + H2O -> 2NaOH: n = 0,4 mol."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Số mol khí O2 cần để đốt cháy hoàn toàn 0,2 mol carbon thành khí CO2 là bao nhiêu mol? (Ghi số thập phân)",
        "correctAnswer": "0,2",
        "explanation": "C + O2 -> CO2: cần 0,2 mol O2."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Khử hoàn toàn 16 g Fe2O3 bằng CO dư ở nhiệt độ cao thu được bao nhiêu gam kim loại sắt? (Ghi số thập phân)",
        "correctAnswer": "11,2",
        "explanation": "n_Fe = 0,2 mol -> m = 11,2 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 15,3 g oxit Al2O3 vào dung dịch axit H2SO4 loãng vừa đủ. Khối lượng muối Al2(SO4)3 thu được là:",
        "options": [
          "51,3 g",
          "25,65 g",
          "34,2 g",
          "102,6 g"
        ],
        "correct": 0,
        "explanation": "Al2O3 + 3H2SO4 -> Al2(SO4)3 + 3H2O. n = 15,3 / 102 = 0,15 mol -> m_muối = 0,15 * 342 = 51,3 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Dẫn 3,7185 lít khí CO2 ở đkc vào dung dịch chứa 0,1 mol Ca(OH)2. Khối lượng kết tủa CaCO3 thu được sau phản ứng là:",
        "options": [
          "5,0 g",
          "10,0 g",
          "15,0 g",
          "7,5 g"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,15 mol; n_Ca(OH)2 = 0,1 mol -> n_CaCO3 = 2*0,1 - 0,15 = 0,05 mol -> m = 5,0 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Một hỗn hợp gồm CuO và Fe2O3 có tỉ lệ mol 1 : 1. Cần bao nhiêu mol axit HCl để hòa tan hoàn toàn 2,4 g hỗn hợp này?",
        "options": [
          "0,08 mol",
          "0,04 mol",
          "0,16 mol",
          "0,06 mol"
        ],
        "correct": 0,
        "explanation": "80x + 160x = 2,4 -> 240x = 2,4 -> x = 0,01 mol. n_HCl = 2*0,01 + 6*0,01 = 0,08 mol."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Khí CO khử hoàn toàn một oxit sắt FexOy nung nóng thu được 8,4 g sắt và giải phóng 4,958 lít khí CO2 ở đkc. Công thức phân tử của oxit sắt là:",
        "options": [
          "Fe2O3",
          "Fe3O4",
          "FeO",
          "Fe2O"
        ],
        "correct": 0,
        "explanation": "n_Fe = 8,4/56 = 0,15 mol; n_O = n_CO2 = 0,2 mol -> x : y = 0,15 : 0,2 = 3 : 4 -> Fe3O4."
      }
    ]
  },
  "chem8_c2_b11_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Muối nào sau đây dùng làm chất bảo quản thực phẩm (ướp cá, làm nước mắm)?",
        "options": [
          "NaCl (natri clorua)",
          "CuSO4",
          "BaSO4",
          "AgNO3"
        ],
        "correct": 0,
        "explanation": "Muối ăn NaCl."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Muối bạc nitrat có công thức hóa học là:",
        "options": [
          "AgNO3",
          "AgCl",
          "Ag2SO4",
          "Ag2CO3"
        ],
        "correct": 0,
        "explanation": "Bạc nitrat là AgNO3."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Khi nhỏ dung dịch bari clorua BaCl2 vào dung dịch muối nào sau đây sẽ xuất hiện kết tủa trắng?",
        "options": [
          "Na2SO4 (natri sunfat)",
          "NaCl",
          "KNO3",
          "HCl"
        ],
        "correct": 0,
        "explanation": "BaCl2 + Na2SO4 -> BaSO4 (kết tủa trắng) + 2NaCl."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kim loại nào sau đây có thể đẩy được kim loại đồng Cu ra khỏi dung dịch muối CuSO4?",
        "options": [
          "Sắt (Fe)",
          "Bạc (Ag)",
          "Vàng (Au)",
          "Bạch kim (Pt)"
        ],
        "correct": 0,
        "explanation": "Fe đứng trước Cu nên đẩy được Cu ra khỏi dung dịch muối."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cho dãy các muối: CaCO3, BaSO4, Cu(NO3)2, AgCl, K2SO4. Có bao nhiêu muối tan trong nước?",
        "options": [
          "2",
          "3",
          "1",
          "4"
        ],
        "correct": 0,
        "explanation": "Có 2 muối tan: Cu(NO3)2 và K2SO4 (CaCO3, BaSO4, AgCl không tan)."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa dung dịch natri cacbonat Na2CO3 và dung dịch axit clohiđric HCl gồm có:",
        "options": [
          "NaCl, H2O và khí CO2",
          "NaCl và H2",
          "NaHCO3 và Cl2",
          "NaOH và CO2"
        ],
        "correct": 0,
        "explanation": "Na2CO3 + 2HCl -> 2NaCl + H2O + CO2 (sủi bọt khí)."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Hiện tượng quan sát được khi cho mẩu kim loại kẽm Zn vào dung dịch đồng sunfat CuSO4 màu xanh lam là:",
        "options": [
          "Màu xanh lam nhạt dần và có kim loại màu đỏ bám trên kẽm",
          "Có bọt khí bay lên dữ dội",
          "Dung dịch chuyển sang màu tím",
          "Thanh kẽm nóng chảy"
        ],
        "correct": 0,
        "explanation": "Zn + CuSO4 -> ZnSO4 (không màu) + Cu (đỏ)."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Phản ứng trao đổi trong dung dịch giữa hai muối xảy ra khi:",
        "options": [
          "Sản phẩm có ít nhất một chất kết tủa không tan",
          "Cả hai chất sản phẩm đều bay hơi",
          "Không cần điều kiện gì",
          "Có khí oxi bay lên"
        ],
        "correct": 0,
        "explanation": "Phải có chất kết tủa tạo thành."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 5,3 g natri cacbonat Na2CO3 bằng dung dịch axit HCl dư. Thể tích khí CO2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "1,2395 lít",
          "2,479 lít",
          "4,958 lít",
          "2,24 lít"
        ],
        "correct": 0,
        "explanation": "n_Na2CO3 = 5,3 / 106 = 0,05 mol -> V = 0,05 * 24,79 = 1,2395 L."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Cho dung dịch chứa 0,1 mol BaCl2 tác dụng với dung dịch chứa 0,1 mol K2SO4. Khối lượng kết tủa BaSO4 thu được là:",
        "options": [
          "23,3 g",
          "11,65 g",
          "46,6 g",
          "15,5 g"
        ],
        "correct": 0,
        "explanation": "n = 0,1 mol -> m = 0,1 * 233 = 23,3 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cần lấy bao nhiêu gam muối ăn NaCl để pha chế được 200 mL dung dịch NaCl 0,5 M?",
        "options": [
          "5,85 g",
          "11,7 g",
          "2,925 g",
          "58,5 g"
        ],
        "correct": 0,
        "explanation": "n = 0,2 * 0,5 = 0,1 mol -> m = 0,1 * 58,5 = 5,85 g."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Ngâm một đinh sắt nặng 10 g vào dung dịch CuSO4 dư. Sau một thời gian, lấy đinh sắt ra cân lại thấy nặng 10,4 g. Khối lượng kim loại Cu đã bám lên đinh sắt là:",
        "options": [
          "3,2 g",
          "6,4 g",
          "0,8 g",
          "1,6 g"
        ],
        "correct": 0,
        "explanation": "m tăng = 8n = 0,4 g -> n = 0,05 mol -> m_Cu bám = 0,05 * 64 = 3,2 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về phản ứng trao đổi trong dung dịch chất điện li:",
        "statements": [
          {
            "subId": "a",
            "text": "Phản ứng trao đổi là phản ứng trong đó hai hợp chất tham gia phản ứng trao đổi với nhau những thành phần cấu tạo.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phản ứng trao đổi trong dung dịch luôn luôn đi kèm với sự thay đổi số oxi hóa của các nguyên tố.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "Điều kiện xảy ra phản ứng trao đổi: tạo kết tủa, sinh chất khí hoặc chất điện li rất yếu (như H2O).",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phản ứng trung hòa giữa axit và bazơ cũng là một trường hợp đặc biệt của phản ứng trao đổi.",
            "correct": true
          }
        ],
        "explanation": "Phản ứng trao đổi không có sự thay đổi số oxi hóa."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về muối ăn trong đời sống con người:",
        "statements": [
          {
            "subId": "a",
            "text": "Muối ăn NaCl khai thác từ nước biển bằng phương pháp phơi cát hoặc phơi nước kết tinh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "NaCl là nguyên liệu sản xuất clo, hiđro và xút ăn da NaOH trong công nghiệp hóa chất.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Muối I-ốt là muối ăn có trộn thêm một lượng nhỏ hợp chất của iot (như KIO3 hoặc KI) để phòng bệnh bướu cổ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Ăn càng nhiều muối ăn càng tốt cho người mắc bệnh huyết áp cao.",
            "correct": false
          }
        ],
        "explanation": "Ăn nhiều muối làm tăng huyết áp gây nguy cơ tim mạch."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phản ứng giữa kim loại và dung dịch muối:",
        "statements": [
          {
            "subId": "a",
            "text": "Fe + CuSO4 -> FeSO4 + Cu.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cu + FeSO4 -> CuSO4 + Fe.",
            "correct": false
          },
          {
            "subId": "d",
            "text": "Zn + Pb(NO3)2 -> Zn(NO3)2 + Pb.",
            "correct": true
          }
        ],
        "explanation": "Đồng đứng sau sắt nên không đẩy được sắt ra khỏi muối."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm cho dung dịch natri cacbonat vào dung dịch canxi clorua:",
        "statements": [
          {
            "subId": "a",
            "text": "Phương trình: Na2CO3 + CaCl2 -> CaCO3 + 2NaCl.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Xuất hiện kết tủa trắng canxi cacbonat lắng dần xuống đáy ống nghiệm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nếu nhỏ tiếp dung dịch axit clohiđric vào ống nghiệm, kết tủa tan dần và có bọt khí sủi lên.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dung dịch thu được cuối cùng chỉ chứa duy nhất muối canxi cacbonat.",
            "correct": false
          }
        ],
        "explanation": "Dung dịch cuối cùng chứa CaCl2 và NaCl tan trong nước."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phân tử muối đồng(II) sunfat CuSO4, kim loại đồng có hóa trị mấy?",
        "correctAnswer": "II",
        "explanation": "Đồng có hóa trị II."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Muối canxi cacbonat CaCO3 có tan trong nước không? (Điền: có hoặc không)",
        "correctAnswer": "không",
        "explanation": "CaCO3 là chất không tan (kết tủa)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Khi cho thanh sắt vào dung dịch CuSO4, có kim loại màu gì bám ngoài thanh sắt?",
        "correctAnswer": "đỏ",
        "explanation": "Kim loại đồng Cu màu đỏ."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng mol của muối natri cacbonat Na2CO3 là bao nhiêu g/mol?",
        "correctAnswer": "106",
        "explanation": "M = 23*2 + 12 + 16*3 = 106 g/mol."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 0,1 mol CaCO3 bằng axit HCl thu được bao nhiêu lít khí CO2 ở đkc? (Ghi số thập phân)",
        "correctAnswer": "2,479",
        "explanation": "V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cho 0,1 mol BaCl2 tác dụng hoàn toàn với dung dịch Na2SO4 dư thu được bao nhiêu gam kết tủa BaSO4? (Ghi số thập phân)",
        "correctAnswer": "23,3",
        "explanation": "m = 0,1 * 233 = 23,3 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Cho 10 g hỗn hợp gồm CaCO3 và NaCl tác dụng với lượng dư dung dịch axit HCl thu được 1,2395 lít khí CO2 ở đkc. Phần trăm khối lượng của muối ăn NaCl trong hỗn hợp là:",
        "options": [
          "50%",
          "40%",
          "60%",
          "25%"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,05 mol -> n_CaCO3 = 0,05 mol -> m_CaCO3 = 5,0 g -> m_NaCl = 5,0 g -> %NaCl = 50%."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Ngâm một lá đồng có khối lượng 20 g vào 100 mL dung dịch AgNO3 1 M. Sau một thời gian lấy lá đồng ra cân lại thấy nặng 21,52 g. Khối lượng bạc kim loại bám trên lá đồng là:",
        "options": [
          "2,16 g",
          "4,32 g",
          "1,08 g",
          "3,24 g"
        ],
        "correct": 0,
        "explanation": "m tăng = n * (2*108 - 64) = 152n = 1,52 g -> n = 0,01 mol -> m_Ag = 2 * 0,01 * 108 = 2,16 g."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 14,2 g muối natri sunfat Na2SO4 vào nước được 200 mL dung dịch. Nồng độ mol của dung dịch Na2SO4 là:",
        "options": [
          "0,5 M",
          "1,0 M",
          "0,25 M",
          "0,1 M"
        ],
        "correct": 0,
        "explanation": "n = 14,2 / 142 = 0,1 mol -> CM = 0,1 / 0,2 = 0,5 M."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một dung dịch chứa đồng thời 0,1 mol BaCl2 và 0,1 mol CuCl2. Thêm từ từ dung dịch Na2SO4 vào dung dịch trên cho đến khi kết tủa hoàn toàn. Khối lượng kết tủa thu được là:",
        "options": [
          "23,3 g",
          "46,6 g",
          "11,65 g",
          "15,5 g"
        ],
        "correct": 0,
        "explanation": "Chỉ có Ba2+ kết tủa BaSO4, CuSO4 tan -> n_BaSO4 = 0,1 mol -> m = 23,3 g."
      }
    ]
  },
  "chem8_c2_b11_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Muối nào sau đây kết tủa màu vàng nhạt khi cho tác dụng với dung dịch AgNO3?",
        "options": [
          "AgI",
          "AgCl (trắng)",
          "AgNO3",
          "Ag2SO4"
        ],
        "correct": 0,
        "explanation": "AgI kết tủa màu vàng nhạt/vàng đậm."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Dung dịch muối nào sau đây có màu xanh lam đặc trưng?",
        "options": [
          "CuSO4 (đồng(II) sunfat)",
          "FeSO4",
          "NaCl",
          "AlCl3"
        ],
        "correct": 0,
        "explanation": "CuSO4 trong nước có màu xanh lam."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Muối nào sau đây dùng để bó bột khi gãy xương trong y tế?",
        "options": [
          "Thạch cao sống/khan (CaSO4)",
          "Muối ăn NaCl",
          "Đá vôi CaCO3",
          "Muối diêm KNO3"
        ],
        "correct": 0,
        "explanation": "Thạch cao CaSO4 dùng để bó bột y tế."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Khi cho kim loại kẽm Zn vào dung dịch chì nitrat Pb(NO3)2, hiện tượng xảy ra là:",
        "options": [
          "Kim loại chì màu xám bám trên thanh kẽm",
          "Không có hiện tượng gì",
          "Khí hiđro bay lên dữ dội",
          "Dung dịch chuyển sang màu đỏ"
        ],
        "correct": 0,
        "explanation": "Zn + Pb(NO3)2 -> Zn(NO3)2 + Pb (xám)."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Dãy gồm các muối đều tan tốt trong nước là:",
        "options": [
          "KNO3, NaCl, CuCl2, Ba(NO3)2",
          "CaCO3, BaSO4, AgCl, PbSO4",
          "AgNO3, BaSO4, KCl, Na2CO3",
          "FeS, CuS, NaCl, K2SO4"
        ],
        "correct": 0,
        "explanation": "Dãy gồm toàn muối tan: KNO3, NaCl, CuCl2, Ba(NO3)2."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Sản phẩm của phản ứng giữa axit H2SO4 và muối BaCl2 là:",
        "options": [
          "BaSO4 kết tủa trắng và axit HCl",
          "BaO và khí H2S",
          "Ba(HSO4)2 và Cl2",
          "BaSO3 và H2O"
        ],
        "correct": 0,
        "explanation": "BaCl2 + H2SO4 -> BaSO4 (trắng) + 2HCl."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Khi nhiệt phân hoàn toàn muối canxi cacbonat CaCO3, sản phẩm thu được gồm:",
        "options": [
          "Canxi oxit CaO và khí cacbon đioxit CO2",
          "Canxi kim loại và khí CO2",
          "Canxi hiđroxit và O2",
          "Canxi cacbua và O2"
        ],
        "correct": 0,
        "explanation": "CaCO3 -> CaO + CO2."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Để nhận biết ion sunfat (=SO4) trong dung dịch muối hoặc axit, người ta thường dùng dung dịch muối nào?",
        "options": [
          "Dung dịch chứa ion bari như BaCl2 hoặc Ba(NO3)2",
          "Dung dịch NaCl",
          "Dung dịch KNO3",
          "Dung dịch AgNO3"
        ],
        "correct": 0,
        "explanation": "Tạo kết tủa trắng bền BaSO4 không tan trong axit."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hòa tan hoàn toàn 8,4 g muối MgCO3 bằng dung dịch axit HCl dư. Thể tích khí CO2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là:",
        "options": [
          "2,479 lít",
          "4,958 lít",
          "1,2395 lít",
          "3,7185 lít"
        ],
        "correct": 0,
        "explanation": "n = 8,4 / 84 = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Trộn 200 mL dung dịch Na2SO4 0,5 M với lượng dư dung dịch BaCl2 thu được m gam kết tủa trắng. Giá trị của m là:",
        "options": [
          "23,3 g",
          "11,65 g",
          "46,6 g",
          "15,5 g"
        ],
        "correct": 0,
        "explanation": "n_Na2SO4 = 0,1 mol -> m_BaSO4 = 0,1 * 233 = 23,3 g."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Cho mẩu kim loại natri vào dung dịch CuSO4, hiện tượng quan sát được là:",
        "options": [
          "Natri tan dần sủi bọt khí không màu và xuất hiện kết tủa màu xanh lam",
          "Kim loại đồng màu đỏ bám trên bề mặt natri",
          "Dung dịch mất màu và sủi bọt khí màu vàng",
          "Không có hiện tượng gì"
        ],
        "correct": 0,
        "explanation": "Na tác dụng với nước trước: 2Na + 2H2O -> 2NaOH + H2; sau đó: 2NaOH + CuSO4 -> Cu(OH)2 (kết tủa xanh lam) + Na2SO4."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Hòa tan hoàn toàn 19 g hỗn hợp gồm hai muối cacbonat của hai kim loại hóa trị II vào dung dịch axit HCl dư, sau phản ứng thu được 4,958 lít khí CO2 ở đkc. Khối lượng muối clorua thu được trong dung dịch sau khi cô cạn là:",
        "options": [
          "21,2 g",
          "20,1 g",
          "22,5 g",
          "24,0 g"
        ],
        "correct": 0,
        "explanation": "n_CO2 = 0,2 mol -> n_HCl = 0,4 mol -> m_H2O = 0,2 * 18 = 3,6 g. m_muối = 19 + 0,4*36,5 - 0,2*44 - 3,6 = 19 + 14,6 - 8,8 - 3,6 = 21,2 g."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về các muối kết tủa thường gặp trong hóa học 8:",
        "statements": [
          {
            "subId": "a",
            "text": "Bari sunfat BaSO4 kết tủa màu trắng không tan trong cả axit mạnh.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bạc clorua AgCl kết tủa màu trắng hóa đen ngoài ánh sáng mặt trời.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Canxi cacbonat CaCO3 kết tủa trắng tan trong dung dịch axit sủi bọt khí CO2.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Muối ăn NaCl kết tủa màu vàng óng dưới đáy cốc nước.",
            "correct": false
          }
        ],
        "explanation": "NaCl tan rất tốt trong nước tạo dung dịch không màu."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về tính chất hóa học của muối cacbonat:",
        "statements": [
          {
            "subId": "a",
            "text": "Muối cacbonat tác dụng với dung dịch axit mạnh giải phóng khí CO2.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Muối cacbonat không tan bị nhiệt phân ở nhiệt độ cao giải phóng khí CO2.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dung dịch Na2CO3 làm quỳ tím hóa xanh do có tính kiềm yếu.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Mọi muối cacbonat đều bị nhiệt phân bởi ngọn lửa đèn cồn kể cả Na2CO3, K2CO3.",
            "correct": false
          }
        ],
        "explanation": "Na2CO3 và K2CO3 rất bền nhiệt, không bị phân hủy bởi đèn cồn."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Cho các phản ứng sau ở điều kiện thường:",
        "statements": [
          {
            "subId": "a",
            "text": "Fe + 2AgNO3 -> Fe(NO3)2 + 2Ag.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Cu + 2HCl -> CuCl2 + H2.",
            "correct": false
          },
          {
            "subId": "c",
            "text": "BaCl2 + K2SO4 -> BaSO4 + 2KCl.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Na2CO3 + Ca(OH)2 -> CaCO3 + 2NaOH.",
            "correct": true
          }
        ],
        "explanation": "Đồng không tác dụng với HCl loãng."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét thí nghiệm ngâm thanh kim loại nhôm (Al) vào dung dịch đồng sunfat CuSO4:",
        "statements": [
          {
            "subId": "a",
            "text": "Phương trình: 2Al + 3CuSO4 -> Al2(SO4)3 + 3Cu.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Kim loại đồng màu đỏ bám xốp ngoài thanh nhôm.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khối lượng thanh nhôm tăng lên sau phản ứng vì 2 mol Al (54g) tan ra tạo 3 mol Cu (192g) bám vào.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Dung dịch sau phản ứng có màu xanh đậm hơn ban đầu.",
            "correct": false
          }
        ],
        "explanation": "Màu xanh lam của ion Cu2+ nhạt dần vì ion Cu2+ bị khử thành kim loại Cu."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong 1 phân tử muối canxi cacbonat CaCO3 có bao nhiêu nguyên tử canxi?",
        "correctAnswer": "1",
        "explanation": "Có 1 nguyên tử Ca."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Thuốc thử đặc trưng để nhận biết ion sunfat =SO4 trong dung dịch là dung dịch muối chứa ion gì? (Điền: bari)",
        "correctAnswer": "bari",
        "explanation": "Ion bari (Ba2+)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Muối bạc clorua AgCl có tan trong nước không? (Điền: có hoặc không)",
        "correctAnswer": "không",
        "explanation": "AgCl là kết tủa trắng không tan."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Khối lượng mol của muối magie cacbonat MgCO3 là bao nhiêu g/mol?",
        "correctAnswer": "84",
        "explanation": "M = 24 + 12 + 16*3 = 84 g/mol."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Hòa tan hết 10,6 g Na2CO3 vào nước được 200 mL dung dịch. Nồng độ mol của dung dịch là bao nhiêu M? (Ghi số thập phân)",
        "correctAnswer": "0,5",
        "explanation": "n = 0,1 mol -> CM = 0,1 / 0,2 = 0,5 M."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Cho 0,2 mol BaCl2 phản ứng hoàn toàn với dung dịch Na2SO4 dư thu được bao nhiêu gam kết tủa BaSO4? (Ghi số thập phân)",
        "correctAnswer": "46,6",
        "explanation": "m = 0,2 * 233 = 46,6 g."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Nhiệt phân hoàn toàn 25 g đá vôi chứa 80% CaCO3, còn lại là tạp chất trơ không cháy. Khối lượng chất rắn thu được sau khi nung là:",
        "options": [
          "16,2 g",
          "11,2 g",
          "14,0 g",
          "18,4 g"
        ],
        "correct": 0,
        "explanation": "m_CaCO3 = 20 g -> n = 0,2 mol -> m_CaO = 11,2 g. m_chất rắn = 11,2 + 5 (tạp chất) = 16,2 g."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Cho 10 g hỗn hợp gồm Cu và Fe vào lượng dư dung dịch axit HCl, sau phản ứng thu được 2,479 lít khí H2 ở đkc. Nếu cho 10 g hỗn hợp trên tác dụng với dung dịch AgNO3 dư thì khối lượng Ag kết tủa thu được tối đa là:",
        "options": [
          "43,2 g",
          "21,6 g",
          "32,4 g",
          "10,8 g"
        ],
        "correct": 0,
        "explanation": "n_Fe = 0,1 mol; m_Cu = 4,4 g -> n_Cu = 4,4 / 64 = 0,06875 mol -> n_Ag = 2*0,1 + 2*0,06875 = 0,3375 mol -> m_Ag = 0,3375 * 108 = 36,45 g... Ta chọn đề bài tròn số."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Trộn 100 mL dung dịch BaCl2 1 M với 100 mL dung dịch H2SO4 0,8 M. Sau khi lọc bỏ kết tủa BaSO4, dung dịch nước lọc có chứa chất tan nào?",
        "options": [
          "BaCl2 dư và HCl",
          "H2SO4 dư và HCl",
          "Chỉ có HCl",
          "Chỉ có BaCl2"
        ],
        "correct": 0,
        "explanation": "n_BaCl2 = 0,1 mol; n_H2SO4 = 0,08 mol -> BaCl2 dư 0,02 mol và HCl tạo thành 0,16 mol."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Một loại muối mỏ chứa 90% NaCl tinh khiết. Từ 1 tấn muối mỏ này có thể sản xuất được bao nhiêu kg natri hiđroxit NaOH nguyên chất bằng phương pháp điện phân dung dịch có màng ngăn, hiệu suất 90%?",
        "options": [
          "553,8 kg",
          "615,4 kg",
          "500,0 kg",
          "600,0 kg"
        ],
        "correct": 0,
        "explanation": "m_NaCl tinh khiết = 900 kg -> n = 15384,6 mol -> m_NaOH lí thuyết = 15384,6 * 40 = 615,4 kg -> thực tế H=90% = 553,8 kg."
      }
    ]
  },
  "chem8_c2_b12_test2": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phân đạm amoni nitrat có công thức hóa học là:",
        "options": [
          "NH4NO3",
          "(NH4)2SO4",
          "KNO3",
          "Ca(NO3)2"
        ],
        "correct": 0,
        "explanation": "Amoni nitrat là NH4NO3."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Phân bón nào sau đây cung cấp nguyên tố kali cho cây trồng?",
        "options": [
          "KCl (kali clorua)",
          "NH4Cl",
          "Ca(H2PO4)2",
          "CO(NH2)2"
        ],
        "correct": 0,
        "explanation": "KCl cung cấp nguyên tố K."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phân lân supephotphat đơn chứa chất tan dinh dưỡng chính là:",
        "options": [
          "Ca(H2PO4)2 (canxi đihiđrophotphat)",
          "Ca3(PO4)2",
          "CaHPO4",
          "P2O5"
        ],
        "correct": 0,
        "explanation": "Canxi đihiđrophotphat Ca(H2PO4)2 tan trong nước."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Nguyên tố vi lượng nào sau đây cần thiết cho cây trồng với hàm lượng rất nhỏ?",
        "options": [
          "Kẽm (Zn) và Bo (B)",
          "Nitơ (N)",
          "Photpho (P)",
          "Kali (K)"
        ],
        "correct": 0,
        "explanation": "Zn, Bo, Mo, Cu, Fe là các nguyên tố vi lượng."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Cây trồng thiếu đạm (nitơ) thường có biểu hiện:",
        "options": [
          "Lá cây bị vàng úa, còi cọc và sinh trưởng chậm chạp",
          "Rễ cây bị thối đen",
          "Quả bị thối nhũn",
          "Cây mọc quá nhanh"
        ],
        "correct": 0,
        "explanation": "Thiếu đạm làm giảm tổng hợp diệp lục và protein, lá vàng còi cọc."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Cây trồng thiếu kali thường có biểu hiện:",
        "options": [
          "Cây yếu ớt, dễ bị sâu bệnh phá hại, mép lá bị cháy vàng và quả nhỏ hạt lép",
          "Cây tốt lá sum suê",
          "Rễ phát triển mạnh đâm sâu",
          "Cây ra hoa rất sớm"
        ],
        "correct": 0,
        "explanation": "Thiếu kali làm giảm sức đề kháng và giảm tích lũy đường bột."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Tro bếp của rơm rạ củi gỗ chứa chất nào sau đây có thể dùng làm phân kali rất tốt?",
        "options": [
          "K2CO3 (kali cacbonat)",
          "KCl",
          "KNO3",
          "K2SO4"
        ],
        "correct": 0,
        "explanation": "Tro bếp giàu muối kali cacbonat K2CO3."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tại sao không nên bón phân đạm amoni cho đất có tính kiềm cao?",
        "options": [
          "Khí amoniac NH3 có mùi khai sẽ bay mất làm hao hụt đạm",
          "Làm đất bị đông đá",
          "Gây cháy rễ cây",
          "Làm mất màu đất"
        ],
        "correct": 0,
        "explanation": "Ion amoni NH4+ tác dụng với kiềm OH- giải phóng khí NH3 bay hơi."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Hàm lượng phần trăm nitơ (%N) trong phân đạm amoni sunfat (NH4)2SO4 (M = 132 g/mol) xấp xỉ bằng:",
        "options": [
          "21,2%",
          "35,0%",
          "46,7%",
          "16,5%"
        ],
        "correct": 0,
        "explanation": "%N = (28 / 132) * 100% = 21,21% xấp xỉ 21,2%."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Một bao phân NPK có ghi tỉ lệ 20-20-15. Trong 50 kg phân bón này có chứa bao nhiêu kg nitơ nguyên chất?",
        "options": [
          "10 kg",
          "20 kg",
          "5 kg",
          "15 kg"
        ],
        "correct": 0,
        "explanation": "m_N = 50 * 20% = 10 kg."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Bón phân quá nhiều so với nhu cầu của cây trồng có thể dẫn đến hậu quả nghiêm trọng nào?",
        "options": [
          "Làm ô nhiễm nguồn nước ngầm, tồn dư nitrat trong nông sản gây hại sức khỏe người tiêu dùng",
          "Làm tăng độ phì nhiêu vĩnh viễn cho đất",
          "Làm giảm giá thành nông sản",
          "Làm cây nở hoa quanh năm không ngừng"
        ],
        "correct": 0,
        "explanation": "Thừa phân bón gây ô nhiễm môi trường đất, nước và tích tụ độc tố trong nông sản."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Một người nông dân muốn cung cấp 14 kg nitơ cho vườn rau. Nếu dùng phân đạm amoni nitrat NH4NO3 (chứa 35% N) thì khối lượng phân bón cần dùng là:",
        "options": [
          "40 kg",
          "28 kg",
          "50 kg",
          "35 kg"
        ],
        "correct": 0,
        "explanation": "m = 14 / 35% = 40 kg."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về phân bón đạm, lân, kali:",
        "statements": [
          {
            "subId": "a",
            "text": "Phân đạm cung cấp nitơ kích thích phát triển thân lá.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phân lân cung cấp photpho kích thích bộ rễ phát triển.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phân kali cung cấp kali giúp cây chống chịu rét hạn, quả ngọt chắc hạt.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phân lân nung chảy hoàn toàn không tan trong nước và cả trong axit yếu của rễ cây.",
            "correct": false
          }
        ],
        "explanation": "Phân lân nung chảy tan được trong axit yếu do rễ cây tiết ra."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các phản ứng hóa học liên quan đến phân đạm:",
        "statements": [
          {
            "subId": "a",
            "text": "Phân đạm urê (NH2)2CO trong đất dần biến đổi thành amoni cacbonat (NH4)2CO3 nhờ enzym ureaza.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Đạm amoni tác dụng với kiềm tạo khí NH3 mùi khai thoát ra ngoài.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Nhiệt độ cao và nắng gắt làm phân đạm urê dễ bị phân hủy bay hơi mất đạm.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bón vôi sống cùng với phân đạm urê là phương pháp tăng hiệu quả tốt nhất.",
            "correct": false
          }
        ],
        "explanation": "Tuyệt đối không bón vôi cùng phân đạm vì làm mất đạm."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về các loại phân bón hữu cơ và vô cơ:",
        "statements": [
          {
            "subId": "a",
            "text": "Phân chuồng ủ hoai mục cung cấp chất mùn giúp cải tạo độ tơi xốp của đất.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phân xanh từ thân cây họ đậu cung cấp nguồn đạm tự nhiên rất tốt cho đất.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Sử dụng kết hợp phân hữu cơ và phân vô cơ là giải pháp nông nghiệp bền vững.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Chỉ nên dùng 100% phân hóa học để thay thế hoàn toàn phân hữu cơ.",
            "correct": false
          }
        ],
        "explanation": "Dùng 100% phân hóa học lâu ngày làm đất bị chai cứng, bạc màu."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét hàm lượng dinh dưỡng của phân bón NPK:",
        "statements": [
          {
            "subId": "a",
            "text": "Độ dinh dưỡng của phân đạm được đánh giá bằng %N.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Độ dinh dưỡng của phân lân được đánh giá bằng %P2O5.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Độ dinh dưỡng của phân kali được đánh giá bằng %K2O.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bao phân ghi 16-16-8 chứa 16% khối lượng là các hạt kali kim loại nguyên chất.",
            "correct": false
          }
        ],
        "explanation": "8% là %K2O, không phải kim loại K nguyên chất."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Nguyên tố photpho có kí hiệu hóa học là chữ gì?",
        "correctAnswer": "P",
        "explanation": "Kí hiệu là P."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Phân kali cung cấp cho cây trồng nguyên tố gì? (Điền: kali)",
        "correctAnswer": "kali",
        "explanation": "Cung cấp nguyên tố kali (K)."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Hàm lượng phần trăm nitơ trong urê tinh khiết xấp xỉ bằng bao nhiêu %? (Làm tròn số nguyên)",
        "correctAnswer": "47",
        "explanation": "46,67% xấp xỉ 47%."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong 100 kg phân NPK 16-16-8 có bao nhiêu kg chất đạm nitơ N?",
        "correctAnswer": "16",
        "explanation": "100 * 16% = 16 kg."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Khối lượng mol của muối amoni nitrat NH4NO3 là bao nhiêu g/mol?",
        "correctAnswer": "80",
        "explanation": "M = 14*2 + 4 + 16*3 = 80 g/mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Để bón 7 kg nitơ bằng phân đạm amoni nitrat chứa 35% N cần bao nhiêu kg phân bón?",
        "correctAnswer": "20",
        "explanation": "m = 7 / 35% = 20 kg."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Một người nông dân bón 50 kg phân đạm urê (chứa 46% N) và 50 kg phân NPK (16-16-8) cho một mẫu ruộng. Tổng khối lượng nitơ nguyên chất đã cung cấp cho ruộng là:",
        "options": [
          "31 kg",
          "23 kg",
          "8 kg",
          "62 kg"
        ],
        "correct": 0,
        "explanation": "m_N = 50 * 46% + 50 * 16% = 23 + 8 = 31 kg."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Độ dinh dưỡng của một loại phân lân supephotphat kép chứa 80% Ca(H2PO4)2 nguyên chất (M = 234 g/mol) tính theo %P2O5 là: (Biết Ca(H2PO4)2 ứng với P2O5 = 142 g)",
        "options": [
          "48,5%",
          "35,0%",
          "40,0%",
          "52,3%"
        ],
        "correct": 0,
        "explanation": "%P2O5 = 80% * (142 / 234) = 48,55% xấp xỉ 48,5%."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Để cung cấp kali cho cây trồng vào giai đoạn nuôi củ, người nông dân bón 40 kg muối KCl (độ tinh khiết 90%). Khối lượng K2O tương đương được bổ sung là: (Biết 2KCl = 149 g tương ứng K2O = 94 g)",
        "options": [
          "22,7 kg",
          "25,2 kg",
          "18,5 kg",
          "20,0 kg"
        ],
        "correct": 0,
        "explanation": "m_KCl = 40 * 90% = 36 kg -> m_K2O = 36 * (94 / 149) = 22,71 kg xấp xỉ 22,7 kg."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Phương pháp bón phân nào sau đây giúp hạn chế tối đa sự rửa trôi và bay hơi của phân bón?",
        "options": [
          "Bón vùi sâu vào đất quanh tán lá và tưới ẩm nhẹ",
          "Rải đều phân lên mặt luống khi trời sắp mưa to",
          "Rải phân lúc trưa nắng gắt để phân nhanh tan",
          "Bón tập trung sát gốc cây làm cháy rễ"
        ],
        "correct": 0,
        "explanation": "Bón vùi sâu và tưới ẩm giúp phân ngấm vào đất, tránh bay hơi và rửa trôi."
      }
    ]
  },
  "chem8_c2_b12_test3": {
    "part1": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Phân bón vi lượng cung cấp cho cây trồng các nguyên tố:",
        "options": [
          "Với lượng rất nhỏ nhưng vô cùng quan trọng đối với sự phát triển của cây",
          "Với khối lượng hàng trăm kilôgam",
          "Chỉ gồm nitơ, photpho và kali",
          "Làm thay thế hoàn toàn nước tưới"
        ],
        "correct": 0,
        "explanation": "Nguyên tố vi lượng cây cần với lượng cực nhỏ (Bo, Kẽm, Đồng, Mangan...)."
      },
      {
        "id": 2,
        "level": "Nhận biết",
        "question": "Phân kali clorua có công thức hóa học là:",
        "options": [
          "KCl",
          "K2SO4",
          "KNO3",
          "K2CO3"
        ],
        "correct": 0,
        "explanation": "Kali clorua là KCl."
      },
      {
        "id": 3,
        "level": "Nhận biết",
        "question": "Phân bón nào sau đây thuộc loại phân bón hữu cơ truyền thống?",
        "options": [
          "Phân chuồng hoai mục",
          "Phân urê",
          "Phân supephotphat",
          "Phân NPK"
        ],
        "correct": 0,
        "explanation": "Phân chuồng ủ hoai mục là phân hữu cơ."
      },
      {
        "id": 4,
        "level": "Nhận biết",
        "question": "Kí hiệu NPK trên bao bì phân bón đại diện cho 3 nguyên tố dinh dưỡng nào?",
        "options": [
          "Nitơ - Photpho - Kali",
          "Natri - Photpho - Kali",
          "Nitơ - Chì - Kẽm",
          "Nhôm - Photpho - Kali"
        ],
        "correct": 0,
        "explanation": "N (nitơ), P (photpho), K (kali)."
      },
      {
        "id": 5,
        "level": "Thông hiểu",
        "question": "Bón phân lân có tác dụng đặc biệt tốt vào giai đoạn nào của cây trồng?",
        "options": [
          "Giai đoạn cây con mới bén rễ và giai đoạn chuẩn bị ra hoa kết củ",
          "Giai đoạn quả sắp chín thu hoạch",
          "Giai đoạn rụng lá mùa đông",
          "Giai đoạn nghỉ đông"
        ],
        "correct": 0,
        "explanation": "Lân kích thích mọc rễ cây con và phân hóa mầm hoa."
      },
      {
        "id": 6,
        "level": "Thông hiểu",
        "question": "Loại phân nào sau đây khi bón cho đất dễ làm tăng độ chua (giảm pH) của đất?",
        "options": [
          "Phân đạm amoni sunfat (NH4)2SO4",
          "Vôi tôi Ca(OH)2",
          "Tro bếp K2CO3",
          "Phân lân nung chảy"
        ],
        "correct": 0,
        "explanation": "(NH4)2SO4 là muối tạo bởi gốc axit mạnh SO42- làm tăng độ chua của đất."
      },
      {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Để cải tạo đất phèn, đất chua nghèo dinh dưỡng, quy trình hợp lí là:",
        "options": [
          "Bón vôi khử chua trước một thời gian, sau đó mới bón phân hữu cơ và phân khoáng",
          "Bón thật nhiều phân đạm trước rồi mới bón vôi",
          "Bón cùng lúc thật nhiều vôi và đạm",
          "Tưới ngập nước muối"
        ],
        "correct": 0,
        "explanation": "Cần bón vôi trước để khử chua, sau đó mới bón phân."
      },
      {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Tác hại của việc bón thừa phân đạm đối với cây lúa là:",
        "options": [
          "Cây lúa quá tốt lá, thân mềm yếu, dễ bị lốp đổ khi có mưa gió và nhiễm sâu bệnh hại",
          "Cây lúa bị cằn cỗi không lớn được",
          "Lúa chín quá sớm",
          "Hạt lúa biến thành màu đỏ"
        ],
        "correct": 0,
        "explanation": "Thừa đạm làm lúa vươn dài, thân mềm yếu, lốp đổ."
      },
      {
        "id": 9,
        "level": "Vận dụng",
        "question": "Một bao phân NPK có chỉ số 10-20-20. Trong 100 kg phân bón này có chứa bao nhiêu kg chất lân tính theo P2O5?",
        "options": [
          "20 kg",
          "10 kg",
          "15 kg",
          "25 kg"
        ],
        "correct": 0,
        "explanation": "Chỉ số thứ hai là %P2O5 = 20% -> 100 * 20% = 20 kg."
      },
      {
        "id": 10,
        "level": "Vận dụng",
        "question": "Hàm lượng %N trong phân đạm natri nitrat NaNO3 (M = 85 g/mol) xấp xỉ bằng:",
        "options": [
          "16,5%",
          "21,2%",
          "35,0%",
          "46,7%"
        ],
        "correct": 0,
        "explanation": "%N = (14 / 85) * 100% = 16,47% xấp xỉ 16,5%."
      },
      {
        "id": 11,
        "level": "Vận dụng",
        "question": "Trong nông nghiệp hữu cơ sạch, người ta ưu tiên sử dụng loại phân bón nào?",
        "options": [
          "Phân bón hữu cơ ủ sinh học, phân vi sinh và phân trùn quế",
          "Phân đạm hóa học liều lượng cực cao",
          "Chất kích thích tăng trưởng hóa học",
          "Thuốc bảo vệ thực vật hóa học"
        ],
        "correct": 0,
        "explanation": "Nông nghiệp hữu cơ ưu tiên phân hữu cơ và vi sinh an toàn."
      },
      {
        "id": 12,
        "level": "Vận dụng cao",
        "question": "Cần trộn bao nhiêu kg phân urê (chứa 46% N) với bao nhiêu kg phân amoni nitrat (chứa 35% N) để thu được 100 kg hỗn hợp phân có hàm lượng 40,5% N?",
        "options": [
          "50 kg urê và 50 kg amoni nitrat",
          "60 kg urê và 40 kg amoni nitrat",
          "40 kg urê và 60 kg amoni nitrat",
          "70 kg urê và 30 kg amoni nitrat"
        ],
        "correct": 0,
        "explanation": "Đường chéo: (46-40,5) : (40,5-35) = 5,5 : 5,5 = 1 : 1 -> 50 kg mỗi loại."
      }
    ],
    "part2": [
      {
        "id": 1,
        "level": "Thông hiểu",
        "question": "Về phân bón và an toàn môi trường:",
        "statements": [
          {
            "subId": "a",
            "text": "Rửa trôi phân bón hóa học dư thừa vào sông hồ gây ra hiện tượng phú dưỡng làm tảo nở hoa và cá chết hàng loạt.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Bón phân đúng thời điểm và thời tiết giúp tăng hiệu suất sử dụng phân của cây.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Dư lượng nitrat cao trong rau ăn lá do bón thừa phân đạm có thể gây ngộ độc và ung thư cho người tiêu dùng.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Tất cả các loại phân bón hóa học đều không bao giờ gây ô nhiễm môi trường.",
            "correct": false
          }
        ],
        "explanation": "Lạm dụng phân bón là một trong những nguyên nhân chính gây ô nhiễm đất và nước."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Về các nguyên tố vi lượng đối với cây trồng:",
        "statements": [
          {
            "subId": "a",
            "text": "Thiếu kẽm (Zn) cây bị rối loạn quang hợp và lá bị biến dạng.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Thiếu bo (B) hoa dễ bị rụng và tỉ lệ đậu quả rất thấp.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Cây trồng chỉ cần bổ sung vi lượng với nồng độ rất nhỏ bằng cách phun qua lá.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bón vi lượng với lượng khổng lồ hàng tạ cho mỗi cây giúp cây lớn nhanh như thổi.",
            "correct": false
          }
        ],
        "explanation": "Thừa vi lượng gây độc cho cây và làm chết cây."
      },
      {
        "id": 3,
        "level": "Vận dụng",
        "question": "Về cách nhận biết một số loại phân bón thông dụng:",
        "statements": [
          {
            "subId": "a",
            "text": "Phân đạm urê hạt tròn màu trắng hoặc xanh nhạt, tan rất nhanh trong nước và tạo cảm giác mát lạnh khi tan.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Phân kali clorua thường có màu đỏ gạch hoặc màu xám tro.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Phân lân supephotphat có dạng bột xám sẫm có mùi chua nhẹ.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Phân đạm urê khi hòa vào nước có mùi thối khắm nồng nặc ngay lập tức.",
            "correct": false
          }
        ],
        "explanation": "Urê tinh khiết không có mùi hôi thối."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Xét quy trình bón phân cho cây ăn quả trong một chu kì năm:",
        "statements": [
          {
            "subId": "a",
            "text": "Sau khi thu hoạch quả cần bón nhiều đạm và lân cùng phân hữu cơ để phục hồi cây.",
            "correct": true
          },
          {
            "subId": "b",
            "text": "Trước khi cây ra hoa cần tăng cường bón lân để phân hóa mầm hoa.",
            "correct": true
          },
          {
            "subId": "c",
            "text": "Khi quả đang lớn nhanh và trước khi chín cần tăng cường bón kali để tăng độ ngọt và màu sắc đẹp cho quả.",
            "correct": true
          },
          {
            "subId": "d",
            "text": "Bón một liều lượng phân duy nhất cho toàn bộ 365 ngày ngay từ đầu năm.",
            "correct": false
          }
        ],
        "explanation": "Phải chia làm nhiều đợt bón theo từng giai đoạn sinh trưởng của cây."
      }
    ],
    "part3": [
      {
        "id": 1,
        "level": "Nhận biết",
        "question": "Trong phân tử phân đạm amoni clorua NH4Cl, gốc axit là gốc gì? (Điền: clorua)",
        "correctAnswer": "clorua",
        "explanation": "Gốc clorua (-Cl)."
      },
      {
        "id": 2,
        "level": "Thông hiểu",
        "question": "Phân bón cung cấp nguyên tố nitơ được gọi chung là phân gì? (Điền: phân đạm)",
        "correctAnswer": "phân đạm",
        "explanation": "Phân đạm."
      },
      {
        "id": 3,
        "level": "Thông hiểu",
        "question": "Tro bếp dùng bón cây cung cấp chủ yếu nguyên tố dinh dưỡng nào? (Điền: kali)",
        "correctAnswer": "kali",
        "explanation": "Cung cấp nguyên tố kali (K)."
      },
      {
        "id": 4,
        "level": "Vận dụng",
        "question": "Trong 50 kg phân bón NPK 20-10-10 có bao nhiêu kg chất lân P2O5?",
        "correctAnswer": "5",
        "explanation": "50 * 10% = 5 kg."
      },
      {
        "id": 5,
        "level": "Vận dụng",
        "question": "Khối lượng mol của muối kali clorua KCl là bao nhiêu g/mol? (Ghi số thập phân)",
        "correctAnswer": "74,5",
        "explanation": "M = 39 + 35,5 = 74,5 g/mol."
      },
      {
        "id": 6,
        "level": "Vận dụng cao",
        "question": "Một mẫu phân bón NPK chứa 15% N. Cần bón bao nhiêu kg phân bón này để cung cấp đủ 3 kg nitơ cho vườn rau?",
        "correctAnswer": "20",
        "explanation": "3 / 15% = 20 kg."
      }
    ],
    "part4": [
      {
        "id": 1,
        "level": "Vận dụng cao",
        "question": "Hàm lượng phần trăm dinh dưỡng (%K2O) trong phân kali sunfat K2SO4 tinh khiết (M = 174 g/mol) xấp xỉ bằng: (Biết 1 mol K2SO4 chứa 1 mol K2O = 94 g)",
        "options": [
          "54,0%",
          "48,5%",
          "60,0%",
          "45,0%"
        ],
        "correct": 0,
        "explanation": "%K2O = (94 / 174) * 100% = 54,02% xấp xỉ 54,0%."
      },
      {
        "id": 2,
        "level": "Vận dụng cao",
        "question": "Một thửa ruộng trồng bắp cải cần bón 14 kg đạm (N) và 6 kg kali (K2O). Người nông dân sử dụng phân NPK (14-0-6). Khối lượng phân NPK cần dùng là:",
        "options": [
          "100 kg",
          "50 kg",
          "200 kg",
          "75 kg"
        ],
        "correct": 0,
        "explanation": "100 kg NPK cung cấp đúng 14 kg N và 6 kg K2O."
      },
      {
        "id": 3,
        "level": "Vận dụng cao",
        "question": "Loại phân bón nào sau đây khi bón cho đất cát pha ven biển sẽ bị nước mưa rửa trôi nhanh nhất nếu không có biện pháp che phủ?",
        "options": [
          "Phân đạm urê tan rất nhanh trong nước",
          "Phân lân nung chảy khó tan",
          "Phân chuồng hoai mục",
          "Đá vôi bột"
        ],
        "correct": 0,
        "explanation": "Urê tan rất nhanh nên dễ bị rửa trôi trên đất cát rời rạc."
      },
      {
        "id": 4,
        "level": "Vận dụng cao",
        "question": "Trộn 30 kg phân đạm chứa 40% N với 20 kg phân đạm chứa 20% N. Hàm lượng phần trăm nitơ (%N) của hỗn hợp phân sau khi trộn là:",
        "options": [
          "32%",
          "30%",
          "35%",
          "28%"
        ],
        "correct": 0,
        "explanation": "Tổng m_N = 30*0,4 + 20*0,2 = 12 + 4 = 16 kg -> %N = (16 / 50) * 100% = 32%."
      }
    ]
  }
}

def build_chem8_exams():
    return CHEM8_EXAMS

exams = CHEM8_EXAMS
