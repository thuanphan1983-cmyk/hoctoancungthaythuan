# HỆ THỐNG KIỂM TRA TOÁN THCS - KẾT NỐI TRI THỨC (LỚP 6, 7, 8, 9)

Hệ thống thi và kiểm tra trực tuyến môn Toán THCS bám sát cấu trúc ma trận mới nhất của Bộ Giáo dục & Đào tạo (chuẩn 2025) và toàn bộ phân phối chương trình bộ sách giáo khoa **Kết nối tri thức với cuộc sống** (Tập 1 & Tập 2).

---

## ✨ TÍNH NĂNG NỔI BẬT

### 1. Phân hóa 3 cấp độ đề kiểm tra rõ rệt (Đề 1 < Đề 2 < Đề 3)
Mỗi bài học và mỗi chương đều có 3 đề kiểm tra với độ khó tăng dần theo thang tư duy Bloom:
* **🌱 Bài kiểm tra số 1 (Mức độ Cơ bản - Mục tiêu 5.0 - 7.0 điểm)**:
  - Tập trung nhận biết và thông hiểu định nghĩa, công thức chuẩn SGK.
  - Tự luận gồm các bài tập mẫu điển hình trong sách giáo khoa, tính toán tường minh.
* **🚀 Bài kiểm tra số 2 (Mức độ Khá - Khó hơn Đề 1 - Mục tiêu 7.0 - 8.5 điểm)**:
  - Tăng cường câu hỏi thông hiểu sâu và vận dụng, biến đổi đại số nhiều bước.
  - Tự luận có bài toán thực tế (chuyển động, năng suất, tỉ số) và chứng minh hình học logic.
* **🔥 Bài kiểm tra số 3 (Mức độ Nâng cao - Khó nhất - Mục tiêu 8.5 - 10.0 điểm)**:
  - Đề phân hóa sâu dành cho học sinh giỏi và định hướng thi vào lớp 10.
  - Chứa câu hỏi tham số $m$, bẫy logic điều kiện xác định.
  - Câu cuối tự luận (1.0đ) là bài toán điểm 10 phân loại: Bất đẳng thức Cauchy/Schwarz, cực trị hình học/đại số, phương trình nghiệm nguyên.

### 2. Đầy đủ chương trình SGK & Đề tổng hợp cuối mỗi chương
* Đầy đủ toàn bộ các Chương và Bài học Toán 6, 7, 8, 9 (Cả 2 học kỳ).
* Cuối mỗi chương đều có mục **Đề kiểm tra cuối chương** (3 đề phân hóa) tổng hợp toàn diện kiến thức của toàn bộ chương.

### 3. Ma trận đề & Thang điểm chuẩn Bộ GD&ĐT (Tổng: 10.0 điểm)
* **Phần I (3.0 điểm):** 12 câu trắc nghiệm nhiều lựa chọn (0.25đ/câu), có **cơ chế khóa tuần tự** (làm xong câu trước mới mở câu kế tiếp).
* **Phần II (2.0 điểm):** 2 câu Đúng/Sai (1.0đ/câu, gồm 4 ý a-b-c-d), áp dụng thuật toán tính điểm lũy tiến chuẩn Bộ: đúng 1 ý = 0.1đ; 2 ý = 0.25đ; 3 ý = 0.5đ; cả 4 ý = 1.0đ.
* **Phần III (2.0 điểm):** 4 câu trả lời ngắn (0.5đ/câu), điền đáp số linh hoạt (chấp nhận cả dấu phẩy và dấu chấm thập phân).
* **Phần IV (3.0 điểm):** 3 câu tự luận (1.0đ/câu), tích hợp AI Vision nhận diện ảnh chụp bài làm viết tay/camera trực tiếp, chấm điểm theo barem từng bước và chỉ ra lỗi sai.

### 4. Phiếu nhận xét chi tiết 4 phần & Xuất PDF / Excel
* Tự động tổng hợp phiếu nhận xét toàn diện trên cả 4 phần: Trắc nghiệm 4 lựa chọn, Đúng/Sai, Trả lời ngắn, và Tự luận.
* Xuất phiếu kết quả kiểm tra cá nhân ra file PDF chuẩn A4.
* Xuất bảng điểm toàn lớp ra file Excel (.xlsx) chuẩn font tiếng Việt cho giáo viên.

---

## 🚀 HƯỚNG DẪN KHỞI CHẠY CỤC BỘ

### Cách 1: Chạy nhanh bằng file `run.bat` (Khuyên dùng trên Windows)
* Nháy đúp chuột vào file **`run.bat`**.
* Hệ thống sẽ tự động bật máy chủ và mở trình duyệt tại `http://localhost:8000`.

