# -*- coding: utf-8 -*-
"""
HÓA HỌC 8 - CHƯƠNG I: PHẢN ỨNG HÓA HỌC (23 ĐỀ THI ĐỘC LẬP 100%)
Gồm:
- chem8_c1_b2: Bài 2: Biến đổi vật lí và biến đổi hóa học (3 đề)
- chem8_c1_b3: Bài 3: Phản ứng hóa học (3 đề)
- chem8_c1_b4: Bài 4: Định luật bảo toàn khối lượng và phương trình hóa học (3 đề)
- chem8_c1_b5: Bài 5: Mol và tỉ khối của chất khí (3 đề)
- chem8_c1_b6: Bài 6: Nồng độ dung dịch (3 đề)
- chem8_c1_b7: Bài 7: Tốc độ phản ứng và chất xúc tác (3 đề)
- chem8_c1_rev: Ôn tập cuối Chương I (5 đề)
Tất cả các đề trong cùng bài hoàn toàn khác nhau 100%, không trùng câu hỏi, bám sát KNTT.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from build_chem8_c1 import exams_c1

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

# ==============================================================================
# BÀI 3: PHẢN ỨNG HÓA HỌC (3 ĐỀ)
# ==============================================================================

# --- ĐỀ 1: Khái niệm chất phản ứng, sản phẩm, bản chất liên kết thay đổi ---
exams_c1["chem8_c1_b3_test1"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Trong một phản ứng hóa học, chất ban đầu bị biến đổi được gọi là:", ["Chất phản ứng (chất tham gia)", "Chất sản phẩm", "Chất xúc tác", "Chất môi trường"], 0, "Chất ban đầu trước khi xảy ra biến đổi gọi là chất phản ứng."),
        make_mc(2, "Nhận biết", "Quá trình biến đổi chất này thành chất khác được gọi là:", ["Hiện tượng vật lí", "Phản ứng hóa học", "Sự ngưng tụ", "Sự hòa tan"], 1, "Phản ứng hóa học là quá trình biến đổi chất này thành chất khác."),
        make_mc(3, "Nhận biết", "Trong phản ứng hóa học, yếu tố nào sau đây KHÔNG THAY ĐỔI?", ["Số lượng phân tử các chất", "Liên kết giữa các nguyên tử", "Số nguyên tử của mỗi nguyên tố", "Tính chất vật lí của các chất"], 2, "Bản chất phản ứng hóa học là chỉ có liên kết thay đổi, số nguyên tử mỗi nguyên tố bảo toàn."),
        make_mc(4, "Nhận biết", "Cho phản ứng: Khí hiđro + Khí oxi -> Nước. Chất sản phẩm của phản ứng là:", ["Khí hiđro", "Khí oxi", "Nước", "Hỗn hợp hiđro và oxi"], 2, "Nước là chất mới tạo thành sau phản ứng."),
        make_mc(5, "Thông hiểu", "Phương trình chữ nào sau đây biểu diễn đúng phản ứng đốt cháy bột lưu huỳnh trong không khí tạo khí sunfurơ?", ["Lưu huỳnh + Khí oxi -> Khí sunfurơ", "Khí sunfurơ + Khí oxi -> Lưu huỳnh", "Lưu huỳnh -> Khí sunfurơ + Khí oxi", "Lưu huỳnh + Khí nitơ -> Khí sunfurơ"], 0, "Lưu huỳnh phản ứng với oxi tạo khí lưu huỳnh đioxit (sunfurơ)."),
        make_mc(6, "Thông hiểu", "Khi một que đóm còn tàn đỏ được đưa vào bình chứa khí oxi, que đóm bùng cháy lên. Dấu hiệu này chứng minh:", ["Có sự ngưng tụ hơi nước", "Xảy ra phản ứng hóa học tỏa nhiệt và phát sáng mãnh liệt", "Khí oxi bị biến đổi vật lí thành chất lỏng", "Que đóm bị làm lạnh đột ngột"], 1, "Khí oxi duy trì sự cháy, phản ứng tỏa nhiều nhiệt và phát sáng."),
        make_mc(7, "Thông hiểu", "Để phản ứng giữa sắt và lưu huỳnh xảy ra tạo thành sắt(II) sunfua, điều kiện bắt buộc lúc đầu là:", ["Hòa tan vào nước lạnh", "Đun nóng để khơi mào phản ứng", "Chiếu tia cực tím", "Tăng áp suất thật cao"], 1, "Cần đun nóng ban đầu để khơi mào phản ứng tỏa nhiệt."),
        make_mc(8, "Thông hiểu", "Phản ứng hóa học diễn ra được khi các chất phản ứng:", ["Phải ở trạng thái khí", "Tiếp xúc trực tiếp với nhau", "Đều tan tốt trong nước", "Có cùng khối lượng"], 1, "Điều kiện đầu tiên là các chất phản ứng phải tiếp xúc với nhau."),
        make_mc(9, "Vận dụng", "Trước phản ứng có 2 phân tử H2 và 1 phân tử O2. Sau phản ứng tạo thành 2 phân tử H2O. Nhận xét nào sau đây là ĐÚNG?", ["Tổng số phân tử trước và sau phản ứng bằng nhau", "Số nguyên tử H và O trước phản ứng bằng sau phản ứng", "Liên kết giữa các nguyên tử H vẫn giữ nguyên", "Tạo ra chất mới có cùng tính chất với H2"], 1, "Số lượng nguyên tử của mỗi nguyên tố được bảo toàn (4 nguyên tử H và 2 nguyên tử O)."),
        make_mc(10, "Vận dụng", "Trong đời sống, tại sao khi dập tắt bếp than củi người ta thường đậy kín nắp lò hoặc phun nước vào?", ["Để ngăn cách than tiếp xúc với oxi không khí và hạ nhiệt độ xuống dưới nhiệt độ cháy", "Để cung cấp thêm khí CO2 cho than cháy", "Để làm tăng nồng độ khí oxi xung quanh than", "Để biến đổi than củi thành than đá"], 0, "Hạ nhiệt độ và cách li than với oxi là nguyên tắc dập tắt đám cháy."),
        make_mc(11, "Vận dụng", "Cho các phản ứng: (1) Cồn cháy tỏa nhiệt; (2) Hòa tan vôi sống vào nước nóng lên; (3) Nung đá vôi cần cấp nhiệt liên tục; (4) Khí gas cháy đun sôi nước. Phản ứng nào là phản ứng thu nhiệt?", ["(1)", "(2)", "(3)", "(4)"], 2, "Nung đá vôi hấp thụ nhiệt năng liên tục từ lò nung (phản ứng thu nhiệt)."),
        make_mc(12, "Vận dụng cao", "Một bạn học sinh viết phương trình chữ: Magiê + Axit clohiđric -> Magiê clorua + Khí hiđro. Nếu cho 4,8 g magiê phản ứng hoàn toàn với dung dịch chứa 14,6 g axit clohiđric thu được 19,0 g magiê clorua. Khối lượng khí hiđro thoát ra là:", ["0,4 g", "0,2 g", "0,8 g", "0,6 g"], 0, "Theo ĐL BTKL: m_H2 = (4,8 + 14,6) - 19,0 = 0,4 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về bản chất và diễn biến của phản ứng hóa học:", [
            ("a", "Trong phản ứng hóa học, chỉ có liên kết giữa các nguyên tử bị biến đổi.", True),
            ("b", "Số lượng nguyên tử của mỗi nguyên tố tăng lên sau phản ứng.", False),
            ("c", "Các phân tử chất phản ứng bị phân rã và tái tổ hợp thành phân tử chất sản phẩm.", True),
            ("d", "Khối lượng của từng nguyên tử bị thay đổi trong quá trình phản ứng.", False)
        ], "Số lượng và khối lượng từng nguyên tử được giữ nguyên."),
        make_tf(2, "Thông hiểu", "Về điều kiện xảy ra và dấu hiệu nhận biết phản ứng:", [
            ("a", "Mọi phản ứng hóa học đều cần đun nóng liên tục mới xảy ra.", False),
            ("b", "Sự xuất hiện chất kết tủa không tan là một dấu hiệu chứng minh có phản ứng xảy ra.", True),
            ("c", "Một số phản ứng cần có chất xúc tác để thúc đẩy tốc độ phản ứng nhanh hơn.", True),
            ("d", "Sự sủi bọt khí không tan thoát ra khỏi dung dịch là bằng chứng có chất mới sinh ra.", True)
        ], "Nhiều phản ứng xảy ra ngay ở nhiệt độ thường khi tiếp xúc (như axit tác dụng bazơ)."),
        make_tf(3, "Vận dụng", "Về phản ứng tỏa nhiệt và thu nhiệt trong đời sống:", [
            ("a", "Phản ứng tỏa nhiệt là phản ứng giải phóng năng lượng dưới dạng nhiệt ra môi trường.", True),
            ("b", "Quá trình đốt cháy xăng xe trong động cơ là phản ứng thu nhiệt.", False),
            ("c", "Phản ứng tôi vôi sống: CaO + H2O -> Ca(OH)2 làm nước sôi sùng sục là phản ứng tỏa nhiệt.", True),
            ("d", "Quá trình quang hợp của cây xanh hấp thụ năng lượng ánh sáng mặt trời có bản chất tương tự phản ứng thu nhiệt.", True)
        ], "Đốt cháy xăng dầu là phản ứng tỏa nhiệt cực mạnh."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng nhiệt phân đường mía (saccarozơ C12H22O11) trong ống nghiệm khô:", [
            ("a", "Trên thành ống nghiệm xuất hiện những giọt nước đọng lại là sản phẩm của phản ứng.", True),
            ("b", "Chất rắn màu đen còn lại trong ống nghiệm là nguyên tố than (carbon).", True),
            ("c", "Đây là phản ứng tỏa nhiệt vì đường tự bốc cháy mà không cần đèn cồn cung cấp nhiệt.", False),
            ("d", "Phương trình chữ của phản ứng: Đường mía -> Nước + Carbon.", True)
        ], "Phản ứng cần đun nóng liên tục bằng đèn cồn nên là phản ứng thu nhiệt.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phản ứng: Kẽm + Axit clohiđric -> Kẽm clorua + Khí hiđro, có bao nhiêu chất phản ứng?", "2", "Có 2 chất phản ứng: Kẽm và Axit clohiđric."),
        make_sa(2, "Thông hiểu", "Cho các hiện tượng: cháy cồn, gỉ sắt, hô hấp tế bào, quang hợp, tôi vôi. Có bao nhiêu quá trình tỏa nhiệt ra môi trường xung quanh?", "4", "Cháy cồn, gỉ sắt, hô hấp, tôi vôi đều tỏa nhiệt (4 quá trình)."),
        make_sa(3, "Thông hiểu", "Trong một phân tử nước H2O có tổng cộng bao nhiêu nguyên tử liên kết với nhau?", "3", "Gồm 2 nguyên tử H và 1 nguyên tử O (tổng 3 nguyên tử)."),
        make_sa(4, "Vận dụng", "Đốt cháy 1,2 g bột cacbon trong khí oxi thu được 4,4 g khí cacbon đioxit. Khối lượng khí oxi đã phản ứng là bao nhiêu gam? (Ghi số thập phân)", "3,2", "m_O2 = 4,4 - 1,2 = 3,2 g."),
        make_sa(5, "Vận dụng", "Để đốt cháy hoàn toàn 1 mol khí metan CH4 cần đúng 2 mol khí oxi O2. Số mol khí CO2 sinh ra là bao nhiêu mol?", "1", "CH4 + 2O2 -> CO2 + 2H2O -> sinh 1 mol CO2."),
        make_sa(6, "Vận dụng cao", "Cho phương trình phản ứng: a Fe + b Cl2 -> c FeCl3. Tổng các hệ số tối giản (a + b + c) của phương trình hóa học này là bao nhiêu?", "7", "2Fe + 3Cl2 -> 2FeCl3. Tổng hệ số: 2 + 3 + 2 = 7.")
    ],
    "part4": [
        make_vdc(1, "Nung nóng 50 g canxi cacbonat (đá vôi) thu được 28 g canxi oxit và một lượng khí canxi cacbon đioxit. Thể tích khí CO2 thu được ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Biết n = 22 / 44 = 0,5 mol)", ["12,395 lít", "24,79 lít", "11,2 lít", "22,4 lít"], 0, "m_CO2 = 50 - 28 = 22g -> n = 0,5 mol -> V = 0,5 * 24,79 = 12,395 L."),
        make_vdc(2, "Khi dẫn khí H2 dư đi qua ống nghiệm chứa bột CuO màu đen nung nóng đỏ, hiện tượng quan sát được chứng minh phản ứng hóa học xảy ra là:", ["Bột CuO chuyển từ màu đen sang màu đỏ của đồng và có hơi nước ngưng tụ ở đầu ống nghiệm", "Bột CuO tan hoàn toàn thành chất lỏng không màu", "Ống nghiệm phát nổ kèm theo khí có mùi hắc", "Không có hiện tượng gì xảy ra"], 0, "H2 + CuO (đen) -> Cu (đỏ) + H2O (lỏng)."),
        make_vdc(3, "Ứng dụng nào sau đây khai thác năng lượng từ phản ứng hóa học tỏa nhiệt phục vụ đời sống con người?", ["Chạy động cơ xe máy bằng xăng sinh học", "Hàn đường ray xe lửa bằng hỗn hợp tecmit (nhôm và oxit sắt)", "Đun nấu thức ăn bằng khí gas hóa lỏng", "Cả 3 ứng dụng trên đều đúng"], 3, "Tất cả đều sử dụng năng lượng nhiệt tỏa ra từ phản ứng hóa học."),
        make_vdc(4, "Một bình kín dung tích không đổi chứa hỗn hợp khí N2 và H2 theo tỉ lệ mol 1 : 3. Sau khi thực hiện phản ứng tổng hợp amoniac (N2 + 3H2 -> 2NH3), áp suất trong bình thay đổi như thế nào ở cùng nhiệt độ?", ["Áp suất trong bình tăng lên do phân tử NH3 nặng hơn", "Áp suất trong bình giảm xuống do tổng số mol khí giảm đi", "Áp suất trong bình không thay đổi", "Áp suất ban đầu giảm rồi sau đó tăng vọt"], 1, "Cứ 1 mol N2 + 3 mol H2 (tổng 4 mol) tạo ra 2 mol NH3 nên số phân tử khí giảm -> áp suất giảm.")
    ]
}

# --- ĐỀ 2: Điều kiện phản ứng, dấu hiệu nhận biết, thí nghiệm tỏa nhiệt ---
exams_c1["chem8_c1_b3_test2"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Dấu hiệu nào sau đây cho biết có phản ứng hóa học xảy ra khi nhỏ dung dịch bari clorua vào dung dịch natri sunfat?", ["Xuất hiện kết tủa màu trắng", "Có bọt khí bay lên mạnh mẽ", "Dung dịch bốc cháy sáng chói", "Nhiệt độ dung dịch hạ xuống 0 độ C"], 0, "BaCl2 + Na2SO4 -> BaSO4 (kết tủa trắng) + 2NaCl."),
        make_mc(2, "Nhận biết", "Phản ứng tỏa nhiệt là phản ứng hóa học:", ["Giải phóng năng lượng dưới dạng nhiệt ra môi trường", "Hấp thụ nhiệt năng từ môi trường xung quanh", "Làm môi trường xung quanh lạnh đi rõ rệt", "Chỉ xảy ra khi liên tục đun nóng bằng ngọn lửa"], 0, "Định nghĩa phản ứng tỏa nhiệt: tỏa nhiệt ra môi trường."),
        make_mc(3, "Nhận biết", "Trong phương trình chữ của phản ứng hóa học, tên các chất tham gia được viết ở phía nào của mũi tên?", ["Bên trái mũi tên", "Bên phải mũi tên", "Phía trên mũi tên", "Phía dưới mũi tên"], 0, "Quy ước: Chất phản ứng -> Chất sản phẩm."),
        make_mc(4, "Nhận biết", "Chất xúc tác là chất có vai trò:", ["Làm tăng tốc độ phản ứng và không bị biến đổi sau phản ứng", "Làm thay đổi sản phẩm của phản ứng hóa học", "Bị tiêu hao hoàn toàn trong phản ứng", "Ngăn cản phản ứng hóa học không xảy ra"], 0, "Xúc tác đẩy nhanh phản ứng nhưng giữ nguyên về lượng và chất."),
        make_mc(5, "Thông hiểu", "Khi hòa tan viên sủi hạ sốt vào cốc nước, ta thấy sủi bọt khí và cầm vào cốc thấy mát nhẹ. Hiện tượng sủi bọt khí chứng tỏ:", ["Viên sủi bay hơi thành hơi sủi", "Đã xảy ra phản ứng hóa học tạo ra chất khí mới", "Nước phản ứng với thủy tinh", "Nhiệt độ nước tăng vọt"], 1, "Axit xitric phản ứng với NaHCO3 tạo khí CO2."),
        make_mc(6, "Thông hiểu", "Cho mẩu đá vôi vào dung dịch axit clohiđric, dấu hiệu chứng tỏ phản ứng xảy ra là:", ["Đá vôi đổi thành màu xanh", "Có bọt khí thoát ra và đá vôi tan dần", "Dung dịch đông cứng lại", "Cốc phát ra tiếng nổ lớn"], 1, "CaCO3 + 2HCl -> CaCl2 + H2O + CO2 (khí)."),
        make_mc(7, "Thông hiểu", "Quá trình hô hấp của cơ thể người lấy khí oxi để đốt cháy các chất dinh dưỡng tạo CO2, H2O và:", ["Hấp thụ nhiệt làm cơ thể lạnh đi", "Giải phóng năng lượng để duy trì thân nhiệt và hoạt động sống", "Tiêu hủy hoàn toàn các tế bào", "Làm giảm cân nặng tức thì về 0"], 1, "Hô hấp tế bào là phản ứng tỏa nhiệt cung cấp năng lượng sống."),
        make_mc(8, "Thông hiểu", "Thí nghiệm nào sau đây thể hiện phản ứng thu nhiệt rõ rệt nhất?", ["Hòa tan vôi sống vào nước", "Nhiệt phân thuốc tím (KMnO4) để điều chế oxi", "Đốt cháy que diêm", "Cho bột kẽm vào dung dịch axit"], 1, "Nhiệt phân KMnO4 cần liên tục cung cấp nhiệt từ ngọn lửa đèn cồn."),
        make_mc(9, "Vận dụng", "Để phân biệt phản ứng tỏa nhiệt và phản ứng thu nhiệt bằng thực nghiệm, dụng cụ đo đơn giản và chính xác nhất là:", ["Cân điện tử", "Nhiệt kế", "Thước kẹp", "Ống đong"], 1, "Nhiệt kế theo dõi sự tăng hoặc giảm nhiệt độ của hệ phản ứng."),
        make_mc(10, "Vận dụng", "Trong công nghiệp hàn cắt kim loại, người ta dùng ngọn lửa axetilen - oxi (C2H2 + O2) có thể đạt nhiệt độ trên 3000 °C. Đây là phản ứng:", ["Thu nhiệt cực lớn", "Tỏa nhiệt với lượng nhiệt rất lớn", "Quang hợp nhân tạo", "Phân hủy axetilen"], 1, "Phản ứng cháy của axetilen tỏa nhiệt cực lớn làm nóng chảy kim loại."),
        make_mc(11, "Vận dụng", "Khi đốt cháy hoàn toàn một mẩu than củi trong bình kín chứa khí oxi, sau phản ứng đưa que đóm còn tàn đỏ vào bình thì que đóm tắt ngay. Điều này giải thích là do:", ["Khí oxi trong bình đã phản ứng hết và sinh ra khí carbon dioxide không duy trì sự cháy", "Bình bị lạnh đi đột ngột", "Khí hiđro sinh ra làm tắt đóm", "Than biến đổi thành nước dập tắt đóm"], 0, "O2 đã hết, khí CO2 không duy trì sự cháy làm đóm tắt."),
        make_mc(12, "Vận dụng cao", "Cho mẩu kim loại natri phản ứng với khí clo theo sơ đồ: Na + Cl2 -> NaCl. Biết 4,6 g natri tác dụng vừa đủ với m gam khí clo sinh ra 11,7 g muối ăn (NaCl). Giá trị của m là:", ["7,1 g", "16,3 g", "3,55 g", "5,85 g"], 0, "m_Cl2 = 11,7 - 4,6 = 7,1 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về các hiện tượng tỏa nhiệt và thu nhiệt:", [
            ("a", "Phản ứng nung đá vôi thành vôi sống là phản ứng thu nhiệt.", True),
            ("b", "Khi vôi sống tác dụng với nước, nhiệt độ của hỗn hợp tăng lên rất cao là phản ứng tỏa nhiệt.", True),
            ("c", "Quá trình hòa tan đường ăn vào nước là phản ứng hóa học thu nhiệt.", False),
            ("d", "Phản ứng cháy của than đá trong lò luyện gang tỏa nhiệt lớn cung cấp nhiệt lượng cho quá trình luyện kim.", True)
        ], "Hòa tan đường là quá trình hòa tan vật lí."),
        make_tf(2, "Thông hiểu", "Về điều kiện khơi mào và duy trì phản ứng hóa học:", [
            ("a", "Mọi phản ứng hóa học một khi đã xảy ra thì không bao giờ dừng lại.", False),
            ("b", "Nhiều phản ứng chỉ cần khơi mào nhiệt ban đầu, sau đó lượng nhiệt tỏa ra sẽ tự duy trì phản ứng (như đốt than, quẹt diêm).", True),
            ("c", "Tăng diện tích tiếp xúc giữa các chất tham gia giúp phản ứng diễn ra thuận lợi hơn.", True),
            ("d", "Chất xúc tác sau phản ứng sẽ bị chuyển hóa thành một chất khác có màu sắc mới.", False)
        ], "Chất xúc tác không bị biến đổi về chất và lượng sau phản ứng."),
        make_tf(3, "Vận dụng", "Về các dấu hiệu nhận biết phản ứng trong phòng thí nghiệm:", [
            ("a", "Nhỏ axit vào bazo có pha phenolphtalein, màu hồng biến mất chứng tỏ có phản ứng xảy ra.", True),
            ("b", "Nhỏ vài giọt iot vào hồ tinh bột thấy xuất hiện màu xanh tím đặc trưng là phản ứng hóa học.", True),
            ("c", "Đun sôi nước thấy hơi nước bốc lên mù mịt là phản ứng hóa học sinh chất khí mới.", False),
            ("d", "Thả viên kẽm vào axit clohiđric thấy sủi bọt khí H2 là biến đổi hóa học.", True)
        ], "Nước sôi bốc hơi là biến đổi trạng thái vật lí."),
        make_tf(4, "Vận dụng cao", "Xét thí nghiệm đốt cháy dải ruy-băng magie (Mg) ngoài không khí:", [
            ("a", "Magie cháy tạo ra ngọn lửa sáng chói lòa và tỏa nhiều nhiệt.", True),
            ("b", "Sản phẩm thu được là chất bột màu trắng có tên gọi là magie oxit (MgO).", True),
            ("c", "Khối lượng chất bột trắng MgO thu được nhỏ hơn khối lượng dải magie ban đầu.", False),
            ("d", "Phương trình chữ: Magiê + Khí oxi -> Magiê oxit.", True)
        ], "m_MgO = m_Mg + m_O2 nên khối lượng chất rắn tăng lên.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phản ứng: Khí metan + Khí oxi -> Khí cacbon đioxit + Nước, có bao nhiêu chất sản phẩm?", "2", "Có 2 chất sản phẩm: CO2 và H2O."),
        make_sa(2, "Thông hiểu", "Cho các phản ứng: đốt nến, tôi vôi, nung đá vôi, que diêm cháy, quang hợp. Có bao nhiêu phản ứng thu nhiệt?", "2", "Nung đá vôi và quang hợp là phản ứng thu nhiệt (2 phản ứng)."),
        make_sa(3, "Thông hiểu", "Một phân tử khí cacbonic CO2 gồm 1 nguyên tử C liên kết với bao nhiêu nguyên tử oxi?", "2", "Gồm 2 nguyên tử oxi."),
        make_sa(4, "Vận dụng", "Đốt cháy hoàn toàn 6,4 g bột đồng (Cu) trong khí oxi dư thu được 8,0 g đồng(II) oxit (CuO). Khối lượng khí oxi đã phản ứng là bao nhiêu gam? (Ghi số thập phân)", "1,6", "m_O2 = 8,0 - 6,4 = 1,6 g."),
        make_sa(5, "Vận dụng", "Hòa tan hoàn toàn 2,7 g nhôm vào dung dịch HCl dư. Phương trình: 2Al + 6HCl -> 2AlCl3 + 3H2. Số mol khí H2 sinh ra tính bằng (2,7 / 27) x 1,5. Giá trị này bằng bao nhiêu mol? (Ghi số thập phân)", "0,15", "n_Al = 0,1 mol -> n_H2 = 0,15 mol."),
        make_sa(6, "Vận dụng cao", "Cho phản ứng: a Al + b O2 -> c Al2O3. Tổng các hệ số nguyên tối giản (a + b + c) của phương trình là bao nhiêu?", "9", "4Al + 3O2 -> 2Al2O3. Tổng hệ số: 4 + 3 + 2 = 9.")
    ],
    "part4": [
        make_vdc(1, "Nhiệt phân hoàn toàn 24,5 g muối kali clorat (KClO3) có chất xúc tác MnO2, thu được 14,9 g muối kali clorua (KCl) và V lít khí oxi (đkc, 25 °C, 1 bar). Biết n_O2 = 9,6 / 32 = 0,3 mol. Thể tích V bằng:", ["7,437 lít", "6,72 lít", "24,79 lít", "14,874 lít"], 0, "m_O2 = 24,5 - 14,9 = 9,6 g -> n = 0,3 mol -> V = 0,3 * 24,79 = 7,437 L."),
        make_vdc(2, "Tại sao khi nướng thịt trên bếp than, người ta thường dùng quạt nan hoặc quạt điện thổi gió vào bếp?", ["Gió thổi làm nguội miếng thịt không bị cháy", "Gió cung cấp thêm khí oxi và tăng nhiệt độ làm than cháy mạnh hơn", "Gió thổi bay hơi nước trong thịt làm thịt ngọt hơn", "Gió biến than củi thành than đá"], 1, "Thổi gió cung cấp dồi dào O2 giúp phản ứng cháy than diễn ra nhanh và mãnh liệt."),
        make_vdc(3, "Bình cứu hỏa dạng bột chứa chất natri hiđrocacbonat (NaHCO3). Khi phun vào đám cháy, NaHCO3 bị phân hủy nhiệt tạo thành chất khí nào giúp ngăn cản oxi tiếp xúc với ngọn lửa?", ["Khí cacbon đioxit (CO2)", "Khí oxi (O2)", "Khí hiđro (H2)", "Khí clo (Cl2)"], 0, "2NaHCO3 -> Na2CO3 + CO2 + H2O. Khí CO2 nặng hơn không khí trùm kín ngọn lửa."),
        make_vdc(4, "Một hỗn hợp gồm 2,8 g Fe và 1,6 g S được nung nóng trong ống nghiệm kín không có không khí. Sau phản ứng hoàn toàn, khối lượng chất rắn FeS thu được là:", ["4,4 g", "3,2 g", "5,6 g", "4,0 g"], 0, "n_Fe = 2,8/56 = 0,05 mol; n_S = 1,6/32 = 0,05 mol (vừa đủ) -> m_FeS = 0,05 * 88 = 4,4 g.")
    ]
}

# --- ĐỀ 3: Phương trình chữ, phân loại phản ứng, liên hệ vi mô ---
exams_c1["chem8_c1_b3_test3"] = {
    "part1": [
        make_mc(1, "Nhận biết", "Trong một phản ứng hóa học, các nguyên tử được liên kết lại theo cách mới là do:", ["Sự phá vỡ các liên kết cũ và hình thành các liên kết mới", "Sự sinh ra các hạt electron mới", "Sự phân hủy các proton trong hạt nhân", "Sự biến mất của các nguyên tử ban đầu"], 0, "Liên kết giữa các nguyên tử thay đổi làm phân tử này biến thành phân tử khác."),
        make_mc(2, "Nhận biết", "Phản ứng thu nhiệt là phản ứng hóa học có đặc điểm:", ["Nhiệt độ của hệ tăng lên rất cao", "Hấp thụ năng lượng nhiệt từ môi trường xung quanh", "Tự phát sáng chói lòa trong bóng tối", "Tự duy trì mà không cần bất kì nguồn năng lượng nào"], 1, "Phản ứng thu nhiệt hấp thu nhiệt năng làm môi trường lạnh đi."),
        make_mc(3, "Nhận biết", "Phương trình chữ nào sau đây viết ĐÚNG cho phản ứng nhiệt phân muối canxi cacbonat thành vôi sống và khí cacbonic?", ["Canxi cacbonat -> Canxi oxit + Khí cacbon đioxit", "Canxi oxit + Canxi cacbonat -> Khí cacbon đioxit", "Khí cacbon đioxit + Canxi oxit -> Canxi cacbonat", "Canxi cacbonat + Khí oxi -> Canxi oxit"], 0, "CaCO3 -> CaO + CO2."),
        make_mc(4, "Nhận biết", "Hiện tượng thanh sắt ngâm trong dung dịch đồng sunfat bị bao phủ bởi lớp kim loại màu đỏ là do:", ["Sắt bị nóng chảy", "Phản ứng hóa học tạo ra kim loại đồng tự do bám vào", "Dung dịch đồng sunfat đông đặc", "Lớp rỉ sét của sắt có màu đỏ gạch"], 1, "Fe + CuSO4 -> FeSO4 + Cu (đỏ)."),
        make_mc(5, "Thông hiểu", "Cho phương trình chữ: Kẽm + Axit sunfuric -> Kẽm sunfat + Khí hiđro. Nếu muốn thu khí hiđro vào ống nghiệm úp ngược, ta dựa vào tính chất nào của hiđro?", ["Khí hiđro nặng hơn không khí", "Khí hiđro rất nhẹ hơn không khí và ít tan trong nước", "Khí hiđro có màu vàng lục", "Khí hiđro có mùi khai"], 1, "H2 nhẹ nhất trong các chất khí nên thu bằng cách úp bình."),
        make_mc(6, "Thông hiểu", "Khi thắp đèn dầu, dầu hỏa được hút lên theo bấc và cháy ở đầu bấc ngọn lửa vàng. Năng lượng tỏa ra chủ yếu ở dạng:", ["Quang năng và nhiệt năng", "Điện năng và cơ năng", "Hóa năng tích trữ", "Hạt nhân"], 0, "Phản ứng cháy tỏa nhiệt năng sưởi ấm và quang năng chiếu sáng."),
        make_mc(7, "Thông hiểu", "Thí nghiệm trộn bột nhôm với bột lưu huỳnh rồi châm ngòi bằng dây magie cháy, hỗn hợp nổ bùng sáng chói và tỏa nhiệt cực lớn. Đây là phản ứng:", ["Thu nhiệt", "Tỏa nhiệt mạnh", "Vật lí đơn thuần", "Chậm không quan sát được"], 1, "Phản ứng giữa Al và S tỏa nhiệt rất lớn."),
        make_mc(8, "Thông hiểu", "Túi chườm lạnh y tế tức thì thường chứa nước và túi muối amoni nitrat (NH4NO3). Khi bóp vỡ túi nước bên trong để muối tan, túi nhanh chóng lạnh buốt. Quá trình hòa tan này là:", ["Biến đổi hóa học tỏa nhiệt", "Quá trình thu nhiệt mạnh từ xung quanh", "Sự ngưng tụ hơi ẩm", "Phản ứng tạo đá lạnh"], 1, "NH4NO3 hòa tan thu nhiệt mạnh làm giảm nhiệt độ tức thì."),
        make_mc(9, "Vận dụng", "Trong công nghiệp sản xuất vôi, để nung chín đá vôi người ta phải liên tục cấp than vào lò đốt. Điều này chứng tỏ phản ứng nhiệt phân đá vôi là:", ["Phản ứng tỏa nhiệt tự duy trì", "Phản ứng thu nhiệt cần năng lượng ngoài cung cấp", "Phản ứng không cần nhiệt độ", "Hiện tượng bay hơi nước"], 1, "Cần cấp nhiệt liên tục chứng minh đây là phản ứng thu nhiệt."),
        make_mc(10, "Vận dụng", "Cho phương trình chữ: Natri hiđroxit + Axit clohiđric -> Natri clorua + Nước. Cả 2 dung dịch ban đầu đều không màu, sau phản ứng dung dịch vẫn không màu. Để nhận biết phản ứng xảy ra, người ta dùng:", ["Quỳ tím hoặc chỉ thị phenolphtalein", "Cân khối lượng dung dịch", "Ống đong thể tích", "Kính hiển vi quang học"], 0, "Dùng chất chỉ thị màu để nhận biết điểm tương đương của phản ứng trung hòa."),
        make_mc(11, "Vận dụng", "Đốt cháy 0,6 g bột magie trong không khí thu được 1,0 g magie oxit (chất rắn màu trắng). Khối lượng khí oxi trong không khí đã kết hợp với magie là:", ["0,4 g", "1,6 g", "0,2 g", "0,5 g"], 0, "m_O2 = 1,0 - 0,6 = 0,4 g."),
        make_mc(12, "Vận dụng cao", "Dẫn luồng khí CO đi qua ống sứ nung nóng chứa 16 g bột oxit sắt Fe2O3. Sau phản ứng thu được 11,2 g kim loại sắt và khí CO2 thoát ra. Khối lượng khí CO đã tham gia phản ứng là:", ["8,4 g", "5,6 g", "11,2 g", "4,2 g"], 0, "n_Fe = 11,2/56 = 0,2 mol -> n_O tách ra = 0,3 mol -> n_CO = 0,3 mol -> m_CO = 0,3 * 28 = 8,4 g."),
    ],
    "part2": [
        make_tf(1, "Thông hiểu", "Về ngôn ngữ hóa học và phương trình chữ:", [
            ("a", "Dấu '+' ở vế chất phản ứng đọc là 'tác dụng với' hoặc 'phản ứng với'.", True),
            ("b", "Dấu mũi tên '->' đọc là 'tạo thành' hoặc 'sinh ra'.", True),
            ("c", "Dấu '+' ở vế sản phẩm đọc là 'và'.", True),
            ("d", "Trong phương trình chữ, ta có thể viết công thức hóa học thay cho tên chất.", False)
        ], "Phương trình chữ dùng tên gọi của các chất."),
        make_tf(2, "Thông hiểu", "Về năng lượng trong các phản ứng hóa học:", [
            ("a", "Phản ứng quang hợp tích lũy năng lượng mặt trời dưới dạng hóa năng trong phân tử tinh bột.", True),
            ("b", "Quá trình hô hấp giải phóng hóa năng tích trữ thành nhiệt năng và ATP cho tế bào.", True),
            ("c", "Tất cả các phản ứng tỏa nhiệt đều tự bốc cháy mà không cần nhiệt độ khơi mào.", False),
            ("d", "Các túi sưởi ấm mùa đông dựa trên phản ứng oxi hóa chậm của bột sắt tỏa nhiệt êm dịu.", True)
        ], "Nhiều phản ứng tỏa nhiệt như than củi, cồn cần mồi lửa ban đầu mới cháy."),
        make_tf(3, "Vận dụng", "Về sự biến đổi của các chất trong thí nghiệm vôi sống:", [
            ("a", "Khi nhỏ nước vào vôi sống CaO, vôi sống hút nước vỡ vụn và bốc khói hơi nước mù mịt.", True),
            ("b", "Nhiệt độ của bát sứ sau khi tôi vôi có thể đạt trên 100 °C làm nước sôi sùng sục.", True),
            ("c", "Sản phẩm thu được sau khi tôi vôi là canxi cacbonat kết tủa rắn chắc.", False),
            ("d", "Phản ứng tôi vôi là phản ứng tỏa nhiệt mạnh.", True)
        ], "Sản phẩm là vôi tôi Ca(OH)2."),
        make_tf(4, "Vận dụng cao", "Xét phản ứng nung quặng pirit sắt (FeS2) trong lò sản xuất axit sunfuric:", [
            ("a", "Chất phản ứng là quặng pirit sắt và khí oxi trong không khí.", True),
            ("b", "Chất sản phẩm là oxit sắt (Fe2O3) và khí sunfurơ (SO2).", True),
            ("c", "Khí SO2 sinh ra có mùi hắc đặc trưng và gây độc cho đường hô hấp.", True),
            ("d", "Đây là phản ứng thu nhiệt vì cần cấp than đốt liên tục trong suốt 1 năm hoạt động của lò.", False)
        ], "Phản ứng đốt cháy quặng pirit tỏa nhiệt lượng rất lớn, sau khi khơi mào không cần cấp thêm nhiên liệu.")
    ],
    "part3": [
        make_sa(1, "Nhận biết", "Trong phương trình: Cacbon + Khí oxi -> Khí cacbon đioxit, có bao nhiêu chất phản ứng?", "2", "Có 2 chất phản ứng: Cacbon và Oxi."),
        make_sa(2, "Thông hiểu", "Cho các hiện tượng: nến cháy, vôi tôi, điện phân nước, nung thạch cao, hòa tan sút vào nước. Có bao nhiêu quá trình tỏa nhiệt?", "3", "Nến cháy, vôi tôi, hòa tan sút NaOH tỏa nhiệt (3 quá trình)."),
        make_sa(3, "Thông hiểu", "Trong một phân tử khí amoniac NH3 có 1 nguyên tử nitơ liên kết với bao nhiêu nguyên tử hiđro?", "3", "Liên kết với 3 nguyên tử hiđro."),
        make_sa(4, "Vận dụng", "Cho m gam kim loại kẽm phản ứng với lưu huỳnh vừa đủ thu được 9,7 g kẽm sunfua (ZnS). Biết khối lượng lưu huỳnh đã dùng là 3,2 g. Giá trị của m là bao nhiêu gam? (Ghi số thập phân)", "6,5", "m_Zn = 9,7 - 3,2 = 6,5 g."),
        make_sa(5, "Vận dụng", "Đốt cháy hoàn toàn 1,6 g khí metan CH4 thu được 4,4 g khí CO2 và bao nhiêu gam nước? (Ghi số thập phân)", "3,6", "CH4 + 2O2 -> CO2 + 2H2O. n_CH4 = 0,1 mol -> m_H2O = 0,2 * 18 = 3,6 g."),
        make_sa(6, "Vận dụng cao", "Cân bằng phương trình: a Fe3O4 + b CO -> c Fe + d CO2. Tổng hệ số nguyên tối giản (a + b + c + d) là bao nhiêu?", "12", "Fe3O4 + 4CO -> 3Fe + 4CO2. Tổng: 1 + 4 + 3 + 4 = 12.")
    ],
    "part4": [
        make_vdc(1, "Để điều chế khí oxi trong phòng thí nghiệm, người ta đun nóng hoàn toàn 31,6 g thuốc tím KMnO4. Thể tích khí oxi thu được ở điều kiện chuẩn (25 °C, 1 bar) là bao nhiêu lít? (Biết n_O2 = 0,1 mol)", ["2,479 lít", "2,24 lít", "4,958 lít", "1,2395 lít"], 0, "2KMnO4 -> K2MnO4 + MnO2 + O2. n_KMnO4 = 0,2 mol -> n_O2 = 0,1 mol -> V = 0,1 * 24,79 = 2,479 L."),
        make_vdc(2, "Khi dập tắt đám cháy kim loại kiềm như natri, magie, tại sao TUYỆT ĐỐI KHÔNG ĐƯỢC dùng bình chữa cháy CO2 hoặc nước?", ["Vì CO2 và H2O sẽ phản ứng mãnh liệt với Mg và Na ở nhiệt độ cao sinh khí H2 và khí độc, làm đám cháy bùng nổ dữ dội hơn", "Vì nước và CO2 làm đông đặc natri", "Vì nước quá đắt tiền", "Vì bình CO2 quá nhẹ không dập được kim loại"], 0, "Mg cháy được trong khí CO2 tạo MgO + C tỏa nhiệt lớn; Na tác dụng mãnh liệt với H2O sinh H2 gây nổ."),
        make_vdc(3, "Hiện tượng nào sau đây là ứng dụng của phản ứng hóa học thu nhiệt?", ["Sử dụng túi chườm lạnh cấp cứu chấn thương thể thao tức thì", "Nấu ăn bằng bếp củi", "Hàn kim loại bằng mỏ hàn nhiệt", "Sưởi ấm bằng đèn dầu"], 0, "Túi chườm lạnh hấp thu nhiệt từ vùng bị viêm sưng để hạ nhiệt độ tức thì."),
        make_vdc(4, "Cho 10 g hỗn hợp gồm bột sắt và bột đồng tác dụng với lượng dư dung dịch axit clohiđric HCl, thấy có 2,479 lít khí hiđro thoát ra ở đkc (tương ứng 0,1 mol H2). Biết đồng không tác dụng với dung dịch HCl. Khối lượng bột đồng trong hỗn hợp là:", ["4,4 g", "5,6 g", "3,2 g", "6,4 g"], 0, "Fe + 2HCl -> FeCl2 + H2. n_Fe = 0,1 mol -> m_Fe = 5,6 g -> m_Cu = 10 - 5,6 = 4,4 g.")
    ]
}

print("Đã nạp xong Bài 3 (3 đề độc lập 100%)")
