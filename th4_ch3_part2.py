# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 3: SỐ CÓ NHIỀU CHỮ SỐ (PHẦN 2: BÀI 14 ĐẾN BÀI 16) - TOÁN 4 KNTT
Gồm 3 bài học, mỗi bài có 3 đề kiểm tra độc lập (test1, test2, test3):
- Bài 14: So sánh các số có nhiều chữ số (th4_b14_test1, th4_b14_test2, th4_b14_test3)
- Bài 15: Làm quen với dãy số tự nhiên (th4_b15_test1, th4_b15_test2, th4_b15_test3)
- Bài 16: Luyện tập chung Chủ đề 3 (th4_b16_test1, th4_b16_test2, th4_b16_test3)
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

def get_part2_exams():
    exams = {}

    # =========================================================================
    # BÀI 14: SO SÁNH CÁC SỐ CÓ NHIỀU CHỮ SỐ
    # =========================================================================
    exams["th4_b14_test1"] = {
        "id": "th4_b14_test1",
        "lessonId": "th4_b14",
        "lessonNum": 14,
        "testNum": 1,
        "title": "Bài 14: So sánh các số có nhiều chữ số - Đề số 1",
        "topic": "So sánh các số có nhiều chữ số",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Trong hai số tự nhiên có số chữ số khác nhau, số nào lớn hơn?", [
                "Số có ít chữ số hơn",
                "Số có nhiều chữ số hơn",
                "Hai số bằng nhau",
                "Tùy vào chữ số đầu tiên"
            ], 1, "Số nào có nhiều chữ số hơn thì lớn hơn."),
            make_mc(2, "Điền dấu thích hợp: 899 999 ... 1 000 000.", [
                "<",
                ">",
                "=",
                "Không so sánh được"
            ], 0, "899 999 có 6 chữ số, 1 000 000 có 7 chữ số nên 899 999 < 1 000 000."),
            make_mc(3, "So sánh hai số 452 718 và 452 817:", [
                "452 718 > 452 817",
                "452 718 = 452 817",
                "452 718 < 452 817",
                "Không có dấu phù hợp"
            ], 2, "Các chữ số hàng trăm nghìn, chục nghìn, nghìn bằng nhau; hàng trăm có 7 < 8 nên 452 718 < 452 817."),
            make_mc(4, "Trong các số: 384 150, 384 510, 381 450, 385 140, số lớn nhất là:", [
                "384 150",
                "384 510",
                "381 450",
                "385 140"
            ], 3, "So sánh hàng nghìn: 385 140 có hàng nghìn là 5 lớn nhất."),
            make_mc(5, "Tìm chữ số x thích hợp để: 567 8x2 < 567 812.", [
                "x = 0",
                "x = 1",
                "x = 2",
                "x = 9"
            ], 0, "So sánh hàng chục: x < 1 nên x = 0."),
            make_mc(6, "Sắp xếp các số: 120 000, 95 000, 102 000 theo thứ tự từ bé đến lớn là:", [
                "95 000; 120 000; 102 000",
                "95 000; 102 000; 120 000",
                "120 000; 102 000; 95 000",
                "102 000; 95 000; 120 000"
            ], 1, "95 000 (5 chữ số) < 102 000 < 120 000.")
        ],
        "part2": [
            make_essay(1, "Điền dấu thích hợp (>, <, =) vào chỗ chấm:\na) 615 284 ... 615 824\nb) 9 999 999 ... 10 000 000",
                       "Lời giải:\na) Hàng trăm nghìn, chục nghìn bằng nhau; hàng trăm: 2 < 8, nên 615 284 < 615 824.\nb) Số 9 999 999 có 7 chữ số, số 10 000 000 có 8 chữ số, nên 9 999 999 < 10 000 000.\nĐáp số: a) < ; b) < .",
                       "a) < ; b) <", 4, 1.0),
            make_essay(2, "Cho bốn số: 728 500; 782 500; 725 800; 785 200. Hãy:\na) Sắp xếp các số trên theo thứ tự từ bé đến lớn.\nb) Chỉ ra số lớn nhất và số bé nhất trong bốn số đó.",
                       "Lời giải:\na) So sánh các số:\n725 800 < 728 500 < 782 500 < 785 200.\nThứ tự từ bé đến lớn: 725 800; 728 500; 782 500; 785 200.\nb) Số bé nhất là: 725 800; Số lớn nhất là: 785 200.\nĐáp số: a) 725 800; 728 500; 782 500; 785 200; b) Bé nhất: 725 800, Lớn nhất: 785 200.",
                       "a) 725 800; 728 500; 782 500; 785 200; b) Bé nhất: 725 800, Lớn nhất: 785 200", 4, 1.0),
            make_essay(3, "Bảng dưới đây thống kê số lượng sách bán được của ba nhà sách trong một năm:\n- Nhà sách Tuổi Trẻ: 425 600 cuốn.\n- Nhà sách Tri Thức: 452 000 cuốn.\n- Nhà sách Hoa Sen: 425 850 cuốn.\nHỏi nhà sách nào bán được nhiều sách nhất và nhà sách nào bán được ít sách nhất?",
                       "Lời giải:\nSo sánh số lượng sách:\n425 600 < 425 850 < 452 000.\nDo đó:\n- Nhà sách Tri Thức bán được nhiều sách nhất (452 000 cuốn).\n- Nhà sách Tuổi Trẻ bán được ít sách nhất (425 600 cuốn).\nĐáp số: Nhiều nhất: Nhà sách Tri Thức; Ít nhất: Nhà sách Tuổi Trẻ.",
                       "Nhiều nhất: Tri Thức; Ít nhất: Tuổi Trẻ", 4, 1.0),
            make_essay(4, "Một trang trại nuôi bò sữa có bốn khu A, B, C, D sản xuất được sản lượng sữa trong năm lần lượt là: 318 400 lít, 325 100 lít, 318 950 lít, 324 800 lít. Em hãy:\na) Sắp xếp các khu theo thứ tự sản lượng sữa từ nhiều nhất đến ít nhất.\nb) Tính hiệu sản lượng giữa khu nhiều nhất và khu ít nhất.",
                       "Lời giải:\na) So sánh: 325 100 > 324 800 > 318 950 > 318 400.\nThứ tự các khu từ nhiều nhất đến ít nhất: Khu B, Khu D, Khu C, Khu A.\nb) Khu nhiều nhất là Khu B (325 100 l), khu ít nhất là Khu A (318 400 l).\nHiệu sản lượng là:\n325 100 - 318 400 = 6 700 (lít)\nĐáp số: a) Khu B, D, C, A; b) 6 700 lít.",
                       "a) B, D, C, A; b) 6 700 lít", 5, 1.5),
            make_essay(5, "Tìm chữ số thích hợp thay cho dấu * để:\na) 83* 520 > 838 520\nb) 459 280 = 45* 280",
                       "Lời giải:\na) Để 83* 520 > 838 520, các hàng trăm nghìn và chục nghìn đã bằng nhau (8 và 3), hàng trăm, chục, đơn vị bằng nhau, nên chữ số hàng nghìn * phải lớn hơn 8. Vậy * = 9.\nb) Để hai số bằng nhau thì chữ số ở cùng hàng phải giống nhau. Do đó * = 9.\nĐáp số: a) * = 9; b) * = 9.",
                       "a) * = 9; b) * = 9", 5, 1.5),
            make_essay(6, "Viết số tự nhiên lớn nhất có sáu chữ số khác nhau và số tự nhiên bé nhất có sáu chữ số khác nhau rồi so sánh hai số đó.",
                       "Lời giải:\n- Số tự nhiên lớn nhất có sáu chữ số khác nhau là: 987 654.\n- Số tự nhiên bé nhất có sáu chữ số khác nhau là: 102 345.\nSo sánh: 987 654 > 102 345.\nĐáp số: 987 654 > 102 345.",
                       "987 654 > 102 345", 4, 1.0)
        ]
    }

    exams["th4_b14_test2"] = {
        "id": "th4_b14_test2",
        "lessonId": "th4_b14",
        "lessonNum": 14,
        "testNum": 2,
        "title": "Bài 14: So sánh các số có nhiều chữ số - Đề số 2",
        "topic": "So sánh các số có nhiều chữ số",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "So sánh hai số: 1 200 000 và 980 000.", [
                "1 200 000 > 980 000",
                "1 200 000 < 980 000",
                "1 200 000 = 980 000",
                "Không so sánh được"
            ], 0, "1 200 000 có 7 chữ số > 980 000 có 6 chữ số."),
            make_mc(2, "Trong các số: 541 230, 541 320, 514 320, 542 130, số bé nhất là:", [
                "541 230",
                "541 320",
                "514 320",
                "542 130"
            ], 2, "514 320 có hàng chục nghìn là 1 bé nhất."),
            make_mc(3, "Điền dấu thích hợp: 700 000 + 40 000 + 8 ... 740 008.", [
                ">",
                "<",
                "=",
                "Không có dấu"
            ], 2, "700 000 + 40 000 + 8 = 740 008, nên ta điền dấu '='."),
            make_mc(4, "Có bao nhiêu số tự nhiên x có 6 chữ số thỏa mãn: 999 997 < x < 1 000 000?", [
                "1 số",
                "2 số",
                "3 số",
                "4 số"
            ], 1, "Các số tự nhiên đó là 999 998 và 999 999. Có đúng 2 số."),
            make_mc(5, "Số liền trước của một số có 7 chữ số bất kì luôn:", [
                "Bé hơn số đó",
                "Lớn hơn số đó",
                "Bằng số đó",
                "Có đúng 6 chữ số"
            ], 0, "Số liền trước của một số tự nhiên luôn bé hơn số đó 1 đơn vị."),
            make_mc(6, "Dãy số nào dưới đây được xếp theo thứ tự giảm dần?", [
                "800 000; 850 000; 900 000",
                "920 000; 915 000; 910 000",
                "705 000; 710 000; 708 000",
                "100 000; 200 000; 300 000"
            ], 1, "920 000 > 915 000 > 910 000 là thứ tự giảm dần.")
        ],
        "part2": [
            make_essay(1, "Điền dấu (>, <, =) thích hợp vào chỗ chấm:\na) 450 000 + 50 000 ... 500 000\nb) 835 120 ... 835 099",
                       "Lời giải:\na) Ta có 450 000 + 50 000 = 500 000. Do đó: 500 000 = 500 000.\nb) So sánh các hàng: hàng trăm 1 > 0 nên 835 120 > 835 099.\nĐáp số: a) = ; b) > .",
                       "a) = ; b) >", 4, 1.0),
            make_essay(2, "Cho các số: 562 108; 526 801; 562 801; 526 108. Hãy sắp xếp các số theo thứ tự từ lớn đến bé.",
                       "Lời giải:\nSo sánh các số:\n562 801 > 562 108 > 526 801 > 526 108.\nVậy thứ tự từ lớn đến bé là:\n562 801; 562 108; 526 801; 526 108.\nĐáp số: 562 801; 562 108; 526 801; 526 108.",
                       "562 801; 562 108; 526 801; 526 108", 4, 1.0),
            make_essay(3, "Ba xã vùng cao trồng cây gây rừng trong mùa xuân:\n- Xã A trồng được: 115 400 cây.\n- Xã B trồng được: 118 200 cây.\n- Xã C trồng được: 114 900 cây.\nHỏi xã nào trồng được nhiều cây nhất? Xã nào trồng được ít cây nhất?",
                       "Lời giải:\nSo sánh số cây trồng của ba xã:\n114 900 < 115 400 < 118 200.\nDo đó:\n- Xã B trồng được nhiều cây nhất (118 200 cây).\n- Xã C trồng được ít cây nhất (114 900 cây).\nĐáp số: Nhiều nhất: Xã B; Ít nhất: Xã C.",
                       "Nhiều nhất: Xã B; Ít nhất: Xã C", 4, 1.0),
            make_essay(4, "Một cửa hàng ô tô có giá bán của bốn mẫu xe như sau:\n- Xe Alfa: 725 000 000 đồng\n- Xe Beta: 699 000 000 đồng\n- Xe Gama: 750 000 000 đồng\n- Xe Delta: 720 000 000 đồng\nEm hãy:\na) Xếp tên các mẫu xe theo thứ tự giá tiền từ rẻ nhất đến đắt nhất.\nb) Tính số tiền mẫu xe đắt nhất đắt hơn mẫu xe rẻ nhất.",
                       "Lời giải:\na) So sánh giá tiền: 699 000 000 < 720 000 000 < 725 000 000 < 750 000 000.\nThứ tự từ rẻ nhất đến đắt nhất: Xe Beta, Xe Delta, Xe Alfa, Xe Gama.\nb) Xe đắt nhất là Gama (750 000 000 đ), xe rẻ nhất là Beta (699 000 000 đ).\nHiệu số tiền là:\n750 000 000 - 699 000 000 = 51 000 000 (đồng)\nĐáp số: a) Beta, Delta, Alfa, Gama; b) 51 000 000 đồng.",
                       "a) Beta, Delta, Alfa, Gama; b) 51 000 000 đồng", 5, 1.5),
            make_essay(5, "Tìm chữ số thích hợp điền vào ô trống [ ] để được khẳng định đúng:\na) 63[ ] 450 < 631 450\nb) 987 500 < 98[ ] 500",
                       "Lời giải:\na) Để 63[ ] 450 < 631 450 thì chữ số hàng nghìn [ ] phải bé hơn 1. Do đó [ ] = 0.\nb) Để 987 500 < 98[ ] 500 thì chữ số hàng nghìn [ ] phải lớn hơn 7. Do đó [ ] có thể là 8 hoặc 9.\nĐáp số: a) [ ] = 0; b) [ ] = 8 hoặc 9.",
                       "a) [ ] = 0; b) [ ] = 8 hoặc 9", 5, 1.5),
            make_essay(6, "So sánh số lớn nhất có năm chữ số với số bé nhất có sáu chữ số.",
                       "Lời giải:\n- Số lớn nhất có năm chữ số là: 99 999.\n- Số bé nhất có sáu chữ số là: 100 000.\nVì số có 5 chữ số luôn bé hơn số có 6 chữ số nên: 99 999 < 100 000.\nĐáp số: 99 999 < 100 000.",
                       "99 999 < 100 000", 4, 1.0)
        ]
    }

    exams["th4_b14_test3"] = {
        "id": "th4_b14_test3",
        "lessonId": "th4_b14",
        "lessonNum": 14,
        "testNum": 3,
        "title": "Bài 14: So sánh các số có nhiều chữ số - Đề số 3",
        "topic": "So sánh các số có nhiều chữ số",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số nào dưới đây lớn hơn số 850 000?", [
                "849 999",
                "850 000",
                "850 001",
                "805 000"
            ], 2, "850 001 lớn hơn 850 000 một đơn vị."),
            make_mc(2, "Cho ba số: A = 642 000, B = 641 999, C = 642 005. Thứ tự từ bé đến lớn là:", [
                "A, B, C",
                "B, A, C",
                "C, A, B",
                "B, C, A"
            ], 1, "641 999 < 642 000 < 642 005 -> Thứ tự là B, A, C."),
            make_mc(3, "Điền dấu thích hợp: 32 000 000 ... 31 999 999.", [
                ">",
                "<",
                "=",
                "Không so sánh được"
            ], 0, "Cả hai đều có 8 chữ số; hàng triệu có 32 > 31 nên 32 000 000 > 31 999 999."),
            make_mc(4, "Trong các số sau, số nào bé hơn 100 000?", [
                "100 001",
                "99 999",
                "100 000",
                "102 000"
            ], 1, "99 999 có 5 chữ số < 100 000 có 6 chữ số."),
            make_mc(5, "Tìm số chẵn lớn nhất có sáu chữ số khác nhau trong các số sau:", [
                "987 654",
                "987 653",
                "987 655",
                "999 998"
            ], 0, "987 654 có các chữ số khác nhau và tận cùng bằng 4 (số chẵn lớn nhất có 6 chữ số khác nhau)."),
            make_mc(6, "Tìm x biết: 789 123 < x < 789 125 với x là số tự nhiên.", [
                "789 122",
                "789 124",
                "789 126",
                "789 125"
            ], 1, "Số tự nhiên nằm giữa 789 123 và 789 125 là 789 124.")
        ],
        "part2": [
            make_essay(1, "Điền dấu (>, <, =) thích hợp vào chỗ chấm:\na) 200 000 + 80 000 + 5 000 ... 285 000\nb) 512 340 ... 512 304",
                       "Lời giải:\na) 200 000 + 80 000 + 5 000 = 285 000. Do đó điền dấu '='.\nb) Hàng chục: 4 > 0, nên 512 340 > 512 304.\nĐáp số: a) = ; b) > .",
                       "a) = ; b) >", 4, 1.0),
            make_essay(2, "Xếp các số sau theo thứ tự từ bé đến lớn: 405 120; 450 120; 405 210; 450 021.",
                       "Lời giải:\nSo sánh các số:\n405 120 < 405 210 < 450 021 < 450 120.\nVậy thứ tự từ bé đến lớn là:\n405 120; 405 210; 450 021; 450 120.\nĐáp số: 405 120; 405 210; 450 021; 450 120.",
                       "405 120; 405 210; 450 021; 450 120", 4, 1.0),
            make_essay(3, "Bốn bạn An, Bình, Cường, Dũng sưu tầm tem. Số tem của mỗi bạn lần lượt là: 1 250 con tem, 1 520 con tem, 1 052 con tem, 1 205 con tem. Hỏi bạn nào có nhiều tem nhất và bạn nào có ít tem nhất?",
                       "Lời giải:\nSo sánh số tem của bốn bạn:\n1 052 < 1 205 < 1 250 < 1 520.\nDo đó:\n- Bạn Bình có nhiều tem nhất (1 520 con tem).\n- Bạn Cường có ít tem nhất (1 052 con tem).\nĐáp số: Nhiều nhất: Bình; Ít nhất: Cường.",
                       "Nhiều nhất: Bình; Ít nhất: Cường", 4, 1.0),
            make_essay(4, "Một công ty có kế hoạch xuất khẩu hải sản trong 3 quý như sau: Quý 1 là 320 000 kg, Quý 2 là 295 000 kg, Quý 3 là 340 000 kg. Em hãy:\na) So sánh sản lượng của Quý 1 với Quý 2 và Quý 3.\nb) Tính tổng sản lượng cả ba quý và kiểm tra xem tổng đó có lớn hơn 950 000 kg không?",
                       "Lời giải:\na) Ta có: 295 000 kg < 320 000 kg < 340 000 kg. Vậy Quý 1 nhiều hơn Quý 2 nhưng ít hơn Quý 3.\nb) Tổng sản lượng cả ba quý là:\n320 000 + 295 000 + 340 000 = 955 000 (kg)\nVì 955 000 > 950 000 nên tổng sản lượng lớn hơn 950 000 kg.\nĐáp số: a) Quý 2 < Quý 1 < Quý 3; b) 955 000 kg; lớn hơn 950 000 kg.",
                       "a) Quý 2 < Quý 1 < Quý 3; b) 955 000 kg (lớn hơn)", 5, 1.5),
            make_essay(5, "Tìm số tự nhiên x có sáu chữ số biết rằng x tròn chục nghìn và thỏa mãn: 520 000 < x < 560 000 và x có chữ số hàng chục nghìn là số lẻ.",
                       "Lời giải:\nx là số tròn chục nghìn nằm trong khoảng từ 520 000 đến 560 000 nên x có thể là: 530 000; 540 000; 550 000.\nChữ số hàng chục nghìn là số lẻ nên chỉ có 3 và 5 là số lẻ.\nVậy các số x thỏa mãn là: 530 000 và 550 000.\nĐáp số: 530 000 và 550 000.",
                       "530 000 và 550 000", 5, 1.5),
            make_essay(6, "Từ bốn chữ số 0, 3, 6, 9 hãy viết số lớn nhất và số bé nhất có bốn chữ số khác nhau rồi tính hiệu của hai số đó.",
                       "Lời giải:\n- Số lớn nhất có bốn chữ số khác nhau từ các chữ số trên là: 9 630.\n- Số bé nhất có bốn chữ số khác nhau từ các chữ số trên là: 3 069.\nHiệu của hai số đó là:\n9 630 - 3 069 = 6 561\nĐáp số: 6 561.",
                       "6 561", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 15: LÀM QUEN VỚI DÃY SỐ TỰ NHIÊN
    # =========================================================================
    exams["th4_b15_test1"] = {
        "id": "th4_b15_test1",
        "lessonId": "th4_b15",
        "lessonNum": 15,
        "testNum": 1,
        "title": "Bài 15: Làm quen với dãy số tự nhiên - Đề số 1",
        "topic": "Làm quen với dãy số tự nhiên",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số tự nhiên bé nhất trong dãy số tự nhiên là số nào?", [
                "0",
                "1",
                "-1",
                "Không có"
            ], 0, "Số tự nhiên bé nhất là 0."),
            make_mc(2, "Khẳng định nào sau đây là ĐÚNG về số tự nhiên lớn nhất?", [
                "Là số 1 000 000",
                "Là số 999 999 999",
                "Không có số tự nhiên lớn nhất",
                "Là số 1 tỉ"
            ], 2, "Dãy số tự nhiên kéo dài vô tận, không có số tự nhiên lớn nhất."),
            make_mc(3, "Hai số tự nhiên liên tiếp hơn hoặc kém nhau bao nhiêu đơn vị?", [
                "0 đơn vị",
                "1 đơn vị",
                "2 đơn vị",
                "10 đơn vị"
            ], 1, "Hai số tự nhiên liên tiếp hơn kém nhau đúng 1 đơn vị."),
            make_mc(4, "Số liền sau của số 499 999 là số nào?", [
                "499 998",
                "500 000",
                "500 001",
                "499 990"
            ], 1, "499 999 + 1 = 500 000."),
            make_mc(5, "Số liền trước của số 1 000 000 là số nào?", [
                "999 999",
                "1 000 001",
                "99 999",
                "900 000"
            ], 0, "1 000 000 - 1 = 999 999."),
            make_mc(6, "Dãy số nào dưới đây là một phần của dãy số tự nhiên gồm các số lẻ liên tiếp?", [
                "1; 2; 3; 4; 5",
                "2; 4; 6; 8; 10",
                "1; 3; 5; 7; 9",
                "0; 1; 2; 3; 4"
            ], 2, "1, 3, 5, 7, 9 là các số lẻ liên tiếp.")
        ],
        "part2": [
            make_essay(1, "Viết 5 số tự nhiên liên tiếp bắt đầu từ số 198.",
                       "Lời giải:\nNăm số tự nhiên liên tiếp là:\n198, 199, 200, 201, 202.\nĐáp số: 198, 199, 200, 201, 202.",
                       "198, 199, 200, 201, 202", 4, 1.0),
            make_essay(2, "Tìm số liền trước và số liền sau của mỗi số sau:\na) 250 000.\nb) 999 999.",
                       "Lời giải:\na) Với số 250 000:\n- Số liền trước là: 250 000 - 1 = 249 999.\n- Số liền sau là: 250 000 + 1 = 250 001.\nb) Với số 999 999:\n- Số liền trước là: 999 999 - 1 = 999 998.\n- Số liền sau là: 999 999 + 1 = 1 000 000.\nĐáp số: a) 249 999 và 250 001; b) 999 998 và 1 000 000.",
                       "a) 249 999 và 250 001; b) 999 998 và 1 000 000", 4, 1.0),
            make_essay(3, "Viết ba số chẵn liên tiếp biết số chẵn bé nhất là 2 024.",
                       "Lời giải:\nBa số chẵn liên tiếp hơn kém nhau 2 đơn vị:\n- Số thứ nhất là: 2 024.\n- Số thứ hai là: 2 024 + 2 = 2 026.\n- Số thứ ba là: 2 026 + 2 = 2 028.\nĐáp số: 2 024, 2 026, 2 028.",
                       "2 024, 2 026, 2 028", 4, 1.0),
            make_essay(4, "Một người đánh số trang của một cuốn sổ tay nhỏ từ trang 1 đến trang 50. Em hãy:\na) Cho biết cuốn sổ có bao nhiêu trang có một chữ số?\nb) Cuốn sổ có bao nhiêu trang có hai chữ số?\nc) Tính tổng số lượt chữ số cần dùng để đánh số toàn bộ các trang cuốn sổ đó.",
                       "Lời giải:\na) Các trang có một chữ số từ trang 1 đến trang 9: có 9 trang.\nb) Các trang có hai chữ số từ trang 10 đến trang 50: có 50 - 10 + 1 = 41 trang.\nc) Tổng số chữ số cần dùng là:\n9 x 1 + 41 x 2 = 9 + 82 = 91 (chữ số)\nĐáp số: a) 9 trang; b) 41 trang; c) 91 chữ số.",
                       "a) 9 trang; b) 41 trang; c) 91 chữ số", 5, 1.5),
            make_essay(5, "Tìm ba số tự nhiên liên tiếp có tổng bằng 300.",
                       "Lời giải:\nCách 1: Ba số tự nhiên liên tiếp thì số ở giữa chính là trung bình cộng của ba số.\nSố thứ hai (ở giữa) là:\n300 : 3 = 100\nSố thứ nhất (liền trước) là:\n100 - 1 = 99\nSố thứ ba (liền sau) là:\n100 + 1 = 101\nBa số đó là: 99, 100, 101.\nĐáp số: 99, 100, 101.",
                       "99, 100, 101", 5, 1.5),
            make_essay(6, "Có bao nhiêu số tự nhiên có ba chữ số?",
                       "Lời giải:\nCác số tự nhiên có ba chữ số bắt đầu từ 100 và kết thúc ở 999.\nSố lượng các số tự nhiên có ba chữ số là:\n999 - 100 + 1 = 900 (số)\nĐáp số: 900 số.",
                       "900 số", 4, 1.0)
        ]
    }

    exams["th4_b15_test2"] = {
        "id": "th4_b15_test2",
        "lessonId": "th4_b15",
        "lessonNum": 15,
        "testNum": 2,
        "title": "Bài 15: Làm quen với dãy số tự nhiên - Đề số 2",
        "topic": "Làm quen với dãy số tự nhiên",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Trên tia số, gốc của tia số là điểm ứng với số nào?", [
                "Số 0",
                "Số 1",
                "Số 10",
                "Số 100"
            ], 0, "Gốc của tia số ứng với điểm 0."),
            make_mc(2, "Số nào dưới đây KHÔNG có số tự nhiên liền trước nó?", [
                "Số 0",
                "Số 1",
                "Số 10",
                "Số 100"
            ], 0, "Số 0 là số tự nhiên bé nhất nên không có số tự nhiên nào liền trước số 0."),
            make_mc(3, "Bớt 1 ở bất kì số tự nhiên nào khác 0 ta được:", [
                "Số liền sau của nó",
                "Số liền trước của nó",
                "Số bằng chính nó",
                "Số chẵn"
            ], 1, "Bớt 1 ở một số tự nhiên khác 0 ta được số tự nhiên liền trước nó."),
            make_mc(4, "Số liền sau của số tự nhiên a là:", [
                "a - 1",
                "a + 1",
                "a x 2",
                "a : 2"
            ], 1, "Thêm 1 vào số tự nhiên a ta được số liền sau là a + 1."),
            make_mc(5, "Hai số lẻ liên tiếp hơn kém nhau bao nhiêu đơn vị?", [
                "1 đơn vị",
                "2 đơn vị",
                "3 đơn vị",
                "4 đơn vị"
            ], 1, "Hai số lẻ liên tiếp hơn kém nhau 2 đơn vị."),
            make_mc(6, "Dãy số: 0, 1, 2, 3, 4, ... được gọi là:", [
                "Dãy số chẵn",
                "Dãy số lẻ",
                "Dãy số tự nhiên",
                "Dãy số tròn chục"
            ], 2, "Đó chính là dãy số tự nhiên.")
        ],
        "part2": [
            make_essay(1, "Viết 4 số lẻ liên tiếp bắt đầu từ số 101.",
                       "Lời giải:\nBốn số lẻ liên tiếp hơn kém nhau 2 đơn vị là:\n101, 103, 105, 107.\nĐáp số: 101, 103, 105, 107.",
                       "101, 103, 105, 107", 4, 1.0),
            make_essay(2, "Điền số thích hợp vào chỗ chấm để được dãy số tự nhiên liên tiếp:\na) 896, 897, ..., 899, ...\nb) ..., 1 000 000, 1 000 001, ...",
                       "Lời giải:\na) 896, 897, 898, 899, 900.\nb) 999 999, 1 000 000, 1 000 001, 1 000 002.\nĐáp số: a) 898, 900; b) 999 999, 1 000 002.",
                       "a) 898, 900; b) 999 999, 1 000 002", 4, 1.0),
            make_essay(3, "Cho ba số tự nhiên liên tiếp biết số lớn nhất là 1 001. Hãy tìm hai số còn lại và tính tổng của cả ba số đó.",
                       "Lời giải:\nSố lớn nhất là 1 001.\nSố thứ hai (liền trước 1 001) là: 1 001 - 1 = 1 000.\nSố thứ nhất (liền trước 1 000) là: 1 000 - 1 = 999.\nTổng của cả ba số là:\n999 + 1 000 + 1 001 = 3 000\nĐáp số: Hai số còn lại là 999 và 1 000; Tổng bằng 3 000.",
                       "999 và 1 000; Tổng bằng 3 000", 4, 1.0),
            make_essay(4, "Một dãy nhà gồm các ngôi nhà ở dãy số chẵn liên tiếp được đánh số từ nhà số 2 đến nhà số 40. Em hãy cho biết:\na) Dãy nhà đó có tất cả bao nhiêu ngôi nhà?\nb) Cần dùng tất cả bao nhiêu chữ số để gắn biển số nhà cho dãy nhà đó?",
                       "Lời giải:\na) Số lượng ngôi nhà trong dãy số chẵn liên tiếp từ 2 đến 40 là:\n(40 - 2) : 2 + 1 = 20 (ngôi nhà)\nb) Các nhà có 1 chữ số là: 2, 4, 6, 8 (gồm 4 nhà, dùng 4 chữ số).\nCác nhà có 2 chữ số từ 10 đến 40 là: 20 - 4 = 16 (nhà).\nSố chữ số cần dùng là:\n4 x 1 + 16 x 2 = 4 + 32 = 36 (chữ số)\nĐáp số: a) 20 ngôi nhà; b) 36 chữ số.",
                       "a) 20 ngôi nhà; b) 36 chữ số", 5, 1.5),
            make_essay(5, "Tìm hai số tự nhiên liên tiếp có tổng bằng 2 025.",
                       "Lời giải:\nHai số tự nhiên liên tiếp có hiệu bằng 1.\nSố bé là:\n(2 025 - 1) : 2 = 1 012\nSố lớn là:\n1 012 + 1 = 1 013\nĐáp số: 1 012 và 1 013.",
                       "1 012 và 1 013", 5, 1.5),
            make_essay(6, "Có bao nhiêu số chẵn có hai chữ số?",
                       "Lời giải:\nCác số chẵn có hai chữ số là dãy: 10, 12, 14, ..., 98.\nSố lượng các số chẵn có hai chữ số là:\n(98 - 10) : 2 + 1 = 45 (số)\nĐáp số: 45 số.",
                       "45 số", 4, 1.0)
        ]
    }

    exams["th4_b15_test3"] = {
        "id": "th4_b15_test3",
        "lessonId": "th4_b15",
        "lessonNum": 15,
        "testNum": 3,
        "title": "Bài 15: Làm quen với dãy số tự nhiên - Đề số 3",
        "topic": "Làm quen với dãy số tự nhiên",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Trong hệ thập phân, người ta dùng bao nhiêu chữ số để viết mọi số tự nhiên?", [
                "9 chữ số",
                "10 chữ số",
                "100 chữ số",
                "Vô số chữ số"
            ], 1, "Dùng đúng 10 chữ số: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9."),
            make_mc(2, "Số liền trước của số x + 1 là số nào? (với x là số tự nhiên khác 0)", [
                "x - 1",
                "x",
                "x + 2",
                "x + 1"
            ], 1, "Bớt 1 ở (x + 1) ta được số liền trước là x."),
            make_mc(3, "Số nào dưới đây là số tự nhiên?", [
                "0",
                "1/2",
                "2,5",
                "0,75"
            ], 0, "0 là số tự nhiên; các số còn lại là phân số hoặc số thập phân."),
            make_mc(4, "Có bao nhiêu số tự nhiên nằm giữa số 200 và số 210?", [
                "8 số",
                "9 số",
                "10 số",
                "11 số"
            ], 1, "Các số từ 201 đến 209 gồm: 209 - 201 + 1 = 9 số."),
            make_mc(5, "Một dãy số tự nhiên liên tiếp gồm 5 số, số ở giữa là 50. Số lớn nhất trong dãy là:", [
                "51",
                "52",
                "53",
                "54"
            ], 1, "Dãy số là 48, 49, 50, 51, 52. Số lớn nhất là 52."),
            make_mc(6, "Điểm biểu diễn số lớn hơn trên tia số nằm ở vị trí nào so với điểm biểu diễn số bé hơn?", [
                "Nằm ở bên phải",
                "Nằm ở bên trái",
                "Trùng nhau",
                "Nằm ở phía dưới"
            ], 0, "Trên tia số nằm ngang hướng sang phải, số lớn hơn nằm ở bên phải số bé hơn.")
        ],
        "part2": [
            make_essay(1, "Viết các số tự nhiên liên tiếp từ số 996 đến số 1 002.",
                       "Lời giải:\nCác số tự nhiên liên tiếp đó là:\n996, 997, 998, 999, 1 000, 1 001, 1 002.\nĐáp số: 996, 997, 998, 999, 1 000, 1 001, 1 002.",
                       "996, 997, 998, 999, 1 000, 1 001, 1 002", 4, 1.0),
            make_essay(2, "Viết số tự nhiên thích hợp vào chỗ chấm:\na) Số liền sau của số 789 999 là ...\nb) Số liền trước của số 300 000 là ...",
                       "Lời giải:\na) 789 999 + 1 = 790 000.\nb) 300 000 - 1 = 299 999.\nĐáp số: a) 790 000; b) 299 999.",
                       "a) 790 000; b) 299 999", 4, 1.0),
            make_essay(3, "Một vận động viên chạy bộ qua các cột mốc được đánh số tự nhiên liên tiếp. Bắt đầu từ cột mốc số 15 đến cột mốc số 45. Hỏi vận động viên đã chạy qua tất cả bao nhiêu cột mốc?",
                       "Lời giải:\nSố cột mốc vận động viên đã chạy qua là:\n45 - 15 + 1 = 31 (cột mốc)\nĐáp số: 31 cột mốc.",
                       "31 cột mốc", 4, 1.0),
            make_essay(4, "Một người thợ đánh số các thùng hàng theo dãy số lẻ liên tiếp: 1, 3, 5, ..., 59. Em hãy tính:\na) Có tất cả bao nhiêu thùng hàng được đánh số?\nb) Tính tổng các số ghi trên thùng hàng đầu tiên và thùng hàng cuối cùng.",
                       "Lời giải:\na) Số lượng thùng hàng là:\n(59 - 1) : 2 + 1 = 30 (thùng hàng)\nb) Thùng hàng đầu tiên ghi số 1, thùng cuối cùng ghi số 59.\nTổng số ghi trên hai thùng hàng đó là:\n1 + 59 = 60\nĐáp số: a) 30 thùng hàng; b) 60.",
                       "a) 30 thùng hàng; b) 60", 5, 1.5),
            make_essay(5, "Tìm bốn số tự nhiên liên tiếp có tổng bằng 206.",
                       "Lời giải:\nGọi bốn số tự nhiên liên tiếp là a, a + 1, a + 2, a + 3.\nTổng của bốn số là:\na + a + 1 + a + 2 + a + 3 = 4 x a + 6 = 206\n4 x a = 206 - 6 = 200\na = 200 : 4 = 50\nVậy bốn số đó là: 50, 51, 52, 53.\nĐáp số: 50, 51, 52, 53.",
                       "50, 51, 52, 53", 5, 1.5),
            make_essay(6, "Có bao nhiêu số tự nhiên có bốn chữ số?",
                       "Lời giải:\nCác số tự nhiên có bốn chữ số từ 1 000 đến 9 999.\nSố lượng các số là:\n9 999 - 1 000 + 1 = 9 000 (số)\nĐáp số: 9 000 số.",
                       "9 000 số", 4, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 16: LUYỆN TẬP CHUNG CHỦ ĐỀ 3
    # =========================================================================
    exams["th4_b16_test1"] = {
        "id": "th4_b16_test1",
        "lessonId": "th4_b16",
        "lessonNum": 16,
        "testNum": 1,
        "title": "Bài 16: Luyện tập chung Chủ đề 3 - Đề số 1",
        "topic": "Luyện tập chung Chủ đề 3",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 4 triệu, 5 trăm nghìn và 6 đơn vị viết là:", [
                "4 500 006",
                "4 050 006",
                "4 506 000",
                "450 006"
            ], 0, "Lớp triệu là 4, lớp nghìn là 500, lớp đơn vị là 006: 4 500 006."),
            make_mc(2, "Lớp triệu của số 325 814 000 gồm các chữ số:", [
                "8, 1, 4",
                "3, 2, 5",
                "0, 0, 0",
                "3, 8, 0"
            ], 1, "Lớp triệu gồm 3 trăm triệu, 2 chục triệu, 5 triệu: 3, 2, 5."),
            make_mc(3, "Làm tròn số 672 500 đến hàng trăm nghìn ta được số:", [
                "600 000",
                "670 000",
                "700 000",
                "680 000"
            ], 2, "Chữ số hàng chục nghìn là 7 >= 5 nên làm tròn lên thành 700 000."),
            make_mc(4, "Trong các số: 852 140, 852 410, 825 410, 854 210, số lớn nhất là:", [
                "852 140",
                "852 410",
                "825 410",
                "854 210"
            ], 3, "Hàng nghìn có 4 lớn nhất trong nhóm 85x nghìn -> 854 210 lớn nhất."),
            make_mc(5, "Số tự nhiên liền trước của số bé nhất có bảy chữ số là:", [
                "999 999",
                "1 000 001",
                "100 000",
                "9 999 999"
            ], 0, "Số bé nhất có 7 chữ số là 1 000 000. Liền trước là 999 999."),
            make_mc(6, "Giá trị của chữ số 9 trong số 29 450 123 là:", [
                "9 000",
                "90 000",
                "900 000",
                "9 000 000"
            ], 3, "Chữ số 9 ở hàng triệu nên có giá trị là 9 000 000.")
        ],
        "part2": [
            make_essay(1, "Viết và đọc các số sau:\na) Số gồm 7 trăm nghìn, 4 chục nghìn và 5 trăm.\nb) Số gồm 8 chục triệu, 3 triệu và 2 chục nghìn.",
                       "Lời giải:\na) Viết số: 740 500.\nĐọc số: Bảy trăm bốn mươi nghìn năm trăm.\nb) Viết số: 83 020 000.\nĐọc số: Tám mươi ba triệu không trăm hai mươi nghìn.\nĐáp số: a) 740 500; Bảy trăm bốn mươi nghìn năm trăm; b) 83 020 000; Tám mươi ba triệu không trăm hai mươi nghìn.",
                       "a) 740 500; b) 83 020 000", 4, 1.0),
            make_essay(2, "Cho số 948 215. Hãy làm tròn số này đến:\na) Hàng chục nghìn.\nb) Hàng trăm nghìn.",
                       "Lời giải:\na) Làm tròn đến hàng chục nghìn (hàng nghìn là 8 >= 5) ta được: 950 000.\nb) Làm tròn đến hàng trăm nghìn (hàng chục nghìn là 4 < 5) ta được: 900 000.\nĐáp số: a) 950 000; b) 900 000.",
                       "a) 950 000; b) 900 000", 4, 1.0),
            make_essay(3, "Bốn tỉnh miền núi có số cây lấy gỗ trồng được trong năm vừa qua như sau:\n- Tỉnh A: 520 000 cây\n- Tỉnh B: 485 000 cây\n- Tỉnh C: 540 000 cây\n- Tỉnh D: 492 000 cây\nHãy sắp xếp tên các tỉnh theo thứ tự số cây trồng được từ nhiều nhất đến ít nhất.",
                       "Lời giải:\nSo sánh số cây:\n540 000 > 520 000 > 492 000 > 485 000.\nVậy thứ tự các tỉnh từ nhiều nhất đến ít nhất là:\nTỉnh C, Tỉnh A, Tỉnh D, Tỉnh B.\nĐáp số: Tỉnh C, Tỉnh A, Tỉnh D, Tỉnh B.",
                       "Tỉnh C, Tỉnh A, Tỉnh D, Tỉnh B", 4, 1.0),
            make_essay(4, "Một công ty kinh doanh thiết bị văn phòng có doanh thu quý 1 là 350 000 000 đồng, quý 2 là 420 000 000 đồng, quý 3 đạt 480 000 000 đồng. Em hãy:\na) Tính tổng doanh thu của công ty trong ba quý đó.\nb) Làm tròn tổng doanh thu đó đến hàng trăm triệu.",
                       "Lời giải:\na) Tổng doanh thu của công ty trong ba quý là:\n350 000 000 + 420 000 000 + 480 000 000 = 1 250 000 000 (đồng)\nb) Làm tròn số 1 250 000 000 đến hàng trăm triệu:\nChữ số hàng trăm triệu là 2, chữ số hàng chục triệu là 5 (>= 5) nên ta làm tròn lên thành: 1 300 000 000 đồng (1 tỉ 300 triệu đồng).\nĐáp số: a) 1 250 000 000 đồng; b) 1 300 000 000 đồng.",
                       "a) 1 250 000 000 đồng; b) 1 300 000 000 đồng", 5, 1.5),
            make_essay(5, "Từ 6 thẻ số: 1, 0, 8, 4, 9, 2. Em hãy:\na) Lập số lớn nhất có 6 chữ số khác nhau.\nb) Lập số bé nhất có 6 chữ số khác nhau.\nc) Tính hiệu của hai số đó.",
                       "Lời giải:\na) Số lớn nhất có 6 chữ số khác nhau là: 984 210.\nb) Số bé nhất có 6 chữ số khác nhau là: 102 489.\nc) Hiệu của hai số đó là:\n984 210 - 102 489 = 881 721\nĐáp số: a) 984 210; b) 102 489; c) 881 721.",
                       "a) 984 210; b) 102 489; c) 881 721", 5, 1.5),
            make_essay(6, "Tìm số tự nhiên có ba chữ số biết rằng khi viết thêm chữ số 5 vào bên trái số đó ta được số mới gấp 9 lần số ban đầu.",
                       "Lời giải:\nGọi số cần tìm là abc (với a khác 0).\nKhi viết thêm chữ số 5 vào bên trái ta được số 5abc = 5 000 + abc.\nTheo đề bài: 5 000 + abc = 9 x abc\n5 000 = 8 x abc\nabc = 5 000 : 8 = 625\nVậy số đó là 625.\nĐáp số: 625.",
                       "625", 4, 1.0)
        ]
    }

    exams["th4_b16_test2"] = {
        "id": "th4_b16_test2",
        "lessonId": "th4_b16",
        "lessonNum": 16,
        "testNum": 2,
        "title": "Bài 16: Luyện tập chung Chủ đề 3 - Đề số 2",
        "topic": "Luyện tập chung Chủ đề 3",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số nào dưới đây có lớp triệu là 15 và lớp nghìn là 240?", [
                "15 240 000",
                "150 240 000",
                "15 024 000",
                "1 524 000"
            ], 0, "Lớp triệu: 15, lớp nghìn: 240, lớp đơn vị: 000 -> 15 240 000."),
            make_mc(2, "Số liền sau của số tự nhiên lớn nhất có sáu chữ số là:", [
                "1 000 000",
                "999 998",
                "100 000",
                "10 000 000"
            ], 0, "Số lớn nhất có 6 chữ số là 999 999. Liền sau là 1 000 000."),
            make_mc(3, "Làm tròn số 816 490 đến hàng trăm nghìn ta được:", [
                "800 000",
                "820 000",
                "900 000",
                "810 000"
            ], 0, "Hàng chục nghìn là 1 < 5 nên làm tròn xuống thành 800 000."),
            make_mc(4, "Trong số 743 952 018, chữ số thuộc hàng chục triệu là:", [
                "7",
                "4",
                "3",
                "9"
            ], 1, "Chữ số hàng chục triệu là 4."),
            make_mc(5, "Số tự nhiên liền trước của một số chẵn luôn là:", [
                "Số chẵn",
                "Số lẻ",
                "Số 0",
                "Số tròn chục"
            ], 1, "Số liền trước của số chẵn là số lẻ."),
            make_mc(6, "Cho: 450 000 + x = 1 000 000. Giá trị của x là:", [
                "450 000",
                "550 000",
                "650 000",
                "500 000"
            ], 1, "x = 1 000 000 - 450 000 = 550 000.")
        ],
        "part2": [
            make_essay(1, "Viết số tự nhiên thích hợp vào chỗ chấm:\na) 400 000 000 + 70 000 000 + 5 000 000 = ...\nb) 900 000 + 60 000 + 4 000 + 200 + 8 = ...",
                       "Lời giải:\na) 400 000 000 + 70 000 000 + 5 000 000 = 475 000 000.\nb) 900 000 + 60 000 + 4 000 + 200 + 8 = 964 208.\nĐáp số: a) 475 000 000; b) 964 208.",
                       "a) 475 000 000; b) 964 208", 4, 1.0),
            make_essay(2, "Cho dãy số: 315 000; 330 000; 345 000; ...; ... Hãy tìm quy luật và viết hai số tiếp theo của dãy số trên.",
                       "Lời giải:\nNhận xét: Mỗi số trong dãy bằng số đứng ngay trước nó cộng thêm 15 000.\nSố tiếp theo thứ nhất là:\n345 000 + 15 000 = 360 000\nSố tiếp theo thứ hai là:\n360 000 + 15 000 = 375 000\nĐáp số: 360 000 và 375 000.",
                       "360 000 và 375 000", 4, 1.0),
            make_essay(3, "Một thư viện thành phố thống kê số trang sách thiếu nhi đã đọc trong kì nghỉ hè là 875 420 trang. Hãy làm tròn số này đến:\na) Hàng chục nghìn.\nb) Hàng trăm nghìn.",
                       "Lời giải:\na) Làm tròn đến hàng chục nghìn: Chữ số hàng nghìn là 5 >= 5 nên làm tròn thành: 880 000 trang.\nb) Làm tròn đến hàng trăm nghìn: Chữ số hàng chục nghìn là 7 >= 5 nên làm tròn thành: 900 000 trang.\nĐáp số: a) 880 000 trang; b) 900 000 trang.",
                       "a) 880 000 trang; b) 900 000 trang", 4, 1.0),
            make_essay(4, "Một quỹ từ thiện phát động quyên góp ủng hộ đồng bào bị lũ lụt. Tuần thứ nhất quyên góp được 245 000 000 đồng, tuần thứ hai quyên góp được 275 000 000 đồng. Dự kiến cần tất cả 800 000 000 đồng. Hỏi tuần thứ ba cần quyên góp bao nhiêu tiền nữa để đạt mục tiêu?",
                       "Lời giải:\nSố tiền quyên góp được trong hai tuần đầu là:\n245 000 000 + 275 000 000 = 520 000 000 (đồng)\nTuần thứ ba cần quyên góp số tiền nữa là:\n800 000 000 - 520 000 000 = 280 000 000 (đồng)\nĐáp số: 280 000 000 đồng.",
                       "280 000 000 đồng", 5, 1.5),
            make_essay(5, "Tìm số tự nhiên có sáu chữ số thỏa mãn ba điều kiện sau:\n- Là số tròn trăm nghìn.\n- Lớn hơn 500 000 và bé hơn 900 000.\n- Chữ số hàng trăm nghìn là số chia hết cho 3.",
                       "Lời giải:\nCác số tròn trăm nghìn lớn hơn 500 000 và bé hơn 900 000 là: 600 000, 700 000, 800 000.\nTrong ba số trên, chỉ có chữ số 6 chia hết cho 3.\nVậy số thỏa mãn là: 600 000.\nĐáp số: 600 000.",
                       "600 000", 5, 1.5),
            make_essay(6, "Có bao nhiêu số có sáu chữ số mà chữ số hàng trăm nghìn là 8?",
                       "Lời giải:\nCác số đó bắt đầu từ 800 000 đến 899 999.\nSố lượng các số là:\n899 999 - 800 000 + 1 = 100 000 (số)\nĐáp số: 100 000 số.",
                       "100 000 số", 4, 1.0)
        ]
    }

    exams["th4_b16_test3"] = {
        "id": "th4_b16_test3",
        "lessonId": "th4_b16",
        "lessonNum": 16,
        "testNum": 3,
        "title": "Bài 16: Luyện tập chung Chủ đề 3 - Đề số 3",
        "topic": "Luyện tập chung Chủ đề 3",
        "chapter": "Chủ đề 3: Số có nhiều chữ số",
        "grade": "4",
        "term": "hk1",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Số gồm 9 trăm triệu và 9 trăm nghìn viết là:", [
                "900 900 000",
                "909 000 000",
                "900 090 000",
                "990 000 000"
            ], 0, "Lớp triệu: 900, lớp nghìn: 900, lớp đơn vị: 000 -> 900 900 000."),
            make_mc(2, "Số 524 380 làm tròn đến hàng chục nghìn ta được:", [
                "520 000",
                "530 000",
                "500 000",
                "524 000"
            ], 0, "Chữ số hàng nghìn là 4 < 5 nên làm tròn xuống thành 520 000."),
            make_mc(3, "So sánh hai số: 48 500 000 ... 48 499 999.", [
                ">",
                "<",
                "=",
                "Không so sánh được"
            ], 0, "Hàng trăm nghìn: 5 > 4 nên 48 500 000 > 48 499 999."),
            make_mc(4, "Có bao nhiêu số tự nhiên liên tiếp từ số 10 đến số 100?", [
                "90 số",
                "91 số",
                "89 số",
                "100 số"
            ], 1, "100 - 10 + 1 = 91 số."),
            make_mc(5, "Chữ số 5 trong số 354 820 100 có giá trị là:", [
                "5 000 000",
                "50 000 000",
                "500 000 000",
                "500 000"
            ], 1, "Chữ số 5 ở hàng chục triệu nên có giá trị là 50 000 000."),
            make_mc(6, "Số nào dưới đây là số lẻ bé nhất có sáu chữ số khác nhau?", [
                "102 345",
                "123 456",
                "100 001",
                "102 354"
            ], 0, "102 345 có các chữ số khác nhau và tận cùng là 5 (số lẻ).")
        ],
        "part2": [
            make_essay(1, "Viết các số sau thành tổng giá trị các chữ số:\na) 705 240.\nb) 42 008 000.",
                       "Lời giải:\na) 705 240 = 700 000 + 5 000 + 200 + 40\nb) 42 008 000 = 40 000 000 + 2 000 000 + 8 000\nĐáp số: a) 700 000 + 5 000 + 200 + 40; b) 40 000 000 + 2 000 000 + 8 000.",
                       "a) 700 000 + 5 000 + 200 + 40; b) 40 000 000 + 2 000 000 + 8 000", 4, 1.0),
            make_essay(2, "Xác định chữ số x để số 38x 500 khi làm tròn đến hàng chục nghìn thì được số 390 000, biết x là chữ số chẵn.",
                       "Lời giải:\nKhi làm tròn đến hàng chục nghìn, chữ số hàng nghìn là 5 (>= 5) nên được cộng 1 vào chữ số hàng chục nghìn x.\nSau khi cộng 1, ta được chữ số 9 ở hàng chục nghìn.\nDo đó: x + 1 = 9 => x = 8.\nChữ số 8 là chữ số chẵn (thỏa mãn điều kiện đề bài).\nĐáp số: x = 8.",
                       "x = 8", 4, 1.0),
            make_essay(3, "Bốn tàu chở dầu vận chuyển khối lượng dầu thô cập cảng như sau:\n- Tàu Hải Âu: 125 000 tấn\n- Tàu Biển Đông: 152 000 tấn\n- Tàu Đại Dương: 120 500 tấn\n- Tàu Sóng Biển: 150 200 tấn\nHãy sắp xếp tên bốn con tàu theo khối lượng dầu chở từ ít nhất đến nhiều nhất.",
                       "Lời giải:\nSo sánh khối lượng dầu:\n120 500 < 125 000 < 150 200 < 152 000.\nThứ tự tàu chở dầu từ ít nhất đến nhiều nhất là:\nTàu Đại Dương, Tàu Hải Âu, Tàu Sóng Biển, Tàu Biển Đông.\nĐáp số: Tàu Đại Dương, Tàu Hải Âu, Tàu Sóng Biển, Tàu Biển Đông.",
                       "Đại Dương, Hải Âu, Sóng Biển, Biển Đông", 4, 1.0),
            make_essay(4, "Một nhà máy điện mặt trời sản xuất được sản lượng điện qua ba năm như sau: Năm thứ nhất sản xuất được 180 000 000 kWh, năm thứ hai sản xuất được nhiều hơn năm thứ nhất 40 000 000 kWh, năm thứ ba sản xuất được bằng một nửa tổng sản lượng hai năm đầu. Em hãy:\na) Tính sản lượng điện của năm thứ hai và năm thứ ba.\nb) Tính tổng sản lượng điện cả ba năm.",
                       "Lời giải:\na) Sản lượng điện năm thứ hai là:\n180 000 000 + 40 000 000 = 220 000 000 (kWh)\nTổng sản lượng hai năm đầu là:\n180 000 000 + 220 000 000 = 400 000 000 (kWh)\nSản lượng điện năm thứ ba là:\n400 000 000 : 2 = 200 000 000 (kWh)\nb) Tổng sản lượng điện cả ba năm là:\n400 000 000 + 200 000 000 = 600 000 000 (kWh)\nĐáp số: a) Năm thứ hai: 220 000 000 kWh, Năm thứ ba: 200 000 000 kWh; b) 600 000 000 kWh.",
                       "a) Năm 2: 220 triệu kWh, Năm 3: 200 triệu kWh; b) 600 triệu kWh", 5, 1.5),
            make_essay(5, "Tìm số có sáu chữ số có chữ số hàng trăm nghìn là 1, chữ số hàng đơn vị là 9 và khi xóa đi hai chữ số đó thì ta được số bé nhất có bốn chữ số khác nhau.",
                       "Lời giải:\nSố bé nhất có bốn chữ số khác nhau là 1 023.\nTuy nhiên ở đây số có dạng 1[abcd]9, phần giữa [abcd] là bốn chữ số.\nĐể số là bé nhất, ta chọn bốn chữ số khác nhau bé nhất (lưu ý chữ số đầu không bị ràng buộc phải khác 0 vì nó đứng sau chữ số 1): đó là 0, 2, 3, 4 (hoặc 0, 1, 2, 3 nhưng chữ số 1 đã dùng ở hàng trăm nghìn, nếu bốn chữ số giữa khác nhau thì có thể là 0, 2, 3, 4 hoặc 0, 1, 2, 3).\nSố bé nhất có 4 chữ số khác nhau là 1 023.\nGhép lại ta được số: 110 239 (nếu tính chữ số giữa độc lập là 1 023) hoặc 102 349 (nếu tất cả các chữ số đều khác nhau).\nĐáp số: 110 239 (hoặc 102 349).",
                       "110 239 (hoặc 102 349)", 5, 1.5),
            make_essay(6, "Viết số tự nhiên liền trước và liền sau của số tự nhiên lớn nhất có 8 chữ số.",
                       "Lời giải:\n- Số tự nhiên lớn nhất có 8 chữ số là: 99 999 999.\n- Số liền trước của nó là: 99 999 999 - 1 = 99 999 998.\n- Số liền sau của nó là: 99 999 999 + 1 = 100 000 000.\nĐáp số: Liền trước: 99 999 998; Liền sau: 100 000 000.",
                       "Liền trước: 99 999 998; Liền sau: 100 000 000", 4, 1.0)
        ]
    }

    return exams
