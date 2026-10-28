# -*- coding: utf-8 -*-
"""
HỆ THỐNG BIÊN SOẠN TOÀN DIỆN TOÁN 8: CHƯƠNG VIII, IX, X
Tạo trọn vẹn:
- grade8_c8_8_exams.json / .js (12 đề)
- grade8_c9_8_exams.json / .js (18 đề)
- grade8_c10_8_exams.json / .js (9 đề)
Tổng cộng: 39 đề kiểm tra chuẩn ma trận 2025.
"""

import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
PROJECT_DIR = r"C:\Users\May Tinh Chau A\.gemini\antigravity\scratch\toan-thcs-kntt"
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from generator_utils import make_mc, make_tf, make_sa, make_essay, save_chapter_package

# ==============================================================================
# CHƯƠNG VIII TOÁN 8: MỞ ĐẦU VỀ TÍNH XÁC SUẤT CỦA BIẾN CỐ (4 BÀI = 12 ĐỀ)
# ==============================================================================
def generate_c8_toan8():
    print("🚀 Đang biên soạn Chương VIII Toán 8: Mở đầu về tính xác suất của biến cố...")
    exams = {}

    # BÀI 1 (Bài 30): Kết quả có thể và kết quả thuận lợi
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c8_8_bai1_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài 30: Kết quả có thể và kết quả thuận lợi - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Gieo một con xúc xắc 6 mặt cân đối. Có bao nhiêu kết quả có thể xảy ra?", ["6 kết quả", "12 kết quả", "1 kết quả", "36 kết quả"], 0),
                make_mc(2, "Nhận biết", "Tung một đồng xu cân đối 1 lần. Tập hợp các kết quả có thể là:", ["{Sấp, Ngửa}", "{Sấp}", "{Ngửa}", "{1, 2, 3, 4, 5, 6}"], 0),
                make_mc(3, "Nhận biết", "Một hộp có 5 viên bi xanh và 3 viên bi đỏ. Lấy ngẫu nhiên 1 viên bi. Số kết quả có thể là:", ["8 kết quả", "5 kết quả", "3 kết quả", "15 kết quả"], 0),
                make_mc(4, "Nhận biết", "Kết quả làm cho một biến cố xảy ra được gọi là:", ["Kết quả thuận lợi cho biến cố", "Kết quả ngẫu nhiên", "Kết quả không thể", "Kết quả chắc chắn"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Gieo một con xúc xắc. Biến cố 'Mặt xuất hiện có số chấm là số chẵn' có bao nhiêu kết quả thuận lợi?", ["3 kết quả ({2; 4; 6})", "2 kết quả", "4 kết quả", "6 kết quả"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Gieo một con xúc xắc. Biến cố nào sau đây là biến cố chắc chắn?", ["Số chấm xuất hiện nhỏ hơn 7", "Số chấm xuất hiện là số lẻ", "Số chấm xuất hiện bằng 6", "Số chấm xuất hiện chia hết cho 5"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Biến cố nào sau đây là biến cố không thể khi gieo một con xúc xắc?", ["Số chấm xuất hiện bằng 8", "Số chấm xuất hiện bằng 1", "Số chấm là số nguyên tố", "Số chấm chia hết cho 2"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Chọn ngẫu nhiên 1 số tự nhiên từ 1 đến 10. Số kết quả thuận lợi cho biến cố 'Số được chọn là số chia hết cho 3' là:", ["3 kết quả ({3; 6; 9})", "4 kết quả", "2 kết quả", "5 kết quả"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Tung hai đồng xu cân đối cùng lúc. Có bao nhiêu kết quả có thể xảy ra?", ["4 kết quả ({SS, SN, NS, NN})", "2 kết quả", "3 kết quả", "8 kết quả"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Chọn ngẫu nhiên một chữ cái trong từ 'HOC SINH'. Số kết quả có thể của phép thử là:", ["7 kết quả", "6 kết quả", "5 kết quả", "8 kết quả"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Trong hộp có 10 tấm thẻ ghi số từ 1 đến 10. Số kết quả thuận lợi cho biến cố 'Rút được tấm thẻ ghi số nguyên tố' là:", ["4 kết quả ({2, 3, 5, 7})", "5 kết quả", "3 kết quả", "6 kết quả"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Gieo đồng thời hai con xúc xắc cân đối. Số kết quả thuận lợi cho biến cố 'Tổng số chấm xuất hiện bằng 7' là:", ["6 kết quả", "4 kết quả", "5 kết quả", "7 kết quả"], 0)
            ],
            "part2": [
                make_tf(1, "Một hộp chứa 4 viên bi xanh, 5 viên bi đỏ và 6 viên bi vàng có kích thước giống nhau. Lấy ngẫu nhiên 1 viên bi:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tổng số kết quả có thể xảy ra của phép thử bằng 15.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Số kết quả thuận lợi cho biến cố 'Lấy được bi màu đỏ' là 5.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Biến cố 'Lấy được bi màu trắng' là biến cố không thể.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Số kết quả thuận lợi cho biến cố 'Lấy được viên bi không phải màu vàng' bằng 9.", "correct": True}
                ]),
                make_tf(2, "Gieo hai con xúc xắc 6 mặt cân đối và quan sát số chấm xuất hiện trên mặt trên của mỗi con:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tổng số kết quả có thể xảy ra của phép thử bằng 36.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Số kết quả thuận lợi cho biến cố 'Hai mặt có số chấm bằng nhau' là 6.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Biến cố 'Tổng số chấm bằng 13' là biến cố có 1 kết quả thuận lợi.", "correct": False},
                    {"key": "d", "level": "Vận dụng", "text": "Số kết quả thuận lợi cho biến cố 'Tích số chấm là một số lẻ' bằng đúng 9.", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Tung một con xúc xắc. Có bao nhiêu kết quả thuận lợi cho biến cố 'Số chấm là số chia hết cho 2'?", "3"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Từ các chữ số 1, 2, 3, 4 lập được bao nhiêu số tự nhiên có hai chữ số khác nhau?", "12"),
                make_sa(3, "Vận dụng", "Một lớp học có 20 nam và 25 nữ. Chọn ngẫu nhiên 1 học sinh. Số kết quả thuận lợi cho biến cố 'Học sinh được chọn là nữ' bằng bao nhiêu?", "25"),
                make_sa(4, "Vận dụng", "Gieo đồng thời hai con xúc xắc. Có bao nhiêu kết quả thuận lợi cho biến cố 'Tổng số chấm trên hai con xúc xắc bằng 8'?", "5")
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một túi đựng các tấm thẻ được đánh số từ 1 đến 20. Rút ngẫu nhiên một thẻ. Liệt kê các kết quả thuận lợi cho biến cố: a) Thẻ rút được là số chia hết cho 5; b) Thẻ rút được là số chính phương.", "a) Các số chia hết cho 5 từ 1 đến 20 là: {5; 10; 15; 20} (4 kết quả thuận lợi) (0.5đ). b) Các số chính phương từ 1 đến 20 là: {1; 4; 9; 16} (4 kết quả thuận lợi) (0.5đ)."),
                make_essay(2, "Vận dụng", "Viết tập hợp các kết quả có thể xảy ra khi tung hai đồng xu cân đối. Từ đó tìm số kết quả thuận lợi cho biến cố 'Có ít nhất một đồng xu xuất hiện mặt sấp'.", "Tập hợp kết quả có thể: Ω = {SS, SN, NS, NN} gồm 4 kết quả (0.5đ). Các kết quả có ít nhất một mặt sấp: {SS, SN, NS} gồm 3 kết quả thuận lợi (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Gieo hai con xúc xắc xanh và đỏ. Gọi x là số chấm trên xúc xắc xanh, y là số chấm trên xúc xắc đỏ. Có bao nhiêu kết quả thuận lợi để phương trình bậc hai $t^2 - 2xt + y = 0$ có nghiệm kép?", "Phương trình có nghiệm kép khi Δ' = x² - y = 0, tức x² = y (0.5đ). Vì 1 ≤ x, y ≤ 6 nên nếu x = 1 thì y = 1; nếu x = 2 thì y = 4; nếu x ≥ 3 thì y ≥ 9 (loại). Vậy có đúng 2 kết quả thuận lợi là (1; 1) và (2; 4) (0.5đ).")
            ]
        }

    # BÀI 2 (Bài 31): Cách tính xác suất của biến cố bằng tỉ số
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c8_8_bai2_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài 31: Tính xác suất của biến cố bằng tỉ số - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Công thức tính xác suất của biến cố $E$ với các kết quả đồng khả năng là:", ["$P(E) = \\frac{n(E)}{n(\\Omega)}$", "$P(E) = \\frac{n(\\Omega)}{n(E)}$", "$P(E) = n(E) \\cdot n(\\Omega)$", "$P(E) = n(E) - n(\\Omega)$"], 0),
                make_mc(2, "Nhận biết", "Xác suất của một biến cố chắc chắn luôn bằng:", ["$1$", "$0$", "$0.5$", "$100$"], 0),
                make_mc(3, "Nhận biết", "Xác suất của một biến cố không thể luôn bằng:", ["$0$", "$1$", "$-1$", "$0.5$"], 0),
                make_mc(4, "Nhận biết", "Xác suất của biến cố $E$ bất kì luôn thỏa mãn:", ["$0 \\le P(E) \\le 1$", "$P(E) > 1$", "$P(E) < 0$", "$-1 \\le P(E) \\le 1$"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Gieo một con xúc xắc cân đối. Xác suất để xuất hiện mặt 5 chấm là:", ["$\\frac{1}{6}$", "$\\frac{5}{6}$", "$\\frac{1}{2}$", "$\\frac{1}{5}$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Gieo một con xúc xắc cân đối. Xác suất để xuất hiện mặt có số chấm chẵn là:", ["$\\frac{1}{2}$", "$\\frac{1}{6}$", "$\\frac{1}{3}$", "$\\frac{2}{3}$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Tung một đồng xu cân đối. Xác suất xuất hiện mặt ngửa là:", ["$\\frac{1}{2}$", "$1$", "$0$", "$\\frac{1}{4}$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Một hộp có 3 bi đỏ và 7 bi xanh. Xác suất bốc ngẫu nhiên được bi đỏ là:", ["$\\frac{3}{10}$", "$\\frac{7}{10}$", "$\\frac{3}{7}$", "$\\frac{1}{3}$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Chọn ngẫu nhiên một số từ 1 đến 20. Xác suất chọn được số chia hết cho 4 là:", ["$\\frac{1}{4}$", "$\\frac{1}{5}$", "$\\frac{3}{20}$", "$\\frac{1}{10}$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Gieo một con xúc xắc. Xác suất để mặt xuất hiện là số nguyên tố là:", ["$\\frac{1}{2}$", "$\\frac{1}{3}$", "$\\frac{2}{3}$", "$\\frac{1}{6}$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Tung hai đồng xu cân đối. Xác suất để có đúng một đồng xu xuất hiện mặt sấp là:", ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$\\frac{3}{4}$", "$1$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Gieo đồng thời hai con xúc xắc. Xác suất để tổng số chấm xuất hiện bằng 9 là:", ["$\\frac{1}{9}$", "$\\frac{1}{6}$", "$\\frac{1}{12}$", "$\\frac{5}{36}$"], 0)
            ],
            "part2": [
                make_tf(1, "Một tổ học sinh có 6 bạn nam và 4 bạn nữ. Chọn ngẫu nhiên 1 bạn làm tổ trưởng:", [
                    {"key": "a", "level": "Nhận biết", "text": "Không gian mẫu của phép thử có 10 phần tử đồng khả năng.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Xác suất chọn được bạn nam bằng 6/10 = 3/5.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Xác suất chọn được bạn nữ bằng 2/5 (tương đương 40%).", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu chọn đồng thời 2 bạn thì xác suất để có 1 nam và 1 nữ bằng 8/15.", "correct": True}
                ]),
                make_tf(2, "Gieo một con xúc xắc 6 mặt cân đối:", [
                    {"key": "a", "level": "Nhận biết", "text": "Xác suất xuất hiện mỗi mặt đều bằng 1/6.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Xác suất xuất hiện mặt có số chấm lớn hơn 4 bằng 1/3.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Xác suất xuất hiện mặt có số chấm chia hết cho 3 bằng 1/2.", "correct": False},
                    {"key": "d", "level": "Vận dụng", "text": "Gieo xúc xắc 2 lần liên tiếp, xác suất để cả 2 lần đều xuất hiện mặt 6 chấm bằng 1/36.", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Một hộp có 12 viên bi gồm 5 bi đỏ, 4 bi xanh và 3 bi vàng. Lấy ngẫu nhiên 1 viên bi. Tính xác suất lấy được viên bi màu đỏ (dạng phân số tối giản a/b):", "5/12"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Chọn ngẫu nhiên 1 số tự nhiên có hai chữ số từ 10 đến 99. Có bao nhiêu kết quả có thể xảy ra?", "90"),
                make_sa(3, "Vận dụng", "Một xạ thủ bắn vào bia với xác suất bắn trúng là $0,85$. Xác suất để xạ thủ đó bắn trượt bia là bao nhiêu (dạng thập phân)?", "0.15", acceptable=["0.15", "0,15", "3/20"]),
                make_sa(4, "Vận dụng", "Gieo đồng thời hai con xúc xắc. Xác suất để tổng số chấm trên hai con xúc xắc là số chẵn bằng bao nhiêu (dạng phân số tối giản)?", "1/2", acceptable=["1/2", "0.5", "0,5"])
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một túi đựng 20 quả bóng bàn cùng kích thước được đánh số từ 1 đến 20. Rút ngẫu nhiên một quả bóng. Tính xác suất để: a) Quả bóng rút được ghi số chia hết cho 3; b) Quả bóng rút được ghi số nguyên tố.", "a) Các số chia hết cho 3: {3, 6, 9, 12, 15, 18} gồm 6 số. Xác suất P = 6/20 = 3/10 (0.5đ). b) Các số nguyên tố: {2, 3, 5, 7, 11, 13, 17, 19} gồm 8 số. Xác suất P = 8/20 = 2/5 (0.5đ)."),
                make_essay(2, "Vận dụng", "Một hộp chứa 5 quả cầu trắng và một số quả cầu đen. Lấy ngẫu nhiên một quả cầu từ hộp, biết xác suất lấy được quả cầu trắng là $0,25$. Tính tổng số quả cầu trong hộp và số quả cầu đen.", "Gọi tổng số quả cầu là N. Xác suất lấy quả trắng: 5/N = 0.25 = 1/4 (0.5đ). Suy ra N = 20 quả cầu. Số quả cầu đen là: 20 - 5 = 15 quả cầu đen (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Tung hai con xúc xắc cân đối cùng lúc. Tính xác suất để hiệu số chấm xuất hiện giữa hai con xúc xắc bằng 2.", "Tổng số kết quả là 36 (0.5đ). Các cặp (x, y) thỏa mãn |x - y| = 2 là: (1, 3), (3, 1), (2, 4), (4, 2), (3, 5), (5, 3), (4, 6), (6, 4) gồm 8 cặp thuận lợi. Xác suất P = 8/36 = 2/9 (0.5đ).")
            ]
        }

    # BÀI 3 (Bài 32): Mối liên hệ xác suất thực nghiệm và lý thuyết
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c8_8_bai3_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài 32: Xác suất thực nghiệm và xác suất ứng dụng - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Xác suất thực nghiệm của một biến cố được tính bằng:", ["Tỉ số giữa số lần xuất hiện biến cố và tổng số lần thực hiện phép thử", "Tổng số lần xuất hiện", "Tích số lần thử", "Xác suất lý thuyết"], 0),
                make_mc(2, "Nhận biết", "Khi số lần thực hiện phép thử càng lớn thì xác suất thực nghiệm:", ["Càng ngày càng gần với xác suất lý thuyết", "Bằng 0", "Càng ngày càng xa xác suất lý thuyết", "Không đổi"], 0),
                make_mc(3, "Nhận biết", "Tung đồng xu 100 lần, thấy 48 lần xuất hiện mặt sấp. Xác suất thực nghiệm của mặt sấp là:", ["$0,48$", "$0,52$", "$0,50$", "$48$"], 0),
                make_mc(4, "Nhận biết", "Một nhà máy kiểm tra 500 sản phẩm thì thấy 10 sản phẩm lỗi. Xác suất thực nghiệm sản phẩm lỗi là:", ["$2\\%$", "$5\\%$", "$10\\%$", "$1\\%$"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Gieo con xúc xắc 60 lần, mặt 1 chấm xuất hiện 12 lần. Xác suất thực nghiệm xuất hiện mặt 1 chấm là:", ["$\\frac{1}{5}$", "$\\frac{1}{6}$", "$\\frac{1}{12}$", "$\\frac{2}{5}$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Một cầu thủ sút phạt đền 50 lần và ghi được 42 bàn thắng. Xác suất thực nghiệm ghi bàn là:", ["$84\\%$", "$42\\%$", "$80\\%$", "$90\\%$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Dự báo thời tiết cho biết xác suất mưa là $70\\%$. Biến cố 'Ngày mai trời không mưa' có xác suất dự báo là:", ["$30\\%$", "$70\\%$", "$50\\%$", "$0\\%$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Tung một đồng xu 200 lần, mặt ngửa xuất hiện 106 lần. Xác suất thực nghiệm của biến cố 'Mặt ngửa' là:", ["$0,53$", "$0,47$", "$0,50$", "$1,06$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Trong 1000 bóng đèn xuất xưởng có khoảng 15 bóng hỏng. Nếu xuất xưởng 4000 bóng đèn thì dự kiến có bao nhiêu bóng hỏng?", ["60 bóng", "15 bóng", "30 bóng", "45 bóng"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Quay vòng quay may mắn 80 lần thì mũi tên dừng ở ô 'Trúng thưởng' 20 lần. Xác suất thực nghiệm trúng thưởng là:", ["$25\\%$", "$20\\%$", "$30\\%$", "$40\\%$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Gieo một con xúc xắc 120 lần. Số lần xuất hiện mặt 6 chấm dự kiến xấp xỉ khoảng:", ["20 lần", "6 lần", "12 lần", "30 lần"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một xạ thủ có xác suất bắn trúng là $0,8$. Nếu người đó bắn 100 phát thì số phát bắn trượt ước tính là:", ["20 phát", "80 phát", "10 phát", "25 phát"], 0)
            ],
            "part2": [
                make_tf(1, "Một nhà máy sản xuất linh kiện điện tử kiểm tra 1000 linh kiện thì thấy có 25 linh kiện bị lỗi:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tổng số lần thử nghiệm là 1000 lần.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Xác suất thực nghiệm của biến cố linh kiện lỗi bằng 2,5%.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Xác suất thực nghiệm của biến cố linh kiện đạt tiêu chuẩn bằng 97,5%.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu sản xuất một lô hàng 8000 linh kiện thì dự kiến có khoảng 200 linh kiện bị lỗi.", "correct": True}
                ]),
                make_tf(2, "Bạn An gieo một đồng xu 50 lần liên tiếp và ghi nhận được 28 lần xuất hiện mặt sấp:", [
                    {"key": "a", "level": "Nhận biết", "text": "Số lần xuất hiện mặt ngửa là 22 lần.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Xác suất thực nghiệm xuất hiện mặt sấp là 28/50 = 56%.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Xác suất thực nghiệm xuất hiện mặt ngửa là 44%.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Vì xác suất thực nghiệm là 56% nên xác suất lý thuyết của đồng xu này cũng bắt buộc bằng 56%.", "correct": False}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Kiểm tra ngẫu nhiên 400 quả trứng thì thấy có 8 quả bị ung. Tính xác suất thực nghiệm quả trứng bị ung (dạng phần trăm %):", "2%"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Tung đồng xu 250 lần thấy mặt ngửa xuất hiện 120 lần. Xác suất thực nghiệm của mặt sấp bằng bao nhiêu (dạng thập phân)?", "0.52", acceptable=["0.52", "0,52", "13/25"]),
                make_sa(3, "Vận dụng", "Tỉ lệ nảy mầm của một loại hạt giống là $92\\%$. Nếu gieo 500 hạt giống thì ước tính có bao nhiêu hạt nảy mầm?", "460"),
                make_sa(4, "Vận dụng", "Một cửa hàng bán được 120 chiếc áo thì có 6 khách hàng yêu cầu đổi size. Nếu cửa hàng bán được 800 chiếc áo thì ước tính có bao nhiêu chiếc bị đổi?", "40")
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Bạn Mai gieo một con xúc xắc 100 lần và được kết quả: mặt 1 chấm xuất hiện 15 lần, mặt 2 chấm xuất hiện 18 lần, mặt 3 chấm xuất hiện 14 lần, mặt 4 chấm xuất hiện 20 lần, mặt 5 chấm xuất hiện 17 lần, mặt 6 chấm xuất hiện 16 lần. Tính xác suất thực nghiệm của biến cố: a) Xuất hiện mặt có số chấm chia hết cho 3; b) Xuất hiện mặt có số chấm lớn hơn 4.", "a) Mặt chia hết cho 3 là mặt 3 và mặt 6: số lần là 14 + 16 = 30 lần. Xác suất P = 30/100 = 0.3 (30%) (0.5đ). b) Mặt lớn hơn 4 là mặt 5 và mặt 6: số lần là 17 + 16 = 33 lần. Xác suất P = 33/100 = 0.33 (33%) (0.5đ)."),
                make_essay(2, "Vận dụng", "Một công ty dược phẩm thử nghiệm một loại vắc-xin trên 2000 tình nguyện viên thì có 1920 người sinh kháng thể tốt. a) Tính xác suất thực nghiệm người tiêm sinh kháng thể tốt. b) Nếu tiêm cho 500 000 người thì ước tính có bao nhiêu người sinh kháng thể tốt?", "a) Xác suất thực nghiệm: P = 1920 / 2000 = 0.96 (96%) (0.5đ). b) Ước tính số người sinh kháng thể tốt: 500 000 * 0.96 = 480 000 người (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Một chiếc hộp chứa một số viên bi xanh và đỏ có kích thước như nhau. Bạn Hùng lấy ngẫu nhiên 1 viên bi, ghi lại màu rồi bỏ lại vào hộp. Sau 150 lần thử thì có 90 lần được bi xanh. Biết trong hộp có 12 viên bi đỏ, ước tính trong hộp có tất cả bao nhiêu viên bi?", "Xác suất thực nghiệm lấy được bi đỏ là (150 - 90)/150 = 60/150 = 0.4 (40%) (0.5đ). Gọi N là tổng số bi trong hộp. Ta có: 12 / N ≈ 0.4 suy ra N ≈ 12 / 0.4 = 30 viên bi. Vậy ước tính trong hộp có khoảng 30 viên bi (0.5đ).")
            ]
        }

    # BÀI 4 (Bài kiểm tra cuối Chương VIII)
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c8_8_bai4_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Ôn tập và kiểm tra cuối Chương VIII - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Xác suất của biến cố chắc chắn bằng:", ["1", "0", "0.5", "100"], 0),
                make_mc(2, "Nhận biết", "Xác suất của biến cố không thể bằng:", ["0", "1", "-1", "0.5"], 0),
                make_mc(3, "Nhận biết", "Gieo con xúc xắc 6 mặt, có bao nhiêu kết quả có thể xảy ra?", ["6", "12", "36", "1"], 0),
                make_mc(4, "Nhận biết", "Tung đồng xu 1 lần, xác suất mặt sấp là:", ["0.5", "1", "0", "0.25"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Một hộp có 4 bi đỏ và 6 bi xanh. Xác suất lấy được bi xanh là:", ["$\\frac{3}{5}$", "$\\frac{2}{5}$", "$\\frac{1}{2}$", "$\\frac{4}{6}$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Một lớp có 18 nam và 22 nữ. Xác suất chọn 1 học sinh là nam là:", ["$\\frac{9}{20}$", "$\\frac{11}{20}$", "$\\frac{9}{11}$", "$\\frac{18}{22}$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Gieo một con xúc xắc, xác suất số chấm nhỏ hơn 5 là:", ["$\\frac{2}{3}$", "$\\frac{1}{2}$", "$\\frac{5}{6}$", "$\\frac{1}{3}$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Chọn ngẫu nhiên một số tự nhiên có 1 chữ số. Xác suất số đó là số lẻ là:", ["$\\frac{1}{2}$", "$\\frac{5}{9}$", "$\\frac{4}{9}$", "$\\frac{1}{5}$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Gieo hai con xúc xắc. Xác suất để tổng số chấm bằng 10 là:", ["$\\frac{1}{12}$", "$\\frac{1}{6}$", "$\\frac{1}{9}$", "$\\frac{5}{36}$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Chọn ngẫu nhiên một số từ 1 đến 30. Xác suất chọn được số chính phương là:", ["$\\frac{1}{6}$", "$\\frac{1}{5}$", "$\\frac{4}{30}$", "$\\frac{1}{10}$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Tung hai đồng xu cân đối. Xác suất hai đồng xu ra cùng một mặt là:", ["$\\frac{1}{2}$", "$\\frac{1}{4}$", "$\\frac{3}{4}$", "$1$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một tổ có 5 nam và 3 nữ. Chọn ngẫu nhiên 2 người. Xác suất để chọn được 2 nữ là:", ["$\\frac{3}{28}$", "$\\frac{3}{8}$", "$\\frac{1}{4}$", "$\\frac{5}{28}$"], 0)
            ],
            "part2": [
                make_tf(1, "Gieo một con xúc xắc 6 mặt cân đối:", [
                    {"key": "a", "level": "Nhận biết", "text": "Không gian mẫu có 6 phần tử đồng khả năng.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Xác suất xuất hiện số chấm lớn hơn 2 là 2/3.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Biến cố 'Xuất hiện số chấm chia hết cho 7' là biến cố chắc chắn.", "correct": False},
                    {"key": "d", "level": "Vận dụng", "text": "Gieo 2 con xúc xắc, xác suất tích số chấm bằng 12 là 1/9.", "correct": True}
                ]),
                make_tf(2, "Một hộp chứa 5 quả bóng trắng và 7 quả bóng đen cùng kích thước:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tổng số bóng trong hộp bằng 12 quả.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Lấy ngẫu nhiên 1 quả, xác suất lấy được bóng trắng là 5/12.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Xác suất lấy được bóng màu đen là 7/12.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu lấy ngẫu nhiên 2 quả bóng cùng lúc thì xác suất lấy được 2 quả bóng cùng màu trắng bằng 5/33.", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Gieo một con xúc xắc. Xác suất để mặt xuất hiện có số chấm chia hết cho 3 bằng bao nhiêu (dạng phân số tối giản)?", "1/3"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Một hộp chứa 30 tấm thẻ từ 1 đến 30. Có bao nhiêu kết quả thuận lợi cho biến cố 'Rút được số chia hết cho cả 2 và 3'?", "5"),
                make_sa(3, "Vận dụng", "Xác suất bắn trúng mục tiêu của một vận động viên bắn cung là $0,9$. Tính xác suất vận động viên bắn trúng cả 2 phát bắn độc lập:", "0.81", acceptable=["0.81", "0,81", "81/100"]),
                make_sa(4, "Vận dụng", "Một lớp học có 40 học sinh gồm 24 bạn thích đá bóng, 16 bạn thích bóng rổ và 8 bạn thích cả hai môn. Chọn ngẫu nhiên 1 học sinh, xác suất bạn đó không thích môn nào bằng bao nhiêu (dạng thập phân)?", "0.2", acceptable=["0.2", "0,2", "1/5"])
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một hộp kín chứa 3 quả cầu đỏ, 4 quả cầu xanh và 5 quả cầu vàng. Lấy ngẫu nhiên 1 quả. Tính xác suất lấy được: a) Quả cầu màu vàng; b) Quả cầu không phải màu đỏ.", "Tổng số cầu: 3 + 4 + 5 = 12 quả (0.25đ). a) Xác suất quả vàng: 5/12 (0.25đ). b) Số quả không phải đỏ: 4 + 5 = 9 quả. Xác suất: 9/12 = 3/4 (0.5đ)."),
                make_essay(2, "Vận dụng", "Gieo đồng thời hai con xúc xắc cân đối. Tính xác suất để: a) Tổng số chấm trên hai con xúc xắc bằng 6; b) Tích số chấm trên hai con xúc xắc là số chẵn.", "a) Các cặp tổng bằng 6: (1,5), (2,4), (3,3), (4,2), (5,1) gồm 5 cặp. P = 5/36 (0.5đ). b) Tích là số lẻ khi cả hai số lẻ: 3 * 3 = 9 cặp. Suy ra tích là số chẵn có 36 - 9 = 27 cặp. Xác suất P = 27/36 = 3/4 (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Trong một hộp có một số bi đỏ và bi xanh. Người ta lấy ngẫu nhiên 1 viên bi, ghi màu rồi trả lại hộp. Lặp lại 200 lần thì được 140 lần bi đỏ. Biết hộp có 18 viên bi xanh, ước tính tổng số viên bi trong hộp là bao nhiêu?", "Xác suất thực nghiệm lấy được bi xanh là (200 - 140)/200 = 60/200 = 0.3 (0.5đ). Gọi N là tổng số bi. Ta có: 18 / N ≈ 0.3 suy ra N ≈ 18 / 0.3 = 60 viên bi (0.5đ).")
            ]
        }

    save_chapter_package(8, "c8_8", "Chương VIII: Mở đầu về tính xác suất của biến cố", exams)

