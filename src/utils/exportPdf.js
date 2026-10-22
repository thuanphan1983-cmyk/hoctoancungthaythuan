// ==============================================================================
// XUẤT PHIẾU KẾT QUẢ ĐỊNH DẠNG CHUẨN A4 BẰNG HTML2PDF.JS
// ==============================================================================

export function exportResultToPDF(elementId, studentName = "Hoc_Sinh", lesson = "Bai_Kiem_Tra") {
  const element = document.getElementById(elementId);
  if (!element) {
    window.print();
    return;
  }

  // Làm sạch tên file
  const cleanName = studentName.replace(/[^a-zA-Z0-9à-ỹÀ-Ỹ]/g, "_");
  const fileName = `Phieu_Ket_Qua_${cleanName}_${Date.now()}.pdf`;

  if (window.html2pdf) {
    const opt = {
      margin: [10, 10, 10, 10], // mm
      filename: fileName,
      image: { type: "jpeg", quality: 0.98 },
      html2canvas: { scale: 2, useCORS: true, logging: false },
      jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
      pagebreak: { mode: ["avoid-all", "css", "legacy"] }
    };

    window.html2pdf().from(element).set(opt).save();
  } else {
    // Dự phòng khi chưa tải được thư viện CDN
    window.print();
  }
}
