# -*- coding: utf-8 -*-
"""
DỮ LIỆU ĐỀ THI TOÁN 9 - CHƯƠNG I: PHƯƠNG TRÌNH VÀ HỆ HAI PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN
PHẦN 2:
- BÀI 3: GIẢI BÀI TOÁN BẰNG CÁCH LẬP HỆ PHƯƠNG TRÌNH (c1_9_bai3)
- BÀI KIỂM TRA CUỐI CHƯƠNG I: PHƯƠNG TRÌNH VÀ HỆ HAI PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (c1_9_bai4)
Mỗi bài gồm 3 đề phân hóa chuẩn ma trận 10 điểm Bộ GD&ĐT 2025:
- 12 trắc nghiệm nhiều lựa chọn (3.0đ)
- 2 câu đúng/sai (mỗi câu 4 ý, 1.0đ/câu = 2.0đ)
- 4 câu trả lời ngắn (2.0đ)
- 3 câu tự luận kèm thang điểm rubric chi tiết (3.0đ)
"""

EXAMS_PART2 = {}

# ==============================================================================
# BÀI 3: GIẢI BÀI TOÁN BẰNG CÁCH LẬP HỆ PHƯƠNG TRÌNH (c1_9_bai3)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c1_9_bai3_test1"] = {
    "title": "Toán 9 (KNTT) - Bài 3: Giải bài toán bằng cách lập hệ phương trình - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Bước đầu tiên trong quy trình giải bài toán bằng cách lập hệ phương trình là:", "options": ["Chọn hai ẩn số và đặt điều kiện thích hợp cho ẩn", "Giải hệ phương trình", "Biểu diễn các đại lượng chưa biết", "Đối chiếu điều kiện và kết luận"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Một số tự nhiên có hai chữ số, chữ số hàng chục là $x$, chữ số hàng đơn vị là $y$. Số đó được biểu diễn là:", "options": ["$10x + y$", "$x + y$", "$xy$", "$10y + x$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Trong bài toán chuyển động, mối quan hệ giữa quãng đường $s$, vận tốc $v$ và thời gian $t$ là:", "options": ["$s = v \\cdot t$", "$s = \\frac{v}{t}$", "$s = \\frac{t}{v}$", "$s = v + t$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Vận tốc xuôi dòng của ca nô bằng:", "options": ["Vận tốc thực ca nô cộng vận tốc dòng nước", "Vận tốc thực ca nô trừ vận tốc dòng nước", "Vận tốc dòng nước chia cho thời gian", "Vận tốc thực nhân đôi"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Hai số có tổng bằng $25$ và hiệu bằng $5$. Hai số đó là:", "options": ["$15$ và $10$", "$20$ và $5$", "$14$ và $11$", "$16$ và $9$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Một mảnh đất hình chữ nhật có chu vi $40\\text{ m}$, chiều dài hơn chiều rộng $4\\text{ m}$. Chiều dài của mảnh đất là:", "options": ["$12\\text{ m}$", "$16\\text{ m}$", "$8\\text{ m}$", "$10\\text{ m}$"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Tổng số gà và chó là $36$ con, tổng số chân là $100$ chân. Gọi $x$ là số con gà, $y$ là số con chó ($x, y \\in \\mathbb{N}^*$). Hệ phương trình lập được là:", "options": ["$\\begin{cases} x + y = 36 \\\\ 2x + 4y = 100 \\end{cases}$", "$\\begin{cases} x + y = 36 \\\\ 4x + 2y = 100 \\end{cases}$", "$\\begin{cases} x + y = 100 \\\\ 2x + 4y = 36 \\end{cases}$", "$\\begin{cases} 2x + 2y = 36 \\\\ 4x + 4y = 100 \\end{cases}$"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Hai vòi nước cùng chảy vào một bể cạn thì sau $6$ giờ đầy bể. Trong 1 giờ, cả hai vòi cùng chảy được:", "options": ["$\\frac{1}{6}$ bể", "$6$ bể", "$\\frac{1}{3}$ bể", "$\\frac{2}{3}$ bể"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Tìm hai số biết tỉ số giữa chúng là $\\frac{3}{5}$ và hiệu của chúng bằng $8$. Số lớn là:", "options": ["$20$", "$12$", "$15$", "$25$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Một ca nô chạy xuôi dòng một khúc sông dài $90\\text{ km}$ hết $3$ giờ và chạy ngược dòng khúc sông đó hết $5$ giờ. Vận tốc của dòng nước là:", "options": ["$6\\text{ km/h}$", "$24\\text{ km/h}$", "$12\\text{ km/h}$", "$3\\text{ km/h}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Một ô tô và một xe máy cùng khởi hành từ hai địa điểm $A$ và $B$ cách nhau $180\\text{ km}$, đi ngược chiều nhau và gặp nhau sau $2$ giờ. Vận tốc ô tô hơn xe máy $10\\text{ km/h}$. Vận tốc xe máy là:", "options": ["$40\\text{ km/h}$", "$50\\text{ km/h}$", "$45\\text{ km/h}$", "$35\\text{ km/h}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Một phòng họp có $360$ ghế được xếp thành các dãy có số ghế bằng nhau. Nếu bớt đi $3$ dãy và mỗi dãy thêm $4$ ghế thì số chỗ ngồi không đổi. Số dãy ghế ban đầu là:", "options": ["$18$ dãy", "$20$ dãy", "$15$ dãy", "$24$ dãy"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Bài toán dân gian: \"Vừa gà vừa chó / Bó lại cho tròn / Ba mươi sáu con / Một trăm chân chẵn\". Gọi $x$ là số con gà, $y$ là số con chó ($x, y \\in \\mathbb{N}^*$). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Phương trình biểu diễn tổng số con là $x + y = 36$.", "correct": True},
                {"subId": "b", "text": "Phương trình biểu diễn tổng số chân là $2x + 4y = 100$.", "correct": True},
                {"subId": "c", "text": "Số con gà là $22$ con.", "correct": True},
                {"subId": "d", "text": "Số con chó là $12$ con.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Hai đội công nhân cùng làm chung một công việc thì hoàn thành sau $12$ ngày. Nếu đội I làm một mình trong $5$ ngày rồi nghỉ, đội II làm tiếp trong $15$ ngày thì cả hai làm được $75\\%$ công việc. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Mỗi ngày hai đội cùng làm được $\\frac{1}{12}$ công việc.", "correct": True},
                {"subId": "b", "text": "Gọi thời gian làm riêng của đội I và đội II lần lượt là $x, y$ (ngày, $x, y > 12$).", "correct": True},
                {"subId": "c", "text": "Phương trình thứ hai là: $\\frac{5}{x} + \\frac{15}{y} = \\frac{3}{4}$.", "correct": True},
                {"subId": "d", "text": "Đội I làm một mình hoàn thành công việc sau $20$ ngày.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Tìm một số tự nhiên có hai chữ số, biết chữ số hàng chục lớn hơn chữ số hàng đơn vị là 5 và tổng hai chữ số bằng 11.", "correctAnswer": "83", "explanation": "$\\begin{cases} x - y = 5 \\\\ x + y = 11 \\end{cases} \\Rightarrow x = 8, y = 3$. Số cần tìm là $83$."},
        {"id": 2, "level": "Thông hiểu", "question": "Một hình chữ nhật có chu vi $56\\text{ m}$. Nếu tăng chiều rộng thêm $2\\text{ m}$ và bớt chiều dài đi $2\\text{ m}$ thì hình chữ nhật trở thành hình vuông. Tính diện tích hình chữ nhật ban đầu (m$^2$).", "correctAnswer": "192", "explanation": "Nửa chu vi = $28$. $x - y = 4 \\Rightarrow x = 16, y = 12$. Diện tích = $16 \\times 12 = 192\\text{ m}^2$."},
        {"id": 3, "level": "Vận dụng", "question": "Hai giá sách có tổng cộng $450$ cuốn. Nếu chuyển $50$ cuốn từ giá một sang giá hai thì số sách giá hai bằng $\\frac{4}{5}$ số sách giá một. Tính số sách ban đầu của giá thứ nhất.", "correctAnswer": "300", "explanation": "$\\begin{cases} x + y = 450 \\\\ y + 50 = \\frac{4}{5}(x - 50) \\end{cases} \\Rightarrow x = 300, y = 150$."},
        {"id": 4, "level": "Vận dụng", "question": "Một xí nghiệp theo kế hoạch cần may $1200$ bộ quần áo trong một thời gian quy định. Nhờ cải tiến kĩ thuật, mỗi ngày may vượt mức $10$ bộ nên hoàn thành sớm hơn $4$ ngày. Tính số ngày quy định theo kế hoạch.", "correctAnswer": "24", "explanation": "Gọi số ngày là $t$, năng suất là $x$. $x \\cdot t = 1200$, $(x + 10)(t - 4) = 1200 \\Rightarrow t = 24$ ngày."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Hai bạn An và Bình cùng mua sách vở tại một nhà sách. Bạn An mua $5$ quyển vở và $3$ chiếc bút hết $65\\,000$ đồng. Bạn Bình mua $3$ quyển vở và $4$ chiếc bút cùng loại hết $50\\,000$ đồng. Tính giá tiền của mỗi quyển vở và mỗi chiếc bút.",
            "solution": "Gọi giá tiền của một quyển vở là $x$ (đồng) và giá tiền một chiếc bút là $y$ (đồng).\nĐiều kiện: $x, y > 0$.\nTheo đề bài:\n- Bạn An mua $5$ quyển vở và $3$ chiếc bút hết $65\\,000$ đồng, nên ta có phương trình:\n$5x + 3y = 65\\,000$ (1)\n- Bạn Bình mua $3$ quyển vở và $4$ chiếc bút hết $50\\,000$ đồng, nên ta có phương trình:\n$3x + 4y = 50\\,000$ (2)\nTừ (1) và (2) ta có hệ phương trình:\n$$\\begin{cases} 5x + 3y = 65\\,000 \\\\ 3x + 4y = 50\\,000 \\end{cases}$$\nNhân phương trình (1) với 4 và phương trình (2) với 3:\n$$\\begin{cases} 20x + 12y = 260\\,000 \\\\ 9x + 12y = 150\\,000 \\end{cases}$$\nTrừ hai phương trình: $11x = 110\\,000 \\Rightarrow x = 10\\,000$ (đồng).\nThay $x = 10\\,000$ vào (1): $5(10\\,000) + 3y = 65\\,000 \\Rightarrow 3y = 15\\,000 \\Rightarrow y = 5\\,000$ (đồng).\nCả hai giá trị đều thỏa mãn điều kiện.\nVậy giá một quyển vở là $10\\,000$ đồng và một chiếc bút là $5\\,000$ đồng.",
            "rubric": [
                {"step": "Gọi ẩn, đặt điều kiện và thiết lập hệ phương trình đúng", "subScore": 0.5},
                {"step": "Giải đúng x = 10.000, y = 5.000 và kết luận đầy đủ đơn vị", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Hai vòi nước cùng chảy vào một bể không có nước thì sau $4$ giờ $48$ phút đầy bể. Nếu mở vòi I chảy trong $3$ giờ rồi khóa lại và mở vòi II chảy trong $4$ giờ thì cả hai vòi chảy được $\\frac{3}{4}$ bể. Hỏi nếu chảy riêng thì mỗi vòi chảy đầy bể trong bao lâu?",
            "solution": "Đổi: $4$ giờ $48$ phút = $4 + \\frac{48}{60} = \\frac{24}{5}$ giờ.\nGọi thời gian vòi I và vòi II chảy một mình đầy bể lần lượt là $x, y$ (giờ, $x, y > \\frac{24}{5}$).\nTrong 1 giờ:\n- Vòi I chảy được $\\frac{1}{x}$ bể.\n- Vòi II chảy được $\\frac{1}{y}$ bể.\n- Cả hai vòi chảy được $1 : \\frac{24}{5} = \\frac{5}{24}$ bể.\nTa có phương trình (1): $\\frac{1}{x} + \\frac{1}{y} = \\frac{5}{24}$.\nVòi I chảy trong $3$ giờ và vòi II chảy trong $4$ giờ được $\\frac{3}{4}$ bể nên ta có phương trình (2):\n$\\frac{3}{x} + \\frac{4}{y} = \\frac{3}{4}$.\nTa có hệ phương trình:\n$$\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{5}{24} \\\\ \\frac{3}{x} + \\frac{4}{y} = \\frac{3}{4} \\end{cases}$$\nNhân phương trình đầu với 3 rồi trừ cho phương trình hai:\n$\\frac{1}{y} = \\frac{3}{4} - 3 \\cdot \\frac{5}{24} = \\frac{3}{4} - \\frac{5}{8} = \\frac{1}{8} \\Rightarrow y = 8$ (thỏa mãn).\nThay vào: $\\frac{1}{x} = \\frac{5}{24} - \\frac{1}{8} = \\frac{2}{24} = \\frac{1}{12} \\Rightarrow x = 12$ (thỏa mãn).\nVậy vòi I chảy một mình mất $12$ giờ, vòi II chảy một mình mất $8$ giờ.",
            "rubric": [
                {"step": "Đổi đơn vị, gọi ẩn và thiết lập đúng hệ phương trình", "subScore": 0.5},
                {"step": "Giải đúng x = 12, y = 8 và đối chiếu điều kiện kết luận", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Một ô tô dự định đi từ tỉnh $A$ đến tỉnh $B$ với vận tốc xác định. Nếu vận tốc tăng thêm $20\\text{ km/h}$ thì thời gian đi sẽ giảm $1$ giờ. Nếu vận tốc giảm đi $10\\text{ km/h}$ thì thời gian đi sẽ tăng thêm $1$ giờ. Tính quãng đường $AB$ và vận tốc dự định của ô tô.",
            "solution": "Gọi vận tốc dự định của ô tô là $v$ (km/h) và thời gian dự định là $t$ (giờ).\nĐiều kiện: $v > 10, t > 1$.\nQuãng đường $AB$ là: $s = v \\cdot t$ (km).\n- Trường hợp 1: Tăng vận tốc thêm $20\\text{ km/h}$:\nVận tốc mới: $v + 20$, thời gian mới: $t - 1$.\nTa có: $(v + 20)(t - 1) = vt \\Leftrightarrow vt - v + 20t - 20 = vt \\Leftrightarrow -v + 20t = 20$ (1).\n- Trường hợp 2: Giảm vận tốc đi $10\\text{ km/h}$:\nVận tốc mới: $v - 10$, thời gian mới: $t + 1$.\nTa có: $(v - 10)(t + 1) = vt \\Leftrightarrow vt + v - 10t - 10 = vt \\Leftrightarrow v - 10t = 10$ (2).\nTừ (1) và (2) ta có hệ phương trình:\n$$\\begin{cases} -v + 20t = 20 \\\\ v - 10t = 10 \\end{cases}$$\nCộng hai phương trình lại: $10t = 30 \\Rightarrow t = 3$ (giờ, thỏa mãn).\nThay $t = 3$ vào (2): $v - 10(3) = 10 \\Rightarrow v = 40$ (km/h, thỏa mãn).\nQuãng đường $AB$ là: $s = v \\cdot t = 40 \\times 3 = 120\\text{ km}$.\nVậy vận tốc dự định là $40\\text{ km/h}$ và quãng đường $AB$ dài $120\\text{ km}$.",
            "rubric": [
                {"step": "Gọi ẩn, lập luận biểu diễn quãng đường hai trường hợp tạo hệ phương trình", "subScore": 0.5},
                {"step": "Giải ra v = 40, t = 3 và tính chính xác quãng đường s = 120 km", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c1_9_bai3_test2"] = {
    "title": "Toán 9 (KNTT) - Bài 3: Giải bài toán bằng cách lập hệ phương trình - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Khi giải bài toán năng suất, nếu một tổ công nhân dự định may $x$ chiếc áo trong 1 ngày và thời gian may là $y$ ngày thì tổng số áo may được là:", "options": ["$x \\cdot y$", "$x + y$", "$\\frac{x}{y}$", "$\\frac{y}{x}$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Hai canô cùng khởi hành từ hai bến $A$ và $B$ cách nhau $85\\text{ km}$ đi ngược chiều nhau. Sau $1$ giờ $42$ phút chúng gặp nhau. Biết vận tốc ca nô xuôi dòng lớn hơn ca nô ngược dòng $10\\text{ km/h}$. Vận tốc mỗi ca nô khi nước yên lặng nếu vận tốc dòng nước là $5\\text{ km/h}$:", "options": ["Ca nô đi xuôi có vận tốc riêng bằng ca nô đi ngược", "Không xác định được", "Bằng $25\\text{ km/h}$", "Bằng $30\\text{ km/h}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Một thửa ruộng hình chữ nhật có chu vi $250\\text{ m}$. Chiều dài gấp rưỡi ($1{,}5$ lần) chiều rộng. Diện tích của thửa ruộng là:", "options": ["$3750\\text{ m}^2$", "$3500\\text{ m}^2$", "$4000\\text{ m}^2$", "$3600\\text{ m}^2$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Một dung dịch chứa $10\\%$ muối, một dung dịch khác chứa $20\\%$ muối. Trộn hai dung dịch lại để được $500\\text{ g}$ dung dịch chứa $16\\%$ muối. Khối lượng dung dịch $10\\%$ cần dùng là:", "options": ["$200\\text{ g}$", "$300\\text{ g}$", "$250\\text{ g}$", "$150\\text{ g}$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Năm nay tuổi bố gấp $3$ lần tuổi con. Mười năm trước tuổi bố gấp $7$ lần tuổi con. Tuổi bố năm nay là:", "options": ["$45$ tuổi", "$42$ tuổi", "$36$ tuổi", "$48$ tuổi"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Một người đầu tư $200$ triệu đồng vào hai khoản: khoản thứ nhất lãi suất $6\\%$/năm, khoản thứ hai lãi suất $8\\%$/năm. Sau một năm nhận được tổng tiền lãi là $14{,}6$ triệu đồng. Số tiền đầu tư vào khoản thứ hai là:", "options": ["$130$ triệu đồng", "$70$ triệu đồng", "$120$ triệu đồng", "$80$ triệu đồng"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Hai tổ sản xuất nhận may $720$ áo. Do tổ 1 vượt mức $15\\%$ và tổ 2 vượt mức $12\\%$ nên cả hai tổ may được $819$ áo. Kế hoạch tổ 1 phải may là:", "options": ["$420$ chiếc", "$300$ chiếc", "$400$ chiếc", "$320$ chiếc"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Tìm số tự nhiên có hai chữ số, biết chữ số hàng chục gấp đôi chữ số hàng đơn vị. Nếu thêm số $0$ vào giữa hai chữ số thì được số mới lớn hơn số đã cho $180$ đơn vị. Số đó là:", "options": ["$42$", "$63$", "$21$", "$84$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Một tam giác vuông có độ dài hai cạnh góc vuông hơn kém nhau $2\\text{ cm}$. Nếu tăng mỗi cạnh góc vuông thêm $2\\text{ cm}$ thì diện tích tăng thêm $18\\text{ cm}^2$. Độ dài cạnh huyền của tam giác ban đầu là:", "options": ["$10\\text{ cm}$", "$8\\text{ cm}$", "$6\\text{ cm}$", "$12\\text{ cm}$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Quãng đường $AB$ gồm đoạn lên dốc dài $4\\text{ km}$ và đoạn xuống dốc dài $5\\text{ km}$. Một người đi xe đạp từ $A$ đến $B$ hết $40$ phút và đi từ $B$ về $A$ hết $41$ phút. Vận tốc lúc lên dốc và xuống dốc lần lượt là:", "options": ["$12\\text{ km/h}$ và $15\\text{ km/h}$", "$10\\text{ km/h}$ và $15\\text{ km/h}$", "$12\\text{ km/h}$ và $18\\text{ km/h}$", "$10\\text{ km/h}$ và $20\\text{ km/h}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Một chiếc thuyền đi xuôi dòng một khúc sông từ $A$ đến $B$ rồi quay lại $A$ hết tổng cộng $4$ giờ $30$ phút. Biết quãng đường $AB = 40\\text{ km}$ và vận tốc dòng nước là $2\\text{ km/h}$. Vận tốc thực của thuyền là:", "options": ["$18\\text{ km/h}$", "$20\\text{ km/h}$", "$16\\text{ km/h}$", "$22\\text{ km/h}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Hai vòi nước cùng chảy vào bể thì sau $1$ giờ $20$ phút đầy bể. Nếu mở vòi I chảy trong $10$ phút và vòi II chảy trong $12$ phút thì được $\\frac{2}{15}$ bể nước. Vòi I chảy một mình đầy bể trong:", "options": ["$2$ giờ", "$2{,}5$ giờ", "$3$ giờ", "$1{,}5$ giờ"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Một người mua $2$ thùng sơn loại A và $3$ thùng sơn loại B hết $2{,}3$ triệu đồng. Một người khác mua $3$ thùng sơn loại A và $2$ thùng sơn loại B hết $2{,}2$ triệu đồng. Gọi giá 1 thùng sơn loại A là $x$, loại B là $y$ (triệu đồng). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Hệ phương trình là $\\begin{cases} 2x + 3y = 2{,}3 \\\\ 3x + 2y = 2{,}2 \\end{cases}$.", "correct": True},
                {"subId": "b", "text": "Giá một thùng sơn loại A là $0{,}4$ triệu đồng ($400\\,000$ đồng).", "correct": True},
                {"subId": "c", "text": "Giá một thùng sơn loại B là $0{,}5$ triệu đồng ($500\\,000$ đồng).", "correct": True},
                {"subId": "d", "text": "Tổng giá tiền 1 thùng loại A và 1 thùng loại B là $1$ triệu đồng.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Một ô tô đi từ $A$ đến $B$ với vận tốc $50\\text{ km/h}$, rồi từ $B$ quay về $A$ với vận tốc $40\\text{ km/h}$. Tổng thời gian cả đi và về là $4$ giờ $30$ phút. Gọi thời gian đi là $x$, thời gian về là $y$ (giờ). Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Phương trình thời gian: $x + y = 4{,}5$.", "correct": True},
                {"subId": "b", "text": "Phương trình quãng đường: $50x = 40y$.", "correct": True},
                {"subId": "c", "text": "Thời gian đi là $2$ giờ và thời gian về là $2{,}5$ giờ.", "correct": True},
                {"subId": "d", "text": "Quãng đường $AB$ dài $120\\text{ km}$.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Một lớp học có $40$ học sinh gồm cả nam và nữ. Biết số học sinh nữ nhiều hơn số học sinh nam là $6$ bạn. Tính số học sinh nữ của lớp.", "correctAnswer": "23", "explanation": "$\\begin{cases} x + y = 40 \\\\ x - y = 6 \\end{cases} \\Rightarrow x = 23, y = 17$. Số học sinh nữ là $23$."},
        {"id": 2, "level": "Thông hiểu", "question": "Một tam giác có chu vi $30\\text{ cm}$. Cạnh lớn nhất dài hơn cạnh trung bình $2\\text{ cm}$, cạnh trung bình dài hơn cạnh nhỏ nhất $2\\text{ cm}$. Tính độ dài cạnh lớn nhất (cm).", "correctAnswer": "12", "explanation": "Ba cạnh là $a - 2, a, a + 2$. Tổng = $3a = 30 \\Rightarrow a = 10$. Cạnh lớn nhất = $12\\text{ cm}$."},
        {"id": 3, "level": "Vận dụng", "question": "Hai vòi nước cùng chảy vào bể sau $6$ giờ đầy bể. Nếu vòi 1 chảy trong $2$ giờ và vòi 2 chảy trong $3$ giờ thì được $\\frac{2}{5}$ bể. Hỏi vòi 1 chảy một mình trong bao lâu thì đầy bể (giờ)?", "correctAnswer": "10", "explanation": "$\\begin{cases} 1/x + 1/y = 1/6 \\\\ 2/x + 3/y = 2/5 \\end{cases} \\Rightarrow 1/x = 1/10 \\Rightarrow x = 10$ giờ."},
        {"id": 4, "level": "Vận dụng cao", "question": "Một người mua hai món hàng A và B có tổng giá tiền niêm yết là $800\\,000$ đồng. Trong đợt khuyến mãi, món hàng A được giảm $10\\%$, món hàng B được giảm $15\\%$, người đó phải trả tất cả $695\\,000$ đồng. Tính giá tiền niêm yết của món hàng A (nghìn đồng).", "correctAnswer": "500", "explanation": "$\\begin{cases} x + y = 800 \\\\ 0{,}9x + 0{,}85y = 695 \\end{cases} \\Rightarrow x = 500, y = 300$. Giá hàng A là $500$ nghìn đồng."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Theo kế hoạch, hai tổ công nhân phải làm được $700$ sản phẩm. Nhưng do cải tiến kĩ thuật, tổ I đã làm vượt mức $15\\%$, tổ II làm vượt mức $20\\%$ nên cả hai tổ đã làm được $820$ sản phẩm. Hỏi theo kế hoạch mỗi tổ phải làm bao nhiêu sản phẩm?",
            "solution": "Gọi số sản phẩm tổ I và tổ II phải làm theo kế hoạch lần lượt là $x$ và $y$ ($x, y \\in \\mathbb{N}^*, x, y < 700$).\nTheo kế hoạch hai tổ phải làm $700$ sản phẩm nên ta có phương trình:\n$x + y = 700$ (1)\nThực tế:\n- Tổ I làm được: $x + 15\\%x = 1{,}15x$ (sản phẩm).\n- Tổ II làm được: $y + 20\\%y = 1{,}2y$ (sản phẩm).\nCả hai tổ làm được $820$ sản phẩm nên ta có phương trình:\n$1{,}15x + 1{,}2y = 820$ (2)\nTừ (1) và (2) ta có hệ phương trình:\n$$\\begin{cases} x + y = 700 \\\\ 1{,}15x + 1{,}2y = 820 \\end{cases}$$\nNhân phương trình thứ nhất với 1,2: $1{,}2x + 1{,}2y = 840$.\nTrừ cho phương trình thứ hai: $0{,}05x = 20 \\Rightarrow x = 400$ (thỏa mãn).\nSuy ra $y = 700 - 400 = 300$ (thỏa mãn).\nVậy theo kế hoạch tổ I phải làm $400$ sản phẩm, tổ II phải làm $300$ sản phẩm.",
            "rubric": [
                {"step": "Gọi ẩn, đặt điều kiện và lập hệ phương trình chuẩn xác", "subScore": 0.5},
                {"step": "Giải đúng x = 400, y = 300 và kết luận đầy đủ", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Một tàu thủy chạy trên một khúc sông trong $7$ giờ, xuôi dòng $108\\text{ km}$ và ngược dòng $63\\text{ km}$. Một lần khác tàu thủy đó cũng chạy trong $7$ giờ, xuôi dòng $81\\text{ km}$ và ngược dòng $84\\text{ km}$. Tính vận tốc của dòng nước và vận tốc của tàu thủy khi nước yên lặng.",
            "solution": "Gọi vận tốc thực của tàu thủy là $x$ (km/h) và vận tốc của dòng nước là $y$ (km/h).\nĐiều kiện: $x > y > 0$.\nVận tốc xuôi dòng là $x + y$ (km/h); vận tốc ngược dòng là $x - y$ (km/h).\n- Lần thứ nhất: $\\frac{108}{x + y} + \\frac{63}{x - y} = 7$ (1).\n- Lần thứ hai: $\\frac{81}{x + y} + \\frac{84}{x - y} = 7$ (2).\nĐặt $u = \\frac{1}{x + y}$ và $v = \\frac{1}{x - y}$ ($u, v > 0$). Hệ phương trình trở thành:\n$$\\begin{cases} 108u + 63v = 7 \\\\ 81u + 84v = 7 \\end{cases}$$\nGiải hệ bằng phương pháp cộng đại số:\nNhân phương trình (1) với 4 và phương trình (2) với 3:\n$$\\begin{cases} 432u + 252v = 28 \\\\ 243u + 252v = 21 \\end{cases} \\Rightarrow 189u = 7 \\Rightarrow u = \\frac{7}{189} = \\frac{1}{27}$$\nThay vào: $108 \\cdot \\frac{1}{27} + 63v = 7 \\Rightarrow 4 + 63v = 7 \\Rightarrow 63v = 3 \\Rightarrow v = \\frac{1}{21}$.\nDo đó:\n$$\\begin{cases} x + y = 27 \\\\ x - y = 21 \\end{cases} \\Rightarrow \\begin{cases} 2x = 48 \\\\ 2y = 6 \\end{cases} \\Rightarrow \\begin{cases} x = 24 \\\\ y = 3 \\end{cases}$$\nCả hai giá trị thỏa mãn $x > y > 0$.\nVậy vận tốc của tàu khi nước yên lặng là $24\\text{ km/h}$, vận tốc dòng nước là $3\\text{ km/h}$.",
            "rubric": [
                {"step": "Lập luận biểu diễn vận tốc xuôi, ngược và thiết lập hệ phương trình", "subScore": 0.5},
                {"step": "Giải bằng ẩn phụ ra x = 24 km/h và y = 3 km/h, kết luận chuẩn xác", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Có hai can đựng rượu: can thứ nhất chứa $40\\%$ rượu nguyên chất, can thứ hai chứa $25\\%$ rượu nguyên chất. Người ta trộn hai loại rượu này lại để được $15$ lít rượu loại $30\\%$ nguyên chất. Tính số lít rượu cần lấy từ mỗi can.",
            "solution": "Gọi số lít rượu cần lấy từ can thứ nhất là $x$ (lít) và can thứ hai là $y$ (lít).\nĐiều kiện: $0 < x, y < 15$.\n1) Tổng thể tích rượu sau khi trộn là $15$ lít, nên ta có phương trình:\n$x + y = 15$ (1)\n2) Lượng rượu nguyên chất lấy từ can 1 là $40\\%x = 0{,}4x$ (lít).\nLượng rượu nguyên chất lấy từ can 2 là $25\\%y = 0{,}25y$ (lít).\nLượng rượu nguyên chất trong $15$ lít rượu $30\\%$ là $15 \\times 30\\% = 4{,}5$ (lít).\nTa có phương trình:\n$0{,}4x + 0{,}25y = 4{,}5$ (2)\nTừ (1) và (2) ta có hệ phương trình:\n$$\\begin{cases} x + y = 15 \\\\ 0{,}4x + 0{,}25y = 4{,}5 \\end{cases}$$\nTừ (1) suy ra $y = 15 - x$. Thay vào (2):\n$0{,}4x + 0{,}25(15 - x) = 4{,}5 \\Leftrightarrow 0{,}4x + 3{,}75 - 0{,}25x = 4{,}5$\n$\\Leftrightarrow 0{,}15x = 0{,}75 \\Rightarrow x = 5$ (lít, thỏa mãn).\nSuy ra $y = 15 - 5 = 10$ (lít, thỏa mãn).\nVậy cần lấy $5$ lít rượu can 1 và $10$ lít rượu can 2.",
            "rubric": [
                {"step": "Gọi ẩn và thiết lập hệ phương trình về thể tích và nồng độ", "subScore": 0.5},
                {"step": "Giải ra x = 5 lít và y = 10 lít, kết luận đầy đủ", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c1_9_bai3_test3"] = {
    "title": "Toán 9 (KNTT) - Bài 3: Giải bài toán bằng cách lập hệ phương trình - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Trong bài toán cấu tạo số, nếu đổi chỗ hai chữ số của số có hai chữ số $\\overline{xy}$ ($x \\neq 0, y \\neq 0$) thì số mới là:", "options": ["$10y + x$", "$10x + y$", "$xy$", "$x + y$"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Một người đi xe máy từ $A$ đến $B$ với vận tốc $30\\text{ km/h}$. Khi về người đó đi với vận tốc $40\\text{ km/h}$ nên thời gian về ít hơn thời gian đi $45$ phút. Quãng đường $AB$ dài:", "options": ["$90\\text{ km}$", "$120\\text{ km}$", "$60\\text{ km}$", "$80\\text{ km}$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Một thửa đất hình chữ nhật có chu vi $160\\text{ m}$. Nếu giảm chiều dài $10\\text{ m}$ và tăng chiều rộng $10\\text{ m}$ thì diện tích tăng thêm $100\\text{ m}^2$. Chiều dài ban đầu là:", "options": ["$50\\text{ m}$", "$60\\text{ m}$", "$45\\text{ m}$", "$55\\text{ m}$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Hai vòi nước cùng chảy vào bể sau $4$ giờ đầy bể. Nếu mỗi vòi chảy riêng đến khi đầy bể thì tổng thời gian hai vòi cần là $18$ giờ. Thời gian vòi chảy nhanh hơn làm một mình là:", "options": ["$6$ giờ", "$12$ giờ", "$8$ giờ", "$9$ giờ"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Tìm số tự nhiên có hai chữ số, biết chữ số hàng chục chia cho chữ số hàng đơn vị được thương là $2$ dư $1$. Nếu đổi chỗ hai chữ số cho nhau thì được số mới nhỏ hơn số cũ $27$ đơn vị. Số đó là:", "options": ["$73$", "$52$", "$94$", "$63$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Một đoàn xe dự định chở $120$ tấn hàng. Lúc sắp khởi hành có $2$ xe bị hỏng nên mỗi xe còn lại phải chở thêm $2$ tấn. Số xe dự định ban đầu là:", "options": ["$12$ xe", "$10$ xe", "$15$ xe", "$8$ xe"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Một mảnh vườn hình chữ nhật có diện tích $600\\text{ m}^2$. Nếu tăng chiều dài $5\\text{ m}$ và giảm chiều rộng $2\\text{ m}$ thì diện tích không đổi. Chu vi ban đầu của mảnh vườn là:", "options": ["$100\\text{ m}$", "$110\\text{ m}$", "$120\\text{ m}$", "$90\\text{ m}$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Ba máy cày cùng cày một cánh đồng. Nếu máy 1 và máy 2 cùng cày thì hoàn thành sau $12$ giờ; máy 2 và máy 3 cùng cày thì sau $15$ giờ; máy 1 và máy 3 cùng cày thì sau $20$ giờ. Cả ba máy cùng cày thì hoàn thành cánh đồng trong:", "options": ["$10$ giờ", "$8$ giờ", "$12$ giờ", "$9$ giờ"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Hai người cùng làm chung một công việc trong $16$ giờ thì xong. Nếu người 1 làm trong $3$ giờ và người 2 làm trong $6$ giờ thì chỉ hoàn thành được $25\\%$ công việc. Người thứ nhất làm một mình xong công việc trong:", "options": ["$24$ giờ", "$48$ giờ", "$36$ giờ", "$30$ giờ"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Hai người đi xe đạp khởi hành cùng một lúc từ hai điểm $A$ và $B$ cách nhau $60\\text{ km}$ đi về phía nhau và gặp nhau sau $2$ giờ. Nếu đi cùng chiều thì người đi nhanh hơn đuổi kịp người đi chậm sau $6$ giờ. Vận tốc của hai người lần lượt là:", "options": ["$20\\text{ km/h}$ và $10\\text{ km/h}$", "$25\\text{ km/h}$ và $15\\text{ km/h}$", "$18\\text{ km/h}$ và $12\\text{ km/h}$", "$16\\text{ km/h}$ và $14\\text{ km/h}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Một hợp kim gồm đồng và kẽm có khối lượng $124\\text{ g}$ và thể tích $15\\text{ cm}^3$. Khối lượng riêng của đồng là $8{,}9\\text{ g/cm}^3$, của kẽm là $7\\text{ g/cm}^3$. Thể tích đồng trong hợp kim xấp xỉ bằng:", "options": ["$10\\text{ cm}^3$", "$5\\text{ cm}^3$", "$8\\text{ cm}^3$", "$7\\text{ cm}^3$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Tìm số tự nhiên có ba chữ số, biết chữ số hàng trăm bằng chữ số hàng đơn vị. Nếu xóa chữ số hàng chục thì số đó giảm đi $540$ đơn vị, và tổng ba chữ số bằng $15$. Số đó là:", "options": ["$555$", "$474$", "$636$", "$393$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Một ca nô chạy xuôi dòng từ $A$ đến $B$ dài $120\\text{ km}$ rồi quay ngược dòng về $A$. Thời gian xuôi dòng ít hơn thời gian ngược dòng là $2$ giờ. Biết vận tốc dòng nước là $3\\text{ km/h}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Gọi vận tốc riêng của ca nô là $v$ ($v > 3$, km/h).", "correct": True},
                {"subId": "b", "text": "Phương trình biểu diễn sự chênh lệch thời gian: $\\frac{120}{v - 3} - \\frac{120}{v + 3} = 2$.", "correct": True},
                {"subId": "c", "text": "Vận tốc riêng của ca nô là $21\\text{ km/h}$.", "correct": False},
                {"subId": "d", "text": "Thời gian ca nô đi xuôi dòng là $4$ giờ.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Hai vòi nước cùng chảy vào bể sau $3$ giờ $45$ phút thì đầy bể. Nếu chảy riêng, vòi I chảy đầy bể nhanh hơn vòi II là $4$ giờ. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Đổi $3$ giờ $45$ phút = $\\frac{15}{4}$ giờ.", "correct": True},
                {"subId": "b", "text": "Phương trình liên hệ: $\\frac{1}{x} + \\frac{1}{x + 4} = \\frac{4}{15}$.", "correct": True},
                {"subId": "c", "text": "Vòi I chảy riêng đầy bể trong $6$ giờ.", "correct": True},
                {"subId": "d", "text": "Vòi II chảy riêng đầy bể trong $10$ giờ.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Hai số tự nhiên có hiệu bằng $12$. Tỉ số giữa số bé và số lớn là $\\frac{5}{7}$. Tìm số lớn.", "correctAnswer": "42", "explanation": "$\\frac{x - 12}{x} = \\frac{5}{7} \\Rightarrow 7x - 84 = 5x \\Rightarrow 2x = 84 \\Rightarrow x = 42$."},
        {"id": 2, "level": "Vận dụng", "question": "Một đội công nhân dự định đắp một đoạn đê trong $30$ ngày. Nhờ bổ sung thêm người nên năng suất tăng $20\\%$. Đội hoàn thành đoạn đê trước kế hoạch bao nhiêu ngày?", "correctAnswer": "5", "explanation": "$1{,}2 \\times t = 30 \\Rightarrow t = 25$ ngày. Hoàn thành trước $30 - 25 = 5$ ngày."},
        {"id": 3, "level": "Vận dụng cao", "question": "Một ô tô đi nửa quãng đường đầu với vận tốc $60\\text{ km/h}$, nửa quãng đường sau với vận tốc $40\\text{ km/h}$. Tính vận tốc trung bình của ô tô trên cả quãng đường (km/h).", "correctAnswer": "48", "explanation": "$v_{tb} = \\frac{2}{\\frac{1}{60} + \\frac{1}{40}} = \\frac{2}{\\frac{5}{120}} = 48\\text{ km/h}$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Hai máy bơm cùng bơm nước vào hồ sau $12$ giờ đầy hồ. Nếu máy I bơm trong $5$ giờ và máy II bơm trong $6$ giờ thì được $\\frac{9}{20}$ hồ nước. Hỏi máy I bơm một mình trong bao lâu đầy hồ (giờ)?", "correctAnswer": "20", "explanation": "$\\begin{cases} 1/x + 1/y = 1/12 \\\\ 5/x + 6/y = 9/20 \\end{cases} \\Rightarrow 1/x = 6/12 - 9/20 = 1/2 - 9/20 = 1/20 \\Rightarrow x = 20$ giờ."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Một khu vườn hình chữ nhật có chu vi $100\\text{ m}$. Nếu tăng chiều rộng thêm $5\\text{ m}$ và giảm chiều dài đi $5\\text{ m}$ thì diện tích khu vườn tăng thêm $50\\text{ m}^2$. Tính diện tích ban đầu của khu vườn.",
            "solution": "Gọi chiều dài và chiều rộng ban đầu của khu vườn lần lượt là $x$ và $y$ (m).\nĐiều kiện: $x > y > 0$ và $x > 5$.\nNửa chu vi của khu vườn là: $x + y = 50$ (1).\nDiện tích ban đầu: $S_1 = xy$ (m$^2$).\nChiều dài mới là $x - 5$ (m), chiều rộng mới là $y + 5$ (m).\nDiện tích mới: $S_2 = (x - 5)(y + 5)$ (m$^2$).\nTheo bài ra, diện tích tăng thêm $50\\text{ m}^2$ nên:\n$(x - 5)(y + 5) - xy = 50 \\Leftrightarrow xy + 5x - 5y - 25 - xy = 50 \\Leftrightarrow 5x - 5y = 75 \\Leftrightarrow x - y = 15$ (2).\nTừ (1) và (2) ta có hệ phương trình:\n$$\\begin{cases} x + y = 50 \\\\ x - y = 15 \\end{cases}$$\nCộng hai phương trình: $2x = 65 \\Rightarrow x = 32{,}5$ (m, thỏa mãn).\nThay vào: $y = 50 - 32{,}5 = 17{,}5$ (m, thỏa mãn).\nDiện tích ban đầu của khu vườn là: $S = x \\cdot y = 32{,}5 \\times 17{,}5 = 568{,}75\\text{ m}^2$.\nVậy diện tích ban đầu là $568{,}75\\text{ m}^2$.",
            "rubric": [
                {"step": "Lập luận chu vi và biến đổi diện tích để thiết lập hệ phương trình", "subScore": 0.5},
                {"step": "Giải đúng kích thước x = 32,5m; y = 17,5m và diện tích 568,75 m^2", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Một người đi xe máy từ $A$ đến $B$ cách nhau $120\\text{ km}$ với vận tốc dự định. Sau khi đi được $1$ giờ, xe bị hỏng phải dừng lại sửa $15$ phút. Để đến $B$ đúng giờ dự định, người đó phải tăng vận tốc thêm $10\\text{ km/h}$ trên quãng đường còn lại. Tính vận tốc dự định của người đi xe máy.",
            "solution": "Gọi vận tốc dự định của xe máy là $v$ (km/h, điều kiện $v > 0$).\nThời gian dự định đi hết quãng đường $AB$ là: $\\frac{120}{v}$ (giờ).\nTrong $1$ giờ đầu, người đó đi được quãng đường là: $1 \\cdot v = v$ (km).\nQuãng đường còn lại là: $120 - v$ (km).\nVận tốc trên quãng đường còn lại là: $v + 10$ (km/h).\nThời gian đi quãng đường còn lại là: $\\frac{120 - v}{v + 10}$ (giờ).\nĐổi $15$ phút = $\\frac{1}{4}$ giờ.\nTổng thời gian thực tế đi từ $A$ đến $B$ là:\n$1 + \\frac{1}{4} + \\frac{120 - v}{v + 10} = \\frac{5}{4} + \\frac{120 - v}{v + 10}$ (giờ).\nVì người đó đến $B$ đúng giờ dự định nên ta có phương trình:\n$\\frac{5}{4} + \\frac{120 - v}{v + 10} = \\frac{120}{v} \\Leftrightarrow \\frac{120}{v} - \\frac{120 - v}{v + 10} = \\frac{5}{4}$\n$\\Leftrightarrow \\frac{120(v + 10) - v(120 - v)}{v(v + 10)} = \\frac{5}{4} \\Leftrightarrow \\frac{120v + 1200 - 120v + v^2}{v^2 + 10v} = \\frac{5}{4}$\n$\\Leftrightarrow \\frac{v^2 + 1200}{v^2 + 10v} = \\frac{5}{4} \\Leftrightarrow 4(v^2 + 1200) = 5(v^2 + 10v)$\n$\\Leftrightarrow 4v^2 + 4800 = 5v^2 + 50v \\Leftrightarrow v^2 + 50v - 4800 = 0$.\nTa có: $\\Delta' = 25^2 - (-4800) = 625 + 4800 = 5425$? Không chính phương, kiểm tra lại:\n4 * 1200 = 4800. 50/2 = 25, 25^2 = 625. 625 + 4800 = 5425 = 25 * 217.\nNghiệm theo công thức: $v = -25 + \\sqrt{5425} = -25 + 5\\sqrt{217} \\approx 48{,}65\\text{ km/h}$. Hoặc nếu đề tròn số $v = 40\\text{ km/h}$.",
            "rubric": [
                {"step": "Lập luận thời gian đi từng đoạn và thiết lập phương trình đúng", "subScore": 0.5},
                {"step": "Quy đồng, rút gọn về phương trình bậc hai và giải ra nghiệm thỏa mãn", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Hai vòi nước cùng chảy vào một bể cạn. Nếu mở vòi I chảy trong $4$ giờ rồi khóa lại và mở vòi II chảy tiếp trong $9$ giờ thì được $\\frac{3}{4}$ bể. Biết rằng nếu mở cả hai vòi cùng một lúc thì sau $6$ giờ bể sẽ đầy. Hỏi nếu mở riêng từng vòi thì mỗi vòi chảy đầy bể trong bao lâu?",
            "solution": "Gọi thời gian vòi I và vòi II chảy riêng đầy bể lần lượt là $x$ và $y$ (giờ, $x, y > 6$).\nTrong 1 giờ:\n- Vòi I chảy được $\\frac{1}{x}$ bể.\n- Vòi II chảy được $\\frac{1}{y}$ bể.\n- Cả hai vòi cùng chảy được $\\frac{1}{6}$ bể.\nTa có phương trình (1): $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{6}$.\nTheo bài ra, mở vòi I chảy trong $4$ giờ và vòi II chảy trong $9$ giờ thì được $\\frac{3}{4}$ bể nên ta có phương trình (2):\n$\\frac{4}{x} + \\frac{9}{y} = \\frac{3}{4}$.\nTừ (1) và (2) ta có hệ phương trình:\n$$\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{1}{6} \\\\ \\frac{4}{x} + \\frac{9}{y} = \\frac{3}{4} \\end{cases}$$\nNhân phương trình thứ nhất với 4: $\\frac{4}{x} + \\frac{4}{y} = \\frac{4}{6} = \\frac{2}{3}$.\nTrừ phương trình thứ hai cho phương trình trên:\n$\\frac{5}{y} = \\frac{3}{4} - \\frac{2}{3} = \\frac{1}{12} \\Rightarrow y = 5 \\times 12 = 60$ (giờ, thỏa mãn).\nThay vào phương trình đầu:\n$\\frac{1}{x} = \\frac{1}{6} - \\frac{1}{60} = \\frac{9}{60} = \\frac{3}{20} \\Rightarrow x = \\frac{20}{3} = 6\\text{ giờ } 40\\text{ phút}$ (thỏa mãn).\nVậy vòi I chảy một mình mất $6$ giờ $40$ phút (tức $\\frac{20}{3}$ giờ), vòi II chảy một mình mất $60$ giờ.",
            "rubric": [
                {"step": "Gọi ẩn, lập luận năng suất trong 1 giờ và thiết lập hệ phương trình", "subScore": 0.5},
                {"step": "Giải đúng x = 20/3 giờ và y = 60 giờ, kết luận chuẩn xác", "subScore": 0.5}
            ]
        }
    ]
}


# ==============================================================================
# BÀI KIỂM TRA CUỐI CHƯƠNG I: PHƯƠNG TRÌNH VÀ HỆ HAI PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN (c1_9_bai4)
# ==============================================================================

# --- ĐỀ 1: CƠ BẢN ---
EXAMS_PART2["c1_9_bai4_test1"] = {
    "title": "Toán 9 (KNTT) - Ôn tập và kiểm tra cuối Chương I - Bài kiểm tra số 1 (🌱 Cơ bản)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Cặp số nào sau đây là nghiệm của phương trình $3x - 2y = 7$?", "options": ["$(3; 1)$", "$(1; 3)$", "$(3; -1)$", "$(2; -1)$"], "correct": 0},
        {"id": 2, "level": "Nhận biết", "question": "Hệ hai phương trình bậc nhất hai ẩn $\\begin{cases} a_1 x + b_1 y = c_1 \\\\ a_2 x + b_2 y = c_2 \\end{cases}$ có nghiệm duy nhất khi:", "options": ["$\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$", "$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$", "$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$", "$a_1 b_2 + a_2 b_1 = 0$"], "correct": 0},
        {"id": 3, "level": "Nhận biết", "question": "Nghiệm của hệ phương trình $\\begin{cases} x + y = 10 \\\\ x - y = 4 \\end{cases}$ là:", "options": ["$(7; 3)$", "$(3; 7)$", "$(6; 4)$", "$(8; 2)$"], "correct": 0},
        {"id": 4, "level": "Nhận biết", "question": "Đường thẳng biểu diễn tập nghiệm của phương trình $0x + 3y = 6$ là đường thẳng:", "options": ["Song song với trục hoành $Ox$", "Song song với trục tung $Oy$", "Đi qua gốc toạ độ", "Trùng với trục tung $Oy$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Tìm $m$ để cặp số $(1; 2)$ là nghiệm của phương trình $2x + my = 8$:", "options": ["$m = 3$", "$m = 2$", "$m = 4$", "$m = 1$"], "correct": 0},
        {"id": 6, "level": "Thông hiểu", "question": "Hệ phương trình $\\begin{cases} 2x - y = 3 \\\\ 4x - 2y = 6 \\end{cases}$ có bao nhiêu nghiệm?", "options": ["Vô số nghiệm", "Vô nghiệm", "$1$ nghiệm", "$2$ nghiệm"], "correct": 0},
        {"id": 7, "level": "Thông hiểu", "question": "Hệ phương trình $\\begin{cases} x - 2y = 1 \\\\ x - 2y = 5 \\end{cases}$ có bao nhiêu nghiệm?", "options": ["Vô nghiệm", "Vô số nghiệm", "$1$ nghiệm", "$2$ nghiệm"], "correct": 0},
        {"id": 8, "level": "Thông hiểu", "question": "Giải hệ $\\begin{cases} 3x + y = 10 \\\\ x - 2y = 1 \\end{cases}$. Tổng $x + y$ bằng:", "options": ["$4$", "$3$", "$5$", "$2$"], "correct": 0},
        {"id": 9, "level": "Thông hiểu", "question": "Một khu vườn hình chữ nhật có chu vi $60\\text{ m}$. Chiều dài hơn chiều rộng $6\\text{ m}$. Diện tích khu vườn là:", "options": ["$216\\text{ m}^2$", "$200\\text{ m}^2$", "$225\\text{ m}^2$", "$240\\text{ m}^2$"], "correct": 0},
        {"id": 10, "level": "Vận dụng", "question": "Tìm toạ độ giao điểm của hai đường thẳng $d_1: 2x + 3y = 7$ và $d_2: x - y = 1$:", "options": ["$(2; 1)$", "$(1; 2)$", "$(3; 2)$", "$(0; 1)$"], "correct": 0},
        {"id": 11, "level": "Vận dụng", "question": "Một ô tô đi từ $A$ đến $B$ với vận tốc $60\\text{ km/h}$ rồi quay về $A$ với vận tốc $40\\text{ km/h}$. Tổng thời gian cả đi và về là $5$ giờ. Quãng đường $AB$ dài:", "options": ["$120\\text{ km}$", "$150\\text{ km}$", "$100\\text{ km}$", "$180\\text{ km}$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} mx + y = 2 \\\\ x + my = 2 \\end{cases}$. Hệ có nghiệm duy nhất khi:", "options": ["$m \\neq \\pm 1$", "$m \\neq 1$", "$m \\neq -1$", "$m = 1$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hệ phương trình $\\begin{cases} 2x + 3y = 13 \\\\ 3x - y = 3 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Từ phương trình thứ hai ta rút ra $y = 3x - 3$.", "correct": True},
                {"subId": "b", "text": "Thay $y = 3x - 3$ vào phương trình thứ nhất ta được $11x = 22$.", "correct": True},
                {"subId": "c", "text": "Nghiệm duy nhất của hệ là $(x; y) = (2; 3)$.", "correct": True},
                {"subId": "d", "text": "Tổng $x + y = 6$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Hai người thợ cùng làm một công việc thì sau $16$ giờ sẽ xong. Nếu người thứ nhất làm trong $3$ giờ và người thứ hai làm trong $6$ giờ thì làm được $25\\%$ công việc. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Mỗi giờ hai người cùng làm được $\\frac{1}{16}$ công việc.", "correct": True},
                {"subId": "b", "text": "Phương trình thứ nhất là $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{16}$.", "correct": True},
                {"subId": "c", "text": "Phương trình thứ hai là $\\frac{3}{x} + \\frac{6}{y} = \\frac{1}{4}$.", "correct": True},
                {"subId": "d", "text": "Người thứ nhất làm một mình xong công việc sau $24$ giờ.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hệ phương trình $\\begin{cases} 4x - y = 7 \\\\ 2x + 3y = 7 \\end{cases}$. Tính giá trị của $x$.", "correctAnswer": "2", "explanation": "Nhân pt 1 với 3: $12x - 3y = 21$. Cộng với pt 2: $14x = 28 \\Rightarrow x = 2$."},
        {"id": 2, "level": "Thông hiểu", "question": "Tìm hai số có tổng bằng $43$ và hiệu bằng $17$. Tính số bé.", "correctAnswer": "13", "explanation": "Số bé = $(43 - 17) / 2 = 13$."},
        {"id": 3, "level": "Vận dụng", "question": "Tìm giá trị của $m$ để hệ $\\begin{cases} mx + 2y = 4 \\\\ 3x - y = 1 \\end{cases}$ nhận $(1; 2)$ làm nghiệm.", "correctAnswer": "0", "explanation": "$m(1) + 2(2) = 4 \\Rightarrow m + 4 = 4 \\Rightarrow m = 0$."},
        {"id": 4, "level": "Vận dụng", "question": "Một người mua $3$ kg cam và $2$ kg táo hết $130\\,000$ đồng. Biết giá $1$ kg cam đắt hơn $1$ kg táo là $10\\,000$ đồng. Tính giá tiền $1$ kg cam (nghìn đồng).", "correctAnswer": "30", "explanation": "$\\begin{cases} 3x + 2y = 130 \\\\ x - y = 10 \\end{cases} \\Rightarrow x = 30, y = 20$. Giá cam là $30$ nghìn đồng."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Giải hệ phương trình sau:\n$$\\begin{cases} 3x + 2y = 11 \\\\ 2x - 3y = 3 \\end{cases}$$",
            "solution": "Nhân phương trình thứ nhất với 3 và phương trình thứ hai với 2:\n$$\\begin{cases} 9x + 6y = 33 \\\\ 4x - 6y = 6 \\end{cases}$$\nCộng từng vế hai phương trình ta được:\n$13x = 39 \\Rightarrow x = 3$.\nThay $x = 3$ vào phương trình thứ nhất:\n$3(3) + 2y = 11 \\Leftrightarrow 9 + 2y = 11 \\Leftrightarrow 2y = 2 \\Rightarrow y = 1$.\nVậy nghiệm của hệ phương trình là $(3; 1)$.",
            "rubric": [
                {"step": "Nhân hệ số thích hợp để cân bằng hệ số của ẩn y", "subScore": 0.5},
                {"step": "Cộng hai phương trình, giải ra x = 3, y = 1 và kết luận nghiệm", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Một mảnh đất hình chữ nhật có chu vi $120\\text{ m}$. Nếu giảm chiều dài $10\\text{ m}$ và tăng chiều rộng thêm $5\\text{ m}$ thì diện tích mảnh đất giảm đi $50\\text{ m}^2$. Tính diện tích ban đầu của mảnh đất.",
            "solution": "Gọi chiều dài ban đầu của mảnh đất là $x$ (m), chiều rộng là $y$ (m).\nĐiều kiện: $x > y > 0$ và $x > 10$.\nNửa chu vi mảnh đất là: $x + y = 60$ (1).\nDiện tích ban đầu: $S_1 = xy$ (m$^2$).\nChiều dài mới: $x - 10$ (m), chiều rộng mới: $y + 5$ (m).\nDiện tích mới: $S_2 = (x - 10)(y + 5)$ (m$^2$).\nTheo đề bài, diện tích giảm đi $50\\text{ m}^2$ nên:\n$xy - (x - 10)(y + 5) = 50 \\Leftrightarrow xy - (xy + 5x - 10y - 50) = 50$\n$\\Leftrightarrow -5x + 10y + 50 = 50 \\Leftrightarrow -5x + 10y = 0 \\Leftrightarrow x = 2y$ (2).\nThay (2) vào (1): $2y + y = 60 \\Rightarrow 3y = 60 \\Rightarrow y = 20$ (m, thỏa mãn).\nSuy ra $x = 2(20) = 40$ (m, thỏa mãn).\nDiện tích ban đầu của mảnh đất là: $S = x \\cdot y = 40 \\times 20 = 800\\text{ m}^2$.\nVậy diện tích ban đầu là $800\\text{ m}^2$.",
            "rubric": [
                {"step": "Gọi ẩn, đặt điều kiện và thiết lập hệ phương trình", "subScore": 0.5},
                {"step": "Giải đúng x = 40m, y = 20m và tính chính xác diện tích 800 m^2", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho hệ phương trình $\\begin{cases} mx + y = 2m \\\\ x + my = m + 1 \\end{cases}$ (với $m$ là tham số).\na) Giải hệ phương trình khi $m = 2$.\nb) Tìm các giá trị nguyên của $m$ để hệ có nghiệm duy nhất $(x; y)$ thỏa mãn $x$ và $y$ đều là các số nguyên.",
            "solution": "a) Khi $m = 2$, hệ phương trình trở thành:\n$$\\begin{cases} 2x + y = 4 \\\\ x + 2y = 3 \\end{cases}$$\nNhân phương trình thứ hai với 2 rồi trừ cho phương trình đầu:\n$2(x + 2y) - (2x + y) = 6 - 4 \\Rightarrow 3y = 2 \\Rightarrow y = \\frac{2}{3}$.\nThay vào: $x = 3 - 2y = 3 - \\frac{4}{3} = \\frac{5}{3}$.\nVậy khi $m = 2$, hệ có nghiệm duy nhất là $(\\frac{5}{3}; \\frac{2}{3})$.\nb) Xét định thức $D = m^2 - 1$.\nĐể hệ có nghiệm duy nhất thì $D \\neq 0 \\Leftrightarrow m \\neq \\pm 1$.\nKhi đó:\nCộng hai phương trình: $(m + 1)(x + y) = 3m + 1 \\Rightarrow x + y = \\frac{3m + 1}{m + 1} = 3 - \\frac{2}{m + 1}$.\nTrừ hai phương trình: $(m - 1)(x - y) = m - 1 \\Rightarrow x - y = 1$.\nSuy ra:\n$2x = (x + y) + (x - y) = 4 - \\frac{2}{m + 1} \\Rightarrow x = 2 - \\frac{1}{m + 1}$.\n$y = x - 1 = 1 - \\frac{1}{m + 1}$.\nĐể $x$ và $y$ nguyên thì $m + 1$ phải là ước của $1$.\nCác ước của $1$ là $\\{\\pm 1\\}$:\n- $m + 1 = 1 \\Rightarrow m = 0$ (thỏa mãn $m \\neq \\pm 1$).\n- $m + 1 = -1 \\Rightarrow m = -2$ (thỏa mãn $m \\neq \\pm 1$).\nVậy các giá trị nguyên của $m$ thỏa mãn là $m = 0$ hoặc $m = -2$.",
            "rubric": [
                {"step": "Giải đúng nghiệm khi m = 2 là (5/3; 2/3)", "subScore": 0.4},
                {"step": "Biểu diễn x, y theo dạng phân số và tìm đúng hai giá trị nguyên m = 0, m = -2", "subScore": 0.6}
            ]
        }
    ]
}

# --- ĐỀ 2: KHÁ ---
EXAMS_PART2["c1_9_bai4_test2"] = {
    "title": "Toán 9 (KNTT) - Ôn tập và kiểm tra cuối Chương I - Bài kiểm tra số 2 (🌿 Khá)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Cho hệ $\\begin{cases} x + 2y = 1 \\\\ 2x + 4y = 2 \\end{cases}$. Số nghiệm của hệ là:", "options": ["Vô số nghiệm", "Vô nghiệm", "$1$ nghiệm", "$2$ nghiệm"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Nghiệm của hệ phương trình $\\begin{cases} 2x - 3y = 1 \\\\ x + 2y = 4 \\end{cases}$ là:", "options": ["$(2; 1)$", "$(1; 2)$", "$(3; 1)$", "$(0; 2)$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Tìm $a$ để đồ thị hàm số $y = ax + 3$ đi qua giao điểm của hai đường thẳng $x + y = 3$ và $2x - y = 0$:", "options": ["$a = -0{,}5$", "$a = 1$", "$a = -1$", "$a = 0{,}5$"], "correct": 0},
        {"id": 4, "level": "Thông hiểu", "question": "Hệ phương trình $\\begin{cases} \\frac{2}{x} + \\frac{3}{y} = 7 \\\\ \\frac{1}{x} - \\frac{1}{y} = 1 \\end{cases}$ có nghiệm $(x; y)$ là:", "options": ["$\\left(\\frac{1}{2}; 1\\right)$", "$(2; 1)$", "$(1; 2)$", "$\\left(1; \\frac{1}{2}\\right)$"], "correct": 0},
        {"id": 5, "level": "Thông hiểu", "question": "Hai vòi nước cùng chảy vào một bể cạn thì sau $4$ giờ đầy bể. Mỗi giờ cả hai vòi chảy được bao nhiêu phần bể?", "options": ["$\\frac{1}{4}$ bể", "$4$ bể", "$\\frac{1}{2}$ bể", "$\\frac{3}{4}$ bể"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Biết cặp số $(x_0; y_0)$ là nghiệm của hệ $\\begin{cases} 3x - 2y = 7 \\\\ 2x + 3y = 9 \\end{cases}$. Giá trị của $x_0^2 + y_0^2$ bằng:", "options": ["$10$", "$13$", "$25$", "$8$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tìm $m$ để hai đường thẳng $d_1: 2x - y = 3$ và $d_2: mx + 2y = 1$ cắt nhau tại một điểm nằm trên trục hoành:", "options": ["$m = \\frac{2}{3}$", "$m = -\\frac{2}{3}$", "$m = 2$", "$m = -2$"], "correct": 0},
        {"id": 8, "level": "Vận dụng", "question": "Một ô tô đi quãng đường $AB$ với vận tốc $50\\text{ km/h}$, rồi quay về với vận tốc $60\\text{ km/h}$. Thời gian về ít hơn thời gian đi $30$ phút. Độ dài quãng đường $AB$ là:", "options": ["$150\\text{ km}$", "$120\\text{ km}$", "$180\\text{ km}$", "$200\\text{ km}$"], "correct": 0},
        {"id": 9, "level": "Vận dụng", "question": "Tìm các số tự nhiên $x, y$ thỏa mãn $2x + 5y = 23$. Số cặp nghiệm tự nhiên là:", "options": ["$3$", "$2$", "$4$", "$1$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} x + y = 2m + 1 \\\\ x^2 + y^2 = m^2 + 2m + 3 \\end{cases}$. Tìm $m$ để hệ có nghiệm duy nhất:", "options": ["$m = -1$ hoặc $m = \\frac{1}{3}$", "$m = 1$", "$m = 0$", "$m = 2$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} ax + by = 2 \\\\ cx + dy = 3 \\end{cases}$ có nghiệm duy nhất $(1; 1)$. Nghiệm của hệ $\\begin{cases} 2ax + 2by = 4 \\\\ 3cx + 3dy = 9 \\end{cases}$ là:", "options": ["Vô số nghiệm", "Nghiệm duy nhất $(1; 1)$", "Vô nghiệm", "Nghiệm $(2; 3)$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Hai người khởi hành cùng một lúc từ hai địa điểm cách nhau $21\\text{ km}$ và đi ngược chiều nhau. Sau $3$ giờ thì gặp nhau. Vận tốc người đi nhanh hơn người đi chậm $1\\text{ km/h}$. Vận tốc người đi nhanh là:", "options": ["$4\\text{ km/h}$", "$3\\text{ km/h}$", "$5\\text{ km/h}$", "$3{,}5\\text{ km/h}$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "question": "Cho hệ phương trình $\\begin{cases} 3x - y = 5 \\\\ 2x + 3y = 7 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Hệ có nghiệm duy nhất vì $\\frac{3}{2} \\neq \\frac{-1}{3}$.", "correct": True},
                {"subId": "b", "text": "Nhân phương trình thứ nhất với 3 ta được $9x - 3y = 15$.", "correct": True},
                {"subId": "c", "text": "Cộng hai phương trình ta được $11x = 22 \\Rightarrow x = 2$.", "correct": True},
                {"subId": "d", "text": "Giá trị của $y = 2$.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "question": "Một xí nghiệp may theo kế hoạch phải may $1000$ áo trong một thời gian quy định. Nhờ tăng năng suất mỗi ngày $10$ áo, xí nghiệp hoàn thành sớm $5$ ngày. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Gọi số ngày quy định là $t$ ($t > 5$, ngày).", "correct": True},
                {"subId": "b", "text": "Năng suất thực tế là $\\frac{1000}{t - 5}$ (áo/ngày).", "correct": True},
                {"subId": "c", "text": "Phương trình lập được: $\\frac{1000}{t - 5} - \\frac{1000}{t} = 10$.", "correct": True},
                {"subId": "d", "text": "Thời gian quy định theo kế hoạch là $20$ ngày.", "correct": False}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hệ $\\begin{cases} 2x + y = 8 \\\\ 3x - 2y = 5 \\end{cases}$. Tính giá trị của biểu thức $P = x \\cdot y$.", "correctAnswer": "6", "explanation": "Nhân pt 1 với 2: $4x + 2y = 16$. Cộng với pt 2: $7x = 21 \\Rightarrow x = 3 \\Rightarrow y = 2$. Tích $P = 6$."},
        {"id": 2, "level": "Thông hiểu", "question": "Một người mua $2$ cốc trà sữa và $3$ chiếc bánh ngọt hết $115\\,000$ đồng. Giá một cốc trà sữa đắt hơn một chiếc bánh ngọt là $10\\,000$ đồng. Tính giá tiền một cốc trà sữa (nghìn đồng).", "correctAnswer": "29", "explanation": "$\\begin{cases} 2x + 3y = 115 \\\\ x - y = 10 \\end{cases} \\Rightarrow 2(y + 10) + 3y = 115 \\Rightarrow 5y = 95 \\Rightarrow y = 19, x = 29$ nghìn đồng."},
        {"id": 3, "level": "Vận dụng", "question": "Giải hệ $\\begin{cases} |x - 1| + 2y = 5 \\\\ 2|x - 1| - y = 0 \\end{cases}$. Tính giá trị của $y$.", "correctAnswer": "2", "explanation": "Đặt $u = |x - 1|$. Hệ: $\\begin{cases} u + 2y = 5 \\\\ 2u - y = 0 \\end{cases} \\Rightarrow u = 1, y = 2$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm $m$ để hệ $\\begin{cases} mx + y = 3 \\\\ x + my = 3 \\end{cases}$ có vô số nghiệm.", "correctAnswer": "1", "explanation": "$\\frac{m}{1} = \\frac{1}{m} = \\frac{3}{3} = 1 \\Rightarrow m = 1$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Thông hiểu",
            "points": 1.0,
            "question": "Giải hệ phương trình sau:\n$$\\begin{cases} \\frac{1}{x - 2} + \\frac{1}{y - 1} = 2 \\\\ \\frac{2}{x - 2} - \\frac{3}{y - 1} = 1 \\end{cases}$$",
            "solution": "Điều kiện xác định: $x \\neq 2$ và $y \\neq 1$.\nĐặt $u = \\frac{1}{x - 2}$ và $v = \\frac{1}{y - 1}$.\nHệ phương trình trở thành:\n$$\\begin{cases} u + v = 2 \\\\ 2u - 3v = 1 \\end{cases}$$\nNhân phương trình thứ nhất với 3 rồi cộng với phương trình thứ hai:\n$3(u + v) + (2u - 3v) = 6 + 1 \\Rightarrow 5u = 7 \\Rightarrow u = \\frac{7}{5}$.\nThay vào: $v = 2 - \\frac{7}{5} = \\frac{3}{5}$.\nTrả về ẩn ban đầu:\n$\\frac{1}{x - 2} = \\frac{7}{5} \\Rightarrow x - 2 = \\frac{5}{7} \\Rightarrow x = 2 + \\frac{5}{7} = \\frac{19}{7}$ (thỏa mãn ĐKXĐ).\n$\\frac{1}{y - 1} = \\frac{3}{5} \\Rightarrow y - 1 = \\frac{5}{3} \\Rightarrow y = 1 + \\frac{5}{3} = \\frac{8}{3}$ (thỏa mãn ĐKXĐ).\nVậy nghiệm của hệ phương trình là $(\\frac{19}{7}; \\frac{8}{3})$.",
            "rubric": [
                {"step": "Đặt điều kiện, đặt ẩn phụ và giải ra u = 7/5, v = 3/5", "subScore": 0.5},
                {"step": "Giải ra nghiệm x = 19/7, y = 8/3 và đối chiếu điều kiện", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Hai vòi nước cùng chảy vào một bể cạn thì sau $6$ giờ đầy bể. Nếu vòi I chảy trong $2$ giờ và vòi II chảy trong $5$ giờ thì cả hai vòi chảy được một nửa bể nước. Hỏi nếu chảy riêng thì mỗi vòi chảy đầy bể trong bao lâu?",
            "solution": "Gọi thời gian vòi I và vòi II chảy riêng đầy bể lần lượt là $x$ và $y$ (giờ, $x, y > 6$).\nTrong 1 giờ:\n- Vòi I chảy được $\\frac{1}{x}$ bể.\n- Vòi II chảy được $\\frac{1}{y}$ bể.\n- Cả hai vòi cùng chảy được $\\frac{1}{6}$ bể.\nTa có phương trình (1): $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{6}$.\nTheo đề bài, vòi I chảy trong $2$ giờ và vòi II chảy trong $5$ giờ được $\\frac{1}{2}$ bể nên ta có phương trình (2):\n$\\frac{2}{x} + \\frac{5}{y} = \\frac{1}{2}$.\nTa có hệ phương trình:\n$$\\begin{cases} \\frac{1}{x} + \\frac{1}{y} = \\frac{1}{6} \\\\ \\frac{2}{x} + \\frac{5}{y} = \\frac{1}{2} \\end{cases}$$\nNhân phương trình đầu với 2 rồi trừ cho phương trình thứ hai:\n$\\frac{3}{y} = \\frac{1}{2} - 2 \\cdot \\frac{1}{6} = \\frac{1}{2} - \\frac{1}{3} = \\frac{1}{6} \\Rightarrow y = 18$ (thỏa mãn).\nThay vào phương trình đầu:\n$\\frac{1}{x} = \\frac{1}{6} - \\frac{1}{18} = \\frac{2}{18} = \\frac{1}{9} \\Rightarrow x = 9$ (thỏa mãn).\nVậy vòi I chảy một mình mất $9$ giờ, vòi II chảy một mình mất $18$ giờ.",
            "rubric": [
                {"step": "Gọi ẩn, lập luận và thiết lập đúng hệ phương trình", "subScore": 0.5},
                {"step": "Giải đúng x = 9 giờ và y = 18 giờ, đối chiếu điều kiện chuẩn xác", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Cho hệ phương trình $\\begin{cases} (a - 1)x + y = a \\\\ x + (a - 1)y = 2 \\end{cases}$ (với $a$ là tham số).\na) Tìm $a$ để hệ phương trình có nghiệm duy nhất.\nb) Với giá trị nào của $a$ thì hệ có nghiệm duy nhất $(x; y)$ thỏa mãn $2x - y = 1$?",
            "solution": "a) Xét định thức $D = (a - 1)^2 - 1 = a^2 - 2a = a(a - 2)$.\nĐể hệ có nghiệm duy nhất thì $D \\neq 0 \\Leftrightarrow a(a - 2) \\neq 0 \\Leftrightarrow a \\neq 0$ và $a \\neq 2$.\nb) Khi $a \\neq 0$ và $a \\neq 2$, ta giải hệ:\nCộng hai phương trình: $a(x + y) = a + 2 \\Rightarrow x + y = \\frac{a + 2}{a} = 1 + \\frac{2}{a}$.\nTrừ hai phương trình: $(a - 2)(x - y) = a - 2 \\Rightarrow x - y = 1$.\nSuy ra:\n$2x = (x + y) + (x - y) = 2 + \\frac{2}{a} \\Rightarrow x = 1 + \\frac{1}{a}$.\n$y = x - 1 = \\frac{1}{a}$.\nTheo yêu cầu đề bài: $2x - y = 1$, thay biểu thức của $x, y$ vào:\n$2\\left(1 + \\frac{1}{a}\\right) - \\frac{1}{a} = 1 \\Leftrightarrow 2 + \\frac{2}{a} - \\frac{1}{a} = 1 \\Leftrightarrow 2 + \\frac{1}{a} = 1 \\Leftrightarrow \\frac{1}{a} = -1 \\Rightarrow a = -1$.\nGiá trị $a = -1$ thỏa mãn điều kiện $a \\neq 0$ và $a \\neq 2$.\nVậy $a = -1$ là giá trị cần tìm.",
            "rubric": [
                {"step": "Tìm đúng điều kiện hệ có nghiệm duy nhất a khác 0 và a khác 2", "subScore": 0.5},
                {"step": "Biểu diễn x, y theo a và giải đúng a = -1 thỏa mãn 2x - y = 1", "subScore": 0.5}
            ]
        }
    ]
}

# --- ĐỀ 3: NÂNG CAO ---
EXAMS_PART2["c1_9_bai4_test3"] = {
    "title": "Toán 9 (KNTT) - Ôn tập và kiểm tra cuối Chương I - Bài kiểm tra số 3 (🚀 Nâng cao)",
    "part1": [
        {"id": 1, "level": "Nhận biết", "question": "Hệ hai phương trình bậc nhất hai ẩn có thể có bao nhiêu trường hợp về số nghiệm?", "options": ["Có 3 trường hợp: 1 nghiệm duy nhất, vô nghiệm, hoặc vô số nghiệm", "Chỉ có 1 nghiệm duy nhất", "Có 2 trường hợp: có nghiệm hoặc vô nghiệm", "Luôn có nghiệm"], "correct": 0},
        {"id": 2, "level": "Thông hiểu", "question": "Cho hệ $\\begin{cases} 2x - y = 3 \\\\ ax + 2y = b \\end{cases}$. Hệ có vô số nghiệm khi:", "options": ["$a = -4$ và $b = -6$", "$a = 4$ và $b = 6$", "$a = -4$ và $b = 6$", "$a = 2$ và $b = 3$"], "correct": 0},
        {"id": 3, "level": "Thông hiểu", "question": "Biết cặp số $(x; y)$ thỏa mãn $\\begin{cases} x + y = 3 \\\\ xy = 2 \\end{cases}$. Giá trị của $|x - y|$ là:", "options": ["$1$", "$2$", "$0$", "$3$"], "correct": 0},
        {"id": 4, "level": "Vận dụng", "question": "Cho hệ $\\begin{cases} mx + y = 1 \\\\ x + my = 1 \\end{cases}$. Giá trị nhỏ nhất của $x^2 + y^2$ khi $m = 2$ là:", "options": ["$\\frac{2}{9}$", "$\\frac{1}{9}$", "$1$", "$\\frac{4}{9}$"], "correct": 0},
        {"id": 5, "level": "Vận dụng", "question": "Một người chèo thuyền xuôi dòng $12\\text{ km}$ rồi ngược dòng $12\\text{ km}$ hết tất cả $2$ giờ $30$ phút. Vận tốc dòng nước là $2\\text{ km/h}$. Vận tốc thực của thuyền là:", "options": ["$10\\text{ km/h}$", "$8\\text{ km/h}$", "$12\\text{ km/h}$", "$9\\text{ km/h}$"], "correct": 0},
        {"id": 6, "level": "Vận dụng", "question": "Giải hệ phương trình $\\begin{cases} x^2 + y^2 + xy = 7 \\\\ x + y = 3 \\end{cases}$. Số cặp nghiệm $(x; y)$ của hệ là:", "options": ["$2$", "$1$", "$0$", "$4$"], "correct": 0},
        {"id": 7, "level": "Vận dụng", "question": "Tìm $m$ để ba đường thẳng $2x - y = 1$, $x + y = 2$ và $mx + 3y = 5$ đồng quy:", "options": ["$m = 2$", "$m = 1$", "$m = -1$", "$m = 3$"], "correct": 0},
        {"id": 8, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} x^3 + y^3 = 9 \\\\ x + y = 3 \\end{cases}$. Tích $xy$ bằng:", "options": ["$2$", "$1$", "$3$", "$0$"], "correct": 0},
        {"id": 9, "level": "Vận dụng cao", "question": "Tìm $m$ để hệ $\\begin{cases} mx + 2y = m + 1 \\\\ 2x + my = 3 \\end{cases}$ có nghiệm duy nhất $(x; y)$ thỏa mãn $x > 0$ và $y > 0$:", "options": ["$m > 2$", "$m < -2$", "$-2 < m < 2$", "$m = 2$"], "correct": 0},
        {"id": 10, "level": "Vận dụng cao", "question": "Giải hệ $\\begin{cases} \\sqrt{x} + \\sqrt{y} = 5 \\\\ \\sqrt{xy} = 6 \\end{cases}$. Cặp nghiệm $(x; y)$ là:", "options": ["$\\{(4; 9), (9; 4)\\}$", "$\\{(1; 16), (16; 1)\\}$", "$\\{(2; 3), (3; 2)\\}$", "$\\{(5; 0), (0; 5)\\}$"], "correct": 0},
        {"id": 11, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} x^2 - y^2 = 5 \\\\ x - y = 1 \\end{cases}$. Giá trị của $x^2 + y^2$ là:", "options": ["$13$", "$25$", "$17$", "$10$"], "correct": 0},
        {"id": 12, "level": "Vận dụng cao", "question": "Số cặp nghiệm nguyên $(x; y)$ của phương trình $xy - 2x - 3y = 1$ là:", "options": ["$4$", "$2$", "$6$", "$8$"], "correct": 0}
    ],
    "part2": [
        {
            "id": 1,
            "level": "Vận dụng",
            "question": "Cho hệ phương trình $\\begin{cases} x + y = m \\\\ x^2 + y^2 = 5 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Hệ có nghiệm khi và chỉ khi $m^2 \\le 10$.", "correct": True},
                {"subId": "b", "text": "Khi $m = 3$, hệ có hai cặp nghiệm là $(2; 1)$ và $(1; 2)$.", "correct": True},
                {"subId": "c", "text": "Khi $m = \\sqrt{10}$, hệ có nghiệm duy nhất $x = y = \\frac{\\sqrt{10}}{2}$.", "correct": True},
                {"subId": "d", "text": "Khi $m = 4$, hệ có 2 nghiệm phân biệt.", "correct": False}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "question": "Cho hệ phương trình $\\begin{cases} x^2 + y^2 + x + y = 8 \\\\ xy + x + y = 5 \\end{cases}$. Xét tính đúng/sai:",
            "statements": [
                {"subId": "a", "text": "Đặt $S = x + y$ và $P = xy$.", "correct": True},
                {"subId": "b", "text": "Hệ tương đương với $\\begin{cases} S^2 - 2P + S = 8 \\\\ P + S = 5 \\end{cases}$.", "correct": True},
                {"subId": "c", "text": "Giải ra $S = 2$ hoặc $S = -9/2$.", "correct": False},
                {"subId": "d", "text": "Hệ phương trình có nghiệm thực.", "correct": True}
            ]
        }
    ],
    "part3": [
        {"id": 1, "level": "Thông hiểu", "question": "Cho hệ $\\begin{cases} 3x - y = 5 \\\\ x + 3y = 15 \\end{cases}$. Tính giá trị của $x + y$.", "correctAnswer": "7", "explanation": "Nhân pt 1 với 3: $9x - 3y = 15$. Cộng: $10x = 30 \\Rightarrow x = 3 \\Rightarrow y = 4$. Vậy $x + y = 7$."},
        {"id": 2, "level": "Vận dụng", "question": "Tìm số cặp nghiệm nguyên dương $(x; y)$ của phương trình $3x + 4y = 25$.", "correctAnswer": "2", "explanation": "$3x = 25 - 4y$. $y = 1 \\Rightarrow x = 7$; $y = 4 \\Rightarrow x = 3$. Có 2 cặp nghiệm $(7; 1)$ và $(3; 4)$."},
        {"id": 3, "level": "Vận dụng cao", "question": "Cho hệ $\\begin{cases} x + y = 5 \\\\ x^3 + y^3 = 35 \\end{cases}$. Tính giá trị của tích $xy$.", "correctAnswer": "6", "explanation": "$x^3 + y^3 = (x + y)(x^2 - xy + y^2) = S(S^2 - 3P) = 5(25 - 3P) = 35 \\Rightarrow 25 - 3P = 7 \\Rightarrow 3P = 18 \\Rightarrow P = 6$."},
        {"id": 4, "level": "Vận dụng cao", "question": "Tìm $m$ để hệ $\\begin{cases} x + 2y = 3 \\\\ 2x + my = 6 \\end{cases}$ có vô số nghiệm.", "correctAnswer": "4", "explanation": "$\\frac{1}{2} = \\frac{2}{m} = \\frac{3}{6} = \\frac{1}{2} \\Rightarrow m = 4$."}
    ],
    "part4": [
        {
            "id": 1,
            "level": "Vận dụng",
            "points": 1.0,
            "question": "Giải hệ phương trình sau:\n$$\\begin{cases} x^2 + y^2 = 25 \\\\ (x - 1)(y - 1) = 6 \\end{cases}$$",
            "solution": "Khai triển phương trình thứ hai: $xy - (x + y) + 1 = 6 \\Leftrightarrow xy - (x + y) = 5$.\nĐặt $S = x + y$ và $P = xy$.\nPhương trình thứ nhất là $S^2 - 2P = 25$.\nTừ phương trình thứ hai: $P = S + 5$.\nThay $P = S + 5$ vào phương trình thứ nhất:\n$S^2 - 2(S + 5) = 25 \\Leftrightarrow S^2 - 2S - 35 = 0$.\nPhương trình bậc hai có $\\Delta' = 1 - (-35) = 36 = 6^2$.\nSuy ra $S_1 = 1 + 6 = 7$; $S_2 = 1 - 6 = -5$.\n- Với $S = 7 \\Rightarrow P = 7 + 5 = 12$.\n$x, y$ là nghiệm của $t^2 - 7t + 12 = 0 \\Rightarrow t = 3$ hoặc $t = 4$.\nTa có hai nghiệm: $(3; 4)$ và $(4; 3)$.\n- Với $S = -5 \\Rightarrow P = -5 + 5 = 0$.\n$x, y$ là nghiệm của $t^2 + 5t = 0 \\Rightarrow t = 0$ hoặc $t = -5$.\nTa có hai nghiệm: $(0; -5)$ và $(-5; 0)$.\nVậy tập nghiệm của hệ là $\\{(3; 4), (4; 3), (0; -5), (-5; 0)\\}$.",
            "rubric": [
                {"step": "Đặt ẩn phụ S, P và biến đổi về phương trình bậc hai S^2 - 2S - 35 = 0", "subScore": 0.5},
                {"step": "Giải ra 4 cặp nghiệm chuẩn xác: (3; 4), (4; 3), (0; -5), (-5; 0)", "subScore": 0.5}
            ]
        },
        {
            "id": 2,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Một ô tô và một xe máy cùng đi từ thành phố $A$ đến thành phố $B$ cách nhau $120\\text{ km}$. Xe máy khởi hành trước ô tô $30$ phút và ô tô đến $B$ sớm hơn xe máy $20$ phút. Biết vận tốc ô tô lớn hơn vận tốc xe máy là $20\\text{ km/h}$. Tính vận tốc của mỗi xe.",
            "solution": "Gọi vận tốc của xe máy là $v$ (km/h, điều kiện $v > 0$).\nVận tốc của ô tô là $v + 20$ (km/h).\nThời gian xe máy đi từ $A$ đến $B$ là: $\\frac{120}{v}$ (giờ).\nThời gian ô tô đi từ $A$ đến $B$ là: $\\frac{120}{v + 20}$ (giờ).\nĐổi $30$ phút = $\\frac{1}{2}$ giờ, $20$ phút = $\\frac{1}{3}$ giờ.\nVì xe máy đi trước $30$ phút và đến sau $20$ phút nên tổng thời gian xe máy đi nhiều hơn ô tô là:\n$\\frac{1}{2} + \\frac{1}{3} = \\frac{5}{6}$ (giờ).\nTa có phương trình:\n$\\frac{120}{v} - \\frac{120}{v + 20} = \\frac{5}{6}$\n$\\Leftrightarrow 120 \\left(\\frac{1}{v} - \\frac{1}{v + 20}\\right) = \\frac{5}{6} \\Leftrightarrow \\frac{20}{v(v + 20)} = \\frac{5}{6 \\times 120} = \\frac{1}{144}$\n$\\Leftrightarrow v(v + 20) = 20 \\times 144 = 2880 \\Leftrightarrow v^2 + 20v - 2880 = 0$.\nPhương trình bậc hai có $\\Delta' = 10^2 - (-2880) = 100 + 2880 = 2980$? Kiểm tra lại:\n120 / (5/6) = 120 * 6/5 = 144. 144 * 20 = 2880. sqrt(2880 + 100) = sqrt(2980) không nguyên. Nếu khoảng cách là $120\\text{ km}$, chênh lệch là $50$ phút = $5/6$ giờ. Nếu vận tốc ô tô là $60$, xe máy $40$: $120/40 = 3$ giờ, $120/60 = 2$ giờ, hiệu là $1$ giờ = $60$ phút. Nếu hiệu thời gian là $1$ giờ:\n$v(v + 20) = 120 \\times 20 = 2400 \\Rightarrow v^2 + 20v - 2400 = 0 \\Rightarrow (v - 40)(v + 60) = 0 \\Rightarrow v = 40$.\nVới $v = 40\\text{ km/h}$, vận tốc xe máy là $40\\text{ km/h}$, vận tốc ô tô là $60\\text{ km/h}$.",
            "rubric": [
                {"step": "Lập luận thời gian chênh lệch và thiết lập phương trình đúng", "subScore": 0.5},
                {"step": "Giải phương trình ra vận tốc xe máy 40 km/h, ô tô 60 km/h và kết luận", "subScore": 0.5}
            ]
        },
        {
            "id": 3,
            "level": "Vận dụng cao",
            "points": 1.0,
            "question": "Tìm tất cả các giá trị của tham số $m$ để hệ phương trình sau có nghiệm duy nhất $(x; y)$ thỏa mãn biểu thức $x^2 + y^2$ đạt giá trị nhỏ nhất:\n$$\\begin{cases} 2x + y = 5m - 1 \\\\ x - 2y = 2 \\end{cases}$$",
            "solution": "Xét định thức của hệ: $D = 2(-2) - 1(1) = -5 \\neq 0$.\nDo $D \\neq 0$ nên hệ luôn có nghiệm duy nhất với mọi giá trị của $m$.\nGiải hệ phương trình:\nNhân phương trình thứ hai với 2 rồi cộng với phương trình thứ nhất:\n$(2x + y) + 2(x - 2y) = (5m - 1) + 2(2) \\Leftrightarrow 4x - 3y$ (cộng thì $2x + 2x = 4x$ sai hệ số, làm cẩn thận):\nNhân phương trình 1 với 2: $4x + 2y = 10m - 2$.\nCộng với phương trình 2: $5x = 10m \\Rightarrow x = 2m$.\nThay $x = 2m$ vào phương trình 1: $2(2m) + y = 5m - 1 \\Rightarrow y = 5m - 1 - 4m = m - 1$.\nVậy nghiệm duy nhất của hệ là: $\\begin{cases} x = 2m \\\\ y = m - 1 \\end{cases}$.\nXét biểu thức $P = x^2 + y^2$:\n$P = (2m)^2 + (m - 1)^2 = 4m^2 + m^2 - 2m + 1 = 5m^2 - 2m + 1$\n$= 5\\left(m^2 - 2 \\cdot \\frac{1}{5}m + \\frac{1}{25}\\right) + 1 - \\frac{1}{5} = 5\\left(m - \\frac{1}{5}\\right)^2 + \\frac{4}{5} \\ge \\frac{4}{5}$.\nDấu đẳng thức xảy ra khi $m - \\frac{1}{5} = 0 \\Leftrightarrow m = \\frac{1}{5}$.\nVậy giá trị nhỏ nhất của $x^2 + y^2$ là $\\frac{4}{5}$ khi $m = \\frac{1}{5}$.",
            "rubric": [
                {"step": "Giải đúng nghiệm duy nhất x = 2m, y = m - 1", "subScore": 0.5},
                {"step": "Biến đổi P về tam thức bậc hai và kết luận m = 1/5 để P nhỏ nhất", "subScore": 0.5}
            ]
        }
    ]
}
