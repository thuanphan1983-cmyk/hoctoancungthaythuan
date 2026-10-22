// ==============================================================================
// XUẤT BẢNG ĐIỂM THỐNG KÊ RA FILE EXCEL (.XLSX) VÀ CSV (.CSV)
// Sử dụng SheetJS (xlsx)
// Bao gồm nhận xét chi tiết CẢ 4 PHẦN (Trắc nghiệm, Đúng/Sai, Trả lời ngắn, Tự luận)
// ==============================================================================

export function exportSubmissionsToExcel(submissions, filterClass = "ALL") {
  if (!submissions || submissions.length === 0) {
    alert("Chưa có dữ liệu bài làm để xuất file Excel!");
    return;
  }

  const filtered = filterClass === "ALL" ? submissions : submissions.filter((s) => s.className === filterClass);

  const dataToExport = filtered.map((sub, idx) => ({
    "STT": idx + 1,
    "Lớp": sub.className,
    "Họ và tên học sinh": sub.studentName,
    "Khối lớp": `Toán ${sub.grade}`,
    "Bài học SGK": sub.lesson,
    "Đề số": `Bài KT số ${sub.testNum}`,
    "Phần I (3đ)": sub.scorePart1,
    "Phần II (2đ)": sub.scorePart2,
    "Phần III (2đ)": sub.scorePart3,
    "Phần IV (3đ)": sub.scorePart4,
    "Tổng điểm (10đ)": sub.totalScore,
    "Xếp loại": sub.totalScore >= 8 ? "Giỏi" : sub.totalScore >= 6.5 ? "Khá" : sub.totalScore >= 5 ? "Đạt" : "Chưa đạt",
    "Thời gian nộp": sub.timestamp,
    "Nhận xét P.I (Trắc nghiệm)": sub.feedbacks?.part1 || "",
    "Nhận xét P.II (Đúng/Sai)": sub.feedbacks?.part2 || "",
    "Nhận xét P.III (Trả lời ngắn)": sub.feedbacks?.part3 || "",
    "Nhận xét P.IV (Tự luận)": sub.feedbacks?.part4 || "",
    "Đánh giá & Định hướng chung": sub.feedbacks?.overall || sub.overallTeacherComment || ""
  }));

  if (window.XLSX) {
    const worksheet = window.XLSX.utils.json_to_sheet(dataToExport);
    worksheet["!cols"] = [
      { wch: 6 },  // STT
      { wch: 10 }, // Lớp
      { wch: 22 }, // Họ tên
      { wch: 10 }, // Khối
      { wch: 35 }, // Bài học
      { wch: 14 }, // Đề số
      { wch: 12 }, // P1
      { wch: 12 }, // P2
      { wch: 12 }, // P3
      { wch: 12 }, // P4
      { wch: 15 }, // Tổng
      { wch: 12 }, // Xếp loại
      { wch: 20 }, // Thời gian
      { wch: 38 }, // NX P1
      { wch: 38 }, // NX P2
      { wch: 38 }, // NX P3
      { wch: 38 }, // NX P4
      { wch: 45 }  // Đánh giá chung
    ];

    const workbook = window.XLSX.utils.book_new();
    window.XLSX.utils.book_append_sheet(workbook, worksheet, "BangDiemToan");
    const fileName = `Bang_Diem_KNTT_${filterClass === "ALL" ? "TatCaLop" : filterClass}_${new Date().toISOString().slice(0, 10)}.xlsx`;
    window.XLSX.writeFile(workbook, fileName);
  } else {
    exportSubmissionsToCSV(submissions, filterClass);
  }
}

export function exportSubmissionsToCSV(submissions, filterClass = "ALL") {
  if (!submissions || submissions.length === 0) {
    alert("Chưa có dữ liệu bài làm để xuất file CSV!");
    return;
  }

  const filtered = filterClass === "ALL" ? submissions : submissions.filter((s) => s.className === filterClass);
  const headers = [
    "STT",
    "Lop",
    "Ho_va_ten",
    "Khoi",
    "Bai_hoc",
    "De_so",
    "Diem_P1",
    "Diem_P2",
    "Diem_P3",
    "Diem_P4",
    "Tong_diem",
    "Xep_loai",
    "Thoi_gian",
    "Nhan_xet_P1",
    "Nhan_xet_P2",
    "Nhan_xet_P3",
    "Nhan_xet_P4",
    "Danh_gia_chung"
  ];

  const rows = filtered.map((sub, idx) => [
    idx + 1,
    `"${sub.className}"`,
    `"${sub.studentName}"`,
    `"Toan ${sub.grade}"`,
    `"${sub.lesson.replace(/"/g, '""')}"`,
    `"Bai KT ${sub.testNum}"`,
    sub.scorePart1,
    sub.scorePart2,
    sub.scorePart3,
    sub.scorePart4,
    sub.totalScore,
    sub.totalScore >= 8 ? "Gioi" : sub.totalScore >= 6.5 ? "Kha" : sub.totalScore >= 5 ? "Dat" : "Chua dat",
    `"${sub.timestamp}"`,
    `"${(sub.feedbacks?.part1 || "").replace(/"/g, '""')}"`,
    `"${(sub.feedbacks?.part2 || "").replace(/"/g, '""')}"`,
    `"${(sub.feedbacks?.part3 || "").replace(/"/g, '""')}"`,
    `"${(sub.feedbacks?.part4 || "").replace(/"/g, '""')}"`,
    `"${(sub.feedbacks?.overall || sub.overallTeacherComment || "").replace(/"/g, '""')}"`
  ]);

  const csvContent = "\uFEFF" + [headers.join(","), ...rows.map((r) => r.join(","))].join("\n");
  const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.setAttribute("download", `Bang_Diem_${filterClass}_${new Date().toISOString().slice(0, 10)}.csv`);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
