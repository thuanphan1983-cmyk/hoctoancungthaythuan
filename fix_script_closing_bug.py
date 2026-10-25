# -*- coding: utf-8 -*-
"""
Sửa triệt để lỗi thẻ </script> bị đóng sớm trong index.html
Nguyên nhân: Trong hàm handlePrintMockExam có chuỗi literal chứa </script> làm trình duyệt
đóng thẻ <script> sớm, dẫn đến mã JavaScript bị tràn ra giao diện như văn bản thô
và trình duyệt tự động gọi window.print() ngay khi vừa mở trang.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Tìm vị trí bắt đầu của hàm handlePrintMockExam
start_marker = "      // HÀM MỞ HỘP THOẠI IN CHUYÊN NGHIỆP HOẶC LƯU DƯỚI DẠNG PDF CỦA TRÌNH DUYỆT (VECTOR NÉT 100%)"
end_marker = "      const [loadingAI, setLoadingAI] = useState(false);"

pos_start = content.find(start_marker)
pos_end = content.find(end_marker)

if pos_start == -1 or pos_end == -1:
    print(f"Lỗi: Không tìm thấy vị trí đánh dấu (pos_start={pos_start}, pos_end={pos_end})")
    sys.exit(1)

print(f"Đã tìm thấy đoạn mã lỗi từ vị trí {pos_start} đến {pos_end}.")

# Hàm handlePrintMockExam mới hoàn toàn không chứa bất kỳ thẻ <script> hay </script> nào!
new_print_function = """      // HÀM MỞ HỘP THOẠI IN CHUYÊN NGHIỆP HOẶC LƯU DƯỚI DẠNG PDF CỦA TRÌNH DUYỆT (VECTOR NÉT 100%)
      const handlePrintMockExam = async (includeSolution = false) => {
        const curExam = mockExamsData?.exams?.[selectedMockExamKey];
        if (!curExam) return;

        setMockViewTab(includeSolution ? "full" : "paper");
        await new Promise(r => setTimeout(r, 350));

        const targetId = includeSolution ? "mock-exam-printable-full" : "mock-exam-printable-paper";
        const element = document.getElementById(targetId);
        if (!element) {
          window.print();
          return;
        }

        const printWindow = window.open('', '_blank', 'width=920,height=1150');
        if (printWindow) {
          const docTitle = curExam.title || 'De_Thi_Vao_10';
          const innerHtmlContent = element.innerHTML;
          printWindow.document.open();
          printWindow.document.write(
            '<!DOCTYPE html>' +
            '<html lang="vi">' +
            '<head>' +
            '<meta charset="utf-8">' +
            '<title>' + docTitle + '</title>' +
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">' +
            '<style>' +
            '@page { size: A4; margin: 15mm 20mm 15mm 20mm; }' +
            'body { font-family: "Times New Roman", Times, serif; font-size: 12pt; line-height: 1.45; color: #000; background: #fff; margin: 0; padding: 8mm; }' +
            '.katex { font-size: 1.05em; }' +
            'table { border-collapse: collapse; width: 100%; margin: 8px 0; }' +
            'th, td { border: 1px solid #000; padding: 6px; text-align: center; }' +
            '.grid-cols-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-top: 4px; }' +
            '.grid-cols-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin-top: 4px; }' +
            '@media print { body { padding: 0; } .no-print { display: none !important; } }' +
            '</style>' +
            '</head>' +
            '<body>' +
            innerHtmlContent +
            '</body>' +
            '</html>'
          );
          printWindow.document.close();
          printWindow.focus();
          setTimeout(() => {
            try {
              printWindow.print();
            } catch (e) {
              console.warn(e);
            }
          }, 500);
        } else {
          window.print();
        }
      };

"""

content = content[:pos_start] + new_print_function + content[pos_end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

# Sao chép sang dist/index.html
if os.path.exists("dist"):
    with open("dist/index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Đã đồng bộ sang dist/index.html")

print("🎉 Hoàn tất sửa lỗi thẻ đóng script! Ứng dụng sẽ tải mượt mà không còn bị mở hộp thoại in và không còn hiện mã nguồn rác.")
