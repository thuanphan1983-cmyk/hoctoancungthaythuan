# -*- coding: utf-8 -*-
"""
Script cập nhật index.html với tính năng "THI THỬ VÀO LỚP 10" và "XUẤT PDF TIMES NEW ROMAN 12PT"
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Thêm thẻ script grade10EntranceExams.js
if "grade10EntranceExams.js" not in content:
    target_head = "  <!-- Curriculum Database -->"
    replacement_head = '  <!-- Grade 10 Entrance Exam Database (GV Phan Đình Thuấn) -->\n  <script src="grade10EntranceExams.js"></script>\n\n  <!-- Curriculum Database -->'
    content = content.replace(target_head, replacement_head, 1)
    print("✅ Đã chèn script grade10EntranceExams.js")

# 2. Thêm style Times New Roman 12pt và định dạng PDF
if ".pdf-exam-container" not in content:
    target_style = "@media print {"
    replacement_style = """/* Định dạng phông chữ Times New Roman 12pt cho Đề thi thử vào 10 & Xuất PDF */
    .font-times {
      font-family: 'Times New Roman', Times, 'Liberation Serif', serif !important;
    }
    .pdf-exam-container {
      font-family: 'Times New Roman', Times, 'Liberation Serif', serif !important;
      font-size: 12pt !important;
      line-height: 1.45 !important;
      color: #000000 !important;
    }
    .pdf-exam-container .katex {
      font-size: 1.05em !important;
    }
    @media print {
      @page {
        size: A4;
        margin: 15mm 20mm 15mm 20mm;
      }
      .mock-exam-print-target {
        display: block !important;
        width: 100% !important;
      }
      body {
        font-family: 'Times New Roman', Times, serif !important;
      }"""
    content = content.replace(target_style, replacement_style, 1)
    print("✅ Đã cập nhật CSS font Times New Roman 12pt")

# 3. Thêm state và handlers trong App()
state_code_marker = '      const [view, setView] = useState("setup");'
mock_state_code = """      const [view, setView] = useState("setup");

      // State chuyên dụng cho THI THỬ VÀO LỚP 10 - GV PHAN ĐÌNH THUẤN
      const [selectedMockExamKey, setSelectedMockExamKey] = useState("de_01");
      const [mockExamsData, setMockExamsData] = useState(() => {
        if (typeof window !== "undefined" && window.GRADE10_MOCK_EXAMS) {
          return window.GRADE10_MOCK_EXAMS;
        }
        return null;
      });
      const [showMockSolution, setShowMockSolution] = useState(false);
      const [mockMcUserAnswers, setMockMcUserAnswers] = useState({});
      const [mockMcSubmitted, setMockMcSubmitted] = useState(false);
      const [isExportingMockPdf, setIsExportingMockPdf] = useState(false);

      useEffect(() => {
        if (!mockExamsData) {
          const loadMock = async () => {
            try {
              const res = await fetch("src/data/generated/grade10_mock_exams.json");
              if (res.ok) {
                const d = await res.json();
                setMockExamsData(d);
                window.GRADE10_MOCK_EXAMS = d;
                return;
              }
            } catch (e) {}
            try {
              const res2 = await fetch("generated/grade10_mock_exams.json");
              if (res2.ok) {
                const d2 = await res2.json();
                setMockExamsData(d2);
                window.GRADE10_MOCK_EXAMS = d2;
              }
            } catch (e) {}
          };
          loadMock();
        }
      }, [mockExamsData]);

      const handleExportMockExamPDF = (includeSolution = false) => {
        const curExam = mockExamsData?.exams?.[selectedMockExamKey];
        if (!curExam) return;
        const targetId = includeSolution ? "mock-exam-printable-full" : "mock-exam-printable-paper";
        const element = document.getElementById(targetId);
        if (!element) {
          window.print();
          return;
        }
        const cleanCode = (curExam.code || "DE_01").replace(/[^a-zA-Z0-9]/g, "_");
        const suffix = includeSolution ? "De_Va_Loi_Giai" : "De_Thi";
        const fileName = `De_Thi_Thu_Vao_10_GV_Phan_Dinh_Thuan_${cleanCode}_${suffix}.pdf`;

        if (window.html2pdf) {
          setIsExportingMockPdf(true);
          const opt = {
            margin: [12, 15, 12, 15],
            filename: fileName,
            image: { type: "jpeg", quality: 0.98 },
            html2canvas: { scale: 2, useCORS: true, logging: false },
            jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
            pagebreak: { mode: ["avoid-all", "css", "legacy"] }
          };
          window.html2pdf().from(element).set(opt).save().then(() => {
            setIsExportingMockPdf(false);
            showToast("success", "Đã xuất file PDF thành công chuẩn phông Times New Roman 12pt!");
          }).catch(err => {
            console.error(err);
            setIsExportingMockPdf(false);
            window.print();
          });
        } else {
          window.print();
        }
      };"""

if "selectedMockExamKey" not in content:
    content = content.replace(state_code_marker, mock_state_code, 1)
    print("✅ Đã chèn state và handlers cho Thi Thử Vào Lớp 10")

# 4. Thêm nút vào Top Header Navigation
nav_marker = '<button\n\n                  onClick={() => setView("setup")}'
nav_replacement = """<button
                  onClick={() => setView("grade10_mock")}
                  className={`px-3.5 py-2 rounded-xl text-xs md:text-sm font-bold flex items-center gap-1.5 transition ${
                    view === "grade10_mock"
                      ? "bg-amber-400 text-slate-950 shadow-md ring-2 ring-amber-300"
                      : "bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white shadow"
                  }`}
                >
                  <span>🎯</span> THI THỬ VÀO LỚP 10
                  <span className="text-[10px] bg-white/20 text-white px-1.5 py-0.5 rounded-full font-black uppercase tracking-wider">Mới</span>
                </button>

                <button

                  onClick={() => setView("setup")}"""

if 'view === "grade10_mock"' not in content:
    content = content.replace(nav_marker, nav_replacement, 1)
    print("✅ Đã chèn nút THI THỬ VÀO LỚP 10 vào Header")

# 5. Thêm Banner vào view === "setup"
setup_banner_marker = '{/* Lựa chọn khối, chương, bài */}'
setup_banner_code = """{/* BANNER THI THỬ VÀO LỚP 10 - GV PHAN ĐÌNH THUẤN */}
                <div className="bg-gradient-to-r from-amber-500 via-orange-500 to-rose-500 text-white p-5 rounded-2xl shadow-sm flex flex-wrap items-center justify-between gap-4">
                  <div className="flex items-center gap-3.5">
                    <div className="w-12 h-12 bg-white/20 backdrop-blur rounded-2xl flex items-center justify-center text-2xl shrink-0">
                      🎯
                    </div>
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="font-black text-[11px] uppercase tracking-wider bg-white/20 px-2 py-0.5 rounded text-white">Chuyên mục đặc biệt</span>
                        <span className="text-xs text-amber-100 font-semibold">GV PHAN ĐÌNH THUẤN</span>
                      </div>
                      <h3 className="text-base md:text-lg font-black mt-0.5">ĐỀ THI THỬ VÀO LỚP 10 MÔN TOÁN (6 BỘ ĐỀ MINH HỌA)</h3>
                      <p className="text-xs text-white/90">
                        Cấu trúc chuẩn 14 câu (8 trắc nghiệm + 6 tự luận) • Đánh chuẩn LaTeX • Xuất file PDF Times New Roman cỡ chữ 12
                      </p>
                    </div>
                  </div>
                  <button
                    onClick={() => setView("grade10_mock")}
                    className="bg-white hover:bg-amber-50 text-slate-950 font-black text-xs md:text-sm px-5 py-2.5 rounded-xl shadow-md transition flex items-center gap-2 shrink-0"
                  >
                    Vào phòng thi thử ngay →
                  </button>
                </div>

                {/* Lựa chọn khối, chương, bài */}"""

if "BANNER THI THỬ VÀO LỚP 10" not in content:
    content = content.replace(setup_banner_marker, setup_banner_code, 1)
    print("✅ Đã chèn Banner vào Màn hình Setup")

# 6. Thêm View chính: view === "grade10_mock"
view_mock_code = """
            {/* ============================================================== */}
            {/* MÀN HÌNH CHUYÊN BIỆT: THI THỬ VÀO LỚP 10 - GV PHAN ĐÌNH THUẤN    */}
            {/* ============================================================== */}
            {view === "grade10_mock" && (() => {
              const examsObj = mockExamsData?.exams || {};
              const examKeys = ["de_01", "de_02", "de_03", "de_04", "de_05", "de_06"];
              const currentExam = examsObj[selectedMockExamKey] || examsObj["de_01"] || null;

              if (!currentExam) {
                return (
                  <div className="bg-white p-8 rounded-2xl shadow border text-center space-y-4">
                    <div className="w-12 h-12 bg-amber-100 text-amber-600 rounded-full flex items-center justify-center mx-auto text-2xl animate-spin">
                      ⏳
                    </div>
                    <h3 className="text-lg font-bold text-slate-800">Đang tải kho Đề thi thử vào Lớp 10...</h3>
                    <p className="text-xs text-slate-500">GV Phan Đình Thuấn • 6 Đề Minh Họa chuẩn Ma trận</p>
                  </div>
                );
              }

              // Tính điểm trắc nghiệm nhanh nếu học sinh đã làm
              const correctMcCount = currentExam.part1.filter(q => mockMcUserAnswers[q.id] === q.answer).length;
              const mcScore = (correctMcCount * 0.25).toFixed(2);

              return (
                <div className="space-y-6">
                  {/* THANH ĐIỀU HƯỚNG TRÊN CÙNG */}
                  <div className="bg-white p-4 rounded-2xl shadow-sm border border-slate-200 flex flex-wrap justify-between items-center gap-3">
                    <button
                      onClick={() => setView("setup")}
                      className="text-xs md:text-sm font-semibold text-slate-600 hover:text-indigo-600 flex items-center gap-1.5 transition"
                    >
                      ← Quay lại Thiết lập SGK (Toán 6, 7, 8, 9)
                    </button>
                    <div className="flex items-center gap-2">
                      <span className="text-xs bg-amber-100 text-amber-900 font-bold px-3 py-1 rounded-full border border-amber-300">
                        ⭐ 6 Đề Minh Họa Chuẩn Ma Trận 2025 - 2026
                      </span>
                      <span className="text-xs bg-indigo-100 text-indigo-900 font-bold px-3 py-1 rounded-full">
                        GV Phan Đình Thuấn
                      </span>
                    </div>
                  </div>

                  {/* BANNER TIÊU ĐỀ & CHỌN MÃ ĐỀ */}
                  <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white p-6 md:p-8 rounded-2xl shadow-md space-y-4">
                    <div className="flex flex-wrap justify-between items-start gap-4 border-b border-indigo-800/60 pb-5">
                      <div>
                        <div className="flex items-center gap-2">
                          <span className="bg-amber-400 text-slate-950 text-[10px] font-black px-2 py-0.5 rounded tracking-wider uppercase">
                            KỲ THI TUYỂN SINH VÀO LỚP 10 THPT
                          </span>
                          <span className="text-xs text-indigo-300">Thời gian làm bài: 90 phút</span>
                        </div>
                        <h2 className="text-xl md:text-2xl font-black text-amber-300 mt-1 uppercase tracking-wide">
                          {currentExam.title}
                        </h2>
                        <p className="text-xs md:text-sm text-slate-300 mt-1">
                          Cấu trúc ma trận chuẩn 14 câu (8 câu Trắc nghiệm 2.0đ + 6 câu Tự luận 8.0đ) • Bám sát 100% đề thi tuyển sinh mới nhất.
                        </p>
                      </div>

                      {/* KHỐI NÚT XUẤT FILE PDF TIMES NEW ROMAN 12PT */}
                      <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-2">
                        <button
                          onClick={() => handleExportMockExamPDF(false)}
                          disabled={isExportingMockPdf}
                          className="bg-indigo-600 hover:bg-indigo-500 text-white font-bold px-4 py-2.5 rounded-xl shadow text-xs md:text-sm flex items-center justify-center gap-2 transition"
                          title="Xuất đề thi chuẩn Times New Roman cỡ 12 để in phát học sinh"
                        >
                          <span>📄</span> Xuất PDF Đề thi
                        </button>
                        <button
                          onClick={() => handleExportMockExamPDF(true)}
                          disabled={isExportingMockPdf}
                          className="bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-4 py-2.5 rounded-xl shadow text-xs md:text-sm flex items-center justify-center gap-2 transition"
                          title="Xuất file PDF bao gồm cả Đề thi và Hướng dẫn giải chi tiết"
                        >
                          <span>📘</span> Xuất PDF Đề & Lời giải
                        </button>
                        <button
                          onClick={() => window.print()}
                          className="bg-slate-700 hover:bg-slate-600 text-white font-bold px-3.5 py-2.5 rounded-xl text-xs md:text-sm flex items-center justify-center gap-1.5 transition"
                          title="In trực tiếp bằng trình duyệt"
                        >
                          <span>🖨️</span> In ngay
                        </button>
                      </div>
                    </div>

                    {/* SELECTOR 6 ĐỀ THI MINH HỌA */}
                    <div>
                      <label className="block text-xs font-bold uppercase tracking-wider text-indigo-200 mb-2">
                        Chọn bộ đề thi thử (1 trong 6 đề minh họa):
                      </label>
                      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2">
                        {examKeys.map((k, idx) => {
                          const isSelected = selectedMockExamKey === k;
                          return (
                            <button
                              key={k}
                              onClick={() => {
                                setSelectedMockExamKey(k);
                                setMockMcUserAnswers({});
                                setMockMcSubmitted(false);
                                setShowMockSolution(false);
                              }}
                              className={`py-2.5 px-3 rounded-xl font-black text-xs transition border flex flex-col items-center justify-center gap-0.5 ${
                                isSelected
                                  ? "bg-amber-400 text-slate-950 border-amber-300 shadow-lg scale-105"
                                  : "bg-white/10 hover:bg-white/20 text-white border-white/10"
                              }`}
                            >
                              <span>ĐỀ SỐ 0{idx + 1}</span>
                              <span className={`text-[10px] font-medium ${isSelected ? "text-slate-800" : "text-slate-300"}`}>
                                14 câu • 90p
                              </span>
                            </button>
                          );
                        })}
                      </div>
                    </div>
                  </div>

                  {/* KHUNG THÔNG TIN THÍ SINH & NÚT BẬT TẮT ĐÁP ÁN */}
                  <div className="bg-white p-5 rounded-2xl shadow-sm border border-slate-200 flex flex-wrap justify-between items-center gap-4">
                    <div className="flex flex-wrap items-center gap-3">
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-bold text-slate-700">Thí sinh:</span>
                        <input
                          type="text"
                          placeholder="Họ và tên thí sinh..."
                          value={studentName}
                          onChange={(e) => setStudentName(e.target.value)}
                          className="px-3 py-1.5 text-xs border border-slate-300 rounded-lg outline-none focus:ring-2 focus:ring-indigo-500 w-48"
                        />
                      </div>
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-bold text-slate-700">Số báo danh:</span>
                        <input
                          type="text"
                          placeholder="SBD (VD: 1001)..."
                          defaultValue="SBD 1001"
                          className="px-3 py-1.5 text-xs border border-slate-300 rounded-lg outline-none focus:ring-2 focus:ring-indigo-500 w-32"
                        />
                      </div>
                    </div>

                    <div className="flex items-center gap-2">
                      <button
                        onClick={() => setShowMockSolution(!showMockSolution)}
                        className={`px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${
                          showMockSolution
                            ? "bg-amber-500 text-white shadow-sm"
                            : "bg-slate-100 hover:bg-slate-200 text-slate-700"
                        }`}
                      >
                        {showMockSolution ? "👁️ Ẩn Đáp án & Lời giải" : "💡 Hiện Đáp án & Lời giải chi tiết"}
                      </button>
                    </div>
                  </div>

                  {/* NỘI DUNG ĐỀ THI TRÊN GIAO DIỆN WEB */}
                  <div className="space-y-6">
                    {/* PHẦN I: TRẮC NGHIỆM */}
                    <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 space-y-4">
                      <div className="flex flex-wrap justify-between items-center border-b pb-3 gap-2">
                        <div>
                          <h3 className="text-base font-black text-indigo-950 uppercase">
                            I. PHẦN TRẮC NGHIỆM (2,0 điểm)
                          </h3>
                          <p className="text-xs text-slate-500 mt-0.5">
                            Trong mỗi câu hỏi từ câu 1 đến câu 8, hãy chọn phương án đúng duy nhất (mỗi câu đúng được 0,25 điểm).
                          </p>
                        </div>
                        {mockMcSubmitted && (
                          <div className="bg-emerald-50 text-emerald-800 border border-emerald-300 px-3.5 py-1.5 rounded-xl text-xs font-bold flex items-center gap-2">
                            <span>Kết quả trắc nghiệm:</span>
                            <span className="text-sm font-black text-emerald-700">{correctMcCount}/8 câu ({mcScore}đ)</span>
                          </div>
                        )}
                      </div>

                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {currentExam.part1.map((q) => {
                          const userAns = mockMcUserAnswers[q.id];
                          const isCorrect = userAns === q.answer;
                          return (
                            <div key={q.id} className="p-4 rounded-xl border border-slate-200 bg-slate-50/50 space-y-2.5">
                              <div className="font-bold text-xs md:text-sm text-slate-900 leading-relaxed">
                                <span className="text-indigo-700 font-black">Câu {q.id}:</span>{" "}
                                <MathView text={q.question} />
                              </div>
                              <div className="grid grid-cols-2 gap-2 text-xs">
                                {q.options.map((opt, oIdx) => {
                                  const optKey = String.fromCharCode(65 + oIdx);
                                  const isSelected = userAns === optKey;
                                  let btnStyle = "bg-white border-slate-200 text-slate-700 hover:bg-indigo-50";
                                  if (mockMcSubmitted || showMockSolution) {
                                    if (optKey === q.answer) {
                                      btnStyle = "bg-emerald-100 border-emerald-400 text-emerald-900 font-bold ring-1 ring-emerald-400";
                                    } else if (isSelected) {
                                      btnStyle = "bg-rose-100 border-rose-400 text-rose-900 font-bold";
                                    }
                                  } else if (isSelected) {
                                    btnStyle = "bg-indigo-600 text-white font-bold border-indigo-600 shadow-sm";
                                  }

                                  return (
                                    <button
                                      key={optKey}
                                      onClick={() => {
                                        if (!mockMcSubmitted) {
                                          setMockMcUserAnswers(prev => ({ ...prev, [q.id]: optKey }));
                                        }
                                      }}
                                      className={`p-2 rounded-lg border text-left transition flex items-center gap-1.5 ${btnStyle}`}
                                    >
                                      <MathView text={opt} />
                                    </button>
                                  );
                                })}
                              </div>
                              {(showMockSolution || mockMcSubmitted) && (
                                <div className="text-[11px] bg-indigo-50/80 p-2.5 rounded-lg border border-indigo-100 text-indigo-950 space-y-1">
                                  <div>
                                    <b className="text-indigo-800">Đáp án: {q.answer}</b>
                                  </div>
                                  <div className="text-slate-600 leading-relaxed">
                                    <MathView text={q.explanation} />
                                  </div>
                                </div>
                              )}
                            </div>
                          );
                        })}
                      </div>

                      <div className="flex justify-between items-center pt-2">
                        <button
                          onClick={() => {
                            setMockMcSubmitted(true);
                            showToast("success", `Đã chấm xong phần trắc nghiệm: ${correctMcCount}/8 câu đúng (${mcScore} điểm)!`);
                          }}
                          className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold px-4 py-2 rounded-xl text-xs shadow transition"
                        >
                          Kiểm tra kết quả Trắc nghiệm
                        </button>
                        {mockMcSubmitted && (
                          <button
                            onClick={() => {
                              setMockMcSubmitted(false);
                              setMockMcUserAnswers({});
                            }}
                            className="text-xs font-semibold text-slate-500 hover:text-slate-800"
                          >
                            Làm lại phần Trắc nghiệm
                          </button>
                        )}
                      </div>
                    </div>

                    {/* PHẦN II: TỰ LUẬN */}
                    <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 space-y-5">
                      <div className="border-b pb-3 flex justify-between items-center">
                        <div>
                          <h3 className="text-base font-black text-indigo-950 uppercase">
                            II. PHẦN TỰ LUẬN (8,0 điểm)
                          </h3>
                          <p className="text-xs text-slate-500 mt-0.5">
                            Thí sinh trình bày lời giải chi tiết vào tờ giấy thi (từ Câu 9 đến Câu 14).
                          </p>
                        </div>
                        <span className="text-xs font-bold bg-slate-100 px-3 py-1 rounded-full text-slate-700">
                          6 câu tự luận
                        </span>
                      </div>

                      <div className="space-y-6">
                        {currentExam.part2.map((q) => (
                          <div key={q.id} className="p-5 rounded-2xl border border-slate-200 bg-slate-50/40 space-y-3">
                            <div className="flex justify-between items-start gap-2">
                              <h4 className="font-bold text-sm md:text-base text-slate-900 leading-relaxed">
                                <span className="text-indigo-700 font-black">Câu {q.id} ({q.points.toFixed(1)} điểm).</span>
                              </h4>
                            </div>
                            <div className="text-xs md:text-sm text-slate-800 leading-relaxed font-serif text-[13pt]">
                              <MathView text={q.question} />
                            </div>

                            {/* BẬT HIỆN LỜI GIẢI CHI TIẾT KÈM BAREM ĐIỂM */}
                            {showMockSolution && (
                              <div className="mt-3 p-4 bg-emerald-50/70 border border-emerald-200 rounded-xl space-y-3">
                                <div className="font-black text-xs text-emerald-900 flex items-center gap-1.5 uppercase tracking-wider">
                                  <span>📘</span> Hướng dẫn giải chi tiết & Thang điểm:
                                </div>
                                <div className="text-xs text-slate-800 leading-relaxed space-y-2">
                                  <MathView text={q.solution} />
                                </div>
                                {q.rubric && q.rubric.length > 0 && (
                                  <div className="mt-2 border-t border-emerald-200 pt-2 space-y-1">
                                    <div className="text-[11px] font-bold text-emerald-950">Barem điểm chấm thi:</div>
                                    <div className="space-y-1">
                                      {q.rubric.map((r, rIdx) => (
                                        <div key={rIdx} className="text-[11px] text-slate-600 flex justify-between gap-2 border-b border-emerald-100 pb-1">
                                          <span>• {r.step}</span>
                                          <span className="font-bold text-emerald-800 shrink-0">+{r.points}đ</span>
                                        </div>
                                      ))}
                                    </div>
                                  </div>
                                )}
                              </div>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>

                  {/* ============================================================== */}
                  {/* CÁC CONTAINER PHỤC VỤ XUẤT FILE PDF & IN ẤN CHUẨN A4            */}
                  {/* Áp dụng phông chữ Times New Roman cỡ chữ 12pt                    */}
                  {/* ============================================================== */}

                  {/* 1. MẪU XUẤT ĐỀ THI (DÀNH CHO HỌC SINH LÀM BÀI) */}
                  <div
                    id="mock-exam-printable-paper"
                    className="hidden print:block pdf-exam-container bg-white p-8 border border-slate-300 rounded-2xl space-y-5"
                    style={{ fontFamily: "'Times New Roman', Times, serif", fontSize: "12pt" }}
                  >
                    {/* Header chuẩn Sở GD&ĐT */}
                    <div className="flex justify-between items-start border-b-2 border-black pb-3 text-center">
                      <div className="w-[45%] text-center">
                        <div className="font-bold text-sm tracking-wide uppercase">SỞ GIÁO DỤC VÀ ĐÀO TẠO</div>
                        <div className="font-bold text-base uppercase mt-0.5">ĐỀ THI CHÍNH THỨC</div>
                        <div className="inline-block border-2 border-black font-black px-4 py-0.5 mt-1 text-sm tracking-wider">
                          {currentExam.code}
                        </div>
                        <div className="text-[11pt] italic mt-1">(Đề thi gồm 14 câu, thời gian 90 phút)</div>
                      </div>
                      <div className="w-[55%] text-center">
                        <div className="font-bold text-sm uppercase">KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT</div>
                        <div className="font-bold text-sm">NĂM HỌC 2025 - 2026</div>
                        <div className="font-black text-base uppercase mt-0.5">Môn thi: TOÁN</div>
                        <div className="text-[11pt] italic">Thời gian làm bài: 90 phút (không kể thời gian phát đề)</div>
                        <div className="font-bold text-[11pt] text-indigo-900 mt-0.5">GIÁO VIÊN: PHAN ĐÌNH THUẤN</div>
                      </div>
                    </div>

                    {/* Khung thí sinh */}
                    <div className="border border-black p-2.5 text-[11pt] flex justify-between items-center">
                      <div>Họ và tên thí sinh: .........................................................................................................</div>
                      <div>Số báo danh: ..........................</div>
                    </div>

                    {/* I. Phần trắc nghiệm */}
                    <div className="space-y-3">
                      <div className="font-bold uppercase text-[12pt]">
                        I- PHẦN TRẮC NGHIỆM (2,0 điểm) <span className="font-normal italic normal-case">(Trong mỗi câu từ câu 1 đến câu 8, hãy viết chữ cái in hoa đứng trước phương án đúng duy nhất vào tờ giấy thi).</span>
                      </div>
                      <div className="space-y-2.5">
                        {currentExam.part1.map(q => (
                          <div key={q.id} className="text-[12pt] leading-relaxed">
                            <div className="font-bold">
                              Câu {q.id}. <span className="font-normal"><MathView text={q.question} /></span>
                            </div>
                            <div className="grid grid-cols-4 gap-2 pl-4 text-[12pt] mt-0.5">
                              {q.options.map((opt, idx) => (
                                <div key={idx}><MathView text={opt} /></div>
                              ))}
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>

                    {/* II. Phần tự luận */}
                    <div className="space-y-3 pt-2">
                      <div className="font-bold uppercase text-[12pt]">
                        II- PHẦN TỰ LUẬN (8,0 điểm) <span className="font-normal italic normal-case">(Thí sinh trình bày lời giải chi tiết vào tờ giấy thi).</span>
                      </div>
                      <div className="space-y-3">
                        {currentExam.part2.map(q => (
                          <div key={q.id} className="text-[12pt] leading-relaxed">
                            <span className="font-bold">Câu {q.id} ({q.points.toFixed(1)} điểm). </span>
                            <MathView text={q.question} />
                          </div>
                        ))}
                      </div>
                    </div>

                    {/* Footer đề thi */}
                    <div className="text-center font-bold text-[12pt] pt-4 border-t border-black">
                      ------------------ HẾT ------------------
                      <div className="text-[10pt] font-normal italic mt-0.5">Cán bộ coi thi không giải thích gì thêm.</div>
                    </div>
                  </div>

                  {/* 2. MẪU XUẤT ĐẦY ĐỦ ĐỀ THI & HƯỚNG DẪN GIẢI CHI TIẾT */}
                  <div
                    id="mock-exam-printable-full"
                    className="hidden print:block pdf-exam-container bg-white p-8 border border-slate-300 rounded-2xl space-y-6"
                    style={{ fontFamily: "'Times New Roman', Times, serif", fontSize: "12pt" }}
                  >
                    {/* Header */}
                    <div className="text-center border-b-2 border-black pb-3 space-y-1">
                      <div className="font-bold uppercase text-sm">KỲ THI THỬ TUYỂN SINH VÀO LỚP 10 THPT - NĂM HỌC 2025 - 2026</div>
                      <div className="font-black text-lg text-indigo-900 uppercase">ĐÁP ÁN VÀ HƯỚNG DẪN CHẤM CHI TIẾT MÔN TOÁN</div>
                      <div className="font-bold text-sm uppercase">{currentExam.title}</div>
                      <div className="text-xs italic">Người biên soạn: GV Phan Đình Thuấn • Thời gian: 90 phút • Thang điểm: 10.0</div>
                    </div>

                    {/* Bảng đáp án trắc nghiệm */}
                    <div className="space-y-2">
                      <div className="font-bold uppercase text-[12pt]">I. ĐÁP ÁN PHẦN TRẮC NGHIỆM (2,0 điểm - Mỗi câu 0,25đ)</div>
                      <table className="w-full border-collapse border border-black text-center text-[12pt]">
                        <thead>
                          <tr className="bg-slate-100">
                            {currentExam.part1.map(q => (
                              <th key={q.id} className="border border-black p-1.5 font-bold">Câu {q.id}</th>
                            ))}
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            {currentExam.part1.map(q => (
                              <td key={q.id} className="border border-black p-1.5 font-black text-indigo-900">{q.answer}</td>
                            ))}
                          </tr>
                        </tbody>
                      </table>
                    </div>

                    {/* Lời giải chi tiết phần tự luận */}
                    <div className="space-y-4 pt-2">
                      <div className="font-bold uppercase text-[12pt]">II. HƯỚNG DẪN GIẢI VÀ THANG ĐIỂM TỰ LUẬN (8,0 điểm)</div>
                      <div className="space-y-4">
                        {currentExam.part2.map(q => (
                          <div key={q.id} className="border border-slate-300 rounded-lg p-3.5 space-y-2 text-[12pt]">
                            <div className="font-bold text-indigo-950 border-b border-slate-200 pb-1">
                              Câu {q.id} ({q.points.toFixed(1)} điểm)
                            </div>
                            <div className="italic text-slate-700 text-[11pt]">
                              <MathView text={q.question} />
                            </div>
                            <div className="font-bold text-emerald-900 pt-1">Lời giải:</div>
                            <div className="leading-relaxed space-y-1">
                              <MathView text={q.solution} />
                            </div>
                            {q.rubric && (
                              <div className="mt-2 border-t border-slate-200 pt-1.5">
                                <div className="text-[11pt] font-bold text-slate-800">Barem chấm điểm:</div>
                                {q.rubric.map((rb, rIdx) => (
                                  <div key={rIdx} className="flex justify-between text-[11pt] text-slate-600 border-b border-slate-100 py-0.5">
                                    <span>- {rb.step}</span>
                                    <span className="font-bold text-emerald-800">+{rb.points}đ</span>
                                  </div>
                                ))}
                              </div>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>

                    <div className="text-center font-bold text-[12pt] pt-4 border-t border-black">
                      ------------------ HẾT HƯỚNG DẪN CHẤM ------------------
                    </div>
                  </div>
                </div>
              );
            })()}
"""

view_dashboard_marker = '{view === "dashboard" && ('
if 'MÀN HÌNH CHUYÊN BIỆT: THI THỬ VÀO LỚP 10' not in content:
    content = content.replace(view_dashboard_marker, view_mock_code + "\n\n            " + view_dashboard_marker, 1)
    print("✅ Đã chèn View chính: view === 'grade10_mock'")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("🎉 Hoàn tất cập nhật index.html thành công 100%!")
