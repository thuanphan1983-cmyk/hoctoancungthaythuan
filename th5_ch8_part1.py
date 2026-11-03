# -*- coding: utf-8 -*-
"""
CHỦ ĐỀ 8 (PHẦN 1): HÌNH HỘP CHỮ NHẬT, HÌNH LẬP PHƯƠNG - DIỆN TÍCH
Gồm Bài 38, 39, 40 (9 đề kiểm tra: test1, test2, test3):
- Bài 38: Hình hộp chữ nhật, hình lập phương
- Bài 39: Diện tích xung quanh và toàn phần hình hộp chữ nhật
- Bài 40: Diện tích xung quanh và toàn phần hình lập phương
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

def get_ch8_part1_exams():
    exams = {}

    # =========================================================================
    # BÀI 38: HÌNH HỘP CHỮ NHẬT, HÌNH LẬP PHƯƠNG
    # =========================================================================

    # --- Bài 38 - Đề 1 ---
    exams["th5_b38_test1"] = {
        "id": "th5_b38_test1",
        "lessonId": "th5_b38",
        "lessonNum": 38,
        "testNum": 1,
        "title": "Bài 38: Hình hộp chữ nhật, hình lập phương - Đề số 1",
        "topic": "Hình hộp chữ nhật, hình lập phương",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hình hộp chữ nhật có bao nhiêu mặt, bao nhiêu cạnh và bao nhiêu đỉnh?", ["6 mặt, 12 cạnh, 8 đỉnh", "6 mặt, 8 cạnh, 12 đỉnh", "8 mặt, 12 cạnh, 6 đỉnh", "6 mặt, 10 cạnh, 8 đỉnh"], 0, "Hình hộp chữ nhật có 6 mặt, 12 cạnh và 8 đỉnh."),
            make_mc(2, "Các mặt của hình lập phương đều là hình gì?", ["Hình chữ nhật", "Hình vuông", "Hình thoi", "Hình tam giác"], 1, "Tất cả 6 mặt của hình lập phương đều là các hình vuông bằng nhau."),
            make_mc(3, "Một hình hộp chữ nhật có bao nhiêu kích thước?", ["1 kích thước", "2 kích thước", "3 kích thước (dài, rộng, cao)", "4 kích thước"], 2, "Hình hộp chữ nhật có 3 kích thước: chiều dài, chiều rộng, chiều cao."),
            make_mc(4, "Một hình lập phương có cạnh dài $6\\text{ cm}$. Tổng độ dài tất cả các cạnh của hình lập phương đó là:", ["24 cm", "48 cm", "72 cm", "36 cm"], 2, "Hình lập phương có 12 cạnh bằng nhau: $6 \\times 12 = 72\\text{ cm}$."),
            make_mc(5, "Đặc điểm nào sau đây là của hình hộp chữ nhật?", ["Các mặt đối diện bằng nhau", "Tất cả các cạnh đều bằng nhau", "Chỉ có 4 mặt xung quanh", "Có 6 đỉnh"], 0, "Hình hộp chữ nhật có các mặt đối diện song song và bằng nhau."),
            make_mc(6, "Một hình hộp chữ nhật có chiều dài $8\\text{ cm}$, chiều rộng $5\\text{ cm}$, chiều cao $4\\text{ cm}$. Diện tích mặt đáy của nó là:", ["$40\\text{ cm}^2$", "$32\\text{ cm}^2$", "$20\\text{ cm}^2$", "$160\\text{ cm}^2$"], 0, "Diện tích mặt đáy là: $8 \\times 5 = 40\\text{ cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Nêu số đỉnh, số cạnh, số mặt của hình hộp chữ nhật và hình lập phương.", "Cả hình hộp chữ nhật và hình lập phương đều có:\n- 8 đỉnh;\n- 12 cạnh;\n- 6 mặt.", "8 đỉnh, 12 cạnh, 6 mặt", 4, 1.0),
            make_essay(2, "Một hình lập phương có cạnh $5\\text{ cm}$. Tính diện tích một mặt của hình lập phương đó.", "Diện tích một mặt của hình lập phương là:\n$5 \\times 5 = 25\\text{ (cm}^2)$\nĐáp số: $25\\text{ cm}^2$.", "25 cm²", 4, 1.0),
            make_essay(3, "Một hình hộp chữ nhật có chiều dài $12\\text{ cm}$, chiều rộng $8\\text{ cm}$ và chiều cao $6\\text{ cm}$. Tính tổng độ dài 4 cạnh chiều dài, 4 cạnh chiều rộng và 4 cạnh chiều cao của hình hộp chữ nhật đó.", "Tổng độ dài tất cả các cạnh của hình hộp chữ nhật là:\n$(12 + 8 + 6) \\times 4 = 26 \\times 4 = 104\\text{ (cm)}$\nĐáp số: 104 cm.", "104 cm", 4, 1.0),
            make_essay(4, "Người ta dùng một sợi dây thép dài $96\\text{ cm}$ để uốn thành một chiếc khung hình lập phương vừa khít.\na) Chiếc khung hình lập phương đó có bao nhiêu cạnh?\nb) Tính độ dài mỗi cạnh của chiếc khung đó.", "Bài giải:\na) Chiếc khung hình lập phương có 12 cạnh bằng nhau.\nb) Độ dài mỗi cạnh của chiếc khung là:\n$96 : 12 = 8\\text{ (cm)}$\nĐáp số:\na) 12 cạnh;\nb) 8 cm.", "a) 12 cạnh; b) 8 cm", 5, 1.5),
            make_essay(5, "Một cái hộp carton dạng hình hộp chữ nhật có chiều dài $40\\text{ cm}$, chiều rộng $25\\text{ cm}$ và chiều cao $30\\text{ cm}$.\na) Tính chu vi mặt đáy của chiếc hộp.\nb) Tính diện tích của hai mặt đáy chiếc hộp đó.", "Bài giải:\na) Chu vi mặt đáy của chiếc hộp là:\n$(40 + 25) \\times 2 = 130\\text{ (cm)}$\nb) Diện tích hai mặt đáy của chiếc hộp là:\n$2 \\times (40 \\times 25) = 2000\\text{ (cm}^2)$\nĐáp số:\na) 130 cm;\nb) $2000\\text{ cm}^2$.", "a) 130 cm; b) 2000 cm²", 5, 1.5),
            make_essay(6, "Bác thợ mộc cưa một khối gỗ hình hộp chữ nhật có kích thước $6\\text{ dm} \\times 4\\text{ dm} \\times 3\\text{ dm}$ thành các khối lập phương nhỏ có cạnh $1\\text{ dm}$. Hỏi bác thợ mộc cưa được tất cả bao nhiêu khối lập phương nhỏ?", "Bài giải:\nSố khối lập phương nhỏ xếp theo chiều dài là: $6 : 1 = 6\\text{ (khối)}$.\nSố khối xếp theo chiều rộng là: $4 : 1 = 4\\text{ (khối)}$.\nSố khối xếp theo chiều cao là: $3 : 1 = 3\\text{ (khối)}$.\nTổng số khối lập phương nhỏ cưa được là:\n$6 \\times 4 \\times 3 = 72\\text{ (khối)}$\nĐáp số: 72 khối.", "72 khối", 5, 1.0)
        ]
    }

    # --- Bài 38 - Đề 2 ---
    exams["th5_b38_test2"] = {
        "id": "th5_b38_test2",
        "lessonId": "th5_b38",
        "lessonNum": 38,
        "testNum": 2,
        "title": "Bài 38: Hình hộp chữ nhật, hình lập phương - Đề số 2",
        "topic": "Hình hộp chữ nhật, hình lập phương",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Hình lập phương là hình hộp chữ nhật đặc biệt có:", ["Chiều dài bằng chiều rộng", "Chiều dài bằng chiều cao", "Chiều dài, chiều rộng, chiều cao đều bằng nhau", "Chỉ có 4 mặt"], 2, "Hình lập phương có 3 kích thước dài, rộng, cao đều bằng nhau."),
            make_mc(2, "Một hình hộp chữ nhật có tổng cộng bao nhiêu cạnh?", ["8 cạnh", "10 cạnh", "12 cạnh", "16 cạnh"], 2, "Có 12 cạnh gồm 4 cạnh dài, 4 cạnh rộng, 4 cạnh cao."),
            make_mc(3, "Hình lập phương có cạnh $4\\text{ dm}$. Chu vi một mặt của nó là:", ["16 dm", "8 dm", "24 dm", "12 dm"], 0, "Chu vi mặt hình vuông: $4 \\times 4 = 16\\text{ dm}$."),
            make_mc(4, "Một chiếc hộp hình chữ nhật có đáy kích thước $10\\text{ cm} \\times 6\\text{ cm}$. Chu vi đáy hộp là:", ["16 cm", "32 cm", "60 cm", "26 cm"], 1, "$(10 + 6) \\times 2 = 32\\text{ cm}$."),
            make_mc(5, "Hình nào sau đây có 6 mặt đều là hình vuông?", ["Hình hộp chữ nhật", "Hình lập phương", "Hình trụ", "Hình thang"], 1, "Hình lập phương có 6 mặt hình vuông bằng nhau."),
            make_mc(6, "Một hình hộp chữ nhật có chiều dài $7\\text{ cm}$, chiều rộng $4\\text{ cm}$, chiều cao $5\\text{ cm}$. Diện tích mặt bên có kích thước lớn hơn là:", ["$28\\text{ cm}^2$", "$35\\text{ cm}^2$", "$20\\text{ cm}^2$", "$40\\text{ cm}^2$"], 1, "Hai mặt bên có kích thước là $7 \\times 5 = 35\\text{ cm}^2$ và $4 \\times 5 = 20\\text{ cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Điền từ thích hợp vào chỗ trống:\na) Hình lập phương có 6 mặt là các hình ... bằng nhau.\nb) Hình hộp chữ nhật có ... đỉnh, ... cạnh và ... mặt.", "a) hình vuông\nb) 8 đỉnh, 12 cạnh và 6 mặt.", "a) hình vuông; b) 8 đỉnh, 12 cạnh, 6 mặt", 4, 1.0),
            make_essay(2, "Tính tổng độ dài tất cả các cạnh của hình lập phương có cạnh bằng $7\\text{ cm}$.", "Tổng độ dài tất cả các cạnh của hình lập phương là:\n$7 \\times 12 = 84\\text{ (cm)}$\nĐáp số: 84 cm.", "84 cm", 4, 1.0),
            make_essay(3, "Một hình hộp chữ nhật có chu vi mặt đáy là $28\\text{ cm}$, chiều dài là $8\\text{ cm}$. Tính chiều rộng của hình hộp chữ nhật đó.", "Nửa chu vi mặt đáy là:\n$28 : 2 = 14\\text{ (cm)}$\nChiều rộng của hình hộp chữ nhật là:\n$14 - 8 = 6\\text{ (cm)}$\nĐáp số: 6 cm.", "6 cm", 4, 1.0),
            make_essay(4, "Bác Nam uốn một khung dây thép hình hộp chữ nhật có chiều dài $20\\text{ cm}$, chiều rộng $15\\text{ cm}$ và chiều cao $10\\text{ cm}$.\na) Tính chiều dài sợi dây thép cần dùng để uốn xong chiếc khung đó.\nb) Nếu dùng sợi dây thép cùng chiều dài đó uốn thành khung hình lập phương thì cạnh hình lập phương dài bao nhiêu xăng-ti-mét?", "Bài giải:\na) Chiều dài sợi dây thép cần dùng là:\n$(20 + 15 + 10) \\times 4 = 45 \\times 4 = 180\\text{ (cm)}$\nb) Độ dài cạnh hình lập phương uốn được là:\n$180 : 12 = 15\\text{ (cm)}$\nĐáp số:\na) 180 cm;\nb) 15 cm.", "a) 180 cm; b) 15 cm", 5, 1.5),
            make_essay(5, "Một cái thùng hình hộp chữ nhật có kích thước dài $60\\text{ cm}$, rộng $40\\text{ cm}$ và cao $50\\text{ cm}$.\na) Tính diện tích mặt đáy của chiếc thùng.\nb) Tính tổng diện tích của 4 mặt bên xung quanh chiếc thùng.", "Bài giải:\na) Diện tích mặt đáy là:\n$60 \\times 40 = 2400\\text{ (cm}^2)$\nb) Chu vi đáy chiếc thùng là:\n$(60 + 40) \\times 2 = 200\\text{ (cm)}$\nTổng diện tích 4 mặt bên là:\n$200 \\times 50 = 10\\,000\\text{ (cm}^2)$\nĐáp số:\na) $2400\\text{ cm}^2$;\nb) $10\\,000\\text{ cm}^2$.", "a) 2400 cm²; b) 10 000 cm²", 5, 1.5),
            make_essay(6, "Người ta dán giấy màu lên tất cả các mặt của một khối rubik hình lập phương có cạnh $6\\text{ cm}$. Biết khối rubik gồm 27 khối nhỏ cạnh $2\\text{ cm}$. Hỏi có bao nhiêu khối nhỏ được dán giấy màu đúng 3 mặt?", "Bài giải:\nCác khối nhỏ được dán đúng 3 mặt nằm ở 8 đỉnh của hình lập phương lớn.\nHình lập phương có 8 đỉnh nên có đúng 8 khối nhỏ được dán giấy màu ở 3 mặt.\nĐáp số: 8 khối.", "8 khối", 5, 1.0)
        ]
    }

    # --- Bài 38 - Đề 3 ---
    exams["th5_b38_test3"] = {
        "id": "th5_b38_test3",
        "lessonId": "th5_b38",
        "lessonNum": 38,
        "testNum": 3,
        "title": "Bài 38: Hình hộp chữ nhật, hình lập phương - Đề số 3",
        "topic": "Hình hộp chữ nhật, hình lập phương",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình lập phương có diện tích một mặt là $36\\text{ cm}^2$. Cạnh của hình lập phương đó dài:", ["4 cm", "5 cm", "6 cm", "9 cm"], 2, "Vì $6 \\times 6 = 36$ nên cạnh dài 6 cm."),
            make_mc(2, "Số mặt đáy của hình hộp chữ nhật là:", ["1 mặt", "2 mặt", "4 mặt", "6 mặt"], 1, "Hình hộp chữ nhật có 2 mặt đáy và 4 mặt bên."),
            make_mc(3, "Hình hộp chữ nhật có chiều dài $a$, chiều rộng $b$, chiều cao $c$. Tổng độ dài tất cả các cạnh là:", ["$a + b + c$", "$(a + b + c) \\times 2$", "$(a + b + c) \\times 4$", "$(a + b) \\times 2 \\times c$"], 2, "Có 4 cạnh dài, 4 cạnh rộng, 4 cạnh cao nên là $(a + b + c) \\times 4$."),
            make_mc(4, "Một hộp quà hình lập phương có cạnh $8\\text{ cm}$. Diện tích một mặt đáy của hộp quà là:", ["$16\\text{ cm}^2$", "$32\\text{ cm}^2$", "$64\\text{ cm}^2$", "$48\\text{ cm}^2$"], 2, "$8 \\times 8 = 64\\text{ cm}^2$."),
            make_mc(5, "Tổng số đỉnh của 3 hình lập phương là:", ["18 đỉnh", "24 đỉnh", "36 đỉnh", "32 đỉnh"], 1, "Mỗi hình lập phương có 8 đỉnh: $8 \\times 3 = 24$ đỉnh."),
            make_mc(6, "Một hình hộp chữ nhật có chiều dài $15\\text{ cm}$, chiều rộng bằng một nửa chiều dài, chiều cao $6\\text{ cm}$. Chiều rộng là:", ["7 cm", "7,5 cm", "8 cm", "10 cm"], 1, "Chiều rộng là: $15 : 2 = 7,5\\text{ cm}$.")
        ],
        "part2": [
            make_essay(1, "Một hình lập phương có cạnh $9\\text{ dm}$.\na) Tính chu vi một mặt của hình lập phương.\nb) Tính diện tích một mặt của hình lập phương đó.", "a) Chu vi một mặt: $9 \\times 4 = 36\\text{ (dm)}$\nb) Diện tích một mặt: $9 \\times 9 = 81\\text{ (dm}^2)$", "a) 36 dm; b) 81 dm²", 4, 1.0),
            make_essay(2, "Một khung sắt hình hộp chữ nhật có chiều dài $1,2\\text{ m}$, chiều rộng $0,8\\text{ m}$ và chiều cao $0,6\\text{ m}$. Tính tổng chiều dài của tất cả các thanh sắt làm nên chiếc khung đó.", "Tổng độ dài các thanh sắt là:\n$(1,2 + 0,8 + 0,6) \\times 4 = 2,6 \\times 4 = 10,4\\text{ (m)}$\nĐáp số: 10,4 m.", "10,4 m", 4, 1.0),
            make_essay(3, "Một hình hộp chữ nhật có diện tích đáy là $48\\text{ cm}^2$, chiều dài là $8\\text{ cm}$. Tính chu vi mặt đáy của hình hộp chữ nhật đó.", "Chiều rộng mặt đáy là:\n$48 : 8 = 6\\text{ (cm)}$\nChu vi mặt đáy là:\n$(8 + 6) \\times 2 = 28\\text{ (cm)}$\nĐáp số: 28 cm.", "28 cm", 4, 1.0),
            make_essay(4, "Một khối gỗ hình lập phương có chu vi một mặt là $24\\text{ cm}$.\na) Tính độ dài cạnh của khối gỗ hình lập phương đó.\nb) Tính tổng độ dài 12 cạnh của khối gỗ đó.", "Bài giải:\na) Độ dài cạnh của khối gỗ là:\n$24 : 4 = 6\\text{ (cm)}$\nb) Tổng độ dài 12 cạnh của khối gỗ là:\n$6 \\times 12 = 72\\text{ (cm)}$\nĐáp số:\na) 6 cm;\nb) 72 cm.", "a) 6 cm; b) 72 cm", 5, 1.5),
            make_essay(5, "Một cái thùng không nắp hình hộp chữ nhật có chiều dài $50\\text{ cm}$, chiều rộng $35\\text{ cm}$, chiều cao $40\\text{ cm}$.\na) Chiếc thùng không nắp có tất cả bao nhiêu mặt?\nb) Tính tổng diện tích của mặt đáy và hai mặt bên có kích thước lớn hơn.", "Bài giải:\na) Chiếc thùng không nắp có 5 mặt (1 mặt đáy và 4 mặt bên xung quanh).\nb) Diện tích mặt đáy là:\n$50 \\times 35 = 1750\\text{ (cm}^2)$\nDiện tích hai mặt bên có kích thước lớn hơn là:\n$2 \\times (50 \\times 40) = 4000\\text{ (cm}^2)$\nTổng diện tích cần tìm là:\n$1750 + 4000 = 5750\\text{ (cm}^2)$\nĐáp số:\na) 5 mặt;\nb) $5750\\text{ cm}^2$.", "a) 5 mặt; b) 5750 cm²", 5, 1.5),
            make_essay(6, "Người ta dùng 8 khối lập phương nhỏ cạnh $2\\text{ cm}$ ghép lại thành một khối lập phương lớn. Hỏi cạnh của khối lập phương lớn dài bao nhiêu xăng-ti-mét?", "Bài giải:\nĐể xếp 8 khối lập phương nhỏ thành khối lập phương lớn, mỗi cạnh của khối lập phương lớn gồm 2 khối nhỏ ghép lại.\nCạnh của khối lập phương lớn dài là:\n$2 \\times 2 = 4\\text{ (cm)}$\nĐáp số: 4 cm.", "4 cm", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 39: DIỆN TÍCH XUNG QUANH VÀ TOÀN PHẦN HÌNH HỘP CHỮ NHẬT
    # =========================================================================

    # --- Bài 39 - Đề 1 ---
    exams["th5_b39_test1"] = {
        "id": "th5_b39_test1",
        "lessonId": "th5_b39",
        "lessonNum": 39,
        "testNum": 1,
        "title": "Bài 39: Diện tích xung quanh và toàn phần hình hộp chữ nhật - Đề số 1",
        "topic": "Diện tích xung quanh và toàn phần hình hộp chữ nhật",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Công thức tính diện tích xung quanh của hình hộp chữ nhật là:", ["$S_{xq} = (a + b) \\times h$", "$S_{xq} = (a + b) \\times 2 \\times h$", "$S_{xq} = a \\times b \\times h$", "$S_{xq} = (a + b) \\times 2$"], 1, "Diện tích xung quanh bằng chu vi đáy nhân với chiều cao."),
            make_mc(2, "Diện tích toàn phần của hình hộp chữ nhật bằng diện tích xung quanh cộng với:", ["Diện tích một mặt đáy", "Diện tích hai mặt đáy", "Chu vi đáy", "Thể tích"], 1, "$S_{tp} = S_{xq} + 2 \\times S_{đáy}$."),
            make_mc(3, "Một hình hộp chữ nhật có chu vi đáy $20\\text{ cm}$ và chiều cao $5\\text{ cm}$. Diện tích xung quanh của nó là:", ["$50\\text{ cm}^2$", "$100\\text{ cm}^2$", "$200\\text{ cm}^2$", "$25\\text{ cm}^2$"], 1, "$S_{xq} = 20 \\times 5 = 100\\text{ cm}^2$."),
            make_mc(4, "Một cái hộp có chiều dài $8\\text{ cm}$, chiều rộng $6\\text{ cm}$ và chiều cao $5\\text{ cm}$. Diện tích xung quanh của chiếc hộp là:", ["$140\\text{ cm}^2$", "$70\\text{ cm}^2$", "$240\\text{ cm}^2$", "$120\\text{ cm}^2$"], 0, "$S_{xq} = (8 + 6) \\times 2 \\times 5 = 140\\text{ cm}^2$."),
            make_mc(5, "Một hình hộp chữ nhật có $S_{xq} = 80\\text{ cm}^2$ và diện tích hai đáy là $50\\text{ cm}^2$. Diện tích toàn phần là:", ["$105\\text{ cm}^2$", "$130\\text{ cm}^2$", "$180\\text{ cm}^2$", "$110\\text{ cm}^2$"], 1, "$S_{tp} = 80 + 50 = 130\\text{ cm}^2$."),
            make_mc(6, "Một cái thùng không nắp hình hộp chữ nhật có $S_{xq} = 120\\text{ dm}^2$ và diện tích đáy là $35\\text{ dm}^2$. Diện tích quét sơn toàn bộ mặt ngoài là:", ["$155\\text{ dm}^2$", "$190\\text{ dm}^2$", "$150\\text{ dm}^2$", "$175\\text{ dm}^2$"], 0, "Thùng không nắp chỉ có 1 đáy: $120 + 35 = 155\\text{ dm}^2$.")
        ],
        "part2": [
            make_essay(1, "Một hình hộp chữ nhật có chiều dài $10\\text{ cm}$, chiều rộng $6\\text{ cm}$ và chiều cao $4\\text{ cm}$.\na) Tính diện tích xung quanh của hình hộp chữ nhật.\nb) Tính diện tích toàn phần của hình hộp chữ nhật.", "a) Chu vi đáy: $(10 + 6) \\times 2 = 32\\text{ (cm)}$\n$S_{xq} = 32 \\times 4 = 128\\text{ (cm}^2)$\nb) Diện tích hai đáy: $2 \\times (10 \\times 6) = 120\\text{ (cm}^2)$\n$S_{tp} = 128 + 120 = 248\\text{ (cm}^2)$", "a) 128 cm²; b) 248 cm²", 4, 1.0),
            make_essay(2, "Một chiếc hộp giấy hình chữ nhật có chu vi mặt đáy là $36\\text{ cm}$, chiều cao $8\\text{ cm}$. Tính diện tích xung quanh của chiếc hộp đó.", "Diện tích xung quanh của chiếc hộp là:\n$36 \\times 8 = 288\\text{ (cm}^2)$\nĐáp số: $288\\text{ cm}^2$.", "288 cm²", 4, 1.0),
            make_essay(3, "Một hình hộp chữ nhật có diện tích xung quanh là $180\\text{ cm}^2$, chiều cao $6\\text{ cm}$. Tính chu vi mặt đáy của hình hộp chữ nhật đó.", "Chu vi mặt đáy của hình hộp chữ nhật là:\n$180 : 6 = 30\\text{ (cm)}$\nĐáp số: 30 cm.", "30 cm", 4, 1.0),
            make_essay(4, "Một người thợ gò một cái thùng tôn không nắp dạng hình hộp chữ nhật có chiều dài $1,2\\text{ m}$, chiều rộng $0,8\\text{ m}$ và chiều cao $0,5\\text{ m}$. Tính diện tích tôn cần dùng để làm thùng (không kể mép hàn).", "Bài giải:\nChu vi đáy của thùng tôn là:\n$(1,2 + 0,8) \\times 2 = 4\\text{ (m)}$\nDiện tích xung quanh của thùng là:\n$4 \\times 0,5 = 2\\text{ (m}^2)$\nDiện tích đáy thùng là:\n$1,2 \\times 0,8 = 0,96\\text{ (m}^2)$\nVì thùng không có nắp nên diện tích tôn dùng làm thùng là:\n$2 + 0,96 = 2,96\\text{ (m}^2)$\nĐáp số: $2,96\\text{ m}^2$.", "2,96 m²", 5, 1.5),
            make_essay(5, "Một căn phòng học hình hộp chữ nhật có chiều dài $8\\text{ m}$, chiều rộng $5,5\\text{ m}$ và chiều cao $3,5\\text{ m}$. Người ta quét vôi trần nhà và 4 bức tường phía trong phòng. Tổng diện tích các cửa sổ và cửa ra vào là $9\\text{ m}^2$.\na) Tính diện tích cần quét vôi của căn phòng.\nb) Biết tiền công quét vôi $1\\text{ m}^2$ là $20\\,000$ đồng. Tính tổng số tiền công phải trả.", "Bài giải:\na) Diện tích xung quanh căn phòng là:\n$(8 + 5,5) \\times 2 \\times 3,5 = 94,5\\text{ (m}^2)$\nDiện tích trần nhà là:\n$8 \\times 5,5 = 44\\text{ (m}^2)$\nDiện tích cần quét vôi là:\n$94,5 + 44 - 9 = 129,5\\text{ (m}^2)$\nb) Số tiền công quét vôi là:\n$129,5 \\times 20\\,000 = 2\\,590\\,000\\text{ (đồng)}$\nĐáp số:\na) $129,5\\text{ m}^2$;\nb) $2\\,590\\,000\\text{ đồng}$.", "a) 129,5 m²; b) 2 590 000 đồng", 5, 1.5),
            make_essay(6, "Một hình hộp chữ nhật có chiều dài $12\\text{ cm}$, chiều rộng $8\\text{ cm}$ và diện tích toàn phần là $432\\text{ cm}^2$. Tính chiều cao của hình hộp chữ nhật đó.", "Bài giải:\nDiện tích hai mặt đáy của hình hộp chữ nhật là:\n$2 \\times (12 \\times 8) = 192\\text{ (cm}^2)$\nDiện tích xung quanh của hình hộp chữ nhật là:\n$432 - 192 = 240\\text{ (cm}^2)$\nChu vi mặt đáy là:\n$(12 + 8) \\times 2 = 40\\text{ (cm)}$\nChiều cao của hình hộp chữ nhật là:\n$240 : 40 = 6\\text{ (cm)}$\nĐáp số: 6 cm.", "6 cm", 5, 1.0)
        ]
    }

    # --- Bài 39 - Đề 2 ---
    exams["th5_b39_test2"] = {
        "id": "th5_b39_test2",
        "lessonId": "th5_b39",
        "lessonNum": 39,
        "testNum": 2,
        "title": "Bài 39: Diện tích xung quanh và toàn phần hình hộp chữ nhật - Đề số 2",
        "topic": "Diện tích xung quanh và toàn phần hình hộp chữ nhật",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình hộp chữ nhật có chiều dài $5\\text{ dm}$, chiều rộng $3\\text{ dm}$, chiều cao $4\\text{ dm}$. Diện tích xung quanh là:", ["$32\\text{ dm}^2$", "$64\\text{ dm}^2$", "$60\\text{ dm}^2$", "$94\\text{ dm}^2$"], 1, "$S_{xq} = (5 + 3) \\times 2 \\times 4 = 64\\text{ dm}^2$."),
            make_mc(2, "Một hình hộp chữ nhật có $S_{xq} = 64\\text{ dm}^2$, diện tích một mặt đáy là $15\\text{ dm}^2$. Diện tích toàn phần là:", ["$79\\text{ dm}^2$", "$94\\text{ dm}^2$", "$84\\text{ dm}^2$", "$109\\text{ dm}^2$"], 1, "$S_{tp} = 64 + 15 \\times 2 = 94\\text{ dm}^2$."),
            make_mc(3, "Muốn tính diện tích toàn phần hình hộp chữ nhật có nắp, ta lấy diện tích xung quanh cộng với:", ["Diện tích 1 đáy", "Diện tích 2 đáy", "Chiều cao", "Chu vi đáy"], 1, "Cộng với diện tích của hai mặt đáy."),
            make_mc(4, "Một bể kính nuôi cá không nắp có $S_{xq} = 2,5\\text{ m}^2$ và diện tích đáy là $0,8\\text{ m}^2$. Diện tích kính làm bể là:", ["$3,3\\text{ m}^2$", "$4,1\\text{ m}^2$", "$3,5\\text{ m}^2$", "$2,8\\text{ m}^2$"], 0, "$2,5 + 0,8 = 3,3\\text{ m}^2$."),
            make_mc(5, "Hình hộp chữ nhật có các kích thước $6\\text{ cm}, 4\\text{ cm}, 3\\text{ cm}$. Chu vi mặt đáy là:", ["10 cm", "20 cm", "24 cm", "14 cm"], 1, "$(6 + 4) \\times 2 = 20\\text{ cm}$."),
            make_mc(6, "Nếu tăng chiều cao hình hộp chữ nhật lên gấp đôi và giữ nguyên đáy thì diện tích xung quanh tăng lên:", ["2 lần", "4 lần", "Không đổi", "8 lần"], 0, "$S_{xq} = C_{đáy} \\times (2 \\times h) = 2 \\times S_{xq}$, tăng lên 2 lần.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật có:\nChiều dài $7\\text{ m}$, chiều rộng $5\\text{ m}$, chiều cao $4,5\\text{ m}$.", "Chu vi đáy: $(7 + 5) \\times 2 = 24\\text{ (m)}$\n$S_{xq} = 24 \\times 4,5 = 108\\text{ (m}^2)$\nDiện tích 2 đáy: $2 \\times (7 \\times 5) = 70\\text{ (m}^2)$\n$S_{tp} = 108 + 70 = 178\\text{ (m}^2)$", "Sxq = 108 m²; Stp = 178 m²", 4, 1.0),
            make_essay(2, "Một hình hộp chữ nhật có chu vi mặt đáy là $42\\text{ dm}$, chiều cao là $1,5\\text{ m}$. Tính diện tích xung quanh của hình hộp chữ nhật theo đơn vị mét vuông.", "Đổi: $42\\text{ dm} = 4,2\\text{ m}$.\nDiện tích xung quanh của hình hộp chữ nhật là:\n$4,2 \\times 1,5 = 6,3\\text{ (m}^2)$\nĐáp số: $6,3\\text{ m}^2$.", "6,3 m²", 4, 1.0),
            make_essay(3, "Một cái thùng tôn có nắp dạng hình hộp chữ nhật có chiều dài $1,5\\text{ m}$, chiều rộng $0,6\\text{ m}$ và diện tích xung quanh là $2,1\\text{ m}^2$. Tính chiều cao của chiếc thùng tôn đó.", "Chu vi đáy thùng tôn là:\n$(1,5 + 0,6) \\times 2 = 4,2\\text{ (m)}$\nChiều cao của thùng tôn là:\n$2,1 : 4,2 = 0,5\\text{ (m)}$\nĐáp số: 0,5 m.", "0,5 m", 4, 1.0),
            make_essay(4, "Một người thợ sơn toàn bộ bề mặt ngoài của một chiếc tủ gỗ hình hộp chữ nhật có chiều dài $1,8\\text{ m}$, chiều rộng $0,8\\text{ m}$ và chiều cao $2\\text{ m}$ (kể cả mặt đáy kê sát đất).\na) Tính diện tích toàn phần của chiếc tủ đó.\nb) Biết giá tiền sơn mỗi mét vuông là $35\\,000$ đồng. Tính tổng số tiền sơn chiếc tủ gỗ.", "Bài giải:\na) Chu vi đáy tủ gỗ là:\n$(1,8 + 0,8) \\times 2 = 5,2\\text{ (m)}$\nDiện tích xung quanh là:\n$5,2 \\times 2 = 10,4\\text{ (m}^2)$\nDiện tích hai đáy là:\n$2 \\times (1,8 \\times 0,8) = 2,88\\text{ (m}^2)$\nDiện tích toàn phần cần sơn là:\n$10,4 + 2,88 = 13,28\\text{ (m}^2)$\nb) Số tiền sơn chiếc tủ gỗ là:\n$13,28 \\times 35\\,000 = 464\\,800\\text{ (đồng)}$\nĐáp số:\na) $13,28\\text{ m}^2$;\nb) $464\\,800\\text{ đồng}$.", "a) 13,28 m²; b) 464 800 đồng", 5, 1.5),
            make_essay(5, "Một cái bể bơi dạng hình hộp chữ nhật có chiều dài $15\\text{ m}$, chiều rộng $8\\text{ m}$ và chiều sâu $1,6\\text{ m}$. Người ta ốp gạch men xung quanh và đáy bể bơi.\na) Tính diện tích cần ốp gạch men của bể bơi.\nb) Người ta dùng loại gạch men hình vuông cạnh $40\\text{ cm}$ để ốp. Hỏi cần mua bao nhiêu viên gạch men (coi mạch vữa không đáng kể)?", "Bài giải:\na) Diện tích xung quanh bể bơi là:\n$(15 + 8) \\times 2 \\times 1,6 = 73,6\\text{ (m}^2)$\nDiện tích đáy bể bơi là:\n$15 \\times 8 = 120\\text{ (m}^2)$\nDiện tích cần ốp gạch men là:\n$73,6 + 120 = 193,6\\text{ (m}^2)$\nb) Diện tích một viên gạch men hình vuông là:\n$0,4 \\times 0,4 = 0,16\\text{ (m}^2)$\nSố viên gạch men cần dùng là:\n$193,6 : 0,16 = 1210\\text{ (viên)}$\nĐáp số:\na) $193,6\\text{ m}^2$;\nb) 1210 viên gạch.", "a) 193,6 m²; b) 1210 viên", 5, 1.5),
            make_essay(6, "Một hình hộp chữ nhật có diện tích xung quanh là $150\\text{ cm}^2$, chiều cao $5\\text{ cm}$. Chiều dài hơn chiều rộng $3\\text{ cm}$. Tính diện tích toàn phần của hình hộp chữ nhật đó.", "Bài giải:\nChu vi mặt đáy là:\n$150 : 5 = 30\\text{ (cm)}$\nNửa chu vi mặt đáy là:\n$30 : 2 = 15\\text{ (cm)}$\nChiều dài hình hộp chữ nhật là:\n$(15 + 3) : 2 = 9\\text{ (cm)}$\nChiều rộng hình hộp chữ nhật là:\n$15 - 9 = 6\\text{ (cm)}$\nDiện tích hai mặt đáy là:\n$2 \\times (9 \\times 6) = 108\\text{ (cm}^2)$\nDiện tích toàn phần là:\n$150 + 108 = 258\\text{ (cm}^2)$\nĐáp số: $258\\text{ cm}^2$.", "258 cm²", 5, 1.0)
        ]
    }

    # --- Bài 39 - Đề 3 ---
    exams["th5_b39_test3"] = {
        "id": "th5_b39_test3",
        "lessonId": "th5_b39",
        "lessonNum": 39,
        "testNum": 3,
        "title": "Bài 39: Diện tích xung quanh và toàn phần hình hộp chữ nhật - Đề số 3",
        "topic": "Diện tích xung quanh và toàn phần hình hộp chữ nhật",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình hộp chữ nhật có chiều dài $10\\text{ cm}$, chiều rộng $7\\text{ cm}$ và chiều cao $6\\text{ cm}$. Chu vi đáy là:", ["17 cm", "34 cm", "42 cm", "70 cm"], 1, "$(10 + 7) \\times 2 = 34\\text{ cm}$."),
            make_mc(2, "Diện tích xung quanh của hình hộp chữ nhật có kích thước $10\\text{ cm} \\times 7\\text{ cm} \\times 6\\text{ cm}$ là:", ["$204\\text{ cm}^2$", "$102\\text{ cm}^2$", "$420\\text{ cm}^2$", "$140\\text{ cm}^2$"], 0, "$S_{xq} = 34 \\times 6 = 204\\text{ cm}^2$."),
            make_mc(3, "Diện tích toàn phần của hình hộp chữ nhật có kích thước $10\\text{ cm} \\times 7\\text{ cm} \\times 6\\text{ cm}$ là:", ["$274\\text{ cm}^2$", "$344\\text{ cm}^2$", "$304\\text{ cm}^2$", "$414\\text{ cm}^2$"], 1, "$S_{tp} = 204 + 2 \\times (10 \\times 7) = 204 + 140 = 344\\text{ cm}^2$."),
            make_mc(4, "Một thùng tôn không nắp có $S_{xq} = 8\\text{ m}^2$, diện tích đáy là $2,5\\text{ m}^2$. Diện tích tôn làm thùng là:", ["$10,5\\text{ m}^2$", "$13\\text{ m}^2$", "$11\\text{ m}^2$", "$10\\text{ m}^2$"], 0, "$8 + 2,5 = 10,5\\text{ m}^2$."),
            make_mc(5, "Một hình hộp chữ nhật có diện tích xung quanh $120\\text{ cm}^2$ và chu vi đáy $24\\text{ cm}$. Chiều cao của hình hộp đó là:", ["4 cm", "5 cm", "6 cm", "8 cm"], 1, "$120 : 24 = 5\\text{ cm}$."),
            make_mc(6, "Căn phòng có chiều dài $6\\text{ m}$, rộng $4\\text{ m}$, cao $3\\text{ m}$. Diện tích 4 bức tường xung quanh là:", ["$60\\text{ m}^2$", "$48\\text{ m}^2$", "$72\\text{ m}^2$", "$24\\text{ m}^2$"], 0, "$(6 + 4) \\times 2 \\times 3 = 60\\text{ m}^2$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích xung quanh và diện tích toàn phần của một chiếc hộp hình chữ nhật có chiều dài $15\\text{ cm}$, chiều rộng $10\\text{ cm}$, chiều cao $8\\text{ cm}$.", "Chu vi đáy: $(15 + 10) \\times 2 = 50\\text{ (cm)}$\n$S_{xq} = 50 \\times 8 = 400\\text{ (cm}^2)$\nDiện tích hai đáy: $2 \\times (15 \\times 10) = 300\\text{ (cm}^2)$\n$S_{tp} = 400 + 300 = 700\\text{ (cm}^2)$", "Sxq = 400 cm²; Stp = 700 cm²", 4, 1.0),
            make_essay(2, "Một căn phòng dạng hình hộp chữ nhật có chiều dài $9\\text{ m}$, chiều rộng $6\\text{ m}$ và chiều cao $3,8\\text{ m}$. Tính diện tích 4 bức tường xung quanh căn phòng đó.", "Chu vi đáy căn phòng là:\n$(9 + 6) \\times 2 = 30\\text{ (m)}$\nDiện tích 4 bức tường xung quanh là:\n$30 \\times 3,8 = 114\\text{ (m}^2)$\nĐáp số: $114\\text{ m}^2$.", "114 m²", 4, 1.0),
            make_essay(3, "Một hình hộp chữ nhật có diện tích xung quanh là $96\\text{ cm}^2$, chiều cao $4\\text{ cm}$ và chiều dài $7\\text{ cm}$. Tính chiều rộng của hình hộp chữ nhật đó.", "Chu vi đáy là: $96 : 4 = 24\\text{ (cm)}$.\nNửa chu vi đáy là: $24 : 2 = 12\\text{ (cm)}$.\nChiều rộng là: $12 - 7 = 5\\text{ (cm)}$.\nĐáp số: 5 cm.", "5 cm", 4, 1.0),
            make_essay(4, "Một người thợ đóng một chiếc hòm gỗ có nắp dạng hình hộp chữ nhật có chiều dài $1,4\\text{ m}$, chiều rộng $0,8\\text{ m}$ và chiều cao $0,6\\text{ m}$. Người đó sơn cả mặt trong lẫn mặt ngoài của chiếc hòm đó.\na) Tính diện tích toàn phần bề mặt ngoài của chiếc hòm gỗ.\nb) Tính tổng diện tích bề mặt cần sơn (cả trong lẫn ngoài).", "Bài giải:\na) Chu vi đáy hòm gỗ là:\n$(1,4 + 0,8) \\times 2 = 4,4\\text{ (m)}$\nDiện tích xung quanh là:\n$4,4 \\times 0,6 = 2,64\\text{ (m}^2)$\nDiện tích 2 đáy là:\n$2 \\times (1,4 \\times 0,8) = 2,24\\text{ (m}^2)$\nDiện tích toàn phần bề mặt ngoài là:\n$2,64 + 2,24 = 4,88\\text{ (m}^2)$\nb) Tổng diện tích bề mặt cần sơn cả trong lẫn ngoài là:\n$4,88 \\times 2 = 9,76\\text{ (m}^2)$\nĐáp số:\na) $4,88\\text{ m}^2$;\nb) $9,76\\text{ m}^2$.", "a) 4,88 m²; b) 9,76 m²", 5, 1.5),
            make_essay(5, "Một hội trường dạng hình hộp chữ nhật có chiều dài $18\\text{ m}$, chiều rộng $10\\text{ m}$ và chiều cao $4,5\\text{ m}$. Người ta sơn trần nhà và 4 bức tường phía trong hội trường. Biết diện tích các cửa sổ và cửa ra vào chiếm $15\\%$ diện tích xung quanh hội trường.\na) Tính diện tích xung quanh của hội trường.\nb) Tính diện tích cần sơn của hội trường đó.", "Bài giải:\na) Diện tích xung quanh của hội trường là:\n$(18 + 10) \\times 2 \\times 4,5 = 252\\text{ (m}^2)$\nb) Diện tích các cửa là:\n$252 \\times 15 : 100 = 37,8\\text{ (m}^2)$\nDiện tích trần nhà là:\n$18 \\times 10 = 180\\text{ (m}^2)$\nDiện tích cần sơn là:\n$252 + 180 - 37,8 = 394,2\\text{ (m}^2)$\nĐáp số:\na) $252\\text{ m}^2$;\nb) $394,2\\text{ m}^2$.", "a) 252 m²; b) 394,2 m²", 5, 1.5),
            make_essay(6, "Một hình hộp chữ nhật có chiều cao $6\\text{ cm}$. Nếu tăng chiều dài thêm $2\\text{ cm}$ và giữ nguyên chiều rộng thì diện tích xung quanh tăng thêm bao nhiêu xăng-ti-mét vuông?", "Bài giải:\nKhi tăng chiều dài thêm $2\\text{ cm}$, chu vi đáy tăng thêm là:\n$2 \\times 2 = 4\\text{ (cm)}$\nDiện tích xung quanh tăng thêm là:\n$4 \\times 6 = 24\\text{ (cm}^2)$\nĐáp số: $24\\text{ cm}^2$.", "24 cm²", 5, 1.0)
        ]
    }

    # =========================================================================
    # BÀI 40: DIỆN TÍCH XUNG QUANH VÀ TOÀN PHẦN HÌNH LẬP PHƯƠNG
    # =========================================================================

    # --- Bài 40 - Đề 1 ---
    exams["th5_b40_test1"] = {
        "id": "th5_b40_test1",
        "lessonId": "th5_b40",
        "lessonNum": 40,
        "testNum": 1,
        "title": "Bài 40: Diện tích xung quanh và toàn phần hình lập phương - Đề số 1",
        "topic": "Diện tích xung quanh và toàn phần hình lập phương",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Công thức tính diện tích xung quanh của hình lập phương cạnh $a$ là:", ["$S_{xq} = a \\times a \\times 4$", "$S_{xq} = a \\times a \\times 6$", "$S_{xq} = a \\times 4$", "$S_{xq} = a \\times a \\times a$"], 0, "$S_{xq} = a \\times a \\times 4$."),
            make_mc(2, "Công thức tính diện tích toàn phần của hình lập phương cạnh $a$ là:", ["$S_{tp} = a \\times a \\times 4$", "$S_{tp} = a \\times a \\times 6$", "$S_{tp} = a \\times 6$", "$S_{tp} = a \\times a \\times a$"], 1, "$S_{tp} = a \\times a \\times 6$."),
            make_mc(3, "Một hình lập phương có cạnh $3\\text{ cm}$. Diện tích xung quanh của nó là:", ["$9\\text{ cm}^2$", "$27\\text{ cm}^2$", "$36\\text{ cm}^2$", "$54\\text{ cm}^2$"], 2, "$S_{xq} = 3 \\times 3 \\times 4 = 36\\text{ cm}^2$."),
            make_mc(4, "Một hình lập phương có cạnh $5\\text{ cm}$. Diện tích toàn phần của nó là:", ["$100\\text{ cm}^2$", "$125\\text{ cm}^2$", "$150\\text{ cm}^2$", "$25\\text{ cm}^2$"], 2, "$S_{tp} = 5 \\times 5 \\times 6 = 150\\text{ cm}^2$."),
            make_mc(5, "Một hình lập phương có diện tích toàn phần là $96\\text{ cm}^2$. Diện tích một mặt của nó là:", ["$16\\text{ cm}^2$", "$24\\text{ cm}^2$", "$12\\text{ cm}^2$", "$18\\text{ cm}^2$"], 0, "$96 : 6 = 16\\text{ cm}^2$."),
            make_mc(6, "Cạnh của hình lập phương có diện tích toàn phần $96\\text{ cm}^2$ là:", ["3 cm", "4 cm", "5 cm", "6 cm"], 1, "Vì $4 \\times 4 = 16$ nên cạnh là 4 cm.")
        ],
        "part2": [
            make_essay(1, "Một hình lập phương có cạnh dài $8\\text{ cm}$.\na) Tính diện tích xung quanh của hình lập phương đó.\nb) Tính diện tích toàn phần của hình lập phương đó.", "a) Diện tích một mặt: $8 \\times 8 = 64\\text{ (cm}^2)$\n$S_{xq} = 64 \\times 4 = 256\\text{ (cm}^2)$\nb) $S_{tp} = 64 \\times 6 = 384\\text{ (cm}^2)$", "a) 256 cm²; b) 384 cm²", 4, 1.0),
            make_essay(2, "Một khối gỗ hình lập phương có diện tích xung quanh là $100\\text{ dm}^2$. Tính diện tích toàn phần của khối gỗ đó.", "Diện tích một mặt của khối gỗ là:\n$100 : 4 = 25\\text{ (dm}^2)$\nDiện tích toàn phần của khối gỗ là:\n$25 \\times 6 = 150\\text{ (dm}^2)$\nĐáp số: $150\\text{ dm}^2$.", "150 dm²", 4, 1.0),
            make_essay(3, "Một hình lập phương có diện tích toàn phần là $216\\text{ cm}^2$. Tính độ dài cạnh của hình lập phương đó.", "Diện tích một mặt của hình lập phương là:\n$216 : 6 = 36\\text{ (cm}^2)$\nVì $6 \\times 6 = 36$ nên độ dài cạnh hình lập phương là $6\\text{ cm}$.\nĐáp số: 6 cm.", "6 cm", 4, 1.0),
            make_essay(4, "Người ta làm một chiếc thùng tôn không nắp dạng hình lập phương có cạnh $0,8\\text{ m}$. Người ta sơn toàn bộ mặt ngoài của chiếc thùng đó.\na) Tính diện tích tôn dùng làm chiếc thùng đó (không kể mép hàn).\nb) Biết tiền sơn $1\\text{ m}^2$ là $45\\,000$ đồng. Hỏi sơn chiếc thùng hết bao nhiêu tiền?", "Bài giải:\na) Vì thùng không có nắp nên thùng có 5 mặt hình vuông.\nDiện tích tôn dùng làm thùng là:\n$0,8 \\times 0,8 \\times 5 = 3,2\\text{ (m}^2)$\nb) Tiền sơn chiếc thùng là:\n$3,2 \\times 45\\,000 = 144\\,000\\text{ (đồng)}$\nĐáp số:\na) $3,2\\text{ m}^2$;\nb) $144\\,000\\text{ đồng}$.", "a) 3,2 m²; b) 144 000 đồng", 5, 1.5),
            make_essay(5, "Bạn Mai dán giấy màu lên tất cả các mặt của một chiếc hộp quà dạng hình lập phương có cạnh $12\\text{ cm}$.\na) Tính diện tích giấy màu bạn Mai cần dùng (coi mép dán không đáng kể).\nb) Bạn Mai đã dùng hết một tờ giấy màu có diện tích $1000\\text{ cm}^2$. Hỏi diện tích giấy màu còn thừa là bao nhiêu xăng-ti-mét vuông?", "Bài giải:\na) Diện tích giấy màu cần dùng là diện tích toàn phần của hộp quà:\n$12 \\times 12 \\times 6 = 864\\text{ (cm}^2)$\nb) Diện tích giấy màu còn thừa là:\n$1000 - 864 = 136\\text{ (cm}^2)$\nĐáp số:\na) $864\\text{ cm}^2$;\nb) $136\\text{ cm}^2$.", "a) 864 cm²; b) 136 cm²", 5, 1.5),
            make_essay(6, "Nếu cạnh của một hình lập phương tăng lên gấp 3 lần thì diện tích toàn phần của hình lập phương đó tăng lên bao nhiêu lần?", "Bài giải:\nGọi cạnh hình lập phương ban đầu là $a$, diện tích toàn phần ban đầu là $a \\times a \\times 6$.\nKhi cạnh tăng lên 3 lần thì cạnh mới là $a \\times 3$.\nDiện tích toàn phần mới là:\n$(a \\times 3) \\times (a \\times 3) \\times 6 = (a \\times a \\times 6) \\times 9$.\nVậy diện tích toàn phần tăng lên 9 lần.\nĐáp số: 9 lần.", "9 lần", 5, 1.0)
        ]
    }

    # --- Bài 40 - Đề 2 ---
    exams["th5_b40_test2"] = {
        "id": "th5_b40_test2",
        "lessonId": "th5_b40",
        "lessonNum": 40,
        "testNum": 2,
        "title": "Bài 40: Diện tích xung quanh và toàn phần hình lập phương - Đề số 2",
        "topic": "Diện tích xung quanh và toàn phần hình lập phương",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình lập phương có cạnh $4\\text{ dm}$. Diện tích xung quanh của nó là:", ["$16\\text{ dm}^2$", "$32\\text{ dm}^2$", "$64\\text{ dm}^2$", "$96\\text{ dm}^2$"], 2, "$S_{xq} = 4 \\times 4 \\times 4 = 64\\text{ dm}^2$."),
            make_mc(2, "Diện tích toàn phần của hình lập phương có cạnh $4\\text{ dm}$ là:", ["$64\\text{ dm}^2$", "$80\\text{ dm}^2$", "$96\\text{ dm}^2$", "$128\\text{ dm}^2$"], 2, "$S_{tp} = 4 \\times 4 \\times 6 = 96\\text{ dm}^2$."),
            make_mc(3, "Một hình lập phương có chu vi một mặt là $20\\text{ cm}$. Diện tích toàn phần của nó là:", ["$100\\text{ cm}^2$", "$150\\text{ cm}^2$", "$200\\text{ cm}^2$", "$125\\text{ cm}^2$"], 1, "Cạnh là $20 : 4 = 5\\text{ cm}$. $S_{tp} = 5 \\times 5 \\times 6 = 150\\text{ cm}^2$."),
            make_mc(4, "Một cái thùng không nắp hình lập phương có cạnh $10\\text{ dm}$. Diện tích tôn làm thùng (5 mặt) là:", ["$400\\text{ dm}^2$", "$500\\text{ dm}^2$", "$600\\text{ dm}^2$", "$100\\text{ dm}^2$"], 1, "Diện tích 5 mặt: $10 \\times 10 \\times 5 = 500\\text{ dm}^2$."),
            make_mc(5, "Tỉ số giữa diện tích xung quanh và diện tích toàn phần của một hình lập phương là:", ["$\\frac{2}{3}$", "$\\frac{1}{2}$", "$\\frac{3}{4}$", "$\\frac{4}{5}$"], 0, "$\\frac{S_{xq}}{S_{tp}} = \\frac{4}{6} = \\frac{2}{3}$."),
            make_mc(6, "Một hình lập phương có diện tích toàn phần là $54\\text{ cm}^2$. Diện tích xung quanh của nó là:", ["$18\\text{ cm}^2$", "$27\\text{ cm}^2$", "$36\\text{ cm}^2$", "$45\\text{ cm}^2$"], 2, "Diện tích một mặt là $54 : 6 = 9\\text{ cm}^2$. $S_{xq} = 9 \\times 4 = 36\\text{ cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích xung quanh và diện tích toàn phần của hình lập phương có cạnh dài $1,5\\text{ m}$.", "Diện tích một mặt: $1,5 \\times 1,5 = 2,25\\text{ (m}^2)$\n$S_{xq} = 2,25 \\times 4 = 9\\text{ (m}^2)$\n$S_{tp} = 2,25 \\times 6 = 13,5\\text{ (m}^2)$", "Sxq = 9 m²; Stp = 13,5 m²", 4, 1.0),
            make_essay(2, "Một hình lập phương có chu vi một mặt là $32\\text{ cm}$. Tính diện tích xung quanh của hình lập phương đó.", "Cạnh hình lập phương là:\n$32 : 4 = 8\\text{ (cm)}$\nDiện tích xung quanh là:\n$8 \\times 8 \\times 4 = 256\\text{ (cm}^2)$\nĐáp số: $256\\text{ cm}^2$.", "256 cm²", 4, 1.0),
            make_essay(3, "Một hình lập phương có diện tích xung quanh là $144\\text{ cm}^2$. Tính diện tích toàn phần của hình lập phương đó.", "Diện tích một mặt của hình lập phương là:\n$144 : 4 = 36\\text{ (cm}^2)$\nDiện tích toàn phần của hình lập phương là:\n$36 \\times 6 = 216\\text{ (cm}^2)$\nĐáp số: $216\\text{ cm}^2$.", "216 cm²", 4, 1.0),
            make_essay(4, "Người ta sơn mặt ngoài của một chiếc thùng gỗ có nắp dạng hình lập phương cạnh $1,2\\text{ m}$.\na) Tính diện tích cần sơn của chiếc thùng gỗ đó.\nb) Biết cứ $1\\text{ m}^2$ sơn hết $0,2\\text{ kg}$ sơn. Hỏi cần bao nhiêu ki-lô-gam sơn để sơn xong chiếc thùng đó?", "Bài giải:\na) Diện tích cần sơn là diện tích toàn phần (có nắp gồm 6 mặt):\n$1,2 \\times 1,2 \\times 6 = 8,64\\text{ (m}^2)$\nb) Lượng sơn cần dùng là:\n$8,64 \\times 0,2 = 1,728\\text{ (kg)}$\nĐáp số:\na) $8,64\\text{ m}^2$;\nb) $1,728\\text{ kg}$.", "a) 8,64 m²; b) 1,728 kg", 5, 1.5),
            make_essay(5, "Một cái hộp không có nắp dạng hình lập phương có cạnh $25\\text{ cm}$. Người ta dán giấy màu mặt trong và mặt ngoài của chiếc hộp đó.\na) Tính diện tích giấy màu cần dùng để dán một mặt (trong hoặc ngoài) của chiếc hộp.\nb) Tính tổng diện tích giấy màu cần dùng để dán cả mặt trong lẫn mặt ngoài của chiếc hộp.", "Bài giải:\na) Hộp không nắp có 5 mặt. Diện tích giấy dán một mặt (trong hoặc ngoài) là:\n$25 \\times 25 \\times 5 = 3125\\text{ (cm}^2)$\nb) Tổng diện tích giấy màu cần dùng là:\n$3125 \\times 2 = 6250\\text{ (cm}^2)$\nĐáp số:\na) $3125\\text{ cm}^2$;\nb) $6250\\text{ cm}^2$.", "a) 3125 cm²; b) 6250 cm²", 5, 1.5),
            make_essay(6, "Hai hình lập phương có tỉ số giữa hai cạnh là 2. Hỏi diện tích toàn phần của hình lập phương lớn gấp mấy lần diện tích toàn phần của hình lập phương bé?", "Bài giải:\nGọi cạnh hình lập phương bé là $a$, thì cạnh hình lập phương lớn là $a \\times 2$.\nDiện tích toàn phần hình bé là: $a \\times a \\times 6$.\nDiện tích toàn phần hình lớn là:\n$(a \\times 2) \\times (a \\times 2) \\times 6 = (a \\times a \\times 6) \\times 4$.\nVậy diện tích toàn phần hình lớn gấp 4 lần diện tích toàn phần hình bé.\nĐáp số: 4 lần.", "4 lần", 5, 1.0)
        ]
    }

    # --- Bài 40 - Đề 3 ---
    exams["th5_b40_test3"] = {
        "id": "th5_b40_test3",
        "lessonId": "th5_b40",
        "lessonNum": 40,
        "testNum": 3,
        "title": "Bài 40: Diện tích xung quanh và toàn phần hình lập phương - Đề số 3",
        "topic": "Diện tích xung quanh và toàn phần hình lập phương",
        "chapter": "Chủ đề 8: Hình hộp chữ nhật, hình lập phương, hình trụ",
        "grade": "5",
        "term": "hk2",
        "duration": "35 phút",
        "points": 10.0,
        "part1": [
            make_mc(1, "Một hình lập phương có cạnh $0,6\\text{ m}$. Diện tích một mặt của nó là:", ["$0,36\\text{ m}^2$", "$3,6\\text{ m}^2$", "$2,4\\text{ m}^2$", "$0,24\\text{ m}^2$"], 0, "$0,6 \\times 0,6 = 0,36\\text{ m}^2$."),
            make_mc(2, "Diện tích xung quanh của hình lập phương có cạnh $0,6\\text{ m}$ là:", ["$1,44\\text{ m}^2$", "$2,16\\text{ m}^2$", "$1,2\\text{ m}^2$", "$1,8\\text{ m}^2$"], 0, "$0,36 \\times 4 = 1,44\\text{ m}^2$."),
            make_mc(3, "Diện tích toàn phần của hình lập phương có cạnh $0,6\\text{ m}$ là:", ["$1,44\\text{ m}^2$", "$2,16\\text{ m}^2$", "$2,4\\text{ m}^2$", "$2,56\\text{ m}^2$"], 1, "$0,36 \\times 6 = 2,16\\text{ m}^2$."),
            make_mc(4, "Một hình lập phương có diện tích toàn phần là $150\\text{ dm}^2$. Cạnh của hình lập phương đó dài:", ["4 dm", "5 dm", "6 dm", "25 dm"], 1, "Diện tích 1 mặt: $150 : 6 = 25\\text{ dm}^2$. Cạnh dài $5\\text{ dm}$ vì $5 \\times 5 = 25$."),
            make_mc(5, "Tổng diện tích xung quanh của hai hình lập phương có cùng cạnh $2\\text{ cm}$ là:", ["$16\\text{ cm}^2$", "$32\\text{ cm}^2$", "$24\\text{ cm}^2$", "$48\\text{ cm}^2$"], 1, "Mỗi hình có $S_{xq} = 2 \\times 2 \\times 4 = 16\\text{ cm}^2$. Tổng là $16 \\times 2 = 32\\text{ cm}^2$."),
            make_mc(6, "Một hình lập phương có $S_{tp} - S_{xq} = 50\\text{ cm}^2$. Diện tích toàn phần của hình đó là:", ["$100\\text{ cm}^2$", "$120\\text{ cm}^2$", "$150\\text{ cm}^2$", "$200\\text{ cm}^2$"], 2, "$S_{tp} - S_{xq} = 2 \\times S_{1mặt} = 50\\text{ cm}^2 \\implies S_{1mặt} = 25\\text{ cm}^2$. $S_{tp} = 25 \\times 6 = 150\\text{ cm}^2$.")
        ],
        "part2": [
            make_essay(1, "Tính diện tích xung quanh và diện tích toàn phần của hình lập phương có cạnh $2,4\\text{ dm}$.", "Diện tích một mặt: $2,4 \\times 2,4 = 5,76\\text{ (dm}^2)$\n$S_{xq} = 5,76 \\times 4 = 23,04\\text{ (dm}^2)$\n$S_{tp} = 5,76 \\times 6 = 34,56\\text{ (dm}^2)$", "Sxq = 23,04 dm²; Stp = 34,56 dm²", 4, 1.0),
            make_essay(2, "Một hình lập phương có tổng độ dài 12 cạnh là $84\\text{ cm}$. Tính diện tích toàn phần của hình lập phương đó.", "Độ dài cạnh hình lập phương là:\n$84 : 12 = 7\\text{ (cm)}$\nDiện tích toàn phần là:\n$7 \\times 7 \\times 6 = 294\\text{ (cm}^2)$\nĐáp số: $294\\text{ cm}^2$.", "294 cm²", 4, 1.0),
            make_essay(3, "Một hình lập phương có diện tích toàn phần là $384\\text{ cm}^2$. Tính diện tích xung quanh của hình lập phương đó.", "Diện tích một mặt là:\n$384 : 6 = 64\\text{ (cm}^2)$\nDiện tích xung quanh là:\n$64 \\times 4 = 256\\text{ (cm}^2)$\nĐáp số: $256\\text{ cm}^2$.", "256 cm²", 4, 1.0),
            make_essay(4, "Người ta gò một chiếc thùng tôn không nắp dạng hình lập phương cạnh $1,5\\text{ m}$.\na) Tính diện tích tôn làm chiếc thùng đó (không tính mép hàn).\nb) Người ta sơn mặt trong và mặt ngoài của chiếc thùng đó. Tính diện tích cần quét sơn.", "Bài giải:\na) Thùng không nắp có 5 mặt hình vuông.\nDiện tích tôn dùng làm thùng là:\n$1,5 \\times 1,5 \\times 5 = 11,25\\text{ (m}^2)$\nb) Diện tích cần quét sơn cả trong lẫn ngoài là:\n$11,25 \\times 2 = 22,5\\text{ (m}^2)$\nĐáp số:\na) $11,25\\text{ m}^2$;\nb) $22,5\\text{ m}^2$.", "a) 11,25 m²; b) 22,5 m²", 5, 1.5),
            make_essay(5, "Người ta xếp 8 khối lập phương nhỏ cạnh $5\\text{ cm}$ thành một khối lập phương lớn.\na) Tính cạnh của khối lập phương lớn được tạo thành.\nb) Tính diện tích toàn phần của khối lập phương lớn đó.", "Bài giải:\na) Khối lập phương lớn gồm 2 lớp, mỗi lớp gồm 4 khối nhỏ (2 hàng $\\times$ 2 khối).\nCạnh của khối lập phương lớn là:\n$5 \\times 2 = 10\\text{ (cm)}$\nb) Diện tích toàn phần của khối lập phương lớn là:\n$10 \\times 10 \\times 6 = 600\\text{ (cm}^2)$\nĐáp số:\na) 10 cm;\nb) $600\\text{ cm}^2$.", "a) 10 cm; b) 600 cm²", 5, 1.5),
            make_essay(6, "Cho một hình lập phương có diện tích xung quanh là $S_1$. Nếu giảm cạnh của hình lập phương đi một nửa thì diện tích xung quanh mới là $S_2$. Hỏi $S_1$ gấp mấy lần $S_2$?", "Bài giải:\nGọi cạnh ban đầu là $a$, thì $S_1 = a \\times a \\times 4$.\nCạnh mới là $a : 2$, thì $S_2 = (a : 2) \\times (a : 2) \\times 4 = (a \\times a \\times 4) : 4 = S_1 : 4$.\nVậy $S_1$ gấp 4 lần $S_2$.\nĐáp số: 4 lần.", "4 lần", 5, 1.0)
        ]
    }

    return exams
