# HỆ THỐNG PIPELINE TỰ ĐỘNG HÓA TẠO VIDEO TOÁN HỌC TRỰC QUAN BẰNG AI
> **Dự án:** Học toán cùng thầy Thuấn Phan • Chuẩn SGK Kết nối tri thức với cuộc sống (Toán 6, 7, 8, 9)

Hệ thống cho phép tự động sinh toàn bộ video bài giảng toán học độ phân giải cao (1080p Full HD) hoàn toàn bằng mã nguồn Python, kết hợp giữa đồ họa hoạt cảnh toán học **Manim Community** và giọng thuyết minh trí tuệ nhân tạo **Edge-TTS Neural Voice**.

---

## 1. CÁC TÍNH NĂNG CHÍNH
- **Đồ họa toán học trực quan (Animation Engine):** Vẽ sơ đồ Ven, di chuyển phần tử, tô màu phân biệt thuộc ($\in$) và không thuộc ($\notin$), minh họa hình tam giác đều, hình vuông, lục giác đều, xoay hình và biến đổi công thức.
- **Giọng đọc AI chuẩn tiếng Việt (Voiceover Engine):** Giọng nam truyền cảm `vi-VN-NamMinhNeural` hoặc giọng nữ trong trẻo `vi-VN-HoaiMyNeural` chuẩn phát âm sư phạm.
- **Tự động đồng bộ âm thanh & hình ảnh (Sync Engine):** Đo thời lượng chính xác của từng câu nói AI và điều chỉnh tốc độ hoạt cảnh đồ họa khớp 100% với lời thuyết minh.
- **Kiến trúc mở rộng không giới hạn (Scalable Config):** Quản lý toàn bộ bài học qua file `config/lessons_config.json`. Thêm bài học mới chỉ cần khai báo kịch bản và văn bản thuyết minh.

---

## 2. CẤU TRÚC DỰ ÁN
```
math_video_pipeline/
│
├── config/
│   └── lessons_config.json      # File kịch bản khai báo toàn bộ các bài học
│
├── animation_engine.py          # Đồ họa Manim (Sơ đồ Ven, hình học, tổng kết kiến thức)
├── voiceover_engine.py          # Bộ sinh giọng nói thuyết minh AI (Edge-TTS)
├── sync_engine.py               # Bộ ghép nối video & audio bằng FFmpeg
├── generate_all_videos.py       # Script thực thi chính điều khiển toàn bộ pipeline
│
├── requirements.txt             # Danh sách thư viện Python cần thiết
├── README.md                    # Hướng dẫn chi tiết
│
├── generated_videos/            # Thư mục lưu các video bài học hoàn chỉnh (.mp4)
└── temp/                        # Thư mục chứa audio/video tạm thời (tự động dọn dẹp)
```

---

## 3. CÀI ĐẶT MÔI TRƯỜNG

### Bước 1: Cài đặt các thư viện Python
Trong terminal, chạy lệnh:
```bash
pip install -r requirements.txt
```

### Bước 2: Cài đặt FFmpeg
Hệ thống đã tích hợp sẵn công cụ lấy binary `ffmpeg` qua thư viện `imageio-ffmpeg` tự động. Bạn cũng có thể cài đặt hệ thống nếu muốn:
```powershell
winget install Gyan.FFmpeg
```

---

## 4. HƯỚNG DẪN CHẠY THỬ NGHIỆM

### 1. Xem danh sách các bài học có trong hệ thống:
```bash
python generate_all_videos.py --list
```

### 2. Chạy thử nghiệm bài học đầu tiên (Toán 6 - Bài 1: Tập hợp):
* **Chế độ kiểm thử siêu nhanh (480p preview):**
```bash
python generate_all_videos.py --lesson toan6_bai1 --quality l
```

* **Chế độ kết xuất chất lượng cao (720p HD):**
```bash
python generate_all_videos.py --lesson toan6_bai1 --quality m
```

* **Chế độ xuất bản YouTube / Studio (1080p Full HD 60fps):**
```bash
python generate_all_videos.py --lesson toan6_bai1 --quality h
```

### 3. Đổi sang giọng đọc nữ (Cô giáo AI):
```bash
python generate_all_videos.py --lesson toan6_bai1 --voice vi-VN-HoaiMyNeural
```

### 4. Tự động sinh video cho toàn bộ bài học:
```bash
python generate_all_videos.py --lesson all --quality m
```

Video thành phẩm sẽ được lưu tại: `math_video_pipeline/generated_videos/Toan6_Bai1_TapHop_PhanTu.mp4`.