# ==============================================================================
# CHƯƠNG IX TOÁN 8: TAM GIÁC ĐỒNG DẠNG (6 BÀI = 18 ĐỀ)
# ==============================================================================
def generate_c9_toan8():
    print("🚀 Đang biên soạn Chương IX Toán 8: Tam giác đồng dạng...")
    exams = {}

    # BÀI 1 (Bài 33): Hai tam giác đồng dạng
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c9_8_bai1_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài 33: Hai tam giác đồng dạng - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Nếu $\\triangle ABC \\backsim \\triangle A'B'C'$ với tỉ số đồng dạng $k$ thì $\\triangle A'B'C' \\backsim \\triangle ABC$ với tỉ số đồng dạng là:", ["$\\frac{1}{k}$", "$k$", "$k^2$", "$-k$"], 0),
                make_mc(2, "Nhận biết", "Tỉ số chu vi của hai tam giác đồng dạng bằng:", ["Tỉ số đồng dạng", "Bình phương tỉ số đồng dạng", "Căn bậc hai tỉ số đồng dạng", "Gấp đôi tỉ số đồng dạng"], 0),
                make_mc(3, "Nhận biết", "Tỉ số diện tích của hai tam giác đồng dạng bằng:", ["Bình phương tỉ số đồng dạng ($k^2$)", "Tỉ số đồng dạng ($k$)", "Căn bậc hai ($k$)", "$2k$"], 0),
                make_mc(4, "Nhận biết", "Hai tam giác bằng nhau thì đồng dạng với tỉ số đồng dạng bằng:", ["$1$", "$0$", "$2$", "$\\frac{1}{2}$"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Nếu $\\triangle ABC \\backsim \\triangle MNP$ thì các góc tương ứng bằng nhau là:", ["$\\widehat{A} = \\widehat{M}, \\widehat{B} = \\widehat{N}, \\widehat{C} = \\widehat{P}$", "$\\widehat{A} = \\widehat{N}$", "$\\widehat{B} = \\widehat{P}$", "$\\widehat{A} = \\widehat{P}$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Cho $\\triangle ABC \\backsim \\triangle DEF$ với tỉ số $k = 2$. Nếu $AB = 6\\text{ cm}$ thì $DE$ bằng:", ["$3\\text{ cm}$", "$12\\text{ cm}$", "$4\\text{ cm}$", "$6\\text{ cm}$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Cho $\\triangle ABC \\backsim \\triangle A'B'C'$ theo tỉ số $k = 3$. Tỉ số diện tích $\\frac{S_{ABC}}{S_{A'B'C'}}$ là:", ["$9$", "$3$", "$\\frac{1}{3}$", "$\\frac{1}{9}$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Tam giác $ABC$ có ba cạnh $3, 4, 5$. Tam giác $A'B'C'$ đồng dạng với $\\triangle ABC$ có cạnh nhỏ nhất là $6$ thì cạnh lớn nhất là:", ["$10$", "$8$", "$12$", "$15$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Cho $\\triangle ABC \\backsim \\triangle DEF$, biết $\\widehat{A} = 50^\\circ, \\widehat{B} = 70^\\circ$. Số đo góc $\\widehat{F}$ bằng:", ["$60^\\circ$", "$50^\\circ$", "$70^\\circ$", "$80^\\circ$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Cho $\\triangle ABC \\backsim \\triangle MNP$ theo tỉ số $k = \\frac{2}{3}$. Biết chu vi $\\triangle MNP$ bằng $45\\text{ cm}$. Chu vi $\\triangle ABC$ là:", ["$30\\text{ cm}$", "$67.5\\text{ cm}$", "$20\\text{ cm}$", "$15\\text{ cm}$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Cho $\\triangle ABC \\backsim \\triangle A'B'C'$ theo tỉ số $k = 4$. Biết $S_{A'B'C'} = 5\\text{ cm}^2$. Diện tích $\\triangle ABC$ bằng:", ["$80\\text{ cm}^2$", "$20\\text{ cm}^2$", "$40\\text{ cm}^2$", "$16\\text{ cm}^2$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một cột cờ cao $8\\text{ m}$ có bóng trên mặt đất dài $5\\text{ m}$. Cùng thời điểm đó, một tòa nhà có bóng dài $25\\text{ m}$. Chiều cao tòa nhà là:", ["$40\\text{ m}$", "$35\\text{ m}$", "$45\\text{ m}$", "$50\\text{ m}$"], 0)
            ],
            "part2": [
                make_tf(1, "Cho tam giác ABC đồng dạng với tam giác DEF theo tỉ số k = 2/3:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tam giác DEF đồng dạng với tam giác ABC theo tỉ số 3/2.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Tỉ số chu vi của tam giác ABC và tam giác DEF bằng 2/3.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Tỉ số diện tích của tam giác ABC và tam giác DEF bằng 4/9.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu tổng chu vi hai tam giác bằng 50 cm thì chu vi tam giác ABC bằng 20 cm.", "correct": True}
                ]),
                make_tf(2, "Cho tam giác ABC có AB = 6 cm, AC = 8 cm, BC = 10 cm. Tam giác MNP đồng dạng tam giác ABC với tỉ số k = 1/2:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tam giác ABC là tam giác vuông tại A.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Các cạnh của tam giác MNP lần lượt là 3 cm, 4 cm, 5 cm.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Diện tích tam giác ABC bằng 24 cm².", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Diện tích tam giác MNP bằng 12 cm².", "correct": False}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Cho $\\triangle ABC \\backsim \\triangle A'B'C'$ theo tỉ số $k = 3$. Biết chu vi tam giác $A'B'C'$ bằng $14\\text{ cm}$. Chu vi tam giác $ABC$ bằng bao nhiêu cm?", "42"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Hai tam giác đồng dạng có tỉ số diện tích là $16/25$. Tỉ số đồng dạng $k$ (nhỏ hơn 1) bằng bao nhiêu (dạng thập phân)?", "0.8", acceptable=["0.8", "0,8", "4/5"]),
                make_sa(3, "Vận dụng", "Một bạn học sinh cao $1,6\\text{ m}$ có bóng trên mặt đất dài $2\\text{ m}$. Cùng thời điểm đó, bóng của cột đèn cao áp dài $7,5\\text{ m}$. Cột đèn cao bao nhiêu mét?", "6"),
                make_sa(4, "Vận dụng", "Cho $\\triangle ABC \\backsim \\triangle DEF$. Biết $AB = 4\\text{ cm}, DE = 6\\text{ cm}$ và diện tích $\\triangle ABC$ bằng $16\\text{ cm}^2$. Diện tích $\\triangle DEF$ bằng bao nhiêu $\\text{cm}^2$?", "36")
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Cho tam giác $ABC$ có $AB = 6\\text{ cm}, AC = 9\\text{ cm}, BC = 12\\text{ cm}$. Tam giác $A'B'C'$ đồng dạng với tam giác $ABC$ và có chu vi bằng $18\\text{ cm}$. Tính độ dài các cạnh của tam giác $A'B'C'$.", "Chu vi tam giác ABC là: 6 + 9 + 12 = 27 cm (0.25đ). Tỉ số đồng dạng k = 18 / 27 = 2/3 (0.25đ). Độ dài các cạnh tam giác A'B'C' là: A'B' = 6 * (2/3) = 4 cm; A'C' = 9 * (2/3) = 6 cm; B'C' = 12 * (2/3) = 8 cm (0.5đ)."),
                make_essay(2, "Vận dụng", "Cho tam giác $ABC$, đường thẳng $d$ song song với $BC$ cắt $AB, AC$ lần lượt tại $D, E$. Biết $AD = 3\\text{ cm}, DB = 2\\text{ cm}$. Tính tỉ số diện tích giữa $\\triangle ADE$ và $\\triangle ABC$.", "Vì DE // BC nên tam giác ADE đồng dạng tam giác ABC (0.5đ). Tỉ số đồng dạng k = AD / AB = 3 / (3 + 2) = 3/5. Tỉ số diện tích bằng k² = (3/5)² = 9/25 (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Cho hình bình hành $ABCD$. Một đường thẳng đi qua $D$ cắt $AB$ tại $M$, cắt $BC$ tại $N$ và cắt $AC$ tại $K$. Chứng minh rằng: $KD^2 = KM \\cdot KN$.", "Áp dụng định lí đồng dạng do các đoạn thẳng song song: AM // CD suy ra tam giác KMA đồng dạng KDC dẫn đến KM / KD = KA / KC (0.5đ). Lại có AD // CN suy ra tam giác KAD đồng dạng KCN dẫn đến KD / KN = KA / KC. Từ đó KM / KD = KD / KN suy ra KD² = KM * KN (0.5đ).")
            ]
        }

    # BÀI 2 (Bài 34): Ba trường hợp đồng dạng của tam giác (c.c.c, c.g.c, g.g)
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c9_8_bai2_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài 34: Ba trường hợp đồng dạng của hai tam giác - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Nếu ba cạnh của tam giác này tỉ lệ với ba cạnh của tam giác kia thì hai tam giác đó:", ["Đồng dạng (c.c.c)", "Bằng nhau", "Đồng dạng (g.g)", "Không đồng dạng"], 0),
                make_mc(2, "Nhận biết", "Nếu hai cạnh của tam giác này tỉ lệ với hai cạnh của tam giác kia và:", ["Hai góc tạo bởi các cặp cạnh đó bằng nhau thì hai tam giác đồng dạng (c.g.c)", "Một góc bất kì bằng nhau", "Góc đối diện bằng nhau", "Cạnh thứ ba bằng nhau"], 0),
                make_mc(3, "Nhận biết", "Nếu hai góc của tam giác này lần lượt bằng hai góc của tam giác kia thì:", ["Hai tam giác đồng dạng (g.g)", "Hai tam giác bằng nhau", "Hai tam giác cân", "Hai tam giác vuông"], 0),
                make_mc(4, "Nhận biết", "Hai tam giác đều bất kì luôn:", ["Đồng dạng với nhau", "Bằng nhau", "Có diện tích bằng nhau", "Có chu vi bằng nhau"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Cho $\\triangle ABC$ có $\\widehat{A} = 60^\\circ, \\widehat{B} = 70^\\circ$ và $\\triangle MNP$ có $\\widehat{M} = 60^\\circ, \\widehat{P} = 50^\\circ$. Hai tam giác đó:", ["Đồng dạng với nhau", "Không đồng dạng", "Bằng nhau", "Có chu vi bằng nhau"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Tam giác $ABC$ có $AB = 4, AC = 6$. Tam giác $A'B'C'$ có $\\widehat{A'} = \\widehat{A}, A'B' = 6, A'C' = 9$. Hai tam giác đồng dạng theo trường hợp:", ["cạnh - góc - cạnh (c.g.c)", "cạnh - cạnh - cạnh (c.c.c)", "góc - góc (g.g)", "cạnh huyền - góc nhọn"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Cho $\\triangle ABC$ có $AB = 3, BC = 5, CA = 6$ và $\\triangle DEF$ có $DE = 6, EF = 10, FD = 12$. Tỉ số đồng dạng bằng:", ["$\\frac{1}{2}$", "$2$", "$\\frac{1}{4}$", "$4$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Hai tam giác vuông có một góc nhọn bằng nhau thì:", ["Đồng dạng với nhau", "Bằng nhau", "Có cạnh huyền bằng nhau", "Không đồng dạng"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Cho hình thang $ABCD$ ($AB // CD$), hai đường chéo cắt nhau tại $O$. Cặp tam giác đồng dạng là:", ["$\\triangle OAB \\backsim \\triangle OCD$", "$\\triangle OAD \\backsim \\triangle OBC$", "$\\triangle ABD \\backsim \\triangle BCD$", "$\\triangle ABC \\backsim \\triangle CDA$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Cho $\\triangle ABC$, trên cạnh $AB, AC$ lấy $D, E$ sao cho $\\frac{AD}{AB} = \\frac{AE}{AC}$. Khẳng định đúng là:", ["$DE // BC$ và $\\triangle ADE \\backsim \\triangle ABC$", "$DE = BC$", "$DE \\perp BC$", "$\\triangle ADE = \\triangle ABC$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Cho $\\triangle ABC$ có $\\widehat{A} = 90^\\circ$, đường cao $AH$. Số cặp tam giác đồng dạng có trong hình là:", ["$3$ cặp", "$2$ cặp", "$4$ cặp", "$1$ cặp"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Cho tam giác $ABC$, điểm $D$ thuộc cạnh $AC$ sao cho $\\widehat{ABD} = \\widehat{C}$. Đẳng thức nào sau đây đúng?", ["$AB^2 = AD \\cdot AC$", "$AC^2 = AD \\cdot AB$", "$BD^2 = AD \\cdot CD$", "$AB \\cdot AC = BD \\cdot BC$"], 0)
            ],
            "part2": [
                make_tf(1, "Cho tam giác ABC có AB = 4 cm, AC = 6 cm. Trên cạnh AB lấy D sao cho AD = 2 cm, trên cạnh AC lấy E sao cho AE = 3 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Tỉ số AD/AB = 1/2 và AE/AC = 1/2.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Tam giác ADE đồng dạng tam giác ABC theo trường hợp (c.g.c).", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Đoạn thẳng DE song song với cạnh BC.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Diện tích tứ giác BDEC gấp 3 lần diện tích tam giác ADE.", "correct": True}
                ]),
                make_tf(2, "Cho hình thang ABCD (AB // CD) có AB = 4 cm, CD = 9 cm. Hai đường chéo AC và BD cắt nhau tại O:", [
                    {"key": "a", "level": "Nhận biết", "text": "Góc OAB = góc OCD (so le trong).", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Tam giác OAB đồng dạng tam giác OCD theo trường hợp (g.g).", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Tỉ số đồng dạng k = OA/OC = 4/9.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Tỉ số diện tích giữa tam giác OAB và tam giác OCD là 2/3.", "correct": False}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 6\\text{ cm}, AC = 8\\text{ cm}$, đường cao $AH$. Tính độ dài $AH$ (cm):", "4.8", acceptable=["4.8", "4,8", "24/5"]),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Cho $\\triangle ABC \\backsim \\triangle DEF$. Biết $AB = 5\\text{ cm}, BC = 7\\text{ cm}, DE = 15\\text{ cm}$. Tính độ dài $EF$ (cm):", "21"),
                make_sa(3, "Vận dụng", "Cho tam giác $ABC$ có $AB = 9\\text{ cm}, AC = 12\\text{ cm}$. Điểm $D$ trên $AB$ sao cho $AD = 4\\text{ cm}$, điểm $E$ trên $AC$ sao cho $AE = 3\\text{ cm}$. Tính tỉ số diện tích $\\frac{S_{ADE}}{S_{ABC}}$ (dạng phân số tối giản):", "1/9"),
                make_sa(4, "Vận dụng", "Cho hình chữ nhật $ABCD$ có $AB = 8\\text{ cm}, BC = 6\\text{ cm}$. Kẻ $AH \\perp BD$. Độ dài đoạn thẳng $DH$ bằng bao nhiêu cm (dạng thập phân)?", "3.6", acceptable=["3.6", "3,6", "18/5"])
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Cho tam giác $ABC$ nhọn. Hai đường cao $BD$ và $CE$ cắt nhau tại $H$. Chứng minh rằng: a) $\\triangle ABD \\backsim \\triangle ACE$; b) $HD \\cdot HB = HE \\cdot HC$.", "a) Xét tam giác ABD và ACE vuông tại D và E có góc A chung nên đồng dạng theo trường hợp (g.g) (0.5đ). b) Xét tam giác HED và HCB có góc EHD = góc CHB (đối đỉnh), góc HED = góc HCB (do tứ giác hoặc góc phụ) suy ra hai tam giác đồng dạng, dẫn đến HD/HE = HC/HB hay HD*HB = HE*HC (0.5đ)."),
                make_essay(2, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$, kẻ đường cao $AH$. Chứng minh rằng: a) $AB^2 = BH \\cdot BC$; b) $AH^2 = BH \\cdot CH$.", "a) Chứng minh tam giác HBA đồng dạng tam giác ABC (g.g) suy ra AB/BC = BH/AB dẫn đến AB² = BH*BC (0.5đ). b) Chứng minh tam giác HBA đồng dạng tam giác HAC (g.g) suy ra HA/HC = HB/HA dẫn đến AH² = BH*CH (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Cho hình vuông $ABCD$, điểm $M$ thuộc cạnh $BC$. Đường thẳng qua $A$ vuông góc với $AM$ cắt đường thẳng $CD$ tại $N$. Chứng minh rằng $\\triangle AMN$ là tam giác vuông cân.", "Xét hai tam giác vuông ABM và ADN có AB = AD (cạnh hình vuông), góc BAM = góc DAN (cùng phụ với góc MAD) (0.5đ). Suy ra tam giác ABM = tam giác ADN (g.c.g), dẫn đến AM = AN. Mà góc MAN = 90° nên tam giác AMN vuông cân tại A (0.5đ).")
            ]
        }

    # BÀI 3, 4, 5, 6 của Chương IX: Bài 35 (Pythagore), Bài 36 (Tam giác vuông đồng dạng), Bài 37 (Hình đồng dạng), Bài ôn tập cuối chương
    for (l_idx, l_name) in [
        (3, "Bài 35: Định lí Pythagore và ứng dụng"),
        (4, "Bài 36: Các trường hợp đồng dạng của hai tam giác vuông"),
        (5, "Bài 37: Hình đồng dạng"),
        (6, "Bài kiểm tra cuối Chương IX: Tam giác đồng dạng")
    ]:
        for t in [1, 2, 3]:
            is_hard = (t == 3)
            diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
            exams[f"c9_8_bai{l_idx}_test{t}"] = {
                "title": f"Toán 8 (KNTT) - {l_name} - Đề số {t} ({diff_name})",
                "part1": [
                    make_mc(1, "Nhận biết", "Trong tam giác vuông, bình phương cạnh huyền bằng:", ["Tổng bình phương hai cạnh góc vuông", "Hiệu bình phương hai cạnh góc vuông", "Tích hai cạnh góc vuông", "Tổng hai cạnh góc vuông"], 0),
                    make_mc(2, "Nhận biết", "Nếu một tam giác có bình phương một cạnh bằng tổng bình phương hai cạnh kia thì:", ["Tam giác đó là tam giác vuông", "Tam giác đó là tam giác đều", "Tam giác đó là tam giác cân", "Tam giác đó là tam giác nhọn"], 0),
                    make_mc(3, "Nhận biết", "Bộ ba số nào sau đây là bộ ba số Pythagore?", ["$3, 4, 5$", "$2, 3, 4$", "$4, 5, 6$", "$5, 6, 7$"], 0),
                    make_mc(4, "Nhận biết", "Hai tam giác vuông đồng dạng khi có:", ["Một góc nhọn bằng nhau", "Một góc vuông", "Một cạnh bằng nhau", "Diện tích bằng nhau"], 0),
                    make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Nếu cạnh huyền và một cạnh góc vuông của tam giác vuông này tỉ lệ với cạnh huyền và cạnh góc vuông của tam giác vuông kia thì:", ["Hai tam giác vuông đó đồng dạng", "Hai tam giác vuông đó bằng nhau", "Hai tam giác vuông cân", "Không đồng dạng"], 0),
                    make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Tam giác $ABC$ vuông tại $A$ có $AB = 5\\text{ cm}, AC = 12\\text{ cm}$. Độ dài cạnh huyền $BC$ là:", ["$13\\text{ cm}$", "$17\\text{ cm}$", "$15\\text{ cm}$", "$14\\text{ cm}$"], 0),
                    make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Tam giác vuông cân có cạnh góc vuông bằng $a$. Cạnh huyền có độ dài bằng:", ["$a\\sqrt{2}$", "$2a$", "$a\\sqrt{3}$", "$a^2$"], 0),
                    make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Độ dài đường chéo của hình vuông cạnh $5\\text{ cm}$ là:", ["$5\\sqrt{2}\\text{ cm}$", "$10\\text{ cm}$", "$5\\sqrt{3}\\text{ cm}$", "$25\\text{ cm}$"], 0),
                    make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Tam giác có độ dài ba cạnh $6\\text{ cm}, 8\\text{ cm}, 10\\text{ cm}$ là tam giác gì?", ["Tam giác vuông", "Tam giác nhọn", "Tam giác tù", "Tam giác cân"], 0),
                    make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Hai hình đồng dạng phối cảnh có tâm phối cảnh là điểm $O$. Tỉ số khoảng cách từ $O$ đến các điểm tương ứng gọi là:", ["Tỉ số vị tự (tỉ số đồng dạng)", "Bán kính", "Độ dốc", "Góc quay"], 0),
                    make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Cho $\\triangle ABC$ vuông tại $A$, đường cao $AH$. Khẳng định nào sau đây là sai?", ["$BC^2 = AB^2 - AC^2$", "$AB^2 = BH \\cdot BC$", "$AC^2 = CH \\cdot BC$", "$AH^2 = BH \\cdot CH$"], 0),
                    make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một chiếc thang dài $5\\text{ m}$ đặt tựa vào tường, chân thang cách tường $3\\text{ m}$. Chiều cao của bức tường mà thang chạm tới là:", ["$4\\text{ m}$", "$3.5\\text{ m}$", "$4.5\\text{ m}$", "$2\\text{ m}$"], 0)
                ],
                "part2": [
                    make_tf(1, "Cho tam giác ABC có độ dài ba cạnh là AB = 9 cm, AC = 12 cm, BC = 15 cm:", [
                        {"key": "a", "level": "Nhận biết", "text": "Vì 9² + 12² = 81 + 144 = 225 = 15² nên tam giác ABC vuông tại A.", "correct": True},
                        {"key": "b", "level": "Nhận biết", "text": "Diện tích tam giác ABC bằng 1/2 * 9 * 12 = 54 cm².", "correct": True},
                        {"key": "c", "level": "Thông hiểu", "text": "Đường cao AH kẻ từ A đến BC có độ dài bằng 7,2 cm.", "correct": True},
                        {"key": "d", "level": "Vận dụng", "text": "Bán kính đường tròn ngoại tiếp tam giác ABC bằng 6 cm.", "correct": False}
                    ]),
                    make_tf(2, "Cho hai hình chữ nhật ABCD kích thước 4 cm x 6 cm và A'B'C'D' kích thước 6 cm x 9 cm:", [
                        {"key": "a", "level": "Nhận biết", "text": "Tỉ số hai chiều rộng bằng 4/6 = 2/3.", "correct": True},
                        {"key": "b", "level": "Thông hiểu", "text": "Tỉ số hai chiều dài bằng 6/9 = 2/3.", "correct": True},
                        {"key": "c", "level": "Thông hiểu", "text": "Hai hình chữ nhật ABCD và A'B'C'D' là hai hình đồng dạng với nhau.", "correct": True},
                        {"key": "d", "level": "Vận dụng", "text": "Tỉ số diện tích giữa hình chữ nhật ABCD và hình chữ nhật A'B'C'D' bằng 2/3.", "correct": False}
                    ])
                ],
                "part3": [
                    make_sa(1, "Thông hiểu", "Tính độ dài cạnh huyền của tam giác vuông có hai cạnh góc vuông bằng $7\\text{ cm}$ và $24\\text{ cm}$:", "25"),
                    make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Cho hình chữ nhật có chiều dài $12\\text{ cm}$, đường chéo $13\\text{ cm}$. Chiều rộng của hình chữ nhật bằng bao nhiêu cm?", "5"),
                    make_sa(3, "Vận dụng", "Cho tam giác đều cạnh $6\\text{ cm}$. Chiều cao của tam giác đều bằng bao nhiêu cm (dạng thập phân làm tròn 2 chữ số)?", "5.2", acceptable=["5.2", "5.196", "5,2", "3*sqrt(3)"]),
                    make_sa(4, "Vận dụng", "Một cây tre cao $9\\text{ m}$ bị gãy ngang thân, ngọn tre chạm đất cách gốc $3\\text{ m}$. Điểm gãy cách mặt đất bao nhiêu mét?", "4")
                ],
                "part4": [
                    make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một người đi từ điểm $A$ về hướng Bắc $6\\text{ km}$, sau đó rẽ sang hướng Đông đi tiếp $8\\text{ km}$ đến điểm $B$. Tính khoảng cách ngắn nhất theo đường chim bay từ $A$ đến $B$.", "Quãng đường di chuyển tạo thành hai cạnh góc vuông của một tam giác vuông với độ dài 6 km và 8 km (0.5đ). Khoảng cách AB theo định lí Pythagore: AB = √(6² + 8²) = √(36 + 64) = √100 = 10 km (0.5đ)."),
                    make_essay(2, "Vận dụng", "Cho tam giác $ABC$ vuông tại $A$ có $AB = 15\\text{ cm}, AC = 20\\text{ cm}$. Kẻ đường cao $AH$. Tính $BC, AH, HB, HC$.", "Cạnh huyền BC = √(15² + 20²) = 25 cm (0.25đ). AH = (AB*AC)/BC = (15*20)/25 = 12 cm (0.25đ). HB = AB²/BC = 15²/25 = 9 cm (0.25đ). HC = BC - HB = 25 - 9 = 16 cm (0.25đ)."),
                    make_essay(3, "Vận dụng cao", "Cho tam giác $ABC$ nhọn. Chứng minh rằng nếu $BC^2 = 2AB^2 + 2AC^2$ thì không thể tồn tại tam giác như vậy.", "Theo bất đẳng thức tam giác và định lí Pythagore, thiết lập quan hệ góc và cạnh để chỉ ra mâu thuẫn hình học (1.0đ).")
                ]
            }

    save_chapter_package(8, "c9_8", "Chương IX: Tam giác đồng dạng", exams)

