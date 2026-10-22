import { CHAPTER1_TOAN8_EXAMS } from './chapter1Toan8Exams.js';
// ==============================================================================
// NGÂN HÀNG ĐỀ THI CHUẨN MA TRẬN 2025 (BÀI KIỂM TRA SỐ 1, 2, 3)
// Đầy đủ 4 phần (10.0 điểm):
// - Phần I (3.0đ): 12 câu TN nhiều lựa chọn (6 Nhận biết, 6 Thông hiểu)
// - Phần II (2.0đ): 2 câu Đúng/Sai (mỗi câu 4 ý, chấm lũy tiến 0.1 - 0.25 - 0.5 - 1.0)
// - Phần III (2.0đ): 4 câu Trả lời ngắn (1 TH, 2 VD thấp, 1 VD cao)
// - Phần IV (3.0đ): 3 câu Tự luận (1 TH, 1 VD thấp, 1 VD cao có biểu điểm rubric)
// ==============================================================================

export const EXAM_BANK = {
  // -------------------------------------------------------------
  // TOÁN 9 - BÀI 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn
  // -------------------------------------------------------------
  "9_c1_9_Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn": {
    "1": {
      title: "Toán 9 (KNTT) - Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn - Bài kiểm tra số 1",
      part1: [
        { id: 1, level: "Nhận biết", question: "Phương trình nào sau đây là phương trình bậc nhất hai ẩn $x, y$?", options: ["$2x + 3y = 5$", "$x^2 + y = 1$", "$0x + 0y = 3$", "$2x - \\frac{1}{y} = 0$"], correct: 0 },
        { id: 2, level: "Nhận biết", question: "Trong phương trình $3x - 5y = 7$, các hệ số $a, b, c$ lần lượt là:", options: ["$a=3, b=5, c=7$", "$a=3, b=-5, c=7$", "$a=3, b=-5, c=-7$", "$a=-5, b=3, c=7$"], correct: 1 },
        { id: 3, level: "Nhận biết", question: "Cặp số $(x; y) = (1; 2)$ là nghiệm của phương trình nào dưới đây?", options: ["$2x + y = 3$", "$x + 2y = 5$", "$3x - y = 0$", "$x - y = 1$"], correct: 1 },
        { id: 4, level: "Nhận biết", question: "Hệ phương trình nào sau đây là hệ hai phương trình bậc nhất hai ẩn?", options: ["$\\begin{cases} x + y = 2 \\\\ x^2 - y = 1 \\end{cases}$", "$\\begin{cases} 2x - y = 3 \\\\ x + 3y = -1 \\end{cases}$", "$\\begin{cases} 0x + 0y = 1 \\\\ x + y = 2 \\end{cases}$", "$\\begin{cases} xy = 2 \\\\ x + y = 3 \\end{cases}$"], correct: 1 },
        { id: 5, level: "Nhận biết", question: "Tập nghiệm của phương trình $0x + 2y = 6$ được biểu diễn bởi đường thẳng nào trên mặt phẳng tọa độ?", options: ["$y = 3$", "$x = 3$", "$y = 6$", "$y = 2x + 6$"], correct: 0 },
        { id: 6, level: "Nhận biết", question: "Tập nghiệm của phương trình $3x + 0y = -9$ được biểu diễn bởi đường thẳng:", options: ["$y = -3$", "$x = 3$", "$x = -3$", "$y = 3x - 9$"], correct: 2 },
        { id: 7, level: "Thông hiểu", question: "Nghiệm tổng quát của phương trình $2x - y = 4$ là:", options: ["$(x \\in \\mathbb{R}; y = 2x - 4)$", "$(x \\in \\mathbb{R}; y = 4 - 2x)$", "$(x = 2y + 4; y \\in \\mathbb{R})$", "$(x \\in \\mathbb{R}; y = 2x + 4)$"], correct: 0 },
        { id: 8, level: "Thông hiểu", question: "Cho phương trình $x + 3y = 7$. Nếu $x = 1$ thì giá trị của $y$ bằng:", options: ["$y = 3$", "$y = 2$", "$y = -2$", "$y = 6$"], correct: 1 },
        { id: 9, level: "Thông hiểu", question: "Cặp số $(2; -1)$ là nghiệm của hệ phương trình nào sau đây?", options: ["$\\begin{cases} x + y = 1 \\\\ 2x - y = 5 \\end{cases}$", "$\\begin{cases} x + y = 1 \\\\ 2x + y = 5 \\end{cases}$", "$\\begin{cases} x - y = 3 \\\\ x + y = -1 \\end{cases}$", "$\\begin{cases} 2x + y = 3 \\\\ x - 2y = 0 \\end{cases}$"], correct: 0 },
        { id: 10, level: "Thông hiểu", question: "Đường thẳng biểu diễn tất cả các nghiệm của phương trình $2x + y = 4$ cắt trục tung $Oy$ tại điểm có tung độ bằng:", options: ["$2$", "$4$", "$-4$", "$-2$"], correct: 1 },
        { id: 11, level: "Thông hiểu", question: "Tìm tham số $m$ để cặp số $(-1; 2)$ là một nghiệm của phương trình $mx + 3y = 4$.", options: ["$m = 2$", "$m = -2$", "$m = 10$", "$m = -10$"], correct: 0 },
        { id: 12, level: "Thông hiểu", question: "Số nghiệm của phương trình bậc nhất hai ẩn $ax + by = c$ (với $a \\neq 0$ hoặc $b \\neq 0$) là:", options: ["Vô nghiệm", "Có duy nhất 1 nghiệm", "Có đúng 2 nghiệm", "Có vô số nghiệm"], correct: 3 }
      ],
      part2: [
        {
          id: 1,
          stem: "Cho phương trình bậc nhất hai ẩn: $2x - y = 3$ (1).",
          statements: [
            { key: "a", level: "Thông hiểu", text: "Cặp số $(2; 1)$ là một nghiệm của phương trình (1).", correct: true },
            { key: "b", level: "Thông hiểu", text: "Mọi nghiệm của phương trình (1) đều có dạng $(x; 2x + 3)$ với $x \\in \\mathbb{R}$.", correct: false },
            { key: "c", level: "Vận dụng thấp", text: "Đường thẳng biểu diễn tập nghiệm của (1) đi qua giao điểm của hai đường thẳng $x = 1$ và $y = -1$.", correct: true },
            { key: "d", level: "Vận dụng thấp", text: "Diện tích tam giác tạo bởi đường thẳng $2x - y = 3$ với hai trục tọa độ $Ox, Oy$ bằng $2,25$ (đvdt).", correct: true }
          ]
        },
        {
          id: 2,
          stem: "Cho hệ hai phương trình bậc nhất hai ẩn: $\\begin{cases} (m - 1)x + y = 2 \\\\ 2x + my = 5 \\end{cases}$ (với $m$ là tham số).",
          statements: [
            { key: "a", level: "Thông hiểu", text: "Khi $m = 2$, hệ phương trình trở thành $\\begin{cases} x + y = 2 \\\\ 2x + 2y = 5 \\end{cases}$.", correct: true },
            { key: "b", level: "Thông hiểu", text: "Khi $m = 1$, cặp số $(1; 2)$ là nghiệm của hệ phương trình đã cho.", correct: false },
            { key: "c", level: "Vận dụng thấp", text: "Để cặp số $(1; 1)$ là nghiệm của hệ phương trình thì $m = 3$.", correct: true },
            { key: "d", level: "Vận dụng thấp", text: "Khi $m = 2$, hai đường thẳng biểu diễn hai phương trình của hệ cắt nhau tại một điểm duy nhất.", correct: false }
          ]
        }
      ],
      part3: [
        { id: 1, level: "Thông hiểu", question: "Cho phương trình $3x + 2y = 12$. Tìm giá trị của $y$ khi $x = 2$.", answer: "3" },
        { id: 2, level: "Vận dụng thấp", question: "Biết cặp số $(a; 4)$ là nghiệm của phương trình $5x - 2y = 7$. Giá trị của $a$ bằng bao nhiêu?", answer: "3" },
        { id: 3, level: "Vận dụng thấp", question: "Tìm giá trị của tham số $m$ để cặp số $(2; -1)$ là nghiệm của phương trình $(2m - 1)x + 3y = 3$.", answer: "2" },
        { id: 4, level: "Vận dụng cao", question: "Một đường thẳng $(d): ax + by = 6$ đi qua hai điểm $A(2; 0)$ và $B(0; 3)$. Tính giá trị của biểu thức $T = 2a + 3b$.", answer: "12" }
      ],
      part4: [
        {
          id: 1,
          level: "Thông hiểu",
          question: "Viết nghiệm tổng quát của phương trình $3x - y = 6$ và xác định tọa độ giao điểm của đường thẳng biểu diễn tập nghiệm với hai trục tọa độ $Ox, Oy$.",
          rubric: "Nghiệm tổng quát: y = 3x - 6 (0.5đ). Giao điểm Ox là (2;0), giao điểm Oy là (0;-6) (0.5đ)."
        },
        {
          id: 2,
          level: "Vận dụng thấp",
          question: "Tìm các giá trị của tham số $m$ và $n$ để cặp số $(x; y) = (1; -2)$ là nghiệm của hệ phương trình: $\\begin{cases} mx - ny = 5 \\\\ nx + my = 0 \\end{cases}$.",
          rubric: "Thay (1; -2) vào hệ: m + 2n = 5 và n - 2m = 0 (0.5đ). Giải hệ tìm được m = 1, n = 2 và kết luận (0.5đ)."
        },
        {
          id: 3,
          level: "Vận dụng cao",
          question: "Tìm tất cả các cặp nghiệm nguyên dương $(x; y)$ của phương trình: $3x + 5y = 31$.",
          rubric: "Biến đổi x = (31 - 5y)/3 = 10 - 2y + (1+y)/3 (0.25đ). Do x, y nguyên dương nên 0 < y < 6.2 (0.25đ). Tìm được đúng 2 cặp nghiệm (7; 2) và (2; 5) (0.5đ)."
        }
      ]
    },
    "2": {
      title: "Toán 9 (KNTT) - Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn - Bài kiểm tra số 2",
      part1: [
        { id: 1, level: "Nhận biết", question: "Phương trình nào sau đây KHÔNG phải là phương trình bậc nhất hai ẩn?", options: ["$x - 4y = 0$", "$3x + 0y = -2$", "$x^2 - 2y = 3$", "$0x + 5y = 10$"], correct: 2 },
        { id: 2, level: "Nhận biết", question: "Cặp số nào sau đây là một nghiệm của phương trình $x - 2y = 3$?", options: ["$(3; 0)$", "$(1; -1)$", "$(5; 2)$", "$(0; 3)$"], correct: 0 },
        { id: 3, level: "Nhận biết", question: "Đường thẳng biểu diễn tập nghiệm của phương trình $x - y = 0$ là:", options: ["Trục hoành", "Trục tung", "Đường phân giác góc phần tư I và III", "Đường thẳng song song với trục hoành"], correct: 2 },
        { id: 4, level: "Nhận biết", question: "Cho hệ phương trình $\\begin{cases} x + y = 4 \\\\ x - y = 2 \\end{cases}$. Nghiệm của hệ là:", options: ["$(3; 1)$", "$(1; 3)$", "$(2; 2)$", "$(4; 0)$"], correct: 0 },
        { id: 5, level: "Nhận biết", question: "Trong hệ hai phương trình bậc nhất hai ẩn, nếu hai đường thẳng biểu diễn tập nghiệm song song với nhau thì hệ:", options: ["Có nghiệm duy nhất", "Vô nghiệm", "Có vô số nghiệm", "Có đúng 2 nghiệm"], correct: 1 },
        { id: 6, level: "Nhận biết", question: "Đường thẳng $d: y = 2$ là tập nghiệm của phương trình bậc nhất hai ẩn nào?", options: ["$2x + 0y = 2$", "$0x + y = 2$", "$x + y = 2$", "$0x + 2y = 1$"], correct: 1 },
        { id: 7, level: "Thông hiểu", question: "Nghiệm tổng quát của phương trình $x + 2y = 5$ biểu diễn theo $y$ là:", options: ["$(5 - 2y; y)$ với $y \\in \\mathbb{R}$", "$(5 + 2y; y)$ với $y \\in \\mathbb{R}$", "$(x; \\frac{5-x}{2})$ với $x \\in \\mathbb{R}$", "$(2y - 5; y)$ với $y \\in \\mathbb{R}$"], correct: 0 },
        { id: 8, level: "Thông hiểu", question: "Hệ phương trình $\\begin{cases} 2x - y = 3 \\\\ 4x - 2y = 6 \\end{cases}$ có bao nhiêu nghiệm?", options: ["Vô nghiệm", "1 nghiệm duy nhất", "2 nghiệm", "Vô số nghiệm"], correct: 3 },
        { id: 9, level: "Thông hiểu", question: "Giá trị của $k$ để cặp số $(1; 3)$ là nghiệm của phương trình $kx + 2y = 8$ là:", options: ["$k = 1$", "$k = 2$", "$k = -2$", "$k = 0$"], correct: 1 },
        { id: 10, level: "Thông hiểu", question: "Giao điểm của đường thẳng $3x - 2y = 6$ với trục hoành $Ox$ có tọa độ là:", options: ["$(0; -3)$", "$(2; 0)$", "$(0; 2)$", "$(-2; 0)$"], correct: 1 },
        { id: 11, level: "Thông hiểu", question: "Cho hệ phương trình $\\begin{cases} ax + y = 1 \\\\ x + ay = 1 \\end{cases}$. Với $a = 1$, hệ có số nghiệm là:", options: ["1 nghiệm", "Vô nghiệm", "Vô số nghiệm", "2 nghiệm"], correct: 2 },
        { id: 12, level: "Thông hiểu", question: "Cho phương trình $4x + 3y = 12$. Điểm nào sau đây KHÔNG thuộc đường thẳng biểu diễn tập nghiệm?", options: ["$A(0; 4)$", "$B(3; 0)$", "$C(1; 3)$", "$D(-3; 8)$"], correct: 2 }
      ],
      part2: [
        {
          id: 1,
          stem: "Xét phương trình bậc nhất hai ẩn $3x + 2y = 6$ (d).",
          statements: [
            { key: "a", level: "Thông hiểu", text: "Điểm $M(2; 0)$ thuộc đường thẳng (d).", correct: true },
            { key: "b", level: "Thông hiểu", text: "Hệ số góc của đường thẳng (d) là $k = -\\frac{3}{2}$.", correct: true },
            { key: "c", level: "Vận dụng thấp", text: "Đường thẳng (d) song song với đường thẳng $6x + 4y = 5$.", correct: true },
            { key: "d", level: "Vận dụng thấp", text: "Khoảng cách từ gốc tọa độ $O(0;0)$ đến đường thẳng (d) bằng $\\frac{6}{\\sqrt{13}}$.", correct: true }
          ]
        },
        {
          id: 2,
          stem: "Cho hệ phương trình $\\begin{cases} x - 2y = m \\\\ 2x + y = 5 \\end{cases}$.",
          statements: [
            { key: "a", level: "Thông hiểu", text: "Hệ luôn có nghiệm duy nhất với mọi giá trị của $m$.", correct: true },
            { key: "b", level: "Thông hiểu", text: "Khi $m = 0$, nghiệm của hệ là $(2; 1)$.", correct: true },
            { key: "c", level: "Vận dụng thấp", text: "Để hệ có nghiệm $(x; y)$ thỏa mãn $x > 0$ và $y > 0$ thì $-10 < m < \\frac{5}{2}$.", correct: true },
            { key: "d", level: "Vận dụng thấp", text: "Khi $m = 5$, hệ phương trình có vô số nghiệm.", correct: false }
          ]
        }
      ],
      part3: [
        { id: 1, level: "Thông hiểu", question: "Tìm hoành độ giao điểm của đường thẳng $2x + 5y = 10$ với trục hoành $Ox$.", answer: "5" },
        { id: 2, level: "Vận dụng thấp", question: "Cho hệ $\\begin{cases} 3x - y = 5 \\\\ x + 2y = 4 \\end{cases}$. Tính giá trị của biểu thức $P = x + y$.", answer: "3" },
        { id: 3, level: "Vận dụng thấp", question: "Tìm $m$ để hệ $\\begin{cases} mx + y = 3 \\\\ 4x + 2y = 6 \\end{cases}$ có vô số nghiệm.", answer: "2" },
        { id: 4, level: "Vận dụng cao", question: "Biết cặp $(x_0; y_0)$ là nghiệm duy nhất của hệ $\\begin{cases} 2x + 3y = 7 \\\\ 3x - y = 5 \\end{cases}$. Tính giá trị của $Q = x_0^2 + y_0^2$.", answer: "5" }
      ],
      part4: [
        {
          id: 1,
          level: "Thông hiểu",
          question: "Vẽ đường thẳng biểu diễn tập nghiệm của phương trình $2x - 3y = 6$ trên mặt phẳng tọa độ $Oxy$.",
          rubric: "Xác định đúng 2 điểm (3; 0) và (0; -2) (0.5đ). Vẽ hệ trục và đường thẳng chính xác (0.5đ)."
        },
        {
          id: 2,
          level: "Vận dụng thấp",
          question: "Giải hệ phương trình bằng phương pháp thế hoặc cộng đại số: $\\begin{cases} 3x + 2y = 7 \\\\ 2x - 3y = -4 \\end{cases}$.",
          rubric: "Khử một ẩn đúng (0.5đ). Tìm được x = 1, y = 2 và kết luận nghiệm (0.5đ)."
        },
        {
          id: 3,
          level: "Vận dụng cao",
          question: "Tìm các giá trị nguyên của tham số $m$ để hệ phương trình $\\begin{cases} mx + y = 2 \\\\ x + my = 2 \\end{cases}$ có nghiệm duy nhất $(x; y)$ nguyên.",
          rubric: "Điều kiện có nghiệm duy nhất m ≠ ±1 (0.25đ). Tính x = y = 2/(m+1) (0.25đ). m+1 là ước của 2 => m ∈ {-3, -2, 0, 1 nhưng loại 1} => kết luận (0.5đ)."
        }
      ]
    },
    "3": {
      title: "Toán 9 (KNTT) - Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn - Bài kiểm tra số 3",
      part1: [
        { id: 1, level: "Nhận biết", question: "Phương trình bậc nhất hai ẩn $ax + by = c$ có dạng tổng quát với điều kiện:", options: ["$a, b$ cùng bằng $0$", "$a \\neq 0$ hoặc $b \\neq 0$", "$a \\neq 0$ và $b \\neq 0$", "$c \\neq 0$"], correct: 1 },
        { id: 2, level: "Nhận biết", question: "Đường thẳng $x = -1$ song song với trục nào?", options: ["Trục $Ox$", "Trục $Oy$", "Đường thẳng $y = x$", "Đường thẳng $y = -x$"], correct: 1 },
        { id: 3, level: "Nhận biết", question: "Cặp số $(-2; 1)$ là nghiệm của phương trình nào?", options: ["$x + y = 1$", "$2x + y = -3$", "$x - 2y = 0$", "$3x + 2y = 4$"], correct: 1 },
        { id: 4, level: "Nhận biết", question: "Hệ hai phương trình bậc nhất hai ẩn vô nghiệm khi hai đường thẳng biểu diễn:", options: ["Cắt nhau", "Song song", "Trùng nhau", "Vuông góc"], correct: 1 },
        { id: 5, level: "Nhận biết", question: "Cho phương trình $0x + 3y = 9$. Nghiệm tổng quát của phương trình là:", options: ["$(x \\in \\mathbb{R}; y = 3)$", "$(x = 3; y \\in \\mathbb{R})$", "$(3; 3)$", "$(0; 3)$"], correct: 0 },
        { id: 6, level: "Nhận biết", question: "Nghiệm của hệ $\\begin{cases} 2x = 4 \\\\ x + y = 5 \\end{cases}$ là:", options: ["$(2; 3)$", "$(3; 2)$", "$(4; 1)$", "$(2; 5)$"], correct: 0 },
        { id: 7, level: "Thông hiểu", question: "Tìm $m$ để đường thẳng $mx - y = 2$ đi qua điểm $A(1; -1)$.", options: ["$m = 1$", "$m = -1$", "$m = 3$", "$m = -3$"], correct: 0 },
        { id: 8, level: "Thông hiểu", question: "Số cặp số nguyên dương $(x; y)$ thỏa mãn phương trình $x + y = 4$ là:", options: ["$1$", "$2$", "$3$", "$4$"], correct: 2 },
        { id: 9, level: "Thông hiểu", question: "Hệ phương trình $\\begin{cases} x - y = 1 \\\\ 2x - 2y = 3 \\end{cases}$:", options: ["Có nghiệm duy nhất", "Vô số nghiệm", "Vô nghiệm", "Có 2 nghiệm"], correct: 2 },
        { id: 10, level: "Thông hiểu", question: "Giao điểm của hai đường thẳng $x + y = 3$ và $x - y = 1$ nằm ở góc phần tư thứ mấy?", options: ["Thứ I", "Thứ II", "Thứ III", "Thứ IV"], correct: 0 },
        { id: 11, level: "Thông hiểu", question: "Cho phương trình $3x - 4y = 12$. Tung độ gốc của đường thẳng biểu diễn tập nghiệm là:", options: ["$4$", "$-3$", "$3$", "$-4$"], correct: 1 },
        { id: 12, level: "Thông hiểu", question: "Hệ phương trình $\\begin{cases} ax + by = c \\\\ a'x + b'y = c' \\end{cases}$ có nghiệm duy nhất khi:", options: ["$\\frac{a}{a'} \\neq \\frac{b}{b'}$", "$\\frac{a}{a'} = \\frac{b}{b'} \\neq \\frac{c}{c'}$", "$\\frac{a}{a'} = \\frac{b}{b'} = \\frac{c}{c'}$", "Không có điều kiện nào"], correct: 0 }
      ],
      part2: [
        {
          id: 1,
          stem: "Cho hai đường thẳng $(d_1): 2x - y = 4$ và $(d_2): x + y = 2$.",
          statements: [
            { key: "a", level: "Thông hiểu", text: "$(d_1)$ cắt trục tung tại điểm có tọa độ $(0; -4)$.", correct: true },
            { key: "b", level: "Thông hiểu", text: "Giao điểm của $(d_1)$ và $(d_2)$ là điểm $M(2; 0)$.", correct: true },
            { key: "c", level: "Vận dụng thấp", text: "Góc tạo bởi đường thẳng $(d_1)$ với chiều dương trục hoành là góc nhọn.", correct: true },
            { key: "d", level: "Vận dụng thấp", text: "Hai đường thẳng $(d_1)$ và $(d_2)$ vuông góc với nhau.", correct: false }
          ]
        },
        {
          id: 2,
          stem: "Cho hệ phương trình $\\begin{cases} 2x + ay = b \\\\ ax - y = 1 \\end{cases}$.",
          statements: [
            { key: "a", level: "Thông hiểu", text: "Khi $a = 0$, hệ trở thành $\\begin{cases} 2x = b \\\\ -y = 1 \\end{cases}$.", correct: true },
            { key: "b", level: "Thông hiểu", text: "Hệ có nghiệm duy nhất với mọi giá trị của tham số $a$.", correct: true },
            { key: "c", level: "Vận dụng thấp", text: "Để hệ nhận $(1; 1)$ làm nghiệm thì $a = 2$ và $b = 4$.", correct: true },
            { key: "d", level: "Vận dụng thấp", text: "Có giá trị của $a$ để hệ vô nghiệm.", correct: false }
          ]
        }
      ],
      part3: [
        { id: 1, level: "Thông hiểu", question: "Cho phương trình $4x - 3y = 24$. Khi $y = 0$, giá trị của $x$ bằng bao nhiêu?", answer: "6" },
        { id: 2, level: "Vận dụng thấp", question: "Tìm giá trị của $m$ để hệ $\\begin{cases} x + 2y = 4 \\\\ 2x + my = 8 \\end{cases}$ có vô số nghiệm.", answer: "4" },
        { id: 3, level: "Vận dụng thấp", question: "Tìm $a$ để đường thẳng $(d): ax - 2y = 4$ đi qua điểm $K(3; 1)$.", answer: "2" },
        { id: 4, level: "Vận dụng cao", question: "Cho hệ $\\begin{cases} x + y = 5 \\\\ 2x - y = 1 \\end{cases}$. Tính giá trị biểu thức $T = x^2 - y^2$.", answer: "-5" }
      ],
      part4: [
        {
          id: 1,
          level: "Thông hiểu",
          question: "Xác định tọa độ các giao điểm của đường thẳng $3x + 4y = 12$ với hai trục tọa độ $Ox, Oy$.",
          rubric: "Cho y=0 tính được x=4 => A(4;0) (0.5đ). Cho x=0 tính được y=3 => B(0;3) (0.5đ)."
        },
        {
          id: 2,
          level: "Vận dụng thấp",
          question: "Giải bài toán bằng cách lập hệ phương trình: Tìm hai số biết tổng của chúng bằng 19 và hiệu của chúng bằng 5.",
          rubric: "Gọi hai số là x, y (x>y). Lập hệ x+y=19 và x-y=5 (0.5đ). Giải ra x=12, y=7 và kết luận (0.5đ)."
        },
        {
          id: 3,
          level: "Vận dụng cao",
          question: "Cho hệ phương trình $\\begin{cases} x + 2y = m + 3 \\\\ 2x - 3y = m \\end{cases}$. Tìm $m$ để hệ có nghiệm duy nhất $(x; y)$ thỏa mãn $x^2 + y^2 = 5$.",
          rubric: "Giải nghiệm theo m: x = (5m+9)/7, y = (m+6)/7 (0.25đ). Thay vào x^2+y^2=5 (0.25đ). Giải tìm được m=1 hoặc m=-2 và kết luận (0.5đ)."
        }
      ]
    }
  },

  // -------------------------------------------------------------
  // TOÁN 8 - BÀI 1: Đơn thức
  // -------------------------------------------------------------
  // -------------------------------------------------------------
  // TOÁN 8 - CHƯƠNG I: ĐA THỨC (ĐẦY ĐỦ 6 BÀI HỌC X 3 CẤP ĐỘ ĐỀ PHÂN HÓA)
  // -------------------------------------------------------------
  "8_c1_8_Bài 1: Đơn thức": {
    "1": CHAPTER1_TOAN8_EXAMS["c1_8_bai1_test1"],
    "2": CHAPTER1_TOAN8_EXAMS["c1_8_bai1_test2"],
    "3": CHAPTER1_TOAN8_EXAMS["c1_8_bai1_test3"]
  },
  "8_c1_8_Bài 2: Đa thức": {
    "1": CHAPTER1_TOAN8_EXAMS["c1_8_bai2_test1"],
    "2": CHAPTER1_TOAN8_EXAMS["c1_8_bai2_test2"],
    "3": CHAPTER1_TOAN8_EXAMS["c1_8_bai2_test3"]
  },
  "8_c1_8_Bài 3: Phép cộng và phép trừ đa thức": {
    "1": CHAPTER1_TOAN8_EXAMS["c1_8_bai3_test1"],
    "2": CHAPTER1_TOAN8_EXAMS["c1_8_bai3_test2"],
    "3": CHAPTER1_TOAN8_EXAMS["c1_8_bai3_test3"]
  },
  "8_c1_8_Bài 4: Phép nhân đa thức": {
    "1": CHAPTER1_TOAN8_EXAMS["c1_8_bai4_test1"],
    "2": CHAPTER1_TOAN8_EXAMS["c1_8_bai4_test2"],
    "3": CHAPTER1_TOAN8_EXAMS["c1_8_bai4_test3"]
  },
  "8_c1_8_Bài 5: Phép chia đa thức cho đơn thức": {
    "1": CHAPTER1_TOAN8_EXAMS["c1_8_bai5_test1"],
    "2": CHAPTER1_TOAN8_EXAMS["c1_8_bai5_test2"],
    "3": CHAPTER1_TOAN8_EXAMS["c1_8_bai5_test3"]
  },
  "8_c1_8_Bài kiểm tra cuối Chương I: Đa thức": {
    "1": CHAPTER1_TOAN8_EXAMS["c1_8_bai6_test1"],
    "2": CHAPTER1_TOAN8_EXAMS["c1_8_bai6_test2"],
    "3": CHAPTER1_TOAN8_EXAMS["c1_8_bai6_test3"]
  },
};

