@echo off
chcp 65001 >nul
title AUTO EXAM GENERATOR - TỰ ĐỘNG SINH KHO ĐỀ KIỂM TRA TOÁN THCS
color 0B

echo ===============================================================================
echo        HỆ THỐNG TỰ ĐỘNG SINH KHO ĐỀ DỰ PHÒNG TOÁN THCS (KẾT NỐI TRI THỨC)
echo        Chuẩn Ma trận 2025 Bộ GD^&ĐT - 3 Mức độ phân hóa (Cơ bản - Khá - Nâng cao)
echo        Tự động chờ khi nghẽn mạng / Rate limit - Chạy miệt mài qua đêm
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
        if "%%A"=="GEMINI_API_KEY" set "USER_KEY=%%B"
    )
)

if "%USER_KEY%"=="" (
    echo [THIẾT LẬP KEY] Chưa cấu hình Google Gemini API Key.
    set /p "USER_KEY=>> Vui lòng dán mã Gemini API Key của bạn vào đây: "
    if not "%USER_KEY%"=="" (
        echo GEMINI_API_KEY=%USER_KEY% > .env
        echo [OK] Đã lưu mã Key vào file .env để dùng tự động cho các lần sau.
    )
) else (
    echo [OK] Đã nạp Gemini API Key từ cấu hình file .env.
)

echo [OK] Mô hình AI: gemini-3.1-pro-preview (Thế hệ mới hỗ trợ logic Toán học tốt nhất)
echo.
echo ===============================================================================
echo CHỌN CHẾ ĐỘ SINH ĐỀ:
echo [1] Sinh TOÀN BỘ kho đề THCS (Toán 6, 7, 8, 9 - 190 bài x 3 = 570 đề)
echo [2] Ưu tiên sinh TOÁN 8 (Đầy đủ 10 chương - 49 bài x 3 = 147 đề)
echo [3] Ưu tiên sinh TOÁN 9 (Đầy đủ 10 chương - 42 bài x 3 = 126 đề)
echo [4] Tùy chọn khối lớp khác (Nhập số 6, 7, 8, 9)
echo ===============================================================================
set /p "MODE=Nhập lựa chọn của bạn (1, 2, 3 hoặc 4) [Mặc định: 2]: "

if "%MODE%"=="1" (
    echo.
    echo Bắt đầu sinh toàn bộ đề THCS bằng mô hình gemini-3.1-pro-preview...
    "%PYTHON_CMD%" auto_exam_generator.py --api-key "%USER_KEY%" --grade all
) else if "%MODE%"=="3" (
    echo.
    echo Bắt đầu sinh kho đề Toán 9 bằng mô hình gemini-3.1-pro-preview...
    "%PYTHON_CMD%" auto_exam_generator.py --api-key "%USER_KEY%" --grade 9
) else if "%MODE%"=="4" (
    set /p "CUSTOM_GRADE=Nhập khối lớp muốn sinh (6, 7, 8 hoặc 9): "
    echo.
    echo Bắt đầu sinh kho đề Toán %CUSTOM_GRADE% bằng mô hình gemini-3.1-pro-preview...
    "%PYTHON_CMD%" auto_exam_generator.py --api-key "%USER_KEY%" --grade %CUSTOM_GRADE%
) else (
    echo.
    echo Bắt đầu sinh kho đề Toán 8 bằng mô hình gemini-3.1-pro-preview...
    "%PYTHON_CMD%" auto_exam_generator.py --api-key "%USER_KEY%" --grade 8
)

echo.
echo ===============================================================================
echo Quá trình thực thi đã hoàn tất hoặc tạm dừng.
echo Dữ liệu đề thi đã được lưu an toàn tại thư mục src\data\generated\
echo ===============================================================================
pause