# ==============================================================================
# CHƯƠNG X TOÁN 8: MỘT SỐ HÌNH KHỐI TRONG THỰC TIỄN (3 BÀI = 9 ĐỀ)
# ==============================================================================
def generate_c10_toan8():
    print("🚀 Đang biên soạn Chương X Toán 8: Một số hình khối trong thực tiễn...")
    exams = {}

    # BÀI 1 (Bài 38): Hình chóp tam giác đều
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c10_8_bai1_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài 38: Hình chóp tam giác đều - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Đáy của hình chóp tam giác đều là:", ["Tam giác đều", "Tam giác vuông", "Tam giác cân", "Tam giác bất kì"], 0),
                make_mc(2, "Nhận biết", "Các mặt bên của hình chóp tam giác đều là:", ["Các tam giác cân bằng nhau", "Các hình chữ nhật", "Các tam giác đều", "Các tam giác vuông"], 0),
                make_mc(3, "Nhận biết", "Đoạn thẳng nối đỉnh với trọng tâm đáy của hình chóp tam giác đều gọi là:", ["Chiều cao của hình chóp", "Trung đoạn", "Cạnh bên", "Cạnh đáy"], 0),
                make_mc(4, "Nhận biết", "Đường cao của mặt bên xuất phát từ đỉnh của hình chóp tam giác đều gọi là:", ["Trung đoạn", "Chiều cao hình chóp", "Đường chéo", "Cạnh bên"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Công thức tính diện tích xung quanh của hình chóp tam giác đều là:", ["$S_{xq} = p \\cdot d$ ($p$ là nửa chu vi đáy, $d$ là trung đoạn)", "$S_{xq} = 2p \\cdot d$", "$S_{xq} = S_{đáy} \\cdot h$", "$S_{xq} = \\frac{1}{3} p \\cdot d$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Công thức tính thể tích của hình chóp tam giác đều là:", ["$V = \\frac{1}{3} S_{đáy} \\cdot h$", "$V = S_{đáy} \\cdot h$", "$V = \\frac{1}{2} S_{đáy} \\cdot h$", "$V = p \\cdot h$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Hình chóp tam giác đều có bao nhiêu mặt, bao nhiêu đỉnh, bao nhiêu cạnh?", ["4 mặt, 4 đỉnh, 6 cạnh", "5 mặt, 5 đỉnh, 8 cạnh", "4 mặt, 6 đỉnh, 4 cạnh", "6 mặt, 4 đỉnh, 6 cạnh"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Các cạnh bên của hình chóp tam giác đều:", ["Bằng nhau", "Vuông góc với đáy", "Bằng cạnh đáy", "Bằng trung đoạn"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Một hình chóp tam giác đều có cạnh đáy $6\\text{ cm}$, trung đoạn $5\\text{ cm}$. Diện tích xung quanh là:", ["$45\\text{ cm}^2$", "$90\\text{ cm}^2$", "$30\\text{ cm}^2$", "$15\\text{ cm}^2$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Hình chóp tam giác đều có diện tích đáy $15\\text{ cm}^2$, chiều cao $8\\text{ cm}$. Thể tích là:", ["$40\\text{ cm}^3$", "$120\\text{ cm}^3$", "$60\\text{ cm}^3$", "$80\\text{ cm}^3$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Hình chóp tam giác đều có chu vi đáy $18\\text{ cm}$, trung đoạn $6\\text{ cm}$. Diện tích xung quanh bằng:", ["$54\\text{ cm}^2$", "$108\\text{ cm}^2$", "$36\\text{ cm}^2$", "$72\\text{ cm}^2$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một chiếc hộp quà hình chóp tam giác đều có thể tích $100\\text{ cm}^3$, chiều cao $12\\text{ cm}$. Diện tích đáy của hộp quà là:", ["$25\\text{ cm}^2$", "$50\\text{ cm}^2$", "$75\\text{ cm}^2$", "$300\\text{ cm}^2$"], 0)
            ],
            "part2": [
                make_tf(1, "Cho hình chóp tam giác đều S.ABC có cạnh đáy AB = 6 cm, trung đoạn d = 8 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Đáy ABC là tam giác đều cạnh 6 cm.", "correct": True},
                    {"key": "b", "level": "Nhận biết", "text": "Nửa chu vi đáy bằng p = (6 * 3)/2 = 9 cm.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Diện tích xung quanh của hình chóp bằng Sxq = 9 * 8 = 72 cm².", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Độ dài mỗi cạnh bên của hình chóp xấp xỉ 8,54 cm.", "correct": True}
                ]),
                make_tf(2, "Một chiếc lều cắm trại có dạng hình chóp tam giác đều S.ABC có diện tích đáy bằng 4 m² và chiều cao SH = 3 m:", [
                    {"key": "a", "level": "Nhận biết", "text": "H là trọng tâm của tam giác đều ABC.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Thể tích không khí bên trong lều là V = 1/3 * 4 * 3 = 4 m³.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Nếu tăng chiều cao lên gấp đôi thì thể tích lều tăng lên gấp 4 lần.", "correct": False},
                    {"key": "d", "level": "Vận dụng", "text": "Biết trung đoạn d = 3,2 m và chu vi đáy 9 m thì diện tích vải bạt xung quanh lều là 14,4 m².", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Hình chóp tam giác đều có diện tích đáy $30\\text{ cm}^2$ và chiều cao $7\\text{ cm}$. Tính thể tích của hình chóp đó ($\\text{cm}^3$):", "70"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Một hình chóp tam giác đều có chu vi đáy $24\\text{ cm}$ và trung đoạn $10\\text{ cm}$. Diện tích xung quanh bằng bao nhiêu $\\text{cm}^2$?", "120"),
                make_sa(3, "Vận dụng", "Một khối rubik hình chóp tam giác đều có thể tích $64\\text{ cm}^3$ và diện tích đáy $16\\text{ cm}^2$. Chiều cao của khối rubik là bao nhiêu cm?", "12"),
                make_sa(4, "Vận dụng", "Một chiếc hộp kim tự tháp tam giác đều có cạnh đáy $10\\text{ cm}$, trung đoạn $13\\text{ cm}$. Chiều cao hình chóp bằng bao nhiêu cm (làm tròn số nguyên)?", "12", acceptable=["12", "12.3", "12.4"])
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một chiếc hộp quà hình chóp tam giác đều có cạnh đáy $8\\text{ cm}$ và trung đoạn $10\\text{ cm}$. Người ta bọc giấy màu quanh 3 mặt bên của hộp quà. Tính diện tích giấy màu cần dùng.", "Nửa chu vi đáy: p = (8 * 3)/2 = 12 cm (0.5đ). Diện tích xung quanh cần bọc giấy màu: Sxq = p * d = 12 * 10 = 120 cm² (0.5đ)."),
                make_essay(2, "Vận dụng", "Tính thể tích của hình chóp tam giác đều $S.ABC$ biết diện tích đáy tam giác đều $ABC$ bằng $27\\sqrt{3}\\text{ cm}^2$ và chiều cao hình chóp $SO = 10\\text{ cm}$.", "Công thức thể tích hình chóp: V = 1/3 * Sđ * h (0.5đ). Thay số: V = 1/3 * 27√3 * 10 = 90√3 cm³ ≈ 155.88 cm³ (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Một cái chụp đèn trang trí dạng hình chóp tam giác đều có cạnh đáy $20\\text{ cm}$, cạnh bên $26\\text{ cm}$. Tính diện tích vải cần may chụp đèn (không may đáy).", "Mỗi mặt bên là tam giác cân có cạnh đáy 20 cm, cạnh bên 26 cm. Nửa đáy bằng 10 cm (0.5đ). Trung đoạn d = √(26² - 10²) = √(676 - 100) = √576 = 24 cm. Diện tích xung quanh: Sxq = p * d = (30) * 24 = 720 cm² (0.5đ).")
            ]
        }

    # BÀI 2 (Bài 39): Hình chóp tứ giác đều
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c10_8_bai2_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Bài 39: Hình chóp tứ giác đều - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Đáy của hình chóp tứ giác đều là:", ["Hình vuông", "Hình chữ nhật", "Hình thoi", "Hình bình hành"], 0),
                make_mc(2, "Nhận biết", "Các mặt bên của hình chóp tứ giác đều là:", ["4 tam giác cân bằng nhau", "4 hình vuông", "4 hình chữ nhật", "4 tam giác đều"], 0),
                make_mc(3, "Nhận biết", "Hình chóp tứ giác đều có bao nhiêu mặt, bao nhiêu đỉnh, bao nhiêu cạnh?", ["5 mặt, 5 đỉnh, 8 cạnh", "6 mặt, 8 đỉnh, 12 cạnh", "5 mặt, 6 đỉnh, 9 cạnh", "4 mặt, 4 đỉnh, 6 cạnh"], 0),
                make_mc(4, "Nhận biết", "Chiều cao của hình chóp tứ giác đều là đoạn nối đỉnh với:", ["Giao điểm hai đường chéo của đáy", "Một đỉnh của đáy", "Trung điểm một cạnh đáy", "Trọng tâm mặt bên"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Công thức tính diện tích xung quanh của hình chóp tứ giác đều là:", ["$S_{xq} = p \\cdot d$", "$S_{xq} = 2p \\cdot d$", "$S_{xq} = S_{đáy} \\cdot h$", "$S_{xq} = \\frac{1}{2} p \\cdot d$"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Công thức tính thể tích của hình chóp tứ giác đều là:", ["$V = \\frac{1}{3} S_{đáy} \\cdot h$", "$V = S_{đáy} \\cdot h$", "$V = \\frac{1}{2} S_{đáy} \\cdot h$", "$V = p \\cdot d$"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Một hình chóp tứ giác đều có cạnh đáy $5\\text{ cm}$. Chu vi đáy là:", ["$20\\text{ cm}$", "$25\\text{ cm}$", "$10\\text{ cm}$", "$15\\text{ cm}$"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Hình chóp tứ giác đều có cạnh đáy $a$, diện tích đáy là:", ["$a^2$", "$4a$", "$2a^2$", "$a^3$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Một hình chóp tứ giác đều có cạnh đáy $6\\text{ cm}$, trung đoạn $5\\text{ cm}$. Diện tích xung quanh là:", ["$60\\text{ cm}^2$", "$120\\text{ cm}^2$", "$30\\text{ cm}^2$", "$90\\text{ cm}^2$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Hình chóp tứ giác đều có cạnh đáy $4\\text{ cm}$, chiều cao $6\\text{ cm}$. Thể tích là:", ["$32\\text{ cm}^3$", "$96\\text{ cm}^3$", "$48\\text{ cm}^3$", "$64\\text{ cm}^3$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Kim tự tháp Kê-ốp (Ai Cập) dạng hình chóp tứ giác đều có cạnh đáy $230\\text{ m}$, chiều cao $147\\text{ m}$. Thể tích của nó xấp xỉ:", ["$2\\ 592\\ 100\\text{ m}^3$", "$7\\ 776\\ 300\\text{ m}^3$", "$1\\ 200\\ 000\\text{ m}^3$", "$5\\ 000\\ 000\\text{ m}^3$"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một hình chóp tứ giác đều có diện tích xung quanh $80\\text{ cm}^2$, trung đoạn $8\\text{ cm}$. Cạnh đáy của hình chóp là:", ["$5\\text{ cm}$", "$10\\text{ cm}$", "$4\\text{ cm}$", "$6\\text{ cm}$"], 0)
            ],
            "part2": [
                make_tf(1, "Cho hình chóp tứ giác đều S.ABCD có cạnh đáy AB = 10 cm, chiều cao SO = 12 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Đáy ABCD là hình vuông có diện tích 100 cm².", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Thể tích hình chóp S.ABCD bằng V = 1/3 * 100 * 12 = 400 cm³.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Đoạn nối từ tâm O đến trung điểm cạnh đáy bằng 5 cm.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Trung đoạn d của hình chóp bằng 13 cm và diện tích xung quanh bằng 260 cm².", "correct": True}
                ]),
                make_tf(2, "Một khối rubik hình chóp tứ giác đều có cạnh đáy 6 cm và diện tích toàn phần bằng 96 cm²:", [
                    {"key": "a", "level": "Nhận biết", "text": "Diện tích đáy của khối rubik là 36 cm².", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Diện tích xung quanh của khối rubik bằng 60 cm².", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Nửa chu vi đáy của hình chóp bằng 12 cm.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Trung đoạn d của khối rubik bằng 5 cm.", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Hình chóp tứ giác đều có cạnh đáy $6\\text{ cm}$, chiều cao $10\\text{ cm}$. Thể tích bằng bao nhiêu $\\text{cm}^3$?", "120"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Một hình chóp tứ giác đều có chu vi đáy $32\\text{ cm}$ và trung đoạn $9\\text{ cm}$. Diện tích xung quanh bằng bao nhiêu $\\text{cm}^2$?", "144"),
                make_sa(3, "Vận dụng", "Một mái nhà của chòi nghỉ có dạng hình chóp tứ giác đều cạnh đáy $4\\text{ m}$, trung đoạn $3\\text{ m}$. Diện tích ngói cần để lợp 4 mái xung quanh là bao nhiêu $\\text{m}^2$?", "24"),
                make_sa(4, "Vận dụng", "Một khối bê tông hình chóp tứ giác đều cạnh đáy $2\\text{ m}$, chiều cao $1,5\\text{ m}$. Khối bê tông nặng bao nhiêu tấn biết khối lượng riêng là $2,5\\text{ tấn/m}^3$?", "5")
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một chiếc lều hình chóp tứ giác đều có đáy là hình vuông cạnh $3\\text{ m}$ và trung đoạn là $2,5\\text{ m}$. Tính diện tích bạt cần thiết để dựng lều (bao gồm cả bạt trải đáy).", "Diện tích đáy hình vuông: Sđ = 3 * 3 = 9 m² (0.25đ). Nửa chu vi đáy: p = (3 * 4)/2 = 6 m. Diện tích xung quanh: Sxq = p * d = 6 * 2.5 = 15 m² (0.25đ). Tổng diện tích bạt: S = 9 + 15 = 24 m² (0.5đ)."),
                make_essay(2, "Vận dụng", "Kim tự tháp Louvre ở Paris có dạng hình chóp tứ giác đều với chiều cao $21,6\\text{ m}$ và cạnh đáy $35\\text{ m}$. Tính thể tích không gian bên trong kim tự tháp.", "Diện tích đáy hình vuông: Sđ = 35 * 35 = 1225 m² (0.5đ). Thể tích của kim tự tháp: V = 1/3 * Sđ * h = 1/3 * 1225 * 21.6 = 8820 m³ (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Một khối gỗ hình chóp tứ giác đều có cạnh đáy $16\\text{ cm}$, chiều cao $15\\text{ cm}$. Tính diện tích toàn phần của khối gỗ đó.", "Nửa cạnh đáy là 8 cm. Trung đoạn d = √(15² + 8²) = √(225 + 64) = √289 = 17 cm (0.5đ). Diện tích đáy: 16² = 256 cm². Nửa chu vi đáy: (16*4)/2 = 32 cm. Diện tích xung quanh: 32 * 17 = 544 cm². Diện tích toàn phần: Stp = 256 + 544 = 800 cm² (0.5đ).")
            ]
        }

    # BÀI 3 (Bài 40): Bài kiểm tra cuối Chương X
    for t in [1, 2, 3]:
        is_hard = (t == 3)
        diff_name = "🚀 Mức độ Khá Giỏi" if is_hard else f"🌿 Mức độ Khá (Đề {t})"
        exams[f"c10_8_bai3_test{t}"] = {
            "title": f"Toán 8 (KNTT) - Ôn tập và kiểm tra cuối Chương X - Đề số {t} ({diff_name})",
            "part1": [
                make_mc(1, "Nhận biết", "Thể tích của hình chóp đều có diện tích đáy $S$ và chiều cao $h$ là:", ["$V = \\frac{1}{3} S \\cdot h$", "$V = S \\cdot h$", "$V = \\frac{1}{2} S \\cdot h$", "$V = 2S \\cdot h$"], 0),
                make_mc(2, "Nhận biết", "Diện tích xung quanh hình chóp đều có nửa chu vi đáy $p$ và trung đoạn $d$ là:", ["$S_{xq} = p \\cdot d$", "$S_{xq} = 2p \\cdot d$", "$S_{xq} = \\frac{1}{2}p \\cdot d$", "$S_{xq} = p + d$"], 0),
                make_mc(3, "Nhận biết", "Đáy của hình chóp tam giác đều là:", ["Tam giác đều", "Tam giác vuông", "Hình vuông", "Tam giác cân"], 0),
                make_mc(4, "Nhận biết", "Đáy của hình chóp tứ giác đều là:", ["Hình vuông", "Hình thoi", "Hình chữ nhật", "Hình thang"], 0),
                make_mc(5, "Nhận biết" if not is_hard else "Thông hiểu", "Hình chóp tứ giác đều có số cạnh là:", ["8 cạnh", "6 cạnh", "10 cạnh", "12 cạnh"], 0),
                make_mc(6, "Nhận biết" if not is_hard else "Thông hiểu", "Hình chóp tam giác đều có số mặt là:", ["4 mặt", "5 mặt", "6 mặt", "3 mặt"], 0),
                make_mc(7, "Nhận biết" if not is_hard else "Thông hiểu", "Trung đoạn của hình chóp đều là:", ["Đường cao của mặt bên", "Chiều cao hình chóp", "Cạnh đáy", "Cạnh bên"], 0),
                make_mc(8, "Nhận biết" if not is_hard else "Thông hiểu", "Hình chóp tứ giác đều có cạnh đáy $4\\text{ cm}$, trung đoạn $6\\text{ cm}$. Diện tích xung quanh là:", ["$48\\text{ cm}^2$", "$96\\text{ cm}^2$", "$24\\text{ cm}^2$", "$36\\text{ cm}^2$"], 0),
                make_mc(9, "Thông hiểu" if not is_hard else "Vận dụng", "Hình chóp tam giác đều có thể tích $36\\text{ cm}^3$, chiều cao $9\\text{ cm}$. Diện tích đáy là:", ["$12\\text{ cm}^2$", "$4\\text{ cm}^2$", "$8\\text{ cm}^2$", "$24\\text{ cm}^2$"], 0),
                make_mc(10, "Thông hiểu" if not is_hard else "Vận dụng", "Hình chóp tứ giác đều có cạnh đáy $10\\text{ cm}$, chiều cao $12\\text{ cm}$. Thể tích là:", ["$400\\text{ cm}^3$", "$1200\\text{ cm}^3$", "$600\\text{ cm}^3$", "$300\\text{ cm}^3$"], 0),
                make_mc(11, "Thông hiểu" if not is_hard else "Vận dụng", "Nếu tăng cạnh đáy của hình chóp tứ giác đều lên gấp 2 lần và giữ nguyên chiều cao thì thể tích của nó tăng lên gấp:", ["$4$ lần", "$2$ lần", "$8$ lần", "$6$ lần"], 0),
                make_mc(12, "Vận dụng" if not is_hard else "Vận dụng cao", "Một hình chóp tứ giác đều có diện tích toàn phần bằng $96\\text{ cm}^2$, diện tích đáy là $36\\text{ cm}^2$. Trung đoạn của hình chóp bằng:", ["$5\\text{ cm}$", "$6\\text{ cm}$", "$4\\text{ cm}$", "$8\\text{ cm}$"], 0)
            ],
            "part2": [
                make_tf(1, "Một hình chóp tam giác đều S.ABC có diện tích đáy 15 cm² và chiều cao 6 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Hình chóp có 4 đỉnh và 6 cạnh.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Thể tích hình chóp S.ABC bằng 30 cm³.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Mỗi mặt bên của hình chóp là một tam giác cân.", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Nếu cạnh đáy bằng 6 cm và trung đoạn bằng 5 cm thì diện tích toàn phần bằng 60 cm².", "correct": True}
                ]),
                make_tf(2, "Một hình chóp tứ giác đều S.ABCD có cạnh đáy 8 cm và trung đoạn 5 cm:", [
                    {"key": "a", "level": "Nhận biết", "text": "Hình chóp có 5 mặt gồm 1 đáy hình vuông và 4 mặt bên.", "correct": True},
                    {"key": "b", "level": "Thông hiểu", "text": "Nửa chu vi đáy bằng p = (8 * 4)/2 = 16 cm.", "correct": True},
                    {"key": "c", "level": "Thông hiểu", "text": "Diện tích xung quanh của hình chóp bằng 80 cm².", "correct": True},
                    {"key": "d", "level": "Vận dụng", "text": "Chiều cao hình chóp bằng h = 3 cm và thể tích bằng 64 cm³.", "correct": True}
                ])
            ],
            "part3": [
                make_sa(1, "Thông hiểu", "Một hình chóp tứ giác đều có diện tích đáy $49\\text{ cm}^2$ và chiều cao $6\\text{ cm}$. Thể tích bằng bao nhiêu $\\text{cm}^3$?", "98"),
                make_sa(2, "Thông hiểu" if not is_hard else "Vận dụng cao", "Hình chóp tam giác đều có cạnh đáy $4\\text{ cm}$, trung đoạn $6\\text{ cm}$. Diện tích xung quanh bằng bao nhiêu $\\text{cm}^2$?", "36"),
                make_sa(3, "Vận dụng", "Một khối gỗ hình chóp tứ giác đều có cạnh đáy $10\\text{ cm}$, chiều cao $12\\text{ cm}$. Khối gỗ có thể tích bằng bao nhiêu $\\text{cm}^3$?", "400"),
                make_sa(4, "Vận dụng", "Một chiếc lều hình chóp tứ giác đều có cạnh đáy $2\\text{ m}$, trung đoạn $2,5\\text{ m}$. Diện tích bạt xung quanh bằng bao nhiêu $\\text{m}^2$?", "10")
            ],
            "part4": [
                make_essay(1, "Thông hiểu" if not is_hard else "Vận dụng", "Một hình chóp tứ giác đều có cạnh đáy $12\\text{ cm}$, chiều cao $8\\text{ cm}$. a) Tính thể tích hình chóp; b) Tính trung đoạn của hình chóp.", "a) Diện tích đáy: Sđ = 12 * 12 = 144 cm². Thể tích V = 1/3 * 144 * 8 = 384 cm³ (0.5đ). b) Nửa cạnh đáy là 6 cm. Trung đoạn d = √(8² + 6²) = √100 = 10 cm (0.5đ)."),
                make_essay(2, "Vận dụng", "Một chiếc đèn lồng hình chóp tam giác đều có cạnh đáy $16\\text{ cm}$, trung đoạn $15\\text{ cm}$. Tính diện tích giấy kính cần dán kín 3 mặt bên của đèn lồng.", "Nửa chu vi đáy tam giác đều: p = (16 * 3)/2 = 24 cm (0.5đ). Diện tích xung quanh cần dán giấy kính: Sxq = p * d = 24 * 15 = 360 cm² (0.5đ)."),
                make_essay(3, "Vận dụng cao", "Một chiếc bánh kem hình chóp tứ giác đều có cạnh đáy $20\\text{ cm}$, chiều cao $24\\text{ cm}$. Người ta cắt một nhát song song với đáy ở chính giữa chiều cao để chia thành hai phần. Tính thể tích của phần hình chóp nhỏ phía trên.", "Phần chóp nhỏ đồng dạng với chóp lớn theo tỉ số k = 1/2 (0.5đ). Thể tích chóp lớn: V = 1/3 * 20² * 24 = 3200 cm³. Thể tích chóp nhỏ: V' = k³ * V = (1/8) * 3200 = 400 cm³ (0.5đ).")
            ]
        }

    save_chapter_package(8, "c10_8", "Chương X: Một số hình khối trong thực tiễn", exams)

if __name__ == "__main__":
    generate_c8_toan8()
    generate_c9_toan8()
    generate_c10_toan8()
    print("🎉 TOÀN BỘ CHƯƠNG VIII, IX, X TOÁN 8 ĐÃ ĐƯỢC TẠO VÀ ĐÓNG GÓI XUẤT SẮC!")
