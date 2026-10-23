@echo off
chcp 65001 >nul
title AUTO EXAM GENERATOR - TỰ ĐỘNG SINH KHO ĐỀ KIỂM TRA TOÁN THCS
color 0B

echo ===============================================================================
echo        HỆ THỐNG TỰ ĐỘNG SINH KHO ĐỀ DỰ PHÒNG TOÁN THCS (KẾT NỐI TRI THỨC)
echo        Chuẩn Ma trận 2025 Bộ GD^&ĐT - 3 Mức độ phân hóa (Cơ bản - Khá - Nâng cao)
echo        ✨ TÍNH NĂNG MỚI: Luân phiên API Key (Key Rotation) khi gặp lỗi 429
echo        ⏳ KIỂM SOÁT NHỊP ĐỘ: Tự động nghỉ 75s sau mỗi đề (Rate Limiter Free Tier)
echo ===============================================================================
echo.

cd /d "%~dp0"

:: 1. Tìm kiếm Python trên máy
set PYTHON_CMD=
where python >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set PYTHON_CMD=python
) else (
    if exist "%LOCALAPPDATA%\Programs\Python311\tools\python.exe" (
        set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python311\tools\python.exe"
    ) else if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
        set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python311\python.exe"
    ) else if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
        set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    )
)

if "%PYTHON_CMD%"=="" (
    echo [LỖI] Không tìm thấy Python 3 trên máy tính của bạn.
    echo Vui lòng cài đặt Python từ python.org hoặc Microsoft Store để tiếp tục.
    echo.
    pause
    exit /b 1
)

echo [OK] Đã tìm thấy Python: "%PYTHON_CMD%"
echo.

:: 2. Kiểm tra API Key trong file .env
set USER_KEY=
if exist ".env" (
    for /f "tokens=1,2 delims==" %%A in (.env) do (
        if "%%A"=="GEMINI_API_KEYS" set "USER_KEY=%%B"
        if "%%A"=="GEMINI_API_KEY" (
            if "%USER_KEY%"=="" set "USER_KEY=%%B"
        )
    )
)

if "%USER_KEY%"=="" (
    echo [THIẾT LẬP KEY] Chưa cấu hình Google Gemini API Key.
    echo Mẹo: Bạn có thể dán nhiều key cách nhau bằng dấu phẩy để hệ thống tự luân phiên!
    set /p "USER_KEY=>> Vui lòng dán mã Gemini API Key của bạn vào đây: "
    if not "%USER_KEY%"=="" (
        echo GEMINI_API_KEYS=%USER_KEY% > .env
        echo [OK] Đã lưu mã Key vào file .env để dùng tự động cho các lần sau.
    )
) else (
    echo [OK] Đã nạp Gemini API Key từ cấu hình file .env.
)

echo [OK] Mô hình AI: gemini-3.8-flash (Tốc độ cao, hạn mức API lớn, phù hợp sinh số lượng lớn)
echo.
echo ===============================================================================
echo CHỌN CHẾ ĐỘ SINH ĐỀ (CÓ HỖ TRỢ CHỌN TỪNG CHƯƠNG ĐỂ GIẢM TẢI):
echo [1] Sinh TOÀN BỘ kho đề THCS (Toán 6, 7, 8, 9 - 190 bài x 3 = 570 đề)
echo [2] Toán 8 - Chương 2: Hằng đẳng thức đáng nhớ (5 bài x 3 = 15 đề - Giảm tải)
echo [3] Toán 8 - Toàn bộ 10 chương (49 bài x 3 = 147 đề)
echo [4] Toán 9 - Toàn bộ 10 chương (42 bài x 3 = 126 đề)
echo [5] Tự chọn Khối lớp và Số chương bất kỳ (--grade và --chuong)
echo ===============================================================================
set /p "MODE=Nhập lựa chọn của bạn (1, 2, 3, 4 hoặc 5) [Mặc định: 2]: "

if "%MODE%"=="1" (
    echo.
    echo Bắt đầu sinh toàn bộ đề THCS bằng mô hình gemini-3.8-flash...
    "%PYTHON_CMD%" auto_exam_generator.py --api-key "%USER_KEY%" --grade all --delay 75 --timeout 150
) else if "%MODE%"=="3" (
    echo.
    echo Bắt đầu sinh toàn bộ 10 chương Toán 8...
    "%PYTHON_CMD%" auto_exam_generator.py --api-key "%USER_KEY%" --grade 8 --delay 75 --timeout 150
) else if "%MODE%"=="4" (
    echo.
    echo Bắt đầu sinh kho đề Toán 9...
    "%PYTHON_CMD%" auto_exam_generator.py --api-key "%USER_KEY%" --grade 9 --delay 75 --timeout 150
) else if "%MODE%"=="5" (
    set /p "CUSTOM_GRADE=Nhập khối lớp muốn sinh (6, 7, 8 hoặc 9): "
    set /p "CUSTOM_CHUONG=Nhập số chương cụ thể (1, 2, 3... hoặc ấn Enter để chạy hết): "
    if "%CUSTOM_CHUONG%"=="" set "CUSTOM_CHUONG=all"
    echo.
    echo Bắt đầu sinh kho đề Toán %CUSTOM_GRADE% - Chương %CUSTOM_CHUONG%...
    "%PYTHON_CMD%" auto_exam_generator.py --api-key "%USER_KEY%" --grade %CUSTOM_GRADE% --chuong %CUSTOM_CHUONG% --delay 75 --timeout 150
) else (
    echo.
    echo Bắt đầu sinh kho đề Toán 8 - Chương 2: Hằng đẳng thức đáng nhớ và ứng dụng...
    "%PYTHON_CMD%" auto_exam_generator.py --api-key "%USER_KEY%" --grade 8 --chuong 2 --delay 75 --timeout 150
)

echo.
echo ===============================================================================
echo Quá trình thực thi đã hoàn tất hoặc tạm dừng.
echo Dữ liệu đề thi đã được lưu an toàn tại thư mục src\data\generated\
echo ===============================================================================
pause
