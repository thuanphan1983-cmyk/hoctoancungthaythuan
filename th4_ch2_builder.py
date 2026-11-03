# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 2: GÓC VÀ ĐƠN VỊ ĐO GÓC (BÀI 7 ĐẾN BÀI 9) - TOÁN 4 KNTT
Gồm 3 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 7: Đo góc, đơn vị đo góc (th4_b7_test1, th4_b7_test2, th4_b7_test3)
- Bài 8: Góc nhọn, góc tù, góc bẹt (th4_b8_test1, th4_b8_test2, th4_b8_test3)
- Bài 9: Luyện tập chung Chủ đề 2 (th4_b9_test1, th4_b9_test2, th4_b9_test3)
Tổng cộng: 9 đề kiểm tra chất lượng cao, độc lập 100%.
"""

def make_mc(qid, question, options, correct, explanation):
    q_text = question if question.startswith(f"**Câu {qid}:** ") else f"**Câu {qid}:** {question}"
    return {
        "id": qid,
        "question": q_text,
        "options": options,
        "correct": correct,
        "explanation": explanation,
        "points": 0.5
    }

def make_essay(qid, question, solution, answer, lineCount=4, points=1.0):
    p_text = question if question.startswith(f"**Bài {qid}:** ") else f"**Bài {qid}:** {question}"
    return {
        "id": qid,
        "question": p_text,
        "solution": solution,
        "answer": answer,
        "lineCount": lineCount,
        "points": points
    }

def get_exams():
    exams = {}

    # =========================================================================
    # BÀI 7: ĐO GÓC, ĐƠN VỊ ĐO GÓC
    # =========================================================================
    exams["th4_b7_test1"] = {
        "id": "th4_b7_test1",
        "lessonId": "th4_b7",
        "lessonNum": 7,
        "testNum": 1,
        "title": "Bài 7: Đo góc, đơn vị đo góc - Đề số 1",
        "topic": "Đo góc, đơn vị đo góc",
        "chapter": "Chủ đề 2: Góc và đơn vị đo góc",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Đơn vị chuẩn thường dùng để đo góc trong chương trình Tiểu học là gì?", [
                "Độ (°)",
                "Mét (m)",
                "Lít (l)",
                "Gam (g)"
            ], 0, "Đơn vị chuẩn đo góc là độ, kí hiệu là °."),
            make_mc(2, "Số đo của một góc vuông bằng bao nhiêu độ?", [
                "45°",
                "60°",
                "90°",
                "180°"
            ], 2, "Góc vuông có số đo chuẩn bằng 90°."),
            make_mc(3, "Góc đỉnh O có hai cạnh OA và OB. Dụng cụ nào dưới đây được dùng để đo số đo góc này?", [
                "Thước đo góc (thước đo độ)",
                "Thước cuộn xây dựng",
                "Com-pa vẽ đường tròn",
                "Nhiệt kế thủy ngân"
            ], 0, "Thước đo góc (thước đo độ) dùng để đo số đo của các góc."),
            make_mc(4, "Góc bẹt có số đo bằng bao nhiêu độ?", [
                "90°",
                "120°",
                "180°",
                "360°"
            ], 2, "Góc bẹt có số đo bằng 180°, tương đương 2 góc vuông."),
            make_mc(5, "Khi đồng hồ chỉ đúng 3 giờ, góc tạo bởi kim giờ và kim phút có số đo là bao nhiêu độ?", [
                "30°",
                "60°",
                "90°",
                "120°"
            ], 2, "Lúc 3 giờ, kim phút chỉ số 12 và kim giờ chỉ số 3, hai kim tạo thành một góc vuông có số đo 90°."),
            make_mc(6, "Quan sát thước đo góc, nếu một cạnh của góc trùng với vạch 0° và cạnh còn lại chỉ vạch 60° thì góc đó có số đo là:", [
                "30°",
                "60°",
                "90°",
                "120°"
            ], 1, "Cạnh còn lại chỉ vạch 60° nên số đo của góc là 60°.")
        ],
        "part2": [
            make_essay(1, "Ghi tên đỉnh, các cạnh và nêu số đo của góc vuông đỉnh M, cạnh MN và MP.",
                       "Lời giải:\n- Góc đã cho có đỉnh là: M.\n- Các cạnh tạo nên góc là: cạnh MN và cạnh MP.\n- Vì đây là góc vuông nên số đo của góc bằng 90°.\nĐáp số: Đỉnh M; hai cạnh MN, MP; số đo 90°.",
                       "Đỉnh M; hai cạnh MN, MP; số đo 90°", 4, 1.0),
            make_essay(2, "Cho góc đỉnh O có cạnh Ox và Oy. Bạn An dùng thước đo góc đo được số đo là 45°, bạn Bình đo được 75°. Biết số đo đúng là trung bình cộng số đo của hai bạn. Hãy tính số đo đúng của góc đó.",
                       "Lời giải:\nTổng số đo góc hai bạn đo được là:\n45 + 75 = 120 (°)\nSố đo đúng của góc đỉnh O là:\n120 : 2 = 60 (°)\nĐáp số: 60°.",
                       "60°", 4, 1.0),
            make_essay(3, "Một mặt đồng hồ hình tròn được chia đều thành 12 khoảng giờ bằng nhau. Biết toàn bộ vòng tròn có số đo là 360°. Hỏi mỗi khoảng giữa hai số liền nhau trên mặt đồng hồ ứng với một góc bao nhiêu độ?",
                       "Lời giải:\nSố đo góc giữa hai vạch số liền nhau trên mặt đồng hồ tròn là:\n360 : 12 = 30 (°)\nĐáp số: 30°.",
                       "30°", 4, 1.0),
            make_essay(4, "Một chiếc quạt giấy xòe ra tạo thành một góc đỉnh O. Khi mở một nửa, góc xòe đo được 60°. Khi mở rộng hết cỡ, góc xòe gấp 3 lần góc mở một nửa. Hỏi khi mở hết cỡ, góc xòe của quạt đo được bao nhiêu độ? Góc đó bằng mấy lần góc vuông?",
                       "Lời giải:\nKhi mở hết cỡ, số đo góc xòe của chiếc quạt giấy là:\n60 x 3 = 180 (°)\nVì một góc vuông có số đo là 90°, nên số lần góc vuông bằng:\n180 : 90 = 2 (lần)\nĐáp số: 180°; bằng 2 lần góc vuông.",
                       "180°; bằng 2 lần góc vuông", 5, 1.5),
            make_essay(5, "Ba bạn Hùng, Dũng và Minh cùng vẽ các góc đỉnh A. Góc của Hùng đo được 30°. Góc của Dũng có số đo gấp đôi góc của Hùng. Góc của Minh có số đo bằng tổng số đo góc của Hùng và Dũng cộng thêm 15°. Tính số đo góc của Minh.",
                       "Lời giải:\nSố đo góc bạn Dũng vẽ là:\n30 x 2 = 60 (°)\nTổng số đo góc của Hùng và Dũng là:\n30 + 60 = 90 (°)\nSố đo góc bạn Minh vẽ là:\n90 + 15 = 105 (°)\nĐáp số: 105°.",
                       "105°", 5, 1.5),
            make_essay(6, "Một góc bẹt đỉnh K có số đo 180°. Tia Kt nằm giữa hai cạnh của góc bẹt chia góc bẹt thành hai góc. Biết góc thứ nhất có số đo là 70°. Hỏi góc thứ hai có số đo là bao nhiêu độ?",
                       "Lời giải:\nSố đo của góc thứ hai là:\n180 - 70 = 110 (°)\nĐáp số: 110°.",
                       "110°", 4, 1.0)
        ]
    }

    exams["th4_b7_test2"] = {
        "id": "th4_b7_test2",
        "lessonId": "th4_b7",
        "lessonNum": 7,
        "testNum": 2,
        "title": "Bài 7: Đo góc, đơn vị đo góc - Đề số 2",
        "topic": "Đo góc, đơn vị đo góc",
        "chapter": "Chủ đề 2: Góc và đơn vị đo góc",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Kí hiệu độ trong số đo góc được viết ở vị trí nào của con số?", [
                "Dưới góc trái",
                "Phía trên bên phải của số (ví dụ 45°)",
                "Trước con số",
                "Dưới đáy con số"
            ], 1, "Kí hiệu độ (°) được viết nhỏ ở phía trên bên phải của con số biểu thị số đo."),
            make_mc(2, "Số đo của một góc bẹt bằng tổng số đo của mấy góc vuông?", [
                "1 góc vuông",
                "2 góc vuông",
                "3 góc vuông",
                "4 góc vuông"
            ], 1, "Góc bẹt có số đo 180° = 90° x 2, tức là bằng 2 góc vuông."),
            make_mc(3, "Khi kim phút quay từ số 12 đến số 2 trên mặt đồng hồ thì kim phút đã quét một góc có số đo là bao nhiêu độ?", [
                "30°",
                "60°",
                "90°",
                "120°"
            ], 1, "Mỗi khoảng giờ là 30°, từ số 12 đến số 2 gồm 2 khoảng giờ: 30° x 2 = 60°."),
            make_mc(4, "Một góc có số đo là 120°. Góc này lớn hơn góc vuông bao nhiêu độ?", [
                "20°",
                "30°",
                "40°",
                "50°"
            ], 1, "Góc vuông là 90°. Hiệu là: 120° - 90° = 30°."),
            make_mc(5, "Đỉnh của góc tạo bởi hai tia OM và ON là điểm nào?", [
                "Điểm M",
                "Điểm N",
                "Điểm O",
                "Điểm bất kì"
            ], 2, "Hai tia OM và ON chung gốc O nên O chính là đỉnh của góc."),
            make_mc(6, "Dùng thước đo góc đặt tâm thước trùng với đỉnh E, cạnh EA đi qua vạch 0°, cạnh EB đi qua vạch 85°. Số đo của góc đỉnh E cạnh EA, EB là:", [
                "75°",
                "85°",
                "95°",
                "105°"
            ], 1, "Cạnh EB chỉ vạch 85° nên số đo của góc là 85°.")
        ],
        "part2": [
            make_essay(1, "Nêu tên đỉnh và các cạnh của góc tạo bởi hai chiếc kim đồng hồ khi đồng hồ chỉ 4 giờ đúng.",
                       "Lời giải:\n- Đỉnh của góc là: Trục tâm của mặt đồng hồ.\n- Hai cạnh của góc là: Cạnh kim giờ (chỉ số 4) và cạnh kim phút (chỉ số 12).\nĐáp số: Đỉnh là trục kim; hai cạnh là kim giờ và kim phút.",
                       "Đỉnh là trục kim; hai cạnh là kim giờ và kim phút", 4, 1.0),
            make_essay(2, "Một góc đỉnh A có số đo bằng 35°. Góc đỉnh B có số đo lớn hơn góc đỉnh A là 25°. Hãy tính số đo của góc đỉnh B.",
                       "Lời giải:\nSố đo của góc đỉnh B là:\n35 + 25 = 60 (°)\nĐáp số: 60°.",
                       "60°", 4, 1.0),
            make_essay(3, "Khi đồng hồ chỉ 6 giờ đúng, hai kim giờ và phút nằm thẳng hàng với nhau tạo thành một góc. Cho biết đó là góc gì và có số đo bao nhiêu độ?",
                       "Lời giải:\nLúc 6 giờ đúng, hai kim tạo thành một đường thẳng đi qua tâm đồng hồ.\nĐó là góc bẹt.\nSố đo của góc bẹt là 180°.\nĐáp số: Góc bẹt, số đo 180°.",
                       "Góc bẹt, số đo 180°", 4, 1.0),
            make_essay(4, "Bác thợ mộc cưa một thanh gỗ tạo thành một góc có số đo 150°. Sau đó bác gọt bớt một góc 60° ở phần đó. Hỏi góc còn lại của thanh gỗ có số đo bằng bao nhiêu độ? Góc còn lại đó bằng mấy lần một góc có số đo 45°?",
                       "Lời giải:\nSố đo góc còn lại của thanh gỗ là:\n150 - 60 = 90 (°)\nSố lần so với góc có số đo 45° là:\n90 : 45 = 2 (lần)\nĐáp số: 90°; bằng 2 lần góc 45°.",
                       "90°; bằng 2 lần góc 45°", 5, 1.5),
            make_essay(5, "Một hình tam giác ABC có góc đỉnh A bằng 60°, góc đỉnh B bằng 70°. Biết tổng số đo ba góc trong một hình tam giác luôn luôn bằng 180°. Hỏi góc đỉnh C của hình tam giác đó có số đo là bao nhiêu độ?",
                       "Lời giải:\nTổng số đo của góc đỉnh A và góc đỉnh B là:\n60 + 70 = 130 (°)\nSố đo của góc đỉnh C là:\n180 - 130 = 50 (°)\nĐáp số: 50°.",
                       "50°", 5, 1.5),
            make_essay(6, "Bạn Lan vẽ một góc đỉnh O có số đo 40°. Bạn Mai vẽ góc đỉnh O thứ hai kề với góc của Lan sao cho tổng số đo hai góc bằng một góc vuông (90°). Hỏi số đo góc của bạn Mai là bao nhiêu độ?",
                       "Lời giải:\nSố đo góc bạn Mai vẽ là:\n90 - 40 = 50 (°)\nĐáp số: 50°.",
                       "50°", 4, 1.0)
        ]
    }

    exams["th4_b7_test3"] = {
        "id": "th4_b7_test3",
        "lessonId": "th4_b7",
        "lessonNum": 7,
        "testNum": 3,
        "title": "Bài 7: Đo góc, đơn vị đo góc - Đề số 3",
        "topic": "Đo góc, đơn vị đo góc",
        "chapter": "Chủ đề 2: Góc và đơn vị đo góc",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một góc có số đo là 180°. Góc đó được gọi là:", [
                "Góc nhọn",
                "Góc tù",
                "Góc bẹt",
                "Góc vuông"
            ], 2, "Góc có số đo bằng 180° chính là góc bẹt."),
            make_mc(2, "Khi đồng hồ chỉ 1 giờ đúng, góc tạo bởi kim giờ và kim phút có số đo là:", [
                "15°",
                "30°",
                "45°",
                "60°"
            ], 1, "Kim phút chỉ số 12, kim giờ chỉ số 1, khoảng cách là 1 khoảng giờ = 360° : 12 = 30°."),
            make_mc(3, "Góc có số đo bé hơn 90° nhưng lớn hơn 0° được đo bằng dụng cụ thước đo góc. Nếu vạch chỉ 55° thì góc đó có số đo là:", [
                "45°",
                "50°",
                "55°",
                "65°"
            ], 2, "Cạnh của góc chỉ vạch 55° nên góc có số đo 55°."),
            make_mc(4, "Góc đỉnh P có cạnh PQ và PR. Điểm nào sau đây là đỉnh của góc?", [
                "Điểm Q",
                "Điểm R",
                "Điểm P",
                "Điểm O"
            ], 2, "Góc đỉnh P có hai cạnh là PQ và PR, vậy P là đỉnh."),
            make_mc(5, "Tổng số đo của hai góc: góc A = 35° và góc B = 55° bằng bao nhiêu độ?", [
                "80°",
                "90°",
                "100°",
                "110°"
            ], 1, "35° + 55° = 90°."),
            make_mc(6, "Nửa góc bẹt có số đo bằng bao nhiêu độ?", [
                "45°",
                "90°",
                "60°",
                "120°"
            ], 1, "Góc bẹt là 180°, một nửa góc bẹt là 180° : 2 = 90° (bằng góc vuông).")
        ],
        "part2": [
            make_essay(1, "Quan sát chiếc ê-ke học sinh thông dụng, em hãy cho biết số đo góc vuông trên ê-ke bằng bao nhiêu độ và hai góc còn lại có đặc điểm gì về số đo so với góc vuông?",
                       "Lời giải:\n- Góc vuông trên ê-ke có số đo bằng 90°.\n- Hai góc còn lại trên ê-ke đều có số đo bé hơn 90° (tức là bé hơn góc vuông).\nĐáp số: Góc vuông bằng 90°; hai góc còn lại bé hơn 90°.",
                       "Góc vuông bằng 90°; hai góc còn lại bé hơn 90°", 4, 1.0),
            make_essay(2, "Góc đỉnh D có số đo là 135°. Hỏi góc đó lớn hơn góc vuông bao nhiêu độ và bé hơn góc bẹt bao nhiêu độ?",
                       "Lời giải:\nGóc đỉnh D lớn hơn góc vuông số độ là:\n135 - 90 = 45 (°)\nGóc đỉnh D bé hơn góc bẹt số độ là:\n180 - 135 = 45 (°)\nĐáp số: Lớn hơn góc vuông 45°; bé hơn góc bẹt 45°.",
                       "Lớn hơn góc vuông 45°; bé hơn góc bẹt 45°", 4, 1.0),
            make_essay(3, "Một chiếc compa khi vẽ hình tròn được mở rộng tạo thành một góc có số đo 40°. Người ta muốn mở rộng thêm để góc tạo bởi hai chân compa đạt đúng 75°. Hỏi cần mở rộng thêm một góc bao nhiêu độ?",
                       "Lời giải:\nSố độ cần mở rộng thêm là:\n75 - 40 = 35 (°)\nĐáp số: 35°.",
                       "35°", 4, 1.0),
            make_essay(4, "Một cánh cửa mở quay tạo thành một góc đỉnh A giữa cánh cửa và mép tường. Buổi sáng mở một góc 30°. Buổi trưa mở rộng gấp 4 lần buổi sáng. Hỏi buổi trưa cánh cửa mở tạo thành một góc bao nhiêu độ? Góc đó lớn hơn một góc vuông bao nhiêu độ?",
                       "Lời giải:\nSố đo góc cánh cửa mở ra vào buổi trưa là:\n30 x 4 = 120 (°)\nGóc mở buổi trưa lớn hơn góc vuông số độ là:\n120 - 90 = 30 (°)\nĐáp số: 120°; lớn hơn góc vuông 30°.",
                       "120°; lớn hơn góc vuông 30°", 5, 1.5),
            make_essay(5, "Ba góc liên tiếp cùng chung đỉnh O tạo thành một góc bẹt. Góc thứ nhất có số đo 50°, góc thứ hai có số đo 65°. Hãy tính số đo của góc thứ ba.",
                       "Lời giải:\nTổng số đo của góc thứ nhất và góc thứ hai là:\n50 + 65 = 115 (°)\nVì tổng ba góc tạo thành một góc bẹt (180°) nên số đo góc thứ ba là:\n180 - 115 = 65 (°)\nĐáp số: 65°.",
                       "65°", 5, 1.5),
            make_essay(6, "Khi kim phút quay từ số 12 đến số 5 trên mặt đồng hồ thì đã quay được một góc bao nhiêu độ?",
                       "Lời giải:\nTừ số 12 đến số 5 gồm 5 khoảng giờ bằng nhau.\nMỗi khoảng giờ có số đo là 30°.\nSố đo góc kim phút đã quay là:\n30 x 5 = 150 (°)\nĐáp số: 150°.",
                       "150°", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 8: GÓC NHỌN, GÓC TÙ, GÓC BẸT
    # =========================================================================
    exams["th4_b8_test1"] = {
        "id": "th4_b8_test1",
        "lessonId": "th4_b8",
        "lessonNum": 8,
        "testNum": 1,
        "title": "Bài 8: Góc nhọn, góc tù, góc bẹt - Đề số 1",
        "topic": "Góc nhọn, góc tù, góc bẹt",
        "chapter": "Chủ đề 2: Góc và đơn vị đo góc",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Góc nào sau đây có số đo bé hơn góc vuông?", [
                "Góc bẹt",
                "Góc tù",
                "Góc nhọn",
                "Góc vuông"
            ], 2, "Góc nhọn là góc có số đo lớn hơn 0° và bé hơn góc vuông (90°)."),
            make_mc(2, "Góc có số đo lớn hơn góc vuông và bé hơn góc bẹt được gọi là:", [
                "Góc nhọn",
                "Góc tù",
                "Góc bẹt",
                "Góc vuông"
            ], 1, "Góc tù lớn hơn góc vuông và bé hơn góc bẹt (90° < góc tù < 180°)."),
            make_mc(3, "Trong các số đo sau, số đo nào là của một góc tù?", [
                "45°",
                "90°",
                "115°",
                "180°"
            ], 2, "115° lớn hơn 90° và bé hơn 180° nên 115° là góc tù."),
            make_mc(4, "Một góc có số đo 75° là loại góc gì?", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 0, "Vì 75° bé hơn 90° nên đây là góc nhọn."),
            make_mc(5, "Khi đồng hồ chỉ 2 giờ đúng, góc tạo bởi kim giờ và kim phút là góc gì?", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 0, "Lúc 2 giờ góc đo được là 30° x 2 = 60° < 90°, do đó là góc nhọn."),
            make_mc(6, "Hình tam giác có ba góc đều là góc nhọn được gọi là tam giác gì?", [
                "Tam giác vuông",
                "Tam giác nhọn",
                "Tam giác tù",
                "Tam giác đều"
            ], 1, "Hình tam giác có cả ba góc nhọn gọi là tam giác nhọn.")
        ],
        "part2": [
            make_essay(1, "Hãy phân loại các góc có số đo sau thành ba nhóm: Góc nhọn, Góc vuông, Góc tù: 35°, 90°, 120°, 68°, 95°.",
                       "Lời giải:\n- Nhóm góc nhọn (bé hơn 90°): 35°, 68°.\n- Nhóm góc vuông (bằng 90°): 90°.\n- Nhóm góc tù (lớn hơn 90° và bé hơn 180°): 120°, 95°.\nĐáp số: Góc nhọn: 35°, 68°; Góc vuông: 90°; Góc tù: 120°, 95°.",
                       "Góc nhọn: 35°, 68°; Góc vuông: 90°; Góc tù: 120°, 95°", 4, 1.0),
            make_essay(2, "Quan sát tứ giác ABCD có góc đỉnh A bằng 90°, góc đỉnh B bằng 65°, góc đỉnh C bằng 115°, góc đỉnh D bằng 90°. Hãy cho biết tứ giác có mấy góc vuông, mấy góc nhọn và mấy góc tù.",
                       "Lời giải:\n- Có 2 góc vuông: góc đỉnh A (90°) và góc đỉnh D (90°).\n- Có 1 góc nhọn: góc đỉnh B (65° < 90°).\n- Có 1 góc tù: góc đỉnh C (115° > 90°).\nĐáp số: 2 góc vuông, 1 góc nhọn, 1 góc tù.",
                       "2 góc vuông, 1 góc nhọn, 1 góc tù", 4, 1.0),
            make_essay(3, "Lúc mấy giờ đúng thì hai kim đồng hồ tạo thành: a) Một góc vuông? b) Một góc bẹt? (Mỗi trường hợp nêu 1 thời điểm cụ thể).",
                       "Lời giải:\na) Lúc 3 giờ đúng (hoặc 9 giờ đúng) hai kim đồng hồ tạo thành một góc vuông.\nb) Lúc 6 giờ đúng hai kim đồng hồ tạo thành một góc bẹt.\nĐáp số: a) 3 giờ; b) 6 giờ.",
                       "a) 3 giờ; b) 6 giờ", 4, 1.0),
            make_essay(4, "Một bạn học sinh vẽ 5 góc đỉnh O. Trong đó có 2 góc vuông, số góc nhọn gấp đôi số góc vuông, còn lại là góc tù. Biết tổng số góc vẽ được là 7 góc. Hỏi bạn đó vẽ được mấy góc nhọn và mấy góc tù? Góc tù đó có số đo là bao nhiêu nếu biết tổng số đo của góc tù đó với một góc nhọn 50° bằng 160°?",
                       "Lời giải:\nSố góc nhọn bạn học sinh vẽ là:\n2 x 2 = 4 (góc)\nSố góc tù bạn học sinh vẽ là:\n7 - (2 + 4) = 1 (góc)\nSố đo của góc tù đó là:\n160 - 50 = 110 (°)\nĐáp số: 4 góc nhọn, 1 góc tù; góc tù có số đo 110°.",
                       "4 góc nhọn, 1 góc tù; góc tù đo 110°", 5, 1.5),
            make_essay(5, "Trong một hình thang vuông MNPQ có góc đỉnh M và đỉnh Q là góc vuông. Góc đỉnh N là góc tù có số đo 130°. Biết tổng bốn góc của một tứ giác luôn bằng 360°. Hãy tính số đo của góc đỉnh P và cho biết góc đỉnh P là góc nhọn hay góc tù.",
                       "Lời giải:\nTổng số đo của ba góc M, Q và N là:\n90 + 90 + 130 = 310 (°)\nSố đo của góc đỉnh P là:\n360 - 310 = 50 (°)\nVì 50° < 90° nên góc đỉnh P là góc nhọn.\nĐáp số: Góc đỉnh P bằng 50°, là góc nhọn.",
                       "50°, góc nhọn", 5, 1.5),
            make_essay(6, "Hãy so sánh số đo góc nhọn 48° với một góc tù 132°: Góc tù lớn hơn góc nhọn bao nhiêu độ?",
                       "Lời giải:\nSố đo góc tù lớn hơn số đo góc nhọn là:\n132 - 48 = 84 (°)\nĐáp số: 84°.",
                       "84°", 4, 1.0)
        ]
    }

    exams["th4_b8_test2"] = {
        "id": "th4_b8_test2",
        "lessonId": "th4_b8",
        "lessonNum": 8,
        "testNum": 2,
        "title": "Bài 8: Góc nhọn, góc tù, góc bẹt - Đề số 2",
        "topic": "Góc nhọn, góc tù, góc bẹt",
        "chapter": "Chủ đề 2: Góc và đơn vị đo góc",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Góc bẹt có số đo bằng bao nhiêu góc vuông cộng lại?", [
                "1 góc vuông",
                "2 góc vuông",
                "3 góc vuông",
                "4 góc vuông"
            ], 1, "Góc bẹt = 180° = 90° + 90° (bằng 2 góc vuông)."),
            make_mc(2, "Khi đồng hồ chỉ 4 giờ đúng, góc tạo bởi kim giờ và kim phút là:", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 2, "Lúc 4 giờ, số đo góc là 30° x 4 = 120° (lớn hơn 90° và bé hơn 180°) nên là góc tù."),
            make_mc(3, "Góc nào có số đo lớn nhất trong các loại góc sau?", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 3, "Góc bẹt (180°) lớn hơn góc tù (>90°), góc vuông (90°) và góc nhọn (<90°)."),
            make_mc(4, "Một góc có số đo 89° là:", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 0, "89° < 90° nên là góc nhọn."),
            make_mc(5, "Một góc có số đo 91° là:", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 2, "91° lớn hơn 90° và bé hơn 180° nên là góc tù."),
            make_mc(6, "Trong hình chữ nhật ABCD có 4 góc ở 4 đỉnh. Cả 4 góc đó đều là:", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 1, "Hình chữ nhật có 4 góc vuông.")
        ],
        "part2": [
            make_essay(1, "Hãy xếp các góc sau theo thứ tự số đo từ bé đến lớn: Góc tù, Góc bẹt, Góc nhọn, Góc vuông.",
                       "Lời giải:\nTa có so sánh số đo:\nGóc nhọn (< 90°) < Góc vuông (= 90°) < Góc tù (> 90° và < 180°) < Góc bẹt (= 180°).\nVậy thứ tự từ bé đến lớn là:\nGóc nhọn, Góc vuông, Góc tù, Góc bẹt.\nĐáp số: Góc nhọn, Góc vuông, Góc tù, Góc bẹt.",
                       "Góc nhọn, Góc vuông, Góc tù, Góc bẹt", 4, 1.0),
            make_essay(2, "Cho hình tam giác có một góc vuông và hai góc còn lại bằng nhau. Hãy tính số đo của hai góc còn lại đó và cho biết hai góc đó là góc nhọn hay góc tù? (Biết tổng 3 góc của tam giác là 180°).",
                       "Lời giải:\nTổng số đo của hai góc còn lại là:\n180 - 90 = 90 (°)\nSố đo của mỗi góc là:\n90 : 2 = 45 (°)\nVì 45° < 90° nên cả hai góc đó đều là góc nhọn.\nĐáp số: Mỗi góc 45°; đều là góc nhọn.",
                       "Mỗi góc 45°; đều là góc nhọn", 4, 1.0),
            make_essay(3, "Khi đồng hồ chỉ 5 giờ đúng, góc tạo bởi kim giờ và kim phút là góc gì và có số đo bao nhiêu độ?",
                       "Lời giải:\nLúc 5 giờ đúng, kim phút chỉ số 12, kim giờ chỉ số 5.\nKhoảng cách giữa hai kim là 5 khoảng giờ.\nSố đo góc tạo bởi hai kim là:\n30 x 5 = 150 (°)\nVì 150° > 90° và 150° < 180° nên đó là góc tù.\nĐáp số: Góc tù, số đo 150°.",
                       "Góc tù, số đo 150°", 4, 1.0),
            make_essay(4, "Một người thợ xếp các thanh sắt thành khung hình ngũ giác có 5 góc. Biết khung có 2 góc vuông, 1 góc nhọn có số đo 70°, còn lại là 2 góc tù bằng nhau. Biết tổng số đo của cả 5 góc ngũ giác là 540°. Hãy tính số đo của mỗi góc tù đó.",
                       "Lời giải:\nTổng số đo của 2 góc vuông và 1 góc nhọn là:\n90 x 2 + 70 = 250 (°)\nTổng số đo của 2 góc tù còn lại là:\n540 - 250 = 290 (°)\nSố đo của mỗi góc tù là:\n290 : 2 = 145 (°)\nĐáp số: 145°.",
                       "145°", 5, 1.5),
            make_essay(5, "Bác thợ mộc đóng một chiếc giá sách. Bác đo góc giữa thanh đỡ và cột dọc được 3 góc đỉnh A. Góc thứ nhất là góc nhọn 40°, góc thứ hai là góc vuông 90°, góc thứ ba là góc tù lớn hơn góc thứ nhất 75°. Tính số đo góc thứ ba và tính tổng số đo cả ba góc.",
                       "Lời giải:\nSố đo góc thứ ba (góc tù) là:\n40 + 75 = 115 (°)\nTổng số đo của cả ba góc là:\n40 + 90 + 115 = 245 (°)\nĐáp số: Góc thứ ba: 115°; Tổng: 245°.",
                       "Góc thứ ba: 115°; Tổng: 245°", 5, 1.5),
            make_essay(6, "Một góc tù có số đo lớn hơn góc vuông 42°. Hỏi góc tù đó có số đo là bao nhiêu độ?",
                       "Lời giải:\nSố đo của góc tù đó là:\n90 + 42 = 132 (°)\nĐáp số: 132°.",
                       "132°", 4, 1.0)
        ]
    }

    exams["th4_b8_test3"] = {
        "id": "th4_b8_test3",
        "lessonId": "th4_b8",
        "lessonNum": 8,
        "testNum": 3,
        "title": "Bài 8: Góc nhọn, góc tù, góc bẹt - Đề số 3",
        "topic": "Góc nhọn, góc tù, góc bẹt",
        "chapter": "Chủ đề 2: Góc và đơn vị đo góc",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình tam giác có thể có nhiều nhất bao nhiêu góc vuông?", [
                "1 góc vuông",
                "2 góc vuông",
                "3 góc vuông",
                "0 góc vuông"
            ], 0, "Trong một hình tam giác chỉ có thể có nhiều nhất 1 góc vuông (vì tổng ba góc là 180°)."),
            make_mc(2, "Khi kim đồng hồ chỉ 10 giờ đúng, góc bé hơn tạo bởi kim giờ và kim phút là loại góc gì?", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 0, "Từ số 10 đến số 12 là 2 khoảng giờ = 30° x 2 = 60° < 90°, là góc nhọn."),
            make_mc(3, "Góc tạo bởi hai mép của một chiếc kéo đang mở rộng có số đo 50°. Đó là góc gì?", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 0, "50° < 90° nên đó là góc nhọn."),
            make_mc(4, "Một góc bẹt có số đo gấp mấy lần góc vuông?", [
                "1 lần",
                "2 lần",
                "3 lần",
                "4 lần"
            ], 1, "180° : 90° = 2 (lần)."),
            make_mc(5, "Góc tù là góc có số đo nằm trong khoảng nào sau đây?", [
                "Bé hơn 90°",
                "Đúng 90°",
                "Lớn hơn 90° và bé hơn 180°",
                "Đúng 180°"
            ], 2, "Góc tù lớn hơn 90° và bé hơn 180°."),
            make_mc(6, "Quan sát chữ cái in hoa 'L', góc tạo bởi hai nét của chữ L là loại góc gì?", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 1, "Hai nét của chữ 'L' vuông góc với nhau tạo thành góc vuông.")
        ],
        "part2": [
            make_essay(1, "Hãy kể tên 2 chữ cái in hoa trong bảng chữ cái tiếng Việt có chứa góc vuông.",
                       "Lời giải:\nCác chữ cái in hoa có chứa góc vuông là:\n- Chữ L (chứa 1 góc vuông giữa nét đứng và nét ngang).\n- Chữ E (chứa các góc vuông giữa nét đứng và các nét ngang).\n(Hoặc các chữ khác như H, T, F...)\nĐáp số: Chữ L và chữ E.",
                       "Chữ L và chữ E", 4, 1.0),
            make_essay(2, "Một góc nhọn có số đo là 55°. Cần tăng thêm bao nhiêu độ nữa để góc đó trở thành góc vuông?",
                       "Lời giải:\nSố độ cần tăng thêm là:\n90 - 55 = 35 (°)\nĐáp số: 35°.",
                       "35°", 4, 1.0),
            make_essay(3, "Trong hình bình hành MNPQ có hai góc đối đỉnh M và P bằng 60°, hai góc đối đỉnh N và Q bằng 120°. Cho biết các góc đỉnh M, P là góc gì và các góc đỉnh N, Q là góc gì.",
                       "Lời giải:\n- Các góc đỉnh M và đỉnh P có số đo 60° (< 90°) nên là các góc nhọn.\n- Các góc đỉnh N và đỉnh Q có số đo 120° (> 90° và < 180°) nên là các góc tù.\nĐáp số: M và P là góc nhọn; N và Q là góc tù.",
                       "M và P là góc nhọn; N và Q là góc tù", 4, 1.0),
            make_essay(4, "Một người lắp đặt pin mặt trời điều chỉnh tấm pin nghiêng tạo với mặt đất một góc nhọn 35°. Sau đó người đó nâng tấm pin lên thêm một góc 25°. Hỏi góc mới tạo bởi tấm pin và mặt đất bằng bao nhiêu độ? Góc đó là góc nhọn hay góc tù?",
                       "Lời giải:\nSố đo góc mới tạo bởi tấm pin và mặt đất là:\n35 + 25 = 60 (°)\nVì 60° < 90° nên góc đó là góc nhọn.\nĐáp số: 60°; là góc nhọn.",
                       "60°; là góc nhọn", 5, 1.5),
            make_essay(5, "Tại một ngã tư, ba con đường giao nhau tại điểm O tạo thành ba góc. Góc thứ nhất là góc vuông 90°, góc thứ hai là góc nhọn 45°. Biết góc thứ ba là góc còn lại để ghép với hai góc kia tạo thành một vòng tròn trọn vẹn (360°). Hãy tính số đo của góc thứ ba và cho biết góc đó lớn hơn góc bẹt bao nhiêu độ.",
                       "Lời giải:\nTổng số đo của góc thứ nhất và góc thứ hai là:\n90 + 45 = 135 (°)\nSố đo của góc thứ ba là:\n360 - 135 = 225 (°)\nGóc thứ ba lớn hơn góc bẹt số độ là:\n225 - 180 = 45 (°)\nĐáp số: 225°; lớn hơn góc bẹt 45°.",
                       "225°; lớn hơn góc bẹt 45°", 5, 1.5),
            make_essay(6, "Cho góc tù xOy có số đo 135°. Kẻ tia phân giác Ot chia góc tù đó thành hai góc bằng nhau. Hỏi mỗi góc mới tạo thành có số đo là bao nhiêu độ và là góc nhọn hay góc tù?",
                       "Lời giải:\nSố đo của mỗi góc mới tạo thành là:\n135 : 2 = 67,5 (°) (hay 67 độ 30 phút)\n(Trong phạm vi lớp 4, ta có: 67,5° < 90° nên mỗi góc là một góc nhọn).\nĐáp số: 67,5°; là góc nhọn.",
                       "67,5°; là góc nhọn", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 9: LUYỆN TẬP CHUNG CHỦ ĐỀ 2
    # =========================================================================
    exams["th4_b9_test1"] = {
        "id": "th4_b9_test1",
        "lessonId": "th4_b9",
        "lessonNum": 9,
        "testNum": 1,
        "title": "Bài 9: Luyện tập chung Chủ đề 2 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 2",
        "chapter": "Chủ đề 2: Góc và đơn vị đo góc",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một góc có số đo bằng 90° là loại góc gì?", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 1, "Góc 90° chính là góc vuông."),
            make_mc(2, "Khẳng định nào sau đây là ĐÚNG về góc tù?", [
                "Góc tù bé hơn góc vuông",
                "Góc tù bằng góc bẹt",
                "Góc tù lớn hơn góc vuông và bé hơn góc bẹt",
                "Góc tù bé hơn góc nhọn"
            ], 2, "Theo định nghĩa, góc tù lớn hơn góc vuông và bé hơn góc bẹt."),
            make_mc(3, "Khi đồng hồ chỉ đúng 9 giờ, hai kim giờ và kim phút tạo thành một góc có số đo là:", [
                "60°",
                "90°",
                "120°",
                "180°"
            ], 1, "Lúc 9 giờ, kim phút chỉ số 12, kim giờ chỉ số 9, tạo thành một góc vuông 90°."),
            make_mc(4, "Một góc bẹt có số đo là 180°. Nếu chia góc bẹt đó thành 3 phần bằng nhau thì mỗi phần có số đo là:", [
                "45°",
                "60°",
                "90°",
                "120°"
            ], 1, "180° : 3 = 60°."),
            make_mc(5, "Trong một tam giác vuông, ngoài góc vuông ra thì hai góc còn lại bắt buộc phải là:", [
                "Hai góc vuông",
                "Hai góc tù",
                "Hai góc nhọn",
                "Một góc nhọn và một góc tù"
            ], 2, "Vì tổng ba góc bằng 180° và có 1 góc vuông 90° nên hai góc còn lại có tổng bằng 90°, mỗi góc đều bé hơn 90° nên là hai góc nhọn."),
            make_mc(6, "Góc đỉnh O cạnh Ox và Oy có số đo 140°. Hỏi đó là góc gì?", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 2, "140° nằm giữa 90° và 180° nên là góc tù.")
        ],
        "part2": [
            make_essay(1, "Đoạn thẳng AB cắt đoạn thẳng CD tại O tạo thành 4 góc. Biết trong đó có một góc bằng 90°. Hỏi 3 góc còn lại có số đo bằng bao nhiêu độ và là loại góc gì?",
                       "Lời giải:\nKhi hai đoạn thẳng cắt nhau tạo thành một góc vuông (90°) thì ba góc còn lại ở đỉnh O cũng đều bằng 90° và đều là các góc vuông.\nĐáp số: Ba góc còn lại đều bằng 90° và là góc vuông.",
                       "Đều bằng 90° và là góc vuông", 4, 1.0),
            make_essay(2, "Một góc tù có số đo là 125°. Hỏi góc tù đó lớn hơn một góc vuông bao nhiêu độ và bé hơn góc bẹt bao nhiêu độ?",
                       "Lời giải:\nGóc tù đó lớn hơn góc vuông số độ là:\n125 - 90 = 35 (°)\nGóc tù đó bé hơn góc bẹt số độ là:\n180 - 125 = 55 (°)\nĐáp số: Lớn hơn góc vuông 35°; bé hơn góc bẹt 55°.",
                       "Lớn hơn góc vuông 35°; bé hơn góc bẹt 55°", 4, 1.0),
            make_essay(3, "Trên mặt đồng hồ, từ lúc 1 giờ đúng đến lúc 3 giờ đúng thì kim giờ đã quét một góc có số đo là bao nhiêu độ?",
                       "Lời giải:\nTừ 1 giờ đến 3 giờ kim giờ đi qua 2 khoảng giờ.\nSố đo góc mà kim giờ đã quét là:\n30 x 2 = 60 (°)\nĐáp số: 60°.",
                       "60°", 4, 1.0),
            make_essay(4, "Một người thợ uốn một đoạn dây thép tạo thành hình một góc nhọn 40°. Sau đó người thợ uốn mở rộng góc đó thêm 2 lần, mỗi lần thêm 25°. Hỏi sau hai lần mở rộng, góc tạo bởi đoạn dây thép có số đo là bao nhiêu độ? Góc đó trở thành góc nhọn hay góc tù?",
                       "Lời giải:\nTổng số độ mở rộng thêm qua hai lần là:\n25 x 2 = 50 (°)\nSố đo của góc sau hai lần mở rộng là:\n40 + 50 = 90 (°)\nVì số đo bằng 90° nên góc đó đã trở thành góc vuông.\nĐáp số: 90°; trở thành góc vuông.",
                       "90°; trở thành góc vuông", 5, 1.5),
            make_essay(5, "Một hình tứ giác có bốn góc. Góc thứ nhất là góc vuông 90°, góc thứ hai là góc nhọn 60°, góc thứ ba là góc tù 110°. Biết tổng bốn góc của hình tứ giác bằng 360°. Hãy tính số đo của góc thứ tư và cho biết góc thứ tư là loại góc gì.",
                       "Lời giải:\nTổng số đo của ba góc đã biết là:\n90 + 60 + 110 = 260 (°)\nSố đo của góc thứ tư là:\n360 - 260 = 100 (°)\nVì 90° < 100° < 180° nên góc thứ tư là góc tù.\nĐáp số: 100°; là góc tù.",
                       "100°; là góc tù", 5, 1.5),
            make_essay(6, "Cho biết một góc nhọn và một góc vuông có tổng số đo bằng 135°. Hỏi số đo của góc nhọn đó bằng bao nhiêu độ?",
                       "Lời giải:\nSố đo của góc nhọn đó là:\n135 - 90 = 45 (°)\nĐáp số: 45°.",
                       "45°", 4, 1.0)
        ]
    }

    exams["th4_b9_test2"] = {
        "id": "th4_b9_test2",
        "lessonId": "th4_b9",
        "lessonNum": 9,
        "testNum": 2,
        "title": "Bài 9: Luyện tập chung Chủ đề 2 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 2",
        "chapter": "Chủ đề 2: Góc và đơn vị đo góc",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình vuông có tất cả bao nhiêu góc vuông?", [
                "1 góc vuông",
                "2 góc vuông",
                "3 góc vuông",
                "4 góc vuông"
            ], 3, "Hình vuông có đúng 4 góc vuông ở 4 đỉnh."),
            make_mc(2, "Số đo của góc tù nào sau đây là nhỏ nhất?", [
                "95°",
                "110°",
                "125°",
                "150°"
            ], 0, "Trong các số đo trên, 95° là số bé nhất và vẫn lớn hơn 90° nên là góc tù nhỏ nhất."),
            make_mc(3, "Góc tạo bởi kim giờ và kim phút lúc 8 giờ đúng có số đo là bao nhiêu độ (tính theo góc bé hơn hoặc bằng góc bẹt)?", [
                "90°",
                "120°",
                "150°",
                "180°"
            ], 1, "Từ số 8 đến số 12 có 4 khoảng giờ: 30° x 4 = 120°."),
            make_mc(4, "Một góc bẹt bị chia bởi một tia thành hai góc, trong đó có một góc bằng 60°. Góc còn lại là:", [
                "Góc nhọn 30°",
                "Góc vuông 90°",
                "Góc tù 120°",
                "Góc tù 150°"
            ], 2, "Góc còn lại có số đo: 180° - 60° = 120° (là góc tù)."),
            make_mc(5, "Đo góc bằng thước đo độ, ta cần đặt tâm của thước đo góc trùng với điểm nào?", [
                "Điểm bất kì trên cạnh thứ nhất",
                "Điểm bất kì trên cạnh thứ hai",
                "Đỉnh của góc",
                "Điểm nằm ngoài góc"
            ], 2, "Quy tắc đo góc: đặt tâm của thước trùng với đỉnh của góc."),
            make_mc(6, "Trong bốn góc sau: 30°, 85°, 90°, 135°, có bao nhiêu góc nhọn?", [
                "1 góc",
                "2 góc",
                "3 góc",
                "4 góc"
            ], 1, "Có 2 góc nhọn là 30° và 85° (đều bé hơn 90°).")
        ],
        "part2": [
            make_essay(1, "Hãy nêu số đo của góc vuông, góc bẹt và mối quan hệ giữa góc bẹt với góc vuông.",
                       "Lời giải:\n- Góc vuông có số đo bằng 90°.\n- Góc bẹt có số đo bằng 180°.\n- Mối quan hệ: Góc bẹt có số đo gấp đôi số đo của góc vuông (180° = 90° x 2).\nĐáp số: Góc vuông 90°, góc bẹt 180°; góc bẹt gấp đôi góc vuông.",
                       "Góc vuông 90°, góc bẹt 180°; gấp đôi góc vuông", 4, 1.0),
            make_essay(2, "Một góc đỉnh O có số đo 160°. Kẻ tia chia góc đó thành hai góc bằng nhau. Hỏi mỗi góc tạo thành có số đo là bao nhiêu và là góc gì?",
                       "Lời giải:\nSố đo của mỗi góc tạo thành là:\n160 : 2 = 80 (°)\nVì 80° < 90° nên mỗi góc tạo thành là góc nhọn.\nĐáp số: 80°; là góc nhọn.",
                       "80°; là góc nhọn", 4, 1.0),
            make_essay(3, "Bác thợ hàn ghép hai thanh kim loại tạo thành góc nhọn 50°. Sau đó bác hàn thêm một góc vuông 90° kề liền với góc nhọn đó. Hỏi tổng số đo hai góc ghép lại bằng bao nhiêu độ và tạo thành loại góc gì?",
                       "Lời giải:\nTổng số đo hai góc ghép lại là:\n50 + 90 = 140 (°)\nVì 90° < 140° < 180° nên góc ghép lại tạo thành một góc tù.\nĐáp số: 140°; tạo thành góc tù.",
                       "140°; tạo thành góc tù", 4, 1.0),
            make_essay(4, "Một nhóm học sinh làm mô hình ngôi nhà bằng que tính. Phần mái nhà tạo thành một góc tù có số đo 120°. Khi lắp thêm ống khói thẳng đứng vuông góc với mặt sàn ngang (tạo góc 90°), các bạn đo được góc giữa ống khói và mái nghiêng là một góc nhọn. Biết góc nhọn đó bằng một nửa hiệu giữa góc mái nhà và góc ống khói. Hãy tính góc nhọn đó.",
                       "Lời giải:\nHiệu giữa góc mái nhà và góc vuông ống khói là:\n120 - 90 = 30 (°)\nSố đo của góc nhọn đó là:\n30 : 2 = 15 (°)\nĐáp số: 15°.",
                       "15°", 5, 1.5),
            make_essay(5, "Tại ngã tư đường, con đường thứ nhất và con đường thứ hai tạo thành góc 75°. Con đường thứ hai và con đường thứ ba tạo thành góc 85°. Biết cả ba con đường cùng nằm trên một nửa mặt phẳng và chung điểm giao O tạo thành một góc lớn. Hãy tính số đo của góc lớn đó và cho biết đó là góc gì.",
                       "Lời giải:\nSố đo của góc lớn tạo bởi con đường thứ nhất và thứ ba là:\n75 + 85 = 160 (°)\nVì 90° < 160° < 180° nên đó là góc tù.\nĐáp số: 160°; là góc tù.",
                       "160°; là góc tù", 5, 1.5),
            make_essay(6, "Một góc nhọn có số đo bằng 1/3 số đo của một góc bẹt. Tính số đo của góc nhọn đó.",
                       "Lời giải:\nGóc bẹt có số đo là 180°.\nSố đo của góc nhọn đó là:\n180 x 1/3 = 60 (°)\nĐáp số: 60°.",
                       "60°", 4, 1.0)
        ]
    }

    exams["th4_b9_test3"] = {
        "id": "th4_b9_test3",
        "lessonId": "th4_b9",
        "lessonNum": 9,
        "testNum": 3,
        "title": "Bài 9: Luyện tập chung Chủ đề 2 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 2",
        "chapter": "Chủ đề 2: Góc và đơn vị đo góc",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một góc lớn hơn 90° nhưng nhỏ hơn 180° được gọi là:", [
                "Góc bẹt",
                "Góc tù",
                "Góc nhọn",
                "Góc vuông"
            ], 1, "Đó chính là định nghĩa của góc tù."),
            make_mc(2, "Khi mở rộng một chiếc quạt giấy xòe tròn hoàn toàn tạo thành một đường thẳng, góc tạo bởi hai nan ngoài cùng là góc gì?", [
                "Góc nhọn",
                "Góc vuông",
                "Góc tù",
                "Góc bẹt"
            ], 3, "Hai nan ngoài cùng thẳng hàng tạo thành góc bẹt (180°)."),
            make_mc(3, "Góc tạo bởi kim phút và kim giờ lúc 7 giờ đúng (tính góc bé hơn) có số đo là bao nhiêu độ?", [
                "120°",
                "150°",
                "180°",
                "210°"
            ], 1, "Từ số 7 đến số 12 là 5 khoảng giờ: 30° x 5 = 150°."),
            make_mc(4, "Một tam giác có 1 góc bằng 90°, 1 góc bằng 30°. Góc còn lại có số đo là bao nhiêu độ? (Biết tổng ba góc của tam giác là 180°)", [
                "30°",
                "45°",
                "60°",
                "90°"
            ], 2, "Góc còn lại: 180° - (90° + 30°) = 60°."),
            make_mc(5, "Nếu gấp đôi một góc nhọn 45° ta sẽ được:", [
                "Một góc nhọn",
                "Một góc vuông",
                "Một góc tù",
                "Một góc bẹt"
            ], 1, "45° x 2 = 90° (chính là một góc vuông)."),
            make_mc(6, "Trong một hình chữ nhật, có tất cả bao nhiêu cặp cạnh vuông góc với nhau?", [
                "2 cặp",
                "3 cặp",
                "4 cặp",
                "8 cặp"
            ], 2, "Hình chữ nhật có 4 góc vuông ở 4 đỉnh nên có 4 cặp cạnh vuông góc với nhau.")
        ],
        "part2": [
            make_essay(1, "Vẽ một góc đỉnh A có hai cạnh AB và AC. Hãy chỉ rõ đỉnh, cạnh và nêu điều kiện để góc đó là một góc nhọn.",
                       "Lời giải:\n- Đỉnh của góc là: Điểm A.\n- Hai cạnh của góc là: Cạnh AB và cạnh AC.\n- Điều kiện để góc đỉnh A là góc nhọn: Số đo của góc phải lớn hơn 0° và bé hơn 90°.\nĐáp số: Đỉnh A; hai cạnh AB, AC; số đo lớn hơn 0° và bé hơn 90°.",
                       "Đỉnh A; cạnh AB, AC; lớn hơn 0° và bé hơn 90°", 4, 1.0),
            make_essay(2, "Một chiếc compa có góc giữa hai chân là 30°. Bạn Nam mở rộng chân compa thêm một góc bằng đúng góc ban đầu. Hỏi sau khi mở rộng, góc giữa hai chân compa là góc gì và có số đo bao nhiêu độ?",
                       "Lời giải:\nSố đo của góc sau khi mở rộng là:\n30 + 30 = 60 (°)\nVì 60° < 90° nên đó vẫn là một góc nhọn.\nĐáp số: Góc nhọn, số đo 60°.",
                       "Góc nhọn, số đo 60°", 4, 1.0),
            make_essay(3, "Góc đỉnh O có số đo 150°. Bạn Hoa chia góc đó thành ba góc nhỏ bằng nhau. Hỏi mỗi góc nhỏ có số đo bao nhiêu độ và thuộc loại góc nào?",
                       "Lời giải:\nSố đo của mỗi góc nhỏ là:\n150 : 3 = 50 (°)\nVì 50° < 90° nên mỗi góc nhỏ là một góc nhọn.\nĐáp số: 50°; là góc nhọn.",
                       "50°; là góc nhọn", 4, 1.0),
            make_essay(4, "Một người làm vườn đo góc nghiêng của thân cây dừa so với mặt đất nằm ngang được một góc nhọn 65°. Để chống đổ, người đó dùng cọc chống vuông góc với thân cây dừa tại điểm đỡ (tạo thành góc 90°). Hỏi góc tạo bởi cọc chống và mặt đất dốc phía bên kia là bao nhiêu độ nếu biết tổng hai góc đó với góc nghiêng là 180°?",
                       "Lời giải:\nTổng số đo của góc vuông và góc nghiêng là:\n90 + 65 = 155 (°)\nSố đo của góc còn lại là:\n180 - 155 = 25 (°)\nĐáp số: 25°.",
                       "25°", 5, 1.5),
            make_essay(5, "Ba góc xOy, yOz và zOt cùng kề nhau quanh đỉnh O nằm trên nửa mặt phẳng. Biết góc xOy = 35°, góc yOz = 55° và góc zOt là góc tù có số đo 100°. Hãy tính tổng số đo của ba góc đó và cho biết tổng số đo ba góc đó lớn hơn góc bẹt bao nhiêu độ.",
                       "Lời giải:\nTổng số đo của ba góc đó là:\n35 + 55 + 100 = 190 (°)\nTổng số đo ba góc lớn hơn góc bẹt số độ là:\n190 - 180 = 10 (°)\nĐáp số: 190°; lớn hơn góc bẹt 10°.",
                       "190°; lớn hơn góc bẹt 10°", 5, 1.5),
            make_essay(6, "Một góc tù lớn gấp 3 lần một góc nhọn 40°. Tính xem góc tù đó có số đo là bao nhiêu độ?",
                       "Lời giải:\nSố đo của góc tù đó là:\n40 x 3 = 120 (°)\nĐáp số: 120°.",
                       "120°", 4, 1.0)
        ]
    }

    return exams