### Cách 2: Mở trực tiếp
* Nháy đúp chuột mở file **`index.html`** bằng trình duyệt bất kỳ (Google Chrome, Microsoft Edge, Opera, Cốc Cốc).

---

## 🤖 HỆ THỐNG AUTO EXAM GENERATOR (TỰ ĐỘNG SINH KHO ĐỀ OFFLINE)
* **Kịch bản:** [auto_exam_generator.py](file:///C:/Users/May%20Tinh%20Chau%20A/.gemini/antigravity/scratch/toan-thcs-kntt/auto_exam_generator.py)
* **Chạy nhanh bằng 1 click:** Nháy đúp chuột vào file **`run_auto_generator.bat`**.
* **Đặc điểm:**
  - Tự động duyệt qua toàn bộ khung chương trình Toán THCS (Lớp 6, 7, 8, 9).
  - Tự động gọi API Google Gemini (`gemini-3.8-flash` tốc độ cao và hạn mức lớn) để sinh 3 đề phân hóa cho từng bài học.
  - Tích hợp cơ chế tự phục hồi, chống lỗi (try-catch), tự động chờ (sleep/delay/backoff) khi gặp rate limit hoặc server bận, cho phép chạy miệt mài qua đêm.
  - Kết quả được xuất tự động vào thư mục `src/data/generated/`.

---

## 📄 HỆ THỐNG XUẤT ĐỀ THI SANG LATEX VÀ PDF (EXPORT TO PDF)
* **Kịch bản:** [export_to_pdf.py](file:///C:/Users/May%20Tinh%20Chau%20A/.gemini/antigravity/scratch/toan-thcs-kntt/export_to_pdf.py)
* **Chạy nhanh bằng 1 click:** Nháy đúp chuột vào file **`export_pdf.bat`**.
* **Tính năng chính:**
  - Quét thư mục `src/data/generated/`, tự động bóc tách tất cả các đề thi JSON.
  - Tự động lắp ráp vào template LaTeX chuẩn Bộ GD&ĐT 2025: tiêu đề hành chính, bảng điểm, Phần I (12 câu trắc nghiệm), Phần II (2 câu Đúng/Sai), Phần III (4 câu trả lời ngắn), Phần IV (3 câu tự luận).
  - Kèm theo trang **Hướng dẫn chấm và Đáp án chi tiết** (bảng đáp án Phần I, II, III và barem điểm từng bước cho Phần IV).
  - Hỗ trợ đa dạng trình biên dịch: **XeLaTeX** (Unicode tiếng Việt tối ưu) và **pdfLaTeX** (amsmath, amssymb, babel vietnamese).
  - Tự động dùng thư viện `subprocess` để biên dịch sang file `.pdf` lưu tại `src/data/pdf/` và file mã nguồn tại `src/data/pdf/tex/`.
  - Tích hợp cơ chế **try-except** vững chắc: nếu một đề bị lỗi cú pháp hoặc lỗi biên dịch, hệ thống sẽ ghi nhận và tự động bỏ qua để biên dịch tiếp các đề khác mà không dừng lại.
* **Các tùy chọn dòng lệnh:**
  ```bash
  # Xuất toàn bộ đề thi sang LaTeX và PDF
  python export_to_pdf.py

  # Chỉ xuất mã nguồn .tex (không cần cài MiKTeX / TeX Live)
  python export_to_pdf.py --tex-only

  # Chỉ xuất một mã đề cụ thể
  python export_to_pdf.py --exam-id c1_6_bai1_test1

  # Chỉ định trình biên dịch ưu tiên
  python export_to_pdf.py --engine xelatex
  ```

---

## 🌐 HƯỚNG DẪN ĐẨY LÊN GITHUB & DEPLOY VERCEL

1. **Khởi tạo và đẩy lên GitHub**:
   ```bash
   git init
   git add .
   git commit -m "feat: he thong kiem tra toan thcs kntt voi 3 muc do de phan hoa"
   git branch -M main
   git remote add origin <URL_REPO_GITHUB_CUA_BAN>
   git push -u origin main
   ```

2. **Deploy lên Vercel**:
   * Truy cập [Vercel](https://vercel.com/) và import repository GitHub vừa tạo.
   * Cấu hình Vercel đã được tối ưu sẵn qua file [vercel.json](file:///C:/Users/May%20Tinh%20Chau%20A/.gemini/antigravity/scratch/toan-thcs-kntt/vercel.json) và [build.js](file:///C:/Users/May%20Tinh%20Chau%20A/.gemini/antigravity/scratch/toan-thcs-kntt/build.js).
   * Nhấn **Deploy** và trang web sẽ hoạt động hoàn hảo 100% không lo lỗi 404 hay thiếu dữ liệu chương trình.