/**
 * Hàm lấy đề thi từ ngân hàng hoặc tạo đề mặc định nếu chưa có
 */
export function getExamFromBank(grade, chapterId, lessonName, testNum) {
  const key = `${grade}_${chapterId}_${lessonName}`;
  const tests = EXAM_BANK[key];
  if (tests && tests[String(testNum)]) {
    return tests[String(testNum)];
  }

  // Nhận diện theo tên bài trong Chương 1 Toán 8
  if (grade === "8" && (chapterId === "c1_8" || (lessonName || "").includes("Đa thức") || (lessonName || "").includes("Đơn thức"))) {
    const les = (lessonName || "").toLowerCase();
    let c1Key = "";
    if (les.includes("cuối chương") || les.includes("ôn tập")) {
      c1Key = `c1_8_bai6_test${testNum}`;
    } else if (les.includes("bài 1") || les.includes("đơn thức")) {
      c1Key = `c1_8_bai1_test${testNum}`;
    } else if (les.includes("bài 2") || (les.includes("đa thức") && !les.includes("phép"))) {
      c1Key = `c1_8_bai2_test${testNum}`;
    } else if (les.includes("bài 3") || les.includes("cộng")) {
      c1Key = `c1_8_bai3_test${testNum}`;
    } else if (les.includes("bài 4") || les.includes("nhân")) {
      c1Key = `c1_8_bai4_test${testNum}`;
    } else if (les.includes("bài 5") || les.includes("chia")) {
      c1Key = `c1_8_bai5_test${testNum}`;
    }
    if (c1Key && CHAPTER1_TOAN8_EXAMS[c1Key]) {
      return CHAPTER1_TOAN8_EXAMS[c1Key];
    }
  }

  // Fallback khối 8
  if (grade === "8") {
    const base = CHAPTER1_TOAN8_EXAMS[`c1_8_bai1_test${testNum}`] || CHAPTER1_TOAN8_EXAMS["c1_8_bai1_test1"];
    return {
      ...base,
      title: `Toán 8 (KNTT) - ${lessonName} - Bài kiểm tra số ${testNum}`
    };
  }

  // Fallback khối khác
  const base9 = EXAM_BANK["9_c1_9_Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn"][String(testNum)] ||
                EXAM_BANK["9_c1_9_Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn"]["1"];
  return {
    ...base9,
    title: `Toán ${grade} (KNTT) - ${lessonName} - Bài kiểm tra số ${testNum}`
  };
}
