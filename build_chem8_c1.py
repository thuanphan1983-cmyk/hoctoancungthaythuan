# -*- coding: utf-8 -*-
"""
BUILDER HÓA HỌC 8 - CHƯƠNG I: PHẢN ỨNG HÓA HỌC (23 ĐỀ ĐỘC LẬP 100%)
Gồm 6 bài học (3 đề/bài = 18 đề) và 1 bài ôn tập cuối chương (5 đề) = 23 đề.
Mỗi đề: 12 MC + 4 TF (16 ý) + 6 SA + 4 VDC.
Không trùng lặp câu hỏi, số liệu, chất và đáp án giữa các đề trong cùng bài.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, level, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation
    }

def make_tf(qid, level, prompt, statements, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": prompt.strip(),
        "statements": [
            {"subId": s[0], "text": s[1].strip(), "correct": s[2]} for s in statements
        ],
        "explanation": explanation
    }

def make_sa(qid, level, q_text, answer, explanation=""):
    return {
        "id": qid,
        "level": level,
        "question": q_text.strip(),
        "correctAnswer": str(answer).strip(),
        "explanation": explanation
    }

def make_vdc(qid, q_text, options, correct_idx, explanation=""):
    return {
        "id": qid,
        "level": "Vận dụng cao",
        "question": q_text.strip(),
        "options": options,
        "correct": correct_idx,
        "explanation": explanation
    }

exams_c1 = {}

# ==============================================================================
# BÀI 2: BIẾN ĐỔI VẬT LÍ VÀ BIẾN ĐỔI HÓA HỌC (3 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Biến đổi trạng thái và hiện tượng thực tế quen thuộc ---
exams_c1["chem8_c1_b2_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Hiện tượng nào sau đây là hiện tượng biến đổi vật lí?", ["Nước đá tan chảy thành nước lỏng", "Cơm để lâu ngày bị ôi thiu", "Đốt cháy một que diêm trong không khí", "Đinh sắt bị gỉ tạo thành lớp gỉ màu nâu đỏ"], 0, "Nước đá tan chỉ biến đổi trạng thái từ rắn sang lỏng, không tạo ra chất mới."),
        make_mc(2, "Nhận biết", "Hiện tượng nào sau đây có sự biến đổi hóa học?", ["Cồn để trong lọ hở miệng bị bay hơi", "Đèn cồn cháy tỏa nhiều nhiệt và ánh sáng", "Mặt trời làm nước biển bốc hơi tạo muối", "Hòa tan đường vào cốc nước ấm"], 1, "Cồn cháy tạo ra chất mới là khí carbon dioxide và hơi nước."),
        make_mc(3, "Nhận biết", "Dấu hiệu nào sau đây chứng tỏ có biến đổi hóa học xảy ra?", ["Chất thay đổi hình dạng kích thước", "Chất chuyển từ thể lỏng sang thể hơi", "Có sự tạo thành chất mới khác biệt", "Chất tan hoàn toàn tạo dung dịch"], 2, "Bản chất của biến đổi hóa học là có chất mới sinh ra."),
        make_mc(4, "Nhận biết", "Quá trình nào sau đây KHÔNG có sự biến đổi hóa học?", ["Quang hợp của cây xanh dưới ánh sáng", "Sự hô hấp của con người và động vật", "Nghiền nhỏ hạt gạo thành bột mịn", "Sự lên men giấm từ rượu nếp"], 2, "Nghiền gạo chỉ làm nhỏ kích thước hạt tinh bột, không sinh chất mới."),
        make_mc(5, "Thông hiểu", "Khi thắp một cây nến làm bằng parafin, giai đoạn nào thể hiện biến đổi vật lí?", ["Parafin nóng chảy và chuyển thành hơi", "Hơi parafin cháy tạo CO2 và H2O", "Nến tỏa nhiệt nóng ấm xung quanh", "Khí sinh ra làm đục nước vôi trong"], 0, "Parafin chảy lỏng và bay hơi là biến đổi trạng thái (vật lí)."),
        make_mc(6, "Thông hiểu", "Cho các hiện tượng: (1) Sắt hút nam châm; (2) Lưu huỳnh cháy trong oxi; (3) Thủy tinh nóng chảy thổi bóng; (4) Vôi sống tác dụng với nước. Số hiện tượng hóa học là:", ["1", "2", "3", "4"], 1, "Hiện tượng hóa học gồm (2) và (4)."),
        make_mc(7, "Thông hiểu", "Khi mở nắp lon nước ngọt có gas, thấy bọt khí sủi lên. Đây là hiện tượng gì?", ["Biến đổi hóa học do khí mới tạo ra", "Biến đổi vật lí do giảm áp suất khí CO2 thoát ra", "Phản ứng phân hủy đường ngọt", "Biến đổi vừa vật lí vừa hóa học"], 1, "CO2 tan trong nước ngọt thoát ra ngoài khi giảm áp suất, là quá trình vật lí."),
        make_mc(8, "Thông hiểu", "Thả một mẩu đá vôi (CaCO3) vào dung dịch axit clohiđric (HCl) thấy sủi bọt khí. Hiện tượng này là biến đổi hóa học vì:", ["Mẩu đá vôi chìm xuống đáy ống nghiệm", "Dung dịch bị đục dần", "Có chất khí mới sinh ra thoát ra ngoài", "Nhiệt độ ống nghiệm giữ nguyên"], 2, "Sinh ra khí mới (CO2) chứng tỏ có phản ứng hóa học."),
        make_mc(9, "Vận dụng", "Trong sản xuất vôi tôi, hai công đoạn chính là: (1) Nung đá vôi ở nhiệt độ cao thành vôi sống; (2) Thả vôi sống vào nước tạo vôi tôi. Nhận định đúng là:", ["(1) là vật lí, (2) là hóa học", "(1) là hóa học, (2) là vật lí", "Cả (1) và (2) đều là biến đổi hóa học", "Cả (1) và (2) đều là biến đổi vật lí"], 2, "Cả hai đều tạo chất mới: CaCO3 -> CaO + CO2 và CaO + H2O -> Ca(OH)2."),
        make_mc(10, "Vận dụng", "Hiện tượng nào sau đây minh họa cho biến đổi hóa học kèm theo sự thay đổi màu sắc rõ rệt?", ["Hòa tan bột đồng sunfat màu xanh vào nước", "Nhúng đinh sắt vào dung dịch đồng sunfat thấy xuất hiện lớp đồng màu đỏ bám ngoài", "Trộn bột lưu huỳnh vàng với bột sắt xám đen", "Đun nóng nước sôi sùng sục"], 1, "Sắt đẩy đồng ra khỏi muối tạo Cu màu đỏ bám trên đinh sắt."),
        make_mc(11, "Vận dụng", "Hiện tượng thức ăn bị ôi thiu trong mùa hè là do:", ["Nước trong thức ăn bị bay hơi nhanh chóng", "Vi sinh vật biến đổi các chất hữu cơ thành chất mới có mùi lạ và độc hại", "Muối ăn trong thức ăn bị kết tinh", "Nhiệt độ cao làm các chất tan chảy"], 1, "Vi sinh vật phân giải protein, lipit tạo thành các hợp chất mới."),
        make_mc(12, "Vận dụng cao", "Tiến hành 4 thí nghiệm: (a) Đun nóng cồn trong đĩa sứ; (b) Đốt cháy cồn trong đĩa sứ; (c) Cho giấm ăn vào baking soda; (d) Làm đông đặc mỡ lợn trong tủ lạnh. Số thí nghiệm xảy ra biến đổi hóa học là:", ["1", "2", "3", "4"], 1, "Gồm thí nghiệm (b) và (c)."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các hiện tượng diễn ra trong đời sống hàng ngày sau đây:", [
            ("a", "Hòa tan viên sủi vitamin C vào nước thấy sủi bọt khí mạnh là biến đổi hóa học.", True),
            ("b", "Băng phiến (long não) đặt trong tủ quần áo thu nhỏ dần là biến đổi hóa học.", False),
            ("c", "Thổi hơi thở vào nước vôi trong thấy bị vẩn đục là biến đổi hóa học.", True),
            ("d", "Bẻ cong một thanh nhôm chỉ làm biến dạng hình học là biến đổi vật lí.", True)
        ], "Băng phiến thu nhỏ là hiện tượng thăng hoa (vật lí)."),
        make_tf(2, "Thông hiểu", "Về các dấu hiệu nhận biết phản ứng và sự biến đổi chất:", [
            ("a", "Biến đổi vật lí chỉ thay đổi trạng thái, hình dạng hoặc kích thước của chất.", True),
            ("b", "Biến đổi hóa học luôn đi kèm sự sinh ra một hoặc nhiều chất mới.", True),
            ("c", "Mọi hiện tượng tỏa nhiệt đều chứng tỏ có phản ứng hóa học xảy ra.", False),
            ("d", "Sự xuất hiện chất kết tủa không tan trong dung dịch là một dấu hiệu của biến đổi hóa học.", True)
        ], "Đèn sợi đốt sáng và tỏa nhiệt là biến đổi vật lí."),
        make_tf(3, "Vận dụng", "Trong quá trình chưng cất rượu thủ công từ cơm rượu lên men:", [
            ("a", "Giai đoạn ủ men rượu từ tinh bột gạo là quá trình biến đổi hóa học.", True),
            ("b", "Giai đoạn đun sôi để cồn bay hơi rồi ngưng tụ là quá trình biến đổi hóa học.", False),
            ("c", "Rượu nguyên chất để lâu ngoài không khí bị chua là do biến đổi hóa học.", True),
            ("d", "Pha loãng rượu với nước tinh khiết là quá trình biến đổi hóa học.", False)
        ], "Chưng cất và pha loãng là quá trình vật lí."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm nung nóng bột sắt trộn với bột lưu huỳnh trong ống nghiệm:", [
            ("a", "Trước khi nung, có thể dùng nam châm tách sắt ra khỏi lưu huỳnh (biến đổi vật lí).", True),
            ("b", "Khi nung nóng, hỗn hợp tự phát sáng đỏ rực và tạo thành hợp chất sắt(II) sunfua màu xám đen.", True),
            ("c", "Chất rắn sau phản ứng vẫn bị nam châm hút mạnh như bột sắt ban đầu.", False),
            ("d", "Quá trình nung nóng là một biến đổi hóa học kèm theo sự tỏa nhiệt mạnh.", True)
        ], "FeS tạo thành không bị nam châm hút như sắt tự do.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong các hiện tượng: làm kem, xé giấy, đốt rơm rạ, đun sôi dầu ăn. Có bao nhiêu hiện tượng biến đổi vật lí?", "3", "Có 3 hiện tượng vật lí: làm kem, xé giấy, đun sôi dầu ăn."),
        make_sa(2, "Thông hiểu", "Cho dãy các quá trình: (1) Sắt gỉ; (2) Cắt tóc; (3) Lên men sữa chua; (4) Khí gas cháy; (5) Cồn bay hơi. Có bao nhiêu quá trình xảy ra biến đổi hóa học?", "3", "Gồm (1), (3), (4) là biến đổi hóa học."),
        make_sa(3, "Thông hiểu", "Một học sinh liệt kê 6 hiện tượng: hòa tan muối, đốt than củi, nung đá vôi, vắt chanh vào sữa đậu nành, nước đóng băng, mài dao. Số hiện tượng có sự tạo thành chất mới là bao nhiêu?", "3", "Đốt than, nung đá vôi, chanh vào sữa đậu nành (3 hiện tượng)."),
        make_sa(4, "Vận dụng", "Trong công nghiệp làm gốm sứ: tạo hình đất sét (1), phơi khô phôi (2), nung gốm trong lò ở 1200 độ C (3), vẽ trang trí lên men sứ (4). Công đoạn nào chắc chắn xảy ra biến đổi hóa học phức tạp nhất? (Điền số thứ tự 1, 2, 3 hoặc 4)", "3", "Công đoạn (3) nung gốm làm các khoáng silicat phản ứng hóa học."),
        make_sa(5, "Vận dụng", "Để phân biệt biến đổi hóa học với biến đổi vật lí, có tối thiểu bao nhiêu dấu hiệu cơ bản thường quan sát thấy (thay đổi màu sắc, sinh khí, tạo kết tủa, tỏa nhiệt/phát sáng)? Điền một số nguyên từ 1 đến 4.", "4", "Có 4 dấu hiệu cơ bản thường gặp."),
        make_sa(6, "Vận dụng cao", "Tiến hành 5 thí nghiệm: nhỏ dung dịch bạc nitrat vào muối ăn, dẫn khí CO2 vào nước, điện phân nước thành khí H2 và O2, thổi thủy tinh nóng chảy, đốt pháo hoa đêm giao thừa. Có bao nhiêu thí nghiệm là biến đổi hóa học?", "4", "Gồm: kết tủa AgCl, tạo H2CO3, điện phân nước, đốt pháo hoa (4 biến đổi hóa học).")
    ],
    "part4": [
        make_vdc(1, "Một thanh sắt nặng 5,6 g để ngoài không khí ẩm sau một thời gian bị gỉ, đem cân lại thấy nặng 7,2 g. Khối lượng khí oxi trong không khí đã tham gia phản ứng hóa học với sắt là:", ["1,6 g", "2,4 g", "1,2 g", "0,8 g"], 0, "Theo ĐL BTKL: m_O2 = 7,2 - 5,6 = 1,6 g."),
        make_vdc(2, "Khi đốt nến (parafin), hiện tượng nào sau đây kết hợp ĐỒNG THỜI cả biến đổi vật lí và biến đổi hóa học theo đúng trình tự?", ["Nến cháy tạo khí -> nến nóng chảy -> nến đông đặc", "Nến nóng chảy -> nến thấm lên bấc và bay hơi -> hơi nến cháy tạo CO2 và H2O", "Hơi nến cháy tỏa nhiệt -> nến đông đặc thành sáp rắn -> sinh kết tủa", "Nến bay hơi ngay lập tức -> nến hóa lỏng -> tạo muội than đen"], 1, "Trình tự: nóng chảy (lỏng) -> hút lên bấc bay hơi (hơi) -> cháy (hóa học)."),
        make_vdc(3, "Xét các quá trình tự nhiên: (1) Chu trình nước bốc hơi tạo mây rồi rơi thành mưa; (2) Sự hình thành thạch nhũ trong hang động đá vôi; (3) Sự phong hóa đá ngầm do rễ cây tiết axit; (4) Sự bào mòn bờ biển do sóng đánh. Số quá trình có biến đổi hóa học là:", ["1", "2", "3", "4"], 1, "Gồm (2) và (3) là quá trình hóa học."),
        make_vdc(4, "Cho một cục đá vôi vào cốc chứa giấm ăn. Hiện tượng quan sát được chứng minh biến đổi hóa học đã diễn ra là:", ["Cục đá vôi nổi lên trên bề mặt giấm ăn", "Có bọt khí sủi lên bám quanh cục đá vôi và đá vôi tan dần", "Giấm ăn chuyển sang màu tím đậm", "Cốc bị lạnh đi đóng băng thành đá"], 1, "Đá vôi tan dần và sủi bọt khí CO2 chứng tỏ có phản ứng hóa học.")
    ]
}

# --- ĐỀ 2: Các quá trình hóa sinh, môi trường và công nghiệp ---
exams_c1["chem8_c1_b2_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Quá trình nào sau đây là biến đổi hóa học?", ["Thanh đồng bị kéo dài thành sợi dây điện mỏng", "Xăng dầu bốc hơi khi mở nắp bình chứa", "Đốt cháy khí biogas (metan) để đun nấu", "Lấy kéo cắt vụn tấm bìa carton"], 2, "Khí biogas cháy tạo thành khí carbon dioxide và hơi nước."),
        make_mc(2, "Nhận biết", "Hiện tượng vật lí là hiện tượng:", ["Chất này biến đổi thành chất khác hoàn toàn", "Chất bị phân hủy thành các đơn chất ban đầu", "Chất biến đổi về trạng thái, hình dạng nhưng vẫn giữ nguyên là chất đó", "Có sự thay đổi bản chất của các liên kết hóa học"], 2, "Biến đổi vật lí không làm thay đổi bản chất chất."),
        make_mc(3, "Nhận biết", "Trong các thí nghiệm sau, thí nghiệm nào là biến đổi vật lí?", ["Đun sôi nước trong ấm đến khi bay hơi hết", "Đun nóng đường kính đến khi thành than đen", "Nung bột đồng ngoài không khí biến thành bột đen", "Nhỏ axit vào vỏ trứng thấy sủi bọt khí"], 0, "Nước sôi bay hơi chỉ là chuyển từ thể lỏng sang thể hơi."),
        make_mc(4, "Nhận biết", "Hiện tượng gỉ sét của khung cửa sắt ngoài trời thuộc loại biến đổi nào?", ["Biến đổi vật lí do mưa làm trôi sơn", "Biến đổi hóa học do sắt tác dụng với oxi và hơi ẩm", "Biến đổi cơ học do gió thổi mài mòn", "Biến đổi nhiệt học do nắng nóng làm dãn nở"], 1, "Sắt bị oxi hóa thành hợp chất iron oxide/hydroxide."),
        make_mc(5, "Thông hiểu", "Khi hòa tan muối ăn vào nước thu được nước muối trong suốt. Để tách lại muối ăn ban đầu, người ta làm thế nào và đây là hiện tượng gì?", ["Đun sôi để nước bay hơi hết; hiện tượng vật lí", "Lọc qua phễu giấy lọc; hiện tượng hóa học", "Nhỏ thêm axit clohiđric vào; hiện tượng hóa học", "Để yên trong bóng râm cho tự phân hủy; hiện tượng vật lí"], 0, "Cô cạn dung dịch muối ăn là quá trình biến đổi vật lí."),
        make_mc(6, "Thông hiểu", "Cho các hiện tượng: (a) Sữa tươi để lâu ngoài trời bị chua; (b) Thủy ngân trong nhiệt kế co giãn theo nhiệt độ; (c) Quả chuối xanh chín dần thơm ngọt; (d) Xay cà phê hạt thành bột cà phê. Số hiện tượng biến đổi hóa học là:", ["1", "2", "3", "4"], 1, "Gồm (a) và (c) là biến đổi hóa học."),
        make_mc(7, "Thông hiểu", "Hiện tượng quang hợp ở lá cây xanh biến đổi khí CO2 và H2O thành tinh bột và giải phóng O2 là biến đổi:", ["Vật lí vì cây vẫn giữ nguyên màu xanh", "Hóa học vì đã tạo thành các chất mới", "Quang học đơn thuần không sinh chất mới", "Vật lí kèm theo tỏa nhiệt ra môi trường"], 1, "Quá trình quang hợp tổng hợp nên tinh bột và khí oxi."),
        make_mc(8, "Thông hiểu", "Khi nhỏ vài giọt giấm ăn (axit axetic) vào bột baking soda (natri hidrocacbonat), hiện tượng quan sát được là:", ["Hỗn hợp đông đặc lại như thạch", "Sủi bọt khí không màu mạnh mẽ", "Bột baking soda chuyển sang màu đen", "Hỗn hợp phát nổ kèm ánh sáng chói"], 1, "Phản ứng sinh khí CO2 gây hiện tượng sủi bọt."),
        make_mc(9, "Vận dụng", "Trong công nghiệp luyện kim, quá trình nung quặng sắt hematit với than cốc trong lò cao để thu được gang lỏng là:", ["Quá trình vật lí do than nóng chảy hòa tan sắt", "Quá trình hóa học vì sắt được khử từ oxit sắt thành sắt tự do", "Quá trình biến đổi hình dạng hạt quặng", "Quá trình ngưng tụ hơi kim loại"], 1, "Oxit sắt phản ứng với CO để tạo sắt kim loại."),
        make_mc(10, "Vận dụng", "Tại sao vỏ tàu thủy bằng thép đi trên biển thường bị ăn mòn nhanh hơn đi trên sông nước ngọt?", ["Nước biển lạnh hơn nước sông", "Muối trong nước biển đóng vai trò dung dịch chất điện li thúc đẩy phản ứng oxi hóa sắt diễn ra nhanh hơn", "Sóng biển đánh mạnh hơn dòng nước sông", "Ánh nắng mặt trời trên biển gay gắt hơn"], 1, "Môi trường nước muối làm tăng tốc độ ăn mòn hóa học và điện hóa."),
        make_mc(11, "Vận dụng", "Hiện tượng tạo mưa nhân tạo bằng cách bắn các hạt bạc iotua (AgI) hoặc băng khô (CO2 rắn) vào các đám mây là ứng dụng của:", ["Biến đổi hóa học tạo ra nước lỏng", "Biến đổi vật lí kích thích ngưng tụ hơi nước thành giọt mưa", "Phản ứng phân hủy mây thành hơi ẩm", "Biến đổi hóa học giữa AgI và hơi nước"], 1, "Băng khô thăng hoa thu nhiệt làm hơi nước ngưng tụ thành mưa (vật lí)."),
        make_mc(12, "Vận dụng cao", "Tiến hành 4 thao tác: (1) Hòa tan vôi sống vào nước thấy nước sôi sùng sục; (2) Dẫn khí thoát ra từ bếp than qua nước vôi trong thấy đục; (3) Đốt sợi dây magiê cháy sáng chói; (4) Nghiền nát viên than hoa thành bột mịn. Số thao tác tỏa nhiệt do phản ứng hóa học là:", ["1", "2", "3", "4"], 1, "Thao tác (1) tôi vôi và (3) đốt Mg tỏa lượng nhiệt lớn."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các biến đổi của nước trong tự nhiên và đời sống:", [
            ("a", "Nước lỏng bay hơi thành hơi nước là biến đổi vật lí.", True),
            ("b", "Hơi nước ngưng tụ tạo sương mù là biến đổi hóa học.", False),
            ("c", "Điện phân nước tạo thành khí hiđro và khí oxi là biến đổi hóa học.", True),
            ("d", "Nước hòa tan cồn tạo hỗn hợp rượu là biến đổi hóa học.", False)
        ], "Ngưng tụ sương mù và hòa tan cồn là biến đổi vật lí."),
        make_tf(2, "Thông hiểu", "Về các hiện tượng liên quan đến kim loại sắt:", [
            ("a", "Rèn đập thanh sắt đỏ rực thành lưỡi cuốc là biến đổi vật lí.", True),
            ("b", "Đốt cháy dây sắt trong bình khí oxi tạo các hạt oxit sắt từ màu nâu đen là biến đổi hóa học.", True),
            ("c", "Ngâm đinh sắt vào dầu hỏa để chống gỉ là một biến đổi hóa học.", False),
            ("d", "Sắt tan trong dung dịch axit clohiđric sủi bọt khí là biến đổi hóa học.", True)
        ], "Ngâm dầu hỏa chỉ ngăn cách sắt với không khí ẩm (biện pháp vật lí)."),
        make_tf(3, "Vận dụng", "Về quá trình làm bánh mì truyền thống:", [
            ("a", "Trộn bột mì với men nở và nước nhào dẻo là biến đổi vật lí.", True),
            ("b", "Quá trình ủ bột phồng xốp do men sinh khí carbon dioxide là biến đổi hóa học.", True),
            ("c", "Nướng bánh trong lò nhiệt độ cao làm vỏ bánh vàng giòn thơm ngậy là biến đổi hóa học.", True),
            ("d", "Bẻ đôi ổ bánh mì khi ăn là biến đổi hóa học.", False)
        ], "Bẻ đôi chỉ thay đổi hình dạng kích thước (vật lí)."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng nhiệt phân muối kali pemanganat (KMnO4 - thuốc tím):", [
            ("a", "Đun nóng thuốc tím giải phóng khí oxi làm tàn đóm đỏ bùng cháy là biến đổi hóa học.", True),
            ("b", "Chất rắn sau phản ứng có màu đen tím gồm K2MnO4 và MnO2 là những chất mới.", True),
            ("c", "Tổng khối lượng chất rắn thu được sau khi nung lớn hơn khối lượng thuốc tím ban đầu.", False),
            ("d", "Khí oxi sinh ra có thể thu bằng phương pháp đẩy nước do ít tan trong nước.", True)
        ], "Khối lượng chất rắn giảm đi do khí oxi đã bay đi.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong 4 hiện tượng: làm sữa chua, đốt củi, nung vôi, xé vải. Có bao nhiêu hiện tượng biến đổi hóa học?", "3", "Có 3 hiện tượng: làm sữa chua, đốt củi, nung vôi."),
        make_sa(2, "Thông hiểu", "Cho các hiện tượng: (1) Sáp nến chảy lỏng; (2) Cồn cháy; (3) Mỡ đông lại khi trời lạnh; (4) Axit làm quỳ tím đổi màu; (5) Luộc chín quả trứng. Số hiện tượng hóa học là bao nhiêu?", "3", "Gồm (2), (4), (5) là hiện tượng hóa học."),
        make_sa(3, "Thông hiểu", "Một nhóm học sinh làm 5 thí nghiệm: mài gỗ, đánh diêm quẹt, hòa tan đường, rỉ sét chìa khóa, cắt bánh ngọt. Có bao nhiêu thí nghiệm KHÔNG sinh ra chất mới?", "3", "Mài gỗ, hòa tan đường, cắt bánh (3 hiện tượng vật lí)."),
        make_sa(4, "Vận dụng", "Trong dạ dày người, thức ăn được tiêu hóa: (1) cơ học nhờ co bóp nghiền nhỏ thức ăn; (2) hóa học nhờ axit HCl và enzim pepsin biến đổi protein. Quá trình nào là biến đổi hóa học? (Điền số 1 hoặc 2)", "2", "Quá trình (2) là biến đổi hóa học do men và axit phân giải chất."),
        make_sa(5, "Vận dụng", "Một mẫu than chứa 96% carbon đem đốt cháy hoàn toàn trong oxi sinh ra bao nhiêu loại oxide khí chính? (Điền 1 nếu chỉ tạo CO2 hoặc CO)", "1", "Đốt cháy hoàn toàn tạo duy nhất CO2."),
        make_sa(6, "Vận dụng cao", "Tiến hành 6 quá trình: chưng cất dầu mỏ, lên men rượu etylic, bốc hơi nước biển lấy muối, nung thạch cao sống thành thạch cao khan, tôi vôi sống, xát vỏ thóc lấy gạo. Có bao nhiêu quá trình hóa học?", "3", "Gồm: lên men rượu, nung thạch cao thoát nước kết tinh, tôi vôi (3 quá trình).")
    ],
    "part4": [
        make_vdc(1, "Nung 100 g đá vôi (chứa 80% CaCO3, còn lại là tạp chất trơ không bị nhiệt phân) đến khi phản ứng hoàn toàn thu được m gam chất rắn. Biết phản ứng nhiệt phân là: CaCO3 -> CaO + CO2. Khối lượng khí CO2 thoát ra là:", ["35,2 g", "44,0 g", "32,0 g", "28,5 g"], 0, "m_CaCO3 = 80g -> n = 0,8 mol -> m_CO2 = 0,8 * 44 = 35,2 g."),
        make_vdc(2, "Quá trình nào sau đây giải thích sự tạo thành thạch nhũ trong các hang động núi đá vôi là sự kết hợp của hai phản ứng hóa học thuận nghịch?", ["CaCO3 + H2O + CO2 <=> Ca(HCO3)2", "CaO + H2O <=> Ca(OH)2", "Ca(OH)2 + CO2 <=> CaCO3 + H2O", "CaCO3 <=> CaO + CO2"], 0, "Nước có CO2 hòa tan CaCO3 thành Ca(HCO3)2, khi nhỏ giọt mất CO2 kết tủa lại CaCO3."),
        make_vdc(3, "Đốt cháy hoàn toàn 2,4 g kim loại magie (Mg) trong bình chứa khí clo (Cl2) dư, thu được 9,5 g muối magie clorua (MgCl2). Khối lượng khí clo đã tham gia phản ứng là:", ["7,1 g", "11,9 g", "6,5 g", "8,2 g"], 0, "m_Cl2 = 9,5 - 2,4 = 7,1 g."),
        make_vdc(4, "Cho thanh đồng nguyên chất nhúng vào dung dịch bạc nitrat (AgNO3). Hiện tượng nào sau đây khẳng định chắc chắn có biến đổi hóa học xảy ra?", ["Thanh đồng bị tan chảy thành chất lỏng màu đỏ", "Dung dịch từ không màu chuyển dần sang màu xanh lam và có kim loại màu xám bạc bám ngoài thanh đồng", "Có bọt khí mùi khai thoát ra dữ dội", "Dung dịch đông cứng lại thành khối trong suốt"], 1, "Cu + 2AgNO3 -> Cu(NO3)2 (xanh lam) + 2Ag (bạc xám).")
    ]
}

# --- ĐỀ 3: Thí nghiệm thực nghiệm chuyên sâu và phân hóa cao ---
exams_c1["chem8_c1_b2_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Trong các hiện tượng tự nhiên sau, hiện tượng nào là biến đổi hóa học?", ["Thủy triều lên xuống theo chu kì lực hút mặt trăng", "Hiện tượng băng tan ở hai cực Trái Đất", "Lá cây rụng xuống đất lâu ngày bị mục nát phân hủy", "Gió bão làm gãy đổ cành cây"], 2, "Xác lá mục nát là quá trình vi sinh vật phân giải chất hữu cơ sinh chất mới."),
        make_mc(2, "Nhận biết", "Dấu hiệu nào sau đây KHÔNG PHẢI là bằng chứng trực tiếp của một biến đổi hóa học?", ["Có chất khí không màu thoát ra", "Có sự thay đổi nhiệt độ tỏa nhiệt hoặc thu nhiệt", "Khối lượng của vật bị chia làm hai phần do cắt đứt", "Xuất hiện kết tủa lắng xuống đáy cốc"], 2, "Cắt đứt vật thể chỉ là biến đổi cơ học về kích thước."),
        make_mc(3, "Nhận biết", "Khi cho đường mía vào chảo đun nóng lâu, đường chuyển từ màu trắng sang vàng nâu (caramen), rồi cuối cùng thành khối đen xốp có mùi khét. Toàn bộ quá trình này là biến đổi:", ["Vật lí thuần túy", "Ban đầu là vật lí (nóng chảy), sau đó là hóa học (bị than hóa)", "Hóa học hoàn toàn ngay từ đầu", "Sinh học do vi khuẩn phân hủy"], 1, "Đầu tiên đường nóng chảy (vật lí), sau đó phân hủy thành than và nước (hóa học)."),
        make_mc(4, "Nhận biết", "Thổi khí thở của người vào dung dịch nước vôi trong, dung dịch bị vẩn đục do tạo chất mới là:", ["Canxi hiđroxit", "Canxi cacbonat kết tủa trắng", "Khí oxi hòa tan", "Khí nitơ ngưng tụ"], 1, "CO2 + Ca(OH)2 -> CaCO3 (kết tủa trắng) + H2O."),
        make_mc(5, "Thông hiểu", "Cho các hiện tượng: (1) Sương mù tan khi mặt trời lên; (2) Thức ăn để trong tủ lạnh lâu bị mốc; (3) Cầu vồng xuất hiện sau cơn mưa; (4) Nước vôi sống để ngoài không khí bị đóng màng cứng. Số hiện tượng hóa học là:", ["1", "2", "3", "4"], 1, "Gồm (2) mốc và (4) Ca(OH)2 tác dụng CO2 tạo CaCO3."),
        make_mc(6, "Thông hiểu", "Tại sao người ta thường quẹt que diêm vào bề mặt sườn bao diêm để diêm bắt cháy?", ["Để làm nguội que diêm", "Ma sát sinh nhiệt làm photpho đỏ bốc cháy, khơi mào phản ứng hóa học ở đầu que diêm", "Để photpho biến đổi vật lí thành chất lỏng", "Để tạo ra dòng điện tích truyền vào diêm"], 1, "Nhiệt ma sát kích thích phản ứng cháy của photpho đỏ."),
        make_mc(7, "Thông hiểu", "Khi hòa tan amoni nitrat (NH4NO3) vào nước trong cốc thủy tinh, sờ tay vào thành cốc thấy rất lạnh. Đây là hiện tượng gì?", ["Biến đổi hóa học tỏa nhiệt", "Biến đổi vật lí hòa tan kèm theo sự thu nhiệt mạnh", "Biến đổi hóa học tạo khí lạnh", "Hiện tượng ngưng tụ hơi nước bên trong cốc"], 1, "Quá trình hòa tan phân li muối thu nhiệt từ môi trường."),
        make_mc(8, "Thông hiểu", "Hiện tượng tạo thành hang động carxtơ ở các vùng núi đá vôi như vịnh Hạ Long, Phong Nha - Kẻ Bàng chủ yếu là do:", ["Gió mài mòn cơ học hàng triệu năm", "Nước mưa hòa tan khí CO2 tạo axit yếu ăn mòn dần đá vôi CaCO3", "Sóng biển đập vỡ đá vôi thành cát", "Ánh sáng mặt trời nung nóng làm đá vôi nứt nẻ"], 1, "Nước mưa có CO2 hòa tan CaCO3 tạo Ca(HCO3)2."),
        make_mc(9, "Vận dụng", "Trong sản xuất bia rượu, gạo hoặc ngô được đường hóa rồi lên men rượu thành cồn etylic. Đây là:", ["Hai biến đổi vật lí liên tiếp", "Hai biến đổi hóa học liên tiếp do men xúc tác", "Giai đoạn đầu là hóa học, giai đoạn sau là vật lí", "Quá trình bay hơi nước ngưng tụ cồn"], 1, "Tinh bột -> đường glucozo -> rượu etylic đều là phản ứng hóa học."),
        make_mc(10, "Vận dụng", "Để bảo quản táo đã gọt vỏ không bị thâm đen do phản ứng oxi hóa với không khí, người ta ngâm táo vào nước muối nhạt hoặc nước pha ít nước cốt chanh. Thao tác này nhằm mục đích gì?", ["Thực hiện phản ứng biến đổi hóa học làm táo ngọt hơn", "Ngăn chặn và làm chậm quá trình oxi hóa của các enzim trong táo với oxi không khí", "Làm đông lạnh miếng táo", "Tách tinh bột ra khỏi miếng táo"], 1, "Vitamin C và axit citric ức chế phản ứng oxi hóa enzyme."),
        make_mc(11, "Vận dụng", "Cho mẩu kim loại natri vào cốc nước có pha vài giọt phenolphtalein. Hiện tượng nào sau đây chứng tỏ có biến đổi hóa học?", ["Natri tan dần vo tròn chạy trên mặt nước", "Dung dịch chuyển sang màu hồng cánh sen và có khí H2 bay lên", "Cốc nước bị ấm lên", "Tất cả các hiện tượng trên đều chứng minh phản ứng hóa học đã diễn ra"], 3, "2Na + 2H2O -> 2NaOH + H2 tỏa nhiệt làm nóng cốc và kiềm làm hồng phenolphtalein."),
        make_mc(12, "Vận dụng cao", "Tiến hành 4 thí nghiệm: (1) Hòa tan dầu ăn vào xăng; (2) Đốt cháy dầu ăn trên chảo; (3) Dùng dung dịch kiềm xà phòng hóa dầu ăn tạo xà phòng; (4) Để dầu ăn lâu ngày bị ôi khét do oxi hóa. Số thí nghiệm là biến đổi hóa học là:", ["1", "2", "3", "4"], 2, "Gồm (2), (3), (4) là biến đổi hóa học (3 thí nghiệm)."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Xét các biến đổi vật chất trong nấu ăn gia đình:", [
            ("a", "Thái mỏng thịt bò là biến đổi vật lí.", True),
            ("b", "Xào thịt bò chín đổi từ màu đỏ sang màu nâu xám là biến đổi hóa học.", True),
            ("c", "Ướp muối vào thịt làm ngấm gia vị là biến đổi hóa học sinh chất mới.", False),
            ("d", "Mỡ lợn rán thành tóp mỡ giòn và nước mỡ lỏng là quá trình có biến đổi hóa học.", True)
        ], "Ướp muối là quá trình khuếch tán vật lí."),
        make_tf(2, "Thông hiểu", "Về các hiện tượng khí quyển và thời tiết:", [
            ("a", "Hiện tượng sấm sét tạo ra tia lửa điện biến N2 và O2 trong không khí thành NO là biến đổi hóa học.", True),
            ("b", "Mưa đá rơi từ trên cao xuống làm vỡ kính là biến đổi hóa học.", False),
            ("c", "Tầng ozon hấp thụ tia cực tím phân hủy O3 thành O2 là biến đổi hóa học.", True),
            ("d", "Khí thải SO2 từ các nhà máy kết hợp với nước mưa tạo mưa axit là biến đổi hóa học.", True)
        ], "Mưa đá rơi làm vỡ kính chỉ là tác dụng cơ học vật lí."),
        make_tf(3, "Vận dụng", "Về quá trình làm tương nếp truyền thống:", [
            ("a", "Rang chín đỗ tương trên chảo là biến đổi hóa học làm chín và dậy mùi thơm.", True),
            ("b", "Xay nhỏ đỗ tương đã rang là biến đổi vật lí.", True),
            ("c", "Nuôi mốc hoa cau trên xôi nếp là quá trình sinh học enzym tạo chất mới.", True),
            ("d", "Để tương ngoài nắng cho bay bớt nước đặc lại là biến đổi hóa học.", False)
        ], "Nắng làm bay hơi nước là biến đổi vật lí."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm cho bột kẽm (Zn) vào cốc đựng dung dịch đồng sunfat (CuSO4):", [
            ("a", "Màu xanh lam của dung dịch nhạt dần theo thời gian.", True),
            ("b", "Có một lớp kim loại màu đỏ gạch bám ngoài các hạt bột kẽm.", True),
            ("c", "Phản ứng trên thuộc loại biến đổi vật lí vì không có chất khí bay lên.", False),
            ("d", "Tổng khối lượng dung dịch sau phản ứng giảm nhẹ so với dung dịch ban đầu.", True)
        ], "Zn tan ra (65g) thay thế Cu bám vào (64g) nên m_dd tăng nhẹ hoặc thay đổi kim loại.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong các hiện tượng: mây ngưng tụ thành mưa, nến chảy lỏng, sữa chua lên men, bóng bay nổ tung. Có bao nhiêu hiện tượng biến đổi vật lí?", "3", "Có 3 hiện tượng vật lí: mưa ngưng tụ, nến chảy, bóng nổ."),
        make_sa(2, "Thông hiểu", "Cho dãy 5 chất và quá trình: cồn cháy, rỉ đồng màu xanh, hòa tan đường phèn, băng khô thăng hoa, nung đá vôi. Có bao nhiêu quá trình hóa học?", "3", "Cồn cháy, rỉ đồng, nung đá vôi (3 quá trình hóa học)."),
        make_sa(3, "Thông hiểu", "Một bình kín chứa hỗn hợp khí H2 và O2. Bật tia lửa điện để phản ứng xảy ra tạo thành nước. Số loại phân tử đơn chất ban đầu còn lại sau khi phản ứng vừa đủ là bao nhiêu?", "0", "Phản ứng vừa đủ thì cả H2 và O2 đều hết (còn lại 0 phân tử đơn chất)."),
        make_sa(4, "Vận dụng", "Nung m gam bột Cu trong bình khí O2 dư một thời gian thu được 16 g bột CuO màu đen. Biết khối lượng Cu ban đầu là 12,8 g. Khối lượng khí O2 đã phản ứng là bao nhiêu gam? (Ghi số thập phân)", "3,2", "m_O2 = 16 - 12,8 = 3,2 g."),
        make_sa(5, "Vận dụng", "Trong một thí nghiệm, đốt cháy hết 6 g carbon trong oxi dư. Thể tích khí CO2 sinh ra ở đkc (lít) được tính bằng 0,5 x 24,79. Giá trị này bằng bao nhiêu lít? (Làm tròn đến 2 chữ số thập phân)", "12,40", "V = 0,5 * 24,79 = 12,395 xấp xỉ 12,40 L."),
        make_sa(6, "Vận dụng cao", "Có 4 ống nghiệm đựng: (1) Nước cất; (2) Dung dịch giấm ăn; (3) Dung dịch nước vôi trong; (4) Dung dịch muối ăn. Thổi khí CO2 vào từng ống nghiệm. Có bao nhiêu ống nghiệm xảy ra biến đổi hóa học tạo kết tủa đục?", "1", "Chỉ có ống (3) Ca(OH)2 tạo kết tủa CaCO3 vẩn đục.")
    ],
    "part4": [
        make_vdc(1, "Cho 13 g kim loại kẽm tác dụng vừa đủ với dung dịch axit clohiđric thu được dung dịch chứa 27,2 g muối kẽm clorua và giải phóng V lít khí H2 ở đkc. Khối lượng axit HCl đã tham gia phản ứng là:", ["14,6 g", "7,3 g", "21,9 g", "18,2 g"], 0, "n_Zn = 0,2 mol -> n_HCl = 0,4 mol -> m_HCl = 0,4 * 36,5 = 14,6 g."),
        make_vdc(2, "Khi đun nóng hỗn hợp sắt và lưu huỳnh không có không khí, một phản ứng hóa học tự duy trì diễn ra tạo thành chất FeS. Đem sản phẩm hòa tan vào axit HCl dư thấy có mùi trứng thối thoát ra. Khí đó là:", ["H2S (hiđro sunfua)", "SO2 (khí sunfurơ)", "H2 (khí hiđro)", "Cl2 (khí clo)"], 0, "FeS + 2HCl -> FeCl2 + H2S (khí mùi trứng thối đặc trưng)."),
        make_vdc(3, "Để phân biệt 2 hiện tượng biến đổi vật lí và biến đổi hóa học một cách khoa học nhất, người ta dựa vào tiêu chí nào?", ["Sự thay đổi về thể tích của vật", "Sự thay đổi về khối lượng mẫu vật thử", "Sự xuất hiện chất mới có tính chất vật lí và hóa học khác với chất ban đầu", "Sự thay đổi màu sắc quan sát được bằng mắt thường"], 2, "Bản chất là có chất mới tạo thành."),
        make_vdc(4, "Một học sinh thực hiện thí nghiệm cho viên kẽm vào dung dịch CuSO4 màu xanh lam. Sau phản ứng lấy thanh kẽm ra cân lại thấy khối lượng thanh kẽm thay đổi như thế nào? (Biết 1 mol Zn = 65 g tan ra tạo 1 mol Cu = 64 g bám vào)", ["Khối lượng thanh kẽm tăng lên", "Khối lượng thanh kẽm giảm đi", "Khối lượng thanh kẽm giữ nguyên không đổi", "Toàn bộ thanh kẽm biến mất hoàn toàn"], 1, "Cứ 65g Zn tan đi chỉ có 64g Cu bám lại nên m thanh kẽm giảm đi 1g/mol phản ứng.")
    ]
}

print("Đã nạp xong Bài 2 (3 đề độc lập 100%)")
