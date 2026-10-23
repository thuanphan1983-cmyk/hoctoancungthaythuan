@echo off
chcp 65001 >nul
title EXPORT TO PDF & LATEX - XUẤT NGÂN HÀNG ĐỀ THI TOÁN THCS
color 0A

echo ===============================================================================
echo       HỆ THỐNG XUẤT ĐỀ THI TOÁN THCS SANG TEMPLATE LATEX VÀ PDF CHUẨN
echo       Hỗ trợ cả XeLaTeX và pdfLaTeX, chuẩn bảng điểm ma trận Bộ GD^&ĐT
echo       Tự động bắt lỗi (Try-Except), không ngắt ngang khi gặp đề lỗi
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
    echo Vui lòng cài đặt Python từ python.org để tiếp tục.
    echo.
    pause
    exit /b 1
)

echo [OK] Đã tìm thấy Python: "%PYTHON_CMD%"
echo.

:: 2. Thực thi kịch bản export_to_pdf.py
"%PYTHON_CMD%" export_to_pdf.py %*

echo.
echo ===============================================================================
echo Quá trình xuất hoàn tất!
echo Các file mã nguồn .tex và .pdf được lưu tại thư mục: src\data\pdf\
echo ===============================================================================
echo.
pause
