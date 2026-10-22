// ==============================================================================
// HỆ THỐNG TÍNH ĐIỂM CHUẨN MA TRẬN BỘ GIÁO DỤC & ĐÀO TẠO 2025
// ==============================================================================

/**
 * Quy tắc tính điểm cho câu trắc nghiệm Đúng/Sai (Phần II)
 * - Đúng 1 ý: 0.1 điểm
 * - Đúng 2 ý: 0.25 điểm
 * - Đúng 3 ý: 0.5 điểm
 * - Đúng 4 ý: 1.0 điểm
 */
export function calculateTrueFalseScore(userAnswers, statements) {
  let correctCount = 0;
  statements.forEach((stmt) => {
    if (userAnswers && userAnswers[stmt.key] === stmt.correct) {
      correctCount++;
    }
  });

  if (correctCount === 1) return 0.1;
  if (correctCount === 2) return 0.25;
  if (correctCount === 3) return 0.5;
  if (correctCount === 4) return 1.0;
  return 0.0;
}

/**
 * Chuẩn hóa đáp án trả lời ngắn (chấp nhận cả dấu phẩy và dấu chấm thập phân)
 */
export function normalizeShortAnswer(val) {
  if (val === undefined || val === null) return "";
  return String(val)
    .trim()
    .replace(",", ".")
    .replace(/\s+/g, "");
}
