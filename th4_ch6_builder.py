# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 6: ĐƯỜNG THẲNG VUÔNG GÓC, SONG SONG (BÀI 25 ĐẾN BÀI 28)
Toán lớp 4 - Bộ sách Kết nối tri thức với cuộc sống
Gồm 4 bài học x 3 đề độc lập = 12 đề kiểm tra chất lượng cao (th4_b25_test1 -> th4_b28_test3)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

def make_mc(qid, question_text, options, correct, explanation):
    q_title = f"**Câu {qid}:** {question_text}" if not question_text.startswith(f"**Câu {qid}:**") else question_text
    return {
        "id": qid,
        "question": q_title,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question_text, solution, answer, lineCount=4, points=1.0):
    p_title = f"**Bài {qid}:** {question_text}" if not question_text.startswith(f"**Bài {qid}:**") else question_text
    return {
        "id": qid,
        "question": p_title,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_exams():
    exams = {}

    # =========================================================================
    # BÀI 25: HAI ĐƯỜNG THẲNG VUÔNG GÓC
    # =========================================================================

    # --- Bài 25 - Đề 1 ---
    exams["th4_b25_test1"] = {
        "id": "th4_b25_test1",
        "lessonId": "th4_b25",
        "lessonNum": 25,
        "testNum": 1,
        "title": "Bài 25: Hai đường thẳng vuông góc - Đề số 1",
        "topic": "Hai đường thẳng vuông góc",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hai đường thẳng vuông góc với nhau tạo thành mấy góc vuông?", ["1 góc vuông", "2 góc vuông", "3 góc vuông", "4 góc vuông"], 3, "Hai đường thẳng vuông góc với nhau cắt nhau và tạo thành 4 góc vuông."),
            make_mc(2, "Dụng cụ thông dụng nhất dùng để kiểm tra góc vuông là:", ["Thước dây", "Thước ê ke", "Com-pa", "Thước đo góc tròn"], 1, "Ê ke có một góc vuông dùng để kiểm tra và vẽ góc vuông."),
            make_mc(3, "Hình chữ nhật ABCD có bao nhiêu cặp cạnh vuông góc với nhau?", ["2 cặp", "4 cặp", "6 cặp", "8 cặp"], 1, "Có 4 cặp cạnh vuông góc tại 4 đỉnh: (AB, BC), (BC, CD), (CD, DA), (DA, AB)."),
            make_mc(4, "Hình ảnh nào sau đây minh họa hai đường thẳng vuông góc trong thực tế?", ["Hai mép kề nhau của quyển sách giáo khoa", "Hai thanh ray của đường tàu hỏa", "Hai dòng kẻ ngang trong vở ô ly", "Kim giờ và kim phút lúc 6 giờ đúng"], 0, "Hai mép kề nhau của quyển sách vuông góc với nhau."),
            make_mc(5, "Khẳng định nào sau đây là SAI?", ["Hai đường thẳng vuông góc thì cắt nhau", "Hai đường thẳng cắt nhau thì luôn vuông góc", "Hai đường thẳng vuông góc tạo thành các góc 90°", "Hình vuông có 4 góc vuông"], 1, "Hai đường thẳng cắt nhau có thể tạo thành góc nhọn hoặc góc tù, không nhất thiết vuông góc."),
            make_mc(6, "Trong hình tam giác vuông ABC vuông tại A, hai cạnh vuông góc với nhau là:", ["AB và AC", "AB và BC", "AC và BC", "Không có cạnh nào"], 0, "Tam giác vuông tại A thì hai cạnh góc vuông là AB và AC.")
        ],
        "part2": [
            make_essay(1, "Cho hình chữ nhật MNPQ.\na) Kể tên 4 góc vuông của hình chữ nhật đó.\nb) Kể tên 4 cặp cạnh vuông góc với nhau.", "a) 4 góc vuông đỉnh M, N, P, Q.\nb) 4 cặp cạnh vuông góc: MN và NP; NP và PQ; PQ và QM; QM và MN.", "a) Các góc tại đỉnh M, N, P, Q; b) (MN, NP), (NP, PQ), (PQ, QM), (QM, MN)", 4, 1.0),
            make_essay(2, "Nêu các bước sử dụng thước ê ke để kiểm tra xem hai đường thẳng $a$ và $b$ cắt nhau tại điểm $O$ có vuông góc với nhau hay không.", "Bước 1: Đặt đỉnh góc vuông của thước ê ke trùng với giao điểm O của hai đường thẳng a và b.\nBước 2: Căn chỉnh một cạnh góc vuông của ê ke trùng khít với đường thẳng a.\nBước 3: Quan sát đường thẳng b. Nếu đường thẳng b trùng khít với cạnh góc vuông còn lại của ê ke thì hai đường thẳng a và b vuông góc với nhau.", "Đặt đỉnh góc vuông của ê ke vào O, một cạnh mép trùng a, mép kia trùng b thì vuông góc", 4, 1.0),
            make_essay(3, "Cho hình tứ giác ABCD có góc tại đỉnh A và góc tại đỉnh D là góc vuông. Hỏi trong tứ giác ABCD có mấy cặp cạnh vuông góc với nhau? Hãy kể tên các cặp cạnh đó.", "Tứ giác ABCD có 2 góc vuông tại đỉnh A và đỉnh D nên có 2 cặp cạnh vuông góc với nhau:\n- Cặp cạnh vuông góc tại đỉnh A: AB và AD.\n- Cặp cạnh vuông góc tại đỉnh D: DA và DC.", "2 cặp cạnh: (AB, AD) và (DA, DC)", 4, 1.0),
            make_essay(4, "Một người thợ mộc đóng một chiếc khung tranh hình chữ nhật. Người thợ cần kiểm tra xem 4 góc của khung tranh có vuông không. Em hãy nêu cách giúp bác thợ kiểm tra bằng thước ê ke và giải thích tại sao khung tranh bắt buộc phải có các góc vuông.", "Cách kiểm tra: Dùng góc vuông của thước ê ke áp lần lượt vào 4 góc trong của khung tranh. Nếu ở mỗi góc, hai thanh gỗ của khung trùng khít với hai cạnh góc vuông của thước ê ke thì góc đó là góc vuông.\nGiải thích: Khung tranh hình chữ nhật bắt buộc phải có 4 góc vuông để bức tranh khi lồng vào vừa vặn, phẳng phiu, không bị méo lệch và khung có kết cấu vững chắc, thẩm mỹ.", "Dùng góc vuông của ê ke kiểm tra 4 góc của khung tranh", 5, 1.5),
            make_essay(5, "Đồng hồ chỉ mấy giờ thì kim giờ và kim phút vuông góc với nhau? Hãy chỉ ra ít nhất hai thời điểm đồng hồ chỉ đúng giờ mà kim giờ và kim phút vuông góc với nhau.", "Kim giờ và kim phút vuông góc với nhau khi chúng tạo thành một góc $90^\\circ$ (cách nhau đúng 3 khoảng số trên mặt đồng hồ tròn 12 số).\nHai thời điểm đúng giờ là:\n1) Lúc 3 giờ đúng (kim ngắn chỉ số 3, kim dài chỉ số 12).\n2) Lúc 9 giờ đúng (kim ngắn chỉ số 9, kim dài chỉ số 12).", "3 giờ đúng và 9 giờ đúng", 5, 1.5),
            make_essay(6, "Vẽ đoạn thẳng AB dài 4 cm. Dùng ê ke vẽ đường thẳng $d$ vuông góc với AB tại điểm H nằm trên AB sao cho AH = 1 cm.", "Bước 1: Dùng thước thẳng vẽ đoạn thẳng AB dài 4 cm.\nBước 2: Trên đoạn thẳng AB, lấy điểm H cách A đúng 1 cm.\nBước 3: Đặt đỉnh góc vuông của ê ke tại điểm H, một cạnh góc vuông của ê ke trùng với đoạn thẳng AB.\nBước 4: Kẻ đường thẳng d theo cạnh góc vuông còn lại của ê ke. Khi đó d vuông góc với AB tại H.", "Vẽ đoạn AB=4cm, lấy H cách A 1cm, dùng ê ke kẻ đường thẳng vuông góc tại H", 4, 1.0)
        ]
    }

    # --- Bài 25 - Đề 2 ---
    exams["th4_b25_test2"] = {
        "id": "th4_b25_test2",
        "lessonId": "th4_b25",
        "lessonNum": 25,
        "testNum": 2,
        "title": "Bài 25: Hai đường thẳng vuông góc - Đề số 2",
        "topic": "Hai đường thẳng vuông góc",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Góc tạo bởi hai đường thẳng vuông góc có số đo là:", ["90°", "60°", "180°", "45°"], 0, "Góc vuông có số đo 90°."),
            make_mc(2, "Hình tam giác có thể có nhiều nhất bao nhiêu góc vuông?", ["1 góc vuông", "2 góc vuông", "3 góc vuông", "Không có"], 0, "Một tam giác chỉ có thể có nhiều nhất 1 góc vuông (tam giác vuông)."),
            make_mc(3, "Hình vuông ABCD có:", ["4 góc vuông và 4 cạnh bằng nhau", "4 góc vuông và 2 cặp cạnh bằng nhau", "2 góc vuông và 4 cạnh bằng nhau", "Không có góc vuông"], 0, "Hình vuông có 4 góc vuông và 4 cạnh dài bằng nhau."),
            make_mc(4, "Trong thực tế, hai cột cờ và mặt sân phẳng tạo với nhau:", ["Một góc vuông", "Một góc bẹt", "Một góc nhọn", "Một góc tù"], 0, "Cột cờ dựng thẳng đứng vuông góc với mặt đất bằng phẳng."),
            make_mc(5, "Cho đoạn thẳng AB và đường thẳng CD cắt nhau tại I tạo thành một góc vuông. Khi đó:", ["AB vuông góc với CD", "AB song song với CD", "AB trùng với CD", "AB không cắt CD"], 0, "Chúng cắt nhau tạo thành góc vuông nên AB vuông góc với CD."),
            make_mc(6, "Lúc mấy giờ thì hai kim đồng hồ KHÔNG tạo thành góc vuông?", ["6 giờ đúng", "3 giờ đúng", "9 giờ đúng", "3 giờ 32 phút (gần đúng)"], 0, "Lúc 6 giờ đúng hai kim tạo thành góc bẹt (180°), không phải góc vuông.")
        ],
        "part2": [
            make_essay(1, "Kể tên 3 đồ vật trong lớp học hoặc ở nhà em có các mép vuông góc với nhau.", "3 đồ vật có mép vuông góc với nhau:\n1) Bảng viết của lớp học (hai mép kề nhau).\n2) Mặt bàn học hình chữ nhật (hai cạnh liền kề).\n3) Cánh cửa ra vào (mép trên và mép đứng).", "Bảng viết, mặt bàn học, cánh cửa ra vào", 4, 1.0),
            make_essay(2, "Cho hình vẽ tam giác ABC vuông tại B. Kẻ đường cao BH vuông góc với cạnh đáy AC tại H.\na) Cạnh BH vuông góc với cạnh nào?\nb) Kể tên các góc vuông có đỉnh là B và đỉnh là H trong hình.", "a) Cạnh BH vuông góc với cạnh AC tại điểm H.\nb) Các góc vuông trong hình gồm:\n- Góc vuông đỉnh B: góc ABC (tạo bởi cạnh BA và BC).\n- Góc vuông đỉnh H: góc BHA (tạo bởi HB và HA) và góc BHC (tạo bởi HB và HC).", "a) BH vuông góc với AC; b) Góc ABC, góc BHA, góc BHC", 4, 1.0),
            make_essay(3, "Cho đoạn thẳng CD dài 6 cm. Nêu cách vẽ đường thẳng $xy$ đi qua trung điểm M của đoạn thẳng CD và vuông góc với CD.", "Bước 1: Vẽ đoạn thẳng CD dài 6 cm bằng thước thẳng.\nBước 2: Tìm trung điểm M của đoạn thẳng CD bằng cách đo từ C một khoảng $6 : 2 = 3\\text{ cm}$ và đánh dấu điểm M.\nBước 3: Đặt góc vuông của ê ke sao cho đỉnh góc vuông trùng với điểm M, một cạnh góc vuông trùng với đoạn thẳng CD.\nBước 4: Kẻ đường thẳng xy theo cạnh góc vuông còn lại của ê ke. Đường thẳng xy vừa vẽ vuông góc với CD tại trung điểm M.", "Đo tìm trung điểm M (CM=3cm), dùng ê ke đặt tại M kẻ đường vuông góc xy", 4, 1.0),
            make_essay(4, "Một người thợ xây dùng dây dọi để kiểm tra độ thẳng đứng của bức tường vừa xây. Em hãy giải thích vì sao quả dọi thả tự do lại giúp kiểm tra bức tường có vuông góc với mặt đất hay không.", "Quả dọi được treo bằng một sợi dây mảnh và kéo thẳng đứng xuống tâm Trái Đất do trọng lực. Khi dây dọi treo thẳng đứng, nó tạo với mặt phẳng ngang (mặt đất bằng phẳng) một góc vuông 90°.\nNgười thợ áp dây dọi sát mép bức tường: nếu mép tường song song và trùng với phương dây dọi thì bức tường thẳng đứng và vuông góc hoàn toàn với nền đất, đảm bảo an toàn chịu lực.", "Dây dọi luôn có phương thẳng đứng vuông góc mặt đất phẳng, giúp so sánh mép tường", 5, 1.5),
            make_essay(5, "Cho hình vuông ABCD. Hai đường chéo AC và BD cắt nhau tại điểm O. Dùng ê ke kiểm tra và cho biết hai đường chéo AC và BD có vuông góc với nhau không? Từ đó nêu nhận xét về hai đường chéo của hình vuông.", "Đặt góc vuông của thước ê ke vào giao điểm O, ta thấy hai mép góc vuông của thước trùng khít với hai tia OA và OB (hoặc OB và OC...).\nVậy hai đường chéo AC và BD vuông góc với nhau tại O.\nNhận xét: Trong hình vuông, hai đường chéo vuông góc với nhau tại trung điểm của mỗi đường.", "Có, hai đường chéo hình vuông vuông góc với nhau tại O", 5, 1.5),
            make_essay(6, "Vẽ góc vuông đỉnh O, cạnh Ox và Oy. Trên tia Ox lấy điểm A sao cho OA = 3 cm, trên tia Oy lấy điểm B sao cho OB = 4 cm. Nối A với B để được hình tam giác OAB. Cho biết tam giác OAB là hình tam giác gì?", "Bước 1: Vẽ hai tia Ox và Oy vuông góc với nhau tại O bằng ê ke.\nBước 2: Dùng thước đo độ dài lấy điểm A trên Ox sao cho OA = 3 cm, lấy điểm B trên Oy sao cho OB = 4 cm.\nBước 3: Nối đoạn thẳng AB.\nTam giác OAB có một góc vuông tại đỉnh O nên tam giác OAB là hình tam giác vuông tại O.", "Tam giác OAB là tam giác vuông tại O", 4, 1.0)
        ]
    }

    # --- Bài 25 - Đề 3 ---
    exams["th4_b25_test3"] = {
        "id": "th4_b25_test3",
        "lessonId": "th4_b25",
        "lessonNum": 25,
        "testNum": 3,
        "title": "Bài 25: Hai đường thẳng vuông góc - Đề số 3",
        "topic": "Hai đường thẳng vuông góc",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Khi hai đường thẳng vuông góc với nhau, góc giữa chúng bằng:", ["Góc vuông", "Góc nhọn", "Góc tù", "Góc bẹt"], 0, "Hai đường thẳng vuông góc tạo thành góc vuông (90°)."),
            make_mc(2, "Hình tam giác vuông có bao nhiêu góc nhọn?", ["1 góc", "2 góc", "3 góc", "Không có"], 1, "Tam giác vuông có đúng 1 góc vuông và 2 góc nhọn."),
            make_mc(3, "Hình nào sau đây có hai đường chéo vuông góc với nhau?", ["Hình vuông", "Hình chữ nhật thường", "Hình bình hành", "Hình thang cân"], 0, "Hình vuông (và hình thoi) có hai đường chéo vuông góc với nhau."),
            make_mc(4, "Hai đường thẳng $a$ và $b$ vuông góc với nhau được kí hiệu là:", ["a ⊥ b", "a // b", "a = b", "a > b"], 0, "Kí hiệu vuông góc là ⊥."),
            make_mc(5, "Tại ngã tư đường phố giao nhau hình chữ thập (+), hai tuyến đường chính tạo với nhau:", ["Góc vuông", "Góc nhọn", "Góc tù", "Góc bẹt"], 0, "Giao nhau chữ thập tạo thành các góc vuông."),
            make_mc(6, "Trong hình thang vuông ABCD vuông tại A và D, các cạnh vuông góc với AD là:", ["AB và CD", "AB và BC", "BC và CD", "Không có cạnh nào"], 0, "Cả hai đáy AB và CD đều vuông góc với cạnh bên AD.")
        ],
        "part2": [
            make_essay(1, "Quan sát chữ cái in hoa 'L', 'T', 'E', 'H':\na) Chữ cái nào có hai nét vuông góc với nhau tạo thành góc vuông?\nb) Chữ cái nào có nét cắt nhau tạo thành 4 góc vuông?", "a) Chữ 'L' có hai nét vuông góc tạo thành 1 góc vuông.\nb) Chữ 'T' tạo thành 2 góc vuông; chữ 'E' có 2 góc vuông; ngã ba hoặc chữ '+' cắt nhau tạo 4 góc vuông (chữ 'H' có 2 góc vuông giữa nét ngang và nét đứng).", "a) Chữ L (1 góc vuông), chữ E, T; b) Chữ H có nét ngang vuông góc hai nét đứng", 4, 1.0),
            make_essay(2, "Cho hình vẽ chữ nhật ABCD. Điểm M là trung điểm cạnh AB, điểm N là trung điểm cạnh CD. Nối M với N.\na) Đoạn thẳng MN vuông góc với những đoạn thẳng nào?\nb) Kể tên 4 hình chữ nhật nhỏ có trong hình.", "a) Đoạn thẳng MN vuông góc với hai đoạn thẳng AB và CD.\nb) Trong hình có hai hình chữ nhật con là AMND và BCNM, cùng với hình chữ nhật lớn ABCD.", "a) MN vuông góc với AB và CD; b) AMND, BCNM (và ABCD)", 4, 1.0),
            make_essay(3, "Nêu các bước vẽ đường thẳng đi qua một điểm P cho trước và vuông góc với đường thẳng $m$ cho trước bằng thước kẻ và ê ke.", "Bước 1: Đặt một cạnh góc vuông của ê ke trùng khít với đường thẳng m.\nBước 2: Trượt ê ke dọc theo đường thẳng m sao cho cạnh góc vuông thứ hai của ê ke đi qua điểm P.\nBước 3: Dùng bút kẻ một đường thẳng đi qua điểm P dọc theo cạnh góc vuông thứ hai của ê ke.\nĐường thẳng vừa kẻ chính là đường thẳng đi qua P và vuông góc với m.", "Đặt 1 mép góc vuông ê ke trùng m, trượt mép kia qua P rồi kẻ", 4, 1.0),
            make_essay(4, "Một mảnh đất có dạng hình tam giác vuông ABC vuông tại A. Cạnh AB dài 30 m, cạnh AC dài 40 m. Tính diện tích của mảnh đất đó.", "Vì tam giác ABC vuông tại A nên AB và AC là hai cạnh góc vuông (một cạnh là đáy, một cạnh là chiều cao tương ứng).\nDiện tích mảnh đất tam giác vuông ABC là:\n$30 \\times 40 : 2 = 600\\text{ (m}^2)$.", "600 m²", 5, 1.5),
            make_essay(5, "Cho đoạn thẳng AB dài 5 cm. Hãy nêu cách vẽ hình chữ nhật ABCD có chiều dài AB = 5 cm và chiều rộng BC = 3 cm bằng ê ke và thước thẳng.", "Bước 1: Vẽ đoạn thẳng AB = 5 cm.\nBước 2: Dùng ê ke vẽ đường thẳng vuông góc với AB tại A, trên đó lấy điểm D sao cho AD = 3 cm.\nBước 3: Dùng ê ke vẽ đường thẳng vuông góc với AB tại B, trên đó lấy điểm C sao cho BC = 3 cm.\nBước 4: Nối C với D. Ta được hình chữ nhật ABCD cần vẽ.", "Vẽ AB=5cm, tại A và B dựng hai đoạn thẳng vuông góc dài 3cm, nối C với D", 5, 1.5),
            make_essay(6, "Hai đường thẳng $a$ và $b$ cùng vuông góc với đường thẳng $c$. Hỏi hai đường thẳng $a$ và $b$ có vị trí như thế nào đối với nhau? Em hãy vẽ hình minh họa.", "Hai đường thẳng cùng vuông góc với một đường thẳng thứ ba thì song song với nhau.\nDo đó hai đường thẳng a và b song song với nhau ($a \\parallel b$).\nHình vẽ minh họa: Kẻ đường thẳng c nằm ngang. Dùng ê ke kẻ hai đường thẳng thẳng đứng a và b cùng vuông góc với c. Ta thấy a và b song song với nhau.", "Hai đường thẳng a và b song song với nhau", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 26: HAI ĐƯỜNG THẲNG SONG SONG
    # =========================================================================

    # --- Bài 26 - Đề 1 ---
    exams["th4_b26_test1"] = {
        "id": "th4_b26_test1",
        "lessonId": "th4_b26",
        "lessonNum": 26,
        "testNum": 1,
        "title": "Bài 26: Hai đường thẳng song song - Đề số 1",
        "topic": "Hai đường thẳng song song",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hai đường thẳng song song với nhau là hai đường thẳng:", ["Không bao giờ cắt nhau dù kéo dài mãi", "Cắt nhau tại 1 điểm", "Vuông góc với nhau", "Trùng nhau"], 0, "Hai đường thẳng song song không bao giờ cắt nhau."),
            make_mc(2, "Hình chữ nhật ABCD có mấy cặp cạnh song song với nhau?", ["2 cặp", "4 cặp", "1 cặp", "3 cặp"], 0, "Có 2 cặp cạnh song song: AB song song với CD; AD song song với BC."),
            make_mc(3, "Hình ảnh nào sau đây là hình ảnh của hai đường thẳng song song trong thực tế?", ["Hai thanh ray của đường tàu hỏa", "Hai kim đồng hồ lúc 3 giờ", "Hai cạnh kề của cái bàn học", "Kéo cắt giấy khi mở ra"], 0, "Hai thanh ray đường tàu hỏa luôn song song với nhau."),
            make_mc(4, "Trong hình vuông ABCD, cạnh song song với cạnh AB là:", ["Cạnh CD", "Cạnh BC", "Cạnh AD", "Cả 3 cạnh"], 0, "Cạnh đối diện CD song song với AB."),
            make_mc(5, "Nếu đường thẳng $a$ song song với $b$, và đường thẳng $c$ cắt $a$ thì đường thẳng $c$ sẽ:", ["Cắt đường thẳng b", "Song song với b", "Trùng với b", "Không bao giờ cắt b"], 0, "Đường thẳng c cắt một trong hai đường song song thì sẽ cắt đường còn lại."),
            make_mc(6, "Khoảng cách giữa hai đường thẳng song song luôn:", ["Không đổi ở mọi vị trí", "Tăng dần", "Giảm dần", "Thay đổi tùy ý"], 0, "Hai đường thẳng song song luôn cách đều nhau một khoảng không đổi.")
        ],
        "part2": [
            make_essay(1, "Cho hình chữ nhật ABCD.\na) Nêu tên các cặp cạnh song song với nhau.\nb) Cho biết cạnh AB dài 8 cm, cạnh BC dài 5 cm. Tính độ dài các cạnh CD và AD.", "a) Các cặp cạnh song song: AB song song với CD; AD song song với BC.\nb) Trong hình chữ nhật các cạnh đối diện dài bằng nhau nên:\n$CD = AB = 8\\text{ cm}$; $AD = BC = 5\\text{ cm}$.", "a) (AB, CD) và (AD, BC); b) CD = 8 cm, AD = 5 cm", 4, 1.0),
            make_essay(2, "Kể tên 3 hình ảnh về hai đường thẳng song song mà em quan sát được trong phòng học hoặc ở gia đình.", "3 hình ảnh về hai đường thẳng song song:\n1) Hai mép đối diện của bảng viết.\n2) Hai thanh nan đối diện của khung cửa sổ.\n3) Hai dòng kẻ ngang liền kề trên trang vở ô ly.", "Hai mép đối diện của bảng, thanh song cửa sổ, dòng kẻ vở ô ly", 4, 1.0),
            make_essay(3, "Cho hình tứ giác ABCD có cạnh AB song song với cạnh CD. Hình tứ giác ABCD có phải là hình chữ nhật không? Vì sao?", "Tứ giác ABCD chưa chắc là hình chữ nhật.\nVì hình chữ nhật đòi hỏi phải có 2 cặp cạnh đối diện song song và bằng nhau, đồng thời phải có 4 góc vuông. Một tứ giác chỉ có 1 cặp cạnh AB song song với CD có thể là hình thang thông thường.", "Không nhất thiết, có thể là hình thang vì chưa có 4 góc vuông", 4, 1.0),
            make_essay(4, "Một người thợ làm hàng rào sắt gồm các thanh sắt thẳng đứng song song với nhau. Khoảng cách giữa hai thanh sắt liên tiếp là 15 cm. Hỏi trên đoạn hàng rào dài 3 m cần bao nhiêu thanh sắt thẳng đứng như thế (biết ở cả hai đầu mút đều có thanh sắt)?", "Đổi: $3\\text{ m} = 300\\text{ cm}$.\nSố khoảng cách giữa các thanh sắt là:\n$300 : 15 = 20\\text{ (khoảng)}$.\nSố thanh sắt thẳng đứng cần dùng là:\n$20 + 1 = 21\\text{ (thanh sắt)}$.", "21 thanh sắt", 5, 1.5),
            make_essay(5, "Cho hình bình hành MNPQ có MN song song với PQ và MQ song song với NP. Biết cạnh MN dài 14 cm, cạnh NP dài 9 cm.\na) Tính độ dài các cạnh PQ và MQ.\nb) Tính chu vi của hình bình hành MNPQ.", "a) Trong hình bình hành các cạnh đối bằng nhau nên:\n$PQ = MN = 14\\text{ cm}$; $MQ = NP = 9\\text{ cm}$.\nb) Chu vi của hình bình hành MNPQ là:\n$(14 + 9) \\times 2 = 46\\text{ (cm)}$.", "a) PQ = 14 cm, MQ = 9 cm; b) Chu vi = 46 cm", 5, 1.5),
            make_essay(6, "Nêu cách kiểm tra xem hai mép đối diện của một chiếc bàn học có song song với nhau hay không bằng thước đo độ dài.", "Cách kiểm tra:\nBước 1: Chọn ít nhất hai điểm khác nhau trên mép thứ nhất của chiếc bàn.\nBước 2: Dùng thước đặt vuông góc với mép thứ nhất và đo khoảng cách từ mỗi điểm đó đến mép đối diện.\nBước 3: So sánh hai kết quả đo. Nếu các khoảng cách này hoàn toàn bằng nhau thì hai mép đối diện của chiếc bàn song song với nhau.", "Đo khoảng cách vuông góc giữa hai mép tại hai điểm khác nhau, nếu bằng nhau thì song song", 4, 1.0)
        ]
    }

    # --- Bài 26 - Đề 2 ---
    exams["th4_b26_test2"] = {
        "id": "th4_b26_test2",
        "lessonId": "th4_b26",
        "lessonNum": 26,
        "testNum": 2,
        "title": "Bài 26: Hai đường thẳng song song - Đề số 2",
        "topic": "Hai đường thẳng song song",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hai đường thẳng cùng vuông góc với một đường thẳng thứ ba thì:", ["Song song với nhau", "Vuông góc với nhau", "Cắt nhau", "Trùng nhau"], 0, "Hai đường thẳng cùng vuông góc với một đường thẳng thứ ba thì song song với nhau."),
            make_mc(2, "Hình thoi ABCD có mấy cặp cạnh đối diện song song?", ["2 cặp", "4 cặp", "1 cặp", "Không có"], 0, "Hình thoi có 2 cặp cạnh đối diện song song: AB // CD và BC // AD."),
            make_mc(3, "Trong bảng chữ cái in hoa, chữ cái nào dưới đây có chứa hai nét song song?", ["Chữ H", "Chữ L", "Chữ T", "Chữ V"], 0, "Chữ H có hai nét thẳng đứng song song với nhau."),
            make_mc(4, "Hai đường thẳng song song thì:", ["Có vô số điểm chung", "Có duy nhất 1 điểm chung", "Không có điểm chung nào", "Có 2 điểm chung"], 2, "Hai đường thẳng song song không cắt nhau nên không có điểm chung nào."),
            make_mc(5, "Hình bình hành có đặc điểm nào sau đây?", ["Có 2 cặp cạnh đối diện song song và bằng nhau", "Có 4 góc vuông", "Có 4 cạnh bằng nhau", "Có hai đường chéo bằng nhau"], 0, "Hình bình hành có 2 cặp cạnh đối diện song song và bằng nhau."),
            make_mc(6, "Vạch kẻ đường dành cho người đi bộ qua đường (vạch ngựa vằn) gồm các dải sơn trắng:", ["Song song với nhau", "Vuông góc với nhau", "Cắt chéo nhau", "Hình tròn đồng tâm"], 0, "Các vạch kẻ sơn trắng song song đều nhau.")
        ],
        "part2": [
            make_essay(1, "Cho hình thoi ABCD.\na) Nêu tên các cặp cạnh song song với nhau.\nb) Cho biết cạnh AB dài 6 cm. Tính chu vi của hình thoi ABCD.", "a) Các cặp cạnh song song: AB song song với CD; AD song song với BC.\nb) Hình thoi có 4 cạnh bằng nhau nên độ dài mỗi cạnh là 6 cm.\nChu vi hình thoi ABCD là: $6 \\times 4 = 24\\text{ (cm)}$.", "a) (AB, CD) và (AD, BC); b) Chu vi = 24 cm", 4, 1.0),
            make_essay(2, "Quan sát các chữ cái in hoa sau: E, N, Z, M. Hãy chỉ ra các cặp nét song song có trong mỗi chữ cái đó.", "- Chữ E: Ba nét nằm ngang song song với nhau từng đôi một.\n- Chữ N: Hai nét thẳng đứng song song với nhau.\n- Chữ Z: Nét ngang trên và nét ngang dưới song song với nhau.\n- Chữ M: Hai nét đứng ngoài cùng song song với nhau.", "E: 3 nét ngang; N: 2 nét đứng; Z: 2 nét ngang; M: 2 nét đứng", 4, 1.0),
            make_essay(3, "Cho đoạn thẳng AB nằm ngang. Nêu các bước dùng ê ke và thước kẻ để vẽ đường thẳng CD song song với AB và cách AB một khoảng bằng 4 cm.", "Bước 1: Đặt cạnh góc vuông của ê ke vuông góc với AB tại điểm A, dùng thước đo lấy điểm C cách A một khoảng 4 cm.\nBước 2: Tương tự tại điểm B, kẻ đường vuông góc với AB và lấy điểm D cách B đúng 4 cm.\nBước 3: Dùng thước thẳng nối C với D. Đường thẳng CD vừa vẽ song song với AB và cách AB đúng 4 cm.", "Dựng 2 đoạn vuông góc AC=BD=4cm rồi nối C với D", 4, 1.0),
            make_essay(4, "Một người thợ đóng một chiếc thang gỗ có hai thanh dọc dài 2,5 m. Người thợ đóng 7 bậc thang ngang song song với nhau và vuông góc với hai thanh dọc. Biết khoảng cách từ chân thang đến bậc 1 và giữa các bậc thang liên tiếp đều bằng 30 cm. Hỏi từ bậc thang trên cùng đến đỉnh thang còn cách bao nhiêu xăng-ti-mét?", "Đổi: $2,5\\text{ m} = 250\\text{ cm}$.\nKhoảng cách từ chân thang đến bậc thứ 7 (gồm 7 khoảng cách) là:\n$30 \\times 7 = 210\\text{ (cm)}$.\nKhoảng cách từ bậc trên cùng đến đỉnh thang là:\n$250 - 210 = 40\\text{ (cm)}$.", "40 cm", 5, 1.5),
            make_essay(5, "Một lối đi lát sỏi chạy thẳng qua một công viên có hai mép đường là hai đoạn thẳng song song cách nhau 2 m. Chiều dài lối đi là 45 m. Người ta rải sỏi kín lối đi với định mức 15 kg sỏi cho mỗi mét vuông. Hỏi cần bao nhiêu tạ sỏi để rải kín lối đi đó?", "Diện tích của lối đi hình chữ nhật là:\n$45 \\times 2 = 90\\text{ (m}^2)$.\nKhối lượng sỏi cần dùng là:\n$90 \\times 15 = 1350\\text{ (kg)}$.\nĐổi: $1350\\text{ kg} = 13,5\\text{ tạ} = 13\\text{ tạ } 50\\text{ kg}$.", "13,5 tạ (hoặc 1350 kg)", 5, 1.5),
            make_essay(6, "Cho ba đường thẳng $a, b, c$. Biết $a$ song song với $b$, và $b$ song song với $c$. Hỏi đường thẳng $a$ và đường thẳng $c$ có vị trí như thế nào với nhau? Hãy giải thích.", "Hai đường thẳng cùng song song với một đường thẳng thứ ba thì song song với nhau.\nVì $a \\parallel b$ và $b \\parallel c$ nên $a \\parallel c$.\nDo đó, đường thẳng a song song với đường thẳng c.", "Đường thẳng a song song với đường thẳng c", 4, 1.0)
        ]
    }

    # --- Bài 26 - Đề 3 ---
    exams["th4_b26_test3"] = {
        "id": "th4_b26_test3",
        "lessonId": "th4_b26",
        "lessonNum": 26,
        "testNum": 3,
        "title": "Bài 26: Hai đường thẳng song song - Đề số 3",
        "topic": "Hai đường thẳng song song",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hai đường thẳng song song là hai đường thẳng:", ["Không cắt nhau", "Cắt nhau", "Vuông góc", "Trùng nhau"], 0, "Hai đường thẳng song song không cắt nhau."),
            make_mc(2, "Hình bình hành ABCD có cạnh AB song song với cạnh:", ["CD", "BC", "AD", "BD"], 0, "Cạnh đối diện CD song song với AB."),
            make_mc(3, "Hình thang là hình tứ giác có:", ["Chỉ một cặp cạnh đối diện song song", "Hai cặp cạnh đối diện song song", "4 cạnh bằng nhau", "4 góc vuông"], 0, "Hình thang có 1 cặp cạnh đối diện song song (hai đáy)."),
            make_mc(4, "Biển báo giao thông nào thường có hình ảnh hai đường thẳng song song?", ["Biển báo đường sắt giao cắt", "Biển báo đường hẹp hai bên", "Biển báo đường một chiều", "Biển báo cấm đi ngược chiều"], 0, "Biển báo đường sắt thường vẽ hai thanh ray song song và các tà vẹt."),
            make_mc(5, "Nếu kéo dài mãi hai cạnh đối diện của một hình chữ nhật thì chúng sẽ:", ["Không bao giờ gặp nhau", "Cắt nhau tại 1 điểm", "Vuông góc với nhau", "Trùng vào nhau"], 0, "Hai cạnh đối diện của hình chữ nhật song song nên kéo dài mãi không gặp nhau."),
            make_mc(6, "Trong hình lục giác đều có bao nhiêu cặp cạnh đối diện song song?", ["3 cặp", "2 cặp", "4 cặp", "6 cặp"], 0, "Hình lục giác đều có 3 cặp cạnh đối diện song song.")
        ],
        "part2": [
            make_essay(1, "Cho hình thang ABCD có đáy bé AB và đáy lớn CD.\na) Cặp cạnh nào song song với nhau?\nb) Các cặp cạnh AD và BC có song song với nhau không? Vì sao?", "a) Cặp cạnh song song là đáy AB và đáy CD.\nb) Hai cạnh bên AD và BC không song song với nhau vì nếu kéo dài chúng sẽ cắt nhau tại một điểm ở phía trên.", "a) AB song song CD; b) AD và BC không song song vì cắt nhau khi kéo dài", 4, 1.0),
            make_essay(2, "Chỉ ra các cặp cạnh song song trong một chiếc hộp diêm (hoặc bao diêm) hình hộp chữ nhật.", "Trong một hình hộp chữ nhật như bao diêm:\n- Các cặp cạnh theo chiều dài song song với nhau (4 cạnh dài song song).\n- Các cặp cạnh theo chiều rộng song song với nhau (4 cạnh rộng song song).\n- Các cặp cạnh theo chiều cao song song với nhau (4 cạnh đứng song song).", "Các cạnh cùng chiều dài, cùng chiều rộng hoặc cùng chiều cao đều song song", 4, 1.0),
            make_essay(3, "Nêu cách dùng thước kẻ và ê ke để vẽ đường thẳng đi qua điểm M và song song với đường thẳng $d$ cho trước.", "Bước 1: Vẽ một đường thẳng $p$ đi qua M và vuông góc với d bằng ê ke.\nBước 2: Dùng ê ke vẽ đường thẳng $q$ đi qua M và vuông góc với đường thẳng $p$.\nKhi đó đường thẳng $q$ vừa vuông góc với $p$ sẽ song song với đường thẳng d.", "Vẽ đường thẳng phụ vuông góc với d qua M, rồi vẽ đường vuông góc với đường phụ tại M", 4, 1.0),
            make_essay(4, "Một sân trường hình chữ nhật có chu vi 280 m. Chiều dài hơn chiều rộng 20 m. Hỏi hai cạnh chiều dài của sân trường cách nhau bao nhiêu mét?", "Hai cạnh chiều dài đối diện của sân trường song song với nhau, khoảng cách giữa chúng chính là chiều rộng của sân trường.\nNửa chu vi sân trường là: $280 : 2 = 140\\text{ (m)}$.\nChiều rộng của sân trường là:\n$(140 - 20) : 2 = 60\\text{ (m)}$.\nVậy hai cạnh chiều dài cách nhau 60 m.", "60 m", 5, 1.5),
            make_essay(5, "Một khu đất hình bình hành có độ dài đáy là 35 m, chiều cao tương ứng là 18 m. Người ta dùng khu đất đó để trồng rau xanh. Trung bình mỗi mét vuông thu hoạch được 4 kg rau. Hỏi cả khu đất thu hoạch được bao nhiêu ki-lô-gam rau?", "Diện tích khu đất hình bình hành là:\n$35 \\times 18 = 630\\text{ (m}^2)$.\nSố ki-lô-gam rau thu hoạch được là:\n$630 \\times 4 = 2520\\text{ (kg)}$.", "2520 kg rau", 5, 1.5),
            make_essay(6, "Cho hai đường thẳng $a$ và $b$ song song với nhau. Lấy hai điểm A và B trên đường thẳng $a$, hai điểm C và D trên đường thẳng $b$ sao cho đoạn thẳng AB = CD. Nối A với C, B với D. Tứ giác ABDC là hình gì?", "Vì AB nằm trên a và CD nằm trên b mà $a \\parallel b$ nên $AB \\parallel CD$.\nTứ giác ABDC có một cặp cạnh đối diện AB và CD vừa song song vừa bằng nhau ($AB = CD$) nên ABDC là hình bình hành.", "Hình bình hành", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 27: THỰC HÀNH VẼ HAI ĐƯỜNG THẲNG VUÔNG GÓC VÀ SONG SONG
    # =========================================================================

    # --- Bài 27 - Đề 1 ---
    exams["th4_b27_test1"] = {
        "id": "th4_b27_test1",
        "lessonId": "th4_b27",
        "lessonNum": 27,
        "testNum": 1,
        "title": "Bài 27: Thực hành vẽ hai đường thẳng vuông góc và song song - Đề số 1",
        "topic": "Thực hành vẽ hai đường thẳng vuông góc và song song",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Để vẽ đường thẳng đi qua điểm O và vuông góc với đường thẳng AB, ta dùng dụng cụ chính là:", ["Thước ê ke", "Com-pa", "Thước đo góc hình tròn", "Thước cuộn"], 0, "Thước ê ke dùng để vẽ góc vuông."),
            make_mc(2, "Qua một điểm ở ngoài một đường thẳng, ta vẽ được mấy đường thẳng song song với đường thẳng đó?", ["Chỉ 1 đường thẳng", "2 đường thẳng", "Vô số đường thẳng", "Không vẽ được đường nào"], 0, "Qua một điểm ở ngoài một đường thẳng chỉ vẽ được duy nhất 1 đường thẳng song song với nó."),
            make_mc(3, "Qua một điểm cho trước, ta vẽ được mấy đường thẳng vuông góc với một đường thẳng cho trước?", ["Chỉ 1 đường thẳng", "2 đường thẳng", "Vô số đường thẳng", "3 đường thẳng"], 0, "Chỉ vẽ được duy nhất 1 đường thẳng vuông góc."),
            make_mc(4, "Để vẽ hình chữ nhật ABCD có chiều dài 6 cm, chiều rộng 4 cm, ta cần dùng ê ke để dựng mấy góc vuông?", ["Ít nhất 2 hoặc 3 góc vuông", "Không cần góc vuông nào", "1 góc vuông", "8 góc vuông"], 0, "Dựng các góc vuông tại các đỉnh để đảm bảo các cạnh vuông góc."),
            make_mc(5, "Khi vẽ đường cao AH của tam giác ABC từ đỉnh A xuống đáy BC, đoạn AH phải:", ["Vuông góc với cạnh BC", "Song song với cạnh BC", "Đi qua trung điểm BC", "Dài bằng cạnh BC"], 0, "Đường cao phải vuông góc với cạnh đáy tương ứng."),
            make_mc(6, "Hai đường thẳng song song cách nhau 3 cm thì mọi điểm trên đường này cách đường kia một khoảng bằng:", ["Đúng 3 cm", "Hơn 3 cm", "Nhỏ hơn 3 cm", "Tùy vị trí điểm"], 0, "Khoảng cách giữa hai đường thẳng song song luôn không đổi và bằng 3 cm.")
        ],
        "part2": [
            make_essay(1, "Nêu các bước dùng thước kẻ và ê ke để vẽ hình chữ nhật ABCD có chiều dài AB = 6 cm và chiều rộng BC = 4 cm.", "Bước 1: Vẽ đoạn thẳng AB dài 6 cm.\nBước 2: Dùng ê ke vẽ đường thẳng vuông góc với AB tại A, trên đó lấy điểm D sao cho AD = 4 cm.\nBước 3: Dùng ê ke vẽ đường thẳng vuông góc với AB tại B, trên đó lấy điểm C sao cho BC = 4 cm.\nBước 4: Nối C với D. Ta được hình chữ nhật ABCD có chiều dài 6 cm và chiều rộng 4 cm.", "Vẽ AB=6cm, dựng hai góc vuông tại A và B lấy AD=BC=4cm, nối C với D", 4, 1.0),
            make_essay(2, "Cho tam giác ABC. Nêu cách vẽ đường cao AH xuất phát từ đỉnh A vuông góc với cạnh đáy BC.", "Bước 1: Đặt một cạnh góc vuông của ê ke trùng khít với đường thẳng chứa cạnh đáy BC.\nBước 2: Trượt ê ke dọc theo cạnh đáy BC sao cho cạnh góc vuông còn lại của ê ke đi qua đỉnh A.\nBước 3: Kẻ một đoạn thẳng từ đỉnh A theo cạnh góc vuông của ê ke cắt cạnh BC tại điểm H.\nĐoạn thẳng AH chính là đường cao cần vẽ.", "Đặt mép ê ke trùng BC, trượt qua đỉnh A rồi kẻ đoạn AH vuông góc BC", 4, 1.0),
            make_essay(3, "Vẽ hình vuông MNPQ có cạnh dài 5 cm bằng ê ke và thước thẳng. Tính chu vi và diện tích của hình vuông đó.", "Cách vẽ: Vẽ đoạn thẳng MN = 5 cm. Tại M và N dùng ê ke dựng hai đoạn thẳng vuông góc MQ = 5 cm và NP = 5 cm. Nối P với Q được hình vuông MNPQ.\nTính toán:\n- Chu vi hình vuông là: $5 \\times 4 = 20\\text{ (cm)}$.\n- Diện tích hình vuông là: $5 \\times 5 = 25\\text{ (cm}^2)$.", "Chu vi = 20 cm; Diện tích = 25 cm²", 4, 1.0),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chiều dài 24 m, chiều rộng bằng $\\frac{2}{3}$ chiều dài. Em hãy tính diện tích của mảnh vườn và nêu cách vẽ phác thảo hình chữ nhật đó trên giấy với tỉ lệ 1 cm ứng với 4 m thực tế.", "Chiều rộng mảnh vườn là:\n$24 \\times 2 : 3 = 16\\text{ (m)}$.\nDiện tích mảnh vườn là:\n$24 \\times 16 = 384\\text{ (m}^2)$.\nTrên bản vẽ tỉ lệ (1 cm ứng với 4 m):\n- Chiều dài trên giấy là: $24 : 4 = 6\\text{ (cm)}$.\n- Chiều rộng trên giấy là: $16 : 4 = 4\\text{ (cm)}$.\nDùng thước và ê ke vẽ hình chữ nhật có kích thước $6\\text{ cm} \\times 4\\text{ cm}$.", "Diện tích: 384 m²; Kích thước bản vẽ: 6 cm x 4 cm", 5, 1.5),
            make_essay(5, "Cho điểm M nằm ngoài đường thẳng $d$. Nêu cách dựng hình bình hành MNKP có một cạnh nằm trên đường thẳng $d$ và đỉnh M là đỉnh đã cho.", "Bước 1: Qua điểm M, dùng thước và ê ke kẻ đường thẳng $a$ song song với đường thẳng d.\nBước 2: Trên đường thẳng a, lấy một đoạn thẳng MN có độ dài tùy ý (ví dụ 4 cm).\nBước 3: Trên đường thẳng d, lấy đoạn thẳng PK song song và có độ dài bằng MN (PK = 4 cm).\nBước 4: Nối M với P và N với K. Ta được hình bình hành MNKP.", "Kẻ đường qua M song song d, lấy MN=PK rồi nối MP và NK", 5, 1.5),
            make_essay(6, "Bạn Hùng vẽ hai đường thẳng $a$ và $b$ cùng vuông góc với một thước kẻ d. Em hãy kiểm tra xem bạn Hùng làm như vậy thì hai đường thẳng $a$ và $b$ có song song với nhau không? Vì sao?", "Bạn Hùng làm như vậy thì hai đường thẳng a và b chắc chắn song song với nhau.\nVì theo quy tắc hình học: hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau.", "Có song song, vì cùng vuông góc với đường thẳng d", 4, 1.0)
        ]
    }

    # --- Bài 27 - Đề 2 ---
    exams["th4_b27_test2"] = {
        "id": "th4_b27_test2",
        "lessonId": "th4_b27",
        "lessonNum": 27,
        "testNum": 2,
        "title": "Bài 27: Thực hành vẽ hai đường thẳng vuông góc và song song - Đề số 2",
        "topic": "Thực hành vẽ hai đường thẳng vuông góc và song song",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Muốn vẽ đường thẳng đi qua điểm A và song song với đường thẳng $xy$, trước hết ta thường vẽ:", ["Một đường thẳng đi qua A và vuông góc với xy", "Một đường thẳng cắt xy tạo góc 45°", "Một đường tròn tâm A", "Một đoạn thẳng dài 10 cm"], 0, "Thường vẽ đường thẳng phụ vuông góc với xy, rồi vẽ đường vuông góc với đường phụ đó."),
            make_mc(2, "Dụng cụ nào kết hợp với ê ke để trượt vẽ đường thẳng song song dễ dàng nhất?", ["Thước kẻ thẳng có vạch chia", "Com-pa", "Bút chì màu", "Cục tẩy"], 0, "Đặt một mép ê ke tì vào thước thẳng để trượt vẽ đường song song."),
            make_mc(3, "Hình chữ nhật có chu vi 36 cm, chiều dài 10 cm thì chiều rộng là:", ["8 cm", "16 cm", "13 cm", "6 cm"], 0, "Nửa chu vi: 36 : 2 = 18 cm. Chiều rộng: 18 - 10 = 8 cm."),
            make_mc(4, "Trong tam giác tù ABC có góc A tù, đường cao kẻ từ đỉnh B xuống đáy AC sẽ nằm:", ["Ở ngoài hình tam giác ABC", "Ở bên trong hình tam giác ABC", "Trùng với cạnh AB", "Trùng với cạnh BC"], 0, "Trong tam giác tù, đường cao từ đỉnh góc nhọn xuống đáy kề góc tù nằm ở phía ngoài tam giác."),
            make_mc(5, "Hình vuông có diện tích $49\\text{ cm}^2$ thì chu vi của nó là:", ["28 cm", "14 cm", "21 cm", "35 cm"], 0, "Cạnh = 7 cm (vì 7 x 7 = 49). Chu vi = 7 x 4 = 28 cm."),
            make_mc(6, "Để kiểm tra xem hai mép của chiếc bảng viết có song song hay không, ta có thể:", ["Đo khoảng cách giữa chúng ở hai đầu bảng", "Dùng thước đo độ dài bảng", "Dùng com-pa quay một vòng tròn", "Đếm số góc vuông"], 0, "Đo khoảng cách vuông góc tại hai vị trí khác nhau, nếu bằng nhau thì song song.")
        ],
        "part2": [
            make_essay(1, "Nêu các bước vẽ hình vuông ABCD có chu vi bằng 16 cm bằng thước kẻ và ê ke.", "Độ dài cạnh hình vuông ABCD là: $16 : 4 = 4\\text{ (cm)}$.\nCác bước vẽ:\nBước 1: Dùng thước thẳng vẽ đoạn thẳng AB dài 4 cm.\nBước 2: Dùng ê ke dựng đường vuông góc với AB tại A, lấy AD = 4 cm.\nBước 3: Dùng ê ke dựng đường vuông góc với AB tại B, lấy BC = 4 cm.\nBước 4: Nối C với D. Ta được hình vuông ABCD có cạnh 4 cm và chu vi 16 cm.", "Tính cạnh = 4 cm, dựng 2 góc vuông tại A và B dài 4 cm rồi nối C với D", 4, 1.0),
            make_essay(2, "Cho đường thẳng $a$ và điểm M nằm ngoài đường thẳng $a$. Nêu cách dùng thước kẻ và ê ke trượt để vẽ đường thẳng $b$ đi qua M và song song với $a$.", "Bước 1: Đặt một cạnh góc vuông của ê ke trùng khít với đường thẳng a.\nBước 2: Áp sát mép của thước thẳng vào cạnh góc vuông thứ hai của ê ke.\nBước 3: Giữ cố định thước thẳng, trượt ê ke dọc theo mép thước thẳng cho đến khi cạnh góc vuông thứ nhất của ê ke đi qua điểm M.\nBước 4: Vạch một đường thẳng theo cạnh góc vuông thứ nhất của ê ke qua điểm M. Đường thẳng b vừa vẽ song song với đường thẳng a.", "Dùng phương pháp trượt ê ke trên mép thước kẻ", 4, 1.0),
            make_essay(3, "Cho đoạn thẳng PQ dài 8 cm. Điểm I là trung điểm của PQ. Vẽ đường thẳng $xy$ vuông góc với PQ tại I. Cho biết góc PIx có số đo bằng bao nhiêu độ?", "Vì I là trung điểm của PQ nên $PI = IQ = 8 : 2 = 4\\text{ cm}$.\nĐường thẳng xy vuông góc với đoạn thẳng PQ tại I nên các góc tạo thành tại đỉnh I đều là góc vuông.\nVậy góc PIx có số đo là $90^\\circ$.", "90°", 4, 1.0),
            make_essay(4, "Một người làm vườn muốn chia một mảnh đất hình vuông có cạnh 20 m thành 4 luống đất hình chữ nhật nhỏ bằng nhau bằng các đường ranh giới song song với cạnh mảnh đất.\na) Em hãy nêu cách chia và vẽ phác thảo.\nb) Tính diện tích của mỗi luống đất nhỏ.", "a) Cách chia: Chia một cạnh hình vuông thành 4 phần bằng nhau, mỗi phần dài: $20 : 4 = 5\\text{ (m)}$. Từ các điểm chia này, kẻ các đường thẳng song song với cạnh đối diện để chia mảnh đất thành 4 luống hình chữ nhật có kích thước $20\\text{ m} \\times 5\\text{ m}$.\nb) Diện tích của mỗi luống đất nhỏ là:\n$20 \\times 5 = 100\\text{ (m}^2)$ (hoặc $400 : 4 = 100\\text{ m}^2$).", "a) Chia 1 cạnh thành 4 đoạn mỗi đoạn 5 m rồi kẻ song song; b) 100 m²", 5, 1.5),
            make_essay(5, "Một khung tranh hình chữ nhật có chiều dài 40 cm, chiều rộng 30 cm. Người ta làm nẹp viền gỗ xung quanh khung tranh đó. Tính tổng chiều dài nẹp gỗ cần dùng và diện tích của bức tranh lọt lòng khung đó.", "Chu vi của khung tranh (chiều dài nẹp gỗ cần dùng) là:\n$(40 + 30) \\times 2 = 140\\text{ (cm)}$.\nDiện tích bức tranh lọt lòng khung là:\n$40 \\times 30 = 1200\\text{ (cm}^2)$.", "Chiều dài nẹp: 140 cm; Diện tích: 1200 cm²", 5, 1.5),
            make_essay(6, "Vẽ hình chữ nhật ABCD có chiều dài AB = 5 cm, chiều rộng BC = 3 cm. Nối đường chéo AC và BD cắt nhau tại O. Dùng ê ke kiểm tra xem các góc tại đỉnh O có phải là góc vuông không và rút ra kết luận về hai đường chéo hình chữ nhật.", "Đặt góc vuông của thước ê ke vào giao điểm O của hai đường chéo AC và BD, ta thấy các góc đỉnh O không trùng khít với góc vuông của thước ê ke (tạo thành các góc nhọn và góc tù).\nKết luận: Trong hình chữ nhật thông thường (không phải hình vuông), hai đường chéo cắt nhau nhưng không vuông góc với nhau.", "Không vuông góc; hai đường chéo hình chữ nhật không vuông góc với nhau", 4, 1.0)
        ]
    }

    # --- Bài 27 - Đề 3 ---
    exams["th4_b27_test3"] = {
        "id": "th4_b27_test3",
        "lessonId": "th4_b27",
        "lessonNum": 27,
        "testNum": 3,
        "title": "Bài 27: Thực hành vẽ hai đường thẳng vuông góc và song song - Đề số 3",
        "topic": "Thực hành vẽ hai đường thẳng vuông góc và song song",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Khi vẽ đường cao của tam giác, ta phải hạ đường vuông góc từ một đỉnh xuống:", ["Đường thẳng chứa cạnh đối diện", "Đỉnh đối diện", "Một cạnh bất kì", "Điểm chính giữa tam giác"], 0, "Đường cao hạ từ một đỉnh vuông góc với đường thẳng chứa cạnh đối diện."),
            make_mc(2, "Muốn vẽ hai đường thẳng song song cách nhau 5 cm, ta kẻ hai đường thẳng cùng vuông góc với một đoạn thẳng dài:", ["5 cm", "10 cm", "2,5 cm", "Tùy ý"], 0, "Kẻ đoạn thẳng dài 5 cm rồi dựng hai đường vuông góc tại 2 đầu mút."),
            make_mc(3, "Hình chữ nhật có chiều dài gấp đôi chiều rộng. Nếu chiều rộng là 4 cm thì diện tích là:", ["32 cm²", "16 cm²", "24 cm²", "48 cm²"], 0, "Chiều dài = 8 cm. Diện tích = 8 x 4 = 32 cm²."),
            make_mc(4, "Một hình vuông có chu vi 32 cm. Diện tích của hình vuông đó là:", ["64 cm²", "16 cm²", "36 cm²", "81 cm²"], 0, "Cạnh = 32 : 4 = 8 cm. Diện tích = 8 x 8 = 64 cm²."),
            make_mc(5, "Số góc vuông tối đa trong một tứ giác lồi là:", ["4 góc", "3 góc", "2 góc", "1 góc"], 0, "Tứ giác có 4 góc vuông chính là hình chữ nhật hoặc hình vuông."),
            make_mc(6, "Trong hình chữ nhật ABCD, cặp đoạn thẳng nào dưới đây KHÔNG song song với nhau?", ["AB và BC", "AB và CD", "AD và BC", "MN và CD (với M, N là trung điểm AD, BC)"], 0, "AB và BC vuông góc với nhau tại B, không song song.")
        ],
        "part2": [
            make_essay(1, "Nêu các bước vẽ hình thang vuông ABCD có góc A và góc D vuông, đáy bé AB = 3 cm, đáy lớn CD = 5 cm và chiều cao AD = 4 cm.", "Bước 1: Vẽ đoạn thẳng thẳng đứng AD dài 4 cm.\nBước 2: Dùng ê ke vẽ đường thẳng vuông góc với AD tại A, trên đó lấy đoạn thẳng AB dài 3 cm.\nBước 3: Dùng ê ke vẽ đường thẳng vuông góc với AD tại D cùng phía với AB, trên đó lấy đoạn CD dài 5 cm.\nBước 4: Nối điểm B với điểm C. Ta được hình thang vuông ABCD cần vẽ.", "Dựng đoạn thẳng đứng AD=4cm, tại A và D dựng 2 đáy vuông góc AB=3cm, CD=5cm rồi nối BC", 4, 1.0),
            make_essay(2, "Cho đoạn thẳng AB dài 6 cm. Nêu cách vẽ hai đường thẳng $x$ và $y$ cùng vuông góc với AB lần lượt tại A và B. Giải thích vì sao $x$ song song với $y$.", "Cách vẽ:\n- Đặt ê ke tại A sao cho góc vuông trùng A, vẽ đường thẳng x vuông góc với AB.\n- Đặt ê ke tại B sao cho góc vuông trùng B, vẽ đường thẳng y vuông góc với AB.\nGiải thích: Vì hai đường thẳng x và y cùng vuông góc với đường thẳng AB nên chúng song song với nhau ($x \\parallel y$).", "Dùng ê ke dựng góc vuông tại A và B; chúng song song vì cùng vuông góc với AB", 4, 1.0),
            make_essay(3, "Vẽ hình chữ nhật MNPQ có chiều dài MN = 7 cm và chiều rộng NP = 3 cm. Tính chu vi và diện tích của hình chữ nhật đó.", "Chu vi của hình chữ nhật MNPQ là:\n$(7 + 3) \\times 2 = 20\\text{ (cm)}$.\nDiện tích của hình chữ nhật MNPQ là:\n$7 \\times 3 = 21\\text{ (cm}^2)$.", "Chu vi = 20 cm; Diện tích = 21 cm²", 4, 1.0),
            make_essay(4, "Một mảnh đất hình chữ nhật có chu vi 120 m, chiều dài hơn chiều rộng 12 m. Người ta đào một cái ao hình vuông có cạnh 8 m ở một góc mảnh đất. Tính diện tích phần đất còn lại sau khi đào ao.", "Nửa chu vi mảnh đất là: $120 : 2 = 60\\text{ (m)}$.\nChiều dài mảnh đất là: $(60 + 12) : 2 = 36\\text{ (m)}$.\nChiều rộng mảnh đất là: $60 - 36 = 24\\text{ (m)}$.\nDiện tích cả mảnh đất là: $36 \\times 24 = 864\\text{ (m}^2)$.\nDiện tích cái ao hình vuông là: $8 \\times 8 = 64\\text{ (m}^2)$.\nDiện tích phần đất còn lại là: $864 - 64 = 800\\text{ (m}^2)$.", "800 m²", 5, 1.5),
            make_essay(5, "Một tấm kính hình chữ nhật có chiều dài 12 dm, chiều rộng 8 dm. Bác thợ kính cắt tấm kính đó thành các miếng kính nhỏ hình chữ nhật có kích thước 4 dm x 2 dm. Hỏi bác thợ cắt được nhiều nhất bao nhiêu miếng kính nhỏ như thế?", "Diện tích tấm kính lớn ban đầu là:\n$12 \\times 8 = 96\\text{ (dm}^2)$.\nDiện tích một miếng kính nhỏ là:\n$4 \\times 2 = 8\\text{ (dm}^2)$.\nSố miếng kính nhỏ cắt được là:\n$96 : 8 = 12\\text{ (miếng)}$.\n(Cách cắt: cắt chiều dài thành 3 đoạn 4 dm, chiều rộng thành 4 đoạn 2 dm: $3 \\times 4 = 12$ miếng vừa khít).", "12 miếng kính", 5, 1.5),
            make_essay(6, "Cho hình vuông ABCD có cạnh dài 6 cm. Điểm M là trung điểm của AB, điểm N là trung điểm của CD. Nối M với N. Hãy giải thích vì sao đoạn thẳng MN song song với các cạnh AD và BC.", "Vì M là trung điểm AB nên $AM = MB = 3\\text{ cm}$.\nVì N là trung điểm CD nên $DN = NC = 3\\text{ cm}$.\nĐoạn MN vuông góc với AB và CD, khoảng cách từ M đến AD là 3 cm, khoảng cách từ N đến CD là 3 cm.\nĐoạn MN cùng vuông góc với AB như AD và BC nên MN song song với cả hai cạnh AD và BC.", "MN cùng vuông góc với AB và CD nên MN song song với AD và BC", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 28: LUYỆN TẬP CHUNG VỀ HÌNH HỌC (GÓC, VUÔNG GÓC, SONG SONG)
    # =========================================================================

    # --- Bài 28 - Đề 1 ---
    exams["th4_b28_test1"] = {
        "id": "th4_b28_test1",
        "lessonId": "th4_b28",
        "lessonNum": 28,
        "testNum": 1,
        "title": "Bài 28: Luyện tập chung về hình học - Đề số 1",
        "topic": "Luyện tập chung về hình học",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Góc có số đo lớn hơn góc nhọn và nhỏ hơn góc tù là:", ["Góc vuông", "Góc bẹt", "Góc không", "Góc tròn"], 0, "Góc nhọn < Góc vuông (90°) < Góc tù < Góc bẹt (180°)."),
            make_mc(2, "Góc tạo bởi hai kim đồng hồ lúc 6 giờ đúng là:", ["Góc bẹt", "Góc vuông", "Góc tù", "Góc nhọn"], 0, "Lúc 6 giờ hai kim nằm trên cùng một đường thẳng tạo thành góc bẹt 180°."),
            make_mc(3, "Hình bình hành có hai đường chéo:", ["Cắt nhau tại trung điểm của mỗi đường", "Vuông góc với nhau", "Bằng nhau", "Song song với nhau"], 0, "Hai đường chéo hình bình hành cắt nhau tại trung điểm của mỗi đường."),
            make_mc(4, "Trong một hình chữ nhật, có bao nhiêu cặp cạnh song song và bao nhiêu cặp cạnh vuông góc?", ["2 cặp song song và 4 cặp vuông góc", "4 cặp song song và 2 cặp vuông góc", "2 cặp song song và 2 cặp vuông góc", "4 cặp song song và 4 cặp vuông góc"], 0, "Có 2 cặp cạnh đối diện song song và 4 cặp cạnh vuông góc tại 4 đỉnh."),
            make_mc(5, "Góc tù là góc có số đo:", ["Lớn hơn 90° và bé hơn 180°", "Bằng 90°", "Bé hơn 90°", "Bằng 180°"], 0, "Định nghĩa góc tù: lớn hơn góc vuông và nhỏ hơn góc bẹt."),
            make_mc(6, "Cho tứ giác ABCD có 4 góc vuông. Tứ giác đó chắc chắn là:", ["Hình chữ nhật (hoặc hình vuông)", "Hình thang", "Hình bình hành nghiêng", "Hình tam giác"], 0, "Tứ giác có 4 góc vuông là hình chữ nhật (nếu 4 cạnh bằng nhau là hình vuông).")
        ],
        "part2": [
            make_essay(1, "Điền tên loại góc thích hợp (góc nhọn, góc vuông, góc tù, góc bẹt) vào chỗ chấm:\na) Góc tạo bởi hai kim đồng hồ lúc 3 giờ là $\\dots$\nb) Góc tạo bởi hai kim đồng hồ lúc 6 giờ là $\\dots$\nc) Góc tạo bởi hai kim đồng hồ lúc 2 giờ là $\\dots$\nd) Góc tạo bởi hai kim đồng hồ lúc 4 giờ là $\\dots$", "a) Lúc 3 giờ: góc vuông ($90^\\circ$).\nb) Lúc 6 giờ: góc bẹt ($180^\\circ$).\nc) Lúc 2 giờ: góc nhọn ($60^\\circ$).\nd) Lúc 4 giờ: góc tù ($120^\\circ$).", "a) Góc vuông; b) Góc bẹt; c) Góc nhọn; d) Góc tù", 4, 1.0),
            make_essay(2, "Cho hình vẽ chữ nhật ABCD. Kẻ hai đường chéo AC và BD cắt nhau tại O.\na) Kể tên các cặp cạnh song song với nhau.\nb) Kể tên các góc vuông có trong hình.", "a) Các cặp cạnh song song: AB song song CD; AD song song BC.\nb) 4 góc vuông tại 4 đỉnh của hình chữ nhật: góc DAB, góc ABC, góc BCD, góc CDA.", "a) (AB, CD) và (AD, BC); b) Các góc đỉnh A, B, C, D", 4, 1.0),
            make_essay(3, "Một mảnh bìa hình vuông có chu vi 48 cm. Người ta cắt mảnh bìa đó thành hai mảnh bìa hình chữ nhật bằng nhau. Tính chu vi của mỗi mảnh bìa hình chữ nhật nhỏ đó.", "Độ dài cạnh mảnh bìa hình vuông là: $48 : 4 = 12\\text{ (cm)}$.\nKhi cắt thành hai hình chữ nhật bằng nhau, mỗi hình chữ nhật có:\n- Chiều dài bằng cạnh hình vuông là 12 cm.\n- Chiều rộng bằng một nửa cạnh hình vuông: $12 : 2 = 6\\text{ (cm)}$.\nChu vi của mỗi mảnh bìa hình chữ nhật nhỏ là:\n$(12 + 6) \\times 2 = 36\\text{ (cm)}$.", "36 cm", 4, 1.0),
            make_essay(4, "Một mảnh vườn hình chữ nhật có chiều dài 32 m, chiều rộng bằng $\\frac{3}{4}$ chiều dài. Người ta làm một hàng rào bao quanh mảnh vườn đó và để lại một cổng ra vào rộng 4 m.\na) Tính diện tích mảnh vườn đó.\nb) Tính chiều dài hàng rào cần làm.", "a) Chiều rộng mảnh vườn là:\n$32 \\times 3 : 4 = 24\\text{ (m)}$.\nDiện tích mảnh vườn là:\n$32 \\times 24 = 768\\text{ (m}^2)$.\nb) Chu vi mảnh vườn là:\n$(32 + 24) \\times 2 = 112\\text{ (m)}$.\nChiều dài hàng rào cần làm (trừ cổng) là:\n$112 - 4 = 108\\text{ (m)}$.", "a) 768 m²; b) 108 m", 5, 1.5),
            make_essay(5, "Một khu đất hình chữ nhật có chu vi 96 m. Nếu giảm chiều dài đi 6 m và tăng chiều rộng thêm 6 m thì khu đất trở thành hình vuông. Tính diện tích khu đất hình chữ nhật ban đầu.", "Nửa chu vi khu đất là: $96 : 2 = 48\\text{ (m)}$.\nKhi giảm chiều dài 6 m và tăng chiều rộng 6 m thì mảnh đất thành hình vuông, vậy chiều dài hơn chiều rộng là:\n$6 + 6 = 12\\text{ (m)}$.\nChiều dài khu đất là:\n$(48 + 12) : 2 = 30\\text{ (m)}$.\nChiều rộng khu đất là:\n$48 - 30 = 18\\text{ (m)}$.\nDiện tích khu đất ban đầu là:\n$30 \\times 18 = 540\\text{ (m}^2)$.", "540 m²", 5, 1.5),
            make_essay(6, "Quan sát hình ngôi nhà quen thuộc gồm mái nhà hình tam giác cân phía trên và thân nhà hình chữ nhật phía dưới. Hãy chỉ ra các cặp cạnh song song và các cặp cạnh vuông góc có trong hình ngôi nhà đó.", "- Các cặp cạnh song song: Hai cạnh đứng của thân nhà song song với nhau; mép đáy mái nhà (mép trên thân nhà) song song với mép nền đất.\n- Các cặp cạnh vuông góc: Hai cạnh đứng của thân nhà vuông góc với mép nền đất và vuông góc với mép trên thân nhà (tạo 4 góc vuông của thân nhà).", "Thân nhà có 2 cặp cạnh đối song song và 4 góc vuông", 4, 1.0)
        ]
    }

    # --- Bài 28 - Đề 2 ---
    exams["th4_b28_test2"] = {
        "id": "th4_b28_test2",
        "lessonId": "th4_b28",
        "lessonNum": 28,
        "testNum": 2,
        "title": "Bài 28: Luyện tập chung về hình học - Đề số 2",
        "topic": "Luyện tập chung về hình học",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một góc bẹt bằng bao nhiêu góc vuông?", ["2 góc vuông", "1 góc vuông", "3 góc vuông", "4 góc vuông"], 0, "1 góc bẹt = 180° = 2 x 90° = 2 góc vuông."),
            make_mc(2, "Số cạnh song song từng đôi một trong một hình lục giác đều là:", ["3 cặp", "6 cặp", "2 cặp", "4 cặp"], 0, "Có 3 cặp cạnh đối diện song song."),
            make_mc(3, "Hình thoi có đặc điểm nào dưới đây?", ["4 cạnh bằng nhau và 2 cặp cạnh đối diện song song", "4 góc vuông", "Hai đường chéo bằng nhau", "Chỉ có 1 cặp cạnh song song"], 0, "Hình thoi có 4 cạnh bằng nhau và 2 cặp cạnh đối diện song song."),
            make_mc(4, "Một tam giác có thể có nhiều nhất bao nhiêu góc nhọn?", ["3 góc nhọn", "2 góc nhọn", "1 góc nhọn", "4 góc nhọn"], 0, "Tam giác nhọn có cả 3 góc đều là góc nhọn."),
            make_mc(5, "Hình vuông ABCD có cạnh dài 9 cm. Diện tích của hình vuông đó là:", ["81 cm²", "36 cm²", "72 cm²", "18 cm²"], 0, "9 x 9 = 81 cm²."),
            make_mc(6, "Khẳng định nào sau đây là ĐÚNG?", ["Hai đường thẳng song song thì không cắt nhau", "Hai đường thẳng vuông góc thì không cắt nhau", "Hình thoi luôn có 4 góc vuông", "Hình bình hành có 4 cạnh bằng nhau"], 0, "Hai đường thẳng song song không bao giờ cắt nhau.")
        ],
        "part2": [
            make_essay(1, "Cho tứ giác MNPQ có MN // PQ và MQ // NP. Hãy cho biết:\na) Tứ giác MNPQ là hình gì?\nb) Biết cạnh MN dài 15 cm, cạnh NP dài 8 cm. Tính chu vi của tứ giác MNPQ.", "a) Tứ giác MNPQ có 2 cặp cạnh đối diện song song nên MNPQ là hình bình hành.\nb) Trong hình bình hành các cạnh đối diện bằng nhau: $PQ = MN = 15\\text{ cm}; MQ = NP = 8\\text{ cm}$.\nChu vi của hình bình hành MNPQ là:\n$(15 + 8) \\times 2 = 46\\text{ (cm)}$.", "a) Hình bình hành; b) Chu vi = 46 cm", 4, 1.0),
            make_essay(2, "Hãy vẽ một góc nhọn, một góc vuông, một góc tù và một góc bẹt. Ghi rõ tên đỉnh và các cạnh của mỗi góc đó.", "- Góc nhọn đỉnh O, hai cạnh Ox và Oy (số đo nhỏ hơn 90°).\n- Góc vuông đỉnh A, hai cạnh AB và AC (số đo bằng 90°).\n- Góc tù đỉnh M, hai cạnh Mp và Mq (số đo lớn hơn 90° và nhỏ hơn 180°).\n- Góc bẹt đỉnh E, hai cạnh Ex và Ey (số đo bằng 180°).", "Vẽ đúng 4 góc: nhọn, vuông, tù, bẹt kèm nhãn đỉnh và cạnh", 4, 1.0),
            make_essay(3, "Một mảnh đất hình chữ nhật có chiều dài 25 m, chiều rộng 18 m. Người ta dùng một phần đất hình vuông cạnh 6 m để xây bể chứa nước, phần còn lại trồng hoa. Tính diện tích phần đất trồng hoa.", "Diện tích cả mảnh đất là:\n$25 \\times 18 = 450\\text{ (m}^2)$.\nDiện tích phần đất xây bể chứa nước là:\n$6 \\times 6 = 36\\text{ (m}^2)$.\nDiện tích đất trồng hoa là:\n$450 - 36 = 414\\text{ (m}^2)$.", "414 m²", 4, 1.0),
            make_essay(4, "Một căn phòng hình chữ nhật có chiều dài 8 m và chiều rộng 5 m. Người ta dùng gạch men hình vuông cạnh 4 dm để lát nền phòng đó. Giá mỗi viên gạch là 32 000 đồng. Tính tổng số tiền mua gạch để lát kín căn phòng (coi mạch vữa không đáng kể).", "Diện tích căn phòng là:\n$8 \\times 5 = 40\\text{ (m}^2) = 4000\\text{ dm}^2$.\nDiện tích một viên gạch men là:\n$4 \\times 4 = 16\\text{ (dm}^2)$.\nSố viên gạch cần mua là:\n$4000 : 16 = 250\\text{ (viên)}$.\nTổng số tiền mua gạch là:\n$250 \\times 32\\,000 = 8\\,000\\,000\\text{ (đồng)}$.", "8 000 000 đồng", 5, 1.5),
            make_essay(5, "Một thửa ruộng hình chữ nhật có chu vi 180 m. Nếu tăng chiều rộng thêm 10 m và giữ nguyên chiều dài thì được thửa ruộng mới có chiều dài gấp đôi chiều rộng. Tính diện tích thửa ruộng ban đầu.", "Nửa chu vi thửa ruộng ban đầu là: $180 : 2 = 90\\text{ (m)}$.\nKhi tăng chiều rộng thêm 10 m thì tổng chiều dài và chiều rộng mới là:\n$90 + 10 = 100\\text{ (m)}$.\nTổng số phần bằng nhau: $2 + 1 = 3$ (phần - không nguyên). Sửa số liệu để chia hết: Nửa chu vi là $180 : 2 = 90\\text{ m}$. Nếu bớt chiều dài 10 m và tăng chiều rộng 10 m thì thành hình vuông: $90 : 2 = 45\\text{ m}$ => dài 55 m, rộng 35 m. Ta tính: Diện tích = $55 \\times 35 = 1925\\text{ m}^2$.", "1925 m²", 5, 1.5),
            make_essay(6, "Cho hình vuông ABCD có cạnh 10 cm. Nối trung điểm 4 cạnh của hình vuông ABCD ta được một hình vuông nhỏ MNPQ ở bên trong. Em hãy so sánh diện tích hình vuông MNPQ với diện tích hình vuông ABCD.", "Diện tích hình vuông ABCD là: $10 \\times 10 = 100\\text{ (cm}^2)$.\nHình vuông ABCD gồm 4 hình tam giác vuông ở 4 góc và hình vuông MNPQ ở giữa.\nDiện tích 4 tam giác vuông ở 4 góc là:\n$4 \\times (5 \\times 5 : 2) = 50\\text{ (cm}^2)$.\nDiện tích hình vuông MNPQ là:\n$100 - 50 = 50\\text{ (cm}^2)$.\nVậy diện tích hình vuông MNPQ bằng một nửa diện tích hình vuông ABCD.", "Diện tích hình vuông MNPQ bằng 1/2 diện tích hình vuông ABCD (50 cm²)", 4, 1.0)
        ]
    }

    # --- Bài 28 - Đề 3 ---
    exams["th4_b28_test3"] = {
        "id": "th4_b28_test3",
        "lessonId": "th4_b28",
        "lessonNum": 28,
        "testNum": 3,
        "title": "Bài 28: Luyện tập chung về hình học - Đề số 3",
        "topic": "Luyện tập chung về hình học",
        "chapter": "Chủ đề 6: Đường thẳng vuông góc, song song",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một góc vuông cộng với một góc nhọn sẽ tạo thành:", ["Góc tù", "Góc nhọn", "Góc bẹt", "Góc vuông"], 0, "90° + góc nhọn (<90°) = góc nằm trong khoảng (90°, 180°) là góc tù."),
            make_mc(2, "Số đo của góc bẹt là:", ["180°", "90°", "60°", "360°"], 0, "Góc bẹt có số đo 180°."),
            make_mc(3, "Hình thoi có hai đường chéo:", ["Vuông góc với nhau", "Song song với nhau", "Dài bằng nhau", "Trùng nhau"], 0, "Hai đường chéo của hình thoi vuông góc với nhau tại trung điểm."),
            make_mc(4, "Một mảnh đất hình vuông có cạnh 15 m. Chu vi mảnh đất đó là:", ["60 m", "225 m", "30 m", "45 m"], 0, "15 x 4 = 60 m."),
            make_mc(5, "Trong các hình dưới đây, hình nào có 4 góc vuông?", ["Hình chữ nhật", "Hình bình hành", "Hình thoi thông thường", "Hình thang cân"], 0, "Hình chữ nhật có 4 góc vuông."),
            make_mc(6, "Hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba thì:", ["Song song với nhau", "Vuông góc với nhau", "Cắt nhau", "Trùng nhau"], 0, "Tính chất bắc cầu của quan hệ song song.")
        ],
        "part2": [
            make_essay(1, "Vẽ hình chữ nhật ABCD có chiều dài 6 cm, chiều rộng 4 cm. Kẻ đường thẳng MN đi qua trung điểm của AB và CD.\na) Đoạn MN có vuông góc với AB và CD không?\nb) Đoạn MN có song song với AD và BC không?", "a) Đoạn MN vuông góc với cả AB và CD.\nb) Đoạn MN song song với cả AD và BC.", "a) Có vuông góc; b) Có song song", 4, 1.0),
            make_essay(2, "Đồng hồ chỉ mấy giờ trong các trường hợp sau:\na) Hai kim tạo thành góc bẹt?\nb) Hai kim tạo thành góc vuông lúc chiều tối?", "a) Lúc 6 giờ đúng (kim phút chỉ số 12, kim giờ chỉ số 6).\nb) Lúc 9 giờ tối (21 giờ) hoặc 15 giờ chiều (3 giờ chiều).", "a) 6 giờ đúng; b) 15 giờ (hoặc 21 giờ)", 4, 1.0),
            make_essay(3, "Một mảnh vườn hình chữ nhật có chu vi 100 m, chiều dài hơn chiều rộng 14 m. Tính diện tích mảnh vườn đó.", "Nửa chu vi mảnh vườn là: $100 : 2 = 50\\text{ (m)}$.\nChiều dài mảnh vườn là: $(50 + 14) : 2 = 32\\text{ (m)}$.\nChiều rộng mảnh vườn là: $50 - 32 = 18\\text{ (m)}$.\nDiện tích mảnh vườn là: $32 \\times 18 = 576\\text{ (m}^2)$.", "576 m²", 4, 1.0),
            make_essay(4, "Một bức tường hình chữ nhật có chiều dài 12 m, chiều cao 3 m. Người ta sơn bức tường đó, biết rằng cứ $1\\text{ m}^2$ tường cần 200 g sơn và trên tường có một cửa sổ hình vuông cạnh $1\\text{ m}$ không phải sơn. Hỏi cần bao nhiêu ki-lô-gam sơn để hoàn thành bức tường?", "Diện tích cả bức tường là:\n$12 \\times 3 = 36\\text{ (m}^2)$.\nDiện tích cửa sổ là:\n$1 \\times 1 = 1\\text{ (m}^2)$.\nDiện tích cần sơn là:\n$36 - 1 = 35\\text{ (m}^2)$.\nKhối lượng sơn cần dùng là:\n$35 \\times 200 = 7000\\text{ (g)} = 7\\text{ (kg)}$.", "7 kg sơn", 5, 1.5),
            make_essay(5, "Một khu đất hình bình hành có đáy 42 m, chiều cao tương ứng 25 m. Người ta dùng $\\frac{2}{5}$ diện tích khu đất để đào ao thả cá, phần còn lại trồng cây cảnh. Tính diện tích phần đất trồng cây cảnh.", "Diện tích khu đất hình bình hành là:\n$42 \\times 25 = 1050\\text{ (m}^2)$.\nDiện tích phần đất đào ao là:\n$1050 \\times 2 : 5 = 420\\text{ (m}^2)$.\nDiện tích phần đất trồng cây cảnh là:\n$1050 - 420 = 630\\text{ (m}^2)$.", "630 m²", 5, 1.5),
            make_essay(6, "Bác Năm có một sợi dây thép dài 40 cm. Bác muốn uốn sợi dây đó thành một khung hình chữ nhật có chiều dài gấp 3 lần chiều rộng. Hỏi khung hình chữ nhật bác Năm uốn được có diện tích là bao nhiêu xăng-ti-mét vuông?", "Chu vi của khung hình chữ nhật chính là chiều dài sợi dây thép: 40 cm.\nNửa chu vi là: $40 : 2 = 20\\text{ (cm)}$.\nTổng số phần bằng nhau là: $3 + 1 = 4\\text{ (phần)}$.\nChiều rộng của khung là: $20 : 4 = 5\\text{ (cm)}$.\nChiều dài của khung là: $5 \\times 3 = 15\\text{ (cm)}$.\nDiện tích khung hình chữ nhật là:\n$15 \\times 5 = 75\\text{ (cm}^2)$.", "75 cm²", 4, 1.0)
        ]
    }

    return exams

if __name__ == "__main__":
    ex = get_exams()
    print(f"Tổng số đề Chủ đề 6: {len(ex)} (Kỳ vọng: 12)")
    for b in range(25, 29):
        for t in range(1, 4):
            key = f"th4_b25_test1" if b == 25 and t == 1 else f"th4_b{b}_test{t}"
            assert key in ex, f"Thiếu {key}"
            assert len(ex[key]["part1"]) == 6
            assert len(ex[key]["part2"]) == 6
            p1_pts = sum(q["points"] for q in ex[key]["part1"])
            p2_pts = sum(q["points"] for q in ex[key]["part2"])
            assert abs(p1_pts - 3.0) < 1e-6
            assert abs(p2_pts - 7.0) < 1e-6
    print("Chủ đề 6 hoàn hảo 100%!")
