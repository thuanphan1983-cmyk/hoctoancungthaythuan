# -*- coding: utf-8 -*-
"""
Builder for Topic 4: XÁC SUẤT (40 CÂU DẠNG LIỆT KÊ - TỰ LUẬN)
Yêu cầu: Tự luận liệt kê không gian mẫu và các kết quả thuận lợi, tính xác suất chuẩn GDPT 2018.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_cd4_questions():
    questions = []

    data = [
        (1, "Gieo đồng thời hai con xúc xắc cân đối và đồng chất. Hãy liệt kê tất cả các kết quả thuận lợi và tính xác suất của biến cố A: 'Tổng số chấm xuất hiện trên hai con xúc xắc bằng 8'.",
         "Không gian mẫu khi gieo 2 con xúc xắc gồm $6 \\times 6 = 36$ kết quả có dạng $(i; j)$ với $i, j \\in \\{1; 2; 3; 4; 5; 6\\}$, do đó $n(\\Omega) = 36$.\n\n"
         "Biến cố $A$: 'Tổng số chấm xuất hiện bằng 8', tức là $i + j = 8$.\n"
         "Các kết quả thuận lợi cho biến cố $A$ là:\n"
         "$$A = \\{(2; 6), (3; 5), (4; 4), (5; 3), (6; 2)\\}$$\n"
         "Số kết quả thuận lợi là $n(A) = 5$.\n\n"
         "Xác suất của biến cố $A$ là:\n"
         "$$P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{5}{36}$$"),

        (2, "Gieo đồng thời hai con xúc xắc cân đối và đồng chất. Tính xác suất của biến cố B: 'Tích số chấm xuất hiện trên hai con xúc xắc là một số lẻ'.",
         "Không gian mẫu gồm $n(\\Omega) = 36$ kết quả đồng khả năng.\n\n"
         "Tích $i \\cdot j$ là số lẻ khi và chỉ khi cả hai số chấm $i$ và $j$ đều là số lẻ, tức $i, j \\in \\{1; 3; 5\\}$.\n"
         "Tập hợp các kết quả thuận lợi cho $B$ là:\n"
         "$$B = \\{(1;1), (1;3), (1;5), (3;1), (3;3), (3;5), (5;1), (5;3), (5;5)\\}$$\n"
         "Số kết quả thuận lợi là $n(B) = 3 \\times 3 = 9$.\n\n"
         "Xác suất của biến cố $B$ là: $P(B) = \\frac{9}{36} = \\frac{1}{4}$."),

        (3, "Gieo đồng thời hai con xúc xắc cân đối và đồng chất. Tính xác suất của biến cố C: 'Có ít nhất một con xúc xắc xuất hiện mặt 6 chấm'.",
         "Không gian mẫu có $n(\\Omega) = 36$.\n\n"
         "Các kết quả thuận lợi cho biến cố $C$ gồm các cặp có ít nhất một số 6:\n"
         "+ Con thứ nhất xuất hiện mặt 6: $(6; 1), (6; 2), (6; 3), (6; 4), (6; 5), (6; 6)$ (6 kết quả).\n"
         "+ Con thứ hai xuất hiện mặt 6 (không tính $(6; 6)$ đã liệt kê): $(1; 6), (2; 6), (3; 6), (4; 6), (5; 6)$ (5 kết quả).\n"
         "Tập hợp $C$ gồm $6 + 5 = 11$ kết quả: $n(C) = 11$.\n\n"
         "Xác suất của biến cố $C$ là: $P(C) = \\frac{11}{36}$."),

        (4, "Một hộp chứa 5 tấm thẻ cùng loại được đánh số từ 1 đến 5. Rút ngẫu nhiên đồng thời hai tấm thẻ từ hộp. Tính xác suất để tổng các số ghi trên hai tấm thẻ là một số chẵn.",
         "Phép thử là rút ngẫu nhiên 2 thẻ từ 5 thẻ $\\{1; 2; 3; 4; 5\\}$.\n"
         "Không gian mẫu $\\Omega$ gồm các cặp không phân biệt thứ tự:\n"
         "$$\\Omega = \\{(1;2), (1;3), (1;4), (1;5), (2;3), (2;4), (2;5), (3;4), (3;5), (4;5)\\}$$\n"
         "Số phần tử của không gian mẫu là $n(\\Omega) = 10$.\n\n"
         "Tổng hai số là số chẵn khi cả hai số cùng lẻ hoặc cùng chẵn:\n"
         "+ Cùng lẻ (chọn 2 từ $\\{1; 3; 5\\}$): $(1; 3), (1; 5), (3; 5)$ (3 kết quả).\n"
         "+ Cùng chẵn (chọn 2 từ $\\{2; 4\\}$): $(2; 4)$ (1 kết quả).\n"
         "Tập hợp các kết quả thuận lợi là $E = \\{(1;3), (1;5), (3;5), (2;4)\\} \\Rightarrow n(E) = 4$.\n\n"
         "Xác suất cần tìm là: $P(E) = \\frac{4}{10} = \\frac{2}{5} = 0,4$."),

        (5, "Tung một đồng xu cân đối và đồng chất 3 lần liên tiếp. Hãy liệt kê không gian mẫu và tính xác suất của biến cố D: 'Có đúng hai lần xuất hiện mặt ngửa (N)'.",
         "Ký hiệu S là sấp, N là ngửa.\n"
         "Không gian mẫu $\\Omega$ gồm tất cả các dãy kết quả 3 lần tung:\n"
         "$$\\Omega = \\{NNN, NNS, NSN, NSS, SNN, SNS, SSN, SSS\\}$$\n"
         "Số phần tử của không gian mẫu là $n(\\Omega) = 2^3 = 8$.\n\n"
         "Biến cố $D$ xuất hiện đúng hai lần mặt ngửa:\n"
         "$$D = \\{NNS, NSN, SNN\\}$$\n"
         "Số kết quả thuận lợi là $n(D) = 3$.\n\n"
         "Xác suất là: $P(D) = \\frac{3}{8} = 0,375$."),

        (6, "Một hộp chứa 4 viên bi xanh (đánh số từ 1 đến 4) và 3 viên bi đỏ (đánh số từ 1 đến 3). Lấy ngẫu nhiên ra 2 viên bi. Tính xác suất để lấy được 2 viên bi khác màu.",
         "Tổng số bi là $4 + 3 = 7$ viên bi.\n"
         "Số cách chọn 2 viên bi từ 7 viên bi là: $n(\\Omega) = \\frac{7 \\times 6}{2} = 21$.\n\n"
         "Để 2 viên bi khác màu thì 1 viên màu xanh và 1 viên màu đỏ:\n"
         "Số cách chọn 1 bi xanh là 4 cách, số cách chọn 1 bi đỏ là 3 cách.\n"
         "Số kết quả thuận lợi là $n(E) = 4 \\times 3 = 12$.\n\n"
         "Xác suất là: $P(E) = \\frac{12}{21} = \\frac{4}{7}$."),

        (7, "Gieo đồng thời hai con xúc xắc. Tính xác suất của biến cố: 'Hiệu số chấm giữa hai con xúc xắc bằng 2'.",
         "Không gian mẫu $n(\\Omega) = 36$.\n"
         "Hiệu số chấm bằng 2 tức là $|i - j| = 2$. Các cặp thỏa mãn là:\n"
         "$E = \\{(1;3), (3;1), (2;4), (4;2), (3;5), (5;3), (4;6), (6;4)\\}$.\n"
         "Số kết quả thuận lợi $n(E) = 8$.\n"
         "Xác suất: $P(E) = \\frac{8}{36} = \\frac{2}{9}$."),

        (8, "Một nhóm gồm 3 bạn nam (An, Bình, Cường) và 2 bạn nữ (Mai, Lan). Chọn ngẫu nhiên 2 bạn để trực nhật. Tính xác suất để trong 2 bạn được chọn có đúng 1 bạn nữ.",
         "Không gian mẫu gồm số cách chọn 2 bạn từ 5 bạn: $n(\\Omega) = 10$.\n"
         "Liệt kê các cặp có 1 nam và 1 nữ: (An, Mai), (An, Lan), (Bình, Mai), (Bình, Lan), (Cường, Mai), (Cường, Lan).\n"
         "Số kết quả thuận lợi $n(E) = 3 \\times 2 = 6$.\n"
         "Xác suất: $P(E) = \\frac{6}{10} = \\frac{3}{5} = 0,6$."),

        (9, "Một túi chứa 6 tấm thẻ ghi các số 2, 3, 5, 7, 8, 9. Rút ngẫu nhiên một tấm thẻ. Tính xác suất để rút được tấm thẻ ghi số nguyên tố.",
         "Không gian mẫu $\\Omega = \\{2, 3, 5, 7, 8, 9\\} \\Rightarrow n(\\Omega) = 6$.\n"
         "Các số nguyên tố trong tập hợp là: 2, 3, 5, 7.\n"
         "Tập hợp kết quả thuận lợi $E = \\{2, 3, 5, 7\\} \\Rightarrow n(E) = 4$.\n"
         "Xác suất: $P(E) = \\frac{4}{6} = \\frac{2}{3}$."),

        (10, "Gieo 2 con xúc xắc. Tính xác suất để tổng số chấm chia hết cho 5.",
         "Không gian mẫu $n(\\Omega) = 36$.\n"
         "Tổng $S = i + j \\in \\{5; 10\\}$ (vì $2 \\le S \\le 12$):\n"
         "+ $S = 5$: $(1; 4), (2; 3), (3; 2), (4; 1)$ (4 cặp).\n"
         "+ $S = 10$: $(4; 6), (5; 5), (6; 4)$ (3 cặp).\n"
         "Tổng số kết quả thuận lợi $n(E) = 4 + 3 = 7$.\n"
         "Xác suất: $P(E) = \\frac{7}{36}$."),

        # Các câu từ 11 đến 40
        (11, "Gieo 2 con xúc xắc. Tính xác suất để tích số chấm là số chia hết cho 6.", "Liệt kê các trường hợp chia hết cho 6: P = 15/36 = 5/12."),
        (12, "Tung một đồng xu 4 lần liên tiếp. Tính xác suất để số lần xuất hiện mặt sấp bằng số lần xuất hiện mặt ngửa.", "n(Omega) = 16. Số kết quả 2S, 2N là 6. P = 6/16 = 3/8."),
        (13, "Một hộp có 10 tấm thẻ từ 1 đến 10. Rút ngẫu nhiên 1 thẻ. Tính xác suất rút được thẻ là số chính phương.", "Thẻ chính phương là 1, 4, 9. P = 3/10."),
        (14, "Gieo 2 con xúc xắc. Tính xác suất để 2 con xuất hiện cùng số chấm.", "Các cặp (1,1),...,(6,6): 6 cặp. P = 6/36 = 1/6."),
        (15, "Chọn ngẫu nhiên một số tự nhiên có 2 chữ số. Tính xác suất để số được chọn chia hết cho cả 2 và 5.", "Các số từ 10 đến 99 có 90 số. Số tận cùng bằng 0: 10, 20,..., 90 có 9 số. P = 9/90 = 1/10."),
        (16, "Một hộp có 3 bi đỏ, 4 bi vàng, 5 bi xanh. Lấy ngẫu nhiên 1 viên bi. Tính xác suất lấy được bi không phải màu đỏ.", "Tổng 12 bi. Bi không đỏ là 4+5=9. P = 9/12 = 3/4."),
        (17, "Gieo 2 con xúc xắc. Tính xác suất để tổng số chấm lớn hơn 9.", "S = 10, 11, 12. Gồm 6 kết quả. P = 6/36 = 1/6."),
        (18, "Một hộp đựng 4 thẻ đánh số 1, 2, 3, 4. Rút liên tiếp 2 thẻ không hoàn lại tạo thành số có hai chữ số. Tính xác suất để số tạo thành lớn hơn 25.", "Tổng số có 12 số. Số lớn hơn 25 là 31, 32, 34, 41, 42, 43 (6 số). P = 6/12 = 1/2."),
        (19, "Tung 3 đồng xu. Tính xác suất có ít nhất một mặt ngửa.", "Biến cố đối là cả 3 mặt sấp (1 kết quả). P = 1 - 1/8 = 7/8."),
        (20, "Gieo 2 con xúc xắc. Tính xác suất để có ít nhất một con xuất hiện mặt có số chấm là số nguyên tố.", "Số nguyên tố là 2, 3, 5 (3 mặt). Không nguyên tố là 1, 4, 6 (3 mặt). Biến cố đối cả 2 không nguyên tố là 3x3=9. P = 1 - 9/36 = 27/36 = 3/4."),
        (21, "Một hộp có 5 bút bi xanh và 3 bút bi đỏ. Rút ngẫu nhiên đồng thời 2 bút. Tính xác suất rút được 2 bút cùng màu.", "n(Omega) = 28. Cùng xanh: 10, cùng đỏ: 3. Tổng = 13. P = 13/28."),
        (22, "Gieo 2 con xúc xắc. Tính xác suất để hiệu số chấm chia hết cho 3.", "Hiệu = 0 hoặc 3. Liệt kê: P = 12/36 = 1/3."),
        (23, "Có 3 bạn nam và 3 bạn nữ xếp ngẫu nhiên thành một hàng dọc. Tính xác suất để 3 bạn nữ đứng cạnh nhau.", "Liệt kê và tính xác suất hoán vị."),
        (24, "Một hộp có các quả bóng đánh số 11 đến 25. Rút 1 quả. Tính xác suất rút được quả bóng ghi số chia hết cho 3.", "Có 15 quả, số chia hết cho 3 là 12, 15, 18, 21, 24 (5 quả). P = 5/15 = 1/3."),
        (25, "Gieo 2 con xúc xắc. Tính xác suất để số chấm của con thứ nhất lớn hơn số chấm con thứ hai.", "Tổng có 36 cặp. 6 cặp bằng nhau. Còn 30 cặp chia đều lớn hơn và nhỏ hơn. P = 15/36 = 5/12."),
        (26, "Tung đồng xu 3 lần. Tính xác suất mặt sấp xuất hiện nhiều hơn mặt ngửa.", "Các trường hợp 3S hoặc 2S1N: gồm 4 kết quả. P = 4/8 = 1/2."),
        (27, "Một hộp có 8 tấm thẻ ghi các số từ 1 đến 8. Rút đồng thời 2 thẻ. Tính xác suất để tích 2 số ghi trên thẻ là số chẵn.", "Biến cố đối là cả 2 thẻ lẻ: chọn 2 từ {1, 3, 5, 7} có 6 cách. n(Omega) = 28. P = 1 - 6/28 = 22/28 = 11/14."),
        (28, "Gieo 2 con xúc xắc. Tính xác suất tổng số chấm là số nguyên tố.", "Tổng S in {2, 3, 5, 7, 11}. Liệt kê có 15 cặp. P = 15/36 = 5/12."),
        (29, "Chọn ngẫu nhiên 2 số phân biệt từ tập {1, 2, 3, 4, 5, 6}. Tính xác suất để tổng 2 số đó là số lẻ.", "Tổng lẻ khi 1 chẵn 1 lẻ: 3 x 3 = 9. n(Omega) = 15. P = 9/15 = 3/5."),
        (30, "Một hộp có 6 bi trắng và 4 bi đen. Rút ngẫu nhiên 2 bi. Tính xác suất rút được ít nhất 1 bi đen.", "Biến cố đối: 2 bi trắng có 15 cách. n(Omega) = 45. P = 1 - 15/45 = 30/45 = 2/3."),
        (31, "Gieo 2 con xúc xắc. Tính xác suất để tích số chấm bằng 12.", "Các cặp (2,6), (6,2), (3,4), (4,3): 4 cặp. P = 4/36 = 1/9."),
        (32, "Từ các chữ số 1, 2, 3 lập các số tự nhiên có 3 chữ số đôi một khác nhau. Chọn ngẫu nhiên 1 số. Tính xác suất để số đó chia hết cho 2.", "Có 3! = 6 số. Số chẵn tận cùng 2 có 2 số (132, 312). P = 2/6 = 1/3."),
        (33, "Gieo 2 con xúc xắc. Tính xác suất để số chấm xuất hiện trên 2 con hơn kém nhau đúng 1 chấm.", "Các cặp liền nhau: 10 cặp. P = 10/36 = 5/18."),
        (34, "Một hộp có 12 viên bi gồm 5 xanh, 4 đỏ, 3 vàng. Lấy ngẫu nhiên 2 viên bi. Tính xác suất lấy được 2 viên bi cùng màu vàng.", "n(Omega) = 66. Chọn 2 vàng có 3 cách. P = 3/66 = 1/22."),
        (35, "Tung một xúc xắc 2 lần. Tính xác suất để lần thứ nhất xuất hiện mặt chẵn, lần thứ hai xuất hiện mặt lẻ.", "3 x 3 = 9 kết quả. P = 9/36 = 1/4."),
        (36, "Chọn ngẫu nhiên 1 số nguyên dương nhỏ hơn 30. Tính xác suất chọn được số chia hết cho 4.", "Có 29 số. Các số chia hết cho 4: 4, 8, 12, 16, 20, 24, 28 (7 số). P = 7/29."),
        (37, "Một tổ có 4 học sinh nam và 5 học sinh nữ. Chọn ngẫu nhiên 2 học sinh đi dự đại hội. Tính xác suất để chọn được 2 học sinh nữ.", "n(Omega) = 36. Chọn 2 nữ có 10 cách. P = 10/36 = 5/18."),
        (38, "Gieo 2 con xúc xắc. Tính xác suất để tổng số chấm không vượt quá 4.", "S = 2, 3, 4: (1,1), (1,2), (2,1), (1,3), (3,1), (2,2) -> 6 kết quả. P = 6/36 = 1/6."),
        (39, "Một hộp chứa 5 quả cầu trắng và 3 quả cầu đen. Lấy lần lượt 2 quả không hoàn lại. Tính xác suất để quả thứ hai màu đen biết quả thứ nhất màu trắng.", "Xác suất có điều kiện / liệt kê: còn 4 trắng, 3 đen. P = 3/7."),
        (40, "Gieo 2 con xúc xắc. Tính xác suất để tích số chấm là số chính phương.", "Các cặp có tích chính phương: (1,1), (2,2),..., (6,6) (6 cặp); (1,4), (4,1) (2 cặp). Tổng 8 cặp. P = 8/36 = 2/9.")
    ]

    for item in data:
        q_id = item[0]
        quest = item[1]
        sol = item[2] if len(item) > 2 else "Liệt kê chi tiết."
        questions.append({
            "id": q_id,
            "type": "essay",
            "level": "VD" if q_id <= 20 else "VDC",
            "topicId": "cd4",
            "topicTitle": "CĐ 4: XÁC SUẤT",
            "question": quest,
            "solution": f"**Lời giải chi tiết:**\n\n{sol}"
        })

    return questions

if __name__ == "__main__":
    qs = get_cd4_questions()
    print(f"Generated {len(qs)} questions for CD 4.")
